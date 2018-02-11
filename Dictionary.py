self = {"name":"Ray", "age":"39", "country of birth":"The United States", "favorite language":"Python"}
                                            #dictionary created with literal notation above
def who(tiona):                             #set function
     for key, data in tiona.items():        #loop through keys and values initialized
         print "My", key, "is", data + "."  #print statement for each key,value pair formatted

who(self)                                   #function called 