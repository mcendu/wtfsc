#include <stdarg.h>
#include <stdio.h>
#include <stdlib.h>

#include "tree.h"

struct tree
mknode(const char *str)
{
	struct tree ret;
	ret.chno = 0;
	ret.car = (void *)str;
	return ret;
}

struct tree
connect(int c, ...)
{
	va_list ap;
	struct tree ret, buf;
	ret.chno = c;
	ret.car = malloc(c * sizeof(struct tree *));
	va_start(ap, c);
	for (int i=0; i<c; i++) {
		buf = va_arg(ap, struct tree);
		as_t(ret.car)[i] = &buf;
	}
	va_end(ap);
}

int
sexps(FILE* f, struct tree t)
{
	int ret;
	if (t.chno == 0)
		ret += fprintf(f, "%s", as_s(t.car));
	else {
		ret += fputc('(', f);
		for (int i=0; i<t.chno; i++) {
			ret += sexps(f, as_t(t.car)[i][0]);
			fputc(i==t.chno-1 ? ')' : ' ', f);
			ret++;
		}
	}
	return ret;
}

void
destroy(struct tree t)
{
	if (t.chno > 0) {
		for (int i=0; i<t.chno; i++) {
			destroy(as_t(t.car)[i][0]);
		}
		free(t.car);
	}
}

#ifdef TEST
int
main
();
#endif
