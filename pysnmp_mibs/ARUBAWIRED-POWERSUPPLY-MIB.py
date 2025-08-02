_T='arubaWiredPowerSupplyTableGroup'
_S='arubaWiredPSUNotificationsGroup'
_R='arubaWiredPowerSupplyTable'
_Q='arubaWiredPSUStateNotification'
_P='arubaWiredPSUStateEnum'
_O='arubaWiredPSUAirflowDirection'
_N='arubaWiredPSUNumberFailures'
_M='arubaWiredPSUMaximumPower'
_L='arubaWiredPSUInstantaneousPower'
_K='arubaWiredPSUSerialNumber'
_J='arubaWiredPSUProductName'
_I='arubaWiredPSUName'
_H='arubaWiredPSUState'
_G='arubaWiredPSUSlotIndex'
_F='arubaWiredPSUGroupIndex'
_E='DisplayString'
_D='Integer32'
_C='read-only'
_B='current'
_A='ARUBAWIRED-POWERSUPPLY-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
arubaWiredChassisMIB,=mibBuilder.importSymbols('ARUBAWIRED-CHASSIS-MIB','arubaWiredChassisMIB')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_E,'PhysAddress','TextualConvention')
arubaWiredPowerSupply=ModuleIdentity((1,3,6,1,4,1,47196,4,1,1,3,11,2))
if mibBuilder.loadTexts:arubaWiredPowerSupply.setRevisions(('2023-05-09 00:00','2023-03-28 00:00','2020-01-07 00:00'))
_ArubaWiredPSUNotifications_ObjectIdentity=ObjectIdentity
arubaWiredPSUNotifications=_ArubaWiredPSUNotifications_ObjectIdentity((1,3,6,1,4,1,47196,4,1,1,3,11,2,0))
_ArubaWiredPowerSupplyTable_Object=MibTable
arubaWiredPowerSupplyTable=_ArubaWiredPowerSupplyTable_Object((1,3,6,1,4,1,47196,4,1,1,3,11,2,1))
if mibBuilder.loadTexts:arubaWiredPowerSupplyTable.setStatus(_B)
_ArubaWiredPowerSupplyEntry_Object=MibTableRow
arubaWiredPowerSupplyEntry=_ArubaWiredPowerSupplyEntry_Object((1,3,6,1,4,1,47196,4,1,1,3,11,2,1,1))
arubaWiredPowerSupplyEntry.setIndexNames((0,_A,_F),(0,_A,_G))
if mibBuilder.loadTexts:arubaWiredPowerSupplyEntry.setStatus(_B)
class _ArubaWiredPSUGroupIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_ArubaWiredPSUGroupIndex_Type.__name__=_D
_ArubaWiredPSUGroupIndex_Object=MibTableColumn
arubaWiredPSUGroupIndex=_ArubaWiredPSUGroupIndex_Object((1,3,6,1,4,1,47196,4,1,1,3,11,2,1,1,1),_ArubaWiredPSUGroupIndex_Type())
arubaWiredPSUGroupIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredPSUGroupIndex.setStatus(_B)
class _ArubaWiredPSUSlotIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_ArubaWiredPSUSlotIndex_Type.__name__=_D
_ArubaWiredPSUSlotIndex_Object=MibTableColumn
arubaWiredPSUSlotIndex=_ArubaWiredPSUSlotIndex_Object((1,3,6,1,4,1,47196,4,1,1,3,11,2,1,1,2),_ArubaWiredPSUSlotIndex_Type())
arubaWiredPSUSlotIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredPSUSlotIndex.setStatus(_B)
class _ArubaWiredPSUName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_ArubaWiredPSUName_Type.__name__=_E
_ArubaWiredPSUName_Object=MibTableColumn
arubaWiredPSUName=_ArubaWiredPSUName_Object((1,3,6,1,4,1,47196,4,1,1,3,11,2,1,1,3),_ArubaWiredPSUName_Type())
arubaWiredPSUName.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredPSUName.setStatus(_B)
class _ArubaWiredPSUState_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_ArubaWiredPSUState_Type.__name__=_E
_ArubaWiredPSUState_Object=MibTableColumn
arubaWiredPSUState=_ArubaWiredPSUState_Object((1,3,6,1,4,1,47196,4,1,1,3,11,2,1,1,4),_ArubaWiredPSUState_Type())
arubaWiredPSUState.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredPSUState.setStatus(_B)
class _ArubaWiredPSUProductName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_ArubaWiredPSUProductName_Type.__name__=_E
_ArubaWiredPSUProductName_Object=MibTableColumn
arubaWiredPSUProductName=_ArubaWiredPSUProductName_Object((1,3,6,1,4,1,47196,4,1,1,3,11,2,1,1,5),_ArubaWiredPSUProductName_Type())
arubaWiredPSUProductName.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredPSUProductName.setStatus(_B)
class _ArubaWiredPSUSerialNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_ArubaWiredPSUSerialNumber_Type.__name__=_E
_ArubaWiredPSUSerialNumber_Object=MibTableColumn
arubaWiredPSUSerialNumber=_ArubaWiredPSUSerialNumber_Object((1,3,6,1,4,1,47196,4,1,1,3,11,2,1,1,6),_ArubaWiredPSUSerialNumber_Type())
arubaWiredPSUSerialNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredPSUSerialNumber.setStatus(_B)
class _ArubaWiredPSUInstantaneousPower_Type(Integer32):defaultValue=0
_ArubaWiredPSUInstantaneousPower_Type.__name__=_D
_ArubaWiredPSUInstantaneousPower_Object=MibTableColumn
arubaWiredPSUInstantaneousPower=_ArubaWiredPSUInstantaneousPower_Object((1,3,6,1,4,1,47196,4,1,1,3,11,2,1,1,7),_ArubaWiredPSUInstantaneousPower_Type())
arubaWiredPSUInstantaneousPower.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredPSUInstantaneousPower.setStatus(_B)
if mibBuilder.loadTexts:arubaWiredPSUInstantaneousPower.setUnits('Watts')
class _ArubaWiredPSUMaximumPower_Type(Integer32):defaultValue=0
_ArubaWiredPSUMaximumPower_Type.__name__=_D
_ArubaWiredPSUMaximumPower_Object=MibTableColumn
arubaWiredPSUMaximumPower=_ArubaWiredPSUMaximumPower_Object((1,3,6,1,4,1,47196,4,1,1,3,11,2,1,1,8),_ArubaWiredPSUMaximumPower_Type())
arubaWiredPSUMaximumPower.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredPSUMaximumPower.setStatus(_B)
if mibBuilder.loadTexts:arubaWiredPSUMaximumPower.setUnits('Watts')
class _ArubaWiredPSUNumberFailures_Type(Integer32):defaultValue=0
_ArubaWiredPSUNumberFailures_Type.__name__=_D
_ArubaWiredPSUNumberFailures_Object=MibTableColumn
arubaWiredPSUNumberFailures=_ArubaWiredPSUNumberFailures_Object((1,3,6,1,4,1,47196,4,1,1,3,11,2,1,1,9),_ArubaWiredPSUNumberFailures_Type())
arubaWiredPSUNumberFailures.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredPSUNumberFailures.setStatus(_B)
class _ArubaWiredPSUAirflowDirection_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_ArubaWiredPSUAirflowDirection_Type.__name__=_E
_ArubaWiredPSUAirflowDirection_Object=MibTableColumn
arubaWiredPSUAirflowDirection=_ArubaWiredPSUAirflowDirection_Object((1,3,6,1,4,1,47196,4,1,1,3,11,2,1,1,10),_ArubaWiredPSUAirflowDirection_Type())
arubaWiredPSUAirflowDirection.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredPSUAirflowDirection.setStatus(_B)
class _ArubaWiredPSUStateEnum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14)));namedValues=NamedValues(*(('ok',1),('faultAbsent',2),('faultInput',3),('faultOutput',4),('faultPOE',5),('faultNoRecov',6),('alert',7),('unknown',8),('unsupported',9),('warning',10),('init',11),('empty',12),('faultAirflow',13),('faultRedundancy',14)))
_ArubaWiredPSUStateEnum_Type.__name__=_D
_ArubaWiredPSUStateEnum_Object=MibTableColumn
arubaWiredPSUStateEnum=_ArubaWiredPSUStateEnum_Object((1,3,6,1,4,1,47196,4,1,1,3,11,2,1,1,11),_ArubaWiredPSUStateEnum_Type())
arubaWiredPSUStateEnum.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredPSUStateEnum.setStatus(_B)
_ArubaWiredPowerSupplyConformance_ObjectIdentity=ObjectIdentity
arubaWiredPowerSupplyConformance=_ArubaWiredPowerSupplyConformance_ObjectIdentity((1,3,6,1,4,1,47196,4,1,1,3,11,2,99))
_ArubaWiredPowerSupplyCompliances_ObjectIdentity=ObjectIdentity
arubaWiredPowerSupplyCompliances=_ArubaWiredPowerSupplyCompliances_ObjectIdentity((1,3,6,1,4,1,47196,4,1,1,3,11,2,99,1))
_ArubaWiredPowerSupplyGroups_ObjectIdentity=ObjectIdentity
arubaWiredPowerSupplyGroups=_ArubaWiredPowerSupplyGroups_ObjectIdentity((1,3,6,1,4,1,47196,4,1,1,3,11,2,99,2))
arubaWiredPowerSupplyTableGroup=ObjectGroup((1,3,6,1,4,1,47196,4,1,1,3,11,2,99,2,1))
arubaWiredPowerSupplyTableGroup.setObjects(*((_A,_F),(_A,_G),(_A,_I),(_A,_H),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P)))
if mibBuilder.loadTexts:arubaWiredPowerSupplyTableGroup.setStatus(_B)
arubaWiredPSUStateNotification=NotificationType((1,3,6,1,4,1,47196,4,1,1,3,11,2,0,1))
arubaWiredPSUStateNotification.setObjects(*((_A,_F),(_A,_G),(_A,_H)))
if mibBuilder.loadTexts:arubaWiredPSUStateNotification.setStatus(_B)
arubaWiredPSUNotificationsGroup=NotificationGroup((1,3,6,1,4,1,47196,4,1,1,3,11,2,99,2,2))
arubaWiredPSUNotificationsGroup.setObjects((_A,_Q))
if mibBuilder.loadTexts:arubaWiredPSUNotificationsGroup.setStatus(_B)
arubaWiredPowerSupplyCompliance=ModuleCompliance((1,3,6,1,4,1,47196,4,1,1,3,11,2,99,1,1))
arubaWiredPowerSupplyCompliance.setObjects(*((_A,_R),(_A,_S),(_A,_T)))
if mibBuilder.loadTexts:arubaWiredPowerSupplyCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'arubaWiredPowerSupply':arubaWiredPowerSupply,'arubaWiredPSUNotifications':arubaWiredPSUNotifications,_Q:arubaWiredPSUStateNotification,_R:arubaWiredPowerSupplyTable,'arubaWiredPowerSupplyEntry':arubaWiredPowerSupplyEntry,_F:arubaWiredPSUGroupIndex,_G:arubaWiredPSUSlotIndex,_I:arubaWiredPSUName,_H:arubaWiredPSUState,_J:arubaWiredPSUProductName,_K:arubaWiredPSUSerialNumber,_L:arubaWiredPSUInstantaneousPower,_M:arubaWiredPSUMaximumPower,_N:arubaWiredPSUNumberFailures,_O:arubaWiredPSUAirflowDirection,_P:arubaWiredPSUStateEnum,'arubaWiredPowerSupplyConformance':arubaWiredPowerSupplyConformance,'arubaWiredPowerSupplyCompliances':arubaWiredPowerSupplyCompliances,'arubaWiredPowerSupplyCompliance':arubaWiredPowerSupplyCompliance,'arubaWiredPowerSupplyGroups':arubaWiredPowerSupplyGroups,_T:arubaWiredPowerSupplyTableGroup,_S:arubaWiredPSUNotificationsGroup})