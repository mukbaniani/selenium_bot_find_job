from HR.hr import HR


with HR() as bot:
    bot.get_first_page()
    bot.job_category("ინფორმაციული ტექნოლოგიები")
    bot.click_advanced_search()
    bot.select_type("ვაკანსია")
    bot.select_excerience("გამოცდილების გარეშე")
    bot.select_place("თბილისი")
    bot.select_salary_range()
    bot.select_published_date("დღეს")
    bot.click_search_btn()
