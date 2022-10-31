# Cортировка выбором на Python

from helper_methods import swap

# selection_sort algorithm
def selectionsort(A, sort_type):
		
	for i in range(len(A)):
		Index = i
		for j in range(i,len(A)):
			if sort_type:
				if A[j] < A[Index]:
					Index = j
			else:
				if A[j] > A[Index]:
					Index = j
		swap(A, i, Index)
		print(A)
		yield A


# Cортировка выбором на C#
# Console.WriteLine("Введите кол-во элементов массива:");
# int n = Convert.ToInt32(Console.ReadLine());
# // Заполнение массива
# int[] array = new int[n];
# for (int i = 0; i < n; i++)
# {
#     Console.Write("Введите число: ");
#     array[i] = Convert.ToInt32(Console.ReadLine());
# }
# Console.WriteLine();
# Console.WriteLine("Начальный массив: [" + string.Join(", ", array) + "]");
# // Cортировка
# for (int i = 0; i < n - 1; i++)
# {
#     int MinIndex = i;
#     for (int j = i + 1; j < n; j++)
#     {
#         if (array[j] < array[MinIndex])
#             MinIndex = j; 
#     }
#     int temp;
#     temp = array[MinIndex];
#     array[MinIndex] = array[i];
#     array[i] = temp;
# }
# Console.WriteLine("Конечный массив: [" + string.Join(", ", array) + "]");