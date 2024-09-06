# Bibliotecas de machine learning
import torch
import transformers
from transformers import TimeSeriesTransformerConfig as TSTConfig
from transformers import TimeSeriesTransformerForPrediction as TSTForPrediction
from gluonts import *

# Bibliotecas de visualização
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# Bibliotecas de manipulação de dados
import pandas as pd
import numpy as np
from datasets import load_dataset

# Outros imports
from functools import lru_cache
from functools import partial
from typing import Optional
from accelerate import Accelerator
from torch.optim import AdamW
from evaluate import load
from gluonts.itertools import Cached, Cyclic
from gluonts.dataset.loader import as_stacked_batches
from gluonts.time_feature import get_seasonality
from gluonts.time_feature import get_lags_for_frequency
from gluonts.time_feature import time_features_from_frequency_str
from gluonts.transform.sampler import InstanceSampler
from gluonts.time_feature import (time_features_from_frequency_str, TimeFeature, get_lags_for_frequency)
from gluonts.dataset.field_names import FieldName
from gluonts.transform import (
    AddAgeFeature,
    AddObservedValuesIndicator,
    AddTimeFeatures,
    AsNumpyArray,
    Chain,
    ExpectedNumInstanceSampler,
    InstanceSplitter,
    RemoveFields,
    SelectFields,
    SetField,
    TestSplitSampler,
    Transformation,
    ValidationSplitSampler,
    VstackFeatures,
    RenameFields,
)

# Desativa warnings
import warnings
warnings.filterwarnings('ignore')
