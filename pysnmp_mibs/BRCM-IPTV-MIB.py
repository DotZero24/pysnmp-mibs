# SNMP MIB module (BRCM-IPTV-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/broadcom/BRCM-IPTV-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:07:47 2025
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

(cableDataMgmtMIBObjects,) = mibBuilder.importSymbols(
    "BRCM-CABLEDATA-MGMT-MIB",
    "cableDataMgmtMIBObjects")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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

brcmIptvMgmt = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1, 13)
)
if mibBuilder.loadTexts:
    brcmIptvMgmt.setRevisions(
        ("2009-08-22 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_IptvMgmtBase_ObjectIdentity = ObjectIdentity
iptvMgmtBase = _IptvMgmtBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1, 13, 1)
)
_BrcmIptvChannelInfo_ObjectIdentity = ObjectIdentity
brcmIptvChannelInfo = _BrcmIptvChannelInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1, 13, 1, 1)
)


class _BrcmIptvChannelTableDescr_Type(DisplayString):
    """Custom type brcmIptvChannelTableDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_BrcmIptvChannelTableDescr_Type.__name__ = "DisplayString"
_BrcmIptvChannelTableDescr_Object = MibScalar
brcmIptvChannelTableDescr = _BrcmIptvChannelTableDescr_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1, 13, 1, 1, 1),
    _BrcmIptvChannelTableDescr_Type()
)
brcmIptvChannelTableDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brcmIptvChannelTableDescr.setStatus("current")
_BrcmIptvChannelTableLastChange_Type = TimeTicks
_BrcmIptvChannelTableLastChange_Object = MibScalar
brcmIptvChannelTableLastChange = _BrcmIptvChannelTableLastChange_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1, 13, 1, 1, 2),
    _BrcmIptvChannelTableLastChange_Type()
)
brcmIptvChannelTableLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcmIptvChannelTableLastChange.setStatus("current")


class _BrcmIptvChannelTableNotificationInterval_Type(Integer32):
    """Custom type brcmIptvChannelTableNotificationInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_BrcmIptvChannelTableNotificationInterval_Type.__name__ = "Integer32"
_BrcmIptvChannelTableNotificationInterval_Object = MibScalar
brcmIptvChannelTableNotificationInterval = _BrcmIptvChannelTableNotificationInterval_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1, 13, 1, 1, 3),
    _BrcmIptvChannelTableNotificationInterval_Type()
)
brcmIptvChannelTableNotificationInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brcmIptvChannelTableNotificationInterval.setStatus("current")
if mibBuilder.loadTexts:
    brcmIptvChannelTableNotificationInterval.setUnits("seconds")
_BrcmIptvChannelTableNotifyNow_Type = TruthValue
_BrcmIptvChannelTableNotifyNow_Object = MibScalar
brcmIptvChannelTableNotifyNow = _BrcmIptvChannelTableNotifyNow_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1, 13, 1, 1, 4),
    _BrcmIptvChannelTableNotifyNow_Type()
)
brcmIptvChannelTableNotifyNow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brcmIptvChannelTableNotifyNow.setStatus("current")
_BrcmIptvChannelTable_Object = MibTable
brcmIptvChannelTable = _BrcmIptvChannelTable_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1, 13, 1, 1, 5)
)
if mibBuilder.loadTexts:
    brcmIptvChannelTable.setStatus("current")
_BrcmIptvChannelEntry_Object = MibTableRow
brcmIptvChannelEntry = _BrcmIptvChannelEntry_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1, 13, 1, 1, 5, 1)
)
brcmIptvChannelEntry.setIndexNames(
    (0, "BRCM-IPTV-MIB", "brcmIptvChanId"),
)
if mibBuilder.loadTexts:
    brcmIptvChannelEntry.setStatus("current")


class _BrcmIptvChanId_Type(Unsigned32):
    """Custom type brcmIptvChanId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BrcmIptvChanId_Type.__name__ = "Unsigned32"
_BrcmIptvChanId_Object = MibTableColumn
brcmIptvChanId = _BrcmIptvChanId_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1, 13, 1, 1, 5, 1, 1),
    _BrcmIptvChanId_Type()
)
brcmIptvChanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    brcmIptvChanId.setStatus("current")


class _BrcmIptvChanName_Type(DisplayString):
    """Custom type brcmIptvChanName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_BrcmIptvChanName_Type.__name__ = "DisplayString"
_BrcmIptvChanName_Object = MibTableColumn
brcmIptvChanName = _BrcmIptvChanName_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1, 13, 1, 1, 5, 1, 2),
    _BrcmIptvChanName_Type()
)
brcmIptvChanName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    brcmIptvChanName.setStatus("current")
_BrcmIptvChanFreq_Type = Unsigned32
_BrcmIptvChanFreq_Object = MibTableColumn
brcmIptvChanFreq = _BrcmIptvChanFreq_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1, 13, 1, 1, 5, 1, 3),
    _BrcmIptvChanFreq_Type()
)
brcmIptvChanFreq.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    brcmIptvChanFreq.setStatus("current")


class _BrcmIptvChanVideoPid_Type(Unsigned32):
    """Custom type brcmIptvChanVideoPid based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8191),
    )


_BrcmIptvChanVideoPid_Type.__name__ = "Unsigned32"
_BrcmIptvChanVideoPid_Object = MibTableColumn
brcmIptvChanVideoPid = _BrcmIptvChanVideoPid_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1, 13, 1, 1, 5, 1, 4),
    _BrcmIptvChanVideoPid_Type()
)
brcmIptvChanVideoPid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    brcmIptvChanVideoPid.setStatus("current")


class _BrcmIptvChanAudioPid_Type(Unsigned32):
    """Custom type brcmIptvChanAudioPid based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8191),
    )


_BrcmIptvChanAudioPid_Type.__name__ = "Unsigned32"
_BrcmIptvChanAudioPid_Object = MibTableColumn
brcmIptvChanAudioPid = _BrcmIptvChanAudioPid_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1, 13, 1, 1, 5, 1, 5),
    _BrcmIptvChanAudioPid_Type()
)
brcmIptvChanAudioPid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    brcmIptvChanAudioPid.setStatus("current")


class _BrcmIptvChanSecondaryAudioPid_Type(Unsigned32):
    """Custom type brcmIptvChanSecondaryAudioPid based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8191),
    )


_BrcmIptvChanSecondaryAudioPid_Type.__name__ = "Unsigned32"
_BrcmIptvChanSecondaryAudioPid_Object = MibTableColumn
brcmIptvChanSecondaryAudioPid = _BrcmIptvChanSecondaryAudioPid_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1, 13, 1, 1, 5, 1, 6),
    _BrcmIptvChanSecondaryAudioPid_Type()
)
brcmIptvChanSecondaryAudioPid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    brcmIptvChanSecondaryAudioPid.setStatus("current")


class _BrcmIptvChanPmtPid_Type(Unsigned32):
    """Custom type brcmIptvChanPmtPid based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8191),
    )


_BrcmIptvChanPmtPid_Type.__name__ = "Unsigned32"
_BrcmIptvChanPmtPid_Object = MibTableColumn
brcmIptvChanPmtPid = _BrcmIptvChanPmtPid_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1, 13, 1, 1, 5, 1, 7),
    _BrcmIptvChanPmtPid_Type()
)
brcmIptvChanPmtPid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    brcmIptvChanPmtPid.setStatus("current")
_BrcmIptvChanMcastGroupAddrType_Type = InetAddressType
_BrcmIptvChanMcastGroupAddrType_Object = MibTableColumn
brcmIptvChanMcastGroupAddrType = _BrcmIptvChanMcastGroupAddrType_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1, 13, 1, 1, 5, 1, 8),
    _BrcmIptvChanMcastGroupAddrType_Type()
)
brcmIptvChanMcastGroupAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    brcmIptvChanMcastGroupAddrType.setStatus("current")
_BrcmIptvChanMcastGroupAddr_Type = InetAddress
_BrcmIptvChanMcastGroupAddr_Object = MibTableColumn
brcmIptvChanMcastGroupAddr = _BrcmIptvChanMcastGroupAddr_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1, 13, 1, 1, 5, 1, 9),
    _BrcmIptvChanMcastGroupAddr_Type()
)
brcmIptvChanMcastGroupAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    brcmIptvChanMcastGroupAddr.setStatus("current")
_BrcmIptvChanPort_Type = Unsigned32
_BrcmIptvChanPort_Object = MibTableColumn
brcmIptvChanPort = _BrcmIptvChanPort_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1, 13, 1, 1, 5, 1, 10),
    _BrcmIptvChanPort_Type()
)
brcmIptvChanPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    brcmIptvChanPort.setStatus("current")
_BrcmIptvChanRowStatus_Type = RowStatus
_BrcmIptvChanRowStatus_Object = MibTableColumn
brcmIptvChanRowStatus = _BrcmIptvChanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1, 13, 1, 1, 5, 1, 11),
    _BrcmIptvChanRowStatus_Type()
)
brcmIptvChanRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    brcmIptvChanRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BRCM-IPTV-MIB",
    **{"brcmIptvMgmt": brcmIptvMgmt,
       "iptvMgmtBase": iptvMgmtBase,
       "brcmIptvChannelInfo": brcmIptvChannelInfo,
       "brcmIptvChannelTableDescr": brcmIptvChannelTableDescr,
       "brcmIptvChannelTableLastChange": brcmIptvChannelTableLastChange,
       "brcmIptvChannelTableNotificationInterval": brcmIptvChannelTableNotificationInterval,
       "brcmIptvChannelTableNotifyNow": brcmIptvChannelTableNotifyNow,
       "brcmIptvChannelTable": brcmIptvChannelTable,
       "brcmIptvChannelEntry": brcmIptvChannelEntry,
       "brcmIptvChanId": brcmIptvChanId,
       "brcmIptvChanName": brcmIptvChanName,
       "brcmIptvChanFreq": brcmIptvChanFreq,
       "brcmIptvChanVideoPid": brcmIptvChanVideoPid,
       "brcmIptvChanAudioPid": brcmIptvChanAudioPid,
       "brcmIptvChanSecondaryAudioPid": brcmIptvChanSecondaryAudioPid,
       "brcmIptvChanPmtPid": brcmIptvChanPmtPid,
       "brcmIptvChanMcastGroupAddrType": brcmIptvChanMcastGroupAddrType,
       "brcmIptvChanMcastGroupAddr": brcmIptvChanMcastGroupAddr,
       "brcmIptvChanPort": brcmIptvChanPort,
       "brcmIptvChanRowStatus": brcmIptvChanRowStatus}
)
