
def get_cs():
    """get string input"""
    string=str(input("Enter the any string:"))
    return string

def cs_to_lot(cs):
    """convert connected string to list of strings"""
    lst=list()
    for word in cs:
      lst.append(word)
    return lst

def lot_to_cs(lot):
    """convert list of strings to connected string"""
    str_word=''
    for word in lot:
      str_word+=word
    return str_word

def main():
    cs=get_cs()

    lot=cs_to_lot(cs)  # convert connect string to list of tuples
    print(lot)

    cs=lot_to_cs(lot)  # convert list of strings to connect string
    print(cs)


if __name__ == '__main__':
    main()
