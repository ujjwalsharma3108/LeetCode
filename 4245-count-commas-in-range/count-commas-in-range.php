class Solution {

    /**
     * @param Integer $n
     * @return Integer
     */
    function countCommas($n) {
        return $n > 999 ? $n-999 :0;
    }
}