_N='aggrL1AlarmAggregatorIndex'
_M='aggrL1AggregableType'
_L='aggrL1AggregableIndex'
_K='aggrL1CapabilityAggregatorIndex'
_J='aggrL1CapabilityAggregableType'
_I='aggrL1CapabilityAggregableIndex'
_H='aggrL1ConnAggregableType'
_G='aggrL1ConnAggregableIndex'
_F='read-write'
_E='read-create'
_D='AlarmSeverityCode'
_C='SIAE-AGGRL1-MANAGEMENT-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndexOrZero,=mibBuilder.importSymbols('IF-MIB','InterfaceIndexOrZero')
AlarmSeverityCode,AlarmStatus=mibBuilder.importSymbols('SIAE-ALARM-MIB',_D,'AlarmStatus')
siaeMib,=mibBuilder.importSymbols('SIAE-TREE-MIB','siaeMib')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,StorageType,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','StorageType','TextualConvention')
aggregationL1=ModuleIdentity((1,3,6,1,4,1,3373,1103,83))
if mibBuilder.loadTexts:aggregationL1.setRevisions(('2016-10-18 00:00','2014-09-29 00:00','2014-05-26 00:00'))
class AggregableType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('other',1),('radio',2),('lan',3)))
_AggrL1MibVersion_Type=Integer32
_AggrL1MibVersion_Object=MibScalar
aggrL1MibVersion=_AggrL1MibVersion_Object((1,3,6,1,4,1,3373,1103,83,1),_AggrL1MibVersion_Type())
aggrL1MibVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:aggrL1MibVersion.setStatus(_A)
_AggrL1CapabilityTable_Object=MibTable
aggrL1CapabilityTable=_AggrL1CapabilityTable_Object((1,3,6,1,4,1,3373,1103,83,2))
if mibBuilder.loadTexts:aggrL1CapabilityTable.setStatus(_A)
_AggrL1CapabilityEntry_Object=MibTableRow
aggrL1CapabilityEntry=_AggrL1CapabilityEntry_Object((1,3,6,1,4,1,3373,1103,83,2,1))
aggrL1CapabilityEntry.setIndexNames((0,_C,_I),(0,_C,_J),(0,_C,_K))
if mibBuilder.loadTexts:aggrL1CapabilityEntry.setStatus(_A)
_AggrL1CapabilityAggregableIndex_Type=Integer32
_AggrL1CapabilityAggregableIndex_Object=MibTableColumn
aggrL1CapabilityAggregableIndex=_AggrL1CapabilityAggregableIndex_Object((1,3,6,1,4,1,3373,1103,83,2,1,1),_AggrL1CapabilityAggregableIndex_Type())
aggrL1CapabilityAggregableIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:aggrL1CapabilityAggregableIndex.setStatus(_A)
_AggrL1CapabilityAggregableType_Type=AggregableType
_AggrL1CapabilityAggregableType_Object=MibTableColumn
aggrL1CapabilityAggregableType=_AggrL1CapabilityAggregableType_Object((1,3,6,1,4,1,3373,1103,83,2,1,2),_AggrL1CapabilityAggregableType_Type())
aggrL1CapabilityAggregableType.setMaxAccess(_B)
if mibBuilder.loadTexts:aggrL1CapabilityAggregableType.setStatus(_A)
_AggrL1CapabilityAggregatorIndex_Type=InterfaceIndexOrZero
_AggrL1CapabilityAggregatorIndex_Object=MibTableColumn
aggrL1CapabilityAggregatorIndex=_AggrL1CapabilityAggregatorIndex_Object((1,3,6,1,4,1,3373,1103,83,2,1,3),_AggrL1CapabilityAggregatorIndex_Type())
aggrL1CapabilityAggregatorIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:aggrL1CapabilityAggregatorIndex.setStatus(_A)
_AggrL1Table_Object=MibTable
aggrL1Table=_AggrL1Table_Object((1,3,6,1,4,1,3373,1103,83,3))
if mibBuilder.loadTexts:aggrL1Table.setStatus(_A)
_AggrL1Entry_Object=MibTableRow
aggrL1Entry=_AggrL1Entry_Object((1,3,6,1,4,1,3373,1103,83,3,1))
aggrL1Entry.setIndexNames((0,_C,_L),(0,_C,_M))
if mibBuilder.loadTexts:aggrL1Entry.setStatus(_A)
_AggrL1AggregableIndex_Type=Integer32
_AggrL1AggregableIndex_Object=MibTableColumn
aggrL1AggregableIndex=_AggrL1AggregableIndex_Object((1,3,6,1,4,1,3373,1103,83,3,1,1),_AggrL1AggregableIndex_Type())
aggrL1AggregableIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:aggrL1AggregableIndex.setStatus(_A)
_AggrL1AggregableType_Type=AggregableType
_AggrL1AggregableType_Object=MibTableColumn
aggrL1AggregableType=_AggrL1AggregableType_Object((1,3,6,1,4,1,3373,1103,83,3,1,2),_AggrL1AggregableType_Type())
aggrL1AggregableType.setMaxAccess(_B)
if mibBuilder.loadTexts:aggrL1AggregableType.setStatus(_A)
_AggrL1AggregatorIndex_Type=InterfaceIndexOrZero
_AggrL1AggregatorIndex_Object=MibTableColumn
aggrL1AggregatorIndex=_AggrL1AggregatorIndex_Object((1,3,6,1,4,1,3373,1103,83,3,1,3),_AggrL1AggregatorIndex_Type())
aggrL1AggregatorIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:aggrL1AggregatorIndex.setStatus(_A)
_AggrL1StorageType_Type=StorageType
_AggrL1StorageType_Object=MibTableColumn
aggrL1StorageType=_AggrL1StorageType_Object((1,3,6,1,4,1,3373,1103,83,3,1,4),_AggrL1StorageType_Type())
aggrL1StorageType.setMaxAccess(_E)
if mibBuilder.loadTexts:aggrL1StorageType.setStatus(_A)
_AggrL1Rowstatus_Type=RowStatus
_AggrL1Rowstatus_Object=MibTableColumn
aggrL1Rowstatus=_AggrL1Rowstatus_Object((1,3,6,1,4,1,3373,1103,83,3,1,5),_AggrL1Rowstatus_Type())
aggrL1Rowstatus.setMaxAccess(_E)
if mibBuilder.loadTexts:aggrL1Rowstatus.setStatus(_A)
_AggrL1AlarmTable_Object=MibTable
aggrL1AlarmTable=_AggrL1AlarmTable_Object((1,3,6,1,4,1,3373,1103,83,4))
if mibBuilder.loadTexts:aggrL1AlarmTable.setStatus(_A)
_AggrL1AlarmEntry_Object=MibTableRow
aggrL1AlarmEntry=_AggrL1AlarmEntry_Object((1,3,6,1,4,1,3373,1103,83,4,1))
aggrL1AlarmEntry.setIndexNames((0,_C,_N))
if mibBuilder.loadTexts:aggrL1AlarmEntry.setStatus(_A)
_AggrL1AlarmAggregatorIndex_Type=InterfaceIndexOrZero
_AggrL1AlarmAggregatorIndex_Object=MibTableColumn
aggrL1AlarmAggregatorIndex=_AggrL1AlarmAggregatorIndex_Object((1,3,6,1,4,1,3373,1103,83,4,1,1),_AggrL1AlarmAggregatorIndex_Type())
aggrL1AlarmAggregatorIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:aggrL1AlarmAggregatorIndex.setStatus(_A)
_AggrL1FailAlarm_Type=AlarmStatus
_AggrL1FailAlarm_Object=MibTableColumn
aggrL1FailAlarm=_AggrL1FailAlarm_Object((1,3,6,1,4,1,3373,1103,83,4,1,2),_AggrL1FailAlarm_Type())
aggrL1FailAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:aggrL1FailAlarm.setStatus(_A)
_AggrL1DegradeAlarm_Type=AlarmStatus
_AggrL1DegradeAlarm_Object=MibTableColumn
aggrL1DegradeAlarm=_AggrL1DegradeAlarm_Object((1,3,6,1,4,1,3373,1103,83,4,1,3),_AggrL1DegradeAlarm_Type())
aggrL1DegradeAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:aggrL1DegradeAlarm.setStatus(_A)
_AggrL1RealignmentAlarm_Type=AlarmStatus
_AggrL1RealignmentAlarm_Object=MibTableColumn
aggrL1RealignmentAlarm=_AggrL1RealignmentAlarm_Object((1,3,6,1,4,1,3373,1103,83,4,1,4),_AggrL1RealignmentAlarm_Type())
aggrL1RealignmentAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:aggrL1RealignmentAlarm.setStatus(_A)
class _AggrL1FailAlarmSeverityCode_Type(AlarmSeverityCode):defaultValue=5
_AggrL1FailAlarmSeverityCode_Type.__name__=_D
_AggrL1FailAlarmSeverityCode_Object=MibScalar
aggrL1FailAlarmSeverityCode=_AggrL1FailAlarmSeverityCode_Object((1,3,6,1,4,1,3373,1103,83,5),_AggrL1FailAlarmSeverityCode_Type())
aggrL1FailAlarmSeverityCode.setMaxAccess(_F)
if mibBuilder.loadTexts:aggrL1FailAlarmSeverityCode.setStatus(_A)
class _AggrL1DegradeAlarmSeverityCode_Type(AlarmSeverityCode):defaultValue=5
_AggrL1DegradeAlarmSeverityCode_Type.__name__=_D
_AggrL1DegradeAlarmSeverityCode_Object=MibScalar
aggrL1DegradeAlarmSeverityCode=_AggrL1DegradeAlarmSeverityCode_Object((1,3,6,1,4,1,3373,1103,83,6),_AggrL1DegradeAlarmSeverityCode_Type())
aggrL1DegradeAlarmSeverityCode.setMaxAccess(_F)
if mibBuilder.loadTexts:aggrL1DegradeAlarmSeverityCode.setStatus(_A)
class _AggrL1RealignmentAlarmSeverityCode_Type(AlarmSeverityCode):defaultValue=5
_AggrL1RealignmentAlarmSeverityCode_Type.__name__=_D
_AggrL1RealignmentAlarmSeverityCode_Object=MibScalar
aggrL1RealignmentAlarmSeverityCode=_AggrL1RealignmentAlarmSeverityCode_Object((1,3,6,1,4,1,3373,1103,83,7),_AggrL1RealignmentAlarmSeverityCode_Type())
aggrL1RealignmentAlarmSeverityCode.setMaxAccess(_F)
if mibBuilder.loadTexts:aggrL1RealignmentAlarmSeverityCode.setStatus(_A)
_AggrL1ConnectionTable_Object=MibTable
aggrL1ConnectionTable=_AggrL1ConnectionTable_Object((1,3,6,1,4,1,3373,1103,83,8))
if mibBuilder.loadTexts:aggrL1ConnectionTable.setStatus(_A)
_AggrL1ConnectionEntry_Object=MibTableRow
aggrL1ConnectionEntry=_AggrL1ConnectionEntry_Object((1,3,6,1,4,1,3373,1103,83,8,1))
aggrL1ConnectionEntry.setIndexNames((0,_C,_G),(0,_C,_H))
if mibBuilder.loadTexts:aggrL1ConnectionEntry.setStatus(_A)
_AggrL1ConnAggregableIndex_Type=Integer32
_AggrL1ConnAggregableIndex_Object=MibTableColumn
aggrL1ConnAggregableIndex=_AggrL1ConnAggregableIndex_Object((1,3,6,1,4,1,3373,1103,83,8,1,1),_AggrL1ConnAggregableIndex_Type())
aggrL1ConnAggregableIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:aggrL1ConnAggregableIndex.setStatus(_A)
_AggrL1ConnAggregableType_Type=AggregableType
_AggrL1ConnAggregableType_Object=MibTableColumn
aggrL1ConnAggregableType=_AggrL1ConnAggregableType_Object((1,3,6,1,4,1,3373,1103,83,8,1,2),_AggrL1ConnAggregableType_Type())
aggrL1ConnAggregableType.setMaxAccess(_B)
if mibBuilder.loadTexts:aggrL1ConnAggregableType.setStatus(_A)
_AggrL1ConnAggregatorIndex_Type=InterfaceIndexOrZero
_AggrL1ConnAggregatorIndex_Object=MibTableColumn
aggrL1ConnAggregatorIndex=_AggrL1ConnAggregatorIndex_Object((1,3,6,1,4,1,3373,1103,83,8,1,3),_AggrL1ConnAggregatorIndex_Type())
aggrL1ConnAggregatorIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:aggrL1ConnAggregatorIndex.setStatus(_A)
_AggrL1CarrierTable_Object=MibTable
aggrL1CarrierTable=_AggrL1CarrierTable_Object((1,3,6,1,4,1,3373,1103,83,9))
if mibBuilder.loadTexts:aggrL1CarrierTable.setStatus(_A)
_AggrL1CarrierEntry_Object=MibTableRow
aggrL1CarrierEntry=_AggrL1CarrierEntry_Object((1,3,6,1,4,1,3373,1103,83,9,1))
aggrL1CarrierEntry.setIndexNames((0,_C,_G),(0,_C,_H))
if mibBuilder.loadTexts:aggrL1CarrierEntry.setStatus(_A)
_AggrL1CarrierIpAddress_Type=IpAddress
_AggrL1CarrierIpAddress_Object=MibTableColumn
aggrL1CarrierIpAddress=_AggrL1CarrierIpAddress_Object((1,3,6,1,4,1,3373,1103,83,9,1,1),_AggrL1CarrierIpAddress_Type())
aggrL1CarrierIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:aggrL1CarrierIpAddress.setStatus(_A)
_AggrL1CarrierMinCapacity_Type=Integer32
_AggrL1CarrierMinCapacity_Object=MibTableColumn
aggrL1CarrierMinCapacity=_AggrL1CarrierMinCapacity_Object((1,3,6,1,4,1,3373,1103,83,9,1,2),_AggrL1CarrierMinCapacity_Type())
aggrL1CarrierMinCapacity.setMaxAccess(_B)
if mibBuilder.loadTexts:aggrL1CarrierMinCapacity.setStatus(_A)
if mibBuilder.loadTexts:aggrL1CarrierMinCapacity.setUnits('Kbps')
_AggrL1CarrierMaxCapacity_Type=Integer32
_AggrL1CarrierMaxCapacity_Object=MibTableColumn
aggrL1CarrierMaxCapacity=_AggrL1CarrierMaxCapacity_Object((1,3,6,1,4,1,3373,1103,83,9,1,3),_AggrL1CarrierMaxCapacity_Type())
aggrL1CarrierMaxCapacity.setMaxAccess(_B)
if mibBuilder.loadTexts:aggrL1CarrierMaxCapacity.setStatus(_A)
if mibBuilder.loadTexts:aggrL1CarrierMaxCapacity.setUnits('Kbps')
mibBuilder.exportSymbols(_C,**{'AggregableType':AggregableType,'aggregationL1':aggregationL1,'aggrL1MibVersion':aggrL1MibVersion,'aggrL1CapabilityTable':aggrL1CapabilityTable,'aggrL1CapabilityEntry':aggrL1CapabilityEntry,_I:aggrL1CapabilityAggregableIndex,_J:aggrL1CapabilityAggregableType,_K:aggrL1CapabilityAggregatorIndex,'aggrL1Table':aggrL1Table,'aggrL1Entry':aggrL1Entry,_L:aggrL1AggregableIndex,_M:aggrL1AggregableType,'aggrL1AggregatorIndex':aggrL1AggregatorIndex,'aggrL1StorageType':aggrL1StorageType,'aggrL1Rowstatus':aggrL1Rowstatus,'aggrL1AlarmTable':aggrL1AlarmTable,'aggrL1AlarmEntry':aggrL1AlarmEntry,_N:aggrL1AlarmAggregatorIndex,'aggrL1FailAlarm':aggrL1FailAlarm,'aggrL1DegradeAlarm':aggrL1DegradeAlarm,'aggrL1RealignmentAlarm':aggrL1RealignmentAlarm,'aggrL1FailAlarmSeverityCode':aggrL1FailAlarmSeverityCode,'aggrL1DegradeAlarmSeverityCode':aggrL1DegradeAlarmSeverityCode,'aggrL1RealignmentAlarmSeverityCode':aggrL1RealignmentAlarmSeverityCode,'aggrL1ConnectionTable':aggrL1ConnectionTable,'aggrL1ConnectionEntry':aggrL1ConnectionEntry,_G:aggrL1ConnAggregableIndex,_H:aggrL1ConnAggregableType,'aggrL1ConnAggregatorIndex':aggrL1ConnAggregatorIndex,'aggrL1CarrierTable':aggrL1CarrierTable,'aggrL1CarrierEntry':aggrL1CarrierEntry,'aggrL1CarrierIpAddress':aggrL1CarrierIpAddress,'aggrL1CarrierMinCapacity':aggrL1CarrierMinCapacity,'aggrL1CarrierMaxCapacity':aggrL1CarrierMaxCapacity})