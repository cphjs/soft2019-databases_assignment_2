# Assignment 2

This little script will connect to a local instance of MongoDB and run some queries against twitter data.
To change a the MongoDB server address, database and/or collection name see [configuration](#configuration).

The script assumes you already have the twitter data. If not, see [data section](#data)

When you run main.py it will print out the answers to questions asked in the [assignment](https://github.com/datsoftlyngby/soft2019spring-databases/blob/master/lecture_notes/02-Intro_to_MongoDB.ipynb). The script contains methods to get the results for all of them. See example output from [my results](#results)

**Warning!** Finding the most mentioned users will take **AN UNREASONABLY LONG** time. By default that part of the script is commented out. If you really want to run that monstrosity, go into the script and uncomment code after the `Most mentioned users` print. But consider yourself warned. 

# Configuration

By default the script is configured to connect to MongoDB server at `localhost`(your own computer), use a database called `social_net` and the collection `tweets`. To change this for your environment you will have to modify the script and set `client`, `db` and `tweets` variables to your preferences. 

# Data

You should have downloaded the data as part of doing your own assignment following the instructions [here](https://github.com/datsoftlyngby/soft2019spring-databases/blob/master/lecture_notes/02-Intro_to_MongoDB.ipynb#your-turn-at-home).

In case you did not, I provide instructions for unix-like systems. Windows people are on their own.
**Warning!** If you run this and you already have a database called `social_net` with a collection `tweets`, it will get deleted and overriden with this data. 

Run this in your favourite shell
```
wget http://cs.stanford.edu/people/alecmgo/trainingandtestdata.zip
unzip trainingandtestdata.zip
mongoimport --drop --db social_net --collection tweets --type csv --fields "polarity,id,date,query,user,text" --file training.1600000.processed.noemoticon.csv
```

# How to run it

Clone repo.

You can do this via the command-line by writting `git clone https://github.com/cphjs/soft2019-databases_assignment_2.git` or by your own preffered method.

## IDE 

 * Open project in your favourite IDE
 * Run main.py file

## Command-line 

```
python3 main.py
```

# Dependencies

 * Python3
   * pymongo

Python libraries can be installed using pip3:
```
pip3 install pymongo
```

# Results

This is sample output from me running it a docker container. Your experience may vary.
