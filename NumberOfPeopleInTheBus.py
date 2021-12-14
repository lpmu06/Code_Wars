'''
There is a bus moving in the city, and it takes and drop some people in each bus stop.
You are provided with a list (or array) of integer pairs. Elements of each pair represent number of people get
into bus (The first item) and number of people get off the bus (The second item) in a bus stop.
Your task is to return number of people who are still in the bus after the last bus station (after the last array).
Even though it is the last bus stop, the bus is not empty and some people are still in the bus,
and they are probably sleeping there :D Take a look on the test cases.
Please keep in mind that the test cases ensure that the number of people in the bus is always >= 0.
So the return integer can't be negative.
The second value in the first integer array is 0, since the bus is empty in the first bus stop.
'''
# Exemplo de entrada: bus_stops = [[10,0],[3,5],[5,8]]
# Cada sublista é uma parada, sendo:
# bus_stops[0][0] = pessoas que entram no bus
# bus_stops[0][1] = pessoas que saem do bus
# Retornar a soma de todos que entram subtraído da soma de todos que saem, deve ser maior ou igual a zero
# Se sobrar alguém no busão ao final da lina, provavelmente ela dormiu =(.

def number(bus_stops):
  people_in = 0
  people_out = 0
  for stops in bus_stops:
    people_in += stops[0]
    people_out += stops[1]
  return people_in - people_out

print(number([[10,0],[3,5],[5,8]]))
