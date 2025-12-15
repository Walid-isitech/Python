import datetime
import psutil
import platform
# Nous allons définir les fonctions de collecte ici pour un script autonome 
# sans dépendre de l'importation d'un autre fichier.

# --- Définitions des Fonctions de Collecte Précédentes ---

def collecter_info_systeme():
    """Collecte les informations OS, version, architecture, hostname."""
    info_dict = {
        'os': platform.system(),
        'version': platform.version(),
        'architecture': platform.architecture(),
        'hostname': platform.node()
    }
    return info_dict

def collecter_cpu():
    """Collecte les cœurs CPU et l'utilisation (interval=1s)."""
    cpu_info = {
        'coeurs_physiques': psutil.cpu_count(logical=False),
        'coeurs_logiques': psutil.cpu_count(logical=True),
        'utilisation': psutil.cpu_percent(interval=1)
    }
    return cpu_info

def collecter_memoire():
    """Collecte la RAM totale, disponible (en octets) et le pourcentage utilisé."""
    ram_stats = psutil.virtual_memory()
    memoire_info = {
        'total': ram_stats.total,
        'disponible': ram_stats.available,
        'pourcentage': ram_stats.percent
    }
    return memoire_info

def collecter_disques():
    """Collecte les statistiques de chaque partition accessible (liste de dictionnaires)."""
    disques_info = []
    partitions = psutil.disk_partitions()

    for partition in partitions:
        point_de_montage = partition.mountpoint
        try:
            usage = psutil.disk_usage(point_de_montage)
            partition_dict = {
                'point_montage': point_de_montage,
                'total': usage.total,
                'utilise': usage.used,
                'pourcentage': usage.percent
            }
            disques_info.append(partition_dict)
        except Exception:
            pass # Ignorer les partitions inaccessibles
            
    return disques_info

# --- NOUVELLE FONCTION GLOBALE ---

def collecter_tout():
    """
    Appelle toutes les fonctions de collecte et agrège les résultats dans 
    un dictionnaire global.
    Ajoute un horodatage (timestamp) de la collecte.
    
    :return: Dictionnaire global des métriques système.
    """
    
    # Utiliser datetime.now() pour obtenir la date et l'heure actuelle
    timestamp_actuel = datetime.datetime.now().isoformat()
    
    # Appel de toutes les fonctions de collecte
    systeme = collecter_info_systeme()
    cpu = collecter_cpu()
    memoire = collecter_memoire()
    disques = collecter_disques()
    
    # Construction du dictionnaire global
    global_data = {
        'timestamp': timestamp_actuel,
        'systeme': systeme,
        'cpu': cpu,
        'memoire': memoire,
        'disques': disques
    }
    
    return global_data

if __name__ == "__main__":
    
    donnees_globales = collecter_tout()
    
    print("=" * 60)
    print("Structure de Données Globale (Collecte Complète)")
    print("=" * 60)
    
    # Affichage structuré du résultat (pour faciliter la lecture)
    
    print(f"Timestamp : {donnees_globales['timestamp']}")
    print("-" * 20)
    
    # Affichage des informations système
    print("SYSTEME :")
    for key, value in donnees_globales['systeme'].items():
        print(f"  {key:<15}: {value}")
        
    # Affichage des métriques CPU
    print("\nCPU :")
    for key, value in donnees_globales['cpu'].items():
        print(f"  {key:<15}: {value}")
        
    # Affichage des métriques Mémoire
    print("\nMEMOIRE :")
    print(f"  Total (octets) : {donnees_globales['memoire']['total']}")
    print(f"  Pourcentage ut.: {donnees_globales['memoire']['pourcentage']}%")

    # Affichage des métriques Disques
    print(f"\nDISQUES (Total: {len(donnees_globales['disques'])} partitions) :")
    if donnees_globales['disques']:
        premier_disque = donnees_globales['disques'][0]
        print(f"  [Première partition: {premier_disque['point_montage']}]")
        print(f"    Utilisation : {premier_disque['pourcentage']}%")