FROM apache/zeppelin:0.8.1

WORKDIR /zeppelin

COPY requirements.txt .

RUN conda create -n py37 python=3.7 &&\
	/opt/conda/envs/py37/bin/python -m pip install -r requirements.txt

CMD ["bin/zeppelin.sh"]