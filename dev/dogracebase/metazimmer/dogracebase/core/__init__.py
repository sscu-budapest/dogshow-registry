from datetime import datetime  # noqa: F401

import datazimmer as dz
import metazimmer.dogshowbase.core


class Competition(dz.BaseEntity):
    pass


class DogOfTheMonth(dz.BaseEntity):
    pass


class DogSize(dz.BaseEntity):
    pass


class DogCategory(dz.CompositeTypeBase):
    pure = bool
    neutered = bool


class IntLimitType(dz.CompositeTypeBase):
    min = int
    max = int


class CompetitionIndex(dz.IndexBase):
    competition_id = str


class DogOfTheMonthIndex(dz.IndexBase):
    dog_type = DogCategory
    year = int
    month = int


class DogSizeFeatures(dz.TableFeaturesBase):
    waist_limit = IntLimitType
    weight_limit = IntLimitType


class DogSizeIndex(dz.IndexBase):
    dogsize_name = str


class DogFeatures(dz.TableFeaturesBase):
    name = str
    color = dz.Nullable(str)
    size = DogSizeIndex


class DogIndex(dz.IndexBase):
    canine_id = str


class CompetitionFeatures(dz.TableFeaturesBase):
    held_date = datetime
    fastest_time = float
    champion = DogIndex


class DogOfTheMonthFeatures(dz.TableFeaturesBase):
    winner = DogIndex


competition_table = dz.ScruTable(features=CompetitionFeatures, subject_of_records=Competition, index=CompetitionIndex)
dog_of_the_month_table = dz.ScruTable(
    features=DogOfTheMonthFeatures, subject_of_records=DogOfTheMonth, index=DogOfTheMonthIndex, max_partition_size=3
)
dog_size_table = dz.ScruTable(features=DogSizeFeatures, subject_of_records=DogSize, index=DogSizeIndex)
dog_table = dz.ScruTable(features=DogFeatures, subject_of_records=metazimmer.dogshowbase.core.Dog, index=DogIndex)
