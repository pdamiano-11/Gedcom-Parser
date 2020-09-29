import pandas as pd
import Project02

'''
This function checks to see if there are any married siblings in the input .ged file
If there are no married siblings, the function returns True
If there are married siblings, the function returns a string of the individuals that violate the rule
'''
def siblingsShouldNotMarry(gedcom_name):
	df = Project02.createIndividualsDataFrame(gedcom_name)

	famDict = {}
	error_string = "" 

	for index, row in df.iterrows(): #iterates through dataframe
		famDict[row['Name']] = list([row['Child'],row['Spouse']]) #stores every Child, Spouse combination in famDict

	for entry in famDict:
		for secondEntry in famDict:
			#loops through every pair in famDicts
			if entry == secondEntry: #same individual
				continue
			elif famDict[entry][0] == famDict[secondEntry][0] and famDict[entry][1] == famDict[secondEntry][1]: 
				#checks if any two individuals have the same child ID and family ID pair, indicating a sibling marriage
				error_string = error_string + " " + entry + "," #constructs string of all individuals in sibling marriages

	if(error_string == ""):
		return True #no sibling marriages
	else: 
		#sibling marriages
		if(error_string[len(error_string)-1] == ","):
			error_string = error_string[0:len(error_string)-1]
		s = "The following individuals are marrying their siblings, which is not allowed:" + error_string
		return(s)