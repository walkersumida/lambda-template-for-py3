import sys
import os
sys.path.append('./packages')
from packages import requests
# import settings # for local debug

def main():
    print(os.environ['DEBUG'])

# if __name__ == '__main__': # for local debug
def lambda_handler(event, context):
    main()
