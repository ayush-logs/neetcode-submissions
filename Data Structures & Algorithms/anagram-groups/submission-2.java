// return type -> list<list>
// anagrams -> sorting, frequncy map, fixed size array, hashset(?)
// only lowercase english letters -> fixed size array


class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<String, List<String>> hm = new HashMap<>();

        for(String s : strs){
            int[] charFreq = new int[26]; 

            for(char ch : s.toCharArray()){
                charFreq[ch - 'a']++; 
            } 

            String strIdentifier = Arrays.toString(charFreq); 
            hm.putIfAbsent(strIdentifier, new ArrayList<>()); 
            hm.get(strIdentifier).add(s); 
        }

        return new ArrayList<>(hm.values()); 
    }
}
