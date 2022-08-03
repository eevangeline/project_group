try:
    from api import exchange_rate
    from pathlib import Path
    import csv
except ImportError:
    print(f"Import keyword not found! Please check keyword.")
list_coh = []
list_days = []
try:
    fp = Path.cwd()/"csv_reports"/"Cash on Hand.csv"
    with fp.open(mode="r", encoding="UTF-8" ) as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            list_coh.append(float(row[1])*exchange_rate)
            list_days.append(float(row[0]))
except FileNotFoundError:
    print(f"File not found! Please check file path.")
except TypeError:
    print(f"Wrong type! Please convert data extracted into float for multiplication.")
except IndexError:
    print(f"Index sequence out of range. Check index! Index should start from 0! ")
def coh():
    first = list_coh[0]
    deficit = False
    days_deficit = []
    for x in range(len(list_coh)-1):
        diff = list_coh[x+1]-first
        if diff <0:
            days_deficit.append(f"[CASH ON HAND DEFICIT] DAY: {list_days[x+1]}, AMOUNT: SGD{round(abs(diff),1)}\n")
            deficit = True
        first = list_coh[x+1]
    if deficit == False:
        days_deficit.append(f"[CASH ON HAND SURPLUS] CASH ON HAND FOR EACH DAY IS HIGHER THAN THE PREVIOUS DAY.\n")
    return days_deficit
print(coh())