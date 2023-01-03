class CarServiceStation:
    def __init__(self, carName, serviceCodes):
        self._carName = carName
        self._serviceCodes = serviceCodes

    def CarSelection(self):
        if self.carName == "Hatchback":
            costingService = {
                "BS01": 2000,
                "EF01": 5000,
                "CF01": 2000,
                "BF01": 1000,
                "GF01": 3000
            }
            return costingService

        elif self.carName == "Sedan":
            costingService = {
                "BS01": 4000,
                "EF01": 8000,
                "CF01": 4000,
                "BF01": 1500,
                "GF01": 6000
            }
            return costingService

        elif self.carName == "SUV":
            costingService = {
                "BS01": 5000,
                "EF01": 10000,
                "CF01": 6000,
                "BF01": 2500,
                "GF01": 8000
            }
            return costingService
        else:
            return False

    def CarServiceBilling(self):
        
        dict = self.CarSelection()
        cost = 0
        for x in self.serviceCodes:
            cost += dict[x]
        return cost


class PrintingBill(CarServiceStation):
    def __init__(self, carName, serviceCodes):
        self.carName = carName
        self.serviceCodes = serviceCodes
       
            

        CarServiceStation.__init__(self, carName, serviceCodes)

    def serviceNameAssignment(self, serviceCode):
        dict2 = {
            "BS01": "Basic Servicing",
            "EF01": "Engine Fixing",
            "CF01": "Clutch Fixing",
            "BF01": "Brake Fixing",
            "GF01": "Gear Fixing",
        }
        return dict2[serviceCode]

    def printing_Bill(self):
        if self.carName not in ["Hatchback", "Sedan","SUV"]:
            print("You entered incorrect car Name from the list")
            return
        if self.serviceCodes not in ["BS01","EF01","CF01","BF01","GF01"]:
            print("You entered incorrect service code Name from the list")
            return
        print("\n \n")
        print(f"Type of Car - {self.carName}")
        print(f"Service Codes - {self.serviceCodes}")
        for x in self.serviceCodes:
            m = self.CarSelection()
            print(f"Charges for {self.serviceNameAssignment(x)} - $ {m[x]}")
        cost = self.CarServiceBilling()
        if cost > 10000:
            print("Complimentary cleaning - $ 0")
            print(f"Total Bill - $ {cost}")
        else:
            print(f"Total Bill - $ {cost}")

if __name__ == '__main__':
    carName = input("Enter the car Name from the list: \n 1: Hatchback \n 2: Sedan \n 3: SUV \n :")
    serviceCodes = list(input('Enter the service codes : { "BS01": "Basic Servicing",\n"EF01": "Engine Fixing",\n"CF01": "Clutch Fixing",\n"BF01": "Brake Fixing",\n"GF01": "Gear Fixing" \n }\n: ').split(" "))
    b = PrintingBill(carName, serviceCodes)
    b.printing_Bill()
