

def get_str():
  """get string input"""
  string=str(input('Enter the string : '))
  return string

def str_to_dict(str):
  """convert connect string to a dictionary"""
  d=dict()
  for char in str:
    d[char]=d.get(char,0)+1
  return d

def dict_to_str(d):
  """convert a dictionary to connect string"""
  s=''
  for key in d.keys():
    s+=key
  return s
  
def main():
    name = get_str()

    d = str_to_dict(name) # convert connect string to a dictionary
    print(d)

    cs = dict_to_str(d)
    print(cs)


if __name__ == '__main__':
    main()
