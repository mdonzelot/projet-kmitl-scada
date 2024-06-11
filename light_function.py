import redis
import json

def turn_light_onoff (state, lightNbr):   
    # Connexion au serveur Redis
    client = redis.Redis(
        host='intelligentbuilding.io',
        port=6379,
        password='ictadmin'  # Omettre ou commenter cette ligne si aucune authentification n'est nécessaire
    )

    # Définir les valeurs à publier
    if lightNbr == 3:
        tag_full_name = 'passion.HueLight{:02d}.OnOff'.format(lightNbr)  # Mettre "ONOFF" en majuscules pour la lumière 3
    else:
        tag_full_name = 'passion.HueLight{:02d}.onoff'.format(lightNbr)
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

def switch_light_birghtness(intensite, lightNbr):
    # Connexion au serveur Redis
    client = redis.Redis(
        host='intelligentbuilding.io',
        port=6379,
        password='ictadmin'  # Omettre ou commenter cette ligne si aucune authentification n'est nécessaire
    )

    tag_full_name = 'passion.HueLight{:02d}.Brightness'.format(lightNbr)
    channel = f'settag2:{tag_full_name}'
    message_data = {
        "channel": "specific.xxxchanneltoresponsexx",
        "user_id": 1,
        "datetime": "2021-03-01 21:04:27.737153",
        "value": intensite
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

def switch_light_color(color, lightNbr):
    # Connexion au serveur Redis
    client = redis.Redis(
        host='intelligentbuilding.io',
        port=6379,
        password='ictadmin'  # Omettre ou commenter cette ligne si aucune authentification n'est nécessaire
    )

    tag_full_name = 'passion.HueLight{:02d}.Color'.format(lightNbr)
    channel = f'settag2:{tag_full_name}'
    message_data = {
        "channel": "specific.xxxchanneltoresponsexx",
        "user_id": 1,
        "datetime": "2021-03-01 21:04:27.737153",
        "value": color
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