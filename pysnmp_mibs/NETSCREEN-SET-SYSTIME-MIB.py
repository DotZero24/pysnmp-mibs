_E='enabled'
_D='disable'
_C='Integer32'
_B='current'
_A='read-only'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
netscreenSetting,netscreenSettingMibModule=mibBuilder.importSymbols('NETSCREEN-SMI','netscreenSetting','netscreenSettingMibModule')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
netscreenSetSystimeMibModule=ModuleIdentity((1,3,6,1,4,1,3224,7,0,6))
if mibBuilder.loadTexts:netscreenSetSystimeMibModule.setRevisions(('2004-05-03 00:00','2004-03-03 00:00','2003-11-12 00:00','2001-09-28 00:00','2001-05-27 00:00'))
_NsSetSysTime_ObjectIdentity=ObjectIdentity
nsSetSysTime=_NsSetSysTime_ObjectIdentity((1,3,6,1,4,1,3224,7,6))
_NsSetSysTimeGmtOffset_Type=Integer32
_NsSetSysTimeGmtOffset_Object=MibScalar
nsSetSysTimeGmtOffset=_NsSetSysTimeGmtOffset_Object((1,3,6,1,4,1,3224,7,6,1),_NsSetSysTimeGmtOffset_Type())
nsSetSysTimeGmtOffset.setMaxAccess(_A)
if mibBuilder.loadTexts:nsSetSysTimeGmtOffset.setStatus(_B)
class _NsSetSysTimeDaySaving_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_NsSetSysTimeDaySaving_Type.__name__=_C
_NsSetSysTimeDaySaving_Object=MibScalar
nsSetSysTimeDaySaving=_NsSetSysTimeDaySaving_Object((1,3,6,1,4,1,3224,7,6,2),_NsSetSysTimeDaySaving_Type())
nsSetSysTimeDaySaving.setMaxAccess(_A)
if mibBuilder.loadTexts:nsSetSysTimeDaySaving.setStatus(_B)
_NsSetSysTimeNTP_ObjectIdentity=ObjectIdentity
nsSetSysTimeNTP=_NsSetSysTimeNTP_ObjectIdentity((1,3,6,1,4,1,3224,7,6,3))
class _NsSetNtpEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_NsSetNtpEnable_Type.__name__=_C
_NsSetNtpEnable_Object=MibScalar
nsSetNtpEnable=_NsSetNtpEnable_Object((1,3,6,1,4,1,3224,7,6,3,1),_NsSetNtpEnable_Type())
nsSetNtpEnable.setMaxAccess(_A)
if mibBuilder.loadTexts:nsSetNtpEnable.setStatus(_B)
_NsSetNtpServer_Type=IpAddress
_NsSetNtpServer_Object=MibScalar
nsSetNtpServer=_NsSetNtpServer_Object((1,3,6,1,4,1,3224,7,6,3,2),_NsSetNtpServer_Type())
nsSetNtpServer.setMaxAccess(_A)
if mibBuilder.loadTexts:nsSetNtpServer.setStatus(_B)
_NsSetNtpUpdateInterval_Type=Integer32
_NsSetNtpUpdateInterval_Object=MibScalar
nsSetNtpUpdateInterval=_NsSetNtpUpdateInterval_Object((1,3,6,1,4,1,3224,7,6,3,3),_NsSetNtpUpdateInterval_Type())
nsSetNtpUpdateInterval.setMaxAccess(_A)
if mibBuilder.loadTexts:nsSetNtpUpdateInterval.setStatus(_B)
mibBuilder.exportSymbols('NETSCREEN-SET-SYSTIME-MIB',**{'netscreenSetSystimeMibModule':netscreenSetSystimeMibModule,'nsSetSysTime':nsSetSysTime,'nsSetSysTimeGmtOffset':nsSetSysTimeGmtOffset,'nsSetSysTimeDaySaving':nsSetSysTimeDaySaving,'nsSetSysTimeNTP':nsSetSysTimeNTP,'nsSetNtpEnable':nsSetNtpEnable,'nsSetNtpServer':nsSetNtpServer,'nsSetNtpUpdateInterval':nsSetNtpUpdateInterval})