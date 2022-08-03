try:
    from api import exchange_rate
    from pathlib import Path
    import csv
except ImportError:
    print(f"Import keyword not found! Please check keyword.")
list_overheads = []
list_values = []
try:
    fp = Path.cwd()/"csv_reports"/"Overheads.csv"
    with fp.open(mode="r", encoding="UTF-8" ) as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            list_overheads.append(f"{row[0].upper()}")
            list_values.append(float(row[1])* exchange_rate)
except FileNotFoundError:
    print(f"File not found! Please check file path.")
except TypeError:
    print(f"Wrong type! Please convert data extracted into float for multiplication.")
except IndexError:
        print(f"Index sequence out of range. Check index! Index should start from 0! ")
def overheads():
    index = list_values.index(max(list_values))
    return f"{list_overheads[index]}: SGD{round(list_values[index],1)}"