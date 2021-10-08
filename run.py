from HR.HR import HR

with HR() as bot:
    bot.get_first_page()
    bot.job_category()
    bot.click_advanced_search()
    bot.select_type()
    bot.select_excerience(4)
    bot.select_place("თბილისი")
    bot.select_salary_range()
    bot.select_published_date()
    bot.click_search_btn()
