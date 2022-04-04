string=[]
for i in range(13,100,13):
    string.append(str(i))
    string.append(',')
string[-1]=''
string=''.join(string)
print(string)