# classe client avec un nom et un prénom
class Client:
    """
    Classe représentant un client avec un nom et un prénom.
    """
    
    def __init__(self, nom, prenom):
        """
        Initialise un nouveau client.
        
        Args:
            nom (str): Le nom du client.
            prenom (str): Le prénom du client.
        """
        self.__nom = nom
        self.__prenom = prenom

    def afficher_informations(self):
        """
        Affiche les informations du client.
        
        Returns:
            str: Les informations du client formatées.
        """
        return f"Client: {self.__prenom} {self.__nom}"

# créer une classe compte bancaire avec un dépôt et un retrait
class CompteBancaire:
    """
    Classe représentant un compte bancaire avec des opérations de base.
    """
    
    def __init__(self, client: Client, solde_initial=100.):
        """
        Initialise un nouveau compte bancaire.
        
        Args:
            solde_initial (float, optional): Le solde initial du compte. Par défaut 0.
            client (Client, optional): Un objet Client associé au compte. Par défaut None.
        """
        self.solde = solde_initial
        self.client = client

    def deposer(self, montant):
        """
        Effectue un dépôt sur le compte.
        
        Args:
            montant (float): Le montant à déposer. Doit être positif.
            
        Returns:
            None
            
        Note:
            Affiche un message confirmant le dépôt ou une erreur si le montant est invalide.
        """
        if montant > 0:
            self.solde += montant
            print(f"Dépôt de {montant} effectué. Nouveau solde: {self.solde}")
        else:
            print("Le montant du dépôt doit être positif.")

    def retirer(self, montant):
        """
        Effectue un retrait du compte.
        
        Args:
            montant (float): Le montant à retirer. Doit être positif et inférieur ou égal au solde.
            
        Returns:
            None
            
        Note:
            Affiche un message confirmant le retrait ou une erreur si le montant est invalide 
            ou si le solde est insuffisant.
        """
        if 0 < montant <= self.solde:
            self.solde -= montant
            print(f"Retrait de {montant} effectué. Nouveau solde: {self.solde}")
        else:
            print("Montant de retrait invalide ou solde insuffisant.")
    
    def afficher_client_informations(self):
        """
        Affiche les informations du client associé au compte.
        
        Returns:
            str: Les informations du client formatées.
        """
        if self.client:
            # injection de dépendance => couplage faible
            # la classe CompteBancaire ne connaît que les méthodes publiques de la classe Client
            return self.client.afficher_informations()
        else:
            return "Aucun client associé à ce compte."