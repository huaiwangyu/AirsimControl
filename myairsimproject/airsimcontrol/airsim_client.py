import airsim
class AirSimDroneClient:
    def __init__(self):
        self.client = airsim.MultirotorClient()
        self.client.confirmConnection()

    def takeoff(self):
        self.client.enableApiControl(True)
        self.client.armDisarm(True)
        self.client.takeoffAsync().join()

    def land(self):
        self.client.landAsync().join()

    def move_to_location(self, x, y, z):
        self.client.moveToPositionAsync(x, y, z, 5).join()

    def get_state(self):
        return self.client.simGetVehiclePose()
