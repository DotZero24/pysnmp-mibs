# SNMP MIB module (HP-ICF-RELOAD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/hp/HP-ICF-RELOAD-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:41:47 2025
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

(entPhysicalIndex,) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "entPhysicalIndex")

(hpicfBasic,) = mibBuilder.importSymbols(
    "HP-ICF-BASIC",
    "hpicfBasic")

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

(DateAndTime,
 DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

hpicfReloadMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 4, 20)
)
if mibBuilder.loadTexts:
    hpicfReloadMIB.setRevisions(
        ("2009-12-03 00:00",
         "2009-10-01 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class ReloadControl(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("reloadSlotNone", 1),
          ("fullPowerCycleReload", 2))
    )



# MIB Managed Objects in the order of their OIDs

_HpicfReloadObjects_ObjectIdentity = ObjectIdentity
hpicfReloadObjects = _HpicfReloadObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 4, 20, 1)
)


class _HpicfReloadState_Type(Integer32):
    """Custom type hpicfReloadState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notScheduled", 1),
          ("reloadAfter", 2),
          ("reloadAt", 3))
    )


_HpicfReloadState_Type.__name__ = "Integer32"
_HpicfReloadState_Object = MibScalar
hpicfReloadState = _HpicfReloadState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 4, 20, 1, 1),
    _HpicfReloadState_Type()
)
hpicfReloadState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfReloadState.setStatus("current")
_HpicfReloadAfter_Type = Integer32
_HpicfReloadAfter_Object = MibScalar
hpicfReloadAfter = _HpicfReloadAfter_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 4, 20, 1, 2),
    _HpicfReloadAfter_Type()
)
hpicfReloadAfter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfReloadAfter.setStatus("current")
_HpicfReloadAt_Type = DateAndTime
_HpicfReloadAt_Object = MibScalar
hpicfReloadAt = _HpicfReloadAt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 4, 20, 1, 3),
    _HpicfReloadAt_Type()
)
hpicfReloadAt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfReloadAt.setStatus("current")
_HpicfEntityReload_ObjectIdentity = ObjectIdentity
hpicfEntityReload = _HpicfEntityReload_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 4, 20, 2)
)
_HpicfReloadTable_Object = MibTable
hpicfReloadTable = _HpicfReloadTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 4, 20, 2, 2)
)
if mibBuilder.loadTexts:
    hpicfReloadTable.setStatus("current")
_HpicfReloadEntry_Object = MibTableRow
hpicfReloadEntry = _HpicfReloadEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 4, 20, 2, 2, 1)
)
hpicfReloadEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    hpicfReloadEntry.setStatus("current")
_HpicfReloadControl_Type = ReloadControl
_HpicfReloadControl_Object = MibTableColumn
hpicfReloadControl = _HpicfReloadControl_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 4, 20, 2, 2, 1, 1),
    _HpicfReloadControl_Type()
)
hpicfReloadControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfReloadControl.setStatus("current")
_HpicfReloadDateTime_Type = DateAndTime
_HpicfReloadDateTime_Object = MibTableColumn
hpicfReloadDateTime = _HpicfReloadDateTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 4, 20, 2, 2, 1, 2),
    _HpicfReloadDateTime_Type()
)
hpicfReloadDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfReloadDateTime.setStatus("current")
_HpicfReloadConformance_ObjectIdentity = ObjectIdentity
hpicfReloadConformance = _HpicfReloadConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 4, 20, 3)
)
_HpicfReloadGroups_ObjectIdentity = ObjectIdentity
hpicfReloadGroups = _HpicfReloadGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 4, 20, 3, 1)
)
_HpicfReloadCompliances_ObjectIdentity = ObjectIdentity
hpicfReloadCompliances = _HpicfReloadCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 4, 20, 3, 2)
)

# Managed Objects groups

hpicfReloadGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 4, 20, 3, 1, 1)
)
hpicfReloadGroup.setObjects(
      *(("HP-ICF-RELOAD-MIB", "hpicfReloadState"),
        ("HP-ICF-RELOAD-MIB", "hpicfReloadAfter"),
        ("HP-ICF-RELOAD-MIB", "hpicfReloadAt"),
        ("HP-ICF-RELOAD-MIB", "hpicfReloadControl"),
        ("HP-ICF-RELOAD-MIB", "hpicfReloadDateTime"))
)
if mibBuilder.loadTexts:
    hpicfReloadGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

hpicfReloadFullCompliance1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 4, 20, 3, 2, 1)
)
hpicfReloadFullCompliance1.setObjects(
    ("HP-ICF-RELOAD-MIB", "hpicfReloadGroup")
)
if mibBuilder.loadTexts:
    hpicfReloadFullCompliance1.setStatus(
        "current"
    )

hpicfReloadFullCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 4, 20, 3, 2, 2)
)
hpicfReloadFullCompliance2.setObjects(
    ("HP-ICF-RELOAD-MIB", "hpicfReloadGroup")
)
if mibBuilder.loadTexts:
    hpicfReloadFullCompliance2.setStatus(
        "current"
    )

hpicfReloadReadOnlyCompliance1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 4, 20, 3, 2, 3)
)
hpicfReloadReadOnlyCompliance1.setObjects(
    ("HP-ICF-RELOAD-MIB", "hpicfReloadGroup")
)
if mibBuilder.loadTexts:
    hpicfReloadReadOnlyCompliance1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HP-ICF-RELOAD-MIB",
    **{"ReloadControl": ReloadControl,
       "hpicfReloadMIB": hpicfReloadMIB,
       "hpicfReloadObjects": hpicfReloadObjects,
       "hpicfReloadState": hpicfReloadState,
       "hpicfReloadAfter": hpicfReloadAfter,
       "hpicfReloadAt": hpicfReloadAt,
       "hpicfEntityReload": hpicfEntityReload,
       "hpicfReloadTable": hpicfReloadTable,
       "hpicfReloadEntry": hpicfReloadEntry,
       "hpicfReloadControl": hpicfReloadControl,
       "hpicfReloadDateTime": hpicfReloadDateTime,
       "hpicfReloadConformance": hpicfReloadConformance,
       "hpicfReloadGroups": hpicfReloadGroups,
       "hpicfReloadGroup": hpicfReloadGroup,
       "hpicfReloadCompliances": hpicfReloadCompliances,
       "hpicfReloadFullCompliance1": hpicfReloadFullCompliance1,
       "hpicfReloadFullCompliance2": hpicfReloadFullCompliance2,
       "hpicfReloadReadOnlyCompliance1": hpicfReloadReadOnlyCompliance1}
)
