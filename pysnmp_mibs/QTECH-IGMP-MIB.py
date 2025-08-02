_i='qtechIgmpInterfaceStaticMIBGroup'
_h='qtechIgmpInterfaceMIBGroup'
_g='qtechIgmpInterfaceStaticStatus'
_f='qtechIgmpInterfaceEnabled'
_e='qtechIgmpInterfaceAccessGroupAclName'
_d='qtechIgmpInterfaceLeaves'
_c='qtechIgmpInterfaceQuerierPresentTimeout'
_b='qtechIgmpInterfaceLastMembQueryIntvl'
_a='qtechIgmpInterfaceRobustness'
_Z='qtechIgmpInterfaceGroups'
_Y='qtechIgmpInterfaceProxyIfIndex'
_X='qtechIgmpInterfaceJoins'
_W='qtechIgmpInterfaceWrongVersionQueries'
_V='qtechIgmpInterfaceVersion1QuerierTimer'
_U='qtechIgmpInterfaceQuerierExpiryTime'
_T='qtechIgmpInterfaceQuerierUpTime'
_S='qtechIgmpInterfaceQueryMaxResponseTime'
_R='qtechIgmpInterfaceQuerier'
_Q='qtechIgmpInterfaceQueryInterval'
_P='qtechIgmpInterfaceStaticGroupAddress'
_O='qtechIgmpInterfaceStaticInterface'
_N='tenths of seconds'
_M='seconds'
_L='DisplayString'
_K='Integer32'
_J='InterfaceIndexOrZero'
_I='qtechIgmpInterfaceHostVersion'
_H='qtechIgmpInterfaceVersion'
_G='not-accessible'
_F='qtechIgmpInterfaceIfIndex'
_E='Unsigned32'
_D='read-write'
_C='read-only'
_B='QTECH-IGMP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,InterfaceIndexOrZero=mibBuilder.importSymbols('IF-MIB','InterfaceIndex',_J)
EnabledStatus,=mibBuilder.importSymbols('P-BRIDGE-MIB','EnabledStatus')
qtechMgmt,=mibBuilder.importSymbols('QTECH-SMI','qtechMgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_K,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_E,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_L,'PhysAddress','RowStatus','TextualConvention')
qtechIgmpMIB=ModuleIdentity((1,3,6,1,4,1,27514,1,1,10,2,26))
if mibBuilder.loadTexts:qtechIgmpMIB.setRevisions(('2003-01-20 00:00',))
_QtechIgmpMIBObjects_ObjectIdentity=ObjectIdentity
qtechIgmpMIBObjects=_QtechIgmpMIBObjects_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,26,1))
_QtechIgmpInterfaceTable_Object=MibTable
qtechIgmpInterfaceTable=_QtechIgmpInterfaceTable_Object((1,3,6,1,4,1,27514,1,1,10,2,26,1,1))
if mibBuilder.loadTexts:qtechIgmpInterfaceTable.setStatus(_A)
_QtechIgmpInterfaceEntry_Object=MibTableRow
qtechIgmpInterfaceEntry=_QtechIgmpInterfaceEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,26,1,1,1))
qtechIgmpInterfaceEntry.setIndexNames((0,_B,_F))
if mibBuilder.loadTexts:qtechIgmpInterfaceEntry.setStatus(_A)
_QtechIgmpInterfaceIfIndex_Type=InterfaceIndex
_QtechIgmpInterfaceIfIndex_Object=MibTableColumn
qtechIgmpInterfaceIfIndex=_QtechIgmpInterfaceIfIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,26,1,1,1,1),_QtechIgmpInterfaceIfIndex_Type())
qtechIgmpInterfaceIfIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:qtechIgmpInterfaceIfIndex.setStatus(_A)
class _QtechIgmpInterfaceQueryInterval_Type(Unsigned32):defaultValue=125;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_QtechIgmpInterfaceQueryInterval_Type.__name__=_E
_QtechIgmpInterfaceQueryInterval_Object=MibTableColumn
qtechIgmpInterfaceQueryInterval=_QtechIgmpInterfaceQueryInterval_Object((1,3,6,1,4,1,27514,1,1,10,2,26,1,1,1,2),_QtechIgmpInterfaceQueryInterval_Type())
qtechIgmpInterfaceQueryInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechIgmpInterfaceQueryInterval.setStatus(_A)
if mibBuilder.loadTexts:qtechIgmpInterfaceQueryInterval.setUnits(_M)
class _QtechIgmpInterfaceVersion_Type(Unsigned32):defaultValue=2
_QtechIgmpInterfaceVersion_Type.__name__=_E
_QtechIgmpInterfaceVersion_Object=MibTableColumn
qtechIgmpInterfaceVersion=_QtechIgmpInterfaceVersion_Object((1,3,6,1,4,1,27514,1,1,10,2,26,1,1,1,3),_QtechIgmpInterfaceVersion_Type())
qtechIgmpInterfaceVersion.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechIgmpInterfaceVersion.setStatus(_A)
_QtechIgmpInterfaceQuerier_Type=IpAddress
_QtechIgmpInterfaceQuerier_Object=MibTableColumn
qtechIgmpInterfaceQuerier=_QtechIgmpInterfaceQuerier_Object((1,3,6,1,4,1,27514,1,1,10,2,26,1,1,1,4),_QtechIgmpInterfaceQuerier_Type())
qtechIgmpInterfaceQuerier.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIgmpInterfaceQuerier.setStatus(_A)
class _QtechIgmpInterfaceQueryMaxResponseTime_Type(Unsigned32):defaultValue=100;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,250))
_QtechIgmpInterfaceQueryMaxResponseTime_Type.__name__=_E
_QtechIgmpInterfaceQueryMaxResponseTime_Object=MibTableColumn
qtechIgmpInterfaceQueryMaxResponseTime=_QtechIgmpInterfaceQueryMaxResponseTime_Object((1,3,6,1,4,1,27514,1,1,10,2,26,1,1,1,5),_QtechIgmpInterfaceQueryMaxResponseTime_Type())
qtechIgmpInterfaceQueryMaxResponseTime.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechIgmpInterfaceQueryMaxResponseTime.setStatus(_A)
if mibBuilder.loadTexts:qtechIgmpInterfaceQueryMaxResponseTime.setUnits(_N)
_QtechIgmpInterfaceQuerierUpTime_Type=TimeTicks
_QtechIgmpInterfaceQuerierUpTime_Object=MibTableColumn
qtechIgmpInterfaceQuerierUpTime=_QtechIgmpInterfaceQuerierUpTime_Object((1,3,6,1,4,1,27514,1,1,10,2,26,1,1,1,6),_QtechIgmpInterfaceQuerierUpTime_Type())
qtechIgmpInterfaceQuerierUpTime.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIgmpInterfaceQuerierUpTime.setStatus(_A)
_QtechIgmpInterfaceQuerierExpiryTime_Type=TimeTicks
_QtechIgmpInterfaceQuerierExpiryTime_Object=MibTableColumn
qtechIgmpInterfaceQuerierExpiryTime=_QtechIgmpInterfaceQuerierExpiryTime_Object((1,3,6,1,4,1,27514,1,1,10,2,26,1,1,1,7),_QtechIgmpInterfaceQuerierExpiryTime_Type())
qtechIgmpInterfaceQuerierExpiryTime.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIgmpInterfaceQuerierExpiryTime.setStatus(_A)
_QtechIgmpInterfaceVersion1QuerierTimer_Type=TimeTicks
_QtechIgmpInterfaceVersion1QuerierTimer_Object=MibTableColumn
qtechIgmpInterfaceVersion1QuerierTimer=_QtechIgmpInterfaceVersion1QuerierTimer_Object((1,3,6,1,4,1,27514,1,1,10,2,26,1,1,1,8),_QtechIgmpInterfaceVersion1QuerierTimer_Type())
qtechIgmpInterfaceVersion1QuerierTimer.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIgmpInterfaceVersion1QuerierTimer.setStatus(_A)
_QtechIgmpInterfaceWrongVersionQueries_Type=Counter32
_QtechIgmpInterfaceWrongVersionQueries_Object=MibTableColumn
qtechIgmpInterfaceWrongVersionQueries=_QtechIgmpInterfaceWrongVersionQueries_Object((1,3,6,1,4,1,27514,1,1,10,2,26,1,1,1,9),_QtechIgmpInterfaceWrongVersionQueries_Type())
qtechIgmpInterfaceWrongVersionQueries.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIgmpInterfaceWrongVersionQueries.setStatus(_A)
_QtechIgmpInterfaceJoins_Type=Counter32
_QtechIgmpInterfaceJoins_Object=MibTableColumn
qtechIgmpInterfaceJoins=_QtechIgmpInterfaceJoins_Object((1,3,6,1,4,1,27514,1,1,10,2,26,1,1,1,10),_QtechIgmpInterfaceJoins_Type())
qtechIgmpInterfaceJoins.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIgmpInterfaceJoins.setStatus(_A)
class _QtechIgmpInterfaceProxyIfIndex_Type(InterfaceIndexOrZero):defaultValue=0
_QtechIgmpInterfaceProxyIfIndex_Type.__name__=_J
_QtechIgmpInterfaceProxyIfIndex_Object=MibTableColumn
qtechIgmpInterfaceProxyIfIndex=_QtechIgmpInterfaceProxyIfIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,26,1,1,1,11),_QtechIgmpInterfaceProxyIfIndex_Type())
qtechIgmpInterfaceProxyIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIgmpInterfaceProxyIfIndex.setStatus('obsolete')
_QtechIgmpInterfaceGroups_Type=Gauge32
_QtechIgmpInterfaceGroups_Object=MibTableColumn
qtechIgmpInterfaceGroups=_QtechIgmpInterfaceGroups_Object((1,3,6,1,4,1,27514,1,1,10,2,26,1,1,1,12),_QtechIgmpInterfaceGroups_Type())
qtechIgmpInterfaceGroups.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIgmpInterfaceGroups.setStatus(_A)
class _QtechIgmpInterfaceRobustness_Type(Unsigned32):defaultValue=2;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_QtechIgmpInterfaceRobustness_Type.__name__=_E
_QtechIgmpInterfaceRobustness_Object=MibTableColumn
qtechIgmpInterfaceRobustness=_QtechIgmpInterfaceRobustness_Object((1,3,6,1,4,1,27514,1,1,10,2,26,1,1,1,13),_QtechIgmpInterfaceRobustness_Type())
qtechIgmpInterfaceRobustness.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechIgmpInterfaceRobustness.setStatus(_A)
class _QtechIgmpInterfaceLastMembQueryIntvl_Type(Unsigned32):defaultValue=10;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,655))
_QtechIgmpInterfaceLastMembQueryIntvl_Type.__name__=_E
_QtechIgmpInterfaceLastMembQueryIntvl_Object=MibTableColumn
qtechIgmpInterfaceLastMembQueryIntvl=_QtechIgmpInterfaceLastMembQueryIntvl_Object((1,3,6,1,4,1,27514,1,1,10,2,26,1,1,1,14),_QtechIgmpInterfaceLastMembQueryIntvl_Type())
qtechIgmpInterfaceLastMembQueryIntvl.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechIgmpInterfaceLastMembQueryIntvl.setStatus(_A)
if mibBuilder.loadTexts:qtechIgmpInterfaceLastMembQueryIntvl.setUnits(_N)
class _QtechIgmpInterfaceQuerierPresentTimeout_Type(Integer32):defaultValue=265;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(60,300))
_QtechIgmpInterfaceQuerierPresentTimeout_Type.__name__=_K
_QtechIgmpInterfaceQuerierPresentTimeout_Object=MibTableColumn
qtechIgmpInterfaceQuerierPresentTimeout=_QtechIgmpInterfaceQuerierPresentTimeout_Object((1,3,6,1,4,1,27514,1,1,10,2,26,1,1,1,15),_QtechIgmpInterfaceQuerierPresentTimeout_Type())
qtechIgmpInterfaceQuerierPresentTimeout.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechIgmpInterfaceQuerierPresentTimeout.setStatus(_A)
if mibBuilder.loadTexts:qtechIgmpInterfaceQuerierPresentTimeout.setUnits(_M)
_QtechIgmpInterfaceLeaves_Type=Counter32
_QtechIgmpInterfaceLeaves_Object=MibTableColumn
qtechIgmpInterfaceLeaves=_QtechIgmpInterfaceLeaves_Object((1,3,6,1,4,1,27514,1,1,10,2,26,1,1,1,16),_QtechIgmpInterfaceLeaves_Type())
qtechIgmpInterfaceLeaves.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIgmpInterfaceLeaves.setStatus(_A)
class _QtechIgmpInterfaceAccessGroupAclName_Type(DisplayString):defaultValue=OctetString('')
_QtechIgmpInterfaceAccessGroupAclName_Type.__name__=_L
_QtechIgmpInterfaceAccessGroupAclName_Object=MibTableColumn
qtechIgmpInterfaceAccessGroupAclName=_QtechIgmpInterfaceAccessGroupAclName_Object((1,3,6,1,4,1,27514,1,1,10,2,26,1,1,1,17),_QtechIgmpInterfaceAccessGroupAclName_Type())
qtechIgmpInterfaceAccessGroupAclName.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechIgmpInterfaceAccessGroupAclName.setStatus(_A)
_QtechIgmpInterfaceEnabled_Type=EnabledStatus
_QtechIgmpInterfaceEnabled_Object=MibTableColumn
qtechIgmpInterfaceEnabled=_QtechIgmpInterfaceEnabled_Object((1,3,6,1,4,1,27514,1,1,10,2,26,1,1,1,18),_QtechIgmpInterfaceEnabled_Type())
qtechIgmpInterfaceEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIgmpInterfaceEnabled.setStatus(_A)
_QtechIgmpInterfaceHostVersion_Type=Unsigned32
_QtechIgmpInterfaceHostVersion_Object=MibTableColumn
qtechIgmpInterfaceHostVersion=_QtechIgmpInterfaceHostVersion_Object((1,3,6,1,4,1,27514,1,1,10,2,26,1,1,1,19),_QtechIgmpInterfaceHostVersion_Type())
qtechIgmpInterfaceHostVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechIgmpInterfaceHostVersion.setStatus(_A)
_QtechIgmpInterfaceStaticTable_Object=MibTable
qtechIgmpInterfaceStaticTable=_QtechIgmpInterfaceStaticTable_Object((1,3,6,1,4,1,27514,1,1,10,2,26,1,2))
if mibBuilder.loadTexts:qtechIgmpInterfaceStaticTable.setStatus(_A)
_QtechIgmpInterfaceStaticEntry_Object=MibTableRow
qtechIgmpInterfaceStaticEntry=_QtechIgmpInterfaceStaticEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,26,1,2,1))
qtechIgmpInterfaceStaticEntry.setIndexNames((0,_B,_O),(0,_B,_P))
if mibBuilder.loadTexts:qtechIgmpInterfaceStaticEntry.setStatus(_A)
_QtechIgmpInterfaceStaticInterface_Type=InterfaceIndex
_QtechIgmpInterfaceStaticInterface_Object=MibTableColumn
qtechIgmpInterfaceStaticInterface=_QtechIgmpInterfaceStaticInterface_Object((1,3,6,1,4,1,27514,1,1,10,2,26,1,2,1,1),_QtechIgmpInterfaceStaticInterface_Type())
qtechIgmpInterfaceStaticInterface.setMaxAccess(_G)
if mibBuilder.loadTexts:qtechIgmpInterfaceStaticInterface.setStatus(_A)
_QtechIgmpInterfaceStaticGroupAddress_Type=IpAddress
_QtechIgmpInterfaceStaticGroupAddress_Object=MibTableColumn
qtechIgmpInterfaceStaticGroupAddress=_QtechIgmpInterfaceStaticGroupAddress_Object((1,3,6,1,4,1,27514,1,1,10,2,26,1,2,1,2),_QtechIgmpInterfaceStaticGroupAddress_Type())
qtechIgmpInterfaceStaticGroupAddress.setMaxAccess(_G)
if mibBuilder.loadTexts:qtechIgmpInterfaceStaticGroupAddress.setStatus(_A)
_QtechIgmpInterfaceStaticStatus_Type=RowStatus
_QtechIgmpInterfaceStaticStatus_Object=MibTableColumn
qtechIgmpInterfaceStaticStatus=_QtechIgmpInterfaceStaticStatus_Object((1,3,6,1,4,1,27514,1,1,10,2,26,1,2,1,3),_QtechIgmpInterfaceStaticStatus_Type())
qtechIgmpInterfaceStaticStatus.setMaxAccess('read-create')
if mibBuilder.loadTexts:qtechIgmpInterfaceStaticStatus.setStatus(_A)
_QtechIgmpTraps_ObjectIdentity=ObjectIdentity
qtechIgmpTraps=_QtechIgmpTraps_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,26,1,3))
_QtechIgmpMIBConformance_ObjectIdentity=ObjectIdentity
qtechIgmpMIBConformance=_QtechIgmpMIBConformance_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,26,2))
_QtechIgmpMIBCompliances_ObjectIdentity=ObjectIdentity
qtechIgmpMIBCompliances=_QtechIgmpMIBCompliances_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,26,2,1))
_QtechIgmpMIBGroups_ObjectIdentity=ObjectIdentity
qtechIgmpMIBGroups=_QtechIgmpMIBGroups_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,26,2,2))
qtechIgmpInterfaceMIBGroup=ObjectGroup((1,3,6,1,4,1,27514,1,1,10,2,26,2,2,1))
qtechIgmpInterfaceMIBGroup.setObjects(*((_B,_Q),(_B,_H),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_I)))
if mibBuilder.loadTexts:qtechIgmpInterfaceMIBGroup.setStatus(_A)
qtechIgmpInterfaceStaticMIBGroup=ObjectGroup((1,3,6,1,4,1,27514,1,1,10,2,26,2,2,2))
qtechIgmpInterfaceStaticMIBGroup.setObjects((_B,_g))
if mibBuilder.loadTexts:qtechIgmpInterfaceStaticMIBGroup.setStatus(_A)
qtechIgmpVersionConflicted=NotificationType((1,3,6,1,4,1,27514,1,1,10,2,26,1,3,1))
qtechIgmpVersionConflicted.setObjects(*((_B,_F),(_B,_H),(_B,_I)))
if mibBuilder.loadTexts:qtechIgmpVersionConflicted.setStatus(_A)
qtechIgmpMIBCompliance=ModuleCompliance((1,3,6,1,4,1,27514,1,1,10,2,26,2,1,1))
qtechIgmpMIBCompliance.setObjects(*((_B,_h),(_B,_i)))
if mibBuilder.loadTexts:qtechIgmpMIBCompliance.setStatus(_A)
igmpExternCompliance=ModuleCompliance((1,3,6,1,4,1,27514,1,1,10,2,26,2,1,2))
if mibBuilder.loadTexts:igmpExternCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'qtechIgmpMIB':qtechIgmpMIB,'qtechIgmpMIBObjects':qtechIgmpMIBObjects,'qtechIgmpInterfaceTable':qtechIgmpInterfaceTable,'qtechIgmpInterfaceEntry':qtechIgmpInterfaceEntry,_F:qtechIgmpInterfaceIfIndex,_Q:qtechIgmpInterfaceQueryInterval,_H:qtechIgmpInterfaceVersion,_R:qtechIgmpInterfaceQuerier,_S:qtechIgmpInterfaceQueryMaxResponseTime,_T:qtechIgmpInterfaceQuerierUpTime,_U:qtechIgmpInterfaceQuerierExpiryTime,_V:qtechIgmpInterfaceVersion1QuerierTimer,_W:qtechIgmpInterfaceWrongVersionQueries,_X:qtechIgmpInterfaceJoins,_Y:qtechIgmpInterfaceProxyIfIndex,_Z:qtechIgmpInterfaceGroups,_a:qtechIgmpInterfaceRobustness,_b:qtechIgmpInterfaceLastMembQueryIntvl,_c:qtechIgmpInterfaceQuerierPresentTimeout,_d:qtechIgmpInterfaceLeaves,_e:qtechIgmpInterfaceAccessGroupAclName,_f:qtechIgmpInterfaceEnabled,_I:qtechIgmpInterfaceHostVersion,'qtechIgmpInterfaceStaticTable':qtechIgmpInterfaceStaticTable,'qtechIgmpInterfaceStaticEntry':qtechIgmpInterfaceStaticEntry,_O:qtechIgmpInterfaceStaticInterface,_P:qtechIgmpInterfaceStaticGroupAddress,_g:qtechIgmpInterfaceStaticStatus,'qtechIgmpTraps':qtechIgmpTraps,'qtechIgmpVersionConflicted':qtechIgmpVersionConflicted,'qtechIgmpMIBConformance':qtechIgmpMIBConformance,'qtechIgmpMIBCompliances':qtechIgmpMIBCompliances,'qtechIgmpMIBCompliance':qtechIgmpMIBCompliance,'igmpExternCompliance':igmpExternCompliance,'qtechIgmpMIBGroups':qtechIgmpMIBGroups,_h:qtechIgmpInterfaceMIBGroup,_i:qtechIgmpInterfaceStaticMIBGroup})