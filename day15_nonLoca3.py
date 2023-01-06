def outer():
    message='outer funtion'
    print(message)

    def inner():
        print(message)

    inner()

outer()
