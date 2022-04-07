from datetime import datetime  # noqa: F401

import datazimmer as dz
import metazimmer.dogshowbase.core


class DogSuccessFeatures(dz.TableFeaturesBase):
    thing = int


dog_success_table = dz.ScruTable(features=DogSuccessFeatures, subject_of_records=metazimmer.dogshowbase.core.Dog)
