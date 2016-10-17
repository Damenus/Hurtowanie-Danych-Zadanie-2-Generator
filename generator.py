from faker import Factory
fake = Factory.create('pl_PL')

fake.name()
# 'Lucy Cechtelar'

fake.address()
# "426 Jordy Lodge
#  Cartwrightshire, SC 88120-6700"

fake.text()