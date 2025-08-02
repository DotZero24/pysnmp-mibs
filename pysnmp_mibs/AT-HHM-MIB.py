_D='atHhmLogMessage'
_C='AT-HHM-MIB'
_B='current'
_A='DisplayStringUnsized'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
DisplayStringUnsized,=mibBuilder.importSymbols('AT-SMI-MIB',_A)
sysinfo,=mibBuilder.importSymbols('AT-SYSINFO-MIB','sysinfo')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
atHwHealthMon=ModuleIdentity((1,3,6,1,4,1,207,8,4,4,3,24))
if mibBuilder.loadTexts:atHwHealthMon.setRevisions(('2013-06-28 00:00',))
_AtHhmNotifications_ObjectIdentity=ObjectIdentity
atHhmNotifications=_AtHhmNotifications_ObjectIdentity((1,3,6,1,4,1,207,8,4,4,3,24,0))
_AtHhmNotificationVariables_ObjectIdentity=ObjectIdentity
atHhmNotificationVariables=_AtHhmNotificationVariables_ObjectIdentity((1,3,6,1,4,1,207,8,4,4,3,24,1))
class _AtHhmLogMessage_Type(DisplayStringUnsized):subtypeSpec=DisplayStringUnsized.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,200))
_AtHhmLogMessage_Type.__name__=_A
_AtHhmLogMessage_Object=MibScalar
atHhmLogMessage=_AtHhmLogMessage_Object((1,3,6,1,4,1,207,8,4,4,3,24,1,1),_AtHhmLogMessage_Type())
atHhmLogMessage.setMaxAccess('accessible-for-notify')
if mibBuilder.loadTexts:atHhmLogMessage.setStatus(_B)
atHhmLogNotify=NotificationType((1,3,6,1,4,1,207,8,4,4,3,24,0,1))
atHhmLogNotify.setObjects((_C,_D))
if mibBuilder.loadTexts:atHhmLogNotify.setStatus(_B)
mibBuilder.exportSymbols(_C,**{'atHwHealthMon':atHwHealthMon,'atHhmNotifications':atHhmNotifications,'atHhmLogNotify':atHhmLogNotify,'atHhmNotificationVariables':atHhmNotificationVariables,_D:atHhmLogMessage})