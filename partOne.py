def main():
    slow = input("Input: ") #ask for input stores it in slow
    myFunction(slow) #refer to myFunction function and complete task
    
def myFunction(text): #text instaed of slow as to not confuse program, text is just saying whatever information incoming
    print(f"Output: {text.replace(" ", "...")}") # formatt is str.replace(old, new) and print(f"") added here so we can see reults
main()

remove extra
