_Ad='ciapPrefixGroup'
_Ac='ciapNotifsGroup'
_Ab='ciapNotifDataGroup'
_Aa='ciapPoolGroupGroup'
_AZ='ciapRangeGroup'
_AY='ciapPoolGroup'
_AX='ciapGlobalGroup'
_AW='ciapEventThresholdFalling'
_AV='ciapEventThresholdRising'
_AU='ciapPoolGroupAddressesFree'
_AT='ciapPoolGroupAddressesInUse'
_AS='ciapPoolGroupThresholdFalling'
_AR='ciapPoolGroupThresholdRising'
_AQ='ciapPoolGroupThresholdUnits'
_AP='ciapPoolGroupName'
_AO='ciapPoolGroupIdNext'
_AN='ciapPrefixTableChanged'
_AM='ciapPrefixPrefixesFree'
_AL='ciapPrefixPrefixesInUse'
_AK='ciapPrefixThresholdFalling'
_AJ='ciapPrefixThresholdRising'
_AI='ciapPrefixThresholdUnits'
_AH='ciapPrefixPriority'
_AG='ciapPrefixRecycleDelay'
_AF='ciapPrefixCacheSize'
_AE='ciapPrefixAssignedLength'
_AD='ciapPrefixStorage'
_AC='ciapPrefixStatus'
_AB='ciapRangeTableChanged'
_AA='ciapRangeAddressesFree'
_A9='ciapRangeAddressesInUse'
_A8='ciapRangeThresholdFalling'
_A7='ciapRangeThresholdRising'
_A6='ciapRangeThresholdUnits'
_A5='ciapRangePriority'
_A4='ciapRangeRecycleDelay'
_A3='ciapRangeCacheSize'
_A2='ciapRangeAddressUpper'
_A1='ciapRangeStorage'
_A0='ciapRangeStatus'
_z='ciapAllocatedAddressMask'
_y='ciapPoolTableChanged'
_x='ciapPoolAddressesFree'
_w='ciapPoolAddressesInUse'
_v='ciapPoolThresholdFalling'
_u='ciapPoolThresholdRising'
_t='ciapPoolThresholdUnits'
_s='ciapPoolContainedIn'
_r='ciapPoolType'
_q='ciapPoolStorage'
_p='ciapPoolStatus'
_o='ciapPoolName'
_n='ciapPoolIdNext'
_m='ciapGlobalThresholdFalling'
_l='ciapGlobalThresholdRising'
_k='ciapGlobalThresholdUnits'
_j='ciapGlobalNotifyEnable'
_i='ciapAllocatedAddress'
_h='ciapAllocatedAddressType'
_g='ciapPrefixAddressMask'
_f='ciapPrefixAddress'
_e='ciapPrefixType'
_d='seconds'
_c='ciapRangeAddressLower'
_b='ciapRangeAddressType'
_a='TruthValue'
_Z='Integer32'
_Y='IpAddressPoolThresholdUnits'
_X='IpAddressPoolNameOrNull'
_W='IpAddressPoolGroupNameOrNull'
_V='ciapNotifyThresholdFalling'
_U='ciapNotifyThresholdRising'
_T='ciapPoolGroupContainsId'
_S='ciapPoolGroupId'
_R='IP prefixes'
_Q='ciapNotifyFree'
_P='ciapNotifyInUse'
_O='ciapNotifyThresholdUnits'
_N='ciapNotifyResource'
_M='IP addresses'
_L='StorageType'
_K='ciapPoolId'
_J='accessible-for-notify'
_I='IP addresses/prefixes'
_H='InetAddress'
_G='read-write'
_F='not-accessible'
_E='read-only'
_D='Unsigned32'
_C='read-create'
_B='current'
_A='CISCO-IP-ADDRESS-POOL-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
IpAddrPoolInstanceIdentifier,IpAddrPoolInstanceIdentifierOrZero,IpAddressPoolGroupName,IpAddressPoolGroupNameOrNull,IpAddressPoolNameOrNull,IpAddressPoolThresholdUnits=mibBuilder.importSymbols('CISCO-IP-ADDRESS-POOL-TC-MIB','IpAddrPoolInstanceIdentifier','IpAddrPoolInstanceIdentifierOrZero','IpAddressPoolGroupName',_W,_X,_Y)
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
InetAddress,InetAddressPrefixLength,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB',_H,'InetAddressPrefixLength','InetAddressType')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_Z,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_D,'iso')
DisplayString,PhysAddress,RowPointer,RowStatus,StorageType,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowPointer','RowStatus',_L,'TextualConvention','TimeStamp',_a)
ciscoIpAddressPoolMIB=ModuleIdentity((1,3,6,1,4,1,9,9,748))
if mibBuilder.loadTexts:ciscoIpAddressPoolMIB.setRevisions(('2010-02-02 00:00',))
_CiscoIpAddressPoolMIBNotifs_ObjectIdentity=ObjectIdentity
ciscoIpAddressPoolMIBNotifs=_CiscoIpAddressPoolMIBNotifs_ObjectIdentity((1,3,6,1,4,1,9,9,748,0))
_CiscoIpAddressPoolMIBObjects_ObjectIdentity=ObjectIdentity
ciscoIpAddressPoolMIBObjects=_CiscoIpAddressPoolMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,748,1))
_CiapGlobal_ObjectIdentity=ObjectIdentity
ciapGlobal=_CiapGlobal_ObjectIdentity((1,3,6,1,4,1,9,9,748,1,1))
class _CiapGlobalNotifyEnable_Type(TruthValue):defaultValue=2
_CiapGlobalNotifyEnable_Type.__name__=_a
_CiapGlobalNotifyEnable_Object=MibScalar
ciapGlobalNotifyEnable=_CiapGlobalNotifyEnable_Object((1,3,6,1,4,1,9,9,748,1,1,1),_CiapGlobalNotifyEnable_Type())
ciapGlobalNotifyEnable.setMaxAccess(_G)
if mibBuilder.loadTexts:ciapGlobalNotifyEnable.setStatus(_B)
class _CiapGlobalThresholdUnits_Type(IpAddressPoolThresholdUnits):defaultValue=2
_CiapGlobalThresholdUnits_Type.__name__=_Y
_CiapGlobalThresholdUnits_Object=MibScalar
ciapGlobalThresholdUnits=_CiapGlobalThresholdUnits_Object((1,3,6,1,4,1,9,9,748,1,1,2),_CiapGlobalThresholdUnits_Type())
ciapGlobalThresholdUnits.setMaxAccess(_G)
if mibBuilder.loadTexts:ciapGlobalThresholdUnits.setStatus(_B)
class _CiapGlobalThresholdRising_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_CiapGlobalThresholdRising_Type.__name__=_D
_CiapGlobalThresholdRising_Object=MibScalar
ciapGlobalThresholdRising=_CiapGlobalThresholdRising_Object((1,3,6,1,4,1,9,9,748,1,1,3),_CiapGlobalThresholdRising_Type())
ciapGlobalThresholdRising.setMaxAccess(_G)
if mibBuilder.loadTexts:ciapGlobalThresholdRising.setStatus(_B)
class _CiapGlobalThresholdFalling_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_CiapGlobalThresholdFalling_Type.__name__=_D
_CiapGlobalThresholdFalling_Object=MibScalar
ciapGlobalThresholdFalling=_CiapGlobalThresholdFalling_Object((1,3,6,1,4,1,9,9,748,1,1,4),_CiapGlobalThresholdFalling_Type())
ciapGlobalThresholdFalling.setMaxAccess(_G)
if mibBuilder.loadTexts:ciapGlobalThresholdFalling.setStatus(_B)
_CiapPools_ObjectIdentity=ObjectIdentity
ciapPools=_CiapPools_ObjectIdentity((1,3,6,1,4,1,9,9,748,1,2))
_CiapPoolIdNext_Type=IpAddrPoolInstanceIdentifierOrZero
_CiapPoolIdNext_Object=MibScalar
ciapPoolIdNext=_CiapPoolIdNext_Object((1,3,6,1,4,1,9,9,748,1,2,1),_CiapPoolIdNext_Type())
ciapPoolIdNext.setMaxAccess(_E)
if mibBuilder.loadTexts:ciapPoolIdNext.setStatus(_B)
_CiapPoolTable_Object=MibTable
ciapPoolTable=_CiapPoolTable_Object((1,3,6,1,4,1,9,9,748,1,2,2))
if mibBuilder.loadTexts:ciapPoolTable.setStatus(_B)
_CiapPoolEntry_Object=MibTableRow
ciapPoolEntry=_CiapPoolEntry_Object((1,3,6,1,4,1,9,9,748,1,2,2,1))
ciapPoolEntry.setIndexNames((0,_A,_K))
if mibBuilder.loadTexts:ciapPoolEntry.setStatus(_B)
_CiapPoolId_Type=IpAddrPoolInstanceIdentifier
_CiapPoolId_Object=MibTableColumn
ciapPoolId=_CiapPoolId_Object((1,3,6,1,4,1,9,9,748,1,2,2,1,1),_CiapPoolId_Type())
ciapPoolId.setMaxAccess(_F)
if mibBuilder.loadTexts:ciapPoolId.setStatus(_B)
_CiapPoolStatus_Type=RowStatus
_CiapPoolStatus_Object=MibTableColumn
ciapPoolStatus=_CiapPoolStatus_Object((1,3,6,1,4,1,9,9,748,1,2,2,1,2),_CiapPoolStatus_Type())
ciapPoolStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ciapPoolStatus.setStatus(_B)
class _CiapPoolStorage_Type(StorageType):defaultValue=2
_CiapPoolStorage_Type.__name__=_L
_CiapPoolStorage_Object=MibTableColumn
ciapPoolStorage=_CiapPoolStorage_Object((1,3,6,1,4,1,9,9,748,1,2,2,1,3),_CiapPoolStorage_Type())
ciapPoolStorage.setMaxAccess(_C)
if mibBuilder.loadTexts:ciapPoolStorage.setStatus(_B)
class _CiapPoolName_Type(IpAddressPoolNameOrNull):defaultValue=OctetString('')
_CiapPoolName_Type.__name__=_X
_CiapPoolName_Object=MibTableColumn
ciapPoolName=_CiapPoolName_Object((1,3,6,1,4,1,9,9,748,1,2,2,1,4),_CiapPoolName_Type())
ciapPoolName.setMaxAccess(_C)
if mibBuilder.loadTexts:ciapPoolName.setStatus(_B)
class _CiapPoolType_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('other',1),('shared',2),('local',3),('dhcp',4)))
_CiapPoolType_Type.__name__=_Z
_CiapPoolType_Object=MibTableColumn
ciapPoolType=_CiapPoolType_Object((1,3,6,1,4,1,9,9,748,1,2,2,1,5),_CiapPoolType_Type())
ciapPoolType.setMaxAccess(_C)
if mibBuilder.loadTexts:ciapPoolType.setStatus(_B)
class _CiapPoolContainedIn_Type(IpAddressPoolGroupNameOrNull):defaultValue=OctetString('')
_CiapPoolContainedIn_Type.__name__=_W
_CiapPoolContainedIn_Object=MibTableColumn
ciapPoolContainedIn=_CiapPoolContainedIn_Object((1,3,6,1,4,1,9,9,748,1,2,2,1,6),_CiapPoolContainedIn_Type())
ciapPoolContainedIn.setMaxAccess(_C)
if mibBuilder.loadTexts:ciapPoolContainedIn.setStatus(_B)
_CiapPoolThresholdUnits_Type=IpAddressPoolThresholdUnits
_CiapPoolThresholdUnits_Object=MibTableColumn
ciapPoolThresholdUnits=_CiapPoolThresholdUnits_Object((1,3,6,1,4,1,9,9,748,1,2,2,1,7),_CiapPoolThresholdUnits_Type())
ciapPoolThresholdUnits.setMaxAccess(_C)
if mibBuilder.loadTexts:ciapPoolThresholdUnits.setStatus(_B)
if mibBuilder.loadTexts:ciapPoolThresholdUnits.setUnits(_M)
class _CiapPoolThresholdRising_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_CiapPoolThresholdRising_Type.__name__=_D
_CiapPoolThresholdRising_Object=MibTableColumn
ciapPoolThresholdRising=_CiapPoolThresholdRising_Object((1,3,6,1,4,1,9,9,748,1,2,2,1,8),_CiapPoolThresholdRising_Type())
ciapPoolThresholdRising.setMaxAccess(_C)
if mibBuilder.loadTexts:ciapPoolThresholdRising.setStatus(_B)
class _CiapPoolThresholdFalling_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_CiapPoolThresholdFalling_Type.__name__=_D
_CiapPoolThresholdFalling_Object=MibTableColumn
ciapPoolThresholdFalling=_CiapPoolThresholdFalling_Object((1,3,6,1,4,1,9,9,748,1,2,2,1,9),_CiapPoolThresholdFalling_Type())
ciapPoolThresholdFalling.setMaxAccess(_C)
if mibBuilder.loadTexts:ciapPoolThresholdFalling.setStatus(_B)
_CiapPoolAddressesInUse_Type=Gauge32
_CiapPoolAddressesInUse_Object=MibTableColumn
ciapPoolAddressesInUse=_CiapPoolAddressesInUse_Object((1,3,6,1,4,1,9,9,748,1,2,2,1,10),_CiapPoolAddressesInUse_Type())
ciapPoolAddressesInUse.setMaxAccess(_C)
if mibBuilder.loadTexts:ciapPoolAddressesInUse.setStatus(_B)
if mibBuilder.loadTexts:ciapPoolAddressesInUse.setUnits(_I)
_CiapPoolAddressesFree_Type=Gauge32
_CiapPoolAddressesFree_Object=MibTableColumn
ciapPoolAddressesFree=_CiapPoolAddressesFree_Object((1,3,6,1,4,1,9,9,748,1,2,2,1,11),_CiapPoolAddressesFree_Type())
ciapPoolAddressesFree.setMaxAccess(_C)
if mibBuilder.loadTexts:ciapPoolAddressesFree.setStatus(_B)
if mibBuilder.loadTexts:ciapPoolAddressesFree.setUnits(_I)
_CiapPoolTableChanged_Type=TimeStamp
_CiapPoolTableChanged_Object=MibScalar
ciapPoolTableChanged=_CiapPoolTableChanged_Object((1,3,6,1,4,1,9,9,748,1,2,3),_CiapPoolTableChanged_Type())
ciapPoolTableChanged.setMaxAccess(_E)
if mibBuilder.loadTexts:ciapPoolTableChanged.setStatus(_B)
_CiapRangeTable_Object=MibTable
ciapRangeTable=_CiapRangeTable_Object((1,3,6,1,4,1,9,9,748,1,2,4))
if mibBuilder.loadTexts:ciapRangeTable.setStatus(_B)
_CiapRangeEntry_Object=MibTableRow
ciapRangeEntry=_CiapRangeEntry_Object((1,3,6,1,4,1,9,9,748,1,2,4,1))
ciapRangeEntry.setIndexNames((0,_A,_K),(0,_A,_b),(0,_A,_c))
if mibBuilder.loadTexts:ciapRangeEntry.setStatus(_B)
_CiapRangeAddressType_Type=InetAddressType
_CiapRangeAddressType_Object=MibTableColumn
ciapRangeAddressType=_CiapRangeAddressType_Object((1,3,6,1,4,1,9,9,748,1,2,4,1,1),_CiapRangeAddressType_Type())
ciapRangeAddressType.setMaxAccess(_F)
if mibBuilder.loadTexts:ciapRangeAddressType.setStatus(_B)
class _CiapRangeAddressLower_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,16))
_CiapRangeAddressLower_Type.__name__=_H
_CiapRangeAddressLower_Object=MibTableColumn
ciapRangeAddressLower=_CiapRangeAddressLower_Object((1,3,6,1,4,1,9,9,748,1,2,4,1,2),_CiapRangeAddressLower_Type())
ciapRangeAddressLower.setMaxAccess(_F)
if mibBuilder.loadTexts:ciapRangeAddressLower.setStatus(_B)
_CiapRangeStatus_Type=RowStatus
_CiapRangeStatus_Object=MibTableColumn
ciapRangeStatus=_CiapRangeStatus_Object((1,3,6,1,4,1,9,9,748,1,2,4,1,3),_CiapRangeStatus_Type())
ciapRangeStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ciapRangeStatus.setStatus(_B)
class _CiapRangeStorage_Type(StorageType):defaultValue=2
_CiapRangeStorage_Type.__name__=_L
_CiapRangeStorage_Object=MibTableColumn
ciapRangeStorage=_CiapRangeStorage_Object((1,3,6,1,4,1,9,9,748,1,2,4,1,4),_CiapRangeStorage_Type())
ciapRangeStorage.setMaxAccess(_C)
if mibBuilder.loadTexts:ciapRangeStorage.setStatus(_B)
_CiapRangeAddressUpper_Type=InetAddress
_CiapRangeAddressUpper_Object=MibTableColumn
ciapRangeAddressUpper=_CiapRangeAddressUpper_Object((1,3,6,1,4,1,9,9,748,1,2,4,1,5),_CiapRangeAddressUpper_Type())
ciapRangeAddressUpper.setMaxAccess(_C)
if mibBuilder.loadTexts:ciapRangeAddressUpper.setStatus(_B)
class _CiapRangeCacheSize_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_CiapRangeCacheSize_Type.__name__=_D
_CiapRangeCacheSize_Object=MibTableColumn
ciapRangeCacheSize=_CiapRangeCacheSize_Object((1,3,6,1,4,1,9,9,748,1,2,4,1,6),_CiapRangeCacheSize_Type())
ciapRangeCacheSize.setMaxAccess(_C)
if mibBuilder.loadTexts:ciapRangeCacheSize.setStatus(_B)
if mibBuilder.loadTexts:ciapRangeCacheSize.setUnits(_M)
class _CiapRangeRecycleDelay_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_CiapRangeRecycleDelay_Type.__name__=_D
_CiapRangeRecycleDelay_Object=MibTableColumn
ciapRangeRecycleDelay=_CiapRangeRecycleDelay_Object((1,3,6,1,4,1,9,9,748,1,2,4,1,7),_CiapRangeRecycleDelay_Type())
ciapRangeRecycleDelay.setMaxAccess(_C)
if mibBuilder.loadTexts:ciapRangeRecycleDelay.setStatus(_B)
if mibBuilder.loadTexts:ciapRangeRecycleDelay.setUnits(_d)
class _CiapRangePriority_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CiapRangePriority_Type.__name__=_D
_CiapRangePriority_Object=MibTableColumn
ciapRangePriority=_CiapRangePriority_Object((1,3,6,1,4,1,9,9,748,1,2,4,1,8),_CiapRangePriority_Type())
ciapRangePriority.setMaxAccess(_C)
if mibBuilder.loadTexts:ciapRangePriority.setStatus(_B)
_CiapRangeThresholdUnits_Type=IpAddressPoolThresholdUnits
_CiapRangeThresholdUnits_Object=MibTableColumn
ciapRangeThresholdUnits=_CiapRangeThresholdUnits_Object((1,3,6,1,4,1,9,9,748,1,2,4,1,9),_CiapRangeThresholdUnits_Type())
ciapRangeThresholdUnits.setMaxAccess(_C)
if mibBuilder.loadTexts:ciapRangeThresholdUnits.setStatus(_B)
class _CiapRangeThresholdRising_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_CiapRangeThresholdRising_Type.__name__=_D
_CiapRangeThresholdRising_Object=MibTableColumn
ciapRangeThresholdRising=_CiapRangeThresholdRising_Object((1,3,6,1,4,1,9,9,748,1,2,4,1,10),_CiapRangeThresholdRising_Type())
ciapRangeThresholdRising.setMaxAccess(_C)
if mibBuilder.loadTexts:ciapRangeThresholdRising.setStatus(_B)
class _CiapRangeThresholdFalling_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_CiapRangeThresholdFalling_Type.__name__=_D
_CiapRangeThresholdFalling_Object=MibTableColumn
ciapRangeThresholdFalling=_CiapRangeThresholdFalling_Object((1,3,6,1,4,1,9,9,748,1,2,4,1,11),_CiapRangeThresholdFalling_Type())
ciapRangeThresholdFalling.setMaxAccess(_C)
if mibBuilder.loadTexts:ciapRangeThresholdFalling.setStatus(_B)
_CiapRangeAddressesInUse_Type=Gauge32
_CiapRangeAddressesInUse_Object=MibTableColumn
ciapRangeAddressesInUse=_CiapRangeAddressesInUse_Object((1,3,6,1,4,1,9,9,748,1,2,4,1,12),_CiapRangeAddressesInUse_Type())
ciapRangeAddressesInUse.setMaxAccess(_E)
if mibBuilder.loadTexts:ciapRangeAddressesInUse.setStatus(_B)
if mibBuilder.loadTexts:ciapRangeAddressesInUse.setUnits(_M)
_CiapRangeAddressesFree_Type=Gauge32
_CiapRangeAddressesFree_Object=MibTableColumn
ciapRangeAddressesFree=_CiapRangeAddressesFree_Object((1,3,6,1,4,1,9,9,748,1,2,4,1,13),_CiapRangeAddressesFree_Type())
ciapRangeAddressesFree.setMaxAccess(_E)
if mibBuilder.loadTexts:ciapRangeAddressesFree.setStatus(_B)
if mibBuilder.loadTexts:ciapRangeAddressesFree.setUnits(_M)
_CiapRangeTableChanged_Type=TimeStamp
_CiapRangeTableChanged_Object=MibScalar
ciapRangeTableChanged=_CiapRangeTableChanged_Object((1,3,6,1,4,1,9,9,748,1,2,5),_CiapRangeTableChanged_Type())
ciapRangeTableChanged.setMaxAccess(_E)
if mibBuilder.loadTexts:ciapRangeTableChanged.setStatus(_B)
_CiapPrefixTable_Object=MibTable
ciapPrefixTable=_CiapPrefixTable_Object((1,3,6,1,4,1,9,9,748,1,2,6))
if mibBuilder.loadTexts:ciapPrefixTable.setStatus(_B)
_CiapPrefixEntry_Object=MibTableRow
ciapPrefixEntry=_CiapPrefixEntry_Object((1,3,6,1,4,1,9,9,748,1,2,6,1))
ciapPrefixEntry.setIndexNames((0,_A,_K),(0,_A,_e),(0,_A,_f),(0,_A,_g))
if mibBuilder.loadTexts:ciapPrefixEntry.setStatus(_B)
_CiapPrefixType_Type=InetAddressType
_CiapPrefixType_Object=MibTableColumn
ciapPrefixType=_CiapPrefixType_Object((1,3,6,1,4,1,9,9,748,1,2,6,1,1),_CiapPrefixType_Type())
ciapPrefixType.setMaxAccess(_F)
if mibBuilder.loadTexts:ciapPrefixType.setStatus(_B)
class _CiapPrefixAddress_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,16))
_CiapPrefixAddress_Type.__name__=_H
_CiapPrefixAddress_Object=MibTableColumn
ciapPrefixAddress=_CiapPrefixAddress_Object((1,3,6,1,4,1,9,9,748,1,2,6,1,2),_CiapPrefixAddress_Type())
ciapPrefixAddress.setMaxAccess(_F)
if mibBuilder.loadTexts:ciapPrefixAddress.setStatus(_B)
class _CiapPrefixAddressMask_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,16))
_CiapPrefixAddressMask_Type.__name__=_H
_CiapPrefixAddressMask_Object=MibTableColumn
ciapPrefixAddressMask=_CiapPrefixAddressMask_Object((1,3,6,1,4,1,9,9,748,1,2,6,1,3),_CiapPrefixAddressMask_Type())
ciapPrefixAddressMask.setMaxAccess(_F)
if mibBuilder.loadTexts:ciapPrefixAddressMask.setStatus(_B)
_CiapPrefixStatus_Type=RowStatus
_CiapPrefixStatus_Object=MibTableColumn
ciapPrefixStatus=_CiapPrefixStatus_Object((1,3,6,1,4,1,9,9,748,1,2,6,1,4),_CiapPrefixStatus_Type())
ciapPrefixStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ciapPrefixStatus.setStatus(_B)
class _CiapPrefixStorage_Type(StorageType):defaultValue=2
_CiapPrefixStorage_Type.__name__=_L
_CiapPrefixStorage_Object=MibTableColumn
ciapPrefixStorage=_CiapPrefixStorage_Object((1,3,6,1,4,1,9,9,748,1,2,6,1,5),_CiapPrefixStorage_Type())
ciapPrefixStorage.setMaxAccess(_C)
if mibBuilder.loadTexts:ciapPrefixStorage.setStatus(_B)
_CiapPrefixAssignedLength_Type=InetAddressPrefixLength
_CiapPrefixAssignedLength_Object=MibTableColumn
ciapPrefixAssignedLength=_CiapPrefixAssignedLength_Object((1,3,6,1,4,1,9,9,748,1,2,6,1,6),_CiapPrefixAssignedLength_Type())
ciapPrefixAssignedLength.setMaxAccess(_C)
if mibBuilder.loadTexts:ciapPrefixAssignedLength.setStatus(_B)
class _CiapPrefixCacheSize_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_CiapPrefixCacheSize_Type.__name__=_D
_CiapPrefixCacheSize_Object=MibTableColumn
ciapPrefixCacheSize=_CiapPrefixCacheSize_Object((1,3,6,1,4,1,9,9,748,1,2,6,1,7),_CiapPrefixCacheSize_Type())
ciapPrefixCacheSize.setMaxAccess(_C)
if mibBuilder.loadTexts:ciapPrefixCacheSize.setStatus(_B)
if mibBuilder.loadTexts:ciapPrefixCacheSize.setUnits(_R)
class _CiapPrefixRecycleDelay_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_CiapPrefixRecycleDelay_Type.__name__=_D
_CiapPrefixRecycleDelay_Object=MibTableColumn
ciapPrefixRecycleDelay=_CiapPrefixRecycleDelay_Object((1,3,6,1,4,1,9,9,748,1,2,6,1,8),_CiapPrefixRecycleDelay_Type())
ciapPrefixRecycleDelay.setMaxAccess(_C)
if mibBuilder.loadTexts:ciapPrefixRecycleDelay.setStatus(_B)
if mibBuilder.loadTexts:ciapPrefixRecycleDelay.setUnits(_d)
class _CiapPrefixPriority_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CiapPrefixPriority_Type.__name__=_D
_CiapPrefixPriority_Object=MibTableColumn
ciapPrefixPriority=_CiapPrefixPriority_Object((1,3,6,1,4,1,9,9,748,1,2,6,1,9),_CiapPrefixPriority_Type())
ciapPrefixPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:ciapPrefixPriority.setStatus(_B)
_CiapPrefixThresholdUnits_Type=IpAddressPoolThresholdUnits
_CiapPrefixThresholdUnits_Object=MibTableColumn
ciapPrefixThresholdUnits=_CiapPrefixThresholdUnits_Object((1,3,6,1,4,1,9,9,748,1,2,6,1,10),_CiapPrefixThresholdUnits_Type())
ciapPrefixThresholdUnits.setMaxAccess(_C)
if mibBuilder.loadTexts:ciapPrefixThresholdUnits.setStatus(_B)
class _CiapPrefixThresholdRising_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_CiapPrefixThresholdRising_Type.__name__=_D
_CiapPrefixThresholdRising_Object=MibTableColumn
ciapPrefixThresholdRising=_CiapPrefixThresholdRising_Object((1,3,6,1,4,1,9,9,748,1,2,6,1,11),_CiapPrefixThresholdRising_Type())
ciapPrefixThresholdRising.setMaxAccess(_C)
if mibBuilder.loadTexts:ciapPrefixThresholdRising.setStatus(_B)
class _CiapPrefixThresholdFalling_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_CiapPrefixThresholdFalling_Type.__name__=_D
_CiapPrefixThresholdFalling_Object=MibTableColumn
ciapPrefixThresholdFalling=_CiapPrefixThresholdFalling_Object((1,3,6,1,4,1,9,9,748,1,2,6,1,12),_CiapPrefixThresholdFalling_Type())
ciapPrefixThresholdFalling.setMaxAccess(_C)
if mibBuilder.loadTexts:ciapPrefixThresholdFalling.setStatus(_B)
_CiapPrefixPrefixesInUse_Type=Gauge32
_CiapPrefixPrefixesInUse_Object=MibTableColumn
ciapPrefixPrefixesInUse=_CiapPrefixPrefixesInUse_Object((1,3,6,1,4,1,9,9,748,1,2,6,1,13),_CiapPrefixPrefixesInUse_Type())
ciapPrefixPrefixesInUse.setMaxAccess(_C)
if mibBuilder.loadTexts:ciapPrefixPrefixesInUse.setStatus(_B)
if mibBuilder.loadTexts:ciapPrefixPrefixesInUse.setUnits(_R)
_CiapPrefixPrefixesFree_Type=Gauge32
_CiapPrefixPrefixesFree_Object=MibTableColumn
ciapPrefixPrefixesFree=_CiapPrefixPrefixesFree_Object((1,3,6,1,4,1,9,9,748,1,2,6,1,14),_CiapPrefixPrefixesFree_Type())
ciapPrefixPrefixesFree.setMaxAccess(_C)
if mibBuilder.loadTexts:ciapPrefixPrefixesFree.setStatus(_B)
if mibBuilder.loadTexts:ciapPrefixPrefixesFree.setUnits(_R)
_CiapPrefixTableChanged_Type=TimeStamp
_CiapPrefixTableChanged_Object=MibScalar
ciapPrefixTableChanged=_CiapPrefixTableChanged_Object((1,3,6,1,4,1,9,9,748,1,2,7),_CiapPrefixTableChanged_Type())
ciapPrefixTableChanged.setMaxAccess(_E)
if mibBuilder.loadTexts:ciapPrefixTableChanged.setStatus(_B)
_CiapPoolGroups_ObjectIdentity=ObjectIdentity
ciapPoolGroups=_CiapPoolGroups_ObjectIdentity((1,3,6,1,4,1,9,9,748,1,3))
_CiapPoolGroupIdNext_Type=IpAddrPoolInstanceIdentifierOrZero
_CiapPoolGroupIdNext_Object=MibScalar
ciapPoolGroupIdNext=_CiapPoolGroupIdNext_Object((1,3,6,1,4,1,9,9,748,1,3,1),_CiapPoolGroupIdNext_Type())
ciapPoolGroupIdNext.setMaxAccess(_E)
if mibBuilder.loadTexts:ciapPoolGroupIdNext.setStatus(_B)
_CiapPoolGroupTable_Object=MibTable
ciapPoolGroupTable=_CiapPoolGroupTable_Object((1,3,6,1,4,1,9,9,748,1,3,2))
if mibBuilder.loadTexts:ciapPoolGroupTable.setStatus(_B)
_CiapPoolGroupEntry_Object=MibTableRow
ciapPoolGroupEntry=_CiapPoolGroupEntry_Object((1,3,6,1,4,1,9,9,748,1,3,2,1))
ciapPoolGroupEntry.setIndexNames((0,_A,_S))
if mibBuilder.loadTexts:ciapPoolGroupEntry.setStatus(_B)
_CiapPoolGroupId_Type=IpAddrPoolInstanceIdentifier
_CiapPoolGroupId_Object=MibTableColumn
ciapPoolGroupId=_CiapPoolGroupId_Object((1,3,6,1,4,1,9,9,748,1,3,2,1,1),_CiapPoolGroupId_Type())
ciapPoolGroupId.setMaxAccess(_F)
if mibBuilder.loadTexts:ciapPoolGroupId.setStatus(_B)
_CiapPoolGroupName_Type=IpAddressPoolGroupName
_CiapPoolGroupName_Object=MibTableColumn
ciapPoolGroupName=_CiapPoolGroupName_Object((1,3,6,1,4,1,9,9,748,1,3,2,1,2),_CiapPoolGroupName_Type())
ciapPoolGroupName.setMaxAccess(_E)
if mibBuilder.loadTexts:ciapPoolGroupName.setStatus(_B)
_CiapPoolGroupThresholdUnits_Type=IpAddressPoolThresholdUnits
_CiapPoolGroupThresholdUnits_Object=MibTableColumn
ciapPoolGroupThresholdUnits=_CiapPoolGroupThresholdUnits_Object((1,3,6,1,4,1,9,9,748,1,3,2,1,3),_CiapPoolGroupThresholdUnits_Type())
ciapPoolGroupThresholdUnits.setMaxAccess(_G)
if mibBuilder.loadTexts:ciapPoolGroupThresholdUnits.setStatus(_B)
class _CiapPoolGroupThresholdRising_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_CiapPoolGroupThresholdRising_Type.__name__=_D
_CiapPoolGroupThresholdRising_Object=MibTableColumn
ciapPoolGroupThresholdRising=_CiapPoolGroupThresholdRising_Object((1,3,6,1,4,1,9,9,748,1,3,2,1,4),_CiapPoolGroupThresholdRising_Type())
ciapPoolGroupThresholdRising.setMaxAccess(_G)
if mibBuilder.loadTexts:ciapPoolGroupThresholdRising.setStatus(_B)
class _CiapPoolGroupThresholdFalling_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_CiapPoolGroupThresholdFalling_Type.__name__=_D
_CiapPoolGroupThresholdFalling_Object=MibTableColumn
ciapPoolGroupThresholdFalling=_CiapPoolGroupThresholdFalling_Object((1,3,6,1,4,1,9,9,748,1,3,2,1,5),_CiapPoolGroupThresholdFalling_Type())
ciapPoolGroupThresholdFalling.setMaxAccess(_G)
if mibBuilder.loadTexts:ciapPoolGroupThresholdFalling.setStatus(_B)
_CiapPoolGroupAddressesInUse_Type=Gauge32
_CiapPoolGroupAddressesInUse_Object=MibTableColumn
ciapPoolGroupAddressesInUse=_CiapPoolGroupAddressesInUse_Object((1,3,6,1,4,1,9,9,748,1,3,2,1,6),_CiapPoolGroupAddressesInUse_Type())
ciapPoolGroupAddressesInUse.setMaxAccess(_E)
if mibBuilder.loadTexts:ciapPoolGroupAddressesInUse.setStatus(_B)
if mibBuilder.loadTexts:ciapPoolGroupAddressesInUse.setUnits(_I)
_CiapPoolGroupAddressesFree_Type=Gauge32
_CiapPoolGroupAddressesFree_Object=MibTableColumn
ciapPoolGroupAddressesFree=_CiapPoolGroupAddressesFree_Object((1,3,6,1,4,1,9,9,748,1,3,2,1,7),_CiapPoolGroupAddressesFree_Type())
ciapPoolGroupAddressesFree.setMaxAccess(_E)
if mibBuilder.loadTexts:ciapPoolGroupAddressesFree.setStatus(_B)
if mibBuilder.loadTexts:ciapPoolGroupAddressesFree.setUnits(_I)
_CiapPoolGroupContainsTable_Object=MibTable
ciapPoolGroupContainsTable=_CiapPoolGroupContainsTable_Object((1,3,6,1,4,1,9,9,748,1,3,3))
if mibBuilder.loadTexts:ciapPoolGroupContainsTable.setStatus(_B)
_CiapPoolGroupContainsEntry_Object=MibTableRow
ciapPoolGroupContainsEntry=_CiapPoolGroupContainsEntry_Object((1,3,6,1,4,1,9,9,748,1,3,3,1))
ciapPoolGroupContainsEntry.setIndexNames((0,_A,_S),(0,_A,_T))
if mibBuilder.loadTexts:ciapPoolGroupContainsEntry.setStatus(_B)
_CiapPoolGroupContainsId_Type=IpAddrPoolInstanceIdentifier
_CiapPoolGroupContainsId_Object=MibTableColumn
ciapPoolGroupContainsId=_CiapPoolGroupContainsId_Object((1,3,6,1,4,1,9,9,748,1,3,3,1,1),_CiapPoolGroupContainsId_Type())
ciapPoolGroupContainsId.setMaxAccess(_E)
if mibBuilder.loadTexts:ciapPoolGroupContainsId.setStatus(_B)
_CiapAllocatedAddresses_ObjectIdentity=ObjectIdentity
ciapAllocatedAddresses=_CiapAllocatedAddresses_ObjectIdentity((1,3,6,1,4,1,9,9,748,1,4))
_CiapAllocatedAddressTable_Object=MibTable
ciapAllocatedAddressTable=_CiapAllocatedAddressTable_Object((1,3,6,1,4,1,9,9,748,1,4,1))
if mibBuilder.loadTexts:ciapAllocatedAddressTable.setStatus(_B)
_CiapAllocatedAddressEntry_Object=MibTableRow
ciapAllocatedAddressEntry=_CiapAllocatedAddressEntry_Object((1,3,6,1,4,1,9,9,748,1,4,1,1))
ciapAllocatedAddressEntry.setIndexNames((0,_A,_K),(0,_A,_h),(0,_A,_i))
if mibBuilder.loadTexts:ciapAllocatedAddressEntry.setStatus(_B)
_CiapAllocatedAddressType_Type=InetAddressType
_CiapAllocatedAddressType_Object=MibTableColumn
ciapAllocatedAddressType=_CiapAllocatedAddressType_Object((1,3,6,1,4,1,9,9,748,1,4,1,1,1),_CiapAllocatedAddressType_Type())
ciapAllocatedAddressType.setMaxAccess(_F)
if mibBuilder.loadTexts:ciapAllocatedAddressType.setStatus(_B)
class _CiapAllocatedAddress_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,16))
_CiapAllocatedAddress_Type.__name__=_H
_CiapAllocatedAddress_Object=MibTableColumn
ciapAllocatedAddress=_CiapAllocatedAddress_Object((1,3,6,1,4,1,9,9,748,1,4,1,1,2),_CiapAllocatedAddress_Type())
ciapAllocatedAddress.setMaxAccess(_F)
if mibBuilder.loadTexts:ciapAllocatedAddress.setStatus(_B)
class _CiapAllocatedAddressMask_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,16))
_CiapAllocatedAddressMask_Type.__name__=_H
_CiapAllocatedAddressMask_Object=MibTableColumn
ciapAllocatedAddressMask=_CiapAllocatedAddressMask_Object((1,3,6,1,4,1,9,9,748,1,4,1,1,3),_CiapAllocatedAddressMask_Type())
ciapAllocatedAddressMask.setMaxAccess(_E)
if mibBuilder.loadTexts:ciapAllocatedAddressMask.setStatus(_B)
_CiapNotifyData_ObjectIdentity=ObjectIdentity
ciapNotifyData=_CiapNotifyData_ObjectIdentity((1,3,6,1,4,1,9,9,748,1,5))
_CiapNotifyResource_Type=RowPointer
_CiapNotifyResource_Object=MibScalar
ciapNotifyResource=_CiapNotifyResource_Object((1,3,6,1,4,1,9,9,748,1,5,1),_CiapNotifyResource_Type())
ciapNotifyResource.setMaxAccess(_J)
if mibBuilder.loadTexts:ciapNotifyResource.setStatus(_B)
_CiapNotifyThresholdUnits_Type=IpAddressPoolThresholdUnits
_CiapNotifyThresholdUnits_Object=MibScalar
ciapNotifyThresholdUnits=_CiapNotifyThresholdUnits_Object((1,3,6,1,4,1,9,9,748,1,5,2),_CiapNotifyThresholdUnits_Type())
ciapNotifyThresholdUnits.setMaxAccess(_J)
if mibBuilder.loadTexts:ciapNotifyThresholdUnits.setStatus(_B)
class _CiapNotifyThresholdRising_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_CiapNotifyThresholdRising_Type.__name__=_D
_CiapNotifyThresholdRising_Object=MibScalar
ciapNotifyThresholdRising=_CiapNotifyThresholdRising_Object((1,3,6,1,4,1,9,9,748,1,5,3),_CiapNotifyThresholdRising_Type())
ciapNotifyThresholdRising.setMaxAccess(_J)
if mibBuilder.loadTexts:ciapNotifyThresholdRising.setStatus(_B)
class _CiapNotifyThresholdFalling_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_CiapNotifyThresholdFalling_Type.__name__=_D
_CiapNotifyThresholdFalling_Object=MibScalar
ciapNotifyThresholdFalling=_CiapNotifyThresholdFalling_Object((1,3,6,1,4,1,9,9,748,1,5,4),_CiapNotifyThresholdFalling_Type())
ciapNotifyThresholdFalling.setMaxAccess(_J)
if mibBuilder.loadTexts:ciapNotifyThresholdFalling.setStatus(_B)
_CiapNotifyInUse_Type=Gauge32
_CiapNotifyInUse_Object=MibScalar
ciapNotifyInUse=_CiapNotifyInUse_Object((1,3,6,1,4,1,9,9,748,1,5,5),_CiapNotifyInUse_Type())
ciapNotifyInUse.setMaxAccess(_J)
if mibBuilder.loadTexts:ciapNotifyInUse.setStatus(_B)
if mibBuilder.loadTexts:ciapNotifyInUse.setUnits(_I)
_CiapNotifyFree_Type=Gauge32
_CiapNotifyFree_Object=MibScalar
ciapNotifyFree=_CiapNotifyFree_Object((1,3,6,1,4,1,9,9,748,1,5,6),_CiapNotifyFree_Type())
ciapNotifyFree.setMaxAccess(_J)
if mibBuilder.loadTexts:ciapNotifyFree.setStatus(_B)
if mibBuilder.loadTexts:ciapNotifyFree.setUnits(_I)
_CiscoIpAddressPoolMIBConform_ObjectIdentity=ObjectIdentity
ciscoIpAddressPoolMIBConform=_CiscoIpAddressPoolMIBConform_ObjectIdentity((1,3,6,1,4,1,9,9,748,2))
_CiscoIpAddressPoolMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoIpAddressPoolMIBCompliances=_CiscoIpAddressPoolMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,748,2,1))
_CiscoIpAddressPoolMIBGroups_ObjectIdentity=ObjectIdentity
ciscoIpAddressPoolMIBGroups=_CiscoIpAddressPoolMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,748,2,2))
ciapGlobalGroup=ObjectGroup((1,3,6,1,4,1,9,9,748,2,2,1))
ciapGlobalGroup.setObjects(*((_A,_j),(_A,_k),(_A,_l),(_A,_m)))
if mibBuilder.loadTexts:ciapGlobalGroup.setStatus(_B)
ciapPoolGroup=ObjectGroup((1,3,6,1,4,1,9,9,748,2,2,2))
ciapPoolGroup.setObjects(*((_A,_n),(_A,_o),(_A,_p),(_A,_q),(_A,_r),(_A,_s),(_A,_t),(_A,_u),(_A,_v),(_A,_w),(_A,_x),(_A,_y),(_A,_z)))
if mibBuilder.loadTexts:ciapPoolGroup.setStatus(_B)
ciapRangeGroup=ObjectGroup((1,3,6,1,4,1,9,9,748,2,2,3))
ciapRangeGroup.setObjects(*((_A,_A0),(_A,_A1),(_A,_A2),(_A,_A3),(_A,_A4),(_A,_A5),(_A,_A6),(_A,_A7),(_A,_A8),(_A,_A9),(_A,_AA),(_A,_AB)))
if mibBuilder.loadTexts:ciapRangeGroup.setStatus(_B)
ciapPrefixGroup=ObjectGroup((1,3,6,1,4,1,9,9,748,2,2,4))
ciapPrefixGroup.setObjects(*((_A,_AC),(_A,_AD),(_A,_AE),(_A,_AF),(_A,_AG),(_A,_AH),(_A,_AI),(_A,_AJ),(_A,_AK),(_A,_AL),(_A,_AM),(_A,_AN)))
if mibBuilder.loadTexts:ciapPrefixGroup.setStatus(_B)
ciapPoolGroupGroup=ObjectGroup((1,3,6,1,4,1,9,9,748,2,2,5))
ciapPoolGroupGroup.setObjects(*((_A,_AO),(_A,_AP),(_A,_AQ),(_A,_AR),(_A,_AS),(_A,_AT),(_A,_AU),(_A,_T)))
if mibBuilder.loadTexts:ciapPoolGroupGroup.setStatus(_B)
ciapNotifDataGroup=ObjectGroup((1,3,6,1,4,1,9,9,748,2,2,6))
ciapNotifDataGroup.setObjects(*((_A,_N),(_A,_O),(_A,_U),(_A,_V),(_A,_P),(_A,_Q)))
if mibBuilder.loadTexts:ciapNotifDataGroup.setStatus(_B)
ciapEventThresholdRising=NotificationType((1,3,6,1,4,1,9,9,748,0,1))
ciapEventThresholdRising.setObjects(*((_A,_N),(_A,_O),(_A,_U),(_A,_P),(_A,_Q)))
if mibBuilder.loadTexts:ciapEventThresholdRising.setStatus(_B)
ciapEventThresholdFalling=NotificationType((1,3,6,1,4,1,9,9,748,0,2))
ciapEventThresholdFalling.setObjects(*((_A,_N),(_A,_O),(_A,_V),(_A,_P),(_A,_Q)))
if mibBuilder.loadTexts:ciapEventThresholdFalling.setStatus(_B)
ciapNotifsGroup=NotificationGroup((1,3,6,1,4,1,9,9,748,2,2,7))
ciapNotifsGroup.setObjects(*((_A,_AV),(_A,_AW)))
if mibBuilder.loadTexts:ciapNotifsGroup.setStatus(_B)
ciscoIpAddressPoolCompliance01=ModuleCompliance((1,3,6,1,4,1,9,9,748,2,1,1))
ciscoIpAddressPoolCompliance01.setObjects(*((_A,_AX),(_A,_AY),(_A,_AZ),(_A,_Aa),(_A,_Ab),(_A,_Ac),(_A,_Ad)))
if mibBuilder.loadTexts:ciscoIpAddressPoolCompliance01.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'ciscoIpAddressPoolMIB':ciscoIpAddressPoolMIB,'ciscoIpAddressPoolMIBNotifs':ciscoIpAddressPoolMIBNotifs,_AV:ciapEventThresholdRising,_AW:ciapEventThresholdFalling,'ciscoIpAddressPoolMIBObjects':ciscoIpAddressPoolMIBObjects,'ciapGlobal':ciapGlobal,_j:ciapGlobalNotifyEnable,_k:ciapGlobalThresholdUnits,_l:ciapGlobalThresholdRising,_m:ciapGlobalThresholdFalling,'ciapPools':ciapPools,_n:ciapPoolIdNext,'ciapPoolTable':ciapPoolTable,'ciapPoolEntry':ciapPoolEntry,_K:ciapPoolId,_p:ciapPoolStatus,_q:ciapPoolStorage,_o:ciapPoolName,_r:ciapPoolType,_s:ciapPoolContainedIn,_t:ciapPoolThresholdUnits,_u:ciapPoolThresholdRising,_v:ciapPoolThresholdFalling,_w:ciapPoolAddressesInUse,_x:ciapPoolAddressesFree,_y:ciapPoolTableChanged,'ciapRangeTable':ciapRangeTable,'ciapRangeEntry':ciapRangeEntry,_b:ciapRangeAddressType,_c:ciapRangeAddressLower,_A0:ciapRangeStatus,_A1:ciapRangeStorage,_A2:ciapRangeAddressUpper,_A3:ciapRangeCacheSize,_A4:ciapRangeRecycleDelay,_A5:ciapRangePriority,_A6:ciapRangeThresholdUnits,_A7:ciapRangeThresholdRising,_A8:ciapRangeThresholdFalling,_A9:ciapRangeAddressesInUse,_AA:ciapRangeAddressesFree,_AB:ciapRangeTableChanged,'ciapPrefixTable':ciapPrefixTable,'ciapPrefixEntry':ciapPrefixEntry,_e:ciapPrefixType,_f:ciapPrefixAddress,_g:ciapPrefixAddressMask,_AC:ciapPrefixStatus,_AD:ciapPrefixStorage,_AE:ciapPrefixAssignedLength,_AF:ciapPrefixCacheSize,_AG:ciapPrefixRecycleDelay,_AH:ciapPrefixPriority,_AI:ciapPrefixThresholdUnits,_AJ:ciapPrefixThresholdRising,_AK:ciapPrefixThresholdFalling,_AL:ciapPrefixPrefixesInUse,_AM:ciapPrefixPrefixesFree,_AN:ciapPrefixTableChanged,'ciapPoolGroups':ciapPoolGroups,_AO:ciapPoolGroupIdNext,'ciapPoolGroupTable':ciapPoolGroupTable,'ciapPoolGroupEntry':ciapPoolGroupEntry,_S:ciapPoolGroupId,_AP:ciapPoolGroupName,_AQ:ciapPoolGroupThresholdUnits,_AR:ciapPoolGroupThresholdRising,_AS:ciapPoolGroupThresholdFalling,_AT:ciapPoolGroupAddressesInUse,_AU:ciapPoolGroupAddressesFree,'ciapPoolGroupContainsTable':ciapPoolGroupContainsTable,'ciapPoolGroupContainsEntry':ciapPoolGroupContainsEntry,_T:ciapPoolGroupContainsId,'ciapAllocatedAddresses':ciapAllocatedAddresses,'ciapAllocatedAddressTable':ciapAllocatedAddressTable,'ciapAllocatedAddressEntry':ciapAllocatedAddressEntry,_h:ciapAllocatedAddressType,_i:ciapAllocatedAddress,_z:ciapAllocatedAddressMask,'ciapNotifyData':ciapNotifyData,_N:ciapNotifyResource,_O:ciapNotifyThresholdUnits,_U:ciapNotifyThresholdRising,_V:ciapNotifyThresholdFalling,_P:ciapNotifyInUse,_Q:ciapNotifyFree,'ciscoIpAddressPoolMIBConform':ciscoIpAddressPoolMIBConform,'ciscoIpAddressPoolMIBCompliances':ciscoIpAddressPoolMIBCompliances,'ciscoIpAddressPoolCompliance01':ciscoIpAddressPoolCompliance01,'ciscoIpAddressPoolMIBGroups':ciscoIpAddressPoolMIBGroups,_AX:ciapGlobalGroup,_AY:ciapPoolGroup,_AZ:ciapRangeGroup,_Ad:ciapPrefixGroup,_Aa:ciapPoolGroupGroup,_Ab:ciapNotifDataGroup,_Ac:ciapNotifsGroup})