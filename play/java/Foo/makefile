build:
	javac -d classes src/com/cc/tools/*.java

jar: build
	cd classes;  jar cfm Foo.jar ../src/manifest.txt com/cc/tools/*.class

run: jar
	java -jar classes/Foo.jar

clean:
	rm -rf classes/*
