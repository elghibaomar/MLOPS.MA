from django.shortcuts import render
from .models import Email
from .serializers import EmailSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
import pandas as pd
import pickle


# Create your views here.



@api_view(['GET'])
def Marital_Customer(request):
    # GET
    if request.method == 'GET':
        maritals = Email.objects.all()
        # df = pd.DataFrame(emails.values())
        # df['Conversion'] = df['Purchase'].apply(lambda x : 1 if x == "yes" else 0)
        serializer = EmailSerializer(maritals, many=True)
        df = pd.DataFrame(serializer.data)
        df['Conversion'] = df['Purchase'].apply(lambda x : 1 if x == "yes" else 0)
        Conversion_By_Marital = df['Marital'].value_counts()
        Conversion_By_Marital = df['Marital'].value_counts()
        return Response(Conversion_By_Marital)



@api_view(['GET'])
def monthly_customer_purchase(request):
    # GET
    if request.method == 'GET':
        monthly = Email.objects.all()
        # df = pd.DataFrame(emails.values())
        # df['Conversion'] = df['Purchase'].apply(lambda x : 1 if x == "yes" else 0)
        serializer = EmailSerializer(monthly, many=True)
        df = pd.DataFrame(serializer.data)
        df['Conversion'] = df['Purchase'].apply(lambda x : 1 if x == "yes" else 0)
        monthly_all_customers = df.loc[df['Conversion'] == 1].groupby('Date')['Customer_id'].count()
        monthly_unique_customers = df.loc[df['Conversion'] == 1].groupby('Date')['Customer_id'].nunique()
        monthly_reapet_customers = monthly_all_customers - monthly_unique_customers
        monthly_reapet_customers_rate = monthly_reapet_customers / monthly_all_customers * 100
        all_customers = [monthly_all_customers , monthly_unique_customers, monthly_reapet_customers_rate]
        return Response(all_customers)


@api_view(['GET'])
def Product_Purchase(request):
    # GET
    if request.method == 'GET':
        products = Email.objects.all()
        # df = pd.DataFrame(emails.values())
        # df['Conversion'] = df['Purchase'].apply(lambda x : 1 if x == "yes" else 0)
        serializer = EmailSerializer(products, many=True)
        df = pd.DataFrame(serializer.data)
        df['Conversion'] = df['Purchase'].apply(lambda x : 1 if x == "yes" else 0)
        top_product_ever = df.loc[df['Conversion'] == 1].groupby('Product_id')['Conversion'].count().sort_values(ascending=False)
        # print(top_product_ever)
        index_top_product_ever = top_product_ever.index[:3]
        top = [top_product_ever.index[:5] , top_product_ever[:3]]
        return Response(top)


@api_view(['GET'])
def Countries_Purchase(request):
    # GET
    if request.method == 'GET':
        countries = Email.objects.all()
        # df = pd.DataFrame(emails.values())
        # df['Conversion'] = df['Purchase'].apply(lambda x : 1 if x == "yes" else 0)
        serializer = EmailSerializer(countries, many=True)
        df = pd.DataFrame(serializer.data)
        df['Conversion'] = df['Purchase'].apply(lambda x : 1 if x == "yes" else 0)
        countries_purchase = df.groupby(by = 'Countries')['Conversion'].sum()
        total_purchase = df['Conversion'].sum()
        tt = [countries_purchase , total_purchase]
        return Response(tt)


@api_view(['GET'])
def Conversion_Age_Marital(request):
    # GET
    if request.method == 'GET':
        ages = Email.objects.all()
        # df = pd.DataFrame(emails.values())
        # df['Conversion'] = df['Purchase'].apply(lambda x : 1 if x == "yes" else 0)
        serializer = EmailSerializer(ages, many=True)
        df = pd.DataFrame(serializer.data)
        df['Conversion'] = df['Purchase'].apply(lambda x : 1 if x == "yes" else 0)
        df['Age_Group'] = df['Age'].apply(
            lambda x: '[18, 30)' if x < 30 else '[30, 40)' if x < 40 \
                else '[40, 50)' if x < 50 else '[50, 60)' if x < 60 \
                else '[60, 70)' if x < 70 else '70+'
        )
        Conversion_Age_Marital = df.groupby(['Age_Group', 'Marital'])['Conversion'].sum().unstack('Marital').fillna(0)
        Conversion_Age_Marital = Conversion_Age_Marital.divide(
            df.groupby(
                by='Age_Group'
            )['Conversion'].count(), 
            axis=0
                )
        return Response(Conversion_Age_Marital.loc[['[18, 30)','[30, 40)','[40, 50)','[50, 60)','[60, 70)','70+']])

@api_view(['GET'])
def Top_5_Products(request):
    # GET
    if request.method == 'GET':
        products = Email.objects.all()
        # df = pd.DataFrame(emails.values())
        # df['Conversion'] = df['Purchase'].apply(lambda x : 1 if x == "yes" else 0)
        serializer = EmailSerializer(products, many=True)
        df = pd.DataFrame(serializer.data)
        df['Conversion'] = df['Purchase'].apply(lambda x : 1 if x == "yes" else 0)
        date_item_5 = pd.DataFrame(df.loc[(df['Product_id'].isin(['85123A','22834','22837','22423','22355'])) & (df['Conversion'] == 1)].groupby(['Date','Product_id'])['Conversion'].count())
        piv_date_item_5 = date_item_5.reset_index().pivot('Date','Product_id').fillna(0)
        print(piv_date_item_5)
        return Response(date_item_5)


@api_view(['GET'])
def Age_Distribution(request):
    # GET
    if request.method == 'GET':
        ages = Email.objects.all()
        # df = pd.DataFrame(emails.values())
        # df['Conversion'] = df['Purchase'].apply(lambda x : 1 if x == "yes" else 0)
        serializer = EmailSerializer(ages, many=True)
        df = pd.DataFrame(serializer.data)
        return Response(df['Age'])


@api_view(['GET'])
def Gender_Conversion(request):
    # GET
    if request.method == 'GET':
        gender = Email.objects.all()
        serializer = EmailSerializer(gender, many=True)
        df = pd.DataFrame(serializer.data)
        df = pd.DataFrame(gender.values())
        df['Conversion'] = df['Purchase'].apply(lambda x : 1 if x == "yes" else 0)
        df_gender = df.groupby(by = 'Gender')['Conversion'].sum()
        return Response(df_gender[1:3])
