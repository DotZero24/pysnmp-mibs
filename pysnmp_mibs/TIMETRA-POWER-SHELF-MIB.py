_f='tmnxPowerShelfNotifGroupV16v0'
_e='tmnxPowerShelfGroupV16v0'
_d='tmnxPowerShelfOutputStatusUp'
_c='tmnxPowerShelfOutputStatusDown'
_b='tmnxPowerShelfOutputStatusSwitch'
_a='tmnxPowerShelfCommsUp'
_Z='tmnxPowerShelfCommsDown'
_Y='tmnxPowerShelfInputPwrModeSwitch'
_X='tmnxPowerShelfDescription'
_W='tmnxPowerShelfSupportedTypes'
_V='tmnxPowerShelfEquippedType'
_U='tmnxPowerShelfAssignedType'
_T='tmnxPowerShelfEntryLastChanged'
_S='tmnxPowerShelfTypeDescription'
_R='tmnxPowerShelfTypeName'
_Q='tmnxPowerShelfTableLastChanged'
_P='read-create'
_O='TmnxPowerShelfType'
_N='tmnxPowerShelfHwIndex'
_M='not-accessible'
_L='tmnxPowerShelfTypeIndex'
_K='TItemDescription'
_J='tmnxCpmPowerShelfCommsFail'
_I='Unsigned32'
_H='Integer32'
_G='tmnxPowerShelfInputPowerMode'
_F='tmnxPowerShelfOutputStatus'
_E='tmnxHwClass'
_D='read-only'
_C='TIMETRA-CHASSIS-MIB'
_B='TIMETRA-POWER-SHELF-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_H,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_I,'iso')
DisplayString,PhysAddress,TextualConvention,TimeStamp=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TimeStamp')
TmnxHwIndex,tmnxCpmPowerShelfCommsFail,tmnxHwClass=mibBuilder.importSymbols(_C,'TmnxHwIndex',_J,_E)
timetraSRMIBModules,tmnxSRConfs,tmnxSRNotifyPrefix,tmnxSRObjs=mibBuilder.importSymbols('TIMETRA-GLOBAL-MIB','timetraSRMIBModules','tmnxSRConfs','tmnxSRNotifyPrefix','tmnxSRObjs')
TItemDescription,TNamedItemOrEmpty=mibBuilder.importSymbols('TIMETRA-TC-MIB',_K,'TNamedItemOrEmpty')
timetraPowerShelfMIBModule=ModuleIdentity((1,3,6,1,4,1,6527,1,1,3,118))
if mibBuilder.loadTexts:timetraPowerShelfMIBModule.setRevisions(('2017-09-12 00:00',))
class TmnxPowerShelfType(TextualConvention,Unsigned32):status=_A
class TmnxPowerShelfSuppType(TextualConvention,Bits):status=_A;namedValues=NamedValues(*(('invalidPowerShelfType',0),('unassigned',1),('suppPowerShelfType2',2),('suppPowerShelfType3',3),('suppPowerShelfType4',4),('suppPowerShelfType5',5),('suppPowerShelfType6',6),('suppPowerShelfType7',7),('suppPowerShelfType8',8),('suppPowerShelfType9',9),('suppPowerShelfType10',10),('suppPowerShelfType11',11),('suppPowerShelfType12',12),('suppPowerShelfType13',13),('suppPowerShelfType14',14),('suppPowerShelfType15',15)))
_TmnxPowerShelfConformance_ObjectIdentity=ObjectIdentity
tmnxPowerShelfConformance=_TmnxPowerShelfConformance_ObjectIdentity((1,3,6,1,4,1,6527,3,1,1,118))
_TmnxPowerShelfCompliances_ObjectIdentity=ObjectIdentity
tmnxPowerShelfCompliances=_TmnxPowerShelfCompliances_ObjectIdentity((1,3,6,1,4,1,6527,3,1,1,118,1))
_TmnxPowerShelfGroups_ObjectIdentity=ObjectIdentity
tmnxPowerShelfGroups=_TmnxPowerShelfGroups_ObjectIdentity((1,3,6,1,4,1,6527,3,1,1,118,2))
_TmnxPowerShelfObjects_ObjectIdentity=ObjectIdentity
tmnxPowerShelfObjects=_TmnxPowerShelfObjects_ObjectIdentity((1,3,6,1,4,1,6527,3,1,2,118))
_TmnxPowerShelfConfigTimestamps_ObjectIdentity=ObjectIdentity
tmnxPowerShelfConfigTimestamps=_TmnxPowerShelfConfigTimestamps_ObjectIdentity((1,3,6,1,4,1,6527,3,1,2,118,1))
_TmnxPowerShelfTableLastChanged_Type=TimeStamp
_TmnxPowerShelfTableLastChanged_Object=MibScalar
tmnxPowerShelfTableLastChanged=_TmnxPowerShelfTableLastChanged_Object((1,3,6,1,4,1,6527,3,1,2,118,1,1),_TmnxPowerShelfTableLastChanged_Type())
tmnxPowerShelfTableLastChanged.setMaxAccess(_D)
if mibBuilder.loadTexts:tmnxPowerShelfTableLastChanged.setStatus(_A)
_TmnxPowerShelfTypeTable_Object=MibTable
tmnxPowerShelfTypeTable=_TmnxPowerShelfTypeTable_Object((1,3,6,1,4,1,6527,3,1,2,118,2))
if mibBuilder.loadTexts:tmnxPowerShelfTypeTable.setStatus(_A)
_TmnxPowerShelfTypeEntry_Object=MibTableRow
tmnxPowerShelfTypeEntry=_TmnxPowerShelfTypeEntry_Object((1,3,6,1,4,1,6527,3,1,2,118,2,1))
tmnxPowerShelfTypeEntry.setIndexNames((0,_B,_L))
if mibBuilder.loadTexts:tmnxPowerShelfTypeEntry.setStatus(_A)
_TmnxPowerShelfTypeIndex_Type=TmnxPowerShelfType
_TmnxPowerShelfTypeIndex_Object=MibTableColumn
tmnxPowerShelfTypeIndex=_TmnxPowerShelfTypeIndex_Object((1,3,6,1,4,1,6527,3,1,2,118,2,1,1),_TmnxPowerShelfTypeIndex_Type())
tmnxPowerShelfTypeIndex.setMaxAccess(_M)
if mibBuilder.loadTexts:tmnxPowerShelfTypeIndex.setStatus(_A)
_TmnxPowerShelfTypeName_Type=TNamedItemOrEmpty
_TmnxPowerShelfTypeName_Object=MibTableColumn
tmnxPowerShelfTypeName=_TmnxPowerShelfTypeName_Object((1,3,6,1,4,1,6527,3,1,2,118,2,1,2),_TmnxPowerShelfTypeName_Type())
tmnxPowerShelfTypeName.setMaxAccess(_D)
if mibBuilder.loadTexts:tmnxPowerShelfTypeName.setStatus(_A)
_TmnxPowerShelfTypeDescription_Type=TItemDescription
_TmnxPowerShelfTypeDescription_Object=MibTableColumn
tmnxPowerShelfTypeDescription=_TmnxPowerShelfTypeDescription_Object((1,3,6,1,4,1,6527,3,1,2,118,2,1,3),_TmnxPowerShelfTypeDescription_Type())
tmnxPowerShelfTypeDescription.setMaxAccess(_D)
if mibBuilder.loadTexts:tmnxPowerShelfTypeDescription.setStatus(_A)
_TmnxPowerShelfConfigurations_ObjectIdentity=ObjectIdentity
tmnxPowerShelfConfigurations=_TmnxPowerShelfConfigurations_ObjectIdentity((1,3,6,1,4,1,6527,3,1,2,118,3))
_TmnxPowerShelfTable_Object=MibTable
tmnxPowerShelfTable=_TmnxPowerShelfTable_Object((1,3,6,1,4,1,6527,3,1,2,118,3,1))
if mibBuilder.loadTexts:tmnxPowerShelfTable.setStatus(_A)
_TmnxPowerShelfEntry_Object=MibTableRow
tmnxPowerShelfEntry=_TmnxPowerShelfEntry_Object((1,3,6,1,4,1,6527,3,1,2,118,3,1,1))
tmnxPowerShelfEntry.setIndexNames((0,_B,_N))
if mibBuilder.loadTexts:tmnxPowerShelfEntry.setStatus(_A)
_TmnxPowerShelfHwIndex_Type=TmnxHwIndex
_TmnxPowerShelfHwIndex_Object=MibTableColumn
tmnxPowerShelfHwIndex=_TmnxPowerShelfHwIndex_Object((1,3,6,1,4,1,6527,3,1,2,118,3,1,1,1),_TmnxPowerShelfHwIndex_Type())
tmnxPowerShelfHwIndex.setMaxAccess(_M)
if mibBuilder.loadTexts:tmnxPowerShelfHwIndex.setStatus(_A)
_TmnxPowerShelfEntryLastChanged_Type=TimeStamp
_TmnxPowerShelfEntryLastChanged_Object=MibTableColumn
tmnxPowerShelfEntryLastChanged=_TmnxPowerShelfEntryLastChanged_Object((1,3,6,1,4,1,6527,3,1,2,118,3,1,1,2),_TmnxPowerShelfEntryLastChanged_Type())
tmnxPowerShelfEntryLastChanged.setMaxAccess(_D)
if mibBuilder.loadTexts:tmnxPowerShelfEntryLastChanged.setStatus(_A)
class _TmnxPowerShelfAssignedType_Type(TmnxPowerShelfType):defaultValue=1
_TmnxPowerShelfAssignedType_Type.__name__=_O
_TmnxPowerShelfAssignedType_Object=MibTableColumn
tmnxPowerShelfAssignedType=_TmnxPowerShelfAssignedType_Object((1,3,6,1,4,1,6527,3,1,2,118,3,1,1,3),_TmnxPowerShelfAssignedType_Type())
tmnxPowerShelfAssignedType.setMaxAccess(_P)
if mibBuilder.loadTexts:tmnxPowerShelfAssignedType.setStatus(_A)
_TmnxPowerShelfEquippedType_Type=TmnxPowerShelfType
_TmnxPowerShelfEquippedType_Object=MibTableColumn
tmnxPowerShelfEquippedType=_TmnxPowerShelfEquippedType_Object((1,3,6,1,4,1,6527,3,1,2,118,3,1,1,4),_TmnxPowerShelfEquippedType_Type())
tmnxPowerShelfEquippedType.setMaxAccess(_D)
if mibBuilder.loadTexts:tmnxPowerShelfEquippedType.setStatus(_A)
_TmnxPowerShelfSupportedTypes_Type=TmnxPowerShelfSuppType
_TmnxPowerShelfSupportedTypes_Object=MibTableColumn
tmnxPowerShelfSupportedTypes=_TmnxPowerShelfSupportedTypes_Object((1,3,6,1,4,1,6527,3,1,2,118,3,1,1,5),_TmnxPowerShelfSupportedTypes_Type())
tmnxPowerShelfSupportedTypes.setMaxAccess(_D)
if mibBuilder.loadTexts:tmnxPowerShelfSupportedTypes.setStatus(_A)
class _TmnxPowerShelfDescription_Type(TItemDescription):defaultHexValue=''
_TmnxPowerShelfDescription_Type.__name__=_K
_TmnxPowerShelfDescription_Object=MibTableColumn
tmnxPowerShelfDescription=_TmnxPowerShelfDescription_Object((1,3,6,1,4,1,6527,3,1,2,118,3,1,1,6),_TmnxPowerShelfDescription_Type())
tmnxPowerShelfDescription.setMaxAccess(_P)
if mibBuilder.loadTexts:tmnxPowerShelfDescription.setStatus(_A)
class _TmnxPowerShelfInputPowerMode_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(60,60),ValueRangeConstraint(80,80))
_TmnxPowerShelfInputPowerMode_Type.__name__=_I
_TmnxPowerShelfInputPowerMode_Object=MibTableColumn
tmnxPowerShelfInputPowerMode=_TmnxPowerShelfInputPowerMode_Object((1,3,6,1,4,1,6527,3,1,2,118,3,1,1,7),_TmnxPowerShelfInputPowerMode_Type())
tmnxPowerShelfInputPowerMode.setMaxAccess(_D)
if mibBuilder.loadTexts:tmnxPowerShelfInputPowerMode.setStatus(_A)
if mibBuilder.loadTexts:tmnxPowerShelfInputPowerMode.setUnits('amperes')
class _TmnxPowerShelfOutputStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('unknown',0),('on',1),('off',2),('notEquipped',3)))
_TmnxPowerShelfOutputStatus_Type.__name__=_H
_TmnxPowerShelfOutputStatus_Object=MibTableColumn
tmnxPowerShelfOutputStatus=_TmnxPowerShelfOutputStatus_Object((1,3,6,1,4,1,6527,3,1,2,118,3,1,1,8),_TmnxPowerShelfOutputStatus_Type())
tmnxPowerShelfOutputStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:tmnxPowerShelfOutputStatus.setStatus(_A)
_TmnxPowerShelfNotifyPrefix_ObjectIdentity=ObjectIdentity
tmnxPowerShelfNotifyPrefix=_TmnxPowerShelfNotifyPrefix_ObjectIdentity((1,3,6,1,4,1,6527,3,1,3,120))
_TmnxPowerShelfNotification_ObjectIdentity=ObjectIdentity
tmnxPowerShelfNotification=_TmnxPowerShelfNotification_ObjectIdentity((1,3,6,1,4,1,6527,3,1,3,120,0))
_TmnxPowerShelfNotifications_ObjectIdentity=ObjectIdentity
tmnxPowerShelfNotifications=_TmnxPowerShelfNotifications_ObjectIdentity((1,3,6,1,4,1,6527,3,1,3,120,0,1))
tmnxPowerShelfGroupV16v0=ObjectGroup((1,3,6,1,4,1,6527,3,1,1,118,2,1))
tmnxPowerShelfGroupV16v0.setObjects(*((_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_G),(_B,_F)))
if mibBuilder.loadTexts:tmnxPowerShelfGroupV16v0.setStatus(_A)
tmnxPowerShelfInputPwrModeSwitch=NotificationType((1,3,6,1,4,1,6527,3,1,3,120,0,1,1))
tmnxPowerShelfInputPwrModeSwitch.setObjects(*((_C,_E),(_B,_G)))
if mibBuilder.loadTexts:tmnxPowerShelfInputPwrModeSwitch.setStatus(_A)
tmnxPowerShelfCommsDown=NotificationType((1,3,6,1,4,1,6527,3,1,3,120,0,1,2))
tmnxPowerShelfCommsDown.setObjects(*((_C,_E),(_C,_J)))
if mibBuilder.loadTexts:tmnxPowerShelfCommsDown.setStatus(_A)
tmnxPowerShelfCommsUp=NotificationType((1,3,6,1,4,1,6527,3,1,3,120,0,1,3))
tmnxPowerShelfCommsUp.setObjects((_C,_E))
if mibBuilder.loadTexts:tmnxPowerShelfCommsUp.setStatus(_A)
tmnxPowerShelfOutputStatusSwitch=NotificationType((1,3,6,1,4,1,6527,3,1,3,120,0,1,4))
tmnxPowerShelfOutputStatusSwitch.setObjects(*((_C,_E),(_B,_F)))
if mibBuilder.loadTexts:tmnxPowerShelfOutputStatusSwitch.setStatus(_A)
tmnxPowerShelfOutputStatusDown=NotificationType((1,3,6,1,4,1,6527,3,1,3,120,0,1,5))
tmnxPowerShelfOutputStatusDown.setObjects(*((_C,_E),(_B,_F)))
if mibBuilder.loadTexts:tmnxPowerShelfOutputStatusDown.setStatus(_A)
tmnxPowerShelfOutputStatusUp=NotificationType((1,3,6,1,4,1,6527,3,1,3,120,0,1,6))
tmnxPowerShelfOutputStatusUp.setObjects(*((_C,_E),(_B,_F)))
if mibBuilder.loadTexts:tmnxPowerShelfOutputStatusUp.setStatus(_A)
tmnxPowerShelfNotifGroupV16v0=NotificationGroup((1,3,6,1,4,1,6527,3,1,1,118,2,2))
tmnxPowerShelfNotifGroupV16v0.setObjects(*((_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d)))
if mibBuilder.loadTexts:tmnxPowerShelfNotifGroupV16v0.setStatus(_A)
tmnxPowerShelfComplianceV16v0=ModuleCompliance((1,3,6,1,4,1,6527,3,1,1,118,1,1))
tmnxPowerShelfComplianceV16v0.setObjects(*((_B,_e),(_B,_f)))
if mibBuilder.loadTexts:tmnxPowerShelfComplianceV16v0.setStatus(_A)
mibBuilder.exportSymbols(_B,**{_O:TmnxPowerShelfType,'TmnxPowerShelfSuppType':TmnxPowerShelfSuppType,'timetraPowerShelfMIBModule':timetraPowerShelfMIBModule,'tmnxPowerShelfConformance':tmnxPowerShelfConformance,'tmnxPowerShelfCompliances':tmnxPowerShelfCompliances,'tmnxPowerShelfComplianceV16v0':tmnxPowerShelfComplianceV16v0,'tmnxPowerShelfGroups':tmnxPowerShelfGroups,_e:tmnxPowerShelfGroupV16v0,_f:tmnxPowerShelfNotifGroupV16v0,'tmnxPowerShelfObjects':tmnxPowerShelfObjects,'tmnxPowerShelfConfigTimestamps':tmnxPowerShelfConfigTimestamps,_Q:tmnxPowerShelfTableLastChanged,'tmnxPowerShelfTypeTable':tmnxPowerShelfTypeTable,'tmnxPowerShelfTypeEntry':tmnxPowerShelfTypeEntry,_L:tmnxPowerShelfTypeIndex,_R:tmnxPowerShelfTypeName,_S:tmnxPowerShelfTypeDescription,'tmnxPowerShelfConfigurations':tmnxPowerShelfConfigurations,'tmnxPowerShelfTable':tmnxPowerShelfTable,'tmnxPowerShelfEntry':tmnxPowerShelfEntry,_N:tmnxPowerShelfHwIndex,_T:tmnxPowerShelfEntryLastChanged,_U:tmnxPowerShelfAssignedType,_V:tmnxPowerShelfEquippedType,_W:tmnxPowerShelfSupportedTypes,_X:tmnxPowerShelfDescription,_G:tmnxPowerShelfInputPowerMode,_F:tmnxPowerShelfOutputStatus,'tmnxPowerShelfNotifyPrefix':tmnxPowerShelfNotifyPrefix,'tmnxPowerShelfNotification':tmnxPowerShelfNotification,'tmnxPowerShelfNotifications':tmnxPowerShelfNotifications,_Y:tmnxPowerShelfInputPwrModeSwitch,_Z:tmnxPowerShelfCommsDown,_a:tmnxPowerShelfCommsUp,_b:tmnxPowerShelfOutputStatusSwitch,_c:tmnxPowerShelfOutputStatusDown,_d:tmnxPowerShelfOutputStatusUp})