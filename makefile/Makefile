PROG_NAME ?= conway

prog: main.o functions.o
	gcc -o $(PROG_NAME) main.o functions.o
main.o:
	gcc -c -o main.o main.c
functions.o: functions.c
	gcc -c -o functions.o functions.c

%.o: %.c
	gcc -o $@ -c $^

.PHONY: clean
clean:
	rm -f *.o
	rm -f $(PROG_NAME)

.PHONY: install
install: $(PROG_NAME)
	install -m 655 -o root $(PROG_NAME) /usr/bin