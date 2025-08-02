_i='dsShdslLineParamsTable60'
_h='dsShdslLineParamsTable55'
_g='dsShdslLineParamsTable50'
_f='dsShdslLineParamsTable45'
_e='dsShdslLineParamsTable40'
_d='dsShdslLineParamsTable35'
_c='dsShdslLineParamsTable30'
_b='dsShdslLineParamsTable25'
_a='dsShdslLineParamsTable20'
_Z='dsShdslLineParamsTable15'
_Y='inSync'
_X='outOfSync'
_W='DisplayString'
_V='Unsigned32'
_U='dsShdslLineParamsTable7'
_T='dsShdslLineParamsTable0'
_S='dsShdslLineParamsTable10'
_R='positive'
_Q='negative'
_P='dsShdslLineParamsTable6'
_O='dsShdslLineParamsTable4'
_N='dsShdslLineParamsTable3'
_M='dsShdslLineParamsTable2'
_L='ifIndex'
_K='IF-MIB'
_J='dsShdslLineParamsTable1'
_I='default'
_H='dsShdslLineParamsTable5'
_G='OctetString'
_F='enable'
_E='disable'
_D='read-only'
_C='read-write'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_G,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dasanMgmt,=mibBuilder.importSymbols('DASAN-SMI','dasanMgmt')
ifIndex,=mibBuilder.importSymbols(_K,_L)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,mib_2=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_V,'iso','mib-2')
DisplayString,PhysAddress,RowStatus,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_W,'PhysAddress','RowStatus','TextualConvention','TimeStamp','TruthValue')
dasanShdslMIB=ModuleIdentity((1,3,6,1,4,1,6296,9,6))
_DasanShdslLineMIB_ObjectIdentity=ObjectIdentity
dasanShdslLineMIB=_DasanShdslLineMIB_ObjectIdentity((1,3,6,1,4,1,6296,9,6,1))
_DasanShdslMIBObjects_ObjectIdentity=ObjectIdentity
dasanShdslMIBObjects=_DasanShdslMIBObjects_ObjectIdentity((1,3,6,1,4,1,6296,9,6,1,1))
_DsShdslCapabilityGroup_ObjectIdentity=ObjectIdentity
dsShdslCapabilityGroup=_DsShdslCapabilityGroup_ObjectIdentity((1,3,6,1,4,1,6296,9,6,1,1,1))
class _DsShdslCapabilityLineTxCap_Type(Bits):namedValues=NamedValues(*(('region1',0),('region2',1)))
_DsShdslCapabilityLineTxCap_Type.__name__='Bits'
_DsShdslCapabilityLineTxCap_Object=MibScalar
dsShdslCapabilityLineTxCap=_DsShdslCapabilityLineTxCap_Object((1,3,6,1,4,1,6296,9,6,1,1,1,1),_DsShdslCapabilityLineTxCap_Type())
dsShdslCapabilityLineTxCap.setMaxAccess(_D)
if mibBuilder.loadTexts:dsShdslCapabilityLineTxCap.setStatus(_A)
_DsShdslLineStatusTable_Object=MibTable
dsShdslLineStatusTable=_DsShdslLineStatusTable_Object((1,3,6,1,4,1,6296,9,6,1,1,2))
if mibBuilder.loadTexts:dsShdslLineStatusTable.setStatus(_A)
_DsShdslLineStatusEntry_Object=MibTableRow
dsShdslLineStatusEntry=_DsShdslLineStatusEntry_Object((1,3,6,1,4,1,6296,9,6,1,1,2,1))
dsShdslLineStatusEntry.setIndexNames((0,_K,_L))
if mibBuilder.loadTexts:dsShdslLineStatusEntry.setStatus(_A)
class _DsShdslOpState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,8,9,16,20,24,26,27,29,128,130,131,133,138,139,142,143,144,145,146)));namedValues=NamedValues(*(('idle',0),('data',1),('bootupLoad',8),('bootupLoadDone',9),('handshake',16),('pmms',20),('training',24),('framerGearShift',26),('framerManualReset',27),('silence',29),('analogLb',128),('rmtFramerLb',130),('digitalLb',131),('spectrumTest',133),('selt',138),('pSDTest',139),('lclFramerLb',142),('interfaceLb',143),('bertTest',144),('analogLbBertTest',145),('digLbBertTest',146)))
_DsShdslOpState_Type.__name__=_B
_DsShdslOpState_Object=MibTableColumn
dsShdslOpState=_DsShdslOpState_Object((1,3,6,1,4,1,6296,9,6,1,1,2,1,1),_DsShdslOpState_Type())
dsShdslOpState.setMaxAccess(_D)
if mibBuilder.loadTexts:dsShdslOpState.setStatus(_A)
class _DsShdslStartProgress_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,4,7,8,55,56,57,64,65,66,67,68,69,70,71,72,73,74,75,113,114,115,116,117,118,128,129,130,131,144,145,146,147)));namedValues=NamedValues(*(('noActivity',0),('preActivation',1),('activation',4),('checkBitrate',7),('pmmsChkComnRate',8),('transmitCr',55),('transmitSc',56),('transmitSr',57),('coLineAgc',64),('cpLineAgc',65),('fdEcTrain',66),('equalizerTrain',67),('tipRingAligned',68),('transmitTc',69),('receiveTr',70),('transmitFc1',71),('transmitFc2',72),('receiveTc',73),('transmitTr',74),('receiveFc',75),('spectTestOk',113),('albTestOk',114),('dlbTestOk',115),('crcFail',116),('framerSyncFail',117),('snrMarginFail',118),('loadCppa',128),('loadCptrain',129),('loadCptom',130),('loadCpdm',131),('loadCopa',144),('loadCotrain',145),('loadCotom',146),('loadCodm',147)))
_DsShdslStartProgress_Type.__name__=_B
_DsShdslStartProgress_Object=MibTableColumn
dsShdslStartProgress=_DsShdslStartProgress_Object((1,3,6,1,4,1,6296,9,6,1,1,2,1,2),_DsShdslStartProgress_Type())
dsShdslStartProgress.setMaxAccess(_D)
if mibBuilder.loadTexts:dsShdslStartProgress.setStatus(_A)
class _DsShdslFwRelease_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_DsShdslFwRelease_Type.__name__=_G
_DsShdslFwRelease_Object=MibTableColumn
dsShdslFwRelease=_DsShdslFwRelease_Object((1,3,6,1,4,1,6296,9,6,1,1,2,1,3),_DsShdslFwRelease_Type())
dsShdslFwRelease.setMaxAccess(_D)
if mibBuilder.loadTexts:dsShdslFwRelease.setStatus(_A)
class _DsShdslLineSwap_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('unswapped',0),('swapped',1)))
_DsShdslLineSwap_Type.__name__=_B
_DsShdslLineSwap_Object=MibTableColumn
dsShdslLineSwap=_DsShdslLineSwap_Object((1,3,6,1,4,1,6296,9,6,1,1,2,1,4),_DsShdslLineSwap_Type())
dsShdslLineSwap.setMaxAccess(_D)
if mibBuilder.loadTexts:dsShdslLineSwap.setStatus(_A)
class _DsShdslRmtCountryCode_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_DsShdslRmtCountryCode_Type.__name__=_G
_DsShdslRmtCountryCode_Object=MibTableColumn
dsShdslRmtCountryCode=_DsShdslRmtCountryCode_Object((1,3,6,1,4,1,6296,9,6,1,1,2,1,5),_DsShdslRmtCountryCode_Type())
dsShdslRmtCountryCode.setMaxAccess(_D)
if mibBuilder.loadTexts:dsShdslRmtCountryCode.setStatus(_A)
_DsShdslRmtEncoderA_Type=Integer32
_DsShdslRmtEncoderA_Object=MibTableColumn
dsShdslRmtEncoderA=_DsShdslRmtEncoderA_Object((1,3,6,1,4,1,6296,9,6,1,1,2,1,6),_DsShdslRmtEncoderA_Type())
dsShdslRmtEncoderA.setMaxAccess(_D)
if mibBuilder.loadTexts:dsShdslRmtEncoderA.setStatus(_A)
_DsShdslRmtEncoderB_Type=Integer32
_DsShdslRmtEncoderB_Object=MibTableColumn
dsShdslRmtEncoderB=_DsShdslRmtEncoderB_Object((1,3,6,1,4,1,6296,9,6,1,1,2,1,7),_DsShdslRmtEncoderB_Type())
dsShdslRmtEncoderB.setMaxAccess(_D)
if mibBuilder.loadTexts:dsShdslRmtEncoderB.setStatus(_A)
class _DsShdslRmtProviderCode_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_DsShdslRmtProviderCode_Type.__name__=_G
_DsShdslRmtProviderCode_Object=MibTableColumn
dsShdslRmtProviderCode=_DsShdslRmtProviderCode_Object((1,3,6,1,4,1,6296,9,6,1,1,2,1,8),_DsShdslRmtProviderCode_Type())
dsShdslRmtProviderCode.setMaxAccess(_D)
if mibBuilder.loadTexts:dsShdslRmtProviderCode.setStatus(_A)
_DsShdslLocDetect_Type=Integer32
_DsShdslLocDetect_Object=MibTableColumn
dsShdslLocDetect=_DsShdslLocDetect_Object((1,3,6,1,4,1,6296,9,6,1,1,2,1,9),_DsShdslLocDetect_Type())
dsShdslLocDetect.setMaxAccess(_D)
if mibBuilder.loadTexts:dsShdslLocDetect.setStatus(_A)
_DsShdslTxPower_Type=Integer32
_DsShdslTxPower_Object=MibTableColumn
dsShdslTxPower=_DsShdslTxPower_Object((1,3,6,1,4,1,6296,9,6,1,1,2,1,10),_DsShdslTxPower_Type())
dsShdslTxPower.setMaxAccess(_D)
if mibBuilder.loadTexts:dsShdslTxPower.setStatus(_A)
class _DsShdslFramerSync_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_X,0),(_Y,1)))
_DsShdslFramerSync_Type.__name__=_B
_DsShdslFramerSync_Object=MibTableColumn
dsShdslFramerSync=_DsShdslFramerSync_Object((1,3,6,1,4,1,6296,9,6,1,1,2,1,11),_DsShdslFramerSync_Type())
dsShdslFramerSync.setMaxAccess(_D)
if mibBuilder.loadTexts:dsShdslFramerSync.setStatus(_A)
_DsShdslRmtTomData_Type=Integer32
_DsShdslRmtTomData_Object=MibTableColumn
dsShdslRmtTomData=_DsShdslRmtTomData_Object((1,3,6,1,4,1,6296,9,6,1,1,2,1,12),_DsShdslRmtTomData_Type())
dsShdslRmtTomData.setMaxAccess(_D)
if mibBuilder.loadTexts:dsShdslRmtTomData.setStatus(_A)
_DsShdslDriftAlarm_Type=Integer32
_DsShdslDriftAlarm_Object=MibTableColumn
dsShdslDriftAlarm=_DsShdslDriftAlarm_Object((1,3,6,1,4,1,6296,9,6,1,1,2,1,13),_DsShdslDriftAlarm_Type())
dsShdslDriftAlarm.setMaxAccess(_D)
if mibBuilder.loadTexts:dsShdslDriftAlarm.setStatus(_A)
_DsShdslReceiverGain_Type=Integer32
_DsShdslReceiverGain_Object=MibTableColumn
dsShdslReceiverGain=_DsShdslReceiverGain_Object((1,3,6,1,4,1,6296,9,6,1,1,2,1,14),_DsShdslReceiverGain_Type())
dsShdslReceiverGain.setMaxAccess(_D)
if mibBuilder.loadTexts:dsShdslReceiverGain.setStatus(_A)
class _DsShdslBertError_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,64,128)));namedValues=NamedValues(*((_X,0),('framedSync',64),('unframedSync',128)))
_DsShdslBertError_Type.__name__=_B
_DsShdslBertError_Object=MibTableColumn
dsShdslBertError=_DsShdslBertError_Object((1,3,6,1,4,1,6296,9,6,1,1,2,1,15),_DsShdslBertError_Type())
dsShdslBertError.setMaxAccess(_D)
if mibBuilder.loadTexts:dsShdslBertError.setStatus(_A)
class _DsShdslFramerOHAndDefects_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,10))
_DsShdslFramerOHAndDefects_Type.__name__=_G
_DsShdslFramerOHAndDefects_Object=MibTableColumn
dsShdslFramerOHAndDefects=_DsShdslFramerOHAndDefects_Object((1,3,6,1,4,1,6296,9,6,1,1,2,1,16),_DsShdslFramerOHAndDefects_Type())
dsShdslFramerOHAndDefects.setMaxAccess(_D)
if mibBuilder.loadTexts:dsShdslFramerOHAndDefects.setStatus(_A)
_DsShdslRmtFwVersion_Type=Integer32
_DsShdslRmtFwVersion_Object=MibTableColumn
dsShdslRmtFwVersion=_DsShdslRmtFwVersion_Object((1,3,6,1,4,1,6296,9,6,1,1,2,1,17),_DsShdslRmtFwVersion_Type())
dsShdslRmtFwVersion.setMaxAccess(_D)
if mibBuilder.loadTexts:dsShdslRmtFwVersion.setStatus(_A)
class _DsShdslUtopiaCellDelineation_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,160,240)));namedValues=NamedValues(*((_Y,1),('preSync',160),('hunt',240)))
_DsShdslUtopiaCellDelineation_Type.__name__=_B
_DsShdslUtopiaCellDelineation_Object=MibTableColumn
dsShdslUtopiaCellDelineation=_DsShdslUtopiaCellDelineation_Object((1,3,6,1,4,1,6296,9,6,1,1,2,1,18),_DsShdslUtopiaCellDelineation_Type())
dsShdslUtopiaCellDelineation.setMaxAccess(_D)
if mibBuilder.loadTexts:dsShdslUtopiaCellDelineation.setStatus(_A)
_DsShdslUtopiaRxCellCnt_Type=Integer32
_DsShdslUtopiaRxCellCnt_Object=MibTableColumn
dsShdslUtopiaRxCellCnt=_DsShdslUtopiaRxCellCnt_Object((1,3,6,1,4,1,6296,9,6,1,1,2,1,19),_DsShdslUtopiaRxCellCnt_Type())
dsShdslUtopiaRxCellCnt.setMaxAccess(_D)
if mibBuilder.loadTexts:dsShdslUtopiaRxCellCnt.setStatus(_A)
_DsShdslUtopiaCellDropCnt_Type=Integer32
_DsShdslUtopiaCellDropCnt_Object=MibTableColumn
dsShdslUtopiaCellDropCnt=_DsShdslUtopiaCellDropCnt_Object((1,3,6,1,4,1,6296,9,6,1,1,2,1,20),_DsShdslUtopiaCellDropCnt_Type())
dsShdslUtopiaCellDropCnt.setMaxAccess(_D)
if mibBuilder.loadTexts:dsShdslUtopiaCellDropCnt.setStatus(_A)
_DsShdslUtopiaRxHecErrorCnt_Type=Integer32
_DsShdslUtopiaRxHecErrorCnt_Object=MibTableColumn
dsShdslUtopiaRxHecErrorCnt=_DsShdslUtopiaRxHecErrorCnt_Object((1,3,6,1,4,1,6296,9,6,1,1,2,1,21),_DsShdslUtopiaRxHecErrorCnt_Type())
dsShdslUtopiaRxHecErrorCnt.setMaxAccess(_D)
if mibBuilder.loadTexts:dsShdslUtopiaRxHecErrorCnt.setStatus(_A)
_DsShdslUtopiaTxCellCnt_Type=Integer32
_DsShdslUtopiaTxCellCnt_Object=MibTableColumn
dsShdslUtopiaTxCellCnt=_DsShdslUtopiaTxCellCnt_Object((1,3,6,1,4,1,6296,9,6,1,1,2,1,22),_DsShdslUtopiaTxCellCnt_Type())
dsShdslUtopiaTxCellCnt.setMaxAccess(_D)
if mibBuilder.loadTexts:dsShdslUtopiaTxCellCnt.setStatus(_A)
_DsShdslRmtNsfCusId_Type=Integer32
_DsShdslRmtNsfCusId_Object=MibTableColumn
dsShdslRmtNsfCusId=_DsShdslRmtNsfCusId_Object((1,3,6,1,4,1,6296,9,6,1,1,2,1,23),_DsShdslRmtNsfCusId_Type())
dsShdslRmtNsfCusId.setMaxAccess(_D)
if mibBuilder.loadTexts:dsShdslRmtNsfCusId.setStatus(_A)
class _DsShdslRmtNsfCusData_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,4))
_DsShdslRmtNsfCusData_Type.__name__=_G
_DsShdslRmtNsfCusData_Object=MibTableColumn
dsShdslRmtNsfCusData=_DsShdslRmtNsfCusData_Object((1,3,6,1,4,1,6296,9,6,1,1,2,1,24),_DsShdslRmtNsfCusData_Type())
dsShdslRmtNsfCusData.setMaxAccess(_D)
if mibBuilder.loadTexts:dsShdslRmtNsfCusData.setStatus(_A)
class _DsShdslLocalHandshake_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,52))
_DsShdslLocalHandshake_Type.__name__=_G
_DsShdslLocalHandshake_Object=MibTableColumn
dsShdslLocalHandshake=_DsShdslLocalHandshake_Object((1,3,6,1,4,1,6296,9,6,1,1,2,1,25),_DsShdslLocalHandshake_Type())
dsShdslLocalHandshake.setMaxAccess(_D)
if mibBuilder.loadTexts:dsShdslLocalHandshake.setStatus(_A)
class _DsShdslRemoteHandshake_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,52))
_DsShdslRemoteHandshake_Type.__name__=_G
_DsShdslRemoteHandshake_Object=MibTableColumn
dsShdslRemoteHandshake=_DsShdslRemoteHandshake_Object((1,3,6,1,4,1,6296,9,6,1,1,2,1,26),_DsShdslRemoteHandshake_Type())
dsShdslRemoteHandshake.setMaxAccess(_D)
if mibBuilder.loadTexts:dsShdslRemoteHandshake.setStatus(_A)
class _DsShdslActualHandshake_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,52))
_DsShdslActualHandshake_Type.__name__=_G
_DsShdslActualHandshake_Object=MibTableColumn
dsShdslActualHandshake=_DsShdslActualHandshake_Object((1,3,6,1,4,1,6296,9,6,1,1,2,1,27),_DsShdslActualHandshake_Type())
dsShdslActualHandshake.setMaxAccess(_D)
if mibBuilder.loadTexts:dsShdslActualHandshake.setStatus(_A)
_DsShdslRmtTxPower_Type=Integer32
_DsShdslRmtTxPower_Object=MibTableColumn
dsShdslRmtTxPower=_DsShdslRmtTxPower_Object((1,3,6,1,4,1,6296,9,6,1,1,2,1,28),_DsShdslRmtTxPower_Type())
dsShdslRmtTxPower.setMaxAccess(_D)
if mibBuilder.loadTexts:dsShdslRmtTxPower.setStatus(_A)
class _DsShdslRmtPowerBackoff_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,32768)));namedValues=NamedValues(*((_F,0),(_E,32768)))
_DsShdslRmtPowerBackoff_Type.__name__=_B
_DsShdslRmtPowerBackoff_Object=MibTableColumn
dsShdslRmtPowerBackoff=_DsShdslRmtPowerBackoff_Object((1,3,6,1,4,1,6296,9,6,1,1,2,1,29),_DsShdslRmtPowerBackoff_Type())
dsShdslRmtPowerBackoff.setMaxAccess(_D)
if mibBuilder.loadTexts:dsShdslRmtPowerBackoff.setStatus(_A)
_DsShdslAutoRetrainCount_Type=Integer32
_DsShdslAutoRetrainCount_Object=MibTableColumn
dsShdslAutoRetrainCount=_DsShdslAutoRetrainCount_Object((1,3,6,1,4,1,6296,9,6,1,1,2,1,30),_DsShdslAutoRetrainCount_Type())
dsShdslAutoRetrainCount.setMaxAccess(_D)
if mibBuilder.loadTexts:dsShdslAutoRetrainCount.setStatus(_A)
class _DsShdslEocState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*(('online',0),('discovery',1),('inventory',2),('configuration',3),('cmdInProgress',4)))
_DsShdslEocState_Type.__name__=_B
_DsShdslEocState_Object=MibTableColumn
dsShdslEocState=_DsShdslEocState_Object((1,3,6,1,4,1,6296,9,6,1,1,2,1,31),_DsShdslEocState_Type())
dsShdslEocState.setMaxAccess(_D)
if mibBuilder.loadTexts:dsShdslEocState.setStatus(_A)
class _DsShdslFramerOneSecondCnt_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,6))
_DsShdslFramerOneSecondCnt_Type.__name__=_G
_DsShdslFramerOneSecondCnt_Object=MibTableColumn
dsShdslFramerOneSecondCnt=_DsShdslFramerOneSecondCnt_Object((1,3,6,1,4,1,6296,9,6,1,1,2,1,32),_DsShdslFramerOneSecondCnt_Type())
dsShdslFramerOneSecondCnt.setMaxAccess(_D)
if mibBuilder.loadTexts:dsShdslFramerOneSecondCnt.setStatus(_A)
class _DsShdslNtrFault_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('present',0),('absent',1)))
_DsShdslNtrFault_Type.__name__=_B
_DsShdslNtrFault_Object=MibTableColumn
dsShdslNtrFault=_DsShdslNtrFault_Object((1,3,6,1,4,1,6296,9,6,1,1,2,1,33),_DsShdslNtrFault_Type())
dsShdslNtrFault.setMaxAccess(_D)
if mibBuilder.loadTexts:dsShdslNtrFault.setStatus(_A)
class _DsShdslCpeMasterCore_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,16,32,48,64,80,96,112,128)));namedValues=NamedValues(*(('core0',0),('core1',16),('core2',32),('core3',48),('core4',64),('core5',80),('core6',96),('core7',112),('noMasterCore',128)))
_DsShdslCpeMasterCore_Type.__name__=_B
_DsShdslCpeMasterCore_Object=MibTableColumn
dsShdslCpeMasterCore=_DsShdslCpeMasterCore_Object((1,3,6,1,4,1,6296,9,6,1,1,2,1,34),_DsShdslCpeMasterCore_Type())
dsShdslCpeMasterCore.setMaxAccess(_D)
if mibBuilder.loadTexts:dsShdslCpeMasterCore.setStatus(_A)
class _DsShdslParametricTestResult_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('pass',0),('fail',1)))
_DsShdslParametricTestResult_Type.__name__=_B
_DsShdslParametricTestResult_Object=MibTableColumn
dsShdslParametricTestResult=_DsShdslParametricTestResult_Object((1,3,6,1,4,1,6296,9,6,1,1,2,1,35),_DsShdslParametricTestResult_Type())
dsShdslParametricTestResult.setMaxAccess(_D)
if mibBuilder.loadTexts:dsShdslParametricTestResult.setStatus(_A)
class _DsShdslParametricTestArray_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,1024))
_DsShdslParametricTestArray_Type.__name__=_G
_DsShdslParametricTestArray_Object=MibTableColumn
dsShdslParametricTestArray=_DsShdslParametricTestArray_Object((1,3,6,1,4,1,6296,9,6,1,1,2,1,36),_DsShdslParametricTestArray_Type())
dsShdslParametricTestArray.setMaxAccess(_D)
if mibBuilder.loadTexts:dsShdslParametricTestArray.setStatus(_A)
_DsShdslLineParamsTable_Object=MibTable
dsShdslLineParamsTable=_DsShdslLineParamsTable_Object((1,3,6,1,4,1,6296,9,6,1,1,3))
if mibBuilder.loadTexts:dsShdslLineParamsTable.setStatus(_A)
_DsShdslLineParamsEntry_Object=MibTableRow
dsShdslLineParamsEntry=_DsShdslLineParamsEntry_Object((1,3,6,1,4,1,6296,9,6,1,1,3,1))
dsShdslLineParamsEntry.setIndexNames((0,_K,_L))
if mibBuilder.loadTexts:dsShdslLineParamsEntry.setStatus(_A)
class _DsShdslAction_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,2,6,8,17,18,20,25,26,32,33,34,35,36,37,38,45,46,47,48)));namedValues=NamedValues(*(('startUp',0),('abortReq',2),('gearShiftReq',6),('downloadReq',8),('bertStartTxReq',17),('bertStartRxReq',18),('bertStopReq',20),('spectrumDownReq',25),('spectrumUpReq',26),('spectrumTxRxReq',32),('hybridLossTestReq',33),('residualEchoReq',34),('totalEchoReq',35),('nextPsdReq',36),('autoRetrainOnReq',37),('autoRetrainOffReq',38),('propEocOnReq',45),('propEocOffReq',46),('rmtAtmCellStatusReq',47),('rmtFullStatusReq',48)))
_DsShdslAction_Type.__name__=_B
_DsShdslAction_Object=MibTableColumn
dsShdslAction=_DsShdslAction_Object((1,3,6,1,4,1,6296,9,6,1,1,3,1,1),_DsShdslAction_Type())
dsShdslAction.setMaxAccess(_C)
if mibBuilder.loadTexts:dsShdslAction.setStatus(_A)
class _DsShdslMode_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('co',0),('cpe',1)))
_DsShdslMode_Type.__name__=_B
_DsShdslMode_Object=MibTableColumn
dsShdslMode=_DsShdslMode_Object((1,3,6,1,4,1,6296,9,6,1,1,3,1,2),_DsShdslMode_Type())
dsShdslMode.setMaxAccess(_C)
if mibBuilder.loadTexts:dsShdslMode.setStatus(_A)
class _DsShdslPowerScale_Type(Integer32):defaultValue=26112;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(26112));namedValues=NamedValues(('defaultScale',26112))
_DsShdslPowerScale_Type.__name__=_B
_DsShdslPowerScale_Object=MibTableColumn
dsShdslPowerScale=_DsShdslPowerScale_Object((1,3,6,1,4,1,6296,9,6,1,1,3,1,3),_DsShdslPowerScale_Type())
dsShdslPowerScale.setMaxAccess(_C)
if mibBuilder.loadTexts:dsShdslPowerScale.setStatus(_A)
class _DsShdslFramerType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,6,7,8,9)));namedValues=NamedValues(*(('unframed',0),('t1Slotted',1),('e1Slotted',2),('utopiaL2',3),('nx64',6),('serialATM',7),('vC12',8),('iMA',9)))
_DsShdslFramerType_Type.__name__=_B
_DsShdslFramerType_Object=MibTableColumn
dsShdslFramerType=_DsShdslFramerType_Object((1,3,6,1,4,1,6296,9,6,1,1,3,1,4),_DsShdslFramerType_Type())
dsShdslFramerType.setMaxAccess(_D)
if mibBuilder.loadTexts:dsShdslFramerType.setStatus(_A)
class _DsShdslAFEType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(3,4)));namedValues=NamedValues(*(('saturn',3),('saturnLg',4)))
_DsShdslAFEType_Type.__name__=_B
_DsShdslAFEType_Object=MibTableColumn
dsShdslAFEType=_DsShdslAFEType_Object((1,3,6,1,4,1,6296,9,6,1,1,3,1,5),_DsShdslAFEType_Type())
dsShdslAFEType.setMaxAccess(_D)
if mibBuilder.loadTexts:dsShdslAFEType.setStatus(_A)
class _DsShdslEncodeCoeffA_Type(Integer32):defaultValue=366;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(366));namedValues=NamedValues((_I,366))
_DsShdslEncodeCoeffA_Type.__name__=_B
_DsShdslEncodeCoeffA_Object=MibTableColumn
dsShdslEncodeCoeffA=_DsShdslEncodeCoeffA_Object((1,3,6,1,4,1,6296,9,6,1,1,3,1,6),_DsShdslEncodeCoeffA_Type())
dsShdslEncodeCoeffA.setMaxAccess(_C)
if mibBuilder.loadTexts:dsShdslEncodeCoeffA.setStatus(_A)
class _DsShdslEncodeCoeffB_Type(Integer32):defaultValue=817;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(817));namedValues=NamedValues((_I,817))
_DsShdslEncodeCoeffB_Type.__name__=_B
_DsShdslEncodeCoeffB_Object=MibTableColumn
dsShdslEncodeCoeffB=_DsShdslEncodeCoeffB_Object((1,3,6,1,4,1,6296,9,6,1,1,3,1,7),_DsShdslEncodeCoeffB_Type())
dsShdslEncodeCoeffB.setMaxAccess(_C)
if mibBuilder.loadTexts:dsShdslEncodeCoeffB.setStatus(_A)
class _DsShdslTxEOCBufferLen_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(5,10,15,20,25,30,35,40,45,50,55,60)));namedValues=NamedValues(*((_H,5),(_S,10),(_Z,15),(_a,20),(_b,25),(_c,30),(_d,35),(_e,40),(_f,45),(_g,50),(_h,55),(_i,60)))
_DsShdslTxEOCBufferLen_Type.__name__=_B
_DsShdslTxEOCBufferLen_Object=MibTableColumn
dsShdslTxEOCBufferLen=_DsShdslTxEOCBufferLen_Object((1,3,6,1,4,1,6296,9,6,1,1,3,1,8),_DsShdslTxEOCBufferLen_Type())
dsShdslTxEOCBufferLen.setMaxAccess(_C)
if mibBuilder.loadTexts:dsShdslTxEOCBufferLen.setStatus(_A)
class _DsShdslRxEOCBufferLen_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(5,10,15,20,25,30,35,40,45,50,55,60)));namedValues=NamedValues(*((_H,5),(_S,10),(_Z,15),(_a,20),(_b,25),(_c,30),(_d,35),(_e,40),(_f,45),(_g,50),(_h,55),(_i,60)))
_DsShdslRxEOCBufferLen_Type.__name__=_B
_DsShdslRxEOCBufferLen_Object=MibTableColumn
dsShdslRxEOCBufferLen=_DsShdslRxEOCBufferLen_Object((1,3,6,1,4,1,6296,9,6,1,1,3,1,9),_DsShdslRxEOCBufferLen_Type())
dsShdslRxEOCBufferLen.setMaxAccess(_C)
if mibBuilder.loadTexts:dsShdslRxEOCBufferLen.setStatus(_A)
class _DsShdslNTR_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,4)));namedValues=NamedValues(*((_E,1),('refClkIp8k',2),('refClkOp4096k',4)))
_DsShdslNTR_Type.__name__=_B
_DsShdslNTR_Object=MibTableColumn
dsShdslNTR=_DsShdslNTR_Object((1,3,6,1,4,1,6296,9,6,1,1,3,1,10),_DsShdslNTR_Type())
dsShdslNTR.setMaxAccess(_C)
if mibBuilder.loadTexts:dsShdslNTR.setStatus(_A)
class _DsShdslRxUpstreamFrameSync_Type(Integer32):defaultValue=13727
_DsShdslRxUpstreamFrameSync_Type.__name__=_B
_DsShdslRxUpstreamFrameSync_Object=MibTableColumn
dsShdslRxUpstreamFrameSync=_DsShdslRxUpstreamFrameSync_Object((1,3,6,1,4,1,6296,9,6,1,1,3,1,11),_DsShdslRxUpstreamFrameSync_Type())
dsShdslRxUpstreamFrameSync.setMaxAccess(_C)
if mibBuilder.loadTexts:dsShdslRxUpstreamFrameSync.setStatus(_A)
class _DsShdslRxDownstreamFrameSync_Type(Integer32):defaultValue=13727
_DsShdslRxDownstreamFrameSync_Type.__name__=_B
_DsShdslRxDownstreamFrameSync_Object=MibTableColumn
dsShdslRxDownstreamFrameSync=_DsShdslRxDownstreamFrameSync_Object((1,3,6,1,4,1,6296,9,6,1,1,3,1,12),_DsShdslRxDownstreamFrameSync_Type())
dsShdslRxDownstreamFrameSync.setMaxAccess(_C)
if mibBuilder.loadTexts:dsShdslRxDownstreamFrameSync.setStatus(_A)
class _DsShdslRxUpstreamStuffBits_Type(Integer32):defaultValue=15
_DsShdslRxUpstreamStuffBits_Type.__name__=_B
_DsShdslRxUpstreamStuffBits_Object=MibTableColumn
dsShdslRxUpstreamStuffBits=_DsShdslRxUpstreamStuffBits_Object((1,3,6,1,4,1,6296,9,6,1,1,3,1,13),_DsShdslRxUpstreamStuffBits_Type())
dsShdslRxUpstreamStuffBits.setMaxAccess(_C)
if mibBuilder.loadTexts:dsShdslRxUpstreamStuffBits.setStatus(_A)
class _DsShdslRxDownstreamStuffBits_Type(Integer32):defaultValue=15
_DsShdslRxDownstreamStuffBits_Type.__name__=_B
_DsShdslRxDownstreamStuffBits_Object=MibTableColumn
dsShdslRxDownstreamStuffBits=_DsShdslRxDownstreamStuffBits_Object((1,3,6,1,4,1,6296,9,6,1,1,3,1,14),_DsShdslRxDownstreamStuffBits_Type())
dsShdslRxDownstreamStuffBits.setMaxAccess(_C)
if mibBuilder.loadTexts:dsShdslRxDownstreamStuffBits.setStatus(_A)
class _DsShdslInitiate_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_I,0),('co',1),('cpe',2)))
_DsShdslInitiate_Type.__name__=_B
_DsShdslInitiate_Object=MibTableColumn
dsShdslInitiate=_DsShdslInitiate_Object((1,3,6,1,4,1,6296,9,6,1,1,3,1,15),_DsShdslInitiate_Type())
dsShdslInitiate.setMaxAccess(_C)
if mibBuilder.loadTexts:dsShdslInitiate.setStatus(_A)
class _DsShdslFramerRxClockMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*(('slave',2),('internal',3)))
_DsShdslFramerRxClockMode_Type.__name__=_B
_DsShdslFramerRxClockMode_Object=MibTableColumn
dsShdslFramerRxClockMode=_DsShdslFramerRxClockMode_Object((1,3,6,1,4,1,6296,9,6,1,1,3,1,16),_DsShdslFramerRxClockMode_Type())
dsShdslFramerRxClockMode.setMaxAccess(_C)
if mibBuilder.loadTexts:dsShdslFramerRxClockMode.setStatus(_A)
class _DsShdslFramerRxPllMode_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_DsShdslFramerRxPllMode_Type.__name__=_B
_DsShdslFramerRxPllMode_Object=MibTableColumn
dsShdslFramerRxPllMode=_DsShdslFramerRxPllMode_Object((1,3,6,1,4,1,6296,9,6,1,1,3,1,17),_DsShdslFramerRxPllMode_Type())
dsShdslFramerRxPllMode.setMaxAccess(_C)
if mibBuilder.loadTexts:dsShdslFramerRxPllMode.setStatus(_A)
class _DsShdslSerialAtmCiuBufferSize_Type(Integer32):defaultValue=53;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(24,53)));namedValues=NamedValues(*(('dsShdslLineParamsTable24',24),('dsShdslLineParamsTable53',53)))
_DsShdslSerialAtmCiuBufferSize_Type.__name__=_B
_DsShdslSerialAtmCiuBufferSize_Object=MibTableColumn
dsShdslSerialAtmCiuBufferSize=_DsShdslSerialAtmCiuBufferSize_Object((1,3,6,1,4,1,6296,9,6,1,1,3,1,18),_DsShdslSerialAtmCiuBufferSize_Type())
dsShdslSerialAtmCiuBufferSize.setMaxAccess(_C)
if mibBuilder.loadTexts:dsShdslSerialAtmCiuBufferSize.setStatus(_A)
_DsShdslUtopiaL2TxAddress_Type=Integer32
_DsShdslUtopiaL2TxAddress_Object=MibTableColumn
dsShdslUtopiaL2TxAddress=_DsShdslUtopiaL2TxAddress_Object((1,3,6,1,4,1,6296,9,6,1,1,3,1,19),_DsShdslUtopiaL2TxAddress_Type())
dsShdslUtopiaL2TxAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:dsShdslUtopiaL2TxAddress.setStatus(_A)
_DsShdslUtopiaL2RxAddress_Type=Integer32
_DsShdslUtopiaL2RxAddress_Object=MibTableColumn
dsShdslUtopiaL2RxAddress=_DsShdslUtopiaL2RxAddress_Object((1,3,6,1,4,1,6296,9,6,1,1,3,1,20),_DsShdslUtopiaL2RxAddress_Type())
dsShdslUtopiaL2RxAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:dsShdslUtopiaL2RxAddress.setStatus(_A)
class _DsShdslTxFramerPulseDelay_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*((_T,0),(_J,1),(_M,2),(_N,3),(_O,4),(_H,5),(_P,6),(_U,7)))
_DsShdslTxFramerPulseDelay_Type.__name__=_B
_DsShdslTxFramerPulseDelay_Object=MibTableColumn
dsShdslTxFramerPulseDelay=_DsShdslTxFramerPulseDelay_Object((1,3,6,1,4,1,6296,9,6,1,1,3,1,21),_DsShdslTxFramerPulseDelay_Type())
dsShdslTxFramerPulseDelay.setMaxAccess(_C)
if mibBuilder.loadTexts:dsShdslTxFramerPulseDelay.setStatus(_A)
class _DsShdslRxFramerPulseDelay_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*((_T,0),(_J,1),(_M,2),(_N,3),(_O,4),(_H,5),(_P,6),(_U,7)))
_DsShdslRxFramerPulseDelay_Type.__name__=_B
_DsShdslRxFramerPulseDelay_Object=MibTableColumn
dsShdslRxFramerPulseDelay=_DsShdslRxFramerPulseDelay_Object((1,3,6,1,4,1,6296,9,6,1,1,3,1,22),_DsShdslRxFramerPulseDelay_Type())
dsShdslRxFramerPulseDelay.setMaxAccess(_C)
if mibBuilder.loadTexts:dsShdslRxFramerPulseDelay.setStatus(_A)
class _DsShdslMultiFrameMode_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_DsShdslMultiFrameMode_Type.__name__=_B
_DsShdslMultiFrameMode_Object=MibTableColumn
dsShdslMultiFrameMode=_DsShdslMultiFrameMode_Object((1,3,6,1,4,1,6296,9,6,1,1,3,1,23),_DsShdslMultiFrameMode_Type())
dsShdslMultiFrameMode.setMaxAccess(_C)
if mibBuilder.loadTexts:dsShdslMultiFrameMode.setStatus(_A)
class _DsShdslEnable4or6MbpsBitrate_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_DsShdslEnable4or6MbpsBitrate_Type.__name__=_B
_DsShdslEnable4or6MbpsBitrate_Object=MibTableColumn
dsShdslEnable4or6MbpsBitrate=_DsShdslEnable4or6MbpsBitrate_Object((1,3,6,1,4,1,6296,9,6,1,1,3,1,24),_DsShdslEnable4or6MbpsBitrate_Type())
dsShdslEnable4or6MbpsBitrate.setMaxAccess(_C)
if mibBuilder.loadTexts:dsShdslEnable4or6MbpsBitrate.setStatus(_A)
class _DsShdslTomDataWord1_Type(Integer32):defaultValue=0
_DsShdslTomDataWord1_Type.__name__=_B
_DsShdslTomDataWord1_Object=MibTableColumn
dsShdslTomDataWord1=_DsShdslTomDataWord1_Object((1,3,6,1,4,1,6296,9,6,1,1,3,1,25),_DsShdslTomDataWord1_Type())
dsShdslTomDataWord1.setMaxAccess(_C)
if mibBuilder.loadTexts:dsShdslTomDataWord1.setStatus(_A)
class _DsShdslTomDataWord2_Type(Integer32):defaultValue=0
_DsShdslTomDataWord2_Type.__name__=_B
_DsShdslTomDataWord2_Object=MibTableColumn
dsShdslTomDataWord2=_DsShdslTomDataWord2_Object((1,3,6,1,4,1,6296,9,6,1,1,3,1,26),_DsShdslTomDataWord2_Type())
dsShdslTomDataWord2.setMaxAccess(_C)
if mibBuilder.loadTexts:dsShdslTomDataWord2.setStatus(_A)
class _DsShdslTomDataWord3_Type(Integer32):defaultValue=0
_DsShdslTomDataWord3_Type.__name__=_B
_DsShdslTomDataWord3_Object=MibTableColumn
dsShdslTomDataWord3=_DsShdslTomDataWord3_Object((1,3,6,1,4,1,6296,9,6,1,1,3,1,27),_DsShdslTomDataWord3_Type())
dsShdslTomDataWord3.setMaxAccess(_C)
if mibBuilder.loadTexts:dsShdslTomDataWord3.setStatus(_A)
class _DsShdslTomDataWord4_Type(Integer32):defaultValue=0
_DsShdslTomDataWord4_Type.__name__=_B
_DsShdslTomDataWord4_Object=MibTableColumn
dsShdslTomDataWord4=_DsShdslTomDataWord4_Object((1,3,6,1,4,1,6296,9,6,1,1,3,1,28),_DsShdslTomDataWord4_Type())
dsShdslTomDataWord4.setMaxAccess(_C)
if mibBuilder.loadTexts:dsShdslTomDataWord4.setStatus(_A)
class _DsShdslSetReqSilenceMode_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,4)));namedValues=NamedValues(*((_E,0),(_F,4)))
_DsShdslSetReqSilenceMode_Type.__name__=_B
_DsShdslSetReqSilenceMode_Object=MibTableColumn
dsShdslSetReqSilenceMode=_DsShdslSetReqSilenceMode_Object((1,3,6,1,4,1,6296,9,6,1,1,3,1,29),_DsShdslSetReqSilenceMode_Type())
dsShdslSetReqSilenceMode.setMaxAccess(_C)
if mibBuilder.loadTexts:dsShdslSetReqSilenceMode.setStatus(_A)
class _DsShdslSetIndividualRates1_Type(Integer32):defaultValue=65535
_DsShdslSetIndividualRates1_Type.__name__=_B
_DsShdslSetIndividualRates1_Object=MibTableColumn
dsShdslSetIndividualRates1=_DsShdslSetIndividualRates1_Object((1,3,6,1,4,1,6296,9,6,1,1,3,1,30),_DsShdslSetIndividualRates1_Type())
dsShdslSetIndividualRates1.setMaxAccess(_C)
if mibBuilder.loadTexts:dsShdslSetIndividualRates1.setStatus(_A)
class _DsShdslSetIndividualRates2_Type(Integer32):defaultValue=65535
_DsShdslSetIndividualRates2_Type.__name__=_B
_DsShdslSetIndividualRates2_Object=MibTableColumn
dsShdslSetIndividualRates2=_DsShdslSetIndividualRates2_Object((1,3,6,1,4,1,6296,9,6,1,1,3,1,31),_DsShdslSetIndividualRates2_Type())
dsShdslSetIndividualRates2.setMaxAccess(_C)
if mibBuilder.loadTexts:dsShdslSetIndividualRates2.setStatus(_A)
class _DsShdslSetIndividualRates3_Type(Integer32):defaultValue=15
_DsShdslSetIndividualRates3_Type.__name__=_B
_DsShdslSetIndividualRates3_Object=MibTableColumn
dsShdslSetIndividualRates3=_DsShdslSetIndividualRates3_Object((1,3,6,1,4,1,6296,9,6,1,1,3,1,32),_DsShdslSetIndividualRates3_Type())
dsShdslSetIndividualRates3.setMaxAccess(_C)
if mibBuilder.loadTexts:dsShdslSetIndividualRates3.setStatus(_A)
class _DsShdslSatmCellDelineation_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_DsShdslSatmCellDelineation_Type.__name__=_B
_DsShdslSatmCellDelineation_Object=MibTableColumn
dsShdslSatmCellDelineation=_DsShdslSatmCellDelineation_Object((1,3,6,1,4,1,6296,9,6,1,1,3,1,33),_DsShdslSatmCellDelineation_Type())
dsShdslSatmCellDelineation.setMaxAccess(_C)
if mibBuilder.loadTexts:dsShdslSatmCellDelineation.setStatus(_A)
class _DsShdslFramerCellDropOnError_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_DsShdslFramerCellDropOnError_Type.__name__=_B
_DsShdslFramerCellDropOnError_Object=MibTableColumn
dsShdslFramerCellDropOnError=_DsShdslFramerCellDropOnError_Object((1,3,6,1,4,1,6296,9,6,1,1,3,1,34),_DsShdslFramerCellDropOnError_Type())
dsShdslFramerCellDropOnError.setMaxAccess(_C)
if mibBuilder.loadTexts:dsShdslFramerCellDropOnError.setStatus(_A)
class _DsShdslGearShiftType_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_T,0),(_J,1)))
_DsShdslGearShiftType_Type.__name__=_B
_DsShdslGearShiftType_Object=MibTableColumn
dsShdslGearShiftType=_DsShdslGearShiftType_Object((1,3,6,1,4,1,6296,9,6,1,1,3,1,35),_DsShdslGearShiftType_Type())
dsShdslGearShiftType.setMaxAccess(_C)
if mibBuilder.loadTexts:dsShdslGearShiftType.setStatus(_A)
class _DsShdslHsNsf_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_DsShdslHsNsf_Type.__name__=_B
_DsShdslHsNsf_Object=MibTableColumn
dsShdslHsNsf=_DsShdslHsNsf_Object((1,3,6,1,4,1,6296,9,6,1,1,3,1,36),_DsShdslHsNsf_Type())
dsShdslHsNsf.setMaxAccess(_C)
if mibBuilder.loadTexts:dsShdslHsNsf.setStatus(_A)
class _DsShdslHsMaxBitsPerBaud_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('dsShdslLineParamsTable1bits',1),('dsShdslLineParamsTable2bits',2),(_I,3)))
_DsShdslHsMaxBitsPerBaud_Type.__name__=_B
_DsShdslHsMaxBitsPerBaud_Object=MibTableColumn
dsShdslHsMaxBitsPerBaud=_DsShdslHsMaxBitsPerBaud_Object((1,3,6,1,4,1,6296,9,6,1,1,3,1,37),_DsShdslHsMaxBitsPerBaud_Type())
dsShdslHsMaxBitsPerBaud.setMaxAccess(_C)
if mibBuilder.loadTexts:dsShdslHsMaxBitsPerBaud.setStatus(_A)
class _DsShdslHsCusId_Type(Integer32):defaultValue=0
_DsShdslHsCusId_Type.__name__=_B
_DsShdslHsCusId_Object=MibTableColumn
dsShdslHsCusId=_DsShdslHsCusId_Object((1,3,6,1,4,1,6296,9,6,1,1,3,1,38),_DsShdslHsCusId_Type())
dsShdslHsCusId.setMaxAccess(_C)
if mibBuilder.loadTexts:dsShdslHsCusId.setStatus(_A)
class _DsShdslHsCusData0_Type(Integer32):defaultValue=0
_DsShdslHsCusData0_Type.__name__=_B
_DsShdslHsCusData0_Object=MibTableColumn
dsShdslHsCusData0=_DsShdslHsCusData0_Object((1,3,6,1,4,1,6296,9,6,1,1,3,1,39),_DsShdslHsCusData0_Type())
dsShdslHsCusData0.setMaxAccess(_C)
if mibBuilder.loadTexts:dsShdslHsCusData0.setStatus(_A)
class _DsShdslHsCusData1_Type(Integer32):defaultValue=0
_DsShdslHsCusData1_Type.__name__=_B
_DsShdslHsCusData1_Object=MibTableColumn
dsShdslHsCusData1=_DsShdslHsCusData1_Object((1,3,6,1,4,1,6296,9,6,1,1,3,1,40),_DsShdslHsCusData1_Type())
dsShdslHsCusData1.setMaxAccess(_C)
if mibBuilder.loadTexts:dsShdslHsCusData1.setStatus(_A)
class _DsShdslHsAnnexBType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_I,1),('anfp',2),('annexbOrAnfp',3)))
_DsShdslHsAnnexBType_Type.__name__=_B
_DsShdslHsAnnexBType_Object=MibTableColumn
dsShdslHsAnnexBType=_DsShdslHsAnnexBType_Object((1,3,6,1,4,1,6296,9,6,1,1,3,1,41),_DsShdslHsAnnexBType_Type())
dsShdslHsAnnexBType.setMaxAccess(_C)
if mibBuilder.loadTexts:dsShdslHsAnnexBType.setStatus(_A)
class _DsShdslAutoRetrain_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_DsShdslAutoRetrain_Type.__name__=_B
_DsShdslAutoRetrain_Object=MibTableColumn
dsShdslAutoRetrain=_DsShdslAutoRetrain_Object((1,3,6,1,4,1,6296,9,6,1,1,3,1,42),_DsShdslAutoRetrain_Type())
dsShdslAutoRetrain.setMaxAccess(_C)
if mibBuilder.loadTexts:dsShdslAutoRetrain.setStatus(_A)
class _DsShdslArCrcCheck_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_DsShdslArCrcCheck_Type.__name__=_B
_DsShdslArCrcCheck_Object=MibTableColumn
dsShdslArCrcCheck=_DsShdslArCrcCheck_Object((1,3,6,1,4,1,6296,9,6,1,1,3,1,43),_DsShdslArCrcCheck_Type())
dsShdslArCrcCheck.setMaxAccess(_C)
if mibBuilder.loadTexts:dsShdslArCrcCheck.setStatus(_A)
class _DsShdslArFramerSyncCheck_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_DsShdslArFramerSyncCheck_Type.__name__=_B
_DsShdslArFramerSyncCheck_Object=MibTableColumn
dsShdslArFramerSyncCheck=_DsShdslArFramerSyncCheck_Object((1,3,6,1,4,1,6296,9,6,1,1,3,1,44),_DsShdslArFramerSyncCheck_Type())
dsShdslArFramerSyncCheck.setMaxAccess(_C)
if mibBuilder.loadTexts:dsShdslArFramerSyncCheck.setStatus(_A)
class _DsShdslArSnrMarginCheck_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_DsShdslArSnrMarginCheck_Type.__name__=_B
_DsShdslArSnrMarginCheck_Object=MibTableColumn
dsShdslArSnrMarginCheck=_DsShdslArSnrMarginCheck_Object((1,3,6,1,4,1,6296,9,6,1,1,3,1,45),_DsShdslArSnrMarginCheck_Type())
dsShdslArSnrMarginCheck.setMaxAccess(_C)
if mibBuilder.loadTexts:dsShdslArSnrMarginCheck.setStatus(_A)
class _DsShdslArCrcThreshold_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1024))
_DsShdslArCrcThreshold_Type.__name__=_B
_DsShdslArCrcThreshold_Object=MibTableColumn
dsShdslArCrcThreshold=_DsShdslArCrcThreshold_Object((1,3,6,1,4,1,6296,9,6,1,1,3,1,46),_DsShdslArCrcThreshold_Type())
dsShdslArCrcThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:dsShdslArCrcThreshold.setStatus(_A)
class _DsShdslArSnrMarginThreshold_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_J,1),(_M,2),(_N,3),(_O,4),(_H,5),(_P,6)))
_DsShdslArSnrMarginThreshold_Type.__name__=_B
_DsShdslArSnrMarginThreshold_Object=MibTableColumn
dsShdslArSnrMarginThreshold=_DsShdslArSnrMarginThreshold_Object((1,3,6,1,4,1,6296,9,6,1,1,3,1,47),_DsShdslArSnrMarginThreshold_Type())
dsShdslArSnrMarginThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:dsShdslArSnrMarginThreshold.setStatus(_A)
class _DsShdslArRetrainTime_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*((_J,1),(_M,2),(_N,3),(_O,4),(_H,5),(_P,6),(_U,7),('dsShdslLineParamsTable8',8),('dsShdslLineParamsTable9',9),(_S,10)))
_DsShdslArRetrainTime_Type.__name__=_B
_DsShdslArRetrainTime_Object=MibTableColumn
dsShdslArRetrainTime=_DsShdslArRetrainTime_Object((1,3,6,1,4,1,6296,9,6,1,1,3,1,48),_DsShdslArRetrainTime_Type())
dsShdslArRetrainTime.setMaxAccess(_C)
if mibBuilder.loadTexts:dsShdslArRetrainTime.setStatus(_A)
class _DsShdslOpStateTrapEnable_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_DsShdslOpStateTrapEnable_Type.__name__=_B
_DsShdslOpStateTrapEnable_Object=MibTableColumn
dsShdslOpStateTrapEnable=_DsShdslOpStateTrapEnable_Object((1,3,6,1,4,1,6296,9,6,1,1,3,1,49),_DsShdslOpStateTrapEnable_Type())
dsShdslOpStateTrapEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:dsShdslOpStateTrapEnable.setStatus(_A)
class _DsShdslTxFrmrDataClkEdge_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_Q,0),(_R,1)))
_DsShdslTxFrmrDataClkEdge_Type.__name__=_B
_DsShdslTxFrmrDataClkEdge_Object=MibTableColumn
dsShdslTxFrmrDataClkEdge=_DsShdslTxFrmrDataClkEdge_Object((1,3,6,1,4,1,6296,9,6,1,1,3,1,50),_DsShdslTxFrmrDataClkEdge_Type())
dsShdslTxFrmrDataClkEdge.setMaxAccess(_C)
if mibBuilder.loadTexts:dsShdslTxFrmrDataClkEdge.setStatus(_A)
class _DsShdslRxFrmrDataClkEdge_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_Q,0),(_R,1)))
_DsShdslRxFrmrDataClkEdge_Type.__name__=_B
_DsShdslRxFrmrDataClkEdge_Object=MibTableColumn
dsShdslRxFrmrDataClkEdge=_DsShdslRxFrmrDataClkEdge_Object((1,3,6,1,4,1,6296,9,6,1,1,3,1,51),_DsShdslRxFrmrDataClkEdge_Type())
dsShdslRxFrmrDataClkEdge.setMaxAccess(_C)
if mibBuilder.loadTexts:dsShdslRxFrmrDataClkEdge.setStatus(_A)
class _DsShdslTxFrmrPulseClkEdge_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_Q,0),(_R,1)))
_DsShdslTxFrmrPulseClkEdge_Type.__name__=_B
_DsShdslTxFrmrPulseClkEdge_Object=MibTableColumn
dsShdslTxFrmrPulseClkEdge=_DsShdslTxFrmrPulseClkEdge_Object((1,3,6,1,4,1,6296,9,6,1,1,3,1,52),_DsShdslTxFrmrPulseClkEdge_Type())
dsShdslTxFrmrPulseClkEdge.setMaxAccess(_C)
if mibBuilder.loadTexts:dsShdslTxFrmrPulseClkEdge.setStatus(_A)
class _DsShdslRxFrmrPulseClkEdge_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_Q,0),(_R,1)))
_DsShdslRxFrmrPulseClkEdge_Type.__name__=_B
_DsShdslRxFrmrPulseClkEdge_Object=MibTableColumn
dsShdslRxFrmrPulseClkEdge=_DsShdslRxFrmrPulseClkEdge_Object((1,3,6,1,4,1,6296,9,6,1,1,3,1,53),_DsShdslRxFrmrPulseClkEdge_Type())
dsShdslRxFrmrPulseClkEdge.setMaxAccess(_C)
if mibBuilder.loadTexts:dsShdslRxFrmrPulseClkEdge.setStatus(_A)
class _DsShdslTxFrmrPulseLvl_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('low',0),('high',1)))
_DsShdslTxFrmrPulseLvl_Type.__name__=_B
_DsShdslTxFrmrPulseLvl_Object=MibTableColumn
dsShdslTxFrmrPulseLvl=_DsShdslTxFrmrPulseLvl_Object((1,3,6,1,4,1,6296,9,6,1,1,3,1,54),_DsShdslTxFrmrPulseLvl_Type())
dsShdslTxFrmrPulseLvl.setMaxAccess(_C)
if mibBuilder.loadTexts:dsShdslTxFrmrPulseLvl.setStatus(_A)
class _DsShdslRxFrmrPulseLvl_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('low',0),('high',1)))
_DsShdslRxFrmrPulseLvl_Type.__name__=_B
_DsShdslRxFrmrPulseLvl_Object=MibTableColumn
dsShdslRxFrmrPulseLvl=_DsShdslRxFrmrPulseLvl_Object((1,3,6,1,4,1,6296,9,6,1,1,3,1,55),_DsShdslRxFrmrPulseLvl_Type())
dsShdslRxFrmrPulseLvl.setMaxAccess(_C)
if mibBuilder.loadTexts:dsShdslRxFrmrPulseLvl.setStatus(_A)
class _DsShdslUtopiaDataBusWidth_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('tx8Rx8',0),('tx16Rx16',1),('tx16Rx8',2),('tx8Rx16',3)))
_DsShdslUtopiaDataBusWidth_Type.__name__=_B
_DsShdslUtopiaDataBusWidth_Object=MibTableColumn
dsShdslUtopiaDataBusWidth=_DsShdslUtopiaDataBusWidth_Object((1,3,6,1,4,1,6296,9,6,1,1,3,1,56),_DsShdslUtopiaDataBusWidth_Type())
dsShdslUtopiaDataBusWidth.setMaxAccess(_D)
if mibBuilder.loadTexts:dsShdslUtopiaDataBusWidth.setStatus(_A)
class _DsShdslFrmrOH_Type(Integer32):defaultValue=15;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_DsShdslFrmrOH_Type.__name__=_B
_DsShdslFrmrOH_Object=MibTableColumn
dsShdslFrmrOH=_DsShdslFrmrOH_Object((1,3,6,1,4,1,6296,9,6,1,1,3,1,57),_DsShdslFrmrOH_Type())
dsShdslFrmrOH.setMaxAccess(_C)
if mibBuilder.loadTexts:dsShdslFrmrOH.setStatus(_A)
class _DsShdslLoopAttenCrossingTrapEnable_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_DsShdslLoopAttenCrossingTrapEnable_Type.__name__=_B
_DsShdslLoopAttenCrossingTrapEnable_Object=MibTableColumn
dsShdslLoopAttenCrossingTrapEnable=_DsShdslLoopAttenCrossingTrapEnable_Object((1,3,6,1,4,1,6296,9,6,1,1,3,1,58),_DsShdslLoopAttenCrossingTrapEnable_Type())
dsShdslLoopAttenCrossingTrapEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:dsShdslLoopAttenCrossingTrapEnable.setStatus(_A)
class _DsShdslSNRMarginCrossingTrapEnable_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_DsShdslSNRMarginCrossingTrapEnable_Type.__name__=_B
_DsShdslSNRMarginCrossingTrapEnable_Object=MibTableColumn
dsShdslSNRMarginCrossingTrapEnable=_DsShdslSNRMarginCrossingTrapEnable_Object((1,3,6,1,4,1,6296,9,6,1,1,3,1,59),_DsShdslSNRMarginCrossingTrapEnable_Type())
dsShdslSNRMarginCrossingTrapEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:dsShdslSNRMarginCrossingTrapEnable.setStatus(_A)
class _DsShdslFramerOHAndDefectsTrapEnable_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_E,2)))
_DsShdslFramerOHAndDefectsTrapEnable_Type.__name__=_B
_DsShdslFramerOHAndDefectsTrapEnable_Object=MibTableColumn
dsShdslFramerOHAndDefectsTrapEnable=_DsShdslFramerOHAndDefectsTrapEnable_Object((1,3,6,1,4,1,6296,9,6,1,1,3,1,60),_DsShdslFramerOHAndDefectsTrapEnable_Type())
dsShdslFramerOHAndDefectsTrapEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:dsShdslFramerOHAndDefectsTrapEnable.setStatus(_A)
class _DsShdslParametricTestInputFile_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,56))
_DsShdslParametricTestInputFile_Type.__name__=_W
_DsShdslParametricTestInputFile_Object=MibTableColumn
dsShdslParametricTestInputFile=_DsShdslParametricTestInputFile_Object((1,3,6,1,4,1,6296,9,6,1,1,3,1,61),_DsShdslParametricTestInputFile_Type())
dsShdslParametricTestInputFile.setMaxAccess(_C)
if mibBuilder.loadTexts:dsShdslParametricTestInputFile.setStatus(_A)
class _DsShdslParamHybridLossTestStart_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_DsShdslParamHybridLossTestStart_Type.__name__=_B
_DsShdslParamHybridLossTestStart_Object=MibTableColumn
dsShdslParamHybridLossTestStart=_DsShdslParamHybridLossTestStart_Object((1,3,6,1,4,1,6296,9,6,1,1,3,1,62),_DsShdslParamHybridLossTestStart_Type())
dsShdslParamHybridLossTestStart.setMaxAccess(_C)
if mibBuilder.loadTexts:dsShdslParamHybridLossTestStart.setStatus(_A)
class _DsShdslParamHybridLossTestEnd_Type(Integer32):defaultValue=64;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_DsShdslParamHybridLossTestEnd_Type.__name__=_B
_DsShdslParamHybridLossTestEnd_Object=MibTableColumn
dsShdslParamHybridLossTestEnd=_DsShdslParamHybridLossTestEnd_Object((1,3,6,1,4,1,6296,9,6,1,1,3,1,63),_DsShdslParamHybridLossTestEnd_Type())
dsShdslParamHybridLossTestEnd.setMaxAccess(_C)
if mibBuilder.loadTexts:dsShdslParamHybridLossTestEnd.setStatus(_A)
_DsShdslSpanStatusExtnTable_Object=MibTable
dsShdslSpanStatusExtnTable=_DsShdslSpanStatusExtnTable_Object((1,3,6,1,4,1,6296,9,6,1,1,4))
if mibBuilder.loadTexts:dsShdslSpanStatusExtnTable.setStatus(_A)
_DsShdslSpanStatusExtnEntry_Object=MibTableRow
dsShdslSpanStatusExtnEntry=_DsShdslSpanStatusExtnEntry_Object((1,3,6,1,4,1,6296,9,6,1,1,4,1))
dsShdslSpanStatusExtnEntry.setIndexNames((0,_K,_L))
if mibBuilder.loadTexts:dsShdslSpanStatusExtnEntry.setStatus(_A)
class _DsShdslStatusPMMSMaxLineRate_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4112000))
_DsShdslStatusPMMSMaxLineRate_Type.__name__=_V
_DsShdslStatusPMMSMaxLineRate_Object=MibTableColumn
dsShdslStatusPMMSMaxLineRate=_DsShdslStatusPMMSMaxLineRate_Object((1,3,6,1,4,1,6296,9,6,1,1,4,1,1),_DsShdslStatusPMMSMaxLineRate_Type())
dsShdslStatusPMMSMaxLineRate.setMaxAccess(_D)
if mibBuilder.loadTexts:dsShdslStatusPMMSMaxLineRate.setStatus(_A)
class _DsShdslStatus4WireHsMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('standard',0),('enhanced',1)))
_DsShdslStatus4WireHsMode_Type.__name__=_B
_DsShdslStatus4WireHsMode_Object=MibTableColumn
dsShdslStatus4WireHsMode=_DsShdslStatus4WireHsMode_Object((1,3,6,1,4,1,6296,9,6,1,1,4,1,2),_DsShdslStatus4WireHsMode_Type())
dsShdslStatus4WireHsMode.setMaxAccess(_D)
if mibBuilder.loadTexts:dsShdslStatus4WireHsMode.setStatus(_A)
mibBuilder.exportSymbols('DASAN-SHDSL-MIB',**{'dasanShdslMIB':dasanShdslMIB,'dasanShdslLineMIB':dasanShdslLineMIB,'dasanShdslMIBObjects':dasanShdslMIBObjects,'dsShdslCapabilityGroup':dsShdslCapabilityGroup,'dsShdslCapabilityLineTxCap':dsShdslCapabilityLineTxCap,'dsShdslLineStatusTable':dsShdslLineStatusTable,'dsShdslLineStatusEntry':dsShdslLineStatusEntry,'dsShdslOpState':dsShdslOpState,'dsShdslStartProgress':dsShdslStartProgress,'dsShdslFwRelease':dsShdslFwRelease,'dsShdslLineSwap':dsShdslLineSwap,'dsShdslRmtCountryCode':dsShdslRmtCountryCode,'dsShdslRmtEncoderA':dsShdslRmtEncoderA,'dsShdslRmtEncoderB':dsShdslRmtEncoderB,'dsShdslRmtProviderCode':dsShdslRmtProviderCode,'dsShdslLocDetect':dsShdslLocDetect,'dsShdslTxPower':dsShdslTxPower,'dsShdslFramerSync':dsShdslFramerSync,'dsShdslRmtTomData':dsShdslRmtTomData,'dsShdslDriftAlarm':dsShdslDriftAlarm,'dsShdslReceiverGain':dsShdslReceiverGain,'dsShdslBertError':dsShdslBertError,'dsShdslFramerOHAndDefects':dsShdslFramerOHAndDefects,'dsShdslRmtFwVersion':dsShdslRmtFwVersion,'dsShdslUtopiaCellDelineation':dsShdslUtopiaCellDelineation,'dsShdslUtopiaRxCellCnt':dsShdslUtopiaRxCellCnt,'dsShdslUtopiaCellDropCnt':dsShdslUtopiaCellDropCnt,'dsShdslUtopiaRxHecErrorCnt':dsShdslUtopiaRxHecErrorCnt,'dsShdslUtopiaTxCellCnt':dsShdslUtopiaTxCellCnt,'dsShdslRmtNsfCusId':dsShdslRmtNsfCusId,'dsShdslRmtNsfCusData':dsShdslRmtNsfCusData,'dsShdslLocalHandshake':dsShdslLocalHandshake,'dsShdslRemoteHandshake':dsShdslRemoteHandshake,'dsShdslActualHandshake':dsShdslActualHandshake,'dsShdslRmtTxPower':dsShdslRmtTxPower,'dsShdslRmtPowerBackoff':dsShdslRmtPowerBackoff,'dsShdslAutoRetrainCount':dsShdslAutoRetrainCount,'dsShdslEocState':dsShdslEocState,'dsShdslFramerOneSecondCnt':dsShdslFramerOneSecondCnt,'dsShdslNtrFault':dsShdslNtrFault,'dsShdslCpeMasterCore':dsShdslCpeMasterCore,'dsShdslParametricTestResult':dsShdslParametricTestResult,'dsShdslParametricTestArray':dsShdslParametricTestArray,'dsShdslLineParamsTable':dsShdslLineParamsTable,'dsShdslLineParamsEntry':dsShdslLineParamsEntry,'dsShdslAction':dsShdslAction,'dsShdslMode':dsShdslMode,'dsShdslPowerScale':dsShdslPowerScale,'dsShdslFramerType':dsShdslFramerType,'dsShdslAFEType':dsShdslAFEType,'dsShdslEncodeCoeffA':dsShdslEncodeCoeffA,'dsShdslEncodeCoeffB':dsShdslEncodeCoeffB,'dsShdslTxEOCBufferLen':dsShdslTxEOCBufferLen,'dsShdslRxEOCBufferLen':dsShdslRxEOCBufferLen,'dsShdslNTR':dsShdslNTR,'dsShdslRxUpstreamFrameSync':dsShdslRxUpstreamFrameSync,'dsShdslRxDownstreamFrameSync':dsShdslRxDownstreamFrameSync,'dsShdslRxUpstreamStuffBits':dsShdslRxUpstreamStuffBits,'dsShdslRxDownstreamStuffBits':dsShdslRxDownstreamStuffBits,'dsShdslInitiate':dsShdslInitiate,'dsShdslFramerRxClockMode':dsShdslFramerRxClockMode,'dsShdslFramerRxPllMode':dsShdslFramerRxPllMode,'dsShdslSerialAtmCiuBufferSize':dsShdslSerialAtmCiuBufferSize,'dsShdslUtopiaL2TxAddress':dsShdslUtopiaL2TxAddress,'dsShdslUtopiaL2RxAddress':dsShdslUtopiaL2RxAddress,'dsShdslTxFramerPulseDelay':dsShdslTxFramerPulseDelay,'dsShdslRxFramerPulseDelay':dsShdslRxFramerPulseDelay,'dsShdslMultiFrameMode':dsShdslMultiFrameMode,'dsShdslEnable4or6MbpsBitrate':dsShdslEnable4or6MbpsBitrate,'dsShdslTomDataWord1':dsShdslTomDataWord1,'dsShdslTomDataWord2':dsShdslTomDataWord2,'dsShdslTomDataWord3':dsShdslTomDataWord3,'dsShdslTomDataWord4':dsShdslTomDataWord4,'dsShdslSetReqSilenceMode':dsShdslSetReqSilenceMode,'dsShdslSetIndividualRates1':dsShdslSetIndividualRates1,'dsShdslSetIndividualRates2':dsShdslSetIndividualRates2,'dsShdslSetIndividualRates3':dsShdslSetIndividualRates3,'dsShdslSatmCellDelineation':dsShdslSatmCellDelineation,'dsShdslFramerCellDropOnError':dsShdslFramerCellDropOnError,'dsShdslGearShiftType':dsShdslGearShiftType,'dsShdslHsNsf':dsShdslHsNsf,'dsShdslHsMaxBitsPerBaud':dsShdslHsMaxBitsPerBaud,'dsShdslHsCusId':dsShdslHsCusId,'dsShdslHsCusData0':dsShdslHsCusData0,'dsShdslHsCusData1':dsShdslHsCusData1,'dsShdslHsAnnexBType':dsShdslHsAnnexBType,'dsShdslAutoRetrain':dsShdslAutoRetrain,'dsShdslArCrcCheck':dsShdslArCrcCheck,'dsShdslArFramerSyncCheck':dsShdslArFramerSyncCheck,'dsShdslArSnrMarginCheck':dsShdslArSnrMarginCheck,'dsShdslArCrcThreshold':dsShdslArCrcThreshold,'dsShdslArSnrMarginThreshold':dsShdslArSnrMarginThreshold,'dsShdslArRetrainTime':dsShdslArRetrainTime,'dsShdslOpStateTrapEnable':dsShdslOpStateTrapEnable,'dsShdslTxFrmrDataClkEdge':dsShdslTxFrmrDataClkEdge,'dsShdslRxFrmrDataClkEdge':dsShdslRxFrmrDataClkEdge,'dsShdslTxFrmrPulseClkEdge':dsShdslTxFrmrPulseClkEdge,'dsShdslRxFrmrPulseClkEdge':dsShdslRxFrmrPulseClkEdge,'dsShdslTxFrmrPulseLvl':dsShdslTxFrmrPulseLvl,'dsShdslRxFrmrPulseLvl':dsShdslRxFrmrPulseLvl,'dsShdslUtopiaDataBusWidth':dsShdslUtopiaDataBusWidth,'dsShdslFrmrOH':dsShdslFrmrOH,'dsShdslLoopAttenCrossingTrapEnable':dsShdslLoopAttenCrossingTrapEnable,'dsShdslSNRMarginCrossingTrapEnable':dsShdslSNRMarginCrossingTrapEnable,'dsShdslFramerOHAndDefectsTrapEnable':dsShdslFramerOHAndDefectsTrapEnable,'dsShdslParametricTestInputFile':dsShdslParametricTestInputFile,'dsShdslParamHybridLossTestStart':dsShdslParamHybridLossTestStart,'dsShdslParamHybridLossTestEnd':dsShdslParamHybridLossTestEnd,'dsShdslSpanStatusExtnTable':dsShdslSpanStatusExtnTable,'dsShdslSpanStatusExtnEntry':dsShdslSpanStatusExtnEntry,'dsShdslStatusPMMSMaxLineRate':dsShdslStatusPMMSMaxLineRate,'dsShdslStatus4WireHsMode':dsShdslStatus4WireHsMode})