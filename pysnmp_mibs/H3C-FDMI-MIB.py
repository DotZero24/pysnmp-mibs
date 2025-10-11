# SNMP MIB module (H3C-FDMI-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/h3c/H3C-FDMI-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:20:00 2025
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

(FcNameIdOrZero,
 fcmInstanceIndex) = mibBuilder.importSymbols(
    "FC-MGMT-MIB",
    "FcNameIdOrZero",
    "fcmInstanceIndex")

(h3cSan,) = mibBuilder.importSymbols(
    "H3C-VSAN-MIB",
    "h3cSan")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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

(T11FabricIndex,) = mibBuilder.importSymbols(
    "T11-TC-MIB",
    "T11FabricIndex")


# MODULE-IDENTITY

h3cFdmi = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 7)
)
if mibBuilder.loadTexts:
    h3cFdmi.setRevisions(
        ("2012-06-18 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_H3cFdmiObjects_ObjectIdentity = ObjectIdentity
h3cFdmiObjects = _H3cFdmiObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 7, 1)
)
_H3cFdmiInfo_ObjectIdentity = ObjectIdentity
h3cFdmiInfo = _H3cFdmiInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 7, 1, 1)
)
_H3cFdmiHbaInfoTable_Object = MibTable
h3cFdmiHbaInfoTable = _H3cFdmiHbaInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 7, 1, 1, 1)
)
if mibBuilder.loadTexts:
    h3cFdmiHbaInfoTable.setStatus("current")
_H3cFdmiHbaInfoEntry_Object = MibTableRow
h3cFdmiHbaInfoEntry = _H3cFdmiHbaInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 7, 1, 1, 1, 1)
)
h3cFdmiHbaInfoEntry.setIndexNames(
    (0, "FC-MGMT-MIB", "fcmInstanceIndex"),
    (0, "H3C-FDMI-MIB", "h3cFdmiHbaInfoFabricIndex"),
    (0, "H3C-FDMI-MIB", "h3cFdmiHbaInfoId"),
)
if mibBuilder.loadTexts:
    h3cFdmiHbaInfoEntry.setStatus("current")
_H3cFdmiHbaInfoFabricIndex_Type = T11FabricIndex
_H3cFdmiHbaInfoFabricIndex_Object = MibTableColumn
h3cFdmiHbaInfoFabricIndex = _H3cFdmiHbaInfoFabricIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 7, 1, 1, 1, 1, 1),
    _H3cFdmiHbaInfoFabricIndex_Type()
)
h3cFdmiHbaInfoFabricIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cFdmiHbaInfoFabricIndex.setStatus("current")
_H3cFdmiHbaInfoId_Type = FcNameIdOrZero
_H3cFdmiHbaInfoId_Object = MibTableColumn
h3cFdmiHbaInfoId = _H3cFdmiHbaInfoId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 7, 1, 1, 1, 1, 2),
    _H3cFdmiHbaInfoId_Type()
)
h3cFdmiHbaInfoId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cFdmiHbaInfoId.setStatus("current")
_H3cFdmiHbaInfoNodeName_Type = FcNameIdOrZero
_H3cFdmiHbaInfoNodeName_Object = MibTableColumn
h3cFdmiHbaInfoNodeName = _H3cFdmiHbaInfoNodeName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 7, 1, 1, 1, 1, 3),
    _H3cFdmiHbaInfoNodeName_Type()
)
h3cFdmiHbaInfoNodeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cFdmiHbaInfoNodeName.setStatus("current")
_H3cFdmiHbaInfoMfg_Type = SnmpAdminString
_H3cFdmiHbaInfoMfg_Object = MibTableColumn
h3cFdmiHbaInfoMfg = _H3cFdmiHbaInfoMfg_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 7, 1, 1, 1, 1, 4),
    _H3cFdmiHbaInfoMfg_Type()
)
h3cFdmiHbaInfoMfg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cFdmiHbaInfoMfg.setStatus("current")
_H3cFdmiHbaInfoSn_Type = SnmpAdminString
_H3cFdmiHbaInfoSn_Object = MibTableColumn
h3cFdmiHbaInfoSn = _H3cFdmiHbaInfoSn_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 7, 1, 1, 1, 1, 5),
    _H3cFdmiHbaInfoSn_Type()
)
h3cFdmiHbaInfoSn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cFdmiHbaInfoSn.setStatus("current")
_H3cFdmiHbaInfoModel_Type = SnmpAdminString
_H3cFdmiHbaInfoModel_Object = MibTableColumn
h3cFdmiHbaInfoModel = _H3cFdmiHbaInfoModel_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 7, 1, 1, 1, 1, 6),
    _H3cFdmiHbaInfoModel_Type()
)
h3cFdmiHbaInfoModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cFdmiHbaInfoModel.setStatus("current")
_H3cFdmiHbaInfoModelDescr_Type = SnmpAdminString
_H3cFdmiHbaInfoModelDescr_Object = MibTableColumn
h3cFdmiHbaInfoModelDescr = _H3cFdmiHbaInfoModelDescr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 7, 1, 1, 1, 1, 7),
    _H3cFdmiHbaInfoModelDescr_Type()
)
h3cFdmiHbaInfoModelDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cFdmiHbaInfoModelDescr.setStatus("current")
_H3cFdmiHbaInfoHwVer_Type = SnmpAdminString
_H3cFdmiHbaInfoHwVer_Object = MibTableColumn
h3cFdmiHbaInfoHwVer = _H3cFdmiHbaInfoHwVer_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 7, 1, 1, 1, 1, 8),
    _H3cFdmiHbaInfoHwVer_Type()
)
h3cFdmiHbaInfoHwVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cFdmiHbaInfoHwVer.setStatus("current")
_H3cFdmiHbaInfoDriverVer_Type = SnmpAdminString
_H3cFdmiHbaInfoDriverVer_Object = MibTableColumn
h3cFdmiHbaInfoDriverVer = _H3cFdmiHbaInfoDriverVer_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 7, 1, 1, 1, 1, 9),
    _H3cFdmiHbaInfoDriverVer_Type()
)
h3cFdmiHbaInfoDriverVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cFdmiHbaInfoDriverVer.setStatus("current")
_H3cFdmiHbaInfoOptROMVer_Type = SnmpAdminString
_H3cFdmiHbaInfoOptROMVer_Object = MibTableColumn
h3cFdmiHbaInfoOptROMVer = _H3cFdmiHbaInfoOptROMVer_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 7, 1, 1, 1, 1, 10),
    _H3cFdmiHbaInfoOptROMVer_Type()
)
h3cFdmiHbaInfoOptROMVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cFdmiHbaInfoOptROMVer.setStatus("current")
_H3cFdmiHbaInfoFwVer_Type = SnmpAdminString
_H3cFdmiHbaInfoFwVer_Object = MibTableColumn
h3cFdmiHbaInfoFwVer = _H3cFdmiHbaInfoFwVer_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 7, 1, 1, 1, 1, 11),
    _H3cFdmiHbaInfoFwVer_Type()
)
h3cFdmiHbaInfoFwVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cFdmiHbaInfoFwVer.setStatus("current")
_H3cFdmiHbaInfoOSInfo_Type = SnmpAdminString
_H3cFdmiHbaInfoOSInfo_Object = MibTableColumn
h3cFdmiHbaInfoOSInfo = _H3cFdmiHbaInfoOSInfo_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 7, 1, 1, 1, 1, 12),
    _H3cFdmiHbaInfoOSInfo_Type()
)
h3cFdmiHbaInfoOSInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cFdmiHbaInfoOSInfo.setStatus("current")
_H3cFdmiHbaInfoMaxCTPayload_Type = Unsigned32
_H3cFdmiHbaInfoMaxCTPayload_Object = MibTableColumn
h3cFdmiHbaInfoMaxCTPayload = _H3cFdmiHbaInfoMaxCTPayload_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 7, 1, 1, 1, 1, 13),
    _H3cFdmiHbaInfoMaxCTPayload_Type()
)
h3cFdmiHbaInfoMaxCTPayload.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cFdmiHbaInfoMaxCTPayload.setStatus("current")
_H3cFdmiHbaPortTable_Object = MibTable
h3cFdmiHbaPortTable = _H3cFdmiHbaPortTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 7, 1, 1, 2)
)
if mibBuilder.loadTexts:
    h3cFdmiHbaPortTable.setStatus("current")
_H3cFdmiHbaPortEntry_Object = MibTableRow
h3cFdmiHbaPortEntry = _H3cFdmiHbaPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 7, 1, 1, 2, 1)
)
h3cFdmiHbaPortEntry.setIndexNames(
    (0, "FC-MGMT-MIB", "fcmInstanceIndex"),
    (0, "H3C-FDMI-MIB", "h3cFdmiHbaInfoFabricIndex"),
    (0, "H3C-FDMI-MIB", "h3cFdmiHbaInfoId"),
    (0, "H3C-FDMI-MIB", "h3cFdmiHbaPortId"),
)
if mibBuilder.loadTexts:
    h3cFdmiHbaPortEntry.setStatus("current")
_H3cFdmiHbaPortId_Type = FcNameIdOrZero
_H3cFdmiHbaPortId_Object = MibTableColumn
h3cFdmiHbaPortId = _H3cFdmiHbaPortId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 7, 1, 1, 2, 1, 1),
    _H3cFdmiHbaPortId_Type()
)
h3cFdmiHbaPortId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cFdmiHbaPortId.setStatus("current")


class _H3cFdmiHbaPortSupportedFC4Type_Type(OctetString):
    """Custom type h3cFdmiHbaPortSupportedFC4Type based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(32, 32),
    )


_H3cFdmiHbaPortSupportedFC4Type_Type.__name__ = "OctetString"
_H3cFdmiHbaPortSupportedFC4Type_Object = MibTableColumn
h3cFdmiHbaPortSupportedFC4Type = _H3cFdmiHbaPortSupportedFC4Type_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 7, 1, 1, 2, 1, 2),
    _H3cFdmiHbaPortSupportedFC4Type_Type()
)
h3cFdmiHbaPortSupportedFC4Type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cFdmiHbaPortSupportedFC4Type.setStatus("current")
_H3cFdmiHbaPortSupportedSpeed_Type = Unsigned32
_H3cFdmiHbaPortSupportedSpeed_Object = MibTableColumn
h3cFdmiHbaPortSupportedSpeed = _H3cFdmiHbaPortSupportedSpeed_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 7, 1, 1, 2, 1, 3),
    _H3cFdmiHbaPortSupportedSpeed_Type()
)
h3cFdmiHbaPortSupportedSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cFdmiHbaPortSupportedSpeed.setStatus("current")
_H3cFdmiHbaPortCurrentSpeed_Type = Unsigned32
_H3cFdmiHbaPortCurrentSpeed_Object = MibTableColumn
h3cFdmiHbaPortCurrentSpeed = _H3cFdmiHbaPortCurrentSpeed_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 7, 1, 1, 2, 1, 4),
    _H3cFdmiHbaPortCurrentSpeed_Type()
)
h3cFdmiHbaPortCurrentSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cFdmiHbaPortCurrentSpeed.setStatus("current")
_H3cFdmiHbaPortMaxFrameSize_Type = Unsigned32
_H3cFdmiHbaPortMaxFrameSize_Object = MibTableColumn
h3cFdmiHbaPortMaxFrameSize = _H3cFdmiHbaPortMaxFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 7, 1, 1, 2, 1, 5),
    _H3cFdmiHbaPortMaxFrameSize_Type()
)
h3cFdmiHbaPortMaxFrameSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cFdmiHbaPortMaxFrameSize.setStatus("current")
_H3cFdmiHbaPortOsDevName_Type = SnmpAdminString
_H3cFdmiHbaPortOsDevName_Object = MibTableColumn
h3cFdmiHbaPortOsDevName = _H3cFdmiHbaPortOsDevName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 7, 1, 1, 2, 1, 6),
    _H3cFdmiHbaPortOsDevName_Type()
)
h3cFdmiHbaPortOsDevName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cFdmiHbaPortOsDevName.setStatus("current")
_H3cFdmiHbaPortHostName_Type = SnmpAdminString
_H3cFdmiHbaPortHostName_Object = MibTableColumn
h3cFdmiHbaPortHostName = _H3cFdmiHbaPortHostName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 7, 1, 1, 2, 1, 7),
    _H3cFdmiHbaPortHostName_Type()
)
h3cFdmiHbaPortHostName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cFdmiHbaPortHostName.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "H3C-FDMI-MIB",
    **{"h3cFdmi": h3cFdmi,
       "h3cFdmiObjects": h3cFdmiObjects,
       "h3cFdmiInfo": h3cFdmiInfo,
       "h3cFdmiHbaInfoTable": h3cFdmiHbaInfoTable,
       "h3cFdmiHbaInfoEntry": h3cFdmiHbaInfoEntry,
       "h3cFdmiHbaInfoFabricIndex": h3cFdmiHbaInfoFabricIndex,
       "h3cFdmiHbaInfoId": h3cFdmiHbaInfoId,
       "h3cFdmiHbaInfoNodeName": h3cFdmiHbaInfoNodeName,
       "h3cFdmiHbaInfoMfg": h3cFdmiHbaInfoMfg,
       "h3cFdmiHbaInfoSn": h3cFdmiHbaInfoSn,
       "h3cFdmiHbaInfoModel": h3cFdmiHbaInfoModel,
       "h3cFdmiHbaInfoModelDescr": h3cFdmiHbaInfoModelDescr,
       "h3cFdmiHbaInfoHwVer": h3cFdmiHbaInfoHwVer,
       "h3cFdmiHbaInfoDriverVer": h3cFdmiHbaInfoDriverVer,
       "h3cFdmiHbaInfoOptROMVer": h3cFdmiHbaInfoOptROMVer,
       "h3cFdmiHbaInfoFwVer": h3cFdmiHbaInfoFwVer,
       "h3cFdmiHbaInfoOSInfo": h3cFdmiHbaInfoOSInfo,
       "h3cFdmiHbaInfoMaxCTPayload": h3cFdmiHbaInfoMaxCTPayload,
       "h3cFdmiHbaPortTable": h3cFdmiHbaPortTable,
       "h3cFdmiHbaPortEntry": h3cFdmiHbaPortEntry,
       "h3cFdmiHbaPortId": h3cFdmiHbaPortId,
       "h3cFdmiHbaPortSupportedFC4Type": h3cFdmiHbaPortSupportedFC4Type,
       "h3cFdmiHbaPortSupportedSpeed": h3cFdmiHbaPortSupportedSpeed,
       "h3cFdmiHbaPortCurrentSpeed": h3cFdmiHbaPortCurrentSpeed,
       "h3cFdmiHbaPortMaxFrameSize": h3cFdmiHbaPortMaxFrameSize,
       "h3cFdmiHbaPortOsDevName": h3cFdmiHbaPortOsDevName,
       "h3cFdmiHbaPortHostName": h3cFdmiHbaPortHostName}
)
