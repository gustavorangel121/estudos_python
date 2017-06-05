my_list = ["segunda-feira", "terça-feira", "quarta-feira", "quinta-feira", "sexta-feira"]

m_iterator = iter(my_list)

for i in range(0, len(my_list)):
    next_item = next(m_iterator)
    print(next_item)