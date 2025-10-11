# SNMP MIB module (ARECA-SAS-CARD1-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/areca/ARECA-SAS-CARD1-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:35:33 2025
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
 NotificationType,
 TimeTicks,
 Unsigned32,
 enterprises,
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
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Areca_ObjectIdentity = ObjectIdentity
areca = _Areca_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18928)
)
_ArecaGroup1_ObjectIdentity = ObjectIdentity
arecaGroup1 = _ArecaGroup1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18928, 1)
)
_SasRaidCard1_ObjectIdentity = ObjectIdentity
sasRaidCard1 = _SasRaidCard1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129)
)
_SystemInformation_ObjectIdentity = ObjectIdentity
systemInformation = _SystemInformation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 1)
)
_SiVendor_Type = OctetString
_SiVendor_Object = MibScalar
siVendor = _SiVendor_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 1, 1),
    _SiVendor_Type()
)
siVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    siVendor.setStatus("mandatory")
_SiModel_Type = OctetString
_SiModel_Object = MibScalar
siModel = _SiModel_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 1, 2),
    _SiModel_Type()
)
siModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    siModel.setStatus("mandatory")
_SiSerial_Type = OctetString
_SiSerial_Object = MibScalar
siSerial = _SiSerial_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 1, 3),
    _SiSerial_Type()
)
siSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    siSerial.setStatus("mandatory")
_SiFirmVer_Type = OctetString
_SiFirmVer_Object = MibScalar
siFirmVer = _SiFirmVer_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 1, 4),
    _SiFirmVer_Type()
)
siFirmVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    siFirmVer.setStatus("mandatory")
_SiBootVer_Type = OctetString
_SiBootVer_Object = MibScalar
siBootVer = _SiBootVer_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 1, 5),
    _SiBootVer_Type()
)
siBootVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    siBootVer.setStatus("mandatory")
_SiMbrVer_Type = OctetString
_SiMbrVer_Object = MibScalar
siMbrVer = _SiMbrVer_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 1, 6),
    _SiMbrVer_Type()
)
siMbrVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    siMbrVer.setStatus("mandatory")
_SiProcessor_Type = OctetString
_SiProcessor_Object = MibScalar
siProcessor = _SiProcessor_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 1, 7),
    _SiProcessor_Type()
)
siProcessor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    siProcessor.setStatus("mandatory")
_SiCpuSpeed_Type = Integer32
_SiCpuSpeed_Object = MibScalar
siCpuSpeed = _SiCpuSpeed_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 1, 8),
    _SiCpuSpeed_Type()
)
siCpuSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    siCpuSpeed.setStatus("mandatory")


class _SiICache_Type(Integer32):
    """Custom type siICache based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(32768,
              524288)
        )
    )
    namedValues = NamedValues(
        *(("s32K", 32768),
          ("s512K", 524288))
    )


_SiICache_Type.__name__ = "Integer32"
_SiICache_Object = MibScalar
siICache = _SiICache_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 1, 9),
    _SiICache_Type()
)
siICache.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    siICache.setStatus("mandatory")


class _SiDCache_Type(Integer32):
    """Custom type siDCache based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(32768,
              524288)
        )
    )
    namedValues = NamedValues(
        *(("s32K", 32768),
          ("s512K", 524288))
    )


_SiDCache_Type.__name__ = "Integer32"
_SiDCache_Object = MibScalar
siDCache = _SiDCache_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 1, 10),
    _SiDCache_Type()
)
siDCache.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    siDCache.setStatus("mandatory")


class _SiSCache_Type(Integer32):
    """Custom type siSCache based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(32768,
              524288)
        )
    )
    namedValues = NamedValues(
        *(("s32K", 32768),
          ("s512K", 524288))
    )


_SiSCache_Type.__name__ = "Integer32"
_SiSCache_Object = MibScalar
siSCache = _SiSCache_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 1, 11),
    _SiSCache_Type()
)
siSCache.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    siSCache.setStatus("mandatory")
_SiMemory_Type = Integer32
_SiMemory_Object = MibScalar
siMemory = _SiMemory_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 1, 12),
    _SiMemory_Type()
)
siMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    siMemory.setStatus("mandatory")
_SiMemSpeed_Type = Integer32
_SiMemSpeed_Object = MibScalar
siMemSpeed = _SiMemSpeed_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 1, 13),
    _SiMemSpeed_Type()
)
siMemSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    siMemSpeed.setStatus("mandatory")


class _SiEcc_Type(Integer32):
    """Custom type siEcc based on Integer32"""
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


_SiEcc_Type.__name__ = "Integer32"
_SiEcc_Object = MibScalar
siEcc = _SiEcc_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 1, 14),
    _SiEcc_Type()
)
siEcc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    siEcc.setStatus("mandatory")
_SiHosts_Type = Integer32
_SiHosts_Object = MibScalar
siHosts = _SiHosts_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 1, 15),
    _SiHosts_Type()
)
siHosts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    siHosts.setStatus("mandatory")
_SiRaidSets_Type = Integer32
_SiRaidSets_Object = MibScalar
siRaidSets = _SiRaidSets_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 1, 16),
    _SiRaidSets_Type()
)
siRaidSets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    siRaidSets.setStatus("mandatory")
_SiVolumeSets_Type = Integer32
_SiVolumeSets_Object = MibScalar
siVolumeSets = _SiVolumeSets_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 1, 17),
    _SiVolumeSets_Type()
)
siVolumeSets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    siVolumeSets.setStatus("mandatory")
_SiEvents_Type = Integer32
_SiEvents_Object = MibScalar
siEvents = _SiEvents_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 1, 18),
    _SiEvents_Type()
)
siEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    siEvents.setStatus("mandatory")


class _SiRaid6_Type(Integer32):
    """Custom type siRaid6 based on Integer32"""
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


_SiRaid6_Type.__name__ = "Integer32"
_SiRaid6_Object = MibScalar
siRaid6 = _SiRaid6_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 1, 19),
    _SiRaid6_Type()
)
siRaid6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    siRaid6.setStatus("mandatory")


class _SiDhcp_Type(Integer32):
    """Custom type siDhcp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SiDhcp_Type.__name__ = "Integer32"
_SiDhcp_Object = MibScalar
siDhcp = _SiDhcp_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 1, 20),
    _SiDhcp_Type()
)
siDhcp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    siDhcp.setStatus("mandatory")


class _SiBeeper_Type(Integer32):
    """Custom type siBeeper based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SiBeeper_Type.__name__ = "Integer32"
_SiBeeper_Object = MibScalar
siBeeper = _SiBeeper_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 1, 21),
    _SiBeeper_Type()
)
siBeeper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    siBeeper.setStatus("mandatory")


class _SiUsage_Type(Integer32):
    """Custom type siUsage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("jbod", 1))
    )


_SiUsage_Type.__name__ = "Integer32"
_SiUsage_Object = MibScalar
siUsage = _SiUsage_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 1, 22),
    _SiUsage_Type()
)
siUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    siUsage.setStatus("mandatory")
_SiRebuildRate_Type = Integer32
_SiRebuildRate_Object = MibScalar
siRebuildRate = _SiRebuildRate_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 1, 23),
    _SiRebuildRate_Type()
)
siRebuildRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    siRebuildRate.setStatus("mandatory")


class _SiBaudRate_Type(Integer32):
    """Custom type siBaudRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1200,
              2400,
              4800,
              9600,
              19200,
              38400,
              57600,
              115200)
        )
    )
    namedValues = NamedValues(
        *(("s1200bps", 1200),
          ("s2400bps", 2400),
          ("s4800bps", 4800),
          ("s9600bps", 9600),
          ("s19200bps", 19200),
          ("s38400bps", 38400),
          ("s57600bps", 57600),
          ("s115200bps", 115200))
    )


_SiBaudRate_Type.__name__ = "Integer32"
_SiBaudRate_Object = MibScalar
siBaudRate = _SiBaudRate_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 1, 24),
    _SiBaudRate_Type()
)
siBaudRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    siBaudRate.setStatus("mandatory")
_HwMonitor_ObjectIdentity = ObjectIdentity
hwMonitor = _HwMonitor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2)
)
_ControllerBoard_ObjectIdentity = ObjectIdentity
controllerBoard = _ControllerBoard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 1)
)
_HwControllerBoardInstalled_Type = Integer32
_HwControllerBoardInstalled_Object = MibScalar
hwControllerBoardInstalled = _HwControllerBoardInstalled_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 1, 1),
    _HwControllerBoardInstalled_Type()
)
hwControllerBoardInstalled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwControllerBoardInstalled.setStatus("mandatory")
_HwControllerBoardDescription_Type = OctetString
_HwControllerBoardDescription_Object = MibScalar
hwControllerBoardDescription = _HwControllerBoardDescription_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 1, 2),
    _HwControllerBoardDescription_Type()
)
hwControllerBoardDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwControllerBoardDescription.setStatus("mandatory")
_HwControllerBoardNumberOfPower_Type = Integer32
_HwControllerBoardNumberOfPower_Object = MibScalar
hwControllerBoardNumberOfPower = _HwControllerBoardNumberOfPower_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 1, 3),
    _HwControllerBoardNumberOfPower_Type()
)
hwControllerBoardNumberOfPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwControllerBoardNumberOfPower.setStatus("mandatory")
_HwControllerBoardNumberOfVol_Type = Integer32
_HwControllerBoardNumberOfVol_Object = MibScalar
hwControllerBoardNumberOfVol = _HwControllerBoardNumberOfVol_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 1, 4),
    _HwControllerBoardNumberOfVol_Type()
)
hwControllerBoardNumberOfVol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwControllerBoardNumberOfVol.setStatus("mandatory")
_HwControllerBoardNumberOfFan_Type = Integer32
_HwControllerBoardNumberOfFan_Object = MibScalar
hwControllerBoardNumberOfFan = _HwControllerBoardNumberOfFan_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 1, 5),
    _HwControllerBoardNumberOfFan_Type()
)
hwControllerBoardNumberOfFan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwControllerBoardNumberOfFan.setStatus("mandatory")
_HwControllerBoardNumberOfTemp_Type = Integer32
_HwControllerBoardNumberOfTemp_Object = MibScalar
hwControllerBoardNumberOfTemp = _HwControllerBoardNumberOfTemp_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 1, 6),
    _HwControllerBoardNumberOfTemp_Type()
)
hwControllerBoardNumberOfTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwControllerBoardNumberOfTemp.setStatus("mandatory")
_HwControllerBoardPowerTable_Object = MibTable
hwControllerBoardPowerTable = _HwControllerBoardPowerTable_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 1, 7)
)
if mibBuilder.loadTexts:
    hwControllerBoardPowerTable.setStatus("mandatory")
_HwControllerBoardPowerEntry_Object = MibTableRow
hwControllerBoardPowerEntry = _HwControllerBoardPowerEntry_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 1, 7, 1)
)
hwControllerBoardPowerEntry.setIndexNames(
    (0, "ARECA-SAS-CARD1-MIB", "hwControllerBoardPowerIndex"),
)
if mibBuilder.loadTexts:
    hwControllerBoardPowerEntry.setStatus("mandatory")
_HwControllerBoardPowerIndex_Type = Integer32
_HwControllerBoardPowerIndex_Object = MibTableColumn
hwControllerBoardPowerIndex = _HwControllerBoardPowerIndex_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 1, 7, 1, 1),
    _HwControllerBoardPowerIndex_Type()
)
hwControllerBoardPowerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwControllerBoardPowerIndex.setStatus("mandatory")
_HwControllerBoardPowerDesc_Type = OctetString
_HwControllerBoardPowerDesc_Object = MibTableColumn
hwControllerBoardPowerDesc = _HwControllerBoardPowerDesc_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 1, 7, 1, 2),
    _HwControllerBoardPowerDesc_Type()
)
hwControllerBoardPowerDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwControllerBoardPowerDesc.setStatus("mandatory")


class _HwControllerBoardPowerState_Type(Integer32):
    """Custom type hwControllerBoardPowerState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("failed", 0),
          ("ok", 1))
    )


_HwControllerBoardPowerState_Type.__name__ = "Integer32"
_HwControllerBoardPowerState_Object = MibTableColumn
hwControllerBoardPowerState = _HwControllerBoardPowerState_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 1, 7, 1, 3),
    _HwControllerBoardPowerState_Type()
)
hwControllerBoardPowerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwControllerBoardPowerState.setStatus("mandatory")
_HwControllerBoardVolTable_Object = MibTable
hwControllerBoardVolTable = _HwControllerBoardVolTable_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 1, 8)
)
if mibBuilder.loadTexts:
    hwControllerBoardVolTable.setStatus("mandatory")
_HwControllerBoardVolEntry_Object = MibTableRow
hwControllerBoardVolEntry = _HwControllerBoardVolEntry_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 1, 8, 1)
)
hwControllerBoardVolEntry.setIndexNames(
    (0, "ARECA-SAS-CARD1-MIB", "hwControllerBoardVolIndex"),
)
if mibBuilder.loadTexts:
    hwControllerBoardVolEntry.setStatus("mandatory")
_HwControllerBoardVolIndex_Type = Integer32
_HwControllerBoardVolIndex_Object = MibTableColumn
hwControllerBoardVolIndex = _HwControllerBoardVolIndex_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 1, 8, 1, 1),
    _HwControllerBoardVolIndex_Type()
)
hwControllerBoardVolIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwControllerBoardVolIndex.setStatus("mandatory")
_HwControllerBoardVolDesc_Type = OctetString
_HwControllerBoardVolDesc_Object = MibTableColumn
hwControllerBoardVolDesc = _HwControllerBoardVolDesc_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 1, 8, 1, 2),
    _HwControllerBoardVolDesc_Type()
)
hwControllerBoardVolDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwControllerBoardVolDesc.setStatus("mandatory")
_HwControllerBoardVolValue_Type = Integer32
_HwControllerBoardVolValue_Object = MibTableColumn
hwControllerBoardVolValue = _HwControllerBoardVolValue_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 1, 8, 1, 3),
    _HwControllerBoardVolValue_Type()
)
hwControllerBoardVolValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwControllerBoardVolValue.setStatus("mandatory")
_HwControllerBoardFanTable_Object = MibTable
hwControllerBoardFanTable = _HwControllerBoardFanTable_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 1, 9)
)
if mibBuilder.loadTexts:
    hwControllerBoardFanTable.setStatus("mandatory")
_HwControllerBoardFanEntry_Object = MibTableRow
hwControllerBoardFanEntry = _HwControllerBoardFanEntry_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 1, 9, 1)
)
hwControllerBoardFanEntry.setIndexNames(
    (0, "ARECA-SAS-CARD1-MIB", "hwControllerBoardFanIndex"),
)
if mibBuilder.loadTexts:
    hwControllerBoardFanEntry.setStatus("mandatory")
_HwControllerBoardFanIndex_Type = Integer32
_HwControllerBoardFanIndex_Object = MibTableColumn
hwControllerBoardFanIndex = _HwControllerBoardFanIndex_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 1, 9, 1, 1),
    _HwControllerBoardFanIndex_Type()
)
hwControllerBoardFanIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwControllerBoardFanIndex.setStatus("mandatory")
_HwControllerBoardFanDesc_Type = OctetString
_HwControllerBoardFanDesc_Object = MibTableColumn
hwControllerBoardFanDesc = _HwControllerBoardFanDesc_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 1, 9, 1, 2),
    _HwControllerBoardFanDesc_Type()
)
hwControllerBoardFanDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwControllerBoardFanDesc.setStatus("mandatory")
_HwControllerBoardFanSpeed_Type = Integer32
_HwControllerBoardFanSpeed_Object = MibTableColumn
hwControllerBoardFanSpeed = _HwControllerBoardFanSpeed_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 1, 9, 1, 3),
    _HwControllerBoardFanSpeed_Type()
)
hwControllerBoardFanSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwControllerBoardFanSpeed.setStatus("mandatory")
_HwControllerBoardTempTable_Object = MibTable
hwControllerBoardTempTable = _HwControllerBoardTempTable_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 1, 10)
)
if mibBuilder.loadTexts:
    hwControllerBoardTempTable.setStatus("mandatory")
_HwControllerBoardTempEntry_Object = MibTableRow
hwControllerBoardTempEntry = _HwControllerBoardTempEntry_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 1, 10, 1)
)
hwControllerBoardTempEntry.setIndexNames(
    (0, "ARECA-SAS-CARD1-MIB", "hwControllerBoardTempIndex"),
)
if mibBuilder.loadTexts:
    hwControllerBoardTempEntry.setStatus("mandatory")
_HwControllerBoardTempIndex_Type = Integer32
_HwControllerBoardTempIndex_Object = MibTableColumn
hwControllerBoardTempIndex = _HwControllerBoardTempIndex_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 1, 10, 1, 1),
    _HwControllerBoardTempIndex_Type()
)
hwControllerBoardTempIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwControllerBoardTempIndex.setStatus("mandatory")
_HwControllerBoardTempDesc_Type = OctetString
_HwControllerBoardTempDesc_Object = MibTableColumn
hwControllerBoardTempDesc = _HwControllerBoardTempDesc_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 1, 10, 1, 2),
    _HwControllerBoardTempDesc_Type()
)
hwControllerBoardTempDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwControllerBoardTempDesc.setStatus("mandatory")
_HwControllerBoardTempValue_Type = Integer32
_HwControllerBoardTempValue_Object = MibTableColumn
hwControllerBoardTempValue = _HwControllerBoardTempValue_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 1, 10, 1, 3),
    _HwControllerBoardTempValue_Type()
)
hwControllerBoardTempValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwControllerBoardTempValue.setStatus("mandatory")
_HwEnclosure1_ObjectIdentity = ObjectIdentity
hwEnclosure1 = _HwEnclosure1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 2)
)
_HwEnclosure01Installed_Type = Integer32
_HwEnclosure01Installed_Object = MibScalar
hwEnclosure01Installed = _HwEnclosure01Installed_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 2, 1),
    _HwEnclosure01Installed_Type()
)
hwEnclosure01Installed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEnclosure01Installed.setStatus("mandatory")
_HwEnclosure01Description_Type = OctetString
_HwEnclosure01Description_Object = MibScalar
hwEnclosure01Description = _HwEnclosure01Description_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 2, 2),
    _HwEnclosure01Description_Type()
)
hwEnclosure01Description.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEnclosure01Description.setStatus("mandatory")
_HwEnclosure01NumberOfPower_Type = Integer32
_HwEnclosure01NumberOfPower_Object = MibScalar
hwEnclosure01NumberOfPower = _HwEnclosure01NumberOfPower_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 2, 3),
    _HwEnclosure01NumberOfPower_Type()
)
hwEnclosure01NumberOfPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEnclosure01NumberOfPower.setStatus("mandatory")
_HwEnclosure01NumberOfVol_Type = Integer32
_HwEnclosure01NumberOfVol_Object = MibScalar
hwEnclosure01NumberOfVol = _HwEnclosure01NumberOfVol_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 2, 4),
    _HwEnclosure01NumberOfVol_Type()
)
hwEnclosure01NumberOfVol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEnclosure01NumberOfVol.setStatus("mandatory")
_HwEnclosure01NumberOfFan_Type = Integer32
_HwEnclosure01NumberOfFan_Object = MibScalar
hwEnclosure01NumberOfFan = _HwEnclosure01NumberOfFan_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 2, 5),
    _HwEnclosure01NumberOfFan_Type()
)
hwEnclosure01NumberOfFan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEnclosure01NumberOfFan.setStatus("mandatory")
_HwEnclosure01NumberOfTemp_Type = Integer32
_HwEnclosure01NumberOfTemp_Object = MibScalar
hwEnclosure01NumberOfTemp = _HwEnclosure01NumberOfTemp_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 2, 6),
    _HwEnclosure01NumberOfTemp_Type()
)
hwEnclosure01NumberOfTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEnclosure01NumberOfTemp.setStatus("mandatory")
_HwEnclosure01PowerTable_Object = MibTable
hwEnclosure01PowerTable = _HwEnclosure01PowerTable_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 2, 7)
)
if mibBuilder.loadTexts:
    hwEnclosure01PowerTable.setStatus("mandatory")
_HwEnclosure01PowerEntry_Object = MibTableRow
hwEnclosure01PowerEntry = _HwEnclosure01PowerEntry_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 2, 7, 1)
)
hwEnclosure01PowerEntry.setIndexNames(
    (0, "ARECA-SAS-CARD1-MIB", "hwEnclosure01PowerIndex"),
)
if mibBuilder.loadTexts:
    hwEnclosure01PowerEntry.setStatus("mandatory")
_HwEnclosure01PowerIndex_Type = Integer32
_HwEnclosure01PowerIndex_Object = MibTableColumn
hwEnclosure01PowerIndex = _HwEnclosure01PowerIndex_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 2, 7, 1, 1),
    _HwEnclosure01PowerIndex_Type()
)
hwEnclosure01PowerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEnclosure01PowerIndex.setStatus("mandatory")
_HwEnclosure01PowerDesc_Type = OctetString
_HwEnclosure01PowerDesc_Object = MibTableColumn
hwEnclosure01PowerDesc = _HwEnclosure01PowerDesc_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 2, 7, 1, 2),
    _HwEnclosure01PowerDesc_Type()
)
hwEnclosure01PowerDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEnclosure01PowerDesc.setStatus("mandatory")


class _HwEnclosure01PowerState_Type(Integer32):
    """Custom type hwEnclosure01PowerState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("failed", 0),
          ("ok", 1))
    )


_HwEnclosure01PowerState_Type.__name__ = "Integer32"
_HwEnclosure01PowerState_Object = MibTableColumn
hwEnclosure01PowerState = _HwEnclosure01PowerState_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 2, 7, 1, 3),
    _HwEnclosure01PowerState_Type()
)
hwEnclosure01PowerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEnclosure01PowerState.setStatus("mandatory")
_HwEnclosure01VolTable_Object = MibTable
hwEnclosure01VolTable = _HwEnclosure01VolTable_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 2, 8)
)
if mibBuilder.loadTexts:
    hwEnclosure01VolTable.setStatus("mandatory")
_HwEnclosure01VolEntry_Object = MibTableRow
hwEnclosure01VolEntry = _HwEnclosure01VolEntry_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 2, 8, 1)
)
hwEnclosure01VolEntry.setIndexNames(
    (0, "ARECA-SAS-CARD1-MIB", "hwEnclosure01VolIndex"),
)
if mibBuilder.loadTexts:
    hwEnclosure01VolEntry.setStatus("mandatory")
_HwEnclosure01VolIndex_Type = Integer32
_HwEnclosure01VolIndex_Object = MibTableColumn
hwEnclosure01VolIndex = _HwEnclosure01VolIndex_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 2, 8, 1, 1),
    _HwEnclosure01VolIndex_Type()
)
hwEnclosure01VolIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEnclosure01VolIndex.setStatus("mandatory")
_HwEnclosure01VolDesc_Type = OctetString
_HwEnclosure01VolDesc_Object = MibTableColumn
hwEnclosure01VolDesc = _HwEnclosure01VolDesc_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 2, 8, 1, 2),
    _HwEnclosure01VolDesc_Type()
)
hwEnclosure01VolDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEnclosure01VolDesc.setStatus("mandatory")
_HwEnclosure01VolValue_Type = Integer32
_HwEnclosure01VolValue_Object = MibTableColumn
hwEnclosure01VolValue = _HwEnclosure01VolValue_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 2, 8, 1, 3),
    _HwEnclosure01VolValue_Type()
)
hwEnclosure01VolValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEnclosure01VolValue.setStatus("mandatory")
_HwEnclosure01FanTable_Object = MibTable
hwEnclosure01FanTable = _HwEnclosure01FanTable_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 2, 9)
)
if mibBuilder.loadTexts:
    hwEnclosure01FanTable.setStatus("mandatory")
_HwEnclosure01FanEntry_Object = MibTableRow
hwEnclosure01FanEntry = _HwEnclosure01FanEntry_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 2, 9, 1)
)
hwEnclosure01FanEntry.setIndexNames(
    (0, "ARECA-SAS-CARD1-MIB", "hwEnclosure01FanIndex"),
)
if mibBuilder.loadTexts:
    hwEnclosure01FanEntry.setStatus("mandatory")
_HwEnclosure01FanIndex_Type = Integer32
_HwEnclosure01FanIndex_Object = MibTableColumn
hwEnclosure01FanIndex = _HwEnclosure01FanIndex_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 2, 9, 1, 1),
    _HwEnclosure01FanIndex_Type()
)
hwEnclosure01FanIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEnclosure01FanIndex.setStatus("mandatory")
_HwEnclosure01FanDesc_Type = OctetString
_HwEnclosure01FanDesc_Object = MibTableColumn
hwEnclosure01FanDesc = _HwEnclosure01FanDesc_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 2, 9, 1, 2),
    _HwEnclosure01FanDesc_Type()
)
hwEnclosure01FanDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEnclosure01FanDesc.setStatus("mandatory")
_HwEnclosure01FanSpeed_Type = Integer32
_HwEnclosure01FanSpeed_Object = MibTableColumn
hwEnclosure01FanSpeed = _HwEnclosure01FanSpeed_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 2, 9, 1, 3),
    _HwEnclosure01FanSpeed_Type()
)
hwEnclosure01FanSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEnclosure01FanSpeed.setStatus("mandatory")
_HwEnclosure01TempTable_Object = MibTable
hwEnclosure01TempTable = _HwEnclosure01TempTable_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 2, 10)
)
if mibBuilder.loadTexts:
    hwEnclosure01TempTable.setStatus("mandatory")
_HwEnclosure01TempEntry_Object = MibTableRow
hwEnclosure01TempEntry = _HwEnclosure01TempEntry_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 2, 10, 1)
)
hwEnclosure01TempEntry.setIndexNames(
    (0, "ARECA-SAS-CARD1-MIB", "hwEnclosure01TempIndex"),
)
if mibBuilder.loadTexts:
    hwEnclosure01TempEntry.setStatus("mandatory")
_HwEnclosure01TempIndex_Type = Integer32
_HwEnclosure01TempIndex_Object = MibTableColumn
hwEnclosure01TempIndex = _HwEnclosure01TempIndex_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 2, 10, 1, 1),
    _HwEnclosure01TempIndex_Type()
)
hwEnclosure01TempIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEnclosure01TempIndex.setStatus("mandatory")
_HwEnclosure01TempDesc_Type = OctetString
_HwEnclosure01TempDesc_Object = MibTableColumn
hwEnclosure01TempDesc = _HwEnclosure01TempDesc_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 2, 10, 1, 2),
    _HwEnclosure01TempDesc_Type()
)
hwEnclosure01TempDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEnclosure01TempDesc.setStatus("mandatory")
_HwEnclosure01TempValue_Type = Integer32
_HwEnclosure01TempValue_Object = MibTableColumn
hwEnclosure01TempValue = _HwEnclosure01TempValue_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 2, 10, 1, 3),
    _HwEnclosure01TempValue_Type()
)
hwEnclosure01TempValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEnclosure01TempValue.setStatus("mandatory")
_HwEnclosure2_ObjectIdentity = ObjectIdentity
hwEnclosure2 = _HwEnclosure2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 3)
)
_HwEnclosure02Installed_Type = Integer32
_HwEnclosure02Installed_Object = MibScalar
hwEnclosure02Installed = _HwEnclosure02Installed_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 3, 1),
    _HwEnclosure02Installed_Type()
)
hwEnclosure02Installed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEnclosure02Installed.setStatus("mandatory")
_HwEnclosure02Description_Type = OctetString
_HwEnclosure02Description_Object = MibScalar
hwEnclosure02Description = _HwEnclosure02Description_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 3, 2),
    _HwEnclosure02Description_Type()
)
hwEnclosure02Description.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEnclosure02Description.setStatus("mandatory")
_HwEnclosure02NumberOfPower_Type = Integer32
_HwEnclosure02NumberOfPower_Object = MibScalar
hwEnclosure02NumberOfPower = _HwEnclosure02NumberOfPower_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 3, 3),
    _HwEnclosure02NumberOfPower_Type()
)
hwEnclosure02NumberOfPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEnclosure02NumberOfPower.setStatus("mandatory")
_HwEnclosure02NumberOfVol_Type = Integer32
_HwEnclosure02NumberOfVol_Object = MibScalar
hwEnclosure02NumberOfVol = _HwEnclosure02NumberOfVol_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 3, 4),
    _HwEnclosure02NumberOfVol_Type()
)
hwEnclosure02NumberOfVol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEnclosure02NumberOfVol.setStatus("mandatory")
_HwEnclosure02NumberOfFan_Type = Integer32
_HwEnclosure02NumberOfFan_Object = MibScalar
hwEnclosure02NumberOfFan = _HwEnclosure02NumberOfFan_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 3, 5),
    _HwEnclosure02NumberOfFan_Type()
)
hwEnclosure02NumberOfFan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEnclosure02NumberOfFan.setStatus("mandatory")
_HwEnclosure02NumberOfTemp_Type = Integer32
_HwEnclosure02NumberOfTemp_Object = MibScalar
hwEnclosure02NumberOfTemp = _HwEnclosure02NumberOfTemp_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 3, 6),
    _HwEnclosure02NumberOfTemp_Type()
)
hwEnclosure02NumberOfTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEnclosure02NumberOfTemp.setStatus("mandatory")
_HwEnclosure02PowerTable_Object = MibTable
hwEnclosure02PowerTable = _HwEnclosure02PowerTable_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 3, 7)
)
if mibBuilder.loadTexts:
    hwEnclosure02PowerTable.setStatus("mandatory")
_HwEnclosure02PowerEntry_Object = MibTableRow
hwEnclosure02PowerEntry = _HwEnclosure02PowerEntry_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 3, 7, 1)
)
hwEnclosure02PowerEntry.setIndexNames(
    (0, "ARECA-SAS-CARD1-MIB", "hwEnclosure02PowerIndex"),
)
if mibBuilder.loadTexts:
    hwEnclosure02PowerEntry.setStatus("mandatory")
_HwEnclosure02PowerIndex_Type = Integer32
_HwEnclosure02PowerIndex_Object = MibTableColumn
hwEnclosure02PowerIndex = _HwEnclosure02PowerIndex_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 3, 7, 1, 1),
    _HwEnclosure02PowerIndex_Type()
)
hwEnclosure02PowerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEnclosure02PowerIndex.setStatus("mandatory")
_HwEnclosure02PowerDesc_Type = OctetString
_HwEnclosure02PowerDesc_Object = MibTableColumn
hwEnclosure02PowerDesc = _HwEnclosure02PowerDesc_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 3, 7, 1, 2),
    _HwEnclosure02PowerDesc_Type()
)
hwEnclosure02PowerDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEnclosure02PowerDesc.setStatus("mandatory")


class _HwEnclosure02PowerState_Type(Integer32):
    """Custom type hwEnclosure02PowerState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("failed", 0),
          ("ok", 1))
    )


_HwEnclosure02PowerState_Type.__name__ = "Integer32"
_HwEnclosure02PowerState_Object = MibTableColumn
hwEnclosure02PowerState = _HwEnclosure02PowerState_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 3, 7, 1, 3),
    _HwEnclosure02PowerState_Type()
)
hwEnclosure02PowerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEnclosure02PowerState.setStatus("mandatory")
_HwEnclosure02VolTable_Object = MibTable
hwEnclosure02VolTable = _HwEnclosure02VolTable_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 3, 8)
)
if mibBuilder.loadTexts:
    hwEnclosure02VolTable.setStatus("mandatory")
_HwEnclosure02VolEntry_Object = MibTableRow
hwEnclosure02VolEntry = _HwEnclosure02VolEntry_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 3, 8, 1)
)
hwEnclosure02VolEntry.setIndexNames(
    (0, "ARECA-SAS-CARD1-MIB", "hwEnclosure02VolIndex"),
)
if mibBuilder.loadTexts:
    hwEnclosure02VolEntry.setStatus("mandatory")
_HwEnclosure02VolIndex_Type = Integer32
_HwEnclosure02VolIndex_Object = MibTableColumn
hwEnclosure02VolIndex = _HwEnclosure02VolIndex_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 3, 8, 1, 1),
    _HwEnclosure02VolIndex_Type()
)
hwEnclosure02VolIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEnclosure02VolIndex.setStatus("mandatory")
_HwEnclosure02VolDesc_Type = OctetString
_HwEnclosure02VolDesc_Object = MibTableColumn
hwEnclosure02VolDesc = _HwEnclosure02VolDesc_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 3, 8, 1, 2),
    _HwEnclosure02VolDesc_Type()
)
hwEnclosure02VolDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEnclosure02VolDesc.setStatus("mandatory")
_HwEnclosure02VolValue_Type = Integer32
_HwEnclosure02VolValue_Object = MibTableColumn
hwEnclosure02VolValue = _HwEnclosure02VolValue_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 3, 8, 1, 3),
    _HwEnclosure02VolValue_Type()
)
hwEnclosure02VolValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEnclosure02VolValue.setStatus("mandatory")
_HwEnclosure02FanTable_Object = MibTable
hwEnclosure02FanTable = _HwEnclosure02FanTable_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 3, 9)
)
if mibBuilder.loadTexts:
    hwEnclosure02FanTable.setStatus("mandatory")
_HwEnclosure02FanEntry_Object = MibTableRow
hwEnclosure02FanEntry = _HwEnclosure02FanEntry_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 3, 9, 1)
)
hwEnclosure02FanEntry.setIndexNames(
    (0, "ARECA-SAS-CARD1-MIB", "hwEnclosure02FanIndex"),
)
if mibBuilder.loadTexts:
    hwEnclosure02FanEntry.setStatus("mandatory")
_HwEnclosure02FanIndex_Type = Integer32
_HwEnclosure02FanIndex_Object = MibTableColumn
hwEnclosure02FanIndex = _HwEnclosure02FanIndex_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 3, 9, 1, 1),
    _HwEnclosure02FanIndex_Type()
)
hwEnclosure02FanIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEnclosure02FanIndex.setStatus("mandatory")
_HwEnclosure02FanDesc_Type = OctetString
_HwEnclosure02FanDesc_Object = MibTableColumn
hwEnclosure02FanDesc = _HwEnclosure02FanDesc_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 3, 9, 1, 2),
    _HwEnclosure02FanDesc_Type()
)
hwEnclosure02FanDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEnclosure02FanDesc.setStatus("mandatory")
_HwEnclosure02FanSpeed_Type = Integer32
_HwEnclosure02FanSpeed_Object = MibTableColumn
hwEnclosure02FanSpeed = _HwEnclosure02FanSpeed_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 3, 9, 1, 3),
    _HwEnclosure02FanSpeed_Type()
)
hwEnclosure02FanSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEnclosure02FanSpeed.setStatus("mandatory")
_HwEnclosure02TempTable_Object = MibTable
hwEnclosure02TempTable = _HwEnclosure02TempTable_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 3, 10)
)
if mibBuilder.loadTexts:
    hwEnclosure02TempTable.setStatus("mandatory")
_HwEnclosure02TempEntry_Object = MibTableRow
hwEnclosure02TempEntry = _HwEnclosure02TempEntry_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 3, 10, 1)
)
hwEnclosure02TempEntry.setIndexNames(
    (0, "ARECA-SAS-CARD1-MIB", "hwEnclosure02TempIndex"),
)
if mibBuilder.loadTexts:
    hwEnclosure02TempEntry.setStatus("mandatory")
_HwEnclosure02TempIndex_Type = Integer32
_HwEnclosure02TempIndex_Object = MibTableColumn
hwEnclosure02TempIndex = _HwEnclosure02TempIndex_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 3, 10, 1, 1),
    _HwEnclosure02TempIndex_Type()
)
hwEnclosure02TempIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEnclosure02TempIndex.setStatus("mandatory")
_HwEnclosure02TempDesc_Type = OctetString
_HwEnclosure02TempDesc_Object = MibTableColumn
hwEnclosure02TempDesc = _HwEnclosure02TempDesc_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 3, 10, 1, 2),
    _HwEnclosure02TempDesc_Type()
)
hwEnclosure02TempDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEnclosure02TempDesc.setStatus("mandatory")
_HwEnclosure02TempValue_Type = Integer32
_HwEnclosure02TempValue_Object = MibTableColumn
hwEnclosure02TempValue = _HwEnclosure02TempValue_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 3, 10, 1, 3),
    _HwEnclosure02TempValue_Type()
)
hwEnclosure02TempValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEnclosure02TempValue.setStatus("mandatory")
_HwEnclosure3_ObjectIdentity = ObjectIdentity
hwEnclosure3 = _HwEnclosure3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 4)
)
_HwEnclosure03Installed_Type = Integer32
_HwEnclosure03Installed_Object = MibScalar
hwEnclosure03Installed = _HwEnclosure03Installed_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 4, 1),
    _HwEnclosure03Installed_Type()
)
hwEnclosure03Installed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEnclosure03Installed.setStatus("mandatory")
_HwEnclosure03Description_Type = OctetString
_HwEnclosure03Description_Object = MibScalar
hwEnclosure03Description = _HwEnclosure03Description_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 4, 2),
    _HwEnclosure03Description_Type()
)
hwEnclosure03Description.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEnclosure03Description.setStatus("mandatory")
_HwEnclosure03NumberOfPower_Type = Integer32
_HwEnclosure03NumberOfPower_Object = MibScalar
hwEnclosure03NumberOfPower = _HwEnclosure03NumberOfPower_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 4, 3),
    _HwEnclosure03NumberOfPower_Type()
)
hwEnclosure03NumberOfPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEnclosure03NumberOfPower.setStatus("mandatory")
_HwEnclosure03NumberOfVol_Type = Integer32
_HwEnclosure03NumberOfVol_Object = MibScalar
hwEnclosure03NumberOfVol = _HwEnclosure03NumberOfVol_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 4, 4),
    _HwEnclosure03NumberOfVol_Type()
)
hwEnclosure03NumberOfVol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEnclosure03NumberOfVol.setStatus("mandatory")
_HwEnclosure03NumberOfFan_Type = Integer32
_HwEnclosure03NumberOfFan_Object = MibScalar
hwEnclosure03NumberOfFan = _HwEnclosure03NumberOfFan_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 4, 5),
    _HwEnclosure03NumberOfFan_Type()
)
hwEnclosure03NumberOfFan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEnclosure03NumberOfFan.setStatus("mandatory")
_HwEnclosure03NumberOfTemp_Type = Integer32
_HwEnclosure03NumberOfTemp_Object = MibScalar
hwEnclosure03NumberOfTemp = _HwEnclosure03NumberOfTemp_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 4, 6),
    _HwEnclosure03NumberOfTemp_Type()
)
hwEnclosure03NumberOfTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEnclosure03NumberOfTemp.setStatus("mandatory")
_HwEnclosure03PowerTable_Object = MibTable
hwEnclosure03PowerTable = _HwEnclosure03PowerTable_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 4, 7)
)
if mibBuilder.loadTexts:
    hwEnclosure03PowerTable.setStatus("mandatory")
_HwEnclosure03PowerEntry_Object = MibTableRow
hwEnclosure03PowerEntry = _HwEnclosure03PowerEntry_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 4, 7, 1)
)
hwEnclosure03PowerEntry.setIndexNames(
    (0, "ARECA-SAS-CARD1-MIB", "hwEnclosure03PowerIndex"),
)
if mibBuilder.loadTexts:
    hwEnclosure03PowerEntry.setStatus("mandatory")
_HwEnclosure03PowerIndex_Type = Integer32
_HwEnclosure03PowerIndex_Object = MibTableColumn
hwEnclosure03PowerIndex = _HwEnclosure03PowerIndex_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 4, 7, 1, 1),
    _HwEnclosure03PowerIndex_Type()
)
hwEnclosure03PowerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEnclosure03PowerIndex.setStatus("mandatory")
_HwEnclosure03PowerDesc_Type = OctetString
_HwEnclosure03PowerDesc_Object = MibTableColumn
hwEnclosure03PowerDesc = _HwEnclosure03PowerDesc_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 4, 7, 1, 2),
    _HwEnclosure03PowerDesc_Type()
)
hwEnclosure03PowerDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEnclosure03PowerDesc.setStatus("mandatory")


class _HwEnclosure03PowerState_Type(Integer32):
    """Custom type hwEnclosure03PowerState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("failed", 0),
          ("ok", 1))
    )


_HwEnclosure03PowerState_Type.__name__ = "Integer32"
_HwEnclosure03PowerState_Object = MibTableColumn
hwEnclosure03PowerState = _HwEnclosure03PowerState_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 4, 7, 1, 3),
    _HwEnclosure03PowerState_Type()
)
hwEnclosure03PowerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEnclosure03PowerState.setStatus("mandatory")
_HwEnclosure03VolTable_Object = MibTable
hwEnclosure03VolTable = _HwEnclosure03VolTable_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 4, 8)
)
if mibBuilder.loadTexts:
    hwEnclosure03VolTable.setStatus("mandatory")
_HwEnclosure03VolEntry_Object = MibTableRow
hwEnclosure03VolEntry = _HwEnclosure03VolEntry_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 4, 8, 1)
)
hwEnclosure03VolEntry.setIndexNames(
    (0, "ARECA-SAS-CARD1-MIB", "hwEnclosure03VolIndex"),
)
if mibBuilder.loadTexts:
    hwEnclosure03VolEntry.setStatus("mandatory")
_HwEnclosure03VolIndex_Type = Integer32
_HwEnclosure03VolIndex_Object = MibTableColumn
hwEnclosure03VolIndex = _HwEnclosure03VolIndex_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 4, 8, 1, 1),
    _HwEnclosure03VolIndex_Type()
)
hwEnclosure03VolIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEnclosure03VolIndex.setStatus("mandatory")
_HwEnclosure03VolDesc_Type = OctetString
_HwEnclosure03VolDesc_Object = MibTableColumn
hwEnclosure03VolDesc = _HwEnclosure03VolDesc_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 4, 8, 1, 2),
    _HwEnclosure03VolDesc_Type()
)
hwEnclosure03VolDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEnclosure03VolDesc.setStatus("mandatory")
_HwEnclosure03VolValue_Type = Integer32
_HwEnclosure03VolValue_Object = MibTableColumn
hwEnclosure03VolValue = _HwEnclosure03VolValue_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 4, 8, 1, 3),
    _HwEnclosure03VolValue_Type()
)
hwEnclosure03VolValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEnclosure03VolValue.setStatus("mandatory")
_HwEnclosure03FanTable_Object = MibTable
hwEnclosure03FanTable = _HwEnclosure03FanTable_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 4, 9)
)
if mibBuilder.loadTexts:
    hwEnclosure03FanTable.setStatus("mandatory")
_HwEnclosure03FanEntry_Object = MibTableRow
hwEnclosure03FanEntry = _HwEnclosure03FanEntry_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 4, 9, 1)
)
hwEnclosure03FanEntry.setIndexNames(
    (0, "ARECA-SAS-CARD1-MIB", "hwEnclosure03FanIndex"),
)
if mibBuilder.loadTexts:
    hwEnclosure03FanEntry.setStatus("mandatory")
_HwEnclosure03FanIndex_Type = Integer32
_HwEnclosure03FanIndex_Object = MibTableColumn
hwEnclosure03FanIndex = _HwEnclosure03FanIndex_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 4, 9, 1, 1),
    _HwEnclosure03FanIndex_Type()
)
hwEnclosure03FanIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEnclosure03FanIndex.setStatus("mandatory")
_HwEnclosure03FanDesc_Type = OctetString
_HwEnclosure03FanDesc_Object = MibTableColumn
hwEnclosure03FanDesc = _HwEnclosure03FanDesc_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 4, 9, 1, 2),
    _HwEnclosure03FanDesc_Type()
)
hwEnclosure03FanDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEnclosure03FanDesc.setStatus("mandatory")
_HwEnclosure03FanSpeed_Type = Integer32
_HwEnclosure03FanSpeed_Object = MibTableColumn
hwEnclosure03FanSpeed = _HwEnclosure03FanSpeed_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 4, 9, 1, 3),
    _HwEnclosure03FanSpeed_Type()
)
hwEnclosure03FanSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEnclosure03FanSpeed.setStatus("mandatory")
_HwEnclosure03TempTable_Object = MibTable
hwEnclosure03TempTable = _HwEnclosure03TempTable_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 4, 10)
)
if mibBuilder.loadTexts:
    hwEnclosure03TempTable.setStatus("mandatory")
_HwEnclosure03TempEntry_Object = MibTableRow
hwEnclosure03TempEntry = _HwEnclosure03TempEntry_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 4, 10, 1)
)
hwEnclosure03TempEntry.setIndexNames(
    (0, "ARECA-SAS-CARD1-MIB", "hwEnclosure03TempIndex"),
)
if mibBuilder.loadTexts:
    hwEnclosure03TempEntry.setStatus("mandatory")
_HwEnclosure03TempIndex_Type = Integer32
_HwEnclosure03TempIndex_Object = MibTableColumn
hwEnclosure03TempIndex = _HwEnclosure03TempIndex_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 4, 10, 1, 1),
    _HwEnclosure03TempIndex_Type()
)
hwEnclosure03TempIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEnclosure03TempIndex.setStatus("mandatory")
_HwEnclosure03TempDesc_Type = OctetString
_HwEnclosure03TempDesc_Object = MibTableColumn
hwEnclosure03TempDesc = _HwEnclosure03TempDesc_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 4, 10, 1, 2),
    _HwEnclosure03TempDesc_Type()
)
hwEnclosure03TempDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEnclosure03TempDesc.setStatus("mandatory")
_HwEnclosure03TempValue_Type = Integer32
_HwEnclosure03TempValue_Object = MibTableColumn
hwEnclosure03TempValue = _HwEnclosure03TempValue_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 4, 10, 1, 3),
    _HwEnclosure03TempValue_Type()
)
hwEnclosure03TempValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEnclosure03TempValue.setStatus("mandatory")
_HwEnclosure4_ObjectIdentity = ObjectIdentity
hwEnclosure4 = _HwEnclosure4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 5)
)
_HwEnclosure04Installed_Type = Integer32
_HwEnclosure04Installed_Object = MibScalar
hwEnclosure04Installed = _HwEnclosure04Installed_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 5, 1),
    _HwEnclosure04Installed_Type()
)
hwEnclosure04Installed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEnclosure04Installed.setStatus("mandatory")
_HwEnclosure04Description_Type = OctetString
_HwEnclosure04Description_Object = MibScalar
hwEnclosure04Description = _HwEnclosure04Description_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 5, 2),
    _HwEnclosure04Description_Type()
)
hwEnclosure04Description.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEnclosure04Description.setStatus("mandatory")
_HwEnclosure04NumberOfPower_Type = Integer32
_HwEnclosure04NumberOfPower_Object = MibScalar
hwEnclosure04NumberOfPower = _HwEnclosure04NumberOfPower_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 5, 3),
    _HwEnclosure04NumberOfPower_Type()
)
hwEnclosure04NumberOfPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEnclosure04NumberOfPower.setStatus("mandatory")
_HwEnclosure04NumberOfVol_Type = Integer32
_HwEnclosure04NumberOfVol_Object = MibScalar
hwEnclosure04NumberOfVol = _HwEnclosure04NumberOfVol_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 5, 4),
    _HwEnclosure04NumberOfVol_Type()
)
hwEnclosure04NumberOfVol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEnclosure04NumberOfVol.setStatus("mandatory")
_HwEnclosure04NumberOfFan_Type = Integer32
_HwEnclosure04NumberOfFan_Object = MibScalar
hwEnclosure04NumberOfFan = _HwEnclosure04NumberOfFan_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 5, 5),
    _HwEnclosure04NumberOfFan_Type()
)
hwEnclosure04NumberOfFan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEnclosure04NumberOfFan.setStatus("mandatory")
_HwEnclosure04NumberOfTemp_Type = Integer32
_HwEnclosure04NumberOfTemp_Object = MibScalar
hwEnclosure04NumberOfTemp = _HwEnclosure04NumberOfTemp_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 5, 6),
    _HwEnclosure04NumberOfTemp_Type()
)
hwEnclosure04NumberOfTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEnclosure04NumberOfTemp.setStatus("mandatory")
_HwEnclosure04PowerTable_Object = MibTable
hwEnclosure04PowerTable = _HwEnclosure04PowerTable_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 5, 7)
)
if mibBuilder.loadTexts:
    hwEnclosure04PowerTable.setStatus("mandatory")
_HwEnclosure04PowerEntry_Object = MibTableRow
hwEnclosure04PowerEntry = _HwEnclosure04PowerEntry_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 5, 7, 1)
)
hwEnclosure04PowerEntry.setIndexNames(
    (0, "ARECA-SAS-CARD1-MIB", "hwEnclosure04PowerIndex"),
)
if mibBuilder.loadTexts:
    hwEnclosure04PowerEntry.setStatus("mandatory")
_HwEnclosure04PowerIndex_Type = Integer32
_HwEnclosure04PowerIndex_Object = MibTableColumn
hwEnclosure04PowerIndex = _HwEnclosure04PowerIndex_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 5, 7, 1, 1),
    _HwEnclosure04PowerIndex_Type()
)
hwEnclosure04PowerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEnclosure04PowerIndex.setStatus("mandatory")
_HwEnclosure04PowerDesc_Type = OctetString
_HwEnclosure04PowerDesc_Object = MibTableColumn
hwEnclosure04PowerDesc = _HwEnclosure04PowerDesc_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 5, 7, 1, 2),
    _HwEnclosure04PowerDesc_Type()
)
hwEnclosure04PowerDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEnclosure04PowerDesc.setStatus("mandatory")


class _HwEnclosure04PowerState_Type(Integer32):
    """Custom type hwEnclosure04PowerState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("failed", 0),
          ("ok", 1))
    )


_HwEnclosure04PowerState_Type.__name__ = "Integer32"
_HwEnclosure04PowerState_Object = MibTableColumn
hwEnclosure04PowerState = _HwEnclosure04PowerState_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 5, 7, 1, 3),
    _HwEnclosure04PowerState_Type()
)
hwEnclosure04PowerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEnclosure04PowerState.setStatus("mandatory")
_HwEnclosure04VolTable_Object = MibTable
hwEnclosure04VolTable = _HwEnclosure04VolTable_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 5, 8)
)
if mibBuilder.loadTexts:
    hwEnclosure04VolTable.setStatus("mandatory")
_HwEnclosure04VolEntry_Object = MibTableRow
hwEnclosure04VolEntry = _HwEnclosure04VolEntry_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 5, 8, 1)
)
hwEnclosure04VolEntry.setIndexNames(
    (0, "ARECA-SAS-CARD1-MIB", "hwEnclosure04VolIndex"),
)
if mibBuilder.loadTexts:
    hwEnclosure04VolEntry.setStatus("mandatory")
_HwEnclosure04VolIndex_Type = Integer32
_HwEnclosure04VolIndex_Object = MibTableColumn
hwEnclosure04VolIndex = _HwEnclosure04VolIndex_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 5, 8, 1, 1),
    _HwEnclosure04VolIndex_Type()
)
hwEnclosure04VolIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEnclosure04VolIndex.setStatus("mandatory")
_HwEnclosure04VolDesc_Type = OctetString
_HwEnclosure04VolDesc_Object = MibTableColumn
hwEnclosure04VolDesc = _HwEnclosure04VolDesc_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 5, 8, 1, 2),
    _HwEnclosure04VolDesc_Type()
)
hwEnclosure04VolDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEnclosure04VolDesc.setStatus("mandatory")
_HwEnclosure04VolValue_Type = Integer32
_HwEnclosure04VolValue_Object = MibTableColumn
hwEnclosure04VolValue = _HwEnclosure04VolValue_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 5, 8, 1, 3),
    _HwEnclosure04VolValue_Type()
)
hwEnclosure04VolValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEnclosure04VolValue.setStatus("mandatory")
_HwEnclosure04FanTable_Object = MibTable
hwEnclosure04FanTable = _HwEnclosure04FanTable_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 5, 9)
)
if mibBuilder.loadTexts:
    hwEnclosure04FanTable.setStatus("mandatory")
_HwEnclosure04FanEntry_Object = MibTableRow
hwEnclosure04FanEntry = _HwEnclosure04FanEntry_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 5, 9, 1)
)
hwEnclosure04FanEntry.setIndexNames(
    (0, "ARECA-SAS-CARD1-MIB", "hwEnclosure04FanIndex"),
)
if mibBuilder.loadTexts:
    hwEnclosure04FanEntry.setStatus("mandatory")
_HwEnclosure04FanIndex_Type = Integer32
_HwEnclosure04FanIndex_Object = MibTableColumn
hwEnclosure04FanIndex = _HwEnclosure04FanIndex_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 5, 9, 1, 1),
    _HwEnclosure04FanIndex_Type()
)
hwEnclosure04FanIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEnclosure04FanIndex.setStatus("mandatory")
_HwEnclosure04FanDesc_Type = OctetString
_HwEnclosure04FanDesc_Object = MibTableColumn
hwEnclosure04FanDesc = _HwEnclosure04FanDesc_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 5, 9, 1, 2),
    _HwEnclosure04FanDesc_Type()
)
hwEnclosure04FanDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEnclosure04FanDesc.setStatus("mandatory")
_HwEnclosure04FanSpeed_Type = Integer32
_HwEnclosure04FanSpeed_Object = MibTableColumn
hwEnclosure04FanSpeed = _HwEnclosure04FanSpeed_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 5, 9, 1, 3),
    _HwEnclosure04FanSpeed_Type()
)
hwEnclosure04FanSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEnclosure04FanSpeed.setStatus("mandatory")
_HwEnclosure04TempTable_Object = MibTable
hwEnclosure04TempTable = _HwEnclosure04TempTable_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 5, 10)
)
if mibBuilder.loadTexts:
    hwEnclosure04TempTable.setStatus("mandatory")
_HwEnclosure04TempEntry_Object = MibTableRow
hwEnclosure04TempEntry = _HwEnclosure04TempEntry_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 5, 10, 1)
)
hwEnclosure04TempEntry.setIndexNames(
    (0, "ARECA-SAS-CARD1-MIB", "hwEnclosure04TempIndex"),
)
if mibBuilder.loadTexts:
    hwEnclosure04TempEntry.setStatus("mandatory")
_HwEnclosure04TempIndex_Type = Integer32
_HwEnclosure04TempIndex_Object = MibTableColumn
hwEnclosure04TempIndex = _HwEnclosure04TempIndex_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 5, 10, 1, 1),
    _HwEnclosure04TempIndex_Type()
)
hwEnclosure04TempIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEnclosure04TempIndex.setStatus("mandatory")
_HwEnclosure04TempDesc_Type = OctetString
_HwEnclosure04TempDesc_Object = MibTableColumn
hwEnclosure04TempDesc = _HwEnclosure04TempDesc_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 5, 10, 1, 2),
    _HwEnclosure04TempDesc_Type()
)
hwEnclosure04TempDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEnclosure04TempDesc.setStatus("mandatory")
_HwEnclosure04TempValue_Type = Integer32
_HwEnclosure04TempValue_Object = MibTableColumn
hwEnclosure04TempValue = _HwEnclosure04TempValue_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 5, 10, 1, 3),
    _HwEnclosure04TempValue_Type()
)
hwEnclosure04TempValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEnclosure04TempValue.setStatus("mandatory")
_HwEnclosure5_ObjectIdentity = ObjectIdentity
hwEnclosure5 = _HwEnclosure5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 6)
)
_HwEnclosure05Installed_Type = Integer32
_HwEnclosure05Installed_Object = MibScalar
hwEnclosure05Installed = _HwEnclosure05Installed_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 6, 1),
    _HwEnclosure05Installed_Type()
)
hwEnclosure05Installed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEnclosure05Installed.setStatus("mandatory")
_HwEnclosure05Description_Type = OctetString
_HwEnclosure05Description_Object = MibScalar
hwEnclosure05Description = _HwEnclosure05Description_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 6, 2),
    _HwEnclosure05Description_Type()
)
hwEnclosure05Description.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEnclosure05Description.setStatus("mandatory")
_HwEnclosure05NumberOfPower_Type = Integer32
_HwEnclosure05NumberOfPower_Object = MibScalar
hwEnclosure05NumberOfPower = _HwEnclosure05NumberOfPower_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 6, 3),
    _HwEnclosure05NumberOfPower_Type()
)
hwEnclosure05NumberOfPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEnclosure05NumberOfPower.setStatus("mandatory")
_HwEnclosure05NumberOfVol_Type = Integer32
_HwEnclosure05NumberOfVol_Object = MibScalar
hwEnclosure05NumberOfVol = _HwEnclosure05NumberOfVol_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 6, 4),
    _HwEnclosure05NumberOfVol_Type()
)
hwEnclosure05NumberOfVol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEnclosure05NumberOfVol.setStatus("mandatory")
_HwEnclosure05NumberOfFan_Type = Integer32
_HwEnclosure05NumberOfFan_Object = MibScalar
hwEnclosure05NumberOfFan = _HwEnclosure05NumberOfFan_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 6, 5),
    _HwEnclosure05NumberOfFan_Type()
)
hwEnclosure05NumberOfFan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEnclosure05NumberOfFan.setStatus("mandatory")
_HwEnclosure05NumberOfTemp_Type = Integer32
_HwEnclosure05NumberOfTemp_Object = MibScalar
hwEnclosure05NumberOfTemp = _HwEnclosure05NumberOfTemp_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 6, 6),
    _HwEnclosure05NumberOfTemp_Type()
)
hwEnclosure05NumberOfTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEnclosure05NumberOfTemp.setStatus("mandatory")
_HwEnclosure05PowerTable_Object = MibTable
hwEnclosure05PowerTable = _HwEnclosure05PowerTable_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 6, 7)
)
if mibBuilder.loadTexts:
    hwEnclosure05PowerTable.setStatus("mandatory")
_HwEnclosure05PowerEntry_Object = MibTableRow
hwEnclosure05PowerEntry = _HwEnclosure05PowerEntry_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 6, 7, 1)
)
hwEnclosure05PowerEntry.setIndexNames(
    (0, "ARECA-SAS-CARD1-MIB", "hwEnclosure05PowerIndex"),
)
if mibBuilder.loadTexts:
    hwEnclosure05PowerEntry.setStatus("mandatory")
_HwEnclosure05PowerIndex_Type = Integer32
_HwEnclosure05PowerIndex_Object = MibTableColumn
hwEnclosure05PowerIndex = _HwEnclosure05PowerIndex_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 6, 7, 1, 1),
    _HwEnclosure05PowerIndex_Type()
)
hwEnclosure05PowerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEnclosure05PowerIndex.setStatus("mandatory")
_HwEnclosure05PowerDesc_Type = OctetString
_HwEnclosure05PowerDesc_Object = MibTableColumn
hwEnclosure05PowerDesc = _HwEnclosure05PowerDesc_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 6, 7, 1, 2),
    _HwEnclosure05PowerDesc_Type()
)
hwEnclosure05PowerDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEnclosure05PowerDesc.setStatus("mandatory")


class _HwEnclosure05PowerState_Type(Integer32):
    """Custom type hwEnclosure05PowerState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("failed", 0),
          ("ok", 1))
    )


_HwEnclosure05PowerState_Type.__name__ = "Integer32"
_HwEnclosure05PowerState_Object = MibTableColumn
hwEnclosure05PowerState = _HwEnclosure05PowerState_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 6, 7, 1, 3),
    _HwEnclosure05PowerState_Type()
)
hwEnclosure05PowerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEnclosure05PowerState.setStatus("mandatory")
_HwEnclosure05VolTable_Object = MibTable
hwEnclosure05VolTable = _HwEnclosure05VolTable_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 6, 8)
)
if mibBuilder.loadTexts:
    hwEnclosure05VolTable.setStatus("mandatory")
_HwEnclosure05VolEntry_Object = MibTableRow
hwEnclosure05VolEntry = _HwEnclosure05VolEntry_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 6, 8, 1)
)
hwEnclosure05VolEntry.setIndexNames(
    (0, "ARECA-SAS-CARD1-MIB", "hwEnclosure05VolIndex"),
)
if mibBuilder.loadTexts:
    hwEnclosure05VolEntry.setStatus("mandatory")
_HwEnclosure05VolIndex_Type = Integer32
_HwEnclosure05VolIndex_Object = MibTableColumn
hwEnclosure05VolIndex = _HwEnclosure05VolIndex_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 6, 8, 1, 1),
    _HwEnclosure05VolIndex_Type()
)
hwEnclosure05VolIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEnclosure05VolIndex.setStatus("mandatory")
_HwEnclosure05VolDesc_Type = OctetString
_HwEnclosure05VolDesc_Object = MibTableColumn
hwEnclosure05VolDesc = _HwEnclosure05VolDesc_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 6, 8, 1, 2),
    _HwEnclosure05VolDesc_Type()
)
hwEnclosure05VolDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEnclosure05VolDesc.setStatus("mandatory")
_HwEnclosure05VolValue_Type = Integer32
_HwEnclosure05VolValue_Object = MibTableColumn
hwEnclosure05VolValue = _HwEnclosure05VolValue_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 6, 8, 1, 3),
    _HwEnclosure05VolValue_Type()
)
hwEnclosure05VolValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEnclosure05VolValue.setStatus("mandatory")
_HwEnclosure05FanTable_Object = MibTable
hwEnclosure05FanTable = _HwEnclosure05FanTable_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 6, 9)
)
if mibBuilder.loadTexts:
    hwEnclosure05FanTable.setStatus("mandatory")
_HwEnclosure05FanEntry_Object = MibTableRow
hwEnclosure05FanEntry = _HwEnclosure05FanEntry_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 6, 9, 1)
)
hwEnclosure05FanEntry.setIndexNames(
    (0, "ARECA-SAS-CARD1-MIB", "hwEnclosure05FanIndex"),
)
if mibBuilder.loadTexts:
    hwEnclosure05FanEntry.setStatus("mandatory")
_HwEnclosure05FanIndex_Type = Integer32
_HwEnclosure05FanIndex_Object = MibTableColumn
hwEnclosure05FanIndex = _HwEnclosure05FanIndex_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 6, 9, 1, 1),
    _HwEnclosure05FanIndex_Type()
)
hwEnclosure05FanIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEnclosure05FanIndex.setStatus("mandatory")
_HwEnclosure05FanDesc_Type = OctetString
_HwEnclosure05FanDesc_Object = MibTableColumn
hwEnclosure05FanDesc = _HwEnclosure05FanDesc_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 6, 9, 1, 2),
    _HwEnclosure05FanDesc_Type()
)
hwEnclosure05FanDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEnclosure05FanDesc.setStatus("mandatory")
_HwEnclosure05FanSpeed_Type = Integer32
_HwEnclosure05FanSpeed_Object = MibTableColumn
hwEnclosure05FanSpeed = _HwEnclosure05FanSpeed_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 6, 9, 1, 3),
    _HwEnclosure05FanSpeed_Type()
)
hwEnclosure05FanSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEnclosure05FanSpeed.setStatus("mandatory")
_HwEnclosure05TempTable_Object = MibTable
hwEnclosure05TempTable = _HwEnclosure05TempTable_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 6, 10)
)
if mibBuilder.loadTexts:
    hwEnclosure05TempTable.setStatus("mandatory")
_HwEnclosure05TempEntry_Object = MibTableRow
hwEnclosure05TempEntry = _HwEnclosure05TempEntry_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 6, 10, 1)
)
hwEnclosure05TempEntry.setIndexNames(
    (0, "ARECA-SAS-CARD1-MIB", "hwEnclosure05TempIndex"),
)
if mibBuilder.loadTexts:
    hwEnclosure05TempEntry.setStatus("mandatory")
_HwEnclosure05TempIndex_Type = Integer32
_HwEnclosure05TempIndex_Object = MibTableColumn
hwEnclosure05TempIndex = _HwEnclosure05TempIndex_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 6, 10, 1, 1),
    _HwEnclosure05TempIndex_Type()
)
hwEnclosure05TempIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEnclosure05TempIndex.setStatus("mandatory")
_HwEnclosure05TempDesc_Type = OctetString
_HwEnclosure05TempDesc_Object = MibTableColumn
hwEnclosure05TempDesc = _HwEnclosure05TempDesc_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 6, 10, 1, 2),
    _HwEnclosure05TempDesc_Type()
)
hwEnclosure05TempDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEnclosure05TempDesc.setStatus("mandatory")
_HwEnclosure05TempValue_Type = Integer32
_HwEnclosure05TempValue_Object = MibTableColumn
hwEnclosure05TempValue = _HwEnclosure05TempValue_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 6, 10, 1, 3),
    _HwEnclosure05TempValue_Type()
)
hwEnclosure05TempValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEnclosure05TempValue.setStatus("mandatory")
_HwEnclosure6_ObjectIdentity = ObjectIdentity
hwEnclosure6 = _HwEnclosure6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 7)
)
_HwEnclosure06Installed_Type = Integer32
_HwEnclosure06Installed_Object = MibScalar
hwEnclosure06Installed = _HwEnclosure06Installed_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 7, 1),
    _HwEnclosure06Installed_Type()
)
hwEnclosure06Installed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEnclosure06Installed.setStatus("mandatory")
_HwEnclosure06Description_Type = OctetString
_HwEnclosure06Description_Object = MibScalar
hwEnclosure06Description = _HwEnclosure06Description_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 7, 2),
    _HwEnclosure06Description_Type()
)
hwEnclosure06Description.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEnclosure06Description.setStatus("mandatory")
_HwEnclosure06NumberOfPower_Type = Integer32
_HwEnclosure06NumberOfPower_Object = MibScalar
hwEnclosure06NumberOfPower = _HwEnclosure06NumberOfPower_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 7, 3),
    _HwEnclosure06NumberOfPower_Type()
)
hwEnclosure06NumberOfPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEnclosure06NumberOfPower.setStatus("mandatory")
_HwEnclosure06NumberOfVol_Type = Integer32
_HwEnclosure06NumberOfVol_Object = MibScalar
hwEnclosure06NumberOfVol = _HwEnclosure06NumberOfVol_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 7, 4),
    _HwEnclosure06NumberOfVol_Type()
)
hwEnclosure06NumberOfVol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEnclosure06NumberOfVol.setStatus("mandatory")
_HwEnclosure06NumberOfFan_Type = Integer32
_HwEnclosure06NumberOfFan_Object = MibScalar
hwEnclosure06NumberOfFan = _HwEnclosure06NumberOfFan_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 7, 5),
    _HwEnclosure06NumberOfFan_Type()
)
hwEnclosure06NumberOfFan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEnclosure06NumberOfFan.setStatus("mandatory")
_HwEnclosure06NumberOfTemp_Type = Integer32
_HwEnclosure06NumberOfTemp_Object = MibScalar
hwEnclosure06NumberOfTemp = _HwEnclosure06NumberOfTemp_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 7, 6),
    _HwEnclosure06NumberOfTemp_Type()
)
hwEnclosure06NumberOfTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEnclosure06NumberOfTemp.setStatus("mandatory")
_HwEnclosure06PowerTable_Object = MibTable
hwEnclosure06PowerTable = _HwEnclosure06PowerTable_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 7, 7)
)
if mibBuilder.loadTexts:
    hwEnclosure06PowerTable.setStatus("mandatory")
_HwEnclosure06PowerEntry_Object = MibTableRow
hwEnclosure06PowerEntry = _HwEnclosure06PowerEntry_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 7, 7, 1)
)
hwEnclosure06PowerEntry.setIndexNames(
    (0, "ARECA-SAS-CARD1-MIB", "hwEnclosure06PowerIndex"),
)
if mibBuilder.loadTexts:
    hwEnclosure06PowerEntry.setStatus("mandatory")
_HwEnclosure06PowerIndex_Type = Integer32
_HwEnclosure06PowerIndex_Object = MibTableColumn
hwEnclosure06PowerIndex = _HwEnclosure06PowerIndex_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 7, 7, 1, 1),
    _HwEnclosure06PowerIndex_Type()
)
hwEnclosure06PowerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEnclosure06PowerIndex.setStatus("mandatory")
_HwEnclosure06PowerDesc_Type = OctetString
_HwEnclosure06PowerDesc_Object = MibTableColumn
hwEnclosure06PowerDesc = _HwEnclosure06PowerDesc_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 7, 7, 1, 2),
    _HwEnclosure06PowerDesc_Type()
)
hwEnclosure06PowerDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEnclosure06PowerDesc.setStatus("mandatory")


class _HwEnclosure06PowerState_Type(Integer32):
    """Custom type hwEnclosure06PowerState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("failed", 0),
          ("ok", 1))
    )


_HwEnclosure06PowerState_Type.__name__ = "Integer32"
_HwEnclosure06PowerState_Object = MibTableColumn
hwEnclosure06PowerState = _HwEnclosure06PowerState_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 7, 7, 1, 3),
    _HwEnclosure06PowerState_Type()
)
hwEnclosure06PowerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEnclosure06PowerState.setStatus("mandatory")
_HwEnclosure06VolTable_Object = MibTable
hwEnclosure06VolTable = _HwEnclosure06VolTable_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 7, 8)
)
if mibBuilder.loadTexts:
    hwEnclosure06VolTable.setStatus("mandatory")
_HwEnclosure06VolEntry_Object = MibTableRow
hwEnclosure06VolEntry = _HwEnclosure06VolEntry_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 7, 8, 1)
)
hwEnclosure06VolEntry.setIndexNames(
    (0, "ARECA-SAS-CARD1-MIB", "hwEnclosure06VolIndex"),
)
if mibBuilder.loadTexts:
    hwEnclosure06VolEntry.setStatus("mandatory")
_HwEnclosure06VolIndex_Type = Integer32
_HwEnclosure06VolIndex_Object = MibTableColumn
hwEnclosure06VolIndex = _HwEnclosure06VolIndex_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 7, 8, 1, 1),
    _HwEnclosure06VolIndex_Type()
)
hwEnclosure06VolIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEnclosure06VolIndex.setStatus("mandatory")
_HwEnclosure06VolDesc_Type = OctetString
_HwEnclosure06VolDesc_Object = MibTableColumn
hwEnclosure06VolDesc = _HwEnclosure06VolDesc_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 7, 8, 1, 2),
    _HwEnclosure06VolDesc_Type()
)
hwEnclosure06VolDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEnclosure06VolDesc.setStatus("mandatory")
_HwEnclosure06VolValue_Type = Integer32
_HwEnclosure06VolValue_Object = MibTableColumn
hwEnclosure06VolValue = _HwEnclosure06VolValue_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 7, 8, 1, 3),
    _HwEnclosure06VolValue_Type()
)
hwEnclosure06VolValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEnclosure06VolValue.setStatus("mandatory")
_HwEnclosure06FanTable_Object = MibTable
hwEnclosure06FanTable = _HwEnclosure06FanTable_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 7, 9)
)
if mibBuilder.loadTexts:
    hwEnclosure06FanTable.setStatus("mandatory")
_HwEnclosure06FanEntry_Object = MibTableRow
hwEnclosure06FanEntry = _HwEnclosure06FanEntry_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 7, 9, 1)
)
hwEnclosure06FanEntry.setIndexNames(
    (0, "ARECA-SAS-CARD1-MIB", "hwEnclosure06FanIndex"),
)
if mibBuilder.loadTexts:
    hwEnclosure06FanEntry.setStatus("mandatory")
_HwEnclosure06FanIndex_Type = Integer32
_HwEnclosure06FanIndex_Object = MibTableColumn
hwEnclosure06FanIndex = _HwEnclosure06FanIndex_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 7, 9, 1, 1),
    _HwEnclosure06FanIndex_Type()
)
hwEnclosure06FanIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEnclosure06FanIndex.setStatus("mandatory")
_HwEnclosure06FanDesc_Type = OctetString
_HwEnclosure06FanDesc_Object = MibTableColumn
hwEnclosure06FanDesc = _HwEnclosure06FanDesc_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 7, 9, 1, 2),
    _HwEnclosure06FanDesc_Type()
)
hwEnclosure06FanDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEnclosure06FanDesc.setStatus("mandatory")
_HwEnclosure06FanSpeed_Type = Integer32
_HwEnclosure06FanSpeed_Object = MibTableColumn
hwEnclosure06FanSpeed = _HwEnclosure06FanSpeed_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 7, 9, 1, 3),
    _HwEnclosure06FanSpeed_Type()
)
hwEnclosure06FanSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEnclosure06FanSpeed.setStatus("mandatory")
_HwEnclosure06TempTable_Object = MibTable
hwEnclosure06TempTable = _HwEnclosure06TempTable_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 7, 10)
)
if mibBuilder.loadTexts:
    hwEnclosure06TempTable.setStatus("mandatory")
_HwEnclosure06TempEntry_Object = MibTableRow
hwEnclosure06TempEntry = _HwEnclosure06TempEntry_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 7, 10, 1)
)
hwEnclosure06TempEntry.setIndexNames(
    (0, "ARECA-SAS-CARD1-MIB", "hwEnclosure06TempIndex"),
)
if mibBuilder.loadTexts:
    hwEnclosure06TempEntry.setStatus("mandatory")
_HwEnclosure06TempIndex_Type = Integer32
_HwEnclosure06TempIndex_Object = MibTableColumn
hwEnclosure06TempIndex = _HwEnclosure06TempIndex_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 7, 10, 1, 1),
    _HwEnclosure06TempIndex_Type()
)
hwEnclosure06TempIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEnclosure06TempIndex.setStatus("mandatory")
_HwEnclosure06TempDesc_Type = OctetString
_HwEnclosure06TempDesc_Object = MibTableColumn
hwEnclosure06TempDesc = _HwEnclosure06TempDesc_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 7, 10, 1, 2),
    _HwEnclosure06TempDesc_Type()
)
hwEnclosure06TempDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEnclosure06TempDesc.setStatus("mandatory")
_HwEnclosure06TempValue_Type = Integer32
_HwEnclosure06TempValue_Object = MibTableColumn
hwEnclosure06TempValue = _HwEnclosure06TempValue_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 7, 10, 1, 3),
    _HwEnclosure06TempValue_Type()
)
hwEnclosure06TempValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEnclosure06TempValue.setStatus("mandatory")
_HwEnclosure7_ObjectIdentity = ObjectIdentity
hwEnclosure7 = _HwEnclosure7_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 8)
)
_HwEnclosure07Installed_Type = Integer32
_HwEnclosure07Installed_Object = MibScalar
hwEnclosure07Installed = _HwEnclosure07Installed_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 8, 1),
    _HwEnclosure07Installed_Type()
)
hwEnclosure07Installed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEnclosure07Installed.setStatus("mandatory")
_HwEnclosure07Description_Type = OctetString
_HwEnclosure07Description_Object = MibScalar
hwEnclosure07Description = _HwEnclosure07Description_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 8, 2),
    _HwEnclosure07Description_Type()
)
hwEnclosure07Description.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEnclosure07Description.setStatus("mandatory")
_HwEnclosure07NumberOfPower_Type = Integer32
_HwEnclosure07NumberOfPower_Object = MibScalar
hwEnclosure07NumberOfPower = _HwEnclosure07NumberOfPower_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 8, 3),
    _HwEnclosure07NumberOfPower_Type()
)
hwEnclosure07NumberOfPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEnclosure07NumberOfPower.setStatus("mandatory")
_HwEnclosure07NumberOfVol_Type = Integer32
_HwEnclosure07NumberOfVol_Object = MibScalar
hwEnclosure07NumberOfVol = _HwEnclosure07NumberOfVol_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 8, 4),
    _HwEnclosure07NumberOfVol_Type()
)
hwEnclosure07NumberOfVol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEnclosure07NumberOfVol.setStatus("mandatory")
_HwEnclosure07NumberOfFan_Type = Integer32
_HwEnclosure07NumberOfFan_Object = MibScalar
hwEnclosure07NumberOfFan = _HwEnclosure07NumberOfFan_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 8, 5),
    _HwEnclosure07NumberOfFan_Type()
)
hwEnclosure07NumberOfFan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEnclosure07NumberOfFan.setStatus("mandatory")
_HwEnclosure07NumberOfTemp_Type = Integer32
_HwEnclosure07NumberOfTemp_Object = MibScalar
hwEnclosure07NumberOfTemp = _HwEnclosure07NumberOfTemp_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 8, 6),
    _HwEnclosure07NumberOfTemp_Type()
)
hwEnclosure07NumberOfTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEnclosure07NumberOfTemp.setStatus("mandatory")
_HwEnclosure07PowerTable_Object = MibTable
hwEnclosure07PowerTable = _HwEnclosure07PowerTable_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 8, 7)
)
if mibBuilder.loadTexts:
    hwEnclosure07PowerTable.setStatus("mandatory")
_HwEnclosure07PowerEntry_Object = MibTableRow
hwEnclosure07PowerEntry = _HwEnclosure07PowerEntry_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 8, 7, 1)
)
hwEnclosure07PowerEntry.setIndexNames(
    (0, "ARECA-SAS-CARD1-MIB", "hwEnclosure07PowerIndex"),
)
if mibBuilder.loadTexts:
    hwEnclosure07PowerEntry.setStatus("mandatory")
_HwEnclosure07PowerIndex_Type = Integer32
_HwEnclosure07PowerIndex_Object = MibTableColumn
hwEnclosure07PowerIndex = _HwEnclosure07PowerIndex_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 8, 7, 1, 1),
    _HwEnclosure07PowerIndex_Type()
)
hwEnclosure07PowerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEnclosure07PowerIndex.setStatus("mandatory")
_HwEnclosure07PowerDesc_Type = OctetString
_HwEnclosure07PowerDesc_Object = MibTableColumn
hwEnclosure07PowerDesc = _HwEnclosure07PowerDesc_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 8, 7, 1, 2),
    _HwEnclosure07PowerDesc_Type()
)
hwEnclosure07PowerDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEnclosure07PowerDesc.setStatus("mandatory")


class _HwEnclosure07PowerState_Type(Integer32):
    """Custom type hwEnclosure07PowerState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("failed", 0),
          ("ok", 1))
    )


_HwEnclosure07PowerState_Type.__name__ = "Integer32"
_HwEnclosure07PowerState_Object = MibTableColumn
hwEnclosure07PowerState = _HwEnclosure07PowerState_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 8, 7, 1, 3),
    _HwEnclosure07PowerState_Type()
)
hwEnclosure07PowerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEnclosure07PowerState.setStatus("mandatory")
_HwEnclosure07VolTable_Object = MibTable
hwEnclosure07VolTable = _HwEnclosure07VolTable_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 8, 8)
)
if mibBuilder.loadTexts:
    hwEnclosure07VolTable.setStatus("mandatory")
_HwEnclosure07VolEntry_Object = MibTableRow
hwEnclosure07VolEntry = _HwEnclosure07VolEntry_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 8, 8, 1)
)
hwEnclosure07VolEntry.setIndexNames(
    (0, "ARECA-SAS-CARD1-MIB", "hwEnclosure07VolIndex"),
)
if mibBuilder.loadTexts:
    hwEnclosure07VolEntry.setStatus("mandatory")
_HwEnclosure07VolIndex_Type = Integer32
_HwEnclosure07VolIndex_Object = MibTableColumn
hwEnclosure07VolIndex = _HwEnclosure07VolIndex_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 8, 8, 1, 1),
    _HwEnclosure07VolIndex_Type()
)
hwEnclosure07VolIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEnclosure07VolIndex.setStatus("mandatory")
_HwEnclosure07VolDesc_Type = OctetString
_HwEnclosure07VolDesc_Object = MibTableColumn
hwEnclosure07VolDesc = _HwEnclosure07VolDesc_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 8, 8, 1, 2),
    _HwEnclosure07VolDesc_Type()
)
hwEnclosure07VolDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEnclosure07VolDesc.setStatus("mandatory")
_HwEnclosure07VolValue_Type = Integer32
_HwEnclosure07VolValue_Object = MibTableColumn
hwEnclosure07VolValue = _HwEnclosure07VolValue_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 8, 8, 1, 3),
    _HwEnclosure07VolValue_Type()
)
hwEnclosure07VolValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEnclosure07VolValue.setStatus("mandatory")
_HwEnclosure07FanTable_Object = MibTable
hwEnclosure07FanTable = _HwEnclosure07FanTable_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 8, 9)
)
if mibBuilder.loadTexts:
    hwEnclosure07FanTable.setStatus("mandatory")
_HwEnclosure07FanEntry_Object = MibTableRow
hwEnclosure07FanEntry = _HwEnclosure07FanEntry_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 8, 9, 1)
)
hwEnclosure07FanEntry.setIndexNames(
    (0, "ARECA-SAS-CARD1-MIB", "hwEnclosure07FanIndex"),
)
if mibBuilder.loadTexts:
    hwEnclosure07FanEntry.setStatus("mandatory")
_HwEnclosure07FanIndex_Type = Integer32
_HwEnclosure07FanIndex_Object = MibTableColumn
hwEnclosure07FanIndex = _HwEnclosure07FanIndex_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 8, 9, 1, 1),
    _HwEnclosure07FanIndex_Type()
)
hwEnclosure07FanIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEnclosure07FanIndex.setStatus("mandatory")
_HwEnclosure07FanDesc_Type = OctetString
_HwEnclosure07FanDesc_Object = MibTableColumn
hwEnclosure07FanDesc = _HwEnclosure07FanDesc_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 8, 9, 1, 2),
    _HwEnclosure07FanDesc_Type()
)
hwEnclosure07FanDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEnclosure07FanDesc.setStatus("mandatory")
_HwEnclosure07FanSpeed_Type = Integer32
_HwEnclosure07FanSpeed_Object = MibTableColumn
hwEnclosure07FanSpeed = _HwEnclosure07FanSpeed_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 8, 9, 1, 3),
    _HwEnclosure07FanSpeed_Type()
)
hwEnclosure07FanSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEnclosure07FanSpeed.setStatus("mandatory")
_HwEnclosure07TempTable_Object = MibTable
hwEnclosure07TempTable = _HwEnclosure07TempTable_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 8, 10)
)
if mibBuilder.loadTexts:
    hwEnclosure07TempTable.setStatus("mandatory")
_HwEnclosure07TempEntry_Object = MibTableRow
hwEnclosure07TempEntry = _HwEnclosure07TempEntry_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 8, 10, 1)
)
hwEnclosure07TempEntry.setIndexNames(
    (0, "ARECA-SAS-CARD1-MIB", "hwEnclosure07TempIndex"),
)
if mibBuilder.loadTexts:
    hwEnclosure07TempEntry.setStatus("mandatory")
_HwEnclosure07TempIndex_Type = Integer32
_HwEnclosure07TempIndex_Object = MibTableColumn
hwEnclosure07TempIndex = _HwEnclosure07TempIndex_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 8, 10, 1, 1),
    _HwEnclosure07TempIndex_Type()
)
hwEnclosure07TempIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEnclosure07TempIndex.setStatus("mandatory")
_HwEnclosure07TempDesc_Type = OctetString
_HwEnclosure07TempDesc_Object = MibTableColumn
hwEnclosure07TempDesc = _HwEnclosure07TempDesc_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 8, 10, 1, 2),
    _HwEnclosure07TempDesc_Type()
)
hwEnclosure07TempDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEnclosure07TempDesc.setStatus("mandatory")
_HwEnclosure07TempValue_Type = Integer32
_HwEnclosure07TempValue_Object = MibTableColumn
hwEnclosure07TempValue = _HwEnclosure07TempValue_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 8, 10, 1, 3),
    _HwEnclosure07TempValue_Type()
)
hwEnclosure07TempValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEnclosure07TempValue.setStatus("mandatory")
_HwEnclosure8_ObjectIdentity = ObjectIdentity
hwEnclosure8 = _HwEnclosure8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 9)
)
_HwEnclosure08Installed_Type = Integer32
_HwEnclosure08Installed_Object = MibScalar
hwEnclosure08Installed = _HwEnclosure08Installed_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 9, 1),
    _HwEnclosure08Installed_Type()
)
hwEnclosure08Installed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEnclosure08Installed.setStatus("mandatory")
_HwEnclosure08Description_Type = OctetString
_HwEnclosure08Description_Object = MibScalar
hwEnclosure08Description = _HwEnclosure08Description_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 9, 2),
    _HwEnclosure08Description_Type()
)
hwEnclosure08Description.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEnclosure08Description.setStatus("mandatory")
_HwEnclosure08NumberOfPower_Type = Integer32
_HwEnclosure08NumberOfPower_Object = MibScalar
hwEnclosure08NumberOfPower = _HwEnclosure08NumberOfPower_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 9, 3),
    _HwEnclosure08NumberOfPower_Type()
)
hwEnclosure08NumberOfPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEnclosure08NumberOfPower.setStatus("mandatory")
_HwEnclosure08NumberOfVol_Type = Integer32
_HwEnclosure08NumberOfVol_Object = MibScalar
hwEnclosure08NumberOfVol = _HwEnclosure08NumberOfVol_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 9, 4),
    _HwEnclosure08NumberOfVol_Type()
)
hwEnclosure08NumberOfVol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEnclosure08NumberOfVol.setStatus("mandatory")
_HwEnclosure08NumberOfFan_Type = Integer32
_HwEnclosure08NumberOfFan_Object = MibScalar
hwEnclosure08NumberOfFan = _HwEnclosure08NumberOfFan_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 9, 5),
    _HwEnclosure08NumberOfFan_Type()
)
hwEnclosure08NumberOfFan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEnclosure08NumberOfFan.setStatus("mandatory")
_HwEnclosure08NumberOfTemp_Type = Integer32
_HwEnclosure08NumberOfTemp_Object = MibScalar
hwEnclosure08NumberOfTemp = _HwEnclosure08NumberOfTemp_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 9, 6),
    _HwEnclosure08NumberOfTemp_Type()
)
hwEnclosure08NumberOfTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEnclosure08NumberOfTemp.setStatus("mandatory")
_HwEnclosure08PowerTable_Object = MibTable
hwEnclosure08PowerTable = _HwEnclosure08PowerTable_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 9, 7)
)
if mibBuilder.loadTexts:
    hwEnclosure08PowerTable.setStatus("mandatory")
_HwEnclosure08PowerEntry_Object = MibTableRow
hwEnclosure08PowerEntry = _HwEnclosure08PowerEntry_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 9, 7, 1)
)
hwEnclosure08PowerEntry.setIndexNames(
    (0, "ARECA-SAS-CARD1-MIB", "hwEnclosure08PowerIndex"),
)
if mibBuilder.loadTexts:
    hwEnclosure08PowerEntry.setStatus("mandatory")
_HwEnclosure08PowerIndex_Type = Integer32
_HwEnclosure08PowerIndex_Object = MibTableColumn
hwEnclosure08PowerIndex = _HwEnclosure08PowerIndex_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 9, 7, 1, 1),
    _HwEnclosure08PowerIndex_Type()
)
hwEnclosure08PowerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEnclosure08PowerIndex.setStatus("mandatory")
_HwEnclosure08PowerDesc_Type = OctetString
_HwEnclosure08PowerDesc_Object = MibTableColumn
hwEnclosure08PowerDesc = _HwEnclosure08PowerDesc_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 9, 7, 1, 2),
    _HwEnclosure08PowerDesc_Type()
)
hwEnclosure08PowerDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEnclosure08PowerDesc.setStatus("mandatory")


class _HwEnclosure08PowerState_Type(Integer32):
    """Custom type hwEnclosure08PowerState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("failed", 0),
          ("ok", 1))
    )


_HwEnclosure08PowerState_Type.__name__ = "Integer32"
_HwEnclosure08PowerState_Object = MibTableColumn
hwEnclosure08PowerState = _HwEnclosure08PowerState_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 9, 7, 1, 3),
    _HwEnclosure08PowerState_Type()
)
hwEnclosure08PowerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEnclosure08PowerState.setStatus("mandatory")
_HwEnclosure08VolTable_Object = MibTable
hwEnclosure08VolTable = _HwEnclosure08VolTable_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 9, 8)
)
if mibBuilder.loadTexts:
    hwEnclosure08VolTable.setStatus("mandatory")
_HwEnclosure08VolEntry_Object = MibTableRow
hwEnclosure08VolEntry = _HwEnclosure08VolEntry_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 9, 8, 1)
)
hwEnclosure08VolEntry.setIndexNames(
    (0, "ARECA-SAS-CARD1-MIB", "hwEnclosure08VolIndex"),
)
if mibBuilder.loadTexts:
    hwEnclosure08VolEntry.setStatus("mandatory")
_HwEnclosure08VolIndex_Type = Integer32
_HwEnclosure08VolIndex_Object = MibTableColumn
hwEnclosure08VolIndex = _HwEnclosure08VolIndex_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 9, 8, 1, 1),
    _HwEnclosure08VolIndex_Type()
)
hwEnclosure08VolIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEnclosure08VolIndex.setStatus("mandatory")
_HwEnclosure08VolDesc_Type = OctetString
_HwEnclosure08VolDesc_Object = MibTableColumn
hwEnclosure08VolDesc = _HwEnclosure08VolDesc_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 9, 8, 1, 2),
    _HwEnclosure08VolDesc_Type()
)
hwEnclosure08VolDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEnclosure08VolDesc.setStatus("mandatory")
_HwEnclosure08VolValue_Type = Integer32
_HwEnclosure08VolValue_Object = MibTableColumn
hwEnclosure08VolValue = _HwEnclosure08VolValue_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 9, 8, 1, 3),
    _HwEnclosure08VolValue_Type()
)
hwEnclosure08VolValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEnclosure08VolValue.setStatus("mandatory")
_HwEnclosure08FanTable_Object = MibTable
hwEnclosure08FanTable = _HwEnclosure08FanTable_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 9, 9)
)
if mibBuilder.loadTexts:
    hwEnclosure08FanTable.setStatus("mandatory")
_HwEnclosure08FanEntry_Object = MibTableRow
hwEnclosure08FanEntry = _HwEnclosure08FanEntry_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 9, 9, 1)
)
hwEnclosure08FanEntry.setIndexNames(
    (0, "ARECA-SAS-CARD1-MIB", "hwEnclosure08FanIndex"),
)
if mibBuilder.loadTexts:
    hwEnclosure08FanEntry.setStatus("mandatory")
_HwEnclosure08FanIndex_Type = Integer32
_HwEnclosure08FanIndex_Object = MibTableColumn
hwEnclosure08FanIndex = _HwEnclosure08FanIndex_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 9, 9, 1, 1),
    _HwEnclosure08FanIndex_Type()
)
hwEnclosure08FanIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEnclosure08FanIndex.setStatus("mandatory")
_HwEnclosure08FanDesc_Type = OctetString
_HwEnclosure08FanDesc_Object = MibTableColumn
hwEnclosure08FanDesc = _HwEnclosure08FanDesc_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 9, 9, 1, 2),
    _HwEnclosure08FanDesc_Type()
)
hwEnclosure08FanDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEnclosure08FanDesc.setStatus("mandatory")
_HwEnclosure08FanSpeed_Type = Integer32
_HwEnclosure08FanSpeed_Object = MibTableColumn
hwEnclosure08FanSpeed = _HwEnclosure08FanSpeed_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 9, 9, 1, 3),
    _HwEnclosure08FanSpeed_Type()
)
hwEnclosure08FanSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEnclosure08FanSpeed.setStatus("mandatory")
_HwEnclosure08TempTable_Object = MibTable
hwEnclosure08TempTable = _HwEnclosure08TempTable_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 9, 10)
)
if mibBuilder.loadTexts:
    hwEnclosure08TempTable.setStatus("mandatory")
_HwEnclosure08TempEntry_Object = MibTableRow
hwEnclosure08TempEntry = _HwEnclosure08TempEntry_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 9, 10, 1)
)
hwEnclosure08TempEntry.setIndexNames(
    (0, "ARECA-SAS-CARD1-MIB", "hwEnclosure08TempIndex"),
)
if mibBuilder.loadTexts:
    hwEnclosure08TempEntry.setStatus("mandatory")
_HwEnclosure08TempIndex_Type = Integer32
_HwEnclosure08TempIndex_Object = MibTableColumn
hwEnclosure08TempIndex = _HwEnclosure08TempIndex_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 9, 10, 1, 1),
    _HwEnclosure08TempIndex_Type()
)
hwEnclosure08TempIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEnclosure08TempIndex.setStatus("mandatory")
_HwEnclosure08TempDesc_Type = OctetString
_HwEnclosure08TempDesc_Object = MibTableColumn
hwEnclosure08TempDesc = _HwEnclosure08TempDesc_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 9, 10, 1, 2),
    _HwEnclosure08TempDesc_Type()
)
hwEnclosure08TempDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEnclosure08TempDesc.setStatus("mandatory")
_HwEnclosure08TempValue_Type = Integer32
_HwEnclosure08TempValue_Object = MibTableColumn
hwEnclosure08TempValue = _HwEnclosure08TempValue_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 2, 9, 10, 1, 3),
    _HwEnclosure08TempValue_Type()
)
hwEnclosure08TempValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEnclosure08TempValue.setStatus("mandatory")
_HddInformation_ObjectIdentity = ObjectIdentity
hddInformation = _HddInformation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 3)
)
_HddEnclosure1_ObjectIdentity = ObjectIdentity
hddEnclosure1 = _HddEnclosure1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 3, 1)
)
_HddEnclosure01Installed_Type = Integer32
_HddEnclosure01Installed_Object = MibScalar
hddEnclosure01Installed = _HddEnclosure01Installed_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 3, 1, 1),
    _HddEnclosure01Installed_Type()
)
hddEnclosure01Installed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hddEnclosure01Installed.setStatus("mandatory")
_HddEnclosure01Description_Type = OctetString
_HddEnclosure01Description_Object = MibScalar
hddEnclosure01Description = _HddEnclosure01Description_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 3, 1, 2),
    _HddEnclosure01Description_Type()
)
hddEnclosure01Description.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hddEnclosure01Description.setStatus("mandatory")
_HddEnclosure01NumberOfSlot_Type = Integer32
_HddEnclosure01NumberOfSlot_Object = MibScalar
hddEnclosure01NumberOfSlot = _HddEnclosure01NumberOfSlot_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 3, 1, 3),
    _HddEnclosure01NumberOfSlot_Type()
)
hddEnclosure01NumberOfSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hddEnclosure01NumberOfSlot.setStatus("mandatory")
_HddEnclosure01InfoTable_Object = MibTable
hddEnclosure01InfoTable = _HddEnclosure01InfoTable_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 3, 1, 4)
)
if mibBuilder.loadTexts:
    hddEnclosure01InfoTable.setStatus("mandatory")
_HddEnclosure01InfoEntry_Object = MibTableRow
hddEnclosure01InfoEntry = _HddEnclosure01InfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 3, 1, 4, 1)
)
hddEnclosure01InfoEntry.setIndexNames(
    (0, "ARECA-SAS-CARD1-MIB", "hddEnclosure01Slots"),
)
if mibBuilder.loadTexts:
    hddEnclosure01InfoEntry.setStatus("mandatory")
_HddEnclosure01Slots_Type = Integer32
_HddEnclosure01Slots_Object = MibTableColumn
hddEnclosure01Slots = _HddEnclosure01Slots_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 3, 1, 4, 1, 1),
    _HddEnclosure01Slots_Type()
)
hddEnclosure01Slots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hddEnclosure01Slots.setStatus("mandatory")
_HddEnclosure01Desc_Type = OctetString
_HddEnclosure01Desc_Object = MibTableColumn
hddEnclosure01Desc = _HddEnclosure01Desc_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 3, 1, 4, 1, 2),
    _HddEnclosure01Desc_Type()
)
hddEnclosure01Desc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hddEnclosure01Desc.setStatus("mandatory")
_HddEnclosure01Name_Type = OctetString
_HddEnclosure01Name_Object = MibTableColumn
hddEnclosure01Name = _HddEnclosure01Name_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 3, 1, 4, 1, 3),
    _HddEnclosure01Name_Type()
)
hddEnclosure01Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hddEnclosure01Name.setStatus("mandatory")
_HddEnclosure01Serial_Type = OctetString
_HddEnclosure01Serial_Object = MibTableColumn
hddEnclosure01Serial = _HddEnclosure01Serial_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 3, 1, 4, 1, 4),
    _HddEnclosure01Serial_Type()
)
hddEnclosure01Serial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hddEnclosure01Serial.setStatus("mandatory")
_HddEnclosure01FirmVer_Type = OctetString
_HddEnclosure01FirmVer_Object = MibTableColumn
hddEnclosure01FirmVer = _HddEnclosure01FirmVer_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 3, 1, 4, 1, 5),
    _HddEnclosure01FirmVer_Type()
)
hddEnclosure01FirmVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hddEnclosure01FirmVer.setStatus("mandatory")
_HddEnclosure01Capacity_Type = Integer32
_HddEnclosure01Capacity_Object = MibTableColumn
hddEnclosure01Capacity = _HddEnclosure01Capacity_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 3, 1, 4, 1, 6),
    _HddEnclosure01Capacity_Type()
)
hddEnclosure01Capacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hddEnclosure01Capacity.setStatus("mandatory")


class _HddEnclosure01Type_Type(Integer32):
    """Custom type hddEnclosure01Type based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("sata", 1),
          ("sas", 2))
    )


_HddEnclosure01Type_Type.__name__ = "Integer32"
_HddEnclosure01Type_Object = MibTableColumn
hddEnclosure01Type = _HddEnclosure01Type_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 3, 1, 4, 1, 7),
    _HddEnclosure01Type_Type()
)
hddEnclosure01Type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hddEnclosure01Type.setStatus("mandatory")
_HddEnclosure01State_Type = OctetString
_HddEnclosure01State_Object = MibTableColumn
hddEnclosure01State = _HddEnclosure01State_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 3, 1, 4, 1, 8),
    _HddEnclosure01State_Type()
)
hddEnclosure01State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hddEnclosure01State.setStatus("mandatory")
_HddEnclosure2_ObjectIdentity = ObjectIdentity
hddEnclosure2 = _HddEnclosure2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 3, 2)
)
_HddEnclosure02Installed_Type = Integer32
_HddEnclosure02Installed_Object = MibScalar
hddEnclosure02Installed = _HddEnclosure02Installed_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 3, 2, 1),
    _HddEnclosure02Installed_Type()
)
hddEnclosure02Installed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hddEnclosure02Installed.setStatus("mandatory")
_HddEnclosure02Description_Type = OctetString
_HddEnclosure02Description_Object = MibScalar
hddEnclosure02Description = _HddEnclosure02Description_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 3, 2, 2),
    _HddEnclosure02Description_Type()
)
hddEnclosure02Description.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hddEnclosure02Description.setStatus("mandatory")
_HddEnclosure02NumberOfSlot_Type = Integer32
_HddEnclosure02NumberOfSlot_Object = MibScalar
hddEnclosure02NumberOfSlot = _HddEnclosure02NumberOfSlot_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 3, 2, 3),
    _HddEnclosure02NumberOfSlot_Type()
)
hddEnclosure02NumberOfSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hddEnclosure02NumberOfSlot.setStatus("mandatory")
_HddEnclosure02InfoTable_Object = MibTable
hddEnclosure02InfoTable = _HddEnclosure02InfoTable_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 3, 2, 4)
)
if mibBuilder.loadTexts:
    hddEnclosure02InfoTable.setStatus("mandatory")
_HddEnclosure02InfoEntry_Object = MibTableRow
hddEnclosure02InfoEntry = _HddEnclosure02InfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 3, 2, 4, 1)
)
hddEnclosure02InfoEntry.setIndexNames(
    (0, "ARECA-SAS-CARD1-MIB", "hddEnclosure02Slots"),
)
if mibBuilder.loadTexts:
    hddEnclosure02InfoEntry.setStatus("mandatory")
_HddEnclosure02Slots_Type = Integer32
_HddEnclosure02Slots_Object = MibTableColumn
hddEnclosure02Slots = _HddEnclosure02Slots_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 3, 2, 4, 1, 1),
    _HddEnclosure02Slots_Type()
)
hddEnclosure02Slots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hddEnclosure02Slots.setStatus("mandatory")
_HddEnclosure02Desc_Type = OctetString
_HddEnclosure02Desc_Object = MibTableColumn
hddEnclosure02Desc = _HddEnclosure02Desc_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 3, 2, 4, 1, 2),
    _HddEnclosure02Desc_Type()
)
hddEnclosure02Desc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hddEnclosure02Desc.setStatus("mandatory")
_HddEnclosure02Name_Type = OctetString
_HddEnclosure02Name_Object = MibTableColumn
hddEnclosure02Name = _HddEnclosure02Name_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 3, 2, 4, 1, 3),
    _HddEnclosure02Name_Type()
)
hddEnclosure02Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hddEnclosure02Name.setStatus("mandatory")
_HddEnclosure02Serial_Type = OctetString
_HddEnclosure02Serial_Object = MibTableColumn
hddEnclosure02Serial = _HddEnclosure02Serial_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 3, 2, 4, 1, 4),
    _HddEnclosure02Serial_Type()
)
hddEnclosure02Serial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hddEnclosure02Serial.setStatus("mandatory")
_HddEnclosure02FirmVer_Type = OctetString
_HddEnclosure02FirmVer_Object = MibTableColumn
hddEnclosure02FirmVer = _HddEnclosure02FirmVer_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 3, 2, 4, 1, 5),
    _HddEnclosure02FirmVer_Type()
)
hddEnclosure02FirmVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hddEnclosure02FirmVer.setStatus("mandatory")
_HddEnclosure02Capacity_Type = Integer32
_HddEnclosure02Capacity_Object = MibTableColumn
hddEnclosure02Capacity = _HddEnclosure02Capacity_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 3, 2, 4, 1, 6),
    _HddEnclosure02Capacity_Type()
)
hddEnclosure02Capacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hddEnclosure02Capacity.setStatus("mandatory")


class _HddEnclosure02Type_Type(Integer32):
    """Custom type hddEnclosure02Type based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("sata", 1),
          ("sas", 2))
    )


_HddEnclosure02Type_Type.__name__ = "Integer32"
_HddEnclosure02Type_Object = MibTableColumn
hddEnclosure02Type = _HddEnclosure02Type_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 3, 2, 4, 1, 7),
    _HddEnclosure02Type_Type()
)
hddEnclosure02Type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hddEnclosure02Type.setStatus("mandatory")
_HddEnclosure02State_Type = OctetString
_HddEnclosure02State_Object = MibTableColumn
hddEnclosure02State = _HddEnclosure02State_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 3, 2, 4, 1, 8),
    _HddEnclosure02State_Type()
)
hddEnclosure02State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hddEnclosure02State.setStatus("mandatory")
_HddEnclosure3_ObjectIdentity = ObjectIdentity
hddEnclosure3 = _HddEnclosure3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 3, 3)
)
_HddEnclosure03Installed_Type = Integer32
_HddEnclosure03Installed_Object = MibScalar
hddEnclosure03Installed = _HddEnclosure03Installed_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 3, 3, 1),
    _HddEnclosure03Installed_Type()
)
hddEnclosure03Installed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hddEnclosure03Installed.setStatus("mandatory")
_HddEnclosure03Description_Type = OctetString
_HddEnclosure03Description_Object = MibScalar
hddEnclosure03Description = _HddEnclosure03Description_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 3, 3, 2),
    _HddEnclosure03Description_Type()
)
hddEnclosure03Description.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hddEnclosure03Description.setStatus("mandatory")
_HddEnclosure03NumberOfSlot_Type = Integer32
_HddEnclosure03NumberOfSlot_Object = MibScalar
hddEnclosure03NumberOfSlot = _HddEnclosure03NumberOfSlot_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 3, 3, 3),
    _HddEnclosure03NumberOfSlot_Type()
)
hddEnclosure03NumberOfSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hddEnclosure03NumberOfSlot.setStatus("mandatory")
_HddEnclosure03InfoTable_Object = MibTable
hddEnclosure03InfoTable = _HddEnclosure03InfoTable_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 3, 3, 4)
)
if mibBuilder.loadTexts:
    hddEnclosure03InfoTable.setStatus("mandatory")
_HddEnclosure03InfoEntry_Object = MibTableRow
hddEnclosure03InfoEntry = _HddEnclosure03InfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 3, 3, 4, 1)
)
hddEnclosure03InfoEntry.setIndexNames(
    (0, "ARECA-SAS-CARD1-MIB", "hddEnclosure03Slots"),
)
if mibBuilder.loadTexts:
    hddEnclosure03InfoEntry.setStatus("mandatory")
_HddEnclosure03Slots_Type = Integer32
_HddEnclosure03Slots_Object = MibTableColumn
hddEnclosure03Slots = _HddEnclosure03Slots_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 3, 3, 4, 1, 1),
    _HddEnclosure03Slots_Type()
)
hddEnclosure03Slots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hddEnclosure03Slots.setStatus("mandatory")
_HddEnclosure03Desc_Type = OctetString
_HddEnclosure03Desc_Object = MibTableColumn
hddEnclosure03Desc = _HddEnclosure03Desc_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 3, 3, 4, 1, 2),
    _HddEnclosure03Desc_Type()
)
hddEnclosure03Desc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hddEnclosure03Desc.setStatus("mandatory")
_HddEnclosure03Name_Type = OctetString
_HddEnclosure03Name_Object = MibTableColumn
hddEnclosure03Name = _HddEnclosure03Name_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 3, 3, 4, 1, 3),
    _HddEnclosure03Name_Type()
)
hddEnclosure03Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hddEnclosure03Name.setStatus("mandatory")
_HddEnclosure03Serial_Type = OctetString
_HddEnclosure03Serial_Object = MibTableColumn
hddEnclosure03Serial = _HddEnclosure03Serial_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 3, 3, 4, 1, 4),
    _HddEnclosure03Serial_Type()
)
hddEnclosure03Serial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hddEnclosure03Serial.setStatus("mandatory")
_HddEnclosure03FirmVer_Type = OctetString
_HddEnclosure03FirmVer_Object = MibTableColumn
hddEnclosure03FirmVer = _HddEnclosure03FirmVer_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 3, 3, 4, 1, 5),
    _HddEnclosure03FirmVer_Type()
)
hddEnclosure03FirmVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hddEnclosure03FirmVer.setStatus("mandatory")
_HddEnclosure03Capacity_Type = Integer32
_HddEnclosure03Capacity_Object = MibTableColumn
hddEnclosure03Capacity = _HddEnclosure03Capacity_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 3, 3, 4, 1, 6),
    _HddEnclosure03Capacity_Type()
)
hddEnclosure03Capacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hddEnclosure03Capacity.setStatus("mandatory")


class _HddEnclosure03Type_Type(Integer32):
    """Custom type hddEnclosure03Type based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("sata", 1),
          ("sas", 2))
    )


_HddEnclosure03Type_Type.__name__ = "Integer32"
_HddEnclosure03Type_Object = MibTableColumn
hddEnclosure03Type = _HddEnclosure03Type_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 3, 3, 4, 1, 7),
    _HddEnclosure03Type_Type()
)
hddEnclosure03Type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hddEnclosure03Type.setStatus("mandatory")
_HddEnclosure03State_Type = OctetString
_HddEnclosure03State_Object = MibTableColumn
hddEnclosure03State = _HddEnclosure03State_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 3, 3, 4, 1, 8),
    _HddEnclosure03State_Type()
)
hddEnclosure03State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hddEnclosure03State.setStatus("mandatory")
_HddEnclosure4_ObjectIdentity = ObjectIdentity
hddEnclosure4 = _HddEnclosure4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 3, 4)
)
_HddEnclosure04Installed_Type = Integer32
_HddEnclosure04Installed_Object = MibScalar
hddEnclosure04Installed = _HddEnclosure04Installed_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 3, 4, 1),
    _HddEnclosure04Installed_Type()
)
hddEnclosure04Installed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hddEnclosure04Installed.setStatus("mandatory")
_HddEnclosure04Description_Type = OctetString
_HddEnclosure04Description_Object = MibScalar
hddEnclosure04Description = _HddEnclosure04Description_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 3, 4, 2),
    _HddEnclosure04Description_Type()
)
hddEnclosure04Description.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hddEnclosure04Description.setStatus("mandatory")
_HddEnclosure04NumberOfSlot_Type = Integer32
_HddEnclosure04NumberOfSlot_Object = MibScalar
hddEnclosure04NumberOfSlot = _HddEnclosure04NumberOfSlot_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 3, 4, 3),
    _HddEnclosure04NumberOfSlot_Type()
)
hddEnclosure04NumberOfSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hddEnclosure04NumberOfSlot.setStatus("mandatory")
_HddEnclosure04InfoTable_Object = MibTable
hddEnclosure04InfoTable = _HddEnclosure04InfoTable_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 3, 4, 4)
)
if mibBuilder.loadTexts:
    hddEnclosure04InfoTable.setStatus("mandatory")
_HddEnclosure04InfoEntry_Object = MibTableRow
hddEnclosure04InfoEntry = _HddEnclosure04InfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 3, 4, 4, 1)
)
hddEnclosure04InfoEntry.setIndexNames(
    (0, "ARECA-SAS-CARD1-MIB", "hddEnclosure04Slots"),
)
if mibBuilder.loadTexts:
    hddEnclosure04InfoEntry.setStatus("mandatory")
_HddEnclosure04Slots_Type = Integer32
_HddEnclosure04Slots_Object = MibTableColumn
hddEnclosure04Slots = _HddEnclosure04Slots_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 3, 4, 4, 1, 1),
    _HddEnclosure04Slots_Type()
)
hddEnclosure04Slots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hddEnclosure04Slots.setStatus("mandatory")
_HddEnclosure04Desc_Type = OctetString
_HddEnclosure04Desc_Object = MibTableColumn
hddEnclosure04Desc = _HddEnclosure04Desc_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 3, 4, 4, 1, 2),
    _HddEnclosure04Desc_Type()
)
hddEnclosure04Desc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hddEnclosure04Desc.setStatus("mandatory")
_HddEnclosure04Name_Type = OctetString
_HddEnclosure04Name_Object = MibTableColumn
hddEnclosure04Name = _HddEnclosure04Name_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 3, 4, 4, 1, 3),
    _HddEnclosure04Name_Type()
)
hddEnclosure04Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hddEnclosure04Name.setStatus("mandatory")
_HddEnclosure04Serial_Type = OctetString
_HddEnclosure04Serial_Object = MibTableColumn
hddEnclosure04Serial = _HddEnclosure04Serial_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 3, 4, 4, 1, 4),
    _HddEnclosure04Serial_Type()
)
hddEnclosure04Serial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hddEnclosure04Serial.setStatus("mandatory")
_HddEnclosure04FirmVer_Type = OctetString
_HddEnclosure04FirmVer_Object = MibTableColumn
hddEnclosure04FirmVer = _HddEnclosure04FirmVer_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 3, 4, 4, 1, 5),
    _HddEnclosure04FirmVer_Type()
)
hddEnclosure04FirmVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hddEnclosure04FirmVer.setStatus("mandatory")
_HddEnclosure04Capacity_Type = Integer32
_HddEnclosure04Capacity_Object = MibTableColumn
hddEnclosure04Capacity = _HddEnclosure04Capacity_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 3, 4, 4, 1, 6),
    _HddEnclosure04Capacity_Type()
)
hddEnclosure04Capacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hddEnclosure04Capacity.setStatus("mandatory")


class _HddEnclosure04Type_Type(Integer32):
    """Custom type hddEnclosure04Type based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("sata", 1),
          ("sas", 2))
    )


_HddEnclosure04Type_Type.__name__ = "Integer32"
_HddEnclosure04Type_Object = MibTableColumn
hddEnclosure04Type = _HddEnclosure04Type_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 3, 4, 4, 1, 7),
    _HddEnclosure04Type_Type()
)
hddEnclosure04Type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hddEnclosure04Type.setStatus("mandatory")
_HddEnclosure04State_Type = OctetString
_HddEnclosure04State_Object = MibTableColumn
hddEnclosure04State = _HddEnclosure04State_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 3, 4, 4, 1, 8),
    _HddEnclosure04State_Type()
)
hddEnclosure04State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hddEnclosure04State.setStatus("mandatory")
_HddEnclosure5_ObjectIdentity = ObjectIdentity
hddEnclosure5 = _HddEnclosure5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 3, 5)
)
_HddEnclosure05Installed_Type = Integer32
_HddEnclosure05Installed_Object = MibScalar
hddEnclosure05Installed = _HddEnclosure05Installed_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 3, 5, 1),
    _HddEnclosure05Installed_Type()
)
hddEnclosure05Installed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hddEnclosure05Installed.setStatus("mandatory")
_HddEnclosure05Description_Type = OctetString
_HddEnclosure05Description_Object = MibScalar
hddEnclosure05Description = _HddEnclosure05Description_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 3, 5, 2),
    _HddEnclosure05Description_Type()
)
hddEnclosure05Description.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hddEnclosure05Description.setStatus("mandatory")
_HddEnclosure05NumberOfSlot_Type = Integer32
_HddEnclosure05NumberOfSlot_Object = MibScalar
hddEnclosure05NumberOfSlot = _HddEnclosure05NumberOfSlot_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 3, 5, 3),
    _HddEnclosure05NumberOfSlot_Type()
)
hddEnclosure05NumberOfSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hddEnclosure05NumberOfSlot.setStatus("mandatory")
_HddEnclosure05InfoTable_Object = MibTable
hddEnclosure05InfoTable = _HddEnclosure05InfoTable_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 3, 5, 4)
)
if mibBuilder.loadTexts:
    hddEnclosure05InfoTable.setStatus("mandatory")
_HddEnclosure05InfoEntry_Object = MibTableRow
hddEnclosure05InfoEntry = _HddEnclosure05InfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 3, 5, 4, 1)
)
hddEnclosure05InfoEntry.setIndexNames(
    (0, "ARECA-SAS-CARD1-MIB", "hddEnclosure05Slots"),
)
if mibBuilder.loadTexts:
    hddEnclosure05InfoEntry.setStatus("mandatory")
_HddEnclosure05Slots_Type = Integer32
_HddEnclosure05Slots_Object = MibTableColumn
hddEnclosure05Slots = _HddEnclosure05Slots_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 3, 5, 4, 1, 1),
    _HddEnclosure05Slots_Type()
)
hddEnclosure05Slots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hddEnclosure05Slots.setStatus("mandatory")
_HddEnclosure05Desc_Type = OctetString
_HddEnclosure05Desc_Object = MibTableColumn
hddEnclosure05Desc = _HddEnclosure05Desc_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 3, 5, 4, 1, 2),
    _HddEnclosure05Desc_Type()
)
hddEnclosure05Desc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hddEnclosure05Desc.setStatus("mandatory")
_HddEnclosure05Name_Type = OctetString
_HddEnclosure05Name_Object = MibTableColumn
hddEnclosure05Name = _HddEnclosure05Name_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 3, 5, 4, 1, 3),
    _HddEnclosure05Name_Type()
)
hddEnclosure05Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hddEnclosure05Name.setStatus("mandatory")
_HddEnclosure05Serial_Type = OctetString
_HddEnclosure05Serial_Object = MibTableColumn
hddEnclosure05Serial = _HddEnclosure05Serial_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 3, 5, 4, 1, 4),
    _HddEnclosure05Serial_Type()
)
hddEnclosure05Serial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hddEnclosure05Serial.setStatus("mandatory")
_HddEnclosure05FirmVer_Type = OctetString
_HddEnclosure05FirmVer_Object = MibTableColumn
hddEnclosure05FirmVer = _HddEnclosure05FirmVer_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 3, 5, 4, 1, 5),
    _HddEnclosure05FirmVer_Type()
)
hddEnclosure05FirmVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hddEnclosure05FirmVer.setStatus("mandatory")
_HddEnclosure05Capacity_Type = Integer32
_HddEnclosure05Capacity_Object = MibTableColumn
hddEnclosure05Capacity = _HddEnclosure05Capacity_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 3, 5, 4, 1, 6),
    _HddEnclosure05Capacity_Type()
)
hddEnclosure05Capacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hddEnclosure05Capacity.setStatus("mandatory")


class _HddEnclosure05Type_Type(Integer32):
    """Custom type hddEnclosure05Type based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("sata", 1),
          ("sas", 2))
    )


_HddEnclosure05Type_Type.__name__ = "Integer32"
_HddEnclosure05Type_Object = MibTableColumn
hddEnclosure05Type = _HddEnclosure05Type_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 3, 5, 4, 1, 7),
    _HddEnclosure05Type_Type()
)
hddEnclosure05Type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hddEnclosure05Type.setStatus("mandatory")
_HddEnclosure05State_Type = OctetString
_HddEnclosure05State_Object = MibTableColumn
hddEnclosure05State = _HddEnclosure05State_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 3, 5, 4, 1, 8),
    _HddEnclosure05State_Type()
)
hddEnclosure05State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hddEnclosure05State.setStatus("mandatory")
_HddEnclosure6_ObjectIdentity = ObjectIdentity
hddEnclosure6 = _HddEnclosure6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 3, 6)
)
_HddEnclosure06Installed_Type = Integer32
_HddEnclosure06Installed_Object = MibScalar
hddEnclosure06Installed = _HddEnclosure06Installed_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 3, 6, 1),
    _HddEnclosure06Installed_Type()
)
hddEnclosure06Installed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hddEnclosure06Installed.setStatus("mandatory")
_HddEnclosure06Description_Type = OctetString
_HddEnclosure06Description_Object = MibScalar
hddEnclosure06Description = _HddEnclosure06Description_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 3, 6, 2),
    _HddEnclosure06Description_Type()
)
hddEnclosure06Description.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hddEnclosure06Description.setStatus("mandatory")
_HddEnclosure06NumberOfSlot_Type = Integer32
_HddEnclosure06NumberOfSlot_Object = MibScalar
hddEnclosure06NumberOfSlot = _HddEnclosure06NumberOfSlot_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 3, 6, 3),
    _HddEnclosure06NumberOfSlot_Type()
)
hddEnclosure06NumberOfSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hddEnclosure06NumberOfSlot.setStatus("mandatory")
_HddEnclosure06InfoTable_Object = MibTable
hddEnclosure06InfoTable = _HddEnclosure06InfoTable_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 3, 6, 4)
)
if mibBuilder.loadTexts:
    hddEnclosure06InfoTable.setStatus("mandatory")
_HddEnclosure06InfoEntry_Object = MibTableRow
hddEnclosure06InfoEntry = _HddEnclosure06InfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 3, 6, 4, 1)
)
hddEnclosure06InfoEntry.setIndexNames(
    (0, "ARECA-SAS-CARD1-MIB", "hddEnclosure06Slots"),
)
if mibBuilder.loadTexts:
    hddEnclosure06InfoEntry.setStatus("mandatory")
_HddEnclosure06Slots_Type = Integer32
_HddEnclosure06Slots_Object = MibTableColumn
hddEnclosure06Slots = _HddEnclosure06Slots_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 3, 6, 4, 1, 1),
    _HddEnclosure06Slots_Type()
)
hddEnclosure06Slots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hddEnclosure06Slots.setStatus("mandatory")
_HddEnclosure06Desc_Type = OctetString
_HddEnclosure06Desc_Object = MibTableColumn
hddEnclosure06Desc = _HddEnclosure06Desc_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 3, 6, 4, 1, 2),
    _HddEnclosure06Desc_Type()
)
hddEnclosure06Desc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hddEnclosure06Desc.setStatus("mandatory")
_HddEnclosure06Name_Type = OctetString
_HddEnclosure06Name_Object = MibTableColumn
hddEnclosure06Name = _HddEnclosure06Name_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 3, 6, 4, 1, 3),
    _HddEnclosure06Name_Type()
)
hddEnclosure06Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hddEnclosure06Name.setStatus("mandatory")
_HddEnclosure06Serial_Type = OctetString
_HddEnclosure06Serial_Object = MibTableColumn
hddEnclosure06Serial = _HddEnclosure06Serial_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 3, 6, 4, 1, 4),
    _HddEnclosure06Serial_Type()
)
hddEnclosure06Serial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hddEnclosure06Serial.setStatus("mandatory")
_HddEnclosure06FirmVer_Type = OctetString
_HddEnclosure06FirmVer_Object = MibTableColumn
hddEnclosure06FirmVer = _HddEnclosure06FirmVer_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 3, 6, 4, 1, 5),
    _HddEnclosure06FirmVer_Type()
)
hddEnclosure06FirmVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hddEnclosure06FirmVer.setStatus("mandatory")
_HddEnclosure06Capacity_Type = Integer32
_HddEnclosure06Capacity_Object = MibTableColumn
hddEnclosure06Capacity = _HddEnclosure06Capacity_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 3, 6, 4, 1, 6),
    _HddEnclosure06Capacity_Type()
)
hddEnclosure06Capacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hddEnclosure06Capacity.setStatus("mandatory")


class _HddEnclosure06Type_Type(Integer32):
    """Custom type hddEnclosure06Type based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("sata", 1),
          ("sas", 2))
    )


_HddEnclosure06Type_Type.__name__ = "Integer32"
_HddEnclosure06Type_Object = MibTableColumn
hddEnclosure06Type = _HddEnclosure06Type_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 3, 6, 4, 1, 7),
    _HddEnclosure06Type_Type()
)
hddEnclosure06Type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hddEnclosure06Type.setStatus("mandatory")
_HddEnclosure06State_Type = OctetString
_HddEnclosure06State_Object = MibTableColumn
hddEnclosure06State = _HddEnclosure06State_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 3, 6, 4, 1, 8),
    _HddEnclosure06State_Type()
)
hddEnclosure06State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hddEnclosure06State.setStatus("mandatory")
_HddEnclosure7_ObjectIdentity = ObjectIdentity
hddEnclosure7 = _HddEnclosure7_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 3, 7)
)
_HddEnclosure07Installed_Type = Integer32
_HddEnclosure07Installed_Object = MibScalar
hddEnclosure07Installed = _HddEnclosure07Installed_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 3, 7, 1),
    _HddEnclosure07Installed_Type()
)
hddEnclosure07Installed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hddEnclosure07Installed.setStatus("mandatory")
_HddEnclosure07Description_Type = OctetString
_HddEnclosure07Description_Object = MibScalar
hddEnclosure07Description = _HddEnclosure07Description_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 3, 7, 2),
    _HddEnclosure07Description_Type()
)
hddEnclosure07Description.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hddEnclosure07Description.setStatus("mandatory")
_HddEnclosure07NumberOfSlot_Type = Integer32
_HddEnclosure07NumberOfSlot_Object = MibScalar
hddEnclosure07NumberOfSlot = _HddEnclosure07NumberOfSlot_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 3, 7, 3),
    _HddEnclosure07NumberOfSlot_Type()
)
hddEnclosure07NumberOfSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hddEnclosure07NumberOfSlot.setStatus("mandatory")
_HddEnclosure07InfoTable_Object = MibTable
hddEnclosure07InfoTable = _HddEnclosure07InfoTable_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 3, 7, 4)
)
if mibBuilder.loadTexts:
    hddEnclosure07InfoTable.setStatus("mandatory")
_HddEnclosure07InfoEntry_Object = MibTableRow
hddEnclosure07InfoEntry = _HddEnclosure07InfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 3, 7, 4, 1)
)
hddEnclosure07InfoEntry.setIndexNames(
    (0, "ARECA-SAS-CARD1-MIB", "hddEnclosure07Slots"),
)
if mibBuilder.loadTexts:
    hddEnclosure07InfoEntry.setStatus("mandatory")
_HddEnclosure07Slots_Type = Integer32
_HddEnclosure07Slots_Object = MibTableColumn
hddEnclosure07Slots = _HddEnclosure07Slots_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 3, 7, 4, 1, 1),
    _HddEnclosure07Slots_Type()
)
hddEnclosure07Slots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hddEnclosure07Slots.setStatus("mandatory")
_HddEnclosure07Desc_Type = OctetString
_HddEnclosure07Desc_Object = MibTableColumn
hddEnclosure07Desc = _HddEnclosure07Desc_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 3, 7, 4, 1, 2),
    _HddEnclosure07Desc_Type()
)
hddEnclosure07Desc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hddEnclosure07Desc.setStatus("mandatory")
_HddEnclosure07Name_Type = OctetString
_HddEnclosure07Name_Object = MibTableColumn
hddEnclosure07Name = _HddEnclosure07Name_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 3, 7, 4, 1, 3),
    _HddEnclosure07Name_Type()
)
hddEnclosure07Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hddEnclosure07Name.setStatus("mandatory")
_HddEnclosure07Serial_Type = OctetString
_HddEnclosure07Serial_Object = MibTableColumn
hddEnclosure07Serial = _HddEnclosure07Serial_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 3, 7, 4, 1, 4),
    _HddEnclosure07Serial_Type()
)
hddEnclosure07Serial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hddEnclosure07Serial.setStatus("mandatory")
_HddEnclosure07FirmVer_Type = OctetString
_HddEnclosure07FirmVer_Object = MibTableColumn
hddEnclosure07FirmVer = _HddEnclosure07FirmVer_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 3, 7, 4, 1, 5),
    _HddEnclosure07FirmVer_Type()
)
hddEnclosure07FirmVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hddEnclosure07FirmVer.setStatus("mandatory")
_HddEnclosure07Capacity_Type = Integer32
_HddEnclosure07Capacity_Object = MibTableColumn
hddEnclosure07Capacity = _HddEnclosure07Capacity_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 3, 7, 4, 1, 6),
    _HddEnclosure07Capacity_Type()
)
hddEnclosure07Capacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hddEnclosure07Capacity.setStatus("mandatory")


class _HddEnclosure07Type_Type(Integer32):
    """Custom type hddEnclosure07Type based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("sata", 1),
          ("sas", 2))
    )


_HddEnclosure07Type_Type.__name__ = "Integer32"
_HddEnclosure07Type_Object = MibTableColumn
hddEnclosure07Type = _HddEnclosure07Type_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 3, 7, 4, 1, 7),
    _HddEnclosure07Type_Type()
)
hddEnclosure07Type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hddEnclosure07Type.setStatus("mandatory")
_HddEnclosure07State_Type = OctetString
_HddEnclosure07State_Object = MibTableColumn
hddEnclosure07State = _HddEnclosure07State_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 3, 7, 4, 1, 8),
    _HddEnclosure07State_Type()
)
hddEnclosure07State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hddEnclosure07State.setStatus("mandatory")
_HddEnclosure8_ObjectIdentity = ObjectIdentity
hddEnclosure8 = _HddEnclosure8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 3, 8)
)
_HddEnclosure08Installed_Type = Integer32
_HddEnclosure08Installed_Object = MibScalar
hddEnclosure08Installed = _HddEnclosure08Installed_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 3, 8, 1),
    _HddEnclosure08Installed_Type()
)
hddEnclosure08Installed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hddEnclosure08Installed.setStatus("mandatory")
_HddEnclosure08Description_Type = OctetString
_HddEnclosure08Description_Object = MibScalar
hddEnclosure08Description = _HddEnclosure08Description_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 3, 8, 2),
    _HddEnclosure08Description_Type()
)
hddEnclosure08Description.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hddEnclosure08Description.setStatus("mandatory")
_HddEnclosure08NumberOfSlot_Type = Integer32
_HddEnclosure08NumberOfSlot_Object = MibScalar
hddEnclosure08NumberOfSlot = _HddEnclosure08NumberOfSlot_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 3, 8, 3),
    _HddEnclosure08NumberOfSlot_Type()
)
hddEnclosure08NumberOfSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hddEnclosure08NumberOfSlot.setStatus("mandatory")
_HddEnclosure08InfoTable_Object = MibTable
hddEnclosure08InfoTable = _HddEnclosure08InfoTable_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 3, 8, 4)
)
if mibBuilder.loadTexts:
    hddEnclosure08InfoTable.setStatus("mandatory")
_HddEnclosure08InfoEntry_Object = MibTableRow
hddEnclosure08InfoEntry = _HddEnclosure08InfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 3, 8, 4, 1)
)
hddEnclosure08InfoEntry.setIndexNames(
    (0, "ARECA-SAS-CARD1-MIB", "hddEnclosure08Slots"),
)
if mibBuilder.loadTexts:
    hddEnclosure08InfoEntry.setStatus("mandatory")
_HddEnclosure08Slots_Type = Integer32
_HddEnclosure08Slots_Object = MibTableColumn
hddEnclosure08Slots = _HddEnclosure08Slots_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 3, 8, 4, 1, 1),
    _HddEnclosure08Slots_Type()
)
hddEnclosure08Slots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hddEnclosure08Slots.setStatus("mandatory")
_HddEnclosure08Desc_Type = OctetString
_HddEnclosure08Desc_Object = MibTableColumn
hddEnclosure08Desc = _HddEnclosure08Desc_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 3, 8, 4, 1, 2),
    _HddEnclosure08Desc_Type()
)
hddEnclosure08Desc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hddEnclosure08Desc.setStatus("mandatory")
_HddEnclosure08Name_Type = OctetString
_HddEnclosure08Name_Object = MibTableColumn
hddEnclosure08Name = _HddEnclosure08Name_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 3, 8, 4, 1, 3),
    _HddEnclosure08Name_Type()
)
hddEnclosure08Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hddEnclosure08Name.setStatus("mandatory")
_HddEnclosure08Serial_Type = OctetString
_HddEnclosure08Serial_Object = MibTableColumn
hddEnclosure08Serial = _HddEnclosure08Serial_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 3, 8, 4, 1, 4),
    _HddEnclosure08Serial_Type()
)
hddEnclosure08Serial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hddEnclosure08Serial.setStatus("mandatory")
_HddEnclosure08FirmVer_Type = OctetString
_HddEnclosure08FirmVer_Object = MibTableColumn
hddEnclosure08FirmVer = _HddEnclosure08FirmVer_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 3, 8, 4, 1, 5),
    _HddEnclosure08FirmVer_Type()
)
hddEnclosure08FirmVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hddEnclosure08FirmVer.setStatus("mandatory")
_HddEnclosure08Capacity_Type = Integer32
_HddEnclosure08Capacity_Object = MibTableColumn
hddEnclosure08Capacity = _HddEnclosure08Capacity_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 3, 8, 4, 1, 6),
    _HddEnclosure08Capacity_Type()
)
hddEnclosure08Capacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hddEnclosure08Capacity.setStatus("mandatory")


class _HddEnclosure08Type_Type(Integer32):
    """Custom type hddEnclosure08Type based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("sata", 1),
          ("sas", 2))
    )


_HddEnclosure08Type_Type.__name__ = "Integer32"
_HddEnclosure08Type_Object = MibTableColumn
hddEnclosure08Type = _HddEnclosure08Type_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 3, 8, 4, 1, 7),
    _HddEnclosure08Type_Type()
)
hddEnclosure08Type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hddEnclosure08Type.setStatus("mandatory")
_HddEnclosure08State_Type = OctetString
_HddEnclosure08State_Object = MibTableColumn
hddEnclosure08State = _HddEnclosure08State_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 3, 8, 4, 1, 8),
    _HddEnclosure08State_Type()
)
hddEnclosure08State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hddEnclosure08State.setStatus("mandatory")
_RaidsetInformation_ObjectIdentity = ObjectIdentity
raidsetInformation = _RaidsetInformation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 4)
)
_RaidInfoTable_Object = MibTable
raidInfoTable = _RaidInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 4, 1)
)
if mibBuilder.loadTexts:
    raidInfoTable.setStatus("mandatory")
_RaidInfoEntry_Object = MibTableRow
raidInfoEntry = _RaidInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 4, 1, 1)
)
raidInfoEntry.setIndexNames(
    (0, "ARECA-SAS-CARD1-MIB", "raidNumber"),
)
if mibBuilder.loadTexts:
    raidInfoEntry.setStatus("mandatory")
_RaidNumber_Type = Integer32
_RaidNumber_Object = MibTableColumn
raidNumber = _RaidNumber_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 4, 1, 1, 1),
    _RaidNumber_Type()
)
raidNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidNumber.setStatus("mandatory")
_RaidName_Type = OctetString
_RaidName_Object = MibTableColumn
raidName = _RaidName_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 4, 1, 1, 2),
    _RaidName_Type()
)
raidName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidName.setStatus("mandatory")
_RaidDisks_Type = Integer32
_RaidDisks_Object = MibTableColumn
raidDisks = _RaidDisks_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 4, 1, 1, 3),
    _RaidDisks_Type()
)
raidDisks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidDisks.setStatus("mandatory")
_RaidState_Type = OctetString
_RaidState_Object = MibTableColumn
raidState = _RaidState_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 4, 1, 1, 4),
    _RaidState_Type()
)
raidState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidState.setStatus("mandatory")
_RaidTotalCapacity_Type = Integer32
_RaidTotalCapacity_Object = MibTableColumn
raidTotalCapacity = _RaidTotalCapacity_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 4, 1, 1, 5),
    _RaidTotalCapacity_Type()
)
raidTotalCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidTotalCapacity.setStatus("mandatory")
_RaidFreeCapacity_Type = Integer32
_RaidFreeCapacity_Object = MibTableColumn
raidFreeCapacity = _RaidFreeCapacity_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 4, 1, 1, 6),
    _RaidFreeCapacity_Type()
)
raidFreeCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidFreeCapacity.setStatus("mandatory")
_RaidMemberDiskCapacity_Type = Integer32
_RaidMemberDiskCapacity_Object = MibTableColumn
raidMemberDiskCapacity = _RaidMemberDiskCapacity_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 4, 1, 1, 7),
    _RaidMemberDiskCapacity_Type()
)
raidMemberDiskCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidMemberDiskCapacity.setStatus("mandatory")
_RaidMemberDiskChannels_Type = OctetString
_RaidMemberDiskChannels_Object = MibTableColumn
raidMemberDiskChannels = _RaidMemberDiskChannels_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 4, 1, 1, 8),
    _RaidMemberDiskChannels_Type()
)
raidMemberDiskChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidMemberDiskChannels.setStatus("mandatory")
_VolumesetInformation_ObjectIdentity = ObjectIdentity
volumesetInformation = _VolumesetInformation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 5)
)
_VolInfoTable_Object = MibTable
volInfoTable = _VolInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 5, 1)
)
if mibBuilder.loadTexts:
    volInfoTable.setStatus("mandatory")
_VolInfoEntry_Object = MibTableRow
volInfoEntry = _VolInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 5, 1, 1)
)
volInfoEntry.setIndexNames(
    (0, "ARECA-SAS-CARD1-MIB", "volNumber"),
)
if mibBuilder.loadTexts:
    volInfoEntry.setStatus("mandatory")
_VolNumber_Type = Integer32
_VolNumber_Object = MibTableColumn
volNumber = _VolNumber_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 5, 1, 1, 1),
    _VolNumber_Type()
)
volNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volNumber.setStatus("mandatory")
_VolName_Type = OctetString
_VolName_Object = MibTableColumn
volName = _VolName_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 5, 1, 1, 2),
    _VolName_Type()
)
volName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volName.setStatus("mandatory")
_VolRaidName_Type = OctetString
_VolRaidName_Object = MibTableColumn
volRaidName = _VolRaidName_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 5, 1, 1, 3),
    _VolRaidName_Type()
)
volRaidName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volRaidName.setStatus("mandatory")
_VolCapacity_Type = Integer32
_VolCapacity_Object = MibTableColumn
volCapacity = _VolCapacity_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 5, 1, 1, 4),
    _VolCapacity_Type()
)
volCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volCapacity.setStatus("mandatory")
_VolState_Type = OctetString
_VolState_Object = MibTableColumn
volState = _VolState_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 5, 1, 1, 5),
    _VolState_Type()
)
volState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volState.setStatus("mandatory")
_VolProgress_Type = Integer32
_VolProgress_Object = MibTableColumn
volProgress = _VolProgress_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 5, 1, 1, 6),
    _VolProgress_Type()
)
volProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volProgress.setStatus("mandatory")
_VolCluster_Type = Integer32
_VolCluster_Object = MibTableColumn
volCluster = _VolCluster_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 5, 1, 1, 7),
    _VolCluster_Type()
)
volCluster.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volCluster.setStatus("mandatory")
_VolChannel_Type = Integer32
_VolChannel_Object = MibTableColumn
volChannel = _VolChannel_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 5, 1, 1, 8),
    _VolChannel_Type()
)
volChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volChannel.setStatus("mandatory")
_VolSCSIID_Type = Integer32
_VolSCSIID_Object = MibTableColumn
volSCSIID = _VolSCSIID_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 5, 1, 1, 9),
    _VolSCSIID_Type()
)
volSCSIID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volSCSIID.setStatus("mandatory")
_VolSCSILUN_Type = Integer32
_VolSCSILUN_Object = MibTableColumn
volSCSILUN = _VolSCSILUN_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 5, 1, 1, 10),
    _VolSCSILUN_Type()
)
volSCSILUN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volSCSILUN.setStatus("mandatory")
_VolRaidLevel_Type = OctetString
_VolRaidLevel_Object = MibTableColumn
volRaidLevel = _VolRaidLevel_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 5, 1, 1, 11),
    _VolRaidLevel_Type()
)
volRaidLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volRaidLevel.setStatus("mandatory")


class _VolStripes_Type(Integer32):
    """Custom type volStripes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(4096,
              8192,
              16384,
              32768,
              65536,
              131072)
        )
    )
    namedValues = NamedValues(
        *(("s4K", 4096),
          ("s8K", 8192),
          ("s16K", 16384),
          ("s32K", 32768),
          ("s64K", 65536),
          ("s128K", 131072))
    )


_VolStripes_Type.__name__ = "Integer32"
_VolStripes_Object = MibTableColumn
volStripes = _VolStripes_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 5, 1, 1, 12),
    _VolStripes_Type()
)
volStripes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volStripes.setStatus("mandatory")
_VolDisks_Type = Integer32
_VolDisks_Object = MibTableColumn
volDisks = _VolDisks_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 5, 1, 1, 13),
    _VolDisks_Type()
)
volDisks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volDisks.setStatus("mandatory")


class _VolCache_Type(Integer32):
    """Custom type volCache based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("write-through", 0),
          ("write-back", 1))
    )


_VolCache_Type.__name__ = "Integer32"
_VolCache_Object = MibTableColumn
volCache = _VolCache_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 5, 1, 1, 14),
    _VolCache_Type()
)
volCache.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volCache.setStatus("mandatory")


class _VolTag_Type(Integer32):
    """Custom type volTag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_VolTag_Type.__name__ = "Integer32"
_VolTag_Object = MibTableColumn
volTag = _VolTag_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 5, 1, 1, 15),
    _VolTag_Type()
)
volTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volTag.setStatus("mandatory")
_VolMaxSpeed_Type = OctetString
_VolMaxSpeed_Object = MibTableColumn
volMaxSpeed = _VolMaxSpeed_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 5, 1, 1, 16),
    _VolMaxSpeed_Type()
)
volMaxSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volMaxSpeed.setStatus("mandatory")
_VolCurrentSpeed_Type = OctetString
_VolCurrentSpeed_Object = MibTableColumn
volCurrentSpeed = _VolCurrentSpeed_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 5, 1, 1, 17),
    _VolCurrentSpeed_Type()
)
volCurrentSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volCurrentSpeed.setStatus("mandatory")
_EventInformation_ObjectIdentity = ObjectIdentity
eventInformation = _EventInformation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 6)
)
_EventInfoTable_Object = MibTable
eventInfoTable = _EventInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 6, 1)
)
if mibBuilder.loadTexts:
    eventInfoTable.setStatus("mandatory")
_EventInfoEntry_Object = MibTableRow
eventInfoEntry = _EventInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 6, 1, 1)
)
eventInfoEntry.setIndexNames(
    (0, "ARECA-SAS-CARD1-MIB", "eventNumber"),
)
if mibBuilder.loadTexts:
    eventInfoEntry.setStatus("mandatory")
_EventNumber_Type = Integer32
_EventNumber_Object = MibTableColumn
eventNumber = _EventNumber_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 6, 1, 1, 1),
    _EventNumber_Type()
)
eventNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventNumber.setStatus("mandatory")
_EventString_Type = OctetString
_EventString_Object = MibTableColumn
eventString = _EventString_Object(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 6, 1, 1, 2),
    _EventString_Type()
)
eventString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventString.setStatus("mandatory")
_RaidSubSysTraps_ObjectIdentity = ObjectIdentity
raidSubSysTraps = _RaidSubSysTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 7)
)

# Managed Objects groups


# Notification objects

rsCreate = NotificationType(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 7, 0, 128)
)
rsCreate.setObjects(
    ("ARECA-SAS-CARD1-MIB", "eventString")
)
if mibBuilder.loadTexts:
    rsCreate.setStatus(
        ""
    )

rsDelete = NotificationType(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 7, 0, 129)
)
rsDelete.setObjects(
    ("ARECA-SAS-CARD1-MIB", "eventString")
)
if mibBuilder.loadTexts:
    rsDelete.setStatus(
        ""
    )

rsExpand = NotificationType(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 7, 0, 130)
)
rsExpand.setObjects(
    ("ARECA-SAS-CARD1-MIB", "eventString")
)
if mibBuilder.loadTexts:
    rsExpand.setStatus(
        ""
    )

rsRebuild = NotificationType(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 7, 0, 131)
)
rsRebuild.setObjects(
    ("ARECA-SAS-CARD1-MIB", "eventString")
)
if mibBuilder.loadTexts:
    rsRebuild.setStatus(
        ""
    )

rsDegraded = NotificationType(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 7, 0, 132)
)
rsDegraded.setObjects(
    ("ARECA-SAS-CARD1-MIB", "eventString")
)
if mibBuilder.loadTexts:
    rsDegraded.setStatus(
        ""
    )

rsNoEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 7, 0, 133)
)
rsNoEvent.setObjects(
    ("ARECA-SAS-CARD1-MIB", "eventString")
)
if mibBuilder.loadTexts:
    rsNoEvent.setStatus(
        ""
    )

vsInitializing = NotificationType(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 7, 0, 256)
)
vsInitializing.setObjects(
    ("ARECA-SAS-CARD1-MIB", "eventString")
)
if mibBuilder.loadTexts:
    vsInitializing.setStatus(
        ""
    )

vsRebuilding = NotificationType(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 7, 0, 257)
)
vsRebuilding.setObjects(
    ("ARECA-SAS-CARD1-MIB", "eventString")
)
if mibBuilder.loadTexts:
    vsRebuilding.setStatus(
        ""
    )

vsMigrating = NotificationType(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 7, 0, 258)
)
vsMigrating.setObjects(
    ("ARECA-SAS-CARD1-MIB", "eventString")
)
if mibBuilder.loadTexts:
    vsMigrating.setStatus(
        ""
    )

vsChecking = NotificationType(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 7, 0, 259)
)
vsChecking.setObjects(
    ("ARECA-SAS-CARD1-MIB", "eventString")
)
if mibBuilder.loadTexts:
    vsChecking.setStatus(
        ""
    )

vsCompleteInit = NotificationType(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 7, 0, 260)
)
vsCompleteInit.setObjects(
    ("ARECA-SAS-CARD1-MIB", "eventString")
)
if mibBuilder.loadTexts:
    vsCompleteInit.setStatus(
        ""
    )

vsCompleteRebuild = NotificationType(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 7, 0, 261)
)
vsCompleteRebuild.setObjects(
    ("ARECA-SAS-CARD1-MIB", "eventString")
)
if mibBuilder.loadTexts:
    vsCompleteRebuild.setStatus(
        ""
    )

vsCompleteMigrating = NotificationType(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 7, 0, 262)
)
vsCompleteMigrating.setObjects(
    ("ARECA-SAS-CARD1-MIB", "eventString")
)
if mibBuilder.loadTexts:
    vsCompleteMigrating.setStatus(
        ""
    )

vsCompleteChecking = NotificationType(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 7, 0, 263)
)
vsCompleteChecking.setObjects(
    ("ARECA-SAS-CARD1-MIB", "eventString")
)
if mibBuilder.loadTexts:
    vsCompleteChecking.setStatus(
        ""
    )

vsCreate = NotificationType(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 7, 0, 264)
)
vsCreate.setObjects(
    ("ARECA-SAS-CARD1-MIB", "eventString")
)
if mibBuilder.loadTexts:
    vsCreate.setStatus(
        ""
    )

vsDelete = NotificationType(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 7, 0, 265)
)
vsDelete.setObjects(
    ("ARECA-SAS-CARD1-MIB", "eventString")
)
if mibBuilder.loadTexts:
    vsDelete.setStatus(
        ""
    )

vsModify = NotificationType(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 7, 0, 266)
)
vsModify.setObjects(
    ("ARECA-SAS-CARD1-MIB", "eventString")
)
if mibBuilder.loadTexts:
    vsModify.setStatus(
        ""
    )

vsDegraded = NotificationType(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 7, 0, 267)
)
vsDegraded.setObjects(
    ("ARECA-SAS-CARD1-MIB", "eventString")
)
if mibBuilder.loadTexts:
    vsDegraded.setStatus(
        ""
    )

vsFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 7, 0, 268)
)
vsFailed.setObjects(
    ("ARECA-SAS-CARD1-MIB", "eventString")
)
if mibBuilder.loadTexts:
    vsFailed.setStatus(
        ""
    )

vsRevived = NotificationType(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 7, 0, 269)
)
vsRevived.setObjects(
    ("ARECA-SAS-CARD1-MIB", "eventString")
)
if mibBuilder.loadTexts:
    vsRevived.setStatus(
        ""
    )

vsTotals = NotificationType(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 7, 0, 270)
)
vsTotals.setObjects(
    ("ARECA-SAS-CARD1-MIB", "eventString")
)
if mibBuilder.loadTexts:
    vsTotals.setStatus(
        ""
    )

pdAdded = NotificationType(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 7, 0, 384)
)
pdAdded.setObjects(
    ("ARECA-SAS-CARD1-MIB", "eventString")
)
if mibBuilder.loadTexts:
    pdAdded.setStatus(
        ""
    )

pdRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 7, 0, 385)
)
pdRemoved.setObjects(
    ("ARECA-SAS-CARD1-MIB", "eventString")
)
if mibBuilder.loadTexts:
    pdRemoved.setStatus(
        ""
    )

pdReadError = NotificationType(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 7, 0, 386)
)
pdReadError.setObjects(
    ("ARECA-SAS-CARD1-MIB", "eventString")
)
if mibBuilder.loadTexts:
    pdReadError.setStatus(
        ""
    )

pdWriteError = NotificationType(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 7, 0, 387)
)
pdWriteError.setObjects(
    ("ARECA-SAS-CARD1-MIB", "eventString")
)
if mibBuilder.loadTexts:
    pdWriteError.setStatus(
        ""
    )

pdAtaEccError = NotificationType(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 7, 0, 388)
)
pdAtaEccError.setObjects(
    ("ARECA-SAS-CARD1-MIB", "eventString")
)
if mibBuilder.loadTexts:
    pdAtaEccError.setStatus(
        ""
    )

pdAtaChangeMode = NotificationType(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 7, 0, 389)
)
pdAtaChangeMode.setObjects(
    ("ARECA-SAS-CARD1-MIB", "eventString")
)
if mibBuilder.loadTexts:
    pdAtaChangeMode.setStatus(
        ""
    )

pdTimeOut = NotificationType(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 7, 0, 390)
)
pdTimeOut.setObjects(
    ("ARECA-SAS-CARD1-MIB", "eventString")
)
if mibBuilder.loadTexts:
    pdTimeOut.setStatus(
        ""
    )

pdMarkFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 7, 0, 391)
)
pdMarkFailed.setObjects(
    ("ARECA-SAS-CARD1-MIB", "eventString")
)
if mibBuilder.loadTexts:
    pdMarkFailed.setStatus(
        ""
    )

pdPciError = NotificationType(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 7, 0, 392)
)
pdPciError.setObjects(
    ("ARECA-SAS-CARD1-MIB", "eventString")
)
if mibBuilder.loadTexts:
    pdPciError.setStatus(
        ""
    )

pdSmartFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 7, 0, 393)
)
pdSmartFailed.setObjects(
    ("ARECA-SAS-CARD1-MIB", "eventString")
)
if mibBuilder.loadTexts:
    pdSmartFailed.setStatus(
        ""
    )

pdCreatePass = NotificationType(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 7, 0, 394)
)
pdCreatePass.setObjects(
    ("ARECA-SAS-CARD1-MIB", "eventString")
)
if mibBuilder.loadTexts:
    pdCreatePass.setStatus(
        ""
    )

pdModifyPass = NotificationType(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 7, 0, 395)
)
pdModifyPass.setObjects(
    ("ARECA-SAS-CARD1-MIB", "eventString")
)
if mibBuilder.loadTexts:
    pdModifyPass.setStatus(
        ""
    )

pdDeletePass = NotificationType(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 7, 0, 396)
)
pdDeletePass.setObjects(
    ("ARECA-SAS-CARD1-MIB", "eventString")
)
if mibBuilder.loadTexts:
    pdDeletePass.setStatus(
        ""
    )

pdTotals = NotificationType(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 7, 0, 397)
)
pdTotals.setObjects(
    ("ARECA-SAS-CARD1-MIB", "eventString")
)
if mibBuilder.loadTexts:
    pdTotals.setStatus(
        ""
    )

scsiReset = NotificationType(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 7, 0, 512)
)
scsiReset.setObjects(
    ("ARECA-SAS-CARD1-MIB", "eventString")
)
if mibBuilder.loadTexts:
    scsiReset.setStatus(
        ""
    )

scsiParity = NotificationType(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 7, 0, 513)
)
scsiParity.setObjects(
    ("ARECA-SAS-CARD1-MIB", "eventString")
)
if mibBuilder.loadTexts:
    scsiParity.setStatus(
        ""
    )

scsiModeChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 7, 0, 514)
)
scsiModeChange.setObjects(
    ("ARECA-SAS-CARD1-MIB", "eventString")
)
if mibBuilder.loadTexts:
    scsiModeChange.setStatus(
        ""
    )

scsiTotals = NotificationType(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 7, 0, 515)
)
scsiTotals.setObjects(
    ("ARECA-SAS-CARD1-MIB", "eventString")
)
if mibBuilder.loadTexts:
    scsiTotals.setStatus(
        ""
    )

hwSdram1BitEcc = NotificationType(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 7, 0, 640)
)
hwSdram1BitEcc.setObjects(
    ("ARECA-SAS-CARD1-MIB", "eventString")
)
if mibBuilder.loadTexts:
    hwSdram1BitEcc.setStatus(
        ""
    )

hwSdramMultiBitEcc = NotificationType(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 7, 0, 641)
)
hwSdramMultiBitEcc.setObjects(
    ("ARECA-SAS-CARD1-MIB", "eventString")
)
if mibBuilder.loadTexts:
    hwSdramMultiBitEcc.setStatus(
        ""
    )

hwTempController = NotificationType(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 7, 0, 642)
)
hwTempController.setObjects(
    ("ARECA-SAS-CARD1-MIB", "eventString")
)
if mibBuilder.loadTexts:
    hwTempController.setStatus(
        ""
    )

hwTempBackplane = NotificationType(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 7, 0, 643)
)
hwTempBackplane.setObjects(
    ("ARECA-SAS-CARD1-MIB", "eventString")
)
if mibBuilder.loadTexts:
    hwTempBackplane.setStatus(
        ""
    )

hwVoltage15 = NotificationType(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 7, 0, 644)
)
hwVoltage15.setObjects(
    ("ARECA-SAS-CARD1-MIB", "eventString")
)
if mibBuilder.loadTexts:
    hwVoltage15.setStatus(
        ""
    )

hwVoltage3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 7, 0, 645)
)
hwVoltage3.setObjects(
    ("ARECA-SAS-CARD1-MIB", "eventString")
)
if mibBuilder.loadTexts:
    hwVoltage3.setStatus(
        ""
    )

hwVoltage5 = NotificationType(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 7, 0, 646)
)
hwVoltage5.setObjects(
    ("ARECA-SAS-CARD1-MIB", "eventString")
)
if mibBuilder.loadTexts:
    hwVoltage5.setStatus(
        ""
    )

hwVoltage12 = NotificationType(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 7, 0, 647)
)
hwVoltage12.setObjects(
    ("ARECA-SAS-CARD1-MIB", "eventString")
)
if mibBuilder.loadTexts:
    hwVoltage12.setStatus(
        ""
    )

hwVoltage13 = NotificationType(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 7, 0, 648)
)
hwVoltage13.setObjects(
    ("ARECA-SAS-CARD1-MIB", "eventString")
)
if mibBuilder.loadTexts:
    hwVoltage13.setStatus(
        ""
    )

hwVoltage25 = NotificationType(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 7, 0, 649)
)
hwVoltage25.setObjects(
    ("ARECA-SAS-CARD1-MIB", "eventString")
)
if mibBuilder.loadTexts:
    hwVoltage25.setStatus(
        ""
    )

hwVoltage125 = NotificationType(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 7, 0, 650)
)
hwVoltage125.setObjects(
    ("ARECA-SAS-CARD1-MIB", "eventString")
)
if mibBuilder.loadTexts:
    hwVoltage125.setStatus(
        ""
    )

hwPower1Failed = NotificationType(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 7, 0, 651)
)
hwPower1Failed.setObjects(
    ("ARECA-SAS-CARD1-MIB", "eventString")
)
if mibBuilder.loadTexts:
    hwPower1Failed.setStatus(
        ""
    )

hwFan1Failed = NotificationType(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 7, 0, 652)
)
hwFan1Failed.setObjects(
    ("ARECA-SAS-CARD1-MIB", "eventString")
)
if mibBuilder.loadTexts:
    hwFan1Failed.setStatus(
        ""
    )

hwPower2Failed = NotificationType(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 7, 0, 653)
)
hwPower2Failed.setObjects(
    ("ARECA-SAS-CARD1-MIB", "eventString")
)
if mibBuilder.loadTexts:
    hwPower2Failed.setStatus(
        ""
    )

hwFan2Failed = NotificationType(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 7, 0, 654)
)
hwFan2Failed.setObjects(
    ("ARECA-SAS-CARD1-MIB", "eventString")
)
if mibBuilder.loadTexts:
    hwFan2Failed.setStatus(
        ""
    )

hwPower3Failed = NotificationType(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 7, 0, 655)
)
hwPower3Failed.setObjects(
    ("ARECA-SAS-CARD1-MIB", "eventString")
)
if mibBuilder.loadTexts:
    hwPower3Failed.setStatus(
        ""
    )

hwFan3Failed = NotificationType(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 7, 0, 656)
)
hwFan3Failed.setObjects(
    ("ARECA-SAS-CARD1-MIB", "eventString")
)
if mibBuilder.loadTexts:
    hwFan3Failed.setStatus(
        ""
    )

hwPower4Failed = NotificationType(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 7, 0, 657)
)
hwPower4Failed.setObjects(
    ("ARECA-SAS-CARD1-MIB", "eventString")
)
if mibBuilder.loadTexts:
    hwPower4Failed.setStatus(
        ""
    )

hwFan4Failed = NotificationType(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 7, 0, 658)
)
hwFan4Failed.setObjects(
    ("ARECA-SAS-CARD1-MIB", "eventString")
)
if mibBuilder.loadTexts:
    hwFan4Failed.setStatus(
        ""
    )

hwUpsPowerLoss = NotificationType(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 7, 0, 659)
)
hwUpsPowerLoss.setObjects(
    ("ARECA-SAS-CARD1-MIB", "eventString")
)
if mibBuilder.loadTexts:
    hwUpsPowerLoss.setStatus(
        ""
    )

hwTempControllerR = NotificationType(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 7, 0, 660)
)
hwTempControllerR.setObjects(
    ("ARECA-SAS-CARD1-MIB", "eventString")
)
if mibBuilder.loadTexts:
    hwTempControllerR.setStatus(
        ""
    )

hwTempBackplaneR = NotificationType(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 7, 0, 661)
)
hwTempBackplaneR.setObjects(
    ("ARECA-SAS-CARD1-MIB", "eventString")
)
if mibBuilder.loadTexts:
    hwTempBackplaneR.setStatus(
        ""
    )

hwVoltage15R = NotificationType(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 7, 0, 662)
)
hwVoltage15R.setObjects(
    ("ARECA-SAS-CARD1-MIB", "eventString")
)
if mibBuilder.loadTexts:
    hwVoltage15R.setStatus(
        ""
    )

hwVoltage3R = NotificationType(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 7, 0, 663)
)
hwVoltage3R.setObjects(
    ("ARECA-SAS-CARD1-MIB", "eventString")
)
if mibBuilder.loadTexts:
    hwVoltage3R.setStatus(
        ""
    )

hwVoltage5R = NotificationType(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 7, 0, 664)
)
hwVoltage5R.setObjects(
    ("ARECA-SAS-CARD1-MIB", "eventString")
)
if mibBuilder.loadTexts:
    hwVoltage5R.setStatus(
        ""
    )

hwVoltage12R = NotificationType(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 7, 0, 665)
)
hwVoltage12R.setObjects(
    ("ARECA-SAS-CARD1-MIB", "eventString")
)
if mibBuilder.loadTexts:
    hwVoltage12R.setStatus(
        ""
    )

hwVoltage13R = NotificationType(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 7, 0, 666)
)
hwVoltage13R.setObjects(
    ("ARECA-SAS-CARD1-MIB", "eventString")
)
if mibBuilder.loadTexts:
    hwVoltage13R.setStatus(
        ""
    )

hwVoltage25R = NotificationType(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 7, 0, 667)
)
hwVoltage25R.setObjects(
    ("ARECA-SAS-CARD1-MIB", "eventString")
)
if mibBuilder.loadTexts:
    hwVoltage25R.setStatus(
        ""
    )

hwVoltage125R = NotificationType(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 7, 0, 668)
)
hwVoltage125R.setObjects(
    ("ARECA-SAS-CARD1-MIB", "eventString")
)
if mibBuilder.loadTexts:
    hwVoltage125R.setStatus(
        ""
    )

hwPower1FailedR = NotificationType(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 7, 0, 669)
)
hwPower1FailedR.setObjects(
    ("ARECA-SAS-CARD1-MIB", "eventString")
)
if mibBuilder.loadTexts:
    hwPower1FailedR.setStatus(
        ""
    )

hwFan1FailedR = NotificationType(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 7, 0, 670)
)
hwFan1FailedR.setObjects(
    ("ARECA-SAS-CARD1-MIB", "eventString")
)
if mibBuilder.loadTexts:
    hwFan1FailedR.setStatus(
        ""
    )

hwPower2FailedR = NotificationType(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 7, 0, 671)
)
hwPower2FailedR.setObjects(
    ("ARECA-SAS-CARD1-MIB", "eventString")
)
if mibBuilder.loadTexts:
    hwPower2FailedR.setStatus(
        ""
    )

hwFan2FailedR = NotificationType(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 7, 0, 672)
)
hwFan2FailedR.setObjects(
    ("ARECA-SAS-CARD1-MIB", "eventString")
)
if mibBuilder.loadTexts:
    hwFan2FailedR.setStatus(
        ""
    )

hwPower3FailedR = NotificationType(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 7, 0, 673)
)
hwPower3FailedR.setObjects(
    ("ARECA-SAS-CARD1-MIB", "eventString")
)
if mibBuilder.loadTexts:
    hwPower3FailedR.setStatus(
        ""
    )

hwFan3FailedR = NotificationType(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 7, 0, 674)
)
hwFan3FailedR.setObjects(
    ("ARECA-SAS-CARD1-MIB", "eventString")
)
if mibBuilder.loadTexts:
    hwFan3FailedR.setStatus(
        ""
    )

hwPower4FailedR = NotificationType(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 7, 0, 675)
)
hwPower4FailedR.setObjects(
    ("ARECA-SAS-CARD1-MIB", "eventString")
)
if mibBuilder.loadTexts:
    hwPower4FailedR.setStatus(
        ""
    )

hwFan4FailedR = NotificationType(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 7, 0, 676)
)
hwFan4FailedR.setObjects(
    ("ARECA-SAS-CARD1-MIB", "eventString")
)
if mibBuilder.loadTexts:
    hwFan4FailedR.setStatus(
        ""
    )

hwUPSPowerR = NotificationType(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 7, 0, 677)
)
hwUPSPowerR.setObjects(
    ("ARECA-SAS-CARD1-MIB", "eventString")
)
if mibBuilder.loadTexts:
    hwUPSPowerR.setStatus(
        ""
    )

hwSystemRestarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 7, 0, 678)
)
hwSystemRestarted.setObjects(
    ("ARECA-SAS-CARD1-MIB", "eventString")
)
if mibBuilder.loadTexts:
    hwSystemRestarted.setStatus(
        ""
    )

hwTest = NotificationType(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 7, 0, 679)
)
hwTest.setObjects(
    ("ARECA-SAS-CARD1-MIB", "eventString")
)
if mibBuilder.loadTexts:
    hwTest.setStatus(
        ""
    )

hwSystemRecovered = NotificationType(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 7, 0, 680)
)
hwSystemRecovered.setObjects(
    ("ARECA-SAS-CARD1-MIB", "eventString")
)
if mibBuilder.loadTexts:
    hwSystemRecovered.setStatus(
        ""
    )

ghmRecover = NotificationType(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 7, 0, 768)
)
ghmRecover.setObjects(
    ("ARECA-SAS-CARD1-MIB", "eventString")
)
if mibBuilder.loadTexts:
    ghmRecover.setStatus(
        ""
    )

ghmOverTemp = NotificationType(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 7, 0, 769)
)
ghmOverTemp.setObjects(
    ("ARECA-SAS-CARD1-MIB", "eventString")
)
if mibBuilder.loadTexts:
    ghmOverTemp.setStatus(
        ""
    )

ghmFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 7, 0, 770)
)
ghmFailed.setObjects(
    ("ARECA-SAS-CARD1-MIB", "eventString")
)
if mibBuilder.loadTexts:
    ghmFailed.setStatus(
        ""
    )

ghmUnderVoltage = NotificationType(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 7, 0, 771)
)
ghmUnderVoltage.setObjects(
    ("ARECA-SAS-CARD1-MIB", "eventString")
)
if mibBuilder.loadTexts:
    ghmUnderVoltage.setStatus(
        ""
    )

ghmOverVoltage = NotificationType(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 7, 0, 772)
)
ghmOverVoltage.setObjects(
    ("ARECA-SAS-CARD1-MIB", "eventString")
)
if mibBuilder.loadTexts:
    ghmOverVoltage.setStatus(
        ""
    )

ghmDiscovered = NotificationType(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 7, 0, 773)
)
ghmDiscovered.setObjects(
    ("ARECA-SAS-CARD1-MIB", "eventString")
)
if mibBuilder.loadTexts:
    ghmDiscovered.setStatus(
        ""
    )

ghmLostMig = NotificationType(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 7, 0, 774)
)
ghmLostMig.setObjects(
    ("ARECA-SAS-CARD1-MIB", "eventString")
)
if mibBuilder.loadTexts:
    ghmLostMig.setStatus(
        ""
    )

ghmRestartLBA = NotificationType(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 7, 0, 775)
)
ghmRestartLBA.setObjects(
    ("ARECA-SAS-CARD1-MIB", "eventString")
)
if mibBuilder.loadTexts:
    ghmRestartLBA.setStatus(
        ""
    )

ghmHTTPLogin = NotificationType(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 7, 0, 776)
)
ghmHTTPLogin.setObjects(
    ("ARECA-SAS-CARD1-MIB", "eventString")
)
if mibBuilder.loadTexts:
    ghmHTTPLogin.setStatus(
        ""
    )

ghmTelnetLogin = NotificationType(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 7, 0, 777)
)
ghmTelnetLogin.setObjects(
    ("ARECA-SAS-CARD1-MIB", "eventString")
)
if mibBuilder.loadTexts:
    ghmTelnetLogin.setStatus(
        ""
    )

ghmVt100Login = NotificationType(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 7, 0, 778)
)
ghmVt100Login.setObjects(
    ("ARECA-SAS-CARD1-MIB", "eventString")
)
if mibBuilder.loadTexts:
    ghmVt100Login.setStatus(
        ""
    )

ghmGUILogin = NotificationType(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 7, 0, 779)
)
ghmGUILogin.setObjects(
    ("ARECA-SAS-CARD1-MIB", "eventString")
)
if mibBuilder.loadTexts:
    ghmGUILogin.setStatus(
        ""
    )

ghmFCLinkUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 7, 0, 780)
)
ghmFCLinkUp.setObjects(
    ("ARECA-SAS-CARD1-MIB", "eventString")
)
if mibBuilder.loadTexts:
    ghmFCLinkUp.setStatus(
        ""
    )

ghmFCLinkDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 7, 0, 781)
)
ghmFCLinkDown.setObjects(
    ("ARECA-SAS-CARD1-MIB", "eventString")
)
if mibBuilder.loadTexts:
    ghmFCLinkDown.setStatus(
        ""
    )

ghm16BytesCDB = NotificationType(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 7, 0, 782)
)
ghm16BytesCDB.setObjects(
    ("ARECA-SAS-CARD1-MIB", "eventString")
)
if mibBuilder.loadTexts:
    ghm16BytesCDB.setStatus(
        ""
    )

ghmInitLBA = NotificationType(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 7, 0, 783)
)
ghmInitLBA.setObjects(
    ("ARECA-SAS-CARD1-MIB", "eventString")
)
if mibBuilder.loadTexts:
    ghmInitLBA.setStatus(
        ""
    )

ghmRebuildLBA = NotificationType(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 7, 0, 784)
)
ghmRebuildLBA.setObjects(
    ("ARECA-SAS-CARD1-MIB", "eventString")
)
if mibBuilder.loadTexts:
    ghmRebuildLBA.setStatus(
        ""
    )

ghmMigrateLBA = NotificationType(
    (1, 3, 6, 1, 4, 1, 18928, 1, 129, 7, 0, 785)
)
ghmMigrateLBA.setObjects(
    ("ARECA-SAS-CARD1-MIB", "eventString")
)
if mibBuilder.loadTexts:
    ghmMigrateLBA.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ARECA-SAS-CARD1-MIB",
    **{"areca": areca,
       "arecaGroup1": arecaGroup1,
       "sasRaidCard1": sasRaidCard1,
       "systemInformation": systemInformation,
       "siVendor": siVendor,
       "siModel": siModel,
       "siSerial": siSerial,
       "siFirmVer": siFirmVer,
       "siBootVer": siBootVer,
       "siMbrVer": siMbrVer,
       "siProcessor": siProcessor,
       "siCpuSpeed": siCpuSpeed,
       "siICache": siICache,
       "siDCache": siDCache,
       "siSCache": siSCache,
       "siMemory": siMemory,
       "siMemSpeed": siMemSpeed,
       "siEcc": siEcc,
       "siHosts": siHosts,
       "siRaidSets": siRaidSets,
       "siVolumeSets": siVolumeSets,
       "siEvents": siEvents,
       "siRaid6": siRaid6,
       "siDhcp": siDhcp,
       "siBeeper": siBeeper,
       "siUsage": siUsage,
       "siRebuildRate": siRebuildRate,
       "siBaudRate": siBaudRate,
       "hwMonitor": hwMonitor,
       "controllerBoard": controllerBoard,
       "hwControllerBoardInstalled": hwControllerBoardInstalled,
       "hwControllerBoardDescription": hwControllerBoardDescription,
       "hwControllerBoardNumberOfPower": hwControllerBoardNumberOfPower,
       "hwControllerBoardNumberOfVol": hwControllerBoardNumberOfVol,
       "hwControllerBoardNumberOfFan": hwControllerBoardNumberOfFan,
       "hwControllerBoardNumberOfTemp": hwControllerBoardNumberOfTemp,
       "hwControllerBoardPowerTable": hwControllerBoardPowerTable,
       "hwControllerBoardPowerEntry": hwControllerBoardPowerEntry,
       "hwControllerBoardPowerIndex": hwControllerBoardPowerIndex,
       "hwControllerBoardPowerDesc": hwControllerBoardPowerDesc,
       "hwControllerBoardPowerState": hwControllerBoardPowerState,
       "hwControllerBoardVolTable": hwControllerBoardVolTable,
       "hwControllerBoardVolEntry": hwControllerBoardVolEntry,
       "hwControllerBoardVolIndex": hwControllerBoardVolIndex,
       "hwControllerBoardVolDesc": hwControllerBoardVolDesc,
       "hwControllerBoardVolValue": hwControllerBoardVolValue,
       "hwControllerBoardFanTable": hwControllerBoardFanTable,
       "hwControllerBoardFanEntry": hwControllerBoardFanEntry,
       "hwControllerBoardFanIndex": hwControllerBoardFanIndex,
       "hwControllerBoardFanDesc": hwControllerBoardFanDesc,
       "hwControllerBoardFanSpeed": hwControllerBoardFanSpeed,
       "hwControllerBoardTempTable": hwControllerBoardTempTable,
       "hwControllerBoardTempEntry": hwControllerBoardTempEntry,
       "hwControllerBoardTempIndex": hwControllerBoardTempIndex,
       "hwControllerBoardTempDesc": hwControllerBoardTempDesc,
       "hwControllerBoardTempValue": hwControllerBoardTempValue,
       "hwEnclosure1": hwEnclosure1,
       "hwEnclosure01Installed": hwEnclosure01Installed,
       "hwEnclosure01Description": hwEnclosure01Description,
       "hwEnclosure01NumberOfPower": hwEnclosure01NumberOfPower,
       "hwEnclosure01NumberOfVol": hwEnclosure01NumberOfVol,
       "hwEnclosure01NumberOfFan": hwEnclosure01NumberOfFan,
       "hwEnclosure01NumberOfTemp": hwEnclosure01NumberOfTemp,
       "hwEnclosure01PowerTable": hwEnclosure01PowerTable,
       "hwEnclosure01PowerEntry": hwEnclosure01PowerEntry,
       "hwEnclosure01PowerIndex": hwEnclosure01PowerIndex,
       "hwEnclosure01PowerDesc": hwEnclosure01PowerDesc,
       "hwEnclosure01PowerState": hwEnclosure01PowerState,
       "hwEnclosure01VolTable": hwEnclosure01VolTable,
       "hwEnclosure01VolEntry": hwEnclosure01VolEntry,
       "hwEnclosure01VolIndex": hwEnclosure01VolIndex,
       "hwEnclosure01VolDesc": hwEnclosure01VolDesc,
       "hwEnclosure01VolValue": hwEnclosure01VolValue,
       "hwEnclosure01FanTable": hwEnclosure01FanTable,
       "hwEnclosure01FanEntry": hwEnclosure01FanEntry,
       "hwEnclosure01FanIndex": hwEnclosure01FanIndex,
       "hwEnclosure01FanDesc": hwEnclosure01FanDesc,
       "hwEnclosure01FanSpeed": hwEnclosure01FanSpeed,
       "hwEnclosure01TempTable": hwEnclosure01TempTable,
       "hwEnclosure01TempEntry": hwEnclosure01TempEntry,
       "hwEnclosure01TempIndex": hwEnclosure01TempIndex,
       "hwEnclosure01TempDesc": hwEnclosure01TempDesc,
       "hwEnclosure01TempValue": hwEnclosure01TempValue,
       "hwEnclosure2": hwEnclosure2,
       "hwEnclosure02Installed": hwEnclosure02Installed,
       "hwEnclosure02Description": hwEnclosure02Description,
       "hwEnclosure02NumberOfPower": hwEnclosure02NumberOfPower,
       "hwEnclosure02NumberOfVol": hwEnclosure02NumberOfVol,
       "hwEnclosure02NumberOfFan": hwEnclosure02NumberOfFan,
       "hwEnclosure02NumberOfTemp": hwEnclosure02NumberOfTemp,
       "hwEnclosure02PowerTable": hwEnclosure02PowerTable,
       "hwEnclosure02PowerEntry": hwEnclosure02PowerEntry,
       "hwEnclosure02PowerIndex": hwEnclosure02PowerIndex,
       "hwEnclosure02PowerDesc": hwEnclosure02PowerDesc,
       "hwEnclosure02PowerState": hwEnclosure02PowerState,
       "hwEnclosure02VolTable": hwEnclosure02VolTable,
       "hwEnclosure02VolEntry": hwEnclosure02VolEntry,
       "hwEnclosure02VolIndex": hwEnclosure02VolIndex,
       "hwEnclosure02VolDesc": hwEnclosure02VolDesc,
       "hwEnclosure02VolValue": hwEnclosure02VolValue,
       "hwEnclosure02FanTable": hwEnclosure02FanTable,
       "hwEnclosure02FanEntry": hwEnclosure02FanEntry,
       "hwEnclosure02FanIndex": hwEnclosure02FanIndex,
       "hwEnclosure02FanDesc": hwEnclosure02FanDesc,
       "hwEnclosure02FanSpeed": hwEnclosure02FanSpeed,
       "hwEnclosure02TempTable": hwEnclosure02TempTable,
       "hwEnclosure02TempEntry": hwEnclosure02TempEntry,
       "hwEnclosure02TempIndex": hwEnclosure02TempIndex,
       "hwEnclosure02TempDesc": hwEnclosure02TempDesc,
       "hwEnclosure02TempValue": hwEnclosure02TempValue,
       "hwEnclosure3": hwEnclosure3,
       "hwEnclosure03Installed": hwEnclosure03Installed,
       "hwEnclosure03Description": hwEnclosure03Description,
       "hwEnclosure03NumberOfPower": hwEnclosure03NumberOfPower,
       "hwEnclosure03NumberOfVol": hwEnclosure03NumberOfVol,
       "hwEnclosure03NumberOfFan": hwEnclosure03NumberOfFan,
       "hwEnclosure03NumberOfTemp": hwEnclosure03NumberOfTemp,
       "hwEnclosure03PowerTable": hwEnclosure03PowerTable,
       "hwEnclosure03PowerEntry": hwEnclosure03PowerEntry,
       "hwEnclosure03PowerIndex": hwEnclosure03PowerIndex,
       "hwEnclosure03PowerDesc": hwEnclosure03PowerDesc,
       "hwEnclosure03PowerState": hwEnclosure03PowerState,
       "hwEnclosure03VolTable": hwEnclosure03VolTable,
       "hwEnclosure03VolEntry": hwEnclosure03VolEntry,
       "hwEnclosure03VolIndex": hwEnclosure03VolIndex,
       "hwEnclosure03VolDesc": hwEnclosure03VolDesc,
       "hwEnclosure03VolValue": hwEnclosure03VolValue,
       "hwEnclosure03FanTable": hwEnclosure03FanTable,
       "hwEnclosure03FanEntry": hwEnclosure03FanEntry,
       "hwEnclosure03FanIndex": hwEnclosure03FanIndex,
       "hwEnclosure03FanDesc": hwEnclosure03FanDesc,
       "hwEnclosure03FanSpeed": hwEnclosure03FanSpeed,
       "hwEnclosure03TempTable": hwEnclosure03TempTable,
       "hwEnclosure03TempEntry": hwEnclosure03TempEntry,
       "hwEnclosure03TempIndex": hwEnclosure03TempIndex,
       "hwEnclosure03TempDesc": hwEnclosure03TempDesc,
       "hwEnclosure03TempValue": hwEnclosure03TempValue,
       "hwEnclosure4": hwEnclosure4,
       "hwEnclosure04Installed": hwEnclosure04Installed,
       "hwEnclosure04Description": hwEnclosure04Description,
       "hwEnclosure04NumberOfPower": hwEnclosure04NumberOfPower,
       "hwEnclosure04NumberOfVol": hwEnclosure04NumberOfVol,
       "hwEnclosure04NumberOfFan": hwEnclosure04NumberOfFan,
       "hwEnclosure04NumberOfTemp": hwEnclosure04NumberOfTemp,
       "hwEnclosure04PowerTable": hwEnclosure04PowerTable,
       "hwEnclosure04PowerEntry": hwEnclosure04PowerEntry,
       "hwEnclosure04PowerIndex": hwEnclosure04PowerIndex,
       "hwEnclosure04PowerDesc": hwEnclosure04PowerDesc,
       "hwEnclosure04PowerState": hwEnclosure04PowerState,
       "hwEnclosure04VolTable": hwEnclosure04VolTable,
       "hwEnclosure04VolEntry": hwEnclosure04VolEntry,
       "hwEnclosure04VolIndex": hwEnclosure04VolIndex,
       "hwEnclosure04VolDesc": hwEnclosure04VolDesc,
       "hwEnclosure04VolValue": hwEnclosure04VolValue,
       "hwEnclosure04FanTable": hwEnclosure04FanTable,
       "hwEnclosure04FanEntry": hwEnclosure04FanEntry,
       "hwEnclosure04FanIndex": hwEnclosure04FanIndex,
       "hwEnclosure04FanDesc": hwEnclosure04FanDesc,
       "hwEnclosure04FanSpeed": hwEnclosure04FanSpeed,
       "hwEnclosure04TempTable": hwEnclosure04TempTable,
       "hwEnclosure04TempEntry": hwEnclosure04TempEntry,
       "hwEnclosure04TempIndex": hwEnclosure04TempIndex,
       "hwEnclosure04TempDesc": hwEnclosure04TempDesc,
       "hwEnclosure04TempValue": hwEnclosure04TempValue,
       "hwEnclosure5": hwEnclosure5,
       "hwEnclosure05Installed": hwEnclosure05Installed,
       "hwEnclosure05Description": hwEnclosure05Description,
       "hwEnclosure05NumberOfPower": hwEnclosure05NumberOfPower,
       "hwEnclosure05NumberOfVol": hwEnclosure05NumberOfVol,
       "hwEnclosure05NumberOfFan": hwEnclosure05NumberOfFan,
       "hwEnclosure05NumberOfTemp": hwEnclosure05NumberOfTemp,
       "hwEnclosure05PowerTable": hwEnclosure05PowerTable,
       "hwEnclosure05PowerEntry": hwEnclosure05PowerEntry,
       "hwEnclosure05PowerIndex": hwEnclosure05PowerIndex,
       "hwEnclosure05PowerDesc": hwEnclosure05PowerDesc,
       "hwEnclosure05PowerState": hwEnclosure05PowerState,
       "hwEnclosure05VolTable": hwEnclosure05VolTable,
       "hwEnclosure05VolEntry": hwEnclosure05VolEntry,
       "hwEnclosure05VolIndex": hwEnclosure05VolIndex,
       "hwEnclosure05VolDesc": hwEnclosure05VolDesc,
       "hwEnclosure05VolValue": hwEnclosure05VolValue,
       "hwEnclosure05FanTable": hwEnclosure05FanTable,
       "hwEnclosure05FanEntry": hwEnclosure05FanEntry,
       "hwEnclosure05FanIndex": hwEnclosure05FanIndex,
       "hwEnclosure05FanDesc": hwEnclosure05FanDesc,
       "hwEnclosure05FanSpeed": hwEnclosure05FanSpeed,
       "hwEnclosure05TempTable": hwEnclosure05TempTable,
       "hwEnclosure05TempEntry": hwEnclosure05TempEntry,
       "hwEnclosure05TempIndex": hwEnclosure05TempIndex,
       "hwEnclosure05TempDesc": hwEnclosure05TempDesc,
       "hwEnclosure05TempValue": hwEnclosure05TempValue,
       "hwEnclosure6": hwEnclosure6,
       "hwEnclosure06Installed": hwEnclosure06Installed,
       "hwEnclosure06Description": hwEnclosure06Description,
       "hwEnclosure06NumberOfPower": hwEnclosure06NumberOfPower,
       "hwEnclosure06NumberOfVol": hwEnclosure06NumberOfVol,
       "hwEnclosure06NumberOfFan": hwEnclosure06NumberOfFan,
       "hwEnclosure06NumberOfTemp": hwEnclosure06NumberOfTemp,
       "hwEnclosure06PowerTable": hwEnclosure06PowerTable,
       "hwEnclosure06PowerEntry": hwEnclosure06PowerEntry,
       "hwEnclosure06PowerIndex": hwEnclosure06PowerIndex,
       "hwEnclosure06PowerDesc": hwEnclosure06PowerDesc,
       "hwEnclosure06PowerState": hwEnclosure06PowerState,
       "hwEnclosure06VolTable": hwEnclosure06VolTable,
       "hwEnclosure06VolEntry": hwEnclosure06VolEntry,
       "hwEnclosure06VolIndex": hwEnclosure06VolIndex,
       "hwEnclosure06VolDesc": hwEnclosure06VolDesc,
       "hwEnclosure06VolValue": hwEnclosure06VolValue,
       "hwEnclosure06FanTable": hwEnclosure06FanTable,
       "hwEnclosure06FanEntry": hwEnclosure06FanEntry,
       "hwEnclosure06FanIndex": hwEnclosure06FanIndex,
       "hwEnclosure06FanDesc": hwEnclosure06FanDesc,
       "hwEnclosure06FanSpeed": hwEnclosure06FanSpeed,
       "hwEnclosure06TempTable": hwEnclosure06TempTable,
       "hwEnclosure06TempEntry": hwEnclosure06TempEntry,
       "hwEnclosure06TempIndex": hwEnclosure06TempIndex,
       "hwEnclosure06TempDesc": hwEnclosure06TempDesc,
       "hwEnclosure06TempValue": hwEnclosure06TempValue,
       "hwEnclosure7": hwEnclosure7,
       "hwEnclosure07Installed": hwEnclosure07Installed,
       "hwEnclosure07Description": hwEnclosure07Description,
       "hwEnclosure07NumberOfPower": hwEnclosure07NumberOfPower,
       "hwEnclosure07NumberOfVol": hwEnclosure07NumberOfVol,
       "hwEnclosure07NumberOfFan": hwEnclosure07NumberOfFan,
       "hwEnclosure07NumberOfTemp": hwEnclosure07NumberOfTemp,
       "hwEnclosure07PowerTable": hwEnclosure07PowerTable,
       "hwEnclosure07PowerEntry": hwEnclosure07PowerEntry,
       "hwEnclosure07PowerIndex": hwEnclosure07PowerIndex,
       "hwEnclosure07PowerDesc": hwEnclosure07PowerDesc,
       "hwEnclosure07PowerState": hwEnclosure07PowerState,
       "hwEnclosure07VolTable": hwEnclosure07VolTable,
       "hwEnclosure07VolEntry": hwEnclosure07VolEntry,
       "hwEnclosure07VolIndex": hwEnclosure07VolIndex,
       "hwEnclosure07VolDesc": hwEnclosure07VolDesc,
       "hwEnclosure07VolValue": hwEnclosure07VolValue,
       "hwEnclosure07FanTable": hwEnclosure07FanTable,
       "hwEnclosure07FanEntry": hwEnclosure07FanEntry,
       "hwEnclosure07FanIndex": hwEnclosure07FanIndex,
       "hwEnclosure07FanDesc": hwEnclosure07FanDesc,
       "hwEnclosure07FanSpeed": hwEnclosure07FanSpeed,
       "hwEnclosure07TempTable": hwEnclosure07TempTable,
       "hwEnclosure07TempEntry": hwEnclosure07TempEntry,
       "hwEnclosure07TempIndex": hwEnclosure07TempIndex,
       "hwEnclosure07TempDesc": hwEnclosure07TempDesc,
       "hwEnclosure07TempValue": hwEnclosure07TempValue,
       "hwEnclosure8": hwEnclosure8,
       "hwEnclosure08Installed": hwEnclosure08Installed,
       "hwEnclosure08Description": hwEnclosure08Description,
       "hwEnclosure08NumberOfPower": hwEnclosure08NumberOfPower,
       "hwEnclosure08NumberOfVol": hwEnclosure08NumberOfVol,
       "hwEnclosure08NumberOfFan": hwEnclosure08NumberOfFan,
       "hwEnclosure08NumberOfTemp": hwEnclosure08NumberOfTemp,
       "hwEnclosure08PowerTable": hwEnclosure08PowerTable,
       "hwEnclosure08PowerEntry": hwEnclosure08PowerEntry,
       "hwEnclosure08PowerIndex": hwEnclosure08PowerIndex,
       "hwEnclosure08PowerDesc": hwEnclosure08PowerDesc,
       "hwEnclosure08PowerState": hwEnclosure08PowerState,
       "hwEnclosure08VolTable": hwEnclosure08VolTable,
       "hwEnclosure08VolEntry": hwEnclosure08VolEntry,
       "hwEnclosure08VolIndex": hwEnclosure08VolIndex,
       "hwEnclosure08VolDesc": hwEnclosure08VolDesc,
       "hwEnclosure08VolValue": hwEnclosure08VolValue,
       "hwEnclosure08FanTable": hwEnclosure08FanTable,
       "hwEnclosure08FanEntry": hwEnclosure08FanEntry,
       "hwEnclosure08FanIndex": hwEnclosure08FanIndex,
       "hwEnclosure08FanDesc": hwEnclosure08FanDesc,
       "hwEnclosure08FanSpeed": hwEnclosure08FanSpeed,
       "hwEnclosure08TempTable": hwEnclosure08TempTable,
       "hwEnclosure08TempEntry": hwEnclosure08TempEntry,
       "hwEnclosure08TempIndex": hwEnclosure08TempIndex,
       "hwEnclosure08TempDesc": hwEnclosure08TempDesc,
       "hwEnclosure08TempValue": hwEnclosure08TempValue,
       "hddInformation": hddInformation,
       "hddEnclosure1": hddEnclosure1,
       "hddEnclosure01Installed": hddEnclosure01Installed,
       "hddEnclosure01Description": hddEnclosure01Description,
       "hddEnclosure01NumberOfSlot": hddEnclosure01NumberOfSlot,
       "hddEnclosure01InfoTable": hddEnclosure01InfoTable,
       "hddEnclosure01InfoEntry": hddEnclosure01InfoEntry,
       "hddEnclosure01Slots": hddEnclosure01Slots,
       "hddEnclosure01Desc": hddEnclosure01Desc,
       "hddEnclosure01Name": hddEnclosure01Name,
       "hddEnclosure01Serial": hddEnclosure01Serial,
       "hddEnclosure01FirmVer": hddEnclosure01FirmVer,
       "hddEnclosure01Capacity": hddEnclosure01Capacity,
       "hddEnclosure01Type": hddEnclosure01Type,
       "hddEnclosure01State": hddEnclosure01State,
       "hddEnclosure2": hddEnclosure2,
       "hddEnclosure02Installed": hddEnclosure02Installed,
       "hddEnclosure02Description": hddEnclosure02Description,
       "hddEnclosure02NumberOfSlot": hddEnclosure02NumberOfSlot,
       "hddEnclosure02InfoTable": hddEnclosure02InfoTable,
       "hddEnclosure02InfoEntry": hddEnclosure02InfoEntry,
       "hddEnclosure02Slots": hddEnclosure02Slots,
       "hddEnclosure02Desc": hddEnclosure02Desc,
       "hddEnclosure02Name": hddEnclosure02Name,
       "hddEnclosure02Serial": hddEnclosure02Serial,
       "hddEnclosure02FirmVer": hddEnclosure02FirmVer,
       "hddEnclosure02Capacity": hddEnclosure02Capacity,
       "hddEnclosure02Type": hddEnclosure02Type,
       "hddEnclosure02State": hddEnclosure02State,
       "hddEnclosure3": hddEnclosure3,
       "hddEnclosure03Installed": hddEnclosure03Installed,
       "hddEnclosure03Description": hddEnclosure03Description,
       "hddEnclosure03NumberOfSlot": hddEnclosure03NumberOfSlot,
       "hddEnclosure03InfoTable": hddEnclosure03InfoTable,
       "hddEnclosure03InfoEntry": hddEnclosure03InfoEntry,
       "hddEnclosure03Slots": hddEnclosure03Slots,
       "hddEnclosure03Desc": hddEnclosure03Desc,
       "hddEnclosure03Name": hddEnclosure03Name,
       "hddEnclosure03Serial": hddEnclosure03Serial,
       "hddEnclosure03FirmVer": hddEnclosure03FirmVer,
       "hddEnclosure03Capacity": hddEnclosure03Capacity,
       "hddEnclosure03Type": hddEnclosure03Type,
       "hddEnclosure03State": hddEnclosure03State,
       "hddEnclosure4": hddEnclosure4,
       "hddEnclosure04Installed": hddEnclosure04Installed,
       "hddEnclosure04Description": hddEnclosure04Description,
       "hddEnclosure04NumberOfSlot": hddEnclosure04NumberOfSlot,
       "hddEnclosure04InfoTable": hddEnclosure04InfoTable,
       "hddEnclosure04InfoEntry": hddEnclosure04InfoEntry,
       "hddEnclosure04Slots": hddEnclosure04Slots,
       "hddEnclosure04Desc": hddEnclosure04Desc,
       "hddEnclosure04Name": hddEnclosure04Name,
       "hddEnclosure04Serial": hddEnclosure04Serial,
       "hddEnclosure04FirmVer": hddEnclosure04FirmVer,
       "hddEnclosure04Capacity": hddEnclosure04Capacity,
       "hddEnclosure04Type": hddEnclosure04Type,
       "hddEnclosure04State": hddEnclosure04State,
       "hddEnclosure5": hddEnclosure5,
       "hddEnclosure05Installed": hddEnclosure05Installed,
       "hddEnclosure05Description": hddEnclosure05Description,
       "hddEnclosure05NumberOfSlot": hddEnclosure05NumberOfSlot,
       "hddEnclosure05InfoTable": hddEnclosure05InfoTable,
       "hddEnclosure05InfoEntry": hddEnclosure05InfoEntry,
       "hddEnclosure05Slots": hddEnclosure05Slots,
       "hddEnclosure05Desc": hddEnclosure05Desc,
       "hddEnclosure05Name": hddEnclosure05Name,
       "hddEnclosure05Serial": hddEnclosure05Serial,
       "hddEnclosure05FirmVer": hddEnclosure05FirmVer,
       "hddEnclosure05Capacity": hddEnclosure05Capacity,
       "hddEnclosure05Type": hddEnclosure05Type,
       "hddEnclosure05State": hddEnclosure05State,
       "hddEnclosure6": hddEnclosure6,
       "hddEnclosure06Installed": hddEnclosure06Installed,
       "hddEnclosure06Description": hddEnclosure06Description,
       "hddEnclosure06NumberOfSlot": hddEnclosure06NumberOfSlot,
       "hddEnclosure06InfoTable": hddEnclosure06InfoTable,
       "hddEnclosure06InfoEntry": hddEnclosure06InfoEntry,
       "hddEnclosure06Slots": hddEnclosure06Slots,
       "hddEnclosure06Desc": hddEnclosure06Desc,
       "hddEnclosure06Name": hddEnclosure06Name,
       "hddEnclosure06Serial": hddEnclosure06Serial,
       "hddEnclosure06FirmVer": hddEnclosure06FirmVer,
       "hddEnclosure06Capacity": hddEnclosure06Capacity,
       "hddEnclosure06Type": hddEnclosure06Type,
       "hddEnclosure06State": hddEnclosure06State,
       "hddEnclosure7": hddEnclosure7,
       "hddEnclosure07Installed": hddEnclosure07Installed,
       "hddEnclosure07Description": hddEnclosure07Description,
       "hddEnclosure07NumberOfSlot": hddEnclosure07NumberOfSlot,
       "hddEnclosure07InfoTable": hddEnclosure07InfoTable,
       "hddEnclosure07InfoEntry": hddEnclosure07InfoEntry,
       "hddEnclosure07Slots": hddEnclosure07Slots,
       "hddEnclosure07Desc": hddEnclosure07Desc,
       "hddEnclosure07Name": hddEnclosure07Name,
       "hddEnclosure07Serial": hddEnclosure07Serial,
       "hddEnclosure07FirmVer": hddEnclosure07FirmVer,
       "hddEnclosure07Capacity": hddEnclosure07Capacity,
       "hddEnclosure07Type": hddEnclosure07Type,
       "hddEnclosure07State": hddEnclosure07State,
       "hddEnclosure8": hddEnclosure8,
       "hddEnclosure08Installed": hddEnclosure08Installed,
       "hddEnclosure08Description": hddEnclosure08Description,
       "hddEnclosure08NumberOfSlot": hddEnclosure08NumberOfSlot,
       "hddEnclosure08InfoTable": hddEnclosure08InfoTable,
       "hddEnclosure08InfoEntry": hddEnclosure08InfoEntry,
       "hddEnclosure08Slots": hddEnclosure08Slots,
       "hddEnclosure08Desc": hddEnclosure08Desc,
       "hddEnclosure08Name": hddEnclosure08Name,
       "hddEnclosure08Serial": hddEnclosure08Serial,
       "hddEnclosure08FirmVer": hddEnclosure08FirmVer,
       "hddEnclosure08Capacity": hddEnclosure08Capacity,
       "hddEnclosure08Type": hddEnclosure08Type,
       "hddEnclosure08State": hddEnclosure08State,
       "raidsetInformation": raidsetInformation,
       "raidInfoTable": raidInfoTable,
       "raidInfoEntry": raidInfoEntry,
       "raidNumber": raidNumber,
       "raidName": raidName,
       "raidDisks": raidDisks,
       "raidState": raidState,
       "raidTotalCapacity": raidTotalCapacity,
       "raidFreeCapacity": raidFreeCapacity,
       "raidMemberDiskCapacity": raidMemberDiskCapacity,
       "raidMemberDiskChannels": raidMemberDiskChannels,
       "volumesetInformation": volumesetInformation,
       "volInfoTable": volInfoTable,
       "volInfoEntry": volInfoEntry,
       "volNumber": volNumber,
       "volName": volName,
       "volRaidName": volRaidName,
       "volCapacity": volCapacity,
       "volState": volState,
       "volProgress": volProgress,
       "volCluster": volCluster,
       "volChannel": volChannel,
       "volSCSIID": volSCSIID,
       "volSCSILUN": volSCSILUN,
       "volRaidLevel": volRaidLevel,
       "volStripes": volStripes,
       "volDisks": volDisks,
       "volCache": volCache,
       "volTag": volTag,
       "volMaxSpeed": volMaxSpeed,
       "volCurrentSpeed": volCurrentSpeed,
       "eventInformation": eventInformation,
       "eventInfoTable": eventInfoTable,
       "eventInfoEntry": eventInfoEntry,
       "eventNumber": eventNumber,
       "eventString": eventString,
       "raidSubSysTraps": raidSubSysTraps,
       "rsCreate": rsCreate,
       "rsDelete": rsDelete,
       "rsExpand": rsExpand,
       "rsRebuild": rsRebuild,
       "rsDegraded": rsDegraded,
       "rsNoEvent": rsNoEvent,
       "vsInitializing": vsInitializing,
       "vsRebuilding": vsRebuilding,
       "vsMigrating": vsMigrating,
       "vsChecking": vsChecking,
       "vsCompleteInit": vsCompleteInit,
       "vsCompleteRebuild": vsCompleteRebuild,
       "vsCompleteMigrating": vsCompleteMigrating,
       "vsCompleteChecking": vsCompleteChecking,
       "vsCreate": vsCreate,
       "vsDelete": vsDelete,
       "vsModify": vsModify,
       "vsDegraded": vsDegraded,
       "vsFailed": vsFailed,
       "vsRevived": vsRevived,
       "vsTotals": vsTotals,
       "pdAdded": pdAdded,
       "pdRemoved": pdRemoved,
       "pdReadError": pdReadError,
       "pdWriteError": pdWriteError,
       "pdAtaEccError": pdAtaEccError,
       "pdAtaChangeMode": pdAtaChangeMode,
       "pdTimeOut": pdTimeOut,
       "pdMarkFailed": pdMarkFailed,
       "pdPciError": pdPciError,
       "pdSmartFailed": pdSmartFailed,
       "pdCreatePass": pdCreatePass,
       "pdModifyPass": pdModifyPass,
       "pdDeletePass": pdDeletePass,
       "pdTotals": pdTotals,
       "scsiReset": scsiReset,
       "scsiParity": scsiParity,
       "scsiModeChange": scsiModeChange,
       "scsiTotals": scsiTotals,
       "hwSdram1BitEcc": hwSdram1BitEcc,
       "hwSdramMultiBitEcc": hwSdramMultiBitEcc,
       "hwTempController": hwTempController,
       "hwTempBackplane": hwTempBackplane,
       "hwVoltage15": hwVoltage15,
       "hwVoltage3": hwVoltage3,
       "hwVoltage5": hwVoltage5,
       "hwVoltage12": hwVoltage12,
       "hwVoltage13": hwVoltage13,
       "hwVoltage25": hwVoltage25,
       "hwVoltage125": hwVoltage125,
       "hwPower1Failed": hwPower1Failed,
       "hwFan1Failed": hwFan1Failed,
       "hwPower2Failed": hwPower2Failed,
       "hwFan2Failed": hwFan2Failed,
       "hwPower3Failed": hwPower3Failed,
       "hwFan3Failed": hwFan3Failed,
       "hwPower4Failed": hwPower4Failed,
       "hwFan4Failed": hwFan4Failed,
       "hwUpsPowerLoss": hwUpsPowerLoss,
       "hwTempControllerR": hwTempControllerR,
       "hwTempBackplaneR": hwTempBackplaneR,
       "hwVoltage15R": hwVoltage15R,
       "hwVoltage3R": hwVoltage3R,
       "hwVoltage5R": hwVoltage5R,
       "hwVoltage12R": hwVoltage12R,
       "hwVoltage13R": hwVoltage13R,
       "hwVoltage25R": hwVoltage25R,
       "hwVoltage125R": hwVoltage125R,
       "hwPower1FailedR": hwPower1FailedR,
       "hwFan1FailedR": hwFan1FailedR,
       "hwPower2FailedR": hwPower2FailedR,
       "hwFan2FailedR": hwFan2FailedR,
       "hwPower3FailedR": hwPower3FailedR,
       "hwFan3FailedR": hwFan3FailedR,
       "hwPower4FailedR": hwPower4FailedR,
       "hwFan4FailedR": hwFan4FailedR,
       "hwUPSPowerR": hwUPSPowerR,
       "hwSystemRestarted": hwSystemRestarted,
       "hwTest": hwTest,
       "hwSystemRecovered": hwSystemRecovered,
       "ghmRecover": ghmRecover,
       "ghmOverTemp": ghmOverTemp,
       "ghmFailed": ghmFailed,
       "ghmUnderVoltage": ghmUnderVoltage,
       "ghmOverVoltage": ghmOverVoltage,
       "ghmDiscovered": ghmDiscovered,
       "ghmLostMig": ghmLostMig,
       "ghmRestartLBA": ghmRestartLBA,
       "ghmHTTPLogin": ghmHTTPLogin,
       "ghmTelnetLogin": ghmTelnetLogin,
       "ghmVt100Login": ghmVt100Login,
       "ghmGUILogin": ghmGUILogin,
       "ghmFCLinkUp": ghmFCLinkUp,
       "ghmFCLinkDown": ghmFCLinkDown,
       "ghm16BytesCDB": ghm16BytesCDB,
       "ghmInitLBA": ghmInitLBA,
       "ghmRebuildLBA": ghmRebuildLBA,
       "ghmMigrateLBA": ghmMigrateLBA}
)
