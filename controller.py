from view_obj import View
from model import Ensemble
from model import Person

class Controller():
    def __init__(self):
        self.view = View(self)
        self.model = Ensemble()
    
    def start_view(self):
        self.view.create_fields()
        self.view.main()
    
    def search(self):
        
        """
        Method that calls 'search_person' and 'display_search' methods in order to
        display the results for searched persons by their last name.
        if not found, it calls 'search_not_found' and 'empty_field_error' methods of view
        to explain the problem to the user.
        """

        if self.view.get_value("Nom") :
            lname = f"{self.view.get_value('Nom')}"
            
            if self.model.search_person(lname) :
                person_info= self.model.search_person(lname)
                self.view.display_search(person_info)
            else :
                self.view.search_not_found()
                   
        else :
            self.view.empty_field_error()


        
    def delete(self):
        pass
    
    def insert(self):
        """
        Transition from Dict to database
        
        Method that verifies input calling 'insert_person' method and when it is
        verified (unique/instance of person) then we insert it into 
        real database 'annuaire.tsv' (updating database from the dictionnary)
        """
        person = Person(self.view.get_value("Nom"),
            self.view.get_value("Prenom"),
            self.view.get_value("Telephone"),
            self.view.get_value("Adresse"),
            self.view.get_value("Ville"))

        self.model.insert_person(person)
        print(self.model.list_person)
            

    def button_press_handle(self, buttonId):
        print("[Controller][button_press_handle] "+ buttonId)
        if buttonId == "Chercher":
            self.search()
        elif buttonId == "Effacer":
            self.delete()
        elif buttonId == "Inserer":
            self.insert()
        else:
            pass

if __name__ == "__main__":
    controller = Controller()
    controller.start_view()