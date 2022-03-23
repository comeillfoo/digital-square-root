def main( N ):
    x = int(input())
    m = 1 << ( N - 2 )
    y = 0
    while ( m != 0 ):
        b = y | m
        y = y >> 1
        if x >= b:
            x = x - b
            y = y | m
        m = m >> 2

    print(y)

if __name__ == '__main__':
    main( 8 )
