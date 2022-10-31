# imports
from matplotlib import pyplot as plt, animation
from bubble_sort import bubblesort
from quick_sort import quicksort
from selection_sort import selectionsort

def visualize_matplotlib(A, method, sort_type):
	# creates a figure and subsequent subplots
	fig, ax = plt.subplots()
	
	# creates a generator object containing all
	# the states of the array while performing
	# sorting algorithm
	if method == 'bubble_sort':
		generator = bubblesort(A, sort_type)
		ax.set_title("Bubble Sort O(n\N{SUPERSCRIPT TWO})")
	elif method == 'selection_sort':
		generator = selectionsort(A, sort_type)
		ax.set_title("Selection Sort O(n\N{SUPERSCRIPT TWO})")
	
	elif method == 'quick_sort':
		generator = quicksort(A, 0, len(A) -1)
		ax.set_title("Quick Sort O(n*logn)")
	
	bar_sub = ax.bar(range(len(A)), A, align="edge")
	
	# sets the maximum limit for the x-axis
	ax.set_xlim(0, len(A))
	text = ax.text(0.02, 0.95, "", transform=ax.transAxes)
	iteration = [0]
	
	# helper function to update each frame in plot
	def update(A, rects, iteration):
		for rect, val in zip(rects, A):
			rect.set_height(val)
		iteration[0] += 1
		text.set_text(f"# of operations: {iteration[0]}")

	# creating animation object for rendering the iteration
	anim = animation.FuncAnimation(
		fig,
		func=update,
		fargs=(bar_sub, iteration),
		frames=generator,
		repeat=False,
		blit=False,
		#Задается задержка
		interval=25,
	)
	
	# for showing the animation on screen
	plt.show()
	plt.close()
