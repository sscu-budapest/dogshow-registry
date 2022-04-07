from datetime import datetime  # noqa: F401

import datazimmer as dz


class SexMatch(dz.BaseEntity):
    pass


class SexMatchFeatures(dz.TableFeaturesBase):
    count = int


class SexMatchIndex(dz.IndexBase):
    sex_1 = str
    sex_2 = str


sex_match_table = dz.ScruTable(features=SexMatchFeatures, subject_of_records=SexMatch, index=SexMatchIndex)
