#RADIX SORT
data = [78, 90, 65, 97, 882, 360, 21, 9, 1, 36, 67, 99, 420, 510, 443, 38, 505, 123, 404, 45, 5, 300, 250, 220, 15, 5, 33, 256, 10, 20, 44, 421, 234, 42, 32, 37, 80, 0, 54, 14, 71, 19, 121, 96, 126, 84, 155, 110, 18, 76, 166, 2, 6, 51, 31, 59, 98, 55, 99, 280, 303, 16, 25, 321]
print('Sebelum di Radix Sort : ', data)
radixArray = [[], [], [], [], [], [], [], [], [], []]
maxVal = max(data)
exp = 1

while maxVal // exp > 0:

  while len(data) > 0:
    val = data.pop()
    radixIndex = (val // exp) % 10
    radixArray[radixIndex].append(val)

  for x in radixArray:
    while len(x) > 0:
      val = x.pop()
      data.append(val)

  exp *= 10

print('\nSetelah di Radix Sort : ', data)


#MERGE SORT
def mergeSort(arr):
  if len(arr) <= 1:
    return arr

  mid = len(arr) // 2
  leftHalf = arr[:mid]
  rightHalf = arr[mid:]

  sortedLeft = mergeSort(leftHalf)
  sortedRight = mergeSort(rightHalf)

  return merge(sortedLeft, sortedRight)

def merge(left, right):
  result = []
  i = j = 0

  while i < len(left) and j < len(right):
    if left[i] < right[j]:
      result.append(left[i])
      i += 1
    else:
      result.append(right[j])
      j += 1

  result.extend(left[i:])
  result.extend(right[j:])

  return result

data = [78, 90, 65, 97, 882, 360, 21, 9, 1, 36, 67, 99, 420, 510, 443, 38, 505, 123, 404, 45, 5, 300, 250, 220, 15, 5, 33, 256, 10, 20, 44, 421, 234, 42, 32, 37, 80, 0, 54, 14, 71, 19, 121, 96, 126, 84, 155, 110, 18, 76, 166, 2, 6, 51, 31, 59, 98, 55, 99, 280, 303, 16, 25, 321]
print('\nSebelum di Merge Sort : ', data)
a = mergeSort(data)
print('\nSetelah di Merge Sort : ', a)


#LINEAR SEARCH
def linearSearch(arr, targetVal):
  for i in range(len(arr)):
    if arr[i] == targetVal:
      return i, arr[i]
  return -1

data = [78, 90, 65, 97, 882, 360, 21, 9, 1, 36, 67, 99, 420, 510, 443, 38, 505, 123, 404, 45, 5, 300, 250, 220, 15, 5, 33, 256, 10, 20, 44, 421, 234, 42, 32, 37, 80, 0, 54, 14, 71, 19, 121, 96, 126, 84, 155, 110, 18, 76, 166, 2, 6, 51, 31, 59, 98, 55, 99, 280, 303, 16, 25, 321]
print('\nData = ',data)
angka = int(input('\nAngka berapa yang ingin dicari Linear Search? '))

result = linearSearch(data, angka)

if result != -1:
  print('Ada pada (indeks,value) : ', result)
else:
  print('Tidak ada')


#BINARY SEARCH
def binarySearch(arr, targetVal):
  left = 0
  right = len(arr) - 1

  while left <= right:
    mid = (left + right) // 2

    if arr[mid] == targetVal:
      return mid, arr[mid]

    if arr[mid] < targetVal:
      left = mid + 1
    else:
      right = mid - 1

  return -1

data = [78, 90, 65, 97, 882, 360, 21, 9, 1, 36, 67, 99, 420, 510, 443, 38, 505, 123, 404, 45, 5, 300, 250, 220, 15, 5, 33, 256, 10, 20, 44, 421, 234, 42, 32, 37, 80, 0, 54, 14, 71, 19, 121, 96, 126, 84, 155, 110, 18, 76, 166, 2, 6, 51, 31, 59, 98, 55, 99, 280, 303, 16, 25, 321]
print('\nData = ',data)
angka = int(input('\nAngka berapa yang ingin dicari dengan Binary Search? '))

result = linearSearch(data, angka)

if result != -1:
  print('Ada pada (indeks,value) : ', result)
else:
  print('Tidak ada')