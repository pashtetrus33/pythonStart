
from helper_methods import swap

# bubble_sort algorithm
def bubblesort(A, sort_type):
	swapped = True
	
	for i in range(len(A) - 1):
		if not swapped:
			return
		swapped = False
		
		for j in range(len(A) - 1 - i):
			if sort_type:
				if A[j] > A[j + 1]:
					swap(A, j, j + 1)
					swapped = True
			else:
				if A[j] < A[j + 1]:
					swap(A, j, j + 1)
					swapped = True
			print(A)
			yield A


# string[] array = new string[5];
# for (int i = 0; i < 5; i++)
# {
#     array[i] = Console.ReadLine();
# }

# Console.Write("[" + string.Join(", ", array) + "]");
# for (int i = 0; i < 4; i++)
# {
#     int MinIndex = i;
#     for (int j = i + 1; j < 5; j++)
#     {
#         if (array[j].Length < array[MinIndex].Length)
#             MinIndex = j; 
#     }
#     string temp;
#     temp = array[MinIndex];
#     array[MinIndex] = array[i];
#     array[i] = temp;
# }
# Console.WriteLine("Конечный массив: [" + string.Join(", ", array) + "]");