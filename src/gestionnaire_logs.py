import logging

# Configuration des logs
logging.basicConfig(
    filename="bourse_track.log",  # Nom du fichier de log
    level=logging.INFO,  # Niveau de log : INFO, WARNING, ERROR, DEBUG
    format="%(asctime)s - %(levelname)s - %(message)s",  # Format des logs
)

logger = logging.getLogger()
