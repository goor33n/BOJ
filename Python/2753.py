year = int(input())

# if year % 4 == 0: #만약 4의 배수다
#     if year % 100 != 0: #만약 100의 배수다
#         print('1') #윤년
#     elif year % 400 == 0: #아니면 400의 배수다
#         print('1') #윤년
#     else: #아니다
#         print('0') #윤년아님
# else: #다 아니다 
#     print('0') #윤년아님
if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    print(1)
else:
    print(0)