# DESCRIPTION

For this assignment I elected to do a more scalable solution instead of what I thought to be the easy and straightforward route to go about the algorithm. I have included the basic algorithm for finding terms within the dictionary as well as my solution using a SQLite database.

I think for complicated terms that involve multiple hashes the database solution may outperform the basic algorithm, but I was unable to produce a test case where building the database and searching for the matches was more efficient than going through the list and checking for a match in every term. If we don't count the database generation in the runtime (which we shouldn't do, but for analysis sake let's do it anyways) then the lookup vastly outperforms iterating through the whole list as CRUD functions in SQLite are O(1). 

As interesting as the databases were for the base cases, I used them immensely for the graduate hash. Thanks to an app that allowed me to run python programs on my phone, my second laptop, multiple friends' computers, and library computers I was actually able to find the terms. I looked into multithreading and multiprocessing but since the data set was so large (one trillion permutations long, to be exact) and the calculations were fairly straightforward those methods would do little to cut down the runtime. So what I did instead was take a database of x-character words and run every permutation from that database and another one of y-character terms. I started with >20 characters matched up against every length of term greater than 10, and worked my way down to matching 10 character terms up against every length of term >10 and hallelujah, the password was a 10 character term concatenated with an 11 character term. I fear that I may not have been able to get the answer if it was a permutation of a 6 or 8 character term because those datasets were absolutely massive. 



# INSTRUCTIONS

running the program is very straightforward. The first time you execute the program you have to add hw2.db to the PATH and run the hw2_dbgen.py file Once that is done, you can run the hw2_thomas_rider.py file. 
