# SNMP MIB module (INFINERA-TP-OSCPTP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/INFINERA-TP-OSCPTP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:13:32 2025
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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

oscPtpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 36)
)
if mibBuilder.loadTexts:
    oscPtpMIB.setRevisions(
        ("2012-10-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_OscPtpTable_Object = MibTable
oscPtpTable = _OscPtpTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 36, 1)
)
if mibBuilder.loadTexts:
    oscPtpTable.setStatus("current")
_OscPtpEntry_Object = MibTableRow
oscPtpEntry = _OscPtpEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 36, 1, 1)
)
oscPtpEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    oscPtpEntry.setStatus("current")


class _OscPtpPmHistStatsEnable_Type(Integer32):
    """Custom type oscPtpPmHistStatsEnable based on Integer32"""
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


_OscPtpPmHistStatsEnable_Type.__name__ = "Integer32"
_OscPtpPmHistStatsEnable_Object = MibTableColumn
oscPtpPmHistStatsEnable = _OscPtpPmHistStatsEnable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 36, 1, 1, 1),
    _OscPtpPmHistStatsEnable_Type()
)
oscPtpPmHistStatsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oscPtpPmHistStatsEnable.setStatus("current")
_OscPtpConformance_ObjectIdentity = ObjectIdentity
oscPtpConformance = _OscPtpConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 36, 3)
)
_OscPtpCompliances_ObjectIdentity = ObjectIdentity
oscPtpCompliances = _OscPtpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 36, 3, 1)
)
_OscPtpGroups_ObjectIdentity = ObjectIdentity
oscPtpGroups = _OscPtpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 36, 3, 2)
)

# Managed Objects groups

oscPtpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 36, 3, 2, 1)
)
oscPtpGroup.setObjects(
    ("INFINERA-TP-OSCPTP-MIB", "oscPtpPmHistStatsEnable")
)
if mibBuilder.loadTexts:
    oscPtpGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

oscPtpCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 36, 3, 1, 1)
)
oscPtpCompliance.setObjects(
    ("INFINERA-TP-OSCPTP-MIB", "oscPtpGroup")
)
if mibBuilder.loadTexts:
    oscPtpCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INFINERA-TP-OSCPTP-MIB",
    **{"oscPtpMIB": oscPtpMIB,
       "oscPtpTable": oscPtpTable,
       "oscPtpEntry": oscPtpEntry,
       "oscPtpPmHistStatsEnable": oscPtpPmHistStatsEnable,
       "oscPtpConformance": oscPtpConformance,
       "oscPtpCompliances": oscPtpCompliances,
       "oscPtpCompliance": oscPtpCompliance,
       "oscPtpGroups": oscPtpGroups,
       "oscPtpGroup": oscPtpGroup}
)
