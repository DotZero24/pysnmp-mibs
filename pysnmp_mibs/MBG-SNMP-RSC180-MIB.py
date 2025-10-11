# SNMP MIB module (MBG-SNMP-RSC180-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/meinberg/MBG-SNMP-RSC180-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:07:07 2025
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

(mbgSnmpRoot,) = mibBuilder.importSymbols(
    "MBG-SNMP-ROOT-MIB",
    "mbgSnmpRoot")

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
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

mbgRSC180 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5597, 80)
)
if mibBuilder.loadTexts:
    mbgRSC180.setRevisions(
        ("2012-01-25 00:00",
         "2006-01-20 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class MeinbergRefClockTyp(TextualConvention, Integer32):
    status = "current"
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
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              50,
              51,
              52)
        )
    )
    namedValues = NamedValues(
        *(("notAvailable", 0),
          ("gps166", 1),
          ("gps167", 2),
          ("gps167SV", 3),
          ("gps167PC", 4),
          ("gps167PCI", 5),
          ("gps163", 6),
          ("gps168PCI", 7),
          ("gps161", 8),
          ("gps169PCI", 9),
          ("tcr167PCI", 10),
          ("gps164", 11),
          ("gps170PCI", 12),
          ("pzf511", 13),
          ("gps170", 14),
          ("tcr511", 15),
          ("am511", 16),
          ("msf511", 17),
          ("grc170", 18),
          ("gps170PEX", 19),
          ("gps162", 20),
          ("ptp270PEX", 21),
          ("frc511PEX", 22),
          ("gen170", 23),
          ("tcr170PEX", 24),
          ("wwvb511", 25),
          ("mbg170", 26),
          ("jjy511", 27),
          ("pzf600", 28),
          ("tcr600", 29),
          ("gps180", 30),
          ("gln170", 31),
          ("gps180PEX", 32),
          ("tcr180PEX", 33),
          ("pzf180PEX", 34),
          ("mbg180", 35),
          ("msf600", 36),
          ("wwvb600", 37),
          ("jjy600", 38),
          ("gps180HS", 39),
          ("gps180AMC", 40),
          ("esi180", 41),
          ("cpe180", 42),
          ("lno180", 43),
          ("grc180", 44),
          ("liu", 45),
          ("dcf600HS", 46),
          ("dcf600RS", 47),
          ("mri", 48),
          ("bpe", 49),
          ("gln180pex", 50),
          ("n2x", 51),
          ("rsc180", 52))
    )



# MIB Managed Objects in the order of their OIDs

_MbgRefClock_ObjectIdentity = ObjectIdentity
mbgRefClock = _MbgRefClock_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5597, 80, 0)
)
_MbgRefClockStatus_ObjectIdentity = ObjectIdentity
mbgRefClockStatus = _MbgRefClockStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5597, 80, 0, 0)
)
_MbgRefClockTable_Object = MibTable
mbgRefClockTable = _MbgRefClockTable_Object(
    (1, 3, 6, 1, 4, 1, 5597, 80, 0, 0, 1)
)
if mibBuilder.loadTexts:
    mbgRefClockTable.setStatus("current")
_MbgRefClockTableEntry_Object = MibTableRow
mbgRefClockTableEntry = _MbgRefClockTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 5597, 80, 0, 0, 1, 1)
)
mbgRefClockTableEntry.setIndexNames(
    (0, "MBG-SNMP-RSC180-MIB", "mbgClkTableIndex"),
)
if mibBuilder.loadTexts:
    mbgRefClockTableEntry.setStatus("current")
_MbgClkTableIndex_Type = Unsigned32
_MbgClkTableIndex_Object = MibTableColumn
mbgClkTableIndex = _MbgClkTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 5597, 80, 0, 0, 1, 1, 1),
    _MbgClkTableIndex_Type()
)
mbgClkTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mbgClkTableIndex.setStatus("current")


class _MbgClkType_Type(MeinbergRefClockTyp):
    """Custom type mbgClkType based on MeinbergRefClockTyp"""
    defaultValue = 0


_MbgClkType_Type.__name__ = "MeinbergRefClockTyp"
_MbgClkType_Object = MibTableColumn
mbgClkType = _MbgClkType_Object(
    (1, 3, 6, 1, 4, 1, 5597, 80, 0, 0, 1, 1, 2),
    _MbgClkType_Type()
)
mbgClkType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgClkType.setStatus("current")
_MbgClkSerialNo_Type = DisplayString
_MbgClkSerialNo_Object = MibTableColumn
mbgClkSerialNo = _MbgClkSerialNo_Object(
    (1, 3, 6, 1, 4, 1, 5597, 80, 0, 0, 1, 1, 3),
    _MbgClkSerialNo_Type()
)
mbgClkSerialNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgClkSerialNo.setStatus("current")
_MbgClkFirmwareRev_Type = DisplayString
_MbgClkFirmwareRev_Object = MibTableColumn
mbgClkFirmwareRev = _MbgClkFirmwareRev_Object(
    (1, 3, 6, 1, 4, 1, 5597, 80, 0, 0, 1, 1, 4),
    _MbgClkFirmwareRev_Type()
)
mbgClkFirmwareRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgClkFirmwareRev.setStatus("current")


class _MbgClkMode_Type(Integer32):
    """Custom type mbgClkMode based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("notAvailable", 0),
          ("normalOperation", 1),
          ("trackingSearching", 2),
          ("antennaFaulty", 3),
          ("warmBoot", 4),
          ("coldBoot", 5))
    )


_MbgClkMode_Type.__name__ = "Integer32"
_MbgClkMode_Object = MibTableColumn
mbgClkMode = _MbgClkMode_Object(
    (1, 3, 6, 1, 4, 1, 5597, 80, 0, 0, 1, 1, 5),
    _MbgClkMode_Type()
)
mbgClkMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgClkMode.setStatus("current")


class _MbgGpsState_Type(Integer32):
    """Custom type mbgGpsState based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notAvailable", 0),
          ("synchronized", 1),
          ("notSynchronized", 2))
    )


_MbgGpsState_Type.__name__ = "Integer32"
_MbgGpsState_Object = MibTableColumn
mbgGpsState = _MbgGpsState_Object(
    (1, 3, 6, 1, 4, 1, 5597, 80, 0, 0, 1, 1, 6),
    _MbgGpsState_Type()
)
mbgGpsState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgGpsState.setStatus("current")
_MbgGpsPosition_Type = DisplayString
_MbgGpsPosition_Object = MibTableColumn
mbgGpsPosition = _MbgGpsPosition_Object(
    (1, 3, 6, 1, 4, 1, 5597, 80, 0, 0, 1, 1, 7),
    _MbgGpsPosition_Type()
)
mbgGpsPosition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgGpsPosition.setStatus("current")
_MbgGpsSatellitesGood_Type = Integer32
_MbgGpsSatellitesGood_Object = MibTableColumn
mbgGpsSatellitesGood = _MbgGpsSatellitesGood_Object(
    (1, 3, 6, 1, 4, 1, 5597, 80, 0, 0, 1, 1, 8),
    _MbgGpsSatellitesGood_Type()
)
mbgGpsSatellitesGood.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgGpsSatellitesGood.setStatus("current")
_MbgGpsSatellitesInView_Type = Integer32
_MbgGpsSatellitesInView_Object = MibTableColumn
mbgGpsSatellitesInView = _MbgGpsSatellitesInView_Object(
    (1, 3, 6, 1, 4, 1, 5597, 80, 0, 0, 1, 1, 9),
    _MbgGpsSatellitesInView_Type()
)
mbgGpsSatellitesInView.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgGpsSatellitesInView.setStatus("current")


class _MbgGPSNavSolved_Type(Integer32):
    """Custom type mbgGPSNavSolved based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_MbgGPSNavSolved_Type.__name__ = "Integer32"
_MbgGPSNavSolved_Object = MibTableColumn
mbgGPSNavSolved = _MbgGPSNavSolved_Object(
    (1, 3, 6, 1, 4, 1, 5597, 80, 0, 0, 1, 1, 10),
    _MbgGPSNavSolved_Type()
)
mbgGPSNavSolved.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgGPSNavSolved.setStatus("current")
_MbgLeapSecond_Type = DisplayString
_MbgLeapSecond_Object = MibTableColumn
mbgLeapSecond = _MbgLeapSecond_Object(
    (1, 3, 6, 1, 4, 1, 5597, 80, 0, 0, 1, 1, 11),
    _MbgLeapSecond_Type()
)
mbgLeapSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgLeapSecond.setStatus("current")
_MbgSCU_ObjectIdentity = ObjectIdentity
mbgSCU = _MbgSCU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5597, 80, 1)
)
_MbgSCUType_Type = MeinbergRefClockTyp
_MbgSCUType_Object = MibScalar
mbgSCUType = _MbgSCUType_Object(
    (1, 3, 6, 1, 4, 1, 5597, 80, 1, 1),
    _MbgSCUType_Type()
)
mbgSCUType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgSCUType.setStatus("current")
_MbgSCUSerialNo_Type = DisplayString
_MbgSCUSerialNo_Object = MibScalar
mbgSCUSerialNo = _MbgSCUSerialNo_Object(
    (1, 3, 6, 1, 4, 1, 5597, 80, 1, 2),
    _MbgSCUSerialNo_Type()
)
mbgSCUSerialNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgSCUSerialNo.setStatus("current")
_MbgSCUFirmwareRev_Type = DisplayString
_MbgSCUFirmwareRev_Object = MibScalar
mbgSCUFirmwareRev = _MbgSCUFirmwareRev_Object(
    (1, 3, 6, 1, 4, 1, 5597, 80, 1, 3),
    _MbgSCUFirmwareRev_Type()
)
mbgSCUFirmwareRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgSCUFirmwareRev.setStatus("current")


class _MbgSCUMasterVal_Type(Integer32):
    """Custom type mbgSCUMasterVal based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noMaster", 0),
          ("clk1isMaster", 1),
          ("clk2isMaster", 2))
    )


_MbgSCUMasterVal_Type.__name__ = "Integer32"
_MbgSCUMasterVal_Object = MibScalar
mbgSCUMasterVal = _MbgSCUMasterVal_Object(
    (1, 3, 6, 1, 4, 1, 5597, 80, 1, 4),
    _MbgSCUMasterVal_Type()
)
mbgSCUMasterVal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgSCUMasterVal.setStatus("current")


class _MbgSCULocalRemote_Type(Integer32):
    """Custom type mbgSCULocalRemote based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("local", 0),
          ("remote", 1))
    )


_MbgSCULocalRemote_Type.__name__ = "Integer32"
_MbgSCULocalRemote_Object = MibScalar
mbgSCULocalRemote = _MbgSCULocalRemote_Object(
    (1, 3, 6, 1, 4, 1, 5597, 80, 1, 5),
    _MbgSCULocalRemote_Type()
)
mbgSCULocalRemote.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgSCULocalRemote.setStatus("current")
_MbgTrapIPAddress_Type = IpAddress
_MbgTrapIPAddress_Object = MibScalar
mbgTrapIPAddress = _MbgTrapIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 5597, 80, 1, 6),
    _MbgTrapIPAddress_Type()
)
mbgTrapIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgTrapIPAddress.setStatus("current")


class _MbgSCUSyncStatusClk1_Type(Integer32):
    """Custom type mbgSCUSyncStatusClk1 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("notSync", 0),
          ("sync", 1))
    )


_MbgSCUSyncStatusClk1_Type.__name__ = "Integer32"
_MbgSCUSyncStatusClk1_Object = MibScalar
mbgSCUSyncStatusClk1 = _MbgSCUSyncStatusClk1_Object(
    (1, 3, 6, 1, 4, 1, 5597, 80, 1, 7),
    _MbgSCUSyncStatusClk1_Type()
)
mbgSCUSyncStatusClk1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgSCUSyncStatusClk1.setStatus("current")


class _MbgSCUSyncStatusClk2_Type(Integer32):
    """Custom type mbgSCUSyncStatusClk2 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("notSync", 0),
          ("sync", 1))
    )


_MbgSCUSyncStatusClk2_Type.__name__ = "Integer32"
_MbgSCUSyncStatusClk2_Object = MibScalar
mbgSCUSyncStatusClk2 = _MbgSCUSyncStatusClk2_Object(
    (1, 3, 6, 1, 4, 1, 5597, 80, 1, 8),
    _MbgSCUSyncStatusClk2_Type()
)
mbgSCUSyncStatusClk2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgSCUSyncStatusClk2.setStatus("current")


class _MbgSCUOutputStatus_Type(Integer32):
    """Custom type mbgSCUOutputStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("outputsDisabled", 0),
          ("outputsEnabled", 1))
    )


_MbgSCUOutputStatus_Type.__name__ = "Integer32"
_MbgSCUOutputStatus_Object = MibScalar
mbgSCUOutputStatus = _MbgSCUOutputStatus_Object(
    (1, 3, 6, 1, 4, 1, 5597, 80, 1, 9),
    _MbgSCUOutputStatus_Type()
)
mbgSCUOutputStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgSCUOutputStatus.setStatus("current")


class _MbgSCUACOMode_Type(Integer32):
    """Custom type mbgSCUACOMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("acoModeOFF", 0),
          ("acoModeON", 1))
    )


_MbgSCUACOMode_Type.__name__ = "Integer32"
_MbgSCUACOMode_Object = MibScalar
mbgSCUACOMode = _MbgSCUACOMode_Object(
    (1, 3, 6, 1, 4, 1, 5597, 80, 1, 10),
    _MbgSCUACOMode_Type()
)
mbgSCUACOMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgSCUACOMode.setStatus("current")


class _MbgSCUPowerSupply1_Type(Integer32):
    """Custom type mbgSCUPowerSupply1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("notOK", 0),
          ("ok", 1))
    )


_MbgSCUPowerSupply1_Type.__name__ = "Integer32"
_MbgSCUPowerSupply1_Object = MibScalar
mbgSCUPowerSupply1 = _MbgSCUPowerSupply1_Object(
    (1, 3, 6, 1, 4, 1, 5597, 80, 1, 11),
    _MbgSCUPowerSupply1_Type()
)
mbgSCUPowerSupply1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgSCUPowerSupply1.setStatus("current")


class _MbgSCUPowerSupply2_Type(Integer32):
    """Custom type mbgSCUPowerSupply2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("notOK", 0),
          ("ok", 1))
    )


_MbgSCUPowerSupply2_Type.__name__ = "Integer32"
_MbgSCUPowerSupply2_Object = MibScalar
mbgSCUPowerSupply2 = _MbgSCUPowerSupply2_Object(
    (1, 3, 6, 1, 4, 1, 5597, 80, 1, 12),
    _MbgSCUPowerSupply2_Type()
)
mbgSCUPowerSupply2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgSCUPowerSupply2.setStatus("current")
_MbgSCUTemp_Type = DisplayString
_MbgSCUTemp_Object = MibScalar
mbgSCUTemp = _MbgSCUTemp_Object(
    (1, 3, 6, 1, 4, 1, 5597, 80, 1, 13),
    _MbgSCUTemp_Type()
)
mbgSCUTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgSCUTemp.setStatus("current")
_MbgSCUOutp1_Type = DisplayString
_MbgSCUOutp1_Object = MibScalar
mbgSCUOutp1 = _MbgSCUOutp1_Object(
    (1, 3, 6, 1, 4, 1, 5597, 80, 1, 14),
    _MbgSCUOutp1_Type()
)
mbgSCUOutp1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgSCUOutp1.setStatus("current")
_MbgSCUOutp2_Type = DisplayString
_MbgSCUOutp2_Object = MibScalar
mbgSCUOutp2 = _MbgSCUOutp2_Object(
    (1, 3, 6, 1, 4, 1, 5597, 80, 1, 15),
    _MbgSCUOutp2_Type()
)
mbgSCUOutp2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgSCUOutp2.setStatus("current")
_MbgSCUOutp3_Type = DisplayString
_MbgSCUOutp3_Object = MibScalar
mbgSCUOutp3 = _MbgSCUOutp3_Object(
    (1, 3, 6, 1, 4, 1, 5597, 80, 1, 16),
    _MbgSCUOutp3_Type()
)
mbgSCUOutp3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgSCUOutp3.setStatus("current")
_MbgSCUOutp4_Type = DisplayString
_MbgSCUOutp4_Object = MibScalar
mbgSCUOutp4 = _MbgSCUOutp4_Object(
    (1, 3, 6, 1, 4, 1, 5597, 80, 1, 17),
    _MbgSCUOutp4_Type()
)
mbgSCUOutp4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgSCUOutp4.setStatus("current")
_MbgSCUOutp5_Type = DisplayString
_MbgSCUOutp5_Object = MibScalar
mbgSCUOutp5 = _MbgSCUOutp5_Object(
    (1, 3, 6, 1, 4, 1, 5597, 80, 1, 18),
    _MbgSCUOutp5_Type()
)
mbgSCUOutp5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgSCUOutp5.setStatus("current")
_MbgSCUOutp6_Type = DisplayString
_MbgSCUOutp6_Object = MibScalar
mbgSCUOutp6 = _MbgSCUOutp6_Object(
    (1, 3, 6, 1, 4, 1, 5597, 80, 1, 19),
    _MbgSCUOutp6_Type()
)
mbgSCUOutp6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgSCUOutp6.setStatus("current")
_MbgSCUOutp7_Type = DisplayString
_MbgSCUOutp7_Object = MibScalar
mbgSCUOutp7 = _MbgSCUOutp7_Object(
    (1, 3, 6, 1, 4, 1, 5597, 80, 1, 20),
    _MbgSCUOutp7_Type()
)
mbgSCUOutp7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgSCUOutp7.setStatus("current")
_MbgSCUOutp8_Type = DisplayString
_MbgSCUOutp8_Object = MibScalar
mbgSCUOutp8 = _MbgSCUOutp8_Object(
    (1, 3, 6, 1, 4, 1, 5597, 80, 1, 21),
    _MbgSCUOutp8_Type()
)
mbgSCUOutp8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgSCUOutp8.setStatus("current")
_MbgSCUOutp9_Type = DisplayString
_MbgSCUOutp9_Object = MibScalar
mbgSCUOutp9 = _MbgSCUOutp9_Object(
    (1, 3, 6, 1, 4, 1, 5597, 80, 1, 22),
    _MbgSCUOutp9_Type()
)
mbgSCUOutp9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgSCUOutp9.setStatus("current")
_MbgSCUOutp10_Type = DisplayString
_MbgSCUOutp10_Object = MibScalar
mbgSCUOutp10 = _MbgSCUOutp10_Object(
    (1, 3, 6, 1, 4, 1, 5597, 80, 1, 23),
    _MbgSCUOutp10_Type()
)
mbgSCUOutp10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgSCUOutp10.setStatus("current")
_MbgSCUOutp11_Type = DisplayString
_MbgSCUOutp11_Object = MibScalar
mbgSCUOutp11 = _MbgSCUOutp11_Object(
    (1, 3, 6, 1, 4, 1, 5597, 80, 1, 24),
    _MbgSCUOutp11_Type()
)
mbgSCUOutp11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgSCUOutp11.setStatus("current")
_MbgSCUOutp12_Type = DisplayString
_MbgSCUOutp12_Object = MibScalar
mbgSCUOutp12 = _MbgSCUOutp12_Object(
    (1, 3, 6, 1, 4, 1, 5597, 80, 1, 25),
    _MbgSCUOutp12_Type()
)
mbgSCUOutp12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgSCUOutp12.setStatus("current")
_MbgSCUOutp13_Type = DisplayString
_MbgSCUOutp13_Object = MibScalar
mbgSCUOutp13 = _MbgSCUOutp13_Object(
    (1, 3, 6, 1, 4, 1, 5597, 80, 1, 26),
    _MbgSCUOutp13_Type()
)
mbgSCUOutp13.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgSCUOutp13.setStatus("current")
_MbgSCUOutp14_Type = DisplayString
_MbgSCUOutp14_Object = MibScalar
mbgSCUOutp14 = _MbgSCUOutp14_Object(
    (1, 3, 6, 1, 4, 1, 5597, 80, 1, 27),
    _MbgSCUOutp14_Type()
)
mbgSCUOutp14.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgSCUOutp14.setStatus("current")
_MbgSCUOutp15_Type = DisplayString
_MbgSCUOutp15_Object = MibScalar
mbgSCUOutp15 = _MbgSCUOutp15_Object(
    (1, 3, 6, 1, 4, 1, 5597, 80, 1, 28),
    _MbgSCUOutp15_Type()
)
mbgSCUOutp15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgSCUOutp15.setStatus("current")
_MbgSCUOutp16_Type = DisplayString
_MbgSCUOutp16_Object = MibScalar
mbgSCUOutp16 = _MbgSCUOutp16_Object(
    (1, 3, 6, 1, 4, 1, 5597, 80, 1, 29),
    _MbgSCUOutp16_Type()
)
mbgSCUOutp16.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgSCUOutp16.setStatus("current")
_MbgSCUInp1_Type = DisplayString
_MbgSCUInp1_Object = MibScalar
mbgSCUInp1 = _MbgSCUInp1_Object(
    (1, 3, 6, 1, 4, 1, 5597, 80, 1, 30),
    _MbgSCUInp1_Type()
)
mbgSCUInp1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgSCUInp1.setStatus("current")
_MbgSCUInp2_Type = DisplayString
_MbgSCUInp2_Object = MibScalar
mbgSCUInp2 = _MbgSCUInp2_Object(
    (1, 3, 6, 1, 4, 1, 5597, 80, 1, 31),
    _MbgSCUInp2_Type()
)
mbgSCUInp2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgSCUInp2.setStatus("current")
_MbgSCUSupl1_Type = DisplayString
_MbgSCUSupl1_Object = MibScalar
mbgSCUSupl1 = _MbgSCUSupl1_Object(
    (1, 3, 6, 1, 4, 1, 5597, 80, 1, 32),
    _MbgSCUSupl1_Type()
)
mbgSCUSupl1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgSCUSupl1.setStatus("current")
_MbgSCUSupl2_Type = DisplayString
_MbgSCUSupl2_Object = MibScalar
mbgSCUSupl2 = _MbgSCUSupl2_Object(
    (1, 3, 6, 1, 4, 1, 5597, 80, 1, 33),
    _MbgSCUSupl2_Type()
)
mbgSCUSupl2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgSCUSupl2.setStatus("current")
_MbgSCUSupl3_Type = DisplayString
_MbgSCUSupl3_Object = MibScalar
mbgSCUSupl3 = _MbgSCUSupl3_Object(
    (1, 3, 6, 1, 4, 1, 5597, 80, 1, 34),
    _MbgSCUSupl3_Type()
)
mbgSCUSupl3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgSCUSupl3.setStatus("current")
_MbgSCUSupl4_Type = DisplayString
_MbgSCUSupl4_Object = MibScalar
mbgSCUSupl4 = _MbgSCUSupl4_Object(
    (1, 3, 6, 1, 4, 1, 5597, 80, 1, 35),
    _MbgSCUSupl4_Type()
)
mbgSCUSupl4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgSCUSupl4.setStatus("current")
_MbgSCUtimeDiff_Type = DisplayString
_MbgSCUtimeDiff_Object = MibScalar
mbgSCUtimeDiff = _MbgSCUtimeDiff_Object(
    (1, 3, 6, 1, 4, 1, 5597, 80, 1, 36),
    _MbgSCUtimeDiff_Type()
)
mbgSCUtimeDiff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgSCUtimeDiff.setStatus("current")


class _MbgSCUAutoManual_Type(Integer32):
    """Custom type mbgSCUAutoManual based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("manual", 0),
          ("auto", 1))
    )


_MbgSCUAutoManual_Type.__name__ = "Integer32"
_MbgSCUAutoManual_Object = MibScalar
mbgSCUAutoManual = _MbgSCUAutoManual_Object(
    (1, 3, 6, 1, 4, 1, 5597, 80, 1, 37),
    _MbgSCUAutoManual_Type()
)
mbgSCUAutoManual.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgSCUAutoManual.setStatus("current")
_MbgSCUDum1_Type = DisplayString
_MbgSCUDum1_Object = MibScalar
mbgSCUDum1 = _MbgSCUDum1_Object(
    (1, 3, 6, 1, 4, 1, 5597, 80, 1, 38),
    _MbgSCUDum1_Type()
)
mbgSCUDum1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgSCUDum1.setStatus("current")
_MbgTrapRoot_ObjectIdentity = ObjectIdentity
mbgTrapRoot = _MbgTrapRoot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5597, 80, 2)
)
_MbgTraps_ObjectIdentity = ObjectIdentity
mbgTraps = _MbgTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5597, 80, 2, 0)
)
_MbgRSC180Conformance_ObjectIdentity = ObjectIdentity
mbgRSC180Conformance = _MbgRSC180Conformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5597, 80, 90)
)
_MbgRSC180Compliances_ObjectIdentity = ObjectIdentity
mbgRSC180Compliances = _MbgRSC180Compliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5597, 80, 90, 1)
)
_MbgRSC180Groups_ObjectIdentity = ObjectIdentity
mbgRSC180Groups = _MbgRSC180Groups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5597, 80, 90, 2)
)

# Managed Objects groups

mbgRSC180ObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5597, 80, 90, 2, 1)
)
mbgRSC180ObjectsGroup.setObjects(
      *(("MBG-SNMP-RSC180-MIB", "mbgClkType"),
        ("MBG-SNMP-RSC180-MIB", "mbgClkSerialNo"),
        ("MBG-SNMP-RSC180-MIB", "mbgClkFirmwareRev"),
        ("MBG-SNMP-RSC180-MIB", "mbgClkMode"),
        ("MBG-SNMP-RSC180-MIB", "mbgGpsState"),
        ("MBG-SNMP-RSC180-MIB", "mbgGpsPosition"),
        ("MBG-SNMP-RSC180-MIB", "mbgGpsSatellitesGood"),
        ("MBG-SNMP-RSC180-MIB", "mbgGpsSatellitesInView"),
        ("MBG-SNMP-RSC180-MIB", "mbgGPSNavSolved"),
        ("MBG-SNMP-RSC180-MIB", "mbgLeapSecond"),
        ("MBG-SNMP-RSC180-MIB", "mbgSCUType"),
        ("MBG-SNMP-RSC180-MIB", "mbgSCUSerialNo"),
        ("MBG-SNMP-RSC180-MIB", "mbgSCUFirmwareRev"),
        ("MBG-SNMP-RSC180-MIB", "mbgSCUMasterVal"),
        ("MBG-SNMP-RSC180-MIB", "mbgSCULocalRemote"),
        ("MBG-SNMP-RSC180-MIB", "mbgTrapIPAddress"),
        ("MBG-SNMP-RSC180-MIB", "mbgSCUSyncStatusClk1"),
        ("MBG-SNMP-RSC180-MIB", "mbgSCUSyncStatusClk2"),
        ("MBG-SNMP-RSC180-MIB", "mbgSCUOutputStatus"),
        ("MBG-SNMP-RSC180-MIB", "mbgSCUACOMode"),
        ("MBG-SNMP-RSC180-MIB", "mbgSCUPowerSupply1"),
        ("MBG-SNMP-RSC180-MIB", "mbgSCUPowerSupply2"),
        ("MBG-SNMP-RSC180-MIB", "mbgSCUTemp"),
        ("MBG-SNMP-RSC180-MIB", "mbgSCUOutp1"),
        ("MBG-SNMP-RSC180-MIB", "mbgSCUOutp2"),
        ("MBG-SNMP-RSC180-MIB", "mbgSCUOutp3"),
        ("MBG-SNMP-RSC180-MIB", "mbgSCUOutp4"),
        ("MBG-SNMP-RSC180-MIB", "mbgSCUOutp5"),
        ("MBG-SNMP-RSC180-MIB", "mbgSCUOutp6"),
        ("MBG-SNMP-RSC180-MIB", "mbgSCUOutp7"),
        ("MBG-SNMP-RSC180-MIB", "mbgSCUOutp8"),
        ("MBG-SNMP-RSC180-MIB", "mbgSCUOutp9"),
        ("MBG-SNMP-RSC180-MIB", "mbgSCUOutp10"),
        ("MBG-SNMP-RSC180-MIB", "mbgSCUOutp11"),
        ("MBG-SNMP-RSC180-MIB", "mbgSCUOutp12"),
        ("MBG-SNMP-RSC180-MIB", "mbgSCUOutp13"),
        ("MBG-SNMP-RSC180-MIB", "mbgSCUOutp14"),
        ("MBG-SNMP-RSC180-MIB", "mbgSCUOutp15"),
        ("MBG-SNMP-RSC180-MIB", "mbgSCUOutp16"),
        ("MBG-SNMP-RSC180-MIB", "mbgSCUInp1"),
        ("MBG-SNMP-RSC180-MIB", "mbgSCUInp2"),
        ("MBG-SNMP-RSC180-MIB", "mbgSCUSupl1"),
        ("MBG-SNMP-RSC180-MIB", "mbgSCUSupl2"),
        ("MBG-SNMP-RSC180-MIB", "mbgSCUSupl3"),
        ("MBG-SNMP-RSC180-MIB", "mbgSCUSupl4"),
        ("MBG-SNMP-RSC180-MIB", "mbgSCUtimeDiff"),
        ("MBG-SNMP-RSC180-MIB", "mbgSCUAutoManual"),
        ("MBG-SNMP-RSC180-MIB", "mbgSCUDum1"))
)
if mibBuilder.loadTexts:
    mbgRSC180ObjectsGroup.setStatus("current")


# Notification objects

mbgColdBootTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5597, 80, 2, 0, 1)
)
if mibBuilder.loadTexts:
    mbgColdBootTrap.setStatus(
        "current"
    )

mbgWarmBootTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5597, 80, 2, 0, 2)
)
if mibBuilder.loadTexts:
    mbgWarmBootTrap.setStatus(
        "current"
    )

mbgGPSNavSolvedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5597, 80, 2, 0, 3)
)
if mibBuilder.loadTexts:
    mbgGPSNavSolvedTrap.setStatus(
        "current"
    )

mbgGPSReceiverNotRespondingTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5597, 80, 2, 0, 4)
)
if mibBuilder.loadTexts:
    mbgGPSReceiverNotRespondingTrap.setStatus(
        "current"
    )

mbgGPSReceiverNotSyncTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5597, 80, 2, 0, 5)
)
if mibBuilder.loadTexts:
    mbgGPSReceiverNotSyncTrap.setStatus(
        "current"
    )

mbgGPSAntennaFaultyTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5597, 80, 2, 0, 6)
)
if mibBuilder.loadTexts:
    mbgGPSAntennaFaultyTrap.setStatus(
        "current"
    )

mbgGPSAntennaReconnectTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5597, 80, 2, 0, 7)
)
if mibBuilder.loadTexts:
    mbgGPSAntennaReconnectTrap.setStatus(
        "current"
    )

mbgSCUBootTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5597, 80, 2, 0, 8)
)
if mibBuilder.loadTexts:
    mbgSCUBootTrap.setStatus(
        "current"
    )

mbgLeapSecondAnnouncedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5597, 80, 2, 0, 9)
)
if mibBuilder.loadTexts:
    mbgLeapSecondAnnouncedTrap.setStatus(
        "current"
    )

mbgMasterclockSwitchoverTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5597, 80, 2, 0, 10)
)
if mibBuilder.loadTexts:
    mbgMasterclockSwitchoverTrap.setStatus(
        "current"
    )

mbgPowerSupplyFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5597, 80, 2, 0, 11)
)
if mibBuilder.loadTexts:
    mbgPowerSupplyFailureTrap.setStatus(
        "current"
    )

mbgPowerSupplyOKTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5597, 80, 2, 0, 12)
)
if mibBuilder.loadTexts:
    mbgPowerSupplyOKTrap.setStatus(
        "current"
    )

mbgHighTempTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5597, 80, 2, 0, 13)
)
if mibBuilder.loadTexts:
    mbgHighTempTrap.setStatus(
        "current"
    )

mbgTestNotificationTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5597, 80, 2, 0, 99)
)
if mibBuilder.loadTexts:
    mbgTestNotificationTrap.setStatus(
        "current"
    )


# Notifications groups

mbgRSC180TrapsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 5597, 80, 90, 2, 2)
)
mbgRSC180TrapsGroup.setObjects(
      *(("MBG-SNMP-RSC180-MIB", "mbgColdBootTrap"),
        ("MBG-SNMP-RSC180-MIB", "mbgWarmBootTrap"),
        ("MBG-SNMP-RSC180-MIB", "mbgGPSNavSolvedTrap"),
        ("MBG-SNMP-RSC180-MIB", "mbgGPSReceiverNotRespondingTrap"),
        ("MBG-SNMP-RSC180-MIB", "mbgGPSReceiverNotSyncTrap"),
        ("MBG-SNMP-RSC180-MIB", "mbgGPSAntennaFaultyTrap"),
        ("MBG-SNMP-RSC180-MIB", "mbgGPSAntennaReconnectTrap"),
        ("MBG-SNMP-RSC180-MIB", "mbgSCUBootTrap"),
        ("MBG-SNMP-RSC180-MIB", "mbgLeapSecondAnnouncedTrap"),
        ("MBG-SNMP-RSC180-MIB", "mbgMasterclockSwitchoverTrap"),
        ("MBG-SNMP-RSC180-MIB", "mbgPowerSupplyFailureTrap"),
        ("MBG-SNMP-RSC180-MIB", "mbgPowerSupplyOKTrap"),
        ("MBG-SNMP-RSC180-MIB", "mbgHighTempTrap"),
        ("MBG-SNMP-RSC180-MIB", "mbgTestNotificationTrap"))
)
if mibBuilder.loadTexts:
    mbgRSC180TrapsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

mbgRSC180Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5597, 80, 90, 1, 1)
)
mbgRSC180Compliance.setObjects(
      *(("MBG-SNMP-RSC180-MIB", "mbgRSC180ObjectsGroup"),
        ("MBG-SNMP-RSC180-MIB", "mbgRSC180TrapsGroup"))
)
if mibBuilder.loadTexts:
    mbgRSC180Compliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MBG-SNMP-RSC180-MIB",
    **{"MeinbergRefClockTyp": MeinbergRefClockTyp,
       "mbgRSC180": mbgRSC180,
       "mbgRefClock": mbgRefClock,
       "mbgRefClockStatus": mbgRefClockStatus,
       "mbgRefClockTable": mbgRefClockTable,
       "mbgRefClockTableEntry": mbgRefClockTableEntry,
       "mbgClkTableIndex": mbgClkTableIndex,
       "mbgClkType": mbgClkType,
       "mbgClkSerialNo": mbgClkSerialNo,
       "mbgClkFirmwareRev": mbgClkFirmwareRev,
       "mbgClkMode": mbgClkMode,
       "mbgGpsState": mbgGpsState,
       "mbgGpsPosition": mbgGpsPosition,
       "mbgGpsSatellitesGood": mbgGpsSatellitesGood,
       "mbgGpsSatellitesInView": mbgGpsSatellitesInView,
       "mbgGPSNavSolved": mbgGPSNavSolved,
       "mbgLeapSecond": mbgLeapSecond,
       "mbgSCU": mbgSCU,
       "mbgSCUType": mbgSCUType,
       "mbgSCUSerialNo": mbgSCUSerialNo,
       "mbgSCUFirmwareRev": mbgSCUFirmwareRev,
       "mbgSCUMasterVal": mbgSCUMasterVal,
       "mbgSCULocalRemote": mbgSCULocalRemote,
       "mbgTrapIPAddress": mbgTrapIPAddress,
       "mbgSCUSyncStatusClk1": mbgSCUSyncStatusClk1,
       "mbgSCUSyncStatusClk2": mbgSCUSyncStatusClk2,
       "mbgSCUOutputStatus": mbgSCUOutputStatus,
       "mbgSCUACOMode": mbgSCUACOMode,
       "mbgSCUPowerSupply1": mbgSCUPowerSupply1,
       "mbgSCUPowerSupply2": mbgSCUPowerSupply2,
       "mbgSCUTemp": mbgSCUTemp,
       "mbgSCUOutp1": mbgSCUOutp1,
       "mbgSCUOutp2": mbgSCUOutp2,
       "mbgSCUOutp3": mbgSCUOutp3,
       "mbgSCUOutp4": mbgSCUOutp4,
       "mbgSCUOutp5": mbgSCUOutp5,
       "mbgSCUOutp6": mbgSCUOutp6,
       "mbgSCUOutp7": mbgSCUOutp7,
       "mbgSCUOutp8": mbgSCUOutp8,
       "mbgSCUOutp9": mbgSCUOutp9,
       "mbgSCUOutp10": mbgSCUOutp10,
       "mbgSCUOutp11": mbgSCUOutp11,
       "mbgSCUOutp12": mbgSCUOutp12,
       "mbgSCUOutp13": mbgSCUOutp13,
       "mbgSCUOutp14": mbgSCUOutp14,
       "mbgSCUOutp15": mbgSCUOutp15,
       "mbgSCUOutp16": mbgSCUOutp16,
       "mbgSCUInp1": mbgSCUInp1,
       "mbgSCUInp2": mbgSCUInp2,
       "mbgSCUSupl1": mbgSCUSupl1,
       "mbgSCUSupl2": mbgSCUSupl2,
       "mbgSCUSupl3": mbgSCUSupl3,
       "mbgSCUSupl4": mbgSCUSupl4,
       "mbgSCUtimeDiff": mbgSCUtimeDiff,
       "mbgSCUAutoManual": mbgSCUAutoManual,
       "mbgSCUDum1": mbgSCUDum1,
       "mbgTrapRoot": mbgTrapRoot,
       "mbgTraps": mbgTraps,
       "mbgColdBootTrap": mbgColdBootTrap,
       "mbgWarmBootTrap": mbgWarmBootTrap,
       "mbgGPSNavSolvedTrap": mbgGPSNavSolvedTrap,
       "mbgGPSReceiverNotRespondingTrap": mbgGPSReceiverNotRespondingTrap,
       "mbgGPSReceiverNotSyncTrap": mbgGPSReceiverNotSyncTrap,
       "mbgGPSAntennaFaultyTrap": mbgGPSAntennaFaultyTrap,
       "mbgGPSAntennaReconnectTrap": mbgGPSAntennaReconnectTrap,
       "mbgSCUBootTrap": mbgSCUBootTrap,
       "mbgLeapSecondAnnouncedTrap": mbgLeapSecondAnnouncedTrap,
       "mbgMasterclockSwitchoverTrap": mbgMasterclockSwitchoverTrap,
       "mbgPowerSupplyFailureTrap": mbgPowerSupplyFailureTrap,
       "mbgPowerSupplyOKTrap": mbgPowerSupplyOKTrap,
       "mbgHighTempTrap": mbgHighTempTrap,
       "mbgTestNotificationTrap": mbgTestNotificationTrap,
       "mbgRSC180Conformance": mbgRSC180Conformance,
       "mbgRSC180Compliances": mbgRSC180Compliances,
       "mbgRSC180Compliance": mbgRSC180Compliance,
       "mbgRSC180Groups": mbgRSC180Groups,
       "mbgRSC180ObjectsGroup": mbgRSC180ObjectsGroup,
       "mbgRSC180TrapsGroup": mbgRSC180TrapsGroup}
)
