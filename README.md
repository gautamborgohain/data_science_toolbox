# Data Science Toolbox

A set of tools that I use for analysing data sets quickly and effectively - built as docker containers

## How to use?

1.  Cone this repo
2.   Run `docker-compose up`


To run only a specific tool, use `docker-compose up manifold`

To stop `docker-compose down`

The env var `DATA_FOLDER` folder is mounted into all the services as `/app/data`.   
The env var `NOTEBOOKS_FOLDER` dir is mounted additionally for jupyter, zeppelin and nbviewer


## List of Services added:
1.  [Hiplot](https://github.com/facebookresearch/hiplot) :  Fast parallel plot visualization  
    Paste link of csv url or, copy file to the `/data` dir, and then load it in hiplot using the prefix:
    `l://data/{fname}.csv`  
    
     *port* : `http:localhost:5005`
     
    Custom fetcher for hiplot to load from local csv file and do some simple preprocessing

    #### Usage (exp_uri):
    `l://data/{fname}.csv;{cmd}`
    
    Examples:
    
    1. Read from local csv:
        `l://data/experiments/exp_20200229/hiplot.csv`

    2. Read subset of the file (for quick view of big files):
        `l://data/experiments/exp_20200229/hiplot.csv;nrows=1000`

    3. View only select columns:
        `l://data/experiments/exp_20200229/hiplot.csv;cols=col1,col2,col3`

    4. Filter data by a value or values:
        Operations implemented:  
            **eq, gt, lt, lteq, gteq, in**  
        `l://data/experiments/exp_20200229/hiplot.csv;sub=abs_ppd:gt:0.10`

    You can chain operations like:
    `l://data/experiments/exp_20200229/hiplot.csv;nrows=10000;sub=abs_ppd:gt:0.10;sub=bedrooms:in:1,2`

    Compare Multiple experiments:
    ```
    multi://{
        "exp1_name": "exp1_uri",
        "exp2_name": "exp2_uri"
    }
    ```

     
2.  [TensorBoard](https://www.tensorflow.org/tensorboard/get_started): Includes the [What If Tool](https://github.com/pair-code/what-if-tool)
    for cross-sectional analysis of dataset. Set the `Path to examples` field to `data/{fname}.csv` file that
    is copied to the `/data` dir. Tensorflow Serving integrtion pending to load models for PDP plots
    and counter-factual inference
      
    *port* : `http:localhost:6006`
    
3.  [Manifold](https://github.com/uber/manifold):  Model Debugging tool. Upload csv files containing 
    features, predictions and ground truth. Sample generation is in [`notebooks/manifold_data_prep`](https://github.com/nightfoxbarricade/data_science_toolbox/blob/master/notebooks/manifold_data_prep.ipynb)
    
    *port* : `http:localhost:8080`
    
4.  [Jupyter Notebook/ Lab](https://hub.docker.com/r/jupyter/datascience-notebook/): Run jupyter notebook
    with nbextensions install. 
    
    *port* :   
    Jupyter Notebook `http:localhost:8888`  
    Jupyter Lab `http:localhost:8888/lab` 

5. [NbViewer](https://hub.docker.com/r/jupyter/nbviewer): View jupyter notebooks locally or on github; Present your notebooks

    *port* :  `http:localhost:8890`

6. [Zeppelin](https://zeppelin.apache.org): Interactive notebooks with Spark and interactive visualization. Also has version control of notebooks

    *port* :  `http:localhost:8889`


    
    
     