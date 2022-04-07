from datetime import datetime  # noqa: F401

import datazimmer as dz
import metazimmer.dogracebase.core

from . import success


class SizeCountFeatures(dz.TableFeaturesBase):
    elem_count = int


class SizeCountIndex(dz.IndexBase):
    size = metazimmer.dogracebase.core.DogSizeIndex


class StatusCountFeatures(dz.TableFeaturesBase):
    elem_count = int


class StatusCountIndex(dz.IndexBase):
    status = success.StatusIndex


size_count_table = dz.ScruTable(
    features=SizeCountFeatures, subject_of_records=metazimmer.dogracebase.core.DogSize, index=SizeCountIndex
)
status_count_table = dz.ScruTable(
    features=StatusCountFeatures, subject_of_records=success.Status, index=StatusCountIndex
)
