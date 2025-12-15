import platform
import psutil


def bytes_to_gb(bytes_value: int) -> float:
    """Convertit les octets en Gigaoctets et arrondit à 2 décimales."""
    return round(bytes_value / (1024**3), 2)



def afficher_informations_systeme():
    """Affiche le système d'exploitation, l'architecture et Python."""
    print("##  1. Informations Générales du Système")
    print(f"* Système d'exploitation : {platform.system()} ({platform.version()})")
    print(f"* Nom de la machine (Hostname) : {platform.node()}")
    print(f"* Architecture : {platform.architecture()}")
    print(f"* Version de Python : {platform.python_version()}")
    print("-" * 50)


def afficher_informations_cpu():
    """Affiche les cœurs physiques/logiques et l'utilisation actuelle du CPU."""
    print("\n## 2. Statistiques CPU")
    
    coeurs_physiques = psutil.cpu_count(logical=False)
    coeurs_logiques = psutil.cpu_count(logical=True)
    
    cpu_usage = psutil.cpu_percent(interval=0.1)
    print(f"* Nombre de cœurs physiques : **{coeurs_physiques}**")
    print(f"* Nombre de cœurs logiques : **{coeurs_logiques}**")
    print(f"* Pourcentage d'utilisation actuel : **{cpu_usage}%**")
    print("-" * 50)


def afficher_informations_ram():
    """Affiche la mémoire RAM totale et disponible en Gigaoctets."""
    print("\n## 3. Statistiques Mémoire (RAM)")
    
    ram_stats = psutil.virtual_memory()
    
    total_gb = bytes_to_gb(ram_stats.total)
    available_gb = bytes_to_gb(ram_stats.available)

    print(f"* Mémoire RAM totale du système : **{total_gb} Go**")
    print(f"* Mémoire RAM disponible : **{available_gb} Go**")
    print(f"* Pourcentage utilisé : {ram_stats.percent}%")
    print("-" * 50)


def afficher_utilisation_partitions():
    """
    Affiche l'utilisation des partitions de disque avec gestion des erreurs.
    (Code repris de votre implémentation.)
    """
    print("\n## 4. Utilisation des Partitions de Disque")
    
    partitions = psutil.disk_partitions()

    for partition in partitions:
        point_de_montage = partition.mountpoint

        try:
            usage = psutil.disk_usage(point_de_montage)
            pourcentage_utilisation = usage.percent
            
            print(f"Point de montage : **{point_de_montage}**")
            print(f"  - Pourcentage d'utilisation : {pourcentage_utilisation}%")
            print("-" * 25)

        except PermissionError:
            print(f"Point de montage : **{point_de_montage}**")
            print("  - Erreur : Permission refusée. (Exécuter en tant qu'administrateur peut aider.)")
            print("-" * 25)
        
        except FileNotFoundError:
            print(f"Point de montage : **{point_de_montage}**")
            print("  - Erreur : Le point de montage est introuvable ou inaccessible.")
            print("-" * 25)
            
        except Exception as e:
            print(f"Point de montage : **{point_de_montage}**")
            print(f"  - Erreur inattendue : {e}")
            print("-" * 25)


def main():
    """Fonction principale, appelle toutes les fonctions d'affichage."""
    
    
    afficher_informations_systeme()
    afficher_informations_cpu()
    afficher_informations_ram()
    afficher_utilisation_partitions()

if __name__ == "__main__":
    main()
