Details in Spanish_Translation_Test.pdf

# Translation AB test?
## Problem
A website originally had a Spaniard do the translation for all Spanish speakers.
The website wanted to test having native translators for Spanish speakers in other countries (Argentina, Mexico, etc)
However, this appears to lower conversion.

## Conclusion
This conclusion is incorrect; actually, there appears to be no significant difference in conversion between the Spaniard's and the native translators.

The apparently lower conversion has two specific causes:
1. All cases in Spain were classified as part of the control group. Since Spain's conversion rate is generally higher,
2. Argentina has a very low general conversion rate in general, and most users in Argentina were shown the test translation. As a result, when aggregating data together, Argentina disproportionately lowered the average conversion rate of the test group.

If we look country by country, we see that there is no country where the native translators caused a significant change in conversion rate.

On a side note, the original data includes plenty of users using the English or other versions of the website. We should not include them when testing the effect of different Spanish translations, but this was not the main issue this time. 

Also, Uruguay has the same issue as Argentina: low general conversion rates with more test than control. Uruguay did not have enough users to affect the aggregated result, and it's solved the same way: check country by country. 

## Solution
As a quick check if we encounter this issue in the future, we can use the total_vs_bycountry function in src.check.
This will say if the full data's significance matches what we get if we check for significant differences country by country.

If it returns false, that mean's something's wrong: we see a significant difference with aggregated data but none of the individual countries are significant, or vice versa.
```
from src.check import total_vs_bycountry
total_vs_bycountry(user,test)
#total_vs_bycountry(df)
```


## Notes from data exploration

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
