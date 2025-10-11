# SNMP MIB module (H3C-TRNG2-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/h3c/H3C-TRNG2-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:18:58 2025
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

(DateAndTime,
 DisplayString,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

h3cTRNG2 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 121)
)
if mibBuilder.loadTexts:
    h3cTRNG2.setRevisions(
        ("2013-03-08 00:00",
         "2012-05-14 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_H3cTRNG2MibObjects_ObjectIdentity = ObjectIdentity
h3cTRNG2MibObjects = _H3cTRNG2MibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 121, 1)
)
_H3cTrangeCreateTimerangeTable_Object = MibTable
h3cTrangeCreateTimerangeTable = _H3cTrangeCreateTimerangeTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 121, 1, 1)
)
if mibBuilder.loadTexts:
    h3cTrangeCreateTimerangeTable.setStatus("current")
_H3cTrangeCreateTimerangeEntry_Object = MibTableRow
h3cTrangeCreateTimerangeEntry = _H3cTrangeCreateTimerangeEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 121, 1, 1, 1)
)
h3cTrangeCreateTimerangeEntry.setIndexNames(
    (0, "H3C-TRNG2-MIB", "h3cTrangeIndex"),
)
if mibBuilder.loadTexts:
    h3cTrangeCreateTimerangeEntry.setStatus("current")


class _H3cTrangeIndex_Type(Integer32):
    """Custom type h3cTrangeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_H3cTrangeIndex_Type.__name__ = "Integer32"
_H3cTrangeIndex_Object = MibTableColumn
h3cTrangeIndex = _H3cTrangeIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 121, 1, 1, 1, 1),
    _H3cTrangeIndex_Type()
)
h3cTrangeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cTrangeIndex.setStatus("current")


class _H3cTrangeName_Type(OctetString):
    """Custom type h3cTrangeName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_H3cTrangeName_Type.__name__ = "OctetString"
_H3cTrangeName_Object = MibTableColumn
h3cTrangeName = _H3cTrangeName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 121, 1, 1, 1, 2),
    _H3cTrangeName_Type()
)
h3cTrangeName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cTrangeName.setStatus("current")
_H3cTrangeValidFlag_Type = TruthValue
_H3cTrangeValidFlag_Object = MibTableColumn
h3cTrangeValidFlag = _H3cTrangeValidFlag_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 121, 1, 1, 1, 3),
    _H3cTrangeValidFlag_Type()
)
h3cTrangeValidFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cTrangeValidFlag.setStatus("current")
_H3cTrangeCreateRowStatus_Type = RowStatus
_H3cTrangeCreateRowStatus_Object = MibTableColumn
h3cTrangeCreateRowStatus = _H3cTrangeCreateRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 121, 1, 1, 1, 4),
    _H3cTrangeCreateRowStatus_Type()
)
h3cTrangeCreateRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cTrangeCreateRowStatus.setStatus("current")
_H3cTrangeAbsoluteTable_Object = MibTable
h3cTrangeAbsoluteTable = _H3cTrangeAbsoluteTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 121, 1, 2)
)
if mibBuilder.loadTexts:
    h3cTrangeAbsoluteTable.setStatus("current")
_H3cTrangeAbsoluteEntry_Object = MibTableRow
h3cTrangeAbsoluteEntry = _H3cTrangeAbsoluteEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 121, 1, 2, 1)
)
h3cTrangeAbsoluteEntry.setIndexNames(
    (0, "H3C-TRNG2-MIB", "h3cTrangeAbsoluteNameIndex"),
    (0, "H3C-TRNG2-MIB", "h3cTrangeAbsoluteSubIndex"),
)
if mibBuilder.loadTexts:
    h3cTrangeAbsoluteEntry.setStatus("current")


class _H3cTrangeAbsoluteNameIndex_Type(Integer32):
    """Custom type h3cTrangeAbsoluteNameIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_H3cTrangeAbsoluteNameIndex_Type.__name__ = "Integer32"
_H3cTrangeAbsoluteNameIndex_Object = MibTableColumn
h3cTrangeAbsoluteNameIndex = _H3cTrangeAbsoluteNameIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 121, 1, 2, 1, 1),
    _H3cTrangeAbsoluteNameIndex_Type()
)
h3cTrangeAbsoluteNameIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cTrangeAbsoluteNameIndex.setStatus("current")


class _H3cTrangeAbsoluteSubIndex_Type(Integer32):
    """Custom type h3cTrangeAbsoluteSubIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_H3cTrangeAbsoluteSubIndex_Type.__name__ = "Integer32"
_H3cTrangeAbsoluteSubIndex_Object = MibTableColumn
h3cTrangeAbsoluteSubIndex = _H3cTrangeAbsoluteSubIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 121, 1, 2, 1, 2),
    _H3cTrangeAbsoluteSubIndex_Type()
)
h3cTrangeAbsoluteSubIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cTrangeAbsoluteSubIndex.setStatus("current")
_H3cTrangeAbsoluteStartTime_Type = DateAndTime
_H3cTrangeAbsoluteStartTime_Object = MibTableColumn
h3cTrangeAbsoluteStartTime = _H3cTrangeAbsoluteStartTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 121, 1, 2, 1, 3),
    _H3cTrangeAbsoluteStartTime_Type()
)
h3cTrangeAbsoluteStartTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cTrangeAbsoluteStartTime.setStatus("current")
_H3cTrangeAbsoluteEndTime_Type = DateAndTime
_H3cTrangeAbsoluteEndTime_Object = MibTableColumn
h3cTrangeAbsoluteEndTime = _H3cTrangeAbsoluteEndTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 121, 1, 2, 1, 4),
    _H3cTrangeAbsoluteEndTime_Type()
)
h3cTrangeAbsoluteEndTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cTrangeAbsoluteEndTime.setStatus("current")
_H3cTrangeAbsolueRowStatus_Type = RowStatus
_H3cTrangeAbsolueRowStatus_Object = MibTableColumn
h3cTrangeAbsolueRowStatus = _H3cTrangeAbsolueRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 121, 1, 2, 1, 5),
    _H3cTrangeAbsolueRowStatus_Type()
)
h3cTrangeAbsolueRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cTrangeAbsolueRowStatus.setStatus("current")
_H3cTrangePeriodicTable_Object = MibTable
h3cTrangePeriodicTable = _H3cTrangePeriodicTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 121, 1, 3)
)
if mibBuilder.loadTexts:
    h3cTrangePeriodicTable.setStatus("current")
_H3cTrangePeriodicEntry_Object = MibTableRow
h3cTrangePeriodicEntry = _H3cTrangePeriodicEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 121, 1, 3, 1)
)
h3cTrangePeriodicEntry.setIndexNames(
    (0, "H3C-TRNG2-MIB", "h3cTrangePeriodicNameIndex"),
    (0, "H3C-TRNG2-MIB", "h3cTrangePeriodicSubIndex"),
)
if mibBuilder.loadTexts:
    h3cTrangePeriodicEntry.setStatus("current")


class _H3cTrangePeriodicNameIndex_Type(Integer32):
    """Custom type h3cTrangePeriodicNameIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_H3cTrangePeriodicNameIndex_Type.__name__ = "Integer32"
_H3cTrangePeriodicNameIndex_Object = MibTableColumn
h3cTrangePeriodicNameIndex = _H3cTrangePeriodicNameIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 121, 1, 3, 1, 1),
    _H3cTrangePeriodicNameIndex_Type()
)
h3cTrangePeriodicNameIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cTrangePeriodicNameIndex.setStatus("current")


class _H3cTrangePeriodicSubIndex_Type(Integer32):
    """Custom type h3cTrangePeriodicSubIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_H3cTrangePeriodicSubIndex_Type.__name__ = "Integer32"
_H3cTrangePeriodicSubIndex_Object = MibTableColumn
h3cTrangePeriodicSubIndex = _H3cTrangePeriodicSubIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 121, 1, 3, 1, 2),
    _H3cTrangePeriodicSubIndex_Type()
)
h3cTrangePeriodicSubIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cTrangePeriodicSubIndex.setStatus("current")


class _H3cTrangePeriodicDayOfWeek_Type(Bits):
    """Custom type h3cTrangePeriodicDayOfWeek based on Bits"""
    namedValues = NamedValues(
        *(("sunday", 0),
          ("monday", 1),
          ("tuesday", 2),
          ("wednesday", 3),
          ("thursday", 4),
          ("friday", 5),
          ("saturday", 6))
    )

_H3cTrangePeriodicDayOfWeek_Type.__name__ = "Bits"
_H3cTrangePeriodicDayOfWeek_Object = MibTableColumn
h3cTrangePeriodicDayOfWeek = _H3cTrangePeriodicDayOfWeek_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 121, 1, 3, 1, 3),
    _H3cTrangePeriodicDayOfWeek_Type()
)
h3cTrangePeriodicDayOfWeek.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cTrangePeriodicDayOfWeek.setStatus("current")
_H3cTrangePeriodicStartTime_Type = DateAndTime
_H3cTrangePeriodicStartTime_Object = MibTableColumn
h3cTrangePeriodicStartTime = _H3cTrangePeriodicStartTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 121, 1, 3, 1, 4),
    _H3cTrangePeriodicStartTime_Type()
)
h3cTrangePeriodicStartTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cTrangePeriodicStartTime.setStatus("current")
_H3cTrangePeriodicEndTime_Type = DateAndTime
_H3cTrangePeriodicEndTime_Object = MibTableColumn
h3cTrangePeriodicEndTime = _H3cTrangePeriodicEndTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 121, 1, 3, 1, 5),
    _H3cTrangePeriodicEndTime_Type()
)
h3cTrangePeriodicEndTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cTrangePeriodicEndTime.setStatus("current")
_H3cTrangePeriodicRowStatus_Type = RowStatus
_H3cTrangePeriodicRowStatus_Object = MibTableColumn
h3cTrangePeriodicRowStatus = _H3cTrangePeriodicRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 121, 1, 3, 1, 6),
    _H3cTrangePeriodicRowStatus_Type()
)
h3cTrangePeriodicRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cTrangePeriodicRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "H3C-TRNG2-MIB",
    **{"h3cTRNG2": h3cTRNG2,
       "h3cTRNG2MibObjects": h3cTRNG2MibObjects,
       "h3cTrangeCreateTimerangeTable": h3cTrangeCreateTimerangeTable,
       "h3cTrangeCreateTimerangeEntry": h3cTrangeCreateTimerangeEntry,
       "h3cTrangeIndex": h3cTrangeIndex,
       "h3cTrangeName": h3cTrangeName,
       "h3cTrangeValidFlag": h3cTrangeValidFlag,
       "h3cTrangeCreateRowStatus": h3cTrangeCreateRowStatus,
       "h3cTrangeAbsoluteTable": h3cTrangeAbsoluteTable,
       "h3cTrangeAbsoluteEntry": h3cTrangeAbsoluteEntry,
       "h3cTrangeAbsoluteNameIndex": h3cTrangeAbsoluteNameIndex,
       "h3cTrangeAbsoluteSubIndex": h3cTrangeAbsoluteSubIndex,
       "h3cTrangeAbsoluteStartTime": h3cTrangeAbsoluteStartTime,
       "h3cTrangeAbsoluteEndTime": h3cTrangeAbsoluteEndTime,
       "h3cTrangeAbsolueRowStatus": h3cTrangeAbsolueRowStatus,
       "h3cTrangePeriodicTable": h3cTrangePeriodicTable,
       "h3cTrangePeriodicEntry": h3cTrangePeriodicEntry,
       "h3cTrangePeriodicNameIndex": h3cTrangePeriodicNameIndex,
       "h3cTrangePeriodicSubIndex": h3cTrangePeriodicSubIndex,
       "h3cTrangePeriodicDayOfWeek": h3cTrangePeriodicDayOfWeek,
       "h3cTrangePeriodicStartTime": h3cTrangePeriodicStartTime,
       "h3cTrangePeriodicEndTime": h3cTrangePeriodicEndTime,
       "h3cTrangePeriodicRowStatus": h3cTrangePeriodicRowStatus}
)
