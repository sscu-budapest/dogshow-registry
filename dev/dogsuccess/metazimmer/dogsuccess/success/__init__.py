from datetime import datetime  # noqa: F401

import datazimmer as dz
import metazimmer.dogracebase.core
import metazimmer.dogshowbase.core


class Status(dz.BaseEntity):
    pass


class SizedDogFeatures(dz.TableFeaturesBase):
    size = metazimmer.dogracebase.core.DogSizeIndex


class SizedDogIndex(dz.IndexBase):
    dog_id = str


class StatusFeatures(dz.TableFeaturesBase):
    wins = metazimmer.dogracebase.core.IntLimitType


class StatusIndex(dz.IndexBase):
    status_name = str


sized_dog_table = dz.ScruTable(
    features=SizedDogFeatures, subject_of_records=metazimmer.dogshowbase.core.Dog, index=SizedDogIndex
)
status_table = dz.ScruTable(features=StatusFeatures, subject_of_records=Status, index=StatusIndex)
