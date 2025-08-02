_g='mldRouterMIBGroup'
_f='mldHostMIBGroup'
_e='mldInterfaceProxyIfIndex'
_d='mldInterfaceLastListenQueryIntvl'
_c='mldInterfaceRobustness'
_b='mldInterfaceQueryMaxResponseDelay'
_a='mldInterfaceVersion'
_Z='mldInterfaceQuerierExpiryTime'
_Y='mldInterfaceQuerierUpTime'
_X='mldCacheLastReporter'
_W='mldInterfaceGroups'
_V='mldInterfaceJoins'
_U='mldInterfaceQueryInterval'
_T='mldCacheExpiryTime'
_S='mldCacheUpTime'
_R='mldInterfaceStatus'
_Q='mldCacheStatus'
_P='mldCacheSelf'
_O='mldCacheIfIndex'
_N='mldCacheAddress'
_M='mldInterfaceIfIndex'
_L='TruthValue'
_K='InterfaceIndexOrZero'
_J='mldBaseMIBGroup'
_I='mldInterfaceQuerier'
_H='seconds'
_G='not-accessible'
_F='InetAddressIPv6'
_E='Unsigned32'
_D='read-only'
_C='read-create'
_B='IPV6-MLD-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,InterfaceIndexOrZero=mibBuilder.importSymbols('IF-MIB','InterfaceIndex',_K)
InetAddressIPv6,=mibBuilder.importSymbols('INET-ADDRESS-MIB',_F)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,mib_2=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_E,'iso','mib-2')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention',_L)
mldMIB=ModuleIdentity((1,3,6,1,2,1,91))
if mibBuilder.loadTexts:mldMIB.setRevisions(('2001-01-25 00:00',))
_MldMIBObjects_ObjectIdentity=ObjectIdentity
mldMIBObjects=_MldMIBObjects_ObjectIdentity((1,3,6,1,2,1,91,1))
_MldInterfaceTable_Object=MibTable
mldInterfaceTable=_MldInterfaceTable_Object((1,3,6,1,2,1,91,1,1))
if mibBuilder.loadTexts:mldInterfaceTable.setStatus(_A)
_MldInterfaceEntry_Object=MibTableRow
mldInterfaceEntry=_MldInterfaceEntry_Object((1,3,6,1,2,1,91,1,1,1))
mldInterfaceEntry.setIndexNames((0,_B,_M))
if mibBuilder.loadTexts:mldInterfaceEntry.setStatus(_A)
_MldInterfaceIfIndex_Type=InterfaceIndex
_MldInterfaceIfIndex_Object=MibTableColumn
mldInterfaceIfIndex=_MldInterfaceIfIndex_Object((1,3,6,1,2,1,91,1,1,1,1),_MldInterfaceIfIndex_Type())
mldInterfaceIfIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:mldInterfaceIfIndex.setStatus(_A)
class _MldInterfaceQueryInterval_Type(Unsigned32):defaultValue=125
_MldInterfaceQueryInterval_Type.__name__=_E
_MldInterfaceQueryInterval_Object=MibTableColumn
mldInterfaceQueryInterval=_MldInterfaceQueryInterval_Object((1,3,6,1,2,1,91,1,1,1,2),_MldInterfaceQueryInterval_Type())
mldInterfaceQueryInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:mldInterfaceQueryInterval.setStatus(_A)
if mibBuilder.loadTexts:mldInterfaceQueryInterval.setUnits(_H)
_MldInterfaceStatus_Type=RowStatus
_MldInterfaceStatus_Object=MibTableColumn
mldInterfaceStatus=_MldInterfaceStatus_Object((1,3,6,1,2,1,91,1,1,1,3),_MldInterfaceStatus_Type())
mldInterfaceStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:mldInterfaceStatus.setStatus(_A)
class _MldInterfaceVersion_Type(Unsigned32):defaultValue=1
_MldInterfaceVersion_Type.__name__=_E
_MldInterfaceVersion_Object=MibTableColumn
mldInterfaceVersion=_MldInterfaceVersion_Object((1,3,6,1,2,1,91,1,1,1,4),_MldInterfaceVersion_Type())
mldInterfaceVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:mldInterfaceVersion.setStatus(_A)
class _MldInterfaceQuerier_Type(InetAddressIPv6):subtypeSpec=InetAddressIPv6.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_MldInterfaceQuerier_Type.__name__=_F
_MldInterfaceQuerier_Object=MibTableColumn
mldInterfaceQuerier=_MldInterfaceQuerier_Object((1,3,6,1,2,1,91,1,1,1,5),_MldInterfaceQuerier_Type())
mldInterfaceQuerier.setMaxAccess(_D)
if mibBuilder.loadTexts:mldInterfaceQuerier.setStatus(_A)
class _MldInterfaceQueryMaxResponseDelay_Type(Unsigned32):defaultValue=10
_MldInterfaceQueryMaxResponseDelay_Type.__name__=_E
_MldInterfaceQueryMaxResponseDelay_Object=MibTableColumn
mldInterfaceQueryMaxResponseDelay=_MldInterfaceQueryMaxResponseDelay_Object((1,3,6,1,2,1,91,1,1,1,6),_MldInterfaceQueryMaxResponseDelay_Type())
mldInterfaceQueryMaxResponseDelay.setMaxAccess(_C)
if mibBuilder.loadTexts:mldInterfaceQueryMaxResponseDelay.setStatus(_A)
if mibBuilder.loadTexts:mldInterfaceQueryMaxResponseDelay.setUnits(_H)
_MldInterfaceJoins_Type=Counter32
_MldInterfaceJoins_Object=MibTableColumn
mldInterfaceJoins=_MldInterfaceJoins_Object((1,3,6,1,2,1,91,1,1,1,7),_MldInterfaceJoins_Type())
mldInterfaceJoins.setMaxAccess(_D)
if mibBuilder.loadTexts:mldInterfaceJoins.setStatus(_A)
_MldInterfaceGroups_Type=Gauge32
_MldInterfaceGroups_Object=MibTableColumn
mldInterfaceGroups=_MldInterfaceGroups_Object((1,3,6,1,2,1,91,1,1,1,8),_MldInterfaceGroups_Type())
mldInterfaceGroups.setMaxAccess(_D)
if mibBuilder.loadTexts:mldInterfaceGroups.setStatus(_A)
class _MldInterfaceRobustness_Type(Unsigned32):defaultValue=2
_MldInterfaceRobustness_Type.__name__=_E
_MldInterfaceRobustness_Object=MibTableColumn
mldInterfaceRobustness=_MldInterfaceRobustness_Object((1,3,6,1,2,1,91,1,1,1,9),_MldInterfaceRobustness_Type())
mldInterfaceRobustness.setMaxAccess(_C)
if mibBuilder.loadTexts:mldInterfaceRobustness.setStatus(_A)
class _MldInterfaceLastListenQueryIntvl_Type(Unsigned32):defaultValue=1
_MldInterfaceLastListenQueryIntvl_Type.__name__=_E
_MldInterfaceLastListenQueryIntvl_Object=MibTableColumn
mldInterfaceLastListenQueryIntvl=_MldInterfaceLastListenQueryIntvl_Object((1,3,6,1,2,1,91,1,1,1,10),_MldInterfaceLastListenQueryIntvl_Type())
mldInterfaceLastListenQueryIntvl.setMaxAccess(_C)
if mibBuilder.loadTexts:mldInterfaceLastListenQueryIntvl.setStatus(_A)
if mibBuilder.loadTexts:mldInterfaceLastListenQueryIntvl.setUnits(_H)
class _MldInterfaceProxyIfIndex_Type(InterfaceIndexOrZero):defaultValue=0
_MldInterfaceProxyIfIndex_Type.__name__=_K
_MldInterfaceProxyIfIndex_Object=MibTableColumn
mldInterfaceProxyIfIndex=_MldInterfaceProxyIfIndex_Object((1,3,6,1,2,1,91,1,1,1,11),_MldInterfaceProxyIfIndex_Type())
mldInterfaceProxyIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:mldInterfaceProxyIfIndex.setStatus(_A)
_MldInterfaceQuerierUpTime_Type=TimeTicks
_MldInterfaceQuerierUpTime_Object=MibTableColumn
mldInterfaceQuerierUpTime=_MldInterfaceQuerierUpTime_Object((1,3,6,1,2,1,91,1,1,1,12),_MldInterfaceQuerierUpTime_Type())
mldInterfaceQuerierUpTime.setMaxAccess(_D)
if mibBuilder.loadTexts:mldInterfaceQuerierUpTime.setStatus(_A)
_MldInterfaceQuerierExpiryTime_Type=TimeTicks
_MldInterfaceQuerierExpiryTime_Object=MibTableColumn
mldInterfaceQuerierExpiryTime=_MldInterfaceQuerierExpiryTime_Object((1,3,6,1,2,1,91,1,1,1,13),_MldInterfaceQuerierExpiryTime_Type())
mldInterfaceQuerierExpiryTime.setMaxAccess(_D)
if mibBuilder.loadTexts:mldInterfaceQuerierExpiryTime.setStatus(_A)
_MldCacheTable_Object=MibTable
mldCacheTable=_MldCacheTable_Object((1,3,6,1,2,1,91,1,2))
if mibBuilder.loadTexts:mldCacheTable.setStatus(_A)
_MldCacheEntry_Object=MibTableRow
mldCacheEntry=_MldCacheEntry_Object((1,3,6,1,2,1,91,1,2,1))
mldCacheEntry.setIndexNames((0,_B,_N),(0,_B,_O))
if mibBuilder.loadTexts:mldCacheEntry.setStatus(_A)
class _MldCacheAddress_Type(InetAddressIPv6):subtypeSpec=InetAddressIPv6.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_MldCacheAddress_Type.__name__=_F
_MldCacheAddress_Object=MibTableColumn
mldCacheAddress=_MldCacheAddress_Object((1,3,6,1,2,1,91,1,2,1,1),_MldCacheAddress_Type())
mldCacheAddress.setMaxAccess(_G)
if mibBuilder.loadTexts:mldCacheAddress.setStatus(_A)
_MldCacheIfIndex_Type=InterfaceIndex
_MldCacheIfIndex_Object=MibTableColumn
mldCacheIfIndex=_MldCacheIfIndex_Object((1,3,6,1,2,1,91,1,2,1,2),_MldCacheIfIndex_Type())
mldCacheIfIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:mldCacheIfIndex.setStatus(_A)
class _MldCacheSelf_Type(TruthValue):defaultValue=1
_MldCacheSelf_Type.__name__=_L
_MldCacheSelf_Object=MibTableColumn
mldCacheSelf=_MldCacheSelf_Object((1,3,6,1,2,1,91,1,2,1,3),_MldCacheSelf_Type())
mldCacheSelf.setMaxAccess(_C)
if mibBuilder.loadTexts:mldCacheSelf.setStatus(_A)
class _MldCacheLastReporter_Type(InetAddressIPv6):subtypeSpec=InetAddressIPv6.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_MldCacheLastReporter_Type.__name__=_F
_MldCacheLastReporter_Object=MibTableColumn
mldCacheLastReporter=_MldCacheLastReporter_Object((1,3,6,1,2,1,91,1,2,1,4),_MldCacheLastReporter_Type())
mldCacheLastReporter.setMaxAccess(_D)
if mibBuilder.loadTexts:mldCacheLastReporter.setStatus(_A)
_MldCacheUpTime_Type=TimeTicks
_MldCacheUpTime_Object=MibTableColumn
mldCacheUpTime=_MldCacheUpTime_Object((1,3,6,1,2,1,91,1,2,1,5),_MldCacheUpTime_Type())
mldCacheUpTime.setMaxAccess(_D)
if mibBuilder.loadTexts:mldCacheUpTime.setStatus(_A)
_MldCacheExpiryTime_Type=TimeTicks
_MldCacheExpiryTime_Object=MibTableColumn
mldCacheExpiryTime=_MldCacheExpiryTime_Object((1,3,6,1,2,1,91,1,2,1,6),_MldCacheExpiryTime_Type())
mldCacheExpiryTime.setMaxAccess(_D)
if mibBuilder.loadTexts:mldCacheExpiryTime.setStatus(_A)
_MldCacheStatus_Type=RowStatus
_MldCacheStatus_Object=MibTableColumn
mldCacheStatus=_MldCacheStatus_Object((1,3,6,1,2,1,91,1,2,1,7),_MldCacheStatus_Type())
mldCacheStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:mldCacheStatus.setStatus(_A)
_MldMIBConformance_ObjectIdentity=ObjectIdentity
mldMIBConformance=_MldMIBConformance_ObjectIdentity((1,3,6,1,2,1,91,2))
_MldMIBCompliances_ObjectIdentity=ObjectIdentity
mldMIBCompliances=_MldMIBCompliances_ObjectIdentity((1,3,6,1,2,1,91,2,1))
_MldMIBGroups_ObjectIdentity=ObjectIdentity
mldMIBGroups=_MldMIBGroups_ObjectIdentity((1,3,6,1,2,1,91,2,2))
mldBaseMIBGroup=ObjectGroup((1,3,6,1,2,1,91,2,2,1))
mldBaseMIBGroup.setObjects(*((_B,_P),(_B,_Q),(_B,_R)))
if mibBuilder.loadTexts:mldBaseMIBGroup.setStatus(_A)
mldRouterMIBGroup=ObjectGroup((1,3,6,1,2,1,91,2,2,2))
mldRouterMIBGroup.setObjects(*((_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_I),(_B,_a),(_B,_b),(_B,_c),(_B,_d)))
if mibBuilder.loadTexts:mldRouterMIBGroup.setStatus(_A)
mldHostMIBGroup=ObjectGroup((1,3,6,1,2,1,91,2,2,3))
mldHostMIBGroup.setObjects((_B,_I))
if mibBuilder.loadTexts:mldHostMIBGroup.setStatus(_A)
mldProxyMIBGroup=ObjectGroup((1,3,6,1,2,1,91,2,2,4))
mldProxyMIBGroup.setObjects((_B,_e))
if mibBuilder.loadTexts:mldProxyMIBGroup.setStatus(_A)
mldHostMIBCompliance=ModuleCompliance((1,3,6,1,2,1,91,2,1,1))
mldHostMIBCompliance.setObjects(*((_B,_J),(_B,_f)))
if mibBuilder.loadTexts:mldHostMIBCompliance.setStatus(_A)
mldRouterMIBCompliance=ModuleCompliance((1,3,6,1,2,1,91,2,1,2))
mldRouterMIBCompliance.setObjects(*((_B,_J),(_B,_g)))
if mibBuilder.loadTexts:mldRouterMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'mldMIB':mldMIB,'mldMIBObjects':mldMIBObjects,'mldInterfaceTable':mldInterfaceTable,'mldInterfaceEntry':mldInterfaceEntry,_M:mldInterfaceIfIndex,_U:mldInterfaceQueryInterval,_R:mldInterfaceStatus,_a:mldInterfaceVersion,_I:mldInterfaceQuerier,_b:mldInterfaceQueryMaxResponseDelay,_V:mldInterfaceJoins,_W:mldInterfaceGroups,_c:mldInterfaceRobustness,_d:mldInterfaceLastListenQueryIntvl,_e:mldInterfaceProxyIfIndex,_Y:mldInterfaceQuerierUpTime,_Z:mldInterfaceQuerierExpiryTime,'mldCacheTable':mldCacheTable,'mldCacheEntry':mldCacheEntry,_N:mldCacheAddress,_O:mldCacheIfIndex,_P:mldCacheSelf,_X:mldCacheLastReporter,_S:mldCacheUpTime,_T:mldCacheExpiryTime,_Q:mldCacheStatus,'mldMIBConformance':mldMIBConformance,'mldMIBCompliances':mldMIBCompliances,'mldHostMIBCompliance':mldHostMIBCompliance,'mldRouterMIBCompliance':mldRouterMIBCompliance,'mldMIBGroups':mldMIBGroups,_J:mldBaseMIBGroup,_g:mldRouterMIBGroup,_f:mldHostMIBGroup,'mldProxyMIBGroup':mldProxyMIBGroup})