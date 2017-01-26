
use strict;
use warnings;

open my $fh, '<', 'log.txt' or die $!;

{
    local $/ = '';

    while ( <$fh> ) {
        print if /peach/;
    }
}
