# Layout

API para geração de layouts padronizados em formatos PDF e imagem.

## Setup

```bash
python -m pip install --upgrade pip
python -m pip install pip-tools
pip-compile --strip-extras
pip install -r requirements-dev.txt
```

## Observações úteis

```bash
# font = utils.get_font('MYRIADPRO-BOLD.OTF')
# draw.text((20, 70), pid, font=ImageFont.truetype(font))
# https://stackoverflow.com/questions/41405632/draw-a-rectangle-and-a-text-in-it-using-pil
# https://stackoverflow.com/questions/34255938/is-there-a-way-to-specify-the-width-of-a-rectangle-in-pil
# https://stackoverflow.com/questions/359706/how-do-you-draw-transparent-polygons-with-python
```
