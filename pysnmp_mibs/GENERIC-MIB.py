# SNMP MIB module (GENERIC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/radware/GENERIC-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:15:14 2025
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

(ipAddrEntry,) = mibBuilder.importSymbols(
    "IP-MIB",
    "ipAddrEntry")

(FeatureStatus,
 RowStatus,
 TruthValue,
 rndErrorDesc,
 rndErrorSeverity,
 rsGeneric,
 rsServerDispatcher,
 rsWSDSshParams,
 rsWSDTelnetParams,
 tftp) = mibBuilder.importSymbols(
    "RADWARE-MIB",
    "FeatureStatus",
    "RowStatus",
    "TruthValue",
    "rndErrorDesc",
    "rndErrorSeverity",
    "rsGeneric",
    "rsServerDispatcher",
    "rsWSDSshParams",
    "rsWSDTelnetParams",
    "tftp")

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



class DisplayStatus(Integer32):
    """Custom type DisplayStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("displayed", 1),
          ("hidden", 2))
    )





class NetNumber(OctetString):
    """Custom type NetNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4





class DpsSessionType(Integer32):
    """Custom type DpsSessionType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("ftpControl", 1),
          ("ftpData", 2),
          ("ftpAll", 3),
          ("tftpControl", 4),
          ("tftpData", 5),
          ("tftpAll", 6),
          ("rshellControl", 7),
          ("rshellErrors", 8),
          ("rshellAll", 9),
          ("rexecControl", 10),
          ("rexecErrors", 11),
          ("rexecAll", 12),
          ("h225Control", 13),
          ("h245Session", 14),
          ("h225All", 15),
          ("sipSignal", 16),
          ("sipMediaControl", 17),
          ("sipAudio", 18),
          ("sipVideo", 19),
          ("sipApplication", 20),
          ("sipOtherMediaType", 21),
          ("sipAll", 22))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RsSendSupportFile_Type = DisplayString
_RsSendSupportFile_Object = MibScalar
rsSendSupportFile = _RsSendSupportFile_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 5, 7),
    _RsSendSupportFile_Type()
)
rsSendSupportFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsSendSupportFile.setStatus("mandatory")


class _RsWSDTelnetSessionTimeout_Type(Integer32):
    """Custom type rsWSDTelnetSessionTimeout based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 120),
    )


_RsWSDTelnetSessionTimeout_Type.__name__ = "Integer32"
_RsWSDTelnetSessionTimeout_Object = MibScalar
rsWSDTelnetSessionTimeout = _RsWSDTelnetSessionTimeout_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 62, 3),
    _RsWSDTelnetSessionTimeout_Type()
)
rsWSDTelnetSessionTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDTelnetSessionTimeout.setStatus("mandatory")


class _RsWSDTelnetAuthenticationTimeout_Type(Integer32):
    """Custom type rsWSDTelnetAuthenticationTimeout based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 60),
    )


_RsWSDTelnetAuthenticationTimeout_Type.__name__ = "Integer32"
_RsWSDTelnetAuthenticationTimeout_Object = MibScalar
rsWSDTelnetAuthenticationTimeout = _RsWSDTelnetAuthenticationTimeout_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 62, 4),
    _RsWSDTelnetAuthenticationTimeout_Type()
)
rsWSDTelnetAuthenticationTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDTelnetAuthenticationTimeout.setStatus("mandatory")


class _RsWSDSshSessionTimeout_Type(Integer32):
    """Custom type rsWSDSshSessionTimeout based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 120),
    )


_RsWSDSshSessionTimeout_Type.__name__ = "Integer32"
_RsWSDSshSessionTimeout_Object = MibScalar
rsWSDSshSessionTimeout = _RsWSDSshSessionTimeout_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 80, 4),
    _RsWSDSshSessionTimeout_Type()
)
rsWSDSshSessionTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDSshSessionTimeout.setStatus("mandatory")


class _RsWSDSshAuthenticationTimeout_Type(Integer32):
    """Custom type rsWSDSshAuthenticationTimeout based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 60),
    )


_RsWSDSshAuthenticationTimeout_Type.__name__ = "Integer32"
_RsWSDSshAuthenticationTimeout_Object = MibScalar
rsWSDSshAuthenticationTimeout = _RsWSDSshAuthenticationTimeout_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 80, 5),
    _RsWSDSshAuthenticationTimeout_Type()
)
rsWSDSshAuthenticationTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDSshAuthenticationTimeout.setStatus("mandatory")


class _RsWSDSshManageAlgorithms_Type(DisplayString):
    """Custom type rsWSDSshManageAlgorithms based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 200),
    )


_RsWSDSshManageAlgorithms_Type.__name__ = "DisplayString"
_RsWSDSshManageAlgorithms_Object = MibScalar
rsWSDSshManageAlgorithms = _RsWSDSshManageAlgorithms_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 80, 6),
    _RsWSDSshManageAlgorithms_Type()
)
rsWSDSshManageAlgorithms.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsWSDSshManageAlgorithms.setStatus("mandatory")
_RsTunnelingMode_Type = FeatureStatus
_RsTunnelingMode_Object = MibScalar
rsTunnelingMode = _RsTunnelingMode_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 122, 1),
    _RsTunnelingMode_Type()
)
rsTunnelingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsTunnelingMode.setStatus("mandatory")


class _RsIpVersionMode_Type(Integer32):
    """Custom type rsIpVersionMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipv4", 1),
          ("ipv4and6", 2))
    )


_RsIpVersionMode_Type.__name__ = "Integer32"
_RsIpVersionMode_Object = MibScalar
rsIpVersionMode = _RsIpVersionMode_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 122, 2),
    _RsIpVersionMode_Type()
)
rsIpVersionMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsIpVersionMode.setStatus("mandatory")


class _DpFtpStatus_Type(FeatureStatus):
    """Custom type dpFtpStatus based on FeatureStatus"""
    defaultValue = 1


_DpFtpStatus_Type.__name__ = "FeatureStatus"
_DpFtpStatus_Object = MibScalar
dpFtpStatus = _DpFtpStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 122, 3),
    _DpFtpStatus_Type()
)
dpFtpStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpFtpStatus.setStatus("mandatory")


class _DpFtpControlAgingTime_Type(Integer32):
    """Custom type dpFtpControlAgingTime based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DpFtpControlAgingTime_Type.__name__ = "Integer32"
_DpFtpControlAgingTime_Object = MibScalar
dpFtpControlAgingTime = _DpFtpControlAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 122, 4),
    _DpFtpControlAgingTime_Type()
)
dpFtpControlAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpFtpControlAgingTime.setStatus("mandatory")


class _DpFtpDataAgingTime_Type(Integer32):
    """Custom type dpFtpDataAgingTime based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DpFtpDataAgingTime_Type.__name__ = "Integer32"
_DpFtpDataAgingTime_Object = MibScalar
dpFtpDataAgingTime = _DpFtpDataAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 122, 5),
    _DpFtpDataAgingTime_Type()
)
dpFtpDataAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpFtpDataAgingTime.setStatus("mandatory")


class _DpFtpControlPorts_Type(DisplayString):
    """Custom type dpFtpControlPorts based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 29),
    )


_DpFtpControlPorts_Type.__name__ = "DisplayString"
_DpFtpControlPorts_Object = MibScalar
dpFtpControlPorts = _DpFtpControlPorts_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 122, 6),
    _DpFtpControlPorts_Type()
)
dpFtpControlPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpFtpControlPorts.setStatus("mandatory")


class _DpTftpStatus_Type(FeatureStatus):
    """Custom type dpTftpStatus based on FeatureStatus"""
    defaultValue = 1


_DpTftpStatus_Type.__name__ = "FeatureStatus"
_DpTftpStatus_Object = MibScalar
dpTftpStatus = _DpTftpStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 122, 7),
    _DpTftpStatus_Type()
)
dpTftpStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpTftpStatus.setStatus("mandatory")


class _DpTftpDataAgingTime_Type(Integer32):
    """Custom type dpTftpDataAgingTime based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DpTftpDataAgingTime_Type.__name__ = "Integer32"
_DpTftpDataAgingTime_Object = MibScalar
dpTftpDataAgingTime = _DpTftpDataAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 122, 8),
    _DpTftpDataAgingTime_Type()
)
dpTftpDataAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpTftpDataAgingTime.setStatus("mandatory")


class _DpTftpControlPorts_Type(DisplayString):
    """Custom type dpTftpControlPorts based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 29),
    )


_DpTftpControlPorts_Type.__name__ = "DisplayString"
_DpTftpControlPorts_Object = MibScalar
dpTftpControlPorts = _DpTftpControlPorts_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 122, 9),
    _DpTftpControlPorts_Type()
)
dpTftpControlPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpTftpControlPorts.setStatus("mandatory")


class _DpRshellStatus_Type(FeatureStatus):
    """Custom type dpRshellStatus based on FeatureStatus"""
    defaultValue = 1


_DpRshellStatus_Type.__name__ = "FeatureStatus"
_DpRshellStatus_Object = MibScalar
dpRshellStatus = _DpRshellStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 122, 10),
    _DpRshellStatus_Type()
)
dpRshellStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpRshellStatus.setStatus("mandatory")


class _DpRshellControlAgingTime_Type(Integer32):
    """Custom type dpRshellControlAgingTime based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DpRshellControlAgingTime_Type.__name__ = "Integer32"
_DpRshellControlAgingTime_Object = MibScalar
dpRshellControlAgingTime = _DpRshellControlAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 122, 11),
    _DpRshellControlAgingTime_Type()
)
dpRshellControlAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpRshellControlAgingTime.setStatus("mandatory")


class _DpRshellDataAgingTime_Type(Integer32):
    """Custom type dpRshellDataAgingTime based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DpRshellDataAgingTime_Type.__name__ = "Integer32"
_DpRshellDataAgingTime_Object = MibScalar
dpRshellDataAgingTime = _DpRshellDataAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 122, 12),
    _DpRshellDataAgingTime_Type()
)
dpRshellDataAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpRshellDataAgingTime.setStatus("mandatory")


class _DpRshellControlPorts_Type(DisplayString):
    """Custom type dpRshellControlPorts based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 29),
    )


_DpRshellControlPorts_Type.__name__ = "DisplayString"
_DpRshellControlPorts_Object = MibScalar
dpRshellControlPorts = _DpRshellControlPorts_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 122, 13),
    _DpRshellControlPorts_Type()
)
dpRshellControlPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpRshellControlPorts.setStatus("mandatory")


class _DpRexecStatus_Type(FeatureStatus):
    """Custom type dpRexecStatus based on FeatureStatus"""
    defaultValue = 1


_DpRexecStatus_Type.__name__ = "FeatureStatus"
_DpRexecStatus_Object = MibScalar
dpRexecStatus = _DpRexecStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 122, 14),
    _DpRexecStatus_Type()
)
dpRexecStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpRexecStatus.setStatus("mandatory")


class _DpRexecControlAgingTime_Type(Integer32):
    """Custom type dpRexecControlAgingTime based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DpRexecControlAgingTime_Type.__name__ = "Integer32"
_DpRexecControlAgingTime_Object = MibScalar
dpRexecControlAgingTime = _DpRexecControlAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 122, 15),
    _DpRexecControlAgingTime_Type()
)
dpRexecControlAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpRexecControlAgingTime.setStatus("mandatory")


class _DpRexecDataAgingTime_Type(Integer32):
    """Custom type dpRexecDataAgingTime based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DpRexecDataAgingTime_Type.__name__ = "Integer32"
_DpRexecDataAgingTime_Object = MibScalar
dpRexecDataAgingTime = _DpRexecDataAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 122, 16),
    _DpRexecDataAgingTime_Type()
)
dpRexecDataAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpRexecDataAgingTime.setStatus("mandatory")


class _DpRexecControlPorts_Type(DisplayString):
    """Custom type dpRexecControlPorts based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 29),
    )


_DpRexecControlPorts_Type.__name__ = "DisplayString"
_DpRexecControlPorts_Object = MibScalar
dpRexecControlPorts = _DpRexecControlPorts_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 122, 17),
    _DpRexecControlPorts_Type()
)
dpRexecControlPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpRexecControlPorts.setStatus("mandatory")


class _DpH225Status_Type(FeatureStatus):
    """Custom type dpH225Status based on FeatureStatus"""
    defaultValue = 1


_DpH225Status_Type.__name__ = "FeatureStatus"
_DpH225Status_Object = MibScalar
dpH225Status = _DpH225Status_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 122, 18),
    _DpH225Status_Type()
)
dpH225Status.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpH225Status.setStatus("mandatory")


class _DpH225ControlAgingTime_Type(Integer32):
    """Custom type dpH225ControlAgingTime based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DpH225ControlAgingTime_Type.__name__ = "Integer32"
_DpH225ControlAgingTime_Object = MibScalar
dpH225ControlAgingTime = _DpH225ControlAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 122, 19),
    _DpH225ControlAgingTime_Type()
)
dpH225ControlAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpH225ControlAgingTime.setStatus("mandatory")


class _DpH225DataAgingTime_Type(Integer32):
    """Custom type dpH225DataAgingTime based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DpH225DataAgingTime_Type.__name__ = "Integer32"
_DpH225DataAgingTime_Object = MibScalar
dpH225DataAgingTime = _DpH225DataAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 122, 20),
    _DpH225DataAgingTime_Type()
)
dpH225DataAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpH225DataAgingTime.setStatus("mandatory")


class _DpH225ControlPorts_Type(DisplayString):
    """Custom type dpH225ControlPorts based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 29),
    )


_DpH225ControlPorts_Type.__name__ = "DisplayString"
_DpH225ControlPorts_Object = MibScalar
dpH225ControlPorts = _DpH225ControlPorts_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 122, 21),
    _DpH225ControlPorts_Type()
)
dpH225ControlPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpH225ControlPorts.setStatus("mandatory")
_RsGenericTuning_ObjectIdentity = ObjectIdentity
rsGenericTuning = _RsGenericTuning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 122, 22)
)
_DpsPendingTableTuning_ObjectIdentity = ObjectIdentity
dpsPendingTableTuning = _DpsPendingTableTuning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 122, 22, 1)
)
_DpsPendingTableEntries_Type = Integer32
_DpsPendingTableEntries_Object = MibScalar
dpsPendingTableEntries = _DpsPendingTableEntries_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 122, 22, 1, 1),
    _DpsPendingTableEntries_Type()
)
dpsPendingTableEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpsPendingTableEntries.setStatus("mandatory")
_DpsPendingTableEntriesAfterReset_Type = Integer32
_DpsPendingTableEntriesAfterReset_Object = MibScalar
dpsPendingTableEntriesAfterReset = _DpsPendingTableEntriesAfterReset_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 122, 22, 1, 2),
    _DpsPendingTableEntriesAfterReset_Type()
)
dpsPendingTableEntriesAfterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpsPendingTableEntriesAfterReset.setStatus("mandatory")
_DpsSIPCallTableTuning_ObjectIdentity = ObjectIdentity
dpsSIPCallTableTuning = _DpsSIPCallTableTuning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 122, 22, 2)
)
_DpSIPCallEntries_Type = Integer32
_DpSIPCallEntries_Object = MibScalar
dpSIPCallEntries = _DpSIPCallEntries_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 122, 22, 2, 1),
    _DpSIPCallEntries_Type()
)
dpSIPCallEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpSIPCallEntries.setStatus("mandatory")
_DpSIPCallEntriesAfterReset_Type = Integer32
_DpSIPCallEntriesAfterReset_Object = MibScalar
dpSIPCallEntriesAfterReset = _DpSIPCallEntriesAfterReset_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 122, 22, 2, 2),
    _DpSIPCallEntriesAfterReset_Type()
)
dpSIPCallEntriesAfterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpSIPCallEntriesAfterReset.setStatus("mandatory")
_DpsTCPSegmentsTableTuning_ObjectIdentity = ObjectIdentity
dpsTCPSegmentsTableTuning = _DpsTCPSegmentsTableTuning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 122, 22, 3)
)
_DpsTCPSegmentsTableEntries_Type = Integer32
_DpsTCPSegmentsTableEntries_Object = MibScalar
dpsTCPSegmentsTableEntries = _DpsTCPSegmentsTableEntries_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 122, 22, 3, 1),
    _DpsTCPSegmentsTableEntries_Type()
)
dpsTCPSegmentsTableEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpsTCPSegmentsTableEntries.setStatus("mandatory")
_DpsTCPSegmentsTableEntriesAfterReset_Type = Integer32
_DpsTCPSegmentsTableEntriesAfterReset_Object = MibScalar
dpsTCPSegmentsTableEntriesAfterReset = _DpsTCPSegmentsTableEntriesAfterReset_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 122, 22, 3, 2),
    _DpsTCPSegmentsTableEntriesAfterReset_Type()
)
dpsTCPSegmentsTableEntriesAfterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpsTCPSegmentsTableEntriesAfterReset.setStatus("mandatory")
_DpsRTSPControlTableTuning_ObjectIdentity = ObjectIdentity
dpsRTSPControlTableTuning = _DpsRTSPControlTableTuning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 122, 22, 4)
)
_DpsRTSPControlTableEntries_Type = Integer32
_DpsRTSPControlTableEntries_Object = MibScalar
dpsRTSPControlTableEntries = _DpsRTSPControlTableEntries_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 122, 22, 4, 1),
    _DpsRTSPControlTableEntries_Type()
)
dpsRTSPControlTableEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpsRTSPControlTableEntries.setStatus("mandatory")
_DpsRTSPControlTableEntriesAfterReset_Type = Integer32
_DpsRTSPControlTableEntriesAfterReset_Object = MibScalar
dpsRTSPControlTableEntriesAfterReset = _DpsRTSPControlTableEntriesAfterReset_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 122, 22, 4, 2),
    _DpsRTSPControlTableEntriesAfterReset_Type()
)
dpsRTSPControlTableEntriesAfterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpsRTSPControlTableEntriesAfterReset.setStatus("mandatory")
_RsDebugPoliciesTuning_ObjectIdentity = ObjectIdentity
rsDebugPoliciesTuning = _RsDebugPoliciesTuning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 122, 22, 5)
)
_RsDEBUGPolicyEntries_Type = Integer32
_RsDEBUGPolicyEntries_Object = MibScalar
rsDEBUGPolicyEntries = _RsDEBUGPolicyEntries_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 122, 22, 5, 1),
    _RsDEBUGPolicyEntries_Type()
)
rsDEBUGPolicyEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsDEBUGPolicyEntries.setStatus("mandatory")
_RsDEBUGPolicyEntriesAfterReset_Type = Integer32
_RsDEBUGPolicyEntriesAfterReset_Object = MibScalar
rsDEBUGPolicyEntriesAfterReset = _RsDEBUGPolicyEntriesAfterReset_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 122, 22, 5, 2),
    _RsDEBUGPolicyEntriesAfterReset_Type()
)
rsDEBUGPolicyEntriesAfterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsDEBUGPolicyEntriesAfterReset.setStatus("mandatory")
_RsIpFragmentTuning_ObjectIdentity = ObjectIdentity
rsIpFragmentTuning = _RsIpFragmentTuning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 122, 22, 6)
)
_RsIpFragmentTableEntries_Type = Integer32
_RsIpFragmentTableEntries_Object = MibScalar
rsIpFragmentTableEntries = _RsIpFragmentTableEntries_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 122, 22, 6, 1),
    _RsIpFragmentTableEntries_Type()
)
rsIpFragmentTableEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIpFragmentTableEntries.setStatus("mandatory")
_RsIpFragmentTableEntriesAfterReset_Type = Integer32
_RsIpFragmentTableEntriesAfterReset_Object = MibScalar
rsIpFragmentTableEntriesAfterReset = _RsIpFragmentTableEntriesAfterReset_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 122, 22, 6, 2),
    _RsIpFragmentTableEntriesAfterReset_Type()
)
rsIpFragmentTableEntriesAfterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsIpFragmentTableEntriesAfterReset.setStatus("mandatory")


class _DpSIPStatus_Type(FeatureStatus):
    """Custom type dpSIPStatus based on FeatureStatus"""
    defaultValue = 2


_DpSIPStatus_Type.__name__ = "FeatureStatus"
_DpSIPStatus_Object = MibScalar
dpSIPStatus = _DpSIPStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 122, 23),
    _DpSIPStatus_Type()
)
dpSIPStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpSIPStatus.setStatus("mandatory")


class _DpSIPSignalAgingTime_Type(Integer32):
    """Custom type dpSIPSignalAgingTime based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_DpSIPSignalAgingTime_Type.__name__ = "Integer32"
_DpSIPSignalAgingTime_Object = MibScalar
dpSIPSignalAgingTime = _DpSIPSignalAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 122, 24),
    _DpSIPSignalAgingTime_Type()
)
dpSIPSignalAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpSIPSignalAgingTime.setStatus("mandatory")


class _DpSIPRTCPAgingTime_Type(Integer32):
    """Custom type dpSIPRTCPAgingTime based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DpSIPRTCPAgingTime_Type.__name__ = "Integer32"
_DpSIPRTCPAgingTime_Object = MibScalar
dpSIPRTCPAgingTime = _DpSIPRTCPAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 122, 25),
    _DpSIPRTCPAgingTime_Type()
)
dpSIPRTCPAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpSIPRTCPAgingTime.setStatus("mandatory")


class _DpSIPControlPorts_Type(DisplayString):
    """Custom type dpSIPControlPorts based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 29),
    )


_DpSIPControlPorts_Type.__name__ = "DisplayString"
_DpSIPControlPorts_Object = MibScalar
dpSIPControlPorts = _DpSIPControlPorts_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 122, 26),
    _DpSIPControlPorts_Type()
)
dpSIPControlPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpSIPControlPorts.setStatus("mandatory")


class _DpsTCPSegmentAgingTime_Type(Integer32):
    """Custom type dpsTCPSegmentAgingTime based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DpsTCPSegmentAgingTime_Type.__name__ = "Integer32"
_DpsTCPSegmentAgingTime_Object = MibScalar
dpsTCPSegmentAgingTime = _DpsTCPSegmentAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 122, 27),
    _DpsTCPSegmentAgingTime_Type()
)
dpsTCPSegmentAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpsTCPSegmentAgingTime.setStatus("mandatory")


class _DpRTSPStatus_Type(FeatureStatus):
    """Custom type dpRTSPStatus based on FeatureStatus"""
    defaultValue = 2


_DpRTSPStatus_Type.__name__ = "FeatureStatus"
_DpRTSPStatus_Object = MibScalar
dpRTSPStatus = _DpRTSPStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 122, 28),
    _DpRTSPStatus_Type()
)
dpRTSPStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpRTSPStatus.setStatus("mandatory")


class _DpRTSPControlAgingTime_Type(Integer32):
    """Custom type dpRTSPControlAgingTime based on Integer32"""
    defaultValue = 3600

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DpRTSPControlAgingTime_Type.__name__ = "Integer32"
_DpRTSPControlAgingTime_Object = MibScalar
dpRTSPControlAgingTime = _DpRTSPControlAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 122, 29),
    _DpRTSPControlAgingTime_Type()
)
dpRTSPControlAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpRTSPControlAgingTime.setStatus("mandatory")


class _DpRTSPDataAgingTime_Type(Integer32):
    """Custom type dpRTSPDataAgingTime based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DpRTSPDataAgingTime_Type.__name__ = "Integer32"
_DpRTSPDataAgingTime_Object = MibScalar
dpRTSPDataAgingTime = _DpRTSPDataAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 122, 30),
    _DpRTSPDataAgingTime_Type()
)
dpRTSPDataAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpRTSPDataAgingTime.setStatus("mandatory")


class _DpRTSPControlPorts_Type(DisplayString):
    """Custom type dpRTSPControlPorts based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 29),
    )


_DpRTSPControlPorts_Type.__name__ = "DisplayString"
_DpRTSPControlPorts_Object = MibScalar
dpRTSPControlPorts = _DpRTSPControlPorts_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 122, 31),
    _DpRTSPControlPorts_Type()
)
dpRTSPControlPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpRTSPControlPorts.setStatus("mandatory")
_RsDEBUGPolicyTable_Object = MibTable
rsDEBUGPolicyTable = _RsDEBUGPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 122, 32)
)
if mibBuilder.loadTexts:
    rsDEBUGPolicyTable.setStatus("mandatory")
_RsDEBUGPolicyEntry_Object = MibTableRow
rsDEBUGPolicyEntry = _RsDEBUGPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 122, 32, 1)
)
rsDEBUGPolicyEntry.setIndexNames(
    (0, "GENERIC-MIB", "rsDEBUGPolicyName"),
)
if mibBuilder.loadTexts:
    rsDEBUGPolicyEntry.setStatus("mandatory")


class _RsDEBUGPolicyName_Type(DisplayString):
    """Custom type rsDEBUGPolicyName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_RsDEBUGPolicyName_Type.__name__ = "DisplayString"
_RsDEBUGPolicyName_Object = MibTableColumn
rsDEBUGPolicyName = _RsDEBUGPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 122, 32, 1, 1),
    _RsDEBUGPolicyName_Type()
)
rsDEBUGPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsDEBUGPolicyName.setStatus("mandatory")
_RsDEBUGPolicyIndex_Type = Integer32
_RsDEBUGPolicyIndex_Object = MibTableColumn
rsDEBUGPolicyIndex = _RsDEBUGPolicyIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 122, 32, 1, 2),
    _RsDEBUGPolicyIndex_Type()
)
rsDEBUGPolicyIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsDEBUGPolicyIndex.setStatus("mandatory")


class _RsDEBUGPolicyDescription_Type(DisplayString):
    """Custom type rsDEBUGPolicyDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_RsDEBUGPolicyDescription_Type.__name__ = "DisplayString"
_RsDEBUGPolicyDescription_Object = MibTableColumn
rsDEBUGPolicyDescription = _RsDEBUGPolicyDescription_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 122, 32, 1, 3),
    _RsDEBUGPolicyDescription_Type()
)
rsDEBUGPolicyDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsDEBUGPolicyDescription.setStatus("mandatory")


class _RsDEBUGPolicySource_Type(DisplayString):
    """Custom type rsDEBUGPolicySource based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_RsDEBUGPolicySource_Type.__name__ = "DisplayString"
_RsDEBUGPolicySource_Object = MibTableColumn
rsDEBUGPolicySource = _RsDEBUGPolicySource_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 122, 32, 1, 4),
    _RsDEBUGPolicySource_Type()
)
rsDEBUGPolicySource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsDEBUGPolicySource.setStatus("mandatory")


class _RsDEBUGPolicyDestination_Type(DisplayString):
    """Custom type rsDEBUGPolicyDestination based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_RsDEBUGPolicyDestination_Type.__name__ = "DisplayString"
_RsDEBUGPolicyDestination_Object = MibTableColumn
rsDEBUGPolicyDestination = _RsDEBUGPolicyDestination_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 122, 32, 1, 5),
    _RsDEBUGPolicyDestination_Type()
)
rsDEBUGPolicyDestination.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsDEBUGPolicyDestination.setStatus("mandatory")


class _RsDEBUGPolicyRXPortGroup_Type(DisplayString):
    """Custom type rsDEBUGPolicyRXPortGroup based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_RsDEBUGPolicyRXPortGroup_Type.__name__ = "DisplayString"
_RsDEBUGPolicyRXPortGroup_Object = MibTableColumn
rsDEBUGPolicyRXPortGroup = _RsDEBUGPolicyRXPortGroup_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 122, 32, 1, 6),
    _RsDEBUGPolicyRXPortGroup_Type()
)
rsDEBUGPolicyRXPortGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsDEBUGPolicyRXPortGroup.setStatus("mandatory")


class _RsDEBUGPolicyTXPortGroup_Type(DisplayString):
    """Custom type rsDEBUGPolicyTXPortGroup based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_RsDEBUGPolicyTXPortGroup_Type.__name__ = "DisplayString"
_RsDEBUGPolicyTXPortGroup_Object = MibTableColumn
rsDEBUGPolicyTXPortGroup = _RsDEBUGPolicyTXPortGroup_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 122, 32, 1, 7),
    _RsDEBUGPolicyTXPortGroup_Type()
)
rsDEBUGPolicyTXPortGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsDEBUGPolicyTXPortGroup.setStatus("mandatory")


class _RsDEBUGPolicyServiceType_Type(Integer32):
    """Custom type rsDEBUGPolicyServiceType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("basic-filter", 2),
          ("and-group", 3),
          ("or-group", 4))
    )


_RsDEBUGPolicyServiceType_Type.__name__ = "Integer32"
_RsDEBUGPolicyServiceType_Object = MibTableColumn
rsDEBUGPolicyServiceType = _RsDEBUGPolicyServiceType_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 122, 32, 1, 8),
    _RsDEBUGPolicyServiceType_Type()
)
rsDEBUGPolicyServiceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsDEBUGPolicyServiceType.setStatus("mandatory")


class _RsDEBUGPolicyService_Type(DisplayString):
    """Custom type rsDEBUGPolicyService based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_RsDEBUGPolicyService_Type.__name__ = "DisplayString"
_RsDEBUGPolicyService_Object = MibTableColumn
rsDEBUGPolicyService = _RsDEBUGPolicyService_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 122, 32, 1, 9),
    _RsDEBUGPolicyService_Type()
)
rsDEBUGPolicyService.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsDEBUGPolicyService.setStatus("mandatory")


class _RsDEBUGPolicyVlanTagGroupName_Type(DisplayString):
    """Custom type rsDEBUGPolicyVlanTagGroupName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_RsDEBUGPolicyVlanTagGroupName_Type.__name__ = "DisplayString"
_RsDEBUGPolicyVlanTagGroupName_Object = MibTableColumn
rsDEBUGPolicyVlanTagGroupName = _RsDEBUGPolicyVlanTagGroupName_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 122, 32, 1, 10),
    _RsDEBUGPolicyVlanTagGroupName_Type()
)
rsDEBUGPolicyVlanTagGroupName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsDEBUGPolicyVlanTagGroupName.setStatus("mandatory")


class _RsDEBUGPolicySrcMacGroupName_Type(DisplayString):
    """Custom type rsDEBUGPolicySrcMacGroupName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_RsDEBUGPolicySrcMacGroupName_Type.__name__ = "DisplayString"
_RsDEBUGPolicySrcMacGroupName_Object = MibTableColumn
rsDEBUGPolicySrcMacGroupName = _RsDEBUGPolicySrcMacGroupName_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 122, 32, 1, 11),
    _RsDEBUGPolicySrcMacGroupName_Type()
)
rsDEBUGPolicySrcMacGroupName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsDEBUGPolicySrcMacGroupName.setStatus("mandatory")


class _RsDEBUGPolicyDstMacGroupName_Type(DisplayString):
    """Custom type rsDEBUGPolicyDstMacGroupName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_RsDEBUGPolicyDstMacGroupName_Type.__name__ = "DisplayString"
_RsDEBUGPolicyDstMacGroupName_Object = MibTableColumn
rsDEBUGPolicyDstMacGroupName = _RsDEBUGPolicyDstMacGroupName_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 122, 32, 1, 12),
    _RsDEBUGPolicyDstMacGroupName_Type()
)
rsDEBUGPolicyDstMacGroupName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsDEBUGPolicyDstMacGroupName.setStatus("mandatory")


class _RsDEBUGPolicyIsSnp_Type(FeatureStatus):
    """Custom type rsDEBUGPolicyIsSnp based on FeatureStatus"""
    defaultValue = 1


_RsDEBUGPolicyIsSnp_Type.__name__ = "FeatureStatus"
_RsDEBUGPolicyIsSnp_Object = MibTableColumn
rsDEBUGPolicyIsSnp = _RsDEBUGPolicyIsSnp_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 122, 32, 1, 13),
    _RsDEBUGPolicyIsSnp_Type()
)
rsDEBUGPolicyIsSnp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsDEBUGPolicyIsSnp.setStatus("mandatory")


class _RsDEBUGPolicyIsTrace_Type(FeatureStatus):
    """Custom type rsDEBUGPolicyIsTrace based on FeatureStatus"""
    defaultValue = 1


_RsDEBUGPolicyIsTrace_Type.__name__ = "FeatureStatus"
_RsDEBUGPolicyIsTrace_Object = MibTableColumn
rsDEBUGPolicyIsTrace = _RsDEBUGPolicyIsTrace_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 122, 32, 1, 14),
    _RsDEBUGPolicyIsTrace_Type()
)
rsDEBUGPolicyIsTrace.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsDEBUGPolicyIsTrace.setStatus("mandatory")
_RsDEBUGPolicyPacketsMaxNum_Type = Integer32
_RsDEBUGPolicyPacketsMaxNum_Object = MibTableColumn
rsDEBUGPolicyPacketsMaxNum = _RsDEBUGPolicyPacketsMaxNum_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 122, 32, 1, 15),
    _RsDEBUGPolicyPacketsMaxNum_Type()
)
rsDEBUGPolicyPacketsMaxNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsDEBUGPolicyPacketsMaxNum.setStatus("mandatory")
_RsDEBUGPolicyPacketMaxLen_Type = Integer32
_RsDEBUGPolicyPacketMaxLen_Object = MibTableColumn
rsDEBUGPolicyPacketMaxLen = _RsDEBUGPolicyPacketMaxLen_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 122, 32, 1, 16),
    _RsDEBUGPolicyPacketMaxLen_Type()
)
rsDEBUGPolicyPacketMaxLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsDEBUGPolicyPacketMaxLen.setStatus("mandatory")
_RsDEBUGPolicyStatus_Type = RowStatus
_RsDEBUGPolicyStatus_Object = MibTableColumn
rsDEBUGPolicyStatus = _RsDEBUGPolicyStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 122, 32, 1, 17),
    _RsDEBUGPolicyStatus_Type()
)
rsDEBUGPolicyStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsDEBUGPolicyStatus.setStatus("mandatory")


class _RsDebugSnapshotStatus_Type(FeatureStatus):
    """Custom type rsDebugSnapshotStatus based on FeatureStatus"""
    defaultValue = 2


_RsDebugSnapshotStatus_Type.__name__ = "FeatureStatus"
_RsDebugSnapshotStatus_Object = MibScalar
rsDebugSnapshotStatus = _RsDebugSnapshotStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 122, 33),
    _RsDebugSnapshotStatus_Type()
)
rsDebugSnapshotStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsDebugSnapshotStatus.setStatus("mandatory")


class _RsDebugSnapshotOutputToFile_Type(Integer32):
    """Custom type rsDebugSnapshotOutputToFile based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ram-file", 1),
          ("ram", 2),
          ("none", 3))
    )


_RsDebugSnapshotOutputToFile_Type.__name__ = "Integer32"
_RsDebugSnapshotOutputToFile_Object = MibScalar
rsDebugSnapshotOutputToFile = _RsDebugSnapshotOutputToFile_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 122, 34),
    _RsDebugSnapshotOutputToFile_Type()
)
rsDebugSnapshotOutputToFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsDebugSnapshotOutputToFile.setStatus("mandatory")


class _RsDebugSnapshotOutputToTerm_Type(FeatureStatus):
    """Custom type rsDebugSnapshotOutputToTerm based on FeatureStatus"""
    defaultValue = 1


_RsDebugSnapshotOutputToTerm_Type.__name__ = "FeatureStatus"
_RsDebugSnapshotOutputToTerm_Object = MibScalar
rsDebugSnapshotOutputToTerm = _RsDebugSnapshotOutputToTerm_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 122, 35),
    _RsDebugSnapshotOutputToTerm_Type()
)
rsDebugSnapshotOutputToTerm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsDebugSnapshotOutputToTerm.setStatus("mandatory")


class _RsDebugSnapshotPortGroup_Type(Integer32):
    """Custom type rsDebugSnapshotPortGroup based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("on-management-ports", 1),
          ("on-data-ports", 2),
          ("on-management-and-data", 3))
    )


_RsDebugSnapshotPortGroup_Type.__name__ = "Integer32"
_RsDebugSnapshotPortGroup_Object = MibScalar
rsDebugSnapshotPortGroup = _RsDebugSnapshotPortGroup_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 122, 36),
    _RsDebugSnapshotPortGroup_Type()
)
rsDebugSnapshotPortGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsDebugSnapshotPortGroup.setStatus("mandatory")


class _RsDebugTraceStatus_Type(FeatureStatus):
    """Custom type rsDebugTraceStatus based on FeatureStatus"""
    defaultValue = 2


_RsDebugTraceStatus_Type.__name__ = "FeatureStatus"
_RsDebugTraceStatus_Object = MibScalar
rsDebugTraceStatus = _RsDebugTraceStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 122, 37),
    _RsDebugTraceStatus_Type()
)
rsDebugTraceStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsDebugTraceStatus.setStatus("mandatory")


class _RsDebugTraceOutputToFile_Type(Integer32):
    """Custom type rsDebugTraceOutputToFile based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ram-file", 1),
          ("ram", 2),
          ("none", 3))
    )


_RsDebugTraceOutputToFile_Type.__name__ = "Integer32"
_RsDebugTraceOutputToFile_Object = MibScalar
rsDebugTraceOutputToFile = _RsDebugTraceOutputToFile_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 122, 38),
    _RsDebugTraceOutputToFile_Type()
)
rsDebugTraceOutputToFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsDebugTraceOutputToFile.setStatus("mandatory")


class _RsDebugTraceOutputToTerm_Type(FeatureStatus):
    """Custom type rsDebugTraceOutputToTerm based on FeatureStatus"""
    defaultValue = 1


_RsDebugTraceOutputToTerm_Type.__name__ = "FeatureStatus"
_RsDebugTraceOutputToTerm_Object = MibScalar
rsDebugTraceOutputToTerm = _RsDebugTraceOutputToTerm_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 122, 39),
    _RsDebugTraceOutputToTerm_Type()
)
rsDebugTraceOutputToTerm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsDebugTraceOutputToTerm.setStatus("mandatory")


class _RsDebugTraceOutputToSysLog_Type(FeatureStatus):
    """Custom type rsDebugTraceOutputToSysLog based on FeatureStatus"""
    defaultValue = 1


_RsDebugTraceOutputToSysLog_Type.__name__ = "FeatureStatus"
_RsDebugTraceOutputToSysLog_Object = MibScalar
rsDebugTraceOutputToSysLog = _RsDebugTraceOutputToSysLog_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 122, 40),
    _RsDebugTraceOutputToSysLog_Type()
)
rsDebugTraceOutputToSysLog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsDebugTraceOutputToSysLog.setStatus("mandatory")


class _RsDebugTraceMsgFormatDate_Type(DisplayStatus):
    """Custom type rsDebugTraceMsgFormatDate based on DisplayStatus"""
    defaultValue = 1


_RsDebugTraceMsgFormatDate_Type.__name__ = "DisplayStatus"
_RsDebugTraceMsgFormatDate_Object = MibScalar
rsDebugTraceMsgFormatDate = _RsDebugTraceMsgFormatDate_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 122, 42),
    _RsDebugTraceMsgFormatDate_Type()
)
rsDebugTraceMsgFormatDate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsDebugTraceMsgFormatDate.setStatus("mandatory")


class _RsDebugTraceMsgFormatTime_Type(DisplayStatus):
    """Custom type rsDebugTraceMsgFormatTime based on DisplayStatus"""
    defaultValue = 1


_RsDebugTraceMsgFormatTime_Type.__name__ = "DisplayStatus"
_RsDebugTraceMsgFormatTime_Object = MibScalar
rsDebugTraceMsgFormatTime = _RsDebugTraceMsgFormatTime_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 122, 43),
    _RsDebugTraceMsgFormatTime_Type()
)
rsDebugTraceMsgFormatTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsDebugTraceMsgFormatTime.setStatus("mandatory")


class _RsDebugTraceMsgFormatPlatform_Type(DisplayStatus):
    """Custom type rsDebugTraceMsgFormatPlatform based on DisplayStatus"""
    defaultValue = 1


_RsDebugTraceMsgFormatPlatform_Type.__name__ = "DisplayStatus"
_RsDebugTraceMsgFormatPlatform_Object = MibScalar
rsDebugTraceMsgFormatPlatform = _RsDebugTraceMsgFormatPlatform_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 122, 44),
    _RsDebugTraceMsgFormatPlatform_Type()
)
rsDebugTraceMsgFormatPlatform.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsDebugTraceMsgFormatPlatform.setStatus("mandatory")


class _RsDebugTraceMsgFormatFile_Type(DisplayStatus):
    """Custom type rsDebugTraceMsgFormatFile based on DisplayStatus"""
    defaultValue = 1


_RsDebugTraceMsgFormatFile_Type.__name__ = "DisplayStatus"
_RsDebugTraceMsgFormatFile_Object = MibScalar
rsDebugTraceMsgFormatFile = _RsDebugTraceMsgFormatFile_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 122, 45),
    _RsDebugTraceMsgFormatFile_Type()
)
rsDebugTraceMsgFormatFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsDebugTraceMsgFormatFile.setStatus("mandatory")


class _RsDebugTraceMsgFormatLine_Type(DisplayStatus):
    """Custom type rsDebugTraceMsgFormatLine based on DisplayStatus"""
    defaultValue = 1


_RsDebugTraceMsgFormatLine_Type.__name__ = "DisplayStatus"
_RsDebugTraceMsgFormatLine_Object = MibScalar
rsDebugTraceMsgFormatLine = _RsDebugTraceMsgFormatLine_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 122, 46),
    _RsDebugTraceMsgFormatLine_Type()
)
rsDebugTraceMsgFormatLine.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsDebugTraceMsgFormatLine.setStatus("mandatory")


class _RsDebugTraceMsgFormatPcktId_Type(DisplayStatus):
    """Custom type rsDebugTraceMsgFormatPcktId based on DisplayStatus"""
    defaultValue = 1


_RsDebugTraceMsgFormatPcktId_Type.__name__ = "DisplayStatus"
_RsDebugTraceMsgFormatPcktId_Object = MibScalar
rsDebugTraceMsgFormatPcktId = _RsDebugTraceMsgFormatPcktId_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 122, 47),
    _RsDebugTraceMsgFormatPcktId_Type()
)
rsDebugTraceMsgFormatPcktId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsDebugTraceMsgFormatPcktId.setStatus("mandatory")


class _RsDebugTraceMsgFormatModule_Type(DisplayStatus):
    """Custom type rsDebugTraceMsgFormatModule based on DisplayStatus"""
    defaultValue = 1


_RsDebugTraceMsgFormatModule_Type.__name__ = "DisplayStatus"
_RsDebugTraceMsgFormatModule_Object = MibScalar
rsDebugTraceMsgFormatModule = _RsDebugTraceMsgFormatModule_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 122, 48),
    _RsDebugTraceMsgFormatModule_Type()
)
rsDebugTraceMsgFormatModule.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsDebugTraceMsgFormatModule.setStatus("mandatory")


class _RsDebugTraceMsgFormatTask_Type(DisplayStatus):
    """Custom type rsDebugTraceMsgFormatTask based on DisplayStatus"""
    defaultValue = 1


_RsDebugTraceMsgFormatTask_Type.__name__ = "DisplayStatus"
_RsDebugTraceMsgFormatTask_Object = MibScalar
rsDebugTraceMsgFormatTask = _RsDebugTraceMsgFormatTask_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 122, 49),
    _RsDebugTraceMsgFormatTask_Type()
)
rsDebugTraceMsgFormatTask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsDebugTraceMsgFormatTask.setStatus("mandatory")
_RsDebugTraceApplTable_Object = MibTable
rsDebugTraceApplTable = _RsDebugTraceApplTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 122, 50)
)
if mibBuilder.loadTexts:
    rsDebugTraceApplTable.setStatus("mandatory")
_RsDebugTraceApplEntry_Object = MibTableRow
rsDebugTraceApplEntry = _RsDebugTraceApplEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 122, 50, 1)
)
rsDebugTraceApplEntry.setIndexNames(
    (0, "GENERIC-MIB", "rsDebugTraceApplName"),
)
if mibBuilder.loadTexts:
    rsDebugTraceApplEntry.setStatus("mandatory")


class _RsDebugTraceApplName_Type(DisplayString):
    """Custom type rsDebugTraceApplName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_RsDebugTraceApplName_Type.__name__ = "DisplayString"
_RsDebugTraceApplName_Object = MibTableColumn
rsDebugTraceApplName = _RsDebugTraceApplName_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 122, 50, 1, 1),
    _RsDebugTraceApplName_Type()
)
rsDebugTraceApplName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsDebugTraceApplName.setStatus("mandatory")
_RsDebugTraceApplStatus_Type = FeatureStatus
_RsDebugTraceApplStatus_Object = MibTableColumn
rsDebugTraceApplStatus = _RsDebugTraceApplStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 122, 50, 1, 2),
    _RsDebugTraceApplStatus_Type()
)
rsDebugTraceApplStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsDebugTraceApplStatus.setStatus("mandatory")


class _RsDebugTraceApplSeverity_Type(Integer32):
    """Custom type rsDebugTraceApplSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("emergency", 1),
          ("alert", 2),
          ("critical", 3),
          ("error", 4),
          ("warning", 5),
          ("notice", 6),
          ("info", 7),
          ("debug", 8))
    )


_RsDebugTraceApplSeverity_Type.__name__ = "Integer32"
_RsDebugTraceApplSeverity_Object = MibTableColumn
rsDebugTraceApplSeverity = _RsDebugTraceApplSeverity_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 122, 50, 1, 3),
    _RsDebugTraceApplSeverity_Type()
)
rsDebugTraceApplSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsDebugTraceApplSeverity.setStatus("mandatory")


class _RsDebugSnapshotPoint_Type(Integer32):
    """Custom type rsDebugSnapshotPoint based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("on-packet-arrive", 1),
          ("on-packet-send", 2),
          ("both", 3),
          ("on-packet-arrive-inc-decrypt-unit", 4),
          ("on-packet-send-inc-decrypt-unit", 5),
          ("both-inc-decrypt-unit", 6),
          ("only-decrypt-unit", 7))
    )


_RsDebugSnapshotPoint_Type.__name__ = "Integer32"
_RsDebugSnapshotPoint_Object = MibScalar
rsDebugSnapshotPoint = _RsDebugSnapshotPoint_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 122, 51),
    _RsDebugSnapshotPoint_Type()
)
rsDebugSnapshotPoint.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsDebugSnapshotPoint.setStatus("mandatory")
_RsDebugFilesTable_Object = MibTable
rsDebugFilesTable = _RsDebugFilesTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 122, 52)
)
if mibBuilder.loadTexts:
    rsDebugFilesTable.setStatus("mandatory")
_RsDebugFileEntry_Object = MibTableRow
rsDebugFileEntry = _RsDebugFileEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 122, 52, 1)
)
rsDebugFileEntry.setIndexNames(
    (0, "GENERIC-MIB", "rsDebugFileName"),
)
if mibBuilder.loadTexts:
    rsDebugFileEntry.setStatus("mandatory")


class _RsDebugFileName_Type(DisplayString):
    """Custom type rsDebugFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 60),
    )


_RsDebugFileName_Type.__name__ = "DisplayString"
_RsDebugFileName_Object = MibTableColumn
rsDebugFileName = _RsDebugFileName_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 122, 52, 1, 1),
    _RsDebugFileName_Type()
)
rsDebugFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsDebugFileName.setStatus("mandatory")
_RsDebugFileSize_Type = Integer32
_RsDebugFileSize_Object = MibTableColumn
rsDebugFileSize = _RsDebugFileSize_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 122, 52, 1, 2),
    _RsDebugFileSize_Type()
)
rsDebugFileSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsDebugFileSize.setStatus("mandatory")
_RsDebugFileRowStatus_Type = RowStatus
_RsDebugFileRowStatus_Object = MibTableColumn
rsDebugFileRowStatus = _RsDebugFileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 122, 52, 1, 3),
    _RsDebugFileRowStatus_Type()
)
rsDebugFileRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsDebugFileRowStatus.setStatus("mandatory")
_RsDebugFileTFTPSendSrc_Type = DisplayString
_RsDebugFileTFTPSendSrc_Object = MibScalar
rsDebugFileTFTPSendSrc = _RsDebugFileTFTPSendSrc_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 122, 53),
    _RsDebugFileTFTPSendSrc_Type()
)
rsDebugFileTFTPSendSrc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsDebugFileTFTPSendSrc.setStatus("mandatory")
_RsDebugFileDelete_Type = DisplayString
_RsDebugFileDelete_Object = MibScalar
rsDebugFileDelete = _RsDebugFileDelete_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 122, 54),
    _RsDebugFileDelete_Type()
)
rsDebugFileDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsDebugFileDelete.setStatus("mandatory")
_RsIpFragment_ObjectIdentity = ObjectIdentity
rsIpFragment = _RsIpFragment_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 122, 55)
)


class _RsIpFragmentStatus_Type(FeatureStatus):
    """Custom type rsIpFragmentStatus based on FeatureStatus"""
    defaultValue = 1


_RsIpFragmentStatus_Type.__name__ = "FeatureStatus"
_RsIpFragmentStatus_Object = MibScalar
rsIpFragmentStatus = _RsIpFragmentStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 122, 55, 1),
    _RsIpFragmentStatus_Type()
)
rsIpFragmentStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsIpFragmentStatus.setStatus("mandatory")


class _RsIpFragmentQueuingLimit_Type(Integer32):
    """Custom type rsIpFragmentQueuingLimit based on Integer32"""
    defaultValue = 25

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_RsIpFragmentQueuingLimit_Type.__name__ = "Integer32"
_RsIpFragmentQueuingLimit_Object = MibScalar
rsIpFragmentQueuingLimit = _RsIpFragmentQueuingLimit_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 122, 55, 2),
    _RsIpFragmentQueuingLimit_Type()
)
rsIpFragmentQueuingLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsIpFragmentQueuingLimit.setStatus("mandatory")


class _RsIpFragmentAging_Type(Integer32):
    """Custom type rsIpFragmentAging based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_RsIpFragmentAging_Type.__name__ = "Integer32"
_RsIpFragmentAging_Object = MibScalar
rsIpFragmentAging = _RsIpFragmentAging_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 122, 55, 3),
    _RsIpFragmentAging_Type()
)
rsIpFragmentAging.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsIpFragmentAging.setStatus("mandatory")


class _RsIpFragmentForwardAgedPacket_Type(FeatureStatus):
    """Custom type rsIpFragmentForwardAgedPacket based on FeatureStatus"""
    defaultValue = 1


_RsIpFragmentForwardAgedPacket_Type.__name__ = "FeatureStatus"
_RsIpFragmentForwardAgedPacket_Object = MibScalar
rsIpFragmentForwardAgedPacket = _RsIpFragmentForwardAgedPacket_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 122, 55, 4),
    _RsIpFragmentForwardAgedPacket_Type()
)
rsIpFragmentForwardAgedPacket.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsIpFragmentForwardAgedPacket.setStatus("mandatory")


class _RsIpFragmentQueueingStatus_Type(FeatureStatus):
    """Custom type rsIpFragmentQueueingStatus based on FeatureStatus"""
    defaultValue = 1


_RsIpFragmentQueueingStatus_Type.__name__ = "FeatureStatus"
_RsIpFragmentQueueingStatus_Object = MibScalar
rsIpFragmentQueueingStatus = _RsIpFragmentQueueingStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 122, 55, 5),
    _RsIpFragmentQueueingStatus_Type()
)
rsIpFragmentQueueingStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsIpFragmentQueueingStatus.setStatus("mandatory")
_RsDebugFileTFTPSendDst_Type = DisplayString
_RsDebugFileTFTPSendDst_Object = MibScalar
rsDebugFileTFTPSendDst = _RsDebugFileTFTPSendDst_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 122, 56),
    _RsDebugFileTFTPSendDst_Type()
)
rsDebugFileTFTPSendDst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsDebugFileTFTPSendDst.setStatus("mandatory")
_RsDebugTraceApplTableInternal_Object = MibTable
rsDebugTraceApplTableInternal = _RsDebugTraceApplTableInternal_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 122, 57)
)
if mibBuilder.loadTexts:
    rsDebugTraceApplTableInternal.setStatus("mandatory")
_RsDebugTraceApplEntryInternal_Object = MibTableRow
rsDebugTraceApplEntryInternal = _RsDebugTraceApplEntryInternal_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 122, 57, 1)
)
rsDebugTraceApplEntryInternal.setIndexNames(
    (0, "GENERIC-MIB", "rsDebugTraceApplNameInternal"),
)
if mibBuilder.loadTexts:
    rsDebugTraceApplEntryInternal.setStatus("mandatory")


class _RsDebugTraceApplNameInternal_Type(DisplayString):
    """Custom type rsDebugTraceApplNameInternal based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_RsDebugTraceApplNameInternal_Type.__name__ = "DisplayString"
_RsDebugTraceApplNameInternal_Object = MibTableColumn
rsDebugTraceApplNameInternal = _RsDebugTraceApplNameInternal_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 122, 57, 1, 1),
    _RsDebugTraceApplNameInternal_Type()
)
rsDebugTraceApplNameInternal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsDebugTraceApplNameInternal.setStatus("mandatory")
_RsDebugTraceApplStatusInternal_Type = FeatureStatus
_RsDebugTraceApplStatusInternal_Object = MibTableColumn
rsDebugTraceApplStatusInternal = _RsDebugTraceApplStatusInternal_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 122, 57, 1, 2),
    _RsDebugTraceApplStatusInternal_Type()
)
rsDebugTraceApplStatusInternal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsDebugTraceApplStatusInternal.setStatus("mandatory")


class _RsDebugTraceApplSeverityInternal_Type(Integer32):
    """Custom type rsDebugTraceApplSeverityInternal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("emergency", 1),
          ("alert", 2),
          ("critical", 3),
          ("error", 4),
          ("warning", 5),
          ("notice", 6),
          ("info", 7),
          ("debug", 8))
    )


_RsDebugTraceApplSeverityInternal_Type.__name__ = "Integer32"
_RsDebugTraceApplSeverityInternal_Object = MibTableColumn
rsDebugTraceApplSeverityInternal = _RsDebugTraceApplSeverityInternal_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 122, 57, 1, 3),
    _RsDebugTraceApplSeverityInternal_Type()
)
rsDebugTraceApplSeverityInternal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsDebugTraceApplSeverityInternal.setStatus("mandatory")


class _RsDebugSnapshotMode_Type(Integer32):
    """Custom type rsDebugSnapshotMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("default", 1),
          ("lab", 2))
    )


_RsDebugSnapshotMode_Type.__name__ = "Integer32"
_RsDebugSnapshotMode_Object = MibScalar
rsDebugSnapshotMode = _RsDebugSnapshotMode_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 122, 58),
    _RsDebugSnapshotMode_Type()
)
rsDebugSnapshotMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsDebugSnapshotMode.setStatus("mandatory")
_RsPortsStatsTable_Object = MibTable
rsPortsStatsTable = _RsPortsStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 122, 59)
)
if mibBuilder.loadTexts:
    rsPortsStatsTable.setStatus("mandatory")
_RsPortStatsEntry_Object = MibTableRow
rsPortStatsEntry = _RsPortStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 122, 59, 1)
)
rsPortStatsEntry.setIndexNames(
    (0, "GENERIC-MIB", "rsPortStatsPortNumber"),
)
if mibBuilder.loadTexts:
    rsPortStatsEntry.setStatus("mandatory")
_RsPortStatsPortNumber_Type = Integer32
_RsPortStatsPortNumber_Object = MibTableColumn
rsPortStatsPortNumber = _RsPortStatsPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 122, 59, 1, 1),
    _RsPortStatsPortNumber_Type()
)
rsPortStatsPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsPortStatsPortNumber.setStatus("mandatory")
_RsPortStatsInOctetsPerSec_Type = Integer32
_RsPortStatsInOctetsPerSec_Object = MibTableColumn
rsPortStatsInOctetsPerSec = _RsPortStatsInOctetsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 122, 59, 1, 2),
    _RsPortStatsInOctetsPerSec_Type()
)
rsPortStatsInOctetsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsPortStatsInOctetsPerSec.setStatus("mandatory")
_RsPortStatsInPktsPerSec_Type = Integer32
_RsPortStatsInPktsPerSec_Object = MibTableColumn
rsPortStatsInPktsPerSec = _RsPortStatsInPktsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 122, 59, 1, 3),
    _RsPortStatsInPktsPerSec_Type()
)
rsPortStatsInPktsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsPortStatsInPktsPerSec.setStatus("mandatory")
_RsPortStatsInDiscardsPerSec_Type = Integer32
_RsPortStatsInDiscardsPerSec_Object = MibTableColumn
rsPortStatsInDiscardsPerSec = _RsPortStatsInDiscardsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 122, 59, 1, 4),
    _RsPortStatsInDiscardsPerSec_Type()
)
rsPortStatsInDiscardsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsPortStatsInDiscardsPerSec.setStatus("mandatory")
_RsPortStatsInErrorsPerSec_Type = Integer32
_RsPortStatsInErrorsPerSec_Object = MibTableColumn
rsPortStatsInErrorsPerSec = _RsPortStatsInErrorsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 122, 59, 1, 5),
    _RsPortStatsInErrorsPerSec_Type()
)
rsPortStatsInErrorsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsPortStatsInErrorsPerSec.setStatus("mandatory")
_RsPortStatsOutOctetsPerSec_Type = Integer32
_RsPortStatsOutOctetsPerSec_Object = MibTableColumn
rsPortStatsOutOctetsPerSec = _RsPortStatsOutOctetsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 122, 59, 1, 6),
    _RsPortStatsOutOctetsPerSec_Type()
)
rsPortStatsOutOctetsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsPortStatsOutOctetsPerSec.setStatus("mandatory")
_RsPortStatsOutPktsPerSec_Type = Integer32
_RsPortStatsOutPktsPerSec_Object = MibTableColumn
rsPortStatsOutPktsPerSec = _RsPortStatsOutPktsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 122, 59, 1, 7),
    _RsPortStatsOutPktsPerSec_Type()
)
rsPortStatsOutPktsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsPortStatsOutPktsPerSec.setStatus("mandatory")
_RsPortStatsOutDiscardsPerSec_Type = Integer32
_RsPortStatsOutDiscardsPerSec_Object = MibTableColumn
rsPortStatsOutDiscardsPerSec = _RsPortStatsOutDiscardsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 122, 59, 1, 8),
    _RsPortStatsOutDiscardsPerSec_Type()
)
rsPortStatsOutDiscardsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsPortStatsOutDiscardsPerSec.setStatus("mandatory")
_RsPortStatsOutErrorsPerSec_Type = Integer32
_RsPortStatsOutErrorsPerSec_Object = MibTableColumn
rsPortStatsOutErrorsPerSec = _RsPortStatsOutErrorsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 122, 59, 1, 9),
    _RsPortStatsOutErrorsPerSec_Type()
)
rsPortStatsOutErrorsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsPortStatsOutErrorsPerSec.setStatus("mandatory")
_RsPortStatsInMbitsPerSec_Type = Integer32
_RsPortStatsInMbitsPerSec_Object = MibTableColumn
rsPortStatsInMbitsPerSec = _RsPortStatsInMbitsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 122, 59, 1, 10),
    _RsPortStatsInMbitsPerSec_Type()
)
rsPortStatsInMbitsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsPortStatsInMbitsPerSec.setStatus("mandatory")
_RsPortStatsOutMbitsPerSec_Type = Integer32
_RsPortStatsOutMbitsPerSec_Object = MibTableColumn
rsPortStatsOutMbitsPerSec = _RsPortStatsOutMbitsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 122, 59, 1, 11),
    _RsPortStatsOutMbitsPerSec_Type()
)
rsPortStatsOutMbitsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsPortStatsOutMbitsPerSec.setStatus("mandatory")
_RsPortStatsTotalInOctetsPerSec_Type = Integer32
_RsPortStatsTotalInOctetsPerSec_Object = MibScalar
rsPortStatsTotalInOctetsPerSec = _RsPortStatsTotalInOctetsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 122, 60),
    _RsPortStatsTotalInOctetsPerSec_Type()
)
rsPortStatsTotalInOctetsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsPortStatsTotalInOctetsPerSec.setStatus("obsolete")
_RsPortStatsTotalInMbitsPerSec_Type = Integer32
_RsPortStatsTotalInMbitsPerSec_Object = MibScalar
rsPortStatsTotalInMbitsPerSec = _RsPortStatsTotalInMbitsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 122, 61),
    _RsPortStatsTotalInMbitsPerSec_Type()
)
rsPortStatsTotalInMbitsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsPortStatsTotalInMbitsPerSec.setStatus("mandatory")


class _RsDebugSnapshotRate_Type(Integer32):
    """Custom type rsDebugSnapshotRate based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_RsDebugSnapshotRate_Type.__name__ = "Integer32"
_RsDebugSnapshotRate_Object = MibScalar
rsDebugSnapshotRate = _RsDebugSnapshotRate_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 122, 62),
    _RsDebugSnapshotRate_Type()
)
rsDebugSnapshotRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsDebugSnapshotRate.setStatus("mandatory")
_RsTunnelingModeProtocolGre_Type = FeatureStatus
_RsTunnelingModeProtocolGre_Object = MibScalar
rsTunnelingModeProtocolGre = _RsTunnelingModeProtocolGre_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 122, 63),
    _RsTunnelingModeProtocolGre_Type()
)
rsTunnelingModeProtocolGre.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsTunnelingModeProtocolGre.setStatus("mandatory")
_RsTunnelingModeProtocolGtp_Type = FeatureStatus
_RsTunnelingModeProtocolGtp_Object = MibScalar
rsTunnelingModeProtocolGtp = _RsTunnelingModeProtocolGtp_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 122, 64),
    _RsTunnelingModeProtocolGtp_Type()
)
rsTunnelingModeProtocolGtp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsTunnelingModeProtocolGtp.setStatus("mandatory")
_RsTunnelingModeProtocolL2tp_Type = FeatureStatus
_RsTunnelingModeProtocolL2tp_Object = MibScalar
rsTunnelingModeProtocolL2tp = _RsTunnelingModeProtocolL2tp_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 122, 65),
    _RsTunnelingModeProtocolL2tp_Type()
)
rsTunnelingModeProtocolL2tp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsTunnelingModeProtocolL2tp.setStatus("mandatory")
_RsTunnelingModeProtocolVlan_Type = FeatureStatus
_RsTunnelingModeProtocolVlan_Object = MibScalar
rsTunnelingModeProtocolVlan = _RsTunnelingModeProtocolVlan_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 122, 66),
    _RsTunnelingModeProtocolVlan_Type()
)
rsTunnelingModeProtocolVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsTunnelingModeProtocolVlan.setStatus("mandatory")
_RsTunnelingModeProtocolIpInIp_Type = FeatureStatus
_RsTunnelingModeProtocolIpInIp_Object = MibScalar
rsTunnelingModeProtocolIpInIp = _RsTunnelingModeProtocolIpInIp_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 122, 67),
    _RsTunnelingModeProtocolIpInIp_Type()
)
rsTunnelingModeProtocolIpInIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsTunnelingModeProtocolIpInIp.setStatus("mandatory")
_RsTunnelingModeProtocolInner_Type = FeatureStatus
_RsTunnelingModeProtocolInner_Object = MibScalar
rsTunnelingModeProtocolInner = _RsTunnelingModeProtocolInner_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 122, 68),
    _RsTunnelingModeProtocolInner_Type()
)
rsTunnelingModeProtocolInner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsTunnelingModeProtocolInner.setStatus("mandatory")
_RsTunnelingModeProtocolIpsecBypass_Type = FeatureStatus
_RsTunnelingModeProtocolIpsecBypass_Object = MibScalar
rsTunnelingModeProtocolIpsecBypass = _RsTunnelingModeProtocolIpsecBypass_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 122, 69),
    _RsTunnelingModeProtocolIpsecBypass_Type()
)
rsTunnelingModeProtocolIpsecBypass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsTunnelingModeProtocolIpsecBypass.setStatus("mandatory")
_RdwrIntConfSyncConfigTimestamp_Type = Integer32
_RdwrIntConfSyncConfigTimestamp_Object = MibScalar
rdwrIntConfSyncConfigTimestamp = _RdwrIntConfSyncConfigTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 122, 70),
    _RdwrIntConfSyncConfigTimestamp_Type()
)
rdwrIntConfSyncConfigTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdwrIntConfSyncConfigTimestamp.setStatus("mandatory")
_RsDebugFilesFlashTable_Object = MibTable
rsDebugFilesFlashTable = _RsDebugFilesFlashTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 122, 71)
)
if mibBuilder.loadTexts:
    rsDebugFilesFlashTable.setStatus("mandatory")
_RsDebugFileFlashEntry_Object = MibTableRow
rsDebugFileFlashEntry = _RsDebugFileFlashEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 122, 71, 1)
)
rsDebugFileFlashEntry.setIndexNames(
    (0, "GENERIC-MIB", "rsDebugFileFlashName"),
)
if mibBuilder.loadTexts:
    rsDebugFileFlashEntry.setStatus("mandatory")


class _RsDebugFileFlashName_Type(DisplayString):
    """Custom type rsDebugFileFlashName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 60),
    )


_RsDebugFileFlashName_Type.__name__ = "DisplayString"
_RsDebugFileFlashName_Object = MibTableColumn
rsDebugFileFlashName = _RsDebugFileFlashName_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 122, 71, 1, 1),
    _RsDebugFileFlashName_Type()
)
rsDebugFileFlashName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsDebugFileFlashName.setStatus("mandatory")
_RsDebugFileFlashSize_Type = Integer32
_RsDebugFileFlashSize_Object = MibTableColumn
rsDebugFileFlashSize = _RsDebugFileFlashSize_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 122, 71, 1, 2),
    _RsDebugFileFlashSize_Type()
)
rsDebugFileFlashSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsDebugFileFlashSize.setStatus("mandatory")


class _RsDebugFileFlashPathSecret_Type(Integer32):
    """Custom type rsDebugFileFlashPathSecret based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ram", 1),
          ("flash", 2))
    )


_RsDebugFileFlashPathSecret_Type.__name__ = "Integer32"
_RsDebugFileFlashPathSecret_Object = MibTableColumn
rsDebugFileFlashPathSecret = _RsDebugFileFlashPathSecret_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 122, 71, 1, 3),
    _RsDebugFileFlashPathSecret_Type()
)
rsDebugFileFlashPathSecret.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsDebugFileFlashPathSecret.setStatus("mandatory")
_RsDebugFileFlashRowStatus_Type = RowStatus
_RsDebugFileFlashRowStatus_Object = MibTableColumn
rsDebugFileFlashRowStatus = _RsDebugFileFlashRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 122, 71, 1, 4),
    _RsDebugFileFlashRowStatus_Type()
)
rsDebugFileFlashRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsDebugFileFlashRowStatus.setStatus("mandatory")
_RsDebugFilesRamTable_Object = MibTable
rsDebugFilesRamTable = _RsDebugFilesRamTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 122, 72)
)
if mibBuilder.loadTexts:
    rsDebugFilesRamTable.setStatus("mandatory")
_RsDebugFileRamEntry_Object = MibTableRow
rsDebugFileRamEntry = _RsDebugFileRamEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 122, 72, 1)
)
rsDebugFileRamEntry.setIndexNames(
    (0, "GENERIC-MIB", "rsDebugFileRamName"),
)
if mibBuilder.loadTexts:
    rsDebugFileRamEntry.setStatus("mandatory")


class _RsDebugFileRamName_Type(DisplayString):
    """Custom type rsDebugFileRamName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 60),
    )


_RsDebugFileRamName_Type.__name__ = "DisplayString"
_RsDebugFileRamName_Object = MibTableColumn
rsDebugFileRamName = _RsDebugFileRamName_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 122, 72, 1, 1),
    _RsDebugFileRamName_Type()
)
rsDebugFileRamName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsDebugFileRamName.setStatus("mandatory")
_RsDebugFileRamSize_Type = Integer32
_RsDebugFileRamSize_Object = MibTableColumn
rsDebugFileRamSize = _RsDebugFileRamSize_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 122, 72, 1, 2),
    _RsDebugFileRamSize_Type()
)
rsDebugFileRamSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsDebugFileRamSize.setStatus("mandatory")


class _RsDebugFileRamPathSecret_Type(Integer32):
    """Custom type rsDebugFileRamPathSecret based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ram", 1),
          ("flash", 2))
    )


_RsDebugFileRamPathSecret_Type.__name__ = "Integer32"
_RsDebugFileRamPathSecret_Object = MibTableColumn
rsDebugFileRamPathSecret = _RsDebugFileRamPathSecret_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 122, 72, 1, 3),
    _RsDebugFileRamPathSecret_Type()
)
rsDebugFileRamPathSecret.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsDebugFileRamPathSecret.setStatus("mandatory")
_RsDebugFileRamRowStatus_Type = RowStatus
_RsDebugFileRamRowStatus_Object = MibTableColumn
rsDebugFileRamRowStatus = _RsDebugFileRamRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 122, 72, 1, 4),
    _RsDebugFileRamRowStatus_Type()
)
rsDebugFileRamRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsDebugFileRamRowStatus.setStatus("mandatory")


class _RsDiagPktCapGlobalStatus_Type(FeatureStatus):
    """Custom type rsDiagPktCapGlobalStatus based on FeatureStatus"""
    defaultValue = 1


_RsDiagPktCapGlobalStatus_Type.__name__ = "FeatureStatus"
_RsDiagPktCapGlobalStatus_Object = MibScalar
rsDiagPktCapGlobalStatus = _RsDiagPktCapGlobalStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 122, 73),
    _RsDiagPktCapGlobalStatus_Type()
)
rsDiagPktCapGlobalStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsDiagPktCapGlobalStatus.setStatus("mandatory")

# Managed Objects groups


# Notification objects

rsGenericTablesFull = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 122, 0, 1)
)
rsGenericTablesFull.setObjects(
      *(("RADWARE-MIB", "rndErrorDesc"),
        ("RADWARE-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    rsGenericTablesFull.setStatus(
        ""
    )

rsDebugTrace = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 122, 0, 2)
)
rsDebugTrace.setObjects(
      *(("RADWARE-MIB", "rndErrorDesc"),
        ("RADWARE-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    rsDebugTrace.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "GENERIC-MIB",
    **{"DisplayStatus": DisplayStatus,
       "NetNumber": NetNumber,
       "DpsSessionType": DpsSessionType,
       "rsSendSupportFile": rsSendSupportFile,
       "rsWSDTelnetSessionTimeout": rsWSDTelnetSessionTimeout,
       "rsWSDTelnetAuthenticationTimeout": rsWSDTelnetAuthenticationTimeout,
       "rsWSDSshSessionTimeout": rsWSDSshSessionTimeout,
       "rsWSDSshAuthenticationTimeout": rsWSDSshAuthenticationTimeout,
       "rsWSDSshManageAlgorithms": rsWSDSshManageAlgorithms,
       "rsGenericTablesFull": rsGenericTablesFull,
       "rsDebugTrace": rsDebugTrace,
       "rsTunnelingMode": rsTunnelingMode,
       "rsIpVersionMode": rsIpVersionMode,
       "dpFtpStatus": dpFtpStatus,
       "dpFtpControlAgingTime": dpFtpControlAgingTime,
       "dpFtpDataAgingTime": dpFtpDataAgingTime,
       "dpFtpControlPorts": dpFtpControlPorts,
       "dpTftpStatus": dpTftpStatus,
       "dpTftpDataAgingTime": dpTftpDataAgingTime,
       "dpTftpControlPorts": dpTftpControlPorts,
       "dpRshellStatus": dpRshellStatus,
       "dpRshellControlAgingTime": dpRshellControlAgingTime,
       "dpRshellDataAgingTime": dpRshellDataAgingTime,
       "dpRshellControlPorts": dpRshellControlPorts,
       "dpRexecStatus": dpRexecStatus,
       "dpRexecControlAgingTime": dpRexecControlAgingTime,
       "dpRexecDataAgingTime": dpRexecDataAgingTime,
       "dpRexecControlPorts": dpRexecControlPorts,
       "dpH225Status": dpH225Status,
       "dpH225ControlAgingTime": dpH225ControlAgingTime,
       "dpH225DataAgingTime": dpH225DataAgingTime,
       "dpH225ControlPorts": dpH225ControlPorts,
       "rsGenericTuning": rsGenericTuning,
       "dpsPendingTableTuning": dpsPendingTableTuning,
       "dpsPendingTableEntries": dpsPendingTableEntries,
       "dpsPendingTableEntriesAfterReset": dpsPendingTableEntriesAfterReset,
       "dpsSIPCallTableTuning": dpsSIPCallTableTuning,
       "dpSIPCallEntries": dpSIPCallEntries,
       "dpSIPCallEntriesAfterReset": dpSIPCallEntriesAfterReset,
       "dpsTCPSegmentsTableTuning": dpsTCPSegmentsTableTuning,
       "dpsTCPSegmentsTableEntries": dpsTCPSegmentsTableEntries,
       "dpsTCPSegmentsTableEntriesAfterReset": dpsTCPSegmentsTableEntriesAfterReset,
       "dpsRTSPControlTableTuning": dpsRTSPControlTableTuning,
       "dpsRTSPControlTableEntries": dpsRTSPControlTableEntries,
       "dpsRTSPControlTableEntriesAfterReset": dpsRTSPControlTableEntriesAfterReset,
       "rsDebugPoliciesTuning": rsDebugPoliciesTuning,
       "rsDEBUGPolicyEntries": rsDEBUGPolicyEntries,
       "rsDEBUGPolicyEntriesAfterReset": rsDEBUGPolicyEntriesAfterReset,
       "rsIpFragmentTuning": rsIpFragmentTuning,
       "rsIpFragmentTableEntries": rsIpFragmentTableEntries,
       "rsIpFragmentTableEntriesAfterReset": rsIpFragmentTableEntriesAfterReset,
       "dpSIPStatus": dpSIPStatus,
       "dpSIPSignalAgingTime": dpSIPSignalAgingTime,
       "dpSIPRTCPAgingTime": dpSIPRTCPAgingTime,
       "dpSIPControlPorts": dpSIPControlPorts,
       "dpsTCPSegmentAgingTime": dpsTCPSegmentAgingTime,
       "dpRTSPStatus": dpRTSPStatus,
       "dpRTSPControlAgingTime": dpRTSPControlAgingTime,
       "dpRTSPDataAgingTime": dpRTSPDataAgingTime,
       "dpRTSPControlPorts": dpRTSPControlPorts,
       "rsDEBUGPolicyTable": rsDEBUGPolicyTable,
       "rsDEBUGPolicyEntry": rsDEBUGPolicyEntry,
       "rsDEBUGPolicyName": rsDEBUGPolicyName,
       "rsDEBUGPolicyIndex": rsDEBUGPolicyIndex,
       "rsDEBUGPolicyDescription": rsDEBUGPolicyDescription,
       "rsDEBUGPolicySource": rsDEBUGPolicySource,
       "rsDEBUGPolicyDestination": rsDEBUGPolicyDestination,
       "rsDEBUGPolicyRXPortGroup": rsDEBUGPolicyRXPortGroup,
       "rsDEBUGPolicyTXPortGroup": rsDEBUGPolicyTXPortGroup,
       "rsDEBUGPolicyServiceType": rsDEBUGPolicyServiceType,
       "rsDEBUGPolicyService": rsDEBUGPolicyService,
       "rsDEBUGPolicyVlanTagGroupName": rsDEBUGPolicyVlanTagGroupName,
       "rsDEBUGPolicySrcMacGroupName": rsDEBUGPolicySrcMacGroupName,
       "rsDEBUGPolicyDstMacGroupName": rsDEBUGPolicyDstMacGroupName,
       "rsDEBUGPolicyIsSnp": rsDEBUGPolicyIsSnp,
       "rsDEBUGPolicyIsTrace": rsDEBUGPolicyIsTrace,
       "rsDEBUGPolicyPacketsMaxNum": rsDEBUGPolicyPacketsMaxNum,
       "rsDEBUGPolicyPacketMaxLen": rsDEBUGPolicyPacketMaxLen,
       "rsDEBUGPolicyStatus": rsDEBUGPolicyStatus,
       "rsDebugSnapshotStatus": rsDebugSnapshotStatus,
       "rsDebugSnapshotOutputToFile": rsDebugSnapshotOutputToFile,
       "rsDebugSnapshotOutputToTerm": rsDebugSnapshotOutputToTerm,
       "rsDebugSnapshotPortGroup": rsDebugSnapshotPortGroup,
       "rsDebugTraceStatus": rsDebugTraceStatus,
       "rsDebugTraceOutputToFile": rsDebugTraceOutputToFile,
       "rsDebugTraceOutputToTerm": rsDebugTraceOutputToTerm,
       "rsDebugTraceOutputToSysLog": rsDebugTraceOutputToSysLog,
       "rsDebugTraceMsgFormatDate": rsDebugTraceMsgFormatDate,
       "rsDebugTraceMsgFormatTime": rsDebugTraceMsgFormatTime,
       "rsDebugTraceMsgFormatPlatform": rsDebugTraceMsgFormatPlatform,
       "rsDebugTraceMsgFormatFile": rsDebugTraceMsgFormatFile,
       "rsDebugTraceMsgFormatLine": rsDebugTraceMsgFormatLine,
       "rsDebugTraceMsgFormatPcktId": rsDebugTraceMsgFormatPcktId,
       "rsDebugTraceMsgFormatModule": rsDebugTraceMsgFormatModule,
       "rsDebugTraceMsgFormatTask": rsDebugTraceMsgFormatTask,
       "rsDebugTraceApplTable": rsDebugTraceApplTable,
       "rsDebugTraceApplEntry": rsDebugTraceApplEntry,
       "rsDebugTraceApplName": rsDebugTraceApplName,
       "rsDebugTraceApplStatus": rsDebugTraceApplStatus,
       "rsDebugTraceApplSeverity": rsDebugTraceApplSeverity,
       "rsDebugSnapshotPoint": rsDebugSnapshotPoint,
       "rsDebugFilesTable": rsDebugFilesTable,
       "rsDebugFileEntry": rsDebugFileEntry,
       "rsDebugFileName": rsDebugFileName,
       "rsDebugFileSize": rsDebugFileSize,
       "rsDebugFileRowStatus": rsDebugFileRowStatus,
       "rsDebugFileTFTPSendSrc": rsDebugFileTFTPSendSrc,
       "rsDebugFileDelete": rsDebugFileDelete,
       "rsIpFragment": rsIpFragment,
       "rsIpFragmentStatus": rsIpFragmentStatus,
       "rsIpFragmentQueuingLimit": rsIpFragmentQueuingLimit,
       "rsIpFragmentAging": rsIpFragmentAging,
       "rsIpFragmentForwardAgedPacket": rsIpFragmentForwardAgedPacket,
       "rsIpFragmentQueueingStatus": rsIpFragmentQueueingStatus,
       "rsDebugFileTFTPSendDst": rsDebugFileTFTPSendDst,
       "rsDebugTraceApplTableInternal": rsDebugTraceApplTableInternal,
       "rsDebugTraceApplEntryInternal": rsDebugTraceApplEntryInternal,
       "rsDebugTraceApplNameInternal": rsDebugTraceApplNameInternal,
       "rsDebugTraceApplStatusInternal": rsDebugTraceApplStatusInternal,
       "rsDebugTraceApplSeverityInternal": rsDebugTraceApplSeverityInternal,
       "rsDebugSnapshotMode": rsDebugSnapshotMode,
       "rsPortsStatsTable": rsPortsStatsTable,
       "rsPortStatsEntry": rsPortStatsEntry,
       "rsPortStatsPortNumber": rsPortStatsPortNumber,
       "rsPortStatsInOctetsPerSec": rsPortStatsInOctetsPerSec,
       "rsPortStatsInPktsPerSec": rsPortStatsInPktsPerSec,
       "rsPortStatsInDiscardsPerSec": rsPortStatsInDiscardsPerSec,
       "rsPortStatsInErrorsPerSec": rsPortStatsInErrorsPerSec,
       "rsPortStatsOutOctetsPerSec": rsPortStatsOutOctetsPerSec,
       "rsPortStatsOutPktsPerSec": rsPortStatsOutPktsPerSec,
       "rsPortStatsOutDiscardsPerSec": rsPortStatsOutDiscardsPerSec,
       "rsPortStatsOutErrorsPerSec": rsPortStatsOutErrorsPerSec,
       "rsPortStatsInMbitsPerSec": rsPortStatsInMbitsPerSec,
       "rsPortStatsOutMbitsPerSec": rsPortStatsOutMbitsPerSec,
       "rsPortStatsTotalInOctetsPerSec": rsPortStatsTotalInOctetsPerSec,
       "rsPortStatsTotalInMbitsPerSec": rsPortStatsTotalInMbitsPerSec,
       "rsDebugSnapshotRate": rsDebugSnapshotRate,
       "rsTunnelingModeProtocolGre": rsTunnelingModeProtocolGre,
       "rsTunnelingModeProtocolGtp": rsTunnelingModeProtocolGtp,
       "rsTunnelingModeProtocolL2tp": rsTunnelingModeProtocolL2tp,
       "rsTunnelingModeProtocolVlan": rsTunnelingModeProtocolVlan,
       "rsTunnelingModeProtocolIpInIp": rsTunnelingModeProtocolIpInIp,
       "rsTunnelingModeProtocolInner": rsTunnelingModeProtocolInner,
       "rsTunnelingModeProtocolIpsecBypass": rsTunnelingModeProtocolIpsecBypass,
       "rdwrIntConfSyncConfigTimestamp": rdwrIntConfSyncConfigTimestamp,
       "rsDebugFilesFlashTable": rsDebugFilesFlashTable,
       "rsDebugFileFlashEntry": rsDebugFileFlashEntry,
       "rsDebugFileFlashName": rsDebugFileFlashName,
       "rsDebugFileFlashSize": rsDebugFileFlashSize,
       "rsDebugFileFlashPathSecret": rsDebugFileFlashPathSecret,
       "rsDebugFileFlashRowStatus": rsDebugFileFlashRowStatus,
       "rsDebugFilesRamTable": rsDebugFilesRamTable,
       "rsDebugFileRamEntry": rsDebugFileRamEntry,
       "rsDebugFileRamName": rsDebugFileRamName,
       "rsDebugFileRamSize": rsDebugFileRamSize,
       "rsDebugFileRamPathSecret": rsDebugFileRamPathSecret,
       "rsDebugFileRamRowStatus": rsDebugFileRamRowStatus,
       "rsDiagPktCapGlobalStatus": rsDiagPktCapGlobalStatus}
)
