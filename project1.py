# 0.import the time module
import time
start_time = time.time()

# 1.generate a list with numbers from 1 to 20, name the list as list1
list1 = list(range(1, 21))

# #2.print the first 5 elements of list1
print(list1[:5])

# 3.replace the last entry of the list with 100, and print the whole
list1[len(list1) - 1] = 100
print(list1)

# 4.sort the list from the largest to the smallest elemnet. and print list again
list1.sort(reverse=True)
print(list1)

# 5.generate a new list with entries from 14 to 40 with step size 2, name it list2
list2 = list(range(14, 41, 2))

# 6. write a loop, dividing the first 10 entries of list2 by 5, keep the rest of
list3 = []
for x in list2[:10]:
    y = x / 5
    list3.append(y)
list3 = list3 + list2[10:]

#7. Given the dictionary hrbook, print the value associate with the key "emp2".
hrbook= {
    'emp1': {'name': 'John', 'salary': 7500},
    'emp2': {'name': 'Emma', 'salary': 8100},
    'emp3': {'name': 'Brad', 'salary': 6500}
    }
print(hrbook.get('emp2'))

#8. Add a new record to the hrbook
hrbook['emp4'] = {'name': 'Misty', 'salary': 7700}

# 9. Use loop and conditional branching to do the following:
for employee in hrbook:
    if hrbook[employee]['salary']<7000:
        hrbook[employee]['salary'] = 7000
    elif hrbook[employee]['salary']<8000:
        hrbook[employee]['salary'] = 8000
    else:
        hrbook[employee]['salary'] = 8200


# 10. time your work
# record the end time
end_time = time.time()
t = end_time-start_time
print("spent %s seconds to run this script" %t)
