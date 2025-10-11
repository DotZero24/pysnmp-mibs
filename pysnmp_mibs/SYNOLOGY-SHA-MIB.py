# SNMP MIB module (SYNOLOGY-SHA-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/synology/SYNOLOGY-SHA-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 18:58:19 2025
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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

synologyHA = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6574, 106)
)
if mibBuilder.loadTexts:
    synologyHA.setRevisions(
        ("2018-07-25 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class HostName(TextualConvention, OctetString):
    status = "current"
    displayHint = "255a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )



class ClusterStatusType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("warning", 1),
          ("critical", 2),
          ("upgrading", 3),
          ("processing", 4))
    )



class HeartbeatStatusType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("abnormal", 1),
          ("disconnected", 2),
          ("empty", 3))
    )



# MIB Managed Objects in the order of their OIDs

_Synology_ObjectIdentity = ObjectIdentity
synology = _Synology_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6574)
)
_ActiveNodeName_Type = HostName
_ActiveNodeName_Object = MibScalar
activeNodeName = _ActiveNodeName_Object(
    (1, 3, 6, 1, 4, 1, 6574, 106, 1),
    _ActiveNodeName_Type()
)
activeNodeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    activeNodeName.setStatus("current")
_PassiveNodeName_Type = HostName
_PassiveNodeName_Object = MibScalar
passiveNodeName = _PassiveNodeName_Object(
    (1, 3, 6, 1, 4, 1, 6574, 106, 2),
    _PassiveNodeName_Type()
)
passiveNodeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    passiveNodeName.setStatus("current")
_ClusterAutoFailover_Type = TruthValue
_ClusterAutoFailover_Object = MibScalar
clusterAutoFailover = _ClusterAutoFailover_Object(
    (1, 3, 6, 1, 4, 1, 6574, 106, 3),
    _ClusterAutoFailover_Type()
)
clusterAutoFailover.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterAutoFailover.setStatus("current")
_ClusterName_Type = HostName
_ClusterName_Object = MibScalar
clusterName = _ClusterName_Object(
    (1, 3, 6, 1, 4, 1, 6574, 106, 4),
    _ClusterName_Type()
)
clusterName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterName.setStatus("current")
_ClusterStatus_Type = ClusterStatusType
_ClusterStatus_Object = MibScalar
clusterStatus = _ClusterStatus_Object(
    (1, 3, 6, 1, 4, 1, 6574, 106, 5),
    _ClusterStatus_Type()
)
clusterStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterStatus.setStatus("current")
_HeartbeatStatus_Type = HeartbeatStatusType
_HeartbeatStatus_Object = MibScalar
heartbeatStatus = _HeartbeatStatus_Object(
    (1, 3, 6, 1, 4, 1, 6574, 106, 6),
    _HeartbeatStatus_Type()
)
heartbeatStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    heartbeatStatus.setStatus("current")
_HeartbeatTxRate_Type = Unsigned32
_HeartbeatTxRate_Object = MibScalar
heartbeatTxRate = _HeartbeatTxRate_Object(
    (1, 3, 6, 1, 4, 1, 6574, 106, 7),
    _HeartbeatTxRate_Type()
)
heartbeatTxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    heartbeatTxRate.setStatus("current")
_HeartbeatLatency_Type = Unsigned32
_HeartbeatLatency_Object = MibScalar
heartbeatLatency = _HeartbeatLatency_Object(
    (1, 3, 6, 1, 4, 1, 6574, 106, 8),
    _HeartbeatLatency_Type()
)
heartbeatLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    heartbeatLatency.setStatus("current")
_SynologyHAConformance_ObjectIdentity = ObjectIdentity
synologyHAConformance = _SynologyHAConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6574, 106, 9)
)
_SynologyHACompliances_ObjectIdentity = ObjectIdentity
synologyHACompliances = _SynologyHACompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6574, 106, 9, 1)
)
_SynologyHAGroups_ObjectIdentity = ObjectIdentity
synologyHAGroups = _SynologyHAGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6574, 106, 9, 2)
)

# Managed Objects groups

synologyHAGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6574, 106, 9, 2, 1)
)
synologyHAGroup.setObjects(
      *(("SYNOLOGY-SHA-MIB", "activeNodeName"),
        ("SYNOLOGY-SHA-MIB", "passiveNodeName"),
        ("SYNOLOGY-SHA-MIB", "clusterAutoFailover"),
        ("SYNOLOGY-SHA-MIB", "clusterName"),
        ("SYNOLOGY-SHA-MIB", "clusterStatus"),
        ("SYNOLOGY-SHA-MIB", "heartbeatStatus"),
        ("SYNOLOGY-SHA-MIB", "heartbeatTxRate"),
        ("SYNOLOGY-SHA-MIB", "heartbeatLatency"))
)
if mibBuilder.loadTexts:
    synologyHAGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

synologyHACompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6574, 106, 9, 1, 1)
)
synologyHACompliance.setObjects(
    ("SYNOLOGY-SHA-MIB", "synologyHAGroup")
)
if mibBuilder.loadTexts:
    synologyHACompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SYNOLOGY-SHA-MIB",
    **{"HostName": HostName,
       "ClusterStatusType": ClusterStatusType,
       "HeartbeatStatusType": HeartbeatStatusType,
       "synology": synology,
       "synologyHA": synologyHA,
       "activeNodeName": activeNodeName,
       "passiveNodeName": passiveNodeName,
       "clusterAutoFailover": clusterAutoFailover,
       "clusterName": clusterName,
       "clusterStatus": clusterStatus,
       "heartbeatStatus": heartbeatStatus,
       "heartbeatTxRate": heartbeatTxRate,
       "heartbeatLatency": heartbeatLatency,
       "synologyHAConformance": synologyHAConformance,
       "synologyHACompliances": synologyHACompliances,
       "synologyHACompliance": synologyHACompliance,
       "synologyHAGroups": synologyHAGroups,
       "synologyHAGroup": synologyHAGroup}
)
