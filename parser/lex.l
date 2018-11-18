%{
#include <stdlib.h>
#include <math.h>
#include <errno.h>

#include "y.tab.h"
%}

INT	[0-9]+
FRAC	\.{INT}
SCI	[eE][+-]{INT}
NUM	{INT}{FRAC}?{SCI}?

/* Special values */
INF	(?i:(inf)(inity)?)
NAN	(?i:nan)

/* Identifier */
ID	[a-z_][a-z0-9_]*

WHITE	[ \t\n\r]
%%

{NUM}	yylval = yytext; return NUM;
{ID}	yylval = yytext; return ID;
{WHITE}
