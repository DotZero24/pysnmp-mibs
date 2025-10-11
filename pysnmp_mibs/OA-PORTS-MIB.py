# SNMP MIB module (OA-PORTS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/mrv/OA-PORTS-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:05:12 2025
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

(nbSwitchG1Il,) = mibBuilder.importSymbols(
    "OS-COMMON-TC-MIB",
    "nbSwitchG1Il")

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

nbPortMediaSelectMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 10, 10)
)
if mibBuilder.loadTexts:
    nbPortMediaSelectMIB.setRevisions(
        ("2006-03-08 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NbPortParams_ObjectIdentity = ObjectIdentity
nbPortParams = _NbPortParams_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 10)
)
_NbPortMediaSelectTable_Object = MibTable
nbPortMediaSelectTable = _NbPortMediaSelectTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 10, 10, 5)
)
if mibBuilder.loadTexts:
    nbPortMediaSelectTable.setStatus("current")
_NbPortMediaSelectEntry_Object = MibTableRow
nbPortMediaSelectEntry = _NbPortMediaSelectEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 10, 10, 5, 1)
)
nbPortMediaSelectEntry.setIndexNames(
    (0, "OA-PORTS-MIB", "nbPortMediaSelectPort"),
)
if mibBuilder.loadTexts:
    nbPortMediaSelectEntry.setStatus("current")


class _NbPortMediaSelectPort_Type(Integer32):
    """Custom type nbPortMediaSelectPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_NbPortMediaSelectPort_Type.__name__ = "Integer32"
_NbPortMediaSelectPort_Object = MibTableColumn
nbPortMediaSelectPort = _NbPortMediaSelectPort_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 10, 10, 5, 1, 1),
    _NbPortMediaSelectPort_Type()
)
nbPortMediaSelectPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nbPortMediaSelectPort.setStatus("current")


class _NbPortMediaSelectMode_Type(Integer32):
    """Custom type nbPortMediaSelectMode based on Integer32"""
    defaultValue = 2

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
          ("autoSelect", 2),
          ("forceRJ45", 3),
          ("forceSFP", 4),
          ("forceSFP100", 5))
    )


_NbPortMediaSelectMode_Type.__name__ = "Integer32"
_NbPortMediaSelectMode_Object = MibTableColumn
nbPortMediaSelectMode = _NbPortMediaSelectMode_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 10, 10, 5, 1, 2),
    _NbPortMediaSelectMode_Type()
)
nbPortMediaSelectMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbPortMediaSelectMode.setStatus("current")


class _NbPortMediaSelectStatus_Type(Integer32):
    """Custom type nbPortMediaSelectStatus based on Integer32"""
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
        *(("unknown", 1),
          ("rj45", 2),
          ("sfp", 3),
          ("sfp100", 4))
    )


_NbPortMediaSelectStatus_Type.__name__ = "Integer32"
_NbPortMediaSelectStatus_Object = MibTableColumn
nbPortMediaSelectStatus = _NbPortMediaSelectStatus_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 10, 10, 5, 1, 3),
    _NbPortMediaSelectStatus_Type()
)
nbPortMediaSelectStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbPortMediaSelectStatus.setStatus("current")
_NbPortMediaSelectConformance_ObjectIdentity = ObjectIdentity
nbPortMediaSelectConformance = _NbPortMediaSelectConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 10, 10, 101)
)
_NbPortMediaSelectMIBCompliances_ObjectIdentity = ObjectIdentity
nbPortMediaSelectMIBCompliances = _NbPortMediaSelectMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 10, 10, 101, 1)
)
_NbPortMediaSelectMIBGroups_ObjectIdentity = ObjectIdentity
nbPortMediaSelectMIBGroups = _NbPortMediaSelectMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 10, 10, 101, 2)
)

# Managed Objects groups

nbPortMediaSelectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 10, 10, 101, 2, 2)
)
nbPortMediaSelectGroup.setObjects(
      *(("OA-PORTS-MIB", "nbPortMediaSelectMode"),
        ("OA-PORTS-MIB", "nbPortMediaSelectStatus"))
)
if mibBuilder.loadTexts:
    nbPortMediaSelectGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

nbPortMediaSelectMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 10, 10, 101, 1, 1)
)
nbPortMediaSelectMIBCompliance.setObjects(
    ("OA-PORTS-MIB", "nbPortMediaSelectGroup")
)
if mibBuilder.loadTexts:
    nbPortMediaSelectMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "OA-PORTS-MIB",
    **{"nbPortParams": nbPortParams,
       "nbPortMediaSelectMIB": nbPortMediaSelectMIB,
       "nbPortMediaSelectTable": nbPortMediaSelectTable,
       "nbPortMediaSelectEntry": nbPortMediaSelectEntry,
       "nbPortMediaSelectPort": nbPortMediaSelectPort,
       "nbPortMediaSelectMode": nbPortMediaSelectMode,
       "nbPortMediaSelectStatus": nbPortMediaSelectStatus,
       "nbPortMediaSelectConformance": nbPortMediaSelectConformance,
       "nbPortMediaSelectMIBCompliances": nbPortMediaSelectMIBCompliances,
       "nbPortMediaSelectMIBCompliance": nbPortMediaSelectMIBCompliance,
       "nbPortMediaSelectMIBGroups": nbPortMediaSelectMIBGroups,
       "nbPortMediaSelectGroup": nbPortMediaSelectGroup}
)
