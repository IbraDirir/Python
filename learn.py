#unpacking arguments
def health_calculator(age, apples_ate, cigs_smoke):
    answer = (100-age)+(apples_ate * 3.5) - (cigs_smoke*2)
    print(answer)
ibras_data = [21, 5, 0]

mohas_data = [45, 0, 20]

health_calculator(*mohas_data)
health_calculator(*ibras_data)