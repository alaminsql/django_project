def first_middeware(get_response):
    print('one time initialization')
    def first_func(request):
        print("this is before veiw")
        response=get_response(request)
        print ('this is after veiw')
        return response
    return first_func