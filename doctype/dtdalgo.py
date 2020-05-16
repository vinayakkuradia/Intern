#Importing Libraries
import cv2
import re
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

#Defining terms for documents
certTerms = ['cerificate', 'certify', 'certify that', 'to whom', 'to whomsoever', 'it may concern', 'certified', 'awarded', 'awarded to', 'presented', 'presented to', 'completed', 'successful', 'completion', 'appreciation', 'participation', 'completion', 'completition of']
legTerms = ['affidavit', 'bail bond', 'bond', 'case citation', 'condition', 'contract', 'party', 'parties', 'defence', 'law', 'order', 'claim', 'parol', 'patent', 'petition', 'restraining', 'clause', 'terms', 'will', 'warranty', 'witness', 'testimony', 'sentenc', 'mediation', 'interrog', 'felony', 'damages', 'agreement', 'court', 'rights', 'section', 'declar', 'memorandum', 'contract', 'policy', 'lease', 'rent']
medTerms = ['medi', 'medical', 'examin', 'person', 'patient', 'health', 'examination', 'practitioner', 'disease', 'suffer', 'hospital', 'emergency', 'vaccin', 'care', 'pathology', 'report', 'condition', 'physical', 'mental', 'doctor', 'dr', 'analysis', 'blood', 'specialist', 'clinic', 'symptom']
billTerms = ['account', 'bill', 'billing', 'due', 'total', 'amount', 'supply', 'service', 'tax', 'customer', 'description', 'units', 'charge', 'payment', 'balance', 'gst', 'goods', 'packing', 'cash', 'cheque', 'rate', 'item', 'qty', 'quantity', 'transaction', 'uses', 'particulars', '[0-9]', '[0-9]\.?[0-9]?', '[A-Z]\d']


def detect(filename):
  #Loading Image
  #img = cv2.imread('./media/2.jpg')

  #Extracting text from Image
  text = pytesseract.image_to_string('doctype/media/'+filename)

  #Initializing word detect count to 0
  certificate = 0
  legal = 0
  medical = 0
  bill = 0

  #Matching words with document
  for element in certTerms:
    x = re.findall(element, text, re.IGNORECASE)
    if len(x)>0:
      certificate = certificate + 1

  for element in legTerms:
    x = re.findall(element, text, re.IGNORECASE)
    if len(x)>0:
      legal = legal + 1

  for element in medTerms:
    x = re.findall(element, text, re.IGNORECASE)
    if len(x)>0:
      medical = medical + 1

  for element in billTerms:
    x = re.findall(element, text, re.IGNORECASE)
    if len(x)>0:
      bill = bill + 1

  #Identifying document type

  var = [certificate, legal, medical, bill]
  occurance = max(var)

  if occurance == certificate and occurance>0:
    doctype = 'Certificate'
  elif occurance == legal and occurance>0:
    doctype = 'Legal'
  elif occurance == medical and occurance>0:
    doctype = 'Medical'
  elif occurance == bill and occurance>0:
    doctype = 'Bill'
  else:
    doctype = 'Unidentified'

  return  doctype
