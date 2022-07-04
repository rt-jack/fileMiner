import os;

from datetime import datetime as dt;


def isFile (f): 
   curr_path = os.getcwd();
   
   try:
       
       os.chdir(f);
       return False;
       
   except NotADirectoryError:
       return True;
       
   finally:
	    
	    os.chdir (curr_path);
	    

	
def sameFiles (f1, f2):
    return f1.lower() == f2.lower();



class FileMiner:


	def __init__ (self, filename  ):

		self.filename = filename;
		
		self.locations = set();

		self.num = 0;
	
	def get_locations (self):
	    
	    print ("Searching locations...");
	    
	    self._operation ("locations");
	    
	    print ("Locations: ");
	    
	    for loc in self.locations:
	        print (loc);
	    
	def count_num (self):
	    
	    print ("Counting files... ");
	    
	    self._operation ( "count_num");
	    
	    print ("Number of files: %d"%(self.num));
	    
	  
	def delete_all (self):
	   
	   print ("Deleting files... ");
	   
	   self._operation ( "delete_all");
	   
	   print ("Files deleted :)");
	    
	    
	   
	    


	def _operation ( self, oper ):
	    
	 
		curr_dirs = os.listdir();
		
		curr_path = os.getcwd();


		for d in curr_dirs:
		    
		    #print (d);
		    
		    if isFile(d):
		        
		        if sameFiles(d, self.filename):
		            
		            
		            if oper == "count_num":
		                self.num += 1;
		                
		            elif oper == "delete_all":
		                os.remove (self.filename);
		            elif oper == "locations":
		                
		                self.locations.add (os.getcwd());
		                
		    else:
		        #print (os.getcwd())
		        os.chdir (d);
		        self._operation (oper);
		        os.chdir(curr_path);
		        

		

ob = None;

def parseCmd (cmd):
    
    global ob;
    
    options = "option", "filename"; 
    
    
    cmds = cmd.split(); # [set, option, function]
    
    
    assert len (cmds) == 3, "SyntaxError";
    
    assert cmds[0] == "set", "Missing 'set' ";
    
    assert cmds[1] in options, "argument 2 should either be 'filename' or 'option' ";
    
    if cmds[1] == "filename":
        
        
        ob = FileMiner ( cmds[2] );
        
        
    elif cmds[1] == "option":
        
        assert ob, "filename is not set";
        
        if cmds[2] == "count":
            ob.count_num();
            
        elif cmds[2] == "delete_all":
            ob.delete_all();
            
        elif cmds[2] == "locations":
            ob.get_locations();
         
            
        else:
            
            raise AssertionError ("could not perform %s"%(cmds[2]));
            
        return "countable";
            
        
    
    
    

help_string = """

Welcome to <!--- FileMiner -->

You can utilize this program to perfom either of the following:
    
    1. Count the number of files that match the given file name from the current directory.
    
    2. Delete all files that match the given file name from the current directory.
    
    3. Find locations of files that match the given file name from the current directory.
    
    example:
        > set filename script.py
        > set option count
        
        Counting files...
        Number of files: 5
        
    example:
        > set filename script.py
        > set option delete_all
        
        Deleting files...
        Files deleted :)
    
    example:
        > set filename script.py
        > set option locations
        
        Searching locations...
        Locations:
            /home/username/
            /home/username/Desktop
            
  
  """
  
  

while True:
    
    cmd = input ("> ");
    
    if not cmd or cmd.lower() == "exit" or cmd.lower() == "exit()":
        break;
    
    if cmd == "help":
        
        print (help_string)
        continue;
        
    print (cmd)
    
    start_time = dt.now();
    countable = parseCmd (cmd);
    end_time = dt.now();
    
    if countable:
        print ("time (s): ", (end_time.second - start_time.second) );
 

