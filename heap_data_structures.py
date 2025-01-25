import time
import random
import heapq

# Heapsort Implementation
def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heapsort(arr):
    n = len(arr)

    # Build max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extract elements from heap
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

# Quicksort Implementation
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

# Merge Sort Implementation
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

# Priority Queue Implementation
class Task:
    def __init__(self, task_id, priority, arrival_time, deadline):
        self.task_id = task_id
        self.priority = priority
        self.arrival_time = arrival_time
        self.deadline = deadline

    def __lt__(self, other):
        return self.priority < other.priority

class PriorityQueue:
    def __init__(self):
        self.heap = []

    def insert(self, task):
        heapq.heappush(self.heap, task)

    def extract_max(self):
        if self.is_empty():
            return None
        return heapq.heappop(self.heap)

    def is_empty(self):
        return len(self.heap) == 0

    def increase_priority(self, task_id, new_priority):
        for task in self.heap:
            if task.task_id == task_id:
                task.priority = new_priority
                heapq.heapify(self.heap)
                return True
        return False

# Timing and Testing Functions
def test_sorting_algorithms():
    sizes = [10, 100, 1000, 5000]
    distributions = {
        "Random": lambda size: random.sample(range(size * 10), size),
        "Sorted": lambda size: list(range(size)),
        "Reverse-Sorted": lambda size: list(range(size, 0, -1)),
    }
    results = []

    for size in sizes:
        for dist_name, dist_func in distributions.items():
            arr = dist_func(size)

            # Heapsort Timing
            arr_copy = arr[:]
            start = time.time()
            heapsort(arr_copy)
            heap_time = time.time() - start

            # Quicksort Timing
            arr_copy = arr[:]
            start = time.time()
            quicksort(arr_copy)
            quick_time = time.time() - start

            # Merge Sort Timing
            arr_copy = arr[:]
            start = time.time()
            merge_sort(arr_copy)
            merge_time = time.time() - start

            results.append((size, dist_name, heap_time, quick_time, merge_time))
            print(f"Size: {size}, {dist_name} - Heap: {heap_time:.4f}s, Quick: {quick_time:.4f}s, Merge: {merge_time:.4f}s")

    return results

def test_priority_queue():
    pq = PriorityQueue()
    tasks = [Task(i, random.randint(1, 100), i, i + 10) for i in range(10)]

    for task in tasks:
        pq.insert(task)

    print("\nPriority Queue (Max-Heap) Operations:")
    print("Tasks extracted in priority order:")
    while not pq.is_empty():
        task = pq.extract_max()
        print(f"Task ID: {task.task_id}, Priority: {task.priority}")

# Run Tests
if __name__ == "__main__":
    print("Testing Sorting Algorithms...\n")
    sorting_results = test_sorting_algorithms()

    print("\nTesting Priority Queue...\n")
    test_priority_queue()
