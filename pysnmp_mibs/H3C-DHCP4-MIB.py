_s='h3cDhcpRelay2UserInfoIpAddr'
_r='h3cDhcpRelay2UserInfoVpnIndex'
_q='h3cDhcpRelay2SrvAddrIP'
_p='sysname'
_o='normal'
_n='h3cDhcpServer2OptionCode'
_m='h3cDhcpServer2RuleHwAddrNumber'
_l='h3cDhcpServer2ValidClassName'
_k='h3cDhcpServer2DefOptGrpClass'
_j='h3cDhcpServer2IPInUseIP'
_i='h3cDhcpServer2ExpiredIP'
_h='h3cDhcpServer2ConflictIP'
_g='h3cDhcpServer2FreeStart'
_f='h3cDhcpServer2ForbidEnd'
_e='h3cDhcpServer2ForbidStart'
_d='h3cDhcpServer2ForbidVpnName'
_c='h3cDhcpServer2RuleNumber'
_b='h3cDhcpServer2PoolForbidIP'
_a='h3cDhcpServer2PoolOptCode'
_Z='tokenRing'
_Y='ethernet'
_X='default'
_W='h3cDhcpServer2PoolStaticIP'
_V='h3cDhcpServer2PoolClassName'
_U='h3cDhcpServer2PoolSecNwMask'
_T='h3cDhcpServer2PoolSecNw'
_S='userDefine'
_R='h3cDhcpServer2OptionGroupId'
_Q='h3cDhcpServer2ClassName'
_P='hex'
_O='ascii'
_N='ifIndex'
_M='IF-MIB'
_L='h3cDhcpServer2PoolName'
_K='Unsigned32'
_J='TruthValue'
_I='h3cDhcpServer2PoolIndex'
_H='not-accessible'
_G='read-write'
_F='Integer32'
_E='OctetString'
_D='H3C-DHCP4-MIB'
_C='read-only'
_B='read-create'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_E,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
h3cCommon,=mibBuilder.importSymbols('HUAWEI-3COM-OID-MIB','h3cCommon')
InterfaceIndexOrZero,ifIndex=mibBuilder.importSymbols(_M,'InterfaceIndexOrZero',_N)
InetAddressIPv4,=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddressIPv4')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_K,'iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention',_J)
h3cDhcp4=ModuleIdentity((1,3,6,1,4,1,2011,10,2,122))
if mibBuilder.loadTexts:h3cDhcp4.setRevisions(('2017-06-03 00:00','2017-01-13 00:00','2015-08-05 00:00','2013-04-24 00:00'))
_H3cDhcpServer2ScalarObjects_ObjectIdentity=ObjectIdentity
h3cDhcpServer2ScalarObjects=_H3cDhcpServer2ScalarObjects_ObjectIdentity((1,3,6,1,4,1,2011,10,2,122,1))
_H3cDhcpServer2ConfigGroup_ObjectIdentity=ObjectIdentity
h3cDhcpServer2ConfigGroup=_H3cDhcpServer2ConfigGroup_ObjectIdentity((1,3,6,1,4,1,2011,10,2,122,1,1))
class _H3cDhcpServer2Enabled_Type(TruthValue):defaultValue=2
_H3cDhcpServer2Enabled_Type.__name__=_J
_H3cDhcpServer2Enabled_Object=MibScalar
h3cDhcpServer2Enabled=_H3cDhcpServer2Enabled_Object((1,3,6,1,4,1,2011,10,2,122,1,1,1),_H3cDhcpServer2Enabled_Type())
h3cDhcpServer2Enabled.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cDhcpServer2Enabled.setStatus(_A)
class _H3cDhcpServer2AlwaysBroadcast_Type(TruthValue):defaultValue=2
_H3cDhcpServer2AlwaysBroadcast_Type.__name__=_J
_H3cDhcpServer2AlwaysBroadcast_Object=MibScalar
h3cDhcpServer2AlwaysBroadcast=_H3cDhcpServer2AlwaysBroadcast_Object((1,3,6,1,4,1,2011,10,2,122,1,1,2),_H3cDhcpServer2AlwaysBroadcast_Type())
h3cDhcpServer2AlwaysBroadcast.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cDhcpServer2AlwaysBroadcast.setStatus(_A)
class _H3cDhcpServer2IgnoreBootp_Type(TruthValue):defaultValue=2
_H3cDhcpServer2IgnoreBootp_Type.__name__=_J
_H3cDhcpServer2IgnoreBootp_Object=MibScalar
h3cDhcpServer2IgnoreBootp=_H3cDhcpServer2IgnoreBootp_Object((1,3,6,1,4,1,2011,10,2,122,1,1,3),_H3cDhcpServer2IgnoreBootp_Type())
h3cDhcpServer2IgnoreBootp.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cDhcpServer2IgnoreBootp.setStatus(_A)
class _H3cDhcpServer2BootpReplyRfc1048_Type(TruthValue):defaultValue=2
_H3cDhcpServer2BootpReplyRfc1048_Type.__name__=_J
_H3cDhcpServer2BootpReplyRfc1048_Object=MibScalar
h3cDhcpServer2BootpReplyRfc1048=_H3cDhcpServer2BootpReplyRfc1048_Object((1,3,6,1,4,1,2011,10,2,122,1,1,4),_H3cDhcpServer2BootpReplyRfc1048_Type())
h3cDhcpServer2BootpReplyRfc1048.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cDhcpServer2BootpReplyRfc1048.setStatus(_A)
class _H3cDhcpServer2Opt82Enabled_Type(TruthValue):defaultValue=1
_H3cDhcpServer2Opt82Enabled_Type.__name__=_J
_H3cDhcpServer2Opt82Enabled_Object=MibScalar
h3cDhcpServer2Opt82Enabled=_H3cDhcpServer2Opt82Enabled_Object((1,3,6,1,4,1,2011,10,2,122,1,1,5),_H3cDhcpServer2Opt82Enabled_Type())
h3cDhcpServer2Opt82Enabled.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cDhcpServer2Opt82Enabled.setStatus(_A)
class _H3cDhcpServer2PingNumber_Type(Unsigned32):defaultValue=1;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10))
_H3cDhcpServer2PingNumber_Type.__name__=_K
_H3cDhcpServer2PingNumber_Object=MibScalar
h3cDhcpServer2PingNumber=_H3cDhcpServer2PingNumber_Object((1,3,6,1,4,1,2011,10,2,122,1,1,6),_H3cDhcpServer2PingNumber_Type())
h3cDhcpServer2PingNumber.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cDhcpServer2PingNumber.setStatus(_A)
class _H3cDhcpServer2PingTimeout_Type(Unsigned32):defaultValue=500;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10000))
_H3cDhcpServer2PingTimeout_Type.__name__=_K
_H3cDhcpServer2PingTimeout_Object=MibScalar
h3cDhcpServer2PingTimeout=_H3cDhcpServer2PingTimeout_Object((1,3,6,1,4,1,2011,10,2,122,1,1,7),_H3cDhcpServer2PingTimeout_Type())
h3cDhcpServer2PingTimeout.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cDhcpServer2PingTimeout.setStatus(_A)
class _H3cDhcpServer2AllocThreshold_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_H3cDhcpServer2AllocThreshold_Type.__name__=_K
_H3cDhcpServer2AllocThreshold_Object=MibScalar
h3cDhcpServer2AllocThreshold=_H3cDhcpServer2AllocThreshold_Object((1,3,6,1,4,1,2011,10,2,122,1,1,8),_H3cDhcpServer2AllocThreshold_Type())
h3cDhcpServer2AllocThreshold.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cDhcpServer2AllocThreshold.setStatus(_A)
_H3cDhcpServer2StatGroup_ObjectIdentity=ObjectIdentity
h3cDhcpServer2StatGroup=_H3cDhcpServer2StatGroup_ObjectIdentity((1,3,6,1,4,1,2011,10,2,122,1,2))
_H3cDhcpServer2BadNum_Type=Counter64
_H3cDhcpServer2BadNum_Object=MibScalar
h3cDhcpServer2BadNum=_H3cDhcpServer2BadNum_Object((1,3,6,1,4,1,2011,10,2,122,1,2,1),_H3cDhcpServer2BadNum_Type())
h3cDhcpServer2BadNum.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cDhcpServer2BadNum.setStatus(_A)
_H3cDhcpServer2BootpRequestNum_Type=Counter64
_H3cDhcpServer2BootpRequestNum_Object=MibScalar
h3cDhcpServer2BootpRequestNum=_H3cDhcpServer2BootpRequestNum_Object((1,3,6,1,4,1,2011,10,2,122,1,2,2),_H3cDhcpServer2BootpRequestNum_Type())
h3cDhcpServer2BootpRequestNum.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cDhcpServer2BootpRequestNum.setStatus(_A)
_H3cDhcpServer2DiscoverNum_Type=Counter64
_H3cDhcpServer2DiscoverNum_Object=MibScalar
h3cDhcpServer2DiscoverNum=_H3cDhcpServer2DiscoverNum_Object((1,3,6,1,4,1,2011,10,2,122,1,2,3),_H3cDhcpServer2DiscoverNum_Type())
h3cDhcpServer2DiscoverNum.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cDhcpServer2DiscoverNum.setStatus(_A)
_H3cDhcpServer2RequestNum_Type=Counter64
_H3cDhcpServer2RequestNum_Object=MibScalar
h3cDhcpServer2RequestNum=_H3cDhcpServer2RequestNum_Object((1,3,6,1,4,1,2011,10,2,122,1,2,4),_H3cDhcpServer2RequestNum_Type())
h3cDhcpServer2RequestNum.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cDhcpServer2RequestNum.setStatus(_A)
_H3cDhcpServer2DeclineNum_Type=Counter64
_H3cDhcpServer2DeclineNum_Object=MibScalar
h3cDhcpServer2DeclineNum=_H3cDhcpServer2DeclineNum_Object((1,3,6,1,4,1,2011,10,2,122,1,2,5),_H3cDhcpServer2DeclineNum_Type())
h3cDhcpServer2DeclineNum.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cDhcpServer2DeclineNum.setStatus(_A)
_H3cDhcpServer2ReleaseNum_Type=Counter64
_H3cDhcpServer2ReleaseNum_Object=MibScalar
h3cDhcpServer2ReleaseNum=_H3cDhcpServer2ReleaseNum_Object((1,3,6,1,4,1,2011,10,2,122,1,2,6),_H3cDhcpServer2ReleaseNum_Type())
h3cDhcpServer2ReleaseNum.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cDhcpServer2ReleaseNum.setStatus(_A)
_H3cDhcpServer2InformNum_Type=Counter64
_H3cDhcpServer2InformNum_Object=MibScalar
h3cDhcpServer2InformNum=_H3cDhcpServer2InformNum_Object((1,3,6,1,4,1,2011,10,2,122,1,2,7),_H3cDhcpServer2InformNum_Type())
h3cDhcpServer2InformNum.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cDhcpServer2InformNum.setStatus(_A)
_H3cDhcpServer2BootpReplyNum_Type=Counter64
_H3cDhcpServer2BootpReplyNum_Object=MibScalar
h3cDhcpServer2BootpReplyNum=_H3cDhcpServer2BootpReplyNum_Object((1,3,6,1,4,1,2011,10,2,122,1,2,8),_H3cDhcpServer2BootpReplyNum_Type())
h3cDhcpServer2BootpReplyNum.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cDhcpServer2BootpReplyNum.setStatus(_A)
_H3cDhcpServer2OfferNum_Type=Counter64
_H3cDhcpServer2OfferNum_Object=MibScalar
h3cDhcpServer2OfferNum=_H3cDhcpServer2OfferNum_Object((1,3,6,1,4,1,2011,10,2,122,1,2,9),_H3cDhcpServer2OfferNum_Type())
h3cDhcpServer2OfferNum.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cDhcpServer2OfferNum.setStatus(_A)
_H3cDhcpServer2AckNum_Type=Counter64
_H3cDhcpServer2AckNum_Object=MibScalar
h3cDhcpServer2AckNum=_H3cDhcpServer2AckNum_Object((1,3,6,1,4,1,2011,10,2,122,1,2,10),_H3cDhcpServer2AckNum_Type())
h3cDhcpServer2AckNum.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cDhcpServer2AckNum.setStatus(_A)
_H3cDhcpServer2NakNum_Type=Counter64
_H3cDhcpServer2NakNum_Object=MibScalar
h3cDhcpServer2NakNum=_H3cDhcpServer2NakNum_Object((1,3,6,1,4,1,2011,10,2,122,1,2,11),_H3cDhcpServer2NakNum_Type())
h3cDhcpServer2NakNum.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cDhcpServer2NakNum.setStatus(_A)
class _H3cDhcpServer2TotalPoolUsage_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_H3cDhcpServer2TotalPoolUsage_Type.__name__=_K
_H3cDhcpServer2TotalPoolUsage_Object=MibScalar
h3cDhcpServer2TotalPoolUsage=_H3cDhcpServer2TotalPoolUsage_Object((1,3,6,1,4,1,2011,10,2,122,1,2,12),_H3cDhcpServer2TotalPoolUsage_Type())
h3cDhcpServer2TotalPoolUsage.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cDhcpServer2TotalPoolUsage.setStatus(_A)
_H3cDhcpServer2PoolNumber_Type=Unsigned32
_H3cDhcpServer2PoolNumber_Object=MibScalar
h3cDhcpServer2PoolNumber=_H3cDhcpServer2PoolNumber_Object((1,3,6,1,4,1,2011,10,2,122,1,2,13),_H3cDhcpServer2PoolNumber_Type())
h3cDhcpServer2PoolNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cDhcpServer2PoolNumber.setStatus(_A)
_H3cDhcpServer2ConflictNum_Type=Unsigned32
_H3cDhcpServer2ConflictNum_Object=MibScalar
h3cDhcpServer2ConflictNum=_H3cDhcpServer2ConflictNum_Object((1,3,6,1,4,1,2011,10,2,122,1,2,14),_H3cDhcpServer2ConflictNum_Type())
h3cDhcpServer2ConflictNum.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cDhcpServer2ConflictNum.setStatus(_A)
_H3cDhcpServer2AutoBindNum_Type=Unsigned32
_H3cDhcpServer2AutoBindNum_Object=MibScalar
h3cDhcpServer2AutoBindNum=_H3cDhcpServer2AutoBindNum_Object((1,3,6,1,4,1,2011,10,2,122,1,2,15),_H3cDhcpServer2AutoBindNum_Type())
h3cDhcpServer2AutoBindNum.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cDhcpServer2AutoBindNum.setStatus(_A)
_H3cDhcpServer2ManualBindNum_Type=Unsigned32
_H3cDhcpServer2ManualBindNum_Object=MibScalar
h3cDhcpServer2ManualBindNum=_H3cDhcpServer2ManualBindNum_Object((1,3,6,1,4,1,2011,10,2,122,1,2,16),_H3cDhcpServer2ManualBindNum_Type())
h3cDhcpServer2ManualBindNum.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cDhcpServer2ManualBindNum.setStatus(_A)
_H3cDhcpServer2ExpiredBindNum_Type=Unsigned32
_H3cDhcpServer2ExpiredBindNum_Object=MibScalar
h3cDhcpServer2ExpiredBindNum=_H3cDhcpServer2ExpiredBindNum_Object((1,3,6,1,4,1,2011,10,2,122,1,2,17),_H3cDhcpServer2ExpiredBindNum_Type())
h3cDhcpServer2ExpiredBindNum.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cDhcpServer2ExpiredBindNum.setStatus(_A)
_H3cDhcpServer2ReqCnt_Type=Counter64
_H3cDhcpServer2ReqCnt_Object=MibScalar
h3cDhcpServer2ReqCnt=_H3cDhcpServer2ReqCnt_Object((1,3,6,1,4,1,2011,10,2,122,1,2,18),_H3cDhcpServer2ReqCnt_Type())
h3cDhcpServer2ReqCnt.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cDhcpServer2ReqCnt.setStatus(_A)
_H3cDhcpServer2ReqSuccCnt_Type=Counter64
_H3cDhcpServer2ReqSuccCnt_Object=MibScalar
h3cDhcpServer2ReqSuccCnt=_H3cDhcpServer2ReqSuccCnt_Object((1,3,6,1,4,1,2011,10,2,122,1,2,19),_H3cDhcpServer2ReqSuccCnt_Type())
h3cDhcpServer2ReqSuccCnt.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cDhcpServer2ReqSuccCnt.setStatus(_A)
_H3cDhcpServer2IPTotalNum_Type=Unsigned32
_H3cDhcpServer2IPTotalNum_Object=MibScalar
h3cDhcpServer2IPTotalNum=_H3cDhcpServer2IPTotalNum_Object((1,3,6,1,4,1,2011,10,2,122,1,2,20),_H3cDhcpServer2IPTotalNum_Type())
h3cDhcpServer2IPTotalNum.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cDhcpServer2IPTotalNum.setStatus(_A)
_H3cDhcpServer2IPUsedNum_Type=Unsigned32
_H3cDhcpServer2IPUsedNum_Object=MibScalar
h3cDhcpServer2IPUsedNum=_H3cDhcpServer2IPUsedNum_Object((1,3,6,1,4,1,2011,10,2,122,1,2,21),_H3cDhcpServer2IPUsedNum_Type())
h3cDhcpServer2IPUsedNum.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cDhcpServer2IPUsedNum.setStatus(_A)
_H3cDhcpServer2IPIdleNum_Type=Unsigned32
_H3cDhcpServer2IPIdleNum_Object=MibScalar
h3cDhcpServer2IPIdleNum=_H3cDhcpServer2IPIdleNum_Object((1,3,6,1,4,1,2011,10,2,122,1,2,22),_H3cDhcpServer2IPIdleNum_Type())
h3cDhcpServer2IPIdleNum.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cDhcpServer2IPIdleNum.setStatus(_A)
_H3cDhcpServer2IPExcludeTotalNum_Type=Unsigned32
_H3cDhcpServer2IPExcludeTotalNum_Object=MibScalar
h3cDhcpServer2IPExcludeTotalNum=_H3cDhcpServer2IPExcludeTotalNum_Object((1,3,6,1,4,1,2011,10,2,122,1,2,23),_H3cDhcpServer2IPExcludeTotalNum_Type())
h3cDhcpServer2IPExcludeTotalNum.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cDhcpServer2IPExcludeTotalNum.setStatus(_A)
_H3cDhcpServer2Tables_ObjectIdentity=ObjectIdentity
h3cDhcpServer2Tables=_H3cDhcpServer2Tables_ObjectIdentity((1,3,6,1,4,1,2011,10,2,122,2))
_H3cDhcpServer2PoolTable_Object=MibTable
h3cDhcpServer2PoolTable=_H3cDhcpServer2PoolTable_Object((1,3,6,1,4,1,2011,10,2,122,2,1))
if mibBuilder.loadTexts:h3cDhcpServer2PoolTable.setStatus(_A)
_H3cDhcpServer2PoolEntry_Object=MibTableRow
h3cDhcpServer2PoolEntry=_H3cDhcpServer2PoolEntry_Object((1,3,6,1,4,1,2011,10,2,122,2,1,1))
h3cDhcpServer2PoolEntry.setIndexNames((0,_D,_I))
if mibBuilder.loadTexts:h3cDhcpServer2PoolEntry.setStatus(_A)
class _H3cDhcpServer2PoolIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_H3cDhcpServer2PoolIndex_Type.__name__=_K
_H3cDhcpServer2PoolIndex_Object=MibTableColumn
h3cDhcpServer2PoolIndex=_H3cDhcpServer2PoolIndex_Object((1,3,6,1,4,1,2011,10,2,122,2,1,1,1),_H3cDhcpServer2PoolIndex_Type())
h3cDhcpServer2PoolIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:h3cDhcpServer2PoolIndex.setStatus(_A)
class _H3cDhcpServer2PoolName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,63))
_H3cDhcpServer2PoolName_Type.__name__=_E
_H3cDhcpServer2PoolName_Object=MibTableColumn
h3cDhcpServer2PoolName=_H3cDhcpServer2PoolName_Object((1,3,6,1,4,1,2011,10,2,122,2,1,1,2),_H3cDhcpServer2PoolName_Type())
h3cDhcpServer2PoolName.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDhcpServer2PoolName.setStatus(_A)
class _H3cDhcpServer2PoolVpnName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_H3cDhcpServer2PoolVpnName_Type.__name__=_E
_H3cDhcpServer2PoolVpnName_Object=MibTableColumn
h3cDhcpServer2PoolVpnName=_H3cDhcpServer2PoolVpnName_Object((1,3,6,1,4,1,2011,10,2,122,2,1,1,3),_H3cDhcpServer2PoolVpnName_Type())
h3cDhcpServer2PoolVpnName.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDhcpServer2PoolVpnName.setStatus(_A)
_H3cDhcpServer2PoolNetwork_Type=InetAddressIPv4
_H3cDhcpServer2PoolNetwork_Object=MibTableColumn
h3cDhcpServer2PoolNetwork=_H3cDhcpServer2PoolNetwork_Object((1,3,6,1,4,1,2011,10,2,122,2,1,1,4),_H3cDhcpServer2PoolNetwork_Type())
h3cDhcpServer2PoolNetwork.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDhcpServer2PoolNetwork.setStatus(_A)
_H3cDhcpServer2PoolNetworkMask_Type=InetAddressIPv4
_H3cDhcpServer2PoolNetworkMask_Object=MibTableColumn
h3cDhcpServer2PoolNetworkMask=_H3cDhcpServer2PoolNetworkMask_Object((1,3,6,1,4,1,2011,10,2,122,2,1,1,5),_H3cDhcpServer2PoolNetworkMask_Type())
h3cDhcpServer2PoolNetworkMask.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDhcpServer2PoolNetworkMask.setStatus(_A)
_H3cDhcpServer2PoolStartAddr_Type=InetAddressIPv4
_H3cDhcpServer2PoolStartAddr_Object=MibTableColumn
h3cDhcpServer2PoolStartAddr=_H3cDhcpServer2PoolStartAddr_Object((1,3,6,1,4,1,2011,10,2,122,2,1,1,6),_H3cDhcpServer2PoolStartAddr_Type())
h3cDhcpServer2PoolStartAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDhcpServer2PoolStartAddr.setStatus(_A)
_H3cDhcpServer2PoolEndAddr_Type=InetAddressIPv4
_H3cDhcpServer2PoolEndAddr_Object=MibTableColumn
h3cDhcpServer2PoolEndAddr=_H3cDhcpServer2PoolEndAddr_Object((1,3,6,1,4,1,2011,10,2,122,2,1,1,7),_H3cDhcpServer2PoolEndAddr_Type())
h3cDhcpServer2PoolEndAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDhcpServer2PoolEndAddr.setStatus(_A)
class _H3cDhcpServer2PoolLeaseDay_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,365))
_H3cDhcpServer2PoolLeaseDay_Type.__name__=_F
_H3cDhcpServer2PoolLeaseDay_Object=MibTableColumn
h3cDhcpServer2PoolLeaseDay=_H3cDhcpServer2PoolLeaseDay_Object((1,3,6,1,4,1,2011,10,2,122,2,1,1,8),_H3cDhcpServer2PoolLeaseDay_Type())
h3cDhcpServer2PoolLeaseDay.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDhcpServer2PoolLeaseDay.setStatus(_A)
class _H3cDhcpServer2PoolLeaseHour_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,23))
_H3cDhcpServer2PoolLeaseHour_Type.__name__=_F
_H3cDhcpServer2PoolLeaseHour_Object=MibTableColumn
h3cDhcpServer2PoolLeaseHour=_H3cDhcpServer2PoolLeaseHour_Object((1,3,6,1,4,1,2011,10,2,122,2,1,1,9),_H3cDhcpServer2PoolLeaseHour_Type())
h3cDhcpServer2PoolLeaseHour.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDhcpServer2PoolLeaseHour.setStatus(_A)
class _H3cDhcpServer2PoolLeaseMinute_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,59))
_H3cDhcpServer2PoolLeaseMinute_Type.__name__=_F
_H3cDhcpServer2PoolLeaseMinute_Object=MibTableColumn
h3cDhcpServer2PoolLeaseMinute=_H3cDhcpServer2PoolLeaseMinute_Object((1,3,6,1,4,1,2011,10,2,122,2,1,1,10),_H3cDhcpServer2PoolLeaseMinute_Type())
h3cDhcpServer2PoolLeaseMinute.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDhcpServer2PoolLeaseMinute.setStatus(_A)
class _H3cDhcpServer2PoolLeaseSecond_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,59))
_H3cDhcpServer2PoolLeaseSecond_Type.__name__=_F
_H3cDhcpServer2PoolLeaseSecond_Object=MibTableColumn
h3cDhcpServer2PoolLeaseSecond=_H3cDhcpServer2PoolLeaseSecond_Object((1,3,6,1,4,1,2011,10,2,122,2,1,1,11),_H3cDhcpServer2PoolLeaseSecond_Type())
h3cDhcpServer2PoolLeaseSecond.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDhcpServer2PoolLeaseSecond.setStatus(_A)
class _H3cDhcpServer2PoolLeaseUnlimit_Type(TruthValue):defaultValue=2
_H3cDhcpServer2PoolLeaseUnlimit_Type.__name__=_J
_H3cDhcpServer2PoolLeaseUnlimit_Object=MibTableColumn
h3cDhcpServer2PoolLeaseUnlimit=_H3cDhcpServer2PoolLeaseUnlimit_Object((1,3,6,1,4,1,2011,10,2,122,2,1,1,12),_H3cDhcpServer2PoolLeaseUnlimit_Type())
h3cDhcpServer2PoolLeaseUnlimit.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDhcpServer2PoolLeaseUnlimit.setStatus(_A)
_H3cDhcpServer2PoolLeaseTime_Type=TimeTicks
_H3cDhcpServer2PoolLeaseTime_Object=MibTableColumn
h3cDhcpServer2PoolLeaseTime=_H3cDhcpServer2PoolLeaseTime_Object((1,3,6,1,4,1,2011,10,2,122,2,1,1,13),_H3cDhcpServer2PoolLeaseTime_Type())
h3cDhcpServer2PoolLeaseTime.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDhcpServer2PoolLeaseTime.setStatus(_A)
class _H3cDhcpServer2PoolDomainName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,50))
_H3cDhcpServer2PoolDomainName_Type.__name__=_E
_H3cDhcpServer2PoolDomainName_Object=MibTableColumn
h3cDhcpServer2PoolDomainName=_H3cDhcpServer2PoolDomainName_Object((1,3,6,1,4,1,2011,10,2,122,2,1,1,14),_H3cDhcpServer2PoolDomainName_Type())
h3cDhcpServer2PoolDomainName.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDhcpServer2PoolDomainName.setStatus(_A)
class _H3cDhcpServer2PoolGatewayIP_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_H3cDhcpServer2PoolGatewayIP_Type.__name__=_E
_H3cDhcpServer2PoolGatewayIP_Object=MibTableColumn
h3cDhcpServer2PoolGatewayIP=_H3cDhcpServer2PoolGatewayIP_Object((1,3,6,1,4,1,2011,10,2,122,2,1,1,15),_H3cDhcpServer2PoolGatewayIP_Type())
h3cDhcpServer2PoolGatewayIP.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDhcpServer2PoolGatewayIP.setStatus(_A)
class _H3cDhcpServer2PoolDNSIP_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_H3cDhcpServer2PoolDNSIP_Type.__name__=_E
_H3cDhcpServer2PoolDNSIP_Object=MibTableColumn
h3cDhcpServer2PoolDNSIP=_H3cDhcpServer2PoolDNSIP_Object((1,3,6,1,4,1,2011,10,2,122,2,1,1,16),_H3cDhcpServer2PoolDNSIP_Type())
h3cDhcpServer2PoolDNSIP.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDhcpServer2PoolDNSIP.setStatus(_A)
_H3cDhcpServer2PoolPrimaryDNSIP_Type=InetAddressIPv4
_H3cDhcpServer2PoolPrimaryDNSIP_Object=MibTableColumn
h3cDhcpServer2PoolPrimaryDNSIP=_H3cDhcpServer2PoolPrimaryDNSIP_Object((1,3,6,1,4,1,2011,10,2,122,2,1,1,17),_H3cDhcpServer2PoolPrimaryDNSIP_Type())
h3cDhcpServer2PoolPrimaryDNSIP.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDhcpServer2PoolPrimaryDNSIP.setStatus(_A)
_H3cDhcpServer2PoolSecondDNSIP_Type=InetAddressIPv4
_H3cDhcpServer2PoolSecondDNSIP_Object=MibTableColumn
h3cDhcpServer2PoolSecondDNSIP=_H3cDhcpServer2PoolSecondDNSIP_Object((1,3,6,1,4,1,2011,10,2,122,2,1,1,18),_H3cDhcpServer2PoolSecondDNSIP_Type())
h3cDhcpServer2PoolSecondDNSIP.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDhcpServer2PoolSecondDNSIP.setStatus(_A)
class _H3cDhcpServer2PoolNetbiosType_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,4,8)));namedValues=NamedValues(*(('null',0),('bnode',1),('pnode',2),('mnode',4),('hnode',8)))
_H3cDhcpServer2PoolNetbiosType_Type.__name__=_F
_H3cDhcpServer2PoolNetbiosType_Object=MibTableColumn
h3cDhcpServer2PoolNetbiosType=_H3cDhcpServer2PoolNetbiosType_Object((1,3,6,1,4,1,2011,10,2,122,2,1,1,19),_H3cDhcpServer2PoolNetbiosType_Type())
h3cDhcpServer2PoolNetbiosType.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDhcpServer2PoolNetbiosType.setStatus(_A)
class _H3cDhcpServer2PoolNbnsIP_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_H3cDhcpServer2PoolNbnsIP_Type.__name__=_E
_H3cDhcpServer2PoolNbnsIP_Object=MibTableColumn
h3cDhcpServer2PoolNbnsIP=_H3cDhcpServer2PoolNbnsIP_Object((1,3,6,1,4,1,2011,10,2,122,2,1,1,20),_H3cDhcpServer2PoolNbnsIP_Type())
h3cDhcpServer2PoolNbnsIP.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDhcpServer2PoolNbnsIP.setStatus(_A)
class _H3cDhcpServer2PoolBootFileName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_H3cDhcpServer2PoolBootFileName_Type.__name__=_E
_H3cDhcpServer2PoolBootFileName_Object=MibTableColumn
h3cDhcpServer2PoolBootFileName=_H3cDhcpServer2PoolBootFileName_Object((1,3,6,1,4,1,2011,10,2,122,2,1,1,21),_H3cDhcpServer2PoolBootFileName_Type())
h3cDhcpServer2PoolBootFileName.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDhcpServer2PoolBootFileName.setStatus(_A)
_H3cDhcpServer2PoolBimsIP_Type=InetAddressIPv4
_H3cDhcpServer2PoolBimsIP_Object=MibTableColumn
h3cDhcpServer2PoolBimsIP=_H3cDhcpServer2PoolBimsIP_Object((1,3,6,1,4,1,2011,10,2,122,2,1,1,22),_H3cDhcpServer2PoolBimsIP_Type())
h3cDhcpServer2PoolBimsIP.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDhcpServer2PoolBimsIP.setStatus(_A)
class _H3cDhcpServer2PoolBimsPort_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65534))
_H3cDhcpServer2PoolBimsPort_Type.__name__=_K
_H3cDhcpServer2PoolBimsPort_Object=MibTableColumn
h3cDhcpServer2PoolBimsPort=_H3cDhcpServer2PoolBimsPort_Object((1,3,6,1,4,1,2011,10,2,122,2,1,1,23),_H3cDhcpServer2PoolBimsPort_Type())
h3cDhcpServer2PoolBimsPort.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDhcpServer2PoolBimsPort.setStatus(_A)
class _H3cDhcpServer2PoolBimsKeyStr_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_H3cDhcpServer2PoolBimsKeyStr_Type.__name__=_E
_H3cDhcpServer2PoolBimsKeyStr_Object=MibTableColumn
h3cDhcpServer2PoolBimsKeyStr=_H3cDhcpServer2PoolBimsKeyStr_Object((1,3,6,1,4,1,2011,10,2,122,2,1,1,24),_H3cDhcpServer2PoolBimsKeyStr_Type())
h3cDhcpServer2PoolBimsKeyStr.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDhcpServer2PoolBimsKeyStr.setStatus(_A)
_H3cDhcpServer2PoolNextServer_Type=InetAddressIPv4
_H3cDhcpServer2PoolNextServer_Object=MibTableColumn
h3cDhcpServer2PoolNextServer=_H3cDhcpServer2PoolNextServer_Object((1,3,6,1,4,1,2011,10,2,122,2,1,1,25),_H3cDhcpServer2PoolNextServer_Type())
h3cDhcpServer2PoolNextServer.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDhcpServer2PoolNextServer.setStatus(_A)
class _H3cDhcpServer2PoolTftpDomName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_H3cDhcpServer2PoolTftpDomName_Type.__name__=_E
_H3cDhcpServer2PoolTftpDomName_Object=MibTableColumn
h3cDhcpServer2PoolTftpDomName=_H3cDhcpServer2PoolTftpDomName_Object((1,3,6,1,4,1,2011,10,2,122,2,1,1,26),_H3cDhcpServer2PoolTftpDomName_Type())
h3cDhcpServer2PoolTftpDomName.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDhcpServer2PoolTftpDomName.setStatus(_A)
_H3cDhcpServer2PoolTftpIP_Type=InetAddressIPv4
_H3cDhcpServer2PoolTftpIP_Object=MibTableColumn
h3cDhcpServer2PoolTftpIP=_H3cDhcpServer2PoolTftpIP_Object((1,3,6,1,4,1,2011,10,2,122,2,1,1,27),_H3cDhcpServer2PoolTftpIP_Type())
h3cDhcpServer2PoolTftpIP.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDhcpServer2PoolTftpIP.setStatus(_A)
_H3cDhcpServer2PoolVoiceAsIP_Type=InetAddressIPv4
_H3cDhcpServer2PoolVoiceAsIP_Object=MibTableColumn
h3cDhcpServer2PoolVoiceAsIP=_H3cDhcpServer2PoolVoiceAsIP_Object((1,3,6,1,4,1,2011,10,2,122,2,1,1,28),_H3cDhcpServer2PoolVoiceAsIP_Type())
h3cDhcpServer2PoolVoiceAsIP.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDhcpServer2PoolVoiceAsIP.setStatus(_A)
_H3cDhcpServer2PoolVoiceFailIP_Type=InetAddressIPv4
_H3cDhcpServer2PoolVoiceFailIP_Object=MibTableColumn
h3cDhcpServer2PoolVoiceFailIP=_H3cDhcpServer2PoolVoiceFailIP_Object((1,3,6,1,4,1,2011,10,2,122,2,1,1,29),_H3cDhcpServer2PoolVoiceFailIP_Type())
h3cDhcpServer2PoolVoiceFailIP.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDhcpServer2PoolVoiceFailIP.setStatus(_A)
class _H3cDhcpServer2PoolVoiceFailStr_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,39))
_H3cDhcpServer2PoolVoiceFailStr_Type.__name__=_E
_H3cDhcpServer2PoolVoiceFailStr_Object=MibTableColumn
h3cDhcpServer2PoolVoiceFailStr=_H3cDhcpServer2PoolVoiceFailStr_Object((1,3,6,1,4,1,2011,10,2,122,2,1,1,30),_H3cDhcpServer2PoolVoiceFailStr_Type())
h3cDhcpServer2PoolVoiceFailStr.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDhcpServer2PoolVoiceFailStr.setStatus(_A)
_H3cDhcpServer2PoolVoiceNCPIP_Type=InetAddressIPv4
_H3cDhcpServer2PoolVoiceNCPIP_Object=MibTableColumn
h3cDhcpServer2PoolVoiceNCPIP=_H3cDhcpServer2PoolVoiceNCPIP_Object((1,3,6,1,4,1,2011,10,2,122,2,1,1,31),_H3cDhcpServer2PoolVoiceNCPIP_Type())
h3cDhcpServer2PoolVoiceNCPIP.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDhcpServer2PoolVoiceNCPIP.setStatus(_A)
class _H3cDhcpServer2PoolVoiceVlanId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,4094),ValueRangeConstraint(65535,65535))
_H3cDhcpServer2PoolVoiceVlanId_Type.__name__=_K
_H3cDhcpServer2PoolVoiceVlanId_Object=MibTableColumn
h3cDhcpServer2PoolVoiceVlanId=_H3cDhcpServer2PoolVoiceVlanId_Object((1,3,6,1,4,1,2011,10,2,122,2,1,1,32),_H3cDhcpServer2PoolVoiceVlanId_Type())
h3cDhcpServer2PoolVoiceVlanId.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDhcpServer2PoolVoiceVlanId.setStatus(_A)
class _H3cDhcpServer2PoolVoiceVlanEnbl_Type(TruthValue):defaultValue=2
_H3cDhcpServer2PoolVoiceVlanEnbl_Type.__name__=_J
_H3cDhcpServer2PoolVoiceVlanEnbl_Object=MibTableColumn
h3cDhcpServer2PoolVoiceVlanEnbl=_H3cDhcpServer2PoolVoiceVlanEnbl_Object((1,3,6,1,4,1,2011,10,2,122,2,1,1,33),_H3cDhcpServer2PoolVoiceVlanEnbl_Type())
h3cDhcpServer2PoolVoiceVlanEnbl.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDhcpServer2PoolVoiceVlanEnbl.setStatus(_A)
_H3cDhcpServer2PoolRowStatus_Type=RowStatus
_H3cDhcpServer2PoolRowStatus_Object=MibTableColumn
h3cDhcpServer2PoolRowStatus=_H3cDhcpServer2PoolRowStatus_Object((1,3,6,1,4,1,2011,10,2,122,2,1,1,34),_H3cDhcpServer2PoolRowStatus_Type())
h3cDhcpServer2PoolRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDhcpServer2PoolRowStatus.setStatus(_A)
class _H3cDhcpServer2PoolVerifyClass_Type(TruthValue):defaultValue=2
_H3cDhcpServer2PoolVerifyClass_Type.__name__=_J
_H3cDhcpServer2PoolVerifyClass_Object=MibTableColumn
h3cDhcpServer2PoolVerifyClass=_H3cDhcpServer2PoolVerifyClass_Object((1,3,6,1,4,1,2011,10,2,122,2,1,1,35),_H3cDhcpServer2PoolVerifyClass_Type())
h3cDhcpServer2PoolVerifyClass.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDhcpServer2PoolVerifyClass.setStatus(_A)
class _H3cDhcpServer2PoolThreshold_Type(Unsigned32):defaultValue=100;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_H3cDhcpServer2PoolThreshold_Type.__name__=_K
_H3cDhcpServer2PoolThreshold_Object=MibTableColumn
h3cDhcpServer2PoolThreshold=_H3cDhcpServer2PoolThreshold_Object((1,3,6,1,4,1,2011,10,2,122,2,1,1,36),_H3cDhcpServer2PoolThreshold_Type())
h3cDhcpServer2PoolThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDhcpServer2PoolThreshold.setStatus(_A)
_H3cDhcpServer2IfApplyPoolTable_Object=MibTable
h3cDhcpServer2IfApplyPoolTable=_H3cDhcpServer2IfApplyPoolTable_Object((1,3,6,1,4,1,2011,10,2,122,2,2))
if mibBuilder.loadTexts:h3cDhcpServer2IfApplyPoolTable.setStatus(_A)
_H3cDhcpServer2IfApplyPoolEntry_Object=MibTableRow
h3cDhcpServer2IfApplyPoolEntry=_H3cDhcpServer2IfApplyPoolEntry_Object((1,3,6,1,4,1,2011,10,2,122,2,2,1))
h3cDhcpServer2IfApplyPoolEntry.setIndexNames((0,_M,_N))
if mibBuilder.loadTexts:h3cDhcpServer2IfApplyPoolEntry.setStatus(_A)
class _H3cDhcpServer2IfApplyPoolName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_H3cDhcpServer2IfApplyPoolName_Type.__name__=_E
_H3cDhcpServer2IfApplyPoolName_Object=MibTableColumn
h3cDhcpServer2IfApplyPoolName=_H3cDhcpServer2IfApplyPoolName_Object((1,3,6,1,4,1,2011,10,2,122,2,2,1,1),_H3cDhcpServer2IfApplyPoolName_Type())
h3cDhcpServer2IfApplyPoolName.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cDhcpServer2IfApplyPoolName.setStatus(_A)
_H3cDhcpServer2PoolSecNwTable_Object=MibTable
h3cDhcpServer2PoolSecNwTable=_H3cDhcpServer2PoolSecNwTable_Object((1,3,6,1,4,1,2011,10,2,122,2,3))
if mibBuilder.loadTexts:h3cDhcpServer2PoolSecNwTable.setStatus(_A)
_H3cDhcpServer2PoolSecNwEntry_Object=MibTableRow
h3cDhcpServer2PoolSecNwEntry=_H3cDhcpServer2PoolSecNwEntry_Object((1,3,6,1,4,1,2011,10,2,122,2,3,1))
h3cDhcpServer2PoolSecNwEntry.setIndexNames((0,_D,_I),(0,_D,_T),(0,_D,_U))
if mibBuilder.loadTexts:h3cDhcpServer2PoolSecNwEntry.setStatus(_A)
_H3cDhcpServer2PoolSecNw_Type=InetAddressIPv4
_H3cDhcpServer2PoolSecNw_Object=MibTableColumn
h3cDhcpServer2PoolSecNw=_H3cDhcpServer2PoolSecNw_Object((1,3,6,1,4,1,2011,10,2,122,2,3,1,1),_H3cDhcpServer2PoolSecNw_Type())
h3cDhcpServer2PoolSecNw.setMaxAccess(_H)
if mibBuilder.loadTexts:h3cDhcpServer2PoolSecNw.setStatus(_A)
_H3cDhcpServer2PoolSecNwMask_Type=InetAddressIPv4
_H3cDhcpServer2PoolSecNwMask_Object=MibTableColumn
h3cDhcpServer2PoolSecNwMask=_H3cDhcpServer2PoolSecNwMask_Object((1,3,6,1,4,1,2011,10,2,122,2,3,1,2),_H3cDhcpServer2PoolSecNwMask_Type())
h3cDhcpServer2PoolSecNwMask.setMaxAccess(_H)
if mibBuilder.loadTexts:h3cDhcpServer2PoolSecNwMask.setStatus(_A)
class _H3cDhcpServer2PoolSecNwGwIP_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_H3cDhcpServer2PoolSecNwGwIP_Type.__name__=_E
_H3cDhcpServer2PoolSecNwGwIP_Object=MibTableColumn
h3cDhcpServer2PoolSecNwGwIP=_H3cDhcpServer2PoolSecNwGwIP_Object((1,3,6,1,4,1,2011,10,2,122,2,3,1,3),_H3cDhcpServer2PoolSecNwGwIP_Type())
h3cDhcpServer2PoolSecNwGwIP.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDhcpServer2PoolSecNwGwIP.setStatus(_A)
_H3cDhcpServer2PoolSecNwStatus_Type=RowStatus
_H3cDhcpServer2PoolSecNwStatus_Object=MibTableColumn
h3cDhcpServer2PoolSecNwStatus=_H3cDhcpServer2PoolSecNwStatus_Object((1,3,6,1,4,1,2011,10,2,122,2,3,1,4),_H3cDhcpServer2PoolSecNwStatus_Type())
h3cDhcpServer2PoolSecNwStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDhcpServer2PoolSecNwStatus.setStatus(_A)
_H3cDhcpServer2PoolClassTable_Object=MibTable
h3cDhcpServer2PoolClassTable=_H3cDhcpServer2PoolClassTable_Object((1,3,6,1,4,1,2011,10,2,122,2,4))
if mibBuilder.loadTexts:h3cDhcpServer2PoolClassTable.setStatus(_A)
_H3cDhcpServer2PoolClassEntry_Object=MibTableRow
h3cDhcpServer2PoolClassEntry=_H3cDhcpServer2PoolClassEntry_Object((1,3,6,1,4,1,2011,10,2,122,2,4,1))
h3cDhcpServer2PoolClassEntry.setIndexNames((0,_D,_I),(0,_D,_V))
if mibBuilder.loadTexts:h3cDhcpServer2PoolClassEntry.setStatus(_A)
class _H3cDhcpServer2PoolClassName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,63))
_H3cDhcpServer2PoolClassName_Type.__name__=_E
_H3cDhcpServer2PoolClassName_Object=MibTableColumn
h3cDhcpServer2PoolClassName=_H3cDhcpServer2PoolClassName_Object((1,3,6,1,4,1,2011,10,2,122,2,4,1,1),_H3cDhcpServer2PoolClassName_Type())
h3cDhcpServer2PoolClassName.setMaxAccess(_H)
if mibBuilder.loadTexts:h3cDhcpServer2PoolClassName.setStatus(_A)
_H3cDhcpServer2PoolClassStart_Type=InetAddressIPv4
_H3cDhcpServer2PoolClassStart_Object=MibTableColumn
h3cDhcpServer2PoolClassStart=_H3cDhcpServer2PoolClassStart_Object((1,3,6,1,4,1,2011,10,2,122,2,4,1,2),_H3cDhcpServer2PoolClassStart_Type())
h3cDhcpServer2PoolClassStart.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDhcpServer2PoolClassStart.setStatus(_A)
_H3cDhcpServer2PoolClassEnd_Type=InetAddressIPv4
_H3cDhcpServer2PoolClassEnd_Object=MibTableColumn
h3cDhcpServer2PoolClassEnd=_H3cDhcpServer2PoolClassEnd_Object((1,3,6,1,4,1,2011,10,2,122,2,4,1,3),_H3cDhcpServer2PoolClassEnd_Type())
h3cDhcpServer2PoolClassEnd.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDhcpServer2PoolClassEnd.setStatus(_A)
_H3cDhcpServer2PoolClassStatus_Type=RowStatus
_H3cDhcpServer2PoolClassStatus_Object=MibTableColumn
h3cDhcpServer2PoolClassStatus=_H3cDhcpServer2PoolClassStatus_Object((1,3,6,1,4,1,2011,10,2,122,2,4,1,4),_H3cDhcpServer2PoolClassStatus_Type())
h3cDhcpServer2PoolClassStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDhcpServer2PoolClassStatus.setStatus(_A)
_H3cDhcpServer2PoolStaticTable_Object=MibTable
h3cDhcpServer2PoolStaticTable=_H3cDhcpServer2PoolStaticTable_Object((1,3,6,1,4,1,2011,10,2,122,2,5))
if mibBuilder.loadTexts:h3cDhcpServer2PoolStaticTable.setStatus(_A)
_H3cDhcpServer2PoolStaticEntry_Object=MibTableRow
h3cDhcpServer2PoolStaticEntry=_H3cDhcpServer2PoolStaticEntry_Object((1,3,6,1,4,1,2011,10,2,122,2,5,1))
h3cDhcpServer2PoolStaticEntry.setIndexNames((0,_D,_I),(0,_D,_W))
if mibBuilder.loadTexts:h3cDhcpServer2PoolStaticEntry.setStatus(_A)
_H3cDhcpServer2PoolStaticIP_Type=InetAddressIPv4
_H3cDhcpServer2PoolStaticIP_Object=MibTableColumn
h3cDhcpServer2PoolStaticIP=_H3cDhcpServer2PoolStaticIP_Object((1,3,6,1,4,1,2011,10,2,122,2,5,1,1),_H3cDhcpServer2PoolStaticIP_Type())
h3cDhcpServer2PoolStaticIP.setMaxAccess(_H)
if mibBuilder.loadTexts:h3cDhcpServer2PoolStaticIP.setStatus(_A)
_H3cDhcpServer2PoolStaticMask_Type=InetAddressIPv4
_H3cDhcpServer2PoolStaticMask_Object=MibTableColumn
h3cDhcpServer2PoolStaticMask=_H3cDhcpServer2PoolStaticMask_Object((1,3,6,1,4,1,2011,10,2,122,2,5,1,2),_H3cDhcpServer2PoolStaticMask_Type())
h3cDhcpServer2PoolStaticMask.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDhcpServer2PoolStaticMask.setStatus(_A)
class _H3cDhcpServer2PoolStaticCID_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,0),ValueSizeConstraint(4,254))
_H3cDhcpServer2PoolStaticCID_Type.__name__=_E
_H3cDhcpServer2PoolStaticCID_Object=MibTableColumn
h3cDhcpServer2PoolStaticCID=_H3cDhcpServer2PoolStaticCID_Object((1,3,6,1,4,1,2011,10,2,122,2,5,1,3),_H3cDhcpServer2PoolStaticCID_Type())
h3cDhcpServer2PoolStaticCID.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDhcpServer2PoolStaticCID.setStatus(_A)
class _H3cDhcpServer2PoolStaticHAddr_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,0),ValueSizeConstraint(4,39))
_H3cDhcpServer2PoolStaticHAddr_Type.__name__=_E
_H3cDhcpServer2PoolStaticHAddr_Object=MibTableColumn
h3cDhcpServer2PoolStaticHAddr=_H3cDhcpServer2PoolStaticHAddr_Object((1,3,6,1,4,1,2011,10,2,122,2,5,1,4),_H3cDhcpServer2PoolStaticHAddr_Type())
h3cDhcpServer2PoolStaticHAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDhcpServer2PoolStaticHAddr.setStatus(_A)
class _H3cDhcpServer2PoolStaticHType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_X,1),(_Y,2),(_Z,3)))
_H3cDhcpServer2PoolStaticHType_Type.__name__=_F
_H3cDhcpServer2PoolStaticHType_Object=MibTableColumn
h3cDhcpServer2PoolStaticHType=_H3cDhcpServer2PoolStaticHType_Object((1,3,6,1,4,1,2011,10,2,122,2,5,1,5),_H3cDhcpServer2PoolStaticHType_Type())
h3cDhcpServer2PoolStaticHType.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDhcpServer2PoolStaticHType.setStatus(_A)
_H3cDhcpServer2PoolStaticStatus_Type=RowStatus
_H3cDhcpServer2PoolStaticStatus_Object=MibTableColumn
h3cDhcpServer2PoolStaticStatus=_H3cDhcpServer2PoolStaticStatus_Object((1,3,6,1,4,1,2011,10,2,122,2,5,1,6),_H3cDhcpServer2PoolStaticStatus_Type())
h3cDhcpServer2PoolStaticStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDhcpServer2PoolStaticStatus.setStatus(_A)
_H3cDhcpServer2PoolOptionTable_Object=MibTable
h3cDhcpServer2PoolOptionTable=_H3cDhcpServer2PoolOptionTable_Object((1,3,6,1,4,1,2011,10,2,122,2,6))
if mibBuilder.loadTexts:h3cDhcpServer2PoolOptionTable.setStatus(_A)
_H3cDhcpServer2PoolOptionEntry_Object=MibTableRow
h3cDhcpServer2PoolOptionEntry=_H3cDhcpServer2PoolOptionEntry_Object((1,3,6,1,4,1,2011,10,2,122,2,6,1))
h3cDhcpServer2PoolOptionEntry.setIndexNames((0,_D,_I),(0,_D,_a))
if mibBuilder.loadTexts:h3cDhcpServer2PoolOptionEntry.setStatus(_A)
class _H3cDhcpServer2PoolOptCode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,254))
_H3cDhcpServer2PoolOptCode_Type.__name__=_F
_H3cDhcpServer2PoolOptCode_Object=MibTableColumn
h3cDhcpServer2PoolOptCode=_H3cDhcpServer2PoolOptCode_Object((1,3,6,1,4,1,2011,10,2,122,2,6,1,1),_H3cDhcpServer2PoolOptCode_Type())
h3cDhcpServer2PoolOptCode.setMaxAccess(_H)
if mibBuilder.loadTexts:h3cDhcpServer2PoolOptCode.setStatus(_A)
class _H3cDhcpServer2PoolOptType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_O,1),(_P,2),('ip',3)))
_H3cDhcpServer2PoolOptType_Type.__name__=_F
_H3cDhcpServer2PoolOptType_Object=MibTableColumn
h3cDhcpServer2PoolOptType=_H3cDhcpServer2PoolOptType_Object((1,3,6,1,4,1,2011,10,2,122,2,6,1,2),_H3cDhcpServer2PoolOptType_Type())
h3cDhcpServer2PoolOptType.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDhcpServer2PoolOptType.setStatus(_A)
class _H3cDhcpServer2PoolOptAscii_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_H3cDhcpServer2PoolOptAscii_Type.__name__=_E
_H3cDhcpServer2PoolOptAscii_Object=MibTableColumn
h3cDhcpServer2PoolOptAscii=_H3cDhcpServer2PoolOptAscii_Object((1,3,6,1,4,1,2011,10,2,122,2,6,1,3),_H3cDhcpServer2PoolOptAscii_Type())
h3cDhcpServer2PoolOptAscii.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDhcpServer2PoolOptAscii.setStatus(_A)
class _H3cDhcpServer2PoolOptHexStr_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,510))
_H3cDhcpServer2PoolOptHexStr_Type.__name__=_E
_H3cDhcpServer2PoolOptHexStr_Object=MibTableColumn
h3cDhcpServer2PoolOptHexStr=_H3cDhcpServer2PoolOptHexStr_Object((1,3,6,1,4,1,2011,10,2,122,2,6,1,4),_H3cDhcpServer2PoolOptHexStr_Type())
h3cDhcpServer2PoolOptHexStr.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDhcpServer2PoolOptHexStr.setStatus(_A)
class _H3cDhcpServer2PoolOptIPStr_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_H3cDhcpServer2PoolOptIPStr_Type.__name__=_E
_H3cDhcpServer2PoolOptIPStr_Object=MibTableColumn
h3cDhcpServer2PoolOptIPStr=_H3cDhcpServer2PoolOptIPStr_Object((1,3,6,1,4,1,2011,10,2,122,2,6,1,5),_H3cDhcpServer2PoolOptIPStr_Type())
h3cDhcpServer2PoolOptIPStr.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDhcpServer2PoolOptIPStr.setStatus(_A)
_H3cDhcpServer2PoolOptRowStatus_Type=RowStatus
_H3cDhcpServer2PoolOptRowStatus_Object=MibTableColumn
h3cDhcpServer2PoolOptRowStatus=_H3cDhcpServer2PoolOptRowStatus_Object((1,3,6,1,4,1,2011,10,2,122,2,6,1,6),_H3cDhcpServer2PoolOptRowStatus_Type())
h3cDhcpServer2PoolOptRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDhcpServer2PoolOptRowStatus.setStatus(_A)
_H3cDhcpServer2PoolForbidTable_Object=MibTable
h3cDhcpServer2PoolForbidTable=_H3cDhcpServer2PoolForbidTable_Object((1,3,6,1,4,1,2011,10,2,122,2,7))
if mibBuilder.loadTexts:h3cDhcpServer2PoolForbidTable.setStatus(_A)
_H3cDhcpServer2PoolForbidEntry_Object=MibTableRow
h3cDhcpServer2PoolForbidEntry=_H3cDhcpServer2PoolForbidEntry_Object((1,3,6,1,4,1,2011,10,2,122,2,7,1))
h3cDhcpServer2PoolForbidEntry.setIndexNames((0,_D,_I),(0,_D,_b))
if mibBuilder.loadTexts:h3cDhcpServer2PoolForbidEntry.setStatus(_A)
_H3cDhcpServer2PoolForbidIP_Type=InetAddressIPv4
_H3cDhcpServer2PoolForbidIP_Object=MibTableColumn
h3cDhcpServer2PoolForbidIP=_H3cDhcpServer2PoolForbidIP_Object((1,3,6,1,4,1,2011,10,2,122,2,7,1,1),_H3cDhcpServer2PoolForbidIP_Type())
h3cDhcpServer2PoolForbidIP.setMaxAccess(_H)
if mibBuilder.loadTexts:h3cDhcpServer2PoolForbidIP.setStatus(_A)
_H3cDhcpServer2PoolForbidStatus_Type=RowStatus
_H3cDhcpServer2PoolForbidStatus_Object=MibTableColumn
h3cDhcpServer2PoolForbidStatus=_H3cDhcpServer2PoolForbidStatus_Object((1,3,6,1,4,1,2011,10,2,122,2,7,1,2),_H3cDhcpServer2PoolForbidStatus_Type())
h3cDhcpServer2PoolForbidStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDhcpServer2PoolForbidStatus.setStatus(_A)
_H3cDhcpServer2ClassTable_Object=MibTable
h3cDhcpServer2ClassTable=_H3cDhcpServer2ClassTable_Object((1,3,6,1,4,1,2011,10,2,122,2,8))
if mibBuilder.loadTexts:h3cDhcpServer2ClassTable.setStatus(_A)
_H3cDhcpServer2ClassEntry_Object=MibTableRow
h3cDhcpServer2ClassEntry=_H3cDhcpServer2ClassEntry_Object((1,3,6,1,4,1,2011,10,2,122,2,8,1))
h3cDhcpServer2ClassEntry.setIndexNames((0,_D,_Q))
if mibBuilder.loadTexts:h3cDhcpServer2ClassEntry.setStatus(_A)
class _H3cDhcpServer2ClassName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,63))
_H3cDhcpServer2ClassName_Type.__name__=_E
_H3cDhcpServer2ClassName_Object=MibTableColumn
h3cDhcpServer2ClassName=_H3cDhcpServer2ClassName_Object((1,3,6,1,4,1,2011,10,2,122,2,8,1,1),_H3cDhcpServer2ClassName_Type())
h3cDhcpServer2ClassName.setMaxAccess(_H)
if mibBuilder.loadTexts:h3cDhcpServer2ClassName.setStatus(_A)
_H3cDhcpServer2ClassRowStatus_Type=RowStatus
_H3cDhcpServer2ClassRowStatus_Object=MibTableColumn
h3cDhcpServer2ClassRowStatus=_H3cDhcpServer2ClassRowStatus_Object((1,3,6,1,4,1,2011,10,2,122,2,8,1,2),_H3cDhcpServer2ClassRowStatus_Type())
h3cDhcpServer2ClassRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDhcpServer2ClassRowStatus.setStatus(_A)
_H3cDhcpServer2RuleTable_Object=MibTable
h3cDhcpServer2RuleTable=_H3cDhcpServer2RuleTable_Object((1,3,6,1,4,1,2011,10,2,122,2,9))
if mibBuilder.loadTexts:h3cDhcpServer2RuleTable.setStatus(_A)
_H3cDhcpServer2RuleEntry_Object=MibTableRow
h3cDhcpServer2RuleEntry=_H3cDhcpServer2RuleEntry_Object((1,3,6,1,4,1,2011,10,2,122,2,9,1))
h3cDhcpServer2RuleEntry.setIndexNames((0,_D,_Q),(0,_D,_c))
if mibBuilder.loadTexts:h3cDhcpServer2RuleEntry.setStatus(_A)
class _H3cDhcpServer2RuleNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,128))
_H3cDhcpServer2RuleNumber_Type.__name__=_F
_H3cDhcpServer2RuleNumber_Object=MibTableColumn
h3cDhcpServer2RuleNumber=_H3cDhcpServer2RuleNumber_Object((1,3,6,1,4,1,2011,10,2,122,2,9,1,1),_H3cDhcpServer2RuleNumber_Type())
h3cDhcpServer2RuleNumber.setMaxAccess(_H)
if mibBuilder.loadTexts:h3cDhcpServer2RuleNumber.setStatus(_A)
class _H3cDhcpServer2RuleOptCode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,254))
_H3cDhcpServer2RuleOptCode_Type.__name__=_F
_H3cDhcpServer2RuleOptCode_Object=MibTableColumn
h3cDhcpServer2RuleOptCode=_H3cDhcpServer2RuleOptCode_Object((1,3,6,1,4,1,2011,10,2,122,2,9,1,2),_H3cDhcpServer2RuleOptCode_Type())
h3cDhcpServer2RuleOptCode.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDhcpServer2RuleOptCode.setStatus(_A)
class _H3cDhcpServer2RuleOptHexStr_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,510))
_H3cDhcpServer2RuleOptHexStr_Type.__name__=_E
_H3cDhcpServer2RuleOptHexStr_Object=MibTableColumn
h3cDhcpServer2RuleOptHexStr=_H3cDhcpServer2RuleOptHexStr_Object((1,3,6,1,4,1,2011,10,2,122,2,9,1,3),_H3cDhcpServer2RuleOptHexStr_Type())
h3cDhcpServer2RuleOptHexStr.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDhcpServer2RuleOptHexStr.setStatus(_A)
class _H3cDhcpServer2RuleOptMask_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,510))
_H3cDhcpServer2RuleOptMask_Type.__name__=_E
_H3cDhcpServer2RuleOptMask_Object=MibTableColumn
h3cDhcpServer2RuleOptMask=_H3cDhcpServer2RuleOptMask_Object((1,3,6,1,4,1,2011,10,2,122,2,9,1,4),_H3cDhcpServer2RuleOptMask_Type())
h3cDhcpServer2RuleOptMask.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDhcpServer2RuleOptMask.setStatus(_A)
class _H3cDhcpServer2RuleOptOffset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,254))
_H3cDhcpServer2RuleOptOffset_Type.__name__=_F
_H3cDhcpServer2RuleOptOffset_Object=MibTableColumn
h3cDhcpServer2RuleOptOffset=_H3cDhcpServer2RuleOptOffset_Object((1,3,6,1,4,1,2011,10,2,122,2,9,1,5),_H3cDhcpServer2RuleOptOffset_Type())
h3cDhcpServer2RuleOptOffset.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDhcpServer2RuleOptOffset.setStatus(_A)
class _H3cDhcpServer2RuleOptLength_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_H3cDhcpServer2RuleOptLength_Type.__name__=_F
_H3cDhcpServer2RuleOptLength_Object=MibTableColumn
h3cDhcpServer2RuleOptLength=_H3cDhcpServer2RuleOptLength_Object((1,3,6,1,4,1,2011,10,2,122,2,9,1,6),_H3cDhcpServer2RuleOptLength_Type())
h3cDhcpServer2RuleOptLength.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDhcpServer2RuleOptLength.setStatus(_A)
_H3cDhcpServer2RuleRowStatus_Type=RowStatus
_H3cDhcpServer2RuleRowStatus_Object=MibTableColumn
h3cDhcpServer2RuleRowStatus=_H3cDhcpServer2RuleRowStatus_Object((1,3,6,1,4,1,2011,10,2,122,2,9,1,7),_H3cDhcpServer2RuleRowStatus_Type())
h3cDhcpServer2RuleRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDhcpServer2RuleRowStatus.setStatus(_A)
_H3cDhcpServer2ForbidTable_Object=MibTable
h3cDhcpServer2ForbidTable=_H3cDhcpServer2ForbidTable_Object((1,3,6,1,4,1,2011,10,2,122,2,10))
if mibBuilder.loadTexts:h3cDhcpServer2ForbidTable.setStatus(_A)
_H3cDhcpServer2ForbidEntry_Object=MibTableRow
h3cDhcpServer2ForbidEntry=_H3cDhcpServer2ForbidEntry_Object((1,3,6,1,4,1,2011,10,2,122,2,10,1))
h3cDhcpServer2ForbidEntry.setIndexNames((0,_D,_d),(0,_D,_e),(0,_D,_f))
if mibBuilder.loadTexts:h3cDhcpServer2ForbidEntry.setStatus(_A)
class _H3cDhcpServer2ForbidVpnName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,31))
_H3cDhcpServer2ForbidVpnName_Type.__name__=_E
_H3cDhcpServer2ForbidVpnName_Object=MibTableColumn
h3cDhcpServer2ForbidVpnName=_H3cDhcpServer2ForbidVpnName_Object((1,3,6,1,4,1,2011,10,2,122,2,10,1,1),_H3cDhcpServer2ForbidVpnName_Type())
h3cDhcpServer2ForbidVpnName.setMaxAccess(_H)
if mibBuilder.loadTexts:h3cDhcpServer2ForbidVpnName.setStatus(_A)
_H3cDhcpServer2ForbidStart_Type=InetAddressIPv4
_H3cDhcpServer2ForbidStart_Object=MibTableColumn
h3cDhcpServer2ForbidStart=_H3cDhcpServer2ForbidStart_Object((1,3,6,1,4,1,2011,10,2,122,2,10,1,2),_H3cDhcpServer2ForbidStart_Type())
h3cDhcpServer2ForbidStart.setMaxAccess(_H)
if mibBuilder.loadTexts:h3cDhcpServer2ForbidStart.setStatus(_A)
_H3cDhcpServer2ForbidEnd_Type=InetAddressIPv4
_H3cDhcpServer2ForbidEnd_Object=MibTableColumn
h3cDhcpServer2ForbidEnd=_H3cDhcpServer2ForbidEnd_Object((1,3,6,1,4,1,2011,10,2,122,2,10,1,3),_H3cDhcpServer2ForbidEnd_Type())
h3cDhcpServer2ForbidEnd.setMaxAccess(_H)
if mibBuilder.loadTexts:h3cDhcpServer2ForbidEnd.setStatus(_A)
_H3cDhcpServer2ForbidRowStatus_Type=RowStatus
_H3cDhcpServer2ForbidRowStatus_Object=MibTableColumn
h3cDhcpServer2ForbidRowStatus=_H3cDhcpServer2ForbidRowStatus_Object((1,3,6,1,4,1,2011,10,2,122,2,10,1,4),_H3cDhcpServer2ForbidRowStatus_Type())
h3cDhcpServer2ForbidRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDhcpServer2ForbidRowStatus.setStatus(_A)
_H3cDhcpServer2FreeTable_Object=MibTable
h3cDhcpServer2FreeTable=_H3cDhcpServer2FreeTable_Object((1,3,6,1,4,1,2011,10,2,122,2,11))
if mibBuilder.loadTexts:h3cDhcpServer2FreeTable.setStatus(_A)
_H3cDhcpServer2FreeEntry_Object=MibTableRow
h3cDhcpServer2FreeEntry=_H3cDhcpServer2FreeEntry_Object((1,3,6,1,4,1,2011,10,2,122,2,11,1))
h3cDhcpServer2FreeEntry.setIndexNames((0,_D,_I),(0,_D,_g))
if mibBuilder.loadTexts:h3cDhcpServer2FreeEntry.setStatus(_A)
_H3cDhcpServer2FreeStart_Type=InetAddressIPv4
_H3cDhcpServer2FreeStart_Object=MibTableColumn
h3cDhcpServer2FreeStart=_H3cDhcpServer2FreeStart_Object((1,3,6,1,4,1,2011,10,2,122,2,11,1,1),_H3cDhcpServer2FreeStart_Type())
h3cDhcpServer2FreeStart.setMaxAccess(_H)
if mibBuilder.loadTexts:h3cDhcpServer2FreeStart.setStatus(_A)
_H3cDhcpServer2FreeEnd_Type=InetAddressIPv4
_H3cDhcpServer2FreeEnd_Object=MibTableColumn
h3cDhcpServer2FreeEnd=_H3cDhcpServer2FreeEnd_Object((1,3,6,1,4,1,2011,10,2,122,2,11,1,2),_H3cDhcpServer2FreeEnd_Type())
h3cDhcpServer2FreeEnd.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cDhcpServer2FreeEnd.setStatus(_A)
_H3cDhcpServer2ConflictTable_Object=MibTable
h3cDhcpServer2ConflictTable=_H3cDhcpServer2ConflictTable_Object((1,3,6,1,4,1,2011,10,2,122,2,12))
if mibBuilder.loadTexts:h3cDhcpServer2ConflictTable.setStatus(_A)
_H3cDhcpServer2ConflictEntry_Object=MibTableRow
h3cDhcpServer2ConflictEntry=_H3cDhcpServer2ConflictEntry_Object((1,3,6,1,4,1,2011,10,2,122,2,12,1))
h3cDhcpServer2ConflictEntry.setIndexNames((0,_D,_I),(0,_D,_h))
if mibBuilder.loadTexts:h3cDhcpServer2ConflictEntry.setStatus(_A)
_H3cDhcpServer2ConflictIP_Type=InetAddressIPv4
_H3cDhcpServer2ConflictIP_Object=MibTableColumn
h3cDhcpServer2ConflictIP=_H3cDhcpServer2ConflictIP_Object((1,3,6,1,4,1,2011,10,2,122,2,12,1,1),_H3cDhcpServer2ConflictIP_Type())
h3cDhcpServer2ConflictIP.setMaxAccess(_H)
if mibBuilder.loadTexts:h3cDhcpServer2ConflictIP.setStatus(_A)
class _H3cDhcpServer2ConflictType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('detectByServer',1),('detectByClient',2)))
_H3cDhcpServer2ConflictType_Type.__name__=_F
_H3cDhcpServer2ConflictType_Object=MibTableColumn
h3cDhcpServer2ConflictType=_H3cDhcpServer2ConflictType_Object((1,3,6,1,4,1,2011,10,2,122,2,12,1,2),_H3cDhcpServer2ConflictType_Type())
h3cDhcpServer2ConflictType.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cDhcpServer2ConflictType.setStatus(_A)
class _H3cDhcpServer2ConflictTime_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,19))
_H3cDhcpServer2ConflictTime_Type.__name__=_E
_H3cDhcpServer2ConflictTime_Object=MibTableColumn
h3cDhcpServer2ConflictTime=_H3cDhcpServer2ConflictTime_Object((1,3,6,1,4,1,2011,10,2,122,2,12,1,3),_H3cDhcpServer2ConflictTime_Type())
h3cDhcpServer2ConflictTime.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cDhcpServer2ConflictTime.setStatus(_A)
_H3cDhcpServer2ConflictRowStatus_Type=RowStatus
_H3cDhcpServer2ConflictRowStatus_Object=MibTableColumn
h3cDhcpServer2ConflictRowStatus=_H3cDhcpServer2ConflictRowStatus_Object((1,3,6,1,4,1,2011,10,2,122,2,12,1,4),_H3cDhcpServer2ConflictRowStatus_Type())
h3cDhcpServer2ConflictRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDhcpServer2ConflictRowStatus.setStatus(_A)
_H3cDhcpServer2ExpiredTable_Object=MibTable
h3cDhcpServer2ExpiredTable=_H3cDhcpServer2ExpiredTable_Object((1,3,6,1,4,1,2011,10,2,122,2,13))
if mibBuilder.loadTexts:h3cDhcpServer2ExpiredTable.setStatus(_A)
_H3cDhcpServer2ExpiredEntry_Object=MibTableRow
h3cDhcpServer2ExpiredEntry=_H3cDhcpServer2ExpiredEntry_Object((1,3,6,1,4,1,2011,10,2,122,2,13,1))
h3cDhcpServer2ExpiredEntry.setIndexNames((0,_D,_I),(0,_D,_i))
if mibBuilder.loadTexts:h3cDhcpServer2ExpiredEntry.setStatus(_A)
_H3cDhcpServer2ExpiredIP_Type=InetAddressIPv4
_H3cDhcpServer2ExpiredIP_Object=MibTableColumn
h3cDhcpServer2ExpiredIP=_H3cDhcpServer2ExpiredIP_Object((1,3,6,1,4,1,2011,10,2,122,2,13,1,1),_H3cDhcpServer2ExpiredIP_Type())
h3cDhcpServer2ExpiredIP.setMaxAccess(_H)
if mibBuilder.loadTexts:h3cDhcpServer2ExpiredIP.setStatus(_A)
class _H3cDhcpServer2ExpiredClientId_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,254))
_H3cDhcpServer2ExpiredClientId_Type.__name__=_E
_H3cDhcpServer2ExpiredClientId_Object=MibTableColumn
h3cDhcpServer2ExpiredClientId=_H3cDhcpServer2ExpiredClientId_Object((1,3,6,1,4,1,2011,10,2,122,2,13,1,2),_H3cDhcpServer2ExpiredClientId_Type())
h3cDhcpServer2ExpiredClientId.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cDhcpServer2ExpiredClientId.setStatus(_A)
class _H3cDhcpServer2ExpiredTime_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,19))
_H3cDhcpServer2ExpiredTime_Type.__name__=_E
_H3cDhcpServer2ExpiredTime_Object=MibTableColumn
h3cDhcpServer2ExpiredTime=_H3cDhcpServer2ExpiredTime_Object((1,3,6,1,4,1,2011,10,2,122,2,13,1,3),_H3cDhcpServer2ExpiredTime_Type())
h3cDhcpServer2ExpiredTime.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cDhcpServer2ExpiredTime.setStatus(_A)
_H3cDhcpServer2ExpiredRowStatus_Type=RowStatus
_H3cDhcpServer2ExpiredRowStatus_Object=MibTableColumn
h3cDhcpServer2ExpiredRowStatus=_H3cDhcpServer2ExpiredRowStatus_Object((1,3,6,1,4,1,2011,10,2,122,2,13,1,4),_H3cDhcpServer2ExpiredRowStatus_Type())
h3cDhcpServer2ExpiredRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDhcpServer2ExpiredRowStatus.setStatus(_A)
_H3cDhcpServer2IPInUseTable_Object=MibTable
h3cDhcpServer2IPInUseTable=_H3cDhcpServer2IPInUseTable_Object((1,3,6,1,4,1,2011,10,2,122,2,14))
if mibBuilder.loadTexts:h3cDhcpServer2IPInUseTable.setStatus(_A)
_H3cDhcpServer2IPInUseEntry_Object=MibTableRow
h3cDhcpServer2IPInUseEntry=_H3cDhcpServer2IPInUseEntry_Object((1,3,6,1,4,1,2011,10,2,122,2,14,1))
h3cDhcpServer2IPInUseEntry.setIndexNames((0,_D,_I),(0,_D,_j))
if mibBuilder.loadTexts:h3cDhcpServer2IPInUseEntry.setStatus(_A)
_H3cDhcpServer2IPInUseIP_Type=InetAddressIPv4
_H3cDhcpServer2IPInUseIP_Object=MibTableColumn
h3cDhcpServer2IPInUseIP=_H3cDhcpServer2IPInUseIP_Object((1,3,6,1,4,1,2011,10,2,122,2,14,1,1),_H3cDhcpServer2IPInUseIP_Type())
h3cDhcpServer2IPInUseIP.setMaxAccess(_H)
if mibBuilder.loadTexts:h3cDhcpServer2IPInUseIP.setStatus(_A)
class _H3cDhcpServer2IPInUseClientId_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,0),ValueSizeConstraint(4,254))
_H3cDhcpServer2IPInUseClientId_Type.__name__=_E
_H3cDhcpServer2IPInUseClientId_Object=MibTableColumn
h3cDhcpServer2IPInUseClientId=_H3cDhcpServer2IPInUseClientId_Object((1,3,6,1,4,1,2011,10,2,122,2,14,1,2),_H3cDhcpServer2IPInUseClientId_Type())
h3cDhcpServer2IPInUseClientId.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cDhcpServer2IPInUseClientId.setStatus(_A)
class _H3cDhcpServer2IPInUseHardAddr_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,0),ValueSizeConstraint(4,39))
_H3cDhcpServer2IPInUseHardAddr_Type.__name__=_E
_H3cDhcpServer2IPInUseHardAddr_Object=MibTableColumn
h3cDhcpServer2IPInUseHardAddr=_H3cDhcpServer2IPInUseHardAddr_Object((1,3,6,1,4,1,2011,10,2,122,2,14,1,3),_H3cDhcpServer2IPInUseHardAddr_Type())
h3cDhcpServer2IPInUseHardAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cDhcpServer2IPInUseHardAddr.setStatus(_A)
class _H3cDhcpServer2IPInUseHardType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_X,1),(_Y,2),(_Z,3)))
_H3cDhcpServer2IPInUseHardType_Type.__name__=_F
_H3cDhcpServer2IPInUseHardType_Object=MibTableColumn
h3cDhcpServer2IPInUseHardType=_H3cDhcpServer2IPInUseHardType_Object((1,3,6,1,4,1,2011,10,2,122,2,14,1,4),_H3cDhcpServer2IPInUseHardType_Type())
h3cDhcpServer2IPInUseHardType.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cDhcpServer2IPInUseHardType.setStatus(_A)
class _H3cDhcpServer2IPInUseVlanId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094),ValueRangeConstraint(65535,65535))
_H3cDhcpServer2IPInUseVlanId_Type.__name__=_K
_H3cDhcpServer2IPInUseVlanId_Object=MibTableColumn
h3cDhcpServer2IPInUseVlanId=_H3cDhcpServer2IPInUseVlanId_Object((1,3,6,1,4,1,2011,10,2,122,2,14,1,5),_H3cDhcpServer2IPInUseVlanId_Type())
h3cDhcpServer2IPInUseVlanId.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cDhcpServer2IPInUseVlanId.setStatus(_A)
class _H3cDhcpServer2IPInUseEndLease_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,19))
_H3cDhcpServer2IPInUseEndLease_Type.__name__=_E
_H3cDhcpServer2IPInUseEndLease_Object=MibTableColumn
h3cDhcpServer2IPInUseEndLease=_H3cDhcpServer2IPInUseEndLease_Object((1,3,6,1,4,1,2011,10,2,122,2,14,1,6),_H3cDhcpServer2IPInUseEndLease_Type())
h3cDhcpServer2IPInUseEndLease.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cDhcpServer2IPInUseEndLease.setStatus(_A)
class _H3cDhcpServer2IPInUseType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('staticUnallocated',1),('staticOffered',2),('staticCommitted',3),('autoOffered',4),('autoCommitted',5)))
_H3cDhcpServer2IPInUseType_Type.__name__=_F
_H3cDhcpServer2IPInUseType_Object=MibTableColumn
h3cDhcpServer2IPInUseType=_H3cDhcpServer2IPInUseType_Object((1,3,6,1,4,1,2011,10,2,122,2,14,1,7),_H3cDhcpServer2IPInUseType_Type())
h3cDhcpServer2IPInUseType.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cDhcpServer2IPInUseType.setStatus(_A)
_H3cDhcpServer2IPInUseIfIndex_Type=InterfaceIndexOrZero
_H3cDhcpServer2IPInUseIfIndex_Object=MibTableColumn
h3cDhcpServer2IPInUseIfIndex=_H3cDhcpServer2IPInUseIfIndex_Object((1,3,6,1,4,1,2011,10,2,122,2,14,1,8),_H3cDhcpServer2IPInUseIfIndex_Type())
h3cDhcpServer2IPInUseIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cDhcpServer2IPInUseIfIndex.setStatus(_A)
_H3cDhcpServer2IPInUseRowStatus_Type=RowStatus
_H3cDhcpServer2IPInUseRowStatus_Object=MibTableColumn
h3cDhcpServer2IPInUseRowStatus=_H3cDhcpServer2IPInUseRowStatus_Object((1,3,6,1,4,1,2011,10,2,122,2,14,1,9),_H3cDhcpServer2IPInUseRowStatus_Type())
h3cDhcpServer2IPInUseRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDhcpServer2IPInUseRowStatus.setStatus(_A)
_H3cDhcpServer2DefOptGrpTable_Object=MibTable
h3cDhcpServer2DefOptGrpTable=_H3cDhcpServer2DefOptGrpTable_Object((1,3,6,1,4,1,2011,10,2,122,2,15))
if mibBuilder.loadTexts:h3cDhcpServer2DefOptGrpTable.setStatus(_A)
_H3cDhcpServer2DefOptGrpEntry_Object=MibTableRow
h3cDhcpServer2DefOptGrpEntry=_H3cDhcpServer2DefOptGrpEntry_Object((1,3,6,1,4,1,2011,10,2,122,2,15,1))
h3cDhcpServer2DefOptGrpEntry.setIndexNames((0,_D,_I),(0,_D,_k))
if mibBuilder.loadTexts:h3cDhcpServer2DefOptGrpEntry.setStatus(_A)
class _H3cDhcpServer2DefOptGrpClass_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,63))
_H3cDhcpServer2DefOptGrpClass_Type.__name__=_E
_H3cDhcpServer2DefOptGrpClass_Object=MibTableColumn
h3cDhcpServer2DefOptGrpClass=_H3cDhcpServer2DefOptGrpClass_Object((1,3,6,1,4,1,2011,10,2,122,2,15,1,1),_H3cDhcpServer2DefOptGrpClass_Type())
h3cDhcpServer2DefOptGrpClass.setMaxAccess(_H)
if mibBuilder.loadTexts:h3cDhcpServer2DefOptGrpClass.setStatus(_A)
class _H3cDhcpServer2DefOptGrpId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32768))
_H3cDhcpServer2DefOptGrpId_Type.__name__=_F
_H3cDhcpServer2DefOptGrpId_Object=MibTableColumn
h3cDhcpServer2DefOptGrpId=_H3cDhcpServer2DefOptGrpId_Object((1,3,6,1,4,1,2011,10,2,122,2,15,1,2),_H3cDhcpServer2DefOptGrpId_Type())
h3cDhcpServer2DefOptGrpId.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDhcpServer2DefOptGrpId.setStatus(_A)
_H3cDhcpServer2DefOptGrpStatus_Type=RowStatus
_H3cDhcpServer2DefOptGrpStatus_Object=MibTableColumn
h3cDhcpServer2DefOptGrpStatus=_H3cDhcpServer2DefOptGrpStatus_Object((1,3,6,1,4,1,2011,10,2,122,2,15,1,3),_H3cDhcpServer2DefOptGrpStatus_Type())
h3cDhcpServer2DefOptGrpStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDhcpServer2DefOptGrpStatus.setStatus(_A)
_H3cDhcpServer2ValidClassTable_Object=MibTable
h3cDhcpServer2ValidClassTable=_H3cDhcpServer2ValidClassTable_Object((1,3,6,1,4,1,2011,10,2,122,2,16))
if mibBuilder.loadTexts:h3cDhcpServer2ValidClassTable.setStatus(_A)
_H3cDhcpServer2ValidClassEntry_Object=MibTableRow
h3cDhcpServer2ValidClassEntry=_H3cDhcpServer2ValidClassEntry_Object((1,3,6,1,4,1,2011,10,2,122,2,16,1))
h3cDhcpServer2ValidClassEntry.setIndexNames((0,_D,_I),(0,_D,_l))
if mibBuilder.loadTexts:h3cDhcpServer2ValidClassEntry.setStatus(_A)
class _H3cDhcpServer2ValidClassName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,63))
_H3cDhcpServer2ValidClassName_Type.__name__=_E
_H3cDhcpServer2ValidClassName_Object=MibTableColumn
h3cDhcpServer2ValidClassName=_H3cDhcpServer2ValidClassName_Object((1,3,6,1,4,1,2011,10,2,122,2,16,1,1),_H3cDhcpServer2ValidClassName_Type())
h3cDhcpServer2ValidClassName.setMaxAccess(_H)
if mibBuilder.loadTexts:h3cDhcpServer2ValidClassName.setStatus(_A)
_H3cDhcpServer2ValidClassStatus_Type=RowStatus
_H3cDhcpServer2ValidClassStatus_Object=MibTableColumn
h3cDhcpServer2ValidClassStatus=_H3cDhcpServer2ValidClassStatus_Object((1,3,6,1,4,1,2011,10,2,122,2,16,1,2),_H3cDhcpServer2ValidClassStatus_Type())
h3cDhcpServer2ValidClassStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDhcpServer2ValidClassStatus.setStatus(_A)
_H3cDhcpServer2RuleHwAddrTable_Object=MibTable
h3cDhcpServer2RuleHwAddrTable=_H3cDhcpServer2RuleHwAddrTable_Object((1,3,6,1,4,1,2011,10,2,122,2,17))
if mibBuilder.loadTexts:h3cDhcpServer2RuleHwAddrTable.setStatus(_A)
_H3cDhcpServer2RuleHwAddrEntry_Object=MibTableRow
h3cDhcpServer2RuleHwAddrEntry=_H3cDhcpServer2RuleHwAddrEntry_Object((1,3,6,1,4,1,2011,10,2,122,2,17,1))
h3cDhcpServer2RuleHwAddrEntry.setIndexNames((0,_D,_Q),(0,_D,_m))
if mibBuilder.loadTexts:h3cDhcpServer2RuleHwAddrEntry.setStatus(_A)
class _H3cDhcpServer2RuleHwAddrNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_H3cDhcpServer2RuleHwAddrNumber_Type.__name__=_F
_H3cDhcpServer2RuleHwAddrNumber_Object=MibTableColumn
h3cDhcpServer2RuleHwAddrNumber=_H3cDhcpServer2RuleHwAddrNumber_Object((1,3,6,1,4,1,2011,10,2,122,2,17,1,1),_H3cDhcpServer2RuleHwAddrNumber_Type())
h3cDhcpServer2RuleHwAddrNumber.setMaxAccess(_H)
if mibBuilder.loadTexts:h3cDhcpServer2RuleHwAddrNumber.setStatus(_A)
class _H3cDhcpServer2RuleHwAddress_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,39))
_H3cDhcpServer2RuleHwAddress_Type.__name__=_E
_H3cDhcpServer2RuleHwAddress_Object=MibTableColumn
h3cDhcpServer2RuleHwAddress=_H3cDhcpServer2RuleHwAddress_Object((1,3,6,1,4,1,2011,10,2,122,2,17,1,2),_H3cDhcpServer2RuleHwAddress_Type())
h3cDhcpServer2RuleHwAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDhcpServer2RuleHwAddress.setStatus(_A)
class _H3cDhcpServer2RuleHwAddrMask_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,39))
_H3cDhcpServer2RuleHwAddrMask_Type.__name__=_E
_H3cDhcpServer2RuleHwAddrMask_Object=MibTableColumn
h3cDhcpServer2RuleHwAddrMask=_H3cDhcpServer2RuleHwAddrMask_Object((1,3,6,1,4,1,2011,10,2,122,2,17,1,3),_H3cDhcpServer2RuleHwAddrMask_Type())
h3cDhcpServer2RuleHwAddrMask.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDhcpServer2RuleHwAddrMask.setStatus(_A)
class _H3cDhcpServer2RuleHwAddrType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_H3cDhcpServer2RuleHwAddrType_Type.__name__=_F
_H3cDhcpServer2RuleHwAddrType_Object=MibTableColumn
h3cDhcpServer2RuleHwAddrType=_H3cDhcpServer2RuleHwAddrType_Object((1,3,6,1,4,1,2011,10,2,122,2,17,1,4),_H3cDhcpServer2RuleHwAddrType_Type())
h3cDhcpServer2RuleHwAddrType.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDhcpServer2RuleHwAddrType.setStatus(_A)
_H3cDhcpServer2RuleHwAddrStatus_Type=RowStatus
_H3cDhcpServer2RuleHwAddrStatus_Object=MibTableColumn
h3cDhcpServer2RuleHwAddrStatus=_H3cDhcpServer2RuleHwAddrStatus_Object((1,3,6,1,4,1,2011,10,2,122,2,17,1,5),_H3cDhcpServer2RuleHwAddrStatus_Type())
h3cDhcpServer2RuleHwAddrStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDhcpServer2RuleHwAddrStatus.setStatus(_A)
_H3cDhcpServer2OptionGroupTable_Object=MibTable
h3cDhcpServer2OptionGroupTable=_H3cDhcpServer2OptionGroupTable_Object((1,3,6,1,4,1,2011,10,2,122,2,18))
if mibBuilder.loadTexts:h3cDhcpServer2OptionGroupTable.setStatus(_A)
_H3cDhcpServer2OptionGroupEntry_Object=MibTableRow
h3cDhcpServer2OptionGroupEntry=_H3cDhcpServer2OptionGroupEntry_Object((1,3,6,1,4,1,2011,10,2,122,2,18,1))
h3cDhcpServer2OptionGroupEntry.setIndexNames((0,_D,_R))
if mibBuilder.loadTexts:h3cDhcpServer2OptionGroupEntry.setStatus(_A)
class _H3cDhcpServer2OptionGroupId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32768))
_H3cDhcpServer2OptionGroupId_Type.__name__=_F
_H3cDhcpServer2OptionGroupId_Object=MibTableColumn
h3cDhcpServer2OptionGroupId=_H3cDhcpServer2OptionGroupId_Object((1,3,6,1,4,1,2011,10,2,122,2,18,1,1),_H3cDhcpServer2OptionGroupId_Type())
h3cDhcpServer2OptionGroupId.setMaxAccess(_H)
if mibBuilder.loadTexts:h3cDhcpServer2OptionGroupId.setStatus(_A)
_H3cDhcpServer2OptionGroupStatus_Type=RowStatus
_H3cDhcpServer2OptionGroupStatus_Object=MibTableColumn
h3cDhcpServer2OptionGroupStatus=_H3cDhcpServer2OptionGroupStatus_Object((1,3,6,1,4,1,2011,10,2,122,2,18,1,2),_H3cDhcpServer2OptionGroupStatus_Type())
h3cDhcpServer2OptionGroupStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDhcpServer2OptionGroupStatus.setStatus(_A)
_H3cDhcpServer2OptionTable_Object=MibTable
h3cDhcpServer2OptionTable=_H3cDhcpServer2OptionTable_Object((1,3,6,1,4,1,2011,10,2,122,2,19))
if mibBuilder.loadTexts:h3cDhcpServer2OptionTable.setStatus(_A)
_H3cDhcpServer2OptionEntry_Object=MibTableRow
h3cDhcpServer2OptionEntry=_H3cDhcpServer2OptionEntry_Object((1,3,6,1,4,1,2011,10,2,122,2,19,1))
h3cDhcpServer2OptionEntry.setIndexNames((0,_D,_R),(0,_D,_n))
if mibBuilder.loadTexts:h3cDhcpServer2OptionEntry.setStatus(_A)
class _H3cDhcpServer2OptionCode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,254))
_H3cDhcpServer2OptionCode_Type.__name__=_F
_H3cDhcpServer2OptionCode_Object=MibTableColumn
h3cDhcpServer2OptionCode=_H3cDhcpServer2OptionCode_Object((1,3,6,1,4,1,2011,10,2,122,2,19,1,1),_H3cDhcpServer2OptionCode_Type())
h3cDhcpServer2OptionCode.setMaxAccess(_H)
if mibBuilder.loadTexts:h3cDhcpServer2OptionCode.setStatus(_A)
class _H3cDhcpServer2OptionType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_O,1),(_P,2),('ip',3)))
_H3cDhcpServer2OptionType_Type.__name__=_F
_H3cDhcpServer2OptionType_Object=MibTableColumn
h3cDhcpServer2OptionType=_H3cDhcpServer2OptionType_Object((1,3,6,1,4,1,2011,10,2,122,2,19,1,2),_H3cDhcpServer2OptionType_Type())
h3cDhcpServer2OptionType.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDhcpServer2OptionType.setStatus(_A)
class _H3cDhcpServer2OptionAscii_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_H3cDhcpServer2OptionAscii_Type.__name__=_E
_H3cDhcpServer2OptionAscii_Object=MibTableColumn
h3cDhcpServer2OptionAscii=_H3cDhcpServer2OptionAscii_Object((1,3,6,1,4,1,2011,10,2,122,2,19,1,3),_H3cDhcpServer2OptionAscii_Type())
h3cDhcpServer2OptionAscii.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDhcpServer2OptionAscii.setStatus(_A)
class _H3cDhcpServer2OptionHexStr_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,510))
_H3cDhcpServer2OptionHexStr_Type.__name__=_E
_H3cDhcpServer2OptionHexStr_Object=MibTableColumn
h3cDhcpServer2OptionHexStr=_H3cDhcpServer2OptionHexStr_Object((1,3,6,1,4,1,2011,10,2,122,2,19,1,4),_H3cDhcpServer2OptionHexStr_Type())
h3cDhcpServer2OptionHexStr.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDhcpServer2OptionHexStr.setStatus(_A)
class _H3cDhcpServer2OptionIPStr_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_H3cDhcpServer2OptionIPStr_Type.__name__=_E
_H3cDhcpServer2OptionIPStr_Object=MibTableColumn
h3cDhcpServer2OptionIPStr=_H3cDhcpServer2OptionIPStr_Object((1,3,6,1,4,1,2011,10,2,122,2,19,1,5),_H3cDhcpServer2OptionIPStr_Type())
h3cDhcpServer2OptionIPStr.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDhcpServer2OptionIPStr.setStatus(_A)
_H3cDhcpServer2OptionRowStatus_Type=RowStatus
_H3cDhcpServer2OptionRowStatus_Object=MibTableColumn
h3cDhcpServer2OptionRowStatus=_H3cDhcpServer2OptionRowStatus_Object((1,3,6,1,4,1,2011,10,2,122,2,19,1,6),_H3cDhcpServer2OptionRowStatus_Type())
h3cDhcpServer2OptionRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDhcpServer2OptionRowStatus.setStatus(_A)
_H3cDhcpServer2PoolStatTable_Object=MibTable
h3cDhcpServer2PoolStatTable=_H3cDhcpServer2PoolStatTable_Object((1,3,6,1,4,1,2011,10,2,122,2,20))
if mibBuilder.loadTexts:h3cDhcpServer2PoolStatTable.setStatus(_A)
_H3cDhcpServer2PoolStatEntry_Object=MibTableRow
h3cDhcpServer2PoolStatEntry=_H3cDhcpServer2PoolStatEntry_Object((1,3,6,1,4,1,2011,10,2,122,2,20,1))
h3cDhcpServer2PoolStatEntry.setIndexNames((0,_D,_I))
if mibBuilder.loadTexts:h3cDhcpServer2PoolStatEntry.setStatus(_A)
class _H3cDhcpServer2PoolUsage_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_H3cDhcpServer2PoolUsage_Type.__name__=_K
_H3cDhcpServer2PoolUsage_Object=MibTableColumn
h3cDhcpServer2PoolUsage=_H3cDhcpServer2PoolUsage_Object((1,3,6,1,4,1,2011,10,2,122,2,20,1,1),_H3cDhcpServer2PoolUsage_Type())
h3cDhcpServer2PoolUsage.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cDhcpServer2PoolUsage.setStatus(_A)
_H3cDhcpServer2PoolReqCnt_Type=Counter64
_H3cDhcpServer2PoolReqCnt_Object=MibTableColumn
h3cDhcpServer2PoolReqCnt=_H3cDhcpServer2PoolReqCnt_Object((1,3,6,1,4,1,2011,10,2,122,2,20,1,2),_H3cDhcpServer2PoolReqCnt_Type())
h3cDhcpServer2PoolReqCnt.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cDhcpServer2PoolReqCnt.setStatus(_A)
_H3cDhcpServer2PoolReqSuccCnt_Type=Counter64
_H3cDhcpServer2PoolReqSuccCnt_Object=MibTableColumn
h3cDhcpServer2PoolReqSuccCnt=_H3cDhcpServer2PoolReqSuccCnt_Object((1,3,6,1,4,1,2011,10,2,122,2,20,1,3),_H3cDhcpServer2PoolReqSuccCnt_Type())
h3cDhcpServer2PoolReqSuccCnt.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cDhcpServer2PoolReqSuccCnt.setStatus(_A)
_H3cDhcpServer2PoolDiscoverCnt_Type=Counter64
_H3cDhcpServer2PoolDiscoverCnt_Object=MibTableColumn
h3cDhcpServer2PoolDiscoverCnt=_H3cDhcpServer2PoolDiscoverCnt_Object((1,3,6,1,4,1,2011,10,2,122,2,20,1,4),_H3cDhcpServer2PoolDiscoverCnt_Type())
h3cDhcpServer2PoolDiscoverCnt.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cDhcpServer2PoolDiscoverCnt.setStatus(_A)
_H3cDhcpServer2PoolOfferCnt_Type=Counter64
_H3cDhcpServer2PoolOfferCnt_Object=MibTableColumn
h3cDhcpServer2PoolOfferCnt=_H3cDhcpServer2PoolOfferCnt_Object((1,3,6,1,4,1,2011,10,2,122,2,20,1,5),_H3cDhcpServer2PoolOfferCnt_Type())
h3cDhcpServer2PoolOfferCnt.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cDhcpServer2PoolOfferCnt.setStatus(_A)
_H3cDhcpServer2PoolAckCnt_Type=Counter64
_H3cDhcpServer2PoolAckCnt_Object=MibTableColumn
h3cDhcpServer2PoolAckCnt=_H3cDhcpServer2PoolAckCnt_Object((1,3,6,1,4,1,2011,10,2,122,2,20,1,6),_H3cDhcpServer2PoolAckCnt_Type())
h3cDhcpServer2PoolAckCnt.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cDhcpServer2PoolAckCnt.setStatus(_A)
_H3cDhcpServer2PoolIPTotalNum_Type=Unsigned32
_H3cDhcpServer2PoolIPTotalNum_Object=MibTableColumn
h3cDhcpServer2PoolIPTotalNum=_H3cDhcpServer2PoolIPTotalNum_Object((1,3,6,1,4,1,2011,10,2,122,2,20,1,7),_H3cDhcpServer2PoolIPTotalNum_Type())
h3cDhcpServer2PoolIPTotalNum.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cDhcpServer2PoolIPTotalNum.setStatus(_A)
_H3cDhcpServer2PoolIPUsedNum_Type=Unsigned32
_H3cDhcpServer2PoolIPUsedNum_Object=MibTableColumn
h3cDhcpServer2PoolIPUsedNum=_H3cDhcpServer2PoolIPUsedNum_Object((1,3,6,1,4,1,2011,10,2,122,2,20,1,8),_H3cDhcpServer2PoolIPUsedNum_Type())
h3cDhcpServer2PoolIPUsedNum.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cDhcpServer2PoolIPUsedNum.setStatus(_A)
_H3cDhcpServer2PoolIPIdleNum_Type=Unsigned32
_H3cDhcpServer2PoolIPIdleNum_Object=MibTableColumn
h3cDhcpServer2PoolIPIdleNum=_H3cDhcpServer2PoolIPIdleNum_Object((1,3,6,1,4,1,2011,10,2,122,2,20,1,9),_H3cDhcpServer2PoolIPIdleNum_Type())
h3cDhcpServer2PoolIPIdleNum.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cDhcpServer2PoolIPIdleNum.setStatus(_A)
_H3cDhcpServer2PoolIPExcludeNum_Type=Unsigned32
_H3cDhcpServer2PoolIPExcludeNum_Object=MibTableColumn
h3cDhcpServer2PoolIPExcludeNum=_H3cDhcpServer2PoolIPExcludeNum_Object((1,3,6,1,4,1,2011,10,2,122,2,20,1,10),_H3cDhcpServer2PoolIPExcludeNum_Type())
h3cDhcpServer2PoolIPExcludeNum.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cDhcpServer2PoolIPExcludeNum.setStatus(_A)
_H3cDhcpServer2PoolConflictNum_Type=Unsigned32
_H3cDhcpServer2PoolConflictNum_Object=MibTableColumn
h3cDhcpServer2PoolConflictNum=_H3cDhcpServer2PoolConflictNum_Object((1,3,6,1,4,1,2011,10,2,122,2,20,1,11),_H3cDhcpServer2PoolConflictNum_Type())
h3cDhcpServer2PoolConflictNum.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cDhcpServer2PoolConflictNum.setStatus(_A)
_H3cDhcpServer2PoolAutoBindNum_Type=Unsigned32
_H3cDhcpServer2PoolAutoBindNum_Object=MibTableColumn
h3cDhcpServer2PoolAutoBindNum=_H3cDhcpServer2PoolAutoBindNum_Object((1,3,6,1,4,1,2011,10,2,122,2,20,1,12),_H3cDhcpServer2PoolAutoBindNum_Type())
h3cDhcpServer2PoolAutoBindNum.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cDhcpServer2PoolAutoBindNum.setStatus(_A)
_H3cDhcpServer2PoolManualBindNum_Type=Unsigned32
_H3cDhcpServer2PoolManualBindNum_Object=MibTableColumn
h3cDhcpServer2PoolManualBindNum=_H3cDhcpServer2PoolManualBindNum_Object((1,3,6,1,4,1,2011,10,2,122,2,20,1,13),_H3cDhcpServer2PoolManualBindNum_Type())
h3cDhcpServer2PoolManualBindNum.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cDhcpServer2PoolManualBindNum.setStatus(_A)
_H3cDhcpServer2PoolExpiredBindNum_Type=Unsigned32
_H3cDhcpServer2PoolExpiredBindNum_Object=MibTableColumn
h3cDhcpServer2PoolExpiredBindNum=_H3cDhcpServer2PoolExpiredBindNum_Object((1,3,6,1,4,1,2011,10,2,122,2,20,1,14),_H3cDhcpServer2PoolExpiredBindNum_Type())
h3cDhcpServer2PoolExpiredBindNum.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cDhcpServer2PoolExpiredBindNum.setStatus(_A)
class _H3cDhcpServer2PoolNameInfo_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,63))
_H3cDhcpServer2PoolNameInfo_Type.__name__=_E
_H3cDhcpServer2PoolNameInfo_Object=MibTableColumn
h3cDhcpServer2PoolNameInfo=_H3cDhcpServer2PoolNameInfo_Object((1,3,6,1,4,1,2011,10,2,122,2,20,1,15),_H3cDhcpServer2PoolNameInfo_Type())
h3cDhcpServer2PoolNameInfo.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDhcpServer2PoolNameInfo.setStatus(_A)
_H3cDhcpRelay2ScalarObjects_ObjectIdentity=ObjectIdentity
h3cDhcpRelay2ScalarObjects=_H3cDhcpRelay2ScalarObjects_ObjectIdentity((1,3,6,1,4,1,2011,10,2,122,3))
_H3cDhcpRelay2ConfigGroup_ObjectIdentity=ObjectIdentity
h3cDhcpRelay2ConfigGroup=_H3cDhcpRelay2ConfigGroup_ObjectIdentity((1,3,6,1,4,1,2011,10,2,122,3,1))
class _H3cDhcpRelay2UserInfoRecord_Type(TruthValue):defaultValue=2
_H3cDhcpRelay2UserInfoRecord_Type.__name__=_J
_H3cDhcpRelay2UserInfoRecord_Object=MibScalar
h3cDhcpRelay2UserInfoRecord=_H3cDhcpRelay2UserInfoRecord_Object((1,3,6,1,4,1,2011,10,2,122,3,1,1),_H3cDhcpRelay2UserInfoRecord_Type())
h3cDhcpRelay2UserInfoRecord.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cDhcpRelay2UserInfoRecord.setStatus(_A)
class _H3cDhcpRelay2UserInfoRefresh_Type(TruthValue):defaultValue=1
_H3cDhcpRelay2UserInfoRefresh_Type.__name__=_J
_H3cDhcpRelay2UserInfoRefresh_Object=MibScalar
h3cDhcpRelay2UserInfoRefresh=_H3cDhcpRelay2UserInfoRefresh_Object((1,3,6,1,4,1,2011,10,2,122,3,1,2),_H3cDhcpRelay2UserInfoRefresh_Type())
h3cDhcpRelay2UserInfoRefresh.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cDhcpRelay2UserInfoRefresh.setStatus(_A)
class _H3cDhcpRelay2UserInfoFlushTime_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,120))
_H3cDhcpRelay2UserInfoFlushTime_Type.__name__=_K
_H3cDhcpRelay2UserInfoFlushTime_Object=MibScalar
h3cDhcpRelay2UserInfoFlushTime=_H3cDhcpRelay2UserInfoFlushTime_Object((1,3,6,1,4,1,2011,10,2,122,3,1,3),_H3cDhcpRelay2UserInfoFlushTime_Type())
h3cDhcpRelay2UserInfoFlushTime.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cDhcpRelay2UserInfoFlushTime.setStatus(_A)
class _H3cDhcpRelay2ReleaseAddr_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,47))
_H3cDhcpRelay2ReleaseAddr_Type.__name__=_E
_H3cDhcpRelay2ReleaseAddr_Object=MibScalar
h3cDhcpRelay2ReleaseAddr=_H3cDhcpRelay2ReleaseAddr_Object((1,3,6,1,4,1,2011,10,2,122,3,1,4),_H3cDhcpRelay2ReleaseAddr_Type())
h3cDhcpRelay2ReleaseAddr.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cDhcpRelay2ReleaseAddr.setStatus(_A)
_H3cDhcpRelay2StatisticsGroup_ObjectIdentity=ObjectIdentity
h3cDhcpRelay2StatisticsGroup=_H3cDhcpRelay2StatisticsGroup_ObjectIdentity((1,3,6,1,4,1,2011,10,2,122,3,2))
_H3cDhcpRelay2RxClientNum_Type=Counter64
_H3cDhcpRelay2RxClientNum_Object=MibScalar
h3cDhcpRelay2RxClientNum=_H3cDhcpRelay2RxClientNum_Object((1,3,6,1,4,1,2011,10,2,122,3,2,1),_H3cDhcpRelay2RxClientNum_Type())
h3cDhcpRelay2RxClientNum.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cDhcpRelay2RxClientNum.setStatus(_A)
_H3cDhcpRelay2TxClientNum_Type=Counter64
_H3cDhcpRelay2TxClientNum_Object=MibScalar
h3cDhcpRelay2TxClientNum=_H3cDhcpRelay2TxClientNum_Object((1,3,6,1,4,1,2011,10,2,122,3,2,2),_H3cDhcpRelay2TxClientNum_Type())
h3cDhcpRelay2TxClientNum.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cDhcpRelay2TxClientNum.setStatus(_A)
_H3cDhcpRelay2RxServerNum_Type=Counter64
_H3cDhcpRelay2RxServerNum_Object=MibScalar
h3cDhcpRelay2RxServerNum=_H3cDhcpRelay2RxServerNum_Object((1,3,6,1,4,1,2011,10,2,122,3,2,3),_H3cDhcpRelay2RxServerNum_Type())
h3cDhcpRelay2RxServerNum.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cDhcpRelay2RxServerNum.setStatus(_A)
_H3cDhcpRelay2TxServerNum_Type=Counter64
_H3cDhcpRelay2TxServerNum_Object=MibScalar
h3cDhcpRelay2TxServerNum=_H3cDhcpRelay2TxServerNum_Object((1,3,6,1,4,1,2011,10,2,122,3,2,4),_H3cDhcpRelay2TxServerNum_Type())
h3cDhcpRelay2TxServerNum.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cDhcpRelay2TxServerNum.setStatus(_A)
_H3cDhcpRelay2BadNum_Type=Counter64
_H3cDhcpRelay2BadNum_Object=MibScalar
h3cDhcpRelay2BadNum=_H3cDhcpRelay2BadNum_Object((1,3,6,1,4,1,2011,10,2,122,3,2,5),_H3cDhcpRelay2BadNum_Type())
h3cDhcpRelay2BadNum.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cDhcpRelay2BadNum.setStatus(_A)
_H3cDhcpRelay2BootpRequestNum_Type=Counter64
_H3cDhcpRelay2BootpRequestNum_Object=MibScalar
h3cDhcpRelay2BootpRequestNum=_H3cDhcpRelay2BootpRequestNum_Object((1,3,6,1,4,1,2011,10,2,122,3,2,6),_H3cDhcpRelay2BootpRequestNum_Type())
h3cDhcpRelay2BootpRequestNum.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cDhcpRelay2BootpRequestNum.setStatus(_A)
_H3cDhcpRelay2DiscoverNum_Type=Counter64
_H3cDhcpRelay2DiscoverNum_Object=MibScalar
h3cDhcpRelay2DiscoverNum=_H3cDhcpRelay2DiscoverNum_Object((1,3,6,1,4,1,2011,10,2,122,3,2,7),_H3cDhcpRelay2DiscoverNum_Type())
h3cDhcpRelay2DiscoverNum.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cDhcpRelay2DiscoverNum.setStatus(_A)
_H3cDhcpRelay2RequestNum_Type=Counter64
_H3cDhcpRelay2RequestNum_Object=MibScalar
h3cDhcpRelay2RequestNum=_H3cDhcpRelay2RequestNum_Object((1,3,6,1,4,1,2011,10,2,122,3,2,8),_H3cDhcpRelay2RequestNum_Type())
h3cDhcpRelay2RequestNum.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cDhcpRelay2RequestNum.setStatus(_A)
_H3cDhcpRelay2DeclineNum_Type=Counter64
_H3cDhcpRelay2DeclineNum_Object=MibScalar
h3cDhcpRelay2DeclineNum=_H3cDhcpRelay2DeclineNum_Object((1,3,6,1,4,1,2011,10,2,122,3,2,9),_H3cDhcpRelay2DeclineNum_Type())
h3cDhcpRelay2DeclineNum.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cDhcpRelay2DeclineNum.setStatus(_A)
_H3cDhcpRelay2ReleaseNum_Type=Counter64
_H3cDhcpRelay2ReleaseNum_Object=MibScalar
h3cDhcpRelay2ReleaseNum=_H3cDhcpRelay2ReleaseNum_Object((1,3,6,1,4,1,2011,10,2,122,3,2,10),_H3cDhcpRelay2ReleaseNum_Type())
h3cDhcpRelay2ReleaseNum.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cDhcpRelay2ReleaseNum.setStatus(_A)
_H3cDhcpRelay2InformNum_Type=Counter64
_H3cDhcpRelay2InformNum_Object=MibScalar
h3cDhcpRelay2InformNum=_H3cDhcpRelay2InformNum_Object((1,3,6,1,4,1,2011,10,2,122,3,2,11),_H3cDhcpRelay2InformNum_Type())
h3cDhcpRelay2InformNum.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cDhcpRelay2InformNum.setStatus(_A)
_H3cDhcpRelay2BootpReplyNum_Type=Counter64
_H3cDhcpRelay2BootpReplyNum_Object=MibScalar
h3cDhcpRelay2BootpReplyNum=_H3cDhcpRelay2BootpReplyNum_Object((1,3,6,1,4,1,2011,10,2,122,3,2,12),_H3cDhcpRelay2BootpReplyNum_Type())
h3cDhcpRelay2BootpReplyNum.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cDhcpRelay2BootpReplyNum.setStatus(_A)
_H3cDhcpRelay2OfferNum_Type=Counter64
_H3cDhcpRelay2OfferNum_Object=MibScalar
h3cDhcpRelay2OfferNum=_H3cDhcpRelay2OfferNum_Object((1,3,6,1,4,1,2011,10,2,122,3,2,13),_H3cDhcpRelay2OfferNum_Type())
h3cDhcpRelay2OfferNum.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cDhcpRelay2OfferNum.setStatus(_A)
_H3cDhcpRelay2AckNum_Type=Counter64
_H3cDhcpRelay2AckNum_Object=MibScalar
h3cDhcpRelay2AckNum=_H3cDhcpRelay2AckNum_Object((1,3,6,1,4,1,2011,10,2,122,3,2,14),_H3cDhcpRelay2AckNum_Type())
h3cDhcpRelay2AckNum.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cDhcpRelay2AckNum.setStatus(_A)
_H3cDhcpRelay2NakNum_Type=Counter64
_H3cDhcpRelay2NakNum_Object=MibScalar
h3cDhcpRelay2NakNum=_H3cDhcpRelay2NakNum_Object((1,3,6,1,4,1,2011,10,2,122,3,2,15),_H3cDhcpRelay2NakNum_Type())
h3cDhcpRelay2NakNum.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cDhcpRelay2NakNum.setStatus(_A)
_H3cDhcpRelay2Tables_ObjectIdentity=ObjectIdentity
h3cDhcpRelay2Tables=_H3cDhcpRelay2Tables_ObjectIdentity((1,3,6,1,4,1,2011,10,2,122,4))
_H3cDhcpRelay2IfConfigTable_Object=MibTable
h3cDhcpRelay2IfConfigTable=_H3cDhcpRelay2IfConfigTable_Object((1,3,6,1,4,1,2011,10,2,122,4,1))
if mibBuilder.loadTexts:h3cDhcpRelay2IfConfigTable.setStatus(_A)
_H3cDhcpRelay2IfConfigEntry_Object=MibTableRow
h3cDhcpRelay2IfConfigEntry=_H3cDhcpRelay2IfConfigEntry_Object((1,3,6,1,4,1,2011,10,2,122,4,1,1))
h3cDhcpRelay2IfConfigEntry.setIndexNames((0,_M,_N))
if mibBuilder.loadTexts:h3cDhcpRelay2IfConfigEntry.setStatus(_A)
class _H3cDhcpRelay2IfSelectRelay_Type(TruthValue):defaultValue=2
_H3cDhcpRelay2IfSelectRelay_Type.__name__=_J
_H3cDhcpRelay2IfSelectRelay_Object=MibTableColumn
h3cDhcpRelay2IfSelectRelay=_H3cDhcpRelay2IfSelectRelay_Object((1,3,6,1,4,1,2011,10,2,122,4,1,1,1),_H3cDhcpRelay2IfSelectRelay_Type())
h3cDhcpRelay2IfSelectRelay.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cDhcpRelay2IfSelectRelay.setStatus(_A)
class _H3cDhcpRelay2IfCheckMac_Type(TruthValue):defaultValue=2
_H3cDhcpRelay2IfCheckMac_Type.__name__=_J
_H3cDhcpRelay2IfCheckMac_Object=MibTableColumn
h3cDhcpRelay2IfCheckMac=_H3cDhcpRelay2IfCheckMac_Object((1,3,6,1,4,1,2011,10,2,122,4,1,1,2),_H3cDhcpRelay2IfCheckMac_Type())
h3cDhcpRelay2IfCheckMac.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cDhcpRelay2IfCheckMac.setStatus(_A)
class _H3cDhcpRelay2IfOpt82Enable_Type(TruthValue):defaultValue=2
_H3cDhcpRelay2IfOpt82Enable_Type.__name__=_J
_H3cDhcpRelay2IfOpt82Enable_Object=MibTableColumn
h3cDhcpRelay2IfOpt82Enable=_H3cDhcpRelay2IfOpt82Enable_Object((1,3,6,1,4,1,2011,10,2,122,4,1,1,3),_H3cDhcpRelay2IfOpt82Enable_Type())
h3cDhcpRelay2IfOpt82Enable.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cDhcpRelay2IfOpt82Enable.setStatus(_A)
class _H3cDhcpRelay2IfOpt82Strategy_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('drop',1),('keep',2),('replace',3)))
_H3cDhcpRelay2IfOpt82Strategy_Type.__name__=_F
_H3cDhcpRelay2IfOpt82Strategy_Object=MibTableColumn
h3cDhcpRelay2IfOpt82Strategy=_H3cDhcpRelay2IfOpt82Strategy_Object((1,3,6,1,4,1,2011,10,2,122,4,1,1,4),_H3cDhcpRelay2IfOpt82Strategy_Type())
h3cDhcpRelay2IfOpt82Strategy.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cDhcpRelay2IfOpt82Strategy.setStatus(_A)
class _H3cDhcpRelay2IfOpt82CIDMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_o,1),('verbose',2),(_S,3)))
_H3cDhcpRelay2IfOpt82CIDMode_Type.__name__=_F
_H3cDhcpRelay2IfOpt82CIDMode_Object=MibTableColumn
h3cDhcpRelay2IfOpt82CIDMode=_H3cDhcpRelay2IfOpt82CIDMode_Object((1,3,6,1,4,1,2011,10,2,122,4,1,1,5),_H3cDhcpRelay2IfOpt82CIDMode_Type())
h3cDhcpRelay2IfOpt82CIDMode.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cDhcpRelay2IfOpt82CIDMode.setStatus(_A)
class _H3cDhcpRelay2IfOpt82CIDNodeType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('invalid',1),('mac',2),(_p,3),(_S,4)))
_H3cDhcpRelay2IfOpt82CIDNodeType_Type.__name__=_F
_H3cDhcpRelay2IfOpt82CIDNodeType_Object=MibTableColumn
h3cDhcpRelay2IfOpt82CIDNodeType=_H3cDhcpRelay2IfOpt82CIDNodeType_Object((1,3,6,1,4,1,2011,10,2,122,4,1,1,6),_H3cDhcpRelay2IfOpt82CIDNodeType_Type())
h3cDhcpRelay2IfOpt82CIDNodeType.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cDhcpRelay2IfOpt82CIDNodeType.setStatus(_A)
class _H3cDhcpRelay2IfOpt82CIDNodeStr_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,50))
_H3cDhcpRelay2IfOpt82CIDNodeStr_Type.__name__=_E
_H3cDhcpRelay2IfOpt82CIDNodeStr_Object=MibTableColumn
h3cDhcpRelay2IfOpt82CIDNodeStr=_H3cDhcpRelay2IfOpt82CIDNodeStr_Object((1,3,6,1,4,1,2011,10,2,122,4,1,1,7),_H3cDhcpRelay2IfOpt82CIDNodeStr_Type())
h3cDhcpRelay2IfOpt82CIDNodeStr.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cDhcpRelay2IfOpt82CIDNodeStr.setStatus(_A)
class _H3cDhcpRelay2IfOpt82CIDStr_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,0),ValueSizeConstraint(3,63))
_H3cDhcpRelay2IfOpt82CIDStr_Type.__name__=_E
_H3cDhcpRelay2IfOpt82CIDStr_Object=MibTableColumn
h3cDhcpRelay2IfOpt82CIDStr=_H3cDhcpRelay2IfOpt82CIDStr_Object((1,3,6,1,4,1,2011,10,2,122,4,1,1,8),_H3cDhcpRelay2IfOpt82CIDStr_Type())
h3cDhcpRelay2IfOpt82CIDStr.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cDhcpRelay2IfOpt82CIDStr.setStatus(_A)
class _H3cDhcpRelay2IfOpt82CIDFormat_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_P,1),(_O,2),('undefine',3)))
_H3cDhcpRelay2IfOpt82CIDFormat_Type.__name__=_F
_H3cDhcpRelay2IfOpt82CIDFormat_Object=MibTableColumn
h3cDhcpRelay2IfOpt82CIDFormat=_H3cDhcpRelay2IfOpt82CIDFormat_Object((1,3,6,1,4,1,2011,10,2,122,4,1,1,9),_H3cDhcpRelay2IfOpt82CIDFormat_Type())
h3cDhcpRelay2IfOpt82CIDFormat.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cDhcpRelay2IfOpt82CIDFormat.setStatus(_A)
class _H3cDhcpRelay2IfOpt82RIDMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_o,1),(_p,2),(_S,3)))
_H3cDhcpRelay2IfOpt82RIDMode_Type.__name__=_F
_H3cDhcpRelay2IfOpt82RIDMode_Object=MibTableColumn
h3cDhcpRelay2IfOpt82RIDMode=_H3cDhcpRelay2IfOpt82RIDMode_Object((1,3,6,1,4,1,2011,10,2,122,4,1,1,10),_H3cDhcpRelay2IfOpt82RIDMode_Type())
h3cDhcpRelay2IfOpt82RIDMode.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cDhcpRelay2IfOpt82RIDMode.setStatus(_A)
class _H3cDhcpRelay2IfOpt82RIDStr_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_H3cDhcpRelay2IfOpt82RIDStr_Type.__name__=_E
_H3cDhcpRelay2IfOpt82RIDStr_Object=MibTableColumn
h3cDhcpRelay2IfOpt82RIDStr=_H3cDhcpRelay2IfOpt82RIDStr_Object((1,3,6,1,4,1,2011,10,2,122,4,1,1,11),_H3cDhcpRelay2IfOpt82RIDStr_Type())
h3cDhcpRelay2IfOpt82RIDStr.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cDhcpRelay2IfOpt82RIDStr.setStatus(_A)
class _H3cDhcpRelay2IfOpt82RIDFormat_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_P,1),(_O,2)))
_H3cDhcpRelay2IfOpt82RIDFormat_Type.__name__=_F
_H3cDhcpRelay2IfOpt82RIDFormat_Object=MibTableColumn
h3cDhcpRelay2IfOpt82RIDFormat=_H3cDhcpRelay2IfOpt82RIDFormat_Object((1,3,6,1,4,1,2011,10,2,122,4,1,1,12),_H3cDhcpRelay2IfOpt82RIDFormat_Type())
h3cDhcpRelay2IfOpt82RIDFormat.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cDhcpRelay2IfOpt82RIDFormat.setStatus(_A)
_H3cDhcpRelay2SrvAddrTable_Object=MibTable
h3cDhcpRelay2SrvAddrTable=_H3cDhcpRelay2SrvAddrTable_Object((1,3,6,1,4,1,2011,10,2,122,4,2))
if mibBuilder.loadTexts:h3cDhcpRelay2SrvAddrTable.setStatus(_A)
_H3cDhcpRelay2SrvAddrEntry_Object=MibTableRow
h3cDhcpRelay2SrvAddrEntry=_H3cDhcpRelay2SrvAddrEntry_Object((1,3,6,1,4,1,2011,10,2,122,4,2,1))
h3cDhcpRelay2SrvAddrEntry.setIndexNames((0,_M,_N),(0,_D,_q))
if mibBuilder.loadTexts:h3cDhcpRelay2SrvAddrEntry.setStatus(_A)
_H3cDhcpRelay2SrvAddrIP_Type=InetAddressIPv4
_H3cDhcpRelay2SrvAddrIP_Object=MibTableColumn
h3cDhcpRelay2SrvAddrIP=_H3cDhcpRelay2SrvAddrIP_Object((1,3,6,1,4,1,2011,10,2,122,4,2,1,1),_H3cDhcpRelay2SrvAddrIP_Type())
h3cDhcpRelay2SrvAddrIP.setMaxAccess(_H)
if mibBuilder.loadTexts:h3cDhcpRelay2SrvAddrIP.setStatus(_A)
_H3cDhcpRelay2SrvAddrRowStatus_Type=RowStatus
_H3cDhcpRelay2SrvAddrRowStatus_Object=MibTableColumn
h3cDhcpRelay2SrvAddrRowStatus=_H3cDhcpRelay2SrvAddrRowStatus_Object((1,3,6,1,4,1,2011,10,2,122,4,2,1,2),_H3cDhcpRelay2SrvAddrRowStatus_Type())
h3cDhcpRelay2SrvAddrRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDhcpRelay2SrvAddrRowStatus.setStatus(_A)
_H3cDhcpRelay2UserInfoTable_Object=MibTable
h3cDhcpRelay2UserInfoTable=_H3cDhcpRelay2UserInfoTable_Object((1,3,6,1,4,1,2011,10,2,122,4,3))
if mibBuilder.loadTexts:h3cDhcpRelay2UserInfoTable.setStatus(_A)
_H3cDhcpRelay2UserInfoEntry_Object=MibTableRow
h3cDhcpRelay2UserInfoEntry=_H3cDhcpRelay2UserInfoEntry_Object((1,3,6,1,4,1,2011,10,2,122,4,3,1))
h3cDhcpRelay2UserInfoEntry.setIndexNames((0,_D,_r),(0,_D,_s))
if mibBuilder.loadTexts:h3cDhcpRelay2UserInfoEntry.setStatus(_A)
class _H3cDhcpRelay2UserInfoVpnIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65534))
_H3cDhcpRelay2UserInfoVpnIndex_Type.__name__=_K
_H3cDhcpRelay2UserInfoVpnIndex_Object=MibTableColumn
h3cDhcpRelay2UserInfoVpnIndex=_H3cDhcpRelay2UserInfoVpnIndex_Object((1,3,6,1,4,1,2011,10,2,122,4,3,1,1),_H3cDhcpRelay2UserInfoVpnIndex_Type())
h3cDhcpRelay2UserInfoVpnIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:h3cDhcpRelay2UserInfoVpnIndex.setStatus(_A)
_H3cDhcpRelay2UserInfoIpAddr_Type=InetAddressIPv4
_H3cDhcpRelay2UserInfoIpAddr_Object=MibTableColumn
h3cDhcpRelay2UserInfoIpAddr=_H3cDhcpRelay2UserInfoIpAddr_Object((1,3,6,1,4,1,2011,10,2,122,4,3,1,2),_H3cDhcpRelay2UserInfoIpAddr_Type())
h3cDhcpRelay2UserInfoIpAddr.setMaxAccess(_H)
if mibBuilder.loadTexts:h3cDhcpRelay2UserInfoIpAddr.setStatus(_A)
_H3cDhcpRelay2UserInfoMacAddr_Type=MacAddress
_H3cDhcpRelay2UserInfoMacAddr_Object=MibTableColumn
h3cDhcpRelay2UserInfoMacAddr=_H3cDhcpRelay2UserInfoMacAddr_Object((1,3,6,1,4,1,2011,10,2,122,4,3,1,3),_H3cDhcpRelay2UserInfoMacAddr_Type())
h3cDhcpRelay2UserInfoMacAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cDhcpRelay2UserInfoMacAddr.setStatus(_A)
_H3cDhcpRelay2UserInfoIfIndex_Type=InterfaceIndexOrZero
_H3cDhcpRelay2UserInfoIfIndex_Object=MibTableColumn
h3cDhcpRelay2UserInfoIfIndex=_H3cDhcpRelay2UserInfoIfIndex_Object((1,3,6,1,4,1,2011,10,2,122,4,3,1,4),_H3cDhcpRelay2UserInfoIfIndex_Type())
h3cDhcpRelay2UserInfoIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cDhcpRelay2UserInfoIfIndex.setStatus(_A)
_H3cDhcpRelay2UserInfoRowStatus_Type=RowStatus
_H3cDhcpRelay2UserInfoRowStatus_Object=MibTableColumn
h3cDhcpRelay2UserInfoRowStatus=_H3cDhcpRelay2UserInfoRowStatus_Object((1,3,6,1,4,1,2011,10,2,122,4,3,1,5),_H3cDhcpRelay2UserInfoRowStatus_Type())
h3cDhcpRelay2UserInfoRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDhcpRelay2UserInfoRowStatus.setStatus(_A)
_H3cDhcpServer2Traps_ObjectIdentity=ObjectIdentity
h3cDhcpServer2Traps=_H3cDhcpServer2Traps_ObjectIdentity((1,3,6,1,4,1,2011,10,2,122,5))
_H3cDhcpServer2TrapNotify_ObjectIdentity=ObjectIdentity
h3cDhcpServer2TrapNotify=_H3cDhcpServer2TrapNotify_ObjectIdentity((1,3,6,1,4,1,2011,10,2,122,5,0))
h3cDhcpServer2AddrExhaust=NotificationType((1,3,6,1,4,1,2011,10,2,122,5,0,1))
h3cDhcpServer2AddrExhaust.setObjects(*((_D,_I),(_D,_L)))
if mibBuilder.loadTexts:h3cDhcpServer2AddrExhaust.setStatus(_A)
h3cDhcpServer2AddrExhaustRecov=NotificationType((1,3,6,1,4,1,2011,10,2,122,5,0,2))
h3cDhcpServer2AddrExhaustRecov.setObjects(*((_D,_I),(_D,_L)))
if mibBuilder.loadTexts:h3cDhcpServer2AddrExhaustRecov.setStatus(_A)
h3cDhcpServer2IpUsageOverflow=NotificationType((1,3,6,1,4,1,2011,10,2,122,5,0,3))
h3cDhcpServer2IpUsageOverflow.setObjects(*((_D,_I),(_D,_L)))
if mibBuilder.loadTexts:h3cDhcpServer2IpUsageOverflow.setStatus(_A)
h3cDhcpServer2AllocOverflow=NotificationType((1,3,6,1,4,1,2011,10,2,122,5,0,4))
if mibBuilder.loadTexts:h3cDhcpServer2AllocOverflow.setStatus(_A)
h3cDhcpServer2IpUsageOverflowRecov=NotificationType((1,3,6,1,4,1,2011,10,2,122,5,0,5))
h3cDhcpServer2IpUsageOverflowRecov.setObjects(*((_D,_I),(_D,_L)))
if mibBuilder.loadTexts:h3cDhcpServer2IpUsageOverflowRecov.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'h3cDhcp4':h3cDhcp4,'h3cDhcpServer2ScalarObjects':h3cDhcpServer2ScalarObjects,'h3cDhcpServer2ConfigGroup':h3cDhcpServer2ConfigGroup,'h3cDhcpServer2Enabled':h3cDhcpServer2Enabled,'h3cDhcpServer2AlwaysBroadcast':h3cDhcpServer2AlwaysBroadcast,'h3cDhcpServer2IgnoreBootp':h3cDhcpServer2IgnoreBootp,'h3cDhcpServer2BootpReplyRfc1048':h3cDhcpServer2BootpReplyRfc1048,'h3cDhcpServer2Opt82Enabled':h3cDhcpServer2Opt82Enabled,'h3cDhcpServer2PingNumber':h3cDhcpServer2PingNumber,'h3cDhcpServer2PingTimeout':h3cDhcpServer2PingTimeout,'h3cDhcpServer2AllocThreshold':h3cDhcpServer2AllocThreshold,'h3cDhcpServer2StatGroup':h3cDhcpServer2StatGroup,'h3cDhcpServer2BadNum':h3cDhcpServer2BadNum,'h3cDhcpServer2BootpRequestNum':h3cDhcpServer2BootpRequestNum,'h3cDhcpServer2DiscoverNum':h3cDhcpServer2DiscoverNum,'h3cDhcpServer2RequestNum':h3cDhcpServer2RequestNum,'h3cDhcpServer2DeclineNum':h3cDhcpServer2DeclineNum,'h3cDhcpServer2ReleaseNum':h3cDhcpServer2ReleaseNum,'h3cDhcpServer2InformNum':h3cDhcpServer2InformNum,'h3cDhcpServer2BootpReplyNum':h3cDhcpServer2BootpReplyNum,'h3cDhcpServer2OfferNum':h3cDhcpServer2OfferNum,'h3cDhcpServer2AckNum':h3cDhcpServer2AckNum,'h3cDhcpServer2NakNum':h3cDhcpServer2NakNum,'h3cDhcpServer2TotalPoolUsage':h3cDhcpServer2TotalPoolUsage,'h3cDhcpServer2PoolNumber':h3cDhcpServer2PoolNumber,'h3cDhcpServer2ConflictNum':h3cDhcpServer2ConflictNum,'h3cDhcpServer2AutoBindNum':h3cDhcpServer2AutoBindNum,'h3cDhcpServer2ManualBindNum':h3cDhcpServer2ManualBindNum,'h3cDhcpServer2ExpiredBindNum':h3cDhcpServer2ExpiredBindNum,'h3cDhcpServer2ReqCnt':h3cDhcpServer2ReqCnt,'h3cDhcpServer2ReqSuccCnt':h3cDhcpServer2ReqSuccCnt,'h3cDhcpServer2IPTotalNum':h3cDhcpServer2IPTotalNum,'h3cDhcpServer2IPUsedNum':h3cDhcpServer2IPUsedNum,'h3cDhcpServer2IPIdleNum':h3cDhcpServer2IPIdleNum,'h3cDhcpServer2IPExcludeTotalNum':h3cDhcpServer2IPExcludeTotalNum,'h3cDhcpServer2Tables':h3cDhcpServer2Tables,'h3cDhcpServer2PoolTable':h3cDhcpServer2PoolTable,'h3cDhcpServer2PoolEntry':h3cDhcpServer2PoolEntry,_I:h3cDhcpServer2PoolIndex,_L:h3cDhcpServer2PoolName,'h3cDhcpServer2PoolVpnName':h3cDhcpServer2PoolVpnName,'h3cDhcpServer2PoolNetwork':h3cDhcpServer2PoolNetwork,'h3cDhcpServer2PoolNetworkMask':h3cDhcpServer2PoolNetworkMask,'h3cDhcpServer2PoolStartAddr':h3cDhcpServer2PoolStartAddr,'h3cDhcpServer2PoolEndAddr':h3cDhcpServer2PoolEndAddr,'h3cDhcpServer2PoolLeaseDay':h3cDhcpServer2PoolLeaseDay,'h3cDhcpServer2PoolLeaseHour':h3cDhcpServer2PoolLeaseHour,'h3cDhcpServer2PoolLeaseMinute':h3cDhcpServer2PoolLeaseMinute,'h3cDhcpServer2PoolLeaseSecond':h3cDhcpServer2PoolLeaseSecond,'h3cDhcpServer2PoolLeaseUnlimit':h3cDhcpServer2PoolLeaseUnlimit,'h3cDhcpServer2PoolLeaseTime':h3cDhcpServer2PoolLeaseTime,'h3cDhcpServer2PoolDomainName':h3cDhcpServer2PoolDomainName,'h3cDhcpServer2PoolGatewayIP':h3cDhcpServer2PoolGatewayIP,'h3cDhcpServer2PoolDNSIP':h3cDhcpServer2PoolDNSIP,'h3cDhcpServer2PoolPrimaryDNSIP':h3cDhcpServer2PoolPrimaryDNSIP,'h3cDhcpServer2PoolSecondDNSIP':h3cDhcpServer2PoolSecondDNSIP,'h3cDhcpServer2PoolNetbiosType':h3cDhcpServer2PoolNetbiosType,'h3cDhcpServer2PoolNbnsIP':h3cDhcpServer2PoolNbnsIP,'h3cDhcpServer2PoolBootFileName':h3cDhcpServer2PoolBootFileName,'h3cDhcpServer2PoolBimsIP':h3cDhcpServer2PoolBimsIP,'h3cDhcpServer2PoolBimsPort':h3cDhcpServer2PoolBimsPort,'h3cDhcpServer2PoolBimsKeyStr':h3cDhcpServer2PoolBimsKeyStr,'h3cDhcpServer2PoolNextServer':h3cDhcpServer2PoolNextServer,'h3cDhcpServer2PoolTftpDomName':h3cDhcpServer2PoolTftpDomName,'h3cDhcpServer2PoolTftpIP':h3cDhcpServer2PoolTftpIP,'h3cDhcpServer2PoolVoiceAsIP':h3cDhcpServer2PoolVoiceAsIP,'h3cDhcpServer2PoolVoiceFailIP':h3cDhcpServer2PoolVoiceFailIP,'h3cDhcpServer2PoolVoiceFailStr':h3cDhcpServer2PoolVoiceFailStr,'h3cDhcpServer2PoolVoiceNCPIP':h3cDhcpServer2PoolVoiceNCPIP,'h3cDhcpServer2PoolVoiceVlanId':h3cDhcpServer2PoolVoiceVlanId,'h3cDhcpServer2PoolVoiceVlanEnbl':h3cDhcpServer2PoolVoiceVlanEnbl,'h3cDhcpServer2PoolRowStatus':h3cDhcpServer2PoolRowStatus,'h3cDhcpServer2PoolVerifyClass':h3cDhcpServer2PoolVerifyClass,'h3cDhcpServer2PoolThreshold':h3cDhcpServer2PoolThreshold,'h3cDhcpServer2IfApplyPoolTable':h3cDhcpServer2IfApplyPoolTable,'h3cDhcpServer2IfApplyPoolEntry':h3cDhcpServer2IfApplyPoolEntry,'h3cDhcpServer2IfApplyPoolName':h3cDhcpServer2IfApplyPoolName,'h3cDhcpServer2PoolSecNwTable':h3cDhcpServer2PoolSecNwTable,'h3cDhcpServer2PoolSecNwEntry':h3cDhcpServer2PoolSecNwEntry,_T:h3cDhcpServer2PoolSecNw,_U:h3cDhcpServer2PoolSecNwMask,'h3cDhcpServer2PoolSecNwGwIP':h3cDhcpServer2PoolSecNwGwIP,'h3cDhcpServer2PoolSecNwStatus':h3cDhcpServer2PoolSecNwStatus,'h3cDhcpServer2PoolClassTable':h3cDhcpServer2PoolClassTable,'h3cDhcpServer2PoolClassEntry':h3cDhcpServer2PoolClassEntry,_V:h3cDhcpServer2PoolClassName,'h3cDhcpServer2PoolClassStart':h3cDhcpServer2PoolClassStart,'h3cDhcpServer2PoolClassEnd':h3cDhcpServer2PoolClassEnd,'h3cDhcpServer2PoolClassStatus':h3cDhcpServer2PoolClassStatus,'h3cDhcpServer2PoolStaticTable':h3cDhcpServer2PoolStaticTable,'h3cDhcpServer2PoolStaticEntry':h3cDhcpServer2PoolStaticEntry,_W:h3cDhcpServer2PoolStaticIP,'h3cDhcpServer2PoolStaticMask':h3cDhcpServer2PoolStaticMask,'h3cDhcpServer2PoolStaticCID':h3cDhcpServer2PoolStaticCID,'h3cDhcpServer2PoolStaticHAddr':h3cDhcpServer2PoolStaticHAddr,'h3cDhcpServer2PoolStaticHType':h3cDhcpServer2PoolStaticHType,'h3cDhcpServer2PoolStaticStatus':h3cDhcpServer2PoolStaticStatus,'h3cDhcpServer2PoolOptionTable':h3cDhcpServer2PoolOptionTable,'h3cDhcpServer2PoolOptionEntry':h3cDhcpServer2PoolOptionEntry,_a:h3cDhcpServer2PoolOptCode,'h3cDhcpServer2PoolOptType':h3cDhcpServer2PoolOptType,'h3cDhcpServer2PoolOptAscii':h3cDhcpServer2PoolOptAscii,'h3cDhcpServer2PoolOptHexStr':h3cDhcpServer2PoolOptHexStr,'h3cDhcpServer2PoolOptIPStr':h3cDhcpServer2PoolOptIPStr,'h3cDhcpServer2PoolOptRowStatus':h3cDhcpServer2PoolOptRowStatus,'h3cDhcpServer2PoolForbidTable':h3cDhcpServer2PoolForbidTable,'h3cDhcpServer2PoolForbidEntry':h3cDhcpServer2PoolForbidEntry,_b:h3cDhcpServer2PoolForbidIP,'h3cDhcpServer2PoolForbidStatus':h3cDhcpServer2PoolForbidStatus,'h3cDhcpServer2ClassTable':h3cDhcpServer2ClassTable,'h3cDhcpServer2ClassEntry':h3cDhcpServer2ClassEntry,_Q:h3cDhcpServer2ClassName,'h3cDhcpServer2ClassRowStatus':h3cDhcpServer2ClassRowStatus,'h3cDhcpServer2RuleTable':h3cDhcpServer2RuleTable,'h3cDhcpServer2RuleEntry':h3cDhcpServer2RuleEntry,_c:h3cDhcpServer2RuleNumber,'h3cDhcpServer2RuleOptCode':h3cDhcpServer2RuleOptCode,'h3cDhcpServer2RuleOptHexStr':h3cDhcpServer2RuleOptHexStr,'h3cDhcpServer2RuleOptMask':h3cDhcpServer2RuleOptMask,'h3cDhcpServer2RuleOptOffset':h3cDhcpServer2RuleOptOffset,'h3cDhcpServer2RuleOptLength':h3cDhcpServer2RuleOptLength,'h3cDhcpServer2RuleRowStatus':h3cDhcpServer2RuleRowStatus,'h3cDhcpServer2ForbidTable':h3cDhcpServer2ForbidTable,'h3cDhcpServer2ForbidEntry':h3cDhcpServer2ForbidEntry,_d:h3cDhcpServer2ForbidVpnName,_e:h3cDhcpServer2ForbidStart,_f:h3cDhcpServer2ForbidEnd,'h3cDhcpServer2ForbidRowStatus':h3cDhcpServer2ForbidRowStatus,'h3cDhcpServer2FreeTable':h3cDhcpServer2FreeTable,'h3cDhcpServer2FreeEntry':h3cDhcpServer2FreeEntry,_g:h3cDhcpServer2FreeStart,'h3cDhcpServer2FreeEnd':h3cDhcpServer2FreeEnd,'h3cDhcpServer2ConflictTable':h3cDhcpServer2ConflictTable,'h3cDhcpServer2ConflictEntry':h3cDhcpServer2ConflictEntry,_h:h3cDhcpServer2ConflictIP,'h3cDhcpServer2ConflictType':h3cDhcpServer2ConflictType,'h3cDhcpServer2ConflictTime':h3cDhcpServer2ConflictTime,'h3cDhcpServer2ConflictRowStatus':h3cDhcpServer2ConflictRowStatus,'h3cDhcpServer2ExpiredTable':h3cDhcpServer2ExpiredTable,'h3cDhcpServer2ExpiredEntry':h3cDhcpServer2ExpiredEntry,_i:h3cDhcpServer2ExpiredIP,'h3cDhcpServer2ExpiredClientId':h3cDhcpServer2ExpiredClientId,'h3cDhcpServer2ExpiredTime':h3cDhcpServer2ExpiredTime,'h3cDhcpServer2ExpiredRowStatus':h3cDhcpServer2ExpiredRowStatus,'h3cDhcpServer2IPInUseTable':h3cDhcpServer2IPInUseTable,'h3cDhcpServer2IPInUseEntry':h3cDhcpServer2IPInUseEntry,_j:h3cDhcpServer2IPInUseIP,'h3cDhcpServer2IPInUseClientId':h3cDhcpServer2IPInUseClientId,'h3cDhcpServer2IPInUseHardAddr':h3cDhcpServer2IPInUseHardAddr,'h3cDhcpServer2IPInUseHardType':h3cDhcpServer2IPInUseHardType,'h3cDhcpServer2IPInUseVlanId':h3cDhcpServer2IPInUseVlanId,'h3cDhcpServer2IPInUseEndLease':h3cDhcpServer2IPInUseEndLease,'h3cDhcpServer2IPInUseType':h3cDhcpServer2IPInUseType,'h3cDhcpServer2IPInUseIfIndex':h3cDhcpServer2IPInUseIfIndex,'h3cDhcpServer2IPInUseRowStatus':h3cDhcpServer2IPInUseRowStatus,'h3cDhcpServer2DefOptGrpTable':h3cDhcpServer2DefOptGrpTable,'h3cDhcpServer2DefOptGrpEntry':h3cDhcpServer2DefOptGrpEntry,_k:h3cDhcpServer2DefOptGrpClass,'h3cDhcpServer2DefOptGrpId':h3cDhcpServer2DefOptGrpId,'h3cDhcpServer2DefOptGrpStatus':h3cDhcpServer2DefOptGrpStatus,'h3cDhcpServer2ValidClassTable':h3cDhcpServer2ValidClassTable,'h3cDhcpServer2ValidClassEntry':h3cDhcpServer2ValidClassEntry,_l:h3cDhcpServer2ValidClassName,'h3cDhcpServer2ValidClassStatus':h3cDhcpServer2ValidClassStatus,'h3cDhcpServer2RuleHwAddrTable':h3cDhcpServer2RuleHwAddrTable,'h3cDhcpServer2RuleHwAddrEntry':h3cDhcpServer2RuleHwAddrEntry,_m:h3cDhcpServer2RuleHwAddrNumber,'h3cDhcpServer2RuleHwAddress':h3cDhcpServer2RuleHwAddress,'h3cDhcpServer2RuleHwAddrMask':h3cDhcpServer2RuleHwAddrMask,'h3cDhcpServer2RuleHwAddrType':h3cDhcpServer2RuleHwAddrType,'h3cDhcpServer2RuleHwAddrStatus':h3cDhcpServer2RuleHwAddrStatus,'h3cDhcpServer2OptionGroupTable':h3cDhcpServer2OptionGroupTable,'h3cDhcpServer2OptionGroupEntry':h3cDhcpServer2OptionGroupEntry,_R:h3cDhcpServer2OptionGroupId,'h3cDhcpServer2OptionGroupStatus':h3cDhcpServer2OptionGroupStatus,'h3cDhcpServer2OptionTable':h3cDhcpServer2OptionTable,'h3cDhcpServer2OptionEntry':h3cDhcpServer2OptionEntry,_n:h3cDhcpServer2OptionCode,'h3cDhcpServer2OptionType':h3cDhcpServer2OptionType,'h3cDhcpServer2OptionAscii':h3cDhcpServer2OptionAscii,'h3cDhcpServer2OptionHexStr':h3cDhcpServer2OptionHexStr,'h3cDhcpServer2OptionIPStr':h3cDhcpServer2OptionIPStr,'h3cDhcpServer2OptionRowStatus':h3cDhcpServer2OptionRowStatus,'h3cDhcpServer2PoolStatTable':h3cDhcpServer2PoolStatTable,'h3cDhcpServer2PoolStatEntry':h3cDhcpServer2PoolStatEntry,'h3cDhcpServer2PoolUsage':h3cDhcpServer2PoolUsage,'h3cDhcpServer2PoolReqCnt':h3cDhcpServer2PoolReqCnt,'h3cDhcpServer2PoolReqSuccCnt':h3cDhcpServer2PoolReqSuccCnt,'h3cDhcpServer2PoolDiscoverCnt':h3cDhcpServer2PoolDiscoverCnt,'h3cDhcpServer2PoolOfferCnt':h3cDhcpServer2PoolOfferCnt,'h3cDhcpServer2PoolAckCnt':h3cDhcpServer2PoolAckCnt,'h3cDhcpServer2PoolIPTotalNum':h3cDhcpServer2PoolIPTotalNum,'h3cDhcpServer2PoolIPUsedNum':h3cDhcpServer2PoolIPUsedNum,'h3cDhcpServer2PoolIPIdleNum':h3cDhcpServer2PoolIPIdleNum,'h3cDhcpServer2PoolIPExcludeNum':h3cDhcpServer2PoolIPExcludeNum,'h3cDhcpServer2PoolConflictNum':h3cDhcpServer2PoolConflictNum,'h3cDhcpServer2PoolAutoBindNum':h3cDhcpServer2PoolAutoBindNum,'h3cDhcpServer2PoolManualBindNum':h3cDhcpServer2PoolManualBindNum,'h3cDhcpServer2PoolExpiredBindNum':h3cDhcpServer2PoolExpiredBindNum,'h3cDhcpServer2PoolNameInfo':h3cDhcpServer2PoolNameInfo,'h3cDhcpRelay2ScalarObjects':h3cDhcpRelay2ScalarObjects,'h3cDhcpRelay2ConfigGroup':h3cDhcpRelay2ConfigGroup,'h3cDhcpRelay2UserInfoRecord':h3cDhcpRelay2UserInfoRecord,'h3cDhcpRelay2UserInfoRefresh':h3cDhcpRelay2UserInfoRefresh,'h3cDhcpRelay2UserInfoFlushTime':h3cDhcpRelay2UserInfoFlushTime,'h3cDhcpRelay2ReleaseAddr':h3cDhcpRelay2ReleaseAddr,'h3cDhcpRelay2StatisticsGroup':h3cDhcpRelay2StatisticsGroup,'h3cDhcpRelay2RxClientNum':h3cDhcpRelay2RxClientNum,'h3cDhcpRelay2TxClientNum':h3cDhcpRelay2TxClientNum,'h3cDhcpRelay2RxServerNum':h3cDhcpRelay2RxServerNum,'h3cDhcpRelay2TxServerNum':h3cDhcpRelay2TxServerNum,'h3cDhcpRelay2BadNum':h3cDhcpRelay2BadNum,'h3cDhcpRelay2BootpRequestNum':h3cDhcpRelay2BootpRequestNum,'h3cDhcpRelay2DiscoverNum':h3cDhcpRelay2DiscoverNum,'h3cDhcpRelay2RequestNum':h3cDhcpRelay2RequestNum,'h3cDhcpRelay2DeclineNum':h3cDhcpRelay2DeclineNum,'h3cDhcpRelay2ReleaseNum':h3cDhcpRelay2ReleaseNum,'h3cDhcpRelay2InformNum':h3cDhcpRelay2InformNum,'h3cDhcpRelay2BootpReplyNum':h3cDhcpRelay2BootpReplyNum,'h3cDhcpRelay2OfferNum':h3cDhcpRelay2OfferNum,'h3cDhcpRelay2AckNum':h3cDhcpRelay2AckNum,'h3cDhcpRelay2NakNum':h3cDhcpRelay2NakNum,'h3cDhcpRelay2Tables':h3cDhcpRelay2Tables,'h3cDhcpRelay2IfConfigTable':h3cDhcpRelay2IfConfigTable,'h3cDhcpRelay2IfConfigEntry':h3cDhcpRelay2IfConfigEntry,'h3cDhcpRelay2IfSelectRelay':h3cDhcpRelay2IfSelectRelay,'h3cDhcpRelay2IfCheckMac':h3cDhcpRelay2IfCheckMac,'h3cDhcpRelay2IfOpt82Enable':h3cDhcpRelay2IfOpt82Enable,'h3cDhcpRelay2IfOpt82Strategy':h3cDhcpRelay2IfOpt82Strategy,'h3cDhcpRelay2IfOpt82CIDMode':h3cDhcpRelay2IfOpt82CIDMode,'h3cDhcpRelay2IfOpt82CIDNodeType':h3cDhcpRelay2IfOpt82CIDNodeType,'h3cDhcpRelay2IfOpt82CIDNodeStr':h3cDhcpRelay2IfOpt82CIDNodeStr,'h3cDhcpRelay2IfOpt82CIDStr':h3cDhcpRelay2IfOpt82CIDStr,'h3cDhcpRelay2IfOpt82CIDFormat':h3cDhcpRelay2IfOpt82CIDFormat,'h3cDhcpRelay2IfOpt82RIDMode':h3cDhcpRelay2IfOpt82RIDMode,'h3cDhcpRelay2IfOpt82RIDStr':h3cDhcpRelay2IfOpt82RIDStr,'h3cDhcpRelay2IfOpt82RIDFormat':h3cDhcpRelay2IfOpt82RIDFormat,'h3cDhcpRelay2SrvAddrTable':h3cDhcpRelay2SrvAddrTable,'h3cDhcpRelay2SrvAddrEntry':h3cDhcpRelay2SrvAddrEntry,_q:h3cDhcpRelay2SrvAddrIP,'h3cDhcpRelay2SrvAddrRowStatus':h3cDhcpRelay2SrvAddrRowStatus,'h3cDhcpRelay2UserInfoTable':h3cDhcpRelay2UserInfoTable,'h3cDhcpRelay2UserInfoEntry':h3cDhcpRelay2UserInfoEntry,_r:h3cDhcpRelay2UserInfoVpnIndex,_s:h3cDhcpRelay2UserInfoIpAddr,'h3cDhcpRelay2UserInfoMacAddr':h3cDhcpRelay2UserInfoMacAddr,'h3cDhcpRelay2UserInfoIfIndex':h3cDhcpRelay2UserInfoIfIndex,'h3cDhcpRelay2UserInfoRowStatus':h3cDhcpRelay2UserInfoRowStatus,'h3cDhcpServer2Traps':h3cDhcpServer2Traps,'h3cDhcpServer2TrapNotify':h3cDhcpServer2TrapNotify,'h3cDhcpServer2AddrExhaust':h3cDhcpServer2AddrExhaust,'h3cDhcpServer2AddrExhaustRecov':h3cDhcpServer2AddrExhaustRecov,'h3cDhcpServer2IpUsageOverflow':h3cDhcpServer2IpUsageOverflow,'h3cDhcpServer2AllocOverflow':h3cDhcpServer2AllocOverflow,'h3cDhcpServer2IpUsageOverflowRecov':h3cDhcpServer2IpUsageOverflowRecov})