import unittest
import pandas as pd
from day5.esercizi.ex1_dataEnrichment import ex1
from day5.esercizi.ex2_dataManipulation import ex2

class TestEx1(unittest.TestCase):
    def test_ex1_step2(self):
        p1, pf1, en1=ex1()
        p,pf,en= self.ex1_steps()
        self.assertTrue(p.equals(p1))
        self.assertTrue(pf.equals(pf1))

    def test_ex1_step3(self):
        p1, pf1, en1=ex1()
        p,pf,en= self.ex1_steps()
        self.assertTrue(en.equals(en1))



    def ex1_steps(self):
        p = pd.read_csv('resources/p.csv', sep='@')
        pf = pd.read_csv('resources/pf.csv',sep='|')
        en = pf.merge(p,on='codp')
        return p,pf,en


class TestEx2(unittest.TestCase):

    def test_ex2_step1(self):
        train, test = self.step1()
        train1, test1, aggregatedConsumption1= ex2()

        self.assertEquals(len(set(train.columns).intersection(train1.columns)),len(train.columns),'train column match')
        self.assertEquals(train.shape, train1[train.columns].shape, 'trazin size match')
        self.assertEquals(len(set(test.columns).intersection(test1.columns)),len(test.columns),'test column match')
        self.assertEquals(test.shape, test1[test.columns].shape, 'test size match')


    def test_ex2_step2(self):
        train, test = self.step2()
        train1, test1, aggregatedConsumption1= ex2()
        train1.sort_values('id',inplace=True)
        train.sort_values('id', inplace=True)
        test1.sort_values('id', inplace=True)
        test.sort_values('id', inplace=True)
        self.assertEquals(len(set(train.columns).intersection(train1.columns)),len(train.columns),'train column match')
        self.assertTrue(train.equals(train1[train.columns]),'dataframe di train non corretto')
        self.assertEquals(len(set(test.columns).intersection(test1.columns)),len(test.columns),'test column match')
        self.assertTrue(test.equals(test1[test.columns]),'dataframe di test non corretto')


    def test_ex2_step3(self):
        train, test,aggregatedConsumption = self.step3()
        train1, test1, aggregatedConsumption1= ex2()
        aggregatedConsumption1.sort_values('wattConsumption',inplace=True)
        aggregatedConsumption.sort_values('wattConsumption', inplace=True)

        self.assertTrue(aggregatedConsumption.equals(aggregatedConsumption1),'dataframe di train non corretto')

    def test_ex2_step4(self):
        train, test,aggregatedConsumption=self.step4()
        train1, test1, aggregatedConsumption1= ex2()
        test1.sort_values('id', inplace=True)
        test.sort_values('id', inplace=True)
        self.assertTrue(test.equals(test1),'confronto daset di test')


    def step1(self):
        train = pd.read_csv('resources\\sample_train.csv')
        test = pd.read_csv('resources\\sample_test.csv')
        return train,test

    def step2(self):
        train,test= self.step1()
        test['datetime'] = pd.to_datetime(test['datetime'])
        train['datetime'] = pd.to_datetime(train['datetime'])
        train['hour'] = train['datetime'].dt.hour
        test['hour'] = test['datetime'].dt.hour
        return train,test

    def step3(self):
        train,test = self.step2()
        aggregatedConsumption = train.groupby('hour').agg({'wattConsumption': 'sum'})
        return  train,test,aggregatedConsumption

    def step4(self):
        train,test,aggregatedConsumption = self.step3()
        test = test.merge(aggregatedConsumption, left_on='hour', right_index=True)
        return  train,test,aggregatedConsumption

if __name__ == '__main__':
    unittest.main()
