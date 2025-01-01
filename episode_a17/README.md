# Episode 17 - Exporting your custom language to EXE

## Episode Timeline
1. Terminal
    - Install `pip install pyinstaller`
2. main.py
    - Import `argparse` classes
    - Set all current DEBUG flags to `False`
    - Create the `parse_arguments` function
    - Add the `PROD_DEBUG` flag
    - Implement the `__name__ == "__main__"` block
3. Terminal
    - Run command `pyinstaller --onefile --name lime --icon=assets/lime_icon.ico main.py`
    - CD into the `dist` directory for the exe location
    - Create a `main.lime` file and write some test code
    - Run the command: `lime main.lime`
    - Add `build/*` + `dist/*` if desired to `.gitignore`