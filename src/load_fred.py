import pandas as pd
import pandas_datareader
import config
from pathlib import Path

DATA_DIR = Path(config.DATA_DIR)


description_crsp = {
    "cash": "Cash -CASH AND DUE FROM DEPOSITORIES (rcfd0010) ",
    
    "total_afs": "AVAILABLE-FOR-SALE SECURITIES (rcfd1773) Total available-for-sale securities, reported at fair value.",
    
    "RMBS_Residential_GNMA_HTM": "MBS Reports Guaranteed by GNMA,Held-to-Maturity, reported at Fair Value.",
    "RMBS_Residential_GNMA_AFS": "MBS Reports Issued by GNMA,  Available-for-Sale, reported at Fair Value",
    "RMBS_Residential_FNMA_HTM": "MBS Reports Guaranteed by FNMA/FHLMC, Held-to-Maturity, reported at Fair Value.",
    "RMBS_Residential_FNMA_AFS": "MBS Reports Issued by FNMA/FHLMC, Available-for-Sale, reported at Fair Value",
    "RMBS_Residential_Other_HTM": "MBS Reports Other Participating Securities, Held-to-Maturity, reported at Fair Value.",
    "RMBS_Residential_Other_AFS": "MBS Reports Other Participating Securities, Available-for-Sale, reported at Fair Value.",
    "RMBS_Residential_FFG_HTM": "MBS for other residential securities issued or guaranteed by Freddie Mac (FFG), held-to-maturity, valued at fair value",
    "RMBS_Residential_FFG_AFS": "MBS for other residential securities issued or guaranteed by Freddie Mac, available-for-sale, valued at fair value.",
    "RMBS_Residential_NOT_FFG_HTM": "MBS for other residential securities not issued or guaranteed by Freddie Mac (FFG), held-to-maturity, valued at fair value",
    "RMBS_Residential_NOT_FFG_AFS": "MBS for other residential securities not issued or guaranteed by Freddie Mac, available-for-sale, valued at fair value.",
    
    "CMBS_Commerical_FNMA_HTM": "MBS for commercial project securities guaranteed by FNMA (Fannie Mae), classified as available-for-sale valued at fair value.",
    "CMBS_Commerical_FNMA_AFS": "MBS for commercial project securities guaranteed by FNMA (Fannie Mae), classified as available-for-sale valued at fair value.",
    "CMBS_Commerical_NOT_FNMA_HTM": "MBS for commercial project securities guaranteed by FNMA (Fannie Mae), classified as available-for-sale valued at fair value.",
    "CMBS_Commerical_NOT_FNMA_AFS": "MBS for commercial project securities NOT guaranteed by FNMA (Fannie Mae), classified as available-for-sale valued at fair value.",
    "CMBS_Other_Commerical_FNMA_HTM": "MBS for other commercial project securities guaranteed by FNMA (Fannie Mae), classified as available-for-sale valued at fair value.",
    "CMBS_Other_Commerical_FNMA_AFS": "MBS for other commercial project securities guaranteed by FNMA (Fannie Mae), classified as available-for-sale valued at fair value.",
    "CMBS_Other_Commerical_NOT_FNMA_HTM": "MBS for other commercial project securities guaranteed by FNMA (Fannie Mae), classified as available-for-sale valued at fair value.",
    "CMBS_Other_Commerical_NOT_FNMA_AFS": "MBS for other commercial project securities NOT guaranteed by FNMA (Fannie Mae), classified as available-for-sale valued at fair value.",
   
    "ABS_HTM": "HTM Asset-backed securities (ABS), reported at Fair Value.",
    "ABS_AFS": "AFS Asset-backed securities (ABS), reported at Fair Value.",
    
    "RELOAN_Construction_FAM": "Loans secured by 1-4 family residential properties under construction.",
    "RELOAN_Construction_other": "Loans secured by other construction projects (not 1-4 family residences) and land.",
    "RELOAN_Other_First_FAM":"All other loans secured by 1-4 family residential properties with a first lien position.",
    "RELOAN_Other_Junior_FAM":"All other loans secured by 1-4 family residential properties with junior lien positions, such as second mortgages.",
    "RELOAN_Owner_OCCPD":"Loans secured by owner-occupied nonfarm, nonresidential properties.",
    "RELOAN_Other_NONFARM_NONRES":"Loans secured by other nonfarm, nonresidential properties, indicating loans for commercial properties not occupied by the owner.",
    
    "AGRI_LOAN":" Loans provided to finance agricultural production.",
    "COMM_INDU_LOAN":"Commercial and industrial loans to borrowers in the U.S.",
}


def load_fred(
    data_dir=DATA_DIR,
    from_cache=True,
    save_cache=False,
    start="1913-01-01",
    end="2023-10-01",
):
    """
    Must first run pull_and_save_fred_data. If loading from cache, then start
    and dates are ignored
    """
    if from_cache:
        file_path = Path(data_dir) / "pulled" / "fred.parquet"
        # df = pd.read_csv(file_path, parse_dates=["DATE"])
        df = pd.read_parquet(file_path)
        # df = df.set_index("DATE")
    else:
        # Load CPI, nominal GDP, and real GDP data from FRED, seasonally adjusted
        df = pandas_datareader.get_data_fred(
            ["CPIAUCNS", "GDP", "GDPC1"], start=start, end=end
        )
        if save_cache:
            file_dir = Path(data_dir) / "pulled"
            file_dir.mkdir(parents=True, exist_ok=True)
            # df.to_csv(file_dir / "fred_cpi.csv")
            df.to_parquet(file_dir / 'fred.parquet')

    # df.info()
    # df = pd.read_parquet(file_path)
    return df


def demo():
    df = load_fred()


if __name__ == "__main__":
    # Pull and save cache of fred data
    _ = load_fred(start="1913-01-01", end="2023-10-01", 
        data_dir=DATA_DIR, from_cache=False, save_cache=True)
