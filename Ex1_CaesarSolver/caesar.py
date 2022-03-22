from langdetect import detect, detect_langs, DetectorFactory

# Szyfr Cezara działający dla małych i dużych liter, niezmieniający pozostałych znaków
def caesarCipher(text, shift):
    encryptedText = ""
    for letter in text:
        letterCode = ord(letter)
        if (97 <= letterCode <= 122):
            encryptedText += chr(97 + (letterCode + shift - 97) % 26)
        elif (65 <= letterCode <= 90):
            encryptedText += chr(65 + (letterCode + shift - 65) % 26)
        else:
            encryptedText += letter
    return encryptedText

# Automatyczny łamacz szyfru Cezara, działa dobrze dla dłuższych tekstów
def ceasarBreaker(text):
    DetectorFactory.seed = 0
    tableOfAllCombinations = []
    currentText = "No valid result"
    currentTextProbability = 0
    
    # Wypełnienie tableOfAllCombinations wszystkimi kombinacjami szyfru Cezara
    for i in range(0, 26):
        tableOfAllCombinations.append(caesarCipher(text, i))

    # Znalezienie najbardziej pasującej z 26 kombinacji z tableOfAllCombinations
    for i in range(0, 26):
        detectedLangsList = detect_langs(tableOfAllCombinations[i])
        for detectedLang in detectedLangsList:
            # Wybranie kombinacji z największym dopasowaniem do j.angielskiego
            if ((detectedLang.lang == "en") and (detectedLang.prob > currentTextProbability)):
                currentText = tableOfAllCombinations[i]
                currentTextProbability = detectedLang.prob
    
    return currentText

encryptedWord = caesarCipher("Poland began to form into a recognizable unitary and territorial entity around the middle of the 10th century under the Piast dynasty. ", 15)
print(encryptedWord)
print(ceasarBreaker(encryptedWord))


