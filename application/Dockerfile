ARG PythonVersion
FROM python:$PythonVersion
# pip インストールリストのコピー
COPY ./requirements.txt /tmp/requirements.txt
# pipのアップデート
RUN pip install --upgrade pip
# インストールリストを用いたpipによるmoduleのダウンロード
RUN pip install -r /tmp/requirements.txt
COPY . /var/application
# HOMEディレクトリを編集
WORKDIR /var/application/
