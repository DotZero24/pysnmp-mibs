# SNMP MIB module (PDN-DS1EXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/paradyne/PDN-DS1EXT-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:00:39 2025
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

(ent_ds1,) = mibBuilder.importSymbols(
    "PDN-HEADER-MIB",
    "ent-ds1")

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

pdnDs1Ext = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 5, 5)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_PdnDs1ExtObjects_ObjectIdentity = ObjectIdentity
pdnDs1ExtObjects = _PdnDs1ExtObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 5, 5, 1)
)
_PdnDs1ExtConfTable_Object = MibTable
pdnDs1ExtConfTable = _PdnDs1ExtConfTable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 5, 5, 1, 1)
)
if mibBuilder.loadTexts:
    pdnDs1ExtConfTable.setStatus("current")
_PdnDs1ExtConfEntry_Object = MibTableRow
pdnDs1ExtConfEntry = _PdnDs1ExtConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 5, 5, 1, 1, 1)
)
pdnDs1ExtConfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    pdnDs1ExtConfEntry.setStatus("current")


class _PdnDs1ExtConfLineLengthType_Type(Integer32):
    """Custom type pdnDs1ExtConfLineLengthType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("shortHaul", 1),
          ("longHaul", 2))
    )


_PdnDs1ExtConfLineLengthType_Type.__name__ = "Integer32"
_PdnDs1ExtConfLineLengthType_Object = MibTableColumn
pdnDs1ExtConfLineLengthType = _PdnDs1ExtConfLineLengthType_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 5, 5, 1, 1, 1, 1),
    _PdnDs1ExtConfLineLengthType_Type()
)
pdnDs1ExtConfLineLengthType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdnDs1ExtConfLineLengthType.setStatus("current")


class _PdnDs1ExtConfLineLength_Type(Integer32):
    """Custom type pdnDs1ExtConfLineLength based on Integer32"""
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
        *(("feet000To133", 1),
          ("feet134To266", 2),
          ("feet267To399", 3),
          ("feet400To533", 4),
          ("feet534To655", 5))
    )


_PdnDs1ExtConfLineLength_Type.__name__ = "Integer32"
_PdnDs1ExtConfLineLength_Object = MibTableColumn
pdnDs1ExtConfLineLength = _PdnDs1ExtConfLineLength_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 5, 5, 1, 1, 1, 2),
    _PdnDs1ExtConfLineLength_Type()
)
pdnDs1ExtConfLineLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdnDs1ExtConfLineLength.setStatus("current")


class _PdnDs1ExtConfLineBuildOut_Type(Integer32):
    """Custom type pdnDs1ExtConfLineBuildOut based on Integer32"""
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
        *(("dB0Pnt0", 1),
          ("dB7Pnt5", 2),
          ("dB15Pnt0", 3),
          ("dB22Pnt5", 4))
    )


_PdnDs1ExtConfLineBuildOut_Type.__name__ = "Integer32"
_PdnDs1ExtConfLineBuildOut_Object = MibTableColumn
pdnDs1ExtConfLineBuildOut = _PdnDs1ExtConfLineBuildOut_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 5, 5, 1, 1, 1, 3),
    _PdnDs1ExtConfLineBuildOut_Type()
)
pdnDs1ExtConfLineBuildOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdnDs1ExtConfLineBuildOut.setStatus("current")


class _PdnDs1ExtConfConnector_Type(Integer32):
    """Custom type pdnDs1ExtConfConnector based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bnc", 1),
          ("rj48", 2))
    )


_PdnDs1ExtConfConnector_Type.__name__ = "Integer32"
_PdnDs1ExtConfConnector_Object = MibTableColumn
pdnDs1ExtConfConnector = _PdnDs1ExtConfConnector_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 5, 5, 1, 1, 1, 4),
    _PdnDs1ExtConfConnector_Type()
)
pdnDs1ExtConfConnector.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdnDs1ExtConfConnector.setStatus("current")
_PdnDs1ExtConformance_ObjectIdentity = ObjectIdentity
pdnDs1ExtConformance = _PdnDs1ExtConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 5, 5, 2)
)
_PdnDs1ExtGroups_ObjectIdentity = ObjectIdentity
pdnDs1ExtGroups = _PdnDs1ExtGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 5, 5, 2, 1)
)
_PdnDs1ExtCompliances_ObjectIdentity = ObjectIdentity
pdnDs1ExtCompliances = _PdnDs1ExtCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 5, 5, 2, 2)
)

# Managed Objects groups

pdnDs1ExtT1ConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 5, 5, 2, 1, 1)
)
pdnDs1ExtT1ConfigGroup.setObjects(
      *(("PDN-DS1EXT-MIB", "pdnDs1ExtConfLineLengthType"),
        ("PDN-DS1EXT-MIB", "pdnDs1ExtConfLineLength"),
        ("PDN-DS1EXT-MIB", "pdnDs1ExtConfLineBuildOut"))
)
if mibBuilder.loadTexts:
    pdnDs1ExtT1ConfigGroup.setStatus("current")

pdnDs1ExtE1ConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 5, 5, 2, 1, 2)
)
pdnDs1ExtE1ConfigGroup.setObjects(
      *(("PDN-DS1EXT-MIB", "pdnDs1ExtConfLineLengthType"),
        ("PDN-DS1EXT-MIB", "pdnDs1ExtConfConnector"))
)
if mibBuilder.loadTexts:
    pdnDs1ExtE1ConfigGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

pdnDs1ExtCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 5, 5, 2, 2, 1)
)
pdnDs1ExtCompliance.setObjects(
    ("PDN-DS1EXT-MIB", "pdnDs1ExtT1ConfigGroup")
)
if mibBuilder.loadTexts:
    pdnDs1ExtCompliance.setStatus(
        "current"
    )

pdnDs1ExtG703Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 5, 5, 2, 2, 2)
)
pdnDs1ExtG703Compliance.setObjects(
    ("PDN-DS1EXT-MIB", "pdnDs1ExtE1ConfigGroup")
)
if mibBuilder.loadTexts:
    pdnDs1ExtG703Compliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PDN-DS1EXT-MIB",
    **{"pdnDs1Ext": pdnDs1Ext,
       "pdnDs1ExtObjects": pdnDs1ExtObjects,
       "pdnDs1ExtConfTable": pdnDs1ExtConfTable,
       "pdnDs1ExtConfEntry": pdnDs1ExtConfEntry,
       "pdnDs1ExtConfLineLengthType": pdnDs1ExtConfLineLengthType,
       "pdnDs1ExtConfLineLength": pdnDs1ExtConfLineLength,
       "pdnDs1ExtConfLineBuildOut": pdnDs1ExtConfLineBuildOut,
       "pdnDs1ExtConfConnector": pdnDs1ExtConfConnector,
       "pdnDs1ExtConformance": pdnDs1ExtConformance,
       "pdnDs1ExtGroups": pdnDs1ExtGroups,
       "pdnDs1ExtT1ConfigGroup": pdnDs1ExtT1ConfigGroup,
       "pdnDs1ExtE1ConfigGroup": pdnDs1ExtE1ConfigGroup,
       "pdnDs1ExtCompliances": pdnDs1ExtCompliances,
       "pdnDs1ExtCompliance": pdnDs1ExtCompliance,
       "pdnDs1ExtG703Compliance": pdnDs1ExtG703Compliance}
)
