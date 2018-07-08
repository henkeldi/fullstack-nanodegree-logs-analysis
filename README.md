# Logs Analysis

This program analyzes log data by quering a SQL Database.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

* VirtualBox: You can download it from the official site - [Oracle VM VirtualBox](https://www.virtualbox.org/wiki/Download_Old_Builds_5_1 "Oracle VM VirtualBox")
* Vagrant: You can download it from [vagrantup.com](https://www.vagrantup.com/downloads.html "Vagrant by HashiCorp")
* Pycodestyle: You can download it from the official [repository](https://github.com/PyCQA/pycodestyle "Python Style Checker") or using `pip install pycodestyle`

### Installing

Clone the `fullstack-nanodegree-vm` repo:

```
git clone https://github.com/udacity/fullstack-nanodegree-vm
```

Download and unpack the database into the `vagrant` folder

```
cd fullstack-nanodegree-vm/vagrant
wget https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip
unzip ./newsdata.zip
rm newsdata.zip
```

Download the source code into the `vagrant` folder:

```
git clone https://github.com/henkeldi/fullstack-nanodegree-logs-analysis.git
```

Build the vm image (this might take some minutes):

```
vagrant up
```

Log on to the virtual machine:

```
vagrant ssh
```

Setup the database:

```
cd /vagrant
psql -d news -f newsdata.sql
```

### Running the program

```
cd /vagrant/fullstack-nanodegree-logs-analysis/
python main.py
```

Example [output](./output.txt "Output document"):

```
1. What are the most popular three articles of all time?
"Candidate is jerk, alleges rival" — 338,647 views
"Bears love berries, alleges bear" — 253,801 views
"Bad things gone, say good people" — 170,098 views

2. Who are the most popular article authors of all time?
Ursula La Multa — 507,594 views
Rudolf von Treppenwitz — 423,457 views
Anonymous Contributor — 170,098 views
Markoff Chaney — 84,557 views

3. On which days did more than 1.0% of requests lead to errors?
July 17, 2016 — 2.3% errors
```

[![asciicast](https://asciinema.org/a/VrjkLdAPwFrh3FGEjJH9H6zbq.png)](https://asciinema.org/a/VrjkLdAPwFrh3FGEjJH9H6zbq)

## Running the tests

### Coding style tests

Checks the code against some of the style conventions in [PEP 8](https://www.python.org/dev/peps/pep-0008/ "PEP 8 -- Syle Guide for Python Code").

```
cd /vagrant/fullstack-nanodegree-logs-analysis/
pycodestyle main.py
```

## Authors

* **Dimitri Henkel** - *Initial work* - [henkeldi](https://github.com/henkeldi)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
