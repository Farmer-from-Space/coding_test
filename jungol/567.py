#%%
nums = [[5,8,10,6,4],[11,20,1,13,2],[7,9,14,22,3]]
temp =""
for i in nums:
    for j in i:
        if j == i[0]:
            temp += str(j).rjust(2)    
        else:
            temp += str(j).rjust(5)
    temp += "\n"
print(temp)
# %%
