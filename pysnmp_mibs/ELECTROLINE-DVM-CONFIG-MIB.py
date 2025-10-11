# SNMP MIB module (ELECTROLINE-DVM-CONFIG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/electroline/ELECTROLINE-DVM-CONFIG-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:07:04 2025
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

(TenthdB,
 TenthdBmV) = mibBuilder.importSymbols(
    "DOCS-IF-MIB",
    "TenthdB",
    "TenthdBmV")

(dvmConfiguration,) = mibBuilder.importSymbols(
    "ELECTROLINE-DVM-ROOT-MIB",
    "dvmConfiguration")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_DvmCfgGlobal_ObjectIdentity = ObjectIdentity
dvmCfgGlobal = _DvmCfgGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 3, 2, 1)
)
if mibBuilder.loadTexts:
    dvmCfgGlobal.setStatus("current")
_DvmCfgEms_ObjectIdentity = ObjectIdentity
dvmCfgEms = _DvmCfgEms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 3, 2, 1, 1)
)
if mibBuilder.loadTexts:
    dvmCfgEms.setStatus("current")
_CfgEmsAddressTable_Object = MibTable
cfgEmsAddressTable = _CfgEmsAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 3, 2, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cfgEmsAddressTable.setStatus("current")
_CfgEmsAddressEntry_Object = MibTableRow
cfgEmsAddressEntry = _CfgEmsAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 3, 2, 1, 1, 1, 1)
)
cfgEmsAddressEntry.setIndexNames(
    (0, "ELECTROLINE-DVM-CONFIG-MIB", "cfgEmsAddressIndex"),
)
if mibBuilder.loadTexts:
    cfgEmsAddressEntry.setStatus("current")
_CfgEmsAddressIndex_Type = Integer32
_CfgEmsAddressIndex_Object = MibTableColumn
cfgEmsAddressIndex = _CfgEmsAddressIndex_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 3, 2, 1, 1, 1, 1, 1),
    _CfgEmsAddressIndex_Type()
)
cfgEmsAddressIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgEmsAddressIndex.setStatus("current")
_CfgEmsAddressIP_Type = IpAddress
_CfgEmsAddressIP_Object = MibTableColumn
cfgEmsAddressIP = _CfgEmsAddressIP_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 3, 2, 1, 1, 1, 1, 2),
    _CfgEmsAddressIP_Type()
)
cfgEmsAddressIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgEmsAddressIP.setStatus("current")


class _CfgEmsAddressTrapPortNumber_Type(Integer32):
    """Custom type cfgEmsAddressTrapPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CfgEmsAddressTrapPortNumber_Type.__name__ = "Integer32"
_CfgEmsAddressTrapPortNumber_Object = MibTableColumn
cfgEmsAddressTrapPortNumber = _CfgEmsAddressTrapPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 3, 2, 1, 1, 1, 1, 3),
    _CfgEmsAddressTrapPortNumber_Type()
)
cfgEmsAddressTrapPortNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgEmsAddressTrapPortNumber.setStatus("current")
_CfgEmsAddressType_Type = InetAddressType
_CfgEmsAddressType_Object = MibTableColumn
cfgEmsAddressType = _CfgEmsAddressType_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 3, 2, 1, 1, 1, 1, 4),
    _CfgEmsAddressType_Type()
)
cfgEmsAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgEmsAddressType.setStatus("current")
_CfgEmsAddress_Type = InetAddress
_CfgEmsAddress_Object = MibTableColumn
cfgEmsAddress = _CfgEmsAddress_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 3, 2, 1, 1, 1, 1, 5),
    _CfgEmsAddress_Type()
)
cfgEmsAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgEmsAddress.setStatus("current")


class _CfgEmsAddressProtocol_Type(Integer32):
    """Custom type cfgEmsAddressProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("snmp", 1),
          ("http_post", 2))
    )


_CfgEmsAddressProtocol_Type.__name__ = "Integer32"
_CfgEmsAddressProtocol_Object = MibTableColumn
cfgEmsAddressProtocol = _CfgEmsAddressProtocol_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 3, 2, 1, 1, 1, 1, 6),
    _CfgEmsAddressProtocol_Type()
)
cfgEmsAddressProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgEmsAddressProtocol.setStatus("current")


class _DvmCfgResetToFactory_Type(Integer32):
    """Custom type dvmCfgResetToFactory based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset", 1)
    )


_DvmCfgResetToFactory_Type.__name__ = "Integer32"
_DvmCfgResetToFactory_Object = MibScalar
dvmCfgResetToFactory = _DvmCfgResetToFactory_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 3, 2, 1, 2),
    _DvmCfgResetToFactory_Type()
)
dvmCfgResetToFactory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dvmCfgResetToFactory.setStatus("current")


class _DvmCfgUsbMode_Type(Integer32):
    """Custom type dvmCfgUsbMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cpe", 1),
          ("craft", 2))
    )


_DvmCfgUsbMode_Type.__name__ = "Integer32"
_DvmCfgUsbMode_Object = MibScalar
dvmCfgUsbMode = _DvmCfgUsbMode_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 3, 2, 1, 3),
    _DvmCfgUsbMode_Type()
)
dvmCfgUsbMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dvmCfgUsbMode.setStatus("current")
_DvmChannelBondingEnable_Type = TruthValue
_DvmChannelBondingEnable_Object = MibScalar
dvmChannelBondingEnable = _DvmChannelBondingEnable_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 3, 2, 1, 4),
    _DvmChannelBondingEnable_Type()
)
dvmChannelBondingEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dvmChannelBondingEnable.setStatus("current")
_DvmCfgFpga_ObjectIdentity = ObjectIdentity
dvmCfgFpga = _DvmCfgFpga_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 3, 2, 1, 5)
)
if mibBuilder.loadTexts:
    dvmCfgFpga.setStatus("current")
_DvmCfgFpgaSoftware_ObjectIdentity = ObjectIdentity
dvmCfgFpgaSoftware = _DvmCfgFpgaSoftware_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 3, 2, 1, 5, 1)
)
if mibBuilder.loadTexts:
    dvmCfgFpgaSoftware.setStatus("current")
_DvmCfgFpgaSwServerAddressType_Type = InetAddressType
_DvmCfgFpgaSwServerAddressType_Object = MibScalar
dvmCfgFpgaSwServerAddressType = _DvmCfgFpgaSwServerAddressType_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 3, 2, 1, 5, 1, 1),
    _DvmCfgFpgaSwServerAddressType_Type()
)
dvmCfgFpgaSwServerAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dvmCfgFpgaSwServerAddressType.setStatus("current")
_DvmCfgFpgaSwServer_Type = IpAddress
_DvmCfgFpgaSwServer_Object = MibScalar
dvmCfgFpgaSwServer = _DvmCfgFpgaSwServer_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 3, 2, 1, 5, 1, 2),
    _DvmCfgFpgaSwServer_Type()
)
dvmCfgFpgaSwServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dvmCfgFpgaSwServer.setStatus("current")
_DvmCfgFpgaSwServerAddress_Type = InetAddress
_DvmCfgFpgaSwServerAddress_Object = MibScalar
dvmCfgFpgaSwServerAddress = _DvmCfgFpgaSwServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 3, 2, 1, 5, 1, 3),
    _DvmCfgFpgaSwServerAddress_Type()
)
dvmCfgFpgaSwServerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dvmCfgFpgaSwServerAddress.setStatus("current")


class _DvmCfgFpgaSwFilename_Type(SnmpAdminString):
    """Custom type dvmCfgFpgaSwFilename based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_DvmCfgFpgaSwFilename_Type.__name__ = "SnmpAdminString"
_DvmCfgFpgaSwFilename_Object = MibScalar
dvmCfgFpgaSwFilename = _DvmCfgFpgaSwFilename_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 3, 2, 1, 5, 1, 4),
    _DvmCfgFpgaSwFilename_Type()
)
dvmCfgFpgaSwFilename.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dvmCfgFpgaSwFilename.setStatus("current")
_DvmCfgFpgaSwDloadNow_Type = TruthValue
_DvmCfgFpgaSwDloadNow_Object = MibScalar
dvmCfgFpgaSwDloadNow = _DvmCfgFpgaSwDloadNow_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 3, 2, 1, 5, 1, 5),
    _DvmCfgFpgaSwDloadNow_Type()
)
dvmCfgFpgaSwDloadNow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dvmCfgFpgaSwDloadNow.setStatus("current")


class _DvmCfgFpgaSwDloadStatus_Type(Integer32):
    """Custom type dvmCfgFpgaSwDloadStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("failure", 0),
          ("success", 1),
          ("inProgress", 2),
          ("other", 3))
    )


_DvmCfgFpgaSwDloadStatus_Type.__name__ = "Integer32"
_DvmCfgFpgaSwDloadStatus_Object = MibScalar
dvmCfgFpgaSwDloadStatus = _DvmCfgFpgaSwDloadStatus_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 3, 2, 1, 5, 1, 6),
    _DvmCfgFpgaSwDloadStatus_Type()
)
dvmCfgFpgaSwDloadStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvmCfgFpgaSwDloadStatus.setStatus("current")
_DvmCfgFpgaSwCurrentVers_Type = SnmpAdminString
_DvmCfgFpgaSwCurrentVers_Object = MibScalar
dvmCfgFpgaSwCurrentVers = _DvmCfgFpgaSwCurrentVers_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 3, 2, 1, 5, 1, 7),
    _DvmCfgFpgaSwCurrentVers_Type()
)
dvmCfgFpgaSwCurrentVers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvmCfgFpgaSwCurrentVers.setStatus("current")


class _DvmCfgSystemTrapEnginFilter_Type(DisplayString):
    """Custom type dvmCfgSystemTrapEnginFilter based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_DvmCfgSystemTrapEnginFilter_Type.__name__ = "DisplayString"
_DvmCfgSystemTrapEnginFilter_Object = MibScalar
dvmCfgSystemTrapEnginFilter = _DvmCfgSystemTrapEnginFilter_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 3, 2, 1, 6),
    _DvmCfgSystemTrapEnginFilter_Type()
)
dvmCfgSystemTrapEnginFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dvmCfgSystemTrapEnginFilter.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ELECTROLINE-DVM-CONFIG-MIB",
    **{"dvmCfgGlobal": dvmCfgGlobal,
       "dvmCfgEms": dvmCfgEms,
       "cfgEmsAddressTable": cfgEmsAddressTable,
       "cfgEmsAddressEntry": cfgEmsAddressEntry,
       "cfgEmsAddressIndex": cfgEmsAddressIndex,
       "cfgEmsAddressIP": cfgEmsAddressIP,
       "cfgEmsAddressTrapPortNumber": cfgEmsAddressTrapPortNumber,
       "cfgEmsAddressType": cfgEmsAddressType,
       "cfgEmsAddress": cfgEmsAddress,
       "cfgEmsAddressProtocol": cfgEmsAddressProtocol,
       "dvmCfgResetToFactory": dvmCfgResetToFactory,
       "dvmCfgUsbMode": dvmCfgUsbMode,
       "dvmChannelBondingEnable": dvmChannelBondingEnable,
       "dvmCfgFpga": dvmCfgFpga,
       "dvmCfgFpgaSoftware": dvmCfgFpgaSoftware,
       "dvmCfgFpgaSwServerAddressType": dvmCfgFpgaSwServerAddressType,
       "dvmCfgFpgaSwServer": dvmCfgFpgaSwServer,
       "dvmCfgFpgaSwServerAddress": dvmCfgFpgaSwServerAddress,
       "dvmCfgFpgaSwFilename": dvmCfgFpgaSwFilename,
       "dvmCfgFpgaSwDloadNow": dvmCfgFpgaSwDloadNow,
       "dvmCfgFpgaSwDloadStatus": dvmCfgFpgaSwDloadStatus,
       "dvmCfgFpgaSwCurrentVers": dvmCfgFpgaSwCurrentVers,
       "dvmCfgSystemTrapEnginFilter": dvmCfgSystemTrapEnginFilter}
)
