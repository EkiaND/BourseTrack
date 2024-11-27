from sqlalchemy import create_engine, Column, Integer, String, Float, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

Base = declarative_base()

class DonneeFinanciere(Base):
    __tablename__ = "donnees_financieres"

    id = Column(Integer, primary_key=True)
    date = Column(Date)
    open = Column(Float)
    high = Column(Float)
    low = Column(Float)
    close = Column(Float)
    volume = Column(Integer)

class GestionnaireBDD:
    def __init__(self, nom_bdd="bourse.db"):
        self.engine = create_engine(f"sqlite:///{nom_bdd}")
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)

    def ajouter_donnees_financieres(self, donnees):
        """
        Ajoute des données financières à la base de données.
        :param donnees: Liste de dictionnaires contenant les données
        """
        session = self.Session()
        try:
            for data in donnees:
                # Conversion de la chaîne en date si nécessaire
                if isinstance(data["date"], str):
                    data["date"] = datetime.strptime(data["date"], "%Y-%m-%d").date()
                session.add(DonneeFinanciere(**data))
            session.commit()
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()
