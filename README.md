# Data Science Toolbox

A set of tools that I use for analysing data sets quickly and effectively - built as docker containers

## How to use?

1.  Cone this repo
2.   Run `docker-compose up`


To run only a specific tool, use `docker-compose up manifold`

To stop `docker-compose down`

The `/data` folder is mounted into all the services as `/app/data`.   
The `/notebooks` dir is mounted additionally for jupyter


## List of Services added:
1.  [Hiplot](https://github.com/facebookresearch/hiplot) :  Fast parallel plot visualization  
    Paste link of csv url or, copy file to the `/data` dir, and then load it in hiplot using the prefix:
    `lcsv://data/{fname}.csv`  
    
     *port* : `http:localhost:5005`
     
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
    Jupyter Notebook `http:localhost:8888/lab` 
    
    
     