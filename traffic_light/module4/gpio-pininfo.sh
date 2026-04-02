#!/bin/bash
# This script format the output of the `gpio readall` command to show the status
# of a specific BCM pin. It takes the BCM pin number as an argument and displays
# the corresponding wPi pin, physical pin, name, mode, and value.
#
# Usage:
#   ./gpio-pininfo.sh <BCM pin>
#
# Example:
#   ./gpio-pininfo.sh 17
#
# Note that this script should be executable on the system
# You can make it executable with:
#   chmod +x gpio-pininfo.sh

PIN=$1

if [ -z "$PIN" ]; then
  echo "Usage: $0 <BCM pin>"
  exit 1
fi

gpio readall | awk -F'|' -v pin="$PIN" '

function trim(s) {
  gsub(/^[ \t]+|[ \t]+$/, "", s)
  return s
}

# Skip non-data lines
$0 ~ /^\+/ { next }
trim($2) == "BCM" {
  next
}

# Skip lines that do not match the pin
(trim($2) != pin && trim($14) != pin) {
  next
}

{
  # Determine if the match is on the left (BCM) or right (BCM) column
  parse_left = trim($2) == pin ? "1" : "0"

  # Extract fields based on which side matched
  bcm   = parse_left == "1" ? trim($2) : trim($14)
  wpi   = parse_left == "1" ? trim($3) : trim($13)
  name  = parse_left == "1" ? trim($4) : trim($12)
  mode  = parse_left == "1" ? trim($5) : trim($11)
  val   = parse_left == "1" ? trim($6) : trim($10)
  phys  = parse_left == "1" ? trim($7) : trim($9)

  # Print the diagnostic information
  printf "\nGPIO Diagnostic\n"
  printf "---------------------------\n"
  printf "BCM Pin:       %s\n", bcm
  printf "wPi Pin:       %s\n", wpi
  printf "Physical Pin:  %s\n", phys
  printf "Name:          %s\n", name
  printf "Mode:          %s\n", mode
  printf "Value:         %s\n", (val == "1" ? "HIGH (1)" : (val == "0" ? "LOW (0)" : val))
  found = 1
  exit
}

END {
  if (!found) {
    printf "GPIO %s not found\n", pin
  }
}
'