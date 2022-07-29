def split(word):
    return [char for char in word]
    
def most_frequent(mylist):
    dict_of_counts = {item:mylist.count(item) for item in mylist}
    sort_dict = sorted(dict_of_counts.items(), key = lambda x : x[1], reverse = True)
    for i in sort_dict:
        print(i[0], i[1])
        
mylist = []
s = input("Please enter a string")
mylist = split(s)
most_frequent(mylist)
