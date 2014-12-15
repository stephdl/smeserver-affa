#!/usr/bin/perl -w

use strict;

(my $hostname, my $job, my $sshCmd) = @ARGV;

# output is written to the log
print "preJobCommand script prescript-sample.pl\n";
print "hostname=$hostname\n";
print "job=$job\n";
print "sshCmd=$sshCmd\n";
system("$sshCmd $hostname ls -l /var");

exit 0;
