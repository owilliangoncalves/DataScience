def imports():
    """
    Essa função realiza os imports das bibliotecas necessárias para o desenvolvimento do projeto.
    """
    # Importa os módulos necessários
    import evaluate
    import torch
    import transformers
    import accelerate
    import gluonts
    import numpy as np
    from datasets import load_dataset
    import matplotlib.pyplot as plt
    import matplotlib.dates as mdates
    from functools import lru_cache
    from transformers import TimeSeriesTransformerForPrediction
    from transformers import PretrainedConfig
    from typing import Optional
    from accelerate import Accelerator
    from torch.optim import AdamW
    from evaluate import load
    from typing import Iterable
    from functools import lru_cache
    from gluonts.itertools import Cached, Cyclic
    from gluonts.dataset.loader import as_stacked_batches
    from gluonts.time_feature import get_seasonality
    
    
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
    import warnings
    warnings.filterwarnings('ignore')