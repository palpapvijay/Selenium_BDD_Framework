from selenium import webdriver

# Before and After All feature
def before_all(context):
    path = "./Drivers/chromedriver.exe"
    context.driver = webdriver.Chrome(executable_path=path)


def after_all(context):
    context.driver.close()

# Before and After for every All feature
# def before_feature(context,feature):
#     path = "./Drivers/chromedriver.exe"
#     context.driver = webdriver.Chrome(executable_path=path)
#
#
# def after_feature(context,feature):
#     context.driver.close()

# Before and After for every Scenario feature
# def before_scenario(context,scenario):
#     path = "./Drivers/chromedriver.exe"
#     context.driver = webdriver.Chrome(executable_path=path)
#
#
# def after_scenario(context,scenario):
#     context.driver.close()