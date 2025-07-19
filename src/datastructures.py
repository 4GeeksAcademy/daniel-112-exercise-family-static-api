"""
TO-DOs:

[x] Add all members of the family in the Constructor method in "self._members = []" (information provided in README)

[x] Finish the methods to desired functionality:
    [x] add_member:
        - Should add a member to the self._members list

    [x] delete_member:
        - Should delete a member from the self._members list

    [x] get_member:
        - Should return a member from the self._members list
"""

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name
        self._next_id = 1
        self._members = [
            {
                "id": self._generate_id(),
                "first_name": "John",
                "last_name": last_name,
                "age": 33,
                "lucky_numbers": [7, 13, 22]
            },
            {
                "id": self._generate_id(),
                "first_name": "Jane",
                "last_name": last_name,
                "age": 35,
                "lucky_numbers": [10, 14, 3]
            },
            {
                "id": self._generate_id(),
                "first_name": "Jimmy",
                "last_name": last_name,
                "age": 5,
                "lucky_numbers": [1]
            }
        ]

    # This method generates a unique incremental ID
    def _generate_id(self):
        generated_id = self._next_id
        self._next_id += 1
        return generated_id


    ##############################################################################
    ##################### Methods that interact with the API #####################
    ##############################################################################


    # Adds a member to the self._members list
    def add_member(self, member):
        ## Append the member to the list of _members
        if 'id' not in member:
            member['id'] = self._generate_id()
        member['last_name'] = self.last_name
        self._members.append(member)

        print(f"Current family members: {self._members}")

        return member

    

    # Deletes a member from the self._members list
    def delete_member(self, id):
        ## Loop the list and delete the member with the given id
        for index, member in enumerate(self._members): # Recorre la lista y elimina el miembro con el id proporcionado
            if member["id"] == id:
                self._members.pop(index) # ALSO these ones --> "del self._members[index]"  OR  "self._members.remove(member)"
                return True
        return False


    # Returns a member from the self._members list
    def get_member(self, id):
        ## Loop all the members and return the one with the given id
        for member in self._members:
            if member['id'] == id:
                return member
        return None


    ####################################################################

    # This method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members