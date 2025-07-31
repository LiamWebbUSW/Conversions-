from pathlib import Path

# Set your directory path here
folder = Path("C:/Users/j20ra/OneDrive - University of South Wales/06_21")

def is_probably_csv(file_path):
    """Check if file content starts like a CSV."""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            first_line = f.readline()
            return ',' in first_line or first_line.lower().strip().startswith("id")
    except:
        return False

# Loop through all .bin files
for file in folder.glob("*.bin"):
    if is_probably_csv(file):
        new_path = file.with_suffix(".csv")
        file.rename(new_path)
        print(f"✅ Renamed: {file.name} → {new_path.name}")
    else:
        print(f"⚠️ Skipped (not CSV): {file.name}")