import os

name = os.getenv('MY_NAME','World')
print(f'Hello {name} from Python')


# export MY_NAME = 'Wade Wilson'
# echo 'Hello $MY_NAME'