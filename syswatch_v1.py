import platform
import psutil

def systeme_exploitation():
    os_name = platform.system()
    print(f"{os_name}") 
systeme_exploitation()

def version_du_systeme():
    os_version = platform.version()
    print(f"{os_version}")
version_du_systeme()

def architecture_du_systeme():
    os_architecture = platform.architecture()
    print(f"{os_architecture}")
architecture_du_systeme()

def nom_de_la_machine():
    machine_name = platform.node()
    print(f"Hostname : {machine_name}")
nom_de_la_machine()

def version_de_python():
    python_version = platform.python_version()
    print(f"Version: {python_version}")
version_de_python()

def afficher_coeurs_cpu_physiques():
    coeurs_physiques = psutil.cpu_count(logical=False)
    print(f"Nombre de coeurs physiques : {coeurs_physiques}")
afficher_coeurs_cpu_physiques()

def afficher_coeurs_cpu_logiques():
    coeurs_logiques = psutil.cpu_count(logical=True)
    print(f"Nombre de coeurs logiques : {coeurs_logiques}")
afficher_coeurs_cpu_logiques()

def pourcentage_utilisation_cpu():
   cpu_usage = psutil.cpu_percent()
   print(f"Pourcentage utilisation : {cpu_usage}")
pourcentage_utilisation_cpu()

ram_stats = psutil.virtual_memory()
total_bytes = ram_stats.total
total_gb = total_bytes / (1024**3)
total_gb_rounded = round(total_gb, 2)
print(f"Mémoire RAM totale du système (arrondie à 2 décimales) : {total_gb_rounded} Go")