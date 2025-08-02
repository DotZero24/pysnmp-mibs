_P='llfCircuitIndex'
_O='llfCircuitPolIndex'
_N='llfCircuitLinkIndex'
_M='llfMapCircuitIndex'
_L='llfMapPolIndex'
_K='llfMapLinkIndex'
_J='DisplayString'
_I='AlarmSeverityCode'
_H='llfIndex'
_G='enable'
_F='disable'
_E='Integer32'
_D='read-create'
_C='SIAE-LLF-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
AlarmSeverityCode,AlarmStatus=mibBuilder.importSymbols('SIAE-ALARM-MIB',_I,'AlarmStatus')
siaeMib,=mibBuilder.importSymbols('SIAE-TREE-MIB','siaeMib')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_J,'PhysAddress','RowStatus','TextualConvention','TruthValue')
llf=ModuleIdentity((1,3,6,1,4,1,3373,1103,85))
class _LlfMibVersion_Type(Integer32):defaultValue=1
_LlfMibVersion_Type.__name__=_E
_LlfMibVersion_Object=MibScalar
llfMibVersion=_LlfMibVersion_Object((1,3,6,1,4,1,3373,1103,85,1),_LlfMibVersion_Type())
llfMibVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:llfMibVersion.setStatus(_A)
_LlfTable_Object=MibTable
llfTable=_LlfTable_Object((1,3,6,1,4,1,3373,1103,85,2))
if mibBuilder.loadTexts:llfTable.setStatus(_A)
_LlfEntry_Object=MibTableRow
llfEntry=_LlfEntry_Object((1,3,6,1,4,1,3373,1103,85,2,1))
llfEntry.setIndexNames((0,_C,_H))
if mibBuilder.loadTexts:llfEntry.setStatus(_A)
_LlfIndex_Type=InterfaceIndex
_LlfIndex_Object=MibTableColumn
llfIndex=_LlfIndex_Object((1,3,6,1,4,1,3373,1103,85,2,1,1),_LlfIndex_Type())
llfIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:llfIndex.setStatus(_A)
class _LlfEnable_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_LlfEnable_Type.__name__=_E
_LlfEnable_Object=MibTableColumn
llfEnable=_LlfEnable_Object((1,3,6,1,4,1,3373,1103,85,2,1,2),_LlfEnable_Type())
llfEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:llfEnable.setStatus(_A)
class _LlfUnidirectionalFault_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_LlfUnidirectionalFault_Type.__name__=_E
_LlfUnidirectionalFault_Object=MibTableColumn
llfUnidirectionalFault=_LlfUnidirectionalFault_Object((1,3,6,1,4,1,3373,1103,85,2,1,3),_LlfUnidirectionalFault_Type())
llfUnidirectionalFault.setMaxAccess(_D)
if mibBuilder.loadTexts:llfUnidirectionalFault.setStatus(_A)
class _LlfDelayTime_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10))
_LlfDelayTime_Type.__name__=_E
_LlfDelayTime_Object=MibTableColumn
llfDelayTime=_LlfDelayTime_Object((1,3,6,1,4,1,3373,1103,85,2,1,4),_LlfDelayTime_Type())
llfDelayTime.setMaxAccess(_D)
if mibBuilder.loadTexts:llfDelayTime.setStatus(_A)
class _LlfProtectionMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_LlfProtectionMode_Type.__name__=_E
_LlfProtectionMode_Object=MibTableColumn
llfProtectionMode=_LlfProtectionMode_Object((1,3,6,1,4,1,3373,1103,85,2,1,5),_LlfProtectionMode_Type())
llfProtectionMode.setMaxAccess(_D)
if mibBuilder.loadTexts:llfProtectionMode.setStatus(_A)
_LlfAlarm_Type=AlarmStatus
_LlfAlarm_Object=MibTableColumn
llfAlarm=_LlfAlarm_Object((1,3,6,1,4,1,3373,1103,85,2,1,6),_LlfAlarm_Type())
llfAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:llfAlarm.setStatus(_A)
_LlfRowStatus_Type=RowStatus
_LlfRowStatus_Object=MibTableColumn
llfRowStatus=_LlfRowStatus_Object((1,3,6,1,4,1,3373,1103,85,2,1,7),_LlfRowStatus_Type())
llfRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:llfRowStatus.setStatus(_A)
_LlfMapTable_Object=MibTable
llfMapTable=_LlfMapTable_Object((1,3,6,1,4,1,3373,1103,85,3))
if mibBuilder.loadTexts:llfMapTable.setStatus(_A)
_LlfMapEntry_Object=MibTableRow
llfMapEntry=_LlfMapEntry_Object((1,3,6,1,4,1,3373,1103,85,3,1))
llfMapEntry.setIndexNames((0,_C,_H),(0,_C,_K),(0,_C,_L),(0,_C,_M))
if mibBuilder.loadTexts:llfMapEntry.setStatus(_A)
_LlfMapLinkIndex_Type=Integer32
_LlfMapLinkIndex_Object=MibTableColumn
llfMapLinkIndex=_LlfMapLinkIndex_Object((1,3,6,1,4,1,3373,1103,85,3,1,1),_LlfMapLinkIndex_Type())
llfMapLinkIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:llfMapLinkIndex.setStatus(_A)
_LlfMapPolIndex_Type=Integer32
_LlfMapPolIndex_Object=MibTableColumn
llfMapPolIndex=_LlfMapPolIndex_Object((1,3,6,1,4,1,3373,1103,85,3,1,2),_LlfMapPolIndex_Type())
llfMapPolIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:llfMapPolIndex.setStatus(_A)
_LlfMapCircuitIndex_Type=Integer32
_LlfMapCircuitIndex_Object=MibTableColumn
llfMapCircuitIndex=_LlfMapCircuitIndex_Object((1,3,6,1,4,1,3373,1103,85,3,1,3),_LlfMapCircuitIndex_Type())
llfMapCircuitIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:llfMapCircuitIndex.setStatus(_A)
class _LlfMapLosInsertion_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_LlfMapLosInsertion_Type.__name__=_E
_LlfMapLosInsertion_Object=MibTableColumn
llfMapLosInsertion=_LlfMapLosInsertion_Object((1,3,6,1,4,1,3373,1103,85,3,1,4),_LlfMapLosInsertion_Type())
llfMapLosInsertion.setMaxAccess(_D)
if mibBuilder.loadTexts:llfMapLosInsertion.setStatus(_A)
class _LlfMapInsertionMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('single',1),('group',2)))
_LlfMapInsertionMode_Type.__name__=_E
_LlfMapInsertionMode_Object=MibTableColumn
llfMapInsertionMode=_LlfMapInsertionMode_Object((1,3,6,1,4,1,3373,1103,85,3,1,5),_LlfMapInsertionMode_Type())
llfMapInsertionMode.setMaxAccess(_D)
if mibBuilder.loadTexts:llfMapInsertionMode.setStatus(_A)
_LlfMapSignalFail_Type=TruthValue
_LlfMapSignalFail_Object=MibTableColumn
llfMapSignalFail=_LlfMapSignalFail_Object((1,3,6,1,4,1,3373,1103,85,3,1,6),_LlfMapSignalFail_Type())
llfMapSignalFail.setMaxAccess(_B)
if mibBuilder.loadTexts:llfMapSignalFail.setStatus(_A)
_LlfMapRowStatus_Type=RowStatus
_LlfMapRowStatus_Object=MibTableColumn
llfMapRowStatus=_LlfMapRowStatus_Object((1,3,6,1,4,1,3373,1103,85,3,1,7),_LlfMapRowStatus_Type())
llfMapRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:llfMapRowStatus.setStatus(_A)
_LlfCircuitTable_Object=MibTable
llfCircuitTable=_LlfCircuitTable_Object((1,3,6,1,4,1,3373,1103,85,4))
if mibBuilder.loadTexts:llfCircuitTable.setStatus(_A)
_LlfCircuitEntry_Object=MibTableRow
llfCircuitEntry=_LlfCircuitEntry_Object((1,3,6,1,4,1,3373,1103,85,4,1))
llfCircuitEntry.setIndexNames((0,_C,_N),(0,_C,_O),(0,_C,_P))
if mibBuilder.loadTexts:llfCircuitEntry.setStatus(_A)
_LlfCircuitLinkIndex_Type=Integer32
_LlfCircuitLinkIndex_Object=MibTableColumn
llfCircuitLinkIndex=_LlfCircuitLinkIndex_Object((1,3,6,1,4,1,3373,1103,85,4,1,1),_LlfCircuitLinkIndex_Type())
llfCircuitLinkIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:llfCircuitLinkIndex.setStatus(_A)
_LlfCircuitPolIndex_Type=Integer32
_LlfCircuitPolIndex_Object=MibTableColumn
llfCircuitPolIndex=_LlfCircuitPolIndex_Object((1,3,6,1,4,1,3373,1103,85,4,1,2),_LlfCircuitPolIndex_Type())
llfCircuitPolIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:llfCircuitPolIndex.setStatus(_A)
_LlfCircuitIndex_Type=Integer32
_LlfCircuitIndex_Object=MibTableColumn
llfCircuitIndex=_LlfCircuitIndex_Object((1,3,6,1,4,1,3373,1103,85,4,1,3),_LlfCircuitIndex_Type())
llfCircuitIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:llfCircuitIndex.setStatus(_A)
class _LlfCircuitLinkLabel_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_LlfCircuitLinkLabel_Type.__name__=_J
_LlfCircuitLinkLabel_Object=MibTableColumn
llfCircuitLinkLabel=_LlfCircuitLinkLabel_Object((1,3,6,1,4,1,3373,1103,85,4,1,4),_LlfCircuitLinkLabel_Type())
llfCircuitLinkLabel.setMaxAccess(_B)
if mibBuilder.loadTexts:llfCircuitLinkLabel.setStatus(_A)
_LlfCircuitRowStatus_Type=RowStatus
_LlfCircuitRowStatus_Object=MibTableColumn
llfCircuitRowStatus=_LlfCircuitRowStatus_Object((1,3,6,1,4,1,3373,1103,85,4,1,5),_LlfCircuitRowStatus_Type())
llfCircuitRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:llfCircuitRowStatus.setStatus(_A)
class _LlfAlarmSeverityCode_Type(AlarmSeverityCode):defaultValue=5
_LlfAlarmSeverityCode_Type.__name__=_I
_LlfAlarmSeverityCode_Object=MibScalar
llfAlarmSeverityCode=_LlfAlarmSeverityCode_Object((1,3,6,1,4,1,3373,1103,85,5),_LlfAlarmSeverityCode_Type())
llfAlarmSeverityCode.setMaxAccess('read-write')
if mibBuilder.loadTexts:llfAlarmSeverityCode.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'llf':llf,'llfMibVersion':llfMibVersion,'llfTable':llfTable,'llfEntry':llfEntry,_H:llfIndex,'llfEnable':llfEnable,'llfUnidirectionalFault':llfUnidirectionalFault,'llfDelayTime':llfDelayTime,'llfProtectionMode':llfProtectionMode,'llfAlarm':llfAlarm,'llfRowStatus':llfRowStatus,'llfMapTable':llfMapTable,'llfMapEntry':llfMapEntry,_K:llfMapLinkIndex,_L:llfMapPolIndex,_M:llfMapCircuitIndex,'llfMapLosInsertion':llfMapLosInsertion,'llfMapInsertionMode':llfMapInsertionMode,'llfMapSignalFail':llfMapSignalFail,'llfMapRowStatus':llfMapRowStatus,'llfCircuitTable':llfCircuitTable,'llfCircuitEntry':llfCircuitEntry,_N:llfCircuitLinkIndex,_O:llfCircuitPolIndex,_P:llfCircuitIndex,'llfCircuitLinkLabel':llfCircuitLinkLabel,'llfCircuitRowStatus':llfCircuitRowStatus,'llfAlarmSeverityCode':llfAlarmSeverityCode})