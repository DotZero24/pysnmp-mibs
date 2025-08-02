_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
radioConfig,=mibBuilder.importSymbols('ExaltComProducts','radioConfig')
SyslogEnableT,SyslogFilterSelectT=mibBuilder.importSymbols('ExaltComm','SyslogEnableT','SyslogFilterSelectT')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
_AdvSystemConfig_ObjectIdentity=ObjectIdentity
advSystemConfig=_AdvSystemConfig_ObjectIdentity((1,3,6,1,4,1,25651,1,2,3,5))
if mibBuilder.loadTexts:advSystemConfig.setStatus(_A)
_SyslogCfg_ObjectIdentity=ObjectIdentity
syslogCfg=_SyslogCfg_ObjectIdentity((1,3,6,1,4,1,25651,1,2,3,5,6))
if mibBuilder.loadTexts:syslogCfg.setStatus(_A)
_SyslogEnable_Type=SyslogEnableT
_SyslogEnable_Object=MibScalar
syslogEnable=_SyslogEnable_Object((1,3,6,1,4,1,25651,1,2,3,5,6,1),_SyslogEnable_Type())
syslogEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:syslogEnable.setStatus(_A)
_SyslogRemoteIpAddr_Type=DisplayString
_SyslogRemoteIpAddr_Object=MibScalar
syslogRemoteIpAddr=_SyslogRemoteIpAddr_Object((1,3,6,1,4,1,25651,1,2,3,5,6,2),_SyslogRemoteIpAddr_Type())
syslogRemoteIpAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:syslogRemoteIpAddr.setStatus(_A)
_SyslogFilterSelect_Type=SyslogFilterSelectT
_SyslogFilterSelect_Object=MibScalar
syslogFilterSelect=_SyslogFilterSelect_Object((1,3,6,1,4,1,25651,1,2,3,5,6,3),_SyslogFilterSelect_Type())
syslogFilterSelect.setMaxAccess(_B)
if mibBuilder.loadTexts:syslogFilterSelect.setStatus(_A)
_CommitSyslogSettings_Type=DisplayString
_CommitSyslogSettings_Object=MibScalar
commitSyslogSettings=_CommitSyslogSettings_Object((1,3,6,1,4,1,25651,1,2,3,5,6,1000),_CommitSyslogSettings_Type())
commitSyslogSettings.setMaxAccess(_B)
if mibBuilder.loadTexts:commitSyslogSettings.setStatus(_A)
mibBuilder.exportSymbols('SYSLOG',**{'advSystemConfig':advSystemConfig,'syslogCfg':syslogCfg,'syslogEnable':syslogEnable,'syslogRemoteIpAddr':syslogRemoteIpAddr,'syslogFilterSelect':syslogFilterSelect,'commitSyslogSettings':commitSyslogSettings})