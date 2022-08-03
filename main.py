try:
    from api import statement
    from cash_on_hand import coh
    from profit_loss import profitnloss
    from overheads import overheads
    from pathlib import Path
    import csv
#exception handling for import error in case we change name of keyword or have typos
except ImportError:
    print(f"Import keyword not found! Please check keyword.")
fp = Path.cwd()/"summary_report.txt"
#creating text file to write summary report into
fp.touch()
#opening file to write summary report using write mode
print(fp.exists())
for data in coh():
    word = data
with fp.open(mode = "w", encoding="UTF-8") as file:
    file.write(f"{statement}\n{overheads()}\n")
    file.writelines(coh())
    file.writelines(profitnloss())