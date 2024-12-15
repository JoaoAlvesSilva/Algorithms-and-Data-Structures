// https://leetcode.com/problems/find-all-anagrams-in-a-string

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        from collections import Counter
        def anagram(s1, s2):
            return Counter(s1) == Counter(s2)
        
        indx =[]
        master_anagram = Counter(p)
        anagram = Counter(s[:len(p)])
        if master_anagram == anagram:
            indx.append(0)
        for i in range(1, len(s)-len(p) +1 ):
            anagram[s[i+len(p)-1]]+=1
            anagram[s[i-1]]-=1
            if master_anagram == anagram:
                indx.append(i)
        return indx



class Solution {
public:
    vector<int> findAnagrams(string s, string p) {
        map<char, int> master_anagram;
        for (auto &ch : p){
            master_anagram[ch]++;
        }
        vector<int> indx;
        map<char, int> anagram;
        for (int i = 0; i<p.length(); i++){
            anagram[s[i]]++;
        }
        if (anagram == master_anagram){
            indx.push_back(0);
        }
        if (p.length()>=s.length()){
            return indx;
        }
        for (int i = 1; i< (s.length()-p.length() +1); i++){
            anagram[s[i-1]]--;
            if (anagram[s[i-1]] ==0){
                anagram.erase(s[i-1]);
            }
            anagram[s[i+p.length()-1]]++;
            if (anagram == master_anagram){
                indx.push_back(i);
        }
            //cout << "for i=" << i << endl;
            //for (const auto& [key, value] : anagram){
                //cout << key << ": " << value << '\n'; 
                    //}
        }
        return indx;   
    }
};

        