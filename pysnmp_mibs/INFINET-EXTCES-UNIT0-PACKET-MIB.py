# SNMP MIB module (INFINET-EXTCES-UNIT0-PACKET-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinet/INFINET-EXTCES-UNIT0-PACKET-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:06:04 2025
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

(cesOverWlanUnit0,) = mibBuilder.importSymbols(
    "INFINET-EXTCES-MIB",
    "cesOverWlanUnit0")

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
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TimeStamp")


# MODULE-IDENTITY

cesOverWlanUnit0Packet = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3942, 2, 1, 1, 3)
)
if mibBuilder.loadTexts:
    cesOverWlanUnit0Packet.setRevisions(
        ("2004-08-16 19:10",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CesOverWlanUnit0PacketTable_Object = MibTable
cesOverWlanUnit0PacketTable = _CesOverWlanUnit0PacketTable_Object(
    (1, 3, 6, 1, 4, 1, 3942, 2, 1, 1, 3, 1)
)
if mibBuilder.loadTexts:
    cesOverWlanUnit0PacketTable.setStatus("current")
_CesOverWlanUnit0PacketEntry_Object = MibTableRow
cesOverWlanUnit0PacketEntry = _CesOverWlanUnit0PacketEntry_Object(
    (1, 3, 6, 1, 4, 1, 3942, 2, 1, 1, 3, 1, 1)
)
cesOverWlanUnit0PacketEntry.setIndexNames(
    (0, "INFINET-EXTCES-UNIT0-PACKET-MIB", "cesOverWlanUnit0PacketPortNumber"),
)
if mibBuilder.loadTexts:
    cesOverWlanUnit0PacketEntry.setStatus("current")
_CesOverWlanUnit0PacketPortNumber_Type = Unsigned32
_CesOverWlanUnit0PacketPortNumber_Object = MibTableColumn
cesOverWlanUnit0PacketPortNumber = _CesOverWlanUnit0PacketPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 3942, 2, 1, 1, 3, 1, 1, 1),
    _CesOverWlanUnit0PacketPortNumber_Type()
)
cesOverWlanUnit0PacketPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cesOverWlanUnit0PacketPortNumber.setStatus("current")


class _CesOverWlanUnit0PacketTxState_Type(Integer32):
    """Custom type cesOverWlanUnit0PacketTxState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_CesOverWlanUnit0PacketTxState_Type.__name__ = "Integer32"
_CesOverWlanUnit0PacketTxState_Object = MibTableColumn
cesOverWlanUnit0PacketTxState = _CesOverWlanUnit0PacketTxState_Object(
    (1, 3, 6, 1, 4, 1, 3942, 2, 1, 1, 3, 1, 1, 2),
    _CesOverWlanUnit0PacketTxState_Type()
)
cesOverWlanUnit0PacketTxState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cesOverWlanUnit0PacketTxState.setStatus("current")


class _CesOverWlanUnit0PacketRxState_Type(Integer32):
    """Custom type cesOverWlanUnit0PacketRxState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_CesOverWlanUnit0PacketRxState_Type.__name__ = "Integer32"
_CesOverWlanUnit0PacketRxState_Object = MibTableColumn
cesOverWlanUnit0PacketRxState = _CesOverWlanUnit0PacketRxState_Object(
    (1, 3, 6, 1, 4, 1, 3942, 2, 1, 1, 3, 1, 1, 3),
    _CesOverWlanUnit0PacketRxState_Type()
)
cesOverWlanUnit0PacketRxState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cesOverWlanUnit0PacketRxState.setStatus("current")
_CesOverWlanUnit0PacketTxRestarts_Type = Counter32
_CesOverWlanUnit0PacketTxRestarts_Object = MibTableColumn
cesOverWlanUnit0PacketTxRestarts = _CesOverWlanUnit0PacketTxRestarts_Object(
    (1, 3, 6, 1, 4, 1, 3942, 2, 1, 1, 3, 1, 1, 4),
    _CesOverWlanUnit0PacketTxRestarts_Type()
)
cesOverWlanUnit0PacketTxRestarts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cesOverWlanUnit0PacketTxRestarts.setStatus("current")
_CesOverWlanUnit0PacketRxRestarts_Type = Counter32
_CesOverWlanUnit0PacketRxRestarts_Object = MibTableColumn
cesOverWlanUnit0PacketRxRestarts = _CesOverWlanUnit0PacketRxRestarts_Object(
    (1, 3, 6, 1, 4, 1, 3942, 2, 1, 1, 3, 1, 1, 5),
    _CesOverWlanUnit0PacketRxRestarts_Type()
)
cesOverWlanUnit0PacketRxRestarts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cesOverWlanUnit0PacketRxRestarts.setStatus("current")
_CesOverWlanUnit0PacketJitterCur_Type = Integer32
_CesOverWlanUnit0PacketJitterCur_Object = MibTableColumn
cesOverWlanUnit0PacketJitterCur = _CesOverWlanUnit0PacketJitterCur_Object(
    (1, 3, 6, 1, 4, 1, 3942, 2, 1, 1, 3, 1, 1, 6),
    _CesOverWlanUnit0PacketJitterCur_Type()
)
cesOverWlanUnit0PacketJitterCur.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cesOverWlanUnit0PacketJitterCur.setStatus("current")
if mibBuilder.loadTexts:
    cesOverWlanUnit0PacketJitterCur.setUnits("microseconds")
_CesOverWlanUnit0PacketJitterMin_Type = Integer32
_CesOverWlanUnit0PacketJitterMin_Object = MibTableColumn
cesOverWlanUnit0PacketJitterMin = _CesOverWlanUnit0PacketJitterMin_Object(
    (1, 3, 6, 1, 4, 1, 3942, 2, 1, 1, 3, 1, 1, 7),
    _CesOverWlanUnit0PacketJitterMin_Type()
)
cesOverWlanUnit0PacketJitterMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cesOverWlanUnit0PacketJitterMin.setStatus("current")
if mibBuilder.loadTexts:
    cesOverWlanUnit0PacketJitterMin.setUnits("microseconds")
_CesOverWlanUnit0PacketJitterMax_Type = Integer32
_CesOverWlanUnit0PacketJitterMax_Object = MibTableColumn
cesOverWlanUnit0PacketJitterMax = _CesOverWlanUnit0PacketJitterMax_Object(
    (1, 3, 6, 1, 4, 1, 3942, 2, 1, 1, 3, 1, 1, 8),
    _CesOverWlanUnit0PacketJitterMax_Type()
)
cesOverWlanUnit0PacketJitterMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cesOverWlanUnit0PacketJitterMax.setStatus("current")
if mibBuilder.loadTexts:
    cesOverWlanUnit0PacketJitterMax.setUnits("microseconds")
_CesOverWlanUnit0PacketTotalInPackets_Type = Counter32
_CesOverWlanUnit0PacketTotalInPackets_Object = MibTableColumn
cesOverWlanUnit0PacketTotalInPackets = _CesOverWlanUnit0PacketTotalInPackets_Object(
    (1, 3, 6, 1, 4, 1, 3942, 2, 1, 1, 3, 1, 1, 9),
    _CesOverWlanUnit0PacketTotalInPackets_Type()
)
cesOverWlanUnit0PacketTotalInPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cesOverWlanUnit0PacketTotalInPackets.setStatus("current")
_CesOverWlanUnit0PacketValidPackets_Type = Counter32
_CesOverWlanUnit0PacketValidPackets_Object = MibTableColumn
cesOverWlanUnit0PacketValidPackets = _CesOverWlanUnit0PacketValidPackets_Object(
    (1, 3, 6, 1, 4, 1, 3942, 2, 1, 1, 3, 1, 1, 10),
    _CesOverWlanUnit0PacketValidPackets_Type()
)
cesOverWlanUnit0PacketValidPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cesOverWlanUnit0PacketValidPackets.setStatus("current")
_CesOverWlanUnit0PacketRbitPackets_Type = Counter32
_CesOverWlanUnit0PacketRbitPackets_Object = MibTableColumn
cesOverWlanUnit0PacketRbitPackets = _CesOverWlanUnit0PacketRbitPackets_Object(
    (1, 3, 6, 1, 4, 1, 3942, 2, 1, 1, 3, 1, 1, 11),
    _CesOverWlanUnit0PacketRbitPackets_Type()
)
cesOverWlanUnit0PacketRbitPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cesOverWlanUnit0PacketRbitPackets.setStatus("current")
_CesOverWlanUnit0PacketLbitPackets_Type = Counter32
_CesOverWlanUnit0PacketLbitPackets_Object = MibTableColumn
cesOverWlanUnit0PacketLbitPackets = _CesOverWlanUnit0PacketLbitPackets_Object(
    (1, 3, 6, 1, 4, 1, 3942, 2, 1, 1, 3, 1, 1, 12),
    _CesOverWlanUnit0PacketLbitPackets_Type()
)
cesOverWlanUnit0PacketLbitPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cesOverWlanUnit0PacketLbitPackets.setStatus("current")
_CesOverWlanUnit0PacketLatePackets_Type = Counter32
_CesOverWlanUnit0PacketLatePackets_Object = MibTableColumn
cesOverWlanUnit0PacketLatePackets = _CesOverWlanUnit0PacketLatePackets_Object(
    (1, 3, 6, 1, 4, 1, 3942, 2, 1, 1, 3, 1, 1, 13),
    _CesOverWlanUnit0PacketLatePackets_Type()
)
cesOverWlanUnit0PacketLatePackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cesOverWlanUnit0PacketLatePackets.setStatus("current")
_CesOverWlanUnit0PacketLostPackets_Type = Counter32
_CesOverWlanUnit0PacketLostPackets_Object = MibTableColumn
cesOverWlanUnit0PacketLostPackets = _CesOverWlanUnit0PacketLostPackets_Object(
    (1, 3, 6, 1, 4, 1, 3942, 2, 1, 1, 3, 1, 1, 14),
    _CesOverWlanUnit0PacketLostPackets_Type()
)
cesOverWlanUnit0PacketLostPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cesOverWlanUnit0PacketLostPackets.setStatus("current")
_CesOverWlanUnit0PacketOutOfOrderPackets_Type = Counter32
_CesOverWlanUnit0PacketOutOfOrderPackets_Object = MibTableColumn
cesOverWlanUnit0PacketOutOfOrderPackets = _CesOverWlanUnit0PacketOutOfOrderPackets_Object(
    (1, 3, 6, 1, 4, 1, 3942, 2, 1, 1, 3, 1, 1, 15),
    _CesOverWlanUnit0PacketOutOfOrderPackets_Type()
)
cesOverWlanUnit0PacketOutOfOrderPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cesOverWlanUnit0PacketOutOfOrderPackets.setStatus("current")
_CesOverWlanUnit0PacketUnderrunPackets_Type = Counter32
_CesOverWlanUnit0PacketUnderrunPackets_Object = MibTableColumn
cesOverWlanUnit0PacketUnderrunPackets = _CesOverWlanUnit0PacketUnderrunPackets_Object(
    (1, 3, 6, 1, 4, 1, 3942, 2, 1, 1, 3, 1, 1, 16),
    _CesOverWlanUnit0PacketUnderrunPackets_Type()
)
cesOverWlanUnit0PacketUnderrunPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cesOverWlanUnit0PacketUnderrunPackets.setStatus("current")
_CesOverWlanUnit0PacketOverrunPackets_Type = Counter32
_CesOverWlanUnit0PacketOverrunPackets_Object = MibTableColumn
cesOverWlanUnit0PacketOverrunPackets = _CesOverWlanUnit0PacketOverrunPackets_Object(
    (1, 3, 6, 1, 4, 1, 3942, 2, 1, 1, 3, 1, 1, 17),
    _CesOverWlanUnit0PacketOverrunPackets_Type()
)
cesOverWlanUnit0PacketOverrunPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cesOverWlanUnit0PacketOverrunPackets.setStatus("current")
_CesOverWlanUnit0PacketInvalidSequencePackets_Type = Counter32
_CesOverWlanUnit0PacketInvalidSequencePackets_Object = MibTableColumn
cesOverWlanUnit0PacketInvalidSequencePackets = _CesOverWlanUnit0PacketInvalidSequencePackets_Object(
    (1, 3, 6, 1, 4, 1, 3942, 2, 1, 1, 3, 1, 1, 18),
    _CesOverWlanUnit0PacketInvalidSequencePackets_Type()
)
cesOverWlanUnit0PacketInvalidSequencePackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cesOverWlanUnit0PacketInvalidSequencePackets.setStatus("current")
_CesOverWlanUnit0PacketDuplicatePackets_Type = Counter32
_CesOverWlanUnit0PacketDuplicatePackets_Object = MibTableColumn
cesOverWlanUnit0PacketDuplicatePackets = _CesOverWlanUnit0PacketDuplicatePackets_Object(
    (1, 3, 6, 1, 4, 1, 3942, 2, 1, 1, 3, 1, 1, 19),
    _CesOverWlanUnit0PacketDuplicatePackets_Type()
)
cesOverWlanUnit0PacketDuplicatePackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cesOverWlanUnit0PacketDuplicatePackets.setStatus("current")
_CesOverWlanUnit0PacketMalformedPackets_Type = Counter32
_CesOverWlanUnit0PacketMalformedPackets_Object = MibTableColumn
cesOverWlanUnit0PacketMalformedPackets = _CesOverWlanUnit0PacketMalformedPackets_Object(
    (1, 3, 6, 1, 4, 1, 3942, 2, 1, 1, 3, 1, 1, 20),
    _CesOverWlanUnit0PacketMalformedPackets_Type()
)
cesOverWlanUnit0PacketMalformedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cesOverWlanUnit0PacketMalformedPackets.setStatus("current")


class _CesOverWlanUnit0PacketJitterBufferStatus_Type(Integer32):
    """Custom type cesOverWlanUnit0PacketJitterBufferStatus based on Integer32"""
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
        *(("unknown", 0),
          ("undeflow", 1),
          ("overflow", 2),
          ("normal", 3))
    )


_CesOverWlanUnit0PacketJitterBufferStatus_Type.__name__ = "Integer32"
_CesOverWlanUnit0PacketJitterBufferStatus_Object = MibTableColumn
cesOverWlanUnit0PacketJitterBufferStatus = _CesOverWlanUnit0PacketJitterBufferStatus_Object(
    (1, 3, 6, 1, 4, 1, 3942, 2, 1, 1, 3, 1, 1, 21),
    _CesOverWlanUnit0PacketJitterBufferStatus_Type()
)
cesOverWlanUnit0PacketJitterBufferStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cesOverWlanUnit0PacketJitterBufferStatus.setStatus("current")
_CesOverWlanUnit0PacketJitterBufferStatusLastChange_Type = TimeStamp
_CesOverWlanUnit0PacketJitterBufferStatusLastChange_Object = MibTableColumn
cesOverWlanUnit0PacketJitterBufferStatusLastChange = _CesOverWlanUnit0PacketJitterBufferStatusLastChange_Object(
    (1, 3, 6, 1, 4, 1, 3942, 2, 1, 1, 3, 1, 1, 22),
    _CesOverWlanUnit0PacketJitterBufferStatusLastChange_Type()
)
cesOverWlanUnit0PacketJitterBufferStatusLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cesOverWlanUnit0PacketJitterBufferStatusLastChange.setStatus("current")
_CesOverWlanUnit0PacketTrapsPrefix_ObjectIdentity = ObjectIdentity
cesOverWlanUnit0PacketTrapsPrefix = _CesOverWlanUnit0PacketTrapsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3942, 2, 1, 1, 3, 2)
)
_CesOverWlanUnit0PacketTraps_ObjectIdentity = ObjectIdentity
cesOverWlanUnit0PacketTraps = _CesOverWlanUnit0PacketTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3942, 2, 1, 1, 3, 2, 0)
)
_CesOverWlanUnit0PacketMIBConformance_ObjectIdentity = ObjectIdentity
cesOverWlanUnit0PacketMIBConformance = _CesOverWlanUnit0PacketMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3942, 2, 1, 1, 3, 4)
)

# Managed Objects groups

cesOverWlanUnit0PacketGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3942, 2, 1, 1, 3, 4, 2)
)
cesOverWlanUnit0PacketGroup.setObjects(
      *(("INFINET-EXTCES-UNIT0-PACKET-MIB", "cesOverWlanUnit0PacketPortNumber"),
        ("INFINET-EXTCES-UNIT0-PACKET-MIB", "cesOverWlanUnit0PacketTxState"),
        ("INFINET-EXTCES-UNIT0-PACKET-MIB", "cesOverWlanUnit0PacketRxState"),
        ("INFINET-EXTCES-UNIT0-PACKET-MIB", "cesOverWlanUnit0PacketTxRestarts"),
        ("INFINET-EXTCES-UNIT0-PACKET-MIB", "cesOverWlanUnit0PacketRxRestarts"),
        ("INFINET-EXTCES-UNIT0-PACKET-MIB", "cesOverWlanUnit0PacketJitterCur"),
        ("INFINET-EXTCES-UNIT0-PACKET-MIB", "cesOverWlanUnit0PacketJitterMin"),
        ("INFINET-EXTCES-UNIT0-PACKET-MIB", "cesOverWlanUnit0PacketJitterMax"),
        ("INFINET-EXTCES-UNIT0-PACKET-MIB", "cesOverWlanUnit0PacketTotalInPackets"),
        ("INFINET-EXTCES-UNIT0-PACKET-MIB", "cesOverWlanUnit0PacketValidPackets"),
        ("INFINET-EXTCES-UNIT0-PACKET-MIB", "cesOverWlanUnit0PacketRbitPackets"),
        ("INFINET-EXTCES-UNIT0-PACKET-MIB", "cesOverWlanUnit0PacketLbitPackets"),
        ("INFINET-EXTCES-UNIT0-PACKET-MIB", "cesOverWlanUnit0PacketLatePackets"),
        ("INFINET-EXTCES-UNIT0-PACKET-MIB", "cesOverWlanUnit0PacketLostPackets"),
        ("INFINET-EXTCES-UNIT0-PACKET-MIB", "cesOverWlanUnit0PacketOutOfOrderPackets"),
        ("INFINET-EXTCES-UNIT0-PACKET-MIB", "cesOverWlanUnit0PacketUnderrunPackets"),
        ("INFINET-EXTCES-UNIT0-PACKET-MIB", "cesOverWlanUnit0PacketOverrunPackets"),
        ("INFINET-EXTCES-UNIT0-PACKET-MIB", "cesOverWlanUnit0PacketInvalidSequencePackets"),
        ("INFINET-EXTCES-UNIT0-PACKET-MIB", "cesOverWlanUnit0PacketDuplicatePackets"),
        ("INFINET-EXTCES-UNIT0-PACKET-MIB", "cesOverWlanUnit0PacketMalformedPackets"),
        ("INFINET-EXTCES-UNIT0-PACKET-MIB", "cesOverWlanUnit0PacketJitterBufferStatus"),
        ("INFINET-EXTCES-UNIT0-PACKET-MIB", "cesOverWlanUnit0PacketJitterBufferStatusLastChange"))
)
if mibBuilder.loadTexts:
    cesOverWlanUnit0PacketGroup.setStatus("current")


# Notification objects

cesOverWlanUnit0PacketJitterStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 3942, 2, 1, 1, 3, 2, 0, 1)
)
cesOverWlanUnit0PacketJitterStatusChange.setObjects(
      *(("INFINET-EXTCES-UNIT0-PACKET-MIB", "cesOverWlanUnit0PacketJitterBufferStatus"),
        ("INFINET-EXTCES-UNIT0-PACKET-MIB", "cesOverWlanUnit0PacketJitterBufferStatusLastChange"))
)
if mibBuilder.loadTexts:
    cesOverWlanUnit0PacketJitterStatusChange.setStatus(
        "current"
    )


# Notifications groups

cesOverWlanUnit0PacketNotifications = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 3942, 2, 1, 1, 3, 4, 1)
)
cesOverWlanUnit0PacketNotifications.setObjects(
    ("INFINET-EXTCES-UNIT0-PACKET-MIB", "cesOverWlanUnit0PacketJitterStatusChange")
)
if mibBuilder.loadTexts:
    cesOverWlanUnit0PacketNotifications.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INFINET-EXTCES-UNIT0-PACKET-MIB",
    **{"cesOverWlanUnit0Packet": cesOverWlanUnit0Packet,
       "cesOverWlanUnit0PacketTable": cesOverWlanUnit0PacketTable,
       "cesOverWlanUnit0PacketEntry": cesOverWlanUnit0PacketEntry,
       "cesOverWlanUnit0PacketPortNumber": cesOverWlanUnit0PacketPortNumber,
       "cesOverWlanUnit0PacketTxState": cesOverWlanUnit0PacketTxState,
       "cesOverWlanUnit0PacketRxState": cesOverWlanUnit0PacketRxState,
       "cesOverWlanUnit0PacketTxRestarts": cesOverWlanUnit0PacketTxRestarts,
       "cesOverWlanUnit0PacketRxRestarts": cesOverWlanUnit0PacketRxRestarts,
       "cesOverWlanUnit0PacketJitterCur": cesOverWlanUnit0PacketJitterCur,
       "cesOverWlanUnit0PacketJitterMin": cesOverWlanUnit0PacketJitterMin,
       "cesOverWlanUnit0PacketJitterMax": cesOverWlanUnit0PacketJitterMax,
       "cesOverWlanUnit0PacketTotalInPackets": cesOverWlanUnit0PacketTotalInPackets,
       "cesOverWlanUnit0PacketValidPackets": cesOverWlanUnit0PacketValidPackets,
       "cesOverWlanUnit0PacketRbitPackets": cesOverWlanUnit0PacketRbitPackets,
       "cesOverWlanUnit0PacketLbitPackets": cesOverWlanUnit0PacketLbitPackets,
       "cesOverWlanUnit0PacketLatePackets": cesOverWlanUnit0PacketLatePackets,
       "cesOverWlanUnit0PacketLostPackets": cesOverWlanUnit0PacketLostPackets,
       "cesOverWlanUnit0PacketOutOfOrderPackets": cesOverWlanUnit0PacketOutOfOrderPackets,
       "cesOverWlanUnit0PacketUnderrunPackets": cesOverWlanUnit0PacketUnderrunPackets,
       "cesOverWlanUnit0PacketOverrunPackets": cesOverWlanUnit0PacketOverrunPackets,
       "cesOverWlanUnit0PacketInvalidSequencePackets": cesOverWlanUnit0PacketInvalidSequencePackets,
       "cesOverWlanUnit0PacketDuplicatePackets": cesOverWlanUnit0PacketDuplicatePackets,
       "cesOverWlanUnit0PacketMalformedPackets": cesOverWlanUnit0PacketMalformedPackets,
       "cesOverWlanUnit0PacketJitterBufferStatus": cesOverWlanUnit0PacketJitterBufferStatus,
       "cesOverWlanUnit0PacketJitterBufferStatusLastChange": cesOverWlanUnit0PacketJitterBufferStatusLastChange,
       "cesOverWlanUnit0PacketTrapsPrefix": cesOverWlanUnit0PacketTrapsPrefix,
       "cesOverWlanUnit0PacketTraps": cesOverWlanUnit0PacketTraps,
       "cesOverWlanUnit0PacketJitterStatusChange": cesOverWlanUnit0PacketJitterStatusChange,
       "cesOverWlanUnit0PacketMIBConformance": cesOverWlanUnit0PacketMIBConformance,
       "cesOverWlanUnit0PacketNotifications": cesOverWlanUnit0PacketNotifications,
       "cesOverWlanUnit0PacketGroup": cesOverWlanUnit0PacketGroup}
)
