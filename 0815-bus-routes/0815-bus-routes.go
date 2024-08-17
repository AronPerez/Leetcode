func numBusesToDestination(routes [][]int, source int, target int) int {
     if source == target {
        return 0
    }

    // Create a map to store bus stops and the buses that stop there
    stopToBuses := make(map[int][]int)
    for bus, route := range routes {
        for _, stop := range route {
            stopToBuses[stop] = append(stopToBuses[stop], bus)
        }
    }

    // Use BFS to find the shortest path
    queue := []int{source}
    visitedStops := make(map[int]bool)
    visitedBuses := make(map[int]bool)
    busesTaken := 0

    for len(queue) > 0 {
        size := len(queue)
        for i := 0; i < size; i++ {
            currStop := queue[0]
            queue = queue[1:]
            visitedStops[currStop] = true

            if currStop == target {
                return busesTaken
            }

            // Get all buses that stop at the current stop
            for _, bus := range stopToBuses[currStop] {
                if visitedBuses[bus] {
                    continue
                }
                visitedBuses[bus] = true

                // Add all stops of this bus to the queue
                for _, stop := range routes[bus] {
                    if !visitedStops[stop] {
                        queue = append(queue, stop)
                    }
                }
            }
        }
        busesTaken++
    }

    return -1
}