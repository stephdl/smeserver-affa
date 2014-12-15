#!/usr/bin/perl -w

use strict;

(my $hostname, my $job, my $sshCmd) = @ARGV;

# output is written to the log
print "postJobCommand script postscript-sample.pl\n";
print "hostname=$hostname\n";
print "job=$job\n";
print "sshCmd=$sshCmd\n";
system("$sshCmd $hostname df");

exit 0;
