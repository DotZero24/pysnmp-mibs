_K='hpnicfRmonExtAlarmFallingThreshold'
_J='hpnicfRmonExtAlarmRisingThreshold'
_I='read-only'
_H='hpnicfRmonExtAlarmValue'
_G='hpnicfRmonExtAlarmSampleType'
_F='hpnicfRmonExtAlarmSympol'
_E='hpnicfRmonExtAlarmIndex'
_D='Integer32'
_C='HPN-ICF-RMON-EXT2-MIB'
_B='read-create'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hpnicfCommon,=mibBuilder.importSymbols('HPN-ICF-OID-MIB','hpnicfCommon')
EntryStatus,OwnerString=mibBuilder.importSymbols('RMON-MIB','EntryStatus','OwnerString')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
hpnicfRmonExt=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,15,2,125))
if mibBuilder.loadTexts:hpnicfRmonExt.setRevisions(('2012-06-19 00:00',))
_HpnicfRmonExtEvent_ObjectIdentity=ObjectIdentity
hpnicfRmonExtEvent=_HpnicfRmonExtEvent_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,125,0))
if mibBuilder.loadTexts:hpnicfRmonExtEvent.setStatus(_A)
_HpnicfRmonExtAlarmTable_Object=MibTable
hpnicfRmonExtAlarmTable=_HpnicfRmonExtAlarmTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,125,1))
if mibBuilder.loadTexts:hpnicfRmonExtAlarmTable.setStatus(_A)
_HpnicfRmonExtAlarmEntry_Object=MibTableRow
hpnicfRmonExtAlarmEntry=_HpnicfRmonExtAlarmEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,125,1,1))
hpnicfRmonExtAlarmEntry.setIndexNames((0,_C,_E))
if mibBuilder.loadTexts:hpnicfRmonExtAlarmEntry.setStatus(_A)
class _HpnicfRmonExtAlarmIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_HpnicfRmonExtAlarmIndex_Type.__name__=_D
_HpnicfRmonExtAlarmIndex_Object=MibTableColumn
hpnicfRmonExtAlarmIndex=_HpnicfRmonExtAlarmIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,125,1,1,1),_HpnicfRmonExtAlarmIndex_Type())
hpnicfRmonExtAlarmIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:hpnicfRmonExtAlarmIndex.setStatus(_A)
class _HpnicfRmonExtAlarmInterval_Type(Integer32):defaultValue=1800;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,65535))
_HpnicfRmonExtAlarmInterval_Type.__name__=_D
_HpnicfRmonExtAlarmInterval_Object=MibTableColumn
hpnicfRmonExtAlarmInterval=_HpnicfRmonExtAlarmInterval_Object((1,3,6,1,4,1,11,2,14,11,15,2,125,1,1,2),_HpnicfRmonExtAlarmInterval_Type())
hpnicfRmonExtAlarmInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfRmonExtAlarmInterval.setStatus(_A)
_HpnicfRmonExtAlarmVariable_Type=DisplayString
_HpnicfRmonExtAlarmVariable_Object=MibTableColumn
hpnicfRmonExtAlarmVariable=_HpnicfRmonExtAlarmVariable_Object((1,3,6,1,4,1,11,2,14,11,15,2,125,1,1,3),_HpnicfRmonExtAlarmVariable_Type())
hpnicfRmonExtAlarmVariable.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfRmonExtAlarmVariable.setStatus(_A)
_HpnicfRmonExtAlarmSympol_Type=DisplayString
_HpnicfRmonExtAlarmSympol_Object=MibTableColumn
hpnicfRmonExtAlarmSympol=_HpnicfRmonExtAlarmSympol_Object((1,3,6,1,4,1,11,2,14,11,15,2,125,1,1,4),_HpnicfRmonExtAlarmSympol_Type())
hpnicfRmonExtAlarmSympol.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfRmonExtAlarmSympol.setStatus(_A)
class _HpnicfRmonExtAlarmSampleType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('absoluteValue',1),('deltaValue',2),('speedValue',3)))
_HpnicfRmonExtAlarmSampleType_Type.__name__=_D
_HpnicfRmonExtAlarmSampleType_Object=MibTableColumn
hpnicfRmonExtAlarmSampleType=_HpnicfRmonExtAlarmSampleType_Object((1,3,6,1,4,1,11,2,14,11,15,2,125,1,1,5),_HpnicfRmonExtAlarmSampleType_Type())
hpnicfRmonExtAlarmSampleType.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfRmonExtAlarmSampleType.setStatus(_A)
_HpnicfRmonExtAlarmValue_Type=Integer32
_HpnicfRmonExtAlarmValue_Object=MibTableColumn
hpnicfRmonExtAlarmValue=_HpnicfRmonExtAlarmValue_Object((1,3,6,1,4,1,11,2,14,11,15,2,125,1,1,6),_HpnicfRmonExtAlarmValue_Type())
hpnicfRmonExtAlarmValue.setMaxAccess(_I)
if mibBuilder.loadTexts:hpnicfRmonExtAlarmValue.setStatus(_A)
class _HpnicfRmonExtAlarmStartupAlarm_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('risingAlarm',1),('fallingAlarm',2),('risingOrFallingAlarm',3)))
_HpnicfRmonExtAlarmStartupAlarm_Type.__name__=_D
_HpnicfRmonExtAlarmStartupAlarm_Object=MibTableColumn
hpnicfRmonExtAlarmStartupAlarm=_HpnicfRmonExtAlarmStartupAlarm_Object((1,3,6,1,4,1,11,2,14,11,15,2,125,1,1,7),_HpnicfRmonExtAlarmStartupAlarm_Type())
hpnicfRmonExtAlarmStartupAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfRmonExtAlarmStartupAlarm.setStatus(_A)
class _HpnicfRmonExtAlarmRisingThreshold_Type(Integer32):defaultValue=1
_HpnicfRmonExtAlarmRisingThreshold_Type.__name__=_D
_HpnicfRmonExtAlarmRisingThreshold_Object=MibTableColumn
hpnicfRmonExtAlarmRisingThreshold=_HpnicfRmonExtAlarmRisingThreshold_Object((1,3,6,1,4,1,11,2,14,11,15,2,125,1,1,8),_HpnicfRmonExtAlarmRisingThreshold_Type())
hpnicfRmonExtAlarmRisingThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfRmonExtAlarmRisingThreshold.setStatus(_A)
class _HpnicfRmonExtAlarmFallingThreshold_Type(Integer32):defaultValue=0
_HpnicfRmonExtAlarmFallingThreshold_Type.__name__=_D
_HpnicfRmonExtAlarmFallingThreshold_Object=MibTableColumn
hpnicfRmonExtAlarmFallingThreshold=_HpnicfRmonExtAlarmFallingThreshold_Object((1,3,6,1,4,1,11,2,14,11,15,2,125,1,1,9),_HpnicfRmonExtAlarmFallingThreshold_Type())
hpnicfRmonExtAlarmFallingThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfRmonExtAlarmFallingThreshold.setStatus(_A)
class _HpnicfRmonExtAlarmRisingEvtIndex_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HpnicfRmonExtAlarmRisingEvtIndex_Type.__name__=_D
_HpnicfRmonExtAlarmRisingEvtIndex_Object=MibTableColumn
hpnicfRmonExtAlarmRisingEvtIndex=_HpnicfRmonExtAlarmRisingEvtIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,125,1,1,10),_HpnicfRmonExtAlarmRisingEvtIndex_Type())
hpnicfRmonExtAlarmRisingEvtIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfRmonExtAlarmRisingEvtIndex.setStatus(_A)
class _HpnicfRmonExtAlarmFallingEvtIndex_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HpnicfRmonExtAlarmFallingEvtIndex_Type.__name__=_D
_HpnicfRmonExtAlarmFallingEvtIndex_Object=MibTableColumn
hpnicfRmonExtAlarmFallingEvtIndex=_HpnicfRmonExtAlarmFallingEvtIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,125,1,1,11),_HpnicfRmonExtAlarmFallingEvtIndex_Type())
hpnicfRmonExtAlarmFallingEvtIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfRmonExtAlarmFallingEvtIndex.setStatus(_A)
class _HpnicfRmonExtAlarmStatCycle_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967))
_HpnicfRmonExtAlarmStatCycle_Type.__name__=_D
_HpnicfRmonExtAlarmStatCycle_Object=MibTableColumn
hpnicfRmonExtAlarmStatCycle=_HpnicfRmonExtAlarmStatCycle_Object((1,3,6,1,4,1,11,2,14,11,15,2,125,1,1,12),_HpnicfRmonExtAlarmStatCycle_Type())
hpnicfRmonExtAlarmStatCycle.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfRmonExtAlarmStatCycle.setStatus(_A)
class _HpnicfRmonExtAlarmStatType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('forever',1),('during',2)))
_HpnicfRmonExtAlarmStatType_Type.__name__=_D
_HpnicfRmonExtAlarmStatType_Object=MibTableColumn
hpnicfRmonExtAlarmStatType=_HpnicfRmonExtAlarmStatType_Object((1,3,6,1,4,1,11,2,14,11,15,2,125,1,1,13),_HpnicfRmonExtAlarmStatType_Type())
hpnicfRmonExtAlarmStatType.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfRmonExtAlarmStatType.setStatus(_A)
_HpnicfRmonExtAlarmOwner_Type=OwnerString
_HpnicfRmonExtAlarmOwner_Object=MibTableColumn
hpnicfRmonExtAlarmOwner=_HpnicfRmonExtAlarmOwner_Object((1,3,6,1,4,1,11,2,14,11,15,2,125,1,1,14),_HpnicfRmonExtAlarmOwner_Type())
hpnicfRmonExtAlarmOwner.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfRmonExtAlarmOwner.setStatus(_A)
_HpnicfRmonExtAlarmStatus_Type=EntryStatus
_HpnicfRmonExtAlarmStatus_Object=MibTableColumn
hpnicfRmonExtAlarmStatus=_HpnicfRmonExtAlarmStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,125,1,1,15),_HpnicfRmonExtAlarmStatus_Type())
hpnicfRmonExtAlarmStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfRmonExtAlarmStatus.setStatus(_A)
hpnicfRmonExtRisingAlarm=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,125,0,1))
hpnicfRmonExtRisingAlarm.setObjects(*((_C,_E),(_C,_F),(_C,_G),(_C,_H),(_C,_J)))
if mibBuilder.loadTexts:hpnicfRmonExtRisingAlarm.setStatus(_A)
hpnicfRmonExtFallingAlarm=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,125,0,2))
hpnicfRmonExtFallingAlarm.setObjects(*((_C,_E),(_C,_F),(_C,_G),(_C,_H),(_C,_K)))
if mibBuilder.loadTexts:hpnicfRmonExtFallingAlarm.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'hpnicfRmonExt':hpnicfRmonExt,'hpnicfRmonExtEvent':hpnicfRmonExtEvent,'hpnicfRmonExtRisingAlarm':hpnicfRmonExtRisingAlarm,'hpnicfRmonExtFallingAlarm':hpnicfRmonExtFallingAlarm,'hpnicfRmonExtAlarmTable':hpnicfRmonExtAlarmTable,'hpnicfRmonExtAlarmEntry':hpnicfRmonExtAlarmEntry,_E:hpnicfRmonExtAlarmIndex,'hpnicfRmonExtAlarmInterval':hpnicfRmonExtAlarmInterval,'hpnicfRmonExtAlarmVariable':hpnicfRmonExtAlarmVariable,_F:hpnicfRmonExtAlarmSympol,_G:hpnicfRmonExtAlarmSampleType,_H:hpnicfRmonExtAlarmValue,'hpnicfRmonExtAlarmStartupAlarm':hpnicfRmonExtAlarmStartupAlarm,_J:hpnicfRmonExtAlarmRisingThreshold,_K:hpnicfRmonExtAlarmFallingThreshold,'hpnicfRmonExtAlarmRisingEvtIndex':hpnicfRmonExtAlarmRisingEvtIndex,'hpnicfRmonExtAlarmFallingEvtIndex':hpnicfRmonExtAlarmFallingEvtIndex,'hpnicfRmonExtAlarmStatCycle':hpnicfRmonExtAlarmStatCycle,'hpnicfRmonExtAlarmStatType':hpnicfRmonExtAlarmStatType,'hpnicfRmonExtAlarmOwner':hpnicfRmonExtAlarmOwner,'hpnicfRmonExtAlarmStatus':hpnicfRmonExtAlarmStatus})