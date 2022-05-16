def input_two_numbers():
  n=input("Enter a Number to add: ")
  return n
  
def add(a, b):
    return a+b

def output(a, b, sum):
    print("Addition of {%d} and {%d} is :",a,b,sum)

def main():
   
    sum = add(a, b)
    output(a, b, sum)

a= int(input_two_numbers())
b=int(input_two_numbers())
if __name__ == '__main__':

  main()
