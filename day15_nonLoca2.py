def outer():
    print('outer funtion')

    def inner():
        print('inner funtion')

    inner()

outer()
