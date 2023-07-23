def bon(w):
    for i in range(len(w)-1):
        if w[i] == w[i+1]:
            return (ord(w[i]) - 96) * 4
secretCode = input("Enter secret code : ")
print(bon(secretCode))