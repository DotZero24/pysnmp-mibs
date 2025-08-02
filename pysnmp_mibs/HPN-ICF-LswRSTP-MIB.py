_J='hpnicfdot1dStpPortXEntry'
_I='hpnicfdot1dVlan'
_H='enable'
_G='HPN-ICF-LswRSTP-MIB'
_F='dot1dStpPort'
_E='BRIDGE-MIB'
_D='read-only'
_C='Integer32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dot1dStpPort,dot1dStpPortEntry=mibBuilder.importSymbols(_E,_F,'dot1dStpPortEntry')
hpnicflswCommon,=mibBuilder.importSymbols('HPN-ICF-OID-MIB','hpnicflswCommon')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','TextualConvention','TruthValue')
hpnicfLswRstpMib=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,15,8,35,6))
if mibBuilder.loadTexts:hpnicfLswRstpMib.setRevisions(('2001-06-29 00:00',))
class EnabledStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
_HpnicfLswRstpMibObject_ObjectIdentity=ObjectIdentity
hpnicfLswRstpMibObject=_HpnicfLswRstpMibObject_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,8,35,6,1))
_HpnicfRstpEventsV2_ObjectIdentity=ObjectIdentity
hpnicfRstpEventsV2=_HpnicfRstpEventsV2_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,8,35,6,1,0))
if mibBuilder.loadTexts:hpnicfRstpEventsV2.setStatus(_A)
_Hpnicfdot1dStpStatus_Type=EnabledStatus
_Hpnicfdot1dStpStatus_Object=MibScalar
hpnicfdot1dStpStatus=_Hpnicfdot1dStpStatus_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,6,1,1),_Hpnicfdot1dStpStatus_Type())
hpnicfdot1dStpStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfdot1dStpStatus.setStatus(_A)
class _Hpnicfdot1dStpForceVersion_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,2)));namedValues=NamedValues(*(('stp',0),('rstp',2)))
_Hpnicfdot1dStpForceVersion_Type.__name__=_C
_Hpnicfdot1dStpForceVersion_Object=MibScalar
hpnicfdot1dStpForceVersion=_Hpnicfdot1dStpForceVersion_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,6,1,2),_Hpnicfdot1dStpForceVersion_Type())
hpnicfdot1dStpForceVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfdot1dStpForceVersion.setStatus(_A)
class _Hpnicfdot1dStpDiameter_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,7))
_Hpnicfdot1dStpDiameter_Type.__name__=_C
_Hpnicfdot1dStpDiameter_Object=MibScalar
hpnicfdot1dStpDiameter=_Hpnicfdot1dStpDiameter_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,6,1,3),_Hpnicfdot1dStpDiameter_Type())
hpnicfdot1dStpDiameter.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfdot1dStpDiameter.setStatus(_A)
_Hpnicfdot1dStpRootBridgeAddress_Type=MacAddress
_Hpnicfdot1dStpRootBridgeAddress_Object=MibScalar
hpnicfdot1dStpRootBridgeAddress=_Hpnicfdot1dStpRootBridgeAddress_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,6,1,4),_Hpnicfdot1dStpRootBridgeAddress_Type())
hpnicfdot1dStpRootBridgeAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfdot1dStpRootBridgeAddress.setStatus(_A)
_Hpnicfdot1dStpPortXTable_Object=MibTable
hpnicfdot1dStpPortXTable=_Hpnicfdot1dStpPortXTable_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,6,1,5))
if mibBuilder.loadTexts:hpnicfdot1dStpPortXTable.setStatus(_A)
_Hpnicfdot1dStpPortXEntry_Object=MibTableRow
hpnicfdot1dStpPortXEntry=_Hpnicfdot1dStpPortXEntry_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,6,1,5,1))
if mibBuilder.loadTexts:hpnicfdot1dStpPortXEntry.setStatus(_A)
_Hpnicfdot1dStpPortStatus_Type=EnabledStatus
_Hpnicfdot1dStpPortStatus_Object=MibTableColumn
hpnicfdot1dStpPortStatus=_Hpnicfdot1dStpPortStatus_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,6,1,5,1,1),_Hpnicfdot1dStpPortStatus_Type())
hpnicfdot1dStpPortStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfdot1dStpPortStatus.setStatus(_A)
_Hpnicfdot1dStpPortEdgeport_Type=TruthValue
_Hpnicfdot1dStpPortEdgeport_Object=MibTableColumn
hpnicfdot1dStpPortEdgeport=_Hpnicfdot1dStpPortEdgeport_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,6,1,5,1,2),_Hpnicfdot1dStpPortEdgeport_Type())
hpnicfdot1dStpPortEdgeport.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfdot1dStpPortEdgeport.setStatus(_A)
class _Hpnicfdot1dStpPortPointToPoint_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('forceTrue',1),('forceFalse',2),('auto',3)))
_Hpnicfdot1dStpPortPointToPoint_Type.__name__=_C
_Hpnicfdot1dStpPortPointToPoint_Object=MibTableColumn
hpnicfdot1dStpPortPointToPoint=_Hpnicfdot1dStpPortPointToPoint_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,6,1,5,1,3),_Hpnicfdot1dStpPortPointToPoint_Type())
hpnicfdot1dStpPortPointToPoint.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfdot1dStpPortPointToPoint.setStatus(_A)
_Hpnicfdot1dStpMcheck_Type=TruthValue
_Hpnicfdot1dStpMcheck_Object=MibTableColumn
hpnicfdot1dStpMcheck=_Hpnicfdot1dStpMcheck_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,6,1,5,1,4),_Hpnicfdot1dStpMcheck_Type())
hpnicfdot1dStpMcheck.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfdot1dStpMcheck.setStatus(_A)
class _Hpnicfdot1dStpTransLimit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_Hpnicfdot1dStpTransLimit_Type.__name__=_C
_Hpnicfdot1dStpTransLimit_Object=MibTableColumn
hpnicfdot1dStpTransLimit=_Hpnicfdot1dStpTransLimit_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,6,1,5,1,5),_Hpnicfdot1dStpTransLimit_Type())
hpnicfdot1dStpTransLimit.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfdot1dStpTransLimit.setStatus(_A)
_Hpnicfdot1dStpRXStpBPDU_Type=Counter32
_Hpnicfdot1dStpRXStpBPDU_Object=MibTableColumn
hpnicfdot1dStpRXStpBPDU=_Hpnicfdot1dStpRXStpBPDU_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,6,1,5,1,6),_Hpnicfdot1dStpRXStpBPDU_Type())
hpnicfdot1dStpRXStpBPDU.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfdot1dStpRXStpBPDU.setStatus(_A)
_Hpnicfdot1dStpTXStpBPDU_Type=Counter32
_Hpnicfdot1dStpTXStpBPDU_Object=MibTableColumn
hpnicfdot1dStpTXStpBPDU=_Hpnicfdot1dStpTXStpBPDU_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,6,1,5,1,7),_Hpnicfdot1dStpTXStpBPDU_Type())
hpnicfdot1dStpTXStpBPDU.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfdot1dStpTXStpBPDU.setStatus(_A)
_Hpnicfdot1dStpRXTCNBPDU_Type=Counter32
_Hpnicfdot1dStpRXTCNBPDU_Object=MibTableColumn
hpnicfdot1dStpRXTCNBPDU=_Hpnicfdot1dStpRXTCNBPDU_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,6,1,5,1,8),_Hpnicfdot1dStpRXTCNBPDU_Type())
hpnicfdot1dStpRXTCNBPDU.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfdot1dStpRXTCNBPDU.setStatus(_A)
_Hpnicfdot1dStpTXTCNBPDU_Type=Counter32
_Hpnicfdot1dStpTXTCNBPDU_Object=MibTableColumn
hpnicfdot1dStpTXTCNBPDU=_Hpnicfdot1dStpTXTCNBPDU_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,6,1,5,1,9),_Hpnicfdot1dStpTXTCNBPDU_Type())
hpnicfdot1dStpTXTCNBPDU.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfdot1dStpTXTCNBPDU.setStatus(_A)
_Hpnicfdot1dStpRXRSTPBPDU_Type=Counter32
_Hpnicfdot1dStpRXRSTPBPDU_Object=MibTableColumn
hpnicfdot1dStpRXRSTPBPDU=_Hpnicfdot1dStpRXRSTPBPDU_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,6,1,5,1,10),_Hpnicfdot1dStpRXRSTPBPDU_Type())
hpnicfdot1dStpRXRSTPBPDU.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfdot1dStpRXRSTPBPDU.setStatus(_A)
_Hpnicfdot1dStpTXRSTPBPDU_Type=Counter32
_Hpnicfdot1dStpTXRSTPBPDU_Object=MibTableColumn
hpnicfdot1dStpTXRSTPBPDU=_Hpnicfdot1dStpTXRSTPBPDU_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,6,1,5,1,11),_Hpnicfdot1dStpTXRSTPBPDU_Type())
hpnicfdot1dStpTXRSTPBPDU.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfdot1dStpTXRSTPBPDU.setStatus(_A)
class _Hpnicfdot1dStpClearStatistics_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('clear',1))
_Hpnicfdot1dStpClearStatistics_Type.__name__=_C
_Hpnicfdot1dStpClearStatistics_Object=MibTableColumn
hpnicfdot1dStpClearStatistics=_Hpnicfdot1dStpClearStatistics_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,6,1,5,1,12),_Hpnicfdot1dStpClearStatistics_Type())
hpnicfdot1dStpClearStatistics.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfdot1dStpClearStatistics.setStatus(_A)
class _Hpnicfdot1dSetStpDefaultPortCost_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues((_H,1))
_Hpnicfdot1dSetStpDefaultPortCost_Type.__name__=_C
_Hpnicfdot1dSetStpDefaultPortCost_Object=MibTableColumn
hpnicfdot1dSetStpDefaultPortCost=_Hpnicfdot1dSetStpDefaultPortCost_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,6,1,5,1,13),_Hpnicfdot1dSetStpDefaultPortCost_Type())
hpnicfdot1dSetStpDefaultPortCost.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfdot1dSetStpDefaultPortCost.setStatus(_A)
_Hpnicfdot1dStpRootGuard_Type=EnabledStatus
_Hpnicfdot1dStpRootGuard_Object=MibTableColumn
hpnicfdot1dStpRootGuard=_Hpnicfdot1dStpRootGuard_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,6,1,5,1,14),_Hpnicfdot1dStpRootGuard_Type())
hpnicfdot1dStpRootGuard.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfdot1dStpRootGuard.setStatus(_A)
_Hpnicfdot1dStpLoopGuard_Type=EnabledStatus
_Hpnicfdot1dStpLoopGuard_Object=MibTableColumn
hpnicfdot1dStpLoopGuard=_Hpnicfdot1dStpLoopGuard_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,6,1,5,1,15),_Hpnicfdot1dStpLoopGuard_Type())
hpnicfdot1dStpLoopGuard.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfdot1dStpLoopGuard.setStatus(_A)
class _Hpnicfdot1dStpPortBlockedReason_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('notBlock',1),('blockForProtocol',2),('blockForRootGuard',3),('blockForBPDUGuard',4),('blockForLoopGuard',5)))
_Hpnicfdot1dStpPortBlockedReason_Type.__name__=_C
_Hpnicfdot1dStpPortBlockedReason_Object=MibTableColumn
hpnicfdot1dStpPortBlockedReason=_Hpnicfdot1dStpPortBlockedReason_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,6,1,5,1,16),_Hpnicfdot1dStpPortBlockedReason_Type())
hpnicfdot1dStpPortBlockedReason.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfdot1dStpPortBlockedReason.setStatus(_A)
_Hpnicfdot1dStpRXTCBPDU_Type=Counter32
_Hpnicfdot1dStpRXTCBPDU_Object=MibTableColumn
hpnicfdot1dStpRXTCBPDU=_Hpnicfdot1dStpRXTCBPDU_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,6,1,5,1,17),_Hpnicfdot1dStpRXTCBPDU_Type())
hpnicfdot1dStpRXTCBPDU.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfdot1dStpRXTCBPDU.setStatus(_A)
class _Hpnicfdot1dStpPortSendingBPDUType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,2)));namedValues=NamedValues(*(('stp',0),('rstp',2)))
_Hpnicfdot1dStpPortSendingBPDUType_Type.__name__=_C
_Hpnicfdot1dStpPortSendingBPDUType_Object=MibTableColumn
hpnicfdot1dStpPortSendingBPDUType=_Hpnicfdot1dStpPortSendingBPDUType_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,6,1,5,1,18),_Hpnicfdot1dStpPortSendingBPDUType_Type())
hpnicfdot1dStpPortSendingBPDUType.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfdot1dStpPortSendingBPDUType.setStatus(_A)
class _Hpnicfdot1dStpOperPortPointToPoint_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('true',1),('false',2)))
_Hpnicfdot1dStpOperPortPointToPoint_Type.__name__=_C
_Hpnicfdot1dStpOperPortPointToPoint_Object=MibTableColumn
hpnicfdot1dStpOperPortPointToPoint=_Hpnicfdot1dStpOperPortPointToPoint_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,6,1,5,1,19),_Hpnicfdot1dStpOperPortPointToPoint_Type())
hpnicfdot1dStpOperPortPointToPoint.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfdot1dStpOperPortPointToPoint.setStatus(_A)
_HpnicfDot1dStpBpduGuard_Type=EnabledStatus
_HpnicfDot1dStpBpduGuard_Object=MibScalar
hpnicfDot1dStpBpduGuard=_HpnicfDot1dStpBpduGuard_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,6,1,6),_HpnicfDot1dStpBpduGuard_Type())
hpnicfDot1dStpBpduGuard.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot1dStpBpduGuard.setStatus(_A)
class _HpnicfDot1dStpRootType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('normal',1),('primary',2),('secondary',3)))
_HpnicfDot1dStpRootType_Type.__name__=_C
_HpnicfDot1dStpRootType_Object=MibScalar
hpnicfDot1dStpRootType=_HpnicfDot1dStpRootType_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,6,1,7),_HpnicfDot1dStpRootType_Type())
hpnicfDot1dStpRootType.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot1dStpRootType.setStatus(_A)
class _HpnicfDot1dTimeOutFactor_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(3,7))
_HpnicfDot1dTimeOutFactor_Type.__name__=_C
_HpnicfDot1dTimeOutFactor_Object=MibScalar
hpnicfDot1dTimeOutFactor=_HpnicfDot1dTimeOutFactor_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,6,1,8),_HpnicfDot1dTimeOutFactor_Type())
hpnicfDot1dTimeOutFactor.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot1dTimeOutFactor.setStatus(_A)
class _HpnicfDot1dStpPathCostStandard_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('dot1d-1998',1),('dot1t',2),('legacy',3)))
_HpnicfDot1dStpPathCostStandard_Type.__name__=_C
_HpnicfDot1dStpPathCostStandard_Object=MibScalar
hpnicfDot1dStpPathCostStandard=_HpnicfDot1dStpPathCostStandard_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,6,1,9),_HpnicfDot1dStpPathCostStandard_Type())
hpnicfDot1dStpPathCostStandard.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDot1dStpPathCostStandard.setStatus(_A)
_Hpnicfdot1dStpIgnoredVlanTable_Object=MibTable
hpnicfdot1dStpIgnoredVlanTable=_Hpnicfdot1dStpIgnoredVlanTable_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,6,1,10))
if mibBuilder.loadTexts:hpnicfdot1dStpIgnoredVlanTable.setStatus(_A)
_Hpnicfdot1dStpIgnoredVlanEntry_Object=MibTableRow
hpnicfdot1dStpIgnoredVlanEntry=_Hpnicfdot1dStpIgnoredVlanEntry_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,6,1,10,1))
hpnicfdot1dStpIgnoredVlanEntry.setIndexNames((0,_G,_I))
if mibBuilder.loadTexts:hpnicfdot1dStpIgnoredVlanEntry.setStatus(_A)
class _Hpnicfdot1dVlan_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_Hpnicfdot1dVlan_Type.__name__=_C
_Hpnicfdot1dVlan_Object=MibTableColumn
hpnicfdot1dVlan=_Hpnicfdot1dVlan_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,6,1,10,1,1),_Hpnicfdot1dVlan_Type())
hpnicfdot1dVlan.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfdot1dVlan.setStatus(_A)
class _Hpnicfdot1dStpIgnore_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),('disable',2)))
_Hpnicfdot1dStpIgnore_Type.__name__=_C
_Hpnicfdot1dStpIgnore_Object=MibTableColumn
hpnicfdot1dStpIgnore=_Hpnicfdot1dStpIgnore_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,6,1,10,1,2),_Hpnicfdot1dStpIgnore_Type())
hpnicfdot1dStpIgnore.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfdot1dStpIgnore.setStatus(_A)
dot1dStpPortEntry.registerAugmentions((_G,_J))
hpnicfdot1dStpPortXEntry.setIndexNames(*dot1dStpPortEntry.getIndexNames())
hpnicfRstpBpduGuarded=NotificationType((1,3,6,1,4,1,11,2,14,11,15,8,35,6,1,0,1))
hpnicfRstpBpduGuarded.setObjects((_E,_F))
if mibBuilder.loadTexts:hpnicfRstpBpduGuarded.setStatus(_A)
hpnicfRstpRootGuarded=NotificationType((1,3,6,1,4,1,11,2,14,11,15,8,35,6,1,0,2))
hpnicfRstpRootGuarded.setObjects((_E,_F))
if mibBuilder.loadTexts:hpnicfRstpRootGuarded.setStatus(_A)
hpnicfRstpBridgeLostRootPrimary=NotificationType((1,3,6,1,4,1,11,2,14,11,15,8,35,6,1,0,3))
if mibBuilder.loadTexts:hpnicfRstpBridgeLostRootPrimary.setStatus(_A)
hpnicfRstpLoopGuarded=NotificationType((1,3,6,1,4,1,11,2,14,11,15,8,35,6,1,0,4))
hpnicfRstpLoopGuarded.setObjects((_E,_F))
if mibBuilder.loadTexts:hpnicfRstpLoopGuarded.setStatus(_A)
mibBuilder.exportSymbols(_G,**{'EnabledStatus':EnabledStatus,'hpnicfLswRstpMib':hpnicfLswRstpMib,'hpnicfLswRstpMibObject':hpnicfLswRstpMibObject,'hpnicfRstpEventsV2':hpnicfRstpEventsV2,'hpnicfRstpBpduGuarded':hpnicfRstpBpduGuarded,'hpnicfRstpRootGuarded':hpnicfRstpRootGuarded,'hpnicfRstpBridgeLostRootPrimary':hpnicfRstpBridgeLostRootPrimary,'hpnicfRstpLoopGuarded':hpnicfRstpLoopGuarded,'hpnicfdot1dStpStatus':hpnicfdot1dStpStatus,'hpnicfdot1dStpForceVersion':hpnicfdot1dStpForceVersion,'hpnicfdot1dStpDiameter':hpnicfdot1dStpDiameter,'hpnicfdot1dStpRootBridgeAddress':hpnicfdot1dStpRootBridgeAddress,'hpnicfdot1dStpPortXTable':hpnicfdot1dStpPortXTable,_J:hpnicfdot1dStpPortXEntry,'hpnicfdot1dStpPortStatus':hpnicfdot1dStpPortStatus,'hpnicfdot1dStpPortEdgeport':hpnicfdot1dStpPortEdgeport,'hpnicfdot1dStpPortPointToPoint':hpnicfdot1dStpPortPointToPoint,'hpnicfdot1dStpMcheck':hpnicfdot1dStpMcheck,'hpnicfdot1dStpTransLimit':hpnicfdot1dStpTransLimit,'hpnicfdot1dStpRXStpBPDU':hpnicfdot1dStpRXStpBPDU,'hpnicfdot1dStpTXStpBPDU':hpnicfdot1dStpTXStpBPDU,'hpnicfdot1dStpRXTCNBPDU':hpnicfdot1dStpRXTCNBPDU,'hpnicfdot1dStpTXTCNBPDU':hpnicfdot1dStpTXTCNBPDU,'hpnicfdot1dStpRXRSTPBPDU':hpnicfdot1dStpRXRSTPBPDU,'hpnicfdot1dStpTXRSTPBPDU':hpnicfdot1dStpTXRSTPBPDU,'hpnicfdot1dStpClearStatistics':hpnicfdot1dStpClearStatistics,'hpnicfdot1dSetStpDefaultPortCost':hpnicfdot1dSetStpDefaultPortCost,'hpnicfdot1dStpRootGuard':hpnicfdot1dStpRootGuard,'hpnicfdot1dStpLoopGuard':hpnicfdot1dStpLoopGuard,'hpnicfdot1dStpPortBlockedReason':hpnicfdot1dStpPortBlockedReason,'hpnicfdot1dStpRXTCBPDU':hpnicfdot1dStpRXTCBPDU,'hpnicfdot1dStpPortSendingBPDUType':hpnicfdot1dStpPortSendingBPDUType,'hpnicfdot1dStpOperPortPointToPoint':hpnicfdot1dStpOperPortPointToPoint,'hpnicfDot1dStpBpduGuard':hpnicfDot1dStpBpduGuard,'hpnicfDot1dStpRootType':hpnicfDot1dStpRootType,'hpnicfDot1dTimeOutFactor':hpnicfDot1dTimeOutFactor,'hpnicfDot1dStpPathCostStandard':hpnicfDot1dStpPathCostStandard,'hpnicfdot1dStpIgnoredVlanTable':hpnicfdot1dStpIgnoredVlanTable,'hpnicfdot1dStpIgnoredVlanEntry':hpnicfdot1dStpIgnoredVlanEntry,_I:hpnicfdot1dVlan,'hpnicfdot1dStpIgnore':hpnicfdot1dStpIgnore})