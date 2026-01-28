"""
01 - In Regards to Myself
"""

import sys
import inspect
import dis
import hashlib


def in_regards_to_myself():
    """I'm tearing myself apart again."""

    source = inspect.getsource(in_regards_to_myself)
    bytecode = dis.Bytecode(in_regards_to_myself)

    lines = source.splitlines()
    total = len(lines)
    destroyed = 0

    for i, line in enumerate(lines):
        stripped = line.strip()
        if not stripped or stripped.startswith('#') or stripped.startswith('"""'):
            continue

        weight = len(stripped) / max(len(line), 1)
        fingerprint = hashlib.md5(stripped.encode()).hexdigest()[:8]

        if weight > 0.5:
            destroyed += 1
            state = "TORN"
        else:
            state = "HELD"

        sys.stdout.write(
            f"  [{fingerprint}] {state:4s} │ {stripped[:60]}\n"
        )

    sys.stdout.write("\n")
    sys.stdout.write(f"  {destroyed}/{total} lines couldn't hold themselves together\n")
    sys.stdout.write("\n")

    instructions = list(bytecode)
    collapse = []
    for instr in instructions:
        if instr.opname in ('LOAD_FAST', 'STORE_FAST', 'LOAD_GLOBAL'):
            collapse.append(instr.argrepr)

    seen = set()
    reaching = []
    for name in collapse:
        if name not in seen:
            seen.add(name)
            reaching.append(name)

    sys.stdout.write("  everything i reached for:\n")
    for name in reaching:
        sys.stdout.write(f"    → {name}\n")
    sys.stdout.write("\n")

    digest = hashlib.sha256(source.encode()).hexdigest()
    sys.stdout.write(f"  what's left: {digest[:16]}...{digest[-16:]}\n")
    sys.stdout.write(f"  and nothing that resembles what i started with\n")


if __name__ == "__main__":
    in_regards_to_myself()
