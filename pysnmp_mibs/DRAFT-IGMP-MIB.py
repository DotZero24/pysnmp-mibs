_i='igmpV2RouterMIBGroup'
_h='igmpV2HostMIBGroup'
_g='igmpInterfaceProxyIfIndex'
_f='igmpCacheVersion1HostTimer'
_e='igmpInterfaceLastMembQueryIntvl'
_d='igmpInterfaceWrongVersionQueries'
_c='igmpInterfaceRobustness'
_b='igmpInterfaceQueryMaxResponseTime'
_a='igmpInterfaceVersion'
_Z='igmpInterfaceVersion1QuerierTimer'
_Y='igmpInterfaceQueryInterval'
_X='igmpInterfaceQuerierExpiryTime'
_W='igmpInterfaceQuerierUpTime'
_V='igmpInterfaceGroups'
_U='igmpInterfaceJoins'
_T='igmpCacheExpiryTime'
_S='igmpCacheUpTime'
_R='igmpInterfaceStatus'
_Q='igmpCacheStatus'
_P='igmpCacheSelf'
_O='igmpCacheIfIndex'
_N='igmpCacheAddress'
_M='tenths of seconds'
_L='igmpInterfaceIfIndex'
_K='TruthValue'
_J='InterfaceIndexOrZero'
_I='igmpRouterMIBGroup'
_H='igmpInterfaceQuerier'
_G='igmpCacheLastReporter'
_F='not-accessible'
_E='igmpBaseMIBGroup'
_D='Integer32'
_C='read-only'
_B='DRAFT-IGMP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,InterfaceIndexOrZero=mibBuilder.importSymbols('IF-MIB','InterfaceIndex',_J)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,experimental,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','experimental','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention',_K)
igmpStdMIB=ModuleIdentity((1,3,6,1,3,59))
if mibBuilder.loadTexts:igmpStdMIB.setRevisions(('1999-09-17 12:00',))
_IgmpMIBObjects_ObjectIdentity=ObjectIdentity
igmpMIBObjects=_IgmpMIBObjects_ObjectIdentity((1,3,6,1,3,59,1))
_Igmp_ObjectIdentity=ObjectIdentity
igmp=_Igmp_ObjectIdentity((1,3,6,1,3,59,1,1))
_IgmpInterfaceTable_Object=MibTable
igmpInterfaceTable=_IgmpInterfaceTable_Object((1,3,6,1,3,59,1,1,1))
if mibBuilder.loadTexts:igmpInterfaceTable.setStatus(_A)
_IgmpInterfaceEntry_Object=MibTableRow
igmpInterfaceEntry=_IgmpInterfaceEntry_Object((1,3,6,1,3,59,1,1,1,1))
igmpInterfaceEntry.setIndexNames((0,_B,_L))
if mibBuilder.loadTexts:igmpInterfaceEntry.setStatus(_A)
_IgmpInterfaceIfIndex_Type=InterfaceIndex
_IgmpInterfaceIfIndex_Object=MibTableColumn
igmpInterfaceIfIndex=_IgmpInterfaceIfIndex_Object((1,3,6,1,3,59,1,1,1,1,1),_IgmpInterfaceIfIndex_Type())
igmpInterfaceIfIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:igmpInterfaceIfIndex.setStatus(_A)
class _IgmpInterfaceQueryInterval_Type(Integer32):defaultValue=125
_IgmpInterfaceQueryInterval_Type.__name__=_D
_IgmpInterfaceQueryInterval_Object=MibTableColumn
igmpInterfaceQueryInterval=_IgmpInterfaceQueryInterval_Object((1,3,6,1,3,59,1,1,1,1,2),_IgmpInterfaceQueryInterval_Type())
igmpInterfaceQueryInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:igmpInterfaceQueryInterval.setStatus(_A)
if mibBuilder.loadTexts:igmpInterfaceQueryInterval.setUnits('seconds')
_IgmpInterfaceStatus_Type=RowStatus
_IgmpInterfaceStatus_Object=MibTableColumn
igmpInterfaceStatus=_IgmpInterfaceStatus_Object((1,3,6,1,3,59,1,1,1,1,3),_IgmpInterfaceStatus_Type())
igmpInterfaceStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:igmpInterfaceStatus.setStatus(_A)
class _IgmpInterfaceVersion_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('version1',1),('version2',2)))
_IgmpInterfaceVersion_Type.__name__=_D
_IgmpInterfaceVersion_Object=MibTableColumn
igmpInterfaceVersion=_IgmpInterfaceVersion_Object((1,3,6,1,3,59,1,1,1,1,4),_IgmpInterfaceVersion_Type())
igmpInterfaceVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:igmpInterfaceVersion.setStatus(_A)
_IgmpInterfaceQuerier_Type=IpAddress
_IgmpInterfaceQuerier_Object=MibTableColumn
igmpInterfaceQuerier=_IgmpInterfaceQuerier_Object((1,3,6,1,3,59,1,1,1,1,5),_IgmpInterfaceQuerier_Type())
igmpInterfaceQuerier.setMaxAccess(_C)
if mibBuilder.loadTexts:igmpInterfaceQuerier.setStatus(_A)
class _IgmpInterfaceQueryMaxResponseTime_Type(Integer32):defaultValue=100
_IgmpInterfaceQueryMaxResponseTime_Type.__name__=_D
_IgmpInterfaceQueryMaxResponseTime_Object=MibTableColumn
igmpInterfaceQueryMaxResponseTime=_IgmpInterfaceQueryMaxResponseTime_Object((1,3,6,1,3,59,1,1,1,1,6),_IgmpInterfaceQueryMaxResponseTime_Type())
igmpInterfaceQueryMaxResponseTime.setMaxAccess(_C)
if mibBuilder.loadTexts:igmpInterfaceQueryMaxResponseTime.setStatus(_A)
if mibBuilder.loadTexts:igmpInterfaceQueryMaxResponseTime.setUnits(_M)
_IgmpInterfaceVersion1QuerierTimer_Type=TimeTicks
_IgmpInterfaceVersion1QuerierTimer_Object=MibTableColumn
igmpInterfaceVersion1QuerierTimer=_IgmpInterfaceVersion1QuerierTimer_Object((1,3,6,1,3,59,1,1,1,1,9),_IgmpInterfaceVersion1QuerierTimer_Type())
igmpInterfaceVersion1QuerierTimer.setMaxAccess(_C)
if mibBuilder.loadTexts:igmpInterfaceVersion1QuerierTimer.setStatus(_A)
_IgmpInterfaceWrongVersionQueries_Type=Counter32
_IgmpInterfaceWrongVersionQueries_Object=MibTableColumn
igmpInterfaceWrongVersionQueries=_IgmpInterfaceWrongVersionQueries_Object((1,3,6,1,3,59,1,1,1,1,10),_IgmpInterfaceWrongVersionQueries_Type())
igmpInterfaceWrongVersionQueries.setMaxAccess(_C)
if mibBuilder.loadTexts:igmpInterfaceWrongVersionQueries.setStatus(_A)
_IgmpInterfaceJoins_Type=Counter32
_IgmpInterfaceJoins_Object=MibTableColumn
igmpInterfaceJoins=_IgmpInterfaceJoins_Object((1,3,6,1,3,59,1,1,1,1,11),_IgmpInterfaceJoins_Type())
igmpInterfaceJoins.setMaxAccess(_C)
if mibBuilder.loadTexts:igmpInterfaceJoins.setStatus(_A)
_IgmpInterfaceGroups_Type=Gauge32
_IgmpInterfaceGroups_Object=MibTableColumn
igmpInterfaceGroups=_IgmpInterfaceGroups_Object((1,3,6,1,3,59,1,1,1,1,13),_IgmpInterfaceGroups_Type())
igmpInterfaceGroups.setMaxAccess(_C)
if mibBuilder.loadTexts:igmpInterfaceGroups.setStatus(_A)
class _IgmpInterfaceRobustness_Type(Integer32):defaultValue=2
_IgmpInterfaceRobustness_Type.__name__=_D
_IgmpInterfaceRobustness_Object=MibTableColumn
igmpInterfaceRobustness=_IgmpInterfaceRobustness_Object((1,3,6,1,3,59,1,1,1,1,14),_IgmpInterfaceRobustness_Type())
igmpInterfaceRobustness.setMaxAccess(_C)
if mibBuilder.loadTexts:igmpInterfaceRobustness.setStatus(_A)
class _IgmpInterfaceLastMembQueryIntvl_Type(Integer32):defaultValue=10
_IgmpInterfaceLastMembQueryIntvl_Type.__name__=_D
_IgmpInterfaceLastMembQueryIntvl_Object=MibTableColumn
igmpInterfaceLastMembQueryIntvl=_IgmpInterfaceLastMembQueryIntvl_Object((1,3,6,1,3,59,1,1,1,1,15),_IgmpInterfaceLastMembQueryIntvl_Type())
igmpInterfaceLastMembQueryIntvl.setMaxAccess(_C)
if mibBuilder.loadTexts:igmpInterfaceLastMembQueryIntvl.setStatus(_A)
if mibBuilder.loadTexts:igmpInterfaceLastMembQueryIntvl.setUnits(_M)
class _IgmpInterfaceProxyIfIndex_Type(InterfaceIndexOrZero):defaultValue=0
_IgmpInterfaceProxyIfIndex_Type.__name__=_J
_IgmpInterfaceProxyIfIndex_Object=MibTableColumn
igmpInterfaceProxyIfIndex=_IgmpInterfaceProxyIfIndex_Object((1,3,6,1,3,59,1,1,1,1,16),_IgmpInterfaceProxyIfIndex_Type())
igmpInterfaceProxyIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:igmpInterfaceProxyIfIndex.setStatus(_A)
_IgmpInterfaceQuerierUpTime_Type=TimeTicks
_IgmpInterfaceQuerierUpTime_Object=MibTableColumn
igmpInterfaceQuerierUpTime=_IgmpInterfaceQuerierUpTime_Object((1,3,6,1,3,59,1,1,1,1,17),_IgmpInterfaceQuerierUpTime_Type())
igmpInterfaceQuerierUpTime.setMaxAccess(_C)
if mibBuilder.loadTexts:igmpInterfaceQuerierUpTime.setStatus(_A)
_IgmpInterfaceQuerierExpiryTime_Type=TimeTicks
_IgmpInterfaceQuerierExpiryTime_Object=MibTableColumn
igmpInterfaceQuerierExpiryTime=_IgmpInterfaceQuerierExpiryTime_Object((1,3,6,1,3,59,1,1,1,1,18),_IgmpInterfaceQuerierExpiryTime_Type())
igmpInterfaceQuerierExpiryTime.setMaxAccess(_C)
if mibBuilder.loadTexts:igmpInterfaceQuerierExpiryTime.setStatus(_A)
_IgmpCacheTable_Object=MibTable
igmpCacheTable=_IgmpCacheTable_Object((1,3,6,1,3,59,1,1,2))
if mibBuilder.loadTexts:igmpCacheTable.setStatus(_A)
_IgmpCacheEntry_Object=MibTableRow
igmpCacheEntry=_IgmpCacheEntry_Object((1,3,6,1,3,59,1,1,2,1))
igmpCacheEntry.setIndexNames((0,_B,_N),(0,_B,_O))
if mibBuilder.loadTexts:igmpCacheEntry.setStatus(_A)
_IgmpCacheAddress_Type=IpAddress
_IgmpCacheAddress_Object=MibTableColumn
igmpCacheAddress=_IgmpCacheAddress_Object((1,3,6,1,3,59,1,1,2,1,1),_IgmpCacheAddress_Type())
igmpCacheAddress.setMaxAccess(_F)
if mibBuilder.loadTexts:igmpCacheAddress.setStatus(_A)
_IgmpCacheIfIndex_Type=InterfaceIndex
_IgmpCacheIfIndex_Object=MibTableColumn
igmpCacheIfIndex=_IgmpCacheIfIndex_Object((1,3,6,1,3,59,1,1,2,1,2),_IgmpCacheIfIndex_Type())
igmpCacheIfIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:igmpCacheIfIndex.setStatus(_A)
class _IgmpCacheSelf_Type(TruthValue):defaultValue=1
_IgmpCacheSelf_Type.__name__=_K
_IgmpCacheSelf_Object=MibTableColumn
igmpCacheSelf=_IgmpCacheSelf_Object((1,3,6,1,3,59,1,1,2,1,3),_IgmpCacheSelf_Type())
igmpCacheSelf.setMaxAccess(_C)
if mibBuilder.loadTexts:igmpCacheSelf.setStatus(_A)
_IgmpCacheLastReporter_Type=IpAddress
_IgmpCacheLastReporter_Object=MibTableColumn
igmpCacheLastReporter=_IgmpCacheLastReporter_Object((1,3,6,1,3,59,1,1,2,1,4),_IgmpCacheLastReporter_Type())
igmpCacheLastReporter.setMaxAccess(_C)
if mibBuilder.loadTexts:igmpCacheLastReporter.setStatus(_A)
_IgmpCacheUpTime_Type=TimeTicks
_IgmpCacheUpTime_Object=MibTableColumn
igmpCacheUpTime=_IgmpCacheUpTime_Object((1,3,6,1,3,59,1,1,2,1,5),_IgmpCacheUpTime_Type())
igmpCacheUpTime.setMaxAccess(_C)
if mibBuilder.loadTexts:igmpCacheUpTime.setStatus(_A)
_IgmpCacheExpiryTime_Type=TimeTicks
_IgmpCacheExpiryTime_Object=MibTableColumn
igmpCacheExpiryTime=_IgmpCacheExpiryTime_Object((1,3,6,1,3,59,1,1,2,1,6),_IgmpCacheExpiryTime_Type())
igmpCacheExpiryTime.setMaxAccess(_C)
if mibBuilder.loadTexts:igmpCacheExpiryTime.setStatus(_A)
_IgmpCacheStatus_Type=RowStatus
_IgmpCacheStatus_Object=MibTableColumn
igmpCacheStatus=_IgmpCacheStatus_Object((1,3,6,1,3,59,1,1,2,1,7),_IgmpCacheStatus_Type())
igmpCacheStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:igmpCacheStatus.setStatus(_A)
_IgmpCacheVersion1HostTimer_Type=TimeTicks
_IgmpCacheVersion1HostTimer_Object=MibTableColumn
igmpCacheVersion1HostTimer=_IgmpCacheVersion1HostTimer_Object((1,3,6,1,3,59,1,1,2,1,8),_IgmpCacheVersion1HostTimer_Type())
igmpCacheVersion1HostTimer.setMaxAccess(_C)
if mibBuilder.loadTexts:igmpCacheVersion1HostTimer.setStatus(_A)
_IgmpMIBConformance_ObjectIdentity=ObjectIdentity
igmpMIBConformance=_IgmpMIBConformance_ObjectIdentity((1,3,6,1,3,59,2))
_IgmpMIBCompliances_ObjectIdentity=ObjectIdentity
igmpMIBCompliances=_IgmpMIBCompliances_ObjectIdentity((1,3,6,1,3,59,2,1))
_IgmpMIBGroups_ObjectIdentity=ObjectIdentity
igmpMIBGroups=_IgmpMIBGroups_ObjectIdentity((1,3,6,1,3,59,2,2))
igmpBaseMIBGroup=ObjectGroup((1,3,6,1,3,59,2,2,1))
igmpBaseMIBGroup.setObjects(*((_B,_P),(_B,_Q),(_B,_R)))
if mibBuilder.loadTexts:igmpBaseMIBGroup.setStatus(_A)
igmpRouterMIBGroup=ObjectGroup((1,3,6,1,3,59,2,2,2))
igmpRouterMIBGroup.setObjects(*((_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_G),(_B,_W),(_B,_X),(_B,_Y)))
if mibBuilder.loadTexts:igmpRouterMIBGroup.setStatus(_A)
igmpV2HostMIBGroup=ObjectGroup((1,3,6,1,3,59,2,2,3))
igmpV2HostMIBGroup.setObjects((_B,_Z))
if mibBuilder.loadTexts:igmpV2HostMIBGroup.setStatus(_A)
igmpHostOptMIBGroup=ObjectGroup((1,3,6,1,3,59,2,2,4))
igmpHostOptMIBGroup.setObjects(*((_B,_G),(_B,_H)))
if mibBuilder.loadTexts:igmpHostOptMIBGroup.setStatus(_A)
igmpV2RouterMIBGroup=ObjectGroup((1,3,6,1,3,59,2,2,5))
igmpV2RouterMIBGroup.setObjects(*((_B,_a),(_B,_H),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f)))
if mibBuilder.loadTexts:igmpV2RouterMIBGroup.setStatus(_A)
igmpV2ProxyMIBGroup=ObjectGroup((1,3,6,1,3,59,2,2,6))
igmpV2ProxyMIBGroup.setObjects((_B,_g))
if mibBuilder.loadTexts:igmpV2ProxyMIBGroup.setStatus(_A)
igmpV1HostMIBCompliance=ModuleCompliance((1,3,6,1,3,59,2,1,1))
igmpV1HostMIBCompliance.setObjects((_B,_E))
if mibBuilder.loadTexts:igmpV1HostMIBCompliance.setStatus(_A)
igmpV1RouterMIBCompliance=ModuleCompliance((1,3,6,1,3,59,2,1,2))
igmpV1RouterMIBCompliance.setObjects(*((_B,_E),(_B,_I)))
if mibBuilder.loadTexts:igmpV1RouterMIBCompliance.setStatus(_A)
igmpV2HostMIBCompliance=ModuleCompliance((1,3,6,1,3,59,2,1,3))
igmpV2HostMIBCompliance.setObjects(*((_B,_E),(_B,_h)))
if mibBuilder.loadTexts:igmpV2HostMIBCompliance.setStatus(_A)
igmpV2RouterMIBCompliance=ModuleCompliance((1,3,6,1,3,59,2,1,4))
igmpV2RouterMIBCompliance.setObjects(*((_B,_E),(_B,_I),(_B,_i)))
if mibBuilder.loadTexts:igmpV2RouterMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'igmpStdMIB':igmpStdMIB,'igmpMIBObjects':igmpMIBObjects,'igmp':igmp,'igmpInterfaceTable':igmpInterfaceTable,'igmpInterfaceEntry':igmpInterfaceEntry,_L:igmpInterfaceIfIndex,_Y:igmpInterfaceQueryInterval,_R:igmpInterfaceStatus,_a:igmpInterfaceVersion,_H:igmpInterfaceQuerier,_b:igmpInterfaceQueryMaxResponseTime,_Z:igmpInterfaceVersion1QuerierTimer,_d:igmpInterfaceWrongVersionQueries,_U:igmpInterfaceJoins,_V:igmpInterfaceGroups,_c:igmpInterfaceRobustness,_e:igmpInterfaceLastMembQueryIntvl,_g:igmpInterfaceProxyIfIndex,_W:igmpInterfaceQuerierUpTime,_X:igmpInterfaceQuerierExpiryTime,'igmpCacheTable':igmpCacheTable,'igmpCacheEntry':igmpCacheEntry,_N:igmpCacheAddress,_O:igmpCacheIfIndex,_P:igmpCacheSelf,_G:igmpCacheLastReporter,_S:igmpCacheUpTime,_T:igmpCacheExpiryTime,_Q:igmpCacheStatus,_f:igmpCacheVersion1HostTimer,'igmpMIBConformance':igmpMIBConformance,'igmpMIBCompliances':igmpMIBCompliances,'igmpV1HostMIBCompliance':igmpV1HostMIBCompliance,'igmpV1RouterMIBCompliance':igmpV1RouterMIBCompliance,'igmpV2HostMIBCompliance':igmpV2HostMIBCompliance,'igmpV2RouterMIBCompliance':igmpV2RouterMIBCompliance,'igmpMIBGroups':igmpMIBGroups,_E:igmpBaseMIBGroup,_I:igmpRouterMIBGroup,_h:igmpV2HostMIBGroup,'igmpHostOptMIBGroup':igmpHostOptMIBGroup,_i:igmpV2RouterMIBGroup,'igmpV2ProxyMIBGroup':igmpV2ProxyMIBGroup})