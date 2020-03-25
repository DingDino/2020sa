import time
import datetime


def dd_test4():
    file_path = r'C:\ADev\Test_folder\Mytest\com\dingdong\test3.py'
    try:
        with open(file_path, 'r') as f:
            auth_key = f.read()
            print('type: %s', type(auth_key))
            if auth_key and len(auth_key) > 1:
                # raise UnicodeError('test coding issue!')
                return auth_key
    except FileNotFoundError as fe:
        print('Cannot read auth key file, it does not exist. ERROR details: ', fe)
    except Exception as ex:
        print('ERROR details: ', ex)

if __name__ == '__main__':
    result = {'111': dd_test4() or '222'}
    print(result['111'])
