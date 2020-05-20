#blood_analysis.py

def interface():
    print("My Blood Analysis Calculator")
    keep_running = True
    while keep_running:
        print("Options:")
        print("9-Quit")
        choice = input("Choose an option: ")
        if choice == '9':
            keep_running = False
        
if __name__ == "__main__":
    interface()