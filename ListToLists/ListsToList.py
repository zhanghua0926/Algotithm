
def listsToList(list):
    result = []
    for i in list:
        if type(i).__name__ == 'list':
            result = listsToList(i)
        else:
            result.append(i)
    return result


if __name__ == "__main__":
    lists = [[[1,2],3],4,5,6]
    list = listsToList(lists)
    print(list)