from .serializers import ledgersSerializers,debthSerializers,accountSerializers,debitSerializers
from .models import ledgers,debth,account,debit
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAdminUser,IsAuthenticated
from rest_framework.authtoken.models import Token
from rest_framework.filters import SearchFilter
from rest_framework.generics import ListAPIView


class ledgersView(APIView):
    def get(self,request,format=None,pk=None):
        id=pk
        if id is not None:
            led=ledgers.objects.get(id=id)
            serializer=ledgersSerializers(led)
            tkn=request.META.get('HTTP_AUTHORIZATION')
            return Response(serializer.data)
        led=ledgers.objects.filter(branch_code=request.user.username)
        serializer=ledgersSerializers(led,many=True)
        return Response(serializer.data)

class ledgersTotalview(ListAPIView):
    queryset=ledgers.objects.all()
    serializer_class=ledgersSerializers

class accountView(APIView):
    def get(self,request,format=None,pk=None):
        id=pk
        tkn=request.META.get('HTTP_AUTHORIZATION')
        acc=account.objects.filter(branch_code=request.user.username)
        serializer=accountSerializers(acc,many=True)
        return Response(serializer.data)

class branchdebitView(ListAPIView):
    queryset=account.objects.all()
    serializer_class=accountSerializers
    filter_backends=[SearchFilter]
    search_fields=['^branch_code']


class accountCreate(APIView):
    def post(self,request):
        bcode=request.data.get('branch_code')
        if request.data.get('aicin'):
            aicin=int(request.data.get('aicin'))
        else:
            aicin=0
        if request.data.get('aicout'):
            aicout=int(request.data.get('aicout'))
        else:
            aicout=0
        desc=request.data.get('description')
        account.objects.create(branch_code=bcode,aicin=aicin,aicout=aicout,description=desc)
        dbt=aicout-aicin
        obj=debit.objects.get(branch_code=bcode)
        obj.debit+=dbt
        obj.save()
        return Response('Created !')




class AICdebthView(APIView):
    permission_classes=[IsAdminUser]
    def get(self,request,format=None,pk=None):
        branch_code=pk
        if branch_code is not None:
            dt=debth.objects.get(branch_code=branch_code)
            serializer=debthSerializers(dt)
            return Response(serializer.data)
        dt=debth.objects.all()
        serializer=debthSerializers(dt,many=True)
        return Response(serializer.data)

class AICdebitView(APIView):
    permission_classes=[IsAdminUser]
    def get(self,request,format=None,pk=None):
        branch_code=pk
        if branch_code is not None:
            dt=debit.objects.get(branch_code=branch_code)
            serializer=debitSerializers(dt)
            return Response(serializer.data)
        dt=debit.objects.all()
        serializer=debitSerializers(dt,many=True)
        return Response(serializer.data)


class debthView(APIView):
    def get(self,request,format=None,pk=None):
        branch_code=pk
        if branch_code is not None:
            dt=debth.objects.get(branch_code=branch_code)
            serializer=debthSerializers(dt)
            return Response(serializer.data)
        dt=debth.objects.filter(branch_code=request.user.username)
        serializer=debthSerializers(dt,many=True)
        return Response(serializer.data)

class debitView(APIView):
    def get(self,request,format=None,pk=None):
        branch_code=pk
        if branch_code is not None:
            dt=debit.objects.get(branch_code=branch_code)
            serializer=debitSerializers(dt)
            return Response(serializer.data)
        dt=debit.objects.filter(branch_code=request.user.username)
        serializer=debitSerializers(dt,many=True)
        return Response(serializer.data)