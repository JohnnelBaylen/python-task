while True:

    word = input("Enter word : ")

    def Cvowel(word):

        vowels = "aeiou"
        count = 0

        for letter in word:
            if letter in vowels:
                count += 1
        return count

    print(Cvowel(word))