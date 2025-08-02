_K='eltexMnFlappingTime'
_J='eltexMnFlappingSecondPortId'
_I='eltexMnFlappingFirstPortId'
_H='eltexMnFlappingVlanNumber'
_G='eltexMnFlappingAddress'
_F='read-write'
_E='TruthValue'
_D='Integer32'
_C='read-only'
_B='ELTEX-MAC-NOTIFICATION-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
VlanIndex,=mibBuilder.importSymbols('CISCO-VTP-MIB','VlanIndex')
eltexLtd,=mibBuilder.importSymbols('ELTEX-SMI-ACTUAL','eltexLtd')
ifIndex,=mibBuilder.importSymbols('IF-MIB','ifIndex')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','TextualConvention','TimeStamp',_E)
eltexMacNotificationMIB=ModuleIdentity((1,3,6,1,4,1,35265,33))
if mibBuilder.loadTexts:eltexMacNotificationMIB.setRevisions(('2015-11-05 00:00',))
_EltexMacNotificationObjects_ObjectIdentity=ObjectIdentity
eltexMacNotificationObjects=_EltexMacNotificationObjects_ObjectIdentity((1,3,6,1,4,1,35265,33,1))
_EltexMnFlappingObjects_ObjectIdentity=ObjectIdentity
eltexMnFlappingObjects=_EltexMnFlappingObjects_ObjectIdentity((1,3,6,1,4,1,35265,33,1,1))
class _EltexMnFlappingFeatureEnabled_Type(TruthValue):defaultValue=1
_EltexMnFlappingFeatureEnabled_Type.__name__=_E
_EltexMnFlappingFeatureEnabled_Object=MibScalar
eltexMnFlappingFeatureEnabled=_EltexMnFlappingFeatureEnabled_Object((1,3,6,1,4,1,35265,33,1,1,1),_EltexMnFlappingFeatureEnabled_Type())
eltexMnFlappingFeatureEnabled.setMaxAccess(_F)
if mibBuilder.loadTexts:eltexMnFlappingFeatureEnabled.setStatus(_A)
class _EltexMnFlappingNotificationsEnabled_Type(TruthValue):defaultValue=1
_EltexMnFlappingNotificationsEnabled_Type.__name__=_E
_EltexMnFlappingNotificationsEnabled_Object=MibScalar
eltexMnFlappingNotificationsEnabled=_EltexMnFlappingNotificationsEnabled_Object((1,3,6,1,4,1,35265,33,1,1,2),_EltexMnFlappingNotificationsEnabled_Type())
eltexMnFlappingNotificationsEnabled.setMaxAccess(_F)
if mibBuilder.loadTexts:eltexMnFlappingNotificationsEnabled.setStatus(_A)
_EltexMnFlappingAddress_Type=MacAddress
_EltexMnFlappingAddress_Object=MibScalar
eltexMnFlappingAddress=_EltexMnFlappingAddress_Object((1,3,6,1,4,1,35265,33,1,1,3),_EltexMnFlappingAddress_Type())
eltexMnFlappingAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:eltexMnFlappingAddress.setStatus(_A)
_EltexMnFlappingVlanNumber_Type=VlanIndex
_EltexMnFlappingVlanNumber_Object=MibScalar
eltexMnFlappingVlanNumber=_EltexMnFlappingVlanNumber_Object((1,3,6,1,4,1,35265,33,1,1,4),_EltexMnFlappingVlanNumber_Type())
eltexMnFlappingVlanNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:eltexMnFlappingVlanNumber.setStatus(_A)
class _EltexMnFlappingFirstPortId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_EltexMnFlappingFirstPortId_Type.__name__=_D
_EltexMnFlappingFirstPortId_Object=MibScalar
eltexMnFlappingFirstPortId=_EltexMnFlappingFirstPortId_Object((1,3,6,1,4,1,35265,33,1,1,5),_EltexMnFlappingFirstPortId_Type())
eltexMnFlappingFirstPortId.setMaxAccess(_C)
if mibBuilder.loadTexts:eltexMnFlappingFirstPortId.setStatus(_A)
class _EltexMnFlappingSecondPortId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_EltexMnFlappingSecondPortId_Type.__name__=_D
_EltexMnFlappingSecondPortId_Object=MibScalar
eltexMnFlappingSecondPortId=_EltexMnFlappingSecondPortId_Object((1,3,6,1,4,1,35265,33,1,1,6),_EltexMnFlappingSecondPortId_Type())
eltexMnFlappingSecondPortId.setMaxAccess(_C)
if mibBuilder.loadTexts:eltexMnFlappingSecondPortId.setStatus(_A)
_EltexMnFlappingTime_Type=TimeStamp
_EltexMnFlappingTime_Object=MibScalar
eltexMnFlappingTime=_EltexMnFlappingTime_Object((1,3,6,1,4,1,35265,33,1,1,7),_EltexMnFlappingTime_Type())
eltexMnFlappingTime.setMaxAccess(_C)
if mibBuilder.loadTexts:eltexMnFlappingTime.setStatus(_A)
_EltexMnNotificationPrefix_ObjectIdentity=ObjectIdentity
eltexMnNotificationPrefix=_EltexMnNotificationPrefix_ObjectIdentity((1,3,6,1,4,1,35265,33,2))
_EltexMnNotifications_ObjectIdentity=ObjectIdentity
eltexMnNotifications=_EltexMnNotifications_ObjectIdentity((1,3,6,1,4,1,35265,33,2,0))
eltexMnFlappingNotification=NotificationType((1,3,6,1,4,1,35265,33,2,0,1))
eltexMnFlappingNotification.setObjects(*((_B,_G),(_B,_H),(_B,_I),(_B,_J),(_B,_K)))
if mibBuilder.loadTexts:eltexMnFlappingNotification.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'eltexMacNotificationMIB':eltexMacNotificationMIB,'eltexMacNotificationObjects':eltexMacNotificationObjects,'eltexMnFlappingObjects':eltexMnFlappingObjects,'eltexMnFlappingFeatureEnabled':eltexMnFlappingFeatureEnabled,'eltexMnFlappingNotificationsEnabled':eltexMnFlappingNotificationsEnabled,_G:eltexMnFlappingAddress,_H:eltexMnFlappingVlanNumber,_I:eltexMnFlappingFirstPortId,_J:eltexMnFlappingSecondPortId,_K:eltexMnFlappingTime,'eltexMnNotificationPrefix':eltexMnNotificationPrefix,'eltexMnNotifications':eltexMnNotifications,'eltexMnFlappingNotification':eltexMnFlappingNotification})