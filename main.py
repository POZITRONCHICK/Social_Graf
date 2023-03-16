# -*- coding: utf8 -*-
import vk_api
import networkx as nx
from pyvis.network import Network

def set_user_friend(user_id):
    name_friend_list = []
    node_user = session.method('users.get', {'user_ids': user_id})
    node_user_name = node_user[0]['first_name'] + ' ' + node_user[0]['last_name']
    friends_id = session.method('friends.get', {'user_id': user_id})
    for friend in friends_id['items']:
        if len(name_friend_list) < 10:
            friend_info = session.method('users.get', {'user_ids': friend})
            one_friend_name = friend_info[0]['first_name'] + ' ' + friend_info[0]['last_name']
            name_friend_list.append((node_user_name, one_friend_name))
    return name_friend_list

session = vk_api.VkApi(token='TOKEN')
my_id = 'USER_ID'

friends_id = session.method('friends.get', {'user_id': my_id})

all_id_list = [my_id]
for friend in friends_id['items']:
    all_id_list.append(friend)

graf_set = []

c = 1

for id in all_id_list:
    if len(graf_set) < 100:
        graf_set.extend(set_user_friend(id))
        print('Number of processed users:', c)
        c += 1

graf_model = nx.DiGraph()
graf_model.add_edges_from(graf_set)

net_model = Network()
net_model.from_nx(graf_model)

net_model.show('test_set.html', notebook=False)