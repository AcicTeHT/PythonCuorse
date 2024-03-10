
nums = input("Enter your number: ")

nums = [int(i) for i in nums]
# print(nums)


sum = 0
while sum < 9:
    res = 0
    for i in nums:
        res = i * i * i
        res = str(sum)
        nums = [int(i) for i in res]
        res = int(res)
        # print(sum)
        print(type(res))
        if res >= 9:
            sum = res

    print(nums)


    # for i in nums:
    #     if sum < 9:
    #         sum = i * i * i
    #     else:
    #         print(1)
    #         break
    #     # sum = str(sum)
    #     # nums = [int(i) for i in sum]
    #     print(sum)



    # nums = [int(i) for i in sum]
    # for j in nums:
    #     sum = i * i * i
        # print(sum)

    # for i in nums:
    #     sum = i * i * i
    #     print(nums)
    #     print(sum)




