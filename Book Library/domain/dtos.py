'''
Created on Dec 2, 2021

@author: Thomas
'''

class RentalDTO(object):
    def __init__(self,id_rental,id_carte,id_client,data_rental):
        self.__id_rental = id_rental
        self.__id_carte = id_carte
        self.__id_client = id_client
        self.__data_rental = data_rental
        self.__data_return = None

    def get_id_rental(self):
        return self.__id_rental


    def get_id_carte(self):
        return self.__id_carte


    def get_id_client(self):
        return self.__id_client


    def get_data_rental(self):
        return self.__data_rental


    def get_data_return(self):
        return self.__data_return


    def set_id_carte(self, value):
        self.__id_carte = value


    def set_id_client(self, value):
        self.__id_client = value


    def set_data_rental(self, value):
        self.__data_rental = value


    def set_data_return(self, value):
        self.__data_return = value
     
    def __eq__(self,other):
        return (self.__id_carte == other.__id_carte and self.get_data_return() == None)   
    
class showRentalsDTO(object):
    def __init__(self,client,carti):
        self.__client = client
        self.__carti = carti
    
    def __str__(self):
        
        st = str(self.__client) +"\n"
        for carte in self.__carti:
            st += "\t" + str(carte) + "\n"
        return st
    

class Raport1DTO(object):
    def __init__(self,titlu,rentals):  
        self.__titlu = titlu
        self.__rentals = rentals
        
    def __gt__(self, other):
        return self.__rentals > other.__rentals
        
    def __str__(self):
        return f"Cartea {self.__titlu} are {self.__rentals} inchirieri"
    
    def get_rentals(self):
        return self.__rentals
    
    def get_titlu(self):
        return self.__titlu
    
class Raport2DTO(object):
    
    
    def __init__(self, nume, carti):
        self.__nume = nume
        self.__carti = carti
    
    def __lt__(self,other):
        return self.__nume < other.__nume
    
    def __gt__(self, other):
        return self.__carti > other.__carti
    
    def __str__(self):
        return f"{self.__nume} a inchiriat {self.__carti} carti"
    
    def get_carti(self):
        return self.__carti
    def get_nume(self):
        return self.__nume



class Raport3DTO(object):
    
    
    def __init__(self, nume, carti):
        self.__nume = nume
        self.__carti = carti
    
    def __gt__(self, other):
        return self.__carti > other.__carti
    
    def __str__(self):
        return f"{self.__nume} a inchiriat {self.__carti} carti"

    def get_carti(self):
        return self.__carti

