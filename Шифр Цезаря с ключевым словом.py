cryptMode = input("[E]ncrypt(шифрование)|[D]ecrypt(расшифровка): ").upper()
if cryptMode not in ['E','D']:
    print("Error: mode is not Found!"); raise SystemExit

alphaList = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
startMessage = input("Введите сообщение: ").upper()

try: numberKey = int(input("Введите ключ: "))
except ValueError: print("Ошибка: введите целое число!"); raise SystemExit

stringKey = list(input("Введите ключевое слово: ").upper())

def remove(alpha, string):
    for symbol in string:
        if symbol in alpha: alpha.remove(symbol)
    for symbol in string:
        if symbol not in [chr(x) for x in range(65,91)] \
        or string.count(symbol) > 1: string.remove(symbol) 
    return alpha, string

def insert(alpha_string):
    for index, symbol in enumerate(alpha_string[1]):
        alpha_string[0].insert((numberKey+index)%26, symbol)
    return alpha_string[0]

def encryptDecrypt(mode, message, key, final = ""):
    alpha = insert(remove(alphaList, stringKey))
    for symbol in message:
        if mode == 'E':
            final += alpha[(alpha.index(symbol) + key)%26]
        else: 
            final += alpha[(alpha.index(symbol) - key)%26]
    return final

message = encryptDecrypt(cryptMode, startMessage, numberKey)
print("Результат:", message)