class Solution {
    public int numberOfMatches(int n) {
        int matches = 0;
        while(n !=1){
            if(n%2==0){
                matches = matches + n/2;
                n = n/2;
            }else{
                matches = matches + Math.abs(n/2);
                n = Math.abs(n/2)+1;
            }
        }
        return matches;
        
    }
}
