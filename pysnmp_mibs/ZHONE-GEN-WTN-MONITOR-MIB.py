_C='read-only'
_B='Bits'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI',_B,'Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
zhoneGenWtn,zhoneModules=mibBuilder.importSymbols('Zhone','zhoneGenWtn','zhoneModules')
zhoneGenWtnMonitorModule=ModuleIdentity((1,3,6,1,4,1,5504,6,102))
if mibBuilder.loadTexts:zhoneGenWtnMonitorModule.setRevisions(('1901-05-25 21:36',))
_WtnMonitor_ObjectIdentity=ObjectIdentity
wtnMonitor=_WtnMonitor_ObjectIdentity((1,3,6,1,4,1,5504,3,9,1))
if mibBuilder.loadTexts:wtnMonitor.setStatus(_A)
class _WtnLedStatus_Type(Bits):namedValues=NamedValues(*(('diag',0),('operational',1),('lineInterface',2),('radio',3),('local',4),('remote',5)))
_WtnLedStatus_Type.__name__=_B
_WtnLedStatus_Object=MibScalar
wtnLedStatus=_WtnLedStatus_Object((1,3,6,1,4,1,5504,3,9,1,1),_WtnLedStatus_Type())
wtnLedStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:wtnLedStatus.setStatus(_A)
class _WtnAlarmStatus_Type(Bits):namedValues=NamedValues(*(('minorAlarm',0),('criticalAlarm',1)))
_WtnAlarmStatus_Type.__name__=_B
_WtnAlarmStatus_Object=MibScalar
wtnAlarmStatus=_WtnAlarmStatus_Object((1,3,6,1,4,1,5504,3,9,1,2),_WtnAlarmStatus_Type())
wtnAlarmStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:wtnAlarmStatus.setStatus(_A)
_RadioLinkConfiguration_ObjectIdentity=ObjectIdentity
radioLinkConfiguration=_RadioLinkConfiguration_ObjectIdentity((1,3,6,1,4,1,5504,3,9,2))
if mibBuilder.loadTexts:radioLinkConfiguration.setStatus(_A)
_WtnLinkName_Type=SnmpAdminString
_WtnLinkName_Object=MibScalar
wtnLinkName=_WtnLinkName_Object((1,3,6,1,4,1,5504,3,9,2,1),_WtnLinkName_Type())
wtnLinkName.setMaxAccess('read-write')
if mibBuilder.loadTexts:wtnLinkName.setStatus(_A)
mibBuilder.exportSymbols('ZHONE-GEN-WTN-MONITOR-MIB',**{'wtnMonitor':wtnMonitor,'wtnLedStatus':wtnLedStatus,'wtnAlarmStatus':wtnAlarmStatus,'radioLinkConfiguration':radioLinkConfiguration,'wtnLinkName':wtnLinkName,'zhoneGenWtnMonitorModule':zhoneGenWtnMonitorModule})