_Y='extremeCfmNotificationsGroup'
_X='extremeCfmMepDbGroup'
_W='extremeCfmMepGroup'
_V='extremeCfmGroupStatusDownUpAlarm'
_U='extremeCfmGroupMepDbRowStatus'
_T='extremeCfmGroupRowStatus'
_S='extremeCfmGroupClients'
_R='extremeCfmGroupRemoteMEPs'
_Q='extremeCfmMepIfIndex'
_P='extremeCfmGroupName'
_O='extremeCfmGroupNextIndex'
_N='extremeCfmGroupMepDbRMepId'
_M='not-accessible'
_L='Unsigned32'
_K='extremeCfmGroupStatus'
_J='read-create'
_I='extremeCfmGroupIndex'
_H='DisplayString'
_G='dot1agCfmMepIdentifier'
_F='dot1agCfmMdIndex'
_E='dot1agCfmMaIndex'
_D='read-only'
_C='IEEE8021-CFM-MIB'
_B='EXTREME-CFM-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
extremeAgent,=mibBuilder.importSymbols('EXTREME-BASE-MIB','extremeAgent')
Dot1afCfmIndexIntegerNextFree,Dot1agCfmMepId,dot1agCfmMaIndex,dot1agCfmMdIndex,dot1agCfmMepIdentifier=mibBuilder.importSymbols(_C,'Dot1afCfmIndexIntegerNextFree','Dot1agCfmMepId',_E,_F,_G)
InterfaceIndexOrZero,=mibBuilder.importSymbols('IF-MIB','InterfaceIndexOrZero')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_L,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_H,'PhysAddress','RowStatus','TextualConvention')
extremeCfm=ModuleIdentity((1,3,6,1,4,1,1916,1,47))
if mibBuilder.loadTexts:extremeCfm.setRevisions(('2015-05-18 00:00',))
class ExtremeCfmGroupOperStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('down',1),('up',2)))
_ExtremeCfmNotifications_ObjectIdentity=ObjectIdentity
extremeCfmNotifications=_ExtremeCfmNotifications_ObjectIdentity((1,3,6,1,4,1,1916,1,47,0))
_ExtremeCfmMibObjects_ObjectIdentity=ObjectIdentity
extremeCfmMibObjects=_ExtremeCfmMibObjects_ObjectIdentity((1,3,6,1,4,1,1916,1,47,1))
_ExtremeCfmGroup_ObjectIdentity=ObjectIdentity
extremeCfmGroup=_ExtremeCfmGroup_ObjectIdentity((1,3,6,1,4,1,1916,1,47,1,1))
_ExtremeCfmGroupNextIndexTable_Object=MibTable
extremeCfmGroupNextIndexTable=_ExtremeCfmGroupNextIndexTable_Object((1,3,6,1,4,1,1916,1,47,1,1,1))
if mibBuilder.loadTexts:extremeCfmGroupNextIndexTable.setStatus(_A)
_ExtremeCfmGroupNextIndexEntry_Object=MibTableRow
extremeCfmGroupNextIndexEntry=_ExtremeCfmGroupNextIndexEntry_Object((1,3,6,1,4,1,1916,1,47,1,1,1,1))
extremeCfmGroupNextIndexEntry.setIndexNames((0,_C,_F),(0,_C,_E),(0,_C,_G))
if mibBuilder.loadTexts:extremeCfmGroupNextIndexEntry.setStatus(_A)
_ExtremeCfmGroupNextIndex_Type=Dot1afCfmIndexIntegerNextFree
_ExtremeCfmGroupNextIndex_Object=MibTableColumn
extremeCfmGroupNextIndex=_ExtremeCfmGroupNextIndex_Object((1,3,6,1,4,1,1916,1,47,1,1,1,1,1),_ExtremeCfmGroupNextIndex_Type())
extremeCfmGroupNextIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:extremeCfmGroupNextIndex.setStatus(_A)
_ExtremeCfmGroupTable_Object=MibTable
extremeCfmGroupTable=_ExtremeCfmGroupTable_Object((1,3,6,1,4,1,1916,1,47,1,1,2))
if mibBuilder.loadTexts:extremeCfmGroupTable.setStatus(_A)
_ExtremeCfmGroupEntry_Object=MibTableRow
extremeCfmGroupEntry=_ExtremeCfmGroupEntry_Object((1,3,6,1,4,1,1916,1,47,1,1,2,1))
extremeCfmGroupEntry.setIndexNames((0,_C,_F),(0,_C,_E),(0,_C,_G),(0,_B,_I))
if mibBuilder.loadTexts:extremeCfmGroupEntry.setStatus(_A)
class _ExtremeCfmGroupIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_ExtremeCfmGroupIndex_Type.__name__=_L
_ExtremeCfmGroupIndex_Object=MibTableColumn
extremeCfmGroupIndex=_ExtremeCfmGroupIndex_Object((1,3,6,1,4,1,1916,1,47,1,1,2,1,1),_ExtremeCfmGroupIndex_Type())
extremeCfmGroupIndex.setMaxAccess(_M)
if mibBuilder.loadTexts:extremeCfmGroupIndex.setStatus(_A)
class _ExtremeCfmGroupName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,31))
_ExtremeCfmGroupName_Type.__name__=_H
_ExtremeCfmGroupName_Object=MibTableColumn
extremeCfmGroupName=_ExtremeCfmGroupName_Object((1,3,6,1,4,1,1916,1,47,1,1,2,1,2),_ExtremeCfmGroupName_Type())
extremeCfmGroupName.setMaxAccess(_J)
if mibBuilder.loadTexts:extremeCfmGroupName.setStatus(_A)
_ExtremeCfmGroupStatus_Type=ExtremeCfmGroupOperStatus
_ExtremeCfmGroupStatus_Object=MibTableColumn
extremeCfmGroupStatus=_ExtremeCfmGroupStatus_Object((1,3,6,1,4,1,1916,1,47,1,1,2,1,3),_ExtremeCfmGroupStatus_Type())
extremeCfmGroupStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:extremeCfmGroupStatus.setStatus(_A)
_ExtremeCfmMepIfIndex_Type=InterfaceIndexOrZero
_ExtremeCfmMepIfIndex_Object=MibTableColumn
extremeCfmMepIfIndex=_ExtremeCfmMepIfIndex_Object((1,3,6,1,4,1,1916,1,47,1,1,2,1,4),_ExtremeCfmMepIfIndex_Type())
extremeCfmMepIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:extremeCfmMepIfIndex.setStatus(_A)
class _ExtremeCfmGroupRemoteMEPs_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
_ExtremeCfmGroupRemoteMEPs_Type.__name__=_H
_ExtremeCfmGroupRemoteMEPs_Object=MibTableColumn
extremeCfmGroupRemoteMEPs=_ExtremeCfmGroupRemoteMEPs_Object((1,3,6,1,4,1,1916,1,47,1,1,2,1,5),_ExtremeCfmGroupRemoteMEPs_Type())
extremeCfmGroupRemoteMEPs.setMaxAccess(_D)
if mibBuilder.loadTexts:extremeCfmGroupRemoteMEPs.setStatus(_A)
class _ExtremeCfmGroupClients_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
_ExtremeCfmGroupClients_Type.__name__=_H
_ExtremeCfmGroupClients_Object=MibTableColumn
extremeCfmGroupClients=_ExtremeCfmGroupClients_Object((1,3,6,1,4,1,1916,1,47,1,1,2,1,6),_ExtremeCfmGroupClients_Type())
extremeCfmGroupClients.setMaxAccess(_D)
if mibBuilder.loadTexts:extremeCfmGroupClients.setStatus(_A)
_ExtremeCfmGroupRowStatus_Type=RowStatus
_ExtremeCfmGroupRowStatus_Object=MibTableColumn
extremeCfmGroupRowStatus=_ExtremeCfmGroupRowStatus_Object((1,3,6,1,4,1,1916,1,47,1,1,2,1,7),_ExtremeCfmGroupRowStatus_Type())
extremeCfmGroupRowStatus.setMaxAccess(_J)
if mibBuilder.loadTexts:extremeCfmGroupRowStatus.setStatus(_A)
_ExtremeCfmGroupMepDbTable_Object=MibTable
extremeCfmGroupMepDbTable=_ExtremeCfmGroupMepDbTable_Object((1,3,6,1,4,1,1916,1,47,1,1,3))
if mibBuilder.loadTexts:extremeCfmGroupMepDbTable.setStatus(_A)
_ExtremeCfmGroupMepDbEntry_Object=MibTableRow
extremeCfmGroupMepDbEntry=_ExtremeCfmGroupMepDbEntry_Object((1,3,6,1,4,1,1916,1,47,1,1,3,1))
extremeCfmGroupMepDbEntry.setIndexNames((0,_C,_F),(0,_C,_E),(0,_C,_G),(0,_B,_I),(0,_B,_N))
if mibBuilder.loadTexts:extremeCfmGroupMepDbEntry.setStatus(_A)
_ExtremeCfmGroupMepDbRMepId_Type=Dot1agCfmMepId
_ExtremeCfmGroupMepDbRMepId_Object=MibTableColumn
extremeCfmGroupMepDbRMepId=_ExtremeCfmGroupMepDbRMepId_Object((1,3,6,1,4,1,1916,1,47,1,1,3,1,1),_ExtremeCfmGroupMepDbRMepId_Type())
extremeCfmGroupMepDbRMepId.setMaxAccess(_M)
if mibBuilder.loadTexts:extremeCfmGroupMepDbRMepId.setStatus(_A)
_ExtremeCfmGroupMepDbRowStatus_Type=RowStatus
_ExtremeCfmGroupMepDbRowStatus_Object=MibTableColumn
extremeCfmGroupMepDbRowStatus=_ExtremeCfmGroupMepDbRowStatus_Object((1,3,6,1,4,1,1916,1,47,1,1,3,1,2),_ExtremeCfmGroupMepDbRowStatus_Type())
extremeCfmGroupMepDbRowStatus.setMaxAccess(_J)
if mibBuilder.loadTexts:extremeCfmGroupMepDbRowStatus.setStatus(_A)
_ExtremeCfmMibConformance_ObjectIdentity=ObjectIdentity
extremeCfmMibConformance=_ExtremeCfmMibConformance_ObjectIdentity((1,3,6,1,4,1,1916,1,47,2))
_ExtremeCfmMibCompliances_ObjectIdentity=ObjectIdentity
extremeCfmMibCompliances=_ExtremeCfmMibCompliances_ObjectIdentity((1,3,6,1,4,1,1916,1,47,2,1))
_ExtremeCfmMibGroups_ObjectIdentity=ObjectIdentity
extremeCfmMibGroups=_ExtremeCfmMibGroups_ObjectIdentity((1,3,6,1,4,1,1916,1,47,2,2))
extremeCfmMepGroup=ObjectGroup((1,3,6,1,4,1,1916,1,47,2,2,1))
extremeCfmMepGroup.setObjects(*((_B,_O),(_B,_P),(_B,_K),(_B,_Q),(_B,_R),(_B,_S),(_B,_T)))
if mibBuilder.loadTexts:extremeCfmMepGroup.setStatus(_A)
extremeCfmMepDbGroup=ObjectGroup((1,3,6,1,4,1,1916,1,47,2,2,2))
extremeCfmMepDbGroup.setObjects((_B,_U))
if mibBuilder.loadTexts:extremeCfmMepDbGroup.setStatus(_A)
extremeCfmGroupStatusDownUpAlarm=NotificationType((1,3,6,1,4,1,1916,1,47,0,1))
extremeCfmGroupStatusDownUpAlarm.setObjects((_B,_K))
if mibBuilder.loadTexts:extremeCfmGroupStatusDownUpAlarm.setStatus(_A)
extremeCfmNotificationsGroup=NotificationGroup((1,3,6,1,4,1,1916,1,47,2,2,3))
extremeCfmNotificationsGroup.setObjects((_B,_V))
if mibBuilder.loadTexts:extremeCfmNotificationsGroup.setStatus(_A)
extremeCfmCompliance=ModuleCompliance((1,3,6,1,4,1,1916,1,47,2,1,1))
extremeCfmCompliance.setObjects(*((_B,_W),(_B,_X),(_B,_Y)))
if mibBuilder.loadTexts:extremeCfmCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ExtremeCfmGroupOperStatus':ExtremeCfmGroupOperStatus,'extremeCfm':extremeCfm,'extremeCfmNotifications':extremeCfmNotifications,_V:extremeCfmGroupStatusDownUpAlarm,'extremeCfmMibObjects':extremeCfmMibObjects,'extremeCfmGroup':extremeCfmGroup,'extremeCfmGroupNextIndexTable':extremeCfmGroupNextIndexTable,'extremeCfmGroupNextIndexEntry':extremeCfmGroupNextIndexEntry,_O:extremeCfmGroupNextIndex,'extremeCfmGroupTable':extremeCfmGroupTable,'extremeCfmGroupEntry':extremeCfmGroupEntry,_I:extremeCfmGroupIndex,_P:extremeCfmGroupName,_K:extremeCfmGroupStatus,_Q:extremeCfmMepIfIndex,_R:extremeCfmGroupRemoteMEPs,_S:extremeCfmGroupClients,_T:extremeCfmGroupRowStatus,'extremeCfmGroupMepDbTable':extremeCfmGroupMepDbTable,'extremeCfmGroupMepDbEntry':extremeCfmGroupMepDbEntry,_N:extremeCfmGroupMepDbRMepId,_U:extremeCfmGroupMepDbRowStatus,'extremeCfmMibConformance':extremeCfmMibConformance,'extremeCfmMibCompliances':extremeCfmMibCompliances,'extremeCfmCompliance':extremeCfmCompliance,'extremeCfmMibGroups':extremeCfmMibGroups,_W:extremeCfmMepGroup,_X:extremeCfmMepDbGroup,_Y:extremeCfmNotificationsGroup})