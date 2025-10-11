# SNMP MIB module (QTECH-WLAN-WLOG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/qtech/QTECH-WLAN-WLOG-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:59:37 2025
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

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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
 MacAddress,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

qtechWlanWlogMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 118)
)
if mibBuilder.loadTexts:
    qtechWlanWlogMIB.setRevisions(
        ("2012-10-10 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_QtechWlanWlogNotificationsMIBObjects_ObjectIdentity = ObjectIdentity
qtechWlanWlogNotificationsMIBObjects = _QtechWlanWlogNotificationsMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 118, 1)
)
_QtechWlanWlogNtfObjects_ObjectIdentity = ObjectIdentity
qtechWlanWlogNtfObjects = _QtechWlanWlogNtfObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 118, 1, 1)
)
_QtechWlogNotifyApName_Type = DisplayString
_QtechWlogNotifyApName_Object = MibScalar
qtechWlogNotifyApName = _QtechWlogNotifyApName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 118, 1, 1, 1),
    _QtechWlogNotifyApName_Type()
)
qtechWlogNotifyApName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    qtechWlogNotifyApName.setStatus("current")
_QtechWlogNotifyApMac_Type = MacAddress
_QtechWlogNotifyApMac_Object = MibScalar
qtechWlogNotifyApMac = _QtechWlogNotifyApMac_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 118, 1, 1, 2),
    _QtechWlogNotifyApMac_Type()
)
qtechWlogNotifyApMac.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    qtechWlogNotifyApMac.setStatus("current")
_QtechWlogNotifyApIp_Type = InetAddress
_QtechWlogNotifyApIp_Object = MibScalar
qtechWlogNotifyApIp = _QtechWlogNotifyApIp_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 118, 1, 1, 3),
    _QtechWlogNotifyApIp_Type()
)
qtechWlogNotifyApIp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    qtechWlogNotifyApIp.setStatus("current")
_QtechWlogNotifyApCwDownId_Type = Integer32
_QtechWlogNotifyApCwDownId_Object = MibScalar
qtechWlogNotifyApCwDownId = _QtechWlogNotifyApCwDownId_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 118, 1, 1, 4),
    _QtechWlogNotifyApCwDownId_Type()
)
qtechWlogNotifyApCwDownId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    qtechWlogNotifyApCwDownId.setStatus("current")
_QtechWlogNotifyApCwDownReason_Type = DisplayString
_QtechWlogNotifyApCwDownReason_Object = MibScalar
qtechWlogNotifyApCwDownReason = _QtechWlogNotifyApCwDownReason_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 118, 1, 1, 5),
    _QtechWlogNotifyApCwDownReason_Type()
)
qtechWlogNotifyApCwDownReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    qtechWlogNotifyApCwDownReason.setStatus("current")
_QtechWlogNotifyApIntfStatTable_Object = MibTable
qtechWlogNotifyApIntfStatTable = _QtechWlogNotifyApIntfStatTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 118, 1, 1, 6)
)
if mibBuilder.loadTexts:
    qtechWlogNotifyApIntfStatTable.setStatus("current")
_QtechWlogNotifyApIntfStatEntry_Object = MibTableRow
qtechWlogNotifyApIntfStatEntry = _QtechWlogNotifyApIntfStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 118, 1, 1, 6, 1)
)
qtechWlogNotifyApIntfStatEntry.setIndexNames(
    (0, "QTECH-WLAN-WLOG-MIB", "qtechWlogNotifyApIntfName"),
)
if mibBuilder.loadTexts:
    qtechWlogNotifyApIntfStatEntry.setStatus("current")
_QtechWlogNotifyApIntfName_Type = DisplayString
_QtechWlogNotifyApIntfName_Object = MibTableColumn
qtechWlogNotifyApIntfName = _QtechWlogNotifyApIntfName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 118, 1, 1, 6, 1, 1),
    _QtechWlogNotifyApIntfName_Type()
)
qtechWlogNotifyApIntfName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    qtechWlogNotifyApIntfName.setStatus("current")
_QtechWlogNotifyApIntfInputRate_Type = Integer32
_QtechWlogNotifyApIntfInputRate_Object = MibTableColumn
qtechWlogNotifyApIntfInputRate = _QtechWlogNotifyApIntfInputRate_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 118, 1, 1, 6, 1, 2),
    _QtechWlogNotifyApIntfInputRate_Type()
)
qtechWlogNotifyApIntfInputRate.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    qtechWlogNotifyApIntfInputRate.setStatus("current")
_QtechWlogNotifyApIntfOutputRate_Type = Integer32
_QtechWlogNotifyApIntfOutputRate_Object = MibTableColumn
qtechWlogNotifyApIntfOutputRate = _QtechWlogNotifyApIntfOutputRate_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 118, 1, 1, 6, 1, 3),
    _QtechWlogNotifyApIntfOutputRate_Type()
)
qtechWlogNotifyApIntfOutputRate.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    qtechWlogNotifyApIntfOutputRate.setStatus("current")
_QtechWlogNotifyApIntfUnicastInputPkts_Type = Integer32
_QtechWlogNotifyApIntfUnicastInputPkts_Object = MibTableColumn
qtechWlogNotifyApIntfUnicastInputPkts = _QtechWlogNotifyApIntfUnicastInputPkts_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 118, 1, 1, 6, 1, 4),
    _QtechWlogNotifyApIntfUnicastInputPkts_Type()
)
qtechWlogNotifyApIntfUnicastInputPkts.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    qtechWlogNotifyApIntfUnicastInputPkts.setStatus("current")
_QtechWlogNotifyApIntfUnicastOutputPkts_Type = Integer32
_QtechWlogNotifyApIntfUnicastOutputPkts_Object = MibTableColumn
qtechWlogNotifyApIntfUnicastOutputPkts = _QtechWlogNotifyApIntfUnicastOutputPkts_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 118, 1, 1, 6, 1, 5),
    _QtechWlogNotifyApIntfUnicastOutputPkts_Type()
)
qtechWlogNotifyApIntfUnicastOutputPkts.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    qtechWlogNotifyApIntfUnicastOutputPkts.setStatus("current")
_QtechWlogNotifyApIntfMulticastInputPkts_Type = Integer32
_QtechWlogNotifyApIntfMulticastInputPkts_Object = MibTableColumn
qtechWlogNotifyApIntfMulticastInputPkts = _QtechWlogNotifyApIntfMulticastInputPkts_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 118, 1, 1, 6, 1, 6),
    _QtechWlogNotifyApIntfMulticastInputPkts_Type()
)
qtechWlogNotifyApIntfMulticastInputPkts.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    qtechWlogNotifyApIntfMulticastInputPkts.setStatus("current")
_QtechWlogNotifyApIntfMulticastOutputPkts_Type = Integer32
_QtechWlogNotifyApIntfMulticastOutputPkts_Object = MibTableColumn
qtechWlogNotifyApIntfMulticastOutputPkts = _QtechWlogNotifyApIntfMulticastOutputPkts_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 118, 1, 1, 6, 1, 7),
    _QtechWlogNotifyApIntfMulticastOutputPkts_Type()
)
qtechWlogNotifyApIntfMulticastOutputPkts.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    qtechWlogNotifyApIntfMulticastOutputPkts.setStatus("current")
_QtechWlogNotifyApIntfBroadcastInputPkts_Type = Integer32
_QtechWlogNotifyApIntfBroadcastInputPkts_Object = MibTableColumn
qtechWlogNotifyApIntfBroadcastInputPkts = _QtechWlogNotifyApIntfBroadcastInputPkts_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 118, 1, 1, 6, 1, 8),
    _QtechWlogNotifyApIntfBroadcastInputPkts_Type()
)
qtechWlogNotifyApIntfBroadcastInputPkts.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    qtechWlogNotifyApIntfBroadcastInputPkts.setStatus("current")
_QtechWlogNotifyApIntfBroadcastOutputPkts_Type = Integer32
_QtechWlogNotifyApIntfBroadcastOutputPkts_Object = MibTableColumn
qtechWlogNotifyApIntfBroadcastOutputPkts = _QtechWlogNotifyApIntfBroadcastOutputPkts_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 118, 1, 1, 6, 1, 9),
    _QtechWlogNotifyApIntfBroadcastOutputPkts_Type()
)
qtechWlogNotifyApIntfBroadcastOutputPkts.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    qtechWlogNotifyApIntfBroadcastOutputPkts.setStatus("current")
_QtechWlogNotifyApIntfErrorInputPkts_Type = Integer32
_QtechWlogNotifyApIntfErrorInputPkts_Object = MibTableColumn
qtechWlogNotifyApIntfErrorInputPkts = _QtechWlogNotifyApIntfErrorInputPkts_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 118, 1, 1, 6, 1, 10),
    _QtechWlogNotifyApIntfErrorInputPkts_Type()
)
qtechWlogNotifyApIntfErrorInputPkts.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    qtechWlogNotifyApIntfErrorInputPkts.setStatus("current")
_QtechWlogNotifyApIntfErrorOutputPkts_Type = Integer32
_QtechWlogNotifyApIntfErrorOutputPkts_Object = MibTableColumn
qtechWlogNotifyApIntfErrorOutputPkts = _QtechWlogNotifyApIntfErrorOutputPkts_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 118, 1, 1, 6, 1, 11),
    _QtechWlogNotifyApIntfErrorOutputPkts_Type()
)
qtechWlogNotifyApIntfErrorOutputPkts.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    qtechWlogNotifyApIntfErrorOutputPkts.setStatus("current")
_QtechWlogNotifyApRadioStatTable_Object = MibTable
qtechWlogNotifyApRadioStatTable = _QtechWlogNotifyApRadioStatTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 118, 1, 1, 7)
)
if mibBuilder.loadTexts:
    qtechWlogNotifyApRadioStatTable.setStatus("current")
_QtechWlogNotifyApRadioStatEntry_Object = MibTableRow
qtechWlogNotifyApRadioStatEntry = _QtechWlogNotifyApRadioStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 118, 1, 1, 7, 1)
)
qtechWlogNotifyApRadioStatEntry.setIndexNames(
    (0, "QTECH-WLAN-WLOG-MIB", "qtechWlogNotifyApRadioId"),
)
if mibBuilder.loadTexts:
    qtechWlogNotifyApRadioStatEntry.setStatus("current")
_QtechWlogNotifyApRadioId_Type = Integer32
_QtechWlogNotifyApRadioId_Object = MibTableColumn
qtechWlogNotifyApRadioId = _QtechWlogNotifyApRadioId_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 118, 1, 1, 7, 1, 1),
    _QtechWlogNotifyApRadioId_Type()
)
qtechWlogNotifyApRadioId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    qtechWlogNotifyApRadioId.setStatus("current")
_QtechWlogNotifyApRadioWorkChnl_Type = Integer32
_QtechWlogNotifyApRadioWorkChnl_Object = MibTableColumn
qtechWlogNotifyApRadioWorkChnl = _QtechWlogNotifyApRadioWorkChnl_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 118, 1, 1, 7, 1, 2),
    _QtechWlogNotifyApRadioWorkChnl_Type()
)
qtechWlogNotifyApRadioWorkChnl.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    qtechWlogNotifyApRadioWorkChnl.setStatus("current")
_QtechWlogNotifyApRadioPower_Type = Integer32
_QtechWlogNotifyApRadioPower_Object = MibTableColumn
qtechWlogNotifyApRadioPower = _QtechWlogNotifyApRadioPower_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 118, 1, 1, 7, 1, 3),
    _QtechWlogNotifyApRadioPower_Type()
)
qtechWlogNotifyApRadioPower.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    qtechWlogNotifyApRadioPower.setStatus("current")
_QtechWlogNotifyApRadioRssi_Type = Integer32
_QtechWlogNotifyApRadioRssi_Object = MibTableColumn
qtechWlogNotifyApRadioRssi = _QtechWlogNotifyApRadioRssi_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 118, 1, 1, 7, 1, 4),
    _QtechWlogNotifyApRadioRssi_Type()
)
qtechWlogNotifyApRadioRssi.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    qtechWlogNotifyApRadioRssi.setStatus("current")
_QtechWlogNotifyApRadioErrFrame_Type = Integer32
_QtechWlogNotifyApRadioErrFrame_Object = MibTableColumn
qtechWlogNotifyApRadioErrFrame = _QtechWlogNotifyApRadioErrFrame_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 118, 1, 1, 7, 1, 5),
    _QtechWlogNotifyApRadioErrFrame_Type()
)
qtechWlogNotifyApRadioErrFrame.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    qtechWlogNotifyApRadioErrFrame.setStatus("current")
_QtechWlogNotifyApRadioRetrsmit_Type = Integer32
_QtechWlogNotifyApRadioRetrsmit_Object = MibTableColumn
qtechWlogNotifyApRadioRetrsmit = _QtechWlogNotifyApRadioRetrsmit_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 118, 1, 1, 7, 1, 6),
    _QtechWlogNotifyApRadioRetrsmit_Type()
)
qtechWlogNotifyApRadioRetrsmit.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    qtechWlogNotifyApRadioRetrsmit.setStatus("current")
_QtechWlogNotifyApRadioTotalStaNum_Type = Integer32
_QtechWlogNotifyApRadioTotalStaNum_Object = MibTableColumn
qtechWlogNotifyApRadioTotalStaNum = _QtechWlogNotifyApRadioTotalStaNum_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 118, 1, 1, 7, 1, 7),
    _QtechWlogNotifyApRadioTotalStaNum_Type()
)
qtechWlogNotifyApRadioTotalStaNum.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    qtechWlogNotifyApRadioTotalStaNum.setStatus("current")
_QtechWlogNotifyApRadioWebStaNum_Type = Integer32
_QtechWlogNotifyApRadioWebStaNum_Object = MibTableColumn
qtechWlogNotifyApRadioWebStaNum = _QtechWlogNotifyApRadioWebStaNum_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 118, 1, 1, 7, 1, 8),
    _QtechWlogNotifyApRadioWebStaNum_Type()
)
qtechWlogNotifyApRadioWebStaNum.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    qtechWlogNotifyApRadioWebStaNum.setStatus("current")
_QtechWlogNotifyApRadioD1xStaNum_Type = Integer32
_QtechWlogNotifyApRadioD1xStaNum_Object = MibTableColumn
qtechWlogNotifyApRadioD1xStaNum = _QtechWlogNotifyApRadioD1xStaNum_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 118, 1, 1, 7, 1, 9),
    _QtechWlogNotifyApRadioD1xStaNum_Type()
)
qtechWlogNotifyApRadioD1xStaNum.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    qtechWlogNotifyApRadioD1xStaNum.setStatus("current")
_QtechWlogNotifyStaMac_Type = MacAddress
_QtechWlogNotifyStaMac_Object = MibScalar
qtechWlogNotifyStaMac = _QtechWlogNotifyStaMac_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 118, 1, 1, 8),
    _QtechWlogNotifyStaMac_Type()
)
qtechWlogNotifyStaMac.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    qtechWlogNotifyStaMac.setStatus("current")
_QtechWlogNotifyStaIp_Type = IpAddress
_QtechWlogNotifyStaIp_Object = MibScalar
qtechWlogNotifyStaIp = _QtechWlogNotifyStaIp_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 118, 1, 1, 9),
    _QtechWlogNotifyStaIp_Type()
)
qtechWlogNotifyStaIp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    qtechWlogNotifyStaIp.setStatus("current")
_QtechWlogNotifyStaIpv6_Type = InetAddress
_QtechWlogNotifyStaIpv6_Object = MibScalar
qtechWlogNotifyStaIpv6 = _QtechWlogNotifyStaIpv6_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 118, 1, 1, 10),
    _QtechWlogNotifyStaIpv6_Type()
)
qtechWlogNotifyStaIpv6.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    qtechWlogNotifyStaIpv6.setStatus("current")
_QtechWlogNotifySsid_Type = DisplayString
_QtechWlogNotifySsid_Object = MibScalar
qtechWlogNotifySsid = _QtechWlogNotifySsid_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 118, 1, 1, 11),
    _QtechWlogNotifySsid_Type()
)
qtechWlogNotifySsid.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    qtechWlogNotifySsid.setStatus("current")
_QtechWlogNotifyStaRssi_Type = Integer32
_QtechWlogNotifyStaRssi_Object = MibScalar
qtechWlogNotifyStaRssi = _QtechWlogNotifyStaRssi_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 118, 1, 1, 12),
    _QtechWlogNotifyStaRssi_Type()
)
qtechWlogNotifyStaRssi.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    qtechWlogNotifyStaRssi.setStatus("current")
_QtechWlogNotifyStaLinkrate_Type = Integer32
_QtechWlogNotifyStaLinkrate_Object = MibScalar
qtechWlogNotifyStaLinkrate = _QtechWlogNotifyStaLinkrate_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 118, 1, 1, 13),
    _QtechWlogNotifyStaLinkrate_Type()
)
qtechWlogNotifyStaLinkrate.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    qtechWlogNotifyStaLinkrate.setStatus("current")
_QtechWlogNotifyStaOperType_Type = Integer32
_QtechWlogNotifyStaOperType_Object = MibScalar
qtechWlogNotifyStaOperType = _QtechWlogNotifyStaOperType_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 118, 1, 1, 14),
    _QtechWlogNotifyStaOperType_Type()
)
qtechWlogNotifyStaOperType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    qtechWlogNotifyStaOperType.setStatus("current")
_QtechWlogNotifyStaAbnormalOperType_Type = Integer32
_QtechWlogNotifyStaAbnormalOperType_Object = MibScalar
qtechWlogNotifyStaAbnormalOperType = _QtechWlogNotifyStaAbnormalOperType_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 118, 1, 1, 15),
    _QtechWlogNotifyStaAbnormalOperType_Type()
)
qtechWlogNotifyStaAbnormalOperType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    qtechWlogNotifyStaAbnormalOperType.setStatus("current")
_QtechWlogNotifyStaOperReason_Type = DisplayString
_QtechWlogNotifyStaOperReason_Object = MibScalar
qtechWlogNotifyStaOperReason = _QtechWlogNotifyStaOperReason_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 118, 1, 1, 16),
    _QtechWlogNotifyStaOperReason_Type()
)
qtechWlogNotifyStaOperReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    qtechWlogNotifyStaOperReason.setStatus("current")
_QtechWlanWlogNotifications_ObjectIdentity = ObjectIdentity
qtechWlanWlogNotifications = _QtechWlanWlogNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 118, 1, 2)
)

# Managed Objects groups


# Notification objects

qtechNotifyApCapwapDownReason = NotificationType(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 118, 1, 2, 1)
)
qtechNotifyApCapwapDownReason.setObjects(
      *(("QTECH-WLAN-WLOG-MIB", "qtechWlogNotifyApName"),
        ("QTECH-WLAN-WLOG-MIB", "qtechWlogNotifyApMac"),
        ("QTECH-WLAN-WLOG-MIB", "qtechWlogNotifyApIp"),
        ("QTECH-WLAN-WLOG-MIB", "qtechWlogNotifyApCwDownId"),
        ("QTECH-WLAN-WLOG-MIB", "qtechWlogNotifyApCwDownReason"))
)
if mibBuilder.loadTexts:
    qtechNotifyApCapwapDownReason.setStatus(
        "current"
    )

qtechNotifyApCapwapDownIntf = NotificationType(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 118, 1, 2, 2)
)
qtechNotifyApCapwapDownIntf.setObjects(
      *(("QTECH-WLAN-WLOG-MIB", "qtechWlogNotifyApName"),
        ("QTECH-WLAN-WLOG-MIB", "qtechWlogNotifyApMac"),
        ("QTECH-WLAN-WLOG-MIB", "qtechWlogNotifyApIp"),
        ("QTECH-WLAN-WLOG-MIB", "qtechWlogNotifyApCwDownId"),
        ("QTECH-WLAN-WLOG-MIB", "qtechWlogNotifyApIntfName"),
        ("QTECH-WLAN-WLOG-MIB", "qtechWlogNotifyApIntfInputRate"),
        ("QTECH-WLAN-WLOG-MIB", "qtechWlogNotifyApIntfOutputRate"),
        ("QTECH-WLAN-WLOG-MIB", "qtechWlogNotifyApIntfUnicastInputPkts"),
        ("QTECH-WLAN-WLOG-MIB", "qtechWlogNotifyApIntfUnicastOutputPkts"),
        ("QTECH-WLAN-WLOG-MIB", "qtechWlogNotifyApIntfMulticastInputPkts"),
        ("QTECH-WLAN-WLOG-MIB", "qtechWlogNotifyApIntfMulticastOutputPkts"),
        ("QTECH-WLAN-WLOG-MIB", "qtechWlogNotifyApIntfBroadcastInputPkts"),
        ("QTECH-WLAN-WLOG-MIB", "qtechWlogNotifyApIntfBroadcastOutputPkts"),
        ("QTECH-WLAN-WLOG-MIB", "qtechWlogNotifyApIntfErrorInputPkts"),
        ("QTECH-WLAN-WLOG-MIB", "qtechWlogNotifyApIntfErrorOutputPkts"))
)
if mibBuilder.loadTexts:
    qtechNotifyApCapwapDownIntf.setStatus(
        "current"
    )

qtechNotifyApCapwapDownRadio = NotificationType(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 118, 1, 2, 3)
)
qtechNotifyApCapwapDownRadio.setObjects(
      *(("QTECH-WLAN-WLOG-MIB", "qtechWlogNotifyApName"),
        ("QTECH-WLAN-WLOG-MIB", "qtechWlogNotifyApMac"),
        ("QTECH-WLAN-WLOG-MIB", "qtechWlogNotifyApIp"),
        ("QTECH-WLAN-WLOG-MIB", "qtechWlogNotifyApCwDownId"),
        ("QTECH-WLAN-WLOG-MIB", "qtechWlogNotifyApRadioId"),
        ("QTECH-WLAN-WLOG-MIB", "qtechWlogNotifyApRadioWorkChnl"),
        ("QTECH-WLAN-WLOG-MIB", "qtechWlogNotifyApRadioPower"),
        ("QTECH-WLAN-WLOG-MIB", "qtechWlogNotifyApRadioRssi"),
        ("QTECH-WLAN-WLOG-MIB", "qtechWlogNotifyApRadioErrFrame"),
        ("QTECH-WLAN-WLOG-MIB", "qtechWlogNotifyApRadioRetrsmit"),
        ("QTECH-WLAN-WLOG-MIB", "qtechWlogNotifyApRadioTotalStaNum"),
        ("QTECH-WLAN-WLOG-MIB", "qtechWlogNotifyApRadioWebStaNum"),
        ("QTECH-WLAN-WLOG-MIB", "qtechWlogNotifyApRadioD1xStaNum"))
)
if mibBuilder.loadTexts:
    qtechNotifyApCapwapDownRadio.setStatus(
        "current"
    )

qtechNotifyStaOper = NotificationType(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 118, 1, 2, 4)
)
qtechNotifyStaOper.setObjects(
      *(("QTECH-WLAN-WLOG-MIB", "qtechWlogNotifyStaMac"),
        ("QTECH-WLAN-WLOG-MIB", "qtechWlogNotifyStaIp"),
        ("QTECH-WLAN-WLOG-MIB", "qtechWlogNotifyStaIpv6"),
        ("QTECH-WLAN-WLOG-MIB", "qtechWlogNotifyStaRssi"),
        ("QTECH-WLAN-WLOG-MIB", "qtechWlogNotifyStaLinkrate"),
        ("QTECH-WLAN-WLOG-MIB", "qtechWlogNotifyApName"),
        ("QTECH-WLAN-WLOG-MIB", "qtechWlogNotifySsid"),
        ("QTECH-WLAN-WLOG-MIB", "qtechWlogNotifyStaOperType"))
)
if mibBuilder.loadTexts:
    qtechNotifyStaOper.setStatus(
        "current"
    )

qtechNotifyStaAbnormalOper = NotificationType(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 118, 1, 2, 5)
)
qtechNotifyStaAbnormalOper.setObjects(
      *(("QTECH-WLAN-WLOG-MIB", "qtechWlogNotifyStaMac"),
        ("QTECH-WLAN-WLOG-MIB", "qtechWlogNotifyStaIp"),
        ("QTECH-WLAN-WLOG-MIB", "qtechWlogNotifyStaIpv6"),
        ("QTECH-WLAN-WLOG-MIB", "qtechWlogNotifyStaAbnormalOperType"),
        ("QTECH-WLAN-WLOG-MIB", "qtechWlogNotifyStaOperReason"))
)
if mibBuilder.loadTexts:
    qtechNotifyStaAbnormalOper.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "QTECH-WLAN-WLOG-MIB",
    **{"qtechWlanWlogMIB": qtechWlanWlogMIB,
       "qtechWlanWlogNotificationsMIBObjects": qtechWlanWlogNotificationsMIBObjects,
       "qtechWlanWlogNtfObjects": qtechWlanWlogNtfObjects,
       "qtechWlogNotifyApName": qtechWlogNotifyApName,
       "qtechWlogNotifyApMac": qtechWlogNotifyApMac,
       "qtechWlogNotifyApIp": qtechWlogNotifyApIp,
       "qtechWlogNotifyApCwDownId": qtechWlogNotifyApCwDownId,
       "qtechWlogNotifyApCwDownReason": qtechWlogNotifyApCwDownReason,
       "qtechWlogNotifyApIntfStatTable": qtechWlogNotifyApIntfStatTable,
       "qtechWlogNotifyApIntfStatEntry": qtechWlogNotifyApIntfStatEntry,
       "qtechWlogNotifyApIntfName": qtechWlogNotifyApIntfName,
       "qtechWlogNotifyApIntfInputRate": qtechWlogNotifyApIntfInputRate,
       "qtechWlogNotifyApIntfOutputRate": qtechWlogNotifyApIntfOutputRate,
       "qtechWlogNotifyApIntfUnicastInputPkts": qtechWlogNotifyApIntfUnicastInputPkts,
       "qtechWlogNotifyApIntfUnicastOutputPkts": qtechWlogNotifyApIntfUnicastOutputPkts,
       "qtechWlogNotifyApIntfMulticastInputPkts": qtechWlogNotifyApIntfMulticastInputPkts,
       "qtechWlogNotifyApIntfMulticastOutputPkts": qtechWlogNotifyApIntfMulticastOutputPkts,
       "qtechWlogNotifyApIntfBroadcastInputPkts": qtechWlogNotifyApIntfBroadcastInputPkts,
       "qtechWlogNotifyApIntfBroadcastOutputPkts": qtechWlogNotifyApIntfBroadcastOutputPkts,
       "qtechWlogNotifyApIntfErrorInputPkts": qtechWlogNotifyApIntfErrorInputPkts,
       "qtechWlogNotifyApIntfErrorOutputPkts": qtechWlogNotifyApIntfErrorOutputPkts,
       "qtechWlogNotifyApRadioStatTable": qtechWlogNotifyApRadioStatTable,
       "qtechWlogNotifyApRadioStatEntry": qtechWlogNotifyApRadioStatEntry,
       "qtechWlogNotifyApRadioId": qtechWlogNotifyApRadioId,
       "qtechWlogNotifyApRadioWorkChnl": qtechWlogNotifyApRadioWorkChnl,
       "qtechWlogNotifyApRadioPower": qtechWlogNotifyApRadioPower,
       "qtechWlogNotifyApRadioRssi": qtechWlogNotifyApRadioRssi,
       "qtechWlogNotifyApRadioErrFrame": qtechWlogNotifyApRadioErrFrame,
       "qtechWlogNotifyApRadioRetrsmit": qtechWlogNotifyApRadioRetrsmit,
       "qtechWlogNotifyApRadioTotalStaNum": qtechWlogNotifyApRadioTotalStaNum,
       "qtechWlogNotifyApRadioWebStaNum": qtechWlogNotifyApRadioWebStaNum,
       "qtechWlogNotifyApRadioD1xStaNum": qtechWlogNotifyApRadioD1xStaNum,
       "qtechWlogNotifyStaMac": qtechWlogNotifyStaMac,
       "qtechWlogNotifyStaIp": qtechWlogNotifyStaIp,
       "qtechWlogNotifyStaIpv6": qtechWlogNotifyStaIpv6,
       "qtechWlogNotifySsid": qtechWlogNotifySsid,
       "qtechWlogNotifyStaRssi": qtechWlogNotifyStaRssi,
       "qtechWlogNotifyStaLinkrate": qtechWlogNotifyStaLinkrate,
       "qtechWlogNotifyStaOperType": qtechWlogNotifyStaOperType,
       "qtechWlogNotifyStaAbnormalOperType": qtechWlogNotifyStaAbnormalOperType,
       "qtechWlogNotifyStaOperReason": qtechWlogNotifyStaOperReason,
       "qtechWlanWlogNotifications": qtechWlanWlogNotifications,
       "qtechNotifyApCapwapDownReason": qtechNotifyApCapwapDownReason,
       "qtechNotifyApCapwapDownIntf": qtechNotifyApCapwapDownIntf,
       "qtechNotifyApCapwapDownRadio": qtechNotifyApCapwapDownRadio,
       "qtechNotifyStaOper": qtechNotifyStaOper,
       "qtechNotifyStaAbnormalOper": qtechNotifyStaAbnormalOper}
)
