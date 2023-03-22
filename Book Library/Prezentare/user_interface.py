from errors.exceptii import RepoError, ValidationError, SrvError
class Consola(object):

    
    def __init__(self, srv_carti, srv_clienti,srv_rental):
        self.__srv_carti = srv_carti
        self.__srv_clienti = srv_clienti
        self.__srv_rental = srv_rental
    def __ui_meniu(self):
        print("""
        Lista de comenzi:
                -help
                -add_carte
                -add_client
                -sterge_carte
                -sterge_client
                -cauta_carte
                -cauta_client
                -show_carti
                -show_clienti
                -modify_carte
                -modify_client
                -add_rental(Inchiriere carte)
                -sterge_rental
                -return_carte(Returneaza carte)
                -show_rentals
                -modify_rental
                -add_random_client
                -raport1(Cele mai inchiriate carti)
                -raport2(Clienti cu carti inchiriate ordanate dupa nume sau dupa numarul cartilor inchiriate)
                -raport3(Primi 20% cei mai activi clienti)
                -raport4
        """)
    def __ui_add_carte(self):
        try:
            id_carte = int(input("Id carte: "))
        except ValueError:
            print("Id numeric invalid!")
            return
        titlu = input("Titlu Carte: ")
        descriere = input("Descriere: ")
        autor = input("Autor: ")
        try:
            self.__srv_carti.add_carte(id_carte, titlu, descriere, autor)
        except RepoError as re:
            print(str(re))
            return
        except ValidationError as ve:
            print(str(ve))
            return
        print("Carte adaugata cu succes")
    
   
    def __ui_cauta_carte(self):
        self.__ui_cauta_carte_dupa_id()
        
            
    def __ui_cauta_carte_dupa_id(self):
        try:
            id = int(input("Introdu id: "))
        except ValueError:
            print("Id invalid!")
            return
        try:
            carte = self.__srv_carti.cauta_carte_dupa_id(id)
        except RepoError as re:
            print(str(re))
            return
        except ValidationError as ve:
            print(str(ve))
            return
        print(carte)
    
    
    def __ui_add_client(self):
        try:
            id_client = int(input("Introdu id: "))
        except ValueError:
            print("Id invalid!")
            return 
        nume_client = input("Introdu nume: ")
        try:
            cnp_client = int(input("Introdu CNP: "))
        except ValueError:
            print("CNP invalid!")
            return 
        try:
            self.__srv_clienti.add_client(id_client, nume_client, cnp_client)
        except RepoError as re:
            print(str(re))
            return 
        except ValidationError as ve:
            print(str(ve))
            return
        print("Client adaugat cu succes!")  
            
    
    
    def __ui_cauta_client(self):
        try:
            id_cautat = int(input("Introdu id: "))
        except ValueError:
            print("Id invalid!")
            return 
        try:
            client = self.__srv_clienti.cauta_client_dupa_id(id_cautat)
        except RepoError as re:
            print(str(re))
            return 
        except ValidationError as ve:
            print(str(ve))
            return 
        print(str(client))
    
    
    def __ui_sterge_carte(self):
        try:
            id_del = int(input("Introdu Id: "))
        except ValueError:
            print("Id invalid!")
            return 
        try:
            self.__srv_rental.sterge_carte(id_del)
        except ValidationError as ve:
            print(str(ve))
            return 
        except RepoError as re:
            print(str(re))
            return 
        print("Carte stearsa cu succes")
    

    def __ui_sterge_client(self):
        try:
            id_del = int(input("Introdu id: "))
        except ValueError:
            print("Id invalid!")
        try:
            self.__srv_rental.sterge_client(id_del)
        except ValidationError as ve:
            print(str(ve))
            return 
        except RepoError as re:
            print(str(re))
            return 
        print("Client sters cu succes")
        
    def show_rec(self,lista):
            if len(lista) == 0:
                return ""
            else:
                return str(lista.pop(0)) +"\n"+ self.show_rec(lista)
    
    def __ui_show_carti(self):
        try:
            lista_carti = self.__srv_carti.show_carti_rec()
        except RepoError as re:
            print(str(re))
            return 
        print(self.show_rec(lista_carti))
        
    
    
    
    def __ui_show_clienti(self):
        try:
            lista_clienti = self.__srv_clienti.show_clienti_rec()
        except RepoError as re:
            print(str(re))
            return 
        print(self.show_rec(lista_clienti))
    
    
    def __ui_modify_carte_all(self):
        try:
            id_modify = int(input("Introdu id: "))
        except ValueError:
            print("Id invalid!")
            return 
        
        titlu_modify = input("Introdu titlu: ")
        descriere_modify = input("Introdu descriere: ")
        autor_modify = input("Introdu autor: ")
        try:
            self.__srv_carti.modify_carte_all(id_modify, titlu_modify, descriere_modify, autor_modify)
        except RepoError as re:
            print(str(re))
            return 
        except ValidationError as ve:
            print(str(ve))
            return 
        print("Carte modificata cu succes!")
        
    
    def __ui_modify_carte(self):
        self.__ui_modify_carte_all()
    
    
    def __ui_modify_client_all(self):
        try:
            id_modify = int(input("Introdu id: "))
        except ValueError:
            print("Id invalid!")
            return 
        nume_modify = input("Introdu nume: ")
        try:
            cnp_modify = int(input("Introdu CNP: "))
        except ValueError:
            print("CNP invalid!")
            return 
        try:
            self.__srv_clienti.modify_client_all(id_modify, nume_modify, cnp_modify)
        except RepoError as re:
            print(str(re))
            return 
        except ValidationError as ve:
            print(str(ve))
            return 
        print("Client modificat cu succes!")
    
    def __ui_modify_client(self):
        self.__ui_modify_client_all()
        
    
    def __ui_add_rental(self):
        try:
            id_carte = int(input("Introdu id carte: "))
        except ValueError:
            print("Id carte invalid!")
            return
        
        try:
            id_client = int(input("Introdu id client: "))
        except ValueError:
            print("Id client invalid!")
        
        try:
            id_rental = int(input("Introdu id rental: "))
        except ValueError:
            print("Id rental invalid!")
            return
        
        try:
            data_rental = input("Introdu data: ")
        except ValueError:
            print("Data invalida!")  
        try:
            rental = self.__srv_rental.add_rental(id_rental,id_carte,id_client,data_rental)
        except RepoError as re:
            print(str(re))
            return
        except ValidationError as ve:
            print(str(ve))
            return
        print("Inchiriere adaugata cu succes\n" + str(rental))
        

    def __ui_return_carte_dupa_id_rental(self):
        try:
            id_returned = int(input("Introdu id inchiriere: "))
        except ValueError:
            print("Id invalid!")
            return
        data_returned = input("Introdu data returnarii: ")
        try:
            self.__srv_rental.return_carte_dupa_id_rental(id_returned, data_returned)
        except RepoError as re:
            print(str(re))
            return 
        except ValidationError as ve:
            print(str(ve))
            return
        print("Carte returnata cu succes!")
    
    def __ui_return_carte(self):
        self.__ui_return_carte_dupa_id_rental()
    
    
    def __ui_show_rentals(self):
        try:
            rentals = self.__srv_rental.show_all_rentals()
        except RepoError as re:
            print(str(re))
            return
        for rental in rentals:
            print(rental)
    
    
    def __ui_add_random_client(self):
        try:
            l = int(input("Introdu numarul de clienti: "))
        except ValueError:
            print("Numar invalid!")
            return
        self.__srv_clienti.add_random_client_r(l)
    
    
    def __ui_sterge_rental(self):
        try:
            id_rental = int(input("Introdu id inchiriere:"))
        except ValueError:
            print("Id inchiriere invalid!")
            return
        try:
            self.__srv_rental.sterge_rental_dupa_id(id_rental)
        except ValidationError as ve:
            print(str(ve))
            return 
        except RepoError as re:
            print(str(re))
            return
        print("Inchiriere stearsa cu succes!")
    

    def __ui_raport_carti_inchiriate(self):
        try:
            carti = self.__srv_rental.raport_cele_mai_inchiriate_carti()
        except SrvError as se:
            print(str(se))
            return
        
        for carte in carti:
            print(str(carte))
        
    
    def __ui_raport2(self):
        tip_sortare = input("Introdu tipul de sortare(dupa nume/carti_inchiriate): ")
        if tip_sortare == "nume":
            try:
                clienti = self.__srv_rental.raport2_nume()
            except SrvError as se:
                print(str(se))
                return 
        elif tip_sortare == "carti_inchiriate":
            try:
                clienti = self.__srv_rental.raport2_nr_carti()
            except SrvError as se:
                print(str(se))
                return  
        else:
            print("Tip de sortare invalida!")
            return
        
        for client in clienti:
            print(str(client))
        

    
    def __ui_raport3(self):
        try:
            clienti = self.__srv_rental.raport3()
        except SrvError as se:
            print(str(se))
            return 
        l = len(clienti)
        l = int(l*0.2)
        if l< 1:
            l = 1
        nr =0
        st = ""
        for client in clienti:
            print(str(client))
            nr += 1
            if nr ==l:
                break
    
    def __ui_raport4(self):
        try:
            carti = self.__srv_rental.raport4()
        except SrvError as se:
            print(str(se))
            return
        print(carti)
    
    
    def __ui_modify_rental(self):
        try:
            id_modify = int(input("Introdu id rental: "))
        except ValueError:
            print("id invalid!")
        try:
            id_carte = int(input("Introdu id carte: "))
        except ValueError:
            print("id invalid!")
        
        try:
            id_client = int(input("Introdu id client: "))
        except ValueError:
            print("id invalid!")   
        
        data_rental = input("Data rental: ")
        data_return = input("Data return: ")
        print("Inchiriere modificata cu succes!\n")  
        
        try:
            self.__srv_rental.modify_rental_all(id_modify,id_carte,id_client,data_rental,data_return)
        except ValidationError as ve:
            print(str(ve))
            return
    
    
    def run(self):
        self.__ui_meniu()
        while True:
            cmd = input(">>>")
            if cmd == "exit":
                print("exiting...")
                return 
            elif cmd == "":
                continue
            elif cmd == "help":
                self.__ui_meniu()
            elif cmd == "add_carte":
                self.__ui_add_carte()
            elif cmd == "cauta_carte":
                self.__ui_cauta_carte()
            elif cmd == "add_client":
                self.__ui_add_client()
            elif cmd == "cauta_client":
                self.__ui_cauta_client()
            elif cmd == "sterge_carte":
                self.__ui_sterge_carte()
            elif cmd =="sterge_client":
                self.__ui_sterge_client()
            elif cmd == "show_carti":
                self.__ui_show_carti()
            elif cmd == "show_clienti":
                self.__ui_show_clienti()
            elif cmd == "modify_carte":
                self.__ui_modify_carte()
            elif cmd =="modify_client":
                self.__ui_modify_client()
            elif cmd =="add_rental":
                self.__ui_add_rental()
            elif cmd =="sterge_rental":
                self.__ui_sterge_rental()
            elif cmd=="return_carte":
                self.__ui_return_carte()
            elif cmd == "show_rentals":
                self.__ui_show_rentals()
            elif cmd == "add_random_client":
                self.__ui_add_random_client()
            elif cmd == "modify_rental":
                self.__ui_modify_rental()
            elif cmd == "raport1":
                self.__ui_raport_carti_inchiriate()
            elif cmd == "raport2":
                self.__ui_raport2()
            elif cmd =="raport3":
                self.__ui_raport3()
            elif cmd =="raport4":
                self.__ui_raport4()
            else:
                print("Comanda Invalida!")
                
    
    



