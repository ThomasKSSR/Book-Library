
from errors.exceptii import RepoError
from domain.entitati import Carte, Client
from domain.dtos import RentalDTO
class RepoCarti(object):
    
    
    def __init__(self):
        self._Carti = []
    
    def __len__(self):
        return len(self._Carti)
    
    
    def adauga_carte(self,carte):
        for i in self._Carti:
            if i == carte:
                raise RepoError("Id carte existent!")
                    
        self._Carti.append(carte)
    
    def cauta_carte_dupa_id(self,id_carte):
        ok  = True
        for carte in self._Carti:
            if carte.get_id_carte() == id_carte:
                return carte
        if ok:
            raise RepoError("Id carte inexistent!")    
    
    def sterge_carte(self,id_del):
        ok = True
        for carte in self._Carti:
            if carte.get_id_carte() == id_del:
                self._Carti.remove(carte)
                ok = False
        if ok:
            raise RepoError("Id carte inexistent!")


    
    def modify_carti_all(self,new_carte):
        ok = True
        for carte in self._Carti:
            if carte.get_id_carte() == new_carte.get_id_carte():
                carte.set_titlu(new_carte.get_titlu())
                carte.set_descriere(new_carte.get_descriere())
                carte.set_autor(new_carte.get_autor())
                ok = False
        if ok:
            raise RepoError("Id inexistent!")
        
    def get_all_carti(self):
        return self._Carti

class FileRepoCarti(RepoCarti):
    def __init__(self,filepath):
        RepoCarti.__init__(self)
        self.__filepath = filepath
    
    def __read_all_from_file_new(self):
        self._Carti = []
        with open(self.__filepath, "r") as f:
            lines = f.readlines()
            nr =0
            for x in range(0,int(len(lines)/4)):
                id_carte = int(lines[nr].strip())
                titlu = lines[nr + 1].strip()
                descriere = lines[nr + 2].strip()
                autor = lines[nr+3].strip()
                carte = Carte(id_carte,titlu,descriere,autor)
                self._Carti.append(carte)
                nr += 4
    
    def __write_all_to_file_new(self):
        with open(self.__filepath, "w") as f:
            for carte in self._Carti:
                f.write(f"{carte.get_id_carte()}\n{carte.get_titlu()}\n{carte.get_descriere()}\n{carte.get_autor()}\n")
    
    def __append_to_file_new(self,carte):
        with open(self.__filepath, "a") as f:
            f.write(f"{carte.get_id_carte()}\n{carte.get_titlu()}\n{carte.get_descriere()}\n{carte.get_autor()}\n")
    
    def __read_all_from_file(self):
        self._Carti = []
        with open(self.__filepath, "r") as f:
            lines = f.readlines()
            for line in lines:
                line = line.strip()
                if len(line) >0:
                    parts = line.split(",")
                    id_carte = int(parts[0])
                    titlu = parts[1]
                    descriere = parts[2]
                    autor = parts[3]
                    carte = Carte(id_carte,titlu,descriere,autor)
                    self._Carti.append(carte)
                
                
    def __write_all_to_file(self):
        with open(self.__filepath, "w") as f:
            for carte in self._Carti:
                f.write(f"{carte.get_id_carte()},{carte.get_titlu()},{carte.get_descriere()},{carte.get_autor()}\n")
                
    
    def __append_to_file(self,carte):
        with open(self.__filepath, "a") as f:
            f.write(f"{carte.get_id_carte()},{carte.get_titlu()},{carte.get_descriere()},{carte.get_autor()}\n")
    
    def adauga_carte(self, carte):
        self.__read_all_from_file_new()
        RepoCarti.adauga_carte(self, carte)
        self.__append_to_file_new(carte)
    
    def sterge_carte(self, id_del):
        self.__read_all_from_file_new()
        RepoCarti.sterge_carte(self, id_del)
        self.__write_all_to_file_new()
    
    def cauta_carte_dupa_id(self, id_carte):
        self.__read_all_from_file_new()
        return RepoCarti.cauta_carte_dupa_id(self, id_carte)
    
    def modify_carti_all(self, new_carte):
        self.__read_all_from_file_new()
        RepoCarti.modify_carti_all(self, new_carte)
        self.__write_all_to_file_new()
    
    def get_all_carti(self):
        self.__read_all_from_file_new()
        return RepoCarti.get_all_carti(self)
    
    def __len__(self):
        self.__read_all_from_file_new()
        return RepoCarti.__len__(self)
        
        
    
class RepoClienti(object):

    
    def __init__(self):
        self._Clienti = []
    
    def __len__(self):
        return len(self._Clienti)
   
    def adauga_client(self, client):
        for i in self._Clienti:
            if i == client:
                raise RepoError("Id si/sau CNP existent!\n")
        self._Clienti.append(client)
    
    def cauta_client_dupa_id(self, id_cautat):
        ok = True
        for client in self._Clienti:
            if client.get_id_client() == id_cautat:
                return client
        if ok:
            raise RepoError("Id client inexistent!")
            
    def sterge_client(self,id_del):
        ok = True
        for client in self._Clienti:
            if client.get_id_client() == id_del:
                self._Clienti.remove(client)
                ok = False
        if ok:
            raise RepoError("Id client inexistent!")

    
    def modify_client_all(self, client_new):
        ok = True
        for client in self._Clienti:
            if client.get_id_client() == client_new.get_id_client():
                client.set_nume_client(client_new.get_nume_client())
                client.set_cnp_client(client_new.get_cnp_client())
                ok = False
        if ok:
            raise RepoError("Id inexistent!")
    
    def get_all_clients(self):
        return self._Clienti  

class FileRepoClienti(RepoClienti):
    def __init__(self,filepath):
        RepoClienti.__init__(self)
        self.__filepath = filepath
    
    def __read_all_from_file_new(self):
        self._Clienti = []
        with open(self.__filepath, "r") as f:
            lines = f.readlines()
            nr =0
            for x in range(0,int(len(lines)/3)):
                id_client = int(lines[nr].strip())
                nume = lines[nr + 1].strip()
                cnp = int(lines[nr + 2].strip())
                client = Client(id_client,nume,cnp)
                self._Clienti.append(client)
                nr += 3
    
    def __write_all_to_file_new(self):
        with open(self.__filepath, "w") as f:
            for client in self._Clienti:
                f.write(f"{client.get_id_client()}\n{client.get_nume_client()}\n{client.get_cnp_client()}\n")
    
    def __append_to_file_new(self, client):
        with open(self.__filepath, "a") as f:
            f.write(f"{client.get_id_client()}\n{client.get_nume_client()}\n{client.get_cnp_client()}\n")
    
    def __read_all_from_file(self):
        self._Clienti = []
        with open(self.__filepath, "r") as f:
            lines = f.readlines()
            for line in lines:
                line = line.strip()
                if len(line) >0:
                    parts = line.split(",")
                    id_client = int(parts[0])
                    nume = parts[1]
                    cnp = int(parts[2])
                    client = Client(id_client,nume,cnp)
                    self._Clienti.append(client)
                
    def __write_all_to_file(self):
        with open(self.__filepath, "w") as f:
            for client in self._Clienti:
                f.write(f"{client.get_id_client()},{client.get_nume_client()},{client.get_cnp_client()}\n")
                
        
        
    def __append_to_file(self, client):
        with open(self.__filepath, "a") as f:
            f.write(f"{client.get_id_client()},{client.get_nume_client()},{client.get_cnp_client()}\n")
            
    
    
    def adauga_client(self, client):
        self.__read_all_from_file_new()
        RepoClienti.adauga_client(self, client)
        self.__append_to_file_new(client)
    
    def sterge_client(self, id_del):
        self.__read_all_from_file_new()
        RepoClienti.sterge_client(self, id_del)
        self.__write_all_to_file_new()
    
    def cauta_client_dupa_id(self, id_cautat):
        self.__read_all_from_file_new()
        return RepoClienti.cauta_client_dupa_id(self, id_cautat)
    
    def modify_client_all(self, client_new):
        self.__read_all_from_file_new()
        RepoClienti.modify_client_all(self, client_new)
        self.__write_all_to_file_new()
    
    def get_all_clients(self):
        self.__read_all_from_file_new()
        return RepoClienti.get_all_clients(self)
    
    def __len__(self):
        self.__read_all_from_file_new()
        return RepoClienti.__len__(self)
        
class RepoRental(object):
    
    def __init__(self):
        self._Rentals = []
    
    def __len__(self):
        return len(self._Rentals)
    
    def adauga_rental(self,rentalDTO):
        for i in self._Rentals:
            if i == rentalDTO:
                raise RepoError("Cartea nu a fost inca returnata!")
            elif rentalDTO.get_id_rental() == i.get_id_rental():
                raise RepoError("Id existent!")
            
        self._Rentals.append(rentalDTO)
    
    def cauta_rental_dupa_id(self,id_rental):
        ok = True
        for rental in self._Rentals:
            if rental.get_id_rental() == id_rental:
                return rental
                ok = False
        if ok:
            raise RepoError("Id inchiriere inexistent!")
        

    def get_all_rentals(self):
        return self._Rentals

    
    def sterge_rental_dupa_id(self, id_rental):
        ok = True
        for rental in self._Rentals:
            if rental.get_id_rental() == id_rental:
                self._Rentals.remove(rental)
                ok = False
        if ok:
            raise RepoError("Id inchiriere inexistent!")
    
    def modify_rental_all(self,id_rental,id_carte,id_client,data_rental,data_returned):
        ok = True
        for rental in self._Rentals:
            if rental.get_id_rental() == id_rental:
                rental.set_id_carte(id_carte)
                rental.set_id_client(id_client)
                rental.set_data_rental(data_rental)
                rental.set_data_return(data_returned)
                ok = False
        if ok:
            raise RepoError("Id inchiriere inexistent!")
    
class FileRepoRental(RepoRental):
    def __init__(self,filepath):
        RepoRental.__init__(self)
        self.__filepath = filepath
    

    def __read_all_from_file(self):
        self._Rentals = []
        with open(self.__filepath, "r") as f:
            lines = f.readlines()
            for line in lines:
                line = line.strip()
                if len(line)>0:
                    parts = line.split(",")
                    id_rental = int(parts[0])
                    id_carte = int(parts[1])
                    id_client = int(parts[2])
                    data_rental = parts[3]
                    data_returned = parts[4]
                    rentalDTO = RentalDTO(id_rental,id_carte,id_client,data_rental)
                    self._Rentals.append(rentalDTO)
    
    def __read_all_from_file_new(self):
        self._Rentals = []
        with open(self.__filepath, "r") as f:
            lines = f.readlines()
            nr =0
            for x in range(0,int(len(lines)/5)):
                id_rental = int(lines[nr].strip())
                id_carte = int(lines[nr + 1].strip())
                id_client = int(lines[nr + 2].strip())
                data_rental = lines[nr + 3].strip()
                data_returned = lines[nr + 4].strip()
                rentalDTO = RentalDTO(id_rental,id_carte,id_client,data_rental)
                self._Rentals.append(rentalDTO)
                nr += 5
                
    def write_all_to_file_new(self):
        with open(self.__filepath, "w") as f:
            for rental in self._Rentals:
                f.write(f"{rental.get_id_rental()}\n{rental.get_id_carte()}\n{rental.get_id_client()}\n{rental.get_data_rental()}\n{rental.get_data_return()}\n")
    
    def __append_to_file_new(self, rental):
        with open(self.__filepath, "a") as f:
            f.write(f"{rental.get_id_rental()}\n{rental.get_id_carte()}\n{rental.get_id_client()}\n{rental.get_data_rental()}\n{rental.get_data_return()}\n")                
    
    
    def __append_to_file(self, rental):
        with open(self.__filepath, "a") as f:
            f.write(f"{rental.get_id_rental()},{rental.get_id_carte()},{rental.get_id_client()},{rental.get_data_rental()},{rental.get_data_return()}\n")
    
    def __write_all_to_file(self):
        with open(self.__filepath, "w") as f:
            for rental in self._Rentals:
                f.write(f"{rental.get_id_rental()},{rental.get_id_carte()},{rental.get_id_client()},{rental.get_data_rental()},{rental.get_data_return()}\n")
            
            
    def adauga_rental(self, rental):
        self.__read_all_from_file_new()
        RepoRental.adauga_rental(self, rental) 
        self.__append_to_file_new(rental)     
    
    def sterge_rental_dupa_id(self, id_rental):
        self.__read_all_from_file_new()
        RepoRental.sterge_rental_dupa_id(self, id_rental)
        self.__write_all_to_file_new()
    
    def cauta_rental_dupa_id(self, id_rental):
        self.__read_all_from_file_new()
        return RepoRental.cauta_rental_dupa_id(self, id_rental)
    
    def modify_rental_all(self, id_rental, carte, client, data_rental, data_returned):
        self.__read_all_from_file_new()
        RepoRental.modify_rental_all(self, id_rental, carte, client, data_rental, data_returned)
        self.__write_all_to_file_new()
    
    def get_all_rentals(self):
        self.__read_all_from_file_new()
        if len(self._Rentals) == 0:
            raise RepoError("Nu exista inchirieri!") 
        
        return RepoRental.get_all_rentals(self)
    
    def __len__(self):
        self.__read_all_from_file_new()
        return RepoRental.__len__(self)