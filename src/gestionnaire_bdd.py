from sqlalchemy import create_engine, Column, Integer, String, Float, Date, ForeignKey, func
from sqlalchemy.orm import declarative_base, sessionmaker, relationship
from sqlalchemy.exc import NoResultFound

Base = declarative_base()

# Classe pour représenter une entreprise
class Entreprise(Base):
    __tablename__ = "entreprises"

    symbole = Column(String, primary_key=True)  # Identifiant unique pour l'entreprise
    nom = Column(String, nullable=False)
    secteur = Column(String, nullable=False)

    # Relation avec les données financières
    donnees_financieres = relationship("DonneeFinanciere", back_populates="entreprise")

    def __repr__(self):
        return f"<Entreprise(symbole={self.symbole}, nom={self.nom}, secteur={self.secteur})>"

# Classe pour représenter les données financières
class DonneeFinanciere(Base):
    __tablename__ = "donnees_financieres"

    id = Column(Integer, primary_key=True)
    symbole = Column(String, ForeignKey('entreprises.symbole'), nullable=False)
    secteur = Column(String, nullable=False)
    date = Column(Date, nullable=False)
    open = Column(Float, nullable=False)
    high = Column(Float, nullable=False)
    low = Column(Float, nullable=False)
    close = Column(Float, nullable=False)
    volume = Column(Integer, nullable=False)

    entreprise = relationship("Entreprise", back_populates="donnees_financieres")

    def __repr__(self):
        return f"<DonneeFinanciere(symbole={self.symbole}, date={self.date}, close={self.close})>"

# Gestionnaire de la base de données
class GestionnaireBDD:
    def __init__(self, nom_bdd="bourse.db"):
        self.engine = create_engine(f"sqlite:///{nom_bdd}")
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)

    def ajouter_entreprise(self, symbole, nom, secteur):
        """
        Ajoute une nouvelle entreprise à la base de données.
        """
        if self.entreprise_existe(symbole):
            raise Exception(f"L'entreprise avec le symbole {symbole} existe déjà.")
        session = self.Session()
        try:
            entreprise = Entreprise(symbole=symbole, nom=nom, secteur=secteur)
            session.add(entreprise)
            session.commit()
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()

    def entreprise_existe(self, symbole):
        """
        Vérifie si une entreprise existe déjà dans la base de données.
        """
        session = self.Session()
        try:
            return session.query(Entreprise).filter_by(symbole=symbole).first() is not None
        finally:
            session.close()

    def ajouter_donnees_financieres(self, donnees, symbole):
        """
        Ajoute des données financières à la base de données.
        """
        session = self.Session()
        try:
            entreprise = session.query(Entreprise).filter_by(symbole=symbole).one()
            secteur = entreprise.secteur

            for data in donnees:
                data["secteur"] = secteur
                session.add(DonneeFinanciere(symbole=symbole, **data))
            session.commit()
        except NoResultFound:
            raise Exception(f"L'entreprise avec le symbole {symbole} n'existe pas.")
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()

    def calculer_indicateurs_financiers(self):
        """
        Calcule les indicateurs financiers pour chaque entreprise.
        """
        session = self.Session()
        indicateurs = []
        entreprises = session.query(Entreprise).all()

        for entreprise in entreprises:
            donnees = (
                session.query(DonneeFinanciere)
                .filter(DonneeFinanciere.symbole == entreprise.symbole)
                .order_by(DonneeFinanciere.date.desc())
                .limit(100)
                .all()
            )

            if donnees:
                prix_ouverture = [d.open for d in donnees]
                prix_fermeture = [d.close for d in donnees]
                volatilites = [d.high - d.low for d in donnees]
                volumes = [d.volume for d in donnees]
                rendements = [(d.close - d.open) / d.open * 100 for d in donnees]

                indicateurs.append({
                    "nom": entreprise.nom,
                    "prix_moyen_ouverture": sum(prix_ouverture) / len(prix_ouverture),
                    "prix_moyen_fermeture": sum(prix_fermeture) / len(prix_fermeture),
                    "volatilite_moyenne": sum(volatilites) / len(volatilites),
                    "volume_moyen": sum(volumes) / len(volumes),
                    "tendance_globale": (
                        sum(prix_fermeture) / len(prix_fermeture) - sum(prix_ouverture) / len(prix_ouverture)
                    ),
                    "rendement_moyen_journalier": sum(rendements) / len(rendements),
                })

        session.close()
        return indicateurs

    def volume_total_par_entreprise(self):
        """
        Calcule le volume total des échanges pour chaque entreprise.
        """
        session = self.Session()
        volumes = (
            session.query(Entreprise.nom, func.sum(DonneeFinanciere.volume))
            .join(DonneeFinanciere)
            .group_by(Entreprise.nom)
            .all()
        )
        session.close()
        return volumes
