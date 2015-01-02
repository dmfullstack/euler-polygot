public class Solution {

  private int range;
  private int solution;

  public Solution(){
    solution = 0;
  }

  public int solve(int x){
    range = x;
    for (int i = 0; i < range; i++ ) {
      if(i%3 == 0 || i%5 == 0){
        solution = solution + i;
      }
    }
    return solution;
  }

}