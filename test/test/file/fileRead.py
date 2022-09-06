path = 'test.txt'
f = None
try :
    f = open(path, 'r')
    # print(f.read())

    text = []
    for line in f:
        text.append(line)
    print(text)
except FileNotFoundError:
    print('ERROR: FileNotFoundError ' + path)
    if f:
        f.close()
# except :
#     print('ERROR: can not found ' + path)
#     if f:
#         f.close()
# except Exception as ex:  # find exception name
#     template = "An exception of type {0} occurred. Arguments:\n{1!r}"
#     message = template.format(type(ex).__name__, ex.args)
#     print (message)
finally:
    if f:
        f.close()