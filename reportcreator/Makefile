all:
	docker run --rm -v `pwd`:/work -it reportcreator python3 makereports.py
clean:
	rm -rf pdf/*
	rm -rf resource/*
	rm -rf report/*
	rm -rf result/*
	test -e pc.pdf && rm pc.pdf
	test -e pll.pdf && rm pll.pdf
	test -e all.pdf && rm all.pdf
