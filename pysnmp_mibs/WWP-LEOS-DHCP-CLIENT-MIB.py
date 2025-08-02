_R='wwpLeosDhcpOptionCode'
_Q='wwpLeosDhcpRelayAgentCidStringPort'
_P='wwpLeosDhcpRelayAgentPort'
_O='wwpLeosDhcpRelayAgentInterfaceIpIndex'
_N='wwpLeosDhcpRelayAgentInterfaceIndex'
_M='wwpLeosDhcpOptionCodeIndex'
_L='DisplayString'
_K='TruthValue'
_J='wwpLeosDhcpRelayAgentVlan'
_I='seconds'
_H='enabled'
_G='disabled'
_F='read-create'
_E='WWP-LEOS-DHCP-CLIENT-MIB'
_D='read-write'
_C='read-only'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_L,'PhysAddress','RowStatus','TextualConvention',_K)
wwpModulesLeos,=mibBuilder.importSymbols('WWP-SMI','wwpModulesLeos')
wwpLeosDhcpClientMIB=ModuleIdentity((1,3,6,1,4,1,6141,2,60,17))
if mibBuilder.loadTexts:wwpLeosDhcpClientMIB.setRevisions(('2006-04-18 17:00','2002-11-01 17:00'))
_WwpLeosDhcpClientMIBObjects_ObjectIdentity=ObjectIdentity
wwpLeosDhcpClientMIBObjects=_WwpLeosDhcpClientMIBObjects_ObjectIdentity((1,3,6,1,4,1,6141,2,60,17,1))
_WwpLeosDhcpClient_ObjectIdentity=ObjectIdentity
wwpLeosDhcpClient=_WwpLeosDhcpClient_ObjectIdentity((1,3,6,1,4,1,6141,2,60,17,1,1))
class _WwpLeosDhcpIfName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_WwpLeosDhcpIfName_Type.__name__=_L
_WwpLeosDhcpIfName_Object=MibScalar
wwpLeosDhcpIfName=_WwpLeosDhcpIfName_Object((1,3,6,1,4,1,6141,2,60,17,1,1,1),_WwpLeosDhcpIfName_Type())
wwpLeosDhcpIfName.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosDhcpIfName.setStatus(_A)
class _WwpLeosDhcpStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enable',1),('disable',2)))
_WwpLeosDhcpStatus_Type.__name__=_B
_WwpLeosDhcpStatus_Object=MibScalar
wwpLeosDhcpStatus=_WwpLeosDhcpStatus_Object((1,3,6,1,4,1,6141,2,60,17,1,1,2),_WwpLeosDhcpStatus_Type())
wwpLeosDhcpStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosDhcpStatus.setStatus(_A)
class _WwpLeosDhcpState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*(('bound',1),(_G,2),('inform',3),('init',4),('rebinding',5),('renewing',6),('requesting',7),('selecting',8),('unknown',9)))
_WwpLeosDhcpState_Type.__name__=_B
_WwpLeosDhcpState_Object=MibScalar
wwpLeosDhcpState=_WwpLeosDhcpState_Object((1,3,6,1,4,1,6141,2,60,17,1,1,3),_WwpLeosDhcpState_Type())
wwpLeosDhcpState.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosDhcpState.setStatus(_A)
class _WwpLeosDhcpLeaseOffered_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_WwpLeosDhcpLeaseOffered_Type.__name__=_B
_WwpLeosDhcpLeaseOffered_Object=MibScalar
wwpLeosDhcpLeaseOffered=_WwpLeosDhcpLeaseOffered_Object((1,3,6,1,4,1,6141,2,60,17,1,1,5),_WwpLeosDhcpLeaseOffered_Type())
wwpLeosDhcpLeaseOffered.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosDhcpLeaseOffered.setStatus(_A)
if mibBuilder.loadTexts:wwpLeosDhcpLeaseOffered.setUnits(_I)
class _WwpLeosDhcpLeaseRemaining_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_WwpLeosDhcpLeaseRemaining_Type.__name__=_B
_WwpLeosDhcpLeaseRemaining_Object=MibScalar
wwpLeosDhcpLeaseRemaining=_WwpLeosDhcpLeaseRemaining_Object((1,3,6,1,4,1,6141,2,60,17,1,1,6),_WwpLeosDhcpLeaseRemaining_Type())
wwpLeosDhcpLeaseRemaining.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosDhcpLeaseRemaining.setStatus(_A)
if mibBuilder.loadTexts:wwpLeosDhcpLeaseRemaining.setUnits(_I)
class _WwpLeosDhcpDiscoveryMsgInterval_Type(Integer32):defaultValue=30;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_WwpLeosDhcpDiscoveryMsgInterval_Type.__name__=_B
_WwpLeosDhcpDiscoveryMsgInterval_Object=MibScalar
wwpLeosDhcpDiscoveryMsgInterval=_WwpLeosDhcpDiscoveryMsgInterval_Object((1,3,6,1,4,1,6141,2,60,17,1,1,7),_WwpLeosDhcpDiscoveryMsgInterval_Type())
wwpLeosDhcpDiscoveryMsgInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosDhcpDiscoveryMsgInterval.setStatus(_A)
if mibBuilder.loadTexts:wwpLeosDhcpDiscoveryMsgInterval.setUnits(_I)
class _WwpLeosDhcpRenewalTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_WwpLeosDhcpRenewalTime_Type.__name__=_B
_WwpLeosDhcpRenewalTime_Object=MibScalar
wwpLeosDhcpRenewalTime=_WwpLeosDhcpRenewalTime_Object((1,3,6,1,4,1,6141,2,60,17,1,1,8),_WwpLeosDhcpRenewalTime_Type())
wwpLeosDhcpRenewalTime.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosDhcpRenewalTime.setStatus(_A)
if mibBuilder.loadTexts:wwpLeosDhcpRenewalTime.setUnits(_I)
class _WwpLeosDhcpRebindingTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_WwpLeosDhcpRebindingTime_Type.__name__=_B
_WwpLeosDhcpRebindingTime_Object=MibScalar
wwpLeosDhcpRebindingTime=_WwpLeosDhcpRebindingTime_Object((1,3,6,1,4,1,6141,2,60,17,1,1,9),_WwpLeosDhcpRebindingTime_Type())
wwpLeosDhcpRebindingTime.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosDhcpRebindingTime.setStatus(_A)
if mibBuilder.loadTexts:wwpLeosDhcpRebindingTime.setUnits(_I)
_WwpLeosDhcpServerAddress_Type=IpAddress
_WwpLeosDhcpServerAddress_Object=MibScalar
wwpLeosDhcpServerAddress=_WwpLeosDhcpServerAddress_Object((1,3,6,1,4,1,6141,2,60,17,1,1,10),_WwpLeosDhcpServerAddress_Type())
wwpLeosDhcpServerAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosDhcpServerAddress.setStatus(_A)
class _WwpLeosDhcpRenewLease_Type(TruthValue):defaultValue=2
_WwpLeosDhcpRenewLease_Type.__name__=_K
_WwpLeosDhcpRenewLease_Object=MibScalar
wwpLeosDhcpRenewLease=_WwpLeosDhcpRenewLease_Object((1,3,6,1,4,1,6141,2,60,17,1,1,11),_WwpLeosDhcpRenewLease_Type())
wwpLeosDhcpRenewLease.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosDhcpRenewLease.setStatus(_A)
class _WwpLeosDhcpReleaseLease_Type(TruthValue):defaultValue=2
_WwpLeosDhcpReleaseLease_Type.__name__=_K
_WwpLeosDhcpReleaseLease_Object=MibScalar
wwpLeosDhcpReleaseLease=_WwpLeosDhcpReleaseLease_Object((1,3,6,1,4,1,6141,2,60,17,1,1,12),_WwpLeosDhcpReleaseLease_Type())
wwpLeosDhcpReleaseLease.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosDhcpReleaseLease.setStatus(_A)
_WwpLeosDhcpClientOptionTable_Object=MibTable
wwpLeosDhcpClientOptionTable=_WwpLeosDhcpClientOptionTable_Object((1,3,6,1,4,1,6141,2,60,17,1,1,13))
if mibBuilder.loadTexts:wwpLeosDhcpClientOptionTable.setStatus(_A)
_WwpLeosDhcpClientOptionEntry_Object=MibTableRow
wwpLeosDhcpClientOptionEntry=_WwpLeosDhcpClientOptionEntry_Object((1,3,6,1,4,1,6141,2,60,17,1,1,13,1))
wwpLeosDhcpClientOptionEntry.setIndexNames((0,_E,_M))
if mibBuilder.loadTexts:wwpLeosDhcpClientOptionEntry.setStatus(_A)
class _WwpLeosDhcpOptionCodeIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_WwpLeosDhcpOptionCodeIndex_Type.__name__=_B
_WwpLeosDhcpOptionCodeIndex_Object=MibTableColumn
wwpLeosDhcpOptionCodeIndex=_WwpLeosDhcpOptionCodeIndex_Object((1,3,6,1,4,1,6141,2,60,17,1,1,13,1,1),_WwpLeosDhcpOptionCodeIndex_Type())
wwpLeosDhcpOptionCodeIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosDhcpOptionCodeIndex.setStatus(_A)
_WwpLeosDhcpOptionDesc_Type=DisplayString
_WwpLeosDhcpOptionDesc_Object=MibTableColumn
wwpLeosDhcpOptionDesc=_WwpLeosDhcpOptionDesc_Object((1,3,6,1,4,1,6141,2,60,17,1,1,13,1,2),_WwpLeosDhcpOptionDesc_Type())
wwpLeosDhcpOptionDesc.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosDhcpOptionDesc.setStatus(_A)
class _WwpLeosDhcpOptionCode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_WwpLeosDhcpOptionCode_Type.__name__=_B
_WwpLeosDhcpOptionCode_Object=MibTableColumn
wwpLeosDhcpOptionCode=_WwpLeosDhcpOptionCode_Object((1,3,6,1,4,1,6141,2,60,17,1,1,13,1,3),_WwpLeosDhcpOptionCode_Type())
wwpLeosDhcpOptionCode.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosDhcpOptionCode.setStatus(_A)
class _WwpLeosDhcpOptionState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_WwpLeosDhcpOptionState_Type.__name__=_B
_WwpLeosDhcpOptionState_Object=MibTableColumn
wwpLeosDhcpOptionState=_WwpLeosDhcpOptionState_Object((1,3,6,1,4,1,6141,2,60,17,1,1,13,1,4),_WwpLeosDhcpOptionState_Type())
wwpLeosDhcpOptionState.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosDhcpOptionState.setStatus(_A)
_WwpLeosDhcpRelayAgent_ObjectIdentity=ObjectIdentity
wwpLeosDhcpRelayAgent=_WwpLeosDhcpRelayAgent_ObjectIdentity((1,3,6,1,4,1,6141,2,60,17,1,2))
_WwpLeosDhcpRelayAgentGlobalAttrs_ObjectIdentity=ObjectIdentity
wwpLeosDhcpRelayAgentGlobalAttrs=_WwpLeosDhcpRelayAgentGlobalAttrs_ObjectIdentity((1,3,6,1,4,1,6141,2,60,17,1,2,1))
class _WwpLeosDhcpRelayAgentCircuitId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('slotAndPort',1),('slotAndPortAndVlan',2),('cidString',3)))
_WwpLeosDhcpRelayAgentCircuitId_Type.__name__=_B
_WwpLeosDhcpRelayAgentCircuitId_Object=MibScalar
wwpLeosDhcpRelayAgentCircuitId=_WwpLeosDhcpRelayAgentCircuitId_Object((1,3,6,1,4,1,6141,2,60,17,1,2,1,1),_WwpLeosDhcpRelayAgentCircuitId_Type())
wwpLeosDhcpRelayAgentCircuitId.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosDhcpRelayAgentCircuitId.setStatus(_A)
class _WwpLeosDhcpRelayAgentRemoteId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('macAddress',1),('hostName',2)))
_WwpLeosDhcpRelayAgentRemoteId_Type.__name__=_B
_WwpLeosDhcpRelayAgentRemoteId_Object=MibScalar
wwpLeosDhcpRelayAgentRemoteId=_WwpLeosDhcpRelayAgentRemoteId_Object((1,3,6,1,4,1,6141,2,60,17,1,2,1,2),_WwpLeosDhcpRelayAgentRemoteId_Type())
wwpLeosDhcpRelayAgentRemoteId.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosDhcpRelayAgentRemoteId.setStatus(_A)
class _WwpLeosDhcpRelayAgentL2State_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_WwpLeosDhcpRelayAgentL2State_Type.__name__=_B
_WwpLeosDhcpRelayAgentL2State_Object=MibScalar
wwpLeosDhcpRelayAgentL2State=_WwpLeosDhcpRelayAgentL2State_Object((1,3,6,1,4,1,6141,2,60,17,1,2,1,3),_WwpLeosDhcpRelayAgentL2State_Type())
wwpLeosDhcpRelayAgentL2State.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosDhcpRelayAgentL2State.setStatus(_A)
class _WwpLeosDhcpRelayAgentL3State_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_WwpLeosDhcpRelayAgentL3State_Type.__name__=_B
_WwpLeosDhcpRelayAgentL3State_Object=MibScalar
wwpLeosDhcpRelayAgentL3State=_WwpLeosDhcpRelayAgentL3State_Object((1,3,6,1,4,1,6141,2,60,17,1,2,1,4),_WwpLeosDhcpRelayAgentL3State_Type())
wwpLeosDhcpRelayAgentL3State.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosDhcpRelayAgentL3State.setStatus(_A)
_WwpLeosDhcpRelayAgentL2StateTable_Object=MibTable
wwpLeosDhcpRelayAgentL2StateTable=_WwpLeosDhcpRelayAgentL2StateTable_Object((1,3,6,1,4,1,6141,2,60,17,1,2,2))
if mibBuilder.loadTexts:wwpLeosDhcpRelayAgentL2StateTable.setStatus(_A)
_WwpLeosDhcpRelayAgentL2StateEntry_Object=MibTableRow
wwpLeosDhcpRelayAgentL2StateEntry=_WwpLeosDhcpRelayAgentL2StateEntry_Object((1,3,6,1,4,1,6141,2,60,17,1,2,2,1))
wwpLeosDhcpRelayAgentL2StateEntry.setIndexNames((0,_E,_J))
if mibBuilder.loadTexts:wwpLeosDhcpRelayAgentL2StateEntry.setStatus(_A)
class _WwpLeosDhcpRelayAgentVlan_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,24576))
_WwpLeosDhcpRelayAgentVlan_Type.__name__=_B
_WwpLeosDhcpRelayAgentVlan_Object=MibTableColumn
wwpLeosDhcpRelayAgentVlan=_WwpLeosDhcpRelayAgentVlan_Object((1,3,6,1,4,1,6141,2,60,17,1,2,2,1,1),_WwpLeosDhcpRelayAgentVlan_Type())
wwpLeosDhcpRelayAgentVlan.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosDhcpRelayAgentVlan.setStatus(_A)
class _WwpLeosDhcpRelayAgentL2AdminState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_WwpLeosDhcpRelayAgentL2AdminState_Type.__name__=_B
_WwpLeosDhcpRelayAgentL2AdminState_Object=MibTableColumn
wwpLeosDhcpRelayAgentL2AdminState=_WwpLeosDhcpRelayAgentL2AdminState_Object((1,3,6,1,4,1,6141,2,60,17,1,2,2,1,2),_WwpLeosDhcpRelayAgentL2AdminState_Type())
wwpLeosDhcpRelayAgentL2AdminState.setMaxAccess(_F)
if mibBuilder.loadTexts:wwpLeosDhcpRelayAgentL2AdminState.setStatus(_A)
class _WwpLeosDhcpRelayAgentL2OperState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_WwpLeosDhcpRelayAgentL2OperState_Type.__name__=_B
_WwpLeosDhcpRelayAgentL2OperState_Object=MibTableColumn
wwpLeosDhcpRelayAgentL2OperState=_WwpLeosDhcpRelayAgentL2OperState_Object((1,3,6,1,4,1,6141,2,60,17,1,2,2,1,3),_WwpLeosDhcpRelayAgentL2OperState_Type())
wwpLeosDhcpRelayAgentL2OperState.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosDhcpRelayAgentL2OperState.setStatus(_A)
_WwpLeosDhcpRelayAgentL2StatsClear_Type=TruthValue
_WwpLeosDhcpRelayAgentL2StatsClear_Object=MibTableColumn
wwpLeosDhcpRelayAgentL2StatsClear=_WwpLeosDhcpRelayAgentL2StatsClear_Object((1,3,6,1,4,1,6141,2,60,17,1,2,2,1,4),_WwpLeosDhcpRelayAgentL2StatsClear_Type())
wwpLeosDhcpRelayAgentL2StatsClear.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosDhcpRelayAgentL2StatsClear.setStatus(_A)
_WwpLeosDhcpRelayAgentL2RowStatus_Type=RowStatus
_WwpLeosDhcpRelayAgentL2RowStatus_Object=MibTableColumn
wwpLeosDhcpRelayAgentL2RowStatus=_WwpLeosDhcpRelayAgentL2RowStatus_Object((1,3,6,1,4,1,6141,2,60,17,1,2,2,1,5),_WwpLeosDhcpRelayAgentL2RowStatus_Type())
wwpLeosDhcpRelayAgentL2RowStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:wwpLeosDhcpRelayAgentL2RowStatus.setStatus(_A)
_WwpLeosDhcpRelayAgentL3StateTable_Object=MibTable
wwpLeosDhcpRelayAgentL3StateTable=_WwpLeosDhcpRelayAgentL3StateTable_Object((1,3,6,1,4,1,6141,2,60,17,1,2,3))
if mibBuilder.loadTexts:wwpLeosDhcpRelayAgentL3StateTable.setStatus(_A)
_WwpLeosDhcpRelayAgentL3StateEntry_Object=MibTableRow
wwpLeosDhcpRelayAgentL3StateEntry=_WwpLeosDhcpRelayAgentL3StateEntry_Object((1,3,6,1,4,1,6141,2,60,17,1,2,3,1))
wwpLeosDhcpRelayAgentL3StateEntry.setIndexNames((0,_E,_N))
if mibBuilder.loadTexts:wwpLeosDhcpRelayAgentL3StateEntry.setStatus(_A)
class _WwpLeosDhcpRelayAgentInterfaceIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_WwpLeosDhcpRelayAgentInterfaceIndex_Type.__name__=_B
_WwpLeosDhcpRelayAgentInterfaceIndex_Object=MibTableColumn
wwpLeosDhcpRelayAgentInterfaceIndex=_WwpLeosDhcpRelayAgentInterfaceIndex_Object((1,3,6,1,4,1,6141,2,60,17,1,2,3,1,1),_WwpLeosDhcpRelayAgentInterfaceIndex_Type())
wwpLeosDhcpRelayAgentInterfaceIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosDhcpRelayAgentInterfaceIndex.setStatus(_A)
class _WwpLeosDhcpRelayAgentL3AdminState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_WwpLeosDhcpRelayAgentL3AdminState_Type.__name__=_B
_WwpLeosDhcpRelayAgentL3AdminState_Object=MibTableColumn
wwpLeosDhcpRelayAgentL3AdminState=_WwpLeosDhcpRelayAgentL3AdminState_Object((1,3,6,1,4,1,6141,2,60,17,1,2,3,1,2),_WwpLeosDhcpRelayAgentL3AdminState_Type())
wwpLeosDhcpRelayAgentL3AdminState.setMaxAccess(_F)
if mibBuilder.loadTexts:wwpLeosDhcpRelayAgentL3AdminState.setStatus(_A)
class _WwpLeosDhcpRelayAgentL3OperState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_WwpLeosDhcpRelayAgentL3OperState_Type.__name__=_B
_WwpLeosDhcpRelayAgentL3OperState_Object=MibTableColumn
wwpLeosDhcpRelayAgentL3OperState=_WwpLeosDhcpRelayAgentL3OperState_Object((1,3,6,1,4,1,6141,2,60,17,1,2,3,1,3),_WwpLeosDhcpRelayAgentL3OperState_Type())
wwpLeosDhcpRelayAgentL3OperState.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosDhcpRelayAgentL3OperState.setStatus(_A)
_WwpLeosDhcpRelayAgentL3RowStatus_Type=RowStatus
_WwpLeosDhcpRelayAgentL3RowStatus_Object=MibTableColumn
wwpLeosDhcpRelayAgentL3RowStatus=_WwpLeosDhcpRelayAgentL3RowStatus_Object((1,3,6,1,4,1,6141,2,60,17,1,2,3,1,4),_WwpLeosDhcpRelayAgentL3RowStatus_Type())
wwpLeosDhcpRelayAgentL3RowStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:wwpLeosDhcpRelayAgentL3RowStatus.setStatus(_A)
_WwpLeosDhcpRelayAgentInterfaceIpTable_Object=MibTable
wwpLeosDhcpRelayAgentInterfaceIpTable=_WwpLeosDhcpRelayAgentInterfaceIpTable_Object((1,3,6,1,4,1,6141,2,60,17,1,2,4))
if mibBuilder.loadTexts:wwpLeosDhcpRelayAgentInterfaceIpTable.setStatus(_A)
_WwpLeosDhcpRelayAgentInterfaceIpEntry_Object=MibTableRow
wwpLeosDhcpRelayAgentInterfaceIpEntry=_WwpLeosDhcpRelayAgentInterfaceIpEntry_Object((1,3,6,1,4,1,6141,2,60,17,1,2,4,1))
wwpLeosDhcpRelayAgentInterfaceIpEntry.setIndexNames((0,_E,_O))
if mibBuilder.loadTexts:wwpLeosDhcpRelayAgentInterfaceIpEntry.setStatus(_A)
class _WwpLeosDhcpRelayAgentInterfaceIpIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_WwpLeosDhcpRelayAgentInterfaceIpIndex_Type.__name__=_B
_WwpLeosDhcpRelayAgentInterfaceIpIndex_Object=MibTableColumn
wwpLeosDhcpRelayAgentInterfaceIpIndex=_WwpLeosDhcpRelayAgentInterfaceIpIndex_Object((1,3,6,1,4,1,6141,2,60,17,1,2,4,1,1),_WwpLeosDhcpRelayAgentInterfaceIpIndex_Type())
wwpLeosDhcpRelayAgentInterfaceIpIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosDhcpRelayAgentInterfaceIpIndex.setStatus(_A)
_WwpLeosDhcpRelayAgentInterfaceIpAddr_Type=IpAddress
_WwpLeosDhcpRelayAgentInterfaceIpAddr_Object=MibTableColumn
wwpLeosDhcpRelayAgentInterfaceIpAddr=_WwpLeosDhcpRelayAgentInterfaceIpAddr_Object((1,3,6,1,4,1,6141,2,60,17,1,2,4,1,2),_WwpLeosDhcpRelayAgentInterfaceIpAddr_Type())
wwpLeosDhcpRelayAgentInterfaceIpAddr.setMaxAccess(_F)
if mibBuilder.loadTexts:wwpLeosDhcpRelayAgentInterfaceIpAddr.setStatus(_A)
_WwpLeosDhcpRelayAgentInterfaceIpRowStatus_Type=RowStatus
_WwpLeosDhcpRelayAgentInterfaceIpRowStatus_Object=MibTableColumn
wwpLeosDhcpRelayAgentInterfaceIpRowStatus=_WwpLeosDhcpRelayAgentInterfaceIpRowStatus_Object((1,3,6,1,4,1,6141,2,60,17,1,2,4,1,3),_WwpLeosDhcpRelayAgentInterfaceIpRowStatus_Type())
wwpLeosDhcpRelayAgentInterfaceIpRowStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:wwpLeosDhcpRelayAgentInterfaceIpRowStatus.setStatus(_A)
_WwpLeosDhcpRelayAgentTrustTable_Object=MibTable
wwpLeosDhcpRelayAgentTrustTable=_WwpLeosDhcpRelayAgentTrustTable_Object((1,3,6,1,4,1,6141,2,60,17,1,2,5))
if mibBuilder.loadTexts:wwpLeosDhcpRelayAgentTrustTable.setStatus(_A)
_WwpLeosDhcpRelayAgentTrustEntry_Object=MibTableRow
wwpLeosDhcpRelayAgentTrustEntry=_WwpLeosDhcpRelayAgentTrustEntry_Object((1,3,6,1,4,1,6141,2,60,17,1,2,5,1))
wwpLeosDhcpRelayAgentTrustEntry.setIndexNames((0,_E,_J),(0,_E,_P))
if mibBuilder.loadTexts:wwpLeosDhcpRelayAgentTrustEntry.setStatus(_A)
class _WwpLeosDhcpRelayAgentPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_WwpLeosDhcpRelayAgentPort_Type.__name__=_B
_WwpLeosDhcpRelayAgentPort_Object=MibTableColumn
wwpLeosDhcpRelayAgentPort=_WwpLeosDhcpRelayAgentPort_Object((1,3,6,1,4,1,6141,2,60,17,1,2,5,1,1),_WwpLeosDhcpRelayAgentPort_Type())
wwpLeosDhcpRelayAgentPort.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosDhcpRelayAgentPort.setStatus(_A)
class _WwpLeosDhcpRelayAgentTrustMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('clientTrust',1),('serverTrust',2),('dualRoleTrust',3),('unTrust',4)))
_WwpLeosDhcpRelayAgentTrustMode_Type.__name__=_B
_WwpLeosDhcpRelayAgentTrustMode_Object=MibTableColumn
wwpLeosDhcpRelayAgentTrustMode=_WwpLeosDhcpRelayAgentTrustMode_Object((1,3,6,1,4,1,6141,2,60,17,1,2,5,1,2),_WwpLeosDhcpRelayAgentTrustMode_Type())
wwpLeosDhcpRelayAgentTrustMode.setMaxAccess(_F)
if mibBuilder.loadTexts:wwpLeosDhcpRelayAgentTrustMode.setStatus(_A)
_WwpLeosDhcpRelayAgentL2StatsTable_Object=MibTable
wwpLeosDhcpRelayAgentL2StatsTable=_WwpLeosDhcpRelayAgentL2StatsTable_Object((1,3,6,1,4,1,6141,2,60,17,1,2,6))
if mibBuilder.loadTexts:wwpLeosDhcpRelayAgentL2StatsTable.setStatus(_A)
_WwpLeosDhcpRelayAgentL2StatsEntry_Object=MibTableRow
wwpLeosDhcpRelayAgentL2StatsEntry=_WwpLeosDhcpRelayAgentL2StatsEntry_Object((1,3,6,1,4,1,6141,2,60,17,1,2,6,1))
wwpLeosDhcpRelayAgentL2StatsEntry.setIndexNames((0,_E,_J))
if mibBuilder.loadTexts:wwpLeosDhcpRelayAgentL2StatsEntry.setStatus(_A)
_WwpLeosDhcpRelayAgentL2IpSecHeaders_Type=Counter32
_WwpLeosDhcpRelayAgentL2IpSecHeaders_Object=MibTableColumn
wwpLeosDhcpRelayAgentL2IpSecHeaders=_WwpLeosDhcpRelayAgentL2IpSecHeaders_Object((1,3,6,1,4,1,6141,2,60,17,1,2,6,1,1),_WwpLeosDhcpRelayAgentL2IpSecHeaders_Type())
wwpLeosDhcpRelayAgentL2IpSecHeaders.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosDhcpRelayAgentL2IpSecHeaders.setStatus(_A)
_WwpLeosDhcpRelayAgentL2Option82Added_Type=Counter32
_WwpLeosDhcpRelayAgentL2Option82Added_Object=MibTableColumn
wwpLeosDhcpRelayAgentL2Option82Added=_WwpLeosDhcpRelayAgentL2Option82Added_Object((1,3,6,1,4,1,6141,2,60,17,1,2,6,1,2),_WwpLeosDhcpRelayAgentL2Option82Added_Type())
wwpLeosDhcpRelayAgentL2Option82Added.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosDhcpRelayAgentL2Option82Added.setStatus(_A)
_WwpLeosDhcpRelayAgentL2Option82Removed_Type=Counter32
_WwpLeosDhcpRelayAgentL2Option82Removed_Object=MibTableColumn
wwpLeosDhcpRelayAgentL2Option82Removed=_WwpLeosDhcpRelayAgentL2Option82Removed_Object((1,3,6,1,4,1,6141,2,60,17,1,2,6,1,3),_WwpLeosDhcpRelayAgentL2Option82Removed_Type())
wwpLeosDhcpRelayAgentL2Option82Removed.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosDhcpRelayAgentL2Option82Removed.setStatus(_A)
_WwpLeosDhcpRelayAgentL2UntrustedClientPortPktsRx_Type=Counter32
_WwpLeosDhcpRelayAgentL2UntrustedClientPortPktsRx_Object=MibTableColumn
wwpLeosDhcpRelayAgentL2UntrustedClientPortPktsRx=_WwpLeosDhcpRelayAgentL2UntrustedClientPortPktsRx_Object((1,3,6,1,4,1,6141,2,60,17,1,2,6,1,4),_WwpLeosDhcpRelayAgentL2UntrustedClientPortPktsRx_Type())
wwpLeosDhcpRelayAgentL2UntrustedClientPortPktsRx.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosDhcpRelayAgentL2UntrustedClientPortPktsRx.setStatus(_A)
_WwpLeosDhcpRelayAgentL2UntrustedServerPortPktsRx_Type=Counter32
_WwpLeosDhcpRelayAgentL2UntrustedServerPortPktsRx_Object=MibTableColumn
wwpLeosDhcpRelayAgentL2UntrustedServerPortPktsRx=_WwpLeosDhcpRelayAgentL2UntrustedServerPortPktsRx_Object((1,3,6,1,4,1,6141,2,60,17,1,2,6,1,5),_WwpLeosDhcpRelayAgentL2UntrustedServerPortPktsRx_Type())
wwpLeosDhcpRelayAgentL2UntrustedServerPortPktsRx.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosDhcpRelayAgentL2UntrustedServerPortPktsRx.setStatus(_A)
_WwpLeosDhcpRelayAgentL2SpoofedDhcpPkts_Type=Counter32
_WwpLeosDhcpRelayAgentL2SpoofedDhcpPkts_Object=MibTableColumn
wwpLeosDhcpRelayAgentL2SpoofedDhcpPkts=_WwpLeosDhcpRelayAgentL2SpoofedDhcpPkts_Object((1,3,6,1,4,1,6141,2,60,17,1,2,6,1,6),_WwpLeosDhcpRelayAgentL2SpoofedDhcpPkts_Type())
wwpLeosDhcpRelayAgentL2SpoofedDhcpPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosDhcpRelayAgentL2SpoofedDhcpPkts.setStatus(_A)
_WwpLeosDhcpRelayAgentL2Option82ExceedMTU_Type=Counter32
_WwpLeosDhcpRelayAgentL2Option82ExceedMTU_Object=MibTableColumn
wwpLeosDhcpRelayAgentL2Option82ExceedMTU=_WwpLeosDhcpRelayAgentL2Option82ExceedMTU_Object((1,3,6,1,4,1,6141,2,60,17,1,2,6,1,7),_WwpLeosDhcpRelayAgentL2Option82ExceedMTU_Type())
wwpLeosDhcpRelayAgentL2Option82ExceedMTU.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosDhcpRelayAgentL2Option82ExceedMTU.setStatus(_A)
_WwpLeosDhcpRelayAgentL2NoTrustedServerPktDrop_Type=Counter32
_WwpLeosDhcpRelayAgentL2NoTrustedServerPktDrop_Object=MibTableColumn
wwpLeosDhcpRelayAgentL2NoTrustedServerPktDrop=_WwpLeosDhcpRelayAgentL2NoTrustedServerPktDrop_Object((1,3,6,1,4,1,6141,2,60,17,1,2,6,1,8),_WwpLeosDhcpRelayAgentL2NoTrustedServerPktDrop_Type())
wwpLeosDhcpRelayAgentL2NoTrustedServerPktDrop.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosDhcpRelayAgentL2NoTrustedServerPktDrop.setStatus(_A)
_WwpLeosDhcpRelayAgentL2NoTrustedClientPktDrop_Type=Counter32
_WwpLeosDhcpRelayAgentL2NoTrustedClientPktDrop_Object=MibTableColumn
wwpLeosDhcpRelayAgentL2NoTrustedClientPktDrop=_WwpLeosDhcpRelayAgentL2NoTrustedClientPktDrop_Object((1,3,6,1,4,1,6141,2,60,17,1,2,6,1,9),_WwpLeosDhcpRelayAgentL2NoTrustedClientPktDrop_Type())
wwpLeosDhcpRelayAgentL2NoTrustedClientPktDrop.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosDhcpRelayAgentL2NoTrustedClientPktDrop.setStatus(_A)
_WwpLeosDhcpRelayAgentCidStringTable_Object=MibTable
wwpLeosDhcpRelayAgentCidStringTable=_WwpLeosDhcpRelayAgentCidStringTable_Object((1,3,6,1,4,1,6141,2,60,17,1,2,7))
if mibBuilder.loadTexts:wwpLeosDhcpRelayAgentCidStringTable.setStatus(_A)
_WwpLeosDhcpRelayAgentCidStringEntry_Object=MibTableRow
wwpLeosDhcpRelayAgentCidStringEntry=_WwpLeosDhcpRelayAgentCidStringEntry_Object((1,3,6,1,4,1,6141,2,60,17,1,2,7,1))
wwpLeosDhcpRelayAgentCidStringEntry.setIndexNames((0,_E,_J),(0,_E,_Q))
if mibBuilder.loadTexts:wwpLeosDhcpRelayAgentCidStringEntry.setStatus(_A)
class _WwpLeosDhcpRelayAgentCidStringPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_WwpLeosDhcpRelayAgentCidStringPort_Type.__name__=_B
_WwpLeosDhcpRelayAgentCidStringPort_Object=MibTableColumn
wwpLeosDhcpRelayAgentCidStringPort=_WwpLeosDhcpRelayAgentCidStringPort_Object((1,3,6,1,4,1,6141,2,60,17,1,2,7,1,1),_WwpLeosDhcpRelayAgentCidStringPort_Type())
wwpLeosDhcpRelayAgentCidStringPort.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosDhcpRelayAgentCidStringPort.setStatus(_A)
_WwpLeosDhcpRelayAgentCidString_Type=DisplayString
_WwpLeosDhcpRelayAgentCidString_Object=MibTableColumn
wwpLeosDhcpRelayAgentCidString=_WwpLeosDhcpRelayAgentCidString_Object((1,3,6,1,4,1,6141,2,60,17,1,2,7,1,2),_WwpLeosDhcpRelayAgentCidString_Type())
wwpLeosDhcpRelayAgentCidString.setMaxAccess(_F)
if mibBuilder.loadTexts:wwpLeosDhcpRelayAgentCidString.setStatus(_A)
_WwpLeosDhcpRelayAgentCidStringRowStatus_Type=RowStatus
_WwpLeosDhcpRelayAgentCidStringRowStatus_Object=MibTableColumn
wwpLeosDhcpRelayAgentCidStringRowStatus=_WwpLeosDhcpRelayAgentCidStringRowStatus_Object((1,3,6,1,4,1,6141,2,60,17,1,2,7,1,3),_WwpLeosDhcpRelayAgentCidStringRowStatus_Type())
wwpLeosDhcpRelayAgentCidStringRowStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:wwpLeosDhcpRelayAgentCidStringRowStatus.setStatus(_A)
_WwpLeosDhcpClientMIBNotificationPrefix_ObjectIdentity=ObjectIdentity
wwpLeosDhcpClientMIBNotificationPrefix=_WwpLeosDhcpClientMIBNotificationPrefix_ObjectIdentity((1,3,6,1,4,1,6141,2,60,17,2))
_WwpLeosDhcpClientMIBNotifications_ObjectIdentity=ObjectIdentity
wwpLeosDhcpClientMIBNotifications=_WwpLeosDhcpClientMIBNotifications_ObjectIdentity((1,3,6,1,4,1,6141,2,60,17,2,0))
_WwpLeosDhcpClientMIBConformance_ObjectIdentity=ObjectIdentity
wwpLeosDhcpClientMIBConformance=_WwpLeosDhcpClientMIBConformance_ObjectIdentity((1,3,6,1,4,1,6141,2,60,17,3))
_WwpLeosDhcpClientMIBCompliances_ObjectIdentity=ObjectIdentity
wwpLeosDhcpClientMIBCompliances=_WwpLeosDhcpClientMIBCompliances_ObjectIdentity((1,3,6,1,4,1,6141,2,60,17,3,1))
_WwpLeosDhcpClientMIBGroups_ObjectIdentity=ObjectIdentity
wwpLeosDhcpClientMIBGroups=_WwpLeosDhcpClientMIBGroups_ObjectIdentity((1,3,6,1,4,1,6141,2,60,17,3,2))
wwpLeosDhcpClientOptionDisabledNotification=NotificationType((1,3,6,1,4,1,6141,2,60,17,2,0,1))
wwpLeosDhcpClientOptionDisabledNotification.setObjects((_E,_R))
if mibBuilder.loadTexts:wwpLeosDhcpClientOptionDisabledNotification.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'wwpLeosDhcpClientMIB':wwpLeosDhcpClientMIB,'wwpLeosDhcpClientMIBObjects':wwpLeosDhcpClientMIBObjects,'wwpLeosDhcpClient':wwpLeosDhcpClient,'wwpLeosDhcpIfName':wwpLeosDhcpIfName,'wwpLeosDhcpStatus':wwpLeosDhcpStatus,'wwpLeosDhcpState':wwpLeosDhcpState,'wwpLeosDhcpLeaseOffered':wwpLeosDhcpLeaseOffered,'wwpLeosDhcpLeaseRemaining':wwpLeosDhcpLeaseRemaining,'wwpLeosDhcpDiscoveryMsgInterval':wwpLeosDhcpDiscoveryMsgInterval,'wwpLeosDhcpRenewalTime':wwpLeosDhcpRenewalTime,'wwpLeosDhcpRebindingTime':wwpLeosDhcpRebindingTime,'wwpLeosDhcpServerAddress':wwpLeosDhcpServerAddress,'wwpLeosDhcpRenewLease':wwpLeosDhcpRenewLease,'wwpLeosDhcpReleaseLease':wwpLeosDhcpReleaseLease,'wwpLeosDhcpClientOptionTable':wwpLeosDhcpClientOptionTable,'wwpLeosDhcpClientOptionEntry':wwpLeosDhcpClientOptionEntry,_M:wwpLeosDhcpOptionCodeIndex,'wwpLeosDhcpOptionDesc':wwpLeosDhcpOptionDesc,_R:wwpLeosDhcpOptionCode,'wwpLeosDhcpOptionState':wwpLeosDhcpOptionState,'wwpLeosDhcpRelayAgent':wwpLeosDhcpRelayAgent,'wwpLeosDhcpRelayAgentGlobalAttrs':wwpLeosDhcpRelayAgentGlobalAttrs,'wwpLeosDhcpRelayAgentCircuitId':wwpLeosDhcpRelayAgentCircuitId,'wwpLeosDhcpRelayAgentRemoteId':wwpLeosDhcpRelayAgentRemoteId,'wwpLeosDhcpRelayAgentL2State':wwpLeosDhcpRelayAgentL2State,'wwpLeosDhcpRelayAgentL3State':wwpLeosDhcpRelayAgentL3State,'wwpLeosDhcpRelayAgentL2StateTable':wwpLeosDhcpRelayAgentL2StateTable,'wwpLeosDhcpRelayAgentL2StateEntry':wwpLeosDhcpRelayAgentL2StateEntry,_J:wwpLeosDhcpRelayAgentVlan,'wwpLeosDhcpRelayAgentL2AdminState':wwpLeosDhcpRelayAgentL2AdminState,'wwpLeosDhcpRelayAgentL2OperState':wwpLeosDhcpRelayAgentL2OperState,'wwpLeosDhcpRelayAgentL2StatsClear':wwpLeosDhcpRelayAgentL2StatsClear,'wwpLeosDhcpRelayAgentL2RowStatus':wwpLeosDhcpRelayAgentL2RowStatus,'wwpLeosDhcpRelayAgentL3StateTable':wwpLeosDhcpRelayAgentL3StateTable,'wwpLeosDhcpRelayAgentL3StateEntry':wwpLeosDhcpRelayAgentL3StateEntry,_N:wwpLeosDhcpRelayAgentInterfaceIndex,'wwpLeosDhcpRelayAgentL3AdminState':wwpLeosDhcpRelayAgentL3AdminState,'wwpLeosDhcpRelayAgentL3OperState':wwpLeosDhcpRelayAgentL3OperState,'wwpLeosDhcpRelayAgentL3RowStatus':wwpLeosDhcpRelayAgentL3RowStatus,'wwpLeosDhcpRelayAgentInterfaceIpTable':wwpLeosDhcpRelayAgentInterfaceIpTable,'wwpLeosDhcpRelayAgentInterfaceIpEntry':wwpLeosDhcpRelayAgentInterfaceIpEntry,_O:wwpLeosDhcpRelayAgentInterfaceIpIndex,'wwpLeosDhcpRelayAgentInterfaceIpAddr':wwpLeosDhcpRelayAgentInterfaceIpAddr,'wwpLeosDhcpRelayAgentInterfaceIpRowStatus':wwpLeosDhcpRelayAgentInterfaceIpRowStatus,'wwpLeosDhcpRelayAgentTrustTable':wwpLeosDhcpRelayAgentTrustTable,'wwpLeosDhcpRelayAgentTrustEntry':wwpLeosDhcpRelayAgentTrustEntry,_P:wwpLeosDhcpRelayAgentPort,'wwpLeosDhcpRelayAgentTrustMode':wwpLeosDhcpRelayAgentTrustMode,'wwpLeosDhcpRelayAgentL2StatsTable':wwpLeosDhcpRelayAgentL2StatsTable,'wwpLeosDhcpRelayAgentL2StatsEntry':wwpLeosDhcpRelayAgentL2StatsEntry,'wwpLeosDhcpRelayAgentL2IpSecHeaders':wwpLeosDhcpRelayAgentL2IpSecHeaders,'wwpLeosDhcpRelayAgentL2Option82Added':wwpLeosDhcpRelayAgentL2Option82Added,'wwpLeosDhcpRelayAgentL2Option82Removed':wwpLeosDhcpRelayAgentL2Option82Removed,'wwpLeosDhcpRelayAgentL2UntrustedClientPortPktsRx':wwpLeosDhcpRelayAgentL2UntrustedClientPortPktsRx,'wwpLeosDhcpRelayAgentL2UntrustedServerPortPktsRx':wwpLeosDhcpRelayAgentL2UntrustedServerPortPktsRx,'wwpLeosDhcpRelayAgentL2SpoofedDhcpPkts':wwpLeosDhcpRelayAgentL2SpoofedDhcpPkts,'wwpLeosDhcpRelayAgentL2Option82ExceedMTU':wwpLeosDhcpRelayAgentL2Option82ExceedMTU,'wwpLeosDhcpRelayAgentL2NoTrustedServerPktDrop':wwpLeosDhcpRelayAgentL2NoTrustedServerPktDrop,'wwpLeosDhcpRelayAgentL2NoTrustedClientPktDrop':wwpLeosDhcpRelayAgentL2NoTrustedClientPktDrop,'wwpLeosDhcpRelayAgentCidStringTable':wwpLeosDhcpRelayAgentCidStringTable,'wwpLeosDhcpRelayAgentCidStringEntry':wwpLeosDhcpRelayAgentCidStringEntry,_Q:wwpLeosDhcpRelayAgentCidStringPort,'wwpLeosDhcpRelayAgentCidString':wwpLeosDhcpRelayAgentCidString,'wwpLeosDhcpRelayAgentCidStringRowStatus':wwpLeosDhcpRelayAgentCidStringRowStatus,'wwpLeosDhcpClientMIBNotificationPrefix':wwpLeosDhcpClientMIBNotificationPrefix,'wwpLeosDhcpClientMIBNotifications':wwpLeosDhcpClientMIBNotifications,'wwpLeosDhcpClientOptionDisabledNotification':wwpLeosDhcpClientOptionDisabledNotification,'wwpLeosDhcpClientMIBConformance':wwpLeosDhcpClientMIBConformance,'wwpLeosDhcpClientMIBCompliances':wwpLeosDhcpClientMIBCompliances,'wwpLeosDhcpClientMIBGroups':wwpLeosDhcpClientMIBGroups})