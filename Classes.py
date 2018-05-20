
print("Classes")
print('-'*11)

class listComposites:

    def __init__(self, lst1, lst2):
        self.list1 = lst1
        self.list2 = lst2
    
    def addLists(self):
        lst = []
        for l1, l2 in zip(self.list1, self.list2):
            lst.append(l1+l2)
        return (lst)

    def subLists(self):
        lst = []
        for l1, l2 in zip(self.list1, self.list2):
            lst.append(l1-l2)
        return (lst)

lstA = [1, 2, 3, 4, 5]
lstB = [10, 20, 30, 40, 50]

lc = listComposites(lstA, lstB)

print("lstA",lstA)
print("lstB",lstB)

lstC = lc.addLists()
print ("Calling Add_list function in listcomposites class",lstC)

lstC = lc.subLists()
print ("Calling Sub_list function in listcomposites class",lstC)



