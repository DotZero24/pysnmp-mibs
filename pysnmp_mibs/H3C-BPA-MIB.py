# SNMP MIB module (H3C-BPA-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/h3c/H3C-BPA-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:17:34 2025
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

(h3cCommon,) = mibBuilder.importSymbols(
    "HUAWEI-3COM-OID-MIB",
    "h3cCommon")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(InetAddressType,) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
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
 PhysAddress,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

h3cBpa = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 144)
)
if mibBuilder.loadTexts:
    h3cBpa.setRevisions(
        ("2014-11-20 09:27",
         "2013-11-13 11:28")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_H3cBpaObjects_ObjectIdentity = ObjectIdentity
h3cBpaObjects = _H3cBpaObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 144, 1)
)
_H3cBpaCfgTable_Object = MibTable
h3cBpaCfgTable = _H3cBpaCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 144, 1, 1)
)
if mibBuilder.loadTexts:
    h3cBpaCfgTable.setStatus("current")
_H3cBpaCfgEntry_Object = MibTableRow
h3cBpaCfgEntry = _H3cBpaCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 144, 1, 1, 1)
)
h3cBpaCfgEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "H3C-BPA-MIB", "h3cBpaDirection"),
)
if mibBuilder.loadTexts:
    h3cBpaCfgEntry.setStatus("current")


class _H3cBpaDirection_Type(Integer32):
    """Custom type h3cBpaDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("input", 1),
          ("output", 2))
    )


_H3cBpaDirection_Type.__name__ = "Integer32"
_H3cBpaDirection_Object = MibTableColumn
h3cBpaDirection = _H3cBpaDirection_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 144, 1, 1, 1, 1),
    _H3cBpaDirection_Type()
)
h3cBpaDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cBpaDirection.setStatus("current")


class _H3cBpaSrcOrDest_Type(Integer32):
    """Custom type h3cBpaSrcOrDest based on Integer32"""
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
        *(("source", 1),
          ("destination", 2),
          ("both", 3))
    )


_H3cBpaSrcOrDest_Type.__name__ = "Integer32"
_H3cBpaSrcOrDest_Object = MibTableColumn
h3cBpaSrcOrDest = _H3cBpaSrcOrDest_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 144, 1, 1, 1, 2),
    _H3cBpaSrcOrDest_Type()
)
h3cBpaSrcOrDest.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cBpaSrcOrDest.setStatus("current")
_H3cBpaRowStatus_Type = RowStatus
_H3cBpaRowStatus_Object = MibTableColumn
h3cBpaRowStatus = _H3cBpaRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 144, 1, 1, 1, 3),
    _H3cBpaRowStatus_Type()
)
h3cBpaRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cBpaRowStatus.setStatus("current")
_H3cBpaStatTable_Object = MibTable
h3cBpaStatTable = _H3cBpaStatTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 144, 1, 2)
)
if mibBuilder.loadTexts:
    h3cBpaStatTable.setStatus("current")
_H3cBpaStatEntry_Object = MibTableRow
h3cBpaStatEntry = _H3cBpaStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 144, 1, 2, 1)
)
h3cBpaStatEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "H3C-BPA-MIB", "h3cBpaTrafficType"),
    (0, "H3C-BPA-MIB", "h3cBpaTrafficIndex"),
)
if mibBuilder.loadTexts:
    h3cBpaStatEntry.setStatus("current")
_H3cBpaTrafficType_Type = InetAddressType
_H3cBpaTrafficType_Object = MibTableColumn
h3cBpaTrafficType = _H3cBpaTrafficType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 144, 1, 2, 1, 1),
    _H3cBpaTrafficType_Type()
)
h3cBpaTrafficType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cBpaTrafficType.setStatus("current")


class _H3cBpaTrafficIndex_Type(Integer32):
    """Custom type h3cBpaTrafficIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_H3cBpaTrafficIndex_Type.__name__ = "Integer32"
_H3cBpaTrafficIndex_Object = MibTableColumn
h3cBpaTrafficIndex = _H3cBpaTrafficIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 144, 1, 2, 1, 2),
    _H3cBpaTrafficIndex_Type()
)
h3cBpaTrafficIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cBpaTrafficIndex.setStatus("current")
_H3cBpaInPacketCount_Type = Counter64
_H3cBpaInPacketCount_Object = MibTableColumn
h3cBpaInPacketCount = _H3cBpaInPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 144, 1, 2, 1, 3),
    _H3cBpaInPacketCount_Type()
)
h3cBpaInPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cBpaInPacketCount.setStatus("current")
_H3cBpaInOctetCount_Type = Counter64
_H3cBpaInOctetCount_Object = MibTableColumn
h3cBpaInOctetCount = _H3cBpaInOctetCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 144, 1, 2, 1, 4),
    _H3cBpaInOctetCount_Type()
)
h3cBpaInOctetCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cBpaInOctetCount.setStatus("current")
_H3cBpaOutPacketCount_Type = Counter64
_H3cBpaOutPacketCount_Object = MibTableColumn
h3cBpaOutPacketCount = _H3cBpaOutPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 144, 1, 2, 1, 5),
    _H3cBpaOutPacketCount_Type()
)
h3cBpaOutPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cBpaOutPacketCount.setStatus("current")
_H3cBpaOutOctetCount_Type = Counter64
_H3cBpaOutOctetCount_Object = MibTableColumn
h3cBpaOutOctetCount = _H3cBpaOutOctetCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 144, 1, 2, 1, 6),
    _H3cBpaOutOctetCount_Type()
)
h3cBpaOutOctetCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cBpaOutOctetCount.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "H3C-BPA-MIB",
    **{"h3cBpa": h3cBpa,
       "h3cBpaObjects": h3cBpaObjects,
       "h3cBpaCfgTable": h3cBpaCfgTable,
       "h3cBpaCfgEntry": h3cBpaCfgEntry,
       "h3cBpaDirection": h3cBpaDirection,
       "h3cBpaSrcOrDest": h3cBpaSrcOrDest,
       "h3cBpaRowStatus": h3cBpaRowStatus,
       "h3cBpaStatTable": h3cBpaStatTable,
       "h3cBpaStatEntry": h3cBpaStatEntry,
       "h3cBpaTrafficType": h3cBpaTrafficType,
       "h3cBpaTrafficIndex": h3cBpaTrafficIndex,
       "h3cBpaInPacketCount": h3cBpaInPacketCount,
       "h3cBpaInOctetCount": h3cBpaInOctetCount,
       "h3cBpaOutPacketCount": h3cBpaOutPacketCount,
       "h3cBpaOutOctetCount": h3cBpaOutOctetCount}
)
