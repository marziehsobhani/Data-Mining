print("******************************************************************************************")

Sentence = input("Enter a string: ")
Alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
print("Your sentence has ",len(Sentence),"letter tottaly.\*")
for i in range(0,26):
    print(".........")
    print(Alphabet[i]," is: " ,Sentence.count(Alphabet[i]))

print("************ sobhani *Exercie1* Data-Mining ************")