| Issue                     | Type   | Line(s) | Description                                      | Fix Approach |
|---------------------------|--------|---------|--------------------------------------------------|--------------|
| Mutable default argument  | Bug    | 7       | logs=[] shared across calls                    | logs=None, init inside |
| Broad except:           | Bug    | 16-20   | Catches all exceptions                           | Specific exceptions |
| No input validation       | Bug    | 7,11    | Accepts any type                                 | isinstance checks |
| eval() usage            | Security| 48      | Code injection risk                              | *Removed* |
| Insecure file I/O         | Security| 25,30   | No context manager                               | with open() + handling |
| Old % formatting        | Style  | 9       | % operator                                     | f-strings |
| Missing docstrings        | Style  | All     | No function docs                                 | Added docstrings |
| Global variables          | Design | 4       | stock_data global                              | Class encapsulation |
| Unused import (logging) | Warning| 2       | Imported but never used                          | Removed |
| Line too long (E501)    | Style  | many    | >79 characters                                   | Broke lines |
| Blank line at EOF (W391)| Style  | EOF     | Extra blank line                                 | One newline only |

## Reflection

1. *Easiest*: style fixes (f-strings, line breaks).  
   *Hardest*: removing eval() and redesigning validation logic.

2. *False positives?* None – every warning pointed to a real improvement.

3. *Workflow integration*  
   * pre-commit hook (flake8, bandit, pylint)  
   * GitHub Actions CI step that fails if any tool reports errors  
   * VS Code extensions for live feedback

4. *Improvements*  
   * *Security* – no eval, safe file handling  
   * *Robustness* – full input validation + logging  
   * *Readability* – docstrings, f-strings, class design  
   * *PEP-8* – *0 Flake8 warnings*

---