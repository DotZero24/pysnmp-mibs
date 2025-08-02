_b='cmDsx3BertConfGroup'
_a='dsx3bertCleanupAction'
_Z='dsx3bertErrorInjectCount'
_Y='dsx3bertErrorInsertionRate'
_X='dsx3bertBitErrorCountLower'
_W='dsx3bertBitErrorCountUpper'
_V='dsx3bertBitCountLower'
_U='dsx3bertBitCountUpper'
_T='dsx3bertStartDate'
_S='dsx3bertStartTime'
_R='dsx3bertLoopback'
_Q='dsx3bertPattern'
_P='dsx3bertMode'
_O='dsx3bertLine'
_N='dsx3bertPort'
_M='dsx3bertTestMedium'
_L='dsx3bertStatus'
_K='dsx3bertUserId'
_J='dsx3bertOwner'
_I='dsx3bertResourceStatus'
_H='dsx3bertControl'
_G='noAction'
_F='DisplayString'
_E='read-write'
_D='read-only'
_C='Integer32'
_B='CISCO-MGX82XX-DSX3-BERT-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
axisDiagnostics,=mibBuilder.importSymbols('BASIS-MIB','axisDiagnostics')
ciscoWan,=mibBuilder.importSymbols('CISCOWAN-SMI','ciscoWan')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_F,'PhysAddress','TextualConvention')
ciscoMgx82xxDsx3BertMIB=ModuleIdentity((1,3,6,1,4,1,351,150,39))
if mibBuilder.loadTexts:ciscoMgx82xxDsx3BertMIB.setRevisions(('2003-01-02 00:00',))
_Dsx3bert_ObjectIdentity=ObjectIdentity
dsx3bert=_Dsx3bert_ObjectIdentity((1,3,6,1,4,1,351,110,6,2))
class _Dsx3bertControl_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6)));namedValues=NamedValues(*((_G,0),('acquireBert',1),('releaseBert',2),('cnfBert',3),('startBert',4),('modBert',5),('delBert',6)))
_Dsx3bertControl_Type.__name__=_C
_Dsx3bertControl_Object=MibScalar
dsx3bertControl=_Dsx3bertControl_Object((1,3,6,1,4,1,351,110,6,2,1),_Dsx3bertControl_Type())
dsx3bertControl.setMaxAccess(_E)
if mibBuilder.loadTexts:dsx3bertControl.setStatus(_A)
class _Dsx3bertResourceStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('free',1),('inUse',2)))
_Dsx3bertResourceStatus_Type.__name__=_C
_Dsx3bertResourceStatus_Object=MibScalar
dsx3bertResourceStatus=_Dsx3bertResourceStatus_Object((1,3,6,1,4,1,351,110,6,2,2),_Dsx3bertResourceStatus_Type())
dsx3bertResourceStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:dsx3bertResourceStatus.setStatus(_A)
_Dsx3bertOwner_Type=DisplayString
_Dsx3bertOwner_Object=MibScalar
dsx3bertOwner=_Dsx3bertOwner_Object((1,3,6,1,4,1,351,110,6,2,3),_Dsx3bertOwner_Type())
dsx3bertOwner.setMaxAccess(_D)
if mibBuilder.loadTexts:dsx3bertOwner.setStatus(_A)
_Dsx3bertUserId_Type=DisplayString
_Dsx3bertUserId_Object=MibScalar
dsx3bertUserId=_Dsx3bertUserId_Object((1,3,6,1,4,1,351,110,6,2,4),_Dsx3bertUserId_Type())
dsx3bertUserId.setMaxAccess(_E)
if mibBuilder.loadTexts:dsx3bertUserId.setStatus(_A)
class _Dsx3bertStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('inactive',1),('bertInSync',2),('bertOutOfSync',3),('farEndInLoop',4),('metallicInLoop',5),('bertFailed',6)))
_Dsx3bertStatus_Type.__name__=_C
_Dsx3bertStatus_Object=MibScalar
dsx3bertStatus=_Dsx3bertStatus_Object((1,3,6,1,4,1,351,110,6,2,5),_Dsx3bertStatus_Type())
dsx3bertStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:dsx3bertStatus.setStatus(_A)
class _Dsx3bertTestMedium_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('port',1),('line',2)))
_Dsx3bertTestMedium_Type.__name__=_C
_Dsx3bertTestMedium_Object=MibScalar
dsx3bertTestMedium=_Dsx3bertTestMedium_Object((1,3,6,1,4,1,351,110,6,2,6),_Dsx3bertTestMedium_Type())
dsx3bertTestMedium.setMaxAccess(_E)
if mibBuilder.loadTexts:dsx3bertTestMedium.setStatus(_A)
class _Dsx3bertPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_Dsx3bertPort_Type.__name__=_C
_Dsx3bertPort_Object=MibScalar
dsx3bertPort=_Dsx3bertPort_Object((1,3,6,1,4,1,351,110,6,2,7),_Dsx3bertPort_Type())
dsx3bertPort.setMaxAccess(_E)
if mibBuilder.loadTexts:dsx3bertPort.setStatus(_A)
class _Dsx3bertLine_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_Dsx3bertLine_Type.__name__=_C
_Dsx3bertLine_Object=MibScalar
dsx3bertLine=_Dsx3bertLine_Object((1,3,6,1,4,1,351,110,6,2,8),_Dsx3bertLine_Type())
dsx3bertLine.setMaxAccess(_E)
if mibBuilder.loadTexts:dsx3bertLine.setStatus(_A)
class _Dsx3bertMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('bertPatternTest',1),('loopback',2)))
_Dsx3bertMode_Type.__name__=_C
_Dsx3bertMode_Object=MibScalar
dsx3bertMode=_Dsx3bertMode_Object((1,3,6,1,4,1,351,110,6,2,9),_Dsx3bertMode_Type())
dsx3bertMode.setMaxAccess(_E)
if mibBuilder.loadTexts:dsx3bertMode.setStatus(_A)
class _Dsx3bertPattern_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33)));namedValues=NamedValues(*(('allOnes',1),('allZeros',2),('alternateOneZero',3),('doubleOneZero',4),('threeInTwentyFour',5),('oneInSixteen',6),('oneInEight',7),('oneInFour',8),('sfLoopUp',9),('sfLoopDown',10),('threeBit',11),('fourBit',12),('fiveBit',13),('sixBit',14),('sevenBit',15),('fracT1LoopUp',16),('fracT1LoopDown',17),('nineBit',18),('tenBit',19),('elevenBit',20),('fifteenBit',21),('seventeenBit',22),('eighteenBit',23),('twentyBit',24),('twentyBitQRSS',25),('twentyOneBit',26),('twentyTwoBit',27),('twentyThreeBit',28),('twentyFiveBit',29),('twentyEightBit',30),('twentyNineBit',31),('thirtyOneBit',32),('thirtyTwo',33)))
_Dsx3bertPattern_Type.__name__=_C
_Dsx3bertPattern_Object=MibScalar
dsx3bertPattern=_Dsx3bertPattern_Object((1,3,6,1,4,1,351,110,6,2,10),_Dsx3bertPattern_Type())
dsx3bertPattern.setMaxAccess(_E)
if mibBuilder.loadTexts:dsx3bertPattern.setStatus(_A)
class _Dsx3bertLoopback_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('farEndLoopback',1),('metallicLoopback',2)))
_Dsx3bertLoopback_Type.__name__=_C
_Dsx3bertLoopback_Object=MibScalar
dsx3bertLoopback=_Dsx3bertLoopback_Object((1,3,6,1,4,1,351,110,6,2,11),_Dsx3bertLoopback_Type())
dsx3bertLoopback.setMaxAccess(_E)
if mibBuilder.loadTexts:dsx3bertLoopback.setStatus(_A)
class _Dsx3bertStartTime_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,0),ValueSizeConstraint(8,8))
_Dsx3bertStartTime_Type.__name__=_F
_Dsx3bertStartTime_Object=MibScalar
dsx3bertStartTime=_Dsx3bertStartTime_Object((1,3,6,1,4,1,351,110,6,2,12),_Dsx3bertStartTime_Type())
dsx3bertStartTime.setMaxAccess(_D)
if mibBuilder.loadTexts:dsx3bertStartTime.setStatus(_A)
class _Dsx3bertStartDate_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,0),ValueSizeConstraint(8,8))
_Dsx3bertStartDate_Type.__name__=_F
_Dsx3bertStartDate_Object=MibScalar
dsx3bertStartDate=_Dsx3bertStartDate_Object((1,3,6,1,4,1,351,110,6,2,13),_Dsx3bertStartDate_Type())
dsx3bertStartDate.setMaxAccess(_D)
if mibBuilder.loadTexts:dsx3bertStartDate.setStatus(_A)
class _Dsx3bertBitCountUpper_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_Dsx3bertBitCountUpper_Type.__name__=_C
_Dsx3bertBitCountUpper_Object=MibScalar
dsx3bertBitCountUpper=_Dsx3bertBitCountUpper_Object((1,3,6,1,4,1,351,110,6,2,14),_Dsx3bertBitCountUpper_Type())
dsx3bertBitCountUpper.setMaxAccess(_D)
if mibBuilder.loadTexts:dsx3bertBitCountUpper.setStatus(_A)
class _Dsx3bertBitCountLower_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_Dsx3bertBitCountLower_Type.__name__=_C
_Dsx3bertBitCountLower_Object=MibScalar
dsx3bertBitCountLower=_Dsx3bertBitCountLower_Object((1,3,6,1,4,1,351,110,6,2,15),_Dsx3bertBitCountLower_Type())
dsx3bertBitCountLower.setMaxAccess(_D)
if mibBuilder.loadTexts:dsx3bertBitCountLower.setStatus(_A)
class _Dsx3bertBitErrorCountUpper_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_Dsx3bertBitErrorCountUpper_Type.__name__=_C
_Dsx3bertBitErrorCountUpper_Object=MibScalar
dsx3bertBitErrorCountUpper=_Dsx3bertBitErrorCountUpper_Object((1,3,6,1,4,1,351,110,6,2,16),_Dsx3bertBitErrorCountUpper_Type())
dsx3bertBitErrorCountUpper.setMaxAccess(_D)
if mibBuilder.loadTexts:dsx3bertBitErrorCountUpper.setStatus(_A)
class _Dsx3bertBitErrorCountLower_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_Dsx3bertBitErrorCountLower_Type.__name__=_C
_Dsx3bertBitErrorCountLower_Object=MibScalar
dsx3bertBitErrorCountLower=_Dsx3bertBitErrorCountLower_Object((1,3,6,1,4,1,351,110,6,2,17),_Dsx3bertBitErrorCountLower_Type())
dsx3bertBitErrorCountLower.setMaxAccess(_D)
if mibBuilder.loadTexts:dsx3bertBitErrorCountLower.setStatus(_A)
class _Dsx3bertErrorInsertionRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('errorInsertionDisabled',1),('oneInTen',2),('oneInTenPowerTwo',3),('oneInTenPowerThree',4),('oneInTenPowerFour',5),('oneInTenPowerFive',6),('oneInTenPowerSix',7),('oneInTenPowerSeven',8)))
_Dsx3bertErrorInsertionRate_Type.__name__=_C
_Dsx3bertErrorInsertionRate_Object=MibScalar
dsx3bertErrorInsertionRate=_Dsx3bertErrorInsertionRate_Object((1,3,6,1,4,1,351,110,6,2,18),_Dsx3bertErrorInsertionRate_Type())
dsx3bertErrorInsertionRate.setMaxAccess(_E)
if mibBuilder.loadTexts:dsx3bertErrorInsertionRate.setStatus(_A)
class _Dsx3bertErrorInjectCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_Dsx3bertErrorInjectCount_Type.__name__=_C
_Dsx3bertErrorInjectCount_Object=MibScalar
dsx3bertErrorInjectCount=_Dsx3bertErrorInjectCount_Object((1,3,6,1,4,1,351,110,6,2,19),_Dsx3bertErrorInjectCount_Type())
dsx3bertErrorInjectCount.setMaxAccess(_D)
if mibBuilder.loadTexts:dsx3bertErrorInjectCount.setStatus(_A)
class _Dsx3bertCleanupAction_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_G,1),('smCleanup',2),('metallicLoopdown',3)))
_Dsx3bertCleanupAction_Type.__name__=_C
_Dsx3bertCleanupAction_Object=MibScalar
dsx3bertCleanupAction=_Dsx3bertCleanupAction_Object((1,3,6,1,4,1,351,110,6,2,20),_Dsx3bertCleanupAction_Type())
dsx3bertCleanupAction.setMaxAccess(_D)
if mibBuilder.loadTexts:dsx3bertCleanupAction.setStatus(_A)
_CmDsx3BertMIBConformance_ObjectIdentity=ObjectIdentity
cmDsx3BertMIBConformance=_CmDsx3BertMIBConformance_ObjectIdentity((1,3,6,1,4,1,351,150,39,2))
_CmDsx3BertMIBGroups_ObjectIdentity=ObjectIdentity
cmDsx3BertMIBGroups=_CmDsx3BertMIBGroups_ObjectIdentity((1,3,6,1,4,1,351,150,39,2,1))
_CmDsx3BertMIBCompliances_ObjectIdentity=ObjectIdentity
cmDsx3BertMIBCompliances=_CmDsx3BertMIBCompliances_ObjectIdentity((1,3,6,1,4,1,351,150,39,2,2))
cmDsx3BertConfGroup=ObjectGroup((1,3,6,1,4,1,351,150,39,2,1,1))
cmDsx3BertConfGroup.setObjects(*((_B,_H),(_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a)))
if mibBuilder.loadTexts:cmDsx3BertConfGroup.setStatus(_A)
cmDsx3BertCompliance=ModuleCompliance((1,3,6,1,4,1,351,150,39,2,2,1))
cmDsx3BertCompliance.setObjects((_B,_b))
if mibBuilder.loadTexts:cmDsx3BertCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'dsx3bert':dsx3bert,_H:dsx3bertControl,_I:dsx3bertResourceStatus,_J:dsx3bertOwner,_K:dsx3bertUserId,_L:dsx3bertStatus,_M:dsx3bertTestMedium,_N:dsx3bertPort,_O:dsx3bertLine,_P:dsx3bertMode,_Q:dsx3bertPattern,_R:dsx3bertLoopback,_S:dsx3bertStartTime,_T:dsx3bertStartDate,_U:dsx3bertBitCountUpper,_V:dsx3bertBitCountLower,_W:dsx3bertBitErrorCountUpper,_X:dsx3bertBitErrorCountLower,_Y:dsx3bertErrorInsertionRate,_Z:dsx3bertErrorInjectCount,_a:dsx3bertCleanupAction,'ciscoMgx82xxDsx3BertMIB':ciscoMgx82xxDsx3BertMIB,'cmDsx3BertMIBConformance':cmDsx3BertMIBConformance,'cmDsx3BertMIBGroups':cmDsx3BertMIBGroups,_b:cmDsx3BertConfGroup,'cmDsx3BertMIBCompliances':cmDsx3BertMIBCompliances,'cmDsx3BertCompliance':cmDsx3BertCompliance})