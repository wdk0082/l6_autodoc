class people:
    """
    A class to define a person.

    Attributes:
        name (str): The name of the person.
        age (int): The age of the person.
    """

    def __init__(self, name, age):
        """
        Initialize the person.
        
        Parameters:
            name (str): The name of the person.
            age (int): The age of the person.
        """
        self.name = name
        self.age = age

    def change_name(self, new_name):
        """
        Change the person's name
        
        Parameters:
            new_name (str): The person's new name.
        """
        self.name = new_name

    def update_age(self):
        """
        Update the person's age by +1.
        """
        self.age += 1

    def get_info(self):
        """
        Get the student's info.
        
        Returns:
            tuple: A tuple containing:
                name (str): The person's name.
                age (int): The person's age.
        """
        return self.name, self.age
