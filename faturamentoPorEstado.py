sp     = 67.83643
rj     = 36.67866
mg     = 29.22988
es     = 27.16548
outros = 19.84953

soma = (sp + rj + mg + es + outros)
sp = ((sp/soma)*100)
rj = ((rj/soma)*100)
mg = ((mg/soma)*100)
es = ((es/soma)*100)
outros = ((outros/soma)*100)
print(f"O percentual de representação do estado de São Paulo foi {sp:.2f}%")
print(f"O percentual de representação do estado do Rio de Janeiro foi {rj:.2f}%")
print(f"O percentual de representação do estado de Minas Gerais foi {mg:.2f}%")
print(f"O percentual de representação do estado do Espírito Santo foi {es:.2f}%")
print(f"O percentual de representação dos outros estados foi {outros:.2f}%")
