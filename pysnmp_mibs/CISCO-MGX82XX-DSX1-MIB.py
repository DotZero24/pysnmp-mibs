_Ak='cmDsx1AlarmGroup'
_Aj='cmDsx1AlarmConfGroup'
_Ai='cmDsx1CountGroup'
_Ah='cmDsx1ConfGroup'
_Ag='cmDsx1GeneralGroup'
_Af='alarmClrButton'
_Ae='percentEFS'
_Ad='uAS24HrBucket'
_Ac='uAS15MinBucket'
_Ab='uASCurrent'
_Aa='aISS24HrBucket'
_AZ='aISS15MinBucket'
_AY='aISSCurrent'
_AX='sEFS24HrBucket'
_AW='sEFS15MinBucket'
_AV='sEFSCurrent'
_AU='cRCSES24HrBucket'
_AT='cRCSES15MinBucket'
_AS='cRCSESCurrent'
_AR='cRCES24HrBucket'
_AQ='cRCES15MinBucket'
_AP='cRCESCurrent'
_AO='cRC24HrBucket'
_AN='cRC15MinBucket'
_AM='cRCCurrent'
_AL='lSES24HrBucket'
_AK='lSES15MinBucket'
_AJ='lSESCurrent'
_AI='lES24HrBucket'
_AH='lES15MinBucket'
_AG='lESCurrent'
_AF='lCV24HrBucket'
_AE='lCV15MinBucket'
_AD='lCVCurrent'
_AC='lineStatisticalAlarmState'
_AB='lineAlarmState'
_AA='uAS24HrThreshold'
_A9='uAS15MinThreshold'
_A8='aISS24HrThreshold'
_A7='aISS15MinThreshold'
_A6='sEFS24HrThreshold'
_A5='sEFS15MinThreshold'
_A4='cRCSES24HrThreshold'
_A3='cRCSES15MinThreshold'
_A2='cRCES24HrThreshold'
_A1='cRCES15MinThreshold'
_A0='cRC24HrThreshold'
_z='cRC15MinThreshold'
_y='lSES24HrThreshold'
_x='lSES15MinThreshold'
_w='lES24HrThreshold'
_v='lES15MinThreshold'
_u='lCV24HrThreshold'
_t='lCV15MinThreshold'
_s='statisticalAlarmSeverity'
_r='fEAlarmThreshold'
_q='fEAlarmDownCount'
_p='fEAlarmUpCount'
_o='nEAlarmThreshold'
_n='nEAlarmDownCount'
_m='nEAlarmUpCount'
_l='rAISeverity'
_k='redSeverity'
_j='counterClearButton'
_i='rcvFECount'
_h='rcvRAICount'
_g='rcvOOFCount'
_f='rcvLOSCount'
_e='bERTResultClrButton'
_d='lineBERTResult'
_c='lineBERTPattern'
_b='lineBERTEnable'
_a='lineUsedTimeslotsBitMap'
_Z='lineLoopbackCodeDetection'
_Y='lineSendCode'
_X='lineLoopbackCommand'
_W='lineXmtClockSource'
_V='lineLength'
_U='lineCoding'
_T='lineType'
_S='lineEnable'
_R='lineConnectorType'
_Q='lineNumofValidEntries'
_P='enable'
_O='disable'
_N='unused'
_M='cntLineNum'
_L='almLineNum'
_K='major'
_J='minor'
_I='almCnfLineNum'
_H='clear'
_G='noaction'
_F='lineNum'
_E='read-only'
_D='read-write'
_C='Integer32'
_B='CISCO-MGX82XX-DSX1-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dsx1Line,=mibBuilder.importSymbols('BASIS-MIB','dsx1Line')
ciscoWan,=mibBuilder.importSymbols('CISCOWAN-SMI','ciscoWan')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
ciscoMgx82xxDsx1MIB=ModuleIdentity((1,3,6,1,4,1,351,150,58))
if mibBuilder.loadTexts:ciscoMgx82xxDsx1MIB.setRevisions(('2003-03-31 00:00',))
_Dsx1CnfGrp_ObjectIdentity=ObjectIdentity
dsx1CnfGrp=_Dsx1CnfGrp_ObjectIdentity((1,3,6,1,4,1,351,110,4,3,1,1))
_Dsx1CnfGrpTable_Object=MibTable
dsx1CnfGrpTable=_Dsx1CnfGrpTable_Object((1,3,6,1,4,1,351,110,4,3,1,1,1))
if mibBuilder.loadTexts:dsx1CnfGrpTable.setStatus(_A)
_Dsx1CnfGrpEntry_Object=MibTableRow
dsx1CnfGrpEntry=_Dsx1CnfGrpEntry_Object((1,3,6,1,4,1,351,110,4,3,1,1,1,1))
dsx1CnfGrpEntry.setIndexNames((0,_B,_F))
if mibBuilder.loadTexts:dsx1CnfGrpEntry.setStatus(_A)
class _LineNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_LineNum_Type.__name__=_C
_LineNum_Object=MibTableColumn
lineNum=_LineNum_Object((1,3,6,1,4,1,351,110,4,3,1,1,1,1,1),_LineNum_Type())
lineNum.setMaxAccess(_E)
if mibBuilder.loadTexts:lineNum.setStatus(_A)
class _LineConnectorType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('db15',1),('bnc',2),('rj48',3),(_N,4),('smb',5)))
_LineConnectorType_Type.__name__=_C
_LineConnectorType_Object=MibTableColumn
lineConnectorType=_LineConnectorType_Object((1,3,6,1,4,1,351,110,4,3,1,1,1,1,2),_LineConnectorType_Type())
lineConnectorType.setMaxAccess(_D)
if mibBuilder.loadTexts:lineConnectorType.setStatus(_A)
class _LineEnable_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_O,1),(_P,2),('modify',3)))
_LineEnable_Type.__name__=_C
_LineEnable_Object=MibTableColumn
lineEnable=_LineEnable_Object((1,3,6,1,4,1,351,110,4,3,1,1,1,1,3),_LineEnable_Type())
lineEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:lineEnable.setStatus(_A)
class _LineType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*(('dsx1ESF',1),('dsx1D4',2),('dsx1E1',3),('dsx1E1CRC',4),('dsx1E1MF',5),('dsx1E1CRC-MF',6),('dsx1E1clearchannel',7),('dsx1E1Q50',8),('dsx1E1Q50CRC',9)))
_LineType_Type.__name__=_C
_LineType_Object=MibTableColumn
lineType=_LineType_Object((1,3,6,1,4,1,351,110,4,3,1,1,1,1,4),_LineType_Type())
lineType.setMaxAccess(_D)
if mibBuilder.loadTexts:lineType.setStatus(_A)
class _LineCoding_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('dsx1JBZS',1),('dsx1B8ZS',2),('dsx1HDB3',3),('dsx1AMI',4),(_N,5)))
_LineCoding_Type.__name__=_C
_LineCoding_Object=MibTableColumn
lineCoding=_LineCoding_Object((1,3,6,1,4,1,351,110,4,3,1,1,1,1,5),_LineCoding_Type())
lineCoding.setMaxAccess(_D)
if mibBuilder.loadTexts:lineCoding.setStatus(_A)
class _LineLength_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16)));namedValues=NamedValues(*(('lineLength0To110Feet',1),('lineLength110To220Feet',2),('lineLength220To330Feet',3),('lineLength330To440Feet',4),('lineLength440To550Feet',5),('lineLength550To660Feet',6),('lineLength660FeetPlus',7),('lineLength-75-Ohm',8),('lineLength-120-Ohm',9),('lineLength0To131Feet',10),('lineLength131To262Feet',11),('lineLength262To393Feet',12),('lineLength393To524Feet',13),('lineLength524To655Feet',14),('lineLength655FeetPlus',15),('notRequired',16)))
_LineLength_Type.__name__=_C
_LineLength_Object=MibTableColumn
lineLength=_LineLength_Object((1,3,6,1,4,1,351,110,4,3,1,1,1,1,6),_LineLength_Type())
lineLength.setMaxAccess(_D)
if mibBuilder.loadTexts:lineLength.setStatus(_A)
class _LineXmtClockSource_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('loopTiming',1),('localTiming',2)))
_LineXmtClockSource_Type.__name__=_C
_LineXmtClockSource_Object=MibTableColumn
lineXmtClockSource=_LineXmtClockSource_Object((1,3,6,1,4,1,351,110,4,3,1,1,1,1,7),_LineXmtClockSource_Type())
lineXmtClockSource.setMaxAccess(_D)
if mibBuilder.loadTexts:lineXmtClockSource.setStatus(_A)
class _LineLoopbackCommand_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('dsx1NoLoop',1),('dsx1RemoteLoop',2),('dsx1LocalLoop',3),('dsx1PayloadLoop',4)))
_LineLoopbackCommand_Type.__name__=_C
_LineLoopbackCommand_Object=MibTableColumn
lineLoopbackCommand=_LineLoopbackCommand_Object((1,3,6,1,4,1,351,110,4,3,1,1,1,1,8),_LineLoopbackCommand_Type())
lineLoopbackCommand.setMaxAccess(_D)
if mibBuilder.loadTexts:lineLoopbackCommand.setStatus(_A)
class _LineSendCode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('dsx1SendNoCode',1),('dsx1SendLineCode',2),('dsx1SendPayloadCode',3),('dsx1SendResetCode',4)))
_LineSendCode_Type.__name__=_C
_LineSendCode_Object=MibTableColumn
lineSendCode=_LineSendCode_Object((1,3,6,1,4,1,351,110,4,3,1,1,1,1,9),_LineSendCode_Type())
lineSendCode.setMaxAccess(_D)
if mibBuilder.loadTexts:lineSendCode.setStatus(_A)
class _LineUsedTimeslotsBitMap_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_LineUsedTimeslotsBitMap_Type.__name__=_C
_LineUsedTimeslotsBitMap_Object=MibTableColumn
lineUsedTimeslotsBitMap=_LineUsedTimeslotsBitMap_Object((1,3,6,1,4,1,351,110,4,3,1,1,1,1,10),_LineUsedTimeslotsBitMap_Type())
lineUsedTimeslotsBitMap.setMaxAccess(_E)
if mibBuilder.loadTexts:lineUsedTimeslotsBitMap.setStatus(_A)
class _LineLoopbackCodeDetection_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('codeDetectDisabled',1),('codeDetectEnabled',2)))
_LineLoopbackCodeDetection_Type.__name__=_C
_LineLoopbackCodeDetection_Object=MibTableColumn
lineLoopbackCodeDetection=_LineLoopbackCodeDetection_Object((1,3,6,1,4,1,351,110,4,3,1,1,1,1,11),_LineLoopbackCodeDetection_Type())
lineLoopbackCodeDetection.setMaxAccess(_D)
if mibBuilder.loadTexts:lineLoopbackCodeDetection.setStatus(_A)
class _LineBERTEnable_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_O,1),(_P,2)))
_LineBERTEnable_Type.__name__=_C
_LineBERTEnable_Object=MibTableColumn
lineBERTEnable=_LineBERTEnable_Object((1,3,6,1,4,1,351,110,4,3,1,1,1,1,12),_LineBERTEnable_Type())
lineBERTEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:lineBERTEnable.setStatus(_A)
class _LineBERTPattern_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12)));namedValues=NamedValues(*(('allZeros',1),('allOnes',2),('alternateONeZero',3),('doubleOneZero',4),('userOneWords',5),('userTwoWords',6),('userThreeWords',7),('userFourWords',8),('fifteenBit',9),('twentyBit',10),('twentyBitQRSS',11),('twentythreeBit',12)))
_LineBERTPattern_Type.__name__=_C
_LineBERTPattern_Object=MibTableColumn
lineBERTPattern=_LineBERTPattern_Object((1,3,6,1,4,1,351,110,4,3,1,1,1,1,13),_LineBERTPattern_Type())
lineBERTPattern.setMaxAccess(_D)
if mibBuilder.loadTexts:lineBERTPattern.setStatus(_A)
class _LineBERTResult_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('failed',1),('passed',2)))
_LineBERTResult_Type.__name__=_C
_LineBERTResult_Object=MibTableColumn
lineBERTResult=_LineBERTResult_Object((1,3,6,1,4,1,351,110,4,3,1,1,1,1,14),_LineBERTResult_Type())
lineBERTResult.setMaxAccess(_D)
if mibBuilder.loadTexts:lineBERTResult.setStatus(_A)
class _BERTResultClrButton_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_BERTResultClrButton_Type.__name__=_C
_BERTResultClrButton_Object=MibTableColumn
bERTResultClrButton=_BERTResultClrButton_Object((1,3,6,1,4,1,351,110,4,3,1,1,1,1,15),_BERTResultClrButton_Type())
bERTResultClrButton.setMaxAccess(_D)
if mibBuilder.loadTexts:bERTResultClrButton.setStatus(_A)
class _LineNumofValidEntries_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_LineNumofValidEntries_Type.__name__=_C
_LineNumofValidEntries_Object=MibScalar
lineNumofValidEntries=_LineNumofValidEntries_Object((1,3,6,1,4,1,351,110,4,3,1,1,2),_LineNumofValidEntries_Type())
lineNumofValidEntries.setMaxAccess(_E)
if mibBuilder.loadTexts:lineNumofValidEntries.setStatus(_A)
_Dsx1AlmCnfGrp_ObjectIdentity=ObjectIdentity
dsx1AlmCnfGrp=_Dsx1AlmCnfGrp_ObjectIdentity((1,3,6,1,4,1,351,110,4,3,1,2))
_Dsx1AlmCnfGrpTable_Object=MibTable
dsx1AlmCnfGrpTable=_Dsx1AlmCnfGrpTable_Object((1,3,6,1,4,1,351,110,4,3,1,2,1))
if mibBuilder.loadTexts:dsx1AlmCnfGrpTable.setStatus(_A)
_Dsx1AlmCnfGrpEntry_Object=MibTableRow
dsx1AlmCnfGrpEntry=_Dsx1AlmCnfGrpEntry_Object((1,3,6,1,4,1,351,110,4,3,1,2,1,1))
dsx1AlmCnfGrpEntry.setIndexNames((0,_B,_I))
if mibBuilder.loadTexts:dsx1AlmCnfGrpEntry.setStatus(_A)
class _AlmCnfLineNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_AlmCnfLineNum_Type.__name__=_C
_AlmCnfLineNum_Object=MibTableColumn
almCnfLineNum=_AlmCnfLineNum_Object((1,3,6,1,4,1,351,110,4,3,1,2,1,1,1),_AlmCnfLineNum_Type())
almCnfLineNum.setMaxAccess(_E)
if mibBuilder.loadTexts:almCnfLineNum.setStatus(_A)
class _RedSeverity_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_RedSeverity_Type.__name__=_C
_RedSeverity_Object=MibTableColumn
redSeverity=_RedSeverity_Object((1,3,6,1,4,1,351,110,4,3,1,2,1,1,2),_RedSeverity_Type())
redSeverity.setMaxAccess(_D)
if mibBuilder.loadTexts:redSeverity.setStatus(_A)
class _RAISeverity_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_RAISeverity_Type.__name__=_C
_RAISeverity_Object=MibTableColumn
rAISeverity=_RAISeverity_Object((1,3,6,1,4,1,351,110,4,3,1,2,1,1,3),_RAISeverity_Type())
rAISeverity.setMaxAccess(_D)
if mibBuilder.loadTexts:rAISeverity.setStatus(_A)
class _NEAlarmUpCount_Type(Integer32):defaultValue=6;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_NEAlarmUpCount_Type.__name__=_C
_NEAlarmUpCount_Object=MibTableColumn
nEAlarmUpCount=_NEAlarmUpCount_Object((1,3,6,1,4,1,351,110,4,3,1,2,1,1,4),_NEAlarmUpCount_Type())
nEAlarmUpCount.setMaxAccess(_D)
if mibBuilder.loadTexts:nEAlarmUpCount.setStatus(_A)
class _NEAlarmDownCount_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_NEAlarmDownCount_Type.__name__=_C
_NEAlarmDownCount_Object=MibTableColumn
nEAlarmDownCount=_NEAlarmDownCount_Object((1,3,6,1,4,1,351,110,4,3,1,2,1,1,5),_NEAlarmDownCount_Type())
nEAlarmDownCount.setMaxAccess(_D)
if mibBuilder.loadTexts:nEAlarmDownCount.setStatus(_A)
class _NEAlarmThreshold_Type(Integer32):defaultValue=1500;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_NEAlarmThreshold_Type.__name__=_C
_NEAlarmThreshold_Object=MibTableColumn
nEAlarmThreshold=_NEAlarmThreshold_Object((1,3,6,1,4,1,351,110,4,3,1,2,1,1,6),_NEAlarmThreshold_Type())
nEAlarmThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:nEAlarmThreshold.setStatus(_A)
class _FEAlarmUpCount_Type(Integer32):defaultValue=6;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_FEAlarmUpCount_Type.__name__=_C
_FEAlarmUpCount_Object=MibTableColumn
fEAlarmUpCount=_FEAlarmUpCount_Object((1,3,6,1,4,1,351,110,4,3,1,2,1,1,7),_FEAlarmUpCount_Type())
fEAlarmUpCount.setMaxAccess(_D)
if mibBuilder.loadTexts:fEAlarmUpCount.setStatus(_A)
class _FEAlarmDownCount_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_FEAlarmDownCount_Type.__name__=_C
_FEAlarmDownCount_Object=MibTableColumn
fEAlarmDownCount=_FEAlarmDownCount_Object((1,3,6,1,4,1,351,110,4,3,1,2,1,1,8),_FEAlarmDownCount_Type())
fEAlarmDownCount.setMaxAccess(_D)
if mibBuilder.loadTexts:fEAlarmDownCount.setStatus(_A)
class _FEAlarmThreshold_Type(Integer32):defaultValue=1500;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_FEAlarmThreshold_Type.__name__=_C
_FEAlarmThreshold_Object=MibTableColumn
fEAlarmThreshold=_FEAlarmThreshold_Object((1,3,6,1,4,1,351,110,4,3,1,2,1,1,9),_FEAlarmThreshold_Type())
fEAlarmThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:fEAlarmThreshold.setStatus(_A)
class _StatisticalAlarmSeverity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_J,1),(_K,2),('inhibit',3)))
_StatisticalAlarmSeverity_Type.__name__=_C
_StatisticalAlarmSeverity_Object=MibTableColumn
statisticalAlarmSeverity=_StatisticalAlarmSeverity_Object((1,3,6,1,4,1,351,110,4,3,1,2,1,1,10),_StatisticalAlarmSeverity_Type())
statisticalAlarmSeverity.setMaxAccess(_D)
if mibBuilder.loadTexts:statisticalAlarmSeverity.setStatus(_A)
class _LCV15MinThreshold_Type(Integer32):defaultValue=14;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_LCV15MinThreshold_Type.__name__=_C
_LCV15MinThreshold_Object=MibTableColumn
lCV15MinThreshold=_LCV15MinThreshold_Object((1,3,6,1,4,1,351,110,4,3,1,2,1,1,11),_LCV15MinThreshold_Type())
lCV15MinThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:lCV15MinThreshold.setStatus(_A)
class _LCV24HrThreshold_Type(Integer32):defaultValue=134;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_LCV24HrThreshold_Type.__name__=_C
_LCV24HrThreshold_Object=MibTableColumn
lCV24HrThreshold=_LCV24HrThreshold_Object((1,3,6,1,4,1,351,110,4,3,1,2,1,1,12),_LCV24HrThreshold_Type())
lCV24HrThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:lCV24HrThreshold.setStatus(_A)
class _LES15MinThreshold_Type(Integer32):defaultValue=12;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_LES15MinThreshold_Type.__name__=_C
_LES15MinThreshold_Object=MibTableColumn
lES15MinThreshold=_LES15MinThreshold_Object((1,3,6,1,4,1,351,110,4,3,1,2,1,1,13),_LES15MinThreshold_Type())
lES15MinThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:lES15MinThreshold.setStatus(_A)
class _LES24HrThreshold_Type(Integer32):defaultValue=121;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_LES24HrThreshold_Type.__name__=_C
_LES24HrThreshold_Object=MibTableColumn
lES24HrThreshold=_LES24HrThreshold_Object((1,3,6,1,4,1,351,110,4,3,1,2,1,1,14),_LES24HrThreshold_Type())
lES24HrThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:lES24HrThreshold.setStatus(_A)
class _LSES15MinThreshold_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_LSES15MinThreshold_Type.__name__=_C
_LSES15MinThreshold_Object=MibTableColumn
lSES15MinThreshold=_LSES15MinThreshold_Object((1,3,6,1,4,1,351,110,4,3,1,2,1,1,15),_LSES15MinThreshold_Type())
lSES15MinThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:lSES15MinThreshold.setStatus(_A)
class _LSES24HrThreshold_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_LSES24HrThreshold_Type.__name__=_C
_LSES24HrThreshold_Object=MibTableColumn
lSES24HrThreshold=_LSES24HrThreshold_Object((1,3,6,1,4,1,351,110,4,3,1,2,1,1,16),_LSES24HrThreshold_Type())
lSES24HrThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:lSES24HrThreshold.setStatus(_A)
class _CRC15MinThreshold_Type(Integer32):defaultValue=14;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CRC15MinThreshold_Type.__name__=_C
_CRC15MinThreshold_Object=MibTableColumn
cRC15MinThreshold=_CRC15MinThreshold_Object((1,3,6,1,4,1,351,110,4,3,1,2,1,1,17),_CRC15MinThreshold_Type())
cRC15MinThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:cRC15MinThreshold.setStatus(_A)
class _CRC24HrThreshold_Type(Integer32):defaultValue=134;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CRC24HrThreshold_Type.__name__=_C
_CRC24HrThreshold_Object=MibTableColumn
cRC24HrThreshold=_CRC24HrThreshold_Object((1,3,6,1,4,1,351,110,4,3,1,2,1,1,18),_CRC24HrThreshold_Type())
cRC24HrThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:cRC24HrThreshold.setStatus(_A)
class _CRCES15MinThreshold_Type(Integer32):defaultValue=12;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CRCES15MinThreshold_Type.__name__=_C
_CRCES15MinThreshold_Object=MibTableColumn
cRCES15MinThreshold=_CRCES15MinThreshold_Object((1,3,6,1,4,1,351,110,4,3,1,2,1,1,19),_CRCES15MinThreshold_Type())
cRCES15MinThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:cRCES15MinThreshold.setStatus(_A)
class _CRCES24HrThreshold_Type(Integer32):defaultValue=121;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CRCES24HrThreshold_Type.__name__=_C
_CRCES24HrThreshold_Object=MibTableColumn
cRCES24HrThreshold=_CRCES24HrThreshold_Object((1,3,6,1,4,1,351,110,4,3,1,2,1,1,20),_CRCES24HrThreshold_Type())
cRCES24HrThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:cRCES24HrThreshold.setStatus(_A)
class _CRCSES15MinThreshold_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CRCSES15MinThreshold_Type.__name__=_C
_CRCSES15MinThreshold_Object=MibTableColumn
cRCSES15MinThreshold=_CRCSES15MinThreshold_Object((1,3,6,1,4,1,351,110,4,3,1,2,1,1,21),_CRCSES15MinThreshold_Type())
cRCSES15MinThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:cRCSES15MinThreshold.setStatus(_A)
class _CRCSES24HrThreshold_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CRCSES24HrThreshold_Type.__name__=_C
_CRCSES24HrThreshold_Object=MibTableColumn
cRCSES24HrThreshold=_CRCSES24HrThreshold_Object((1,3,6,1,4,1,351,110,4,3,1,2,1,1,22),_CRCSES24HrThreshold_Type())
cRCSES24HrThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:cRCSES24HrThreshold.setStatus(_A)
class _SEFS15MinThreshold_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_SEFS15MinThreshold_Type.__name__=_C
_SEFS15MinThreshold_Object=MibTableColumn
sEFS15MinThreshold=_SEFS15MinThreshold_Object((1,3,6,1,4,1,351,110,4,3,1,2,1,1,23),_SEFS15MinThreshold_Type())
sEFS15MinThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:sEFS15MinThreshold.setStatus(_A)
class _SEFS24HrThreshold_Type(Integer32):defaultValue=17;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_SEFS24HrThreshold_Type.__name__=_C
_SEFS24HrThreshold_Object=MibTableColumn
sEFS24HrThreshold=_SEFS24HrThreshold_Object((1,3,6,1,4,1,351,110,4,3,1,2,1,1,24),_SEFS24HrThreshold_Type())
sEFS24HrThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:sEFS24HrThreshold.setStatus(_A)
class _AISS15MinThreshold_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_AISS15MinThreshold_Type.__name__=_C
_AISS15MinThreshold_Object=MibTableColumn
aISS15MinThreshold=_AISS15MinThreshold_Object((1,3,6,1,4,1,351,110,4,3,1,2,1,1,25),_AISS15MinThreshold_Type())
aISS15MinThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:aISS15MinThreshold.setStatus(_A)
class _AISS24HrThreshold_Type(Integer32):defaultValue=17;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_AISS24HrThreshold_Type.__name__=_C
_AISS24HrThreshold_Object=MibTableColumn
aISS24HrThreshold=_AISS24HrThreshold_Object((1,3,6,1,4,1,351,110,4,3,1,2,1,1,26),_AISS24HrThreshold_Type())
aISS24HrThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:aISS24HrThreshold.setStatus(_A)
class _UAS15MinThreshold_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_UAS15MinThreshold_Type.__name__=_C
_UAS15MinThreshold_Object=MibTableColumn
uAS15MinThreshold=_UAS15MinThreshold_Object((1,3,6,1,4,1,351,110,4,3,1,2,1,1,27),_UAS15MinThreshold_Type())
uAS15MinThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:uAS15MinThreshold.setStatus(_A)
class _UAS24HrThreshold_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_UAS24HrThreshold_Type.__name__=_C
_UAS24HrThreshold_Object=MibTableColumn
uAS24HrThreshold=_UAS24HrThreshold_Object((1,3,6,1,4,1,351,110,4,3,1,2,1,1,28),_UAS24HrThreshold_Type())
uAS24HrThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:uAS24HrThreshold.setStatus(_A)
_Dsx1AlmGrp_ObjectIdentity=ObjectIdentity
dsx1AlmGrp=_Dsx1AlmGrp_ObjectIdentity((1,3,6,1,4,1,351,110,4,3,1,3))
_Dsx1AlmGrpTable_Object=MibTable
dsx1AlmGrpTable=_Dsx1AlmGrpTable_Object((1,3,6,1,4,1,351,110,4,3,1,3,1))
if mibBuilder.loadTexts:dsx1AlmGrpTable.setStatus(_A)
_Dsx1AlmGrpEntry_Object=MibTableRow
dsx1AlmGrpEntry=_Dsx1AlmGrpEntry_Object((1,3,6,1,4,1,351,110,4,3,1,3,1,1))
dsx1AlmGrpEntry.setIndexNames((0,_B,_L))
if mibBuilder.loadTexts:dsx1AlmGrpEntry.setStatus(_A)
class _AlmLineNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_AlmLineNum_Type.__name__=_C
_AlmLineNum_Object=MibTableColumn
almLineNum=_AlmLineNum_Object((1,3,6,1,4,1,351,110,4,3,1,3,1,1,1),_AlmLineNum_Type())
almLineNum.setMaxAccess(_E)
if mibBuilder.loadTexts:almLineNum.setStatus(_A)
class _LineAlarmState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_LineAlarmState_Type.__name__=_C
_LineAlarmState_Object=MibTableColumn
lineAlarmState=_LineAlarmState_Object((1,3,6,1,4,1,351,110,4,3,1,3,1,1,2),_LineAlarmState_Type())
lineAlarmState.setMaxAccess(_E)
if mibBuilder.loadTexts:lineAlarmState.setStatus(_A)
class _LineStatisticalAlarmState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_LineStatisticalAlarmState_Type.__name__=_C
_LineStatisticalAlarmState_Object=MibTableColumn
lineStatisticalAlarmState=_LineStatisticalAlarmState_Object((1,3,6,1,4,1,351,110,4,3,1,3,1,1,3),_LineStatisticalAlarmState_Type())
lineStatisticalAlarmState.setMaxAccess(_E)
if mibBuilder.loadTexts:lineStatisticalAlarmState.setStatus(_A)
_LCVCurrent_Type=Counter32
_LCVCurrent_Object=MibTableColumn
lCVCurrent=_LCVCurrent_Object((1,3,6,1,4,1,351,110,4,3,1,3,1,1,4),_LCVCurrent_Type())
lCVCurrent.setMaxAccess(_E)
if mibBuilder.loadTexts:lCVCurrent.setStatus(_A)
_LCV15MinBucket_Type=Counter32
_LCV15MinBucket_Object=MibTableColumn
lCV15MinBucket=_LCV15MinBucket_Object((1,3,6,1,4,1,351,110,4,3,1,3,1,1,5),_LCV15MinBucket_Type())
lCV15MinBucket.setMaxAccess(_E)
if mibBuilder.loadTexts:lCV15MinBucket.setStatus(_A)
_LCV24HrBucket_Type=Counter32
_LCV24HrBucket_Object=MibTableColumn
lCV24HrBucket=_LCV24HrBucket_Object((1,3,6,1,4,1,351,110,4,3,1,3,1,1,6),_LCV24HrBucket_Type())
lCV24HrBucket.setMaxAccess(_E)
if mibBuilder.loadTexts:lCV24HrBucket.setStatus(_A)
_LESCurrent_Type=Counter32
_LESCurrent_Object=MibTableColumn
lESCurrent=_LESCurrent_Object((1,3,6,1,4,1,351,110,4,3,1,3,1,1,7),_LESCurrent_Type())
lESCurrent.setMaxAccess(_E)
if mibBuilder.loadTexts:lESCurrent.setStatus(_A)
_LES15MinBucket_Type=Counter32
_LES15MinBucket_Object=MibTableColumn
lES15MinBucket=_LES15MinBucket_Object((1,3,6,1,4,1,351,110,4,3,1,3,1,1,8),_LES15MinBucket_Type())
lES15MinBucket.setMaxAccess(_E)
if mibBuilder.loadTexts:lES15MinBucket.setStatus(_A)
_LES24HrBucket_Type=Counter32
_LES24HrBucket_Object=MibTableColumn
lES24HrBucket=_LES24HrBucket_Object((1,3,6,1,4,1,351,110,4,3,1,3,1,1,9),_LES24HrBucket_Type())
lES24HrBucket.setMaxAccess(_E)
if mibBuilder.loadTexts:lES24HrBucket.setStatus(_A)
_LSESCurrent_Type=Counter32
_LSESCurrent_Object=MibTableColumn
lSESCurrent=_LSESCurrent_Object((1,3,6,1,4,1,351,110,4,3,1,3,1,1,10),_LSESCurrent_Type())
lSESCurrent.setMaxAccess(_E)
if mibBuilder.loadTexts:lSESCurrent.setStatus(_A)
_LSES15MinBucket_Type=Counter32
_LSES15MinBucket_Object=MibTableColumn
lSES15MinBucket=_LSES15MinBucket_Object((1,3,6,1,4,1,351,110,4,3,1,3,1,1,11),_LSES15MinBucket_Type())
lSES15MinBucket.setMaxAccess(_E)
if mibBuilder.loadTexts:lSES15MinBucket.setStatus(_A)
_LSES24HrBucket_Type=Counter32
_LSES24HrBucket_Object=MibTableColumn
lSES24HrBucket=_LSES24HrBucket_Object((1,3,6,1,4,1,351,110,4,3,1,3,1,1,12),_LSES24HrBucket_Type())
lSES24HrBucket.setMaxAccess(_E)
if mibBuilder.loadTexts:lSES24HrBucket.setStatus(_A)
_CRCCurrent_Type=Counter32
_CRCCurrent_Object=MibTableColumn
cRCCurrent=_CRCCurrent_Object((1,3,6,1,4,1,351,110,4,3,1,3,1,1,13),_CRCCurrent_Type())
cRCCurrent.setMaxAccess(_E)
if mibBuilder.loadTexts:cRCCurrent.setStatus(_A)
_CRC15MinBucket_Type=Counter32
_CRC15MinBucket_Object=MibTableColumn
cRC15MinBucket=_CRC15MinBucket_Object((1,3,6,1,4,1,351,110,4,3,1,3,1,1,14),_CRC15MinBucket_Type())
cRC15MinBucket.setMaxAccess(_E)
if mibBuilder.loadTexts:cRC15MinBucket.setStatus(_A)
_CRC24HrBucket_Type=Counter32
_CRC24HrBucket_Object=MibTableColumn
cRC24HrBucket=_CRC24HrBucket_Object((1,3,6,1,4,1,351,110,4,3,1,3,1,1,15),_CRC24HrBucket_Type())
cRC24HrBucket.setMaxAccess(_E)
if mibBuilder.loadTexts:cRC24HrBucket.setStatus(_A)
_CRCESCurrent_Type=Counter32
_CRCESCurrent_Object=MibTableColumn
cRCESCurrent=_CRCESCurrent_Object((1,3,6,1,4,1,351,110,4,3,1,3,1,1,16),_CRCESCurrent_Type())
cRCESCurrent.setMaxAccess(_E)
if mibBuilder.loadTexts:cRCESCurrent.setStatus(_A)
_CRCES15MinBucket_Type=Counter32
_CRCES15MinBucket_Object=MibTableColumn
cRCES15MinBucket=_CRCES15MinBucket_Object((1,3,6,1,4,1,351,110,4,3,1,3,1,1,17),_CRCES15MinBucket_Type())
cRCES15MinBucket.setMaxAccess(_E)
if mibBuilder.loadTexts:cRCES15MinBucket.setStatus(_A)
_CRCES24HrBucket_Type=Counter32
_CRCES24HrBucket_Object=MibTableColumn
cRCES24HrBucket=_CRCES24HrBucket_Object((1,3,6,1,4,1,351,110,4,3,1,3,1,1,18),_CRCES24HrBucket_Type())
cRCES24HrBucket.setMaxAccess(_E)
if mibBuilder.loadTexts:cRCES24HrBucket.setStatus(_A)
_CRCSESCurrent_Type=Counter32
_CRCSESCurrent_Object=MibTableColumn
cRCSESCurrent=_CRCSESCurrent_Object((1,3,6,1,4,1,351,110,4,3,1,3,1,1,19),_CRCSESCurrent_Type())
cRCSESCurrent.setMaxAccess(_E)
if mibBuilder.loadTexts:cRCSESCurrent.setStatus(_A)
_CRCSES15MinBucket_Type=Counter32
_CRCSES15MinBucket_Object=MibTableColumn
cRCSES15MinBucket=_CRCSES15MinBucket_Object((1,3,6,1,4,1,351,110,4,3,1,3,1,1,20),_CRCSES15MinBucket_Type())
cRCSES15MinBucket.setMaxAccess(_E)
if mibBuilder.loadTexts:cRCSES15MinBucket.setStatus(_A)
_CRCSES24HrBucket_Type=Counter32
_CRCSES24HrBucket_Object=MibTableColumn
cRCSES24HrBucket=_CRCSES24HrBucket_Object((1,3,6,1,4,1,351,110,4,3,1,3,1,1,21),_CRCSES24HrBucket_Type())
cRCSES24HrBucket.setMaxAccess(_E)
if mibBuilder.loadTexts:cRCSES24HrBucket.setStatus(_A)
_SEFSCurrent_Type=Counter32
_SEFSCurrent_Object=MibTableColumn
sEFSCurrent=_SEFSCurrent_Object((1,3,6,1,4,1,351,110,4,3,1,3,1,1,22),_SEFSCurrent_Type())
sEFSCurrent.setMaxAccess(_E)
if mibBuilder.loadTexts:sEFSCurrent.setStatus(_A)
_SEFS15MinBucket_Type=Counter32
_SEFS15MinBucket_Object=MibTableColumn
sEFS15MinBucket=_SEFS15MinBucket_Object((1,3,6,1,4,1,351,110,4,3,1,3,1,1,23),_SEFS15MinBucket_Type())
sEFS15MinBucket.setMaxAccess(_E)
if mibBuilder.loadTexts:sEFS15MinBucket.setStatus(_A)
_SEFS24HrBucket_Type=Counter32
_SEFS24HrBucket_Object=MibTableColumn
sEFS24HrBucket=_SEFS24HrBucket_Object((1,3,6,1,4,1,351,110,4,3,1,3,1,1,24),_SEFS24HrBucket_Type())
sEFS24HrBucket.setMaxAccess(_E)
if mibBuilder.loadTexts:sEFS24HrBucket.setStatus(_A)
_AISSCurrent_Type=Counter32
_AISSCurrent_Object=MibTableColumn
aISSCurrent=_AISSCurrent_Object((1,3,6,1,4,1,351,110,4,3,1,3,1,1,25),_AISSCurrent_Type())
aISSCurrent.setMaxAccess(_E)
if mibBuilder.loadTexts:aISSCurrent.setStatus(_A)
_AISS15MinBucket_Type=Counter32
_AISS15MinBucket_Object=MibTableColumn
aISS15MinBucket=_AISS15MinBucket_Object((1,3,6,1,4,1,351,110,4,3,1,3,1,1,26),_AISS15MinBucket_Type())
aISS15MinBucket.setMaxAccess(_E)
if mibBuilder.loadTexts:aISS15MinBucket.setStatus(_A)
_AISS24HrBucket_Type=Counter32
_AISS24HrBucket_Object=MibTableColumn
aISS24HrBucket=_AISS24HrBucket_Object((1,3,6,1,4,1,351,110,4,3,1,3,1,1,27),_AISS24HrBucket_Type())
aISS24HrBucket.setMaxAccess(_E)
if mibBuilder.loadTexts:aISS24HrBucket.setStatus(_A)
_UASCurrent_Type=Counter32
_UASCurrent_Object=MibTableColumn
uASCurrent=_UASCurrent_Object((1,3,6,1,4,1,351,110,4,3,1,3,1,1,28),_UASCurrent_Type())
uASCurrent.setMaxAccess(_E)
if mibBuilder.loadTexts:uASCurrent.setStatus(_A)
_UAS15MinBucket_Type=Counter32
_UAS15MinBucket_Object=MibTableColumn
uAS15MinBucket=_UAS15MinBucket_Object((1,3,6,1,4,1,351,110,4,3,1,3,1,1,29),_UAS15MinBucket_Type())
uAS15MinBucket.setMaxAccess(_E)
if mibBuilder.loadTexts:uAS15MinBucket.setStatus(_A)
_UAS24HrBucket_Type=Counter32
_UAS24HrBucket_Object=MibTableColumn
uAS24HrBucket=_UAS24HrBucket_Object((1,3,6,1,4,1,351,110,4,3,1,3,1,1,30),_UAS24HrBucket_Type())
uAS24HrBucket.setMaxAccess(_E)
if mibBuilder.loadTexts:uAS24HrBucket.setStatus(_A)
class _PercentEFS_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_PercentEFS_Type.__name__=_C
_PercentEFS_Object=MibTableColumn
percentEFS=_PercentEFS_Object((1,3,6,1,4,1,351,110,4,3,1,3,1,1,31),_PercentEFS_Type())
percentEFS.setMaxAccess(_E)
if mibBuilder.loadTexts:percentEFS.setStatus(_A)
class _AlarmClrButton_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_AlarmClrButton_Type.__name__=_C
_AlarmClrButton_Object=MibTableColumn
alarmClrButton=_AlarmClrButton_Object((1,3,6,1,4,1,351,110,4,3,1,3,1,1,32),_AlarmClrButton_Type())
alarmClrButton.setMaxAccess(_D)
if mibBuilder.loadTexts:alarmClrButton.setStatus(_A)
_Dsx1CntGrp_ObjectIdentity=ObjectIdentity
dsx1CntGrp=_Dsx1CntGrp_ObjectIdentity((1,3,6,1,4,1,351,110,4,3,1,4))
_Dsx1CntGrpTable_Object=MibTable
dsx1CntGrpTable=_Dsx1CntGrpTable_Object((1,3,6,1,4,1,351,110,4,3,1,4,1))
if mibBuilder.loadTexts:dsx1CntGrpTable.setStatus(_A)
_Dsx1CntGrpEntry_Object=MibTableRow
dsx1CntGrpEntry=_Dsx1CntGrpEntry_Object((1,3,6,1,4,1,351,110,4,3,1,4,1,1))
dsx1CntGrpEntry.setIndexNames((0,_B,_M))
if mibBuilder.loadTexts:dsx1CntGrpEntry.setStatus(_A)
class _CntLineNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_CntLineNum_Type.__name__=_C
_CntLineNum_Object=MibTableColumn
cntLineNum=_CntLineNum_Object((1,3,6,1,4,1,351,110,4,3,1,4,1,1,1),_CntLineNum_Type())
cntLineNum.setMaxAccess(_E)
if mibBuilder.loadTexts:cntLineNum.setStatus(_A)
_RcvLOSCount_Type=Counter32
_RcvLOSCount_Object=MibTableColumn
rcvLOSCount=_RcvLOSCount_Object((1,3,6,1,4,1,351,110,4,3,1,4,1,1,2),_RcvLOSCount_Type())
rcvLOSCount.setMaxAccess(_E)
if mibBuilder.loadTexts:rcvLOSCount.setStatus(_A)
_RcvOOFCount_Type=Counter32
_RcvOOFCount_Object=MibTableColumn
rcvOOFCount=_RcvOOFCount_Object((1,3,6,1,4,1,351,110,4,3,1,4,1,1,3),_RcvOOFCount_Type())
rcvOOFCount.setMaxAccess(_E)
if mibBuilder.loadTexts:rcvOOFCount.setStatus(_A)
_RcvRAICount_Type=Counter32
_RcvRAICount_Object=MibTableColumn
rcvRAICount=_RcvRAICount_Object((1,3,6,1,4,1,351,110,4,3,1,4,1,1,4),_RcvRAICount_Type())
rcvRAICount.setMaxAccess(_E)
if mibBuilder.loadTexts:rcvRAICount.setStatus(_A)
_RcvFECount_Type=Counter32
_RcvFECount_Object=MibTableColumn
rcvFECount=_RcvFECount_Object((1,3,6,1,4,1,351,110,4,3,1,4,1,1,5),_RcvFECount_Type())
rcvFECount.setMaxAccess(_E)
if mibBuilder.loadTexts:rcvFECount.setStatus(_A)
class _CounterClearButton_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_CounterClearButton_Type.__name__=_C
_CounterClearButton_Object=MibTableColumn
counterClearButton=_CounterClearButton_Object((1,3,6,1,4,1,351,110,4,3,1,4,1,1,6),_CounterClearButton_Type())
counterClearButton.setMaxAccess(_D)
if mibBuilder.loadTexts:counterClearButton.setStatus(_A)
_CmDsx1MIBConformance_ObjectIdentity=ObjectIdentity
cmDsx1MIBConformance=_CmDsx1MIBConformance_ObjectIdentity((1,3,6,1,4,1,351,150,58,2))
_CmDsx1MIBGroups_ObjectIdentity=ObjectIdentity
cmDsx1MIBGroups=_CmDsx1MIBGroups_ObjectIdentity((1,3,6,1,4,1,351,150,58,2,1))
_CmDsx1MIBCompliances_ObjectIdentity=ObjectIdentity
cmDsx1MIBCompliances=_CmDsx1MIBCompliances_ObjectIdentity((1,3,6,1,4,1,351,150,58,2,2))
cmDsx1GeneralGroup=ObjectGroup((1,3,6,1,4,1,351,150,58,2,1,1))
cmDsx1GeneralGroup.setObjects((_B,_Q))
if mibBuilder.loadTexts:cmDsx1GeneralGroup.setStatus(_A)
cmDsx1ConfGroup=ObjectGroup((1,3,6,1,4,1,351,150,58,2,1,2))
cmDsx1ConfGroup.setObjects(*((_B,_F),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e)))
if mibBuilder.loadTexts:cmDsx1ConfGroup.setStatus(_A)
cmDsx1CountGroup=ObjectGroup((1,3,6,1,4,1,351,150,58,2,1,3))
cmDsx1CountGroup.setObjects(*((_B,_M),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j)))
if mibBuilder.loadTexts:cmDsx1CountGroup.setStatus(_A)
cmDsx1AlarmConfGroup=ObjectGroup((1,3,6,1,4,1,351,150,58,2,1,4))
cmDsx1AlarmConfGroup.setObjects(*((_B,_I),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6),(_B,_A7),(_B,_A8),(_B,_A9),(_B,_AA)))
if mibBuilder.loadTexts:cmDsx1AlarmConfGroup.setStatus(_A)
cmDsx1AlarmGroup=ObjectGroup((1,3,6,1,4,1,351,150,58,2,1,5))
cmDsx1AlarmGroup.setObjects(*((_B,_L),(_B,_AB),(_B,_AC),(_B,_AD),(_B,_AE),(_B,_AF),(_B,_AG),(_B,_AH),(_B,_AI),(_B,_AJ),(_B,_AK),(_B,_AL),(_B,_AM),(_B,_AN),(_B,_AO),(_B,_AP),(_B,_AQ),(_B,_AR),(_B,_AS),(_B,_AT),(_B,_AU),(_B,_AV),(_B,_AW),(_B,_AX),(_B,_AY),(_B,_AZ),(_B,_Aa),(_B,_Ab),(_B,_Ac),(_B,_Ad),(_B,_Ae),(_B,_Af)))
if mibBuilder.loadTexts:cmDsx1AlarmGroup.setStatus(_A)
cmDsx1Compliance=ModuleCompliance((1,3,6,1,4,1,351,150,58,2,2,1))
cmDsx1Compliance.setObjects(*((_B,_Ag),(_B,_Ah),(_B,_Ai),(_B,_Aj),(_B,_Ak)))
if mibBuilder.loadTexts:cmDsx1Compliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'dsx1CnfGrp':dsx1CnfGrp,'dsx1CnfGrpTable':dsx1CnfGrpTable,'dsx1CnfGrpEntry':dsx1CnfGrpEntry,_F:lineNum,_R:lineConnectorType,_S:lineEnable,_T:lineType,_U:lineCoding,_V:lineLength,_W:lineXmtClockSource,_X:lineLoopbackCommand,_Y:lineSendCode,_a:lineUsedTimeslotsBitMap,_Z:lineLoopbackCodeDetection,_b:lineBERTEnable,_c:lineBERTPattern,_d:lineBERTResult,_e:bERTResultClrButton,_Q:lineNumofValidEntries,'dsx1AlmCnfGrp':dsx1AlmCnfGrp,'dsx1AlmCnfGrpTable':dsx1AlmCnfGrpTable,'dsx1AlmCnfGrpEntry':dsx1AlmCnfGrpEntry,_I:almCnfLineNum,_k:redSeverity,_l:rAISeverity,_m:nEAlarmUpCount,_n:nEAlarmDownCount,_o:nEAlarmThreshold,_p:fEAlarmUpCount,_q:fEAlarmDownCount,_r:fEAlarmThreshold,_s:statisticalAlarmSeverity,_t:lCV15MinThreshold,_u:lCV24HrThreshold,_v:lES15MinThreshold,_w:lES24HrThreshold,_x:lSES15MinThreshold,_y:lSES24HrThreshold,_z:cRC15MinThreshold,_A0:cRC24HrThreshold,_A1:cRCES15MinThreshold,_A2:cRCES24HrThreshold,_A3:cRCSES15MinThreshold,_A4:cRCSES24HrThreshold,_A5:sEFS15MinThreshold,_A6:sEFS24HrThreshold,_A7:aISS15MinThreshold,_A8:aISS24HrThreshold,_A9:uAS15MinThreshold,_AA:uAS24HrThreshold,'dsx1AlmGrp':dsx1AlmGrp,'dsx1AlmGrpTable':dsx1AlmGrpTable,'dsx1AlmGrpEntry':dsx1AlmGrpEntry,_L:almLineNum,_AB:lineAlarmState,_AC:lineStatisticalAlarmState,_AD:lCVCurrent,_AE:lCV15MinBucket,_AF:lCV24HrBucket,_AG:lESCurrent,_AH:lES15MinBucket,_AI:lES24HrBucket,_AJ:lSESCurrent,_AK:lSES15MinBucket,_AL:lSES24HrBucket,_AM:cRCCurrent,_AN:cRC15MinBucket,_AO:cRC24HrBucket,_AP:cRCESCurrent,_AQ:cRCES15MinBucket,_AR:cRCES24HrBucket,_AS:cRCSESCurrent,_AT:cRCSES15MinBucket,_AU:cRCSES24HrBucket,_AV:sEFSCurrent,_AW:sEFS15MinBucket,_AX:sEFS24HrBucket,_AY:aISSCurrent,_AZ:aISS15MinBucket,_Aa:aISS24HrBucket,_Ab:uASCurrent,_Ac:uAS15MinBucket,_Ad:uAS24HrBucket,_Ae:percentEFS,_Af:alarmClrButton,'dsx1CntGrp':dsx1CntGrp,'dsx1CntGrpTable':dsx1CntGrpTable,'dsx1CntGrpEntry':dsx1CntGrpEntry,_M:cntLineNum,_f:rcvLOSCount,_g:rcvOOFCount,_h:rcvRAICount,_i:rcvFECount,_j:counterClearButton,'ciscoMgx82xxDsx1MIB':ciscoMgx82xxDsx1MIB,'cmDsx1MIBConformance':cmDsx1MIBConformance,'cmDsx1MIBGroups':cmDsx1MIBGroups,_Ag:cmDsx1GeneralGroup,_Ah:cmDsx1ConfGroup,_Ai:cmDsx1CountGroup,_Aj:cmDsx1AlarmConfGroup,_Ak:cmDsx1AlarmGroup,'cmDsx1MIBCompliances':cmDsx1MIBCompliances,'cmDsx1Compliance':cmDsx1Compliance})