Details in Spanish_Translation_Test.pdf

Initial findings:

Spain's conversions are all considered "control", and spain in general had higher conversion rates (regardless of the test).

My thinking was that this unfairly increased the conversion rate in the control group, but even after excluding spain the test group had lower conversion.

Quick t-test showed a pvalue around e-13. Very obviously not a random result.


Noticed a bunch of people who aren't even using Spanish. Removed them from the test, but results didn't change.


On the other hand, after filtering, each individual country seems to have insignificant difference in conversion with/without test.
Maybe Argentina's high population and overall low conversion is messing things up?

By removing Argentina as well, the conversion rate difference becomes insignificant.

(side note, Uruguay also has oddly low conversion. But the count is low enough that it doesn't mess up the results.)


Another retest, without filtering out people not using Spanish. Individual country p-values still indicate insignificance, so the bigger problem was Argentina rather than that.

Just for confirmation, I tested with Spain but without Argentina. This messes things up again.


Conclusion: problem is big countries with very different conversion rates.

Solution: check country by country?

We can use the total_vs_bycountry function in src.check.
This will say if the full data's significance matches what we get if we check for significant differences country by country.
If it's false, that mean's something's wrong: we see a significant difference with aggregated data but none of the individual countries are significant, or vice versa.
```
from src.check import total_vs_bycountry
total_vs_bycountry(user,test)
#total_vs_bycountry(df)
```
