_n='jmAttributeGroup'
_m='jmJobGroup'
_l='jmJobIDGroup'
_k='jmGeneralGroup'
_j='jmAttributeValueAsOctets'
_i='jmAttributeValueAsInteger'
_h='jmJobOwner'
_g='jmJobImpressionsCompleted'
_f='jmJobImpressionsPerCopyRequested'
_e='jmJobKOctetsProcessed'
_d='jmJobKOctetsPerCopyRequested'
_c='jmNumberOfInterveningJobs'
_b='jmJobStateReasons1'
_a='jmJobState'
_Z='jmJobIDJobIndex'
_Y='jmJobIDJobSetIndex'
_X='jmGeneralJobSetName'
_W='jmGeneralAttributePersistence'
_V='jmGeneralJobPersistence'
_U='jmGeneralNewestActiveJobIndex'
_T='jmGeneralOldestActiveJobIndex'
_S='jmGeneralNumberOfActiveJobs'
_R='jmAttributeInstanceIndex'
_Q='jmAttributeTypeIndex'
_P='JmJobStringTC'
_O='JmJobStateReasons1TC'
_N='JmJobStateTC'
_M='jmJobSubmissionID'
_L='JmUTF8StringTC'
_K='seconds'
_J='jmJobIndex'
_I='OctetString'
_H='jmGeneralJobSetIndex'
_G='not-accessible'
_F='other'
_E='unknown'
_D='Integer32'
_C='read-only'
_B='Job-Monitoring-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_I,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
jobmonMIB=ModuleIdentity((1,3,6,1,4,1,2699,1,1))
if mibBuilder.loadTexts:jobmonMIB.setRevisions(('1999-02-19 00:00',))
class JmUTF8StringTC(TextualConvention,OctetString):status=_A;displayHint='255a';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
class JmJobStringTC(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
class JmNaturalLanguageTagTC(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
class JmTimeStampTC(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
class JmJobSourcePlatformTypeTC(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12)));namedValues=NamedValues(*((_F,1),(_E,2),('sptUNIX',3),('sptOS2',4),('sptPCDOS',5),('sptNT',6),('sptMVS',7),('sptVM',8),('sptOS400',9),('sptVMS',10),('sptWindows',11),('sptNetWare',12)))
class JmFinishingTC(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_F,1),(_E,2),('none',3),('staple',4),('punch',5),('cover',6),('bind',7)))
class JmPrintQualityTC(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_F,1),(_E,2),('draft',3),('normal',4),('high',5)))
class JmPrinterResolutionTC(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(9,9));fixedLength=9
class JmTonerEconomyTC(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3,4)));namedValues=NamedValues(*((_E,2),('off',3),('on',4)))
class JmBooleanTC(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3,4)));namedValues=NamedValues(*((_E,2),('false',3),('true',4)))
class JmMediumTypeTC(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13)));namedValues=NamedValues(*((_F,1),(_E,2),('stationery',3),('transparency',4),('envelope',5),('envelopePlain',6),('envelopeWindow',7),('continuousLong',8),('continuousShort',9),('tabStock',10),('multiPartForm',11),('labels',12),('multiLayer',13)))
class JmJobCollationTypeTC(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_F,1),(_E,2),('uncollatedSheets',3),('collatedDocuments',4),('uncollatedDocuments',5)))
class JmJobSubmissionIDTypeTC(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,1));fixedLength=1
class JmJobStateTC(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3,4,5,6,7,8,9)));namedValues=NamedValues(*((_E,2),('pending',3),('pendingHeld',4),('processing',5),('processingStopped',6),('canceled',7),('aborted',8),('completed',9)))
class JmAttributeTypeTC(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,3,4,5,6,7,8,9,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,50,51,52,53,54,55,56,70,71,72,73,74,75,76,77,90,91,92,93,94,95,96,97,110,111,112,113,114,115,130,131,132,150,151,152,170,171,172,173,174,175,190,191,192,193,194,195)));namedValues=NamedValues(*((_F,1),('jobStateReasons2',3),('jobStateReasons3',4),('jobStateReasons4',5),('processingMessage',6),('processingMessageNaturalLangTag',7),('jobCodedCharSet',8),('jobNaturalLanguageTag',9),('jobURI',20),('jobAccountName',21),('serverAssignedJobName',22),('jobName',23),('jobServiceTypes',24),('jobSourceChannelIndex',25),('jobSourcePlatformType',26),('submittingServerName',27),('submittingApplicationName',28),('jobOriginatingHost',29),('deviceNameRequested',30),('queueNameRequested',31),('physicalDevice',32),('numberOfDocuments',33),('fileName',34),('documentName',35),('jobComment',36),('documentFormatIndex',37),('documentFormat',38),('jobPriority',50),('jobProcessAfterDateAndTime',51),('jobHold',52),('jobHoldUntil',53),('outputBin',54),('sides',55),('finishing',56),('printQualityRequested',70),('printQualityUsed',71),('printerResolutionRequested',72),('printerResolutionUsed',73),('tonerEcomonyRequested',74),('tonerEcomonyUsed',75),('tonerDensityRequested',76),('tonerDensityUsed',77),('jobCopiesRequested',90),('jobCopiesCompleted',91),('documentCopiesRequested',92),('documentCopiesCompleted',93),('jobKOctetsTransferred',94),('sheetCompletedCopyNumber',95),('sheetCompletedDocumentNumber',96),('jobCollationType',97),('impressionsSpooled',110),('impressionsSentToDevice',111),('impressionsInterpreted',112),('impressionsCompletedCurrentCopy',113),('fullColorImpressionsCompleted',114),('highlightColorImpressionsCompleted',115),('pagesRequested',130),('pagesCompleted',131),('pagesCompletedCurrentCopy',132),('sheetsRequested',150),('sheetsCompleted',151),('sheetsCompletedCurrentCopy',152),('mediumRequested',170),('mediumConsumed',171),('colorantRequested',172),('colorantConsumed',173),('mediumTypeConsumed',174),('mediumSizeConsumed',175),('jobSubmissionToServerTime',190),('jobSubmissionTime',191),('jobStartedBeingHeldTime',192),('jobStartedProcessingTime',193),('jobCompletionTime',194),('jobProcessingCPUTime',195)))
class JmJobServiceTypesTC(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
class JmJobStateReasons1TC(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
class JmJobStateReasons2TC(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
class JmJobStateReasons3TC(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
class JmJobStateReasons4TC(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_JobmonMIBObjects_ObjectIdentity=ObjectIdentity
jobmonMIBObjects=_JobmonMIBObjects_ObjectIdentity((1,3,6,1,4,1,2699,1,1,1))
_JmGeneral_ObjectIdentity=ObjectIdentity
jmGeneral=_JmGeneral_ObjectIdentity((1,3,6,1,4,1,2699,1,1,1,1))
_JmGeneralTable_Object=MibTable
jmGeneralTable=_JmGeneralTable_Object((1,3,6,1,4,1,2699,1,1,1,1,1))
if mibBuilder.loadTexts:jmGeneralTable.setStatus(_A)
_JmGeneralEntry_Object=MibTableRow
jmGeneralEntry=_JmGeneralEntry_Object((1,3,6,1,4,1,2699,1,1,1,1,1,1))
jmGeneralEntry.setIndexNames((0,_B,_H))
if mibBuilder.loadTexts:jmGeneralEntry.setStatus(_A)
class _JmGeneralJobSetIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32767))
_JmGeneralJobSetIndex_Type.__name__=_D
_JmGeneralJobSetIndex_Object=MibTableColumn
jmGeneralJobSetIndex=_JmGeneralJobSetIndex_Object((1,3,6,1,4,1,2699,1,1,1,1,1,1,1),_JmGeneralJobSetIndex_Type())
jmGeneralJobSetIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:jmGeneralJobSetIndex.setStatus(_A)
class _JmGeneralNumberOfActiveJobs_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_JmGeneralNumberOfActiveJobs_Type.__name__=_D
_JmGeneralNumberOfActiveJobs_Object=MibTableColumn
jmGeneralNumberOfActiveJobs=_JmGeneralNumberOfActiveJobs_Object((1,3,6,1,4,1,2699,1,1,1,1,1,1,2),_JmGeneralNumberOfActiveJobs_Type())
jmGeneralNumberOfActiveJobs.setMaxAccess(_C)
if mibBuilder.loadTexts:jmGeneralNumberOfActiveJobs.setStatus(_A)
class _JmGeneralOldestActiveJobIndex_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_JmGeneralOldestActiveJobIndex_Type.__name__=_D
_JmGeneralOldestActiveJobIndex_Object=MibTableColumn
jmGeneralOldestActiveJobIndex=_JmGeneralOldestActiveJobIndex_Object((1,3,6,1,4,1,2699,1,1,1,1,1,1,3),_JmGeneralOldestActiveJobIndex_Type())
jmGeneralOldestActiveJobIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:jmGeneralOldestActiveJobIndex.setStatus(_A)
class _JmGeneralNewestActiveJobIndex_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_JmGeneralNewestActiveJobIndex_Type.__name__=_D
_JmGeneralNewestActiveJobIndex_Object=MibTableColumn
jmGeneralNewestActiveJobIndex=_JmGeneralNewestActiveJobIndex_Object((1,3,6,1,4,1,2699,1,1,1,1,1,1,4),_JmGeneralNewestActiveJobIndex_Type())
jmGeneralNewestActiveJobIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:jmGeneralNewestActiveJobIndex.setStatus(_A)
class _JmGeneralJobPersistence_Type(Integer32):defaultValue=60;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(15,2147483647))
_JmGeneralJobPersistence_Type.__name__=_D
_JmGeneralJobPersistence_Object=MibTableColumn
jmGeneralJobPersistence=_JmGeneralJobPersistence_Object((1,3,6,1,4,1,2699,1,1,1,1,1,1,5),_JmGeneralJobPersistence_Type())
jmGeneralJobPersistence.setMaxAccess(_C)
if mibBuilder.loadTexts:jmGeneralJobPersistence.setStatus(_A)
if mibBuilder.loadTexts:jmGeneralJobPersistence.setUnits(_K)
class _JmGeneralAttributePersistence_Type(Integer32):defaultValue=60;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(15,2147483647))
_JmGeneralAttributePersistence_Type.__name__=_D
_JmGeneralAttributePersistence_Object=MibTableColumn
jmGeneralAttributePersistence=_JmGeneralAttributePersistence_Object((1,3,6,1,4,1,2699,1,1,1,1,1,1,6),_JmGeneralAttributePersistence_Type())
jmGeneralAttributePersistence.setMaxAccess(_C)
if mibBuilder.loadTexts:jmGeneralAttributePersistence.setStatus(_A)
if mibBuilder.loadTexts:jmGeneralAttributePersistence.setUnits(_K)
class _JmGeneralJobSetName_Type(JmUTF8StringTC):defaultHexValue='';subtypeSpec=JmUTF8StringTC.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_JmGeneralJobSetName_Type.__name__=_L
_JmGeneralJobSetName_Object=MibTableColumn
jmGeneralJobSetName=_JmGeneralJobSetName_Object((1,3,6,1,4,1,2699,1,1,1,1,1,1,7),_JmGeneralJobSetName_Type())
jmGeneralJobSetName.setMaxAccess(_C)
if mibBuilder.loadTexts:jmGeneralJobSetName.setStatus(_A)
_JmJobID_ObjectIdentity=ObjectIdentity
jmJobID=_JmJobID_ObjectIdentity((1,3,6,1,4,1,2699,1,1,1,2))
_JmJobIDTable_Object=MibTable
jmJobIDTable=_JmJobIDTable_Object((1,3,6,1,4,1,2699,1,1,1,2,1))
if mibBuilder.loadTexts:jmJobIDTable.setStatus(_A)
_JmJobIDEntry_Object=MibTableRow
jmJobIDEntry=_JmJobIDEntry_Object((1,3,6,1,4,1,2699,1,1,1,2,1,1))
jmJobIDEntry.setIndexNames((0,_B,_M))
if mibBuilder.loadTexts:jmJobIDEntry.setStatus(_A)
class _JmJobSubmissionID_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(48,48));fixedLength=48
_JmJobSubmissionID_Type.__name__=_I
_JmJobSubmissionID_Object=MibTableColumn
jmJobSubmissionID=_JmJobSubmissionID_Object((1,3,6,1,4,1,2699,1,1,1,2,1,1,1),_JmJobSubmissionID_Type())
jmJobSubmissionID.setMaxAccess(_G)
if mibBuilder.loadTexts:jmJobSubmissionID.setStatus(_A)
class _JmJobIDJobSetIndex_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,32767))
_JmJobIDJobSetIndex_Type.__name__=_D
_JmJobIDJobSetIndex_Object=MibTableColumn
jmJobIDJobSetIndex=_JmJobIDJobSetIndex_Object((1,3,6,1,4,1,2699,1,1,1,2,1,1,2),_JmJobIDJobSetIndex_Type())
jmJobIDJobSetIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:jmJobIDJobSetIndex.setStatus(_A)
class _JmJobIDJobIndex_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_JmJobIDJobIndex_Type.__name__=_D
_JmJobIDJobIndex_Object=MibTableColumn
jmJobIDJobIndex=_JmJobIDJobIndex_Object((1,3,6,1,4,1,2699,1,1,1,2,1,1,3),_JmJobIDJobIndex_Type())
jmJobIDJobIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:jmJobIDJobIndex.setStatus(_A)
_JmJob_ObjectIdentity=ObjectIdentity
jmJob=_JmJob_ObjectIdentity((1,3,6,1,4,1,2699,1,1,1,3))
_JmJobTable_Object=MibTable
jmJobTable=_JmJobTable_Object((1,3,6,1,4,1,2699,1,1,1,3,1))
if mibBuilder.loadTexts:jmJobTable.setStatus(_A)
_JmJobEntry_Object=MibTableRow
jmJobEntry=_JmJobEntry_Object((1,3,6,1,4,1,2699,1,1,1,3,1,1))
jmJobEntry.setIndexNames((0,_B,_H),(0,_B,_J))
if mibBuilder.loadTexts:jmJobEntry.setStatus(_A)
class _JmJobIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_JmJobIndex_Type.__name__=_D
_JmJobIndex_Object=MibTableColumn
jmJobIndex=_JmJobIndex_Object((1,3,6,1,4,1,2699,1,1,1,3,1,1,1),_JmJobIndex_Type())
jmJobIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:jmJobIndex.setStatus(_A)
class _JmJobState_Type(JmJobStateTC):defaultValue=2
_JmJobState_Type.__name__=_N
_JmJobState_Object=MibTableColumn
jmJobState=_JmJobState_Object((1,3,6,1,4,1,2699,1,1,1,3,1,1,2),_JmJobState_Type())
jmJobState.setMaxAccess(_C)
if mibBuilder.loadTexts:jmJobState.setStatus(_A)
class _JmJobStateReasons1_Type(JmJobStateReasons1TC):defaultValue=0
_JmJobStateReasons1_Type.__name__=_O
_JmJobStateReasons1_Object=MibTableColumn
jmJobStateReasons1=_JmJobStateReasons1_Object((1,3,6,1,4,1,2699,1,1,1,3,1,1,3),_JmJobStateReasons1_Type())
jmJobStateReasons1.setMaxAccess(_C)
if mibBuilder.loadTexts:jmJobStateReasons1.setStatus(_A)
class _JmNumberOfInterveningJobs_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2,2147483647))
_JmNumberOfInterveningJobs_Type.__name__=_D
_JmNumberOfInterveningJobs_Object=MibTableColumn
jmNumberOfInterveningJobs=_JmNumberOfInterveningJobs_Object((1,3,6,1,4,1,2699,1,1,1,3,1,1,4),_JmNumberOfInterveningJobs_Type())
jmNumberOfInterveningJobs.setMaxAccess(_C)
if mibBuilder.loadTexts:jmNumberOfInterveningJobs.setStatus(_A)
class _JmJobKOctetsPerCopyRequested_Type(Integer32):defaultValue=-2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2,2147483647))
_JmJobKOctetsPerCopyRequested_Type.__name__=_D
_JmJobKOctetsPerCopyRequested_Object=MibTableColumn
jmJobKOctetsPerCopyRequested=_JmJobKOctetsPerCopyRequested_Object((1,3,6,1,4,1,2699,1,1,1,3,1,1,5),_JmJobKOctetsPerCopyRequested_Type())
jmJobKOctetsPerCopyRequested.setMaxAccess(_C)
if mibBuilder.loadTexts:jmJobKOctetsPerCopyRequested.setStatus(_A)
class _JmJobKOctetsProcessed_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2,2147483647))
_JmJobKOctetsProcessed_Type.__name__=_D
_JmJobKOctetsProcessed_Object=MibTableColumn
jmJobKOctetsProcessed=_JmJobKOctetsProcessed_Object((1,3,6,1,4,1,2699,1,1,1,3,1,1,6),_JmJobKOctetsProcessed_Type())
jmJobKOctetsProcessed.setMaxAccess(_C)
if mibBuilder.loadTexts:jmJobKOctetsProcessed.setStatus(_A)
class _JmJobImpressionsPerCopyRequested_Type(Integer32):defaultValue=-2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2,2147483647))
_JmJobImpressionsPerCopyRequested_Type.__name__=_D
_JmJobImpressionsPerCopyRequested_Object=MibTableColumn
jmJobImpressionsPerCopyRequested=_JmJobImpressionsPerCopyRequested_Object((1,3,6,1,4,1,2699,1,1,1,3,1,1,7),_JmJobImpressionsPerCopyRequested_Type())
jmJobImpressionsPerCopyRequested.setMaxAccess(_C)
if mibBuilder.loadTexts:jmJobImpressionsPerCopyRequested.setStatus(_A)
class _JmJobImpressionsCompleted_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2,2147483647))
_JmJobImpressionsCompleted_Type.__name__=_D
_JmJobImpressionsCompleted_Object=MibTableColumn
jmJobImpressionsCompleted=_JmJobImpressionsCompleted_Object((1,3,6,1,4,1,2699,1,1,1,3,1,1,8),_JmJobImpressionsCompleted_Type())
jmJobImpressionsCompleted.setMaxAccess(_C)
if mibBuilder.loadTexts:jmJobImpressionsCompleted.setStatus(_A)
class _JmJobOwner_Type(JmJobStringTC):defaultHexValue='';subtypeSpec=JmJobStringTC.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_JmJobOwner_Type.__name__=_P
_JmJobOwner_Object=MibTableColumn
jmJobOwner=_JmJobOwner_Object((1,3,6,1,4,1,2699,1,1,1,3,1,1,9),_JmJobOwner_Type())
jmJobOwner.setMaxAccess(_C)
if mibBuilder.loadTexts:jmJobOwner.setStatus(_A)
_JmAttribute_ObjectIdentity=ObjectIdentity
jmAttribute=_JmAttribute_ObjectIdentity((1,3,6,1,4,1,2699,1,1,1,4))
_JmAttributeTable_Object=MibTable
jmAttributeTable=_JmAttributeTable_Object((1,3,6,1,4,1,2699,1,1,1,4,1))
if mibBuilder.loadTexts:jmAttributeTable.setStatus(_A)
_JmAttributeEntry_Object=MibTableRow
jmAttributeEntry=_JmAttributeEntry_Object((1,3,6,1,4,1,2699,1,1,1,4,1,1))
jmAttributeEntry.setIndexNames((0,_B,_H),(0,_B,_J),(0,_B,_Q),(0,_B,_R))
if mibBuilder.loadTexts:jmAttributeEntry.setStatus(_A)
_JmAttributeTypeIndex_Type=JmAttributeTypeTC
_JmAttributeTypeIndex_Object=MibTableColumn
jmAttributeTypeIndex=_JmAttributeTypeIndex_Object((1,3,6,1,4,1,2699,1,1,1,4,1,1,1),_JmAttributeTypeIndex_Type())
jmAttributeTypeIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:jmAttributeTypeIndex.setStatus(_A)
class _JmAttributeInstanceIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32767))
_JmAttributeInstanceIndex_Type.__name__=_D
_JmAttributeInstanceIndex_Object=MibTableColumn
jmAttributeInstanceIndex=_JmAttributeInstanceIndex_Object((1,3,6,1,4,1,2699,1,1,1,4,1,1,2),_JmAttributeInstanceIndex_Type())
jmAttributeInstanceIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:jmAttributeInstanceIndex.setStatus(_A)
class _JmAttributeValueAsInteger_Type(Integer32):defaultValue=-2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2,2147483647))
_JmAttributeValueAsInteger_Type.__name__=_D
_JmAttributeValueAsInteger_Object=MibTableColumn
jmAttributeValueAsInteger=_JmAttributeValueAsInteger_Object((1,3,6,1,4,1,2699,1,1,1,4,1,1,3),_JmAttributeValueAsInteger_Type())
jmAttributeValueAsInteger.setMaxAccess(_C)
if mibBuilder.loadTexts:jmAttributeValueAsInteger.setStatus(_A)
class _JmAttributeValueAsOctets_Type(OctetString):defaultHexValue='';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_JmAttributeValueAsOctets_Type.__name__=_I
_JmAttributeValueAsOctets_Object=MibTableColumn
jmAttributeValueAsOctets=_JmAttributeValueAsOctets_Object((1,3,6,1,4,1,2699,1,1,1,4,1,1,4),_JmAttributeValueAsOctets_Type())
jmAttributeValueAsOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:jmAttributeValueAsOctets.setStatus(_A)
_JobmonMIBNotifications_ObjectIdentity=ObjectIdentity
jobmonMIBNotifications=_JobmonMIBNotifications_ObjectIdentity((1,3,6,1,4,1,2699,1,1,2))
_JmMIBConformance_ObjectIdentity=ObjectIdentity
jmMIBConformance=_JmMIBConformance_ObjectIdentity((1,3,6,1,4,1,2699,1,1,3))
_JmMIBGroups_ObjectIdentity=ObjectIdentity
jmMIBGroups=_JmMIBGroups_ObjectIdentity((1,3,6,1,4,1,2699,1,1,3,2))
jmGeneralGroup=ObjectGroup((1,3,6,1,4,1,2699,1,1,3,2,1))
jmGeneralGroup.setObjects(*((_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X)))
if mibBuilder.loadTexts:jmGeneralGroup.setStatus(_A)
jmJobIDGroup=ObjectGroup((1,3,6,1,4,1,2699,1,1,3,2,2))
jmJobIDGroup.setObjects(*((_B,_Y),(_B,_Z)))
if mibBuilder.loadTexts:jmJobIDGroup.setStatus(_A)
jmJobGroup=ObjectGroup((1,3,6,1,4,1,2699,1,1,3,2,3))
jmJobGroup.setObjects(*((_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h)))
if mibBuilder.loadTexts:jmJobGroup.setStatus(_A)
jmAttributeGroup=ObjectGroup((1,3,6,1,4,1,2699,1,1,3,2,4))
jmAttributeGroup.setObjects(*((_B,_i),(_B,_j)))
if mibBuilder.loadTexts:jmAttributeGroup.setStatus(_A)
jmMIBCompliance=ModuleCompliance((1,3,6,1,4,1,2699,1,1,3,1))
jmMIBCompliance.setObjects(*((_B,_k),(_B,_l),(_B,_m),(_B,_n)))
if mibBuilder.loadTexts:jmMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{_L:JmUTF8StringTC,_P:JmJobStringTC,'JmNaturalLanguageTagTC':JmNaturalLanguageTagTC,'JmTimeStampTC':JmTimeStampTC,'JmJobSourcePlatformTypeTC':JmJobSourcePlatformTypeTC,'JmFinishingTC':JmFinishingTC,'JmPrintQualityTC':JmPrintQualityTC,'JmPrinterResolutionTC':JmPrinterResolutionTC,'JmTonerEconomyTC':JmTonerEconomyTC,'JmBooleanTC':JmBooleanTC,'JmMediumTypeTC':JmMediumTypeTC,'JmJobCollationTypeTC':JmJobCollationTypeTC,'JmJobSubmissionIDTypeTC':JmJobSubmissionIDTypeTC,_N:JmJobStateTC,'JmAttributeTypeTC':JmAttributeTypeTC,'JmJobServiceTypesTC':JmJobServiceTypesTC,_O:JmJobStateReasons1TC,'JmJobStateReasons2TC':JmJobStateReasons2TC,'JmJobStateReasons3TC':JmJobStateReasons3TC,'JmJobStateReasons4TC':JmJobStateReasons4TC,'jobmonMIB':jobmonMIB,'jobmonMIBObjects':jobmonMIBObjects,'jmGeneral':jmGeneral,'jmGeneralTable':jmGeneralTable,'jmGeneralEntry':jmGeneralEntry,_H:jmGeneralJobSetIndex,_S:jmGeneralNumberOfActiveJobs,_T:jmGeneralOldestActiveJobIndex,_U:jmGeneralNewestActiveJobIndex,_V:jmGeneralJobPersistence,_W:jmGeneralAttributePersistence,_X:jmGeneralJobSetName,'jmJobID':jmJobID,'jmJobIDTable':jmJobIDTable,'jmJobIDEntry':jmJobIDEntry,_M:jmJobSubmissionID,_Y:jmJobIDJobSetIndex,_Z:jmJobIDJobIndex,'jmJob':jmJob,'jmJobTable':jmJobTable,'jmJobEntry':jmJobEntry,_J:jmJobIndex,_a:jmJobState,_b:jmJobStateReasons1,_c:jmNumberOfInterveningJobs,_d:jmJobKOctetsPerCopyRequested,_e:jmJobKOctetsProcessed,_f:jmJobImpressionsPerCopyRequested,_g:jmJobImpressionsCompleted,_h:jmJobOwner,'jmAttribute':jmAttribute,'jmAttributeTable':jmAttributeTable,'jmAttributeEntry':jmAttributeEntry,_Q:jmAttributeTypeIndex,_R:jmAttributeInstanceIndex,_i:jmAttributeValueAsInteger,_j:jmAttributeValueAsOctets,'jobmonMIBNotifications':jobmonMIBNotifications,'jmMIBConformance':jmMIBConformance,'jmMIBCompliance':jmMIBCompliance,'jmMIBGroups':jmMIBGroups,_k:jmGeneralGroup,_l:jmJobIDGroup,_m:jmJobGroup,_n:jmAttributeGroup})