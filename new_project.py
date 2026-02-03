import csv

with open("emp.csv", "w", newline="") as fp:
    writer = csv.writer(fp)
    writer.writerow(["id", "name", "salary"])
    writer.writerow([1, "Om", 20000])
    writer.writerow([2, "Amit", 30000])