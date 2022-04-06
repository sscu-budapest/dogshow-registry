from datetime import datetime  # noqa: F401

import datazimmer as dz


class Competition(dz.BaseEntity):
    pass


class Photo(dz.BaseEntity):
    pass


class Relationship(dz.BaseEntity):
    pass


class Spot(dz.BaseEntity):
    pass


class Creature(dz.BaseEntity):
    pass


class Pet(dz.BaseEntity):
    pass


class BuildingInfoType(dz.CompositeTypeBase):
    floor = int
    door = int


class CompetitionIndex(dz.IndexBase):
    competition_id = str


class DogFeatures(dz.TableFeaturesBase):
    name = str
    date_of_birth = datetime
    waist = dz.Nullable(float)
    sex = str


class DogIndex(dz.IndexBase):
    dog_id = str


class PersonFeatures(dz.TableFeaturesBase):
    name = str
    date_of_birth = dz.Nullable(datetime)


class PersonIndex(dz.IndexBase):
    person_id = str


class PhotoIndex(dz.IndexBase):
    photo_id = str


class RelationshipFeatures(dz.TableFeaturesBase):
    since_birth = bool


class RelationshipIndex(dz.IndexBase):
    owner = PersonIndex
    dog = DogIndex


class Dog(Creature, Pet):
    pass


class Person(Creature):
    pass


class AddressType(dz.CompositeTypeBase):
    city = str
    street_address = str
    building = BuildingInfoType
    zip = str


class ResultType(dz.CompositeTypeBase):
    owner = PersonIndex
    pet = DogIndex
    prize = int


class CompetitionFeatures(dz.TableFeaturesBase):
    prize_pool = int
    winner = ResultType
    runner_up = ResultType
    special_mention = ResultType


class PhotoFeatures(dz.TableFeaturesBase):
    cuteness = float
    rel = RelationshipIndex


class SpotFeatures(dz.TableFeaturesBase):
    dog_1 = DogIndex
    dog_2 = DogIndex
    place = AddressType


competition_table = dz.ScruTable(features=CompetitionFeatures, subject_of_records=Competition, index=CompetitionIndex)
dog_table = dz.ScruTable(features=DogFeatures, subject_of_records=Dog, index=DogIndex, partitioning_cols=["sex"])
person_table = dz.ScruTable(features=PersonFeatures, subject_of_records=Person, index=PersonIndex)
photo_table = dz.ScruTable(features=PhotoFeatures, subject_of_records=Photo, index=PhotoIndex)
relationship_table = dz.ScruTable(
    features=RelationshipFeatures, subject_of_records=Relationship, index=RelationshipIndex
)
spot_table = dz.ScruTable(features=SpotFeatures, subject_of_records=Spot)
