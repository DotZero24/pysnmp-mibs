_M='dellNetMacNotificationGroup'
_L='macMoveNotification'
_K='macLearnNotification'
_J='newPortId'
_I='message'
_H='timeStamp'
_G='portId'
_F='vlanId'
_E='macAddress'
_D='Integer32'
_C='accessible-for-notify'
_B='current'
_A='DELL-NETWORKING-MAC-NOTIFICATION-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dellNetMgmt,=mibBuilder.importSymbols('DELL-NETWORKING-SMI','dellNetMgmt')
ifIndex,=mibBuilder.importSymbols('IF-MIB','ifIndex')
VlanId,=mibBuilder.importSymbols('Q-BRIDGE-MIB','VlanId')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','TextualConvention')
dellNetMacNotifMib=ModuleIdentity((1,3,6,1,4,1,6027,3,28))
if mibBuilder.loadTexts:dellNetMacNotifMib.setRevisions(('2017-01-01 12:00',))
_DellNetMacNotificationObjects_ObjectIdentity=ObjectIdentity
dellNetMacNotificationObjects=_DellNetMacNotificationObjects_ObjectIdentity((1,3,6,1,4,1,6027,3,28,1))
_DellNetMacNotificationTraps_ObjectIdentity=ObjectIdentity
dellNetMacNotificationTraps=_DellNetMacNotificationTraps_ObjectIdentity((1,3,6,1,4,1,6027,3,28,1,1))
_MacAddress_Type=MacAddress
_MacAddress_Object=MibScalar
macAddress=_MacAddress_Object((1,3,6,1,4,1,6027,3,28,1,2),_MacAddress_Type())
macAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:macAddress.setStatus(_B)
_VlanId_Type=VlanId
_VlanId_Object=MibScalar
vlanId=_VlanId_Object((1,3,6,1,4,1,6027,3,28,1,3),_VlanId_Type())
vlanId.setMaxAccess(_C)
if mibBuilder.loadTexts:vlanId.setStatus(_B)
class _PortId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PortId_Type.__name__=_D
_PortId_Object=MibScalar
portId=_PortId_Object((1,3,6,1,4,1,6027,3,28,1,4),_PortId_Type())
portId.setMaxAccess(_C)
if mibBuilder.loadTexts:portId.setStatus(_B)
class _NewPortId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_NewPortId_Type.__name__=_D
_NewPortId_Object=MibScalar
newPortId=_NewPortId_Object((1,3,6,1,4,1,6027,3,28,1,5),_NewPortId_Type())
newPortId.setMaxAccess(_C)
if mibBuilder.loadTexts:newPortId.setStatus(_B)
_TimeStamp_Type=TimeTicks
_TimeStamp_Object=MibScalar
timeStamp=_TimeStamp_Object((1,3,6,1,4,1,6027,3,28,1,6),_TimeStamp_Type())
timeStamp.setMaxAccess(_C)
if mibBuilder.loadTexts:timeStamp.setStatus(_B)
_Message_Type=OctetString
_Message_Object=MibScalar
message=_Message_Object((1,3,6,1,4,1,6027,3,28,1,7),_Message_Type())
message.setMaxAccess(_C)
if mibBuilder.loadTexts:message.setStatus(_B)
_DellNetMacMibConformance_ObjectIdentity=ObjectIdentity
dellNetMacMibConformance=_DellNetMacMibConformance_ObjectIdentity((1,3,6,1,4,1,6027,3,28,2))
_DellNetMacMibCompliances_ObjectIdentity=ObjectIdentity
dellNetMacMibCompliances=_DellNetMacMibCompliances_ObjectIdentity((1,3,6,1,4,1,6027,3,28,2,1))
_DellNetMacMibGroups_ObjectIdentity=ObjectIdentity
dellNetMacMibGroups=_DellNetMacMibGroups_ObjectIdentity((1,3,6,1,4,1,6027,3,28,2,2))
macLearnNotification=NotificationType((1,3,6,1,4,1,6027,3,28,1,1,1))
macLearnNotification.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_H),(_A,_I)))
if mibBuilder.loadTexts:macLearnNotification.setStatus(_B)
macMoveNotification=NotificationType((1,3,6,1,4,1,6027,3,28,1,1,2))
macMoveNotification.setObjects(*((_A,_E),(_A,_F),(_A,_G),(_A,_J),(_A,_H),(_A,_I)))
if mibBuilder.loadTexts:macMoveNotification.setStatus(_B)
dellNetMacNotificationGroup=NotificationGroup((1,3,6,1,4,1,6027,3,28,2,2,1))
dellNetMacNotificationGroup.setObjects(*((_A,_K),(_A,_L)))
if mibBuilder.loadTexts:dellNetMacNotificationGroup.setStatus(_B)
dellNetMacMibCompliance=ModuleCompliance((1,3,6,1,4,1,6027,3,28,2,1,1))
dellNetMacMibCompliance.setObjects((_A,_M))
if mibBuilder.loadTexts:dellNetMacMibCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'dellNetMacNotifMib':dellNetMacNotifMib,'dellNetMacNotificationObjects':dellNetMacNotificationObjects,'dellNetMacNotificationTraps':dellNetMacNotificationTraps,_K:macLearnNotification,_L:macMoveNotification,_E:macAddress,_F:vlanId,_G:portId,_J:newPortId,_H:timeStamp,_I:message,'dellNetMacMibConformance':dellNetMacMibConformance,'dellNetMacMibCompliances':dellNetMacMibCompliances,'dellNetMacMibCompliance':dellNetMacMibCompliance,'dellNetMacMibGroups':dellNetMacMibGroups,_M:dellNetMacNotificationGroup})