for n in range(5):
    yield n  # Noncompliant: yield outside a function

try:
    ...
except SystemExit:
    pass  # Noncompliant: SystemExit swallowed

try:
    ...
except BaseException:
    pass  # Noncompliant: catches SystemExit, doesn't re‑raise

try:
    ...
except:
    pass  # Noncompliant: overly broad exception, should specify
