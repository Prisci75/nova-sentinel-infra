#!/usr/bin/env python3
# ===============================================================
#  Nova Sentinel - Phase 1 : Audit & Collecte
#  Auteur : DataNova Team
#  Objectif : Audit complet du serveur Linux
# ===============================================================

import os
import psutil
import socket
import platform
import subprocess
import json
import logging
from datetime import datetime

# ===============================================================
#  CONFIGURATION DU LOGGING
# ===============================================================
LOG_DIR = "reports"
os.makedirs(LOG_DIR, exist_ok=True)
LOG_FILE = os.path.join(LOG_DIR, "sentinel_init.log")

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("===== DÉMARRAGE DE L’AUDIT NOVA SENTINEL =====")

# ===============================================================
#  FONCTIONS DE COLLECTE
# ===============================================================

def get_system_info():
    """Retourne les informations système de base."""
    try:
        info = {
            "hostname": socket.gethostname(),
            "os": platform.system(),
            "os_version": platform.version(),
            "architecture": platform.machine(),
            "kernel": platform.release()
        }
        logging.info("Informations système collectées avec succès.")
        return info
    except Exception as e:
        logging.error(f"Erreur lors de la collecte système : {e}")
        return {}

def get_cpu_info():
    """Retourne l'utilisation du CPU."""
    try:
        info = {
            "cpu_percent": psutil.cpu_percent(interval=1),
            "cpu_count": psutil.cpu_count(logical=True)
        }
        logging.info("Informations CPU collectées avec succès.")
        return info
    except Exception as e:
        logging.error(f"Erreur CPU : {e}")
        return {}

def get_memory_info():
    """Retourne les informations sur la RAM."""
    try:
        mem = psutil.virtual_memory()
        info = {
            "total_MB": mem.total // (1024 * 1024),
            "used_MB": mem.used // (1024 * 1024),
            "free_MB": mem.available // (1024 * 1024),
            "percent_used": mem.percent
        }
        logging.info("Informations mémoire collectées avec succès.")
        return info
    except Exception as e:
        logging.error(f"Erreur mémoire : {e}")
        return {}

def get_disk_info():
    """Retourne les informations sur les disques."""
    try:
        disk = psutil.disk_usage('/')
        info = {
            "total_GB": round(disk.total / (1024 ** 3), 2),
            "used_GB": round(disk.used / (1024 ** 3), 2),
            "free_GB": round(disk.free / (1024 ** 3), 2),
            "percent_used": disk.percent
        }
        logging.info("Informations disque collectées avec succès.")
        return info
    except Exception as e:
        logging.error(f"Erreur disque : {e}")
        return {}

def get_network_info():
    """Retourne les informations réseau et ports ouverts."""
    try:
        interfaces = psutil.net_if_addrs()
        ip_addresses = []
        for interface, addrs in interfaces.items():
            for addr in addrs:
                if addr.family == socket.AF_INET:
                    ip_addresses.append({
                        "interface": interface,
                        "ip_address": addr.address
                    })

        # Commande Linux pour lister les ports ouverts
        try:
            ports_output = subprocess.check_output(["ss", "-tulnp"], text=True)
        except Exception:
            ports_output = "Commande 'ss' non disponible."

        info = {
            "interfaces": ip_addresses,
            "ports_open": ports_output
        }
        logging.info("Informations réseau collectées avec succès.")
        return info
    except Exception as e:
        logging.error(f"Erreur réseau : {e}")
        return {}

def get_process_info():
    """Retourne le nombre de processus actifs."""
    try:
        count = len(psutil.pids())
        info = {"total_processes": count}
        logging.info("Nombre de processus collecté avec succès.")
        return info
    except Exception as e:
        logging.error(f"Erreur processus : {e}")
        return {}

def get_security_info():
    """Analyse optionnelle : fichiers SUID et utilisateurs UID < 1000."""
    try:
        suid_files = subprocess.getoutput("find / -perm -4000 -type f 2>/dev/null").split("\n")
        users_output = subprocess.getoutput("awk -F: '($3<1000){print $1,$3,$6}' /etc/passwd").split("\n")
        info = {
            "suid_files": suid_files[:10],  # Limite à 10 fichiers pour le rapport
            "low_uid_users": users_output
        }
        logging.info("Analyse sécurité collectée avec succès.")
        return info
    except Exception as e:
        logging.error(f"Erreur sécurité : {e}")
        return {}

# ===============================================================
#  GÉNÉRATION DES RAPPORTS
# ===============================================================

def generate_json_report(data):
    """Crée le fichier JSON structuré."""
    try:
        path = os.path.join(LOG_DIR, "sentinel_report.json")
        with open(path, "w") as f:
            json.dump(data, f, indent=4)
        logging.info("Rapport JSON généré avec succès.")
    except Exception as e:
        logging.error(f"Erreur génération JSON : {e}")

def generate_markdown_report(data):
    """Crée un rapport Markdown lisible."""
    try:
        path = os.path.join(LOG_DIR, "sentinel_report.md")
        with open(path, "w") as f:
            f.write("# 🛰️ Rapport Nova Sentinel\n\n")
            f.write(f"**Horodatage :** {data['timestamp']}\n\n")

            f.write("## Informations Système\n")
            for k, v in data['system'].items():
                f.write(f"- **{k.capitalize()}** : {v}\n")
            f.write("\n")

            f.write("## CPU\n")
            for k, v in data['cpu'].items():
                f.write(f"- **{k.replace('_', ' ').capitalize()}** : {v}\n")
            f.write("\n")

            f.write("## Mémoire\n")
            for k, v in data['memory'].items():
                f.write(f"- **{k.replace('_', ' ').capitalize()}** : {v}\n")
            f.write("\n")

            f.write("## Disque\n")
            for k, v in data['disk'].items():
                f.write(f"- **{k.replace('_', ' ').capitalize()}** : {v}\n")
            f.write("\n")

            f.write("## Réseau\n")
            for iface in data['network']['interfaces']:
                f.write(f"- **{iface['interface']}** : {iface['ip_address']}\n")
            f.write("\n### Ports ouverts\n```\n" + data['network']['ports_open'] + "\n```\n")

            f.write("\n## Processus\n")
            f.write(f"- **Nombre total** : {data['process']['total_processes']}\n")

            if "security" in data:
                f.write("\n## Sécurité (Optionnel)\n")
                f.write("### Fichiers SUID\n")
                f.write("\n".join(data['security']['suid_files']) + "\n\n")
                f.write("### Utilisateurs UID < 1000\n")
                f.write("\n".join(data['security']['low_uid_users']) + "\n")

        logging.info("Rapport Markdown généré avec succès.")
    except Exception as e:
        logging.error(f"Erreur génération Markdown : {e}")

# ===============================================================
#  MAIN - EXECUTION GLOBALE
# ===============================================================

if __name__ == "__main__":
    try:
        logging.info("Collecte des données en cours...")

        report_data = {
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "system": get_system_info(),
            "cpu": get_cpu_info(),
            "memory": get_memory_info(),
            "disk": get_disk_info(),
            "network": get_network_info(),
            "process": get_process_info(),
            "security": get_security_info()
        }

        generate_json_report(report_data)
        generate_markdown_report(report_data)

        logging.info("===== FIN DE L’AUDIT NOVA SENTINEL =====")
        print("✅ Audit terminé avec succès ! Les rapports sont disponibles dans le dossier 'reports/'.")

    except Exception as main_e:
        logging.critical(f"Erreur critique : {main_e}")
        print("❌ Une erreur critique est survenue. Consultez 'sentinel_init.log' pour plus de détails.")
