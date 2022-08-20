ASCIIPA-2
=========

A markup language, using a subset of ASCII, that compiles to IPA. Design goals:

- It uses no delimiters besides `()`. It does use backslashes, but only as an
  escape character for literals. It does not use `$` or `|`, on account of them
  not being found on all keyboards. It leaves single hyphens and hashes alone,
  because they are often used in glossing and sound change notation
  respectively. (Literal underscores must be typed as `__`.)
- If an ASCII character is already in IPA, or close to it (e.g. exists as a
  small capital character), then it will represent that IPA character. `E`,
  `O`, and `Z` from X-SAMPA are also present.
- Otherwise, the ASCII character or multigraph most similar visually to the
  IPA character in question will be used. For example, the clicks ǀ, ǁ, and ǂ
  are represented by `--`, `==`, and `++` respectively.
- It prefers simple, alphanumeric multigraphs to weird combinations of symbols
  or unintuitive capitalized letters. For example, ɸ, β, θ, and ð are
  represented by `ph`, `bh`, `th`, and `dh` respectively.
- If a colloquial ASCII rendering of a sound already exists, it will try to
  use that. For example, ɬ is represented by `&`, as in colloquial Inuktitut
  romanization, and ʕ is represented by `3`, as in the Arabic chat alphabet.
  
The following ASCII characters don't appear in it at all: ``/'"`[]{}$|``.

Example usage:
```python
>>> import asciipa2
>>> asciipa2.compile('dh0(:+rh)..:(13531)')
'ð̥̟̈˞ʰʼː˩˧˥˧˩'
```
