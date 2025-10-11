# SNMP MIB module (MBG-SNMP-RSC-MDU-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/meinberg/MBG-SNMP-RSC-MDU-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:07:08 2025
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
        ("2017-03-28 00:00",
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
              52,
              53,
              54,
              55,
              56,
              57,
              58,
              59,
              60,
              61,
              62,
              63,
              64,
              65,
              66,
              67,
              68,
              69,
              70,
              71,
              72,
              73,
              74,
              75,
              76,
              77,
              78,
              79,
              80,
              81,
              82,
              83,
              84,
              85,
              86,
              87)
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
          ("rsc180", 52),
          ("lne_gb", 53),
          ("Ppg180", 54),
          ("scg", 55),
          ("mdu300", 56),
          ("sdi", 57),
          ("fdm180", 58),
          ("spt", 59),
          ("pzf180", 60),
          ("rel1000", 61),
          ("hps100", 62),
          ("vsg180", 63),
          ("msf180", 64),
          ("wwvb180", 65),
          ("cpc180", 66),
          ("ctc100", 67),
          ("tcr180", 68),
          ("lue180", 69),
          ("cpc_01", 70),
          ("tsu_01", 71),
          ("cmc_01", 72),
          ("scu_01", 73),
          ("fcu_01", 74),
          ("csm100", 75),
          ("lne180sfp", 76),
          ("gts180", 77),
          ("gps180csm", 78),
          ("grc181", 79),
          ("n2x180", 80),
          ("grc181PEX", 81),
          ("mdu180", 82),
          ("mdu312", 83),
          ("gps165", 84),
          ("gns181_uc", 85),
          ("psx_4ge", 86),
          ("rsc180rdu", 87))
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
    (0, "MBG-SNMP-RSC-MDU-MIB", "mbgClkTableIndex"),
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
    (1, 3, 6, 1, 4, 1, 5597, 80, 0, 0, 1, 1, 5),
    _MbgGpsState_Type()
)
mbgGpsState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgGpsState.setStatus("current")
_MbgMDU_ObjectIdentity = ObjectIdentity
mbgMDU = _MbgMDU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5597, 80, 1)
)
_MbgMDUType_Type = MeinbergRefClockTyp
_MbgMDUType_Object = MibScalar
mbgMDUType = _MbgMDUType_Object(
    (1, 3, 6, 1, 4, 1, 5597, 80, 1, 1),
    _MbgMDUType_Type()
)
mbgMDUType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgMDUType.setStatus("current")
_MbgMDUSerialNo_Type = DisplayString
_MbgMDUSerialNo_Object = MibScalar
mbgMDUSerialNo = _MbgMDUSerialNo_Object(
    (1, 3, 6, 1, 4, 1, 5597, 80, 1, 2),
    _MbgMDUSerialNo_Type()
)
mbgMDUSerialNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgMDUSerialNo.setStatus("current")
_MbgMDUFirmwareRev_Type = DisplayString
_MbgMDUFirmwareRev_Object = MibScalar
mbgMDUFirmwareRev = _MbgMDUFirmwareRev_Object(
    (1, 3, 6, 1, 4, 1, 5597, 80, 1, 3),
    _MbgMDUFirmwareRev_Type()
)
mbgMDUFirmwareRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgMDUFirmwareRev.setStatus("current")


class _MbgMDUMasterVal_Type(Integer32):
    """Custom type mbgMDUMasterVal based on Integer32"""
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


_MbgMDUMasterVal_Type.__name__ = "Integer32"
_MbgMDUMasterVal_Object = MibScalar
mbgMDUMasterVal = _MbgMDUMasterVal_Object(
    (1, 3, 6, 1, 4, 1, 5597, 80, 1, 4),
    _MbgMDUMasterVal_Type()
)
mbgMDUMasterVal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgMDUMasterVal.setStatus("current")


class _MbgMDULocalRemote_Type(Integer32):
    """Custom type mbgMDULocalRemote based on Integer32"""
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


_MbgMDULocalRemote_Type.__name__ = "Integer32"
_MbgMDULocalRemote_Object = MibScalar
mbgMDULocalRemote = _MbgMDULocalRemote_Object(
    (1, 3, 6, 1, 4, 1, 5597, 80, 1, 5),
    _MbgMDULocalRemote_Type()
)
mbgMDULocalRemote.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgMDULocalRemote.setStatus("current")
_MbgTrapIPAddress_Type = IpAddress
_MbgTrapIPAddress_Object = MibScalar
mbgTrapIPAddress = _MbgTrapIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 5597, 80, 1, 6),
    _MbgTrapIPAddress_Type()
)
mbgTrapIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mbgTrapIPAddress.setStatus("current")


class _MbgMDUSyncStatusClk1_Type(Integer32):
    """Custom type mbgMDUSyncStatusClk1 based on Integer32"""
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


_MbgMDUSyncStatusClk1_Type.__name__ = "Integer32"
_MbgMDUSyncStatusClk1_Object = MibScalar
mbgMDUSyncStatusClk1 = _MbgMDUSyncStatusClk1_Object(
    (1, 3, 6, 1, 4, 1, 5597, 80, 1, 7),
    _MbgMDUSyncStatusClk1_Type()
)
mbgMDUSyncStatusClk1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgMDUSyncStatusClk1.setStatus("current")


class _MbgMDUSyncStatusClk2_Type(Integer32):
    """Custom type mbgMDUSyncStatusClk2 based on Integer32"""
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


_MbgMDUSyncStatusClk2_Type.__name__ = "Integer32"
_MbgMDUSyncStatusClk2_Object = MibScalar
mbgMDUSyncStatusClk2 = _MbgMDUSyncStatusClk2_Object(
    (1, 3, 6, 1, 4, 1, 5597, 80, 1, 8),
    _MbgMDUSyncStatusClk2_Type()
)
mbgMDUSyncStatusClk2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgMDUSyncStatusClk2.setStatus("current")


class _MbgMDUOutputStatus_Type(Integer32):
    """Custom type mbgMDUOutputStatus based on Integer32"""
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


_MbgMDUOutputStatus_Type.__name__ = "Integer32"
_MbgMDUOutputStatus_Object = MibScalar
mbgMDUOutputStatus = _MbgMDUOutputStatus_Object(
    (1, 3, 6, 1, 4, 1, 5597, 80, 1, 9),
    _MbgMDUOutputStatus_Type()
)
mbgMDUOutputStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgMDUOutputStatus.setStatus("current")


class _MbgMDUACOMode_Type(Integer32):
    """Custom type mbgMDUACOMode based on Integer32"""
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


_MbgMDUACOMode_Type.__name__ = "Integer32"
_MbgMDUACOMode_Object = MibScalar
mbgMDUACOMode = _MbgMDUACOMode_Object(
    (1, 3, 6, 1, 4, 1, 5597, 80, 1, 10),
    _MbgMDUACOMode_Type()
)
mbgMDUACOMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgMDUACOMode.setStatus("current")


class _MbgMDUPowerSupply1_Type(Integer32):
    """Custom type mbgMDUPowerSupply1 based on Integer32"""
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


_MbgMDUPowerSupply1_Type.__name__ = "Integer32"
_MbgMDUPowerSupply1_Object = MibScalar
mbgMDUPowerSupply1 = _MbgMDUPowerSupply1_Object(
    (1, 3, 6, 1, 4, 1, 5597, 80, 1, 11),
    _MbgMDUPowerSupply1_Type()
)
mbgMDUPowerSupply1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgMDUPowerSupply1.setStatus("current")


class _MbgMDUPowerSupply2_Type(Integer32):
    """Custom type mbgMDUPowerSupply2 based on Integer32"""
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


_MbgMDUPowerSupply2_Type.__name__ = "Integer32"
_MbgMDUPowerSupply2_Object = MibScalar
mbgMDUPowerSupply2 = _MbgMDUPowerSupply2_Object(
    (1, 3, 6, 1, 4, 1, 5597, 80, 1, 12),
    _MbgMDUPowerSupply2_Type()
)
mbgMDUPowerSupply2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgMDUPowerSupply2.setStatus("current")


class _MbgMDUPowerSupply3_Type(Integer32):
    """Custom type mbgMDUPowerSupply3 based on Integer32"""
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


_MbgMDUPowerSupply3_Type.__name__ = "Integer32"
_MbgMDUPowerSupply3_Object = MibScalar
mbgMDUPowerSupply3 = _MbgMDUPowerSupply3_Object(
    (1, 3, 6, 1, 4, 1, 5597, 80, 1, 13),
    _MbgMDUPowerSupply3_Type()
)
mbgMDUPowerSupply3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgMDUPowerSupply3.setStatus("current")


class _MbgMDUPowerSupply4_Type(Integer32):
    """Custom type mbgMDUPowerSupply4 based on Integer32"""
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


_MbgMDUPowerSupply4_Type.__name__ = "Integer32"
_MbgMDUPowerSupply4_Object = MibScalar
mbgMDUPowerSupply4 = _MbgMDUPowerSupply4_Object(
    (1, 3, 6, 1, 4, 1, 5597, 80, 1, 14),
    _MbgMDUPowerSupply4_Type()
)
mbgMDUPowerSupply4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgMDUPowerSupply4.setStatus("current")
_MbgMDUTemp_Type = DisplayString
_MbgMDUTemp_Object = MibScalar
mbgMDUTemp = _MbgMDUTemp_Object(
    (1, 3, 6, 1, 4, 1, 5597, 80, 1, 15),
    _MbgMDUTemp_Type()
)
mbgMDUTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgMDUTemp.setStatus("current")
_MbgMDUSlot1_Type = DisplayString
_MbgMDUSlot1_Object = MibScalar
mbgMDUSlot1 = _MbgMDUSlot1_Object(
    (1, 3, 6, 1, 4, 1, 5597, 80, 1, 16),
    _MbgMDUSlot1_Type()
)
mbgMDUSlot1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgMDUSlot1.setStatus("current")
_MbgMDUSlot2_Type = DisplayString
_MbgMDUSlot2_Object = MibScalar
mbgMDUSlot2 = _MbgMDUSlot2_Object(
    (1, 3, 6, 1, 4, 1, 5597, 80, 1, 17),
    _MbgMDUSlot2_Type()
)
mbgMDUSlot2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgMDUSlot2.setStatus("current")
_MbgMDUSlot3_Type = DisplayString
_MbgMDUSlot3_Object = MibScalar
mbgMDUSlot3 = _MbgMDUSlot3_Object(
    (1, 3, 6, 1, 4, 1, 5597, 80, 1, 18),
    _MbgMDUSlot3_Type()
)
mbgMDUSlot3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgMDUSlot3.setStatus("current")
_MbgMDUSlot4_Type = DisplayString
_MbgMDUSlot4_Object = MibScalar
mbgMDUSlot4 = _MbgMDUSlot4_Object(
    (1, 3, 6, 1, 4, 1, 5597, 80, 1, 19),
    _MbgMDUSlot4_Type()
)
mbgMDUSlot4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgMDUSlot4.setStatus("current")
_MbgMDUSlot5_Type = DisplayString
_MbgMDUSlot5_Object = MibScalar
mbgMDUSlot5 = _MbgMDUSlot5_Object(
    (1, 3, 6, 1, 4, 1, 5597, 80, 1, 20),
    _MbgMDUSlot5_Type()
)
mbgMDUSlot5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgMDUSlot5.setStatus("current")
_MbgMDUSlot6_Type = DisplayString
_MbgMDUSlot6_Object = MibScalar
mbgMDUSlot6 = _MbgMDUSlot6_Object(
    (1, 3, 6, 1, 4, 1, 5597, 80, 1, 21),
    _MbgMDUSlot6_Type()
)
mbgMDUSlot6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgMDUSlot6.setStatus("current")
_MbgMDUSlot7_Type = DisplayString
_MbgMDUSlot7_Object = MibScalar
mbgMDUSlot7 = _MbgMDUSlot7_Object(
    (1, 3, 6, 1, 4, 1, 5597, 80, 1, 22),
    _MbgMDUSlot7_Type()
)
mbgMDUSlot7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgMDUSlot7.setStatus("current")
_MbgMDUSlot8_Type = DisplayString
_MbgMDUSlot8_Object = MibScalar
mbgMDUSlot8 = _MbgMDUSlot8_Object(
    (1, 3, 6, 1, 4, 1, 5597, 80, 1, 23),
    _MbgMDUSlot8_Type()
)
mbgMDUSlot8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgMDUSlot8.setStatus("current")
_MbgMDUSlot9_Type = DisplayString
_MbgMDUSlot9_Object = MibScalar
mbgMDUSlot9 = _MbgMDUSlot9_Object(
    (1, 3, 6, 1, 4, 1, 5597, 80, 1, 24),
    _MbgMDUSlot9_Type()
)
mbgMDUSlot9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgMDUSlot9.setStatus("current")
_MbgMDUSlot10_Type = DisplayString
_MbgMDUSlot10_Object = MibScalar
mbgMDUSlot10 = _MbgMDUSlot10_Object(
    (1, 3, 6, 1, 4, 1, 5597, 80, 1, 25),
    _MbgMDUSlot10_Type()
)
mbgMDUSlot10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgMDUSlot10.setStatus("current")
_MbgMDUSlot11_Type = DisplayString
_MbgMDUSlot11_Object = MibScalar
mbgMDUSlot11 = _MbgMDUSlot11_Object(
    (1, 3, 6, 1, 4, 1, 5597, 80, 1, 26),
    _MbgMDUSlot11_Type()
)
mbgMDUSlot11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgMDUSlot11.setStatus("current")
_MbgMDUSlot12_Type = DisplayString
_MbgMDUSlot12_Object = MibScalar
mbgMDUSlot12 = _MbgMDUSlot12_Object(
    (1, 3, 6, 1, 4, 1, 5597, 80, 1, 27),
    _MbgMDUSlot12_Type()
)
mbgMDUSlot12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgMDUSlot12.setStatus("current")
_MbgMDUSlot13_Type = DisplayString
_MbgMDUSlot13_Object = MibScalar
mbgMDUSlot13 = _MbgMDUSlot13_Object(
    (1, 3, 6, 1, 4, 1, 5597, 80, 1, 28),
    _MbgMDUSlot13_Type()
)
mbgMDUSlot13.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgMDUSlot13.setStatus("current")
_MbgMDUSlot14_Type = DisplayString
_MbgMDUSlot14_Object = MibScalar
mbgMDUSlot14 = _MbgMDUSlot14_Object(
    (1, 3, 6, 1, 4, 1, 5597, 80, 1, 29),
    _MbgMDUSlot14_Type()
)
mbgMDUSlot14.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgMDUSlot14.setStatus("current")
_MbgMDUClk1_Type = DisplayString
_MbgMDUClk1_Object = MibScalar
mbgMDUClk1 = _MbgMDUClk1_Object(
    (1, 3, 6, 1, 4, 1, 5597, 80, 1, 30),
    _MbgMDUClk1_Type()
)
mbgMDUClk1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgMDUClk1.setStatus("current")
_MbgMDUClk2_Type = DisplayString
_MbgMDUClk2_Object = MibScalar
mbgMDUClk2 = _MbgMDUClk2_Object(
    (1, 3, 6, 1, 4, 1, 5597, 80, 1, 31),
    _MbgMDUClk2_Type()
)
mbgMDUClk2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgMDUClk2.setStatus("current")
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
      *(("MBG-SNMP-RSC-MDU-MIB", "mbgClkType"),
        ("MBG-SNMP-RSC-MDU-MIB", "mbgClkSerialNo"),
        ("MBG-SNMP-RSC-MDU-MIB", "mbgClkFirmwareRev"),
        ("MBG-SNMP-RSC-MDU-MIB", "mbgClkMode"),
        ("MBG-SNMP-RSC-MDU-MIB", "mbgGpsState"),
        ("MBG-SNMP-RSC-MDU-MIB", "mbgGpsPosition"),
        ("MBG-SNMP-RSC-MDU-MIB", "mbgGpsSatellitesGood"),
        ("MBG-SNMP-RSC-MDU-MIB", "mbgGpsSatellitesInView"),
        ("MBG-SNMP-RSC-MDU-MIB", "mbgGPSNavSolved"),
        ("MBG-SNMP-RSC-MDU-MIB", "mbgLeapSecond"),
        ("MBG-SNMP-RSC-MDU-MIB", "mbgSCUType"),
        ("MBG-SNMP-RSC-MDU-MIB", "mbgSCUSerialNo"),
        ("MBG-SNMP-RSC-MDU-MIB", "mbgSCUFirmwareRev"),
        ("MBG-SNMP-RSC-MDU-MIB", "mbgSCUMasterVal"),
        ("MBG-SNMP-RSC-MDU-MIB", "mbgSCULocalRemote"),
        ("MBG-SNMP-RSC-MDU-MIB", "mbgTrapIPAddress"),
        ("MBG-SNMP-RSC-MDU-MIB", "mbgSCUSyncStatusClk1"),
        ("MBG-SNMP-RSC-MDU-MIB", "mbgSCUSyncStatusClk2"),
        ("MBG-SNMP-RSC-MDU-MIB", "mbgSCUOutputStatus"),
        ("MBG-SNMP-RSC-MDU-MIB", "mbgSCUACOMode"),
        ("MBG-SNMP-RSC-MDU-MIB", "mbgSCUPowerSupply1"),
        ("MBG-SNMP-RSC-MDU-MIB", "mbgSCUPowerSupply2"),
        ("MBG-SNMP-RSC-MDU-MIB", "mbgSCUTemp"))
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
      *(("MBG-SNMP-RSC-MDU-MIB", "mbgColdBootTrap"),
        ("MBG-SNMP-RSC-MDU-MIB", "mbgWarmBootTrap"),
        ("MBG-SNMP-RSC-MDU-MIB", "mbgGPSNavSolvedTrap"),
        ("MBG-SNMP-RSC-MDU-MIB", "mbgGPSReceiverNotRespondingTrap"),
        ("MBG-SNMP-RSC-MDU-MIB", "mbgGPSReceiverNotSyncTrap"),
        ("MBG-SNMP-RSC-MDU-MIB", "mbgGPSAntennaFaultyTrap"),
        ("MBG-SNMP-RSC-MDU-MIB", "mbgGPSAntennaReconnectTrap"),
        ("MBG-SNMP-RSC-MDU-MIB", "mbgSCUBootTrap"),
        ("MBG-SNMP-RSC-MDU-MIB", "mbgLeapSecondAnnouncedTrap"),
        ("MBG-SNMP-RSC-MDU-MIB", "mbgMasterclockSwitchoverTrap"),
        ("MBG-SNMP-RSC-MDU-MIB", "mbgPowerSupplyFailureTrap"),
        ("MBG-SNMP-RSC-MDU-MIB", "mbgPowerSupplyOKTrap"),
        ("MBG-SNMP-RSC-MDU-MIB", "mbgHighTempTrap"),
        ("MBG-SNMP-RSC-MDU-MIB", "mbgTestNotificationTrap"))
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
      *(("MBG-SNMP-RSC-MDU-MIB", "mbgRSC180ObjectsGroup"),
        ("MBG-SNMP-RSC-MDU-MIB", "mbgRSC180TrapsGroup"))
)
if mibBuilder.loadTexts:
    mbgRSC180Compliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MBG-SNMP-RSC-MDU-MIB",
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
       "mbgGpsState": mbgGpsState,
       "mbgMDU": mbgMDU,
       "mbgMDUType": mbgMDUType,
       "mbgMDUSerialNo": mbgMDUSerialNo,
       "mbgMDUFirmwareRev": mbgMDUFirmwareRev,
       "mbgMDUMasterVal": mbgMDUMasterVal,
       "mbgMDULocalRemote": mbgMDULocalRemote,
       "mbgTrapIPAddress": mbgTrapIPAddress,
       "mbgMDUSyncStatusClk1": mbgMDUSyncStatusClk1,
       "mbgMDUSyncStatusClk2": mbgMDUSyncStatusClk2,
       "mbgMDUOutputStatus": mbgMDUOutputStatus,
       "mbgMDUACOMode": mbgMDUACOMode,
       "mbgMDUPowerSupply1": mbgMDUPowerSupply1,
       "mbgMDUPowerSupply2": mbgMDUPowerSupply2,
       "mbgMDUPowerSupply3": mbgMDUPowerSupply3,
       "mbgMDUPowerSupply4": mbgMDUPowerSupply4,
       "mbgMDUTemp": mbgMDUTemp,
       "mbgMDUSlot1": mbgMDUSlot1,
       "mbgMDUSlot2": mbgMDUSlot2,
       "mbgMDUSlot3": mbgMDUSlot3,
       "mbgMDUSlot4": mbgMDUSlot4,
       "mbgMDUSlot5": mbgMDUSlot5,
       "mbgMDUSlot6": mbgMDUSlot6,
       "mbgMDUSlot7": mbgMDUSlot7,
       "mbgMDUSlot8": mbgMDUSlot8,
       "mbgMDUSlot9": mbgMDUSlot9,
       "mbgMDUSlot10": mbgMDUSlot10,
       "mbgMDUSlot11": mbgMDUSlot11,
       "mbgMDUSlot12": mbgMDUSlot12,
       "mbgMDUSlot13": mbgMDUSlot13,
       "mbgMDUSlot14": mbgMDUSlot14,
       "mbgMDUClk1": mbgMDUClk1,
       "mbgMDUClk2": mbgMDUClk2,
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
