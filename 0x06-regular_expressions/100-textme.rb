#!/usr/bin/env ruby
# A Ruby script that accepts one argument
# And pass it to a regular expression matching method

puts ARGV[0].scan(/\[from:[\w.+]{7,16}\]\s\[to:[\w.+]{7,16}\]\s\[flags:[\w._%-:]{3,15}\]/).join(',')
