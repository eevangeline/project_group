from api import exchange_rate
from pathlib import Path
import csv
list_overheads = []
list_values = []
fp = Path.cwd()/"csv_reports"/"Overheads.csv"
with fp.open(mode="r", encoding="UTF-8" ) as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        list_overheads.append(f"{row[0].upper()}")
        list_values.append(float(row[1])* exchange_rate)

def overheads():
    index = list_values.index(max(list_values))
    return f"{list_overheads[index]}: SGD{round(list_values[index],1)}"