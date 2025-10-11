# SNMP MIB module (ELTEX-FASTPATH-SWITCHING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/eltex/ELTEX-FASTPATH-SWITCHING-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:50:07 2025
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

(eltMesFastpath,) = mibBuilder.importSymbols(
    "ELTEX-MES-FASTPATH-MIB",
    "eltMesFastpath")

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

eltFastpathSwitchingMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 103, 5)
)
if mibBuilder.loadTexts:
    eltFastpathSwitchingMIB.setRevisions(
        ("2018-02-26 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_EfpSwitchingObjects_ObjectIdentity = ObjectIdentity
efpSwitchingObjects = _EfpSwitchingObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 103, 5, 1)
)
_EfpSwitchingCpuTrafficGlobals_ObjectIdentity = ObjectIdentity
efpSwitchingCpuTrafficGlobals = _EfpSwitchingCpuTrafficGlobals_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 103, 5, 1, 1)
)
_EfpSwitchingCpuTrafficConfigs_ObjectIdentity = ObjectIdentity
efpSwitchingCpuTrafficConfigs = _EfpSwitchingCpuTrafficConfigs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 103, 5, 1, 2)
)
_EfpAgentCpuTrafficRateLimitQueueTable_Object = MibTable
efpAgentCpuTrafficRateLimitQueueTable = _EfpAgentCpuTrafficRateLimitQueueTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 103, 5, 1, 2, 1)
)
if mibBuilder.loadTexts:
    efpAgentCpuTrafficRateLimitQueueTable.setStatus("current")
_EfpAgentCpuTrafficRateLimitQueueEntry_Object = MibTableRow
efpAgentCpuTrafficRateLimitQueueEntry = _EfpAgentCpuTrafficRateLimitQueueEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 103, 5, 1, 2, 1, 1)
)
efpAgentCpuTrafficRateLimitQueueEntry.setIndexNames(
    (0, "ELTEX-FASTPATH-SWITCHING-MIB", "efpAgentCpuTrafficRateLimitQueueNumber"),
)
if mibBuilder.loadTexts:
    efpAgentCpuTrafficRateLimitQueueEntry.setStatus("current")
_EfpAgentCpuTrafficRateLimitQueueNumber_Type = Integer32
_EfpAgentCpuTrafficRateLimitQueueNumber_Object = MibTableColumn
efpAgentCpuTrafficRateLimitQueueNumber = _EfpAgentCpuTrafficRateLimitQueueNumber_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 103, 5, 1, 2, 1, 1, 1),
    _EfpAgentCpuTrafficRateLimitQueueNumber_Type()
)
efpAgentCpuTrafficRateLimitQueueNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    efpAgentCpuTrafficRateLimitQueueNumber.setStatus("current")


class _EfpAgentCpuTrafficRateLimitQueueLimit_Type(Integer32):
    """Custom type efpAgentCpuTrafficRateLimitQueueLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(8, 2048),
    )


_EfpAgentCpuTrafficRateLimitQueueLimit_Type.__name__ = "Integer32"
_EfpAgentCpuTrafficRateLimitQueueLimit_Object = MibTableColumn
efpAgentCpuTrafficRateLimitQueueLimit = _EfpAgentCpuTrafficRateLimitQueueLimit_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 103, 5, 1, 2, 1, 1, 2),
    _EfpAgentCpuTrafficRateLimitQueueLimit_Type()
)
efpAgentCpuTrafficRateLimitQueueLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    efpAgentCpuTrafficRateLimitQueueLimit.setStatus("current")
_EfpSwitchingCpuTrafficStatistics_ObjectIdentity = ObjectIdentity
efpSwitchingCpuTrafficStatistics = _EfpSwitchingCpuTrafficStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 103, 5, 1, 3)
)
_EfpAgentCpuTrafficRateLimitQueueStatTable_Object = MibTable
efpAgentCpuTrafficRateLimitQueueStatTable = _EfpAgentCpuTrafficRateLimitQueueStatTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 103, 5, 1, 3, 1)
)
if mibBuilder.loadTexts:
    efpAgentCpuTrafficRateLimitQueueStatTable.setStatus("current")
_EfpAgentCpuTrafficRateLimitQueueStatEntry_Object = MibTableRow
efpAgentCpuTrafficRateLimitQueueStatEntry = _EfpAgentCpuTrafficRateLimitQueueStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 103, 5, 1, 3, 1, 1)
)
efpAgentCpuTrafficRateLimitQueueStatEntry.setIndexNames(
    (0, "ELTEX-FASTPATH-SWITCHING-MIB", "efpAgentCpuTrafficRateLimitQueueNumber"),
)
if mibBuilder.loadTexts:
    efpAgentCpuTrafficRateLimitQueueStatEntry.setStatus("current")
_EfpAgentCpuTrafficRateLimitQueueRate_Type = Integer32
_EfpAgentCpuTrafficRateLimitQueueRate_Object = MibTableColumn
efpAgentCpuTrafficRateLimitQueueRate = _EfpAgentCpuTrafficRateLimitQueueRate_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 103, 5, 1, 3, 1, 1, 1),
    _EfpAgentCpuTrafficRateLimitQueueRate_Type()
)
efpAgentCpuTrafficRateLimitQueueRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    efpAgentCpuTrafficRateLimitQueueRate.setStatus("current")
_EfpAgentCpuTrafficRateLimitQueuePackets_Type = Integer32
_EfpAgentCpuTrafficRateLimitQueuePackets_Object = MibTableColumn
efpAgentCpuTrafficRateLimitQueuePackets = _EfpAgentCpuTrafficRateLimitQueuePackets_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 103, 5, 1, 3, 1, 1, 2),
    _EfpAgentCpuTrafficRateLimitQueuePackets_Type()
)
efpAgentCpuTrafficRateLimitQueuePackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    efpAgentCpuTrafficRateLimitQueuePackets.setStatus("current")
_EfpSwitchingNotifications_ObjectIdentity = ObjectIdentity
efpSwitchingNotifications = _EfpSwitchingNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 103, 5, 2)
)
_EfpSwitchingNotificationsPrefix_ObjectIdentity = ObjectIdentity
efpSwitchingNotificationsPrefix = _EfpSwitchingNotificationsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 103, 5, 2, 0)
)
_EfpSwitchingConformance_ObjectIdentity = ObjectIdentity
efpSwitchingConformance = _EfpSwitchingConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 103, 5, 3)
)
_EfpSwitchingCompliances_ObjectIdentity = ObjectIdentity
efpSwitchingCompliances = _EfpSwitchingCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 103, 5, 3, 1)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ELTEX-FASTPATH-SWITCHING-MIB",
    **{"eltFastpathSwitchingMIB": eltFastpathSwitchingMIB,
       "efpSwitchingObjects": efpSwitchingObjects,
       "efpSwitchingCpuTrafficGlobals": efpSwitchingCpuTrafficGlobals,
       "efpSwitchingCpuTrafficConfigs": efpSwitchingCpuTrafficConfigs,
       "efpAgentCpuTrafficRateLimitQueueTable": efpAgentCpuTrafficRateLimitQueueTable,
       "efpAgentCpuTrafficRateLimitQueueEntry": efpAgentCpuTrafficRateLimitQueueEntry,
       "efpAgentCpuTrafficRateLimitQueueNumber": efpAgentCpuTrafficRateLimitQueueNumber,
       "efpAgentCpuTrafficRateLimitQueueLimit": efpAgentCpuTrafficRateLimitQueueLimit,
       "efpSwitchingCpuTrafficStatistics": efpSwitchingCpuTrafficStatistics,
       "efpAgentCpuTrafficRateLimitQueueStatTable": efpAgentCpuTrafficRateLimitQueueStatTable,
       "efpAgentCpuTrafficRateLimitQueueStatEntry": efpAgentCpuTrafficRateLimitQueueStatEntry,
       "efpAgentCpuTrafficRateLimitQueueRate": efpAgentCpuTrafficRateLimitQueueRate,
       "efpAgentCpuTrafficRateLimitQueuePackets": efpAgentCpuTrafficRateLimitQueuePackets,
       "efpSwitchingNotifications": efpSwitchingNotifications,
       "efpSwitchingNotificationsPrefix": efpSwitchingNotificationsPrefix,
       "efpSwitchingConformance": efpSwitchingConformance,
       "efpSwitchingCompliances": efpSwitchingCompliances}
)
