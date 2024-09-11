# Question2:-
# count the occurrences of a particular element in the list and output highest occurring element
# days = ['sun','mon','mon','tue','wed','thu','fri','sat','mon','thu',]

# solution 2:-

days = ['sun','mon','mon','tue','wed','thu','fri','sat','mon','thu',]

count= {}
for i in days:
  if i in count:
    count[i]+=1
  else:
    count[i] = 1
# print(count)    

max_day = max(count, key=count.get)
print(max_day)