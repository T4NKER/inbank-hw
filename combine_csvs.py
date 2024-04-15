import pandas as pd
import sys
from datetime import datetime


def main():
    df1 = pd.read_csv(sys.argv[1], sep=";")
    df2 = pd.read_csv(sys.argv[2], sep=";")

    combined_df = pd.concat([df1, df2])

    combined_df.reset_index(drop=True, inplace=True)

    combined_df["metric_date"] = pd.to_datetime(combined_df["metric_date"])

    combined_df = combined_df.sort_values(by="metric_id")

    combined_df["combining_date"] = datetime.now().strftime("%Y-%m-%d")

    combined_df.to_csv("combined.csv", index=False)

if __name__ == "__main__":
    main()
