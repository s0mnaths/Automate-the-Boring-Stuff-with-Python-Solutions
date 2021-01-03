import sys

def collatz(number):
    if number%2==0:
        ans=number//2
        print(ans)
    else:
        ans=3*number+1
        print(ans)
    return ans

print('Enter Number: ')
while True:    
    try:
        x=collatz(int(input()))
    except ValueError:
        print('Wrong Input: Enter an integer!')
    if(x==1):
        sys.exit()