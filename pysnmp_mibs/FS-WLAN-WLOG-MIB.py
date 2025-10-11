# SNMP MIB module (FS-WLAN-WLOG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/fscom/FS-WLAN-WLOG-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:15:25 2025
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

fsWlanWlogMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 118)
)
if mibBuilder.loadTexts:
    fsWlanWlogMIB.setRevisions(
        ("2012-10-10 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FsWlanWlogNotificationsMIBObjects_ObjectIdentity = ObjectIdentity
fsWlanWlogNotificationsMIBObjects = _FsWlanWlogNotificationsMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 118, 1)
)
_FsWlanWlogNtfObjects_ObjectIdentity = ObjectIdentity
fsWlanWlogNtfObjects = _FsWlanWlogNtfObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 118, 1, 1)
)
_FsWlogNotifyApName_Type = DisplayString
_FsWlogNotifyApName_Object = MibScalar
fsWlogNotifyApName = _FsWlogNotifyApName_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 118, 1, 1, 1),
    _FsWlogNotifyApName_Type()
)
fsWlogNotifyApName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsWlogNotifyApName.setStatus("current")
_FsWlogNotifyApMac_Type = MacAddress
_FsWlogNotifyApMac_Object = MibScalar
fsWlogNotifyApMac = _FsWlogNotifyApMac_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 118, 1, 1, 2),
    _FsWlogNotifyApMac_Type()
)
fsWlogNotifyApMac.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsWlogNotifyApMac.setStatus("current")
_FsWlogNotifyApIp_Type = InetAddress
_FsWlogNotifyApIp_Object = MibScalar
fsWlogNotifyApIp = _FsWlogNotifyApIp_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 118, 1, 1, 3),
    _FsWlogNotifyApIp_Type()
)
fsWlogNotifyApIp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsWlogNotifyApIp.setStatus("current")
_FsWlogNotifyApCwDownId_Type = Integer32
_FsWlogNotifyApCwDownId_Object = MibScalar
fsWlogNotifyApCwDownId = _FsWlogNotifyApCwDownId_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 118, 1, 1, 4),
    _FsWlogNotifyApCwDownId_Type()
)
fsWlogNotifyApCwDownId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsWlogNotifyApCwDownId.setStatus("current")
_FsWlogNotifyApCwDownReason_Type = DisplayString
_FsWlogNotifyApCwDownReason_Object = MibScalar
fsWlogNotifyApCwDownReason = _FsWlogNotifyApCwDownReason_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 118, 1, 1, 5),
    _FsWlogNotifyApCwDownReason_Type()
)
fsWlogNotifyApCwDownReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsWlogNotifyApCwDownReason.setStatus("current")
_FsWlogNotifyApIntfStatTable_Object = MibTable
fsWlogNotifyApIntfStatTable = _FsWlogNotifyApIntfStatTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 118, 1, 1, 6)
)
if mibBuilder.loadTexts:
    fsWlogNotifyApIntfStatTable.setStatus("current")
_FsWlogNotifyApIntfStatEntry_Object = MibTableRow
fsWlogNotifyApIntfStatEntry = _FsWlogNotifyApIntfStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 118, 1, 1, 6, 1)
)
fsWlogNotifyApIntfStatEntry.setIndexNames(
    (0, "FS-WLAN-WLOG-MIB", "fsWlogNotifyApIntfName"),
)
if mibBuilder.loadTexts:
    fsWlogNotifyApIntfStatEntry.setStatus("current")
_FsWlogNotifyApIntfName_Type = DisplayString
_FsWlogNotifyApIntfName_Object = MibTableColumn
fsWlogNotifyApIntfName = _FsWlogNotifyApIntfName_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 118, 1, 1, 6, 1, 1),
    _FsWlogNotifyApIntfName_Type()
)
fsWlogNotifyApIntfName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsWlogNotifyApIntfName.setStatus("current")
_FsWlogNotifyApIntfInputRate_Type = Integer32
_FsWlogNotifyApIntfInputRate_Object = MibTableColumn
fsWlogNotifyApIntfInputRate = _FsWlogNotifyApIntfInputRate_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 118, 1, 1, 6, 1, 2),
    _FsWlogNotifyApIntfInputRate_Type()
)
fsWlogNotifyApIntfInputRate.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsWlogNotifyApIntfInputRate.setStatus("current")
_FsWlogNotifyApIntfOutputRate_Type = Integer32
_FsWlogNotifyApIntfOutputRate_Object = MibTableColumn
fsWlogNotifyApIntfOutputRate = _FsWlogNotifyApIntfOutputRate_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 118, 1, 1, 6, 1, 3),
    _FsWlogNotifyApIntfOutputRate_Type()
)
fsWlogNotifyApIntfOutputRate.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsWlogNotifyApIntfOutputRate.setStatus("current")
_FsWlogNotifyApIntfUnicastInputPkts_Type = Integer32
_FsWlogNotifyApIntfUnicastInputPkts_Object = MibTableColumn
fsWlogNotifyApIntfUnicastInputPkts = _FsWlogNotifyApIntfUnicastInputPkts_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 118, 1, 1, 6, 1, 4),
    _FsWlogNotifyApIntfUnicastInputPkts_Type()
)
fsWlogNotifyApIntfUnicastInputPkts.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsWlogNotifyApIntfUnicastInputPkts.setStatus("current")
_FsWlogNotifyApIntfUnicastOutputPkts_Type = Integer32
_FsWlogNotifyApIntfUnicastOutputPkts_Object = MibTableColumn
fsWlogNotifyApIntfUnicastOutputPkts = _FsWlogNotifyApIntfUnicastOutputPkts_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 118, 1, 1, 6, 1, 5),
    _FsWlogNotifyApIntfUnicastOutputPkts_Type()
)
fsWlogNotifyApIntfUnicastOutputPkts.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsWlogNotifyApIntfUnicastOutputPkts.setStatus("current")
_FsWlogNotifyApIntfMulticastInputPkts_Type = Integer32
_FsWlogNotifyApIntfMulticastInputPkts_Object = MibTableColumn
fsWlogNotifyApIntfMulticastInputPkts = _FsWlogNotifyApIntfMulticastInputPkts_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 118, 1, 1, 6, 1, 6),
    _FsWlogNotifyApIntfMulticastInputPkts_Type()
)
fsWlogNotifyApIntfMulticastInputPkts.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsWlogNotifyApIntfMulticastInputPkts.setStatus("current")
_FsWlogNotifyApIntfMulticastOutputPkts_Type = Integer32
_FsWlogNotifyApIntfMulticastOutputPkts_Object = MibTableColumn
fsWlogNotifyApIntfMulticastOutputPkts = _FsWlogNotifyApIntfMulticastOutputPkts_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 118, 1, 1, 6, 1, 7),
    _FsWlogNotifyApIntfMulticastOutputPkts_Type()
)
fsWlogNotifyApIntfMulticastOutputPkts.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsWlogNotifyApIntfMulticastOutputPkts.setStatus("current")
_FsWlogNotifyApIntfBroadcastInputPkts_Type = Integer32
_FsWlogNotifyApIntfBroadcastInputPkts_Object = MibTableColumn
fsWlogNotifyApIntfBroadcastInputPkts = _FsWlogNotifyApIntfBroadcastInputPkts_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 118, 1, 1, 6, 1, 8),
    _FsWlogNotifyApIntfBroadcastInputPkts_Type()
)
fsWlogNotifyApIntfBroadcastInputPkts.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsWlogNotifyApIntfBroadcastInputPkts.setStatus("current")
_FsWlogNotifyApIntfBroadcastOutputPkts_Type = Integer32
_FsWlogNotifyApIntfBroadcastOutputPkts_Object = MibTableColumn
fsWlogNotifyApIntfBroadcastOutputPkts = _FsWlogNotifyApIntfBroadcastOutputPkts_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 118, 1, 1, 6, 1, 9),
    _FsWlogNotifyApIntfBroadcastOutputPkts_Type()
)
fsWlogNotifyApIntfBroadcastOutputPkts.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsWlogNotifyApIntfBroadcastOutputPkts.setStatus("current")
_FsWlogNotifyApIntfErrorInputPkts_Type = Integer32
_FsWlogNotifyApIntfErrorInputPkts_Object = MibTableColumn
fsWlogNotifyApIntfErrorInputPkts = _FsWlogNotifyApIntfErrorInputPkts_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 118, 1, 1, 6, 1, 10),
    _FsWlogNotifyApIntfErrorInputPkts_Type()
)
fsWlogNotifyApIntfErrorInputPkts.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsWlogNotifyApIntfErrorInputPkts.setStatus("current")
_FsWlogNotifyApIntfErrorOutputPkts_Type = Integer32
_FsWlogNotifyApIntfErrorOutputPkts_Object = MibTableColumn
fsWlogNotifyApIntfErrorOutputPkts = _FsWlogNotifyApIntfErrorOutputPkts_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 118, 1, 1, 6, 1, 11),
    _FsWlogNotifyApIntfErrorOutputPkts_Type()
)
fsWlogNotifyApIntfErrorOutputPkts.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsWlogNotifyApIntfErrorOutputPkts.setStatus("current")
_FsWlogNotifyApRadioStatTable_Object = MibTable
fsWlogNotifyApRadioStatTable = _FsWlogNotifyApRadioStatTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 118, 1, 1, 7)
)
if mibBuilder.loadTexts:
    fsWlogNotifyApRadioStatTable.setStatus("current")
_FsWlogNotifyApRadioStatEntry_Object = MibTableRow
fsWlogNotifyApRadioStatEntry = _FsWlogNotifyApRadioStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 118, 1, 1, 7, 1)
)
fsWlogNotifyApRadioStatEntry.setIndexNames(
    (0, "FS-WLAN-WLOG-MIB", "fsWlogNotifyApRadioId"),
)
if mibBuilder.loadTexts:
    fsWlogNotifyApRadioStatEntry.setStatus("current")
_FsWlogNotifyApRadioId_Type = Integer32
_FsWlogNotifyApRadioId_Object = MibTableColumn
fsWlogNotifyApRadioId = _FsWlogNotifyApRadioId_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 118, 1, 1, 7, 1, 1),
    _FsWlogNotifyApRadioId_Type()
)
fsWlogNotifyApRadioId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsWlogNotifyApRadioId.setStatus("current")
_FsWlogNotifyApRadioWorkChnl_Type = Integer32
_FsWlogNotifyApRadioWorkChnl_Object = MibTableColumn
fsWlogNotifyApRadioWorkChnl = _FsWlogNotifyApRadioWorkChnl_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 118, 1, 1, 7, 1, 2),
    _FsWlogNotifyApRadioWorkChnl_Type()
)
fsWlogNotifyApRadioWorkChnl.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsWlogNotifyApRadioWorkChnl.setStatus("current")
_FsWlogNotifyApRadioPower_Type = Integer32
_FsWlogNotifyApRadioPower_Object = MibTableColumn
fsWlogNotifyApRadioPower = _FsWlogNotifyApRadioPower_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 118, 1, 1, 7, 1, 3),
    _FsWlogNotifyApRadioPower_Type()
)
fsWlogNotifyApRadioPower.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsWlogNotifyApRadioPower.setStatus("current")
_FsWlogNotifyApRadioRssi_Type = Integer32
_FsWlogNotifyApRadioRssi_Object = MibTableColumn
fsWlogNotifyApRadioRssi = _FsWlogNotifyApRadioRssi_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 118, 1, 1, 7, 1, 4),
    _FsWlogNotifyApRadioRssi_Type()
)
fsWlogNotifyApRadioRssi.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsWlogNotifyApRadioRssi.setStatus("current")
_FsWlogNotifyApRadioErrFrame_Type = Integer32
_FsWlogNotifyApRadioErrFrame_Object = MibTableColumn
fsWlogNotifyApRadioErrFrame = _FsWlogNotifyApRadioErrFrame_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 118, 1, 1, 7, 1, 5),
    _FsWlogNotifyApRadioErrFrame_Type()
)
fsWlogNotifyApRadioErrFrame.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsWlogNotifyApRadioErrFrame.setStatus("current")
_FsWlogNotifyApRadioRetrsmit_Type = Integer32
_FsWlogNotifyApRadioRetrsmit_Object = MibTableColumn
fsWlogNotifyApRadioRetrsmit = _FsWlogNotifyApRadioRetrsmit_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 118, 1, 1, 7, 1, 6),
    _FsWlogNotifyApRadioRetrsmit_Type()
)
fsWlogNotifyApRadioRetrsmit.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsWlogNotifyApRadioRetrsmit.setStatus("current")
_FsWlogNotifyApRadioTotalStaNum_Type = Integer32
_FsWlogNotifyApRadioTotalStaNum_Object = MibTableColumn
fsWlogNotifyApRadioTotalStaNum = _FsWlogNotifyApRadioTotalStaNum_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 118, 1, 1, 7, 1, 7),
    _FsWlogNotifyApRadioTotalStaNum_Type()
)
fsWlogNotifyApRadioTotalStaNum.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsWlogNotifyApRadioTotalStaNum.setStatus("current")
_FsWlogNotifyApRadioWebStaNum_Type = Integer32
_FsWlogNotifyApRadioWebStaNum_Object = MibTableColumn
fsWlogNotifyApRadioWebStaNum = _FsWlogNotifyApRadioWebStaNum_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 118, 1, 1, 7, 1, 8),
    _FsWlogNotifyApRadioWebStaNum_Type()
)
fsWlogNotifyApRadioWebStaNum.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsWlogNotifyApRadioWebStaNum.setStatus("current")
_FsWlogNotifyApRadioD1xStaNum_Type = Integer32
_FsWlogNotifyApRadioD1xStaNum_Object = MibTableColumn
fsWlogNotifyApRadioD1xStaNum = _FsWlogNotifyApRadioD1xStaNum_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 118, 1, 1, 7, 1, 9),
    _FsWlogNotifyApRadioD1xStaNum_Type()
)
fsWlogNotifyApRadioD1xStaNum.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsWlogNotifyApRadioD1xStaNum.setStatus("current")
_FsWlogNotifyStaMac_Type = MacAddress
_FsWlogNotifyStaMac_Object = MibScalar
fsWlogNotifyStaMac = _FsWlogNotifyStaMac_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 118, 1, 1, 8),
    _FsWlogNotifyStaMac_Type()
)
fsWlogNotifyStaMac.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsWlogNotifyStaMac.setStatus("current")
_FsWlogNotifyStaIp_Type = IpAddress
_FsWlogNotifyStaIp_Object = MibScalar
fsWlogNotifyStaIp = _FsWlogNotifyStaIp_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 118, 1, 1, 9),
    _FsWlogNotifyStaIp_Type()
)
fsWlogNotifyStaIp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsWlogNotifyStaIp.setStatus("current")
_FsWlogNotifyStaIpv6_Type = InetAddress
_FsWlogNotifyStaIpv6_Object = MibScalar
fsWlogNotifyStaIpv6 = _FsWlogNotifyStaIpv6_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 118, 1, 1, 10),
    _FsWlogNotifyStaIpv6_Type()
)
fsWlogNotifyStaIpv6.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsWlogNotifyStaIpv6.setStatus("current")
_FsWlogNotifySsid_Type = DisplayString
_FsWlogNotifySsid_Object = MibScalar
fsWlogNotifySsid = _FsWlogNotifySsid_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 118, 1, 1, 11),
    _FsWlogNotifySsid_Type()
)
fsWlogNotifySsid.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsWlogNotifySsid.setStatus("current")
_FsWlogNotifyStaRssi_Type = Integer32
_FsWlogNotifyStaRssi_Object = MibScalar
fsWlogNotifyStaRssi = _FsWlogNotifyStaRssi_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 118, 1, 1, 12),
    _FsWlogNotifyStaRssi_Type()
)
fsWlogNotifyStaRssi.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsWlogNotifyStaRssi.setStatus("current")
_FsWlogNotifyStaLinkrate_Type = Integer32
_FsWlogNotifyStaLinkrate_Object = MibScalar
fsWlogNotifyStaLinkrate = _FsWlogNotifyStaLinkrate_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 118, 1, 1, 13),
    _FsWlogNotifyStaLinkrate_Type()
)
fsWlogNotifyStaLinkrate.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsWlogNotifyStaLinkrate.setStatus("current")
_FsWlogNotifyStaOperType_Type = Integer32
_FsWlogNotifyStaOperType_Object = MibScalar
fsWlogNotifyStaOperType = _FsWlogNotifyStaOperType_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 118, 1, 1, 14),
    _FsWlogNotifyStaOperType_Type()
)
fsWlogNotifyStaOperType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsWlogNotifyStaOperType.setStatus("current")
_FsWlogNotifyStaAbnormalOperType_Type = Integer32
_FsWlogNotifyStaAbnormalOperType_Object = MibScalar
fsWlogNotifyStaAbnormalOperType = _FsWlogNotifyStaAbnormalOperType_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 118, 1, 1, 15),
    _FsWlogNotifyStaAbnormalOperType_Type()
)
fsWlogNotifyStaAbnormalOperType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsWlogNotifyStaAbnormalOperType.setStatus("current")
_FsWlogNotifyStaOperReason_Type = DisplayString
_FsWlogNotifyStaOperReason_Object = MibScalar
fsWlogNotifyStaOperReason = _FsWlogNotifyStaOperReason_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 118, 1, 1, 16),
    _FsWlogNotifyStaOperReason_Type()
)
fsWlogNotifyStaOperReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsWlogNotifyStaOperReason.setStatus("current")
_FsWlanWlogNotifications_ObjectIdentity = ObjectIdentity
fsWlanWlogNotifications = _FsWlanWlogNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 118, 1, 2)
)

# Managed Objects groups


# Notification objects

fsNotifyApCapwapDownReason = NotificationType(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 118, 1, 2, 1)
)
fsNotifyApCapwapDownReason.setObjects(
      *(("FS-WLAN-WLOG-MIB", "fsWlogNotifyApName"),
        ("FS-WLAN-WLOG-MIB", "fsWlogNotifyApMac"),
        ("FS-WLAN-WLOG-MIB", "fsWlogNotifyApIp"),
        ("FS-WLAN-WLOG-MIB", "fsWlogNotifyApCwDownId"),
        ("FS-WLAN-WLOG-MIB", "fsWlogNotifyApCwDownReason"))
)
if mibBuilder.loadTexts:
    fsNotifyApCapwapDownReason.setStatus(
        "current"
    )

fsNotifyApCapwapDownIntf = NotificationType(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 118, 1, 2, 2)
)
fsNotifyApCapwapDownIntf.setObjects(
      *(("FS-WLAN-WLOG-MIB", "fsWlogNotifyApName"),
        ("FS-WLAN-WLOG-MIB", "fsWlogNotifyApMac"),
        ("FS-WLAN-WLOG-MIB", "fsWlogNotifyApIp"),
        ("FS-WLAN-WLOG-MIB", "fsWlogNotifyApCwDownId"),
        ("FS-WLAN-WLOG-MIB", "fsWlogNotifyApIntfName"),
        ("FS-WLAN-WLOG-MIB", "fsWlogNotifyApIntfInputRate"),
        ("FS-WLAN-WLOG-MIB", "fsWlogNotifyApIntfOutputRate"),
        ("FS-WLAN-WLOG-MIB", "fsWlogNotifyApIntfUnicastInputPkts"),
        ("FS-WLAN-WLOG-MIB", "fsWlogNotifyApIntfUnicastOutputPkts"),
        ("FS-WLAN-WLOG-MIB", "fsWlogNotifyApIntfMulticastInputPkts"),
        ("FS-WLAN-WLOG-MIB", "fsWlogNotifyApIntfMulticastOutputPkts"),
        ("FS-WLAN-WLOG-MIB", "fsWlogNotifyApIntfBroadcastInputPkts"),
        ("FS-WLAN-WLOG-MIB", "fsWlogNotifyApIntfBroadcastOutputPkts"),
        ("FS-WLAN-WLOG-MIB", "fsWlogNotifyApIntfErrorInputPkts"),
        ("FS-WLAN-WLOG-MIB", "fsWlogNotifyApIntfErrorOutputPkts"))
)
if mibBuilder.loadTexts:
    fsNotifyApCapwapDownIntf.setStatus(
        "current"
    )

fsNotifyApCapwapDownRadio = NotificationType(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 118, 1, 2, 3)
)
fsNotifyApCapwapDownRadio.setObjects(
      *(("FS-WLAN-WLOG-MIB", "fsWlogNotifyApName"),
        ("FS-WLAN-WLOG-MIB", "fsWlogNotifyApMac"),
        ("FS-WLAN-WLOG-MIB", "fsWlogNotifyApIp"),
        ("FS-WLAN-WLOG-MIB", "fsWlogNotifyApCwDownId"),
        ("FS-WLAN-WLOG-MIB", "fsWlogNotifyApRadioId"),
        ("FS-WLAN-WLOG-MIB", "fsWlogNotifyApRadioWorkChnl"),
        ("FS-WLAN-WLOG-MIB", "fsWlogNotifyApRadioPower"),
        ("FS-WLAN-WLOG-MIB", "fsWlogNotifyApRadioRssi"),
        ("FS-WLAN-WLOG-MIB", "fsWlogNotifyApRadioErrFrame"),
        ("FS-WLAN-WLOG-MIB", "fsWlogNotifyApRadioRetrsmit"),
        ("FS-WLAN-WLOG-MIB", "fsWlogNotifyApRadioTotalStaNum"),
        ("FS-WLAN-WLOG-MIB", "fsWlogNotifyApRadioWebStaNum"),
        ("FS-WLAN-WLOG-MIB", "fsWlogNotifyApRadioD1xStaNum"))
)
if mibBuilder.loadTexts:
    fsNotifyApCapwapDownRadio.setStatus(
        "current"
    )

fsNotifyStaOper = NotificationType(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 118, 1, 2, 4)
)
fsNotifyStaOper.setObjects(
      *(("FS-WLAN-WLOG-MIB", "fsWlogNotifyStaMac"),
        ("FS-WLAN-WLOG-MIB", "fsWlogNotifyStaIp"),
        ("FS-WLAN-WLOG-MIB", "fsWlogNotifyStaIpv6"),
        ("FS-WLAN-WLOG-MIB", "fsWlogNotifyStaRssi"),
        ("FS-WLAN-WLOG-MIB", "fsWlogNotifyStaLinkrate"),
        ("FS-WLAN-WLOG-MIB", "fsWlogNotifyApName"),
        ("FS-WLAN-WLOG-MIB", "fsWlogNotifySsid"),
        ("FS-WLAN-WLOG-MIB", "fsWlogNotifyStaOperType"))
)
if mibBuilder.loadTexts:
    fsNotifyStaOper.setStatus(
        "current"
    )

fsNotifyStaAbnormalOper = NotificationType(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 118, 1, 2, 5)
)
fsNotifyStaAbnormalOper.setObjects(
      *(("FS-WLAN-WLOG-MIB", "fsWlogNotifyStaMac"),
        ("FS-WLAN-WLOG-MIB", "fsWlogNotifyStaIp"),
        ("FS-WLAN-WLOG-MIB", "fsWlogNotifyStaIpv6"),
        ("FS-WLAN-WLOG-MIB", "fsWlogNotifyStaAbnormalOperType"),
        ("FS-WLAN-WLOG-MIB", "fsWlogNotifyStaOperReason"))
)
if mibBuilder.loadTexts:
    fsNotifyStaAbnormalOper.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FS-WLAN-WLOG-MIB",
    **{"fsWlanWlogMIB": fsWlanWlogMIB,
       "fsWlanWlogNotificationsMIBObjects": fsWlanWlogNotificationsMIBObjects,
       "fsWlanWlogNtfObjects": fsWlanWlogNtfObjects,
       "fsWlogNotifyApName": fsWlogNotifyApName,
       "fsWlogNotifyApMac": fsWlogNotifyApMac,
       "fsWlogNotifyApIp": fsWlogNotifyApIp,
       "fsWlogNotifyApCwDownId": fsWlogNotifyApCwDownId,
       "fsWlogNotifyApCwDownReason": fsWlogNotifyApCwDownReason,
       "fsWlogNotifyApIntfStatTable": fsWlogNotifyApIntfStatTable,
       "fsWlogNotifyApIntfStatEntry": fsWlogNotifyApIntfStatEntry,
       "fsWlogNotifyApIntfName": fsWlogNotifyApIntfName,
       "fsWlogNotifyApIntfInputRate": fsWlogNotifyApIntfInputRate,
       "fsWlogNotifyApIntfOutputRate": fsWlogNotifyApIntfOutputRate,
       "fsWlogNotifyApIntfUnicastInputPkts": fsWlogNotifyApIntfUnicastInputPkts,
       "fsWlogNotifyApIntfUnicastOutputPkts": fsWlogNotifyApIntfUnicastOutputPkts,
       "fsWlogNotifyApIntfMulticastInputPkts": fsWlogNotifyApIntfMulticastInputPkts,
       "fsWlogNotifyApIntfMulticastOutputPkts": fsWlogNotifyApIntfMulticastOutputPkts,
       "fsWlogNotifyApIntfBroadcastInputPkts": fsWlogNotifyApIntfBroadcastInputPkts,
       "fsWlogNotifyApIntfBroadcastOutputPkts": fsWlogNotifyApIntfBroadcastOutputPkts,
       "fsWlogNotifyApIntfErrorInputPkts": fsWlogNotifyApIntfErrorInputPkts,
       "fsWlogNotifyApIntfErrorOutputPkts": fsWlogNotifyApIntfErrorOutputPkts,
       "fsWlogNotifyApRadioStatTable": fsWlogNotifyApRadioStatTable,
       "fsWlogNotifyApRadioStatEntry": fsWlogNotifyApRadioStatEntry,
       "fsWlogNotifyApRadioId": fsWlogNotifyApRadioId,
       "fsWlogNotifyApRadioWorkChnl": fsWlogNotifyApRadioWorkChnl,
       "fsWlogNotifyApRadioPower": fsWlogNotifyApRadioPower,
       "fsWlogNotifyApRadioRssi": fsWlogNotifyApRadioRssi,
       "fsWlogNotifyApRadioErrFrame": fsWlogNotifyApRadioErrFrame,
       "fsWlogNotifyApRadioRetrsmit": fsWlogNotifyApRadioRetrsmit,
       "fsWlogNotifyApRadioTotalStaNum": fsWlogNotifyApRadioTotalStaNum,
       "fsWlogNotifyApRadioWebStaNum": fsWlogNotifyApRadioWebStaNum,
       "fsWlogNotifyApRadioD1xStaNum": fsWlogNotifyApRadioD1xStaNum,
       "fsWlogNotifyStaMac": fsWlogNotifyStaMac,
       "fsWlogNotifyStaIp": fsWlogNotifyStaIp,
       "fsWlogNotifyStaIpv6": fsWlogNotifyStaIpv6,
       "fsWlogNotifySsid": fsWlogNotifySsid,
       "fsWlogNotifyStaRssi": fsWlogNotifyStaRssi,
       "fsWlogNotifyStaLinkrate": fsWlogNotifyStaLinkrate,
       "fsWlogNotifyStaOperType": fsWlogNotifyStaOperType,
       "fsWlogNotifyStaAbnormalOperType": fsWlogNotifyStaAbnormalOperType,
       "fsWlogNotifyStaOperReason": fsWlogNotifyStaOperReason,
       "fsWlanWlogNotifications": fsWlanWlogNotifications,
       "fsNotifyApCapwapDownReason": fsNotifyApCapwapDownReason,
       "fsNotifyApCapwapDownIntf": fsNotifyApCapwapDownIntf,
       "fsNotifyApCapwapDownRadio": fsNotifyApCapwapDownRadio,
       "fsNotifyStaOper": fsNotifyStaOper,
       "fsNotifyStaAbnormalOper": fsNotifyStaAbnormalOper}
)
