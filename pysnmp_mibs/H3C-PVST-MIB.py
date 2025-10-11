# SNMP MIB module (H3C-PVST-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/h3c/H3C-PVST-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:20:17 2025
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

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

h3cPvst = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 131)
)
if mibBuilder.loadTexts:
    h3cPvst.setRevisions(
        ("2014-05-27 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_H3cPvstObjects_ObjectIdentity = ObjectIdentity
h3cPvstObjects = _H3cPvstObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 131, 1)
)
_H3cPvstVlanConfigTable_Object = MibTable
h3cPvstVlanConfigTable = _H3cPvstVlanConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 131, 1, 1)
)
if mibBuilder.loadTexts:
    h3cPvstVlanConfigTable.setStatus("current")
_H3cPvstVlanConfigEntry_Object = MibTableRow
h3cPvstVlanConfigEntry = _H3cPvstVlanConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 131, 1, 1, 1)
)
h3cPvstVlanConfigEntry.setIndexNames(
    (0, "H3C-PVST-MIB", "h3cPvstVlanID"),
)
if mibBuilder.loadTexts:
    h3cPvstVlanConfigEntry.setStatus("current")


class _H3cPvstVlanID_Type(Integer32):
    """Custom type h3cPvstVlanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_H3cPvstVlanID_Type.__name__ = "Integer32"
_H3cPvstVlanID_Object = MibTableColumn
h3cPvstVlanID = _H3cPvstVlanID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 131, 1, 1, 1, 1),
    _H3cPvstVlanID_Type()
)
h3cPvstVlanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cPvstVlanID.setStatus("current")
_H3cPvstVlanPortConfigTable_Object = MibTable
h3cPvstVlanPortConfigTable = _H3cPvstVlanPortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 131, 1, 2)
)
if mibBuilder.loadTexts:
    h3cPvstVlanPortConfigTable.setStatus("current")
_H3cPvstVlanPortConfigEntry_Object = MibTableRow
h3cPvstVlanPortConfigEntry = _H3cPvstVlanPortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 131, 1, 2, 1)
)
h3cPvstVlanPortConfigEntry.setIndexNames(
    (0, "H3C-PVST-MIB", "h3cPvstPortVlanID"),
    (0, "H3C-PVST-MIB", "h3cPvstPortIndex"),
)
if mibBuilder.loadTexts:
    h3cPvstVlanPortConfigEntry.setStatus("current")


class _H3cPvstPortVlanID_Type(Integer32):
    """Custom type h3cPvstPortVlanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_H3cPvstPortVlanID_Type.__name__ = "Integer32"
_H3cPvstPortVlanID_Object = MibTableColumn
h3cPvstPortVlanID = _H3cPvstPortVlanID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 131, 1, 2, 1, 1),
    _H3cPvstPortVlanID_Type()
)
h3cPvstPortVlanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cPvstPortVlanID.setStatus("current")


class _H3cPvstPortIndex_Type(Integer32):
    """Custom type h3cPvstPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_H3cPvstPortIndex_Type.__name__ = "Integer32"
_H3cPvstPortIndex_Object = MibTableColumn
h3cPvstPortIndex = _H3cPvstPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 131, 1, 2, 1, 2),
    _H3cPvstPortIndex_Type()
)
h3cPvstPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cPvstPortIndex.setStatus("current")
_H3cPvstNotifications_ObjectIdentity = ObjectIdentity
h3cPvstNotifications = _H3cPvstNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 131, 2)
)
_H3cPvstEvents_ObjectIdentity = ObjectIdentity
h3cPvstEvents = _H3cPvstEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 131, 2, 0)
)

# Managed Objects groups


# Notification objects

h3cPvstVlanPortDetectedTc = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 131, 2, 0, 1)
)
h3cPvstVlanPortDetectedTc.setObjects(
      *(("H3C-PVST-MIB", "h3cPvstPortVlanID"),
        ("H3C-PVST-MIB", "h3cPvstPortIndex"))
)
if mibBuilder.loadTexts:
    h3cPvstVlanPortDetectedTc.setStatus(
        "current"
    )

h3cPvstVlanPortRcvdTc = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 131, 2, 0, 2)
)
h3cPvstVlanPortRcvdTc.setObjects(
      *(("H3C-PVST-MIB", "h3cPvstPortVlanID"),
        ("H3C-PVST-MIB", "h3cPvstPortIndex"))
)
if mibBuilder.loadTexts:
    h3cPvstVlanPortRcvdTc.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "H3C-PVST-MIB",
    **{"h3cPvst": h3cPvst,
       "h3cPvstObjects": h3cPvstObjects,
       "h3cPvstVlanConfigTable": h3cPvstVlanConfigTable,
       "h3cPvstVlanConfigEntry": h3cPvstVlanConfigEntry,
       "h3cPvstVlanID": h3cPvstVlanID,
       "h3cPvstVlanPortConfigTable": h3cPvstVlanPortConfigTable,
       "h3cPvstVlanPortConfigEntry": h3cPvstVlanPortConfigEntry,
       "h3cPvstPortVlanID": h3cPvstPortVlanID,
       "h3cPvstPortIndex": h3cPvstPortIndex,
       "h3cPvstNotifications": h3cPvstNotifications,
       "h3cPvstEvents": h3cPvstEvents,
       "h3cPvstVlanPortDetectedTc": h3cPvstVlanPortDetectedTc,
       "h3cPvstVlanPortRcvdTc": h3cPvstVlanPortRcvdTc}
)
