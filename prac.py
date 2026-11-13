x = 90 # x is an variable here and 90 is the object which has it tyoe n vskue

x =90
u = x

x = 800

print(u)
print(x)


#  floor div 
print(10//3)
# -3.333  = 4 is in floor div

a = [1, 2]
b = [1, 2]
print(a==b)# elemen size is qwl so true
print(a is b)# values arent eql

try:
    x = int(input())
    print(10/x)

except ValueError:
    print("Try givin num")

except ZeroDivisionError:
    print("qhy 0 ?")

else:
    print("no exception occured")

finally:
    print("printing this no matter what")



    #  pandas has two data strucutre 1 series and 2 dataframe
    #  df.head() shows the first rows by def or given args
    # df.tail() shows the last element rows by def or given argd
    #  shape means Num of rows n col (2,3)
    # size mean num of total ele 
    #  dim means num of rows (2)
    #  doc string describes whats a func do print(f().__doc__)

    