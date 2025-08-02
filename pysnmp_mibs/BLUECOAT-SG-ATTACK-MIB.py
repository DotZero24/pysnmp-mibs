_G='deviceAttackStatus'
_F='deviceAttackName'
_E='deviceAttackIndex'
_D='Integer32'
_C='read-only'
_B='BLUECOAT-SG-ATTACK-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
blueCoatMgmt,=mibBuilder.importSymbols('BLUECOAT-MIB','blueCoatMgmt')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TimeStamp=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TimeStamp')
deviceAttackMIB=ModuleIdentity((1,3,6,1,4,1,3417,2,3))
if mibBuilder.loadTexts:deviceAttackMIB.setRevisions(('2007-11-05 03:00','2002-11-06 03:00'))
class AttackStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('noAttack',1),('underAttack',2)))
_DeviceAttackMIBObjects_ObjectIdentity=ObjectIdentity
deviceAttackMIBObjects=_DeviceAttackMIBObjects_ObjectIdentity((1,3,6,1,4,1,3417,2,3,1))
_DeviceAttackValues_ObjectIdentity=ObjectIdentity
deviceAttackValues=_DeviceAttackValues_ObjectIdentity((1,3,6,1,4,1,3417,2,3,1,1))
_DeviceAttackTable_Object=MibTable
deviceAttackTable=_DeviceAttackTable_Object((1,3,6,1,4,1,3417,2,3,1,1,1))
if mibBuilder.loadTexts:deviceAttackTable.setStatus(_A)
_DeviceAttackEntry_Object=MibTableRow
deviceAttackEntry=_DeviceAttackEntry_Object((1,3,6,1,4,1,3417,2,3,1,1,1,1))
deviceAttackEntry.setIndexNames((0,_B,_E))
if mibBuilder.loadTexts:deviceAttackEntry.setStatus(_A)
class _DeviceAttackIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_DeviceAttackIndex_Type.__name__=_D
_DeviceAttackIndex_Object=MibTableColumn
deviceAttackIndex=_DeviceAttackIndex_Object((1,3,6,1,4,1,3417,2,3,1,1,1,1,1),_DeviceAttackIndex_Type())
deviceAttackIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:deviceAttackIndex.setStatus(_A)
_DeviceAttackName_Type=DisplayString
_DeviceAttackName_Object=MibTableColumn
deviceAttackName=_DeviceAttackName_Object((1,3,6,1,4,1,3417,2,3,1,1,1,1,2),_DeviceAttackName_Type())
deviceAttackName.setMaxAccess(_C)
if mibBuilder.loadTexts:deviceAttackName.setStatus(_A)
_DeviceAttackStatus_Type=AttackStatus
_DeviceAttackStatus_Object=MibTableColumn
deviceAttackStatus=_DeviceAttackStatus_Object((1,3,6,1,4,1,3417,2,3,1,1,1,1,3),_DeviceAttackStatus_Type())
deviceAttackStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:deviceAttackStatus.setStatus(_A)
_DeviceAttackTime_Type=TimeStamp
_DeviceAttackTime_Object=MibTableColumn
deviceAttackTime=_DeviceAttackTime_Object((1,3,6,1,4,1,3417,2,3,1,1,1,1,4),_DeviceAttackTime_Type())
deviceAttackTime.setMaxAccess(_C)
if mibBuilder.loadTexts:deviceAttackTime.setStatus(_A)
if mibBuilder.loadTexts:deviceAttackTime.setUnits('Hundredths of seconds')
_DeviceAttackMIBNotifications_ObjectIdentity=ObjectIdentity
deviceAttackMIBNotifications=_DeviceAttackMIBNotifications_ObjectIdentity((1,3,6,1,4,1,3417,2,3,2))
_DeviceAttackMIBNotificationsPrefix_ObjectIdentity=ObjectIdentity
deviceAttackMIBNotificationsPrefix=_DeviceAttackMIBNotificationsPrefix_ObjectIdentity((1,3,6,1,4,1,3417,2,3,2,0))
deviceAttackTrap=NotificationType((1,3,6,1,4,1,3417,2,3,2,0,1))
deviceAttackTrap.setObjects(*((_B,_F),(_B,_G)))
if mibBuilder.loadTexts:deviceAttackTrap.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'AttackStatus':AttackStatus,'deviceAttackMIB':deviceAttackMIB,'deviceAttackMIBObjects':deviceAttackMIBObjects,'deviceAttackValues':deviceAttackValues,'deviceAttackTable':deviceAttackTable,'deviceAttackEntry':deviceAttackEntry,_E:deviceAttackIndex,_F:deviceAttackName,_G:deviceAttackStatus,'deviceAttackTime':deviceAttackTime,'deviceAttackMIBNotifications':deviceAttackMIBNotifications,'deviceAttackMIBNotificationsPrefix':deviceAttackMIBNotificationsPrefix,'deviceAttackTrap':deviceAttackTrap})