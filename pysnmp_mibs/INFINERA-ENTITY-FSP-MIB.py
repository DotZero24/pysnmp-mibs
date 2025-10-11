# SNMP MIB module (INFINERA-ENTITY-FSP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/INFINERA-ENTITY-FSP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:14:59 2025
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

(entLPPhysicalIndex,) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "entLPPhysicalIndex")

(equipment,) = mibBuilder.importSymbols(
    "INFINERA-REG-MIB",
    "equipment")

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

fspMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 35)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FspTable_Object = MibTable
fspTable = _FspTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 35, 1)
)
if mibBuilder.loadTexts:
    fspTable.setStatus("current")
_FspEntry_Object = MibTableRow
fspEntry = _FspEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 35, 1, 1)
)
fspEntry.setIndexNames(
    (0, "ENTITY-MIB", "entLPPhysicalIndex"),
)
if mibBuilder.loadTexts:
    fspEntry.setStatus("current")


class _FspType_Type(Integer32):
    """Custom type fspType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(7805,
              7806,
              7807,
              7808)
        )
    )
    namedValues = NamedValues(
        *(("fspE9D18MPO", 7805),
          ("fspS4D8MPO", 7806),
          ("fspC1D1MPO", 7807),
          ("fmpC8fourLcMPO", 7808))
    )


_FspType_Type.__name__ = "Integer32"
_FspType_Object = MibTableColumn
fspType = _FspType_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 35, 1, 1, 1),
    _FspType_Type()
)
fspType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fspType.setStatus("current")
_FspProvSerialNumber_Type = DisplayString
_FspProvSerialNumber_Object = MibTableColumn
fspProvSerialNumber = _FspProvSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 35, 1, 1, 2),
    _FspProvSerialNumber_Type()
)
fspProvSerialNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fspProvSerialNumber.setStatus("current")
_FspLabel_Type = DisplayString
_FspLabel_Object = MibTableColumn
fspLabel = _FspLabel_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 35, 1, 1, 3),
    _FspLabel_Type()
)
fspLabel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fspLabel.setStatus("current")
_FspAid_Type = DisplayString
_FspAid_Object = MibTableColumn
fspAid = _FspAid_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 35, 1, 1, 4),
    _FspAid_Type()
)
fspAid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fspAid.setStatus("current")
_FspConformance_ObjectIdentity = ObjectIdentity
fspConformance = _FspConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 35, 3)
)
_FspCompliances_ObjectIdentity = ObjectIdentity
fspCompliances = _FspCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 35, 3, 1)
)
_FspGroups_ObjectIdentity = ObjectIdentity
fspGroups = _FspGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 35, 3, 2)
)

# Managed Objects groups

fspGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 35, 3, 2, 1)
)
fspGroup.setObjects(
      *(("INFINERA-ENTITY-FSP-MIB", "fspType"),
        ("INFINERA-ENTITY-FSP-MIB", "fspProvSerialNumber"),
        ("INFINERA-ENTITY-FSP-MIB", "fspLabel"),
        ("INFINERA-ENTITY-FSP-MIB", "fspAid"))
)
if mibBuilder.loadTexts:
    fspGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

fspCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 35, 3, 1, 1)
)
fspCompliance.setObjects(
    ("INFINERA-ENTITY-FSP-MIB", "fspGroup")
)
if mibBuilder.loadTexts:
    fspCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INFINERA-ENTITY-FSP-MIB",
    **{"fspMIB": fspMIB,
       "fspTable": fspTable,
       "fspEntry": fspEntry,
       "fspType": fspType,
       "fspProvSerialNumber": fspProvSerialNumber,
       "fspLabel": fspLabel,
       "fspAid": fspAid,
       "fspConformance": fspConformance,
       "fspCompliances": fspCompliances,
       "fspCompliance": fspCompliance,
       "fspGroups": fspGroups,
       "fspGroup": fspGroup}
)
