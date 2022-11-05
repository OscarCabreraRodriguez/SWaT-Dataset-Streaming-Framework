"""Utlis Module Contain all the needed functions to load and save files ..etc"""
import pandas as pd

def load_csv(path: str) -> pd.DataFrame:
    return pd.read_excel(path)