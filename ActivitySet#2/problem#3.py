

def get_cs():
   """get string input"""
   words=input("Enter the string:")
   return words


def cs_to_lot(cs):
    """convert connected string to list of strings"""
    lst=list()
    for word in words:
      lst.append(word)
      return lst

def main():
    cs = get_cs()
    lot = cs_to_lot(cs)
    print(lot)


if __name__ == '__main__':
    main()
