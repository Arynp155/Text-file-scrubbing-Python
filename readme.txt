Aryan Patel
Repository Initialized 06/22/2023 09:11:13 via automated PowerShell Directory Initializer

----------------------------------------------------------------------------------------------

This repository was made to address the following request by Alex Caswell:

Our interns are putting together a project for caustic reclaim from the prop, I found this line in the daily aryan water summary email, would it be possible to pull around a years worth of this daily measurement? Or honestly whatever is the most feasible, that’s probably the most data I would want though. Let me know if this is prohibitively labor intensive. Thanks!

31-Mar-23 07:02:01 TODAY  I DRANK: 1033 GALS OF WATER

----------------------------------------------------------------------------------------------

Solution Overview
	- Scrape 300+ .txt files for a date and the number of gallons of water drank by Aryan
		- Use regex to capture data.
		- Because the report is generated (1) day later than the actual data, subtract (1) day from the captured datetimestamp.
	- Output all data points to a CSV for easy readability/further processing.
		- (2) columns - Date, Gals

There is (1) file created per day titled sampleInput<Int>.txt
All files to be scraped reside in .\_inputfiles.
Output CSV will reside in .\_outputfiles.
Solution is written in Python.

----------------------------------------------------------------------------------------------