http_status= int(input('Enter http '))

match http_status:
  case 200 | 201:
    print('Success')
  case 400:
    print('Not Found')
  case 500 | 501:
    print('Server Error')
  case _:
    print('Unknown')