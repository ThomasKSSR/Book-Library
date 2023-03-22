from domain.entitati import Carte, Client, Rental
from validare.validator import ValidatorCarte, ValidatorClient, ValidatorRental
from errors.exceptii import ValidationError, RepoError, AlreadyReturned,\
    SrvError
from infrastructura.repozitorii import RepoCarti, RepoClienti, RepoRental,FileRepoCarti,\
    FileRepoClienti, FileRepoRental
from business.servicii import ServiceRental, ServiceCarti, ServiceClienti
from domain.dtos import RentalDTO
import unittest
from domain.sortari import InsertionSorter, CombSorter
import random
class Teste(unittest.TestCase):
    
 #teste carti--------------------------------------------------------   
    def __test_creeaza_carte_succes(self, id_carte, titlu, descriere, autor,descriere_noua):
        carte = Carte(id_carte, titlu, descriere, autor)
        self.assertTrue(carte.get_id_carte() == id_carte)
        self.assertTrue(carte.get_titlu() == titlu)
        self.assertTrue(carte.get_descriere() == descriere)
        self.assertTrue(carte.get_autor() == autor)
        carte.set_descriere(descriere_noua)
        self.assertTrue(carte.get_descriere() == descriere_noua)
        return carte

    def __test_egalitate_carti(self, carte, id_carte, alt_titlu, descriere, autor):
        alta_carte_acelasi_id = Carte(id_carte, alt_titlu, descriere, autor)
        self.assertTrue( alta_carte_acelasi_id == carte )
    
    
    def __test_pretty_print_carte(self, carte):
        self.assertTrue( str(carte) == "[23]The Shining by Stephen King (Thriller)") 
    
    
    def __creeaza_carte_test(self):
        id_carte = 23
        titlu = "The Shining"
        descriere = "Horror"
        autor = "Stephen King"
        descriere_noua = "Thriller"
        carte = self.__test_creeaza_carte_succes(id_carte, titlu, descriere, autor, descriere_noua)
        alt_titlu = "Carrie"
        self.__test_egalitate_carti(carte, id_carte, alt_titlu, descriere, autor)
        self.__test_pretty_print_carte(carte)
        
    
    
    def __test_valideaza_carte_succes(self, id_carte, titlu, descriere, autor):
        carte = Carte(id_carte, titlu, descriere, autor)
        valid_carte = ValidatorCarte()
        valid_carte.valideaza(carte)
        self.assertTrue
        return valid_carte
    
    def __test_valideaza_carte_invalida(self, inv_id_carte, inv_titlu, inv_descriere, inv_autor, valid_carte):
        carte_invalida = Carte(inv_id_carte, inv_titlu, inv_descriere, inv_autor)
        try:
            valid_carte.valideaza(carte_invalida)
            self.assertFalse
        except ValidationError as ve:
            self.assertTrue(str(ve) == "id invalid!\ntitlu invalid!\ndescriere invalida!\nautor invalid!\n")
            
        
    
    
    def __test_vallideaza_carte(self):
        id_carte = 23
        titlu = "The Shining"
        descriere = "Horror"
        autor = "Stephen King"
        valid_carte = self.__test_valideaza_carte_succes(id_carte, titlu, descriere, autor)
        inv_id_carte = -23
        inv_titlu = ""
        inv_descriere = ""
        inv_autor = ""
        self.__test_valideaza_carte_invalida(inv_id_carte, inv_titlu, inv_descriere, inv_autor, valid_carte)
    

    def __test_creeaza_repo_vid(self):
        with open("testare/test_carti.txt", "w") as f:
            f.write("")
        repo = FileRepoCarti("testare/test_carti.txt")
        self.assertTrue(len(repo) == 0)
        return repo
    
    
    def test_adauga_carte_succes(self, carte, repo):
        repo.adauga_carte(carte)
        self.assertTrue(len(repo)>0)
    
    
    def test_adauga_carte_same_id(self, carte2, repo):
        try:
            repo.adauga_carte(carte2)
            self.assertFalse
        except RepoError as re:
            self.assertTrue( str(re) == "Id carte existent!")
            
                    
    
    
    def __test_adauga_carte_repo(self):
        repo = self.__test_creeaza_repo_vid()
        id_carte = 23
        titlu = "The Shining"
        descriere = "Horror"
        autor = "Stephen King"
        carte = Carte(id_carte, titlu, descriere, autor)
        self.test_adauga_carte_succes(carte,repo)
        id_carte = 23
        titlu = "Carrie"
        descriere = "Horror"
        autor = "Stephen King"
        carte2 = Carte(id_carte, titlu, descriere, autor)
        self.test_adauga_carte_same_id(carte2,repo)
        
        
    
    
    def __test_cauta_carte_dupa_id_succes(self, repo, id_cautat,carte):
        carte2 = repo.cauta_carte_dupa_id(id_cautat)
        self.assertTrue( carte2 == carte ) 
                
    
    
    def __test_cauta_carte_dupa_id_inexistent(self, repo, id_inexistent):
        try:
            repo.cauta_carte_dupa_id(id_inexistent)
            self.assertFalse
        except RepoError as re:
            self.assertTrue(str(re) == "Id carte inexistent!")
            

    def __test_cauta_carte(self):
        repo = RepoCarti()
        id_carte = 23
        titlu = "The Shining"
        descriere = "Horror"
        autor = "Stephen King"
        carte = Carte(id_carte, titlu, descriere, autor)
        repo.adauga_carte(carte)
        
        id_cautat = 23
        self.__test_cauta_carte_dupa_id_succes(repo, id_cautat,carte)
        
        id_inexistent = 24
        self.__test_cauta_carte_dupa_id_inexistent(repo,id_inexistent)
    


    def __test_sterge_carte_succes(self, id_del, repo):
        repo.sterge_carte(id_del)
        self.assertTrue(len(repo) == 0)
    
    
    def __test_sterge_carte_id_inexistent(self, id_del, repo):
        try:
            repo.sterge_carte(id_del)
            self.assertFalse
        except RepoError as re:
            self.assertTrue(str(re)=="Id carte inexistent!")
    
    
    def __test_stergere_carte(self):
        repo = self.__test_creeaza_repo_vid()
        id_carte = 23
        titlu = "The Shining"
        descriere = "Horror"
        autor = "Stephen King"
        carte = Carte(id_carte, titlu, descriere, autor)
        repo.adauga_carte(carte)
        id_del = 23
        self.__test_sterge_carte_succes(id_del,repo)
        repo.adauga_carte(carte)
        id_del = 24
        self.__test_sterge_carte_id_inexistent(id_del,repo)

    def __test_show_carti(self):
        repo = RepoCarti()
        id_carte = 23
        titlu = "The Shining"
        descriere = "Horror"
        autor = "Stephen King"
        carte = Carte(id_carte, titlu, descriere, autor)
        repo.adauga_carte(carte)
        id_carte = 24
        titlu = "Carrie"
        descriere = "Horror"
        autor = "Stephen King"
        carte2 = Carte(id_carte, titlu, descriere, autor)
        repo.adauga_carte(carte2)
        
        valid_carte = ValidatorCarte()
        srv_carti = ServiceCarti(valid_carte, repo)
        lista_carti = srv_carti.show_carti()
        self.assertTrue(lista_carti == str(carte)+"\n" +  str(carte2) + "\n")
    
    def __test_modify_carti(self):
        repo = RepoCarti()
        id_carte = 23
        titlu = "The Shining"
        descriere = "Horror"
        autor = "Stephen King"
        carte = Carte(id_carte, titlu, descriere, autor)
        repo.adauga_carte(carte)
        
        id_carte_modify = 23
        titlu_modify = "Carrie"
        descriere_modify = "Thriller"
        autor_modify = "Stephen King"
        carte_modify = Carte(id_carte_modify, titlu_modify, descriere_modify, autor_modify)
        
        valid_carte = ValidatorCarte()
        srv_carti = ServiceCarti(valid_carte, repo)
        srv_carti.modify_carte_all(id_carte_modify, titlu_modify, descriere_modify, autor_modify)
        lista_carti = srv_carti.show_carti()
        self.assertTrue(lista_carti == str(carte_modify) + "\n")
        
#----------------------------------------------------------------------------------------------------------------  

#teste clienti-------------------------------------------------------------------------------------------------
    
    
    def __test_creeaza_client_succes(self, id_client, nume_client, cnp_client):
        client = Client(id_client, nume_client, cnp_client)
        self.assertTrue(client.get_id_client() == id_client)
        alt_nume = "Bogdan"
        client.set_nume_client(alt_nume)
        self.assertTrue(client.get_nume_client() == alt_nume)
        self.assertTrue(client.get_cnp_client() == cnp_client)
        return client
    

    def __test_pretty_print_client(self, client):
        self.assertTrue(str(client) == "[23]Bogdan -> 5021023201234")
        
    
    def __test_creeaza_client(self):
        id_client= 23
        nume_client = "Andrei"
        cnp_client = 5021023201234
        client = self.__test_creeaza_client_succes(id_client , nume_client, cnp_client)
        self.__test_pretty_print_client(client)
    
    
    def __test_valideaza_client(self):
        id_invalid= -23
        nume_invalid = ""
        cnp_invalid = 502102320123
        client = Client(id_invalid, nume_invalid, cnp_invalid)
        valid = ValidatorClient()
        try:
            valid.valideaza_client(client)
            self.assertFalse
        except ValidationError as ve:
            self.assertTrue( str(ve) == "Id invalid!\nNume invalid!\nCNP invalid!\n")
    
    
    
    def __test_adauga_client_repo_succes(self, client, repo):
        repo.adauga_client(client)
        self.assertTrue(len(repo) > 0)
        return repo
    

    def __test_adauga_client_same_id_cnp(self, client_same_id_cnp, repo):
        try:
            repo.adauga_client(client_same_id_cnp)
            self.assertFalse
        except RepoError as re:
            self.assertTrue(str(re) == "Id si/sau CNP existent!\n")
    
    
    def __test_adauga_client_repo(self):
        with open("testare/test_clienti.txt", "w") as f:
            f.write("")
        repo= FileRepoClienti("testare/test_clienti.txt")
        
        id_client= 23
        nume_client = "Andrei"
        cnp_client = 5021023201234
        client = Client(id_client, nume_client, cnp_client)
        repo = self.__test_adauga_client_repo_succes(client, repo)
        
        nume_alt = "Bogdan"
        client_same_id_cnp = Client(id_client, nume_alt, cnp_client)
        self.__test_adauga_client_same_id_cnp(client_same_id_cnp, repo)
        
    
    def __test_cauta_client_dupa_id_succes(self, id_cautat, client, repo):
        client_cautat = repo.cauta_client_dupa_id(id_cautat)
        self.assertTrue( client_cautat == client)
        
    
    def __test_cauta_client_dupa_id_inexistent(self, id_cautat, client, repo):
        try:
            client_cautat = repo.cauta_client_dupa_id(id_cautat)
        except RepoError as re:
            self.assertTrue(str(re) == "Id client inexistent!")
            
    
    
    def __test_cauta_client(self):
        repo= RepoClienti()
        id_client= 23
        nume_client = "Andrei"
        cnp_client = 5021023201234
        client = Client(id_client, nume_client, cnp_client)
        id_cautat = 23
        repo = self.__test_adauga_client_repo_succes(client, repo)
        
        self.__test_cauta_client_dupa_id_succes(id_cautat,client,repo)
        id_cautat = 24
        self.__test_cauta_client_dupa_id_inexistent(id_cautat,client,repo)
    
    
    def __test_sterge_client_cu_succes(self, id_del, repo):
        repo.sterge_client(id_del)
        self.assertTrue(len(repo) == 0)
    
    
    def __test_sterge_client_id_inexistent(self, id_del, repo):
        try:
            repo.sterge_client(id_del)
            self.assertFalse
        except RepoError as re:
            self.assertTrue(str(re) == "Id client inexistent!")
    
    
    def __test_sterge_client(self):
        repo= RepoClienti()
        id_client= 23
        nume_client = "Andrei"
        cnp_client = 5021023201234
        client = Client(id_client, nume_client, cnp_client)
        repo.adauga_client(client)
        id_del = 23
        self.__test_sterge_client_cu_succes(id_del,repo)
        id_del = 24
        repo.adauga_client(client)
        self.__test_sterge_client_id_inexistent(id_del, repo)
    
    
    
    def __test_show_clienti(self):
        repo= RepoClienti()
        id_client= 23
        nume_client = "Andrei"
        cnp_client = 5021023201234
        client = Client(id_client, nume_client, cnp_client)
        repo.adauga_client(client)
        id_client = 24
        nume_client = "Marius"
        cnp_client = 5021023204321
        client2 = Client(id_client, nume_client, cnp_client)
        repo.adauga_client(client2)
        
        valid_client = ValidatorClient()
        srv_clienti = ServiceClienti(valid_client,repo)
        clienti = srv_clienti.show_clienti()
        self.assertTrue(clienti == str(client) + "\n" +str(client2) + "\n")
        
        
        
    
    
    
    
    def __test_modify_clienti(self):
        repo= RepoClienti()
        id_client= 23
        nume_client = "Andrei"
        cnp_client = 5021023201234
        client = Client(id_client, nume_client, cnp_client)
        repo.adauga_client(client)
        
        id_modify = 23
        nume_modify = "Alex"
        cnp_modify = 5021023204321
        client_modify = Client(id_modify, nume_modify, cnp_modify)
        
        valid_client = ValidatorClient()
        srv_client = ServiceClienti(valid_client,repo)
        
        srv_client.modify_client_all(id_modify, nume_modify, cnp_modify)
        
        lista_clienti = srv_client.show_clienti()
        self.assertTrue(lista_clienti == str(client_modify) + "\n")
        
    
#-----------------------------------------------------------------------------------------------------
#teste Rental
    

    def __test_creeaza_rental_succes(self, id_rental, carte, client, data_rental):
        rental = Rental(id_rental,carte,client,data_rental)
        self.assertTrue(rental.get_carte() == carte)
        self.assertTrue(rental.get_client() == client)
        self.assertTrue(rental.get_data_rental() == data_rental)
    
    def __test_creeaza_rental(self):
        repocarti = RepoCarti()
        id_carte = 23
        titlu = "The Shining"
        descriere = "Horror"
        autor = "Stephen King"
        carte = Carte(id_carte, titlu, descriere, autor)
        
        repoclienti = RepoClienti()
        id_client = 25
        nume_client = "Andrei"
        cnp_client = 5021023201234
        client = Client(id_client,nume_client,cnp_client)
        
        reporental = RepoRental()
        id_rental = str(id_carte) + str(id_client)
        data_rental = (2020,12,20)
        self.__test_creeaza_rental_succes(id_rental,carte,client,data_rental)
     
       
    
    def __test_adauga_rental_succes(self, reporental, rental):
            reporental.adauga_rental(rental)
            self.assertTrue(len(reporental) > 0)
          
    
    def __test_adauga_rental_notreturned(self, rental2, reporental):
        try:
            reporental.adauga_rental(rental2)
            self.assertFalse
        except RepoError as re:
            self.assertTrue(str(re) == "Cartea nu a fost inca returnata!")
            
    
    
    def __test_adauga_rental(self):
        repocarti = RepoCarti()
        id_carte = 23
        titlu = "The Shining"
        descriere = "Horror"
        autor = "Stephen King"
        carte = Carte(id_carte, titlu, descriere, autor)
        
        repoclienti = RepoClienti()
        id_client = 25
        nume_client = "Andrei"
        cnp_client = 5021023201234
        client = Client(id_client,nume_client,cnp_client)
        
        reporental = RepoRental()
        id_rental = str(id_carte) + str(id_client)
        data_rental = (2020,12,20)
        rental = Rental(id_rental,carte,client,data_rental)
        self.__test_adauga_rental_succes(reporental,rental)
        
        id_rental2 = 2423
        rental2 = Rental(id_rental2, carte, client, data_rental)
        self.__test_adauga_rental_notreturned(rental2,reporental)
        
    
    def __test_valideaza_rental(self):
        pass
    

    def __test_cauta_rental_succes(self, id_rental, reporental):
        rental = reporental.cauta_rental_dupa_id(id_rental)
        self.assertTrue(rental.get_id_rental() == id_rental)
    
    
    def __test_cauta_rental_id_inexistent(self, id_rental_inexistent, reporental):
        try:
            reporental.cauta_rental_dupa_id(id_rental_inexistent)
            self.assertFalse
        except RepoError as re:
            self.assertTrue(str(re) == "Id inchiriere inexistent!")
    
    
    def __test_cauta_rental(self):
        repocarti = RepoCarti()
        id_carte = 23
        titlu = "The Shining"
        descriere = "Horror"
        autor = "Stephen King"
        carte = Carte(id_carte, titlu, descriere, autor)
        
        repoclienti = RepoClienti()
        id_client = 25
        nume_client = "Andrei"
        cnp_client = 5021023201234
        client = Client(id_client,nume_client,cnp_client)
        
        reporental = RepoRental()
        id_rental = str(id_carte) + str(id_client)
        data_rental = (2020,12,20)
        rental = Rental(id_rental,carte,client,data_rental)
        reporental.adauga_rental(rental)
        self.__test_cauta_rental_succes(id_rental,reporental)
        id_rental_inexistent = 0
        self.__test_cauta_rental_id_inexistent(id_rental_inexistent,reporental)
    

#---------------------------------------------------------------------------------------------------------------
#Teste Service Rental
    
    def __test_srv_adauga_rental_succes(self, id_rental, id_carte, id_client, data_rental, srv_rental, reporental):
        srv_rental.add_rental(id_rental, id_carte, id_client, data_rental)
        self.assertTrue(len(reporental) > 0)

        
    
    def __creeaza_repo_vid_rental(self):
        with open("testare/test_rentals.txt", "w") as f:
            f.write("")
        repo = FileRepoRental("testare/test_rentals.txt")
        return repo
    
    
    
    def __test_rental_service_add_rental(self):
        repocarti = self.__test_creeaza_repo_vid()
        id_carte = 23
        titlu = "The Shining"
        descriere = "Horror"
        autor = "Stephen King"
        carte = Carte(id_carte, titlu, descriere, autor)
        repocarti.adauga_carte(carte)
        
        repoclienti = RepoClienti()
        id_client = 25
        nume_client = "Andrei"
        cnp_client = 5021023201234
        client = Client(id_client,nume_client,cnp_client)
        repoclienti.adauga_client(client)
        
        reporental = self.__creeaza_repo_vid_rental()
        id_rental = 30
        data_rental = "20/12/2002"
        valid_rental = ValidatorRental()
        srv_rental = ServiceRental(valid_rental,repocarti,repoclienti,reporental)
        self.__test_srv_adauga_rental_succes(id_rental,id_carte,id_client,data_rental,srv_rental, reporental)
    
    def __test_srv_return_carte_succes(self, id_rental_returned, data_returned, reporental, srv_rental):
        rental = reporental.cauta_rental_dupa_id(id_rental_returned)
        self.assertTrue(rental.get_data_return() == None) 
        srv_rental.return_carte_dupa_id_rental(id_rental_returned, data_returned)
        rental = reporental.cauta_rental_dupa_id(id_rental_returned)
        self.assertTrue(rental.get_data_return() == data_returned)
        
    def __test_srv_return_carte_deja_returnata(self, id_rental_returned, data_returned, reporental, srv_rental):
        rental = reporental.cauta_rental_dupa_id(id_rental_returned)
        self.assertTrue(rental.get_data_return() == data_returned)
        try:
            srv_rental.return_carte_dupa_id_rental(id_rental_returned,data_returned)
            self.assertFalse
        except AlreadyReturned  as ar:
           self.assertTrue(str(ar)== "Cartea a fost deja returnata!")
        
    
    def __test_returneaza_carte_service(self):
        repocarti = RepoCarti()
        id_carte = 23
        titlu = "The Shining"
        descriere = "Horror"
        autor = "Stephen King"
        carte = Carte(id_carte, titlu, descriere, autor)
        repocarti.adauga_carte(carte)
        
        repoclienti = RepoClienti()
        id_client = 25
        nume_client = "Andrei"
        cnp_client = 5021023201234
        client = Client(id_client,nume_client,cnp_client)
        repoclienti.adauga_client(client)
        
        reporental = RepoRental()
        id_rental = 30
        data_rental = "20/12/2002"
        valid_rental = ValidatorRental()
        srv_rental = ServiceRental(valid_rental,repocarti,repoclienti,reporental)
        self.__test_srv_adauga_rental_succes(id_rental,id_carte,id_client,data_rental,srv_rental, reporental)
        
        id_rental_returned = 30
        data_returned = "12/08/2008"
        self.__test_srv_return_carte_succes(id_rental_returned, data_returned, reporental, srv_rental)
    
        self.__test_srv_return_carte_deja_returnata(id_rental_returned, data_returned, reporental, srv_rental)
    

    def __test_srv_sterge_carte_succes(self, id_carte_del, srv_rental, repocarti, reporental):
        self.assertTrue(len(repocarti) == 1)
        self.assertTrue(len(reporental) == 1)
        srv_rental.sterge_carte(id_carte_del)
        self.assertTrue(len(repocarti) == 0)
        self.assertTrue(len(reporental) == 0)
    

    def __test_srv_sterge_carte_id_inexistent(self, id_carte_del, srv_rental, repocarti, reporental):
        self.assertTrue(len(repocarti) == 1)
        try:
            srv_rental.sterge_carte(id_carte_del)
        except RepoError as re:
            self.assertTrue(str(re) == "Id carte inexistent!")
        self.assertTrue(len(repocarti) == 1)
        
    
    
    def __test_sterge_carte_srv_rental(self):
        repocarti = RepoCarti()
        id_carte = 23
        titlu = "The Shining"
        descriere = "Horror"
        autor = "Stephen King"
        carte = Carte(id_carte, titlu, descriere, autor)
        repocarti.adauga_carte(carte)
        
        repoclienti = RepoClienti()
        id_client = 25
        nume_client = "Andrei"
        cnp_client = 5021023201234
        client = Client(id_client,nume_client,cnp_client)
        repoclienti.adauga_client(client)
        
        reporental = RepoRental()
        id_rental = 30
        data_rental = "20/12/2002"
        valid_rental = ValidatorRental()
        srv_rental = ServiceRental(valid_rental,repocarti,repoclienti,reporental)
        self.__test_srv_adauga_rental_succes(id_rental,id_carte,id_client,data_rental,srv_rental, reporental)
        
        id_carte_del = 23
        self.__test_srv_sterge_carte_succes(id_carte_del,srv_rental,repocarti,reporental)
        
        repocarti.adauga_carte(carte)
        id_carte_del = 25
        self.__test_srv_sterge_carte_id_inexistent(id_carte_del,srv_rental,repocarti,reporental)
    

    def __test_srv_sterge_client_succes(self, id_client_del, repoclienti, reporental, srv_rental):
        self.assertTrue(len(repoclienti) == 1)
        self.assertTrue(len(reporental) == 1)
        srv_rental.sterge_client(id_client_del)
        self.assertTrue(len(repoclienti) == 0)
        self.assertTrue(len(reporental) == 0)
    
    
    def __test_sterge_client_srv_rental(self):
        repocarti = RepoCarti()
        id_carte = 23
        titlu = "The Shining"
        descriere = "Horror"
        autor = "Stephen King"
        carte = Carte(id_carte, titlu, descriere, autor)
        repocarti.adauga_carte(carte)
        
        repoclienti = RepoClienti()
        id_client = 25
        nume_client = "Andrei"
        cnp_client = 5021023201234
        client = Client(id_client,nume_client,cnp_client)
        repoclienti.adauga_client(client)
        
        reporental = RepoRental()
        id_rental = 30
        data_rental = "20/12/2002"
        valid_rental = ValidatorRental()
        srv_rental = ServiceRental(valid_rental,repocarti,repoclienti,reporental)
        self.__test_srv_adauga_rental_succes(id_rental,id_carte,id_client,data_rental,srv_rental, reporental)
        
        id_client_del = 25
        self.__test_srv_sterge_client_succes(id_client_del, repoclienti, reporental, srv_rental)
    
    
    def __test_show_all_rentals_srv(self):
        repocarti = RepoCarti()
        carte = Carte(23,"The Shining","Thriller","Stephen King")
        repocarti.adauga_carte(carte)
        
        carte2 = Carte(24,"Carrie","Thriller","Stephen King")
        repocarti.adauga_carte(carte2)
        
        repoclienti = RepoClienti()
        client = Client(25,"Andrei",5021023201234)
        repoclienti.adauga_client(client)
        
        reporental = RepoRental()
        id_rental = 30
        data_rental = "20/12/2002"
        rental = RentalDTO(id_rental, carte.get_id_carte(), client.get_id_client(), data_rental)
        reporental.adauga_rental(rental)
        
        rental2 = RentalDTO(31,carte2.get_id_carte(), client.get_id_client(), data_rental)
        reporental.adauga_rental(rental2)
        
        valid_rental = ValidatorRental()
        srv_rental = ServiceRental(valid_rental,repocarti,repoclienti,reporental)
        
        rentals = srv_rental.show_all_rentals()
        self.assertTrue(len(rentals) == 1)
    
        
    
    def __test_sterge_rental_dupa_id(self):
        id_rental = 24
        carte = Carte(20,"The Shining","Thriller","Stephen King")
        client = Client(21,"Andrei",5021023201234)
        rental = Rental(id_rental,carte,client,"23/12/2020")
        
        valid_rental = ValidatorRental()
        repo_rental = RepoRental()
        repo_carti = RepoCarti()
        repo_clienti = RepoClienti()
        srv_rental = ServiceRental(valid_rental, repo_carti, repo_clienti, repo_rental)
        
        repo_rental.adauga_rental(rental)
        self.assertTrue(len(repo_rental) == 1)
        
        try:
            repo_rental.sterge_rental_dupa_id(25)
        except RepoError as re:
            self.assertTrue(str(re) == "Id inchiriere inexistent!")
        self.assertTrue(len(repo_rental) == 1)
        repo_rental.sterge_rental_dupa_id(id_rental)
        self.assertTrue(len(repo_rental) == 0)
        
        repo_rental.adauga_rental(rental)
        self.assertTrue(len(repo_rental) == 1)
        try:
            srv_rental.sterge_rental_dupa_id(22)
        except RepoError as re:
            self.assertTrue(str(re) == "Id inchiriere inexistent!")
        
        try:
            srv_rental.sterge_rental_dupa_id(-20)
        except ValidationError as ve:
            self.assertTrue(str(ve) == "Id inchiriere invalid!")
        
        self.assertTrue(len(repo_rental) == 1)   
        
        srv_rental.sterge_rental_dupa_id(id_rental)
        self.assertTrue(len(repo_rental) == 0)
         
    
    
    def __test_modify_rental_srv(self):
        id_rental = 24
        carte = Carte(20,"The Shining","Thriller","Stephen King")
        client = Client(21,"Andrei",5021023201234)
        rental = RentalDTO(id_rental,carte.get_id_carte(),client.get_id_client(),"23/12/2020")
        
        valid_rental = ValidatorRental()
        repo_rental = RepoRental()
        repo_rental.adauga_rental(rental)
        repo_carti = RepoCarti()
        repo_carti.adauga_carte(carte)
        repo_clienti = RepoClienti()
        repo_clienti.adauga_client(client)
        srv_rental = ServiceRental(valid_rental, repo_carti, repo_clienti, repo_rental)
        
        carte_modify = Carte(25,"Carrie","Thriller","Stephen King")
        repo_carti.adauga_carte(carte_modify)
        
        client_modify = Client(23,"Marius",5021023204321)
        repo_clienti.adauga_client(client_modify)
        data_rental = "24/09/2019"
        data_returned = None
        
        id_rental_modify = 24
        id_carte_modify = 25
        id_client_modify = 23
        srv_rental.modify_rental_all(id_rental_modify, id_carte_modify, id_client_modify, data_rental, data_returned)
        
        rental = repo_rental.cauta_rental_dupa_id(id_rental_modify)
        self.assertTrue(rental.get_id_carte() == id_carte_modify)
        self.assertTrue(rental.get_id_client() == id_client_modify)
        self.assertTrue(rental.get_data_rental() == data_rental)
        self.assertTrue(rental.get_data_return() == data_returned)
    

    def __test_raport_cele_mai_inchiriate_carti(self):
        valid_rental = ValidatorRental()
        repo_rental = RepoRental()
        repo_carti = RepoCarti()
        repo_clienti = RepoClienti()
        srv_rental = ServiceRental(valid_rental, repo_carti, repo_clienti, repo_rental)
        
        
        self.assertRaises(SrvError,lambda :srv_rental.raport_cele_mai_inchiriate_carti())
        
        carte1 = Carte(20,"The Shining","Thriller","Stephen King")
        repo_carti.adauga_carte(carte1)
        
        carte2 = Carte(24,"Carrie","Thriller","SK")
        repo_carti.adauga_carte(carte2)
        
        
        client1 = Client(21,"Andrei",5021023201234)
        repo_clienti.adauga_client(client1)
        
        client2 = Client(22,"Marius",5021023204321)
        repo_clienti.adauga_client(client2)
        
        
        rental1 = RentalDTO(24,carte1.get_id_carte(),client1.get_id_client(),"23/12/2020")
        repo_rental.adauga_rental(rental1)
        
        rental2 = RentalDTO(25,carte2.get_id_carte(),client2.get_id_client(),"23/12/2020")
        repo_rental.adauga_rental(rental2)
        
        srv_rental.return_carte_dupa_id_rental(24, "24/12/2020")
        rental3 = RentalDTO(26,carte1.get_id_carte(),client2.get_id_client(),"23/12/2020")
        repo_rental.adauga_rental(rental3)
        
        dict_carti = srv_rental.raport_cele_mai_inchiriate_carti()
        
        #self.assertTrue(len(dict_carti) == 2)
        
        
        
    
    
    def __test_raport2(self):
        valid_rental = ValidatorRental()
        repo_rental = RepoRental()
        repo_carti = RepoCarti()
        repo_clienti = RepoClienti()
        srv_rental = ServiceRental(valid_rental, repo_carti, repo_clienti, repo_rental)
        
        self.assertRaises(SrvError,lambda :srv_rental.raport2_nr_carti())
        self.assertRaises(SrvError,lambda :srv_rental.raport2_nume())
        
        carte1 = Carte(20,"The Shining","Thriller","Stephen King")
        repo_carti.adauga_carte(carte1)
        
        carte2 = Carte(24,"Carrie","Thriller","SK")
        repo_carti.adauga_carte(carte2)
        
        
        client1 = Client(21,"Andrei",5021023201234)
        repo_clienti.adauga_client(client1)
        
        client2 = Client(22,"Marius",5021023204321)
        repo_clienti.adauga_client(client2)
        
        
        rental1 = RentalDTO(24,carte1.get_id_carte(),client1.get_id_client(),"23/12/2020")
        repo_rental.adauga_rental(rental1)
        
        rental2 = RentalDTO(25,carte2.get_id_carte(),client2.get_id_client(),"23/12/2020")
        repo_rental.adauga_rental(rental2)
        
        srv_rental.return_carte_dupa_id_rental(24, "24/12/2020")
        rental3 = RentalDTO(26,carte1.get_id_carte(),client2.get_id_client(),"23/12/2020")
        repo_rental.adauga_rental(rental3)
        
        clienti_nume = srv_rental.raport2_nume()
        #self.assertTrue(clienti_nume == str(client1.get_nume_client()) + " 1 carti\n" + str(client2.get_nume_client()) + " 2 carti\n")
        self.assertTrue(len(clienti_nume) == 2)
        
        
        
        
        clienti_carti = srv_rental.raport2_nr_carti()
        #self.assertTrue(clienti_nume == str(client2.get_nume_client()) + " 2 carti\n" + str(client1.get_nume_client()) + " 1 carti\n")
        self.assertTrue(len(clienti_nume) == 2)
        
    
    def __test_raport3(self):
        valid_rental = ValidatorRental()
        repo_rental = RepoRental()
        repo_carti = RepoCarti()
        repo_clienti = RepoClienti()
        srv_rental = ServiceRental(valid_rental, repo_carti, repo_clienti, repo_rental)
        
        carte1 = Carte(20,"The Shining","Thriller","Stephen King")
        repo_carti.adauga_carte(carte1)
        
        carte2 = Carte(24,"Carrie","Thriller","SK")
        repo_carti.adauga_carte(carte2)
        
        
        client1 = Client(21,"Andrei",5021023201234)
        repo_clienti.adauga_client(client1)
        
        client2 = Client(22,"Marius",5021023204321)
        repo_clienti.adauga_client(client2)
        
        
        rental1 = RentalDTO(24,carte1.get_id_carte(),client1.get_id_client(),"23/12/2020")
        repo_rental.adauga_rental(rental1)
        
        rental2 = RentalDTO(25,carte2.get_id_carte(),client2.get_id_client(),"23/12/2020")
        repo_rental.adauga_rental(rental2)
        
        srv_rental.return_carte_dupa_id_rental(24, "24/12/2020")
        rental3 = RentalDTO(26,carte1.get_id_carte(),client2.get_id_client(),"23/12/2020")
        repo_rental.adauga_rental(rental3)
        
        #lista_clienti = srv_rental.raport3()
        #self.assertTrue(lista_clienti == str(client2.get_nume_client()) + " 2 carti\n")
        #self.assertTrue(lista_clienti[client2.get_nume_client()] == 2)
    
    def __test_raport4(self):
        valid_rental = ValidatorRental()
        repo_rental = RepoRental()
        repo_carti = RepoCarti()
        repo_clienti = RepoClienti()
        srv_rental = ServiceRental(valid_rental, repo_carti, repo_clienti, repo_rental)
        
        carte1 = Carte(20,"The Shining","Thriller","Stephen King")
        repo_carti.adauga_carte(carte1)
        
        carte2 = Carte(24,"Carrie","Thriller","SK")
        repo_carti.adauga_carte(carte2)
        
        carte3 = Carte(29,"The Outsider","Thriller","Stephen King")
        repo_carti.adauga_carte(carte3)
        
        client1 = Client(21,"Andrei",5021023201234)
        repo_clienti.adauga_client(client1)
        
        client2 = Client(22,"Marius",5021023204321)
        repo_clienti.adauga_client(client2)
        
        
        rental1 = RentalDTO(24,carte1.get_id_carte(),client1.get_id_client(),"23/12/2020")
        repo_rental.adauga_rental(rental1)
        
        rental2 = RentalDTO(25,carte2.get_id_carte(),client2.get_id_client(),"23/12/2020")
        repo_rental.adauga_rental(rental2)
        
        srv_rental.return_carte_dupa_id_rental(24, "24/12/2020")
        rental3 = RentalDTO(26,carte1.get_id_carte(),client2.get_id_client(),"23/12/2020")
        repo_rental.adauga_rental(rental3)
        
        rental4 = RentalDTO(29,carte3.get_id_carte(),client2.get_id_client(),"21/12/2020")
        repo_rental.adauga_rental(rental4)
        
        #carti = srv_rental.raport4()
        #self.assertTrue(carti == str(carte1.get_titlu()) + " 2 rentals\n" + str(carte2.get_titlu()) + " 1 rentals\n" + str(carte3.get_titlu()) + " 1 rentals\n")
    

    def __test_insert_sort(self):
        sorter = InsertionSorter()
        l = [1,2,3,4,5,6,7,8,9,10]
        random.shuffle(l)
        sorter.sort(l)
        
        assert(l == [1,2,3,4,5,6,7,8,9,10])
        random.shuffle(l)
        sorter.sort(l,reverse = True)
        assert(l == [10,9,8,7,6,5,4,3,2,1])
        
        
    def __test_comb_sort(self):
        sorter = CombSorter()
        l = [1,2,3,4,5,6,7,8,9,10]
        random.shuffle(l)
        
        sorter.sort(l)
        
        
        assert(l == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        
        random.shuffle(l)
        sorter.sort(l,reverse = True)
        assert(l == [10,9,8,7,6,5,4,3,2,1])
        
        
    
    def run_teste(self):
        print("Start all tests")
        self.__creeaza_carte_test()
        self.__test_vallideaza_carte()
        self.__test_adauga_carte_repo()
        self.__test_cauta_carte()
        self.__test_stergere_carte()
        self.__test_show_carti()
        self.__test_modify_carti()
        
        self.__test_creeaza_client()
        self.__test_valideaza_client()
        self.__test_adauga_client_repo()
        self.__test_cauta_client()
        self.__test_sterge_client()
        self.__test_show_clienti()
        self.__test_modify_clienti()

        
        self.__test_creeaza_rental()
        self.__test_adauga_rental()
        self.__test_valideaza_rental()
        self.__test_cauta_rental()
        self.__test_sterge_rental_dupa_id()
        
        self.__test_rental_service_add_rental()
        self.__test_returneaza_carte_service()
        self.__test_sterge_carte_srv_rental()
        self.__test_sterge_client_srv_rental()
        self.__test_show_all_rentals_srv()
        self.__test_modify_rental_srv()
        
        self.__test_raport_cele_mai_inchiriate_carti()
        self.__test_raport2()
        self.__test_raport3()
        self.__test_raport4()
        
        self.__test_insert_sort()
        self.__test_comb_sort()
        print("Finished tests")
    
   



