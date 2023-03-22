from errors.exceptii import ValidationError
class ValidatorCarte(object):
    
    
    def valideaza(self, carte):
        errors = ""
        if carte.get_id_carte() <0:
            errors +="id invalid!\n"
        if carte.get_titlu() == "":
            errors += "titlu invalid!\n"
        if carte.get_descriere() == "":
            errors += "descriere invalida!\n"
        if carte.get_autor() == "":
            errors += "autor invalid!\n"
        if len(errors) > 0:
            raise ValidationError(errors)
    
    def valideaza_id(self,id_carte):
        if id_carte <= 0:
            raise ValidationError("Id invalid!")
    
    def valideaza_titlu(self,titlu_carte):
        if titlu_carte == "":
            raise ValidationError("Titlu invalid!")



class ValidatorClient(object):
    
    
    def valideaza_client(self, client):
        error = ""
        if client.get_id_client() <0:
            error += "Id invalid!\n"
        if client.get_nume_client() == "":
            error += "Nume invalid!\n"
        if len(str(client.get_cnp_client())) != 13:
            error += "CNP invalid!\n"
        if len(error) >  0:
            raise ValidationError(str(error))
            
    def valideaza_id(self,id_client):
        if id_client <0:
            raise ValidationError("Id invalid!")




class ValidatorRental(object):
    def valideaza_id(self,id_client):
        if id_client <0:
            raise ValidationError("Id inchiriere invalid!")
    
    def valideaza_data(self,data):
        data = str(data)
        if "/" not in data:
            raise ValidationError("Format data invalid!")
        
        parts = data.split("/")
        if len(parts) != 3:
            raise ValidationError("Format data invalid!")
        try:
            zi = int(parts[0])
        except ValueError:
            raise ValidationError("Format data invalid!")
        try:
            luna = int(parts[1])
        except ValueError:
            raise ValidationError("Format data invalid!")
        try:
            an = int(parts[2])
        except ValueError:
            raise ValidationError("Format data invalid!")
        
        err = ""
        
        if luna <1 or luna >12:
            err += "Luna invalida\n"
        
        if luna == 1 or luna == 3 or luna == 5 or luna == 7  or luna == 8 or luna == 10 or luna == 12:
            if zi <1 or zi >31:
                err+= "Zi invalida\n"
        elif luna == 2:
            if zi <1 or zi >28:
                err+= "Zi invalida\n"
        else:
            if zi <1 or zi >30:
                err+= "Zi invalida\n"
        if an <1500 or an >2022:
            err += "An invalid\n"
        if len(err) > 0:
            raise ValidationError(str(err))
        

