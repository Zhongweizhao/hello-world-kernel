#include <linux/module.h>
#include <linux/kernel.h>
#include <linux/init.h>

#define DRIVER_AUTHOR "Zhongwei Zhao <zhongwei.zhao@uwaterloo.ca>"
#define DRIVER_DESC "A simple driver"

static int __init hello_init(void)
{
    printk(KERN_INFO "Hello world 1.\n");

    return 0;
}

static void __exit hello_exit(void)
{
    printk(KERN_INFO "Goodbye world 1.\n");
}

module_init(hello_init);
module_exit(hello_exit);

MODULE_LICENSE("GPL");
MODULE_AUTHOR(DRIVER_AUTHOR);
MODULE_DESCRIPTION(DRIVER_DESC);

