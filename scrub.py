import re
from pathlib import Path
from datetime import datetime, timedelta
import pandas as pd
import arrow
import datetime
import time
import path
import samplePaths
def get_data(file):
    directory = file
    files = Path(directory).glob('*')
    lineArr = []
    count = 0
    fullDayTrial = ""
    fileCount = 0
    for fileName in files:
        openFile = open(fileName, "r")
        lines = openFile.readlines()
        for line in lines:
            result = re.findall(samplePaths.grabSampleRegexPath(), line) #grab the date and number of gallons
            if(result != [] and count < 1):
                (Day, gallons) = result[0]# result ouputs like [('...', '...')] so this unpacks it and assigns it
                fullDayTrial = arrow.get(Day, 'D-MMM-YY').format('YYYY-MM-DD')#re-format the date so that you can use datetime properties on it
                input_date = datetime.datetime.strptime(fullDayTrial, "%Y-%m-%d")
                newDate = input_date - timedelta(days=1)#subtract a day
                newDate = newDate.strftime('%d-%b-%y') #re-format the new date to reuired output
                lineArr.append({"Day": newDate, "Gallons": gallons})#adding to dictonary
                count += 1
            result = []
        result = []
        fileCount += 1
        count = 0 #reset for every file
    return lineArr

def export(data):
    for i in data:
        df = pd.DataFrame(i)
        df.to_csv("readings_summary_new.csv")
    # fd = pd.read_csv("readings_summary_new.csv")
    # print(fd.dtypes)

if __name__ == '__main__':
    start = time.time()
    print("start timer")
    data = get_data(samplePaths.getSampleFile())
    export(data)
    
    print("done. it took ", time.time()-start, " to run")
