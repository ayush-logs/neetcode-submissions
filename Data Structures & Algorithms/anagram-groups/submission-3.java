class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
            Map<String, List<String>> hm = new HashMap<>(); 

            for(String s : strs){
                String key = getKey(s); 
                hm.putIfAbsent(key, new ArrayList<>()); 
                hm.get(key).add(s); 
            }

            return new ArrayList<>(hm.values()); 
    }

    public static String getKey(String s){
        int[] count = new int[26]; 
        for(char ch : s.toCharArray()){
            count[ch - 'a']++;
        }
        return Arrays.toString(count); 
    }
}


/**
1. Initialise a Map<String, List<String>> 
2. Traverse the given List
3. Find the frequency map of each array, convert to string and store it as the key 
4. Group strings by key
5. Return the list of Map values

**/