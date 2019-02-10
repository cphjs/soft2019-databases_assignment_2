# Assignment 2

This little script will connect to a local instance of MongoDB and run some queries against twitter data.
To change a the MongoDB server address, database and/or collection name see [configuration](#configuration).

The script assumes you already have the twitter data. If not, see [data section](#data)

When you run main.py it will print out the answers to questions asked in the [assignment](https://github.com/datsoftlyngby/soft2019spring-databases/blob/master/lecture_notes/02-Intro_to_MongoDB.ipynb). The script contains methods to get the results for all of them. See example output from [my results](#results)

**Warning!** Finding the most mentioned users will take **AN UNREASONABLY LONG** time. Consider this part of the assignment not completed. By default that part of the script is commented out. If you really want to run that monstrosity, go into the script and uncomment code after the `Most mentioned users` print. But consider yourself warned. 

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

```
Distinct users: 659774
This took 3401 MS

Users mentioning others the most:
cchastain - 12 mentions
janeylicious - 11 mentions
HalfassBackward - 11 mentions
esoterismo - 11 mentions
DaRevolutionary - 11 mentions
Mia_R - 11 mentions
dottibailey - 11 mentions
indyval - 11 mentions
kittylaney - 11 mentions
jobrich - 11 mentions
This took 11209 MS

Most mentioned users
===============================================
This section was commented out because its slow
===============================================

Most active user(by number of tweets)
lost_dog - 549 tweets
webwoke - 345 tweets
tweetpet - 310 tweets
SallytheShizzle - 281 tweets
VioletsCRUK - 279 tweets
This took 4371 MS

Most grumpy users:
lost_dog - 549 negative tweets
tweetpet - 310 negative tweets
webwoke - 264 negative tweets
mcraddictal - 210 negative tweets
wowlew - 210 negative tweets
This took 3638 MS

Most happy users:
what_bugs_u - 246 positive tweets
DarkPiano - 231 positive tweets
VioletsCRUK - 218 positive tweets
tsarnick - 212 positive tweets
keza34 - 211 positive tweets
This took 3719 MS
```