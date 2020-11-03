#
# Example file for working with loops
#

def main():
  x = 0

  # define a while loop
  while (x < 5 ):
    print (x)

    x = x+1

  # # define a for loop
  for x in range( 5, 11):
    print (x)

  # # use a for loop over a collection
  days = ["Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag"]
  for d in days :
    print (d)
  
  # use the break and continue statements
  for b in range ( 1, 10):
    if( b == 7 ): break
    print (b)

  for y in range ( 1, 10):
    if ( y % 2 == 0) : continue
    print (y)

  #using the enumerate() function to get index 
  days = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
  for i, d in enumerate(days):
    print(d,i)

  
if __name__ == "__main__":
  main()
