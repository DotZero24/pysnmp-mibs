# SNMP MIB module (DELL-NETWORKING-PORT-SECURITY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/dell/DELL-NETWORKING-PORT-SECURITY-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:09:19 2025
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

(dellNetMgmt,) = mibBuilder.importSymbols(
    "DELL-NETWORKING-SMI",
    "dellNetMgmt")

(InterfaceIndex,
 ifIndex,
 ifName) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex",
    "ifName")

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


# MODULE-IDENTITY

dellNetPortSecurityMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 31)
)
if mibBuilder.loadTexts:
    dellNetPortSecurityMib.setRevisions(
        ("2018-07-16 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class ClearSecureMacAddrType(TextualConvention, Integer32):
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
          ("dynamic", 1),
          ("sticky", 2))
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

_DellNetPortSecurityMibObjects_ObjectIdentity = ObjectIdentity
dellNetPortSecurityMibObjects = _DellNetPortSecurityMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 31, 1)
)
_DellNetPortSecGlobalObjects_ObjectIdentity = ObjectIdentity
dellNetPortSecGlobalObjects = _DellNetPortSecGlobalObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 31, 1, 1)
)


class _DellNetGlobalPortSecurityMode_Type(Integer32):
    """Custom type dellNetGlobalPortSecurityMode based on Integer32"""
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


_DellNetGlobalPortSecurityMode_Type.__name__ = "Integer32"
_DellNetGlobalPortSecurityMode_Object = MibScalar
dellNetGlobalPortSecurityMode = _DellNetGlobalPortSecurityMode_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 31, 1, 1, 1),
    _DellNetGlobalPortSecurityMode_Type()
)
dellNetGlobalPortSecurityMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dellNetGlobalPortSecurityMode.setStatus("current")


class _DellNetGlobalTotalSecureAddress_Type(Integer32):
    """Custom type dellNetGlobalTotalSecureAddress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_DellNetGlobalTotalSecureAddress_Type.__name__ = "Integer32"
_DellNetGlobalTotalSecureAddress_Object = MibScalar
dellNetGlobalTotalSecureAddress = _DellNetGlobalTotalSecureAddress_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 31, 1, 1, 2),
    _DellNetGlobalTotalSecureAddress_Type()
)
dellNetGlobalTotalSecureAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetGlobalTotalSecureAddress.setStatus("current")
_DellNetGlobalClearSecureMacAddresses_Type = ClearSecureMacAddrType
_DellNetGlobalClearSecureMacAddresses_Object = MibScalar
dellNetGlobalClearSecureMacAddresses = _DellNetGlobalClearSecureMacAddresses_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 31, 1, 1, 3),
    _DellNetGlobalClearSecureMacAddresses_Type()
)
dellNetGlobalClearSecureMacAddresses.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dellNetGlobalClearSecureMacAddresses.setStatus("current")
_DellNetGlobalResetViolationStatus_Type = SecureMacViolationType
_DellNetGlobalResetViolationStatus_Object = MibScalar
dellNetGlobalResetViolationStatus = _DellNetGlobalResetViolationStatus_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 31, 1, 1, 4),
    _DellNetGlobalResetViolationStatus_Type()
)
dellNetGlobalResetViolationStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dellNetGlobalResetViolationStatus.setStatus("current")
_DellNetPortSecInterfaceObjects_ObjectIdentity = ObjectIdentity
dellNetPortSecInterfaceObjects = _DellNetPortSecInterfaceObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 31, 1, 2)
)
_DellNetPortSecIfConfigTable_Object = MibTable
dellNetPortSecIfConfigTable = _DellNetPortSecIfConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 31, 1, 2, 1)
)
if mibBuilder.loadTexts:
    dellNetPortSecIfConfigTable.setStatus("current")
_DellNetPortSecIfConfigEntry_Object = MibTableRow
dellNetPortSecIfConfigEntry = _DellNetPortSecIfConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 31, 1, 2, 1, 1)
)
dellNetPortSecIfConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dellNetPortSecIfConfigEntry.setStatus("current")
_DellNetPortSecIfPortSecurityEnable_Type = TruthValue
_DellNetPortSecIfPortSecurityEnable_Object = MibTableColumn
dellNetPortSecIfPortSecurityEnable = _DellNetPortSecIfPortSecurityEnable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 31, 1, 2, 1, 1, 1),
    _DellNetPortSecIfPortSecurityEnable_Type()
)
dellNetPortSecIfPortSecurityEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetPortSecIfPortSecurityEnable.setStatus("current")


class _DellNetPortSecIfPortSecurityStatus_Type(Integer32):
    """Custom type dellNetPortSecIfPortSecurityStatus based on Integer32"""
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
          ("dynMacLimitErrDisable", 2),
          ("stationMoveErrDisable", 3))
    )


_DellNetPortSecIfPortSecurityStatus_Type.__name__ = "Integer32"
_DellNetPortSecIfPortSecurityStatus_Object = MibTableColumn
dellNetPortSecIfPortSecurityStatus = _DellNetPortSecIfPortSecurityStatus_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 31, 1, 2, 1, 1, 2),
    _DellNetPortSecIfPortSecurityStatus_Type()
)
dellNetPortSecIfPortSecurityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetPortSecIfPortSecurityStatus.setStatus("current")


class _DellNetPortSecIfSecureMacLimit_Type(Integer32):
    """Custom type dellNetPortSecIfSecureMacLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_DellNetPortSecIfSecureMacLimit_Type.__name__ = "Integer32"
_DellNetPortSecIfSecureMacLimit_Object = MibTableColumn
dellNetPortSecIfSecureMacLimit = _DellNetPortSecIfSecureMacLimit_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 31, 1, 2, 1, 1, 3),
    _DellNetPortSecIfSecureMacLimit_Type()
)
dellNetPortSecIfSecureMacLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dellNetPortSecIfSecureMacLimit.setStatus("current")


class _DellNetPortSecIfCurrentMacCount_Type(Integer32):
    """Custom type dellNetPortSecIfCurrentMacCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_DellNetPortSecIfCurrentMacCount_Type.__name__ = "Integer32"
_DellNetPortSecIfCurrentMacCount_Object = MibTableColumn
dellNetPortSecIfCurrentMacCount = _DellNetPortSecIfCurrentMacCount_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 31, 1, 2, 1, 1, 4),
    _DellNetPortSecIfCurrentMacCount_Type()
)
dellNetPortSecIfCurrentMacCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetPortSecIfCurrentMacCount.setStatus("current")


class _DellNetPortSecIfStationMoveEnable_Type(TruthValue):
    """Custom type dellNetPortSecIfStationMoveEnable based on TruthValue"""
    defaultValue = 2


_DellNetPortSecIfStationMoveEnable_Type.__name__ = "TruthValue"
_DellNetPortSecIfStationMoveEnable_Object = MibTableColumn
dellNetPortSecIfStationMoveEnable = _DellNetPortSecIfStationMoveEnable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 31, 1, 2, 1, 1, 5),
    _DellNetPortSecIfStationMoveEnable_Type()
)
dellNetPortSecIfStationMoveEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dellNetPortSecIfStationMoveEnable.setStatus("current")


class _DellNetPortSecIfSecureMacViolationAction_Type(Integer32):
    """Custom type dellNetPortSecIfSecureMacViolationAction based on Integer32"""
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
        *(("none", 1),
          ("notify", 2),
          ("shutdown", 3))
    )


_DellNetPortSecIfSecureMacViolationAction_Type.__name__ = "Integer32"
_DellNetPortSecIfSecureMacViolationAction_Object = MibTableColumn
dellNetPortSecIfSecureMacViolationAction = _DellNetPortSecIfSecureMacViolationAction_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 31, 1, 2, 1, 1, 6),
    _DellNetPortSecIfSecureMacViolationAction_Type()
)
dellNetPortSecIfSecureMacViolationAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dellNetPortSecIfSecureMacViolationAction.setStatus("current")


class _DellNetPortSecIfStmvViolationAction_Type(Integer32):
    """Custom type dellNetPortSecIfStmvViolationAction based on Integer32"""
    defaultValue = 1

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
        *(("none", 1),
          ("notify", 2),
          ("shutdownOrigPort", 3),
          ("shutDownOffendingPort", 4),
          ("shutdownBoth", 5))
    )


_DellNetPortSecIfStmvViolationAction_Type.__name__ = "Integer32"
_DellNetPortSecIfStmvViolationAction_Object = MibTableColumn
dellNetPortSecIfStmvViolationAction = _DellNetPortSecIfStmvViolationAction_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 31, 1, 2, 1, 1, 7),
    _DellNetPortSecIfStmvViolationAction_Type()
)
dellNetPortSecIfStmvViolationAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dellNetPortSecIfStmvViolationAction.setStatus("current")


class _DellNetPortSecIfStickyEnable_Type(TruthValue):
    """Custom type dellNetPortSecIfStickyEnable based on TruthValue"""
    defaultValue = 2


_DellNetPortSecIfStickyEnable_Type.__name__ = "TruthValue"
_DellNetPortSecIfStickyEnable_Object = MibTableColumn
dellNetPortSecIfStickyEnable = _DellNetPortSecIfStickyEnable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 31, 1, 2, 1, 1, 8),
    _DellNetPortSecIfStickyEnable_Type()
)
dellNetPortSecIfStickyEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dellNetPortSecIfStickyEnable.setStatus("current")


class _DellNetPortSecIfClearSecureMacAddresses_Type(ClearSecureMacAddrType):
    """Custom type dellNetPortSecIfClearSecureMacAddresses based on ClearSecureMacAddrType"""
    defaultValue = 0


_DellNetPortSecIfClearSecureMacAddresses_Type.__name__ = "ClearSecureMacAddrType"
_DellNetPortSecIfClearSecureMacAddresses_Object = MibTableColumn
dellNetPortSecIfClearSecureMacAddresses = _DellNetPortSecIfClearSecureMacAddresses_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 31, 1, 2, 1, 1, 9),
    _DellNetPortSecIfClearSecureMacAddresses_Type()
)
dellNetPortSecIfClearSecureMacAddresses.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dellNetPortSecIfClearSecureMacAddresses.setStatus("current")


class _DellNetPortSecIfResetViolationStatus_Type(SecureMacViolationType):
    """Custom type dellNetPortSecIfResetViolationStatus based on SecureMacViolationType"""
    defaultValue = 0


_DellNetPortSecIfResetViolationStatus_Type.__name__ = "SecureMacViolationType"
_DellNetPortSecIfResetViolationStatus_Object = MibTableColumn
dellNetPortSecIfResetViolationStatus = _DellNetPortSecIfResetViolationStatus_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 31, 1, 2, 1, 1, 10),
    _DellNetPortSecIfResetViolationStatus_Type()
)
dellNetPortSecIfResetViolationStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dellNetPortSecIfResetViolationStatus.setStatus("current")


class _DellNetPortSecIfSecureMacAgeEnable_Type(TruthValue):
    """Custom type dellNetPortSecIfSecureMacAgeEnable based on TruthValue"""
    defaultValue = 2


_DellNetPortSecIfSecureMacAgeEnable_Type.__name__ = "TruthValue"
_DellNetPortSecIfSecureMacAgeEnable_Object = MibTableColumn
dellNetPortSecIfSecureMacAgeEnable = _DellNetPortSecIfSecureMacAgeEnable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 31, 1, 2, 1, 1, 11),
    _DellNetPortSecIfSecureMacAgeEnable_Type()
)
dellNetPortSecIfSecureMacAgeEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dellNetPortSecIfSecureMacAgeEnable.setStatus("current")
_DellNetPortSecSecureStaticMacAddrTable_Object = MibTable
dellNetPortSecSecureStaticMacAddrTable = _DellNetPortSecSecureStaticMacAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 31, 1, 2, 2)
)
if mibBuilder.loadTexts:
    dellNetPortSecSecureStaticMacAddrTable.setStatus("current")
_DellNetPortSecIfSecureStaticMacAddrEntry_Object = MibTableRow
dellNetPortSecIfSecureStaticMacAddrEntry = _DellNetPortSecIfSecureStaticMacAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 31, 1, 2, 2, 1)
)
dellNetPortSecIfSecureStaticMacAddrEntry.setIndexNames(
    (0, "DELL-NETWORKING-PORT-SECURITY-MIB", "dellNetPortSecIfSecureStaticMacAddress"),
    (0, "DELL-NETWORKING-PORT-SECURITY-MIB", "dellNetPortSecIfSecureStaticMacVlanId"),
    (0, "DELL-NETWORKING-PORT-SECURITY-MIB", "dellNetPortSecIfSecureStaticMacIfIndex"),
)
if mibBuilder.loadTexts:
    dellNetPortSecIfSecureStaticMacAddrEntry.setStatus("current")
_DellNetPortSecIfSecureStaticMacAddress_Type = MacAddress
_DellNetPortSecIfSecureStaticMacAddress_Object = MibTableColumn
dellNetPortSecIfSecureStaticMacAddress = _DellNetPortSecIfSecureStaticMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 31, 1, 2, 2, 1, 1),
    _DellNetPortSecIfSecureStaticMacAddress_Type()
)
dellNetPortSecIfSecureStaticMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dellNetPortSecIfSecureStaticMacAddress.setStatus("current")
_DellNetPortSecIfSecureStaticMacVlanId_Type = VlanIndex
_DellNetPortSecIfSecureStaticMacVlanId_Object = MibTableColumn
dellNetPortSecIfSecureStaticMacVlanId = _DellNetPortSecIfSecureStaticMacVlanId_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 31, 1, 2, 2, 1, 2),
    _DellNetPortSecIfSecureStaticMacVlanId_Type()
)
dellNetPortSecIfSecureStaticMacVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dellNetPortSecIfSecureStaticMacVlanId.setStatus("current")
_DellNetPortSecIfSecureStaticMacIfIndex_Type = InterfaceIndex
_DellNetPortSecIfSecureStaticMacIfIndex_Object = MibTableColumn
dellNetPortSecIfSecureStaticMacIfIndex = _DellNetPortSecIfSecureStaticMacIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 31, 1, 2, 2, 1, 3),
    _DellNetPortSecIfSecureStaticMacIfIndex_Type()
)
dellNetPortSecIfSecureStaticMacIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dellNetPortSecIfSecureStaticMacIfIndex.setStatus("current")
_DellNetPortSecIfSecureStaticMacRowStatus_Type = RowStatus
_DellNetPortSecIfSecureStaticMacRowStatus_Object = MibTableColumn
dellNetPortSecIfSecureStaticMacRowStatus = _DellNetPortSecIfSecureStaticMacRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 31, 1, 2, 2, 1, 4),
    _DellNetPortSecIfSecureStaticMacRowStatus_Type()
)
dellNetPortSecIfSecureStaticMacRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dellNetPortSecIfSecureStaticMacRowStatus.setStatus("current")
_DellNetPortSecMacObjects_ObjectIdentity = ObjectIdentity
dellNetPortSecMacObjects = _DellNetPortSecMacObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 31, 1, 3)
)
_DellNetPortSecSecureMacAddrTable_Object = MibTable
dellNetPortSecSecureMacAddrTable = _DellNetPortSecSecureMacAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 31, 1, 3, 1)
)
if mibBuilder.loadTexts:
    dellNetPortSecSecureMacAddrTable.setStatus("current")
_DellNetSecureMacAddrEntry_Object = MibTableRow
dellNetSecureMacAddrEntry = _DellNetSecureMacAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 31, 1, 3, 1, 1)
)
dellNetSecureMacAddrEntry.setIndexNames(
    (0, "DELL-NETWORKING-PORT-SECURITY-MIB", "dellNetSecureMacAddress"),
    (0, "DELL-NETWORKING-PORT-SECURITY-MIB", "dellNetSecureMacVlanId"),
)
if mibBuilder.loadTexts:
    dellNetSecureMacAddrEntry.setStatus("current")
_DellNetSecureMacAddress_Type = MacAddress
_DellNetSecureMacAddress_Object = MibTableColumn
dellNetSecureMacAddress = _DellNetSecureMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 31, 1, 3, 1, 1, 1),
    _DellNetSecureMacAddress_Type()
)
dellNetSecureMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dellNetSecureMacAddress.setStatus("current")
_DellNetSecureMacVlanId_Type = VlanIndex
_DellNetSecureMacVlanId_Object = MibTableColumn
dellNetSecureMacVlanId = _DellNetSecureMacVlanId_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 31, 1, 3, 1, 1, 2),
    _DellNetSecureMacVlanId_Type()
)
dellNetSecureMacVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetSecureMacVlanId.setStatus("current")
_DellNetSecureMacIfIndex_Type = InterfaceIndex
_DellNetSecureMacIfIndex_Object = MibTableColumn
dellNetSecureMacIfIndex = _DellNetSecureMacIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 31, 1, 3, 1, 1, 3),
    _DellNetSecureMacIfIndex_Type()
)
dellNetSecureMacIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetSecureMacIfIndex.setStatus("current")


class _DellNetSecureMacAddrType_Type(Integer32):
    """Custom type dellNetSecureMacAddrType based on Integer32"""
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


_DellNetSecureMacAddrType_Type.__name__ = "Integer32"
_DellNetSecureMacAddrType_Object = MibTableColumn
dellNetSecureMacAddrType = _DellNetSecureMacAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 31, 1, 3, 1, 1, 4),
    _DellNetSecureMacAddrType_Type()
)
dellNetSecureMacAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetSecureMacAddrType.setStatus("current")
_DellNetPortSecurityMibConformance_ObjectIdentity = ObjectIdentity
dellNetPortSecurityMibConformance = _DellNetPortSecurityMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 31, 2)
)
_DellNtPortSecurityCompliances_ObjectIdentity = ObjectIdentity
dellNtPortSecurityCompliances = _DellNtPortSecurityCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 31, 2, 1)
)
_DellNetPortSecurityGroups_ObjectIdentity = ObjectIdentity
dellNetPortSecurityGroups = _DellNetPortSecurityGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 31, 2, 2)
)

# Managed Objects groups

dellNetPortSecGlobalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6027, 3, 31, 2, 2, 1)
)
dellNetPortSecGlobalGroup.setObjects(
      *(("DELL-NETWORKING-PORT-SECURITY-MIB", "dellNetGlobalPortSecurityMode"),
        ("DELL-NETWORKING-PORT-SECURITY-MIB", "dellNetGlobalTotalSecureAddress"),
        ("DELL-NETWORKING-PORT-SECURITY-MIB", "dellNetGlobalClearSecureMacAddresses"),
        ("DELL-NETWORKING-PORT-SECURITY-MIB", "dellNetPortSecIfResetViolationStatus"))
)
if mibBuilder.loadTexts:
    dellNetPortSecGlobalGroup.setStatus("current")

dellNetPortSecInterfaceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6027, 3, 31, 2, 2, 2)
)
dellNetPortSecInterfaceGroup.setObjects(
      *(("DELL-NETWORKING-PORT-SECURITY-MIB", "dellNetPortSecIfPortSecurityEnable"),
        ("DELL-NETWORKING-PORT-SECURITY-MIB", "dellNetPortSecIfPortSecurityStatus"),
        ("DELL-NETWORKING-PORT-SECURITY-MIB", "dellNetPortSecIfSecureMacLimit"),
        ("DELL-NETWORKING-PORT-SECURITY-MIB", "dellNetPortSecIfCurrentMacCount"),
        ("DELL-NETWORKING-PORT-SECURITY-MIB", "dellNetPortSecIfStationMoveEnable"),
        ("DELL-NETWORKING-PORT-SECURITY-MIB", "dellNetPortSecIfSecureMacViolationAction"),
        ("DELL-NETWORKING-PORT-SECURITY-MIB", "dellNetPortSecIfStmvViolationAction"),
        ("DELL-NETWORKING-PORT-SECURITY-MIB", "dellNetPortSecIfStickyEnable"),
        ("DELL-NETWORKING-PORT-SECURITY-MIB", "dellNetPortSecIfClearSecureMacAddresses"),
        ("DELL-NETWORKING-PORT-SECURITY-MIB", "dellNetPortSecIfResetViolationStatus"),
        ("DELL-NETWORKING-PORT-SECURITY-MIB", "dellNetPortSecIfSecureMacAgeEnable"))
)
if mibBuilder.loadTexts:
    dellNetPortSecInterfaceGroup.setStatus("current")

dellNetPortSecIfSecureStaticMacAddrGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6027, 3, 31, 2, 2, 3)
)
dellNetPortSecIfSecureStaticMacAddrGroup.setObjects(
    ("DELL-NETWORKING-PORT-SECURITY-MIB", "dellNetPortSecIfSecureStaticMacRowStatus")
)
if mibBuilder.loadTexts:
    dellNetPortSecIfSecureStaticMacAddrGroup.setStatus("current")

dellNetSecureMacAddrGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6027, 3, 31, 2, 2, 4)
)
dellNetSecureMacAddrGroup.setObjects(
      *(("DELL-NETWORKING-PORT-SECURITY-MIB", "dellNetSecureMacVlanId"),
        ("DELL-NETWORKING-PORT-SECURITY-MIB", "dellNetSecureMacIfIndex"),
        ("DELL-NETWORKING-PORT-SECURITY-MIB", "dellNetSecureMacAddrType"))
)
if mibBuilder.loadTexts:
    dellNetSecureMacAddrGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

dellNetPortSecurityMibConform = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6027, 3, 31, 2, 1, 1)
)
dellNetPortSecurityMibConform.setObjects(
      *(("DELL-NETWORKING-PORT-SECURITY-MIB", "dellNetPortSecGlobalGroup"),
        ("DELL-NETWORKING-PORT-SECURITY-MIB", "dellNetPortSecInterfaceGroup"),
        ("DELL-NETWORKING-PORT-SECURITY-MIB", "dellNetPortSecIfSecureStaticMacAddrGroup"),
        ("DELL-NETWORKING-PORT-SECURITY-MIB", "dellNetSecureMacAddrGroup"))
)
if mibBuilder.loadTexts:
    dellNetPortSecurityMibConform.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DELL-NETWORKING-PORT-SECURITY-MIB",
    **{"ClearSecureMacAddrType": ClearSecureMacAddrType,
       "SecureMacViolationType": SecureMacViolationType,
       "dellNetPortSecurityMib": dellNetPortSecurityMib,
       "dellNetPortSecurityMibObjects": dellNetPortSecurityMibObjects,
       "dellNetPortSecGlobalObjects": dellNetPortSecGlobalObjects,
       "dellNetGlobalPortSecurityMode": dellNetGlobalPortSecurityMode,
       "dellNetGlobalTotalSecureAddress": dellNetGlobalTotalSecureAddress,
       "dellNetGlobalClearSecureMacAddresses": dellNetGlobalClearSecureMacAddresses,
       "dellNetGlobalResetViolationStatus": dellNetGlobalResetViolationStatus,
       "dellNetPortSecInterfaceObjects": dellNetPortSecInterfaceObjects,
       "dellNetPortSecIfConfigTable": dellNetPortSecIfConfigTable,
       "dellNetPortSecIfConfigEntry": dellNetPortSecIfConfigEntry,
       "dellNetPortSecIfPortSecurityEnable": dellNetPortSecIfPortSecurityEnable,
       "dellNetPortSecIfPortSecurityStatus": dellNetPortSecIfPortSecurityStatus,
       "dellNetPortSecIfSecureMacLimit": dellNetPortSecIfSecureMacLimit,
       "dellNetPortSecIfCurrentMacCount": dellNetPortSecIfCurrentMacCount,
       "dellNetPortSecIfStationMoveEnable": dellNetPortSecIfStationMoveEnable,
       "dellNetPortSecIfSecureMacViolationAction": dellNetPortSecIfSecureMacViolationAction,
       "dellNetPortSecIfStmvViolationAction": dellNetPortSecIfStmvViolationAction,
       "dellNetPortSecIfStickyEnable": dellNetPortSecIfStickyEnable,
       "dellNetPortSecIfClearSecureMacAddresses": dellNetPortSecIfClearSecureMacAddresses,
       "dellNetPortSecIfResetViolationStatus": dellNetPortSecIfResetViolationStatus,
       "dellNetPortSecIfSecureMacAgeEnable": dellNetPortSecIfSecureMacAgeEnable,
       "dellNetPortSecSecureStaticMacAddrTable": dellNetPortSecSecureStaticMacAddrTable,
       "dellNetPortSecIfSecureStaticMacAddrEntry": dellNetPortSecIfSecureStaticMacAddrEntry,
       "dellNetPortSecIfSecureStaticMacAddress": dellNetPortSecIfSecureStaticMacAddress,
       "dellNetPortSecIfSecureStaticMacVlanId": dellNetPortSecIfSecureStaticMacVlanId,
       "dellNetPortSecIfSecureStaticMacIfIndex": dellNetPortSecIfSecureStaticMacIfIndex,
       "dellNetPortSecIfSecureStaticMacRowStatus": dellNetPortSecIfSecureStaticMacRowStatus,
       "dellNetPortSecMacObjects": dellNetPortSecMacObjects,
       "dellNetPortSecSecureMacAddrTable": dellNetPortSecSecureMacAddrTable,
       "dellNetSecureMacAddrEntry": dellNetSecureMacAddrEntry,
       "dellNetSecureMacAddress": dellNetSecureMacAddress,
       "dellNetSecureMacVlanId": dellNetSecureMacVlanId,
       "dellNetSecureMacIfIndex": dellNetSecureMacIfIndex,
       "dellNetSecureMacAddrType": dellNetSecureMacAddrType,
       "dellNetPortSecurityMibConformance": dellNetPortSecurityMibConformance,
       "dellNtPortSecurityCompliances": dellNtPortSecurityCompliances,
       "dellNetPortSecurityMibConform": dellNetPortSecurityMibConform,
       "dellNetPortSecurityGroups": dellNetPortSecurityGroups,
       "dellNetPortSecGlobalGroup": dellNetPortSecGlobalGroup,
       "dellNetPortSecInterfaceGroup": dellNetPortSecInterfaceGroup,
       "dellNetPortSecIfSecureStaticMacAddrGroup": dellNetPortSecIfSecureStaticMacAddrGroup,
       "dellNetSecureMacAddrGroup": dellNetSecureMacAddrGroup}
)
