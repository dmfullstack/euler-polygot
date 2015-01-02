package eulerSolution1

func solve(x int) int {
	var z int
	for i := 0; i < x; i++ {
		if i%3 == 0 || i%5 == 0 {
			z = z + i
		}
	}
	return z
}
