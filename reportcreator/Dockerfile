# $ docker run --rm -v `pwd`:/work -it reportcreator pdftk  *.pdf cat output test.pdf
FROM ubuntu

# The directory containing the PDF files to be processed is expected to be mounted here
# as a docker volume when running the container.
RUN mkdir /work
WORKDIR /work
VOLUME ["/work"]

RUN apt-get update  && \
    apt-get install -y --no-install-recommends unzip build-essential \
    libreoffice libreoffice-l10n-ja fonts-ipafont fonts-ipaexfont \
    pdftk-java && \
    apt-get clean
RUN fc-cache -fv
