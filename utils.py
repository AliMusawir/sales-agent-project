# utils.py

import csv
import os

def update_csv(lead_id, data, status):
    file_path = "leads.csv"
    fields = ["lead_id", "age", "country", "interest", "status"]
    exists = os.path.isfile(file_path)

    rows = []
    found = False

    if exists:
        with open(file_path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row["lead_id"] == lead_id:
                    row.update(data)
                    row["status"] = status
                    found = True
                rows.append(row)

    if not found:
        new_row = {
            "lead_id": lead_id,
            "age": data.get("age", ""),
            "country": data.get("country", ""),
            "interest": data.get("interest", ""),
            "status": status
        }
        rows.append(new_row)

    with open(file_path, "w", newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)
