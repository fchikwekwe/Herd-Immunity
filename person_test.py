import pytest
import person
import virus

""" Tests for the Person class in Herd Immunity """


def test_person_init():
    exposed_person = person.Person(12, is_vaccinated=False, infection=None)

    assert exposed_person._id == 12
    assert exposed_person.is_vaccinated == False
    assert exposed_person.infection == None

def test_did_survive_infection_certain_death():
    # mortality rate is impossibly high, so exposed_person2 should always die
    new_virus = virus.Virus("new_virus", 1.01, 1.01)
    exposed_person2 = person.Person(34, is_vaccinated=False, infection=new_virus)

    assert new_virus.name == "new_virus"
    assert new_virus.mortality_rate == 1.01
    assert new_virus.repro_rate == 1.01

    assert exposed_person2._id == 34
    assert exposed_person2.is_vaccinated == False
    assert exposed_person2.infection == new_virus
# unsure how to implement this test; trying to make sure that did_survive_infection() returns a value
    assert exposed_person2.did_survive_infection() == False
    assert exposed_person2.is_alive == False
