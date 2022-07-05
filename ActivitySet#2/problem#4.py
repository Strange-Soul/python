def get_string():
    """get string input"""
    string=str(input("Enter the string :"))
    return string

def str_to_lst(str):
    """convert connected string to list of strings"""
    l=[]  #l=list()
    for char in str:
      l.append(char)
    return l
  
def lst_to_str(lst):
    """convert list of strings to connected string"""
    str=''
    for i in lst:
      str+=i
    return str
print(f"Present Directory/__name__ == {__name__}")
def main():
    name=get_string()
    list=str_to_lst(name)
    string=lst_to_str(list)
    print(list)
    print(string)

if __name__ == '__main__':
    main()
