from imports import load_dataset

def data ():
  """"
  Essa função realiza o carregamento do dataset que será utilizado. Nesse exemplo, o repositório monash_tsf com dataset tourism_monthly disponível no Hugging Face."""
  dataset = load_dataset("monash_tsf", "tourism_monthly")