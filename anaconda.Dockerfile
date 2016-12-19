FROM continuumio/anaconda

# need to add
# sklearn, pandas, nltk, jupyter, numpy, tensorflow

RUN /opt/conda/bin/conda install jupyter pandas scikit-learn nltk numpy seaborn -y --quiet \
&& conda install -c conda-forge tensorflow -y --quiet \
&& apt-get install -y gcc g++ && pip install bhtsne

RUN python -m nltk.downloader -d /usr/local/share/nltk_data brown

EXPOSE 6006
EXPOSE 9000

VOLUME ["/host"]

WORKDIR "/host"

CMD ["/opt/conda/bin/jupyter", "notebook", "--notebook-dir=/host", "--ip='*'", "--port=9000","--no-browser"]

