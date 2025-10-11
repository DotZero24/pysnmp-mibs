# SNMP MIB module (FS-DOT11-WIDS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/fscom/FS-DOT11-WIDS-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:14:58 2025
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

fsDot11WIDSMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 62)
)
if mibBuilder.loadTexts:
    fsDot11WIDSMIB.setRevisions(
        ("2009-04-15 09:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FsDot11WIDSTraps_ObjectIdentity = ObjectIdentity
fsDot11WIDSTraps = _FsDot11WIDSTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 62, 0)
)
_FsDot11WIDSConfigObjects_ObjectIdentity = ObjectIdentity
fsDot11WIDSConfigObjects = _FsDot11WIDSConfigObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 62, 1)
)
_FsDot11WIDSPermitVendorTable_Object = MibTable
fsDot11WIDSPermitVendorTable = _FsDot11WIDSPermitVendorTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 62, 1, 1)
)
if mibBuilder.loadTexts:
    fsDot11WIDSPermitVendorTable.setStatus("current")
_FsDot11WIDSPermitVendorEntry_Object = MibTableRow
fsDot11WIDSPermitVendorEntry = _FsDot11WIDSPermitVendorEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 62, 1, 1, 1)
)
fsDot11WIDSPermitVendorEntry.setIndexNames(
    (0, "FS-DOT11-WIDS-MIB", "fsDot11VendorOUI"),
)
if mibBuilder.loadTexts:
    fsDot11WIDSPermitVendorEntry.setStatus("current")
_FsDot11VendorOUI_Type = Integer32
_FsDot11VendorOUI_Object = MibTableColumn
fsDot11VendorOUI = _FsDot11VendorOUI_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 62, 1, 1, 1, 1),
    _FsDot11VendorOUI_Type()
)
fsDot11VendorOUI.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsDot11VendorOUI.setStatus("current")
_FsDot11VendorOper_Type = Integer32
_FsDot11VendorOper_Object = MibTableColumn
fsDot11VendorOper = _FsDot11VendorOper_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 62, 1, 1, 1, 2),
    _FsDot11VendorOper_Type()
)
fsDot11VendorOper.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot11VendorOper.setStatus("current")
_FsDot11VendorName_Type = MacAddress
_FsDot11VendorName_Object = MibTableColumn
fsDot11VendorName = _FsDot11VendorName_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 62, 1, 1, 1, 3),
    _FsDot11VendorName_Type()
)
fsDot11VendorName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot11VendorName.setStatus("current")
_FsDot11WIDSPermitSSIDTable_Object = MibTable
fsDot11WIDSPermitSSIDTable = _FsDot11WIDSPermitSSIDTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 62, 1, 2)
)
if mibBuilder.loadTexts:
    fsDot11WIDSPermitSSIDTable.setStatus("current")
_FsDot11WIDSPermitSSIDEntry_Object = MibTableRow
fsDot11WIDSPermitSSIDEntry = _FsDot11WIDSPermitSSIDEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 62, 1, 2, 1)
)
fsDot11WIDSPermitSSIDEntry.setIndexNames(
    (0, "FS-DOT11-WIDS-MIB", "fsDot11PermitNum"),
)
if mibBuilder.loadTexts:
    fsDot11WIDSPermitSSIDEntry.setStatus("current")
_FsDot11PermitNum_Type = Integer32
_FsDot11PermitNum_Object = MibTableColumn
fsDot11PermitNum = _FsDot11PermitNum_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 62, 1, 2, 1, 1),
    _FsDot11PermitNum_Type()
)
fsDot11PermitNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsDot11PermitNum.setStatus("current")
_FsDot11PermitOper_Type = Integer32
_FsDot11PermitOper_Object = MibTableColumn
fsDot11PermitOper = _FsDot11PermitOper_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 62, 1, 2, 1, 2),
    _FsDot11PermitOper_Type()
)
fsDot11PermitOper.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot11PermitOper.setStatus("current")


class _FsDot11PermitSSID_Type(DisplayString):
    """Custom type fsDot11PermitSSID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_FsDot11PermitSSID_Type.__name__ = "DisplayString"
_FsDot11PermitSSID_Object = MibTableColumn
fsDot11PermitSSID = _FsDot11PermitSSID_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 62, 1, 2, 1, 3),
    _FsDot11PermitSSID_Type()
)
fsDot11PermitSSID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot11PermitSSID.setStatus("current")
_FsDot11WIDSDeviceAttackMacaddressListTable_Object = MibTable
fsDot11WIDSDeviceAttackMacaddressListTable = _FsDot11WIDSDeviceAttackMacaddressListTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 62, 1, 3)
)
if mibBuilder.loadTexts:
    fsDot11WIDSDeviceAttackMacaddressListTable.setStatus("current")
_FsDot11WIDSDeviceAttackMacaddressListEntry_Object = MibTableRow
fsDot11WIDSDeviceAttackMacaddressListEntry = _FsDot11WIDSDeviceAttackMacaddressListEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 62, 1, 3, 1)
)
fsDot11WIDSDeviceAttackMacaddressListEntry.setIndexNames(
    (0, "FS-DOT11-WIDS-MIB", "fsDot11AttackNum"),
)
if mibBuilder.loadTexts:
    fsDot11WIDSDeviceAttackMacaddressListEntry.setStatus("current")
_FsDot11AttackNum_Type = Integer32
_FsDot11AttackNum_Object = MibTableColumn
fsDot11AttackNum = _FsDot11AttackNum_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 62, 1, 3, 1, 1),
    _FsDot11AttackNum_Type()
)
fsDot11AttackNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsDot11AttackNum.setStatus("current")
_FsDot11AttackOper_Type = Integer32
_FsDot11AttackOper_Object = MibTableColumn
fsDot11AttackOper = _FsDot11AttackOper_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 62, 1, 3, 1, 2),
    _FsDot11AttackOper_Type()
)
fsDot11AttackOper.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot11AttackOper.setStatus("current")
_FsDot11AttackMAC_Type = MacAddress
_FsDot11AttackMAC_Object = MibTableColumn
fsDot11AttackMAC = _FsDot11AttackMAC_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 62, 1, 3, 1, 3),
    _FsDot11AttackMAC_Type()
)
fsDot11AttackMAC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot11AttackMAC.setStatus("current")


class _FsDot11AttackInfo_Type(DisplayString):
    """Custom type fsDot11AttackInfo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_FsDot11AttackInfo_Type.__name__ = "DisplayString"
_FsDot11AttackInfo_Object = MibTableColumn
fsDot11AttackInfo = _FsDot11AttackInfo_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 62, 1, 3, 1, 4),
    _FsDot11AttackInfo_Type()
)
fsDot11AttackInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDot11AttackInfo.setStatus("current")
_FsDot11WIDSDevicePermitMacaddressListTable_Object = MibTable
fsDot11WIDSDevicePermitMacaddressListTable = _FsDot11WIDSDevicePermitMacaddressListTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 62, 1, 4)
)
if mibBuilder.loadTexts:
    fsDot11WIDSDevicePermitMacaddressListTable.setStatus("current")
_FsDot11WIDSDevicePermitMacaddressListEntry_Object = MibTableRow
fsDot11WIDSDevicePermitMacaddressListEntry = _FsDot11WIDSDevicePermitMacaddressListEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 62, 1, 4, 1)
)
fsDot11WIDSDevicePermitMacaddressListEntry.setIndexNames(
    (0, "FS-DOT11-WIDS-MIB", "fsDot11PermitMACNum"),
)
if mibBuilder.loadTexts:
    fsDot11WIDSDevicePermitMacaddressListEntry.setStatus("current")
_FsDot11PermitMACNum_Type = Integer32
_FsDot11PermitMACNum_Object = MibTableColumn
fsDot11PermitMACNum = _FsDot11PermitMACNum_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 62, 1, 4, 1, 1),
    _FsDot11PermitMACNum_Type()
)
fsDot11PermitMACNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsDot11PermitMACNum.setStatus("current")
_FsDot11PermitMACOper_Type = Integer32
_FsDot11PermitMACOper_Object = MibTableColumn
fsDot11PermitMACOper = _FsDot11PermitMACOper_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 62, 1, 4, 1, 2),
    _FsDot11PermitMACOper_Type()
)
fsDot11PermitMACOper.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot11PermitMACOper.setStatus("current")
_FsDot11PermitMACAddr_Type = MacAddress
_FsDot11PermitMACAddr_Object = MibTableColumn
fsDot11PermitMACAddr = _FsDot11PermitMACAddr_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 62, 1, 4, 1, 3),
    _FsDot11PermitMACAddr_Type()
)
fsDot11PermitMACAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot11PermitMACAddr.setStatus("current")
_FsDot11WIDSDeviceagingDuration_Type = Integer32
_FsDot11WIDSDeviceagingDuration_Object = MibScalar
fsDot11WIDSDeviceagingDuration = _FsDot11WIDSDeviceagingDuration_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 62, 1, 5),
    _FsDot11WIDSDeviceagingDuration_Type()
)
fsDot11WIDSDeviceagingDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot11WIDSDeviceagingDuration.setStatus("current")
_FsDot11WIDSCountermeasuresMode_Type = Integer32
_FsDot11WIDSCountermeasuresMode_Object = MibScalar
fsDot11WIDSCountermeasuresMode = _FsDot11WIDSCountermeasuresMode_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 62, 1, 6),
    _FsDot11WIDSCountermeasuresMode_Type()
)
fsDot11WIDSCountermeasuresMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot11WIDSCountermeasuresMode.setStatus("current")
_FsDot11WIDSCountermeasureSet_Type = Integer32
_FsDot11WIDSCountermeasureSet_Object = MibScalar
fsDot11WIDSCountermeasureSet = _FsDot11WIDSCountermeasureSet_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 62, 1, 7),
    _FsDot11WIDSCountermeasureSet_Type()
)
fsDot11WIDSCountermeasureSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot11WIDSCountermeasureSet.setStatus("current")
_FsDot11WIDSModeTable_Object = MibTable
fsDot11WIDSModeTable = _FsDot11WIDSModeTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 62, 1, 8)
)
if mibBuilder.loadTexts:
    fsDot11WIDSModeTable.setStatus("current")
_FsDot11WIDSModeEntry_Object = MibTableRow
fsDot11WIDSModeEntry = _FsDot11WIDSModeEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 62, 1, 8, 1)
)
fsDot11WIDSModeEntry.setIndexNames(
    (0, "FS-DOT11-WIDS-MIB", "fsDot11WIDSAPID"),
)
if mibBuilder.loadTexts:
    fsDot11WIDSModeEntry.setStatus("current")
_FsDot11WIDSAPID_Type = Integer32
_FsDot11WIDSAPID_Object = MibTableColumn
fsDot11WIDSAPID = _FsDot11WIDSAPID_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 62, 1, 8, 1, 1),
    _FsDot11WIDSAPID_Type()
)
fsDot11WIDSAPID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsDot11WIDSAPID.setStatus("current")
_FsDot11WIDSDeviceMode_Type = Integer32
_FsDot11WIDSDeviceMode_Object = MibTableColumn
fsDot11WIDSDeviceMode = _FsDot11WIDSDeviceMode_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 62, 1, 8, 1, 2),
    _FsDot11WIDSDeviceMode_Type()
)
fsDot11WIDSDeviceMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot11WIDSDeviceMode.setStatus("current")
_FsDot11WIDSWhitelistMacaddressListTable_Object = MibTable
fsDot11WIDSWhitelistMacaddressListTable = _FsDot11WIDSWhitelistMacaddressListTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 62, 1, 9)
)
if mibBuilder.loadTexts:
    fsDot11WIDSWhitelistMacaddressListTable.setStatus("current")
_FsDot11WIDSWhitelistMacaddressListEntry_Object = MibTableRow
fsDot11WIDSWhitelistMacaddressListEntry = _FsDot11WIDSWhitelistMacaddressListEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 62, 1, 9, 1)
)
fsDot11WIDSWhitelistMacaddressListEntry.setIndexNames(
    (0, "FS-DOT11-WIDS-MIB", "fsDot11WhitelistNum"),
)
if mibBuilder.loadTexts:
    fsDot11WIDSWhitelistMacaddressListEntry.setStatus("current")
_FsDot11WhitelistNum_Type = Integer32
_FsDot11WhitelistNum_Object = MibTableColumn
fsDot11WhitelistNum = _FsDot11WhitelistNum_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 62, 1, 9, 1, 1),
    _FsDot11WhitelistNum_Type()
)
fsDot11WhitelistNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsDot11WhitelistNum.setStatus("current")
_FsDot11WhitelistOper_Type = Integer32
_FsDot11WhitelistOper_Object = MibTableColumn
fsDot11WhitelistOper = _FsDot11WhitelistOper_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 62, 1, 9, 1, 2),
    _FsDot11WhitelistOper_Type()
)
fsDot11WhitelistOper.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot11WhitelistOper.setStatus("current")
_FsDot11WhitelistMAC_Type = MacAddress
_FsDot11WhitelistMAC_Object = MibTableColumn
fsDot11WhitelistMAC = _FsDot11WhitelistMAC_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 62, 1, 9, 1, 3),
    _FsDot11WhitelistMAC_Type()
)
fsDot11WhitelistMAC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot11WhitelistMAC.setStatus("current")
_FsDot11WIDSStaticblackListTable_Object = MibTable
fsDot11WIDSStaticblackListTable = _FsDot11WIDSStaticblackListTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 62, 1, 10)
)
if mibBuilder.loadTexts:
    fsDot11WIDSStaticblackListTable.setStatus("current")
_FsDot11WIDSStaticblackListEntry_Object = MibTableRow
fsDot11WIDSStaticblackListEntry = _FsDot11WIDSStaticblackListEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 62, 1, 10, 1)
)
fsDot11WIDSStaticblackListEntry.setIndexNames(
    (0, "FS-DOT11-WIDS-MIB", "fsDot11StaticblacklistNum"),
)
if mibBuilder.loadTexts:
    fsDot11WIDSStaticblackListEntry.setStatus("current")
_FsDot11StaticblacklistNum_Type = Integer32
_FsDot11StaticblacklistNum_Object = MibTableColumn
fsDot11StaticblacklistNum = _FsDot11StaticblacklistNum_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 62, 1, 10, 1, 1),
    _FsDot11StaticblacklistNum_Type()
)
fsDot11StaticblacklistNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsDot11StaticblacklistNum.setStatus("current")
_FsDot11StaticblacklistOper_Type = Integer32
_FsDot11StaticblacklistOper_Object = MibTableColumn
fsDot11StaticblacklistOper = _FsDot11StaticblacklistOper_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 62, 1, 10, 1, 2),
    _FsDot11StaticblacklistOper_Type()
)
fsDot11StaticblacklistOper.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot11StaticblacklistOper.setStatus("current")
_FsDot11StaticblacklistMAC_Type = MacAddress
_FsDot11StaticblacklistMAC_Object = MibTableColumn
fsDot11StaticblacklistMAC = _FsDot11StaticblacklistMAC_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 62, 1, 10, 1, 3),
    _FsDot11StaticblacklistMAC_Type()
)
fsDot11StaticblacklistMAC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot11StaticblacklistMAC.setStatus("current")
_FsDot11WIDSDynamicblacklistEnable_Type = TruthValue
_FsDot11WIDSDynamicblacklistEnable_Object = MibScalar
fsDot11WIDSDynamicblacklistEnable = _FsDot11WIDSDynamicblacklistEnable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 62, 1, 11),
    _FsDot11WIDSDynamicblacklistEnable_Type()
)
fsDot11WIDSDynamicblacklistEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot11WIDSDynamicblacklistEnable.setStatus("current")
_FsDot11WIDSDynamicblacklistLifetime_Type = Integer32
_FsDot11WIDSDynamicblacklistLifetime_Object = MibScalar
fsDot11WIDSDynamicblacklistLifetime = _FsDot11WIDSDynamicblacklistLifetime_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 62, 1, 12),
    _FsDot11WIDSDynamicblacklistLifetime_Type()
)
fsDot11WIDSDynamicblacklistLifetime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot11WIDSDynamicblacklistLifetime.setStatus("current")
_FsDot11WIDSAttackDetectionMode_Type = Integer32
_FsDot11WIDSAttackDetectionMode_Object = MibScalar
fsDot11WIDSAttackDetectionMode = _FsDot11WIDSAttackDetectionMode_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 62, 1, 13),
    _FsDot11WIDSAttackDetectionMode_Type()
)
fsDot11WIDSAttackDetectionMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot11WIDSAttackDetectionMode.setStatus("current")
_FsDot11WIDSRogueInfoTable_Object = MibTable
fsDot11WIDSRogueInfoTable = _FsDot11WIDSRogueInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 62, 1, 14)
)
if mibBuilder.loadTexts:
    fsDot11WIDSRogueInfoTable.setStatus("current")
_FsDot11WIDSRogueInfoEntry_Object = MibTableRow
fsDot11WIDSRogueInfoEntry = _FsDot11WIDSRogueInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 62, 1, 14, 1)
)
fsDot11WIDSRogueInfoEntry.setIndexNames(
    (0, "FS-DOT11-WIDS-MIB", "fsDot11WIDSRogueInfoNUM"),
    (0, "FS-DOT11-WIDS-MIB", "fsDot11WIDSRogueInfoTYPE"),
)
if mibBuilder.loadTexts:
    fsDot11WIDSRogueInfoEntry.setStatus("current")
_FsDot11WIDSRogueInfoNUM_Type = Integer32
_FsDot11WIDSRogueInfoNUM_Object = MibTableColumn
fsDot11WIDSRogueInfoNUM = _FsDot11WIDSRogueInfoNUM_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 62, 1, 14, 1, 1),
    _FsDot11WIDSRogueInfoNUM_Type()
)
fsDot11WIDSRogueInfoNUM.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsDot11WIDSRogueInfoNUM.setStatus("current")
_FsDot11WIDSRogueInfoTYPE_Type = Integer32
_FsDot11WIDSRogueInfoTYPE_Object = MibTableColumn
fsDot11WIDSRogueInfoTYPE = _FsDot11WIDSRogueInfoTYPE_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 62, 1, 14, 1, 2),
    _FsDot11WIDSRogueInfoTYPE_Type()
)
fsDot11WIDSRogueInfoTYPE.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsDot11WIDSRogueInfoTYPE.setStatus("current")
_FsDot11WIDSRogueInfoOper_Type = Integer32
_FsDot11WIDSRogueInfoOper_Object = MibTableColumn
fsDot11WIDSRogueInfoOper = _FsDot11WIDSRogueInfoOper_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 62, 1, 14, 1, 3),
    _FsDot11WIDSRogueInfoOper_Type()
)
fsDot11WIDSRogueInfoOper.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot11WIDSRogueInfoOper.setStatus("current")
_FsDot11WIDSRogueInfoMAC_Type = MacAddress
_FsDot11WIDSRogueInfoMAC_Object = MibTableColumn
fsDot11WIDSRogueInfoMAC = _FsDot11WIDSRogueInfoMAC_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 62, 1, 14, 1, 4),
    _FsDot11WIDSRogueInfoMAC_Type()
)
fsDot11WIDSRogueInfoMAC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot11WIDSRogueInfoMAC.setStatus("current")
_FsDot11WIDSRogueInfoString_Type = DisplayString
_FsDot11WIDSRogueInfoString_Object = MibTableColumn
fsDot11WIDSRogueInfoString = _FsDot11WIDSRogueInfoString_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 62, 1, 14, 1, 5),
    _FsDot11WIDSRogueInfoString_Type()
)
fsDot11WIDSRogueInfoString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot11WIDSRogueInfoString.setStatus("current")
_FsDot11WIDSPermitmaclistEnableTable_Object = MibTable
fsDot11WIDSPermitmaclistEnableTable = _FsDot11WIDSPermitmaclistEnableTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 62, 1, 15)
)
if mibBuilder.loadTexts:
    fsDot11WIDSPermitmaclistEnableTable.setStatus("current")
_FsDot11WIDSPermitmaclistEnableEntry_Object = MibTableRow
fsDot11WIDSPermitmaclistEnableEntry = _FsDot11WIDSPermitmaclistEnableEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 62, 1, 15, 1)
)
fsDot11WIDSPermitmaclistEnableEntry.setIndexNames(
    (0, "FS-DOT11-WIDS-MIB", "fsDot11WIDSEnableVlanPermitmaclistNum"),
)
if mibBuilder.loadTexts:
    fsDot11WIDSPermitmaclistEnableEntry.setStatus("current")
_FsDot11WIDSEnableVlanPermitmaclistNum_Type = Integer32
_FsDot11WIDSEnableVlanPermitmaclistNum_Object = MibTableColumn
fsDot11WIDSEnableVlanPermitmaclistNum = _FsDot11WIDSEnableVlanPermitmaclistNum_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 62, 1, 15, 1, 1),
    _FsDot11WIDSEnableVlanPermitmaclistNum_Type()
)
fsDot11WIDSEnableVlanPermitmaclistNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsDot11WIDSEnableVlanPermitmaclistNum.setStatus("current")
_FsDot11WIDSEnableVlanPermitmaclistOper_Type = Integer32
_FsDot11WIDSEnableVlanPermitmaclistOper_Object = MibTableColumn
fsDot11WIDSEnableVlanPermitmaclistOper = _FsDot11WIDSEnableVlanPermitmaclistOper_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 62, 1, 15, 1, 2),
    _FsDot11WIDSEnableVlanPermitmaclistOper_Type()
)
fsDot11WIDSEnableVlanPermitmaclistOper.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot11WIDSEnableVlanPermitmaclistOper.setStatus("current")
_FsDot11WIDSEnableVlanPermitmaclist_Type = MacAddress
_FsDot11WIDSEnableVlanPermitmaclist_Object = MibTableColumn
fsDot11WIDSEnableVlanPermitmaclist = _FsDot11WIDSEnableVlanPermitmaclist_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 62, 1, 15, 1, 3),
    _FsDot11WIDSEnableVlanPermitmaclist_Type()
)
fsDot11WIDSEnableVlanPermitmaclist.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot11WIDSEnableVlanPermitmaclist.setStatus("current")
_FsDot11WIDSResetStatistics_Type = TruthValue
_FsDot11WIDSResetStatistics_Object = MibScalar
fsDot11WIDSResetStatistics = _FsDot11WIDSResetStatistics_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 62, 1, 18),
    _FsDot11WIDSResetStatistics_Type()
)
fsDot11WIDSResetStatistics.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot11WIDSResetStatistics.setStatus("current")
_FsDot11WIDSResetRoguehistoryStatistics_Type = Integer32
_FsDot11WIDSResetRoguehistoryStatistics_Object = MibScalar
fsDot11WIDSResetRoguehistoryStatistics = _FsDot11WIDSResetRoguehistoryStatistics_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 62, 1, 19),
    _FsDot11WIDSResetRoguehistoryStatistics_Type()
)
fsDot11WIDSResetRoguehistoryStatistics.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot11WIDSResetRoguehistoryStatistics.setStatus("current")
_FsDot11WIDSResethistory_Type = Integer32
_FsDot11WIDSResethistory_Object = MibScalar
fsDot11WIDSResethistory = _FsDot11WIDSResethistory_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 62, 1, 20),
    _FsDot11WIDSResethistory_Type()
)
fsDot11WIDSResethistory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot11WIDSResethistory.setStatus("current")
_FsDot11WIDSResetDynamicBlacklistTable_Object = MibTable
fsDot11WIDSResetDynamicBlacklistTable = _FsDot11WIDSResetDynamicBlacklistTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 62, 1, 21)
)
if mibBuilder.loadTexts:
    fsDot11WIDSResetDynamicBlacklistTable.setStatus("current")
_FsDot11WIDSResetDynamicBlacklistEntry_Object = MibTableRow
fsDot11WIDSResetDynamicBlacklistEntry = _FsDot11WIDSResetDynamicBlacklistEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 62, 1, 21, 1)
)
fsDot11WIDSResetDynamicBlacklistEntry.setIndexNames(
    (0, "FS-DOT11-WIDS-MIB", "fsDot11WIDSResetDynamicBlacklistMac"),
)
if mibBuilder.loadTexts:
    fsDot11WIDSResetDynamicBlacklistEntry.setStatus("current")
_FsDot11WIDSResetDynamicBlacklistMac_Type = MacAddress
_FsDot11WIDSResetDynamicBlacklistMac_Object = MibTableColumn
fsDot11WIDSResetDynamicBlacklistMac = _FsDot11WIDSResetDynamicBlacklistMac_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 62, 1, 21, 1, 1),
    _FsDot11WIDSResetDynamicBlacklistMac_Type()
)
fsDot11WIDSResetDynamicBlacklistMac.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsDot11WIDSResetDynamicBlacklistMac.setStatus("current")
_FsDot11WIDSResetDynamicBlacklistType_Type = Integer32
_FsDot11WIDSResetDynamicBlacklistType_Object = MibTableColumn
fsDot11WIDSResetDynamicBlacklistType = _FsDot11WIDSResetDynamicBlacklistType_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 62, 1, 21, 1, 2),
    _FsDot11WIDSResetDynamicBlacklistType_Type()
)
fsDot11WIDSResetDynamicBlacklistType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot11WIDSResetDynamicBlacklistType.setStatus("current")
_FsDot11WIDResetUserisolationStatistics_Type = Integer32
_FsDot11WIDResetUserisolationStatistics_Object = MibScalar
fsDot11WIDResetUserisolationStatistics = _FsDot11WIDResetUserisolationStatistics_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 62, 1, 22),
    _FsDot11WIDResetUserisolationStatistics_Type()
)
fsDot11WIDResetUserisolationStatistics.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot11WIDResetUserisolationStatistics.setStatus("current")
_FsDot11WIDUserisolationAC_Type = Integer32
_FsDot11WIDUserisolationAC_Object = MibScalar
fsDot11WIDUserisolationAC = _FsDot11WIDUserisolationAC_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 62, 1, 23),
    _FsDot11WIDUserisolationAC_Type()
)
fsDot11WIDUserisolationAC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot11WIDUserisolationAC.setStatus("current")
_FsDot11WIDUserisolationAP_Type = Integer32
_FsDot11WIDUserisolationAP_Object = MibScalar
fsDot11WIDUserisolationAP = _FsDot11WIDUserisolationAP_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 62, 1, 24),
    _FsDot11WIDUserisolationAP_Type()
)
fsDot11WIDUserisolationAP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot11WIDUserisolationAP.setStatus("current")
_FsDot11WIDSShowStaticsTable_Object = MibTable
fsDot11WIDSShowStaticsTable = _FsDot11WIDSShowStaticsTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 62, 1, 25)
)
if mibBuilder.loadTexts:
    fsDot11WIDSShowStaticsTable.setStatus("current")
_FsDot11WIDSShowStaticsEntry_Object = MibTableRow
fsDot11WIDSShowStaticsEntry = _FsDot11WIDSShowStaticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 62, 1, 25, 1)
)
fsDot11WIDSShowStaticsEntry.setIndexNames(
    (0, "FS-DOT11-WIDS-MIB", "fsDot11WIDSShowStaticsNum"),
)
if mibBuilder.loadTexts:
    fsDot11WIDSShowStaticsEntry.setStatus("current")
_FsDot11WIDSShowStaticsNum_Type = Integer32
_FsDot11WIDSShowStaticsNum_Object = MibTableColumn
fsDot11WIDSShowStaticsNum = _FsDot11WIDSShowStaticsNum_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 62, 1, 25, 1, 1),
    _FsDot11WIDSShowStaticsNum_Type()
)
fsDot11WIDSShowStaticsNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsDot11WIDSShowStaticsNum.setStatus("current")
_FsDot11WIDSShowStaticsOper_Type = Integer32
_FsDot11WIDSShowStaticsOper_Object = MibTableColumn
fsDot11WIDSShowStaticsOper = _FsDot11WIDSShowStaticsOper_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 62, 1, 25, 1, 2),
    _FsDot11WIDSShowStaticsOper_Type()
)
fsDot11WIDSShowStaticsOper.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot11WIDSShowStaticsOper.setStatus("current")
_FsDot11WIDSShowStaticsMac_Type = MacAddress
_FsDot11WIDSShowStaticsMac_Object = MibTableColumn
fsDot11WIDSShowStaticsMac = _FsDot11WIDSShowStaticsMac_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 62, 1, 25, 1, 3),
    _FsDot11WIDSShowStaticsMac_Type()
)
fsDot11WIDSShowStaticsMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot11WIDSShowStaticsMac.setStatus("current")


class _FsDot11WIDSShowStaticsInfo_Type(DisplayString):
    """Custom type fsDot11WIDSShowStaticsInfo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_FsDot11WIDSShowStaticsInfo_Type.__name__ = "DisplayString"
_FsDot11WIDSShowStaticsInfo_Object = MibTableColumn
fsDot11WIDSShowStaticsInfo = _FsDot11WIDSShowStaticsInfo_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 62, 1, 25, 1, 4),
    _FsDot11WIDSShowStaticsInfo_Type()
)
fsDot11WIDSShowStaticsInfo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot11WIDSShowStaticsInfo.setStatus("current")
_FsDot11WIDSAssociationFailureTotalTimes_Type = Integer32
_FsDot11WIDSAssociationFailureTotalTimes_Object = MibScalar
fsDot11WIDSAssociationFailureTotalTimes = _FsDot11WIDSAssociationFailureTotalTimes_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 62, 1, 26),
    _FsDot11WIDSAssociationFailureTotalTimes_Type()
)
fsDot11WIDSAssociationFailureTotalTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDot11WIDSAssociationFailureTotalTimes.setStatus("current")
_FsDot11WIDSSuspiciousAPInfoTable_Object = MibTable
fsDot11WIDSSuspiciousAPInfoTable = _FsDot11WIDSSuspiciousAPInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 62, 1, 27)
)
if mibBuilder.loadTexts:
    fsDot11WIDSSuspiciousAPInfoTable.setStatus("current")
_FsDot11WIDSSuspiciousAPInfoEntry_Object = MibTableRow
fsDot11WIDSSuspiciousAPInfoEntry = _FsDot11WIDSSuspiciousAPInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 62, 1, 27, 1)
)
fsDot11WIDSSuspiciousAPInfoEntry.setIndexNames(
    (0, "FS-DOT11-WIDS-MIB", "fsDot11WIDSSuspiciousAPBSS"),
)
if mibBuilder.loadTexts:
    fsDot11WIDSSuspiciousAPInfoEntry.setStatus("current")
_FsDot11WIDSSuspiciousAPBSS_Type = MacAddress
_FsDot11WIDSSuspiciousAPBSS_Object = MibTableColumn
fsDot11WIDSSuspiciousAPBSS = _FsDot11WIDSSuspiciousAPBSS_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 62, 1, 27, 1, 1),
    _FsDot11WIDSSuspiciousAPBSS_Type()
)
fsDot11WIDSSuspiciousAPBSS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDot11WIDSSuspiciousAPBSS.setStatus("current")
_FsDot11WIDSSuspiciousAPCount_Type = Integer32
_FsDot11WIDSSuspiciousAPCount_Object = MibTableColumn
fsDot11WIDSSuspiciousAPCount = _FsDot11WIDSSuspiciousAPCount_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 62, 1, 27, 1, 2),
    _FsDot11WIDSSuspiciousAPCount_Type()
)
fsDot11WIDSSuspiciousAPCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDot11WIDSSuspiciousAPCount.setStatus("current")
_FsDot11WIDSMomentFirstTimeDetectedSusAP_Type = TimeTicks
_FsDot11WIDSMomentFirstTimeDetectedSusAP_Object = MibTableColumn
fsDot11WIDSMomentFirstTimeDetectedSusAP = _FsDot11WIDSMomentFirstTimeDetectedSusAP_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 62, 1, 27, 1, 3),
    _FsDot11WIDSMomentFirstTimeDetectedSusAP_Type()
)
fsDot11WIDSMomentFirstTimeDetectedSusAP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDot11WIDSMomentFirstTimeDetectedSusAP.setStatus("current")
_FsDot11WIDSMomentLastTimeDetectedSusAP_Type = TimeTicks
_FsDot11WIDSMomentLastTimeDetectedSusAP_Object = MibTableColumn
fsDot11WIDSMomentLastTimeDetectedSusAP = _FsDot11WIDSMomentLastTimeDetectedSusAP_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 62, 1, 27, 1, 4),
    _FsDot11WIDSMomentLastTimeDetectedSusAP_Type()
)
fsDot11WIDSMomentLastTimeDetectedSusAP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDot11WIDSMomentLastTimeDetectedSusAP.setStatus("current")
_FsDot11WIDSSuspiciousAPSSID_Type = DisplayString
_FsDot11WIDSSuspiciousAPSSID_Object = MibTableColumn
fsDot11WIDSSuspiciousAPSSID = _FsDot11WIDSSuspiciousAPSSID_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 62, 1, 27, 1, 5),
    _FsDot11WIDSSuspiciousAPSSID_Type()
)
fsDot11WIDSSuspiciousAPSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDot11WIDSSuspiciousAPSSID.setStatus("current")
_FsDot11WIDSSuspiciousAPMaxSignalStrength_Type = Integer32
_FsDot11WIDSSuspiciousAPMaxSignalStrength_Object = MibTableColumn
fsDot11WIDSSuspiciousAPMaxSignalStrength = _FsDot11WIDSSuspiciousAPMaxSignalStrength_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 62, 1, 27, 1, 6),
    _FsDot11WIDSSuspiciousAPMaxSignalStrength_Type()
)
fsDot11WIDSSuspiciousAPMaxSignalStrength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDot11WIDSSuspiciousAPMaxSignalStrength.setStatus("current")
_FsDot11WIDSSuspiciousAPUsingChannel_Type = Integer32
_FsDot11WIDSSuspiciousAPUsingChannel_Object = MibTableColumn
fsDot11WIDSSuspiciousAPUsingChannel = _FsDot11WIDSSuspiciousAPUsingChannel_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 62, 1, 27, 1, 7),
    _FsDot11WIDSSuspiciousAPUsingChannel_Type()
)
fsDot11WIDSSuspiciousAPUsingChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDot11WIDSSuspiciousAPUsingChannel.setStatus("current")
_FsDot11WIDSSuspiciousAPFrameEncrption_Type = Integer32
_FsDot11WIDSSuspiciousAPFrameEncrption_Object = MibTableColumn
fsDot11WIDSSuspiciousAPFrameEncrption = _FsDot11WIDSSuspiciousAPFrameEncrption_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 62, 1, 27, 1, 8),
    _FsDot11WIDSSuspiciousAPFrameEncrption_Type()
)
fsDot11WIDSSuspiciousAPFrameEncrption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDot11WIDSSuspiciousAPFrameEncrption.setStatus("current")
_FsDot11WIDSSuspiciousAPNeedsDealingTag_Type = TruthValue
_FsDot11WIDSSuspiciousAPNeedsDealingTag_Object = MibTableColumn
fsDot11WIDSSuspiciousAPNeedsDealingTag = _FsDot11WIDSSuspiciousAPNeedsDealingTag_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 62, 1, 27, 1, 9),
    _FsDot11WIDSSuspiciousAPNeedsDealingTag_Type()
)
fsDot11WIDSSuspiciousAPNeedsDealingTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDot11WIDSSuspiciousAPNeedsDealingTag.setStatus("current")
_FsDot11WIDSSuspiciousAPIgnoredTag_Type = TruthValue
_FsDot11WIDSSuspiciousAPIgnoredTag_Object = MibTableColumn
fsDot11WIDSSuspiciousAPIgnoredTag = _FsDot11WIDSSuspiciousAPIgnoredTag_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 62, 1, 27, 1, 10),
    _FsDot11WIDSSuspiciousAPIgnoredTag_Type()
)
fsDot11WIDSSuspiciousAPIgnoredTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDot11WIDSSuspiciousAPIgnoredTag.setStatus("current")
_FsDot11WIDSSuspiciousSTAInfoTable_Object = MibTable
fsDot11WIDSSuspiciousSTAInfoTable = _FsDot11WIDSSuspiciousSTAInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 62, 1, 28)
)
if mibBuilder.loadTexts:
    fsDot11WIDSSuspiciousSTAInfoTable.setStatus("current")
_FsDot11WIDSSuspiciousSTAInfoEntry_Object = MibTableRow
fsDot11WIDSSuspiciousSTAInfoEntry = _FsDot11WIDSSuspiciousSTAInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 62, 1, 28, 1)
)
fsDot11WIDSSuspiciousSTAInfoEntry.setIndexNames(
    (0, "FS-DOT11-WIDS-MIB", "fsDot11WIDSSuspiciousSTAMAC"),
)
if mibBuilder.loadTexts:
    fsDot11WIDSSuspiciousSTAInfoEntry.setStatus("current")
_FsDot11WIDSSuspiciousSTAMAC_Type = MacAddress
_FsDot11WIDSSuspiciousSTAMAC_Object = MibTableColumn
fsDot11WIDSSuspiciousSTAMAC = _FsDot11WIDSSuspiciousSTAMAC_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 62, 1, 28, 1, 1),
    _FsDot11WIDSSuspiciousSTAMAC_Type()
)
fsDot11WIDSSuspiciousSTAMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDot11WIDSSuspiciousSTAMAC.setStatus("current")
_FsDot11WIDSAPCountDetectingSuspiciousSTA_Type = Integer32
_FsDot11WIDSAPCountDetectingSuspiciousSTA_Object = MibTableColumn
fsDot11WIDSAPCountDetectingSuspiciousSTA = _FsDot11WIDSAPCountDetectingSuspiciousSTA_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 62, 1, 28, 1, 2),
    _FsDot11WIDSAPCountDetectingSuspiciousSTA_Type()
)
fsDot11WIDSAPCountDetectingSuspiciousSTA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDot11WIDSAPCountDetectingSuspiciousSTA.setStatus("current")
_FsDot11WIDSMomentFirstTimeDetectedSusSTA_Type = TimeTicks
_FsDot11WIDSMomentFirstTimeDetectedSusSTA_Object = MibTableColumn
fsDot11WIDSMomentFirstTimeDetectedSusSTA = _FsDot11WIDSMomentFirstTimeDetectedSusSTA_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 62, 1, 28, 1, 3),
    _FsDot11WIDSMomentFirstTimeDetectedSusSTA_Type()
)
fsDot11WIDSMomentFirstTimeDetectedSusSTA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDot11WIDSMomentFirstTimeDetectedSusSTA.setStatus("current")
_FsDot11WIDSMomentLastTimeDetectedSusSTA_Type = TimeTicks
_FsDot11WIDSMomentLastTimeDetectedSusSTA_Object = MibTableColumn
fsDot11WIDSMomentLastTimeDetectedSusSTA = _FsDot11WIDSMomentLastTimeDetectedSusSTA_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 62, 1, 28, 1, 4),
    _FsDot11WIDSMomentLastTimeDetectedSusSTA_Type()
)
fsDot11WIDSMomentLastTimeDetectedSusSTA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDot11WIDSMomentLastTimeDetectedSusSTA.setStatus("current")
_FsDot11WIDSBSSIDSuspiciousSTAAccessing_Type = MacAddress
_FsDot11WIDSBSSIDSuspiciousSTAAccessing_Object = MibTableColumn
fsDot11WIDSBSSIDSuspiciousSTAAccessing = _FsDot11WIDSBSSIDSuspiciousSTAAccessing_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 62, 1, 28, 1, 5),
    _FsDot11WIDSBSSIDSuspiciousSTAAccessing_Type()
)
fsDot11WIDSBSSIDSuspiciousSTAAccessing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDot11WIDSBSSIDSuspiciousSTAAccessing.setStatus("current")
_FsDot11WIDSSuspiciousSTAMaxSignalStrength_Type = Integer32
_FsDot11WIDSSuspiciousSTAMaxSignalStrength_Object = MibTableColumn
fsDot11WIDSSuspiciousSTAMaxSignalStrength = _FsDot11WIDSSuspiciousSTAMaxSignalStrength_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 62, 1, 28, 1, 6),
    _FsDot11WIDSSuspiciousSTAMaxSignalStrength_Type()
)
fsDot11WIDSSuspiciousSTAMaxSignalStrength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDot11WIDSSuspiciousSTAMaxSignalStrength.setStatus("current")
_FsDot11WIDSSuspiciousSTAUsingChannel_Type = Integer32
_FsDot11WIDSSuspiciousSTAUsingChannel_Object = MibTableColumn
fsDot11WIDSSuspiciousSTAUsingChannel = _FsDot11WIDSSuspiciousSTAUsingChannel_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 62, 1, 28, 1, 7),
    _FsDot11WIDSSuspiciousSTAUsingChannel_Type()
)
fsDot11WIDSSuspiciousSTAUsingChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDot11WIDSSuspiciousSTAUsingChannel.setStatus("current")
_FsDot11WIDSSuspiciousSTAWorksInAdhocMode_Type = TruthValue
_FsDot11WIDSSuspiciousSTAWorksInAdhocMode_Object = MibTableColumn
fsDot11WIDSSuspiciousSTAWorksInAdhocMode = _FsDot11WIDSSuspiciousSTAWorksInAdhocMode_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 62, 1, 28, 1, 8),
    _FsDot11WIDSSuspiciousSTAWorksInAdhocMode_Type()
)
fsDot11WIDSSuspiciousSTAWorksInAdhocMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDot11WIDSSuspiciousSTAWorksInAdhocMode.setStatus("current")
_FsDot11WIDSSuspiciousSTANeedsDealingTag_Type = TruthValue
_FsDot11WIDSSuspiciousSTANeedsDealingTag_Object = MibTableColumn
fsDot11WIDSSuspiciousSTANeedsDealingTag = _FsDot11WIDSSuspiciousSTANeedsDealingTag_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 62, 1, 28, 1, 9),
    _FsDot11WIDSSuspiciousSTANeedsDealingTag_Type()
)
fsDot11WIDSSuspiciousSTANeedsDealingTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDot11WIDSSuspiciousSTANeedsDealingTag.setStatus("current")
_FsDot11WIDSSuspiciousSTAIgnoredTag_Type = TruthValue
_FsDot11WIDSSuspiciousSTAIgnoredTag_Object = MibTableColumn
fsDot11WIDSSuspiciousSTAIgnoredTag = _FsDot11WIDSSuspiciousSTAIgnoredTag_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 62, 1, 28, 1, 10),
    _FsDot11WIDSSuspiciousSTAIgnoredTag_Type()
)
fsDot11WIDSSuspiciousSTAIgnoredTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot11WIDSSuspiciousSTAIgnoredTag.setStatus("current")
_FsDot11WIDSDetectObjects_ObjectIdentity = ObjectIdentity
fsDot11WIDSDetectObjects = _FsDot11WIDSDetectObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 62, 2)
)
_FsDot11WIDSShowDot11IdsAttacklistTable_Object = MibTable
fsDot11WIDSShowDot11IdsAttacklistTable = _FsDot11WIDSShowDot11IdsAttacklistTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 62, 2, 1)
)
if mibBuilder.loadTexts:
    fsDot11WIDSShowDot11IdsAttacklistTable.setStatus("current")
_FsDot11WIDSShowDot11IdsAttacklistEntry_Object = MibTableRow
fsDot11WIDSShowDot11IdsAttacklistEntry = _FsDot11WIDSShowDot11IdsAttacklistEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 62, 2, 1, 1)
)
fsDot11WIDSShowDot11IdsAttacklistEntry.setIndexNames(
    (0, "FS-DOT11-WIDS-MIB", "fsDot11WIDSShowDot11IdsAttacklistNum"),
)
if mibBuilder.loadTexts:
    fsDot11WIDSShowDot11IdsAttacklistEntry.setStatus("current")
_FsDot11WIDSShowDot11IdsAttacklistNum_Type = Integer32
_FsDot11WIDSShowDot11IdsAttacklistNum_Object = MibTableColumn
fsDot11WIDSShowDot11IdsAttacklistNum = _FsDot11WIDSShowDot11IdsAttacklistNum_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 62, 2, 1, 1, 1),
    _FsDot11WIDSShowDot11IdsAttacklistNum_Type()
)
fsDot11WIDSShowDot11IdsAttacklistNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsDot11WIDSShowDot11IdsAttacklistNum.setStatus("current")
_FsDot11WIDSShowDot11IdsAttacklistOper_Type = Integer32
_FsDot11WIDSShowDot11IdsAttacklistOper_Object = MibTableColumn
fsDot11WIDSShowDot11IdsAttacklistOper = _FsDot11WIDSShowDot11IdsAttacklistOper_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 62, 2, 1, 1, 2),
    _FsDot11WIDSShowDot11IdsAttacklistOper_Type()
)
fsDot11WIDSShowDot11IdsAttacklistOper.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot11WIDSShowDot11IdsAttacklistOper.setStatus("current")
_FsDot11WIDSShowDot11IdsAttacklistMac_Type = MacAddress
_FsDot11WIDSShowDot11IdsAttacklistMac_Object = MibTableColumn
fsDot11WIDSShowDot11IdsAttacklistMac = _FsDot11WIDSShowDot11IdsAttacklistMac_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 62, 2, 1, 1, 3),
    _FsDot11WIDSShowDot11IdsAttacklistMac_Type()
)
fsDot11WIDSShowDot11IdsAttacklistMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot11WIDSShowDot11IdsAttacklistMac.setStatus("current")


class _FsDot11WIDSShowDot11IdsAttacklistInfo_Type(DisplayString):
    """Custom type fsDot11WIDSShowDot11IdsAttacklistInfo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_FsDot11WIDSShowDot11IdsAttacklistInfo_Type.__name__ = "DisplayString"
_FsDot11WIDSShowDot11IdsAttacklistInfo_Object = MibTableColumn
fsDot11WIDSShowDot11IdsAttacklistInfo = _FsDot11WIDSShowDot11IdsAttacklistInfo_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 62, 2, 1, 1, 4),
    _FsDot11WIDSShowDot11IdsAttacklistInfo_Type()
)
fsDot11WIDSShowDot11IdsAttacklistInfo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot11WIDSShowDot11IdsAttacklistInfo.setStatus("current")
_FsDot11WIDSTrapsObjects_ObjectIdentity = ObjectIdentity
fsDot11WIDSTrapsObjects = _FsDot11WIDSTrapsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 62, 3)
)
_FsDot11WIDSSTAMAC_Type = MacAddress
_FsDot11WIDSSTAMAC_Object = MibScalar
fsDot11WIDSSTAMAC = _FsDot11WIDSSTAMAC_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 62, 3, 1),
    _FsDot11WIDSSTAMAC_Type()
)
fsDot11WIDSSTAMAC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot11WIDSSTAMAC.setStatus("current")


class _FsDot11WIDSAPBSSID_Type(DisplayString):
    """Custom type fsDot11WIDSAPBSSID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_FsDot11WIDSAPBSSID_Type.__name__ = "DisplayString"
_FsDot11WIDSAPBSSID_Object = MibScalar
fsDot11WIDSAPBSSID = _FsDot11WIDSAPBSSID_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 62, 3, 2),
    _FsDot11WIDSAPBSSID_Type()
)
fsDot11WIDSAPBSSID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot11WIDSAPBSSID.setStatus("current")


class _FsDot11WIDSInformation_Type(DisplayString):
    """Custom type fsDot11WIDSInformation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_FsDot11WIDSInformation_Type.__name__ = "DisplayString"
_FsDot11WIDSInformation_Object = MibScalar
fsDot11WIDSInformation = _FsDot11WIDSInformation_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 62, 3, 3),
    _FsDot11WIDSInformation_Type()
)
fsDot11WIDSInformation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot11WIDSInformation.setStatus("current")


class _FsDot11WIDSextinfo_Type(DisplayString):
    """Custom type fsDot11WIDSextinfo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_FsDot11WIDSextinfo_Type.__name__ = "DisplayString"
_FsDot11WIDSextinfo_Object = MibScalar
fsDot11WIDSextinfo = _FsDot11WIDSextinfo_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 62, 3, 4),
    _FsDot11WIDSextinfo_Type()
)
fsDot11WIDSextinfo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot11WIDSextinfo.setStatus("current")
_FsDot11WIDSDeviceInfoNUM_Type = Integer32
_FsDot11WIDSDeviceInfoNUM_Object = MibScalar
fsDot11WIDSDeviceInfoNUM = _FsDot11WIDSDeviceInfoNUM_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 62, 3, 5),
    _FsDot11WIDSDeviceInfoNUM_Type()
)
fsDot11WIDSDeviceInfoNUM.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot11WIDSDeviceInfoNUM.setStatus("current")
_FsDot11WIDSDeviceInfoTYPE_Type = Integer32
_FsDot11WIDSDeviceInfoTYPE_Object = MibScalar
fsDot11WIDSDeviceInfoTYPE = _FsDot11WIDSDeviceInfoTYPE_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 62, 3, 6),
    _FsDot11WIDSDeviceInfoTYPE_Type()
)
fsDot11WIDSDeviceInfoTYPE.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot11WIDSDeviceInfoTYPE.setStatus("current")
_FsDot11WIDSDeviceInfoOper_Type = Integer32
_FsDot11WIDSDeviceInfoOper_Object = MibScalar
fsDot11WIDSDeviceInfoOper = _FsDot11WIDSDeviceInfoOper_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 62, 3, 7),
    _FsDot11WIDSDeviceInfoOper_Type()
)
fsDot11WIDSDeviceInfoOper.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot11WIDSDeviceInfoOper.setStatus("current")
_FsDot11WIDSDeviceInfoMAC_Type = MacAddress
_FsDot11WIDSDeviceInfoMAC_Object = MibScalar
fsDot11WIDSDeviceInfoMAC = _FsDot11WIDSDeviceInfoMAC_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 62, 3, 8),
    _FsDot11WIDSDeviceInfoMAC_Type()
)
fsDot11WIDSDeviceInfoMAC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot11WIDSDeviceInfoMAC.setStatus("current")


class _FsDot11WIDSDeviceInfoString_Type(DisplayString):
    """Custom type fsDot11WIDSDeviceInfoString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_FsDot11WIDSDeviceInfoString_Type.__name__ = "DisplayString"
_FsDot11WIDSDeviceInfoString_Object = MibScalar
fsDot11WIDSDeviceInfoString = _FsDot11WIDSDeviceInfoString_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 62, 3, 9),
    _FsDot11WIDSDeviceInfoString_Type()
)
fsDot11WIDSDeviceInfoString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot11WIDSDeviceInfoString.setStatus("current")
_FsDot11WIDSSuspiciousDeviceMac_Type = MacAddress
_FsDot11WIDSSuspiciousDeviceMac_Object = MibScalar
fsDot11WIDSSuspiciousDeviceMac = _FsDot11WIDSSuspiciousDeviceMac_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 62, 3, 10),
    _FsDot11WIDSSuspiciousDeviceMac_Type()
)
fsDot11WIDSSuspiciousDeviceMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot11WIDSSuspiciousDeviceMac.setStatus("current")
_FsDot11WIDSSuspiciousDeviceExtensionInfo_Type = DisplayString
_FsDot11WIDSSuspiciousDeviceExtensionInfo_Object = MibScalar
fsDot11WIDSSuspiciousDeviceExtensionInfo = _FsDot11WIDSSuspiciousDeviceExtensionInfo_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 62, 3, 11),
    _FsDot11WIDSSuspiciousDeviceExtensionInfo_Type()
)
fsDot11WIDSSuspiciousDeviceExtensionInfo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot11WIDSSuspiciousDeviceExtensionInfo.setStatus("current")
_FsDot11WIDSUnauthorizedSSID_Type = DisplayString
_FsDot11WIDSUnauthorizedSSID_Object = MibScalar
fsDot11WIDSUnauthorizedSSID = _FsDot11WIDSUnauthorizedSSID_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 62, 3, 12),
    _FsDot11WIDSUnauthorizedSSID_Type()
)
fsDot11WIDSUnauthorizedSSID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot11WIDSUnauthorizedSSID.setStatus("current")
_FsDot11WIDSSUnauthorizedSSIDExtensionInfo_Type = DisplayString
_FsDot11WIDSSUnauthorizedSSIDExtensionInfo_Object = MibScalar
fsDot11WIDSSUnauthorizedSSIDExtensionInfo = _FsDot11WIDSSUnauthorizedSSIDExtensionInfo_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 62, 3, 13),
    _FsDot11WIDSSUnauthorizedSSIDExtensionInfo_Type()
)
fsDot11WIDSSUnauthorizedSSIDExtensionInfo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot11WIDSSUnauthorizedSSIDExtensionInfo.setStatus("current")
_FsDot11WIDSAttackingDeviceMac_Type = MacAddress
_FsDot11WIDSAttackingDeviceMac_Object = MibScalar
fsDot11WIDSAttackingDeviceMac = _FsDot11WIDSAttackingDeviceMac_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 62, 3, 14),
    _FsDot11WIDSAttackingDeviceMac_Type()
)
fsDot11WIDSAttackingDeviceMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot11WIDSAttackingDeviceMac.setStatus("current")
_FsDot11WIDSAttackType_Type = Integer32
_FsDot11WIDSAttackType_Object = MibScalar
fsDot11WIDSAttackType = _FsDot11WIDSAttackType_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 62, 3, 15),
    _FsDot11WIDSAttackType_Type()
)
fsDot11WIDSAttackType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot11WIDSAttackType.setStatus("current")
_FsDot11WIDSAttackExtensionInfo_Type = DisplayString
_FsDot11WIDSAttackExtensionInfo_Object = MibScalar
fsDot11WIDSAttackExtensionInfo = _FsDot11WIDSAttackExtensionInfo_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 62, 3, 16),
    _FsDot11WIDSAttackExtensionInfo_Type()
)
fsDot11WIDSAttackExtensionInfo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot11WIDSAttackExtensionInfo.setStatus("current")
_FsDot11WIDSMIBConform_ObjectIdentity = ObjectIdentity
fsDot11WIDSMIBConform = _FsDot11WIDSMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 62, 4)
)
_FsDot11WIDSMIBCompliances_ObjectIdentity = ObjectIdentity
fsDot11WIDSMIBCompliances = _FsDot11WIDSMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 62, 4, 1)
)
_FsDot11WIDSMIBGroups_ObjectIdentity = ObjectIdentity
fsDot11WIDSMIBGroups = _FsDot11WIDSMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 62, 4, 2)
)

# Managed Objects groups

fsDot11WIDSMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 62, 4, 2, 1)
)
fsDot11WIDSMIBGroup.setObjects(
      *(("FS-DOT11-WIDS-MIB", "fsDot11VendorOper"),
        ("FS-DOT11-WIDS-MIB", "fsDot11VendorName"),
        ("FS-DOT11-WIDS-MIB", "fsDot11PermitOper"),
        ("FS-DOT11-WIDS-MIB", "fsDot11PermitSSID"),
        ("FS-DOT11-WIDS-MIB", "fsDot11AttackOper"),
        ("FS-DOT11-WIDS-MIB", "fsDot11AttackMAC"),
        ("FS-DOT11-WIDS-MIB", "fsDot11AttackInfo"),
        ("FS-DOT11-WIDS-MIB", "fsDot11PermitMACOper"),
        ("FS-DOT11-WIDS-MIB", "fsDot11PermitMACAddr"),
        ("FS-DOT11-WIDS-MIB", "fsDot11WIDSDeviceagingDuration"),
        ("FS-DOT11-WIDS-MIB", "fsDot11WIDSCountermeasuresMode"),
        ("FS-DOT11-WIDS-MIB", "fsDot11WIDSCountermeasureSet"),
        ("FS-DOT11-WIDS-MIB", "fsDot11WIDSDeviceMode"),
        ("FS-DOT11-WIDS-MIB", "fsDot11WhitelistOper"),
        ("FS-DOT11-WIDS-MIB", "fsDot11WhitelistMAC"),
        ("FS-DOT11-WIDS-MIB", "fsDot11StaticblacklistOper"),
        ("FS-DOT11-WIDS-MIB", "fsDot11StaticblacklistMAC"),
        ("FS-DOT11-WIDS-MIB", "fsDot11WIDSDynamicblacklistEnable"),
        ("FS-DOT11-WIDS-MIB", "fsDot11WIDSDynamicblacklistLifetime"),
        ("FS-DOT11-WIDS-MIB", "fsDot11WIDSAttackDetectionMode"),
        ("FS-DOT11-WIDS-MIB", "fsDot11WIDSRogueInfoOper"),
        ("FS-DOT11-WIDS-MIB", "fsDot11WIDSRogueInfoMAC"),
        ("FS-DOT11-WIDS-MIB", "fsDot11WIDSRogueInfoString"),
        ("FS-DOT11-WIDS-MIB", "fsDot11WIDSEnableVlanPermitmaclistOper"),
        ("FS-DOT11-WIDS-MIB", "fsDot11WIDSEnableVlanPermitmaclist"),
        ("FS-DOT11-WIDS-MIB", "fsDot11WIDSResetStatistics"),
        ("FS-DOT11-WIDS-MIB", "fsDot11WIDSResetRoguehistoryStatistics"),
        ("FS-DOT11-WIDS-MIB", "fsDot11WIDSResethistory"),
        ("FS-DOT11-WIDS-MIB", "fsDot11WIDSResetDynamicBlacklistType"),
        ("FS-DOT11-WIDS-MIB", "fsDot11WIDResetUserisolationStatistics"),
        ("FS-DOT11-WIDS-MIB", "fsDot11WIDSShowDot11IdsAttacklistOper"),
        ("FS-DOT11-WIDS-MIB", "fsDot11WIDSShowDot11IdsAttacklistMac"),
        ("FS-DOT11-WIDS-MIB", "fsDot11WIDSShowDot11IdsAttacklistInfo"),
        ("FS-DOT11-WIDS-MIB", "fsDot11WIDUserisolationAC"),
        ("FS-DOT11-WIDS-MIB", "fsDot11WIDUserisolationAP"),
        ("FS-DOT11-WIDS-MIB", "fsDot11WIDSShowStaticsOper"),
        ("FS-DOT11-WIDS-MIB", "fsDot11WIDSShowStaticsMac"),
        ("FS-DOT11-WIDS-MIB", "fsDot11WIDSShowStaticsInfo"),
        ("FS-DOT11-WIDS-MIB", "fsDot11WIDSAssociationFailureTotalTimes"),
        ("FS-DOT11-WIDS-MIB", "fsDot11WIDSSuspiciousAPCount"),
        ("FS-DOT11-WIDS-MIB", "fsDot11WIDSMomentFirstTimeDetectedSusAP"),
        ("FS-DOT11-WIDS-MIB", "fsDot11WIDSMomentLastTimeDetectedSusAP"),
        ("FS-DOT11-WIDS-MIB", "fsDot11WIDSSuspiciousAPSSID"),
        ("FS-DOT11-WIDS-MIB", "fsDot11WIDSSuspiciousAPMaxSignalStrength"),
        ("FS-DOT11-WIDS-MIB", "fsDot11WIDSSuspiciousAPUsingChannel"),
        ("FS-DOT11-WIDS-MIB", "fsDot11WIDSSuspiciousAPFrameEncrption"),
        ("FS-DOT11-WIDS-MIB", "fsDot11WIDSSuspiciousAPNeedsDealingTag"),
        ("FS-DOT11-WIDS-MIB", "fsDot11WIDSSuspiciousAPIgnoredTag"),
        ("FS-DOT11-WIDS-MIB", "fsDot11WIDSAPCountDetectingSuspiciousSTA"),
        ("FS-DOT11-WIDS-MIB", "fsDot11WIDSMomentFirstTimeDetectedSusSTA"),
        ("FS-DOT11-WIDS-MIB", "fsDot11WIDSMomentLastTimeDetectedSusSTA"),
        ("FS-DOT11-WIDS-MIB", "fsDot11WIDSBSSIDSuspiciousSTAAccessing"),
        ("FS-DOT11-WIDS-MIB", "fsDot11WIDSSuspiciousSTAMaxSignalStrength"),
        ("FS-DOT11-WIDS-MIB", "fsDot11WIDSSuspiciousSTAUsingChannel"),
        ("FS-DOT11-WIDS-MIB", "fsDot11WIDSSuspiciousSTAWorksInAdhocMode"),
        ("FS-DOT11-WIDS-MIB", "fsDot11WIDSSuspiciousSTANeedsDealingTag"),
        ("FS-DOT11-WIDS-MIB", "fsDot11WIDSSuspiciousSTAIgnoredTag"),
        ("FS-DOT11-WIDS-MIB", "fsDot11WIDSSuspiciousDeviceMac"),
        ("FS-DOT11-WIDS-MIB", "fsDot11WIDSSuspiciousDeviceExtensionInfo"),
        ("FS-DOT11-WIDS-MIB", "fsDot11WIDSUnauthorizedSSID"),
        ("FS-DOT11-WIDS-MIB", "fsDot11WIDSSUnauthorizedSSIDExtensionInfo"),
        ("FS-DOT11-WIDS-MIB", "fsDot11WIDSAttackingDeviceMac"),
        ("FS-DOT11-WIDS-MIB", "fsDot11WIDSAttackType"),
        ("FS-DOT11-WIDS-MIB", "fsDot11WIDSAttackExtensionInfo"),
        ("FS-DOT11-WIDS-MIB", "fsDot11WIDSSTAMAC"),
        ("FS-DOT11-WIDS-MIB", "fsDot11WIDSAPBSSID"),
        ("FS-DOT11-WIDS-MIB", "fsDot11WIDSInformation"),
        ("FS-DOT11-WIDS-MIB", "fsDot11WIDSextinfo"),
        ("FS-DOT11-WIDS-MIB", "fsDot11WIDSDeviceInfoNUM"),
        ("FS-DOT11-WIDS-MIB", "fsDot11WIDSDeviceInfoTYPE"),
        ("FS-DOT11-WIDS-MIB", "fsDot11WIDSDeviceInfoOper"),
        ("FS-DOT11-WIDS-MIB", "fsDot11WIDSDeviceInfoMAC"),
        ("FS-DOT11-WIDS-MIB", "fsDot11WIDSDeviceInfoString"))
)
if mibBuilder.loadTexts:
    fsDot11WIDSMIBGroup.setStatus("current")


# Notification objects

fsDot11WIDSWirelessUserConnect = NotificationType(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 62, 0, 1)
)
fsDot11WIDSWirelessUserConnect.setObjects(
      *(("FS-DOT11-WIDS-MIB", "fsDot11WIDSSTAMAC"),
        ("FS-DOT11-WIDS-MIB", "fsDot11WIDSAPBSSID"),
        ("FS-DOT11-WIDS-MIB", "fsDot11WIDSInformation"),
        ("FS-DOT11-WIDS-MIB", "fsDot11WIDSextinfo"))
)
if mibBuilder.loadTexts:
    fsDot11WIDSWirelessUserConnect.setStatus(
        "current"
    )

fsDot11WIDSWirelessUserDisconnect = NotificationType(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 62, 0, 2)
)
fsDot11WIDSWirelessUserDisconnect.setObjects(
      *(("FS-DOT11-WIDS-MIB", "fsDot11WIDSSTAMAC"),
        ("FS-DOT11-WIDS-MIB", "fsDot11WIDSAPBSSID"),
        ("FS-DOT11-WIDS-MIB", "fsDot11WIDSInformation"),
        ("FS-DOT11-WIDS-MIB", "fsDot11WIDSextinfo"))
)
if mibBuilder.loadTexts:
    fsDot11WIDSWirelessUserDisconnect.setStatus(
        "current"
    )

fsDot11WIDSWirelessUserReauthentication = NotificationType(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 62, 0, 3)
)
fsDot11WIDSWirelessUserReauthentication.setObjects(
      *(("FS-DOT11-WIDS-MIB", "fsDot11WIDSSTAMAC"),
        ("FS-DOT11-WIDS-MIB", "fsDot11WIDSAPBSSID"),
        ("FS-DOT11-WIDS-MIB", "fsDot11WIDSInformation"),
        ("FS-DOT11-WIDS-MIB", "fsDot11WIDSextinfo"))
)
if mibBuilder.loadTexts:
    fsDot11WIDSWirelessUserReauthentication.setStatus(
        "current"
    )

fsDot11WIDSWirelessUserAuthenticationFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 62, 0, 4)
)
fsDot11WIDSWirelessUserAuthenticationFailure.setObjects(
      *(("FS-DOT11-WIDS-MIB", "fsDot11WIDSSTAMAC"),
        ("FS-DOT11-WIDS-MIB", "fsDot11WIDSAPBSSID"),
        ("FS-DOT11-WIDS-MIB", "fsDot11WIDSInformation"),
        ("FS-DOT11-WIDS-MIB", "fsDot11WIDSextinfo"))
)
if mibBuilder.loadTexts:
    fsDot11WIDSWirelessUserAuthenticationFailure.setStatus(
        "current"
    )

fsDot11WIDSWirelessUserConnectFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 62, 0, 5)
)
fsDot11WIDSWirelessUserConnectFailure.setObjects(
      *(("FS-DOT11-WIDS-MIB", "fsDot11WIDSSTAMAC"),
        ("FS-DOT11-WIDS-MIB", "fsDot11WIDSAPBSSID"),
        ("FS-DOT11-WIDS-MIB", "fsDot11WIDSInformation"),
        ("FS-DOT11-WIDS-MIB", "fsDot11WIDSextinfo"))
)
if mibBuilder.loadTexts:
    fsDot11WIDSWirelessUserConnectFailure.setStatus(
        "current"
    )

fsDot11WIDSDevice = NotificationType(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 62, 0, 6)
)
fsDot11WIDSDevice.setObjects(
      *(("FS-DOT11-WIDS-MIB", "fsDot11WIDSDeviceInfoNUM"),
        ("FS-DOT11-WIDS-MIB", "fsDot11WIDSDeviceInfoTYPE"),
        ("FS-DOT11-WIDS-MIB", "fsDot11WIDSDeviceInfoOper"),
        ("FS-DOT11-WIDS-MIB", "fsDot11WIDSDeviceInfoMAC"),
        ("FS-DOT11-WIDS-MIB", "fsDot11WIDSDeviceInfoString"))
)
if mibBuilder.loadTexts:
    fsDot11WIDSDevice.setStatus(
        "current"
    )

fsDot11WIDSSuspiciousDeviceTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 62, 0, 7)
)
fsDot11WIDSSuspiciousDeviceTrap.setObjects(
      *(("FS-DOT11-WIDS-MIB", "fsDot11WIDSSuspiciousDeviceMac"),
        ("FS-DOT11-WIDS-MIB", "fsDot11WIDSSuspiciousDeviceExtensionInfo"))
)
if mibBuilder.loadTexts:
    fsDot11WIDSSuspiciousDeviceTrap.setStatus(
        "current"
    )

fsDot11WIDSUnauthorizedSSIDTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 62, 0, 8)
)
fsDot11WIDSUnauthorizedSSIDTrap.setObjects(
      *(("FS-DOT11-WIDS-MIB", "fsDot11WIDSUnauthorizedSSID"),
        ("FS-DOT11-WIDS-MIB", "fsDot11WIDSSUnauthorizedSSIDExtensionInfo"))
)
if mibBuilder.loadTexts:
    fsDot11WIDSUnauthorizedSSIDTrap.setStatus(
        "current"
    )

fsDot11WIDSDetectingAttackTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 62, 0, 9)
)
fsDot11WIDSDetectingAttackTrap.setObjects(
      *(("FS-DOT11-WIDS-MIB", "fsDot11WIDSAttackingDeviceMac"),
        ("FS-DOT11-WIDS-MIB", "fsDot11WIDSAttackType"),
        ("FS-DOT11-WIDS-MIB", "fsDot11WIDSAttackExtensionInfo"))
)
if mibBuilder.loadTexts:
    fsDot11WIDSDetectingAttackTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance

fsDot11WIDSMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 62, 4, 1, 1)
)
fsDot11WIDSMIBCompliance.setObjects(
    ("FS-DOT11-WIDS-MIB", "fsDot11WIDSMIBGroup")
)
if mibBuilder.loadTexts:
    fsDot11WIDSMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FS-DOT11-WIDS-MIB",
    **{"fsDot11WIDSMIB": fsDot11WIDSMIB,
       "fsDot11WIDSTraps": fsDot11WIDSTraps,
       "fsDot11WIDSWirelessUserConnect": fsDot11WIDSWirelessUserConnect,
       "fsDot11WIDSWirelessUserDisconnect": fsDot11WIDSWirelessUserDisconnect,
       "fsDot11WIDSWirelessUserReauthentication": fsDot11WIDSWirelessUserReauthentication,
       "fsDot11WIDSWirelessUserAuthenticationFailure": fsDot11WIDSWirelessUserAuthenticationFailure,
       "fsDot11WIDSWirelessUserConnectFailure": fsDot11WIDSWirelessUserConnectFailure,
       "fsDot11WIDSDevice": fsDot11WIDSDevice,
       "fsDot11WIDSSuspiciousDeviceTrap": fsDot11WIDSSuspiciousDeviceTrap,
       "fsDot11WIDSUnauthorizedSSIDTrap": fsDot11WIDSUnauthorizedSSIDTrap,
       "fsDot11WIDSDetectingAttackTrap": fsDot11WIDSDetectingAttackTrap,
       "fsDot11WIDSConfigObjects": fsDot11WIDSConfigObjects,
       "fsDot11WIDSPermitVendorTable": fsDot11WIDSPermitVendorTable,
       "fsDot11WIDSPermitVendorEntry": fsDot11WIDSPermitVendorEntry,
       "fsDot11VendorOUI": fsDot11VendorOUI,
       "fsDot11VendorOper": fsDot11VendorOper,
       "fsDot11VendorName": fsDot11VendorName,
       "fsDot11WIDSPermitSSIDTable": fsDot11WIDSPermitSSIDTable,
       "fsDot11WIDSPermitSSIDEntry": fsDot11WIDSPermitSSIDEntry,
       "fsDot11PermitNum": fsDot11PermitNum,
       "fsDot11PermitOper": fsDot11PermitOper,
       "fsDot11PermitSSID": fsDot11PermitSSID,
       "fsDot11WIDSDeviceAttackMacaddressListTable": fsDot11WIDSDeviceAttackMacaddressListTable,
       "fsDot11WIDSDeviceAttackMacaddressListEntry": fsDot11WIDSDeviceAttackMacaddressListEntry,
       "fsDot11AttackNum": fsDot11AttackNum,
       "fsDot11AttackOper": fsDot11AttackOper,
       "fsDot11AttackMAC": fsDot11AttackMAC,
       "fsDot11AttackInfo": fsDot11AttackInfo,
       "fsDot11WIDSDevicePermitMacaddressListTable": fsDot11WIDSDevicePermitMacaddressListTable,
       "fsDot11WIDSDevicePermitMacaddressListEntry": fsDot11WIDSDevicePermitMacaddressListEntry,
       "fsDot11PermitMACNum": fsDot11PermitMACNum,
       "fsDot11PermitMACOper": fsDot11PermitMACOper,
       "fsDot11PermitMACAddr": fsDot11PermitMACAddr,
       "fsDot11WIDSDeviceagingDuration": fsDot11WIDSDeviceagingDuration,
       "fsDot11WIDSCountermeasuresMode": fsDot11WIDSCountermeasuresMode,
       "fsDot11WIDSCountermeasureSet": fsDot11WIDSCountermeasureSet,
       "fsDot11WIDSModeTable": fsDot11WIDSModeTable,
       "fsDot11WIDSModeEntry": fsDot11WIDSModeEntry,
       "fsDot11WIDSAPID": fsDot11WIDSAPID,
       "fsDot11WIDSDeviceMode": fsDot11WIDSDeviceMode,
       "fsDot11WIDSWhitelistMacaddressListTable": fsDot11WIDSWhitelistMacaddressListTable,
       "fsDot11WIDSWhitelistMacaddressListEntry": fsDot11WIDSWhitelistMacaddressListEntry,
       "fsDot11WhitelistNum": fsDot11WhitelistNum,
       "fsDot11WhitelistOper": fsDot11WhitelistOper,
       "fsDot11WhitelistMAC": fsDot11WhitelistMAC,
       "fsDot11WIDSStaticblackListTable": fsDot11WIDSStaticblackListTable,
       "fsDot11WIDSStaticblackListEntry": fsDot11WIDSStaticblackListEntry,
       "fsDot11StaticblacklistNum": fsDot11StaticblacklistNum,
       "fsDot11StaticblacklistOper": fsDot11StaticblacklistOper,
       "fsDot11StaticblacklistMAC": fsDot11StaticblacklistMAC,
       "fsDot11WIDSDynamicblacklistEnable": fsDot11WIDSDynamicblacklistEnable,
       "fsDot11WIDSDynamicblacklistLifetime": fsDot11WIDSDynamicblacklistLifetime,
       "fsDot11WIDSAttackDetectionMode": fsDot11WIDSAttackDetectionMode,
       "fsDot11WIDSRogueInfoTable": fsDot11WIDSRogueInfoTable,
       "fsDot11WIDSRogueInfoEntry": fsDot11WIDSRogueInfoEntry,
       "fsDot11WIDSRogueInfoNUM": fsDot11WIDSRogueInfoNUM,
       "fsDot11WIDSRogueInfoTYPE": fsDot11WIDSRogueInfoTYPE,
       "fsDot11WIDSRogueInfoOper": fsDot11WIDSRogueInfoOper,
       "fsDot11WIDSRogueInfoMAC": fsDot11WIDSRogueInfoMAC,
       "fsDot11WIDSRogueInfoString": fsDot11WIDSRogueInfoString,
       "fsDot11WIDSPermitmaclistEnableTable": fsDot11WIDSPermitmaclistEnableTable,
       "fsDot11WIDSPermitmaclistEnableEntry": fsDot11WIDSPermitmaclistEnableEntry,
       "fsDot11WIDSEnableVlanPermitmaclistNum": fsDot11WIDSEnableVlanPermitmaclistNum,
       "fsDot11WIDSEnableVlanPermitmaclistOper": fsDot11WIDSEnableVlanPermitmaclistOper,
       "fsDot11WIDSEnableVlanPermitmaclist": fsDot11WIDSEnableVlanPermitmaclist,
       "fsDot11WIDSResetStatistics": fsDot11WIDSResetStatistics,
       "fsDot11WIDSResetRoguehistoryStatistics": fsDot11WIDSResetRoguehistoryStatistics,
       "fsDot11WIDSResethistory": fsDot11WIDSResethistory,
       "fsDot11WIDSResetDynamicBlacklistTable": fsDot11WIDSResetDynamicBlacklistTable,
       "fsDot11WIDSResetDynamicBlacklistEntry": fsDot11WIDSResetDynamicBlacklistEntry,
       "fsDot11WIDSResetDynamicBlacklistMac": fsDot11WIDSResetDynamicBlacklistMac,
       "fsDot11WIDSResetDynamicBlacklistType": fsDot11WIDSResetDynamicBlacklistType,
       "fsDot11WIDResetUserisolationStatistics": fsDot11WIDResetUserisolationStatistics,
       "fsDot11WIDUserisolationAC": fsDot11WIDUserisolationAC,
       "fsDot11WIDUserisolationAP": fsDot11WIDUserisolationAP,
       "fsDot11WIDSShowStaticsTable": fsDot11WIDSShowStaticsTable,
       "fsDot11WIDSShowStaticsEntry": fsDot11WIDSShowStaticsEntry,
       "fsDot11WIDSShowStaticsNum": fsDot11WIDSShowStaticsNum,
       "fsDot11WIDSShowStaticsOper": fsDot11WIDSShowStaticsOper,
       "fsDot11WIDSShowStaticsMac": fsDot11WIDSShowStaticsMac,
       "fsDot11WIDSShowStaticsInfo": fsDot11WIDSShowStaticsInfo,
       "fsDot11WIDSAssociationFailureTotalTimes": fsDot11WIDSAssociationFailureTotalTimes,
       "fsDot11WIDSSuspiciousAPInfoTable": fsDot11WIDSSuspiciousAPInfoTable,
       "fsDot11WIDSSuspiciousAPInfoEntry": fsDot11WIDSSuspiciousAPInfoEntry,
       "fsDot11WIDSSuspiciousAPBSS": fsDot11WIDSSuspiciousAPBSS,
       "fsDot11WIDSSuspiciousAPCount": fsDot11WIDSSuspiciousAPCount,
       "fsDot11WIDSMomentFirstTimeDetectedSusAP": fsDot11WIDSMomentFirstTimeDetectedSusAP,
       "fsDot11WIDSMomentLastTimeDetectedSusAP": fsDot11WIDSMomentLastTimeDetectedSusAP,
       "fsDot11WIDSSuspiciousAPSSID": fsDot11WIDSSuspiciousAPSSID,
       "fsDot11WIDSSuspiciousAPMaxSignalStrength": fsDot11WIDSSuspiciousAPMaxSignalStrength,
       "fsDot11WIDSSuspiciousAPUsingChannel": fsDot11WIDSSuspiciousAPUsingChannel,
       "fsDot11WIDSSuspiciousAPFrameEncrption": fsDot11WIDSSuspiciousAPFrameEncrption,
       "fsDot11WIDSSuspiciousAPNeedsDealingTag": fsDot11WIDSSuspiciousAPNeedsDealingTag,
       "fsDot11WIDSSuspiciousAPIgnoredTag": fsDot11WIDSSuspiciousAPIgnoredTag,
       "fsDot11WIDSSuspiciousSTAInfoTable": fsDot11WIDSSuspiciousSTAInfoTable,
       "fsDot11WIDSSuspiciousSTAInfoEntry": fsDot11WIDSSuspiciousSTAInfoEntry,
       "fsDot11WIDSSuspiciousSTAMAC": fsDot11WIDSSuspiciousSTAMAC,
       "fsDot11WIDSAPCountDetectingSuspiciousSTA": fsDot11WIDSAPCountDetectingSuspiciousSTA,
       "fsDot11WIDSMomentFirstTimeDetectedSusSTA": fsDot11WIDSMomentFirstTimeDetectedSusSTA,
       "fsDot11WIDSMomentLastTimeDetectedSusSTA": fsDot11WIDSMomentLastTimeDetectedSusSTA,
       "fsDot11WIDSBSSIDSuspiciousSTAAccessing": fsDot11WIDSBSSIDSuspiciousSTAAccessing,
       "fsDot11WIDSSuspiciousSTAMaxSignalStrength": fsDot11WIDSSuspiciousSTAMaxSignalStrength,
       "fsDot11WIDSSuspiciousSTAUsingChannel": fsDot11WIDSSuspiciousSTAUsingChannel,
       "fsDot11WIDSSuspiciousSTAWorksInAdhocMode": fsDot11WIDSSuspiciousSTAWorksInAdhocMode,
       "fsDot11WIDSSuspiciousSTANeedsDealingTag": fsDot11WIDSSuspiciousSTANeedsDealingTag,
       "fsDot11WIDSSuspiciousSTAIgnoredTag": fsDot11WIDSSuspiciousSTAIgnoredTag,
       "fsDot11WIDSDetectObjects": fsDot11WIDSDetectObjects,
       "fsDot11WIDSShowDot11IdsAttacklistTable": fsDot11WIDSShowDot11IdsAttacklistTable,
       "fsDot11WIDSShowDot11IdsAttacklistEntry": fsDot11WIDSShowDot11IdsAttacklistEntry,
       "fsDot11WIDSShowDot11IdsAttacklistNum": fsDot11WIDSShowDot11IdsAttacklistNum,
       "fsDot11WIDSShowDot11IdsAttacklistOper": fsDot11WIDSShowDot11IdsAttacklistOper,
       "fsDot11WIDSShowDot11IdsAttacklistMac": fsDot11WIDSShowDot11IdsAttacklistMac,
       "fsDot11WIDSShowDot11IdsAttacklistInfo": fsDot11WIDSShowDot11IdsAttacklistInfo,
       "fsDot11WIDSTrapsObjects": fsDot11WIDSTrapsObjects,
       "fsDot11WIDSSTAMAC": fsDot11WIDSSTAMAC,
       "fsDot11WIDSAPBSSID": fsDot11WIDSAPBSSID,
       "fsDot11WIDSInformation": fsDot11WIDSInformation,
       "fsDot11WIDSextinfo": fsDot11WIDSextinfo,
       "fsDot11WIDSDeviceInfoNUM": fsDot11WIDSDeviceInfoNUM,
       "fsDot11WIDSDeviceInfoTYPE": fsDot11WIDSDeviceInfoTYPE,
       "fsDot11WIDSDeviceInfoOper": fsDot11WIDSDeviceInfoOper,
       "fsDot11WIDSDeviceInfoMAC": fsDot11WIDSDeviceInfoMAC,
       "fsDot11WIDSDeviceInfoString": fsDot11WIDSDeviceInfoString,
       "fsDot11WIDSSuspiciousDeviceMac": fsDot11WIDSSuspiciousDeviceMac,
       "fsDot11WIDSSuspiciousDeviceExtensionInfo": fsDot11WIDSSuspiciousDeviceExtensionInfo,
       "fsDot11WIDSUnauthorizedSSID": fsDot11WIDSUnauthorizedSSID,
       "fsDot11WIDSSUnauthorizedSSIDExtensionInfo": fsDot11WIDSSUnauthorizedSSIDExtensionInfo,
       "fsDot11WIDSAttackingDeviceMac": fsDot11WIDSAttackingDeviceMac,
       "fsDot11WIDSAttackType": fsDot11WIDSAttackType,
       "fsDot11WIDSAttackExtensionInfo": fsDot11WIDSAttackExtensionInfo,
       "fsDot11WIDSMIBConform": fsDot11WIDSMIBConform,
       "fsDot11WIDSMIBCompliances": fsDot11WIDSMIBCompliances,
       "fsDot11WIDSMIBCompliance": fsDot11WIDSMIBCompliance,
       "fsDot11WIDSMIBGroups": fsDot11WIDSMIBGroups,
       "fsDot11WIDSMIBGroup": fsDot11WIDSMIBGroup}
)
