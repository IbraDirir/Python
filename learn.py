stocks =  {
    'GOOG': 520.54,
    'FB': 76.54,
    'YHOO':399.28,
    'APPL':99.76
}
print(min(zip(stocks.values(), stocks.keys())))
print(max(zip(stocks.values(), stocks.keys())))
print(sorted(zip(stocks.values(), stocks.keys())))