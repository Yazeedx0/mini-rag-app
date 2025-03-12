# mini-rag-app
```bash
cd /mnt/c/Users/'yazeed kamel'/Downloads/mini-rag

export PS1="\[\033[01;32m\]\u@\h:\w\n\[\033[00m\]\$ "

uvicorn main:app --reload
```

```bash
sudo docker stop $(sudo docker ps -aq)
sudo docker rm $(sudo docker ps -aq)
sudo docker rmi $(sudo docker images -q)
sudo docker volume rm $(sudo docker volume ls -q)
sudo docker system prune --all