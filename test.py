def pyramid(n):

    for y in range(n+1):
        for x in range(2*n+1):
            if -y<=x-n and y>=x-n:
                print('*',end='')
            else:
                print(end=' ')
        print()

def inversePyramid(n):
    for y in range(1,n+1):
        for x in range(2*n+1):
            if y <=  x and -y >= x - 2*n:
                print('*',end='')
            else:
                print(end=' ')
        print()
pyramid(5)
inversePyramid(5)