# SNMP MIB module (ZTE-DSL-SEC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/zte/ZTE-DSL-SEC-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:45:04 2025
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 PhysAddress,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")

(zxDsl,) = mibBuilder.importSymbols(
    "ZTE-DSL-MIB",
    "zxDsl")


# MODULE-IDENTITY

zxDslSysSecMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 36)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ZxDslSysSecObjects_ObjectIdentity = ObjectIdentity
zxDslSysSecObjects = _ZxDslSysSecObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 36, 1)
)


class _ZxDslCrftTerminalEnable_Type(Integer32):
    """Custom type zxDslCrftTerminalEnable based on Integer32"""
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


_ZxDslCrftTerminalEnable_Type.__name__ = "Integer32"
_ZxDslCrftTerminalEnable_Object = MibScalar
zxDslCrftTerminalEnable = _ZxDslCrftTerminalEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 36, 1, 1),
    _ZxDslCrftTerminalEnable_Type()
)
zxDslCrftTerminalEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxDslCrftTerminalEnable.setStatus("current")


class _ZxDslCliSecurityLevel_Type(Integer32):
    """Custom type zxDslCliSecurityLevel based on Integer32"""
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


_ZxDslCliSecurityLevel_Type.__name__ = "Integer32"
_ZxDslCliSecurityLevel_Object = MibScalar
zxDslCliSecurityLevel = _ZxDslCliSecurityLevel_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 36, 1, 2),
    _ZxDslCliSecurityLevel_Type()
)
zxDslCliSecurityLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxDslCliSecurityLevel.setStatus("current")


class _ZxDslCrftTerminalLogonStatus_Type(Integer32):
    """Custom type zxDslCrftTerminalLogonStatus based on Integer32"""
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


_ZxDslCrftTerminalLogonStatus_Type.__name__ = "Integer32"
_ZxDslCrftTerminalLogonStatus_Object = MibScalar
zxDslCrftTerminalLogonStatus = _ZxDslCrftTerminalLogonStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 36, 1, 3),
    _ZxDslCrftTerminalLogonStatus_Type()
)
zxDslCrftTerminalLogonStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxDslCrftTerminalLogonStatus.setStatus("current")


class _ZxDslSysLatestLogonCrftTerminalType_Type(Integer32):
    """Custom type zxDslSysLatestLogonCrftTerminalType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("rs232SerialInterface", 1),
          ("outbandMgmtInterface", 2))
    )


_ZxDslSysLatestLogonCrftTerminalType_Type.__name__ = "Integer32"
_ZxDslSysLatestLogonCrftTerminalType_Object = MibScalar
zxDslSysLatestLogonCrftTerminalType = _ZxDslSysLatestLogonCrftTerminalType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 36, 1, 4),
    _ZxDslSysLatestLogonCrftTerminalType_Type()
)
zxDslSysLatestLogonCrftTerminalType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxDslSysLatestLogonCrftTerminalType.setStatus("current")


class _ZxDslCliLogonWelcomeMessage_Type(DisplayString):
    """Custom type zxDslCliLogonWelcomeMessage based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 400),
    )


_ZxDslCliLogonWelcomeMessage_Type.__name__ = "DisplayString"
_ZxDslCliLogonWelcomeMessage_Object = MibScalar
zxDslCliLogonWelcomeMessage = _ZxDslCliLogonWelcomeMessage_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 36, 1, 5),
    _ZxDslCliLogonWelcomeMessage_Type()
)
zxDslCliLogonWelcomeMessage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxDslCliLogonWelcomeMessage.setStatus("current")


class _ZxDslCliLogonOvertimeMin_Type(Integer32):
    """Custom type zxDslCliLogonOvertimeMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_ZxDslCliLogonOvertimeMin_Type.__name__ = "Integer32"
_ZxDslCliLogonOvertimeMin_Object = MibScalar
zxDslCliLogonOvertimeMin = _ZxDslCliLogonOvertimeMin_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 36, 1, 6),
    _ZxDslCliLogonOvertimeMin_Type()
)
zxDslCliLogonOvertimeMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxDslCliLogonOvertimeMin.setStatus("current")


class _ZxDslIllegalLoginUserName_Type(DisplayString):
    """Custom type zxDslIllegalLoginUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_ZxDslIllegalLoginUserName_Type.__name__ = "DisplayString"
_ZxDslIllegalLoginUserName_Object = MibScalar
zxDslIllegalLoginUserName = _ZxDslIllegalLoginUserName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 36, 1, 7),
    _ZxDslIllegalLoginUserName_Type()
)
zxDslIllegalLoginUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxDslIllegalLoginUserName.setStatus("current")


class _ZxDslIllegalLoginType_Type(Integer32):
    """Custom type zxDslIllegalLoginType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("console", 1),
          ("telnet", 2),
          ("ssh", 3))
    )


_ZxDslIllegalLoginType_Type.__name__ = "Integer32"
_ZxDslIllegalLoginType_Object = MibScalar
zxDslIllegalLoginType = _ZxDslIllegalLoginType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 36, 1, 8),
    _ZxDslIllegalLoginType_Type()
)
zxDslIllegalLoginType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxDslIllegalLoginType.setStatus("current")
_ZxDslIllegalLoginIP_Type = IpAddress
_ZxDslIllegalLoginIP_Object = MibScalar
zxDslIllegalLoginIP = _ZxDslIllegalLoginIP_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 36, 1, 9),
    _ZxDslIllegalLoginIP_Type()
)
zxDslIllegalLoginIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxDslIllegalLoginIP.setStatus("current")
_ZxDslSysSecTrapObjects_ObjectIdentity = ObjectIdentity
zxDslSysSecTrapObjects = _ZxDslSysSecTrapObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 36, 2)
)

# Managed Objects groups


# Notification objects

zxDslCrftTerminLogonTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 36, 2, 1)
)
zxDslCrftTerminLogonTrap.setObjects(
    ("ZTE-DSL-SEC-MIB", "zxDslSysLatestLogonCrftTerminalType")
)
if mibBuilder.loadTexts:
    zxDslCrftTerminLogonTrap.setStatus(
        "current"
    )

zxDslCrftTerminLogoutTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 36, 2, 2)
)
zxDslCrftTerminLogoutTrap.setObjects(
    ("ZTE-DSL-SEC-MIB", "zxDslSysLatestLogonCrftTerminalType")
)
if mibBuilder.loadTexts:
    zxDslCrftTerminLogoutTrap.setStatus(
        "current"
    )

zxDslIllegalLoginTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 36, 2, 3)
)
zxDslIllegalLoginTrap.setObjects(
      *(("ZTE-DSL-SEC-MIB", "zxDslIllegalLoginUserName"),
        ("ZTE-DSL-SEC-MIB", "zxDslIllegalLoginType"),
        ("ZTE-DSL-SEC-MIB", "zxDslIllegalLoginIP"))
)
if mibBuilder.loadTexts:
    zxDslIllegalLoginTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZTE-DSL-SEC-MIB",
    **{"zxDslSysSecMib": zxDslSysSecMib,
       "zxDslSysSecObjects": zxDslSysSecObjects,
       "zxDslCrftTerminalEnable": zxDslCrftTerminalEnable,
       "zxDslCliSecurityLevel": zxDslCliSecurityLevel,
       "zxDslCrftTerminalLogonStatus": zxDslCrftTerminalLogonStatus,
       "zxDslSysLatestLogonCrftTerminalType": zxDslSysLatestLogonCrftTerminalType,
       "zxDslCliLogonWelcomeMessage": zxDslCliLogonWelcomeMessage,
       "zxDslCliLogonOvertimeMin": zxDslCliLogonOvertimeMin,
       "zxDslIllegalLoginUserName": zxDslIllegalLoginUserName,
       "zxDslIllegalLoginType": zxDslIllegalLoginType,
       "zxDslIllegalLoginIP": zxDslIllegalLoginIP,
       "zxDslSysSecTrapObjects": zxDslSysSecTrapObjects,
       "zxDslCrftTerminLogonTrap": zxDslCrftTerminLogonTrap,
       "zxDslCrftTerminLogoutTrap": zxDslCrftTerminLogoutTrap,
       "zxDslIllegalLoginTrap": zxDslIllegalLoginTrap}
)
