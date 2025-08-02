_R='hmRouterRedLastErrorMessage'
_Q='hmRouterRedErrorStatus'
_P='hmRouterForwardControlIndex'
_O='hmRouterStaticArpNetAddress'
_N='invalid'
_M='hmRouterStaticDestIpAddr'
_L='hmRouterIfIndex'
_K='hmRouterRedOperStatus'
_J='enable'
_I='other'
_H='OctetString'
_G='disable'
_F='DisplayString'
_E='HIRSCHMANN-ROUTER-MIB'
_D='read-only'
_C='Integer32'
_B='read-write'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_H,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,private=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso','private')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_F,'PhysAddress','TextualConvention')
_Enterprises_ObjectIdentity=ObjectIdentity
enterprises=_Enterprises_ObjectIdentity((1,3,6,1,4,1))
_Hirschmann_ObjectIdentity=ObjectIdentity
hirschmann=_Hirschmann_ObjectIdentity((1,3,6,1,4,1,248))
_HmConfiguration_ObjectIdentity=ObjectIdentity
hmConfiguration=_HmConfiguration_ObjectIdentity((1,3,6,1,4,1,248,14))
_HmRouter_ObjectIdentity=ObjectIdentity
hmRouter=_HmRouter_ObjectIdentity((1,3,6,1,4,1,248,14,6))
_HmRouterMisc_ObjectIdentity=ObjectIdentity
hmRouterMisc=_HmRouterMisc_ObjectIdentity((1,3,6,1,4,1,248,14,6,1))
_HmRouterNumInterfaces_Type=Integer32
_HmRouterNumInterfaces_Object=MibScalar
hmRouterNumInterfaces=_HmRouterNumInterfaces_Object((1,3,6,1,4,1,248,14,6,1,1),_HmRouterNumInterfaces_Type())
hmRouterNumInterfaces.setMaxAccess(_D)
if mibBuilder.loadTexts:hmRouterNumInterfaces.setStatus(_A)
_HmRouterMaxHostRouteEntries_Type=Integer32
_HmRouterMaxHostRouteEntries_Object=MibScalar
hmRouterMaxHostRouteEntries=_HmRouterMaxHostRouteEntries_Object((1,3,6,1,4,1,248,14,6,1,2),_HmRouterMaxHostRouteEntries_Type())
hmRouterMaxHostRouteEntries.setMaxAccess(_D)
if mibBuilder.loadTexts:hmRouterMaxHostRouteEntries.setStatus(_A)
_HmRouterMaxSubnetRouteEntries_Type=Integer32
_HmRouterMaxSubnetRouteEntries_Object=MibScalar
hmRouterMaxSubnetRouteEntries=_HmRouterMaxSubnetRouteEntries_Object((1,3,6,1,4,1,248,14,6,1,3),_HmRouterMaxSubnetRouteEntries_Type())
hmRouterMaxSubnetRouteEntries.setMaxAccess(_D)
if mibBuilder.loadTexts:hmRouterMaxSubnetRouteEntries.setStatus(_A)
class _HmRouterRipEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('true',1),('false',2)))
_HmRouterRipEnable_Type.__name__=_C
_HmRouterRipEnable_Object=MibScalar
hmRouterRipEnable=_HmRouterRipEnable_Object((1,3,6,1,4,1,248,14,6,1,4),_HmRouterRipEnable_Type())
hmRouterRipEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:hmRouterRipEnable.setStatus(_A)
class _HmRouterOspfEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('true',1),('false',2)))
_HmRouterOspfEnable_Type.__name__=_C
_HmRouterOspfEnable_Object=MibScalar
hmRouterOspfEnable=_HmRouterOspfEnable_Object((1,3,6,1,4,1,248,14,6,1,5),_HmRouterOspfEnable_Type())
hmRouterOspfEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:hmRouterOspfEnable.setStatus(_A)
_HmRouterDHCPServerIpAddr_Type=IpAddress
_HmRouterDHCPServerIpAddr_Object=MibScalar
hmRouterDHCPServerIpAddr=_HmRouterDHCPServerIpAddr_Object((1,3,6,1,4,1,248,14,6,1,6),_HmRouterDHCPServerIpAddr_Type())
hmRouterDHCPServerIpAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:hmRouterDHCPServerIpAddr.setStatus(_A)
_HmRouterDHCPServer2IpAddr_Type=IpAddress
_HmRouterDHCPServer2IpAddr_Object=MibScalar
hmRouterDHCPServer2IpAddr=_HmRouterDHCPServer2IpAddr_Object((1,3,6,1,4,1,248,14,6,1,7),_HmRouterDHCPServer2IpAddr_Type())
hmRouterDHCPServer2IpAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:hmRouterDHCPServer2IpAddr.setStatus(_A)
_HmRouterDHCPServer3IpAddr_Type=IpAddress
_HmRouterDHCPServer3IpAddr_Object=MibScalar
hmRouterDHCPServer3IpAddr=_HmRouterDHCPServer3IpAddr_Object((1,3,6,1,4,1,248,14,6,1,8),_HmRouterDHCPServer3IpAddr_Type())
hmRouterDHCPServer3IpAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:hmRouterDHCPServer3IpAddr.setStatus(_A)
_HmRouterDHCPServer4IpAddr_Type=IpAddress
_HmRouterDHCPServer4IpAddr_Object=MibScalar
hmRouterDHCPServer4IpAddr=_HmRouterDHCPServer4IpAddr_Object((1,3,6,1,4,1,248,14,6,1,9),_HmRouterDHCPServer4IpAddr_Type())
hmRouterDHCPServer4IpAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:hmRouterDHCPServer4IpAddr.setStatus(_A)
_HmRouterIfTable_Object=MibTable
hmRouterIfTable=_HmRouterIfTable_Object((1,3,6,1,4,1,248,14,6,2))
if mibBuilder.loadTexts:hmRouterIfTable.setStatus(_A)
_HmRouterIfEntry_Object=MibTableRow
hmRouterIfEntry=_HmRouterIfEntry_Object((1,3,6,1,4,1,248,14,6,2,1))
hmRouterIfEntry.setIndexNames((0,_E,_L))
if mibBuilder.loadTexts:hmRouterIfEntry.setStatus(_A)
_HmRouterIfIndex_Type=Integer32
_HmRouterIfIndex_Object=MibTableColumn
hmRouterIfIndex=_HmRouterIfIndex_Object((1,3,6,1,4,1,248,14,6,2,1,1),_HmRouterIfIndex_Type())
hmRouterIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:hmRouterIfIndex.setStatus(_A)
class _HmRouterIfVlanID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_HmRouterIfVlanID_Type.__name__=_C
_HmRouterIfVlanID_Object=MibTableColumn
hmRouterIfVlanID=_HmRouterIfVlanID_Object((1,3,6,1,4,1,248,14,6,2,1,2),_HmRouterIfVlanID_Type())
hmRouterIfVlanID.setMaxAccess(_B)
if mibBuilder.loadTexts:hmRouterIfVlanID.setStatus(_A)
_HmRouterIfIpAddr_Type=IpAddress
_HmRouterIfIpAddr_Object=MibTableColumn
hmRouterIfIpAddr=_HmRouterIfIpAddr_Object((1,3,6,1,4,1,248,14,6,2,1,3),_HmRouterIfIpAddr_Type())
hmRouterIfIpAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:hmRouterIfIpAddr.setStatus(_A)
_HmRouterIfSubnetMask_Type=IpAddress
_HmRouterIfSubnetMask_Object=MibTableColumn
hmRouterIfSubnetMask=_HmRouterIfSubnetMask_Object((1,3,6,1,4,1,248,14,6,2,1,4),_HmRouterIfSubnetMask_Type())
hmRouterIfSubnetMask.setMaxAccess(_B)
if mibBuilder.loadTexts:hmRouterIfSubnetMask.setStatus(_A)
class _HmRouterIfName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_HmRouterIfName_Type.__name__=_F
_HmRouterIfName_Object=MibTableColumn
hmRouterIfName=_HmRouterIfName_Object((1,3,6,1,4,1,248,14,6,2,1,5),_HmRouterIfName_Type())
hmRouterIfName.setMaxAccess(_B)
if mibBuilder.loadTexts:hmRouterIfName.setStatus(_A)
class _HmRouterIfAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),('down',2)))
_HmRouterIfAdminStatus_Type.__name__=_C
_HmRouterIfAdminStatus_Object=MibTableColumn
hmRouterIfAdminStatus=_HmRouterIfAdminStatus_Object((1,3,6,1,4,1,248,14,6,2,1,6),_HmRouterIfAdminStatus_Type())
hmRouterIfAdminStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hmRouterIfAdminStatus.setStatus(_A)
class _HmRouterIfOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),('down',2)))
_HmRouterIfOperStatus_Type.__name__=_C
_HmRouterIfOperStatus_Object=MibTableColumn
hmRouterIfOperStatus=_HmRouterIfOperStatus_Object((1,3,6,1,4,1,248,14,6,2,1,7),_HmRouterIfOperStatus_Type())
hmRouterIfOperStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:hmRouterIfOperStatus.setStatus(_A)
_HmRouterIfRedundantIpAddr_Type=IpAddress
_HmRouterIfRedundantIpAddr_Object=MibTableColumn
hmRouterIfRedundantIpAddr=_HmRouterIfRedundantIpAddr_Object((1,3,6,1,4,1,248,14,6,2,1,8),_HmRouterIfRedundantIpAddr_Type())
hmRouterIfRedundantIpAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:hmRouterIfRedundantIpAddr.setStatus(_A)
_HmRouterStaticTable_Object=MibTable
hmRouterStaticTable=_HmRouterStaticTable_Object((1,3,6,1,4,1,248,14,6,4))
if mibBuilder.loadTexts:hmRouterStaticTable.setStatus(_A)
_HmRouterStaticEntry_Object=MibTableRow
hmRouterStaticEntry=_HmRouterStaticEntry_Object((1,3,6,1,4,1,248,14,6,4,1))
hmRouterStaticEntry.setIndexNames((0,_E,_M))
if mibBuilder.loadTexts:hmRouterStaticEntry.setStatus(_A)
_HmRouterStaticDestIpAddr_Type=IpAddress
_HmRouterStaticDestIpAddr_Object=MibTableColumn
hmRouterStaticDestIpAddr=_HmRouterStaticDestIpAddr_Object((1,3,6,1,4,1,248,14,6,4,1,1),_HmRouterStaticDestIpAddr_Type())
hmRouterStaticDestIpAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:hmRouterStaticDestIpAddr.setStatus(_A)
_HmRouterStaticMask_Type=IpAddress
_HmRouterStaticMask_Object=MibTableColumn
hmRouterStaticMask=_HmRouterStaticMask_Object((1,3,6,1,4,1,248,14,6,4,1,2),_HmRouterStaticMask_Type())
hmRouterStaticMask.setMaxAccess(_B)
if mibBuilder.loadTexts:hmRouterStaticMask.setStatus(_A)
_HmRouterStaticNextHop_Type=IpAddress
_HmRouterStaticNextHop_Object=MibTableColumn
hmRouterStaticNextHop=_HmRouterStaticNextHop_Object((1,3,6,1,4,1,248,14,6,4,1,3),_HmRouterStaticNextHop_Type())
hmRouterStaticNextHop.setMaxAccess(_B)
if mibBuilder.loadTexts:hmRouterStaticNextHop.setStatus(_A)
class _HmRouterStaticRouteName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_HmRouterStaticRouteName_Type.__name__=_F
_HmRouterStaticRouteName_Object=MibTableColumn
hmRouterStaticRouteName=_HmRouterStaticRouteName_Object((1,3,6,1,4,1,248,14,6,4,1,4),_HmRouterStaticRouteName_Type())
hmRouterStaticRouteName.setMaxAccess(_B)
if mibBuilder.loadTexts:hmRouterStaticRouteName.setStatus(_A)
class _HmRouterStaticRouteType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_I,1),(_N,2),('direct',3),('indirect',4)))
_HmRouterStaticRouteType_Type.__name__=_C
_HmRouterStaticRouteType_Object=MibTableColumn
hmRouterStaticRouteType=_HmRouterStaticRouteType_Object((1,3,6,1,4,1,248,14,6,4,1,5),_HmRouterStaticRouteType_Type())
hmRouterStaticRouteType.setMaxAccess(_B)
if mibBuilder.loadTexts:hmRouterStaticRouteType.setStatus(_A)
_HmRouterOptions_ObjectIdentity=ObjectIdentity
hmRouterOptions=_HmRouterOptions_ObjectIdentity((1,3,6,1,4,1,248,14,6,5))
class _HmRouterIcmpTimeExceededMessage_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_G,2)))
_HmRouterIcmpTimeExceededMessage_Type.__name__=_C
_HmRouterIcmpTimeExceededMessage_Object=MibScalar
hmRouterIcmpTimeExceededMessage=_HmRouterIcmpTimeExceededMessage_Object((1,3,6,1,4,1,248,14,6,5,1),_HmRouterIcmpTimeExceededMessage_Type())
hmRouterIcmpTimeExceededMessage.setMaxAccess(_B)
if mibBuilder.loadTexts:hmRouterIcmpTimeExceededMessage.setStatus(_A)
_HmRouterStaticArpTable_Object=MibTable
hmRouterStaticArpTable=_HmRouterStaticArpTable_Object((1,3,6,1,4,1,248,14,6,6))
if mibBuilder.loadTexts:hmRouterStaticArpTable.setStatus(_A)
_HmRouterStaticArpEntry_Object=MibTableRow
hmRouterStaticArpEntry=_HmRouterStaticArpEntry_Object((1,3,6,1,4,1,248,14,6,6,1))
hmRouterStaticArpEntry.setIndexNames((0,_E,_O))
if mibBuilder.loadTexts:hmRouterStaticArpEntry.setStatus(_A)
_HmRouterStaticArpNetAddress_Type=IpAddress
_HmRouterStaticArpNetAddress_Object=MibTableColumn
hmRouterStaticArpNetAddress=_HmRouterStaticArpNetAddress_Object((1,3,6,1,4,1,248,14,6,6,1,1),_HmRouterStaticArpNetAddress_Type())
hmRouterStaticArpNetAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:hmRouterStaticArpNetAddress.setStatus(_A)
_HmRouterStaticArpPhysAddress_Type=PhysAddress
_HmRouterStaticArpPhysAddress_Object=MibTableColumn
hmRouterStaticArpPhysAddress=_HmRouterStaticArpPhysAddress_Object((1,3,6,1,4,1,248,14,6,6,1,2),_HmRouterStaticArpPhysAddress_Type())
hmRouterStaticArpPhysAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:hmRouterStaticArpPhysAddress.setStatus(_A)
class _HmRouterStaticArpName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_HmRouterStaticArpName_Type.__name__=_F
_HmRouterStaticArpName_Object=MibTableColumn
hmRouterStaticArpName=_HmRouterStaticArpName_Object((1,3,6,1,4,1,248,14,6,6,1,3),_HmRouterStaticArpName_Type())
hmRouterStaticArpName.setMaxAccess(_B)
if mibBuilder.loadTexts:hmRouterStaticArpName.setStatus(_A)
class _HmRouterStaticArpType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_I,1),(_N,2),('static',3)))
_HmRouterStaticArpType_Type.__name__=_C
_HmRouterStaticArpType_Object=MibTableColumn
hmRouterStaticArpType=_HmRouterStaticArpType_Object((1,3,6,1,4,1,248,14,6,6,1,4),_HmRouterStaticArpType_Type())
hmRouterStaticArpType.setMaxAccess(_B)
if mibBuilder.loadTexts:hmRouterStaticArpType.setStatus(_A)
_HmRouterRedundancy_ObjectIdentity=ObjectIdentity
hmRouterRedundancy=_HmRouterRedundancy_ObjectIdentity((1,3,6,1,4,1,248,14,6,10))
_HmRouterRedConfiguration_ObjectIdentity=ObjectIdentity
hmRouterRedConfiguration=_HmRouterRedConfiguration_ObjectIdentity((1,3,6,1,4,1,248,14,6,10,1))
_HmRouterRedPartnerIpAddress_Type=IpAddress
_HmRouterRedPartnerIpAddress_Object=MibScalar
hmRouterRedPartnerIpAddress=_HmRouterRedPartnerIpAddress_Object((1,3,6,1,4,1,248,14,6,10,1,1),_HmRouterRedPartnerIpAddress_Type())
hmRouterRedPartnerIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:hmRouterRedPartnerIpAddress.setStatus(_A)
class _HmRouterRedPartnerInfo_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(128,128));fixedLength=128
_HmRouterRedPartnerInfo_Type.__name__=_H
_HmRouterRedPartnerInfo_Object=MibScalar
hmRouterRedPartnerInfo=_HmRouterRedPartnerInfo_Object((1,3,6,1,4,1,248,14,6,10,1,2),_HmRouterRedPartnerInfo_Type())
hmRouterRedPartnerInfo.setMaxAccess(_D)
if mibBuilder.loadTexts:hmRouterRedPartnerInfo.setStatus(_A)
class _HmRouterRedMessageInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(50,5000))
_HmRouterRedMessageInterval_Type.__name__=_C
_HmRouterRedMessageInterval_Object=MibScalar
hmRouterRedMessageInterval=_HmRouterRedMessageInterval_Object((1,3,6,1,4,1,248,14,6,10,1,3),_HmRouterRedMessageInterval_Type())
hmRouterRedMessageInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:hmRouterRedMessageInterval.setStatus(_A)
class _HmRouterRedMessageTimeout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(500,60000))
_HmRouterRedMessageTimeout_Type.__name__=_C
_HmRouterRedMessageTimeout_Object=MibScalar
hmRouterRedMessageTimeout=_HmRouterRedMessageTimeout_Object((1,3,6,1,4,1,248,14,6,10,1,4),_HmRouterRedMessageTimeout_Type())
hmRouterRedMessageTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:hmRouterRedMessageTimeout.setStatus(_A)
class _HmRouterRedAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_G,2)))
_HmRouterRedAdminStatus_Type.__name__=_C
_HmRouterRedAdminStatus_Object=MibScalar
hmRouterRedAdminStatus=_HmRouterRedAdminStatus_Object((1,3,6,1,4,1,248,14,6,10,1,5),_HmRouterRedAdminStatus_Type())
hmRouterRedAdminStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hmRouterRedAdminStatus.setStatus(_A)
class _HmRouterRedOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_G,1),('standby',2),('active',3),(_I,4)))
_HmRouterRedOperStatus_Type.__name__=_C
_HmRouterRedOperStatus_Object=MibScalar
hmRouterRedOperStatus=_HmRouterRedOperStatus_Object((1,3,6,1,4,1,248,14,6,10,1,6),_HmRouterRedOperStatus_Type())
hmRouterRedOperStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:hmRouterRedOperStatus.setStatus(_A)
_HmRouterRedLastErrorMessage_Type=DisplayString
_HmRouterRedLastErrorMessage_Object=MibScalar
hmRouterRedLastErrorMessage=_HmRouterRedLastErrorMessage_Object((1,3,6,1,4,1,248,14,6,10,1,7),_HmRouterRedLastErrorMessage_Type())
hmRouterRedLastErrorMessage.setMaxAccess(_D)
if mibBuilder.loadTexts:hmRouterRedLastErrorMessage.setStatus(_A)
class _HmRouterRedErrorStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ok',1),('error',2)))
_HmRouterRedErrorStatus_Type.__name__=_C
_HmRouterRedErrorStatus_Object=MibScalar
hmRouterRedErrorStatus=_HmRouterRedErrorStatus_Object((1,3,6,1,4,1,248,14,6,10,1,8),_HmRouterRedErrorStatus_Type())
hmRouterRedErrorStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:hmRouterRedErrorStatus.setStatus(_A)
_HmRouterRedStats_ObjectIdentity=ObjectIdentity
hmRouterRedStats=_HmRouterRedStats_ObjectIdentity((1,3,6,1,4,1,248,14,6,10,2))
_HmRouterRedStatsTakeoverCount_Type=Counter32
_HmRouterRedStatsTakeoverCount_Object=MibScalar
hmRouterRedStatsTakeoverCount=_HmRouterRedStatsTakeoverCount_Object((1,3,6,1,4,1,248,14,6,10,2,1),_HmRouterRedStatsTakeoverCount_Type())
hmRouterRedStatsTakeoverCount.setMaxAccess(_D)
if mibBuilder.loadTexts:hmRouterRedStatsTakeoverCount.setStatus(_A)
_HmRouterRedStatsLastChange_Type=TimeTicks
_HmRouterRedStatsLastChange_Object=MibScalar
hmRouterRedStatsLastChange=_HmRouterRedStatsLastChange_Object((1,3,6,1,4,1,248,14,6,10,2,2),_HmRouterRedStatsLastChange_Type())
hmRouterRedStatsLastChange.setMaxAccess(_D)
if mibBuilder.loadTexts:hmRouterRedStatsLastChange.setStatus(_A)
_HmRouterForwardControl_ObjectIdentity=ObjectIdentity
hmRouterForwardControl=_HmRouterForwardControl_ObjectIdentity((1,3,6,1,4,1,248,14,6,11))
class _HmRouterForwardControlEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_G,2)))
_HmRouterForwardControlEnable_Type.__name__=_C
_HmRouterForwardControlEnable_Object=MibScalar
hmRouterForwardControlEnable=_HmRouterForwardControlEnable_Object((1,3,6,1,4,1,248,14,6,11,1),_HmRouterForwardControlEnable_Type())
hmRouterForwardControlEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:hmRouterForwardControlEnable.setStatus(_A)
_HmRouterForwardControlTable_Object=MibTable
hmRouterForwardControlTable=_HmRouterForwardControlTable_Object((1,3,6,1,4,1,248,14,6,11,10))
if mibBuilder.loadTexts:hmRouterForwardControlTable.setStatus(_A)
_HmRouterForwardControlEntry_Object=MibTableRow
hmRouterForwardControlEntry=_HmRouterForwardControlEntry_Object((1,3,6,1,4,1,248,14,6,11,10,1))
hmRouterForwardControlEntry.setIndexNames((0,_E,_P))
if mibBuilder.loadTexts:hmRouterForwardControlEntry.setStatus(_A)
_HmRouterForwardControlIndex_Type=Integer32
_HmRouterForwardControlIndex_Object=MibTableColumn
hmRouterForwardControlIndex=_HmRouterForwardControlIndex_Object((1,3,6,1,4,1,248,14,6,11,10,1,1),_HmRouterForwardControlIndex_Type())
hmRouterForwardControlIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:hmRouterForwardControlIndex.setStatus(_A)
class _HmRouterFCAllowedToGo_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(10,10));fixedLength=10
_HmRouterFCAllowedToGo_Type.__name__=_H
_HmRouterFCAllowedToGo_Object=MibTableColumn
hmRouterFCAllowedToGo=_HmRouterFCAllowedToGo_Object((1,3,6,1,4,1,248,14,6,11,10,1,2),_HmRouterFCAllowedToGo_Type())
hmRouterFCAllowedToGo.setMaxAccess(_B)
if mibBuilder.loadTexts:hmRouterFCAllowedToGo.setStatus(_A)
_HmRouterFCIngressRejects_Type=Counter32
_HmRouterFCIngressRejects_Object=MibTableColumn
hmRouterFCIngressRejects=_HmRouterFCIngressRejects_Object((1,3,6,1,4,1,248,14,6,11,10,1,3),_HmRouterFCIngressRejects_Type())
hmRouterFCIngressRejects.setMaxAccess(_D)
if mibBuilder.loadTexts:hmRouterFCIngressRejects.setStatus(_A)
_HmRouterFCEgressRejects_Type=Counter32
_HmRouterFCEgressRejects_Object=MibTableColumn
hmRouterFCEgressRejects=_HmRouterFCEgressRejects_Object((1,3,6,1,4,1,248,14,6,11,10,1,4),_HmRouterFCEgressRejects_Type())
hmRouterFCEgressRejects.setMaxAccess(_D)
if mibBuilder.loadTexts:hmRouterFCEgressRejects.setStatus(_A)
hmRouterRedTransition=NotificationType((1,3,6,1,4,1,248,14,6,10,0,1))
hmRouterRedTransition.setObjects((_E,_K))
if mibBuilder.loadTexts:hmRouterRedTransition.setStatus('')
hmRouterRedConfigError=NotificationType((1,3,6,1,4,1,248,14,6,10,0,2))
hmRouterRedConfigError.setObjects(*((_E,_Q),(_E,_R),(_E,_K)))
if mibBuilder.loadTexts:hmRouterRedConfigError.setStatus('')
mibBuilder.exportSymbols(_E,**{'enterprises':enterprises,'hirschmann':hirschmann,'hmConfiguration':hmConfiguration,'hmRouter':hmRouter,'hmRouterMisc':hmRouterMisc,'hmRouterNumInterfaces':hmRouterNumInterfaces,'hmRouterMaxHostRouteEntries':hmRouterMaxHostRouteEntries,'hmRouterMaxSubnetRouteEntries':hmRouterMaxSubnetRouteEntries,'hmRouterRipEnable':hmRouterRipEnable,'hmRouterOspfEnable':hmRouterOspfEnable,'hmRouterDHCPServerIpAddr':hmRouterDHCPServerIpAddr,'hmRouterDHCPServer2IpAddr':hmRouterDHCPServer2IpAddr,'hmRouterDHCPServer3IpAddr':hmRouterDHCPServer3IpAddr,'hmRouterDHCPServer4IpAddr':hmRouterDHCPServer4IpAddr,'hmRouterIfTable':hmRouterIfTable,'hmRouterIfEntry':hmRouterIfEntry,_L:hmRouterIfIndex,'hmRouterIfVlanID':hmRouterIfVlanID,'hmRouterIfIpAddr':hmRouterIfIpAddr,'hmRouterIfSubnetMask':hmRouterIfSubnetMask,'hmRouterIfName':hmRouterIfName,'hmRouterIfAdminStatus':hmRouterIfAdminStatus,'hmRouterIfOperStatus':hmRouterIfOperStatus,'hmRouterIfRedundantIpAddr':hmRouterIfRedundantIpAddr,'hmRouterStaticTable':hmRouterStaticTable,'hmRouterStaticEntry':hmRouterStaticEntry,_M:hmRouterStaticDestIpAddr,'hmRouterStaticMask':hmRouterStaticMask,'hmRouterStaticNextHop':hmRouterStaticNextHop,'hmRouterStaticRouteName':hmRouterStaticRouteName,'hmRouterStaticRouteType':hmRouterStaticRouteType,'hmRouterOptions':hmRouterOptions,'hmRouterIcmpTimeExceededMessage':hmRouterIcmpTimeExceededMessage,'hmRouterStaticArpTable':hmRouterStaticArpTable,'hmRouterStaticArpEntry':hmRouterStaticArpEntry,_O:hmRouterStaticArpNetAddress,'hmRouterStaticArpPhysAddress':hmRouterStaticArpPhysAddress,'hmRouterStaticArpName':hmRouterStaticArpName,'hmRouterStaticArpType':hmRouterStaticArpType,'hmRouterRedundancy':hmRouterRedundancy,'hmRouterRedTransition':hmRouterRedTransition,'hmRouterRedConfigError':hmRouterRedConfigError,'hmRouterRedConfiguration':hmRouterRedConfiguration,'hmRouterRedPartnerIpAddress':hmRouterRedPartnerIpAddress,'hmRouterRedPartnerInfo':hmRouterRedPartnerInfo,'hmRouterRedMessageInterval':hmRouterRedMessageInterval,'hmRouterRedMessageTimeout':hmRouterRedMessageTimeout,'hmRouterRedAdminStatus':hmRouterRedAdminStatus,_K:hmRouterRedOperStatus,_R:hmRouterRedLastErrorMessage,_Q:hmRouterRedErrorStatus,'hmRouterRedStats':hmRouterRedStats,'hmRouterRedStatsTakeoverCount':hmRouterRedStatsTakeoverCount,'hmRouterRedStatsLastChange':hmRouterRedStatsLastChange,'hmRouterForwardControl':hmRouterForwardControl,'hmRouterForwardControlEnable':hmRouterForwardControlEnable,'hmRouterForwardControlTable':hmRouterForwardControlTable,'hmRouterForwardControlEntry':hmRouterForwardControlEntry,_P:hmRouterForwardControlIndex,'hmRouterFCAllowedToGo':hmRouterFCAllowedToGo,'hmRouterFCIngressRejects':hmRouterFCIngressRejects,'hmRouterFCEgressRejects':hmRouterFCEgressRejects})