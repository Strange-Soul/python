

def get_cs():
   """get string input"""
   str=input("Enter the string:")
   return str


def cs_to_lot(cs):
    """convert connected string to list of strings"""
    lst=list()
    for word in cs:
      lst.append(word)
    return lst

def main():
    cs = get_cs()
    lot = cs_to_lot(cs)
    print(lot)


if __name__ == '__main__':
    main()
