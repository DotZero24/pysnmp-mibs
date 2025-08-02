_h='ccdTdrGroup'
_g='ccdPrbsGroup'
_f='ccdTdrIfResultPairStatus'
_e='ccdTdrIfResultPairLengthUnit'
_d='ccdTdrIfResultPairDistAccuracy'
_c='ccdTdrIfResultPairDistToFault'
_b='ccdTdrIfResultPairLenAccuracy'
_a='ccdTdrIfResultPairLength'
_Z='ccdTdrIfResultPairChannel'
_Y='ccdTdrIfResultValid'
_X='ccdTdrIfLastTestTime'
_W='ccdTdrIfActionStatus'
_V='ccdTdrIfAction'
_U='ccdPrbsIfTestErrorsMaxValue'
_T='ccdPrbsIfTestErrorsResetTime'
_S='ccdPrbsIfTestErrors'
_R='ccdPrbsIfActionStatus'
_Q='ccdPrbsIfAction'
_P='unknown'
_O='ccdTdrIfResultPairIndex'
_N='failedDueToInterfaceDisabled'
_M='failedDueToInternalError'
_L='failedDueToResourceUnavailable'
_K='failedDueToUnknownReason'
_J='succeeded'
_I='read-write'
_H='notRunning'
_G='running'
_F='ifIndex'
_E='IF-MIB'
_D='Integer32'
_C='read-only'
_B='CISCO-CABLE-DIAG-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
ifIndex,=mibBuilder.importSymbols(_E,_F)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TimeStamp','TruthValue')
ciscoCableDiagMIB=ModuleIdentity((1,3,6,1,4,1,9,9,390))
if mibBuilder.loadTexts:ciscoCableDiagMIB.setRevisions(('2004-09-13 00:00','2004-01-15 00:00'))
_CiscoCableDiagMIBNotifs_ObjectIdentity=ObjectIdentity
ciscoCableDiagMIBNotifs=_CiscoCableDiagMIBNotifs_ObjectIdentity((1,3,6,1,4,1,9,9,390,0))
_CiscoCableDiagMIBObjects_ObjectIdentity=ObjectIdentity
ciscoCableDiagMIBObjects=_CiscoCableDiagMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,390,1))
_CcdPrbsObjects_ObjectIdentity=ObjectIdentity
ccdPrbsObjects=_CcdPrbsObjects_ObjectIdentity((1,3,6,1,4,1,9,9,390,1,1))
_CcdPrbsIfTable_Object=MibTable
ccdPrbsIfTable=_CcdPrbsIfTable_Object((1,3,6,1,4,1,9,9,390,1,1,1))
if mibBuilder.loadTexts:ccdPrbsIfTable.setStatus(_A)
_CcdPrbsIfEntry_Object=MibTableRow
ccdPrbsIfEntry=_CcdPrbsIfEntry_Object((1,3,6,1,4,1,9,9,390,1,1,1,1))
ccdPrbsIfEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:ccdPrbsIfEntry.setStatus(_A)
class _CcdPrbsIfAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('start',1),('stop',2),('errorReset',3),(_G,4),(_H,5)))
_CcdPrbsIfAction_Type.__name__=_D
_CcdPrbsIfAction_Object=MibTableColumn
ccdPrbsIfAction=_CcdPrbsIfAction_Object((1,3,6,1,4,1,9,9,390,1,1,1,1,1),_CcdPrbsIfAction_Type())
ccdPrbsIfAction.setMaxAccess(_I)
if mibBuilder.loadTexts:ccdPrbsIfAction.setStatus(_A)
class _CcdPrbsIfActionStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_J,1),(_K,2),(_L,3),(_M,4),('failedDueToTestAlreadyStarted',5),('failedDueToTestAlreadyStopped',6),(_N,7)))
_CcdPrbsIfActionStatus_Type.__name__=_D
_CcdPrbsIfActionStatus_Object=MibTableColumn
ccdPrbsIfActionStatus=_CcdPrbsIfActionStatus_Object((1,3,6,1,4,1,9,9,390,1,1,1,1,2),_CcdPrbsIfActionStatus_Type())
ccdPrbsIfActionStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ccdPrbsIfActionStatus.setStatus(_A)
_CcdPrbsIfTestErrors_Type=Gauge32
_CcdPrbsIfTestErrors_Object=MibTableColumn
ccdPrbsIfTestErrors=_CcdPrbsIfTestErrors_Object((1,3,6,1,4,1,9,9,390,1,1,1,1,3),_CcdPrbsIfTestErrors_Type())
ccdPrbsIfTestErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:ccdPrbsIfTestErrors.setStatus(_A)
_CcdPrbsIfTestErrorsResetTime_Type=TimeStamp
_CcdPrbsIfTestErrorsResetTime_Object=MibTableColumn
ccdPrbsIfTestErrorsResetTime=_CcdPrbsIfTestErrorsResetTime_Object((1,3,6,1,4,1,9,9,390,1,1,1,1,4),_CcdPrbsIfTestErrorsResetTime_Type())
ccdPrbsIfTestErrorsResetTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ccdPrbsIfTestErrorsResetTime.setStatus(_A)
_CcdPrbsIfTestErrorsMaxValue_Type=Unsigned32
_CcdPrbsIfTestErrorsMaxValue_Object=MibTableColumn
ccdPrbsIfTestErrorsMaxValue=_CcdPrbsIfTestErrorsMaxValue_Object((1,3,6,1,4,1,9,9,390,1,1,1,1,5),_CcdPrbsIfTestErrorsMaxValue_Type())
ccdPrbsIfTestErrorsMaxValue.setMaxAccess(_C)
if mibBuilder.loadTexts:ccdPrbsIfTestErrorsMaxValue.setStatus(_A)
_CcdTdrObjects_ObjectIdentity=ObjectIdentity
ccdTdrObjects=_CcdTdrObjects_ObjectIdentity((1,3,6,1,4,1,9,9,390,1,2))
_CcdTdrIfTable_Object=MibTable
ccdTdrIfTable=_CcdTdrIfTable_Object((1,3,6,1,4,1,9,9,390,1,2,1))
if mibBuilder.loadTexts:ccdTdrIfTable.setStatus(_A)
_CcdTdrIfEntry_Object=MibTableRow
ccdTdrIfEntry=_CcdTdrIfEntry_Object((1,3,6,1,4,1,9,9,390,1,2,1,1))
ccdTdrIfEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:ccdTdrIfEntry.setStatus(_A)
class _CcdTdrIfAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('start',1),('clear',2),(_G,3),(_H,4)))
_CcdTdrIfAction_Type.__name__=_D
_CcdTdrIfAction_Object=MibTableColumn
ccdTdrIfAction=_CcdTdrIfAction_Object((1,3,6,1,4,1,9,9,390,1,2,1,1,1),_CcdTdrIfAction_Type())
ccdTdrIfAction.setMaxAccess(_I)
if mibBuilder.loadTexts:ccdTdrIfAction.setStatus(_A)
class _CcdTdrIfActionStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_J,1),(_K,2),(_L,3),(_M,4),('failedDueToTestAlreadyRunning',5),(_N,6)))
_CcdTdrIfActionStatus_Type.__name__=_D
_CcdTdrIfActionStatus_Object=MibTableColumn
ccdTdrIfActionStatus=_CcdTdrIfActionStatus_Object((1,3,6,1,4,1,9,9,390,1,2,1,1,2),_CcdTdrIfActionStatus_Type())
ccdTdrIfActionStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ccdTdrIfActionStatus.setStatus(_A)
_CcdTdrIfLastTestTime_Type=TimeStamp
_CcdTdrIfLastTestTime_Object=MibTableColumn
ccdTdrIfLastTestTime=_CcdTdrIfLastTestTime_Object((1,3,6,1,4,1,9,9,390,1,2,1,1,3),_CcdTdrIfLastTestTime_Type())
ccdTdrIfLastTestTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ccdTdrIfLastTestTime.setStatus(_A)
_CcdTdrIfResultValid_Type=TruthValue
_CcdTdrIfResultValid_Object=MibTableColumn
ccdTdrIfResultValid=_CcdTdrIfResultValid_Object((1,3,6,1,4,1,9,9,390,1,2,1,1,4),_CcdTdrIfResultValid_Type())
ccdTdrIfResultValid.setMaxAccess(_C)
if mibBuilder.loadTexts:ccdTdrIfResultValid.setStatus(_A)
_CcdTdrIfResultTable_Object=MibTable
ccdTdrIfResultTable=_CcdTdrIfResultTable_Object((1,3,6,1,4,1,9,9,390,1,2,2))
if mibBuilder.loadTexts:ccdTdrIfResultTable.setStatus(_A)
_CcdTdrIfResultEntry_Object=MibTableRow
ccdTdrIfResultEntry=_CcdTdrIfResultEntry_Object((1,3,6,1,4,1,9,9,390,1,2,2,1))
ccdTdrIfResultEntry.setIndexNames((0,_E,_F),(0,_B,_O))
if mibBuilder.loadTexts:ccdTdrIfResultEntry.setStatus(_A)
class _CcdTdrIfResultPairIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('pair1to2',1),('pair3to6',2),('pair4to5',3),('pair7to8',4)))
_CcdTdrIfResultPairIndex_Type.__name__=_D
_CcdTdrIfResultPairIndex_Object=MibTableColumn
ccdTdrIfResultPairIndex=_CcdTdrIfResultPairIndex_Object((1,3,6,1,4,1,9,9,390,1,2,2,1,1),_CcdTdrIfResultPairIndex_Type())
ccdTdrIfResultPairIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:ccdTdrIfResultPairIndex.setStatus(_A)
class _CcdTdrIfResultPairChannel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('other',1),('channelA',2),('channelB',3),('channelC',4),('channelD',5)))
_CcdTdrIfResultPairChannel_Type.__name__=_D
_CcdTdrIfResultPairChannel_Object=MibTableColumn
ccdTdrIfResultPairChannel=_CcdTdrIfResultPairChannel_Object((1,3,6,1,4,1,9,9,390,1,2,2,1,2),_CcdTdrIfResultPairChannel_Type())
ccdTdrIfResultPairChannel.setMaxAccess(_C)
if mibBuilder.loadTexts:ccdTdrIfResultPairChannel.setStatus(_A)
class _CcdTdrIfResultPairLength_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,2147483647))
_CcdTdrIfResultPairLength_Type.__name__=_D
_CcdTdrIfResultPairLength_Object=MibTableColumn
ccdTdrIfResultPairLength=_CcdTdrIfResultPairLength_Object((1,3,6,1,4,1,9,9,390,1,2,2,1,3),_CcdTdrIfResultPairLength_Type())
ccdTdrIfResultPairLength.setMaxAccess(_C)
if mibBuilder.loadTexts:ccdTdrIfResultPairLength.setStatus(_A)
class _CcdTdrIfResultPairLenAccuracy_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,2147483647))
_CcdTdrIfResultPairLenAccuracy_Type.__name__=_D
_CcdTdrIfResultPairLenAccuracy_Object=MibTableColumn
ccdTdrIfResultPairLenAccuracy=_CcdTdrIfResultPairLenAccuracy_Object((1,3,6,1,4,1,9,9,390,1,2,2,1,4),_CcdTdrIfResultPairLenAccuracy_Type())
ccdTdrIfResultPairLenAccuracy.setMaxAccess(_C)
if mibBuilder.loadTexts:ccdTdrIfResultPairLenAccuracy.setStatus(_A)
class _CcdTdrIfResultPairDistToFault_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,2147483647))
_CcdTdrIfResultPairDistToFault_Type.__name__=_D
_CcdTdrIfResultPairDistToFault_Object=MibTableColumn
ccdTdrIfResultPairDistToFault=_CcdTdrIfResultPairDistToFault_Object((1,3,6,1,4,1,9,9,390,1,2,2,1,5),_CcdTdrIfResultPairDistToFault_Type())
ccdTdrIfResultPairDistToFault.setMaxAccess(_C)
if mibBuilder.loadTexts:ccdTdrIfResultPairDistToFault.setStatus(_A)
class _CcdTdrIfResultPairDistAccuracy_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,2147483647))
_CcdTdrIfResultPairDistAccuracy_Type.__name__=_D
_CcdTdrIfResultPairDistAccuracy_Object=MibTableColumn
ccdTdrIfResultPairDistAccuracy=_CcdTdrIfResultPairDistAccuracy_Object((1,3,6,1,4,1,9,9,390,1,2,2,1,6),_CcdTdrIfResultPairDistAccuracy_Type())
ccdTdrIfResultPairDistAccuracy.setMaxAccess(_C)
if mibBuilder.loadTexts:ccdTdrIfResultPairDistAccuracy.setStatus(_A)
class _CcdTdrIfResultPairLengthUnit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_P,1),('meter',2),('centimeter',3),('kilometer',4)))
_CcdTdrIfResultPairLengthUnit_Type.__name__=_D
_CcdTdrIfResultPairLengthUnit_Object=MibTableColumn
ccdTdrIfResultPairLengthUnit=_CcdTdrIfResultPairLengthUnit_Object((1,3,6,1,4,1,9,9,390,1,2,2,1,7),_CcdTdrIfResultPairLengthUnit_Type())
ccdTdrIfResultPairLengthUnit.setMaxAccess(_C)
if mibBuilder.loadTexts:ccdTdrIfResultPairLengthUnit.setStatus(_A)
class _CcdTdrIfResultPairStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*((_P,1),('terminated',2),('notCompleted',3),('notSupported',4),('open',5),('shorted',6),('impedanceMismatch',7),('broken',8),('indeterminate',9)))
_CcdTdrIfResultPairStatus_Type.__name__=_D
_CcdTdrIfResultPairStatus_Object=MibTableColumn
ccdTdrIfResultPairStatus=_CcdTdrIfResultPairStatus_Object((1,3,6,1,4,1,9,9,390,1,2,2,1,8),_CcdTdrIfResultPairStatus_Type())
ccdTdrIfResultPairStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ccdTdrIfResultPairStatus.setStatus(_A)
_CiscoCableDiagMIBConform_ObjectIdentity=ObjectIdentity
ciscoCableDiagMIBConform=_CiscoCableDiagMIBConform_ObjectIdentity((1,3,6,1,4,1,9,9,390,2))
_CiscoCableDiagMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoCableDiagMIBCompliances=_CiscoCableDiagMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,390,2,1))
_CiscoCableDiagMIBGroups_ObjectIdentity=ObjectIdentity
ciscoCableDiagMIBGroups=_CiscoCableDiagMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,390,2,2))
ccdPrbsGroup=ObjectGroup((1,3,6,1,4,1,9,9,390,2,2,1))
ccdPrbsGroup.setObjects(*((_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U)))
if mibBuilder.loadTexts:ccdPrbsGroup.setStatus(_A)
ccdTdrGroup=ObjectGroup((1,3,6,1,4,1,9,9,390,2,2,2))
ccdTdrGroup.setObjects(*((_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f)))
if mibBuilder.loadTexts:ccdTdrGroup.setStatus(_A)
ciscoCableDiagMIBComplianceRev1=ModuleCompliance((1,3,6,1,4,1,9,9,390,2,1,1))
ciscoCableDiagMIBComplianceRev1.setObjects(*((_B,_g),(_B,_h)))
if mibBuilder.loadTexts:ciscoCableDiagMIBComplianceRev1.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ciscoCableDiagMIB':ciscoCableDiagMIB,'ciscoCableDiagMIBNotifs':ciscoCableDiagMIBNotifs,'ciscoCableDiagMIBObjects':ciscoCableDiagMIBObjects,'ccdPrbsObjects':ccdPrbsObjects,'ccdPrbsIfTable':ccdPrbsIfTable,'ccdPrbsIfEntry':ccdPrbsIfEntry,_Q:ccdPrbsIfAction,_R:ccdPrbsIfActionStatus,_S:ccdPrbsIfTestErrors,_T:ccdPrbsIfTestErrorsResetTime,_U:ccdPrbsIfTestErrorsMaxValue,'ccdTdrObjects':ccdTdrObjects,'ccdTdrIfTable':ccdTdrIfTable,'ccdTdrIfEntry':ccdTdrIfEntry,_V:ccdTdrIfAction,_W:ccdTdrIfActionStatus,_X:ccdTdrIfLastTestTime,_Y:ccdTdrIfResultValid,'ccdTdrIfResultTable':ccdTdrIfResultTable,'ccdTdrIfResultEntry':ccdTdrIfResultEntry,_O:ccdTdrIfResultPairIndex,_Z:ccdTdrIfResultPairChannel,_a:ccdTdrIfResultPairLength,_b:ccdTdrIfResultPairLenAccuracy,_c:ccdTdrIfResultPairDistToFault,_d:ccdTdrIfResultPairDistAccuracy,_e:ccdTdrIfResultPairLengthUnit,_f:ccdTdrIfResultPairStatus,'ciscoCableDiagMIBConform':ciscoCableDiagMIBConform,'ciscoCableDiagMIBCompliances':ciscoCableDiagMIBCompliances,'ciscoCableDiagMIBComplianceRev1':ciscoCableDiagMIBComplianceRev1,'ciscoCableDiagMIBGroups':ciscoCableDiagMIBGroups,_g:ccdPrbsGroup,_h:ccdTdrGroup})