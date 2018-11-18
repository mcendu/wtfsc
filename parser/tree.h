#pragma once

#include <stdio.h>
/*
 * A simple implementation of the tree
 * structure.
 */
struct tree {
	void *car;
	/* char *car; */
	/* struct tree **car; */
	int chno;
};

/* Convenient typecasts */
#define as_t(a) ((struct tree **)a)
#define as_s(a) ((char *)a)

/*
 * Create tree from a string.
 */
extern struct tree mknode(const char *str);
/*
 * Connect c entries to a root node.
 */
extern struct tree connect(int c, /* struct tree */...);
/*
 * Serialize tree into s-expression.
 */
extern int sexps(FILE *f, struct tree t);
/*
 * Destructor
 */
extern void destroy(struct tree t);
