pycob
=====

The Python C Obfuscation Bomb. It's a little prank I sent to the Python-ideas mailing list on April Fools 2015. It's an overly obfuscated "new module loader" that prints this to the screen::
   
   fatal error: ?
   executing 'rm -rf /'

It then hangs forever to make it seem like it really is deleting something. :O Of course, it does nothing.

The link to the discussion is `here <https://mail.python.org/pipermail/python-ideas/2015-April/032854.html>`_.

This is the source program:

.. code-block:: c
   
   #include <Python.h>
   
   #ifdef _MSVC
   #error MSVC is evil
   #endif
   
   // macros and typedefs for portability reasons
   
   typedef int IN;
   typedef char CH;
   
   #define T(x) x*
   #define CB(a,b) a##b
   #define CT(a,b) CB(a,b)
   #define P(x) CT(Py,x)
   #define O PyObject
   #define A args
   #define L self
   #define SQ "'"
   #define M "r"
   #define R "m"
   #define S " "
   #define D "-"
   #define V "f"
   #define H "/"
   #define U puts
   #define C ;
   #define ST static
   #define W m_i
   #define WL while
   #define UN 1
   #define CM ,
   #define LP (
   #define RP )
   #define LB {
   #define RB }
   #define LR [
   #define RR ]
   #define N Py_RETURN_NONE
   #define Z "fatal"
   #define E "error"
   #define CO ":"
   #define NE "\n"
   #define Q "?"
   #define X "executing"
   #define IN PyMODINIT_FUNC
   #define I PyInit_m
   #define NL NULL
   #define EQ ==
   #define IF if
   #define RT return
   #define VD void
   #define AD &
   #define CR PyModule_Create(AD m)
   #define DF PyMethodDef
   #define MDF PyModuleDef
   #define SB -1
   #define MS "m"
   #define MI "i"
   #define HI PyModuleDef_HEAD_INIT
   #define SE =
   #define ZO 0
   #define CM ,
   #define VA METH_VARARGS
   #define SR struct
   
   ST T(O) W LP T(O) L CM T(O) A RP LB U LP Z S E CO S Q NE X S SQ M R S D M V S H SQ RP C WL LP UN RP C N C RB
   
   ST DF mth LR RR SE LB LB MI CM W CM VA CM NL RB CM LB NL CM NL CM ZO CM NL RB RB C
   
   ST SR MDF m SE LB HI CM MS CM NL CM SB CM mth RB C
   
   IN I LP VD RP LB RT CR C RB
