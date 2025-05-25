class Solution:
    def compress(self, chars: List[str]) -> int:
        read,write=0,0
        n=len(chars)

        while read<n:
            current_char=chars[read]
            count=1

            while read+1<n and chars[read+1]==current_char:
                read+=1
                count+=1
            
            chars[write]=current_char
            write+=1

            if count>1:
                count_str=str(count)
                for digit in count_str:
                    chars[write]=digit
                    write+=1
            
            read+=1

        return write