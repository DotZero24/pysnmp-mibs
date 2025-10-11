# SNMP MIB module (QTS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/qnap/QTS-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:10:59 2025
# On host Robs-Air.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]

if 'mibBuilder' not in globals():
    import sys

    sys.stderr.write(__doc__)
    sys.exit(1)

# Import base ASN.1 objects even if this MIB does not use it

(Integer,
 OctetString,
 ObjectIdentifier) = mibBuilder.importSymbols(
    "ASN1",
    "Integer",
    "OctetString",
    "ObjectIdentifier")

(NamedValues,) = mibBuilder.importSymbols(
    "ASN1-ENUMERATION",
    "NamedValues")
(ConstraintsIntersection,
 ConstraintsUnion,
 SingleValueConstraint,
 ValueRangeConstraint,
 ValueSizeConstraint) = mibBuilder.importSymbols(
    "ASN1-REFINEMENT",
    "ConstraintsIntersection",
    "ConstraintsUnion",
    "SingleValueConstraint",
    "ValueRangeConstraint",
    "ValueSizeConstraint")

# Import SMI symbols from the MIBs this MIB depends on

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(Bits,
 Counter32,
 Counter64,
 Gauge32,
 Integer32,
 IpAddress,
 ModuleIdentity,
 MibIdentifier,
 NotificationType,
 ObjectIdentity,
 MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn,
 NotificationType,
 TimeTicks,
 Unsigned32,
 enterprises,
 iso) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "Bits",
    "Counter32",
    "Counter64",
    "Gauge32",
    "Integer32",
    "IpAddress",
    "ModuleIdentity",
    "MibIdentifier",
    "NotificationType",
    "ObjectIdentity",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions



class DisplayString(OctetString):
    """Custom type DisplayString based on OctetString"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_QNAP_ObjectIdentity = ObjectIdentity
QNAP = _QNAP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 55062)
)
_QTS_ObjectIdentity = ObjectIdentity
QTS = _QTS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 55062, 1)
)
_System_ObjectIdentity = ObjectIdentity
system = _System_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 55062, 1, 12)
)
_SystemEventMsg_ObjectIdentity = ObjectIdentity
systemEventMsg = _SystemEventMsg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 55062, 1, 12, 1)
)
_EventInformMsg_Type = DisplayString
_EventInformMsg_Object = MibScalar
eventInformMsg = _EventInformMsg_Object(
    (1, 3, 6, 1, 4, 1, 55062, 1, 12, 1, 101),
    _EventInformMsg_Type()
)
eventInformMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventInformMsg.setStatus("current")
_EventWarningMsg_Type = DisplayString
_EventWarningMsg_Object = MibScalar
eventWarningMsg = _EventWarningMsg_Object(
    (1, 3, 6, 1, 4, 1, 55062, 1, 12, 1, 102),
    _EventWarningMsg_Type()
)
eventWarningMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventWarningMsg.setStatus("current")
_EventErrorMsg_Type = DisplayString
_EventErrorMsg_Object = MibScalar
eventErrorMsg = _EventErrorMsg_Object(
    (1, 3, 6, 1, 4, 1, 55062, 1, 12, 1, 103),
    _EventErrorMsg_Type()
)
eventErrorMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventErrorMsg.setStatus("current")
_SystemTraps_ObjectIdentity = ObjectIdentity
systemTraps = _SystemTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 55062, 1, 12, 2)
)
_SystemModel_Type = DisplayString
_SystemModel_Object = MibScalar
systemModel = _SystemModel_Object(
    (1, 3, 6, 1, 4, 1, 55062, 1, 12, 3),
    _SystemModel_Type()
)
systemModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemModel.setStatus("current")
_Hostname_Type = DisplayString
_Hostname_Object = MibScalar
hostname = _Hostname_Object(
    (1, 3, 6, 1, 4, 1, 55062, 1, 12, 4),
    _Hostname_Type()
)
hostname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostname.setStatus("current")


class _SerialNumber_Type(DisplayString):
    """Custom type serialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SerialNumber_Type.__name__ = "DisplayString"
_SerialNumber_Object = MibScalar
serialNumber = _SerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 55062, 1, 12, 5),
    _SerialNumber_Type()
)
serialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serialNumber.setStatus("current")
_FirmwareVersion_Type = DisplayString
_FirmwareVersion_Object = MibScalar
firmwareVersion = _FirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 55062, 1, 12, 6),
    _FirmwareVersion_Type()
)
firmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    firmwareVersion.setStatus("current")
_FirmwareUpgradeAvailable_Type = Integer32
_FirmwareUpgradeAvailable_Object = MibScalar
firmwareUpgradeAvailable = _FirmwareUpgradeAvailable_Object(
    (1, 3, 6, 1, 4, 1, 55062, 1, 12, 7),
    _FirmwareUpgradeAvailable_Type()
)
firmwareUpgradeAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    firmwareUpgradeAvailable.setStatus("current")
_SysFanNumber_Type = Integer32
_SysFanNumber_Object = MibScalar
sysFanNumber = _SysFanNumber_Object(
    (1, 3, 6, 1, 4, 1, 55062, 1, 12, 8),
    _SysFanNumber_Type()
)
sysFanNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysFanNumber.setStatus("current")
_SystemFanTable_Object = MibTable
systemFanTable = _SystemFanTable_Object(
    (1, 3, 6, 1, 4, 1, 55062, 1, 12, 9)
)
if mibBuilder.loadTexts:
    systemFanTable.setStatus("current")
_SysFanEntry_Object = MibTableRow
sysFanEntry = _SysFanEntry_Object(
    (1, 3, 6, 1, 4, 1, 55062, 1, 12, 9, 1)
)
sysFanEntry.setIndexNames(
    (0, "QTS-MIB", "sysFanIndex"),
)
if mibBuilder.loadTexts:
    sysFanEntry.setStatus("current")
_SysFanIndex_Type = Integer32
_SysFanIndex_Object = MibTableColumn
sysFanIndex = _SysFanIndex_Object(
    (1, 3, 6, 1, 4, 1, 55062, 1, 12, 9, 1, 1),
    _SysFanIndex_Type()
)
sysFanIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysFanIndex.setStatus("current")


class _SysFanDescr_Type(DisplayString):
    """Custom type sysFanDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SysFanDescr_Type.__name__ = "DisplayString"
_SysFanDescr_Object = MibTableColumn
sysFanDescr = _SysFanDescr_Object(
    (1, 3, 6, 1, 4, 1, 55062, 1, 12, 9, 1, 2),
    _SysFanDescr_Type()
)
sysFanDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysFanDescr.setStatus("current")
_SysFanSpeed_Type = Integer32
_SysFanSpeed_Object = MibTableColumn
sysFanSpeed = _SysFanSpeed_Object(
    (1, 3, 6, 1, 4, 1, 55062, 1, 12, 9, 1, 3),
    _SysFanSpeed_Type()
)
sysFanSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysFanSpeed.setStatus("current")
_CpuTemperature_Type = Integer32
_CpuTemperature_Object = MibScalar
cpuTemperature = _CpuTemperature_Object(
    (1, 3, 6, 1, 4, 1, 55062, 1, 12, 10),
    _CpuTemperature_Type()
)
cpuTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuTemperature.setStatus("current")
_SystemTemperature_Type = Integer32
_SystemTemperature_Object = MibScalar
systemTemperature = _SystemTemperature_Object(
    (1, 3, 6, 1, 4, 1, 55062, 1, 12, 11),
    _SystemTemperature_Type()
)
systemTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemTemperature.setStatus("current")
_SystemCPU_Usage_Type = Integer32
_SystemCPU_Usage_Object = MibScalar
systemCPU_Usage = _SystemCPU_Usage_Object(
    (1, 3, 6, 1, 4, 1, 55062, 1, 12, 12),
    _SystemCPU_Usage_Type()
)
systemCPU_Usage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemCPU_Usage.setStatus("current")
_SystemTotalMem_Type = Counter64
_SystemTotalMem_Object = MibScalar
systemTotalMem = _SystemTotalMem_Object(
    (1, 3, 6, 1, 4, 1, 55062, 1, 12, 13),
    _SystemTotalMem_Type()
)
systemTotalMem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemTotalMem.setStatus("current")
_SystemFreeMem_Type = Counter64
_SystemFreeMem_Object = MibScalar
systemFreeMem = _SystemFreeMem_Object(
    (1, 3, 6, 1, 4, 1, 55062, 1, 12, 14),
    _SystemFreeMem_Type()
)
systemFreeMem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemFreeMem.setStatus("current")
_SystemAvailableMem_Type = Counter64
_SystemAvailableMem_Object = MibScalar
systemAvailableMem = _SystemAvailableMem_Object(
    (1, 3, 6, 1, 4, 1, 55062, 1, 12, 15),
    _SystemAvailableMem_Type()
)
systemAvailableMem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemAvailableMem.setStatus("current")
_SystemUsedMemory_Type = Counter64
_SystemUsedMemory_Object = MibScalar
systemUsedMemory = _SystemUsedMemory_Object(
    (1, 3, 6, 1, 4, 1, 55062, 1, 12, 16),
    _SystemUsedMemory_Type()
)
systemUsedMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemUsedMemory.setStatus("current")
_SystemCacheMemory_Type = Counter64
_SystemCacheMemory_Object = MibScalar
systemCacheMemory = _SystemCacheMemory_Object(
    (1, 3, 6, 1, 4, 1, 55062, 1, 12, 17),
    _SystemCacheMemory_Type()
)
systemCacheMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemCacheMemory.setStatus("current")
_SystemBufferMemory_Type = Counter64
_SystemBufferMemory_Object = MibScalar
systemBufferMemory = _SystemBufferMemory_Object(
    (1, 3, 6, 1, 4, 1, 55062, 1, 12, 18),
    _SystemBufferMemory_Type()
)
systemBufferMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemBufferMemory.setStatus("current")


class _SysPowerStatus_Type(Integer32):
    """Custom type sysPowerStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0)
        )
    )
    namedValues = NamedValues(
        *(("failed", -1),
          ("ok", 0))
    )


_SysPowerStatus_Type.__name__ = "Integer32"
_SysPowerStatus_Object = MibScalar
sysPowerStatus = _SysPowerStatus_Object(
    (1, 3, 6, 1, 4, 1, 55062, 1, 12, 19),
    _SysPowerStatus_Type()
)
sysPowerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysPowerStatus.setStatus("current")
_SysUPSStatus_Type = Integer32
_SysUPSStatus_Object = MibScalar
sysUPSStatus = _SysUPSStatus_Object(
    (1, 3, 6, 1, 4, 1, 55062, 1, 12, 20),
    _SysUPSStatus_Type()
)
sysUPSStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysUPSStatus.setStatus("current")
_SysUptime_Type = TimeTicks
_SysUptime_Object = MibScalar
sysUptime = _SysUptime_Object(
    (1, 3, 6, 1, 4, 1, 55062, 1, 12, 21),
    _SysUptime_Type()
)
sysUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysUptime.setStatus("current")
_Services_ObjectIdentity = ObjectIdentity
services = _Services_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 55062, 1, 14)
)


class _NfsV2V3IsEnabled_Type(Integer32):
    """Custom type nfsV2V3IsEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_NfsV2V3IsEnabled_Type.__name__ = "Integer32"
_NfsV2V3IsEnabled_Object = MibScalar
nfsV2V3IsEnabled = _NfsV2V3IsEnabled_Object(
    (1, 3, 6, 1, 4, 1, 55062, 1, 14, 1),
    _NfsV2V3IsEnabled_Type()
)
nfsV2V3IsEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nfsV2V3IsEnabled.setStatus("current")


class _NfsV4IsEnabled_Type(Integer32):
    """Custom type nfsV4IsEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_NfsV4IsEnabled_Type.__name__ = "Integer32"
_NfsV4IsEnabled_Object = MibScalar
nfsV4IsEnabled = _NfsV4IsEnabled_Object(
    (1, 3, 6, 1, 4, 1, 55062, 1, 14, 2),
    _NfsV4IsEnabled_Type()
)
nfsV4IsEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nfsV4IsEnabled.setStatus("current")
_HttpPort_Type = Integer32
_HttpPort_Object = MibScalar
httpPort = _HttpPort_Object(
    (1, 3, 6, 1, 4, 1, 55062, 1, 14, 3),
    _HttpPort_Type()
)
httpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpPort.setStatus("current")
_HttpsPort_Type = Integer32
_HttpsPort_Object = MibScalar
httpsPort = _HttpsPort_Object(
    (1, 3, 6, 1, 4, 1, 55062, 1, 14, 4),
    _HttpsPort_Type()
)
httpsPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    httpsPort.setStatus("current")


class _SshIsEnabled_Type(Integer32):
    """Custom type sshIsEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_SshIsEnabled_Type.__name__ = "Integer32"
_SshIsEnabled_Object = MibScalar
sshIsEnabled = _SshIsEnabled_Object(
    (1, 3, 6, 1, 4, 1, 55062, 1, 14, 5),
    _SshIsEnabled_Type()
)
sshIsEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshIsEnabled.setStatus("current")


class _SshSFTPEnabled_Type(Integer32):
    """Custom type sshSFTPEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_SshSFTPEnabled_Type.__name__ = "Integer32"
_SshSFTPEnabled_Object = MibScalar
sshSFTPEnabled = _SshSFTPEnabled_Object(
    (1, 3, 6, 1, 4, 1, 55062, 1, 14, 6),
    _SshSFTPEnabled_Type()
)
sshSFTPEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshSFTPEnabled.setStatus("current")
_SshPortNumber_Type = Integer32
_SshPortNumber_Object = MibScalar
sshPortNumber = _SshPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 55062, 1, 14, 7),
    _SshPortNumber_Type()
)
sshPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshPortNumber.setStatus("current")


class _TelnetIsEnabled_Type(Integer32):
    """Custom type telnetIsEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_TelnetIsEnabled_Type.__name__ = "Integer32"
_TelnetIsEnabled_Object = MibScalar
telnetIsEnabled = _TelnetIsEnabled_Object(
    (1, 3, 6, 1, 4, 1, 55062, 1, 14, 8),
    _TelnetIsEnabled_Type()
)
telnetIsEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telnetIsEnabled.setStatus("current")
_TelnetPortNumber_Type = Integer32
_TelnetPortNumber_Object = MibScalar
telnetPortNumber = _TelnetPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 55062, 1, 14, 9),
    _TelnetPortNumber_Type()
)
telnetPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telnetPortNumber.setStatus("current")


class _FtpEnabled_Type(Integer32):
    """Custom type ftpEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_FtpEnabled_Type.__name__ = "Integer32"
_FtpEnabled_Object = MibScalar
ftpEnabled = _FtpEnabled_Object(
    (1, 3, 6, 1, 4, 1, 55062, 1, 14, 10),
    _FtpEnabled_Type()
)
ftpEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ftpEnabled.setStatus("current")


class _FtpProtocolStandardEnabled_Type(Integer32):
    """Custom type ftpProtocolStandardEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_FtpProtocolStandardEnabled_Type.__name__ = "Integer32"
_FtpProtocolStandardEnabled_Object = MibScalar
ftpProtocolStandardEnabled = _FtpProtocolStandardEnabled_Object(
    (1, 3, 6, 1, 4, 1, 55062, 1, 14, 11),
    _FtpProtocolStandardEnabled_Type()
)
ftpProtocolStandardEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ftpProtocolStandardEnabled.setStatus("current")


class _FtpProtocolSSL_TLSEnabled_Type(Integer32):
    """Custom type ftpProtocolSSL_TLSEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_FtpProtocolSSL_TLSEnabled_Type.__name__ = "Integer32"
_FtpProtocolSSL_TLSEnabled_Object = MibScalar
ftpProtocolSSL_TLSEnabled = _FtpProtocolSSL_TLSEnabled_Object(
    (1, 3, 6, 1, 4, 1, 55062, 1, 14, 12),
    _FtpProtocolSSL_TLSEnabled_Type()
)
ftpProtocolSSL_TLSEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ftpProtocolSSL_TLSEnabled.setStatus("current")
_FtpPortNumber_Type = Integer32
_FtpPortNumber_Object = MibScalar
ftpPortNumber = _FtpPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 55062, 1, 14, 13),
    _FtpPortNumber_Type()
)
ftpPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ftpPortNumber.setStatus("current")


class _FtpUnicodeSupportEnabled_Type(Integer32):
    """Custom type ftpUnicodeSupportEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_FtpUnicodeSupportEnabled_Type.__name__ = "Integer32"
_FtpUnicodeSupportEnabled_Object = MibScalar
ftpUnicodeSupportEnabled = _FtpUnicodeSupportEnabled_Object(
    (1, 3, 6, 1, 4, 1, 55062, 1, 14, 14),
    _FtpUnicodeSupportEnabled_Type()
)
ftpUnicodeSupportEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ftpUnicodeSupportEnabled.setStatus("current")


class _FtpAnnonymousaccessEnabled_Type(Integer32):
    """Custom type ftpAnnonymousaccessEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_FtpAnnonymousaccessEnabled_Type.__name__ = "Integer32"
_FtpAnnonymousaccessEnabled_Object = MibScalar
ftpAnnonymousaccessEnabled = _FtpAnnonymousaccessEnabled_Object(
    (1, 3, 6, 1, 4, 1, 55062, 1, 14, 15),
    _FtpAnnonymousaccessEnabled_Type()
)
ftpAnnonymousaccessEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ftpAnnonymousaccessEnabled.setStatus("current")
_FtpMaxConnectionsAllowed_Type = Integer32
_FtpMaxConnectionsAllowed_Object = MibScalar
ftpMaxConnectionsAllowed = _FtpMaxConnectionsAllowed_Object(
    (1, 3, 6, 1, 4, 1, 55062, 1, 14, 16),
    _FtpMaxConnectionsAllowed_Type()
)
ftpMaxConnectionsAllowed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ftpMaxConnectionsAllowed.setStatus("current")
_FtpMaxConnectionsPerAccount_Type = Integer32
_FtpMaxConnectionsPerAccount_Object = MibScalar
ftpMaxConnectionsPerAccount = _FtpMaxConnectionsPerAccount_Object(
    (1, 3, 6, 1, 4, 1, 55062, 1, 14, 17),
    _FtpMaxConnectionsPerAccount_Type()
)
ftpMaxConnectionsPerAccount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ftpMaxConnectionsPerAccount.setStatus("current")


class _FtpMaxUploadRate_Type(Integer32):
    """Custom type ftpMaxUploadRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("unlimited", 0)
    )


_FtpMaxUploadRate_Type.__name__ = "Integer32"
_FtpMaxUploadRate_Object = MibScalar
ftpMaxUploadRate = _FtpMaxUploadRate_Object(
    (1, 3, 6, 1, 4, 1, 55062, 1, 14, 18),
    _FtpMaxUploadRate_Type()
)
ftpMaxUploadRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ftpMaxUploadRate.setStatus("current")


class _FtpMaxDownloadRate_Type(Integer32):
    """Custom type ftpMaxDownloadRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("unlimited", 0)
    )


_FtpMaxDownloadRate_Type.__name__ = "Integer32"
_FtpMaxDownloadRate_Object = MibScalar
ftpMaxDownloadRate = _FtpMaxDownloadRate_Object(
    (1, 3, 6, 1, 4, 1, 55062, 1, 14, 19),
    _FtpMaxDownloadRate_Type()
)
ftpMaxDownloadRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ftpMaxDownloadRate.setStatus("current")

# Managed Objects groups


# Notification objects

eventInform = NotificationType(
    (1, 3, 6, 1, 4, 1, 55062, 1, 12, 2, 1)
)
eventInform.setObjects(
    ("QTS-MIB", "eventInformMsg")
)
if mibBuilder.loadTexts:
    eventInform.setStatus(
        "current"
    )

eventWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 55062, 1, 12, 2, 2)
)
eventWarning.setObjects(
    ("QTS-MIB", "eventWarningMsg")
)
if mibBuilder.loadTexts:
    eventWarning.setStatus(
        "current"
    )

eventError = NotificationType(
    (1, 3, 6, 1, 4, 1, 55062, 1, 12, 2, 4)
)
eventError.setObjects(
    ("QTS-MIB", "eventErrorMsg")
)
if mibBuilder.loadTexts:
    eventError.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "QTS-MIB",
    **{"DisplayString": DisplayString,
       "QNAP": QNAP,
       "QTS": QTS,
       "system": system,
       "systemEventMsg": systemEventMsg,
       "eventInformMsg": eventInformMsg,
       "eventWarningMsg": eventWarningMsg,
       "eventErrorMsg": eventErrorMsg,
       "systemTraps": systemTraps,
       "eventInform": eventInform,
       "eventWarning": eventWarning,
       "eventError": eventError,
       "systemModel": systemModel,
       "hostname": hostname,
       "serialNumber": serialNumber,
       "firmwareVersion": firmwareVersion,
       "firmwareUpgradeAvailable": firmwareUpgradeAvailable,
       "sysFanNumber": sysFanNumber,
       "systemFanTable": systemFanTable,
       "sysFanEntry": sysFanEntry,
       "sysFanIndex": sysFanIndex,
       "sysFanDescr": sysFanDescr,
       "sysFanSpeed": sysFanSpeed,
       "cpuTemperature": cpuTemperature,
       "systemTemperature": systemTemperature,
       "systemCPU-Usage": systemCPU_Usage,
       "systemTotalMem": systemTotalMem,
       "systemFreeMem": systemFreeMem,
       "systemAvailableMem": systemAvailableMem,
       "systemUsedMemory": systemUsedMemory,
       "systemCacheMemory": systemCacheMemory,
       "systemBufferMemory": systemBufferMemory,
       "sysPowerStatus": sysPowerStatus,
       "sysUPSStatus": sysUPSStatus,
       "sysUptime": sysUptime,
       "services": services,
       "nfsV2V3IsEnabled": nfsV2V3IsEnabled,
       "nfsV4IsEnabled": nfsV4IsEnabled,
       "httpPort": httpPort,
       "httpsPort": httpsPort,
       "sshIsEnabled": sshIsEnabled,
       "sshSFTPEnabled": sshSFTPEnabled,
       "sshPortNumber": sshPortNumber,
       "telnetIsEnabled": telnetIsEnabled,
       "telnetPortNumber": telnetPortNumber,
       "ftpEnabled": ftpEnabled,
       "ftpProtocolStandardEnabled": ftpProtocolStandardEnabled,
       "ftpProtocolSSL-TLSEnabled": ftpProtocolSSL_TLSEnabled,
       "ftpPortNumber": ftpPortNumber,
       "ftpUnicodeSupportEnabled": ftpUnicodeSupportEnabled,
       "ftpAnnonymousaccessEnabled": ftpAnnonymousaccessEnabled,
       "ftpMaxConnectionsAllowed": ftpMaxConnectionsAllowed,
       "ftpMaxConnectionsPerAccount": ftpMaxConnectionsPerAccount,
       "ftpMaxUploadRate": ftpMaxUploadRate,
       "ftpMaxDownloadRate": ftpMaxDownloadRate}
)
