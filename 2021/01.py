def main():
  depths = []
  with open('inputs/01.txt') as input_file:
    for line in input_file:
      depths.append(int(line))

  deeper = 0

  for i in range(len(depths)-1):
    if depths[i+1] > depths[i]:
      deeper = deeper+1

  return deeper

def main_p2():
  depths = []
  with open('inputs/01.txt') as input_file:
    for line in input_file:
      depths.append(int(line))

  deeper = 0

  for i in range(len(depths)-3):
    if (depths[i+1] + depths[i+2] + depths[i+3]) > (depths[i] + depths[i+1] + depths[i+2]):
      deeper = deeper+1

  return deeper


if __name__ == '__main__':
  result = main_p2()
  print(result)
