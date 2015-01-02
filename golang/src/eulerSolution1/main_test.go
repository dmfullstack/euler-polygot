package eulerSolution1

import "testing"

func TestXtesting(t *testing.T) {
}

func TestSolutionLimit0(t *testing.T) {
	sol := solve(0)
	if sol != 0 {
		t.Errorf("Solution is not was %v", sol)
	}
}

func TestSolutionLimit10(t *testing.T) {
	sol := solve(10)
	if sol != 23 {
		t.Errorf("Solution is not was %v", sol)
	}
}

func TestSolutionLimit1000(t *testing.T) {
	sol := solve(1000)
	if sol != 233168 {
		t.Errorf("Solution is not 233168 was %v", sol)
	}
}
