from telegram.ext import* 
from telegram.constants import PARSEMODE_MARKDOWN_V2

updater= Updater(token='TOKEN')
dispatcher= updater.dispatcher


import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

def start(update, context) : 
    context.bot.send_message(chat_id=update.message.chat_id, text=''' 
    Bienvenue dans notre bot de télégramme .. ce bot vous aidera à développer vos connaissances en médicaments 
    choisissez l'un de ces médicaments :
    1_  /Spasfon 
    2_  /Dexamethasone
    3_  /voltarene
    4_  /cordarone
    5_  /salbutamol
    6_  /hydrocortisone
    7_  /zantac 
    8_  /loxen 
    9_  /primperan
    10_ /aspegic
    11_ /solumedrol
    
    
    ''')

def spasfon(update, context):
    context.bot.send_message(chat_id=update.message.chat_id,    
    text='''
    1\_ * Classification pharmacothérapeutique  * :
Gastro , Entéro , Hépatologie : Troubles fonctionnels digestifs et ou biliaires , Antispasmodiques à visée digestive : Antispasmodiques musculotropes 
Antalgiques , Antipyrétiques , Antispasmodiques , Antispasmodiques
   2\_ *Dénomination chimique * :
\_ phloroglucinol dihydrate
\_ triméthylphloroglucinol
   3\_ *Dénomination commune internationale* :
spasfon 
   4\_ *Indications* :
Traitement symptomatique des douleurs aiguës liées aux :
\_ troubles fonctionnels du tube digestif\.
\_ des voies biliaires, des voies urinaires : coliques néphrétiques\. 
\_ douloureuses aiguës en gynécologie\.
''' , parse_mode=PARSEMODE_MARKDOWN_V2 )
    context.bot.send_photo(chat_id=update.message.chat_id, photo=open('img/spasfon.jpg', 'rb'))

def Dexamethasone(update, context):
    context.bot.send_message(chat_id=update.message.chat_id,    
    text='''
    1\_ * Classification pharmacothérapeutique  * :
 Anti\-inflammatoires , Anti\-inflammatoires stéroïdiens \(AIS\) : corticoïdes : AIS voie injectable : action immédiate \(Dexaméthasone\)
   2\_ *Dénomination chimique * :
\_ dexaméthasone phosphate sodique
   3\_ *Dénomination commune internationale* :
Dexamethasone 
   4\_ *Indications* :
\_il est un corticostéroïde qui empêche la libération de substances dans le corps qui provoquent une inflammation\.
\_il est utilisée pour traiter de nombreuses affections inflammatoires telles que les troubles allergiques et les affections cutanées\.
\_il est utilisée pour traiter la colite ulcéreuse, l'arthrite, le lupus, le psoriasis et les troubles respiratoires\.
''' , parse_mode=PARSEMODE_MARKDOWN_V2 )
    context.bot.send_photo(chat_id=update.message.chat_id, photo=open('img/Dexamethasone.jpg', 'rb'))

def voltarene(update, context):
    context.bot.send_message(chat_id=update.message.chat_id,    
    text='''
    1\_ * Classification pharmacothérapeutique  * :
Anti\-inflammatoires : Anti\-inflammatoires non stéroïdiens \(AINS\) \- AINS arylcarboxyliques : Diclofénac \(Diclofénac seul\)
Rhumatologie : Anti\-inflammatoires non stéroïdiens \- AINS arylcarboxyliques : Diclofénac \(Diclofénac seul\)
   2\_ *Dénomination chimique * :
\_  diclofénac sodique 
   3\_ *Dénomination commune internationale* :
Voltarene 
   4\_ *Indications* :
\_ Le diclofénac agit en réduisant les substances dans le corps qui causent douleur et inflammation\.
\_ Les comprimés oraux de Voltaren sont utilisés pour traiter les douleurs légères à modérées\.
\_ traiter les signes et symptômes de l'arthrose ou de la polyarthrite rhumatoïde\.
\_ Voltaren est également utilisé pour traiter la spondylarthrite ankylosante\.
''' , parse_mode=PARSEMODE_MARKDOWN_V2 )
    context.bot.send_photo(chat_id=update.message.chat_id, photo=open('img/voltarene.jpg', 'rb'))

def cordarone(update, context):
    context.bot.send_message(chat_id=update.message.chat_id,    
    text='''
    1\_ * Classification pharmacothérapeutique  * :
 Cardiologie , Angéiologie , Antiarythmiques : Antiarythmiques , Groupe III \(Amiodarone : voie orale\)
   2\_ *Dénomination chimique * :
\_  amiodarone chlorhydrate\. 
   3\_ *Dénomination commune internationale* :
cordarone \.
   4\_ *Indications* :
\_Ce médicament est utilisé uniquement pour traiter les battements cardiaques anormaux qui peuvent être mortels\.
\_Il peut provoquer des effets secondaires graves et parfois mortels tels que des problèmes pulmonaires, thyroïdiens ou hépatiques\.
\_Ce médicament peut également aggraver les battements cardiaques anormaux\.
''' , parse_mode=PARSEMODE_MARKDOWN_V2 )
    context.bot.send_photo(chat_id=update.message.chat_id, photo=open('img/cordarone.jpg', 'rb'))

def salbutamol(update, context):
    context.bot.send_message(chat_id=update.message.chat_id,    
    text='''
    1\_ * Classification pharmacothérapeutique  * :
Pneumologie : Asthme et bronchopneumopathies chroniques : Bronchodilatateurs bêta\-2 stimulants d'action brève \- Voie respiratoire : Solutions pour inhalation par nébuliseur \(Salbutamol\)\.
   2\_ *Dénomination chimique * :
\_ salbutamol sulfate 
   3\_ *Dénomination commune internationale* :
salbutamol 
   4\_ *Indications* :
\_Salbutamol est utilisé pour traiter ou prévenir le bronchospasme chez les patients souffrant d'asthme, de bronchite, d'emphysème et d'autres maladies pulmonaires\.
\_Il est également utilisé pour prévenir le bronchospasme causé par l'exercice\.
\_Albuterol appartient à la famille des médicaments appelés bronchodilatateurs adrénergiques\.
''' , parse_mode=PARSEMODE_MARKDOWN_V2 )
    context.bot.send_photo(chat_id=update.message.chat_id, photo=open('img/salbutamol.jpg', 'rb'))


def hydrocortisone(update, context):
    context.bot.send_message(chat_id=update.message.chat_id,    
    text='''
    1\_ * Classification pharmacothérapeutique  * :
 Endocrinologie \- Médicaments de l'axe hypophyso\-surrénalien : Hormones glucocorticoïdes \(Voie injectable\)
   2\_ *Dénomination chimique * :
\_ hydrocortisone hémisuccinate sodique 
   3\_ *Dénomination commune internationale* :
hydrocortisone 
   4\_ *Indications* :
L'hydrocortisone est un médicament stéroïde utilisé dans le traitement de nombreuses affections différentes :
\_ y compris les troubles allergiques\.
\_les affections cutanées\.
\_la colite ulcéreuse\.
\_l'arthrite\.
\_le lupus\.
\_la sclérose en plaques ou les troubles pulmonaires\.
''' , parse_mode=PARSEMODE_MARKDOWN_V2 )
    context.bot.send_photo(chat_id=update.message.chat_id, photo=open('img/hydrocortisone.jpg', 'rb'))

def zantac(update, context):
    context.bot.send_message(chat_id=update.message.chat_id,    
    text='''
    1\_ * Classification pharmacothérapeutique  * :
Gastro \- Entéro \- Hépatologie : Reflux gastro\-oesophagien : Antisécrétoires gastriques : Antihistaminiques H2 : Ranitidine : Ulcère gastroduodénal \- Antisécrétoires gastriques : Antihistaminiques H2 \(Ranitidine\)
   2\_ *Dénomination chimique * :
\_  ranitidine chlorhydrate 
   3\_ *Dénomination commune internationale* :
zantac 
   4\_ *Indications* :
\_Zantac \(ranitidine\) appartient à un groupe de médicaments appelés inhibiteurs de l'histamine\-2\.
\_Il agit en réduisant la quantité d'acide produite par votre estomac\.
\_Zantac a été utilisé pour traiter et prévenir les ulcères de l'estomac et des intestins\. 
\_Il a également été utilisé pour traiter les conditions dans lesquelles l'estomac produit trop d'acide\.
''' , parse_mode=PARSEMODE_MARKDOWN_V2 )
    context.bot.send_photo(chat_id=update.message.chat_id, photo=open('img/zantac.jpg', 'rb'))

def loxen(update, context):
    context.bot.send_message(chat_id=update.message.chat_id,    
    text='''
    1\_ * Classification pharmacothérapeutique  * :
 Cardiologie \- Angéiologie : Antihypertenseurs \- Antihypertenseurs : voie IV : Inhibiteurs calciques \(Nicardipine\)\.
   2\_ *Dénomination chimique * :
\_  nicardipine chlorhydrate 
   3\_ *Dénomination commune internationale* :
loxen
   4\_ *Indications* :
\_ Hypertension artérielle maligne/encéphalopathie hypertensive\.
\_ Dissection aortique, quand le traitement par des bêtabloquants à courte durée d'action n'est pas approprié, ou en association avec un bêtabloquant quand le blocage des récepteurs bêta seul n'est pas efficace\. 
\_ La nicardipine est également indiquée dans le traitement de l'hypertension post\-opératoire \.
''' , parse_mode=PARSEMODE_MARKDOWN_V2 )
    context.bot.send_photo(chat_id=update.message.chat_id, photo=open('img/loxen.jpg', 'rb'))
    
def primperan (update, context):
    context.bot.send_message(chat_id=update.message.chat_id,    
    text='''
    1\_ * Classification pharmacothérapeutique  * :
Cancérologie \- Hématologie : Traitements associés \- Antiémétiques : Antagonistes de la dopamine \(Benzamides\)
Gastro \- Entéro \- Hépatologie : Nausées et vomissements \- Antagonistes de la dopamine : Benzamides \(Métoclopramide\)\.
   2\_ *Dénomination chimique * :
\_  métoclopramide chlorhydrate\.
   3\_ *Dénomination commune internationale* :
primperan 
   4\_ *Indications* :
\_ la prévention des nausées et vomissements post\-opératoires \.
\_ le traitement symptomatique des nausées et vomissements, incluant les nausées et vomissements induits par une crise migraineuse \.
\_ la prévention des nausées et vomissements induits par une radiothérapie\.
''' , parse_mode=PARSEMODE_MARKDOWN_V2 )
    context.bot.send_photo(chat_id=update.message.chat_id, photo=open('img/primperan.jpg', 'rb'))
start_handler = CommandHandler('start', start)


def aspegic(update, context):
    context.bot.send_message(chat_id=update.message.chat_id,    
    text='''
    1\_ * Classification pharmacothérapeutique  * :
Antalgiques \- Antipyrétiques \- Antispasmodiques : Antalgiques non opioïdes : Antalgiques non opioïdes seuls \- AINS et dérivés : Acide acétylsalicylique \(Formes injectables\)\.
   2\_ *Dénomination chimique * :
\_  acétylsalicylate de lysine 
   3\_ *Dénomination commune internationale* :
aspegic 
   4\_ *Indications* :
\_ Traitement de courte durée des douleurs intenses\.
\_ Traitement des rhumatismes inflammatoires\.
\_ Traitement symptomatique de la fièvre lorsque l'administration par voie orale n'est pas possible\.
''' , parse_mode=PARSEMODE_MARKDOWN_V2 )
    context.bot.send_photo(chat_id=update.message.chat_id, photo=open('img/aspegic.jpg', 'rb'))
    
def solumedrol(update, context):
    context.bot.send_message(chat_id=update.message.chat_id,    
    text='''
    1\_ * Classification pharmacothérapeutique  * :
Anti\-inflammatoires \- Anti\-inflammatoires stéroïdiens \(AIS\) : corticoïdes : AIS voie injectable : action immédiate \(Méthylprednisolone\)
   2\_ *Dénomination chimique * :
\_  méthylprednisolone hémisuccinate 
   3\_ *Dénomination commune internationale* :
solumedrol 
   4\_ *Indications* :
Utilisations de Solu\-Medrol: Il est utilisé pour de nombreux problèmes de santé comme les signes d'allergie, l'asthme, les problèmes de glande surrénale, les problèmes de sang, les éruptions cutanées ou les problèmes de gonflement\.
''' , parse_mode=PARSEMODE_MARKDOWN_V2 )
    context.bot.send_photo(chat_id=update.message.chat_id, photo=open('img/solumedrol.jpg', 'rb'))
    

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

start_handler = CommandHandler('spasfon', spasfon)
dispatcher.add_handler(start_handler)

start_handler = CommandHandler('Dexamethasone', Dexamethasone)
dispatcher.add_handler(start_handler)

start_handler = CommandHandler('voltarene', voltarene)
dispatcher.add_handler(start_handler)

start_handler = CommandHandler('cordarone', cordarone)
dispatcher.add_handler(start_handler)

start_handler = CommandHandler('salbutamol', salbutamol)
dispatcher.add_handler(start_handler)

start_handler = CommandHandler('hydrocortisone', hydrocortisone)
dispatcher.add_handler(start_handler)

start_handler = CommandHandler('zantac', zantac)
dispatcher.add_handler(start_handler)
                           
start_handler = CommandHandler('loxen', loxen)
dispatcher.add_handler(start_handler)


start_handler = CommandHandler('primperan', primperan)
dispatcher.add_handler(start_handler)

start_handler = CommandHandler('aspegic', aspegic)
dispatcher.add_handler(start_handler)


start_handler = CommandHandler('solumedrol', solumedrol)
dispatcher.add_handler(start_handler)

updater.start_polling()
