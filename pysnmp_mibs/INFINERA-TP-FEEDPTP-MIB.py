# SNMP MIB module (INFINERA-TP-FEEDPTP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/INFINERA-TP-FEEDPTP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:16:51 2025
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

feedPtpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 52)
)
if mibBuilder.loadTexts:
    feedPtpMIB.setRevisions(
        ("2008-10-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FeedPtpTable_Object = MibTable
feedPtpTable = _FeedPtpTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 52, 1)
)
if mibBuilder.loadTexts:
    feedPtpTable.setStatus("current")
_FeedPtpEntry_Object = MibTableRow
feedPtpEntry = _FeedPtpEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 52, 1, 1)
)
feedPtpEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    feedPtpEntry.setStatus("current")


class _FeedPtpPmHistStatsEnable_Type(Integer32):
    """Custom type feedPtpPmHistStatsEnable based on Integer32"""
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


_FeedPtpPmHistStatsEnable_Type.__name__ = "Integer32"
_FeedPtpPmHistStatsEnable_Object = MibTableColumn
feedPtpPmHistStatsEnable = _FeedPtpPmHistStatsEnable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 52, 1, 1, 1),
    _FeedPtpPmHistStatsEnable_Type()
)
feedPtpPmHistStatsEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feedPtpPmHistStatsEnable.setStatus("current")
_FeedPtpConformance_ObjectIdentity = ObjectIdentity
feedPtpConformance = _FeedPtpConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 52, 3)
)
_FeedPtpCompliances_ObjectIdentity = ObjectIdentity
feedPtpCompliances = _FeedPtpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 52, 3, 1)
)
_FeedPtpGroups_ObjectIdentity = ObjectIdentity
feedPtpGroups = _FeedPtpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 52, 3, 2)
)

# Managed Objects groups

feedPtpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 52, 3, 2, 1)
)
feedPtpGroup.setObjects(
    ("INFINERA-TP-FEEDPTP-MIB", "feedPtpPmHistStatsEnable")
)
if mibBuilder.loadTexts:
    feedPtpGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

feedPtpCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 52, 3, 1, 1)
)
feedPtpCompliance.setObjects(
    ("INFINERA-TP-FEEDPTP-MIB", "feedPtpGroup")
)
if mibBuilder.loadTexts:
    feedPtpCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INFINERA-TP-FEEDPTP-MIB",
    **{"feedPtpMIB": feedPtpMIB,
       "feedPtpTable": feedPtpTable,
       "feedPtpEntry": feedPtpEntry,
       "feedPtpPmHistStatsEnable": feedPtpPmHistStatsEnable,
       "feedPtpConformance": feedPtpConformance,
       "feedPtpCompliances": feedPtpCompliances,
       "feedPtpCompliance": feedPtpCompliance,
       "feedPtpGroups": feedPtpGroups,
       "feedPtpGroup": feedPtpGroup}
)
