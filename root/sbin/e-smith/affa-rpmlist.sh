#!/bin/bash
#
# This script is part of the smeserver-affa package

# Copyright (C) 2008 Michael Weinberger, neddix Stuttgart, Germany
#
/usr/bin/yum --noplugins list installed\
|/bin/grep "installed *$"\
|/bin/sed -e 's/\./ /'\
|/bin/awk '{printf "%s %s\n", $1,$3}'
