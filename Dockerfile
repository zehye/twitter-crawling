FROM ubuntu:18.04
MAINTAINER maintain

# update, upgrade
RUN                 apt -y update && apt -y dist-upgrade

# zsh
RUN                 apt -y install zsh curl git
RUN                 curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh | bash
RUN                 chsh -s /usr/bin/zsh

ENV                 AWS_ACCESS_KEY_ID ACCESS_KEY_ID
ENV                 AWS_SECRET_ACCESS_KEY SECRET_ACCESS_KEY
ENV                 AWS_DEFAULT_REGION REGION