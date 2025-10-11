# SNMP MIB module (AUTO-CONFIGURATION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/raisecom/AUTO-CONFIGURATION-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:36:06 2025
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

(iscomSwitch,) = mibBuilder.importSymbols(
    "RAISECOM-BASE-MIB",
    "iscomSwitch")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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
 TimeTicks,
 Unsigned32,
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
    "TimeTicks",
    "Unsigned32",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")

(EnableVar,) = mibBuilder.importSymbols(
    "SWITCH-TC",
    "EnableVar")


# MODULE-IDENTITY

rcAutoConfig = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 28)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RcAutoConfigTftpServerAddress_Type = IpAddress
_RcAutoConfigTftpServerAddress_Object = MibScalar
rcAutoConfigTftpServerAddress = _RcAutoConfigTftpServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 28, 1),
    _RcAutoConfigTftpServerAddress_Type()
)
rcAutoConfigTftpServerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcAutoConfigTftpServerAddress.setStatus("current")


class _RcAutoConfigFileName_Type(OctetString):
    """Custom type rcAutoConfigFileName based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_RcAutoConfigFileName_Type.__name__ = "OctetString"
_RcAutoConfigFileName_Object = MibScalar
rcAutoConfigFileName = _RcAutoConfigFileName_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 28, 2),
    _RcAutoConfigFileName_Type()
)
rcAutoConfigFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcAutoConfigFileName.setStatus("current")


class _RcAutoConfigStartupEnable_Type(EnableVar):
    """Custom type rcAutoConfigStartupEnable based on EnableVar"""
    defaultValue = 2


_RcAutoConfigStartupEnable_Type.__name__ = "EnableVar"
_RcAutoConfigStartupEnable_Object = MibScalar
rcAutoConfigStartupEnable = _RcAutoConfigStartupEnable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 28, 3),
    _RcAutoConfigStartupEnable_Type()
)
rcAutoConfigStartupEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcAutoConfigStartupEnable.setStatus("current")


class _RcAutoConfigOverwriteEnable_Type(EnableVar):
    """Custom type rcAutoConfigOverwriteEnable based on EnableVar"""
    defaultValue = 2


_RcAutoConfigOverwriteEnable_Type.__name__ = "EnableVar"
_RcAutoConfigOverwriteEnable_Object = MibScalar
rcAutoConfigOverwriteEnable = _RcAutoConfigOverwriteEnable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 28, 4),
    _RcAutoConfigOverwriteEnable_Type()
)
rcAutoConfigOverwriteEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcAutoConfigOverwriteEnable.setStatus("current")


class _RcAutoConfigTrapEnable_Type(EnableVar):
    """Custom type rcAutoConfigTrapEnable based on EnableVar"""
    defaultValue = 2


_RcAutoConfigTrapEnable_Type.__name__ = "EnableVar"
_RcAutoConfigTrapEnable_Object = MibScalar
rcAutoConfigTrapEnable = _RcAutoConfigTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 28, 5),
    _RcAutoConfigTrapEnable_Type()
)
rcAutoConfigTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcAutoConfigTrapEnable.setStatus("current")


class _RcAutoConfigCommand_Type(Integer32):
    """Custom type rcAutoConfigCommand based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("start", 1),
          ("stop", 2))
    )


_RcAutoConfigCommand_Type.__name__ = "Integer32"
_RcAutoConfigCommand_Object = MibScalar
rcAutoConfigCommand = _RcAutoConfigCommand_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 28, 6),
    _RcAutoConfigCommand_Type()
)
rcAutoConfigCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcAutoConfigCommand.setStatus("deprecated")


class _RcAutoConfigOperationStates_Type(Integer32):
    """Custom type rcAutoConfigOperationStates based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("waiting", 1),
          ("getting", 2),
          ("loading", 3),
          ("writing", 4),
          ("done", 5))
    )


_RcAutoConfigOperationStates_Type.__name__ = "Integer32"
_RcAutoConfigOperationStates_Object = MibScalar
rcAutoConfigOperationStates = _RcAutoConfigOperationStates_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 28, 7),
    _RcAutoConfigOperationStates_Type()
)
rcAutoConfigOperationStates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcAutoConfigOperationStates.setStatus("current")


class _RcAutoConfigResult_Type(Integer32):
    """Custom type rcAutoConfigResult based on Integer32"""
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
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("succeeded", 2),
          ("ipAddressUnavailable", 3),
          ("acquireFailed", 4),
          ("getFailed", 5),
          ("writeFailed", 6),
          ("notEnoughMemory", 7),
          ("other", 8),
          ("stopped", 9))
    )


_RcAutoConfigResult_Type.__name__ = "Integer32"
_RcAutoConfigResult_Object = MibScalar
rcAutoConfigResult = _RcAutoConfigResult_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 28, 8),
    _RcAutoConfigResult_Type()
)
rcAutoConfigResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcAutoConfigResult.setStatus("current")
_RcAutoConfigTraps_ObjectIdentity = ObjectIdentity
rcAutoConfigTraps = _RcAutoConfigTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 28, 9)
)


class _RcAutoConfigFilenameRule_Type(Unsigned32):
    """Custom type rcAutoConfigFilenameRule based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(80000, 89999),
    )


_RcAutoConfigFilenameRule_Type.__name__ = "Unsigned32"
_RcAutoConfigFilenameRule_Object = MibScalar
rcAutoConfigFilenameRule = _RcAutoConfigFilenameRule_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 28, 10),
    _RcAutoConfigFilenameRule_Type()
)
rcAutoConfigFilenameRule.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcAutoConfigFilenameRule.setStatus("current")


class _RcAutoConfigSystemBootVersion_Type(OctetString):
    """Custom type rcAutoConfigSystemBootVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 7),
    )


_RcAutoConfigSystemBootVersion_Type.__name__ = "OctetString"
_RcAutoConfigSystemBootVersion_Object = MibScalar
rcAutoConfigSystemBootVersion = _RcAutoConfigSystemBootVersion_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 28, 11),
    _RcAutoConfigSystemBootVersion_Type()
)
rcAutoConfigSystemBootVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcAutoConfigSystemBootVersion.setStatus("current")


class _RcAutoConfigBootstrapVersion_Type(OctetString):
    """Custom type rcAutoConfigBootstrapVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 7),
    )


_RcAutoConfigBootstrapVersion_Type.__name__ = "OctetString"
_RcAutoConfigBootstrapVersion_Object = MibScalar
rcAutoConfigBootstrapVersion = _RcAutoConfigBootstrapVersion_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 28, 12),
    _RcAutoConfigBootstrapVersion_Type()
)
rcAutoConfigBootstrapVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcAutoConfigBootstrapVersion.setStatus("current")


class _RcAutoConfigStartupConfigVersion_Type(OctetString):
    """Custom type rcAutoConfigStartupConfigVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 7),
    )


_RcAutoConfigStartupConfigVersion_Type.__name__ = "OctetString"
_RcAutoConfigStartupConfigVersion_Object = MibScalar
rcAutoConfigStartupConfigVersion = _RcAutoConfigStartupConfigVersion_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 28, 13),
    _RcAutoConfigStartupConfigVersion_Type()
)
rcAutoConfigStartupConfigVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcAutoConfigStartupConfigVersion.setStatus("current")


class _RcAutoConfigEnable_Type(EnableVar):
    """Custom type rcAutoConfigEnable based on EnableVar"""
    defaultValue = 1


_RcAutoConfigEnable_Type.__name__ = "EnableVar"
_RcAutoConfigEnable_Object = MibScalar
rcAutoConfigEnable = _RcAutoConfigEnable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 28, 14),
    _RcAutoConfigEnable_Type()
)
rcAutoConfigEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcAutoConfigEnable.setStatus("current")


class _RcAutoConfigCurrentFileType_Type(Integer32):
    """Custom type rcAutoConfigCurrentFileType based on Integer32"""
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
          ("startup-config", 2),
          ("system-boot", 3),
          ("bootstrap", 4))
    )


_RcAutoConfigCurrentFileType_Type.__name__ = "Integer32"
_RcAutoConfigCurrentFileType_Object = MibScalar
rcAutoConfigCurrentFileType = _RcAutoConfigCurrentFileType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 28, 15),
    _RcAutoConfigCurrentFileType_Type()
)
rcAutoConfigCurrentFileType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcAutoConfigCurrentFileType.setStatus("current")


class _RcAutoConfigFilenamePrefix_Type(OctetString):
    """Custom type rcAutoConfigFilenamePrefix based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_RcAutoConfigFilenamePrefix_Type.__name__ = "OctetString"
_RcAutoConfigFilenamePrefix_Object = MibScalar
rcAutoConfigFilenamePrefix = _RcAutoConfigFilenamePrefix_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 28, 16),
    _RcAutoConfigFilenamePrefix_Type()
)
rcAutoConfigFilenamePrefix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcAutoConfigFilenamePrefix.setStatus("current")


class _RcAutoConfigFilenamePostfix_Type(OctetString):
    """Custom type rcAutoConfigFilenamePostfix based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_RcAutoConfigFilenamePostfix_Type.__name__ = "OctetString"
_RcAutoConfigFilenamePostfix_Object = MibScalar
rcAutoConfigFilenamePostfix = _RcAutoConfigFilenamePostfix_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 28, 17),
    _RcAutoConfigFilenamePostfix_Type()
)
rcAutoConfigFilenamePostfix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcAutoConfigFilenamePostfix.setStatus("current")


class _RcAutoConfigAccessType_Type(Integer32):
    """Custom type rcAutoConfigAccessType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("DHCPC", 2),
          ("Auto-provision", 3))
    )


_RcAutoConfigAccessType_Type.__name__ = "Integer32"
_RcAutoConfigAccessType_Object = MibScalar
rcAutoConfigAccessType = _RcAutoConfigAccessType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 28, 18),
    _RcAutoConfigAccessType_Type()
)
rcAutoConfigAccessType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcAutoConfigAccessType.setStatus("current")


class _RcAutoConfigStatus_Type(Integer32):
    """Custom type rcAutoConfigStatus based on Integer32"""
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
        *(("init", 1),
          ("management-access", 2),
          ("success", 3),
          ("fail", 4))
    )


_RcAutoConfigStatus_Type.__name__ = "Integer32"
_RcAutoConfigStatus_Object = MibScalar
rcAutoConfigStatus = _RcAutoConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 28, 19),
    _RcAutoConfigStatus_Type()
)
rcAutoConfigStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcAutoConfigStatus.setStatus("current")


class _RcAutoConfigLoadConfigStatus_Type(Integer32):
    """Custom type rcAutoConfigLoadConfigStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("success", 1),
          ("tftp-fail", 2),
          ("load-fail", 3),
          ("config-conflict", 4),
          ("write-fail", 5),
          ("format-fail", 6))
    )


_RcAutoConfigLoadConfigStatus_Type.__name__ = "Integer32"
_RcAutoConfigLoadConfigStatus_Object = MibScalar
rcAutoConfigLoadConfigStatus = _RcAutoConfigLoadConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 28, 20),
    _RcAutoConfigLoadConfigStatus_Type()
)
rcAutoConfigLoadConfigStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcAutoConfigLoadConfigStatus.setStatus("current")
_RcAutoConfigDhcpTftpAddress_Type = IpAddress
_RcAutoConfigDhcpTftpAddress_Object = MibScalar
rcAutoConfigDhcpTftpAddress = _RcAutoConfigDhcpTftpAddress_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 28, 21),
    _RcAutoConfigDhcpTftpAddress_Type()
)
rcAutoConfigDhcpTftpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcAutoConfigDhcpTftpAddress.setStatus("current")


class _RcAutoConfigErrorLineNum_Type(OctetString):
    """Custom type rcAutoConfigErrorLineNum based on OctetString"""
    defaultValue = OctetString("The configuration file line numbers which load failed.")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_RcAutoConfigErrorLineNum_Type.__name__ = "OctetString"
_RcAutoConfigErrorLineNum_Object = MibScalar
rcAutoConfigErrorLineNum = _RcAutoConfigErrorLineNum_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 28, 22),
    _RcAutoConfigErrorLineNum_Type()
)
rcAutoConfigErrorLineNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcAutoConfigErrorLineNum.setStatus("current")

# Managed Objects groups


# Notification objects

rcAutoConfigCompletionTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 28, 9, 1)
)
rcAutoConfigCompletionTrap.setObjects(
      *(("AUTO-CONFIGURATION-MIB", "rcAutoConfigCurrentFileType"),
        ("AUTO-CONFIGURATION-MIB", "rcAutoConfigResult"))
)
if mibBuilder.loadTexts:
    rcAutoConfigCompletionTrap.setStatus(
        "current"
    )

rcAutoConfigLoadFailTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 28, 9, 2)
)
if mibBuilder.loadTexts:
    rcAutoConfigLoadFailTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AUTO-CONFIGURATION-MIB",
    **{"rcAutoConfig": rcAutoConfig,
       "rcAutoConfigTftpServerAddress": rcAutoConfigTftpServerAddress,
       "rcAutoConfigFileName": rcAutoConfigFileName,
       "rcAutoConfigStartupEnable": rcAutoConfigStartupEnable,
       "rcAutoConfigOverwriteEnable": rcAutoConfigOverwriteEnable,
       "rcAutoConfigTrapEnable": rcAutoConfigTrapEnable,
       "rcAutoConfigCommand": rcAutoConfigCommand,
       "rcAutoConfigOperationStates": rcAutoConfigOperationStates,
       "rcAutoConfigResult": rcAutoConfigResult,
       "rcAutoConfigTraps": rcAutoConfigTraps,
       "rcAutoConfigCompletionTrap": rcAutoConfigCompletionTrap,
       "rcAutoConfigLoadFailTrap": rcAutoConfigLoadFailTrap,
       "rcAutoConfigFilenameRule": rcAutoConfigFilenameRule,
       "rcAutoConfigSystemBootVersion": rcAutoConfigSystemBootVersion,
       "rcAutoConfigBootstrapVersion": rcAutoConfigBootstrapVersion,
       "rcAutoConfigStartupConfigVersion": rcAutoConfigStartupConfigVersion,
       "rcAutoConfigEnable": rcAutoConfigEnable,
       "rcAutoConfigCurrentFileType": rcAutoConfigCurrentFileType,
       "rcAutoConfigFilenamePrefix": rcAutoConfigFilenamePrefix,
       "rcAutoConfigFilenamePostfix": rcAutoConfigFilenamePostfix,
       "rcAutoConfigAccessType": rcAutoConfigAccessType,
       "rcAutoConfigStatus": rcAutoConfigStatus,
       "rcAutoConfigLoadConfigStatus": rcAutoConfigLoadConfigStatus,
       "rcAutoConfigDhcpTftpAddress": rcAutoConfigDhcpTftpAddress,
       "rcAutoConfigErrorLineNum": rcAutoConfigErrorLineNum}
)
