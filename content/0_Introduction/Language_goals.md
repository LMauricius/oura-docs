# Language goals

Oura is developed with love towards both the programmer and the end-user. Here is the list of goals that the author believes will help make the language better.

- **Fast execution** - Oura is designed with optimizability in mind. Compiled code should run as fast as humanly possible.
- **Portability** - Compilable for all systems and (mostly) platform-agnostic behavior. For real this time.
- **Safety** - Fast or powerful code shouldn't be gatekept as a harder or less safe skill. Accessibility and speed/power aren't mutually exclusive.
- **Obvious semantics** - While function overloading is mostly OK, language features and symbols should *never* be.
- **Reusability** - Language features should rarely be context-dependant. The programmers can mix-and-match them as they see fit
- **Backwards compatibility** - The module system should ensure old versions of a library can be replaced with a new one with as little pain as possible.
- **API implies the ABI** - The binary compatibility should be evident from the explicit specification in the API and the platform/binary file format used
- **Interoperability with other languages** - Oura shouldn't require a huge ecosystem built specifically for it, but should be an interface to language-agnostic specifications.
- **Reduce the amount of work** - Even if you consider the programmer a wizard, their work and time aren't zero-cost. We don't expect the programmers to repeat work that can be done once and then shared.