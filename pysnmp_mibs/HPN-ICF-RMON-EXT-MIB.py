_M='hpnicfprialarmFallingThreshold'
_L='hpnicfprialarmRisingThreshold'
_K='hpnicfTrapDestEntry'
_J='hpnicfrmonEnableIfIndex'
_I='hpnicfprialarmValue'
_H='hpnicfprialarmSampleType'
_G='hpnicfprialarmSympol'
_F='read-only'
_E='hpnicfprialarmIndex'
_D='Integer32'
_C='read-write'
_B='HPN-ICF-RMON-EXT-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hpnicfrmonExtend,=mibBuilder.importSymbols('HPN-ICF-OID-MIB','hpnicfrmonExtend')
OwnerString,=mibBuilder.importSymbols('IF-MIB','OwnerString')
EntryStatus,=mibBuilder.importSymbols('RMON-MIB','EntryStatus')
trapDestEntry,trapDestIndex=mibBuilder.importSymbols('RMON2-MIB','trapDestEntry','trapDestIndex')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
hpnicfperformance=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,15,8,4,4))
if mibBuilder.loadTexts:hpnicfperformance.setRevisions(('2003-03-15 00:00',))
_HpnicfrmonExtendEventsV2_ObjectIdentity=ObjectIdentity
hpnicfrmonExtendEventsV2=_HpnicfrmonExtendEventsV2_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,8,4,0))
if mibBuilder.loadTexts:hpnicfrmonExtendEventsV2.setStatus(_A)
_HpnicfprialarmTable_Object=MibTable
hpnicfprialarmTable=_HpnicfprialarmTable_Object((1,3,6,1,4,1,11,2,14,11,15,8,4,4,1))
if mibBuilder.loadTexts:hpnicfprialarmTable.setStatus(_A)
_HpnicfprialarmEntry_Object=MibTableRow
hpnicfprialarmEntry=_HpnicfprialarmEntry_Object((1,3,6,1,4,1,11,2,14,11,15,8,4,4,1,1))
hpnicfprialarmEntry.setIndexNames((0,_B,_E))
if mibBuilder.loadTexts:hpnicfprialarmEntry.setStatus(_A)
class _HpnicfprialarmIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_HpnicfprialarmIndex_Type.__name__=_D
_HpnicfprialarmIndex_Object=MibTableColumn
hpnicfprialarmIndex=_HpnicfprialarmIndex_Object((1,3,6,1,4,1,11,2,14,11,15,8,4,4,1,1,1),_HpnicfprialarmIndex_Type())
hpnicfprialarmIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfprialarmIndex.setStatus(_A)
_HpnicfprialarmInterval_Type=Integer32
_HpnicfprialarmInterval_Object=MibTableColumn
hpnicfprialarmInterval=_HpnicfprialarmInterval_Object((1,3,6,1,4,1,11,2,14,11,15,8,4,4,1,1,2),_HpnicfprialarmInterval_Type())
hpnicfprialarmInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfprialarmInterval.setStatus(_A)
_HpnicfprialarmVariable_Type=DisplayString
_HpnicfprialarmVariable_Object=MibTableColumn
hpnicfprialarmVariable=_HpnicfprialarmVariable_Object((1,3,6,1,4,1,11,2,14,11,15,8,4,4,1,1,3),_HpnicfprialarmVariable_Type())
hpnicfprialarmVariable.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfprialarmVariable.setStatus(_A)
_HpnicfprialarmSympol_Type=DisplayString
_HpnicfprialarmSympol_Object=MibTableColumn
hpnicfprialarmSympol=_HpnicfprialarmSympol_Object((1,3,6,1,4,1,11,2,14,11,15,8,4,4,1,1,4),_HpnicfprialarmSympol_Type())
hpnicfprialarmSympol.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfprialarmSympol.setStatus(_A)
class _HpnicfprialarmSampleType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('absoluteValue',1),('deltaValue',2),('speedValue',3)))
_HpnicfprialarmSampleType_Type.__name__=_D
_HpnicfprialarmSampleType_Object=MibTableColumn
hpnicfprialarmSampleType=_HpnicfprialarmSampleType_Object((1,3,6,1,4,1,11,2,14,11,15,8,4,4,1,1,5),_HpnicfprialarmSampleType_Type())
hpnicfprialarmSampleType.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfprialarmSampleType.setStatus(_A)
_HpnicfprialarmValue_Type=Integer32
_HpnicfprialarmValue_Object=MibTableColumn
hpnicfprialarmValue=_HpnicfprialarmValue_Object((1,3,6,1,4,1,11,2,14,11,15,8,4,4,1,1,6),_HpnicfprialarmValue_Type())
hpnicfprialarmValue.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfprialarmValue.setStatus(_A)
class _HpnicfprialarmStartupAlarm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('risingAlarm',1),('fallingAlarm',2),('risingOrFallingAlarm',3)))
_HpnicfprialarmStartupAlarm_Type.__name__=_D
_HpnicfprialarmStartupAlarm_Object=MibTableColumn
hpnicfprialarmStartupAlarm=_HpnicfprialarmStartupAlarm_Object((1,3,6,1,4,1,11,2,14,11,15,8,4,4,1,1,7),_HpnicfprialarmStartupAlarm_Type())
hpnicfprialarmStartupAlarm.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfprialarmStartupAlarm.setStatus(_A)
_HpnicfprialarmRisingThreshold_Type=Integer32
_HpnicfprialarmRisingThreshold_Object=MibTableColumn
hpnicfprialarmRisingThreshold=_HpnicfprialarmRisingThreshold_Object((1,3,6,1,4,1,11,2,14,11,15,8,4,4,1,1,8),_HpnicfprialarmRisingThreshold_Type())
hpnicfprialarmRisingThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfprialarmRisingThreshold.setStatus(_A)
_HpnicfprialarmFallingThreshold_Type=Integer32
_HpnicfprialarmFallingThreshold_Object=MibTableColumn
hpnicfprialarmFallingThreshold=_HpnicfprialarmFallingThreshold_Object((1,3,6,1,4,1,11,2,14,11,15,8,4,4,1,1,9),_HpnicfprialarmFallingThreshold_Type())
hpnicfprialarmFallingThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfprialarmFallingThreshold.setStatus(_A)
class _HpnicfprialarmRisingEventIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HpnicfprialarmRisingEventIndex_Type.__name__=_D
_HpnicfprialarmRisingEventIndex_Object=MibTableColumn
hpnicfprialarmRisingEventIndex=_HpnicfprialarmRisingEventIndex_Object((1,3,6,1,4,1,11,2,14,11,15,8,4,4,1,1,10),_HpnicfprialarmRisingEventIndex_Type())
hpnicfprialarmRisingEventIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfprialarmRisingEventIndex.setStatus(_A)
class _HpnicfprialarmFallingEventIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HpnicfprialarmFallingEventIndex_Type.__name__=_D
_HpnicfprialarmFallingEventIndex_Object=MibTableColumn
hpnicfprialarmFallingEventIndex=_HpnicfprialarmFallingEventIndex_Object((1,3,6,1,4,1,11,2,14,11,15,8,4,4,1,1,11),_HpnicfprialarmFallingEventIndex_Type())
hpnicfprialarmFallingEventIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfprialarmFallingEventIndex.setStatus(_A)
_HpnicfprialarmStatCycle_Type=Integer32
_HpnicfprialarmStatCycle_Object=MibTableColumn
hpnicfprialarmStatCycle=_HpnicfprialarmStatCycle_Object((1,3,6,1,4,1,11,2,14,11,15,8,4,4,1,1,12),_HpnicfprialarmStatCycle_Type())
hpnicfprialarmStatCycle.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfprialarmStatCycle.setStatus(_A)
class _HpnicfprialarmStatType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('forever',1),('during',2)))
_HpnicfprialarmStatType_Type.__name__=_D
_HpnicfprialarmStatType_Object=MibTableColumn
hpnicfprialarmStatType=_HpnicfprialarmStatType_Object((1,3,6,1,4,1,11,2,14,11,15,8,4,4,1,1,13),_HpnicfprialarmStatType_Type())
hpnicfprialarmStatType.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfprialarmStatType.setStatus(_A)
_HpnicfprialarmOwner_Type=OwnerString
_HpnicfprialarmOwner_Object=MibTableColumn
hpnicfprialarmOwner=_HpnicfprialarmOwner_Object((1,3,6,1,4,1,11,2,14,11,15,8,4,4,1,1,14),_HpnicfprialarmOwner_Type())
hpnicfprialarmOwner.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfprialarmOwner.setStatus(_A)
_HpnicfprialarmStatus_Type=EntryStatus
_HpnicfprialarmStatus_Object=MibTableColumn
hpnicfprialarmStatus=_HpnicfprialarmStatus_Object((1,3,6,1,4,1,11,2,14,11,15,8,4,4,1,1,15),_HpnicfprialarmStatus_Type())
hpnicfprialarmStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfprialarmStatus.setStatus(_A)
_HpnicfrmonEnableTable_Object=MibTable
hpnicfrmonEnableTable=_HpnicfrmonEnableTable_Object((1,3,6,1,4,1,11,2,14,11,15,8,4,5))
if mibBuilder.loadTexts:hpnicfrmonEnableTable.setStatus(_A)
_HpnicfrmonEnableEntry_Object=MibTableRow
hpnicfrmonEnableEntry=_HpnicfrmonEnableEntry_Object((1,3,6,1,4,1,11,2,14,11,15,8,4,5,1))
hpnicfrmonEnableEntry.setIndexNames((0,_B,_J))
if mibBuilder.loadTexts:hpnicfrmonEnableEntry.setStatus(_A)
class _HpnicfrmonEnableIfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HpnicfrmonEnableIfIndex_Type.__name__=_D
_HpnicfrmonEnableIfIndex_Object=MibTableColumn
hpnicfrmonEnableIfIndex=_HpnicfrmonEnableIfIndex_Object((1,3,6,1,4,1,11,2,14,11,15,8,4,5,1,1),_HpnicfrmonEnableIfIndex_Type())
hpnicfrmonEnableIfIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfrmonEnableIfIndex.setStatus(_A)
class _HpnicfrmonEnableStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enable',1),('disable',2)))
_HpnicfrmonEnableStatus_Type.__name__=_D
_HpnicfrmonEnableStatus_Object=MibTableColumn
hpnicfrmonEnableStatus=_HpnicfrmonEnableStatus_Object((1,3,6,1,4,1,11,2,14,11,15,8,4,5,1,2),_HpnicfrmonEnableStatus_Type())
hpnicfrmonEnableStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfrmonEnableStatus.setStatus(_A)
_HpnicfTrapDestTable_Object=MibTable
hpnicfTrapDestTable=_HpnicfTrapDestTable_Object((1,3,6,1,4,1,11,2,14,11,15,8,4,6))
if mibBuilder.loadTexts:hpnicfTrapDestTable.setStatus(_A)
_HpnicfTrapDestEntry_Object=MibTableRow
hpnicfTrapDestEntry=_HpnicfTrapDestEntry_Object((1,3,6,1,4,1,11,2,14,11,15,8,4,6,1))
if mibBuilder.loadTexts:hpnicfTrapDestEntry.setStatus(_A)
class _HpnicfTrapDestVersion_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('snmpv1',1),('snmpv2',2),('snmpv3andauthen',3),('snmpv3andnoauthen',4),('snmpv3andpriv',5)))
_HpnicfTrapDestVersion_Type.__name__=_D
_HpnicfTrapDestVersion_Object=MibTableColumn
hpnicfTrapDestVersion=_HpnicfTrapDestVersion_Object((1,3,6,1,4,1,11,2,14,11,15,8,4,6,1,1),_HpnicfTrapDestVersion_Type())
hpnicfTrapDestVersion.setMaxAccess('read-create')
if mibBuilder.loadTexts:hpnicfTrapDestVersion.setStatus(_A)
trapDestEntry.registerAugmentions((_B,_K))
hpnicfTrapDestEntry.setIndexNames(*trapDestEntry.getIndexNames())
hpnicfpririsingAlarm=NotificationType((1,3,6,1,4,1,11,2,14,11,15,8,4,0,1))
hpnicfpririsingAlarm.setObjects(*((_B,_E),(_B,_G),(_B,_H),(_B,_I),(_B,_L)))
if mibBuilder.loadTexts:hpnicfpririsingAlarm.setStatus(_A)
hpnicfprifallingAlarm=NotificationType((1,3,6,1,4,1,11,2,14,11,15,8,4,0,2))
hpnicfprifallingAlarm.setObjects(*((_B,_E),(_B,_G),(_B,_H),(_B,_I),(_B,_M)))
if mibBuilder.loadTexts:hpnicfprifallingAlarm.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'hpnicfrmonExtendEventsV2':hpnicfrmonExtendEventsV2,'hpnicfpririsingAlarm':hpnicfpririsingAlarm,'hpnicfprifallingAlarm':hpnicfprifallingAlarm,'hpnicfperformance':hpnicfperformance,'hpnicfprialarmTable':hpnicfprialarmTable,'hpnicfprialarmEntry':hpnicfprialarmEntry,_E:hpnicfprialarmIndex,'hpnicfprialarmInterval':hpnicfprialarmInterval,'hpnicfprialarmVariable':hpnicfprialarmVariable,_G:hpnicfprialarmSympol,_H:hpnicfprialarmSampleType,_I:hpnicfprialarmValue,'hpnicfprialarmStartupAlarm':hpnicfprialarmStartupAlarm,_L:hpnicfprialarmRisingThreshold,_M:hpnicfprialarmFallingThreshold,'hpnicfprialarmRisingEventIndex':hpnicfprialarmRisingEventIndex,'hpnicfprialarmFallingEventIndex':hpnicfprialarmFallingEventIndex,'hpnicfprialarmStatCycle':hpnicfprialarmStatCycle,'hpnicfprialarmStatType':hpnicfprialarmStatType,'hpnicfprialarmOwner':hpnicfprialarmOwner,'hpnicfprialarmStatus':hpnicfprialarmStatus,'hpnicfrmonEnableTable':hpnicfrmonEnableTable,'hpnicfrmonEnableEntry':hpnicfrmonEnableEntry,_J:hpnicfrmonEnableIfIndex,'hpnicfrmonEnableStatus':hpnicfrmonEnableStatus,'hpnicfTrapDestTable':hpnicfTrapDestTable,_K:hpnicfTrapDestEntry,'hpnicfTrapDestVersion':hpnicfTrapDestVersion})