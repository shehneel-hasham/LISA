package main

import (
	"encoding/csv"
	"fmt"
	"log"
	"os"
	"regexp"
	"strconv"
	"strings"

	"github.com/gocolly/colly"
)

func main() {
	// exporting to csv
	filename := "talk_content.csv"
	file, err := os.Create(filename)
	if err != nil {
		log.Fatalf("Something went wrong, the error is: %q", err)
		return
	}
	defer file.Close()

	writer := csv.NewWriter(file)
	defer writer.Flush()

	// actual colly collector, making sure that all links are unique
	seenLinks := make(map[string]struct{})
	c := colly.NewCollector(
		colly.AllowedDomains("ted.com", "www.ted.com"),
	)
	transcriptScraper := c.Clone()
	// Find and visit all links
	c.OnHTML("a[href]", func(e *colly.HTMLElement) {
		href := e.Attr("href")
		if strings.HasPrefix(href, "/talks/") {
			if _, ok := seenLinks[href]; !ok {
				seenLinks[href] = struct{}{}
				transcriptScraper.Visit(fmt.Sprintf("%s/transcript", e.Request.AbsoluteURL(e.Attr("href"))))
			}
		}
	})
	// a little data cleaning for the transcript
	re := regexp.MustCompile(`[\s\p{Zs}]{2,}`)
	re1 := regexp.MustCompile(`\n`)
	var records []string
	transcriptScraper.OnHTML("div[class=Grid]", func(e *colly.HTMLElement) {
		if s := strings.TrimSpace(e.Text); s != "" {
			s = re1.ReplaceAllLiteralString(s, " ")
			s = re.ReplaceAllString(s, " ")
			records = strings.Split(s, "/n")
			writer.Write(records)
		}
	})
	// printing what URLs are visited to terminal
	transcriptScraper.OnRequest(func(r *colly.Request) {
		fmt.Println("Visiting", r.URL)
	})
	// generating all the URLs that I want to visit, ie the tech pages on tedx
	techpageURLs := []string{}
	techpageURLs = append(techpageURLs, "https://www.ted.com/talks?sort=newest&topics%5B%5D=Technology")
	for i := 2; i < 34; i++ {
		techpageURLs = append(techpageURLs, "https://www.ted.com/talks?page="+strconv.Itoa(i)+"&sort=newest&topics%5B%5D=Technology")
	}
	// telling colly to visit all the tech pages that I generated
	for i := 0; i < len(techpageURLs); i++ {
		c.Visit(techpageURLs[i])
	}
}
