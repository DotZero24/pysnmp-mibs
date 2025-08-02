_Y='arubaWiredModuleTableGroup'
_X='arubaWiredModuleNotificationsGroup'
_W='arubaWiredModuleTable'
_V='arubaWiredModuleUnrecognizedNotification'
_U='arubaWiredModuleRemovedNotification'
_T='arubaWiredModuleInsertedNotification'
_S='arubaWiredModuleStateNotification'
_R='arubaWiredModulePowerPriority'
_Q='arubaWiredModuleAdminState'
_P='arubaWiredModuleProductNumber'
_O='arubaWiredModuleSerialNumber'
_N='arubaWiredModuleProductDescription'
_M='arubaWiredModuleSlotIndex'
_L='arubaWiredModuleTypeIndex'
_K='arubaWiredModuleGroupIndex'
_J='arubaWiredModuleUnrecognizedDescriptor'
_I='arubaWiredModuleState'
_H='not-accessible'
_G='Integer32'
_F='arubaWiredModuleType'
_E='arubaWiredModuleName'
_D='read-only'
_C='DisplayString'
_B='current'
_A='ARUBAWIRED-MODULE-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
arubaWiredChassisMIB,=mibBuilder.importSymbols('ARUBAWIRED-CHASSIS-MIB','arubaWiredChassisMIB')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_G,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_C,'PhysAddress','TextualConvention')
arubaWiredModule=ModuleIdentity((1,3,6,1,4,1,47196,4,1,1,3,11,6))
if mibBuilder.loadTexts:arubaWiredModule.setRevisions(('2021-07-01 00:00','2021-01-07 00:00'))
_ArubaWiredModuleNotifications_ObjectIdentity=ObjectIdentity
arubaWiredModuleNotifications=_ArubaWiredModuleNotifications_ObjectIdentity((1,3,6,1,4,1,47196,4,1,1,3,11,6,0))
_ArubaWiredModuleTable_Object=MibTable
arubaWiredModuleTable=_ArubaWiredModuleTable_Object((1,3,6,1,4,1,47196,4,1,1,3,11,6,1))
if mibBuilder.loadTexts:arubaWiredModuleTable.setStatus(_B)
_ArubaWiredModuleEntry_Object=MibTableRow
arubaWiredModuleEntry=_ArubaWiredModuleEntry_Object((1,3,6,1,4,1,47196,4,1,1,3,11,6,1,1))
arubaWiredModuleEntry.setIndexNames((0,_A,_K),(0,_A,_L),(0,_A,_M))
if mibBuilder.loadTexts:arubaWiredModuleEntry.setStatus(_B)
class _ArubaWiredModuleGroupIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_ArubaWiredModuleGroupIndex_Type.__name__=_G
_ArubaWiredModuleGroupIndex_Object=MibTableColumn
arubaWiredModuleGroupIndex=_ArubaWiredModuleGroupIndex_Object((1,3,6,1,4,1,47196,4,1,1,3,11,6,1,1,1),_ArubaWiredModuleGroupIndex_Type())
arubaWiredModuleGroupIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:arubaWiredModuleGroupIndex.setStatus(_B)
class _ArubaWiredModuleTypeIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_ArubaWiredModuleTypeIndex_Type.__name__=_G
_ArubaWiredModuleTypeIndex_Object=MibTableColumn
arubaWiredModuleTypeIndex=_ArubaWiredModuleTypeIndex_Object((1,3,6,1,4,1,47196,4,1,1,3,11,6,1,1,2),_ArubaWiredModuleTypeIndex_Type())
arubaWiredModuleTypeIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:arubaWiredModuleTypeIndex.setStatus(_B)
class _ArubaWiredModuleSlotIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_ArubaWiredModuleSlotIndex_Type.__name__=_G
_ArubaWiredModuleSlotIndex_Object=MibTableColumn
arubaWiredModuleSlotIndex=_ArubaWiredModuleSlotIndex_Object((1,3,6,1,4,1,47196,4,1,1,3,11,6,1,1,3),_ArubaWiredModuleSlotIndex_Type())
arubaWiredModuleSlotIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:arubaWiredModuleSlotIndex.setStatus(_B)
class _ArubaWiredModuleName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_ArubaWiredModuleName_Type.__name__=_C
_ArubaWiredModuleName_Object=MibTableColumn
arubaWiredModuleName=_ArubaWiredModuleName_Object((1,3,6,1,4,1,47196,4,1,1,3,11,6,1,1,4),_ArubaWiredModuleName_Type())
arubaWiredModuleName.setMaxAccess(_D)
if mibBuilder.loadTexts:arubaWiredModuleName.setStatus(_B)
class _ArubaWiredModuleType_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_ArubaWiredModuleType_Type.__name__=_C
_ArubaWiredModuleType_Object=MibTableColumn
arubaWiredModuleType=_ArubaWiredModuleType_Object((1,3,6,1,4,1,47196,4,1,1,3,11,6,1,1,5),_ArubaWiredModuleType_Type())
arubaWiredModuleType.setMaxAccess(_D)
if mibBuilder.loadTexts:arubaWiredModuleType.setStatus(_B)
class _ArubaWiredModuleState_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_ArubaWiredModuleState_Type.__name__=_C
_ArubaWiredModuleState_Object=MibTableColumn
arubaWiredModuleState=_ArubaWiredModuleState_Object((1,3,6,1,4,1,47196,4,1,1,3,11,6,1,1,6),_ArubaWiredModuleState_Type())
arubaWiredModuleState.setMaxAccess(_D)
if mibBuilder.loadTexts:arubaWiredModuleState.setStatus(_B)
class _ArubaWiredModuleProductDescription_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,80))
_ArubaWiredModuleProductDescription_Type.__name__=_C
_ArubaWiredModuleProductDescription_Object=MibTableColumn
arubaWiredModuleProductDescription=_ArubaWiredModuleProductDescription_Object((1,3,6,1,4,1,47196,4,1,1,3,11,6,1,1,7),_ArubaWiredModuleProductDescription_Type())
arubaWiredModuleProductDescription.setMaxAccess(_D)
if mibBuilder.loadTexts:arubaWiredModuleProductDescription.setStatus(_B)
class _ArubaWiredModuleSerialNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_ArubaWiredModuleSerialNumber_Type.__name__=_C
_ArubaWiredModuleSerialNumber_Object=MibTableColumn
arubaWiredModuleSerialNumber=_ArubaWiredModuleSerialNumber_Object((1,3,6,1,4,1,47196,4,1,1,3,11,6,1,1,8),_ArubaWiredModuleSerialNumber_Type())
arubaWiredModuleSerialNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:arubaWiredModuleSerialNumber.setStatus(_B)
class _ArubaWiredModuleProductNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_ArubaWiredModuleProductNumber_Type.__name__=_C
_ArubaWiredModuleProductNumber_Object=MibTableColumn
arubaWiredModuleProductNumber=_ArubaWiredModuleProductNumber_Object((1,3,6,1,4,1,47196,4,1,1,3,11,6,1,1,9),_ArubaWiredModuleProductNumber_Type())
arubaWiredModuleProductNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:arubaWiredModuleProductNumber.setStatus(_B)
class _ArubaWiredModuleAdminState_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_ArubaWiredModuleAdminState_Type.__name__=_C
_ArubaWiredModuleAdminState_Object=MibTableColumn
arubaWiredModuleAdminState=_ArubaWiredModuleAdminState_Object((1,3,6,1,4,1,47196,4,1,1,3,11,6,1,1,10),_ArubaWiredModuleAdminState_Type())
arubaWiredModuleAdminState.setMaxAccess(_D)
if mibBuilder.loadTexts:arubaWiredModuleAdminState.setStatus(_B)
class _ArubaWiredModulePowerPriority_Type(Integer32):defaultValue=128;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,254))
_ArubaWiredModulePowerPriority_Type.__name__=_G
_ArubaWiredModulePowerPriority_Object=MibTableColumn
arubaWiredModulePowerPriority=_ArubaWiredModulePowerPriority_Object((1,3,6,1,4,1,47196,4,1,1,3,11,6,1,1,11),_ArubaWiredModulePowerPriority_Type())
arubaWiredModulePowerPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:arubaWiredModulePowerPriority.setStatus(_B)
if mibBuilder.loadTexts:arubaWiredModulePowerPriority.setUnits('None')
class _ArubaWiredModuleUnrecognizedDescriptor_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,40))
_ArubaWiredModuleUnrecognizedDescriptor_Type.__name__=_C
_ArubaWiredModuleUnrecognizedDescriptor_Object=MibTableColumn
arubaWiredModuleUnrecognizedDescriptor=_ArubaWiredModuleUnrecognizedDescriptor_Object((1,3,6,1,4,1,47196,4,1,1,3,11,6,1,1,12),_ArubaWiredModuleUnrecognizedDescriptor_Type())
arubaWiredModuleUnrecognizedDescriptor.setMaxAccess('accessible-for-notify')
if mibBuilder.loadTexts:arubaWiredModuleUnrecognizedDescriptor.setStatus(_B)
_ArubaWiredModuleConformance_ObjectIdentity=ObjectIdentity
arubaWiredModuleConformance=_ArubaWiredModuleConformance_ObjectIdentity((1,3,6,1,4,1,47196,4,1,1,3,11,6,99))
_ArubaWiredModuleCompliances_ObjectIdentity=ObjectIdentity
arubaWiredModuleCompliances=_ArubaWiredModuleCompliances_ObjectIdentity((1,3,6,1,4,1,47196,4,1,1,3,11,6,99,1))
_ArubaWiredModuleGroups_ObjectIdentity=ObjectIdentity
arubaWiredModuleGroups=_ArubaWiredModuleGroups_ObjectIdentity((1,3,6,1,4,1,47196,4,1,1,3,11,6,99,2))
arubaWiredModuleTableGroup=ObjectGroup((1,3,6,1,4,1,47196,4,1,1,3,11,6,99,2,1))
arubaWiredModuleTableGroup.setObjects(*((_A,_E),(_A,_F),(_A,_I),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_J)))
if mibBuilder.loadTexts:arubaWiredModuleTableGroup.setStatus(_B)
arubaWiredModuleStateNotification=NotificationType((1,3,6,1,4,1,47196,4,1,1,3,11,6,0,1))
arubaWiredModuleStateNotification.setObjects(*((_A,_F),(_A,_E),(_A,_I)))
if mibBuilder.loadTexts:arubaWiredModuleStateNotification.setStatus(_B)
arubaWiredModuleInsertedNotification=NotificationType((1,3,6,1,4,1,47196,4,1,1,3,11,6,0,2))
arubaWiredModuleInsertedNotification.setObjects(*((_A,_F),(_A,_E)))
if mibBuilder.loadTexts:arubaWiredModuleInsertedNotification.setStatus(_B)
arubaWiredModuleRemovedNotification=NotificationType((1,3,6,1,4,1,47196,4,1,1,3,11,6,0,3))
arubaWiredModuleRemovedNotification.setObjects(*((_A,_F),(_A,_E)))
if mibBuilder.loadTexts:arubaWiredModuleRemovedNotification.setStatus(_B)
arubaWiredModuleUnrecognizedNotification=NotificationType((1,3,6,1,4,1,47196,4,1,1,3,11,6,0,4))
arubaWiredModuleUnrecognizedNotification.setObjects(*((_A,_F),(_A,_E),(_A,_J)))
if mibBuilder.loadTexts:arubaWiredModuleUnrecognizedNotification.setStatus(_B)
arubaWiredModuleNotificationsGroup=NotificationGroup((1,3,6,1,4,1,47196,4,1,1,3,11,6,99,2,2))
arubaWiredModuleNotificationsGroup.setObjects(*((_A,_S),(_A,_T),(_A,_U),(_A,_V)))
if mibBuilder.loadTexts:arubaWiredModuleNotificationsGroup.setStatus(_B)
arubaWiredModuleCompliance=ModuleCompliance((1,3,6,1,4,1,47196,4,1,1,3,11,6,99,1,1))
arubaWiredModuleCompliance.setObjects(*((_A,_W),(_A,_X),(_A,_Y)))
if mibBuilder.loadTexts:arubaWiredModuleCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'arubaWiredModule':arubaWiredModule,'arubaWiredModuleNotifications':arubaWiredModuleNotifications,_S:arubaWiredModuleStateNotification,_T:arubaWiredModuleInsertedNotification,_U:arubaWiredModuleRemovedNotification,_V:arubaWiredModuleUnrecognizedNotification,_W:arubaWiredModuleTable,'arubaWiredModuleEntry':arubaWiredModuleEntry,_K:arubaWiredModuleGroupIndex,_L:arubaWiredModuleTypeIndex,_M:arubaWiredModuleSlotIndex,_E:arubaWiredModuleName,_F:arubaWiredModuleType,_I:arubaWiredModuleState,_N:arubaWiredModuleProductDescription,_O:arubaWiredModuleSerialNumber,_P:arubaWiredModuleProductNumber,_Q:arubaWiredModuleAdminState,_R:arubaWiredModulePowerPriority,_J:arubaWiredModuleUnrecognizedDescriptor,'arubaWiredModuleConformance':arubaWiredModuleConformance,'arubaWiredModuleCompliances':arubaWiredModuleCompliances,'arubaWiredModuleCompliance':arubaWiredModuleCompliance,'arubaWiredModuleGroups':arubaWiredModuleGroups,_Y:arubaWiredModuleTableGroup,_X:arubaWiredModuleNotificationsGroup})