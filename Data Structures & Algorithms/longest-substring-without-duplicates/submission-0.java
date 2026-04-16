class Solution {
    public int lengthOfLongestSubstring(String s) {
        int maxLength = 0, l = 0; 
        Set<Character> hs = new HashSet<>(); 
        for(int r = 0; r < s.length(); r++){
            char ch = s.charAt(r); 
            while(hs.contains(ch)) hs.remove(s.charAt(l++));
            hs.add(ch); 
            maxLength = Math.max(hs.size(), maxLength); 
        }
        return maxLength; 
    }
}
