
def get_str():
  """get string input"""
  string=str(input('Enter the string : '))
  return string

def str_to_dict(str):
  """convert connect string to a dictionary"""
  '''for char in str:
    d[char]=d.get(char,0)+1'''
  d=dict()
  for l in str:
    l=l.split(';')
    for i in l:
      k,*v=i.split("=")
      d[k]=v
  return d

def dict_to_str(d):
  """convert a dictionary to connect string"""
  s=str()
  '''for key  in d:
    s+=key'''
  return s
  
def main():
    name = get_str()
    d = str_to_dict(name) # convert connect string to a dictionary
    print(d)
    cs = dict_to_str(d)
    print(cs)
  
if __name__ == '__main__':
    main()
