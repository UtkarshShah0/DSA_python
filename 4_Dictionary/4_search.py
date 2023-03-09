#3 Traverse dict

a={'name': 'Edy', 'age': 27, 'address': 'London'}

def search(dict ,value):
    for key in dict:
        if(dict[key] == value):           #Time complexity O(n)
            print(key , dict[key])  #Space complexity O(1)

search(a,"London")
