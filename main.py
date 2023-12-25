from ClientInfo import ClientInfo
from Technician import Technician
from Inventory import Inventory

def main():
    """
        client1 = ClientInfo('Bowie', '0945895252525', 'UTOPIAN PARADISE', 'bowie@example.com')
        client1.add_contract_detail('Rodent', 'Pest Control', '11/12/23', '11/12/24', '25', '127', '150000')
        print(client1.client[0].__str__())
        client1.add_schedule('Posting', '2023-13-09', '2023-26-09', 9, 17)

        tech1 = Technician('Mora', 'Jeremy', '0945895252525', 'Pasig City')
        print(tech1.__str__())
        tech1.assign_item('Misting Can', 'Equipment', '1', '2023-07-03')
        print(tech1.item[0].__str__())
        tech1.assign_item('Pest Chemical', 'Chemical', '1000', '2023-07-03')
        print(tech1.item[1].__str__())
        tech1.assign_client(client1.client[0])
        print(tech1.handled_client())
    """
    inv = Inventory('Termite MODO', 'Chemical', 200, '2023-10-05', 'For Termite Use Only')
    print(inv.inventory[0].__str__())
    tech1 = Technician('Mora', 'Jeremy', '0945895252525', 'Pasig City')
    print(tech1.__str__())
    tech1.assign_item('Termite MODO', 'Chemical', 250, '2023-07-03', inv)
    print(inv.inventory[0].__str__())
    print(tech1.accounted_item())
    

if __name__ == "__main__": 
    main()