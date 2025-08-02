_r='hpnicfDhcpRelay2UserInfoIpAddr'
_q='hpnicfDhcpRelay2UserInfoVpnIndex'
_p='hpnicfDhcpRelay2SrvAddrIP'
_o='sysname'
_n='normal'
_m='hpnicfDhcpServer2OptionCode'
_l='hpnicfDhcpServer2RuleHwAddrNumber'
_k='hpnicfDhcpServer2ValidClassName'
_j='hpnicfDhcpServer2DefOptGrpClass'
_i='hpnicfDhcpServer2IPInUseIP'
_h='hpnicfDhcpServer2ExpiredIP'
_g='hpnicfDhcpServer2ConflictIP'
_f='hpnicfDhcpServer2FreeStart'
_e='hpnicfDhcpServer2ForbidEnd'
_d='hpnicfDhcpServer2ForbidStart'
_c='hpnicfDhcpServer2ForbidVpnName'
_b='hpnicfDhcpServer2RuleNumber'
_a='hpnicfDhcpServer2PoolForbidIP'
_Z='hpnicfDhcpServer2PoolOptCode'
_Y='tokenRing'
_X='ethernet'
_W='default'
_V='hpnicfDhcpServer2PoolStaticIP'
_U='hpnicfDhcpServer2PoolClassName'
_T='hpnicfDhcpServer2PoolSecNwMask'
_S='hpnicfDhcpServer2PoolSecNw'
_R='userDefine'
_Q='hpnicfDhcpServer2OptionGroupId'
_P='hpnicfDhcpServer2ClassName'
_O='hex'
_N='ascii'
_M='ifIndex'
_L='IF-MIB'
_K='Unsigned32'
_J='hpnicfDhcpServer2PoolIndex'
_I='TruthValue'
_H='not-accessible'
_G='read-write'
_F='Integer32'
_E='HPN-ICF-DHCP4-MIB'
_D='OctetString'
_C='read-only'
_B='read-create'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_D,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hpnicfCommon,=mibBuilder.importSymbols('HPN-ICF-OID-MIB','hpnicfCommon')
InterfaceIndexOrZero,ifIndex=mibBuilder.importSymbols(_L,'InterfaceIndexOrZero',_M)
InetAddressIPv4,=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddressIPv4')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_K,'iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention',_I)
hpnicfDhcp4=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,15,2,122))
if mibBuilder.loadTexts:hpnicfDhcp4.setRevisions(('2013-04-24 00:00',))
_HpnicfDhcpServer2ScalarObjects_ObjectIdentity=ObjectIdentity
hpnicfDhcpServer2ScalarObjects=_HpnicfDhcpServer2ScalarObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,122,1))
_HpnicfDhcpServer2ConfigGroup_ObjectIdentity=ObjectIdentity
hpnicfDhcpServer2ConfigGroup=_HpnicfDhcpServer2ConfigGroup_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,122,1,1))
class _HpnicfDhcpServer2Enabled_Type(TruthValue):defaultValue=2
_HpnicfDhcpServer2Enabled_Type.__name__=_I
_HpnicfDhcpServer2Enabled_Object=MibScalar
hpnicfDhcpServer2Enabled=_HpnicfDhcpServer2Enabled_Object((1,3,6,1,4,1,11,2,14,11,15,2,122,1,1,1),_HpnicfDhcpServer2Enabled_Type())
hpnicfDhcpServer2Enabled.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfDhcpServer2Enabled.setStatus(_A)
class _HpnicfDhcpServer2AlwaysBroadcast_Type(TruthValue):defaultValue=2
_HpnicfDhcpServer2AlwaysBroadcast_Type.__name__=_I
_HpnicfDhcpServer2AlwaysBroadcast_Object=MibScalar
hpnicfDhcpServer2AlwaysBroadcast=_HpnicfDhcpServer2AlwaysBroadcast_Object((1,3,6,1,4,1,11,2,14,11,15,2,122,1,1,2),_HpnicfDhcpServer2AlwaysBroadcast_Type())
hpnicfDhcpServer2AlwaysBroadcast.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfDhcpServer2AlwaysBroadcast.setStatus(_A)
class _HpnicfDhcpServer2IgnoreBootp_Type(TruthValue):defaultValue=2
_HpnicfDhcpServer2IgnoreBootp_Type.__name__=_I
_HpnicfDhcpServer2IgnoreBootp_Object=MibScalar
hpnicfDhcpServer2IgnoreBootp=_HpnicfDhcpServer2IgnoreBootp_Object((1,3,6,1,4,1,11,2,14,11,15,2,122,1,1,3),_HpnicfDhcpServer2IgnoreBootp_Type())
hpnicfDhcpServer2IgnoreBootp.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfDhcpServer2IgnoreBootp.setStatus(_A)
class _HpnicfDhcpServer2BootpReplyRfc1048_Type(TruthValue):defaultValue=2
_HpnicfDhcpServer2BootpReplyRfc1048_Type.__name__=_I
_HpnicfDhcpServer2BootpReplyRfc1048_Object=MibScalar
hpnicfDhcpServer2BootpReplyRfc1048=_HpnicfDhcpServer2BootpReplyRfc1048_Object((1,3,6,1,4,1,11,2,14,11,15,2,122,1,1,4),_HpnicfDhcpServer2BootpReplyRfc1048_Type())
hpnicfDhcpServer2BootpReplyRfc1048.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfDhcpServer2BootpReplyRfc1048.setStatus(_A)
class _HpnicfDhcpServer2Opt82Enabled_Type(TruthValue):defaultValue=1
_HpnicfDhcpServer2Opt82Enabled_Type.__name__=_I
_HpnicfDhcpServer2Opt82Enabled_Object=MibScalar
hpnicfDhcpServer2Opt82Enabled=_HpnicfDhcpServer2Opt82Enabled_Object((1,3,6,1,4,1,11,2,14,11,15,2,122,1,1,5),_HpnicfDhcpServer2Opt82Enabled_Type())
hpnicfDhcpServer2Opt82Enabled.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfDhcpServer2Opt82Enabled.setStatus(_A)
class _HpnicfDhcpServer2PingNumber_Type(Unsigned32):defaultValue=1;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10))
_HpnicfDhcpServer2PingNumber_Type.__name__=_K
_HpnicfDhcpServer2PingNumber_Object=MibScalar
hpnicfDhcpServer2PingNumber=_HpnicfDhcpServer2PingNumber_Object((1,3,6,1,4,1,11,2,14,11,15,2,122,1,1,6),_HpnicfDhcpServer2PingNumber_Type())
hpnicfDhcpServer2PingNumber.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfDhcpServer2PingNumber.setStatus(_A)
class _HpnicfDhcpServer2PingTimeout_Type(Unsigned32):defaultValue=500;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10000))
_HpnicfDhcpServer2PingTimeout_Type.__name__=_K
_HpnicfDhcpServer2PingTimeout_Object=MibScalar
hpnicfDhcpServer2PingTimeout=_HpnicfDhcpServer2PingTimeout_Object((1,3,6,1,4,1,11,2,14,11,15,2,122,1,1,7),_HpnicfDhcpServer2PingTimeout_Type())
hpnicfDhcpServer2PingTimeout.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfDhcpServer2PingTimeout.setStatus(_A)
_HpnicfDhcpServer2StatGroup_ObjectIdentity=ObjectIdentity
hpnicfDhcpServer2StatGroup=_HpnicfDhcpServer2StatGroup_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,122,1,2))
_HpnicfDhcpServer2BadNum_Type=Counter64
_HpnicfDhcpServer2BadNum_Object=MibScalar
hpnicfDhcpServer2BadNum=_HpnicfDhcpServer2BadNum_Object((1,3,6,1,4,1,11,2,14,11,15,2,122,1,2,1),_HpnicfDhcpServer2BadNum_Type())
hpnicfDhcpServer2BadNum.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDhcpServer2BadNum.setStatus(_A)
_HpnicfDhcpServer2BootpRequestNum_Type=Counter64
_HpnicfDhcpServer2BootpRequestNum_Object=MibScalar
hpnicfDhcpServer2BootpRequestNum=_HpnicfDhcpServer2BootpRequestNum_Object((1,3,6,1,4,1,11,2,14,11,15,2,122,1,2,2),_HpnicfDhcpServer2BootpRequestNum_Type())
hpnicfDhcpServer2BootpRequestNum.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDhcpServer2BootpRequestNum.setStatus(_A)
_HpnicfDhcpServer2DiscoverNum_Type=Counter64
_HpnicfDhcpServer2DiscoverNum_Object=MibScalar
hpnicfDhcpServer2DiscoverNum=_HpnicfDhcpServer2DiscoverNum_Object((1,3,6,1,4,1,11,2,14,11,15,2,122,1,2,3),_HpnicfDhcpServer2DiscoverNum_Type())
hpnicfDhcpServer2DiscoverNum.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDhcpServer2DiscoverNum.setStatus(_A)
_HpnicfDhcpServer2RequestNum_Type=Counter64
_HpnicfDhcpServer2RequestNum_Object=MibScalar
hpnicfDhcpServer2RequestNum=_HpnicfDhcpServer2RequestNum_Object((1,3,6,1,4,1,11,2,14,11,15,2,122,1,2,4),_HpnicfDhcpServer2RequestNum_Type())
hpnicfDhcpServer2RequestNum.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDhcpServer2RequestNum.setStatus(_A)
_HpnicfDhcpServer2DeclineNum_Type=Counter64
_HpnicfDhcpServer2DeclineNum_Object=MibScalar
hpnicfDhcpServer2DeclineNum=_HpnicfDhcpServer2DeclineNum_Object((1,3,6,1,4,1,11,2,14,11,15,2,122,1,2,5),_HpnicfDhcpServer2DeclineNum_Type())
hpnicfDhcpServer2DeclineNum.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDhcpServer2DeclineNum.setStatus(_A)
_HpnicfDhcpServer2ReleaseNum_Type=Counter64
_HpnicfDhcpServer2ReleaseNum_Object=MibScalar
hpnicfDhcpServer2ReleaseNum=_HpnicfDhcpServer2ReleaseNum_Object((1,3,6,1,4,1,11,2,14,11,15,2,122,1,2,6),_HpnicfDhcpServer2ReleaseNum_Type())
hpnicfDhcpServer2ReleaseNum.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDhcpServer2ReleaseNum.setStatus(_A)
_HpnicfDhcpServer2InformNum_Type=Counter64
_HpnicfDhcpServer2InformNum_Object=MibScalar
hpnicfDhcpServer2InformNum=_HpnicfDhcpServer2InformNum_Object((1,3,6,1,4,1,11,2,14,11,15,2,122,1,2,7),_HpnicfDhcpServer2InformNum_Type())
hpnicfDhcpServer2InformNum.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDhcpServer2InformNum.setStatus(_A)
_HpnicfDhcpServer2BootpReplyNum_Type=Counter64
_HpnicfDhcpServer2BootpReplyNum_Object=MibScalar
hpnicfDhcpServer2BootpReplyNum=_HpnicfDhcpServer2BootpReplyNum_Object((1,3,6,1,4,1,11,2,14,11,15,2,122,1,2,8),_HpnicfDhcpServer2BootpReplyNum_Type())
hpnicfDhcpServer2BootpReplyNum.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDhcpServer2BootpReplyNum.setStatus(_A)
_HpnicfDhcpServer2OfferNum_Type=Counter64
_HpnicfDhcpServer2OfferNum_Object=MibScalar
hpnicfDhcpServer2OfferNum=_HpnicfDhcpServer2OfferNum_Object((1,3,6,1,4,1,11,2,14,11,15,2,122,1,2,9),_HpnicfDhcpServer2OfferNum_Type())
hpnicfDhcpServer2OfferNum.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDhcpServer2OfferNum.setStatus(_A)
_HpnicfDhcpServer2AckNum_Type=Counter64
_HpnicfDhcpServer2AckNum_Object=MibScalar
hpnicfDhcpServer2AckNum=_HpnicfDhcpServer2AckNum_Object((1,3,6,1,4,1,11,2,14,11,15,2,122,1,2,10),_HpnicfDhcpServer2AckNum_Type())
hpnicfDhcpServer2AckNum.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDhcpServer2AckNum.setStatus(_A)
_HpnicfDhcpServer2NakNum_Type=Counter64
_HpnicfDhcpServer2NakNum_Object=MibScalar
hpnicfDhcpServer2NakNum=_HpnicfDhcpServer2NakNum_Object((1,3,6,1,4,1,11,2,14,11,15,2,122,1,2,11),_HpnicfDhcpServer2NakNum_Type())
hpnicfDhcpServer2NakNum.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDhcpServer2NakNum.setStatus(_A)
class _HpnicfDhcpServer2TotalPoolUsage_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_HpnicfDhcpServer2TotalPoolUsage_Type.__name__=_K
_HpnicfDhcpServer2TotalPoolUsage_Object=MibScalar
hpnicfDhcpServer2TotalPoolUsage=_HpnicfDhcpServer2TotalPoolUsage_Object((1,3,6,1,4,1,11,2,14,11,15,2,122,1,2,12),_HpnicfDhcpServer2TotalPoolUsage_Type())
hpnicfDhcpServer2TotalPoolUsage.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDhcpServer2TotalPoolUsage.setStatus(_A)
_HpnicfDhcpServer2PoolNumber_Type=Unsigned32
_HpnicfDhcpServer2PoolNumber_Object=MibScalar
hpnicfDhcpServer2PoolNumber=_HpnicfDhcpServer2PoolNumber_Object((1,3,6,1,4,1,11,2,14,11,15,2,122,1,2,13),_HpnicfDhcpServer2PoolNumber_Type())
hpnicfDhcpServer2PoolNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDhcpServer2PoolNumber.setStatus(_A)
_HpnicfDhcpServer2ConflictNum_Type=Unsigned32
_HpnicfDhcpServer2ConflictNum_Object=MibScalar
hpnicfDhcpServer2ConflictNum=_HpnicfDhcpServer2ConflictNum_Object((1,3,6,1,4,1,11,2,14,11,15,2,122,1,2,14),_HpnicfDhcpServer2ConflictNum_Type())
hpnicfDhcpServer2ConflictNum.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDhcpServer2ConflictNum.setStatus(_A)
_HpnicfDhcpServer2AutoBindNum_Type=Unsigned32
_HpnicfDhcpServer2AutoBindNum_Object=MibScalar
hpnicfDhcpServer2AutoBindNum=_HpnicfDhcpServer2AutoBindNum_Object((1,3,6,1,4,1,11,2,14,11,15,2,122,1,2,15),_HpnicfDhcpServer2AutoBindNum_Type())
hpnicfDhcpServer2AutoBindNum.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDhcpServer2AutoBindNum.setStatus(_A)
_HpnicfDhcpServer2ManualBindNum_Type=Unsigned32
_HpnicfDhcpServer2ManualBindNum_Object=MibScalar
hpnicfDhcpServer2ManualBindNum=_HpnicfDhcpServer2ManualBindNum_Object((1,3,6,1,4,1,11,2,14,11,15,2,122,1,2,16),_HpnicfDhcpServer2ManualBindNum_Type())
hpnicfDhcpServer2ManualBindNum.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDhcpServer2ManualBindNum.setStatus(_A)
_HpnicfDhcpServer2ExpiredBindNum_Type=Unsigned32
_HpnicfDhcpServer2ExpiredBindNum_Object=MibScalar
hpnicfDhcpServer2ExpiredBindNum=_HpnicfDhcpServer2ExpiredBindNum_Object((1,3,6,1,4,1,11,2,14,11,15,2,122,1,2,17),_HpnicfDhcpServer2ExpiredBindNum_Type())
hpnicfDhcpServer2ExpiredBindNum.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDhcpServer2ExpiredBindNum.setStatus(_A)
_HpnicfDhcpServer2Tables_ObjectIdentity=ObjectIdentity
hpnicfDhcpServer2Tables=_HpnicfDhcpServer2Tables_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,122,2))
_HpnicfDhcpServer2PoolTable_Object=MibTable
hpnicfDhcpServer2PoolTable=_HpnicfDhcpServer2PoolTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,122,2,1))
if mibBuilder.loadTexts:hpnicfDhcpServer2PoolTable.setStatus(_A)
_HpnicfDhcpServer2PoolEntry_Object=MibTableRow
hpnicfDhcpServer2PoolEntry=_HpnicfDhcpServer2PoolEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,122,2,1,1))
hpnicfDhcpServer2PoolEntry.setIndexNames((0,_E,_J))
if mibBuilder.loadTexts:hpnicfDhcpServer2PoolEntry.setStatus(_A)
class _HpnicfDhcpServer2PoolIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_HpnicfDhcpServer2PoolIndex_Type.__name__=_K
_HpnicfDhcpServer2PoolIndex_Object=MibTableColumn
hpnicfDhcpServer2PoolIndex=_HpnicfDhcpServer2PoolIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,122,2,1,1,1),_HpnicfDhcpServer2PoolIndex_Type())
hpnicfDhcpServer2PoolIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:hpnicfDhcpServer2PoolIndex.setStatus(_A)
class _HpnicfDhcpServer2PoolName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,63))
_HpnicfDhcpServer2PoolName_Type.__name__=_D
_HpnicfDhcpServer2PoolName_Object=MibTableColumn
hpnicfDhcpServer2PoolName=_HpnicfDhcpServer2PoolName_Object((1,3,6,1,4,1,11,2,14,11,15,2,122,2,1,1,2),_HpnicfDhcpServer2PoolName_Type())
hpnicfDhcpServer2PoolName.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDhcpServer2PoolName.setStatus(_A)
class _HpnicfDhcpServer2PoolVpnName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_HpnicfDhcpServer2PoolVpnName_Type.__name__=_D
_HpnicfDhcpServer2PoolVpnName_Object=MibTableColumn
hpnicfDhcpServer2PoolVpnName=_HpnicfDhcpServer2PoolVpnName_Object((1,3,6,1,4,1,11,2,14,11,15,2,122,2,1,1,3),_HpnicfDhcpServer2PoolVpnName_Type())
hpnicfDhcpServer2PoolVpnName.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDhcpServer2PoolVpnName.setStatus(_A)
_HpnicfDhcpServer2PoolNetwork_Type=InetAddressIPv4
_HpnicfDhcpServer2PoolNetwork_Object=MibTableColumn
hpnicfDhcpServer2PoolNetwork=_HpnicfDhcpServer2PoolNetwork_Object((1,3,6,1,4,1,11,2,14,11,15,2,122,2,1,1,4),_HpnicfDhcpServer2PoolNetwork_Type())
hpnicfDhcpServer2PoolNetwork.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDhcpServer2PoolNetwork.setStatus(_A)
_HpnicfDhcpServer2PoolNetworkMask_Type=InetAddressIPv4
_HpnicfDhcpServer2PoolNetworkMask_Object=MibTableColumn
hpnicfDhcpServer2PoolNetworkMask=_HpnicfDhcpServer2PoolNetworkMask_Object((1,3,6,1,4,1,11,2,14,11,15,2,122,2,1,1,5),_HpnicfDhcpServer2PoolNetworkMask_Type())
hpnicfDhcpServer2PoolNetworkMask.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDhcpServer2PoolNetworkMask.setStatus(_A)
_HpnicfDhcpServer2PoolStartAddr_Type=InetAddressIPv4
_HpnicfDhcpServer2PoolStartAddr_Object=MibTableColumn
hpnicfDhcpServer2PoolStartAddr=_HpnicfDhcpServer2PoolStartAddr_Object((1,3,6,1,4,1,11,2,14,11,15,2,122,2,1,1,6),_HpnicfDhcpServer2PoolStartAddr_Type())
hpnicfDhcpServer2PoolStartAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDhcpServer2PoolStartAddr.setStatus(_A)
_HpnicfDhcpServer2PoolEndAddr_Type=InetAddressIPv4
_HpnicfDhcpServer2PoolEndAddr_Object=MibTableColumn
hpnicfDhcpServer2PoolEndAddr=_HpnicfDhcpServer2PoolEndAddr_Object((1,3,6,1,4,1,11,2,14,11,15,2,122,2,1,1,7),_HpnicfDhcpServer2PoolEndAddr_Type())
hpnicfDhcpServer2PoolEndAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDhcpServer2PoolEndAddr.setStatus(_A)
class _HpnicfDhcpServer2PoolLeaseDay_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,365))
_HpnicfDhcpServer2PoolLeaseDay_Type.__name__=_F
_HpnicfDhcpServer2PoolLeaseDay_Object=MibTableColumn
hpnicfDhcpServer2PoolLeaseDay=_HpnicfDhcpServer2PoolLeaseDay_Object((1,3,6,1,4,1,11,2,14,11,15,2,122,2,1,1,8),_HpnicfDhcpServer2PoolLeaseDay_Type())
hpnicfDhcpServer2PoolLeaseDay.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDhcpServer2PoolLeaseDay.setStatus(_A)
class _HpnicfDhcpServer2PoolLeaseHour_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,23))
_HpnicfDhcpServer2PoolLeaseHour_Type.__name__=_F
_HpnicfDhcpServer2PoolLeaseHour_Object=MibTableColumn
hpnicfDhcpServer2PoolLeaseHour=_HpnicfDhcpServer2PoolLeaseHour_Object((1,3,6,1,4,1,11,2,14,11,15,2,122,2,1,1,9),_HpnicfDhcpServer2PoolLeaseHour_Type())
hpnicfDhcpServer2PoolLeaseHour.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDhcpServer2PoolLeaseHour.setStatus(_A)
class _HpnicfDhcpServer2PoolLeaseMinute_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,59))
_HpnicfDhcpServer2PoolLeaseMinute_Type.__name__=_F
_HpnicfDhcpServer2PoolLeaseMinute_Object=MibTableColumn
hpnicfDhcpServer2PoolLeaseMinute=_HpnicfDhcpServer2PoolLeaseMinute_Object((1,3,6,1,4,1,11,2,14,11,15,2,122,2,1,1,10),_HpnicfDhcpServer2PoolLeaseMinute_Type())
hpnicfDhcpServer2PoolLeaseMinute.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDhcpServer2PoolLeaseMinute.setStatus(_A)
class _HpnicfDhcpServer2PoolLeaseSecond_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,59))
_HpnicfDhcpServer2PoolLeaseSecond_Type.__name__=_F
_HpnicfDhcpServer2PoolLeaseSecond_Object=MibTableColumn
hpnicfDhcpServer2PoolLeaseSecond=_HpnicfDhcpServer2PoolLeaseSecond_Object((1,3,6,1,4,1,11,2,14,11,15,2,122,2,1,1,11),_HpnicfDhcpServer2PoolLeaseSecond_Type())
hpnicfDhcpServer2PoolLeaseSecond.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDhcpServer2PoolLeaseSecond.setStatus(_A)
class _HpnicfDhcpServer2PoolLeaseUnlimit_Type(TruthValue):defaultValue=2
_HpnicfDhcpServer2PoolLeaseUnlimit_Type.__name__=_I
_HpnicfDhcpServer2PoolLeaseUnlimit_Object=MibTableColumn
hpnicfDhcpServer2PoolLeaseUnlimit=_HpnicfDhcpServer2PoolLeaseUnlimit_Object((1,3,6,1,4,1,11,2,14,11,15,2,122,2,1,1,12),_HpnicfDhcpServer2PoolLeaseUnlimit_Type())
hpnicfDhcpServer2PoolLeaseUnlimit.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDhcpServer2PoolLeaseUnlimit.setStatus(_A)
_HpnicfDhcpServer2PoolLeaseTime_Type=TimeTicks
_HpnicfDhcpServer2PoolLeaseTime_Object=MibTableColumn
hpnicfDhcpServer2PoolLeaseTime=_HpnicfDhcpServer2PoolLeaseTime_Object((1,3,6,1,4,1,11,2,14,11,15,2,122,2,1,1,13),_HpnicfDhcpServer2PoolLeaseTime_Type())
hpnicfDhcpServer2PoolLeaseTime.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDhcpServer2PoolLeaseTime.setStatus(_A)
class _HpnicfDhcpServer2PoolDomainName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,50))
_HpnicfDhcpServer2PoolDomainName_Type.__name__=_D
_HpnicfDhcpServer2PoolDomainName_Object=MibTableColumn
hpnicfDhcpServer2PoolDomainName=_HpnicfDhcpServer2PoolDomainName_Object((1,3,6,1,4,1,11,2,14,11,15,2,122,2,1,1,14),_HpnicfDhcpServer2PoolDomainName_Type())
hpnicfDhcpServer2PoolDomainName.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDhcpServer2PoolDomainName.setStatus(_A)
class _HpnicfDhcpServer2PoolGatewayIP_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_HpnicfDhcpServer2PoolGatewayIP_Type.__name__=_D
_HpnicfDhcpServer2PoolGatewayIP_Object=MibTableColumn
hpnicfDhcpServer2PoolGatewayIP=_HpnicfDhcpServer2PoolGatewayIP_Object((1,3,6,1,4,1,11,2,14,11,15,2,122,2,1,1,15),_HpnicfDhcpServer2PoolGatewayIP_Type())
hpnicfDhcpServer2PoolGatewayIP.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDhcpServer2PoolGatewayIP.setStatus(_A)
class _HpnicfDhcpServer2PoolDNSIP_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_HpnicfDhcpServer2PoolDNSIP_Type.__name__=_D
_HpnicfDhcpServer2PoolDNSIP_Object=MibTableColumn
hpnicfDhcpServer2PoolDNSIP=_HpnicfDhcpServer2PoolDNSIP_Object((1,3,6,1,4,1,11,2,14,11,15,2,122,2,1,1,16),_HpnicfDhcpServer2PoolDNSIP_Type())
hpnicfDhcpServer2PoolDNSIP.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDhcpServer2PoolDNSIP.setStatus(_A)
_HpnicfDhcpServer2PoolPrimaryDNSIP_Type=InetAddressIPv4
_HpnicfDhcpServer2PoolPrimaryDNSIP_Object=MibTableColumn
hpnicfDhcpServer2PoolPrimaryDNSIP=_HpnicfDhcpServer2PoolPrimaryDNSIP_Object((1,3,6,1,4,1,11,2,14,11,15,2,122,2,1,1,17),_HpnicfDhcpServer2PoolPrimaryDNSIP_Type())
hpnicfDhcpServer2PoolPrimaryDNSIP.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDhcpServer2PoolPrimaryDNSIP.setStatus(_A)
_HpnicfDhcpServer2PoolSecondDNSIP_Type=InetAddressIPv4
_HpnicfDhcpServer2PoolSecondDNSIP_Object=MibTableColumn
hpnicfDhcpServer2PoolSecondDNSIP=_HpnicfDhcpServer2PoolSecondDNSIP_Object((1,3,6,1,4,1,11,2,14,11,15,2,122,2,1,1,18),_HpnicfDhcpServer2PoolSecondDNSIP_Type())
hpnicfDhcpServer2PoolSecondDNSIP.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDhcpServer2PoolSecondDNSIP.setStatus(_A)
class _HpnicfDhcpServer2PoolNetbiosType_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,4,8)));namedValues=NamedValues(*(('null',0),('bnode',1),('pnode',2),('mnode',4),('hnode',8)))
_HpnicfDhcpServer2PoolNetbiosType_Type.__name__=_F
_HpnicfDhcpServer2PoolNetbiosType_Object=MibTableColumn
hpnicfDhcpServer2PoolNetbiosType=_HpnicfDhcpServer2PoolNetbiosType_Object((1,3,6,1,4,1,11,2,14,11,15,2,122,2,1,1,19),_HpnicfDhcpServer2PoolNetbiosType_Type())
hpnicfDhcpServer2PoolNetbiosType.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDhcpServer2PoolNetbiosType.setStatus(_A)
class _HpnicfDhcpServer2PoolNbnsIP_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_HpnicfDhcpServer2PoolNbnsIP_Type.__name__=_D
_HpnicfDhcpServer2PoolNbnsIP_Object=MibTableColumn
hpnicfDhcpServer2PoolNbnsIP=_HpnicfDhcpServer2PoolNbnsIP_Object((1,3,6,1,4,1,11,2,14,11,15,2,122,2,1,1,20),_HpnicfDhcpServer2PoolNbnsIP_Type())
hpnicfDhcpServer2PoolNbnsIP.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDhcpServer2PoolNbnsIP.setStatus(_A)
class _HpnicfDhcpServer2PoolBootFileName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_HpnicfDhcpServer2PoolBootFileName_Type.__name__=_D
_HpnicfDhcpServer2PoolBootFileName_Object=MibTableColumn
hpnicfDhcpServer2PoolBootFileName=_HpnicfDhcpServer2PoolBootFileName_Object((1,3,6,1,4,1,11,2,14,11,15,2,122,2,1,1,21),_HpnicfDhcpServer2PoolBootFileName_Type())
hpnicfDhcpServer2PoolBootFileName.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDhcpServer2PoolBootFileName.setStatus(_A)
_HpnicfDhcpServer2PoolBimsIP_Type=InetAddressIPv4
_HpnicfDhcpServer2PoolBimsIP_Object=MibTableColumn
hpnicfDhcpServer2PoolBimsIP=_HpnicfDhcpServer2PoolBimsIP_Object((1,3,6,1,4,1,11,2,14,11,15,2,122,2,1,1,22),_HpnicfDhcpServer2PoolBimsIP_Type())
hpnicfDhcpServer2PoolBimsIP.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDhcpServer2PoolBimsIP.setStatus(_A)
class _HpnicfDhcpServer2PoolBimsPort_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65534))
_HpnicfDhcpServer2PoolBimsPort_Type.__name__=_K
_HpnicfDhcpServer2PoolBimsPort_Object=MibTableColumn
hpnicfDhcpServer2PoolBimsPort=_HpnicfDhcpServer2PoolBimsPort_Object((1,3,6,1,4,1,11,2,14,11,15,2,122,2,1,1,23),_HpnicfDhcpServer2PoolBimsPort_Type())
hpnicfDhcpServer2PoolBimsPort.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDhcpServer2PoolBimsPort.setStatus(_A)
class _HpnicfDhcpServer2PoolBimsKeyStr_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_HpnicfDhcpServer2PoolBimsKeyStr_Type.__name__=_D
_HpnicfDhcpServer2PoolBimsKeyStr_Object=MibTableColumn
hpnicfDhcpServer2PoolBimsKeyStr=_HpnicfDhcpServer2PoolBimsKeyStr_Object((1,3,6,1,4,1,11,2,14,11,15,2,122,2,1,1,24),_HpnicfDhcpServer2PoolBimsKeyStr_Type())
hpnicfDhcpServer2PoolBimsKeyStr.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDhcpServer2PoolBimsKeyStr.setStatus(_A)
_HpnicfDhcpServer2PoolNextServer_Type=InetAddressIPv4
_HpnicfDhcpServer2PoolNextServer_Object=MibTableColumn
hpnicfDhcpServer2PoolNextServer=_HpnicfDhcpServer2PoolNextServer_Object((1,3,6,1,4,1,11,2,14,11,15,2,122,2,1,1,25),_HpnicfDhcpServer2PoolNextServer_Type())
hpnicfDhcpServer2PoolNextServer.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDhcpServer2PoolNextServer.setStatus(_A)
class _HpnicfDhcpServer2PoolTftpDomName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_HpnicfDhcpServer2PoolTftpDomName_Type.__name__=_D
_HpnicfDhcpServer2PoolTftpDomName_Object=MibTableColumn
hpnicfDhcpServer2PoolTftpDomName=_HpnicfDhcpServer2PoolTftpDomName_Object((1,3,6,1,4,1,11,2,14,11,15,2,122,2,1,1,26),_HpnicfDhcpServer2PoolTftpDomName_Type())
hpnicfDhcpServer2PoolTftpDomName.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDhcpServer2PoolTftpDomName.setStatus(_A)
_HpnicfDhcpServer2PoolTftpIP_Type=InetAddressIPv4
_HpnicfDhcpServer2PoolTftpIP_Object=MibTableColumn
hpnicfDhcpServer2PoolTftpIP=_HpnicfDhcpServer2PoolTftpIP_Object((1,3,6,1,4,1,11,2,14,11,15,2,122,2,1,1,27),_HpnicfDhcpServer2PoolTftpIP_Type())
hpnicfDhcpServer2PoolTftpIP.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDhcpServer2PoolTftpIP.setStatus(_A)
_HpnicfDhcpServer2PoolVoiceAsIP_Type=InetAddressIPv4
_HpnicfDhcpServer2PoolVoiceAsIP_Object=MibTableColumn
hpnicfDhcpServer2PoolVoiceAsIP=_HpnicfDhcpServer2PoolVoiceAsIP_Object((1,3,6,1,4,1,11,2,14,11,15,2,122,2,1,1,28),_HpnicfDhcpServer2PoolVoiceAsIP_Type())
hpnicfDhcpServer2PoolVoiceAsIP.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDhcpServer2PoolVoiceAsIP.setStatus(_A)
_HpnicfDhcpServer2PoolVoiceFailIP_Type=InetAddressIPv4
_HpnicfDhcpServer2PoolVoiceFailIP_Object=MibTableColumn
hpnicfDhcpServer2PoolVoiceFailIP=_HpnicfDhcpServer2PoolVoiceFailIP_Object((1,3,6,1,4,1,11,2,14,11,15,2,122,2,1,1,29),_HpnicfDhcpServer2PoolVoiceFailIP_Type())
hpnicfDhcpServer2PoolVoiceFailIP.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDhcpServer2PoolVoiceFailIP.setStatus(_A)
class _HpnicfDhcpServer2PoolVoiceFailStr_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,39))
_HpnicfDhcpServer2PoolVoiceFailStr_Type.__name__=_D
_HpnicfDhcpServer2PoolVoiceFailStr_Object=MibTableColumn
hpnicfDhcpServer2PoolVoiceFailStr=_HpnicfDhcpServer2PoolVoiceFailStr_Object((1,3,6,1,4,1,11,2,14,11,15,2,122,2,1,1,30),_HpnicfDhcpServer2PoolVoiceFailStr_Type())
hpnicfDhcpServer2PoolVoiceFailStr.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDhcpServer2PoolVoiceFailStr.setStatus(_A)
_HpnicfDhcpServer2PoolVoiceNCPIP_Type=InetAddressIPv4
_HpnicfDhcpServer2PoolVoiceNCPIP_Object=MibTableColumn
hpnicfDhcpServer2PoolVoiceNCPIP=_HpnicfDhcpServer2PoolVoiceNCPIP_Object((1,3,6,1,4,1,11,2,14,11,15,2,122,2,1,1,31),_HpnicfDhcpServer2PoolVoiceNCPIP_Type())
hpnicfDhcpServer2PoolVoiceNCPIP.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDhcpServer2PoolVoiceNCPIP.setStatus(_A)
class _HpnicfDhcpServer2PoolVoiceVlanId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,4094),ValueRangeConstraint(65535,65535))
_HpnicfDhcpServer2PoolVoiceVlanId_Type.__name__=_K
_HpnicfDhcpServer2PoolVoiceVlanId_Object=MibTableColumn
hpnicfDhcpServer2PoolVoiceVlanId=_HpnicfDhcpServer2PoolVoiceVlanId_Object((1,3,6,1,4,1,11,2,14,11,15,2,122,2,1,1,32),_HpnicfDhcpServer2PoolVoiceVlanId_Type())
hpnicfDhcpServer2PoolVoiceVlanId.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDhcpServer2PoolVoiceVlanId.setStatus(_A)
class _HpnicfDhcpServer2PoolVoiceVlanEnbl_Type(TruthValue):defaultValue=2
_HpnicfDhcpServer2PoolVoiceVlanEnbl_Type.__name__=_I
_HpnicfDhcpServer2PoolVoiceVlanEnbl_Object=MibTableColumn
hpnicfDhcpServer2PoolVoiceVlanEnbl=_HpnicfDhcpServer2PoolVoiceVlanEnbl_Object((1,3,6,1,4,1,11,2,14,11,15,2,122,2,1,1,33),_HpnicfDhcpServer2PoolVoiceVlanEnbl_Type())
hpnicfDhcpServer2PoolVoiceVlanEnbl.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDhcpServer2PoolVoiceVlanEnbl.setStatus(_A)
_HpnicfDhcpServer2PoolRowStatus_Type=RowStatus
_HpnicfDhcpServer2PoolRowStatus_Object=MibTableColumn
hpnicfDhcpServer2PoolRowStatus=_HpnicfDhcpServer2PoolRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,122,2,1,1,34),_HpnicfDhcpServer2PoolRowStatus_Type())
hpnicfDhcpServer2PoolRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDhcpServer2PoolRowStatus.setStatus(_A)
class _HpnicfDhcpServer2PoolVerifyClass_Type(TruthValue):defaultValue=2
_HpnicfDhcpServer2PoolVerifyClass_Type.__name__=_I
_HpnicfDhcpServer2PoolVerifyClass_Object=MibTableColumn
hpnicfDhcpServer2PoolVerifyClass=_HpnicfDhcpServer2PoolVerifyClass_Object((1,3,6,1,4,1,11,2,14,11,15,2,122,2,1,1,35),_HpnicfDhcpServer2PoolVerifyClass_Type())
hpnicfDhcpServer2PoolVerifyClass.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDhcpServer2PoolVerifyClass.setStatus(_A)
_HpnicfDhcpServer2IfApplyPoolTable_Object=MibTable
hpnicfDhcpServer2IfApplyPoolTable=_HpnicfDhcpServer2IfApplyPoolTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,122,2,2))
if mibBuilder.loadTexts:hpnicfDhcpServer2IfApplyPoolTable.setStatus(_A)
_HpnicfDhcpServer2IfApplyPoolEntry_Object=MibTableRow
hpnicfDhcpServer2IfApplyPoolEntry=_HpnicfDhcpServer2IfApplyPoolEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,122,2,2,1))
hpnicfDhcpServer2IfApplyPoolEntry.setIndexNames((0,_L,_M))
if mibBuilder.loadTexts:hpnicfDhcpServer2IfApplyPoolEntry.setStatus(_A)
class _HpnicfDhcpServer2IfApplyPoolName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_HpnicfDhcpServer2IfApplyPoolName_Type.__name__=_D
_HpnicfDhcpServer2IfApplyPoolName_Object=MibTableColumn
hpnicfDhcpServer2IfApplyPoolName=_HpnicfDhcpServer2IfApplyPoolName_Object((1,3,6,1,4,1,11,2,14,11,15,2,122,2,2,1,1),_HpnicfDhcpServer2IfApplyPoolName_Type())
hpnicfDhcpServer2IfApplyPoolName.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfDhcpServer2IfApplyPoolName.setStatus(_A)
_HpnicfDhcpServer2PoolSecNwTable_Object=MibTable
hpnicfDhcpServer2PoolSecNwTable=_HpnicfDhcpServer2PoolSecNwTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,122,2,3))
if mibBuilder.loadTexts:hpnicfDhcpServer2PoolSecNwTable.setStatus(_A)
_HpnicfDhcpServer2PoolSecNwEntry_Object=MibTableRow
hpnicfDhcpServer2PoolSecNwEntry=_HpnicfDhcpServer2PoolSecNwEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,122,2,3,1))
hpnicfDhcpServer2PoolSecNwEntry.setIndexNames((0,_E,_J),(0,_E,_S),(0,_E,_T))
if mibBuilder.loadTexts:hpnicfDhcpServer2PoolSecNwEntry.setStatus(_A)
_HpnicfDhcpServer2PoolSecNw_Type=InetAddressIPv4
_HpnicfDhcpServer2PoolSecNw_Object=MibTableColumn
hpnicfDhcpServer2PoolSecNw=_HpnicfDhcpServer2PoolSecNw_Object((1,3,6,1,4,1,11,2,14,11,15,2,122,2,3,1,1),_HpnicfDhcpServer2PoolSecNw_Type())
hpnicfDhcpServer2PoolSecNw.setMaxAccess(_H)
if mibBuilder.loadTexts:hpnicfDhcpServer2PoolSecNw.setStatus(_A)
_HpnicfDhcpServer2PoolSecNwMask_Type=InetAddressIPv4
_HpnicfDhcpServer2PoolSecNwMask_Object=MibTableColumn
hpnicfDhcpServer2PoolSecNwMask=_HpnicfDhcpServer2PoolSecNwMask_Object((1,3,6,1,4,1,11,2,14,11,15,2,122,2,3,1,2),_HpnicfDhcpServer2PoolSecNwMask_Type())
hpnicfDhcpServer2PoolSecNwMask.setMaxAccess(_H)
if mibBuilder.loadTexts:hpnicfDhcpServer2PoolSecNwMask.setStatus(_A)
class _HpnicfDhcpServer2PoolSecNwGwIP_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_HpnicfDhcpServer2PoolSecNwGwIP_Type.__name__=_D
_HpnicfDhcpServer2PoolSecNwGwIP_Object=MibTableColumn
hpnicfDhcpServer2PoolSecNwGwIP=_HpnicfDhcpServer2PoolSecNwGwIP_Object((1,3,6,1,4,1,11,2,14,11,15,2,122,2,3,1,3),_HpnicfDhcpServer2PoolSecNwGwIP_Type())
hpnicfDhcpServer2PoolSecNwGwIP.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDhcpServer2PoolSecNwGwIP.setStatus(_A)
_HpnicfDhcpServer2PoolSecNwStatus_Type=RowStatus
_HpnicfDhcpServer2PoolSecNwStatus_Object=MibTableColumn
hpnicfDhcpServer2PoolSecNwStatus=_HpnicfDhcpServer2PoolSecNwStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,122,2,3,1,4),_HpnicfDhcpServer2PoolSecNwStatus_Type())
hpnicfDhcpServer2PoolSecNwStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDhcpServer2PoolSecNwStatus.setStatus(_A)
_HpnicfDhcpServer2PoolClassTable_Object=MibTable
hpnicfDhcpServer2PoolClassTable=_HpnicfDhcpServer2PoolClassTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,122,2,4))
if mibBuilder.loadTexts:hpnicfDhcpServer2PoolClassTable.setStatus(_A)
_HpnicfDhcpServer2PoolClassEntry_Object=MibTableRow
hpnicfDhcpServer2PoolClassEntry=_HpnicfDhcpServer2PoolClassEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,122,2,4,1))
hpnicfDhcpServer2PoolClassEntry.setIndexNames((0,_E,_J),(0,_E,_U))
if mibBuilder.loadTexts:hpnicfDhcpServer2PoolClassEntry.setStatus(_A)
class _HpnicfDhcpServer2PoolClassName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,63))
_HpnicfDhcpServer2PoolClassName_Type.__name__=_D
_HpnicfDhcpServer2PoolClassName_Object=MibTableColumn
hpnicfDhcpServer2PoolClassName=_HpnicfDhcpServer2PoolClassName_Object((1,3,6,1,4,1,11,2,14,11,15,2,122,2,4,1,1),_HpnicfDhcpServer2PoolClassName_Type())
hpnicfDhcpServer2PoolClassName.setMaxAccess(_H)
if mibBuilder.loadTexts:hpnicfDhcpServer2PoolClassName.setStatus(_A)
_HpnicfDhcpServer2PoolClassStart_Type=InetAddressIPv4
_HpnicfDhcpServer2PoolClassStart_Object=MibTableColumn
hpnicfDhcpServer2PoolClassStart=_HpnicfDhcpServer2PoolClassStart_Object((1,3,6,1,4,1,11,2,14,11,15,2,122,2,4,1,2),_HpnicfDhcpServer2PoolClassStart_Type())
hpnicfDhcpServer2PoolClassStart.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDhcpServer2PoolClassStart.setStatus(_A)
_HpnicfDhcpServer2PoolClassEnd_Type=InetAddressIPv4
_HpnicfDhcpServer2PoolClassEnd_Object=MibTableColumn
hpnicfDhcpServer2PoolClassEnd=_HpnicfDhcpServer2PoolClassEnd_Object((1,3,6,1,4,1,11,2,14,11,15,2,122,2,4,1,3),_HpnicfDhcpServer2PoolClassEnd_Type())
hpnicfDhcpServer2PoolClassEnd.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDhcpServer2PoolClassEnd.setStatus(_A)
_HpnicfDhcpServer2PoolClassStatus_Type=RowStatus
_HpnicfDhcpServer2PoolClassStatus_Object=MibTableColumn
hpnicfDhcpServer2PoolClassStatus=_HpnicfDhcpServer2PoolClassStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,122,2,4,1,4),_HpnicfDhcpServer2PoolClassStatus_Type())
hpnicfDhcpServer2PoolClassStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDhcpServer2PoolClassStatus.setStatus(_A)
_HpnicfDhcpServer2PoolStaticTable_Object=MibTable
hpnicfDhcpServer2PoolStaticTable=_HpnicfDhcpServer2PoolStaticTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,122,2,5))
if mibBuilder.loadTexts:hpnicfDhcpServer2PoolStaticTable.setStatus(_A)
_HpnicfDhcpServer2PoolStaticEntry_Object=MibTableRow
hpnicfDhcpServer2PoolStaticEntry=_HpnicfDhcpServer2PoolStaticEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,122,2,5,1))
hpnicfDhcpServer2PoolStaticEntry.setIndexNames((0,_E,_J),(0,_E,_V))
if mibBuilder.loadTexts:hpnicfDhcpServer2PoolStaticEntry.setStatus(_A)
_HpnicfDhcpServer2PoolStaticIP_Type=InetAddressIPv4
_HpnicfDhcpServer2PoolStaticIP_Object=MibTableColumn
hpnicfDhcpServer2PoolStaticIP=_HpnicfDhcpServer2PoolStaticIP_Object((1,3,6,1,4,1,11,2,14,11,15,2,122,2,5,1,1),_HpnicfDhcpServer2PoolStaticIP_Type())
hpnicfDhcpServer2PoolStaticIP.setMaxAccess(_H)
if mibBuilder.loadTexts:hpnicfDhcpServer2PoolStaticIP.setStatus(_A)
_HpnicfDhcpServer2PoolStaticMask_Type=InetAddressIPv4
_HpnicfDhcpServer2PoolStaticMask_Object=MibTableColumn
hpnicfDhcpServer2PoolStaticMask=_HpnicfDhcpServer2PoolStaticMask_Object((1,3,6,1,4,1,11,2,14,11,15,2,122,2,5,1,2),_HpnicfDhcpServer2PoolStaticMask_Type())
hpnicfDhcpServer2PoolStaticMask.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDhcpServer2PoolStaticMask.setStatus(_A)
class _HpnicfDhcpServer2PoolStaticCID_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,0),ValueSizeConstraint(4,254))
_HpnicfDhcpServer2PoolStaticCID_Type.__name__=_D
_HpnicfDhcpServer2PoolStaticCID_Object=MibTableColumn
hpnicfDhcpServer2PoolStaticCID=_HpnicfDhcpServer2PoolStaticCID_Object((1,3,6,1,4,1,11,2,14,11,15,2,122,2,5,1,3),_HpnicfDhcpServer2PoolStaticCID_Type())
hpnicfDhcpServer2PoolStaticCID.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDhcpServer2PoolStaticCID.setStatus(_A)
class _HpnicfDhcpServer2PoolStaticHAddr_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,0),ValueSizeConstraint(4,39))
_HpnicfDhcpServer2PoolStaticHAddr_Type.__name__=_D
_HpnicfDhcpServer2PoolStaticHAddr_Object=MibTableColumn
hpnicfDhcpServer2PoolStaticHAddr=_HpnicfDhcpServer2PoolStaticHAddr_Object((1,3,6,1,4,1,11,2,14,11,15,2,122,2,5,1,4),_HpnicfDhcpServer2PoolStaticHAddr_Type())
hpnicfDhcpServer2PoolStaticHAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDhcpServer2PoolStaticHAddr.setStatus(_A)
class _HpnicfDhcpServer2PoolStaticHType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_W,1),(_X,2),(_Y,3)))
_HpnicfDhcpServer2PoolStaticHType_Type.__name__=_F
_HpnicfDhcpServer2PoolStaticHType_Object=MibTableColumn
hpnicfDhcpServer2PoolStaticHType=_HpnicfDhcpServer2PoolStaticHType_Object((1,3,6,1,4,1,11,2,14,11,15,2,122,2,5,1,5),_HpnicfDhcpServer2PoolStaticHType_Type())
hpnicfDhcpServer2PoolStaticHType.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDhcpServer2PoolStaticHType.setStatus(_A)
_HpnicfDhcpServer2PoolStaticStatus_Type=RowStatus
_HpnicfDhcpServer2PoolStaticStatus_Object=MibTableColumn
hpnicfDhcpServer2PoolStaticStatus=_HpnicfDhcpServer2PoolStaticStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,122,2,5,1,6),_HpnicfDhcpServer2PoolStaticStatus_Type())
hpnicfDhcpServer2PoolStaticStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDhcpServer2PoolStaticStatus.setStatus(_A)
_HpnicfDhcpServer2PoolOptionTable_Object=MibTable
hpnicfDhcpServer2PoolOptionTable=_HpnicfDhcpServer2PoolOptionTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,122,2,6))
if mibBuilder.loadTexts:hpnicfDhcpServer2PoolOptionTable.setStatus(_A)
_HpnicfDhcpServer2PoolOptionEntry_Object=MibTableRow
hpnicfDhcpServer2PoolOptionEntry=_HpnicfDhcpServer2PoolOptionEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,122,2,6,1))
hpnicfDhcpServer2PoolOptionEntry.setIndexNames((0,_E,_J),(0,_E,_Z))
if mibBuilder.loadTexts:hpnicfDhcpServer2PoolOptionEntry.setStatus(_A)
class _HpnicfDhcpServer2PoolOptCode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,254))
_HpnicfDhcpServer2PoolOptCode_Type.__name__=_F
_HpnicfDhcpServer2PoolOptCode_Object=MibTableColumn
hpnicfDhcpServer2PoolOptCode=_HpnicfDhcpServer2PoolOptCode_Object((1,3,6,1,4,1,11,2,14,11,15,2,122,2,6,1,1),_HpnicfDhcpServer2PoolOptCode_Type())
hpnicfDhcpServer2PoolOptCode.setMaxAccess(_H)
if mibBuilder.loadTexts:hpnicfDhcpServer2PoolOptCode.setStatus(_A)
class _HpnicfDhcpServer2PoolOptType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_N,1),(_O,2),('ip',3)))
_HpnicfDhcpServer2PoolOptType_Type.__name__=_F
_HpnicfDhcpServer2PoolOptType_Object=MibTableColumn
hpnicfDhcpServer2PoolOptType=_HpnicfDhcpServer2PoolOptType_Object((1,3,6,1,4,1,11,2,14,11,15,2,122,2,6,1,2),_HpnicfDhcpServer2PoolOptType_Type())
hpnicfDhcpServer2PoolOptType.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDhcpServer2PoolOptType.setStatus(_A)
class _HpnicfDhcpServer2PoolOptAscii_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_HpnicfDhcpServer2PoolOptAscii_Type.__name__=_D
_HpnicfDhcpServer2PoolOptAscii_Object=MibTableColumn
hpnicfDhcpServer2PoolOptAscii=_HpnicfDhcpServer2PoolOptAscii_Object((1,3,6,1,4,1,11,2,14,11,15,2,122,2,6,1,3),_HpnicfDhcpServer2PoolOptAscii_Type())
hpnicfDhcpServer2PoolOptAscii.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDhcpServer2PoolOptAscii.setStatus(_A)
class _HpnicfDhcpServer2PoolOptHexStr_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,510))
_HpnicfDhcpServer2PoolOptHexStr_Type.__name__=_D
_HpnicfDhcpServer2PoolOptHexStr_Object=MibTableColumn
hpnicfDhcpServer2PoolOptHexStr=_HpnicfDhcpServer2PoolOptHexStr_Object((1,3,6,1,4,1,11,2,14,11,15,2,122,2,6,1,4),_HpnicfDhcpServer2PoolOptHexStr_Type())
hpnicfDhcpServer2PoolOptHexStr.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDhcpServer2PoolOptHexStr.setStatus(_A)
class _HpnicfDhcpServer2PoolOptIPStr_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_HpnicfDhcpServer2PoolOptIPStr_Type.__name__=_D
_HpnicfDhcpServer2PoolOptIPStr_Object=MibTableColumn
hpnicfDhcpServer2PoolOptIPStr=_HpnicfDhcpServer2PoolOptIPStr_Object((1,3,6,1,4,1,11,2,14,11,15,2,122,2,6,1,5),_HpnicfDhcpServer2PoolOptIPStr_Type())
hpnicfDhcpServer2PoolOptIPStr.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDhcpServer2PoolOptIPStr.setStatus(_A)
_HpnicfDhcpServer2PoolOptRowStatus_Type=RowStatus
_HpnicfDhcpServer2PoolOptRowStatus_Object=MibTableColumn
hpnicfDhcpServer2PoolOptRowStatus=_HpnicfDhcpServer2PoolOptRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,122,2,6,1,6),_HpnicfDhcpServer2PoolOptRowStatus_Type())
hpnicfDhcpServer2PoolOptRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDhcpServer2PoolOptRowStatus.setStatus(_A)
_HpnicfDhcpServer2PoolForbidTable_Object=MibTable
hpnicfDhcpServer2PoolForbidTable=_HpnicfDhcpServer2PoolForbidTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,122,2,7))
if mibBuilder.loadTexts:hpnicfDhcpServer2PoolForbidTable.setStatus(_A)
_HpnicfDhcpServer2PoolForbidEntry_Object=MibTableRow
hpnicfDhcpServer2PoolForbidEntry=_HpnicfDhcpServer2PoolForbidEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,122,2,7,1))
hpnicfDhcpServer2PoolForbidEntry.setIndexNames((0,_E,_J),(0,_E,_a))
if mibBuilder.loadTexts:hpnicfDhcpServer2PoolForbidEntry.setStatus(_A)
_HpnicfDhcpServer2PoolForbidIP_Type=InetAddressIPv4
_HpnicfDhcpServer2PoolForbidIP_Object=MibTableColumn
hpnicfDhcpServer2PoolForbidIP=_HpnicfDhcpServer2PoolForbidIP_Object((1,3,6,1,4,1,11,2,14,11,15,2,122,2,7,1,1),_HpnicfDhcpServer2PoolForbidIP_Type())
hpnicfDhcpServer2PoolForbidIP.setMaxAccess(_H)
if mibBuilder.loadTexts:hpnicfDhcpServer2PoolForbidIP.setStatus(_A)
_HpnicfDhcpServer2PoolForbidStatus_Type=RowStatus
_HpnicfDhcpServer2PoolForbidStatus_Object=MibTableColumn
hpnicfDhcpServer2PoolForbidStatus=_HpnicfDhcpServer2PoolForbidStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,122,2,7,1,2),_HpnicfDhcpServer2PoolForbidStatus_Type())
hpnicfDhcpServer2PoolForbidStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDhcpServer2PoolForbidStatus.setStatus(_A)
_HpnicfDhcpServer2ClassTable_Object=MibTable
hpnicfDhcpServer2ClassTable=_HpnicfDhcpServer2ClassTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,122,2,8))
if mibBuilder.loadTexts:hpnicfDhcpServer2ClassTable.setStatus(_A)
_HpnicfDhcpServer2ClassEntry_Object=MibTableRow
hpnicfDhcpServer2ClassEntry=_HpnicfDhcpServer2ClassEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,122,2,8,1))
hpnicfDhcpServer2ClassEntry.setIndexNames((0,_E,_P))
if mibBuilder.loadTexts:hpnicfDhcpServer2ClassEntry.setStatus(_A)
class _HpnicfDhcpServer2ClassName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,63))
_HpnicfDhcpServer2ClassName_Type.__name__=_D
_HpnicfDhcpServer2ClassName_Object=MibTableColumn
hpnicfDhcpServer2ClassName=_HpnicfDhcpServer2ClassName_Object((1,3,6,1,4,1,11,2,14,11,15,2,122,2,8,1,1),_HpnicfDhcpServer2ClassName_Type())
hpnicfDhcpServer2ClassName.setMaxAccess(_H)
if mibBuilder.loadTexts:hpnicfDhcpServer2ClassName.setStatus(_A)
_HpnicfDhcpServer2ClassRowStatus_Type=RowStatus
_HpnicfDhcpServer2ClassRowStatus_Object=MibTableColumn
hpnicfDhcpServer2ClassRowStatus=_HpnicfDhcpServer2ClassRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,122,2,8,1,2),_HpnicfDhcpServer2ClassRowStatus_Type())
hpnicfDhcpServer2ClassRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDhcpServer2ClassRowStatus.setStatus(_A)
_HpnicfDhcpServer2RuleTable_Object=MibTable
hpnicfDhcpServer2RuleTable=_HpnicfDhcpServer2RuleTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,122,2,9))
if mibBuilder.loadTexts:hpnicfDhcpServer2RuleTable.setStatus(_A)
_HpnicfDhcpServer2RuleEntry_Object=MibTableRow
hpnicfDhcpServer2RuleEntry=_HpnicfDhcpServer2RuleEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,122,2,9,1))
hpnicfDhcpServer2RuleEntry.setIndexNames((0,_E,_P),(0,_E,_b))
if mibBuilder.loadTexts:hpnicfDhcpServer2RuleEntry.setStatus(_A)
class _HpnicfDhcpServer2RuleNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_HpnicfDhcpServer2RuleNumber_Type.__name__=_F
_HpnicfDhcpServer2RuleNumber_Object=MibTableColumn
hpnicfDhcpServer2RuleNumber=_HpnicfDhcpServer2RuleNumber_Object((1,3,6,1,4,1,11,2,14,11,15,2,122,2,9,1,1),_HpnicfDhcpServer2RuleNumber_Type())
hpnicfDhcpServer2RuleNumber.setMaxAccess(_H)
if mibBuilder.loadTexts:hpnicfDhcpServer2RuleNumber.setStatus(_A)
class _HpnicfDhcpServer2RuleOptCode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,254))
_HpnicfDhcpServer2RuleOptCode_Type.__name__=_F
_HpnicfDhcpServer2RuleOptCode_Object=MibTableColumn
hpnicfDhcpServer2RuleOptCode=_HpnicfDhcpServer2RuleOptCode_Object((1,3,6,1,4,1,11,2,14,11,15,2,122,2,9,1,2),_HpnicfDhcpServer2RuleOptCode_Type())
hpnicfDhcpServer2RuleOptCode.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDhcpServer2RuleOptCode.setStatus(_A)
class _HpnicfDhcpServer2RuleOptHexStr_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,510))
_HpnicfDhcpServer2RuleOptHexStr_Type.__name__=_D
_HpnicfDhcpServer2RuleOptHexStr_Object=MibTableColumn
hpnicfDhcpServer2RuleOptHexStr=_HpnicfDhcpServer2RuleOptHexStr_Object((1,3,6,1,4,1,11,2,14,11,15,2,122,2,9,1,3),_HpnicfDhcpServer2RuleOptHexStr_Type())
hpnicfDhcpServer2RuleOptHexStr.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDhcpServer2RuleOptHexStr.setStatus(_A)
class _HpnicfDhcpServer2RuleOptMask_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,510))
_HpnicfDhcpServer2RuleOptMask_Type.__name__=_D
_HpnicfDhcpServer2RuleOptMask_Object=MibTableColumn
hpnicfDhcpServer2RuleOptMask=_HpnicfDhcpServer2RuleOptMask_Object((1,3,6,1,4,1,11,2,14,11,15,2,122,2,9,1,4),_HpnicfDhcpServer2RuleOptMask_Type())
hpnicfDhcpServer2RuleOptMask.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDhcpServer2RuleOptMask.setStatus(_A)
class _HpnicfDhcpServer2RuleOptOffset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,254))
_HpnicfDhcpServer2RuleOptOffset_Type.__name__=_F
_HpnicfDhcpServer2RuleOptOffset_Object=MibTableColumn
hpnicfDhcpServer2RuleOptOffset=_HpnicfDhcpServer2RuleOptOffset_Object((1,3,6,1,4,1,11,2,14,11,15,2,122,2,9,1,5),_HpnicfDhcpServer2RuleOptOffset_Type())
hpnicfDhcpServer2RuleOptOffset.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDhcpServer2RuleOptOffset.setStatus(_A)
class _HpnicfDhcpServer2RuleOptLength_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_HpnicfDhcpServer2RuleOptLength_Type.__name__=_F
_HpnicfDhcpServer2RuleOptLength_Object=MibTableColumn
hpnicfDhcpServer2RuleOptLength=_HpnicfDhcpServer2RuleOptLength_Object((1,3,6,1,4,1,11,2,14,11,15,2,122,2,9,1,6),_HpnicfDhcpServer2RuleOptLength_Type())
hpnicfDhcpServer2RuleOptLength.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDhcpServer2RuleOptLength.setStatus(_A)
_HpnicfDhcpServer2RuleRowStatus_Type=RowStatus
_HpnicfDhcpServer2RuleRowStatus_Object=MibTableColumn
hpnicfDhcpServer2RuleRowStatus=_HpnicfDhcpServer2RuleRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,122,2,9,1,7),_HpnicfDhcpServer2RuleRowStatus_Type())
hpnicfDhcpServer2RuleRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDhcpServer2RuleRowStatus.setStatus(_A)
_HpnicfDhcpServer2ForbidTable_Object=MibTable
hpnicfDhcpServer2ForbidTable=_HpnicfDhcpServer2ForbidTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,122,2,10))
if mibBuilder.loadTexts:hpnicfDhcpServer2ForbidTable.setStatus(_A)
_HpnicfDhcpServer2ForbidEntry_Object=MibTableRow
hpnicfDhcpServer2ForbidEntry=_HpnicfDhcpServer2ForbidEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,122,2,10,1))
hpnicfDhcpServer2ForbidEntry.setIndexNames((0,_E,_c),(0,_E,_d),(0,_E,_e))
if mibBuilder.loadTexts:hpnicfDhcpServer2ForbidEntry.setStatus(_A)
class _HpnicfDhcpServer2ForbidVpnName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,31))
_HpnicfDhcpServer2ForbidVpnName_Type.__name__=_D
_HpnicfDhcpServer2ForbidVpnName_Object=MibTableColumn
hpnicfDhcpServer2ForbidVpnName=_HpnicfDhcpServer2ForbidVpnName_Object((1,3,6,1,4,1,11,2,14,11,15,2,122,2,10,1,1),_HpnicfDhcpServer2ForbidVpnName_Type())
hpnicfDhcpServer2ForbidVpnName.setMaxAccess(_H)
if mibBuilder.loadTexts:hpnicfDhcpServer2ForbidVpnName.setStatus(_A)
_HpnicfDhcpServer2ForbidStart_Type=InetAddressIPv4
_HpnicfDhcpServer2ForbidStart_Object=MibTableColumn
hpnicfDhcpServer2ForbidStart=_HpnicfDhcpServer2ForbidStart_Object((1,3,6,1,4,1,11,2,14,11,15,2,122,2,10,1,2),_HpnicfDhcpServer2ForbidStart_Type())
hpnicfDhcpServer2ForbidStart.setMaxAccess(_H)
if mibBuilder.loadTexts:hpnicfDhcpServer2ForbidStart.setStatus(_A)
_HpnicfDhcpServer2ForbidEnd_Type=InetAddressIPv4
_HpnicfDhcpServer2ForbidEnd_Object=MibTableColumn
hpnicfDhcpServer2ForbidEnd=_HpnicfDhcpServer2ForbidEnd_Object((1,3,6,1,4,1,11,2,14,11,15,2,122,2,10,1,3),_HpnicfDhcpServer2ForbidEnd_Type())
hpnicfDhcpServer2ForbidEnd.setMaxAccess(_H)
if mibBuilder.loadTexts:hpnicfDhcpServer2ForbidEnd.setStatus(_A)
_HpnicfDhcpServer2ForbidRowStatus_Type=RowStatus
_HpnicfDhcpServer2ForbidRowStatus_Object=MibTableColumn
hpnicfDhcpServer2ForbidRowStatus=_HpnicfDhcpServer2ForbidRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,122,2,10,1,4),_HpnicfDhcpServer2ForbidRowStatus_Type())
hpnicfDhcpServer2ForbidRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDhcpServer2ForbidRowStatus.setStatus(_A)
_HpnicfDhcpServer2FreeTable_Object=MibTable
hpnicfDhcpServer2FreeTable=_HpnicfDhcpServer2FreeTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,122,2,11))
if mibBuilder.loadTexts:hpnicfDhcpServer2FreeTable.setStatus(_A)
_HpnicfDhcpServer2FreeEntry_Object=MibTableRow
hpnicfDhcpServer2FreeEntry=_HpnicfDhcpServer2FreeEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,122,2,11,1))
hpnicfDhcpServer2FreeEntry.setIndexNames((0,_E,_J),(0,_E,_f))
if mibBuilder.loadTexts:hpnicfDhcpServer2FreeEntry.setStatus(_A)
_HpnicfDhcpServer2FreeStart_Type=InetAddressIPv4
_HpnicfDhcpServer2FreeStart_Object=MibTableColumn
hpnicfDhcpServer2FreeStart=_HpnicfDhcpServer2FreeStart_Object((1,3,6,1,4,1,11,2,14,11,15,2,122,2,11,1,1),_HpnicfDhcpServer2FreeStart_Type())
hpnicfDhcpServer2FreeStart.setMaxAccess(_H)
if mibBuilder.loadTexts:hpnicfDhcpServer2FreeStart.setStatus(_A)
_HpnicfDhcpServer2FreeEnd_Type=InetAddressIPv4
_HpnicfDhcpServer2FreeEnd_Object=MibTableColumn
hpnicfDhcpServer2FreeEnd=_HpnicfDhcpServer2FreeEnd_Object((1,3,6,1,4,1,11,2,14,11,15,2,122,2,11,1,2),_HpnicfDhcpServer2FreeEnd_Type())
hpnicfDhcpServer2FreeEnd.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDhcpServer2FreeEnd.setStatus(_A)
_HpnicfDhcpServer2ConflictTable_Object=MibTable
hpnicfDhcpServer2ConflictTable=_HpnicfDhcpServer2ConflictTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,122,2,12))
if mibBuilder.loadTexts:hpnicfDhcpServer2ConflictTable.setStatus(_A)
_HpnicfDhcpServer2ConflictEntry_Object=MibTableRow
hpnicfDhcpServer2ConflictEntry=_HpnicfDhcpServer2ConflictEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,122,2,12,1))
hpnicfDhcpServer2ConflictEntry.setIndexNames((0,_E,_J),(0,_E,_g))
if mibBuilder.loadTexts:hpnicfDhcpServer2ConflictEntry.setStatus(_A)
_HpnicfDhcpServer2ConflictIP_Type=InetAddressIPv4
_HpnicfDhcpServer2ConflictIP_Object=MibTableColumn
hpnicfDhcpServer2ConflictIP=_HpnicfDhcpServer2ConflictIP_Object((1,3,6,1,4,1,11,2,14,11,15,2,122,2,12,1,1),_HpnicfDhcpServer2ConflictIP_Type())
hpnicfDhcpServer2ConflictIP.setMaxAccess(_H)
if mibBuilder.loadTexts:hpnicfDhcpServer2ConflictIP.setStatus(_A)
class _HpnicfDhcpServer2ConflictType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('detectByServer',1),('detectByClient',2)))
_HpnicfDhcpServer2ConflictType_Type.__name__=_F
_HpnicfDhcpServer2ConflictType_Object=MibTableColumn
hpnicfDhcpServer2ConflictType=_HpnicfDhcpServer2ConflictType_Object((1,3,6,1,4,1,11,2,14,11,15,2,122,2,12,1,2),_HpnicfDhcpServer2ConflictType_Type())
hpnicfDhcpServer2ConflictType.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDhcpServer2ConflictType.setStatus(_A)
class _HpnicfDhcpServer2ConflictTime_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,19))
_HpnicfDhcpServer2ConflictTime_Type.__name__=_D
_HpnicfDhcpServer2ConflictTime_Object=MibTableColumn
hpnicfDhcpServer2ConflictTime=_HpnicfDhcpServer2ConflictTime_Object((1,3,6,1,4,1,11,2,14,11,15,2,122,2,12,1,3),_HpnicfDhcpServer2ConflictTime_Type())
hpnicfDhcpServer2ConflictTime.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDhcpServer2ConflictTime.setStatus(_A)
_HpnicfDhcpServer2ConflictRowStatus_Type=RowStatus
_HpnicfDhcpServer2ConflictRowStatus_Object=MibTableColumn
hpnicfDhcpServer2ConflictRowStatus=_HpnicfDhcpServer2ConflictRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,122,2,12,1,4),_HpnicfDhcpServer2ConflictRowStatus_Type())
hpnicfDhcpServer2ConflictRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDhcpServer2ConflictRowStatus.setStatus(_A)
_HpnicfDhcpServer2ExpiredTable_Object=MibTable
hpnicfDhcpServer2ExpiredTable=_HpnicfDhcpServer2ExpiredTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,122,2,13))
if mibBuilder.loadTexts:hpnicfDhcpServer2ExpiredTable.setStatus(_A)
_HpnicfDhcpServer2ExpiredEntry_Object=MibTableRow
hpnicfDhcpServer2ExpiredEntry=_HpnicfDhcpServer2ExpiredEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,122,2,13,1))
hpnicfDhcpServer2ExpiredEntry.setIndexNames((0,_E,_J),(0,_E,_h))
if mibBuilder.loadTexts:hpnicfDhcpServer2ExpiredEntry.setStatus(_A)
_HpnicfDhcpServer2ExpiredIP_Type=InetAddressIPv4
_HpnicfDhcpServer2ExpiredIP_Object=MibTableColumn
hpnicfDhcpServer2ExpiredIP=_HpnicfDhcpServer2ExpiredIP_Object((1,3,6,1,4,1,11,2,14,11,15,2,122,2,13,1,1),_HpnicfDhcpServer2ExpiredIP_Type())
hpnicfDhcpServer2ExpiredIP.setMaxAccess(_H)
if mibBuilder.loadTexts:hpnicfDhcpServer2ExpiredIP.setStatus(_A)
class _HpnicfDhcpServer2ExpiredClientId_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,254))
_HpnicfDhcpServer2ExpiredClientId_Type.__name__=_D
_HpnicfDhcpServer2ExpiredClientId_Object=MibTableColumn
hpnicfDhcpServer2ExpiredClientId=_HpnicfDhcpServer2ExpiredClientId_Object((1,3,6,1,4,1,11,2,14,11,15,2,122,2,13,1,2),_HpnicfDhcpServer2ExpiredClientId_Type())
hpnicfDhcpServer2ExpiredClientId.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDhcpServer2ExpiredClientId.setStatus(_A)
class _HpnicfDhcpServer2ExpiredTime_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,19))
_HpnicfDhcpServer2ExpiredTime_Type.__name__=_D
_HpnicfDhcpServer2ExpiredTime_Object=MibTableColumn
hpnicfDhcpServer2ExpiredTime=_HpnicfDhcpServer2ExpiredTime_Object((1,3,6,1,4,1,11,2,14,11,15,2,122,2,13,1,3),_HpnicfDhcpServer2ExpiredTime_Type())
hpnicfDhcpServer2ExpiredTime.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDhcpServer2ExpiredTime.setStatus(_A)
_HpnicfDhcpServer2ExpiredRowStatus_Type=RowStatus
_HpnicfDhcpServer2ExpiredRowStatus_Object=MibTableColumn
hpnicfDhcpServer2ExpiredRowStatus=_HpnicfDhcpServer2ExpiredRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,122,2,13,1,4),_HpnicfDhcpServer2ExpiredRowStatus_Type())
hpnicfDhcpServer2ExpiredRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDhcpServer2ExpiredRowStatus.setStatus(_A)
_HpnicfDhcpServer2IPInUseTable_Object=MibTable
hpnicfDhcpServer2IPInUseTable=_HpnicfDhcpServer2IPInUseTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,122,2,14))
if mibBuilder.loadTexts:hpnicfDhcpServer2IPInUseTable.setStatus(_A)
_HpnicfDhcpServer2IPInUseEntry_Object=MibTableRow
hpnicfDhcpServer2IPInUseEntry=_HpnicfDhcpServer2IPInUseEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,122,2,14,1))
hpnicfDhcpServer2IPInUseEntry.setIndexNames((0,_E,_J),(0,_E,_i))
if mibBuilder.loadTexts:hpnicfDhcpServer2IPInUseEntry.setStatus(_A)
_HpnicfDhcpServer2IPInUseIP_Type=InetAddressIPv4
_HpnicfDhcpServer2IPInUseIP_Object=MibTableColumn
hpnicfDhcpServer2IPInUseIP=_HpnicfDhcpServer2IPInUseIP_Object((1,3,6,1,4,1,11,2,14,11,15,2,122,2,14,1,1),_HpnicfDhcpServer2IPInUseIP_Type())
hpnicfDhcpServer2IPInUseIP.setMaxAccess(_H)
if mibBuilder.loadTexts:hpnicfDhcpServer2IPInUseIP.setStatus(_A)
class _HpnicfDhcpServer2IPInUseClientId_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,0),ValueSizeConstraint(4,254))
_HpnicfDhcpServer2IPInUseClientId_Type.__name__=_D
_HpnicfDhcpServer2IPInUseClientId_Object=MibTableColumn
hpnicfDhcpServer2IPInUseClientId=_HpnicfDhcpServer2IPInUseClientId_Object((1,3,6,1,4,1,11,2,14,11,15,2,122,2,14,1,2),_HpnicfDhcpServer2IPInUseClientId_Type())
hpnicfDhcpServer2IPInUseClientId.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDhcpServer2IPInUseClientId.setStatus(_A)
class _HpnicfDhcpServer2IPInUseHardAddr_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,0),ValueSizeConstraint(4,39))
_HpnicfDhcpServer2IPInUseHardAddr_Type.__name__=_D
_HpnicfDhcpServer2IPInUseHardAddr_Object=MibTableColumn
hpnicfDhcpServer2IPInUseHardAddr=_HpnicfDhcpServer2IPInUseHardAddr_Object((1,3,6,1,4,1,11,2,14,11,15,2,122,2,14,1,3),_HpnicfDhcpServer2IPInUseHardAddr_Type())
hpnicfDhcpServer2IPInUseHardAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDhcpServer2IPInUseHardAddr.setStatus(_A)
class _HpnicfDhcpServer2IPInUseHardType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_W,1),(_X,2),(_Y,3)))
_HpnicfDhcpServer2IPInUseHardType_Type.__name__=_F
_HpnicfDhcpServer2IPInUseHardType_Object=MibTableColumn
hpnicfDhcpServer2IPInUseHardType=_HpnicfDhcpServer2IPInUseHardType_Object((1,3,6,1,4,1,11,2,14,11,15,2,122,2,14,1,4),_HpnicfDhcpServer2IPInUseHardType_Type())
hpnicfDhcpServer2IPInUseHardType.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDhcpServer2IPInUseHardType.setStatus(_A)
class _HpnicfDhcpServer2IPInUseVlanId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094),ValueRangeConstraint(65535,65535))
_HpnicfDhcpServer2IPInUseVlanId_Type.__name__=_K
_HpnicfDhcpServer2IPInUseVlanId_Object=MibTableColumn
hpnicfDhcpServer2IPInUseVlanId=_HpnicfDhcpServer2IPInUseVlanId_Object((1,3,6,1,4,1,11,2,14,11,15,2,122,2,14,1,5),_HpnicfDhcpServer2IPInUseVlanId_Type())
hpnicfDhcpServer2IPInUseVlanId.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDhcpServer2IPInUseVlanId.setStatus(_A)
class _HpnicfDhcpServer2IPInUseEndLease_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,19))
_HpnicfDhcpServer2IPInUseEndLease_Type.__name__=_D
_HpnicfDhcpServer2IPInUseEndLease_Object=MibTableColumn
hpnicfDhcpServer2IPInUseEndLease=_HpnicfDhcpServer2IPInUseEndLease_Object((1,3,6,1,4,1,11,2,14,11,15,2,122,2,14,1,6),_HpnicfDhcpServer2IPInUseEndLease_Type())
hpnicfDhcpServer2IPInUseEndLease.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDhcpServer2IPInUseEndLease.setStatus(_A)
class _HpnicfDhcpServer2IPInUseType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('staticUnallocated',1),('staticOffered',2),('staticCommitted',3),('autoOffered',4),('autoCommitted',5)))
_HpnicfDhcpServer2IPInUseType_Type.__name__=_F
_HpnicfDhcpServer2IPInUseType_Object=MibTableColumn
hpnicfDhcpServer2IPInUseType=_HpnicfDhcpServer2IPInUseType_Object((1,3,6,1,4,1,11,2,14,11,15,2,122,2,14,1,7),_HpnicfDhcpServer2IPInUseType_Type())
hpnicfDhcpServer2IPInUseType.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDhcpServer2IPInUseType.setStatus(_A)
_HpnicfDhcpServer2IPInUseIfIndex_Type=InterfaceIndexOrZero
_HpnicfDhcpServer2IPInUseIfIndex_Object=MibTableColumn
hpnicfDhcpServer2IPInUseIfIndex=_HpnicfDhcpServer2IPInUseIfIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,122,2,14,1,8),_HpnicfDhcpServer2IPInUseIfIndex_Type())
hpnicfDhcpServer2IPInUseIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDhcpServer2IPInUseIfIndex.setStatus(_A)
_HpnicfDhcpServer2IPInUseRowStatus_Type=RowStatus
_HpnicfDhcpServer2IPInUseRowStatus_Object=MibTableColumn
hpnicfDhcpServer2IPInUseRowStatus=_HpnicfDhcpServer2IPInUseRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,122,2,14,1,9),_HpnicfDhcpServer2IPInUseRowStatus_Type())
hpnicfDhcpServer2IPInUseRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDhcpServer2IPInUseRowStatus.setStatus(_A)
_HpnicfDhcpServer2DefOptGrpTable_Object=MibTable
hpnicfDhcpServer2DefOptGrpTable=_HpnicfDhcpServer2DefOptGrpTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,122,2,15))
if mibBuilder.loadTexts:hpnicfDhcpServer2DefOptGrpTable.setStatus(_A)
_HpnicfDhcpServer2DefOptGrpEntry_Object=MibTableRow
hpnicfDhcpServer2DefOptGrpEntry=_HpnicfDhcpServer2DefOptGrpEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,122,2,15,1))
hpnicfDhcpServer2DefOptGrpEntry.setIndexNames((0,_E,_J),(0,_E,_j))
if mibBuilder.loadTexts:hpnicfDhcpServer2DefOptGrpEntry.setStatus(_A)
class _HpnicfDhcpServer2DefOptGrpClass_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,63))
_HpnicfDhcpServer2DefOptGrpClass_Type.__name__=_D
_HpnicfDhcpServer2DefOptGrpClass_Object=MibTableColumn
hpnicfDhcpServer2DefOptGrpClass=_HpnicfDhcpServer2DefOptGrpClass_Object((1,3,6,1,4,1,11,2,14,11,15,2,122,2,15,1,1),_HpnicfDhcpServer2DefOptGrpClass_Type())
hpnicfDhcpServer2DefOptGrpClass.setMaxAccess(_H)
if mibBuilder.loadTexts:hpnicfDhcpServer2DefOptGrpClass.setStatus(_A)
class _HpnicfDhcpServer2DefOptGrpId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32768))
_HpnicfDhcpServer2DefOptGrpId_Type.__name__=_F
_HpnicfDhcpServer2DefOptGrpId_Object=MibTableColumn
hpnicfDhcpServer2DefOptGrpId=_HpnicfDhcpServer2DefOptGrpId_Object((1,3,6,1,4,1,11,2,14,11,15,2,122,2,15,1,2),_HpnicfDhcpServer2DefOptGrpId_Type())
hpnicfDhcpServer2DefOptGrpId.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDhcpServer2DefOptGrpId.setStatus(_A)
_HpnicfDhcpServer2DefOptGrpStatus_Type=RowStatus
_HpnicfDhcpServer2DefOptGrpStatus_Object=MibTableColumn
hpnicfDhcpServer2DefOptGrpStatus=_HpnicfDhcpServer2DefOptGrpStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,122,2,15,1,3),_HpnicfDhcpServer2DefOptGrpStatus_Type())
hpnicfDhcpServer2DefOptGrpStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDhcpServer2DefOptGrpStatus.setStatus(_A)
_HpnicfDhcpServer2ValidClassTable_Object=MibTable
hpnicfDhcpServer2ValidClassTable=_HpnicfDhcpServer2ValidClassTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,122,2,16))
if mibBuilder.loadTexts:hpnicfDhcpServer2ValidClassTable.setStatus(_A)
_HpnicfDhcpServer2ValidClassEntry_Object=MibTableRow
hpnicfDhcpServer2ValidClassEntry=_HpnicfDhcpServer2ValidClassEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,122,2,16,1))
hpnicfDhcpServer2ValidClassEntry.setIndexNames((0,_E,_J),(0,_E,_k))
if mibBuilder.loadTexts:hpnicfDhcpServer2ValidClassEntry.setStatus(_A)
class _HpnicfDhcpServer2ValidClassName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,63))
_HpnicfDhcpServer2ValidClassName_Type.__name__=_D
_HpnicfDhcpServer2ValidClassName_Object=MibTableColumn
hpnicfDhcpServer2ValidClassName=_HpnicfDhcpServer2ValidClassName_Object((1,3,6,1,4,1,11,2,14,11,15,2,122,2,16,1,1),_HpnicfDhcpServer2ValidClassName_Type())
hpnicfDhcpServer2ValidClassName.setMaxAccess(_H)
if mibBuilder.loadTexts:hpnicfDhcpServer2ValidClassName.setStatus(_A)
_HpnicfDhcpServer2ValidClassStatus_Type=RowStatus
_HpnicfDhcpServer2ValidClassStatus_Object=MibTableColumn
hpnicfDhcpServer2ValidClassStatus=_HpnicfDhcpServer2ValidClassStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,122,2,16,1,2),_HpnicfDhcpServer2ValidClassStatus_Type())
hpnicfDhcpServer2ValidClassStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDhcpServer2ValidClassStatus.setStatus(_A)
_HpnicfDhcpServer2RuleHwAddrTable_Object=MibTable
hpnicfDhcpServer2RuleHwAddrTable=_HpnicfDhcpServer2RuleHwAddrTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,122,2,17))
if mibBuilder.loadTexts:hpnicfDhcpServer2RuleHwAddrTable.setStatus(_A)
_HpnicfDhcpServer2RuleHwAddrEntry_Object=MibTableRow
hpnicfDhcpServer2RuleHwAddrEntry=_HpnicfDhcpServer2RuleHwAddrEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,122,2,17,1))
hpnicfDhcpServer2RuleHwAddrEntry.setIndexNames((0,_E,_P),(0,_E,_l))
if mibBuilder.loadTexts:hpnicfDhcpServer2RuleHwAddrEntry.setStatus(_A)
class _HpnicfDhcpServer2RuleHwAddrNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_HpnicfDhcpServer2RuleHwAddrNumber_Type.__name__=_F
_HpnicfDhcpServer2RuleHwAddrNumber_Object=MibTableColumn
hpnicfDhcpServer2RuleHwAddrNumber=_HpnicfDhcpServer2RuleHwAddrNumber_Object((1,3,6,1,4,1,11,2,14,11,15,2,122,2,17,1,1),_HpnicfDhcpServer2RuleHwAddrNumber_Type())
hpnicfDhcpServer2RuleHwAddrNumber.setMaxAccess(_H)
if mibBuilder.loadTexts:hpnicfDhcpServer2RuleHwAddrNumber.setStatus(_A)
class _HpnicfDhcpServer2RuleHwAddress_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,39))
_HpnicfDhcpServer2RuleHwAddress_Type.__name__=_D
_HpnicfDhcpServer2RuleHwAddress_Object=MibTableColumn
hpnicfDhcpServer2RuleHwAddress=_HpnicfDhcpServer2RuleHwAddress_Object((1,3,6,1,4,1,11,2,14,11,15,2,122,2,17,1,2),_HpnicfDhcpServer2RuleHwAddress_Type())
hpnicfDhcpServer2RuleHwAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDhcpServer2RuleHwAddress.setStatus(_A)
class _HpnicfDhcpServer2RuleHwAddrMask_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,39))
_HpnicfDhcpServer2RuleHwAddrMask_Type.__name__=_D
_HpnicfDhcpServer2RuleHwAddrMask_Object=MibTableColumn
hpnicfDhcpServer2RuleHwAddrMask=_HpnicfDhcpServer2RuleHwAddrMask_Object((1,3,6,1,4,1,11,2,14,11,15,2,122,2,17,1,3),_HpnicfDhcpServer2RuleHwAddrMask_Type())
hpnicfDhcpServer2RuleHwAddrMask.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDhcpServer2RuleHwAddrMask.setStatus(_A)
class _HpnicfDhcpServer2RuleHwAddrType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_HpnicfDhcpServer2RuleHwAddrType_Type.__name__=_F
_HpnicfDhcpServer2RuleHwAddrType_Object=MibTableColumn
hpnicfDhcpServer2RuleHwAddrType=_HpnicfDhcpServer2RuleHwAddrType_Object((1,3,6,1,4,1,11,2,14,11,15,2,122,2,17,1,4),_HpnicfDhcpServer2RuleHwAddrType_Type())
hpnicfDhcpServer2RuleHwAddrType.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDhcpServer2RuleHwAddrType.setStatus(_A)
_HpnicfDhcpServer2RuleHwAddrStatus_Type=RowStatus
_HpnicfDhcpServer2RuleHwAddrStatus_Object=MibTableColumn
hpnicfDhcpServer2RuleHwAddrStatus=_HpnicfDhcpServer2RuleHwAddrStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,122,2,17,1,5),_HpnicfDhcpServer2RuleHwAddrStatus_Type())
hpnicfDhcpServer2RuleHwAddrStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDhcpServer2RuleHwAddrStatus.setStatus(_A)
_HpnicfDhcpServer2OptionGroupTable_Object=MibTable
hpnicfDhcpServer2OptionGroupTable=_HpnicfDhcpServer2OptionGroupTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,122,2,18))
if mibBuilder.loadTexts:hpnicfDhcpServer2OptionGroupTable.setStatus(_A)
_HpnicfDhcpServer2OptionGroupEntry_Object=MibTableRow
hpnicfDhcpServer2OptionGroupEntry=_HpnicfDhcpServer2OptionGroupEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,122,2,18,1))
hpnicfDhcpServer2OptionGroupEntry.setIndexNames((0,_E,_Q))
if mibBuilder.loadTexts:hpnicfDhcpServer2OptionGroupEntry.setStatus(_A)
class _HpnicfDhcpServer2OptionGroupId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32768))
_HpnicfDhcpServer2OptionGroupId_Type.__name__=_F
_HpnicfDhcpServer2OptionGroupId_Object=MibTableColumn
hpnicfDhcpServer2OptionGroupId=_HpnicfDhcpServer2OptionGroupId_Object((1,3,6,1,4,1,11,2,14,11,15,2,122,2,18,1,1),_HpnicfDhcpServer2OptionGroupId_Type())
hpnicfDhcpServer2OptionGroupId.setMaxAccess(_H)
if mibBuilder.loadTexts:hpnicfDhcpServer2OptionGroupId.setStatus(_A)
_HpnicfDhcpServer2OptionGroupStatus_Type=RowStatus
_HpnicfDhcpServer2OptionGroupStatus_Object=MibTableColumn
hpnicfDhcpServer2OptionGroupStatus=_HpnicfDhcpServer2OptionGroupStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,122,2,18,1,2),_HpnicfDhcpServer2OptionGroupStatus_Type())
hpnicfDhcpServer2OptionGroupStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDhcpServer2OptionGroupStatus.setStatus(_A)
_HpnicfDhcpServer2OptionTable_Object=MibTable
hpnicfDhcpServer2OptionTable=_HpnicfDhcpServer2OptionTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,122,2,19))
if mibBuilder.loadTexts:hpnicfDhcpServer2OptionTable.setStatus(_A)
_HpnicfDhcpServer2OptionEntry_Object=MibTableRow
hpnicfDhcpServer2OptionEntry=_HpnicfDhcpServer2OptionEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,122,2,19,1))
hpnicfDhcpServer2OptionEntry.setIndexNames((0,_E,_Q),(0,_E,_m))
if mibBuilder.loadTexts:hpnicfDhcpServer2OptionEntry.setStatus(_A)
class _HpnicfDhcpServer2OptionCode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,254))
_HpnicfDhcpServer2OptionCode_Type.__name__=_F
_HpnicfDhcpServer2OptionCode_Object=MibTableColumn
hpnicfDhcpServer2OptionCode=_HpnicfDhcpServer2OptionCode_Object((1,3,6,1,4,1,11,2,14,11,15,2,122,2,19,1,1),_HpnicfDhcpServer2OptionCode_Type())
hpnicfDhcpServer2OptionCode.setMaxAccess(_H)
if mibBuilder.loadTexts:hpnicfDhcpServer2OptionCode.setStatus(_A)
class _HpnicfDhcpServer2OptionType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_N,1),(_O,2),('ip',3)))
_HpnicfDhcpServer2OptionType_Type.__name__=_F
_HpnicfDhcpServer2OptionType_Object=MibTableColumn
hpnicfDhcpServer2OptionType=_HpnicfDhcpServer2OptionType_Object((1,3,6,1,4,1,11,2,14,11,15,2,122,2,19,1,2),_HpnicfDhcpServer2OptionType_Type())
hpnicfDhcpServer2OptionType.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDhcpServer2OptionType.setStatus(_A)
class _HpnicfDhcpServer2OptionAscii_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_HpnicfDhcpServer2OptionAscii_Type.__name__=_D
_HpnicfDhcpServer2OptionAscii_Object=MibTableColumn
hpnicfDhcpServer2OptionAscii=_HpnicfDhcpServer2OptionAscii_Object((1,3,6,1,4,1,11,2,14,11,15,2,122,2,19,1,3),_HpnicfDhcpServer2OptionAscii_Type())
hpnicfDhcpServer2OptionAscii.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDhcpServer2OptionAscii.setStatus(_A)
class _HpnicfDhcpServer2OptionHexStr_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,510))
_HpnicfDhcpServer2OptionHexStr_Type.__name__=_D
_HpnicfDhcpServer2OptionHexStr_Object=MibTableColumn
hpnicfDhcpServer2OptionHexStr=_HpnicfDhcpServer2OptionHexStr_Object((1,3,6,1,4,1,11,2,14,11,15,2,122,2,19,1,4),_HpnicfDhcpServer2OptionHexStr_Type())
hpnicfDhcpServer2OptionHexStr.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDhcpServer2OptionHexStr.setStatus(_A)
class _HpnicfDhcpServer2OptionIPStr_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_HpnicfDhcpServer2OptionIPStr_Type.__name__=_D
_HpnicfDhcpServer2OptionIPStr_Object=MibTableColumn
hpnicfDhcpServer2OptionIPStr=_HpnicfDhcpServer2OptionIPStr_Object((1,3,6,1,4,1,11,2,14,11,15,2,122,2,19,1,5),_HpnicfDhcpServer2OptionIPStr_Type())
hpnicfDhcpServer2OptionIPStr.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDhcpServer2OptionIPStr.setStatus(_A)
_HpnicfDhcpServer2OptionRowStatus_Type=RowStatus
_HpnicfDhcpServer2OptionRowStatus_Object=MibTableColumn
hpnicfDhcpServer2OptionRowStatus=_HpnicfDhcpServer2OptionRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,122,2,19,1,6),_HpnicfDhcpServer2OptionRowStatus_Type())
hpnicfDhcpServer2OptionRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDhcpServer2OptionRowStatus.setStatus(_A)
_HpnicfDhcpRelay2ScalarObjects_ObjectIdentity=ObjectIdentity
hpnicfDhcpRelay2ScalarObjects=_HpnicfDhcpRelay2ScalarObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,122,3))
_HpnicfDhcpRelay2ConfigGroup_ObjectIdentity=ObjectIdentity
hpnicfDhcpRelay2ConfigGroup=_HpnicfDhcpRelay2ConfigGroup_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,122,3,1))
class _HpnicfDhcpRelay2UserInfoRecord_Type(TruthValue):defaultValue=2
_HpnicfDhcpRelay2UserInfoRecord_Type.__name__=_I
_HpnicfDhcpRelay2UserInfoRecord_Object=MibScalar
hpnicfDhcpRelay2UserInfoRecord=_HpnicfDhcpRelay2UserInfoRecord_Object((1,3,6,1,4,1,11,2,14,11,15,2,122,3,1,1),_HpnicfDhcpRelay2UserInfoRecord_Type())
hpnicfDhcpRelay2UserInfoRecord.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfDhcpRelay2UserInfoRecord.setStatus(_A)
class _HpnicfDhcpRelay2UserInfoRefresh_Type(TruthValue):defaultValue=1
_HpnicfDhcpRelay2UserInfoRefresh_Type.__name__=_I
_HpnicfDhcpRelay2UserInfoRefresh_Object=MibScalar
hpnicfDhcpRelay2UserInfoRefresh=_HpnicfDhcpRelay2UserInfoRefresh_Object((1,3,6,1,4,1,11,2,14,11,15,2,122,3,1,2),_HpnicfDhcpRelay2UserInfoRefresh_Type())
hpnicfDhcpRelay2UserInfoRefresh.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfDhcpRelay2UserInfoRefresh.setStatus(_A)
class _HpnicfDhcpRelay2UserInfoFlushTime_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,120))
_HpnicfDhcpRelay2UserInfoFlushTime_Type.__name__=_K
_HpnicfDhcpRelay2UserInfoFlushTime_Object=MibScalar
hpnicfDhcpRelay2UserInfoFlushTime=_HpnicfDhcpRelay2UserInfoFlushTime_Object((1,3,6,1,4,1,11,2,14,11,15,2,122,3,1,3),_HpnicfDhcpRelay2UserInfoFlushTime_Type())
hpnicfDhcpRelay2UserInfoFlushTime.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfDhcpRelay2UserInfoFlushTime.setStatus(_A)
class _HpnicfDhcpRelay2ReleaseAddr_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,47))
_HpnicfDhcpRelay2ReleaseAddr_Type.__name__=_D
_HpnicfDhcpRelay2ReleaseAddr_Object=MibScalar
hpnicfDhcpRelay2ReleaseAddr=_HpnicfDhcpRelay2ReleaseAddr_Object((1,3,6,1,4,1,11,2,14,11,15,2,122,3,1,4),_HpnicfDhcpRelay2ReleaseAddr_Type())
hpnicfDhcpRelay2ReleaseAddr.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfDhcpRelay2ReleaseAddr.setStatus(_A)
_HpnicfDhcpRelay2StatisticsGroup_ObjectIdentity=ObjectIdentity
hpnicfDhcpRelay2StatisticsGroup=_HpnicfDhcpRelay2StatisticsGroup_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,122,3,2))
_HpnicfDhcpRelay2RxClientNum_Type=Counter64
_HpnicfDhcpRelay2RxClientNum_Object=MibScalar
hpnicfDhcpRelay2RxClientNum=_HpnicfDhcpRelay2RxClientNum_Object((1,3,6,1,4,1,11,2,14,11,15,2,122,3,2,1),_HpnicfDhcpRelay2RxClientNum_Type())
hpnicfDhcpRelay2RxClientNum.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDhcpRelay2RxClientNum.setStatus(_A)
_HpnicfDhcpRelay2TxClientNum_Type=Counter64
_HpnicfDhcpRelay2TxClientNum_Object=MibScalar
hpnicfDhcpRelay2TxClientNum=_HpnicfDhcpRelay2TxClientNum_Object((1,3,6,1,4,1,11,2,14,11,15,2,122,3,2,2),_HpnicfDhcpRelay2TxClientNum_Type())
hpnicfDhcpRelay2TxClientNum.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDhcpRelay2TxClientNum.setStatus(_A)
_HpnicfDhcpRelay2RxServerNum_Type=Counter64
_HpnicfDhcpRelay2RxServerNum_Object=MibScalar
hpnicfDhcpRelay2RxServerNum=_HpnicfDhcpRelay2RxServerNum_Object((1,3,6,1,4,1,11,2,14,11,15,2,122,3,2,3),_HpnicfDhcpRelay2RxServerNum_Type())
hpnicfDhcpRelay2RxServerNum.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDhcpRelay2RxServerNum.setStatus(_A)
_HpnicfDhcpRelay2TxServerNum_Type=Counter64
_HpnicfDhcpRelay2TxServerNum_Object=MibScalar
hpnicfDhcpRelay2TxServerNum=_HpnicfDhcpRelay2TxServerNum_Object((1,3,6,1,4,1,11,2,14,11,15,2,122,3,2,4),_HpnicfDhcpRelay2TxServerNum_Type())
hpnicfDhcpRelay2TxServerNum.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDhcpRelay2TxServerNum.setStatus(_A)
_HpnicfDhcpRelay2BadNum_Type=Counter64
_HpnicfDhcpRelay2BadNum_Object=MibScalar
hpnicfDhcpRelay2BadNum=_HpnicfDhcpRelay2BadNum_Object((1,3,6,1,4,1,11,2,14,11,15,2,122,3,2,5),_HpnicfDhcpRelay2BadNum_Type())
hpnicfDhcpRelay2BadNum.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDhcpRelay2BadNum.setStatus(_A)
_HpnicfDhcpRelay2BootpRequestNum_Type=Counter64
_HpnicfDhcpRelay2BootpRequestNum_Object=MibScalar
hpnicfDhcpRelay2BootpRequestNum=_HpnicfDhcpRelay2BootpRequestNum_Object((1,3,6,1,4,1,11,2,14,11,15,2,122,3,2,6),_HpnicfDhcpRelay2BootpRequestNum_Type())
hpnicfDhcpRelay2BootpRequestNum.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDhcpRelay2BootpRequestNum.setStatus(_A)
_HpnicfDhcpRelay2DiscoverNum_Type=Counter64
_HpnicfDhcpRelay2DiscoverNum_Object=MibScalar
hpnicfDhcpRelay2DiscoverNum=_HpnicfDhcpRelay2DiscoverNum_Object((1,3,6,1,4,1,11,2,14,11,15,2,122,3,2,7),_HpnicfDhcpRelay2DiscoverNum_Type())
hpnicfDhcpRelay2DiscoverNum.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDhcpRelay2DiscoverNum.setStatus(_A)
_HpnicfDhcpRelay2RequestNum_Type=Counter64
_HpnicfDhcpRelay2RequestNum_Object=MibScalar
hpnicfDhcpRelay2RequestNum=_HpnicfDhcpRelay2RequestNum_Object((1,3,6,1,4,1,11,2,14,11,15,2,122,3,2,8),_HpnicfDhcpRelay2RequestNum_Type())
hpnicfDhcpRelay2RequestNum.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDhcpRelay2RequestNum.setStatus(_A)
_HpnicfDhcpRelay2DeclineNum_Type=Counter64
_HpnicfDhcpRelay2DeclineNum_Object=MibScalar
hpnicfDhcpRelay2DeclineNum=_HpnicfDhcpRelay2DeclineNum_Object((1,3,6,1,4,1,11,2,14,11,15,2,122,3,2,9),_HpnicfDhcpRelay2DeclineNum_Type())
hpnicfDhcpRelay2DeclineNum.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDhcpRelay2DeclineNum.setStatus(_A)
_HpnicfDhcpRelay2ReleaseNum_Type=Counter64
_HpnicfDhcpRelay2ReleaseNum_Object=MibScalar
hpnicfDhcpRelay2ReleaseNum=_HpnicfDhcpRelay2ReleaseNum_Object((1,3,6,1,4,1,11,2,14,11,15,2,122,3,2,10),_HpnicfDhcpRelay2ReleaseNum_Type())
hpnicfDhcpRelay2ReleaseNum.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDhcpRelay2ReleaseNum.setStatus(_A)
_HpnicfDhcpRelay2InformNum_Type=Counter64
_HpnicfDhcpRelay2InformNum_Object=MibScalar
hpnicfDhcpRelay2InformNum=_HpnicfDhcpRelay2InformNum_Object((1,3,6,1,4,1,11,2,14,11,15,2,122,3,2,11),_HpnicfDhcpRelay2InformNum_Type())
hpnicfDhcpRelay2InformNum.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDhcpRelay2InformNum.setStatus(_A)
_HpnicfDhcpRelay2BootpReplyNum_Type=Counter64
_HpnicfDhcpRelay2BootpReplyNum_Object=MibScalar
hpnicfDhcpRelay2BootpReplyNum=_HpnicfDhcpRelay2BootpReplyNum_Object((1,3,6,1,4,1,11,2,14,11,15,2,122,3,2,12),_HpnicfDhcpRelay2BootpReplyNum_Type())
hpnicfDhcpRelay2BootpReplyNum.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDhcpRelay2BootpReplyNum.setStatus(_A)
_HpnicfDhcpRelay2OfferNum_Type=Counter64
_HpnicfDhcpRelay2OfferNum_Object=MibScalar
hpnicfDhcpRelay2OfferNum=_HpnicfDhcpRelay2OfferNum_Object((1,3,6,1,4,1,11,2,14,11,15,2,122,3,2,13),_HpnicfDhcpRelay2OfferNum_Type())
hpnicfDhcpRelay2OfferNum.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDhcpRelay2OfferNum.setStatus(_A)
_HpnicfDhcpRelay2AckNum_Type=Counter64
_HpnicfDhcpRelay2AckNum_Object=MibScalar
hpnicfDhcpRelay2AckNum=_HpnicfDhcpRelay2AckNum_Object((1,3,6,1,4,1,11,2,14,11,15,2,122,3,2,14),_HpnicfDhcpRelay2AckNum_Type())
hpnicfDhcpRelay2AckNum.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDhcpRelay2AckNum.setStatus(_A)
_HpnicfDhcpRelay2NakNum_Type=Counter64
_HpnicfDhcpRelay2NakNum_Object=MibScalar
hpnicfDhcpRelay2NakNum=_HpnicfDhcpRelay2NakNum_Object((1,3,6,1,4,1,11,2,14,11,15,2,122,3,2,15),_HpnicfDhcpRelay2NakNum_Type())
hpnicfDhcpRelay2NakNum.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDhcpRelay2NakNum.setStatus(_A)
_HpnicfDhcpRelay2Tables_ObjectIdentity=ObjectIdentity
hpnicfDhcpRelay2Tables=_HpnicfDhcpRelay2Tables_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,122,4))
_HpnicfDhcpRelay2IfConfigTable_Object=MibTable
hpnicfDhcpRelay2IfConfigTable=_HpnicfDhcpRelay2IfConfigTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,122,4,1))
if mibBuilder.loadTexts:hpnicfDhcpRelay2IfConfigTable.setStatus(_A)
_HpnicfDhcpRelay2IfConfigEntry_Object=MibTableRow
hpnicfDhcpRelay2IfConfigEntry=_HpnicfDhcpRelay2IfConfigEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,122,4,1,1))
hpnicfDhcpRelay2IfConfigEntry.setIndexNames((0,_L,_M))
if mibBuilder.loadTexts:hpnicfDhcpRelay2IfConfigEntry.setStatus(_A)
class _HpnicfDhcpRelay2IfSelectRelay_Type(TruthValue):defaultValue=2
_HpnicfDhcpRelay2IfSelectRelay_Type.__name__=_I
_HpnicfDhcpRelay2IfSelectRelay_Object=MibTableColumn
hpnicfDhcpRelay2IfSelectRelay=_HpnicfDhcpRelay2IfSelectRelay_Object((1,3,6,1,4,1,11,2,14,11,15,2,122,4,1,1,1),_HpnicfDhcpRelay2IfSelectRelay_Type())
hpnicfDhcpRelay2IfSelectRelay.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfDhcpRelay2IfSelectRelay.setStatus(_A)
class _HpnicfDhcpRelay2IfCheckMac_Type(TruthValue):defaultValue=2
_HpnicfDhcpRelay2IfCheckMac_Type.__name__=_I
_HpnicfDhcpRelay2IfCheckMac_Object=MibTableColumn
hpnicfDhcpRelay2IfCheckMac=_HpnicfDhcpRelay2IfCheckMac_Object((1,3,6,1,4,1,11,2,14,11,15,2,122,4,1,1,2),_HpnicfDhcpRelay2IfCheckMac_Type())
hpnicfDhcpRelay2IfCheckMac.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfDhcpRelay2IfCheckMac.setStatus(_A)
class _HpnicfDhcpRelay2IfOpt82Enable_Type(TruthValue):defaultValue=2
_HpnicfDhcpRelay2IfOpt82Enable_Type.__name__=_I
_HpnicfDhcpRelay2IfOpt82Enable_Object=MibTableColumn
hpnicfDhcpRelay2IfOpt82Enable=_HpnicfDhcpRelay2IfOpt82Enable_Object((1,3,6,1,4,1,11,2,14,11,15,2,122,4,1,1,3),_HpnicfDhcpRelay2IfOpt82Enable_Type())
hpnicfDhcpRelay2IfOpt82Enable.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfDhcpRelay2IfOpt82Enable.setStatus(_A)
class _HpnicfDhcpRelay2IfOpt82Strategy_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('drop',1),('keep',2),('replace',3)))
_HpnicfDhcpRelay2IfOpt82Strategy_Type.__name__=_F
_HpnicfDhcpRelay2IfOpt82Strategy_Object=MibTableColumn
hpnicfDhcpRelay2IfOpt82Strategy=_HpnicfDhcpRelay2IfOpt82Strategy_Object((1,3,6,1,4,1,11,2,14,11,15,2,122,4,1,1,4),_HpnicfDhcpRelay2IfOpt82Strategy_Type())
hpnicfDhcpRelay2IfOpt82Strategy.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfDhcpRelay2IfOpt82Strategy.setStatus(_A)
class _HpnicfDhcpRelay2IfOpt82CIDMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_n,1),('verbose',2),(_R,3)))
_HpnicfDhcpRelay2IfOpt82CIDMode_Type.__name__=_F
_HpnicfDhcpRelay2IfOpt82CIDMode_Object=MibTableColumn
hpnicfDhcpRelay2IfOpt82CIDMode=_HpnicfDhcpRelay2IfOpt82CIDMode_Object((1,3,6,1,4,1,11,2,14,11,15,2,122,4,1,1,5),_HpnicfDhcpRelay2IfOpt82CIDMode_Type())
hpnicfDhcpRelay2IfOpt82CIDMode.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfDhcpRelay2IfOpt82CIDMode.setStatus(_A)
class _HpnicfDhcpRelay2IfOpt82CIDNodeType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('invalid',1),('mac',2),(_o,3),(_R,4)))
_HpnicfDhcpRelay2IfOpt82CIDNodeType_Type.__name__=_F
_HpnicfDhcpRelay2IfOpt82CIDNodeType_Object=MibTableColumn
hpnicfDhcpRelay2IfOpt82CIDNodeType=_HpnicfDhcpRelay2IfOpt82CIDNodeType_Object((1,3,6,1,4,1,11,2,14,11,15,2,122,4,1,1,6),_HpnicfDhcpRelay2IfOpt82CIDNodeType_Type())
hpnicfDhcpRelay2IfOpt82CIDNodeType.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfDhcpRelay2IfOpt82CIDNodeType.setStatus(_A)
class _HpnicfDhcpRelay2IfOpt82CIDNodeStr_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,50))
_HpnicfDhcpRelay2IfOpt82CIDNodeStr_Type.__name__=_D
_HpnicfDhcpRelay2IfOpt82CIDNodeStr_Object=MibTableColumn
hpnicfDhcpRelay2IfOpt82CIDNodeStr=_HpnicfDhcpRelay2IfOpt82CIDNodeStr_Object((1,3,6,1,4,1,11,2,14,11,15,2,122,4,1,1,7),_HpnicfDhcpRelay2IfOpt82CIDNodeStr_Type())
hpnicfDhcpRelay2IfOpt82CIDNodeStr.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfDhcpRelay2IfOpt82CIDNodeStr.setStatus(_A)
class _HpnicfDhcpRelay2IfOpt82CIDStr_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,0),ValueSizeConstraint(3,63))
_HpnicfDhcpRelay2IfOpt82CIDStr_Type.__name__=_D
_HpnicfDhcpRelay2IfOpt82CIDStr_Object=MibTableColumn
hpnicfDhcpRelay2IfOpt82CIDStr=_HpnicfDhcpRelay2IfOpt82CIDStr_Object((1,3,6,1,4,1,11,2,14,11,15,2,122,4,1,1,8),_HpnicfDhcpRelay2IfOpt82CIDStr_Type())
hpnicfDhcpRelay2IfOpt82CIDStr.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfDhcpRelay2IfOpt82CIDStr.setStatus(_A)
class _HpnicfDhcpRelay2IfOpt82CIDFormat_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_O,1),(_N,2),('undefine',3)))
_HpnicfDhcpRelay2IfOpt82CIDFormat_Type.__name__=_F
_HpnicfDhcpRelay2IfOpt82CIDFormat_Object=MibTableColumn
hpnicfDhcpRelay2IfOpt82CIDFormat=_HpnicfDhcpRelay2IfOpt82CIDFormat_Object((1,3,6,1,4,1,11,2,14,11,15,2,122,4,1,1,9),_HpnicfDhcpRelay2IfOpt82CIDFormat_Type())
hpnicfDhcpRelay2IfOpt82CIDFormat.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfDhcpRelay2IfOpt82CIDFormat.setStatus(_A)
class _HpnicfDhcpRelay2IfOpt82RIDMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_n,1),(_o,2),(_R,3)))
_HpnicfDhcpRelay2IfOpt82RIDMode_Type.__name__=_F
_HpnicfDhcpRelay2IfOpt82RIDMode_Object=MibTableColumn
hpnicfDhcpRelay2IfOpt82RIDMode=_HpnicfDhcpRelay2IfOpt82RIDMode_Object((1,3,6,1,4,1,11,2,14,11,15,2,122,4,1,1,10),_HpnicfDhcpRelay2IfOpt82RIDMode_Type())
hpnicfDhcpRelay2IfOpt82RIDMode.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfDhcpRelay2IfOpt82RIDMode.setStatus(_A)
class _HpnicfDhcpRelay2IfOpt82RIDStr_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_HpnicfDhcpRelay2IfOpt82RIDStr_Type.__name__=_D
_HpnicfDhcpRelay2IfOpt82RIDStr_Object=MibTableColumn
hpnicfDhcpRelay2IfOpt82RIDStr=_HpnicfDhcpRelay2IfOpt82RIDStr_Object((1,3,6,1,4,1,11,2,14,11,15,2,122,4,1,1,11),_HpnicfDhcpRelay2IfOpt82RIDStr_Type())
hpnicfDhcpRelay2IfOpt82RIDStr.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfDhcpRelay2IfOpt82RIDStr.setStatus(_A)
class _HpnicfDhcpRelay2IfOpt82RIDFormat_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_O,1),(_N,2)))
_HpnicfDhcpRelay2IfOpt82RIDFormat_Type.__name__=_F
_HpnicfDhcpRelay2IfOpt82RIDFormat_Object=MibTableColumn
hpnicfDhcpRelay2IfOpt82RIDFormat=_HpnicfDhcpRelay2IfOpt82RIDFormat_Object((1,3,6,1,4,1,11,2,14,11,15,2,122,4,1,1,12),_HpnicfDhcpRelay2IfOpt82RIDFormat_Type())
hpnicfDhcpRelay2IfOpt82RIDFormat.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfDhcpRelay2IfOpt82RIDFormat.setStatus(_A)
_HpnicfDhcpRelay2SrvAddrTable_Object=MibTable
hpnicfDhcpRelay2SrvAddrTable=_HpnicfDhcpRelay2SrvAddrTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,122,4,2))
if mibBuilder.loadTexts:hpnicfDhcpRelay2SrvAddrTable.setStatus(_A)
_HpnicfDhcpRelay2SrvAddrEntry_Object=MibTableRow
hpnicfDhcpRelay2SrvAddrEntry=_HpnicfDhcpRelay2SrvAddrEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,122,4,2,1))
hpnicfDhcpRelay2SrvAddrEntry.setIndexNames((0,_L,_M),(0,_E,_p))
if mibBuilder.loadTexts:hpnicfDhcpRelay2SrvAddrEntry.setStatus(_A)
_HpnicfDhcpRelay2SrvAddrIP_Type=InetAddressIPv4
_HpnicfDhcpRelay2SrvAddrIP_Object=MibTableColumn
hpnicfDhcpRelay2SrvAddrIP=_HpnicfDhcpRelay2SrvAddrIP_Object((1,3,6,1,4,1,11,2,14,11,15,2,122,4,2,1,1),_HpnicfDhcpRelay2SrvAddrIP_Type())
hpnicfDhcpRelay2SrvAddrIP.setMaxAccess(_H)
if mibBuilder.loadTexts:hpnicfDhcpRelay2SrvAddrIP.setStatus(_A)
_HpnicfDhcpRelay2SrvAddrRowStatus_Type=RowStatus
_HpnicfDhcpRelay2SrvAddrRowStatus_Object=MibTableColumn
hpnicfDhcpRelay2SrvAddrRowStatus=_HpnicfDhcpRelay2SrvAddrRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,122,4,2,1,2),_HpnicfDhcpRelay2SrvAddrRowStatus_Type())
hpnicfDhcpRelay2SrvAddrRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDhcpRelay2SrvAddrRowStatus.setStatus(_A)
_HpnicfDhcpRelay2UserInfoTable_Object=MibTable
hpnicfDhcpRelay2UserInfoTable=_HpnicfDhcpRelay2UserInfoTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,122,4,3))
if mibBuilder.loadTexts:hpnicfDhcpRelay2UserInfoTable.setStatus(_A)
_HpnicfDhcpRelay2UserInfoEntry_Object=MibTableRow
hpnicfDhcpRelay2UserInfoEntry=_HpnicfDhcpRelay2UserInfoEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,122,4,3,1))
hpnicfDhcpRelay2UserInfoEntry.setIndexNames((0,_E,_q),(0,_E,_r))
if mibBuilder.loadTexts:hpnicfDhcpRelay2UserInfoEntry.setStatus(_A)
class _HpnicfDhcpRelay2UserInfoVpnIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65534))
_HpnicfDhcpRelay2UserInfoVpnIndex_Type.__name__=_K
_HpnicfDhcpRelay2UserInfoVpnIndex_Object=MibTableColumn
hpnicfDhcpRelay2UserInfoVpnIndex=_HpnicfDhcpRelay2UserInfoVpnIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,122,4,3,1,1),_HpnicfDhcpRelay2UserInfoVpnIndex_Type())
hpnicfDhcpRelay2UserInfoVpnIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:hpnicfDhcpRelay2UserInfoVpnIndex.setStatus(_A)
_HpnicfDhcpRelay2UserInfoIpAddr_Type=InetAddressIPv4
_HpnicfDhcpRelay2UserInfoIpAddr_Object=MibTableColumn
hpnicfDhcpRelay2UserInfoIpAddr=_HpnicfDhcpRelay2UserInfoIpAddr_Object((1,3,6,1,4,1,11,2,14,11,15,2,122,4,3,1,2),_HpnicfDhcpRelay2UserInfoIpAddr_Type())
hpnicfDhcpRelay2UserInfoIpAddr.setMaxAccess(_H)
if mibBuilder.loadTexts:hpnicfDhcpRelay2UserInfoIpAddr.setStatus(_A)
_HpnicfDhcpRelay2UserInfoMacAddr_Type=MacAddress
_HpnicfDhcpRelay2UserInfoMacAddr_Object=MibTableColumn
hpnicfDhcpRelay2UserInfoMacAddr=_HpnicfDhcpRelay2UserInfoMacAddr_Object((1,3,6,1,4,1,11,2,14,11,15,2,122,4,3,1,3),_HpnicfDhcpRelay2UserInfoMacAddr_Type())
hpnicfDhcpRelay2UserInfoMacAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDhcpRelay2UserInfoMacAddr.setStatus(_A)
_HpnicfDhcpRelay2UserInfoIfIndex_Type=InterfaceIndexOrZero
_HpnicfDhcpRelay2UserInfoIfIndex_Object=MibTableColumn
hpnicfDhcpRelay2UserInfoIfIndex=_HpnicfDhcpRelay2UserInfoIfIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,122,4,3,1,4),_HpnicfDhcpRelay2UserInfoIfIndex_Type())
hpnicfDhcpRelay2UserInfoIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfDhcpRelay2UserInfoIfIndex.setStatus(_A)
_HpnicfDhcpRelay2UserInfoRowStatus_Type=RowStatus
_HpnicfDhcpRelay2UserInfoRowStatus_Object=MibTableColumn
hpnicfDhcpRelay2UserInfoRowStatus=_HpnicfDhcpRelay2UserInfoRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,122,4,3,1,5),_HpnicfDhcpRelay2UserInfoRowStatus_Type())
hpnicfDhcpRelay2UserInfoRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDhcpRelay2UserInfoRowStatus.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'hpnicfDhcp4':hpnicfDhcp4,'hpnicfDhcpServer2ScalarObjects':hpnicfDhcpServer2ScalarObjects,'hpnicfDhcpServer2ConfigGroup':hpnicfDhcpServer2ConfigGroup,'hpnicfDhcpServer2Enabled':hpnicfDhcpServer2Enabled,'hpnicfDhcpServer2AlwaysBroadcast':hpnicfDhcpServer2AlwaysBroadcast,'hpnicfDhcpServer2IgnoreBootp':hpnicfDhcpServer2IgnoreBootp,'hpnicfDhcpServer2BootpReplyRfc1048':hpnicfDhcpServer2BootpReplyRfc1048,'hpnicfDhcpServer2Opt82Enabled':hpnicfDhcpServer2Opt82Enabled,'hpnicfDhcpServer2PingNumber':hpnicfDhcpServer2PingNumber,'hpnicfDhcpServer2PingTimeout':hpnicfDhcpServer2PingTimeout,'hpnicfDhcpServer2StatGroup':hpnicfDhcpServer2StatGroup,'hpnicfDhcpServer2BadNum':hpnicfDhcpServer2BadNum,'hpnicfDhcpServer2BootpRequestNum':hpnicfDhcpServer2BootpRequestNum,'hpnicfDhcpServer2DiscoverNum':hpnicfDhcpServer2DiscoverNum,'hpnicfDhcpServer2RequestNum':hpnicfDhcpServer2RequestNum,'hpnicfDhcpServer2DeclineNum':hpnicfDhcpServer2DeclineNum,'hpnicfDhcpServer2ReleaseNum':hpnicfDhcpServer2ReleaseNum,'hpnicfDhcpServer2InformNum':hpnicfDhcpServer2InformNum,'hpnicfDhcpServer2BootpReplyNum':hpnicfDhcpServer2BootpReplyNum,'hpnicfDhcpServer2OfferNum':hpnicfDhcpServer2OfferNum,'hpnicfDhcpServer2AckNum':hpnicfDhcpServer2AckNum,'hpnicfDhcpServer2NakNum':hpnicfDhcpServer2NakNum,'hpnicfDhcpServer2TotalPoolUsage':hpnicfDhcpServer2TotalPoolUsage,'hpnicfDhcpServer2PoolNumber':hpnicfDhcpServer2PoolNumber,'hpnicfDhcpServer2ConflictNum':hpnicfDhcpServer2ConflictNum,'hpnicfDhcpServer2AutoBindNum':hpnicfDhcpServer2AutoBindNum,'hpnicfDhcpServer2ManualBindNum':hpnicfDhcpServer2ManualBindNum,'hpnicfDhcpServer2ExpiredBindNum':hpnicfDhcpServer2ExpiredBindNum,'hpnicfDhcpServer2Tables':hpnicfDhcpServer2Tables,'hpnicfDhcpServer2PoolTable':hpnicfDhcpServer2PoolTable,'hpnicfDhcpServer2PoolEntry':hpnicfDhcpServer2PoolEntry,_J:hpnicfDhcpServer2PoolIndex,'hpnicfDhcpServer2PoolName':hpnicfDhcpServer2PoolName,'hpnicfDhcpServer2PoolVpnName':hpnicfDhcpServer2PoolVpnName,'hpnicfDhcpServer2PoolNetwork':hpnicfDhcpServer2PoolNetwork,'hpnicfDhcpServer2PoolNetworkMask':hpnicfDhcpServer2PoolNetworkMask,'hpnicfDhcpServer2PoolStartAddr':hpnicfDhcpServer2PoolStartAddr,'hpnicfDhcpServer2PoolEndAddr':hpnicfDhcpServer2PoolEndAddr,'hpnicfDhcpServer2PoolLeaseDay':hpnicfDhcpServer2PoolLeaseDay,'hpnicfDhcpServer2PoolLeaseHour':hpnicfDhcpServer2PoolLeaseHour,'hpnicfDhcpServer2PoolLeaseMinute':hpnicfDhcpServer2PoolLeaseMinute,'hpnicfDhcpServer2PoolLeaseSecond':hpnicfDhcpServer2PoolLeaseSecond,'hpnicfDhcpServer2PoolLeaseUnlimit':hpnicfDhcpServer2PoolLeaseUnlimit,'hpnicfDhcpServer2PoolLeaseTime':hpnicfDhcpServer2PoolLeaseTime,'hpnicfDhcpServer2PoolDomainName':hpnicfDhcpServer2PoolDomainName,'hpnicfDhcpServer2PoolGatewayIP':hpnicfDhcpServer2PoolGatewayIP,'hpnicfDhcpServer2PoolDNSIP':hpnicfDhcpServer2PoolDNSIP,'hpnicfDhcpServer2PoolPrimaryDNSIP':hpnicfDhcpServer2PoolPrimaryDNSIP,'hpnicfDhcpServer2PoolSecondDNSIP':hpnicfDhcpServer2PoolSecondDNSIP,'hpnicfDhcpServer2PoolNetbiosType':hpnicfDhcpServer2PoolNetbiosType,'hpnicfDhcpServer2PoolNbnsIP':hpnicfDhcpServer2PoolNbnsIP,'hpnicfDhcpServer2PoolBootFileName':hpnicfDhcpServer2PoolBootFileName,'hpnicfDhcpServer2PoolBimsIP':hpnicfDhcpServer2PoolBimsIP,'hpnicfDhcpServer2PoolBimsPort':hpnicfDhcpServer2PoolBimsPort,'hpnicfDhcpServer2PoolBimsKeyStr':hpnicfDhcpServer2PoolBimsKeyStr,'hpnicfDhcpServer2PoolNextServer':hpnicfDhcpServer2PoolNextServer,'hpnicfDhcpServer2PoolTftpDomName':hpnicfDhcpServer2PoolTftpDomName,'hpnicfDhcpServer2PoolTftpIP':hpnicfDhcpServer2PoolTftpIP,'hpnicfDhcpServer2PoolVoiceAsIP':hpnicfDhcpServer2PoolVoiceAsIP,'hpnicfDhcpServer2PoolVoiceFailIP':hpnicfDhcpServer2PoolVoiceFailIP,'hpnicfDhcpServer2PoolVoiceFailStr':hpnicfDhcpServer2PoolVoiceFailStr,'hpnicfDhcpServer2PoolVoiceNCPIP':hpnicfDhcpServer2PoolVoiceNCPIP,'hpnicfDhcpServer2PoolVoiceVlanId':hpnicfDhcpServer2PoolVoiceVlanId,'hpnicfDhcpServer2PoolVoiceVlanEnbl':hpnicfDhcpServer2PoolVoiceVlanEnbl,'hpnicfDhcpServer2PoolRowStatus':hpnicfDhcpServer2PoolRowStatus,'hpnicfDhcpServer2PoolVerifyClass':hpnicfDhcpServer2PoolVerifyClass,'hpnicfDhcpServer2IfApplyPoolTable':hpnicfDhcpServer2IfApplyPoolTable,'hpnicfDhcpServer2IfApplyPoolEntry':hpnicfDhcpServer2IfApplyPoolEntry,'hpnicfDhcpServer2IfApplyPoolName':hpnicfDhcpServer2IfApplyPoolName,'hpnicfDhcpServer2PoolSecNwTable':hpnicfDhcpServer2PoolSecNwTable,'hpnicfDhcpServer2PoolSecNwEntry':hpnicfDhcpServer2PoolSecNwEntry,_S:hpnicfDhcpServer2PoolSecNw,_T:hpnicfDhcpServer2PoolSecNwMask,'hpnicfDhcpServer2PoolSecNwGwIP':hpnicfDhcpServer2PoolSecNwGwIP,'hpnicfDhcpServer2PoolSecNwStatus':hpnicfDhcpServer2PoolSecNwStatus,'hpnicfDhcpServer2PoolClassTable':hpnicfDhcpServer2PoolClassTable,'hpnicfDhcpServer2PoolClassEntry':hpnicfDhcpServer2PoolClassEntry,_U:hpnicfDhcpServer2PoolClassName,'hpnicfDhcpServer2PoolClassStart':hpnicfDhcpServer2PoolClassStart,'hpnicfDhcpServer2PoolClassEnd':hpnicfDhcpServer2PoolClassEnd,'hpnicfDhcpServer2PoolClassStatus':hpnicfDhcpServer2PoolClassStatus,'hpnicfDhcpServer2PoolStaticTable':hpnicfDhcpServer2PoolStaticTable,'hpnicfDhcpServer2PoolStaticEntry':hpnicfDhcpServer2PoolStaticEntry,_V:hpnicfDhcpServer2PoolStaticIP,'hpnicfDhcpServer2PoolStaticMask':hpnicfDhcpServer2PoolStaticMask,'hpnicfDhcpServer2PoolStaticCID':hpnicfDhcpServer2PoolStaticCID,'hpnicfDhcpServer2PoolStaticHAddr':hpnicfDhcpServer2PoolStaticHAddr,'hpnicfDhcpServer2PoolStaticHType':hpnicfDhcpServer2PoolStaticHType,'hpnicfDhcpServer2PoolStaticStatus':hpnicfDhcpServer2PoolStaticStatus,'hpnicfDhcpServer2PoolOptionTable':hpnicfDhcpServer2PoolOptionTable,'hpnicfDhcpServer2PoolOptionEntry':hpnicfDhcpServer2PoolOptionEntry,_Z:hpnicfDhcpServer2PoolOptCode,'hpnicfDhcpServer2PoolOptType':hpnicfDhcpServer2PoolOptType,'hpnicfDhcpServer2PoolOptAscii':hpnicfDhcpServer2PoolOptAscii,'hpnicfDhcpServer2PoolOptHexStr':hpnicfDhcpServer2PoolOptHexStr,'hpnicfDhcpServer2PoolOptIPStr':hpnicfDhcpServer2PoolOptIPStr,'hpnicfDhcpServer2PoolOptRowStatus':hpnicfDhcpServer2PoolOptRowStatus,'hpnicfDhcpServer2PoolForbidTable':hpnicfDhcpServer2PoolForbidTable,'hpnicfDhcpServer2PoolForbidEntry':hpnicfDhcpServer2PoolForbidEntry,_a:hpnicfDhcpServer2PoolForbidIP,'hpnicfDhcpServer2PoolForbidStatus':hpnicfDhcpServer2PoolForbidStatus,'hpnicfDhcpServer2ClassTable':hpnicfDhcpServer2ClassTable,'hpnicfDhcpServer2ClassEntry':hpnicfDhcpServer2ClassEntry,_P:hpnicfDhcpServer2ClassName,'hpnicfDhcpServer2ClassRowStatus':hpnicfDhcpServer2ClassRowStatus,'hpnicfDhcpServer2RuleTable':hpnicfDhcpServer2RuleTable,'hpnicfDhcpServer2RuleEntry':hpnicfDhcpServer2RuleEntry,_b:hpnicfDhcpServer2RuleNumber,'hpnicfDhcpServer2RuleOptCode':hpnicfDhcpServer2RuleOptCode,'hpnicfDhcpServer2RuleOptHexStr':hpnicfDhcpServer2RuleOptHexStr,'hpnicfDhcpServer2RuleOptMask':hpnicfDhcpServer2RuleOptMask,'hpnicfDhcpServer2RuleOptOffset':hpnicfDhcpServer2RuleOptOffset,'hpnicfDhcpServer2RuleOptLength':hpnicfDhcpServer2RuleOptLength,'hpnicfDhcpServer2RuleRowStatus':hpnicfDhcpServer2RuleRowStatus,'hpnicfDhcpServer2ForbidTable':hpnicfDhcpServer2ForbidTable,'hpnicfDhcpServer2ForbidEntry':hpnicfDhcpServer2ForbidEntry,_c:hpnicfDhcpServer2ForbidVpnName,_d:hpnicfDhcpServer2ForbidStart,_e:hpnicfDhcpServer2ForbidEnd,'hpnicfDhcpServer2ForbidRowStatus':hpnicfDhcpServer2ForbidRowStatus,'hpnicfDhcpServer2FreeTable':hpnicfDhcpServer2FreeTable,'hpnicfDhcpServer2FreeEntry':hpnicfDhcpServer2FreeEntry,_f:hpnicfDhcpServer2FreeStart,'hpnicfDhcpServer2FreeEnd':hpnicfDhcpServer2FreeEnd,'hpnicfDhcpServer2ConflictTable':hpnicfDhcpServer2ConflictTable,'hpnicfDhcpServer2ConflictEntry':hpnicfDhcpServer2ConflictEntry,_g:hpnicfDhcpServer2ConflictIP,'hpnicfDhcpServer2ConflictType':hpnicfDhcpServer2ConflictType,'hpnicfDhcpServer2ConflictTime':hpnicfDhcpServer2ConflictTime,'hpnicfDhcpServer2ConflictRowStatus':hpnicfDhcpServer2ConflictRowStatus,'hpnicfDhcpServer2ExpiredTable':hpnicfDhcpServer2ExpiredTable,'hpnicfDhcpServer2ExpiredEntry':hpnicfDhcpServer2ExpiredEntry,_h:hpnicfDhcpServer2ExpiredIP,'hpnicfDhcpServer2ExpiredClientId':hpnicfDhcpServer2ExpiredClientId,'hpnicfDhcpServer2ExpiredTime':hpnicfDhcpServer2ExpiredTime,'hpnicfDhcpServer2ExpiredRowStatus':hpnicfDhcpServer2ExpiredRowStatus,'hpnicfDhcpServer2IPInUseTable':hpnicfDhcpServer2IPInUseTable,'hpnicfDhcpServer2IPInUseEntry':hpnicfDhcpServer2IPInUseEntry,_i:hpnicfDhcpServer2IPInUseIP,'hpnicfDhcpServer2IPInUseClientId':hpnicfDhcpServer2IPInUseClientId,'hpnicfDhcpServer2IPInUseHardAddr':hpnicfDhcpServer2IPInUseHardAddr,'hpnicfDhcpServer2IPInUseHardType':hpnicfDhcpServer2IPInUseHardType,'hpnicfDhcpServer2IPInUseVlanId':hpnicfDhcpServer2IPInUseVlanId,'hpnicfDhcpServer2IPInUseEndLease':hpnicfDhcpServer2IPInUseEndLease,'hpnicfDhcpServer2IPInUseType':hpnicfDhcpServer2IPInUseType,'hpnicfDhcpServer2IPInUseIfIndex':hpnicfDhcpServer2IPInUseIfIndex,'hpnicfDhcpServer2IPInUseRowStatus':hpnicfDhcpServer2IPInUseRowStatus,'hpnicfDhcpServer2DefOptGrpTable':hpnicfDhcpServer2DefOptGrpTable,'hpnicfDhcpServer2DefOptGrpEntry':hpnicfDhcpServer2DefOptGrpEntry,_j:hpnicfDhcpServer2DefOptGrpClass,'hpnicfDhcpServer2DefOptGrpId':hpnicfDhcpServer2DefOptGrpId,'hpnicfDhcpServer2DefOptGrpStatus':hpnicfDhcpServer2DefOptGrpStatus,'hpnicfDhcpServer2ValidClassTable':hpnicfDhcpServer2ValidClassTable,'hpnicfDhcpServer2ValidClassEntry':hpnicfDhcpServer2ValidClassEntry,_k:hpnicfDhcpServer2ValidClassName,'hpnicfDhcpServer2ValidClassStatus':hpnicfDhcpServer2ValidClassStatus,'hpnicfDhcpServer2RuleHwAddrTable':hpnicfDhcpServer2RuleHwAddrTable,'hpnicfDhcpServer2RuleHwAddrEntry':hpnicfDhcpServer2RuleHwAddrEntry,_l:hpnicfDhcpServer2RuleHwAddrNumber,'hpnicfDhcpServer2RuleHwAddress':hpnicfDhcpServer2RuleHwAddress,'hpnicfDhcpServer2RuleHwAddrMask':hpnicfDhcpServer2RuleHwAddrMask,'hpnicfDhcpServer2RuleHwAddrType':hpnicfDhcpServer2RuleHwAddrType,'hpnicfDhcpServer2RuleHwAddrStatus':hpnicfDhcpServer2RuleHwAddrStatus,'hpnicfDhcpServer2OptionGroupTable':hpnicfDhcpServer2OptionGroupTable,'hpnicfDhcpServer2OptionGroupEntry':hpnicfDhcpServer2OptionGroupEntry,_Q:hpnicfDhcpServer2OptionGroupId,'hpnicfDhcpServer2OptionGroupStatus':hpnicfDhcpServer2OptionGroupStatus,'hpnicfDhcpServer2OptionTable':hpnicfDhcpServer2OptionTable,'hpnicfDhcpServer2OptionEntry':hpnicfDhcpServer2OptionEntry,_m:hpnicfDhcpServer2OptionCode,'hpnicfDhcpServer2OptionType':hpnicfDhcpServer2OptionType,'hpnicfDhcpServer2OptionAscii':hpnicfDhcpServer2OptionAscii,'hpnicfDhcpServer2OptionHexStr':hpnicfDhcpServer2OptionHexStr,'hpnicfDhcpServer2OptionIPStr':hpnicfDhcpServer2OptionIPStr,'hpnicfDhcpServer2OptionRowStatus':hpnicfDhcpServer2OptionRowStatus,'hpnicfDhcpRelay2ScalarObjects':hpnicfDhcpRelay2ScalarObjects,'hpnicfDhcpRelay2ConfigGroup':hpnicfDhcpRelay2ConfigGroup,'hpnicfDhcpRelay2UserInfoRecord':hpnicfDhcpRelay2UserInfoRecord,'hpnicfDhcpRelay2UserInfoRefresh':hpnicfDhcpRelay2UserInfoRefresh,'hpnicfDhcpRelay2UserInfoFlushTime':hpnicfDhcpRelay2UserInfoFlushTime,'hpnicfDhcpRelay2ReleaseAddr':hpnicfDhcpRelay2ReleaseAddr,'hpnicfDhcpRelay2StatisticsGroup':hpnicfDhcpRelay2StatisticsGroup,'hpnicfDhcpRelay2RxClientNum':hpnicfDhcpRelay2RxClientNum,'hpnicfDhcpRelay2TxClientNum':hpnicfDhcpRelay2TxClientNum,'hpnicfDhcpRelay2RxServerNum':hpnicfDhcpRelay2RxServerNum,'hpnicfDhcpRelay2TxServerNum':hpnicfDhcpRelay2TxServerNum,'hpnicfDhcpRelay2BadNum':hpnicfDhcpRelay2BadNum,'hpnicfDhcpRelay2BootpRequestNum':hpnicfDhcpRelay2BootpRequestNum,'hpnicfDhcpRelay2DiscoverNum':hpnicfDhcpRelay2DiscoverNum,'hpnicfDhcpRelay2RequestNum':hpnicfDhcpRelay2RequestNum,'hpnicfDhcpRelay2DeclineNum':hpnicfDhcpRelay2DeclineNum,'hpnicfDhcpRelay2ReleaseNum':hpnicfDhcpRelay2ReleaseNum,'hpnicfDhcpRelay2InformNum':hpnicfDhcpRelay2InformNum,'hpnicfDhcpRelay2BootpReplyNum':hpnicfDhcpRelay2BootpReplyNum,'hpnicfDhcpRelay2OfferNum':hpnicfDhcpRelay2OfferNum,'hpnicfDhcpRelay2AckNum':hpnicfDhcpRelay2AckNum,'hpnicfDhcpRelay2NakNum':hpnicfDhcpRelay2NakNum,'hpnicfDhcpRelay2Tables':hpnicfDhcpRelay2Tables,'hpnicfDhcpRelay2IfConfigTable':hpnicfDhcpRelay2IfConfigTable,'hpnicfDhcpRelay2IfConfigEntry':hpnicfDhcpRelay2IfConfigEntry,'hpnicfDhcpRelay2IfSelectRelay':hpnicfDhcpRelay2IfSelectRelay,'hpnicfDhcpRelay2IfCheckMac':hpnicfDhcpRelay2IfCheckMac,'hpnicfDhcpRelay2IfOpt82Enable':hpnicfDhcpRelay2IfOpt82Enable,'hpnicfDhcpRelay2IfOpt82Strategy':hpnicfDhcpRelay2IfOpt82Strategy,'hpnicfDhcpRelay2IfOpt82CIDMode':hpnicfDhcpRelay2IfOpt82CIDMode,'hpnicfDhcpRelay2IfOpt82CIDNodeType':hpnicfDhcpRelay2IfOpt82CIDNodeType,'hpnicfDhcpRelay2IfOpt82CIDNodeStr':hpnicfDhcpRelay2IfOpt82CIDNodeStr,'hpnicfDhcpRelay2IfOpt82CIDStr':hpnicfDhcpRelay2IfOpt82CIDStr,'hpnicfDhcpRelay2IfOpt82CIDFormat':hpnicfDhcpRelay2IfOpt82CIDFormat,'hpnicfDhcpRelay2IfOpt82RIDMode':hpnicfDhcpRelay2IfOpt82RIDMode,'hpnicfDhcpRelay2IfOpt82RIDStr':hpnicfDhcpRelay2IfOpt82RIDStr,'hpnicfDhcpRelay2IfOpt82RIDFormat':hpnicfDhcpRelay2IfOpt82RIDFormat,'hpnicfDhcpRelay2SrvAddrTable':hpnicfDhcpRelay2SrvAddrTable,'hpnicfDhcpRelay2SrvAddrEntry':hpnicfDhcpRelay2SrvAddrEntry,_p:hpnicfDhcpRelay2SrvAddrIP,'hpnicfDhcpRelay2SrvAddrRowStatus':hpnicfDhcpRelay2SrvAddrRowStatus,'hpnicfDhcpRelay2UserInfoTable':hpnicfDhcpRelay2UserInfoTable,'hpnicfDhcpRelay2UserInfoEntry':hpnicfDhcpRelay2UserInfoEntry,_q:hpnicfDhcpRelay2UserInfoVpnIndex,_r:hpnicfDhcpRelay2UserInfoIpAddr,'hpnicfDhcpRelay2UserInfoMacAddr':hpnicfDhcpRelay2UserInfoMacAddr,'hpnicfDhcpRelay2UserInfoIfIndex':hpnicfDhcpRelay2UserInfoIfIndex,'hpnicfDhcpRelay2UserInfoRowStatus':hpnicfDhcpRelay2UserInfoRowStatus})