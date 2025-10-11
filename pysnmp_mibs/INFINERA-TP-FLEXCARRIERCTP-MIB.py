# SNMP MIB module (INFINERA-TP-FLEXCARRIERCTP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/INFINERA-TP-FLEXCARRIERCTP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:13:35 2025
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

(FloatHundredths,
 FloatTenths,
 InfnModulation,
 InfnPmHistStatsControl) = mibBuilder.importSymbols(
    "INFINERA-TC-MIB",
    "FloatHundredths",
    "FloatTenths",
    "InfnModulation",
    "InfnPmHistStatsControl")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

flexCarrierCtpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 59)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FlexCarrierCtpTable_Object = MibTable
flexCarrierCtpTable = _FlexCarrierCtpTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 59, 1)
)
if mibBuilder.loadTexts:
    flexCarrierCtpTable.setStatus("current")
_FlexCarrierCtpEntry_Object = MibTableRow
flexCarrierCtpEntry = _FlexCarrierCtpEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 59, 1, 1)
)
flexCarrierCtpEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    flexCarrierCtpEntry.setStatus("current")
_FlexCarrierCtpPmHistStatsEnable_Type = InfnPmHistStatsControl
_FlexCarrierCtpPmHistStatsEnable_Object = MibTableColumn
flexCarrierCtpPmHistStatsEnable = _FlexCarrierCtpPmHistStatsEnable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 59, 1, 1, 1),
    _FlexCarrierCtpPmHistStatsEnable_Type()
)
flexCarrierCtpPmHistStatsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flexCarrierCtpPmHistStatsEnable.setStatus("current")
_FlexCarrierCtpFreqSlotList_Type = DisplayString
_FlexCarrierCtpFreqSlotList_Object = MibTableColumn
flexCarrierCtpFreqSlotList = _FlexCarrierCtpFreqSlotList_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 59, 1, 1, 2),
    _FlexCarrierCtpFreqSlotList_Type()
)
flexCarrierCtpFreqSlotList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flexCarrierCtpFreqSlotList.setStatus("current")
_FlexCarrierCtpConformance_ObjectIdentity = ObjectIdentity
flexCarrierCtpConformance = _FlexCarrierCtpConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 59, 59)
)
_FlexCarrierCtpCompliances_ObjectIdentity = ObjectIdentity
flexCarrierCtpCompliances = _FlexCarrierCtpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 59, 59, 1)
)
_FlexCarrierCtpGroups_ObjectIdentity = ObjectIdentity
flexCarrierCtpGroups = _FlexCarrierCtpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 59, 59, 2)
)

# Managed Objects groups

flexCarrierCtpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 59, 59, 2, 1)
)
flexCarrierCtpGroup.setObjects(
      *(("INFINERA-TP-FLEXCARRIERCTP-MIB", "flexCarrierCtpPmHistStatsEnable"),
        ("INFINERA-TP-FLEXCARRIERCTP-MIB", "flexCarrierCtpFreqSlotList"))
)
if mibBuilder.loadTexts:
    flexCarrierCtpGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

flexCarrierCtpCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 59, 59, 1, 1)
)
flexCarrierCtpCompliance.setObjects(
    ("INFINERA-TP-FLEXCARRIERCTP-MIB", "flexCarrierCtpGroup")
)
if mibBuilder.loadTexts:
    flexCarrierCtpCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INFINERA-TP-FLEXCARRIERCTP-MIB",
    **{"flexCarrierCtpMIB": flexCarrierCtpMIB,
       "flexCarrierCtpTable": flexCarrierCtpTable,
       "flexCarrierCtpEntry": flexCarrierCtpEntry,
       "flexCarrierCtpPmHistStatsEnable": flexCarrierCtpPmHistStatsEnable,
       "flexCarrierCtpFreqSlotList": flexCarrierCtpFreqSlotList,
       "flexCarrierCtpConformance": flexCarrierCtpConformance,
       "flexCarrierCtpCompliances": flexCarrierCtpCompliances,
       "flexCarrierCtpCompliance": flexCarrierCtpCompliance,
       "flexCarrierCtpGroups": flexCarrierCtpGroups,
       "flexCarrierCtpGroup": flexCarrierCtpGroup}
)
