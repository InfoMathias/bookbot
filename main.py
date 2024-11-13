def main():

    words = 0
    charDict = {}
    bookPath = 'books/frankenstein.txt'

    with open(bookPath) as f:
        file_contents = f.read()
        words = countWords(file_contents)
        charDict = countCharacters(file_contents)
        printReport(bookPath, words, charDict)
        

def countWords(content):
    return len(content.split())

def countCharacters(content):
    chars = list(content)
    charDict = {}
    for char in chars:
        charDict[char.lower()] = charDict[char.lower()] + 1 if char.lower() in charDict else 1
    
    return charDict

def printReport(bookPath, words, charDict):
    print(f'--- Begin report of {bookPath} ---')
    print (f'{words} words found in the document \n')

    for char in charDict:
        charCount = charDict[char]
        if char == '\n':
            print(f"The '\\n' character was found {charCount} times")
        else:
            print(f"The '{char}' character was found {charCount} times")
    
    print('--- End report ---')


main()