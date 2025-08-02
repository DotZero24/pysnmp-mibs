_e='me1200HqosConfigInterfaceHqosQueueTableInfoGroup'
_d='me1200HqosConfigInterfaceHqosTableRowEditorInfoGroup'
_c='me1200HqosConfigInterfaceHqosTableInfoGroup'
_b='me1200HqosConfigInterfaceTableInfoGroup'
_a='me1200HqosConfigInterfaceHqosQueueSchedulerWeight'
_Z='me1200HqosConfigInterfaceHqosQueueShaperRate'
_Y='me1200HqosConfigInterfaceHqosQueueShaperEnable'
_X='me1200HqosConfigInterfaceHqosTableRowEditorAction'
_W='me1200HqosConfigInterfaceHqosTableRowEditorMinRate'
_V='me1200HqosConfigInterfaceHqosTableRowEditorShaperRate'
_U='me1200HqosConfigInterfaceHqosTableRowEditorShaperEnable'
_T='me1200HqosConfigInterfaceHqosTableRowEditorDwrrCount'
_S='me1200HqosConfigInterfaceHqosTableRowEditorHqosId'
_R='me1200HqosConfigInterfaceHqosTableRowEditorIfIndex'
_Q='me1200HqosConfigInterfaceHqosAction'
_P='me1200HqosConfigInterfaceHqosMinRate'
_O='me1200HqosConfigInterfaceHqosShaperRate'
_N='me1200HqosConfigInterfaceHqosShaperEnable'
_M='me1200HqosConfigInterfaceHqosDwrrCount'
_L='me1200HqosConfigInterfaceSchMode'
_K='me1200HqosConfigInterfaceHqosQueueQueue'
_J='me1200HqosConfigInterfaceHqosQueueHqosId'
_I='me1200HqosConfigInterfaceHqosQueueIfIndex'
_H='me1200HqosConfigInterfaceHqosHqosId'
_G='me1200HqosConfigInterfaceHqosIfIndex'
_F='me1200HqosConfigInterfaceIfIndex'
_E='Integer32'
_D='not-accessible'
_C='read-write'
_B='ME1200-HQOS-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
me1200SwitchMgmt,=mibBuilder.importSymbols('CISCOME1200-MIB','me1200SwitchMgmt')
ME1200InterfaceIndex,ME1200RowEditorState,ME1200Unsigned8=mibBuilder.importSymbols('ME1200-TC','ME1200InterfaceIndex','ME1200RowEditorState','ME1200Unsigned8')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
me1200HqosMib=ModuleIdentity((1,3,6,1,4,1,9,9,815,1,125))
if mibBuilder.loadTexts:me1200HqosMib.setRevisions(('2015-01-09 00:00','2014-04-10 00:00'))
class ME1200hqosSchMode(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('normal',0),('basic',1),('hierarchical',2)))
_Me1200HqosMibObjects_ObjectIdentity=ObjectIdentity
me1200HqosMibObjects=_Me1200HqosMibObjects_ObjectIdentity((1,3,6,1,4,1,9,9,815,1,125,1))
_Me1200HqosConfig_ObjectIdentity=ObjectIdentity
me1200HqosConfig=_Me1200HqosConfig_ObjectIdentity((1,3,6,1,4,1,9,9,815,1,125,1,2))
_Me1200HqosConfigInterface_ObjectIdentity=ObjectIdentity
me1200HqosConfigInterface=_Me1200HqosConfigInterface_ObjectIdentity((1,3,6,1,4,1,9,9,815,1,125,1,2,2))
_Me1200HqosConfigInterfaceTable_Object=MibTable
me1200HqosConfigInterfaceTable=_Me1200HqosConfigInterfaceTable_Object((1,3,6,1,4,1,9,9,815,1,125,1,2,2,1))
if mibBuilder.loadTexts:me1200HqosConfigInterfaceTable.setStatus(_A)
_Me1200HqosConfigInterfaceEntry_Object=MibTableRow
me1200HqosConfigInterfaceEntry=_Me1200HqosConfigInterfaceEntry_Object((1,3,6,1,4,1,9,9,815,1,125,1,2,2,1,1))
me1200HqosConfigInterfaceEntry.setIndexNames((0,_B,_F))
if mibBuilder.loadTexts:me1200HqosConfigInterfaceEntry.setStatus(_A)
_Me1200HqosConfigInterfaceIfIndex_Type=ME1200InterfaceIndex
_Me1200HqosConfigInterfaceIfIndex_Object=MibTableColumn
me1200HqosConfigInterfaceIfIndex=_Me1200HqosConfigInterfaceIfIndex_Object((1,3,6,1,4,1,9,9,815,1,125,1,2,2,1,1,1),_Me1200HqosConfigInterfaceIfIndex_Type())
me1200HqosConfigInterfaceIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:me1200HqosConfigInterfaceIfIndex.setStatus(_A)
_Me1200HqosConfigInterfaceSchMode_Type=ME1200hqosSchMode
_Me1200HqosConfigInterfaceSchMode_Object=MibTableColumn
me1200HqosConfigInterfaceSchMode=_Me1200HqosConfigInterfaceSchMode_Object((1,3,6,1,4,1,9,9,815,1,125,1,2,2,1,1,2),_Me1200HqosConfigInterfaceSchMode_Type())
me1200HqosConfigInterfaceSchMode.setMaxAccess(_C)
if mibBuilder.loadTexts:me1200HqosConfigInterfaceSchMode.setStatus(_A)
_Me1200HqosConfigInterfaceHqosTable_Object=MibTable
me1200HqosConfigInterfaceHqosTable=_Me1200HqosConfigInterfaceHqosTable_Object((1,3,6,1,4,1,9,9,815,1,125,1,2,2,2))
if mibBuilder.loadTexts:me1200HqosConfigInterfaceHqosTable.setStatus(_A)
_Me1200HqosConfigInterfaceHqosEntry_Object=MibTableRow
me1200HqosConfigInterfaceHqosEntry=_Me1200HqosConfigInterfaceHqosEntry_Object((1,3,6,1,4,1,9,9,815,1,125,1,2,2,2,1))
me1200HqosConfigInterfaceHqosEntry.setIndexNames((0,_B,_G),(0,_B,_H))
if mibBuilder.loadTexts:me1200HqosConfigInterfaceHqosEntry.setStatus(_A)
_Me1200HqosConfigInterfaceHqosIfIndex_Type=ME1200InterfaceIndex
_Me1200HqosConfigInterfaceHqosIfIndex_Object=MibTableColumn
me1200HqosConfigInterfaceHqosIfIndex=_Me1200HqosConfigInterfaceHqosIfIndex_Object((1,3,6,1,4,1,9,9,815,1,125,1,2,2,2,1,1),_Me1200HqosConfigInterfaceHqosIfIndex_Type())
me1200HqosConfigInterfaceHqosIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:me1200HqosConfigInterfaceHqosIfIndex.setStatus(_A)
class _Me1200HqosConfigInterfaceHqosHqosId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_Me1200HqosConfigInterfaceHqosHqosId_Type.__name__=_E
_Me1200HqosConfigInterfaceHqosHqosId_Object=MibTableColumn
me1200HqosConfigInterfaceHqosHqosId=_Me1200HqosConfigInterfaceHqosHqosId_Object((1,3,6,1,4,1,9,9,815,1,125,1,2,2,2,1,2),_Me1200HqosConfigInterfaceHqosHqosId_Type())
me1200HqosConfigInterfaceHqosHqosId.setMaxAccess(_D)
if mibBuilder.loadTexts:me1200HqosConfigInterfaceHqosHqosId.setStatus(_A)
_Me1200HqosConfigInterfaceHqosDwrrCount_Type=ME1200Unsigned8
_Me1200HqosConfigInterfaceHqosDwrrCount_Object=MibTableColumn
me1200HqosConfigInterfaceHqosDwrrCount=_Me1200HqosConfigInterfaceHqosDwrrCount_Object((1,3,6,1,4,1,9,9,815,1,125,1,2,2,2,1,3),_Me1200HqosConfigInterfaceHqosDwrrCount_Type())
me1200HqosConfigInterfaceHqosDwrrCount.setMaxAccess(_C)
if mibBuilder.loadTexts:me1200HqosConfigInterfaceHqosDwrrCount.setStatus(_A)
_Me1200HqosConfigInterfaceHqosShaperEnable_Type=TruthValue
_Me1200HqosConfigInterfaceHqosShaperEnable_Object=MibTableColumn
me1200HqosConfigInterfaceHqosShaperEnable=_Me1200HqosConfigInterfaceHqosShaperEnable_Object((1,3,6,1,4,1,9,9,815,1,125,1,2,2,2,1,4),_Me1200HqosConfigInterfaceHqosShaperEnable_Type())
me1200HqosConfigInterfaceHqosShaperEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:me1200HqosConfigInterfaceHqosShaperEnable.setStatus(_A)
_Me1200HqosConfigInterfaceHqosShaperRate_Type=Unsigned32
_Me1200HqosConfigInterfaceHqosShaperRate_Object=MibTableColumn
me1200HqosConfigInterfaceHqosShaperRate=_Me1200HqosConfigInterfaceHqosShaperRate_Object((1,3,6,1,4,1,9,9,815,1,125,1,2,2,2,1,5),_Me1200HqosConfigInterfaceHqosShaperRate_Type())
me1200HqosConfigInterfaceHqosShaperRate.setMaxAccess(_C)
if mibBuilder.loadTexts:me1200HqosConfigInterfaceHqosShaperRate.setStatus(_A)
_Me1200HqosConfigInterfaceHqosMinRate_Type=Unsigned32
_Me1200HqosConfigInterfaceHqosMinRate_Object=MibTableColumn
me1200HqosConfigInterfaceHqosMinRate=_Me1200HqosConfigInterfaceHqosMinRate_Object((1,3,6,1,4,1,9,9,815,1,125,1,2,2,2,1,6),_Me1200HqosConfigInterfaceHqosMinRate_Type())
me1200HqosConfigInterfaceHqosMinRate.setMaxAccess(_C)
if mibBuilder.loadTexts:me1200HqosConfigInterfaceHqosMinRate.setStatus(_A)
_Me1200HqosConfigInterfaceHqosAction_Type=ME1200RowEditorState
_Me1200HqosConfigInterfaceHqosAction_Object=MibTableColumn
me1200HqosConfigInterfaceHqosAction=_Me1200HqosConfigInterfaceHqosAction_Object((1,3,6,1,4,1,9,9,815,1,125,1,2,2,2,1,10000),_Me1200HqosConfigInterfaceHqosAction_Type())
me1200HqosConfigInterfaceHqosAction.setMaxAccess(_C)
if mibBuilder.loadTexts:me1200HqosConfigInterfaceHqosAction.setStatus(_A)
_Me1200HqosConfigInterfaceHqosTableRowEditor_ObjectIdentity=ObjectIdentity
me1200HqosConfigInterfaceHqosTableRowEditor=_Me1200HqosConfigInterfaceHqosTableRowEditor_ObjectIdentity((1,3,6,1,4,1,9,9,815,1,125,1,2,2,3))
_Me1200HqosConfigInterfaceHqosTableRowEditorIfIndex_Type=ME1200InterfaceIndex
_Me1200HqosConfigInterfaceHqosTableRowEditorIfIndex_Object=MibScalar
me1200HqosConfigInterfaceHqosTableRowEditorIfIndex=_Me1200HqosConfigInterfaceHqosTableRowEditorIfIndex_Object((1,3,6,1,4,1,9,9,815,1,125,1,2,2,3,1),_Me1200HqosConfigInterfaceHqosTableRowEditorIfIndex_Type())
me1200HqosConfigInterfaceHqosTableRowEditorIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:me1200HqosConfigInterfaceHqosTableRowEditorIfIndex.setStatus(_A)
class _Me1200HqosConfigInterfaceHqosTableRowEditorHqosId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_Me1200HqosConfigInterfaceHqosTableRowEditorHqosId_Type.__name__=_E
_Me1200HqosConfigInterfaceHqosTableRowEditorHqosId_Object=MibScalar
me1200HqosConfigInterfaceHqosTableRowEditorHqosId=_Me1200HqosConfigInterfaceHqosTableRowEditorHqosId_Object((1,3,6,1,4,1,9,9,815,1,125,1,2,2,3,2),_Me1200HqosConfigInterfaceHqosTableRowEditorHqosId_Type())
me1200HqosConfigInterfaceHqosTableRowEditorHqosId.setMaxAccess(_C)
if mibBuilder.loadTexts:me1200HqosConfigInterfaceHqosTableRowEditorHqosId.setStatus(_A)
_Me1200HqosConfigInterfaceHqosTableRowEditorDwrrCount_Type=ME1200Unsigned8
_Me1200HqosConfigInterfaceHqosTableRowEditorDwrrCount_Object=MibScalar
me1200HqosConfigInterfaceHqosTableRowEditorDwrrCount=_Me1200HqosConfigInterfaceHqosTableRowEditorDwrrCount_Object((1,3,6,1,4,1,9,9,815,1,125,1,2,2,3,3),_Me1200HqosConfigInterfaceHqosTableRowEditorDwrrCount_Type())
me1200HqosConfigInterfaceHqosTableRowEditorDwrrCount.setMaxAccess(_C)
if mibBuilder.loadTexts:me1200HqosConfigInterfaceHqosTableRowEditorDwrrCount.setStatus(_A)
_Me1200HqosConfigInterfaceHqosTableRowEditorShaperEnable_Type=TruthValue
_Me1200HqosConfigInterfaceHqosTableRowEditorShaperEnable_Object=MibScalar
me1200HqosConfigInterfaceHqosTableRowEditorShaperEnable=_Me1200HqosConfigInterfaceHqosTableRowEditorShaperEnable_Object((1,3,6,1,4,1,9,9,815,1,125,1,2,2,3,4),_Me1200HqosConfigInterfaceHqosTableRowEditorShaperEnable_Type())
me1200HqosConfigInterfaceHqosTableRowEditorShaperEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:me1200HqosConfigInterfaceHqosTableRowEditorShaperEnable.setStatus(_A)
_Me1200HqosConfigInterfaceHqosTableRowEditorShaperRate_Type=Unsigned32
_Me1200HqosConfigInterfaceHqosTableRowEditorShaperRate_Object=MibScalar
me1200HqosConfigInterfaceHqosTableRowEditorShaperRate=_Me1200HqosConfigInterfaceHqosTableRowEditorShaperRate_Object((1,3,6,1,4,1,9,9,815,1,125,1,2,2,3,5),_Me1200HqosConfigInterfaceHqosTableRowEditorShaperRate_Type())
me1200HqosConfigInterfaceHqosTableRowEditorShaperRate.setMaxAccess(_C)
if mibBuilder.loadTexts:me1200HqosConfigInterfaceHqosTableRowEditorShaperRate.setStatus(_A)
_Me1200HqosConfigInterfaceHqosTableRowEditorMinRate_Type=Unsigned32
_Me1200HqosConfigInterfaceHqosTableRowEditorMinRate_Object=MibScalar
me1200HqosConfigInterfaceHqosTableRowEditorMinRate=_Me1200HqosConfigInterfaceHqosTableRowEditorMinRate_Object((1,3,6,1,4,1,9,9,815,1,125,1,2,2,3,6),_Me1200HqosConfigInterfaceHqosTableRowEditorMinRate_Type())
me1200HqosConfigInterfaceHqosTableRowEditorMinRate.setMaxAccess(_C)
if mibBuilder.loadTexts:me1200HqosConfigInterfaceHqosTableRowEditorMinRate.setStatus(_A)
_Me1200HqosConfigInterfaceHqosTableRowEditorAction_Type=ME1200RowEditorState
_Me1200HqosConfigInterfaceHqosTableRowEditorAction_Object=MibScalar
me1200HqosConfigInterfaceHqosTableRowEditorAction=_Me1200HqosConfigInterfaceHqosTableRowEditorAction_Object((1,3,6,1,4,1,9,9,815,1,125,1,2,2,3,10000),_Me1200HqosConfigInterfaceHqosTableRowEditorAction_Type())
me1200HqosConfigInterfaceHqosTableRowEditorAction.setMaxAccess(_C)
if mibBuilder.loadTexts:me1200HqosConfigInterfaceHqosTableRowEditorAction.setStatus(_A)
_Me1200HqosConfigInterfaceHqosQueueTable_Object=MibTable
me1200HqosConfigInterfaceHqosQueueTable=_Me1200HqosConfigInterfaceHqosQueueTable_Object((1,3,6,1,4,1,9,9,815,1,125,1,2,2,4))
if mibBuilder.loadTexts:me1200HqosConfigInterfaceHqosQueueTable.setStatus(_A)
_Me1200HqosConfigInterfaceHqosQueueEntry_Object=MibTableRow
me1200HqosConfigInterfaceHqosQueueEntry=_Me1200HqosConfigInterfaceHqosQueueEntry_Object((1,3,6,1,4,1,9,9,815,1,125,1,2,2,4,1))
me1200HqosConfigInterfaceHqosQueueEntry.setIndexNames((0,_B,_I),(0,_B,_J),(0,_B,_K))
if mibBuilder.loadTexts:me1200HqosConfigInterfaceHqosQueueEntry.setStatus(_A)
_Me1200HqosConfigInterfaceHqosQueueIfIndex_Type=ME1200InterfaceIndex
_Me1200HqosConfigInterfaceHqosQueueIfIndex_Object=MibTableColumn
me1200HqosConfigInterfaceHqosQueueIfIndex=_Me1200HqosConfigInterfaceHqosQueueIfIndex_Object((1,3,6,1,4,1,9,9,815,1,125,1,2,2,4,1,1),_Me1200HqosConfigInterfaceHqosQueueIfIndex_Type())
me1200HqosConfigInterfaceHqosQueueIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:me1200HqosConfigInterfaceHqosQueueIfIndex.setStatus(_A)
class _Me1200HqosConfigInterfaceHqosQueueHqosId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_Me1200HqosConfigInterfaceHqosQueueHqosId_Type.__name__=_E
_Me1200HqosConfigInterfaceHqosQueueHqosId_Object=MibTableColumn
me1200HqosConfigInterfaceHqosQueueHqosId=_Me1200HqosConfigInterfaceHqosQueueHqosId_Object((1,3,6,1,4,1,9,9,815,1,125,1,2,2,4,1,2),_Me1200HqosConfigInterfaceHqosQueueHqosId_Type())
me1200HqosConfigInterfaceHqosQueueHqosId.setMaxAccess(_D)
if mibBuilder.loadTexts:me1200HqosConfigInterfaceHqosQueueHqosId.setStatus(_A)
class _Me1200HqosConfigInterfaceHqosQueueQueue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_Me1200HqosConfigInterfaceHqosQueueQueue_Type.__name__=_E
_Me1200HqosConfigInterfaceHqosQueueQueue_Object=MibTableColumn
me1200HqosConfigInterfaceHqosQueueQueue=_Me1200HqosConfigInterfaceHqosQueueQueue_Object((1,3,6,1,4,1,9,9,815,1,125,1,2,2,4,1,3),_Me1200HqosConfigInterfaceHqosQueueQueue_Type())
me1200HqosConfigInterfaceHqosQueueQueue.setMaxAccess(_D)
if mibBuilder.loadTexts:me1200HqosConfigInterfaceHqosQueueQueue.setStatus(_A)
_Me1200HqosConfigInterfaceHqosQueueShaperEnable_Type=TruthValue
_Me1200HqosConfigInterfaceHqosQueueShaperEnable_Object=MibTableColumn
me1200HqosConfigInterfaceHqosQueueShaperEnable=_Me1200HqosConfigInterfaceHqosQueueShaperEnable_Object((1,3,6,1,4,1,9,9,815,1,125,1,2,2,4,1,4),_Me1200HqosConfigInterfaceHqosQueueShaperEnable_Type())
me1200HqosConfigInterfaceHqosQueueShaperEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:me1200HqosConfigInterfaceHqosQueueShaperEnable.setStatus(_A)
_Me1200HqosConfigInterfaceHqosQueueShaperRate_Type=Unsigned32
_Me1200HqosConfigInterfaceHqosQueueShaperRate_Object=MibTableColumn
me1200HqosConfigInterfaceHqosQueueShaperRate=_Me1200HqosConfigInterfaceHqosQueueShaperRate_Object((1,3,6,1,4,1,9,9,815,1,125,1,2,2,4,1,5),_Me1200HqosConfigInterfaceHqosQueueShaperRate_Type())
me1200HqosConfigInterfaceHqosQueueShaperRate.setMaxAccess(_C)
if mibBuilder.loadTexts:me1200HqosConfigInterfaceHqosQueueShaperRate.setStatus(_A)
_Me1200HqosConfigInterfaceHqosQueueSchedulerWeight_Type=ME1200Unsigned8
_Me1200HqosConfigInterfaceHqosQueueSchedulerWeight_Object=MibTableColumn
me1200HqosConfigInterfaceHqosQueueSchedulerWeight=_Me1200HqosConfigInterfaceHqosQueueSchedulerWeight_Object((1,3,6,1,4,1,9,9,815,1,125,1,2,2,4,1,6),_Me1200HqosConfigInterfaceHqosQueueSchedulerWeight_Type())
me1200HqosConfigInterfaceHqosQueueSchedulerWeight.setMaxAccess(_C)
if mibBuilder.loadTexts:me1200HqosConfigInterfaceHqosQueueSchedulerWeight.setStatus(_A)
_Me1200HqosConfigHqos_ObjectIdentity=ObjectIdentity
me1200HqosConfigHqos=_Me1200HqosConfigHqos_ObjectIdentity((1,3,6,1,4,1,9,9,815,1,125,1,2,4))
_Me1200HqosMibConformance_ObjectIdentity=ObjectIdentity
me1200HqosMibConformance=_Me1200HqosMibConformance_ObjectIdentity((1,3,6,1,4,1,9,9,815,1,125,2))
_Me1200HqosMibCompliances_ObjectIdentity=ObjectIdentity
me1200HqosMibCompliances=_Me1200HqosMibCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,815,1,125,2,1))
_Me1200HqosMibGroups_ObjectIdentity=ObjectIdentity
me1200HqosMibGroups=_Me1200HqosMibGroups_ObjectIdentity((1,3,6,1,4,1,9,9,815,1,125,2,2))
me1200HqosConfigInterfaceTableInfoGroup=ObjectGroup((1,3,6,1,4,1,9,9,815,1,125,2,2,1))
me1200HqosConfigInterfaceTableInfoGroup.setObjects((_B,_L))
if mibBuilder.loadTexts:me1200HqosConfigInterfaceTableInfoGroup.setStatus(_A)
me1200HqosConfigInterfaceHqosTableInfoGroup=ObjectGroup((1,3,6,1,4,1,9,9,815,1,125,2,2,2))
me1200HqosConfigInterfaceHqosTableInfoGroup.setObjects(*((_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q)))
if mibBuilder.loadTexts:me1200HqosConfigInterfaceHqosTableInfoGroup.setStatus(_A)
me1200HqosConfigInterfaceHqosTableRowEditorInfoGroup=ObjectGroup((1,3,6,1,4,1,9,9,815,1,125,2,2,3))
me1200HqosConfigInterfaceHqosTableRowEditorInfoGroup.setObjects(*((_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X)))
if mibBuilder.loadTexts:me1200HqosConfigInterfaceHqosTableRowEditorInfoGroup.setStatus(_A)
me1200HqosConfigInterfaceHqosQueueTableInfoGroup=ObjectGroup((1,3,6,1,4,1,9,9,815,1,125,2,2,4))
me1200HqosConfigInterfaceHqosQueueTableInfoGroup.setObjects(*((_B,_Y),(_B,_Z),(_B,_a)))
if mibBuilder.loadTexts:me1200HqosConfigInterfaceHqosQueueTableInfoGroup.setStatus(_A)
me1200HqosMibCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,815,1,125,2,1,1))
me1200HqosMibCompliance.setObjects(*((_B,_b),(_B,_c),(_B,_d),(_B,_e)))
if mibBuilder.loadTexts:me1200HqosMibCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ME1200hqosSchMode':ME1200hqosSchMode,'me1200HqosMib':me1200HqosMib,'me1200HqosMibObjects':me1200HqosMibObjects,'me1200HqosConfig':me1200HqosConfig,'me1200HqosConfigInterface':me1200HqosConfigInterface,'me1200HqosConfigInterfaceTable':me1200HqosConfigInterfaceTable,'me1200HqosConfigInterfaceEntry':me1200HqosConfigInterfaceEntry,_F:me1200HqosConfigInterfaceIfIndex,_L:me1200HqosConfigInterfaceSchMode,'me1200HqosConfigInterfaceHqosTable':me1200HqosConfigInterfaceHqosTable,'me1200HqosConfigInterfaceHqosEntry':me1200HqosConfigInterfaceHqosEntry,_G:me1200HqosConfigInterfaceHqosIfIndex,_H:me1200HqosConfigInterfaceHqosHqosId,_M:me1200HqosConfigInterfaceHqosDwrrCount,_N:me1200HqosConfigInterfaceHqosShaperEnable,_O:me1200HqosConfigInterfaceHqosShaperRate,_P:me1200HqosConfigInterfaceHqosMinRate,_Q:me1200HqosConfigInterfaceHqosAction,'me1200HqosConfigInterfaceHqosTableRowEditor':me1200HqosConfigInterfaceHqosTableRowEditor,_R:me1200HqosConfigInterfaceHqosTableRowEditorIfIndex,_S:me1200HqosConfigInterfaceHqosTableRowEditorHqosId,_T:me1200HqosConfigInterfaceHqosTableRowEditorDwrrCount,_U:me1200HqosConfigInterfaceHqosTableRowEditorShaperEnable,_V:me1200HqosConfigInterfaceHqosTableRowEditorShaperRate,_W:me1200HqosConfigInterfaceHqosTableRowEditorMinRate,_X:me1200HqosConfigInterfaceHqosTableRowEditorAction,'me1200HqosConfigInterfaceHqosQueueTable':me1200HqosConfigInterfaceHqosQueueTable,'me1200HqosConfigInterfaceHqosQueueEntry':me1200HqosConfigInterfaceHqosQueueEntry,_I:me1200HqosConfigInterfaceHqosQueueIfIndex,_J:me1200HqosConfigInterfaceHqosQueueHqosId,_K:me1200HqosConfigInterfaceHqosQueueQueue,_Y:me1200HqosConfigInterfaceHqosQueueShaperEnable,_Z:me1200HqosConfigInterfaceHqosQueueShaperRate,_a:me1200HqosConfigInterfaceHqosQueueSchedulerWeight,'me1200HqosConfigHqos':me1200HqosConfigHqos,'me1200HqosMibConformance':me1200HqosMibConformance,'me1200HqosMibCompliances':me1200HqosMibCompliances,'me1200HqosMibCompliance':me1200HqosMibCompliance,'me1200HqosMibGroups':me1200HqosMibGroups,_b:me1200HqosConfigInterfaceTableInfoGroup,_c:me1200HqosConfigInterfaceHqosTableInfoGroup,_d:me1200HqosConfigInterfaceHqosTableRowEditorInfoGroup,_e:me1200HqosConfigInterfaceHqosQueueTableInfoGroup})