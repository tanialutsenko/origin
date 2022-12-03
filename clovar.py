grades = {'Python': [10, 10], 'HTML': [10, 10]}
average_grade = {}

for key,value in grades.items():
    sum_grade = 0
    for val in value:
        sum_grade += val
        average_grad_v = sum_grade/len(value)
        average_grade.update({key: average_grad_v})
#print(sum_grade)

#print(average_grade)


class Clock:
    __DAY = 86400  # число секунд в одном дне

    def __init__(self, seconds: int):
        if not isinstance(seconds, int):
            raise TypeError("Секунды должны быть целым числом")
        self.seconds = seconds * 5

    def __eq__(self, other):
        if not isinstance(other, (int, Clock)):
            raise TypeError("Операнд справа должен иметь тип int или Clock")

        sc = other if isinstance(other, int) else other.seconds
        return self.seconds == sc
c1 = Clock(1)
c2 = Clock(1)
print(c1 == c2)


with open("data_3.txt", encoding='utf-8') as file:
    cook_book = {}
    for txt in file.read().split('\n\n'):
        print(txt)
        name = txt.split('\n')
        number = txt.split('\n')
    print(name)

cook_book = {}
def get_cooking_book():
    with open('data_3.txt', encoding="utf-8") as file_to_read:
        for txt in file.read().split('\n\n'):
            while True:
                cook_book = {}
                recipe_name = file_to_read.readline().strip()
                print(recipe_name)

                number_of_ingredients = int(file_to_read.readline().strip())
                print(number_of_ingredients)


                list_of_ingredients = []

                for i in range(number_of_ingredients):
                    ingredient = file_to_read.readline().strip().split(' | ')
                    ingredients = {'ingredient_name': ingredient[0], 'quantity': int(ingredient[1]),'measure': ingredient[2]}
                    list_of_ingredients.append(ingredients)
                    print(list_of_ingredients)

                    cook_book.update({recipe_name: list_of_ingredients})
                    print(cook_book)
                    t = file_to_read.readline().split()
                    print(t)


                print("kkkkkkk",cook_book)

get_cooking_book()


