_R='arubaWiredFanTrayTableGroup'
_Q='arubaWiredFanTrayNotificationsGroup'
_P='arubaWiredFanTrayTable'
_O='arubaWiredFanTrayStateNotification'
_N='arubaWiredFanTrayStateEnum'
_M='arubaWiredFanTrayNumberFans'
_L='arubaWiredFanTraySerialNumber'
_K='arubaWiredFanTrayProductName'
_J='not-accessible'
_I='arubaWiredFanTraySlotIndex'
_H='arubaWiredFanTrayGroupIndex'
_G='arubaWiredFanTrayState'
_F='arubaWiredFanTrayName'
_E='DisplayString'
_D='Integer32'
_C='read-only'
_B='current'
_A='ARUBAWIRED-FANTRAY-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
arubaWiredChassisMIB,=mibBuilder.importSymbols('ARUBAWIRED-CHASSIS-MIB','arubaWiredChassisMIB')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_E,'PhysAddress','TextualConvention')
arubaWiredFanTray=ModuleIdentity((1,3,6,1,4,1,47196,4,1,1,3,11,4))
if mibBuilder.loadTexts:arubaWiredFanTray.setRevisions(('2023-03-31 00:00','2020-02-13 00:00'))
_ArubaWiredFanTrayNotifications_ObjectIdentity=ObjectIdentity
arubaWiredFanTrayNotifications=_ArubaWiredFanTrayNotifications_ObjectIdentity((1,3,6,1,4,1,47196,4,1,1,3,11,4,0))
_ArubaWiredFanTrayTable_Object=MibTable
arubaWiredFanTrayTable=_ArubaWiredFanTrayTable_Object((1,3,6,1,4,1,47196,4,1,1,3,11,4,1))
if mibBuilder.loadTexts:arubaWiredFanTrayTable.setStatus(_B)
_ArubaWiredFanTrayEntry_Object=MibTableRow
arubaWiredFanTrayEntry=_ArubaWiredFanTrayEntry_Object((1,3,6,1,4,1,47196,4,1,1,3,11,4,1,1))
arubaWiredFanTrayEntry.setIndexNames((0,_A,_H),(0,_A,_I))
if mibBuilder.loadTexts:arubaWiredFanTrayEntry.setStatus(_B)
class _ArubaWiredFanTrayGroupIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_ArubaWiredFanTrayGroupIndex_Type.__name__=_D
_ArubaWiredFanTrayGroupIndex_Object=MibTableColumn
arubaWiredFanTrayGroupIndex=_ArubaWiredFanTrayGroupIndex_Object((1,3,6,1,4,1,47196,4,1,1,3,11,4,1,1,1),_ArubaWiredFanTrayGroupIndex_Type())
arubaWiredFanTrayGroupIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:arubaWiredFanTrayGroupIndex.setStatus(_B)
class _ArubaWiredFanTraySlotIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_ArubaWiredFanTraySlotIndex_Type.__name__=_D
_ArubaWiredFanTraySlotIndex_Object=MibTableColumn
arubaWiredFanTraySlotIndex=_ArubaWiredFanTraySlotIndex_Object((1,3,6,1,4,1,47196,4,1,1,3,11,4,1,1,2),_ArubaWiredFanTraySlotIndex_Type())
arubaWiredFanTraySlotIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:arubaWiredFanTraySlotIndex.setStatus(_B)
class _ArubaWiredFanTrayName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_ArubaWiredFanTrayName_Type.__name__=_E
_ArubaWiredFanTrayName_Object=MibTableColumn
arubaWiredFanTrayName=_ArubaWiredFanTrayName_Object((1,3,6,1,4,1,47196,4,1,1,3,11,4,1,1,3),_ArubaWiredFanTrayName_Type())
arubaWiredFanTrayName.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredFanTrayName.setStatus(_B)
class _ArubaWiredFanTrayState_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_ArubaWiredFanTrayState_Type.__name__=_E
_ArubaWiredFanTrayState_Object=MibTableColumn
arubaWiredFanTrayState=_ArubaWiredFanTrayState_Object((1,3,6,1,4,1,47196,4,1,1,3,11,4,1,1,4),_ArubaWiredFanTrayState_Type())
arubaWiredFanTrayState.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredFanTrayState.setStatus(_B)
class _ArubaWiredFanTrayProductName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,30))
_ArubaWiredFanTrayProductName_Type.__name__=_E
_ArubaWiredFanTrayProductName_Object=MibTableColumn
arubaWiredFanTrayProductName=_ArubaWiredFanTrayProductName_Object((1,3,6,1,4,1,47196,4,1,1,3,11,4,1,1,5),_ArubaWiredFanTrayProductName_Type())
arubaWiredFanTrayProductName.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredFanTrayProductName.setStatus(_B)
class _ArubaWiredFanTraySerialNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_ArubaWiredFanTraySerialNumber_Type.__name__=_E
_ArubaWiredFanTraySerialNumber_Object=MibTableColumn
arubaWiredFanTraySerialNumber=_ArubaWiredFanTraySerialNumber_Object((1,3,6,1,4,1,47196,4,1,1,3,11,4,1,1,6),_ArubaWiredFanTraySerialNumber_Type())
arubaWiredFanTraySerialNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredFanTraySerialNumber.setStatus(_B)
class _ArubaWiredFanTrayNumberFans_Type(Integer32):defaultValue=0
_ArubaWiredFanTrayNumberFans_Type.__name__=_D
_ArubaWiredFanTrayNumberFans_Object=MibTableColumn
arubaWiredFanTrayNumberFans=_ArubaWiredFanTrayNumberFans_Object((1,3,6,1,4,1,47196,4,1,1,3,11,4,1,1,7),_ArubaWiredFanTrayNumberFans_Type())
arubaWiredFanTrayNumberFans.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredFanTrayNumberFans.setStatus(_B)
class _ArubaWiredFanTrayStateEnum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('unknown',1),('empty',2),('initializing',3),('ready',4),('down',5),('unsupported',6)))
_ArubaWiredFanTrayStateEnum_Type.__name__=_D
_ArubaWiredFanTrayStateEnum_Object=MibTableColumn
arubaWiredFanTrayStateEnum=_ArubaWiredFanTrayStateEnum_Object((1,3,6,1,4,1,47196,4,1,1,3,11,4,1,1,8),_ArubaWiredFanTrayStateEnum_Type())
arubaWiredFanTrayStateEnum.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredFanTrayStateEnum.setStatus(_B)
_ArubaWiredFanTrayConformance_ObjectIdentity=ObjectIdentity
arubaWiredFanTrayConformance=_ArubaWiredFanTrayConformance_ObjectIdentity((1,3,6,1,4,1,47196,4,1,1,3,11,4,99))
_ArubaWiredFanTrayCompliances_ObjectIdentity=ObjectIdentity
arubaWiredFanTrayCompliances=_ArubaWiredFanTrayCompliances_ObjectIdentity((1,3,6,1,4,1,47196,4,1,1,3,11,4,99,1))
_ArubaWiredFanTrayGroups_ObjectIdentity=ObjectIdentity
arubaWiredFanTrayGroups=_ArubaWiredFanTrayGroups_ObjectIdentity((1,3,6,1,4,1,47196,4,1,1,3,11,4,99,2))
arubaWiredFanTrayTableGroup=ObjectGroup((1,3,6,1,4,1,47196,4,1,1,3,11,4,99,2,1))
arubaWiredFanTrayTableGroup.setObjects(*((_A,_F),(_A,_G),(_A,_K),(_A,_L),(_A,_M),(_A,_N)))
if mibBuilder.loadTexts:arubaWiredFanTrayTableGroup.setStatus(_B)
arubaWiredFanTrayStateNotification=NotificationType((1,3,6,1,4,1,47196,4,1,1,3,11,4,0,1))
arubaWiredFanTrayStateNotification.setObjects(*((_A,_F),(_A,_G)))
if mibBuilder.loadTexts:arubaWiredFanTrayStateNotification.setStatus(_B)
arubaWiredFanTrayNotificationsGroup=NotificationGroup((1,3,6,1,4,1,47196,4,1,1,3,11,4,99,2,2))
arubaWiredFanTrayNotificationsGroup.setObjects((_A,_O))
if mibBuilder.loadTexts:arubaWiredFanTrayNotificationsGroup.setStatus(_B)
arubaWiredFanTrayCompliance=ModuleCompliance((1,3,6,1,4,1,47196,4,1,1,3,11,4,99,1,1))
arubaWiredFanTrayCompliance.setObjects(*((_A,_P),(_A,_Q),(_A,_R)))
if mibBuilder.loadTexts:arubaWiredFanTrayCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'arubaWiredFanTray':arubaWiredFanTray,'arubaWiredFanTrayNotifications':arubaWiredFanTrayNotifications,_O:arubaWiredFanTrayStateNotification,_P:arubaWiredFanTrayTable,'arubaWiredFanTrayEntry':arubaWiredFanTrayEntry,_H:arubaWiredFanTrayGroupIndex,_I:arubaWiredFanTraySlotIndex,_F:arubaWiredFanTrayName,_G:arubaWiredFanTrayState,_K:arubaWiredFanTrayProductName,_L:arubaWiredFanTraySerialNumber,_M:arubaWiredFanTrayNumberFans,_N:arubaWiredFanTrayStateEnum,'arubaWiredFanTrayConformance':arubaWiredFanTrayConformance,'arubaWiredFanTrayCompliances':arubaWiredFanTrayCompliances,'arubaWiredFanTrayCompliance':arubaWiredFanTrayCompliance,'arubaWiredFanTrayGroups':arubaWiredFanTrayGroups,_R:arubaWiredFanTrayTableGroup,_Q:arubaWiredFanTrayNotificationsGroup})