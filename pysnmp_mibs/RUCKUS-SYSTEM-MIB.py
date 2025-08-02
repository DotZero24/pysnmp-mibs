_E='read-only'
_D='OctetString'
_C='TruthValue'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_D,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ruckusCommonSystemModule,=mibBuilder.importSymbols('RUCKUS-ROOT-MIB','ruckusCommonSystemModule')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention',_C)
ruckusSystemMIB=ModuleIdentity((1,3,6,1,4,1,25053,1,1,11,1))
_RuckusSystemObjects_ObjectIdentity=ObjectIdentity
ruckusSystemObjects=_RuckusSystemObjects_ObjectIdentity((1,3,6,1,4,1,25053,1,1,11,1,1))
_RuckusSystemInfo_ObjectIdentity=ObjectIdentity
ruckusSystemInfo=_RuckusSystemInfo_ObjectIdentity((1,3,6,1,4,1,25053,1,1,11,1,1,1))
_RuckusSystemCPUUtil_Type=Integer32
_RuckusSystemCPUUtil_Object=MibScalar
ruckusSystemCPUUtil=_RuckusSystemCPUUtil_Object((1,3,6,1,4,1,25053,1,1,11,1,1,1,1),_RuckusSystemCPUUtil_Type())
ruckusSystemCPUUtil.setMaxAccess(_E)
if mibBuilder.loadTexts:ruckusSystemCPUUtil.setStatus(_A)
_RuckusSystemMemoryUtil_Type=Integer32
_RuckusSystemMemoryUtil_Object=MibScalar
ruckusSystemMemoryUtil=_RuckusSystemMemoryUtil_Object((1,3,6,1,4,1,25053,1,1,11,1,1,1,2),_RuckusSystemMemoryUtil_Type())
ruckusSystemMemoryUtil.setMaxAccess(_E)
if mibBuilder.loadTexts:ruckusSystemMemoryUtil.setStatus(_A)
_RuckusSystemServices_ObjectIdentity=ObjectIdentity
ruckusSystemServices=_RuckusSystemServices_ObjectIdentity((1,3,6,1,4,1,25053,1,1,11,1,1,2))
_RuckusSystemHTTP_ObjectIdentity=ObjectIdentity
ruckusSystemHTTP=_RuckusSystemHTTP_ObjectIdentity((1,3,6,1,4,1,25053,1,1,11,1,1,2,1))
class _RuckusSystemHTTPStatus_Type(TruthValue):defaultValue=1
_RuckusSystemHTTPStatus_Type.__name__=_C
_RuckusSystemHTTPStatus_Object=MibScalar
ruckusSystemHTTPStatus=_RuckusSystemHTTPStatus_Object((1,3,6,1,4,1,25053,1,1,11,1,1,2,1,1),_RuckusSystemHTTPStatus_Type())
ruckusSystemHTTPStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusSystemHTTPStatus.setStatus(_A)
_RuckusSystemHTTPS_ObjectIdentity=ObjectIdentity
ruckusSystemHTTPS=_RuckusSystemHTTPS_ObjectIdentity((1,3,6,1,4,1,25053,1,1,11,1,1,2,2))
class _RuckusSystemHTTPSStatus_Type(TruthValue):defaultValue=1
_RuckusSystemHTTPSStatus_Type.__name__=_C
_RuckusSystemHTTPSStatus_Object=MibScalar
ruckusSystemHTTPSStatus=_RuckusSystemHTTPSStatus_Object((1,3,6,1,4,1,25053,1,1,11,1,1,2,2,1),_RuckusSystemHTTPSStatus_Type())
ruckusSystemHTTPSStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusSystemHTTPSStatus.setStatus(_A)
_RuckusSystemTelnet_ObjectIdentity=ObjectIdentity
ruckusSystemTelnet=_RuckusSystemTelnet_ObjectIdentity((1,3,6,1,4,1,25053,1,1,11,1,1,2,3))
class _RuckusSystemTelnetStatus_Type(TruthValue):defaultValue=1
_RuckusSystemTelnetStatus_Type.__name__=_C
_RuckusSystemTelnetStatus_Object=MibScalar
ruckusSystemTelnetStatus=_RuckusSystemTelnetStatus_Object((1,3,6,1,4,1,25053,1,1,11,1,1,2,3,1),_RuckusSystemTelnetStatus_Type())
ruckusSystemTelnetStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusSystemTelnetStatus.setStatus(_A)
_RuckusSystemSSH_ObjectIdentity=ObjectIdentity
ruckusSystemSSH=_RuckusSystemSSH_ObjectIdentity((1,3,6,1,4,1,25053,1,1,11,1,1,2,4))
class _RuckusSystemSSHStatus_Type(TruthValue):defaultValue=1
_RuckusSystemSSHStatus_Type.__name__=_C
_RuckusSystemSSHStatus_Object=MibScalar
ruckusSystemSSHStatus=_RuckusSystemSSHStatus_Object((1,3,6,1,4,1,25053,1,1,11,1,1,2,4,1),_RuckusSystemSSHStatus_Type())
ruckusSystemSSHStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusSystemSSHStatus.setStatus(_A)
_RuckusSystemBonjour_ObjectIdentity=ObjectIdentity
ruckusSystemBonjour=_RuckusSystemBonjour_ObjectIdentity((1,3,6,1,4,1,25053,1,1,11,1,1,2,5))
class _RuckusSystemBonjourStatus_Type(TruthValue):defaultValue=1
_RuckusSystemBonjourStatus_Type.__name__=_C
_RuckusSystemBonjourStatus_Object=MibScalar
ruckusSystemBonjourStatus=_RuckusSystemBonjourStatus_Object((1,3,6,1,4,1,25053,1,1,11,1,1,2,5,1),_RuckusSystemBonjourStatus_Type())
ruckusSystemBonjourStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusSystemBonjourStatus.setStatus(_A)
_RuckusSystemSyslog_ObjectIdentity=ObjectIdentity
ruckusSystemSyslog=_RuckusSystemSyslog_ObjectIdentity((1,3,6,1,4,1,25053,1,1,11,1,1,2,6))
class _RuckusSystemSyslogStatus_Type(TruthValue):defaultValue=1
_RuckusSystemSyslogStatus_Type.__name__=_C
_RuckusSystemSyslogStatus_Object=MibScalar
ruckusSystemSyslogStatus=_RuckusSystemSyslogStatus_Object((1,3,6,1,4,1,25053,1,1,11,1,1,2,6,1),_RuckusSystemSyslogStatus_Type())
ruckusSystemSyslogStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusSystemSyslogStatus.setStatus(_A)
class _RuckusSystemSyslogServerIP_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,40))
_RuckusSystemSyslogServerIP_Type.__name__=_D
_RuckusSystemSyslogServerIP_Object=MibScalar
ruckusSystemSyslogServerIP=_RuckusSystemSyslogServerIP_Object((1,3,6,1,4,1,25053,1,1,11,1,1,2,6,2),_RuckusSystemSyslogServerIP_Type())
ruckusSystemSyslogServerIP.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusSystemSyslogServerIP.setStatus(_A)
_RuckusSystemSyslogServerPort_Type=Integer32
_RuckusSystemSyslogServerPort_Object=MibScalar
ruckusSystemSyslogServerPort=_RuckusSystemSyslogServerPort_Object((1,3,6,1,4,1,25053,1,1,11,1,1,2,6,3),_RuckusSystemSyslogServerPort_Type())
ruckusSystemSyslogServerPort.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusSystemSyslogServerPort.setStatus(_A)
_RuckusSystemSyslogServerProto_Type=DisplayString
_RuckusSystemSyslogServerProto_Object=MibScalar
ruckusSystemSyslogServerProto=_RuckusSystemSyslogServerProto_Object((1,3,6,1,4,1,25053,1,1,11,1,1,2,6,4),_RuckusSystemSyslogServerProto_Type())
ruckusSystemSyslogServerProto.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusSystemSyslogServerProto.setStatus(_A)
class _RuckusSystemSyslogSecondaryServerIP_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,40))
_RuckusSystemSyslogSecondaryServerIP_Type.__name__=_D
_RuckusSystemSyslogSecondaryServerIP_Object=MibScalar
ruckusSystemSyslogSecondaryServerIP=_RuckusSystemSyslogSecondaryServerIP_Object((1,3,6,1,4,1,25053,1,1,11,1,1,2,6,5),_RuckusSystemSyslogSecondaryServerIP_Type())
ruckusSystemSyslogSecondaryServerIP.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusSystemSyslogSecondaryServerIP.setStatus(_A)
_RuckusSystemSyslogSecondaryServerPort_Type=Integer32
_RuckusSystemSyslogSecondaryServerPort_Object=MibScalar
ruckusSystemSyslogSecondaryServerPort=_RuckusSystemSyslogSecondaryServerPort_Object((1,3,6,1,4,1,25053,1,1,11,1,1,2,6,6),_RuckusSystemSyslogSecondaryServerPort_Type())
ruckusSystemSyslogSecondaryServerPort.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusSystemSyslogSecondaryServerPort.setStatus(_A)
_RuckusSystemSyslogSecondaryServerProto_Type=DisplayString
_RuckusSystemSyslogSecondaryServerProto_Object=MibScalar
ruckusSystemSyslogSecondaryServerProto=_RuckusSystemSyslogSecondaryServerProto_Object((1,3,6,1,4,1,25053,1,1,11,1,1,2,6,7),_RuckusSystemSyslogSecondaryServerProto_Type())
ruckusSystemSyslogSecondaryServerProto.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusSystemSyslogSecondaryServerProto.setStatus(_A)
_RuckusSystemNTP_ObjectIdentity=ObjectIdentity
ruckusSystemNTP=_RuckusSystemNTP_ObjectIdentity((1,3,6,1,4,1,25053,1,1,11,1,1,2,7))
class _RuckusSystemNTPStatus_Type(TruthValue):defaultValue=1
_RuckusSystemNTPStatus_Type.__name__=_C
_RuckusSystemNTPStatus_Object=MibScalar
ruckusSystemNTPStatus=_RuckusSystemNTPStatus_Object((1,3,6,1,4,1,25053,1,1,11,1,1,2,7,1),_RuckusSystemNTPStatus_Type())
ruckusSystemNTPStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:ruckusSystemNTPStatus.setStatus(_A)
_RuckusSystemNTPGMTTime_Type=OctetString
_RuckusSystemNTPGMTTime_Object=MibScalar
ruckusSystemNTPGMTTime=_RuckusSystemNTPGMTTime_Object((1,3,6,1,4,1,25053,1,1,11,1,1,2,7,2),_RuckusSystemNTPGMTTime_Type())
ruckusSystemNTPGMTTime.setMaxAccess(_E)
if mibBuilder.loadTexts:ruckusSystemNTPGMTTime.setStatus(_A)
class _RuckusSystemNTPActiveServer_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,128))
_RuckusSystemNTPActiveServer_Type.__name__=_D
_RuckusSystemNTPActiveServer_Object=MibScalar
ruckusSystemNTPActiveServer=_RuckusSystemNTPActiveServer_Object((1,3,6,1,4,1,25053,1,1,11,1,1,2,7,3),_RuckusSystemNTPActiveServer_Type())
ruckusSystemNTPActiveServer.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusSystemNTPActiveServer.setStatus(_A)
_RuckusSystemNTPUpdate_Type=Integer32
_RuckusSystemNTPUpdate_Object=MibScalar
ruckusSystemNTPUpdate=_RuckusSystemNTPUpdate_Object((1,3,6,1,4,1,25053,1,1,11,1,1,2,7,4),_RuckusSystemNTPUpdate_Type())
ruckusSystemNTPUpdate.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusSystemNTPUpdate.setStatus(_A)
_RuckusSystemFlexMaster_ObjectIdentity=ObjectIdentity
ruckusSystemFlexMaster=_RuckusSystemFlexMaster_ObjectIdentity((1,3,6,1,4,1,25053,1,1,11,1,1,2,8))
class _RuckusSystemFlexMasterURL_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,128))
_RuckusSystemFlexMasterURL_Type.__name__=_D
_RuckusSystemFlexMasterURL_Object=MibScalar
ruckusSystemFlexMasterURL=_RuckusSystemFlexMasterURL_Object((1,3,6,1,4,1,25053,1,1,11,1,1,2,8,1),_RuckusSystemFlexMasterURL_Type())
ruckusSystemFlexMasterURL.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusSystemFlexMasterURL.setStatus(_A)
_RuckusSystemCommands_ObjectIdentity=ObjectIdentity
ruckusSystemCommands=_RuckusSystemCommands_ObjectIdentity((1,3,6,1,4,1,25053,1,1,11,1,1,3))
class _RuckusSystemReboot_Type(TruthValue):defaultValue=1
_RuckusSystemReboot_Type.__name__=_C
_RuckusSystemReboot_Object=MibScalar
ruckusSystemReboot=_RuckusSystemReboot_Object((1,3,6,1,4,1,25053,1,1,11,1,1,3,1),_RuckusSystemReboot_Type())
ruckusSystemReboot.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusSystemReboot.setStatus(_A)
class _RuckusSystemSetFactory_Type(TruthValue):defaultValue=1
_RuckusSystemSetFactory_Type.__name__=_C
_RuckusSystemSetFactory_Object=MibScalar
ruckusSystemSetFactory=_RuckusSystemSetFactory_Object((1,3,6,1,4,1,25053,1,1,11,1,1,3,2),_RuckusSystemSetFactory_Type())
ruckusSystemSetFactory.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusSystemSetFactory.setStatus(_A)
class _RuckusSystemDHCPRenew_Type(TruthValue):defaultValue=1
_RuckusSystemDHCPRenew_Type.__name__=_C
_RuckusSystemDHCPRenew_Object=MibScalar
ruckusSystemDHCPRenew=_RuckusSystemDHCPRenew_Object((1,3,6,1,4,1,25053,1,1,11,1,1,3,3),_RuckusSystemDHCPRenew_Type())
ruckusSystemDHCPRenew.setMaxAccess(_B)
if mibBuilder.loadTexts:ruckusSystemDHCPRenew.setStatus(_A)
_RuckusSystemEvents_ObjectIdentity=ObjectIdentity
ruckusSystemEvents=_RuckusSystemEvents_ObjectIdentity((1,3,6,1,4,1,25053,1,1,11,1,2))
mibBuilder.exportSymbols('RUCKUS-SYSTEM-MIB',**{'ruckusSystemMIB':ruckusSystemMIB,'ruckusSystemObjects':ruckusSystemObjects,'ruckusSystemInfo':ruckusSystemInfo,'ruckusSystemCPUUtil':ruckusSystemCPUUtil,'ruckusSystemMemoryUtil':ruckusSystemMemoryUtil,'ruckusSystemServices':ruckusSystemServices,'ruckusSystemHTTP':ruckusSystemHTTP,'ruckusSystemHTTPStatus':ruckusSystemHTTPStatus,'ruckusSystemHTTPS':ruckusSystemHTTPS,'ruckusSystemHTTPSStatus':ruckusSystemHTTPSStatus,'ruckusSystemTelnet':ruckusSystemTelnet,'ruckusSystemTelnetStatus':ruckusSystemTelnetStatus,'ruckusSystemSSH':ruckusSystemSSH,'ruckusSystemSSHStatus':ruckusSystemSSHStatus,'ruckusSystemBonjour':ruckusSystemBonjour,'ruckusSystemBonjourStatus':ruckusSystemBonjourStatus,'ruckusSystemSyslog':ruckusSystemSyslog,'ruckusSystemSyslogStatus':ruckusSystemSyslogStatus,'ruckusSystemSyslogServerIP':ruckusSystemSyslogServerIP,'ruckusSystemSyslogServerPort':ruckusSystemSyslogServerPort,'ruckusSystemSyslogServerProto':ruckusSystemSyslogServerProto,'ruckusSystemSyslogSecondaryServerIP':ruckusSystemSyslogSecondaryServerIP,'ruckusSystemSyslogSecondaryServerPort':ruckusSystemSyslogSecondaryServerPort,'ruckusSystemSyslogSecondaryServerProto':ruckusSystemSyslogSecondaryServerProto,'ruckusSystemNTP':ruckusSystemNTP,'ruckusSystemNTPStatus':ruckusSystemNTPStatus,'ruckusSystemNTPGMTTime':ruckusSystemNTPGMTTime,'ruckusSystemNTPActiveServer':ruckusSystemNTPActiveServer,'ruckusSystemNTPUpdate':ruckusSystemNTPUpdate,'ruckusSystemFlexMaster':ruckusSystemFlexMaster,'ruckusSystemFlexMasterURL':ruckusSystemFlexMasterURL,'ruckusSystemCommands':ruckusSystemCommands,'ruckusSystemReboot':ruckusSystemReboot,'ruckusSystemSetFactory':ruckusSystemSetFactory,'ruckusSystemDHCPRenew':ruckusSystemDHCPRenew,'ruckusSystemEvents':ruckusSystemEvents})