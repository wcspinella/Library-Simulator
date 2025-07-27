# Author: William Spinella
# GitHub username: wcspinella
# Date: 5/17/2025
# Description: This is a full library system that includes the library itself, multiple library items for checking out, and the ability to create a system of library members. You can do all the library things including checking out items, returning items, and placing items on holds and paying fines.

class LibraryItem:
    """Represents a library item that a patron can check out from a library."""
    def __init__(self, library_item_id, title):
        self._library_item_id = library_item_id #A unique identifier for a LibraryItem - you can assume uniqueness, you don't have to enforce it.
        self._title = title #Cannot be assumed to be unique.
        self._location = None #A LibraryItem can be "ON_SHELF", "ON_HOLD_SHELF", or "CHECKED_OUT".
        self._checked_out_by = None #Refers to the Patron who has it checked out (if any).
        self._requested_by = None #Refers to the Patron who has requested it (if any); a LibraryItem can only be requested by one Patron at a time.
        self._date_checked_out = None #When a LibraryItem is checked out, this will be set to the current_date of the Library.

    def get_library_item_id(self):
        """Returns the item id of the library item."""
        return self._library_item_id

    def get_title(self):
        """Returns title of library item."""
        return self._title

    def get_location(self):
        """Returns the library item's location."""
        return self._location

    def get_checked_out_by(self):
        """Returns who the item is checked out by."""
        return self._checked_out_by

    def get_requested_by(self):
        """Returns who requested this library item."""
        return self._requested_by

    def get_date_checked_out(self):
        """Returns date checked out of the library item."""
        return self._date_checked_out

    def set_location(self, new_location):
        """Sets new location of the library item."""
        self._location = new_location
        return self._location

    def set_checked_out_by(self, patron_id):
        """Sets which patron checked out the book."""
        self._checked_out_by = patron_id
        return self._checked_out_by

    def set_date_checked_out(self, new_date):
        "Sets new date checked out for library item."
        self._date_checked_out = new_date
        return new_date

    def set_requested_by(self, new_patron):
        "Sets new person who requested library item."
        self._requested_by = new_patron
        return self._requested_by


class Book(LibraryItem):
    """Creates a book item for the library."""
    def __init__(self, library_item_id, title, author):
        super().__init__(library_item_id, title)
        self._author = author

    def get_author(self):
        """Returns book author."""
        return self._author

    def get_check_out_length(self):
        """Returns the number of days that type of library item may be checked out for."""
        length_of_days = 21
        return length_of_days

class Album(LibraryItem):
    """Creates an album item for the library."""
    def __init__(self, library_item_id, title, artist):
        super().__init__(library_item_id, title)
        self._artist = artist

    def get_artist(self):
        """Returns album artist."""
        return self._artist

    def get_check_out_length(self):
        """Returns the number of days that type of library item may be checked out for."""
        length_of_days = 14
        return length_of_days

class Movie(LibraryItem):
    """Creates a movie item for the library."""
    def __init__(self, library_item_id, title, director):
        super().__init__(library_item_id, title)
        self._director = director

    def get_director(self):
        """Returns movie director."""
        return self._director

    def get_check_out_length(self):
        """Returns the number of days that type of library item may be checked out for."""
        length_of_days = 7
        return length_of_days

class Patron:
    """Represents a patron of the library."""
    def __init__(self, patron_id, name):
        self._patron_id = patron_id #A unique identifier for a Patron - you can assume uniqueness, you don't have to enforce it.
        self._name = name #Cannot be assumed to be unique.
        self._checked_out_items = [] #A collection of LibraryItems that a Patron currently has checked out(you choose both the type of collection and whether to store LibraryItem IDs or LibraryItem objects).
        self._fine_amount = 0 #How much the Patron owes the Library in late fines (measured in dollars); this is allowed to go negative.

    def get_patron_id(self):
        """Returns patron id"""
        return self._patron_id

    def get_name(self):
        """Returns patron name."""
        return self._name

    def get_checked_out_items(self):
        """Returns list of checked out items."""
        return self._checked_out_items

    def get_fine_amount(self):
        """Returns late fine amount for patron measured in dollars. This is allowed to go negative."""
        return self._fine_amount

    def add_library_item(self, library_item):
        """Adds the specified library item to checked_out_items."""
        self._checked_out_items.append(library_item)
        return self._checked_out_items

    def remove_library_item(self, library_item):
        """Removes the specified library item from checked_out_items."""
        self._checked_out_items.remove(library_item)
        return self._checked_out_items

    def amend_fine(self, fine_change):
        """Changes the fine of the patron. A positive argument increases the fine_amount, a negative one decreases it; this is allowed to go negative."""
        self._fine_amount += fine_change
        return self._fine_amount

class Library:
    """Represents a library that contains various library items, and is used by various patrons."""
    def __init__(self):
        self._holdings = [] #A collection of the LibraryItems that belong to the Library (you choose both the type of collection and whether to store LibraryItem IDs or LibraryItem objects)
        self._members = [] #A collection of the Patrons who are members of the Library (you choose both the type of collection and whether to store Patron IDs or Patron objects)
        self._current_date = 0

    def get_holdings(self):
        """Returns collection of library items in the library."""
        return self._holdings

    def get_members(self):
        """Returns collection of patrons who are library members."""
        return self._members

    def get_current_date(self):
        """Returns current date."""
        return self._current_date

    def add_library_item(self, library_item):
        """Takes a library item object as a parameter and adds it to the holdings."""
        self._holdings.append(library_item)
        return self._holdings

    def add_patron(self, patron):
        """Takes a Patron object as a parameter and adds it to the members."""
        self._members.append(patron)
        return self._members

    def lookup_library_item_from_id(self, library_item_id):
        """Returns the library item object corresponding to the ID parameter, or None if no such library item is in the holdings."""
        for library_item in self._holdings:
            if library_item.get_library_item_id() == library_item_id:
                return library_item

    def lookup_patron_from_id(self, patron_id):
        """Returns the Patron object corresponding to the ID parameter, or None if no such Patron is a member."""
        for patron in self._members:
            if patron.get_patron_id() == patron_id:
                return patron

    def check_out_library_item(self, patron_id, library_item_id):
        """Goes through the process of checking out a library item."""
        #If the specified Patron is not in the Library's members, return "patron not found"
        patron_id_check = self.lookup_patron_from_id(patron_id)
        if patron_id_check == None:
            return "Patron not found."

        #If the specified LibraryItem is not in the Library's holdings, return "item not found"
        library_item_check = self.lookup_library_item_from_id(library_item_id)
        if library_item_check == None:
            return "Item not found."

        #If the specified LibraryItem is already checked out, return "item already checked out"
        item_location_check = library_item_check.get_location()
        if item_location_check == "CHECKED_OUT":
            return "Item already checked out."

        #If the specified LibraryItem is on hold by another Patron, return "item on hold by other patron"
        elif item_location_check == "ON_HOLD_SHELF":
            return "Item on hold by other patron."

        #Otherwise update the LibraryItem's checked_out_by, date_checked_out and location
        else:
            library_item_check.set_checked_out_by(patron_id)
            library_item_check.set_date_checked_out(self._current_date)
            library_item_check.set_location("CHECKED OUT")
            new_item_location = library_item_check.get_location ()

        #If the LibraryItem was on hold for this Patron, update requested_by
        hold_check = library_item_check.get_requested_by()
        if hold_check == patron_id:
            library_item_check.set_requested_by(None)

        #Update the Patron's checked_out_items
        patron_id_check.add_library_item(library_item_check)

        #Return "check out successful"
        return "Check out successful."

    def return_library_item(self, library_item_id):
        """Goes through the process of returning a library item."""
        #If the specified LibraryItem is not in the Library's holdings, return "item not found"
        library_item_check = self.lookup_library_item_from_id(library_item_id)
        if library_item_check == None:
            return "Item not found."

        #If the LibraryItem is not checked out, return "item already in library"
        item_location_check = library_item_check.get_location()
        if item_location_check != "CHECKED OUT":
            return "Item already in library."

        #Update the Patron's checked_out_items
        patron_id = library_item_check.get_checked_out_by()
        lookup_patron = self.lookup_patron_from_id(patron_id)
        lookup_patron.remove_library_item(library_item_check)

        #Update the LibraryItem's location depending on whether another Patron has requested it (if so, it should go on the hold shelf)
        hold_check = library_item_check.get_requested_by()
        if hold_check != None:
            library_item_check.set_location("ON_HOLD_SHELF")
        else:
            library_item_check.set_location("ON_SHELF")
            new_item_location = library_item_check.get_location()

        #Update the LibraryItem's checked_out_by
        library_item_check.set_checked_out_by(None)

        #return "return successful"
        return "Return Successful"

    def request_library_item(self, patron_id, library_item_id):
        """Requests library item for the patron."""
        #If the specified Patron is not in the Library's members, return "patron not found"
        patron_id_check = self.lookup_patron_from_id(patron_id)
        if patron_id_check == None:
            return "Patron not found."

        #If the specified LibraryItem is not in the Library's holdings, return "item not found"
        library_item_check = self.lookup_library_item_from_id(library_item_id)
        if library_item_check == None:
            return "Item not found."

        #If the specified LibraryItem is already requested, return "item already on hold"
        item_location_check = library_item_check.get_location()
        if item_location_check == "ON_HOLD_SHELF":
            return "Item already on hold."

        #Update the LibraryItem's requested_by
        library_item_check.set_requested_by(patron_id)
        new_holder = library_item_check.get_requested_by()

        #If the LibraryItem is on the shelf, update its location to on hold
        item_location_check_again = library_item_check.get_location()
        if item_location_check_again == "ON_SHELF":
            library_item_check.set_location("ON_HOLD_SHELF")
            new_location = library_item_check.get_location()

        #Return "request successful"
        return "Request Successful"

    def pay_fine(self, patron_id, dollar_amount):
        """Pays the patrons fine."""
        #If the specified Patron is not in the Library's members, return "patron not found"
        patron_id_check = self.lookup_patron_from_id(patron_id)
        if patron_id_check == None:
            return "Patron not found."

        #Use amend_fine to update the Patron's fine; return "payment successful"
        current_fine_amount = patron_id_check.get_fine_amount()
        new_fine_amount = patron_id_check.amend_fine(-dollar_amount)
        return "Payment Successful"

    def increment_current_date(self):
        """Increases current date in Library system."""
        #Increment current date
        self._current_date +=1

        #Increase each Patron's fines by 10 cents for each overdue LibraryItem they have checked out (by calling amend_fine).
        for patron in self._members:
            for library_item in patron.get_checked_out_items():
                if library_item:
                    return_date = library_item.get_check_out_length() + library_item.get_date_checked_out()
                    if self._current_date > return_date:
                        patron.amend_fine(.10)