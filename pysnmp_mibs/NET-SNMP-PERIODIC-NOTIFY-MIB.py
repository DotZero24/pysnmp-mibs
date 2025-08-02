_B='accessible-for-notify'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
netSnmpModuleIDs,netSnmpNotifications,netSnmpObjects=mibBuilder.importSymbols('NET-SNMP-MIB','netSnmpModuleIDs','netSnmpNotifications','netSnmpObjects')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
netSnmpPeriodicNotifyMib=ModuleIdentity((1,3,6,1,4,1,8072,3,1,5))
if mibBuilder.loadTexts:netSnmpPeriodicNotifyMib.setRevisions(('2011-04-20 00:00',))
_NsPNScalars_ObjectIdentity=ObjectIdentity
nsPNScalars=_NsPNScalars_ObjectIdentity((1,3,6,1,4,1,8072,3,1,5,1))
_NsPNTables_ObjectIdentity=ObjectIdentity
nsPNTables=_NsPNTables_ObjectIdentity((1,3,6,1,4,1,8072,3,1,5,2))
_NsPNotifyObjects_ObjectIdentity=ObjectIdentity
nsPNotifyObjects=_NsPNotifyObjects_ObjectIdentity((1,3,6,1,4,1,8072,3,1,5,3))
_NsPNPeriodicTime_Type=Unsigned32
_NsPNPeriodicTime_Object=MibScalar
nsPNPeriodicTime=_NsPNPeriodicTime_Object((1,3,6,1,4,1,8072,3,1,5,3,1),_NsPNPeriodicTime_Type())
nsPNPeriodicTime.setMaxAccess(_B)
if mibBuilder.loadTexts:nsPNPeriodicTime.setStatus(_A)
_NsPNotifyMessageNumber_Type=Unsigned32
_NsPNotifyMessageNumber_Object=MibScalar
nsPNotifyMessageNumber=_NsPNotifyMessageNumber_Object((1,3,6,1,4,1,8072,3,1,5,3,2),_NsPNotifyMessageNumber_Type())
nsPNotifyMessageNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:nsPNotifyMessageNumber.setStatus(_A)
_NsPNotifyMaxMessageNumber_Type=Unsigned32
_NsPNotifyMaxMessageNumber_Object=MibScalar
nsPNotifyMaxMessageNumber=_NsPNotifyMaxMessageNumber_Object((1,3,6,1,4,1,8072,3,1,5,3,3),_NsPNotifyMaxMessageNumber_Type())
nsPNotifyMaxMessageNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:nsPNotifyMaxMessageNumber.setStatus(_A)
_NsPNotificationPrefix_ObjectIdentity=ObjectIdentity
nsPNotificationPrefix=_NsPNotificationPrefix_ObjectIdentity((1,3,6,1,4,1,8072,3,1,5,4))
_NsPNotifications_ObjectIdentity=ObjectIdentity
nsPNotifications=_NsPNotifications_ObjectIdentity((1,3,6,1,4,1,8072,3,1,5,4,0))
_NsPNotificationObjects_ObjectIdentity=ObjectIdentity
nsPNotificationObjects=_NsPNotificationObjects_ObjectIdentity((1,3,6,1,4,1,8072,3,1,5,4,1))
nsNotifyPeriodicNotification=NotificationType((1,3,6,1,4,1,8072,3,1,5,4,0,1))
if mibBuilder.loadTexts:nsNotifyPeriodicNotification.setStatus(_A)
mibBuilder.exportSymbols('NET-SNMP-PERIODIC-NOTIFY-MIB',**{'netSnmpPeriodicNotifyMib':netSnmpPeriodicNotifyMib,'nsPNScalars':nsPNScalars,'nsPNTables':nsPNTables,'nsPNotifyObjects':nsPNotifyObjects,'nsPNPeriodicTime':nsPNPeriodicTime,'nsPNotifyMessageNumber':nsPNotifyMessageNumber,'nsPNotifyMaxMessageNumber':nsPNotifyMaxMessageNumber,'nsPNotificationPrefix':nsPNotificationPrefix,'nsPNotifications':nsPNotifications,'nsNotifyPeriodicNotification':nsNotifyPeriodicNotification,'nsPNotificationObjects':nsPNotificationObjects})