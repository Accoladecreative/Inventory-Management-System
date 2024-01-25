from model.inventory import InventoryManagementSystem


def main():
    inventory_system = InventoryManagementSystem()
    
    inventory_system.add_book("The Great Gatsby", "F. Scott Fitzgerald", 50)
    inventory_system.add_book("To Kill a Mockingbird", "Harper Lee", 30)
    inventory_system.add_book("1984", "George Orwell", 40)

    inventory_system.display_inventory()

    inventory_system.update_quantity("The Great Gatsby", 45)
    inventory_system.display_inventory()

    inventory_system.process_order("To Kill a Mockingbird", 20)
    inventory_system.display_inventory()

    inventory_system.process_order("1984", 50)
    inventory_system.display_inventory()
    

if __name__ == "__main__":
    main()