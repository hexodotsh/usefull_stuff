#!/bin/bash

# Define variables
read -p "Enter path to target file: " target_file
read -p "Enter list of IP addresses to exclude (separated by spaces): " exclude_ips_input

output_file="scoped-targets.txt"
exclude_ips=()

# Check if exclude_ips_input is a file or a list of IPs
if [[ -f "$exclude_ips_input" ]]; then
  # Read exclude file and store IPs in array
  if [[ -f "$exclude_ips_input" ]]; then
    while read -r line; do
      exclude_ips+=("$line")
    done < "$exclude_ips_input"
  else
    echo "Exclude file not found."
    exit 1
  fi
else
  # Convert input string to array
  exclude_ips=($exclude_ips_input)
fi

# Filter target file and remove excluded IPs
echo "Filtering target file..."
echo "${exclude_ips[@]}" | tr ' ' '\n' > exclude.tmp
grep -vFf exclude.tmp "$target_file" > "$output_file"
rm exclude.tmp

echo "Filtering complete. Results saved to $output_file"
