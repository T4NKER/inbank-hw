import pandas as pd
import sys
from datetime import datetime


def main():
    date1 = sys.argv[1].split("_")[1]
    date2 = sys.argv[2].split("_")[1]

    date1 = date1.split(".")[0]
    date2 = date2.split(".")[0]

    if date1 > date2:
        date1, date2 = date2, date1

    df1 = pd.read_csv(sys.argv[1], sep=";")
    df2 = pd.read_csv(sys.argv[2], sep=";")

    combined_df = pd.concat([df1, df2])
    combined_df.reset_index(drop=True, inplace=True)

    combined_df["metric_date"] = pd.to_datetime(combined_df["metric_date"])

    combined_df = combined_df.sort_values(by="metric_id")

    output_file_name = f"data_{date1}_{date2}_combined.csv"

    combined_df["combining_date"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    combined_df.to_csv(output_file_name, index=False)


if __name__ == "__main__":
    main()
