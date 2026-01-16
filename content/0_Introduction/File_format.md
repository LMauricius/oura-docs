# File format

Here are described the file formats, folder structures and conventions used in Oura.

## File naming

The file names must start with a letter and can contain leters, digits and underscores. Double underscores are forbidden. If the file has multiple extensions (separated by multiple dots), all but the last extension will be ignored.

## File extensions

| File type             | Extension |
| --------------------- | --------- |
| Source file           | `oura`    |
| Module interface file | `orai`    |

## Compiler

A compiler is a program that reads code written in a programming language of choice,
understands it, and usually creates a binary file understood by the machine.

To run Oura code, you need to install an Oura compiler.

### Source files
The source files are the ones containing Oura code. Multiple source files are combined into a single *module* if they are stored in a single directory. Oura module directories should also have an extension `.oura`.

Before running or using Oura programs modules get compiled into a *binary file*, which can be either an *executable* or a *library*. If the binary we are compiling is a library meant to be used by other developers, the source files can also produce *module interface files* which simplify the loading of library symbols without revealing the full source code to others.

## Text file format

Source files should always be saved using the `UTF-8` encoding. Other formats might not be recognized or read properly by the compiler. Most modern text editors use `UTF-8` by default.