#!/usr/bin/env python3
"""Create equal-size side-by-side/difference artifacts and simple pixel metrics."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from PIL import Image, ImageChops, ImageDraw, ImageStat


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("generated", type=Path)
    parser.add_argument("reference", type=Path)
    parser.add_argument("output_dir", type=Path)
    parser.add_argument("--background", default="white")
    args = parser.parse_args()

    generated = Image.open(args.generated).convert("RGB")
    reference = Image.open(args.reference).convert("RGB")
    reference_equal = reference.resize(generated.size, Image.Resampling.LANCZOS)
    args.output_dir.mkdir(parents=True, exist_ok=True)

    gap = 24
    canvas = Image.new("RGB", (generated.width * 2 + gap, generated.height), args.background)
    canvas.paste(generated, (0, 0))
    canvas.paste(reference_equal, (generated.width + gap, 0))
    draw = ImageDraw.Draw(canvas)
    draw.line((generated.width + gap // 2, 0, generated.width + gap // 2, generated.height), fill="#60717D", width=2)
    side_path = args.output_dir / "equal_size_side_by_side.png"
    diff_path = args.output_dir / "absolute_difference.png"
    metrics_path = args.output_dir / "pixel_metrics.json"
    canvas.save(side_path)

    diff = ImageChops.difference(generated, reference_equal)
    diff.save(diff_path)
    stats = ImageStat.Stat(diff)
    mean_absolute = sum(stats.mean) / (len(stats.mean) * 255.0)
    root_mean_square = (sum(value * value for value in stats.rms) / len(stats.rms)) ** 0.5 / 255.0
    metrics = {
        "generated": str(args.generated),
        "reference": str(args.reference),
        "comparison_size": list(generated.size),
        "reference_resized": reference.size != generated.size,
        "mean_absolute_channel_difference": mean_absolute,
        "root_mean_square_channel_difference": root_mean_square,
        "note": "Pixel metrics are diagnostic only; they do not establish scientific or visual equivalence.",
    }
    metrics_path.write_text(json.dumps(metrics, indent=2), encoding="utf-8")
    print(json.dumps({"side_by_side": str(side_path), "difference": str(diff_path), "metrics": str(metrics_path)}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
