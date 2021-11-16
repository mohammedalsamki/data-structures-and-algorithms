from stack_and_queue.stack_queue_animal_shelter import AnimalShelter
import pytest

def test_enqueue_cat():
    expected = "cat"
    animal_shelter=AnimalShelter()
    animal_shelter.enqueue_animal("cat")
    actual = animal_shelter.cat.rear.data

    assert expected == actual

def test_enqueues_dog():
    expected = "dog"
    animal_shelter=AnimalShelter()
    animal_shelter.enqueue_animal("dog")
    actual = animal_shelter.dog.rear.data

    assert expected == actual

def test_enqueues_other():
    with pytest.raises(Exception):
        animal_shelter=AnimalShelter()
        animal_shelter.enqueue_animal("duck")


def test_dequeues_dog():
    expected = "dog2"
    animal_shelter=AnimalShelter()
    animal_shelter.enqueue_animal("dog1")
    animal_shelter.enqueue_animal("dog2")
    animal_shelter.dequeue_animal("dog1")
    actual = animal_shelter.dog.front.data

    assert expected == actual

def test_dequeues_cat():
    expected = "cat2"
    animal_shelter=AnimalShelter()
    animal_shelter.enqueue_animal("cat1")
    animal_shelter.enqueue_animal("cat2")
    animal_shelter.dequeue_animal("cat1")
    actual = animal_shelter.cat.front.data

    assert expected == actual

def test_dequeues_other():
    expected = "NULL"
    animal_shelter=AnimalShelter()
    actual= animal_shelter.dequeue_animal("duck")

    assert expected == actual
