# SNMP MIB module (ELTEX-FASTPATH-QOS-COS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/eltex/ELTEX-FASTPATH-QOS-COS-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:50:56 2025
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

(eltFastpathQosMIB,) = mibBuilder.importSymbols(
    "ELTEX-FASTPATH-QOS-MIB",
    "eltFastpathQosMIB")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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

eltFastpathQosCosMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 103, 2, 1)
)
if mibBuilder.loadTexts:
    eltFastpathQosCosMIB.setRevisions(
        ("2017-03-09 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_EfpQosCosObjects_ObjectIdentity = ObjectIdentity
efpQosCosObjects = _EfpQosCosObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 103, 2, 1, 1)
)
_EfpQosCosStatistics_ObjectIdentity = ObjectIdentity
efpQosCosStatistics = _EfpQosCosStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 103, 2, 1, 1, 3)
)
_EfpAgentCosTrafficInfoTable_Object = MibTable
efpAgentCosTrafficInfoTable = _EfpAgentCosTrafficInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 103, 2, 1, 1, 3, 1)
)
if mibBuilder.loadTexts:
    efpAgentCosTrafficInfoTable.setStatus("current")
_EfpAgentCosTrafficInfoEntry_Object = MibTableRow
efpAgentCosTrafficInfoEntry = _EfpAgentCosTrafficInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 103, 2, 1, 1, 3, 1, 1)
)
efpAgentCosTrafficInfoEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    efpAgentCosTrafficInfoEntry.setStatus("current")
_EfpAgentCosTrafficInfoTotalPass_Type = Counter64
_EfpAgentCosTrafficInfoTotalPass_Object = MibTableColumn
efpAgentCosTrafficInfoTotalPass = _EfpAgentCosTrafficInfoTotalPass_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 103, 2, 1, 1, 3, 1, 1, 1),
    _EfpAgentCosTrafficInfoTotalPass_Type()
)
efpAgentCosTrafficInfoTotalPass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    efpAgentCosTrafficInfoTotalPass.setStatus("current")
_EfpAgentCosTrafficInfoTotalDrops_Type = Counter64
_EfpAgentCosTrafficInfoTotalDrops_Object = MibTableColumn
efpAgentCosTrafficInfoTotalDrops = _EfpAgentCosTrafficInfoTotalDrops_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 103, 2, 1, 1, 3, 1, 1, 2),
    _EfpAgentCosTrafficInfoTotalDrops_Type()
)
efpAgentCosTrafficInfoTotalDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    efpAgentCosTrafficInfoTotalDrops.setStatus("current")
_EfpAgentCosTrafficInfoTxQueue_Type = Gauge32
_EfpAgentCosTrafficInfoTxQueue_Object = MibTableColumn
efpAgentCosTrafficInfoTxQueue = _EfpAgentCosTrafficInfoTxQueue_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 103, 2, 1, 1, 3, 1, 1, 3),
    _EfpAgentCosTrafficInfoTxQueue_Type()
)
efpAgentCosTrafficInfoTxQueue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    efpAgentCosTrafficInfoTxQueue.setStatus("current")
_EfpAgentCosTrafficInfoRxQueue_Type = Gauge32
_EfpAgentCosTrafficInfoRxQueue_Object = MibTableColumn
efpAgentCosTrafficInfoRxQueue = _EfpAgentCosTrafficInfoRxQueue_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 103, 2, 1, 1, 3, 1, 1, 4),
    _EfpAgentCosTrafficInfoRxQueue_Type()
)
efpAgentCosTrafficInfoRxQueue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    efpAgentCosTrafficInfoRxQueue.setStatus("current")
_EfpAgentCosTrafficInfoRedDrops_Type = Counter64
_EfpAgentCosTrafficInfoRedDrops_Object = MibTableColumn
efpAgentCosTrafficInfoRedDrops = _EfpAgentCosTrafficInfoRedDrops_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 103, 2, 1, 1, 3, 1, 1, 5),
    _EfpAgentCosTrafficInfoRedDrops_Type()
)
efpAgentCosTrafficInfoRedDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    efpAgentCosTrafficInfoRedDrops.setStatus("current")
_EfpAgentCosTrafficInfoYellowDrops_Type = Counter64
_EfpAgentCosTrafficInfoYellowDrops_Object = MibTableColumn
efpAgentCosTrafficInfoYellowDrops = _EfpAgentCosTrafficInfoYellowDrops_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 103, 2, 1, 1, 3, 1, 1, 6),
    _EfpAgentCosTrafficInfoYellowDrops_Type()
)
efpAgentCosTrafficInfoYellowDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    efpAgentCosTrafficInfoYellowDrops.setStatus("current")
_EfpAgentCosTrafficInfoWredQueue_Type = Gauge32
_EfpAgentCosTrafficInfoWredQueue_Object = MibTableColumn
efpAgentCosTrafficInfoWredQueue = _EfpAgentCosTrafficInfoWredQueue_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 103, 2, 1, 1, 3, 1, 1, 7),
    _EfpAgentCosTrafficInfoWredQueue_Type()
)
efpAgentCosTrafficInfoWredQueue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    efpAgentCosTrafficInfoWredQueue.setStatus("current")
_EfpAgentCosTrafficInfoQueueTable_Object = MibTable
efpAgentCosTrafficInfoQueueTable = _EfpAgentCosTrafficInfoQueueTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 103, 2, 1, 1, 3, 2)
)
if mibBuilder.loadTexts:
    efpAgentCosTrafficInfoQueueTable.setStatus("current")
_EfpAgentCosTrafficInfoQueueEntry_Object = MibTableRow
efpAgentCosTrafficInfoQueueEntry = _EfpAgentCosTrafficInfoQueueEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 103, 2, 1, 1, 3, 2, 1)
)
efpAgentCosTrafficInfoQueueEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ELTEX-FASTPATH-QOS-COS-MIB", "efpAgentCosTrafficInfoQueueIndex"),
)
if mibBuilder.loadTexts:
    efpAgentCosTrafficInfoQueueEntry.setStatus("current")
_EfpAgentCosTrafficInfoQueueIndex_Type = Unsigned32
_EfpAgentCosTrafficInfoQueueIndex_Object = MibTableColumn
efpAgentCosTrafficInfoQueueIndex = _EfpAgentCosTrafficInfoQueueIndex_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 103, 2, 1, 1, 3, 2, 1, 1),
    _EfpAgentCosTrafficInfoQueueIndex_Type()
)
efpAgentCosTrafficInfoQueueIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    efpAgentCosTrafficInfoQueueIndex.setStatus("current")


class _EfpAgentCosTrafficInfoQueueName_Type(DisplayString):
    """Custom type efpAgentCosTrafficInfoQueueName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 3),
    )


_EfpAgentCosTrafficInfoQueueName_Type.__name__ = "DisplayString"
_EfpAgentCosTrafficInfoQueueName_Object = MibTableColumn
efpAgentCosTrafficInfoQueueName = _EfpAgentCosTrafficInfoQueueName_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 103, 2, 1, 1, 3, 2, 1, 2),
    _EfpAgentCosTrafficInfoQueueName_Type()
)
efpAgentCosTrafficInfoQueueName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    efpAgentCosTrafficInfoQueueName.setStatus("current")
_EfpAgentCosTrafficInfoQueueTotalPass_Type = Counter64
_EfpAgentCosTrafficInfoQueueTotalPass_Object = MibTableColumn
efpAgentCosTrafficInfoQueueTotalPass = _EfpAgentCosTrafficInfoQueueTotalPass_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 103, 2, 1, 1, 3, 2, 1, 3),
    _EfpAgentCosTrafficInfoQueueTotalPass_Type()
)
efpAgentCosTrafficInfoQueueTotalPass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    efpAgentCosTrafficInfoQueueTotalPass.setStatus("current")
_EfpAgentCosTrafficInfoQueueTotalDrops_Type = Counter64
_EfpAgentCosTrafficInfoQueueTotalDrops_Object = MibTableColumn
efpAgentCosTrafficInfoQueueTotalDrops = _EfpAgentCosTrafficInfoQueueTotalDrops_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 103, 2, 1, 1, 3, 2, 1, 4),
    _EfpAgentCosTrafficInfoQueueTotalDrops_Type()
)
efpAgentCosTrafficInfoQueueTotalDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    efpAgentCosTrafficInfoQueueTotalDrops.setStatus("current")
_EfpAgentCosTrafficInfoQueueTxQueue_Type = Gauge32
_EfpAgentCosTrafficInfoQueueTxQueue_Object = MibTableColumn
efpAgentCosTrafficInfoQueueTxQueue = _EfpAgentCosTrafficInfoQueueTxQueue_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 103, 2, 1, 1, 3, 2, 1, 5),
    _EfpAgentCosTrafficInfoQueueTxQueue_Type()
)
efpAgentCosTrafficInfoQueueTxQueue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    efpAgentCosTrafficInfoQueueTxQueue.setStatus("current")
_EfpAgentCosTrafficInfoQueueWredQueue_Type = Gauge32
_EfpAgentCosTrafficInfoQueueWredQueue_Object = MibTableColumn
efpAgentCosTrafficInfoQueueWredQueue = _EfpAgentCosTrafficInfoQueueWredQueue_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 103, 2, 1, 1, 3, 2, 1, 6),
    _EfpAgentCosTrafficInfoQueueWredQueue_Type()
)
efpAgentCosTrafficInfoQueueWredQueue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    efpAgentCosTrafficInfoQueueWredQueue.setStatus("current")
_EfpQosCosNotifications_ObjectIdentity = ObjectIdentity
efpQosCosNotifications = _EfpQosCosNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 103, 2, 1, 2)
)
_EfpQosCosNotificationsPrefix_ObjectIdentity = ObjectIdentity
efpQosCosNotificationsPrefix = _EfpQosCosNotificationsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 103, 2, 1, 2, 0)
)
_EfpQosCosConformance_ObjectIdentity = ObjectIdentity
efpQosCosConformance = _EfpQosCosConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 103, 2, 1, 3)
)
_EfpQosCosCompliances_ObjectIdentity = ObjectIdentity
efpQosCosCompliances = _EfpQosCosCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 103, 2, 1, 3, 1)
)
_EfpQosCosGroups_ObjectIdentity = ObjectIdentity
efpQosCosGroups = _EfpQosCosGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 103, 2, 1, 3, 2)
)

# Managed Objects groups

efpAgentQosCosTrafficInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 35265, 1, 103, 2, 1, 3, 2, 1)
)
efpAgentQosCosTrafficInfoGroup.setObjects(
      *(("ELTEX-FASTPATH-QOS-COS-MIB", "efpAgentCosTrafficInfoTotalPass"),
        ("ELTEX-FASTPATH-QOS-COS-MIB", "efpAgentCosTrafficInfoTotalDrops"),
        ("ELTEX-FASTPATH-QOS-COS-MIB", "efpAgentCosTrafficInfoTxQueue"),
        ("ELTEX-FASTPATH-QOS-COS-MIB", "efpAgentCosTrafficInfoRxQueue"),
        ("ELTEX-FASTPATH-QOS-COS-MIB", "efpAgentCosTrafficInfoRedDrops"),
        ("ELTEX-FASTPATH-QOS-COS-MIB", "efpAgentCosTrafficInfoYellowDrops"),
        ("ELTEX-FASTPATH-QOS-COS-MIB", "efpAgentCosTrafficInfoWredQueue"))
)
if mibBuilder.loadTexts:
    efpAgentQosCosTrafficInfoGroup.setStatus("current")

efpAgentQosCosTrafficInfoQueueGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 35265, 1, 103, 2, 1, 3, 2, 2)
)
efpAgentQosCosTrafficInfoQueueGroup.setObjects(
      *(("ELTEX-FASTPATH-QOS-COS-MIB", "efpAgentCosTrafficInfoQueueName"),
        ("ELTEX-FASTPATH-QOS-COS-MIB", "efpAgentCosTrafficInfoQueueTotalPass"),
        ("ELTEX-FASTPATH-QOS-COS-MIB", "efpAgentCosTrafficInfoQueueTotalDrops"),
        ("ELTEX-FASTPATH-QOS-COS-MIB", "efpAgentCosTrafficInfoQueueTxQueue"),
        ("ELTEX-FASTPATH-QOS-COS-MIB", "efpAgentCosTrafficInfoQueueWredQueue"))
)
if mibBuilder.loadTexts:
    efpAgentQosCosTrafficInfoQueueGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

efpQosCosCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 35265, 1, 103, 2, 1, 3, 1, 1)
)
efpQosCosCompliance.setObjects(
      *(("ELTEX-FASTPATH-QOS-COS-MIB", "efpAgentQosCosTrafficInfoGroup"),
        ("ELTEX-FASTPATH-QOS-COS-MIB", "efpAgentQosCosTrafficInfoQueueGroup"))
)
if mibBuilder.loadTexts:
    efpQosCosCompliance.setStatus(
        "obsolete"
    )

efpQosCosCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 35265, 1, 103, 2, 1, 3, 1, 2)
)
efpQosCosCompliance2.setObjects(
      *(("ELTEX-FASTPATH-QOS-COS-MIB", "efpAgentQosCosTrafficInfoGroup"),
        ("ELTEX-FASTPATH-QOS-COS-MIB", "efpAgentQosCosTrafficInfoQueueGroup"))
)
if mibBuilder.loadTexts:
    efpQosCosCompliance2.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ELTEX-FASTPATH-QOS-COS-MIB",
    **{"eltFastpathQosCosMIB": eltFastpathQosCosMIB,
       "efpQosCosObjects": efpQosCosObjects,
       "efpQosCosStatistics": efpQosCosStatistics,
       "efpAgentCosTrafficInfoTable": efpAgentCosTrafficInfoTable,
       "efpAgentCosTrafficInfoEntry": efpAgentCosTrafficInfoEntry,
       "efpAgentCosTrafficInfoTotalPass": efpAgentCosTrafficInfoTotalPass,
       "efpAgentCosTrafficInfoTotalDrops": efpAgentCosTrafficInfoTotalDrops,
       "efpAgentCosTrafficInfoTxQueue": efpAgentCosTrafficInfoTxQueue,
       "efpAgentCosTrafficInfoRxQueue": efpAgentCosTrafficInfoRxQueue,
       "efpAgentCosTrafficInfoRedDrops": efpAgentCosTrafficInfoRedDrops,
       "efpAgentCosTrafficInfoYellowDrops": efpAgentCosTrafficInfoYellowDrops,
       "efpAgentCosTrafficInfoWredQueue": efpAgentCosTrafficInfoWredQueue,
       "efpAgentCosTrafficInfoQueueTable": efpAgentCosTrafficInfoQueueTable,
       "efpAgentCosTrafficInfoQueueEntry": efpAgentCosTrafficInfoQueueEntry,
       "efpAgentCosTrafficInfoQueueIndex": efpAgentCosTrafficInfoQueueIndex,
       "efpAgentCosTrafficInfoQueueName": efpAgentCosTrafficInfoQueueName,
       "efpAgentCosTrafficInfoQueueTotalPass": efpAgentCosTrafficInfoQueueTotalPass,
       "efpAgentCosTrafficInfoQueueTotalDrops": efpAgentCosTrafficInfoQueueTotalDrops,
       "efpAgentCosTrafficInfoQueueTxQueue": efpAgentCosTrafficInfoQueueTxQueue,
       "efpAgentCosTrafficInfoQueueWredQueue": efpAgentCosTrafficInfoQueueWredQueue,
       "efpQosCosNotifications": efpQosCosNotifications,
       "efpQosCosNotificationsPrefix": efpQosCosNotificationsPrefix,
       "efpQosCosConformance": efpQosCosConformance,
       "efpQosCosCompliances": efpQosCosCompliances,
       "efpQosCosCompliance": efpQosCosCompliance,
       "efpQosCosCompliance2": efpQosCosCompliance2,
       "efpQosCosGroups": efpQosCosGroups,
       "efpAgentQosCosTrafficInfoGroup": efpAgentQosCosTrafficInfoGroup,
       "efpAgentQosCosTrafficInfoQueueGroup": efpAgentQosCosTrafficInfoQueueGroup}
)
