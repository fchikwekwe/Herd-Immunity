

class Virus(object):

    
    """Properties and attributes of the virus used in Simulation"""

    def __init__(self, name, mortality_rate, repro_rate):
        """Attributes instatiated with each virus."""
        self.name = name
        self.mortality_rate = mortality_rate
        self.repro_rate = repro_rate

# pytest style test function
    def test_virus_instatiation():
        """ Check to make sure that the virus instatiator is working"""
        virus = Virus("HIV", 0.8, 0.3)
        assert virus.name == "HIV"
        assert virus.mortality_rate == 0.8
        assert virus.repro_rate == 0.3
