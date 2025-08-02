_U='rlDhcpSrvAuxOptionType'
_T='rlDhcpSrvAuxOptionCode'
_S='rlDhcpSrvOptionParamsCode'
_R='rlDhcpSrvOptionParamsName'
_Q='rlDhcpSrvConfParamsName'
_P='rlDhcpSrvDynamicPoolName'
_O='rlDhcpSrvIpAddrIpAddr'
_N='rlDhcpRelayInterfaceListIndex'
_M='rlDhcpRelayInterfaceIfindex'
_L='rlDhcpRelayNextServerIpAddr'
_K='OctetString'
_J='SnmpAdminString'
_I='obsolete'
_H='TruthValue'
_G='Integer32'
_F='Unsigned32'
_E='RADLAN-DHCP-MIB'
_D='DisplayString'
_C='read-only'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_K,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
PortList,=mibBuilder.importSymbols('Q-BRIDGE-MIB','PortList')
VlanList1,VlanList2,VlanList3,VlanList4=mibBuilder.importSymbols('RADLAN-BRIDGEMIBOBJECTS-MIB','VlanList1','VlanList2','VlanList3','VlanList4')
rnd,=mibBuilder.importSymbols('RADLAN-MIB','rnd')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_J)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_G,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_F,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_D,'PhysAddress','RowStatus','TextualConvention',_H)
rsDHCP=ModuleIdentity((1,3,6,1,4,1,89,38))
if mibBuilder.loadTexts:rsDHCP.setRevisions(('2003-10-18 00:00',))
class RlDhcpSrvOptionTypeEnum(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('boolean',1),('integer',2),('ascii',3),('ip',4),('hex',5),('ip-list',6)))
_RsDhcpMibVersion_Type=Integer32
_RsDhcpMibVersion_Object=MibScalar
rsDhcpMibVersion=_RsDhcpMibVersion_Object((1,3,6,1,4,1,89,38,14),_RsDhcpMibVersion_Type())
rsDhcpMibVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:rsDhcpMibVersion.setStatus(_A)
_RlDhcpRelayMaximalNumberOfNonIpVlans_Type=Unsigned32
_RlDhcpRelayMaximalNumberOfNonIpVlans_Object=MibScalar
rlDhcpRelayMaximalNumberOfNonIpVlans=_RlDhcpRelayMaximalNumberOfNonIpVlans_Object((1,3,6,1,4,1,89,38,23),_RlDhcpRelayMaximalNumberOfNonIpVlans_Type())
rlDhcpRelayMaximalNumberOfNonIpVlans.setMaxAccess(_C)
if mibBuilder.loadTexts:rlDhcpRelayMaximalNumberOfNonIpVlans.setStatus(_A)
_RlDhcpRelayCurrentNumberOfNonIpVlans_Type=Unsigned32
_RlDhcpRelayCurrentNumberOfNonIpVlans_Object=MibScalar
rlDhcpRelayCurrentNumberOfNonIpVlans=_RlDhcpRelayCurrentNumberOfNonIpVlans_Object((1,3,6,1,4,1,89,38,24),_RlDhcpRelayCurrentNumberOfNonIpVlans_Type())
rlDhcpRelayCurrentNumberOfNonIpVlans.setMaxAccess(_C)
if mibBuilder.loadTexts:rlDhcpRelayCurrentNumberOfNonIpVlans.setStatus(_A)
_RlDhcpRelayEnable_Type=TruthValue
_RlDhcpRelayEnable_Object=MibScalar
rlDhcpRelayEnable=_RlDhcpRelayEnable_Object((1,3,6,1,4,1,89,38,25),_RlDhcpRelayEnable_Type())
rlDhcpRelayEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:rlDhcpRelayEnable.setStatus(_A)
_RlDhcpRelayExists_Type=TruthValue
_RlDhcpRelayExists_Object=MibScalar
rlDhcpRelayExists=_RlDhcpRelayExists_Object((1,3,6,1,4,1,89,38,26),_RlDhcpRelayExists_Type())
rlDhcpRelayExists.setMaxAccess(_C)
if mibBuilder.loadTexts:rlDhcpRelayExists.setStatus(_A)
_RlDhcpRelayNextServerTable_Object=MibTable
rlDhcpRelayNextServerTable=_RlDhcpRelayNextServerTable_Object((1,3,6,1,4,1,89,38,27))
if mibBuilder.loadTexts:rlDhcpRelayNextServerTable.setStatus(_A)
_RlDhcpRelayNextServerEntry_Object=MibTableRow
rlDhcpRelayNextServerEntry=_RlDhcpRelayNextServerEntry_Object((1,3,6,1,4,1,89,38,27,1))
rlDhcpRelayNextServerEntry.setIndexNames((0,_E,_L))
if mibBuilder.loadTexts:rlDhcpRelayNextServerEntry.setStatus(_A)
_RlDhcpRelayNextServerIpAddr_Type=IpAddress
_RlDhcpRelayNextServerIpAddr_Object=MibTableColumn
rlDhcpRelayNextServerIpAddr=_RlDhcpRelayNextServerIpAddr_Object((1,3,6,1,4,1,89,38,27,1,1),_RlDhcpRelayNextServerIpAddr_Type())
rlDhcpRelayNextServerIpAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:rlDhcpRelayNextServerIpAddr.setStatus(_A)
_RlDhcpRelayNextServerSecThreshold_Type=Unsigned32
_RlDhcpRelayNextServerSecThreshold_Object=MibTableColumn
rlDhcpRelayNextServerSecThreshold=_RlDhcpRelayNextServerSecThreshold_Object((1,3,6,1,4,1,89,38,27,1,2),_RlDhcpRelayNextServerSecThreshold_Type())
rlDhcpRelayNextServerSecThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:rlDhcpRelayNextServerSecThreshold.setStatus(_A)
_RlDhcpRelayNextServerRowStatus_Type=RowStatus
_RlDhcpRelayNextServerRowStatus_Object=MibTableColumn
rlDhcpRelayNextServerRowStatus=_RlDhcpRelayNextServerRowStatus_Object((1,3,6,1,4,1,89,38,27,1,3),_RlDhcpRelayNextServerRowStatus_Type())
rlDhcpRelayNextServerRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:rlDhcpRelayNextServerRowStatus.setStatus(_A)
_RlDhcpRelayInterfaceTable_Object=MibTable
rlDhcpRelayInterfaceTable=_RlDhcpRelayInterfaceTable_Object((1,3,6,1,4,1,89,38,28))
if mibBuilder.loadTexts:rlDhcpRelayInterfaceTable.setStatus(_A)
_RlDhcpRelayInterfaceEntry_Object=MibTableRow
rlDhcpRelayInterfaceEntry=_RlDhcpRelayInterfaceEntry_Object((1,3,6,1,4,1,89,38,28,1))
rlDhcpRelayInterfaceEntry.setIndexNames((0,_E,_M))
if mibBuilder.loadTexts:rlDhcpRelayInterfaceEntry.setStatus(_A)
_RlDhcpRelayInterfaceIfindex_Type=Integer32
_RlDhcpRelayInterfaceIfindex_Object=MibTableColumn
rlDhcpRelayInterfaceIfindex=_RlDhcpRelayInterfaceIfindex_Object((1,3,6,1,4,1,89,38,28,1,1),_RlDhcpRelayInterfaceIfindex_Type())
rlDhcpRelayInterfaceIfindex.setMaxAccess(_B)
if mibBuilder.loadTexts:rlDhcpRelayInterfaceIfindex.setStatus(_A)
_RlDhcpRelayInterfaceUseGiaddr_Type=TruthValue
_RlDhcpRelayInterfaceUseGiaddr_Object=MibTableColumn
rlDhcpRelayInterfaceUseGiaddr=_RlDhcpRelayInterfaceUseGiaddr_Object((1,3,6,1,4,1,89,38,28,1,2),_RlDhcpRelayInterfaceUseGiaddr_Type())
rlDhcpRelayInterfaceUseGiaddr.setMaxAccess(_B)
if mibBuilder.loadTexts:rlDhcpRelayInterfaceUseGiaddr.setStatus(_A)
_RlDhcpRelayInterfaceRowStatus_Type=RowStatus
_RlDhcpRelayInterfaceRowStatus_Object=MibTableColumn
rlDhcpRelayInterfaceRowStatus=_RlDhcpRelayInterfaceRowStatus_Object((1,3,6,1,4,1,89,38,28,1,3),_RlDhcpRelayInterfaceRowStatus_Type())
rlDhcpRelayInterfaceRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:rlDhcpRelayInterfaceRowStatus.setStatus(_A)
_RlDhcpRelayInterfaceListTable_Object=MibTable
rlDhcpRelayInterfaceListTable=_RlDhcpRelayInterfaceListTable_Object((1,3,6,1,4,1,89,38,29))
if mibBuilder.loadTexts:rlDhcpRelayInterfaceListTable.setStatus(_A)
_RlDhcpRelayInterfaceListEntry_Object=MibTableRow
rlDhcpRelayInterfaceListEntry=_RlDhcpRelayInterfaceListEntry_Object((1,3,6,1,4,1,89,38,29,1))
rlDhcpRelayInterfaceListEntry.setIndexNames((0,_E,_N))
if mibBuilder.loadTexts:rlDhcpRelayInterfaceListEntry.setStatus(_A)
_RlDhcpRelayInterfaceListIndex_Type=Integer32
_RlDhcpRelayInterfaceListIndex_Object=MibTableColumn
rlDhcpRelayInterfaceListIndex=_RlDhcpRelayInterfaceListIndex_Object((1,3,6,1,4,1,89,38,29,1,1),_RlDhcpRelayInterfaceListIndex_Type())
rlDhcpRelayInterfaceListIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:rlDhcpRelayInterfaceListIndex.setStatus(_A)
_RlDhcpRelayInterfaceListPortList_Type=PortList
_RlDhcpRelayInterfaceListPortList_Object=MibTableColumn
rlDhcpRelayInterfaceListPortList=_RlDhcpRelayInterfaceListPortList_Object((1,3,6,1,4,1,89,38,29,1,2),_RlDhcpRelayInterfaceListPortList_Type())
rlDhcpRelayInterfaceListPortList.setMaxAccess(_B)
if mibBuilder.loadTexts:rlDhcpRelayInterfaceListPortList.setStatus(_A)
_RlDhcpRelayInterfaceListVlanId1To1024_Type=VlanList1
_RlDhcpRelayInterfaceListVlanId1To1024_Object=MibTableColumn
rlDhcpRelayInterfaceListVlanId1To1024=_RlDhcpRelayInterfaceListVlanId1To1024_Object((1,3,6,1,4,1,89,38,29,1,3),_RlDhcpRelayInterfaceListVlanId1To1024_Type())
rlDhcpRelayInterfaceListVlanId1To1024.setMaxAccess(_B)
if mibBuilder.loadTexts:rlDhcpRelayInterfaceListVlanId1To1024.setStatus(_A)
_RlDhcpRelayInterfaceListVlanId1025To2048_Type=VlanList2
_RlDhcpRelayInterfaceListVlanId1025To2048_Object=MibTableColumn
rlDhcpRelayInterfaceListVlanId1025To2048=_RlDhcpRelayInterfaceListVlanId1025To2048_Object((1,3,6,1,4,1,89,38,29,1,4),_RlDhcpRelayInterfaceListVlanId1025To2048_Type())
rlDhcpRelayInterfaceListVlanId1025To2048.setMaxAccess(_B)
if mibBuilder.loadTexts:rlDhcpRelayInterfaceListVlanId1025To2048.setStatus(_A)
_RlDhcpRelayInterfaceListVlanId2049To3072_Type=VlanList3
_RlDhcpRelayInterfaceListVlanId2049To3072_Object=MibTableColumn
rlDhcpRelayInterfaceListVlanId2049To3072=_RlDhcpRelayInterfaceListVlanId2049To3072_Object((1,3,6,1,4,1,89,38,29,1,5),_RlDhcpRelayInterfaceListVlanId2049To3072_Type())
rlDhcpRelayInterfaceListVlanId2049To3072.setMaxAccess(_B)
if mibBuilder.loadTexts:rlDhcpRelayInterfaceListVlanId2049To3072.setStatus(_A)
_RlDhcpRelayInterfaceListVlanId3073To4094_Type=VlanList4
_RlDhcpRelayInterfaceListVlanId3073To4094_Object=MibTableColumn
rlDhcpRelayInterfaceListVlanId3073To4094=_RlDhcpRelayInterfaceListVlanId3073To4094_Object((1,3,6,1,4,1,89,38,29,1,6),_RlDhcpRelayInterfaceListVlanId3073To4094_Type())
rlDhcpRelayInterfaceListVlanId3073To4094.setMaxAccess(_B)
if mibBuilder.loadTexts:rlDhcpRelayInterfaceListVlanId3073To4094.setStatus(_A)
class _RlDhcpSrvEnable_Type(TruthValue):defaultValue=2
_RlDhcpSrvEnable_Type.__name__=_H
_RlDhcpSrvEnable_Object=MibScalar
rlDhcpSrvEnable=_RlDhcpSrvEnable_Object((1,3,6,1,4,1,89,38,30),_RlDhcpSrvEnable_Type())
rlDhcpSrvEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:rlDhcpSrvEnable.setStatus(_A)
_RlDhcpSrvExists_Type=TruthValue
_RlDhcpSrvExists_Object=MibScalar
rlDhcpSrvExists=_RlDhcpSrvExists_Object((1,3,6,1,4,1,89,38,31),_RlDhcpSrvExists_Type())
rlDhcpSrvExists.setMaxAccess(_C)
if mibBuilder.loadTexts:rlDhcpSrvExists.setStatus(_A)
class _RlDhcpSrvDbLocation_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('nvram',1),('flash',2)))
_RlDhcpSrvDbLocation_Type.__name__=_G
_RlDhcpSrvDbLocation_Object=MibScalar
rlDhcpSrvDbLocation=_RlDhcpSrvDbLocation_Object((1,3,6,1,4,1,89,38,32),_RlDhcpSrvDbLocation_Type())
rlDhcpSrvDbLocation.setMaxAccess(_C)
if mibBuilder.loadTexts:rlDhcpSrvDbLocation.setStatus(_I)
_RlDhcpSrvMaxNumOfClients_Type=Unsigned32
_RlDhcpSrvMaxNumOfClients_Object=MibScalar
rlDhcpSrvMaxNumOfClients=_RlDhcpSrvMaxNumOfClients_Object((1,3,6,1,4,1,89,38,33),_RlDhcpSrvMaxNumOfClients_Type())
rlDhcpSrvMaxNumOfClients.setMaxAccess(_C)
if mibBuilder.loadTexts:rlDhcpSrvMaxNumOfClients.setStatus(_A)
_RlDhcpSrvDbNumOfActiveEntries_Type=Unsigned32
_RlDhcpSrvDbNumOfActiveEntries_Object=MibScalar
rlDhcpSrvDbNumOfActiveEntries=_RlDhcpSrvDbNumOfActiveEntries_Object((1,3,6,1,4,1,89,38,34),_RlDhcpSrvDbNumOfActiveEntries_Type())
rlDhcpSrvDbNumOfActiveEntries.setMaxAccess(_C)
if mibBuilder.loadTexts:rlDhcpSrvDbNumOfActiveEntries.setStatus(_A)
class _RlDhcpSrvDbErase_Type(TruthValue):defaultValue=2
_RlDhcpSrvDbErase_Type.__name__=_H
_RlDhcpSrvDbErase_Object=MibScalar
rlDhcpSrvDbErase=_RlDhcpSrvDbErase_Object((1,3,6,1,4,1,89,38,35),_RlDhcpSrvDbErase_Type())
rlDhcpSrvDbErase.setMaxAccess(_B)
if mibBuilder.loadTexts:rlDhcpSrvDbErase.setStatus(_I)
class _RlDhcpSrvProbeEnable_Type(TruthValue):defaultValue=2
_RlDhcpSrvProbeEnable_Type.__name__=_H
_RlDhcpSrvProbeEnable_Object=MibScalar
rlDhcpSrvProbeEnable=_RlDhcpSrvProbeEnable_Object((1,3,6,1,4,1,89,38,36),_RlDhcpSrvProbeEnable_Type())
rlDhcpSrvProbeEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:rlDhcpSrvProbeEnable.setStatus(_A)
class _RlDhcpSrvProbeTimeout_Type(Unsigned32):defaultValue=500;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(300,10000))
_RlDhcpSrvProbeTimeout_Type.__name__=_F
_RlDhcpSrvProbeTimeout_Object=MibScalar
rlDhcpSrvProbeTimeout=_RlDhcpSrvProbeTimeout_Object((1,3,6,1,4,1,89,38,37),_RlDhcpSrvProbeTimeout_Type())
rlDhcpSrvProbeTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:rlDhcpSrvProbeTimeout.setStatus(_A)
class _RlDhcpSrvProbeRetries_Type(Unsigned32):defaultValue=2;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_RlDhcpSrvProbeRetries_Type.__name__=_F
_RlDhcpSrvProbeRetries_Object=MibScalar
rlDhcpSrvProbeRetries=_RlDhcpSrvProbeRetries_Object((1,3,6,1,4,1,89,38,38),_RlDhcpSrvProbeRetries_Type())
rlDhcpSrvProbeRetries.setMaxAccess(_B)
if mibBuilder.loadTexts:rlDhcpSrvProbeRetries.setStatus(_A)
class _RlDhcpSrvDefaultNetworkPoolName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_RlDhcpSrvDefaultNetworkPoolName_Type.__name__=_D
_RlDhcpSrvDefaultNetworkPoolName_Object=MibScalar
rlDhcpSrvDefaultNetworkPoolName=_RlDhcpSrvDefaultNetworkPoolName_Object((1,3,6,1,4,1,89,38,39),_RlDhcpSrvDefaultNetworkPoolName_Type())
rlDhcpSrvDefaultNetworkPoolName.setMaxAccess(_C)
if mibBuilder.loadTexts:rlDhcpSrvDefaultNetworkPoolName.setStatus(_A)
_RlDhcpSrvIpAddrTable_Object=MibTable
rlDhcpSrvIpAddrTable=_RlDhcpSrvIpAddrTable_Object((1,3,6,1,4,1,89,38,45))
if mibBuilder.loadTexts:rlDhcpSrvIpAddrTable.setStatus(_A)
_RlDhcpSrvIpAddrEntry_Object=MibTableRow
rlDhcpSrvIpAddrEntry=_RlDhcpSrvIpAddrEntry_Object((1,3,6,1,4,1,89,38,45,1))
rlDhcpSrvIpAddrEntry.setIndexNames((0,_E,_O))
if mibBuilder.loadTexts:rlDhcpSrvIpAddrEntry.setStatus(_A)
_RlDhcpSrvIpAddrIpAddr_Type=IpAddress
_RlDhcpSrvIpAddrIpAddr_Object=MibTableColumn
rlDhcpSrvIpAddrIpAddr=_RlDhcpSrvIpAddrIpAddr_Object((1,3,6,1,4,1,89,38,45,1,1),_RlDhcpSrvIpAddrIpAddr_Type())
rlDhcpSrvIpAddrIpAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:rlDhcpSrvIpAddrIpAddr.setStatus(_A)
_RlDhcpSrvIpAddrIpNetMask_Type=IpAddress
_RlDhcpSrvIpAddrIpNetMask_Object=MibTableColumn
rlDhcpSrvIpAddrIpNetMask=_RlDhcpSrvIpAddrIpNetMask_Object((1,3,6,1,4,1,89,38,45,1,2),_RlDhcpSrvIpAddrIpNetMask_Type())
rlDhcpSrvIpAddrIpNetMask.setMaxAccess(_B)
if mibBuilder.loadTexts:rlDhcpSrvIpAddrIpNetMask.setStatus(_A)
class _RlDhcpSrvIpAddrIdentifier_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,32))
_RlDhcpSrvIpAddrIdentifier_Type.__name__=_K
_RlDhcpSrvIpAddrIdentifier_Object=MibTableColumn
rlDhcpSrvIpAddrIdentifier=_RlDhcpSrvIpAddrIdentifier_Object((1,3,6,1,4,1,89,38,45,1,3),_RlDhcpSrvIpAddrIdentifier_Type())
rlDhcpSrvIpAddrIdentifier.setMaxAccess(_B)
if mibBuilder.loadTexts:rlDhcpSrvIpAddrIdentifier.setStatus(_A)
class _RlDhcpSrvIpAddrIdentifierType_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('physAddr',1),('clientId',2)))
_RlDhcpSrvIpAddrIdentifierType_Type.__name__=_G
_RlDhcpSrvIpAddrIdentifierType_Object=MibTableColumn
rlDhcpSrvIpAddrIdentifierType=_RlDhcpSrvIpAddrIdentifierType_Object((1,3,6,1,4,1,89,38,45,1,4),_RlDhcpSrvIpAddrIdentifierType_Type())
rlDhcpSrvIpAddrIdentifierType.setMaxAccess(_B)
if mibBuilder.loadTexts:rlDhcpSrvIpAddrIdentifierType.setStatus(_A)
class _RlDhcpSrvIpAddrClnHostName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_RlDhcpSrvIpAddrClnHostName_Type.__name__=_J
_RlDhcpSrvIpAddrClnHostName_Object=MibTableColumn
rlDhcpSrvIpAddrClnHostName=_RlDhcpSrvIpAddrClnHostName_Object((1,3,6,1,4,1,89,38,45,1,5),_RlDhcpSrvIpAddrClnHostName_Type())
rlDhcpSrvIpAddrClnHostName.setMaxAccess(_B)
if mibBuilder.loadTexts:rlDhcpSrvIpAddrClnHostName.setStatus(_A)
class _RlDhcpSrvIpAddrMechanism_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('manual',1),('automatic',2),('dynamic',3)))
_RlDhcpSrvIpAddrMechanism_Type.__name__=_G
_RlDhcpSrvIpAddrMechanism_Object=MibTableColumn
rlDhcpSrvIpAddrMechanism=_RlDhcpSrvIpAddrMechanism_Object((1,3,6,1,4,1,89,38,45,1,6),_RlDhcpSrvIpAddrMechanism_Type())
rlDhcpSrvIpAddrMechanism.setMaxAccess(_B)
if mibBuilder.loadTexts:rlDhcpSrvIpAddrMechanism.setStatus(_A)
class _RlDhcpSrvIpAddrAgeTime_Type(Unsigned32):defaultValue=0
_RlDhcpSrvIpAddrAgeTime_Type.__name__=_F
_RlDhcpSrvIpAddrAgeTime_Object=MibTableColumn
rlDhcpSrvIpAddrAgeTime=_RlDhcpSrvIpAddrAgeTime_Object((1,3,6,1,4,1,89,38,45,1,7),_RlDhcpSrvIpAddrAgeTime_Type())
rlDhcpSrvIpAddrAgeTime.setMaxAccess(_C)
if mibBuilder.loadTexts:rlDhcpSrvIpAddrAgeTime.setStatus(_A)
class _RlDhcpSrvIpAddrPoolName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_RlDhcpSrvIpAddrPoolName_Type.__name__=_D
_RlDhcpSrvIpAddrPoolName_Object=MibTableColumn
rlDhcpSrvIpAddrPoolName=_RlDhcpSrvIpAddrPoolName_Object((1,3,6,1,4,1,89,38,45,1,8),_RlDhcpSrvIpAddrPoolName_Type())
rlDhcpSrvIpAddrPoolName.setMaxAccess(_B)
if mibBuilder.loadTexts:rlDhcpSrvIpAddrPoolName.setStatus(_A)
class _RlDhcpSrvIpAddrConfParamsName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_RlDhcpSrvIpAddrConfParamsName_Type.__name__=_D
_RlDhcpSrvIpAddrConfParamsName_Object=MibTableColumn
rlDhcpSrvIpAddrConfParamsName=_RlDhcpSrvIpAddrConfParamsName_Object((1,3,6,1,4,1,89,38,45,1,9),_RlDhcpSrvIpAddrConfParamsName_Type())
rlDhcpSrvIpAddrConfParamsName.setMaxAccess(_B)
if mibBuilder.loadTexts:rlDhcpSrvIpAddrConfParamsName.setStatus(_A)
_RlDhcpSrvIpAddrRowStatus_Type=RowStatus
_RlDhcpSrvIpAddrRowStatus_Object=MibTableColumn
rlDhcpSrvIpAddrRowStatus=_RlDhcpSrvIpAddrRowStatus_Object((1,3,6,1,4,1,89,38,45,1,10),_RlDhcpSrvIpAddrRowStatus_Type())
rlDhcpSrvIpAddrRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:rlDhcpSrvIpAddrRowStatus.setStatus(_A)
class _RlDhcpSrvIpAddrLeaseTime_Type(Unsigned32):defaultValue=86400
_RlDhcpSrvIpAddrLeaseTime_Type.__name__=_F
_RlDhcpSrvIpAddrLeaseTime_Object=MibTableColumn
rlDhcpSrvIpAddrLeaseTime=_RlDhcpSrvIpAddrLeaseTime_Object((1,3,6,1,4,1,89,38,45,1,11),_RlDhcpSrvIpAddrLeaseTime_Type())
rlDhcpSrvIpAddrLeaseTime.setMaxAccess(_C)
if mibBuilder.loadTexts:rlDhcpSrvIpAddrLeaseTime.setStatus(_A)
class _RlDhcpSrvIpAddrState_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('pre-allocated',1),('valid',2),('expired',3),('declined',4)))
_RlDhcpSrvIpAddrState_Type.__name__=_G
_RlDhcpSrvIpAddrState_Object=MibTableColumn
rlDhcpSrvIpAddrState=_RlDhcpSrvIpAddrState_Object((1,3,6,1,4,1,89,38,45,1,12),_RlDhcpSrvIpAddrState_Type())
rlDhcpSrvIpAddrState.setMaxAccess(_C)
if mibBuilder.loadTexts:rlDhcpSrvIpAddrState.setStatus(_A)
class _RlDhcpSrvIpAddrOptionParamsName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_RlDhcpSrvIpAddrOptionParamsName_Type.__name__=_D
_RlDhcpSrvIpAddrOptionParamsName_Object=MibTableColumn
rlDhcpSrvIpAddrOptionParamsName=_RlDhcpSrvIpAddrOptionParamsName_Object((1,3,6,1,4,1,89,38,45,1,13),_RlDhcpSrvIpAddrOptionParamsName_Type())
rlDhcpSrvIpAddrOptionParamsName.setMaxAccess(_B)
if mibBuilder.loadTexts:rlDhcpSrvIpAddrOptionParamsName.setStatus(_A)
_RlDhcpSrvDynamicTable_Object=MibTable
rlDhcpSrvDynamicTable=_RlDhcpSrvDynamicTable_Object((1,3,6,1,4,1,89,38,46))
if mibBuilder.loadTexts:rlDhcpSrvDynamicTable.setStatus(_A)
_RlDhcpSrvDynamicEntry_Object=MibTableRow
rlDhcpSrvDynamicEntry=_RlDhcpSrvDynamicEntry_Object((1,3,6,1,4,1,89,38,46,1))
rlDhcpSrvDynamicEntry.setIndexNames((0,_E,_P))
if mibBuilder.loadTexts:rlDhcpSrvDynamicEntry.setStatus(_A)
class _RlDhcpSrvDynamicPoolName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_RlDhcpSrvDynamicPoolName_Type.__name__=_D
_RlDhcpSrvDynamicPoolName_Object=MibTableColumn
rlDhcpSrvDynamicPoolName=_RlDhcpSrvDynamicPoolName_Object((1,3,6,1,4,1,89,38,46,1,1),_RlDhcpSrvDynamicPoolName_Type())
rlDhcpSrvDynamicPoolName.setMaxAccess(_B)
if mibBuilder.loadTexts:rlDhcpSrvDynamicPoolName.setStatus(_A)
_RlDhcpSrvDynamicIpAddrFrom_Type=IpAddress
_RlDhcpSrvDynamicIpAddrFrom_Object=MibTableColumn
rlDhcpSrvDynamicIpAddrFrom=_RlDhcpSrvDynamicIpAddrFrom_Object((1,3,6,1,4,1,89,38,46,1,2),_RlDhcpSrvDynamicIpAddrFrom_Type())
rlDhcpSrvDynamicIpAddrFrom.setMaxAccess(_B)
if mibBuilder.loadTexts:rlDhcpSrvDynamicIpAddrFrom.setStatus(_A)
_RlDhcpSrvDynamicIpAddrTo_Type=IpAddress
_RlDhcpSrvDynamicIpAddrTo_Object=MibTableColumn
rlDhcpSrvDynamicIpAddrTo=_RlDhcpSrvDynamicIpAddrTo_Object((1,3,6,1,4,1,89,38,46,1,3),_RlDhcpSrvDynamicIpAddrTo_Type())
rlDhcpSrvDynamicIpAddrTo.setMaxAccess(_B)
if mibBuilder.loadTexts:rlDhcpSrvDynamicIpAddrTo.setStatus(_A)
_RlDhcpSrvDynamicIpNetMask_Type=IpAddress
_RlDhcpSrvDynamicIpNetMask_Object=MibTableColumn
rlDhcpSrvDynamicIpNetMask=_RlDhcpSrvDynamicIpNetMask_Object((1,3,6,1,4,1,89,38,46,1,4),_RlDhcpSrvDynamicIpNetMask_Type())
rlDhcpSrvDynamicIpNetMask.setMaxAccess(_B)
if mibBuilder.loadTexts:rlDhcpSrvDynamicIpNetMask.setStatus(_A)
class _RlDhcpSrvDynamicLeaseTime_Type(Unsigned32):defaultValue=86400
_RlDhcpSrvDynamicLeaseTime_Type.__name__=_F
_RlDhcpSrvDynamicLeaseTime_Object=MibTableColumn
rlDhcpSrvDynamicLeaseTime=_RlDhcpSrvDynamicLeaseTime_Object((1,3,6,1,4,1,89,38,46,1,5),_RlDhcpSrvDynamicLeaseTime_Type())
rlDhcpSrvDynamicLeaseTime.setMaxAccess(_B)
if mibBuilder.loadTexts:rlDhcpSrvDynamicLeaseTime.setStatus(_A)
class _RlDhcpSrvDynamicProbeEnable_Type(TruthValue):defaultValue=1
_RlDhcpSrvDynamicProbeEnable_Type.__name__=_H
_RlDhcpSrvDynamicProbeEnable_Object=MibTableColumn
rlDhcpSrvDynamicProbeEnable=_RlDhcpSrvDynamicProbeEnable_Object((1,3,6,1,4,1,89,38,46,1,6),_RlDhcpSrvDynamicProbeEnable_Type())
rlDhcpSrvDynamicProbeEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:rlDhcpSrvDynamicProbeEnable.setStatus(_A)
_RlDhcpSrvDynamicTotalNumOfAddr_Type=Unsigned32
_RlDhcpSrvDynamicTotalNumOfAddr_Object=MibTableColumn
rlDhcpSrvDynamicTotalNumOfAddr=_RlDhcpSrvDynamicTotalNumOfAddr_Object((1,3,6,1,4,1,89,38,46,1,7),_RlDhcpSrvDynamicTotalNumOfAddr_Type())
rlDhcpSrvDynamicTotalNumOfAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:rlDhcpSrvDynamicTotalNumOfAddr.setStatus(_A)
_RlDhcpSrvDynamicFreeNumOfAddr_Type=Unsigned32
_RlDhcpSrvDynamicFreeNumOfAddr_Object=MibTableColumn
rlDhcpSrvDynamicFreeNumOfAddr=_RlDhcpSrvDynamicFreeNumOfAddr_Object((1,3,6,1,4,1,89,38,46,1,8),_RlDhcpSrvDynamicFreeNumOfAddr_Type())
rlDhcpSrvDynamicFreeNumOfAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:rlDhcpSrvDynamicFreeNumOfAddr.setStatus(_A)
class _RlDhcpSrvDynamicConfParamsName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_RlDhcpSrvDynamicConfParamsName_Type.__name__=_D
_RlDhcpSrvDynamicConfParamsName_Object=MibTableColumn
rlDhcpSrvDynamicConfParamsName=_RlDhcpSrvDynamicConfParamsName_Object((1,3,6,1,4,1,89,38,46,1,9),_RlDhcpSrvDynamicConfParamsName_Type())
rlDhcpSrvDynamicConfParamsName.setMaxAccess(_B)
if mibBuilder.loadTexts:rlDhcpSrvDynamicConfParamsName.setStatus(_A)
_RlDhcpSrvDynamicRowStatus_Type=RowStatus
_RlDhcpSrvDynamicRowStatus_Object=MibTableColumn
rlDhcpSrvDynamicRowStatus=_RlDhcpSrvDynamicRowStatus_Object((1,3,6,1,4,1,89,38,46,1,10),_RlDhcpSrvDynamicRowStatus_Type())
rlDhcpSrvDynamicRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:rlDhcpSrvDynamicRowStatus.setStatus(_A)
_RlDhcpSrvDynamicAvailableNumOfAddr_Type=Unsigned32
_RlDhcpSrvDynamicAvailableNumOfAddr_Object=MibTableColumn
rlDhcpSrvDynamicAvailableNumOfAddr=_RlDhcpSrvDynamicAvailableNumOfAddr_Object((1,3,6,1,4,1,89,38,46,1,11),_RlDhcpSrvDynamicAvailableNumOfAddr_Type())
rlDhcpSrvDynamicAvailableNumOfAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:rlDhcpSrvDynamicAvailableNumOfAddr.setStatus(_A)
_RlDhcpSrvDynamicNumOfPreallocatedAddr_Type=Unsigned32
_RlDhcpSrvDynamicNumOfPreallocatedAddr_Object=MibTableColumn
rlDhcpSrvDynamicNumOfPreallocatedAddr=_RlDhcpSrvDynamicNumOfPreallocatedAddr_Object((1,3,6,1,4,1,89,38,46,1,12),_RlDhcpSrvDynamicNumOfPreallocatedAddr_Type())
rlDhcpSrvDynamicNumOfPreallocatedAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:rlDhcpSrvDynamicNumOfPreallocatedAddr.setStatus(_A)
_RlDhcpSrvDynamicNumOfValidAddr_Type=Unsigned32
_RlDhcpSrvDynamicNumOfValidAddr_Object=MibTableColumn
rlDhcpSrvDynamicNumOfValidAddr=_RlDhcpSrvDynamicNumOfValidAddr_Object((1,3,6,1,4,1,89,38,46,1,13),_RlDhcpSrvDynamicNumOfValidAddr_Type())
rlDhcpSrvDynamicNumOfValidAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:rlDhcpSrvDynamicNumOfValidAddr.setStatus(_A)
_RlDhcpSrvDynamicNumOfExpiredAddr_Type=Unsigned32
_RlDhcpSrvDynamicNumOfExpiredAddr_Object=MibTableColumn
rlDhcpSrvDynamicNumOfExpiredAddr=_RlDhcpSrvDynamicNumOfExpiredAddr_Object((1,3,6,1,4,1,89,38,46,1,14),_RlDhcpSrvDynamicNumOfExpiredAddr_Type())
rlDhcpSrvDynamicNumOfExpiredAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:rlDhcpSrvDynamicNumOfExpiredAddr.setStatus(_A)
_RlDhcpSrvDynamicNumOfDeclinedAddr_Type=Unsigned32
_RlDhcpSrvDynamicNumOfDeclinedAddr_Object=MibTableColumn
rlDhcpSrvDynamicNumOfDeclinedAddr=_RlDhcpSrvDynamicNumOfDeclinedAddr_Object((1,3,6,1,4,1,89,38,46,1,15),_RlDhcpSrvDynamicNumOfDeclinedAddr_Type())
rlDhcpSrvDynamicNumOfDeclinedAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:rlDhcpSrvDynamicNumOfDeclinedAddr.setStatus(_A)
class _RlDhcpSrvDynamicOptionParamsName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_RlDhcpSrvDynamicOptionParamsName_Type.__name__=_D
_RlDhcpSrvDynamicOptionParamsName_Object=MibTableColumn
rlDhcpSrvDynamicOptionParamsName=_RlDhcpSrvDynamicOptionParamsName_Object((1,3,6,1,4,1,89,38,46,1,16),_RlDhcpSrvDynamicOptionParamsName_Type())
rlDhcpSrvDynamicOptionParamsName.setMaxAccess(_B)
if mibBuilder.loadTexts:rlDhcpSrvDynamicOptionParamsName.setStatus(_A)
_RlDhcpSrvConfParamsTable_Object=MibTable
rlDhcpSrvConfParamsTable=_RlDhcpSrvConfParamsTable_Object((1,3,6,1,4,1,89,38,47))
if mibBuilder.loadTexts:rlDhcpSrvConfParamsTable.setStatus(_A)
_RlDhcpSrvConfParamsEntry_Object=MibTableRow
rlDhcpSrvConfParamsEntry=_RlDhcpSrvConfParamsEntry_Object((1,3,6,1,4,1,89,38,47,1))
rlDhcpSrvConfParamsEntry.setIndexNames((0,_E,_Q))
if mibBuilder.loadTexts:rlDhcpSrvConfParamsEntry.setStatus(_A)
class _RlDhcpSrvConfParamsName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_RlDhcpSrvConfParamsName_Type.__name__=_D
_RlDhcpSrvConfParamsName_Object=MibTableColumn
rlDhcpSrvConfParamsName=_RlDhcpSrvConfParamsName_Object((1,3,6,1,4,1,89,38,47,1,1),_RlDhcpSrvConfParamsName_Type())
rlDhcpSrvConfParamsName.setMaxAccess(_B)
if mibBuilder.loadTexts:rlDhcpSrvConfParamsName.setStatus(_A)
_RlDhcpSrvConfParamsNextServerIp_Type=IpAddress
_RlDhcpSrvConfParamsNextServerIp_Object=MibTableColumn
rlDhcpSrvConfParamsNextServerIp=_RlDhcpSrvConfParamsNextServerIp_Object((1,3,6,1,4,1,89,38,47,1,2),_RlDhcpSrvConfParamsNextServerIp_Type())
rlDhcpSrvConfParamsNextServerIp.setMaxAccess(_B)
if mibBuilder.loadTexts:rlDhcpSrvConfParamsNextServerIp.setStatus(_A)
class _RlDhcpSrvConfParamsNextServerName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_RlDhcpSrvConfParamsNextServerName_Type.__name__=_D
_RlDhcpSrvConfParamsNextServerName_Object=MibTableColumn
rlDhcpSrvConfParamsNextServerName=_RlDhcpSrvConfParamsNextServerName_Object((1,3,6,1,4,1,89,38,47,1,3),_RlDhcpSrvConfParamsNextServerName_Type())
rlDhcpSrvConfParamsNextServerName.setMaxAccess(_B)
if mibBuilder.loadTexts:rlDhcpSrvConfParamsNextServerName.setStatus(_A)
class _RlDhcpSrvConfParamsBootfileName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_RlDhcpSrvConfParamsBootfileName_Type.__name__=_D
_RlDhcpSrvConfParamsBootfileName_Object=MibTableColumn
rlDhcpSrvConfParamsBootfileName=_RlDhcpSrvConfParamsBootfileName_Object((1,3,6,1,4,1,89,38,47,1,4),_RlDhcpSrvConfParamsBootfileName_Type())
rlDhcpSrvConfParamsBootfileName.setMaxAccess(_B)
if mibBuilder.loadTexts:rlDhcpSrvConfParamsBootfileName.setStatus(_A)
_RlDhcpSrvConfParamsRoutersList_Type=DisplayString
_RlDhcpSrvConfParamsRoutersList_Object=MibTableColumn
rlDhcpSrvConfParamsRoutersList=_RlDhcpSrvConfParamsRoutersList_Object((1,3,6,1,4,1,89,38,47,1,5),_RlDhcpSrvConfParamsRoutersList_Type())
rlDhcpSrvConfParamsRoutersList.setMaxAccess(_B)
if mibBuilder.loadTexts:rlDhcpSrvConfParamsRoutersList.setStatus(_A)
_RlDhcpSrvConfParamsTimeSrvList_Type=DisplayString
_RlDhcpSrvConfParamsTimeSrvList_Object=MibTableColumn
rlDhcpSrvConfParamsTimeSrvList=_RlDhcpSrvConfParamsTimeSrvList_Object((1,3,6,1,4,1,89,38,47,1,6),_RlDhcpSrvConfParamsTimeSrvList_Type())
rlDhcpSrvConfParamsTimeSrvList.setMaxAccess(_B)
if mibBuilder.loadTexts:rlDhcpSrvConfParamsTimeSrvList.setStatus(_A)
_RlDhcpSrvConfParamsDnsList_Type=DisplayString
_RlDhcpSrvConfParamsDnsList_Object=MibTableColumn
rlDhcpSrvConfParamsDnsList=_RlDhcpSrvConfParamsDnsList_Object((1,3,6,1,4,1,89,38,47,1,7),_RlDhcpSrvConfParamsDnsList_Type())
rlDhcpSrvConfParamsDnsList.setMaxAccess(_B)
if mibBuilder.loadTexts:rlDhcpSrvConfParamsDnsList.setStatus(_A)
class _RlDhcpSrvConfParamsDomainName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_RlDhcpSrvConfParamsDomainName_Type.__name__=_J
_RlDhcpSrvConfParamsDomainName_Object=MibTableColumn
rlDhcpSrvConfParamsDomainName=_RlDhcpSrvConfParamsDomainName_Object((1,3,6,1,4,1,89,38,47,1,8),_RlDhcpSrvConfParamsDomainName_Type())
rlDhcpSrvConfParamsDomainName.setMaxAccess(_B)
if mibBuilder.loadTexts:rlDhcpSrvConfParamsDomainName.setStatus(_A)
_RlDhcpSrvConfParamsNetbiosNameList_Type=DisplayString
_RlDhcpSrvConfParamsNetbiosNameList_Object=MibTableColumn
rlDhcpSrvConfParamsNetbiosNameList=_RlDhcpSrvConfParamsNetbiosNameList_Object((1,3,6,1,4,1,89,38,47,1,9),_RlDhcpSrvConfParamsNetbiosNameList_Type())
rlDhcpSrvConfParamsNetbiosNameList.setMaxAccess(_B)
if mibBuilder.loadTexts:rlDhcpSrvConfParamsNetbiosNameList.setStatus(_A)
class _RlDhcpSrvConfParamsNetbiosNodeType_Type(Integer32):defaultValue=8;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,4,8)));namedValues=NamedValues(*(('b-node',1),('p-node',2),('m-node',4),('h-node',8)))
_RlDhcpSrvConfParamsNetbiosNodeType_Type.__name__=_G
_RlDhcpSrvConfParamsNetbiosNodeType_Object=MibTableColumn
rlDhcpSrvConfParamsNetbiosNodeType=_RlDhcpSrvConfParamsNetbiosNodeType_Object((1,3,6,1,4,1,89,38,47,1,10),_RlDhcpSrvConfParamsNetbiosNodeType_Type())
rlDhcpSrvConfParamsNetbiosNodeType.setMaxAccess(_B)
if mibBuilder.loadTexts:rlDhcpSrvConfParamsNetbiosNodeType.setStatus(_A)
class _RlDhcpSrvConfParamsCommunity_Type(DisplayString):defaultValue=OctetString('public');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_RlDhcpSrvConfParamsCommunity_Type.__name__=_D
_RlDhcpSrvConfParamsCommunity_Object=MibTableColumn
rlDhcpSrvConfParamsCommunity=_RlDhcpSrvConfParamsCommunity_Object((1,3,6,1,4,1,89,38,47,1,11),_RlDhcpSrvConfParamsCommunity_Type())
rlDhcpSrvConfParamsCommunity.setMaxAccess(_B)
if mibBuilder.loadTexts:rlDhcpSrvConfParamsCommunity.setStatus(_I)
_RlDhcpSrvConfParamsNmsIp_Type=IpAddress
_RlDhcpSrvConfParamsNmsIp_Object=MibTableColumn
rlDhcpSrvConfParamsNmsIp=_RlDhcpSrvConfParamsNmsIp_Object((1,3,6,1,4,1,89,38,47,1,12),_RlDhcpSrvConfParamsNmsIp_Type())
rlDhcpSrvConfParamsNmsIp.setMaxAccess(_B)
if mibBuilder.loadTexts:rlDhcpSrvConfParamsNmsIp.setStatus(_I)
_RlDhcpSrvConfParamsOptionsList_Type=DisplayString
_RlDhcpSrvConfParamsOptionsList_Object=MibTableColumn
rlDhcpSrvConfParamsOptionsList=_RlDhcpSrvConfParamsOptionsList_Object((1,3,6,1,4,1,89,38,47,1,13),_RlDhcpSrvConfParamsOptionsList_Type())
rlDhcpSrvConfParamsOptionsList.setMaxAccess(_B)
if mibBuilder.loadTexts:rlDhcpSrvConfParamsOptionsList.setStatus(_I)
_RlDhcpSrvConfParamsRowStatus_Type=RowStatus
_RlDhcpSrvConfParamsRowStatus_Object=MibTableColumn
rlDhcpSrvConfParamsRowStatus=_RlDhcpSrvConfParamsRowStatus_Object((1,3,6,1,4,1,89,38,47,1,14),_RlDhcpSrvConfParamsRowStatus_Type())
rlDhcpSrvConfParamsRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:rlDhcpSrvConfParamsRowStatus.setStatus(_A)
class _RlDhcpSrvConfParamsAutoDefaultRouter_Type(TruthValue):defaultValue=1
_RlDhcpSrvConfParamsAutoDefaultRouter_Type.__name__=_H
_RlDhcpSrvConfParamsAutoDefaultRouter_Object=MibTableColumn
rlDhcpSrvConfParamsAutoDefaultRouter=_RlDhcpSrvConfParamsAutoDefaultRouter_Object((1,3,6,1,4,1,89,38,47,1,15),_RlDhcpSrvConfParamsAutoDefaultRouter_Type())
rlDhcpSrvConfParamsAutoDefaultRouter.setMaxAccess(_B)
if mibBuilder.loadTexts:rlDhcpSrvConfParamsAutoDefaultRouter.setStatus(_A)
_RlDhcpSrvNumOfNetworkPools_Type=Unsigned32
_RlDhcpSrvNumOfNetworkPools_Object=MibScalar
rlDhcpSrvNumOfNetworkPools=_RlDhcpSrvNumOfNetworkPools_Object((1,3,6,1,4,1,89,38,48),_RlDhcpSrvNumOfNetworkPools_Type())
rlDhcpSrvNumOfNetworkPools.setMaxAccess(_C)
if mibBuilder.loadTexts:rlDhcpSrvNumOfNetworkPools.setStatus(_A)
_RlDhcpSrvNumOfExcludedPools_Type=Unsigned32
_RlDhcpSrvNumOfExcludedPools_Object=MibScalar
rlDhcpSrvNumOfExcludedPools=_RlDhcpSrvNumOfExcludedPools_Object((1,3,6,1,4,1,89,38,49),_RlDhcpSrvNumOfExcludedPools_Type())
rlDhcpSrvNumOfExcludedPools.setMaxAccess(_C)
if mibBuilder.loadTexts:rlDhcpSrvNumOfExcludedPools.setStatus(_A)
_RlDhcpSrvNumOfHostPools_Type=Unsigned32
_RlDhcpSrvNumOfHostPools_Object=MibScalar
rlDhcpSrvNumOfHostPools=_RlDhcpSrvNumOfHostPools_Object((1,3,6,1,4,1,89,38,50),_RlDhcpSrvNumOfHostPools_Type())
rlDhcpSrvNumOfHostPools.setMaxAccess(_C)
if mibBuilder.loadTexts:rlDhcpSrvNumOfHostPools.setStatus(_A)
_RlDhcpSrvNumOfDynamicEntries_Type=Unsigned32
_RlDhcpSrvNumOfDynamicEntries_Object=MibScalar
rlDhcpSrvNumOfDynamicEntries=_RlDhcpSrvNumOfDynamicEntries_Object((1,3,6,1,4,1,89,38,51),_RlDhcpSrvNumOfDynamicEntries_Type())
rlDhcpSrvNumOfDynamicEntries.setMaxAccess(_C)
if mibBuilder.loadTexts:rlDhcpSrvNumOfDynamicEntries.setStatus(_A)
_RlDhcpSrvNumOfUsedEntries_Type=Unsigned32
_RlDhcpSrvNumOfUsedEntries_Object=MibScalar
rlDhcpSrvNumOfUsedEntries=_RlDhcpSrvNumOfUsedEntries_Object((1,3,6,1,4,1,89,38,52),_RlDhcpSrvNumOfUsedEntries_Type())
rlDhcpSrvNumOfUsedEntries.setMaxAccess(_C)
if mibBuilder.loadTexts:rlDhcpSrvNumOfUsedEntries.setStatus(_A)
_RlDhcpSrvNumOfPreAllocatedEntries_Type=Unsigned32
_RlDhcpSrvNumOfPreAllocatedEntries_Object=MibScalar
rlDhcpSrvNumOfPreAllocatedEntries=_RlDhcpSrvNumOfPreAllocatedEntries_Object((1,3,6,1,4,1,89,38,53),_RlDhcpSrvNumOfPreAllocatedEntries_Type())
rlDhcpSrvNumOfPreAllocatedEntries.setMaxAccess(_C)
if mibBuilder.loadTexts:rlDhcpSrvNumOfPreAllocatedEntries.setStatus(_A)
_RlDhcpSrvNumOfExpiredEntries_Type=Unsigned32
_RlDhcpSrvNumOfExpiredEntries_Object=MibScalar
rlDhcpSrvNumOfExpiredEntries=_RlDhcpSrvNumOfExpiredEntries_Object((1,3,6,1,4,1,89,38,54),_RlDhcpSrvNumOfExpiredEntries_Type())
rlDhcpSrvNumOfExpiredEntries.setMaxAccess(_C)
if mibBuilder.loadTexts:rlDhcpSrvNumOfExpiredEntries.setStatus(_A)
_RlDhcpSrvNumOfDeclinedEntries_Type=Unsigned32
_RlDhcpSrvNumOfDeclinedEntries_Object=MibScalar
rlDhcpSrvNumOfDeclinedEntries=_RlDhcpSrvNumOfDeclinedEntries_Object((1,3,6,1,4,1,89,38,55),_RlDhcpSrvNumOfDeclinedEntries_Type())
rlDhcpSrvNumOfDeclinedEntries.setMaxAccess(_C)
if mibBuilder.loadTexts:rlDhcpSrvNumOfDeclinedEntries.setStatus(_A)
_RlDhcpSrvNumOfAutomaticEntries_Type=Unsigned32
_RlDhcpSrvNumOfAutomaticEntries_Object=MibScalar
rlDhcpSrvNumOfAutomaticEntries=_RlDhcpSrvNumOfAutomaticEntries_Object((1,3,6,1,4,1,89,38,56),_RlDhcpSrvNumOfAutomaticEntries_Type())
rlDhcpSrvNumOfAutomaticEntries.setMaxAccess(_C)
if mibBuilder.loadTexts:rlDhcpSrvNumOfAutomaticEntries.setStatus(_A)
_RlDhcpSrvOptionParamsTable_Object=MibTable
rlDhcpSrvOptionParamsTable=_RlDhcpSrvOptionParamsTable_Object((1,3,6,1,4,1,89,38,57))
if mibBuilder.loadTexts:rlDhcpSrvOptionParamsTable.setStatus(_A)
_RlDhcpSrvOptionParamsEntry_Object=MibTableRow
rlDhcpSrvOptionParamsEntry=_RlDhcpSrvOptionParamsEntry_Object((1,3,6,1,4,1,89,38,57,1))
rlDhcpSrvOptionParamsEntry.setIndexNames((0,_E,_R),(0,_E,_S))
if mibBuilder.loadTexts:rlDhcpSrvOptionParamsEntry.setStatus(_A)
class _RlDhcpSrvOptionParamsName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_RlDhcpSrvOptionParamsName_Type.__name__=_D
_RlDhcpSrvOptionParamsName_Object=MibTableColumn
rlDhcpSrvOptionParamsName=_RlDhcpSrvOptionParamsName_Object((1,3,6,1,4,1,89,38,57,1,1),_RlDhcpSrvOptionParamsName_Type())
rlDhcpSrvOptionParamsName.setMaxAccess(_B)
if mibBuilder.loadTexts:rlDhcpSrvOptionParamsName.setStatus(_A)
class _RlDhcpSrvOptionParamsCode_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_RlDhcpSrvOptionParamsCode_Type.__name__=_F
_RlDhcpSrvOptionParamsCode_Object=MibTableColumn
rlDhcpSrvOptionParamsCode=_RlDhcpSrvOptionParamsCode_Object((1,3,6,1,4,1,89,38,57,1,2),_RlDhcpSrvOptionParamsCode_Type())
rlDhcpSrvOptionParamsCode.setMaxAccess(_B)
if mibBuilder.loadTexts:rlDhcpSrvOptionParamsCode.setStatus(_A)
_RlDhcpSrvOptionParamsType_Type=RlDhcpSrvOptionTypeEnum
_RlDhcpSrvOptionParamsType_Object=MibTableColumn
rlDhcpSrvOptionParamsType=_RlDhcpSrvOptionParamsType_Object((1,3,6,1,4,1,89,38,57,1,3),_RlDhcpSrvOptionParamsType_Type())
rlDhcpSrvOptionParamsType.setMaxAccess(_B)
if mibBuilder.loadTexts:rlDhcpSrvOptionParamsType.setStatus(_A)
_RlDhcpSrvOptionParamsOrigString_Type=OctetString
_RlDhcpSrvOptionParamsOrigString_Object=MibTableColumn
rlDhcpSrvOptionParamsOrigString=_RlDhcpSrvOptionParamsOrigString_Object((1,3,6,1,4,1,89,38,57,1,4),_RlDhcpSrvOptionParamsOrigString_Type())
rlDhcpSrvOptionParamsOrigString.setMaxAccess(_B)
if mibBuilder.loadTexts:rlDhcpSrvOptionParamsOrigString.setStatus(_A)
_RlDhcpSrvOptionParamsDescription_Type=DisplayString
_RlDhcpSrvOptionParamsDescription_Object=MibTableColumn
rlDhcpSrvOptionParamsDescription=_RlDhcpSrvOptionParamsDescription_Object((1,3,6,1,4,1,89,38,57,1,5),_RlDhcpSrvOptionParamsDescription_Type())
rlDhcpSrvOptionParamsDescription.setMaxAccess(_B)
if mibBuilder.loadTexts:rlDhcpSrvOptionParamsDescription.setStatus(_A)
_RlDhcpSrvOptionParamsRowStatus_Type=RowStatus
_RlDhcpSrvOptionParamsRowStatus_Object=MibTableColumn
rlDhcpSrvOptionParamsRowStatus=_RlDhcpSrvOptionParamsRowStatus_Object((1,3,6,1,4,1,89,38,57,1,6),_RlDhcpSrvOptionParamsRowStatus_Type())
rlDhcpSrvOptionParamsRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:rlDhcpSrvOptionParamsRowStatus.setStatus(_A)
_RlDhcpSrvAuxOptionTable_Object=MibTable
rlDhcpSrvAuxOptionTable=_RlDhcpSrvAuxOptionTable_Object((1,3,6,1,4,1,89,38,58))
if mibBuilder.loadTexts:rlDhcpSrvAuxOptionTable.setStatus(_A)
_RlDhcpSrvAuxOptionEntry_Object=MibTableRow
rlDhcpSrvAuxOptionEntry=_RlDhcpSrvAuxOptionEntry_Object((1,3,6,1,4,1,89,38,58,1))
rlDhcpSrvAuxOptionEntry.setIndexNames((0,_E,_T),(0,_E,_U))
if mibBuilder.loadTexts:rlDhcpSrvAuxOptionEntry.setStatus(_A)
class _RlDhcpSrvAuxOptionCode_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,254))
_RlDhcpSrvAuxOptionCode_Type.__name__=_F
_RlDhcpSrvAuxOptionCode_Object=MibTableColumn
rlDhcpSrvAuxOptionCode=_RlDhcpSrvAuxOptionCode_Object((1,3,6,1,4,1,89,38,58,1,1),_RlDhcpSrvAuxOptionCode_Type())
rlDhcpSrvAuxOptionCode.setMaxAccess(_C)
if mibBuilder.loadTexts:rlDhcpSrvAuxOptionCode.setStatus(_A)
_RlDhcpSrvAuxOptionType_Type=RlDhcpSrvOptionTypeEnum
_RlDhcpSrvAuxOptionType_Object=MibTableColumn
rlDhcpSrvAuxOptionType=_RlDhcpSrvAuxOptionType_Object((1,3,6,1,4,1,89,38,58,1,2),_RlDhcpSrvAuxOptionType_Type())
rlDhcpSrvAuxOptionType.setMaxAccess(_C)
if mibBuilder.loadTexts:rlDhcpSrvAuxOptionType.setStatus(_A)
_RlDhcpSrvAuxOptionMinVal_Type=Unsigned32
_RlDhcpSrvAuxOptionMinVal_Object=MibTableColumn
rlDhcpSrvAuxOptionMinVal=_RlDhcpSrvAuxOptionMinVal_Object((1,3,6,1,4,1,89,38,58,1,3),_RlDhcpSrvAuxOptionMinVal_Type())
rlDhcpSrvAuxOptionMinVal.setMaxAccess(_C)
if mibBuilder.loadTexts:rlDhcpSrvAuxOptionMinVal.setStatus(_A)
_RlDhcpSrvAuxOptionMaxVal_Type=Unsigned32
_RlDhcpSrvAuxOptionMaxVal_Object=MibTableColumn
rlDhcpSrvAuxOptionMaxVal=_RlDhcpSrvAuxOptionMaxVal_Object((1,3,6,1,4,1,89,38,58,1,4),_RlDhcpSrvAuxOptionMaxVal_Type())
rlDhcpSrvAuxOptionMaxVal.setMaxAccess(_C)
if mibBuilder.loadTexts:rlDhcpSrvAuxOptionMaxVal.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'RlDhcpSrvOptionTypeEnum':RlDhcpSrvOptionTypeEnum,'rsDHCP':rsDHCP,'rsDhcpMibVersion':rsDhcpMibVersion,'rlDhcpRelayMaximalNumberOfNonIpVlans':rlDhcpRelayMaximalNumberOfNonIpVlans,'rlDhcpRelayCurrentNumberOfNonIpVlans':rlDhcpRelayCurrentNumberOfNonIpVlans,'rlDhcpRelayEnable':rlDhcpRelayEnable,'rlDhcpRelayExists':rlDhcpRelayExists,'rlDhcpRelayNextServerTable':rlDhcpRelayNextServerTable,'rlDhcpRelayNextServerEntry':rlDhcpRelayNextServerEntry,_L:rlDhcpRelayNextServerIpAddr,'rlDhcpRelayNextServerSecThreshold':rlDhcpRelayNextServerSecThreshold,'rlDhcpRelayNextServerRowStatus':rlDhcpRelayNextServerRowStatus,'rlDhcpRelayInterfaceTable':rlDhcpRelayInterfaceTable,'rlDhcpRelayInterfaceEntry':rlDhcpRelayInterfaceEntry,_M:rlDhcpRelayInterfaceIfindex,'rlDhcpRelayInterfaceUseGiaddr':rlDhcpRelayInterfaceUseGiaddr,'rlDhcpRelayInterfaceRowStatus':rlDhcpRelayInterfaceRowStatus,'rlDhcpRelayInterfaceListTable':rlDhcpRelayInterfaceListTable,'rlDhcpRelayInterfaceListEntry':rlDhcpRelayInterfaceListEntry,_N:rlDhcpRelayInterfaceListIndex,'rlDhcpRelayInterfaceListPortList':rlDhcpRelayInterfaceListPortList,'rlDhcpRelayInterfaceListVlanId1To1024':rlDhcpRelayInterfaceListVlanId1To1024,'rlDhcpRelayInterfaceListVlanId1025To2048':rlDhcpRelayInterfaceListVlanId1025To2048,'rlDhcpRelayInterfaceListVlanId2049To3072':rlDhcpRelayInterfaceListVlanId2049To3072,'rlDhcpRelayInterfaceListVlanId3073To4094':rlDhcpRelayInterfaceListVlanId3073To4094,'rlDhcpSrvEnable':rlDhcpSrvEnable,'rlDhcpSrvExists':rlDhcpSrvExists,'rlDhcpSrvDbLocation':rlDhcpSrvDbLocation,'rlDhcpSrvMaxNumOfClients':rlDhcpSrvMaxNumOfClients,'rlDhcpSrvDbNumOfActiveEntries':rlDhcpSrvDbNumOfActiveEntries,'rlDhcpSrvDbErase':rlDhcpSrvDbErase,'rlDhcpSrvProbeEnable':rlDhcpSrvProbeEnable,'rlDhcpSrvProbeTimeout':rlDhcpSrvProbeTimeout,'rlDhcpSrvProbeRetries':rlDhcpSrvProbeRetries,'rlDhcpSrvDefaultNetworkPoolName':rlDhcpSrvDefaultNetworkPoolName,'rlDhcpSrvIpAddrTable':rlDhcpSrvIpAddrTable,'rlDhcpSrvIpAddrEntry':rlDhcpSrvIpAddrEntry,_O:rlDhcpSrvIpAddrIpAddr,'rlDhcpSrvIpAddrIpNetMask':rlDhcpSrvIpAddrIpNetMask,'rlDhcpSrvIpAddrIdentifier':rlDhcpSrvIpAddrIdentifier,'rlDhcpSrvIpAddrIdentifierType':rlDhcpSrvIpAddrIdentifierType,'rlDhcpSrvIpAddrClnHostName':rlDhcpSrvIpAddrClnHostName,'rlDhcpSrvIpAddrMechanism':rlDhcpSrvIpAddrMechanism,'rlDhcpSrvIpAddrAgeTime':rlDhcpSrvIpAddrAgeTime,'rlDhcpSrvIpAddrPoolName':rlDhcpSrvIpAddrPoolName,'rlDhcpSrvIpAddrConfParamsName':rlDhcpSrvIpAddrConfParamsName,'rlDhcpSrvIpAddrRowStatus':rlDhcpSrvIpAddrRowStatus,'rlDhcpSrvIpAddrLeaseTime':rlDhcpSrvIpAddrLeaseTime,'rlDhcpSrvIpAddrState':rlDhcpSrvIpAddrState,'rlDhcpSrvIpAddrOptionParamsName':rlDhcpSrvIpAddrOptionParamsName,'rlDhcpSrvDynamicTable':rlDhcpSrvDynamicTable,'rlDhcpSrvDynamicEntry':rlDhcpSrvDynamicEntry,_P:rlDhcpSrvDynamicPoolName,'rlDhcpSrvDynamicIpAddrFrom':rlDhcpSrvDynamicIpAddrFrom,'rlDhcpSrvDynamicIpAddrTo':rlDhcpSrvDynamicIpAddrTo,'rlDhcpSrvDynamicIpNetMask':rlDhcpSrvDynamicIpNetMask,'rlDhcpSrvDynamicLeaseTime':rlDhcpSrvDynamicLeaseTime,'rlDhcpSrvDynamicProbeEnable':rlDhcpSrvDynamicProbeEnable,'rlDhcpSrvDynamicTotalNumOfAddr':rlDhcpSrvDynamicTotalNumOfAddr,'rlDhcpSrvDynamicFreeNumOfAddr':rlDhcpSrvDynamicFreeNumOfAddr,'rlDhcpSrvDynamicConfParamsName':rlDhcpSrvDynamicConfParamsName,'rlDhcpSrvDynamicRowStatus':rlDhcpSrvDynamicRowStatus,'rlDhcpSrvDynamicAvailableNumOfAddr':rlDhcpSrvDynamicAvailableNumOfAddr,'rlDhcpSrvDynamicNumOfPreallocatedAddr':rlDhcpSrvDynamicNumOfPreallocatedAddr,'rlDhcpSrvDynamicNumOfValidAddr':rlDhcpSrvDynamicNumOfValidAddr,'rlDhcpSrvDynamicNumOfExpiredAddr':rlDhcpSrvDynamicNumOfExpiredAddr,'rlDhcpSrvDynamicNumOfDeclinedAddr':rlDhcpSrvDynamicNumOfDeclinedAddr,'rlDhcpSrvDynamicOptionParamsName':rlDhcpSrvDynamicOptionParamsName,'rlDhcpSrvConfParamsTable':rlDhcpSrvConfParamsTable,'rlDhcpSrvConfParamsEntry':rlDhcpSrvConfParamsEntry,_Q:rlDhcpSrvConfParamsName,'rlDhcpSrvConfParamsNextServerIp':rlDhcpSrvConfParamsNextServerIp,'rlDhcpSrvConfParamsNextServerName':rlDhcpSrvConfParamsNextServerName,'rlDhcpSrvConfParamsBootfileName':rlDhcpSrvConfParamsBootfileName,'rlDhcpSrvConfParamsRoutersList':rlDhcpSrvConfParamsRoutersList,'rlDhcpSrvConfParamsTimeSrvList':rlDhcpSrvConfParamsTimeSrvList,'rlDhcpSrvConfParamsDnsList':rlDhcpSrvConfParamsDnsList,'rlDhcpSrvConfParamsDomainName':rlDhcpSrvConfParamsDomainName,'rlDhcpSrvConfParamsNetbiosNameList':rlDhcpSrvConfParamsNetbiosNameList,'rlDhcpSrvConfParamsNetbiosNodeType':rlDhcpSrvConfParamsNetbiosNodeType,'rlDhcpSrvConfParamsCommunity':rlDhcpSrvConfParamsCommunity,'rlDhcpSrvConfParamsNmsIp':rlDhcpSrvConfParamsNmsIp,'rlDhcpSrvConfParamsOptionsList':rlDhcpSrvConfParamsOptionsList,'rlDhcpSrvConfParamsRowStatus':rlDhcpSrvConfParamsRowStatus,'rlDhcpSrvConfParamsAutoDefaultRouter':rlDhcpSrvConfParamsAutoDefaultRouter,'rlDhcpSrvNumOfNetworkPools':rlDhcpSrvNumOfNetworkPools,'rlDhcpSrvNumOfExcludedPools':rlDhcpSrvNumOfExcludedPools,'rlDhcpSrvNumOfHostPools':rlDhcpSrvNumOfHostPools,'rlDhcpSrvNumOfDynamicEntries':rlDhcpSrvNumOfDynamicEntries,'rlDhcpSrvNumOfUsedEntries':rlDhcpSrvNumOfUsedEntries,'rlDhcpSrvNumOfPreAllocatedEntries':rlDhcpSrvNumOfPreAllocatedEntries,'rlDhcpSrvNumOfExpiredEntries':rlDhcpSrvNumOfExpiredEntries,'rlDhcpSrvNumOfDeclinedEntries':rlDhcpSrvNumOfDeclinedEntries,'rlDhcpSrvNumOfAutomaticEntries':rlDhcpSrvNumOfAutomaticEntries,'rlDhcpSrvOptionParamsTable':rlDhcpSrvOptionParamsTable,'rlDhcpSrvOptionParamsEntry':rlDhcpSrvOptionParamsEntry,_R:rlDhcpSrvOptionParamsName,_S:rlDhcpSrvOptionParamsCode,'rlDhcpSrvOptionParamsType':rlDhcpSrvOptionParamsType,'rlDhcpSrvOptionParamsOrigString':rlDhcpSrvOptionParamsOrigString,'rlDhcpSrvOptionParamsDescription':rlDhcpSrvOptionParamsDescription,'rlDhcpSrvOptionParamsRowStatus':rlDhcpSrvOptionParamsRowStatus,'rlDhcpSrvAuxOptionTable':rlDhcpSrvAuxOptionTable,'rlDhcpSrvAuxOptionEntry':rlDhcpSrvAuxOptionEntry,_T:rlDhcpSrvAuxOptionCode,_U:rlDhcpSrvAuxOptionType,'rlDhcpSrvAuxOptionMinVal':rlDhcpSrvAuxOptionMinVal,'rlDhcpSrvAuxOptionMaxVal':rlDhcpSrvAuxOptionMaxVal})