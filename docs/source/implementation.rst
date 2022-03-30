:octicon:`code` Implementation
==============================



:octicon:`project` Project Structure
------------------------------------




:octicon:`file` Data
--------------------



:octicon:`device-camera-video` Embed OpenCV stream into UI
----------------------------------------------------------



:octicon:`file-binary` Compilation
----------------------------------

Using python as the main language for the application development poses a set of difficulties
when trying to create a distributable version of it. Even though Python is an interpreted
language, we have managed to create a set of executable versions of our application for different platforms.
This section will describe our compilation procedure, its advantages and limitations.

When it comes to compiling python to an executable, the standard approach is to package the python
interpreter along side with the source code and compress all of it to an executable. The mentioned
process is called "freezing", which results in a pretty reliable package yet comes with some drawbacks:

#. No code optimisation during compilation stage.

#. Long startup times due to code decompression (especially significant for large codebases).

#. Poor app efficiency over all.

There exists an alternative approach to "freezing" python code, which is to translate python to a compiled language
like C, and then compile the resultant C code. One of the tools that allows to do that is `Nuitka <https://nuitka.net/index.html>`. There are a couple of advantages that we get from using it.

#. The resultant executable is faster than running the code with a python interpreter.

#. The code is optimised during compilation time.

#. Solves the issue of long start up times, since there is nothing to decompress.


The only issue here is the compilation time. It takes around 20 minutes to compile our codebase to an executable.
This is an unfavourable constraint,


Dependencies:

python3-devel
