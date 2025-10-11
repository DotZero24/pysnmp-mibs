# SNMP MIB module (FS-WAN-FPM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/fscom/FS-WAN-FPM-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:15:45 2025
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

(fsMgmt,) = mibBuilder.importSymbols(
    "FS-SMI",
    "fsMgmt")

(IfIndex,) = mibBuilder.importSymbols(
    "FS-TC",
    "IfIndex")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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

(DateAndTime,
 DisplayString,
 PhysAddress,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

fsWanFpmMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 153)
)
if mibBuilder.loadTexts:
    fsWanFpmMIB.setRevisions(
        ("2017-01-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FsWanFpmMIBObjects_ObjectIdentity = ObjectIdentity
fsWanFpmMIBObjects = _FsWanFpmMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 153, 1)
)
_FsWanFpmResultsTable_Object = MibTable
fsWanFpmResultsTable = _FsWanFpmResultsTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 153, 1, 1)
)
if mibBuilder.loadTexts:
    fsWanFpmResultsTable.setStatus("current")
_FsWanFpmResultsEntry_Object = MibTableRow
fsWanFpmResultsEntry = _FsWanFpmResultsEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 153, 1, 1, 1)
)
fsWanFpmResultsEntry.setIndexNames(
    (0, "FS-WAN-FPM-MIB", "fsWanFpmResultsIfIndex"),
)
if mibBuilder.loadTexts:
    fsWanFpmResultsEntry.setStatus("current")
_FsWanFpmResultsIfIndex_Type = IfIndex
_FsWanFpmResultsIfIndex_Object = MibTableColumn
fsWanFpmResultsIfIndex = _FsWanFpmResultsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 153, 1, 1, 1, 1),
    _FsWanFpmResultsIfIndex_Type()
)
fsWanFpmResultsIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsWanFpmResultsIfIndex.setStatus("current")


class _FsWanFpmResultsMode_Type(Integer32):
    """Custom type fsWanFpmResultsMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("passive", 1),
          ("active", 2))
    )


_FsWanFpmResultsMode_Type.__name__ = "Integer32"
_FsWanFpmResultsMode_Object = MibTableColumn
fsWanFpmResultsMode = _FsWanFpmResultsMode_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 153, 1, 1, 1, 2),
    _FsWanFpmResultsMode_Type()
)
fsWanFpmResultsMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsWanFpmResultsMode.setStatus("current")
_FsWanFpmResultsPeerIp_Type = InetAddress
_FsWanFpmResultsPeerIp_Object = MibTableColumn
fsWanFpmResultsPeerIp = _FsWanFpmResultsPeerIp_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 153, 1, 1, 1, 3),
    _FsWanFpmResultsPeerIp_Type()
)
fsWanFpmResultsPeerIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsWanFpmResultsPeerIp.setStatus("current")
_FsWanFpmResultsNetworkAF_Type = InetAddressType
_FsWanFpmResultsNetworkAF_Object = MibTableColumn
fsWanFpmResultsNetworkAF = _FsWanFpmResultsNetworkAF_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 153, 1, 1, 1, 4),
    _FsWanFpmResultsNetworkAF_Type()
)
fsWanFpmResultsNetworkAF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsWanFpmResultsNetworkAF.setStatus("current")


class _FsWanFpmResultsSessStatus_Type(Integer32):
    """Custom type fsWanFpmResultsSessStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2),
          ("reserved", 3))
    )


_FsWanFpmResultsSessStatus_Type.__name__ = "Integer32"
_FsWanFpmResultsSessStatus_Object = MibTableColumn
fsWanFpmResultsSessStatus = _FsWanFpmResultsSessStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 153, 1, 1, 1, 5),
    _FsWanFpmResultsSessStatus_Type()
)
fsWanFpmResultsSessStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsWanFpmResultsSessStatus.setStatus("current")


class _FsWanFpmResultsLinkQuality_Type(Integer32):
    """Custom type fsWanFpmResultsLinkQuality based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("well", 1),
          ("worse", 2),
          ("reserved", 3))
    )


_FsWanFpmResultsLinkQuality_Type.__name__ = "Integer32"
_FsWanFpmResultsLinkQuality_Object = MibTableColumn
fsWanFpmResultsLinkQuality = _FsWanFpmResultsLinkQuality_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 153, 1, 1, 1, 6),
    _FsWanFpmResultsLinkQuality_Type()
)
fsWanFpmResultsLinkQuality.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsWanFpmResultsLinkQuality.setStatus("current")


class _FsWanFpmResultsWorseAction_Type(Integer32):
    """Custom type fsWanFpmResultsWorseAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("forward", 1),
          ("unforward", 2))
    )


_FsWanFpmResultsWorseAction_Type.__name__ = "Integer32"
_FsWanFpmResultsWorseAction_Object = MibTableColumn
fsWanFpmResultsWorseAction = _FsWanFpmResultsWorseAction_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 153, 1, 1, 1, 7),
    _FsWanFpmResultsWorseAction_Type()
)
fsWanFpmResultsWorseAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsWanFpmResultsWorseAction.setStatus("current")
_FsWanFpmResultsRTT_Type = Unsigned32
_FsWanFpmResultsRTT_Object = MibTableColumn
fsWanFpmResultsRTT = _FsWanFpmResultsRTT_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 153, 1, 1, 1, 8),
    _FsWanFpmResultsRTT_Type()
)
fsWanFpmResultsRTT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsWanFpmResultsRTT.setStatus("current")
_FsWanFpmResultsJitter_Type = Unsigned32
_FsWanFpmResultsJitter_Object = MibTableColumn
fsWanFpmResultsJitter = _FsWanFpmResultsJitter_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 153, 1, 1, 1, 9),
    _FsWanFpmResultsJitter_Type()
)
fsWanFpmResultsJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsWanFpmResultsJitter.setStatus("current")
_FsWanFpmResultsUpDroprate_Type = Unsigned32
_FsWanFpmResultsUpDroprate_Object = MibTableColumn
fsWanFpmResultsUpDroprate = _FsWanFpmResultsUpDroprate_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 153, 1, 1, 1, 10),
    _FsWanFpmResultsUpDroprate_Type()
)
fsWanFpmResultsUpDroprate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsWanFpmResultsUpDroprate.setStatus("current")
_FsWanFpmResultsDownDroprate_Type = Unsigned32
_FsWanFpmResultsDownDroprate_Object = MibTableColumn
fsWanFpmResultsDownDroprate = _FsWanFpmResultsDownDroprate_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 153, 1, 1, 1, 11),
    _FsWanFpmResultsDownDroprate_Type()
)
fsWanFpmResultsDownDroprate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsWanFpmResultsDownDroprate.setStatus("current")
_FsWanFpmResultsByteTxSpeed_Type = Unsigned32
_FsWanFpmResultsByteTxSpeed_Object = MibTableColumn
fsWanFpmResultsByteTxSpeed = _FsWanFpmResultsByteTxSpeed_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 153, 1, 1, 1, 12),
    _FsWanFpmResultsByteTxSpeed_Type()
)
fsWanFpmResultsByteTxSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsWanFpmResultsByteTxSpeed.setStatus("current")
_FsWanFpmResultsByteRxSpeed_Type = Unsigned32
_FsWanFpmResultsByteRxSpeed_Object = MibTableColumn
fsWanFpmResultsByteRxSpeed = _FsWanFpmResultsByteRxSpeed_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 153, 1, 1, 1, 13),
    _FsWanFpmResultsByteRxSpeed_Type()
)
fsWanFpmResultsByteRxSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsWanFpmResultsByteRxSpeed.setStatus("current")
_FsWanFpmResultsPktsTxSpeed_Type = Unsigned32
_FsWanFpmResultsPktsTxSpeed_Object = MibTableColumn
fsWanFpmResultsPktsTxSpeed = _FsWanFpmResultsPktsTxSpeed_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 153, 1, 1, 1, 14),
    _FsWanFpmResultsPktsTxSpeed_Type()
)
fsWanFpmResultsPktsTxSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsWanFpmResultsPktsTxSpeed.setStatus("current")
_FsWanFpmResultsPktsRxSpeed_Type = Unsigned32
_FsWanFpmResultsPktsRxSpeed_Object = MibTableColumn
fsWanFpmResultsPktsRxSpeed = _FsWanFpmResultsPktsRxSpeed_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 153, 1, 1, 1, 15),
    _FsWanFpmResultsPktsRxSpeed_Type()
)
fsWanFpmResultsPktsRxSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsWanFpmResultsPktsRxSpeed.setStatus("current")
_FsWanFpmResultsCresteTime_Type = DateAndTime
_FsWanFpmResultsCresteTime_Object = MibTableColumn
fsWanFpmResultsCresteTime = _FsWanFpmResultsCresteTime_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 153, 1, 1, 1, 16),
    _FsWanFpmResultsCresteTime_Type()
)
fsWanFpmResultsCresteTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsWanFpmResultsCresteTime.setStatus("current")


class _FsWanFpmResultsTrapType_Type(Integer32):
    """Custom type fsWanFpmResultsTrapType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("getPeriodResult", 1),
          ("getTickResult", 2),
          ("reserved", 3))
    )


_FsWanFpmResultsTrapType_Type.__name__ = "Integer32"
_FsWanFpmResultsTrapType_Object = MibTableColumn
fsWanFpmResultsTrapType = _FsWanFpmResultsTrapType_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 153, 1, 1, 1, 17),
    _FsWanFpmResultsTrapType_Type()
)
fsWanFpmResultsTrapType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsWanFpmResultsTrapType.setStatus("current")
_FsWanFpmResultsSessId_Type = Unsigned32
_FsWanFpmResultsSessId_Object = MibTableColumn
fsWanFpmResultsSessId = _FsWanFpmResultsSessId_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 153, 1, 1, 1, 18),
    _FsWanFpmResultsSessId_Type()
)
fsWanFpmResultsSessId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsWanFpmResultsSessId.setStatus("current")
_FsWanFpmMonitor_ObjectIdentity = ObjectIdentity
fsWanFpmMonitor = _FsWanFpmMonitor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 153, 2)
)
_FsWanFpmMonitorTRAP_ObjectIdentity = ObjectIdentity
fsWanFpmMonitorTRAP = _FsWanFpmMonitorTRAP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 153, 2, 1)
)
_FsWanFpmNotifications_ObjectIdentity = ObjectIdentity
fsWanFpmNotifications = _FsWanFpmNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 153, 2, 1, 1)
)

# Managed Objects groups


# Notification objects

fsWanFpmLqWell = NotificationType(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 153, 2, 1, 1, 1)
)
fsWanFpmLqWell.setObjects(
      *(("FS-WAN-FPM-MIB", "fsWanFpmResultsIfIndex"),
        ("FS-WAN-FPM-MIB", "fsWanFpmResultsSessStatus"),
        ("FS-WAN-FPM-MIB", "fsWanFpmResultsLinkQuality"))
)
if mibBuilder.loadTexts:
    fsWanFpmLqWell.setStatus(
        "current"
    )

fsWanFpmLqBad = NotificationType(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 153, 2, 1, 1, 2)
)
fsWanFpmLqBad.setObjects(
      *(("FS-WAN-FPM-MIB", "fsWanFpmResultsIfIndex"),
        ("FS-WAN-FPM-MIB", "fsWanFpmResultsSessStatus"),
        ("FS-WAN-FPM-MIB", "fsWanFpmResultsLinkQuality"))
)
if mibBuilder.loadTexts:
    fsWanFpmLqBad.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FS-WAN-FPM-MIB",
    **{"fsWanFpmMIB": fsWanFpmMIB,
       "fsWanFpmMIBObjects": fsWanFpmMIBObjects,
       "fsWanFpmResultsTable": fsWanFpmResultsTable,
       "fsWanFpmResultsEntry": fsWanFpmResultsEntry,
       "fsWanFpmResultsIfIndex": fsWanFpmResultsIfIndex,
       "fsWanFpmResultsMode": fsWanFpmResultsMode,
       "fsWanFpmResultsPeerIp": fsWanFpmResultsPeerIp,
       "fsWanFpmResultsNetworkAF": fsWanFpmResultsNetworkAF,
       "fsWanFpmResultsSessStatus": fsWanFpmResultsSessStatus,
       "fsWanFpmResultsLinkQuality": fsWanFpmResultsLinkQuality,
       "fsWanFpmResultsWorseAction": fsWanFpmResultsWorseAction,
       "fsWanFpmResultsRTT": fsWanFpmResultsRTT,
       "fsWanFpmResultsJitter": fsWanFpmResultsJitter,
       "fsWanFpmResultsUpDroprate": fsWanFpmResultsUpDroprate,
       "fsWanFpmResultsDownDroprate": fsWanFpmResultsDownDroprate,
       "fsWanFpmResultsByteTxSpeed": fsWanFpmResultsByteTxSpeed,
       "fsWanFpmResultsByteRxSpeed": fsWanFpmResultsByteRxSpeed,
       "fsWanFpmResultsPktsTxSpeed": fsWanFpmResultsPktsTxSpeed,
       "fsWanFpmResultsPktsRxSpeed": fsWanFpmResultsPktsRxSpeed,
       "fsWanFpmResultsCresteTime": fsWanFpmResultsCresteTime,
       "fsWanFpmResultsTrapType": fsWanFpmResultsTrapType,
       "fsWanFpmResultsSessId": fsWanFpmResultsSessId,
       "fsWanFpmMonitor": fsWanFpmMonitor,
       "fsWanFpmMonitorTRAP": fsWanFpmMonitorTRAP,
       "fsWanFpmNotifications": fsWanFpmNotifications,
       "fsWanFpmLqWell": fsWanFpmLqWell,
       "fsWanFpmLqBad": fsWanFpmLqBad}
)
