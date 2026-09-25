import sqlite3
import ListOperations
connectionDB = sqlite3.connect("iris_DB.db")

cursor = connectionDB.cursor()

fetchData = """select * from irisDB;"""

cursor.execute(fetchData)
irisData = cursor.fetchall()

sepalLengthList = []
sepalWidthList = []
petalLengthList = []
petalWidthList = []
for row in irisData:
    sepalLengthList.append(row[1])
    sepalWidthList.append(row[2])
    petalLengthList.append(row[3])
    petalWidthList.append(row[4])


print("operation,   sepalLength,       sepalWidth,         petalLength,        petalWidth")
print("mean:       ", ListOperations.calculateMean(sepalLengthList),"",ListOperations.calculateMean(sepalWidthList),"",ListOperations.calculateMean(petalLengthList),"",ListOperations.calculateMean(petalWidthList) )
print("median:     ", ListOperations.calculateMedian(sepalLengthList),"              ",ListOperations.calculateMedian(sepalWidthList),"               ",ListOperations.calculateMedian(petalLengthList),"               ",ListOperations.calculateMedian(petalWidthList) )
print("mode:       ", ListOperations.calculateMode(sepalLengthList),"              ",ListOperations.calculateMode(sepalWidthList),"               ",ListOperations.calculateMode(petalLengthList),"               ",ListOperations.calculateMode(petalWidthList) )
print("range:      ", ListOperations.calculateRange(sepalLengthList),ListOperations.calculateRange(sepalWidthList),"",ListOperations.calculateRange(petalLengthList),"               ",ListOperations.calculateRange(petalWidthList) )
print("")
print("frequency = [value, times it repeats]")
print("frequency for sepalLength:",ListOperations.calculateFrequency(sepalLengthList))
print("")
print("frequency for sepalWidth:",ListOperations.calculateFrequency(sepalWidthList))
print("")
print("frequency for petalLength:",ListOperations.calculateFrequency(petalLengthList))
print("")
print("frequency for petalWidth:",ListOperations.calculateFrequency(petalWidthList))


cursor.close()
connectionDB.close()
