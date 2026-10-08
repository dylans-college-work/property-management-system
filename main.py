from pathlib import Path
 
FILE_NAME = Path(__file__).with_name("properties.txt")
 
def load_properties():
    properties = []
    if not FILE_NAME.exists():
        return properties
    with FILE_NAME.open("r", encoding="utf-8") as file:
        for line in file:
            fields = line.strip().split("|")
            if len(fields) == 6:
                properties.append({
                    "id": fields[0], "address": fields[1],
                    "city": fields[2], "type": fields[3],
                    "rent": fields[4], "status": fields[5]
                })
    return properties
 
def save_properties(properties):
    # TODO: Open FILE_NAME in write mode.
    # TODO: Loop through all properties.
    # TODO: Join fields in the correct order with '|'.
    # TODO: Write each record followed by a newline.
    pass
 
def add_property(properties):
    print("\n--- ADD PROPERTY ---")
    property_id = input("Property ID: ")
    address = input("Address: ")
    city = input("City: ")
    property_type = input("Property type: ")
    rent = input("Monthly rent (£): ")
    status = input("Status: ")
    # TODO: Reject duplicate IDs.
    # TODO: Build a dictionary and append it to properties.
    # TODO: Call save_properties(properties).
    pass
 
def view_properties(properties):
    print("\n--- PROPERTY LIST ---")
    # TODO: Handle an empty list.
    # TODO: Display every property with a for loop.
    pass
 
def update_property(properties):
    property_id = input("Property ID to update: ")
    # TODO: Find the matching property by ID.
    # TODO: Ask for new rent and status.
    # TODO: Change the matching dictionary and save.
    # TODO: Handle an unknown ID.
    pass
 
def delete_property(properties):
    property_id = input("Property ID to delete: ")
    # TODO: Find the matching property.
    # TODO: Ask for Y/N confirmation.
    # TODO: Remove only the selected record, then save.
    # TODO: Handle unknown ID or cancellation.
    pass
 
def main():
    properties = load_properties()
    while True:
        print("\n=== PROPERTY MANAGEMENT ===")
        print("1. Add property")
        print("2. View properties")
        print("3. Update property")
        print("4. Delete property")
        print("5. Exit")
        choice = input("Choose an option: ")
        if choice == "1": add_property(properties)
        elif choice == "2": view_properties(properties)
        elif choice == "3": update_property(properties)
        elif choice == "4": delete_property(properties)
        elif choice == "5": break
        else: print("Invalid choice.")
 
if __name__ == "__main__":
    main()
