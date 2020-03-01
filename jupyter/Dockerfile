FROM jupyter/datascience-notebook

RUN /opt/conda/bin/conda install jupyter -y --quiet

# Install jupyter nbextensions
RUN pip install jupyter_contrib_nbextensions && \
	pip install https://github.com/ipython-contrib/jupyter_contrib_nbextensions/tarball/master && \
	/opt/conda/bin/jupyter contrib nbextension install --user

# Install nbextensions configurator
RUN pip install jupyter_nbextensions_configurator && \
	/opt/conda/bin/jupyter nbextensions_configurator enable --user


EXPOSE 8888

WORKDIR /app

CMD /opt/conda/bin/jupyter notebook --notebook-dir=/app --ip='*' --port=8888 --allow-root --no-browser --NotebookApp.token=''
