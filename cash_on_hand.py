try:
    #importing api for currency conversion
    from api import exchange_rate
    from pathlib import Path
    import csv
#exception handling for import error in case we change name of keyword or have typos
except ImportError:
    print(f"Import keyword not found! Please check keyword.")
list_coh = []
list_days = []
try:
    #creating file path to access csv file
    fp = Path.cwd()/"csv_reports"/"Cash on Hand.csv"
    #opening file to extract data using read mode
    with fp.open(mode="r", encoding="UTF-8" ) as file:
        reader = csv.reader(file)
        #using next() to skip first row consisting of headings
        next(reader)
        for row in reader:
        #appending day and cash on hand data separately into different lists
        #converting data into float to use exchange rate imported from api.py to change currency of cash on hand
            list_coh.append(float(row[1])*exchange_rate)
            list_days.append(float(row[0]))
#exception handling for wrong file path in case we type wrongly or change name of file,
#wrong type in case data was not converted to float 
#and index in case we started from 1 instead of 0 or counted wrongly
except FileNotFoundError:
    print(f"File not found! Please check file path.")
except TypeError:
    print(f"Wrong type! Please convert data extracted into float for multiplication.")
except IndexError:
    print(f"Index sequence out of range. Check index! Index should start from 0! ")
#creating a function
def coh():
    #create a variable to store first index from list extracted
    first = list_coh[0]
    #set deficit to False
    deficit = False
    #creating new list to append final data into
    days_deficit = []
    #creating a loop
    for x in range(len(list_coh)-1):
        diff = list_coh[x+1]-first
        if diff <0:
            days_deficit.append(f"[CASH ON HAND DEFICIT] DAY: {list_days[x+1]}, AMOUNT: SGD{round(abs(diff),1)}\n")
            #set deficit to True to stop the loop
            deficit = True
        first = list_coh[x+1]
    if deficit == False:
        days_deficit.append(f"[CASH ON HAND SURPLUS] CASH ON HAND FOR EACH DAY IS HIGHER THAN THE PREVIOUS DAY.\n")
    return days_deficit
print(coh())