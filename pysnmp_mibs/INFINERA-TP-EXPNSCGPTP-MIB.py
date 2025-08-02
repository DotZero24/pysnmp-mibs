_Q='expnScgPtpGroup'
_P='expnScgPtpPathLossHigh'
_O='expnScgPtpLastPathLossCheckFailedReason'
_N='expnScgPtpLastPathLossCheckAttemptStatus'
_M='expnScgPtpLastPathLossCheckAttemptTS'
_L='expnScgPtpPathLossCheckDetectedPort'
_K='expnScgPtpPathLoss'
_J='expnScgPtpLastSuccessfullPathLossCheckTS'
_I='expnScgPtpPathLossCheckControlStatus'
_H='expnScgPtpMPOAID'
_G='expnScgPtpScgNumber'
_F='ifIndex'
_E='IF-MIB'
_D='Integer32'
_C='read-only'
_B='INFINERA-TP-EXPNSCGPTP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_E,_F)
terminationPoint,=mibBuilder.importSymbols('INFINERA-REG-MIB','terminationPoint')
FloatHundredths,InfnEnableDisable=mibBuilder.importSymbols('INFINERA-TC-MIB','FloatHundredths','InfnEnableDisable')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
expnScgPtpMIB=ModuleIdentity((1,3,6,1,4,1,21296,2,2,2,2,47))
if mibBuilder.loadTexts:expnScgPtpMIB.setRevisions(('2013-10-20 00:00',))
_ExpnScgPtpTable_Object=MibTable
expnScgPtpTable=_ExpnScgPtpTable_Object((1,3,6,1,4,1,21296,2,2,2,2,47,1))
if mibBuilder.loadTexts:expnScgPtpTable.setStatus(_A)
_ExpnScgPtpEntry_Object=MibTableRow
expnScgPtpEntry=_ExpnScgPtpEntry_Object((1,3,6,1,4,1,21296,2,2,2,2,47,1,1))
expnScgPtpEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:expnScgPtpEntry.setStatus(_A)
_ExpnScgPtpScgNumber_Type=Integer32
_ExpnScgPtpScgNumber_Object=MibTableColumn
expnScgPtpScgNumber=_ExpnScgPtpScgNumber_Object((1,3,6,1,4,1,21296,2,2,2,2,47,1,1,1),_ExpnScgPtpScgNumber_Type())
expnScgPtpScgNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:expnScgPtpScgNumber.setStatus(_A)
_ExpnScgPtpMPOAID_Type=DisplayString
_ExpnScgPtpMPOAID_Object=MibTableColumn
expnScgPtpMPOAID=_ExpnScgPtpMPOAID_Object((1,3,6,1,4,1,21296,2,2,2,2,47,1,1,2),_ExpnScgPtpMPOAID_Type())
expnScgPtpMPOAID.setMaxAccess('read-write')
if mibBuilder.loadTexts:expnScgPtpMPOAID.setStatus(_A)
class _ExpnScgPtpPathLossCheckControlStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('inProgress',1),('idle',2)))
_ExpnScgPtpPathLossCheckControlStatus_Type.__name__=_D
_ExpnScgPtpPathLossCheckControlStatus_Object=MibTableColumn
expnScgPtpPathLossCheckControlStatus=_ExpnScgPtpPathLossCheckControlStatus_Object((1,3,6,1,4,1,21296,2,2,2,2,47,1,1,3),_ExpnScgPtpPathLossCheckControlStatus_Type())
expnScgPtpPathLossCheckControlStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:expnScgPtpPathLossCheckControlStatus.setStatus(_A)
_ExpnScgPtpLastSuccessfullPathLossCheckTS_Type=Integer32
_ExpnScgPtpLastSuccessfullPathLossCheckTS_Object=MibTableColumn
expnScgPtpLastSuccessfullPathLossCheckTS=_ExpnScgPtpLastSuccessfullPathLossCheckTS_Object((1,3,6,1,4,1,21296,2,2,2,2,47,1,1,4),_ExpnScgPtpLastSuccessfullPathLossCheckTS_Type())
expnScgPtpLastSuccessfullPathLossCheckTS.setMaxAccess(_C)
if mibBuilder.loadTexts:expnScgPtpLastSuccessfullPathLossCheckTS.setStatus(_A)
_ExpnScgPtpPathLoss_Type=FloatHundredths
_ExpnScgPtpPathLoss_Object=MibTableColumn
expnScgPtpPathLoss=_ExpnScgPtpPathLoss_Object((1,3,6,1,4,1,21296,2,2,2,2,47,1,1,5),_ExpnScgPtpPathLoss_Type())
expnScgPtpPathLoss.setMaxAccess(_C)
if mibBuilder.loadTexts:expnScgPtpPathLoss.setStatus(_A)
_ExpnScgPtpPathLossCheckDetectedPort_Type=DisplayString
_ExpnScgPtpPathLossCheckDetectedPort_Object=MibTableColumn
expnScgPtpPathLossCheckDetectedPort=_ExpnScgPtpPathLossCheckDetectedPort_Object((1,3,6,1,4,1,21296,2,2,2,2,47,1,1,6),_ExpnScgPtpPathLossCheckDetectedPort_Type())
expnScgPtpPathLossCheckDetectedPort.setMaxAccess(_C)
if mibBuilder.loadTexts:expnScgPtpPathLossCheckDetectedPort.setStatus(_A)
_ExpnScgPtpLastPathLossCheckAttemptTS_Type=Integer32
_ExpnScgPtpLastPathLossCheckAttemptTS_Object=MibTableColumn
expnScgPtpLastPathLossCheckAttemptTS=_ExpnScgPtpLastPathLossCheckAttemptTS_Object((1,3,6,1,4,1,21296,2,2,2,2,47,1,1,7),_ExpnScgPtpLastPathLossCheckAttemptTS_Type())
expnScgPtpLastPathLossCheckAttemptTS.setMaxAccess(_C)
if mibBuilder.loadTexts:expnScgPtpLastPathLossCheckAttemptTS.setStatus(_A)
class _ExpnScgPtpLastPathLossCheckAttemptStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('successfull',1),('unsuccessfull',2),('notAttempted',3)))
_ExpnScgPtpLastPathLossCheckAttemptStatus_Type.__name__=_D
_ExpnScgPtpLastPathLossCheckAttemptStatus_Object=MibTableColumn
expnScgPtpLastPathLossCheckAttemptStatus=_ExpnScgPtpLastPathLossCheckAttemptStatus_Object((1,3,6,1,4,1,21296,2,2,2,2,47,1,1,8),_ExpnScgPtpLastPathLossCheckAttemptStatus_Type())
expnScgPtpLastPathLossCheckAttemptStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:expnScgPtpLastPathLossCheckAttemptStatus.setStatus(_A)
class _ExpnScgPtpLastPathLossCheckFailedReason_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('na',1),('timedOut',2),('interruptedbyAD',3),('interruptedbyReset',4),('portInService',5)))
_ExpnScgPtpLastPathLossCheckFailedReason_Type.__name__=_D
_ExpnScgPtpLastPathLossCheckFailedReason_Object=MibTableColumn
expnScgPtpLastPathLossCheckFailedReason=_ExpnScgPtpLastPathLossCheckFailedReason_Object((1,3,6,1,4,1,21296,2,2,2,2,47,1,1,9),_ExpnScgPtpLastPathLossCheckFailedReason_Type())
expnScgPtpLastPathLossCheckFailedReason.setMaxAccess(_C)
if mibBuilder.loadTexts:expnScgPtpLastPathLossCheckFailedReason.setStatus(_A)
class _ExpnScgPtpPathLossHigh_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('true',1),('false',2)))
_ExpnScgPtpPathLossHigh_Type.__name__=_D
_ExpnScgPtpPathLossHigh_Object=MibTableColumn
expnScgPtpPathLossHigh=_ExpnScgPtpPathLossHigh_Object((1,3,6,1,4,1,21296,2,2,2,2,47,1,1,10),_ExpnScgPtpPathLossHigh_Type())
expnScgPtpPathLossHigh.setMaxAccess(_C)
if mibBuilder.loadTexts:expnScgPtpPathLossHigh.setStatus(_A)
_ExpnScgPtpConformance_ObjectIdentity=ObjectIdentity
expnScgPtpConformance=_ExpnScgPtpConformance_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,47,3))
_ExpnScgPtpCompliances_ObjectIdentity=ObjectIdentity
expnScgPtpCompliances=_ExpnScgPtpCompliances_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,47,3,1))
_ExpnScgPtpGroups_ObjectIdentity=ObjectIdentity
expnScgPtpGroups=_ExpnScgPtpGroups_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,47,3,2))
expnScgPtpGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,2,2,47,3,2,1))
expnScgPtpGroup.setObjects(*((_B,_G),(_B,_H),(_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P)))
if mibBuilder.loadTexts:expnScgPtpGroup.setStatus(_A)
expnScgPtpCompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,2,2,47,3,1,1))
expnScgPtpCompliance.setObjects((_B,_Q))
if mibBuilder.loadTexts:expnScgPtpCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'expnScgPtpMIB':expnScgPtpMIB,'expnScgPtpTable':expnScgPtpTable,'expnScgPtpEntry':expnScgPtpEntry,_G:expnScgPtpScgNumber,_H:expnScgPtpMPOAID,_I:expnScgPtpPathLossCheckControlStatus,_J:expnScgPtpLastSuccessfullPathLossCheckTS,_K:expnScgPtpPathLoss,_L:expnScgPtpPathLossCheckDetectedPort,_M:expnScgPtpLastPathLossCheckAttemptTS,_N:expnScgPtpLastPathLossCheckAttemptStatus,_O:expnScgPtpLastPathLossCheckFailedReason,_P:expnScgPtpPathLossHigh,'expnScgPtpConformance':expnScgPtpConformance,'expnScgPtpCompliances':expnScgPtpCompliances,'expnScgPtpCompliance':expnScgPtpCompliance,'expnScgPtpGroups':expnScgPtpGroups,_Q:expnScgPtpGroup})