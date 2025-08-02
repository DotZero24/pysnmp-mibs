_O='raisecomIgmpVlanCopyEgressPort'
_N='raisecomIgmpVlanCopyIpAddress'
_M='raisecomIgmpVlanCopyIpAddressType'
_L='raisecomIgmpVlanCopyMVlan'
_K='raisecomL2MulticastAddress'
_J='raisecomL2MulticastMVlan'
_I='read-write'
_H='EnableVar'
_G='InetAddress'
_F='read-create'
_E='Integer32'
_D='not-accessible'
_C='read-only'
_B='RAISECOM-MCAST-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB',_G,'InetAddressType')
VlanId,VlanIndex=mibBuilder.importSymbols('Q-BRIDGE-MIB','VlanId','VlanIndex')
raisecomAgent,=mibBuilder.importSymbols('RAISECOM-BASE-MIB','raisecomAgent')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention')
EnableVar,PortList,Vlanset=mibBuilder.importSymbols('SWITCH-TC',_H,'PortList','Vlanset')
raisecomMcast=ModuleIdentity((1,3,6,1,4,1,8886,1,27))
if mibBuilder.loadTexts:raisecomMcast.setRevisions(('2010-10-29 00:00',))
_RaisecomMcastNotifications_ObjectIdentity=ObjectIdentity
raisecomMcastNotifications=_RaisecomMcastNotifications_ObjectIdentity((1,3,6,1,4,1,8886,1,27,1))
_RaisecomMcastObjects_ObjectIdentity=ObjectIdentity
raisecomMcastObjects=_RaisecomMcastObjects_ObjectIdentity((1,3,6,1,4,1,8886,1,27,2))
_RaisecomMcastScalar_ObjectIdentity=ObjectIdentity
raisecomMcastScalar=_RaisecomMcastScalar_ObjectIdentity((1,3,6,1,4,1,8886,1,27,2,1))
class _RaisecomMulticastFilterEnable_Type(EnableVar):defaultValue=2
_RaisecomMulticastFilterEnable_Type.__name__=_H
_RaisecomMulticastFilterEnable_Object=MibScalar
raisecomMulticastFilterEnable=_RaisecomMulticastFilterEnable_Object((1,3,6,1,4,1,8886,1,27,2,1,1),_RaisecomMulticastFilterEnable_Type())
raisecomMulticastFilterEnable.setMaxAccess(_I)
if mibBuilder.loadTexts:raisecomMulticastFilterEnable.setStatus(_A)
_RaisecomMulticastFilterVlanlist_Type=Vlanset
_RaisecomMulticastFilterVlanlist_Object=MibScalar
raisecomMulticastFilterVlanlist=_RaisecomMulticastFilterVlanlist_Object((1,3,6,1,4,1,8886,1,27,2,1,2),_RaisecomMulticastFilterVlanlist_Type())
raisecomMulticastFilterVlanlist.setMaxAccess(_I)
if mibBuilder.loadTexts:raisecomMulticastFilterVlanlist.setStatus(_A)
_RaisecomMcastL2_ObjectIdentity=ObjectIdentity
raisecomMcastL2=_RaisecomMcastL2_ObjectIdentity((1,3,6,1,4,1,8886,1,27,2,2))
class _RaisecomL2MulticastMaxGroupNum_Type(Integer32):defaultValue=0
_RaisecomL2MulticastMaxGroupNum_Type.__name__=_E
_RaisecomL2MulticastMaxGroupNum_Object=MibScalar
raisecomL2MulticastMaxGroupNum=_RaisecomL2MulticastMaxGroupNum_Object((1,3,6,1,4,1,8886,1,27,2,2,1),_RaisecomL2MulticastMaxGroupNum_Type())
raisecomL2MulticastMaxGroupNum.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomL2MulticastMaxGroupNum.setStatus(_A)
class _RaisecomL2MulticastCurrentGroupNum_Type(Integer32):defaultValue=0
_RaisecomL2MulticastCurrentGroupNum_Type.__name__=_E
_RaisecomL2MulticastCurrentGroupNum_Object=MibScalar
raisecomL2MulticastCurrentGroupNum=_RaisecomL2MulticastCurrentGroupNum_Object((1,3,6,1,4,1,8886,1,27,2,2,2),_RaisecomL2MulticastCurrentGroupNum_Type())
raisecomL2MulticastCurrentGroupNum.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomL2MulticastCurrentGroupNum.setStatus(_A)
_RaisecomL2MulticastAddressTable_Object=MibTable
raisecomL2MulticastAddressTable=_RaisecomL2MulticastAddressTable_Object((1,3,6,1,4,1,8886,1,27,2,2,3))
if mibBuilder.loadTexts:raisecomL2MulticastAddressTable.setStatus(_A)
_RaisecomL2MulticastAddressEntry_Object=MibTableRow
raisecomL2MulticastAddressEntry=_RaisecomL2MulticastAddressEntry_Object((1,3,6,1,4,1,8886,1,27,2,2,3,1))
raisecomL2MulticastAddressEntry.setIndexNames((0,_B,_J),(0,_B,_K))
if mibBuilder.loadTexts:raisecomL2MulticastAddressEntry.setStatus(_A)
_RaisecomL2MulticastMVlan_Type=Integer32
_RaisecomL2MulticastMVlan_Object=MibTableColumn
raisecomL2MulticastMVlan=_RaisecomL2MulticastMVlan_Object((1,3,6,1,4,1,8886,1,27,2,2,3,1,1),_RaisecomL2MulticastMVlan_Type())
raisecomL2MulticastMVlan.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomL2MulticastMVlan.setStatus(_A)
_RaisecomL2MulticastAddress_Type=MacAddress
_RaisecomL2MulticastAddress_Object=MibTableColumn
raisecomL2MulticastAddress=_RaisecomL2MulticastAddress_Object((1,3,6,1,4,1,8886,1,27,2,2,3,1,2),_RaisecomL2MulticastAddress_Type())
raisecomL2MulticastAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomL2MulticastAddress.setStatus(_A)
_RaisecomL2MulticastEgressPortlist_Type=PortList
_RaisecomL2MulticastEgressPortlist_Object=MibTableColumn
raisecomL2MulticastEgressPortlist=_RaisecomL2MulticastEgressPortlist_Object((1,3,6,1,4,1,8886,1,27,2,2,3,1,3),_RaisecomL2MulticastEgressPortlist_Type())
raisecomL2MulticastEgressPortlist.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomL2MulticastEgressPortlist.setStatus(_A)
_RaisecomL2MulticastStaticPortlist_Type=PortList
_RaisecomL2MulticastStaticPortlist_Object=MibTableColumn
raisecomL2MulticastStaticPortlist=_RaisecomL2MulticastStaticPortlist_Object((1,3,6,1,4,1,8886,1,27,2,2,3,1,4),_RaisecomL2MulticastStaticPortlist_Type())
raisecomL2MulticastStaticPortlist.setMaxAccess(_F)
if mibBuilder.loadTexts:raisecomL2MulticastStaticPortlist.setStatus(_A)
_RaisecomL2MulticastRowStatus_Type=RowStatus
_RaisecomL2MulticastRowStatus_Object=MibTableColumn
raisecomL2MulticastRowStatus=_RaisecomL2MulticastRowStatus_Object((1,3,6,1,4,1,8886,1,27,2,2,3,1,5),_RaisecomL2MulticastRowStatus_Type())
raisecomL2MulticastRowStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:raisecomL2MulticastRowStatus.setStatus(_A)
_RaisecomMcastVlanCopy_ObjectIdentity=ObjectIdentity
raisecomMcastVlanCopy=_RaisecomMcastVlanCopy_ObjectIdentity((1,3,6,1,4,1,8886,1,27,2,3))
class _RaisecomIgmpVlanCopyMaxGroupNum_Type(Integer32):defaultValue=0
_RaisecomIgmpVlanCopyMaxGroupNum_Type.__name__=_E
_RaisecomIgmpVlanCopyMaxGroupNum_Object=MibScalar
raisecomIgmpVlanCopyMaxGroupNum=_RaisecomIgmpVlanCopyMaxGroupNum_Object((1,3,6,1,4,1,8886,1,27,2,3,1),_RaisecomIgmpVlanCopyMaxGroupNum_Type())
raisecomIgmpVlanCopyMaxGroupNum.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomIgmpVlanCopyMaxGroupNum.setStatus(_A)
class _RaisecomIgmpVlanCopyCurrentGroupNum_Type(Integer32):defaultValue=0
_RaisecomIgmpVlanCopyCurrentGroupNum_Type.__name__=_E
_RaisecomIgmpVlanCopyCurrentGroupNum_Object=MibScalar
raisecomIgmpVlanCopyCurrentGroupNum=_RaisecomIgmpVlanCopyCurrentGroupNum_Object((1,3,6,1,4,1,8886,1,27,2,3,2),_RaisecomIgmpVlanCopyCurrentGroupNum_Type())
raisecomIgmpVlanCopyCurrentGroupNum.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomIgmpVlanCopyCurrentGroupNum.setStatus(_A)
_RaisecomIgmpVlanCopyAddressTable_Object=MibTable
raisecomIgmpVlanCopyAddressTable=_RaisecomIgmpVlanCopyAddressTable_Object((1,3,6,1,4,1,8886,1,27,2,3,3))
if mibBuilder.loadTexts:raisecomIgmpVlanCopyAddressTable.setStatus(_A)
_RaisecomIgmpVlanCopyAddressEntry_Object=MibTableRow
raisecomIgmpVlanCopyAddressEntry=_RaisecomIgmpVlanCopyAddressEntry_Object((1,3,6,1,4,1,8886,1,27,2,3,3,1))
raisecomIgmpVlanCopyAddressEntry.setIndexNames((0,_B,_L),(0,_B,_M),(0,_B,_N),(0,_B,_O))
if mibBuilder.loadTexts:raisecomIgmpVlanCopyAddressEntry.setStatus(_A)
_RaisecomIgmpVlanCopyMVlan_Type=VlanIndex
_RaisecomIgmpVlanCopyMVlan_Object=MibTableColumn
raisecomIgmpVlanCopyMVlan=_RaisecomIgmpVlanCopyMVlan_Object((1,3,6,1,4,1,8886,1,27,2,3,3,1,1),_RaisecomIgmpVlanCopyMVlan_Type())
raisecomIgmpVlanCopyMVlan.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomIgmpVlanCopyMVlan.setStatus(_A)
_RaisecomIgmpVlanCopyIpAddressType_Type=InetAddressType
_RaisecomIgmpVlanCopyIpAddressType_Object=MibTableColumn
raisecomIgmpVlanCopyIpAddressType=_RaisecomIgmpVlanCopyIpAddressType_Object((1,3,6,1,4,1,8886,1,27,2,3,3,1,2),_RaisecomIgmpVlanCopyIpAddressType_Type())
raisecomIgmpVlanCopyIpAddressType.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomIgmpVlanCopyIpAddressType.setStatus(_A)
class _RaisecomIgmpVlanCopyIpAddress_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_RaisecomIgmpVlanCopyIpAddress_Type.__name__=_G
_RaisecomIgmpVlanCopyIpAddress_Object=MibTableColumn
raisecomIgmpVlanCopyIpAddress=_RaisecomIgmpVlanCopyIpAddress_Object((1,3,6,1,4,1,8886,1,27,2,3,3,1,3),_RaisecomIgmpVlanCopyIpAddress_Type())
raisecomIgmpVlanCopyIpAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomIgmpVlanCopyIpAddress.setStatus(_A)
_RaisecomIgmpVlanCopyEgressPort_Type=Integer32
_RaisecomIgmpVlanCopyEgressPort_Object=MibTableColumn
raisecomIgmpVlanCopyEgressPort=_RaisecomIgmpVlanCopyEgressPort_Object((1,3,6,1,4,1,8886,1,27,2,3,3,1,4),_RaisecomIgmpVlanCopyEgressPort_Type())
raisecomIgmpVlanCopyEgressPort.setMaxAccess(_D)
if mibBuilder.loadTexts:raisecomIgmpVlanCopyEgressPort.setStatus(_A)
_RaisecomIgmpVlanCopyUVlanList_Type=Vlanset
_RaisecomIgmpVlanCopyUVlanList_Object=MibTableColumn
raisecomIgmpVlanCopyUVlanList=_RaisecomIgmpVlanCopyUVlanList_Object((1,3,6,1,4,1,8886,1,27,2,3,3,1,5),_RaisecomIgmpVlanCopyUVlanList_Type())
raisecomIgmpVlanCopyUVlanList.setMaxAccess(_C)
if mibBuilder.loadTexts:raisecomIgmpVlanCopyUVlanList.setStatus(_A)
_RaisecomIgmpVlanCopyStaticFlagList_Type=Vlanset
_RaisecomIgmpVlanCopyStaticFlagList_Object=MibTableColumn
raisecomIgmpVlanCopyStaticFlagList=_RaisecomIgmpVlanCopyStaticFlagList_Object((1,3,6,1,4,1,8886,1,27,2,3,3,1,6),_RaisecomIgmpVlanCopyStaticFlagList_Type())
raisecomIgmpVlanCopyStaticFlagList.setMaxAccess(_F)
if mibBuilder.loadTexts:raisecomIgmpVlanCopyStaticFlagList.setStatus(_A)
_RaisecomIgmpVlanCopyRowStatus_Type=RowStatus
_RaisecomIgmpVlanCopyRowStatus_Object=MibTableColumn
raisecomIgmpVlanCopyRowStatus=_RaisecomIgmpVlanCopyRowStatus_Object((1,3,6,1,4,1,8886,1,27,2,3,3,1,7),_RaisecomIgmpVlanCopyRowStatus_Type())
raisecomIgmpVlanCopyRowStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:raisecomIgmpVlanCopyRowStatus.setStatus(_A)
_RaisecomMcastConformance_ObjectIdentity=ObjectIdentity
raisecomMcastConformance=_RaisecomMcastConformance_ObjectIdentity((1,3,6,1,4,1,8886,1,27,3))
mibBuilder.exportSymbols(_B,**{'raisecomMcast':raisecomMcast,'raisecomMcastNotifications':raisecomMcastNotifications,'raisecomMcastObjects':raisecomMcastObjects,'raisecomMcastScalar':raisecomMcastScalar,'raisecomMulticastFilterEnable':raisecomMulticastFilterEnable,'raisecomMulticastFilterVlanlist':raisecomMulticastFilterVlanlist,'raisecomMcastL2':raisecomMcastL2,'raisecomL2MulticastMaxGroupNum':raisecomL2MulticastMaxGroupNum,'raisecomL2MulticastCurrentGroupNum':raisecomL2MulticastCurrentGroupNum,'raisecomL2MulticastAddressTable':raisecomL2MulticastAddressTable,'raisecomL2MulticastAddressEntry':raisecomL2MulticastAddressEntry,_J:raisecomL2MulticastMVlan,_K:raisecomL2MulticastAddress,'raisecomL2MulticastEgressPortlist':raisecomL2MulticastEgressPortlist,'raisecomL2MulticastStaticPortlist':raisecomL2MulticastStaticPortlist,'raisecomL2MulticastRowStatus':raisecomL2MulticastRowStatus,'raisecomMcastVlanCopy':raisecomMcastVlanCopy,'raisecomIgmpVlanCopyMaxGroupNum':raisecomIgmpVlanCopyMaxGroupNum,'raisecomIgmpVlanCopyCurrentGroupNum':raisecomIgmpVlanCopyCurrentGroupNum,'raisecomIgmpVlanCopyAddressTable':raisecomIgmpVlanCopyAddressTable,'raisecomIgmpVlanCopyAddressEntry':raisecomIgmpVlanCopyAddressEntry,_L:raisecomIgmpVlanCopyMVlan,_M:raisecomIgmpVlanCopyIpAddressType,_N:raisecomIgmpVlanCopyIpAddress,_O:raisecomIgmpVlanCopyEgressPort,'raisecomIgmpVlanCopyUVlanList':raisecomIgmpVlanCopyUVlanList,'raisecomIgmpVlanCopyStaticFlagList':raisecomIgmpVlanCopyStaticFlagList,'raisecomIgmpVlanCopyRowStatus':raisecomIgmpVlanCopyRowStatus,'raisecomMcastConformance':raisecomMcastConformance})