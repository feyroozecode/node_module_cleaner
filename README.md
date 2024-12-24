# Node Modules Cleaner

A powerful command-line tool for finding and removing `node_modules` directories to free up disk space. This tool combines Python's efficient directory traversal with shell script's robust file handling.

## Features

- 🔍 Recursively finds all `node_modules` directories
- 📊 Calculates and displays size of each directory
- 💾 Shows total space that can be freed
- ✅ Provides dry-run option (Python script only)
- 🎨 Colored output for better readability
- 🔒 Safe deletion with confirmation prompt
- 🔄 Modular design with separate finder and cleaner components

## Installation

1. Clone this repository
2. Install Python dependencies:
```bash
pip install -r requirements.txt
```
3. Make the scripts executable:
```bash
chmod +x main.py node_cleaner.sh
```

## Usage

### Using the Shell Script (Recommended)

The shell script provides a complete solution for finding and removing node_modules:

```bash
./node_cleaner.sh
```

This will:
1. Search for all node_modules directories
2. Display each directory with its size
3. Show total space used
4. Ask for confirmation before deletion
5. Remove confirmed directories and show progress

### Using the Python Script

The Python script can be used independently for finding node_modules without deletion:

```bash
# Search in default directory (/Users/ahmad/dev/wb_projects)
./main.py

# Search in a specific directory
./main.py /path/to/search

# Output in JSON format (used by shell script)
./main.py --json-output
```

## Project Structure

- `main.py`: Python script for finding node_modules
  - Uses Click for CLI argument handling
  - Calculates directory sizes
  - Supports human-readable and JSON output
  - Default search path: `/Users/ahmad/dev/wb_projects`

- `node_cleaner.sh`: Shell script for handling deletion
  - Uses main.py for directory discovery
  - Handles user interaction
  - Provides colored output
  - Safe deletion with confirmation

- `requirements.txt`: Python dependencies
  - click: Command line interface creation
  - colorama: Cross-platform colored terminal output

## Safety Features

- ✋ Confirmation prompt before any deletion
- 🔍 Preview of what will be deleted
- 📝 Detailed logging of actions
- ⚠️ Error handling for failed deletions
- 🔒 Only targets exact 'node_modules' directory matches

## Dependencies

Python packages (from requirements.txt):
- click==8.1.7
- colorama==0.4.6

## Error Handling

The tool includes several safety measures:
- Validates directory existence before operations
- Handles permission errors gracefully
- Reports failed deletions without stopping the process
- Prevents accidental deletions with confirmation prompt

## Contributing

Feel free to submit issues and enhancement requests!
