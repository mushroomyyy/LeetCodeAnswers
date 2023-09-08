class Solution {
    public boolean containsDuplicate(int[] nums) {
        Map<Integer, Integer> countHashMap = new HashMap<>();
        for (int num : nums) {
            if(countHashMap.containsKey(num)) {
                countHashMap.put(num, countHashMap.get(num)+1);
            }
            else {
                countHashMap.put(num, 1);
                 }
         }
         for (int count: countHashMap.values()) {
             if (count>1){
                 return true;
             }
         }
        return false;                 
     } 
}