_M='prialarmFallingThreshold'
_L='prialarmRisingThreshold'
_K='hwTrapDestEntry'
_J='hwrmonEnableIfIndex'
_I='prialarmValue'
_H='prialarmSampleType'
_G='prialarmSympol'
_F='read-only'
_E='prialarmIndex'
_D='Integer32'
_C='read-write'
_B='HUAWEI-RMON-EXT-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hwInternetProtocol,hwLocal,rmonExtend=mibBuilder.importSymbols('HUAWEI-3COM-OID-MIB','hwInternetProtocol','hwLocal','rmonExtend')
OwnerString,=mibBuilder.importSymbols('IF-MIB','OwnerString')
EntryStatus,=mibBuilder.importSymbols('RMON-MIB','EntryStatus')
trapDestEntry,trapDestIndex=mibBuilder.importSymbols('RMON2-MIB','trapDestEntry','trapDestIndex')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
performance=ModuleIdentity((1,3,6,1,4,1,2011,1,3,4,4))
if mibBuilder.loadTexts:performance.setRevisions(('2003-03-15 00:00',))
_RmonExtendEventsV2_ObjectIdentity=ObjectIdentity
rmonExtendEventsV2=_RmonExtendEventsV2_ObjectIdentity((1,3,6,1,4,1,2011,1,3,4,0))
if mibBuilder.loadTexts:rmonExtendEventsV2.setStatus(_A)
_PrialarmTable_Object=MibTable
prialarmTable=_PrialarmTable_Object((1,3,6,1,4,1,2011,1,3,4,4,1))
if mibBuilder.loadTexts:prialarmTable.setStatus(_A)
_PrialarmEntry_Object=MibTableRow
prialarmEntry=_PrialarmEntry_Object((1,3,6,1,4,1,2011,1,3,4,4,1,1))
prialarmEntry.setIndexNames((0,_B,_E))
if mibBuilder.loadTexts:prialarmEntry.setStatus(_A)
class _PrialarmIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_PrialarmIndex_Type.__name__=_D
_PrialarmIndex_Object=MibTableColumn
prialarmIndex=_PrialarmIndex_Object((1,3,6,1,4,1,2011,1,3,4,4,1,1,1),_PrialarmIndex_Type())
prialarmIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:prialarmIndex.setStatus(_A)
_PrialarmInterval_Type=Integer32
_PrialarmInterval_Object=MibTableColumn
prialarmInterval=_PrialarmInterval_Object((1,3,6,1,4,1,2011,1,3,4,4,1,1,2),_PrialarmInterval_Type())
prialarmInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:prialarmInterval.setStatus(_A)
_PrialarmVariable_Type=DisplayString
_PrialarmVariable_Object=MibTableColumn
prialarmVariable=_PrialarmVariable_Object((1,3,6,1,4,1,2011,1,3,4,4,1,1,3),_PrialarmVariable_Type())
prialarmVariable.setMaxAccess(_C)
if mibBuilder.loadTexts:prialarmVariable.setStatus(_A)
_PrialarmSympol_Type=DisplayString
_PrialarmSympol_Object=MibTableColumn
prialarmSympol=_PrialarmSympol_Object((1,3,6,1,4,1,2011,1,3,4,4,1,1,4),_PrialarmSympol_Type())
prialarmSympol.setMaxAccess(_C)
if mibBuilder.loadTexts:prialarmSympol.setStatus(_A)
class _PrialarmSampleType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('absoluteValue',1),('deltaValue',2),('speedValue',3)))
_PrialarmSampleType_Type.__name__=_D
_PrialarmSampleType_Object=MibTableColumn
prialarmSampleType=_PrialarmSampleType_Object((1,3,6,1,4,1,2011,1,3,4,4,1,1,5),_PrialarmSampleType_Type())
prialarmSampleType.setMaxAccess(_C)
if mibBuilder.loadTexts:prialarmSampleType.setStatus(_A)
_PrialarmValue_Type=Integer32
_PrialarmValue_Object=MibTableColumn
prialarmValue=_PrialarmValue_Object((1,3,6,1,4,1,2011,1,3,4,4,1,1,6),_PrialarmValue_Type())
prialarmValue.setMaxAccess(_F)
if mibBuilder.loadTexts:prialarmValue.setStatus(_A)
class _PrialarmStartupAlarm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('risingAlarm',1),('fallingAlarm',2),('risingOrFallingAlarm',3)))
_PrialarmStartupAlarm_Type.__name__=_D
_PrialarmStartupAlarm_Object=MibTableColumn
prialarmStartupAlarm=_PrialarmStartupAlarm_Object((1,3,6,1,4,1,2011,1,3,4,4,1,1,7),_PrialarmStartupAlarm_Type())
prialarmStartupAlarm.setMaxAccess(_C)
if mibBuilder.loadTexts:prialarmStartupAlarm.setStatus(_A)
_PrialarmRisingThreshold_Type=Integer32
_PrialarmRisingThreshold_Object=MibTableColumn
prialarmRisingThreshold=_PrialarmRisingThreshold_Object((1,3,6,1,4,1,2011,1,3,4,4,1,1,8),_PrialarmRisingThreshold_Type())
prialarmRisingThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:prialarmRisingThreshold.setStatus(_A)
_PrialarmFallingThreshold_Type=Integer32
_PrialarmFallingThreshold_Object=MibTableColumn
prialarmFallingThreshold=_PrialarmFallingThreshold_Object((1,3,6,1,4,1,2011,1,3,4,4,1,1,9),_PrialarmFallingThreshold_Type())
prialarmFallingThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:prialarmFallingThreshold.setStatus(_A)
class _PrialarmRisingEventIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PrialarmRisingEventIndex_Type.__name__=_D
_PrialarmRisingEventIndex_Object=MibTableColumn
prialarmRisingEventIndex=_PrialarmRisingEventIndex_Object((1,3,6,1,4,1,2011,1,3,4,4,1,1,10),_PrialarmRisingEventIndex_Type())
prialarmRisingEventIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:prialarmRisingEventIndex.setStatus(_A)
class _PrialarmFallingEventIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PrialarmFallingEventIndex_Type.__name__=_D
_PrialarmFallingEventIndex_Object=MibTableColumn
prialarmFallingEventIndex=_PrialarmFallingEventIndex_Object((1,3,6,1,4,1,2011,1,3,4,4,1,1,11),_PrialarmFallingEventIndex_Type())
prialarmFallingEventIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:prialarmFallingEventIndex.setStatus(_A)
_PrialarmStatCycle_Type=Integer32
_PrialarmStatCycle_Object=MibTableColumn
prialarmStatCycle=_PrialarmStatCycle_Object((1,3,6,1,4,1,2011,1,3,4,4,1,1,12),_PrialarmStatCycle_Type())
prialarmStatCycle.setMaxAccess(_C)
if mibBuilder.loadTexts:prialarmStatCycle.setStatus(_A)
class _PrialarmStatType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('forever',1),('during',2)))
_PrialarmStatType_Type.__name__=_D
_PrialarmStatType_Object=MibTableColumn
prialarmStatType=_PrialarmStatType_Object((1,3,6,1,4,1,2011,1,3,4,4,1,1,13),_PrialarmStatType_Type())
prialarmStatType.setMaxAccess(_C)
if mibBuilder.loadTexts:prialarmStatType.setStatus(_A)
_PrialarmOwner_Type=OwnerString
_PrialarmOwner_Object=MibTableColumn
prialarmOwner=_PrialarmOwner_Object((1,3,6,1,4,1,2011,1,3,4,4,1,1,14),_PrialarmOwner_Type())
prialarmOwner.setMaxAccess(_C)
if mibBuilder.loadTexts:prialarmOwner.setStatus(_A)
_PrialarmStatus_Type=EntryStatus
_PrialarmStatus_Object=MibTableColumn
prialarmStatus=_PrialarmStatus_Object((1,3,6,1,4,1,2011,1,3,4,4,1,1,15),_PrialarmStatus_Type())
prialarmStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:prialarmStatus.setStatus(_A)
_HwrmonEnableTable_Object=MibTable
hwrmonEnableTable=_HwrmonEnableTable_Object((1,3,6,1,4,1,2011,1,3,4,5))
if mibBuilder.loadTexts:hwrmonEnableTable.setStatus(_A)
_HwrmonEnableTableEntry_Object=MibTableRow
hwrmonEnableTableEntry=_HwrmonEnableTableEntry_Object((1,3,6,1,4,1,2011,1,3,4,5,1))
hwrmonEnableTableEntry.setIndexNames((0,_B,_J))
if mibBuilder.loadTexts:hwrmonEnableTableEntry.setStatus(_A)
class _HwrmonEnableIfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HwrmonEnableIfIndex_Type.__name__=_D
_HwrmonEnableIfIndex_Object=MibTableColumn
hwrmonEnableIfIndex=_HwrmonEnableIfIndex_Object((1,3,6,1,4,1,2011,1,3,4,5,1,1),_HwrmonEnableIfIndex_Type())
hwrmonEnableIfIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:hwrmonEnableIfIndex.setStatus(_A)
class _HwrmonEnableStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enable',1),('disable',2)))
_HwrmonEnableStatus_Type.__name__=_D
_HwrmonEnableStatus_Object=MibTableColumn
hwrmonEnableStatus=_HwrmonEnableStatus_Object((1,3,6,1,4,1,2011,1,3,4,5,1,2),_HwrmonEnableStatus_Type())
hwrmonEnableStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hwrmonEnableStatus.setStatus(_A)
_HwTrapDestTable_Object=MibTable
hwTrapDestTable=_HwTrapDestTable_Object((1,3,6,1,4,1,2011,1,3,4,6))
if mibBuilder.loadTexts:hwTrapDestTable.setStatus(_A)
_HwTrapDestEntry_Object=MibTableRow
hwTrapDestEntry=_HwTrapDestEntry_Object((1,3,6,1,4,1,2011,1,3,4,6,1))
if mibBuilder.loadTexts:hwTrapDestEntry.setStatus(_A)
class _HwTrapDestVersion_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('snmpv1',1),('snmpv2',2),('snmpv3andauthen',3),('snmpv3andnoauthen',4),('snmpv3andpriv',5)))
_HwTrapDestVersion_Type.__name__=_D
_HwTrapDestVersion_Object=MibTableColumn
hwTrapDestVersion=_HwTrapDestVersion_Object((1,3,6,1,4,1,2011,1,3,4,6,1,1),_HwTrapDestVersion_Type())
hwTrapDestVersion.setMaxAccess('read-create')
if mibBuilder.loadTexts:hwTrapDestVersion.setStatus(_A)
trapDestEntry.registerAugmentions((_B,_K))
hwTrapDestEntry.setIndexNames(*trapDestEntry.getIndexNames())
pririsingAlarm=NotificationType((1,3,6,1,4,1,2011,1,3,4,0,1))
pririsingAlarm.setObjects(*((_B,_E),(_B,_G),(_B,_H),(_B,_I),(_B,_L)))
if mibBuilder.loadTexts:pririsingAlarm.setStatus(_A)
prifallingAlarm=NotificationType((1,3,6,1,4,1,2011,1,3,4,0,2))
prifallingAlarm.setObjects(*((_B,_E),(_B,_G),(_B,_H),(_B,_I),(_B,_M)))
if mibBuilder.loadTexts:prifallingAlarm.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'rmonExtendEventsV2':rmonExtendEventsV2,'pririsingAlarm':pririsingAlarm,'prifallingAlarm':prifallingAlarm,'performance':performance,'prialarmTable':prialarmTable,'prialarmEntry':prialarmEntry,_E:prialarmIndex,'prialarmInterval':prialarmInterval,'prialarmVariable':prialarmVariable,_G:prialarmSympol,_H:prialarmSampleType,_I:prialarmValue,'prialarmStartupAlarm':prialarmStartupAlarm,_L:prialarmRisingThreshold,_M:prialarmFallingThreshold,'prialarmRisingEventIndex':prialarmRisingEventIndex,'prialarmFallingEventIndex':prialarmFallingEventIndex,'prialarmStatCycle':prialarmStatCycle,'prialarmStatType':prialarmStatType,'prialarmOwner':prialarmOwner,'prialarmStatus':prialarmStatus,'hwrmonEnableTable':hwrmonEnableTable,'hwrmonEnableTableEntry':hwrmonEnableTableEntry,_J:hwrmonEnableIfIndex,'hwrmonEnableStatus':hwrmonEnableStatus,'hwTrapDestTable':hwTrapDestTable,_K:hwTrapDestEntry,'hwTrapDestVersion':hwTrapDestVersion})