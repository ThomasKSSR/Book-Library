from domain.entitati import Client,Carte,Rental
from errors.exceptii import AlreadyReturned,SrvError
from domain.sortari import InsertionSorter,CombSorter
import random
import string
import operator
from domain.dtos import RentalDTO, showRentalsDTO,Raport1DTO,Raport2DTO, Raport3DTO
class ServiceCarti(object):
    
    
    def __init__(self, valid_carte, repo_carti):
        self.__valid_carte = valid_carte
        self.__repo_carti = repo_carti
    
    def add_carte(self,id_carte, titlu, descriere, autor):
        carte = Carte(id_carte, titlu, descriere, autor)
        self.__valid_carte.valideaza(carte)
        self.__repo_carti.adauga_carte(carte)
    
    def cauta_carte_dupa_id(self,id_carte,):
        self.__valid_carte.valideaza_id(id_carte)
        carte = self.__repo_carti.cauta_carte_dupa_id(id_carte)
        return carte
   
    def cauta_carte_dupa_titlu(self,titlu_carte):
        self.__valid_carte.valideaza_titlu(titlu_carte)
        carte = self.__repo_carti.cauta_carte_dupa_titlu(titlu_carte)
        return carte 
    """
    def sterge_carte(self,id_del):
        self.__valid_carte.valideaza_id(id_del)
        self.__repo_carti.sterge_carte(id_del)
    """
    def show_rec(self,lista):
            if len(lista) == 0:
                return ""
            else:
                return str(lista.pop(0)) +"\n"+ self.show_rec(lista)
    
    def show_carti(self):
        st = ""
        carti = self.__repo_carti.get_all_carti()
        for carte in carti:
            st += str(carte) +"\n"
        return st
    
    def show_carti_rec(self):
        carti = self.__repo_carti.get_all_carti()[:]
        return carti
        
    def modify_carte_all(self, id_modify, titlu_modify, descriere_modify, autor_modify):
        self.__valid_carte.valideaza_id(id_modify)
        carte_valid = Carte(id_modify, titlu_modify, descriere_modify, autor_modify)
        self.__valid_carte.valideaza(carte_valid)
        
        carte = self.__repo_carti.cauta_carte_dupa_id(id_modify)
        carte_new = Carte(id_modify,titlu_modify,descriere_modify,autor_modify)
        self.__repo_carti.modify_carti_all(carte_new)
    
        

class ServiceClienti(object):
    
    
    def __init__(self, valid_client, repo_clienti):
        self.__valid_client = valid_client
        self.__repo_clienti = repo_clienti
    
    def add_client(self,id_client, nume_client, cnp_client):
        client = Client(id_client,nume_client,cnp_client)
        self.__valid_client.valideaza_client(client)
        self.__repo_clienti.adauga_client(client)
    
    def cauta_client_dupa_id(self,id_client):
        self.__valid_client.valideaza_id(id_client)
        client = self.__repo_clienti.cauta_client_dupa_id(id_client)
        return client
    """
    def sterge_client(self,id_del):
        self.__valid_client.valideaza_id(id_del)
        self.__repo_clienti.sterge_client(id_del)
    """
    def show_clienti(self):
        lista_clienti = self.__repo_clienti.get_all_clients()
        st = ""
        for client in lista_clienti:
            st += str(client) + "\n"
        return st
    
    def show_rec(self,lista):
            if len(lista) == 0:
                return ""
            else:
                return str(lista.pop(0)) +"\n"+ self.show_rec(lista)
    
    def show_clienti_rec(self):
        lista_clienti = self.__repo_clienti.get_all_clients()
        return lista_clienti
        

    
    def modify_client_all(self, id_modify, nume_modify, cnp_modify):
        self.__valid_client.valideaza_id(id_modify)
        client = self.__repo_clienti.cauta_client_dupa_id(id_modify)
        
        client_valid = Client(id_modify, nume_modify, cnp_modify)
        self.__valid_client.valideaza_client(client_valid)
        
        client_new = Client(id_modify,nume_modify,cnp_modify)
        self.__repo_clienti.modify_client_all(client_new)
        
         
        
    
    def min_client_nume(self):
        min = self.__repo_clienti.min_client_nume()
        return min
    
    def add_random_client_r(self,nr):
        if nr == 0:
            return
        id = random.randint(0,1000000000)
        nume = ''.join((random.choice(string.ascii_letters)) for i in range(5,10))
        cnp = random.randint(1000000000000, 9000000000000)
        nr = nr-1
        client = Client(id,nume,cnp)
        self.__valid_client.valideaza_client(client)
        self.__repo_clienti.adauga_client(client)
        return self.add_random_client_r(nr)
    
    """
    def add_random_client(self,l):
        while(l):
            id = random.randint(0,1000000000)
            nume = ''.join((random.choice(string.ascii_letters)) for i in range(5,10))
            cnp = random.randint(1000000000000, 9000000000000)
            l = l-1
            client = Client(id,nume,cnp)
            self.__valid_client.valideaza_client(client)
            self.__repo_clienti.adauga_client(client)
    """ 
            
        

class ServiceRental(object):
    
    
    def __init__(self, valid_rental, repo_carti, repo_clienti, repo_rental):
        self.__valid_rental = valid_rental
        self.__repo_carti = repo_carti
        self.__repo_clienti = repo_clienti
        self.__repo_rental = repo_rental
    
    
    def get_all_rentals_service(self):
        rentalDTOs = self.__repo_rental.get_all_rentals()
        rentals = []
        for rentalDTO in rentalDTOs:
            carte = self.__repo_carti.cauta_carte_dupa_id(rentalDTO.get_id_carte())
            client = self.__repo_clienti.cauta_client_dupa_id(rentalDTO.get_id_client())
            
            rental = Rental(rentalDTO.get_id_rental(),carte,client,rentalDTO.get_data_rental())
            rental.set_data_return(rentalDTO.get_data_return())
            
            rentals.append(rental)
        return rentals
    
    def add_rental(self,id_rental, id_carte, id_client, data_rental):
        self.__valid_rental.valideaza_id(id_carte)
        self.__valid_rental.valideaza_id(id_client)
        self.__valid_rental.valideaza_id(id_rental)
        self.__valid_rental.valideaza_data(data_rental)
        
        carte = self.__repo_carti.cauta_carte_dupa_id(id_carte)
        client = self.__repo_clienti.cauta_client_dupa_id(id_client)
        
        rentalDTO = RentalDTO(id_rental,id_carte,id_client,data_rental)
        self.__repo_rental.adauga_rental(rentalDTO)
        
        rental = Rental(id_rental,carte,client,data_rental)
        return rental
    
    def sterge_carte(self,id_del):
        self.__valid_rental.valideaza_id(id_del)
        carte = self.__repo_carti.cauta_carte_dupa_id(id_del)
    
        rentals = self.get_all_rentals_service()
        
        for rental in rentals:
            if rental.get_carte().get_id_carte() == id_del:
                id_del_rental = rental.get_id_rental()
                self.__repo_rental.sterge_rental_dupa_id(id_del_rental)
        self.__repo_carti.sterge_carte(id_del)
        

    def return_carte_dupa_id_rental(self,id_return,data_return):
        self.__valid_rental.valideaza_id(id_return)
        self.__valid_rental.valideaza_data(data_return)
        rentalDTO = self.__repo_rental.cauta_rental_dupa_id(id_return)
        rentals = self.__repo_rental.get_all_rentals()
        for rental in rentals:
            if rental.get_id_rental() == id_return:
                if rental.get_data_return() != None:
                    raise AlreadyReturned("Cartea a fost deja returnata!")
                
                if rental.get_data_return() == None:
                    self.__repo_rental.modify_rental_all(id_return,rentalDTO.get_id_carte(),rentalDTO.get_id_client(),rentalDTO.get_data_rental(),data_return)
                
                
        
    def sterge_client(self,id_del):
        self.__valid_rental.valideaza_id(id_del)
        client = self.__repo_clienti.cauta_client_dupa_id(id_del)
        
        rentals = self.get_all_rentals_service()
        
        for rental in rentals:
            if rental.get_client().get_id_client() == id_del:
                id_rental_del = rental.get_id_rental()
                self.__repo_rental.sterge_rental_dupa_id(id_rental_del)
                
        self.__repo_clienti.sterge_client(id_del)
        
    
    def show_all_rentals(self):
        rentals = self.get_all_rentals_service()
        
        clients = self.__repo_clienti.get_all_clients()
        dct = {}
        for rental in rentals:
            if str(rental.get_client()) not in dct:
                dct[str(rental.get_client())] = []
            carte = rental.get_carte()
            dct[str(rental.get_client())].append(str(carte))
        
        rezultat = []
        for key,values in dct.items():
            
            showDTO = showRentalsDTO(key,values[:])
            
            rezultat.append(str(showDTO))
        return rezultat
        
                    
    def cauta_rental_dupa_id(self,id_rental):
        self.__valid_rental.valideaza_id(id_rental)
        rental = self.__repo_rental.cauta_rental_dupa_id(id_rental)
        return rental

    
    def sterge_rental_dupa_id(self, id_rental):
        self.__valid_rental.valideaza_id(id_rental)
        self.__repo_rental.cauta_rental_dupa_id(id_rental)
        
        self.__repo_rental.sterge_rental_dupa_id(id_rental)

    
    def modify_rental_all(self, id_rental_modify, id_carte_modify, id_client_modify, data_rental, data_returned):
        self.__valid_rental.valideaza_id(id_rental_modify)
        self.__valid_rental.valideaza_data(data_rental)
        carte = self.__repo_carti.cauta_carte_dupa_id(id_carte_modify)
        client = self.__repo_clienti.cauta_client_dupa_id(id_client_modify)
        self.__repo_rental.modify_rental_all(id_rental_modify,id_carte_modify,id_client_modify,data_rental,data_returned)

    
    def raport_cele_mai_inchiriate_carti(self):
        #returneaza cele mai inchiriate carti 
        #ouput: st-str
        carti = self.__repo_carti.get_all_carti()
        rentals = self.get_all_rentals_service()
        
        dict_carti = {}
        if len(rentals) == 0:
            raise SrvError("Nu exista inchirieri!")
        for rental in rentals:
            carte = rental.get_carte()
            titlu = carte.get_titlu()
            if titlu not in dict_carti:
                dict_carti[titlu] = 1
            else:
                dict_carti[titlu] += 1
            
        #dict_carti = dict(sorted(dict_carti.items(),key = operator.itemgetter(1),reverse = True))
        #return dict_carti
        list_dto = []
        for titlu,rentals in dict_carti.items():
            raport = Raport1DTO(titlu,rentals)
            list_dto.append(raport)
        
        sorter = InsertionSorter()
        sorter.sort(list_dto, key = lambda raport:(raport.get_rentals(),raport.get_titlu()))
        return list_dto
            

    
    def raport2_nume(self):
        #returneaza clientii sortati in functie de nume
        #ouput: st-str
        clienti = self.__repo_clienti.get_all_clients()
        rentals = self.get_all_rentals_service()
        
        dict_clienti = {}
        if len(rentals) == 0:
            raise SrvError("Nu exista inchirieri!")
        for rental in rentals:
            
            client = rental.get_client()
            nume = client.get_nume_client()
            if nume not in dict_clienti:
                dict_clienti[nume] = 1
            else:
                dict_clienti[nume] +=1
        #dict_clienti = dict(sorted(dict_clienti.items(), key = operator.itemgetter(0)))        
        #st = ""
        #for key,value in dict_clienti.items():
            #st += str(key) +" "+str(value) + " carti\n"
        
        list_dto = []
        for nume,carti in dict_clienti.items():
            raport2 = Raport2DTO(nume,carti)
            list_dto.append(raport2)
        
        sorter = InsertionSorter()
        sorter.sort(list_dto,key = lambda raport: raport.get_nume())
        return list_dto

    
    def raport2_nr_carti(self):
        #returneaza un dictionar cu clienti sortati in functie de numarul de carti inchiriate
        #output st -str
        rentals = self.get_all_rentals_service()
        
        dict_clienti = {}
        if len(rentals) == 0:
            raise SrvError("Nu exista inchirieri!")
        for rental in rentals:
            client = rental.get_client()
            nume = client.get_nume_client()
            if nume not in dict_clienti:
                dict_clienti[nume] = 1
            else:
                dict_clienti[nume] +=1
        #dict_clienti = dict(sorted(dict_clienti.items(), key = operator.itemgetter(1),reverse = True))        
        #st = ""
        #for key,value in dict_clienti.items():
            #st += str(key) +" "+str(value) + " carti\n"
        
        list_dto = []
        for nume,carti in dict_clienti.items():
            raport2 = Raport2DTO(nume,carti)
            list_dto.append(raport2)
        
        sorter = CombSorter()
        sorter.sort(list_dto,key = lambda raport: raport.get_carti(),reverse = True)
        
        return list_dto

    
    def raport3(self):
        #returneza un dicitonar cu cei mai activi clienti(nume client si numarul de carti inchiriate)
        #output dict_clienti - dictionar
        
        rentals = self.get_all_rentals_service()
        
        dict_clienti = {}
        if len(rentals) == 0:
            raise SrvError("Nu exista inchirieri!")
        for rental in rentals:
            client = rental.get_client()
            nume = client.get_nume_client()
            if nume not in dict_clienti:
                dict_clienti[nume] = 1
            else:
                dict_clienti[nume] +=1
        dict_clienti = dict(sorted(dict_clienti.items(), key = operator.itemgetter(1),reverse = True))        
        
        #l = len(dict_clienti)
        #l = int(l*0.2)
        #if l< 1:
            #l = 1
        #nr =0
        #st = ""
        #for key,value in dict_clienti.items():
            #st += str(key) +" "+str(value) + " carti\n"
            #nr += 1
            #if nr ==l:
                #return st
        list_dto = []
        for nume,carti in dict_clienti.items():
            raport3 = Raport3DTO(nume,carti)
            list_dto.append(raport3)
        
        sorter = InsertionSorter()
        sorter.sort(list_dto,key = lambda raport: raport.get_carti(),reverse = True)
        return list_dto
    
    """
    def raport4(self):
        carti = self.__repo_carti.get_all_carti()
        rentals = self.get_all_rentals_service()
        dict_carti = {}
        if len(rentals) == 0:
            raise SrvError("Nu exista inchirieri!")
        for rental in rentals:
            carte = rental.get_carte()
            titlu = carte.get_titlu()
            if titlu not in dict_carti:
                    dict_carti[titlu] = 1
            else:
                dict_carti[titlu] += 1
            
        dict_carti = dict(sorted(dict_carti.items(),key = operator.itemgetter(1),reverse = True))
        nr = 1
        st = ""
        for key,value in dict_carti.items():
            if nr <=3:
                st += str(key)+ " " +str(value) + " rentals\n"
        return st
    """
            
            
        
                
            
                
    
    
    
    
    
    
        
    
    
    
    
    