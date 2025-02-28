# Release checklist

- [ ] Get `main` to the appropriate code release state.
      [GitHub Actions](https://github.com/termcolor/termcolor/actions) should be running
      cleanly for all merges to `main`.
      [![GitHub Actions status](https://github.com/termcolor/termcolor/workflows/Test/badge.svg)](https://github.com/termcolor/termcolor/actions)

- [ ] Edit release draft, adjust text if needed:
      https://github.com/termcolor/termcolor/releases

- [ ] Check next tag is correct, amend if needed

- [ ] Publish release

- [ ] Check the tagged
      [GitHub Actions build](https://github.com/termcolor/termcolor/actions/workflows/deploy.yml)
      has deployed to [PyPI](https://pypi.org/project/termcolor/#history)

- [ ] Check installation:

```bash
pip3 uninstall -y termcolor && pip3 install -U termcolor && python -c "from termcolor import cprint; cprint('done', 'green')"
```
