<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Steghide Operations</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            max-width: 800px;
            margin: auto;
            padding: 20px;
        }
        h1, h2, h3 {
            color: #333;
            border-bottom: 1px solid #ccc;
            padding-bottom: 5px;
        }
        ul {
            list-style-type: disc;
            padding-left: 20px;
        }
        pre {
            background-color: #f4f4f4;
            padding: 10px;
            overflow-x: auto;
            border-radius: 5px;
        }
        code {
            font-family: Consolas, monospace;
            font-size: 14px;
        }
    </style>
</head>
<body>
    <h1>Steghide Operations</h1>

    <p>Steghide Operations is a bash script for performing various operations using the steghide tool. It allows users to embed, extract, and view information from files using steganography techniques.</p>

    <h2>Features</h2>

    <ul>
        <li><strong>Embed Data:</strong> Embed data into a file using steghide.</li>
        <li><strong>Extract Data:</strong> Extract hidden data from a file.</li>
        <li><strong>View Embedded Data Information:</strong> Display information about embedded data in a file.</li>
        <li><strong>User-friendly Interface:</strong> Simple command-line interface for interacting with steghide.</li>
    </ul>

    <h2>Usage</h2>

    <ol>
        <li><strong>Clone the repository:</strong></li>
        <pre><code>git clone https://github.com/yourusername/steghide-operations.git</code></pre>

        <li><strong>Navigate to the project directory:</strong></li>
        <pre><code>cd steghide-operations</code></pre>

        <li><strong>Make the script executable:</strong></li>
        <pre><code>chmod +x steghide_operations.sh</code></pre>

        <li><strong>Run the script:</strong></li>
        <pre><code>./steghide_operations.sh</code></pre>
    </ol>

    <h3>Steghide Options</h3>

    <p>The script prompts for different steghide operations:</p>

    <ul>
        <li><strong>Embed Data into a File:</strong> Embed data into a specified file.</li>
        <li><strong>Extract Data from a File:</strong> Extract hidden data from a specified file.</li>
        <li><strong>View Embedded Data Information:</strong> Display information about embedded data in a specified file.</li>
        <li><strong>Exit:</strong> Exit the steghide operations.</li>
    </ul>

    <h2>Requirements</h2>

    <p>The script requires the following dependencies:</p>

    <pre><code>keyboard
pyperclip</code></pre>

    <h2>Installation</h2>

    <p>Install the required libraries using the provided <code>requirements.txt</code> file:</p>

    <pre><code>pip install -r requirements.txt</code></pre>

    <h2>Notes</h2>

    <ul>
        <li>Ensure that the script is executed in an environment where steghide is properly installed and accessible via the command line.</li>
        <li>Adjust paths and filenames as necessary to suit your specific use case.</li>
    </ul>
</body>
</html>
