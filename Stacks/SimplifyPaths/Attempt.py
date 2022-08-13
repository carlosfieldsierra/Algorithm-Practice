'''
    Given a string A representing an absolute path for a file (Unix-style).
    Return the string A after simplifying the absolute path.

    Note:

    In Unix-style file system: 

    A period '.' refers to the current directory.
    A double period '..' refers to the directory up a level.
    Any multiple consecutive slashes '//' are treated as a single slash '/'.
    In Simplified Absolute path:

    The path starts with a single slash '/'.
    Any two directories are separated by a single slash '/'.
    The path doesn't end with trailing slashes '/'.
    The path only contains the directories on the path from the root directory 
    to the target file or directory (i.e., no period '.' or double period '..')
    Path will not have whitespace characters.
'''

# O(N) runtime | O(N) spacetime
def solve(A):
    stack = A.split("/")
    stack.reverse()
    
    ansStack = []
    while stack:
        value = stack.pop()
        if value == "" or value=="." or value=="":
            continue
        if value == "..":
            if ansStack:
                ansStack.pop()
            continue
        
        ansStack.append(value)

    ans = "/" + "/".join(ansStack)
    
    return ans
    
        
        

    

def Main():
    ans = solve("/a/./b/../../c/")
    print(f"Anwser: {ans}")
    ans = solve("/home/../../tmp//./")
    print(f"Anwser: {ans}")

 
if __name__ == "__main__":
    Main()