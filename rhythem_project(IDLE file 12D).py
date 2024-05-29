#Importing Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#CSV to Dataframe
dfmain=pd.read_csv('C:\rhythem\1.INFORMATICS\info project\final_proj_tobesubmitted\folders to be submitted to maam\blackfridayfinal.csv')

#Login Data
data={'Username':['Ram','Sita','Gita','Laxman'],'Password':['abcd1','ghij23','xyz123','pqr123']}
df=pd.DataFrame(data)

#Login/Register code
def login():
    print('****************************************************')
    print('*             BLACK FRIDAY SALE ANALYSIS           *')
    print('****************************************************''\n')
    
    while True:
        
        print('+++++++++++++++LOGIN/REGISTER+++++++++++++++''\n')
        
        print('1.LOGIN (If you already have an account)')
        print('2.REGISTER(To create a new account)') 
        print('3.EXIT')
        
        choice1=int(input('Enter your choice:'))

        if choice1==1:
            user_name=input('Enter your username:')
            if user_name in list(df['Username']):
                password=input('Enter your password:')
                if password in list(df['Password']):
                    print('----------------------''\n'
                          'LOGGED IN SUCCESSFULLY''\n'
                          '-----------------------''\n')
                    break
                else:
                    print('.........INCORRECT PASSWORD.........')
            else:
                print('.........INCORRECT USERNAME.........''\n')

        elif choice1==2:
            user_name=input('Enter your username:')
            password=input('Create your password:')
            df.loc[len(df)]=[user_name,password]
            print('-------------------------------------''\n'
                  'YOU HAVE BEEN REGISTERED SUCCESSFULLY''\n'
                  '-------------------------------------''\n'
                  '-------------------------------------''\n'
                  '-------PLEASE LOGIN AGAIN-------''\n'
                  '-------------------------------------''\n')

        elif choice1==3:
            print('---------------')
            print('----GOODBYE----')
            print('---------------')
            break
        
        else:
            print('----------INVALID INPUT----------''\n')

#Data Visualisation
def mainmenu():
    while True:
        print('+++++++ MAIN_MENU +++++++''\n')
        print('ON WHAT BASIS WOULD YOU LIKE TO SEE THE ANALYSIS?')
        print('++++++++++++++++++++++++++++++++++++++++++''\n'
              '+ 1.Based on AGE of customers            +''\n'
              '+ 2.Based on GENDER of customers         +''\n'
              '+ 3.Based on MARITAL STATUS of customers +''\n'
              '+ 4.Based on CITY CATEGORY & YEARS OF    +''\n'
              '+   STAY IN CURRENT CITY  of customers   +''\n'
              '+ 5.LOGOUT                               +''\n'
              '++++++++++++++++++++++++++++++++++++++++++')
        
        choice2=int(input('Enter your choice:'))
        
        if choice2==1:
            print('+++++++++++++++++++++++++++++++++++''\n'
                  '+ 1.AGE STATS                     +''\n'
                  '+ 2.AGE VS PURCHASE STATS         +''\n'
                  '+ 3.AGE VS GENDER                 +''\n'
                  '+++++++++++++++++++++++++++++++++++')
            choice3=int(input('Enter your choice:'))
            if choice3==1:
                print('AGE GROUP VS NO OF CUSTOMERS IN THAT AGE GROUP')
                print(dfmain['Age'].value_counts().sort_index())
                dfmain['Age'].value_counts().plot(kind='pie',autopct='%1.2f%%',explode=(.05,.05,.05,.05,.25,.25,.25))
                plt.show()
            
            elif choice3==2:
                print('AGE GROUP VS TOTAL PURCHASE')
                age=['0-17','18-25','26-35','36-45','46-50','51-55','55+']
                purchase=[]
                gdf=dfmain.groupby('Age')
                for i in age:
                    tot=sum(gdf.get_group(i)['Purchase'])
                    purchase.append(tot)
                print(pd.Series(purchase,index=age))
                plt.bar(age,purchase)
                plt.xlabel('age groups')
                plt.ylabel('total purchase')
                plt.show()

            elif choice3==3:
                print('AGE GROUP VS NO OF MALES & FEMALES')
                age=['0-17','18-25','26-35','36-45','46-50','51-55','55+']
                gdf=dfmain.groupby('Age')
                female=[]
                male=[]
                x=np.arange(7)
                for i in age:
                    ftot=gdf.get_group(i)['Gender'].value_counts()['F']
                    mtot=gdf.get_group(i)['Gender'].value_counts()['M']
                    female.append(ftot)
                    male.append(mtot)
                plt.bar(x+0.00,female,width=0.25,label='females')
                plt.bar(x+0.25,male,width=0.25,label='males')
                plt.legend()
                plt.xlabel('Age_groups')
                plt.ylabel('No of males/females')
                plt.xticks(x,age)
                print(pd.DataFrame({'Females':female,'Males':male},index=age))
                plt.show()


        elif choice2==2:
            print('+++++++++++++++++++++++++''\n'
                  '+ 1.GENDER STATS        +''\n'
                  '+ 2.GENDER VS PURCHASE  +''\n'
                  '+++++++++++++++++++++++++')
            choice4=int(input('Enter your choice:'))
            if choice4==1:
                print('GENDER VS NO OF CUSTOMERS')
                print(dfmain['Gender'].value_counts())
                dfmain['Gender'].value_counts().plot(kind='pie',autopct='%1.2f%%',explode=(0.02,0.02))
                plt.show()

            elif choice4==2:
                print('GENDER VS TOTAL PURCHASE')
                gdf1=dfmain.groupby('Gender')
                gen=['F','M']
                genpur=[]
                for k in gen:
                    gtot=sum(gdf1.get_group(k)['Purchase'])
                    genpur.append(gtot)
                print(pd.Series(genpur,index=gen))
                plt.bar(gen,genpur)
                plt.ylabel('total purchase')
                plt.show()
                

        elif choice2==3:
            print('++++++++++++++++++++++++++++++''\n'
                  '+ 1.MARITAL STATUS STATS     +''\n'
                  '+ 2.AGE GROUP+MARITAL STATUS +''\n'
                  '++++++++++++++++++++++++++++++')
            choice5=int(input('Enter your choice:'))
            if choice5==1:
                print('% OF MARRIED/UNMARRIED CUSTOMERS')
                mar_stat=pd.Series(dfmain['Marital_Status'].value_counts())
                mar_stat.rename(index={1:'Married',0:'Unmarried'},inplace=True)
                print(mar_stat)
                mar_stat.plot(kind='barh')
                plt.xlabel('No of customers')
                plt.show()

            if choice5==2:
                print('AGE GROUP VS NO OF MARRIED/UNMARRIED CUSTOMERS')
                l=['0-17','18-25','26-35','36-45','46-50','51-55','55+']
                q=dfmain.groupby('Age')
                unmarried=[]
                married=[]
                x=np.arange(7)
                for i in l:
                    if len(q.get_group(i)['Marital_Status'].value_counts())==2:
                        unmar_tot=q.get_group(i)['Marital_Status'].value_counts()[0]
                        mar_tot=q.get_group(i)['Marital_Status'].value_counts()[1]
                        unmarried.append(unmar_tot)
                        married.append(mar_tot)
                    else:
                        if q.get_group(i)['Marital_Status'].value_counts().index[0]==1:
                            mar_tot=q.get_group(i)['Marital_Status'].value_counts()[1]
                            unmarried.append(0)
                            married.append(mar_tot)
                        if q.get_group(i)['Marital_Status'].value_counts().index[0]==0:
                            unmar_tot=q.get_group(i)['Marital_Status'].value_counts()[0]
                            unmarried.append(unmar_tot)
                            married.append(0)
                plt.bar(x+0.00,unmarried,width=0.25,label='unmarried')
                plt.bar(x+0.25,married,width=0.25,label='married')
                plt.legend()
                plt.xlabel('Age_groups')
                plt.ylabel('No of married/unmarried')
                plt.xticks(x,l)
                plt.show()
                

        elif choice2==4:
            print('++++++++++++++++++++++++++++++''\n'
                  '+ 1.CITY CATEGORY STATS      +''\n'
                  '+ 2.YEARS OF STAY IN CURRENT +''\n'
                  '+   CITY                     +''\n'
                  '+ 3.CITY CATEGORY AND AMOUNT +''\n'
                  '+   OF PURCHASE              +''\n'
                  '++++++++++++++++++++++++++++++')
            choice6=int(input('Enter your choice:'))
            if choice6==1:
                print('CITY CATEGORY VS NO OF CUSTOMERS')
                print(dfmain['City_Category'].value_counts())
                dfmain['City_Category'].value_counts().plot(kind='pie',autopct='%1.2f%%',explode=(.01,.01,.01))
                plt.show()

            elif choice6==2:
                print('YEARS OF STAY VS NO OF CUSTOMERS')
                print(dfmain['Stay_In_Current_City_Years'].value_counts())
                dfmain['Stay_In_Current_City_Years'].value_counts().plot(kind = 'pie', autopct='%0.2f')
                plt.show()

            elif choice6==3:
               print('CITY CATEGORY VS TOTAL PURCHASE')
               gdf2=dfmain.groupby('City_Category')
               csum=[]
               city=['A','B','C']
               for i in city:
                   ctot=sum(gdf2.get_group(i)['Purchase'])
                   csum.append(ctot)
               cdf=pd.DataFrame({'city_category':city,'purchase_total':csum})
               print(cdf)
               plt.bar(cdf['city_category'],cdf['purchase_total'])
               plt.xlabel('city_category')
               plt.ylabel('total purchase')
               plt.show()

                  
        elif choice2==5:
            print(login())     
            break
            
            
                

