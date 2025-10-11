# SNMP MIB module (RUCKUS-SCG-SYSTEM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/ruckus/RUCKUS-SCG-SYSTEM-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:13:44 2025
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

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex")

(ruckusSCGSystemModule,) = mibBuilder.importSymbols(
    "RUCKUS-ROOT-MIB",
    "ruckusSCGSystemModule")

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
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ruckusSystemMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 1, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RuckusSystemObjects_ObjectIdentity = ObjectIdentity
ruckusSystemObjects = _RuckusSystemObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 1, 1, 1)
)
_RuckusSystemStats_ObjectIdentity = ObjectIdentity
ruckusSystemStats = _RuckusSystemStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 1, 1, 1, 15)
)
_RuckusSystemStatsNumAP_Type = Unsigned32
_RuckusSystemStatsNumAP_Object = MibScalar
ruckusSystemStatsNumAP = _RuckusSystemStatsNumAP_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 1, 1, 1, 15, 1),
    _RuckusSystemStatsNumAP_Type()
)
ruckusSystemStatsNumAP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusSystemStatsNumAP.setStatus("current")
_RuckusSystemStatsNumSta_Type = Unsigned32
_RuckusSystemStatsNumSta_Object = MibScalar
ruckusSystemStatsNumSta = _RuckusSystemStatsNumSta_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 1, 1, 1, 15, 2),
    _RuckusSystemStatsNumSta_Type()
)
ruckusSystemStatsNumSta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusSystemStatsNumSta.setStatus("current")
_RuckusSystemStatsWLANTotalRxPkts_Type = Counter64
_RuckusSystemStatsWLANTotalRxPkts_Object = MibScalar
ruckusSystemStatsWLANTotalRxPkts = _RuckusSystemStatsWLANTotalRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 1, 1, 1, 15, 5),
    _RuckusSystemStatsWLANTotalRxPkts_Type()
)
ruckusSystemStatsWLANTotalRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusSystemStatsWLANTotalRxPkts.setStatus("current")
_RuckusSystemStatsWLANTotalRxBytes_Type = Counter64
_RuckusSystemStatsWLANTotalRxBytes_Object = MibScalar
ruckusSystemStatsWLANTotalRxBytes = _RuckusSystemStatsWLANTotalRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 1, 1, 1, 15, 6),
    _RuckusSystemStatsWLANTotalRxBytes_Type()
)
ruckusSystemStatsWLANTotalRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusSystemStatsWLANTotalRxBytes.setStatus("current")
_RuckusSystemStatsWLANTotalRxMulticast_Type = Counter64
_RuckusSystemStatsWLANTotalRxMulticast_Object = MibScalar
ruckusSystemStatsWLANTotalRxMulticast = _RuckusSystemStatsWLANTotalRxMulticast_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 1, 1, 1, 15, 7),
    _RuckusSystemStatsWLANTotalRxMulticast_Type()
)
ruckusSystemStatsWLANTotalRxMulticast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusSystemStatsWLANTotalRxMulticast.setStatus("current")
_RuckusSystemStatsWLANTotalTxPkts_Type = Counter64
_RuckusSystemStatsWLANTotalTxPkts_Object = MibScalar
ruckusSystemStatsWLANTotalTxPkts = _RuckusSystemStatsWLANTotalTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 1, 1, 1, 15, 8),
    _RuckusSystemStatsWLANTotalTxPkts_Type()
)
ruckusSystemStatsWLANTotalTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusSystemStatsWLANTotalTxPkts.setStatus("current")
_RuckusSystemStatsWLANTotalTxBytes_Type = Counter64
_RuckusSystemStatsWLANTotalTxBytes_Object = MibScalar
ruckusSystemStatsWLANTotalTxBytes = _RuckusSystemStatsWLANTotalTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 1, 1, 1, 15, 9),
    _RuckusSystemStatsWLANTotalTxBytes_Type()
)
ruckusSystemStatsWLANTotalTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusSystemStatsWLANTotalTxBytes.setStatus("current")
_RuckusSystemStatsWLANTotalTxMulticast_Type = Counter64
_RuckusSystemStatsWLANTotalTxMulticast_Object = MibScalar
ruckusSystemStatsWLANTotalTxMulticast = _RuckusSystemStatsWLANTotalTxMulticast_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 1, 1, 1, 15, 10),
    _RuckusSystemStatsWLANTotalTxMulticast_Type()
)
ruckusSystemStatsWLANTotalTxMulticast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusSystemStatsWLANTotalTxMulticast.setStatus("current")
_RuckusSystemStatsWLANTotalTxFail_Type = Counter64
_RuckusSystemStatsWLANTotalTxFail_Object = MibScalar
ruckusSystemStatsWLANTotalTxFail = _RuckusSystemStatsWLANTotalTxFail_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 1, 1, 1, 15, 11),
    _RuckusSystemStatsWLANTotalTxFail_Type()
)
ruckusSystemStatsWLANTotalTxFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusSystemStatsWLANTotalTxFail.setStatus("current")
_RuckusSystemStatsWLANTotalTxRetry_Type = Counter64
_RuckusSystemStatsWLANTotalTxRetry_Object = MibScalar
ruckusSystemStatsWLANTotalTxRetry = _RuckusSystemStatsWLANTotalTxRetry_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 1, 1, 1, 15, 12),
    _RuckusSystemStatsWLANTotalTxRetry_Type()
)
ruckusSystemStatsWLANTotalTxRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusSystemStatsWLANTotalTxRetry.setStatus("current")
_RuckusSystemStatsSerialNumber_Type = DisplayString
_RuckusSystemStatsSerialNumber_Object = MibScalar
ruckusSystemStatsSerialNumber = _RuckusSystemStatsSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 3, 1, 1, 1, 15, 13),
    _RuckusSystemStatsSerialNumber_Type()
)
ruckusSystemStatsSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusSystemStatsSerialNumber.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RUCKUS-SCG-SYSTEM-MIB",
    **{"ruckusSystemMIB": ruckusSystemMIB,
       "ruckusSystemObjects": ruckusSystemObjects,
       "ruckusSystemStats": ruckusSystemStats,
       "ruckusSystemStatsNumAP": ruckusSystemStatsNumAP,
       "ruckusSystemStatsNumSta": ruckusSystemStatsNumSta,
       "ruckusSystemStatsWLANTotalRxPkts": ruckusSystemStatsWLANTotalRxPkts,
       "ruckusSystemStatsWLANTotalRxBytes": ruckusSystemStatsWLANTotalRxBytes,
       "ruckusSystemStatsWLANTotalRxMulticast": ruckusSystemStatsWLANTotalRxMulticast,
       "ruckusSystemStatsWLANTotalTxPkts": ruckusSystemStatsWLANTotalTxPkts,
       "ruckusSystemStatsWLANTotalTxBytes": ruckusSystemStatsWLANTotalTxBytes,
       "ruckusSystemStatsWLANTotalTxMulticast": ruckusSystemStatsWLANTotalTxMulticast,
       "ruckusSystemStatsWLANTotalTxFail": ruckusSystemStatsWLANTotalTxFail,
       "ruckusSystemStatsWLANTotalTxRetry": ruckusSystemStatsWLANTotalTxRetry,
       "ruckusSystemStatsSerialNumber": ruckusSystemStatsSerialNumber}
)
