# SNMP MIB module (QTECH-DOT11-WIDS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/qtech/QTECH-DOT11-WIDS-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:59:34 2025
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


# MODULE-IDENTITY

qtechDot11WIDSMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 62)
)
if mibBuilder.loadTexts:
    qtechDot11WIDSMIB.setRevisions(
        ("2009-04-15 09:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_QtechDot11WIDSTraps_ObjectIdentity = ObjectIdentity
qtechDot11WIDSTraps = _QtechDot11WIDSTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 62, 0)
)
_QtechDot11WIDSConfigObjects_ObjectIdentity = ObjectIdentity
qtechDot11WIDSConfigObjects = _QtechDot11WIDSConfigObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 62, 1)
)
_QtechDot11WIDSPermitVendorTable_Object = MibTable
qtechDot11WIDSPermitVendorTable = _QtechDot11WIDSPermitVendorTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 62, 1, 1)
)
if mibBuilder.loadTexts:
    qtechDot11WIDSPermitVendorTable.setStatus("current")
_QtechDot11WIDSPermitVendorEntry_Object = MibTableRow
qtechDot11WIDSPermitVendorEntry = _QtechDot11WIDSPermitVendorEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 62, 1, 1, 1)
)
qtechDot11WIDSPermitVendorEntry.setIndexNames(
    (0, "QTECH-DOT11-WIDS-MIB", "qtechDot11VendorOUI"),
)
if mibBuilder.loadTexts:
    qtechDot11WIDSPermitVendorEntry.setStatus("current")
_QtechDot11VendorOUI_Type = Integer32
_QtechDot11VendorOUI_Object = MibTableColumn
qtechDot11VendorOUI = _QtechDot11VendorOUI_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 62, 1, 1, 1, 1),
    _QtechDot11VendorOUI_Type()
)
qtechDot11VendorOUI.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qtechDot11VendorOUI.setStatus("current")
_QtechDot11VendorOper_Type = Integer32
_QtechDot11VendorOper_Object = MibTableColumn
qtechDot11VendorOper = _QtechDot11VendorOper_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 62, 1, 1, 1, 2),
    _QtechDot11VendorOper_Type()
)
qtechDot11VendorOper.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechDot11VendorOper.setStatus("current")
_QtechDot11VendorName_Type = MacAddress
_QtechDot11VendorName_Object = MibTableColumn
qtechDot11VendorName = _QtechDot11VendorName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 62, 1, 1, 1, 3),
    _QtechDot11VendorName_Type()
)
qtechDot11VendorName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechDot11VendorName.setStatus("current")
_QtechDot11WIDSPermitSSIDTable_Object = MibTable
qtechDot11WIDSPermitSSIDTable = _QtechDot11WIDSPermitSSIDTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 62, 1, 2)
)
if mibBuilder.loadTexts:
    qtechDot11WIDSPermitSSIDTable.setStatus("current")
_QtechDot11WIDSPermitSSIDEntry_Object = MibTableRow
qtechDot11WIDSPermitSSIDEntry = _QtechDot11WIDSPermitSSIDEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 62, 1, 2, 1)
)
qtechDot11WIDSPermitSSIDEntry.setIndexNames(
    (0, "QTECH-DOT11-WIDS-MIB", "qtechDot11PermitNum"),
)
if mibBuilder.loadTexts:
    qtechDot11WIDSPermitSSIDEntry.setStatus("current")
_QtechDot11PermitNum_Type = Integer32
_QtechDot11PermitNum_Object = MibTableColumn
qtechDot11PermitNum = _QtechDot11PermitNum_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 62, 1, 2, 1, 1),
    _QtechDot11PermitNum_Type()
)
qtechDot11PermitNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qtechDot11PermitNum.setStatus("current")
_QtechDot11PermitOper_Type = Integer32
_QtechDot11PermitOper_Object = MibTableColumn
qtechDot11PermitOper = _QtechDot11PermitOper_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 62, 1, 2, 1, 2),
    _QtechDot11PermitOper_Type()
)
qtechDot11PermitOper.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechDot11PermitOper.setStatus("current")


class _QtechDot11PermitSSID_Type(DisplayString):
    """Custom type qtechDot11PermitSSID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_QtechDot11PermitSSID_Type.__name__ = "DisplayString"
_QtechDot11PermitSSID_Object = MibTableColumn
qtechDot11PermitSSID = _QtechDot11PermitSSID_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 62, 1, 2, 1, 3),
    _QtechDot11PermitSSID_Type()
)
qtechDot11PermitSSID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechDot11PermitSSID.setStatus("current")
_QtechDot11WIDSDeviceAttackMacaddressListTable_Object = MibTable
qtechDot11WIDSDeviceAttackMacaddressListTable = _QtechDot11WIDSDeviceAttackMacaddressListTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 62, 1, 3)
)
if mibBuilder.loadTexts:
    qtechDot11WIDSDeviceAttackMacaddressListTable.setStatus("current")
_QtechDot11WIDSDeviceAttackMacaddressListEntry_Object = MibTableRow
qtechDot11WIDSDeviceAttackMacaddressListEntry = _QtechDot11WIDSDeviceAttackMacaddressListEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 62, 1, 3, 1)
)
qtechDot11WIDSDeviceAttackMacaddressListEntry.setIndexNames(
    (0, "QTECH-DOT11-WIDS-MIB", "qtechDot11AttackNum"),
)
if mibBuilder.loadTexts:
    qtechDot11WIDSDeviceAttackMacaddressListEntry.setStatus("current")
_QtechDot11AttackNum_Type = Integer32
_QtechDot11AttackNum_Object = MibTableColumn
qtechDot11AttackNum = _QtechDot11AttackNum_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 62, 1, 3, 1, 1),
    _QtechDot11AttackNum_Type()
)
qtechDot11AttackNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qtechDot11AttackNum.setStatus("current")
_QtechDot11AttackOper_Type = Integer32
_QtechDot11AttackOper_Object = MibTableColumn
qtechDot11AttackOper = _QtechDot11AttackOper_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 62, 1, 3, 1, 2),
    _QtechDot11AttackOper_Type()
)
qtechDot11AttackOper.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechDot11AttackOper.setStatus("current")
_QtechDot11AttackMAC_Type = MacAddress
_QtechDot11AttackMAC_Object = MibTableColumn
qtechDot11AttackMAC = _QtechDot11AttackMAC_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 62, 1, 3, 1, 3),
    _QtechDot11AttackMAC_Type()
)
qtechDot11AttackMAC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechDot11AttackMAC.setStatus("current")


class _QtechDot11AttackInfo_Type(DisplayString):
    """Custom type qtechDot11AttackInfo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_QtechDot11AttackInfo_Type.__name__ = "DisplayString"
_QtechDot11AttackInfo_Object = MibTableColumn
qtechDot11AttackInfo = _QtechDot11AttackInfo_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 62, 1, 3, 1, 4),
    _QtechDot11AttackInfo_Type()
)
qtechDot11AttackInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechDot11AttackInfo.setStatus("current")
_QtechDot11WIDSDevicePermitMacaddressListTable_Object = MibTable
qtechDot11WIDSDevicePermitMacaddressListTable = _QtechDot11WIDSDevicePermitMacaddressListTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 62, 1, 4)
)
if mibBuilder.loadTexts:
    qtechDot11WIDSDevicePermitMacaddressListTable.setStatus("current")
_QtechDot11WIDSDevicePermitMacaddressListEntry_Object = MibTableRow
qtechDot11WIDSDevicePermitMacaddressListEntry = _QtechDot11WIDSDevicePermitMacaddressListEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 62, 1, 4, 1)
)
qtechDot11WIDSDevicePermitMacaddressListEntry.setIndexNames(
    (0, "QTECH-DOT11-WIDS-MIB", "qtechDot11PermitMACNum"),
)
if mibBuilder.loadTexts:
    qtechDot11WIDSDevicePermitMacaddressListEntry.setStatus("current")
_QtechDot11PermitMACNum_Type = Integer32
_QtechDot11PermitMACNum_Object = MibTableColumn
qtechDot11PermitMACNum = _QtechDot11PermitMACNum_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 62, 1, 4, 1, 1),
    _QtechDot11PermitMACNum_Type()
)
qtechDot11PermitMACNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qtechDot11PermitMACNum.setStatus("current")
_QtechDot11PermitMACOper_Type = Integer32
_QtechDot11PermitMACOper_Object = MibTableColumn
qtechDot11PermitMACOper = _QtechDot11PermitMACOper_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 62, 1, 4, 1, 2),
    _QtechDot11PermitMACOper_Type()
)
qtechDot11PermitMACOper.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechDot11PermitMACOper.setStatus("current")
_QtechDot11PermitMACAddr_Type = MacAddress
_QtechDot11PermitMACAddr_Object = MibTableColumn
qtechDot11PermitMACAddr = _QtechDot11PermitMACAddr_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 62, 1, 4, 1, 3),
    _QtechDot11PermitMACAddr_Type()
)
qtechDot11PermitMACAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechDot11PermitMACAddr.setStatus("current")
_QtechDot11WIDSDeviceagingDuration_Type = Integer32
_QtechDot11WIDSDeviceagingDuration_Object = MibScalar
qtechDot11WIDSDeviceagingDuration = _QtechDot11WIDSDeviceagingDuration_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 62, 1, 5),
    _QtechDot11WIDSDeviceagingDuration_Type()
)
qtechDot11WIDSDeviceagingDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechDot11WIDSDeviceagingDuration.setStatus("current")
_QtechDot11WIDSCountermeasuresMode_Type = Integer32
_QtechDot11WIDSCountermeasuresMode_Object = MibScalar
qtechDot11WIDSCountermeasuresMode = _QtechDot11WIDSCountermeasuresMode_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 62, 1, 6),
    _QtechDot11WIDSCountermeasuresMode_Type()
)
qtechDot11WIDSCountermeasuresMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechDot11WIDSCountermeasuresMode.setStatus("current")
_QtechDot11WIDSCountermeasureSet_Type = Integer32
_QtechDot11WIDSCountermeasureSet_Object = MibScalar
qtechDot11WIDSCountermeasureSet = _QtechDot11WIDSCountermeasureSet_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 62, 1, 7),
    _QtechDot11WIDSCountermeasureSet_Type()
)
qtechDot11WIDSCountermeasureSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechDot11WIDSCountermeasureSet.setStatus("current")
_QtechDot11WIDSModeTable_Object = MibTable
qtechDot11WIDSModeTable = _QtechDot11WIDSModeTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 62, 1, 8)
)
if mibBuilder.loadTexts:
    qtechDot11WIDSModeTable.setStatus("current")
_QtechDot11WIDSModeEntry_Object = MibTableRow
qtechDot11WIDSModeEntry = _QtechDot11WIDSModeEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 62, 1, 8, 1)
)
qtechDot11WIDSModeEntry.setIndexNames(
    (0, "QTECH-DOT11-WIDS-MIB", "qtechDot11WIDSAPID"),
)
if mibBuilder.loadTexts:
    qtechDot11WIDSModeEntry.setStatus("current")
_QtechDot11WIDSAPID_Type = Integer32
_QtechDot11WIDSAPID_Object = MibTableColumn
qtechDot11WIDSAPID = _QtechDot11WIDSAPID_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 62, 1, 8, 1, 1),
    _QtechDot11WIDSAPID_Type()
)
qtechDot11WIDSAPID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qtechDot11WIDSAPID.setStatus("current")
_QtechDot11WIDSDeviceMode_Type = Integer32
_QtechDot11WIDSDeviceMode_Object = MibTableColumn
qtechDot11WIDSDeviceMode = _QtechDot11WIDSDeviceMode_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 62, 1, 8, 1, 2),
    _QtechDot11WIDSDeviceMode_Type()
)
qtechDot11WIDSDeviceMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechDot11WIDSDeviceMode.setStatus("current")
_QtechDot11WIDSWhitelistMacaddressListTable_Object = MibTable
qtechDot11WIDSWhitelistMacaddressListTable = _QtechDot11WIDSWhitelistMacaddressListTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 62, 1, 9)
)
if mibBuilder.loadTexts:
    qtechDot11WIDSWhitelistMacaddressListTable.setStatus("current")
_QtechDot11WIDSWhitelistMacaddressListEntry_Object = MibTableRow
qtechDot11WIDSWhitelistMacaddressListEntry = _QtechDot11WIDSWhitelistMacaddressListEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 62, 1, 9, 1)
)
qtechDot11WIDSWhitelistMacaddressListEntry.setIndexNames(
    (0, "QTECH-DOT11-WIDS-MIB", "qtechDot11WhitelistNum"),
)
if mibBuilder.loadTexts:
    qtechDot11WIDSWhitelistMacaddressListEntry.setStatus("current")
_QtechDot11WhitelistNum_Type = Integer32
_QtechDot11WhitelistNum_Object = MibTableColumn
qtechDot11WhitelistNum = _QtechDot11WhitelistNum_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 62, 1, 9, 1, 1),
    _QtechDot11WhitelistNum_Type()
)
qtechDot11WhitelistNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qtechDot11WhitelistNum.setStatus("current")
_QtechDot11WhitelistOper_Type = Integer32
_QtechDot11WhitelistOper_Object = MibTableColumn
qtechDot11WhitelistOper = _QtechDot11WhitelistOper_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 62, 1, 9, 1, 2),
    _QtechDot11WhitelistOper_Type()
)
qtechDot11WhitelistOper.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechDot11WhitelistOper.setStatus("current")
_QtechDot11WhitelistMAC_Type = MacAddress
_QtechDot11WhitelistMAC_Object = MibTableColumn
qtechDot11WhitelistMAC = _QtechDot11WhitelistMAC_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 62, 1, 9, 1, 3),
    _QtechDot11WhitelistMAC_Type()
)
qtechDot11WhitelistMAC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechDot11WhitelistMAC.setStatus("current")
_QtechDot11WIDSStaticblackListTable_Object = MibTable
qtechDot11WIDSStaticblackListTable = _QtechDot11WIDSStaticblackListTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 62, 1, 10)
)
if mibBuilder.loadTexts:
    qtechDot11WIDSStaticblackListTable.setStatus("current")
_QtechDot11WIDSStaticblackListEntry_Object = MibTableRow
qtechDot11WIDSStaticblackListEntry = _QtechDot11WIDSStaticblackListEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 62, 1, 10, 1)
)
qtechDot11WIDSStaticblackListEntry.setIndexNames(
    (0, "QTECH-DOT11-WIDS-MIB", "qtechDot11StaticblacklistNum"),
)
if mibBuilder.loadTexts:
    qtechDot11WIDSStaticblackListEntry.setStatus("current")
_QtechDot11StaticblacklistNum_Type = Integer32
_QtechDot11StaticblacklistNum_Object = MibTableColumn
qtechDot11StaticblacklistNum = _QtechDot11StaticblacklistNum_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 62, 1, 10, 1, 1),
    _QtechDot11StaticblacklistNum_Type()
)
qtechDot11StaticblacklistNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qtechDot11StaticblacklistNum.setStatus("current")
_QtechDot11StaticblacklistOper_Type = Integer32
_QtechDot11StaticblacklistOper_Object = MibTableColumn
qtechDot11StaticblacklistOper = _QtechDot11StaticblacklistOper_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 62, 1, 10, 1, 2),
    _QtechDot11StaticblacklistOper_Type()
)
qtechDot11StaticblacklistOper.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechDot11StaticblacklistOper.setStatus("current")
_QtechDot11StaticblacklistMAC_Type = MacAddress
_QtechDot11StaticblacklistMAC_Object = MibTableColumn
qtechDot11StaticblacklistMAC = _QtechDot11StaticblacklistMAC_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 62, 1, 10, 1, 3),
    _QtechDot11StaticblacklistMAC_Type()
)
qtechDot11StaticblacklistMAC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechDot11StaticblacklistMAC.setStatus("current")
_QtechDot11WIDSDynamicblacklistEnable_Type = TruthValue
_QtechDot11WIDSDynamicblacklistEnable_Object = MibScalar
qtechDot11WIDSDynamicblacklistEnable = _QtechDot11WIDSDynamicblacklistEnable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 62, 1, 11),
    _QtechDot11WIDSDynamicblacklistEnable_Type()
)
qtechDot11WIDSDynamicblacklistEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechDot11WIDSDynamicblacklistEnable.setStatus("current")
_QtechDot11WIDSDynamicblacklistLifetime_Type = Integer32
_QtechDot11WIDSDynamicblacklistLifetime_Object = MibScalar
qtechDot11WIDSDynamicblacklistLifetime = _QtechDot11WIDSDynamicblacklistLifetime_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 62, 1, 12),
    _QtechDot11WIDSDynamicblacklistLifetime_Type()
)
qtechDot11WIDSDynamicblacklistLifetime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechDot11WIDSDynamicblacklistLifetime.setStatus("current")
_QtechDot11WIDSAttackDetectionMode_Type = Integer32
_QtechDot11WIDSAttackDetectionMode_Object = MibScalar
qtechDot11WIDSAttackDetectionMode = _QtechDot11WIDSAttackDetectionMode_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 62, 1, 13),
    _QtechDot11WIDSAttackDetectionMode_Type()
)
qtechDot11WIDSAttackDetectionMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechDot11WIDSAttackDetectionMode.setStatus("current")
_QtechDot11WIDSRogueInfoTable_Object = MibTable
qtechDot11WIDSRogueInfoTable = _QtechDot11WIDSRogueInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 62, 1, 14)
)
if mibBuilder.loadTexts:
    qtechDot11WIDSRogueInfoTable.setStatus("current")
_QtechDot11WIDSRogueInfoEntry_Object = MibTableRow
qtechDot11WIDSRogueInfoEntry = _QtechDot11WIDSRogueInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 62, 1, 14, 1)
)
qtechDot11WIDSRogueInfoEntry.setIndexNames(
    (0, "QTECH-DOT11-WIDS-MIB", "qtechDot11WIDSRogueInfoNUM"),
    (0, "QTECH-DOT11-WIDS-MIB", "qtechDot11WIDSRogueInfoTYPE"),
)
if mibBuilder.loadTexts:
    qtechDot11WIDSRogueInfoEntry.setStatus("current")
_QtechDot11WIDSRogueInfoNUM_Type = Integer32
_QtechDot11WIDSRogueInfoNUM_Object = MibTableColumn
qtechDot11WIDSRogueInfoNUM = _QtechDot11WIDSRogueInfoNUM_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 62, 1, 14, 1, 1),
    _QtechDot11WIDSRogueInfoNUM_Type()
)
qtechDot11WIDSRogueInfoNUM.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qtechDot11WIDSRogueInfoNUM.setStatus("current")
_QtechDot11WIDSRogueInfoTYPE_Type = Integer32
_QtechDot11WIDSRogueInfoTYPE_Object = MibTableColumn
qtechDot11WIDSRogueInfoTYPE = _QtechDot11WIDSRogueInfoTYPE_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 62, 1, 14, 1, 2),
    _QtechDot11WIDSRogueInfoTYPE_Type()
)
qtechDot11WIDSRogueInfoTYPE.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qtechDot11WIDSRogueInfoTYPE.setStatus("current")
_QtechDot11WIDSRogueInfoOper_Type = Integer32
_QtechDot11WIDSRogueInfoOper_Object = MibTableColumn
qtechDot11WIDSRogueInfoOper = _QtechDot11WIDSRogueInfoOper_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 62, 1, 14, 1, 3),
    _QtechDot11WIDSRogueInfoOper_Type()
)
qtechDot11WIDSRogueInfoOper.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechDot11WIDSRogueInfoOper.setStatus("current")
_QtechDot11WIDSRogueInfoMAC_Type = MacAddress
_QtechDot11WIDSRogueInfoMAC_Object = MibTableColumn
qtechDot11WIDSRogueInfoMAC = _QtechDot11WIDSRogueInfoMAC_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 62, 1, 14, 1, 4),
    _QtechDot11WIDSRogueInfoMAC_Type()
)
qtechDot11WIDSRogueInfoMAC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechDot11WIDSRogueInfoMAC.setStatus("current")
_QtechDot11WIDSRogueInfoString_Type = DisplayString
_QtechDot11WIDSRogueInfoString_Object = MibTableColumn
qtechDot11WIDSRogueInfoString = _QtechDot11WIDSRogueInfoString_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 62, 1, 14, 1, 5),
    _QtechDot11WIDSRogueInfoString_Type()
)
qtechDot11WIDSRogueInfoString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechDot11WIDSRogueInfoString.setStatus("current")
_QtechDot11WIDSPermitmaclistEnableTable_Object = MibTable
qtechDot11WIDSPermitmaclistEnableTable = _QtechDot11WIDSPermitmaclistEnableTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 62, 1, 15)
)
if mibBuilder.loadTexts:
    qtechDot11WIDSPermitmaclistEnableTable.setStatus("current")
_QtechDot11WIDSPermitmaclistEnableEntry_Object = MibTableRow
qtechDot11WIDSPermitmaclistEnableEntry = _QtechDot11WIDSPermitmaclistEnableEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 62, 1, 15, 1)
)
qtechDot11WIDSPermitmaclistEnableEntry.setIndexNames(
    (0, "QTECH-DOT11-WIDS-MIB", "qtechDot11WIDSEnableVlanPermitmaclistNum"),
)
if mibBuilder.loadTexts:
    qtechDot11WIDSPermitmaclistEnableEntry.setStatus("current")
_QtechDot11WIDSEnableVlanPermitmaclistNum_Type = Integer32
_QtechDot11WIDSEnableVlanPermitmaclistNum_Object = MibTableColumn
qtechDot11WIDSEnableVlanPermitmaclistNum = _QtechDot11WIDSEnableVlanPermitmaclistNum_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 62, 1, 15, 1, 1),
    _QtechDot11WIDSEnableVlanPermitmaclistNum_Type()
)
qtechDot11WIDSEnableVlanPermitmaclistNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qtechDot11WIDSEnableVlanPermitmaclistNum.setStatus("current")
_QtechDot11WIDSEnableVlanPermitmaclistOper_Type = Integer32
_QtechDot11WIDSEnableVlanPermitmaclistOper_Object = MibTableColumn
qtechDot11WIDSEnableVlanPermitmaclistOper = _QtechDot11WIDSEnableVlanPermitmaclistOper_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 62, 1, 15, 1, 2),
    _QtechDot11WIDSEnableVlanPermitmaclistOper_Type()
)
qtechDot11WIDSEnableVlanPermitmaclistOper.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechDot11WIDSEnableVlanPermitmaclistOper.setStatus("current")
_QtechDot11WIDSEnableVlanPermitmaclist_Type = MacAddress
_QtechDot11WIDSEnableVlanPermitmaclist_Object = MibTableColumn
qtechDot11WIDSEnableVlanPermitmaclist = _QtechDot11WIDSEnableVlanPermitmaclist_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 62, 1, 15, 1, 3),
    _QtechDot11WIDSEnableVlanPermitmaclist_Type()
)
qtechDot11WIDSEnableVlanPermitmaclist.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechDot11WIDSEnableVlanPermitmaclist.setStatus("current")
_QtechDot11WIDSResetStatistics_Type = TruthValue
_QtechDot11WIDSResetStatistics_Object = MibScalar
qtechDot11WIDSResetStatistics = _QtechDot11WIDSResetStatistics_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 62, 1, 18),
    _QtechDot11WIDSResetStatistics_Type()
)
qtechDot11WIDSResetStatistics.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechDot11WIDSResetStatistics.setStatus("current")
_QtechDot11WIDSResetRoguehistoryStatistics_Type = Integer32
_QtechDot11WIDSResetRoguehistoryStatistics_Object = MibScalar
qtechDot11WIDSResetRoguehistoryStatistics = _QtechDot11WIDSResetRoguehistoryStatistics_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 62, 1, 19),
    _QtechDot11WIDSResetRoguehistoryStatistics_Type()
)
qtechDot11WIDSResetRoguehistoryStatistics.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechDot11WIDSResetRoguehistoryStatistics.setStatus("current")
_QtechDot11WIDSResethistory_Type = Integer32
_QtechDot11WIDSResethistory_Object = MibScalar
qtechDot11WIDSResethistory = _QtechDot11WIDSResethistory_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 62, 1, 20),
    _QtechDot11WIDSResethistory_Type()
)
qtechDot11WIDSResethistory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechDot11WIDSResethistory.setStatus("current")
_QtechDot11WIDSResetDynamicBlacklistTable_Object = MibTable
qtechDot11WIDSResetDynamicBlacklistTable = _QtechDot11WIDSResetDynamicBlacklistTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 62, 1, 21)
)
if mibBuilder.loadTexts:
    qtechDot11WIDSResetDynamicBlacklistTable.setStatus("current")
_QtechDot11WIDSResetDynamicBlacklistEntry_Object = MibTableRow
qtechDot11WIDSResetDynamicBlacklistEntry = _QtechDot11WIDSResetDynamicBlacklistEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 62, 1, 21, 1)
)
qtechDot11WIDSResetDynamicBlacklistEntry.setIndexNames(
    (0, "QTECH-DOT11-WIDS-MIB", "qtechDot11WIDSResetDynamicBlacklistMac"),
)
if mibBuilder.loadTexts:
    qtechDot11WIDSResetDynamicBlacklistEntry.setStatus("current")
_QtechDot11WIDSResetDynamicBlacklistMac_Type = MacAddress
_QtechDot11WIDSResetDynamicBlacklistMac_Object = MibTableColumn
qtechDot11WIDSResetDynamicBlacklistMac = _QtechDot11WIDSResetDynamicBlacklistMac_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 62, 1, 21, 1, 1),
    _QtechDot11WIDSResetDynamicBlacklistMac_Type()
)
qtechDot11WIDSResetDynamicBlacklistMac.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qtechDot11WIDSResetDynamicBlacklistMac.setStatus("current")
_QtechDot11WIDSResetDynamicBlacklistType_Type = Integer32
_QtechDot11WIDSResetDynamicBlacklistType_Object = MibTableColumn
qtechDot11WIDSResetDynamicBlacklistType = _QtechDot11WIDSResetDynamicBlacklistType_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 62, 1, 21, 1, 2),
    _QtechDot11WIDSResetDynamicBlacklistType_Type()
)
qtechDot11WIDSResetDynamicBlacklistType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechDot11WIDSResetDynamicBlacklistType.setStatus("current")
_QtechDot11WIDResetUserisolationStatistics_Type = Integer32
_QtechDot11WIDResetUserisolationStatistics_Object = MibScalar
qtechDot11WIDResetUserisolationStatistics = _QtechDot11WIDResetUserisolationStatistics_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 62, 1, 22),
    _QtechDot11WIDResetUserisolationStatistics_Type()
)
qtechDot11WIDResetUserisolationStatistics.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechDot11WIDResetUserisolationStatistics.setStatus("current")
_QtechDot11WIDUserisolationAC_Type = Integer32
_QtechDot11WIDUserisolationAC_Object = MibScalar
qtechDot11WIDUserisolationAC = _QtechDot11WIDUserisolationAC_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 62, 1, 23),
    _QtechDot11WIDUserisolationAC_Type()
)
qtechDot11WIDUserisolationAC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechDot11WIDUserisolationAC.setStatus("current")
_QtechDot11WIDUserisolationAP_Type = Integer32
_QtechDot11WIDUserisolationAP_Object = MibScalar
qtechDot11WIDUserisolationAP = _QtechDot11WIDUserisolationAP_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 62, 1, 24),
    _QtechDot11WIDUserisolationAP_Type()
)
qtechDot11WIDUserisolationAP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechDot11WIDUserisolationAP.setStatus("current")
_QtechDot11WIDSShowStaticsTable_Object = MibTable
qtechDot11WIDSShowStaticsTable = _QtechDot11WIDSShowStaticsTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 62, 1, 25)
)
if mibBuilder.loadTexts:
    qtechDot11WIDSShowStaticsTable.setStatus("current")
_QtechDot11WIDSShowStaticsEntry_Object = MibTableRow
qtechDot11WIDSShowStaticsEntry = _QtechDot11WIDSShowStaticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 62, 1, 25, 1)
)
qtechDot11WIDSShowStaticsEntry.setIndexNames(
    (0, "QTECH-DOT11-WIDS-MIB", "qtechDot11WIDSShowStaticsNum"),
)
if mibBuilder.loadTexts:
    qtechDot11WIDSShowStaticsEntry.setStatus("current")
_QtechDot11WIDSShowStaticsNum_Type = Integer32
_QtechDot11WIDSShowStaticsNum_Object = MibTableColumn
qtechDot11WIDSShowStaticsNum = _QtechDot11WIDSShowStaticsNum_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 62, 1, 25, 1, 1),
    _QtechDot11WIDSShowStaticsNum_Type()
)
qtechDot11WIDSShowStaticsNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qtechDot11WIDSShowStaticsNum.setStatus("current")
_QtechDot11WIDSShowStaticsOper_Type = Integer32
_QtechDot11WIDSShowStaticsOper_Object = MibTableColumn
qtechDot11WIDSShowStaticsOper = _QtechDot11WIDSShowStaticsOper_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 62, 1, 25, 1, 2),
    _QtechDot11WIDSShowStaticsOper_Type()
)
qtechDot11WIDSShowStaticsOper.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechDot11WIDSShowStaticsOper.setStatus("current")
_QtechDot11WIDSShowStaticsMac_Type = MacAddress
_QtechDot11WIDSShowStaticsMac_Object = MibTableColumn
qtechDot11WIDSShowStaticsMac = _QtechDot11WIDSShowStaticsMac_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 62, 1, 25, 1, 3),
    _QtechDot11WIDSShowStaticsMac_Type()
)
qtechDot11WIDSShowStaticsMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechDot11WIDSShowStaticsMac.setStatus("current")


class _QtechDot11WIDSShowStaticsInfo_Type(DisplayString):
    """Custom type qtechDot11WIDSShowStaticsInfo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_QtechDot11WIDSShowStaticsInfo_Type.__name__ = "DisplayString"
_QtechDot11WIDSShowStaticsInfo_Object = MibTableColumn
qtechDot11WIDSShowStaticsInfo = _QtechDot11WIDSShowStaticsInfo_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 62, 1, 25, 1, 4),
    _QtechDot11WIDSShowStaticsInfo_Type()
)
qtechDot11WIDSShowStaticsInfo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechDot11WIDSShowStaticsInfo.setStatus("current")
_QtechDot11WIDSAssociationFailureTotalTimes_Type = Integer32
_QtechDot11WIDSAssociationFailureTotalTimes_Object = MibScalar
qtechDot11WIDSAssociationFailureTotalTimes = _QtechDot11WIDSAssociationFailureTotalTimes_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 62, 1, 26),
    _QtechDot11WIDSAssociationFailureTotalTimes_Type()
)
qtechDot11WIDSAssociationFailureTotalTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechDot11WIDSAssociationFailureTotalTimes.setStatus("current")
_QtechDot11WIDSSuspiciousAPInfoTable_Object = MibTable
qtechDot11WIDSSuspiciousAPInfoTable = _QtechDot11WIDSSuspiciousAPInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 62, 1, 27)
)
if mibBuilder.loadTexts:
    qtechDot11WIDSSuspiciousAPInfoTable.setStatus("current")
_QtechDot11WIDSSuspiciousAPInfoEntry_Object = MibTableRow
qtechDot11WIDSSuspiciousAPInfoEntry = _QtechDot11WIDSSuspiciousAPInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 62, 1, 27, 1)
)
qtechDot11WIDSSuspiciousAPInfoEntry.setIndexNames(
    (0, "QTECH-DOT11-WIDS-MIB", "qtechDot11WIDSSuspiciousAPBSS"),
)
if mibBuilder.loadTexts:
    qtechDot11WIDSSuspiciousAPInfoEntry.setStatus("current")
_QtechDot11WIDSSuspiciousAPBSS_Type = MacAddress
_QtechDot11WIDSSuspiciousAPBSS_Object = MibTableColumn
qtechDot11WIDSSuspiciousAPBSS = _QtechDot11WIDSSuspiciousAPBSS_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 62, 1, 27, 1, 1),
    _QtechDot11WIDSSuspiciousAPBSS_Type()
)
qtechDot11WIDSSuspiciousAPBSS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechDot11WIDSSuspiciousAPBSS.setStatus("current")
_QtechDot11WIDSSuspiciousAPCount_Type = Integer32
_QtechDot11WIDSSuspiciousAPCount_Object = MibTableColumn
qtechDot11WIDSSuspiciousAPCount = _QtechDot11WIDSSuspiciousAPCount_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 62, 1, 27, 1, 2),
    _QtechDot11WIDSSuspiciousAPCount_Type()
)
qtechDot11WIDSSuspiciousAPCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechDot11WIDSSuspiciousAPCount.setStatus("current")
_QtechDot11WIDSMomentFirstTimeDetectedSusAP_Type = TimeTicks
_QtechDot11WIDSMomentFirstTimeDetectedSusAP_Object = MibTableColumn
qtechDot11WIDSMomentFirstTimeDetectedSusAP = _QtechDot11WIDSMomentFirstTimeDetectedSusAP_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 62, 1, 27, 1, 3),
    _QtechDot11WIDSMomentFirstTimeDetectedSusAP_Type()
)
qtechDot11WIDSMomentFirstTimeDetectedSusAP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechDot11WIDSMomentFirstTimeDetectedSusAP.setStatus("current")
_QtechDot11WIDSMomentLastTimeDetectedSusAP_Type = TimeTicks
_QtechDot11WIDSMomentLastTimeDetectedSusAP_Object = MibTableColumn
qtechDot11WIDSMomentLastTimeDetectedSusAP = _QtechDot11WIDSMomentLastTimeDetectedSusAP_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 62, 1, 27, 1, 4),
    _QtechDot11WIDSMomentLastTimeDetectedSusAP_Type()
)
qtechDot11WIDSMomentLastTimeDetectedSusAP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechDot11WIDSMomentLastTimeDetectedSusAP.setStatus("current")
_QtechDot11WIDSSuspiciousAPSSID_Type = DisplayString
_QtechDot11WIDSSuspiciousAPSSID_Object = MibTableColumn
qtechDot11WIDSSuspiciousAPSSID = _QtechDot11WIDSSuspiciousAPSSID_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 62, 1, 27, 1, 5),
    _QtechDot11WIDSSuspiciousAPSSID_Type()
)
qtechDot11WIDSSuspiciousAPSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechDot11WIDSSuspiciousAPSSID.setStatus("current")
_QtechDot11WIDSSuspiciousAPMaxSignalStrength_Type = Integer32
_QtechDot11WIDSSuspiciousAPMaxSignalStrength_Object = MibTableColumn
qtechDot11WIDSSuspiciousAPMaxSignalStrength = _QtechDot11WIDSSuspiciousAPMaxSignalStrength_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 62, 1, 27, 1, 6),
    _QtechDot11WIDSSuspiciousAPMaxSignalStrength_Type()
)
qtechDot11WIDSSuspiciousAPMaxSignalStrength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechDot11WIDSSuspiciousAPMaxSignalStrength.setStatus("current")
_QtechDot11WIDSSuspiciousAPUsingChannel_Type = Integer32
_QtechDot11WIDSSuspiciousAPUsingChannel_Object = MibTableColumn
qtechDot11WIDSSuspiciousAPUsingChannel = _QtechDot11WIDSSuspiciousAPUsingChannel_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 62, 1, 27, 1, 7),
    _QtechDot11WIDSSuspiciousAPUsingChannel_Type()
)
qtechDot11WIDSSuspiciousAPUsingChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechDot11WIDSSuspiciousAPUsingChannel.setStatus("current")
_QtechDot11WIDSSuspiciousAPFrameEncrption_Type = Integer32
_QtechDot11WIDSSuspiciousAPFrameEncrption_Object = MibTableColumn
qtechDot11WIDSSuspiciousAPFrameEncrption = _QtechDot11WIDSSuspiciousAPFrameEncrption_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 62, 1, 27, 1, 8),
    _QtechDot11WIDSSuspiciousAPFrameEncrption_Type()
)
qtechDot11WIDSSuspiciousAPFrameEncrption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechDot11WIDSSuspiciousAPFrameEncrption.setStatus("current")
_QtechDot11WIDSSuspiciousAPNeedsDealingTag_Type = TruthValue
_QtechDot11WIDSSuspiciousAPNeedsDealingTag_Object = MibTableColumn
qtechDot11WIDSSuspiciousAPNeedsDealingTag = _QtechDot11WIDSSuspiciousAPNeedsDealingTag_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 62, 1, 27, 1, 9),
    _QtechDot11WIDSSuspiciousAPNeedsDealingTag_Type()
)
qtechDot11WIDSSuspiciousAPNeedsDealingTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechDot11WIDSSuspiciousAPNeedsDealingTag.setStatus("current")
_QtechDot11WIDSSuspiciousAPIgnoredTag_Type = TruthValue
_QtechDot11WIDSSuspiciousAPIgnoredTag_Object = MibTableColumn
qtechDot11WIDSSuspiciousAPIgnoredTag = _QtechDot11WIDSSuspiciousAPIgnoredTag_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 62, 1, 27, 1, 10),
    _QtechDot11WIDSSuspiciousAPIgnoredTag_Type()
)
qtechDot11WIDSSuspiciousAPIgnoredTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechDot11WIDSSuspiciousAPIgnoredTag.setStatus("current")
_QtechDot11WIDSSuspiciousSTAInfoTable_Object = MibTable
qtechDot11WIDSSuspiciousSTAInfoTable = _QtechDot11WIDSSuspiciousSTAInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 62, 1, 28)
)
if mibBuilder.loadTexts:
    qtechDot11WIDSSuspiciousSTAInfoTable.setStatus("current")
_QtechDot11WIDSSuspiciousSTAInfoEntry_Object = MibTableRow
qtechDot11WIDSSuspiciousSTAInfoEntry = _QtechDot11WIDSSuspiciousSTAInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 62, 1, 28, 1)
)
qtechDot11WIDSSuspiciousSTAInfoEntry.setIndexNames(
    (0, "QTECH-DOT11-WIDS-MIB", "qtechDot11WIDSSuspiciousSTAMAC"),
)
if mibBuilder.loadTexts:
    qtechDot11WIDSSuspiciousSTAInfoEntry.setStatus("current")
_QtechDot11WIDSSuspiciousSTAMAC_Type = MacAddress
_QtechDot11WIDSSuspiciousSTAMAC_Object = MibTableColumn
qtechDot11WIDSSuspiciousSTAMAC = _QtechDot11WIDSSuspiciousSTAMAC_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 62, 1, 28, 1, 1),
    _QtechDot11WIDSSuspiciousSTAMAC_Type()
)
qtechDot11WIDSSuspiciousSTAMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechDot11WIDSSuspiciousSTAMAC.setStatus("current")
_QtechDot11WIDSAPCountDetectingSuspiciousSTA_Type = Integer32
_QtechDot11WIDSAPCountDetectingSuspiciousSTA_Object = MibTableColumn
qtechDot11WIDSAPCountDetectingSuspiciousSTA = _QtechDot11WIDSAPCountDetectingSuspiciousSTA_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 62, 1, 28, 1, 2),
    _QtechDot11WIDSAPCountDetectingSuspiciousSTA_Type()
)
qtechDot11WIDSAPCountDetectingSuspiciousSTA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechDot11WIDSAPCountDetectingSuspiciousSTA.setStatus("current")
_QtechDot11WIDSMomentFirstTimeDetectedSusSTA_Type = TimeTicks
_QtechDot11WIDSMomentFirstTimeDetectedSusSTA_Object = MibTableColumn
qtechDot11WIDSMomentFirstTimeDetectedSusSTA = _QtechDot11WIDSMomentFirstTimeDetectedSusSTA_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 62, 1, 28, 1, 3),
    _QtechDot11WIDSMomentFirstTimeDetectedSusSTA_Type()
)
qtechDot11WIDSMomentFirstTimeDetectedSusSTA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechDot11WIDSMomentFirstTimeDetectedSusSTA.setStatus("current")
_QtechDot11WIDSMomentLastTimeDetectedSusSTA_Type = TimeTicks
_QtechDot11WIDSMomentLastTimeDetectedSusSTA_Object = MibTableColumn
qtechDot11WIDSMomentLastTimeDetectedSusSTA = _QtechDot11WIDSMomentLastTimeDetectedSusSTA_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 62, 1, 28, 1, 4),
    _QtechDot11WIDSMomentLastTimeDetectedSusSTA_Type()
)
qtechDot11WIDSMomentLastTimeDetectedSusSTA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechDot11WIDSMomentLastTimeDetectedSusSTA.setStatus("current")
_QtechDot11WIDSBSSIDSuspiciousSTAAccessing_Type = MacAddress
_QtechDot11WIDSBSSIDSuspiciousSTAAccessing_Object = MibTableColumn
qtechDot11WIDSBSSIDSuspiciousSTAAccessing = _QtechDot11WIDSBSSIDSuspiciousSTAAccessing_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 62, 1, 28, 1, 5),
    _QtechDot11WIDSBSSIDSuspiciousSTAAccessing_Type()
)
qtechDot11WIDSBSSIDSuspiciousSTAAccessing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechDot11WIDSBSSIDSuspiciousSTAAccessing.setStatus("current")
_QtechDot11WIDSSuspiciousSTAMaxSignalStrength_Type = Integer32
_QtechDot11WIDSSuspiciousSTAMaxSignalStrength_Object = MibTableColumn
qtechDot11WIDSSuspiciousSTAMaxSignalStrength = _QtechDot11WIDSSuspiciousSTAMaxSignalStrength_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 62, 1, 28, 1, 6),
    _QtechDot11WIDSSuspiciousSTAMaxSignalStrength_Type()
)
qtechDot11WIDSSuspiciousSTAMaxSignalStrength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechDot11WIDSSuspiciousSTAMaxSignalStrength.setStatus("current")
_QtechDot11WIDSSuspiciousSTAUsingChannel_Type = Integer32
_QtechDot11WIDSSuspiciousSTAUsingChannel_Object = MibTableColumn
qtechDot11WIDSSuspiciousSTAUsingChannel = _QtechDot11WIDSSuspiciousSTAUsingChannel_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 62, 1, 28, 1, 7),
    _QtechDot11WIDSSuspiciousSTAUsingChannel_Type()
)
qtechDot11WIDSSuspiciousSTAUsingChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechDot11WIDSSuspiciousSTAUsingChannel.setStatus("current")
_QtechDot11WIDSSuspiciousSTAWorksInAdhocMode_Type = TruthValue
_QtechDot11WIDSSuspiciousSTAWorksInAdhocMode_Object = MibTableColumn
qtechDot11WIDSSuspiciousSTAWorksInAdhocMode = _QtechDot11WIDSSuspiciousSTAWorksInAdhocMode_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 62, 1, 28, 1, 8),
    _QtechDot11WIDSSuspiciousSTAWorksInAdhocMode_Type()
)
qtechDot11WIDSSuspiciousSTAWorksInAdhocMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechDot11WIDSSuspiciousSTAWorksInAdhocMode.setStatus("current")
_QtechDot11WIDSSuspiciousSTANeedsDealingTag_Type = TruthValue
_QtechDot11WIDSSuspiciousSTANeedsDealingTag_Object = MibTableColumn
qtechDot11WIDSSuspiciousSTANeedsDealingTag = _QtechDot11WIDSSuspiciousSTANeedsDealingTag_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 62, 1, 28, 1, 9),
    _QtechDot11WIDSSuspiciousSTANeedsDealingTag_Type()
)
qtechDot11WIDSSuspiciousSTANeedsDealingTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechDot11WIDSSuspiciousSTANeedsDealingTag.setStatus("current")
_QtechDot11WIDSSuspiciousSTAIgnoredTag_Type = TruthValue
_QtechDot11WIDSSuspiciousSTAIgnoredTag_Object = MibTableColumn
qtechDot11WIDSSuspiciousSTAIgnoredTag = _QtechDot11WIDSSuspiciousSTAIgnoredTag_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 62, 1, 28, 1, 10),
    _QtechDot11WIDSSuspiciousSTAIgnoredTag_Type()
)
qtechDot11WIDSSuspiciousSTAIgnoredTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechDot11WIDSSuspiciousSTAIgnoredTag.setStatus("current")
_QtechDot11WIDSDetectObjects_ObjectIdentity = ObjectIdentity
qtechDot11WIDSDetectObjects = _QtechDot11WIDSDetectObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 62, 2)
)
_QtechDot11WIDSShowDot11IdsAttacklistTable_Object = MibTable
qtechDot11WIDSShowDot11IdsAttacklistTable = _QtechDot11WIDSShowDot11IdsAttacklistTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 62, 2, 1)
)
if mibBuilder.loadTexts:
    qtechDot11WIDSShowDot11IdsAttacklistTable.setStatus("current")
_QtechDot11WIDSShowDot11IdsAttacklistEntry_Object = MibTableRow
qtechDot11WIDSShowDot11IdsAttacklistEntry = _QtechDot11WIDSShowDot11IdsAttacklistEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 62, 2, 1, 1)
)
qtechDot11WIDSShowDot11IdsAttacklistEntry.setIndexNames(
    (0, "QTECH-DOT11-WIDS-MIB", "qtechDot11WIDSShowDot11IdsAttacklistNum"),
)
if mibBuilder.loadTexts:
    qtechDot11WIDSShowDot11IdsAttacklistEntry.setStatus("current")
_QtechDot11WIDSShowDot11IdsAttacklistNum_Type = Integer32
_QtechDot11WIDSShowDot11IdsAttacklistNum_Object = MibTableColumn
qtechDot11WIDSShowDot11IdsAttacklistNum = _QtechDot11WIDSShowDot11IdsAttacklistNum_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 62, 2, 1, 1, 1),
    _QtechDot11WIDSShowDot11IdsAttacklistNum_Type()
)
qtechDot11WIDSShowDot11IdsAttacklistNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qtechDot11WIDSShowDot11IdsAttacklistNum.setStatus("current")
_QtechDot11WIDSShowDot11IdsAttacklistOper_Type = Integer32
_QtechDot11WIDSShowDot11IdsAttacklistOper_Object = MibTableColumn
qtechDot11WIDSShowDot11IdsAttacklistOper = _QtechDot11WIDSShowDot11IdsAttacklistOper_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 62, 2, 1, 1, 2),
    _QtechDot11WIDSShowDot11IdsAttacklistOper_Type()
)
qtechDot11WIDSShowDot11IdsAttacklistOper.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechDot11WIDSShowDot11IdsAttacklistOper.setStatus("current")
_QtechDot11WIDSShowDot11IdsAttacklistMac_Type = MacAddress
_QtechDot11WIDSShowDot11IdsAttacklistMac_Object = MibTableColumn
qtechDot11WIDSShowDot11IdsAttacklistMac = _QtechDot11WIDSShowDot11IdsAttacklistMac_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 62, 2, 1, 1, 3),
    _QtechDot11WIDSShowDot11IdsAttacklistMac_Type()
)
qtechDot11WIDSShowDot11IdsAttacklistMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechDot11WIDSShowDot11IdsAttacklistMac.setStatus("current")


class _QtechDot11WIDSShowDot11IdsAttacklistInfo_Type(DisplayString):
    """Custom type qtechDot11WIDSShowDot11IdsAttacklistInfo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_QtechDot11WIDSShowDot11IdsAttacklistInfo_Type.__name__ = "DisplayString"
_QtechDot11WIDSShowDot11IdsAttacklistInfo_Object = MibTableColumn
qtechDot11WIDSShowDot11IdsAttacklistInfo = _QtechDot11WIDSShowDot11IdsAttacklistInfo_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 62, 2, 1, 1, 4),
    _QtechDot11WIDSShowDot11IdsAttacklistInfo_Type()
)
qtechDot11WIDSShowDot11IdsAttacklistInfo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechDot11WIDSShowDot11IdsAttacklistInfo.setStatus("current")
_QtechDot11WIDSTrapsObjects_ObjectIdentity = ObjectIdentity
qtechDot11WIDSTrapsObjects = _QtechDot11WIDSTrapsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 62, 3)
)
_QtechDot11WIDSSTAMAC_Type = MacAddress
_QtechDot11WIDSSTAMAC_Object = MibScalar
qtechDot11WIDSSTAMAC = _QtechDot11WIDSSTAMAC_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 62, 3, 1),
    _QtechDot11WIDSSTAMAC_Type()
)
qtechDot11WIDSSTAMAC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechDot11WIDSSTAMAC.setStatus("current")


class _QtechDot11WIDSAPBSSID_Type(DisplayString):
    """Custom type qtechDot11WIDSAPBSSID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_QtechDot11WIDSAPBSSID_Type.__name__ = "DisplayString"
_QtechDot11WIDSAPBSSID_Object = MibScalar
qtechDot11WIDSAPBSSID = _QtechDot11WIDSAPBSSID_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 62, 3, 2),
    _QtechDot11WIDSAPBSSID_Type()
)
qtechDot11WIDSAPBSSID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechDot11WIDSAPBSSID.setStatus("current")


class _QtechDot11WIDSInformation_Type(DisplayString):
    """Custom type qtechDot11WIDSInformation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_QtechDot11WIDSInformation_Type.__name__ = "DisplayString"
_QtechDot11WIDSInformation_Object = MibScalar
qtechDot11WIDSInformation = _QtechDot11WIDSInformation_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 62, 3, 3),
    _QtechDot11WIDSInformation_Type()
)
qtechDot11WIDSInformation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechDot11WIDSInformation.setStatus("current")


class _QtechDot11WIDSextinfo_Type(DisplayString):
    """Custom type qtechDot11WIDSextinfo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_QtechDot11WIDSextinfo_Type.__name__ = "DisplayString"
_QtechDot11WIDSextinfo_Object = MibScalar
qtechDot11WIDSextinfo = _QtechDot11WIDSextinfo_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 62, 3, 4),
    _QtechDot11WIDSextinfo_Type()
)
qtechDot11WIDSextinfo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechDot11WIDSextinfo.setStatus("current")
_QtechDot11WIDSDeviceInfoNUM_Type = Integer32
_QtechDot11WIDSDeviceInfoNUM_Object = MibScalar
qtechDot11WIDSDeviceInfoNUM = _QtechDot11WIDSDeviceInfoNUM_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 62, 3, 5),
    _QtechDot11WIDSDeviceInfoNUM_Type()
)
qtechDot11WIDSDeviceInfoNUM.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechDot11WIDSDeviceInfoNUM.setStatus("current")
_QtechDot11WIDSDeviceInfoTYPE_Type = Integer32
_QtechDot11WIDSDeviceInfoTYPE_Object = MibScalar
qtechDot11WIDSDeviceInfoTYPE = _QtechDot11WIDSDeviceInfoTYPE_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 62, 3, 6),
    _QtechDot11WIDSDeviceInfoTYPE_Type()
)
qtechDot11WIDSDeviceInfoTYPE.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechDot11WIDSDeviceInfoTYPE.setStatus("current")
_QtechDot11WIDSDeviceInfoOper_Type = Integer32
_QtechDot11WIDSDeviceInfoOper_Object = MibScalar
qtechDot11WIDSDeviceInfoOper = _QtechDot11WIDSDeviceInfoOper_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 62, 3, 7),
    _QtechDot11WIDSDeviceInfoOper_Type()
)
qtechDot11WIDSDeviceInfoOper.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechDot11WIDSDeviceInfoOper.setStatus("current")
_QtechDot11WIDSDeviceInfoMAC_Type = MacAddress
_QtechDot11WIDSDeviceInfoMAC_Object = MibScalar
qtechDot11WIDSDeviceInfoMAC = _QtechDot11WIDSDeviceInfoMAC_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 62, 3, 8),
    _QtechDot11WIDSDeviceInfoMAC_Type()
)
qtechDot11WIDSDeviceInfoMAC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechDot11WIDSDeviceInfoMAC.setStatus("current")


class _QtechDot11WIDSDeviceInfoString_Type(DisplayString):
    """Custom type qtechDot11WIDSDeviceInfoString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_QtechDot11WIDSDeviceInfoString_Type.__name__ = "DisplayString"
_QtechDot11WIDSDeviceInfoString_Object = MibScalar
qtechDot11WIDSDeviceInfoString = _QtechDot11WIDSDeviceInfoString_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 62, 3, 9),
    _QtechDot11WIDSDeviceInfoString_Type()
)
qtechDot11WIDSDeviceInfoString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechDot11WIDSDeviceInfoString.setStatus("current")
_QtechDot11WIDSSuspiciousDeviceMac_Type = MacAddress
_QtechDot11WIDSSuspiciousDeviceMac_Object = MibScalar
qtechDot11WIDSSuspiciousDeviceMac = _QtechDot11WIDSSuspiciousDeviceMac_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 62, 3, 10),
    _QtechDot11WIDSSuspiciousDeviceMac_Type()
)
qtechDot11WIDSSuspiciousDeviceMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechDot11WIDSSuspiciousDeviceMac.setStatus("current")
_QtechDot11WIDSSuspiciousDeviceExtensionInfo_Type = DisplayString
_QtechDot11WIDSSuspiciousDeviceExtensionInfo_Object = MibScalar
qtechDot11WIDSSuspiciousDeviceExtensionInfo = _QtechDot11WIDSSuspiciousDeviceExtensionInfo_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 62, 3, 11),
    _QtechDot11WIDSSuspiciousDeviceExtensionInfo_Type()
)
qtechDot11WIDSSuspiciousDeviceExtensionInfo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechDot11WIDSSuspiciousDeviceExtensionInfo.setStatus("current")
_QtechDot11WIDSUnauthorizedSSID_Type = DisplayString
_QtechDot11WIDSUnauthorizedSSID_Object = MibScalar
qtechDot11WIDSUnauthorizedSSID = _QtechDot11WIDSUnauthorizedSSID_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 62, 3, 12),
    _QtechDot11WIDSUnauthorizedSSID_Type()
)
qtechDot11WIDSUnauthorizedSSID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechDot11WIDSUnauthorizedSSID.setStatus("current")
_QtechDot11WIDSSUnauthorizedSSIDExtensionInfo_Type = DisplayString
_QtechDot11WIDSSUnauthorizedSSIDExtensionInfo_Object = MibScalar
qtechDot11WIDSSUnauthorizedSSIDExtensionInfo = _QtechDot11WIDSSUnauthorizedSSIDExtensionInfo_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 62, 3, 13),
    _QtechDot11WIDSSUnauthorizedSSIDExtensionInfo_Type()
)
qtechDot11WIDSSUnauthorizedSSIDExtensionInfo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechDot11WIDSSUnauthorizedSSIDExtensionInfo.setStatus("current")
_QtechDot11WIDSAttackingDeviceMac_Type = MacAddress
_QtechDot11WIDSAttackingDeviceMac_Object = MibScalar
qtechDot11WIDSAttackingDeviceMac = _QtechDot11WIDSAttackingDeviceMac_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 62, 3, 14),
    _QtechDot11WIDSAttackingDeviceMac_Type()
)
qtechDot11WIDSAttackingDeviceMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechDot11WIDSAttackingDeviceMac.setStatus("current")
_QtechDot11WIDSAttackType_Type = Integer32
_QtechDot11WIDSAttackType_Object = MibScalar
qtechDot11WIDSAttackType = _QtechDot11WIDSAttackType_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 62, 3, 15),
    _QtechDot11WIDSAttackType_Type()
)
qtechDot11WIDSAttackType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechDot11WIDSAttackType.setStatus("current")
_QtechDot11WIDSAttackExtensionInfo_Type = DisplayString
_QtechDot11WIDSAttackExtensionInfo_Object = MibScalar
qtechDot11WIDSAttackExtensionInfo = _QtechDot11WIDSAttackExtensionInfo_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 62, 3, 16),
    _QtechDot11WIDSAttackExtensionInfo_Type()
)
qtechDot11WIDSAttackExtensionInfo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechDot11WIDSAttackExtensionInfo.setStatus("current")
_QtechDot11WIDSMIBConform_ObjectIdentity = ObjectIdentity
qtechDot11WIDSMIBConform = _QtechDot11WIDSMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 62, 4)
)
_QtechDot11WIDSMIBCompliances_ObjectIdentity = ObjectIdentity
qtechDot11WIDSMIBCompliances = _QtechDot11WIDSMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 62, 4, 1)
)
_QtechDot11WIDSMIBGroups_ObjectIdentity = ObjectIdentity
qtechDot11WIDSMIBGroups = _QtechDot11WIDSMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 62, 4, 2)
)

# Managed Objects groups

qtechDot11WIDSMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 62, 4, 2, 1)
)
qtechDot11WIDSMIBGroup.setObjects(
      *(("QTECH-DOT11-WIDS-MIB", "qtechDot11VendorOper"),
        ("QTECH-DOT11-WIDS-MIB", "qtechDot11VendorName"),
        ("QTECH-DOT11-WIDS-MIB", "qtechDot11PermitOper"),
        ("QTECH-DOT11-WIDS-MIB", "qtechDot11PermitSSID"),
        ("QTECH-DOT11-WIDS-MIB", "qtechDot11AttackOper"),
        ("QTECH-DOT11-WIDS-MIB", "qtechDot11AttackMAC"),
        ("QTECH-DOT11-WIDS-MIB", "qtechDot11AttackInfo"),
        ("QTECH-DOT11-WIDS-MIB", "qtechDot11PermitMACOper"),
        ("QTECH-DOT11-WIDS-MIB", "qtechDot11PermitMACAddr"),
        ("QTECH-DOT11-WIDS-MIB", "qtechDot11WIDSDeviceagingDuration"),
        ("QTECH-DOT11-WIDS-MIB", "qtechDot11WIDSCountermeasuresMode"),
        ("QTECH-DOT11-WIDS-MIB", "qtechDot11WIDSCountermeasureSet"),
        ("QTECH-DOT11-WIDS-MIB", "qtechDot11WIDSDeviceMode"),
        ("QTECH-DOT11-WIDS-MIB", "qtechDot11WhitelistOper"),
        ("QTECH-DOT11-WIDS-MIB", "qtechDot11WhitelistMAC"),
        ("QTECH-DOT11-WIDS-MIB", "qtechDot11StaticblacklistOper"),
        ("QTECH-DOT11-WIDS-MIB", "qtechDot11StaticblacklistMAC"),
        ("QTECH-DOT11-WIDS-MIB", "qtechDot11WIDSDynamicblacklistEnable"),
        ("QTECH-DOT11-WIDS-MIB", "qtechDot11WIDSDynamicblacklistLifetime"),
        ("QTECH-DOT11-WIDS-MIB", "qtechDot11WIDSAttackDetectionMode"),
        ("QTECH-DOT11-WIDS-MIB", "qtechDot11WIDSRogueInfoOper"),
        ("QTECH-DOT11-WIDS-MIB", "qtechDot11WIDSRogueInfoMAC"),
        ("QTECH-DOT11-WIDS-MIB", "qtechDot11WIDSRogueInfoString"),
        ("QTECH-DOT11-WIDS-MIB", "qtechDot11WIDSEnableVlanPermitmaclistOper"),
        ("QTECH-DOT11-WIDS-MIB", "qtechDot11WIDSEnableVlanPermitmaclist"),
        ("QTECH-DOT11-WIDS-MIB", "qtechDot11WIDSResetStatistics"),
        ("QTECH-DOT11-WIDS-MIB", "qtechDot11WIDSResetRoguehistoryStatistics"),
        ("QTECH-DOT11-WIDS-MIB", "qtechDot11WIDSResethistory"),
        ("QTECH-DOT11-WIDS-MIB", "qtechDot11WIDSResetDynamicBlacklistType"),
        ("QTECH-DOT11-WIDS-MIB", "qtechDot11WIDResetUserisolationStatistics"),
        ("QTECH-DOT11-WIDS-MIB", "qtechDot11WIDSShowDot11IdsAttacklistOper"),
        ("QTECH-DOT11-WIDS-MIB", "qtechDot11WIDSShowDot11IdsAttacklistMac"),
        ("QTECH-DOT11-WIDS-MIB", "qtechDot11WIDSShowDot11IdsAttacklistInfo"),
        ("QTECH-DOT11-WIDS-MIB", "qtechDot11WIDUserisolationAC"),
        ("QTECH-DOT11-WIDS-MIB", "qtechDot11WIDUserisolationAP"),
        ("QTECH-DOT11-WIDS-MIB", "qtechDot11WIDSShowStaticsOper"),
        ("QTECH-DOT11-WIDS-MIB", "qtechDot11WIDSShowStaticsMac"),
        ("QTECH-DOT11-WIDS-MIB", "qtechDot11WIDSShowStaticsInfo"),
        ("QTECH-DOT11-WIDS-MIB", "qtechDot11WIDSAssociationFailureTotalTimes"),
        ("QTECH-DOT11-WIDS-MIB", "qtechDot11WIDSSuspiciousAPCount"),
        ("QTECH-DOT11-WIDS-MIB", "qtechDot11WIDSMomentFirstTimeDetectedSusAP"),
        ("QTECH-DOT11-WIDS-MIB", "qtechDot11WIDSMomentLastTimeDetectedSusAP"),
        ("QTECH-DOT11-WIDS-MIB", "qtechDot11WIDSSuspiciousAPSSID"),
        ("QTECH-DOT11-WIDS-MIB", "qtechDot11WIDSSuspiciousAPMaxSignalStrength"),
        ("QTECH-DOT11-WIDS-MIB", "qtechDot11WIDSSuspiciousAPUsingChannel"),
        ("QTECH-DOT11-WIDS-MIB", "qtechDot11WIDSSuspiciousAPFrameEncrption"),
        ("QTECH-DOT11-WIDS-MIB", "qtechDot11WIDSSuspiciousAPNeedsDealingTag"),
        ("QTECH-DOT11-WIDS-MIB", "qtechDot11WIDSSuspiciousAPIgnoredTag"),
        ("QTECH-DOT11-WIDS-MIB", "qtechDot11WIDSAPCountDetectingSuspiciousSTA"),
        ("QTECH-DOT11-WIDS-MIB", "qtechDot11WIDSMomentFirstTimeDetectedSusSTA"),
        ("QTECH-DOT11-WIDS-MIB", "qtechDot11WIDSMomentLastTimeDetectedSusSTA"),
        ("QTECH-DOT11-WIDS-MIB", "qtechDot11WIDSBSSIDSuspiciousSTAAccessing"),
        ("QTECH-DOT11-WIDS-MIB", "qtechDot11WIDSSuspiciousSTAMaxSignalStrength"),
        ("QTECH-DOT11-WIDS-MIB", "qtechDot11WIDSSuspiciousSTAUsingChannel"),
        ("QTECH-DOT11-WIDS-MIB", "qtechDot11WIDSSuspiciousSTAWorksInAdhocMode"),
        ("QTECH-DOT11-WIDS-MIB", "qtechDot11WIDSSuspiciousSTANeedsDealingTag"),
        ("QTECH-DOT11-WIDS-MIB", "qtechDot11WIDSSuspiciousSTAIgnoredTag"),
        ("QTECH-DOT11-WIDS-MIB", "qtechDot11WIDSSuspiciousDeviceMac"),
        ("QTECH-DOT11-WIDS-MIB", "qtechDot11WIDSSuspiciousDeviceExtensionInfo"),
        ("QTECH-DOT11-WIDS-MIB", "qtechDot11WIDSUnauthorizedSSID"),
        ("QTECH-DOT11-WIDS-MIB", "qtechDot11WIDSSUnauthorizedSSIDExtensionInfo"),
        ("QTECH-DOT11-WIDS-MIB", "qtechDot11WIDSAttackingDeviceMac"),
        ("QTECH-DOT11-WIDS-MIB", "qtechDot11WIDSAttackType"),
        ("QTECH-DOT11-WIDS-MIB", "qtechDot11WIDSAttackExtensionInfo"),
        ("QTECH-DOT11-WIDS-MIB", "qtechDot11WIDSSTAMAC"),
        ("QTECH-DOT11-WIDS-MIB", "qtechDot11WIDSAPBSSID"),
        ("QTECH-DOT11-WIDS-MIB", "qtechDot11WIDSInformation"),
        ("QTECH-DOT11-WIDS-MIB", "qtechDot11WIDSextinfo"),
        ("QTECH-DOT11-WIDS-MIB", "qtechDot11WIDSDeviceInfoNUM"),
        ("QTECH-DOT11-WIDS-MIB", "qtechDot11WIDSDeviceInfoTYPE"),
        ("QTECH-DOT11-WIDS-MIB", "qtechDot11WIDSDeviceInfoOper"),
        ("QTECH-DOT11-WIDS-MIB", "qtechDot11WIDSDeviceInfoMAC"),
        ("QTECH-DOT11-WIDS-MIB", "qtechDot11WIDSDeviceInfoString"))
)
if mibBuilder.loadTexts:
    qtechDot11WIDSMIBGroup.setStatus("current")


# Notification objects

qtechDot11WIDSWirelessUserConnect = NotificationType(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 62, 0, 1)
)
qtechDot11WIDSWirelessUserConnect.setObjects(
      *(("QTECH-DOT11-WIDS-MIB", "qtechDot11WIDSSTAMAC"),
        ("QTECH-DOT11-WIDS-MIB", "qtechDot11WIDSAPBSSID"),
        ("QTECH-DOT11-WIDS-MIB", "qtechDot11WIDSInformation"),
        ("QTECH-DOT11-WIDS-MIB", "qtechDot11WIDSextinfo"))
)
if mibBuilder.loadTexts:
    qtechDot11WIDSWirelessUserConnect.setStatus(
        "current"
    )

qtechDot11WIDSWirelessUserDisconnect = NotificationType(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 62, 0, 2)
)
qtechDot11WIDSWirelessUserDisconnect.setObjects(
      *(("QTECH-DOT11-WIDS-MIB", "qtechDot11WIDSSTAMAC"),
        ("QTECH-DOT11-WIDS-MIB", "qtechDot11WIDSAPBSSID"),
        ("QTECH-DOT11-WIDS-MIB", "qtechDot11WIDSInformation"),
        ("QTECH-DOT11-WIDS-MIB", "qtechDot11WIDSextinfo"))
)
if mibBuilder.loadTexts:
    qtechDot11WIDSWirelessUserDisconnect.setStatus(
        "current"
    )

qtechDot11WIDSWirelessUserReauthentication = NotificationType(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 62, 0, 3)
)
qtechDot11WIDSWirelessUserReauthentication.setObjects(
      *(("QTECH-DOT11-WIDS-MIB", "qtechDot11WIDSSTAMAC"),
        ("QTECH-DOT11-WIDS-MIB", "qtechDot11WIDSAPBSSID"),
        ("QTECH-DOT11-WIDS-MIB", "qtechDot11WIDSInformation"),
        ("QTECH-DOT11-WIDS-MIB", "qtechDot11WIDSextinfo"))
)
if mibBuilder.loadTexts:
    qtechDot11WIDSWirelessUserReauthentication.setStatus(
        "current"
    )

qtechDot11WIDSWirelessUserAuthenticationFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 62, 0, 4)
)
qtechDot11WIDSWirelessUserAuthenticationFailure.setObjects(
      *(("QTECH-DOT11-WIDS-MIB", "qtechDot11WIDSSTAMAC"),
        ("QTECH-DOT11-WIDS-MIB", "qtechDot11WIDSAPBSSID"),
        ("QTECH-DOT11-WIDS-MIB", "qtechDot11WIDSInformation"),
        ("QTECH-DOT11-WIDS-MIB", "qtechDot11WIDSextinfo"))
)
if mibBuilder.loadTexts:
    qtechDot11WIDSWirelessUserAuthenticationFailure.setStatus(
        "current"
    )

qtechDot11WIDSWirelessUserConnectFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 62, 0, 5)
)
qtechDot11WIDSWirelessUserConnectFailure.setObjects(
      *(("QTECH-DOT11-WIDS-MIB", "qtechDot11WIDSSTAMAC"),
        ("QTECH-DOT11-WIDS-MIB", "qtechDot11WIDSAPBSSID"),
        ("QTECH-DOT11-WIDS-MIB", "qtechDot11WIDSInformation"),
        ("QTECH-DOT11-WIDS-MIB", "qtechDot11WIDSextinfo"))
)
if mibBuilder.loadTexts:
    qtechDot11WIDSWirelessUserConnectFailure.setStatus(
        "current"
    )

qtechDot11WIDSDevice = NotificationType(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 62, 0, 6)
)
qtechDot11WIDSDevice.setObjects(
      *(("QTECH-DOT11-WIDS-MIB", "qtechDot11WIDSDeviceInfoNUM"),
        ("QTECH-DOT11-WIDS-MIB", "qtechDot11WIDSDeviceInfoTYPE"),
        ("QTECH-DOT11-WIDS-MIB", "qtechDot11WIDSDeviceInfoOper"),
        ("QTECH-DOT11-WIDS-MIB", "qtechDot11WIDSDeviceInfoMAC"),
        ("QTECH-DOT11-WIDS-MIB", "qtechDot11WIDSDeviceInfoString"))
)
if mibBuilder.loadTexts:
    qtechDot11WIDSDevice.setStatus(
        "current"
    )

qtechDot11WIDSSuspiciousDeviceTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 62, 0, 7)
)
qtechDot11WIDSSuspiciousDeviceTrap.setObjects(
      *(("QTECH-DOT11-WIDS-MIB", "qtechDot11WIDSSuspiciousDeviceMac"),
        ("QTECH-DOT11-WIDS-MIB", "qtechDot11WIDSSuspiciousDeviceExtensionInfo"))
)
if mibBuilder.loadTexts:
    qtechDot11WIDSSuspiciousDeviceTrap.setStatus(
        "current"
    )

qtechDot11WIDSUnauthorizedSSIDTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 62, 0, 8)
)
qtechDot11WIDSUnauthorizedSSIDTrap.setObjects(
      *(("QTECH-DOT11-WIDS-MIB", "qtechDot11WIDSUnauthorizedSSID"),
        ("QTECH-DOT11-WIDS-MIB", "qtechDot11WIDSSUnauthorizedSSIDExtensionInfo"))
)
if mibBuilder.loadTexts:
    qtechDot11WIDSUnauthorizedSSIDTrap.setStatus(
        "current"
    )

qtechDot11WIDSDetectingAttackTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 62, 0, 9)
)
qtechDot11WIDSDetectingAttackTrap.setObjects(
      *(("QTECH-DOT11-WIDS-MIB", "qtechDot11WIDSAttackingDeviceMac"),
        ("QTECH-DOT11-WIDS-MIB", "qtechDot11WIDSAttackType"),
        ("QTECH-DOT11-WIDS-MIB", "qtechDot11WIDSAttackExtensionInfo"))
)
if mibBuilder.loadTexts:
    qtechDot11WIDSDetectingAttackTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance

qtechDot11WIDSMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 62, 4, 1, 1)
)
qtechDot11WIDSMIBCompliance.setObjects(
    ("QTECH-DOT11-WIDS-MIB", "qtechDot11WIDSMIBGroup")
)
if mibBuilder.loadTexts:
    qtechDot11WIDSMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "QTECH-DOT11-WIDS-MIB",
    **{"qtechDot11WIDSMIB": qtechDot11WIDSMIB,
       "qtechDot11WIDSTraps": qtechDot11WIDSTraps,
       "qtechDot11WIDSWirelessUserConnect": qtechDot11WIDSWirelessUserConnect,
       "qtechDot11WIDSWirelessUserDisconnect": qtechDot11WIDSWirelessUserDisconnect,
       "qtechDot11WIDSWirelessUserReauthentication": qtechDot11WIDSWirelessUserReauthentication,
       "qtechDot11WIDSWirelessUserAuthenticationFailure": qtechDot11WIDSWirelessUserAuthenticationFailure,
       "qtechDot11WIDSWirelessUserConnectFailure": qtechDot11WIDSWirelessUserConnectFailure,
       "qtechDot11WIDSDevice": qtechDot11WIDSDevice,
       "qtechDot11WIDSSuspiciousDeviceTrap": qtechDot11WIDSSuspiciousDeviceTrap,
       "qtechDot11WIDSUnauthorizedSSIDTrap": qtechDot11WIDSUnauthorizedSSIDTrap,
       "qtechDot11WIDSDetectingAttackTrap": qtechDot11WIDSDetectingAttackTrap,
       "qtechDot11WIDSConfigObjects": qtechDot11WIDSConfigObjects,
       "qtechDot11WIDSPermitVendorTable": qtechDot11WIDSPermitVendorTable,
       "qtechDot11WIDSPermitVendorEntry": qtechDot11WIDSPermitVendorEntry,
       "qtechDot11VendorOUI": qtechDot11VendorOUI,
       "qtechDot11VendorOper": qtechDot11VendorOper,
       "qtechDot11VendorName": qtechDot11VendorName,
       "qtechDot11WIDSPermitSSIDTable": qtechDot11WIDSPermitSSIDTable,
       "qtechDot11WIDSPermitSSIDEntry": qtechDot11WIDSPermitSSIDEntry,
       "qtechDot11PermitNum": qtechDot11PermitNum,
       "qtechDot11PermitOper": qtechDot11PermitOper,
       "qtechDot11PermitSSID": qtechDot11PermitSSID,
       "qtechDot11WIDSDeviceAttackMacaddressListTable": qtechDot11WIDSDeviceAttackMacaddressListTable,
       "qtechDot11WIDSDeviceAttackMacaddressListEntry": qtechDot11WIDSDeviceAttackMacaddressListEntry,
       "qtechDot11AttackNum": qtechDot11AttackNum,
       "qtechDot11AttackOper": qtechDot11AttackOper,
       "qtechDot11AttackMAC": qtechDot11AttackMAC,
       "qtechDot11AttackInfo": qtechDot11AttackInfo,
       "qtechDot11WIDSDevicePermitMacaddressListTable": qtechDot11WIDSDevicePermitMacaddressListTable,
       "qtechDot11WIDSDevicePermitMacaddressListEntry": qtechDot11WIDSDevicePermitMacaddressListEntry,
       "qtechDot11PermitMACNum": qtechDot11PermitMACNum,
       "qtechDot11PermitMACOper": qtechDot11PermitMACOper,
       "qtechDot11PermitMACAddr": qtechDot11PermitMACAddr,
       "qtechDot11WIDSDeviceagingDuration": qtechDot11WIDSDeviceagingDuration,
       "qtechDot11WIDSCountermeasuresMode": qtechDot11WIDSCountermeasuresMode,
       "qtechDot11WIDSCountermeasureSet": qtechDot11WIDSCountermeasureSet,
       "qtechDot11WIDSModeTable": qtechDot11WIDSModeTable,
       "qtechDot11WIDSModeEntry": qtechDot11WIDSModeEntry,
       "qtechDot11WIDSAPID": qtechDot11WIDSAPID,
       "qtechDot11WIDSDeviceMode": qtechDot11WIDSDeviceMode,
       "qtechDot11WIDSWhitelistMacaddressListTable": qtechDot11WIDSWhitelistMacaddressListTable,
       "qtechDot11WIDSWhitelistMacaddressListEntry": qtechDot11WIDSWhitelistMacaddressListEntry,
       "qtechDot11WhitelistNum": qtechDot11WhitelistNum,
       "qtechDot11WhitelistOper": qtechDot11WhitelistOper,
       "qtechDot11WhitelistMAC": qtechDot11WhitelistMAC,
       "qtechDot11WIDSStaticblackListTable": qtechDot11WIDSStaticblackListTable,
       "qtechDot11WIDSStaticblackListEntry": qtechDot11WIDSStaticblackListEntry,
       "qtechDot11StaticblacklistNum": qtechDot11StaticblacklistNum,
       "qtechDot11StaticblacklistOper": qtechDot11StaticblacklistOper,
       "qtechDot11StaticblacklistMAC": qtechDot11StaticblacklistMAC,
       "qtechDot11WIDSDynamicblacklistEnable": qtechDot11WIDSDynamicblacklistEnable,
       "qtechDot11WIDSDynamicblacklistLifetime": qtechDot11WIDSDynamicblacklistLifetime,
       "qtechDot11WIDSAttackDetectionMode": qtechDot11WIDSAttackDetectionMode,
       "qtechDot11WIDSRogueInfoTable": qtechDot11WIDSRogueInfoTable,
       "qtechDot11WIDSRogueInfoEntry": qtechDot11WIDSRogueInfoEntry,
       "qtechDot11WIDSRogueInfoNUM": qtechDot11WIDSRogueInfoNUM,
       "qtechDot11WIDSRogueInfoTYPE": qtechDot11WIDSRogueInfoTYPE,
       "qtechDot11WIDSRogueInfoOper": qtechDot11WIDSRogueInfoOper,
       "qtechDot11WIDSRogueInfoMAC": qtechDot11WIDSRogueInfoMAC,
       "qtechDot11WIDSRogueInfoString": qtechDot11WIDSRogueInfoString,
       "qtechDot11WIDSPermitmaclistEnableTable": qtechDot11WIDSPermitmaclistEnableTable,
       "qtechDot11WIDSPermitmaclistEnableEntry": qtechDot11WIDSPermitmaclistEnableEntry,
       "qtechDot11WIDSEnableVlanPermitmaclistNum": qtechDot11WIDSEnableVlanPermitmaclistNum,
       "qtechDot11WIDSEnableVlanPermitmaclistOper": qtechDot11WIDSEnableVlanPermitmaclistOper,
       "qtechDot11WIDSEnableVlanPermitmaclist": qtechDot11WIDSEnableVlanPermitmaclist,
       "qtechDot11WIDSResetStatistics": qtechDot11WIDSResetStatistics,
       "qtechDot11WIDSResetRoguehistoryStatistics": qtechDot11WIDSResetRoguehistoryStatistics,
       "qtechDot11WIDSResethistory": qtechDot11WIDSResethistory,
       "qtechDot11WIDSResetDynamicBlacklistTable": qtechDot11WIDSResetDynamicBlacklistTable,
       "qtechDot11WIDSResetDynamicBlacklistEntry": qtechDot11WIDSResetDynamicBlacklistEntry,
       "qtechDot11WIDSResetDynamicBlacklistMac": qtechDot11WIDSResetDynamicBlacklistMac,
       "qtechDot11WIDSResetDynamicBlacklistType": qtechDot11WIDSResetDynamicBlacklistType,
       "qtechDot11WIDResetUserisolationStatistics": qtechDot11WIDResetUserisolationStatistics,
       "qtechDot11WIDUserisolationAC": qtechDot11WIDUserisolationAC,
       "qtechDot11WIDUserisolationAP": qtechDot11WIDUserisolationAP,
       "qtechDot11WIDSShowStaticsTable": qtechDot11WIDSShowStaticsTable,
       "qtechDot11WIDSShowStaticsEntry": qtechDot11WIDSShowStaticsEntry,
       "qtechDot11WIDSShowStaticsNum": qtechDot11WIDSShowStaticsNum,
       "qtechDot11WIDSShowStaticsOper": qtechDot11WIDSShowStaticsOper,
       "qtechDot11WIDSShowStaticsMac": qtechDot11WIDSShowStaticsMac,
       "qtechDot11WIDSShowStaticsInfo": qtechDot11WIDSShowStaticsInfo,
       "qtechDot11WIDSAssociationFailureTotalTimes": qtechDot11WIDSAssociationFailureTotalTimes,
       "qtechDot11WIDSSuspiciousAPInfoTable": qtechDot11WIDSSuspiciousAPInfoTable,
       "qtechDot11WIDSSuspiciousAPInfoEntry": qtechDot11WIDSSuspiciousAPInfoEntry,
       "qtechDot11WIDSSuspiciousAPBSS": qtechDot11WIDSSuspiciousAPBSS,
       "qtechDot11WIDSSuspiciousAPCount": qtechDot11WIDSSuspiciousAPCount,
       "qtechDot11WIDSMomentFirstTimeDetectedSusAP": qtechDot11WIDSMomentFirstTimeDetectedSusAP,
       "qtechDot11WIDSMomentLastTimeDetectedSusAP": qtechDot11WIDSMomentLastTimeDetectedSusAP,
       "qtechDot11WIDSSuspiciousAPSSID": qtechDot11WIDSSuspiciousAPSSID,
       "qtechDot11WIDSSuspiciousAPMaxSignalStrength": qtechDot11WIDSSuspiciousAPMaxSignalStrength,
       "qtechDot11WIDSSuspiciousAPUsingChannel": qtechDot11WIDSSuspiciousAPUsingChannel,
       "qtechDot11WIDSSuspiciousAPFrameEncrption": qtechDot11WIDSSuspiciousAPFrameEncrption,
       "qtechDot11WIDSSuspiciousAPNeedsDealingTag": qtechDot11WIDSSuspiciousAPNeedsDealingTag,
       "qtechDot11WIDSSuspiciousAPIgnoredTag": qtechDot11WIDSSuspiciousAPIgnoredTag,
       "qtechDot11WIDSSuspiciousSTAInfoTable": qtechDot11WIDSSuspiciousSTAInfoTable,
       "qtechDot11WIDSSuspiciousSTAInfoEntry": qtechDot11WIDSSuspiciousSTAInfoEntry,
       "qtechDot11WIDSSuspiciousSTAMAC": qtechDot11WIDSSuspiciousSTAMAC,
       "qtechDot11WIDSAPCountDetectingSuspiciousSTA": qtechDot11WIDSAPCountDetectingSuspiciousSTA,
       "qtechDot11WIDSMomentFirstTimeDetectedSusSTA": qtechDot11WIDSMomentFirstTimeDetectedSusSTA,
       "qtechDot11WIDSMomentLastTimeDetectedSusSTA": qtechDot11WIDSMomentLastTimeDetectedSusSTA,
       "qtechDot11WIDSBSSIDSuspiciousSTAAccessing": qtechDot11WIDSBSSIDSuspiciousSTAAccessing,
       "qtechDot11WIDSSuspiciousSTAMaxSignalStrength": qtechDot11WIDSSuspiciousSTAMaxSignalStrength,
       "qtechDot11WIDSSuspiciousSTAUsingChannel": qtechDot11WIDSSuspiciousSTAUsingChannel,
       "qtechDot11WIDSSuspiciousSTAWorksInAdhocMode": qtechDot11WIDSSuspiciousSTAWorksInAdhocMode,
       "qtechDot11WIDSSuspiciousSTANeedsDealingTag": qtechDot11WIDSSuspiciousSTANeedsDealingTag,
       "qtechDot11WIDSSuspiciousSTAIgnoredTag": qtechDot11WIDSSuspiciousSTAIgnoredTag,
       "qtechDot11WIDSDetectObjects": qtechDot11WIDSDetectObjects,
       "qtechDot11WIDSShowDot11IdsAttacklistTable": qtechDot11WIDSShowDot11IdsAttacklistTable,
       "qtechDot11WIDSShowDot11IdsAttacklistEntry": qtechDot11WIDSShowDot11IdsAttacklistEntry,
       "qtechDot11WIDSShowDot11IdsAttacklistNum": qtechDot11WIDSShowDot11IdsAttacklistNum,
       "qtechDot11WIDSShowDot11IdsAttacklistOper": qtechDot11WIDSShowDot11IdsAttacklistOper,
       "qtechDot11WIDSShowDot11IdsAttacklistMac": qtechDot11WIDSShowDot11IdsAttacklistMac,
       "qtechDot11WIDSShowDot11IdsAttacklistInfo": qtechDot11WIDSShowDot11IdsAttacklistInfo,
       "qtechDot11WIDSTrapsObjects": qtechDot11WIDSTrapsObjects,
       "qtechDot11WIDSSTAMAC": qtechDot11WIDSSTAMAC,
       "qtechDot11WIDSAPBSSID": qtechDot11WIDSAPBSSID,
       "qtechDot11WIDSInformation": qtechDot11WIDSInformation,
       "qtechDot11WIDSextinfo": qtechDot11WIDSextinfo,
       "qtechDot11WIDSDeviceInfoNUM": qtechDot11WIDSDeviceInfoNUM,
       "qtechDot11WIDSDeviceInfoTYPE": qtechDot11WIDSDeviceInfoTYPE,
       "qtechDot11WIDSDeviceInfoOper": qtechDot11WIDSDeviceInfoOper,
       "qtechDot11WIDSDeviceInfoMAC": qtechDot11WIDSDeviceInfoMAC,
       "qtechDot11WIDSDeviceInfoString": qtechDot11WIDSDeviceInfoString,
       "qtechDot11WIDSSuspiciousDeviceMac": qtechDot11WIDSSuspiciousDeviceMac,
       "qtechDot11WIDSSuspiciousDeviceExtensionInfo": qtechDot11WIDSSuspiciousDeviceExtensionInfo,
       "qtechDot11WIDSUnauthorizedSSID": qtechDot11WIDSUnauthorizedSSID,
       "qtechDot11WIDSSUnauthorizedSSIDExtensionInfo": qtechDot11WIDSSUnauthorizedSSIDExtensionInfo,
       "qtechDot11WIDSAttackingDeviceMac": qtechDot11WIDSAttackingDeviceMac,
       "qtechDot11WIDSAttackType": qtechDot11WIDSAttackType,
       "qtechDot11WIDSAttackExtensionInfo": qtechDot11WIDSAttackExtensionInfo,
       "qtechDot11WIDSMIBConform": qtechDot11WIDSMIBConform,
       "qtechDot11WIDSMIBCompliances": qtechDot11WIDSMIBCompliances,
       "qtechDot11WIDSMIBCompliance": qtechDot11WIDSMIBCompliance,
       "qtechDot11WIDSMIBGroups": qtechDot11WIDSMIBGroups,
       "qtechDot11WIDSMIBGroup": qtechDot11WIDSMIBGroup}
)
