# SNMP MIB module (INFINERA-TP-OSAPTP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/INFINERA-TP-OSAPTP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:13:01 2025
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

(FloatTenths,
 InfnServiceType) = mibBuilder.importSymbols(
    "INFINERA-TC-MIB",
    "FloatTenths",
    "InfnServiceType")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

osaPtpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 21)
)
if mibBuilder.loadTexts:
    osaPtpMIB.setRevisions(
        ("2008-10-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_OsaPtpTable_Object = MibTable
osaPtpTable = _OsaPtpTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 21, 1)
)
if mibBuilder.loadTexts:
    osaPtpTable.setStatus("current")
_OsaPtpEntry_Object = MibTableRow
osaPtpEntry = _OsaPtpEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 21, 1, 1)
)
osaPtpEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    osaPtpEntry.setStatus("current")


class _OsaPtpPmHistStatsEnable_Type(Integer32):
    """Custom type osaPtpPmHistStatsEnable based on Integer32"""
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


_OsaPtpPmHistStatsEnable_Type.__name__ = "Integer32"
_OsaPtpPmHistStatsEnable_Object = MibTableColumn
osaPtpPmHistStatsEnable = _OsaPtpPmHistStatsEnable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 21, 1, 1, 1),
    _OsaPtpPmHistStatsEnable_Type()
)
osaPtpPmHistStatsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    osaPtpPmHistStatsEnable.setStatus("current")
_OsaPtpConformance_ObjectIdentity = ObjectIdentity
osaPtpConformance = _OsaPtpConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 21, 3)
)
_OsaPtpCompliances_ObjectIdentity = ObjectIdentity
osaPtpCompliances = _OsaPtpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 21, 3, 1)
)
_OsaPtpGroups_ObjectIdentity = ObjectIdentity
osaPtpGroups = _OsaPtpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 21, 3, 2)
)

# Managed Objects groups

osaPtpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 21, 3, 2, 1)
)
osaPtpGroup.setObjects(
    ("INFINERA-TP-OSAPTP-MIB", "osaPtpPmHistStatsEnable")
)
if mibBuilder.loadTexts:
    osaPtpGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

osaPtpCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 21, 3, 1, 1)
)
osaPtpCompliance.setObjects(
    ("INFINERA-TP-OSAPTP-MIB", "osaPtpGroup")
)
if mibBuilder.loadTexts:
    osaPtpCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INFINERA-TP-OSAPTP-MIB",
    **{"osaPtpMIB": osaPtpMIB,
       "osaPtpTable": osaPtpTable,
       "osaPtpEntry": osaPtpEntry,
       "osaPtpPmHistStatsEnable": osaPtpPmHistStatsEnable,
       "osaPtpConformance": osaPtpConformance,
       "osaPtpCompliances": osaPtpCompliances,
       "osaPtpCompliance": osaPtpCompliance,
       "osaPtpGroups": osaPtpGroups,
       "osaPtpGroup": osaPtpGroup}
)
