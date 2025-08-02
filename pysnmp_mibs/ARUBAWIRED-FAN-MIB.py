_T='arubaWiredFanTableGroup'
_S='arubaWiredFanNotificationsGroup'
_R='arubaWiredFanTable'
_Q='arubaWiredFanStateNotification'
_P='arubaWiredFanStateEnum'
_O='arubaWiredFanAirflowDirection'
_N='arubaWiredFanRPM'
_M='arubaWiredFanSerialNumber'
_L='arubaWiredFanProductName'
_K='arubaWiredFanSlotIndex'
_J='arubaWiredFanTrayIndex'
_I='arubaWiredFanGroupIndex'
_H='arubaWiredFanState'
_G='arubaWiredFanName'
_F='not-accessible'
_E='Integer32'
_D='DisplayString'
_C='read-only'
_B='current'
_A='ARUBAWIRED-FAN-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
arubaWiredChassisMIB,=mibBuilder.importSymbols('ARUBAWIRED-CHASSIS-MIB','arubaWiredChassisMIB')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_D,'PhysAddress','TextualConvention')
arubaWiredFan=ModuleIdentity((1,3,6,1,4,1,47196,4,1,1,3,11,5))
if mibBuilder.loadTexts:arubaWiredFan.setRevisions(('2023-03-31 00:00','2020-02-13 00:00'))
_ArubaWiredFanNotifications_ObjectIdentity=ObjectIdentity
arubaWiredFanNotifications=_ArubaWiredFanNotifications_ObjectIdentity((1,3,6,1,4,1,47196,4,1,1,3,11,5,0))
_ArubaWiredFanTable_Object=MibTable
arubaWiredFanTable=_ArubaWiredFanTable_Object((1,3,6,1,4,1,47196,4,1,1,3,11,5,1))
if mibBuilder.loadTexts:arubaWiredFanTable.setStatus(_B)
_ArubaWiredFanEntry_Object=MibTableRow
arubaWiredFanEntry=_ArubaWiredFanEntry_Object((1,3,6,1,4,1,47196,4,1,1,3,11,5,1,1))
arubaWiredFanEntry.setIndexNames((0,_A,_I),(0,_A,_J),(0,_A,_K))
if mibBuilder.loadTexts:arubaWiredFanEntry.setStatus(_B)
class _ArubaWiredFanGroupIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_ArubaWiredFanGroupIndex_Type.__name__=_E
_ArubaWiredFanGroupIndex_Object=MibTableColumn
arubaWiredFanGroupIndex=_ArubaWiredFanGroupIndex_Object((1,3,6,1,4,1,47196,4,1,1,3,11,5,1,1,1),_ArubaWiredFanGroupIndex_Type())
arubaWiredFanGroupIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:arubaWiredFanGroupIndex.setStatus(_B)
class _ArubaWiredFanTrayIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_ArubaWiredFanTrayIndex_Type.__name__=_E
_ArubaWiredFanTrayIndex_Object=MibTableColumn
arubaWiredFanTrayIndex=_ArubaWiredFanTrayIndex_Object((1,3,6,1,4,1,47196,4,1,1,3,11,5,1,1,2),_ArubaWiredFanTrayIndex_Type())
arubaWiredFanTrayIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:arubaWiredFanTrayIndex.setStatus(_B)
class _ArubaWiredFanSlotIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_ArubaWiredFanSlotIndex_Type.__name__=_E
_ArubaWiredFanSlotIndex_Object=MibTableColumn
arubaWiredFanSlotIndex=_ArubaWiredFanSlotIndex_Object((1,3,6,1,4,1,47196,4,1,1,3,11,5,1,1,3),_ArubaWiredFanSlotIndex_Type())
arubaWiredFanSlotIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:arubaWiredFanSlotIndex.setStatus(_B)
class _ArubaWiredFanName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_ArubaWiredFanName_Type.__name__=_D
_ArubaWiredFanName_Object=MibTableColumn
arubaWiredFanName=_ArubaWiredFanName_Object((1,3,6,1,4,1,47196,4,1,1,3,11,5,1,1,4),_ArubaWiredFanName_Type())
arubaWiredFanName.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredFanName.setStatus(_B)
class _ArubaWiredFanState_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_ArubaWiredFanState_Type.__name__=_D
_ArubaWiredFanState_Object=MibTableColumn
arubaWiredFanState=_ArubaWiredFanState_Object((1,3,6,1,4,1,47196,4,1,1,3,11,5,1,1,5),_ArubaWiredFanState_Type())
arubaWiredFanState.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredFanState.setStatus(_B)
class _ArubaWiredFanProductName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_ArubaWiredFanProductName_Type.__name__=_D
_ArubaWiredFanProductName_Object=MibTableColumn
arubaWiredFanProductName=_ArubaWiredFanProductName_Object((1,3,6,1,4,1,47196,4,1,1,3,11,5,1,1,6),_ArubaWiredFanProductName_Type())
arubaWiredFanProductName.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredFanProductName.setStatus(_B)
class _ArubaWiredFanSerialNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_ArubaWiredFanSerialNumber_Type.__name__=_D
_ArubaWiredFanSerialNumber_Object=MibTableColumn
arubaWiredFanSerialNumber=_ArubaWiredFanSerialNumber_Object((1,3,6,1,4,1,47196,4,1,1,3,11,5,1,1,7),_ArubaWiredFanSerialNumber_Type())
arubaWiredFanSerialNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredFanSerialNumber.setStatus(_B)
_ArubaWiredFanRPM_Type=Integer32
_ArubaWiredFanRPM_Object=MibTableColumn
arubaWiredFanRPM=_ArubaWiredFanRPM_Object((1,3,6,1,4,1,47196,4,1,1,3,11,5,1,1,8),_ArubaWiredFanRPM_Type())
arubaWiredFanRPM.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredFanRPM.setStatus(_B)
if mibBuilder.loadTexts:arubaWiredFanRPM.setUnits('RPM')
class _ArubaWiredFanAirflowDirection_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_ArubaWiredFanAirflowDirection_Type.__name__=_D
_ArubaWiredFanAirflowDirection_Object=MibTableColumn
arubaWiredFanAirflowDirection=_ArubaWiredFanAirflowDirection_Object((1,3,6,1,4,1,47196,4,1,1,3,11,5,1,1,9),_ArubaWiredFanAirflowDirection_Type())
arubaWiredFanAirflowDirection.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredFanAirflowDirection.setStatus(_B)
class _ArubaWiredFanStateEnum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('unknown',1),('empty',2),('uninitialized',3),('ok',4),('fault',5)))
_ArubaWiredFanStateEnum_Type.__name__=_E
_ArubaWiredFanStateEnum_Object=MibTableColumn
arubaWiredFanStateEnum=_ArubaWiredFanStateEnum_Object((1,3,6,1,4,1,47196,4,1,1,3,11,5,1,1,10),_ArubaWiredFanStateEnum_Type())
arubaWiredFanStateEnum.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredFanStateEnum.setStatus(_B)
_ArubaWiredFanConformance_ObjectIdentity=ObjectIdentity
arubaWiredFanConformance=_ArubaWiredFanConformance_ObjectIdentity((1,3,6,1,4,1,47196,4,1,1,3,11,5,99))
_ArubaWiredFanCompliances_ObjectIdentity=ObjectIdentity
arubaWiredFanCompliances=_ArubaWiredFanCompliances_ObjectIdentity((1,3,6,1,4,1,47196,4,1,1,3,11,5,99,1))
_ArubaWiredFanGroups_ObjectIdentity=ObjectIdentity
arubaWiredFanGroups=_ArubaWiredFanGroups_ObjectIdentity((1,3,6,1,4,1,47196,4,1,1,3,11,5,99,2))
arubaWiredFanTableGroup=ObjectGroup((1,3,6,1,4,1,47196,4,1,1,3,11,5,99,2,1))
arubaWiredFanTableGroup.setObjects(*((_A,_G),(_A,_H),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P)))
if mibBuilder.loadTexts:arubaWiredFanTableGroup.setStatus(_B)
arubaWiredFanStateNotification=NotificationType((1,3,6,1,4,1,47196,4,1,1,3,11,5,0,1))
arubaWiredFanStateNotification.setObjects(*((_A,_G),(_A,_H)))
if mibBuilder.loadTexts:arubaWiredFanStateNotification.setStatus(_B)
arubaWiredFanNotificationsGroup=NotificationGroup((1,3,6,1,4,1,47196,4,1,1,3,11,5,99,2,2))
arubaWiredFanNotificationsGroup.setObjects((_A,_Q))
if mibBuilder.loadTexts:arubaWiredFanNotificationsGroup.setStatus(_B)
arubaWiredFanCompliance=ModuleCompliance((1,3,6,1,4,1,47196,4,1,1,3,11,5,99,1,1))
arubaWiredFanCompliance.setObjects(*((_A,_R),(_A,_S),(_A,_T)))
if mibBuilder.loadTexts:arubaWiredFanCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'arubaWiredFan':arubaWiredFan,'arubaWiredFanNotifications':arubaWiredFanNotifications,_Q:arubaWiredFanStateNotification,_R:arubaWiredFanTable,'arubaWiredFanEntry':arubaWiredFanEntry,_I:arubaWiredFanGroupIndex,_J:arubaWiredFanTrayIndex,_K:arubaWiredFanSlotIndex,_G:arubaWiredFanName,_H:arubaWiredFanState,_L:arubaWiredFanProductName,_M:arubaWiredFanSerialNumber,_N:arubaWiredFanRPM,_O:arubaWiredFanAirflowDirection,_P:arubaWiredFanStateEnum,'arubaWiredFanConformance':arubaWiredFanConformance,'arubaWiredFanCompliances':arubaWiredFanCompliances,'arubaWiredFanCompliance':arubaWiredFanCompliance,'arubaWiredFanGroups':arubaWiredFanGroups,_T:arubaWiredFanTableGroup,_S:arubaWiredFanNotificationsGroup})