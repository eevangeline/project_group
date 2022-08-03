try:
    #importing api for currency conversion
    from api import exchange_rate
    from pathlib import Path
    import csv
#exception handling for import error in case we change name of keyword or have typos
except ImportError:
    print(f"Import keyword not found! Please check keyword.")
#creating lists to append extracted data into
list_overheads = []
list_values = []
try:
    #creating file path to access csv file
    fp = Path.cwd()/"csv_reports"/"Overheads.csv"
    #opening file to extract data using read mode
    with fp.open(mode="r", encoding="UTF-8" ) as file:
        reader = csv.reader(file)
        #using next() to skip first row consisting of headings
        next(reader)
        #appending category and overheads data separately into different lists
        for row in reader:
            list_overheads.append(f"{row[0].upper()}")
            list_values.append(float(row[1])* exchange_rate)
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
def overheads():
    """
    - This function is used to find the highest overhead category and its value.
    - When exeucted, the function will return the highest overhead category and its value.
    - This function does not require any parameter.
    """
    try:
    #using max() function to find the largest overhead value
    #using .index() function to extract the index value of the largest overhead value
        index = list_values.index(max(list_values))
        #return statement made to write into summary report easily
        return f"[HIGHEST OVERHEADS] {list_overheads[index]}: SGD{round(list_values[index],1)}"
    #exception handling for index in case index value from above is wrong
    except IndexError:
        print(f"Index sequence out of range. Check index value above! ")