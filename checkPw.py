print('Enter your password.')
typePassword = input()
if typePassword == 'swordfish':
    print('Access granted')
elif typePassword == 'mary':
    print('Hint: password is a fish')
elif typePassword == '12345':
    print('That is a super obvious password')
else:
    print('access denied')
print('Done')