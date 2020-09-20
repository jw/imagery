Install
=========

docker run --name imagery -e POSTGRES_PASSWORD=s3cr3t -e POSTGRES_USER=imagery -p 65432:5432 -d postgres:9
export DATABASE_URL=postgres://imagery:s3cr3t@127.0.0.1:65432/imagery

python manage.py migrate

curl -o latest.dump `heroku pg:backups public-url` (or get it via your browser)
docker cp latest.dump imagery:/tmp
docker exec -it imagery pg_restore -U imagery -d imagery /tmp/latest.dump

mkdir -p imagery/imagery/media/artists
cp imagery/images imagery/imagery/media/artists

python manage.py runserver
