class VowelCount:

    def __init__ (self, text):
        self.text = text

    def count_vowels(self):
        vowels_list =[]
        vowels= ['a', 'e', 'i', 'o', 'u']
        for char in self.text.lower():
            if char in vowels:
                vowels_list.append(char)
        return len(vowels_list)

my_text = input("Please enter a sentence and I'll tell you how many vowels are in it: ")
my_text_vowels=VowelCount(my_text)
print(f'The number of vowels in your text is: {my_text_vowels.count_vowels()}')    
