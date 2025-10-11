# SNMP MIB module (ZTE-DSL-LINE-TEST-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/zte/ZTE-DSL-LINE-TEST-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:43:56 2025
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

zxDslLineTestMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 29)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ZxDslLineTestMibObjects_ObjectIdentity = ObjectIdentity
zxDslLineTestMibObjects = _ZxDslLineTestMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 29, 1)
)


class _ZxDslLineTestUnitType_Type(Integer32):
    """Custom type zxDslLineTestUnitType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("tam", 1),
          ("ltc", 2))
    )


_ZxDslLineTestUnitType_Type.__name__ = "Integer32"
_ZxDslLineTestUnitType_Object = MibScalar
zxDslLineTestUnitType = _ZxDslLineTestUnitType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 29, 1, 5),
    _ZxDslLineTestUnitType_Type()
)
zxDslLineTestUnitType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxDslLineTestUnitType.setStatus("current")
_ZxDslLineTestTam_ObjectIdentity = ObjectIdentity
zxDslLineTestTam = _ZxDslLineTestTam_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 29, 1, 10)
)
_ZxDslLineTestTamIp_Type = IpAddress
_ZxDslLineTestTamIp_Object = MibScalar
zxDslLineTestTamIp = _ZxDslLineTestTamIp_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 29, 1, 10, 1),
    _ZxDslLineTestTamIp_Type()
)
zxDslLineTestTamIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxDslLineTestTamIp.setStatus("current")
_ZxDslLineTestTamIpMask_Type = IpAddress
_ZxDslLineTestTamIpMask_Object = MibScalar
zxDslLineTestTamIpMask = _ZxDslLineTestTamIpMask_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 29, 1, 10, 2),
    _ZxDslLineTestTamIpMask_Type()
)
zxDslLineTestTamIpMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxDslLineTestTamIpMask.setStatus("current")
_ZxDslLineTestServerTable_Object = MibTable
zxDslLineTestServerTable = _ZxDslLineTestServerTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 29, 1, 50)
)
if mibBuilder.loadTexts:
    zxDslLineTestServerTable.setStatus("current")
_ZxDslLineTestServerEntry_Object = MibTableRow
zxDslLineTestServerEntry = _ZxDslLineTestServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 29, 1, 50, 1)
)
zxDslLineTestServerEntry.setIndexNames(
    (0, "ZTE-DSL-LINE-TEST-MIB", "zxDslLineTestServerIndex"),
)
if mibBuilder.loadTexts:
    zxDslLineTestServerEntry.setStatus("current")


class _ZxDslLineTestServerIndex_Type(Integer32):
    """Custom type zxDslLineTestServerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_ZxDslLineTestServerIndex_Type.__name__ = "Integer32"
_ZxDslLineTestServerIndex_Object = MibTableColumn
zxDslLineTestServerIndex = _ZxDslLineTestServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 29, 1, 50, 1, 1),
    _ZxDslLineTestServerIndex_Type()
)
zxDslLineTestServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxDslLineTestServerIndex.setStatus("current")
_ZxDslLineTestServerIp_Type = IpAddress
_ZxDslLineTestServerIp_Object = MibTableColumn
zxDslLineTestServerIp = _ZxDslLineTestServerIp_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 29, 1, 50, 1, 2),
    _ZxDslLineTestServerIp_Type()
)
zxDslLineTestServerIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxDslLineTestServerIp.setStatus("current")


class _ZxDslLineTestServerNatMode_Type(Integer32):
    """Custom type zxDslLineTestServerNatMode based on Integer32"""
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
        *(("noNAT", 1),
          ("inBandNAT", 2),
          ("outBandNAT", 3),
          ("bridging_in_out_band", 4))
    )


_ZxDslLineTestServerNatMode_Type.__name__ = "Integer32"
_ZxDslLineTestServerNatMode_Object = MibTableColumn
zxDslLineTestServerNatMode = _ZxDslLineTestServerNatMode_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 29, 1, 50, 1, 3),
    _ZxDslLineTestServerNatMode_Type()
)
zxDslLineTestServerNatMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxDslLineTestServerNatMode.setStatus("current")
_ZxDslLineTestServerRowStatus_Type = RowStatus
_ZxDslLineTestServerRowStatus_Object = MibTableColumn
zxDslLineTestServerRowStatus = _ZxDslLineTestServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 29, 1, 50, 1, 4),
    _ZxDslLineTestServerRowStatus_Type()
)
zxDslLineTestServerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxDslLineTestServerRowStatus.setStatus("current")
_ZxDslLineTestTrapObjects_ObjectIdentity = ObjectIdentity
zxDslLineTestTrapObjects = _ZxDslLineTestTrapObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 29, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZTE-DSL-LINE-TEST-MIB",
    **{"zxDslLineTestMib": zxDslLineTestMib,
       "zxDslLineTestMibObjects": zxDslLineTestMibObjects,
       "zxDslLineTestUnitType": zxDslLineTestUnitType,
       "zxDslLineTestTam": zxDslLineTestTam,
       "zxDslLineTestTamIp": zxDslLineTestTamIp,
       "zxDslLineTestTamIpMask": zxDslLineTestTamIpMask,
       "zxDslLineTestServerTable": zxDslLineTestServerTable,
       "zxDslLineTestServerEntry": zxDslLineTestServerEntry,
       "zxDslLineTestServerIndex": zxDslLineTestServerIndex,
       "zxDslLineTestServerIp": zxDslLineTestServerIp,
       "zxDslLineTestServerNatMode": zxDslLineTestServerNatMode,
       "zxDslLineTestServerRowStatus": zxDslLineTestServerRowStatus,
       "zxDslLineTestTrapObjects": zxDslLineTestTrapObjects}
)
