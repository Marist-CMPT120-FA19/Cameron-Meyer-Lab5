def main ():
    sentence= input("Please enter a sentence: ").lower()
    num=len(sentence)
    print("The number of characters in your sentence is: ", num)
    wcount=len(sentence.split())
    print("The number of words is: ", wcount)
    average= float(num/wcount)
    print("The average word length is: ", average)

main()
