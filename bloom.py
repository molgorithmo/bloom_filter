
# coding: utf-8

# In[3]:


bloom_array = list()
s = int(input("Enter how many elements you want:"))
print ('Enter numbers in array: ')
for i in range(s):
    n = int(input("num :"))
    bloom_array.append(n)
print ('ARRAY: ',bloom_array)


# In[12]:


final_bloom = [0] * 11
print (final_bloom)
def binz(x):
    zeros = bin(x).count("0")-1
    print("Zeroes in ",x,"are",zeros)
    zeros_mod = zeros%11
    print("Mod zero is :",zeros_mod)
    return zeros_mod

def bino(x):
    ones = bin(x).count("1")
    print("Ones in ",x,"are",ones) 
    ones_mod = ones%11
    print("Mod one is :",ones_mod)
    print()
    return ones_mod


# In[13]:


for i in range(s):
    temp = binz(bloom_array[i])
    final_bloom[temp] = 1
    temp = bino(bloom_array[i])
    final_bloom[temp] = 1
    
print (final_bloom)


# In[21]:


print(final_bloom)
check = int(input("Enter your number to check whether it exists or not : "))
temp0 = binz(check)    
temp1 = bino(check)
print("temp", temp0, temp1)
if(final_bloom[temp0] == 1 and final_bloom[temp1] == 1):
    print("Number", check, "exists")
    if(check in bloom_array):
        print("True Positive")
    else:
        print("False Positive")
else:
    print("Number", check, "doesn't exist")

