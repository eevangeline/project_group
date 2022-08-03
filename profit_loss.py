try:
    from api import exchange_rate
    from pathlib import Path
    import csv
except ImportError:
    print(f"Import keyword not found! Please check keyword.")
list_profitnloss = []
list_days = []
try:
    fp = Path.cwd()/"csv_reports"/"Profit and Loss.csv"
    with fp.open(mode="r", encoding="UTF-8" ) as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            list_profitnloss.append(float(row[4])*exchange_rate)
            list_days.append(int(row[0]))
except FileNotFoundError:
    print(f"File not found! Please check file path.")
except TypeError:
    print(f"Wrong type! Please convert data extracted into float for multiplication.")
except IndexError:
    print(f"Index sequence out of range. Check index! Index should start from 0! ")
def profitnloss():
    first = list_profitnloss[0]
    deficit = False
    days_deficit = []
    for x in range(len(list_profitnloss)-1):
        diff = list_profitnloss[x+1]-first
        if diff <0:
            days_deficit.append(f"[PROFIT DEFICIT] DAY: {list_days[x+1]}, AMOUNT: SGD{round(abs(diff),1)}")
            deficit = True
        first = list_profitnloss[x+1]
    if deficit == False:
        days_deficit.append(f"[NET PROFIT SURPLUS] NET PROFIT ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY.")
    return days_deficit
print(profitnloss())