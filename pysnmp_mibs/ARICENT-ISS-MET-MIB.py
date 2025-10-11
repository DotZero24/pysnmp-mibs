# SNMP MIB module (ARICENT-ISS-MET-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/aricent/ARICENT-ISS-MET-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:43:21 2025
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

(issL2FilterEntry,
 issL3FilterEntry) = mibBuilder.importSymbols(
    "ARICENT-ISS-MIB",
    "issL2FilterEntry",
    "issL3FilterEntry")

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

issMet = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 81, 8, 4)
)
if mibBuilder.loadTexts:
    issMet.setRevisions(
        ("2012-09-05 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_IssMetroL2Filter_ObjectIdentity = ObjectIdentity
issMetroL2Filter = _IssMetroL2Filter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 81, 8, 4, 1)
)
_IssMetroL2FilterTable_Object = MibTable
issMetroL2FilterTable = _IssMetroL2FilterTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 8, 4, 1, 1)
)
if mibBuilder.loadTexts:
    issMetroL2FilterTable.setStatus("current")
_IssMetroL2FilterEntry_Object = MibTableRow
issMetroL2FilterEntry = _IssMetroL2FilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 8, 4, 1, 1, 1)
)
if mibBuilder.loadTexts:
    issMetroL2FilterEntry.setStatus("current")


class _IssMetroL2FilterOuterEtherType_Type(Integer32):
    """Custom type issMetroL2FilterOuterEtherType based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IssMetroL2FilterOuterEtherType_Type.__name__ = "Integer32"
_IssMetroL2FilterOuterEtherType_Object = MibTableColumn
issMetroL2FilterOuterEtherType = _IssMetroL2FilterOuterEtherType_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 8, 4, 1, 1, 1, 1),
    _IssMetroL2FilterOuterEtherType_Type()
)
issMetroL2FilterOuterEtherType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issMetroL2FilterOuterEtherType.setStatus("current")


class _IssMetroL2FilterSVlanId_Type(Integer32):
    """Custom type issMetroL2FilterSVlanId based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_IssMetroL2FilterSVlanId_Type.__name__ = "Integer32"
_IssMetroL2FilterSVlanId_Object = MibTableColumn
issMetroL2FilterSVlanId = _IssMetroL2FilterSVlanId_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 8, 4, 1, 1, 1, 2),
    _IssMetroL2FilterSVlanId_Type()
)
issMetroL2FilterSVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issMetroL2FilterSVlanId.setStatus("current")


class _IssMetroL2FilterSVlanPriority_Type(Integer32):
    """Custom type issMetroL2FilterSVlanPriority based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 7),
    )


_IssMetroL2FilterSVlanPriority_Type.__name__ = "Integer32"
_IssMetroL2FilterSVlanPriority_Object = MibTableColumn
issMetroL2FilterSVlanPriority = _IssMetroL2FilterSVlanPriority_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 8, 4, 1, 1, 1, 3),
    _IssMetroL2FilterSVlanPriority_Type()
)
issMetroL2FilterSVlanPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issMetroL2FilterSVlanPriority.setStatus("current")


class _IssMetroL2FilterCVlanPriority_Type(Integer32):
    """Custom type issMetroL2FilterCVlanPriority based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 7),
    )


_IssMetroL2FilterCVlanPriority_Type.__name__ = "Integer32"
_IssMetroL2FilterCVlanPriority_Object = MibTableColumn
issMetroL2FilterCVlanPriority = _IssMetroL2FilterCVlanPriority_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 8, 4, 1, 1, 1, 4),
    _IssMetroL2FilterCVlanPriority_Type()
)
issMetroL2FilterCVlanPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issMetroL2FilterCVlanPriority.setStatus("current")


class _IssMetroL2FilterPacketTagType_Type(Integer32):
    """Custom type issMetroL2FilterPacketTagType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("singleTag", 1),
          ("doubleTag", 2))
    )


_IssMetroL2FilterPacketTagType_Type.__name__ = "Integer32"
_IssMetroL2FilterPacketTagType_Object = MibTableColumn
issMetroL2FilterPacketTagType = _IssMetroL2FilterPacketTagType_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 8, 4, 1, 1, 1, 5),
    _IssMetroL2FilterPacketTagType_Type()
)
issMetroL2FilterPacketTagType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issMetroL2FilterPacketTagType.setStatus("current")
_IssMetroL3Filter_ObjectIdentity = ObjectIdentity
issMetroL3Filter = _IssMetroL3Filter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 81, 8, 4, 2)
)
_IssMetroL3FilterTable_Object = MibTable
issMetroL3FilterTable = _IssMetroL3FilterTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 8, 4, 2, 1)
)
if mibBuilder.loadTexts:
    issMetroL3FilterTable.setStatus("current")
_IssMetroL3FilterEntry_Object = MibTableRow
issMetroL3FilterEntry = _IssMetroL3FilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 8, 4, 2, 1, 1)
)
if mibBuilder.loadTexts:
    issMetroL3FilterEntry.setStatus("current")


class _IssMetroL3FilterSVlanId_Type(Integer32):
    """Custom type issMetroL3FilterSVlanId based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_IssMetroL3FilterSVlanId_Type.__name__ = "Integer32"
_IssMetroL3FilterSVlanId_Object = MibTableColumn
issMetroL3FilterSVlanId = _IssMetroL3FilterSVlanId_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 8, 4, 2, 1, 1, 1),
    _IssMetroL3FilterSVlanId_Type()
)
issMetroL3FilterSVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issMetroL3FilterSVlanId.setStatus("current")


class _IssMetroL3FilterSVlanPriority_Type(Integer32):
    """Custom type issMetroL3FilterSVlanPriority based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 7),
    )


_IssMetroL3FilterSVlanPriority_Type.__name__ = "Integer32"
_IssMetroL3FilterSVlanPriority_Object = MibTableColumn
issMetroL3FilterSVlanPriority = _IssMetroL3FilterSVlanPriority_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 8, 4, 2, 1, 1, 2),
    _IssMetroL3FilterSVlanPriority_Type()
)
issMetroL3FilterSVlanPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issMetroL3FilterSVlanPriority.setStatus("current")


class _IssMetroL3FilterCVlanId_Type(Integer32):
    """Custom type issMetroL3FilterCVlanId based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_IssMetroL3FilterCVlanId_Type.__name__ = "Integer32"
_IssMetroL3FilterCVlanId_Object = MibTableColumn
issMetroL3FilterCVlanId = _IssMetroL3FilterCVlanId_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 8, 4, 2, 1, 1, 3),
    _IssMetroL3FilterCVlanId_Type()
)
issMetroL3FilterCVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issMetroL3FilterCVlanId.setStatus("current")


class _IssMetroL3FilterCVlanPriority_Type(Integer32):
    """Custom type issMetroL3FilterCVlanPriority based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 7),
    )


_IssMetroL3FilterCVlanPriority_Type.__name__ = "Integer32"
_IssMetroL3FilterCVlanPriority_Object = MibTableColumn
issMetroL3FilterCVlanPriority = _IssMetroL3FilterCVlanPriority_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 8, 4, 2, 1, 1, 4),
    _IssMetroL3FilterCVlanPriority_Type()
)
issMetroL3FilterCVlanPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issMetroL3FilterCVlanPriority.setStatus("current")


class _IssMetroL3FilterPacketTagType_Type(Integer32):
    """Custom type issMetroL3FilterPacketTagType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("singleTag", 1),
          ("doubleTag", 2))
    )


_IssMetroL3FilterPacketTagType_Type.__name__ = "Integer32"
_IssMetroL3FilterPacketTagType_Object = MibTableColumn
issMetroL3FilterPacketTagType = _IssMetroL3FilterPacketTagType_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 8, 4, 2, 1, 1, 5),
    _IssMetroL3FilterPacketTagType_Type()
)
issMetroL3FilterPacketTagType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    issMetroL3FilterPacketTagType.setStatus("current")
issL2FilterEntry.registerAugmentions(
    ("ARICENT-ISS-MET-MIB",
     "issMetroL2FilterEntry")
)
issMetroL2FilterEntry.setIndexNames(*issL2FilterEntry.getIndexNames())
issL3FilterEntry.registerAugmentions(
    ("ARICENT-ISS-MET-MIB",
     "issMetroL3FilterEntry")
)
issMetroL3FilterEntry.setIndexNames(*issL3FilterEntry.getIndexNames())

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ARICENT-ISS-MET-MIB",
    **{"issMet": issMet,
       "issMetroL2Filter": issMetroL2Filter,
       "issMetroL2FilterTable": issMetroL2FilterTable,
       "issMetroL2FilterEntry": issMetroL2FilterEntry,
       "issMetroL2FilterOuterEtherType": issMetroL2FilterOuterEtherType,
       "issMetroL2FilterSVlanId": issMetroL2FilterSVlanId,
       "issMetroL2FilterSVlanPriority": issMetroL2FilterSVlanPriority,
       "issMetroL2FilterCVlanPriority": issMetroL2FilterCVlanPriority,
       "issMetroL2FilterPacketTagType": issMetroL2FilterPacketTagType,
       "issMetroL3Filter": issMetroL3Filter,
       "issMetroL3FilterTable": issMetroL3FilterTable,
       "issMetroL3FilterEntry": issMetroL3FilterEntry,
       "issMetroL3FilterSVlanId": issMetroL3FilterSVlanId,
       "issMetroL3FilterSVlanPriority": issMetroL3FilterSVlanPriority,
       "issMetroL3FilterCVlanId": issMetroL3FilterCVlanId,
       "issMetroL3FilterCVlanPriority": issMetroL3FilterCVlanPriority,
       "issMetroL3FilterPacketTagType": issMetroL3FilterPacketTagType}
)
