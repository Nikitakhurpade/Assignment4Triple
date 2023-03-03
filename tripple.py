#Write a Python program to triple all numbers of a given list of integers. Use Python map.
#sample list: [1, 2, 3, 4, 5, 6, 7]
#Triple of list numbers:
#[3, 6, 9, 12, 15, 18, 21]

def triple(num):
    return int (num)*3
result= map(triple, input('Enter the list of integers : ').split(','))
print('Triple of all the numbers of entered list of integers : ',list(result))

