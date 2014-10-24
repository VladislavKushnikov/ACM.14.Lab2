#!C:/Perl64/bin/Perl.exe

use strict;
use CGI;
use CGI::Carp qw(fatalsToBrowser);

use lab2::st01::st01;
use lab2::st12::st12;

my @MODULES = 
(
	\&ST01::st01,
	\&ST12::st12
);

my @NAMES = 
(
	"Student 01",
	"Kushnikov V."
);

Lab2Main();

sub menu
{
	my ($q, $global) = @_;
	print $q->header();
	my $i = 0;
	print "<pre>\n------------------------------\n";
	foreach my $s(@NAMES)
	{
		$i++;
		print "<a href=\"$global->{selfurl}?student=$i\">$i. $s</a>\n";
	}
	print "------------------------------</pre>";
}

sub Lab2Main
{
	my $q = new CGI;
	my $st = 0+$q->param('student');
	my $global = {selfurl => $ENV{SCRIPT_NAME}, student => $st};
	if($st && defined $MODULES[$st-1])
	{
		$MODULES[$st-1]->($q, $global);
	}
	else
	{
		menu($q, $global);
	}
}
