package utils

import (
	"fmt"
	"time"
)

const (
	colres  = "\033[0m"
	colred  = "\033[31m"
	colgrn  = "\033[32m"
	colyel  = "\033[33m"
	colcyan = "\033[36m"
)

func Evnt() string {
	return "[" + colcyan + "~" + colres + "]"
}

func Err() string {
	return "[" + colred + "!" + colres + "]"
}

func Time() string {
	now := time.Now()
	timee := now.Format("15:04:05")
	nowtime := fmt.Sprintf("%s[%s%s%s]%s", colyel, colres, timee, colyel, colres)
	return nowtime
}
