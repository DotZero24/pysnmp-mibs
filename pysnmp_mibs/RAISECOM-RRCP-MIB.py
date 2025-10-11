# SNMP MIB module (RAISECOM-RRCP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/raisecom/RAISECOM-RRCP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:37:35 2025
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

(rcRrcp,) = mibBuilder.importSymbols(
    "RAISECOM-RRCP-VLAN-MIB",
    "rcRrcp")

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
 MacAddress,
 PhysAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")

(EnableVar,) = mibBuilder.importSymbols(
    "SWITCH-TC",
    "EnableVar")


# MODULE-IDENTITY

rcRrcpProtocol = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 52, 1)
)
if mibBuilder.loadTexts:
    rcRrcpProtocol.setRevisions(
        ("2010-04-09 00:00",
         "2009-07-06 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RcRrcpMibNotifications_ObjectIdentity = ObjectIdentity
rcRrcpMibNotifications = _RcRrcpMibNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 52, 1, 1)
)
_RcRrcpMibObjects_ObjectIdentity = ObjectIdentity
rcRrcpMibObjects = _RcRrcpMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 52, 1, 2)
)
_RcRrcpGlobalGroup_ObjectIdentity = ObjectIdentity
rcRrcpGlobalGroup = _RcRrcpGlobalGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 52, 1, 2, 1)
)
_RcRrcpCurrentNumDevices_Type = Integer32
_RcRrcpCurrentNumDevices_Object = MibScalar
rcRrcpCurrentNumDevices = _RcRrcpCurrentNumDevices_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 52, 1, 2, 1, 1),
    _RcRrcpCurrentNumDevices_Type()
)
rcRrcpCurrentNumDevices.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcRrcpCurrentNumDevices.setStatus("current")
_RcRrcpNumDevices_Type = Integer32
_RcRrcpNumDevices_Object = MibScalar
rcRrcpNumDevices = _RcRrcpNumDevices_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 52, 1, 2, 1, 2),
    _RcRrcpNumDevices_Type()
)
rcRrcpNumDevices.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcRrcpNumDevices.setStatus("current")
_RcRrcpTrapEnable_Type = EnableVar
_RcRrcpTrapEnable_Object = MibScalar
rcRrcpTrapEnable = _RcRrcpTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 52, 1, 2, 1, 3),
    _RcRrcpTrapEnable_Type()
)
rcRrcpTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcRrcpTrapEnable.setStatus("current")


class _RcRrcpHelloTime_Type(Integer32):
    """Custom type rcRrcpHelloTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RcRrcpHelloTime_Type.__name__ = "Integer32"
_RcRrcpHelloTime_Object = MibScalar
rcRrcpHelloTime = _RcRrcpHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 52, 1, 2, 1, 4),
    _RcRrcpHelloTime_Type()
)
rcRrcpHelloTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcRrcpHelloTime.setStatus("current")
if mibBuilder.loadTexts:
    rcRrcpHelloTime.setUnits("minutes")
_RcRrcpDeviceUpdate_Type = TruthValue
_RcRrcpDeviceUpdate_Object = MibScalar
rcRrcpDeviceUpdate = _RcRrcpDeviceUpdate_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 52, 1, 2, 1, 5),
    _RcRrcpDeviceUpdate_Type()
)
rcRrcpDeviceUpdate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcRrcpDeviceUpdate.setStatus("current")
_RcRrcpStatsClear_Type = TruthValue
_RcRrcpStatsClear_Object = MibScalar
rcRrcpStatsClear = _RcRrcpStatsClear_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 52, 1, 2, 1, 6),
    _RcRrcpStatsClear_Type()
)
rcRrcpStatsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcRrcpStatsClear.setStatus("current")
_RcRrcpCopyGroup_ObjectIdentity = ObjectIdentity
rcRrcpCopyGroup = _RcRrcpCopyGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 52, 1, 2, 2)
)
_RcRrcpSourceDeviceId_Type = Integer32
_RcRrcpSourceDeviceId_Object = MibScalar
rcRrcpSourceDeviceId = _RcRrcpSourceDeviceId_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 52, 1, 2, 2, 1),
    _RcRrcpSourceDeviceId_Type()
)
rcRrcpSourceDeviceId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcRrcpSourceDeviceId.setStatus("current")
_RcRrcpDestinationDeviceList_Type = OctetString
_RcRrcpDestinationDeviceList_Object = MibScalar
rcRrcpDestinationDeviceList = _RcRrcpDestinationDeviceList_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 52, 1, 2, 2, 2),
    _RcRrcpDestinationDeviceList_Type()
)
rcRrcpDestinationDeviceList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcRrcpDestinationDeviceList.setStatus("current")


class _RcRrcpCopyStatus_Type(Integer32):
    """Custom type rcRrcpCopyStatus based on Integer32"""
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
        *(("start", 1),
          ("busy", 2),
          ("completed", 3),
          ("error", 4))
    )


_RcRrcpCopyStatus_Type.__name__ = "Integer32"
_RcRrcpCopyStatus_Object = MibScalar
rcRrcpCopyStatus = _RcRrcpCopyStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 52, 1, 2, 2, 3),
    _RcRrcpCopyStatus_Type()
)
rcRrcpCopyStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcRrcpCopyStatus.setStatus("current")
_RcRrcpCopyFailDeviceList_Type = OctetString
_RcRrcpCopyFailDeviceList_Object = MibScalar
rcRrcpCopyFailDeviceList = _RcRrcpCopyFailDeviceList_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 52, 1, 2, 2, 4),
    _RcRrcpCopyFailDeviceList_Type()
)
rcRrcpCopyFailDeviceList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcRrcpCopyFailDeviceList.setStatus("current")
_RcRrcpInterfaceTable_Object = MibTable
rcRrcpInterfaceTable = _RcRrcpInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 52, 1, 2, 3)
)
if mibBuilder.loadTexts:
    rcRrcpInterfaceTable.setStatus("current")
_RcRrcpInterfaceEntry_Object = MibTableRow
rcRrcpInterfaceEntry = _RcRrcpInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 52, 1, 2, 3, 1)
)
rcRrcpInterfaceEntry.setIndexNames(
    (0, "RAISECOM-RRCP-MIB", "rcRrcpInterfaceIndex"),
)
if mibBuilder.loadTexts:
    rcRrcpInterfaceEntry.setStatus("current")
_RcRrcpInterfaceIndex_Type = Integer32
_RcRrcpInterfaceIndex_Object = MibTableColumn
rcRrcpInterfaceIndex = _RcRrcpInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 52, 1, 2, 3, 1, 1),
    _RcRrcpInterfaceIndex_Type()
)
rcRrcpInterfaceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcRrcpInterfaceIndex.setStatus("current")


class _RcRrcpInterfaceDescription_Type(OctetString):
    """Custom type rcRrcpInterfaceDescription based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_RcRrcpInterfaceDescription_Type.__name__ = "OctetString"
_RcRrcpInterfaceDescription_Object = MibTableColumn
rcRrcpInterfaceDescription = _RcRrcpInterfaceDescription_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 52, 1, 2, 3, 1, 2),
    _RcRrcpInterfaceDescription_Type()
)
rcRrcpInterfaceDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcRrcpInterfaceDescription.setStatus("current")
_RcRrcpInterfaceEnable_Type = EnableVar
_RcRrcpInterfaceEnable_Object = MibTableColumn
rcRrcpInterfaceEnable = _RcRrcpInterfaceEnable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 52, 1, 2, 3, 1, 3),
    _RcRrcpInterfaceEnable_Type()
)
rcRrcpInterfaceEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcRrcpInterfaceEnable.setStatus("current")
_RcRrcpDeviceTable_Object = MibTable
rcRrcpDeviceTable = _RcRrcpDeviceTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 52, 1, 2, 4)
)
if mibBuilder.loadTexts:
    rcRrcpDeviceTable.setStatus("current")
_RcRrcpDeviceEntry_Object = MibTableRow
rcRrcpDeviceEntry = _RcRrcpDeviceEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 52, 1, 2, 4, 1)
)
rcRrcpDeviceEntry.setIndexNames(
    (0, "RAISECOM-RRCP-MIB", "rcRrcpInterfaceIndex"),
    (0, "RAISECOM-RRCP-MIB", "rcRrcpMacAddress"),
)
if mibBuilder.loadTexts:
    rcRrcpDeviceEntry.setStatus("current")
_RcRrcpMacAddress_Type = MacAddress
_RcRrcpMacAddress_Object = MibTableColumn
rcRrcpMacAddress = _RcRrcpMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 52, 1, 2, 4, 1, 1),
    _RcRrcpMacAddress_Type()
)
rcRrcpMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcRrcpMacAddress.setStatus("current")
_RcRrcpDeviceId_Type = Integer32
_RcRrcpDeviceId_Object = MibTableColumn
rcRrcpDeviceId = _RcRrcpDeviceId_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 52, 1, 2, 4, 1, 2),
    _RcRrcpDeviceId_Type()
)
rcRrcpDeviceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcRrcpDeviceId.setStatus("current")


class _RcRrcpDeviceType_Type(OctetString):
    """Custom type rcRrcpDeviceType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_RcRrcpDeviceType_Type.__name__ = "OctetString"
_RcRrcpDeviceType_Object = MibTableColumn
rcRrcpDeviceType = _RcRrcpDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 52, 1, 2, 4, 1, 3),
    _RcRrcpDeviceType_Type()
)
rcRrcpDeviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcRrcpDeviceType.setStatus("current")
_RcRrcpDownlinkPort_Type = Integer32
_RcRrcpDownlinkPort_Object = MibTableColumn
rcRrcpDownlinkPort = _RcRrcpDownlinkPort_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 52, 1, 2, 4, 1, 4),
    _RcRrcpDownlinkPort_Type()
)
rcRrcpDownlinkPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcRrcpDownlinkPort.setStatus("current")
_RcRrcpUplinkPort_Type = Integer32
_RcRrcpUplinkPort_Object = MibTableColumn
rcRrcpUplinkPort = _RcRrcpUplinkPort_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 52, 1, 2, 4, 1, 5),
    _RcRrcpUplinkPort_Type()
)
rcRrcpUplinkPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcRrcpUplinkPort.setStatus("current")
_RcRrcpUplinkMac_Type = MacAddress
_RcRrcpUplinkMac_Object = MibTableColumn
rcRrcpUplinkMac = _RcRrcpUplinkMac_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 52, 1, 2, 4, 1, 6),
    _RcRrcpUplinkMac_Type()
)
rcRrcpUplinkMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcRrcpUplinkMac.setStatus("current")
_RcRrcpSoftVersion_Type = Integer32
_RcRrcpSoftVersion_Object = MibTableColumn
rcRrcpSoftVersion = _RcRrcpSoftVersion_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 52, 1, 2, 4, 1, 7),
    _RcRrcpSoftVersion_Type()
)
rcRrcpSoftVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcRrcpSoftVersion.setStatus("current")
_RcRrcpStatsTable_Object = MibTable
rcRrcpStatsTable = _RcRrcpStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 52, 1, 2, 5)
)
if mibBuilder.loadTexts:
    rcRrcpStatsTable.setStatus("current")
_RcRrcpStatsEntry_Object = MibTableRow
rcRrcpStatsEntry = _RcRrcpStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 52, 1, 2, 5, 1)
)
rcRrcpStatsEntry.setIndexNames(
    (0, "RAISECOM-RRCP-MIB", "rcRrcpInterfaceIndex"),
)
if mibBuilder.loadTexts:
    rcRrcpStatsEntry.setStatus("current")
_RcRrcpHelloTx_Type = Counter32
_RcRrcpHelloTx_Object = MibTableColumn
rcRrcpHelloTx = _RcRrcpHelloTx_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 52, 1, 2, 5, 1, 1),
    _RcRrcpHelloTx_Type()
)
rcRrcpHelloTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcRrcpHelloTx.setStatus("current")
_RcRrcpGetTx_Type = Counter32
_RcRrcpGetTx_Object = MibTableColumn
rcRrcpGetTx = _RcRrcpGetTx_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 52, 1, 2, 5, 1, 2),
    _RcRrcpGetTx_Type()
)
rcRrcpGetTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcRrcpGetTx.setStatus("current")
_RcRrcpSetTx_Type = Counter32
_RcRrcpSetTx_Object = MibTableColumn
rcRrcpSetTx = _RcRrcpSetTx_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 52, 1, 2, 5, 1, 3),
    _RcRrcpSetTx_Type()
)
rcRrcpSetTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcRrcpSetTx.setStatus("current")
_RcRrcpGetReplyRx_Type = Counter32
_RcRrcpGetReplyRx_Object = MibTableColumn
rcRrcpGetReplyRx = _RcRrcpGetReplyRx_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 52, 1, 2, 5, 1, 4),
    _RcRrcpGetReplyRx_Type()
)
rcRrcpGetReplyRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcRrcpGetReplyRx.setStatus("current")
_RcRrcpHelloReplyRx_Type = Counter32
_RcRrcpHelloReplyRx_Object = MibTableColumn
rcRrcpHelloReplyRx = _RcRrcpHelloReplyRx_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 52, 1, 2, 5, 1, 5),
    _RcRrcpHelloReplyRx_Type()
)
rcRrcpHelloReplyRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcRrcpHelloReplyRx.setStatus("current")

# Managed Objects groups


# Notification objects

rcRrcpDeviceUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 52, 1, 1, 1)
)
rcRrcpDeviceUp.setObjects(
      *(("RAISECOM-RRCP-MIB", "rcRrcpInterfaceIndex"),
        ("RAISECOM-RRCP-MIB", "rcRrcpMacAddress"),
        ("RAISECOM-RRCP-MIB", "rcRrcpDeviceId"),
        ("RAISECOM-RRCP-MIB", "rcRrcpDeviceType"))
)
if mibBuilder.loadTexts:
    rcRrcpDeviceUp.setStatus(
        "current"
    )

rcRrcpDeviceDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 52, 1, 1, 2)
)
rcRrcpDeviceDown.setObjects(
      *(("RAISECOM-RRCP-MIB", "rcRrcpInterfaceIndex"),
        ("RAISECOM-RRCP-MIB", "rcRrcpMacAddress"),
        ("RAISECOM-RRCP-MIB", "rcRrcpDeviceId"),
        ("RAISECOM-RRCP-MIB", "rcRrcpDeviceType"))
)
if mibBuilder.loadTexts:
    rcRrcpDeviceDown.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RAISECOM-RRCP-MIB",
    **{"rcRrcpProtocol": rcRrcpProtocol,
       "rcRrcpMibNotifications": rcRrcpMibNotifications,
       "rcRrcpDeviceUp": rcRrcpDeviceUp,
       "rcRrcpDeviceDown": rcRrcpDeviceDown,
       "rcRrcpMibObjects": rcRrcpMibObjects,
       "rcRrcpGlobalGroup": rcRrcpGlobalGroup,
       "rcRrcpCurrentNumDevices": rcRrcpCurrentNumDevices,
       "rcRrcpNumDevices": rcRrcpNumDevices,
       "rcRrcpTrapEnable": rcRrcpTrapEnable,
       "rcRrcpHelloTime": rcRrcpHelloTime,
       "rcRrcpDeviceUpdate": rcRrcpDeviceUpdate,
       "rcRrcpStatsClear": rcRrcpStatsClear,
       "rcRrcpCopyGroup": rcRrcpCopyGroup,
       "rcRrcpSourceDeviceId": rcRrcpSourceDeviceId,
       "rcRrcpDestinationDeviceList": rcRrcpDestinationDeviceList,
       "rcRrcpCopyStatus": rcRrcpCopyStatus,
       "rcRrcpCopyFailDeviceList": rcRrcpCopyFailDeviceList,
       "rcRrcpInterfaceTable": rcRrcpInterfaceTable,
       "rcRrcpInterfaceEntry": rcRrcpInterfaceEntry,
       "rcRrcpInterfaceIndex": rcRrcpInterfaceIndex,
       "rcRrcpInterfaceDescription": rcRrcpInterfaceDescription,
       "rcRrcpInterfaceEnable": rcRrcpInterfaceEnable,
       "rcRrcpDeviceTable": rcRrcpDeviceTable,
       "rcRrcpDeviceEntry": rcRrcpDeviceEntry,
       "rcRrcpMacAddress": rcRrcpMacAddress,
       "rcRrcpDeviceId": rcRrcpDeviceId,
       "rcRrcpDeviceType": rcRrcpDeviceType,
       "rcRrcpDownlinkPort": rcRrcpDownlinkPort,
       "rcRrcpUplinkPort": rcRrcpUplinkPort,
       "rcRrcpUplinkMac": rcRrcpUplinkMac,
       "rcRrcpSoftVersion": rcRrcpSoftVersion,
       "rcRrcpStatsTable": rcRrcpStatsTable,
       "rcRrcpStatsEntry": rcRrcpStatsEntry,
       "rcRrcpHelloTx": rcRrcpHelloTx,
       "rcRrcpGetTx": rcRrcpGetTx,
       "rcRrcpSetTx": rcRrcpSetTx,
       "rcRrcpGetReplyRx": rcRrcpGetReplyRx,
       "rcRrcpHelloReplyRx": rcRrcpHelloReplyRx}
)
