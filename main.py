listToSort = [3,6,9,7,1,3,2,6]

for x in range(len(listToSort)):
  for index in range(len(listToSort)):
    huidigeGetal = listToSort[index]

    if index + 1 < len(listToSort):
      volgendGetal = listToSort[index + 1]
      if huidigeGetal > volgendGetal:
        listToSort[index] = volgendGetal
        listToSort[index + 1] = huidigeGetal

else:
  print(listToSort)