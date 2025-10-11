# SNMP MIB module (SAMSUNG-HOST-RESOURCES-EXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/samsung/SAMSUNG-HOST-RESOURCES-EXT-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:12:41 2025
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

(hrDeviceIndex,) = mibBuilder.importSymbols(
    "HOST-RESOURCES-MIB",
    "hrDeviceIndex")

(samsungCommonMIB,) = mibBuilder.importSymbols(
    "SAMSUNG-COMMON-MIB",
    "samsungCommonMIB")

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


# MODULE-IDENTITY

scmHrMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 53)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class ScmHrDevCountJobTypeTC(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              11,
              12,
              21)
        )
    )
    namedValues = NamedValues(
        *(("print", 1),
          ("copy", 2),
          ("faxIn", 3),
          ("faxOut", 4),
          ("scan", 5),
          ("report", 6),
          ("digitalSend", 11),
          ("digitalRecieve", 12),
          ("localStorage", 21))
    )



class ScmHrDevCountMediaSizeTC(TextualConvention, Integer32):
    status = "current"
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
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32)
        )
    )
    namedValues = NamedValues(
        *(("small", 1),
          ("large", 2),
          ("letter", 3),
          ("legal", 4),
          ("a4", 5),
          ("executive", 6),
          ("jisB5", 7),
          ("isoB5", 8),
          ("com10", 9),
          ("monarch", 10),
          ("dl", 11),
          ("c5", 12),
          ("postA6", 13),
          ("c6", 14),
          ("folio", 15),
          ("a5", 16),
          ("statement", 17),
          ("a6", 18),
          ("ledger", 19),
          ("a3", 20),
          ("jisB4", 21),
          ("jpost", 22),
          ("jpostd", 23),
          ("custom", 24),
          ("letterP", 25),
          ("a4P", 26),
          ("jisB5P", 27),
          ("a5P", 28),
          ("executiveP", 29),
          ("statementP", 30),
          ("a3Over", 31),
          ("b5Envelope", 32))
    )



class ScmHrDevCountUnitTC(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              7,
              8,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("unknown", 2),
          ("tenThousandthsOfInches", 3),
          ("micrometers", 4),
          ("impressions", 7),
          ("sheets", 8),
          ("hours", 11),
          ("thousandthsOfOunces", 12),
          ("tenthsOfGrams", 13),
          ("hundrethsOfFluidOunces", 14),
          ("tenthsOfMilliliters", 15),
          ("feet", 16),
          ("meters", 17),
          ("items", 18),
          ("percent", 19))
    )



class ScmHrDevCountDuplexTC(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("simplex", 1),
          ("duplex", 2),
          ("duplexSingle", 3))
    )



class ScmHrDevCountColorTC(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fullColor", 1),
          ("singleColor", 2),
          ("monoColor", 3))
    )



# MIB Managed Objects in the order of their OIDs

_ScmHrMIBConformance_ObjectIdentity = ObjectIdentity
scmHrMIBConformance = _ScmHrMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 53, 2)
)
_ScmHrMIBGroups_ObjectIdentity = ObjectIdentity
scmHrMIBGroups = _ScmHrMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 53, 2, 2)
)
_ScmHrDevCount_ObjectIdentity = ObjectIdentity
scmHrDevCount = _ScmHrDevCount_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 53, 11)
)
_ScmHrDevCountSimple_ObjectIdentity = ObjectIdentity
scmHrDevCountSimple = _ScmHrDevCountSimple_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 53, 11, 1)
)
_ScmHrDevCountTable_Object = MibTable
scmHrDevCountTable = _ScmHrDevCountTable_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 53, 11, 2)
)
if mibBuilder.loadTexts:
    scmHrDevCountTable.setStatus("current")
_ScmHrDevCountEntry_Object = MibTableRow
scmHrDevCountEntry = _ScmHrDevCountEntry_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 53, 11, 2, 1)
)
scmHrDevCountEntry.setIndexNames(
    (0, "HOST-RESOURCES-MIB", "hrDeviceIndex"),
    (0, "SAMSUNG-HOST-RESOURCES-EXT-MIB", "scmHrDevCountIndex"),
)
if mibBuilder.loadTexts:
    scmHrDevCountEntry.setStatus("current")


class _ScmHrDevCountIndex_Type(Integer32):
    """Custom type scmHrDevCountIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32767),
    )


_ScmHrDevCountIndex_Type.__name__ = "Integer32"
_ScmHrDevCountIndex_Object = MibTableColumn
scmHrDevCountIndex = _ScmHrDevCountIndex_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 53, 11, 2, 1, 1),
    _ScmHrDevCountIndex_Type()
)
scmHrDevCountIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmHrDevCountIndex.setStatus("current")
_ScmHrDevCountJobType_Type = ScmHrDevCountJobTypeTC
_ScmHrDevCountJobType_Object = MibTableColumn
scmHrDevCountJobType = _ScmHrDevCountJobType_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 53, 11, 2, 1, 2),
    _ScmHrDevCountJobType_Type()
)
scmHrDevCountJobType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmHrDevCountJobType.setStatus("current")
_ScmHrDevCountMediaSize_Type = ScmHrDevCountMediaSizeTC
_ScmHrDevCountMediaSize_Object = MibTableColumn
scmHrDevCountMediaSize = _ScmHrDevCountMediaSize_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 53, 11, 2, 1, 3),
    _ScmHrDevCountMediaSize_Type()
)
scmHrDevCountMediaSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmHrDevCountMediaSize.setStatus("current")
_ScmHrDevCountUnit_Type = ScmHrDevCountUnitTC
_ScmHrDevCountUnit_Object = MibTableColumn
scmHrDevCountUnit = _ScmHrDevCountUnit_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 53, 11, 2, 1, 4),
    _ScmHrDevCountUnit_Type()
)
scmHrDevCountUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmHrDevCountUnit.setStatus("current")
_ScmHrDevCountDuplex_Type = ScmHrDevCountDuplexTC
_ScmHrDevCountDuplex_Object = MibTableColumn
scmHrDevCountDuplex = _ScmHrDevCountDuplex_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 53, 11, 2, 1, 5),
    _ScmHrDevCountDuplex_Type()
)
scmHrDevCountDuplex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmHrDevCountDuplex.setStatus("current")
_ScmHrDevCountColor_Type = ScmHrDevCountColorTC
_ScmHrDevCountColor_Object = MibTableColumn
scmHrDevCountColor = _ScmHrDevCountColor_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 53, 11, 2, 1, 6),
    _ScmHrDevCountColor_Type()
)
scmHrDevCountColor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmHrDevCountColor.setStatus("current")
_ScmHrDevCountValue_Type = Counter32
_ScmHrDevCountValue_Object = MibTableColumn
scmHrDevCountValue = _ScmHrDevCountValue_Object(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 53, 11, 2, 1, 7),
    _ScmHrDevCountValue_Type()
)
scmHrDevCountValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scmHrDevCountValue.setStatus("current")

# Managed Objects groups

scmHrDevInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 53, 2, 2, 3)
)
scmHrDevInfoGroup.setObjects(
      *(("SAMSUNG-HOST-RESOURCES-EXT-MIB", "scmHrDevCountIndex"),
        ("SAMSUNG-HOST-RESOURCES-EXT-MIB", "scmHrDevCountJobType"),
        ("SAMSUNG-HOST-RESOURCES-EXT-MIB", "scmHrDevCountMediaSize"),
        ("SAMSUNG-HOST-RESOURCES-EXT-MIB", "scmHrDevCountUnit"),
        ("SAMSUNG-HOST-RESOURCES-EXT-MIB", "scmHrDevCountDuplex"),
        ("SAMSUNG-HOST-RESOURCES-EXT-MIB", "scmHrDevCountColor"),
        ("SAMSUNG-HOST-RESOURCES-EXT-MIB", "scmHrDevCountValue"))
)
if mibBuilder.loadTexts:
    scmHrDevInfoGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SAMSUNG-HOST-RESOURCES-EXT-MIB",
    **{"ScmHrDevCountJobTypeTC": ScmHrDevCountJobTypeTC,
       "ScmHrDevCountMediaSizeTC": ScmHrDevCountMediaSizeTC,
       "ScmHrDevCountUnitTC": ScmHrDevCountUnitTC,
       "ScmHrDevCountDuplexTC": ScmHrDevCountDuplexTC,
       "ScmHrDevCountColorTC": ScmHrDevCountColorTC,
       "scmHrMIB": scmHrMIB,
       "scmHrMIBConformance": scmHrMIBConformance,
       "scmHrMIBGroups": scmHrMIBGroups,
       "scmHrDevInfoGroup": scmHrDevInfoGroup,
       "scmHrDevCount": scmHrDevCount,
       "scmHrDevCountSimple": scmHrDevCountSimple,
       "scmHrDevCountTable": scmHrDevCountTable,
       "scmHrDevCountEntry": scmHrDevCountEntry,
       "scmHrDevCountIndex": scmHrDevCountIndex,
       "scmHrDevCountJobType": scmHrDevCountJobType,
       "scmHrDevCountMediaSize": scmHrDevCountMediaSize,
       "scmHrDevCountUnit": scmHrDevCountUnit,
       "scmHrDevCountDuplex": scmHrDevCountDuplex,
       "scmHrDevCountColor": scmHrDevCountColor,
       "scmHrDevCountValue": scmHrDevCountValue}
)
