#!/bin/bash

# Node Modules Cleaner
# This script works in conjunction with main.py to find and remove node_modules directories
# It provides a user-friendly interface with colored output and confirmation prompts
# 
# Features:
# - Uses main.py to find node_modules directories
# - Calculates and displays total space used
# - Colored output for better readability
# - Safe deletion with confirmation
# - Progress feedback during deletion
#
# Dependencies:
# - Python 3 with required packages (see requirements.txt)
# - bc command for floating-point arithmetic
# - main.py in the same directory

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${YELLOW}Searching for node_modules directories...${NC}"

# Initialize variables
declare -a paths
total_size=0

# Store the results in an array
# Format from main.py: "path|size"
while IFS='|' read -r path size; do
    if [ ! -z "$path" ]; then
        echo -e "${YELLOW}Found: ${path} (${size} MB)${NC}"
        paths+=("$path")
        total_size=$(echo "$total_size + $size" | bc)
    fi
done < <(python3 main.py --json-output)

# Check if any directories were found
if [ ${#paths[@]} -eq 0 ]; then
    echo -e "${GREEN}No node_modules directories found.${NC}"
    exit 0
fi

# Display total space and ask for confirmation
echo -e "\n${YELLOW}Total space used: ${total_size} MB${NC}"
echo -e "\n${RED}Do you want to remove these directories? (y/N)${NC}"
read -r response

# Process user response
if [[ "$response" =~ ^[Yy]$ ]]; then
    # Remove each directory and provide feedback
    for path in "${paths[@]}"; do
        echo -e "${YELLOW}Removing: $path${NC}"
        rm -rf "$path"
        if [ $? -eq 0 ]; then
            echo -e "${GREEN}Successfully removed: $path${NC}"
        else
            echo -e "${RED}Failed to remove: $path${NC}"
        fi
    done
    echo -e "\n${GREEN}Cleanup complete! Freed up approximately ${total_size} MB${NC}"
else
    echo -e "${YELLOW}Operation cancelled.${NC}"
fi
