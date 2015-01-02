import org.junit.* ;
import static org.junit.Assert.* ;

public class SolutionTest {

   @Test
   public void test_returnZero() {
      System.out.println("Test if solution returns Zero...") ;
      Solution S = new Solution() ;
      assertEquals(S.solve(0), 0) ;
   }

   @Test
   public void test_returnFor10() {
      System.out.println("Test if solution returns 23...") ;
      Solution S = new Solution() ;
      assertEquals(S.solve(10), 23) ;
   }

   @Test
   public void test_returnFor1000(){
      System.out.println("Test if solution returns 233168...") ;
      Solution S = new Solution() ;
      assertEquals(S.solve(1000), 233168) ;
   }
}