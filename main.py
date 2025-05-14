import argparse
from reader.csv_reader import read_csv_files
from reports import get_report


def main():
    parser = argparse.ArgumentParser(description="Employee report generator")
    parser.add_argument("files", nargs="+", help="CSV data files")
    parser.add_argument("--report", required=True, help="Report name (e.g. payout)")

    args = parser.parse_args()

    data = read_csv_files(args.files)
    report_func = get_report(args.report)
    if not report_func:
        print(f"Unknown report type: {args.report}")
        return

    report_func(data)


if __name__ == "__main__":
    main()
