package main

import (
	"bufio"
	"bullsploit/utils"
	"fmt"
	"net"
	"os"
	"strconv"
	"sync"
	"time"
)

const (
	colres  = "\033[0m"
	colred  = "\033[31m"
	colgrn  = "\033[32m"
	colyel  = "\033[33m"
	colcyan = "\033[36m"
)

func worker(ip string, ports <-chan int, wg *sync.WaitGroup, writer *bufio.Writer, mutex *sync.Mutex) {
	defer wg.Done()
	timeout := 400 * time.Millisecond
	for port := range ports {
		address := net.JoinHostPort(ip, strconv.Itoa(port))
		conn, err := net.DialTimeout("tcp", address, timeout)
		if err == nil {
			conn.Close()
			mutex.Lock()
			fmt.Fprintf(writer, "%s Port %d is open\n", utils.Time(), port)
			writer.Flush()
			mutex.Unlock()
		}

	}
}

func main() {
	if len(os.Args) < 5 {
		fmt.Printf("%s Error missing arguments\n", utils.Err())
		os.Exit(1)

	}
	ip := os.Args[1]
	sport, _ := strconv.Atoi(os.Args[2])
	eport, _ := strconv.Atoi(os.Args[3])
	threads, _ := strconv.Atoi(os.Args[4])
	fmt.Printf(" %s Scanning start %s%s%s in %d threads...\n", utils.Evnt(), colgrn, ip, colres, threads)
	startTime := time.Now()
	ports := make(chan int, threads*2)
	var wg sync.WaitGroup
	var mutex sync.Mutex
	writer := bufio.NewWriter(os.Stdout)
	for i := 0; i < threads; i++ {
		wg.Add(1)
		go worker(ip, ports, &wg, writer, &mutex)
	}
	for port := sport; port <= eport; port++ {
		ports <- port
	}
	close(ports)
	wg.Wait()
	duration := time.Since(startTime).Round(time.Millisecond)
	fmt.Fprintf(writer, "%s Scan successfully finished %v\n", utils.Evnt(), duration)
	writer.Flush()

}
