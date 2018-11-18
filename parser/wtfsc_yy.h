#pragma once

#include <stdlib.h>

#include "tree.h"

/* Routines required by yacc. */
extern void yyerror(const char *);
extern int yylex(void);

/* Routines that can come into handy. */
extern int __est (const char *format, ...);
#define output
#define chksn(a) snprintf
