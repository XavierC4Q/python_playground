import re

b1 = """1000.00!=

125 Market !=:125.45
126 Hardware =34.95
127 Video! 7.45
128 Book :14.32
129 Gasoline ::16.10
"""

b2="""1233.00
125 Hardware;! 24.8?;
123 Flowers 93.5
127 Meat 120.90
120 Picture 34.00
124 Gasoline 11.00
123 Photos;! 71.4?;
122 Picture 93.5
132 Tyres;! 19.00,?;
129 Stamps 13.6
129 Fruits{} 17.6
129 Market;! 128.00?;
121 Gasoline;! 13.6?;"""


"""
You are given a (small) check book as a - sometimes - cluttered (by non-alphanumeric characters) string:

"1000.00
125 Market 125.45
126 Hardware 34.95
127 Video 7.45
128 Book 14.32
129 Gasoline 16.10"
The first line shows the original balance. Each other line (when not blank) gives information: check number, category, check amount.

First you have to clean the lines keeping only letters, digits, dots and spaces.

Then return a report as a string (underscores show spaces -- don't put them in your solution. They are there so you can see them and how many of them you need to have):

"Original_Balance:_1000.00
125_Market_125.45_Balance_874.55
126_Hardware_34.95_Balance_839.60
127_Video_7.45_Balance_832.15
128_Book_14.32_Balance_817.83
129_Gasoline_16.10_Balance_801.73
Total_expense__198.27
Average_expense__39.65"
On each line of the report you have to add the new balance and then in the last two lines the total expense and the average expense. So as not to have a too long result string we don't ask for a properly formatted result.

Notes
It may happen that one (or more) line(s) is (are) blank.
Round to 2 decimals your results.
The line separator of results may depend on the language \n or \r\n. See examples in the "Sample tests".
"""



def balance(book):
        book = re.sub('[$!?;,{}:[\\]/()=-]', '' ,book)
        book = book.replace('*', '')
        book = book.replace('+', '')
        info = book.split()
        front = info.pop(0)
        total_float = float(front)
        total = str(total_float)
        if total[-2] == '.':
                total += '0'
        new_str = 'Original Balance: ' + total + '\r\n'
        spent = 0
        items = 0

        for i in range(0, len(info), 3):
                diff = round(total_float - float(info[i + 2]), 2)
                spent += float(info[i + 2])
                balance = str(diff)
                cost = info[i + 2]
                if balance[-2] == '.':
                        balance += '0'
                if cost[-2] == '.':
                        cost += '0'
                entry = info[i] + ' ' + info[i + 1] + ' ' + cost + ' Balance ' + balance + '\r\n'
                new_str += entry
                total_float = float(balance)
                items += 1
        
        total_expense = str(round(spent,2))
        average_expense = str(round(spent / items, 2))

        if total_expense[-2] == '.':
                total_expense += '0'
        if average_expense[-2] == '.':
                average_expense += '0'
        
        new_str = new_str + 'Total expense  ' + total_expense + '\r\n' + 'Average expense  ' + average_expense

        return new_str
        
print(balance(b1))