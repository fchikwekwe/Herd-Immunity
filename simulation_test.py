from simulation import Simulation
from person import Person
from virus import Virus
from logger import Logger

""" Tests for simulation class """

def test_init_parameters():
    person = Person(1, is_vaccinated=True, infection=None)
    simulation = Simulation(population_size=1, vacc_percentage=0.5, virus_name="bad virus", mortality_rate=0.5, basic_repro_num=0.5)
    population = [person]

    assert population_size == 1
    assert vacc_percentage == 0.5
    assert virus_name is "bad virus"
    assert mortality_rate == 0.5
    assert basic_repro_num == 0.5
    assert initial_infected == 1

    assert len(population) == population_size


def test_logger_created():
    simulation.Simulation.logger = Logger(test_logger.txt)
    assert simulation.Simulation.logger.name == test_logger.txt
