_A2='dsliteAFTRAlarmScalarGroup'
_A1='dsliteNotificationsGroup'
_A0='dsliteStatisticsGroup'
_z='dsliteTunnelGroup'
_y='dsliteNATBindGroup'
_x='dsliteAFTRPortUsageOfSpecificIpAlarm'
_w='dsliteAFTRUserSessionNumAlarm'
_v='dsliteTunnelNumAlarm'
_u='dsliteAFTRAlarmPortNumber'
_t='dsliteAFTRAlarmSessionNumber'
_s='dsliteAFTRAlarmConnectNumber'
_r='dsliteStatisticsIpv6Session'
_q='dsliteStatisticsIpv4Session'
_p='dsliteStatisticsReceives'
_o='dsliteStatisticsSends'
_n='dsliteStatisticsDiscards'
_m='dsliteTunnelStartAddPreLen'
_l='dsliteNATBindMappingAddressPooling'
_k='dsliteNATBindMappingFilterBehavior'
_j='dsliteNATBindMappingMapBehavior'
_i='dsliteNATBindMappingPool'
_h='dsliteNATBindMappingIntPort'
_g='dsliteNATBindMappingIntAddress'
_f='dsliteNATBindMappingIntAddressType'
_e='dsliteNATBindMappingIntRealm'
_d='dsliteStatisticsSubscriberIndex'
_c='addressAndPortDependent'
_b='addressDependent'
_a='endpointIndependent'
_Z='dsliteNATBindMappingExtPort'
_Y='dsliteNATBindMappingExtAddress'
_X='dsliteNATBindMappingExtAddressType'
_W='dsliteNATBindMappingExtRealm'
_V='dsliteNATBindMappingProto'
_U='dsliteNATBindMappingInstanceIndex'
_T='dsliteTunnelEndAddress'
_S='dsliteTunnelAddressType'
_R='Unsigned32'
_Q='dsliteAFTRAlarmSpecificIP'
_P='dsliteAFTRAlarmSpecificIPAddrType'
_O='read-write'
_N='dsliteTunnelStartAddress'
_M='SnmpAdminString'
_L='ifIndex'
_K='IF-MIB'
_J='dsliteAFTRAlarmProtocolType'
_I='dsliteAFTRAlarmB4Addr'
_H='dsliteAFTRAlarmB4AddrType'
_G='InetAddress'
_F='accessible-for-notify'
_E='Integer32'
_D='not-accessible'
_C='read-only'
_B='current'
_A='DSLite-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_K,_L)
InetAddress,InetAddressPrefixLength,InetAddressType,InetPortNumber=mibBuilder.importSymbols('INET-ADDRESS-MIB',_G,'InetAddressPrefixLength','InetAddressType','InetPortNumber')
Natv2InstanceIndex,Natv2SubscriberIndex,ProtocolNumber=mibBuilder.importSymbols('NATV2-MIB','Natv2InstanceIndex','Natv2SubscriberIndex','ProtocolNumber')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_M)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,mib_2=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_R,'iso','mib-2')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
dsliteMIB=ModuleIdentity((1,3,6,1,2,1,240))
if mibBuilder.loadTexts:dsliteMIB.setRevisions(('2016-05-11 00:00',))
_DsliteNotifications_ObjectIdentity=ObjectIdentity
dsliteNotifications=_DsliteNotifications_ObjectIdentity((1,3,6,1,2,1,240,0))
_DsliteMIBObjects_ObjectIdentity=ObjectIdentity
dsliteMIBObjects=_DsliteMIBObjects_ObjectIdentity((1,3,6,1,2,1,240,1))
_DsliteTunnel_ObjectIdentity=ObjectIdentity
dsliteTunnel=_DsliteTunnel_ObjectIdentity((1,3,6,1,2,1,240,1,1))
_DsliteTunnelTable_Object=MibTable
dsliteTunnelTable=_DsliteTunnelTable_Object((1,3,6,1,2,1,240,1,1,1))
if mibBuilder.loadTexts:dsliteTunnelTable.setStatus(_B)
_DsliteTunnelEntry_Object=MibTableRow
dsliteTunnelEntry=_DsliteTunnelEntry_Object((1,3,6,1,2,1,240,1,1,1,1))
dsliteTunnelEntry.setIndexNames((0,_A,_S),(0,_A,_N),(0,_A,_T),(0,_K,_L))
if mibBuilder.loadTexts:dsliteTunnelEntry.setStatus(_B)
_DsliteTunnelAddressType_Type=InetAddressType
_DsliteTunnelAddressType_Object=MibTableColumn
dsliteTunnelAddressType=_DsliteTunnelAddressType_Object((1,3,6,1,2,1,240,1,1,1,1,1),_DsliteTunnelAddressType_Type())
dsliteTunnelAddressType.setMaxAccess(_D)
if mibBuilder.loadTexts:dsliteTunnelAddressType.setStatus(_B)
class _DsliteTunnelStartAddress_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_DsliteTunnelStartAddress_Type.__name__=_G
_DsliteTunnelStartAddress_Object=MibTableColumn
dsliteTunnelStartAddress=_DsliteTunnelStartAddress_Object((1,3,6,1,2,1,240,1,1,1,1,2),_DsliteTunnelStartAddress_Type())
dsliteTunnelStartAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:dsliteTunnelStartAddress.setStatus(_B)
class _DsliteTunnelEndAddress_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_DsliteTunnelEndAddress_Type.__name__=_G
_DsliteTunnelEndAddress_Object=MibTableColumn
dsliteTunnelEndAddress=_DsliteTunnelEndAddress_Object((1,3,6,1,2,1,240,1,1,1,1,3),_DsliteTunnelEndAddress_Type())
dsliteTunnelEndAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:dsliteTunnelEndAddress.setStatus(_B)
_DsliteTunnelStartAddPreLen_Type=InetAddressPrefixLength
_DsliteTunnelStartAddPreLen_Object=MibTableColumn
dsliteTunnelStartAddPreLen=_DsliteTunnelStartAddPreLen_Object((1,3,6,1,2,1,240,1,1,1,1,4),_DsliteTunnelStartAddPreLen_Type())
dsliteTunnelStartAddPreLen.setMaxAccess(_C)
if mibBuilder.loadTexts:dsliteTunnelStartAddPreLen.setStatus(_B)
_DsliteNAT_ObjectIdentity=ObjectIdentity
dsliteNAT=_DsliteNAT_ObjectIdentity((1,3,6,1,2,1,240,1,2))
_DsliteNATBindTable_Object=MibTable
dsliteNATBindTable=_DsliteNATBindTable_Object((1,3,6,1,2,1,240,1,2,1))
if mibBuilder.loadTexts:dsliteNATBindTable.setStatus(_B)
_DsliteNATBindEntry_Object=MibTableRow
dsliteNATBindEntry=_DsliteNATBindEntry_Object((1,3,6,1,2,1,240,1,2,1,1))
dsliteNATBindEntry.setIndexNames((0,_A,_U),(0,_A,_V),(0,_A,_W),(0,_A,_X),(0,_A,_Y),(0,_A,_Z),(0,_K,_L),(0,_A,_N))
if mibBuilder.loadTexts:dsliteNATBindEntry.setStatus(_B)
_DsliteNATBindMappingInstanceIndex_Type=Natv2InstanceIndex
_DsliteNATBindMappingInstanceIndex_Object=MibTableColumn
dsliteNATBindMappingInstanceIndex=_DsliteNATBindMappingInstanceIndex_Object((1,3,6,1,2,1,240,1,2,1,1,1),_DsliteNATBindMappingInstanceIndex_Type())
dsliteNATBindMappingInstanceIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:dsliteNATBindMappingInstanceIndex.setStatus(_B)
_DsliteNATBindMappingProto_Type=ProtocolNumber
_DsliteNATBindMappingProto_Object=MibTableColumn
dsliteNATBindMappingProto=_DsliteNATBindMappingProto_Object((1,3,6,1,2,1,240,1,2,1,1,2),_DsliteNATBindMappingProto_Type())
dsliteNATBindMappingProto.setMaxAccess(_D)
if mibBuilder.loadTexts:dsliteNATBindMappingProto.setStatus(_B)
class _DsliteNATBindMappingExtRealm_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_DsliteNATBindMappingExtRealm_Type.__name__=_M
_DsliteNATBindMappingExtRealm_Object=MibTableColumn
dsliteNATBindMappingExtRealm=_DsliteNATBindMappingExtRealm_Object((1,3,6,1,2,1,240,1,2,1,1,3),_DsliteNATBindMappingExtRealm_Type())
dsliteNATBindMappingExtRealm.setMaxAccess(_D)
if mibBuilder.loadTexts:dsliteNATBindMappingExtRealm.setStatus(_B)
_DsliteNATBindMappingExtAddressType_Type=InetAddressType
_DsliteNATBindMappingExtAddressType_Object=MibTableColumn
dsliteNATBindMappingExtAddressType=_DsliteNATBindMappingExtAddressType_Object((1,3,6,1,2,1,240,1,2,1,1,4),_DsliteNATBindMappingExtAddressType_Type())
dsliteNATBindMappingExtAddressType.setMaxAccess(_D)
if mibBuilder.loadTexts:dsliteNATBindMappingExtAddressType.setStatus(_B)
class _DsliteNATBindMappingExtAddress_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,4))
_DsliteNATBindMappingExtAddress_Type.__name__=_G
_DsliteNATBindMappingExtAddress_Object=MibTableColumn
dsliteNATBindMappingExtAddress=_DsliteNATBindMappingExtAddress_Object((1,3,6,1,2,1,240,1,2,1,1,5),_DsliteNATBindMappingExtAddress_Type())
dsliteNATBindMappingExtAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:dsliteNATBindMappingExtAddress.setStatus(_B)
_DsliteNATBindMappingExtPort_Type=InetPortNumber
_DsliteNATBindMappingExtPort_Object=MibTableColumn
dsliteNATBindMappingExtPort=_DsliteNATBindMappingExtPort_Object((1,3,6,1,2,1,240,1,2,1,1,6),_DsliteNATBindMappingExtPort_Type())
dsliteNATBindMappingExtPort.setMaxAccess(_D)
if mibBuilder.loadTexts:dsliteNATBindMappingExtPort.setStatus(_B)
class _DsliteNATBindMappingIntRealm_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_DsliteNATBindMappingIntRealm_Type.__name__=_M
_DsliteNATBindMappingIntRealm_Object=MibTableColumn
dsliteNATBindMappingIntRealm=_DsliteNATBindMappingIntRealm_Object((1,3,6,1,2,1,240,1,2,1,1,7),_DsliteNATBindMappingIntRealm_Type())
dsliteNATBindMappingIntRealm.setMaxAccess(_C)
if mibBuilder.loadTexts:dsliteNATBindMappingIntRealm.setStatus(_B)
_DsliteNATBindMappingIntAddressType_Type=InetAddressType
_DsliteNATBindMappingIntAddressType_Object=MibTableColumn
dsliteNATBindMappingIntAddressType=_DsliteNATBindMappingIntAddressType_Object((1,3,6,1,2,1,240,1,2,1,1,8),_DsliteNATBindMappingIntAddressType_Type())
dsliteNATBindMappingIntAddressType.setMaxAccess(_C)
if mibBuilder.loadTexts:dsliteNATBindMappingIntAddressType.setStatus(_B)
_DsliteNATBindMappingIntAddress_Type=InetAddress
_DsliteNATBindMappingIntAddress_Object=MibTableColumn
dsliteNATBindMappingIntAddress=_DsliteNATBindMappingIntAddress_Object((1,3,6,1,2,1,240,1,2,1,1,9),_DsliteNATBindMappingIntAddress_Type())
dsliteNATBindMappingIntAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:dsliteNATBindMappingIntAddress.setStatus(_B)
_DsliteNATBindMappingIntPort_Type=InetPortNumber
_DsliteNATBindMappingIntPort_Object=MibTableColumn
dsliteNATBindMappingIntPort=_DsliteNATBindMappingIntPort_Object((1,3,6,1,2,1,240,1,2,1,1,10),_DsliteNATBindMappingIntPort_Type())
dsliteNATBindMappingIntPort.setMaxAccess(_C)
if mibBuilder.loadTexts:dsliteNATBindMappingIntPort.setStatus(_B)
class _DsliteNATBindMappingPool_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,4294967295))
_DsliteNATBindMappingPool_Type.__name__=_R
_DsliteNATBindMappingPool_Object=MibTableColumn
dsliteNATBindMappingPool=_DsliteNATBindMappingPool_Object((1,3,6,1,2,1,240,1,2,1,1,11),_DsliteNATBindMappingPool_Type())
dsliteNATBindMappingPool.setMaxAccess(_C)
if mibBuilder.loadTexts:dsliteNATBindMappingPool.setStatus(_B)
class _DsliteNATBindMappingMapBehavior_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_a,0),(_b,1),(_c,2)))
_DsliteNATBindMappingMapBehavior_Type.__name__=_E
_DsliteNATBindMappingMapBehavior_Object=MibTableColumn
dsliteNATBindMappingMapBehavior=_DsliteNATBindMappingMapBehavior_Object((1,3,6,1,2,1,240,1,2,1,1,12),_DsliteNATBindMappingMapBehavior_Type())
dsliteNATBindMappingMapBehavior.setMaxAccess(_C)
if mibBuilder.loadTexts:dsliteNATBindMappingMapBehavior.setStatus(_B)
class _DsliteNATBindMappingFilterBehavior_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_a,0),(_b,1),(_c,2)))
_DsliteNATBindMappingFilterBehavior_Type.__name__=_E
_DsliteNATBindMappingFilterBehavior_Object=MibTableColumn
dsliteNATBindMappingFilterBehavior=_DsliteNATBindMappingFilterBehavior_Object((1,3,6,1,2,1,240,1,2,1,1,13),_DsliteNATBindMappingFilterBehavior_Type())
dsliteNATBindMappingFilterBehavior.setMaxAccess(_C)
if mibBuilder.loadTexts:dsliteNATBindMappingFilterBehavior.setStatus(_B)
class _DsliteNATBindMappingAddressPooling_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('arbitrary',0),('paired',1)))
_DsliteNATBindMappingAddressPooling_Type.__name__=_E
_DsliteNATBindMappingAddressPooling_Object=MibTableColumn
dsliteNATBindMappingAddressPooling=_DsliteNATBindMappingAddressPooling_Object((1,3,6,1,2,1,240,1,2,1,1,14),_DsliteNATBindMappingAddressPooling_Type())
dsliteNATBindMappingAddressPooling.setMaxAccess(_C)
if mibBuilder.loadTexts:dsliteNATBindMappingAddressPooling.setStatus(_B)
_DsliteInfo_ObjectIdentity=ObjectIdentity
dsliteInfo=_DsliteInfo_ObjectIdentity((1,3,6,1,2,1,240,1,3))
_DsliteAFTRAlarmScalar_ObjectIdentity=ObjectIdentity
dsliteAFTRAlarmScalar=_DsliteAFTRAlarmScalar_ObjectIdentity((1,3,6,1,2,1,240,1,3,1))
_DsliteAFTRAlarmB4AddrType_Type=InetAddressType
_DsliteAFTRAlarmB4AddrType_Object=MibScalar
dsliteAFTRAlarmB4AddrType=_DsliteAFTRAlarmB4AddrType_Object((1,3,6,1,2,1,240,1,3,1,1),_DsliteAFTRAlarmB4AddrType_Type())
dsliteAFTRAlarmB4AddrType.setMaxAccess(_F)
if mibBuilder.loadTexts:dsliteAFTRAlarmB4AddrType.setStatus(_B)
_DsliteAFTRAlarmB4Addr_Type=InetAddress
_DsliteAFTRAlarmB4Addr_Object=MibScalar
dsliteAFTRAlarmB4Addr=_DsliteAFTRAlarmB4Addr_Object((1,3,6,1,2,1,240,1,3,1,2),_DsliteAFTRAlarmB4Addr_Type())
dsliteAFTRAlarmB4Addr.setMaxAccess(_F)
if mibBuilder.loadTexts:dsliteAFTRAlarmB4Addr.setStatus(_B)
class _DsliteAFTRAlarmProtocolType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('tcp',0),('udp',1),('icmp',2),('total',3)))
_DsliteAFTRAlarmProtocolType_Type.__name__=_E
_DsliteAFTRAlarmProtocolType_Object=MibScalar
dsliteAFTRAlarmProtocolType=_DsliteAFTRAlarmProtocolType_Object((1,3,6,1,2,1,240,1,3,1,3),_DsliteAFTRAlarmProtocolType_Type())
dsliteAFTRAlarmProtocolType.setMaxAccess(_F)
if mibBuilder.loadTexts:dsliteAFTRAlarmProtocolType.setStatus(_B)
_DsliteAFTRAlarmSpecificIPAddrType_Type=InetAddressType
_DsliteAFTRAlarmSpecificIPAddrType_Object=MibScalar
dsliteAFTRAlarmSpecificIPAddrType=_DsliteAFTRAlarmSpecificIPAddrType_Object((1,3,6,1,2,1,240,1,3,1,4),_DsliteAFTRAlarmSpecificIPAddrType_Type())
dsliteAFTRAlarmSpecificIPAddrType.setMaxAccess(_F)
if mibBuilder.loadTexts:dsliteAFTRAlarmSpecificIPAddrType.setStatus(_B)
_DsliteAFTRAlarmSpecificIP_Type=InetAddress
_DsliteAFTRAlarmSpecificIP_Object=MibScalar
dsliteAFTRAlarmSpecificIP=_DsliteAFTRAlarmSpecificIP_Object((1,3,6,1,2,1,240,1,3,1,5),_DsliteAFTRAlarmSpecificIP_Type())
dsliteAFTRAlarmSpecificIP.setMaxAccess(_F)
if mibBuilder.loadTexts:dsliteAFTRAlarmSpecificIP.setStatus(_B)
class _DsliteAFTRAlarmConnectNumber_Type(Integer32):defaultValue=60;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(60,90))
_DsliteAFTRAlarmConnectNumber_Type.__name__=_E
_DsliteAFTRAlarmConnectNumber_Object=MibScalar
dsliteAFTRAlarmConnectNumber=_DsliteAFTRAlarmConnectNumber_Object((1,3,6,1,2,1,240,1,3,1,6),_DsliteAFTRAlarmConnectNumber_Type())
dsliteAFTRAlarmConnectNumber.setMaxAccess(_O)
if mibBuilder.loadTexts:dsliteAFTRAlarmConnectNumber.setStatus(_B)
class _DsliteAFTRAlarmSessionNumber_Type(Integer32):defaultValue=-1
_DsliteAFTRAlarmSessionNumber_Type.__name__=_E
_DsliteAFTRAlarmSessionNumber_Object=MibScalar
dsliteAFTRAlarmSessionNumber=_DsliteAFTRAlarmSessionNumber_Object((1,3,6,1,2,1,240,1,3,1,7),_DsliteAFTRAlarmSessionNumber_Type())
dsliteAFTRAlarmSessionNumber.setMaxAccess(_O)
if mibBuilder.loadTexts:dsliteAFTRAlarmSessionNumber.setStatus(_B)
class _DsliteAFTRAlarmPortNumber_Type(Integer32):defaultValue=-1
_DsliteAFTRAlarmPortNumber_Type.__name__=_E
_DsliteAFTRAlarmPortNumber_Object=MibScalar
dsliteAFTRAlarmPortNumber=_DsliteAFTRAlarmPortNumber_Object((1,3,6,1,2,1,240,1,3,1,8),_DsliteAFTRAlarmPortNumber_Type())
dsliteAFTRAlarmPortNumber.setMaxAccess(_O)
if mibBuilder.loadTexts:dsliteAFTRAlarmPortNumber.setStatus(_B)
_DsliteStatisticsTable_Object=MibTable
dsliteStatisticsTable=_DsliteStatisticsTable_Object((1,3,6,1,2,1,240,1,3,2))
if mibBuilder.loadTexts:dsliteStatisticsTable.setStatus(_B)
_DsliteStatisticsEntry_Object=MibTableRow
dsliteStatisticsEntry=_DsliteStatisticsEntry_Object((1,3,6,1,2,1,240,1,3,2,1))
dsliteStatisticsEntry.setIndexNames((0,_A,_d))
if mibBuilder.loadTexts:dsliteStatisticsEntry.setStatus(_B)
_DsliteStatisticsSubscriberIndex_Type=Natv2SubscriberIndex
_DsliteStatisticsSubscriberIndex_Object=MibTableColumn
dsliteStatisticsSubscriberIndex=_DsliteStatisticsSubscriberIndex_Object((1,3,6,1,2,1,240,1,3,2,1,1),_DsliteStatisticsSubscriberIndex_Type())
dsliteStatisticsSubscriberIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:dsliteStatisticsSubscriberIndex.setStatus(_B)
_DsliteStatisticsDiscards_Type=Counter64
_DsliteStatisticsDiscards_Object=MibTableColumn
dsliteStatisticsDiscards=_DsliteStatisticsDiscards_Object((1,3,6,1,2,1,240,1,3,2,1,2),_DsliteStatisticsDiscards_Type())
dsliteStatisticsDiscards.setMaxAccess(_C)
if mibBuilder.loadTexts:dsliteStatisticsDiscards.setStatus(_B)
_DsliteStatisticsSends_Type=Counter64
_DsliteStatisticsSends_Object=MibTableColumn
dsliteStatisticsSends=_DsliteStatisticsSends_Object((1,3,6,1,2,1,240,1,3,2,1,3),_DsliteStatisticsSends_Type())
dsliteStatisticsSends.setMaxAccess(_C)
if mibBuilder.loadTexts:dsliteStatisticsSends.setStatus(_B)
_DsliteStatisticsReceives_Type=Counter64
_DsliteStatisticsReceives_Object=MibTableColumn
dsliteStatisticsReceives=_DsliteStatisticsReceives_Object((1,3,6,1,2,1,240,1,3,2,1,4),_DsliteStatisticsReceives_Type())
dsliteStatisticsReceives.setMaxAccess(_C)
if mibBuilder.loadTexts:dsliteStatisticsReceives.setStatus(_B)
_DsliteStatisticsIpv4Session_Type=Counter64
_DsliteStatisticsIpv4Session_Object=MibTableColumn
dsliteStatisticsIpv4Session=_DsliteStatisticsIpv4Session_Object((1,3,6,1,2,1,240,1,3,2,1,5),_DsliteStatisticsIpv4Session_Type())
dsliteStatisticsIpv4Session.setMaxAccess(_C)
if mibBuilder.loadTexts:dsliteStatisticsIpv4Session.setStatus(_B)
_DsliteStatisticsIpv6Session_Type=Counter64
_DsliteStatisticsIpv6Session_Object=MibTableColumn
dsliteStatisticsIpv6Session=_DsliteStatisticsIpv6Session_Object((1,3,6,1,2,1,240,1,3,2,1,6),_DsliteStatisticsIpv6Session_Type())
dsliteStatisticsIpv6Session.setMaxAccess(_C)
if mibBuilder.loadTexts:dsliteStatisticsIpv6Session.setStatus(_B)
_DsliteConformance_ObjectIdentity=ObjectIdentity
dsliteConformance=_DsliteConformance_ObjectIdentity((1,3,6,1,2,1,240,2))
_DsliteCompliances_ObjectIdentity=ObjectIdentity
dsliteCompliances=_DsliteCompliances_ObjectIdentity((1,3,6,1,2,1,240,2,1))
_DsliteGroups_ObjectIdentity=ObjectIdentity
dsliteGroups=_DsliteGroups_ObjectIdentity((1,3,6,1,2,1,240,2,2))
dsliteNATBindGroup=ObjectGroup((1,3,6,1,2,1,240,2,2,1))
dsliteNATBindGroup.setObjects(*((_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_i),(_A,_j),(_A,_k),(_A,_l)))
if mibBuilder.loadTexts:dsliteNATBindGroup.setStatus(_B)
dsliteTunnelGroup=ObjectGroup((1,3,6,1,2,1,240,2,2,2))
dsliteTunnelGroup.setObjects((_A,_m))
if mibBuilder.loadTexts:dsliteTunnelGroup.setStatus(_B)
dsliteStatisticsGroup=ObjectGroup((1,3,6,1,2,1,240,2,2,3))
dsliteStatisticsGroup.setObjects(*((_A,_n),(_A,_o),(_A,_p),(_A,_q),(_A,_r)))
if mibBuilder.loadTexts:dsliteStatisticsGroup.setStatus(_B)
dsliteAFTRAlarmScalarGroup=ObjectGroup((1,3,6,1,2,1,240,2,2,5))
dsliteAFTRAlarmScalarGroup.setObjects(*((_A,_H),(_A,_I),(_A,_J),(_A,_P),(_A,_Q),(_A,_s),(_A,_t),(_A,_u)))
if mibBuilder.loadTexts:dsliteAFTRAlarmScalarGroup.setStatus(_B)
dsliteTunnelNumAlarm=NotificationType((1,3,6,1,2,1,240,0,1))
dsliteTunnelNumAlarm.setObjects(*((_A,_J),(_A,_H),(_A,_I)))
if mibBuilder.loadTexts:dsliteTunnelNumAlarm.setStatus(_B)
dsliteAFTRUserSessionNumAlarm=NotificationType((1,3,6,1,2,1,240,0,2))
dsliteAFTRUserSessionNumAlarm.setObjects(*((_A,_J),(_A,_H),(_A,_I)))
if mibBuilder.loadTexts:dsliteAFTRUserSessionNumAlarm.setStatus(_B)
dsliteAFTRPortUsageOfSpecificIpAlarm=NotificationType((1,3,6,1,2,1,240,0,3))
dsliteAFTRPortUsageOfSpecificIpAlarm.setObjects(*((_A,_P),(_A,_Q)))
if mibBuilder.loadTexts:dsliteAFTRPortUsageOfSpecificIpAlarm.setStatus(_B)
dsliteNotificationsGroup=NotificationGroup((1,3,6,1,2,1,240,2,2,4))
dsliteNotificationsGroup.setObjects(*((_A,_v),(_A,_w),(_A,_x)))
if mibBuilder.loadTexts:dsliteNotificationsGroup.setStatus(_B)
dsliteCompliance=ModuleCompliance((1,3,6,1,2,1,240,2,1,1))
dsliteCompliance.setObjects(*((_A,_y),(_A,_z),(_A,_A0),(_A,_A1),(_A,_A2)))
if mibBuilder.loadTexts:dsliteCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'dsliteMIB':dsliteMIB,'dsliteNotifications':dsliteNotifications,_v:dsliteTunnelNumAlarm,_w:dsliteAFTRUserSessionNumAlarm,_x:dsliteAFTRPortUsageOfSpecificIpAlarm,'dsliteMIBObjects':dsliteMIBObjects,'dsliteTunnel':dsliteTunnel,'dsliteTunnelTable':dsliteTunnelTable,'dsliteTunnelEntry':dsliteTunnelEntry,_S:dsliteTunnelAddressType,_N:dsliteTunnelStartAddress,_T:dsliteTunnelEndAddress,_m:dsliteTunnelStartAddPreLen,'dsliteNAT':dsliteNAT,'dsliteNATBindTable':dsliteNATBindTable,'dsliteNATBindEntry':dsliteNATBindEntry,_U:dsliteNATBindMappingInstanceIndex,_V:dsliteNATBindMappingProto,_W:dsliteNATBindMappingExtRealm,_X:dsliteNATBindMappingExtAddressType,_Y:dsliteNATBindMappingExtAddress,_Z:dsliteNATBindMappingExtPort,_e:dsliteNATBindMappingIntRealm,_f:dsliteNATBindMappingIntAddressType,_g:dsliteNATBindMappingIntAddress,_h:dsliteNATBindMappingIntPort,_i:dsliteNATBindMappingPool,_j:dsliteNATBindMappingMapBehavior,_k:dsliteNATBindMappingFilterBehavior,_l:dsliteNATBindMappingAddressPooling,'dsliteInfo':dsliteInfo,'dsliteAFTRAlarmScalar':dsliteAFTRAlarmScalar,_H:dsliteAFTRAlarmB4AddrType,_I:dsliteAFTRAlarmB4Addr,_J:dsliteAFTRAlarmProtocolType,_P:dsliteAFTRAlarmSpecificIPAddrType,_Q:dsliteAFTRAlarmSpecificIP,_s:dsliteAFTRAlarmConnectNumber,_t:dsliteAFTRAlarmSessionNumber,_u:dsliteAFTRAlarmPortNumber,'dsliteStatisticsTable':dsliteStatisticsTable,'dsliteStatisticsEntry':dsliteStatisticsEntry,_d:dsliteStatisticsSubscriberIndex,_n:dsliteStatisticsDiscards,_o:dsliteStatisticsSends,_p:dsliteStatisticsReceives,_q:dsliteStatisticsIpv4Session,_r:dsliteStatisticsIpv6Session,'dsliteConformance':dsliteConformance,'dsliteCompliances':dsliteCompliances,'dsliteCompliance':dsliteCompliance,'dsliteGroups':dsliteGroups,_y:dsliteNATBindGroup,_z:dsliteTunnelGroup,_A0:dsliteStatisticsGroup,_A1:dsliteNotificationsGroup,_A2:dsliteAFTRAlarmScalarGroup})