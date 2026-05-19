FROM python:3.10
WORKDIR /app
COPY . .
RUN pip install flask
RUN apt-get update && apt-get install -y openssh-server git
RUN mkdir -p /run/sshd
RUN echo 'root:1234' | chpasswd
RUN sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config
RUN git config --global user.email "jaferalkukhun1@gmail.com"
RUN git config --global user.name "Jaafarkukhon"
EXPOSE 5000
CMD service ssh start && python3 app.py