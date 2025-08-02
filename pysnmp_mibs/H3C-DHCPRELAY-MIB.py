_S='replace'
_R='h3cDHCPRSecurityClientIpAddr'
_Q='h3cDHCPRSecurityClientIpAddrType'
_P='h3cDHCPRIpToGroupServerIp'
_O='h3cDHCPRIpToGroupServerIpType'
_N='h3cDHCPRIpToGroupGroupId'
_M='OctetString'
_L='disabled'
_K='enabled'
_J='read-create'
_I='InetAddress'
_H='not-accessible'
_G='ifIndex'
_F='IF-MIB'
_E='H3C-DHCPRELAY-MIB'
_D='read-only'
_C='Integer32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_M,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
h3cCommon,=mibBuilder.importSymbols('HUAWEI-3COM-OID-MIB','h3cCommon')
ifIndex,=mibBuilder.importSymbols(_F,_G)
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB',_I,'InetAddressType')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention','TruthValue')
h3cDhcpRelay=ModuleIdentity((1,3,6,1,4,1,2011,10,2,58))
if mibBuilder.loadTexts:h3cDhcpRelay.setRevisions(('2005-06-08 00:00',))
_H3cDHCPRMibObject_ObjectIdentity=ObjectIdentity
h3cDHCPRMibObject=_H3cDHCPRMibObject_ObjectIdentity((1,3,6,1,4,1,2011,10,2,58,1))
_H3cDHCPRIfSelectTable_Object=MibTable
h3cDHCPRIfSelectTable=_H3cDHCPRIfSelectTable_Object((1,3,6,1,4,1,2011,10,2,58,1,1))
if mibBuilder.loadTexts:h3cDHCPRIfSelectTable.setStatus(_A)
_H3cDHCPRIfSelectEntry_Object=MibTableRow
h3cDHCPRIfSelectEntry=_H3cDHCPRIfSelectEntry_Object((1,3,6,1,4,1,2011,10,2,58,1,1,1))
h3cDHCPRIfSelectEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:h3cDHCPRIfSelectEntry.setStatus(_A)
class _H3cDHCPRIfSelectRelayMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('on',1),('off',2)))
_H3cDHCPRIfSelectRelayMode_Type.__name__=_C
_H3cDHCPRIfSelectRelayMode_Object=MibTableColumn
h3cDHCPRIfSelectRelayMode=_H3cDHCPRIfSelectRelayMode_Object((1,3,6,1,4,1,2011,10,2,58,1,1,1,1),_H3cDHCPRIfSelectRelayMode_Type())
h3cDHCPRIfSelectRelayMode.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDHCPRIfSelectRelayMode.setStatus(_A)
_H3cDHCPRIpToGroupTable_Object=MibTable
h3cDHCPRIpToGroupTable=_H3cDHCPRIpToGroupTable_Object((1,3,6,1,4,1,2011,10,2,58,1,2))
if mibBuilder.loadTexts:h3cDHCPRIpToGroupTable.setStatus(_A)
_H3cDHCPRIpToGroupEntry_Object=MibTableRow
h3cDHCPRIpToGroupEntry=_H3cDHCPRIpToGroupEntry_Object((1,3,6,1,4,1,2011,10,2,58,1,2,1))
h3cDHCPRIpToGroupEntry.setIndexNames((0,_E,_N),(0,_E,_O),(0,_E,_P))
if mibBuilder.loadTexts:h3cDHCPRIpToGroupEntry.setStatus(_A)
class _H3cDHCPRIpToGroupGroupId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,19))
_H3cDHCPRIpToGroupGroupId_Type.__name__=_C
_H3cDHCPRIpToGroupGroupId_Object=MibTableColumn
h3cDHCPRIpToGroupGroupId=_H3cDHCPRIpToGroupGroupId_Object((1,3,6,1,4,1,2011,10,2,58,1,2,1,1),_H3cDHCPRIpToGroupGroupId_Type())
h3cDHCPRIpToGroupGroupId.setMaxAccess(_H)
if mibBuilder.loadTexts:h3cDHCPRIpToGroupGroupId.setStatus(_A)
_H3cDHCPRIpToGroupServerIpType_Type=InetAddressType
_H3cDHCPRIpToGroupServerIpType_Object=MibTableColumn
h3cDHCPRIpToGroupServerIpType=_H3cDHCPRIpToGroupServerIpType_Object((1,3,6,1,4,1,2011,10,2,58,1,2,1,2),_H3cDHCPRIpToGroupServerIpType_Type())
h3cDHCPRIpToGroupServerIpType.setMaxAccess(_H)
if mibBuilder.loadTexts:h3cDHCPRIpToGroupServerIpType.setStatus(_A)
class _H3cDHCPRIpToGroupServerIp_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_H3cDHCPRIpToGroupServerIp_Type.__name__=_I
_H3cDHCPRIpToGroupServerIp_Object=MibTableColumn
h3cDHCPRIpToGroupServerIp=_H3cDHCPRIpToGroupServerIp_Object((1,3,6,1,4,1,2011,10,2,58,1,2,1,3),_H3cDHCPRIpToGroupServerIp_Type())
h3cDHCPRIpToGroupServerIp.setMaxAccess(_H)
if mibBuilder.loadTexts:h3cDHCPRIpToGroupServerIp.setStatus(_A)
_H3cDHCPRIpToGroupRowStatus_Type=RowStatus
_H3cDHCPRIpToGroupRowStatus_Object=MibTableColumn
h3cDHCPRIpToGroupRowStatus=_H3cDHCPRIpToGroupRowStatus_Object((1,3,6,1,4,1,2011,10,2,58,1,2,1,4),_H3cDHCPRIpToGroupRowStatus_Type())
h3cDHCPRIpToGroupRowStatus.setMaxAccess(_J)
if mibBuilder.loadTexts:h3cDHCPRIpToGroupRowStatus.setStatus(_A)
_H3cDHCPRIfToGroupTable_Object=MibTable
h3cDHCPRIfToGroupTable=_H3cDHCPRIfToGroupTable_Object((1,3,6,1,4,1,2011,10,2,58,1,3))
if mibBuilder.loadTexts:h3cDHCPRIfToGroupTable.setStatus(_A)
_H3cDHCPRIfToGroupEntry_Object=MibTableRow
h3cDHCPRIfToGroupEntry=_H3cDHCPRIfToGroupEntry_Object((1,3,6,1,4,1,2011,10,2,58,1,3,1))
h3cDHCPRIfToGroupEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:h3cDHCPRIfToGroupEntry.setStatus(_A)
class _H3cDHCPRIfToGroupGroupId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,19))
_H3cDHCPRIfToGroupGroupId_Type.__name__=_C
_H3cDHCPRIfToGroupGroupId_Object=MibTableColumn
h3cDHCPRIfToGroupGroupId=_H3cDHCPRIfToGroupGroupId_Object((1,3,6,1,4,1,2011,10,2,58,1,3,1,1),_H3cDHCPRIfToGroupGroupId_Type())
h3cDHCPRIfToGroupGroupId.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDHCPRIfToGroupGroupId.setStatus(_A)
_H3cDHCPRIfToGroupRowStatus_Type=RowStatus
_H3cDHCPRIfToGroupRowStatus_Object=MibTableColumn
h3cDHCPRIfToGroupRowStatus=_H3cDHCPRIfToGroupRowStatus_Object((1,3,6,1,4,1,2011,10,2,58,1,3,1,2),_H3cDHCPRIfToGroupRowStatus_Type())
h3cDHCPRIfToGroupRowStatus.setMaxAccess(_J)
if mibBuilder.loadTexts:h3cDHCPRIfToGroupRowStatus.setStatus(_A)
_H3cDHCPRAddrCheckTable_Object=MibTable
h3cDHCPRAddrCheckTable=_H3cDHCPRAddrCheckTable_Object((1,3,6,1,4,1,2011,10,2,58,1,4))
if mibBuilder.loadTexts:h3cDHCPRAddrCheckTable.setStatus(_A)
_H3cDHCPRAddrCheckEntry_Object=MibTableRow
h3cDHCPRAddrCheckEntry=_H3cDHCPRAddrCheckEntry_Object((1,3,6,1,4,1,2011,10,2,58,1,4,1))
h3cDHCPRAddrCheckEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:h3cDHCPRAddrCheckEntry.setStatus(_A)
class _H3cDHCPRAddrCheckSwitch_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_L,2)))
_H3cDHCPRAddrCheckSwitch_Type.__name__=_C
_H3cDHCPRAddrCheckSwitch_Object=MibTableColumn
h3cDHCPRAddrCheckSwitch=_H3cDHCPRAddrCheckSwitch_Object((1,3,6,1,4,1,2011,10,2,58,1,4,1,1),_H3cDHCPRAddrCheckSwitch_Type())
h3cDHCPRAddrCheckSwitch.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDHCPRAddrCheckSwitch.setStatus(_A)
_H3cDHCPRSecurityTable_Object=MibTable
h3cDHCPRSecurityTable=_H3cDHCPRSecurityTable_Object((1,3,6,1,4,1,2011,10,2,58,1,5))
if mibBuilder.loadTexts:h3cDHCPRSecurityTable.setStatus(_A)
_H3cDHCPRSecurityEntry_Object=MibTableRow
h3cDHCPRSecurityEntry=_H3cDHCPRSecurityEntry_Object((1,3,6,1,4,1,2011,10,2,58,1,5,1))
h3cDHCPRSecurityEntry.setIndexNames((0,_E,_Q),(0,_E,_R))
if mibBuilder.loadTexts:h3cDHCPRSecurityEntry.setStatus(_A)
_H3cDHCPRSecurityClientIpAddrType_Type=InetAddressType
_H3cDHCPRSecurityClientIpAddrType_Object=MibTableColumn
h3cDHCPRSecurityClientIpAddrType=_H3cDHCPRSecurityClientIpAddrType_Object((1,3,6,1,4,1,2011,10,2,58,1,5,1,1),_H3cDHCPRSecurityClientIpAddrType_Type())
h3cDHCPRSecurityClientIpAddrType.setMaxAccess(_H)
if mibBuilder.loadTexts:h3cDHCPRSecurityClientIpAddrType.setStatus(_A)
class _H3cDHCPRSecurityClientIpAddr_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_H3cDHCPRSecurityClientIpAddr_Type.__name__=_I
_H3cDHCPRSecurityClientIpAddr_Object=MibTableColumn
h3cDHCPRSecurityClientIpAddr=_H3cDHCPRSecurityClientIpAddr_Object((1,3,6,1,4,1,2011,10,2,58,1,5,1,2),_H3cDHCPRSecurityClientIpAddr_Type())
h3cDHCPRSecurityClientIpAddr.setMaxAccess(_H)
if mibBuilder.loadTexts:h3cDHCPRSecurityClientIpAddr.setStatus(_A)
_H3cDHCPRSecurityClientMacAddr_Type=MacAddress
_H3cDHCPRSecurityClientMacAddr_Object=MibTableColumn
h3cDHCPRSecurityClientMacAddr=_H3cDHCPRSecurityClientMacAddr_Object((1,3,6,1,4,1,2011,10,2,58,1,5,1,3),_H3cDHCPRSecurityClientMacAddr_Type())
h3cDHCPRSecurityClientMacAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDHCPRSecurityClientMacAddr.setStatus(_A)
class _H3cDHCPRSecurityClientProperty_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('static',1),('dynamic',2)))
_H3cDHCPRSecurityClientProperty_Type.__name__=_C
_H3cDHCPRSecurityClientProperty_Object=MibTableColumn
h3cDHCPRSecurityClientProperty=_H3cDHCPRSecurityClientProperty_Object((1,3,6,1,4,1,2011,10,2,58,1,5,1,4),_H3cDHCPRSecurityClientProperty_Type())
h3cDHCPRSecurityClientProperty.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDHCPRSecurityClientProperty.setStatus(_A)
_H3cDHCPRSecurityClientRowStatus_Type=RowStatus
_H3cDHCPRSecurityClientRowStatus_Object=MibTableColumn
h3cDHCPRSecurityClientRowStatus=_H3cDHCPRSecurityClientRowStatus_Object((1,3,6,1,4,1,2011,10,2,58,1,5,1,5),_H3cDHCPRSecurityClientRowStatus_Type())
h3cDHCPRSecurityClientRowStatus.setMaxAccess(_J)
if mibBuilder.loadTexts:h3cDHCPRSecurityClientRowStatus.setStatus(_A)
_H3cDHCPRStatisticsGroup_ObjectIdentity=ObjectIdentity
h3cDHCPRStatisticsGroup=_H3cDHCPRStatisticsGroup_ObjectIdentity((1,3,6,1,4,1,2011,10,2,58,1,6))
_H3cDHCPRRxClientPktNum_Type=Unsigned32
_H3cDHCPRRxClientPktNum_Object=MibScalar
h3cDHCPRRxClientPktNum=_H3cDHCPRRxClientPktNum_Object((1,3,6,1,4,1,2011,10,2,58,1,6,1),_H3cDHCPRRxClientPktNum_Type())
h3cDHCPRRxClientPktNum.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cDHCPRRxClientPktNum.setStatus(_A)
_H3cDHCPRTxClientPktNum_Type=Unsigned32
_H3cDHCPRTxClientPktNum_Object=MibScalar
h3cDHCPRTxClientPktNum=_H3cDHCPRTxClientPktNum_Object((1,3,6,1,4,1,2011,10,2,58,1,6,2),_H3cDHCPRTxClientPktNum_Type())
h3cDHCPRTxClientPktNum.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cDHCPRTxClientPktNum.setStatus(_A)
_H3cDHCPRRxServerPktNum_Type=Unsigned32
_H3cDHCPRRxServerPktNum_Object=MibScalar
h3cDHCPRRxServerPktNum=_H3cDHCPRRxServerPktNum_Object((1,3,6,1,4,1,2011,10,2,58,1,6,3),_H3cDHCPRRxServerPktNum_Type())
h3cDHCPRRxServerPktNum.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cDHCPRRxServerPktNum.setStatus(_A)
_H3cDHCPRTxServerPktNum_Type=Unsigned32
_H3cDHCPRTxServerPktNum_Object=MibScalar
h3cDHCPRTxServerPktNum=_H3cDHCPRTxServerPktNum_Object((1,3,6,1,4,1,2011,10,2,58,1,6,4),_H3cDHCPRTxServerPktNum_Type())
h3cDHCPRTxServerPktNum.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cDHCPRTxServerPktNum.setStatus(_A)
_H3cDHCPRDiscoverPktNum_Type=Unsigned32
_H3cDHCPRDiscoverPktNum_Object=MibScalar
h3cDHCPRDiscoverPktNum=_H3cDHCPRDiscoverPktNum_Object((1,3,6,1,4,1,2011,10,2,58,1,6,5),_H3cDHCPRDiscoverPktNum_Type())
h3cDHCPRDiscoverPktNum.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cDHCPRDiscoverPktNum.setStatus(_A)
_H3cDHCPRRequestPktNum_Type=Unsigned32
_H3cDHCPRRequestPktNum_Object=MibScalar
h3cDHCPRRequestPktNum=_H3cDHCPRRequestPktNum_Object((1,3,6,1,4,1,2011,10,2,58,1,6,6),_H3cDHCPRRequestPktNum_Type())
h3cDHCPRRequestPktNum.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cDHCPRRequestPktNum.setStatus(_A)
_H3cDHCPRDeclinePktNum_Type=Unsigned32
_H3cDHCPRDeclinePktNum_Object=MibScalar
h3cDHCPRDeclinePktNum=_H3cDHCPRDeclinePktNum_Object((1,3,6,1,4,1,2011,10,2,58,1,6,7),_H3cDHCPRDeclinePktNum_Type())
h3cDHCPRDeclinePktNum.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cDHCPRDeclinePktNum.setStatus(_A)
_H3cDHCPRReleasePktNum_Type=Unsigned32
_H3cDHCPRReleasePktNum_Object=MibScalar
h3cDHCPRReleasePktNum=_H3cDHCPRReleasePktNum_Object((1,3,6,1,4,1,2011,10,2,58,1,6,8),_H3cDHCPRReleasePktNum_Type())
h3cDHCPRReleasePktNum.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cDHCPRReleasePktNum.setStatus(_A)
_H3cDHCPRInformPktNum_Type=Unsigned32
_H3cDHCPRInformPktNum_Object=MibScalar
h3cDHCPRInformPktNum=_H3cDHCPRInformPktNum_Object((1,3,6,1,4,1,2011,10,2,58,1,6,9),_H3cDHCPRInformPktNum_Type())
h3cDHCPRInformPktNum.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cDHCPRInformPktNum.setStatus(_A)
_H3cDHCPROfferPktNum_Type=Unsigned32
_H3cDHCPROfferPktNum_Object=MibScalar
h3cDHCPROfferPktNum=_H3cDHCPROfferPktNum_Object((1,3,6,1,4,1,2011,10,2,58,1,6,10),_H3cDHCPROfferPktNum_Type())
h3cDHCPROfferPktNum.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cDHCPROfferPktNum.setStatus(_A)
_H3cDHCPRAckPktNum_Type=Unsigned32
_H3cDHCPRAckPktNum_Object=MibScalar
h3cDHCPRAckPktNum=_H3cDHCPRAckPktNum_Object((1,3,6,1,4,1,2011,10,2,58,1,6,11),_H3cDHCPRAckPktNum_Type())
h3cDHCPRAckPktNum.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cDHCPRAckPktNum.setStatus(_A)
_H3cDHCPRNakPktNum_Type=Unsigned32
_H3cDHCPRNakPktNum_Object=MibScalar
h3cDHCPRNakPktNum=_H3cDHCPRNakPktNum_Object((1,3,6,1,4,1,2011,10,2,58,1,6,12),_H3cDHCPRNakPktNum_Type())
h3cDHCPRNakPktNum.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cDHCPRNakPktNum.setStatus(_A)
_H3cDHCPRStatisticsReset_Type=TruthValue
_H3cDHCPRStatisticsReset_Object=MibScalar
h3cDHCPRStatisticsReset=_H3cDHCPRStatisticsReset_Object((1,3,6,1,4,1,2011,10,2,58,1,6,13),_H3cDHCPRStatisticsReset_Type())
h3cDHCPRStatisticsReset.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDHCPRStatisticsReset.setStatus(_A)
_H3cDHCPRCycleGroup_ObjectIdentity=ObjectIdentity
h3cDHCPRCycleGroup=_H3cDHCPRCycleGroup_ObjectIdentity((1,3,6,1,4,1,2011,10,2,58,1,7))
class _H3cDHCPRCycleStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('on',1),('off',2)))
_H3cDHCPRCycleStatus_Type.__name__=_C
_H3cDHCPRCycleStatus_Object=MibScalar
h3cDHCPRCycleStatus=_H3cDHCPRCycleStatus_Object((1,3,6,1,4,1,2011,10,2,58,1,7,1),_H3cDHCPRCycleStatus_Type())
h3cDHCPRCycleStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDHCPRCycleStatus.setStatus(_A)
_H3cDHCPRConfigOption82Group_ObjectIdentity=ObjectIdentity
h3cDHCPRConfigOption82Group=_H3cDHCPRConfigOption82Group_ObjectIdentity((1,3,6,1,4,1,2011,10,2,58,1,8))
class _H3cDHCPROption82Switch_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_L,2)))
_H3cDHCPROption82Switch_Type.__name__=_C
_H3cDHCPROption82Switch_Object=MibScalar
h3cDHCPROption82Switch=_H3cDHCPROption82Switch_Object((1,3,6,1,4,1,2011,10,2,58,1,8,1),_H3cDHCPROption82Switch_Type())
h3cDHCPROption82Switch.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDHCPROption82Switch.setStatus(_A)
class _H3cDHCPROption82HandleStrategy_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('drop',1),('keep',2),(_S,3)))
_H3cDHCPROption82HandleStrategy_Type.__name__=_C
_H3cDHCPROption82HandleStrategy_Object=MibScalar
h3cDHCPROption82HandleStrategy=_H3cDHCPROption82HandleStrategy_Object((1,3,6,1,4,1,2011,10,2,58,1,8,2),_H3cDHCPROption82HandleStrategy_Type())
h3cDHCPROption82HandleStrategy.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDHCPROption82HandleStrategy.setStatus(_A)
_H3cDHCPRConfigOption82IfTable_Object=MibTable
h3cDHCPRConfigOption82IfTable=_H3cDHCPRConfigOption82IfTable_Object((1,3,6,1,4,1,2011,10,2,58,1,8,3))
if mibBuilder.loadTexts:h3cDHCPRConfigOption82IfTable.setStatus(_A)
_H3cDHCPRConfigOption82IfEntry_Object=MibTableRow
h3cDHCPRConfigOption82IfEntry=_H3cDHCPRConfigOption82IfEntry_Object((1,3,6,1,4,1,2011,10,2,58,1,8,3,1))
h3cDHCPRConfigOption82IfEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:h3cDHCPRConfigOption82IfEntry.setStatus(_A)
class _H3cDHCPROption82IfSwitch_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_L,2)))
_H3cDHCPROption82IfSwitch_Type.__name__=_C
_H3cDHCPROption82IfSwitch_Object=MibTableColumn
h3cDHCPROption82IfSwitch=_H3cDHCPROption82IfSwitch_Object((1,3,6,1,4,1,2011,10,2,58,1,8,3,1,1),_H3cDHCPROption82IfSwitch_Type())
h3cDHCPROption82IfSwitch.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDHCPROption82IfSwitch.setStatus(_A)
class _H3cDHCPROption82IfStrategy_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('drop',1),('keep',2),(_S,3)))
_H3cDHCPROption82IfStrategy_Type.__name__=_C
_H3cDHCPROption82IfStrategy_Object=MibTableColumn
h3cDHCPROption82IfStrategy=_H3cDHCPROption82IfStrategy_Object((1,3,6,1,4,1,2011,10,2,58,1,8,3,1,2),_H3cDHCPROption82IfStrategy_Type())
h3cDHCPROption82IfStrategy.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDHCPROption82IfStrategy.setStatus(_A)
class _H3cDHCPROption82IfFormat_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('normal',1),('verbose',2)))
_H3cDHCPROption82IfFormat_Type.__name__=_C
_H3cDHCPROption82IfFormat_Object=MibTableColumn
h3cDHCPROption82IfFormat=_H3cDHCPROption82IfFormat_Object((1,3,6,1,4,1,2011,10,2,58,1,8,3,1,3),_H3cDHCPROption82IfFormat_Type())
h3cDHCPROption82IfFormat.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDHCPROption82IfFormat.setStatus(_A)
class _H3cDHCPROption82IfNodeType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('invalid',1),('mac',2),('sysname',3),('userdefine',4)))
_H3cDHCPROption82IfNodeType_Type.__name__=_C
_H3cDHCPROption82IfNodeType_Object=MibTableColumn
h3cDHCPROption82IfNodeType=_H3cDHCPROption82IfNodeType_Object((1,3,6,1,4,1,2011,10,2,58,1,8,3,1,4),_H3cDHCPROption82IfNodeType_Type())
h3cDHCPROption82IfNodeType.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDHCPROption82IfNodeType.setStatus(_A)
class _H3cDHCPROption82IfUsrDefString_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
_H3cDHCPROption82IfUsrDefString_Type.__name__=_M
_H3cDHCPROption82IfUsrDefString_Object=MibTableColumn
h3cDHCPROption82IfUsrDefString=_H3cDHCPROption82IfUsrDefString_Object((1,3,6,1,4,1,2011,10,2,58,1,8,3,1,5),_H3cDHCPROption82IfUsrDefString_Type())
h3cDHCPROption82IfUsrDefString.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDHCPROption82IfUsrDefString.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'h3cDhcpRelay':h3cDhcpRelay,'h3cDHCPRMibObject':h3cDHCPRMibObject,'h3cDHCPRIfSelectTable':h3cDHCPRIfSelectTable,'h3cDHCPRIfSelectEntry':h3cDHCPRIfSelectEntry,'h3cDHCPRIfSelectRelayMode':h3cDHCPRIfSelectRelayMode,'h3cDHCPRIpToGroupTable':h3cDHCPRIpToGroupTable,'h3cDHCPRIpToGroupEntry':h3cDHCPRIpToGroupEntry,_N:h3cDHCPRIpToGroupGroupId,_O:h3cDHCPRIpToGroupServerIpType,_P:h3cDHCPRIpToGroupServerIp,'h3cDHCPRIpToGroupRowStatus':h3cDHCPRIpToGroupRowStatus,'h3cDHCPRIfToGroupTable':h3cDHCPRIfToGroupTable,'h3cDHCPRIfToGroupEntry':h3cDHCPRIfToGroupEntry,'h3cDHCPRIfToGroupGroupId':h3cDHCPRIfToGroupGroupId,'h3cDHCPRIfToGroupRowStatus':h3cDHCPRIfToGroupRowStatus,'h3cDHCPRAddrCheckTable':h3cDHCPRAddrCheckTable,'h3cDHCPRAddrCheckEntry':h3cDHCPRAddrCheckEntry,'h3cDHCPRAddrCheckSwitch':h3cDHCPRAddrCheckSwitch,'h3cDHCPRSecurityTable':h3cDHCPRSecurityTable,'h3cDHCPRSecurityEntry':h3cDHCPRSecurityEntry,_Q:h3cDHCPRSecurityClientIpAddrType,_R:h3cDHCPRSecurityClientIpAddr,'h3cDHCPRSecurityClientMacAddr':h3cDHCPRSecurityClientMacAddr,'h3cDHCPRSecurityClientProperty':h3cDHCPRSecurityClientProperty,'h3cDHCPRSecurityClientRowStatus':h3cDHCPRSecurityClientRowStatus,'h3cDHCPRStatisticsGroup':h3cDHCPRStatisticsGroup,'h3cDHCPRRxClientPktNum':h3cDHCPRRxClientPktNum,'h3cDHCPRTxClientPktNum':h3cDHCPRTxClientPktNum,'h3cDHCPRRxServerPktNum':h3cDHCPRRxServerPktNum,'h3cDHCPRTxServerPktNum':h3cDHCPRTxServerPktNum,'h3cDHCPRDiscoverPktNum':h3cDHCPRDiscoverPktNum,'h3cDHCPRRequestPktNum':h3cDHCPRRequestPktNum,'h3cDHCPRDeclinePktNum':h3cDHCPRDeclinePktNum,'h3cDHCPRReleasePktNum':h3cDHCPRReleasePktNum,'h3cDHCPRInformPktNum':h3cDHCPRInformPktNum,'h3cDHCPROfferPktNum':h3cDHCPROfferPktNum,'h3cDHCPRAckPktNum':h3cDHCPRAckPktNum,'h3cDHCPRNakPktNum':h3cDHCPRNakPktNum,'h3cDHCPRStatisticsReset':h3cDHCPRStatisticsReset,'h3cDHCPRCycleGroup':h3cDHCPRCycleGroup,'h3cDHCPRCycleStatus':h3cDHCPRCycleStatus,'h3cDHCPRConfigOption82Group':h3cDHCPRConfigOption82Group,'h3cDHCPROption82Switch':h3cDHCPROption82Switch,'h3cDHCPROption82HandleStrategy':h3cDHCPROption82HandleStrategy,'h3cDHCPRConfigOption82IfTable':h3cDHCPRConfigOption82IfTable,'h3cDHCPRConfigOption82IfEntry':h3cDHCPRConfigOption82IfEntry,'h3cDHCPROption82IfSwitch':h3cDHCPROption82IfSwitch,'h3cDHCPROption82IfStrategy':h3cDHCPROption82IfStrategy,'h3cDHCPROption82IfFormat':h3cDHCPROption82IfFormat,'h3cDHCPROption82IfNodeType':h3cDHCPROption82IfNodeType,'h3cDHCPROption82IfUsrDefString':h3cDHCPROption82IfUsrDefString})