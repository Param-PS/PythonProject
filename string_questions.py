name = "safdsajnfdsanfdsasjdbfsjdfdsnmsbfsabfdsa22134456666!!@#"
se = set(name)
# print(s)
for i in se:
    cnt = name.count(i)
    if cnt == 1:
        print(i, "is a unique")
    else:
        print(i, "count is", cnt, "and it is not unique")
