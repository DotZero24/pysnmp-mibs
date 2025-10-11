# SNMP MIB module (ALU-IPSEC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/nokia/ALU-IPSEC-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:01:17 2025
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

(aluSARConfs,
 aluSARMIBModules,
 aluSARNotifyPrefix,
 aluSARObjs) = mibBuilder.importSymbols(
    "ALU-SAR-GLOBAL-MIB",
    "aluSARConfs",
    "aluSARMIBModules",
    "aluSARNotifyPrefix",
    "aluSARObjs")

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

(tmnxCardSlotNum,
 tmnxChassisIndex,
 tmnxMDASlotNum) = mibBuilder.importSymbols(
    "TIMETRA-CHASSIS-MIB",
    "tmnxCardSlotNum",
    "tmnxChassisIndex",
    "tmnxMDASlotNum")

(tmnxIPsecMdaDpStatsEntry,
 tmnxIPsecTunnelEntry) = mibBuilder.importSymbols(
    "TIMETRA-IPSEC-MIB",
    "tmnxIPsecMdaDpStatsEntry",
    "tmnxIPsecTunnelEntry")

(sapEncapValue,
 sapPortId) = mibBuilder.importSymbols(
    "TIMETRA-SAP-MIB",
    "sapEncapValue",
    "sapPortId")

(svcId,) = mibBuilder.importSymbols(
    "TIMETRA-SERV-MIB",
    "svcId")


# MODULE-IDENTITY

aluIPsecMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 1, 1, 3, 16)
)
if mibBuilder.loadTexts:
    aluIPsecMIBModule.setRevisions(
        ("2011-04-18 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AluIPsecMIBConformance_ObjectIdentity = ObjectIdentity
aluIPsecMIBConformance = _AluIPsecMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 19)
)
_AluIPsecMIBCompliances_ObjectIdentity = ObjectIdentity
aluIPsecMIBCompliances = _AluIPsecMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 19, 1)
)
_AluIPsecMIBGroups_ObjectIdentity = ObjectIdentity
aluIPsecMIBGroups = _AluIPsecMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 19, 2)
)
_AluIPsecObjects_ObjectIdentity = ObjectIdentity
aluIPsecObjects = _AluIPsecObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 19)
)
_AluExtIPsecMdaDpStatsTable_Object = MibTable
aluExtIPsecMdaDpStatsTable = _AluExtIPsecMdaDpStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 19, 1)
)
if mibBuilder.loadTexts:
    aluExtIPsecMdaDpStatsTable.setStatus("current")
_AluExtIPsecMdaDpStatsEntry_Object = MibTableRow
aluExtIPsecMdaDpStatsEntry = _AluExtIPsecMdaDpStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 19, 1, 1)
)
if mibBuilder.loadTexts:
    aluExtIPsecMdaDpStatsEntry.setStatus("current")
_AluExtIPsecMdaDpStatsIPFragDrop_Type = Counter64
_AluExtIPsecMdaDpStatsIPFragDrop_Object = MibTableColumn
aluExtIPsecMdaDpStatsIPFragDrop = _AluExtIPsecMdaDpStatsIPFragDrop_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 19, 1, 1, 1),
    _AluExtIPsecMdaDpStatsIPFragDrop_Type()
)
aluExtIPsecMdaDpStatsIPFragDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aluExtIPsecMdaDpStatsIPFragDrop.setStatus("current")
_AluExtIPsecTunnelTable_Object = MibTable
aluExtIPsecTunnelTable = _AluExtIPsecTunnelTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 19, 2)
)
if mibBuilder.loadTexts:
    aluExtIPsecTunnelTable.setStatus("current")
_AluExtIPsecTunnelEntry_Object = MibTableRow
aluExtIPsecTunnelEntry = _AluExtIPsecTunnelEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 19, 2, 1)
)
if mibBuilder.loadTexts:
    aluExtIPsecTunnelEntry.setStatus("current")


class _AluExtIPsecTunnelCopyDfBit_Type(TruthValue):
    """Custom type aluExtIPsecTunnelCopyDfBit based on TruthValue"""
    defaultValue = 2


_AluExtIPsecTunnelCopyDfBit_Type.__name__ = "TruthValue"
_AluExtIPsecTunnelCopyDfBit_Object = MibTableColumn
aluExtIPsecTunnelCopyDfBit = _AluExtIPsecTunnelCopyDfBit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 2, 19, 2, 1, 1),
    _AluExtIPsecTunnelCopyDfBit_Type()
)
aluExtIPsecTunnelCopyDfBit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aluExtIPsecTunnelCopyDfBit.setStatus("current")
_AluIPsecNotificationsPrefix_ObjectIdentity = ObjectIdentity
aluIPsecNotificationsPrefix = _AluIPsecNotificationsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 3, 15)
)
_AluIPsecNotifications_ObjectIdentity = ObjectIdentity
aluIPsecNotifications = _AluIPsecNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 3, 15, 0)
)
tmnxIPsecMdaDpStatsEntry.registerAugmentions(
    ("ALU-IPSEC-MIB",
     "aluExtIPsecMdaDpStatsEntry")
)
aluExtIPsecMdaDpStatsEntry.setIndexNames(*tmnxIPsecMdaDpStatsEntry.getIndexNames())
tmnxIPsecTunnelEntry.registerAugmentions(
    ("ALU-IPSEC-MIB",
     "aluExtIPsecTunnelEntry")
)
aluExtIPsecTunnelEntry.setIndexNames(*tmnxIPsecTunnelEntry.getIndexNames())

# Managed Objects groups

aluIPsecMdaDpStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 19, 2, 1)
)
aluIPsecMdaDpStatsGroup.setObjects(
    ("ALU-IPSEC-MIB", "aluExtIPsecMdaDpStatsIPFragDrop")
)
if mibBuilder.loadTexts:
    aluIPsecMdaDpStatsGroup.setStatus("current")

aluIPsecGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 19, 2, 2)
)
aluIPsecGroup.setObjects(
    ("ALU-IPSEC-MIB", "aluExtIPsecTunnelCopyDfBit")
)
if mibBuilder.loadTexts:
    aluIPsecGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

aluIPsec7705V6v1Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 6, 1, 2, 1, 19, 1, 1)
)
aluIPsec7705V6v1Compliance.setObjects(
      *(("ALU-IPSEC-MIB", "aluIPsecMdaDpStatsGroup"),
        ("ALU-IPSEC-MIB", "aluIPsecGroup"))
)
if mibBuilder.loadTexts:
    aluIPsec7705V6v1Compliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALU-IPSEC-MIB",
    **{"aluIPsecMIBModule": aluIPsecMIBModule,
       "aluIPsecMIBConformance": aluIPsecMIBConformance,
       "aluIPsecMIBCompliances": aluIPsecMIBCompliances,
       "aluIPsec7705V6v1Compliance": aluIPsec7705V6v1Compliance,
       "aluIPsecMIBGroups": aluIPsecMIBGroups,
       "aluIPsecMdaDpStatsGroup": aluIPsecMdaDpStatsGroup,
       "aluIPsecGroup": aluIPsecGroup,
       "aluIPsecObjects": aluIPsecObjects,
       "aluExtIPsecMdaDpStatsTable": aluExtIPsecMdaDpStatsTable,
       "aluExtIPsecMdaDpStatsEntry": aluExtIPsecMdaDpStatsEntry,
       "aluExtIPsecMdaDpStatsIPFragDrop": aluExtIPsecMdaDpStatsIPFragDrop,
       "aluExtIPsecTunnelTable": aluExtIPsecTunnelTable,
       "aluExtIPsecTunnelEntry": aluExtIPsecTunnelEntry,
       "aluExtIPsecTunnelCopyDfBit": aluExtIPsecTunnelCopyDfBit,
       "aluIPsecNotificationsPrefix": aluIPsecNotificationsPrefix,
       "aluIPsecNotifications": aluIPsecNotifications}
)
