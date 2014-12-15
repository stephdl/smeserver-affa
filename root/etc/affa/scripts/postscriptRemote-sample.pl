#!/usr/bin/perl -w

use strict;

(my $hostname, my $job) = @ARGV;

# output is written to the log
print "postJobCommandRemote script postscriptRemote-sample.pl\n";
print "hostname=$hostname\n";
print "job=$job\n";
system("df");

exit 0;
