import shutil, os, re

dateFormatOriginal = '0'
while dateFormatOriginal != '1' or '2' or '3':
    dateFormatOriginal = input('Choose date format to convert from: 1. MMDDYYYY 2. DDMMYYYY 3. YYYYMMDD \n')
    print(dateFormatOriginal)

dateFormatConvert = '0'
while dateFormatConvert != '1' or '2' or '3':
    dateFormatConvert = input('Choose date format to convert to: 1. MMDDYYYY 2. DDMMYYYY 3. YYYYMMDD \n')
    print(dateFormatConvert)


# Create a regex that matches american date format
americanDateFormat = re.compile(r"""
^(.*?) # gets any text before date format
((0|1)?\d)(-|/)? # matches month one or two digits
((0|1|2|3)?\d)(-|/)? # matches day
((19|20)\d\d) #four digits to match the year
(.*?)$
""", re.VERBOSE)

# Create a regex that matches Japanese date format
japanDateFormat = re.compile(r"""^(.*?) # gets any text before date format
((19|20)\d\d)(-|/)? # matches year
((0|1)?\d)(-|/)? # matches month
((0|1|2|3)?\d) # matches day
(.*?)$
""", re.VERBOSE)

# Create a regex that matches European date format
europeanDateFormat = re.compile(r"""^(.*?) # gets any text before date format
((0|1|2|3)?\d)(-|/)? # matches day
((0|1)?\d) (-|/)? # matches month
((19|20)\d\d) # matches year
(.*?)$
""", re.VERBOSE)

# Loop over files in working directory

if dateFormatOriginal == '1':
    print('American format')
    for americanFilename in os.listdir('.'):
        print(os.listdir('.'))
        mo = americanDateFormat.search(americanFilename)

        if mo is None:
            continue

        beforePart = mo.group(1)
        monthPart = mo.group(2)
        dayPart = mo.group(5)
        yearPart = mo.group(8)
        afterPart = mo.group(10)
        # get the different parts of the file name

        if dateFormatConvert == '2':

            europeanFileName = beforePart + dayPart + monthPart + yearPart + afterPart
            print('renaming %s to %s' % (americanFilename, europeanFileName))
            shutil.move(americanFilename, europeanFileName)

        if dateFormatConvert == '3':

            japaneseFileName = beforePart + yearPart + monthPart + dayPart + afterPart
            print('renaming %s to %s' % (americanFilename, japaneseFileName))
            shutil.move(americanFilename, japaneseFileName)


if dateFormatOriginal == '2':
    for europeanFileName in os.listdir('.'):
        mo = europeanDateFormat.search(europeanFileName)

        if mo is None:
            continue

        beforePart = mo.group(1)
        monthPart = mo.group(5)
        dayPart = mo.group(2)
        yearPart = mo.group(8)
        afterPart = mo.group(10)
        # get the different parts of the file name

        if dateFormatConvert == '1':

            americanFileName = beforePart + monthPart + dayPart + yearPart + afterPart
            print('renaming %s to %s' % (europeanFileName, americanFileName))
            shutil.move(europeanFileName, americanFileName)

        if dateFormatConvert == '3':

            japaneseFileName = beforePart + yearPart + monthPart + dayPart + afterPart
            print('renaming %s to %s' % (europeanFileName, japaneseFileName))
            shutil.move(europeanFileName, japaneseFileName)


if dateFormatOriginal == '3':
    for japaneseFileName in os.listdir('.'):
        mo = japanDateFormat.search(japaneseFileName)

        if mo is None:
            continue

        beforePart = mo.group(1)
        monthPart = mo.group(5)
        dayPart = mo.group(8)
        yearPart = mo.group(2)
        afterPart = mo.group(10)
        # get the different parts of the file name

        if dateFormatConvert == '1':

            americanFileName = beforePart + monthPart + dayPart + yearPart + afterPart
            print('renaming %s to %s' % (japaneseFileName, americanFileName))
            shutil.move(japaneseFileName, americanFileName)

        if dateFormatConvert == '2':

            europeanFileName = beforePart + dayPart + monthPart + yearPart + afterPart
            print('renaming %s to %s' % (japaneseFileName, japaneseFileName))
            shutil.move(japaneseFileName, europeanFileName)






