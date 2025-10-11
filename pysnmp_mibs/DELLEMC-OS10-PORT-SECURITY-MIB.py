# SNMP MIB module (DELLEMC-OS10-PORT-SECURITY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/dell/DELLEMC-OS10-PORT-SECURITY-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:08:11 2025
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

(os10,) = mibBuilder.importSymbols(
    "DELLEMC-OS10-SMI-MIB",
    "os10")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(VlanIndex,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "VlanIndex")

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
 MacAddress,
 PhysAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

os10PortSecurityMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 100, 5)
)
if mibBuilder.loadTexts:
    os10PortSecurityMib.setRevisions(
        ("2019-07-22 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class SecureMacAddrType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("dynamic", 1),
          ("sticky", 2),
          ("all", 3))
    )



class SecureMacViolationType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("macLimitViolation", 1),
          ("stmvViolation", 2))
    )



# MIB Managed Objects in the order of their OIDs

_Os10PortSecurityMibObjects_ObjectIdentity = ObjectIdentity
os10PortSecurityMibObjects = _Os10PortSecurityMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 100, 5, 1)
)
_Os10PortSecurityGlobalObjects_ObjectIdentity = ObjectIdentity
os10PortSecurityGlobalObjects = _Os10PortSecurityGlobalObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 100, 5, 1, 1)
)


class _Os10PortSecurityGlobalEnable_Type(TruthValue):
    """Custom type os10PortSecurityGlobalEnable based on TruthValue"""
    defaultValue = 1


_Os10PortSecurityGlobalEnable_Type.__name__ = "TruthValue"
_Os10PortSecurityGlobalEnable_Object = MibScalar
os10PortSecurityGlobalEnable = _Os10PortSecurityGlobalEnable_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 100, 5, 1, 1, 1),
    _Os10PortSecurityGlobalEnable_Type()
)
os10PortSecurityGlobalEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    os10PortSecurityGlobalEnable.setStatus("current")


class _Os10PortSecurityGlobalTotalSecureAddresses_Type(Integer32):
    """Custom type os10PortSecurityGlobalTotalSecureAddresses based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Os10PortSecurityGlobalTotalSecureAddresses_Type.__name__ = "Integer32"
_Os10PortSecurityGlobalTotalSecureAddresses_Object = MibScalar
os10PortSecurityGlobalTotalSecureAddresses = _Os10PortSecurityGlobalTotalSecureAddresses_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 100, 5, 1, 1, 2),
    _Os10PortSecurityGlobalTotalSecureAddresses_Type()
)
os10PortSecurityGlobalTotalSecureAddresses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    os10PortSecurityGlobalTotalSecureAddresses.setStatus("current")


class _Os10PortSecurityGlobalTotalSecureDynamicAddresses_Type(Integer32):
    """Custom type os10PortSecurityGlobalTotalSecureDynamicAddresses based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Os10PortSecurityGlobalTotalSecureDynamicAddresses_Type.__name__ = "Integer32"
_Os10PortSecurityGlobalTotalSecureDynamicAddresses_Object = MibScalar
os10PortSecurityGlobalTotalSecureDynamicAddresses = _Os10PortSecurityGlobalTotalSecureDynamicAddresses_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 100, 5, 1, 1, 3),
    _Os10PortSecurityGlobalTotalSecureDynamicAddresses_Type()
)
os10PortSecurityGlobalTotalSecureDynamicAddresses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    os10PortSecurityGlobalTotalSecureDynamicAddresses.setStatus("current")


class _Os10PortSecurityGlobalTotalSecureStickyAddresses_Type(Integer32):
    """Custom type os10PortSecurityGlobalTotalSecureStickyAddresses based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Os10PortSecurityGlobalTotalSecureStickyAddresses_Type.__name__ = "Integer32"
_Os10PortSecurityGlobalTotalSecureStickyAddresses_Object = MibScalar
os10PortSecurityGlobalTotalSecureStickyAddresses = _Os10PortSecurityGlobalTotalSecureStickyAddresses_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 100, 5, 1, 1, 4),
    _Os10PortSecurityGlobalTotalSecureStickyAddresses_Type()
)
os10PortSecurityGlobalTotalSecureStickyAddresses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    os10PortSecurityGlobalTotalSecureStickyAddresses.setStatus("current")


class _Os10PortSecurityGlobalTotalSecureStaticAddresses_Type(Integer32):
    """Custom type os10PortSecurityGlobalTotalSecureStaticAddresses based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Os10PortSecurityGlobalTotalSecureStaticAddresses_Type.__name__ = "Integer32"
_Os10PortSecurityGlobalTotalSecureStaticAddresses_Object = MibScalar
os10PortSecurityGlobalTotalSecureStaticAddresses = _Os10PortSecurityGlobalTotalSecureStaticAddresses_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 100, 5, 1, 1, 5),
    _Os10PortSecurityGlobalTotalSecureStaticAddresses_Type()
)
os10PortSecurityGlobalTotalSecureStaticAddresses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    os10PortSecurityGlobalTotalSecureStaticAddresses.setStatus("current")
_Os10PortSecurityGlobalClearSecureMacAddresses_Type = SecureMacAddrType
_Os10PortSecurityGlobalClearSecureMacAddresses_Object = MibScalar
os10PortSecurityGlobalClearSecureMacAddresses = _Os10PortSecurityGlobalClearSecureMacAddresses_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 100, 5, 1, 1, 6),
    _Os10PortSecurityGlobalClearSecureMacAddresses_Type()
)
os10PortSecurityGlobalClearSecureMacAddresses.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    os10PortSecurityGlobalClearSecureMacAddresses.setStatus("current")
_Os10PortSecurityGlobalResetViolation_Type = SecureMacViolationType
_Os10PortSecurityGlobalResetViolation_Object = MibScalar
os10PortSecurityGlobalResetViolation = _Os10PortSecurityGlobalResetViolation_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 100, 5, 1, 1, 7),
    _Os10PortSecurityGlobalResetViolation_Type()
)
os10PortSecurityGlobalResetViolation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    os10PortSecurityGlobalResetViolation.setStatus("current")
_Os10PortSecurityInterfaceObjects_ObjectIdentity = ObjectIdentity
os10PortSecurityInterfaceObjects = _Os10PortSecurityInterfaceObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 100, 5, 1, 2)
)
_Os10PortSecurityIfConfigTable_Object = MibTable
os10PortSecurityIfConfigTable = _Os10PortSecurityIfConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 100, 5, 1, 2, 1)
)
if mibBuilder.loadTexts:
    os10PortSecurityIfConfigTable.setStatus("current")
_Os10PortSecurityIfConfigEntry_Object = MibTableRow
os10PortSecurityIfConfigEntry = _Os10PortSecurityIfConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 100, 5, 1, 2, 1, 1)
)
os10PortSecurityIfConfigEntry.setIndexNames(
    (0, "DELLEMC-OS10-PORT-SECURITY-MIB", "os10PortSecurityIfIndex"),
)
if mibBuilder.loadTexts:
    os10PortSecurityIfConfigEntry.setStatus("current")
_Os10PortSecurityIfIndex_Type = InterfaceIndex
_Os10PortSecurityIfIndex_Object = MibTableColumn
os10PortSecurityIfIndex = _Os10PortSecurityIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 100, 5, 1, 2, 1, 1, 1),
    _Os10PortSecurityIfIndex_Type()
)
os10PortSecurityIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    os10PortSecurityIfIndex.setStatus("current")


class _Os10PortSecurityIfPortSecurityEnable_Type(TruthValue):
    """Custom type os10PortSecurityIfPortSecurityEnable based on TruthValue"""
    defaultValue = 2


_Os10PortSecurityIfPortSecurityEnable_Type.__name__ = "TruthValue"
_Os10PortSecurityIfPortSecurityEnable_Object = MibTableColumn
os10PortSecurityIfPortSecurityEnable = _Os10PortSecurityIfPortSecurityEnable_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 100, 5, 1, 2, 1, 1, 2),
    _Os10PortSecurityIfPortSecurityEnable_Type()
)
os10PortSecurityIfPortSecurityEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    os10PortSecurityIfPortSecurityEnable.setStatus("current")


class _Os10PortSecurityIfViolationStatus_Type(Integer32):
    """Custom type os10PortSecurityIfViolationStatus based on Integer32"""
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
          ("macLearnLimitErrDisable", 2),
          ("stationMoveErrDisable", 3))
    )


_Os10PortSecurityIfViolationStatus_Type.__name__ = "Integer32"
_Os10PortSecurityIfViolationStatus_Object = MibTableColumn
os10PortSecurityIfViolationStatus = _Os10PortSecurityIfViolationStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 100, 5, 1, 2, 1, 1, 3),
    _Os10PortSecurityIfViolationStatus_Type()
)
os10PortSecurityIfViolationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    os10PortSecurityIfViolationStatus.setStatus("current")


class _Os10PortSecurityIfSecureMacLearnLimit_Type(Unsigned32):
    """Custom type os10PortSecurityIfSecureMacLearnLimit based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_Os10PortSecurityIfSecureMacLearnLimit_Type.__name__ = "Unsigned32"
_Os10PortSecurityIfSecureMacLearnLimit_Object = MibTableColumn
os10PortSecurityIfSecureMacLearnLimit = _Os10PortSecurityIfSecureMacLearnLimit_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 100, 5, 1, 2, 1, 1, 4),
    _Os10PortSecurityIfSecureMacLearnLimit_Type()
)
os10PortSecurityIfSecureMacLearnLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    os10PortSecurityIfSecureMacLearnLimit.setStatus("current")


class _Os10PortSecurityIfStationMoveEnable_Type(TruthValue):
    """Custom type os10PortSecurityIfStationMoveEnable based on TruthValue"""
    defaultValue = 2


_Os10PortSecurityIfStationMoveEnable_Type.__name__ = "TruthValue"
_Os10PortSecurityIfStationMoveEnable_Object = MibTableColumn
os10PortSecurityIfStationMoveEnable = _Os10PortSecurityIfStationMoveEnable_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 100, 5, 1, 2, 1, 1, 5),
    _Os10PortSecurityIfStationMoveEnable_Type()
)
os10PortSecurityIfStationMoveEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    os10PortSecurityIfStationMoveEnable.setStatus("current")


class _Os10PortSecurityIfMacViolationAction_Type(Integer32):
    """Custom type os10PortSecurityIfMacViolationAction based on Integer32"""
    defaultValue = 2

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
        *(("drop", 1),
          ("dropAndNotify", 2),
          ("shutdown", 3),
          ("forward", 4))
    )


_Os10PortSecurityIfMacViolationAction_Type.__name__ = "Integer32"
_Os10PortSecurityIfMacViolationAction_Object = MibTableColumn
os10PortSecurityIfMacViolationAction = _Os10PortSecurityIfMacViolationAction_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 100, 5, 1, 2, 1, 1, 6),
    _Os10PortSecurityIfMacViolationAction_Type()
)
os10PortSecurityIfMacViolationAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    os10PortSecurityIfMacViolationAction.setStatus("current")


class _Os10PortSecurityIfStmvViolationAction_Type(Integer32):
    """Custom type os10PortSecurityIfStmvViolationAction based on Integer32"""
    defaultValue = 2

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
        *(("drop", 1),
          ("dropAndNotify", 2),
          ("shutdownOrigPort", 3),
          ("shutDownOffendingPort", 4),
          ("shutdownBoth", 5))
    )


_Os10PortSecurityIfStmvViolationAction_Type.__name__ = "Integer32"
_Os10PortSecurityIfStmvViolationAction_Object = MibTableColumn
os10PortSecurityIfStmvViolationAction = _Os10PortSecurityIfStmvViolationAction_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 100, 5, 1, 2, 1, 1, 7),
    _Os10PortSecurityIfStmvViolationAction_Type()
)
os10PortSecurityIfStmvViolationAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    os10PortSecurityIfStmvViolationAction.setStatus("current")


class _Os10PortSecurityIfStickyEnable_Type(TruthValue):
    """Custom type os10PortSecurityIfStickyEnable based on TruthValue"""
    defaultValue = 2


_Os10PortSecurityIfStickyEnable_Type.__name__ = "TruthValue"
_Os10PortSecurityIfStickyEnable_Object = MibTableColumn
os10PortSecurityIfStickyEnable = _Os10PortSecurityIfStickyEnable_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 100, 5, 1, 2, 1, 1, 8),
    _Os10PortSecurityIfStickyEnable_Type()
)
os10PortSecurityIfStickyEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    os10PortSecurityIfStickyEnable.setStatus("current")
_Os10PortSecurityIfClearSecureMacAddresses_Type = SecureMacAddrType
_Os10PortSecurityIfClearSecureMacAddresses_Object = MibTableColumn
os10PortSecurityIfClearSecureMacAddresses = _Os10PortSecurityIfClearSecureMacAddresses_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 100, 5, 1, 2, 1, 1, 9),
    _Os10PortSecurityIfClearSecureMacAddresses_Type()
)
os10PortSecurityIfClearSecureMacAddresses.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    os10PortSecurityIfClearSecureMacAddresses.setStatus("current")


class _Os10PortSecurityIfSecureMacAgeEnable_Type(TruthValue):
    """Custom type os10PortSecurityIfSecureMacAgeEnable based on TruthValue"""
    defaultValue = 2


_Os10PortSecurityIfSecureMacAgeEnable_Type.__name__ = "TruthValue"
_Os10PortSecurityIfSecureMacAgeEnable_Object = MibTableColumn
os10PortSecurityIfSecureMacAgeEnable = _Os10PortSecurityIfSecureMacAgeEnable_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 100, 5, 1, 2, 1, 1, 10),
    _Os10PortSecurityIfSecureMacAgeEnable_Type()
)
os10PortSecurityIfSecureMacAgeEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    os10PortSecurityIfSecureMacAgeEnable.setStatus("current")


class _Os10PortSecurityIfTotalSecureAddresses_Type(Integer32):
    """Custom type os10PortSecurityIfTotalSecureAddresses based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Os10PortSecurityIfTotalSecureAddresses_Type.__name__ = "Integer32"
_Os10PortSecurityIfTotalSecureAddresses_Object = MibTableColumn
os10PortSecurityIfTotalSecureAddresses = _Os10PortSecurityIfTotalSecureAddresses_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 100, 5, 1, 2, 1, 1, 11),
    _Os10PortSecurityIfTotalSecureAddresses_Type()
)
os10PortSecurityIfTotalSecureAddresses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    os10PortSecurityIfTotalSecureAddresses.setStatus("current")


class _Os10PortSecurityIfTotalSecureDynamicAddresses_Type(Integer32):
    """Custom type os10PortSecurityIfTotalSecureDynamicAddresses based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Os10PortSecurityIfTotalSecureDynamicAddresses_Type.__name__ = "Integer32"
_Os10PortSecurityIfTotalSecureDynamicAddresses_Object = MibTableColumn
os10PortSecurityIfTotalSecureDynamicAddresses = _Os10PortSecurityIfTotalSecureDynamicAddresses_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 100, 5, 1, 2, 1, 1, 12),
    _Os10PortSecurityIfTotalSecureDynamicAddresses_Type()
)
os10PortSecurityIfTotalSecureDynamicAddresses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    os10PortSecurityIfTotalSecureDynamicAddresses.setStatus("current")


class _Os10PortSecurityIfTotalSecureStickyAddresses_Type(Integer32):
    """Custom type os10PortSecurityIfTotalSecureStickyAddresses based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Os10PortSecurityIfTotalSecureStickyAddresses_Type.__name__ = "Integer32"
_Os10PortSecurityIfTotalSecureStickyAddresses_Object = MibTableColumn
os10PortSecurityIfTotalSecureStickyAddresses = _Os10PortSecurityIfTotalSecureStickyAddresses_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 100, 5, 1, 2, 1, 1, 13),
    _Os10PortSecurityIfTotalSecureStickyAddresses_Type()
)
os10PortSecurityIfTotalSecureStickyAddresses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    os10PortSecurityIfTotalSecureStickyAddresses.setStatus("current")


class _Os10PortSecurityIfTotalSecureStaticAddresses_Type(Integer32):
    """Custom type os10PortSecurityIfTotalSecureStaticAddresses based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Os10PortSecurityIfTotalSecureStaticAddresses_Type.__name__ = "Integer32"
_Os10PortSecurityIfTotalSecureStaticAddresses_Object = MibTableColumn
os10PortSecurityIfTotalSecureStaticAddresses = _Os10PortSecurityIfTotalSecureStaticAddresses_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 100, 5, 1, 2, 1, 1, 14),
    _Os10PortSecurityIfTotalSecureStaticAddresses_Type()
)
os10PortSecurityIfTotalSecureStaticAddresses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    os10PortSecurityIfTotalSecureStaticAddresses.setStatus("current")
_Os10PortSecurityMacObjects_ObjectIdentity = ObjectIdentity
os10PortSecurityMacObjects = _Os10PortSecurityMacObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 100, 5, 1, 3)
)
_Os10PortSecuritySecureMacAddrTable_Object = MibTable
os10PortSecuritySecureMacAddrTable = _Os10PortSecuritySecureMacAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 100, 5, 1, 3, 1)
)
if mibBuilder.loadTexts:
    os10PortSecuritySecureMacAddrTable.setStatus("current")
_Os10PortSecuritySecureMacAddrEntry_Object = MibTableRow
os10PortSecuritySecureMacAddrEntry = _Os10PortSecuritySecureMacAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 100, 5, 1, 3, 1, 1)
)
os10PortSecuritySecureMacAddrEntry.setIndexNames(
    (0, "DELLEMC-OS10-PORT-SECURITY-MIB", "os10PortSecuritySecureMacVlanId"),
    (0, "DELLEMC-OS10-PORT-SECURITY-MIB", "os10PortSecuritySecureMacAddress"),
)
if mibBuilder.loadTexts:
    os10PortSecuritySecureMacAddrEntry.setStatus("current")
_Os10PortSecuritySecureMacVlanId_Type = VlanIndex
_Os10PortSecuritySecureMacVlanId_Object = MibTableColumn
os10PortSecuritySecureMacVlanId = _Os10PortSecuritySecureMacVlanId_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 100, 5, 1, 3, 1, 1, 1),
    _Os10PortSecuritySecureMacVlanId_Type()
)
os10PortSecuritySecureMacVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    os10PortSecuritySecureMacVlanId.setStatus("current")
_Os10PortSecuritySecureMacAddress_Type = MacAddress
_Os10PortSecuritySecureMacAddress_Object = MibTableColumn
os10PortSecuritySecureMacAddress = _Os10PortSecuritySecureMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 100, 5, 1, 3, 1, 1, 2),
    _Os10PortSecuritySecureMacAddress_Type()
)
os10PortSecuritySecureMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    os10PortSecuritySecureMacAddress.setStatus("current")
_Os10PortSecuritySecureMacIfIndex_Type = InterfaceIndex
_Os10PortSecuritySecureMacIfIndex_Object = MibTableColumn
os10PortSecuritySecureMacIfIndex = _Os10PortSecuritySecureMacIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 100, 5, 1, 3, 1, 1, 3),
    _Os10PortSecuritySecureMacIfIndex_Type()
)
os10PortSecuritySecureMacIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    os10PortSecuritySecureMacIfIndex.setStatus("current")


class _Os10PortSecuritySecureMacAddrType_Type(Integer32):
    """Custom type os10PortSecuritySecureMacAddrType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("static", 1),
          ("dynamic", 2),
          ("sticky", 3))
    )


_Os10PortSecuritySecureMacAddrType_Type.__name__ = "Integer32"
_Os10PortSecuritySecureMacAddrType_Object = MibTableColumn
os10PortSecuritySecureMacAddrType = _Os10PortSecuritySecureMacAddrType_Object(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 100, 5, 1, 3, 1, 1, 4),
    _Os10PortSecuritySecureMacAddrType_Type()
)
os10PortSecuritySecureMacAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    os10PortSecuritySecureMacAddrType.setStatus("current")
_Os10PortSecurityMibConformance_ObjectIdentity = ObjectIdentity
os10PortSecurityMibConformance = _Os10PortSecurityMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 100, 5, 2)
)
_Os10PortSecurityCompliances_ObjectIdentity = ObjectIdentity
os10PortSecurityCompliances = _Os10PortSecurityCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 100, 5, 2, 1)
)
_Os10PortSecurityGroups_ObjectIdentity = ObjectIdentity
os10PortSecurityGroups = _Os10PortSecurityGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 100, 5, 2, 2)
)

# Managed Objects groups

os10PortSecurityGlobalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 100, 5, 2, 2, 1)
)
os10PortSecurityGlobalGroup.setObjects(
      *(("DELLEMC-OS10-PORT-SECURITY-MIB", "os10PortSecurityGlobalEnable"),
        ("DELLEMC-OS10-PORT-SECURITY-MIB", "os10PortSecurityGlobalTotalSecureAddresses"),
        ("DELLEMC-OS10-PORT-SECURITY-MIB", "os10PortSecurityGlobalTotalSecureDynamicAddresses"),
        ("DELLEMC-OS10-PORT-SECURITY-MIB", "os10PortSecurityGlobalTotalSecureStickyAddresses"),
        ("DELLEMC-OS10-PORT-SECURITY-MIB", "os10PortSecurityGlobalTotalSecureStaticAddresses"),
        ("DELLEMC-OS10-PORT-SECURITY-MIB", "os10PortSecurityGlobalClearSecureMacAddresses"),
        ("DELLEMC-OS10-PORT-SECURITY-MIB", "os10PortSecurityGlobalResetViolation"))
)
if mibBuilder.loadTexts:
    os10PortSecurityGlobalGroup.setStatus("current")

os10PortSecurityInterfaceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 100, 5, 2, 2, 2)
)
os10PortSecurityInterfaceGroup.setObjects(
      *(("DELLEMC-OS10-PORT-SECURITY-MIB", "os10PortSecurityIfPortSecurityEnable"),
        ("DELLEMC-OS10-PORT-SECURITY-MIB", "os10PortSecurityIfViolationStatus"),
        ("DELLEMC-OS10-PORT-SECURITY-MIB", "os10PortSecurityIfSecureMacLearnLimit"),
        ("DELLEMC-OS10-PORT-SECURITY-MIB", "os10PortSecurityIfStationMoveEnable"),
        ("DELLEMC-OS10-PORT-SECURITY-MIB", "os10PortSecurityIfMacViolationAction"),
        ("DELLEMC-OS10-PORT-SECURITY-MIB", "os10PortSecurityIfStmvViolationAction"),
        ("DELLEMC-OS10-PORT-SECURITY-MIB", "os10PortSecurityIfStickyEnable"),
        ("DELLEMC-OS10-PORT-SECURITY-MIB", "os10PortSecurityIfSecureMacAgeEnable"),
        ("DELLEMC-OS10-PORT-SECURITY-MIB", "os10PortSecurityIfTotalSecureAddresses"),
        ("DELLEMC-OS10-PORT-SECURITY-MIB", "os10PortSecurityIfTotalSecureDynamicAddresses"),
        ("DELLEMC-OS10-PORT-SECURITY-MIB", "os10PortSecurityIfTotalSecureStickyAddresses"),
        ("DELLEMC-OS10-PORT-SECURITY-MIB", "os10PortSecurityIfTotalSecureStaticAddresses"),
        ("DELLEMC-OS10-PORT-SECURITY-MIB", "os10PortSecurityIfClearSecureMacAddresses"))
)
if mibBuilder.loadTexts:
    os10PortSecurityInterfaceGroup.setStatus("current")

os10PortSecuritySecureMacAddrGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 100, 5, 2, 2, 3)
)
os10PortSecuritySecureMacAddrGroup.setObjects(
      *(("DELLEMC-OS10-PORT-SECURITY-MIB", "os10PortSecuritySecureMacIfIndex"),
        ("DELLEMC-OS10-PORT-SECURITY-MIB", "os10PortSecuritySecureMacAddrType"))
)
if mibBuilder.loadTexts:
    os10PortSecuritySecureMacAddrGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

os10PortSecurityMibConform = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 674, 11000, 5000, 100, 5, 2, 1, 1)
)
os10PortSecurityMibConform.setObjects(
      *(("DELLEMC-OS10-PORT-SECURITY-MIB", "os10PortSecurityGlobalGroup"),
        ("DELLEMC-OS10-PORT-SECURITY-MIB", "os10PortSecurityInterfaceGroup"),
        ("DELLEMC-OS10-PORT-SECURITY-MIB", "os10PortSecuritySecureMacAddrGroup"))
)
if mibBuilder.loadTexts:
    os10PortSecurityMibConform.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DELLEMC-OS10-PORT-SECURITY-MIB",
    **{"SecureMacAddrType": SecureMacAddrType,
       "SecureMacViolationType": SecureMacViolationType,
       "os10PortSecurityMib": os10PortSecurityMib,
       "os10PortSecurityMibObjects": os10PortSecurityMibObjects,
       "os10PortSecurityGlobalObjects": os10PortSecurityGlobalObjects,
       "os10PortSecurityGlobalEnable": os10PortSecurityGlobalEnable,
       "os10PortSecurityGlobalTotalSecureAddresses": os10PortSecurityGlobalTotalSecureAddresses,
       "os10PortSecurityGlobalTotalSecureDynamicAddresses": os10PortSecurityGlobalTotalSecureDynamicAddresses,
       "os10PortSecurityGlobalTotalSecureStickyAddresses": os10PortSecurityGlobalTotalSecureStickyAddresses,
       "os10PortSecurityGlobalTotalSecureStaticAddresses": os10PortSecurityGlobalTotalSecureStaticAddresses,
       "os10PortSecurityGlobalClearSecureMacAddresses": os10PortSecurityGlobalClearSecureMacAddresses,
       "os10PortSecurityGlobalResetViolation": os10PortSecurityGlobalResetViolation,
       "os10PortSecurityInterfaceObjects": os10PortSecurityInterfaceObjects,
       "os10PortSecurityIfConfigTable": os10PortSecurityIfConfigTable,
       "os10PortSecurityIfConfigEntry": os10PortSecurityIfConfigEntry,
       "os10PortSecurityIfIndex": os10PortSecurityIfIndex,
       "os10PortSecurityIfPortSecurityEnable": os10PortSecurityIfPortSecurityEnable,
       "os10PortSecurityIfViolationStatus": os10PortSecurityIfViolationStatus,
       "os10PortSecurityIfSecureMacLearnLimit": os10PortSecurityIfSecureMacLearnLimit,
       "os10PortSecurityIfStationMoveEnable": os10PortSecurityIfStationMoveEnable,
       "os10PortSecurityIfMacViolationAction": os10PortSecurityIfMacViolationAction,
       "os10PortSecurityIfStmvViolationAction": os10PortSecurityIfStmvViolationAction,
       "os10PortSecurityIfStickyEnable": os10PortSecurityIfStickyEnable,
       "os10PortSecurityIfClearSecureMacAddresses": os10PortSecurityIfClearSecureMacAddresses,
       "os10PortSecurityIfSecureMacAgeEnable": os10PortSecurityIfSecureMacAgeEnable,
       "os10PortSecurityIfTotalSecureAddresses": os10PortSecurityIfTotalSecureAddresses,
       "os10PortSecurityIfTotalSecureDynamicAddresses": os10PortSecurityIfTotalSecureDynamicAddresses,
       "os10PortSecurityIfTotalSecureStickyAddresses": os10PortSecurityIfTotalSecureStickyAddresses,
       "os10PortSecurityIfTotalSecureStaticAddresses": os10PortSecurityIfTotalSecureStaticAddresses,
       "os10PortSecurityMacObjects": os10PortSecurityMacObjects,
       "os10PortSecuritySecureMacAddrTable": os10PortSecuritySecureMacAddrTable,
       "os10PortSecuritySecureMacAddrEntry": os10PortSecuritySecureMacAddrEntry,
       "os10PortSecuritySecureMacVlanId": os10PortSecuritySecureMacVlanId,
       "os10PortSecuritySecureMacAddress": os10PortSecuritySecureMacAddress,
       "os10PortSecuritySecureMacIfIndex": os10PortSecuritySecureMacIfIndex,
       "os10PortSecuritySecureMacAddrType": os10PortSecuritySecureMacAddrType,
       "os10PortSecurityMibConformance": os10PortSecurityMibConformance,
       "os10PortSecurityCompliances": os10PortSecurityCompliances,
       "os10PortSecurityMibConform": os10PortSecurityMibConform,
       "os10PortSecurityGroups": os10PortSecurityGroups,
       "os10PortSecurityGlobalGroup": os10PortSecurityGlobalGroup,
       "os10PortSecurityInterfaceGroup": os10PortSecurityInterfaceGroup,
       "os10PortSecuritySecureMacAddrGroup": os10PortSecuritySecureMacAddrGroup}
)
