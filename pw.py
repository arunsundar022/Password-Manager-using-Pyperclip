import sys,pyperclip


passwords = {
    'account_name':'password', #add your account and password here
    
}

if len(sys.argv)<2:
    print('usage:pw[account] -copy account password')
    sys.exit()

account = sys.argv[1]

if account in passwords:
    pyperclip.copy(passwords[account])
    print('password for '+ account +'copied to clipboard.')
else:
    print('there is no acoount named :'+account)
