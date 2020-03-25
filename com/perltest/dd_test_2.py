from com.perltest import dd_utils, dd_test_3

if __name__ == '__main__':
    if dd_utils.ESE_AUTHKEY_FILE_PATH:
        dd_utils.DD_HEY = 15
    print('dd_utils.DD_HEY: %s' % dd_utils.DD_HEY)
    dd_test_3.dd_print()
