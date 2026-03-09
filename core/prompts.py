def research_prompt(persona_prompt, company, information):

    return f"""
{persona_prompt}

You are an expert business research analyst.

Generate a professional company research report using the information below.

Company: {company}

Information Sources:
{information}

Provide the analysis using the following structure:

1. Company Overview
- Brief history
- Mission and business focus

2. Products and Services
- Main offerings
- Key technologies

3. Market Position
- Industry role
- Competitive advantages

4. Competitors
- Major companies competing in this market

5. Recent Developments
- News, partnerships, product launches

6. Opportunities
- Potential growth areas

7. Strategic Account Plan
- Business opportunities
- Potential partnerships
- Strategic recommendations

Write clearly and professionally.
"""

def comparison_prompt(company1, company2, info1, info2):

    return f"""
You are a strategic business analyst.

Compare the following two companies.

Company 1: {company1}
Information:
{info1}

Company 2: {company2}
Information:
{info2}

Provide a structured comparison:

1. Company Overview
2. Key Products and Technologies
3. Market Position
4. Competitive Advantages
5. Growth Opportunities
6. Strategic Insights

Be clear and analytical.
"""