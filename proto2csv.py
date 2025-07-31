import json
import csv
import gtfs_realtime_pb2
from pathlib import Path
from protobuf_to_dict import protobuf_to_dict
# Path to folder containing .bin files
folder = Path("C:/Users/j20ra/OneDrive - University of South Wales/06_21")

def flatten(d, parent_key='', sep='.'):
    """Flattens nested dictionaries for CSV export."""
    items = []
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten(v, new_key, sep=sep).items())
        elif isinstance(v, list):
            items.append((new_key, json.dumps(v)))  # Convert list to JSON string zzzzzz
        else:
            items.append((new_key, v))
    return dict(items)

# Process all .bin files in the folder (when we store proto files could be a different storage file)
for file in folder.glob("*.bin"):
    try:
        # Read protobuf binary data
        with open(file, "rb") as f:
            data = f.read()

        # Parse using FeedMessage
        feed = gtfs_realtime_pb2.FeedMessage()
        feed.ParseFromString(data)

        # Convert to dict
        feed_dict = protobuf_to_dict(feed)

        # Grab the 'entity' list (each entity = 1 row)
        entities = feed_dict.get("entity", [])
        if not entities:
            print(f"⚠️ No entities in {file.name}")
            continue

        # Flatten each entity for CSV
        flat_rows = [flatten(entity) for entity in entities]

        # Get unique fieldnames across all rows
        fieldnames = sorted(set(k for row in flat_rows for k in row.keys()))

        csv_path = file.with_suffix(".csv") # without this suffix wont change so it will be a csv within a .bin file
        
        # Write CSV, overwriting the .bin file
        with open(csv_path, "w", newline="", encoding="utf-8") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(flat_rows)

        print(f"✅ Converted {file.name} to CSV")

    except Exception as e:
        print(f"❌ Failed to convert {file.name}: {e}")
        
        
        
#        from pathlib import Path

# # Set your directory path here
# folder = Path("C:/Users/j20ra/OneDrive - University of South Wales/06_21")

# def is_probably_csv(file_path):
#     """Check if file content starts like a CSV."""
#     try:
#         with open(file_path, "r", encoding="utf-8") as f:
#             first_line = f.readline()
#             return ',' in first_line or first_line.lower().strip().startswith("id")
#     except:
#         return False

# # Loop through all .bin files
# for file in folder.glob("*.bin"):
#     if is_probably_csv(file):
#         new_path = file.with_suffix(".csv")
#         file.rename(new_path)
#         print(f"✅ Renamed: {file.name} → {new_path.name}")
#     else:
#         print(f"⚠️ Skipped (not CSV): {file.name}")

## can use this to change file to csv if there is csv stored within i.e it will check to see if the content is csv then loop and change suffix 