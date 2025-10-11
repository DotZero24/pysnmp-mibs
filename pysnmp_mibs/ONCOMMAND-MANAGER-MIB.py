# SNMP MIB module (ONCOMMAND-MANAGER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/netapp/ONCOMMAND-MANAGER-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:07:33 2025
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

(netappOnCommand,) = mibBuilder.importSymbols(
    "NETAPP-MIB",
    "netappOnCommand")

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


# Types definitions



class DisplayString(OctetString):
    """Custom type DisplayString based on OctetString"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NetappOnCommandUnifiedManager_ObjectIdentity = ObjectIdentity
netappOnCommandUnifiedManager = _NetappOnCommandUnifiedManager_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 789, 5, 1)
)
_OcumSystemId_Type = DisplayString
_OcumSystemId_Object = MibScalar
ocumSystemId = _OcumSystemId_Object(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 1),
    _OcumSystemId_Type()
)
ocumSystemId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocumSystemId.setStatus("mandatory")
_OcumEvent_ObjectIdentity = ObjectIdentity
ocumEvent = _OcumEvent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 2)
)
_OcumEventName_Type = DisplayString
_OcumEventName_Object = MibScalar
ocumEventName = _OcumEventName_Object(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 2, 1),
    _OcumEventName_Type()
)
ocumEventName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocumEventName.setStatus("mandatory")


class _OcumEventSeverity_Type(Integer32):
    """Custom type ocumEventSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("warning", 3),
          ("error", 4),
          ("critical", 5))
    )


_OcumEventSeverity_Type.__name__ = "Integer32"
_OcumEventSeverity_Object = MibScalar
ocumEventSeverity = _OcumEventSeverity_Object(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 2, 2),
    _OcumEventSeverity_Type()
)
ocumEventSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocumEventSeverity.setStatus("mandatory")


class _OcumEventImpactLevel_Type(Integer32):
    """Custom type ocumEventImpactLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("event", 1),
          ("risk", 2),
          ("incident", 3))
    )


_OcumEventImpactLevel_Type.__name__ = "Integer32"
_OcumEventImpactLevel_Object = MibScalar
ocumEventImpactLevel = _OcumEventImpactLevel_Object(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 2, 3),
    _OcumEventImpactLevel_Type()
)
ocumEventImpactLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocumEventImpactLevel.setStatus("mandatory")
_OcumEventTimestamp_Type = Integer32
_OcumEventTimestamp_Object = MibScalar
ocumEventTimestamp = _OcumEventTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 2, 4),
    _OcumEventTimestamp_Type()
)
ocumEventTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocumEventTimestamp.setStatus("mandatory")
_OcumEventMessage_Type = DisplayString
_OcumEventMessage_Object = MibScalar
ocumEventMessage = _OcumEventMessage_Object(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 2, 5),
    _OcumEventMessage_Type()
)
ocumEventMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocumEventMessage.setStatus("mandatory")
_OcumEventMessageDetails_Type = DisplayString
_OcumEventMessageDetails_Object = MibScalar
ocumEventMessageDetails = _OcumEventMessageDetails_Object(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 2, 6),
    _OcumEventMessageDetails_Type()
)
ocumEventMessageDetails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocumEventMessageDetails.setStatus("mandatory")
_OcumEventSourceResourceKey_Type = DisplayString
_OcumEventSourceResourceKey_Object = MibScalar
ocumEventSourceResourceKey = _OcumEventSourceResourceKey_Object(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 2, 7),
    _OcumEventSourceResourceKey_Type()
)
ocumEventSourceResourceKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocumEventSourceResourceKey.setStatus("optional")
_OcumEventSourceFullName_Type = DisplayString
_OcumEventSourceFullName_Object = MibScalar
ocumEventSourceFullName = _OcumEventSourceFullName_Object(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 2, 8),
    _OcumEventSourceFullName_Type()
)
ocumEventSourceFullName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocumEventSourceFullName.setStatus("mandatory")


class _OcumEventSourceType_Type(Integer32):
    """Custom type ocumEventSourceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              32)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("mgmtStation", 2),
          ("cluster", 3),
          ("clusterNode", 4),
          ("vserver", 5),
          ("volume", 6),
          ("qtree", 7),
          ("lun", 8),
          ("aggregate", 9),
          ("disk", 10),
          ("port", 11),
          ("lif", 12),
          ("storageService", 13),
          ("igroup", 14),
          ("fcpTarget", 15),
          ("mirror", 16),
          ("portSet", 17),
          ("exportPolicy", 18),
          ("userQuota", 19),
          ("storageClass", 20),
          ("switch", 21),
          ("bridge", 22),
          ("nodeSwitchConnection", 23),
          ("metroClusterRelationship", 24),
          ("interSwitchConnection", 25),
          ("switchBridgeConnection", 26),
          ("bridgeStackConnection", 27),
          ("interNodeConnection", 28),
          ("nodeBridgeConnection", 29),
          ("nodeStackConnection", 30),
          ("objectstoreConfig", 32))
    )


_OcumEventSourceType_Type.__name__ = "Integer32"
_OcumEventSourceType_Object = MibScalar
ocumEventSourceType = _OcumEventSourceType_Object(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 2, 9),
    _OcumEventSourceType_Type()
)
ocumEventSourceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocumEventSourceType.setStatus("mandatory")


class _OcumEventSourceHealthStatus_Type(Integer32):
    """Custom type ocumEventSourceHealthStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("warning", 2),
          ("error", 3),
          ("critical", 4))
    )


_OcumEventSourceHealthStatus_Type.__name__ = "Integer32"
_OcumEventSourceHealthStatus_Object = MibScalar
ocumEventSourceHealthStatus = _OcumEventSourceHealthStatus_Object(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 2, 10),
    _OcumEventSourceHealthStatus_Type()
)
ocumEventSourceHealthStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocumEventSourceHealthStatus.setStatus("mandatory")
_OcumEventSourceScopedResourceKey_Type = DisplayString
_OcumEventSourceScopedResourceKey_Object = MibScalar
ocumEventSourceScopedResourceKey = _OcumEventSourceScopedResourceKey_Object(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 2, 11),
    _OcumEventSourceScopedResourceKey_Type()
)
ocumEventSourceScopedResourceKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocumEventSourceScopedResourceKey.setStatus("mandatory")
_OcumEventSourceScopedFullName_Type = DisplayString
_OcumEventSourceScopedFullName_Object = MibScalar
ocumEventSourceScopedFullName = _OcumEventSourceScopedFullName_Object(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 2, 12),
    _OcumEventSourceScopedFullName_Type()
)
ocumEventSourceScopedFullName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocumEventSourceScopedFullName.setStatus("mandatory")
_OcumEventSourceClusterResourceKey_Type = DisplayString
_OcumEventSourceClusterResourceKey_Object = MibScalar
ocumEventSourceClusterResourceKey = _OcumEventSourceClusterResourceKey_Object(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 2, 13),
    _OcumEventSourceClusterResourceKey_Type()
)
ocumEventSourceClusterResourceKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocumEventSourceClusterResourceKey.setStatus("mandatory")
_OcumEventSourceClusterFullName_Type = DisplayString
_OcumEventSourceClusterFullName_Object = MibScalar
ocumEventSourceClusterFullName = _OcumEventSourceClusterFullName_Object(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 2, 14),
    _OcumEventSourceClusterFullName_Type()
)
ocumEventSourceClusterFullName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocumEventSourceClusterFullName.setStatus("mandatory")


class _OcumEventState_Type(Integer32):
    """Custom type ocumEventState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("new", 1),
          ("acknowledged", 2),
          ("resolved", 3),
          ("obsolete_um", 4))
    )


_OcumEventState_Type.__name__ = "Integer32"
_OcumEventState_Object = MibScalar
ocumEventState = _OcumEventState_Object(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 2, 15),
    _OcumEventState_Type()
)
ocumEventState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocumEventState.setStatus("mandatory")
_OcumTestAlert_ObjectIdentity = ObjectIdentity
ocumTestAlert = _OcumTestAlert_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 3)
)
_OcumTestAlertTimestamp_Type = Integer32
_OcumTestAlertTimestamp_Object = MibScalar
ocumTestAlertTimestamp = _OcumTestAlertTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 3, 1),
    _OcumTestAlertTimestamp_Type()
)
ocumTestAlertTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocumTestAlertTimestamp.setStatus("mandatory")

# Managed Objects groups


# Notification objects

ocumAlertTest = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 11111)
)
ocumAlertTest.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumTestAlertTimestamp"))
)
if mibBuilder.loadTexts:
    ocumAlertTest.setStatus(
        ""
    )

ocumEvtAggregate64BitUpgrade = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 13000)
)
ocumEvtAggregate64BitUpgrade.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtAggregate64BitUpgrade.setStatus(
        ""
    )

ocumEvtAggregateDiscovered = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 13010)
)
ocumEvtAggregateDiscovered.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtAggregateDiscovered.setStatus(
        ""
    )

ocumEvtAggregateStateFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 13020)
)
ocumEvtAggregateStateFailed.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtAggregateStateFailed.setStatus(
        ""
    )

ocumEvtAggregateStateRestricted = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 13021)
)
ocumEvtAggregateStateRestricted.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtAggregateStateRestricted.setStatus(
        ""
    )

ocumEvtAggregateStateOnline = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 13022)
)
ocumEvtAggregateStateOnline.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtAggregateStateOnline.setStatus(
        ""
    )

ocumEvtAggregateStateOffline = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 13023)
)
ocumEvtAggregateStateOffline.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtAggregateStateOffline.setStatus(
        ""
    )

ocumEvtAggregateRaidStateNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 13030)
)
ocumEvtAggregateRaidStateNormal.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtAggregateRaidStateNormal.setStatus(
        ""
    )

ocumEvtAggregateRaidStateDegraded = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 13031)
)
ocumEvtAggregateRaidStateDegraded.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtAggregateRaidStateDegraded.setStatus(
        ""
    )

ocumEvtAggregateRaidStateReconstructing = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 13032)
)
ocumEvtAggregateRaidStateReconstructing.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtAggregateRaidStateReconstructing.setStatus(
        ""
    )

ocumEvtAggregateSpaceOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 13040)
)
ocumEvtAggregateSpaceOk.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtAggregateSpaceOk.setStatus(
        ""
    )

ocumEvtAggregateNearlyFull = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 13041)
)
ocumEvtAggregateNearlyFull.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtAggregateNearlyFull.setStatus(
        ""
    )

ocumEvtAggregateFull = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 13042)
)
ocumEvtAggregateFull.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtAggregateFull.setStatus(
        ""
    )

ocumEvtAggregateDaysUntilFullNotSoon = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 13050)
)
ocumEvtAggregateDaysUntilFullNotSoon.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtAggregateDaysUntilFullNotSoon.setStatus(
        ""
    )

ocumEvtAggregateDaysUntilFullSoon = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 13051)
)
ocumEvtAggregateDaysUntilFullSoon.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtAggregateDaysUntilFullSoon.setStatus(
        ""
    )

ocumEvtAggregateNotOvercommited = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 13060)
)
ocumEvtAggregateNotOvercommited.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtAggregateNotOvercommited.setStatus(
        ""
    )

ocumEvtAggregateAlmostOvercommitted = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 13061)
)
ocumEvtAggregateAlmostOvercommitted.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtAggregateAlmostOvercommitted.setStatus(
        ""
    )

ocumEvtAggregateOvercommitted = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 13062)
)
ocumEvtAggregateOvercommitted.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtAggregateOvercommitted.setStatus(
        ""
    )

ocumEvtAggregateSnapReserveOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 13070)
)
ocumEvtAggregateSnapReserveOk.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtAggregateSnapReserveOk.setStatus(
        ""
    )

ocumEvtAggregateSnapReserveFull = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 13071)
)
ocumEvtAggregateSnapReserveFull.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtAggregateSnapReserveFull.setStatus(
        ""
    )

ocumEvtAggregateGrowthRateOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 13080)
)
ocumEvtAggregateGrowthRateOk.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtAggregateGrowthRateOk.setStatus(
        ""
    )

ocumEvtAggregateGrowthRateAbnormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 13081)
)
ocumEvtAggregateGrowthRateAbnormal.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtAggregateGrowthRateAbnormal.setStatus(
        ""
    )

ocumEvtAggregateDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 13090)
)
ocumEvtAggregateDeleted.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtAggregateDeleted.setStatus(
        ""
    )

ocumEvtAggregateRenamed = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 13100)
)
ocumEvtAggregateRenamed.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtAggregateRenamed.setStatus(
        ""
    )

ocumEvtMetroClusterAggregateLeftBehindFixed = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 13110)
)
ocumEvtMetroClusterAggregateLeftBehindFixed.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtMetroClusterAggregateLeftBehindFixed.setStatus(
        ""
    )

ocumEvtMetroClusterAggregateLeftBehind = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 13111)
)
ocumEvtMetroClusterAggregateLeftBehind.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtMetroClusterAggregateLeftBehind.setStatus(
        ""
    )

ocumEvtClusterUnassignedDisksNone = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 13210)
)
ocumEvtClusterUnassignedDisksNone.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtClusterUnassignedDisksNone.setStatus(
        ""
    )

ocumEvtClusterUnassignedDisksSome = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 13211)
)
ocumEvtClusterUnassignedDisksSome.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtClusterUnassignedDisksSome.setStatus(
        ""
    )

ocumEvtDisksSparesAvailable = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 13220)
)
ocumEvtDisksSparesAvailable.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtDisksSparesAvailable.setStatus(
        ""
    )

ocumEvtDisksNoSpares = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 13221)
)
ocumEvtDisksNoSpares.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtDisksNoSpares.setStatus(
        ""
    )

ocumEvtDisksNoneFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 13230)
)
ocumEvtDisksNoneFailed.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtDisksNoneFailed.setStatus(
        ""
    )

ocumEvtDisksSomeFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 13231)
)
ocumEvtDisksSomeFailed.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtDisksSomeFailed.setStatus(
        ""
    )

ocumEvtClusterRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 13240)
)
ocumEvtClusterRemoved.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtClusterRemoved.setStatus(
        ""
    )

ocumEvtClusterAddFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 13241)
)
ocumEvtClusterAddFailed.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtClusterAddFailed.setStatus(
        ""
    )

ocumEvtClusterRenamed = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 13250)
)
ocumEvtClusterRenamed.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtClusterRenamed.setStatus(
        ""
    )

ocumEvtClusterReachable = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 13270)
)
ocumEvtClusterReachable.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtClusterReachable.setStatus(
        ""
    )

ocumEvtClusterUnreachable = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 13271)
)
ocumEvtClusterUnreachable.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtClusterUnreachable.setStatus(
        ""
    )

ocumEvtClusterMonitoringSucceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 13280)
)
ocumEvtClusterMonitoringSucceeded.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtClusterMonitoringSucceeded.setStatus(
        ""
    )

ocumEvtClusterMonitoringFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 13281)
)
ocumEvtClusterMonitoringFailed.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtClusterMonitoringFailed.setStatus(
        ""
    )

ocumEvtClusterUnsupportedDisksNone = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 13360)
)
ocumEvtClusterUnsupportedDisksNone.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtClusterUnsupportedDisksNone.setStatus(
        ""
    )

ocumEvtClusterUnsupportedDisksSome = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 13361)
)
ocumEvtClusterUnsupportedDisksSome.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtClusterUnsupportedDisksSome.setStatus(
        ""
    )

ocumEvtClusterNodeAdded = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 13400)
)
ocumEvtClusterNodeAdded.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtClusterNodeAdded.setStatus(
        ""
    )

ocumEvtClusterNodeRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 13410)
)
ocumEvtClusterNodeRemoved.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtClusterNodeRemoved.setStatus(
        ""
    )

ocumEvtClusterNodeRenamed = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 13411)
)
ocumEvtClusterNodeRenamed.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtClusterNodeRenamed.setStatus(
        ""
    )

ocumEvtSfoInterconnectUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 13420)
)
ocumEvtSfoInterconnectUp.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtSfoInterconnectUp.setStatus(
        ""
    )

ocumEvtSfoInterconnectOneOrMoreLinksDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 13421)
)
ocumEvtSfoInterconnectOneOrMoreLinksDown.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtSfoInterconnectOneOrMoreLinksDown.setStatus(
        ""
    )

ocumEvtSfoSettingsEnabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 13430)
)
ocumEvtSfoSettingsEnabled.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtSfoSettingsEnabled.setStatus(
        ""
    )

ocumEvtSfoSettingsNotConfigured = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 13431)
)
ocumEvtSfoSettingsNotConfigured.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtSfoSettingsNotConfigured.setStatus(
        ""
    )

ocumEvtSfoSettingsDisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 13432)
)
ocumEvtSfoSettingsDisabled.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtSfoSettingsDisabled.setStatus(
        ""
    )

ocumEvtSfoStateConnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 13440)
)
ocumEvtSfoStateConnected.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtSfoStateConnected.setStatus(
        ""
    )

ocumEvtSfoStateTakeover = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 13441)
)
ocumEvtSfoStateTakeover.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtSfoStateTakeover.setStatus(
        ""
    )

ocumEvtSfoStatePartialGiveback = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 13442)
)
ocumEvtSfoStatePartialGiveback.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtSfoStatePartialGiveback.setStatus(
        ""
    )

ocumEvtSfoNodeStatusUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 13450)
)
ocumEvtSfoNodeStatusUp.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtSfoNodeStatusUp.setStatus(
        ""
    )

ocumEvtSfoNodeStatusDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 13451)
)
ocumEvtSfoNodeStatusDown.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtSfoNodeStatusDown.setStatus(
        ""
    )

ocumEvtSfoTakeoverPossible = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 13460)
)
ocumEvtSfoTakeoverPossible.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtSfoTakeoverPossible.setStatus(
        ""
    )

ocumEvtSfoTakeoverNotPossible = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 13461)
)
ocumEvtSfoTakeoverNotPossible.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtSfoTakeoverNotPossible.setStatus(
        ""
    )

ocumEvtFansNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 13470)
)
ocumEvtFansNormal.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtFansNormal.setStatus(
        ""
    )

ocumEvtFansOneOrMoreFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 13471)
)
ocumEvtFansOneOrMoreFailed.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtFansOneOrMoreFailed.setStatus(
        ""
    )

ocumEvtNvramBatteryOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 13480)
)
ocumEvtNvramBatteryOk.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtNvramBatteryOk.setStatus(
        ""
    )

ocumEvtNvramBatteryLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 13481)
)
ocumEvtNvramBatteryLow.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtNvramBatteryLow.setStatus(
        ""
    )

ocumEvtNvramBatteryOverCharged = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 13482)
)
ocumEvtNvramBatteryOverCharged.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtNvramBatteryOverCharged.setStatus(
        ""
    )

ocumEvtNvramBatteryDischarged = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 13483)
)
ocumEvtNvramBatteryDischarged.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtNvramBatteryDischarged.setStatus(
        ""
    )

ocumEvtPowerSupplyOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 13490)
)
ocumEvtPowerSupplyOk.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtPowerSupplyOk.setStatus(
        ""
    )

ocumEvtPowerSupplyOneOrMoreFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 13491)
)
ocumEvtPowerSupplyOneOrMoreFailed.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtPowerSupplyOneOrMoreFailed.setStatus(
        ""
    )

ocumEvtClusterNodeRootVolumeSpaceOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 13500)
)
ocumEvtClusterNodeRootVolumeSpaceOk.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtClusterNodeRootVolumeSpaceOk.setStatus(
        ""
    )

ocumEvtClusterNodeRootVolumeSpaceNearlyFull = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 13501)
)
ocumEvtClusterNodeRootVolumeSpaceNearlyFull.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtClusterNodeRootVolumeSpaceNearlyFull.setStatus(
        ""
    )

ocumEvtPortStatusUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 13510)
)
ocumEvtPortStatusUp.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtPortStatusUp.setStatus(
        ""
    )

ocumEvtPortStatusDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 13511)
)
ocumEvtPortStatusDown.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtPortStatusDown.setStatus(
        ""
    )

ocumEvtFlashCardOnline = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 13520)
)
ocumEvtFlashCardOnline.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtFlashCardOnline.setStatus(
        ""
    )

ocumEvtFlashCardOffline = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 13521)
)
ocumEvtFlashCardOffline.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtFlashCardOffline.setStatus(
        ""
    )

ocumEvtServiceProcessorOnline = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 13522)
)
ocumEvtServiceProcessorOnline.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtServiceProcessorOnline.setStatus(
        ""
    )

ocumEvtServiceProcessorOffline = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 13523)
)
ocumEvtServiceProcessorOffline.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtServiceProcessorOffline.setStatus(
        ""
    )

ocumEvtServiceProcessorNotConfigured = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 13524)
)
ocumEvtServiceProcessorNotConfigured.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtServiceProcessorNotConfigured.setStatus(
        ""
    )

ocumEvtEfficiencyPolicyEnabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 13600)
)
ocumEvtEfficiencyPolicyEnabled.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtEfficiencyPolicyEnabled.setStatus(
        ""
    )

ocumEvtEfficiencyPolicyDisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 13601)
)
ocumEvtEfficiencyPolicyDisabled.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtEfficiencyPolicyDisabled.setStatus(
        ""
    )

ocumEvtLifStatusUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 13700)
)
ocumEvtLifStatusUp.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtLifStatusUp.setStatus(
        ""
    )

ocumEvtLifStatusDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 13701)
)
ocumEvtLifStatusDown.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtLifStatusDown.setStatus(
        ""
    )

ocumEvtLifMigrated = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 13702)
)
ocumEvtLifMigrated.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtLifMigrated.setStatus(
        ""
    )

ocumEvtLifFailoverPossible = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 13703)
)
ocumEvtLifFailoverPossible.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtLifFailoverPossible.setStatus(
        ""
    )

ocumEvtLifFailoverNotPossible = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 13704)
)
ocumEvtLifFailoverNotPossible.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtLifFailoverNotPossible.setStatus(
        ""
    )

ocumEvtLifNoRouteConfigured = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 13705)
)
ocumEvtLifNoRouteConfigured.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtLifNoRouteConfigured.setStatus(
        ""
    )

ocumEvtLifNotAtHomePort = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 13706)
)
ocumEvtLifNotAtHomePort.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtLifNotAtHomePort.setStatus(
        ""
    )

ocumEvtLifAtHomePort = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 13707)
)
ocumEvtLifAtHomePort.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtLifAtHomePort.setStatus(
        ""
    )

ocumEvtLunSnapshotOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 13800)
)
ocumEvtLunSnapshotOk.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtLunSnapshotOk.setStatus(
        ""
    )

ocumEvtLunSnapshotNotPossible = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 13801)
)
ocumEvtLunSnapshotNotPossible.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtLunSnapshotNotPossible.setStatus(
        ""
    )

ocumEvtLunSpaceReservationEnabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 13810)
)
ocumEvtLunSpaceReservationEnabled.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtLunSpaceReservationEnabled.setStatus(
        ""
    )

ocumEvtLunSpaceReservationDisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 13811)
)
ocumEvtLunSpaceReservationDisabled.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtLunSpaceReservationDisabled.setStatus(
        ""
    )

ocumEvtLunOnline = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 13820)
)
ocumEvtLunOnline.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtLunOnline.setStatus(
        ""
    )

ocumEvtLunOffline = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 13821)
)
ocumEvtLunOffline.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtLunOffline.setStatus(
        ""
    )

ocumEvtLunMultipleActivePath = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 13830)
)
ocumEvtLunMultipleActivePath.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtLunMultipleActivePath.setStatus(
        ""
    )

ocumEvtLunSingleActivePath = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 13831)
)
ocumEvtLunSingleActivePath.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtLunSingleActivePath.setStatus(
        ""
    )

ocumEvtLunReachable = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 13840)
)
ocumEvtLunReachable.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtLunReachable.setStatus(
        ""
    )

ocumEvtLunNotReachable = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 13841)
)
ocumEvtLunNotReachable.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtLunNotReachable.setStatus(
        ""
    )

ocumEvtLunOptimizedPathActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 13850)
)
ocumEvtLunOptimizedPathActive.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtLunOptimizedPathActive.setStatus(
        ""
    )

ocumEvtLunOptimizedPathInactive = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 13851)
)
ocumEvtLunOptimizedPathInactive.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtLunOptimizedPathInactive.setStatus(
        ""
    )

ocumEvtAlertCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 13900)
)
ocumEvtAlertCreated.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtAlertCreated.setStatus(
        ""
    )

ocumEvtAlertDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 13910)
)
ocumEvtAlertDeleted.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtAlertDeleted.setStatus(
        ""
    )

ocumEvtAlertModified = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 13920)
)
ocumEvtAlertModified.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtAlertModified.setStatus(
        ""
    )

ocumEvtQtreeFilesOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 14100)
)
ocumEvtQtreeFilesOk.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtQtreeFilesOk.setStatus(
        ""
    )

ocumEvtQtreeFilesSoftLimitBreached = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 14101)
)
ocumEvtQtreeFilesSoftLimitBreached.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtQtreeFilesSoftLimitBreached.setStatus(
        ""
    )

ocumEvtQtreeFilesHardLimitReached = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 14102)
)
ocumEvtQtreeFilesHardLimitReached.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtQtreeFilesHardLimitReached.setStatus(
        ""
    )

ocumEvtQtreeSpaceOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 14110)
)
ocumEvtQtreeSpaceOk.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtQtreeSpaceOk.setStatus(
        ""
    )

ocumEvtQtreeSpaceSoftLimitBreached = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 14111)
)
ocumEvtQtreeSpaceSoftLimitBreached.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtQtreeSpaceSoftLimitBreached.setStatus(
        ""
    )

ocumEvtQtreeSpaceHardLimitReached = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 14112)
)
ocumEvtQtreeSpaceHardLimitReached.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtQtreeSpaceHardLimitReached.setStatus(
        ""
    )

ocumEvtQtreeSpaceFull = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 14120)
)
ocumEvtQtreeSpaceFull.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtQtreeSpaceFull.setStatus(
        ""
    )

ocumEvtQtreeSpaceNearlyFull = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 14121)
)
ocumEvtQtreeSpaceNearlyFull.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtQtreeSpaceNearlyFull.setStatus(
        ""
    )

ocumEvtQtreeSpaceThresholdOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 14122)
)
ocumEvtQtreeSpaceThresholdOk.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtQtreeSpaceThresholdOk.setStatus(
        ""
    )

ocumEvtSnapshotPolicyEnabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 14200)
)
ocumEvtSnapshotPolicyEnabled.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtSnapshotPolicyEnabled.setStatus(
        ""
    )

ocumEvtSnapshotPolicyDisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 14201)
)
ocumEvtSnapshotPolicyDisabled.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtSnapshotPolicyDisabled.setStatus(
        ""
    )

ocumEvtSnapshotPolicyCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 14202)
)
ocumEvtSnapshotPolicyCreated.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtSnapshotPolicyCreated.setStatus(
        ""
    )

ocumEvtSnapshotPolicyDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 14210)
)
ocumEvtSnapshotPolicyDeleted.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtSnapshotPolicyDeleted.setStatus(
        ""
    )

ocumEvtSnapshotPolicyScheduleAdded = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 14220)
)
ocumEvtSnapshotPolicyScheduleAdded.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtSnapshotPolicyScheduleAdded.setStatus(
        ""
    )

ocumEvtSnapshotPolicyScheduleModified = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 14221)
)
ocumEvtSnapshotPolicyScheduleModified.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtSnapshotPolicyScheduleModified.setStatus(
        ""
    )

ocumEvtSnapshotPolicyScheduleRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 14222)
)
ocumEvtSnapshotPolicyScheduleRemoved.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtSnapshotPolicyScheduleRemoved.setStatus(
        ""
    )

ocumEvtStorageServiceCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 14300)
)
ocumEvtStorageServiceCreated.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtStorageServiceCreated.setStatus(
        ""
    )

ocumEvtStorageServiceSubscribed = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 14310)
)
ocumEvtStorageServiceSubscribed.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtStorageServiceSubscribed.setStatus(
        ""
    )

ocumEvtStorageServiceUnsubscribed = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 14320)
)
ocumEvtStorageServiceUnsubscribed.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtStorageServiceUnsubscribed.setStatus(
        ""
    )

ocumEvtStorageServiceUnexpectedRelationshipDeletion = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 14330)
)
ocumEvtStorageServiceUnexpectedRelationshipDeletion.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtStorageServiceUnexpectedRelationshipDeletion.setStatus(
        ""
    )

ocumEvtStorageServiceUnexpectedVolumeDeletion = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 14340)
)
ocumEvtStorageServiceUnexpectedVolumeDeletion.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtStorageServiceUnexpectedVolumeDeletion.setStatus(
        ""
    )

ocumEvtShelfFanNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 14400)
)
ocumEvtShelfFanNormal.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtShelfFanNormal.setStatus(
        ""
    )

ocumEvtShelfFanFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 14401)
)
ocumEvtShelfFanFailed.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtShelfFanFailed.setStatus(
        ""
    )

ocumEvtShelfPowerSupplyNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 14410)
)
ocumEvtShelfPowerSupplyNormal.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtShelfPowerSupplyNormal.setStatus(
        ""
    )

ocumEvtShelfPowerSupplyFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 14411)
)
ocumEvtShelfPowerSupplyFailed.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtShelfPowerSupplyFailed.setStatus(
        ""
    )

ocumEvtShelfVoltageNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 14420)
)
ocumEvtShelfVoltageNormal.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtShelfVoltageNormal.setStatus(
        ""
    )

ocumEvtShelfVoltageAbnormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 14421)
)
ocumEvtShelfVoltageAbnormal.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtShelfVoltageAbnormal.setStatus(
        ""
    )

ocumEvtShelfCurrentNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 14430)
)
ocumEvtShelfCurrentNormal.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtShelfCurrentNormal.setStatus(
        ""
    )

ocumEvtShelfCurrentAbnormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 14431)
)
ocumEvtShelfCurrentAbnormal.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtShelfCurrentAbnormal.setStatus(
        ""
    )

ocumEvtShelfTemperatureNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 14440)
)
ocumEvtShelfTemperatureNormal.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtShelfTemperatureNormal.setStatus(
        ""
    )

ocumEvtShelfTemperatureAbnormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 14441)
)
ocumEvtShelfTemperatureAbnormal.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtShelfTemperatureAbnormal.setStatus(
        ""
    )

ocumEvtStorageShelfDiscovered = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 14450)
)
ocumEvtStorageShelfDiscovered.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtStorageShelfDiscovered.setStatus(
        ""
    )

ocumEvtStorageShelfRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 14460)
)
ocumEvtStorageShelfRemoved.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtStorageShelfRemoved.setStatus(
        ""
    )

ocumEvtProtectionJobTaskFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 14600)
)
ocumEvtProtectionJobTaskFailed.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtProtectionJobTaskFailed.setStatus(
        ""
    )

ocumEvtProtectionJobAborted = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 14610)
)
ocumEvtProtectionJobAborted.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtProtectionJobAborted.setStatus(
        ""
    )

ocumEvtVolumeOnline = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 14700)
)
ocumEvtVolumeOnline.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtVolumeOnline.setStatus(
        ""
    )

ocumEvtVolumeRestricted = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 14701)
)
ocumEvtVolumeRestricted.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtVolumeRestricted.setStatus(
        ""
    )

ocumEvtVolumeOffline = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 14702)
)
ocumEvtVolumeOffline.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtVolumeOffline.setStatus(
        ""
    )

ocumEvtVolumeMixed = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 14703)
)
ocumEvtVolumeMixed.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtVolumeMixed.setStatus(
        ""
    )

ocumEvtVolumeSpaceOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 14710)
)
ocumEvtVolumeSpaceOk.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtVolumeSpaceOk.setStatus(
        ""
    )

ocumEvtVolumeNearlyFull = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 14711)
)
ocumEvtVolumeNearlyFull.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtVolumeNearlyFull.setStatus(
        ""
    )

ocumEvtVolumeFull = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 14712)
)
ocumEvtVolumeFull.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtVolumeFull.setStatus(
        ""
    )

ocumEvtInodesUtilOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 14720)
)
ocumEvtInodesUtilOk.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtInodesUtilOk.setStatus(
        ""
    )

ocumEvtInodesAlmostFull = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 14721)
)
ocumEvtInodesAlmostFull.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtInodesAlmostFull.setStatus(
        ""
    )

ocumEvtInodesFull = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 14722)
)
ocumEvtInodesFull.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtInodesFull.setStatus(
        ""
    )

ocumEvtVolumeCloneDiscovered = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 14730)
)
ocumEvtVolumeCloneDiscovered.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtVolumeCloneDiscovered.setStatus(
        ""
    )

ocumEvtVolumeCloneDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 14740)
)
ocumEvtVolumeCloneDeleted.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtVolumeCloneDeleted.setStatus(
        ""
    )

ocumEvtVolumeCloneSplit = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 14750)
)
ocumEvtVolumeCloneSplit.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtVolumeCloneSplit.setStatus(
        ""
    )

ocumEvtVolumeQtreeQuotaOvercommitOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 14760)
)
ocumEvtVolumeQtreeQuotaOvercommitOk.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtVolumeQtreeQuotaOvercommitOk.setStatus(
        ""
    )

ocumEvtVolumeQtreeQuotaAlmostOvercommitted = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 14761)
)
ocumEvtVolumeQtreeQuotaAlmostOvercommitted.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtVolumeQtreeQuotaAlmostOvercommitted.setStatus(
        ""
    )

ocumEvtVolumeQtreeQuotaOvercommitted = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 14762)
)
ocumEvtVolumeQtreeQuotaOvercommitted.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtVolumeQtreeQuotaOvercommitted.setStatus(
        ""
    )

ocumEvtVolumeInlineCompressionEnabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 14780)
)
ocumEvtVolumeInlineCompressionEnabled.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtVolumeInlineCompressionEnabled.setStatus(
        ""
    )

ocumEvtVolumeInlineCompressionDisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 14781)
)
ocumEvtVolumeInlineCompressionDisabled.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtVolumeInlineCompressionDisabled.setStatus(
        ""
    )

ocumEvtVolumeBackgroundCompressionEnabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 14790)
)
ocumEvtVolumeBackgroundCompressionEnabled.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtVolumeBackgroundCompressionEnabled.setStatus(
        ""
    )

ocumEvtVolumeBackgroundCompressionDisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 14791)
)
ocumEvtVolumeBackgroundCompressionDisabled.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtVolumeBackgroundCompressionDisabled.setStatus(
        ""
    )

ocumEvtVolumeDedupeEnabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 14800)
)
ocumEvtVolumeDedupeEnabled.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtVolumeDedupeEnabled.setStatus(
        ""
    )

ocumEvtVolumeDedupeDisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 14801)
)
ocumEvtVolumeDedupeDisabled.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtVolumeDedupeDisabled.setStatus(
        ""
    )

ocumEvtVolumeEfficiencyOperationOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 14810)
)
ocumEvtVolumeEfficiencyOperationOk.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtVolumeEfficiencyOperationOk.setStatus(
        ""
    )

ocumEvtVolumeEfficiencyOperationError = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 14811)
)
ocumEvtVolumeEfficiencyOperationError.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtVolumeEfficiencyOperationError.setStatus(
        ""
    )

ocumEvtVolumeGrowthRateOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 14820)
)
ocumEvtVolumeGrowthRateOk.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtVolumeGrowthRateOk.setStatus(
        ""
    )

ocumEvtVolumeGrowthRateAbnormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 14821)
)
ocumEvtVolumeGrowthRateAbnormal.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtVolumeGrowthRateAbnormal.setStatus(
        ""
    )

ocumEvtVolumeRenamed = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 14830)
)
ocumEvtVolumeRenamed.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtVolumeRenamed.setStatus(
        ""
    )

ocumEvtVolumeDiscovered = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 14840)
)
ocumEvtVolumeDiscovered.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtVolumeDiscovered.setStatus(
        ""
    )

ocumEvtVolumeRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 14850)
)
ocumEvtVolumeRemoved.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtVolumeRemoved.setStatus(
        ""
    )

ocumEvtVolumeMounted = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 14860)
)
ocumEvtVolumeMounted.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtVolumeMounted.setStatus(
        ""
    )

ocumEvtVolumeUnmounted = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 14861)
)
ocumEvtVolumeUnmounted.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtVolumeUnmounted.setStatus(
        ""
    )

ocumEvtVolumeRemounted = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 14862)
)
ocumEvtVolumeRemounted.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtVolumeRemounted.setStatus(
        ""
    )

ocumEvtVolumeExportPolicyModified = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 14870)
)
ocumEvtVolumeExportPolicyModified.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtVolumeExportPolicyModified.setStatus(
        ""
    )

ocumEvtVolumeDaysUntilFullNotSoon = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 14880)
)
ocumEvtVolumeDaysUntilFullNotSoon.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtVolumeDaysUntilFullNotSoon.setStatus(
        ""
    )

ocumEvtVolumeDaysUntilFullSoon = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 14881)
)
ocumEvtVolumeDaysUntilFullSoon.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtVolumeDaysUntilFullSoon.setStatus(
        ""
    )

ocumEvtVolumeFractionalReserveModified = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 14890)
)
ocumEvtVolumeFractionalReserveModified.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtVolumeFractionalReserveModified.setStatus(
        ""
    )

ocumEvtVolumeSpaceGuaranteeModified = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 14900)
)
ocumEvtVolumeSpaceGuaranteeModified.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtVolumeSpaceGuaranteeModified.setStatus(
        ""
    )

ocumEvtVolumeSpaceGuaranteeEnabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 14901)
)
ocumEvtVolumeSpaceGuaranteeEnabled.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtVolumeSpaceGuaranteeEnabled.setStatus(
        ""
    )

ocumEvtVolumeSpaceGuaranteeDisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 14902)
)
ocumEvtVolumeSpaceGuaranteeDisabled.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtVolumeSpaceGuaranteeDisabled.setStatus(
        ""
    )

ocumEvtVolumeAutosizeEnabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 14910)
)
ocumEvtVolumeAutosizeEnabled.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtVolumeAutosizeEnabled.setStatus(
        ""
    )

ocumEvtVolumeAutosizeDisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 14911)
)
ocumEvtVolumeAutosizeDisabled.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtVolumeAutosizeDisabled.setStatus(
        ""
    )

ocumEvtVolumeAutosizeModifiedMax = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 14912)
)
ocumEvtVolumeAutosizeModifiedMax.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtVolumeAutosizeModifiedMax.setStatus(
        ""
    )

ocumEvtVolumeAutosizeModifiedIncrement = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 14913)
)
ocumEvtVolumeAutosizeModifiedIncrement.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtVolumeAutosizeModifiedIncrement.setStatus(
        ""
    )

ocumEvtVolumeMoveFinished = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 14920)
)
ocumEvtVolumeMoveFinished.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtVolumeMoveFinished.setStatus(
        ""
    )

ocumEvtVolumeMoveProgress = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 14921)
)
ocumEvtVolumeMoveProgress.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtVolumeMoveProgress.setStatus(
        ""
    )

ocumEvtVolumeMoveCompleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 14922)
)
ocumEvtVolumeMoveCompleted.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtVolumeMoveCompleted.setStatus(
        ""
    )

ocumEvtVolumeMoveCutoverDeferred = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 14923)
)
ocumEvtVolumeMoveCutoverDeferred.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtVolumeMoveCutoverDeferred.setStatus(
        ""
    )

ocumEvtVolumeMoveFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 14924)
)
ocumEvtVolumeMoveFailed.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtVolumeMoveFailed.setStatus(
        ""
    )

ocumEvtVolumeJunctionPathActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 14930)
)
ocumEvtVolumeJunctionPathActive.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtVolumeJunctionPathActive.setStatus(
        ""
    )

ocumEvtVolumeJunctionPathInactive = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 14931)
)
ocumEvtVolumeJunctionPathInactive.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtVolumeJunctionPathInactive.setStatus(
        ""
    )

ocumEvtSnapshotSpaceOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 15000)
)
ocumEvtSnapshotSpaceOk.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtSnapshotSpaceOk.setStatus(
        ""
    )

ocumEvtSnapshotFull = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 15001)
)
ocumEvtSnapshotFull.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtSnapshotFull.setStatus(
        ""
    )

ocumEvtSnapshotTooMany = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 15010)
)
ocumEvtSnapshotTooMany.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtSnapshotTooMany.setStatus(
        ""
    )

ocumEvtSnapshotNotTooMany = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 15011)
)
ocumEvtSnapshotNotTooMany.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtSnapshotNotTooMany.setStatus(
        ""
    )

ocumEvtSnapSchedModified = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 15020)
)
ocumEvtSnapSchedModified.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtSnapSchedModified.setStatus(
        ""
    )

ocumEvtSnapEnabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 15030)
)
ocumEvtSnapEnabled.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtSnapEnabled.setStatus(
        ""
    )

ocumEvtSnapDisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 15031)
)
ocumEvtSnapDisabled.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtSnapDisabled.setStatus(
        ""
    )

ocumEvtSnapshotAutodeleteEnabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 15040)
)
ocumEvtSnapshotAutodeleteEnabled.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtSnapshotAutodeleteEnabled.setStatus(
        ""
    )

ocumEvtSnapshotAutodeleteDisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 15041)
)
ocumEvtSnapshotAutodeleteDisabled.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtSnapshotAutodeleteDisabled.setStatus(
        ""
    )

ocumEvtSnapshotAutodeleteModified = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 15042)
)
ocumEvtSnapshotAutodeleteModified.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtSnapshotAutodeleteModified.setStatus(
        ""
    )

ocumEvtVolumeSnapshotReserveDaysUntilFullNotSoon = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 15050)
)
ocumEvtVolumeSnapshotReserveDaysUntilFullNotSoon.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtVolumeSnapshotReserveDaysUntilFullNotSoon.setStatus(
        ""
    )

ocumEvtVolumeSnapshotReserveDaysUntilFullSoon = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 15051)
)
ocumEvtVolumeSnapshotReserveDaysUntilFullSoon.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtVolumeSnapshotReserveDaysUntilFullSoon.setStatus(
        ""
    )

ocumEvtVolumeSnapshotReserveModified = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 15060)
)
ocumEvtVolumeSnapshotReserveModified.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtVolumeSnapshotReserveModified.setStatus(
        ""
    )

ocumEvtVolumeNextSnapshotPossible = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 15070)
)
ocumEvtVolumeNextSnapshotPossible.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtVolumeNextSnapshotPossible.setStatus(
        ""
    )

ocumEvtVolumeNextSnapshotNotPossible = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 15071)
)
ocumEvtVolumeNextSnapshotNotPossible.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtVolumeNextSnapshotNotPossible.setStatus(
        ""
    )

ocumEvtSnapmirrorRelationshipDiscovered = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 15200)
)
ocumEvtSnapmirrorRelationshipDiscovered.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtSnapmirrorRelationshipDiscovered.setStatus(
        ""
    )

ocumEvtSnapmirrorRelationshipModified = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 15201)
)
ocumEvtSnapmirrorRelationshipModified.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtSnapmirrorRelationshipModified.setStatus(
        ""
    )

ocumEvtSnapmirrorRelationshipDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 15210)
)
ocumEvtSnapmirrorRelationshipDeleted.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtSnapmirrorRelationshipDeleted.setStatus(
        ""
    )

ocumEvtSnapmirrorRelationshipHealthy = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 15220)
)
ocumEvtSnapmirrorRelationshipHealthy.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtSnapmirrorRelationshipHealthy.setStatus(
        ""
    )

ocumEvtSnapmirrorRelationshipUnhealthy = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 15221)
)
ocumEvtSnapmirrorRelationshipUnhealthy.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtSnapmirrorRelationshipUnhealthy.setStatus(
        ""
    )

ocumEvtSnapmirrorRelationshipStateOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 15230)
)
ocumEvtSnapmirrorRelationshipStateOk.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtSnapmirrorRelationshipStateOk.setStatus(
        ""
    )

ocumEvtSnapmirrorRelationshipStateBrokenoff = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 15231)
)
ocumEvtSnapmirrorRelationshipStateBrokenoff.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtSnapmirrorRelationshipStateBrokenoff.setStatus(
        ""
    )

ocumEvtSnapmirrorRelationshipInitializeOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 15240)
)
ocumEvtSnapmirrorRelationshipInitializeOk.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtSnapmirrorRelationshipInitializeOk.setStatus(
        ""
    )

ocumEvtSnapmirrorRelationshipInitializeFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 15241)
)
ocumEvtSnapmirrorRelationshipInitializeFailed.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtSnapmirrorRelationshipInitializeFailed.setStatus(
        ""
    )

ocumEvtSnapmirrorRelationshipUpdateOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 15250)
)
ocumEvtSnapmirrorRelationshipUpdateOk.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtSnapmirrorRelationshipUpdateOk.setStatus(
        ""
    )

ocumEvtSnapmirrorRelationshipUpdateFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 15251)
)
ocumEvtSnapmirrorRelationshipUpdateFailed.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtSnapmirrorRelationshipUpdateFailed.setStatus(
        ""
    )

ocumEvtSnapmirrorRelationshipResyncOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 15252)
)
ocumEvtSnapmirrorRelationshipResyncOk.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtSnapmirrorRelationshipResyncOk.setStatus(
        ""
    )

ocumEvtSnapmirrorRelationshipResyncFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 15253)
)
ocumEvtSnapmirrorRelationshipResyncFailed.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtSnapmirrorRelationshipResyncFailed.setStatus(
        ""
    )

ocumEvtSnapMirrorRelationshipLagWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 15260)
)
ocumEvtSnapMirrorRelationshipLagWarning.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtSnapMirrorRelationshipLagWarning.setStatus(
        ""
    )

ocumEvtSnapMirrorRelationshipLagError = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 15261)
)
ocumEvtSnapMirrorRelationshipLagError.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtSnapMirrorRelationshipLagError.setStatus(
        ""
    )

ocumEvtSnapMirrorRelationshipLagNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 15262)
)
ocumEvtSnapMirrorRelationshipLagNormal.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtSnapMirrorRelationshipLagNormal.setStatus(
        ""
    )

ocumEvtSnapvaultRelationshipHealthy = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 15300)
)
ocumEvtSnapvaultRelationshipHealthy.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtSnapvaultRelationshipHealthy.setStatus(
        ""
    )

ocumEvtSnapvaultRelationshipUnhealthy = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 15301)
)
ocumEvtSnapvaultRelationshipUnhealthy.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtSnapvaultRelationshipUnhealthy.setStatus(
        ""
    )

ocumEvtSnapvaultRelationshipStateOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 15310)
)
ocumEvtSnapvaultRelationshipStateOk.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtSnapvaultRelationshipStateOk.setStatus(
        ""
    )

ocumEvtSnapvaultRelationshipStateBrokenoff = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 15311)
)
ocumEvtSnapvaultRelationshipStateBrokenoff.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtSnapvaultRelationshipStateBrokenoff.setStatus(
        ""
    )

ocumEvtSnapvaultRelationshipInitializeOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 15320)
)
ocumEvtSnapvaultRelationshipInitializeOk.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtSnapvaultRelationshipInitializeOk.setStatus(
        ""
    )

ocumEvtSnapvaultRelationshipInitializeFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 15321)
)
ocumEvtSnapvaultRelationshipInitializeFailed.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtSnapvaultRelationshipInitializeFailed.setStatus(
        ""
    )

ocumEvtSnapvaultRelationshipUpdateOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 15330)
)
ocumEvtSnapvaultRelationshipUpdateOk.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtSnapvaultRelationshipUpdateOk.setStatus(
        ""
    )

ocumEvtSnapvaultRelationshipUpdateFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 15331)
)
ocumEvtSnapvaultRelationshipUpdateFailed.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtSnapvaultRelationshipUpdateFailed.setStatus(
        ""
    )

ocumEvtSnapvaultRelationshipResyncOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 15332)
)
ocumEvtSnapvaultRelationshipResyncOk.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtSnapvaultRelationshipResyncOk.setStatus(
        ""
    )

ocumEvtSnapvaultRelationshipResyncFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 15333)
)
ocumEvtSnapvaultRelationshipResyncFailed.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtSnapvaultRelationshipResyncFailed.setStatus(
        ""
    )

ocumEvtSnapVaultRelationshipLagWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 15340)
)
ocumEvtSnapVaultRelationshipLagWarning.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtSnapVaultRelationshipLagWarning.setStatus(
        ""
    )

ocumEvtSnapVaultRelationshipLagError = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 15341)
)
ocumEvtSnapVaultRelationshipLagError.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtSnapVaultRelationshipLagError.setStatus(
        ""
    )

ocumEvtSnapVaultRelationshipLagNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 15342)
)
ocumEvtSnapVaultRelationshipLagNormal.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtSnapVaultRelationshipLagNormal.setStatus(
        ""
    )

ocumEvtVserverCifsServiceStatusUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 15400)
)
ocumEvtVserverCifsServiceStatusUp.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtVserverCifsServiceStatusUp.setStatus(
        ""
    )

ocumEvtVserverCifsServiceStatusDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 15401)
)
ocumEvtVserverCifsServiceStatusDown.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtVserverCifsServiceStatusDown.setStatus(
        ""
    )

ocumEvtVserverFcServiceStatusUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 15410)
)
ocumEvtVserverFcServiceStatusUp.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtVserverFcServiceStatusUp.setStatus(
        ""
    )

ocumEvtVserverFcServiceStatusDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 15411)
)
ocumEvtVserverFcServiceStatusDown.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtVserverFcServiceStatusDown.setStatus(
        ""
    )

ocumEvtVserverIscsiServiceStatusUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 15420)
)
ocumEvtVserverIscsiServiceStatusUp.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtVserverIscsiServiceStatusUp.setStatus(
        ""
    )

ocumEvtVserverIscsiServiceStatusDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 15421)
)
ocumEvtVserverIscsiServiceStatusDown.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtVserverIscsiServiceStatusDown.setStatus(
        ""
    )

ocumEvtVserverNfsServiceStatusUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 15430)
)
ocumEvtVserverNfsServiceStatusUp.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtVserverNfsServiceStatusUp.setStatus(
        ""
    )

ocumEvtVserverNfsServiceStatusDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 15431)
)
ocumEvtVserverNfsServiceStatusDown.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtVserverNfsServiceStatusDown.setStatus(
        ""
    )

ocumEvtVserverCifsServiceNotConfigured = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 15440)
)
ocumEvtVserverCifsServiceNotConfigured.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtVserverCifsServiceNotConfigured.setStatus(
        ""
    )

ocumEvtVserverFcServiceNotConfigured = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 15450)
)
ocumEvtVserverFcServiceNotConfigured.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtVserverFcServiceNotConfigured.setStatus(
        ""
    )

ocumEvtVserverIscsiServiceNotConfigured = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 15460)
)
ocumEvtVserverIscsiServiceNotConfigured.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtVserverIscsiServiceNotConfigured.setStatus(
        ""
    )

ocumEvtVserverNfsServiceNotConfigured = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 15470)
)
ocumEvtVserverNfsServiceNotConfigured.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtVserverNfsServiceNotConfigured.setStatus(
        ""
    )

ocumEvtVserverRenamed = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 15480)
)
ocumEvtVserverRenamed.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtVserverRenamed.setStatus(
        ""
    )

ocumEvtVserverUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 15490)
)
ocumEvtVserverUp.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtVserverUp.setStatus(
        ""
    )

ocumEvtVserverDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 15491)
)
ocumEvtVserverDown.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtVserverDown.setStatus(
        ""
    )

ocumEvtVserverDiscovered = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 15500)
)
ocumEvtVserverDiscovered.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtVserverDiscovered.setStatus(
        ""
    )

ocumEvtVserverDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 15510)
)
ocumEvtVserverDeleted.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtVserverDeleted.setStatus(
        ""
    )

ocumEvtVserverStorageAvailable = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 15520)
)
ocumEvtVserverStorageAvailable.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtVserverStorageAvailable.setStatus(
        ""
    )

ocumEvtVserverStoragePartiallyAvailable = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 15521)
)
ocumEvtVserverStoragePartiallyAvailable.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtVserverStoragePartiallyAvailable.setStatus(
        ""
    )

ocumEvtVserverStorageNotAvailable = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 15522)
)
ocumEvtVserverStorageNotAvailable.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtVserverStorageNotAvailable.setStatus(
        ""
    )

ocumEvtVserverSpaceOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 15530)
)
ocumEvtVserverSpaceOk.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtVserverSpaceOk.setStatus(
        ""
    )

ocumEvtVserverNearlyFull = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 15531)
)
ocumEvtVserverNearlyFull.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtVserverNearlyFull.setStatus(
        ""
    )

ocumEvtVserverFull = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 15532)
)
ocumEvtVserverFull.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtVserverFull.setStatus(
        ""
    )

ocumEvtVserverSnapshotUsageOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 15540)
)
ocumEvtVserverSnapshotUsageOk.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtVserverSnapshotUsageOk.setStatus(
        ""
    )

ocumEvtVserverSnapshotUsageExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 15541)
)
ocumEvtVserverSnapshotUsageExceeded.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtVserverSnapshotUsageExceeded.setStatus(
        ""
    )

ocumEvtVserverNsMirrorAvailabilityOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 15550)
)
ocumEvtVserverNsMirrorAvailabilityOk.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtVserverNsMirrorAvailabilityOk.setStatus(
        ""
    )

ocumEvtVserverNsMirrorAvailabilityHavingIssues = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 15551)
)
ocumEvtVserverNsMirrorAvailabilityHavingIssues.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtVserverNsMirrorAvailabilityHavingIssues.setStatus(
        ""
    )

ocumEvtVserverNamespaceSpaceOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 15560)
)
ocumEvtVserverNamespaceSpaceOk.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtVserverNamespaceSpaceOk.setStatus(
        ""
    )

ocumEvtVserverNamespaceNearlyFull = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 15561)
)
ocumEvtVserverNamespaceNearlyFull.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtVserverNamespaceNearlyFull.setStatus(
        ""
    )

ocumEvtVserverNamespaceFull = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 15562)
)
ocumEvtVserverNamespaceFull.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtVserverNamespaceFull.setStatus(
        ""
    )

ocumEvtVserverStorageClassAvailable = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 15600)
)
ocumEvtVserverStorageClassAvailable.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtVserverStorageClassAvailable.setStatus(
        ""
    )

ocumEvtVserverStorageClassPartiallyAvailable = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 15601)
)
ocumEvtVserverStorageClassPartiallyAvailable.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtVserverStorageClassPartiallyAvailable.setStatus(
        ""
    )

ocumEvtVserverStorageClassNotAvailable = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 15602)
)
ocumEvtVserverStorageClassNotAvailable.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtVserverStorageClassNotAvailable.setStatus(
        ""
    )

ocumEvtVserverStorageClassSpaceOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 15610)
)
ocumEvtVserverStorageClassSpaceOk.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtVserverStorageClassSpaceOk.setStatus(
        ""
    )

ocumEvtVserverStorageClassNearlyFull = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 15611)
)
ocumEvtVserverStorageClassNearlyFull.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtVserverStorageClassNearlyFull.setStatus(
        ""
    )

ocumEvtVserverStorageClassFull = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 15612)
)
ocumEvtVserverStorageClassFull.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtVserverStorageClassFull.setStatus(
        ""
    )

ocumEvtVserverStorageClassSnapshotUsageOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 15620)
)
ocumEvtVserverStorageClassSnapshotUsageOk.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtVserverStorageClassSnapshotUsageOk.setStatus(
        ""
    )

ocumEvtVserverStorageClassSnapshotUsageExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 15621)
)
ocumEvtVserverStorageClassSnapshotUsageExceeded.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtVserverStorageClassSnapshotUsageExceeded.setStatus(
        ""
    )

ocumEvtScriptNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 15700)
)
ocumEvtScriptNormal.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtScriptNormal.setStatus(
        ""
    )

ocumEvtScriptInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 15701)
)
ocumEvtScriptInformation.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtScriptInformation.setStatus(
        ""
    )

ocumEvtScriptWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 15702)
)
ocumEvtScriptWarning.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtScriptWarning.setStatus(
        ""
    )

ocumEvtScriptError = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 15703)
)
ocumEvtScriptError.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtScriptError.setStatus(
        ""
    )

ocumEvtScriptCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 15704)
)
ocumEvtScriptCritical.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtScriptCritical.setStatus(
        ""
    )

ocumEvtUserOrGroupQuotaFileCountOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 15800)
)
ocumEvtUserOrGroupQuotaFileCountOk.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtUserOrGroupQuotaFileCountOk.setStatus(
        ""
    )

ocumEvtUserOrGroupQuotaFileCountSoftLimitBreached = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 15801)
)
ocumEvtUserOrGroupQuotaFileCountSoftLimitBreached.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtUserOrGroupQuotaFileCountSoftLimitBreached.setStatus(
        ""
    )

ocumEvtUserOrGroupQuotaFileCountHardLimitReached = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 15802)
)
ocumEvtUserOrGroupQuotaFileCountHardLimitReached.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtUserOrGroupQuotaFileCountHardLimitReached.setStatus(
        ""
    )

ocumEvtUserOrGroupQuotaDiskSpaceOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 15810)
)
ocumEvtUserOrGroupQuotaDiskSpaceOk.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtUserOrGroupQuotaDiskSpaceOk.setStatus(
        ""
    )

ocumEvtUserOrGroupQuotaDiskSpaceSoftLimitBreached = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 15811)
)
ocumEvtUserOrGroupQuotaDiskSpaceSoftLimitBreached.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtUserOrGroupQuotaDiskSpaceSoftLimitBreached.setStatus(
        ""
    )

ocumEvtUserOrGroupQuotaDiskSpaceHardLimitReached = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 15812)
)
ocumEvtUserOrGroupQuotaDiskSpaceHardLimitReached.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtUserOrGroupQuotaDiskSpaceHardLimitReached.setStatus(
        ""
    )

ocumPerformanceIncident = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 15820)
)
ocumPerformanceIncident.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumPerformanceIncident.setStatus(
        ""
    )

ocumPerformanceIncidentCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 15821)
)
ocumPerformanceIncidentCleared.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumPerformanceIncidentCleared.setStatus(
        ""
    )

ocumPerformanceError = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 15822)
)
ocumPerformanceError.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumPerformanceError.setStatus(
        ""
    )

ocumPerformanceWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 15823)
)
ocumPerformanceWarning.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumPerformanceWarning.setStatus(
        ""
    )

ocumPerformanceInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 15824)
)
ocumPerformanceInformation.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumPerformanceInformation.setStatus(
        ""
    )

ocumThinProvisionVolumeSpaceAtRisk = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 15830)
)
ocumThinProvisionVolumeSpaceAtRisk.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumThinProvisionVolumeSpaceAtRisk.setStatus(
        ""
    )

ocumThinProvisionVolumeSpaceNotAtRisk = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 15831)
)
ocumThinProvisionVolumeSpaceNotAtRisk.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumThinProvisionVolumeSpaceNotAtRisk.setStatus(
        ""
    )

ocumDiskShelfConnectivityInMultiPath = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 15840)
)
ocumDiskShelfConnectivityInMultiPath.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumDiskShelfConnectivityInMultiPath.setStatus(
        ""
    )

ocumDiskShelfConnectivityNotInMultiPath = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 15841)
)
ocumDiskShelfConnectivityNotInMultiPath.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumDiskShelfConnectivityNotInMultiPath.setStatus(
        ""
    )

ocumDiskShelfConnectivityPathNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 15850)
)
ocumDiskShelfConnectivityPathNormal.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumDiskShelfConnectivityPathNormal.setStatus(
        ""
    )

ocumDiskShelfConnectivityPathFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 15851)
)
ocumDiskShelfConnectivityPathFailure.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumDiskShelfConnectivityPathFailure.setStatus(
        ""
    )

ocumClusterAddNeeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 15860)
)
ocumClusterAddNeeded.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumClusterAddNeeded.setStatus(
        ""
    )

ocumClusterAdded = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 15861)
)
ocumClusterAdded.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumClusterAdded.setStatus(
        ""
    )

ocumEvtMccNodeSwitchFcviLinksUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 15900)
)
ocumEvtMccNodeSwitchFcviLinksUp.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtMccNodeSwitchFcviLinksUp.setStatus(
        ""
    )

ocumEvtMccNodeSwitchFcviLinksOneOrMoreDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 15901)
)
ocumEvtMccNodeSwitchFcviLinksOneOrMoreDown.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtMccNodeSwitchFcviLinksOneOrMoreDown.setStatus(
        ""
    )

ocumEvtMccNodeSwitchFcviLinksDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 15902)
)
ocumEvtMccNodeSwitchFcviLinksDown.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtMccNodeSwitchFcviLinksDown.setStatus(
        ""
    )

ocumEvtMccNodeSwitchFcLinksUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 15910)
)
ocumEvtMccNodeSwitchFcLinksUp.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtMccNodeSwitchFcLinksUp.setStatus(
        ""
    )

ocumEvtMccNodeSwitchFcLinksOneOrMoreDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 15911)
)
ocumEvtMccNodeSwitchFcLinksOneOrMoreDown.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtMccNodeSwitchFcLinksOneOrMoreDown.setStatus(
        ""
    )

ocumEvtMccNodeSwitchFcLinksDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 15912)
)
ocumEvtMccNodeSwitchFcLinksDown.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtMccNodeSwitchFcLinksDown.setStatus(
        ""
    )

ocumEvtMccSwitchBridgeFcLinksUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 15920)
)
ocumEvtMccSwitchBridgeFcLinksUp.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtMccSwitchBridgeFcLinksUp.setStatus(
        ""
    )

ocumEvtMccSwitchBridgeFcLinksDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 15921)
)
ocumEvtMccSwitchBridgeFcLinksDown.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtMccSwitchBridgeFcLinksDown.setStatus(
        ""
    )

ocumEvtSwitchTemperatureNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 16000)
)
ocumEvtSwitchTemperatureNormal.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtSwitchTemperatureNormal.setStatus(
        ""
    )

ocumEvtSwitchTemperatureAbnormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 16001)
)
ocumEvtSwitchTemperatureAbnormal.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtSwitchTemperatureAbnormal.setStatus(
        ""
    )

ocumEvtSwitchFansNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 16010)
)
ocumEvtSwitchFansNormal.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtSwitchFansNormal.setStatus(
        ""
    )

ocumEvtSwitchFansOneOrMoreFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 16011)
)
ocumEvtSwitchFansOneOrMoreFailed.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtSwitchFansOneOrMoreFailed.setStatus(
        ""
    )

ocumEvtSwitchPowerSuppliesNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 16020)
)
ocumEvtSwitchPowerSuppliesNormal.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtSwitchPowerSuppliesNormal.setStatus(
        ""
    )

ocumEvtSwitchPowerSuppliesOneOrMoreFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 16021)
)
ocumEvtSwitchPowerSuppliesOneOrMoreFailed.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtSwitchPowerSuppliesOneOrMoreFailed.setStatus(
        ""
    )

ocumEvtSwitchReachable = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 16030)
)
ocumEvtSwitchReachable.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtSwitchReachable.setStatus(
        ""
    )

ocumEvtSwitchUnreachable = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 16031)
)
ocumEvtSwitchUnreachable.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtSwitchUnreachable.setStatus(
        ""
    )

ocumEvtSwitchTemperatureSensorNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 16040)
)
ocumEvtSwitchTemperatureSensorNormal.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtSwitchTemperatureSensorNormal.setStatus(
        ""
    )

ocumEvtSwitchTemperatureSensorFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 16041)
)
ocumEvtSwitchTemperatureSensorFailed.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtSwitchTemperatureSensorFailed.setStatus(
        ""
    )

ocumEvtBridgeTemperatureNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 16100)
)
ocumEvtBridgeTemperatureNormal.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtBridgeTemperatureNormal.setStatus(
        ""
    )

ocumEvtBridgeTemperatureAbnormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 16101)
)
ocumEvtBridgeTemperatureAbnormal.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtBridgeTemperatureAbnormal.setStatus(
        ""
    )

ocumEvtBridgeReachable = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 16110)
)
ocumEvtBridgeReachable.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtBridgeReachable.setStatus(
        ""
    )

ocumEvtBridgeUnreachable = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 16111)
)
ocumEvtBridgeUnreachable.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtBridgeUnreachable.setStatus(
        ""
    )

ocumEvtMetroClusterAllLinksBetweenPartnersUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 16200)
)
ocumEvtMetroClusterAllLinksBetweenPartnersUp.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtMetroClusterAllLinksBetweenPartnersUp.setStatus(
        ""
    )

ocumEvtMetroClusterAllLinksBetweenPartnersDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 16201)
)
ocumEvtMetroClusterAllLinksBetweenPartnersDown.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtMetroClusterAllLinksBetweenPartnersDown.setStatus(
        ""
    )

ocumEvtMetroClusterPartnersReachableOverPeeringNetwork = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 16210)
)
ocumEvtMetroClusterPartnersReachableOverPeeringNetwork.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtMetroClusterPartnersReachableOverPeeringNetwork.setStatus(
        ""
    )

ocumEvtMetroClusterPartnersNotReachableOverPeeringNetwork = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 16211)
)
ocumEvtMetroClusterPartnersNotReachableOverPeeringNetwork.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtMetroClusterPartnersNotReachableOverPeeringNetwork.setStatus(
        ""
    )

ocumEvtMetroClusterAllISLBetweenSwitchesUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 16220)
)
ocumEvtMetroClusterAllISLBetweenSwitchesUp.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtMetroClusterAllISLBetweenSwitchesUp.setStatus(
        ""
    )

ocumEvtMetroClusterAllISLBetweenSwitchesDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 16221)
)
ocumEvtMetroClusterAllISLBetweenSwitchesDown.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtMetroClusterAllISLBetweenSwitchesDown.setStatus(
        ""
    )

ocumEvtMetroClusterDRStatusOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 16230)
)
ocumEvtMetroClusterDRStatusOk.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtMetroClusterDRStatusOk.setStatus(
        ""
    )

ocumEvtMetroClusterDRStatusPartiallyImpacted = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 16231)
)
ocumEvtMetroClusterDRStatusPartiallyImpacted.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtMetroClusterDRStatusPartiallyImpacted.setStatus(
        ""
    )

ocumEvtMetroClusterDRStatusImpacted = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 16232)
)
ocumEvtMetroClusterDRStatusImpacted.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtMetroClusterDRStatusImpacted.setStatus(
        ""
    )

ocumEvtMetroClusterDRStatusCompleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 16233)
)
ocumEvtMetroClusterDRStatusCompleted.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtMetroClusterDRStatusCompleted.setStatus(
        ""
    )

ocumEvtMetroClusterAggregateMirrorNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 16300)
)
ocumEvtMetroClusterAggregateMirrorNormal.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtMetroClusterAggregateMirrorNormal.setStatus(
        ""
    )

ocumEvtMetroClusterAggregateMirrorDegraded = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 16301)
)
ocumEvtMetroClusterAggregateMirrorDegraded.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtMetroClusterAggregateMirrorDegraded.setStatus(
        ""
    )

ocumEvtNoSpareDiskLeftBehind = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 16310)
)
ocumEvtNoSpareDiskLeftBehind.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtNoSpareDiskLeftBehind.setStatus(
        ""
    )

ocumEvtSpareDiskLeftBehind = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 16311)
)
ocumEvtSpareDiskLeftBehind.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtSpareDiskLeftBehind.setStatus(
        ""
    )

ocumEvtMccBridgeStorageStackSASLinksUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 16320)
)
ocumEvtMccBridgeStorageStackSASLinksUp.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtMccBridgeStorageStackSASLinksUp.setStatus(
        ""
    )

ocumEvtMccBridgeStorageStackSASLinksDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 16321)
)
ocumEvtMccBridgeStorageStackSASLinksDown.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtMccBridgeStorageStackSASLinksDown.setStatus(
        ""
    )

ocumEvtClusterFlashDiskFewerSpareBlockNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 16330)
)
ocumEvtClusterFlashDiskFewerSpareBlockNormal.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtClusterFlashDiskFewerSpareBlockNormal.setStatus(
        ""
    )

ocumEvtClusterFlashDiskFewerSpareBlockError = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 16331)
)
ocumEvtClusterFlashDiskFewerSpareBlockError.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtClusterFlashDiskFewerSpareBlockError.setStatus(
        ""
    )

ocumEvtClusterFlashDiskNoSpareBlockNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 16340)
)
ocumEvtClusterFlashDiskNoSpareBlockNormal.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtClusterFlashDiskNoSpareBlockNormal.setStatus(
        ""
    )

ocumEvtClusterFlashDiskNoSpareBlockCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 16341)
)
ocumEvtClusterFlashDiskNoSpareBlockCritical.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtClusterFlashDiskNoSpareBlockCritical.setStatus(
        ""
    )

ocumEvtBackupCreationSucceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 16350)
)
ocumEvtBackupCreationSucceeded.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtBackupCreationSucceeded.setStatus(
        ""
    )

ocumEvtBackupCreationFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 16351)
)
ocumEvtBackupCreationFailed.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtBackupCreationFailed.setStatus(
        ""
    )

ocumEvtBackupCreationNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 16352)
)
ocumEvtBackupCreationNormal.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtBackupCreationNormal.setStatus(
        ""
    )

ocumEvtMccInterNodeLinksUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 16400)
)
ocumEvtMccInterNodeLinksUp.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtMccInterNodeLinksUp.setStatus(
        ""
    )

ocumEvtMccInterNodeLinksOneOrMoreDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 16401)
)
ocumEvtMccInterNodeLinksOneOrMoreDown.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtMccInterNodeLinksOneOrMoreDown.setStatus(
        ""
    )

ocumEvtMccInterNodeLinksDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 16402)
)
ocumEvtMccInterNodeLinksDown.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtMccInterNodeLinksDown.setStatus(
        ""
    )

ocumEvtMccNodeBridgeLinksUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 16410)
)
ocumEvtMccNodeBridgeLinksUp.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtMccNodeBridgeLinksUp.setStatus(
        ""
    )

ocumEvtMccNodeBridgeLinksDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 16411)
)
ocumEvtMccNodeBridgeLinksDown.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtMccNodeBridgeLinksDown.setStatus(
        ""
    )

ocumEvtMccNodeStackLinksUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 16420)
)
ocumEvtMccNodeStackLinksUp.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtMccNodeStackLinksUp.setStatus(
        ""
    )

ocumEvtMccNodeStackLinksOneOrMoreDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 16421)
)
ocumEvtMccNodeStackLinksOneOrMoreDown.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtMccNodeStackLinksOneOrMoreDown.setStatus(
        ""
    )

ocumEvtMccNodeStackLinksDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 16422)
)
ocumEvtMccNodeStackLinksDown.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtMccNodeStackLinksDown.setStatus(
        ""
    )

ocumEvtMccAutomaticUnplannedSwitchOverDisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 16500)
)
ocumEvtMccAutomaticUnplannedSwitchOverDisabled.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtMccAutomaticUnplannedSwitchOverDisabled.setStatus(
        ""
    )

ocumEvtMccAutomaticUnplannedSwitchOverEnabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 16501)
)
ocumEvtMccAutomaticUnplannedSwitchOverEnabled.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtMccAutomaticUnplannedSwitchOverEnabled.setStatus(
        ""
    )

ocumEvtEMSWarningEventReceived = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 16600)
)
ocumEvtEMSWarningEventReceived.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtEMSWarningEventReceived.setStatus(
        ""
    )

ocumEvtEMSCriticalEventReceived = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 16610)
)
ocumEvtEMSCriticalEventReceived.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtEMSCriticalEventReceived.setStatus(
        ""
    )

ocumEvtEMSErrorEventReceived = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 16620)
)
ocumEvtEMSErrorEventReceived.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtEMSErrorEventReceived.setStatus(
        ""
    )

ocumEvtEMSInformationalEventReceived = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 16630)
)
ocumEvtEMSInformationalEventReceived.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtEMSInformationalEventReceived.setStatus(
        ""
    )

ocumEvtEMSNoticeEventReceived = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 16640)
)
ocumEvtEMSNoticeEventReceived.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtEMSNoticeEventReceived.setStatus(
        ""
    )

ocumEvtEMSDebugEventReceived = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 16650)
)
ocumEvtEMSDebugEventReceived.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtEMSDebugEventReceived.setStatus(
        ""
    )

ocumEvtEMSEmergencyEventReceived = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 16660)
)
ocumEvtEMSEmergencyEventReceived.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtEMSEmergencyEventReceived.setStatus(
        ""
    )

ocumEvtEMSAlertEventReceived = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 16670)
)
ocumEvtEMSAlertEventReceived.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtEMSAlertEventReceived.setStatus(
        ""
    )

ocumEvtHeartbeatServiceStatusDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 16700)
)
ocumEvtHeartbeatServiceStatusDown.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtHeartbeatServiceStatusDown.setStatus(
        ""
    )

ocumEvtHeartbeatServiceStatusUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 16701)
)
ocumEvtHeartbeatServiceStatusUp.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtHeartbeatServiceStatusUp.setStatus(
        ""
    )

ocumEvtUnifiedManagerDiskSpaceNearlyFull = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 16800)
)
ocumEvtUnifiedManagerDiskSpaceNearlyFull.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtUnifiedManagerDiskSpaceNearlyFull.setStatus(
        ""
    )

ocumEvtUnifiedManagerDiskSpaceFull = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 16801)
)
ocumEvtUnifiedManagerDiskSpaceFull.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtUnifiedManagerDiskSpaceFull.setStatus(
        ""
    )

ocumEvtUnifiedManagerDiskSpaceNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 16802)
)
ocumEvtUnifiedManagerDiskSpaceNormal.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtUnifiedManagerDiskSpaceNormal.setStatus(
        ""
    )

ocumEvtUnifiedManagerDataNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 16813)
)
ocumEvtUnifiedManagerDataNormal.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtUnifiedManagerDataNormal.setStatus(
        ""
    )

ocumEvtUnifiedManagerDataMissingAnalyze = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 16814)
)
ocumEvtUnifiedManagerDataMissingAnalyze.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtUnifiedManagerDataMissingAnalyze.setStatus(
        ""
    )

ocumEvtUnifiedManagerDataMissingCollection = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 16815)
)
ocumEvtUnifiedManagerDataMissingCollection.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtUnifiedManagerDataMissingCollection.setStatus(
        ""
    )

ocumAggregateLatencyIncident = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 16820)
)
ocumAggregateLatencyIncident.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumAggregateLatencyIncident.setStatus(
        ""
    )

ocumAggregateLatencyWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 16821)
)
ocumAggregateLatencyWarning.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumAggregateLatencyWarning.setStatus(
        ""
    )

ocumAggregateLatencyCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 16822)
)
ocumAggregateLatencyCleared.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumAggregateLatencyCleared.setStatus(
        ""
    )

ocumAggregateIopsIncident = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 16830)
)
ocumAggregateIopsIncident.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumAggregateIopsIncident.setStatus(
        ""
    )

ocumAggregateIopsWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 16831)
)
ocumAggregateIopsWarning.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumAggregateIopsWarning.setStatus(
        ""
    )

ocumAggregateIopsCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 16832)
)
ocumAggregateIopsCleared.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumAggregateIopsCleared.setStatus(
        ""
    )

ocumAggregateMbpsIncident = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 16840)
)
ocumAggregateMbpsIncident.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumAggregateMbpsIncident.setStatus(
        ""
    )

ocumAggregateMbpsWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 16841)
)
ocumAggregateMbpsWarning.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumAggregateMbpsWarning.setStatus(
        ""
    )

ocumAggregateMbpsCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 16842)
)
ocumAggregateMbpsCleared.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumAggregateMbpsCleared.setStatus(
        ""
    )

ocumAggregatePerfCapacityUsedIncident = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 16850)
)
ocumAggregatePerfCapacityUsedIncident.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumAggregatePerfCapacityUsedIncident.setStatus(
        ""
    )

ocumAggregatePerfCapacityUsedWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 16851)
)
ocumAggregatePerfCapacityUsedWarning.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumAggregatePerfCapacityUsedWarning.setStatus(
        ""
    )

ocumAggregatePerfCapacityUsedCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 16852)
)
ocumAggregatePerfCapacityUsedCleared.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumAggregatePerfCapacityUsedCleared.setStatus(
        ""
    )

ocumAggregateUtilizationIncident = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 16860)
)
ocumAggregateUtilizationIncident.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumAggregateUtilizationIncident.setStatus(
        ""
    )

ocumAggregateUtilizationWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 16861)
)
ocumAggregateUtilizationWarning.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumAggregateUtilizationWarning.setStatus(
        ""
    )

ocumAggregateUtilizationCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 16862)
)
ocumAggregateUtilizationCleared.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumAggregateUtilizationCleared.setStatus(
        ""
    )

ocumNodeLatencyIncident = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 16870)
)
ocumNodeLatencyIncident.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumNodeLatencyIncident.setStatus(
        ""
    )

ocumNodeLatencyWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 16871)
)
ocumNodeLatencyWarning.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumNodeLatencyWarning.setStatus(
        ""
    )

ocumNodeLatencyCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 16872)
)
ocumNodeLatencyCleared.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumNodeLatencyCleared.setStatus(
        ""
    )

ocumNodeIopsIncident = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 16880)
)
ocumNodeIopsIncident.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumNodeIopsIncident.setStatus(
        ""
    )

ocumNodeIopsWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 16881)
)
ocumNodeIopsWarning.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumNodeIopsWarning.setStatus(
        ""
    )

ocumNodeIopsCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 16882)
)
ocumNodeIopsCleared.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumNodeIopsCleared.setStatus(
        ""
    )

ocumNodeMbpsIncident = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 16890)
)
ocumNodeMbpsIncident.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumNodeMbpsIncident.setStatus(
        ""
    )

ocumNodeMbpsWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 16891)
)
ocumNodeMbpsWarning.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumNodeMbpsWarning.setStatus(
        ""
    )

ocumNodeMbpsCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 16892)
)
ocumNodeMbpsCleared.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumNodeMbpsCleared.setStatus(
        ""
    )

ocumNodePerfCapacityUsedIncident = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 16900)
)
ocumNodePerfCapacityUsedIncident.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumNodePerfCapacityUsedIncident.setStatus(
        ""
    )

ocumNodePerfCapacityUsedWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 16901)
)
ocumNodePerfCapacityUsedWarning.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumNodePerfCapacityUsedWarning.setStatus(
        ""
    )

ocumNodePerfCapacityUsedCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 16902)
)
ocumNodePerfCapacityUsedCleared.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumNodePerfCapacityUsedCleared.setStatus(
        ""
    )

ocumNodePerfCapacityUsedTakeoverIncident = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 16910)
)
ocumNodePerfCapacityUsedTakeoverIncident.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumNodePerfCapacityUsedTakeoverIncident.setStatus(
        ""
    )

ocumNodePerfCapacityUsedTakeoverWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 16911)
)
ocumNodePerfCapacityUsedTakeoverWarning.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumNodePerfCapacityUsedTakeoverWarning.setStatus(
        ""
    )

ocumNodePerfCapacityUsedTakeoverCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 16912)
)
ocumNodePerfCapacityUsedTakeoverCleared.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumNodePerfCapacityUsedTakeoverCleared.setStatus(
        ""
    )

ocumNodeUtilizationIncident = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 16920)
)
ocumNodeUtilizationIncident.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumNodeUtilizationIncident.setStatus(
        ""
    )

ocumNodeUtilizationWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 16921)
)
ocumNodeUtilizationWarning.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumNodeUtilizationWarning.setStatus(
        ""
    )

ocumNodeUtilizationCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 16922)
)
ocumNodeUtilizationCleared.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumNodeUtilizationCleared.setStatus(
        ""
    )

ocumClusterIopsIncident = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 16930)
)
ocumClusterIopsIncident.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumClusterIopsIncident.setStatus(
        ""
    )

ocumClusterIopsWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 16931)
)
ocumClusterIopsWarning.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumClusterIopsWarning.setStatus(
        ""
    )

ocumClusterIopsCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 16932)
)
ocumClusterIopsCleared.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumClusterIopsCleared.setStatus(
        ""
    )

ocumClusterMbpsIncident = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 16940)
)
ocumClusterMbpsIncident.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumClusterMbpsIncident.setStatus(
        ""
    )

ocumClusterMbpsWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 16941)
)
ocumClusterMbpsWarning.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumClusterMbpsWarning.setStatus(
        ""
    )

ocumClusterMbpsCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 16942)
)
ocumClusterMbpsCleared.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumClusterMbpsCleared.setStatus(
        ""
    )

ocumNetworkPortUtilizationIncident = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 16950)
)
ocumNetworkPortUtilizationIncident.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumNetworkPortUtilizationIncident.setStatus(
        ""
    )

ocumNetworkPortUtilizationWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 16951)
)
ocumNetworkPortUtilizationWarning.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumNetworkPortUtilizationWarning.setStatus(
        ""
    )

ocumNetworkPortUtilizationCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 16952)
)
ocumNetworkPortUtilizationCleared.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumNetworkPortUtilizationCleared.setStatus(
        ""
    )

ocumNetworkPortMbpsIncident = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 16960)
)
ocumNetworkPortMbpsIncident.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumNetworkPortMbpsIncident.setStatus(
        ""
    )

ocumNetworkPortMbpsWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 16961)
)
ocumNetworkPortMbpsWarning.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumNetworkPortMbpsWarning.setStatus(
        ""
    )

ocumNetworkPortMbpsCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 16962)
)
ocumNetworkPortMbpsCleared.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumNetworkPortMbpsCleared.setStatus(
        ""
    )

ocumSvmLatencyIncident = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 16970)
)
ocumSvmLatencyIncident.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumSvmLatencyIncident.setStatus(
        ""
    )

ocumSvmLatencyWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 16971)
)
ocumSvmLatencyWarning.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumSvmLatencyWarning.setStatus(
        ""
    )

ocumSvmLatencyCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 16972)
)
ocumSvmLatencyCleared.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumSvmLatencyCleared.setStatus(
        ""
    )

ocumSvmIopsIncident = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 16980)
)
ocumSvmIopsIncident.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumSvmIopsIncident.setStatus(
        ""
    )

ocumSvmIopsWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 16981)
)
ocumSvmIopsWarning.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumSvmIopsWarning.setStatus(
        ""
    )

ocumSvmIopsCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 16982)
)
ocumSvmIopsCleared.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumSvmIopsCleared.setStatus(
        ""
    )

ocumSvmMbpsIncident = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 16990)
)
ocumSvmMbpsIncident.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumSvmMbpsIncident.setStatus(
        ""
    )

ocumSvmMbpsWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 16991)
)
ocumSvmMbpsWarning.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumSvmMbpsWarning.setStatus(
        ""
    )

ocumSvmMbpsCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 16992)
)
ocumSvmMbpsCleared.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumSvmMbpsCleared.setStatus(
        ""
    )

ocumVolumeLatencyIncident = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 17000)
)
ocumVolumeLatencyIncident.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumVolumeLatencyIncident.setStatus(
        ""
    )

ocumVolumeLatencyWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 17001)
)
ocumVolumeLatencyWarning.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumVolumeLatencyWarning.setStatus(
        ""
    )

ocumVolumeLatencyCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 17002)
)
ocumVolumeLatencyCleared.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumVolumeLatencyCleared.setStatus(
        ""
    )

ocumVolumeIopsIncident = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 17010)
)
ocumVolumeIopsIncident.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumVolumeIopsIncident.setStatus(
        ""
    )

ocumVolumeIopsWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 17011)
)
ocumVolumeIopsWarning.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumVolumeIopsWarning.setStatus(
        ""
    )

ocumVolumeIopsCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 17012)
)
ocumVolumeIopsCleared.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumVolumeIopsCleared.setStatus(
        ""
    )

ocumVolumeMbpsIncident = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 17020)
)
ocumVolumeMbpsIncident.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumVolumeMbpsIncident.setStatus(
        ""
    )

ocumVolumeMbpsWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 17021)
)
ocumVolumeMbpsWarning.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumVolumeMbpsWarning.setStatus(
        ""
    )

ocumVolumeMbpsCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 17022)
)
ocumVolumeMbpsCleared.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumVolumeMbpsCleared.setStatus(
        ""
    )

ocumVolumeCacheMissRatioIncident = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 17030)
)
ocumVolumeCacheMissRatioIncident.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumVolumeCacheMissRatioIncident.setStatus(
        ""
    )

ocumVolumeCacheMissRatioWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 17031)
)
ocumVolumeCacheMissRatioWarning.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumVolumeCacheMissRatioWarning.setStatus(
        ""
    )

ocumVolumeCacheMissRatioCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 17032)
)
ocumVolumeCacheMissRatioCleared.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumVolumeCacheMissRatioCleared.setStatus(
        ""
    )

ocumVolumeLatencyIopsIncident = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 17040)
)
ocumVolumeLatencyIopsIncident.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumVolumeLatencyIopsIncident.setStatus(
        ""
    )

ocumVolumeLatencyIopsWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 17041)
)
ocumVolumeLatencyIopsWarning.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumVolumeLatencyIopsWarning.setStatus(
        ""
    )

ocumVolumeLatencyIopsCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 17042)
)
ocumVolumeLatencyIopsCleared.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumVolumeLatencyIopsCleared.setStatus(
        ""
    )

ocumVolumeLatencyMbpsIncident = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 17050)
)
ocumVolumeLatencyMbpsIncident.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumVolumeLatencyMbpsIncident.setStatus(
        ""
    )

ocumVolumeLatencyMbpsWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 17051)
)
ocumVolumeLatencyMbpsWarning.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumVolumeLatencyMbpsWarning.setStatus(
        ""
    )

ocumVolumeLatencyMbpsCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 17052)
)
ocumVolumeLatencyMbpsCleared.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumVolumeLatencyMbpsCleared.setStatus(
        ""
    )

ocumVolumeLatencyAggregatePerfCapacityUsedIncident = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 17060)
)
ocumVolumeLatencyAggregatePerfCapacityUsedIncident.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumVolumeLatencyAggregatePerfCapacityUsedIncident.setStatus(
        ""
    )

ocumVolumeLatencyAggregatePerfCapacityUsedWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 17061)
)
ocumVolumeLatencyAggregatePerfCapacityUsedWarning.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumVolumeLatencyAggregatePerfCapacityUsedWarning.setStatus(
        ""
    )

ocumVolumeLatencyAggregatePerfCapacityUsedCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 17062)
)
ocumVolumeLatencyAggregatePerfCapacityUsedCleared.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumVolumeLatencyAggregatePerfCapacityUsedCleared.setStatus(
        ""
    )

ocumVolumeLatencyAggregateUtilizationIncident = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 17070)
)
ocumVolumeLatencyAggregateUtilizationIncident.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumVolumeLatencyAggregateUtilizationIncident.setStatus(
        ""
    )

ocumVolumeLatencyAggregateUtilizationWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 17071)
)
ocumVolumeLatencyAggregateUtilizationWarning.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumVolumeLatencyAggregateUtilizationWarning.setStatus(
        ""
    )

ocumVolumeLatencyAggregateUtilizationCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 17072)
)
ocumVolumeLatencyAggregateUtilizationCleared.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumVolumeLatencyAggregateUtilizationCleared.setStatus(
        ""
    )

ocumVolumeLatencyNodePerfCapacityUsedIncident = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 17080)
)
ocumVolumeLatencyNodePerfCapacityUsedIncident.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumVolumeLatencyNodePerfCapacityUsedIncident.setStatus(
        ""
    )

ocumVolumeLatencyNodePerfCapacityUsedWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 17081)
)
ocumVolumeLatencyNodePerfCapacityUsedWarning.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumVolumeLatencyNodePerfCapacityUsedWarning.setStatus(
        ""
    )

ocumVolumeLatencyNodePerfCapacityUsedCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 17082)
)
ocumVolumeLatencyNodePerfCapacityUsedCleared.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumVolumeLatencyNodePerfCapacityUsedCleared.setStatus(
        ""
    )

ocumVolumeLatencyAggregatePerfCapacityUsedTakeoverIncident = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 17090)
)
ocumVolumeLatencyAggregatePerfCapacityUsedTakeoverIncident.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumVolumeLatencyAggregatePerfCapacityUsedTakeoverIncident.setStatus(
        ""
    )

ocumVolumeLatencyAggregatePerfCapacityUsedTakeoverWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 17091)
)
ocumVolumeLatencyAggregatePerfCapacityUsedTakeoverWarning.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumVolumeLatencyAggregatePerfCapacityUsedTakeoverWarning.setStatus(
        ""
    )

ocumVolumeLatencyAggregatePerfCapacityUsedTakeoverCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 17092)
)
ocumVolumeLatencyAggregatePerfCapacityUsedTakeoverCleared.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumVolumeLatencyAggregatePerfCapacityUsedTakeoverCleared.setStatus(
        ""
    )

ocumVolumeLatencyNodeUtilizationIncident = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 17100)
)
ocumVolumeLatencyNodeUtilizationIncident.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumVolumeLatencyNodeUtilizationIncident.setStatus(
        ""
    )

ocumVolumeLatencyNodeUtilizationWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 17101)
)
ocumVolumeLatencyNodeUtilizationWarning.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumVolumeLatencyNodeUtilizationWarning.setStatus(
        ""
    )

ocumVolumeLatencyNodeUtilizationCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 17102)
)
ocumVolumeLatencyNodeUtilizationCleared.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumVolumeLatencyNodeUtilizationCleared.setStatus(
        ""
    )

ocumLunLatencyIncident = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 17110)
)
ocumLunLatencyIncident.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumLunLatencyIncident.setStatus(
        ""
    )

ocumLunLatencyWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 17111)
)
ocumLunLatencyWarning.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumLunLatencyWarning.setStatus(
        ""
    )

ocumLunLatencyCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 17112)
)
ocumLunLatencyCleared.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumLunLatencyCleared.setStatus(
        ""
    )

ocumLunIopsIncident = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 17120)
)
ocumLunIopsIncident.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumLunIopsIncident.setStatus(
        ""
    )

ocumLunIopsWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 17121)
)
ocumLunIopsWarning.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumLunIopsWarning.setStatus(
        ""
    )

ocumLunIopsCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 17122)
)
ocumLunIopsCleared.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumLunIopsCleared.setStatus(
        ""
    )

ocumLunMbpsIncident = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 17130)
)
ocumLunMbpsIncident.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumLunMbpsIncident.setStatus(
        ""
    )

ocumLunMbpsWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 17131)
)
ocumLunMbpsWarning.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumLunMbpsWarning.setStatus(
        ""
    )

ocumLunMbpsCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 17132)
)
ocumLunMbpsCleared.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumLunMbpsCleared.setStatus(
        ""
    )

ocumLunLatencyIopsIncident = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 17140)
)
ocumLunLatencyIopsIncident.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumLunLatencyIopsIncident.setStatus(
        ""
    )

ocumLunLatencyIopsWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 17141)
)
ocumLunLatencyIopsWarning.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumLunLatencyIopsWarning.setStatus(
        ""
    )

ocumLunLatencyIopsCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 17142)
)
ocumLunLatencyIopsCleared.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumLunLatencyIopsCleared.setStatus(
        ""
    )

ocumLunLatencyMbpsIncident = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 17150)
)
ocumLunLatencyMbpsIncident.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumLunLatencyMbpsIncident.setStatus(
        ""
    )

ocumLunLatencyMbpsWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 17151)
)
ocumLunLatencyMbpsWarning.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumLunLatencyMbpsWarning.setStatus(
        ""
    )

ocumLunLatencyMbpsCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 17152)
)
ocumLunLatencyMbpsCleared.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumLunLatencyMbpsCleared.setStatus(
        ""
    )

ocumLunLatencyAggregatePerfCapacityUsedIncident = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 17160)
)
ocumLunLatencyAggregatePerfCapacityUsedIncident.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumLunLatencyAggregatePerfCapacityUsedIncident.setStatus(
        ""
    )

ocumLunLatencyAggregatePerfCapacityUsedWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 17161)
)
ocumLunLatencyAggregatePerfCapacityUsedWarning.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumLunLatencyAggregatePerfCapacityUsedWarning.setStatus(
        ""
    )

ocumLunLatencyAggregatePerfCapacityUsedCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 17162)
)
ocumLunLatencyAggregatePerfCapacityUsedCleared.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumLunLatencyAggregatePerfCapacityUsedCleared.setStatus(
        ""
    )

ocumLunLatencyAggregateUtilizationIncident = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 17170)
)
ocumLunLatencyAggregateUtilizationIncident.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumLunLatencyAggregateUtilizationIncident.setStatus(
        ""
    )

ocumLunLatencyAggregateUtilizationWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 17171)
)
ocumLunLatencyAggregateUtilizationWarning.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumLunLatencyAggregateUtilizationWarning.setStatus(
        ""
    )

ocumLunLatencyAggregateUtilizationCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 17172)
)
ocumLunLatencyAggregateUtilizationCleared.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumLunLatencyAggregateUtilizationCleared.setStatus(
        ""
    )

ocumLunLatencyNodePerfCapacityUsedIncident = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 17180)
)
ocumLunLatencyNodePerfCapacityUsedIncident.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumLunLatencyNodePerfCapacityUsedIncident.setStatus(
        ""
    )

ocumLunLatencyNodePerfCapacityUsedWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 17181)
)
ocumLunLatencyNodePerfCapacityUsedWarning.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumLunLatencyNodePerfCapacityUsedWarning.setStatus(
        ""
    )

ocumLunLatencyNodePerfCapacityUsedCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 17182)
)
ocumLunLatencyNodePerfCapacityUsedCleared.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumLunLatencyNodePerfCapacityUsedCleared.setStatus(
        ""
    )

ocumLunLatencyAggregatePerfCapacityUsedTakeoverIncident = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 17190)
)
ocumLunLatencyAggregatePerfCapacityUsedTakeoverIncident.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumLunLatencyAggregatePerfCapacityUsedTakeoverIncident.setStatus(
        ""
    )

ocumLunLatencyAggregatePerfCapacityUsedTakeoverWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 17191)
)
ocumLunLatencyAggregatePerfCapacityUsedTakeoverWarning.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumLunLatencyAggregatePerfCapacityUsedTakeoverWarning.setStatus(
        ""
    )

ocumLunLatencyAggregatePerfCapacityUsedTakeoverCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 17192)
)
ocumLunLatencyAggregatePerfCapacityUsedTakeoverCleared.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumLunLatencyAggregatePerfCapacityUsedTakeoverCleared.setStatus(
        ""
    )

ocumLunLatencyNodeUtilizationIncident = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 17200)
)
ocumLunLatencyNodeUtilizationIncident.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumLunLatencyNodeUtilizationIncident.setStatus(
        ""
    )

ocumLunLatencyNodeUtilizationWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 17201)
)
ocumLunLatencyNodeUtilizationWarning.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumLunLatencyNodeUtilizationWarning.setStatus(
        ""
    )

ocumLunLatencyNodeUtilizationCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 17202)
)
ocumLunLatencyNodeUtilizationCleared.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumLunLatencyNodeUtilizationCleared.setStatus(
        ""
    )

ocumNetworkLifMbpsIncident = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 17210)
)
ocumNetworkLifMbpsIncident.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumNetworkLifMbpsIncident.setStatus(
        ""
    )

ocumNetworkLifMbpsWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 17211)
)
ocumNetworkLifMbpsWarning.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumNetworkLifMbpsWarning.setStatus(
        ""
    )

ocumNetworkLifMbpsCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 17212)
)
ocumNetworkLifMbpsCleared.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumNetworkLifMbpsCleared.setStatus(
        ""
    )

ocumFcpPortUtilizationIncident = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 17220)
)
ocumFcpPortUtilizationIncident.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumFcpPortUtilizationIncident.setStatus(
        ""
    )

ocumFcpPortUtilizationWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 17221)
)
ocumFcpPortUtilizationWarning.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumFcpPortUtilizationWarning.setStatus(
        ""
    )

ocumFcpPortUtilizationCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 17222)
)
ocumFcpPortUtilizationCleared.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumFcpPortUtilizationCleared.setStatus(
        ""
    )

ocumFcpPortMbpsIncident = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 17230)
)
ocumFcpPortMbpsIncident.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumFcpPortMbpsIncident.setStatus(
        ""
    )

ocumFcpPortMbpsWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 17231)
)
ocumFcpPortMbpsWarning.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumFcpPortMbpsWarning.setStatus(
        ""
    )

ocumFcpPortMbpsCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 17232)
)
ocumFcpPortMbpsCleared.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumFcpPortMbpsCleared.setStatus(
        ""
    )

ocumAggregateDisksOverUtilizedWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 17240)
)
ocumAggregateDisksOverUtilizedWarning.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumAggregateDisksOverUtilizedWarning.setStatus(
        ""
    )

ocumAggregateDisksOverUtilizedCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 17241)
)
ocumAggregateDisksOverUtilizedCleared.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumAggregateDisksOverUtilizedCleared.setStatus(
        ""
    )

ocumNodeHaPairOverUtilizedInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 17250)
)
ocumNodeHaPairOverUtilizedInformation.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumNodeHaPairOverUtilizedInformation.setStatus(
        ""
    )

ocumNodeHaPairOverUtilizedCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 17251)
)
ocumNodeHaPairOverUtilizedCleared.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumNodeHaPairOverUtilizedCleared.setStatus(
        ""
    )

ocumNodeDiskFragmentationWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 17260)
)
ocumNodeDiskFragmentationWarning.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumNodeDiskFragmentationWarning.setStatus(
        ""
    )

ocumNodeDiskFragmentationCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 17261)
)
ocumNodeDiskFragmentationCleared.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumNodeDiskFragmentationCleared.setStatus(
        ""
    )

ocumNodeOverUtilizedWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 17270)
)
ocumNodeOverUtilizedWarning.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumNodeOverUtilizedWarning.setStatus(
        ""
    )

ocumNodeOverUtilizedCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 17271)
)
ocumNodeOverUtilizedCleared.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumNodeOverUtilizedCleared.setStatus(
        ""
    )

ocumClusterDynamicEventWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 17280)
)
ocumClusterDynamicEventWarning.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumClusterDynamicEventWarning.setStatus(
        ""
    )

ocumClusterDynamicEventCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 17281)
)
ocumClusterDynamicEventCleared.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumClusterDynamicEventCleared.setStatus(
        ""
    )

ocumNodeDynamicEventWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 17290)
)
ocumNodeDynamicEventWarning.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumNodeDynamicEventWarning.setStatus(
        ""
    )

ocumNodeDynamicEventCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 17291)
)
ocumNodeDynamicEventCleared.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumNodeDynamicEventCleared.setStatus(
        ""
    )

ocumAggregateDynamicEventWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 17300)
)
ocumAggregateDynamicEventWarning.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumAggregateDynamicEventWarning.setStatus(
        ""
    )

ocumAggregateDynamicEventCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 17301)
)
ocumAggregateDynamicEventCleared.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumAggregateDynamicEventCleared.setStatus(
        ""
    )

ocumFcpLifMbpsIncident = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 17310)
)
ocumFcpLifMbpsIncident.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumFcpLifMbpsIncident.setStatus(
        ""
    )

ocumFcpLifMbpsWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 17311)
)
ocumFcpLifMbpsWarning.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumFcpLifMbpsWarning.setStatus(
        ""
    )

ocumFcpLifMbpsCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 17312)
)
ocumFcpLifMbpsCleared.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumFcpLifMbpsCleared.setStatus(
        ""
    )

ocumEvtClusterFabricpoolLicenseCapacityLimitExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 17321)
)
ocumEvtClusterFabricpoolLicenseCapacityLimitExceeded.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtClusterFabricpoolLicenseCapacityLimitExceeded.setStatus(
        ""
    )

ocumEvtClusterFabricpoolLicenseCapacityLimitNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 17322)
)
ocumEvtClusterFabricpoolLicenseCapacityLimitNormal.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtClusterFabricpoolLicenseCapacityLimitNormal.setStatus(
        ""
    )

ocumEventExternalCapacityUnreachable = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 17331)
)
ocumEventExternalCapacityUnreachable.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEventExternalCapacityUnreachable.setStatus(
        ""
    )

ocumEventExternalCapacityReachable = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 17332)
)
ocumEventExternalCapacityReachable.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEventExternalCapacityReachable.setStatus(
        ""
    )

ocumEventExternalCapacityPartiallyReachable = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 17333)
)
ocumEventExternalCapacityPartiallyReachable.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEventExternalCapacityPartiallyReachable.setStatus(
        ""
    )

ocumQosVolumeMaxIopsWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 17340)
)
ocumQosVolumeMaxIopsWarning.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumQosVolumeMaxIopsWarning.setStatus(
        ""
    )

ocumQosVolumeMaxIopsCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 17341)
)
ocumQosVolumeMaxIopsCleared.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumQosVolumeMaxIopsCleared.setStatus(
        ""
    )

ocumQosVolumeMaxMbpsWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 17350)
)
ocumQosVolumeMaxMbpsWarning.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumQosVolumeMaxMbpsWarning.setStatus(
        ""
    )

ocumQosVolumeMaxMbpsCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 17351)
)
ocumQosVolumeMaxMbpsCleared.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumQosVolumeMaxMbpsCleared.setStatus(
        ""
    )

ocumQosLunMaxIopsWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 17360)
)
ocumQosLunMaxIopsWarning.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumQosLunMaxIopsWarning.setStatus(
        ""
    )

ocumQosLunMaxIopsCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 17361)
)
ocumQosLunMaxIopsCleared.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumQosLunMaxIopsCleared.setStatus(
        ""
    )

ocumQosLunMaxMbpsWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 17370)
)
ocumQosLunMaxMbpsWarning.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumQosLunMaxMbpsWarning.setStatus(
        ""
    )

ocumQosLunMaxMbpsCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 17371)
)
ocumQosLunMaxMbpsCleared.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumQosLunMaxMbpsCleared.setStatus(
        ""
    )

ocumQosVolumeMaxIopsPerTbWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 17380)
)
ocumQosVolumeMaxIopsPerTbWarning.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumQosVolumeMaxIopsPerTbWarning.setStatus(
        ""
    )

ocumQosVolumeMaxIopsPerTbCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 17381)
)
ocumQosVolumeMaxIopsPerTbCleared.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumQosVolumeMaxIopsPerTbCleared.setStatus(
        ""
    )

ocumQosLunMaxIopsPerTbWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 17390)
)
ocumQosLunMaxIopsPerTbWarning.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumQosLunMaxIopsPerTbWarning.setStatus(
        ""
    )

ocumQosLunMaxIopsPerTbCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 17391)
)
ocumQosLunMaxIopsPerTbCleared.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumQosLunMaxIopsPerTbCleared.setStatus(
        ""
    )

ocumArlNetraCaCheckFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 17400)
)
ocumArlNetraCaCheckFailed.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumArlNetraCaCheckFailed.setStatus(
        ""
    )

ocumGbNetraCaCheckFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 17410)
)
ocumGbNetraCaCheckFailed.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumGbNetraCaCheckFailed.setStatus(
        ""
    )

ocumObjstoreHostUnresolvable = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 17420)
)
ocumObjstoreHostUnresolvable.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumObjstoreHostUnresolvable.setStatus(
        ""
    )

ocumObjstoreInterClusterLifDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 17430)
)
ocumObjstoreInterClusterLifDown.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumObjstoreInterClusterLifDown.setStatus(
        ""
    )

ocumWaflCaLatencyThreashold = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 17440)
)
ocumWaflCaLatencyThreashold.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumWaflCaLatencyThreashold.setStatus(
        ""
    )

ocumS3BucketSignatureMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 17450)
)
ocumS3BucketSignatureMismatch.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumS3BucketSignatureMismatch.setStatus(
        ""
    )

ocumCloudAwsMetadataConnFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 17460)
)
ocumCloudAwsMetadataConnFail.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumCloudAwsMetadataConnFail.setStatus(
        ""
    )

ocumCloudAwsIamCredsExpired = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 17470)
)
ocumCloudAwsIamCredsExpired.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumCloudAwsIamCredsExpired.setStatus(
        ""
    )

ocumCloudAwsIamCredsInvalid = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 17471)
)
ocumCloudAwsIamCredsInvalid.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumCloudAwsIamCredsInvalid.setStatus(
        ""
    )

ocumCloudAwsIamCredsNotFound = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 17472)
)
ocumCloudAwsIamCredsNotFound.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumCloudAwsIamCredsNotFound.setStatus(
        ""
    )

ocumCloudAwsIamCredsNotInitialized = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 17473)
)
ocumCloudAwsIamCredsNotInitialized.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumCloudAwsIamCredsNotInitialized.setStatus(
        ""
    )

ocumCloudAwsIamRoleInvalid = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 17480)
)
ocumCloudAwsIamRoleInvalid.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumCloudAwsIamRoleInvalid.setStatus(
        ""
    )

ocumCloudAwsIamRoleNotFound = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 17481)
)
ocumCloudAwsIamRoleNotFound.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumCloudAwsIamRoleNotFound.setStatus(
        ""
    )

ocumQosMonitorMemoryMaxed = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 17490)
)
ocumQosMonitorMemoryMaxed.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumQosMonitorMemoryMaxed.setStatus(
        ""
    )

ocumQosMonitorMemoryAbated = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 17491)
)
ocumQosMonitorMemoryAbated.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumQosMonitorMemoryAbated.setStatus(
        ""
    )

ocumQosViolationReport = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 17500)
)
ocumQosViolationReport.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumQosViolationReport.setStatus(
        ""
    )

ocumEvtUnifiedManagerMemoryLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 17510)
)
ocumEvtUnifiedManagerMemoryLow.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtUnifiedManagerMemoryLow.setStatus(
        ""
    )

ocumEvtUnifiedManagerMemoryAlmostOut = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 17511)
)
ocumEvtUnifiedManagerMemoryAlmostOut.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtUnifiedManagerMemoryAlmostOut.setStatus(
        ""
    )

ocumEvtUnifiedManagerMemoryNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 17512)
)
ocumEvtUnifiedManagerMemoryNormal.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtUnifiedManagerMemoryNormal.setStatus(
        ""
    )

nvmeNamespaceStatusOnline = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 17520)
)
nvmeNamespaceStatusOnline.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    nvmeNamespaceStatusOnline.setStatus(
        ""
    )

nvmeNamespaceStatusOffline = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 17521)
)
nvmeNamespaceStatusOffline.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    nvmeNamespaceStatusOffline.setStatus(
        ""
    )

nvmeNamespaceSpaceOutOfSpace = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 17530)
)
nvmeNamespaceSpaceOutOfSpace.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    nvmeNamespaceSpaceOutOfSpace.setStatus(
        ""
    )

nvmeNamespaceDestroy = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 17540)
)
nvmeNamespaceDestroy.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    nvmeNamespaceDestroy.setStatus(
        ""
    )

flexGroupConstituentsHaveSpaceIssues = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 17550)
)
flexGroupConstituentsHaveSpaceIssues.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    flexGroupConstituentsHaveSpaceIssues.setStatus(
        ""
    )

flexGroupConstituentsSpaceStatusAllOK = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 17551)
)
flexGroupConstituentsSpaceStatusAllOK.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    flexGroupConstituentsSpaceStatusAllOK.setStatus(
        ""
    )

flexGroupConstituentsHaveInodesIssues = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 17560)
)
flexGroupConstituentsHaveInodesIssues.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    flexGroupConstituentsHaveInodesIssues.setStatus(
        ""
    )

flexGroupConstituentsInodesStatusAllOK = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 17561)
)
flexGroupConstituentsInodesStatusAllOK.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    flexGroupConstituentsInodesStatusAllOK.setStatus(
        ""
    )

ocumNvmeNamespaceLatencyIncident = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 17562)
)
ocumNvmeNamespaceLatencyIncident.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumNvmeNamespaceLatencyIncident.setStatus(
        ""
    )

ocumNvmeNamespaceLatencyWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 17563)
)
ocumNvmeNamespaceLatencyWarning.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumNvmeNamespaceLatencyWarning.setStatus(
        ""
    )

ocumNvmeNamespaceLatencyCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 17564)
)
ocumNvmeNamespaceLatencyCleared.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumNvmeNamespaceLatencyCleared.setStatus(
        ""
    )

ocumNvmeNamespaceIopsIncident = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 17565)
)
ocumNvmeNamespaceIopsIncident.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumNvmeNamespaceIopsIncident.setStatus(
        ""
    )

ocumNvmeNamespaceIopsWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 17566)
)
ocumNvmeNamespaceIopsWarning.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumNvmeNamespaceIopsWarning.setStatus(
        ""
    )

ocumNvmeNamespaceIopsCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 17567)
)
ocumNvmeNamespaceIopsCleared.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumNvmeNamespaceIopsCleared.setStatus(
        ""
    )

ocumNvmeNamespaceMbpsIncident = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 17568)
)
ocumNvmeNamespaceMbpsIncident.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumNvmeNamespaceMbpsIncident.setStatus(
        ""
    )

ocumNvmeNamespaceMbpsWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 17569)
)
ocumNvmeNamespaceMbpsWarning.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumNvmeNamespaceMbpsWarning.setStatus(
        ""
    )

ocumNvmeNamespaceMbpsCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 17570)
)
ocumNvmeNamespaceMbpsCleared.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumNvmeNamespaceMbpsCleared.setStatus(
        ""
    )

ocumNvmeNamespaceLatencyIopsIncident = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 17571)
)
ocumNvmeNamespaceLatencyIopsIncident.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumNvmeNamespaceLatencyIopsIncident.setStatus(
        ""
    )

ocumNvmeNamespaceLatencyIopsWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 17572)
)
ocumNvmeNamespaceLatencyIopsWarning.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumNvmeNamespaceLatencyIopsWarning.setStatus(
        ""
    )

ocumNvmeNamespaceLatencyIopsCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 17573)
)
ocumNvmeNamespaceLatencyIopsCleared.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumNvmeNamespaceLatencyIopsCleared.setStatus(
        ""
    )

ocumNvmeNamespaceLatencyMbpsIncident = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 17574)
)
ocumNvmeNamespaceLatencyMbpsIncident.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumNvmeNamespaceLatencyMbpsIncident.setStatus(
        ""
    )

ocumNvmeNamespaceLatencyMbpsWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 17575)
)
ocumNvmeNamespaceLatencyMbpsWarning.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumNvmeNamespaceLatencyMbpsWarning.setStatus(
        ""
    )

ocumNvmeNamespaceLatencyMbpsCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 17576)
)
ocumNvmeNamespaceLatencyMbpsCleared.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumNvmeNamespaceLatencyMbpsCleared.setStatus(
        ""
    )

ocumNvmfFcLifMbpsIncident = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 17577)
)
ocumNvmfFcLifMbpsIncident.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumNvmfFcLifMbpsIncident.setStatus(
        ""
    )

ocumNvmfFcLifMbpsWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 17578)
)
ocumNvmfFcLifMbpsWarning.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumNvmfFcLifMbpsWarning.setStatus(
        ""
    )

ocumNvmfFcLifMbpsCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 17579)
)
ocumNvmfFcLifMbpsCleared.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumNvmfFcLifMbpsCleared.setStatus(
        ""
    )

objectMaintenanceWindowStarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 17580)
)
objectMaintenanceWindowStarted.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    objectMaintenanceWindowStarted.setStatus(
        ""
    )

objectMaintenanceWindowEnded = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 17581)
)
objectMaintenanceWindowEnded.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    objectMaintenanceWindowEnded.setStatus(
        ""
    )

ocumDynamicEventWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 17590)
)
ocumDynamicEventWarning.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumDynamicEventWarning.setStatus(
        ""
    )

ocumDynamicEventCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 17591)
)
ocumDynamicEventCleared.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumDynamicEventCleared.setStatus(
        ""
    )

syncSnapmirrorRelationshipOutofsync = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 17600)
)
syncSnapmirrorRelationshipOutofsync.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    syncSnapmirrorRelationshipOutofsync.setStatus(
        ""
    )

syncSnapmirrorRelationshipInSync = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 17601)
)
syncSnapmirrorRelationshipInSync.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    syncSnapmirrorRelationshipInSync.setStatus(
        ""
    )

syncSnapmirrorRelationshipAutoSyncRetryFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 17602)
)
syncSnapmirrorRelationshipAutoSyncRetryFailed.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    syncSnapmirrorRelationshipAutoSyncRetryFailed.setStatus(
        ""
    )

volumeLogicalSpaceNearlyFull = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 17610)
)
volumeLogicalSpaceNearlyFull.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    volumeLogicalSpaceNearlyFull.setStatus(
        ""
    )

volumeLogicalSpaceFull = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 17611)
)
volumeLogicalSpaceFull.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    volumeLogicalSpaceFull.setStatus(
        ""
    )

volumeLogicalSpaceAllOK = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 17612)
)
volumeLogicalSpaceAllOK.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    volumeLogicalSpaceAllOK.setStatus(
        ""
    )

ocumQosVolumeMaxIopsBlocksizePerTbWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 17613)
)
ocumQosVolumeMaxIopsBlocksizePerTbWarning.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumQosVolumeMaxIopsBlocksizePerTbWarning.setStatus(
        ""
    )

ocumQosVolumeMaxIopsBlocksizePerTbCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 17614)
)
ocumQosVolumeMaxIopsBlocksizePerTbCleared.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumQosVolumeMaxIopsBlocksizePerTbCleared.setStatus(
        ""
    )

clusterCapacityTierPlanningWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 17700)
)
clusterCapacityTierPlanningWarning.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    clusterCapacityTierPlanningWarning.setStatus(
        ""
    )

clusterCapacityTierPlanningCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 17701)
)
clusterCapacityTierPlanningCleared.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    clusterCapacityTierPlanningCleared.setStatus(
        ""
    )

waflVolAutoSizeFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 17710)
)
waflVolAutoSizeFail.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    waflVolAutoSizeFail.setStatus(
        ""
    )

waflVolAutoSizeDone = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 17711)
)
waflVolAutoSizeDone.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    waflVolAutoSizeDone.setStatus(
        ""
    )

lunDestroy = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 17720)
)
lunDestroy.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    lunDestroy.setStatus(
        ""
    )

nbladeCifsManyAuths = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 17730)
)
nbladeCifsManyAuths.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    nbladeCifsManyAuths.setStatus(
        ""
    )

nbladeCifsMaxOpenSameFile = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 17731)
)
nbladeCifsMaxOpenSameFile.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    nbladeCifsMaxOpenSameFile.setStatus(
        ""
    )

nbladeCifsMaxSessPerUsrConn = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 17732)
)
nbladeCifsMaxSessPerUsrConn.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    nbladeCifsMaxSessPerUsrConn.setStatus(
        ""
    )

nbladeCifsNbNameConflict = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 17734)
)
nbladeCifsNbNameConflict.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    nbladeCifsNbNameConflict.setStatus(
        ""
    )

nbladeCifsNoPrivShare = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 17735)
)
nbladeCifsNoPrivShare.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    nbladeCifsNoPrivShare.setStatus(
        ""
    )

nbladeVscanVirusDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 17740)
)
nbladeVscanVirusDetected.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    nbladeVscanVirusDetected.setStatus(
        ""
    )

nbladeVscanNoScannerConn = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 17741)
)
nbladeVscanNoScannerConn.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    nbladeVscanNoScannerConn.setStatus(
        ""
    )

nbladeVscanNoRegdScanner = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 17742)
)
nbladeVscanNoRegdScanner.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    nbladeVscanNoRegdScanner.setStatus(
        ""
    )

nbladeVscanConnInactive = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 17744)
)
nbladeVscanConnInactive.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    nbladeVscanConnInactive.setStatus(
        ""
    )

nbladeVscanConnBackPressure = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 17745)
)
nbladeVscanConnBackPressure.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    nbladeVscanConnBackPressure.setStatus(
        ""
    )

nbladeVscanBadUserPrivAccess = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 17746)
)
nbladeVscanBadUserPrivAccess.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    nbladeVscanBadUserPrivAccess.setStatus(
        ""
    )

nbladeNfsv4PoolEXhaust = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 17750)
)
nbladeNfsv4PoolEXhaust.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    nbladeNfsv4PoolEXhaust.setStatus(
        ""
    )

cifsShadowCopyFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 17760)
)
cifsShadowCopyFailure.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    cifsShadowCopyFailure.setStatus(
        ""
    )

clusterFabricPoolNearlyFull = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 17770)
)
clusterFabricPoolNearlyFull.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    clusterFabricPoolNearlyFull.setStatus(
        ""
    )

oscSignatureMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 17780)
)
oscSignatureMismatch.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    oscSignatureMismatch.setStatus(
        ""
    )

arlNetraCaCheckFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 17790)
)
arlNetraCaCheckFailed.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    arlNetraCaCheckFailed.setStatus(
        ""
    )

gbNetraCaCheckFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 17791)
)
gbNetraCaCheckFailed.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    gbNetraCaCheckFailed.setStatus(
        ""
    )

nvmfGracePeriodStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 17800)
)
nvmfGracePeriodStart.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    nvmfGracePeriodStart.setStatus(
        ""
    )

nvmfGracePeriodActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 17801)
)
nvmfGracePeriodActive.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    nvmfGracePeriodActive.setStatus(
        ""
    )

nvmfGracePeriodExpired = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 17802)
)
nvmfGracePeriodExpired.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    nvmfGracePeriodExpired.setStatus(
        ""
    )

ocumEvtLunHaPartnerPathActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 138512)
)
ocumEvtLunHaPartnerPathActive.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtLunHaPartnerPathActive.setStatus(
        ""
    )

ocumEvtLunHaPartnerPathInActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 5, 1, 0, 138513)
)
ocumEvtLunHaPartnerPathInActive.setObjects(
      *(("ONCOMMAND-MANAGER-MIB", "ocumSystemId"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSeverity"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventImpactLevel"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventTimestamp"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessage"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventMessageDetails"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceType"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceHealthStatus"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceScopedFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterResourceKey"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventSourceClusterFullName"),
        ("ONCOMMAND-MANAGER-MIB", "ocumEventState"))
)
if mibBuilder.loadTexts:
    ocumEvtLunHaPartnerPathInActive.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ONCOMMAND-MANAGER-MIB",
    **{"DisplayString": DisplayString,
       "netappOnCommandUnifiedManager": netappOnCommandUnifiedManager,
       "ocumAlertTest": ocumAlertTest,
       "ocumEvtAggregate64BitUpgrade": ocumEvtAggregate64BitUpgrade,
       "ocumEvtAggregateDiscovered": ocumEvtAggregateDiscovered,
       "ocumEvtAggregateStateFailed": ocumEvtAggregateStateFailed,
       "ocumEvtAggregateStateRestricted": ocumEvtAggregateStateRestricted,
       "ocumEvtAggregateStateOnline": ocumEvtAggregateStateOnline,
       "ocumEvtAggregateStateOffline": ocumEvtAggregateStateOffline,
       "ocumEvtAggregateRaidStateNormal": ocumEvtAggregateRaidStateNormal,
       "ocumEvtAggregateRaidStateDegraded": ocumEvtAggregateRaidStateDegraded,
       "ocumEvtAggregateRaidStateReconstructing": ocumEvtAggregateRaidStateReconstructing,
       "ocumEvtAggregateSpaceOk": ocumEvtAggregateSpaceOk,
       "ocumEvtAggregateNearlyFull": ocumEvtAggregateNearlyFull,
       "ocumEvtAggregateFull": ocumEvtAggregateFull,
       "ocumEvtAggregateDaysUntilFullNotSoon": ocumEvtAggregateDaysUntilFullNotSoon,
       "ocumEvtAggregateDaysUntilFullSoon": ocumEvtAggregateDaysUntilFullSoon,
       "ocumEvtAggregateNotOvercommited": ocumEvtAggregateNotOvercommited,
       "ocumEvtAggregateAlmostOvercommitted": ocumEvtAggregateAlmostOvercommitted,
       "ocumEvtAggregateOvercommitted": ocumEvtAggregateOvercommitted,
       "ocumEvtAggregateSnapReserveOk": ocumEvtAggregateSnapReserveOk,
       "ocumEvtAggregateSnapReserveFull": ocumEvtAggregateSnapReserveFull,
       "ocumEvtAggregateGrowthRateOk": ocumEvtAggregateGrowthRateOk,
       "ocumEvtAggregateGrowthRateAbnormal": ocumEvtAggregateGrowthRateAbnormal,
       "ocumEvtAggregateDeleted": ocumEvtAggregateDeleted,
       "ocumEvtAggregateRenamed": ocumEvtAggregateRenamed,
       "ocumEvtMetroClusterAggregateLeftBehindFixed": ocumEvtMetroClusterAggregateLeftBehindFixed,
       "ocumEvtMetroClusterAggregateLeftBehind": ocumEvtMetroClusterAggregateLeftBehind,
       "ocumEvtClusterUnassignedDisksNone": ocumEvtClusterUnassignedDisksNone,
       "ocumEvtClusterUnassignedDisksSome": ocumEvtClusterUnassignedDisksSome,
       "ocumEvtDisksSparesAvailable": ocumEvtDisksSparesAvailable,
       "ocumEvtDisksNoSpares": ocumEvtDisksNoSpares,
       "ocumEvtDisksNoneFailed": ocumEvtDisksNoneFailed,
       "ocumEvtDisksSomeFailed": ocumEvtDisksSomeFailed,
       "ocumEvtClusterRemoved": ocumEvtClusterRemoved,
       "ocumEvtClusterAddFailed": ocumEvtClusterAddFailed,
       "ocumEvtClusterRenamed": ocumEvtClusterRenamed,
       "ocumEvtClusterReachable": ocumEvtClusterReachable,
       "ocumEvtClusterUnreachable": ocumEvtClusterUnreachable,
       "ocumEvtClusterMonitoringSucceeded": ocumEvtClusterMonitoringSucceeded,
       "ocumEvtClusterMonitoringFailed": ocumEvtClusterMonitoringFailed,
       "ocumEvtClusterUnsupportedDisksNone": ocumEvtClusterUnsupportedDisksNone,
       "ocumEvtClusterUnsupportedDisksSome": ocumEvtClusterUnsupportedDisksSome,
       "ocumEvtClusterNodeAdded": ocumEvtClusterNodeAdded,
       "ocumEvtClusterNodeRemoved": ocumEvtClusterNodeRemoved,
       "ocumEvtClusterNodeRenamed": ocumEvtClusterNodeRenamed,
       "ocumEvtSfoInterconnectUp": ocumEvtSfoInterconnectUp,
       "ocumEvtSfoInterconnectOneOrMoreLinksDown": ocumEvtSfoInterconnectOneOrMoreLinksDown,
       "ocumEvtSfoSettingsEnabled": ocumEvtSfoSettingsEnabled,
       "ocumEvtSfoSettingsNotConfigured": ocumEvtSfoSettingsNotConfigured,
       "ocumEvtSfoSettingsDisabled": ocumEvtSfoSettingsDisabled,
       "ocumEvtSfoStateConnected": ocumEvtSfoStateConnected,
       "ocumEvtSfoStateTakeover": ocumEvtSfoStateTakeover,
       "ocumEvtSfoStatePartialGiveback": ocumEvtSfoStatePartialGiveback,
       "ocumEvtSfoNodeStatusUp": ocumEvtSfoNodeStatusUp,
       "ocumEvtSfoNodeStatusDown": ocumEvtSfoNodeStatusDown,
       "ocumEvtSfoTakeoverPossible": ocumEvtSfoTakeoverPossible,
       "ocumEvtSfoTakeoverNotPossible": ocumEvtSfoTakeoverNotPossible,
       "ocumEvtFansNormal": ocumEvtFansNormal,
       "ocumEvtFansOneOrMoreFailed": ocumEvtFansOneOrMoreFailed,
       "ocumEvtNvramBatteryOk": ocumEvtNvramBatteryOk,
       "ocumEvtNvramBatteryLow": ocumEvtNvramBatteryLow,
       "ocumEvtNvramBatteryOverCharged": ocumEvtNvramBatteryOverCharged,
       "ocumEvtNvramBatteryDischarged": ocumEvtNvramBatteryDischarged,
       "ocumEvtPowerSupplyOk": ocumEvtPowerSupplyOk,
       "ocumEvtPowerSupplyOneOrMoreFailed": ocumEvtPowerSupplyOneOrMoreFailed,
       "ocumEvtClusterNodeRootVolumeSpaceOk": ocumEvtClusterNodeRootVolumeSpaceOk,
       "ocumEvtClusterNodeRootVolumeSpaceNearlyFull": ocumEvtClusterNodeRootVolumeSpaceNearlyFull,
       "ocumEvtPortStatusUp": ocumEvtPortStatusUp,
       "ocumEvtPortStatusDown": ocumEvtPortStatusDown,
       "ocumEvtFlashCardOnline": ocumEvtFlashCardOnline,
       "ocumEvtFlashCardOffline": ocumEvtFlashCardOffline,
       "ocumEvtServiceProcessorOnline": ocumEvtServiceProcessorOnline,
       "ocumEvtServiceProcessorOffline": ocumEvtServiceProcessorOffline,
       "ocumEvtServiceProcessorNotConfigured": ocumEvtServiceProcessorNotConfigured,
       "ocumEvtEfficiencyPolicyEnabled": ocumEvtEfficiencyPolicyEnabled,
       "ocumEvtEfficiencyPolicyDisabled": ocumEvtEfficiencyPolicyDisabled,
       "ocumEvtLifStatusUp": ocumEvtLifStatusUp,
       "ocumEvtLifStatusDown": ocumEvtLifStatusDown,
       "ocumEvtLifMigrated": ocumEvtLifMigrated,
       "ocumEvtLifFailoverPossible": ocumEvtLifFailoverPossible,
       "ocumEvtLifFailoverNotPossible": ocumEvtLifFailoverNotPossible,
       "ocumEvtLifNoRouteConfigured": ocumEvtLifNoRouteConfigured,
       "ocumEvtLifNotAtHomePort": ocumEvtLifNotAtHomePort,
       "ocumEvtLifAtHomePort": ocumEvtLifAtHomePort,
       "ocumEvtLunSnapshotOk": ocumEvtLunSnapshotOk,
       "ocumEvtLunSnapshotNotPossible": ocumEvtLunSnapshotNotPossible,
       "ocumEvtLunSpaceReservationEnabled": ocumEvtLunSpaceReservationEnabled,
       "ocumEvtLunSpaceReservationDisabled": ocumEvtLunSpaceReservationDisabled,
       "ocumEvtLunOnline": ocumEvtLunOnline,
       "ocumEvtLunOffline": ocumEvtLunOffline,
       "ocumEvtLunMultipleActivePath": ocumEvtLunMultipleActivePath,
       "ocumEvtLunSingleActivePath": ocumEvtLunSingleActivePath,
       "ocumEvtLunReachable": ocumEvtLunReachable,
       "ocumEvtLunNotReachable": ocumEvtLunNotReachable,
       "ocumEvtLunOptimizedPathActive": ocumEvtLunOptimizedPathActive,
       "ocumEvtLunOptimizedPathInactive": ocumEvtLunOptimizedPathInactive,
       "ocumEvtAlertCreated": ocumEvtAlertCreated,
       "ocumEvtAlertDeleted": ocumEvtAlertDeleted,
       "ocumEvtAlertModified": ocumEvtAlertModified,
       "ocumEvtQtreeFilesOk": ocumEvtQtreeFilesOk,
       "ocumEvtQtreeFilesSoftLimitBreached": ocumEvtQtreeFilesSoftLimitBreached,
       "ocumEvtQtreeFilesHardLimitReached": ocumEvtQtreeFilesHardLimitReached,
       "ocumEvtQtreeSpaceOk": ocumEvtQtreeSpaceOk,
       "ocumEvtQtreeSpaceSoftLimitBreached": ocumEvtQtreeSpaceSoftLimitBreached,
       "ocumEvtQtreeSpaceHardLimitReached": ocumEvtQtreeSpaceHardLimitReached,
       "ocumEvtQtreeSpaceFull": ocumEvtQtreeSpaceFull,
       "ocumEvtQtreeSpaceNearlyFull": ocumEvtQtreeSpaceNearlyFull,
       "ocumEvtQtreeSpaceThresholdOk": ocumEvtQtreeSpaceThresholdOk,
       "ocumEvtSnapshotPolicyEnabled": ocumEvtSnapshotPolicyEnabled,
       "ocumEvtSnapshotPolicyDisabled": ocumEvtSnapshotPolicyDisabled,
       "ocumEvtSnapshotPolicyCreated": ocumEvtSnapshotPolicyCreated,
       "ocumEvtSnapshotPolicyDeleted": ocumEvtSnapshotPolicyDeleted,
       "ocumEvtSnapshotPolicyScheduleAdded": ocumEvtSnapshotPolicyScheduleAdded,
       "ocumEvtSnapshotPolicyScheduleModified": ocumEvtSnapshotPolicyScheduleModified,
       "ocumEvtSnapshotPolicyScheduleRemoved": ocumEvtSnapshotPolicyScheduleRemoved,
       "ocumEvtStorageServiceCreated": ocumEvtStorageServiceCreated,
       "ocumEvtStorageServiceSubscribed": ocumEvtStorageServiceSubscribed,
       "ocumEvtStorageServiceUnsubscribed": ocumEvtStorageServiceUnsubscribed,
       "ocumEvtStorageServiceUnexpectedRelationshipDeletion": ocumEvtStorageServiceUnexpectedRelationshipDeletion,
       "ocumEvtStorageServiceUnexpectedVolumeDeletion": ocumEvtStorageServiceUnexpectedVolumeDeletion,
       "ocumEvtShelfFanNormal": ocumEvtShelfFanNormal,
       "ocumEvtShelfFanFailed": ocumEvtShelfFanFailed,
       "ocumEvtShelfPowerSupplyNormal": ocumEvtShelfPowerSupplyNormal,
       "ocumEvtShelfPowerSupplyFailed": ocumEvtShelfPowerSupplyFailed,
       "ocumEvtShelfVoltageNormal": ocumEvtShelfVoltageNormal,
       "ocumEvtShelfVoltageAbnormal": ocumEvtShelfVoltageAbnormal,
       "ocumEvtShelfCurrentNormal": ocumEvtShelfCurrentNormal,
       "ocumEvtShelfCurrentAbnormal": ocumEvtShelfCurrentAbnormal,
       "ocumEvtShelfTemperatureNormal": ocumEvtShelfTemperatureNormal,
       "ocumEvtShelfTemperatureAbnormal": ocumEvtShelfTemperatureAbnormal,
       "ocumEvtStorageShelfDiscovered": ocumEvtStorageShelfDiscovered,
       "ocumEvtStorageShelfRemoved": ocumEvtStorageShelfRemoved,
       "ocumEvtProtectionJobTaskFailed": ocumEvtProtectionJobTaskFailed,
       "ocumEvtProtectionJobAborted": ocumEvtProtectionJobAborted,
       "ocumEvtVolumeOnline": ocumEvtVolumeOnline,
       "ocumEvtVolumeRestricted": ocumEvtVolumeRestricted,
       "ocumEvtVolumeOffline": ocumEvtVolumeOffline,
       "ocumEvtVolumeMixed": ocumEvtVolumeMixed,
       "ocumEvtVolumeSpaceOk": ocumEvtVolumeSpaceOk,
       "ocumEvtVolumeNearlyFull": ocumEvtVolumeNearlyFull,
       "ocumEvtVolumeFull": ocumEvtVolumeFull,
       "ocumEvtInodesUtilOk": ocumEvtInodesUtilOk,
       "ocumEvtInodesAlmostFull": ocumEvtInodesAlmostFull,
       "ocumEvtInodesFull": ocumEvtInodesFull,
       "ocumEvtVolumeCloneDiscovered": ocumEvtVolumeCloneDiscovered,
       "ocumEvtVolumeCloneDeleted": ocumEvtVolumeCloneDeleted,
       "ocumEvtVolumeCloneSplit": ocumEvtVolumeCloneSplit,
       "ocumEvtVolumeQtreeQuotaOvercommitOk": ocumEvtVolumeQtreeQuotaOvercommitOk,
       "ocumEvtVolumeQtreeQuotaAlmostOvercommitted": ocumEvtVolumeQtreeQuotaAlmostOvercommitted,
       "ocumEvtVolumeQtreeQuotaOvercommitted": ocumEvtVolumeQtreeQuotaOvercommitted,
       "ocumEvtVolumeInlineCompressionEnabled": ocumEvtVolumeInlineCompressionEnabled,
       "ocumEvtVolumeInlineCompressionDisabled": ocumEvtVolumeInlineCompressionDisabled,
       "ocumEvtVolumeBackgroundCompressionEnabled": ocumEvtVolumeBackgroundCompressionEnabled,
       "ocumEvtVolumeBackgroundCompressionDisabled": ocumEvtVolumeBackgroundCompressionDisabled,
       "ocumEvtVolumeDedupeEnabled": ocumEvtVolumeDedupeEnabled,
       "ocumEvtVolumeDedupeDisabled": ocumEvtVolumeDedupeDisabled,
       "ocumEvtVolumeEfficiencyOperationOk": ocumEvtVolumeEfficiencyOperationOk,
       "ocumEvtVolumeEfficiencyOperationError": ocumEvtVolumeEfficiencyOperationError,
       "ocumEvtVolumeGrowthRateOk": ocumEvtVolumeGrowthRateOk,
       "ocumEvtVolumeGrowthRateAbnormal": ocumEvtVolumeGrowthRateAbnormal,
       "ocumEvtVolumeRenamed": ocumEvtVolumeRenamed,
       "ocumEvtVolumeDiscovered": ocumEvtVolumeDiscovered,
       "ocumEvtVolumeRemoved": ocumEvtVolumeRemoved,
       "ocumEvtVolumeMounted": ocumEvtVolumeMounted,
       "ocumEvtVolumeUnmounted": ocumEvtVolumeUnmounted,
       "ocumEvtVolumeRemounted": ocumEvtVolumeRemounted,
       "ocumEvtVolumeExportPolicyModified": ocumEvtVolumeExportPolicyModified,
       "ocumEvtVolumeDaysUntilFullNotSoon": ocumEvtVolumeDaysUntilFullNotSoon,
       "ocumEvtVolumeDaysUntilFullSoon": ocumEvtVolumeDaysUntilFullSoon,
       "ocumEvtVolumeFractionalReserveModified": ocumEvtVolumeFractionalReserveModified,
       "ocumEvtVolumeSpaceGuaranteeModified": ocumEvtVolumeSpaceGuaranteeModified,
       "ocumEvtVolumeSpaceGuaranteeEnabled": ocumEvtVolumeSpaceGuaranteeEnabled,
       "ocumEvtVolumeSpaceGuaranteeDisabled": ocumEvtVolumeSpaceGuaranteeDisabled,
       "ocumEvtVolumeAutosizeEnabled": ocumEvtVolumeAutosizeEnabled,
       "ocumEvtVolumeAutosizeDisabled": ocumEvtVolumeAutosizeDisabled,
       "ocumEvtVolumeAutosizeModifiedMax": ocumEvtVolumeAutosizeModifiedMax,
       "ocumEvtVolumeAutosizeModifiedIncrement": ocumEvtVolumeAutosizeModifiedIncrement,
       "ocumEvtVolumeMoveFinished": ocumEvtVolumeMoveFinished,
       "ocumEvtVolumeMoveProgress": ocumEvtVolumeMoveProgress,
       "ocumEvtVolumeMoveCompleted": ocumEvtVolumeMoveCompleted,
       "ocumEvtVolumeMoveCutoverDeferred": ocumEvtVolumeMoveCutoverDeferred,
       "ocumEvtVolumeMoveFailed": ocumEvtVolumeMoveFailed,
       "ocumEvtVolumeJunctionPathActive": ocumEvtVolumeJunctionPathActive,
       "ocumEvtVolumeJunctionPathInactive": ocumEvtVolumeJunctionPathInactive,
       "ocumEvtSnapshotSpaceOk": ocumEvtSnapshotSpaceOk,
       "ocumEvtSnapshotFull": ocumEvtSnapshotFull,
       "ocumEvtSnapshotTooMany": ocumEvtSnapshotTooMany,
       "ocumEvtSnapshotNotTooMany": ocumEvtSnapshotNotTooMany,
       "ocumEvtSnapSchedModified": ocumEvtSnapSchedModified,
       "ocumEvtSnapEnabled": ocumEvtSnapEnabled,
       "ocumEvtSnapDisabled": ocumEvtSnapDisabled,
       "ocumEvtSnapshotAutodeleteEnabled": ocumEvtSnapshotAutodeleteEnabled,
       "ocumEvtSnapshotAutodeleteDisabled": ocumEvtSnapshotAutodeleteDisabled,
       "ocumEvtSnapshotAutodeleteModified": ocumEvtSnapshotAutodeleteModified,
       "ocumEvtVolumeSnapshotReserveDaysUntilFullNotSoon": ocumEvtVolumeSnapshotReserveDaysUntilFullNotSoon,
       "ocumEvtVolumeSnapshotReserveDaysUntilFullSoon": ocumEvtVolumeSnapshotReserveDaysUntilFullSoon,
       "ocumEvtVolumeSnapshotReserveModified": ocumEvtVolumeSnapshotReserveModified,
       "ocumEvtVolumeNextSnapshotPossible": ocumEvtVolumeNextSnapshotPossible,
       "ocumEvtVolumeNextSnapshotNotPossible": ocumEvtVolumeNextSnapshotNotPossible,
       "ocumEvtSnapmirrorRelationshipDiscovered": ocumEvtSnapmirrorRelationshipDiscovered,
       "ocumEvtSnapmirrorRelationshipModified": ocumEvtSnapmirrorRelationshipModified,
       "ocumEvtSnapmirrorRelationshipDeleted": ocumEvtSnapmirrorRelationshipDeleted,
       "ocumEvtSnapmirrorRelationshipHealthy": ocumEvtSnapmirrorRelationshipHealthy,
       "ocumEvtSnapmirrorRelationshipUnhealthy": ocumEvtSnapmirrorRelationshipUnhealthy,
       "ocumEvtSnapmirrorRelationshipStateOk": ocumEvtSnapmirrorRelationshipStateOk,
       "ocumEvtSnapmirrorRelationshipStateBrokenoff": ocumEvtSnapmirrorRelationshipStateBrokenoff,
       "ocumEvtSnapmirrorRelationshipInitializeOk": ocumEvtSnapmirrorRelationshipInitializeOk,
       "ocumEvtSnapmirrorRelationshipInitializeFailed": ocumEvtSnapmirrorRelationshipInitializeFailed,
       "ocumEvtSnapmirrorRelationshipUpdateOk": ocumEvtSnapmirrorRelationshipUpdateOk,
       "ocumEvtSnapmirrorRelationshipUpdateFailed": ocumEvtSnapmirrorRelationshipUpdateFailed,
       "ocumEvtSnapmirrorRelationshipResyncOk": ocumEvtSnapmirrorRelationshipResyncOk,
       "ocumEvtSnapmirrorRelationshipResyncFailed": ocumEvtSnapmirrorRelationshipResyncFailed,
       "ocumEvtSnapMirrorRelationshipLagWarning": ocumEvtSnapMirrorRelationshipLagWarning,
       "ocumEvtSnapMirrorRelationshipLagError": ocumEvtSnapMirrorRelationshipLagError,
       "ocumEvtSnapMirrorRelationshipLagNormal": ocumEvtSnapMirrorRelationshipLagNormal,
       "ocumEvtSnapvaultRelationshipHealthy": ocumEvtSnapvaultRelationshipHealthy,
       "ocumEvtSnapvaultRelationshipUnhealthy": ocumEvtSnapvaultRelationshipUnhealthy,
       "ocumEvtSnapvaultRelationshipStateOk": ocumEvtSnapvaultRelationshipStateOk,
       "ocumEvtSnapvaultRelationshipStateBrokenoff": ocumEvtSnapvaultRelationshipStateBrokenoff,
       "ocumEvtSnapvaultRelationshipInitializeOk": ocumEvtSnapvaultRelationshipInitializeOk,
       "ocumEvtSnapvaultRelationshipInitializeFailed": ocumEvtSnapvaultRelationshipInitializeFailed,
       "ocumEvtSnapvaultRelationshipUpdateOk": ocumEvtSnapvaultRelationshipUpdateOk,
       "ocumEvtSnapvaultRelationshipUpdateFailed": ocumEvtSnapvaultRelationshipUpdateFailed,
       "ocumEvtSnapvaultRelationshipResyncOk": ocumEvtSnapvaultRelationshipResyncOk,
       "ocumEvtSnapvaultRelationshipResyncFailed": ocumEvtSnapvaultRelationshipResyncFailed,
       "ocumEvtSnapVaultRelationshipLagWarning": ocumEvtSnapVaultRelationshipLagWarning,
       "ocumEvtSnapVaultRelationshipLagError": ocumEvtSnapVaultRelationshipLagError,
       "ocumEvtSnapVaultRelationshipLagNormal": ocumEvtSnapVaultRelationshipLagNormal,
       "ocumEvtVserverCifsServiceStatusUp": ocumEvtVserverCifsServiceStatusUp,
       "ocumEvtVserverCifsServiceStatusDown": ocumEvtVserverCifsServiceStatusDown,
       "ocumEvtVserverFcServiceStatusUp": ocumEvtVserverFcServiceStatusUp,
       "ocumEvtVserverFcServiceStatusDown": ocumEvtVserverFcServiceStatusDown,
       "ocumEvtVserverIscsiServiceStatusUp": ocumEvtVserverIscsiServiceStatusUp,
       "ocumEvtVserverIscsiServiceStatusDown": ocumEvtVserverIscsiServiceStatusDown,
       "ocumEvtVserverNfsServiceStatusUp": ocumEvtVserverNfsServiceStatusUp,
       "ocumEvtVserverNfsServiceStatusDown": ocumEvtVserverNfsServiceStatusDown,
       "ocumEvtVserverCifsServiceNotConfigured": ocumEvtVserverCifsServiceNotConfigured,
       "ocumEvtVserverFcServiceNotConfigured": ocumEvtVserverFcServiceNotConfigured,
       "ocumEvtVserverIscsiServiceNotConfigured": ocumEvtVserverIscsiServiceNotConfigured,
       "ocumEvtVserverNfsServiceNotConfigured": ocumEvtVserverNfsServiceNotConfigured,
       "ocumEvtVserverRenamed": ocumEvtVserverRenamed,
       "ocumEvtVserverUp": ocumEvtVserverUp,
       "ocumEvtVserverDown": ocumEvtVserverDown,
       "ocumEvtVserverDiscovered": ocumEvtVserverDiscovered,
       "ocumEvtVserverDeleted": ocumEvtVserverDeleted,
       "ocumEvtVserverStorageAvailable": ocumEvtVserverStorageAvailable,
       "ocumEvtVserverStoragePartiallyAvailable": ocumEvtVserverStoragePartiallyAvailable,
       "ocumEvtVserverStorageNotAvailable": ocumEvtVserverStorageNotAvailable,
       "ocumEvtVserverSpaceOk": ocumEvtVserverSpaceOk,
       "ocumEvtVserverNearlyFull": ocumEvtVserverNearlyFull,
       "ocumEvtVserverFull": ocumEvtVserverFull,
       "ocumEvtVserverSnapshotUsageOk": ocumEvtVserverSnapshotUsageOk,
       "ocumEvtVserverSnapshotUsageExceeded": ocumEvtVserverSnapshotUsageExceeded,
       "ocumEvtVserverNsMirrorAvailabilityOk": ocumEvtVserverNsMirrorAvailabilityOk,
       "ocumEvtVserverNsMirrorAvailabilityHavingIssues": ocumEvtVserverNsMirrorAvailabilityHavingIssues,
       "ocumEvtVserverNamespaceSpaceOk": ocumEvtVserverNamespaceSpaceOk,
       "ocumEvtVserverNamespaceNearlyFull": ocumEvtVserverNamespaceNearlyFull,
       "ocumEvtVserverNamespaceFull": ocumEvtVserverNamespaceFull,
       "ocumEvtVserverStorageClassAvailable": ocumEvtVserverStorageClassAvailable,
       "ocumEvtVserverStorageClassPartiallyAvailable": ocumEvtVserverStorageClassPartiallyAvailable,
       "ocumEvtVserverStorageClassNotAvailable": ocumEvtVserverStorageClassNotAvailable,
       "ocumEvtVserverStorageClassSpaceOk": ocumEvtVserverStorageClassSpaceOk,
       "ocumEvtVserverStorageClassNearlyFull": ocumEvtVserverStorageClassNearlyFull,
       "ocumEvtVserverStorageClassFull": ocumEvtVserverStorageClassFull,
       "ocumEvtVserverStorageClassSnapshotUsageOk": ocumEvtVserverStorageClassSnapshotUsageOk,
       "ocumEvtVserverStorageClassSnapshotUsageExceeded": ocumEvtVserverStorageClassSnapshotUsageExceeded,
       "ocumEvtScriptNormal": ocumEvtScriptNormal,
       "ocumEvtScriptInformation": ocumEvtScriptInformation,
       "ocumEvtScriptWarning": ocumEvtScriptWarning,
       "ocumEvtScriptError": ocumEvtScriptError,
       "ocumEvtScriptCritical": ocumEvtScriptCritical,
       "ocumEvtUserOrGroupQuotaFileCountOk": ocumEvtUserOrGroupQuotaFileCountOk,
       "ocumEvtUserOrGroupQuotaFileCountSoftLimitBreached": ocumEvtUserOrGroupQuotaFileCountSoftLimitBreached,
       "ocumEvtUserOrGroupQuotaFileCountHardLimitReached": ocumEvtUserOrGroupQuotaFileCountHardLimitReached,
       "ocumEvtUserOrGroupQuotaDiskSpaceOk": ocumEvtUserOrGroupQuotaDiskSpaceOk,
       "ocumEvtUserOrGroupQuotaDiskSpaceSoftLimitBreached": ocumEvtUserOrGroupQuotaDiskSpaceSoftLimitBreached,
       "ocumEvtUserOrGroupQuotaDiskSpaceHardLimitReached": ocumEvtUserOrGroupQuotaDiskSpaceHardLimitReached,
       "ocumPerformanceIncident": ocumPerformanceIncident,
       "ocumPerformanceIncidentCleared": ocumPerformanceIncidentCleared,
       "ocumPerformanceError": ocumPerformanceError,
       "ocumPerformanceWarning": ocumPerformanceWarning,
       "ocumPerformanceInformation": ocumPerformanceInformation,
       "ocumThinProvisionVolumeSpaceAtRisk": ocumThinProvisionVolumeSpaceAtRisk,
       "ocumThinProvisionVolumeSpaceNotAtRisk": ocumThinProvisionVolumeSpaceNotAtRisk,
       "ocumDiskShelfConnectivityInMultiPath": ocumDiskShelfConnectivityInMultiPath,
       "ocumDiskShelfConnectivityNotInMultiPath": ocumDiskShelfConnectivityNotInMultiPath,
       "ocumDiskShelfConnectivityPathNormal": ocumDiskShelfConnectivityPathNormal,
       "ocumDiskShelfConnectivityPathFailure": ocumDiskShelfConnectivityPathFailure,
       "ocumClusterAddNeeded": ocumClusterAddNeeded,
       "ocumClusterAdded": ocumClusterAdded,
       "ocumEvtMccNodeSwitchFcviLinksUp": ocumEvtMccNodeSwitchFcviLinksUp,
       "ocumEvtMccNodeSwitchFcviLinksOneOrMoreDown": ocumEvtMccNodeSwitchFcviLinksOneOrMoreDown,
       "ocumEvtMccNodeSwitchFcviLinksDown": ocumEvtMccNodeSwitchFcviLinksDown,
       "ocumEvtMccNodeSwitchFcLinksUp": ocumEvtMccNodeSwitchFcLinksUp,
       "ocumEvtMccNodeSwitchFcLinksOneOrMoreDown": ocumEvtMccNodeSwitchFcLinksOneOrMoreDown,
       "ocumEvtMccNodeSwitchFcLinksDown": ocumEvtMccNodeSwitchFcLinksDown,
       "ocumEvtMccSwitchBridgeFcLinksUp": ocumEvtMccSwitchBridgeFcLinksUp,
       "ocumEvtMccSwitchBridgeFcLinksDown": ocumEvtMccSwitchBridgeFcLinksDown,
       "ocumEvtSwitchTemperatureNormal": ocumEvtSwitchTemperatureNormal,
       "ocumEvtSwitchTemperatureAbnormal": ocumEvtSwitchTemperatureAbnormal,
       "ocumEvtSwitchFansNormal": ocumEvtSwitchFansNormal,
       "ocumEvtSwitchFansOneOrMoreFailed": ocumEvtSwitchFansOneOrMoreFailed,
       "ocumEvtSwitchPowerSuppliesNormal": ocumEvtSwitchPowerSuppliesNormal,
       "ocumEvtSwitchPowerSuppliesOneOrMoreFailed": ocumEvtSwitchPowerSuppliesOneOrMoreFailed,
       "ocumEvtSwitchReachable": ocumEvtSwitchReachable,
       "ocumEvtSwitchUnreachable": ocumEvtSwitchUnreachable,
       "ocumEvtSwitchTemperatureSensorNormal": ocumEvtSwitchTemperatureSensorNormal,
       "ocumEvtSwitchTemperatureSensorFailed": ocumEvtSwitchTemperatureSensorFailed,
       "ocumEvtBridgeTemperatureNormal": ocumEvtBridgeTemperatureNormal,
       "ocumEvtBridgeTemperatureAbnormal": ocumEvtBridgeTemperatureAbnormal,
       "ocumEvtBridgeReachable": ocumEvtBridgeReachable,
       "ocumEvtBridgeUnreachable": ocumEvtBridgeUnreachable,
       "ocumEvtMetroClusterAllLinksBetweenPartnersUp": ocumEvtMetroClusterAllLinksBetweenPartnersUp,
       "ocumEvtMetroClusterAllLinksBetweenPartnersDown": ocumEvtMetroClusterAllLinksBetweenPartnersDown,
       "ocumEvtMetroClusterPartnersReachableOverPeeringNetwork": ocumEvtMetroClusterPartnersReachableOverPeeringNetwork,
       "ocumEvtMetroClusterPartnersNotReachableOverPeeringNetwork": ocumEvtMetroClusterPartnersNotReachableOverPeeringNetwork,
       "ocumEvtMetroClusterAllISLBetweenSwitchesUp": ocumEvtMetroClusterAllISLBetweenSwitchesUp,
       "ocumEvtMetroClusterAllISLBetweenSwitchesDown": ocumEvtMetroClusterAllISLBetweenSwitchesDown,
       "ocumEvtMetroClusterDRStatusOk": ocumEvtMetroClusterDRStatusOk,
       "ocumEvtMetroClusterDRStatusPartiallyImpacted": ocumEvtMetroClusterDRStatusPartiallyImpacted,
       "ocumEvtMetroClusterDRStatusImpacted": ocumEvtMetroClusterDRStatusImpacted,
       "ocumEvtMetroClusterDRStatusCompleted": ocumEvtMetroClusterDRStatusCompleted,
       "ocumEvtMetroClusterAggregateMirrorNormal": ocumEvtMetroClusterAggregateMirrorNormal,
       "ocumEvtMetroClusterAggregateMirrorDegraded": ocumEvtMetroClusterAggregateMirrorDegraded,
       "ocumEvtNoSpareDiskLeftBehind": ocumEvtNoSpareDiskLeftBehind,
       "ocumEvtSpareDiskLeftBehind": ocumEvtSpareDiskLeftBehind,
       "ocumEvtMccBridgeStorageStackSASLinksUp": ocumEvtMccBridgeStorageStackSASLinksUp,
       "ocumEvtMccBridgeStorageStackSASLinksDown": ocumEvtMccBridgeStorageStackSASLinksDown,
       "ocumEvtClusterFlashDiskFewerSpareBlockNormal": ocumEvtClusterFlashDiskFewerSpareBlockNormal,
       "ocumEvtClusterFlashDiskFewerSpareBlockError": ocumEvtClusterFlashDiskFewerSpareBlockError,
       "ocumEvtClusterFlashDiskNoSpareBlockNormal": ocumEvtClusterFlashDiskNoSpareBlockNormal,
       "ocumEvtClusterFlashDiskNoSpareBlockCritical": ocumEvtClusterFlashDiskNoSpareBlockCritical,
       "ocumEvtBackupCreationSucceeded": ocumEvtBackupCreationSucceeded,
       "ocumEvtBackupCreationFailed": ocumEvtBackupCreationFailed,
       "ocumEvtBackupCreationNormal": ocumEvtBackupCreationNormal,
       "ocumEvtMccInterNodeLinksUp": ocumEvtMccInterNodeLinksUp,
       "ocumEvtMccInterNodeLinksOneOrMoreDown": ocumEvtMccInterNodeLinksOneOrMoreDown,
       "ocumEvtMccInterNodeLinksDown": ocumEvtMccInterNodeLinksDown,
       "ocumEvtMccNodeBridgeLinksUp": ocumEvtMccNodeBridgeLinksUp,
       "ocumEvtMccNodeBridgeLinksDown": ocumEvtMccNodeBridgeLinksDown,
       "ocumEvtMccNodeStackLinksUp": ocumEvtMccNodeStackLinksUp,
       "ocumEvtMccNodeStackLinksOneOrMoreDown": ocumEvtMccNodeStackLinksOneOrMoreDown,
       "ocumEvtMccNodeStackLinksDown": ocumEvtMccNodeStackLinksDown,
       "ocumEvtMccAutomaticUnplannedSwitchOverDisabled": ocumEvtMccAutomaticUnplannedSwitchOverDisabled,
       "ocumEvtMccAutomaticUnplannedSwitchOverEnabled": ocumEvtMccAutomaticUnplannedSwitchOverEnabled,
       "ocumEvtEMSWarningEventReceived": ocumEvtEMSWarningEventReceived,
       "ocumEvtEMSCriticalEventReceived": ocumEvtEMSCriticalEventReceived,
       "ocumEvtEMSErrorEventReceived": ocumEvtEMSErrorEventReceived,
       "ocumEvtEMSInformationalEventReceived": ocumEvtEMSInformationalEventReceived,
       "ocumEvtEMSNoticeEventReceived": ocumEvtEMSNoticeEventReceived,
       "ocumEvtEMSDebugEventReceived": ocumEvtEMSDebugEventReceived,
       "ocumEvtEMSEmergencyEventReceived": ocumEvtEMSEmergencyEventReceived,
       "ocumEvtEMSAlertEventReceived": ocumEvtEMSAlertEventReceived,
       "ocumEvtHeartbeatServiceStatusDown": ocumEvtHeartbeatServiceStatusDown,
       "ocumEvtHeartbeatServiceStatusUp": ocumEvtHeartbeatServiceStatusUp,
       "ocumEvtUnifiedManagerDiskSpaceNearlyFull": ocumEvtUnifiedManagerDiskSpaceNearlyFull,
       "ocumEvtUnifiedManagerDiskSpaceFull": ocumEvtUnifiedManagerDiskSpaceFull,
       "ocumEvtUnifiedManagerDiskSpaceNormal": ocumEvtUnifiedManagerDiskSpaceNormal,
       "ocumEvtUnifiedManagerDataNormal": ocumEvtUnifiedManagerDataNormal,
       "ocumEvtUnifiedManagerDataMissingAnalyze": ocumEvtUnifiedManagerDataMissingAnalyze,
       "ocumEvtUnifiedManagerDataMissingCollection": ocumEvtUnifiedManagerDataMissingCollection,
       "ocumAggregateLatencyIncident": ocumAggregateLatencyIncident,
       "ocumAggregateLatencyWarning": ocumAggregateLatencyWarning,
       "ocumAggregateLatencyCleared": ocumAggregateLatencyCleared,
       "ocumAggregateIopsIncident": ocumAggregateIopsIncident,
       "ocumAggregateIopsWarning": ocumAggregateIopsWarning,
       "ocumAggregateIopsCleared": ocumAggregateIopsCleared,
       "ocumAggregateMbpsIncident": ocumAggregateMbpsIncident,
       "ocumAggregateMbpsWarning": ocumAggregateMbpsWarning,
       "ocumAggregateMbpsCleared": ocumAggregateMbpsCleared,
       "ocumAggregatePerfCapacityUsedIncident": ocumAggregatePerfCapacityUsedIncident,
       "ocumAggregatePerfCapacityUsedWarning": ocumAggregatePerfCapacityUsedWarning,
       "ocumAggregatePerfCapacityUsedCleared": ocumAggregatePerfCapacityUsedCleared,
       "ocumAggregateUtilizationIncident": ocumAggregateUtilizationIncident,
       "ocumAggregateUtilizationWarning": ocumAggregateUtilizationWarning,
       "ocumAggregateUtilizationCleared": ocumAggregateUtilizationCleared,
       "ocumNodeLatencyIncident": ocumNodeLatencyIncident,
       "ocumNodeLatencyWarning": ocumNodeLatencyWarning,
       "ocumNodeLatencyCleared": ocumNodeLatencyCleared,
       "ocumNodeIopsIncident": ocumNodeIopsIncident,
       "ocumNodeIopsWarning": ocumNodeIopsWarning,
       "ocumNodeIopsCleared": ocumNodeIopsCleared,
       "ocumNodeMbpsIncident": ocumNodeMbpsIncident,
       "ocumNodeMbpsWarning": ocumNodeMbpsWarning,
       "ocumNodeMbpsCleared": ocumNodeMbpsCleared,
       "ocumNodePerfCapacityUsedIncident": ocumNodePerfCapacityUsedIncident,
       "ocumNodePerfCapacityUsedWarning": ocumNodePerfCapacityUsedWarning,
       "ocumNodePerfCapacityUsedCleared": ocumNodePerfCapacityUsedCleared,
       "ocumNodePerfCapacityUsedTakeoverIncident": ocumNodePerfCapacityUsedTakeoverIncident,
       "ocumNodePerfCapacityUsedTakeoverWarning": ocumNodePerfCapacityUsedTakeoverWarning,
       "ocumNodePerfCapacityUsedTakeoverCleared": ocumNodePerfCapacityUsedTakeoverCleared,
       "ocumNodeUtilizationIncident": ocumNodeUtilizationIncident,
       "ocumNodeUtilizationWarning": ocumNodeUtilizationWarning,
       "ocumNodeUtilizationCleared": ocumNodeUtilizationCleared,
       "ocumClusterIopsIncident": ocumClusterIopsIncident,
       "ocumClusterIopsWarning": ocumClusterIopsWarning,
       "ocumClusterIopsCleared": ocumClusterIopsCleared,
       "ocumClusterMbpsIncident": ocumClusterMbpsIncident,
       "ocumClusterMbpsWarning": ocumClusterMbpsWarning,
       "ocumClusterMbpsCleared": ocumClusterMbpsCleared,
       "ocumNetworkPortUtilizationIncident": ocumNetworkPortUtilizationIncident,
       "ocumNetworkPortUtilizationWarning": ocumNetworkPortUtilizationWarning,
       "ocumNetworkPortUtilizationCleared": ocumNetworkPortUtilizationCleared,
       "ocumNetworkPortMbpsIncident": ocumNetworkPortMbpsIncident,
       "ocumNetworkPortMbpsWarning": ocumNetworkPortMbpsWarning,
       "ocumNetworkPortMbpsCleared": ocumNetworkPortMbpsCleared,
       "ocumSvmLatencyIncident": ocumSvmLatencyIncident,
       "ocumSvmLatencyWarning": ocumSvmLatencyWarning,
       "ocumSvmLatencyCleared": ocumSvmLatencyCleared,
       "ocumSvmIopsIncident": ocumSvmIopsIncident,
       "ocumSvmIopsWarning": ocumSvmIopsWarning,
       "ocumSvmIopsCleared": ocumSvmIopsCleared,
       "ocumSvmMbpsIncident": ocumSvmMbpsIncident,
       "ocumSvmMbpsWarning": ocumSvmMbpsWarning,
       "ocumSvmMbpsCleared": ocumSvmMbpsCleared,
       "ocumVolumeLatencyIncident": ocumVolumeLatencyIncident,
       "ocumVolumeLatencyWarning": ocumVolumeLatencyWarning,
       "ocumVolumeLatencyCleared": ocumVolumeLatencyCleared,
       "ocumVolumeIopsIncident": ocumVolumeIopsIncident,
       "ocumVolumeIopsWarning": ocumVolumeIopsWarning,
       "ocumVolumeIopsCleared": ocumVolumeIopsCleared,
       "ocumVolumeMbpsIncident": ocumVolumeMbpsIncident,
       "ocumVolumeMbpsWarning": ocumVolumeMbpsWarning,
       "ocumVolumeMbpsCleared": ocumVolumeMbpsCleared,
       "ocumVolumeCacheMissRatioIncident": ocumVolumeCacheMissRatioIncident,
       "ocumVolumeCacheMissRatioWarning": ocumVolumeCacheMissRatioWarning,
       "ocumVolumeCacheMissRatioCleared": ocumVolumeCacheMissRatioCleared,
       "ocumVolumeLatencyIopsIncident": ocumVolumeLatencyIopsIncident,
       "ocumVolumeLatencyIopsWarning": ocumVolumeLatencyIopsWarning,
       "ocumVolumeLatencyIopsCleared": ocumVolumeLatencyIopsCleared,
       "ocumVolumeLatencyMbpsIncident": ocumVolumeLatencyMbpsIncident,
       "ocumVolumeLatencyMbpsWarning": ocumVolumeLatencyMbpsWarning,
       "ocumVolumeLatencyMbpsCleared": ocumVolumeLatencyMbpsCleared,
       "ocumVolumeLatencyAggregatePerfCapacityUsedIncident": ocumVolumeLatencyAggregatePerfCapacityUsedIncident,
       "ocumVolumeLatencyAggregatePerfCapacityUsedWarning": ocumVolumeLatencyAggregatePerfCapacityUsedWarning,
       "ocumVolumeLatencyAggregatePerfCapacityUsedCleared": ocumVolumeLatencyAggregatePerfCapacityUsedCleared,
       "ocumVolumeLatencyAggregateUtilizationIncident": ocumVolumeLatencyAggregateUtilizationIncident,
       "ocumVolumeLatencyAggregateUtilizationWarning": ocumVolumeLatencyAggregateUtilizationWarning,
       "ocumVolumeLatencyAggregateUtilizationCleared": ocumVolumeLatencyAggregateUtilizationCleared,
       "ocumVolumeLatencyNodePerfCapacityUsedIncident": ocumVolumeLatencyNodePerfCapacityUsedIncident,
       "ocumVolumeLatencyNodePerfCapacityUsedWarning": ocumVolumeLatencyNodePerfCapacityUsedWarning,
       "ocumVolumeLatencyNodePerfCapacityUsedCleared": ocumVolumeLatencyNodePerfCapacityUsedCleared,
       "ocumVolumeLatencyAggregatePerfCapacityUsedTakeoverIncident": ocumVolumeLatencyAggregatePerfCapacityUsedTakeoverIncident,
       "ocumVolumeLatencyAggregatePerfCapacityUsedTakeoverWarning": ocumVolumeLatencyAggregatePerfCapacityUsedTakeoverWarning,
       "ocumVolumeLatencyAggregatePerfCapacityUsedTakeoverCleared": ocumVolumeLatencyAggregatePerfCapacityUsedTakeoverCleared,
       "ocumVolumeLatencyNodeUtilizationIncident": ocumVolumeLatencyNodeUtilizationIncident,
       "ocumVolumeLatencyNodeUtilizationWarning": ocumVolumeLatencyNodeUtilizationWarning,
       "ocumVolumeLatencyNodeUtilizationCleared": ocumVolumeLatencyNodeUtilizationCleared,
       "ocumLunLatencyIncident": ocumLunLatencyIncident,
       "ocumLunLatencyWarning": ocumLunLatencyWarning,
       "ocumLunLatencyCleared": ocumLunLatencyCleared,
       "ocumLunIopsIncident": ocumLunIopsIncident,
       "ocumLunIopsWarning": ocumLunIopsWarning,
       "ocumLunIopsCleared": ocumLunIopsCleared,
       "ocumLunMbpsIncident": ocumLunMbpsIncident,
       "ocumLunMbpsWarning": ocumLunMbpsWarning,
       "ocumLunMbpsCleared": ocumLunMbpsCleared,
       "ocumLunLatencyIopsIncident": ocumLunLatencyIopsIncident,
       "ocumLunLatencyIopsWarning": ocumLunLatencyIopsWarning,
       "ocumLunLatencyIopsCleared": ocumLunLatencyIopsCleared,
       "ocumLunLatencyMbpsIncident": ocumLunLatencyMbpsIncident,
       "ocumLunLatencyMbpsWarning": ocumLunLatencyMbpsWarning,
       "ocumLunLatencyMbpsCleared": ocumLunLatencyMbpsCleared,
       "ocumLunLatencyAggregatePerfCapacityUsedIncident": ocumLunLatencyAggregatePerfCapacityUsedIncident,
       "ocumLunLatencyAggregatePerfCapacityUsedWarning": ocumLunLatencyAggregatePerfCapacityUsedWarning,
       "ocumLunLatencyAggregatePerfCapacityUsedCleared": ocumLunLatencyAggregatePerfCapacityUsedCleared,
       "ocumLunLatencyAggregateUtilizationIncident": ocumLunLatencyAggregateUtilizationIncident,
       "ocumLunLatencyAggregateUtilizationWarning": ocumLunLatencyAggregateUtilizationWarning,
       "ocumLunLatencyAggregateUtilizationCleared": ocumLunLatencyAggregateUtilizationCleared,
       "ocumLunLatencyNodePerfCapacityUsedIncident": ocumLunLatencyNodePerfCapacityUsedIncident,
       "ocumLunLatencyNodePerfCapacityUsedWarning": ocumLunLatencyNodePerfCapacityUsedWarning,
       "ocumLunLatencyNodePerfCapacityUsedCleared": ocumLunLatencyNodePerfCapacityUsedCleared,
       "ocumLunLatencyAggregatePerfCapacityUsedTakeoverIncident": ocumLunLatencyAggregatePerfCapacityUsedTakeoverIncident,
       "ocumLunLatencyAggregatePerfCapacityUsedTakeoverWarning": ocumLunLatencyAggregatePerfCapacityUsedTakeoverWarning,
       "ocumLunLatencyAggregatePerfCapacityUsedTakeoverCleared": ocumLunLatencyAggregatePerfCapacityUsedTakeoverCleared,
       "ocumLunLatencyNodeUtilizationIncident": ocumLunLatencyNodeUtilizationIncident,
       "ocumLunLatencyNodeUtilizationWarning": ocumLunLatencyNodeUtilizationWarning,
       "ocumLunLatencyNodeUtilizationCleared": ocumLunLatencyNodeUtilizationCleared,
       "ocumNetworkLifMbpsIncident": ocumNetworkLifMbpsIncident,
       "ocumNetworkLifMbpsWarning": ocumNetworkLifMbpsWarning,
       "ocumNetworkLifMbpsCleared": ocumNetworkLifMbpsCleared,
       "ocumFcpPortUtilizationIncident": ocumFcpPortUtilizationIncident,
       "ocumFcpPortUtilizationWarning": ocumFcpPortUtilizationWarning,
       "ocumFcpPortUtilizationCleared": ocumFcpPortUtilizationCleared,
       "ocumFcpPortMbpsIncident": ocumFcpPortMbpsIncident,
       "ocumFcpPortMbpsWarning": ocumFcpPortMbpsWarning,
       "ocumFcpPortMbpsCleared": ocumFcpPortMbpsCleared,
       "ocumAggregateDisksOverUtilizedWarning": ocumAggregateDisksOverUtilizedWarning,
       "ocumAggregateDisksOverUtilizedCleared": ocumAggregateDisksOverUtilizedCleared,
       "ocumNodeHaPairOverUtilizedInformation": ocumNodeHaPairOverUtilizedInformation,
       "ocumNodeHaPairOverUtilizedCleared": ocumNodeHaPairOverUtilizedCleared,
       "ocumNodeDiskFragmentationWarning": ocumNodeDiskFragmentationWarning,
       "ocumNodeDiskFragmentationCleared": ocumNodeDiskFragmentationCleared,
       "ocumNodeOverUtilizedWarning": ocumNodeOverUtilizedWarning,
       "ocumNodeOverUtilizedCleared": ocumNodeOverUtilizedCleared,
       "ocumClusterDynamicEventWarning": ocumClusterDynamicEventWarning,
       "ocumClusterDynamicEventCleared": ocumClusterDynamicEventCleared,
       "ocumNodeDynamicEventWarning": ocumNodeDynamicEventWarning,
       "ocumNodeDynamicEventCleared": ocumNodeDynamicEventCleared,
       "ocumAggregateDynamicEventWarning": ocumAggregateDynamicEventWarning,
       "ocumAggregateDynamicEventCleared": ocumAggregateDynamicEventCleared,
       "ocumFcpLifMbpsIncident": ocumFcpLifMbpsIncident,
       "ocumFcpLifMbpsWarning": ocumFcpLifMbpsWarning,
       "ocumFcpLifMbpsCleared": ocumFcpLifMbpsCleared,
       "ocumEvtClusterFabricpoolLicenseCapacityLimitExceeded": ocumEvtClusterFabricpoolLicenseCapacityLimitExceeded,
       "ocumEvtClusterFabricpoolLicenseCapacityLimitNormal": ocumEvtClusterFabricpoolLicenseCapacityLimitNormal,
       "ocumEventExternalCapacityUnreachable": ocumEventExternalCapacityUnreachable,
       "ocumEventExternalCapacityReachable": ocumEventExternalCapacityReachable,
       "ocumEventExternalCapacityPartiallyReachable": ocumEventExternalCapacityPartiallyReachable,
       "ocumQosVolumeMaxIopsWarning": ocumQosVolumeMaxIopsWarning,
       "ocumQosVolumeMaxIopsCleared": ocumQosVolumeMaxIopsCleared,
       "ocumQosVolumeMaxMbpsWarning": ocumQosVolumeMaxMbpsWarning,
       "ocumQosVolumeMaxMbpsCleared": ocumQosVolumeMaxMbpsCleared,
       "ocumQosLunMaxIopsWarning": ocumQosLunMaxIopsWarning,
       "ocumQosLunMaxIopsCleared": ocumQosLunMaxIopsCleared,
       "ocumQosLunMaxMbpsWarning": ocumQosLunMaxMbpsWarning,
       "ocumQosLunMaxMbpsCleared": ocumQosLunMaxMbpsCleared,
       "ocumQosVolumeMaxIopsPerTbWarning": ocumQosVolumeMaxIopsPerTbWarning,
       "ocumQosVolumeMaxIopsPerTbCleared": ocumQosVolumeMaxIopsPerTbCleared,
       "ocumQosLunMaxIopsPerTbWarning": ocumQosLunMaxIopsPerTbWarning,
       "ocumQosLunMaxIopsPerTbCleared": ocumQosLunMaxIopsPerTbCleared,
       "ocumArlNetraCaCheckFailed": ocumArlNetraCaCheckFailed,
       "ocumGbNetraCaCheckFailed": ocumGbNetraCaCheckFailed,
       "ocumObjstoreHostUnresolvable": ocumObjstoreHostUnresolvable,
       "ocumObjstoreInterClusterLifDown": ocumObjstoreInterClusterLifDown,
       "ocumWaflCaLatencyThreashold": ocumWaflCaLatencyThreashold,
       "ocumS3BucketSignatureMismatch": ocumS3BucketSignatureMismatch,
       "ocumCloudAwsMetadataConnFail": ocumCloudAwsMetadataConnFail,
       "ocumCloudAwsIamCredsExpired": ocumCloudAwsIamCredsExpired,
       "ocumCloudAwsIamCredsInvalid": ocumCloudAwsIamCredsInvalid,
       "ocumCloudAwsIamCredsNotFound": ocumCloudAwsIamCredsNotFound,
       "ocumCloudAwsIamCredsNotInitialized": ocumCloudAwsIamCredsNotInitialized,
       "ocumCloudAwsIamRoleInvalid": ocumCloudAwsIamRoleInvalid,
       "ocumCloudAwsIamRoleNotFound": ocumCloudAwsIamRoleNotFound,
       "ocumQosMonitorMemoryMaxed": ocumQosMonitorMemoryMaxed,
       "ocumQosMonitorMemoryAbated": ocumQosMonitorMemoryAbated,
       "ocumQosViolationReport": ocumQosViolationReport,
       "ocumEvtUnifiedManagerMemoryLow": ocumEvtUnifiedManagerMemoryLow,
       "ocumEvtUnifiedManagerMemoryAlmostOut": ocumEvtUnifiedManagerMemoryAlmostOut,
       "ocumEvtUnifiedManagerMemoryNormal": ocumEvtUnifiedManagerMemoryNormal,
       "nvmeNamespaceStatusOnline": nvmeNamespaceStatusOnline,
       "nvmeNamespaceStatusOffline": nvmeNamespaceStatusOffline,
       "nvmeNamespaceSpaceOutOfSpace": nvmeNamespaceSpaceOutOfSpace,
       "nvmeNamespaceDestroy": nvmeNamespaceDestroy,
       "flexGroupConstituentsHaveSpaceIssues": flexGroupConstituentsHaveSpaceIssues,
       "flexGroupConstituentsSpaceStatusAllOK": flexGroupConstituentsSpaceStatusAllOK,
       "flexGroupConstituentsHaveInodesIssues": flexGroupConstituentsHaveInodesIssues,
       "flexGroupConstituentsInodesStatusAllOK": flexGroupConstituentsInodesStatusAllOK,
       "ocumNvmeNamespaceLatencyIncident": ocumNvmeNamespaceLatencyIncident,
       "ocumNvmeNamespaceLatencyWarning": ocumNvmeNamespaceLatencyWarning,
       "ocumNvmeNamespaceLatencyCleared": ocumNvmeNamespaceLatencyCleared,
       "ocumNvmeNamespaceIopsIncident": ocumNvmeNamespaceIopsIncident,
       "ocumNvmeNamespaceIopsWarning": ocumNvmeNamespaceIopsWarning,
       "ocumNvmeNamespaceIopsCleared": ocumNvmeNamespaceIopsCleared,
       "ocumNvmeNamespaceMbpsIncident": ocumNvmeNamespaceMbpsIncident,
       "ocumNvmeNamespaceMbpsWarning": ocumNvmeNamespaceMbpsWarning,
       "ocumNvmeNamespaceMbpsCleared": ocumNvmeNamespaceMbpsCleared,
       "ocumNvmeNamespaceLatencyIopsIncident": ocumNvmeNamespaceLatencyIopsIncident,
       "ocumNvmeNamespaceLatencyIopsWarning": ocumNvmeNamespaceLatencyIopsWarning,
       "ocumNvmeNamespaceLatencyIopsCleared": ocumNvmeNamespaceLatencyIopsCleared,
       "ocumNvmeNamespaceLatencyMbpsIncident": ocumNvmeNamespaceLatencyMbpsIncident,
       "ocumNvmeNamespaceLatencyMbpsWarning": ocumNvmeNamespaceLatencyMbpsWarning,
       "ocumNvmeNamespaceLatencyMbpsCleared": ocumNvmeNamespaceLatencyMbpsCleared,
       "ocumNvmfFcLifMbpsIncident": ocumNvmfFcLifMbpsIncident,
       "ocumNvmfFcLifMbpsWarning": ocumNvmfFcLifMbpsWarning,
       "ocumNvmfFcLifMbpsCleared": ocumNvmfFcLifMbpsCleared,
       "objectMaintenanceWindowStarted": objectMaintenanceWindowStarted,
       "objectMaintenanceWindowEnded": objectMaintenanceWindowEnded,
       "ocumDynamicEventWarning": ocumDynamicEventWarning,
       "ocumDynamicEventCleared": ocumDynamicEventCleared,
       "syncSnapmirrorRelationshipOutofsync": syncSnapmirrorRelationshipOutofsync,
       "syncSnapmirrorRelationshipInSync": syncSnapmirrorRelationshipInSync,
       "syncSnapmirrorRelationshipAutoSyncRetryFailed": syncSnapmirrorRelationshipAutoSyncRetryFailed,
       "volumeLogicalSpaceNearlyFull": volumeLogicalSpaceNearlyFull,
       "volumeLogicalSpaceFull": volumeLogicalSpaceFull,
       "volumeLogicalSpaceAllOK": volumeLogicalSpaceAllOK,
       "ocumQosVolumeMaxIopsBlocksizePerTbWarning": ocumQosVolumeMaxIopsBlocksizePerTbWarning,
       "ocumQosVolumeMaxIopsBlocksizePerTbCleared": ocumQosVolumeMaxIopsBlocksizePerTbCleared,
       "clusterCapacityTierPlanningWarning": clusterCapacityTierPlanningWarning,
       "clusterCapacityTierPlanningCleared": clusterCapacityTierPlanningCleared,
       "waflVolAutoSizeFail": waflVolAutoSizeFail,
       "waflVolAutoSizeDone": waflVolAutoSizeDone,
       "lunDestroy": lunDestroy,
       "nbladeCifsManyAuths": nbladeCifsManyAuths,
       "nbladeCifsMaxOpenSameFile": nbladeCifsMaxOpenSameFile,
       "nbladeCifsMaxSessPerUsrConn": nbladeCifsMaxSessPerUsrConn,
       "nbladeCifsNbNameConflict": nbladeCifsNbNameConflict,
       "nbladeCifsNoPrivShare": nbladeCifsNoPrivShare,
       "nbladeVscanVirusDetected": nbladeVscanVirusDetected,
       "nbladeVscanNoScannerConn": nbladeVscanNoScannerConn,
       "nbladeVscanNoRegdScanner": nbladeVscanNoRegdScanner,
       "nbladeVscanConnInactive": nbladeVscanConnInactive,
       "nbladeVscanConnBackPressure": nbladeVscanConnBackPressure,
       "nbladeVscanBadUserPrivAccess": nbladeVscanBadUserPrivAccess,
       "nbladeNfsv4PoolEXhaust": nbladeNfsv4PoolEXhaust,
       "cifsShadowCopyFailure": cifsShadowCopyFailure,
       "clusterFabricPoolNearlyFull": clusterFabricPoolNearlyFull,
       "oscSignatureMismatch": oscSignatureMismatch,
       "arlNetraCaCheckFailed": arlNetraCaCheckFailed,
       "gbNetraCaCheckFailed": gbNetraCaCheckFailed,
       "nvmfGracePeriodStart": nvmfGracePeriodStart,
       "nvmfGracePeriodActive": nvmfGracePeriodActive,
       "nvmfGracePeriodExpired": nvmfGracePeriodExpired,
       "ocumEvtLunHaPartnerPathActive": ocumEvtLunHaPartnerPathActive,
       "ocumEvtLunHaPartnerPathInActive": ocumEvtLunHaPartnerPathInActive,
       "ocumSystemId": ocumSystemId,
       "ocumEvent": ocumEvent,
       "ocumEventName": ocumEventName,
       "ocumEventSeverity": ocumEventSeverity,
       "ocumEventImpactLevel": ocumEventImpactLevel,
       "ocumEventTimestamp": ocumEventTimestamp,
       "ocumEventMessage": ocumEventMessage,
       "ocumEventMessageDetails": ocumEventMessageDetails,
       "ocumEventSourceResourceKey": ocumEventSourceResourceKey,
       "ocumEventSourceFullName": ocumEventSourceFullName,
       "ocumEventSourceType": ocumEventSourceType,
       "ocumEventSourceHealthStatus": ocumEventSourceHealthStatus,
       "ocumEventSourceScopedResourceKey": ocumEventSourceScopedResourceKey,
       "ocumEventSourceScopedFullName": ocumEventSourceScopedFullName,
       "ocumEventSourceClusterResourceKey": ocumEventSourceClusterResourceKey,
       "ocumEventSourceClusterFullName": ocumEventSourceClusterFullName,
       "ocumEventState": ocumEventState,
       "ocumTestAlert": ocumTestAlert,
       "ocumTestAlertTimestamp": ocumTestAlertTimestamp}
)
