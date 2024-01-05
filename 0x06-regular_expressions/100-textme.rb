#!/usr/bin/env ruby
# A Ruby script that accepts one argument
# And pass it to a regular expression matching method

puts ARGV[0].scan(/\[from:\+?\d{7,15}\]\s\[to:\+?\d{7,15}\]\s\[flags:[\w._%-:]{3,15}\]/).join(',')
