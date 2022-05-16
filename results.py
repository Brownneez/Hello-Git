#result for 1
def my_items(a,b):
   my_tuple=(a, b)
   return my_tuple


#result for 3
def of_numbers(my_tuple):
   counter = 0
   for item in my_tuple:
       if item % 2 == 1:
           counter+=1
   return counter

#result for 4
def my_char(my_tuple):
    for num in my_tuple:
        print(num)

#result for 5
def my_char(tumple,par):
   if par in tumple:
       return "true"
   else:
       return "false"

#result for 6
def my_char(tumple,par2):
   if par2 in tumple:
       return True
   else:
       return False
#result for 7
def my_tuple(tuple):
   for num in tuple:
       if len(tuple) == num:
           return True
       else:
           return False
#result for 8
def two_tuples(tuple1, tuple2):
   for same_vlaue in (two_tuples):
       count(same_vlaue)
       if same_vlaue>1:
           return True

#result for 9
def two_tuples(tuple1, tuple2):
    for same_vlaue in (two_tuples):
        count(same_vlaue)
        if same_vlaue > 1:
            if index(tuple1) == index(tuple2):
                return True

#result for 10
def checkTuple(my_num, my_tuple):
     counter = 0
     for i in my_tuple:
          if len(i) >= my_num:
                counter += 1
                return counter
#lists
#result for  1 -

def sumListElements (my_list):
    sum_elements= 0
    for i in my_list:
       sum_elements = sum_elements + i
    return sum_elements



#result for 2

def mul_list_elements (my_list):
    mul_elements = 1
    for i in my_list:
        mul_elements = mul_elements * i
    return mul_elements



# result for 3 - better name
def max_numbers(list_num):
    max_num = list_num[0]
    for i in list_num:
        if max_num < i:
            max_num = i
    return max_num

#result for 4 - better name

def max_numers(list_num):
    max_num = list_num[0]
    for i in list_num:
        if max_num < i:
            max_num = i
    return list_num.index(max_num)

#result for 5 -  better name

def my_list(num_list):
    for i in num_list:
        if i % 10 == 0:
            return i
    return -1

#result for 6

def count_six(my_list):
    counter = 0
    for i in my_list:
        if i == 6:
            counter += 1
    return counter

#result for 7

def count_strings(list_of_strings):
    counter = 0
    for i in list_of_strings:
        if len(i) == 4:
            counter += 1
    return counter

print(count_strings(["four", "five", "mm"]))



