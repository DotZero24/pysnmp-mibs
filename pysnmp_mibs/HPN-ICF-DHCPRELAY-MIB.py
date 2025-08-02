_S='replace'
_R='hpnicfDHCPRSecurityClientIpAddr'
_Q='hpnicfDHCPRSecurityClientIpAddrType'
_P='hpnicfDHCPRIpToGroupServerIp'
_O='hpnicfDHCPRIpToGroupServerIpType'
_N='hpnicfDHCPRIpToGroupGroupId'
_M='OctetString'
_L='disabled'
_K='enabled'
_J='read-create'
_I='InetAddress'
_H='not-accessible'
_G='ifIndex'
_F='IF-MIB'
_E='HPN-ICF-DHCPRELAY-MIB'
_D='read-only'
_C='Integer32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_M,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hpnicfCommon,=mibBuilder.importSymbols('HPN-ICF-OID-MIB','hpnicfCommon')
ifIndex,=mibBuilder.importSymbols(_F,_G)
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB',_I,'InetAddressType')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention','TruthValue')
hpnicfDhcpRelay=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,15,2,58))
if mibBuilder.loadTexts:hpnicfDhcpRelay.setRevisions(('2005-06-08 00:00',))
_HpnicfDHCPRMibObject_ObjectIdentity=ObjectIdentity
hpnicfDHCPRMibObject=_HpnicfDHCPRMibObject_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,58,1))
_HpnicfDHCPRIfSelectTable_Object=MibTable
hpnicfDHCPRIfSelectTable=_HpnicfDHCPRIfSelectTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,58,1,1))
if mibBuilder.loadTexts:hpnicfDHCPRIfSelectTable.setStatus(_A)
_HpnicfDHCPRIfSelectEntry_Object=MibTableRow
hpnicfDHCPRIfSelectEntry=_HpnicfDHCPRIfSelectEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,58,1,1,1))
hpnicfDHCPRIfSelectEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:hpnicfDHCPRIfSelectEntry.setStatus(_A)
class _HpnicfDHCPRIfSelectRelayMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('on',1),('off',2)))
_HpnicfDHCPRIfSelectRelayMode_Type.__name__=_C
_HpnicfDHCPRIfSelectRelayMode_Object=MibTableColumn
hpnicfDHCPRIfSelectRelayMode=_HpnicfDHCPRIfSelectRelayMode_Object((1,3,6,1,4,1,11,2,14,11,15,2,58,1,1,1,1),_HpnicfDHCPRIfSelectRelayMode_Type())
hpnicfDHCPRIfSelectRelayMode.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDHCPRIfSelectRelayMode.setStatus(_A)
_HpnicfDHCPRIpToGroupTable_Object=MibTable
hpnicfDHCPRIpToGroupTable=_HpnicfDHCPRIpToGroupTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,58,1,2))
if mibBuilder.loadTexts:hpnicfDHCPRIpToGroupTable.setStatus(_A)
_HpnicfDHCPRIpToGroupEntry_Object=MibTableRow
hpnicfDHCPRIpToGroupEntry=_HpnicfDHCPRIpToGroupEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,58,1,2,1))
hpnicfDHCPRIpToGroupEntry.setIndexNames((0,_E,_N),(0,_E,_O),(0,_E,_P))
if mibBuilder.loadTexts:hpnicfDHCPRIpToGroupEntry.setStatus(_A)
class _HpnicfDHCPRIpToGroupGroupId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,19))
_HpnicfDHCPRIpToGroupGroupId_Type.__name__=_C
_HpnicfDHCPRIpToGroupGroupId_Object=MibTableColumn
hpnicfDHCPRIpToGroupGroupId=_HpnicfDHCPRIpToGroupGroupId_Object((1,3,6,1,4,1,11,2,14,11,15,2,58,1,2,1,1),_HpnicfDHCPRIpToGroupGroupId_Type())
hpnicfDHCPRIpToGroupGroupId.setMaxAccess(_H)
if mibBuilder.loadTexts:hpnicfDHCPRIpToGroupGroupId.setStatus(_A)
_HpnicfDHCPRIpToGroupServerIpType_Type=InetAddressType
_HpnicfDHCPRIpToGroupServerIpType_Object=MibTableColumn
hpnicfDHCPRIpToGroupServerIpType=_HpnicfDHCPRIpToGroupServerIpType_Object((1,3,6,1,4,1,11,2,14,11,15,2,58,1,2,1,2),_HpnicfDHCPRIpToGroupServerIpType_Type())
hpnicfDHCPRIpToGroupServerIpType.setMaxAccess(_H)
if mibBuilder.loadTexts:hpnicfDHCPRIpToGroupServerIpType.setStatus(_A)
class _HpnicfDHCPRIpToGroupServerIp_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_HpnicfDHCPRIpToGroupServerIp_Type.__name__=_I
_HpnicfDHCPRIpToGroupServerIp_Object=MibTableColumn
hpnicfDHCPRIpToGroupServerIp=_HpnicfDHCPRIpToGroupServerIp_Object((1,3,6,1,4,1,11,2,14,11,15,2,58,1,2,1,3),_HpnicfDHCPRIpToGroupServerIp_Type())
hpnicfDHCPRIpToGroupServerIp.setMaxAccess(_H)
if mibBuilder.loadTexts:hpnicfDHCPRIpToGroupServerIp.setStatus(_A)
_HpnicfDHCPRIpToGroupRowStatus_Type=RowStatus
_HpnicfDHCPRIpToGroupRowStatus_Object=MibTableColumn
hpnicfDHCPRIpToGroupRowStatus=_HpnicfDHCPRIpToGroupRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,58,1,2,1,4),_HpnicfDHCPRIpToGroupRowStatus_Type())
hpnicfDHCPRIpToGroupRowStatus.setMaxAccess(_J)
if mibBuilder.loadTexts:hpnicfDHCPRIpToGroupRowStatus.setStatus(_A)
_HpnicfDHCPRIfToGroupTable_Object=MibTable
hpnicfDHCPRIfToGroupTable=_HpnicfDHCPRIfToGroupTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,58,1,3))
if mibBuilder.loadTexts:hpnicfDHCPRIfToGroupTable.setStatus(_A)
_HpnicfDHCPRIfToGroupEntry_Object=MibTableRow
hpnicfDHCPRIfToGroupEntry=_HpnicfDHCPRIfToGroupEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,58,1,3,1))
hpnicfDHCPRIfToGroupEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:hpnicfDHCPRIfToGroupEntry.setStatus(_A)
class _HpnicfDHCPRIfToGroupGroupId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,19))
_HpnicfDHCPRIfToGroupGroupId_Type.__name__=_C
_HpnicfDHCPRIfToGroupGroupId_Object=MibTableColumn
hpnicfDHCPRIfToGroupGroupId=_HpnicfDHCPRIfToGroupGroupId_Object((1,3,6,1,4,1,11,2,14,11,15,2,58,1,3,1,1),_HpnicfDHCPRIfToGroupGroupId_Type())
hpnicfDHCPRIfToGroupGroupId.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDHCPRIfToGroupGroupId.setStatus(_A)
_HpnicfDHCPRIfToGroupRowStatus_Type=RowStatus
_HpnicfDHCPRIfToGroupRowStatus_Object=MibTableColumn
hpnicfDHCPRIfToGroupRowStatus=_HpnicfDHCPRIfToGroupRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,58,1,3,1,2),_HpnicfDHCPRIfToGroupRowStatus_Type())
hpnicfDHCPRIfToGroupRowStatus.setMaxAccess(_J)
if mibBuilder.loadTexts:hpnicfDHCPRIfToGroupRowStatus.setStatus(_A)
_HpnicfDHCPRAddrCheckTable_Object=MibTable
hpnicfDHCPRAddrCheckTable=_HpnicfDHCPRAddrCheckTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,58,1,4))
if mibBuilder.loadTexts:hpnicfDHCPRAddrCheckTable.setStatus(_A)
_HpnicfDHCPRAddrCheckEntry_Object=MibTableRow
hpnicfDHCPRAddrCheckEntry=_HpnicfDHCPRAddrCheckEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,58,1,4,1))
hpnicfDHCPRAddrCheckEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:hpnicfDHCPRAddrCheckEntry.setStatus(_A)
class _HpnicfDHCPRAddrCheckSwitch_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_L,2)))
_HpnicfDHCPRAddrCheckSwitch_Type.__name__=_C
_HpnicfDHCPRAddrCheckSwitch_Object=MibTableColumn
hpnicfDHCPRAddrCheckSwitch=_HpnicfDHCPRAddrCheckSwitch_Object((1,3,6,1,4,1,11,2,14,11,15,2,58,1,4,1,1),_HpnicfDHCPRAddrCheckSwitch_Type())
hpnicfDHCPRAddrCheckSwitch.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDHCPRAddrCheckSwitch.setStatus(_A)
_HpnicfDHCPRSecurityTable_Object=MibTable
hpnicfDHCPRSecurityTable=_HpnicfDHCPRSecurityTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,58,1,5))
if mibBuilder.loadTexts:hpnicfDHCPRSecurityTable.setStatus(_A)
_HpnicfDHCPRSecurityEntry_Object=MibTableRow
hpnicfDHCPRSecurityEntry=_HpnicfDHCPRSecurityEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,58,1,5,1))
hpnicfDHCPRSecurityEntry.setIndexNames((0,_E,_Q),(0,_E,_R))
if mibBuilder.loadTexts:hpnicfDHCPRSecurityEntry.setStatus(_A)
_HpnicfDHCPRSecurityClientIpAddrType_Type=InetAddressType
_HpnicfDHCPRSecurityClientIpAddrType_Object=MibTableColumn
hpnicfDHCPRSecurityClientIpAddrType=_HpnicfDHCPRSecurityClientIpAddrType_Object((1,3,6,1,4,1,11,2,14,11,15,2,58,1,5,1,1),_HpnicfDHCPRSecurityClientIpAddrType_Type())
hpnicfDHCPRSecurityClientIpAddrType.setMaxAccess(_H)
if mibBuilder.loadTexts:hpnicfDHCPRSecurityClientIpAddrType.setStatus(_A)
class _HpnicfDHCPRSecurityClientIpAddr_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_HpnicfDHCPRSecurityClientIpAddr_Type.__name__=_I
_HpnicfDHCPRSecurityClientIpAddr_Object=MibTableColumn
hpnicfDHCPRSecurityClientIpAddr=_HpnicfDHCPRSecurityClientIpAddr_Object((1,3,6,1,4,1,11,2,14,11,15,2,58,1,5,1,2),_HpnicfDHCPRSecurityClientIpAddr_Type())
hpnicfDHCPRSecurityClientIpAddr.setMaxAccess(_H)
if mibBuilder.loadTexts:hpnicfDHCPRSecurityClientIpAddr.setStatus(_A)
_HpnicfDHCPRSecurityClientMacAddr_Type=MacAddress
_HpnicfDHCPRSecurityClientMacAddr_Object=MibTableColumn
hpnicfDHCPRSecurityClientMacAddr=_HpnicfDHCPRSecurityClientMacAddr_Object((1,3,6,1,4,1,11,2,14,11,15,2,58,1,5,1,3),_HpnicfDHCPRSecurityClientMacAddr_Type())
hpnicfDHCPRSecurityClientMacAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDHCPRSecurityClientMacAddr.setStatus(_A)
class _HpnicfDHCPRSecurityClientProperty_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('static',1),('dynamic',2)))
_HpnicfDHCPRSecurityClientProperty_Type.__name__=_C
_HpnicfDHCPRSecurityClientProperty_Object=MibTableColumn
hpnicfDHCPRSecurityClientProperty=_HpnicfDHCPRSecurityClientProperty_Object((1,3,6,1,4,1,11,2,14,11,15,2,58,1,5,1,4),_HpnicfDHCPRSecurityClientProperty_Type())
hpnicfDHCPRSecurityClientProperty.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDHCPRSecurityClientProperty.setStatus(_A)
_HpnicfDHCPRSecurityClientRowStatus_Type=RowStatus
_HpnicfDHCPRSecurityClientRowStatus_Object=MibTableColumn
hpnicfDHCPRSecurityClientRowStatus=_HpnicfDHCPRSecurityClientRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,58,1,5,1,5),_HpnicfDHCPRSecurityClientRowStatus_Type())
hpnicfDHCPRSecurityClientRowStatus.setMaxAccess(_J)
if mibBuilder.loadTexts:hpnicfDHCPRSecurityClientRowStatus.setStatus(_A)
_HpnicfDHCPRStatisticsGroup_ObjectIdentity=ObjectIdentity
hpnicfDHCPRStatisticsGroup=_HpnicfDHCPRStatisticsGroup_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,58,1,6))
_HpnicfDHCPRRxClientPktNum_Type=Unsigned32
_HpnicfDHCPRRxClientPktNum_Object=MibScalar
hpnicfDHCPRRxClientPktNum=_HpnicfDHCPRRxClientPktNum_Object((1,3,6,1,4,1,11,2,14,11,15,2,58,1,6,1),_HpnicfDHCPRRxClientPktNum_Type())
hpnicfDHCPRRxClientPktNum.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfDHCPRRxClientPktNum.setStatus(_A)
_HpnicfDHCPRTxClientPktNum_Type=Unsigned32
_HpnicfDHCPRTxClientPktNum_Object=MibScalar
hpnicfDHCPRTxClientPktNum=_HpnicfDHCPRTxClientPktNum_Object((1,3,6,1,4,1,11,2,14,11,15,2,58,1,6,2),_HpnicfDHCPRTxClientPktNum_Type())
hpnicfDHCPRTxClientPktNum.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfDHCPRTxClientPktNum.setStatus(_A)
_HpnicfDHCPRRxServerPktNum_Type=Unsigned32
_HpnicfDHCPRRxServerPktNum_Object=MibScalar
hpnicfDHCPRRxServerPktNum=_HpnicfDHCPRRxServerPktNum_Object((1,3,6,1,4,1,11,2,14,11,15,2,58,1,6,3),_HpnicfDHCPRRxServerPktNum_Type())
hpnicfDHCPRRxServerPktNum.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfDHCPRRxServerPktNum.setStatus(_A)
_HpnicfDHCPRTxServerPktNum_Type=Unsigned32
_HpnicfDHCPRTxServerPktNum_Object=MibScalar
hpnicfDHCPRTxServerPktNum=_HpnicfDHCPRTxServerPktNum_Object((1,3,6,1,4,1,11,2,14,11,15,2,58,1,6,4),_HpnicfDHCPRTxServerPktNum_Type())
hpnicfDHCPRTxServerPktNum.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfDHCPRTxServerPktNum.setStatus(_A)
_HpnicfDHCPRDiscoverPktNum_Type=Unsigned32
_HpnicfDHCPRDiscoverPktNum_Object=MibScalar
hpnicfDHCPRDiscoverPktNum=_HpnicfDHCPRDiscoverPktNum_Object((1,3,6,1,4,1,11,2,14,11,15,2,58,1,6,5),_HpnicfDHCPRDiscoverPktNum_Type())
hpnicfDHCPRDiscoverPktNum.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfDHCPRDiscoverPktNum.setStatus(_A)
_HpnicfDHCPRRequestPktNum_Type=Unsigned32
_HpnicfDHCPRRequestPktNum_Object=MibScalar
hpnicfDHCPRRequestPktNum=_HpnicfDHCPRRequestPktNum_Object((1,3,6,1,4,1,11,2,14,11,15,2,58,1,6,6),_HpnicfDHCPRRequestPktNum_Type())
hpnicfDHCPRRequestPktNum.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfDHCPRRequestPktNum.setStatus(_A)
_HpnicfDHCPRDeclinePktNum_Type=Unsigned32
_HpnicfDHCPRDeclinePktNum_Object=MibScalar
hpnicfDHCPRDeclinePktNum=_HpnicfDHCPRDeclinePktNum_Object((1,3,6,1,4,1,11,2,14,11,15,2,58,1,6,7),_HpnicfDHCPRDeclinePktNum_Type())
hpnicfDHCPRDeclinePktNum.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfDHCPRDeclinePktNum.setStatus(_A)
_HpnicfDHCPRReleasePktNum_Type=Unsigned32
_HpnicfDHCPRReleasePktNum_Object=MibScalar
hpnicfDHCPRReleasePktNum=_HpnicfDHCPRReleasePktNum_Object((1,3,6,1,4,1,11,2,14,11,15,2,58,1,6,8),_HpnicfDHCPRReleasePktNum_Type())
hpnicfDHCPRReleasePktNum.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfDHCPRReleasePktNum.setStatus(_A)
_HpnicfDHCPRInformPktNum_Type=Unsigned32
_HpnicfDHCPRInformPktNum_Object=MibScalar
hpnicfDHCPRInformPktNum=_HpnicfDHCPRInformPktNum_Object((1,3,6,1,4,1,11,2,14,11,15,2,58,1,6,9),_HpnicfDHCPRInformPktNum_Type())
hpnicfDHCPRInformPktNum.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfDHCPRInformPktNum.setStatus(_A)
_HpnicfDHCPROfferPktNum_Type=Unsigned32
_HpnicfDHCPROfferPktNum_Object=MibScalar
hpnicfDHCPROfferPktNum=_HpnicfDHCPROfferPktNum_Object((1,3,6,1,4,1,11,2,14,11,15,2,58,1,6,10),_HpnicfDHCPROfferPktNum_Type())
hpnicfDHCPROfferPktNum.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfDHCPROfferPktNum.setStatus(_A)
_HpnicfDHCPRAckPktNum_Type=Unsigned32
_HpnicfDHCPRAckPktNum_Object=MibScalar
hpnicfDHCPRAckPktNum=_HpnicfDHCPRAckPktNum_Object((1,3,6,1,4,1,11,2,14,11,15,2,58,1,6,11),_HpnicfDHCPRAckPktNum_Type())
hpnicfDHCPRAckPktNum.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfDHCPRAckPktNum.setStatus(_A)
_HpnicfDHCPRNakPktNum_Type=Unsigned32
_HpnicfDHCPRNakPktNum_Object=MibScalar
hpnicfDHCPRNakPktNum=_HpnicfDHCPRNakPktNum_Object((1,3,6,1,4,1,11,2,14,11,15,2,58,1,6,12),_HpnicfDHCPRNakPktNum_Type())
hpnicfDHCPRNakPktNum.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfDHCPRNakPktNum.setStatus(_A)
_HpnicfDHCPRStatisticsReset_Type=TruthValue
_HpnicfDHCPRStatisticsReset_Object=MibScalar
hpnicfDHCPRStatisticsReset=_HpnicfDHCPRStatisticsReset_Object((1,3,6,1,4,1,11,2,14,11,15,2,58,1,6,13),_HpnicfDHCPRStatisticsReset_Type())
hpnicfDHCPRStatisticsReset.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDHCPRStatisticsReset.setStatus(_A)
_HpnicfDHCPRCycleGroup_ObjectIdentity=ObjectIdentity
hpnicfDHCPRCycleGroup=_HpnicfDHCPRCycleGroup_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,58,1,7))
class _HpnicfDHCPRCycleStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('on',1),('off',2)))
_HpnicfDHCPRCycleStatus_Type.__name__=_C
_HpnicfDHCPRCycleStatus_Object=MibScalar
hpnicfDHCPRCycleStatus=_HpnicfDHCPRCycleStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,58,1,7,1),_HpnicfDHCPRCycleStatus_Type())
hpnicfDHCPRCycleStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDHCPRCycleStatus.setStatus(_A)
_HpnicfDHCPRConfigOption82Group_ObjectIdentity=ObjectIdentity
hpnicfDHCPRConfigOption82Group=_HpnicfDHCPRConfigOption82Group_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,58,1,8))
class _HpnicfDHCPROption82Switch_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_L,2)))
_HpnicfDHCPROption82Switch_Type.__name__=_C
_HpnicfDHCPROption82Switch_Object=MibScalar
hpnicfDHCPROption82Switch=_HpnicfDHCPROption82Switch_Object((1,3,6,1,4,1,11,2,14,11,15,2,58,1,8,1),_HpnicfDHCPROption82Switch_Type())
hpnicfDHCPROption82Switch.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDHCPROption82Switch.setStatus(_A)
class _HpnicfDHCPROption82HandleStrategy_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('drop',1),('keep',2),(_S,3)))
_HpnicfDHCPROption82HandleStrategy_Type.__name__=_C
_HpnicfDHCPROption82HandleStrategy_Object=MibScalar
hpnicfDHCPROption82HandleStrategy=_HpnicfDHCPROption82HandleStrategy_Object((1,3,6,1,4,1,11,2,14,11,15,2,58,1,8,2),_HpnicfDHCPROption82HandleStrategy_Type())
hpnicfDHCPROption82HandleStrategy.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDHCPROption82HandleStrategy.setStatus(_A)
_HpnicfDHCPRConfigOption82IfTable_Object=MibTable
hpnicfDHCPRConfigOption82IfTable=_HpnicfDHCPRConfigOption82IfTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,58,1,8,3))
if mibBuilder.loadTexts:hpnicfDHCPRConfigOption82IfTable.setStatus(_A)
_HpnicfDHCPRConfigOption82IfEntry_Object=MibTableRow
hpnicfDHCPRConfigOption82IfEntry=_HpnicfDHCPRConfigOption82IfEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,58,1,8,3,1))
hpnicfDHCPRConfigOption82IfEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:hpnicfDHCPRConfigOption82IfEntry.setStatus(_A)
class _HpnicfDHCPROption82IfSwitch_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_L,2)))
_HpnicfDHCPROption82IfSwitch_Type.__name__=_C
_HpnicfDHCPROption82IfSwitch_Object=MibTableColumn
hpnicfDHCPROption82IfSwitch=_HpnicfDHCPROption82IfSwitch_Object((1,3,6,1,4,1,11,2,14,11,15,2,58,1,8,3,1,1),_HpnicfDHCPROption82IfSwitch_Type())
hpnicfDHCPROption82IfSwitch.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDHCPROption82IfSwitch.setStatus(_A)
class _HpnicfDHCPROption82IfStrategy_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('drop',1),('keep',2),(_S,3)))
_HpnicfDHCPROption82IfStrategy_Type.__name__=_C
_HpnicfDHCPROption82IfStrategy_Object=MibTableColumn
hpnicfDHCPROption82IfStrategy=_HpnicfDHCPROption82IfStrategy_Object((1,3,6,1,4,1,11,2,14,11,15,2,58,1,8,3,1,2),_HpnicfDHCPROption82IfStrategy_Type())
hpnicfDHCPROption82IfStrategy.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDHCPROption82IfStrategy.setStatus(_A)
class _HpnicfDHCPROption82IfFormat_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('normal',1),('verbose',2)))
_HpnicfDHCPROption82IfFormat_Type.__name__=_C
_HpnicfDHCPROption82IfFormat_Object=MibTableColumn
hpnicfDHCPROption82IfFormat=_HpnicfDHCPROption82IfFormat_Object((1,3,6,1,4,1,11,2,14,11,15,2,58,1,8,3,1,3),_HpnicfDHCPROption82IfFormat_Type())
hpnicfDHCPROption82IfFormat.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDHCPROption82IfFormat.setStatus(_A)
class _HpnicfDHCPROption82IfNodeType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('invalid',1),('mac',2),('sysname',3),('userdefine',4)))
_HpnicfDHCPROption82IfNodeType_Type.__name__=_C
_HpnicfDHCPROption82IfNodeType_Object=MibTableColumn
hpnicfDHCPROption82IfNodeType=_HpnicfDHCPROption82IfNodeType_Object((1,3,6,1,4,1,11,2,14,11,15,2,58,1,8,3,1,4),_HpnicfDHCPROption82IfNodeType_Type())
hpnicfDHCPROption82IfNodeType.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDHCPROption82IfNodeType.setStatus(_A)
class _HpnicfDHCPROption82IfUsrDefString_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
_HpnicfDHCPROption82IfUsrDefString_Type.__name__=_M
_HpnicfDHCPROption82IfUsrDefString_Object=MibTableColumn
hpnicfDHCPROption82IfUsrDefString=_HpnicfDHCPROption82IfUsrDefString_Object((1,3,6,1,4,1,11,2,14,11,15,2,58,1,8,3,1,5),_HpnicfDHCPROption82IfUsrDefString_Type())
hpnicfDHCPROption82IfUsrDefString.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDHCPROption82IfUsrDefString.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'hpnicfDhcpRelay':hpnicfDhcpRelay,'hpnicfDHCPRMibObject':hpnicfDHCPRMibObject,'hpnicfDHCPRIfSelectTable':hpnicfDHCPRIfSelectTable,'hpnicfDHCPRIfSelectEntry':hpnicfDHCPRIfSelectEntry,'hpnicfDHCPRIfSelectRelayMode':hpnicfDHCPRIfSelectRelayMode,'hpnicfDHCPRIpToGroupTable':hpnicfDHCPRIpToGroupTable,'hpnicfDHCPRIpToGroupEntry':hpnicfDHCPRIpToGroupEntry,_N:hpnicfDHCPRIpToGroupGroupId,_O:hpnicfDHCPRIpToGroupServerIpType,_P:hpnicfDHCPRIpToGroupServerIp,'hpnicfDHCPRIpToGroupRowStatus':hpnicfDHCPRIpToGroupRowStatus,'hpnicfDHCPRIfToGroupTable':hpnicfDHCPRIfToGroupTable,'hpnicfDHCPRIfToGroupEntry':hpnicfDHCPRIfToGroupEntry,'hpnicfDHCPRIfToGroupGroupId':hpnicfDHCPRIfToGroupGroupId,'hpnicfDHCPRIfToGroupRowStatus':hpnicfDHCPRIfToGroupRowStatus,'hpnicfDHCPRAddrCheckTable':hpnicfDHCPRAddrCheckTable,'hpnicfDHCPRAddrCheckEntry':hpnicfDHCPRAddrCheckEntry,'hpnicfDHCPRAddrCheckSwitch':hpnicfDHCPRAddrCheckSwitch,'hpnicfDHCPRSecurityTable':hpnicfDHCPRSecurityTable,'hpnicfDHCPRSecurityEntry':hpnicfDHCPRSecurityEntry,_Q:hpnicfDHCPRSecurityClientIpAddrType,_R:hpnicfDHCPRSecurityClientIpAddr,'hpnicfDHCPRSecurityClientMacAddr':hpnicfDHCPRSecurityClientMacAddr,'hpnicfDHCPRSecurityClientProperty':hpnicfDHCPRSecurityClientProperty,'hpnicfDHCPRSecurityClientRowStatus':hpnicfDHCPRSecurityClientRowStatus,'hpnicfDHCPRStatisticsGroup':hpnicfDHCPRStatisticsGroup,'hpnicfDHCPRRxClientPktNum':hpnicfDHCPRRxClientPktNum,'hpnicfDHCPRTxClientPktNum':hpnicfDHCPRTxClientPktNum,'hpnicfDHCPRRxServerPktNum':hpnicfDHCPRRxServerPktNum,'hpnicfDHCPRTxServerPktNum':hpnicfDHCPRTxServerPktNum,'hpnicfDHCPRDiscoverPktNum':hpnicfDHCPRDiscoverPktNum,'hpnicfDHCPRRequestPktNum':hpnicfDHCPRRequestPktNum,'hpnicfDHCPRDeclinePktNum':hpnicfDHCPRDeclinePktNum,'hpnicfDHCPRReleasePktNum':hpnicfDHCPRReleasePktNum,'hpnicfDHCPRInformPktNum':hpnicfDHCPRInformPktNum,'hpnicfDHCPROfferPktNum':hpnicfDHCPROfferPktNum,'hpnicfDHCPRAckPktNum':hpnicfDHCPRAckPktNum,'hpnicfDHCPRNakPktNum':hpnicfDHCPRNakPktNum,'hpnicfDHCPRStatisticsReset':hpnicfDHCPRStatisticsReset,'hpnicfDHCPRCycleGroup':hpnicfDHCPRCycleGroup,'hpnicfDHCPRCycleStatus':hpnicfDHCPRCycleStatus,'hpnicfDHCPRConfigOption82Group':hpnicfDHCPRConfigOption82Group,'hpnicfDHCPROption82Switch':hpnicfDHCPROption82Switch,'hpnicfDHCPROption82HandleStrategy':hpnicfDHCPROption82HandleStrategy,'hpnicfDHCPRConfigOption82IfTable':hpnicfDHCPRConfigOption82IfTable,'hpnicfDHCPRConfigOption82IfEntry':hpnicfDHCPRConfigOption82IfEntry,'hpnicfDHCPROption82IfSwitch':hpnicfDHCPROption82IfSwitch,'hpnicfDHCPROption82IfStrategy':hpnicfDHCPROption82IfStrategy,'hpnicfDHCPROption82IfFormat':hpnicfDHCPROption82IfFormat,'hpnicfDHCPROption82IfNodeType':hpnicfDHCPROption82IfNodeType,'hpnicfDHCPROption82IfUsrDefString':hpnicfDHCPROption82IfUsrDefString})