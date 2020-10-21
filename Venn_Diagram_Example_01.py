import matplotlib_venn as ven
import matplotlib.pyplot as plt

plt.rc("font", family="chosunilboNM", size=13)
subsets = (7, 7, 1, 7, 1, 1, 1)
v = ven.venn3(subsets=subsets, set_labels=('통근시간', '크기', '고정지출비율'))
ven.venn3_circles(subsets=subsets, linewidth=2.0)

v.get_label_by_id('100').set_text("30-45분이내")
v.get_label_by_id('010').set_text("25-30m2")
v.get_label_by_id('001').set_text("월실수령액의\n25%-30%")
v.get_label_by_id('110').set_text("가깝고\n큰집")
v.get_label_by_id('101').set_text("가깝고\n싼집")
v.get_label_by_id('011').set_text("크고\n싼집")
v.get_label_by_id('111').set_text("허위매물")
plt.title("도쿄에서 집구하기 세 조건")
plt.tight_layout()
plt.savefig("Venn_Diagram.jpeg", dpi=900)