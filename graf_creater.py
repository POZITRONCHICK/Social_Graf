# -*- coding: utf8 -*-
import networkx as nx
from pyvis.network import Network

test_set = [('Рома Фролов', 'Галина Швец'), ('Рома Фролов', 'Антон Барсков'), ('Рома Фролов', 'Владимир Рувинский'), ('Рома Фролов', 'Анна Молчанова'), ('Рома Фролов', 'Kirill Efimov'), ('Рома Фролов', 'Лена Браславская'), ('Рома Фролов', 'Данил Моргуновский'), ('Рома Фролов', 'Valera Rossov'), ('Рома Фролов', 'Филимон Горчаков'), ('Рома Фролов', 'Мария Фролова'), ('Анастасия Городецкая', 'Галина Швец'), ('Анастасия Городецкая', 'Валерий Гутник'), ('Анастасия Городецкая', 'Антон Галдин'), ('Анастасия Городецкая', 'Вячеслав Лей'), ('Анастасия Городецкая', 'Глеб Захаров'), ('Анастасия Городецкая', 'Ирина Дымченко'), ('Анастасия Городецкая', 'Наталья Лямина'), ('Анастасия Городецкая', 'Жорка Сергеев'), ('Анастасия Городецкая', 'Лена Браславская'), ('Анастасия Городецкая', 'Ольга Еланская')]

graf_model = nx.DiGraph()
graf_model.add_edges_from(test_set)

net_model = Network()
net_model.from_nx(graf_model)

net_model.show('test_set.html', notebook=False)