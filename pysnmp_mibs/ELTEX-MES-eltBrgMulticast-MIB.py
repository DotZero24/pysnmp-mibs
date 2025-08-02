_S='eltIgmpMldSnoopVlanEntry'
_R='eltPimSnoopVlanStatisticVlanTag'
_Q='eltPimSnoopNeighborIpAddress'
_P='eltPimSnoopNeighborIpAddressType'
_O='eltPimSnoopNeighborVlanTag'
_N='eltPimSnoopMembershipOutgoingPort'
_M='eltPimSnoopMembershipSourceIpAddress'
_L='eltPimSnoopMembershipSourceIpAddressType'
_K='eltPimSnoopMembershipGroupIpAddress'
_J='eltPimSnoopMembershipGroupIpAddressType'
_I='eltPimSnoopMembershipVlanTag'
_H='eltPimSnoopVlanConfigVlanTag'
_G='Integer32'
_F='OctetString'
_E='TruthValue'
_D='ELTEX-MES-eltBrgMulticast-MIB'
_C='read-write'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_F,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
eltMesMacMulticast,=mibBuilder.importSymbols('ELTEX-MES','eltMesMacMulticast')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
PortList,VlanIndex=mibBuilder.importSymbols('Q-BRIDGE-MIB','PortList','VlanIndex')
rlIgmpMldSnoopVlanEntry,=mibBuilder.importSymbols('RADLAN-rlMacMulticast-MIB','rlIgmpMldSnoopVlanEntry')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_G,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention',_E)
_EltMesMacMulticastFilter_ObjectIdentity=ObjectIdentity
eltMesMacMulticastFilter=_EltMesMacMulticastFilter_ObjectIdentity((1,3,6,1,4,1,35265,1,23,55,1))
_EltMesMacMulticastFilterPerVlan_ObjectIdentity=ObjectIdentity
eltMesMacMulticastFilterPerVlan=_EltMesMacMulticastFilterPerVlan_ObjectIdentity((1,3,6,1,4,1,35265,1,23,55,1,1))
class _EltMacMulticastUnregFilterEnableVlanId1To1024_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_EltMacMulticastUnregFilterEnableVlanId1To1024_Type.__name__=_F
_EltMacMulticastUnregFilterEnableVlanId1To1024_Object=MibScalar
eltMacMulticastUnregFilterEnableVlanId1To1024=_EltMacMulticastUnregFilterEnableVlanId1To1024_Object((1,3,6,1,4,1,35265,1,23,55,1,1,1),_EltMacMulticastUnregFilterEnableVlanId1To1024_Type())
eltMacMulticastUnregFilterEnableVlanId1To1024.setMaxAccess(_C)
if mibBuilder.loadTexts:eltMacMulticastUnregFilterEnableVlanId1To1024.setStatus(_A)
class _EltMacMulticastUnregFilterEnableVlanId1025To2048_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_EltMacMulticastUnregFilterEnableVlanId1025To2048_Type.__name__=_F
_EltMacMulticastUnregFilterEnableVlanId1025To2048_Object=MibScalar
eltMacMulticastUnregFilterEnableVlanId1025To2048=_EltMacMulticastUnregFilterEnableVlanId1025To2048_Object((1,3,6,1,4,1,35265,1,23,55,1,1,2),_EltMacMulticastUnregFilterEnableVlanId1025To2048_Type())
eltMacMulticastUnregFilterEnableVlanId1025To2048.setMaxAccess(_C)
if mibBuilder.loadTexts:eltMacMulticastUnregFilterEnableVlanId1025To2048.setStatus(_A)
class _EltMacMulticastUnregFilterEnableVlanId2049To3072_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_EltMacMulticastUnregFilterEnableVlanId2049To3072_Type.__name__=_F
_EltMacMulticastUnregFilterEnableVlanId2049To3072_Object=MibScalar
eltMacMulticastUnregFilterEnableVlanId2049To3072=_EltMacMulticastUnregFilterEnableVlanId2049To3072_Object((1,3,6,1,4,1,35265,1,23,55,1,1,3),_EltMacMulticastUnregFilterEnableVlanId2049To3072_Type())
eltMacMulticastUnregFilterEnableVlanId2049To3072.setMaxAccess(_C)
if mibBuilder.loadTexts:eltMacMulticastUnregFilterEnableVlanId2049To3072.setStatus(_A)
class _EltMacMulticastUnregFilterEnableVlanId3073To4094_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_EltMacMulticastUnregFilterEnableVlanId3073To4094_Type.__name__=_F
_EltMacMulticastUnregFilterEnableVlanId3073To4094_Object=MibScalar
eltMacMulticastUnregFilterEnableVlanId3073To4094=_EltMacMulticastUnregFilterEnableVlanId3073To4094_Object((1,3,6,1,4,1,35265,1,23,55,1,1,4),_EltMacMulticastUnregFilterEnableVlanId3073To4094_Type())
eltMacMulticastUnregFilterEnableVlanId3073To4094.setMaxAccess(_C)
if mibBuilder.loadTexts:eltMacMulticastUnregFilterEnableVlanId3073To4094.setStatus(_A)
_EltMesMldSnoop_ObjectIdentity=ObjectIdentity
eltMesMldSnoop=_EltMesMldSnoop_ObjectIdentity((1,3,6,1,4,1,35265,1,23,55,5))
_EltIgmpMldSnoopVlanTable_Object=MibTable
eltIgmpMldSnoopVlanTable=_EltIgmpMldSnoopVlanTable_Object((1,3,6,1,4,1,35265,1,23,55,5,5))
if mibBuilder.loadTexts:eltIgmpMldSnoopVlanTable.setStatus(_A)
_EltIgmpMldSnoopVlanEntry_Object=MibTableRow
eltIgmpMldSnoopVlanEntry=_EltIgmpMldSnoopVlanEntry_Object((1,3,6,1,4,1,35265,1,23,55,5,5,1))
if mibBuilder.loadTexts:eltIgmpMldSnoopVlanEntry.setStatus(_A)
class _EltIgmpMldSnoopVlanIsImmediateLeaveHostBased_Type(TruthValue):defaultValue=2
_EltIgmpMldSnoopVlanIsImmediateLeaveHostBased_Type.__name__=_E
_EltIgmpMldSnoopVlanIsImmediateLeaveHostBased_Object=MibTableColumn
eltIgmpMldSnoopVlanIsImmediateLeaveHostBased=_EltIgmpMldSnoopVlanIsImmediateLeaveHostBased_Object((1,3,6,1,4,1,35265,1,23,55,5,5,1,1),_EltIgmpMldSnoopVlanIsImmediateLeaveHostBased_Type())
eltIgmpMldSnoopVlanIsImmediateLeaveHostBased.setMaxAccess(_C)
if mibBuilder.loadTexts:eltIgmpMldSnoopVlanIsImmediateLeaveHostBased.setStatus(_A)
class _EltIgmpMldSnoopVlanCos_Type(Integer32):defaultValue=255;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7),ValueRangeConstraint(255,255))
_EltIgmpMldSnoopVlanCos_Type.__name__=_G
_EltIgmpMldSnoopVlanCos_Object=MibTableColumn
eltIgmpMldSnoopVlanCos=_EltIgmpMldSnoopVlanCos_Object((1,3,6,1,4,1,35265,1,23,55,5,5,1,2),_EltIgmpMldSnoopVlanCos_Type())
eltIgmpMldSnoopVlanCos.setMaxAccess(_C)
if mibBuilder.loadTexts:eltIgmpMldSnoopVlanCos.setStatus(_A)
_EltIgmpMldSnoopVlanReplaceSourceIp_Type=InetAddress
_EltIgmpMldSnoopVlanReplaceSourceIp_Object=MibTableColumn
eltIgmpMldSnoopVlanReplaceSourceIp=_EltIgmpMldSnoopVlanReplaceSourceIp_Object((1,3,6,1,4,1,35265,1,23,55,5,5,1,3),_EltIgmpMldSnoopVlanReplaceSourceIp_Type())
eltIgmpMldSnoopVlanReplaceSourceIp.setMaxAccess(_C)
if mibBuilder.loadTexts:eltIgmpMldSnoopVlanReplaceSourceIp.setStatus(_A)
class _EltIgmpMldSnoopVlanProxyReportEnable_Type(TruthValue):defaultValue=2
_EltIgmpMldSnoopVlanProxyReportEnable_Type.__name__=_E
_EltIgmpMldSnoopVlanProxyReportEnable_Object=MibTableColumn
eltIgmpMldSnoopVlanProxyReportEnable=_EltIgmpMldSnoopVlanProxyReportEnable_Object((1,3,6,1,4,1,35265,1,23,55,5,5,1,4),_EltIgmpMldSnoopVlanProxyReportEnable_Type())
eltIgmpMldSnoopVlanProxyReportEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:eltIgmpMldSnoopVlanProxyReportEnable.setStatus(_A)
class _EltIgmpMldSnoopVlanProxyReportVersion_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_EltIgmpMldSnoopVlanProxyReportVersion_Type.__name__=_G
_EltIgmpMldSnoopVlanProxyReportVersion_Object=MibTableColumn
eltIgmpMldSnoopVlanProxyReportVersion=_EltIgmpMldSnoopVlanProxyReportVersion_Object((1,3,6,1,4,1,35265,1,23,55,5,5,1,5),_EltIgmpMldSnoopVlanProxyReportVersion_Type())
eltIgmpMldSnoopVlanProxyReportVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:eltIgmpMldSnoopVlanProxyReportVersion.setStatus(_A)
class _EltIgmpMldSnoopVlanGsqSuppress_Type(TruthValue):defaultValue=2
_EltIgmpMldSnoopVlanGsqSuppress_Type.__name__=_E
_EltIgmpMldSnoopVlanGsqSuppress_Object=MibTableColumn
eltIgmpMldSnoopVlanGsqSuppress=_EltIgmpMldSnoopVlanGsqSuppress_Object((1,3,6,1,4,1,35265,1,23,55,5,5,1,6),_EltIgmpMldSnoopVlanGsqSuppress_Type())
eltIgmpMldSnoopVlanGsqSuppress.setMaxAccess(_C)
if mibBuilder.loadTexts:eltIgmpMldSnoopVlanGsqSuppress.setStatus(_A)
_EltIgmpMldSnoopVlanImmediateLeavePortlist_Type=PortList
_EltIgmpMldSnoopVlanImmediateLeavePortlist_Object=MibTableColumn
eltIgmpMldSnoopVlanImmediateLeavePortlist=_EltIgmpMldSnoopVlanImmediateLeavePortlist_Object((1,3,6,1,4,1,35265,1,23,55,5,5,1,7),_EltIgmpMldSnoopVlanImmediateLeavePortlist_Type())
eltIgmpMldSnoopVlanImmediateLeavePortlist.setMaxAccess(_C)
if mibBuilder.loadTexts:eltIgmpMldSnoopVlanImmediateLeavePortlist.setStatus(_A)
_EltIgmpMldSnoopVlanHostBasedPortlist_Type=PortList
_EltIgmpMldSnoopVlanHostBasedPortlist_Object=MibTableColumn
eltIgmpMldSnoopVlanHostBasedPortlist=_EltIgmpMldSnoopVlanHostBasedPortlist_Object((1,3,6,1,4,1,35265,1,23,55,5,5,1,8),_EltIgmpMldSnoopVlanHostBasedPortlist_Type())
eltIgmpMldSnoopVlanHostBasedPortlist.setMaxAccess(_C)
if mibBuilder.loadTexts:eltIgmpMldSnoopVlanHostBasedPortlist.setStatus(_A)
_EltMesPimSnoop_ObjectIdentity=ObjectIdentity
eltMesPimSnoop=_EltMesPimSnoop_ObjectIdentity((1,3,6,1,4,1,35265,1,23,55,6))
_EltMesPimSnoopObjects_ObjectIdentity=ObjectIdentity
eltMesPimSnoopObjects=_EltMesPimSnoopObjects_ObjectIdentity((1,3,6,1,4,1,35265,1,23,55,6,1))
_EltMesPimSnoopGlobals_ObjectIdentity=ObjectIdentity
eltMesPimSnoopGlobals=_EltMesPimSnoopGlobals_ObjectIdentity((1,3,6,1,4,1,35265,1,23,55,6,1,1))
class _EltPimSnoopEnable_Type(TruthValue):defaultValue=2
_EltPimSnoopEnable_Type.__name__=_E
_EltPimSnoopEnable_Object=MibScalar
eltPimSnoopEnable=_EltPimSnoopEnable_Object((1,3,6,1,4,1,35265,1,23,55,6,1,1,1),_EltPimSnoopEnable_Type())
eltPimSnoopEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:eltPimSnoopEnable.setStatus(_A)
_EltMesPimSnoopConfigs_ObjectIdentity=ObjectIdentity
eltMesPimSnoopConfigs=_EltMesPimSnoopConfigs_ObjectIdentity((1,3,6,1,4,1,35265,1,23,55,6,1,2))
_EltPimSnoopVlanConfigTable_Object=MibTable
eltPimSnoopVlanConfigTable=_EltPimSnoopVlanConfigTable_Object((1,3,6,1,4,1,35265,1,23,55,6,1,2,1))
if mibBuilder.loadTexts:eltPimSnoopVlanConfigTable.setStatus(_A)
_EltPimSnoopVlanConfigEntry_Object=MibTableRow
eltPimSnoopVlanConfigEntry=_EltPimSnoopVlanConfigEntry_Object((1,3,6,1,4,1,35265,1,23,55,6,1,2,1,1))
eltPimSnoopVlanConfigEntry.setIndexNames((0,_D,_H))
if mibBuilder.loadTexts:eltPimSnoopVlanConfigEntry.setStatus(_A)
_EltPimSnoopVlanConfigVlanTag_Type=VlanIndex
_EltPimSnoopVlanConfigVlanTag_Object=MibTableColumn
eltPimSnoopVlanConfigVlanTag=_EltPimSnoopVlanConfigVlanTag_Object((1,3,6,1,4,1,35265,1,23,55,6,1,2,1,1,1),_EltPimSnoopVlanConfigVlanTag_Type())
eltPimSnoopVlanConfigVlanTag.setMaxAccess(_B)
if mibBuilder.loadTexts:eltPimSnoopVlanConfigVlanTag.setStatus(_A)
class _EltPimSnoopVlanConfigEnable_Type(TruthValue):defaultValue=2
_EltPimSnoopVlanConfigEnable_Type.__name__=_E
_EltPimSnoopVlanConfigEnable_Object=MibTableColumn
eltPimSnoopVlanConfigEnable=_EltPimSnoopVlanConfigEnable_Object((1,3,6,1,4,1,35265,1,23,55,6,1,2,1,1,2),_EltPimSnoopVlanConfigEnable_Type())
eltPimSnoopVlanConfigEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:eltPimSnoopVlanConfigEnable.setStatus(_A)
_EltMesPimSnoopStatictics_ObjectIdentity=ObjectIdentity
eltMesPimSnoopStatictics=_EltMesPimSnoopStatictics_ObjectIdentity((1,3,6,1,4,1,35265,1,23,55,6,1,3))
_EltPimSnoopMembershipTable_Object=MibTable
eltPimSnoopMembershipTable=_EltPimSnoopMembershipTable_Object((1,3,6,1,4,1,35265,1,23,55,6,1,3,1))
if mibBuilder.loadTexts:eltPimSnoopMembershipTable.setStatus(_A)
_EltPimSnoopMembershipEntry_Object=MibTableRow
eltPimSnoopMembershipEntry=_EltPimSnoopMembershipEntry_Object((1,3,6,1,4,1,35265,1,23,55,6,1,3,1,1))
eltPimSnoopMembershipEntry.setIndexNames((0,_D,_I),(0,_D,_J),(0,_D,_K),(0,_D,_L),(0,_D,_M),(0,_D,_N))
if mibBuilder.loadTexts:eltPimSnoopMembershipEntry.setStatus(_A)
_EltPimSnoopMembershipVlanTag_Type=VlanIndex
_EltPimSnoopMembershipVlanTag_Object=MibTableColumn
eltPimSnoopMembershipVlanTag=_EltPimSnoopMembershipVlanTag_Object((1,3,6,1,4,1,35265,1,23,55,6,1,3,1,1,1),_EltPimSnoopMembershipVlanTag_Type())
eltPimSnoopMembershipVlanTag.setMaxAccess(_B)
if mibBuilder.loadTexts:eltPimSnoopMembershipVlanTag.setStatus(_A)
_EltPimSnoopMembershipGroupIpAddressType_Type=InetAddressType
_EltPimSnoopMembershipGroupIpAddressType_Object=MibTableColumn
eltPimSnoopMembershipGroupIpAddressType=_EltPimSnoopMembershipGroupIpAddressType_Object((1,3,6,1,4,1,35265,1,23,55,6,1,3,1,1,2),_EltPimSnoopMembershipGroupIpAddressType_Type())
eltPimSnoopMembershipGroupIpAddressType.setMaxAccess(_B)
if mibBuilder.loadTexts:eltPimSnoopMembershipGroupIpAddressType.setStatus(_A)
_EltPimSnoopMembershipGroupIpAddress_Type=InetAddress
_EltPimSnoopMembershipGroupIpAddress_Object=MibTableColumn
eltPimSnoopMembershipGroupIpAddress=_EltPimSnoopMembershipGroupIpAddress_Object((1,3,6,1,4,1,35265,1,23,55,6,1,3,1,1,3),_EltPimSnoopMembershipGroupIpAddress_Type())
eltPimSnoopMembershipGroupIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:eltPimSnoopMembershipGroupIpAddress.setStatus(_A)
_EltPimSnoopMembershipSourceIpAddressType_Type=InetAddressType
_EltPimSnoopMembershipSourceIpAddressType_Object=MibTableColumn
eltPimSnoopMembershipSourceIpAddressType=_EltPimSnoopMembershipSourceIpAddressType_Object((1,3,6,1,4,1,35265,1,23,55,6,1,3,1,1,4),_EltPimSnoopMembershipSourceIpAddressType_Type())
eltPimSnoopMembershipSourceIpAddressType.setMaxAccess(_B)
if mibBuilder.loadTexts:eltPimSnoopMembershipSourceIpAddressType.setStatus(_A)
_EltPimSnoopMembershipSourceIpAddress_Type=InetAddress
_EltPimSnoopMembershipSourceIpAddress_Object=MibTableColumn
eltPimSnoopMembershipSourceIpAddress=_EltPimSnoopMembershipSourceIpAddress_Object((1,3,6,1,4,1,35265,1,23,55,6,1,3,1,1,5),_EltPimSnoopMembershipSourceIpAddress_Type())
eltPimSnoopMembershipSourceIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:eltPimSnoopMembershipSourceIpAddress.setStatus(_A)
_EltPimSnoopMembershipOutgoingPort_Type=InterfaceIndex
_EltPimSnoopMembershipOutgoingPort_Object=MibTableColumn
eltPimSnoopMembershipOutgoingPort=_EltPimSnoopMembershipOutgoingPort_Object((1,3,6,1,4,1,35265,1,23,55,6,1,3,1,1,6),_EltPimSnoopMembershipOutgoingPort_Type())
eltPimSnoopMembershipOutgoingPort.setMaxAccess(_B)
if mibBuilder.loadTexts:eltPimSnoopMembershipOutgoingPort.setStatus(_A)
_EltPimSnoopMembershipExpiryTime_Type=Integer32
_EltPimSnoopMembershipExpiryTime_Object=MibTableColumn
eltPimSnoopMembershipExpiryTime=_EltPimSnoopMembershipExpiryTime_Object((1,3,6,1,4,1,35265,1,23,55,6,1,3,1,1,7),_EltPimSnoopMembershipExpiryTime_Type())
eltPimSnoopMembershipExpiryTime.setMaxAccess(_B)
if mibBuilder.loadTexts:eltPimSnoopMembershipExpiryTime.setStatus(_A)
_EltPimSnoopNeighborTable_Object=MibTable
eltPimSnoopNeighborTable=_EltPimSnoopNeighborTable_Object((1,3,6,1,4,1,35265,1,23,55,6,1,3,2))
if mibBuilder.loadTexts:eltPimSnoopNeighborTable.setStatus(_A)
_EltPimSnoopNeighborEntry_Object=MibTableRow
eltPimSnoopNeighborEntry=_EltPimSnoopNeighborEntry_Object((1,3,6,1,4,1,35265,1,23,55,6,1,3,2,1))
eltPimSnoopNeighborEntry.setIndexNames((0,_D,_O),(0,_D,_P),(0,_D,_Q))
if mibBuilder.loadTexts:eltPimSnoopNeighborEntry.setStatus(_A)
_EltPimSnoopNeighborVlanTag_Type=VlanIndex
_EltPimSnoopNeighborVlanTag_Object=MibTableColumn
eltPimSnoopNeighborVlanTag=_EltPimSnoopNeighborVlanTag_Object((1,3,6,1,4,1,35265,1,23,55,6,1,3,2,1,1),_EltPimSnoopNeighborVlanTag_Type())
eltPimSnoopNeighborVlanTag.setMaxAccess(_B)
if mibBuilder.loadTexts:eltPimSnoopNeighborVlanTag.setStatus(_A)
_EltPimSnoopNeighborIpAddressType_Type=InetAddressType
_EltPimSnoopNeighborIpAddressType_Object=MibTableColumn
eltPimSnoopNeighborIpAddressType=_EltPimSnoopNeighborIpAddressType_Object((1,3,6,1,4,1,35265,1,23,55,6,1,3,2,1,2),_EltPimSnoopNeighborIpAddressType_Type())
eltPimSnoopNeighborIpAddressType.setMaxAccess(_B)
if mibBuilder.loadTexts:eltPimSnoopNeighborIpAddressType.setStatus(_A)
_EltPimSnoopNeighborIpAddress_Type=InetAddress
_EltPimSnoopNeighborIpAddress_Object=MibTableColumn
eltPimSnoopNeighborIpAddress=_EltPimSnoopNeighborIpAddress_Object((1,3,6,1,4,1,35265,1,23,55,6,1,3,2,1,3),_EltPimSnoopNeighborIpAddress_Type())
eltPimSnoopNeighborIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:eltPimSnoopNeighborIpAddress.setStatus(_A)
_EltPimSnoopNeighborPort_Type=InterfaceIndex
_EltPimSnoopNeighborPort_Object=MibTableColumn
eltPimSnoopNeighborPort=_EltPimSnoopNeighborPort_Object((1,3,6,1,4,1,35265,1,23,55,6,1,3,2,1,4),_EltPimSnoopNeighborPort_Type())
eltPimSnoopNeighborPort.setMaxAccess(_B)
if mibBuilder.loadTexts:eltPimSnoopNeighborPort.setStatus(_A)
_EltPimSnoopNeighborDrPriority_Type=Integer32
_EltPimSnoopNeighborDrPriority_Object=MibTableColumn
eltPimSnoopNeighborDrPriority=_EltPimSnoopNeighborDrPriority_Object((1,3,6,1,4,1,35265,1,23,55,6,1,3,2,1,5),_EltPimSnoopNeighborDrPriority_Type())
eltPimSnoopNeighborDrPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:eltPimSnoopNeighborDrPriority.setStatus(_A)
_EltPimSnoopNeighborExpiryTime_Type=Integer32
_EltPimSnoopNeighborExpiryTime_Object=MibTableColumn
eltPimSnoopNeighborExpiryTime=_EltPimSnoopNeighborExpiryTime_Object((1,3,6,1,4,1,35265,1,23,55,6,1,3,2,1,6),_EltPimSnoopNeighborExpiryTime_Type())
eltPimSnoopNeighborExpiryTime.setMaxAccess(_B)
if mibBuilder.loadTexts:eltPimSnoopNeighborExpiryTime.setStatus(_A)
_EltPimSnoopVlanStatisticTable_Object=MibTable
eltPimSnoopVlanStatisticTable=_EltPimSnoopVlanStatisticTable_Object((1,3,6,1,4,1,35265,1,23,55,6,1,3,3))
if mibBuilder.loadTexts:eltPimSnoopVlanStatisticTable.setStatus(_A)
_EltPimSnoopVlanStatisticEntry_Object=MibTableRow
eltPimSnoopVlanStatisticEntry=_EltPimSnoopVlanStatisticEntry_Object((1,3,6,1,4,1,35265,1,23,55,6,1,3,3,1))
eltPimSnoopVlanStatisticEntry.setIndexNames((0,_D,_R))
if mibBuilder.loadTexts:eltPimSnoopVlanStatisticEntry.setStatus(_A)
_EltPimSnoopVlanStatisticVlanTag_Type=VlanIndex
_EltPimSnoopVlanStatisticVlanTag_Object=MibTableColumn
eltPimSnoopVlanStatisticVlanTag=_EltPimSnoopVlanStatisticVlanTag_Object((1,3,6,1,4,1,35265,1,23,55,6,1,3,3,1,1),_EltPimSnoopVlanStatisticVlanTag_Type())
eltPimSnoopVlanStatisticVlanTag.setMaxAccess(_B)
if mibBuilder.loadTexts:eltPimSnoopVlanStatisticVlanTag.setStatus(_A)
_EltPimSnoopVlanStatisticEnable_Type=TruthValue
_EltPimSnoopVlanStatisticEnable_Object=MibTableColumn
eltPimSnoopVlanStatisticEnable=_EltPimSnoopVlanStatisticEnable_Object((1,3,6,1,4,1,35265,1,23,55,6,1,3,3,1,2),_EltPimSnoopVlanStatisticEnable_Type())
eltPimSnoopVlanStatisticEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:eltPimSnoopVlanStatisticEnable.setStatus(_A)
_EltPimSnoopVlanStatisticRouterPortList_Type=PortList
_EltPimSnoopVlanStatisticRouterPortList_Object=MibTableColumn
eltPimSnoopVlanStatisticRouterPortList=_EltPimSnoopVlanStatisticRouterPortList_Object((1,3,6,1,4,1,35265,1,23,55,6,1,3,3,1,3),_EltPimSnoopVlanStatisticRouterPortList_Type())
eltPimSnoopVlanStatisticRouterPortList.setMaxAccess(_B)
if mibBuilder.loadTexts:eltPimSnoopVlanStatisticRouterPortList.setStatus(_A)
_EltPimSnoopVlanStatisticNeighborsCount_Type=Integer32
_EltPimSnoopVlanStatisticNeighborsCount_Object=MibTableColumn
eltPimSnoopVlanStatisticNeighborsCount=_EltPimSnoopVlanStatisticNeighborsCount_Object((1,3,6,1,4,1,35265,1,23,55,6,1,3,3,1,4),_EltPimSnoopVlanStatisticNeighborsCount_Type())
eltPimSnoopVlanStatisticNeighborsCount.setMaxAccess(_B)
if mibBuilder.loadTexts:eltPimSnoopVlanStatisticNeighborsCount.setStatus(_A)
_EltPimSnoopVlanStatisticGroupsCount_Type=Integer32
_EltPimSnoopVlanStatisticGroupsCount_Object=MibTableColumn
eltPimSnoopVlanStatisticGroupsCount=_EltPimSnoopVlanStatisticGroupsCount_Object((1,3,6,1,4,1,35265,1,23,55,6,1,3,3,1,5),_EltPimSnoopVlanStatisticGroupsCount_Type())
eltPimSnoopVlanStatisticGroupsCount.setMaxAccess(_B)
if mibBuilder.loadTexts:eltPimSnoopVlanStatisticGroupsCount.setStatus(_A)
_EltPimSnoopVlanStatisticJoinedCount_Type=Integer32
_EltPimSnoopVlanStatisticJoinedCount_Object=MibTableColumn
eltPimSnoopVlanStatisticJoinedCount=_EltPimSnoopVlanStatisticJoinedCount_Object((1,3,6,1,4,1,35265,1,23,55,6,1,3,3,1,6),_EltPimSnoopVlanStatisticJoinedCount_Type())
eltPimSnoopVlanStatisticJoinedCount.setMaxAccess(_B)
if mibBuilder.loadTexts:eltPimSnoopVlanStatisticJoinedCount.setStatus(_A)
_EltPimSnoopVlanStatisticPrunedCount_Type=Integer32
_EltPimSnoopVlanStatisticPrunedCount_Object=MibTableColumn
eltPimSnoopVlanStatisticPrunedCount=_EltPimSnoopVlanStatisticPrunedCount_Object((1,3,6,1,4,1,35265,1,23,55,6,1,3,3,1,7),_EltPimSnoopVlanStatisticPrunedCount_Type())
eltPimSnoopVlanStatisticPrunedCount.setMaxAccess(_B)
if mibBuilder.loadTexts:eltPimSnoopVlanStatisticPrunedCount.setStatus(_A)
_EltPimSnoopVlanStatisticHelloCount_Type=Integer32
_EltPimSnoopVlanStatisticHelloCount_Object=MibTableColumn
eltPimSnoopVlanStatisticHelloCount=_EltPimSnoopVlanStatisticHelloCount_Object((1,3,6,1,4,1,35265,1,23,55,6,1,3,3,1,8),_EltPimSnoopVlanStatisticHelloCount_Type())
eltPimSnoopVlanStatisticHelloCount.setMaxAccess(_B)
if mibBuilder.loadTexts:eltPimSnoopVlanStatisticHelloCount.setStatus(_A)
_EltMesPimSnoopNotifications_ObjectIdentity=ObjectIdentity
eltMesPimSnoopNotifications=_EltMesPimSnoopNotifications_ObjectIdentity((1,3,6,1,4,1,35265,1,23,55,6,2))
_EltMesPimSnoopNotificationsPrefix_ObjectIdentity=ObjectIdentity
eltMesPimSnoopNotificationsPrefix=_EltMesPimSnoopNotificationsPrefix_ObjectIdentity((1,3,6,1,4,1,35265,1,23,55,6,2,0))
_EltMesPimSnoopConformance_ObjectIdentity=ObjectIdentity
eltMesPimSnoopConformance=_EltMesPimSnoopConformance_ObjectIdentity((1,3,6,1,4,1,35265,1,23,55,6,3))
rlIgmpMldSnoopVlanEntry.registerAugmentions((_D,_S))
eltIgmpMldSnoopVlanEntry.setIndexNames(*rlIgmpMldSnoopVlanEntry.getIndexNames())
mibBuilder.exportSymbols(_D,**{'eltMesMacMulticastFilter':eltMesMacMulticastFilter,'eltMesMacMulticastFilterPerVlan':eltMesMacMulticastFilterPerVlan,'eltMacMulticastUnregFilterEnableVlanId1To1024':eltMacMulticastUnregFilterEnableVlanId1To1024,'eltMacMulticastUnregFilterEnableVlanId1025To2048':eltMacMulticastUnregFilterEnableVlanId1025To2048,'eltMacMulticastUnregFilterEnableVlanId2049To3072':eltMacMulticastUnregFilterEnableVlanId2049To3072,'eltMacMulticastUnregFilterEnableVlanId3073To4094':eltMacMulticastUnregFilterEnableVlanId3073To4094,'eltMesMldSnoop':eltMesMldSnoop,'eltIgmpMldSnoopVlanTable':eltIgmpMldSnoopVlanTable,_S:eltIgmpMldSnoopVlanEntry,'eltIgmpMldSnoopVlanIsImmediateLeaveHostBased':eltIgmpMldSnoopVlanIsImmediateLeaveHostBased,'eltIgmpMldSnoopVlanCos':eltIgmpMldSnoopVlanCos,'eltIgmpMldSnoopVlanReplaceSourceIp':eltIgmpMldSnoopVlanReplaceSourceIp,'eltIgmpMldSnoopVlanProxyReportEnable':eltIgmpMldSnoopVlanProxyReportEnable,'eltIgmpMldSnoopVlanProxyReportVersion':eltIgmpMldSnoopVlanProxyReportVersion,'eltIgmpMldSnoopVlanGsqSuppress':eltIgmpMldSnoopVlanGsqSuppress,'eltIgmpMldSnoopVlanImmediateLeavePortlist':eltIgmpMldSnoopVlanImmediateLeavePortlist,'eltIgmpMldSnoopVlanHostBasedPortlist':eltIgmpMldSnoopVlanHostBasedPortlist,'eltMesPimSnoop':eltMesPimSnoop,'eltMesPimSnoopObjects':eltMesPimSnoopObjects,'eltMesPimSnoopGlobals':eltMesPimSnoopGlobals,'eltPimSnoopEnable':eltPimSnoopEnable,'eltMesPimSnoopConfigs':eltMesPimSnoopConfigs,'eltPimSnoopVlanConfigTable':eltPimSnoopVlanConfigTable,'eltPimSnoopVlanConfigEntry':eltPimSnoopVlanConfigEntry,_H:eltPimSnoopVlanConfigVlanTag,'eltPimSnoopVlanConfigEnable':eltPimSnoopVlanConfigEnable,'eltMesPimSnoopStatictics':eltMesPimSnoopStatictics,'eltPimSnoopMembershipTable':eltPimSnoopMembershipTable,'eltPimSnoopMembershipEntry':eltPimSnoopMembershipEntry,_I:eltPimSnoopMembershipVlanTag,_J:eltPimSnoopMembershipGroupIpAddressType,_K:eltPimSnoopMembershipGroupIpAddress,_L:eltPimSnoopMembershipSourceIpAddressType,_M:eltPimSnoopMembershipSourceIpAddress,_N:eltPimSnoopMembershipOutgoingPort,'eltPimSnoopMembershipExpiryTime':eltPimSnoopMembershipExpiryTime,'eltPimSnoopNeighborTable':eltPimSnoopNeighborTable,'eltPimSnoopNeighborEntry':eltPimSnoopNeighborEntry,_O:eltPimSnoopNeighborVlanTag,_P:eltPimSnoopNeighborIpAddressType,_Q:eltPimSnoopNeighborIpAddress,'eltPimSnoopNeighborPort':eltPimSnoopNeighborPort,'eltPimSnoopNeighborDrPriority':eltPimSnoopNeighborDrPriority,'eltPimSnoopNeighborExpiryTime':eltPimSnoopNeighborExpiryTime,'eltPimSnoopVlanStatisticTable':eltPimSnoopVlanStatisticTable,'eltPimSnoopVlanStatisticEntry':eltPimSnoopVlanStatisticEntry,_R:eltPimSnoopVlanStatisticVlanTag,'eltPimSnoopVlanStatisticEnable':eltPimSnoopVlanStatisticEnable,'eltPimSnoopVlanStatisticRouterPortList':eltPimSnoopVlanStatisticRouterPortList,'eltPimSnoopVlanStatisticNeighborsCount':eltPimSnoopVlanStatisticNeighborsCount,'eltPimSnoopVlanStatisticGroupsCount':eltPimSnoopVlanStatisticGroupsCount,'eltPimSnoopVlanStatisticJoinedCount':eltPimSnoopVlanStatisticJoinedCount,'eltPimSnoopVlanStatisticPrunedCount':eltPimSnoopVlanStatisticPrunedCount,'eltPimSnoopVlanStatisticHelloCount':eltPimSnoopVlanStatisticHelloCount,'eltMesPimSnoopNotifications':eltMesPimSnoopNotifications,'eltMesPimSnoopNotificationsPrefix':eltMesPimSnoopNotificationsPrefix,'eltMesPimSnoopConformance':eltMesPimSnoopConformance})