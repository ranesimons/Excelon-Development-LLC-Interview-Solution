if __name__ == '__main__':

    # Write a short program that prints each number from 1 to 100 on a new line. 
    # For each multiple of 3, print "Foo" instead of the number. 
    # For each multiple of 5, print "Bar" instead of the number.
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FooBar")
        elif i % 3 == 0:
            print("Foo")
        elif i % 5 == 0:
            print("Bar")
        else:
            print(i)
