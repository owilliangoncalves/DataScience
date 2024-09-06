import os
# Configurações de desempenho
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
os.environ['PYTORCH_ENABLE_MPS_FALLBACK'] = '1'
