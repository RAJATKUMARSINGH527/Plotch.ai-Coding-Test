# Question4.
# Return the Item with highest value count
#items = [{'Delhi': 3}, {'Mumbai': 9}, {'Goa': 7}, {'Gujrat': 4}] 
# #Output: Mumbai

# Solution 4:-

items = [{'Delhi': 3}, {'Mumbai': 9}, {'Goa': 7}, {'Gujrat': 4}]

def highest_count(items):
    max_item = 0  
    max_value = 0  

    for item in items:
        for key in item:
            if item[key] > max_value: 
                max_value = item[key] 
                max_item = key  

    return max_item  

print(highest_count(items))
