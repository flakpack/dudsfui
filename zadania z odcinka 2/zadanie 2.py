#.Stworz liste ktora bedzie zawierac 10 słow,
# nastpnie stworz liste zawierajaca tylko slowa majace wiecej niz 5 liter

slowa = ('elo','siemanko','hejkanaklejka','witam','spoczko','hej','dziendobry','dobrywieczor','czesc','siema')
liter5 = [slowo for slowo in slowa if len(slowo) > 5]
print(liter5)
