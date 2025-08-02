_AW='madcapServerGroup'
_AV='mallocAllocRangeAdvertisable'
_AU='mallocAllocRangeTotalRequestedAddrs'
_AT='mallocAllocRangeTotalAllocatedAddrs'
_AS='mallocScopeServerAddress'
_AR='mallocScopeServerAddressType'
_AQ='madcapConfigNoResponseDelay'
_AP='mallocRequestLeaseIdentifier'
_AO='madcapReleases'
_AN='madcapRenews'
_AM='madcapRequests'
_AL='madcapInforms'
_AK='madcapDiscovers'
_AJ='madcapExcessiveClockSkews'
_AI='madcapBadLeaseIds'
_AH='madcapInvalidRequests'
_AG='madcapRequestsDenied'
_AF='madcapTotalErrors'
_AE='madcapConfigResponseCacheInterval'
_AD='madcapConfigOfferHold'
_AC='madcapConfigExtraAllocationTime'
_AB='madcapConfigClockSkewAllowance'
_AA='mallocRequestServerAddress'
_A9='mallocRequestServerAddressType'
_A8='mallocRequestClientAddress'
_A7='mallocRequestClientAddressType'
_A6='mallocAllocRangeMaxLeaseTime'
_A5='mallocAllocRangeMaxLeaseAddrs'
_A4='mallocAllocRangeNumTryingAddrs'
_A3='mallocAllocRangeNumWaitingAddrs'
_A2='mallocAllocRangeNumOfferedAddrs'
_A1='mallocAllocRangeNumAllocatedAddrs'
_A0='mallocAddressRequestId'
_z='mallocAddressNumAddrs'
_y='mallocRequestState'
_x='mallocRequestNumAddrs'
_w='mallocRequestEndTime'
_v='mallocRequestStartTime'
_u='mallocRequestScopeFirstAddress'
_t='mallocRequestScopeAddressType'
_s='mallocCapabilities'
_r='mallocAddressFirstAddress'
_q='mallocAddressAddressType'
_p='mallocRequestId'
_o='mallocAllocRangeFirstAddress'
_n='mallocScopeNameLangName'
_m='Integer32'
_l='LanguageTag'
_k='InetAddressType'
_j='OctetString'
_i='mallocPrefixCoordinatorGroup'
_h='madcapClientGroup'
_g='mallocClientScopeGroup'
_f='mallocClientGroup'
_e='mallocServerGroup'
_d='mallocScopeNameStorage'
_c='mallocScopeNameStatus'
_b='mallocScopeNameDefault'
_a='mallocScopeNameScopeName'
_Z='mallocScopeDivisible'
_Y='mallocAllocRangeStorage'
_X='mallocAllocRangeStatus'
_W='mallocAllocRangeSource'
_V='mallocAllocRangeLifetime'
_U='mallocAllocRangeLastAddress'
_T='mallocScopeStorage'
_S='mallocScopeStatus'
_R='mallocScopeSSM'
_Q='mallocScopeHopLimit'
_P='mallocScopeSource'
_O='mallocScopeLastAddress'
_N='mallocScopeFirstAddress'
_M='mallocScopeAddressType'
_L='TruthValue'
_K='StorageType'
_J='read-write'
_I='mallocBasicGroup'
_H='not-accessible'
_G='Unsigned32'
_F='InetAddress'
_E='seconds'
_D='read-create'
_C='read-only'
_B='current'
_A='MALLOC-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_j,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
IANAmallocRangeSource,IANAscopeSource=mibBuilder.importSymbols('IANA-MALLOC-MIB','IANAmallocRangeSource','IANAscopeSource')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB',_F,_k)
LanguageTag,=mibBuilder.importSymbols('IPMROUTE-STD-MIB',_l)
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,mib_2=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_m,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_G,'iso','mib-2')
DisplayString,PhysAddress,RowStatus,StorageType,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus',_K,'TextualConvention',_L)
mallocMIB=ModuleIdentity((1,3,6,1,2,1,101))
if mibBuilder.loadTexts:mallocMIB.setRevisions(('2003-06-09 00:00',))
_MallocMIBObjects_ObjectIdentity=ObjectIdentity
mallocMIBObjects=_MallocMIBObjects_ObjectIdentity((1,3,6,1,2,1,101,1))
_Malloc_ObjectIdentity=ObjectIdentity
malloc=_Malloc_ObjectIdentity((1,3,6,1,2,1,101,1,1))
class _MallocCapabilities_Type(Bits):namedValues=NamedValues(*(('startTime',0),('serverMobility',1),('retryAfter',2)))
_MallocCapabilities_Type.__name__='Bits'
_MallocCapabilities_Object=MibScalar
mallocCapabilities=_MallocCapabilities_Object((1,3,6,1,2,1,101,1,1,1),_MallocCapabilities_Type())
mallocCapabilities.setMaxAccess(_C)
if mibBuilder.loadTexts:mallocCapabilities.setStatus(_B)
_MallocScopeTable_Object=MibTable
mallocScopeTable=_MallocScopeTable_Object((1,3,6,1,2,1,101,1,1,2))
if mibBuilder.loadTexts:mallocScopeTable.setStatus(_B)
_MallocScopeEntry_Object=MibTableRow
mallocScopeEntry=_MallocScopeEntry_Object((1,3,6,1,2,1,101,1,1,2,1))
mallocScopeEntry.setIndexNames((0,_A,_M),(0,_A,_N))
if mibBuilder.loadTexts:mallocScopeEntry.setStatus(_B)
_MallocScopeAddressType_Type=InetAddressType
_MallocScopeAddressType_Object=MibTableColumn
mallocScopeAddressType=_MallocScopeAddressType_Object((1,3,6,1,2,1,101,1,1,2,1,1),_MallocScopeAddressType_Type())
mallocScopeAddressType.setMaxAccess(_H)
if mibBuilder.loadTexts:mallocScopeAddressType.setStatus(_B)
class _MallocScopeFirstAddress_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_MallocScopeFirstAddress_Type.__name__=_F
_MallocScopeFirstAddress_Object=MibTableColumn
mallocScopeFirstAddress=_MallocScopeFirstAddress_Object((1,3,6,1,2,1,101,1,1,2,1,2),_MallocScopeFirstAddress_Type())
mallocScopeFirstAddress.setMaxAccess(_H)
if mibBuilder.loadTexts:mallocScopeFirstAddress.setStatus(_B)
class _MallocScopeLastAddress_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_MallocScopeLastAddress_Type.__name__=_F
_MallocScopeLastAddress_Object=MibTableColumn
mallocScopeLastAddress=_MallocScopeLastAddress_Object((1,3,6,1,2,1,101,1,1,2,1,3),_MallocScopeLastAddress_Type())
mallocScopeLastAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:mallocScopeLastAddress.setStatus(_B)
class _MallocScopeHopLimit_Type(Unsigned32):defaultValue=255;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_MallocScopeHopLimit_Type.__name__=_G
_MallocScopeHopLimit_Object=MibTableColumn
mallocScopeHopLimit=_MallocScopeHopLimit_Object((1,3,6,1,2,1,101,1,1,2,1,4),_MallocScopeHopLimit_Type())
mallocScopeHopLimit.setMaxAccess(_D)
if mibBuilder.loadTexts:mallocScopeHopLimit.setStatus(_B)
_MallocScopeStatus_Type=RowStatus
_MallocScopeStatus_Object=MibTableColumn
mallocScopeStatus=_MallocScopeStatus_Object((1,3,6,1,2,1,101,1,1,2,1,5),_MallocScopeStatus_Type())
mallocScopeStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:mallocScopeStatus.setStatus(_B)
_MallocScopeSource_Type=IANAscopeSource
_MallocScopeSource_Object=MibTableColumn
mallocScopeSource=_MallocScopeSource_Object((1,3,6,1,2,1,101,1,1,2,1,6),_MallocScopeSource_Type())
mallocScopeSource.setMaxAccess(_C)
if mibBuilder.loadTexts:mallocScopeSource.setStatus(_B)
class _MallocScopeDivisible_Type(TruthValue):defaultValue=2
_MallocScopeDivisible_Type.__name__=_L
_MallocScopeDivisible_Object=MibTableColumn
mallocScopeDivisible=_MallocScopeDivisible_Object((1,3,6,1,2,1,101,1,1,2,1,7),_MallocScopeDivisible_Type())
mallocScopeDivisible.setMaxAccess(_D)
if mibBuilder.loadTexts:mallocScopeDivisible.setStatus(_B)
class _MallocScopeServerAddressType_Type(InetAddressType):defaultValue=0
_MallocScopeServerAddressType_Type.__name__=_k
_MallocScopeServerAddressType_Object=MibTableColumn
mallocScopeServerAddressType=_MallocScopeServerAddressType_Object((1,3,6,1,2,1,101,1,1,2,1,8),_MallocScopeServerAddressType_Type())
mallocScopeServerAddressType.setMaxAccess(_D)
if mibBuilder.loadTexts:mallocScopeServerAddressType.setStatus(_B)
class _MallocScopeServerAddress_Type(InetAddress):defaultHexValue=''
_MallocScopeServerAddress_Type.__name__=_F
_MallocScopeServerAddress_Object=MibTableColumn
mallocScopeServerAddress=_MallocScopeServerAddress_Object((1,3,6,1,2,1,101,1,1,2,1,9),_MallocScopeServerAddress_Type())
mallocScopeServerAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:mallocScopeServerAddress.setStatus(_B)
class _MallocScopeSSM_Type(TruthValue):defaultValue=2
_MallocScopeSSM_Type.__name__=_L
_MallocScopeSSM_Object=MibTableColumn
mallocScopeSSM=_MallocScopeSSM_Object((1,3,6,1,2,1,101,1,1,2,1,10),_MallocScopeSSM_Type())
mallocScopeSSM.setMaxAccess(_D)
if mibBuilder.loadTexts:mallocScopeSSM.setStatus(_B)
class _MallocScopeStorage_Type(StorageType):defaultValue=3
_MallocScopeStorage_Type.__name__=_K
_MallocScopeStorage_Object=MibTableColumn
mallocScopeStorage=_MallocScopeStorage_Object((1,3,6,1,2,1,101,1,1,2,1,11),_MallocScopeStorage_Type())
mallocScopeStorage.setMaxAccess(_D)
if mibBuilder.loadTexts:mallocScopeStorage.setStatus(_B)
_MallocScopeNameTable_Object=MibTable
mallocScopeNameTable=_MallocScopeNameTable_Object((1,3,6,1,2,1,101,1,1,3))
if mibBuilder.loadTexts:mallocScopeNameTable.setStatus(_B)
_MallocScopeNameEntry_Object=MibTableRow
mallocScopeNameEntry=_MallocScopeNameEntry_Object((1,3,6,1,2,1,101,1,1,3,1))
mallocScopeNameEntry.setIndexNames((0,_A,_M),(0,_A,_N),(1,_A,_n))
if mibBuilder.loadTexts:mallocScopeNameEntry.setStatus(_B)
class _MallocScopeNameLangName_Type(LanguageTag):subtypeSpec=LanguageTag.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,94))
_MallocScopeNameLangName_Type.__name__=_l
_MallocScopeNameLangName_Object=MibTableColumn
mallocScopeNameLangName=_MallocScopeNameLangName_Object((1,3,6,1,2,1,101,1,1,3,1,1),_MallocScopeNameLangName_Type())
mallocScopeNameLangName.setMaxAccess(_H)
if mibBuilder.loadTexts:mallocScopeNameLangName.setStatus(_B)
_MallocScopeNameScopeName_Type=SnmpAdminString
_MallocScopeNameScopeName_Object=MibTableColumn
mallocScopeNameScopeName=_MallocScopeNameScopeName_Object((1,3,6,1,2,1,101,1,1,3,1,2),_MallocScopeNameScopeName_Type())
mallocScopeNameScopeName.setMaxAccess(_D)
if mibBuilder.loadTexts:mallocScopeNameScopeName.setStatus(_B)
class _MallocScopeNameDefault_Type(TruthValue):defaultValue=2
_MallocScopeNameDefault_Type.__name__=_L
_MallocScopeNameDefault_Object=MibTableColumn
mallocScopeNameDefault=_MallocScopeNameDefault_Object((1,3,6,1,2,1,101,1,1,3,1,3),_MallocScopeNameDefault_Type())
mallocScopeNameDefault.setMaxAccess(_D)
if mibBuilder.loadTexts:mallocScopeNameDefault.setStatus(_B)
_MallocScopeNameStatus_Type=RowStatus
_MallocScopeNameStatus_Object=MibTableColumn
mallocScopeNameStatus=_MallocScopeNameStatus_Object((1,3,6,1,2,1,101,1,1,3,1,4),_MallocScopeNameStatus_Type())
mallocScopeNameStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:mallocScopeNameStatus.setStatus(_B)
class _MallocScopeNameStorage_Type(StorageType):defaultValue=3
_MallocScopeNameStorage_Type.__name__=_K
_MallocScopeNameStorage_Object=MibTableColumn
mallocScopeNameStorage=_MallocScopeNameStorage_Object((1,3,6,1,2,1,101,1,1,3,1,5),_MallocScopeNameStorage_Type())
mallocScopeNameStorage.setMaxAccess(_D)
if mibBuilder.loadTexts:mallocScopeNameStorage.setStatus(_B)
_MallocAllocRangeTable_Object=MibTable
mallocAllocRangeTable=_MallocAllocRangeTable_Object((1,3,6,1,2,1,101,1,1,4))
if mibBuilder.loadTexts:mallocAllocRangeTable.setStatus(_B)
_MallocAllocRangeEntry_Object=MibTableRow
mallocAllocRangeEntry=_MallocAllocRangeEntry_Object((1,3,6,1,2,1,101,1,1,4,1))
mallocAllocRangeEntry.setIndexNames((0,_A,_M),(0,_A,_N),(0,_A,_o))
if mibBuilder.loadTexts:mallocAllocRangeEntry.setStatus(_B)
class _MallocAllocRangeFirstAddress_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_MallocAllocRangeFirstAddress_Type.__name__=_F
_MallocAllocRangeFirstAddress_Object=MibTableColumn
mallocAllocRangeFirstAddress=_MallocAllocRangeFirstAddress_Object((1,3,6,1,2,1,101,1,1,4,1,1),_MallocAllocRangeFirstAddress_Type())
mallocAllocRangeFirstAddress.setMaxAccess(_H)
if mibBuilder.loadTexts:mallocAllocRangeFirstAddress.setStatus(_B)
class _MallocAllocRangeLastAddress_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_MallocAllocRangeLastAddress_Type.__name__=_F
_MallocAllocRangeLastAddress_Object=MibTableColumn
mallocAllocRangeLastAddress=_MallocAllocRangeLastAddress_Object((1,3,6,1,2,1,101,1,1,4,1,2),_MallocAllocRangeLastAddress_Type())
mallocAllocRangeLastAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:mallocAllocRangeLastAddress.setStatus(_B)
_MallocAllocRangeStatus_Type=RowStatus
_MallocAllocRangeStatus_Object=MibTableColumn
mallocAllocRangeStatus=_MallocAllocRangeStatus_Object((1,3,6,1,2,1,101,1,1,4,1,3),_MallocAllocRangeStatus_Type())
mallocAllocRangeStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:mallocAllocRangeStatus.setStatus(_B)
_MallocAllocRangeSource_Type=IANAmallocRangeSource
_MallocAllocRangeSource_Object=MibTableColumn
mallocAllocRangeSource=_MallocAllocRangeSource_Object((1,3,6,1,2,1,101,1,1,4,1,4),_MallocAllocRangeSource_Type())
mallocAllocRangeSource.setMaxAccess(_C)
if mibBuilder.loadTexts:mallocAllocRangeSource.setStatus(_B)
class _MallocAllocRangeLifetime_Type(Unsigned32):defaultValue=0
_MallocAllocRangeLifetime_Type.__name__=_G
_MallocAllocRangeLifetime_Object=MibTableColumn
mallocAllocRangeLifetime=_MallocAllocRangeLifetime_Object((1,3,6,1,2,1,101,1,1,4,1,5),_MallocAllocRangeLifetime_Type())
mallocAllocRangeLifetime.setMaxAccess(_D)
if mibBuilder.loadTexts:mallocAllocRangeLifetime.setStatus(_B)
if mibBuilder.loadTexts:mallocAllocRangeLifetime.setUnits(_E)
class _MallocAllocRangeMaxLeaseAddrs_Type(Unsigned32):defaultValue=0
_MallocAllocRangeMaxLeaseAddrs_Type.__name__=_G
_MallocAllocRangeMaxLeaseAddrs_Object=MibTableColumn
mallocAllocRangeMaxLeaseAddrs=_MallocAllocRangeMaxLeaseAddrs_Object((1,3,6,1,2,1,101,1,1,4,1,6),_MallocAllocRangeMaxLeaseAddrs_Type())
mallocAllocRangeMaxLeaseAddrs.setMaxAccess(_D)
if mibBuilder.loadTexts:mallocAllocRangeMaxLeaseAddrs.setStatus(_B)
class _MallocAllocRangeMaxLeaseTime_Type(Unsigned32):defaultValue=0
_MallocAllocRangeMaxLeaseTime_Type.__name__=_G
_MallocAllocRangeMaxLeaseTime_Object=MibTableColumn
mallocAllocRangeMaxLeaseTime=_MallocAllocRangeMaxLeaseTime_Object((1,3,6,1,2,1,101,1,1,4,1,7),_MallocAllocRangeMaxLeaseTime_Type())
mallocAllocRangeMaxLeaseTime.setMaxAccess(_D)
if mibBuilder.loadTexts:mallocAllocRangeMaxLeaseTime.setStatus(_B)
if mibBuilder.loadTexts:mallocAllocRangeMaxLeaseTime.setUnits(_E)
_MallocAllocRangeNumAllocatedAddrs_Type=Gauge32
_MallocAllocRangeNumAllocatedAddrs_Object=MibTableColumn
mallocAllocRangeNumAllocatedAddrs=_MallocAllocRangeNumAllocatedAddrs_Object((1,3,6,1,2,1,101,1,1,4,1,8),_MallocAllocRangeNumAllocatedAddrs_Type())
mallocAllocRangeNumAllocatedAddrs.setMaxAccess(_C)
if mibBuilder.loadTexts:mallocAllocRangeNumAllocatedAddrs.setStatus(_B)
_MallocAllocRangeNumOfferedAddrs_Type=Gauge32
_MallocAllocRangeNumOfferedAddrs_Object=MibTableColumn
mallocAllocRangeNumOfferedAddrs=_MallocAllocRangeNumOfferedAddrs_Object((1,3,6,1,2,1,101,1,1,4,1,9),_MallocAllocRangeNumOfferedAddrs_Type())
mallocAllocRangeNumOfferedAddrs.setMaxAccess(_C)
if mibBuilder.loadTexts:mallocAllocRangeNumOfferedAddrs.setStatus(_B)
_MallocAllocRangeNumWaitingAddrs_Type=Gauge32
_MallocAllocRangeNumWaitingAddrs_Object=MibTableColumn
mallocAllocRangeNumWaitingAddrs=_MallocAllocRangeNumWaitingAddrs_Object((1,3,6,1,2,1,101,1,1,4,1,10),_MallocAllocRangeNumWaitingAddrs_Type())
mallocAllocRangeNumWaitingAddrs.setMaxAccess(_C)
if mibBuilder.loadTexts:mallocAllocRangeNumWaitingAddrs.setStatus(_B)
_MallocAllocRangeNumTryingAddrs_Type=Gauge32
_MallocAllocRangeNumTryingAddrs_Object=MibTableColumn
mallocAllocRangeNumTryingAddrs=_MallocAllocRangeNumTryingAddrs_Object((1,3,6,1,2,1,101,1,1,4,1,11),_MallocAllocRangeNumTryingAddrs_Type())
mallocAllocRangeNumTryingAddrs.setMaxAccess(_C)
if mibBuilder.loadTexts:mallocAllocRangeNumTryingAddrs.setStatus(_B)
_MallocAllocRangeAdvertisable_Type=TruthValue
_MallocAllocRangeAdvertisable_Object=MibTableColumn
mallocAllocRangeAdvertisable=_MallocAllocRangeAdvertisable_Object((1,3,6,1,2,1,101,1,1,4,1,12),_MallocAllocRangeAdvertisable_Type())
mallocAllocRangeAdvertisable.setMaxAccess(_D)
if mibBuilder.loadTexts:mallocAllocRangeAdvertisable.setStatus(_B)
_MallocAllocRangeTotalAllocatedAddrs_Type=Gauge32
_MallocAllocRangeTotalAllocatedAddrs_Object=MibTableColumn
mallocAllocRangeTotalAllocatedAddrs=_MallocAllocRangeTotalAllocatedAddrs_Object((1,3,6,1,2,1,101,1,1,4,1,13),_MallocAllocRangeTotalAllocatedAddrs_Type())
mallocAllocRangeTotalAllocatedAddrs.setMaxAccess(_C)
if mibBuilder.loadTexts:mallocAllocRangeTotalAllocatedAddrs.setStatus(_B)
_MallocAllocRangeTotalRequestedAddrs_Type=Gauge32
_MallocAllocRangeTotalRequestedAddrs_Object=MibTableColumn
mallocAllocRangeTotalRequestedAddrs=_MallocAllocRangeTotalRequestedAddrs_Object((1,3,6,1,2,1,101,1,1,4,1,14),_MallocAllocRangeTotalRequestedAddrs_Type())
mallocAllocRangeTotalRequestedAddrs.setMaxAccess(_C)
if mibBuilder.loadTexts:mallocAllocRangeTotalRequestedAddrs.setStatus(_B)
class _MallocAllocRangeStorage_Type(StorageType):defaultValue=3
_MallocAllocRangeStorage_Type.__name__=_K
_MallocAllocRangeStorage_Object=MibTableColumn
mallocAllocRangeStorage=_MallocAllocRangeStorage_Object((1,3,6,1,2,1,101,1,1,4,1,15),_MallocAllocRangeStorage_Type())
mallocAllocRangeStorage.setMaxAccess(_D)
if mibBuilder.loadTexts:mallocAllocRangeStorage.setStatus(_B)
_MallocRequestTable_Object=MibTable
mallocRequestTable=_MallocRequestTable_Object((1,3,6,1,2,1,101,1,1,5))
if mibBuilder.loadTexts:mallocRequestTable.setStatus(_B)
_MallocRequestEntry_Object=MibTableRow
mallocRequestEntry=_MallocRequestEntry_Object((1,3,6,1,2,1,101,1,1,5,1))
mallocRequestEntry.setIndexNames((0,_A,_p))
if mibBuilder.loadTexts:mallocRequestEntry.setStatus(_B)
class _MallocRequestId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_MallocRequestId_Type.__name__=_G
_MallocRequestId_Object=MibTableColumn
mallocRequestId=_MallocRequestId_Object((1,3,6,1,2,1,101,1,1,5,1,1),_MallocRequestId_Type())
mallocRequestId.setMaxAccess(_H)
if mibBuilder.loadTexts:mallocRequestId.setStatus(_B)
_MallocRequestScopeAddressType_Type=InetAddressType
_MallocRequestScopeAddressType_Object=MibTableColumn
mallocRequestScopeAddressType=_MallocRequestScopeAddressType_Object((1,3,6,1,2,1,101,1,1,5,1,2),_MallocRequestScopeAddressType_Type())
mallocRequestScopeAddressType.setMaxAccess(_C)
if mibBuilder.loadTexts:mallocRequestScopeAddressType.setStatus(_B)
_MallocRequestScopeFirstAddress_Type=InetAddress
_MallocRequestScopeFirstAddress_Object=MibTableColumn
mallocRequestScopeFirstAddress=_MallocRequestScopeFirstAddress_Object((1,3,6,1,2,1,101,1,1,5,1,3),_MallocRequestScopeFirstAddress_Type())
mallocRequestScopeFirstAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:mallocRequestScopeFirstAddress.setStatus(_B)
_MallocRequestStartTime_Type=Unsigned32
_MallocRequestStartTime_Object=MibTableColumn
mallocRequestStartTime=_MallocRequestStartTime_Object((1,3,6,1,2,1,101,1,1,5,1,4),_MallocRequestStartTime_Type())
mallocRequestStartTime.setMaxAccess(_C)
if mibBuilder.loadTexts:mallocRequestStartTime.setStatus(_B)
if mibBuilder.loadTexts:mallocRequestStartTime.setUnits(_E)
_MallocRequestEndTime_Type=Unsigned32
_MallocRequestEndTime_Object=MibTableColumn
mallocRequestEndTime=_MallocRequestEndTime_Object((1,3,6,1,2,1,101,1,1,5,1,5),_MallocRequestEndTime_Type())
mallocRequestEndTime.setMaxAccess(_C)
if mibBuilder.loadTexts:mallocRequestEndTime.setStatus(_B)
if mibBuilder.loadTexts:mallocRequestEndTime.setUnits(_E)
_MallocRequestNumAddrs_Type=Unsigned32
_MallocRequestNumAddrs_Object=MibTableColumn
mallocRequestNumAddrs=_MallocRequestNumAddrs_Object((1,3,6,1,2,1,101,1,1,5,1,6),_MallocRequestNumAddrs_Type())
mallocRequestNumAddrs.setMaxAccess(_C)
if mibBuilder.loadTexts:mallocRequestNumAddrs.setStatus(_B)
class _MallocRequestState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('allocated',1),('offered',2),('waiting',3),('trying',4)))
_MallocRequestState_Type.__name__=_m
_MallocRequestState_Object=MibTableColumn
mallocRequestState=_MallocRequestState_Object((1,3,6,1,2,1,101,1,1,5,1,7),_MallocRequestState_Type())
mallocRequestState.setMaxAccess(_C)
if mibBuilder.loadTexts:mallocRequestState.setStatus(_B)
_MallocRequestClientAddressType_Type=InetAddressType
_MallocRequestClientAddressType_Object=MibTableColumn
mallocRequestClientAddressType=_MallocRequestClientAddressType_Object((1,3,6,1,2,1,101,1,1,5,1,8),_MallocRequestClientAddressType_Type())
mallocRequestClientAddressType.setMaxAccess(_C)
if mibBuilder.loadTexts:mallocRequestClientAddressType.setStatus(_B)
_MallocRequestClientAddress_Type=InetAddress
_MallocRequestClientAddress_Object=MibTableColumn
mallocRequestClientAddress=_MallocRequestClientAddress_Object((1,3,6,1,2,1,101,1,1,5,1,9),_MallocRequestClientAddress_Type())
mallocRequestClientAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:mallocRequestClientAddress.setStatus(_B)
_MallocRequestServerAddressType_Type=InetAddressType
_MallocRequestServerAddressType_Object=MibTableColumn
mallocRequestServerAddressType=_MallocRequestServerAddressType_Object((1,3,6,1,2,1,101,1,1,5,1,10),_MallocRequestServerAddressType_Type())
mallocRequestServerAddressType.setMaxAccess(_C)
if mibBuilder.loadTexts:mallocRequestServerAddressType.setStatus(_B)
_MallocRequestServerAddress_Type=InetAddress
_MallocRequestServerAddress_Object=MibTableColumn
mallocRequestServerAddress=_MallocRequestServerAddress_Object((1,3,6,1,2,1,101,1,1,5,1,11),_MallocRequestServerAddress_Type())
mallocRequestServerAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:mallocRequestServerAddress.setStatus(_B)
class _MallocRequestLeaseIdentifier_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_MallocRequestLeaseIdentifier_Type.__name__=_j
_MallocRequestLeaseIdentifier_Object=MibTableColumn
mallocRequestLeaseIdentifier=_MallocRequestLeaseIdentifier_Object((1,3,6,1,2,1,101,1,1,5,1,12),_MallocRequestLeaseIdentifier_Type())
mallocRequestLeaseIdentifier.setMaxAccess(_C)
if mibBuilder.loadTexts:mallocRequestLeaseIdentifier.setStatus(_B)
_MallocAddressTable_Object=MibTable
mallocAddressTable=_MallocAddressTable_Object((1,3,6,1,2,1,101,1,1,6))
if mibBuilder.loadTexts:mallocAddressTable.setStatus(_B)
_MallocAddressEntry_Object=MibTableRow
mallocAddressEntry=_MallocAddressEntry_Object((1,3,6,1,2,1,101,1,1,6,1))
mallocAddressEntry.setIndexNames((0,_A,_q),(0,_A,_r))
if mibBuilder.loadTexts:mallocAddressEntry.setStatus(_B)
_MallocAddressAddressType_Type=InetAddressType
_MallocAddressAddressType_Object=MibTableColumn
mallocAddressAddressType=_MallocAddressAddressType_Object((1,3,6,1,2,1,101,1,1,6,1,1),_MallocAddressAddressType_Type())
mallocAddressAddressType.setMaxAccess(_H)
if mibBuilder.loadTexts:mallocAddressAddressType.setStatus(_B)
class _MallocAddressFirstAddress_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_MallocAddressFirstAddress_Type.__name__=_F
_MallocAddressFirstAddress_Object=MibTableColumn
mallocAddressFirstAddress=_MallocAddressFirstAddress_Object((1,3,6,1,2,1,101,1,1,6,1,2),_MallocAddressFirstAddress_Type())
mallocAddressFirstAddress.setMaxAccess(_H)
if mibBuilder.loadTexts:mallocAddressFirstAddress.setStatus(_B)
_MallocAddressNumAddrs_Type=Unsigned32
_MallocAddressNumAddrs_Object=MibTableColumn
mallocAddressNumAddrs=_MallocAddressNumAddrs_Object((1,3,6,1,2,1,101,1,1,6,1,3),_MallocAddressNumAddrs_Type())
mallocAddressNumAddrs.setMaxAccess(_C)
if mibBuilder.loadTexts:mallocAddressNumAddrs.setStatus(_B)
_MallocAddressRequestId_Type=Unsigned32
_MallocAddressRequestId_Object=MibTableColumn
mallocAddressRequestId=_MallocAddressRequestId_Object((1,3,6,1,2,1,101,1,1,6,1,4),_MallocAddressRequestId_Type())
mallocAddressRequestId.setMaxAccess(_C)
if mibBuilder.loadTexts:mallocAddressRequestId.setStatus(_B)
_Madcap_ObjectIdentity=ObjectIdentity
madcap=_Madcap_ObjectIdentity((1,3,6,1,2,1,101,1,2))
_MadcapConfig_ObjectIdentity=ObjectIdentity
madcapConfig=_MadcapConfig_ObjectIdentity((1,3,6,1,2,1,101,1,2,1))
if mibBuilder.loadTexts:madcapConfig.setStatus(_B)
_MadcapConfigExtraAllocationTime_Type=Unsigned32
_MadcapConfigExtraAllocationTime_Object=MibScalar
madcapConfigExtraAllocationTime=_MadcapConfigExtraAllocationTime_Object((1,3,6,1,2,1,101,1,2,1,1),_MadcapConfigExtraAllocationTime_Type())
madcapConfigExtraAllocationTime.setMaxAccess(_J)
if mibBuilder.loadTexts:madcapConfigExtraAllocationTime.setStatus(_B)
if mibBuilder.loadTexts:madcapConfigExtraAllocationTime.setUnits(_E)
_MadcapConfigNoResponseDelay_Type=Unsigned32
_MadcapConfigNoResponseDelay_Object=MibScalar
madcapConfigNoResponseDelay=_MadcapConfigNoResponseDelay_Object((1,3,6,1,2,1,101,1,2,1,2),_MadcapConfigNoResponseDelay_Type())
madcapConfigNoResponseDelay.setMaxAccess(_J)
if mibBuilder.loadTexts:madcapConfigNoResponseDelay.setStatus(_B)
if mibBuilder.loadTexts:madcapConfigNoResponseDelay.setUnits(_E)
_MadcapConfigOfferHold_Type=Unsigned32
_MadcapConfigOfferHold_Object=MibScalar
madcapConfigOfferHold=_MadcapConfigOfferHold_Object((1,3,6,1,2,1,101,1,2,1,3),_MadcapConfigOfferHold_Type())
madcapConfigOfferHold.setMaxAccess(_J)
if mibBuilder.loadTexts:madcapConfigOfferHold.setStatus(_B)
if mibBuilder.loadTexts:madcapConfigOfferHold.setUnits(_E)
class _MadcapConfigResponseCacheInterval_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,300))
_MadcapConfigResponseCacheInterval_Type.__name__=_G
_MadcapConfigResponseCacheInterval_Object=MibScalar
madcapConfigResponseCacheInterval=_MadcapConfigResponseCacheInterval_Object((1,3,6,1,2,1,101,1,2,1,4),_MadcapConfigResponseCacheInterval_Type())
madcapConfigResponseCacheInterval.setMaxAccess(_J)
if mibBuilder.loadTexts:madcapConfigResponseCacheInterval.setStatus(_B)
if mibBuilder.loadTexts:madcapConfigResponseCacheInterval.setUnits(_E)
_MadcapConfigClockSkewAllowance_Type=Unsigned32
_MadcapConfigClockSkewAllowance_Object=MibScalar
madcapConfigClockSkewAllowance=_MadcapConfigClockSkewAllowance_Object((1,3,6,1,2,1,101,1,2,1,5),_MadcapConfigClockSkewAllowance_Type())
madcapConfigClockSkewAllowance.setMaxAccess(_J)
if mibBuilder.loadTexts:madcapConfigClockSkewAllowance.setStatus(_B)
if mibBuilder.loadTexts:madcapConfigClockSkewAllowance.setUnits(_E)
_MadcapCounters_ObjectIdentity=ObjectIdentity
madcapCounters=_MadcapCounters_ObjectIdentity((1,3,6,1,2,1,101,1,2,2))
if mibBuilder.loadTexts:madcapCounters.setStatus(_B)
_MadcapTotalErrors_Type=Counter32
_MadcapTotalErrors_Object=MibScalar
madcapTotalErrors=_MadcapTotalErrors_Object((1,3,6,1,2,1,101,1,2,2,1),_MadcapTotalErrors_Type())
madcapTotalErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:madcapTotalErrors.setStatus(_B)
_MadcapRequestsDenied_Type=Counter32
_MadcapRequestsDenied_Object=MibScalar
madcapRequestsDenied=_MadcapRequestsDenied_Object((1,3,6,1,2,1,101,1,2,2,2),_MadcapRequestsDenied_Type())
madcapRequestsDenied.setMaxAccess(_C)
if mibBuilder.loadTexts:madcapRequestsDenied.setStatus(_B)
_MadcapInvalidRequests_Type=Counter32
_MadcapInvalidRequests_Object=MibScalar
madcapInvalidRequests=_MadcapInvalidRequests_Object((1,3,6,1,2,1,101,1,2,2,3),_MadcapInvalidRequests_Type())
madcapInvalidRequests.setMaxAccess(_C)
if mibBuilder.loadTexts:madcapInvalidRequests.setStatus(_B)
_MadcapExcessiveClockSkews_Type=Counter32
_MadcapExcessiveClockSkews_Object=MibScalar
madcapExcessiveClockSkews=_MadcapExcessiveClockSkews_Object((1,3,6,1,2,1,101,1,2,2,4),_MadcapExcessiveClockSkews_Type())
madcapExcessiveClockSkews.setMaxAccess(_C)
if mibBuilder.loadTexts:madcapExcessiveClockSkews.setStatus(_B)
_MadcapBadLeaseIds_Type=Counter32
_MadcapBadLeaseIds_Object=MibScalar
madcapBadLeaseIds=_MadcapBadLeaseIds_Object((1,3,6,1,2,1,101,1,2,2,5),_MadcapBadLeaseIds_Type())
madcapBadLeaseIds.setMaxAccess(_C)
if mibBuilder.loadTexts:madcapBadLeaseIds.setStatus(_B)
_MadcapDiscovers_Type=Counter32
_MadcapDiscovers_Object=MibScalar
madcapDiscovers=_MadcapDiscovers_Object((1,3,6,1,2,1,101,1,2,2,6),_MadcapDiscovers_Type())
madcapDiscovers.setMaxAccess(_C)
if mibBuilder.loadTexts:madcapDiscovers.setStatus(_B)
_MadcapInforms_Type=Counter32
_MadcapInforms_Object=MibScalar
madcapInforms=_MadcapInforms_Object((1,3,6,1,2,1,101,1,2,2,7),_MadcapInforms_Type())
madcapInforms.setMaxAccess(_C)
if mibBuilder.loadTexts:madcapInforms.setStatus(_B)
_MadcapRequests_Type=Counter32
_MadcapRequests_Object=MibScalar
madcapRequests=_MadcapRequests_Object((1,3,6,1,2,1,101,1,2,2,8),_MadcapRequests_Type())
madcapRequests.setMaxAccess(_C)
if mibBuilder.loadTexts:madcapRequests.setStatus(_B)
_MadcapRenews_Type=Counter32
_MadcapRenews_Object=MibScalar
madcapRenews=_MadcapRenews_Object((1,3,6,1,2,1,101,1,2,2,9),_MadcapRenews_Type())
madcapRenews.setMaxAccess(_C)
if mibBuilder.loadTexts:madcapRenews.setStatus(_B)
_MadcapReleases_Type=Counter32
_MadcapReleases_Object=MibScalar
madcapReleases=_MadcapReleases_Object((1,3,6,1,2,1,101,1,2,2,10),_MadcapReleases_Type())
madcapReleases.setMaxAccess(_C)
if mibBuilder.loadTexts:madcapReleases.setStatus(_B)
_MallocConformance_ObjectIdentity=ObjectIdentity
mallocConformance=_MallocConformance_ObjectIdentity((1,3,6,1,2,1,101,2))
_MallocCompliances_ObjectIdentity=ObjectIdentity
mallocCompliances=_MallocCompliances_ObjectIdentity((1,3,6,1,2,1,101,2,1))
_MallocGroups_ObjectIdentity=ObjectIdentity
mallocGroups=_MallocGroups_ObjectIdentity((1,3,6,1,2,1,101,2,2))
mallocBasicGroup=ObjectGroup((1,3,6,1,2,1,101,2,2,1))
mallocBasicGroup.setObjects(*((_A,_s),(_A,_t),(_A,_u),(_A,_v),(_A,_w),(_A,_x),(_A,_y),(_A,_z),(_A,_A0)))
if mibBuilder.loadTexts:mallocBasicGroup.setStatus(_B)
mallocServerGroup=ObjectGroup((1,3,6,1,2,1,101,2,2,2))
mallocServerGroup.setObjects(*((_A,_O),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_A1),(_A,_A2),(_A,_A3),(_A,_A4),(_A,_A5),(_A,_A6),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_P),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_A7),(_A,_A8)))
if mibBuilder.loadTexts:mallocServerGroup.setStatus(_B)
mallocClientGroup=ObjectGroup((1,3,6,1,2,1,101,2,2,3))
mallocClientGroup.setObjects(*((_A,_A9),(_A,_AA)))
if mibBuilder.loadTexts:mallocClientGroup.setStatus(_B)
madcapServerGroup=ObjectGroup((1,3,6,1,2,1,101,2,2,4))
madcapServerGroup.setObjects(*((_A,_AB),(_A,_AC),(_A,_AD),(_A,_AE),(_A,_AF),(_A,_AG),(_A,_AH),(_A,_AI),(_A,_AJ),(_A,_AK),(_A,_AL),(_A,_AM),(_A,_AN),(_A,_AO)))
if mibBuilder.loadTexts:madcapServerGroup.setStatus(_B)
madcapClientGroup=ObjectGroup((1,3,6,1,2,1,101,2,2,5))
madcapClientGroup.setObjects(*((_A,_AP),(_A,_AQ)))
if mibBuilder.loadTexts:madcapClientGroup.setStatus(_B)
mallocClientScopeGroup=ObjectGroup((1,3,6,1,2,1,101,2,2,6))
mallocClientScopeGroup.setObjects(*((_A,_O),(_A,_Q),(_A,_S),(_A,_T),(_A,_P),(_A,_AR),(_A,_AS),(_A,_R),(_A,_a),(_A,_b),(_A,_c),(_A,_d)))
if mibBuilder.loadTexts:mallocClientScopeGroup.setStatus(_B)
mallocPrefixCoordinatorGroup=ObjectGroup((1,3,6,1,2,1,101,2,2,7))
mallocPrefixCoordinatorGroup.setObjects(*((_A,_U),(_A,_V),(_A,_X),(_A,_Y),(_A,_W),(_A,_AT),(_A,_AU),(_A,_AV),(_A,_O),(_A,_Z),(_A,_P)))
if mibBuilder.loadTexts:mallocPrefixCoordinatorGroup.setStatus(_B)
mallocServerReadOnlyCompliance=ModuleCompliance((1,3,6,1,2,1,101,2,1,1))
mallocServerReadOnlyCompliance.setObjects(*((_A,_I),(_A,_e)))
if mibBuilder.loadTexts:mallocServerReadOnlyCompliance.setStatus(_B)
mallocClientReadOnlyCompliance=ModuleCompliance((1,3,6,1,2,1,101,2,1,2))
mallocClientReadOnlyCompliance.setObjects(*((_A,_I),(_A,_f),(_A,_g),(_A,_h)))
if mibBuilder.loadTexts:mallocClientReadOnlyCompliance.setStatus(_B)
mallocPrefixCoordinatorReadOnlyCompliance=ModuleCompliance((1,3,6,1,2,1,101,2,1,3))
mallocPrefixCoordinatorReadOnlyCompliance.setObjects(*((_A,_I),(_A,_i)))
if mibBuilder.loadTexts:mallocPrefixCoordinatorReadOnlyCompliance.setStatus(_B)
mallocServerFullCompliance=ModuleCompliance((1,3,6,1,2,1,101,2,1,4))
mallocServerFullCompliance.setObjects(*((_A,_I),(_A,_e),(_A,_AW)))
if mibBuilder.loadTexts:mallocServerFullCompliance.setStatus(_B)
mallocClientFullCompliance=ModuleCompliance((1,3,6,1,2,1,101,2,1,5))
mallocClientFullCompliance.setObjects(*((_A,_I),(_A,_f),(_A,_g),(_A,_h)))
if mibBuilder.loadTexts:mallocClientFullCompliance.setStatus(_B)
mallocPrefixCoordinatorFullCompliance=ModuleCompliance((1,3,6,1,2,1,101,2,1,6))
mallocPrefixCoordinatorFullCompliance.setObjects(*((_A,_I),(_A,_i)))
if mibBuilder.loadTexts:mallocPrefixCoordinatorFullCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'mallocMIB':mallocMIB,'mallocMIBObjects':mallocMIBObjects,'malloc':malloc,_s:mallocCapabilities,'mallocScopeTable':mallocScopeTable,'mallocScopeEntry':mallocScopeEntry,_M:mallocScopeAddressType,_N:mallocScopeFirstAddress,_O:mallocScopeLastAddress,_Q:mallocScopeHopLimit,_S:mallocScopeStatus,_P:mallocScopeSource,_Z:mallocScopeDivisible,_AR:mallocScopeServerAddressType,_AS:mallocScopeServerAddress,_R:mallocScopeSSM,_T:mallocScopeStorage,'mallocScopeNameTable':mallocScopeNameTable,'mallocScopeNameEntry':mallocScopeNameEntry,_n:mallocScopeNameLangName,_a:mallocScopeNameScopeName,_b:mallocScopeNameDefault,_c:mallocScopeNameStatus,_d:mallocScopeNameStorage,'mallocAllocRangeTable':mallocAllocRangeTable,'mallocAllocRangeEntry':mallocAllocRangeEntry,_o:mallocAllocRangeFirstAddress,_U:mallocAllocRangeLastAddress,_X:mallocAllocRangeStatus,_W:mallocAllocRangeSource,_V:mallocAllocRangeLifetime,_A5:mallocAllocRangeMaxLeaseAddrs,_A6:mallocAllocRangeMaxLeaseTime,_A1:mallocAllocRangeNumAllocatedAddrs,_A2:mallocAllocRangeNumOfferedAddrs,_A3:mallocAllocRangeNumWaitingAddrs,_A4:mallocAllocRangeNumTryingAddrs,_AV:mallocAllocRangeAdvertisable,_AT:mallocAllocRangeTotalAllocatedAddrs,_AU:mallocAllocRangeTotalRequestedAddrs,_Y:mallocAllocRangeStorage,'mallocRequestTable':mallocRequestTable,'mallocRequestEntry':mallocRequestEntry,_p:mallocRequestId,_t:mallocRequestScopeAddressType,_u:mallocRequestScopeFirstAddress,_v:mallocRequestStartTime,_w:mallocRequestEndTime,_x:mallocRequestNumAddrs,_y:mallocRequestState,_A7:mallocRequestClientAddressType,_A8:mallocRequestClientAddress,_A9:mallocRequestServerAddressType,_AA:mallocRequestServerAddress,_AP:mallocRequestLeaseIdentifier,'mallocAddressTable':mallocAddressTable,'mallocAddressEntry':mallocAddressEntry,_q:mallocAddressAddressType,_r:mallocAddressFirstAddress,_z:mallocAddressNumAddrs,_A0:mallocAddressRequestId,'madcap':madcap,'madcapConfig':madcapConfig,_AC:madcapConfigExtraAllocationTime,_AQ:madcapConfigNoResponseDelay,_AD:madcapConfigOfferHold,_AE:madcapConfigResponseCacheInterval,_AB:madcapConfigClockSkewAllowance,'madcapCounters':madcapCounters,_AF:madcapTotalErrors,_AG:madcapRequestsDenied,_AH:madcapInvalidRequests,_AJ:madcapExcessiveClockSkews,_AI:madcapBadLeaseIds,_AK:madcapDiscovers,_AL:madcapInforms,_AM:madcapRequests,_AN:madcapRenews,_AO:madcapReleases,'mallocConformance':mallocConformance,'mallocCompliances':mallocCompliances,'mallocServerReadOnlyCompliance':mallocServerReadOnlyCompliance,'mallocClientReadOnlyCompliance':mallocClientReadOnlyCompliance,'mallocPrefixCoordinatorReadOnlyCompliance':mallocPrefixCoordinatorReadOnlyCompliance,'mallocServerFullCompliance':mallocServerFullCompliance,'mallocClientFullCompliance':mallocClientFullCompliance,'mallocPrefixCoordinatorFullCompliance':mallocPrefixCoordinatorFullCompliance,'mallocGroups':mallocGroups,_I:mallocBasicGroup,_e:mallocServerGroup,_f:mallocClientGroup,_AW:madcapServerGroup,_h:madcapClientGroup,_g:mallocClientScopeGroup,_i:mallocPrefixCoordinatorGroup})