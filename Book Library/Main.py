'''
Created on Nov 6, 2021

@author: Thomas
'''
from Prezentare.user_interface import Consola
from business.servicii import ServiceCarti, ServiceClienti, ServiceRental
from infrastructura.repozitorii import FileRepoCarti,FileRepoClienti, RepoRental,RepoCarti,RepoClienti,FileRepoRental
from validare.validator import ValidatorClient, ValidatorCarte, ValidatorRental
from testare.teste import Teste
if __name__ == '__main__':
    valid_carte = ValidatorCarte()
    valid_client = ValidatorClient()
    valid_rental = ValidatorRental()
   
    file_repo_carti = FileRepoCarti("Carti.txt")
    file_repo_clienti = FileRepoClienti("Clienti.txt")
    file_repo_rental = FileRepoRental("Rentals.txt")
    
    repo_carti = RepoCarti()
    repo_clienti = RepoClienti()
    repo_rental = RepoRental()
    
    srv_carti = ServiceCarti(valid_carte, file_repo_carti)
    srv_clienti = ServiceClienti(valid_client, file_repo_clienti)
    srv_rental = ServiceRental(valid_rental, file_repo_carti, file_repo_clienti, file_repo_rental)
    
    ui = Consola(srv_carti, srv_clienti,srv_rental)
    teste = Teste()
    teste.run_teste()
    
    ui.run()
    
    