const express = require('express');
const { exec } = require('child_process');
const path = require('path');

const app = express();
const port = 3000;

// Serve static files (HTML, CSS, JS) from the current directory
app.use(express.static(path.join(__dirname)));

// Endpoint to run the Python script
app.get('/run-python', (req, res) => {
    // Path to your Python script
    const pythonScriptPath = path.join(__dirname, 'open_blender.py');
    
    // Execute the Python script
    exec(`python3 ${pythonScriptPath}`, (error, stdout, stderr) => {
        if (error) {
            console.error(`exec error: ${error}`);
            return res.status(500).json({ message: 'Failed to run Python script', error: stderr });
        }
        
        // Successful execution of the script
        console.log(stdout);
        res.json({ message: 'Blender file opened successfully!' });
    });
});

// Start the server
app.listen(port, () => {
    console.log(`Server running at http://localhost:${port}`);
});
