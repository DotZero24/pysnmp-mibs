_M='eventErrorMsg'
_L='eventWarningMsg'
_K='eventInformMsg'
_J='unlimited'
_I='sysFanIndex'
_H='NotificationType'
_G='DisplayString'
_F='QTS-MIB'
_E='yes'
_D='no'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,NotificationType,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier',_H,'ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn',_H,'TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_G,'PhysAddress','TextualConvention')
class DisplayString(OctetString):0
_QNAP_ObjectIdentity=ObjectIdentity
QNAP=_QNAP_ObjectIdentity((1,3,6,1,4,1,55062))
_QTS_ObjectIdentity=ObjectIdentity
QTS=_QTS_ObjectIdentity((1,3,6,1,4,1,55062,1))
_System_ObjectIdentity=ObjectIdentity
system=_System_ObjectIdentity((1,3,6,1,4,1,55062,1,12))
_SystemEventMsg_ObjectIdentity=ObjectIdentity
systemEventMsg=_SystemEventMsg_ObjectIdentity((1,3,6,1,4,1,55062,1,12,1))
_EventInformMsg_Type=DisplayString
_EventInformMsg_Object=MibScalar
eventInformMsg=_EventInformMsg_Object((1,3,6,1,4,1,55062,1,12,1,101),_EventInformMsg_Type())
eventInformMsg.setMaxAccess(_B)
if mibBuilder.loadTexts:eventInformMsg.setStatus(_A)
_EventWarningMsg_Type=DisplayString
_EventWarningMsg_Object=MibScalar
eventWarningMsg=_EventWarningMsg_Object((1,3,6,1,4,1,55062,1,12,1,102),_EventWarningMsg_Type())
eventWarningMsg.setMaxAccess(_B)
if mibBuilder.loadTexts:eventWarningMsg.setStatus(_A)
_EventErrorMsg_Type=DisplayString
_EventErrorMsg_Object=MibScalar
eventErrorMsg=_EventErrorMsg_Object((1,3,6,1,4,1,55062,1,12,1,103),_EventErrorMsg_Type())
eventErrorMsg.setMaxAccess(_B)
if mibBuilder.loadTexts:eventErrorMsg.setStatus(_A)
_SystemTraps_ObjectIdentity=ObjectIdentity
systemTraps=_SystemTraps_ObjectIdentity((1,3,6,1,4,1,55062,1,12,2))
_SystemModel_Type=DisplayString
_SystemModel_Object=MibScalar
systemModel=_SystemModel_Object((1,3,6,1,4,1,55062,1,12,3),_SystemModel_Type())
systemModel.setMaxAccess(_B)
if mibBuilder.loadTexts:systemModel.setStatus(_A)
_Hostname_Type=DisplayString
_Hostname_Object=MibScalar
hostname=_Hostname_Object((1,3,6,1,4,1,55062,1,12,4),_Hostname_Type())
hostname.setMaxAccess(_B)
if mibBuilder.loadTexts:hostname.setStatus(_A)
class _SerialNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_SerialNumber_Type.__name__=_G
_SerialNumber_Object=MibScalar
serialNumber=_SerialNumber_Object((1,3,6,1,4,1,55062,1,12,5),_SerialNumber_Type())
serialNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:serialNumber.setStatus(_A)
_FirmwareVersion_Type=DisplayString
_FirmwareVersion_Object=MibScalar
firmwareVersion=_FirmwareVersion_Object((1,3,6,1,4,1,55062,1,12,6),_FirmwareVersion_Type())
firmwareVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:firmwareVersion.setStatus(_A)
_FirmwareUpgradeAvailable_Type=Integer32
_FirmwareUpgradeAvailable_Object=MibScalar
firmwareUpgradeAvailable=_FirmwareUpgradeAvailable_Object((1,3,6,1,4,1,55062,1,12,7),_FirmwareUpgradeAvailable_Type())
firmwareUpgradeAvailable.setMaxAccess(_B)
if mibBuilder.loadTexts:firmwareUpgradeAvailable.setStatus(_A)
_SysFanNumber_Type=Integer32
_SysFanNumber_Object=MibScalar
sysFanNumber=_SysFanNumber_Object((1,3,6,1,4,1,55062,1,12,8),_SysFanNumber_Type())
sysFanNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:sysFanNumber.setStatus(_A)
_SystemFanTable_Object=MibTable
systemFanTable=_SystemFanTable_Object((1,3,6,1,4,1,55062,1,12,9))
if mibBuilder.loadTexts:systemFanTable.setStatus(_A)
_SysFanEntry_Object=MibTableRow
sysFanEntry=_SysFanEntry_Object((1,3,6,1,4,1,55062,1,12,9,1))
sysFanEntry.setIndexNames((0,_F,_I))
if mibBuilder.loadTexts:sysFanEntry.setStatus(_A)
_SysFanIndex_Type=Integer32
_SysFanIndex_Object=MibTableColumn
sysFanIndex=_SysFanIndex_Object((1,3,6,1,4,1,55062,1,12,9,1,1),_SysFanIndex_Type())
sysFanIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:sysFanIndex.setStatus(_A)
class _SysFanDescr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_SysFanDescr_Type.__name__=_G
_SysFanDescr_Object=MibTableColumn
sysFanDescr=_SysFanDescr_Object((1,3,6,1,4,1,55062,1,12,9,1,2),_SysFanDescr_Type())
sysFanDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:sysFanDescr.setStatus(_A)
_SysFanSpeed_Type=Integer32
_SysFanSpeed_Object=MibTableColumn
sysFanSpeed=_SysFanSpeed_Object((1,3,6,1,4,1,55062,1,12,9,1,3),_SysFanSpeed_Type())
sysFanSpeed.setMaxAccess(_B)
if mibBuilder.loadTexts:sysFanSpeed.setStatus(_A)
_CpuTemperature_Type=Integer32
_CpuTemperature_Object=MibScalar
cpuTemperature=_CpuTemperature_Object((1,3,6,1,4,1,55062,1,12,10),_CpuTemperature_Type())
cpuTemperature.setMaxAccess(_B)
if mibBuilder.loadTexts:cpuTemperature.setStatus(_A)
_SystemTemperature_Type=Integer32
_SystemTemperature_Object=MibScalar
systemTemperature=_SystemTemperature_Object((1,3,6,1,4,1,55062,1,12,11),_SystemTemperature_Type())
systemTemperature.setMaxAccess(_B)
if mibBuilder.loadTexts:systemTemperature.setStatus(_A)
_SystemCPU_Usage_Type=Integer32
_SystemCPU_Usage_Object=MibScalar
systemCPU_Usage=_SystemCPU_Usage_Object((1,3,6,1,4,1,55062,1,12,12),_SystemCPU_Usage_Type())
systemCPU_Usage.setMaxAccess(_B)
if mibBuilder.loadTexts:systemCPU_Usage.setStatus(_A)
_SystemTotalMem_Type=Counter64
_SystemTotalMem_Object=MibScalar
systemTotalMem=_SystemTotalMem_Object((1,3,6,1,4,1,55062,1,12,13),_SystemTotalMem_Type())
systemTotalMem.setMaxAccess(_B)
if mibBuilder.loadTexts:systemTotalMem.setStatus(_A)
_SystemFreeMem_Type=Counter64
_SystemFreeMem_Object=MibScalar
systemFreeMem=_SystemFreeMem_Object((1,3,6,1,4,1,55062,1,12,14),_SystemFreeMem_Type())
systemFreeMem.setMaxAccess(_B)
if mibBuilder.loadTexts:systemFreeMem.setStatus(_A)
_SystemAvailableMem_Type=Counter64
_SystemAvailableMem_Object=MibScalar
systemAvailableMem=_SystemAvailableMem_Object((1,3,6,1,4,1,55062,1,12,15),_SystemAvailableMem_Type())
systemAvailableMem.setMaxAccess(_B)
if mibBuilder.loadTexts:systemAvailableMem.setStatus(_A)
_SystemUsedMemory_Type=Counter64
_SystemUsedMemory_Object=MibScalar
systemUsedMemory=_SystemUsedMemory_Object((1,3,6,1,4,1,55062,1,12,16),_SystemUsedMemory_Type())
systemUsedMemory.setMaxAccess(_B)
if mibBuilder.loadTexts:systemUsedMemory.setStatus(_A)
_SystemCacheMemory_Type=Counter64
_SystemCacheMemory_Object=MibScalar
systemCacheMemory=_SystemCacheMemory_Object((1,3,6,1,4,1,55062,1,12,17),_SystemCacheMemory_Type())
systemCacheMemory.setMaxAccess(_B)
if mibBuilder.loadTexts:systemCacheMemory.setStatus(_A)
_SystemBufferMemory_Type=Counter64
_SystemBufferMemory_Object=MibScalar
systemBufferMemory=_SystemBufferMemory_Object((1,3,6,1,4,1,55062,1,12,18),_SystemBufferMemory_Type())
systemBufferMemory.setMaxAccess(_B)
if mibBuilder.loadTexts:systemBufferMemory.setStatus(_A)
class _SysPowerStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(-1,0)));namedValues=NamedValues(*(('failed',-1),('ok',0)))
_SysPowerStatus_Type.__name__=_C
_SysPowerStatus_Object=MibScalar
sysPowerStatus=_SysPowerStatus_Object((1,3,6,1,4,1,55062,1,12,19),_SysPowerStatus_Type())
sysPowerStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:sysPowerStatus.setStatus(_A)
_SysUPSStatus_Type=Integer32
_SysUPSStatus_Object=MibScalar
sysUPSStatus=_SysUPSStatus_Object((1,3,6,1,4,1,55062,1,12,20),_SysUPSStatus_Type())
sysUPSStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:sysUPSStatus.setStatus(_A)
_SysUptime_Type=TimeTicks
_SysUptime_Object=MibScalar
sysUptime=_SysUptime_Object((1,3,6,1,4,1,55062,1,12,21),_SysUptime_Type())
sysUptime.setMaxAccess(_B)
if mibBuilder.loadTexts:sysUptime.setStatus(_A)
_Services_ObjectIdentity=ObjectIdentity
services=_Services_ObjectIdentity((1,3,6,1,4,1,55062,1,14))
class _NfsV2V3IsEnabled_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_NfsV2V3IsEnabled_Type.__name__=_C
_NfsV2V3IsEnabled_Object=MibScalar
nfsV2V3IsEnabled=_NfsV2V3IsEnabled_Object((1,3,6,1,4,1,55062,1,14,1),_NfsV2V3IsEnabled_Type())
nfsV2V3IsEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:nfsV2V3IsEnabled.setStatus(_A)
class _NfsV4IsEnabled_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_NfsV4IsEnabled_Type.__name__=_C
_NfsV4IsEnabled_Object=MibScalar
nfsV4IsEnabled=_NfsV4IsEnabled_Object((1,3,6,1,4,1,55062,1,14,2),_NfsV4IsEnabled_Type())
nfsV4IsEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:nfsV4IsEnabled.setStatus(_A)
_HttpPort_Type=Integer32
_HttpPort_Object=MibScalar
httpPort=_HttpPort_Object((1,3,6,1,4,1,55062,1,14,3),_HttpPort_Type())
httpPort.setMaxAccess(_B)
if mibBuilder.loadTexts:httpPort.setStatus(_A)
_HttpsPort_Type=Integer32
_HttpsPort_Object=MibScalar
httpsPort=_HttpsPort_Object((1,3,6,1,4,1,55062,1,14,4),_HttpsPort_Type())
httpsPort.setMaxAccess(_B)
if mibBuilder.loadTexts:httpsPort.setStatus(_A)
class _SshIsEnabled_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_SshIsEnabled_Type.__name__=_C
_SshIsEnabled_Object=MibScalar
sshIsEnabled=_SshIsEnabled_Object((1,3,6,1,4,1,55062,1,14,5),_SshIsEnabled_Type())
sshIsEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:sshIsEnabled.setStatus(_A)
class _SshSFTPEnabled_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_SshSFTPEnabled_Type.__name__=_C
_SshSFTPEnabled_Object=MibScalar
sshSFTPEnabled=_SshSFTPEnabled_Object((1,3,6,1,4,1,55062,1,14,6),_SshSFTPEnabled_Type())
sshSFTPEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:sshSFTPEnabled.setStatus(_A)
_SshPortNumber_Type=Integer32
_SshPortNumber_Object=MibScalar
sshPortNumber=_SshPortNumber_Object((1,3,6,1,4,1,55062,1,14,7),_SshPortNumber_Type())
sshPortNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:sshPortNumber.setStatus(_A)
class _TelnetIsEnabled_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_TelnetIsEnabled_Type.__name__=_C
_TelnetIsEnabled_Object=MibScalar
telnetIsEnabled=_TelnetIsEnabled_Object((1,3,6,1,4,1,55062,1,14,8),_TelnetIsEnabled_Type())
telnetIsEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:telnetIsEnabled.setStatus(_A)
_TelnetPortNumber_Type=Integer32
_TelnetPortNumber_Object=MibScalar
telnetPortNumber=_TelnetPortNumber_Object((1,3,6,1,4,1,55062,1,14,9),_TelnetPortNumber_Type())
telnetPortNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:telnetPortNumber.setStatus(_A)
class _FtpEnabled_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_FtpEnabled_Type.__name__=_C
_FtpEnabled_Object=MibScalar
ftpEnabled=_FtpEnabled_Object((1,3,6,1,4,1,55062,1,14,10),_FtpEnabled_Type())
ftpEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:ftpEnabled.setStatus(_A)
class _FtpProtocolStandardEnabled_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_FtpProtocolStandardEnabled_Type.__name__=_C
_FtpProtocolStandardEnabled_Object=MibScalar
ftpProtocolStandardEnabled=_FtpProtocolStandardEnabled_Object((1,3,6,1,4,1,55062,1,14,11),_FtpProtocolStandardEnabled_Type())
ftpProtocolStandardEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:ftpProtocolStandardEnabled.setStatus(_A)
class _FtpProtocolSSL_TLSEnabled_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_FtpProtocolSSL_TLSEnabled_Type.__name__=_C
_FtpProtocolSSL_TLSEnabled_Object=MibScalar
ftpProtocolSSL_TLSEnabled=_FtpProtocolSSL_TLSEnabled_Object((1,3,6,1,4,1,55062,1,14,12),_FtpProtocolSSL_TLSEnabled_Type())
ftpProtocolSSL_TLSEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:ftpProtocolSSL_TLSEnabled.setStatus(_A)
_FtpPortNumber_Type=Integer32
_FtpPortNumber_Object=MibScalar
ftpPortNumber=_FtpPortNumber_Object((1,3,6,1,4,1,55062,1,14,13),_FtpPortNumber_Type())
ftpPortNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:ftpPortNumber.setStatus(_A)
class _FtpUnicodeSupportEnabled_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_FtpUnicodeSupportEnabled_Type.__name__=_C
_FtpUnicodeSupportEnabled_Object=MibScalar
ftpUnicodeSupportEnabled=_FtpUnicodeSupportEnabled_Object((1,3,6,1,4,1,55062,1,14,14),_FtpUnicodeSupportEnabled_Type())
ftpUnicodeSupportEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:ftpUnicodeSupportEnabled.setStatus(_A)
class _FtpAnnonymousaccessEnabled_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_D,0),(_E,1)))
_FtpAnnonymousaccessEnabled_Type.__name__=_C
_FtpAnnonymousaccessEnabled_Object=MibScalar
ftpAnnonymousaccessEnabled=_FtpAnnonymousaccessEnabled_Object((1,3,6,1,4,1,55062,1,14,15),_FtpAnnonymousaccessEnabled_Type())
ftpAnnonymousaccessEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:ftpAnnonymousaccessEnabled.setStatus(_A)
_FtpMaxConnectionsAllowed_Type=Integer32
_FtpMaxConnectionsAllowed_Object=MibScalar
ftpMaxConnectionsAllowed=_FtpMaxConnectionsAllowed_Object((1,3,6,1,4,1,55062,1,14,16),_FtpMaxConnectionsAllowed_Type())
ftpMaxConnectionsAllowed.setMaxAccess(_B)
if mibBuilder.loadTexts:ftpMaxConnectionsAllowed.setStatus(_A)
_FtpMaxConnectionsPerAccount_Type=Integer32
_FtpMaxConnectionsPerAccount_Object=MibScalar
ftpMaxConnectionsPerAccount=_FtpMaxConnectionsPerAccount_Object((1,3,6,1,4,1,55062,1,14,17),_FtpMaxConnectionsPerAccount_Type())
ftpMaxConnectionsPerAccount.setMaxAccess(_B)
if mibBuilder.loadTexts:ftpMaxConnectionsPerAccount.setStatus(_A)
class _FtpMaxUploadRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(0));namedValues=NamedValues((_J,0))
_FtpMaxUploadRate_Type.__name__=_C
_FtpMaxUploadRate_Object=MibScalar
ftpMaxUploadRate=_FtpMaxUploadRate_Object((1,3,6,1,4,1,55062,1,14,18),_FtpMaxUploadRate_Type())
ftpMaxUploadRate.setMaxAccess(_B)
if mibBuilder.loadTexts:ftpMaxUploadRate.setStatus(_A)
class _FtpMaxDownloadRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(0));namedValues=NamedValues((_J,0))
_FtpMaxDownloadRate_Type.__name__=_C
_FtpMaxDownloadRate_Object=MibScalar
ftpMaxDownloadRate=_FtpMaxDownloadRate_Object((1,3,6,1,4,1,55062,1,14,19),_FtpMaxDownloadRate_Type())
ftpMaxDownloadRate.setMaxAccess(_B)
if mibBuilder.loadTexts:ftpMaxDownloadRate.setStatus(_A)
eventInform=NotificationType((1,3,6,1,4,1,55062,1,12,2,1))
eventInform.setObjects((_F,_K))
if mibBuilder.loadTexts:eventInform.setStatus(_A)
eventWarning=NotificationType((1,3,6,1,4,1,55062,1,12,2,2))
eventWarning.setObjects((_F,_L))
if mibBuilder.loadTexts:eventWarning.setStatus(_A)
eventError=NotificationType((1,3,6,1,4,1,55062,1,12,2,4))
eventError.setObjects((_F,_M))
if mibBuilder.loadTexts:eventError.setStatus(_A)
mibBuilder.exportSymbols(_F,**{_G:DisplayString,'QNAP':QNAP,'QTS':QTS,'system':system,'systemEventMsg':systemEventMsg,_K:eventInformMsg,_L:eventWarningMsg,_M:eventErrorMsg,'systemTraps':systemTraps,'eventInform':eventInform,'eventWarning':eventWarning,'eventError':eventError,'systemModel':systemModel,'hostname':hostname,'serialNumber':serialNumber,'firmwareVersion':firmwareVersion,'firmwareUpgradeAvailable':firmwareUpgradeAvailable,'sysFanNumber':sysFanNumber,'systemFanTable':systemFanTable,'sysFanEntry':sysFanEntry,_I:sysFanIndex,'sysFanDescr':sysFanDescr,'sysFanSpeed':sysFanSpeed,'cpuTemperature':cpuTemperature,'systemTemperature':systemTemperature,'systemCPU-Usage':systemCPU_Usage,'systemTotalMem':systemTotalMem,'systemFreeMem':systemFreeMem,'systemAvailableMem':systemAvailableMem,'systemUsedMemory':systemUsedMemory,'systemCacheMemory':systemCacheMemory,'systemBufferMemory':systemBufferMemory,'sysPowerStatus':sysPowerStatus,'sysUPSStatus':sysUPSStatus,'sysUptime':sysUptime,'services':services,'nfsV2V3IsEnabled':nfsV2V3IsEnabled,'nfsV4IsEnabled':nfsV4IsEnabled,'httpPort':httpPort,'httpsPort':httpsPort,'sshIsEnabled':sshIsEnabled,'sshSFTPEnabled':sshSFTPEnabled,'sshPortNumber':sshPortNumber,'telnetIsEnabled':telnetIsEnabled,'telnetPortNumber':telnetPortNumber,'ftpEnabled':ftpEnabled,'ftpProtocolStandardEnabled':ftpProtocolStandardEnabled,'ftpProtocolSSL-TLSEnabled':ftpProtocolSSL_TLSEnabled,'ftpPortNumber':ftpPortNumber,'ftpUnicodeSupportEnabled':ftpUnicodeSupportEnabled,'ftpAnnonymousaccessEnabled':ftpAnnonymousaccessEnabled,'ftpMaxConnectionsAllowed':ftpMaxConnectionsAllowed,'ftpMaxConnectionsPerAccount':ftpMaxConnectionsPerAccount,'ftpMaxUploadRate':ftpMaxUploadRate,'ftpMaxDownloadRate':ftpMaxDownloadRate})