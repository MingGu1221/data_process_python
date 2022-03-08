from matplotlib import pyplot as plt
import csv
import glob
from os.path import basename

# fig = plt.figure(dpi = 128, figsize=(10,6))                        #creat a new plot object
plt.title("ABC_Raman", fontsize = 16)
plt.xlabel("Wavelength cm^-1", fontsize = 16)
plt.ylabel("Raman Intensity", fontsize = 16)

files = sorted(glob.glob("C:\\Users\Ming\python\pythonProject\R*_*.txt"))   #list of files
print("processing raw files")
for file in files:
    filename = basename(file).rsplit('.', 1)[0]                                                         # each file in list of files
    print('\r'+ filename + "  ", flush = True)                                                              # progress information
    with open(file) as f:                                                                                #'with' will auto close after loop
        csvreader = csv.reader(f, delimiter = ",", quotechar='"')                                       #read into csv object
        for line in range(48):
            try:
                next (csvreader)                                                                       #without try and except; will stopiteration
            except StopIteration as err:
                break

        wavelength = []  # init lists在这里插入图片描述
        RamanIntensity = []
        newT = []
        count = 0
        for row in csvreader:
            list = row[0].split("\t")
            print(list[0])
            wavelength.append(float(list[0]))  # process each row
            RamanIntensity.append(float(list[1]))  # extract column
            newT.append(float(list[1]))
        plt.plot(wavelength, RamanIntensity, '-', label=filename)  # actual plot
        plt.legend()  # legend

print("Done processing " + str(len(files)) + " files.")  # final information
plt.show()  # present plot
plt.savefig('DIV.all' + '.png', dpi=300)

