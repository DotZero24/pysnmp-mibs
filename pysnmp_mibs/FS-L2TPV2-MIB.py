# SNMP MIB module (FS-L2TPV2-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/fscom/FS-L2TPV2-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:12:45 2025
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

fsL2TPv2MIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 117)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FsL2TPv2Objects_ObjectIdentity = ObjectIdentity
fsL2TPv2Objects = _FsL2TPv2Objects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 117, 1)
)
_FsL2TPv2TunnelTable_Object = MibTable
fsL2TPv2TunnelTable = _FsL2TPv2TunnelTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 117, 1, 1)
)
if mibBuilder.loadTexts:
    fsL2TPv2TunnelTable.setStatus("current")
_FsL2TPv2TunnelEntry_Object = MibTableRow
fsL2TPv2TunnelEntry = _FsL2TPv2TunnelEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 117, 1, 1, 1)
)
fsL2TPv2TunnelEntry.setIndexNames(
    (0, "FS-L2TPV2-MIB", "fsL2TPv2TunnelLocalID"),
)
if mibBuilder.loadTexts:
    fsL2TPv2TunnelEntry.setStatus("current")


class _FsL2TPv2TunnelLocalID_Type(Unsigned32):
    """Custom type fsL2TPv2TunnelLocalID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_FsL2TPv2TunnelLocalID_Type.__name__ = "Unsigned32"
_FsL2TPv2TunnelLocalID_Object = MibTableColumn
fsL2TPv2TunnelLocalID = _FsL2TPv2TunnelLocalID_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 117, 1, 1, 1, 1),
    _FsL2TPv2TunnelLocalID_Type()
)
fsL2TPv2TunnelLocalID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsL2TPv2TunnelLocalID.setStatus("current")
_FsL2TPv2TunnelRemoteID_Type = Unsigned32
_FsL2TPv2TunnelRemoteID_Object = MibTableColumn
fsL2TPv2TunnelRemoteID = _FsL2TPv2TunnelRemoteID_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 117, 1, 1, 1, 2),
    _FsL2TPv2TunnelRemoteID_Type()
)
fsL2TPv2TunnelRemoteID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsL2TPv2TunnelRemoteID.setStatus("current")
_FsL2TPv2TunnelStatus_Type = Unsigned32
_FsL2TPv2TunnelStatus_Object = MibTableColumn
fsL2TPv2TunnelStatus = _FsL2TPv2TunnelStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 117, 1, 1, 1, 3),
    _FsL2TPv2TunnelStatus_Type()
)
fsL2TPv2TunnelStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsL2TPv2TunnelStatus.setStatus("current")
_FsL2TPv2TunnelSrcIP_Type = IpAddress
_FsL2TPv2TunnelSrcIP_Object = MibTableColumn
fsL2TPv2TunnelSrcIP = _FsL2TPv2TunnelSrcIP_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 117, 1, 1, 1, 4),
    _FsL2TPv2TunnelSrcIP_Type()
)
fsL2TPv2TunnelSrcIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsL2TPv2TunnelSrcIP.setStatus("current")
_FsL2TPv2TunnelDstIP_Type = IpAddress
_FsL2TPv2TunnelDstIP_Object = MibTableColumn
fsL2TPv2TunnelDstIP = _FsL2TPv2TunnelDstIP_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 117, 1, 1, 1, 5),
    _FsL2TPv2TunnelDstIP_Type()
)
fsL2TPv2TunnelDstIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsL2TPv2TunnelDstIP.setStatus("current")
_FsL2TPv2TunnelLacHostname_Type = OctetString
_FsL2TPv2TunnelLacHostname_Object = MibTableColumn
fsL2TPv2TunnelLacHostname = _FsL2TPv2TunnelLacHostname_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 117, 1, 1, 1, 6),
    _FsL2TPv2TunnelLacHostname_Type()
)
fsL2TPv2TunnelLacHostname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsL2TPv2TunnelLacHostname.setStatus("current")
_FsL2TPv2TunnelLacVendor_Type = OctetString
_FsL2TPv2TunnelLacVendor_Object = MibTableColumn
fsL2TPv2TunnelLacVendor = _FsL2TPv2TunnelLacVendor_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 117, 1, 1, 1, 7),
    _FsL2TPv2TunnelLacVendor_Type()
)
fsL2TPv2TunnelLacVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsL2TPv2TunnelLacVendor.setStatus("current")
_FsL2TPv2SessionTable_Object = MibTable
fsL2TPv2SessionTable = _FsL2TPv2SessionTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 117, 1, 2)
)
if mibBuilder.loadTexts:
    fsL2TPv2SessionTable.setStatus("current")
_FsL2TPv2SessionEntry_Object = MibTableRow
fsL2TPv2SessionEntry = _FsL2TPv2SessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 117, 1, 2, 1)
)
fsL2TPv2SessionEntry.setIndexNames(
    (0, "FS-L2TPV2-MIB", "fsL2TPv2TunnelLocalID"),
    (0, "FS-L2TPV2-MIB", "fsL2TPv2SessionLocalID"),
)
if mibBuilder.loadTexts:
    fsL2TPv2SessionEntry.setStatus("current")


class _FsL2TPv2SessionLocalID_Type(Unsigned32):
    """Custom type fsL2TPv2SessionLocalID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_FsL2TPv2SessionLocalID_Type.__name__ = "Unsigned32"
_FsL2TPv2SessionLocalID_Object = MibTableColumn
fsL2TPv2SessionLocalID = _FsL2TPv2SessionLocalID_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 117, 1, 2, 1, 1),
    _FsL2TPv2SessionLocalID_Type()
)
fsL2TPv2SessionLocalID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsL2TPv2SessionLocalID.setStatus("current")
_FsL2TPv2SessionRemoteID_Type = Unsigned32
_FsL2TPv2SessionRemoteID_Object = MibTableColumn
fsL2TPv2SessionRemoteID = _FsL2TPv2SessionRemoteID_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 117, 1, 2, 1, 2),
    _FsL2TPv2SessionRemoteID_Type()
)
fsL2TPv2SessionRemoteID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsL2TPv2SessionRemoteID.setStatus("current")
_FsL2TPv2SessionUserName_Type = OctetString
_FsL2TPv2SessionUserName_Object = MibTableColumn
fsL2TPv2SessionUserName = _FsL2TPv2SessionUserName_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 117, 1, 2, 1, 3),
    _FsL2TPv2SessionUserName_Type()
)
fsL2TPv2SessionUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsL2TPv2SessionUserName.setStatus("current")
_FsL2TPv2SessionStatus_Type = Unsigned32
_FsL2TPv2SessionStatus_Object = MibTableColumn
fsL2TPv2SessionStatus = _FsL2TPv2SessionStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 117, 1, 2, 1, 4),
    _FsL2TPv2SessionStatus_Type()
)
fsL2TPv2SessionStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsL2TPv2SessionStatus.setStatus("current")
_FsL2TPv2SessionSrcIP_Type = IpAddress
_FsL2TPv2SessionSrcIP_Object = MibTableColumn
fsL2TPv2SessionSrcIP = _FsL2TPv2SessionSrcIP_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 117, 1, 2, 1, 5),
    _FsL2TPv2SessionSrcIP_Type()
)
fsL2TPv2SessionSrcIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsL2TPv2SessionSrcIP.setStatus("current")
_FsL2TPv2SessionDstIP_Type = IpAddress
_FsL2TPv2SessionDstIP_Object = MibTableColumn
fsL2TPv2SessionDstIP = _FsL2TPv2SessionDstIP_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 117, 1, 2, 1, 6),
    _FsL2TPv2SessionDstIP_Type()
)
fsL2TPv2SessionDstIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsL2TPv2SessionDstIP.setStatus("current")
_FsL2TPv2SessionLocalVrf_Type = Integer32
_FsL2TPv2SessionLocalVrf_Object = MibTableColumn
fsL2TPv2SessionLocalVrf = _FsL2TPv2SessionLocalVrf_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 117, 1, 2, 1, 7),
    _FsL2TPv2SessionLocalVrf_Type()
)
fsL2TPv2SessionLocalVrf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsL2TPv2SessionLocalVrf.setStatus("current")
_FsL2TPv2SessionExistTime_Type = Integer32
_FsL2TPv2SessionExistTime_Object = MibTableColumn
fsL2TPv2SessionExistTime = _FsL2TPv2SessionExistTime_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 117, 1, 2, 1, 8),
    _FsL2TPv2SessionExistTime_Type()
)
fsL2TPv2SessionExistTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsL2TPv2SessionExistTime.setStatus("current")
_FsL2TPv2SessionIMSI_Type = OctetString
_FsL2TPv2SessionIMSI_Object = MibTableColumn
fsL2TPv2SessionIMSI = _FsL2TPv2SessionIMSI_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 117, 1, 2, 1, 9),
    _FsL2TPv2SessionIMSI_Type()
)
fsL2TPv2SessionIMSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsL2TPv2SessionIMSI.setStatus("current")
_FsL2TPv2SessionAccessDeviceID_Type = OctetString
_FsL2TPv2SessionAccessDeviceID_Object = MibTableColumn
fsL2TPv2SessionAccessDeviceID = _FsL2TPv2SessionAccessDeviceID_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 117, 1, 2, 1, 10),
    _FsL2TPv2SessionAccessDeviceID_Type()
)
fsL2TPv2SessionAccessDeviceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsL2TPv2SessionAccessDeviceID.setStatus("current")
_FsL2TPv2SessionTrafficStatTable_Object = MibTable
fsL2TPv2SessionTrafficStatTable = _FsL2TPv2SessionTrafficStatTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 117, 1, 3)
)
if mibBuilder.loadTexts:
    fsL2TPv2SessionTrafficStatTable.setStatus("current")
_FsL2TPv2SessionTrafficStatEntry_Object = MibTableRow
fsL2TPv2SessionTrafficStatEntry = _FsL2TPv2SessionTrafficStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 117, 1, 3, 1)
)
fsL2TPv2SessionTrafficStatEntry.setIndexNames(
    (0, "FS-L2TPV2-MIB", "fsL2TPv2TunnelLocalID"),
    (0, "FS-L2TPV2-MIB", "fsL2TPv2SessionLocalID"),
)
if mibBuilder.loadTexts:
    fsL2TPv2SessionTrafficStatEntry.setStatus("current")
_FsL2TPv2SessionTrafficStatRxBytes_Type = Counter64
_FsL2TPv2SessionTrafficStatRxBytes_Object = MibTableColumn
fsL2TPv2SessionTrafficStatRxBytes = _FsL2TPv2SessionTrafficStatRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 117, 1, 3, 1, 1),
    _FsL2TPv2SessionTrafficStatRxBytes_Type()
)
fsL2TPv2SessionTrafficStatRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsL2TPv2SessionTrafficStatRxBytes.setStatus("current")
_FsL2TPv2SessionTrafficStatRxPkts_Type = Counter64
_FsL2TPv2SessionTrafficStatRxPkts_Object = MibTableColumn
fsL2TPv2SessionTrafficStatRxPkts = _FsL2TPv2SessionTrafficStatRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 117, 1, 3, 1, 2),
    _FsL2TPv2SessionTrafficStatRxPkts_Type()
)
fsL2TPv2SessionTrafficStatRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsL2TPv2SessionTrafficStatRxPkts.setStatus("current")
_FsL2TPv2SessionTrafficStatRxErrPkts_Type = Counter64
_FsL2TPv2SessionTrafficStatRxErrPkts_Object = MibTableColumn
fsL2TPv2SessionTrafficStatRxErrPkts = _FsL2TPv2SessionTrafficStatRxErrPkts_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 117, 1, 3, 1, 3),
    _FsL2TPv2SessionTrafficStatRxErrPkts_Type()
)
fsL2TPv2SessionTrafficStatRxErrPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsL2TPv2SessionTrafficStatRxErrPkts.setStatus("current")
_FsL2TPv2SessionTrafficStatRxSpeed_Type = Counter64
_FsL2TPv2SessionTrafficStatRxSpeed_Object = MibTableColumn
fsL2TPv2SessionTrafficStatRxSpeed = _FsL2TPv2SessionTrafficStatRxSpeed_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 117, 1, 3, 1, 4),
    _FsL2TPv2SessionTrafficStatRxSpeed_Type()
)
fsL2TPv2SessionTrafficStatRxSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsL2TPv2SessionTrafficStatRxSpeed.setStatus("current")
_FsL2TPv2SessionTrafficStatTxBytes_Type = Counter64
_FsL2TPv2SessionTrafficStatTxBytes_Object = MibTableColumn
fsL2TPv2SessionTrafficStatTxBytes = _FsL2TPv2SessionTrafficStatTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 117, 1, 3, 1, 5),
    _FsL2TPv2SessionTrafficStatTxBytes_Type()
)
fsL2TPv2SessionTrafficStatTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsL2TPv2SessionTrafficStatTxBytes.setStatus("current")
_FsL2TPv2SessionTrafficStatTxPkts_Type = Counter64
_FsL2TPv2SessionTrafficStatTxPkts_Object = MibTableColumn
fsL2TPv2SessionTrafficStatTxPkts = _FsL2TPv2SessionTrafficStatTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 117, 1, 3, 1, 6),
    _FsL2TPv2SessionTrafficStatTxPkts_Type()
)
fsL2TPv2SessionTrafficStatTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsL2TPv2SessionTrafficStatTxPkts.setStatus("current")
_FsL2TPv2SessionTrafficStatTxSpeed_Type = Counter64
_FsL2TPv2SessionTrafficStatTxSpeed_Object = MibTableColumn
fsL2TPv2SessionTrafficStatTxSpeed = _FsL2TPv2SessionTrafficStatTxSpeed_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 117, 1, 3, 1, 7),
    _FsL2TPv2SessionTrafficStatTxSpeed_Type()
)
fsL2TPv2SessionTrafficStatTxSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsL2TPv2SessionTrafficStatTxSpeed.setStatus("current")
_FsL2TPv2Notifications_ObjectIdentity = ObjectIdentity
fsL2TPv2Notifications = _FsL2TPv2Notifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 117, 2)
)
_FsL2TPv2SessionNotifications_ObjectIdentity = ObjectIdentity
fsL2TPv2SessionNotifications = _FsL2TPv2SessionNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 117, 2, 1)
)
_FsL2TPVersion_Type = OctetString
_FsL2TPVersion_Object = MibScalar
fsL2TPVersion = _FsL2TPVersion_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 117, 3),
    _FsL2TPVersion_Type()
)
fsL2TPVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsL2TPVersion.setStatus("current")

# Managed Objects groups


# Notification objects

fsL2TPv2SessionStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 117, 2, 1, 1)
)
fsL2TPv2SessionStart.setObjects(
      *(("FS-L2TPV2-MIB", "fsL2TPv2TunnelDstIP"),
        ("FS-L2TPV2-MIB", "fsL2TPv2TunnelLocalID"),
        ("FS-L2TPV2-MIB", "fsL2TPv2SessionLocalID"),
        ("FS-L2TPV2-MIB", "fsL2TPv2SessionIMSI"),
        ("FS-L2TPV2-MIB", "fsL2TPv2SessionAccessDeviceID"),
        ("FS-L2TPV2-MIB", "fsL2TPv2SessionSrcIP"),
        ("FS-L2TPV2-MIB", "fsL2TPv2SessionExistTime"),
        ("FS-L2TPV2-MIB", "fsL2TPv2SessionLocalVrf"),
        ("FS-L2TPV2-MIB", "fsL2TPv2SessionDstIP"),
        ("FS-L2TPV2-MIB", "fsL2TPv2TunnelSrcIP"))
)
if mibBuilder.loadTexts:
    fsL2TPv2SessionStart.setStatus(
        "current"
    )

fsL2TPv2SessionStop = NotificationType(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 117, 2, 1, 2)
)
fsL2TPv2SessionStop.setObjects(
      *(("FS-L2TPV2-MIB", "fsL2TPv2TunnelLocalID"),
        ("FS-L2TPV2-MIB", "fsL2TPv2SessionLocalID"),
        ("FS-L2TPV2-MIB", "fsL2TPv2TunnelSrcIP"),
        ("FS-L2TPV2-MIB", "fsL2TPv2TunnelDstIP"),
        ("FS-L2TPV2-MIB", "fsL2TPv2SessionSrcIP"),
        ("FS-L2TPV2-MIB", "fsL2TPv2SessionDstIP"),
        ("FS-L2TPV2-MIB", "fsL2TPv2SessionLocalVrf"),
        ("FS-L2TPV2-MIB", "fsL2TPv2SessionExistTime"),
        ("FS-L2TPV2-MIB", "fsL2TPv2SessionIMSI"),
        ("FS-L2TPV2-MIB", "fsL2TPv2SessionAccessDeviceID"))
)
if mibBuilder.loadTexts:
    fsL2TPv2SessionStop.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FS-L2TPV2-MIB",
    **{"fsL2TPv2MIB": fsL2TPv2MIB,
       "fsL2TPv2Objects": fsL2TPv2Objects,
       "fsL2TPv2TunnelTable": fsL2TPv2TunnelTable,
       "fsL2TPv2TunnelEntry": fsL2TPv2TunnelEntry,
       "fsL2TPv2TunnelLocalID": fsL2TPv2TunnelLocalID,
       "fsL2TPv2TunnelRemoteID": fsL2TPv2TunnelRemoteID,
       "fsL2TPv2TunnelStatus": fsL2TPv2TunnelStatus,
       "fsL2TPv2TunnelSrcIP": fsL2TPv2TunnelSrcIP,
       "fsL2TPv2TunnelDstIP": fsL2TPv2TunnelDstIP,
       "fsL2TPv2TunnelLacHostname": fsL2TPv2TunnelLacHostname,
       "fsL2TPv2TunnelLacVendor": fsL2TPv2TunnelLacVendor,
       "fsL2TPv2SessionTable": fsL2TPv2SessionTable,
       "fsL2TPv2SessionEntry": fsL2TPv2SessionEntry,
       "fsL2TPv2SessionLocalID": fsL2TPv2SessionLocalID,
       "fsL2TPv2SessionRemoteID": fsL2TPv2SessionRemoteID,
       "fsL2TPv2SessionUserName": fsL2TPv2SessionUserName,
       "fsL2TPv2SessionStatus": fsL2TPv2SessionStatus,
       "fsL2TPv2SessionSrcIP": fsL2TPv2SessionSrcIP,
       "fsL2TPv2SessionDstIP": fsL2TPv2SessionDstIP,
       "fsL2TPv2SessionLocalVrf": fsL2TPv2SessionLocalVrf,
       "fsL2TPv2SessionExistTime": fsL2TPv2SessionExistTime,
       "fsL2TPv2SessionIMSI": fsL2TPv2SessionIMSI,
       "fsL2TPv2SessionAccessDeviceID": fsL2TPv2SessionAccessDeviceID,
       "fsL2TPv2SessionTrafficStatTable": fsL2TPv2SessionTrafficStatTable,
       "fsL2TPv2SessionTrafficStatEntry": fsL2TPv2SessionTrafficStatEntry,
       "fsL2TPv2SessionTrafficStatRxBytes": fsL2TPv2SessionTrafficStatRxBytes,
       "fsL2TPv2SessionTrafficStatRxPkts": fsL2TPv2SessionTrafficStatRxPkts,
       "fsL2TPv2SessionTrafficStatRxErrPkts": fsL2TPv2SessionTrafficStatRxErrPkts,
       "fsL2TPv2SessionTrafficStatRxSpeed": fsL2TPv2SessionTrafficStatRxSpeed,
       "fsL2TPv2SessionTrafficStatTxBytes": fsL2TPv2SessionTrafficStatTxBytes,
       "fsL2TPv2SessionTrafficStatTxPkts": fsL2TPv2SessionTrafficStatTxPkts,
       "fsL2TPv2SessionTrafficStatTxSpeed": fsL2TPv2SessionTrafficStatTxSpeed,
       "fsL2TPv2Notifications": fsL2TPv2Notifications,
       "fsL2TPv2SessionNotifications": fsL2TPv2SessionNotifications,
       "fsL2TPv2SessionStart": fsL2TPv2SessionStart,
       "fsL2TPv2SessionStop": fsL2TPv2SessionStop,
       "fsL2TPVersion": fsL2TPVersion}
)
