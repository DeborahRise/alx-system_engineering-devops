#!/usr/bin/env ruby
# A Ruby script that accepts one argument
# And pass it to a regular expression matching method

puts ARGV[0].scan(/hb?tn/).join
