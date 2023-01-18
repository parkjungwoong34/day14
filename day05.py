# 11
a_set = {number for number in range(10) if number % 2 == 1}
print(a_set)

# # 12
for thing in ('got %s' % number for number in range(10)):
    print(thing)

# 13
character = 'optimist', 'pessimist', 'troll'
sentence = 'The glass is half full', 'The glass is half empty', 'How did you get a glass?'
ex13 = dict( zip(character, sentence))
print(ex13)

#14
titles = ['Creature of Habit', 'Crewl Fate']
plots = ['A nun turns into a mon ster', 'A haunted yarn shop']
movies = dict( zip(titles, plots))
print(movies)

#9. 1
def good():
    return ['Harry', 'Ron', 'Hermione']

print(good())