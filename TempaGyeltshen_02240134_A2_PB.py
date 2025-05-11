# Pokemon Card Managing Program

MAX_ENTRIES = 1025
PAGE_SIZE = 64
ROWS = 8
COLS = 8

class CardEntry:
    
    #Each Pokemon card entry holds its assigned location in the album.
    def __init__(self, card_id):
        self.card_id = card_id
        self.page, self.row, self.col = self.determine_location()

    def determine_location(self):
        idx = self.card_id - 1         # Subtract 1 from the card_id to convert to 0 based index
        page = idx // PAGE_SIZE + 1    # This gives us 0-based pageindix, so add 1 to make it 1-based
        local_pos = idx % PAGE_SIZE    # Use modulo 64 to find the position within page
        row = local_pos // COLS + 1    # Divide by 8 to get row (then add 1 for 1-based indexing)
        col = local_pos % COLS + 1     # Modulo 8 to get column (then add 1 for 1-based indexing)
        return page, row, col


class AlbumTracker:
    
    #Manages card data, validation, and user actions like reset and display.
    
    def __init__(self):
        self.collection = {}

    def insert_card(self, card_id):
        if not (1 <= card_id <= MAX_ENTRIES):
            print("Invalid number. Please enter a number between 1 and 1025.")
            return

        if card_id in self.collection:
            card = self.collection[card_id]
            print(f"Card already present - Page {card.page}, Row {card.row}, Col {card.col}")
        else:
            new_card = CardEntry(card_id)
            self.collection[card_id] = new_card
            print(f"Output:\nStatue: Added Pokedex #{card_id} to the binder\nPage: {new_card.page},\nPosition: Row {new_card.row}, Column {new_card.col}")

    def clear_album(self):
        print("⚠️ WARNING: This will remove your entire collection.")      #Displaying a warning and requiring explicit confirmation (CONFIRM).
        confirm = input("Enter CONFIRM to proceed or EXIT to cancel: ")
        if confirm == "CONFIRM":                  # If confirmed, the entire crs dictionary is cleared with self.collection.clear()
            self.collection.clear()
            print("✅ Album successfully cleared.")
        else:                                     # If EXIT is typed, the user is returned to the main menu without clearing the data
            print("Cancelled. Returning to menu.")

    def show_contents(self):
        if not self.collection:
            print("Album is currently empty.")
        else:
            print("Your Collection:")
            for card_id in sorted(self.collection.keys()):
                c = self.collection[card_id]
                print(f"Pokedex: #{card_id}\n  Page: {c.page},\n  Position: Row {c.row}, Col {c.col}")
        total = len(self.collection)
        progress = (total / MAX_ENTRIES) * 100
        print(f"\nTotal Cards: {total} | Completion: {progress:.1f}%")
        if total == MAX_ENTRIES:
            print("🎉 Congratulations! You've completed the entire set!")

    def quit(self):
        print("Exiting program.\nThank you for using Pokemon Card Manager.\nSee you next time!")
        return


class CardBinder:
    
    #Interface handler for the user to interact with the album.
    
    def __init__(self):
        self.album = AlbumTracker()


    def input_card(self):
        try:
            card_id = int(input("Enter Pokedex number: "))
            self.album.insert_card(card_id)
        except ValueError:
            print("Please input a valid number.")


# Start the application
if __name__ == "__main__":
    program = CardBinder()
    program.launch()
