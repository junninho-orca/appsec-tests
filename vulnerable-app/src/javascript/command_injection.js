const express = require('express');
const { exec } = require('child_process');

const app = express();

app.get('/network-health', (req, res) => {
  const { target } = req.query;

  // Vulnerable to command injection
  exec(`ping -c 1 ${target}`, (error, stdout, stderr) => {
    if (error) {
      console.error(`exec error: ${error}`);
      return res.status(500).send('Error executing command');
    }
    res.send(`<pre>${stdout}${stderr}</pre>`);
  });
});

app.listen(3000, () => {
  console.log('Server is running on port 3000');
}); 