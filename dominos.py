# -*- coding: utf-8 -*-
"""
Created on Thu Oct 05 19:08:27 2017

@author: wildcat
"""

import csv
from gurobipy import *
import sqlite3

"""
import os
os.chdir('C:\Users\wildcat\Documents\GitHub\or604pizzaV2')
print os.getcwd()
"""

       

########################## LOAD THE DATA FROM CSV #################3
#Loads the OR604 Good Dominos Data in as Tuples
with open('OR604 Good Dominos Data.csv') as f:
    goodData=[tuple(line) for line in csv.reader(f)]
#print goodData

#source: https://stackoverflow.com/questions/18776370/converting-a-csv-file-into-a-list-of-tuples-with-python 
#Loads the OR604 Good Dominos Data in as Tuples
with open('OR 604 Dominos Daily Demand.csv') as f:
    demand=[tuple(line) for line in csv.reader(f)]
#print demand

########################## LOAD THE DATA INTO SQL DATABASE#################3
import sqlite3 
con = sqlite3.connect("C:\Users\wildcat\Documents\GitHub\or604pizza\DominoDatabase.db")

##goodData Table
con.execute("create table if not exists goodData(StoreNumber, Store, Street, City, State, Zip, Latitute, Longitude)")
con.executemany("INSERT INTO goodData (StoreNumber, Store, Street, City, State, Zip, Latitute, Longitude) VALUES (?,?,?,?,?,?,?,?)", goodData)
con.commit()
con.close

##Demand Table
con = sqlite3.connect("C:\Users\wildcat\Documents\GitHub\or604pizza\Demand.db")
con.execute("create table if not exists Demand(Date, StoreNumber, PizzaSales)")
con.executemany("INSERT INTO Demand (Date, StoreNumber, PizzaSales) VALUES (?,?,?)", demand)
con.commit()
con.close


    #2 files
    #1 file has all the stores and street addresses
    #211 megs. has 6.5 years of daily demand data for hte stores
    
    #how many stores do i have? write the info in a database and then index it on the store number.  
    #then write a query in sql (why do you index? it makes everything faster)
    #next do an aggregating function and group it by store
    #next find the average daily demand. group by store. this will give me average daily demand per store.
    #take that information. that has been aggregated and export it to another table. (we won't have to run the aggregate function again). this will speed things up
    #this is much faster. should hvae 4000 aggregated data (4000 is stores, i believe)
    #do another query asking if i have demand for all of them? (not all stores will have demand)
    #to capture demand for every store, aggregate by some function, charb set zip code (i.e. 6301x)...basicall a good justification
    #do a library(haversine) loop for all stores
    
    
    # Supply Constraint #each distribution center will have a demand constraint. 16 distribution centers. for my supply, we will iterate over the distribution center.
    # Demand Constraints. #4000 demand constraints, sum over the 16 distribution centers. 
    
     #don't forget gas code mileage to ship for each distribution center is (it's in teh background info file)
    #for the distribution cetner dictionary, (supply/7)*4/float = int. s.t. demand*4

    #not worried about flour or tomato sauce. just the pizza dough to worry about
    #20% of the truck will be filled by sauce and flour. other 80% is filled by dough. dough is the driving cost
    #have to figure out half week supply for every distribution center. cost per mile . 4 days for half week. for store dictionary we will have daily demand.
   
        
    #DC1: half week supply, cost per mile. store as at tuple
    # #of doughs/distribution center.
    
  
 #what does the decision variable in this problem represent? the number of doughs sent from thsi distribution cetner sent to that store
 
 # xds = number of doughs shipped for d to s
 # double index this.
 
    #rough python code
#    for d in DC:
#        for s in store:
#                myPizza.addVarObj = ,vtype = GRB.continuous, name...)
#        myPizza.update
        
        #this will create 16 * ~4000 of these variables. save all the variables into another dictionary (variable dictionary)
        #don't forget to update
        
              
        # objective function is to minimize
        #we have cost per mile. we got miles and pizza doughs. we got a cost fator per distribution center * times distro center to store * # of pizza doughs from store. this will tell us dollars per pizza dough. some where in the write up it says 9900 pizza doughs per truck.
        # this is dollars per truck (once we divive by 9900pizzas). this is dollars per truck load) (there's something else in the write up we may need to add in here)
    # this objective function coeffiecent is cost factors *miles divide by 9900. this tells us dollars per truck load.
    

 # xds*mds*fd