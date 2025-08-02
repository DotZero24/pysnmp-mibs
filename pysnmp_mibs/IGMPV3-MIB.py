_T='mgmdRouterIGMPStaticGroupIpAddr'
_S='mgmdRouterIGMPStaticGroupIfIndex'
_R='mgmdRouterChkSubSrcNetIfIndex'
_Q='mgmdRouterSrcListHostAddress'
_P='mgmdRouterSrcListAddress'
_O='mgmdRouterSrcListIfIndex'
_N='mgmdRouterSrcListAddressType'
_M='mgmdRouterCacheAddress'
_L='mgmdRouterCacheIfIndex'
_K='mgmdRouterCacheAddressType'
_J='tenths of seconds'
_I='mgmdRouterInterfaceQuerierType'
_H='mgmdRouterInterfaceIfIndex'
_G='Integer32'
_F='Unsigned32'
_E='not-accessible'
_D='read-create'
_C='IGMPV3-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dlink_common_mgmt,=mibBuilder.importSymbols('DLINK-ID-REC-MIB','dlink-common-mgmt')
InterfaceIndex,InterfaceIndexOrZero=mibBuilder.importSymbols('IF-MIB','InterfaceIndex','InterfaceIndexOrZero')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,mib_2=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_G,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_F,'iso','mib-2')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TruthValue')
swIgmpMIB=ModuleIdentity((1,3,6,1,4,1,171,12,18))
_SwIgmpMIBObjects_ObjectIdentity=ObjectIdentity
swIgmpMIBObjects=_SwIgmpMIBObjects_ObjectIdentity((1,3,6,1,4,1,171,12,18,1))
_MgmdRouterInterfaceTable_Object=MibTable
mgmdRouterInterfaceTable=_MgmdRouterInterfaceTable_Object((1,3,6,1,4,1,171,12,18,1,4))
if mibBuilder.loadTexts:mgmdRouterInterfaceTable.setStatus(_A)
_MgmdRouterInterfaceEntry_Object=MibTableRow
mgmdRouterInterfaceEntry=_MgmdRouterInterfaceEntry_Object((1,3,6,1,4,1,171,12,18,1,4,1))
mgmdRouterInterfaceEntry.setIndexNames((0,_C,_H),(0,_C,_I))
if mibBuilder.loadTexts:mgmdRouterInterfaceEntry.setStatus(_A)
_MgmdRouterInterfaceIfIndex_Type=InterfaceIndex
_MgmdRouterInterfaceIfIndex_Object=MibTableColumn
mgmdRouterInterfaceIfIndex=_MgmdRouterInterfaceIfIndex_Object((1,3,6,1,4,1,171,12,18,1,4,1,1),_MgmdRouterInterfaceIfIndex_Type())
mgmdRouterInterfaceIfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:mgmdRouterInterfaceIfIndex.setStatus(_A)
_MgmdRouterInterfaceQuerierType_Type=InetAddressType
_MgmdRouterInterfaceQuerierType_Object=MibTableColumn
mgmdRouterInterfaceQuerierType=_MgmdRouterInterfaceQuerierType_Object((1,3,6,1,4,1,171,12,18,1,4,1,2),_MgmdRouterInterfaceQuerierType_Type())
mgmdRouterInterfaceQuerierType.setMaxAccess(_E)
if mibBuilder.loadTexts:mgmdRouterInterfaceQuerierType.setStatus(_A)
_MgmdRouterInterfaceQuerier_Type=InetAddress
_MgmdRouterInterfaceQuerier_Object=MibTableColumn
mgmdRouterInterfaceQuerier=_MgmdRouterInterfaceQuerier_Object((1,3,6,1,4,1,171,12,18,1,4,1,3),_MgmdRouterInterfaceQuerier_Type())
mgmdRouterInterfaceQuerier.setMaxAccess(_B)
if mibBuilder.loadTexts:mgmdRouterInterfaceQuerier.setStatus(_A)
class _MgmdRouterInterfaceQueryInterval_Type(Unsigned32):defaultValue=125
_MgmdRouterInterfaceQueryInterval_Type.__name__=_F
_MgmdRouterInterfaceQueryInterval_Object=MibTableColumn
mgmdRouterInterfaceQueryInterval=_MgmdRouterInterfaceQueryInterval_Object((1,3,6,1,4,1,171,12,18,1,4,1,4),_MgmdRouterInterfaceQueryInterval_Type())
mgmdRouterInterfaceQueryInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:mgmdRouterInterfaceQueryInterval.setStatus(_A)
if mibBuilder.loadTexts:mgmdRouterInterfaceQueryInterval.setUnits('seconds')
_MgmdRouterInterfaceStatus_Type=RowStatus
_MgmdRouterInterfaceStatus_Object=MibTableColumn
mgmdRouterInterfaceStatus=_MgmdRouterInterfaceStatus_Object((1,3,6,1,4,1,171,12,18,1,4,1,5),_MgmdRouterInterfaceStatus_Type())
mgmdRouterInterfaceStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:mgmdRouterInterfaceStatus.setStatus(_A)
class _MgmdRouterInterfaceVersion_Type(Unsigned32):defaultValue=3
_MgmdRouterInterfaceVersion_Type.__name__=_F
_MgmdRouterInterfaceVersion_Object=MibTableColumn
mgmdRouterInterfaceVersion=_MgmdRouterInterfaceVersion_Object((1,3,6,1,4,1,171,12,18,1,4,1,6),_MgmdRouterInterfaceVersion_Type())
mgmdRouterInterfaceVersion.setMaxAccess(_D)
if mibBuilder.loadTexts:mgmdRouterInterfaceVersion.setStatus(_A)
class _MgmdRouterInterfaceQueryMaxResponseTime_Type(Unsigned32):defaultValue=100;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_MgmdRouterInterfaceQueryMaxResponseTime_Type.__name__=_F
_MgmdRouterInterfaceQueryMaxResponseTime_Object=MibTableColumn
mgmdRouterInterfaceQueryMaxResponseTime=_MgmdRouterInterfaceQueryMaxResponseTime_Object((1,3,6,1,4,1,171,12,18,1,4,1,7),_MgmdRouterInterfaceQueryMaxResponseTime_Type())
mgmdRouterInterfaceQueryMaxResponseTime.setMaxAccess(_D)
if mibBuilder.loadTexts:mgmdRouterInterfaceQueryMaxResponseTime.setStatus(_A)
if mibBuilder.loadTexts:mgmdRouterInterfaceQueryMaxResponseTime.setUnits(_J)
_MgmdRouterInterfaceQuerierUpTime_Type=TimeTicks
_MgmdRouterInterfaceQuerierUpTime_Object=MibTableColumn
mgmdRouterInterfaceQuerierUpTime=_MgmdRouterInterfaceQuerierUpTime_Object((1,3,6,1,4,1,171,12,18,1,4,1,8),_MgmdRouterInterfaceQuerierUpTime_Type())
mgmdRouterInterfaceQuerierUpTime.setMaxAccess(_B)
if mibBuilder.loadTexts:mgmdRouterInterfaceQuerierUpTime.setStatus(_A)
_MgmdRouterInterfaceQuerierExpiryTime_Type=TimeTicks
_MgmdRouterInterfaceQuerierExpiryTime_Object=MibTableColumn
mgmdRouterInterfaceQuerierExpiryTime=_MgmdRouterInterfaceQuerierExpiryTime_Object((1,3,6,1,4,1,171,12,18,1,4,1,9),_MgmdRouterInterfaceQuerierExpiryTime_Type())
mgmdRouterInterfaceQuerierExpiryTime.setMaxAccess(_B)
if mibBuilder.loadTexts:mgmdRouterInterfaceQuerierExpiryTime.setStatus(_A)
class _MgmdRouterInterfaceRobustness_Type(Unsigned32):defaultValue=2;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_MgmdRouterInterfaceRobustness_Type.__name__=_F
_MgmdRouterInterfaceRobustness_Object=MibTableColumn
mgmdRouterInterfaceRobustness=_MgmdRouterInterfaceRobustness_Object((1,3,6,1,4,1,171,12,18,1,4,1,14),_MgmdRouterInterfaceRobustness_Type())
mgmdRouterInterfaceRobustness.setMaxAccess(_D)
if mibBuilder.loadTexts:mgmdRouterInterfaceRobustness.setStatus(_A)
class _MgmdRouterInterfaceLastMembQueryIntvl_Type(Unsigned32):defaultValue=10;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_MgmdRouterInterfaceLastMembQueryIntvl_Type.__name__=_F
_MgmdRouterInterfaceLastMembQueryIntvl_Object=MibTableColumn
mgmdRouterInterfaceLastMembQueryIntvl=_MgmdRouterInterfaceLastMembQueryIntvl_Object((1,3,6,1,4,1,171,12,18,1,4,1,15),_MgmdRouterInterfaceLastMembQueryIntvl_Type())
mgmdRouterInterfaceLastMembQueryIntvl.setMaxAccess(_D)
if mibBuilder.loadTexts:mgmdRouterInterfaceLastMembQueryIntvl.setStatus(_A)
if mibBuilder.loadTexts:mgmdRouterInterfaceLastMembQueryIntvl.setUnits(_J)
_MgmdRouterCacheTable_Object=MibTable
mgmdRouterCacheTable=_MgmdRouterCacheTable_Object((1,3,6,1,4,1,171,12,18,1,6))
if mibBuilder.loadTexts:mgmdRouterCacheTable.setStatus(_A)
_MgmdRouterCacheEntry_Object=MibTableRow
mgmdRouterCacheEntry=_MgmdRouterCacheEntry_Object((1,3,6,1,4,1,171,12,18,1,6,1))
mgmdRouterCacheEntry.setIndexNames((0,_C,_K),(0,_C,_L),(0,_C,_M))
if mibBuilder.loadTexts:mgmdRouterCacheEntry.setStatus(_A)
_MgmdRouterCacheAddressType_Type=InetAddressType
_MgmdRouterCacheAddressType_Object=MibTableColumn
mgmdRouterCacheAddressType=_MgmdRouterCacheAddressType_Object((1,3,6,1,4,1,171,12,18,1,6,1,1),_MgmdRouterCacheAddressType_Type())
mgmdRouterCacheAddressType.setMaxAccess(_B)
if mibBuilder.loadTexts:mgmdRouterCacheAddressType.setStatus(_A)
_MgmdRouterCacheIfIndex_Type=InterfaceIndex
_MgmdRouterCacheIfIndex_Object=MibTableColumn
mgmdRouterCacheIfIndex=_MgmdRouterCacheIfIndex_Object((1,3,6,1,4,1,171,12,18,1,6,1,2),_MgmdRouterCacheIfIndex_Type())
mgmdRouterCacheIfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:mgmdRouterCacheIfIndex.setStatus(_A)
_MgmdRouterCacheAddress_Type=InetAddress
_MgmdRouterCacheAddress_Object=MibTableColumn
mgmdRouterCacheAddress=_MgmdRouterCacheAddress_Object((1,3,6,1,4,1,171,12,18,1,6,1,3),_MgmdRouterCacheAddress_Type())
mgmdRouterCacheAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:mgmdRouterCacheAddress.setStatus(_A)
_MgmdRouterCacheLastReporter_Type=InetAddress
_MgmdRouterCacheLastReporter_Object=MibTableColumn
mgmdRouterCacheLastReporter=_MgmdRouterCacheLastReporter_Object((1,3,6,1,4,1,171,12,18,1,6,1,4),_MgmdRouterCacheLastReporter_Type())
mgmdRouterCacheLastReporter.setMaxAccess(_B)
if mibBuilder.loadTexts:mgmdRouterCacheLastReporter.setStatus(_A)
_MgmdRouterCacheExpiryTime_Type=TimeTicks
_MgmdRouterCacheExpiryTime_Object=MibTableColumn
mgmdRouterCacheExpiryTime=_MgmdRouterCacheExpiryTime_Object((1,3,6,1,4,1,171,12,18,1,6,1,6),_MgmdRouterCacheExpiryTime_Type())
mgmdRouterCacheExpiryTime.setMaxAccess(_B)
if mibBuilder.loadTexts:mgmdRouterCacheExpiryTime.setStatus(_A)
_MgmdRouterCacheStatus_Type=RowStatus
_MgmdRouterCacheStatus_Object=MibTableColumn
mgmdRouterCacheStatus=_MgmdRouterCacheStatus_Object((1,3,6,1,4,1,171,12,18,1,6,1,7),_MgmdRouterCacheStatus_Type())
mgmdRouterCacheStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:mgmdRouterCacheStatus.setStatus(_A)
_MgmdRouterCacheVersion1HostTimer_Type=TimeTicks
_MgmdRouterCacheVersion1HostTimer_Object=MibTableColumn
mgmdRouterCacheVersion1HostTimer=_MgmdRouterCacheVersion1HostTimer_Object((1,3,6,1,4,1,171,12,18,1,6,1,8),_MgmdRouterCacheVersion1HostTimer_Type())
mgmdRouterCacheVersion1HostTimer.setMaxAccess(_B)
if mibBuilder.loadTexts:mgmdRouterCacheVersion1HostTimer.setStatus(_A)
_MgmdRouterCacheVersion2HostTimer_Type=TimeTicks
_MgmdRouterCacheVersion2HostTimer_Object=MibTableColumn
mgmdRouterCacheVersion2HostTimer=_MgmdRouterCacheVersion2HostTimer_Object((1,3,6,1,4,1,171,12,18,1,6,1,9),_MgmdRouterCacheVersion2HostTimer_Type())
mgmdRouterCacheVersion2HostTimer.setMaxAccess(_B)
if mibBuilder.loadTexts:mgmdRouterCacheVersion2HostTimer.setStatus(_A)
class _MgmdRouterCacheSourceFilterMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('include',1),('exclude',2)))
_MgmdRouterCacheSourceFilterMode_Type.__name__=_G
_MgmdRouterCacheSourceFilterMode_Object=MibTableColumn
mgmdRouterCacheSourceFilterMode=_MgmdRouterCacheSourceFilterMode_Object((1,3,6,1,4,1,171,12,18,1,6,1,10),_MgmdRouterCacheSourceFilterMode_Type())
mgmdRouterCacheSourceFilterMode.setMaxAccess(_B)
if mibBuilder.loadTexts:mgmdRouterCacheSourceFilterMode.setStatus(_A)
_MgmdRouterSrcListTable_Object=MibTable
mgmdRouterSrcListTable=_MgmdRouterSrcListTable_Object((1,3,6,1,4,1,171,12,18,1,10))
if mibBuilder.loadTexts:mgmdRouterSrcListTable.setStatus(_A)
_MgmdRouterSrcListEntry_Object=MibTableRow
mgmdRouterSrcListEntry=_MgmdRouterSrcListEntry_Object((1,3,6,1,4,1,171,12,18,1,10,1))
mgmdRouterSrcListEntry.setIndexNames((0,_C,_N),(0,_C,_O),(0,_C,_P),(0,_C,_Q))
if mibBuilder.loadTexts:mgmdRouterSrcListEntry.setStatus(_A)
_MgmdRouterSrcListAddressType_Type=InetAddressType
_MgmdRouterSrcListAddressType_Object=MibTableColumn
mgmdRouterSrcListAddressType=_MgmdRouterSrcListAddressType_Object((1,3,6,1,4,1,171,12,18,1,10,1,1),_MgmdRouterSrcListAddressType_Type())
mgmdRouterSrcListAddressType.setMaxAccess(_B)
if mibBuilder.loadTexts:mgmdRouterSrcListAddressType.setStatus(_A)
_MgmdRouterSrcListIfIndex_Type=InterfaceIndex
_MgmdRouterSrcListIfIndex_Object=MibTableColumn
mgmdRouterSrcListIfIndex=_MgmdRouterSrcListIfIndex_Object((1,3,6,1,4,1,171,12,18,1,10,1,2),_MgmdRouterSrcListIfIndex_Type())
mgmdRouterSrcListIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:mgmdRouterSrcListIfIndex.setStatus(_A)
_MgmdRouterSrcListAddress_Type=InetAddress
_MgmdRouterSrcListAddress_Object=MibTableColumn
mgmdRouterSrcListAddress=_MgmdRouterSrcListAddress_Object((1,3,6,1,4,1,171,12,18,1,10,1,3),_MgmdRouterSrcListAddress_Type())
mgmdRouterSrcListAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:mgmdRouterSrcListAddress.setStatus(_A)
_MgmdRouterSrcListHostAddress_Type=InetAddress
_MgmdRouterSrcListHostAddress_Object=MibTableColumn
mgmdRouterSrcListHostAddress=_MgmdRouterSrcListHostAddress_Object((1,3,6,1,4,1,171,12,18,1,10,1,4),_MgmdRouterSrcListHostAddress_Type())
mgmdRouterSrcListHostAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:mgmdRouterSrcListHostAddress.setStatus(_A)
_MgmdRouterSrcListExpire_Type=TimeTicks
_MgmdRouterSrcListExpire_Object=MibTableColumn
mgmdRouterSrcListExpire=_MgmdRouterSrcListExpire_Object((1,3,6,1,4,1,171,12,18,1,10,1,5),_MgmdRouterSrcListExpire_Type())
mgmdRouterSrcListExpire.setMaxAccess(_B)
if mibBuilder.loadTexts:mgmdRouterSrcListExpire.setStatus(_A)
_MgmdRouterChkSubSrcNetTable_Object=MibTable
mgmdRouterChkSubSrcNetTable=_MgmdRouterChkSubSrcNetTable_Object((1,3,6,1,4,1,171,12,18,1,11))
if mibBuilder.loadTexts:mgmdRouterChkSubSrcNetTable.setStatus(_A)
_MgmdRouterChkSubSrcNetEntry_Object=MibTableRow
mgmdRouterChkSubSrcNetEntry=_MgmdRouterChkSubSrcNetEntry_Object((1,3,6,1,4,1,171,12,18,1,11,1))
mgmdRouterChkSubSrcNetEntry.setIndexNames((0,_C,_R))
if mibBuilder.loadTexts:mgmdRouterChkSubSrcNetEntry.setStatus(_A)
_MgmdRouterChkSubSrcNetIfIndex_Type=InterfaceIndex
_MgmdRouterChkSubSrcNetIfIndex_Object=MibTableColumn
mgmdRouterChkSubSrcNetIfIndex=_MgmdRouterChkSubSrcNetIfIndex_Object((1,3,6,1,4,1,171,12,18,1,11,1,1),_MgmdRouterChkSubSrcNetIfIndex_Type())
mgmdRouterChkSubSrcNetIfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:mgmdRouterChkSubSrcNetIfIndex.setStatus(_A)
_MgmdRouterChkSubSrcNetIpAddr_Type=IpAddress
_MgmdRouterChkSubSrcNetIpAddr_Object=MibTableColumn
mgmdRouterChkSubSrcNetIpAddr=_MgmdRouterChkSubSrcNetIpAddr_Object((1,3,6,1,4,1,171,12,18,1,11,1,2),_MgmdRouterChkSubSrcNetIpAddr_Type())
mgmdRouterChkSubSrcNetIpAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:mgmdRouterChkSubSrcNetIpAddr.setStatus(_A)
_MgmdRouterChkSubSrcNetIpNetMask_Type=IpAddress
_MgmdRouterChkSubSrcNetIpNetMask_Object=MibTableColumn
mgmdRouterChkSubSrcNetIpNetMask=_MgmdRouterChkSubSrcNetIpNetMask_Object((1,3,6,1,4,1,171,12,18,1,11,1,3),_MgmdRouterChkSubSrcNetIpNetMask_Type())
mgmdRouterChkSubSrcNetIpNetMask.setMaxAccess(_B)
if mibBuilder.loadTexts:mgmdRouterChkSubSrcNetIpNetMask.setStatus(_A)
class _MgmdRouterChkSubSrcNetState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
_MgmdRouterChkSubSrcNetState_Type.__name__=_G
_MgmdRouterChkSubSrcNetState_Object=MibTableColumn
mgmdRouterChkSubSrcNetState=_MgmdRouterChkSubSrcNetState_Object((1,3,6,1,4,1,171,12,18,1,11,1,4),_MgmdRouterChkSubSrcNetState_Type())
mgmdRouterChkSubSrcNetState.setMaxAccess('read-write')
if mibBuilder.loadTexts:mgmdRouterChkSubSrcNetState.setStatus(_A)
_MgmdRouterIGMPStaticGroupTable_Object=MibTable
mgmdRouterIGMPStaticGroupTable=_MgmdRouterIGMPStaticGroupTable_Object((1,3,6,1,4,1,171,12,18,1,12))
if mibBuilder.loadTexts:mgmdRouterIGMPStaticGroupTable.setStatus(_A)
_MgmdRouterIGMPStaticGroupEntry_Object=MibTableRow
mgmdRouterIGMPStaticGroupEntry=_MgmdRouterIGMPStaticGroupEntry_Object((1,3,6,1,4,1,171,12,18,1,12,1))
mgmdRouterIGMPStaticGroupEntry.setIndexNames((0,_C,_S),(0,_C,_T))
if mibBuilder.loadTexts:mgmdRouterIGMPStaticGroupEntry.setStatus(_A)
_MgmdRouterIGMPStaticGroupIfIndex_Type=InterfaceIndex
_MgmdRouterIGMPStaticGroupIfIndex_Object=MibTableColumn
mgmdRouterIGMPStaticGroupIfIndex=_MgmdRouterIGMPStaticGroupIfIndex_Object((1,3,6,1,4,1,171,12,18,1,12,1,1),_MgmdRouterIGMPStaticGroupIfIndex_Type())
mgmdRouterIGMPStaticGroupIfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:mgmdRouterIGMPStaticGroupIfIndex.setStatus(_A)
_MgmdRouterIGMPStaticGroupIpAddr_Type=IpAddress
_MgmdRouterIGMPStaticGroupIpAddr_Object=MibTableColumn
mgmdRouterIGMPStaticGroupIpAddr=_MgmdRouterIGMPStaticGroupIpAddr_Object((1,3,6,1,4,1,171,12,18,1,12,1,2),_MgmdRouterIGMPStaticGroupIpAddr_Type())
mgmdRouterIGMPStaticGroupIpAddr.setMaxAccess(_E)
if mibBuilder.loadTexts:mgmdRouterIGMPStaticGroupIpAddr.setStatus(_A)
_MgmdRouterIGMPStaticGroupRowStatus_Type=RowStatus
_MgmdRouterIGMPStaticGroupRowStatus_Object=MibTableColumn
mgmdRouterIGMPStaticGroupRowStatus=_MgmdRouterIGMPStaticGroupRowStatus_Object((1,3,6,1,4,1,171,12,18,1,12,1,3),_MgmdRouterIGMPStaticGroupRowStatus_Type())
mgmdRouterIGMPStaticGroupRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:mgmdRouterIGMPStaticGroupRowStatus.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'swIgmpMIB':swIgmpMIB,'swIgmpMIBObjects':swIgmpMIBObjects,'mgmdRouterInterfaceTable':mgmdRouterInterfaceTable,'mgmdRouterInterfaceEntry':mgmdRouterInterfaceEntry,_H:mgmdRouterInterfaceIfIndex,_I:mgmdRouterInterfaceQuerierType,'mgmdRouterInterfaceQuerier':mgmdRouterInterfaceQuerier,'mgmdRouterInterfaceQueryInterval':mgmdRouterInterfaceQueryInterval,'mgmdRouterInterfaceStatus':mgmdRouterInterfaceStatus,'mgmdRouterInterfaceVersion':mgmdRouterInterfaceVersion,'mgmdRouterInterfaceQueryMaxResponseTime':mgmdRouterInterfaceQueryMaxResponseTime,'mgmdRouterInterfaceQuerierUpTime':mgmdRouterInterfaceQuerierUpTime,'mgmdRouterInterfaceQuerierExpiryTime':mgmdRouterInterfaceQuerierExpiryTime,'mgmdRouterInterfaceRobustness':mgmdRouterInterfaceRobustness,'mgmdRouterInterfaceLastMembQueryIntvl':mgmdRouterInterfaceLastMembQueryIntvl,'mgmdRouterCacheTable':mgmdRouterCacheTable,'mgmdRouterCacheEntry':mgmdRouterCacheEntry,_K:mgmdRouterCacheAddressType,_L:mgmdRouterCacheIfIndex,_M:mgmdRouterCacheAddress,'mgmdRouterCacheLastReporter':mgmdRouterCacheLastReporter,'mgmdRouterCacheExpiryTime':mgmdRouterCacheExpiryTime,'mgmdRouterCacheStatus':mgmdRouterCacheStatus,'mgmdRouterCacheVersion1HostTimer':mgmdRouterCacheVersion1HostTimer,'mgmdRouterCacheVersion2HostTimer':mgmdRouterCacheVersion2HostTimer,'mgmdRouterCacheSourceFilterMode':mgmdRouterCacheSourceFilterMode,'mgmdRouterSrcListTable':mgmdRouterSrcListTable,'mgmdRouterSrcListEntry':mgmdRouterSrcListEntry,_N:mgmdRouterSrcListAddressType,_O:mgmdRouterSrcListIfIndex,_P:mgmdRouterSrcListAddress,_Q:mgmdRouterSrcListHostAddress,'mgmdRouterSrcListExpire':mgmdRouterSrcListExpire,'mgmdRouterChkSubSrcNetTable':mgmdRouterChkSubSrcNetTable,'mgmdRouterChkSubSrcNetEntry':mgmdRouterChkSubSrcNetEntry,_R:mgmdRouterChkSubSrcNetIfIndex,'mgmdRouterChkSubSrcNetIpAddr':mgmdRouterChkSubSrcNetIpAddr,'mgmdRouterChkSubSrcNetIpNetMask':mgmdRouterChkSubSrcNetIpNetMask,'mgmdRouterChkSubSrcNetState':mgmdRouterChkSubSrcNetState,'mgmdRouterIGMPStaticGroupTable':mgmdRouterIGMPStaticGroupTable,'mgmdRouterIGMPStaticGroupEntry':mgmdRouterIGMPStaticGroupEntry,_S:mgmdRouterIGMPStaticGroupIfIndex,_T:mgmdRouterIGMPStaticGroupIpAddr,'mgmdRouterIGMPStaticGroupRowStatus':mgmdRouterIGMPStaticGroupRowStatus})