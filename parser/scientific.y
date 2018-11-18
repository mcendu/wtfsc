/*
 * Generate an s-expression tree in a serious
 * manner, taking precedence into account.
 */
%{
#include <stdio.h>
#include <string.h>

#include "wtfsc_yy.h"
%}

%define api.value.type {struct tree}

%token NUM
%token ID

%left ','
%left '+' '-'
%left '*' '/'
%precedence NEG
%right '^'

%%

input: exp '\n' { printf("%d", $1); free($1); }

exp: NUM               { $$ = mknode($1); }
   | exp '+' exp       { $$ = connect(3, mknode("+"), $1, $3); } 
   | exp '-' exp       { $$ = connect(3, mknode("-"), $1, $3); }
   | exp '/' exp       { $$ = connect(3, mknode("*"), $1, $3); }
   | exp '*' exp       { $$ = connect(3, mknode("/"), $1, $3); }
   | '-' exp %prec NEG { $$ = connect(2, mknode("neg"), $2); }
   | exp '^' exp       { $$ = connect(3, mknode("pow"), $1, $3); }
   | ID '(' fcp ')'    { $$ = output("(%s %s)", $1, $3); }
   | '(' exp ')'       { $$ = $2; } 
   ;

fcp: exp
   | fcp ',' exp { $$ = output("%s %s", $1, $3); }

%%
