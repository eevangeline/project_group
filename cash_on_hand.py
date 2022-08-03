from api import exchange_rate
from pathlib import Path
import csv
list_coh = []
list_days = []
fp = Path.cwd()/"csv_reports"/"Cash on Hand.csv"
with fp.open(mode="r", encoding="UTF-8" ) as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        list_coh.append(float(row[1])*exchange_rate)
        list_days.append(float(row[0]))