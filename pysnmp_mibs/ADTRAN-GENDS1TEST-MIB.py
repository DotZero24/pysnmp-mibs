_a='adGenDS1TestPatternResetCount'
_Z='adGenDS1TestPatternInsertError'
_Y='adGenDS1TestPatternErrorsRcvd'
_X='adGenDS1TestPatternSync'
_W='adGenDS1TestPatternType'
_V='adGenDS1TestFarEndFAC2NIUInwardRequest'
_U='adGenDS1TestFarEndCSUInwardRequest'
_T='adGenDS1TestFarEndFAC2NIURequest'
_S='adGenDS1TestFarEndFEACRequest'
_R='adGenDS1TestFarEndFDLRequest'
_Q='adGenDS1TestFarEndCSURequest'
_P='adGenDS1TestFarEndLpbkType'
_O='adGenDS1TestNearEndLoopbackType'
_N='adGenDS1TestTimeElapsed'
_M='adGenDS1TestTimeRemaining'
_L='adGenDS1TestStatus'
_K='adGenDS1TestStartStop'
_J='adGenDS1TestTimeout'
_I='read-only'
_H='ifIndex'
_G='IF-MIB'
_F='disable'
_E='enable'
_D='read-write'
_C='Integer32'
_B='ADTRAN-GENDS1TEST-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
adGenPortTrapIdentifier,=mibBuilder.importSymbols('ADTRAN-GENPORT-MIB','adGenPortTrapIdentifier')
adGenSlotInfoIndex,=mibBuilder.importSymbols('ADTRAN-GENSLOT-MIB','adGenSlotInfoIndex')
adTrapInformSeqNum,=mibBuilder.importSymbols('ADTRAN-GENTRAPINFORM-MIB','adTrapInformSeqNum')
adShared,=mibBuilder.importSymbols('ADTRAN-MIB','adShared')
adDS1,adGenDS1TestID=mibBuilder.importSymbols('ADTRAN-SHARED-DS1-MIB','adDS1','adGenDS1TestID')
ifIndex,=mibBuilder.importSymbols(_G,_H)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
sysName,=mibBuilder.importSymbols('SNMPv2-MIB','sysName')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
adGenDS1TestIdentity=ModuleIdentity((1,3,6,1,4,1,664,6,10000,78,1,1))
if mibBuilder.loadTexts:adGenDS1TestIdentity.setRevisions(('2014-05-06 00:00','2011-08-22 00:00','2011-07-12 00:00','2011-03-24 00:00','2008-09-18 00:00'))
_AdGenDS1Test_ObjectIdentity=ObjectIdentity
adGenDS1Test=_AdGenDS1Test_ObjectIdentity((1,3,6,1,4,1,664,5,78,1))
_AdGenDS1TestCommand_ObjectIdentity=ObjectIdentity
adGenDS1TestCommand=_AdGenDS1TestCommand_ObjectIdentity((1,3,6,1,4,1,664,5,78,1,1))
_AdGenDS1TestCommandTable_Object=MibTable
adGenDS1TestCommandTable=_AdGenDS1TestCommandTable_Object((1,3,6,1,4,1,664,5,78,1,1,1))
if mibBuilder.loadTexts:adGenDS1TestCommandTable.setStatus(_A)
_AdGenDS1TestCommandEntry_Object=MibTableRow
adGenDS1TestCommandEntry=_AdGenDS1TestCommandEntry_Object((1,3,6,1,4,1,664,5,78,1,1,1,1))
adGenDS1TestCommandEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:adGenDS1TestCommandEntry.setStatus(_A)
_AdGenDS1TestTimeout_Type=Integer32
_AdGenDS1TestTimeout_Object=MibTableColumn
adGenDS1TestTimeout=_AdGenDS1TestTimeout_Object((1,3,6,1,4,1,664,5,78,1,1,1,1,1),_AdGenDS1TestTimeout_Type())
adGenDS1TestTimeout.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenDS1TestTimeout.setStatus(_A)
class _AdGenDS1TestStartStop_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('nearEndStart',1),('farEndStart',2),('allStop',3)))
_AdGenDS1TestStartStop_Type.__name__=_C
_AdGenDS1TestStartStop_Object=MibTableColumn
adGenDS1TestStartStop=_AdGenDS1TestStartStop_Object((1,3,6,1,4,1,664,5,78,1,1,1,1,2),_AdGenDS1TestStartStop_Type())
adGenDS1TestStartStop.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenDS1TestStartStop.setStatus(_A)
class _AdGenDS1TestStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50)));namedValues=NamedValues(*(('none',1),('nearEndLine',2),('nearEndPayload',3),('nearEndCsu',4),('nearEndFdlPayload',5),('nearEndFeacLine',6),('pattQrss',7),('pattOneInEight',8),('pattAllOnes',9),('pattAllZeros',10),('farEndPattQrssCsu',11),('farEndPattOneInEightCsu',12),('farEndPattAllOnesCsu',13),('farEndPattAllZerosCsu',14),('farEndPattQrssFdlPayload',15),('farEndPattOneInEightFdlPayload',16),('farEndPattAllOnesFdlPayload',17),('farEndPattAllZerosFdlPayload',18),('farEndPattQrssFac2niu',19),('farEndPattOneInEightFac2niu',20),('farEndPattAllOnesFac2niu',21),('farEndPattAllZerosFac2niu',22),('farEndPattQrssFeac',23),('farEndPattOneInEightFeac',24),('farEndPattAllOnesFeac',25),('farEndPattAllZerosFeac',26),('nearEndFac2niu',27),('farEndCsu',28),('farEndFdlPayload',29),('farEndFac2Niu',30),('farEndFeac',31),('nearEndInward',32),('nearEndCsuInward',33),('nearEndFac2niuInward',34),('pattTwoInEight',35),('pattThreeInTwentyFour',36),('patt2to23',37),('patt2to15',38),('patt2to20',39),('patt511',40),('farEndPattTwoInEightCsu',41),('farEndPattTwoInEightFdlPayload',42),('farEndPattTwoInEightFac2Niu',43),('farEndPattTwoInEightFeac',44),('farEndPattThreeInTwentyFourCsu',45),('farEndPattThreeInTwentyFourFdlPayload',46),('farEndPattThreeInTwentyFourFac2Niu',47),('farEndPattThreeInTwentyFourFeac',48),('farEndFdlLine',49),('farEndNiuInband',50)))
_AdGenDS1TestStatus_Type.__name__=_C
_AdGenDS1TestStatus_Object=MibTableColumn
adGenDS1TestStatus=_AdGenDS1TestStatus_Object((1,3,6,1,4,1,664,5,78,1,1,1,1,3),_AdGenDS1TestStatus_Type())
adGenDS1TestStatus.setMaxAccess(_I)
if mibBuilder.loadTexts:adGenDS1TestStatus.setStatus(_A)
_AdGenDS1TestTimeRemaining_Type=Unsigned32
_AdGenDS1TestTimeRemaining_Object=MibTableColumn
adGenDS1TestTimeRemaining=_AdGenDS1TestTimeRemaining_Object((1,3,6,1,4,1,664,5,78,1,1,1,1,4),_AdGenDS1TestTimeRemaining_Type())
adGenDS1TestTimeRemaining.setMaxAccess(_I)
if mibBuilder.loadTexts:adGenDS1TestTimeRemaining.setStatus(_A)
_AdGenDS1TestTimeElapsed_Type=Unsigned32
_AdGenDS1TestTimeElapsed_Object=MibTableColumn
adGenDS1TestTimeElapsed=_AdGenDS1TestTimeElapsed_Object((1,3,6,1,4,1,664,5,78,1,1,1,1,5),_AdGenDS1TestTimeElapsed_Type())
adGenDS1TestTimeElapsed.setMaxAccess(_I)
if mibBuilder.loadTexts:adGenDS1TestTimeElapsed.setStatus(_A)
_AdGenDS1TestNearEndLoopback_ObjectIdentity=ObjectIdentity
adGenDS1TestNearEndLoopback=_AdGenDS1TestNearEndLoopback_ObjectIdentity((1,3,6,1,4,1,664,5,78,1,2))
_AdGenDS1TestNearEndLoopbackTable_Object=MibTable
adGenDS1TestNearEndLoopbackTable=_AdGenDS1TestNearEndLoopbackTable_Object((1,3,6,1,4,1,664,5,78,1,2,1))
if mibBuilder.loadTexts:adGenDS1TestNearEndLoopbackTable.setStatus(_A)
_AdGenDS1TestNearEndLoopbackEntry_Object=MibTableRow
adGenDS1TestNearEndLoopbackEntry=_AdGenDS1TestNearEndLoopbackEntry_Object((1,3,6,1,4,1,664,5,78,1,2,1,1))
adGenDS1TestNearEndLoopbackEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:adGenDS1TestNearEndLoopbackEntry.setStatus(_A)
class _AdGenDS1TestNearEndLoopbackType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('line',1),('payload',2),('inward',3)))
_AdGenDS1TestNearEndLoopbackType_Type.__name__=_C
_AdGenDS1TestNearEndLoopbackType_Object=MibTableColumn
adGenDS1TestNearEndLoopbackType=_AdGenDS1TestNearEndLoopbackType_Object((1,3,6,1,4,1,664,5,78,1,2,1,1,1),_AdGenDS1TestNearEndLoopbackType_Type())
adGenDS1TestNearEndLoopbackType.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenDS1TestNearEndLoopbackType.setStatus(_A)
_AdGenDS1TestFarEndLoopback_ObjectIdentity=ObjectIdentity
adGenDS1TestFarEndLoopback=_AdGenDS1TestFarEndLoopback_ObjectIdentity((1,3,6,1,4,1,664,5,78,1,3))
_AdGenDS1TestFarEndLoopbackTable_Object=MibTable
adGenDS1TestFarEndLoopbackTable=_AdGenDS1TestFarEndLoopbackTable_Object((1,3,6,1,4,1,664,5,78,1,3,1))
if mibBuilder.loadTexts:adGenDS1TestFarEndLoopbackTable.setStatus(_A)
_AdGenDS1TestFarEndLoopbackEntry_Object=MibTableRow
adGenDS1TestFarEndLoopbackEntry=_AdGenDS1TestFarEndLoopbackEntry_Object((1,3,6,1,4,1,664,5,78,1,3,1,1))
adGenDS1TestFarEndLoopbackEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:adGenDS1TestFarEndLoopbackEntry.setStatus(_A)
class _AdGenDS1TestFarEndLpbkType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('none',1),('csu',2),('fdlPayload',3),('fac2niu',4),('feac',5),('fdlLine',6),('niuInband',7)))
_AdGenDS1TestFarEndLpbkType_Type.__name__=_C
_AdGenDS1TestFarEndLpbkType_Object=MibTableColumn
adGenDS1TestFarEndLpbkType=_AdGenDS1TestFarEndLpbkType_Object((1,3,6,1,4,1,664,5,78,1,3,1,1,1),_AdGenDS1TestFarEndLpbkType_Type())
adGenDS1TestFarEndLpbkType.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenDS1TestFarEndLpbkType.setStatus(_A)
class _AdGenDS1TestFarEndCSURequest_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_AdGenDS1TestFarEndCSURequest_Type.__name__=_C
_AdGenDS1TestFarEndCSURequest_Object=MibTableColumn
adGenDS1TestFarEndCSURequest=_AdGenDS1TestFarEndCSURequest_Object((1,3,6,1,4,1,664,5,78,1,3,1,1,2),_AdGenDS1TestFarEndCSURequest_Type())
adGenDS1TestFarEndCSURequest.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenDS1TestFarEndCSURequest.setStatus(_A)
class _AdGenDS1TestFarEndFDLRequest_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_AdGenDS1TestFarEndFDLRequest_Type.__name__=_C
_AdGenDS1TestFarEndFDLRequest_Object=MibTableColumn
adGenDS1TestFarEndFDLRequest=_AdGenDS1TestFarEndFDLRequest_Object((1,3,6,1,4,1,664,5,78,1,3,1,1,3),_AdGenDS1TestFarEndFDLRequest_Type())
adGenDS1TestFarEndFDLRequest.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenDS1TestFarEndFDLRequest.setStatus(_A)
class _AdGenDS1TestFarEndFEACRequest_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_AdGenDS1TestFarEndFEACRequest_Type.__name__=_C
_AdGenDS1TestFarEndFEACRequest_Object=MibTableColumn
adGenDS1TestFarEndFEACRequest=_AdGenDS1TestFarEndFEACRequest_Object((1,3,6,1,4,1,664,5,78,1,3,1,1,4),_AdGenDS1TestFarEndFEACRequest_Type())
adGenDS1TestFarEndFEACRequest.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenDS1TestFarEndFEACRequest.setStatus(_A)
class _AdGenDS1TestFarEndFAC2NIURequest_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_AdGenDS1TestFarEndFAC2NIURequest_Type.__name__=_C
_AdGenDS1TestFarEndFAC2NIURequest_Object=MibTableColumn
adGenDS1TestFarEndFAC2NIURequest=_AdGenDS1TestFarEndFAC2NIURequest_Object((1,3,6,1,4,1,664,5,78,1,3,1,1,5),_AdGenDS1TestFarEndFAC2NIURequest_Type())
adGenDS1TestFarEndFAC2NIURequest.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenDS1TestFarEndFAC2NIURequest.setStatus(_A)
class _AdGenDS1TestFarEndCSUInwardRequest_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_AdGenDS1TestFarEndCSUInwardRequest_Type.__name__=_C
_AdGenDS1TestFarEndCSUInwardRequest_Object=MibTableColumn
adGenDS1TestFarEndCSUInwardRequest=_AdGenDS1TestFarEndCSUInwardRequest_Object((1,3,6,1,4,1,664,5,78,1,3,1,1,6),_AdGenDS1TestFarEndCSUInwardRequest_Type())
adGenDS1TestFarEndCSUInwardRequest.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenDS1TestFarEndCSUInwardRequest.setStatus(_A)
class _AdGenDS1TestFarEndFAC2NIUInwardRequest_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_AdGenDS1TestFarEndFAC2NIUInwardRequest_Type.__name__=_C
_AdGenDS1TestFarEndFAC2NIUInwardRequest_Object=MibTableColumn
adGenDS1TestFarEndFAC2NIUInwardRequest=_AdGenDS1TestFarEndFAC2NIUInwardRequest_Object((1,3,6,1,4,1,664,5,78,1,3,1,1,7),_AdGenDS1TestFarEndFAC2NIUInwardRequest_Type())
adGenDS1TestFarEndFAC2NIUInwardRequest.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenDS1TestFarEndFAC2NIUInwardRequest.setStatus(_A)
_AdGenDS1TestPattern_ObjectIdentity=ObjectIdentity
adGenDS1TestPattern=_AdGenDS1TestPattern_ObjectIdentity((1,3,6,1,4,1,664,5,78,1,4))
_AdGenDS1TestPatternTable_Object=MibTable
adGenDS1TestPatternTable=_AdGenDS1TestPatternTable_Object((1,3,6,1,4,1,664,5,78,1,4,1))
if mibBuilder.loadTexts:adGenDS1TestPatternTable.setStatus(_A)
_AdGenDS1TestPatternEntry_Object=MibTableRow
adGenDS1TestPatternEntry=_AdGenDS1TestPatternEntry_Object((1,3,6,1,4,1,664,5,78,1,4,1,1))
adGenDS1TestPatternEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:adGenDS1TestPatternEntry.setStatus(_A)
class _AdGenDS1TestPatternType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12)));namedValues=NamedValues(*(('notUsed1',1),('qrss',2),('notUsed3',3),('allOnes',4),('allZeros',5),('notUsed6',6),('notUsed7',7),('notUsed8',8),('notUsed9',9),('oneInEight',10),('twoInEight',11),('threeInTwentyFour',12)))
_AdGenDS1TestPatternType_Type.__name__=_C
_AdGenDS1TestPatternType_Object=MibTableColumn
adGenDS1TestPatternType=_AdGenDS1TestPatternType_Object((1,3,6,1,4,1,664,5,78,1,4,1,1,1),_AdGenDS1TestPatternType_Type())
adGenDS1TestPatternType.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenDS1TestPatternType.setStatus(_A)
class _AdGenDS1TestPatternSync_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('true',1),('false',2)))
_AdGenDS1TestPatternSync_Type.__name__=_C
_AdGenDS1TestPatternSync_Object=MibTableColumn
adGenDS1TestPatternSync=_AdGenDS1TestPatternSync_Object((1,3,6,1,4,1,664,5,78,1,4,1,1,2),_AdGenDS1TestPatternSync_Type())
adGenDS1TestPatternSync.setMaxAccess(_I)
if mibBuilder.loadTexts:adGenDS1TestPatternSync.setStatus(_A)
_AdGenDS1TestPatternErrorsRcvd_Type=Gauge32
_AdGenDS1TestPatternErrorsRcvd_Object=MibTableColumn
adGenDS1TestPatternErrorsRcvd=_AdGenDS1TestPatternErrorsRcvd_Object((1,3,6,1,4,1,664,5,78,1,4,1,1,3),_AdGenDS1TestPatternErrorsRcvd_Type())
adGenDS1TestPatternErrorsRcvd.setMaxAccess(_I)
if mibBuilder.loadTexts:adGenDS1TestPatternErrorsRcvd.setStatus(_A)
class _AdGenDS1TestPatternInsertError_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('insert',1))
_AdGenDS1TestPatternInsertError_Type.__name__=_C
_AdGenDS1TestPatternInsertError_Object=MibTableColumn
adGenDS1TestPatternInsertError=_AdGenDS1TestPatternInsertError_Object((1,3,6,1,4,1,664,5,78,1,4,1,1,4),_AdGenDS1TestPatternInsertError_Type())
adGenDS1TestPatternInsertError.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenDS1TestPatternInsertError.setStatus(_A)
class _AdGenDS1TestPatternResetCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('reset',1))
_AdGenDS1TestPatternResetCount_Type.__name__=_C
_AdGenDS1TestPatternResetCount_Object=MibTableColumn
adGenDS1TestPatternResetCount=_AdGenDS1TestPatternResetCount_Object((1,3,6,1,4,1,664,5,78,1,4,1,1,5),_AdGenDS1TestPatternResetCount_Type())
adGenDS1TestPatternResetCount.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenDS1TestPatternResetCount.setStatus(_A)
_AdGenDS1TestMibConformance_ObjectIdentity=ObjectIdentity
adGenDS1TestMibConformance=_AdGenDS1TestMibConformance_ObjectIdentity((1,3,6,1,4,1,664,5,78,1,5))
_AdGenDS1TestMibGroups_ObjectIdentity=ObjectIdentity
adGenDS1TestMibGroups=_AdGenDS1TestMibGroups_ObjectIdentity((1,3,6,1,4,1,664,5,78,1,5,1))
adGenDS1TestGroup=ObjectGroup((1,3,6,1,4,1,664,5,78,1,5,1,1))
adGenDS1TestGroup.setObjects(*((_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a)))
if mibBuilder.loadTexts:adGenDS1TestGroup.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'adGenDS1Test':adGenDS1Test,'adGenDS1TestCommand':adGenDS1TestCommand,'adGenDS1TestCommandTable':adGenDS1TestCommandTable,'adGenDS1TestCommandEntry':adGenDS1TestCommandEntry,_J:adGenDS1TestTimeout,_K:adGenDS1TestStartStop,_L:adGenDS1TestStatus,_M:adGenDS1TestTimeRemaining,_N:adGenDS1TestTimeElapsed,'adGenDS1TestNearEndLoopback':adGenDS1TestNearEndLoopback,'adGenDS1TestNearEndLoopbackTable':adGenDS1TestNearEndLoopbackTable,'adGenDS1TestNearEndLoopbackEntry':adGenDS1TestNearEndLoopbackEntry,_O:adGenDS1TestNearEndLoopbackType,'adGenDS1TestFarEndLoopback':adGenDS1TestFarEndLoopback,'adGenDS1TestFarEndLoopbackTable':adGenDS1TestFarEndLoopbackTable,'adGenDS1TestFarEndLoopbackEntry':adGenDS1TestFarEndLoopbackEntry,_P:adGenDS1TestFarEndLpbkType,_Q:adGenDS1TestFarEndCSURequest,_R:adGenDS1TestFarEndFDLRequest,_S:adGenDS1TestFarEndFEACRequest,_T:adGenDS1TestFarEndFAC2NIURequest,_U:adGenDS1TestFarEndCSUInwardRequest,_V:adGenDS1TestFarEndFAC2NIUInwardRequest,'adGenDS1TestPattern':adGenDS1TestPattern,'adGenDS1TestPatternTable':adGenDS1TestPatternTable,'adGenDS1TestPatternEntry':adGenDS1TestPatternEntry,_W:adGenDS1TestPatternType,_X:adGenDS1TestPatternSync,_Y:adGenDS1TestPatternErrorsRcvd,_Z:adGenDS1TestPatternInsertError,_a:adGenDS1TestPatternResetCount,'adGenDS1TestMibConformance':adGenDS1TestMibConformance,'adGenDS1TestMibGroups':adGenDS1TestMibGroups,'adGenDS1TestGroup':adGenDS1TestGroup,'adGenDS1TestIdentity':adGenDS1TestIdentity})