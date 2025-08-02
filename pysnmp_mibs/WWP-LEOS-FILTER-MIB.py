_L='wwpLeosFilterPortId'
_K='wwpLeosFilterVlan'
_J='disabled'
_I='enabled'
_H='wwpLeosFilterProtocolIndex'
_G='OctetString'
_F='wwpLeosFilterIndex'
_E='WWP-LEOS-FILTER-MIB'
_D='read-only'
_C='read-create'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_G,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
wwpModulesLeos,=mibBuilder.importSymbols('WWP-SMI','wwpModulesLeos')
wwpLeosFilterMIB=ModuleIdentity((1,3,6,1,4,1,6141,2,60,15))
if mibBuilder.loadTexts:wwpLeosFilterMIB.setRevisions(('2006-02-17 18:45','2003-01-15 17:00'))
_WwpLeosFilterMIBObjects_ObjectIdentity=ObjectIdentity
wwpLeosFilterMIBObjects=_WwpLeosFilterMIBObjects_ObjectIdentity((1,3,6,1,4,1,6141,2,60,15,1))
_WwpLeosFilter_ObjectIdentity=ObjectIdentity
wwpLeosFilter=_WwpLeosFilter_ObjectIdentity((1,3,6,1,4,1,6141,2,60,15,1,1))
_WwpLeosFilterResources_ObjectIdentity=ObjectIdentity
wwpLeosFilterResources=_WwpLeosFilterResources_ObjectIdentity((1,3,6,1,4,1,6141,2,60,15,1,1,1))
_WwpLeosFilterMaxHardwareResources_Type=Unsigned32
_WwpLeosFilterMaxHardwareResources_Object=MibScalar
wwpLeosFilterMaxHardwareResources=_WwpLeosFilterMaxHardwareResources_Object((1,3,6,1,4,1,6141,2,60,15,1,1,1,1),_WwpLeosFilterMaxHardwareResources_Type())
wwpLeosFilterMaxHardwareResources.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosFilterMaxHardwareResources.setStatus(_A)
_WwpLeosFilterUsedHardwareResources_Type=Unsigned32
_WwpLeosFilterUsedHardwareResources_Object=MibScalar
wwpLeosFilterUsedHardwareResources=_WwpLeosFilterUsedHardwareResources_Object((1,3,6,1,4,1,6141,2,60,15,1,1,1,2),_WwpLeosFilterUsedHardwareResources_Type())
wwpLeosFilterUsedHardwareResources.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosFilterUsedHardwareResources.setStatus(_A)
_WwpLeosFilterCreated_Type=Unsigned32
_WwpLeosFilterCreated_Object=MibScalar
wwpLeosFilterCreated=_WwpLeosFilterCreated_Object((1,3,6,1,4,1,6141,2,60,15,1,1,1,3),_WwpLeosFilterCreated_Type())
wwpLeosFilterCreated.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosFilterCreated.setStatus(_A)
_WwpLeosFilterCountersMax_Type=Unsigned32
_WwpLeosFilterCountersMax_Object=MibScalar
wwpLeosFilterCountersMax=_WwpLeosFilterCountersMax_Object((1,3,6,1,4,1,6141,2,60,15,1,1,1,4),_WwpLeosFilterCountersMax_Type())
wwpLeosFilterCountersMax.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosFilterCountersMax.setStatus(_A)
_WwpLeosFilterCountersUsed_Type=Unsigned32
_WwpLeosFilterCountersUsed_Object=MibScalar
wwpLeosFilterCountersUsed=_WwpLeosFilterCountersUsed_Object((1,3,6,1,4,1,6141,2,60,15,1,1,1,5),_WwpLeosFilterCountersUsed_Type())
wwpLeosFilterCountersUsed.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosFilterCountersUsed.setStatus(_A)
_WwpLeosFilterTable_Object=MibTable
wwpLeosFilterTable=_WwpLeosFilterTable_Object((1,3,6,1,4,1,6141,2,60,15,1,1,2))
if mibBuilder.loadTexts:wwpLeosFilterTable.setStatus(_A)
_WwpLeosFilterEntry_Object=MibTableRow
wwpLeosFilterEntry=_WwpLeosFilterEntry_Object((1,3,6,1,4,1,6141,2,60,15,1,1,2,1))
wwpLeosFilterEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:wwpLeosFilterEntry.setStatus(_A)
class _WwpLeosFilterIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,64))
_WwpLeosFilterIndex_Type.__name__=_B
_WwpLeosFilterIndex_Object=MibTableColumn
wwpLeosFilterIndex=_WwpLeosFilterIndex_Object((1,3,6,1,4,1,6141,2,60,15,1,1,2,1,1),_WwpLeosFilterIndex_Type())
wwpLeosFilterIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosFilterIndex.setStatus(_A)
class _WwpLeosFilterName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,16))
_WwpLeosFilterName_Type.__name__=_G
_WwpLeosFilterName_Object=MibTableColumn
wwpLeosFilterName=_WwpLeosFilterName_Object((1,3,6,1,4,1,6141,2,60,15,1,1,2,1,2),_WwpLeosFilterName_Type())
wwpLeosFilterName.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosFilterName.setStatus(_A)
class _WwpLeosFilterAdminState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_WwpLeosFilterAdminState_Type.__name__=_B
_WwpLeosFilterAdminState_Object=MibTableColumn
wwpLeosFilterAdminState=_WwpLeosFilterAdminState_Object((1,3,6,1,4,1,6141,2,60,15,1,1,2,1,3),_WwpLeosFilterAdminState_Type())
wwpLeosFilterAdminState.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosFilterAdminState.setStatus(_A)
class _WwpLeosFilterOperState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_WwpLeosFilterOperState_Type.__name__=_B
_WwpLeosFilterOperState_Object=MibTableColumn
wwpLeosFilterOperState=_WwpLeosFilterOperState_Object((1,3,6,1,4,1,6141,2,60,15,1,1,2,1,4),_WwpLeosFilterOperState_Type())
wwpLeosFilterOperState.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosFilterOperState.setStatus(_A)
class _WwpLeosFilterCounter_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('on',1),('off',2)))
_WwpLeosFilterCounter_Type.__name__=_B
_WwpLeosFilterCounter_Object=MibTableColumn
wwpLeosFilterCounter=_WwpLeosFilterCounter_Object((1,3,6,1,4,1,6141,2,60,15,1,1,2,1,5),_WwpLeosFilterCounter_Type())
wwpLeosFilterCounter.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosFilterCounter.setStatus(_A)
_WwpLeosFilterStatus_Type=RowStatus
_WwpLeosFilterStatus_Object=MibTableColumn
wwpLeosFilterStatus=_WwpLeosFilterStatus_Object((1,3,6,1,4,1,6141,2,60,15,1,1,2,1,6),_WwpLeosFilterStatus_Type())
wwpLeosFilterStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosFilterStatus.setStatus(_A)
_WwpLeosFilterProtocolTable_Object=MibTable
wwpLeosFilterProtocolTable=_WwpLeosFilterProtocolTable_Object((1,3,6,1,4,1,6141,2,60,15,1,1,3))
if mibBuilder.loadTexts:wwpLeosFilterProtocolTable.setStatus(_A)
_WwpLeosFilterProtocolEntry_Object=MibTableRow
wwpLeosFilterProtocolEntry=_WwpLeosFilterProtocolEntry_Object((1,3,6,1,4,1,6141,2,60,15,1,1,3,1))
wwpLeosFilterProtocolEntry.setIndexNames((0,_E,_H))
if mibBuilder.loadTexts:wwpLeosFilterProtocolEntry.setStatus(_A)
class _WwpLeosFilterProtocolIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,41))
_WwpLeosFilterProtocolIndex_Type.__name__=_B
_WwpLeosFilterProtocolIndex_Object=MibTableColumn
wwpLeosFilterProtocolIndex=_WwpLeosFilterProtocolIndex_Object((1,3,6,1,4,1,6141,2,60,15,1,1,3,1,1),_WwpLeosFilterProtocolIndex_Type())
wwpLeosFilterProtocolIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosFilterProtocolIndex.setStatus(_A)
class _WwpLeosFilterProtocolName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,16))
_WwpLeosFilterProtocolName_Type.__name__=_G
_WwpLeosFilterProtocolName_Object=MibTableColumn
wwpLeosFilterProtocolName=_WwpLeosFilterProtocolName_Object((1,3,6,1,4,1,6141,2,60,15,1,1,3,1,2),_WwpLeosFilterProtocolName_Type())
wwpLeosFilterProtocolName.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosFilterProtocolName.setStatus(_A)
class _WwpLeosFilterProtocolType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_WwpLeosFilterProtocolType_Type.__name__=_B
_WwpLeosFilterProtocolType_Object=MibTableColumn
wwpLeosFilterProtocolType=_WwpLeosFilterProtocolType_Object((1,3,6,1,4,1,6141,2,60,15,1,1,3,1,3),_WwpLeosFilterProtocolType_Type())
wwpLeosFilterProtocolType.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosFilterProtocolType.setStatus(_A)
class _WwpLeosFilterProtocolSrcPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_WwpLeosFilterProtocolSrcPort_Type.__name__=_B
_WwpLeosFilterProtocolSrcPort_Object=MibTableColumn
wwpLeosFilterProtocolSrcPort=_WwpLeosFilterProtocolSrcPort_Object((1,3,6,1,4,1,6141,2,60,15,1,1,3,1,4),_WwpLeosFilterProtocolSrcPort_Type())
wwpLeosFilterProtocolSrcPort.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosFilterProtocolSrcPort.setStatus(_A)
class _WwpLeosFilterProtocolDstPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_WwpLeosFilterProtocolDstPort_Type.__name__=_B
_WwpLeosFilterProtocolDstPort_Object=MibTableColumn
wwpLeosFilterProtocolDstPort=_WwpLeosFilterProtocolDstPort_Object((1,3,6,1,4,1,6141,2,60,15,1,1,3,1,5),_WwpLeosFilterProtocolDstPort_Type())
wwpLeosFilterProtocolDstPort.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosFilterProtocolDstPort.setStatus(_A)
_WwpLeosFilterProtocolStatus_Type=RowStatus
_WwpLeosFilterProtocolStatus_Object=MibTableColumn
wwpLeosFilterProtocolStatus=_WwpLeosFilterProtocolStatus_Object((1,3,6,1,4,1,6141,2,60,15,1,1,3,1,6),_WwpLeosFilterProtocolStatus_Type())
wwpLeosFilterProtocolStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosFilterProtocolStatus.setStatus(_A)
_WwpLeosFilterMemTable_Object=MibTable
wwpLeosFilterMemTable=_WwpLeosFilterMemTable_Object((1,3,6,1,4,1,6141,2,60,15,1,1,4))
if mibBuilder.loadTexts:wwpLeosFilterMemTable.setStatus(_A)
_WwpLeosFilterMemEntry_Object=MibTableRow
wwpLeosFilterMemEntry=_WwpLeosFilterMemEntry_Object((1,3,6,1,4,1,6141,2,60,15,1,1,4,1))
wwpLeosFilterMemEntry.setIndexNames((0,_E,_F),(0,_E,_K),(0,_E,_L))
if mibBuilder.loadTexts:wwpLeosFilterMemEntry.setStatus(_A)
class _WwpLeosFilterVlan_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,24576))
_WwpLeosFilterVlan_Type.__name__=_B
_WwpLeosFilterVlan_Object=MibTableColumn
wwpLeosFilterVlan=_WwpLeosFilterVlan_Object((1,3,6,1,4,1,6141,2,60,15,1,1,4,1,1),_WwpLeosFilterVlan_Type())
wwpLeosFilterVlan.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosFilterVlan.setStatus(_A)
class _WwpLeosFilterPortId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_WwpLeosFilterPortId_Type.__name__=_B
_WwpLeosFilterPortId_Object=MibTableColumn
wwpLeosFilterPortId=_WwpLeosFilterPortId_Object((1,3,6,1,4,1,6141,2,60,15,1,1,4,1,2),_WwpLeosFilterPortId_Type())
wwpLeosFilterPortId.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosFilterPortId.setStatus(_A)
_WwpLeosFilterMemStatus_Type=RowStatus
_WwpLeosFilterMemStatus_Object=MibTableColumn
wwpLeosFilterMemStatus=_WwpLeosFilterMemStatus_Object((1,3,6,1,4,1,6141,2,60,15,1,1,4,1,3),_WwpLeosFilterMemStatus_Type())
wwpLeosFilterMemStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosFilterMemStatus.setStatus(_A)
class _WwpLeosFilterMemRule_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('block',1),('allow',2)))
_WwpLeosFilterMemRule_Type.__name__=_B
_WwpLeosFilterMemRule_Object=MibTableColumn
wwpLeosFilterMemRule=_WwpLeosFilterMemRule_Object((1,3,6,1,4,1,6141,2,60,15,1,1,4,1,4),_WwpLeosFilterMemRule_Type())
wwpLeosFilterMemRule.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosFilterMemRule.setStatus(_A)
_WwpLeosFilterProtocolMemTable_Object=MibTable
wwpLeosFilterProtocolMemTable=_WwpLeosFilterProtocolMemTable_Object((1,3,6,1,4,1,6141,2,60,15,1,1,5))
if mibBuilder.loadTexts:wwpLeosFilterProtocolMemTable.setStatus(_A)
_WwpLeosFilterProtocolMemEntry_Object=MibTableRow
wwpLeosFilterProtocolMemEntry=_WwpLeosFilterProtocolMemEntry_Object((1,3,6,1,4,1,6141,2,60,15,1,1,5,1))
wwpLeosFilterProtocolMemEntry.setIndexNames((0,_E,_F),(0,_E,_H))
if mibBuilder.loadTexts:wwpLeosFilterProtocolMemEntry.setStatus(_A)
_WwpLeosFilterProtocolMemStatus_Type=RowStatus
_WwpLeosFilterProtocolMemStatus_Object=MibTableColumn
wwpLeosFilterProtocolMemStatus=_WwpLeosFilterProtocolMemStatus_Object((1,3,6,1,4,1,6141,2,60,15,1,1,5,1,1),_WwpLeosFilterProtocolMemStatus_Type())
wwpLeosFilterProtocolMemStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosFilterProtocolMemStatus.setStatus(_A)
_WwpLeosFilterStatsTable_Object=MibTable
wwpLeosFilterStatsTable=_WwpLeosFilterStatsTable_Object((1,3,6,1,4,1,6141,2,60,15,1,1,6))
if mibBuilder.loadTexts:wwpLeosFilterStatsTable.setStatus(_A)
_WwpLeosFilterStatsEntry_Object=MibTableRow
wwpLeosFilterStatsEntry=_WwpLeosFilterStatsEntry_Object((1,3,6,1,4,1,6141,2,60,15,1,1,6,1))
wwpLeosFilterStatsEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:wwpLeosFilterStatsEntry.setStatus(_A)
_WwpLeosFilterDropBytes_Type=Counter32
_WwpLeosFilterDropBytes_Object=MibTableColumn
wwpLeosFilterDropBytes=_WwpLeosFilterDropBytes_Object((1,3,6,1,4,1,6141,2,60,15,1,1,6,1,1),_WwpLeosFilterDropBytes_Type())
wwpLeosFilterDropBytes.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosFilterDropBytes.setStatus(_A)
_WwpLeosFilterMIBNotificationPrefix_ObjectIdentity=ObjectIdentity
wwpLeosFilterMIBNotificationPrefix=_WwpLeosFilterMIBNotificationPrefix_ObjectIdentity((1,3,6,1,4,1,6141,2,60,15,2))
_WwpLeosFilterMIBNotifications_ObjectIdentity=ObjectIdentity
wwpLeosFilterMIBNotifications=_WwpLeosFilterMIBNotifications_ObjectIdentity((1,3,6,1,4,1,6141,2,60,15,2,0))
_WwpLeosFilterMIBConformance_ObjectIdentity=ObjectIdentity
wwpLeosFilterMIBConformance=_WwpLeosFilterMIBConformance_ObjectIdentity((1,3,6,1,4,1,6141,2,60,15,3))
_WwpLeosFilterMIBCompliances_ObjectIdentity=ObjectIdentity
wwpLeosFilterMIBCompliances=_WwpLeosFilterMIBCompliances_ObjectIdentity((1,3,6,1,4,1,6141,2,60,15,3,1))
_WwpLeosFilterMIBGroups_ObjectIdentity=ObjectIdentity
wwpLeosFilterMIBGroups=_WwpLeosFilterMIBGroups_ObjectIdentity((1,3,6,1,4,1,6141,2,60,15,3,2))
mibBuilder.exportSymbols(_E,**{'wwpLeosFilterMIB':wwpLeosFilterMIB,'wwpLeosFilterMIBObjects':wwpLeosFilterMIBObjects,'wwpLeosFilter':wwpLeosFilter,'wwpLeosFilterResources':wwpLeosFilterResources,'wwpLeosFilterMaxHardwareResources':wwpLeosFilterMaxHardwareResources,'wwpLeosFilterUsedHardwareResources':wwpLeosFilterUsedHardwareResources,'wwpLeosFilterCreated':wwpLeosFilterCreated,'wwpLeosFilterCountersMax':wwpLeosFilterCountersMax,'wwpLeosFilterCountersUsed':wwpLeosFilterCountersUsed,'wwpLeosFilterTable':wwpLeosFilterTable,'wwpLeosFilterEntry':wwpLeosFilterEntry,_F:wwpLeosFilterIndex,'wwpLeosFilterName':wwpLeosFilterName,'wwpLeosFilterAdminState':wwpLeosFilterAdminState,'wwpLeosFilterOperState':wwpLeosFilterOperState,'wwpLeosFilterCounter':wwpLeosFilterCounter,'wwpLeosFilterStatus':wwpLeosFilterStatus,'wwpLeosFilterProtocolTable':wwpLeosFilterProtocolTable,'wwpLeosFilterProtocolEntry':wwpLeosFilterProtocolEntry,_H:wwpLeosFilterProtocolIndex,'wwpLeosFilterProtocolName':wwpLeosFilterProtocolName,'wwpLeosFilterProtocolType':wwpLeosFilterProtocolType,'wwpLeosFilterProtocolSrcPort':wwpLeosFilterProtocolSrcPort,'wwpLeosFilterProtocolDstPort':wwpLeosFilterProtocolDstPort,'wwpLeosFilterProtocolStatus':wwpLeosFilterProtocolStatus,'wwpLeosFilterMemTable':wwpLeosFilterMemTable,'wwpLeosFilterMemEntry':wwpLeosFilterMemEntry,_K:wwpLeosFilterVlan,_L:wwpLeosFilterPortId,'wwpLeosFilterMemStatus':wwpLeosFilterMemStatus,'wwpLeosFilterMemRule':wwpLeosFilterMemRule,'wwpLeosFilterProtocolMemTable':wwpLeosFilterProtocolMemTable,'wwpLeosFilterProtocolMemEntry':wwpLeosFilterProtocolMemEntry,'wwpLeosFilterProtocolMemStatus':wwpLeosFilterProtocolMemStatus,'wwpLeosFilterStatsTable':wwpLeosFilterStatsTable,'wwpLeosFilterStatsEntry':wwpLeosFilterStatsEntry,'wwpLeosFilterDropBytes':wwpLeosFilterDropBytes,'wwpLeosFilterMIBNotificationPrefix':wwpLeosFilterMIBNotificationPrefix,'wwpLeosFilterMIBNotifications':wwpLeosFilterMIBNotifications,'wwpLeosFilterMIBConformance':wwpLeosFilterMIBConformance,'wwpLeosFilterMIBCompliances':wwpLeosFilterMIBCompliances,'wwpLeosFilterMIBGroups':wwpLeosFilterMIBGroups})