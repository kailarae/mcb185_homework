gunzip -c ../MCB185/data/dictionary.gz | grep -v "[qwetyupsdfghjklxvbm]" | grep -E ".{4,}" | grep "r"
