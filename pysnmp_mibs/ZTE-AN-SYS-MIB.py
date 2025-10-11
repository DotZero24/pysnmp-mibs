# SNMP MIB module (ZTE-AN-SYS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/zte/ZTE-AN-SYS-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:45:23 2025
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

(InetAddress,
 InetAddressPrefixLength,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressPrefixLength",
    "InetAddressType")

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
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")

(ZxAnIfindex,
 zxAn) = mibBuilder.importSymbols(
    "ZTE-AN-TC-MIB",
    "ZxAnIfindex",
    "zxAn")


# MODULE-IDENTITY

zxAnSysMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ZxAnSysObjects_ObjectIdentity = ObjectIdentity
zxAnSysObjects = _ZxAnSysObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1)
)


class _ZxAnSnmpSetCmdErrCode_Type(Integer32):
    """Custom type zxAnSnmpSetCmdErrCode based on Integer32"""
    defaultValue = 0


_ZxAnSnmpSetCmdErrCode_Type.__name__ = "Integer32"
_ZxAnSnmpSetCmdErrCode_Object = MibScalar
zxAnSnmpSetCmdErrCode = _ZxAnSnmpSetCmdErrCode_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 2),
    _ZxAnSnmpSetCmdErrCode_Type()
)
zxAnSnmpSetCmdErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSnmpSetCmdErrCode.setStatus("current")
_ZxAnSysSecMgmt_ObjectIdentity = ObjectIdentity
zxAnSysSecMgmt = _ZxAnSysSecMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 3)
)


class _ZxAnCliCrftTerminalEnable_Type(Integer32):
    """Custom type zxAnCliCrftTerminalEnable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_ZxAnCliCrftTerminalEnable_Type.__name__ = "Integer32"
_ZxAnCliCrftTerminalEnable_Object = MibScalar
zxAnCliCrftTerminalEnable = _ZxAnCliCrftTerminalEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 3, 1),
    _ZxAnCliCrftTerminalEnable_Type()
)
zxAnCliCrftTerminalEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnCliCrftTerminalEnable.setStatus("current")


class _ZxAnCliSecurityLevel_Type(Integer32):
    """Custom type zxAnCliSecurityLevel based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("guest", 1),
          ("administrator", 2))
    )


_ZxAnCliSecurityLevel_Type.__name__ = "Integer32"
_ZxAnCliSecurityLevel_Object = MibScalar
zxAnCliSecurityLevel = _ZxAnCliSecurityLevel_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 3, 2),
    _ZxAnCliSecurityLevel_Type()
)
zxAnCliSecurityLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnCliSecurityLevel.setStatus("current")


class _ZxAnCliCrftTerminalLoginStatus_Type(Integer32):
    """Custom type zxAnCliCrftTerminalLoginStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("logon", 1),
          ("logout", 2))
    )


_ZxAnCliCrftTerminalLoginStatus_Type.__name__ = "Integer32"
_ZxAnCliCrftTerminalLoginStatus_Object = MibScalar
zxAnCliCrftTerminalLoginStatus = _ZxAnCliCrftTerminalLoginStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 3, 3),
    _ZxAnCliCrftTerminalLoginStatus_Type()
)
zxAnCliCrftTerminalLoginStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCliCrftTerminalLoginStatus.setStatus("current")


class _ZxAnCliCrftTerminalLastLoginType_Type(Integer32):
    """Custom type zxAnCliCrftTerminalLastLoginType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("rs232SerialInterface", 1),
          ("outbandMgmtInterface", 2),
          ("inbandMgmtInterface", 3))
    )


_ZxAnCliCrftTerminalLastLoginType_Type.__name__ = "Integer32"
_ZxAnCliCrftTerminalLastLoginType_Object = MibScalar
zxAnCliCrftTerminalLastLoginType = _ZxAnCliCrftTerminalLastLoginType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 3, 4),
    _ZxAnCliCrftTerminalLastLoginType_Type()
)
zxAnCliCrftTerminalLastLoginType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCliCrftTerminalLastLoginType.setStatus("current")


class _ZxAnCliPromptName_Type(DisplayString):
    """Custom type zxAnCliPromptName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_ZxAnCliPromptName_Type.__name__ = "DisplayString"
_ZxAnCliPromptName_Object = MibScalar
zxAnCliPromptName = _ZxAnCliPromptName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 3, 5),
    _ZxAnCliPromptName_Type()
)
zxAnCliPromptName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnCliPromptName.setStatus("current")


class _ZxAnCliSuperUserName_Type(DisplayString):
    """Custom type zxAnCliSuperUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_ZxAnCliSuperUserName_Type.__name__ = "DisplayString"
_ZxAnCliSuperUserName_Object = MibScalar
zxAnCliSuperUserName = _ZxAnCliSuperUserName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 3, 6),
    _ZxAnCliSuperUserName_Type()
)
zxAnCliSuperUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCliSuperUserName.setStatus("current")


class _ZxAnCliSuperUserPwd_Type(DisplayString):
    """Custom type zxAnCliSuperUserPwd based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_ZxAnCliSuperUserPwd_Type.__name__ = "DisplayString"
_ZxAnCliSuperUserPwd_Object = MibScalar
zxAnCliSuperUserPwd = _ZxAnCliSuperUserPwd_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 3, 7),
    _ZxAnCliSuperUserPwd_Type()
)
zxAnCliSuperUserPwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCliSuperUserPwd.setStatus("current")


class _ZxAnCliTelnetEnable_Type(Integer32):
    """Custom type zxAnCliTelnetEnable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_ZxAnCliTelnetEnable_Type.__name__ = "Integer32"
_ZxAnCliTelnetEnable_Object = MibScalar
zxAnCliTelnetEnable = _ZxAnCliTelnetEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 3, 8),
    _ZxAnCliTelnetEnable_Type()
)
zxAnCliTelnetEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnCliTelnetEnable.setStatus("current")


class _ZxAnCliUserSuspendMode_Type(Integer32):
    """Custom type zxAnCliUserSuspendMode based on Integer32"""
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
        *(("notSuspend", 1),
          ("byIp", 2),
          ("byUserName", 3),
          ("byIpOrUserName", 4))
    )


_ZxAnCliUserSuspendMode_Type.__name__ = "Integer32"
_ZxAnCliUserSuspendMode_Object = MibScalar
zxAnCliUserSuspendMode = _ZxAnCliUserSuspendMode_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 3, 9),
    _ZxAnCliUserSuspendMode_Type()
)
zxAnCliUserSuspendMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnCliUserSuspendMode.setStatus("current")


class _ZxAnCliUserSuspendDuration_Type(Integer32):
    """Custom type zxAnCliUserSuspendDuration based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 1440),
    )


_ZxAnCliUserSuspendDuration_Type.__name__ = "Integer32"
_ZxAnCliUserSuspendDuration_Object = MibScalar
zxAnCliUserSuspendDuration = _ZxAnCliUserSuspendDuration_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 3, 10),
    _ZxAnCliUserSuspendDuration_Type()
)
zxAnCliUserSuspendDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnCliUserSuspendDuration.setStatus("current")
if mibBuilder.loadTexts:
    zxAnCliUserSuspendDuration.setUnits("minutes")


class _ZxAnCliUserPasswordRetries_Type(Integer32):
    """Custom type zxAnCliUserPasswordRetries based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_ZxAnCliUserPasswordRetries_Type.__name__ = "Integer32"
_ZxAnCliUserPasswordRetries_Object = MibScalar
zxAnCliUserPasswordRetries = _ZxAnCliUserPasswordRetries_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 3, 11),
    _ZxAnCliUserPasswordRetries_Type()
)
zxAnCliUserPasswordRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnCliUserPasswordRetries.setStatus("current")


class _ZxAnCliTryToLoginUserName_Type(DisplayString):
    """Custom type zxAnCliTryToLoginUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ZxAnCliTryToLoginUserName_Type.__name__ = "DisplayString"
_ZxAnCliTryToLoginUserName_Object = MibScalar
zxAnCliTryToLoginUserName = _ZxAnCliTryToLoginUserName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 3, 12),
    _ZxAnCliTryToLoginUserName_Type()
)
zxAnCliTryToLoginUserName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    zxAnCliTryToLoginUserName.setStatus("current")


class _ZxAnCliTryToLoginUserLocation_Type(DisplayString):
    """Custom type zxAnCliTryToLoginUserLocation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_ZxAnCliTryToLoginUserLocation_Type.__name__ = "DisplayString"
_ZxAnCliTryToLoginUserLocation_Object = MibScalar
zxAnCliTryToLoginUserLocation = _ZxAnCliTryToLoginUserLocation_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 3, 13),
    _ZxAnCliTryToLoginUserLocation_Type()
)
zxAnCliTryToLoginUserLocation.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    zxAnCliTryToLoginUserLocation.setStatus("current")


class _ZxAnCliMultiSessionsInformEnable_Type(Integer32):
    """Custom type zxAnCliMultiSessionsInformEnable based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_ZxAnCliMultiSessionsInformEnable_Type.__name__ = "Integer32"
_ZxAnCliMultiSessionsInformEnable_Object = MibScalar
zxAnCliMultiSessionsInformEnable = _ZxAnCliMultiSessionsInformEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 3, 14),
    _ZxAnCliMultiSessionsInformEnable_Type()
)
zxAnCliMultiSessionsInformEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnCliMultiSessionsInformEnable.setStatus("current")
_ZxAnSysSshObjects_ObjectIdentity = ObjectIdentity
zxAnSysSshObjects = _ZxAnSysSshObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 3, 47)
)
_ZxAnSysSshGlobalObjects_ObjectIdentity = ObjectIdentity
zxAnSysSshGlobalObjects = _ZxAnSysSshGlobalObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 3, 47, 1)
)


class _ZxAnSysSshEnable_Type(Integer32):
    """Custom type zxAnSysSshEnable based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_ZxAnSysSshEnable_Type.__name__ = "Integer32"
_ZxAnSysSshEnable_Object = MibScalar
zxAnSysSshEnable = _ZxAnSysSshEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 3, 47, 1, 2),
    _ZxAnSysSshEnable_Type()
)
zxAnSysSshEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnSysSshEnable.setStatus("current")


class _ZxAnSysSshVersion_Type(Integer32):
    """Custom type zxAnSysSshVersion based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("v1", 1),
          ("v2", 2))
    )


_ZxAnSysSshVersion_Type.__name__ = "Integer32"
_ZxAnSysSshVersion_Object = MibScalar
zxAnSysSshVersion = _ZxAnSysSshVersion_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 3, 47, 1, 3),
    _ZxAnSysSshVersion_Type()
)
zxAnSysSshVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnSysSshVersion.setStatus("current")


class _ZxAnSysSshOnlyEnable_Type(Integer32):
    """Custom type zxAnSysSshOnlyEnable based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_ZxAnSysSshOnlyEnable_Type.__name__ = "Integer32"
_ZxAnSysSshOnlyEnable_Object = MibScalar
zxAnSysSshOnlyEnable = _ZxAnSysSshOnlyEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 3, 47, 1, 4),
    _ZxAnSysSshOnlyEnable_Type()
)
zxAnSysSshOnlyEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnSysSshOnlyEnable.setStatus("current")


class _ZxAnSysSshGenerateKeyEnable_Type(Integer32):
    """Custom type zxAnSysSshGenerateKeyEnable based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_ZxAnSysSshGenerateKeyEnable_Type.__name__ = "Integer32"
_ZxAnSysSshGenerateKeyEnable_Object = MibScalar
zxAnSysSshGenerateKeyEnable = _ZxAnSysSshGenerateKeyEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 3, 47, 1, 5),
    _ZxAnSysSshGenerateKeyEnable_Type()
)
zxAnSysSshGenerateKeyEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnSysSshGenerateKeyEnable.setStatus("current")


class _ZxAnSysSshAuthType_Type(Integer32):
    """Custom type zxAnSysSshAuthType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("pap", 1),
          ("chap", 2))
    )


_ZxAnSysSshAuthType_Type.__name__ = "Integer32"
_ZxAnSysSshAuthType_Object = MibScalar
zxAnSysSshAuthType = _ZxAnSysSshAuthType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 3, 47, 1, 6),
    _ZxAnSysSshAuthType_Type()
)
zxAnSysSshAuthType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnSysSshAuthType.setStatus("current")
_ZxAnSysWriteLockObjects_ObjectIdentity = ObjectIdentity
zxAnSysWriteLockObjects = _ZxAnSysWriteLockObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 3, 48)
)


class _ZxAnSysWriteLockOwner_Type(Integer32):
    """Custom type zxAnSysWriteLockOwner based on Integer32"""
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
          ("snmp", 2),
          ("console", 3),
          ("telnet", 4))
    )


_ZxAnSysWriteLockOwner_Type.__name__ = "Integer32"
_ZxAnSysWriteLockOwner_Object = MibScalar
zxAnSysWriteLockOwner = _ZxAnSysWriteLockOwner_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 3, 48, 1),
    _ZxAnSysWriteLockOwner_Type()
)
zxAnSysWriteLockOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSysWriteLockOwner.setStatus("current")


class _ZxAnSysWriteLockAction_Type(Integer32):
    """Custom type zxAnSysWriteLockAction based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("lock", 1),
          ("unlock", 2))
    )


_ZxAnSysWriteLockAction_Type.__name__ = "Integer32"
_ZxAnSysWriteLockAction_Object = MibScalar
zxAnSysWriteLockAction = _ZxAnSysWriteLockAction_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 3, 48, 2),
    _ZxAnSysWriteLockAction_Type()
)
zxAnSysWriteLockAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnSysWriteLockAction.setStatus("current")
_ZxAnSysCliUserTable_Object = MibTable
zxAnSysCliUserTable = _ZxAnSysCliUserTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 3, 49)
)
if mibBuilder.loadTexts:
    zxAnSysCliUserTable.setStatus("current")
_ZxAnSysCliUserEntry_Object = MibTableRow
zxAnSysCliUserEntry = _ZxAnSysCliUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 3, 49, 1)
)
zxAnSysCliUserEntry.setIndexNames(
    (0, "ZTE-AN-SYS-MIB", "zxAnCliUserConfIndex"),
)
if mibBuilder.loadTexts:
    zxAnSysCliUserEntry.setStatus("current")
_ZxAnCliUserConfIndex_Type = Integer32
_ZxAnCliUserConfIndex_Object = MibTableColumn
zxAnCliUserConfIndex = _ZxAnCliUserConfIndex_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 3, 49, 1, 1),
    _ZxAnCliUserConfIndex_Type()
)
zxAnCliUserConfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnCliUserConfIndex.setStatus("current")


class _ZxAnCliUserConfName_Type(DisplayString):
    """Custom type zxAnCliUserConfName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_ZxAnCliUserConfName_Type.__name__ = "DisplayString"
_ZxAnCliUserConfName_Object = MibTableColumn
zxAnCliUserConfName = _ZxAnCliUserConfName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 3, 49, 1, 2),
    _ZxAnCliUserConfName_Type()
)
zxAnCliUserConfName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnCliUserConfName.setStatus("current")


class _ZxAnCliUserConfPwd_Type(DisplayString):
    """Custom type zxAnCliUserConfPwd based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 32),
    )


_ZxAnCliUserConfPwd_Type.__name__ = "DisplayString"
_ZxAnCliUserConfPwd_Object = MibTableColumn
zxAnCliUserConfPwd = _ZxAnCliUserConfPwd_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 3, 49, 1, 3),
    _ZxAnCliUserConfPwd_Type()
)
zxAnCliUserConfPwd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnCliUserConfPwd.setStatus("current")


class _ZxAnCliUserConfAccessLevel_Type(Integer32):
    """Custom type zxAnCliUserConfAccessLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_ZxAnCliUserConfAccessLevel_Type.__name__ = "Integer32"
_ZxAnCliUserConfAccessLevel_Object = MibTableColumn
zxAnCliUserConfAccessLevel = _ZxAnCliUserConfAccessLevel_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 3, 49, 1, 4),
    _ZxAnCliUserConfAccessLevel_Type()
)
zxAnCliUserConfAccessLevel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnCliUserConfAccessLevel.setStatus("current")
_ZxAnCliUserConfRowStatus_Type = RowStatus
_ZxAnCliUserConfRowStatus_Object = MibTableColumn
zxAnCliUserConfRowStatus = _ZxAnCliUserConfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 3, 49, 1, 5),
    _ZxAnCliUserConfRowStatus_Type()
)
zxAnCliUserConfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnCliUserConfRowStatus.setStatus("current")


class _ZxAnCliUserConfPwdEncryptEnable_Type(Integer32):
    """Custom type zxAnCliUserConfPwdEncryptEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noEncrypt", 1),
          ("encrypt", 2))
    )


_ZxAnCliUserConfPwdEncryptEnable_Type.__name__ = "Integer32"
_ZxAnCliUserConfPwdEncryptEnable_Object = MibTableColumn
zxAnCliUserConfPwdEncryptEnable = _ZxAnCliUserConfPwdEncryptEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 3, 49, 1, 6),
    _ZxAnCliUserConfPwdEncryptEnable_Type()
)
zxAnCliUserConfPwdEncryptEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnCliUserConfPwdEncryptEnable.setStatus("current")


class _ZxAnCliUserConfMaxSessions_Type(Integer32):
    """Custom type zxAnCliUserConfMaxSessions based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_ZxAnCliUserConfMaxSessions_Type.__name__ = "Integer32"
_ZxAnCliUserConfMaxSessions_Object = MibTableColumn
zxAnCliUserConfMaxSessions = _ZxAnCliUserConfMaxSessions_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 3, 49, 1, 7),
    _ZxAnCliUserConfMaxSessions_Type()
)
zxAnCliUserConfMaxSessions.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnCliUserConfMaxSessions.setStatus("current")


class _ZxAnCliUserConfAdminStatus_Type(Integer32):
    """Custom type zxAnCliUserConfAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_ZxAnCliUserConfAdminStatus_Type.__name__ = "Integer32"
_ZxAnCliUserConfAdminStatus_Object = MibTableColumn
zxAnCliUserConfAdminStatus = _ZxAnCliUserConfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 3, 49, 1, 8),
    _ZxAnCliUserConfAdminStatus_Type()
)
zxAnCliUserConfAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnCliUserConfAdminStatus.setStatus("current")


class _ZxAnCliUserConfOperStatus_Type(Integer32):
    """Custom type zxAnCliUserConfOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("suspended", 2),
          ("disabled", 3))
    )


_ZxAnCliUserConfOperStatus_Type.__name__ = "Integer32"
_ZxAnCliUserConfOperStatus_Object = MibTableColumn
zxAnCliUserConfOperStatus = _ZxAnCliUserConfOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 3, 49, 1, 9),
    _ZxAnCliUserConfOperStatus_Type()
)
zxAnCliUserConfOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCliUserConfOperStatus.setStatus("current")
_ZxAnSysMgmtAclTable_Object = MibTable
zxAnSysMgmtAclTable = _ZxAnSysMgmtAclTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 3, 50)
)
if mibBuilder.loadTexts:
    zxAnSysMgmtAclTable.setStatus("current")
_ZxAnSysMgmtAclEntry_Object = MibTableRow
zxAnSysMgmtAclEntry = _ZxAnSysMgmtAclEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 3, 50, 1)
)
zxAnSysMgmtAclEntry.setIndexNames(
    (0, "ZTE-AN-SYS-MIB", "zxAnSysMgmtAclIndex"),
)
if mibBuilder.loadTexts:
    zxAnSysMgmtAclEntry.setStatus("current")


class _ZxAnSysMgmtAclIndex_Type(Integer32):
    """Custom type zxAnSysMgmtAclIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99),
    )


_ZxAnSysMgmtAclIndex_Type.__name__ = "Integer32"
_ZxAnSysMgmtAclIndex_Object = MibTableColumn
zxAnSysMgmtAclIndex = _ZxAnSysMgmtAclIndex_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 3, 50, 1, 1),
    _ZxAnSysMgmtAclIndex_Type()
)
zxAnSysMgmtAclIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnSysMgmtAclIndex.setStatus("current")


class _ZxAnSysMgmtAclAlias_Type(DisplayString):
    """Custom type zxAnSysMgmtAclAlias based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_ZxAnSysMgmtAclAlias_Type.__name__ = "DisplayString"
_ZxAnSysMgmtAclAlias_Object = MibTableColumn
zxAnSysMgmtAclAlias = _ZxAnSysMgmtAclAlias_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 3, 50, 1, 2),
    _ZxAnSysMgmtAclAlias_Type()
)
zxAnSysMgmtAclAlias.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnSysMgmtAclAlias.setStatus("current")
_ZxAnSysMgmtAclRowStatus_Type = RowStatus
_ZxAnSysMgmtAclRowStatus_Object = MibTableColumn
zxAnSysMgmtAclRowStatus = _ZxAnSysMgmtAclRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 3, 50, 1, 30),
    _ZxAnSysMgmtAclRowStatus_Type()
)
zxAnSysMgmtAclRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnSysMgmtAclRowStatus.setStatus("current")
_ZxAnSysMgmtAclRuleTable_Object = MibTable
zxAnSysMgmtAclRuleTable = _ZxAnSysMgmtAclRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 3, 51)
)
if mibBuilder.loadTexts:
    zxAnSysMgmtAclRuleTable.setStatus("current")
_ZxAnSysMgmtAclRuleEntry_Object = MibTableRow
zxAnSysMgmtAclRuleEntry = _ZxAnSysMgmtAclRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 3, 51, 1)
)
zxAnSysMgmtAclRuleEntry.setIndexNames(
    (0, "ZTE-AN-SYS-MIB", "zxAnSysMgmtAclIndex"),
    (0, "ZTE-AN-SYS-MIB", "zxAnSysMgmtAclRuleID"),
)
if mibBuilder.loadTexts:
    zxAnSysMgmtAclRuleEntry.setStatus("current")


class _ZxAnSysMgmtAclRuleID_Type(Integer32):
    """Custom type zxAnSysMgmtAclRuleID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_ZxAnSysMgmtAclRuleID_Type.__name__ = "Integer32"
_ZxAnSysMgmtAclRuleID_Object = MibTableColumn
zxAnSysMgmtAclRuleID = _ZxAnSysMgmtAclRuleID_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 3, 51, 1, 1),
    _ZxAnSysMgmtAclRuleID_Type()
)
zxAnSysMgmtAclRuleID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnSysMgmtAclRuleID.setStatus("current")


class _ZxAnSysMgmtAclRuleAccessCtrl_Type(Integer32):
    """Custom type zxAnSysMgmtAclRuleAccessCtrl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("permit", 1),
          ("deny", 2))
    )


_ZxAnSysMgmtAclRuleAccessCtrl_Type.__name__ = "Integer32"
_ZxAnSysMgmtAclRuleAccessCtrl_Object = MibTableColumn
zxAnSysMgmtAclRuleAccessCtrl = _ZxAnSysMgmtAclRuleAccessCtrl_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 3, 51, 1, 2),
    _ZxAnSysMgmtAclRuleAccessCtrl_Type()
)
zxAnSysMgmtAclRuleAccessCtrl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnSysMgmtAclRuleAccessCtrl.setStatus("current")


class _ZxAnSysMgmtAclRuleSrcAddrType_Type(InetAddressType):
    """Custom type zxAnSysMgmtAclRuleSrcAddrType based on InetAddressType"""
    defaultValue = 1


_ZxAnSysMgmtAclRuleSrcAddrType_Type.__name__ = "InetAddressType"
_ZxAnSysMgmtAclRuleSrcAddrType_Object = MibTableColumn
zxAnSysMgmtAclRuleSrcAddrType = _ZxAnSysMgmtAclRuleSrcAddrType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 3, 51, 1, 3),
    _ZxAnSysMgmtAclRuleSrcAddrType_Type()
)
zxAnSysMgmtAclRuleSrcAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnSysMgmtAclRuleSrcAddrType.setStatus("current")
_ZxAnSysMgmtAclRuleSrcAddr_Type = InetAddress
_ZxAnSysMgmtAclRuleSrcAddr_Object = MibTableColumn
zxAnSysMgmtAclRuleSrcAddr = _ZxAnSysMgmtAclRuleSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 3, 51, 1, 4),
    _ZxAnSysMgmtAclRuleSrcAddr_Type()
)
zxAnSysMgmtAclRuleSrcAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnSysMgmtAclRuleSrcAddr.setStatus("current")
_ZxAnSysMngAclRuleSrcAddrWildcard_Type = InetAddress
_ZxAnSysMngAclRuleSrcAddrWildcard_Object = MibTableColumn
zxAnSysMngAclRuleSrcAddrWildcard = _ZxAnSysMngAclRuleSrcAddrWildcard_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 3, 51, 1, 5),
    _ZxAnSysMngAclRuleSrcAddrWildcard_Type()
)
zxAnSysMngAclRuleSrcAddrWildcard.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnSysMngAclRuleSrcAddrWildcard.setStatus("current")
_ZxAnSysMgmtAclRuleRowStatus_Type = RowStatus
_ZxAnSysMgmtAclRuleRowStatus_Object = MibTableColumn
zxAnSysMgmtAclRuleRowStatus = _ZxAnSysMgmtAclRuleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 3, 51, 1, 50),
    _ZxAnSysMgmtAclRuleRowStatus_Type()
)
zxAnSysMgmtAclRuleRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnSysMgmtAclRuleRowStatus.setStatus("current")
_ZxAnSysMgmtAclBindTable_Object = MibTable
zxAnSysMgmtAclBindTable = _ZxAnSysMgmtAclBindTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 3, 52)
)
if mibBuilder.loadTexts:
    zxAnSysMgmtAclBindTable.setStatus("current")
_ZxAnSysMgmtAclBindEntry_Object = MibTableRow
zxAnSysMgmtAclBindEntry = _ZxAnSysMgmtAclBindEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 3, 52, 1)
)
zxAnSysMgmtAclBindEntry.setIndexNames(
    (0, "ZTE-AN-SYS-MIB", "zxAnSysMgmtAclProtocol"),
)
if mibBuilder.loadTexts:
    zxAnSysMgmtAclBindEntry.setStatus("current")


class _ZxAnSysMgmtAclProtocol_Type(Integer32):
    """Custom type zxAnSysMgmtAclProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("telnet", 1),
          ("snmp", 2))
    )


_ZxAnSysMgmtAclProtocol_Type.__name__ = "Integer32"
_ZxAnSysMgmtAclProtocol_Object = MibTableColumn
zxAnSysMgmtAclProtocol = _ZxAnSysMgmtAclProtocol_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 3, 52, 1, 1),
    _ZxAnSysMgmtAclProtocol_Type()
)
zxAnSysMgmtAclProtocol.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnSysMgmtAclProtocol.setStatus("current")


class _ZxAnSysMgmtAclBindIndex_Type(Integer32):
    """Custom type zxAnSysMgmtAclBindIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99),
    )


_ZxAnSysMgmtAclBindIndex_Type.__name__ = "Integer32"
_ZxAnSysMgmtAclBindIndex_Object = MibTableColumn
zxAnSysMgmtAclBindIndex = _ZxAnSysMgmtAclBindIndex_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 3, 52, 1, 2),
    _ZxAnSysMgmtAclBindIndex_Type()
)
zxAnSysMgmtAclBindIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnSysMgmtAclBindIndex.setStatus("current")
_ZxAnSysCliActiveUsersTable_Object = MibTable
zxAnSysCliActiveUsersTable = _ZxAnSysCliActiveUsersTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 3, 53)
)
if mibBuilder.loadTexts:
    zxAnSysCliActiveUsersTable.setStatus("current")
_ZxAnSysCliActiveUsersEntry_Object = MibTableRow
zxAnSysCliActiveUsersEntry = _ZxAnSysCliActiveUsersEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 3, 53, 1)
)
zxAnSysCliActiveUsersEntry.setIndexNames(
    (0, "ZTE-AN-SYS-MIB", "zxAnCliActiveUserIndex"),
)
if mibBuilder.loadTexts:
    zxAnSysCliActiveUsersEntry.setStatus("current")
_ZxAnCliActiveUserIndex_Type = Integer32
_ZxAnCliActiveUserIndex_Object = MibTableColumn
zxAnCliActiveUserIndex = _ZxAnCliActiveUserIndex_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 3, 53, 1, 1),
    _ZxAnCliActiveUserIndex_Type()
)
zxAnCliActiveUserIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnCliActiveUserIndex.setStatus("current")


class _ZxAnCliActiveUserType_Type(Integer32):
    """Custom type zxAnCliActiveUserType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("con", 1),
          ("vty", 2))
    )


_ZxAnCliActiveUserType_Type.__name__ = "Integer32"
_ZxAnCliActiveUserType_Object = MibTableColumn
zxAnCliActiveUserType = _ZxAnCliActiveUserType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 3, 53, 1, 2),
    _ZxAnCliActiveUserType_Type()
)
zxAnCliActiveUserType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCliActiveUserType.setStatus("current")


class _ZxAnCliActiveUserName_Type(DisplayString):
    """Custom type zxAnCliActiveUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_ZxAnCliActiveUserName_Type.__name__ = "DisplayString"
_ZxAnCliActiveUserName_Object = MibTableColumn
zxAnCliActiveUserName = _ZxAnCliActiveUserName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 3, 53, 1, 3),
    _ZxAnCliActiveUserName_Type()
)
zxAnCliActiveUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCliActiveUserName.setStatus("current")


class _ZxAnCliActiveUserPriority_Type(Integer32):
    """Custom type zxAnCliActiveUserPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_ZxAnCliActiveUserPriority_Type.__name__ = "Integer32"
_ZxAnCliActiveUserPriority_Object = MibTableColumn
zxAnCliActiveUserPriority = _ZxAnCliActiveUserPriority_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 3, 53, 1, 4),
    _ZxAnCliActiveUserPriority_Type()
)
zxAnCliActiveUserPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCliActiveUserPriority.setStatus("current")


class _ZxAnCliActiveUserHost_Type(DisplayString):
    """Custom type zxAnCliActiveUserHost based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 40),
    )


_ZxAnCliActiveUserHost_Type.__name__ = "DisplayString"
_ZxAnCliActiveUserHost_Object = MibTableColumn
zxAnCliActiveUserHost = _ZxAnCliActiveUserHost_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 3, 53, 1, 5),
    _ZxAnCliActiveUserHost_Type()
)
zxAnCliActiveUserHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCliActiveUserHost.setStatus("current")


class _ZxAnCliActiveUserIdleTime_Type(DisplayString):
    """Custom type zxAnCliActiveUserIdleTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_ZxAnCliActiveUserIdleTime_Type.__name__ = "DisplayString"
_ZxAnCliActiveUserIdleTime_Object = MibTableColumn
zxAnCliActiveUserIdleTime = _ZxAnCliActiveUserIdleTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 3, 53, 1, 6),
    _ZxAnCliActiveUserIdleTime_Type()
)
zxAnCliActiveUserIdleTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCliActiveUserIdleTime.setStatus("current")


class _ZxAnCliActiveUserLocation_Type(DisplayString):
    """Custom type zxAnCliActiveUserLocation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 40),
    )


_ZxAnCliActiveUserLocation_Type.__name__ = "DisplayString"
_ZxAnCliActiveUserLocation_Object = MibTableColumn
zxAnCliActiveUserLocation = _ZxAnCliActiveUserLocation_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 3, 53, 1, 7),
    _ZxAnCliActiveUserLocation_Type()
)
zxAnCliActiveUserLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnCliActiveUserLocation.setStatus("current")
_ZxAnSysCliActiveUserRowStatus_Type = RowStatus
_ZxAnSysCliActiveUserRowStatus_Object = MibTableColumn
zxAnSysCliActiveUserRowStatus = _ZxAnSysCliActiveUserRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 3, 53, 1, 31),
    _ZxAnSysCliActiveUserRowStatus_Type()
)
zxAnSysCliActiveUserRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnSysCliActiveUserRowStatus.setStatus("current")
_ZxAnSysCommunityConfTable_Object = MibTable
zxAnSysCommunityConfTable = _ZxAnSysCommunityConfTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 3, 54)
)
if mibBuilder.loadTexts:
    zxAnSysCommunityConfTable.setStatus("current")
_ZxAnSysCommunityConfEntry_Object = MibTableRow
zxAnSysCommunityConfEntry = _ZxAnSysCommunityConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 3, 54, 1)
)
zxAnSysCommunityConfEntry.setIndexNames(
    (0, "ZTE-AN-SYS-MIB", "zxAnSysCommunityConfCommunity"),
)
if mibBuilder.loadTexts:
    zxAnSysCommunityConfEntry.setStatus("current")


class _ZxAnSysCommunityConfCommunity_Type(DisplayString):
    """Custom type zxAnSysCommunityConfCommunity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_ZxAnSysCommunityConfCommunity_Type.__name__ = "DisplayString"
_ZxAnSysCommunityConfCommunity_Object = MibTableColumn
zxAnSysCommunityConfCommunity = _ZxAnSysCommunityConfCommunity_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 3, 54, 1, 1),
    _ZxAnSysCommunityConfCommunity_Type()
)
zxAnSysCommunityConfCommunity.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnSysCommunityConfCommunity.setStatus("current")


class _ZxAnSysCommunityConfPermission_Type(Integer32):
    """Custom type zxAnSysCommunityConfPermission based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("readOnly", 1),
          ("readWrite", 2))
    )


_ZxAnSysCommunityConfPermission_Type.__name__ = "Integer32"
_ZxAnSysCommunityConfPermission_Object = MibTableColumn
zxAnSysCommunityConfPermission = _ZxAnSysCommunityConfPermission_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 3, 54, 1, 2),
    _ZxAnSysCommunityConfPermission_Type()
)
zxAnSysCommunityConfPermission.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnSysCommunityConfPermission.setStatus("current")


class _ZxAnSysCommunityConfViewName_Type(DisplayString):
    """Custom type zxAnSysCommunityConfViewName based on DisplayString"""
    defaultValue = OctetString("allView")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_ZxAnSysCommunityConfViewName_Type.__name__ = "DisplayString"
_ZxAnSysCommunityConfViewName_Object = MibTableColumn
zxAnSysCommunityConfViewName = _ZxAnSysCommunityConfViewName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 3, 54, 1, 3),
    _ZxAnSysCommunityConfViewName_Type()
)
zxAnSysCommunityConfViewName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnSysCommunityConfViewName.setStatus("current")
_ZxAnSysCommunityConfRowStatus_Type = RowStatus
_ZxAnSysCommunityConfRowStatus_Object = MibTableColumn
zxAnSysCommunityConfRowStatus = _ZxAnSysCommunityConfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 3, 54, 1, 15),
    _ZxAnSysCommunityConfRowStatus_Type()
)
zxAnSysCommunityConfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnSysCommunityConfRowStatus.setStatus("current")
_ZxAnSysDataMgmt_ObjectIdentity = ObjectIdentity
zxAnSysDataMgmt = _ZxAnSysDataMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 4)
)


class _ZxAnSysConfigSavingAction_Type(Integer32):
    """Custom type zxAnSysConfigSavingAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("saveFlash", 1)
    )


_ZxAnSysConfigSavingAction_Type.__name__ = "Integer32"
_ZxAnSysConfigSavingAction_Object = MibScalar
zxAnSysConfigSavingAction = _ZxAnSysConfigSavingAction_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 4, 1),
    _ZxAnSysConfigSavingAction_Type()
)
zxAnSysConfigSavingAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnSysConfigSavingAction.setStatus("current")


class _ZxAnSysConfigSaveStatus_Type(Integer32):
    """Custom type zxAnSysConfigSaveStatus based on Integer32"""
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
        *(("success", 1),
          ("failed", 2),
          ("saving", 3),
          ("noOperation", 4))
    )


_ZxAnSysConfigSaveStatus_Type.__name__ = "Integer32"
_ZxAnSysConfigSaveStatus_Object = MibScalar
zxAnSysConfigSaveStatus = _ZxAnSysConfigSaveStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 4, 2),
    _ZxAnSysConfigSaveStatus_Type()
)
zxAnSysConfigSaveStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSysConfigSaveStatus.setStatus("current")


class _ZxAnSysAutoSaveFlashMode_Type(Integer32):
    """Custom type zxAnSysAutoSaveFlashMode based on Integer32"""
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
        *(("disable", 1),
          ("everyday", 2),
          ("interval", 3),
          ("configChanged", 4))
    )


_ZxAnSysAutoSaveFlashMode_Type.__name__ = "Integer32"
_ZxAnSysAutoSaveFlashMode_Object = MibScalar
zxAnSysAutoSaveFlashMode = _ZxAnSysAutoSaveFlashMode_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 4, 3),
    _ZxAnSysAutoSaveFlashMode_Type()
)
zxAnSysAutoSaveFlashMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnSysAutoSaveFlashMode.setStatus("current")


class _ZxAnSysDailyAutoSaveFlashTime_Type(DisplayString):
    """Custom type zxAnSysDailyAutoSaveFlashTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 9),
    )


_ZxAnSysDailyAutoSaveFlashTime_Type.__name__ = "DisplayString"
_ZxAnSysDailyAutoSaveFlashTime_Object = MibScalar
zxAnSysDailyAutoSaveFlashTime = _ZxAnSysDailyAutoSaveFlashTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 4, 4),
    _ZxAnSysDailyAutoSaveFlashTime_Type()
)
zxAnSysDailyAutoSaveFlashTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnSysDailyAutoSaveFlashTime.setStatus("current")


class _ZxAnSysAutoSaveFlashStartDate_Type(DisplayString):
    """Custom type zxAnSysAutoSaveFlashStartDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_ZxAnSysAutoSaveFlashStartDate_Type.__name__ = "DisplayString"
_ZxAnSysAutoSaveFlashStartDate_Object = MibScalar
zxAnSysAutoSaveFlashStartDate = _ZxAnSysAutoSaveFlashStartDate_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 4, 5),
    _ZxAnSysAutoSaveFlashStartDate_Type()
)
zxAnSysAutoSaveFlashStartDate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnSysAutoSaveFlashStartDate.setStatus("current")


class _ZxAnSysAutoSaveFlashInterval_Type(Integer32):
    """Custom type zxAnSysAutoSaveFlashInterval based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8760),
    )


_ZxAnSysAutoSaveFlashInterval_Type.__name__ = "Integer32"
_ZxAnSysAutoSaveFlashInterval_Object = MibScalar
zxAnSysAutoSaveFlashInterval = _ZxAnSysAutoSaveFlashInterval_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 4, 6),
    _ZxAnSysAutoSaveFlashInterval_Type()
)
zxAnSysAutoSaveFlashInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnSysAutoSaveFlashInterval.setStatus("current")
if mibBuilder.loadTexts:
    zxAnSysAutoSaveFlashInterval.setUnits("hours")


class _ZxAnSysConfigSaveProgress_Type(Integer32):
    """Custom type zxAnSysConfigSaveProgress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ZxAnSysConfigSaveProgress_Type.__name__ = "Integer32"
_ZxAnSysConfigSaveProgress_Object = MibScalar
zxAnSysConfigSaveProgress = _ZxAnSysConfigSaveProgress_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 4, 7),
    _ZxAnSysConfigSaveProgress_Type()
)
zxAnSysConfigSaveProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSysConfigSaveProgress.setStatus("current")
if mibBuilder.loadTexts:
    zxAnSysConfigSaveProgress.setUnits("percents")


class _ZxAnSysDataSaveFlashFailReason_Type(Integer32):
    """Custom type zxAnSysDataSaveFlashFailReason based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              99)
        )
    )
    namedValues = NamedValues(
        *(("noError", 1),
          ("flashMediaFull", 2),
          ("createConfigFilesFailed", 3),
          ("openConfigFilesFailed", 4),
          ("standbyCardCopyConfigFilesFailed", 5),
          ("unknown", 99))
    )


_ZxAnSysDataSaveFlashFailReason_Type.__name__ = "Integer32"
_ZxAnSysDataSaveFlashFailReason_Object = MibScalar
zxAnSysDataSaveFlashFailReason = _ZxAnSysDataSaveFlashFailReason_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 4, 8),
    _ZxAnSysDataSaveFlashFailReason_Type()
)
zxAnSysDataSaveFlashFailReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSysDataSaveFlashFailReason.setStatus("current")


class _ZxAnSysCfgChangeSaveFlashEnable_Type(Integer32):
    """Custom type zxAnSysCfgChangeSaveFlashEnable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_ZxAnSysCfgChangeSaveFlashEnable_Type.__name__ = "Integer32"
_ZxAnSysCfgChangeSaveFlashEnable_Object = MibScalar
zxAnSysCfgChangeSaveFlashEnable = _ZxAnSysCfgChangeSaveFlashEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 4, 9),
    _ZxAnSysCfgChangeSaveFlashEnable_Type()
)
zxAnSysCfgChangeSaveFlashEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnSysCfgChangeSaveFlashEnable.setStatus("current")


class _ZxAnSysCfgChangeSaveHoldOffTime_Type(Integer32):
    """Custom type zxAnSysCfgChangeSaveHoldOffTime based on Integer32"""
    defaultValue = 3600

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 86400),
    )


_ZxAnSysCfgChangeSaveHoldOffTime_Type.__name__ = "Integer32"
_ZxAnSysCfgChangeSaveHoldOffTime_Object = MibScalar
zxAnSysCfgChangeSaveHoldOffTime = _ZxAnSysCfgChangeSaveHoldOffTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 4, 10),
    _ZxAnSysCfgChangeSaveHoldOffTime_Type()
)
zxAnSysCfgChangeSaveHoldOffTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnSysCfgChangeSaveHoldOffTime.setStatus("current")
if mibBuilder.loadTexts:
    zxAnSysCfgChangeSaveHoldOffTime.setUnits("seconds")
_ZxAnSysRunningCtrl_ObjectIdentity = ObjectIdentity
zxAnSysRunningCtrl = _ZxAnSysRunningCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 5)
)


class _ZxAnChassisSysReboot_Type(Integer32):
    """Custom type zxAnChassisSysReboot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("rebootSystem", 1)
    )


_ZxAnChassisSysReboot_Type.__name__ = "Integer32"
_ZxAnChassisSysReboot_Object = MibScalar
zxAnChassisSysReboot = _ZxAnChassisSysReboot_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 5, 1),
    _ZxAnChassisSysReboot_Type()
)
zxAnChassisSysReboot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnChassisSysReboot.setStatus("current")


class _ZxAnSysRevision_Type(Bits):
    """Custom type zxAnSysRevision based on Bits"""
    namedValues = NamedValues(
        *(("aclTrafficLimit", 0),
          ("extendedACLTtl", 1),
          ("hybridACLDscp", 2),
          ("xConnectVlan", 3),
          ("qosIIVPortPrfType", 4),
          ("servicePortCosAndMode", 5),
          ("supportIPV6", 6),
          ("supportIgmpHostVersion", 7),
          ("qosII4KTVersion", 8),
          ("supportEtherIfMcastFloodingCtrl", 9),
          ("supportVdslDataRateTrap", 10),
          ("supportBrgUniActualEncapsType", 11),
          ("supportAdslProfileExt", 12),
          ("supportVlanDesc", 13),
          ("supportProtocolVlanMapEnable", 14),
          ("supportMulticastFloodingMode", 15),
          ("supportXdslXtuInitFailTrapEnable", 16),
          ("supportGINP4Vdsl", 17),
          ("supportGINP4Adsl", 18),
          ("supportMvlanCvlanId", 19),
          ("supportSecSvcInterworkVlan", 20),
          ("supportExtendAcceptFrameTypes4DT", 21),
          ("supportSnmpGetbulk", 22))
    )

_ZxAnSysRevision_Type.__name__ = "Bits"
_ZxAnSysRevision_Object = MibScalar
zxAnSysRevision = _ZxAnSysRevision_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 5, 2),
    _ZxAnSysRevision_Type()
)
zxAnSysRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSysRevision.setStatus("current")


class _ZxAnFileLoadDefaultConfiguration_Type(Integer32):
    """Custom type zxAnFileLoadDefaultConfiguration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("loadFactoryDefaults", 1)
    )


_ZxAnFileLoadDefaultConfiguration_Type.__name__ = "Integer32"
_ZxAnFileLoadDefaultConfiguration_Object = MibScalar
zxAnFileLoadDefaultConfiguration = _ZxAnFileLoadDefaultConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 5, 3),
    _ZxAnFileLoadDefaultConfiguration_Type()
)
zxAnFileLoadDefaultConfiguration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnFileLoadDefaultConfiguration.setStatus("current")


class _ZxAnSysLastRebootReason_Type(Integer32):
    """Custom type zxAnSysLastRebootReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              99)
        )
    )
    namedValues = NamedValues(
        *(("byCli", 1),
          ("byNms", 2),
          ("byWatchdog", 3),
          ("byPowerOff", 4),
          ("bySoftwareRestart", 5),
          ("byProcessSuspended", 6),
          ("unknown", 99))
    )


_ZxAnSysLastRebootReason_Type.__name__ = "Integer32"
_ZxAnSysLastRebootReason_Object = MibScalar
zxAnSysLastRebootReason = _ZxAnSysLastRebootReason_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 5, 4),
    _ZxAnSysLastRebootReason_Type()
)
zxAnSysLastRebootReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSysLastRebootReason.setStatus("current")


class _ZxAnSysResourceType_Type(Integer32):
    """Custom type zxAnSysResourceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("memory", 1)
    )


_ZxAnSysResourceType_Type.__name__ = "Integer32"
_ZxAnSysResourceType_Object = MibScalar
zxAnSysResourceType = _ZxAnSysResourceType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 5, 5),
    _ZxAnSysResourceType_Type()
)
zxAnSysResourceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSysResourceType.setStatus("current")
_ZxAnSysNmsMgmt_ObjectIdentity = ObjectIdentity
zxAnSysNmsMgmt = _ZxAnSysNmsMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 100)
)
_ZxAnSysNmsMgmtPath_ObjectIdentity = ObjectIdentity
zxAnSysNmsMgmtPath = _ZxAnSysNmsMgmtPath_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 100, 1)
)
_ZxAnSysNmsMgmtOutbandIpAddr_Type = IpAddress
_ZxAnSysNmsMgmtOutbandIpAddr_Object = MibScalar
zxAnSysNmsMgmtOutbandIpAddr = _ZxAnSysNmsMgmtOutbandIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 100, 1, 1),
    _ZxAnSysNmsMgmtOutbandIpAddr_Type()
)
zxAnSysNmsMgmtOutbandIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnSysNmsMgmtOutbandIpAddr.setStatus("current")
_ZxAnSysNmsMgmtOutbandIpMask_Type = IpAddress
_ZxAnSysNmsMgmtOutbandIpMask_Object = MibScalar
zxAnSysNmsMgmtOutbandIpMask = _ZxAnSysNmsMgmtOutbandIpMask_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 100, 1, 2),
    _ZxAnSysNmsMgmtOutbandIpMask_Type()
)
zxAnSysNmsMgmtOutbandIpMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnSysNmsMgmtOutbandIpMask.setStatus("current")
_ZxAnSysNmsMgmtOutbandMac_Type = MacAddress
_ZxAnSysNmsMgmtOutbandMac_Object = MibScalar
zxAnSysNmsMgmtOutbandMac = _ZxAnSysNmsMgmtOutbandMac_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 100, 1, 3),
    _ZxAnSysNmsMgmtOutbandMac_Type()
)
zxAnSysNmsMgmtOutbandMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSysNmsMgmtOutbandMac.setStatus("current")
_ZxAnSysNmsMgmtInbandIpAddr_Type = IpAddress
_ZxAnSysNmsMgmtInbandIpAddr_Object = MibScalar
zxAnSysNmsMgmtInbandIpAddr = _ZxAnSysNmsMgmtInbandIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 100, 1, 4),
    _ZxAnSysNmsMgmtInbandIpAddr_Type()
)
zxAnSysNmsMgmtInbandIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnSysNmsMgmtInbandIpAddr.setStatus("current")
_ZxAnSysNmsMgmtInbandIpMask_Type = IpAddress
_ZxAnSysNmsMgmtInbandIpMask_Object = MibScalar
zxAnSysNmsMgmtInbandIpMask = _ZxAnSysNmsMgmtInbandIpMask_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 100, 1, 5),
    _ZxAnSysNmsMgmtInbandIpMask_Type()
)
zxAnSysNmsMgmtInbandIpMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnSysNmsMgmtInbandIpMask.setStatus("current")
_ZxAnSysNmsMgmtInbandMac_Type = MacAddress
_ZxAnSysNmsMgmtInbandMac_Object = MibScalar
zxAnSysNmsMgmtInbandMac = _ZxAnSysNmsMgmtInbandMac_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 100, 1, 6),
    _ZxAnSysNmsMgmtInbandMac_Type()
)
zxAnSysNmsMgmtInbandMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSysNmsMgmtInbandMac.setStatus("current")
_ZxAnSysNmsMgmtInbandVlan_Type = Integer32
_ZxAnSysNmsMgmtInbandVlan_Object = MibScalar
zxAnSysNmsMgmtInbandVlan = _ZxAnSysNmsMgmtInbandVlan_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 100, 1, 7),
    _ZxAnSysNmsMgmtInbandVlan_Type()
)
zxAnSysNmsMgmtInbandVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnSysNmsMgmtInbandVlan.setStatus("current")


class _ZxAnSysNmsMgmtInbandVpnId_Type(Integer32):
    """Custom type zxAnSysNmsMgmtInbandVpnId based on Integer32"""
    defaultValue = 0


_ZxAnSysNmsMgmtInbandVpnId_Type.__name__ = "Integer32"
_ZxAnSysNmsMgmtInbandVpnId_Object = MibScalar
zxAnSysNmsMgmtInbandVpnId = _ZxAnSysNmsMgmtInbandVpnId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 100, 1, 8),
    _ZxAnSysNmsMgmtInbandVpnId_Type()
)
zxAnSysNmsMgmtInbandVpnId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnSysNmsMgmtInbandVpnId.setStatus("current")
_ZxAnSysMgmtOutbandIpv6Addr_Type = InetAddress
_ZxAnSysMgmtOutbandIpv6Addr_Object = MibScalar
zxAnSysMgmtOutbandIpv6Addr = _ZxAnSysMgmtOutbandIpv6Addr_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 100, 1, 9),
    _ZxAnSysMgmtOutbandIpv6Addr_Type()
)
zxAnSysMgmtOutbandIpv6Addr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnSysMgmtOutbandIpv6Addr.setStatus("current")
_ZxAnSysMgmtOutbandIpv6AddrPfxLen_Type = InetAddressPrefixLength
_ZxAnSysMgmtOutbandIpv6AddrPfxLen_Object = MibScalar
zxAnSysMgmtOutbandIpv6AddrPfxLen = _ZxAnSysMgmtOutbandIpv6AddrPfxLen_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 100, 1, 10),
    _ZxAnSysMgmtOutbandIpv6AddrPfxLen_Type()
)
zxAnSysMgmtOutbandIpv6AddrPfxLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnSysMgmtOutbandIpv6AddrPfxLen.setStatus("current")


class _ZxAnSysNmsMgmtInbandEnable_Type(Integer32):
    """Custom type zxAnSysNmsMgmtInbandEnable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_ZxAnSysNmsMgmtInbandEnable_Type.__name__ = "Integer32"
_ZxAnSysNmsMgmtInbandEnable_Object = MibScalar
zxAnSysNmsMgmtInbandEnable = _ZxAnSysNmsMgmtInbandEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 100, 1, 11),
    _ZxAnSysNmsMgmtInbandEnable_Type()
)
zxAnSysNmsMgmtInbandEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnSysNmsMgmtInbandEnable.setStatus("current")
_ZxAnSysServiceMgmtPath_ObjectIdentity = ObjectIdentity
zxAnSysServiceMgmtPath = _ZxAnSysServiceMgmtPath_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 100, 2)
)
_ZxAnSysServiceMgmtIpTable_Object = MibTable
zxAnSysServiceMgmtIpTable = _ZxAnSysServiceMgmtIpTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 100, 2, 1)
)
if mibBuilder.loadTexts:
    zxAnSysServiceMgmtIpTable.setStatus("current")
_ZxAnSysServiceMgmtIpEntry_Object = MibTableRow
zxAnSysServiceMgmtIpEntry = _ZxAnSysServiceMgmtIpEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 100, 2, 1, 1)
)
zxAnSysServiceMgmtIpEntry.setIndexNames(
    (0, "ZTE-AN-SYS-MIB", "zxAnSysServiceMgmtVlanId"),
)
if mibBuilder.loadTexts:
    zxAnSysServiceMgmtIpEntry.setStatus("current")


class _ZxAnSysServiceMgmtVlanId_Type(Integer32):
    """Custom type zxAnSysServiceMgmtVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_ZxAnSysServiceMgmtVlanId_Type.__name__ = "Integer32"
_ZxAnSysServiceMgmtVlanId_Object = MibTableColumn
zxAnSysServiceMgmtVlanId = _ZxAnSysServiceMgmtVlanId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 100, 2, 1, 1, 1),
    _ZxAnSysServiceMgmtVlanId_Type()
)
zxAnSysServiceMgmtVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnSysServiceMgmtVlanId.setStatus("current")


class _ZxAnSysServiceMgmtVpnId_Type(Integer32):
    """Custom type zxAnSysServiceMgmtVpnId based on Integer32"""
    defaultValue = 0


_ZxAnSysServiceMgmtVpnId_Type.__name__ = "Integer32"
_ZxAnSysServiceMgmtVpnId_Object = MibTableColumn
zxAnSysServiceMgmtVpnId = _ZxAnSysServiceMgmtVpnId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 100, 2, 1, 1, 2),
    _ZxAnSysServiceMgmtVpnId_Type()
)
zxAnSysServiceMgmtVpnId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnSysServiceMgmtVpnId.setStatus("current")
_ZxAnSysServiceMgmtIpAddr_Type = IpAddress
_ZxAnSysServiceMgmtIpAddr_Object = MibTableColumn
zxAnSysServiceMgmtIpAddr = _ZxAnSysServiceMgmtIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 100, 2, 1, 1, 3),
    _ZxAnSysServiceMgmtIpAddr_Type()
)
zxAnSysServiceMgmtIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnSysServiceMgmtIpAddr.setStatus("current")
_ZxAnSysServiceMgmtIpMask_Type = IpAddress
_ZxAnSysServiceMgmtIpMask_Object = MibTableColumn
zxAnSysServiceMgmtIpMask = _ZxAnSysServiceMgmtIpMask_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 100, 2, 1, 1, 4),
    _ZxAnSysServiceMgmtIpMask_Type()
)
zxAnSysServiceMgmtIpMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnSysServiceMgmtIpMask.setStatus("current")
_ZxAnSysServiceMgmtMac_Type = MacAddress
_ZxAnSysServiceMgmtMac_Object = MibTableColumn
zxAnSysServiceMgmtMac = _ZxAnSysServiceMgmtMac_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 100, 2, 1, 1, 5),
    _ZxAnSysServiceMgmtMac_Type()
)
zxAnSysServiceMgmtMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSysServiceMgmtMac.setStatus("current")
_ZxAnSysServiceMgmtIpRowStatus_Type = RowStatus
_ZxAnSysServiceMgmtIpRowStatus_Object = MibTableColumn
zxAnSysServiceMgmtIpRowStatus = _ZxAnSysServiceMgmtIpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 100, 2, 1, 1, 6),
    _ZxAnSysServiceMgmtIpRowStatus_Type()
)
zxAnSysServiceMgmtIpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnSysServiceMgmtIpRowStatus.setStatus("current")
_ZxAnSysTimeMgmt_ObjectIdentity = ObjectIdentity
zxAnSysTimeMgmt = _ZxAnSysTimeMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 101)
)


class _ZxAnRtcSysDateTime_Type(DisplayString):
    """Custom type zxAnRtcSysDateTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_ZxAnRtcSysDateTime_Type.__name__ = "DisplayString"
_ZxAnRtcSysDateTime_Object = MibScalar
zxAnRtcSysDateTime = _ZxAnRtcSysDateTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 101, 1),
    _ZxAnRtcSysDateTime_Type()
)
zxAnRtcSysDateTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnRtcSysDateTime.setStatus("current")


class _ZxAnRtcZoneType_Type(Integer32):
    """Custom type zxAnRtcZoneType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("east", 1),
          ("west", 2),
          ("zero", 3))
    )


_ZxAnRtcZoneType_Type.__name__ = "Integer32"
_ZxAnRtcZoneType_Object = MibScalar
zxAnRtcZoneType = _ZxAnRtcZoneType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 101, 2),
    _ZxAnRtcZoneType_Type()
)
zxAnRtcZoneType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnRtcZoneType.setStatus("current")
_ZxAnRtcZoneHours_Type = Integer32
_ZxAnRtcZoneHours_Object = MibScalar
zxAnRtcZoneHours = _ZxAnRtcZoneHours_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 101, 3),
    _ZxAnRtcZoneHours_Type()
)
zxAnRtcZoneHours.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnRtcZoneHours.setStatus("current")
_ZxAnSysNtpMgmt_ObjectIdentity = ObjectIdentity
zxAnSysNtpMgmt = _ZxAnSysNtpMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 101, 4)
)


class _ZxAnSysNtpEnable_Type(Integer32):
    """Custom type zxAnSysNtpEnable based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_ZxAnSysNtpEnable_Type.__name__ = "Integer32"
_ZxAnSysNtpEnable_Object = MibScalar
zxAnSysNtpEnable = _ZxAnSysNtpEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 101, 4, 1),
    _ZxAnSysNtpEnable_Type()
)
zxAnSysNtpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnSysNtpEnable.setStatus("current")
_ZxAnSysNtpServerAddr_Type = IpAddress
_ZxAnSysNtpServerAddr_Object = MibScalar
zxAnSysNtpServerAddr = _ZxAnSysNtpServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 101, 4, 2),
    _ZxAnSysNtpServerAddr_Type()
)
zxAnSysNtpServerAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnSysNtpServerAddr.setStatus("current")
_ZxAnSysNtpClientAddr_Type = IpAddress
_ZxAnSysNtpClientAddr_Object = MibScalar
zxAnSysNtpClientAddr = _ZxAnSysNtpClientAddr_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 101, 4, 3),
    _ZxAnSysNtpClientAddr_Type()
)
zxAnSysNtpClientAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnSysNtpClientAddr.setStatus("current")


class _ZxAnSysNtpProtoVersion_Type(Integer32):
    """Custom type zxAnSysNtpProtoVersion based on Integer32"""
    defaultValue = 3

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
        *(("version1", 1),
          ("version2", 2),
          ("version3", 3),
          ("version4", 4))
    )


_ZxAnSysNtpProtoVersion_Type.__name__ = "Integer32"
_ZxAnSysNtpProtoVersion_Object = MibScalar
zxAnSysNtpProtoVersion = _ZxAnSysNtpProtoVersion_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 101, 4, 4),
    _ZxAnSysNtpProtoVersion_Type()
)
zxAnSysNtpProtoVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnSysNtpProtoVersion.setStatus("current")


class _ZxAnSysNtpPollInterval_Type(Integer32):
    """Custom type zxAnSysNtpPollInterval based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 86400),
    )


_ZxAnSysNtpPollInterval_Type.__name__ = "Integer32"
_ZxAnSysNtpPollInterval_Object = MibScalar
zxAnSysNtpPollInterval = _ZxAnSysNtpPollInterval_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 101, 4, 5),
    _ZxAnSysNtpPollInterval_Type()
)
zxAnSysNtpPollInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnSysNtpPollInterval.setStatus("current")
if mibBuilder.loadTexts:
    zxAnSysNtpPollInterval.setUnits("seconds")


class _ZxAnSysNtpStatusCurrentState_Type(Integer32):
    """Custom type zxAnSysNtpStatusCurrentState based on Integer32"""
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
        *(("unknown", 1),
          ("notRunning", 2),
          ("notSynchronized", 3),
          ("noneConfigured", 4),
          ("syncToLocal", 5),
          ("syncToRefclock", 6),
          ("syncToRemoteServer", 7))
    )


_ZxAnSysNtpStatusCurrentState_Type.__name__ = "Integer32"
_ZxAnSysNtpStatusCurrentState_Object = MibScalar
zxAnSysNtpStatusCurrentState = _ZxAnSysNtpStatusCurrentState_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 101, 4, 6),
    _ZxAnSysNtpStatusCurrentState_Type()
)
zxAnSysNtpStatusCurrentState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSysNtpStatusCurrentState.setStatus("current")
_ZxAnSysNtpStratum_Type = Integer32
_ZxAnSysNtpStratum_Object = MibScalar
zxAnSysNtpStratum = _ZxAnSysNtpStratum_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 101, 4, 7),
    _ZxAnSysNtpStratum_Type()
)
zxAnSysNtpStratum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSysNtpStratum.setStatus("current")
_ZxAnSysNtpCurrentOffset_Type = DisplayString
_ZxAnSysNtpCurrentOffset_Object = MibScalar
zxAnSysNtpCurrentOffset = _ZxAnSysNtpCurrentOffset_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 101, 4, 8),
    _ZxAnSysNtpCurrentOffset_Type()
)
zxAnSysNtpCurrentOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSysNtpCurrentOffset.setStatus("current")
if mibBuilder.loadTexts:
    zxAnSysNtpCurrentOffset.setUnits("seconds")


class _ZxAnSysNtpOffsetAlarmThreshold_Type(Integer32):
    """Custom type zxAnSysNtpOffsetAlarmThreshold based on Integer32"""
    defaultValue = 7000


_ZxAnSysNtpOffsetAlarmThreshold_Type.__name__ = "Integer32"
_ZxAnSysNtpOffsetAlarmThreshold_Object = MibScalar
zxAnSysNtpOffsetAlarmThreshold = _ZxAnSysNtpOffsetAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 101, 4, 9),
    _ZxAnSysNtpOffsetAlarmThreshold_Type()
)
zxAnSysNtpOffsetAlarmThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnSysNtpOffsetAlarmThreshold.setStatus("current")
if mibBuilder.loadTexts:
    zxAnSysNtpOffsetAlarmThreshold.setUnits("ms")


class _ZxAnSysNtpMode_Type(Integer32):
    """Custom type zxAnSysNtpMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              255)
        )
    )
    namedValues = NamedValues(
        *(("symmetricActive", 1),
          ("symmetricPassive", 2),
          ("client", 3),
          ("server", 4),
          ("broadcast", 5),
          ("unspecified", 255))
    )


_ZxAnSysNtpMode_Type.__name__ = "Integer32"
_ZxAnSysNtpMode_Object = MibScalar
zxAnSysNtpMode = _ZxAnSysNtpMode_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 101, 4, 10),
    _ZxAnSysNtpMode_Type()
)
zxAnSysNtpMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSysNtpMode.setStatus("current")


class _ZxAnSysNtpCurrServerIpAddrType_Type(InetAddressType):
    """Custom type zxAnSysNtpCurrServerIpAddrType based on InetAddressType"""
    defaultValue = 1


_ZxAnSysNtpCurrServerIpAddrType_Type.__name__ = "InetAddressType"
_ZxAnSysNtpCurrServerIpAddrType_Object = MibScalar
zxAnSysNtpCurrServerIpAddrType = _ZxAnSysNtpCurrServerIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 101, 4, 11),
    _ZxAnSysNtpCurrServerIpAddrType_Type()
)
zxAnSysNtpCurrServerIpAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSysNtpCurrServerIpAddrType.setStatus("current")
_ZxAnSysNtpCurrServerIpAddress_Type = InetAddress
_ZxAnSysNtpCurrServerIpAddress_Object = MibScalar
zxAnSysNtpCurrServerIpAddress = _ZxAnSysNtpCurrServerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 101, 4, 12),
    _ZxAnSysNtpCurrServerIpAddress_Type()
)
zxAnSysNtpCurrServerIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSysNtpCurrServerIpAddress.setStatus("current")


class _ZxAnSysNtpCurrServerVrf_Type(DisplayString):
    """Custom type zxAnSysNtpCurrServerVrf based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ZxAnSysNtpCurrServerVrf_Type.__name__ = "DisplayString"
_ZxAnSysNtpCurrServerVrf_Object = MibScalar
zxAnSysNtpCurrServerVrf = _ZxAnSysNtpCurrServerVrf_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 101, 4, 13),
    _ZxAnSysNtpCurrServerVrf_Type()
)
zxAnSysNtpCurrServerVrf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSysNtpCurrServerVrf.setStatus("current")


class _ZxAnSysNtpClientAddrType_Type(InetAddressType):
    """Custom type zxAnSysNtpClientAddrType based on InetAddressType"""
    defaultValue = 1


_ZxAnSysNtpClientAddrType_Type.__name__ = "InetAddressType"
_ZxAnSysNtpClientAddrType_Object = MibScalar
zxAnSysNtpClientAddrType = _ZxAnSysNtpClientAddrType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 101, 4, 14),
    _ZxAnSysNtpClientAddrType_Type()
)
zxAnSysNtpClientAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnSysNtpClientAddrType.setStatus("current")
_ZxAnSysNtpClientAddrIpv6_Type = InetAddress
_ZxAnSysNtpClientAddrIpv6_Object = MibScalar
zxAnSysNtpClientAddrIpv6 = _ZxAnSysNtpClientAddrIpv6_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 101, 4, 15),
    _ZxAnSysNtpClientAddrIpv6_Type()
)
zxAnSysNtpClientAddrIpv6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnSysNtpClientAddrIpv6.setStatus("current")


class _ZxAnSysNtpAuthenticationEnable_Type(Integer32):
    """Custom type zxAnSysNtpAuthenticationEnable based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_ZxAnSysNtpAuthenticationEnable_Type.__name__ = "Integer32"
_ZxAnSysNtpAuthenticationEnable_Object = MibScalar
zxAnSysNtpAuthenticationEnable = _ZxAnSysNtpAuthenticationEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 101, 4, 16),
    _ZxAnSysNtpAuthenticationEnable_Type()
)
zxAnSysNtpAuthenticationEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnSysNtpAuthenticationEnable.setStatus("current")
_ZxAnSysNtpServerTable_Object = MibTable
zxAnSysNtpServerTable = _ZxAnSysNtpServerTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 101, 4, 51)
)
if mibBuilder.loadTexts:
    zxAnSysNtpServerTable.setStatus("current")
_ZxAnSysNtpServerEntry_Object = MibTableRow
zxAnSysNtpServerEntry = _ZxAnSysNtpServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 101, 4, 51, 1)
)
zxAnSysNtpServerEntry.setIndexNames(
    (0, "ZTE-AN-SYS-MIB", "zxAnSysNtpServerPriority"),
)
if mibBuilder.loadTexts:
    zxAnSysNtpServerEntry.setStatus("current")


class _ZxAnSysNtpServerPriority_Type(Integer32):
    """Custom type zxAnSysNtpServerPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_ZxAnSysNtpServerPriority_Type.__name__ = "Integer32"
_ZxAnSysNtpServerPriority_Object = MibTableColumn
zxAnSysNtpServerPriority = _ZxAnSysNtpServerPriority_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 101, 4, 51, 1, 1),
    _ZxAnSysNtpServerPriority_Type()
)
zxAnSysNtpServerPriority.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnSysNtpServerPriority.setStatus("current")


class _ZxAnSysNtpServerVrf_Type(DisplayString):
    """Custom type zxAnSysNtpServerVrf based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ZxAnSysNtpServerVrf_Type.__name__ = "DisplayString"
_ZxAnSysNtpServerVrf_Object = MibTableColumn
zxAnSysNtpServerVrf = _ZxAnSysNtpServerVrf_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 101, 4, 51, 1, 2),
    _ZxAnSysNtpServerVrf_Type()
)
zxAnSysNtpServerVrf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnSysNtpServerVrf.setStatus("current")


class _ZxAnSysNtpServerIpAddressType_Type(InetAddressType):
    """Custom type zxAnSysNtpServerIpAddressType based on InetAddressType"""
    defaultValue = 1


_ZxAnSysNtpServerIpAddressType_Type.__name__ = "InetAddressType"
_ZxAnSysNtpServerIpAddressType_Object = MibTableColumn
zxAnSysNtpServerIpAddressType = _ZxAnSysNtpServerIpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 101, 4, 51, 1, 3),
    _ZxAnSysNtpServerIpAddressType_Type()
)
zxAnSysNtpServerIpAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnSysNtpServerIpAddressType.setStatus("current")
_ZxAnSysNtpServerIpAddress_Type = InetAddress
_ZxAnSysNtpServerIpAddress_Object = MibTableColumn
zxAnSysNtpServerIpAddress = _ZxAnSysNtpServerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 101, 4, 51, 1, 4),
    _ZxAnSysNtpServerIpAddress_Type()
)
zxAnSysNtpServerIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnSysNtpServerIpAddress.setStatus("current")


class _ZxAnSysNtpServerVersion_Type(Integer32):
    """Custom type zxAnSysNtpServerVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_ZxAnSysNtpServerVersion_Type.__name__ = "Integer32"
_ZxAnSysNtpServerVersion_Object = MibTableColumn
zxAnSysNtpServerVersion = _ZxAnSysNtpServerVersion_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 101, 4, 51, 1, 5),
    _ZxAnSysNtpServerVersion_Type()
)
zxAnSysNtpServerVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnSysNtpServerVersion.setStatus("current")


class _ZxAnSysNtpServerAuthKeyId_Type(Integer32):
    """Custom type zxAnSysNtpServerAuthKeyId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ZxAnSysNtpServerAuthKeyId_Type.__name__ = "Integer32"
_ZxAnSysNtpServerAuthKeyId_Object = MibTableColumn
zxAnSysNtpServerAuthKeyId = _ZxAnSysNtpServerAuthKeyId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 101, 4, 51, 1, 6),
    _ZxAnSysNtpServerAuthKeyId_Type()
)
zxAnSysNtpServerAuthKeyId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnSysNtpServerAuthKeyId.setStatus("current")


class _ZxAnSysNtpServerLock_Type(Integer32):
    """Custom type zxAnSysNtpServerLock based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("lock", 1),
          ("unlock", 2))
    )


_ZxAnSysNtpServerLock_Type.__name__ = "Integer32"
_ZxAnSysNtpServerLock_Object = MibTableColumn
zxAnSysNtpServerLock = _ZxAnSysNtpServerLock_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 101, 4, 51, 1, 7),
    _ZxAnSysNtpServerLock_Type()
)
zxAnSysNtpServerLock.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnSysNtpServerLock.setStatus("current")
_ZxAnSysNtpServerRowStatus_Type = RowStatus
_ZxAnSysNtpServerRowStatus_Object = MibTableColumn
zxAnSysNtpServerRowStatus = _ZxAnSysNtpServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 101, 4, 51, 1, 30),
    _ZxAnSysNtpServerRowStatus_Type()
)
zxAnSysNtpServerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnSysNtpServerRowStatus.setStatus("current")
_ZxAnSysNtpAuthenticationTable_Object = MibTable
zxAnSysNtpAuthenticationTable = _ZxAnSysNtpAuthenticationTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 101, 4, 52)
)
if mibBuilder.loadTexts:
    zxAnSysNtpAuthenticationTable.setStatus("current")
_ZxAnSysNtpAuthenticationEntry_Object = MibTableRow
zxAnSysNtpAuthenticationEntry = _ZxAnSysNtpAuthenticationEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 101, 4, 52, 1)
)
zxAnSysNtpAuthenticationEntry.setIndexNames(
    (0, "ZTE-AN-SYS-MIB", "zxAnSysNtpAuthenticationKeyId"),
)
if mibBuilder.loadTexts:
    zxAnSysNtpAuthenticationEntry.setStatus("current")


class _ZxAnSysNtpAuthenticationKeyId_Type(Integer32):
    """Custom type zxAnSysNtpAuthenticationKeyId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_ZxAnSysNtpAuthenticationKeyId_Type.__name__ = "Integer32"
_ZxAnSysNtpAuthenticationKeyId_Object = MibTableColumn
zxAnSysNtpAuthenticationKeyId = _ZxAnSysNtpAuthenticationKeyId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 101, 4, 52, 1, 1),
    _ZxAnSysNtpAuthenticationKeyId_Type()
)
zxAnSysNtpAuthenticationKeyId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnSysNtpAuthenticationKeyId.setStatus("current")


class _ZxAnSysNtpAuthenticationKey_Type(DisplayString):
    """Custom type zxAnSysNtpAuthenticationKey based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_ZxAnSysNtpAuthenticationKey_Type.__name__ = "DisplayString"
_ZxAnSysNtpAuthenticationKey_Object = MibTableColumn
zxAnSysNtpAuthenticationKey = _ZxAnSysNtpAuthenticationKey_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 101, 4, 52, 1, 2),
    _ZxAnSysNtpAuthenticationKey_Type()
)
zxAnSysNtpAuthenticationKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnSysNtpAuthenticationKey.setStatus("current")
_ZxAnSysNtpAuthenticationTrust_Type = TruthValue
_ZxAnSysNtpAuthenticationTrust_Object = MibTableColumn
zxAnSysNtpAuthenticationTrust = _ZxAnSysNtpAuthenticationTrust_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 101, 4, 52, 1, 3),
    _ZxAnSysNtpAuthenticationTrust_Type()
)
zxAnSysNtpAuthenticationTrust.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnSysNtpAuthenticationTrust.setStatus("current")
_ZxAnSysNtpAuthRowStatus_Type = RowStatus
_ZxAnSysNtpAuthRowStatus_Object = MibTableColumn
zxAnSysNtpAuthRowStatus = _ZxAnSysNtpAuthRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 101, 4, 52, 1, 30),
    _ZxAnSysNtpAuthRowStatus_Type()
)
zxAnSysNtpAuthRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnSysNtpAuthRowStatus.setStatus("current")
_ZxAnSysNtpIfConfigTable_Object = MibTable
zxAnSysNtpIfConfigTable = _ZxAnSysNtpIfConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 101, 4, 53)
)
if mibBuilder.loadTexts:
    zxAnSysNtpIfConfigTable.setStatus("current")
_ZxAnSysNtpIfConfigEntry_Object = MibTableRow
zxAnSysNtpIfConfigEntry = _ZxAnSysNtpIfConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 101, 4, 53, 1)
)
zxAnSysNtpIfConfigEntry.setIndexNames(
    (0, "ZTE-AN-SYS-MIB", "zxAnSysNtpIfIndex"),
)
if mibBuilder.loadTexts:
    zxAnSysNtpIfConfigEntry.setStatus("current")
_ZxAnSysNtpIfIndex_Type = ZxAnIfindex
_ZxAnSysNtpIfIndex_Object = MibTableColumn
zxAnSysNtpIfIndex = _ZxAnSysNtpIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 101, 4, 53, 1, 1),
    _ZxAnSysNtpIfIndex_Type()
)
zxAnSysNtpIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnSysNtpIfIndex.setStatus("current")


class _ZxAnSysNtpIfBroadcastClientEn_Type(Integer32):
    """Custom type zxAnSysNtpIfBroadcastClientEn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_ZxAnSysNtpIfBroadcastClientEn_Type.__name__ = "Integer32"
_ZxAnSysNtpIfBroadcastClientEn_Object = MibTableColumn
zxAnSysNtpIfBroadcastClientEn = _ZxAnSysNtpIfBroadcastClientEn_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 101, 4, 53, 1, 2),
    _ZxAnSysNtpIfBroadcastClientEn_Type()
)
zxAnSysNtpIfBroadcastClientEn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnSysNtpIfBroadcastClientEn.setStatus("current")


class _ZxAnSysNtpIfMulticastClientEn_Type(Integer32):
    """Custom type zxAnSysNtpIfMulticastClientEn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_ZxAnSysNtpIfMulticastClientEn_Type.__name__ = "Integer32"
_ZxAnSysNtpIfMulticastClientEn_Object = MibTableColumn
zxAnSysNtpIfMulticastClientEn = _ZxAnSysNtpIfMulticastClientEn_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 101, 4, 53, 1, 3),
    _ZxAnSysNtpIfMulticastClientEn_Type()
)
zxAnSysNtpIfMulticastClientEn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnSysNtpIfMulticastClientEn.setStatus("current")


class _ZxAnSysNtpIfMulticastIpAddrType_Type(InetAddressType):
    """Custom type zxAnSysNtpIfMulticastIpAddrType based on InetAddressType"""
    defaultValue = 1


_ZxAnSysNtpIfMulticastIpAddrType_Type.__name__ = "InetAddressType"
_ZxAnSysNtpIfMulticastIpAddrType_Object = MibTableColumn
zxAnSysNtpIfMulticastIpAddrType = _ZxAnSysNtpIfMulticastIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 101, 4, 53, 1, 4),
    _ZxAnSysNtpIfMulticastIpAddrType_Type()
)
zxAnSysNtpIfMulticastIpAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnSysNtpIfMulticastIpAddrType.setStatus("current")
_ZxAnSysNtpIfMulticastIpAddr_Type = InetAddress
_ZxAnSysNtpIfMulticastIpAddr_Object = MibTableColumn
zxAnSysNtpIfMulticastIpAddr = _ZxAnSysNtpIfMulticastIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 101, 4, 53, 1, 5),
    _ZxAnSysNtpIfMulticastIpAddr_Type()
)
zxAnSysNtpIfMulticastIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnSysNtpIfMulticastIpAddr.setStatus("current")
_ZxAnSysNtpIfConfigRowStatus_Type = RowStatus
_ZxAnSysNtpIfConfigRowStatus_Object = MibTableColumn
zxAnSysNtpIfConfigRowStatus = _ZxAnSysNtpIfConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 101, 4, 53, 1, 30),
    _ZxAnSysNtpIfConfigRowStatus_Type()
)
zxAnSysNtpIfConfigRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnSysNtpIfConfigRowStatus.setStatus("current")


class _ZxAnRtcZoneAlias_Type(DisplayString):
    """Custom type zxAnRtcZoneAlias based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_ZxAnRtcZoneAlias_Type.__name__ = "DisplayString"
_ZxAnRtcZoneAlias_Object = MibScalar
zxAnRtcZoneAlias = _ZxAnRtcZoneAlias_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 101, 5),
    _ZxAnRtcZoneAlias_Type()
)
zxAnRtcZoneAlias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnRtcZoneAlias.setStatus("current")


class _ZxAnRtcZoneMinutes_Type(Integer32):
    """Custom type zxAnRtcZoneMinutes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60),
    )


_ZxAnRtcZoneMinutes_Type.__name__ = "Integer32"
_ZxAnRtcZoneMinutes_Object = MibScalar
zxAnRtcZoneMinutes = _ZxAnRtcZoneMinutes_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 101, 6),
    _ZxAnRtcZoneMinutes_Type()
)
zxAnRtcZoneMinutes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnRtcZoneMinutes.setStatus("current")
_ZxAnSysSummerTimeMgmt_ObjectIdentity = ObjectIdentity
zxAnSysSummerTimeMgmt = _ZxAnSysSummerTimeMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 101, 7)
)


class _ZxAnRtcSummerTimeAdminStatus_Type(Integer32):
    """Custom type zxAnRtcSummerTimeAdminStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_ZxAnRtcSummerTimeAdminStatus_Type.__name__ = "Integer32"
_ZxAnRtcSummerTimeAdminStatus_Object = MibScalar
zxAnRtcSummerTimeAdminStatus = _ZxAnRtcSummerTimeAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 101, 7, 1),
    _ZxAnRtcSummerTimeAdminStatus_Type()
)
zxAnRtcSummerTimeAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnRtcSummerTimeAdminStatus.setStatus("current")


class _ZxAnRtcSummerTimeName_Type(DisplayString):
    """Custom type zxAnRtcSummerTimeName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_ZxAnRtcSummerTimeName_Type.__name__ = "DisplayString"
_ZxAnRtcSummerTimeName_Object = MibScalar
zxAnRtcSummerTimeName = _ZxAnRtcSummerTimeName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 101, 7, 2),
    _ZxAnRtcSummerTimeName_Type()
)
zxAnRtcSummerTimeName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnRtcSummerTimeName.setStatus("current")


class _ZxAnRtcSummerTimeType_Type(Integer32):
    """Custom type zxAnRtcSummerTimeType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("once", 1),
          ("recurring", 2))
    )


_ZxAnRtcSummerTimeType_Type.__name__ = "Integer32"
_ZxAnRtcSummerTimeType_Object = MibScalar
zxAnRtcSummerTimeType = _ZxAnRtcSummerTimeType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 101, 7, 3),
    _ZxAnRtcSummerTimeType_Type()
)
zxAnRtcSummerTimeType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnRtcSummerTimeType.setStatus("current")


class _ZxAnRtcSummerTimeStart_Type(DisplayString):
    """Custom type zxAnRtcSummerTimeStart based on DisplayString"""
    defaultValue = OctetString("ff-01-03 02:00:00")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_ZxAnRtcSummerTimeStart_Type.__name__ = "DisplayString"
_ZxAnRtcSummerTimeStart_Object = MibScalar
zxAnRtcSummerTimeStart = _ZxAnRtcSummerTimeStart_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 101, 7, 4),
    _ZxAnRtcSummerTimeStart_Type()
)
zxAnRtcSummerTimeStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnRtcSummerTimeStart.setStatus("current")


class _ZxAnRtcSummerTimeEnd_Type(DisplayString):
    """Custom type zxAnRtcSummerTimeEnd based on DisplayString"""
    defaultValue = OctetString("ff-01-10 02:00:00")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_ZxAnRtcSummerTimeEnd_Type.__name__ = "DisplayString"
_ZxAnRtcSummerTimeEnd_Object = MibScalar
zxAnRtcSummerTimeEnd = _ZxAnRtcSummerTimeEnd_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 101, 7, 5),
    _ZxAnRtcSummerTimeEnd_Type()
)
zxAnRtcSummerTimeEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnRtcSummerTimeEnd.setStatus("current")


class _ZxAnRtcSummerTimeOffset_Type(Integer32):
    """Custom type zxAnRtcSummerTimeOffset based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 300),
    )


_ZxAnRtcSummerTimeOffset_Type.__name__ = "Integer32"
_ZxAnRtcSummerTimeOffset_Object = MibScalar
zxAnRtcSummerTimeOffset = _ZxAnRtcSummerTimeOffset_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 101, 7, 6),
    _ZxAnRtcSummerTimeOffset_Type()
)
zxAnRtcSummerTimeOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnRtcSummerTimeOffset.setStatus("current")
if mibBuilder.loadTexts:
    zxAnRtcSummerTimeOffset.setUnits("minute")


class _ZxAnRtcSummerTimeOperStatus_Type(Integer32):
    """Custom type zxAnRtcSummerTimeOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("summertime", 1),
          ("standard", 2))
    )


_ZxAnRtcSummerTimeOperStatus_Type.__name__ = "Integer32"
_ZxAnRtcSummerTimeOperStatus_Object = MibScalar
zxAnRtcSummerTimeOperStatus = _ZxAnRtcSummerTimeOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 101, 7, 7),
    _ZxAnRtcSummerTimeOperStatus_Type()
)
zxAnRtcSummerTimeOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnRtcSummerTimeOperStatus.setStatus("current")
_ZxAnSysPtpMgmt_ObjectIdentity = ObjectIdentity
zxAnSysPtpMgmt = _ZxAnSysPtpMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 101, 8)
)
_ZxAnSysPtpGlobalObjects_ObjectIdentity = ObjectIdentity
zxAnSysPtpGlobalObjects = _ZxAnSysPtpGlobalObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 101, 8, 1)
)


class _ZxAnSysPtpConfigClockMode_Type(Integer32):
    """Custom type zxAnSysPtpConfigClockMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ordinary", 1),
          ("boundary", 2))
    )


_ZxAnSysPtpConfigClockMode_Type.__name__ = "Integer32"
_ZxAnSysPtpConfigClockMode_Object = MibScalar
zxAnSysPtpConfigClockMode = _ZxAnSysPtpConfigClockMode_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 101, 8, 1, 1),
    _ZxAnSysPtpConfigClockMode_Type()
)
zxAnSysPtpConfigClockMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnSysPtpConfigClockMode.setStatus("current")


class _ZxAnSysPtpConfigTsc_Type(TruthValue):
    """Custom type zxAnSysPtpConfigTsc based on TruthValue"""
    defaultValue = 1


_ZxAnSysPtpConfigTsc_Type.__name__ = "TruthValue"
_ZxAnSysPtpConfigTsc_Object = MibScalar
zxAnSysPtpConfigTsc = _ZxAnSysPtpConfigTsc_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 101, 8, 1, 2),
    _ZxAnSysPtpConfigTsc_Type()
)
zxAnSysPtpConfigTsc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnSysPtpConfigTsc.setStatus("current")


class _ZxAnSysPtpServiceVlan_Type(Integer32):
    """Custom type zxAnSysPtpServiceVlan based on Integer32"""
    defaultValue = 1


_ZxAnSysPtpServiceVlan_Type.__name__ = "Integer32"
_ZxAnSysPtpServiceVlan_Object = MibScalar
zxAnSysPtpServiceVlan = _ZxAnSysPtpServiceVlan_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 101, 8, 1, 3),
    _ZxAnSysPtpServiceVlan_Type()
)
zxAnSysPtpServiceVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnSysPtpServiceVlan.setStatus("current")


class _ZxAnSysPtpTodTransMode_Type(Integer32):
    """Custom type zxAnSysPtpTodTransMode based on Integer32"""
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
        *(("transparent", 1),
          ("untransmit", 2),
          ("local", 3))
    )


_ZxAnSysPtpTodTransMode_Type.__name__ = "Integer32"
_ZxAnSysPtpTodTransMode_Object = MibScalar
zxAnSysPtpTodTransMode = _ZxAnSysPtpTodTransMode_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 101, 8, 1, 4),
    _ZxAnSysPtpTodTransMode_Type()
)
zxAnSysPtpTodTransMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnSysPtpTodTransMode.setStatus("current")


class _ZxAnSysPtpTodSignalType_Type(Integer32):
    """Custom type zxAnSysPtpTodSignalType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("chinaMobile", 1),
          ("chinaTelecom", 2))
    )


_ZxAnSysPtpTodSignalType_Type.__name__ = "Integer32"
_ZxAnSysPtpTodSignalType_Object = MibScalar
zxAnSysPtpTodSignalType = _ZxAnSysPtpTodSignalType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 101, 8, 1, 5),
    _ZxAnSysPtpTodSignalType_Type()
)
zxAnSysPtpTodSignalType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnSysPtpTodSignalType.setStatus("current")
_ZxAnSysPtpPortTable_Object = MibTable
zxAnSysPtpPortTable = _ZxAnSysPtpPortTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 101, 8, 2)
)
if mibBuilder.loadTexts:
    zxAnSysPtpPortTable.setStatus("current")
_ZxAnSysPtpPortEntry_Object = MibTableRow
zxAnSysPtpPortEntry = _ZxAnSysPtpPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 101, 8, 2, 1)
)
zxAnSysPtpPortEntry.setIndexNames(
    (0, "ZTE-AN-SYS-MIB", "zxAnSysPtpPortIndex"),
)
if mibBuilder.loadTexts:
    zxAnSysPtpPortEntry.setStatus("current")


class _ZxAnSysPtpPortIndex_Type(Integer32):
    """Custom type zxAnSysPtpPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_ZxAnSysPtpPortIndex_Type.__name__ = "Integer32"
_ZxAnSysPtpPortIndex_Object = MibTableColumn
zxAnSysPtpPortIndex = _ZxAnSysPtpPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 101, 8, 2, 1, 1),
    _ZxAnSysPtpPortIndex_Type()
)
zxAnSysPtpPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnSysPtpPortIndex.setStatus("current")


class _ZxAnSysPtpPortConfState_Type(Integer32):
    """Custom type zxAnSysPtpPortConfState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("master", 1),
          ("slave", 2))
    )


_ZxAnSysPtpPortConfState_Type.__name__ = "Integer32"
_ZxAnSysPtpPortConfState_Object = MibTableColumn
zxAnSysPtpPortConfState = _ZxAnSysPtpPortConfState_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 101, 8, 2, 1, 2),
    _ZxAnSysPtpPortConfState_Type()
)
zxAnSysPtpPortConfState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnSysPtpPortConfState.setStatus("current")


class _ZxAnSysPtpPortSyncInterval_Type(Integer32):
    """Custom type zxAnSysPtpPortSyncInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_ZxAnSysPtpPortSyncInterval_Type.__name__ = "Integer32"
_ZxAnSysPtpPortSyncInterval_Object = MibTableColumn
zxAnSysPtpPortSyncInterval = _ZxAnSysPtpPortSyncInterval_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 101, 8, 2, 1, 3),
    _ZxAnSysPtpPortSyncInterval_Type()
)
zxAnSysPtpPortSyncInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnSysPtpPortSyncInterval.setStatus("current")
if mibBuilder.loadTexts:
    zxAnSysPtpPortSyncInterval.setUnits("pps")
_ZxAnSysPtpPortClockDestIpAddress_Type = InetAddress
_ZxAnSysPtpPortClockDestIpAddress_Object = MibTableColumn
zxAnSysPtpPortClockDestIpAddress = _ZxAnSysPtpPortClockDestIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 101, 8, 2, 1, 4),
    _ZxAnSysPtpPortClockDestIpAddress_Type()
)
zxAnSysPtpPortClockDestIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnSysPtpPortClockDestIpAddress.setStatus("current")
_ZxAnSysPtpPortRowStatus_Type = RowStatus
_ZxAnSysPtpPortRowStatus_Object = MibTableColumn
zxAnSysPtpPortRowStatus = _ZxAnSysPtpPortRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 101, 8, 2, 1, 20),
    _ZxAnSysPtpPortRowStatus_Type()
)
zxAnSysPtpPortRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnSysPtpPortRowStatus.setStatus("current")
_ZxAnSysSnmpOperSyslogMgmt_ObjectIdentity = ObjectIdentity
zxAnSysSnmpOperSyslogMgmt = _ZxAnSysSnmpOperSyslogMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 102)
)


class _ZxAnSysSnmpOperSyslogStatus_Type(Integer32):
    """Custom type zxAnSysSnmpOperSyslogStatus based on Integer32"""
    defaultValue = 4

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
        *(("logRead", 1),
          ("logWrite", 2),
          ("logReadAndWrite", 3),
          ("logNone", 4))
    )


_ZxAnSysSnmpOperSyslogStatus_Type.__name__ = "Integer32"
_ZxAnSysSnmpOperSyslogStatus_Object = MibScalar
zxAnSysSnmpOperSyslogStatus = _ZxAnSysSnmpOperSyslogStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 102, 1),
    _ZxAnSysSnmpOperSyslogStatus_Type()
)
zxAnSysSnmpOperSyslogStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnSysSnmpOperSyslogStatus.setStatus("current")
_ZxAnSysSnmpOperOidExceptTable_Object = MibTable
zxAnSysSnmpOperOidExceptTable = _ZxAnSysSnmpOperOidExceptTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 102, 10)
)
if mibBuilder.loadTexts:
    zxAnSysSnmpOperOidExceptTable.setStatus("current")
_ZxAnSysSnmpOperOidExceptEntry_Object = MibTableRow
zxAnSysSnmpOperOidExceptEntry = _ZxAnSysSnmpOperOidExceptEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 102, 10, 1)
)
zxAnSysSnmpOperOidExceptEntry.setIndexNames(
    (0, "ZTE-AN-SYS-MIB", "zxAnSysSnmpOidId"),
)
if mibBuilder.loadTexts:
    zxAnSysSnmpOperOidExceptEntry.setStatus("current")


class _ZxAnSysSnmpOidId_Type(Integer32):
    """Custom type zxAnSysSnmpOidId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_ZxAnSysSnmpOidId_Type.__name__ = "Integer32"
_ZxAnSysSnmpOidId_Object = MibTableColumn
zxAnSysSnmpOidId = _ZxAnSysSnmpOidId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 102, 10, 1, 1),
    _ZxAnSysSnmpOidId_Type()
)
zxAnSysSnmpOidId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnSysSnmpOidId.setStatus("current")
_ZxAnSysSnmpOidItem_Type = DisplayString
_ZxAnSysSnmpOidItem_Object = MibTableColumn
zxAnSysSnmpOidItem = _ZxAnSysSnmpOidItem_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 102, 10, 1, 2),
    _ZxAnSysSnmpOidItem_Type()
)
zxAnSysSnmpOidItem.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnSysSnmpOidItem.setStatus("current")
_ZxAnSysSnmpOidRowStatus_Type = RowStatus
_ZxAnSysSnmpOidRowStatus_Object = MibTableColumn
zxAnSysSnmpOidRowStatus = _ZxAnSysSnmpOidRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 102, 10, 1, 10),
    _ZxAnSysSnmpOidRowStatus_Type()
)
zxAnSysSnmpOidRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnSysSnmpOidRowStatus.setStatus("current")
_ZxAnLog_ObjectIdentity = ObjectIdentity
zxAnLog = _ZxAnLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 103)
)
_ZxAnLogTypeTable_Object = MibTable
zxAnLogTypeTable = _ZxAnLogTypeTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 103, 1)
)
if mibBuilder.loadTexts:
    zxAnLogTypeTable.setStatus("current")
_ZxAnLogTypeEntry_Object = MibTableRow
zxAnLogTypeEntry = _ZxAnLogTypeEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 103, 1, 1)
)
zxAnLogTypeEntry.setIndexNames(
    (0, "ZTE-AN-SYS-MIB", "zxAnLogType"),
    (0, "ZTE-AN-SYS-MIB", "zxAnLogLevel"),
)
if mibBuilder.loadTexts:
    zxAnLogTypeEntry.setStatus("current")
_ZxAnLogType_Type = Integer32
_ZxAnLogType_Object = MibTableColumn
zxAnLogType = _ZxAnLogType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 103, 1, 1, 1),
    _ZxAnLogType_Type()
)
zxAnLogType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnLogType.setStatus("current")
_ZxAnLogLevel_Type = Integer32
_ZxAnLogLevel_Object = MibTableColumn
zxAnLogLevel = _ZxAnLogLevel_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 103, 1, 1, 2),
    _ZxAnLogLevel_Type()
)
zxAnLogLevel.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnLogLevel.setStatus("current")


class _ZxAnLogTypeDesc_Type(DisplayString):
    """Custom type zxAnLogTypeDesc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_ZxAnLogTypeDesc_Type.__name__ = "DisplayString"
_ZxAnLogTypeDesc_Object = MibTableColumn
zxAnLogTypeDesc = _ZxAnLogTypeDesc_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 103, 1, 1, 3),
    _ZxAnLogTypeDesc_Type()
)
zxAnLogTypeDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnLogTypeDesc.setStatus("current")
_ZxAnLogConfTable_Object = MibTable
zxAnLogConfTable = _ZxAnLogConfTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 103, 2)
)
if mibBuilder.loadTexts:
    zxAnLogConfTable.setStatus("current")
_ZxAnLogConfEntry_Object = MibTableRow
zxAnLogConfEntry = _ZxAnLogConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 103, 2, 1)
)
zxAnLogConfEntry.setIndexNames(
    (0, "ZTE-AN-SYS-MIB", "zxAnLogConfType"),
    (0, "ZTE-AN-SYS-MIB", "zxAnLogConfLevel"),
)
if mibBuilder.loadTexts:
    zxAnLogConfEntry.setStatus("current")
_ZxAnLogConfType_Type = Integer32
_ZxAnLogConfType_Object = MibTableColumn
zxAnLogConfType = _ZxAnLogConfType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 103, 2, 1, 1),
    _ZxAnLogConfType_Type()
)
zxAnLogConfType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnLogConfType.setStatus("current")
_ZxAnLogConfLevel_Type = Integer32
_ZxAnLogConfLevel_Object = MibTableColumn
zxAnLogConfLevel = _ZxAnLogConfLevel_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 103, 2, 1, 2),
    _ZxAnLogConfLevel_Type()
)
zxAnLogConfLevel.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnLogConfLevel.setStatus("current")


class _ZxAnLogCapability_Type(Bits):
    """Custom type zxAnLogCapability based on Bits"""
    namedValues = NamedValues(
        *(("syslog", 0),
          ("memory", 1),
          ("highMemory", 2),
          ("flash", 3),
          ("reserved1", 4),
          ("reserved2", 5),
          ("reserved3", 6),
          ("reserved4", 7))
    )

_ZxAnLogCapability_Type.__name__ = "Bits"
_ZxAnLogCapability_Object = MibTableColumn
zxAnLogCapability = _ZxAnLogCapability_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 103, 2, 1, 3),
    _ZxAnLogCapability_Type()
)
zxAnLogCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnLogCapability.setStatus("current")


class _ZxAnLogConfig_Type(Bits):
    """Custom type zxAnLogConfig based on Bits"""
    namedValues = NamedValues(
        *(("syslog", 0),
          ("memory", 1),
          ("highMemory", 2),
          ("flash", 3),
          ("reserved1", 4),
          ("reserved2", 5),
          ("reserved3", 6),
          ("reserved4", 7))
    )

_ZxAnLogConfig_Type.__name__ = "Bits"
_ZxAnLogConfig_Object = MibTableColumn
zxAnLogConfig = _ZxAnLogConfig_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 103, 2, 1, 4),
    _ZxAnLogConfig_Type()
)
zxAnLogConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnLogConfig.setStatus("current")
_ZxAnLogGlobalObjects_ObjectIdentity = ObjectIdentity
zxAnLogGlobalObjects = _ZxAnLogGlobalObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 103, 10)
)
_ZxAnLogClear_Type = Integer32
_ZxAnLogClear_Object = MibScalar
zxAnLogClear = _ZxAnLogClear_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 103, 10, 1),
    _ZxAnLogClear_Type()
)
zxAnLogClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnLogClear.setStatus("current")
_ZxAnSysClockMgmt_ObjectIdentity = ObjectIdentity
zxAnSysClockMgmt = _ZxAnSysClockMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 104)
)


class _ZxAnSysConfigClockSource_Type(Integer32):
    """Custom type zxAnSysConfigClockSource based on Integer32"""
    defaultValue = 7

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
        *(("bitse1", 1),
          ("bits2m", 2),
          ("est2m", 3),
          ("ttl2m", 4),
          ("e12ml", 5),
          ("e12mr", 6),
          ("default", 7))
    )


_ZxAnSysConfigClockSource_Type.__name__ = "Integer32"
_ZxAnSysConfigClockSource_Object = MibScalar
zxAnSysConfigClockSource = _ZxAnSysConfigClockSource_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 104, 1),
    _ZxAnSysConfigClockSource_Type()
)
zxAnSysConfigClockSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnSysConfigClockSource.setStatus("current")


class _ZxAnSysActualClockSource_Type(Integer32):
    """Custom type zxAnSysActualClockSource based on Integer32"""
    defaultValue = 7

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
        *(("bitse1", 1),
          ("bits2m", 2),
          ("est2m", 3),
          ("ttl2m", 4),
          ("e12ml", 5),
          ("e12mr", 6),
          ("default", 7))
    )


_ZxAnSysActualClockSource_Type.__name__ = "Integer32"
_ZxAnSysActualClockSource_Object = MibScalar
zxAnSysActualClockSource = _ZxAnSysActualClockSource_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 104, 2),
    _ZxAnSysActualClockSource_Type()
)
zxAnSysActualClockSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSysActualClockSource.setStatus("current")


class _ZxAnSysSupportClockSource_Type(Bits):
    """Custom type zxAnSysSupportClockSource based on Bits"""
    namedValues = NamedValues(
        *(("bitse1", 0),
          ("bits2m", 1),
          ("est2m", 2),
          ("ttl2m", 3),
          ("e12ml", 4),
          ("e12mr", 5),
          ("default", 6))
    )

_ZxAnSysSupportClockSource_Type.__name__ = "Bits"
_ZxAnSysSupportClockSource_Object = MibScalar
zxAnSysSupportClockSource = _ZxAnSysSupportClockSource_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 104, 3),
    _ZxAnSysSupportClockSource_Type()
)
zxAnSysSupportClockSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSysSupportClockSource.setStatus("current")


class _ZxAnSysAvailableClockSource_Type(Bits):
    """Custom type zxAnSysAvailableClockSource based on Bits"""
    namedValues = NamedValues(
        *(("bitse1", 0),
          ("bits2m", 1),
          ("est2m", 2),
          ("ttl2m", 3),
          ("e12ml", 4),
          ("e12mr", 5),
          ("default", 6))
    )

_ZxAnSysAvailableClockSource_Type.__name__ = "Bits"
_ZxAnSysAvailableClockSource_Object = MibScalar
zxAnSysAvailableClockSource = _ZxAnSysAvailableClockSource_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 104, 4),
    _ZxAnSysAvailableClockSource_Type()
)
zxAnSysAvailableClockSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSysAvailableClockSource.setStatus("current")
_ZxAnSysClockSourcePriority_Type = DisplayString
_ZxAnSysClockSourcePriority_Object = MibScalar
zxAnSysClockSourcePriority = _ZxAnSysClockSourcePriority_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 104, 5),
    _ZxAnSysClockSourcePriority_Type()
)
zxAnSysClockSourcePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnSysClockSourcePriority.setStatus("current")
_ZxAnSysActualClockSourceE1_Type = DisplayString
_ZxAnSysActualClockSourceE1_Object = MibScalar
zxAnSysActualClockSourceE1 = _ZxAnSysActualClockSourceE1_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 104, 6),
    _ZxAnSysActualClockSourceE1_Type()
)
zxAnSysActualClockSourceE1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSysActualClockSourceE1.setStatus("current")


class _ZxAnSysLastClockSource_Type(Integer32):
    """Custom type zxAnSysLastClockSource based on Integer32"""
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
        *(("bitse1", 1),
          ("bits2m", 2),
          ("est2m", 3),
          ("ttl2m", 4),
          ("e12ml", 5),
          ("e12mr", 6),
          ("default", 7))
    )


_ZxAnSysLastClockSource_Type.__name__ = "Integer32"
_ZxAnSysLastClockSource_Object = MibScalar
zxAnSysLastClockSource = _ZxAnSysLastClockSource_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 104, 7),
    _ZxAnSysLastClockSource_Type()
)
zxAnSysLastClockSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSysLastClockSource.setStatus("current")
_ZxAnSysLastClockSourceE1_Type = DisplayString
_ZxAnSysLastClockSourceE1_Object = MibScalar
zxAnSysLastClockSourceE1 = _ZxAnSysLastClockSourceE1_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 104, 8),
    _ZxAnSysLastClockSourceE1_Type()
)
zxAnSysLastClockSourceE1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSysLastClockSourceE1.setStatus("current")


class _ZxAnSysClockSourceTrapEnable_Type(Bits):
    """Custom type zxAnSysClockSourceTrapEnable based on Bits"""
    namedValues = NamedValues(
        *(("bitse1", 0),
          ("bits2m", 1),
          ("est2m", 2),
          ("ttl2m", 3),
          ("e12ml", 4),
          ("e12mr", 5),
          ("default", 6))
    )

_ZxAnSysClockSourceTrapEnable_Type.__name__ = "Bits"
_ZxAnSysClockSourceTrapEnable_Object = MibScalar
zxAnSysClockSourceTrapEnable = _ZxAnSysClockSourceTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 104, 9),
    _ZxAnSysClockSourceTrapEnable_Type()
)
zxAnSysClockSourceTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnSysClockSourceTrapEnable.setStatus("current")


class _ZxAnSysClockSourceIfType_Type(Integer32):
    """Custom type zxAnSysClockSourceIfType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("e1", 1),
          ("t1", 2))
    )


_ZxAnSysClockSourceIfType_Type.__name__ = "Integer32"
_ZxAnSysClockSourceIfType_Object = MibScalar
zxAnSysClockSourceIfType = _ZxAnSysClockSourceIfType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 104, 10),
    _ZxAnSysClockSourceIfType_Type()
)
zxAnSysClockSourceIfType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnSysClockSourceIfType.setStatus("current")
_ZxAnSysDsx1ClockSourceTable_Object = MibTable
zxAnSysDsx1ClockSourceTable = _ZxAnSysDsx1ClockSourceTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 104, 100)
)
if mibBuilder.loadTexts:
    zxAnSysDsx1ClockSourceTable.setStatus("current")
_ZxAnSysDsx1ClockSourceEntry_Object = MibTableRow
zxAnSysDsx1ClockSourceEntry = _ZxAnSysDsx1ClockSourceEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 104, 100, 1)
)
zxAnSysDsx1ClockSourceEntry.setIndexNames(
    (0, "ZTE-AN-SYS-MIB", "zxAnSysDsx1ClkSrcRack"),
    (0, "ZTE-AN-SYS-MIB", "zxAnSysDsx1ClkSrcShelf"),
    (0, "ZTE-AN-SYS-MIB", "zxAnSysDsx1ClkSrcSlot"),
    (0, "ZTE-AN-SYS-MIB", "zxAnSysDsx1ClkSrcLinkNo"),
)
if mibBuilder.loadTexts:
    zxAnSysDsx1ClockSourceEntry.setStatus("current")
_ZxAnSysDsx1ClkSrcRack_Type = Integer32
_ZxAnSysDsx1ClkSrcRack_Object = MibTableColumn
zxAnSysDsx1ClkSrcRack = _ZxAnSysDsx1ClkSrcRack_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 104, 100, 1, 1),
    _ZxAnSysDsx1ClkSrcRack_Type()
)
zxAnSysDsx1ClkSrcRack.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnSysDsx1ClkSrcRack.setStatus("current")
_ZxAnSysDsx1ClkSrcShelf_Type = Integer32
_ZxAnSysDsx1ClkSrcShelf_Object = MibTableColumn
zxAnSysDsx1ClkSrcShelf = _ZxAnSysDsx1ClkSrcShelf_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 104, 100, 1, 2),
    _ZxAnSysDsx1ClkSrcShelf_Type()
)
zxAnSysDsx1ClkSrcShelf.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnSysDsx1ClkSrcShelf.setStatus("current")
_ZxAnSysDsx1ClkSrcSlot_Type = Integer32
_ZxAnSysDsx1ClkSrcSlot_Object = MibTableColumn
zxAnSysDsx1ClkSrcSlot = _ZxAnSysDsx1ClkSrcSlot_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 104, 100, 1, 3),
    _ZxAnSysDsx1ClkSrcSlot_Type()
)
zxAnSysDsx1ClkSrcSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnSysDsx1ClkSrcSlot.setStatus("current")
_ZxAnSysDsx1ClkSrcLinkNo_Type = Integer32
_ZxAnSysDsx1ClkSrcLinkNo_Object = MibTableColumn
zxAnSysDsx1ClkSrcLinkNo = _ZxAnSysDsx1ClkSrcLinkNo_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 104, 100, 1, 4),
    _ZxAnSysDsx1ClkSrcLinkNo_Type()
)
zxAnSysDsx1ClkSrcLinkNo.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnSysDsx1ClkSrcLinkNo.setStatus("current")


class _ZxAnSysDsx1ClkSrcAvailableStatus_Type(Integer32):
    """Custom type zxAnSysDsx1ClkSrcAvailableStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("available", 1),
          ("unavailable", 2))
    )


_ZxAnSysDsx1ClkSrcAvailableStatus_Type.__name__ = "Integer32"
_ZxAnSysDsx1ClkSrcAvailableStatus_Object = MibTableColumn
zxAnSysDsx1ClkSrcAvailableStatus = _ZxAnSysDsx1ClkSrcAvailableStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 104, 100, 1, 5),
    _ZxAnSysDsx1ClkSrcAvailableStatus_Type()
)
zxAnSysDsx1ClkSrcAvailableStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSysDsx1ClkSrcAvailableStatus.setStatus("current")


class _ZxAnSysDsx1ClkSrcCurrUsingStatus_Type(Integer32):
    """Custom type zxAnSysDsx1ClkSrcCurrUsingStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inUse", 1),
          ("unused", 2))
    )


_ZxAnSysDsx1ClkSrcCurrUsingStatus_Type.__name__ = "Integer32"
_ZxAnSysDsx1ClkSrcCurrUsingStatus_Object = MibTableColumn
zxAnSysDsx1ClkSrcCurrUsingStatus = _ZxAnSysDsx1ClkSrcCurrUsingStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 104, 100, 1, 6),
    _ZxAnSysDsx1ClkSrcCurrUsingStatus_Type()
)
zxAnSysDsx1ClkSrcCurrUsingStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSysDsx1ClkSrcCurrUsingStatus.setStatus("current")


class _ZxAnSysDsx1ClkSrcPriority_Type(Integer32):
    """Custom type zxAnSysDsx1ClkSrcPriority based on Integer32"""
    defaultValue = 255


_ZxAnSysDsx1ClkSrcPriority_Type.__name__ = "Integer32"
_ZxAnSysDsx1ClkSrcPriority_Object = MibTableColumn
zxAnSysDsx1ClkSrcPriority = _ZxAnSysDsx1ClkSrcPriority_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 104, 100, 1, 7),
    _ZxAnSysDsx1ClkSrcPriority_Type()
)
zxAnSysDsx1ClkSrcPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnSysDsx1ClkSrcPriority.setStatus("current")
_ZxAnSysIpv6GlobalMgmt_ObjectIdentity = ObjectIdentity
zxAnSysIpv6GlobalMgmt = _ZxAnSysIpv6GlobalMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 105)
)


class _ZxAnSysIpv6GlobalEnable_Type(Integer32):
    """Custom type zxAnSysIpv6GlobalEnable based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_ZxAnSysIpv6GlobalEnable_Type.__name__ = "Integer32"
_ZxAnSysIpv6GlobalEnable_Object = MibScalar
zxAnSysIpv6GlobalEnable = _ZxAnSysIpv6GlobalEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 105, 1),
    _ZxAnSysIpv6GlobalEnable_Type()
)
zxAnSysIpv6GlobalEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnSysIpv6GlobalEnable.setStatus("current")
_ZxAnSysDns_ObjectIdentity = ObjectIdentity
zxAnSysDns = _ZxAnSysDns_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 106)
)
_ZxAnSysDnsServerTable_Object = MibTable
zxAnSysDnsServerTable = _ZxAnSysDnsServerTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 106, 1)
)
if mibBuilder.loadTexts:
    zxAnSysDnsServerTable.setStatus("current")
_ZxAnSysDnsServerEntry_Object = MibTableRow
zxAnSysDnsServerEntry = _ZxAnSysDnsServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 106, 1, 1)
)
zxAnSysDnsServerEntry.setIndexNames(
    (0, "ZTE-AN-SYS-MIB", "zxAnSysDnsServerIpAddressType"),
    (0, "ZTE-AN-SYS-MIB", "zxAnSysDnsServerIpAddress"),
)
if mibBuilder.loadTexts:
    zxAnSysDnsServerEntry.setStatus("current")
_ZxAnSysDnsServerIpAddressType_Type = InetAddressType
_ZxAnSysDnsServerIpAddressType_Object = MibTableColumn
zxAnSysDnsServerIpAddressType = _ZxAnSysDnsServerIpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 106, 1, 1, 1),
    _ZxAnSysDnsServerIpAddressType_Type()
)
zxAnSysDnsServerIpAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnSysDnsServerIpAddressType.setStatus("current")
_ZxAnSysDnsServerIpAddress_Type = InetAddress
_ZxAnSysDnsServerIpAddress_Object = MibTableColumn
zxAnSysDnsServerIpAddress = _ZxAnSysDnsServerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 106, 1, 1, 2),
    _ZxAnSysDnsServerIpAddress_Type()
)
zxAnSysDnsServerIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnSysDnsServerIpAddress.setStatus("current")


class _ZxAnSysDnsServerType_Type(Integer32):
    """Custom type zxAnSysDnsServerType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("primary", 1),
          ("secondary", 2))
    )


_ZxAnSysDnsServerType_Type.__name__ = "Integer32"
_ZxAnSysDnsServerType_Object = MibTableColumn
zxAnSysDnsServerType = _ZxAnSysDnsServerType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 106, 1, 1, 3),
    _ZxAnSysDnsServerType_Type()
)
zxAnSysDnsServerType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnSysDnsServerType.setStatus("current")
_ZxAnSysDnsServerRowStatus_Type = RowStatus
_ZxAnSysDnsServerRowStatus_Object = MibTableColumn
zxAnSysDnsServerRowStatus = _ZxAnSysDnsServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 106, 1, 1, 10),
    _ZxAnSysDnsServerRowStatus_Type()
)
zxAnSysDnsServerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnSysDnsServerRowStatus.setStatus("current")
_ZxAnSysDnsGlobalObjects_ObjectIdentity = ObjectIdentity
zxAnSysDnsGlobalObjects = _ZxAnSysDnsGlobalObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 106, 50)
)


class _ZxAnSysDnsRequestMode_Type(Integer32):
    """Custom type zxAnSysDnsRequestMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ttl", 1),
          ("requestOnceWhenPowerOn", 2))
    )


_ZxAnSysDnsRequestMode_Type.__name__ = "Integer32"
_ZxAnSysDnsRequestMode_Object = MibScalar
zxAnSysDnsRequestMode = _ZxAnSysDnsRequestMode_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 106, 50, 1),
    _ZxAnSysDnsRequestMode_Type()
)
zxAnSysDnsRequestMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnSysDnsRequestMode.setStatus("current")
_ZxAnSysOutbandPortMgmt_ObjectIdentity = ObjectIdentity
zxAnSysOutbandPortMgmt = _ZxAnSysOutbandPortMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 107)
)


class _ZxAnSysOutbandPortAdminStatus_Type(Integer32):
    """Custom type zxAnSysOutbandPortAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_ZxAnSysOutbandPortAdminStatus_Type.__name__ = "Integer32"
_ZxAnSysOutbandPortAdminStatus_Object = MibScalar
zxAnSysOutbandPortAdminStatus = _ZxAnSysOutbandPortAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 107, 1),
    _ZxAnSysOutbandPortAdminStatus_Type()
)
zxAnSysOutbandPortAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnSysOutbandPortAdminStatus.setStatus("current")


class _ZxAnSysOutbandPortOperStatus_Type(Integer32):
    """Custom type zxAnSysOutbandPortOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_ZxAnSysOutbandPortOperStatus_Type.__name__ = "Integer32"
_ZxAnSysOutbandPortOperStatus_Object = MibScalar
zxAnSysOutbandPortOperStatus = _ZxAnSysOutbandPortOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 107, 2),
    _ZxAnSysOutbandPortOperStatus_Type()
)
zxAnSysOutbandPortOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSysOutbandPortOperStatus.setStatus("current")


class _ZxAnSysOutbandPortDuplexSpeed_Type(Integer32):
    """Custom type zxAnSysOutbandPortDuplexSpeed based on Integer32"""
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
              99)
        )
    )
    namedValues = NamedValues(
        *(("autoNegotiate", 1),
          ("half10", 2),
          ("full10", 3),
          ("half100", 4),
          ("full100", 5),
          ("full1000", 6),
          ("full10000", 7),
          ("illegal", 99))
    )


_ZxAnSysOutbandPortDuplexSpeed_Type.__name__ = "Integer32"
_ZxAnSysOutbandPortDuplexSpeed_Object = MibScalar
zxAnSysOutbandPortDuplexSpeed = _ZxAnSysOutbandPortDuplexSpeed_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 107, 3),
    _ZxAnSysOutbandPortDuplexSpeed_Type()
)
zxAnSysOutbandPortDuplexSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnSysOutbandPortDuplexSpeed.setStatus("current")


class _ZxAnSysOutbandPortActualDuplex_Type(Integer32):
    """Custom type zxAnSysOutbandPortActualDuplex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("autoNegotiate", 1),
          ("half", 2),
          ("full", 3))
    )


_ZxAnSysOutbandPortActualDuplex_Type.__name__ = "Integer32"
_ZxAnSysOutbandPortActualDuplex_Object = MibScalar
zxAnSysOutbandPortActualDuplex = _ZxAnSysOutbandPortActualDuplex_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 107, 4),
    _ZxAnSysOutbandPortActualDuplex_Type()
)
zxAnSysOutbandPortActualDuplex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSysOutbandPortActualDuplex.setStatus("current")


class _ZxAnSysOutbandPortActualSpeed_Type(Integer32):
    """Custom type zxAnSysOutbandPortActualSpeed based on Integer32"""
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
        *(("speed10", 1),
          ("speed100", 2),
          ("speed1000", 3),
          ("speed10000", 4),
          ("autoSpeed", 5))
    )


_ZxAnSysOutbandPortActualSpeed_Type.__name__ = "Integer32"
_ZxAnSysOutbandPortActualSpeed_Object = MibScalar
zxAnSysOutbandPortActualSpeed = _ZxAnSysOutbandPortActualSpeed_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 107, 5),
    _ZxAnSysOutbandPortActualSpeed_Type()
)
zxAnSysOutbandPortActualSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSysOutbandPortActualSpeed.setStatus("current")


class _ZxAnSysOutbandPortTagMode_Type(Integer32):
    """Custom type zxAnSysOutbandPortTagMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("untagged", 1),
          ("tagged", 2))
    )


_ZxAnSysOutbandPortTagMode_Type.__name__ = "Integer32"
_ZxAnSysOutbandPortTagMode_Object = MibScalar
zxAnSysOutbandPortTagMode = _ZxAnSysOutbandPortTagMode_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 107, 6),
    _ZxAnSysOutbandPortTagMode_Type()
)
zxAnSysOutbandPortTagMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnSysOutbandPortTagMode.setStatus("current")


class _ZxAnSysOutbandPortVlanId_Type(Integer32):
    """Custom type zxAnSysOutbandPortVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_ZxAnSysOutbandPortVlanId_Type.__name__ = "Integer32"
_ZxAnSysOutbandPortVlanId_Object = MibScalar
zxAnSysOutbandPortVlanId = _ZxAnSysOutbandPortVlanId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 107, 7),
    _ZxAnSysOutbandPortVlanId_Type()
)
zxAnSysOutbandPortVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnSysOutbandPortVlanId.setStatus("current")


class _ZxAnSysOutbandPortCos_Type(Integer32):
    """Custom type zxAnSysOutbandPortCos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
        ValueRangeConstraint(255, 255),
    )


_ZxAnSysOutbandPortCos_Type.__name__ = "Integer32"
_ZxAnSysOutbandPortCos_Object = MibScalar
zxAnSysOutbandPortCos = _ZxAnSysOutbandPortCos_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 107, 8),
    _ZxAnSysOutbandPortCos_Type()
)
zxAnSysOutbandPortCos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnSysOutbandPortCos.setStatus("current")
_ZxAnSysSnmpMgmt_ObjectIdentity = ObjectIdentity
zxAnSysSnmpMgmt = _ZxAnSysSnmpMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 108)
)


class _ZxAnSnmpEngineIdGenerateMode_Type(Integer32):
    """Custom type zxAnSnmpEngineIdGenerateMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mac", 1),
          ("sysName", 2))
    )


_ZxAnSnmpEngineIdGenerateMode_Type.__name__ = "Integer32"
_ZxAnSnmpEngineIdGenerateMode_Object = MibScalar
zxAnSnmpEngineIdGenerateMode = _ZxAnSnmpEngineIdGenerateMode_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 108, 1),
    _ZxAnSnmpEngineIdGenerateMode_Type()
)
zxAnSnmpEngineIdGenerateMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnSnmpEngineIdGenerateMode.setStatus("current")


class _ZxAnSnmpSupportedVersion_Type(Integer32):
    """Custom type zxAnSnmpSupportedVersion based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("all", 1),
          ("onlySnmpV3", 2))
    )


_ZxAnSnmpSupportedVersion_Type.__name__ = "Integer32"
_ZxAnSnmpSupportedVersion_Object = MibScalar
zxAnSnmpSupportedVersion = _ZxAnSnmpSupportedVersion_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 108, 2),
    _ZxAnSnmpSupportedVersion_Type()
)
zxAnSnmpSupportedVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnSnmpSupportedVersion.setStatus("current")
_ZxAnSysProfileOperMgmt_ObjectIdentity = ObjectIdentity
zxAnSysProfileOperMgmt = _ZxAnSysProfileOperMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 109)
)
_ZxAnSysProfileOperGlobalObjects_ObjectIdentity = ObjectIdentity
zxAnSysProfileOperGlobalObjects = _ZxAnSysProfileOperGlobalObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 109, 1)
)


class _ZxAnSysProfileCategory_Type(DisplayString):
    """Custom type zxAnSysProfileCategory based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ZxAnSysProfileCategory_Type.__name__ = "DisplayString"
_ZxAnSysProfileCategory_Object = MibScalar
zxAnSysProfileCategory = _ZxAnSysProfileCategory_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 109, 1, 1),
    _ZxAnSysProfileCategory_Type()
)
zxAnSysProfileCategory.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    zxAnSysProfileCategory.setStatus("current")


class _ZxAnSysProfileName_Type(DisplayString):
    """Custom type zxAnSysProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ZxAnSysProfileName_Type.__name__ = "DisplayString"
_ZxAnSysProfileName_Object = MibScalar
zxAnSysProfileName = _ZxAnSysProfileName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 109, 1, 2),
    _ZxAnSysProfileName_Type()
)
zxAnSysProfileName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    zxAnSysProfileName.setStatus("current")
_ZxAnSysProfileId_Type = Integer32
_ZxAnSysProfileId_Object = MibScalar
zxAnSysProfileId = _ZxAnSysProfileId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 109, 1, 3),
    _ZxAnSysProfileId_Type()
)
zxAnSysProfileId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    zxAnSysProfileId.setStatus("current")


class _ZxAnSysProfileInfo_Type(DisplayString):
    """Custom type zxAnSysProfileInfo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_ZxAnSysProfileInfo_Type.__name__ = "DisplayString"
_ZxAnSysProfileInfo_Object = MibScalar
zxAnSysProfileInfo = _ZxAnSysProfileInfo_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 109, 1, 4),
    _ZxAnSysProfileInfo_Type()
)
zxAnSysProfileInfo.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    zxAnSysProfileInfo.setStatus("current")
_ZxAnSysMgmtArp_ObjectIdentity = ObjectIdentity
zxAnSysMgmtArp = _ZxAnSysMgmtArp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 110)
)
_ZxAnSysMgmtArpGlobalObjects_ObjectIdentity = ObjectIdentity
zxAnSysMgmtArpGlobalObjects = _ZxAnSysMgmtArpGlobalObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 110, 1)
)


class _ZxAnSysMgmtArpAgingTime_Type(Integer32):
    """Custom type zxAnSysMgmtArpAgingTime based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_ZxAnSysMgmtArpAgingTime_Type.__name__ = "Integer32"
_ZxAnSysMgmtArpAgingTime_Object = MibScalar
zxAnSysMgmtArpAgingTime = _ZxAnSysMgmtArpAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 1, 110, 1, 1),
    _ZxAnSysMgmtArpAgingTime_Type()
)
zxAnSysMgmtArpAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnSysMgmtArpAgingTime.setStatus("current")
if mibBuilder.loadTexts:
    zxAnSysMgmtArpAgingTime.setUnits("minutes")
_ZxAnSysTrapObjects_ObjectIdentity = ObjectIdentity
zxAnSysTrapObjects = _ZxAnSysTrapObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 2)
)
_ZxAnSysNtpTrapGroup_ObjectIdentity = ObjectIdentity
zxAnSysNtpTrapGroup = _ZxAnSysNtpTrapGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 2, 5)
)
_ZxAnSysSecurityTrapGroup_ObjectIdentity = ObjectIdentity
zxAnSysSecurityTrapGroup = _ZxAnSysSecurityTrapGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 2, 6)
)
_ZxAnSysSummerTimeTrapGroup_ObjectIdentity = ObjectIdentity
zxAnSysSummerTimeTrapGroup = _ZxAnSysSummerTimeTrapGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 2, 7)
)
_ZxAnSysClockTrapGroup_ObjectIdentity = ObjectIdentity
zxAnSysClockTrapGroup = _ZxAnSysClockTrapGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 2, 8)
)
_ZxAnSysProfileOperTrapGroup_ObjectIdentity = ObjectIdentity
zxAnSysProfileOperTrapGroup = _ZxAnSysProfileOperTrapGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 2, 9)
)
_ZxAnSysResourceTrapGroup_ObjectIdentity = ObjectIdentity
zxAnSysResourceTrapGroup = _ZxAnSysResourceTrapGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 2, 10)
)

# Managed Objects groups


# Notification objects

zxAnSysNtpOffsetOverThreshTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 2, 5, 1)
)
zxAnSysNtpOffsetOverThreshTrap.setObjects(
      *(("ZTE-AN-SYS-MIB", "zxAnSysNtpCurrentOffset"),
        ("ZTE-AN-SYS-MIB", "zxAnSysNtpOffsetAlarmThreshold"))
)
if mibBuilder.loadTexts:
    zxAnSysNtpOffsetOverThreshTrap.setStatus(
        "current"
    )

zxAnSysNtpOffsetUnderThreshTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 2, 5, 2)
)
zxAnSysNtpOffsetUnderThreshTrap.setObjects(
      *(("ZTE-AN-SYS-MIB", "zxAnSysNtpCurrentOffset"),
        ("ZTE-AN-SYS-MIB", "zxAnSysNtpOffsetAlarmThreshold"))
)
if mibBuilder.loadTexts:
    zxAnSysNtpOffsetUnderThreshTrap.setStatus(
        "current"
    )

zxAnSysSecCrftTerminLogonTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 2, 6, 1)
)
zxAnSysSecCrftTerminLogonTrap.setObjects(
      *(("ZTE-AN-SYS-MIB", "zxAnCliCrftTerminalLastLoginType"),
        ("ZTE-AN-SYS-MIB", "zxAnCliActiveUserName"),
        ("ZTE-AN-SYS-MIB", "zxAnCliActiveUserLocation"))
)
if mibBuilder.loadTexts:
    zxAnSysSecCrftTerminLogonTrap.setStatus(
        "current"
    )

zxAnSysSecCrftTerminLogoutTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 2, 6, 2)
)
zxAnSysSecCrftTerminLogoutTrap.setObjects(
      *(("ZTE-AN-SYS-MIB", "zxAnCliCrftTerminalLastLoginType"),
        ("ZTE-AN-SYS-MIB", "zxAnCliActiveUserName"),
        ("ZTE-AN-SYS-MIB", "zxAnCliActiveUserLocation"))
)
if mibBuilder.loadTexts:
    zxAnSysSecCrftTerminLogoutTrap.setStatus(
        "current"
    )

zxAnSysSecCrftTerminLoginFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 2, 6, 3)
)
zxAnSysSecCrftTerminLoginFailed.setObjects(
      *(("ZTE-AN-SYS-MIB", "zxAnCliCrftTerminalLastLoginType"),
        ("ZTE-AN-SYS-MIB", "zxAnCliTryToLoginUserName"),
        ("ZTE-AN-SYS-MIB", "zxAnCliTryToLoginUserLocation"))
)
if mibBuilder.loadTexts:
    zxAnSysSecCrftTerminLoginFailed.setStatus(
        "current"
    )

zxAnSysSummerTimeStartTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 2, 7, 1)
)
zxAnSysSummerTimeStartTrap.setObjects(
      *(("ZTE-AN-SYS-MIB", "zxAnRtcSummerTimeName"),
        ("ZTE-AN-SYS-MIB", "zxAnRtcSummerTimeOffset"),
        ("ZTE-AN-SYS-MIB", "zxAnRtcSummerTimeStart"),
        ("ZTE-AN-SYS-MIB", "zxAnRtcSummerTimeEnd"))
)
if mibBuilder.loadTexts:
    zxAnSysSummerTimeStartTrap.setStatus(
        "current"
    )

zxAnSysSummerTimeEndTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 2, 7, 2)
)
zxAnSysSummerTimeEndTrap.setObjects(
      *(("ZTE-AN-SYS-MIB", "zxAnRtcSummerTimeName"),
        ("ZTE-AN-SYS-MIB", "zxAnRtcSummerTimeOffset"),
        ("ZTE-AN-SYS-MIB", "zxAnRtcSummerTimeStart"),
        ("ZTE-AN-SYS-MIB", "zxAnRtcSummerTimeEnd"))
)
if mibBuilder.loadTexts:
    zxAnSysSummerTimeEndTrap.setStatus(
        "current"
    )

zxAnSysClockSourceSwitchTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 2, 8, 1)
)
zxAnSysClockSourceSwitchTrap.setObjects(
      *(("ZTE-AN-SYS-MIB", "zxAnSysActualClockSource"),
        ("ZTE-AN-SYS-MIB", "zxAnSysLastClockSource"),
        ("ZTE-AN-SYS-MIB", "zxAnSysActualClockSourceE1"),
        ("ZTE-AN-SYS-MIB", "zxAnSysLastClockSourceE1"))
)
if mibBuilder.loadTexts:
    zxAnSysClockSourceSwitchTrap.setStatus(
        "current"
    )

zxAnSysClkSrcUnavailableTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 2, 8, 2)
)
zxAnSysClkSrcUnavailableTrap.setObjects(
    ("ZTE-AN-SYS-MIB", "zxAnSysLastClockSource")
)
if mibBuilder.loadTexts:
    zxAnSysClkSrcUnavailableTrap.setStatus(
        "current"
    )

zxAnSysClkSrcAvailableTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 2, 8, 3)
)
zxAnSysClkSrcAvailableTrap.setObjects(
    ("ZTE-AN-SYS-MIB", "zxAnSysLastClockSource")
)
if mibBuilder.loadTexts:
    zxAnSysClkSrcAvailableTrap.setStatus(
        "current"
    )

zxAnSysDelAppliedPrfFailedNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 2, 9, 1)
)
zxAnSysDelAppliedPrfFailedNotify.setObjects(
      *(("ZTE-AN-SYS-MIB", "zxAnSysProfileCategory"),
        ("ZTE-AN-SYS-MIB", "zxAnSysProfileName"),
        ("ZTE-AN-SYS-MIB", "zxAnSysProfileId"),
        ("ZTE-AN-SYS-MIB", "zxAnSysProfileInfo"))
)
if mibBuilder.loadTexts:
    zxAnSysDelAppliedPrfFailedNotify.setStatus(
        "current"
    )

zxAnSysResourceInsufficientTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1, 2, 10, 1)
)
zxAnSysResourceInsufficientTrap.setObjects(
    ("ZTE-AN-SYS-MIB", "zxAnSysResourceType")
)
if mibBuilder.loadTexts:
    zxAnSysResourceInsufficientTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZTE-AN-SYS-MIB",
    **{"zxAnSysMib": zxAnSysMib,
       "zxAnSysObjects": zxAnSysObjects,
       "zxAnSnmpSetCmdErrCode": zxAnSnmpSetCmdErrCode,
       "zxAnSysSecMgmt": zxAnSysSecMgmt,
       "zxAnCliCrftTerminalEnable": zxAnCliCrftTerminalEnable,
       "zxAnCliSecurityLevel": zxAnCliSecurityLevel,
       "zxAnCliCrftTerminalLoginStatus": zxAnCliCrftTerminalLoginStatus,
       "zxAnCliCrftTerminalLastLoginType": zxAnCliCrftTerminalLastLoginType,
       "zxAnCliPromptName": zxAnCliPromptName,
       "zxAnCliSuperUserName": zxAnCliSuperUserName,
       "zxAnCliSuperUserPwd": zxAnCliSuperUserPwd,
       "zxAnCliTelnetEnable": zxAnCliTelnetEnable,
       "zxAnCliUserSuspendMode": zxAnCliUserSuspendMode,
       "zxAnCliUserSuspendDuration": zxAnCliUserSuspendDuration,
       "zxAnCliUserPasswordRetries": zxAnCliUserPasswordRetries,
       "zxAnCliTryToLoginUserName": zxAnCliTryToLoginUserName,
       "zxAnCliTryToLoginUserLocation": zxAnCliTryToLoginUserLocation,
       "zxAnCliMultiSessionsInformEnable": zxAnCliMultiSessionsInformEnable,
       "zxAnSysSshObjects": zxAnSysSshObjects,
       "zxAnSysSshGlobalObjects": zxAnSysSshGlobalObjects,
       "zxAnSysSshEnable": zxAnSysSshEnable,
       "zxAnSysSshVersion": zxAnSysSshVersion,
       "zxAnSysSshOnlyEnable": zxAnSysSshOnlyEnable,
       "zxAnSysSshGenerateKeyEnable": zxAnSysSshGenerateKeyEnable,
       "zxAnSysSshAuthType": zxAnSysSshAuthType,
       "zxAnSysWriteLockObjects": zxAnSysWriteLockObjects,
       "zxAnSysWriteLockOwner": zxAnSysWriteLockOwner,
       "zxAnSysWriteLockAction": zxAnSysWriteLockAction,
       "zxAnSysCliUserTable": zxAnSysCliUserTable,
       "zxAnSysCliUserEntry": zxAnSysCliUserEntry,
       "zxAnCliUserConfIndex": zxAnCliUserConfIndex,
       "zxAnCliUserConfName": zxAnCliUserConfName,
       "zxAnCliUserConfPwd": zxAnCliUserConfPwd,
       "zxAnCliUserConfAccessLevel": zxAnCliUserConfAccessLevel,
       "zxAnCliUserConfRowStatus": zxAnCliUserConfRowStatus,
       "zxAnCliUserConfPwdEncryptEnable": zxAnCliUserConfPwdEncryptEnable,
       "zxAnCliUserConfMaxSessions": zxAnCliUserConfMaxSessions,
       "zxAnCliUserConfAdminStatus": zxAnCliUserConfAdminStatus,
       "zxAnCliUserConfOperStatus": zxAnCliUserConfOperStatus,
       "zxAnSysMgmtAclTable": zxAnSysMgmtAclTable,
       "zxAnSysMgmtAclEntry": zxAnSysMgmtAclEntry,
       "zxAnSysMgmtAclIndex": zxAnSysMgmtAclIndex,
       "zxAnSysMgmtAclAlias": zxAnSysMgmtAclAlias,
       "zxAnSysMgmtAclRowStatus": zxAnSysMgmtAclRowStatus,
       "zxAnSysMgmtAclRuleTable": zxAnSysMgmtAclRuleTable,
       "zxAnSysMgmtAclRuleEntry": zxAnSysMgmtAclRuleEntry,
       "zxAnSysMgmtAclRuleID": zxAnSysMgmtAclRuleID,
       "zxAnSysMgmtAclRuleAccessCtrl": zxAnSysMgmtAclRuleAccessCtrl,
       "zxAnSysMgmtAclRuleSrcAddrType": zxAnSysMgmtAclRuleSrcAddrType,
       "zxAnSysMgmtAclRuleSrcAddr": zxAnSysMgmtAclRuleSrcAddr,
       "zxAnSysMngAclRuleSrcAddrWildcard": zxAnSysMngAclRuleSrcAddrWildcard,
       "zxAnSysMgmtAclRuleRowStatus": zxAnSysMgmtAclRuleRowStatus,
       "zxAnSysMgmtAclBindTable": zxAnSysMgmtAclBindTable,
       "zxAnSysMgmtAclBindEntry": zxAnSysMgmtAclBindEntry,
       "zxAnSysMgmtAclProtocol": zxAnSysMgmtAclProtocol,
       "zxAnSysMgmtAclBindIndex": zxAnSysMgmtAclBindIndex,
       "zxAnSysCliActiveUsersTable": zxAnSysCliActiveUsersTable,
       "zxAnSysCliActiveUsersEntry": zxAnSysCliActiveUsersEntry,
       "zxAnCliActiveUserIndex": zxAnCliActiveUserIndex,
       "zxAnCliActiveUserType": zxAnCliActiveUserType,
       "zxAnCliActiveUserName": zxAnCliActiveUserName,
       "zxAnCliActiveUserPriority": zxAnCliActiveUserPriority,
       "zxAnCliActiveUserHost": zxAnCliActiveUserHost,
       "zxAnCliActiveUserIdleTime": zxAnCliActiveUserIdleTime,
       "zxAnCliActiveUserLocation": zxAnCliActiveUserLocation,
       "zxAnSysCliActiveUserRowStatus": zxAnSysCliActiveUserRowStatus,
       "zxAnSysCommunityConfTable": zxAnSysCommunityConfTable,
       "zxAnSysCommunityConfEntry": zxAnSysCommunityConfEntry,
       "zxAnSysCommunityConfCommunity": zxAnSysCommunityConfCommunity,
       "zxAnSysCommunityConfPermission": zxAnSysCommunityConfPermission,
       "zxAnSysCommunityConfViewName": zxAnSysCommunityConfViewName,
       "zxAnSysCommunityConfRowStatus": zxAnSysCommunityConfRowStatus,
       "zxAnSysDataMgmt": zxAnSysDataMgmt,
       "zxAnSysConfigSavingAction": zxAnSysConfigSavingAction,
       "zxAnSysConfigSaveStatus": zxAnSysConfigSaveStatus,
       "zxAnSysAutoSaveFlashMode": zxAnSysAutoSaveFlashMode,
       "zxAnSysDailyAutoSaveFlashTime": zxAnSysDailyAutoSaveFlashTime,
       "zxAnSysAutoSaveFlashStartDate": zxAnSysAutoSaveFlashStartDate,
       "zxAnSysAutoSaveFlashInterval": zxAnSysAutoSaveFlashInterval,
       "zxAnSysConfigSaveProgress": zxAnSysConfigSaveProgress,
       "zxAnSysDataSaveFlashFailReason": zxAnSysDataSaveFlashFailReason,
       "zxAnSysCfgChangeSaveFlashEnable": zxAnSysCfgChangeSaveFlashEnable,
       "zxAnSysCfgChangeSaveHoldOffTime": zxAnSysCfgChangeSaveHoldOffTime,
       "zxAnSysRunningCtrl": zxAnSysRunningCtrl,
       "zxAnChassisSysReboot": zxAnChassisSysReboot,
       "zxAnSysRevision": zxAnSysRevision,
       "zxAnFileLoadDefaultConfiguration": zxAnFileLoadDefaultConfiguration,
       "zxAnSysLastRebootReason": zxAnSysLastRebootReason,
       "zxAnSysResourceType": zxAnSysResourceType,
       "zxAnSysNmsMgmt": zxAnSysNmsMgmt,
       "zxAnSysNmsMgmtPath": zxAnSysNmsMgmtPath,
       "zxAnSysNmsMgmtOutbandIpAddr": zxAnSysNmsMgmtOutbandIpAddr,
       "zxAnSysNmsMgmtOutbandIpMask": zxAnSysNmsMgmtOutbandIpMask,
       "zxAnSysNmsMgmtOutbandMac": zxAnSysNmsMgmtOutbandMac,
       "zxAnSysNmsMgmtInbandIpAddr": zxAnSysNmsMgmtInbandIpAddr,
       "zxAnSysNmsMgmtInbandIpMask": zxAnSysNmsMgmtInbandIpMask,
       "zxAnSysNmsMgmtInbandMac": zxAnSysNmsMgmtInbandMac,
       "zxAnSysNmsMgmtInbandVlan": zxAnSysNmsMgmtInbandVlan,
       "zxAnSysNmsMgmtInbandVpnId": zxAnSysNmsMgmtInbandVpnId,
       "zxAnSysMgmtOutbandIpv6Addr": zxAnSysMgmtOutbandIpv6Addr,
       "zxAnSysMgmtOutbandIpv6AddrPfxLen": zxAnSysMgmtOutbandIpv6AddrPfxLen,
       "zxAnSysNmsMgmtInbandEnable": zxAnSysNmsMgmtInbandEnable,
       "zxAnSysServiceMgmtPath": zxAnSysServiceMgmtPath,
       "zxAnSysServiceMgmtIpTable": zxAnSysServiceMgmtIpTable,
       "zxAnSysServiceMgmtIpEntry": zxAnSysServiceMgmtIpEntry,
       "zxAnSysServiceMgmtVlanId": zxAnSysServiceMgmtVlanId,
       "zxAnSysServiceMgmtVpnId": zxAnSysServiceMgmtVpnId,
       "zxAnSysServiceMgmtIpAddr": zxAnSysServiceMgmtIpAddr,
       "zxAnSysServiceMgmtIpMask": zxAnSysServiceMgmtIpMask,
       "zxAnSysServiceMgmtMac": zxAnSysServiceMgmtMac,
       "zxAnSysServiceMgmtIpRowStatus": zxAnSysServiceMgmtIpRowStatus,
       "zxAnSysTimeMgmt": zxAnSysTimeMgmt,
       "zxAnRtcSysDateTime": zxAnRtcSysDateTime,
       "zxAnRtcZoneType": zxAnRtcZoneType,
       "zxAnRtcZoneHours": zxAnRtcZoneHours,
       "zxAnSysNtpMgmt": zxAnSysNtpMgmt,
       "zxAnSysNtpEnable": zxAnSysNtpEnable,
       "zxAnSysNtpServerAddr": zxAnSysNtpServerAddr,
       "zxAnSysNtpClientAddr": zxAnSysNtpClientAddr,
       "zxAnSysNtpProtoVersion": zxAnSysNtpProtoVersion,
       "zxAnSysNtpPollInterval": zxAnSysNtpPollInterval,
       "zxAnSysNtpStatusCurrentState": zxAnSysNtpStatusCurrentState,
       "zxAnSysNtpStratum": zxAnSysNtpStratum,
       "zxAnSysNtpCurrentOffset": zxAnSysNtpCurrentOffset,
       "zxAnSysNtpOffsetAlarmThreshold": zxAnSysNtpOffsetAlarmThreshold,
       "zxAnSysNtpMode": zxAnSysNtpMode,
       "zxAnSysNtpCurrServerIpAddrType": zxAnSysNtpCurrServerIpAddrType,
       "zxAnSysNtpCurrServerIpAddress": zxAnSysNtpCurrServerIpAddress,
       "zxAnSysNtpCurrServerVrf": zxAnSysNtpCurrServerVrf,
       "zxAnSysNtpClientAddrType": zxAnSysNtpClientAddrType,
       "zxAnSysNtpClientAddrIpv6": zxAnSysNtpClientAddrIpv6,
       "zxAnSysNtpAuthenticationEnable": zxAnSysNtpAuthenticationEnable,
       "zxAnSysNtpServerTable": zxAnSysNtpServerTable,
       "zxAnSysNtpServerEntry": zxAnSysNtpServerEntry,
       "zxAnSysNtpServerPriority": zxAnSysNtpServerPriority,
       "zxAnSysNtpServerVrf": zxAnSysNtpServerVrf,
       "zxAnSysNtpServerIpAddressType": zxAnSysNtpServerIpAddressType,
       "zxAnSysNtpServerIpAddress": zxAnSysNtpServerIpAddress,
       "zxAnSysNtpServerVersion": zxAnSysNtpServerVersion,
       "zxAnSysNtpServerAuthKeyId": zxAnSysNtpServerAuthKeyId,
       "zxAnSysNtpServerLock": zxAnSysNtpServerLock,
       "zxAnSysNtpServerRowStatus": zxAnSysNtpServerRowStatus,
       "zxAnSysNtpAuthenticationTable": zxAnSysNtpAuthenticationTable,
       "zxAnSysNtpAuthenticationEntry": zxAnSysNtpAuthenticationEntry,
       "zxAnSysNtpAuthenticationKeyId": zxAnSysNtpAuthenticationKeyId,
       "zxAnSysNtpAuthenticationKey": zxAnSysNtpAuthenticationKey,
       "zxAnSysNtpAuthenticationTrust": zxAnSysNtpAuthenticationTrust,
       "zxAnSysNtpAuthRowStatus": zxAnSysNtpAuthRowStatus,
       "zxAnSysNtpIfConfigTable": zxAnSysNtpIfConfigTable,
       "zxAnSysNtpIfConfigEntry": zxAnSysNtpIfConfigEntry,
       "zxAnSysNtpIfIndex": zxAnSysNtpIfIndex,
       "zxAnSysNtpIfBroadcastClientEn": zxAnSysNtpIfBroadcastClientEn,
       "zxAnSysNtpIfMulticastClientEn": zxAnSysNtpIfMulticastClientEn,
       "zxAnSysNtpIfMulticastIpAddrType": zxAnSysNtpIfMulticastIpAddrType,
       "zxAnSysNtpIfMulticastIpAddr": zxAnSysNtpIfMulticastIpAddr,
       "zxAnSysNtpIfConfigRowStatus": zxAnSysNtpIfConfigRowStatus,
       "zxAnRtcZoneAlias": zxAnRtcZoneAlias,
       "zxAnRtcZoneMinutes": zxAnRtcZoneMinutes,
       "zxAnSysSummerTimeMgmt": zxAnSysSummerTimeMgmt,
       "zxAnRtcSummerTimeAdminStatus": zxAnRtcSummerTimeAdminStatus,
       "zxAnRtcSummerTimeName": zxAnRtcSummerTimeName,
       "zxAnRtcSummerTimeType": zxAnRtcSummerTimeType,
       "zxAnRtcSummerTimeStart": zxAnRtcSummerTimeStart,
       "zxAnRtcSummerTimeEnd": zxAnRtcSummerTimeEnd,
       "zxAnRtcSummerTimeOffset": zxAnRtcSummerTimeOffset,
       "zxAnRtcSummerTimeOperStatus": zxAnRtcSummerTimeOperStatus,
       "zxAnSysPtpMgmt": zxAnSysPtpMgmt,
       "zxAnSysPtpGlobalObjects": zxAnSysPtpGlobalObjects,
       "zxAnSysPtpConfigClockMode": zxAnSysPtpConfigClockMode,
       "zxAnSysPtpConfigTsc": zxAnSysPtpConfigTsc,
       "zxAnSysPtpServiceVlan": zxAnSysPtpServiceVlan,
       "zxAnSysPtpTodTransMode": zxAnSysPtpTodTransMode,
       "zxAnSysPtpTodSignalType": zxAnSysPtpTodSignalType,
       "zxAnSysPtpPortTable": zxAnSysPtpPortTable,
       "zxAnSysPtpPortEntry": zxAnSysPtpPortEntry,
       "zxAnSysPtpPortIndex": zxAnSysPtpPortIndex,
       "zxAnSysPtpPortConfState": zxAnSysPtpPortConfState,
       "zxAnSysPtpPortSyncInterval": zxAnSysPtpPortSyncInterval,
       "zxAnSysPtpPortClockDestIpAddress": zxAnSysPtpPortClockDestIpAddress,
       "zxAnSysPtpPortRowStatus": zxAnSysPtpPortRowStatus,
       "zxAnSysSnmpOperSyslogMgmt": zxAnSysSnmpOperSyslogMgmt,
       "zxAnSysSnmpOperSyslogStatus": zxAnSysSnmpOperSyslogStatus,
       "zxAnSysSnmpOperOidExceptTable": zxAnSysSnmpOperOidExceptTable,
       "zxAnSysSnmpOperOidExceptEntry": zxAnSysSnmpOperOidExceptEntry,
       "zxAnSysSnmpOidId": zxAnSysSnmpOidId,
       "zxAnSysSnmpOidItem": zxAnSysSnmpOidItem,
       "zxAnSysSnmpOidRowStatus": zxAnSysSnmpOidRowStatus,
       "zxAnLog": zxAnLog,
       "zxAnLogTypeTable": zxAnLogTypeTable,
       "zxAnLogTypeEntry": zxAnLogTypeEntry,
       "zxAnLogType": zxAnLogType,
       "zxAnLogLevel": zxAnLogLevel,
       "zxAnLogTypeDesc": zxAnLogTypeDesc,
       "zxAnLogConfTable": zxAnLogConfTable,
       "zxAnLogConfEntry": zxAnLogConfEntry,
       "zxAnLogConfType": zxAnLogConfType,
       "zxAnLogConfLevel": zxAnLogConfLevel,
       "zxAnLogCapability": zxAnLogCapability,
       "zxAnLogConfig": zxAnLogConfig,
       "zxAnLogGlobalObjects": zxAnLogGlobalObjects,
       "zxAnLogClear": zxAnLogClear,
       "zxAnSysClockMgmt": zxAnSysClockMgmt,
       "zxAnSysConfigClockSource": zxAnSysConfigClockSource,
       "zxAnSysActualClockSource": zxAnSysActualClockSource,
       "zxAnSysSupportClockSource": zxAnSysSupportClockSource,
       "zxAnSysAvailableClockSource": zxAnSysAvailableClockSource,
       "zxAnSysClockSourcePriority": zxAnSysClockSourcePriority,
       "zxAnSysActualClockSourceE1": zxAnSysActualClockSourceE1,
       "zxAnSysLastClockSource": zxAnSysLastClockSource,
       "zxAnSysLastClockSourceE1": zxAnSysLastClockSourceE1,
       "zxAnSysClockSourceTrapEnable": zxAnSysClockSourceTrapEnable,
       "zxAnSysClockSourceIfType": zxAnSysClockSourceIfType,
       "zxAnSysDsx1ClockSourceTable": zxAnSysDsx1ClockSourceTable,
       "zxAnSysDsx1ClockSourceEntry": zxAnSysDsx1ClockSourceEntry,
       "zxAnSysDsx1ClkSrcRack": zxAnSysDsx1ClkSrcRack,
       "zxAnSysDsx1ClkSrcShelf": zxAnSysDsx1ClkSrcShelf,
       "zxAnSysDsx1ClkSrcSlot": zxAnSysDsx1ClkSrcSlot,
       "zxAnSysDsx1ClkSrcLinkNo": zxAnSysDsx1ClkSrcLinkNo,
       "zxAnSysDsx1ClkSrcAvailableStatus": zxAnSysDsx1ClkSrcAvailableStatus,
       "zxAnSysDsx1ClkSrcCurrUsingStatus": zxAnSysDsx1ClkSrcCurrUsingStatus,
       "zxAnSysDsx1ClkSrcPriority": zxAnSysDsx1ClkSrcPriority,
       "zxAnSysIpv6GlobalMgmt": zxAnSysIpv6GlobalMgmt,
       "zxAnSysIpv6GlobalEnable": zxAnSysIpv6GlobalEnable,
       "zxAnSysDns": zxAnSysDns,
       "zxAnSysDnsServerTable": zxAnSysDnsServerTable,
       "zxAnSysDnsServerEntry": zxAnSysDnsServerEntry,
       "zxAnSysDnsServerIpAddressType": zxAnSysDnsServerIpAddressType,
       "zxAnSysDnsServerIpAddress": zxAnSysDnsServerIpAddress,
       "zxAnSysDnsServerType": zxAnSysDnsServerType,
       "zxAnSysDnsServerRowStatus": zxAnSysDnsServerRowStatus,
       "zxAnSysDnsGlobalObjects": zxAnSysDnsGlobalObjects,
       "zxAnSysDnsRequestMode": zxAnSysDnsRequestMode,
       "zxAnSysOutbandPortMgmt": zxAnSysOutbandPortMgmt,
       "zxAnSysOutbandPortAdminStatus": zxAnSysOutbandPortAdminStatus,
       "zxAnSysOutbandPortOperStatus": zxAnSysOutbandPortOperStatus,
       "zxAnSysOutbandPortDuplexSpeed": zxAnSysOutbandPortDuplexSpeed,
       "zxAnSysOutbandPortActualDuplex": zxAnSysOutbandPortActualDuplex,
       "zxAnSysOutbandPortActualSpeed": zxAnSysOutbandPortActualSpeed,
       "zxAnSysOutbandPortTagMode": zxAnSysOutbandPortTagMode,
       "zxAnSysOutbandPortVlanId": zxAnSysOutbandPortVlanId,
       "zxAnSysOutbandPortCos": zxAnSysOutbandPortCos,
       "zxAnSysSnmpMgmt": zxAnSysSnmpMgmt,
       "zxAnSnmpEngineIdGenerateMode": zxAnSnmpEngineIdGenerateMode,
       "zxAnSnmpSupportedVersion": zxAnSnmpSupportedVersion,
       "zxAnSysProfileOperMgmt": zxAnSysProfileOperMgmt,
       "zxAnSysProfileOperGlobalObjects": zxAnSysProfileOperGlobalObjects,
       "zxAnSysProfileCategory": zxAnSysProfileCategory,
       "zxAnSysProfileName": zxAnSysProfileName,
       "zxAnSysProfileId": zxAnSysProfileId,
       "zxAnSysProfileInfo": zxAnSysProfileInfo,
       "zxAnSysMgmtArp": zxAnSysMgmtArp,
       "zxAnSysMgmtArpGlobalObjects": zxAnSysMgmtArpGlobalObjects,
       "zxAnSysMgmtArpAgingTime": zxAnSysMgmtArpAgingTime,
       "zxAnSysTrapObjects": zxAnSysTrapObjects,
       "zxAnSysNtpTrapGroup": zxAnSysNtpTrapGroup,
       "zxAnSysNtpOffsetOverThreshTrap": zxAnSysNtpOffsetOverThreshTrap,
       "zxAnSysNtpOffsetUnderThreshTrap": zxAnSysNtpOffsetUnderThreshTrap,
       "zxAnSysSecurityTrapGroup": zxAnSysSecurityTrapGroup,
       "zxAnSysSecCrftTerminLogonTrap": zxAnSysSecCrftTerminLogonTrap,
       "zxAnSysSecCrftTerminLogoutTrap": zxAnSysSecCrftTerminLogoutTrap,
       "zxAnSysSecCrftTerminLoginFailed": zxAnSysSecCrftTerminLoginFailed,
       "zxAnSysSummerTimeTrapGroup": zxAnSysSummerTimeTrapGroup,
       "zxAnSysSummerTimeStartTrap": zxAnSysSummerTimeStartTrap,
       "zxAnSysSummerTimeEndTrap": zxAnSysSummerTimeEndTrap,
       "zxAnSysClockTrapGroup": zxAnSysClockTrapGroup,
       "zxAnSysClockSourceSwitchTrap": zxAnSysClockSourceSwitchTrap,
       "zxAnSysClkSrcUnavailableTrap": zxAnSysClkSrcUnavailableTrap,
       "zxAnSysClkSrcAvailableTrap": zxAnSysClkSrcAvailableTrap,
       "zxAnSysProfileOperTrapGroup": zxAnSysProfileOperTrapGroup,
       "zxAnSysDelAppliedPrfFailedNotify": zxAnSysDelAppliedPrfFailedNotify,
       "zxAnSysResourceTrapGroup": zxAnSysResourceTrapGroup,
       "zxAnSysResourceInsufficientTrap": zxAnSysResourceInsufficientTrap}
)
