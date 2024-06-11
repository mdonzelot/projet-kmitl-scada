import redis
import json

def turn_tv_onoff (state):   
    # Connexion au serveur Redis
    client = redis.Redis(
        host='intelligentbuilding.io',
        port=6379,
        password='ictadmin'  # Omettre ou commenter cette ligne si aucune authentification n'est nécessaire
    )

    # Définir les valeurs à publier
    tag_full_name = 'passion.Lab_TV_Remote.on'
    channel = f'settag2:{tag_full_name}'
    value = 1 if state == 1 else 0
    message_data = {
        "channel": "specific.xxxchanneltoresponsexx",
        "user_id": 1,
        "datetime": "2021-03-01 21:04:27.737153",
        "value": value
    }
frfr
    # Convertir le dictionnaire en chaîne JSON
    message_json = json.dumps(message_data)

    # Publier le message sur le canal
    try:
        result = client.publish(channel, message_json)
        print(f"Message publié sur le canal {channel}: {message_json}")
        print(f"Nombre de clients ayant reçu le message: {result}")
    except redis.AuthenticationError:
        print("Erreur d'authentification : mot de passe incorrect")
    except redis.RedisError as e:
        print("Erreur Redis :", e)

def turn_tv_mute (state):   
    # Connexion au serveur Redis
    client = redis.Redis(
        host='intelligentbuilding.io',
        port=6379,
        password='ictadmin'  # Omettre ou commenter cette ligne si aucune authentification n'est nécessaire
    )

    # Définir les valeurs à publier
    tag_full_name = 'passion.Lab_TV_Remote.mute'
    channel = f'settag2:{tag_full_name}'
    value = 1 if state == 1 else 0
    message_data = {
        "channel": "specific.xxxchanneltoresponsexx",
        "user_id": 1,
        "datetime": "2021-03-01 21:04:27.737153",
        "value": value
    }

    # Convertir le dictionnaire en chaîne JSON
    message_json = json.dumps(message_data)

    # Publier le message sur le canal
    try:
        result = client.publish(channel, message_json)
        print(f"Message publié sur le canal {channel}: {message_json}")
        print(f"Nombre de clients ayant reçu le message: {result}")
    except redis.AuthenticationError:
        print("Erreur d'authentification : mot de passe incorrect")
    except redis.RedisError as e:
        print("Erreur Redis :", e)

def switch_tv_channel(channel):
    # Connexion au serveur Redis
    client = redis.Redis(
        host='intelligentbuilding.io',
        port=6379,
        password='ictadmin'  # Omettre ou commenter cette ligne si aucune authentification n'est nécessaire
    )

    tag_full_name = 'passion.Lab_TV_Remote.channel'
    channel = f'settag2:{tag_full_name}'
    message_data = {
        "channel": "specific.xxxchanneltoresponsexx",
        "user_id": 1,
        "datetime": "2021-03-01 21:04:27.737153",
        "value": channel
    }

    # Convertir le dictionnaire en chaîne JSON
    message_json = json.dumps(message_data)

    # Publier le message sur le canal
    try:
        result = client.publish(channel, message_json)
        print(f"Message publié sur le canal {channel}: {message_json}")
        print(f"Nombre de clients ayant reçu le message: {result}")
    except redis.AuthenticationError:
        print("Erreur d'authentification : mot de passe incorrect")
    except redis.RedisError as e:
        print("Erreur Redis :", e)

def switch_tv_volume(volume):
    # Connexion au serveur Redis
    client = redis.Redis(
        host='intelligentbuilding.io',
        port=6379,
        password='ictadmin'  # Omettre ou commenter cette ligne si aucune authentification n'est nécessaire
    )

    tag_full_name = 'passion.Lab_TV_Remote.volume'
    channel = f'settag2:{tag_full_name}'
    message_data = {
        "channel": "specific.xxxchanneltoresponsexx",
        "user_id": 1,
        "datetime": "2021-03-01 21:04:27.737153",
        "value": volume
    }

    # Convertir le dictionnaire en chaîne JSON
    message_json = json.dumps(message_data)

    # Publier le message sur le canal
    try:
        result = client.publish(channel, message_json)
        print(f"Message publié sur le canal {channel}: {message_json}")
        print(f"Nombre de clients ayant reçu le message: {result}")
    except redis.AuthenticationError:
        print("Erreur d'authentification : mot de passe incorrect")
    except redis.RedisError as e:
        print("Erreur Redis :", e)