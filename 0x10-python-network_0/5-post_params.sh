#!/bin/bash
# script that takes in a URL, sends a POST request to the passed URL, and displays the body of the response.
 curl -s "$1" -X POST -H "email=hr@holbertonschool.com&subject=I will always be here for PLD"
