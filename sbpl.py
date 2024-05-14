import requests
from bs4 import BeautifulSoup
from prettytable import PrettyTable

combs = []
numbers = []
set_level = 1

def search_number(number):
    data = tmp = []
    url = f'https://calltracer.in/{number}-phone-call-tracking/'
    page = requests.get(url)

    if page.status_code == 404:
        tmp = [number, "-", "-", "-", "-", "-", "-", "-"]

    else:
        soup = BeautifulSoup(page.text,'html.parser')
        table = soup.find("table", class_="trace-details")
        rows = table.find_all('tr')
        
        for row in rows:
            cols = row.find_all('td')
            cols = [ele.text.strip() for ele in cols]
            data.append([ele for ele in cols if ele])

        # We are using 8/23 fields of data in list(data) to display in the final table
        if str(data[3][1]) == "Number Ported":
            tmp = [data[0][1], data[3][1],"-", data[4][1], data[5][1], data[7][1], "-", data[13][1]]
        else:
            tmp = [data[0][1], data[3][1], data[4][1], data[5][1], data[6][1], data[8][1], data[11][1], data[20][1]]

    numbers.append(tmp)

def combination(number, index, nextNum):
    global d, combs

    if (len(number) != 10):
        combs.append(number[:-1])
        number = number[1:]

    # Fast list
    if (set_level == 1):
        d = {"0":["0", "8"],"1": ["1"], "2":["2"], "3": ["3", "9", "8"], "4": ["4", "9"], "5": ["5", "3", "8"], "6": ["6", "8"], "7": ["7", "1"], "8":["8"], "9": ["9"]}

    # Exhaustive list
    elif (set_level == 2):
        d = {"0": ["0", "8"], "1": ["1", "7"], "2": ["2"], "3": ["3", "9", "8"], "4": ["4", "9"], "5":["5", "8", "3"], "6":["6", "8"], "7":["7", "1"], "8": ["8", "0", "3", "5", "6"], "9": ["9", "3"]}

    if (index == 10):
        combs.append("".join(nextNum))
        return

    val = number[index]
    for c in d[val]:
        nextNum[index] = c
        combination(number, index+1, nextNum)

def output():
    count = 0
    myTable = PrettyTable(["No", "Number", "SIM card", "State", "IMEI", "MAC addr", "IP addr", "Physical location", "Tracking No."])
    
    for i in numbers:
        myTable.add_row([count, numbers[count][0], numbers[count][1], numbers[count][2], numbers[count][3], numbers[count][4], numbers[count][5], numbers[count][6], numbers[count][7]])
        count += 1

    print(myTable)

def main():
    number = input("Enter a number: ")
    combination(number, 0, ["0","0","0","0","0","0","0","0","0","0"])
    for _ in combs:
        search_number(_)
    output()

if __name__ == '__main__':
    main()
