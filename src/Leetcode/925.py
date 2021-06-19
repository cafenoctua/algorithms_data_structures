class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        idx_src= 0
        
        size_src, size_type = len(name), len(typed)
        
        for idx_type, char_type in enumerate(typed):
            
            if idx_src < size_src and name[idx_src] == char_type:
                # current type char is matched with friend's name char
                idx_src += 1 
                
            elif idx_type == 0 or typed[idx_type] != typed[idx_type-1]:
                # If first character mismatch, or it is not long-pressed repeated characters
                # Reject
                return False
        
        # Accept if all character is matched with friend name
        return idx_src == size_src




sol = Solution()
print(sol.isLongPressedName("alex", "aaleex"))
print(sol.isLongPressedName("saeed", "ssaaedd"))
print(sol.isLongPressedName("rick", "kric"))
print(sol.isLongPressedName("vtkgn", "vttkgnn"))
print(sol.isLongPressedName("vtkgn", "vttkgnn"))