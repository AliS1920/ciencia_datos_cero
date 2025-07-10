#CAPITULO 1 

#PARTE 1
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

#Parejas de amigos en comun 
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

# Ahora estas líneas van fuera de la función
total_connections = sum(number_of_friends(user) for user in users)
num_users = len(users)
avg_connections = total_connections / num_users
print("Total connections:", total_connections) #24
print("Promedio de conecciones:", avg_connections)  # 24/10 = 2.4 

#Ordenar los usuarios de “la mayor cantidad de amigos” a “la menor cantidad de amigos”
# Crea una lista (user_id, number_of_friends).
num_friends_by_id = [(user["id"], number_of_friends(user))
 for user in users]
num_friends_by_id.sort(                         # Ordena la lista de tuplas por el número de amigos
 key=lambda id_and_friends: id_and_friends[1],  #De mayor a menor
 reverse=True)
 # Cada par es (user_id, num_friends):
 # [(1, 3), (2, 3), (3, 3), (5, 3), (8, 3),
 # (0, 2), (4, 2), (6, 2), (7, 2), (9, 1)]
 
 
#Conocer amigos de los amigos

def foaf_ids_bad(user):
 """foaf is short for "friend of a friend" """
 return [foaf_id
for friend_id in friendships[user["id"]]
for foaf_id in friendships[friend_id]]
#Se aplico sobre el usuario 0 Hero -> Resultado [0, 2, 3, 0, 1, 3]

#Contador de amigos mutuos
from collections import Counter
def friends_of_friends(user):
 user_id = user["id"]
 return Counter(
 foaf_id
 for friend_id in friendships[user_id]
 for foaf_id in friendships[friend_id]
 if foaf_id != user_id
 and foaf_id not in
 friendships[user_id]
 )
print(friends_of_friends(users[3])) # Contador({0: 2, 5: 1})
#(id 3)  tiene dos amigos mutuos con Hero (id 0), pero solo uno con Clive (id 5)

#Conocer amigos con intereses comunes 
interests = [
 (0, "Hadoop"), (0, "Big Data"), (0, "HBase"), (0, "Java"),
 (0, "Spark"), (0, "Storm"), (0, "Cassandra"),
 (1, "NoSQL"), (1, "MongoDB"), (1, "Cassandra"), (1, "HBase"),
 (1, "Postgres"), (2, "Python"), (2, "scikit-learn"), (2, "scipy"),
 (2, "numpy"), (2, "statsmodels"), (2, "pandas"), (3, "R"), (3, "Python"),
 (3, "statistics"), (3, "regression"), (3, "probability"),
 (4, "machine learning"), (4, "regression"), (4, "decision trees"),
 (4, "libsvm"), (5, "Python"), (5, "R"), (5, "Java"), (5, "C++"),
 (5, "Haskell"), (5, "programming languages"), (6, "statistics"),
 (6, "probability"), (6, "mathematics"), (6, "theory"),
 (7, "machine learning"), (7, "scikit-learn"), (7, "Mahout"),
 (7, "neural networks"), (8, "neural networks"), (8, "deep learning"),
 (8, "Big Data"), (8, "artificial intelligence"), (9, "Hadoop"),
 (9, "Java"), (9, "MapReduce"), (9, "Big Data")
 ]

#Encontrar usuarios con un determinado interés
def data_scientists_who_like(target_interest):
 """Find the ids of all users who like the target interest."""
 return [user_id
 for user_id, user_interest in interests
 if user_interest == target_interest]

#Crear indices de intereses
from collections import defaultdict
# Las claves son intereses, los valores son listas de user_ids con ese interés
user_ids_by_interest = defaultdict(list)
for user_id, interest in interests:
    user_ids_by_interest[interest].append(user_id)

#Crear indices de usuarios a intereses
# Las claves son user_ids, los valores son listas de intereses para ese
interests_by_user_id = defaultdict(list)
for user_id, interest in interests:
    interests_by_user_id[user_id].append(interest)
    
#Se puede averiguar quién tiene el mayor número de intereses en común con un determinado usuario
def most_common_interests_with(user):
 return Counter(
 interested_user_id
 for interest in interests_by_user_id[user["id"]]
 for interested_user_id in user_ids_by_interest[interest]
 if interested_user_id != user["id"]
 )

#PARTE 2
#Suministrar datos curiosos sobre lo que ganan los científicos de datos
#Salario / experiencia en años
salaries_and_tenures = [(83000, 8.7), (88000, 8.1),
 (48000, 0.7), (76000, 6),
 (69000, 6.5), (76000, 7.5),
 (60000, 2.5), (83000, 10),
 (48000, 1.9), (63000, 4.2)]

#Parece que el salario aumenta con la antiguedad 
#Años de antigüedad en un bucket:
def tenure_bucket(tenure):
    if tenure < 2:
        return "less than two"
    elif tenure < 5:
        return "between two and five"
    else:
        return "more than five"

#Agrupar los salarios correspondientes a cada bucket:
#Las claves son buckets de años de antigüedad, los valores son listas de salarios
salary_by_tenure_bucket = defaultdict(list)
for salary, tenure in salaries_and_tenures:
    bucket = tenure_bucket(tenure)
    salary_by_tenure_bucket[bucket].append(salary)

#Calcular el salario medio para cada grupo:
#Las claves son buckets de años de antigüedad, los valores son el salario medio 
average_salary_by_bucket = {
    tenure_bucket: sum(salaries) / len(salaries)
    for tenure_bucket, salaries in salary_by_tenure_bucket.items()
}
# Lo que es más interesante:
{'between two and five': 61500.0,
'less than two': 48000.0,
'more than five': 79166.66666666667}
#El salario medio de los científicos de datos con menos de 2 años de experiencia es 48000.0
#El salario medio de los científicos de datos con entre 2 y 5 años de experiencia   es 61500.0
#El salario medio de los científicos de datos con más de 5 años de experiencia es 79166.66666666667

#PARTE 3
#Qué usuarios pagan por las cuentas y cuáles no
#Cuentas de pago
# 0.7 paid
# 1.9 unpaid
# 2.5 paid
# 4.2 unpaid
# 6.0 unpaid
# 6.5 unpaid
# 7.5 unpaid
# 8.1 unpaid
# 8.7 paid
# 10.0 paid

#Usuarios con muy pocos y muchos años de experiencia tienden a pagar
#Usuarios con cantidades de experiencia medias no lo hacen
def predict_paid_or_unpaid(years_experience):
 if years_experience < 3.0:
    return "paid"
 elif years_experience < 8.5:
    return "unpaid"
 else:
    return "paid"

#PARTE 4
#Temas que más interesan a los usuarios, para planificar el calendario de
interests = [
 (0, "Hadoop"), (0, "Big Data"), (0, "HBase"), (0, "Java"),
 (0, "Spark"), (0, "Storm"), (0, "Cassandra"),
 (1, "NoSQL"), (1, "MongoDB"), (1, "Cassandra"), (1, "HBase"),
 (1, "Postgres"), (2, "Python"), (2, "scikit-learn"), (2, "scipy"),
 (2, "numpy"), (2, "statsmodels"), (2, "pandas"), (3, "R"), (3, "Python"),
 (3, "statistics"), (3, "regression"), (3, "probability"),
 (4, "machine learning"), (4, "regression"), (4, "decision trees"),
 (4, "libsvm"), (5, "Python"), (5, "R"), (5, "Java"), (5, "C++"),
 (5, "Haskell"), (5, "programming languages"), (6, "statistics"),
 (6, "probability"), (6, "mathematics"), (6, "theory"),
 (7, "machine learning"), (7, "scikit-learn"), (7, "Mahout"),
 (7, "neural networks"), (8, "neural networks"), (8, "deep learning"),
 (8, "Big Data"), (8, "artificial intelligence"), (9, "Hadoop"),
 (9, "Java"), (9, "MapReduce"), (9, "Big Data")
 ]

# 1. Ponemos en minúsculas todos los hobbies 
# (ya que habrá usuarios que los pongan en mayúscula y otros en minúscula).
# 2. Los dividimos en palabras.
# 3. Contamos los resultados

words_and_counts = Counter(word
    for user, interest in interests
    for word in interest.lower().split())
for word, count in words_and_counts.most_common():
    if count > 1:
        print(word, count)