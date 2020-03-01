from django import forms
from crispy_forms.helper import FormHelper
from .models import CreateRecord

class CreateRecordForm(forms.ModelForm):

    class Meta:
        model = CreateRecord
        fields = ('cr_no','cer_no','date_recieved','date_assigned',
        'complaint_name','complaint_address','complaint_state_of_origin','complaint_LGA',
        'complaint_sex','complaint_age','suspect_name','suspect_address','suspect_state_of_origin',
        'suspect_LGA','suspect_sex','suspect_age','offence','amount_involved_naira','amount_involved_dollar',
        'cfa_involved','others_involved','amount_recieved_naira','amount_recieved_dollar',
        'cfa_recieved','others_recieved','team','status','date_sent_to_legal')

        widgets={
            'cr_no':forms.TextInput(attrs={'class':'form-group'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["cr_no"].label = "CR:No."
        self.fields["cer_no"].label = "CER:No."
        self.fields["date_recieved"].label = "DATE RECIEVED"
        self.fields["date_assigned"].label = "DATE ASSIGNED"
        self.fields["complaint_name"].label = " COMPLAINT NAME"
        self.fields["complaint_address"].label = "COMPLAINT ADDRESS"
        self.fields["complaint_state_of_origin"].label = "COMPLAINT STATE OF ORIGIN"
        self.fields["complaint_LGA"].label = "COMPLAINT LGA"
        self.fields["complaint_sex"].label = "COMPLAINT SEX"
        self.fields["complaint_age"].label = "COMPLAINT AGE"
        self.fields["suspect_name"].label = "SUSPECT NAME"
        self.fields["suspect_address"].label = "SUSPECT ADDRESS"
        self.fields["suspect_state_of_origin"].label = "SUSPECT STATE OF ORIGIN"
        self.fields["suspect_LGA"].label = "SUSPECT LGA"
        self.fields["suspect_sex"].label = "SUSPECT SEX"
        self.fields["suspect_age"].label = "SUSPECT AGE"
        self.fields["offence"].label = "OFFENCE(S)"
        self.fields["amount_involved_naira"].label = "AMOUNT INVOVLED (NAIRA)"
        self.fields["amount_involved_dollar"].label = "AMOUNT INVOLVED (DOLLAR)"
        self.fields["cfa_involved"].label = "CFA (INVOLVED)"
        self.fields["others_involved"].label = "OTHERS INVOLVED"
        self.fields["amount_recieved_naira"].label = "AMOUNT RECIEVED (NAIRA)"
        self.fields["amount_recieved_dollar"].label = "AMOUNT RECIEVED (DOLLAR)"
        self.fields["cfa_recieved"].label = "CFA RECIEVED"
        self.fields["others_recieved"].label = "OTHERS RECIEVED"
        self.fields["team"].label = "IO/TEAM"
        self.fields["status"].label = "STATUS"
        self.fields["date_sent_to_legal"].label = "DATE SENT TO LEGAL"