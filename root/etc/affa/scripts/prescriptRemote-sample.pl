#!/usr/bin/perl -w

use strict;

(my $hostname, my $job) = @ARGV;

# output is written to the log
print "preJobCommandRemote script prescriptRemote-sample.pl\n";
print "hostname=$hostname\n";
print "job=$job\n";
system("ls -l /var");

exit 0;
