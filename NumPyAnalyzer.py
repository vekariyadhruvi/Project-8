import numpy as np

class DataAnalytics:
    
    # Constructor
    def __init__(self):
        self.__arr = None

    # Class and Static method
    @classmethod
    def info(cls):
        print("NumPy Analyzer Class")

    @staticmethod
    def greet():
        print("---- Welcome to the NumPy Analyzer! ----")

    # Defining Private methods
    def __dot(self, arr2):
        return np.dot(self.__arr, arr2)

    def __matmul(self, arr2):
        return np.matmul(self.__arr, arr2)

    def __corr(self, arr2):
        return np.corrcoef(self.__arr, arr2)

    # Array Management
    def array_menu(self):
        print("\nSelect the type of array to create:")
        print("1. 1D Array")
        print("2. 2D Array")
        print("3. 3D Array")

        ch = int(input("Enter choice: "))
        if ch == 1:
            data = list(map(int, input("Enter elements: ").split()))
            self.__arr = np.array(data)

        elif ch == 2:
            r = int(input("Rows: "))
            c = int(input("Cols: "))
            print(f"Enter {r * c} elements total:")
            data = list(map(int, input().split()))
            self.__arr = np.array(data).reshape(r, c)

        elif ch == 3:
            l = int(input("Layers: "))
            r = int(input("Rows: "))
            c = int(input("Cols: "))
            print(f"Enter {l * r * c} elements total:")
            data = list(map(int, input().split()))
            self.__arr = np.array(data).reshape(l, r, c)

        else:
            print("Invalid choice!")
            return

        print("Array created:\n", self.__arr)
        
        # Indexing and Slicing
        while True:
            print("\nChoose an operation:")
            print("\n1. Indexing\n2. Slicing\n3. Back")
            op = int(input("Enter choice: "))

            if op == 1:
                try:
                    # 1D indexing
                    if self.__arr.ndim == 1:
                        i = int(input("Enter index: "))
                        print(f"Element at index {i}: ",self.__arr[i])

                    # 2D indexing
                    elif self.__arr.ndim == 2:
                        i = int(input("Enter row index: "))
                        j = int(input("Enter column index: "))
                        print(f"Element: ",self.__arr[i, j])
                        
                    # 3D indexing
                    elif self.__arr.ndim == 3:
                        l = int(input("Enter layer index: "))
                        i = int(input("Enter row index: "))
                        j = int(input("Enter column index: "))
                        print(f"Element: ",self.__arr[l, i, j])

                except:
                    print("Invalid index!")

            elif op == 2:
                try:
                    if self.__arr.ndim == 1:
                        s = int(input("Enter start index: "))
                        e = int(input("Enter end index: "))
                        print("Sliced Array:\n", self.__arr[s:e])

                    elif self.__arr.ndim == 2:
                        r = input("Enter row range (start:end): ")
                        c = input("Enter column range (start:end): ")

                        r1, r2 = map(int, r.split(":"))
                        c1, c2 = map(int, c.split(":"))

                        print("Sliced Array:\n", self.__arr[r1:r2, c1:c2])

                    elif self.__arr.ndim == 3:
                        l = input("Enter layer range(start:end): ")
                        r = input("Enter row range(start:end): ")
                        c = input("Enter column range(start:end): ")

                        l1, l2 = map(int, l.split(":"))
                        r1, r2 = map(int, r.split(":"))
                        c1, c2 = map(int, c.split(":"))

                        print("Sliced Array:\n", self.__arr[l1:l2, r1:r2, c1:c2])

                except:
                    print("Invalid slicing input!")

            elif op == 3:
                break
    
    # Mathematical Operations
    def math_menu(self):
        while True:
            print("Choose a Mathematical Operation")
            print("\n1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5. Dot Product\n6. Matrix Multiplication")
        
            ch = int(input("Enter choice: "))
            data = list(map(int, input("Enter same-size array elements: ").split()))
            arr2 = np.array(data).reshape(self.__arr.shape)

            print("Original Array:\n",self.__arr)
            print("Second Array:\n",arr2)
        
            if ch == 1:
                print("Addition:\n",self.__arr + arr2)
            elif ch == 2:
                print("Subtraction:\n",self.__arr - arr2)
            elif ch == 3:
                print("Multiplication:\n",self.__arr * arr2)
            elif ch == 4:
                print("Division:\n",self.__arr / arr2)
            elif ch == 5:
                print("Dot Product:\n", self.__dot(arr2))
            elif ch == 6:
                print("Matrix Multiplication:\n", self.__matmul(arr2))
            else:
                break

    # Combine & Split Arrays
    def combine_split(self):
        print("Choose an option:")
        print("\n1. Combine\n2. Split")
        ch = int(input("Enter choice: "))

        if ch == 1:
            data = list(map(int, input("Enter second array elements: ").split()))
            arr2 = np.array(data).reshape(self.__arr.shape)
            print("Original Array:\n",self.__arr)
            print("Second Array:\n",arr2)
            print("After combining:\n", np.concatenate((self.__arr, arr2)))

        elif ch == 2:
            n = int(input("Enter parts: "))
            print("After splitting:\n",np.array_split(self.__arr, n))

    # Search, Sort or Filter Arrays
    def search_sort_filter(self):
        print("Choose an option:")
        print("\n1. Search\n2. Sort\n3. Filter")
        ch = int(input("Enter choice: "))

        if ch == 1:
            x = int(input("Enter value: "))
            print(np.where(self.__arr == x))

        elif ch == 2:
            print("Original Array:\n",self.__arr)
            print("Array in Ascending order:\n", np.sort(self.__arr))
            print("Array in Descending order:\n", np.sort(self.__arr)[::-1])

        elif ch == 3:
            x = int(input("Array should be greater than: "))
            print(self.__arr[self.__arr > x])

    # Aggregates And Statistics
    def aggregate_stats(self):
        print("Choose an option:")
        print("\n1. Aggregate\n2. Statistics\n3. Correlation Coefficient")
        ch = int(input("Enter choice: "))

        if ch == 1:
            print("Sum:", np.sum(self.__arr))
            print("Mean:", np.mean(self.__arr))
            print("Median:", np.median(self.__arr))
            print("Std Dev:", np.std(self.__arr))
            print("Variance:", np.var(self.__arr))

        elif ch == 2:
            print("Min:", np.min(self.__arr))
            print("Max:", np.max(self.__arr))
            p = int(input("Percentile: "))
            print(np.percentile(self.__arr, p))

        elif ch == 3:
            data = list(map(int, input("Enter second array: ").split()))
            arr2 = np.array(data).reshape(self.__arr.shape)
            print("Correlation:\n", self.__corr(arr2))

obj = DataAnalytics()

DataAnalytics.info()
DataAnalytics.greet()

while True:
    print("-*-"*10 +"\nChoose an option:")
    print("1. Create a NumPy Array")
    print("2. Perform Mathematical Operations")
    print("3. Combine or Split Arrays")
    print("4. Search, Sort, or Filter Arrays")
    print("5. Compute Aggregates and Statistics")
    print("6. Exit\n"+"-*-"*10)

    choice = int(input("\nEnter your choice: "))

    if choice == 1:
        obj.array_menu()
        print("="*50)
    elif choice == 2:
        obj.math_menu()
        print("="*50)
    elif choice == 3:
        obj.combine_split()
        print("="*50)
    elif choice == 4:
        obj.search_sort_filter()
        print("="*50)
    elif choice == 5:
        obj.aggregate_stats()
        print("="*50)
    elif choice == 6:
        print("-"*25+"\nThank you for using the NumPy Analyzer! Goodbye!\n"+"-"*25)
        break
    else:
        print("\nInvalid choice. Please choose again!")