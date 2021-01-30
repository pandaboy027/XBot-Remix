# We're using Ubuntu 20.10
FROM xnewbie/docker:groovy

#
# Clone repo and prepare working directory
#
RUN git clone -b x-sql-extended https://github.com/Camel07/XBot-Remix /root/userbot
RUN mkdir /root/userbot/.bin
RUN pip install --upgrade pip setuptools
WORKDIR /root/userbot

#Install python requirements
RUN pip3 install -r https://raw.githubusercontent.com/Camel07/XBot-Remix/x-sql-extended/requirements.txt

CMD ["python3","-m","userbot"]
