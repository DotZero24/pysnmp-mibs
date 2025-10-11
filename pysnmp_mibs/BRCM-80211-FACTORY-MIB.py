# SNMP MIB module (BRCM-80211-FACTORY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/broadcom/BRCM-80211-FACTORY-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:08:16 2025
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

(cableDataFactory,) = mibBuilder.importSymbols(
    "BRCM-CABLEDATA-FACTORY-MIB",
    "cableDataFactory")

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


# MODULE-IDENTITY

ieee802dot11Factory = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 2, 5)
)
if mibBuilder.loadTexts:
    ieee802dot11Factory.setRevisions(
        ("2008-07-01 00:00",
         "2007-02-05 00:00",
         "2003-08-22 00:00",
         "2003-04-28 00:00",
         "2002-09-19 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Dot11FactoryCfg_ObjectIdentity = ObjectIdentity
dot11FactoryCfg = _Dot11FactoryCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 2, 5, 1)
)


class _Dot11RegDomain_Type(Integer32):
    """Custom type dot11RegDomain based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(16,
              32,
              48,
              49,
              50,
              64)
        )
    )
    namedValues = NamedValues(
        *(("fcc", 16),
          ("doc", 32),
          ("etsi", 48),
          ("spain", 49),
          ("france", 50),
          ("mkk", 64))
    )


_Dot11RegDomain_Type.__name__ = "Integer32"
_Dot11RegDomain_Object = MibScalar
dot11RegDomain = _Dot11RegDomain_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 2, 5, 1, 2),
    _Dot11RegDomain_Type()
)
dot11RegDomain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11RegDomain.setStatus("deprecated")
_Dot11BoardRev_Type = Unsigned32
_Dot11BoardRev_Object = MibScalar
dot11BoardRev = _Dot11BoardRev_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 2, 5, 1, 3),
    _Dot11BoardRev_Type()
)
dot11BoardRev.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11BoardRev.setStatus("current")
_Dot11MaxPower_Type = Unsigned32
_Dot11MaxPower_Object = MibScalar
dot11MaxPower = _Dot11MaxPower_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 2, 5, 1, 4),
    _Dot11MaxPower_Type()
)
dot11MaxPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11MaxPower.setStatus("current")


class _Dot11Country_Type(Integer32):
    """Custom type dot11Country based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("worldWide", 0),
          ("thailand", 1),
          ("israel", 2),
          ("jordan", 3),
          ("china", 4),
          ("japan", 5),
          ("usa", 6),
          ("europe", 7),
          ("allChannels", 8))
    )


_Dot11Country_Type.__name__ = "Integer32"
_Dot11Country_Object = MibScalar
dot11Country = _Dot11Country_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 2, 5, 1, 5),
    _Dot11Country_Type()
)
dot11Country.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11Country.setStatus("deprecated")


class _Dot11PAParameters_Type(OctetString):
    """Custom type dot11PAParameters based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )
    fixed_length = 6


_Dot11PAParameters_Type.__name__ = "OctetString"
_Dot11PAParameters_Object = MibScalar
dot11PAParameters = _Dot11PAParameters_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 2, 5, 1, 6),
    _Dot11PAParameters_Type()
)
dot11PAParameters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11PAParameters.setStatus("current")


class _Dot11IdleTSSI_Type(Integer32):
    """Custom type dot11IdleTSSI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Dot11IdleTSSI_Type.__name__ = "Integer32"
_Dot11IdleTSSI_Object = MibScalar
dot11IdleTSSI = _Dot11IdleTSSI_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 2, 5, 1, 7),
    _Dot11IdleTSSI_Type()
)
dot11IdleTSSI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11IdleTSSI.setStatus("current")


class _Dot11AntennaGain_Type(Integer32):
    """Custom type dot11AntennaGain based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Dot11AntennaGain_Type.__name__ = "Integer32"
_Dot11AntennaGain_Object = MibScalar
dot11AntennaGain = _Dot11AntennaGain_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 2, 5, 1, 8),
    _Dot11AntennaGain_Type()
)
dot11AntennaGain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11AntennaGain.setStatus("current")
_Dot11SromWrite_Type = OctetString
_Dot11SromWrite_Object = MibScalar
dot11SromWrite = _Dot11SromWrite_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 2, 5, 1, 9),
    _Dot11SromWrite_Type()
)
dot11SromWrite.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11SromWrite.setStatus("current")
_Dot11SromRead_Type = OctetString
_Dot11SromRead_Object = MibScalar
dot11SromRead = _Dot11SromRead_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 2, 5, 1, 10),
    _Dot11SromRead_Type()
)
dot11SromRead.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11SromRead.setStatus("current")
_Dot11IsoCountry_Type = OctetString
_Dot11IsoCountry_Object = MibScalar
dot11IsoCountry = _Dot11IsoCountry_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 2, 5, 1, 11),
    _Dot11IsoCountry_Type()
)
dot11IsoCountry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11IsoCountry.setStatus("current")
_Dot11FactoryDiagnostics_ObjectIdentity = ObjectIdentity
dot11FactoryDiagnostics = _Dot11FactoryDiagnostics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 2, 5, 2)
)


class _Dot11DiagChannel_Type(Unsigned32):
    """Custom type dot11DiagChannel based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 14),
    )


_Dot11DiagChannel_Type.__name__ = "Unsigned32"
_Dot11DiagChannel_Object = MibScalar
dot11DiagChannel = _Dot11DiagChannel_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 2, 5, 2, 1),
    _Dot11DiagChannel_Type()
)
dot11DiagChannel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11DiagChannel.setStatus("current")


class _Dot11DiagAntennaDiversity_Type(Integer32):
    """Custom type dot11DiagAntennaDiversity based on Integer32"""
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
        *(("diversityDisabledAntenna0", 0),
          ("diversityDisabledAntenna1", 1),
          ("diversityEnabledAntenna1", 2),
          ("diversityEnabledAntenna0", 3))
    )


_Dot11DiagAntennaDiversity_Type.__name__ = "Integer32"
_Dot11DiagAntennaDiversity_Object = MibScalar
dot11DiagAntennaDiversity = _Dot11DiagAntennaDiversity_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 2, 5, 2, 2),
    _Dot11DiagAntennaDiversity_Type()
)
dot11DiagAntennaDiversity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11DiagAntennaDiversity.setStatus("current")


class _Dot11DiagTxMode_Type(Integer32):
    """Custom type dot11DiagTxMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cw", 0),
          ("evm", 1),
          ("normal", 2))
    )


_Dot11DiagTxMode_Type.__name__ = "Integer32"
_Dot11DiagTxMode_Object = MibScalar
dot11DiagTxMode = _Dot11DiagTxMode_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 2, 5, 2, 3),
    _Dot11DiagTxMode_Type()
)
dot11DiagTxMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11DiagTxMode.setStatus("current")


class _Dot11DiagTxPowerLevel_Type(Integer32):
    """Custom type dot11DiagTxPowerLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_Dot11DiagTxPowerLevel_Type.__name__ = "Integer32"
_Dot11DiagTxPowerLevel_Object = MibScalar
dot11DiagTxPowerLevel = _Dot11DiagTxPowerLevel_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 2, 5, 2, 4),
    _Dot11DiagTxPowerLevel_Type()
)
dot11DiagTxPowerLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11DiagTxPowerLevel.setStatus("current")
if mibBuilder.loadTexts:
    dot11DiagTxPowerLevel.setUnits("milliwatts")
_Dot11DiagWirelessLanCmd_Type = DisplayString
_Dot11DiagWirelessLanCmd_Object = MibScalar
dot11DiagWirelessLanCmd = _Dot11DiagWirelessLanCmd_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 2, 5, 2, 5),
    _Dot11DiagWirelessLanCmd_Type()
)
dot11DiagWirelessLanCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11DiagWirelessLanCmd.setStatus("current")
_Dot11DiagWirelessLanOutput_Type = OctetString
_Dot11DiagWirelessLanOutput_Object = MibScalar
dot11DiagWirelessLanOutput = _Dot11DiagWirelessLanOutput_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 2, 5, 2, 6),
    _Dot11DiagWirelessLanOutput_Type()
)
dot11DiagWirelessLanOutput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot11DiagWirelessLanOutput.setStatus("current")
_Dot11FactoryWPSSettings_ObjectIdentity = ObjectIdentity
dot11FactoryWPSSettings = _Dot11FactoryWPSSettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 2, 5, 3)
)


class _Dot11WPSBoardNum_Type(SnmpAdminString):
    """Custom type dot11WPSBoardNum based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Dot11WPSBoardNum_Type.__name__ = "SnmpAdminString"
_Dot11WPSBoardNum_Object = MibScalar
dot11WPSBoardNum = _Dot11WPSBoardNum_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 2, 5, 3, 1),
    _Dot11WPSBoardNum_Type()
)
dot11WPSBoardNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11WPSBoardNum.setStatus("current")


class _Dot11WPSDeviceName_Type(SnmpAdminString):
    """Custom type dot11WPSDeviceName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Dot11WPSDeviceName_Type.__name__ = "SnmpAdminString"
_Dot11WPSDeviceName_Object = MibScalar
dot11WPSDeviceName = _Dot11WPSDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 2, 5, 3, 2),
    _Dot11WPSDeviceName_Type()
)
dot11WPSDeviceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11WPSDeviceName.setStatus("current")


class _Dot11WPSDevicePin_Type(SnmpAdminString):
    """Custom type dot11WPSDevicePin based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_Dot11WPSDevicePin_Type.__name__ = "SnmpAdminString"
_Dot11WPSDevicePin_Object = MibScalar
dot11WPSDevicePin = _Dot11WPSDevicePin_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 2, 5, 3, 3),
    _Dot11WPSDevicePin_Type()
)
dot11WPSDevicePin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11WPSDevicePin.setStatus("current")


class _Dot11WPSMfgName_Type(SnmpAdminString):
    """Custom type dot11WPSMfgName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Dot11WPSMfgName_Type.__name__ = "SnmpAdminString"
_Dot11WPSMfgName_Object = MibScalar
dot11WPSMfgName = _Dot11WPSMfgName_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 2, 5, 3, 4),
    _Dot11WPSMfgName_Type()
)
dot11WPSMfgName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11WPSMfgName.setStatus("current")


class _Dot11WPSModelName_Type(SnmpAdminString):
    """Custom type dot11WPSModelName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Dot11WPSModelName_Type.__name__ = "SnmpAdminString"
_Dot11WPSModelName_Object = MibScalar
dot11WPSModelName = _Dot11WPSModelName_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 2, 5, 3, 5),
    _Dot11WPSModelName_Type()
)
dot11WPSModelName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11WPSModelName.setStatus("current")


class _Dot11WPSModelNum_Type(SnmpAdminString):
    """Custom type dot11WPSModelNum based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Dot11WPSModelNum_Type.__name__ = "SnmpAdminString"
_Dot11WPSModelNum_Object = MibScalar
dot11WPSModelNum = _Dot11WPSModelNum_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 2, 5, 3, 6),
    _Dot11WPSModelNum_Type()
)
dot11WPSModelNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11WPSModelNum.setStatus("current")


class _Dot11WPSUUID_Type(SnmpAdminString):
    """Custom type dot11WPSUUID based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Dot11WPSUUID_Type.__name__ = "SnmpAdminString"
_Dot11WPSUUID_Object = MibScalar
dot11WPSUUID = _Dot11WPSUUID_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 2, 5, 3, 7),
    _Dot11WPSUUID_Type()
)
dot11WPSUUID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot11WPSUUID.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BRCM-80211-FACTORY-MIB",
    **{"ieee802dot11Factory": ieee802dot11Factory,
       "dot11FactoryCfg": dot11FactoryCfg,
       "dot11RegDomain": dot11RegDomain,
       "dot11BoardRev": dot11BoardRev,
       "dot11MaxPower": dot11MaxPower,
       "dot11Country": dot11Country,
       "dot11PAParameters": dot11PAParameters,
       "dot11IdleTSSI": dot11IdleTSSI,
       "dot11AntennaGain": dot11AntennaGain,
       "dot11SromWrite": dot11SromWrite,
       "dot11SromRead": dot11SromRead,
       "dot11IsoCountry": dot11IsoCountry,
       "dot11FactoryDiagnostics": dot11FactoryDiagnostics,
       "dot11DiagChannel": dot11DiagChannel,
       "dot11DiagAntennaDiversity": dot11DiagAntennaDiversity,
       "dot11DiagTxMode": dot11DiagTxMode,
       "dot11DiagTxPowerLevel": dot11DiagTxPowerLevel,
       "dot11DiagWirelessLanCmd": dot11DiagWirelessLanCmd,
       "dot11DiagWirelessLanOutput": dot11DiagWirelessLanOutput,
       "dot11FactoryWPSSettings": dot11FactoryWPSSettings,
       "dot11WPSBoardNum": dot11WPSBoardNum,
       "dot11WPSDeviceName": dot11WPSDeviceName,
       "dot11WPSDevicePin": dot11WPSDevicePin,
       "dot11WPSMfgName": dot11WPSMfgName,
       "dot11WPSModelName": dot11WPSModelName,
       "dot11WPSModelNum": dot11WPSModelNum,
       "dot11WPSUUID": dot11WPSUUID}
)
