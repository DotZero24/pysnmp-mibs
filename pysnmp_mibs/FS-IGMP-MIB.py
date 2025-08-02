_i='fsIgmpInterfaceStaticMIBGroup'
_h='fsIgmpInterfaceMIBGroup'
_g='fsIgmpInterfaceStaticStatus'
_f='fsIgmpInterfaceEnabled'
_e='fsIgmpInterfaceAccessGroupAclName'
_d='fsIgmpInterfaceLeaves'
_c='fsIgmpInterfaceQuerierPresentTimeout'
_b='fsIgmpInterfaceLastMembQueryIntvl'
_a='fsIgmpInterfaceRobustness'
_Z='fsIgmpInterfaceGroups'
_Y='fsIgmpInterfaceProxyIfIndex'
_X='fsIgmpInterfaceJoins'
_W='fsIgmpInterfaceWrongVersionQueries'
_V='fsIgmpInterfaceVersion1QuerierTimer'
_U='fsIgmpInterfaceQuerierExpiryTime'
_T='fsIgmpInterfaceQuerierUpTime'
_S='fsIgmpInterfaceQueryMaxResponseTime'
_R='fsIgmpInterfaceQuerier'
_Q='fsIgmpInterfaceQueryInterval'
_P='fsIgmpInterfaceStaticGroupAddress'
_O='fsIgmpInterfaceStaticInterface'
_N='tenths of seconds'
_M='seconds'
_L='DisplayString'
_K='Integer32'
_J='InterfaceIndexOrZero'
_I='fsIgmpInterfaceHostVersion'
_H='fsIgmpInterfaceVersion'
_G='not-accessible'
_F='fsIgmpInterfaceIfIndex'
_E='Unsigned32'
_D='read-write'
_C='read-only'
_B='FS-IGMP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
fsMgmt,=mibBuilder.importSymbols('FS-SMI','fsMgmt')
InterfaceIndex,InterfaceIndexOrZero=mibBuilder.importSymbols('IF-MIB','InterfaceIndex',_J)
EnabledStatus,=mibBuilder.importSymbols('P-BRIDGE-MIB','EnabledStatus')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_K,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_E,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_L,'PhysAddress','RowStatus','TextualConvention')
fsIgmpMIB=ModuleIdentity((1,3,6,1,4,1,52642,1,1,10,2,26))
if mibBuilder.loadTexts:fsIgmpMIB.setRevisions(('2003-01-20 00:00',))
_FsIgmpMIBObjects_ObjectIdentity=ObjectIdentity
fsIgmpMIBObjects=_FsIgmpMIBObjects_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,26,1))
_FsIgmpInterfaceTable_Object=MibTable
fsIgmpInterfaceTable=_FsIgmpInterfaceTable_Object((1,3,6,1,4,1,52642,1,1,10,2,26,1,1))
if mibBuilder.loadTexts:fsIgmpInterfaceTable.setStatus(_A)
_FsIgmpInterfaceEntry_Object=MibTableRow
fsIgmpInterfaceEntry=_FsIgmpInterfaceEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,26,1,1,1))
fsIgmpInterfaceEntry.setIndexNames((0,_B,_F))
if mibBuilder.loadTexts:fsIgmpInterfaceEntry.setStatus(_A)
_FsIgmpInterfaceIfIndex_Type=InterfaceIndex
_FsIgmpInterfaceIfIndex_Object=MibTableColumn
fsIgmpInterfaceIfIndex=_FsIgmpInterfaceIfIndex_Object((1,3,6,1,4,1,52642,1,1,10,2,26,1,1,1,1),_FsIgmpInterfaceIfIndex_Type())
fsIgmpInterfaceIfIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:fsIgmpInterfaceIfIndex.setStatus(_A)
class _FsIgmpInterfaceQueryInterval_Type(Unsigned32):defaultValue=125;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_FsIgmpInterfaceQueryInterval_Type.__name__=_E
_FsIgmpInterfaceQueryInterval_Object=MibTableColumn
fsIgmpInterfaceQueryInterval=_FsIgmpInterfaceQueryInterval_Object((1,3,6,1,4,1,52642,1,1,10,2,26,1,1,1,2),_FsIgmpInterfaceQueryInterval_Type())
fsIgmpInterfaceQueryInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:fsIgmpInterfaceQueryInterval.setStatus(_A)
if mibBuilder.loadTexts:fsIgmpInterfaceQueryInterval.setUnits(_M)
class _FsIgmpInterfaceVersion_Type(Unsigned32):defaultValue=2
_FsIgmpInterfaceVersion_Type.__name__=_E
_FsIgmpInterfaceVersion_Object=MibTableColumn
fsIgmpInterfaceVersion=_FsIgmpInterfaceVersion_Object((1,3,6,1,4,1,52642,1,1,10,2,26,1,1,1,3),_FsIgmpInterfaceVersion_Type())
fsIgmpInterfaceVersion.setMaxAccess(_D)
if mibBuilder.loadTexts:fsIgmpInterfaceVersion.setStatus(_A)
_FsIgmpInterfaceQuerier_Type=IpAddress
_FsIgmpInterfaceQuerier_Object=MibTableColumn
fsIgmpInterfaceQuerier=_FsIgmpInterfaceQuerier_Object((1,3,6,1,4,1,52642,1,1,10,2,26,1,1,1,4),_FsIgmpInterfaceQuerier_Type())
fsIgmpInterfaceQuerier.setMaxAccess(_C)
if mibBuilder.loadTexts:fsIgmpInterfaceQuerier.setStatus(_A)
class _FsIgmpInterfaceQueryMaxResponseTime_Type(Unsigned32):defaultValue=100;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,250))
_FsIgmpInterfaceQueryMaxResponseTime_Type.__name__=_E
_FsIgmpInterfaceQueryMaxResponseTime_Object=MibTableColumn
fsIgmpInterfaceQueryMaxResponseTime=_FsIgmpInterfaceQueryMaxResponseTime_Object((1,3,6,1,4,1,52642,1,1,10,2,26,1,1,1,5),_FsIgmpInterfaceQueryMaxResponseTime_Type())
fsIgmpInterfaceQueryMaxResponseTime.setMaxAccess(_D)
if mibBuilder.loadTexts:fsIgmpInterfaceQueryMaxResponseTime.setStatus(_A)
if mibBuilder.loadTexts:fsIgmpInterfaceQueryMaxResponseTime.setUnits(_N)
_FsIgmpInterfaceQuerierUpTime_Type=TimeTicks
_FsIgmpInterfaceQuerierUpTime_Object=MibTableColumn
fsIgmpInterfaceQuerierUpTime=_FsIgmpInterfaceQuerierUpTime_Object((1,3,6,1,4,1,52642,1,1,10,2,26,1,1,1,6),_FsIgmpInterfaceQuerierUpTime_Type())
fsIgmpInterfaceQuerierUpTime.setMaxAccess(_C)
if mibBuilder.loadTexts:fsIgmpInterfaceQuerierUpTime.setStatus(_A)
_FsIgmpInterfaceQuerierExpiryTime_Type=TimeTicks
_FsIgmpInterfaceQuerierExpiryTime_Object=MibTableColumn
fsIgmpInterfaceQuerierExpiryTime=_FsIgmpInterfaceQuerierExpiryTime_Object((1,3,6,1,4,1,52642,1,1,10,2,26,1,1,1,7),_FsIgmpInterfaceQuerierExpiryTime_Type())
fsIgmpInterfaceQuerierExpiryTime.setMaxAccess(_C)
if mibBuilder.loadTexts:fsIgmpInterfaceQuerierExpiryTime.setStatus(_A)
_FsIgmpInterfaceVersion1QuerierTimer_Type=TimeTicks
_FsIgmpInterfaceVersion1QuerierTimer_Object=MibTableColumn
fsIgmpInterfaceVersion1QuerierTimer=_FsIgmpInterfaceVersion1QuerierTimer_Object((1,3,6,1,4,1,52642,1,1,10,2,26,1,1,1,8),_FsIgmpInterfaceVersion1QuerierTimer_Type())
fsIgmpInterfaceVersion1QuerierTimer.setMaxAccess(_C)
if mibBuilder.loadTexts:fsIgmpInterfaceVersion1QuerierTimer.setStatus(_A)
_FsIgmpInterfaceWrongVersionQueries_Type=Counter32
_FsIgmpInterfaceWrongVersionQueries_Object=MibTableColumn
fsIgmpInterfaceWrongVersionQueries=_FsIgmpInterfaceWrongVersionQueries_Object((1,3,6,1,4,1,52642,1,1,10,2,26,1,1,1,9),_FsIgmpInterfaceWrongVersionQueries_Type())
fsIgmpInterfaceWrongVersionQueries.setMaxAccess(_C)
if mibBuilder.loadTexts:fsIgmpInterfaceWrongVersionQueries.setStatus(_A)
_FsIgmpInterfaceJoins_Type=Counter32
_FsIgmpInterfaceJoins_Object=MibTableColumn
fsIgmpInterfaceJoins=_FsIgmpInterfaceJoins_Object((1,3,6,1,4,1,52642,1,1,10,2,26,1,1,1,10),_FsIgmpInterfaceJoins_Type())
fsIgmpInterfaceJoins.setMaxAccess(_C)
if mibBuilder.loadTexts:fsIgmpInterfaceJoins.setStatus(_A)
class _FsIgmpInterfaceProxyIfIndex_Type(InterfaceIndexOrZero):defaultValue=0
_FsIgmpInterfaceProxyIfIndex_Type.__name__=_J
_FsIgmpInterfaceProxyIfIndex_Object=MibTableColumn
fsIgmpInterfaceProxyIfIndex=_FsIgmpInterfaceProxyIfIndex_Object((1,3,6,1,4,1,52642,1,1,10,2,26,1,1,1,11),_FsIgmpInterfaceProxyIfIndex_Type())
fsIgmpInterfaceProxyIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:fsIgmpInterfaceProxyIfIndex.setStatus('obsolete')
_FsIgmpInterfaceGroups_Type=Gauge32
_FsIgmpInterfaceGroups_Object=MibTableColumn
fsIgmpInterfaceGroups=_FsIgmpInterfaceGroups_Object((1,3,6,1,4,1,52642,1,1,10,2,26,1,1,1,12),_FsIgmpInterfaceGroups_Type())
fsIgmpInterfaceGroups.setMaxAccess(_C)
if mibBuilder.loadTexts:fsIgmpInterfaceGroups.setStatus(_A)
class _FsIgmpInterfaceRobustness_Type(Unsigned32):defaultValue=2;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_FsIgmpInterfaceRobustness_Type.__name__=_E
_FsIgmpInterfaceRobustness_Object=MibTableColumn
fsIgmpInterfaceRobustness=_FsIgmpInterfaceRobustness_Object((1,3,6,1,4,1,52642,1,1,10,2,26,1,1,1,13),_FsIgmpInterfaceRobustness_Type())
fsIgmpInterfaceRobustness.setMaxAccess(_D)
if mibBuilder.loadTexts:fsIgmpInterfaceRobustness.setStatus(_A)
class _FsIgmpInterfaceLastMembQueryIntvl_Type(Unsigned32):defaultValue=10;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,655))
_FsIgmpInterfaceLastMembQueryIntvl_Type.__name__=_E
_FsIgmpInterfaceLastMembQueryIntvl_Object=MibTableColumn
fsIgmpInterfaceLastMembQueryIntvl=_FsIgmpInterfaceLastMembQueryIntvl_Object((1,3,6,1,4,1,52642,1,1,10,2,26,1,1,1,14),_FsIgmpInterfaceLastMembQueryIntvl_Type())
fsIgmpInterfaceLastMembQueryIntvl.setMaxAccess(_D)
if mibBuilder.loadTexts:fsIgmpInterfaceLastMembQueryIntvl.setStatus(_A)
if mibBuilder.loadTexts:fsIgmpInterfaceLastMembQueryIntvl.setUnits(_N)
class _FsIgmpInterfaceQuerierPresentTimeout_Type(Integer32):defaultValue=265;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(60,300))
_FsIgmpInterfaceQuerierPresentTimeout_Type.__name__=_K
_FsIgmpInterfaceQuerierPresentTimeout_Object=MibTableColumn
fsIgmpInterfaceQuerierPresentTimeout=_FsIgmpInterfaceQuerierPresentTimeout_Object((1,3,6,1,4,1,52642,1,1,10,2,26,1,1,1,15),_FsIgmpInterfaceQuerierPresentTimeout_Type())
fsIgmpInterfaceQuerierPresentTimeout.setMaxAccess(_D)
if mibBuilder.loadTexts:fsIgmpInterfaceQuerierPresentTimeout.setStatus(_A)
if mibBuilder.loadTexts:fsIgmpInterfaceQuerierPresentTimeout.setUnits(_M)
_FsIgmpInterfaceLeaves_Type=Counter32
_FsIgmpInterfaceLeaves_Object=MibTableColumn
fsIgmpInterfaceLeaves=_FsIgmpInterfaceLeaves_Object((1,3,6,1,4,1,52642,1,1,10,2,26,1,1,1,16),_FsIgmpInterfaceLeaves_Type())
fsIgmpInterfaceLeaves.setMaxAccess(_C)
if mibBuilder.loadTexts:fsIgmpInterfaceLeaves.setStatus(_A)
class _FsIgmpInterfaceAccessGroupAclName_Type(DisplayString):defaultValue=OctetString('')
_FsIgmpInterfaceAccessGroupAclName_Type.__name__=_L
_FsIgmpInterfaceAccessGroupAclName_Object=MibTableColumn
fsIgmpInterfaceAccessGroupAclName=_FsIgmpInterfaceAccessGroupAclName_Object((1,3,6,1,4,1,52642,1,1,10,2,26,1,1,1,17),_FsIgmpInterfaceAccessGroupAclName_Type())
fsIgmpInterfaceAccessGroupAclName.setMaxAccess(_D)
if mibBuilder.loadTexts:fsIgmpInterfaceAccessGroupAclName.setStatus(_A)
_FsIgmpInterfaceEnabled_Type=EnabledStatus
_FsIgmpInterfaceEnabled_Object=MibTableColumn
fsIgmpInterfaceEnabled=_FsIgmpInterfaceEnabled_Object((1,3,6,1,4,1,52642,1,1,10,2,26,1,1,1,18),_FsIgmpInterfaceEnabled_Type())
fsIgmpInterfaceEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:fsIgmpInterfaceEnabled.setStatus(_A)
_FsIgmpInterfaceHostVersion_Type=Unsigned32
_FsIgmpInterfaceHostVersion_Object=MibTableColumn
fsIgmpInterfaceHostVersion=_FsIgmpInterfaceHostVersion_Object((1,3,6,1,4,1,52642,1,1,10,2,26,1,1,1,19),_FsIgmpInterfaceHostVersion_Type())
fsIgmpInterfaceHostVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:fsIgmpInterfaceHostVersion.setStatus(_A)
_FsIgmpInterfaceStaticTable_Object=MibTable
fsIgmpInterfaceStaticTable=_FsIgmpInterfaceStaticTable_Object((1,3,6,1,4,1,52642,1,1,10,2,26,1,2))
if mibBuilder.loadTexts:fsIgmpInterfaceStaticTable.setStatus(_A)
_FsIgmpInterfaceStaticEntry_Object=MibTableRow
fsIgmpInterfaceStaticEntry=_FsIgmpInterfaceStaticEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,26,1,2,1))
fsIgmpInterfaceStaticEntry.setIndexNames((0,_B,_O),(0,_B,_P))
if mibBuilder.loadTexts:fsIgmpInterfaceStaticEntry.setStatus(_A)
_FsIgmpInterfaceStaticInterface_Type=InterfaceIndex
_FsIgmpInterfaceStaticInterface_Object=MibTableColumn
fsIgmpInterfaceStaticInterface=_FsIgmpInterfaceStaticInterface_Object((1,3,6,1,4,1,52642,1,1,10,2,26,1,2,1,1),_FsIgmpInterfaceStaticInterface_Type())
fsIgmpInterfaceStaticInterface.setMaxAccess(_G)
if mibBuilder.loadTexts:fsIgmpInterfaceStaticInterface.setStatus(_A)
_FsIgmpInterfaceStaticGroupAddress_Type=IpAddress
_FsIgmpInterfaceStaticGroupAddress_Object=MibTableColumn
fsIgmpInterfaceStaticGroupAddress=_FsIgmpInterfaceStaticGroupAddress_Object((1,3,6,1,4,1,52642,1,1,10,2,26,1,2,1,2),_FsIgmpInterfaceStaticGroupAddress_Type())
fsIgmpInterfaceStaticGroupAddress.setMaxAccess(_G)
if mibBuilder.loadTexts:fsIgmpInterfaceStaticGroupAddress.setStatus(_A)
_FsIgmpInterfaceStaticStatus_Type=RowStatus
_FsIgmpInterfaceStaticStatus_Object=MibTableColumn
fsIgmpInterfaceStaticStatus=_FsIgmpInterfaceStaticStatus_Object((1,3,6,1,4,1,52642,1,1,10,2,26,1,2,1,3),_FsIgmpInterfaceStaticStatus_Type())
fsIgmpInterfaceStaticStatus.setMaxAccess('read-create')
if mibBuilder.loadTexts:fsIgmpInterfaceStaticStatus.setStatus(_A)
_FsIgmpTraps_ObjectIdentity=ObjectIdentity
fsIgmpTraps=_FsIgmpTraps_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,26,1,3))
_FsIgmpMIBConformance_ObjectIdentity=ObjectIdentity
fsIgmpMIBConformance=_FsIgmpMIBConformance_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,26,2))
_FsIgmpMIBCompliances_ObjectIdentity=ObjectIdentity
fsIgmpMIBCompliances=_FsIgmpMIBCompliances_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,26,2,1))
_FsIgmpMIBGroups_ObjectIdentity=ObjectIdentity
fsIgmpMIBGroups=_FsIgmpMIBGroups_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,26,2,2))
fsIgmpInterfaceMIBGroup=ObjectGroup((1,3,6,1,4,1,52642,1,1,10,2,26,2,2,1))
fsIgmpInterfaceMIBGroup.setObjects(*((_B,_Q),(_B,_H),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_I)))
if mibBuilder.loadTexts:fsIgmpInterfaceMIBGroup.setStatus(_A)
fsIgmpInterfaceStaticMIBGroup=ObjectGroup((1,3,6,1,4,1,52642,1,1,10,2,26,2,2,2))
fsIgmpInterfaceStaticMIBGroup.setObjects((_B,_g))
if mibBuilder.loadTexts:fsIgmpInterfaceStaticMIBGroup.setStatus(_A)
fsIgmpVersionConflicted=NotificationType((1,3,6,1,4,1,52642,1,1,10,2,26,1,3,1))
fsIgmpVersionConflicted.setObjects(*((_B,_F),(_B,_H),(_B,_I)))
if mibBuilder.loadTexts:fsIgmpVersionConflicted.setStatus(_A)
fsIgmpMIBCompliance=ModuleCompliance((1,3,6,1,4,1,52642,1,1,10,2,26,2,1,1))
fsIgmpMIBCompliance.setObjects(*((_B,_h),(_B,_i)))
if mibBuilder.loadTexts:fsIgmpMIBCompliance.setStatus(_A)
igmpExternCompliance=ModuleCompliance((1,3,6,1,4,1,52642,1,1,10,2,26,2,1,2))
if mibBuilder.loadTexts:igmpExternCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'fsIgmpMIB':fsIgmpMIB,'fsIgmpMIBObjects':fsIgmpMIBObjects,'fsIgmpInterfaceTable':fsIgmpInterfaceTable,'fsIgmpInterfaceEntry':fsIgmpInterfaceEntry,_F:fsIgmpInterfaceIfIndex,_Q:fsIgmpInterfaceQueryInterval,_H:fsIgmpInterfaceVersion,_R:fsIgmpInterfaceQuerier,_S:fsIgmpInterfaceQueryMaxResponseTime,_T:fsIgmpInterfaceQuerierUpTime,_U:fsIgmpInterfaceQuerierExpiryTime,_V:fsIgmpInterfaceVersion1QuerierTimer,_W:fsIgmpInterfaceWrongVersionQueries,_X:fsIgmpInterfaceJoins,_Y:fsIgmpInterfaceProxyIfIndex,_Z:fsIgmpInterfaceGroups,_a:fsIgmpInterfaceRobustness,_b:fsIgmpInterfaceLastMembQueryIntvl,_c:fsIgmpInterfaceQuerierPresentTimeout,_d:fsIgmpInterfaceLeaves,_e:fsIgmpInterfaceAccessGroupAclName,_f:fsIgmpInterfaceEnabled,_I:fsIgmpInterfaceHostVersion,'fsIgmpInterfaceStaticTable':fsIgmpInterfaceStaticTable,'fsIgmpInterfaceStaticEntry':fsIgmpInterfaceStaticEntry,_O:fsIgmpInterfaceStaticInterface,_P:fsIgmpInterfaceStaticGroupAddress,_g:fsIgmpInterfaceStaticStatus,'fsIgmpTraps':fsIgmpTraps,'fsIgmpVersionConflicted':fsIgmpVersionConflicted,'fsIgmpMIBConformance':fsIgmpMIBConformance,'fsIgmpMIBCompliances':fsIgmpMIBCompliances,'fsIgmpMIBCompliance':fsIgmpMIBCompliance,'igmpExternCompliance':igmpExternCompliance,'fsIgmpMIBGroups':fsIgmpMIBGroups,_h:fsIgmpInterfaceMIBGroup,_i:fsIgmpInterfaceStaticMIBGroup})