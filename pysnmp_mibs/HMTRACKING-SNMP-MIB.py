_Q='hmTrackState'
_P='hmTrackRowStatus'
_O='hmTrackLogicalInstanceId'
_N='not-accessible'
_M='hmTrackAppId'
_L='read-create'
_K='DisplayString'
_J='TimeTicks'
_I='seconds'
_H='RowStatus'
_G='InterfaceIndexOrZero'
_F='hmTrackId'
_E='read-only'
_D='HMTRACKING-SNMP-MIB'
_C='read-write'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hmConfiguration,=mibBuilder.importSymbols('HMPRIV-MGMT-SNMP-MIB','hmConfiguration')
InterfaceIndexOrZero,=mibBuilder.importSymbols('IF-MIB',_G)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn',_J,'Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_K,'PhysAddress',_H,'TextualConvention')
hmTracking=ModuleIdentity((1,3,6,1,4,1,248,14,15))
if mibBuilder.loadTexts:hmTracking.setRevisions(('2007-09-13 12:00',))
_HmTrackingGroup_ObjectIdentity=ObjectIdentity
hmTrackingGroup=_HmTrackingGroup_ObjectIdentity((1,3,6,1,4,1,248,14,15,1))
_HmTrackEvent_ObjectIdentity=ObjectIdentity
hmTrackEvent=_HmTrackEvent_ObjectIdentity((1,3,6,1,4,1,248,14,15,1,0))
if mibBuilder.loadTexts:hmTrackEvent.setStatus(_A)
_HmTrackingTable_Object=MibTable
hmTrackingTable=_HmTrackingTable_Object((1,3,6,1,4,1,248,14,15,1,1))
if mibBuilder.loadTexts:hmTrackingTable.setStatus(_A)
_HmTrackingEntry_Object=MibTableRow
hmTrackingEntry=_HmTrackingEntry_Object((1,3,6,1,4,1,248,14,15,1,1,1))
hmTrackingEntry.setIndexNames((0,_D,_F))
if mibBuilder.loadTexts:hmTrackingEntry.setStatus(_A)
_HmTrackId_Type=Integer32
_HmTrackId_Object=MibTableColumn
hmTrackId=_HmTrackId_Object((1,3,6,1,4,1,248,14,15,1,1,1,1),_HmTrackId_Type())
hmTrackId.setMaxAccess(_E)
if mibBuilder.loadTexts:hmTrackId.setStatus(_A)
class _HmTrackRowStatus_Type(RowStatus):defaultValue=3
_HmTrackRowStatus_Type.__name__=_H
_HmTrackRowStatus_Object=MibTableColumn
hmTrackRowStatus=_HmTrackRowStatus_Object((1,3,6,1,4,1,248,14,15,1,1,1,2),_HmTrackRowStatus_Type())
hmTrackRowStatus.setMaxAccess(_L)
if mibBuilder.loadTexts:hmTrackRowStatus.setStatus(_A)
class _HmTrackType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('undefined',1),('interface',2),('ping',3),('logical',4)))
_HmTrackType_Type.__name__=_B
_HmTrackType_Object=MibTableColumn
hmTrackType=_HmTrackType_Object((1,3,6,1,4,1,248,14,15,1,1,1,3),_HmTrackType_Type())
hmTrackType.setMaxAccess(_C)
if mibBuilder.loadTexts:hmTrackType.setStatus(_A)
class _HmTrackState_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),('down',2)))
_HmTrackState_Type.__name__=_B
_HmTrackState_Object=MibTableColumn
hmTrackState=_HmTrackState_Object((1,3,6,1,4,1,248,14,15,1,1,1,4),_HmTrackState_Type())
hmTrackState.setMaxAccess(_E)
if mibBuilder.loadTexts:hmTrackState.setStatus(_A)
class _HmTrackNumberOfChanges_Type(Integer32):defaultValue=0
_HmTrackNumberOfChanges_Type.__name__=_B
_HmTrackNumberOfChanges_Object=MibTableColumn
hmTrackNumberOfChanges=_HmTrackNumberOfChanges_Object((1,3,6,1,4,1,248,14,15,1,1,1,5),_HmTrackNumberOfChanges_Type())
hmTrackNumberOfChanges.setMaxAccess(_E)
if mibBuilder.loadTexts:hmTrackNumberOfChanges.setStatus(_A)
class _HmTrackTimeSinceLastChange_Type(TimeTicks):defaultValue=0
_HmTrackTimeSinceLastChange_Type.__name__=_J
_HmTrackTimeSinceLastChange_Object=MibTableColumn
hmTrackTimeSinceLastChange=_HmTrackTimeSinceLastChange_Object((1,3,6,1,4,1,248,14,15,1,1,1,6),_HmTrackTimeSinceLastChange_Type())
hmTrackTimeSinceLastChange.setMaxAccess(_E)
if mibBuilder.loadTexts:hmTrackTimeSinceLastChange.setStatus(_A)
class _HmTrackIfNumber_Type(InterfaceIndexOrZero):defaultValue=0
_HmTrackIfNumber_Type.__name__=_G
_HmTrackIfNumber_Object=MibTableColumn
hmTrackIfNumber=_HmTrackIfNumber_Object((1,3,6,1,4,1,248,14,15,1,1,1,7),_HmTrackIfNumber_Type())
hmTrackIfNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:hmTrackIfNumber.setStatus(_A)
class _HmTrackIfLinkUpDelay_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_HmTrackIfLinkUpDelay_Type.__name__=_B
_HmTrackIfLinkUpDelay_Object=MibTableColumn
hmTrackIfLinkUpDelay=_HmTrackIfLinkUpDelay_Object((1,3,6,1,4,1,248,14,15,1,1,1,8),_HmTrackIfLinkUpDelay_Type())
hmTrackIfLinkUpDelay.setMaxAccess(_C)
if mibBuilder.loadTexts:hmTrackIfLinkUpDelay.setStatus(_A)
if mibBuilder.loadTexts:hmTrackIfLinkUpDelay.setUnits(_I)
class _HmTrackIfLinkDownDelay_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_HmTrackIfLinkDownDelay_Type.__name__=_B
_HmTrackIfLinkDownDelay_Object=MibTableColumn
hmTrackIfLinkDownDelay=_HmTrackIfLinkDownDelay_Object((1,3,6,1,4,1,248,14,15,1,1,1,9),_HmTrackIfLinkDownDelay_Type())
hmTrackIfLinkDownDelay.setMaxAccess(_C)
if mibBuilder.loadTexts:hmTrackIfLinkDownDelay.setStatus(_A)
if mibBuilder.loadTexts:hmTrackIfLinkDownDelay.setUnits(_I)
_HmTrackPingIpAddress_Type=IpAddress
_HmTrackPingIpAddress_Object=MibTableColumn
hmTrackPingIpAddress=_HmTrackPingIpAddress_Object((1,3,6,1,4,1,248,14,15,1,1,1,10),_HmTrackPingIpAddress_Type())
hmTrackPingIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:hmTrackPingIpAddress.setStatus(_A)
class _HmTrackPingInterval_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_HmTrackPingInterval_Type.__name__=_B
_HmTrackPingInterval_Object=MibTableColumn
hmTrackPingInterval=_HmTrackPingInterval_Object((1,3,6,1,4,1,248,14,15,1,1,1,11),_HmTrackPingInterval_Type())
hmTrackPingInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:hmTrackPingInterval.setStatus(_A)
if mibBuilder.loadTexts:hmTrackPingInterval.setUnits(_I)
class _HmTrackPingMiss_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_HmTrackPingMiss_Type.__name__=_B
_HmTrackPingMiss_Object=MibTableColumn
hmTrackPingMiss=_HmTrackPingMiss_Object((1,3,6,1,4,1,248,14,15,1,1,1,12),_HmTrackPingMiss_Type())
hmTrackPingMiss.setMaxAccess(_C)
if mibBuilder.loadTexts:hmTrackPingMiss.setStatus(_A)
class _HmTrackPingSuccess_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_HmTrackPingSuccess_Type.__name__=_B
_HmTrackPingSuccess_Object=MibTableColumn
hmTrackPingSuccess=_HmTrackPingSuccess_Object((1,3,6,1,4,1,248,14,15,1,1,1,13),_HmTrackPingSuccess_Type())
hmTrackPingSuccess.setMaxAccess(_C)
if mibBuilder.loadTexts:hmTrackPingSuccess.setStatus(_A)
class _HmTrackPingTimeout_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,10000))
_HmTrackPingTimeout_Type.__name__=_B
_HmTrackPingTimeout_Object=MibTableColumn
hmTrackPingTimeout=_HmTrackPingTimeout_Object((1,3,6,1,4,1,248,14,15,1,1,1,14),_HmTrackPingTimeout_Type())
hmTrackPingTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:hmTrackPingTimeout.setStatus(_A)
if mibBuilder.loadTexts:hmTrackPingTimeout.setUnits('milliseconds')
class _HmTrackPingTTL_Type(Integer32):defaultValue=128;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_HmTrackPingTTL_Type.__name__=_B
_HmTrackPingTTL_Object=MibTableColumn
hmTrackPingTTL=_HmTrackPingTTL_Object((1,3,6,1,4,1,248,14,15,1,1,1,15),_HmTrackPingTTL_Type())
hmTrackPingTTL.setMaxAccess(_C)
if mibBuilder.loadTexts:hmTrackPingTTL.setStatus(_A)
class _HmTrackPingBestRouteIfNumber_Type(InterfaceIndexOrZero):defaultValue=0
_HmTrackPingBestRouteIfNumber_Type.__name__=_G
_HmTrackPingBestRouteIfNumber_Object=MibTableColumn
hmTrackPingBestRouteIfNumber=_HmTrackPingBestRouteIfNumber_Object((1,3,6,1,4,1,248,14,15,1,1,1,16),_HmTrackPingBestRouteIfNumber_Type())
hmTrackPingBestRouteIfNumber.setMaxAccess(_E)
if mibBuilder.loadTexts:hmTrackPingBestRouteIfNumber.setStatus(_A)
class _HmTrackLogicalOperator_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('and',1),('or',2)))
_HmTrackLogicalOperator_Type.__name__=_B
_HmTrackLogicalOperator_Object=MibTableColumn
hmTrackLogicalOperator=_HmTrackLogicalOperator_Object((1,3,6,1,4,1,248,14,15,1,1,1,17),_HmTrackLogicalOperator_Type())
hmTrackLogicalOperator.setMaxAccess(_C)
if mibBuilder.loadTexts:hmTrackLogicalOperator.setStatus(_A)
class _HmTrackSendStateChangeTrap_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enable',1),('disable',2)))
_HmTrackSendStateChangeTrap_Type.__name__=_B
_HmTrackSendStateChangeTrap_Object=MibTableColumn
hmTrackSendStateChangeTrap=_HmTrackSendStateChangeTrap_Object((1,3,6,1,4,1,248,14,15,1,1,1,18),_HmTrackSendStateChangeTrap_Type())
hmTrackSendStateChangeTrap.setMaxAccess(_C)
if mibBuilder.loadTexts:hmTrackSendStateChangeTrap.setStatus(_A)
_HmTrackingApplicationTable_Object=MibTable
hmTrackingApplicationTable=_HmTrackingApplicationTable_Object((1,3,6,1,4,1,248,14,15,1,2))
if mibBuilder.loadTexts:hmTrackingApplicationTable.setStatus(_A)
_HmTrackingApplicationEntry_Object=MibTableRow
hmTrackingApplicationEntry=_HmTrackingApplicationEntry_Object((1,3,6,1,4,1,248,14,15,1,2,1))
hmTrackingApplicationEntry.setIndexNames((0,_D,_F),(0,_D,_M))
if mibBuilder.loadTexts:hmTrackingApplicationEntry.setStatus(_A)
_HmTrackAppId_Type=Integer32
_HmTrackAppId_Object=MibTableColumn
hmTrackAppId=_HmTrackAppId_Object((1,3,6,1,4,1,248,14,15,1,2,1,2),_HmTrackAppId_Type())
hmTrackAppId.setMaxAccess(_N)
if mibBuilder.loadTexts:hmTrackAppId.setStatus(_A)
class _HmTrackAppName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_HmTrackAppName_Type.__name__=_K
_HmTrackAppName_Object=MibTableColumn
hmTrackAppName=_HmTrackAppName_Object((1,3,6,1,4,1,248,14,15,1,2,1,3),_HmTrackAppName_Type())
hmTrackAppName.setMaxAccess(_E)
if mibBuilder.loadTexts:hmTrackAppName.setStatus(_A)
_HmTrackLogicalInstanceTable_Object=MibTable
hmTrackLogicalInstanceTable=_HmTrackLogicalInstanceTable_Object((1,3,6,1,4,1,248,14,15,1,3))
if mibBuilder.loadTexts:hmTrackLogicalInstanceTable.setStatus(_A)
_HmTrackLogicalInstanceEntry_Object=MibTableRow
hmTrackLogicalInstanceEntry=_HmTrackLogicalInstanceEntry_Object((1,3,6,1,4,1,248,14,15,1,3,1))
hmTrackLogicalInstanceEntry.setIndexNames((0,_D,_F),(0,_D,_O))
if mibBuilder.loadTexts:hmTrackLogicalInstanceEntry.setStatus(_A)
_HmTrackLogicalInstanceId_Type=Integer32
_HmTrackLogicalInstanceId_Object=MibTableColumn
hmTrackLogicalInstanceId=_HmTrackLogicalInstanceId_Object((1,3,6,1,4,1,248,14,15,1,3,1,2),_HmTrackLogicalInstanceId_Type())
hmTrackLogicalInstanceId.setMaxAccess(_N)
if mibBuilder.loadTexts:hmTrackLogicalInstanceId.setStatus(_A)
class _HmTrackLogicInstRowStatus_Type(RowStatus):defaultValue=3
_HmTrackLogicInstRowStatus_Type.__name__=_H
_HmTrackLogicInstRowStatus_Object=MibTableColumn
hmTrackLogicInstRowStatus=_HmTrackLogicInstRowStatus_Object((1,3,6,1,4,1,248,14,15,1,3,1,3),_HmTrackLogicInstRowStatus_Type())
hmTrackLogicInstRowStatus.setMaxAccess(_L)
if mibBuilder.loadTexts:hmTrackLogicInstRowStatus.setStatus(_A)
hmTrackStatusChangeEvent=NotificationType((1,3,6,1,4,1,248,14,15,1,0,1))
hmTrackStatusChangeEvent.setObjects(*((_D,_F),(_D,_P),(_D,_Q)))
if mibBuilder.loadTexts:hmTrackStatusChangeEvent.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'hmTracking':hmTracking,'hmTrackingGroup':hmTrackingGroup,'hmTrackEvent':hmTrackEvent,'hmTrackStatusChangeEvent':hmTrackStatusChangeEvent,'hmTrackingTable':hmTrackingTable,'hmTrackingEntry':hmTrackingEntry,_F:hmTrackId,_P:hmTrackRowStatus,'hmTrackType':hmTrackType,_Q:hmTrackState,'hmTrackNumberOfChanges':hmTrackNumberOfChanges,'hmTrackTimeSinceLastChange':hmTrackTimeSinceLastChange,'hmTrackIfNumber':hmTrackIfNumber,'hmTrackIfLinkUpDelay':hmTrackIfLinkUpDelay,'hmTrackIfLinkDownDelay':hmTrackIfLinkDownDelay,'hmTrackPingIpAddress':hmTrackPingIpAddress,'hmTrackPingInterval':hmTrackPingInterval,'hmTrackPingMiss':hmTrackPingMiss,'hmTrackPingSuccess':hmTrackPingSuccess,'hmTrackPingTimeout':hmTrackPingTimeout,'hmTrackPingTTL':hmTrackPingTTL,'hmTrackPingBestRouteIfNumber':hmTrackPingBestRouteIfNumber,'hmTrackLogicalOperator':hmTrackLogicalOperator,'hmTrackSendStateChangeTrap':hmTrackSendStateChangeTrap,'hmTrackingApplicationTable':hmTrackingApplicationTable,'hmTrackingApplicationEntry':hmTrackingApplicationEntry,_M:hmTrackAppId,'hmTrackAppName':hmTrackAppName,'hmTrackLogicalInstanceTable':hmTrackLogicalInstanceTable,'hmTrackLogicalInstanceEntry':hmTrackLogicalInstanceEntry,_O:hmTrackLogicalInstanceId,'hmTrackLogicInstRowStatus':hmTrackLogicInstRowStatus})