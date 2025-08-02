_J='slPortConfigLedMode'
_I='slPortConfigLedColor'
_H='read-write'
_G='slPortConfigLabel'
_F='slPortConfigAlarmMask'
_E='slPortConfigChangeType'
_D='read-only'
_C='slPortConfigIndex'
_B='SL-PORT-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
slMain,=mibBuilder.importSymbols('SL-MAIN-MIB','slMain')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,PhysAddress,RowStatus,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','RowStatus','TextualConvention','TimeStamp','TruthValue')
slPort=ModuleIdentity((1,3,6,1,4,1,4515,1,3,14))
class LedColor(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('off',1),('red',2),('yellow',3),('green',4)))
class LedMode(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('stable',1),('fastBlinking',2),('slowBlinking',3)))
_SlPortConfig_ObjectIdentity=ObjectIdentity
slPortConfig=_SlPortConfig_ObjectIdentity((1,3,6,1,4,1,4515,1,3,14,1))
_SlPortConfigTable_Object=MibTable
slPortConfigTable=_SlPortConfigTable_Object((1,3,6,1,4,1,4515,1,3,14,1,1))
if mibBuilder.loadTexts:slPortConfigTable.setStatus(_A)
_SlPortConfigEntry_Object=MibTableRow
slPortConfigEntry=_SlPortConfigEntry_Object((1,3,6,1,4,1,4515,1,3,14,1,1,1))
slPortConfigEntry.setIndexNames((0,_B,_C))
if mibBuilder.loadTexts:slPortConfigEntry.setStatus(_A)
_SlPortConfigIndex_Type=Integer32
_SlPortConfigIndex_Object=MibTableColumn
slPortConfigIndex=_SlPortConfigIndex_Object((1,3,6,1,4,1,4515,1,3,14,1,1,1,1),_SlPortConfigIndex_Type())
slPortConfigIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:slPortConfigIndex.setStatus(_A)
_SlPortConfigLedColor_Type=LedColor
_SlPortConfigLedColor_Object=MibTableColumn
slPortConfigLedColor=_SlPortConfigLedColor_Object((1,3,6,1,4,1,4515,1,3,14,1,1,1,2),_SlPortConfigLedColor_Type())
slPortConfigLedColor.setMaxAccess(_D)
if mibBuilder.loadTexts:slPortConfigLedColor.setStatus(_A)
_SlPortConfigLedMode_Type=LedMode
_SlPortConfigLedMode_Object=MibTableColumn
slPortConfigLedMode=_SlPortConfigLedMode_Object((1,3,6,1,4,1,4515,1,3,14,1,1,1,3),_SlPortConfigLedMode_Type())
slPortConfigLedMode.setMaxAccess(_D)
if mibBuilder.loadTexts:slPortConfigLedMode.setStatus(_A)
_SlPortConfigChangeType_Type=Integer32
_SlPortConfigChangeType_Object=MibTableColumn
slPortConfigChangeType=_SlPortConfigChangeType_Object((1,3,6,1,4,1,4515,1,3,14,1,1,1,4),_SlPortConfigChangeType_Type())
slPortConfigChangeType.setMaxAccess(_H)
if mibBuilder.loadTexts:slPortConfigChangeType.setStatus(_A)
_SlPortConfigAlarmMask_Type=TruthValue
_SlPortConfigAlarmMask_Object=MibTableColumn
slPortConfigAlarmMask=_SlPortConfigAlarmMask_Object((1,3,6,1,4,1,4515,1,3,14,1,1,1,5),_SlPortConfigAlarmMask_Type())
slPortConfigAlarmMask.setMaxAccess(_H)
if mibBuilder.loadTexts:slPortConfigAlarmMask.setStatus(_A)
_SlPortConfigLabel_Type=DisplayString
_SlPortConfigLabel_Object=MibTableColumn
slPortConfigLabel=_SlPortConfigLabel_Object((1,3,6,1,4,1,4515,1,3,14,1,1,1,6),_SlPortConfigLabel_Type())
slPortConfigLabel.setMaxAccess(_D)
if mibBuilder.loadTexts:slPortConfigLabel.setStatus(_A)
_SlPortConfigLastChange_Type=TimeTicks
_SlPortConfigLastChange_Object=MibScalar
slPortConfigLastChange=_SlPortConfigLastChange_Object((1,3,6,1,4,1,4515,1,3,14,1,2),_SlPortConfigLastChange_Type())
slPortConfigLastChange.setMaxAccess(_D)
if mibBuilder.loadTexts:slPortConfigLastChange.setStatus(_A)
_SlPortNotification_ObjectIdentity=ObjectIdentity
slPortNotification=_SlPortNotification_ObjectIdentity((1,3,6,1,4,1,4515,1,3,14,2))
slPortConfigChanged=NotificationType((1,3,6,1,4,1,4515,1,3,14,2,1))
slPortConfigChanged.setObjects(*((_B,_C),(_B,_I),(_B,_J),(_B,_E),(_B,_F),(_B,_G)))
if mibBuilder.loadTexts:slPortConfigChanged.setStatus(_A)
slPortConfigChangedType=NotificationType((1,3,6,1,4,1,4515,1,3,14,2,2))
slPortConfigChangedType.setObjects(*((_B,_C),(_B,_E)))
if mibBuilder.loadTexts:slPortConfigChangedType.setStatus(_A)
slPortConfigChangedMask=NotificationType((1,3,6,1,4,1,4515,1,3,14,2,3))
slPortConfigChangedMask.setObjects(*((_B,_C),(_B,_F)))
if mibBuilder.loadTexts:slPortConfigChangedMask.setStatus(_A)
slPortConfigChangedLabel=NotificationType((1,3,6,1,4,1,4515,1,3,14,2,4))
slPortConfigChangedLabel.setObjects(*((_B,_C),(_B,_G)))
if mibBuilder.loadTexts:slPortConfigChangedLabel.setStatus(_A)
slPortConfigChangedApsEnabled=NotificationType((1,3,6,1,4,1,4515,1,3,14,2,5))
slPortConfigChangedApsEnabled.setObjects((_B,_C))
if mibBuilder.loadTexts:slPortConfigChangedApsEnabled.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'LedColor':LedColor,'LedMode':LedMode,'slPort':slPort,'slPortConfig':slPortConfig,'slPortConfigTable':slPortConfigTable,'slPortConfigEntry':slPortConfigEntry,_C:slPortConfigIndex,_I:slPortConfigLedColor,_J:slPortConfigLedMode,_E:slPortConfigChangeType,_F:slPortConfigAlarmMask,_G:slPortConfigLabel,'slPortConfigLastChange':slPortConfigLastChange,'slPortNotification':slPortNotification,'slPortConfigChanged':slPortConfigChanged,'slPortConfigChangedType':slPortConfigChangedType,'slPortConfigChangedMask':slPortConfigChangedMask,'slPortConfigChangedLabel':slPortConfigChangedLabel,'slPortConfigChangedApsEnabled':slPortConfigChangedApsEnabled})