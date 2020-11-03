def main():
    x, y = 10000, 100

    # conditional flow uses if, elif, else
    if ( x < y ):
        a = "x is less than y"
    elif ( x == y):
        a = "they are equal"
    else:
        a = "x is greater"

    print(a)

    # conditional statements let you use "a if C else b"
    s = "x is less than y" if( x<y) else "x is greater or equal to y"

    print(s)

if __name__ == "__main__":
    main()
