# Test task for the position Programmer Python
## Task description
Given text file, each line of which indicates the path to a folder or file.
If the line describes a file, then the file size in bytes is indicated, separated by a space.
You need to output a tree of folders and files in this format into a new text file
Within a folder, you should first display subfolders in alphabetical order, then files in descending order of size.
Files of the same size should be sorted alphabetically. Files may not have an extension.

## Example input data:
```
TEST1\TEST\b 77  
TEST1\TEST\C  
TEST1\TEST\Z\test 111  
TEST1\ABC\EFG\ZZZ\QWERTY\ASD\F\a.txt 16  
TEST1\ABC\EFG\ZZZ\QWERTY\ASD\F\c.txt 32  
TEST1\ABC\EFG\ZZZ\QWERTY\ASD\F\b.txt 32  
TEST1\ABC\EFG\ZZZ\QWERTY\ASD\F\F  
TEST3\TEST\B\XXX  
TEST3\TEST\a 111
```

## Example output data:
```
TEST1  
 ABC  
  EFG  
   ZZZ  
    QWERTY  
     ASD  
      F  
       F  
       b.txt  
       c.txt  
       a.txt  
 TEST  
  C  
  Z  
   test  
  b  
TEST3  
 TEST  
  B  
   XXX  
  a
```
