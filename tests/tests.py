from pconf.settings import binder

@binder(value='token')
def token(value):
    return value

def main():
    assert token() == 'tokenvalue'

if __name__ == '__main__':
    main()