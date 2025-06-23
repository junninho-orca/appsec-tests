package main

import (
	"database/sql"
	"fmt"
	"log"
	"net/http"

	_ "github.com/mattn/go-sqlite3"
)

func main() {
	db, err := sql.Open("sqlite3", "./users.db")
	if err != nil {
		log.Fatal(err)
	}
	defer db.Close()

	http.HandleFunc("/user", func(w http.ResponseWriter, r *http.Request) {
		userId := r.URL.Query().Get("id")

		// Vulnerable to SQL Injection
		query := fmt.Sprintf("SELECT name FROM users WHERE id = %s", userId)
		var name string
		err := db.QueryRow(query).Scan(&name)
		if err != nil {
			http.Error(w, "User not found", http.StatusNotFound)
			return
		}
		fmt.Fprintf(w, "User name is %s", name)
	})

	log.Fatal(http.ListenAndServe(":8080", nil))
} 