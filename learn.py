def drop_first_last(grades):
    first, *middle, last = grades
    avg = sum(middle) / len(middle)
    print(avg)
drop_first_last([90,87,90,21,30])
drop_first_last([90,90,98,78,89])