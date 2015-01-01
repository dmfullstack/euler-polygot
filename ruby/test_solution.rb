require "./solution"
require "minitest/autorun"

# http://docs.seattlerb.org/minitest/Minitest/Assertions.html#method-i-assert

class TestSolution < Minitest::Test

  def test_fail
    assert(true, "Assertion was true")
  end

  def test_solution_limit_0
    assert_equal(0,solution(0))
  end

  def test_solution_limit_10
    assert_equal(23,solution(10))
  end

  def test_solution
    assert_equal(233168, solution(1000), "Solution is Correct")
  end

end