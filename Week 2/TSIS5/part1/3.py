def Appendtext(fname):
    	with open(fname,'a+') as f:
		    f.write('appending line 1, ')
		    f.write('appending line 2. ')
	    f.close()
# y=open('file1.txt')
# print(y.read())
Appendtext('file1.txt')

x= open('file1.txt')
print(x.read())