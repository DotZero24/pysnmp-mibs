_K='eltMnFlappingTime'
_J='eltMnFlappingSecondPortId'
_I='eltMnFlappingFirstPortId'
_H='eltMnFlappingVlanNumber'
_G='eltMnFlappingAddress'
_F='read-write'
_E='TruthValue'
_D='Integer32'
_C='read-only'
_B='ELTEX-MES-eltMacNotification-MIB'
_A='deprecated'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
VlanIndex,=mibBuilder.importSymbols('CISCO-VTP-MIB','VlanIndex')
eltMesMng,=mibBuilder.importSymbols('ELTEX-MES','eltMesMng')
ifIndex,=mibBuilder.importSymbols('IF-MIB','ifIndex')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','TextualConvention','TimeStamp',_E)
eltMesMacNotificationMIB=ModuleIdentity((1,3,6,1,4,1,35265,1,23,1,7))
if mibBuilder.loadTexts:eltMesMacNotificationMIB.setRevisions(('2015-11-05 00:00','2015-11-19 00:00'))
_EltMesMacNotificationObjects_ObjectIdentity=ObjectIdentity
eltMesMacNotificationObjects=_EltMesMacNotificationObjects_ObjectIdentity((1,3,6,1,4,1,35265,1,23,1,7,1))
_EltMesMnFlappingObjects_ObjectIdentity=ObjectIdentity
eltMesMnFlappingObjects=_EltMesMnFlappingObjects_ObjectIdentity((1,3,6,1,4,1,35265,1,23,1,7,1,1))
class _EltMnFlappingFeatureEnabled_Type(TruthValue):defaultValue=1
_EltMnFlappingFeatureEnabled_Type.__name__=_E
_EltMnFlappingFeatureEnabled_Object=MibScalar
eltMnFlappingFeatureEnabled=_EltMnFlappingFeatureEnabled_Object((1,3,6,1,4,1,35265,1,23,1,7,1,1,1),_EltMnFlappingFeatureEnabled_Type())
eltMnFlappingFeatureEnabled.setMaxAccess(_F)
if mibBuilder.loadTexts:eltMnFlappingFeatureEnabled.setStatus(_A)
class _EltMnFlappingNotificationsEnabled_Type(TruthValue):defaultValue=1
_EltMnFlappingNotificationsEnabled_Type.__name__=_E
_EltMnFlappingNotificationsEnabled_Object=MibScalar
eltMnFlappingNotificationsEnabled=_EltMnFlappingNotificationsEnabled_Object((1,3,6,1,4,1,35265,1,23,1,7,1,1,2),_EltMnFlappingNotificationsEnabled_Type())
eltMnFlappingNotificationsEnabled.setMaxAccess(_F)
if mibBuilder.loadTexts:eltMnFlappingNotificationsEnabled.setStatus(_A)
_EltMnFlappingAddress_Type=MacAddress
_EltMnFlappingAddress_Object=MibScalar
eltMnFlappingAddress=_EltMnFlappingAddress_Object((1,3,6,1,4,1,35265,1,23,1,7,1,1,3),_EltMnFlappingAddress_Type())
eltMnFlappingAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:eltMnFlappingAddress.setStatus(_A)
_EltMnFlappingVlanNumber_Type=VlanIndex
_EltMnFlappingVlanNumber_Object=MibScalar
eltMnFlappingVlanNumber=_EltMnFlappingVlanNumber_Object((1,3,6,1,4,1,35265,1,23,1,7,1,1,4),_EltMnFlappingVlanNumber_Type())
eltMnFlappingVlanNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:eltMnFlappingVlanNumber.setStatus(_A)
class _EltMnFlappingFirstPortId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_EltMnFlappingFirstPortId_Type.__name__=_D
_EltMnFlappingFirstPortId_Object=MibScalar
eltMnFlappingFirstPortId=_EltMnFlappingFirstPortId_Object((1,3,6,1,4,1,35265,1,23,1,7,1,1,5),_EltMnFlappingFirstPortId_Type())
eltMnFlappingFirstPortId.setMaxAccess(_C)
if mibBuilder.loadTexts:eltMnFlappingFirstPortId.setStatus(_A)
class _EltMnFlappingSecondPortId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_EltMnFlappingSecondPortId_Type.__name__=_D
_EltMnFlappingSecondPortId_Object=MibScalar
eltMnFlappingSecondPortId=_EltMnFlappingSecondPortId_Object((1,3,6,1,4,1,35265,1,23,1,7,1,1,6),_EltMnFlappingSecondPortId_Type())
eltMnFlappingSecondPortId.setMaxAccess(_C)
if mibBuilder.loadTexts:eltMnFlappingSecondPortId.setStatus(_A)
_EltMnFlappingTime_Type=TimeStamp
_EltMnFlappingTime_Object=MibScalar
eltMnFlappingTime=_EltMnFlappingTime_Object((1,3,6,1,4,1,35265,1,23,1,7,1,1,7),_EltMnFlappingTime_Type())
eltMnFlappingTime.setMaxAccess(_C)
if mibBuilder.loadTexts:eltMnFlappingTime.setStatus(_A)
_EltMesMnNotificationPrefix_ObjectIdentity=ObjectIdentity
eltMesMnNotificationPrefix=_EltMesMnNotificationPrefix_ObjectIdentity((1,3,6,1,4,1,35265,1,23,1,7,2))
_EltMesMnNotifications_ObjectIdentity=ObjectIdentity
eltMesMnNotifications=_EltMesMnNotifications_ObjectIdentity((1,3,6,1,4,1,35265,1,23,1,7,2,0))
eltMnFlappingNotification=NotificationType((1,3,6,1,4,1,35265,1,23,1,7,2,0,1))
eltMnFlappingNotification.setObjects(*((_B,_G),(_B,_H),(_B,_I),(_B,_J),(_B,_K)))
if mibBuilder.loadTexts:eltMnFlappingNotification.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'eltMesMacNotificationMIB':eltMesMacNotificationMIB,'eltMesMacNotificationObjects':eltMesMacNotificationObjects,'eltMesMnFlappingObjects':eltMesMnFlappingObjects,'eltMnFlappingFeatureEnabled':eltMnFlappingFeatureEnabled,'eltMnFlappingNotificationsEnabled':eltMnFlappingNotificationsEnabled,_G:eltMnFlappingAddress,_H:eltMnFlappingVlanNumber,_I:eltMnFlappingFirstPortId,_J:eltMnFlappingSecondPortId,_K:eltMnFlappingTime,'eltMesMnNotificationPrefix':eltMesMnNotificationPrefix,'eltMesMnNotifications':eltMesMnNotifications,'eltMnFlappingNotification':eltMnFlappingNotification})