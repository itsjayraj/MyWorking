def first_dup_ch(str):
        i=0
        str=str.lower()
        for ch in str:
            i = i + 1
            #print "1: " + str[0:i-1]
            #print "2: " + str[i:]
            #print "3: " + ch
            if(ch not in str[:i-1] and ch not in str[i:]):
                print ch
                break

def Main():
        str = "First strif dup ch"
        first_dup_ch(str)

if __name__ == '__main__':
    Main()