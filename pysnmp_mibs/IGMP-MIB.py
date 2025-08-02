_i='igmpV2RouterMIBGroup'
_h='igmpV2HostMIBGroup'
_g='igmpInterfaceGroups'
_f='igmpInterfaceRobustness'
_e='igmpInterfaceLeaves'
_d='igmpInterfaceLeaveEnabled'
_c='igmpInterfaceQuerierPresentTimeout'
_b='igmpInterfaceVersion1QuerierTimer'
_a='igmpInterfaceQueryInterval'
_Z='igmpCacheExpiryTime'
_Y='igmpCacheUpTime'
_X='igmpInterfaceStatus'
_W='igmpCacheStatus'
_V='igmpCacheLastReporter'
_U='igmpCacheSelf'
_T='igmpCacheIfIndex'
_S='igmpCacheAddress'
_R='igmpInterfaceIfIndex'
_Q='igmpRouterMIBGroup'
_P='igmpCacheVersion1HostTimer'
_O='igmpInterfaceJoins'
_N='igmpInterfaceWrongVersionQueries'
_M='igmpInterfaceQueryMaxResponseTime'
_L='igmpInterfaceVersion'
_K='igmpInterfaceQuerier'
_J='not-accessible'
_I='TruthValue'
_H='deprecated'
_G='igmpBaseMIBGroup'
_F='seconds'
_E='Integer32'
_D='read-create'
_C='read-only'
_B='current'
_A='IGMP-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,experimental,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','experimental','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention',_I)
igmpMIB=ModuleIdentity((1,3,6,1,3,59))
if mibBuilder.loadTexts:igmpMIB.setRevisions(('1995-08-15 00:00','1997-01-06 00:00','1997-12-18 00:00'))
_IgmpMIBObjects_ObjectIdentity=ObjectIdentity
igmpMIBObjects=_IgmpMIBObjects_ObjectIdentity((1,3,6,1,3,59,1))
_Igmp_ObjectIdentity=ObjectIdentity
igmp=_Igmp_ObjectIdentity((1,3,6,1,3,59,1,1))
_IgmpInterfaceTable_Object=MibTable
igmpInterfaceTable=_IgmpInterfaceTable_Object((1,3,6,1,3,59,1,1,1))
if mibBuilder.loadTexts:igmpInterfaceTable.setStatus(_B)
_IgmpInterfaceEntry_Object=MibTableRow
igmpInterfaceEntry=_IgmpInterfaceEntry_Object((1,3,6,1,3,59,1,1,1,1))
igmpInterfaceEntry.setIndexNames((0,_A,_R))
if mibBuilder.loadTexts:igmpInterfaceEntry.setStatus(_B)
class _IgmpInterfaceIfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_IgmpInterfaceIfIndex_Type.__name__=_E
_IgmpInterfaceIfIndex_Object=MibTableColumn
igmpInterfaceIfIndex=_IgmpInterfaceIfIndex_Object((1,3,6,1,3,59,1,1,1,1,1),_IgmpInterfaceIfIndex_Type())
igmpInterfaceIfIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:igmpInterfaceIfIndex.setStatus(_B)
class _IgmpInterfaceQueryInterval_Type(Integer32):defaultValue=60
_IgmpInterfaceQueryInterval_Type.__name__=_E
_IgmpInterfaceQueryInterval_Object=MibTableColumn
igmpInterfaceQueryInterval=_IgmpInterfaceQueryInterval_Object((1,3,6,1,3,59,1,1,1,1,2),_IgmpInterfaceQueryInterval_Type())
igmpInterfaceQueryInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:igmpInterfaceQueryInterval.setStatus(_B)
if mibBuilder.loadTexts:igmpInterfaceQueryInterval.setUnits(_F)
_IgmpInterfaceStatus_Type=RowStatus
_IgmpInterfaceStatus_Object=MibTableColumn
igmpInterfaceStatus=_IgmpInterfaceStatus_Object((1,3,6,1,3,59,1,1,1,1,3),_IgmpInterfaceStatus_Type())
igmpInterfaceStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:igmpInterfaceStatus.setStatus(_B)
class _IgmpInterfaceVersion_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('version1',1),('version2',2)))
_IgmpInterfaceVersion_Type.__name__=_E
_IgmpInterfaceVersion_Object=MibTableColumn
igmpInterfaceVersion=_IgmpInterfaceVersion_Object((1,3,6,1,3,59,1,1,1,1,4),_IgmpInterfaceVersion_Type())
igmpInterfaceVersion.setMaxAccess(_D)
if mibBuilder.loadTexts:igmpInterfaceVersion.setStatus(_B)
_IgmpInterfaceQuerier_Type=IpAddress
_IgmpInterfaceQuerier_Object=MibTableColumn
igmpInterfaceQuerier=_IgmpInterfaceQuerier_Object((1,3,6,1,3,59,1,1,1,1,5),_IgmpInterfaceQuerier_Type())
igmpInterfaceQuerier.setMaxAccess(_C)
if mibBuilder.loadTexts:igmpInterfaceQuerier.setStatus(_B)
class _IgmpInterfaceQueryMaxResponseTime_Type(Integer32):defaultValue=10
_IgmpInterfaceQueryMaxResponseTime_Type.__name__=_E
_IgmpInterfaceQueryMaxResponseTime_Object=MibTableColumn
igmpInterfaceQueryMaxResponseTime=_IgmpInterfaceQueryMaxResponseTime_Object((1,3,6,1,3,59,1,1,1,1,6),_IgmpInterfaceQueryMaxResponseTime_Type())
igmpInterfaceQueryMaxResponseTime.setMaxAccess(_D)
if mibBuilder.loadTexts:igmpInterfaceQueryMaxResponseTime.setStatus(_B)
if mibBuilder.loadTexts:igmpInterfaceQueryMaxResponseTime.setUnits(_F)
class _IgmpInterfaceQuerierPresentTimeout_Type(Integer32):defaultValue=255
_IgmpInterfaceQuerierPresentTimeout_Type.__name__=_E
_IgmpInterfaceQuerierPresentTimeout_Object=MibTableColumn
igmpInterfaceQuerierPresentTimeout=_IgmpInterfaceQuerierPresentTimeout_Object((1,3,6,1,3,59,1,1,1,1,7),_IgmpInterfaceQuerierPresentTimeout_Type())
igmpInterfaceQuerierPresentTimeout.setMaxAccess(_D)
if mibBuilder.loadTexts:igmpInterfaceQuerierPresentTimeout.setStatus(_H)
if mibBuilder.loadTexts:igmpInterfaceQuerierPresentTimeout.setUnits(_F)
class _IgmpInterfaceLeaveEnabled_Type(TruthValue):defaultValue=1
_IgmpInterfaceLeaveEnabled_Type.__name__=_I
_IgmpInterfaceLeaveEnabled_Object=MibTableColumn
igmpInterfaceLeaveEnabled=_IgmpInterfaceLeaveEnabled_Object((1,3,6,1,3,59,1,1,1,1,8),_IgmpInterfaceLeaveEnabled_Type())
igmpInterfaceLeaveEnabled.setMaxAccess(_D)
if mibBuilder.loadTexts:igmpInterfaceLeaveEnabled.setStatus(_H)
_IgmpInterfaceVersion1QuerierTimer_Type=Integer32
_IgmpInterfaceVersion1QuerierTimer_Object=MibTableColumn
igmpInterfaceVersion1QuerierTimer=_IgmpInterfaceVersion1QuerierTimer_Object((1,3,6,1,3,59,1,1,1,1,9),_IgmpInterfaceVersion1QuerierTimer_Type())
igmpInterfaceVersion1QuerierTimer.setMaxAccess(_C)
if mibBuilder.loadTexts:igmpInterfaceVersion1QuerierTimer.setStatus(_B)
if mibBuilder.loadTexts:igmpInterfaceVersion1QuerierTimer.setUnits(_F)
_IgmpInterfaceWrongVersionQueries_Type=Counter32
_IgmpInterfaceWrongVersionQueries_Object=MibTableColumn
igmpInterfaceWrongVersionQueries=_IgmpInterfaceWrongVersionQueries_Object((1,3,6,1,3,59,1,1,1,1,10),_IgmpInterfaceWrongVersionQueries_Type())
igmpInterfaceWrongVersionQueries.setMaxAccess(_C)
if mibBuilder.loadTexts:igmpInterfaceWrongVersionQueries.setStatus(_B)
_IgmpInterfaceJoins_Type=Counter32
_IgmpInterfaceJoins_Object=MibTableColumn
igmpInterfaceJoins=_IgmpInterfaceJoins_Object((1,3,6,1,3,59,1,1,1,1,11),_IgmpInterfaceJoins_Type())
igmpInterfaceJoins.setMaxAccess(_C)
if mibBuilder.loadTexts:igmpInterfaceJoins.setStatus(_B)
_IgmpInterfaceLeaves_Type=Counter32
_IgmpInterfaceLeaves_Object=MibTableColumn
igmpInterfaceLeaves=_IgmpInterfaceLeaves_Object((1,3,6,1,3,59,1,1,1,1,12),_IgmpInterfaceLeaves_Type())
igmpInterfaceLeaves.setMaxAccess(_C)
if mibBuilder.loadTexts:igmpInterfaceLeaves.setStatus(_H)
_IgmpInterfaceGroups_Type=Gauge32
_IgmpInterfaceGroups_Object=MibTableColumn
igmpInterfaceGroups=_IgmpInterfaceGroups_Object((1,3,6,1,3,59,1,1,1,1,13),_IgmpInterfaceGroups_Type())
igmpInterfaceGroups.setMaxAccess(_C)
if mibBuilder.loadTexts:igmpInterfaceGroups.setStatus(_B)
class _IgmpInterfaceRobustness_Type(Integer32):defaultValue=2
_IgmpInterfaceRobustness_Type.__name__=_E
_IgmpInterfaceRobustness_Object=MibTableColumn
igmpInterfaceRobustness=_IgmpInterfaceRobustness_Object((1,3,6,1,3,59,1,1,1,1,14),_IgmpInterfaceRobustness_Type())
igmpInterfaceRobustness.setMaxAccess(_D)
if mibBuilder.loadTexts:igmpInterfaceRobustness.setStatus(_B)
_IgmpCacheTable_Object=MibTable
igmpCacheTable=_IgmpCacheTable_Object((1,3,6,1,3,59,1,1,2))
if mibBuilder.loadTexts:igmpCacheTable.setStatus(_B)
_IgmpCacheEntry_Object=MibTableRow
igmpCacheEntry=_IgmpCacheEntry_Object((1,3,6,1,3,59,1,1,2,1))
igmpCacheEntry.setIndexNames((0,_A,_S),(0,_A,_T))
if mibBuilder.loadTexts:igmpCacheEntry.setStatus(_B)
_IgmpCacheAddress_Type=IpAddress
_IgmpCacheAddress_Object=MibTableColumn
igmpCacheAddress=_IgmpCacheAddress_Object((1,3,6,1,3,59,1,1,2,1,1),_IgmpCacheAddress_Type())
igmpCacheAddress.setMaxAccess(_J)
if mibBuilder.loadTexts:igmpCacheAddress.setStatus(_B)
class _IgmpCacheIfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_IgmpCacheIfIndex_Type.__name__=_E
_IgmpCacheIfIndex_Object=MibTableColumn
igmpCacheIfIndex=_IgmpCacheIfIndex_Object((1,3,6,1,3,59,1,1,2,1,2),_IgmpCacheIfIndex_Type())
igmpCacheIfIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:igmpCacheIfIndex.setStatus(_B)
class _IgmpCacheSelf_Type(TruthValue):defaultValue=1
_IgmpCacheSelf_Type.__name__=_I
_IgmpCacheSelf_Object=MibTableColumn
igmpCacheSelf=_IgmpCacheSelf_Object((1,3,6,1,3,59,1,1,2,1,3),_IgmpCacheSelf_Type())
igmpCacheSelf.setMaxAccess(_D)
if mibBuilder.loadTexts:igmpCacheSelf.setStatus(_B)
_IgmpCacheLastReporter_Type=IpAddress
_IgmpCacheLastReporter_Object=MibTableColumn
igmpCacheLastReporter=_IgmpCacheLastReporter_Object((1,3,6,1,3,59,1,1,2,1,4),_IgmpCacheLastReporter_Type())
igmpCacheLastReporter.setMaxAccess(_C)
if mibBuilder.loadTexts:igmpCacheLastReporter.setStatus(_B)
_IgmpCacheUpTime_Type=TimeTicks
_IgmpCacheUpTime_Object=MibTableColumn
igmpCacheUpTime=_IgmpCacheUpTime_Object((1,3,6,1,3,59,1,1,2,1,5),_IgmpCacheUpTime_Type())
igmpCacheUpTime.setMaxAccess(_C)
if mibBuilder.loadTexts:igmpCacheUpTime.setStatus(_B)
_IgmpCacheExpiryTime_Type=TimeTicks
_IgmpCacheExpiryTime_Object=MibTableColumn
igmpCacheExpiryTime=_IgmpCacheExpiryTime_Object((1,3,6,1,3,59,1,1,2,1,6),_IgmpCacheExpiryTime_Type())
igmpCacheExpiryTime.setMaxAccess(_C)
if mibBuilder.loadTexts:igmpCacheExpiryTime.setStatus(_B)
_IgmpCacheStatus_Type=RowStatus
_IgmpCacheStatus_Object=MibTableColumn
igmpCacheStatus=_IgmpCacheStatus_Object((1,3,6,1,3,59,1,1,2,1,7),_IgmpCacheStatus_Type())
igmpCacheStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:igmpCacheStatus.setStatus(_B)
_IgmpCacheVersion1HostTimer_Type=Integer32
_IgmpCacheVersion1HostTimer_Object=MibTableColumn
igmpCacheVersion1HostTimer=_IgmpCacheVersion1HostTimer_Object((1,3,6,1,3,59,1,1,2,1,8),_IgmpCacheVersion1HostTimer_Type())
igmpCacheVersion1HostTimer.setMaxAccess(_C)
if mibBuilder.loadTexts:igmpCacheVersion1HostTimer.setStatus(_B)
if mibBuilder.loadTexts:igmpCacheVersion1HostTimer.setUnits(_F)
_IgmpMIBConformance_ObjectIdentity=ObjectIdentity
igmpMIBConformance=_IgmpMIBConformance_ObjectIdentity((1,3,6,1,3,59,2))
_IgmpMIBCompliances_ObjectIdentity=ObjectIdentity
igmpMIBCompliances=_IgmpMIBCompliances_ObjectIdentity((1,3,6,1,3,59,2,1))
_IgmpMIBGroups_ObjectIdentity=ObjectIdentity
igmpMIBGroups=_IgmpMIBGroups_ObjectIdentity((1,3,6,1,3,59,2,2))
igmpBaseMIBGroup=ObjectGroup((1,3,6,1,3,59,2,2,1))
igmpBaseMIBGroup.setObjects(*((_A,_U),(_A,_V),(_A,_W),(_A,_X)))
if mibBuilder.loadTexts:igmpBaseMIBGroup.setStatus(_B)
igmpRouterMIBGroup=ObjectGroup((1,3,6,1,3,59,2,2,2))
igmpRouterMIBGroup.setObjects(*((_A,_Y),(_A,_Z),(_A,_a)))
if mibBuilder.loadTexts:igmpRouterMIBGroup.setStatus(_B)
igmpV2HostMIBGroup=ObjectGroup((1,3,6,1,3,59,2,2,3))
igmpV2HostMIBGroup.setObjects(*((_A,_K),(_A,_b)))
if mibBuilder.loadTexts:igmpV2HostMIBGroup.setStatus(_B)
igmpRouterVersion2MIBGroup=ObjectGroup((1,3,6,1,3,59,2,2,4))
igmpRouterVersion2MIBGroup.setObjects(*((_A,_L),(_A,_M),(_A,_c),(_A,_d),(_A,_N),(_A,_O),(_A,_e),(_A,_P)))
if mibBuilder.loadTexts:igmpRouterVersion2MIBGroup.setStatus(_H)
igmpV2RouterMIBGroup=ObjectGroup((1,3,6,1,3,59,2,2,5))
igmpV2RouterMIBGroup.setObjects(*((_A,_L),(_A,_K),(_A,_M),(_A,_f),(_A,_N),(_A,_O),(_A,_g),(_A,_P)))
if mibBuilder.loadTexts:igmpV2RouterMIBGroup.setStatus(_B)
igmpV1HostMIBCompliance=ModuleCompliance((1,3,6,1,3,59,2,1,1))
igmpV1HostMIBCompliance.setObjects((_A,_G))
if mibBuilder.loadTexts:igmpV1HostMIBCompliance.setStatus(_B)
igmpV1RouterMIBCompliance=ModuleCompliance((1,3,6,1,3,59,2,1,2))
igmpV1RouterMIBCompliance.setObjects(*((_A,_G),(_A,_Q)))
if mibBuilder.loadTexts:igmpV1RouterMIBCompliance.setStatus(_B)
igmpV2HostMIBCompliance=ModuleCompliance((1,3,6,1,3,59,2,1,3))
igmpV2HostMIBCompliance.setObjects(*((_A,_G),(_A,_h)))
if mibBuilder.loadTexts:igmpV2HostMIBCompliance.setStatus(_B)
igmpV2RouterMIBCompliance=ModuleCompliance((1,3,6,1,3,59,2,1,4))
igmpV2RouterMIBCompliance.setObjects(*((_A,_G),(_A,_Q),(_A,_i)))
if mibBuilder.loadTexts:igmpV2RouterMIBCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'igmpMIB':igmpMIB,'igmpMIBObjects':igmpMIBObjects,'igmp':igmp,'igmpInterfaceTable':igmpInterfaceTable,'igmpInterfaceEntry':igmpInterfaceEntry,_R:igmpInterfaceIfIndex,_a:igmpInterfaceQueryInterval,_X:igmpInterfaceStatus,_L:igmpInterfaceVersion,_K:igmpInterfaceQuerier,_M:igmpInterfaceQueryMaxResponseTime,_c:igmpInterfaceQuerierPresentTimeout,_d:igmpInterfaceLeaveEnabled,_b:igmpInterfaceVersion1QuerierTimer,_N:igmpInterfaceWrongVersionQueries,_O:igmpInterfaceJoins,_e:igmpInterfaceLeaves,_g:igmpInterfaceGroups,_f:igmpInterfaceRobustness,'igmpCacheTable':igmpCacheTable,'igmpCacheEntry':igmpCacheEntry,_S:igmpCacheAddress,_T:igmpCacheIfIndex,_U:igmpCacheSelf,_V:igmpCacheLastReporter,_Y:igmpCacheUpTime,_Z:igmpCacheExpiryTime,_W:igmpCacheStatus,_P:igmpCacheVersion1HostTimer,'igmpMIBConformance':igmpMIBConformance,'igmpMIBCompliances':igmpMIBCompliances,'igmpV1HostMIBCompliance':igmpV1HostMIBCompliance,'igmpV1RouterMIBCompliance':igmpV1RouterMIBCompliance,'igmpV2HostMIBCompliance':igmpV2HostMIBCompliance,'igmpV2RouterMIBCompliance':igmpV2RouterMIBCompliance,'igmpMIBGroups':igmpMIBGroups,_G:igmpBaseMIBGroup,_Q:igmpRouterMIBGroup,_h:igmpV2HostMIBGroup,'igmpRouterVersion2MIBGroup':igmpRouterVersion2MIBGroup,_i:igmpV2RouterMIBGroup})