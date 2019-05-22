def is_leap(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True
year = int(input('請輸入西元年分: '))
if is_leap(year) == True:
	print('平年')
else:
	print('閨年')