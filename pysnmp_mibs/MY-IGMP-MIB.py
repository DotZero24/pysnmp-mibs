_i='myIgmpInterfaceStaticMIBGroup'
_h='myIgmpInterfaceMIBGroup'
_g='myIgmpInterfaceStaticStatus'
_f='myIgmpInterfaceEnabled'
_e='myIgmpInterfaceAccessGroupAclName'
_d='myIgmpInterfaceLeaves'
_c='myIgmpInterfaceQuerierPresentTimeout'
_b='myIgmpInterfaceLastMembQueryIntvl'
_a='myIgmpInterfaceRobustness'
_Z='myIgmpInterfaceGroups'
_Y='myIgmpInterfaceProxyIfIndex'
_X='myIgmpInterfaceJoins'
_W='myIgmpInterfaceWrongVersionQueries'
_V='myIgmpInterfaceVersion1QuerierTimer'
_U='myIgmpInterfaceQuerierExpiryTime'
_T='myIgmpInterfaceQuerierUpTime'
_S='myIgmpInterfaceQueryMaxResponseTime'
_R='myIgmpInterfaceQuerier'
_Q='myIgmpInterfaceQueryInterval'
_P='tenths of seconds'
_O='seconds'
_N='DisplayString'
_M='Integer32'
_L='InterfaceIndexOrZero'
_K='myIgmpInterfaceHostVersion'
_J='myIgmpInterfaceVersion'
_I='myIgmpInterfaceStaticGroupAddress'
_H='myIgmpInterfaceStaticInterface'
_G='not-accessible'
_F='myIgmpInterfaceIfIndex'
_E='Unsigned32'
_D='read-write'
_C='read-only'
_B='current'
_A='MY-IGMP-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,InterfaceIndexOrZero=mibBuilder.importSymbols('IF-MIB','InterfaceIndex',_L)
myMgmt,=mibBuilder.importSymbols('MY-SMI','myMgmt')
EnabledStatus,=mibBuilder.importSymbols('P-BRIDGE-MIB','EnabledStatus')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,experimental,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_M,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_E,'experimental','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_N,'PhysAddress','RowStatus','TextualConvention','TruthValue')
myIgmpMIB=ModuleIdentity((1,3,6,1,4,1,4881,1,1,10,2,26))
if mibBuilder.loadTexts:myIgmpMIB.setRevisions(('2003-01-20 00:00',))
_MyIgmpMIBObjects_ObjectIdentity=ObjectIdentity
myIgmpMIBObjects=_MyIgmpMIBObjects_ObjectIdentity((1,3,6,1,4,1,4881,1,1,10,2,26,1))
_MyIgmpInterfaceTable_Object=MibTable
myIgmpInterfaceTable=_MyIgmpInterfaceTable_Object((1,3,6,1,4,1,4881,1,1,10,2,26,1,1))
if mibBuilder.loadTexts:myIgmpInterfaceTable.setStatus(_B)
_MyIgmpInterfaceEntry_Object=MibTableRow
myIgmpInterfaceEntry=_MyIgmpInterfaceEntry_Object((1,3,6,1,4,1,4881,1,1,10,2,26,1,1,1))
myIgmpInterfaceEntry.setIndexNames((0,_A,_F))
if mibBuilder.loadTexts:myIgmpInterfaceEntry.setStatus(_B)
_MyIgmpInterfaceIfIndex_Type=InterfaceIndex
_MyIgmpInterfaceIfIndex_Object=MibTableColumn
myIgmpInterfaceIfIndex=_MyIgmpInterfaceIfIndex_Object((1,3,6,1,4,1,4881,1,1,10,2,26,1,1,1,1),_MyIgmpInterfaceIfIndex_Type())
myIgmpInterfaceIfIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:myIgmpInterfaceIfIndex.setStatus(_B)
class _MyIgmpInterfaceQueryInterval_Type(Unsigned32):defaultValue=125;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_MyIgmpInterfaceQueryInterval_Type.__name__=_E
_MyIgmpInterfaceQueryInterval_Object=MibTableColumn
myIgmpInterfaceQueryInterval=_MyIgmpInterfaceQueryInterval_Object((1,3,6,1,4,1,4881,1,1,10,2,26,1,1,1,2),_MyIgmpInterfaceQueryInterval_Type())
myIgmpInterfaceQueryInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:myIgmpInterfaceQueryInterval.setStatus(_B)
if mibBuilder.loadTexts:myIgmpInterfaceQueryInterval.setUnits(_O)
class _MyIgmpInterfaceVersion_Type(Unsigned32):defaultValue=2
_MyIgmpInterfaceVersion_Type.__name__=_E
_MyIgmpInterfaceVersion_Object=MibTableColumn
myIgmpInterfaceVersion=_MyIgmpInterfaceVersion_Object((1,3,6,1,4,1,4881,1,1,10,2,26,1,1,1,3),_MyIgmpInterfaceVersion_Type())
myIgmpInterfaceVersion.setMaxAccess(_D)
if mibBuilder.loadTexts:myIgmpInterfaceVersion.setStatus(_B)
_MyIgmpInterfaceQuerier_Type=IpAddress
_MyIgmpInterfaceQuerier_Object=MibTableColumn
myIgmpInterfaceQuerier=_MyIgmpInterfaceQuerier_Object((1,3,6,1,4,1,4881,1,1,10,2,26,1,1,1,4),_MyIgmpInterfaceQuerier_Type())
myIgmpInterfaceQuerier.setMaxAccess(_C)
if mibBuilder.loadTexts:myIgmpInterfaceQuerier.setStatus(_B)
class _MyIgmpInterfaceQueryMaxResponseTime_Type(Unsigned32):defaultValue=100;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,250))
_MyIgmpInterfaceQueryMaxResponseTime_Type.__name__=_E
_MyIgmpInterfaceQueryMaxResponseTime_Object=MibTableColumn
myIgmpInterfaceQueryMaxResponseTime=_MyIgmpInterfaceQueryMaxResponseTime_Object((1,3,6,1,4,1,4881,1,1,10,2,26,1,1,1,5),_MyIgmpInterfaceQueryMaxResponseTime_Type())
myIgmpInterfaceQueryMaxResponseTime.setMaxAccess(_D)
if mibBuilder.loadTexts:myIgmpInterfaceQueryMaxResponseTime.setStatus(_B)
if mibBuilder.loadTexts:myIgmpInterfaceQueryMaxResponseTime.setUnits(_P)
_MyIgmpInterfaceQuerierUpTime_Type=TimeTicks
_MyIgmpInterfaceQuerierUpTime_Object=MibTableColumn
myIgmpInterfaceQuerierUpTime=_MyIgmpInterfaceQuerierUpTime_Object((1,3,6,1,4,1,4881,1,1,10,2,26,1,1,1,6),_MyIgmpInterfaceQuerierUpTime_Type())
myIgmpInterfaceQuerierUpTime.setMaxAccess(_C)
if mibBuilder.loadTexts:myIgmpInterfaceQuerierUpTime.setStatus(_B)
_MyIgmpInterfaceQuerierExpiryTime_Type=TimeTicks
_MyIgmpInterfaceQuerierExpiryTime_Object=MibTableColumn
myIgmpInterfaceQuerierExpiryTime=_MyIgmpInterfaceQuerierExpiryTime_Object((1,3,6,1,4,1,4881,1,1,10,2,26,1,1,1,7),_MyIgmpInterfaceQuerierExpiryTime_Type())
myIgmpInterfaceQuerierExpiryTime.setMaxAccess(_C)
if mibBuilder.loadTexts:myIgmpInterfaceQuerierExpiryTime.setStatus(_B)
_MyIgmpInterfaceVersion1QuerierTimer_Type=TimeTicks
_MyIgmpInterfaceVersion1QuerierTimer_Object=MibTableColumn
myIgmpInterfaceVersion1QuerierTimer=_MyIgmpInterfaceVersion1QuerierTimer_Object((1,3,6,1,4,1,4881,1,1,10,2,26,1,1,1,8),_MyIgmpInterfaceVersion1QuerierTimer_Type())
myIgmpInterfaceVersion1QuerierTimer.setMaxAccess(_C)
if mibBuilder.loadTexts:myIgmpInterfaceVersion1QuerierTimer.setStatus(_B)
_MyIgmpInterfaceWrongVersionQueries_Type=Counter32
_MyIgmpInterfaceWrongVersionQueries_Object=MibTableColumn
myIgmpInterfaceWrongVersionQueries=_MyIgmpInterfaceWrongVersionQueries_Object((1,3,6,1,4,1,4881,1,1,10,2,26,1,1,1,9),_MyIgmpInterfaceWrongVersionQueries_Type())
myIgmpInterfaceWrongVersionQueries.setMaxAccess(_C)
if mibBuilder.loadTexts:myIgmpInterfaceWrongVersionQueries.setStatus(_B)
_MyIgmpInterfaceJoins_Type=Counter32
_MyIgmpInterfaceJoins_Object=MibTableColumn
myIgmpInterfaceJoins=_MyIgmpInterfaceJoins_Object((1,3,6,1,4,1,4881,1,1,10,2,26,1,1,1,10),_MyIgmpInterfaceJoins_Type())
myIgmpInterfaceJoins.setMaxAccess(_C)
if mibBuilder.loadTexts:myIgmpInterfaceJoins.setStatus(_B)
class _MyIgmpInterfaceProxyIfIndex_Type(InterfaceIndexOrZero):defaultValue=0
_MyIgmpInterfaceProxyIfIndex_Type.__name__=_L
_MyIgmpInterfaceProxyIfIndex_Object=MibTableColumn
myIgmpInterfaceProxyIfIndex=_MyIgmpInterfaceProxyIfIndex_Object((1,3,6,1,4,1,4881,1,1,10,2,26,1,1,1,11),_MyIgmpInterfaceProxyIfIndex_Type())
myIgmpInterfaceProxyIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:myIgmpInterfaceProxyIfIndex.setStatus('obsolete')
_MyIgmpInterfaceGroups_Type=Gauge32
_MyIgmpInterfaceGroups_Object=MibTableColumn
myIgmpInterfaceGroups=_MyIgmpInterfaceGroups_Object((1,3,6,1,4,1,4881,1,1,10,2,26,1,1,1,12),_MyIgmpInterfaceGroups_Type())
myIgmpInterfaceGroups.setMaxAccess(_C)
if mibBuilder.loadTexts:myIgmpInterfaceGroups.setStatus(_B)
class _MyIgmpInterfaceRobustness_Type(Unsigned32):defaultValue=2;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_MyIgmpInterfaceRobustness_Type.__name__=_E
_MyIgmpInterfaceRobustness_Object=MibTableColumn
myIgmpInterfaceRobustness=_MyIgmpInterfaceRobustness_Object((1,3,6,1,4,1,4881,1,1,10,2,26,1,1,1,13),_MyIgmpInterfaceRobustness_Type())
myIgmpInterfaceRobustness.setMaxAccess(_D)
if mibBuilder.loadTexts:myIgmpInterfaceRobustness.setStatus(_B)
class _MyIgmpInterfaceLastMembQueryIntvl_Type(Unsigned32):defaultValue=10;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,655))
_MyIgmpInterfaceLastMembQueryIntvl_Type.__name__=_E
_MyIgmpInterfaceLastMembQueryIntvl_Object=MibTableColumn
myIgmpInterfaceLastMembQueryIntvl=_MyIgmpInterfaceLastMembQueryIntvl_Object((1,3,6,1,4,1,4881,1,1,10,2,26,1,1,1,14),_MyIgmpInterfaceLastMembQueryIntvl_Type())
myIgmpInterfaceLastMembQueryIntvl.setMaxAccess(_D)
if mibBuilder.loadTexts:myIgmpInterfaceLastMembQueryIntvl.setStatus(_B)
if mibBuilder.loadTexts:myIgmpInterfaceLastMembQueryIntvl.setUnits(_P)
class _MyIgmpInterfaceQuerierPresentTimeout_Type(Integer32):defaultValue=265;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(60,300))
_MyIgmpInterfaceQuerierPresentTimeout_Type.__name__=_M
_MyIgmpInterfaceQuerierPresentTimeout_Object=MibTableColumn
myIgmpInterfaceQuerierPresentTimeout=_MyIgmpInterfaceQuerierPresentTimeout_Object((1,3,6,1,4,1,4881,1,1,10,2,26,1,1,1,15),_MyIgmpInterfaceQuerierPresentTimeout_Type())
myIgmpInterfaceQuerierPresentTimeout.setMaxAccess(_D)
if mibBuilder.loadTexts:myIgmpInterfaceQuerierPresentTimeout.setStatus(_B)
if mibBuilder.loadTexts:myIgmpInterfaceQuerierPresentTimeout.setUnits(_O)
_MyIgmpInterfaceLeaves_Type=Counter32
_MyIgmpInterfaceLeaves_Object=MibTableColumn
myIgmpInterfaceLeaves=_MyIgmpInterfaceLeaves_Object((1,3,6,1,4,1,4881,1,1,10,2,26,1,1,1,16),_MyIgmpInterfaceLeaves_Type())
myIgmpInterfaceLeaves.setMaxAccess(_C)
if mibBuilder.loadTexts:myIgmpInterfaceLeaves.setStatus(_B)
class _MyIgmpInterfaceAccessGroupAclName_Type(DisplayString):defaultValue=OctetString('')
_MyIgmpInterfaceAccessGroupAclName_Type.__name__=_N
_MyIgmpInterfaceAccessGroupAclName_Object=MibTableColumn
myIgmpInterfaceAccessGroupAclName=_MyIgmpInterfaceAccessGroupAclName_Object((1,3,6,1,4,1,4881,1,1,10,2,26,1,1,1,17),_MyIgmpInterfaceAccessGroupAclName_Type())
myIgmpInterfaceAccessGroupAclName.setMaxAccess(_D)
if mibBuilder.loadTexts:myIgmpInterfaceAccessGroupAclName.setStatus(_B)
_MyIgmpInterfaceEnabled_Type=EnabledStatus
_MyIgmpInterfaceEnabled_Object=MibTableColumn
myIgmpInterfaceEnabled=_MyIgmpInterfaceEnabled_Object((1,3,6,1,4,1,4881,1,1,10,2,26,1,1,1,18),_MyIgmpInterfaceEnabled_Type())
myIgmpInterfaceEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:myIgmpInterfaceEnabled.setStatus(_B)
_MyIgmpInterfaceHostVersion_Type=Unsigned32
_MyIgmpInterfaceHostVersion_Object=MibTableColumn
myIgmpInterfaceHostVersion=_MyIgmpInterfaceHostVersion_Object((1,3,6,1,4,1,4881,1,1,10,2,26,1,1,1,19),_MyIgmpInterfaceHostVersion_Type())
myIgmpInterfaceHostVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:myIgmpInterfaceHostVersion.setStatus(_B)
_MyIgmpInterfaceStaticTable_Object=MibTable
myIgmpInterfaceStaticTable=_MyIgmpInterfaceStaticTable_Object((1,3,6,1,4,1,4881,1,1,10,2,26,1,2))
if mibBuilder.loadTexts:myIgmpInterfaceStaticTable.setStatus(_B)
_MyIgmpInterfaceStaticEntry_Object=MibTableRow
myIgmpInterfaceStaticEntry=_MyIgmpInterfaceStaticEntry_Object((1,3,6,1,4,1,4881,1,1,10,2,26,1,2,1))
myIgmpInterfaceStaticEntry.setIndexNames((0,_A,_H),(0,_A,_I))
if mibBuilder.loadTexts:myIgmpInterfaceStaticEntry.setStatus(_B)
_MyIgmpInterfaceStaticInterface_Type=InterfaceIndex
_MyIgmpInterfaceStaticInterface_Object=MibTableColumn
myIgmpInterfaceStaticInterface=_MyIgmpInterfaceStaticInterface_Object((1,3,6,1,4,1,4881,1,1,10,2,26,1,2,1,1),_MyIgmpInterfaceStaticInterface_Type())
myIgmpInterfaceStaticInterface.setMaxAccess(_G)
if mibBuilder.loadTexts:myIgmpInterfaceStaticInterface.setStatus(_B)
_MyIgmpInterfaceStaticGroupAddress_Type=IpAddress
_MyIgmpInterfaceStaticGroupAddress_Object=MibTableColumn
myIgmpInterfaceStaticGroupAddress=_MyIgmpInterfaceStaticGroupAddress_Object((1,3,6,1,4,1,4881,1,1,10,2,26,1,2,1,2),_MyIgmpInterfaceStaticGroupAddress_Type())
myIgmpInterfaceStaticGroupAddress.setMaxAccess(_G)
if mibBuilder.loadTexts:myIgmpInterfaceStaticGroupAddress.setStatus(_B)
_MyIgmpInterfaceStaticStatus_Type=RowStatus
_MyIgmpInterfaceStaticStatus_Object=MibTableColumn
myIgmpInterfaceStaticStatus=_MyIgmpInterfaceStaticStatus_Object((1,3,6,1,4,1,4881,1,1,10,2,26,1,2,1,3),_MyIgmpInterfaceStaticStatus_Type())
myIgmpInterfaceStaticStatus.setMaxAccess('read-create')
if mibBuilder.loadTexts:myIgmpInterfaceStaticStatus.setStatus(_B)
_MyIgmpTraps_ObjectIdentity=ObjectIdentity
myIgmpTraps=_MyIgmpTraps_ObjectIdentity((1,3,6,1,4,1,4881,1,1,10,2,26,1,3))
_MyIgmpMIBConformance_ObjectIdentity=ObjectIdentity
myIgmpMIBConformance=_MyIgmpMIBConformance_ObjectIdentity((1,3,6,1,4,1,4881,1,1,10,2,26,2))
_MyIgmpMIBCompliances_ObjectIdentity=ObjectIdentity
myIgmpMIBCompliances=_MyIgmpMIBCompliances_ObjectIdentity((1,3,6,1,4,1,4881,1,1,10,2,26,2,1))
_MyIgmpMIBGroups_ObjectIdentity=ObjectIdentity
myIgmpMIBGroups=_MyIgmpMIBGroups_ObjectIdentity((1,3,6,1,4,1,4881,1,1,10,2,26,2,2))
myIgmpInterfaceMIBGroup=ObjectGroup((1,3,6,1,4,1,4881,1,1,10,2,26,2,2,1))
myIgmpInterfaceMIBGroup.setObjects(*((_A,_F),(_A,_Q),(_A,_J),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_K)))
if mibBuilder.loadTexts:myIgmpInterfaceMIBGroup.setStatus(_B)
myIgmpInterfaceStaticMIBGroup=ObjectGroup((1,3,6,1,4,1,4881,1,1,10,2,26,2,2,2))
myIgmpInterfaceStaticMIBGroup.setObjects(*((_A,_H),(_A,_I),(_A,_g)))
if mibBuilder.loadTexts:myIgmpInterfaceStaticMIBGroup.setStatus(_B)
myIgmpVersionConflicted=NotificationType((1,3,6,1,4,1,4881,1,1,10,2,26,1,3,1))
myIgmpVersionConflicted.setObjects(*((_A,_F),(_A,_J),(_A,_K)))
if mibBuilder.loadTexts:myIgmpVersionConflicted.setStatus(_B)
myIgmpMIBCompliance=ModuleCompliance((1,3,6,1,4,1,4881,1,1,10,2,26,2,1,1))
myIgmpMIBCompliance.setObjects(*((_A,_h),(_A,_i)))
if mibBuilder.loadTexts:myIgmpMIBCompliance.setStatus(_B)
igmpExternCompliance=ModuleCompliance((1,3,6,1,4,1,4881,1,1,10,2,26,2,1,2))
if mibBuilder.loadTexts:igmpExternCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'myIgmpMIB':myIgmpMIB,'myIgmpMIBObjects':myIgmpMIBObjects,'myIgmpInterfaceTable':myIgmpInterfaceTable,'myIgmpInterfaceEntry':myIgmpInterfaceEntry,_F:myIgmpInterfaceIfIndex,_Q:myIgmpInterfaceQueryInterval,_J:myIgmpInterfaceVersion,_R:myIgmpInterfaceQuerier,_S:myIgmpInterfaceQueryMaxResponseTime,_T:myIgmpInterfaceQuerierUpTime,_U:myIgmpInterfaceQuerierExpiryTime,_V:myIgmpInterfaceVersion1QuerierTimer,_W:myIgmpInterfaceWrongVersionQueries,_X:myIgmpInterfaceJoins,_Y:myIgmpInterfaceProxyIfIndex,_Z:myIgmpInterfaceGroups,_a:myIgmpInterfaceRobustness,_b:myIgmpInterfaceLastMembQueryIntvl,_c:myIgmpInterfaceQuerierPresentTimeout,_d:myIgmpInterfaceLeaves,_e:myIgmpInterfaceAccessGroupAclName,_f:myIgmpInterfaceEnabled,_K:myIgmpInterfaceHostVersion,'myIgmpInterfaceStaticTable':myIgmpInterfaceStaticTable,'myIgmpInterfaceStaticEntry':myIgmpInterfaceStaticEntry,_H:myIgmpInterfaceStaticInterface,_I:myIgmpInterfaceStaticGroupAddress,_g:myIgmpInterfaceStaticStatus,'myIgmpTraps':myIgmpTraps,'myIgmpVersionConflicted':myIgmpVersionConflicted,'myIgmpMIBConformance':myIgmpMIBConformance,'myIgmpMIBCompliances':myIgmpMIBCompliances,'myIgmpMIBCompliance':myIgmpMIBCompliance,'igmpExternCompliance':igmpExternCompliance,'myIgmpMIBGroups':myIgmpMIBGroups,_h:myIgmpInterfaceMIBGroup,_i:myIgmpInterfaceStaticMIBGroup})