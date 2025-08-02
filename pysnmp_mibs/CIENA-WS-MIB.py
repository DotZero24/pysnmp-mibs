_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
ciena=ModuleIdentity((1,3,6,1,4,1,1271))
if mibBuilder.loadTexts:ciena.setRevisions(('2018-04-27 00:00',))
_Waveserver_ObjectIdentity=ObjectIdentity
waveserver=_Waveserver_ObjectIdentity((1,3,6,1,4,1,1271,3))
if mibBuilder.loadTexts:waveserver.setStatus(_A)
_CienaWsConfigV1_ObjectIdentity=ObjectIdentity
cienaWsConfigV1=_CienaWsConfigV1_ObjectIdentity((1,3,6,1,4,1,1271,3,1))
if mibBuilder.loadTexts:cienaWsConfigV1.setStatus(_A)
_CienaWsNotifications_ObjectIdentity=ObjectIdentity
cienaWsNotifications=_CienaWsNotifications_ObjectIdentity((1,3,6,1,4,1,1271,3,2))
if mibBuilder.loadTexts:cienaWsNotifications.setStatus(_A)
_CienaWsNotificationsControlModule_ObjectIdentity=ObjectIdentity
cienaWsNotificationsControlModule=_CienaWsNotificationsControlModule_ObjectIdentity((1,3,6,1,4,1,1271,3,2,1))
if mibBuilder.loadTexts:cienaWsNotificationsControlModule.setStatus(_A)
_CienaWsStatistics_ObjectIdentity=ObjectIdentity
cienaWsStatistics=_CienaWsStatistics_ObjectIdentity((1,3,6,1,4,1,1271,3,3))
if mibBuilder.loadTexts:cienaWsStatistics.setStatus('obsolete')
_CienaWsConfig_ObjectIdentity=ObjectIdentity
cienaWsConfig=_CienaWsConfig_ObjectIdentity((1,3,6,1,4,1,1271,3,4))
if mibBuilder.loadTexts:cienaWsConfig.setStatus(_A)
_CienaWsPlatformConfig_ObjectIdentity=ObjectIdentity
cienaWsPlatformConfig=_CienaWsPlatformConfig_ObjectIdentity((1,3,6,1,4,1,1271,3,5))
if mibBuilder.loadTexts:cienaWsPlatformConfig.setStatus(_A)
mibBuilder.exportSymbols('CIENA-WS-MIB',**{'ciena':ciena,'waveserver':waveserver,'cienaWsConfigV1':cienaWsConfigV1,'cienaWsNotifications':cienaWsNotifications,'cienaWsNotificationsControlModule':cienaWsNotificationsControlModule,'cienaWsStatistics':cienaWsStatistics,'cienaWsConfig':cienaWsConfig,'cienaWsPlatformConfig':cienaWsPlatformConfig})