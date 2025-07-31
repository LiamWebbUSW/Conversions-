
# 🧰 Conversions

This repository contains a collection of Python scripts designed to assist with data structure transformation and cleanup — especially for converting and flattening data formats like `.proto`, `.bin`, and `.csv` into usable tabular forms.

These tools are particularly useful in handling GTFS real-time protobuf feeds, batch CSV merging, and fixing file suffixes.

---

## 📁 Contents

### 1. `proto2csv.py`
Converts `.bin` files containing GTFS real-time protobuf data into flattened `.csv` files.

- Parses `.bin` protobuf files using `gtfs_realtime_pb2`.
- Flattens nested entities for tabular export.
- Outputs new `.csv` files with the same filename (but `.csv` suffix).

📌 **Usage notes:**
- Requires `protobuf-to-dict` and `gtfs-realtime-bindings` Python libraries.
- Make sure the `.proto` schema (e.g., `gtfs_realtime.proto`) is available and compiled if not using prebuilt bindings.

---

### 2. `loop to change suffix.py`
Renames `.bin` files to `.csv` **only if** the file contents are already in CSV format (useful if `.bin` files were overwritten with CSV content accidentally).

📌 **What it does:**
- Checks the first line of each `.bin` file.
- If it looks like a CSV (e.g., starts with "id," or contains commas), it renames the file to `.csv`.

---

### 3. `combine_csv.py`
Combines multiple CSV files with a matching pattern into a single merged file.

- Searches for files in a target directory that match a specific naming pattern.
- Concatenates them into one DataFrame using `pandas`.
- Saves the result to a new output file.

📌 **Update path variables as needed** depending on your local setup.

---

## 🛠 Dependencies

Install required packages via pip:

```bash
pip install pandas protobuf protobuf-to-dict gtfs-realtime-bindings
```

---

## 📝 Usage

Each script is standalone and can be run using Python:

```bash
python proto2csv.py
python "loop to change suffix.py"
python combine_csv.py
```

Make sure to update hardcoded paths inside the scripts to match your local environment.

---

## 📌 Notes

- Scripts are designed to be modular and straightforward.
- File paths are currently hardcoded for convenience — refactor for CLI arguments or environment variables if needed.
- Useful for research, transport data manipulation, or any task involving raw GTFS or CSV batch processing.

---

## 📄 License

MIT License. See [LICENSE](LICENSE) file (if applicable).

---

## 💻 PowerShell Script: Automated BODS Data Download

This PowerShell script continuously fetches GTFS and SIRI data from the UK Department for Transport's BODS API.

### 🌐 Features
- Runs in an infinite loop, downloading real-time data every 20–40 seconds depending on time of day.
- During the day (00:01 to 23:59), it:
  - Downloads GTFS-RT feeds for South West and North East regions.
  - Converts `.json` GTFS files to `.csv` using `json2csv`.
  - Removes intermediate `.json` files.
- Outside those hours, it:
  - Downloads SIRI-VM and SIRI-SX XML feeds to predefined folders.

### 📁 Example Output Structure
- `D:/swoutputs/*.csv` — South West GTFS
- `D:/neoutputs/*.csv` — North East GTFS
- `D:/sirisw/*.xml`, `D:/sirine/*.xml`, `D:/sirisx/*.xml` — SIRI feeds

### ⚙️ Requirements
- [`gtfs-realtime`](https://pypi.org/project/gtfs-realtime-bindings/) CLI tool or similar downloader
- [`json2csv`](https://www.npmjs.com/package/json2csv) tool (Node.js CLI)

### 🚀 To Run

Save the script as `bods_downloader.ps1` and run it with:

```powershell
powershell -ExecutionPolicy Bypass -File bods_downloader.ps1
```

Make sure the output directories (`D:/swoutputs`, `D:/neoutputs`, etc.) exist before execution.
