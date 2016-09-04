def find_totalOf_multiple_of_3_or_5_for_range(number=1000):
    if(number<0 or isinstance(number, float)):
        return -1
    return sum([x for x in range(0,int(number)) if x % 3== 0 or x % 5== 0])

print(find_totalOf_multiple_of_3_or_5_for_range())
