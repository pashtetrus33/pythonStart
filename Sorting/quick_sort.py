# Быстрая сортировка на Python

from helper_methods import swap

# quicksort function
def quicksort(a, l, r):
	if l >= r:
		return
	x = a[l]
	j = l
	for i in range(l + 1, r + 1):
		if a[i] <= x:
			j += 1
			a[j], a[i] = a[i], a[j]
		yield a
	a[l], a[j]= a[j], a[l]
	yield a

	# yield from statement used to yield
	# the array after dividing
	yield from quicksort(a, l, j-1)
	yield from quicksort(a, j + 1, r)


# Быстрая сортировка на С#
# 1. arr = {1, 0, -6, 2, 5, 3, 2} 
# 2. pivot = arr[6]  (опорный элемент)
# 3. Вызвать шаги 1-2 для подмассива слева от pivot и справа от pivot

# int[] arr = { 0, -5, 2, 3, 5, 9, -1, 7 };
# QuickSort(arr, 0, arr.Length - 1);
# Console.Write($"Отсортированный массив {string.Join(", ", arr)}");

# static void QuickSort(int[] inputArray, int minIndex, int maxIndex)
# {
#     if (minIndex >= maxIndex) return;
#     int pivot = GetPivotIndex(inputArray, minIndex, maxIndex);
#     QuickSort(inputArray, minIndex, pivot - 1);
#     QuickSort(inputArray, pivot + 1, maxIndex);
#     return;
# }
# static int GetPivotIndex(int[] inputArray, int minIndex, int maxIndex)
# {
#     int pivotIndex = minIndex - 1;
#     for (int i = minIndex; i <= maxIndex; i++)
#     {
#         if (inputArray[i] < inputArray[maxIndex])
#         {
#             pivotIndex++;
#             Swap(inputArray, i, pivotIndex);
#         }
#     }
#     pivotIndex++;
#     Swap(inputArray, pivotIndex, maxIndex);
#     return pivotIndex;
# }
# static void Swap(int[] inputArray, int leftValue, int rightValue)
# {
#     int temp = inputArray[leftValue];
#     inputArray[leftValue] = inputArray[rightValue];
#     inputArray[rightValue] = temp;
# }