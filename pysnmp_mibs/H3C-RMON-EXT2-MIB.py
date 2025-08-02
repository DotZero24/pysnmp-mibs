_K='h3cRmonExtAlarmFallingThreshold'
_J='h3cRmonExtAlarmRisingThreshold'
_I='read-only'
_H='h3cRmonExtAlarmValue'
_G='h3cRmonExtAlarmSampleType'
_F='h3cRmonExtAlarmSympol'
_E='h3cRmonExtAlarmIndex'
_D='Integer32'
_C='H3C-RMON-EXT2-MIB'
_B='read-create'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
h3cCommon,=mibBuilder.importSymbols('HUAWEI-3COM-OID-MIB','h3cCommon')
EntryStatus,OwnerString=mibBuilder.importSymbols('RMON-MIB','EntryStatus','OwnerString')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
h3cRmonExt=ModuleIdentity((1,3,6,1,4,1,2011,10,2,125))
if mibBuilder.loadTexts:h3cRmonExt.setRevisions(('2012-06-19 00:00',))
_H3cRmonExtEvent_ObjectIdentity=ObjectIdentity
h3cRmonExtEvent=_H3cRmonExtEvent_ObjectIdentity((1,3,6,1,4,1,2011,10,2,125,0))
if mibBuilder.loadTexts:h3cRmonExtEvent.setStatus(_A)
_H3cRmonExtAlarmTable_Object=MibTable
h3cRmonExtAlarmTable=_H3cRmonExtAlarmTable_Object((1,3,6,1,4,1,2011,10,2,125,1))
if mibBuilder.loadTexts:h3cRmonExtAlarmTable.setStatus(_A)
_H3cRmonExtAlarmEntry_Object=MibTableRow
h3cRmonExtAlarmEntry=_H3cRmonExtAlarmEntry_Object((1,3,6,1,4,1,2011,10,2,125,1,1))
h3cRmonExtAlarmEntry.setIndexNames((0,_C,_E))
if mibBuilder.loadTexts:h3cRmonExtAlarmEntry.setStatus(_A)
class _H3cRmonExtAlarmIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_H3cRmonExtAlarmIndex_Type.__name__=_D
_H3cRmonExtAlarmIndex_Object=MibTableColumn
h3cRmonExtAlarmIndex=_H3cRmonExtAlarmIndex_Object((1,3,6,1,4,1,2011,10,2,125,1,1,1),_H3cRmonExtAlarmIndex_Type())
h3cRmonExtAlarmIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:h3cRmonExtAlarmIndex.setStatus(_A)
class _H3cRmonExtAlarmInterval_Type(Integer32):defaultValue=1800;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,65535))
_H3cRmonExtAlarmInterval_Type.__name__=_D
_H3cRmonExtAlarmInterval_Object=MibTableColumn
h3cRmonExtAlarmInterval=_H3cRmonExtAlarmInterval_Object((1,3,6,1,4,1,2011,10,2,125,1,1,2),_H3cRmonExtAlarmInterval_Type())
h3cRmonExtAlarmInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cRmonExtAlarmInterval.setStatus(_A)
_H3cRmonExtAlarmVariable_Type=DisplayString
_H3cRmonExtAlarmVariable_Object=MibTableColumn
h3cRmonExtAlarmVariable=_H3cRmonExtAlarmVariable_Object((1,3,6,1,4,1,2011,10,2,125,1,1,3),_H3cRmonExtAlarmVariable_Type())
h3cRmonExtAlarmVariable.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cRmonExtAlarmVariable.setStatus(_A)
_H3cRmonExtAlarmSympol_Type=DisplayString
_H3cRmonExtAlarmSympol_Object=MibTableColumn
h3cRmonExtAlarmSympol=_H3cRmonExtAlarmSympol_Object((1,3,6,1,4,1,2011,10,2,125,1,1,4),_H3cRmonExtAlarmSympol_Type())
h3cRmonExtAlarmSympol.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cRmonExtAlarmSympol.setStatus(_A)
class _H3cRmonExtAlarmSampleType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('absoluteValue',1),('deltaValue',2),('speedValue',3)))
_H3cRmonExtAlarmSampleType_Type.__name__=_D
_H3cRmonExtAlarmSampleType_Object=MibTableColumn
h3cRmonExtAlarmSampleType=_H3cRmonExtAlarmSampleType_Object((1,3,6,1,4,1,2011,10,2,125,1,1,5),_H3cRmonExtAlarmSampleType_Type())
h3cRmonExtAlarmSampleType.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cRmonExtAlarmSampleType.setStatus(_A)
_H3cRmonExtAlarmValue_Type=Integer32
_H3cRmonExtAlarmValue_Object=MibTableColumn
h3cRmonExtAlarmValue=_H3cRmonExtAlarmValue_Object((1,3,6,1,4,1,2011,10,2,125,1,1,6),_H3cRmonExtAlarmValue_Type())
h3cRmonExtAlarmValue.setMaxAccess(_I)
if mibBuilder.loadTexts:h3cRmonExtAlarmValue.setStatus(_A)
class _H3cRmonExtAlarmStartupAlarm_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('risingAlarm',1),('fallingAlarm',2),('risingOrFallingAlarm',3)))
_H3cRmonExtAlarmStartupAlarm_Type.__name__=_D
_H3cRmonExtAlarmStartupAlarm_Object=MibTableColumn
h3cRmonExtAlarmStartupAlarm=_H3cRmonExtAlarmStartupAlarm_Object((1,3,6,1,4,1,2011,10,2,125,1,1,7),_H3cRmonExtAlarmStartupAlarm_Type())
h3cRmonExtAlarmStartupAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cRmonExtAlarmStartupAlarm.setStatus(_A)
class _H3cRmonExtAlarmRisingThreshold_Type(Integer32):defaultValue=1
_H3cRmonExtAlarmRisingThreshold_Type.__name__=_D
_H3cRmonExtAlarmRisingThreshold_Object=MibTableColumn
h3cRmonExtAlarmRisingThreshold=_H3cRmonExtAlarmRisingThreshold_Object((1,3,6,1,4,1,2011,10,2,125,1,1,8),_H3cRmonExtAlarmRisingThreshold_Type())
h3cRmonExtAlarmRisingThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cRmonExtAlarmRisingThreshold.setStatus(_A)
class _H3cRmonExtAlarmFallingThreshold_Type(Integer32):defaultValue=0
_H3cRmonExtAlarmFallingThreshold_Type.__name__=_D
_H3cRmonExtAlarmFallingThreshold_Object=MibTableColumn
h3cRmonExtAlarmFallingThreshold=_H3cRmonExtAlarmFallingThreshold_Object((1,3,6,1,4,1,2011,10,2,125,1,1,9),_H3cRmonExtAlarmFallingThreshold_Type())
h3cRmonExtAlarmFallingThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cRmonExtAlarmFallingThreshold.setStatus(_A)
class _H3cRmonExtAlarmRisingEvtIndex_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_H3cRmonExtAlarmRisingEvtIndex_Type.__name__=_D
_H3cRmonExtAlarmRisingEvtIndex_Object=MibTableColumn
h3cRmonExtAlarmRisingEvtIndex=_H3cRmonExtAlarmRisingEvtIndex_Object((1,3,6,1,4,1,2011,10,2,125,1,1,10),_H3cRmonExtAlarmRisingEvtIndex_Type())
h3cRmonExtAlarmRisingEvtIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cRmonExtAlarmRisingEvtIndex.setStatus(_A)
class _H3cRmonExtAlarmFallingEvtIndex_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_H3cRmonExtAlarmFallingEvtIndex_Type.__name__=_D
_H3cRmonExtAlarmFallingEvtIndex_Object=MibTableColumn
h3cRmonExtAlarmFallingEvtIndex=_H3cRmonExtAlarmFallingEvtIndex_Object((1,3,6,1,4,1,2011,10,2,125,1,1,11),_H3cRmonExtAlarmFallingEvtIndex_Type())
h3cRmonExtAlarmFallingEvtIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cRmonExtAlarmFallingEvtIndex.setStatus(_A)
class _H3cRmonExtAlarmStatCycle_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967))
_H3cRmonExtAlarmStatCycle_Type.__name__=_D
_H3cRmonExtAlarmStatCycle_Object=MibTableColumn
h3cRmonExtAlarmStatCycle=_H3cRmonExtAlarmStatCycle_Object((1,3,6,1,4,1,2011,10,2,125,1,1,12),_H3cRmonExtAlarmStatCycle_Type())
h3cRmonExtAlarmStatCycle.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cRmonExtAlarmStatCycle.setStatus(_A)
class _H3cRmonExtAlarmStatType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('forever',1),('during',2)))
_H3cRmonExtAlarmStatType_Type.__name__=_D
_H3cRmonExtAlarmStatType_Object=MibTableColumn
h3cRmonExtAlarmStatType=_H3cRmonExtAlarmStatType_Object((1,3,6,1,4,1,2011,10,2,125,1,1,13),_H3cRmonExtAlarmStatType_Type())
h3cRmonExtAlarmStatType.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cRmonExtAlarmStatType.setStatus(_A)
_H3cRmonExtAlarmOwner_Type=OwnerString
_H3cRmonExtAlarmOwner_Object=MibTableColumn
h3cRmonExtAlarmOwner=_H3cRmonExtAlarmOwner_Object((1,3,6,1,4,1,2011,10,2,125,1,1,14),_H3cRmonExtAlarmOwner_Type())
h3cRmonExtAlarmOwner.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cRmonExtAlarmOwner.setStatus(_A)
_H3cRmonExtAlarmStatus_Type=EntryStatus
_H3cRmonExtAlarmStatus_Object=MibTableColumn
h3cRmonExtAlarmStatus=_H3cRmonExtAlarmStatus_Object((1,3,6,1,4,1,2011,10,2,125,1,1,15),_H3cRmonExtAlarmStatus_Type())
h3cRmonExtAlarmStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cRmonExtAlarmStatus.setStatus(_A)
h3cRmonExtRisingAlarm=NotificationType((1,3,6,1,4,1,2011,10,2,125,0,1))
h3cRmonExtRisingAlarm.setObjects(*((_C,_E),(_C,_F),(_C,_G),(_C,_H),(_C,_J)))
if mibBuilder.loadTexts:h3cRmonExtRisingAlarm.setStatus(_A)
h3cRmonExtFallingAlarm=NotificationType((1,3,6,1,4,1,2011,10,2,125,0,2))
h3cRmonExtFallingAlarm.setObjects(*((_C,_E),(_C,_F),(_C,_G),(_C,_H),(_C,_K)))
if mibBuilder.loadTexts:h3cRmonExtFallingAlarm.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'h3cRmonExt':h3cRmonExt,'h3cRmonExtEvent':h3cRmonExtEvent,'h3cRmonExtRisingAlarm':h3cRmonExtRisingAlarm,'h3cRmonExtFallingAlarm':h3cRmonExtFallingAlarm,'h3cRmonExtAlarmTable':h3cRmonExtAlarmTable,'h3cRmonExtAlarmEntry':h3cRmonExtAlarmEntry,_E:h3cRmonExtAlarmIndex,'h3cRmonExtAlarmInterval':h3cRmonExtAlarmInterval,'h3cRmonExtAlarmVariable':h3cRmonExtAlarmVariable,_F:h3cRmonExtAlarmSympol,_G:h3cRmonExtAlarmSampleType,_H:h3cRmonExtAlarmValue,'h3cRmonExtAlarmStartupAlarm':h3cRmonExtAlarmStartupAlarm,_J:h3cRmonExtAlarmRisingThreshold,_K:h3cRmonExtAlarmFallingThreshold,'h3cRmonExtAlarmRisingEvtIndex':h3cRmonExtAlarmRisingEvtIndex,'h3cRmonExtAlarmFallingEvtIndex':h3cRmonExtAlarmFallingEvtIndex,'h3cRmonExtAlarmStatCycle':h3cRmonExtAlarmStatCycle,'h3cRmonExtAlarmStatType':h3cRmonExtAlarmStatType,'h3cRmonExtAlarmOwner':h3cRmonExtAlarmOwner,'h3cRmonExtAlarmStatus':h3cRmonExtAlarmStatus})