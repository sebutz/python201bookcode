# You will get an UnboundLocalError when running this script

def my_func(a, b):
    print(x)
    x = 5
    print(x)

if __name__ == '__main__':
    x = 10
    my_func(1, 2)
    print(x)