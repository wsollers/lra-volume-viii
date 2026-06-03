# Volume Bibliography

This directory is owned by $repo.

The standalone volume build uses:

- $bib

Add entries needed by this volume to that shard, then run:

`powershell
python scripts/check_bibliography.py --bib-dir bibliography
`

The volume sync workflow copies this shard into Learning-Real-Analysis/bibliography/.
Do not add unrelated volume bibliography files here.