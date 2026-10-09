def analyze_marks():
    raw_input_str = input("Enter student marks separated by spaces (e.g., 78 35 92 45): ")
    marks = [int(x) for x in raw_input_str.split()]
    
    if not marks:
        print("No marks entered.\n")
        return
        
    highest = max(marks)
    lowest = min(marks)
    average = sum(marks) / len(marks)
    passed = sum(1 for m in marks if m >= 40)
    
    print(f"Highest: {highest} | Lowest: {lowest} | Average: {average:.2f} | Passed Students: {passed}\n")

# Call the function to run it
if __name__ == "__main__":
    analyze_marks()
