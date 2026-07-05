# Python File Organizer

Automatically sorts any cluttered folder into clean, 
categorized subfolders based on file type. One click - 
instantly organized.

## What It Does

- Scans any folder on your computer
- Automatically detects file types by extension
- Creates category folders (Images, Documents, Videos, etc.)
- Moves every file to its correct folder instantly
- Renames duplicates automatically instead of overwriting
- Handles permission errors and locked files gracefully

## Why Use This

A cluttered Downloads folder with 500+ mixed files wastes 
time and creates confusion. This script organizes everything 
in seconds - a task that would take 30+ minutes manually.

## Requirements

- Python 3.x
- No external libraries needed (uses built-in os and shutil modules)

## How To Use

1. Clone this repository
2. Open `file_organizer.py`
3. Set your target folder path
4. Run the script:

```bash
python file_organizer.py
```

## Supported File Categories

| Category | File Types |  
|---|---|  
| Images | .jpg .jpeg .png .gif .bmp .svg .webp |  
| Documents | .pdf .docx .doc .txt .xlsx .csv .pptx |  
| Videos | .mp4 .mkv .avi .mov .wmv |  
| Audio | .mp3 .wav .aac .flac |  
| Archives | .zip .rar .7z .tar .gz |  
| Code | .py .js .html .css .json .xml |  
| Others | Everything else |  

## Error Handling

- Folder not found → clear error message, safe exit
- Duplicate files → auto-renamed with `_duplicate` suffix
- Files open in another program → skipped with warning
- Unexpected errors → logged clearly, script continues

## Customization

Easily extendable to:
- Add new file categories
- Schedule automatic runs (daily/weekly cleanup)
- Organize multiple folders in one run
- Generate a report of moved files

## License

MIT License - free to use and modify
