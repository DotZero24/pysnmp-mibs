_Q='baseScgPtpGroup'
_P='baseScgPtpPathLossHigh'
_O='baseScgPtpLastPathLossCheckFailedReason'
_N='baseScgPtpLastPathLossCheckAttemptStatus'
_M='baseScgPtpLastPathLossCheckAttemptTS'
_L='baseScgPtpPathLossCheckDetectedPort'
_K='baseScgPtpPathLoss'
_J='baseScgPtpLastSuccessfullPathLossCheckTS'
_I='baseScgPtpPathLossCheckControlStatus'
_H='baseScgPtpMPOAID'
_G='baseScgPtpScgNumber'
_F='ifIndex'
_E='IF-MIB'
_D='Integer32'
_C='read-only'
_B='INFINERA-TP-BASESCGPTP-MIB'
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
baseScgPtpMIB=ModuleIdentity((1,3,6,1,4,1,21296,2,2,2,2,46))
if mibBuilder.loadTexts:baseScgPtpMIB.setRevisions(('2013-10-20 00:00',))
_BaseScgPtpTable_Object=MibTable
baseScgPtpTable=_BaseScgPtpTable_Object((1,3,6,1,4,1,21296,2,2,2,2,46,1))
if mibBuilder.loadTexts:baseScgPtpTable.setStatus(_A)
_BaseScgPtpEntry_Object=MibTableRow
baseScgPtpEntry=_BaseScgPtpEntry_Object((1,3,6,1,4,1,21296,2,2,2,2,46,1,1))
baseScgPtpEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:baseScgPtpEntry.setStatus(_A)
_BaseScgPtpScgNumber_Type=Integer32
_BaseScgPtpScgNumber_Object=MibTableColumn
baseScgPtpScgNumber=_BaseScgPtpScgNumber_Object((1,3,6,1,4,1,21296,2,2,2,2,46,1,1,1),_BaseScgPtpScgNumber_Type())
baseScgPtpScgNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:baseScgPtpScgNumber.setStatus(_A)
_BaseScgPtpMPOAID_Type=DisplayString
_BaseScgPtpMPOAID_Object=MibTableColumn
baseScgPtpMPOAID=_BaseScgPtpMPOAID_Object((1,3,6,1,4,1,21296,2,2,2,2,46,1,1,2),_BaseScgPtpMPOAID_Type())
baseScgPtpMPOAID.setMaxAccess(_C)
if mibBuilder.loadTexts:baseScgPtpMPOAID.setStatus(_A)
class _BaseScgPtpPathLossCheckControlStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('inProgress',1),('idle',2)))
_BaseScgPtpPathLossCheckControlStatus_Type.__name__=_D
_BaseScgPtpPathLossCheckControlStatus_Object=MibTableColumn
baseScgPtpPathLossCheckControlStatus=_BaseScgPtpPathLossCheckControlStatus_Object((1,3,6,1,4,1,21296,2,2,2,2,46,1,1,3),_BaseScgPtpPathLossCheckControlStatus_Type())
baseScgPtpPathLossCheckControlStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:baseScgPtpPathLossCheckControlStatus.setStatus(_A)
_BaseScgPtpLastSuccessfullPathLossCheckTS_Type=Integer32
_BaseScgPtpLastSuccessfullPathLossCheckTS_Object=MibTableColumn
baseScgPtpLastSuccessfullPathLossCheckTS=_BaseScgPtpLastSuccessfullPathLossCheckTS_Object((1,3,6,1,4,1,21296,2,2,2,2,46,1,1,4),_BaseScgPtpLastSuccessfullPathLossCheckTS_Type())
baseScgPtpLastSuccessfullPathLossCheckTS.setMaxAccess(_C)
if mibBuilder.loadTexts:baseScgPtpLastSuccessfullPathLossCheckTS.setStatus(_A)
_BaseScgPtpPathLoss_Type=FloatHundredths
_BaseScgPtpPathLoss_Object=MibTableColumn
baseScgPtpPathLoss=_BaseScgPtpPathLoss_Object((1,3,6,1,4,1,21296,2,2,2,2,46,1,1,5),_BaseScgPtpPathLoss_Type())
baseScgPtpPathLoss.setMaxAccess(_C)
if mibBuilder.loadTexts:baseScgPtpPathLoss.setStatus(_A)
_BaseScgPtpPathLossCheckDetectedPort_Type=DisplayString
_BaseScgPtpPathLossCheckDetectedPort_Object=MibTableColumn
baseScgPtpPathLossCheckDetectedPort=_BaseScgPtpPathLossCheckDetectedPort_Object((1,3,6,1,4,1,21296,2,2,2,2,46,1,1,6),_BaseScgPtpPathLossCheckDetectedPort_Type())
baseScgPtpPathLossCheckDetectedPort.setMaxAccess(_C)
if mibBuilder.loadTexts:baseScgPtpPathLossCheckDetectedPort.setStatus(_A)
_BaseScgPtpLastPathLossCheckAttemptTS_Type=Integer32
_BaseScgPtpLastPathLossCheckAttemptTS_Object=MibTableColumn
baseScgPtpLastPathLossCheckAttemptTS=_BaseScgPtpLastPathLossCheckAttemptTS_Object((1,3,6,1,4,1,21296,2,2,2,2,46,1,1,7),_BaseScgPtpLastPathLossCheckAttemptTS_Type())
baseScgPtpLastPathLossCheckAttemptTS.setMaxAccess(_C)
if mibBuilder.loadTexts:baseScgPtpLastPathLossCheckAttemptTS.setStatus(_A)
class _BaseScgPtpLastPathLossCheckAttemptStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('successfull',1),('unsuccessfull',2),('notAttempted',3)))
_BaseScgPtpLastPathLossCheckAttemptStatus_Type.__name__=_D
_BaseScgPtpLastPathLossCheckAttemptStatus_Object=MibTableColumn
baseScgPtpLastPathLossCheckAttemptStatus=_BaseScgPtpLastPathLossCheckAttemptStatus_Object((1,3,6,1,4,1,21296,2,2,2,2,46,1,1,8),_BaseScgPtpLastPathLossCheckAttemptStatus_Type())
baseScgPtpLastPathLossCheckAttemptStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:baseScgPtpLastPathLossCheckAttemptStatus.setStatus(_A)
class _BaseScgPtpLastPathLossCheckFailedReason_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('na',1),('timedOut',2),('interruptedbyAD',3),('interruptedbyReset',4),('portInService',5)))
_BaseScgPtpLastPathLossCheckFailedReason_Type.__name__=_D
_BaseScgPtpLastPathLossCheckFailedReason_Object=MibTableColumn
baseScgPtpLastPathLossCheckFailedReason=_BaseScgPtpLastPathLossCheckFailedReason_Object((1,3,6,1,4,1,21296,2,2,2,2,46,1,1,9),_BaseScgPtpLastPathLossCheckFailedReason_Type())
baseScgPtpLastPathLossCheckFailedReason.setMaxAccess(_C)
if mibBuilder.loadTexts:baseScgPtpLastPathLossCheckFailedReason.setStatus(_A)
class _BaseScgPtpPathLossHigh_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('true',1),('false',2)))
_BaseScgPtpPathLossHigh_Type.__name__=_D
_BaseScgPtpPathLossHigh_Object=MibTableColumn
baseScgPtpPathLossHigh=_BaseScgPtpPathLossHigh_Object((1,3,6,1,4,1,21296,2,2,2,2,46,1,1,10),_BaseScgPtpPathLossHigh_Type())
baseScgPtpPathLossHigh.setMaxAccess(_C)
if mibBuilder.loadTexts:baseScgPtpPathLossHigh.setStatus(_A)
_BaseScgPtpConformance_ObjectIdentity=ObjectIdentity
baseScgPtpConformance=_BaseScgPtpConformance_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,46,3))
_BaseScgPtpCompliances_ObjectIdentity=ObjectIdentity
baseScgPtpCompliances=_BaseScgPtpCompliances_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,46,3,1))
_BaseScgPtpGroups_ObjectIdentity=ObjectIdentity
baseScgPtpGroups=_BaseScgPtpGroups_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,46,3,2))
baseScgPtpGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,2,2,46,3,2,1))
baseScgPtpGroup.setObjects(*((_B,_G),(_B,_H),(_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P)))
if mibBuilder.loadTexts:baseScgPtpGroup.setStatus(_A)
baseScgPtpCompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,2,2,46,3,1,1))
baseScgPtpCompliance.setObjects((_B,_Q))
if mibBuilder.loadTexts:baseScgPtpCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'baseScgPtpMIB':baseScgPtpMIB,'baseScgPtpTable':baseScgPtpTable,'baseScgPtpEntry':baseScgPtpEntry,_G:baseScgPtpScgNumber,_H:baseScgPtpMPOAID,_I:baseScgPtpPathLossCheckControlStatus,_J:baseScgPtpLastSuccessfullPathLossCheckTS,_K:baseScgPtpPathLoss,_L:baseScgPtpPathLossCheckDetectedPort,_M:baseScgPtpLastPathLossCheckAttemptTS,_N:baseScgPtpLastPathLossCheckAttemptStatus,_O:baseScgPtpLastPathLossCheckFailedReason,_P:baseScgPtpPathLossHigh,'baseScgPtpConformance':baseScgPtpConformance,'baseScgPtpCompliances':baseScgPtpCompliances,'baseScgPtpCompliance':baseScgPtpCompliance,'baseScgPtpGroups':baseScgPtpGroups,_Q:baseScgPtpGroup})