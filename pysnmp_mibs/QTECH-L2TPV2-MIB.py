# SNMP MIB module (QTECH-L2TPV2-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/qtech/QTECH-L2TPV2-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:59:05 2025
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

(qtechMgmt,) = mibBuilder.importSymbols(
    "QTECH-SMI",
    "qtechMgmt")

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

qtechL2TPv2MIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 117)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_QtechL2TPv2Objects_ObjectIdentity = ObjectIdentity
qtechL2TPv2Objects = _QtechL2TPv2Objects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 117, 1)
)
_QtechL2TPv2TunnelTable_Object = MibTable
qtechL2TPv2TunnelTable = _QtechL2TPv2TunnelTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 117, 1, 1)
)
if mibBuilder.loadTexts:
    qtechL2TPv2TunnelTable.setStatus("current")
_QtechL2TPv2TunnelEntry_Object = MibTableRow
qtechL2TPv2TunnelEntry = _QtechL2TPv2TunnelEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 117, 1, 1, 1)
)
qtechL2TPv2TunnelEntry.setIndexNames(
    (0, "QTECH-L2TPV2-MIB", "qtechL2TPv2TunnelLocalID"),
)
if mibBuilder.loadTexts:
    qtechL2TPv2TunnelEntry.setStatus("current")


class _QtechL2TPv2TunnelLocalID_Type(Unsigned32):
    """Custom type qtechL2TPv2TunnelLocalID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_QtechL2TPv2TunnelLocalID_Type.__name__ = "Unsigned32"
_QtechL2TPv2TunnelLocalID_Object = MibTableColumn
qtechL2TPv2TunnelLocalID = _QtechL2TPv2TunnelLocalID_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 117, 1, 1, 1, 1),
    _QtechL2TPv2TunnelLocalID_Type()
)
qtechL2TPv2TunnelLocalID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechL2TPv2TunnelLocalID.setStatus("current")
_QtechL2TPv2TunnelRemoteID_Type = Unsigned32
_QtechL2TPv2TunnelRemoteID_Object = MibTableColumn
qtechL2TPv2TunnelRemoteID = _QtechL2TPv2TunnelRemoteID_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 117, 1, 1, 1, 2),
    _QtechL2TPv2TunnelRemoteID_Type()
)
qtechL2TPv2TunnelRemoteID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechL2TPv2TunnelRemoteID.setStatus("current")
_QtechL2TPv2TunnelStatus_Type = Unsigned32
_QtechL2TPv2TunnelStatus_Object = MibTableColumn
qtechL2TPv2TunnelStatus = _QtechL2TPv2TunnelStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 117, 1, 1, 1, 3),
    _QtechL2TPv2TunnelStatus_Type()
)
qtechL2TPv2TunnelStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechL2TPv2TunnelStatus.setStatus("current")
_QtechL2TPv2TunnelSrcIP_Type = IpAddress
_QtechL2TPv2TunnelSrcIP_Object = MibTableColumn
qtechL2TPv2TunnelSrcIP = _QtechL2TPv2TunnelSrcIP_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 117, 1, 1, 1, 4),
    _QtechL2TPv2TunnelSrcIP_Type()
)
qtechL2TPv2TunnelSrcIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechL2TPv2TunnelSrcIP.setStatus("current")
_QtechL2TPv2TunnelDstIP_Type = IpAddress
_QtechL2TPv2TunnelDstIP_Object = MibTableColumn
qtechL2TPv2TunnelDstIP = _QtechL2TPv2TunnelDstIP_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 117, 1, 1, 1, 5),
    _QtechL2TPv2TunnelDstIP_Type()
)
qtechL2TPv2TunnelDstIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechL2TPv2TunnelDstIP.setStatus("current")
_QtechL2TPv2TunnelLacHostname_Type = OctetString
_QtechL2TPv2TunnelLacHostname_Object = MibTableColumn
qtechL2TPv2TunnelLacHostname = _QtechL2TPv2TunnelLacHostname_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 117, 1, 1, 1, 6),
    _QtechL2TPv2TunnelLacHostname_Type()
)
qtechL2TPv2TunnelLacHostname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechL2TPv2TunnelLacHostname.setStatus("current")
_QtechL2TPv2TunnelLacVendor_Type = OctetString
_QtechL2TPv2TunnelLacVendor_Object = MibTableColumn
qtechL2TPv2TunnelLacVendor = _QtechL2TPv2TunnelLacVendor_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 117, 1, 1, 1, 7),
    _QtechL2TPv2TunnelLacVendor_Type()
)
qtechL2TPv2TunnelLacVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechL2TPv2TunnelLacVendor.setStatus("current")
_QtechL2TPv2SessionTable_Object = MibTable
qtechL2TPv2SessionTable = _QtechL2TPv2SessionTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 117, 1, 2)
)
if mibBuilder.loadTexts:
    qtechL2TPv2SessionTable.setStatus("current")
_QtechL2TPv2SessionEntry_Object = MibTableRow
qtechL2TPv2SessionEntry = _QtechL2TPv2SessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 117, 1, 2, 1)
)
qtechL2TPv2SessionEntry.setIndexNames(
    (0, "QTECH-L2TPV2-MIB", "qtechL2TPv2TunnelLocalID"),
    (0, "QTECH-L2TPV2-MIB", "qtechL2TPv2SessionLocalID"),
)
if mibBuilder.loadTexts:
    qtechL2TPv2SessionEntry.setStatus("current")


class _QtechL2TPv2SessionLocalID_Type(Unsigned32):
    """Custom type qtechL2TPv2SessionLocalID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_QtechL2TPv2SessionLocalID_Type.__name__ = "Unsigned32"
_QtechL2TPv2SessionLocalID_Object = MibTableColumn
qtechL2TPv2SessionLocalID = _QtechL2TPv2SessionLocalID_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 117, 1, 2, 1, 1),
    _QtechL2TPv2SessionLocalID_Type()
)
qtechL2TPv2SessionLocalID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechL2TPv2SessionLocalID.setStatus("current")
_QtechL2TPv2SessionRemoteID_Type = Unsigned32
_QtechL2TPv2SessionRemoteID_Object = MibTableColumn
qtechL2TPv2SessionRemoteID = _QtechL2TPv2SessionRemoteID_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 117, 1, 2, 1, 2),
    _QtechL2TPv2SessionRemoteID_Type()
)
qtechL2TPv2SessionRemoteID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechL2TPv2SessionRemoteID.setStatus("current")
_QtechL2TPv2SessionUserName_Type = OctetString
_QtechL2TPv2SessionUserName_Object = MibTableColumn
qtechL2TPv2SessionUserName = _QtechL2TPv2SessionUserName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 117, 1, 2, 1, 3),
    _QtechL2TPv2SessionUserName_Type()
)
qtechL2TPv2SessionUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechL2TPv2SessionUserName.setStatus("current")
_QtechL2TPv2SessionStatus_Type = Unsigned32
_QtechL2TPv2SessionStatus_Object = MibTableColumn
qtechL2TPv2SessionStatus = _QtechL2TPv2SessionStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 117, 1, 2, 1, 4),
    _QtechL2TPv2SessionStatus_Type()
)
qtechL2TPv2SessionStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechL2TPv2SessionStatus.setStatus("current")
_QtechL2TPv2SessionSrcIP_Type = IpAddress
_QtechL2TPv2SessionSrcIP_Object = MibTableColumn
qtechL2TPv2SessionSrcIP = _QtechL2TPv2SessionSrcIP_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 117, 1, 2, 1, 5),
    _QtechL2TPv2SessionSrcIP_Type()
)
qtechL2TPv2SessionSrcIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechL2TPv2SessionSrcIP.setStatus("current")
_QtechL2TPv2SessionDstIP_Type = IpAddress
_QtechL2TPv2SessionDstIP_Object = MibTableColumn
qtechL2TPv2SessionDstIP = _QtechL2TPv2SessionDstIP_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 117, 1, 2, 1, 6),
    _QtechL2TPv2SessionDstIP_Type()
)
qtechL2TPv2SessionDstIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechL2TPv2SessionDstIP.setStatus("current")
_QtechL2TPv2SessionLocalVrf_Type = Integer32
_QtechL2TPv2SessionLocalVrf_Object = MibTableColumn
qtechL2TPv2SessionLocalVrf = _QtechL2TPv2SessionLocalVrf_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 117, 1, 2, 1, 7),
    _QtechL2TPv2SessionLocalVrf_Type()
)
qtechL2TPv2SessionLocalVrf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechL2TPv2SessionLocalVrf.setStatus("current")
_QtechL2TPv2SessionExistTime_Type = Integer32
_QtechL2TPv2SessionExistTime_Object = MibTableColumn
qtechL2TPv2SessionExistTime = _QtechL2TPv2SessionExistTime_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 117, 1, 2, 1, 8),
    _QtechL2TPv2SessionExistTime_Type()
)
qtechL2TPv2SessionExistTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechL2TPv2SessionExistTime.setStatus("current")
_QtechL2TPv2SessionIMSI_Type = OctetString
_QtechL2TPv2SessionIMSI_Object = MibTableColumn
qtechL2TPv2SessionIMSI = _QtechL2TPv2SessionIMSI_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 117, 1, 2, 1, 9),
    _QtechL2TPv2SessionIMSI_Type()
)
qtechL2TPv2SessionIMSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechL2TPv2SessionIMSI.setStatus("current")
_QtechL2TPv2SessionAccessDeviceID_Type = OctetString
_QtechL2TPv2SessionAccessDeviceID_Object = MibTableColumn
qtechL2TPv2SessionAccessDeviceID = _QtechL2TPv2SessionAccessDeviceID_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 117, 1, 2, 1, 10),
    _QtechL2TPv2SessionAccessDeviceID_Type()
)
qtechL2TPv2SessionAccessDeviceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechL2TPv2SessionAccessDeviceID.setStatus("current")
_QtechL2TPv2SessionTrafficStatTable_Object = MibTable
qtechL2TPv2SessionTrafficStatTable = _QtechL2TPv2SessionTrafficStatTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 117, 1, 3)
)
if mibBuilder.loadTexts:
    qtechL2TPv2SessionTrafficStatTable.setStatus("current")
_QtechL2TPv2SessionTrafficStatEntry_Object = MibTableRow
qtechL2TPv2SessionTrafficStatEntry = _QtechL2TPv2SessionTrafficStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 117, 1, 3, 1)
)
qtechL2TPv2SessionTrafficStatEntry.setIndexNames(
    (0, "QTECH-L2TPV2-MIB", "qtechL2TPv2TunnelLocalID"),
    (0, "QTECH-L2TPV2-MIB", "qtechL2TPv2SessionLocalID"),
)
if mibBuilder.loadTexts:
    qtechL2TPv2SessionTrafficStatEntry.setStatus("current")
_QtechL2TPv2SessionTrafficStatRxBytes_Type = Counter64
_QtechL2TPv2SessionTrafficStatRxBytes_Object = MibTableColumn
qtechL2TPv2SessionTrafficStatRxBytes = _QtechL2TPv2SessionTrafficStatRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 117, 1, 3, 1, 1),
    _QtechL2TPv2SessionTrafficStatRxBytes_Type()
)
qtechL2TPv2SessionTrafficStatRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechL2TPv2SessionTrafficStatRxBytes.setStatus("current")
_QtechL2TPv2SessionTrafficStatRxPkts_Type = Counter64
_QtechL2TPv2SessionTrafficStatRxPkts_Object = MibTableColumn
qtechL2TPv2SessionTrafficStatRxPkts = _QtechL2TPv2SessionTrafficStatRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 117, 1, 3, 1, 2),
    _QtechL2TPv2SessionTrafficStatRxPkts_Type()
)
qtechL2TPv2SessionTrafficStatRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechL2TPv2SessionTrafficStatRxPkts.setStatus("current")
_QtechL2TPv2SessionTrafficStatRxErrPkts_Type = Counter64
_QtechL2TPv2SessionTrafficStatRxErrPkts_Object = MibTableColumn
qtechL2TPv2SessionTrafficStatRxErrPkts = _QtechL2TPv2SessionTrafficStatRxErrPkts_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 117, 1, 3, 1, 3),
    _QtechL2TPv2SessionTrafficStatRxErrPkts_Type()
)
qtechL2TPv2SessionTrafficStatRxErrPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechL2TPv2SessionTrafficStatRxErrPkts.setStatus("current")
_QtechL2TPv2SessionTrafficStatRxSpeed_Type = Counter64
_QtechL2TPv2SessionTrafficStatRxSpeed_Object = MibTableColumn
qtechL2TPv2SessionTrafficStatRxSpeed = _QtechL2TPv2SessionTrafficStatRxSpeed_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 117, 1, 3, 1, 4),
    _QtechL2TPv2SessionTrafficStatRxSpeed_Type()
)
qtechL2TPv2SessionTrafficStatRxSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechL2TPv2SessionTrafficStatRxSpeed.setStatus("current")
_QtechL2TPv2SessionTrafficStatTxBytes_Type = Counter64
_QtechL2TPv2SessionTrafficStatTxBytes_Object = MibTableColumn
qtechL2TPv2SessionTrafficStatTxBytes = _QtechL2TPv2SessionTrafficStatTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 117, 1, 3, 1, 5),
    _QtechL2TPv2SessionTrafficStatTxBytes_Type()
)
qtechL2TPv2SessionTrafficStatTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechL2TPv2SessionTrafficStatTxBytes.setStatus("current")
_QtechL2TPv2SessionTrafficStatTxPkts_Type = Counter64
_QtechL2TPv2SessionTrafficStatTxPkts_Object = MibTableColumn
qtechL2TPv2SessionTrafficStatTxPkts = _QtechL2TPv2SessionTrafficStatTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 117, 1, 3, 1, 6),
    _QtechL2TPv2SessionTrafficStatTxPkts_Type()
)
qtechL2TPv2SessionTrafficStatTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechL2TPv2SessionTrafficStatTxPkts.setStatus("current")
_QtechL2TPv2SessionTrafficStatTxSpeed_Type = Counter64
_QtechL2TPv2SessionTrafficStatTxSpeed_Object = MibTableColumn
qtechL2TPv2SessionTrafficStatTxSpeed = _QtechL2TPv2SessionTrafficStatTxSpeed_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 117, 1, 3, 1, 7),
    _QtechL2TPv2SessionTrafficStatTxSpeed_Type()
)
qtechL2TPv2SessionTrafficStatTxSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechL2TPv2SessionTrafficStatTxSpeed.setStatus("current")
_QtechL2TPv2Notifications_ObjectIdentity = ObjectIdentity
qtechL2TPv2Notifications = _QtechL2TPv2Notifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 117, 2)
)
_QtechL2TPv2SessionNotifications_ObjectIdentity = ObjectIdentity
qtechL2TPv2SessionNotifications = _QtechL2TPv2SessionNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 117, 2, 1)
)
_QtechL2TPVersion_Type = OctetString
_QtechL2TPVersion_Object = MibScalar
qtechL2TPVersion = _QtechL2TPVersion_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 117, 3),
    _QtechL2TPVersion_Type()
)
qtechL2TPVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechL2TPVersion.setStatus("current")

# Managed Objects groups


# Notification objects

qtechL2TPv2SessionStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 117, 2, 1, 1)
)
qtechL2TPv2SessionStart.setObjects(
      *(("QTECH-L2TPV2-MIB", "qtechL2TPv2TunnelDstIP"),
        ("QTECH-L2TPV2-MIB", "qtechL2TPv2TunnelLocalID"),
        ("QTECH-L2TPV2-MIB", "qtechL2TPv2SessionLocalID"),
        ("QTECH-L2TPV2-MIB", "qtechL2TPv2SessionIMSI"),
        ("QTECH-L2TPV2-MIB", "qtechL2TPv2SessionAccessDeviceID"),
        ("QTECH-L2TPV2-MIB", "qtechL2TPv2SessionSrcIP"),
        ("QTECH-L2TPV2-MIB", "qtechL2TPv2SessionExistTime"),
        ("QTECH-L2TPV2-MIB", "qtechL2TPv2SessionLocalVrf"),
        ("QTECH-L2TPV2-MIB", "qtechL2TPv2SessionDstIP"),
        ("QTECH-L2TPV2-MIB", "qtechL2TPv2TunnelSrcIP"))
)
if mibBuilder.loadTexts:
    qtechL2TPv2SessionStart.setStatus(
        "current"
    )

qtechL2TPv2SessionStop = NotificationType(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 117, 2, 1, 2)
)
qtechL2TPv2SessionStop.setObjects(
      *(("QTECH-L2TPV2-MIB", "qtechL2TPv2TunnelLocalID"),
        ("QTECH-L2TPV2-MIB", "qtechL2TPv2SessionLocalID"),
        ("QTECH-L2TPV2-MIB", "qtechL2TPv2TunnelSrcIP"),
        ("QTECH-L2TPV2-MIB", "qtechL2TPv2TunnelDstIP"),
        ("QTECH-L2TPV2-MIB", "qtechL2TPv2SessionSrcIP"),
        ("QTECH-L2TPV2-MIB", "qtechL2TPv2SessionDstIP"),
        ("QTECH-L2TPV2-MIB", "qtechL2TPv2SessionLocalVrf"),
        ("QTECH-L2TPV2-MIB", "qtechL2TPv2SessionExistTime"),
        ("QTECH-L2TPV2-MIB", "qtechL2TPv2SessionIMSI"),
        ("QTECH-L2TPV2-MIB", "qtechL2TPv2SessionAccessDeviceID"))
)
if mibBuilder.loadTexts:
    qtechL2TPv2SessionStop.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "QTECH-L2TPV2-MIB",
    **{"qtechL2TPv2MIB": qtechL2TPv2MIB,
       "qtechL2TPv2Objects": qtechL2TPv2Objects,
       "qtechL2TPv2TunnelTable": qtechL2TPv2TunnelTable,
       "qtechL2TPv2TunnelEntry": qtechL2TPv2TunnelEntry,
       "qtechL2TPv2TunnelLocalID": qtechL2TPv2TunnelLocalID,
       "qtechL2TPv2TunnelRemoteID": qtechL2TPv2TunnelRemoteID,
       "qtechL2TPv2TunnelStatus": qtechL2TPv2TunnelStatus,
       "qtechL2TPv2TunnelSrcIP": qtechL2TPv2TunnelSrcIP,
       "qtechL2TPv2TunnelDstIP": qtechL2TPv2TunnelDstIP,
       "qtechL2TPv2TunnelLacHostname": qtechL2TPv2TunnelLacHostname,
       "qtechL2TPv2TunnelLacVendor": qtechL2TPv2TunnelLacVendor,
       "qtechL2TPv2SessionTable": qtechL2TPv2SessionTable,
       "qtechL2TPv2SessionEntry": qtechL2TPv2SessionEntry,
       "qtechL2TPv2SessionLocalID": qtechL2TPv2SessionLocalID,
       "qtechL2TPv2SessionRemoteID": qtechL2TPv2SessionRemoteID,
       "qtechL2TPv2SessionUserName": qtechL2TPv2SessionUserName,
       "qtechL2TPv2SessionStatus": qtechL2TPv2SessionStatus,
       "qtechL2TPv2SessionSrcIP": qtechL2TPv2SessionSrcIP,
       "qtechL2TPv2SessionDstIP": qtechL2TPv2SessionDstIP,
       "qtechL2TPv2SessionLocalVrf": qtechL2TPv2SessionLocalVrf,
       "qtechL2TPv2SessionExistTime": qtechL2TPv2SessionExistTime,
       "qtechL2TPv2SessionIMSI": qtechL2TPv2SessionIMSI,
       "qtechL2TPv2SessionAccessDeviceID": qtechL2TPv2SessionAccessDeviceID,
       "qtechL2TPv2SessionTrafficStatTable": qtechL2TPv2SessionTrafficStatTable,
       "qtechL2TPv2SessionTrafficStatEntry": qtechL2TPv2SessionTrafficStatEntry,
       "qtechL2TPv2SessionTrafficStatRxBytes": qtechL2TPv2SessionTrafficStatRxBytes,
       "qtechL2TPv2SessionTrafficStatRxPkts": qtechL2TPv2SessionTrafficStatRxPkts,
       "qtechL2TPv2SessionTrafficStatRxErrPkts": qtechL2TPv2SessionTrafficStatRxErrPkts,
       "qtechL2TPv2SessionTrafficStatRxSpeed": qtechL2TPv2SessionTrafficStatRxSpeed,
       "qtechL2TPv2SessionTrafficStatTxBytes": qtechL2TPv2SessionTrafficStatTxBytes,
       "qtechL2TPv2SessionTrafficStatTxPkts": qtechL2TPv2SessionTrafficStatTxPkts,
       "qtechL2TPv2SessionTrafficStatTxSpeed": qtechL2TPv2SessionTrafficStatTxSpeed,
       "qtechL2TPv2Notifications": qtechL2TPv2Notifications,
       "qtechL2TPv2SessionNotifications": qtechL2TPv2SessionNotifications,
       "qtechL2TPv2SessionStart": qtechL2TPv2SessionStart,
       "qtechL2TPv2SessionStop": qtechL2TPv2SessionStop,
       "qtechL2TPVersion": qtechL2TPVersion}
)
