class cars():
    #colors = ["Blue","Green","Black","White","Grey"]
    #drive = ["Left hand drive","Right hand drive"]
    #model = ["Hashback","Sedan"]

    def getModel(self):
        model = ["Hashback","Sedan"]
        print("Car model is " + model)
        


    def getConfig(self):
        colors = ["Blue","Green","Black","White","Grey"]
        drive = ["Left hand drive","Right hand drive"]
        print("This is the configuration detail:")
        print("=================================")
        print("Colors available:" + colors)
        print("Drive:" + drive)
        
def main():
    c = cars()
    c.getModel()
    c.getConfig()
    