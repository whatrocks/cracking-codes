# Caesar Cipher Hacker

message = 'guv6Jv6Jz!J6rp5r7Jzr66ntrM'
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'

# loop thru every possible key
for key in range(len(SYMBOLS)):
    # It is important to reset translated to blank string
    # so that the previos iteration is clearted
    translated = ''

    # the rest of the program is same as caesar
    for symbol in message:
        if symbol in SYMBOLS:
            symbolIndex = SYMBOLS.find(symbol)
            translatedIndex = symbolIndex - key

            # handle wraparound
            if translatedIndex < 0:
                translatedIndex = translatedIndex + len(SYMBOLS)

            # append the decrypted cymbol
            translated = translated + SYMBOLS[translatedIndex]

        else:
            # append it
            translated = translated + symbol

    print('Key #%s: %s' % (key, translated))