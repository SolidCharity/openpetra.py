recreatedb:
	python manage.py createmodel
	rm -f apps/data/migrations/000* && python manage.py makemigrations
	echo "yes" | python manage.py reset_db && python manage.py migrate
	#mysqldump --defaults-file=.my.cnf openpetra_py | gzip > openpetra_py.sql.gz
	pg_dump --user openpetra_py -d openpetra_py --clean | gzip > openpetra_py.sql.gz

resetdb:
	#zcat openpetra_py.sql.gz | mysql  --defaults-file=.my.cnf openpetra_py
	zcat openpetra_py.sql.gz | psql -U openpetra_py openpetra_py

importdb:
	# python manage.py importdatabase --ymlfile=definitions/demoWith1ledger.yml --debug=True --startattable AGiftBatch
	# python manage.py importdatabase --ymlfile=definitions/small.yml --debug=True
	python manage.py importdatabase --ymlfile=definitions/exportedDatabase.yml
