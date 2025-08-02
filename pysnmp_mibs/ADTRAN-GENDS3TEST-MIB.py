_S='adGenDS3TestPatternResetCount'
_R='adGenDS3TestPatternInsertError'
_Q='adGenDS3TestPatternErrorsRcvd'
_P='adGenDS3TestPatternSync'
_O='adGenDS3TestPatternType'
_N='adGenDS3TestFarEndLpbkType'
_M='adGenDS3TestNearEndLoopbackType'
_L='adGenDS3TestTimeElapsed'
_K='adGenDS3TestTimeRemaining'
_J='adGenDS3TestStatus'
_I='adGenDS3TestStartStop'
_H='adGenDS3TestTimeout'
_G='read-only'
_F='ifIndex'
_E='IF-MIB'
_D='read-write'
_C='Integer32'
_B='ADTRAN-GENDS3TEST-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
adGenPortTrapIdentifier,=mibBuilder.importSymbols('ADTRAN-GENPORT-MIB','adGenPortTrapIdentifier')
adGenSlotInfoIndex,=mibBuilder.importSymbols('ADTRAN-GENSLOT-MIB','adGenSlotInfoIndex')
adTrapInformSeqNum,=mibBuilder.importSymbols('ADTRAN-GENTRAPINFORM-MIB','adTrapInformSeqNum')
adGenDS3Test,adGenDS3TestID=mibBuilder.importSymbols('ADTRAN-SHARED-DS3-MIB','adGenDS3Test','adGenDS3TestID')
ifIndex,=mibBuilder.importSymbols(_E,_F)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
sysName,=mibBuilder.importSymbols('SNMPv2-MIB','sysName')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
adGenDS3TestIdentity=ModuleIdentity((1,3,6,1,4,1,664,6,10000,74,1,1))
if mibBuilder.loadTexts:adGenDS3TestIdentity.setRevisions(('2008-04-10 00:00',))
_AdGenDS3TestCommand_ObjectIdentity=ObjectIdentity
adGenDS3TestCommand=_AdGenDS3TestCommand_ObjectIdentity((1,3,6,1,4,1,664,5,74,1,2))
_AdGenDS3TestCommandTable_Object=MibTable
adGenDS3TestCommandTable=_AdGenDS3TestCommandTable_Object((1,3,6,1,4,1,664,5,74,1,2,1))
if mibBuilder.loadTexts:adGenDS3TestCommandTable.setStatus(_A)
_AdGenDS3TestCommandEntry_Object=MibTableRow
adGenDS3TestCommandEntry=_AdGenDS3TestCommandEntry_Object((1,3,6,1,4,1,664,5,74,1,2,1,1))
adGenDS3TestCommandEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:adGenDS3TestCommandEntry.setStatus(_A)
_AdGenDS3TestTimeout_Type=Integer32
_AdGenDS3TestTimeout_Object=MibTableColumn
adGenDS3TestTimeout=_AdGenDS3TestTimeout_Object((1,3,6,1,4,1,664,5,74,1,2,1,1,1),_AdGenDS3TestTimeout_Type())
adGenDS3TestTimeout.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenDS3TestTimeout.setStatus(_A)
class _AdGenDS3TestStartStop_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('nearEndStart',1),('farEndStart',2),('allStop',3)))
_AdGenDS3TestStartStop_Type.__name__=_C
_AdGenDS3TestStartStop_Object=MibTableColumn
adGenDS3TestStartStop=_AdGenDS3TestStartStop_Object((1,3,6,1,4,1,664,5,74,1,2,1,1,2),_AdGenDS3TestStartStop_Type())
adGenDS3TestStartStop.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenDS3TestStartStop.setStatus(_A)
class _AdGenDS3TestStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11)));namedValues=NamedValues(*(('none',1),('nearEndLine',2),('nearEndPayload',3),('nearEndLineFEAC',4),('farEndPatt2to23',5),('farEndPatt2to20',6),('farEndPatt2to15',7),('farEndPatt2to23LineLpbk',8),('farEndPatt2to20LineLpbk',9),('farEndPatt2to15LineLpbk',10),('farEndLineLpbk',11)))
_AdGenDS3TestStatus_Type.__name__=_C
_AdGenDS3TestStatus_Object=MibTableColumn
adGenDS3TestStatus=_AdGenDS3TestStatus_Object((1,3,6,1,4,1,664,5,74,1,2,1,1,3),_AdGenDS3TestStatus_Type())
adGenDS3TestStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:adGenDS3TestStatus.setStatus(_A)
_AdGenDS3TestTimeRemaining_Type=Unsigned32
_AdGenDS3TestTimeRemaining_Object=MibTableColumn
adGenDS3TestTimeRemaining=_AdGenDS3TestTimeRemaining_Object((1,3,6,1,4,1,664,5,74,1,2,1,1,4),_AdGenDS3TestTimeRemaining_Type())
adGenDS3TestTimeRemaining.setMaxAccess(_G)
if mibBuilder.loadTexts:adGenDS3TestTimeRemaining.setStatus(_A)
_AdGenDS3TestTimeElapsed_Type=Unsigned32
_AdGenDS3TestTimeElapsed_Object=MibTableColumn
adGenDS3TestTimeElapsed=_AdGenDS3TestTimeElapsed_Object((1,3,6,1,4,1,664,5,74,1,2,1,1,5),_AdGenDS3TestTimeElapsed_Type())
adGenDS3TestTimeElapsed.setMaxAccess(_G)
if mibBuilder.loadTexts:adGenDS3TestTimeElapsed.setStatus(_A)
_AdGenDS3TestNearEndLoopback_ObjectIdentity=ObjectIdentity
adGenDS3TestNearEndLoopback=_AdGenDS3TestNearEndLoopback_ObjectIdentity((1,3,6,1,4,1,664,5,74,1,3))
_AdGenDS3TestNearEndLoopbackTable_Object=MibTable
adGenDS3TestNearEndLoopbackTable=_AdGenDS3TestNearEndLoopbackTable_Object((1,3,6,1,4,1,664,5,74,1,3,1))
if mibBuilder.loadTexts:adGenDS3TestNearEndLoopbackTable.setStatus(_A)
_AdGenDS3TestNearEndLoopbackEntry_Object=MibTableRow
adGenDS3TestNearEndLoopbackEntry=_AdGenDS3TestNearEndLoopbackEntry_Object((1,3,6,1,4,1,664,5,74,1,3,1,1))
adGenDS3TestNearEndLoopbackEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:adGenDS3TestNearEndLoopbackEntry.setStatus(_A)
class _AdGenDS3TestNearEndLoopbackType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('line',1),('payload',2)))
_AdGenDS3TestNearEndLoopbackType_Type.__name__=_C
_AdGenDS3TestNearEndLoopbackType_Object=MibTableColumn
adGenDS3TestNearEndLoopbackType=_AdGenDS3TestNearEndLoopbackType_Object((1,3,6,1,4,1,664,5,74,1,3,1,1,1),_AdGenDS3TestNearEndLoopbackType_Type())
adGenDS3TestNearEndLoopbackType.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenDS3TestNearEndLoopbackType.setStatus(_A)
_AdGenDS3TestFarEndLoopback_ObjectIdentity=ObjectIdentity
adGenDS3TestFarEndLoopback=_AdGenDS3TestFarEndLoopback_ObjectIdentity((1,3,6,1,4,1,664,5,74,1,4))
_AdGenDS3TestFarEndLoopbackTable_Object=MibTable
adGenDS3TestFarEndLoopbackTable=_AdGenDS3TestFarEndLoopbackTable_Object((1,3,6,1,4,1,664,5,74,1,4,1))
if mibBuilder.loadTexts:adGenDS3TestFarEndLoopbackTable.setStatus(_A)
_AdGenDS3TestFarEndLoopbackEntry_Object=MibTableRow
adGenDS3TestFarEndLoopbackEntry=_AdGenDS3TestFarEndLoopbackEntry_Object((1,3,6,1,4,1,664,5,74,1,4,1,1))
adGenDS3TestFarEndLoopbackEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:adGenDS3TestFarEndLoopbackEntry.setStatus(_A)
class _AdGenDS3TestFarEndLpbkType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('none',1),('line',2)))
_AdGenDS3TestFarEndLpbkType_Type.__name__=_C
_AdGenDS3TestFarEndLpbkType_Object=MibTableColumn
adGenDS3TestFarEndLpbkType=_AdGenDS3TestFarEndLpbkType_Object((1,3,6,1,4,1,664,5,74,1,4,1,1,1),_AdGenDS3TestFarEndLpbkType_Type())
adGenDS3TestFarEndLpbkType.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenDS3TestFarEndLpbkType.setStatus(_A)
class _AdGenDS3TestFarEndFEACRequest_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enable',1),('disable',2)))
_AdGenDS3TestFarEndFEACRequest_Type.__name__=_C
_AdGenDS3TestFarEndFEACRequest_Object=MibTableColumn
adGenDS3TestFarEndFEACRequest=_AdGenDS3TestFarEndFEACRequest_Object((1,3,6,1,4,1,664,5,74,1,4,1,1,2),_AdGenDS3TestFarEndFEACRequest_Type())
adGenDS3TestFarEndFEACRequest.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenDS3TestFarEndFEACRequest.setStatus(_A)
_AdGenDS3TestPattern_ObjectIdentity=ObjectIdentity
adGenDS3TestPattern=_AdGenDS3TestPattern_ObjectIdentity((1,3,6,1,4,1,664,5,74,1,5))
_AdGenDS3TestPatternTable_Object=MibTable
adGenDS3TestPatternTable=_AdGenDS3TestPatternTable_Object((1,3,6,1,4,1,664,5,74,1,5,1))
if mibBuilder.loadTexts:adGenDS3TestPatternTable.setStatus(_A)
_AdGenDS3TestPatternEntry_Object=MibTableRow
adGenDS3TestPatternEntry=_AdGenDS3TestPatternEntry_Object((1,3,6,1,4,1,664,5,74,1,5,1,1))
adGenDS3TestPatternEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:adGenDS3TestPatternEntry.setStatus(_A)
class _AdGenDS3TestPatternType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('patt2to23',1),('patt2to20',2),('patt2to15',3)))
_AdGenDS3TestPatternType_Type.__name__=_C
_AdGenDS3TestPatternType_Object=MibTableColumn
adGenDS3TestPatternType=_AdGenDS3TestPatternType_Object((1,3,6,1,4,1,664,5,74,1,5,1,1,1),_AdGenDS3TestPatternType_Type())
adGenDS3TestPatternType.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenDS3TestPatternType.setStatus(_A)
class _AdGenDS3TestPatternSync_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('true',1),('false',2)))
_AdGenDS3TestPatternSync_Type.__name__=_C
_AdGenDS3TestPatternSync_Object=MibTableColumn
adGenDS3TestPatternSync=_AdGenDS3TestPatternSync_Object((1,3,6,1,4,1,664,5,74,1,5,1,1,2),_AdGenDS3TestPatternSync_Type())
adGenDS3TestPatternSync.setMaxAccess(_G)
if mibBuilder.loadTexts:adGenDS3TestPatternSync.setStatus(_A)
_AdGenDS3TestPatternErrorsRcvd_Type=Gauge32
_AdGenDS3TestPatternErrorsRcvd_Object=MibTableColumn
adGenDS3TestPatternErrorsRcvd=_AdGenDS3TestPatternErrorsRcvd_Object((1,3,6,1,4,1,664,5,74,1,5,1,1,3),_AdGenDS3TestPatternErrorsRcvd_Type())
adGenDS3TestPatternErrorsRcvd.setMaxAccess(_G)
if mibBuilder.loadTexts:adGenDS3TestPatternErrorsRcvd.setStatus(_A)
class _AdGenDS3TestPatternInsertError_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('insert',1))
_AdGenDS3TestPatternInsertError_Type.__name__=_C
_AdGenDS3TestPatternInsertError_Object=MibTableColumn
adGenDS3TestPatternInsertError=_AdGenDS3TestPatternInsertError_Object((1,3,6,1,4,1,664,5,74,1,5,1,1,4),_AdGenDS3TestPatternInsertError_Type())
adGenDS3TestPatternInsertError.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenDS3TestPatternInsertError.setStatus(_A)
class _AdGenDS3TestPatternResetCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('reset',1))
_AdGenDS3TestPatternResetCount_Type.__name__=_C
_AdGenDS3TestPatternResetCount_Object=MibTableColumn
adGenDS3TestPatternResetCount=_AdGenDS3TestPatternResetCount_Object((1,3,6,1,4,1,664,5,74,1,5,1,1,5),_AdGenDS3TestPatternResetCount_Type())
adGenDS3TestPatternResetCount.setMaxAccess(_D)
if mibBuilder.loadTexts:adGenDS3TestPatternResetCount.setStatus(_A)
_AdGenDS3TestMibConformance_ObjectIdentity=ObjectIdentity
adGenDS3TestMibConformance=_AdGenDS3TestMibConformance_ObjectIdentity((1,3,6,1,4,1,664,5,74,1,6))
_AdGenDS3TestMibGroups_ObjectIdentity=ObjectIdentity
adGenDS3TestMibGroups=_AdGenDS3TestMibGroups_ObjectIdentity((1,3,6,1,4,1,664,5,74,1,6,1))
adGenDS3TestGroup=ObjectGroup((1,3,6,1,4,1,664,5,74,1,6,1,1))
adGenDS3TestGroup.setObjects(*((_B,_H),(_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S)))
if mibBuilder.loadTexts:adGenDS3TestGroup.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'adGenDS3TestCommand':adGenDS3TestCommand,'adGenDS3TestCommandTable':adGenDS3TestCommandTable,'adGenDS3TestCommandEntry':adGenDS3TestCommandEntry,_H:adGenDS3TestTimeout,_I:adGenDS3TestStartStop,_J:adGenDS3TestStatus,_K:adGenDS3TestTimeRemaining,_L:adGenDS3TestTimeElapsed,'adGenDS3TestNearEndLoopback':adGenDS3TestNearEndLoopback,'adGenDS3TestNearEndLoopbackTable':adGenDS3TestNearEndLoopbackTable,'adGenDS3TestNearEndLoopbackEntry':adGenDS3TestNearEndLoopbackEntry,_M:adGenDS3TestNearEndLoopbackType,'adGenDS3TestFarEndLoopback':adGenDS3TestFarEndLoopback,'adGenDS3TestFarEndLoopbackTable':adGenDS3TestFarEndLoopbackTable,'adGenDS3TestFarEndLoopbackEntry':adGenDS3TestFarEndLoopbackEntry,_N:adGenDS3TestFarEndLpbkType,'adGenDS3TestFarEndFEACRequest':adGenDS3TestFarEndFEACRequest,'adGenDS3TestPattern':adGenDS3TestPattern,'adGenDS3TestPatternTable':adGenDS3TestPatternTable,'adGenDS3TestPatternEntry':adGenDS3TestPatternEntry,_O:adGenDS3TestPatternType,_P:adGenDS3TestPatternSync,_Q:adGenDS3TestPatternErrorsRcvd,_R:adGenDS3TestPatternInsertError,_S:adGenDS3TestPatternResetCount,'adGenDS3TestMibConformance':adGenDS3TestMibConformance,'adGenDS3TestMibGroups':adGenDS3TestMibGroups,'adGenDS3TestGroup':adGenDS3TestGroup,'adGenDS3TestIdentity':adGenDS3TestIdentity})