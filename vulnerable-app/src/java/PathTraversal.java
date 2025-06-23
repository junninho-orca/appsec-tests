import java.io.File;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;

public class PathTraversal {

    public String readFile(String fileName) throws IOException {
        // Vulnerable to path traversal
        File file = new File("public/" + fileName);
        return new String(Files.readAllBytes(file.toPath()));
    }
} 