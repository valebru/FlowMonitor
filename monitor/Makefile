all:	top-sqlite3 top-mysql


top-mysql:
	g++ -ggdb -std=c++11 -I/usr/include/mysql -DBIG_JOINS=1  -fno-strict-aliasing    -g -DNDEBUG  main_mysql.cpp -o sip_topMYSQL -L/usr/lib/x86_64-linux-gnu -lmysqlclient -lpthread -lz -lm -ldl -lpcap -lcurses
	g++ -ggdb -std=c++11 -I/usr/include/mysql -DBIG_JOINS=1  -fno-strict-aliasing    -g -DNDEBUG mysql_showing.cpp -lcurses -o mysql_show -L/usr/lib/x86_64-linux-gnu -lmysqlclient -lpthread -lz -lm -ldl
	g++ -ggdb -std=c++11 -I/usr/include/mysql -DBIG_JOINS=1  -fno-strict-aliasing    -g -DNDEBUG mysql_test.cpp -lcurses -o mysql_test -L/usr/lib/x86_64-linux-gnu -lmysqlclient -lpthread -lz -lm -ldl
