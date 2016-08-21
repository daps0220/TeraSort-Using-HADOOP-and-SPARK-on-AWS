
# This read me file content the program execution of Shared Memory, Hadoop and Spark


###########################################

SHARED MEMORY

###########################################

	
	- open terminal on launched instance on AMAZON EC2
	
	python shared_memory_10gb.txt

	Enter No. of Threads : 1/2/4

###########################################

HADOOP

###########################################


	- launch and configure hadoop on instance mentiond in congiguration

	./hadoop hadoop-mapper.py|hadoop-reducer.py <input-file-path> <output-file-path>


##########################################

SPARK

##########################################


	- launch and configure spark on instance mentiond in congiguration

	- open pyspark(Python shell) shell in master node and run 3 command mentioned below 

	sortedFile = sc.textFile("hdfs://PUBLIC DNS :9000/user/hadooo/input/spark_tera_10gb.txt")

	sortedObj = sortFile.flatMap(lambda line:ine.split("\n")).map(lambda dicto:(str(dicto[:10]),str(dicto[10:]))).sortByKey().map(lambda (a,b) : a+b)

	sortedObj.saveAsTextFile("hdfs://Public DNS :9000/user/hadoop/output_filnal")


############################################
