#Capitulo 1 

#Queremos hallar los amigos en comun 
#Usuarios 
users = [
 { "id": 0, "name": "Hero" },
 { "id": 1, "name": "Dunn" },
 { "id": 2, "name": "Sue" },
 { "id": 3, "name": "Chi" },
 { "id": 4, "name": "Thor" },
 { "id": 5, "name": "Clive" },
 { "id": 6, "name": "Hicks" },
 { "id": 7, "name": "Devin" },
 { "id": 8, "name": "Kate" },
 { "id": 9, "name": "Klein" }
]

friendship_pairs = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4),
 (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]

# Inicializar el dict con una lista vacía para cada id de usuario:
friendships = {user["id"]: [] for user in users}
# Y pasar por todos los pares de amistad para llenarlo:
for i, j in friendship_pairs:
 friendships[i].append(j)
 friendships[j].append(i)
 # Añadir j como un amigo del usuario i
 # Añadir i como un amigo del usuario j
 
 #Hallamos el número total de conexiones sumando las longitudes de todas las listas friends:
def number_of_friends(user):
 """How many friends does _user_ have?"""
 user_id = user["id"]
 friend_ids = friendships[user_id]
 return len(friend_ids)
 total_connections = sum(number_of_friends(user)
 for user in users)
 # 24
#Dividimos por el número de usuarios:
num_users = len(users)
avg_connections = total_connections / num_users