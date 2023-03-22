class Carte(object):
    
    
    def __init__(self, id_carte, titlu, descriere, autor):
        self.__id_carte = id_carte
        self.__titlu = titlu
        self.__descriere = descriere
        self.__autor = autor

    def get_id_carte(self):
        return self.__id_carte


    def get_titlu(self):
        return self.__titlu


    def get_descriere(self):
        return self.__descriere


    def get_autor(self):
        return self.__autor


    def set_titlu(self, value):
        self.__titlu = value


    def set_descriere(self, value):
        self.__descriere = value


    def set_autor(self, value):
        self.__autor = value

    def __eq__(self,other):
        return self.get_id_carte() == other.get_id_carte()
    
    def __str__(self):
        return "[" + str(self.get_id_carte()) + "]" + str(self.get_titlu()) + " by " + str(self.get_autor()) + " (" + str(self.get_descriere() +")")
    


class Client(object):
    
    
    def __init__(self, id_client, nume_client, cnp_client):
        self.__id_client = id_client
        self.__nume_client = nume_client
        self.__cnp_client = cnp_client

    def get_id_client(self):
        return self.__id_client


    def get_nume_client(self):
        return self.__nume_client


    def get_cnp_client(self):
        return self.__cnp_client


    def set_nume_client(self, value):
        self.__nume_client = value


    def set_cnp_client(self, value):
        self.__cnp_client = value
    
    def __str__(self):
        return "[" + str(self.get_id_client()) +"]"  + str(self.get_nume_client()) + " -> " + str(self.get_cnp_client()) 
     
    def __eq__(self,other):
        return self.get_cnp_client() == other.get_cnp_client() or self.get_id_client() == other.get_id_client()
            
    
    
    
    



class Rental(object):
    
    
    def __init__(self, id_rental, carte, client, data_rental):
        self.__id_rental = id_rental
        self.__carte = carte
        self.__client = client
        self.__data_rental = data_rental
        self.__data_return = None
    
    def __str__(self):
        if self.__data_return == None:
            return "rental" + "[" + str(self.__id_rental) + "] " + str(self.__client) + " rented " + str(self.__carte) + " on " + str(self.__data_rental) + " [Not returned yet]"
        else:
            return "[" + str(self.__id_rental) + "] " + str(self.__client) + " rented  " + str(self.__carte) + " on " + str(self.__data_rental) + " returned on " + str(self.__data_return)
    
    def __eq__(self,other):
        return (self.get_carte() == other.get_carte() and self.get_data_return() == None)
        
    def get_data_return(self):
        return self.__data_return


    def set_data_return(self, value):
        self.__data_return = value


    def get_id_rental(self):
        return self.__id_rental


    def get_carte(self):
        return self.__carte


    def get_client(self):
        return self.__client


    def get_data_rental(self):
        return self.__data_rental


    def set_carte(self, value):
        self.__carte = value


    def set_client(self, value):
        self.__client = value


    def set_data_rental(self, value):
        self.__data_rental = value
    

    
    



