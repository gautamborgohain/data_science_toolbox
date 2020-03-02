import hiplot as hip
import pandas as pd


def fetch_local_csv_experiment(uri):
    """
    Custom fetcher for hiplot to load from local csv file and do some simple preprocessing

    Usage:

    1. Read from local csv:
        l://data/experiments/exp_20200229/hiplot.csv

    2. Read subset of the file (for quick view of big files:
        l://data/experiments/exp_20200229/hiplot.csv;nrows=1000

    3. View only select columns:
        l://data/experiments/exp_20200229/hiplot.csv;cols=col1,col2,col3

    4. Filter data by a value or values:
        Operations implemented:
            eq, gt, lt, lteq, gteq, in
        l://data/experiments/exp_20200229/hiplot.csv;sub=abs_ppd:gt:0.10

    You can chain operations like:
    l://data/experiments/exp_20200229/hiplot.csv;nrows=10000;sub=abs_ppd:gt:0.10;sub=bedrooms:in:1,2

    :param uri: the experiment uri
    :return: hip.Experiment
    """
    PREFIX = "l://"

    if not uri.startswith(PREFIX):
        # Let other fetchers handle this one
        raise hip.ExperimentFetcherDoesntApply()

    # Parse out the local file path from the uri
    options = uri[len(PREFIX):].split(";")  # Remove the prefix

    local_path = options[0]  # Get the path to file

    # the preprocessing opertations
    if len(options) > 1:

        # First check if subset of the dataset is to be loaded
        if options[1].split("=")[0] == "nrows":
            nrows = int(options[1].split("=")[1])
            df = pd.read_csv(local_path, nrows=nrows)
            options = options[1:]
        else:
            df = pd.read_csv(local_path)

        # For any options, preprocess
        for opt in options[1:]:
            try:
                k, v = opt.split('=')

                if k == "cols":
                    cols = v.split(",")
                    cols = set(cols) & set(df.columns)
                    df = df[cols]

                if k == "sub":
                    col, operation, values = v.split(":")
                    values = values.split(',')
                    val = values[0]
                    if col in df.columns:
                        if operation == "eq":
                            df = df[df[col] == val]
                        elif operation == "lt":
                            df = df[df[col] < float(val)]
                        elif operation == "lteq":
                            df = df[df[col] <= float(val)]
                        elif operation == "gt":
                            df = df[df[col] > float(val)]
                        elif operation == "gteq":
                            df = df[df[col] >= float(val)]
                        elif operation == "in":
                            df = df[df[col].isin(values)]

            except Exception as e:
                print(f"Exception performing opertation: {opt} : {e}")

        df = df.to_dict("records") # Convert to dict for hip.Experiment
        return hip.Experiment.from_iterable(df)

    else:
        # Return the hiplot experiment to render
        return hip.Experiment.from_csv(local_path)
