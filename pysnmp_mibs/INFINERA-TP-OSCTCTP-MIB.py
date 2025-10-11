# SNMP MIB module (INFINERA-TP-OSCTCTP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/INFINERA-TP-OSCTCTP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:16:15 2025
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

(terminationPoint,) = mibBuilder.importSymbols(
    "INFINERA-REG-MIB",
    "terminationPoint")

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

osctCtpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 11)
)
if mibBuilder.loadTexts:
    osctCtpMIB.setRevisions(
        ("2009-03-25 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_OsctCtpTable_Object = MibTable
osctCtpTable = _OsctCtpTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 11, 1)
)
if mibBuilder.loadTexts:
    osctCtpTable.setStatus("current")
_OsctCtpEntry_Object = MibTableRow
osctCtpEntry = _OsctCtpEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 11, 1, 1)
)
osctCtpEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    osctCtpEntry.setStatus("current")


class _OsctCtpPmHistStatsEnable_Type(Integer32):
    """Custom type osctCtpPmHistStatsEnable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_OsctCtpPmHistStatsEnable_Type.__name__ = "Integer32"
_OsctCtpPmHistStatsEnable_Object = MibTableColumn
osctCtpPmHistStatsEnable = _OsctCtpPmHistStatsEnable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 11, 1, 1, 1),
    _OsctCtpPmHistStatsEnable_Type()
)
osctCtpPmHistStatsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    osctCtpPmHistStatsEnable.setStatus("current")
_OsctCtpConformance_ObjectIdentity = ObjectIdentity
osctCtpConformance = _OsctCtpConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 11, 3)
)
_OsctCtpCompliances_ObjectIdentity = ObjectIdentity
osctCtpCompliances = _OsctCtpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 11, 3, 1)
)
_OsctCtpGroups_ObjectIdentity = ObjectIdentity
osctCtpGroups = _OsctCtpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 11, 3, 2)
)

# Managed Objects groups

osctCtpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 11, 3, 2, 1)
)
osctCtpGroup.setObjects(
    ("INFINERA-TP-OSCTCTP-MIB", "osctCtpPmHistStatsEnable")
)
if mibBuilder.loadTexts:
    osctCtpGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INFINERA-TP-OSCTCTP-MIB",
    **{"osctCtpMIB": osctCtpMIB,
       "osctCtpTable": osctCtpTable,
       "osctCtpEntry": osctCtpEntry,
       "osctCtpPmHistStatsEnable": osctCtpPmHistStatsEnable,
       "osctCtpConformance": osctCtpConformance,
       "osctCtpCompliances": osctCtpCompliances,
       "osctCtpGroups": osctCtpGroups,
       "osctCtpGroup": osctCtpGroup}
)
