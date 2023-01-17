def contains_even_number(L) :
    for ele in L :
        if ele % 2 == 0 :
            print("list berisi bilangan genap")
            break

    else:
        print("lidt tidak berisi bilangan genap")


print("for list 1:")
contains_even_number([1, 9, 8])
print(" \nfor list 2:")
contains_even_number([1, 3, 5])
