_I='aristaTestNotificationsGroup'
_H='aristaTestObjectsGroup'
_G='aristaTestNotification'
_F='read-only'
_E='DisplayString'
_D='aristaTestNotificationComment'
_C='aristaTestNotificationCounter'
_B='current'
_A='ARISTA-TEST-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
aristaMibs,=mibBuilder.importSymbols('ARISTA-SMI-MIB','aristaMibs')
ZeroBasedCounter32,=mibBuilder.importSymbols('RMON2-MIB','ZeroBasedCounter32')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_E,'PhysAddress','TextualConvention')
aristaTestMIB=ModuleIdentity((1,3,6,1,4,1,30065,3,3))
if mibBuilder.loadTexts:aristaTestMIB.setRevisions(('2014-08-15 00:00','2011-03-31 13:00','2010-12-01 00:00'))
_AristaTestNotifications_ObjectIdentity=ObjectIdentity
aristaTestNotifications=_AristaTestNotifications_ObjectIdentity((1,3,6,1,4,1,30065,3,3,0))
_AristaTestNotificationPrefix_ObjectIdentity=ObjectIdentity
aristaTestNotificationPrefix=_AristaTestNotificationPrefix_ObjectIdentity((1,3,6,1,4,1,30065,3,3,0,0))
_AristaTestObjects_ObjectIdentity=ObjectIdentity
aristaTestObjects=_AristaTestObjects_ObjectIdentity((1,3,6,1,4,1,30065,3,3,1))
_AristaTestNotificationCounter_Type=ZeroBasedCounter32
_AristaTestNotificationCounter_Object=MibScalar
aristaTestNotificationCounter=_AristaTestNotificationCounter_Object((1,3,6,1,4,1,30065,3,3,1,1),_AristaTestNotificationCounter_Type())
aristaTestNotificationCounter.setMaxAccess(_F)
if mibBuilder.loadTexts:aristaTestNotificationCounter.setStatus(_B)
class _AristaTestNotificationComment_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_AristaTestNotificationComment_Type.__name__=_E
_AristaTestNotificationComment_Object=MibScalar
aristaTestNotificationComment=_AristaTestNotificationComment_Object((1,3,6,1,4,1,30065,3,3,1,2),_AristaTestNotificationComment_Type())
aristaTestNotificationComment.setMaxAccess(_F)
if mibBuilder.loadTexts:aristaTestNotificationComment.setStatus(_B)
_AristaTestConformance_ObjectIdentity=ObjectIdentity
aristaTestConformance=_AristaTestConformance_ObjectIdentity((1,3,6,1,4,1,30065,3,3,2))
_AristaTestCompliances_ObjectIdentity=ObjectIdentity
aristaTestCompliances=_AristaTestCompliances_ObjectIdentity((1,3,6,1,4,1,30065,3,3,2,1))
_AristaTestGroups_ObjectIdentity=ObjectIdentity
aristaTestGroups=_AristaTestGroups_ObjectIdentity((1,3,6,1,4,1,30065,3,3,2,2))
aristaTestObjectsGroup=ObjectGroup((1,3,6,1,4,1,30065,3,3,2,2,1))
aristaTestObjectsGroup.setObjects(*((_A,_C),(_A,_D)))
if mibBuilder.loadTexts:aristaTestObjectsGroup.setStatus(_B)
aristaTestNotification=NotificationType((1,3,6,1,4,1,30065,3,3,0,0,1))
aristaTestNotification.setObjects(*((_A,_C),(_A,_D)))
if mibBuilder.loadTexts:aristaTestNotification.setStatus(_B)
aristaTestNotificationsGroup=NotificationGroup((1,3,6,1,4,1,30065,3,3,2,2,2))
aristaTestNotificationsGroup.setObjects((_A,_G))
if mibBuilder.loadTexts:aristaTestNotificationsGroup.setStatus(_B)
aristaTestCompliance=ModuleCompliance((1,3,6,1,4,1,30065,3,3,2,1,1))
aristaTestCompliance.setObjects(*((_A,_H),(_A,_I)))
if mibBuilder.loadTexts:aristaTestCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'aristaTestMIB':aristaTestMIB,'aristaTestNotifications':aristaTestNotifications,'aristaTestNotificationPrefix':aristaTestNotificationPrefix,_G:aristaTestNotification,'aristaTestObjects':aristaTestObjects,_C:aristaTestNotificationCounter,_D:aristaTestNotificationComment,'aristaTestConformance':aristaTestConformance,'aristaTestCompliances':aristaTestCompliances,'aristaTestCompliance':aristaTestCompliance,'aristaTestGroups':aristaTestGroups,_H:aristaTestObjectsGroup,_I:aristaTestNotificationsGroup})