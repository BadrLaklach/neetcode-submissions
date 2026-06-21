class Solution {
public:
    bool isAnagram(string s, string t) {
        unordered_map<char,int> Scount;
        unordered_map<char,int> Tcount;

        if (s.length() != t.length()){
            return false;
        }

        for( char si:s ){
            Scount[si]++;
        }
        for( char ti:t ){
            Tcount[ti]++;
        }

        for( int i ; i < s.length() ; i++){
            if (Scount[s[i]] != Tcount[s[i]]){
                return false;
            } 
        }
        return true;

        

    }
};
