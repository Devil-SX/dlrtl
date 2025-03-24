import dlrtl
import os
import torch
from pathlib import Path

if __name__ == "__main__":
    dir_path = Path("./temp")
    x = torch.arange(0, 224 * 3).reshape(224, 3).to(torch.bfloat16)

    hlist = dlrtl.Hlist.from_tensor(x)
    hlist.to_binfile(dir_path / "dump.bin")
    hlist.to_memhexfile(dir_path / "dump.mem")

    y = dlrtl.Hlist.from_binfile(dir_path / "dump.bin", 3, torch.bfloat16).to_tensor()
    print(y)
    dlrtl.compare(x, y)