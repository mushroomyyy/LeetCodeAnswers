class Solution {
    public int lengthOfLastWord(String s) {
        s = s.trim(); // pass test cases with " " at the end of the string
        int l = s.length();
        int lwl = 0;
        // for length -1 if i > 0 i -- 
        for (int i = l - 1; i >= 0; i --) {
            if (s.charAt(i) == ' ') {
                break;
            }
            lwl++;
        }

        return Math.max(lwl,1);
    }
}