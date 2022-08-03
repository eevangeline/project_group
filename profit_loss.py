from api import exchange_rate
from pathlib import Path
import csv
list_profitnloss = []
list_days = []
fp = Path.cwd()/"csv_reports"/"Profit and Loss.csv"
with fp.open(mode="r", encoding="UTF-8" ) as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        list_profitnloss.append(float(row[4])*exchange_rate)
        list_days.append(int(row[0]))