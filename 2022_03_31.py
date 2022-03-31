#1
price_list = [32100, 32150, 32000, 32500]
for i in range(len(price_list)):
    print(0 + i, price_list[i])

#2
price_list = [32100, 32150, 32000, 32500]
for i in range(1, 4):
    print(90 + 10 * i, price_list[i])

#3
for x in range(2002, 2051, 4) :
    print (x)

#4
for num in range(10) :
    print(num / 10)

#5
ticker = "btc_krw"
ticker1 = ticker.upper()
print(ticker1)

#6
file_name = "보고서.xlsx"
file_name.endswith("xlsx")
if file_name.endswith("xlsx"):
    print('It end with "xlsx"')

if not file_name.endswith("xlsx"):
    print('It does not end with "xlsx"')

#7
a = "hello world"
r = a.split()
print(f'a.split     :{r}')

#8
date = "2020-05-01"
r = date.split("-")
print(f'date.split     :{r}')

#9
상장주식수 = "5,969,782,550"
컴마제거 = 상장주식수.replace(",", "")
정수타입 = int(컴마제거)
print(정수타입)

#10
a = "hello world"
r = a.split()
print(f'a.split     :{r}')

#11
price = ['20180728', 100, 130, 140, 150, 160, 170]
print(price[1:])

#12
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(nums[1::2])

#13
리스트 = [3, 100, 23, 44]
for 변수 in 리스트:
  if 변수 % 3 == 0:
    print(변수)