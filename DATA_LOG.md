# Data log

## Collection
PVR INOX Q4 FY26 results (11 May 2026) as reported by Business Standard, Kotak Neo, DSIJ and Outlook Business. Each row in `data/pvr_metrics.csv` carries a note on its source.

## Cleaning and judgement calls
1. **Q4 FY25 ATP and SPH** were not reported directly in the sources found; they were back-calculated from the reported Q4 FY26 values and year-on-year growth (+22.4% and +32.3%). Results are rounded to whole rupees.
2. **Net realisation:** reported ATP x footfalls exceeds reported box-office revenue, so a ratio (revenue / (footfalls x ATP)) of about 84% for tickets and 94% for F&B was computed and used in the scenarios. Interpretation that ATP and SPH are quoted gross of tax is our inference, not a company statement.
3. **FY26 ATP, SPH and footfalls** (Rs 280, Rs 147, 150 million) are used as the scenario base; the Q4 net-realisation ratios are assumed to hold for the full year.
4. **Assumptions not in any disclosure** (distributor share, F&B cost of goods, price response) are stated in `analysis/analysis.py` and the Excel model and tested in sensitivities.
