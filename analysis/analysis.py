"""Revenue bridge and pricing scenarios. Run from repo root: python analysis/analysis.py"""
import pandas as pd, matplotlib.pyplot as plt
m = pd.read_csv("data/pvr_metrics.csv").set_index("metric")
f0, f1 = m.loc["footfalls_mn", ["q4_fy25", "q4_fy26"]]
a0, a1 = m.loc["atp_rs", ["q4_fy25", "q4_fy26"]]
s0, s1 = m.loc["sph_rs", ["q4_fy25", "q4_fy26"]]
foot, atp, sph = (a * 0 + v for a, v in [(0, (f1 - f0) * (a0 + s0)), (0, (a1 - a0) * f1), (0, (s1 - s0) * f1)])
total = foot + atp + sph
assert abs(total - (f1 * (a1 + s1) - f0 * (a0 + s0))) < 1e-6
print(f"Bridge (Rs mn): footfall {foot:.0f}, ATP {atp:.0f}, SPH {sph:.0f}; price+spend share {(atp+sph)/total:.1%}")
# scenarios (FY26 base). ASSUMPTIONS below are NOT company data.
F, ATP, SPH = m.loc["footfalls_mn", "fy26"], m.loc["atp_rs", "fy26"], m.loc["sph_rs", "fy26"]
nb = m.loc["box_office_rev_rs_cr", "q4_fy26"] / (f1 * a1 / 10)      # net realisation, box office
nf = m.loc["fnb_rev_rs_cr", "q4_fy26"] / (f1 * s1 / 10)            # net realisation, F&B
DIST, COGS, DATP, DFOOT, DSPH, GFOOT = 0.45, 0.30, 10, -0.03, 0.08, 0.03
def contrib(foot, atp, sph): return foot * (atp * nb * (1 - DIST) + sph * nf * (1 - COGS)) / 10
base = contrib(F, ATP, SPH)
res = {"A. ATP +Rs10, footfalls -3%": contrib(F * (1 + DFOOT), ATP + DATP, SPH) - base,
       "B. F&B spend +8%": contrib(F, ATP, SPH * (1 + DSPH)) - base,
       "C. Footfalls +3%": contrib(F * (1 + GFOOT), ATP, SPH) - base}
for k, v in res.items(): print(f"{k}: {v:+.0f} Rs Cr")
be = (ATP * nb * (1 - DIST) + SPH * nf * (1 - COGS)) / ((ATP + DATP) * nb * (1 - DIST) + SPH * nf * (1 - COGS)) - 1
print(f"Break-even footfall change for +Rs10 ATP: {be:.2%}")
fig, ax = plt.subplots(figsize=(7, 4.5))
ax.bar(["Footfalls", "Ticket price", "F&B spend"], [foot, atp, sph], color=["#8A93A5", "#2A5C9E", "#2A5C9E"])
ax.set_ylabel("Rs mn"); ax.set_title("Q4 FY26 change in gross ticket + F&B value, by driver"); plt.tight_layout()
plt.savefig("charts/revenue_bridge.png", dpi=150)
fig, ax = plt.subplots(figsize=(8, 4.5))
ax.barh(list(res), list(res.values()), color=["#B5481B" if v < 0 else "#2A5C9E" for v in res.values()])
ax.set_xlabel("Change in contribution, Rs Cr (assumption-driven)"); ax.set_title("Pricing scenarios, FY26 base"); ax.invert_yaxis()
plt.tight_layout(); plt.savefig("charts/scenarios.png", dpi=150)
