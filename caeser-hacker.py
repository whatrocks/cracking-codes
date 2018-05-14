SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'

MESSAGE = '''
qeFIP?eGSeECNNS,
5coOMXXcoPSZIWoQI,
avnl1olyD4l'ylDohww6DhzDjhuDil,
z.GM?.cEQc. 70c.7KcKMKHA9AGFK,
?MFYp2pPJJUpZSIJWpRdpMFY,
ZqH8sl5HtqHTH4s3lyvH5zH5spH4t pHzqHlH3l5K
Zfbi,!tif!xpvme!qspcbcmz!fbu!nfA
'''


def decipher_line(line):
    for key in range(len(SYMBOLS)):
        
        translated = ''

        for char in line:

            if char in SYMBOLS:


                index = SYMBOLS.find(char)
                new_index = index - key

                if (new_index < 0):
                    new_index += len(SYMBOLS)

                translated += SYMBOLS[new_index]

            else:

                translated += char

        print(translated)
        




lines = MESSAGE.split('\n')
for line in lines:
    print("--------------------")
    print(decipher_line(line))

# decipher_line("hello")



'''
I love my kitty,
My kitty loves me,
Together we're as happy as can be,
Though my head has suspicions,
That I keep under my hat,
Of what if I shrank to the size of a rat.
Yeah, she would probably eat me.
'''