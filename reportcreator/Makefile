all:
	docker run --rm -v `pwd`:/work -it reportcreator python3 makereports.py
clean:
	rm -rf pdf/*
	rm -rf excel/*
	rm -rf report/*
	rm -rf result/*
	test -e all.pdf && rm all.pdf
