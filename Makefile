DST := 'Andrew-Hoyt-Resume.pdf'
SRC := resume.md.tpl

.PHONY: build clean

build: $(DST)

$(DST): $(SRC)
	./generate -i $(SRC) -o $(DST)

clean:
	rm $(DST)

