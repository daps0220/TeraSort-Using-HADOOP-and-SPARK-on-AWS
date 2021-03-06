import random
import string
import os
import time
import multiprocessing

####################################################################################

# Main function which do chunk sort of each 20MB files. ############

#####################################################################################


def chunk_sort(file_p):
    temp_file_count = 0
	line_count = 0 
	############### this for loop is divide 1st 10 character as keys and put into one file for sorting #################
	for line in file_p.readlines():
        whole_dict[line[:10]] = line[10:] # make keys for sorting
        if(cnt % no_of_lines == 0):
            keys = []
            cnt = 0
            keys.append(line[:10]) # list of keys of chunk
            cnt += 1
            fp = open("/mnt/temp/" + str(temp_file_count) + ".txt", "w") # open all temp files with perticular temp file count 
            temp_file_count += 1      
        else:
            if cnt >= (lines-2):
                keys.append(keys[:10])
                for i in mergesort(keys): # call merge_sort function for those keys of each temorary chunk
                    file_p.write(line + "\n") # write sorted output into file
                file_p.close() #close file
            else:
                keys.append(line[:10]) 
            line_count += 1

	all_temp_files = [] # store all sotred chunk into one list
    for each_file in os.listdir("/mnt/temp/"): 
            all_temp_files.append(each_file) # add all temporary files into list
	line_list = []
	for f in files:
        f_temp = open("/mnt/temp/" + f, "r")
        line_list.append(f_temp.read().split("\n")) # take all file's line spilt by ENTER
        f_temp.close()
	line_list = mergesort(line_list)  # mergesort for all sorted chunks...
    output = open(�/mnt/output_shared/opt_final�, 'w') # write output into a output file.
    for keys in line_list:
        out.write(keys + whole_dict[keys]) # write all sorted key and values into output file.
    output.close() # close file

	
##############################################################################	

######### used mergesort  function from cited link in REFRENCEs ###############

##############################################################################

def mergesort(arr):  
    if len(arr) == 1:  
        return arr  
      
    m = len(arr) / 2  
    l = mergesort(arr[:m])  
    r = mergesort(arr[m:])  
  
    if not len(l) or not len(r):  
        return l or r  
          
    result = []  
    i = j = 0  
    while (len(result) < len(r)+len(l)):          
        if l[i] < r[j]:  
            result.append(l[i])  
            i += 1  
        else:  
            result.append(r[j])  
            j += 1              
        if i == len(l) or j == len(r):              
            result.extend(l[i:] or r[j:])  
            break  
          
    return result  

###################################################################

######## Main Function ################

###################################################################
	
	
	
if __name__ == '__main__':

    whole_dict = {}   ######### store whole file data into dictonary ############### 

    s_time = time.time() ############# start timer as start time ###########

    fp = open(�/mnt/shared_input_10gb.txt� , 'r') ########## open input file 
	
    no_of_threads = raw_input("Enter No. Of Threads : ") ##### user input no. of threads..

    no_of_files = 500 # for 20MB chunk size i need to make 500 temporary files. #### number of temporary files
    file_size = os.stat(�/mnt/shared_input_10gb.txt�).st_size ## file size 

    no_of_lines = int(file_size / (no_of_files * 10)) ######### count number of files

	############ start multi-threading as Process in Python ###############
    thread = Process(target=chunk_sort, args=(file_size/no_of_threads,)) ######### do sorting using thread
    thread.start() ###### start thread
    thread.join()  ########## join thread 

    fp.close()

	########## print output files
	
    print 
    print "*"*20,i " threads time taken is " + str(time.time() - starttime) + " seconds", "*"*20

    for files in os.listdir(�/mnt/temp/�):
		os.unlink("/mnt/temp"+files)



