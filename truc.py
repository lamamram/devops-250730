# créer une classe compte bancaire avec un dépôt et un retrait
class CompteBancaire:
    """
    Classe représentant un compte bancaire avec des opérations de base.
    """
    
    def __init__(self, solde_initial=0):
        """
        Initialise un nouveau compte bancaire.
        
        Args:
            solde_initial (float, optional): Le solde initial du compte. Par défaut 0.
        """
        self.solde = solde_initial

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