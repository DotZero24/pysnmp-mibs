# SNMP MIB module (ZTE-AN-PETH-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/zte/ZTE-AN-PETH-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:44:53 2025
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")

(zxAn,) = mibBuilder.importSymbols(
    "ZTE-AN-TC-MIB",
    "zxAn")


# MODULE-IDENTITY

zxAnPethMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 300)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ZxAnPethObjects_ObjectIdentity = ObjectIdentity
zxAnPethObjects = _ZxAnPethObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 300, 1)
)
_ZxAnPethGlobalObjects_ObjectIdentity = ObjectIdentity
zxAnPethGlobalObjects = _ZxAnPethGlobalObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 300, 1, 1)
)


class _ZxAnPethPsePmMode_Type(Integer32):
    """Custom type zxAnPethPsePmMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("staticPowerWithPriority", 2),
          ("dynamicPowerWithPriority", 3),
          ("staticPowerWithoutPriority", 4),
          ("dynamicPowerWithoutPriority", 5))
    )


_ZxAnPethPsePmMode_Type.__name__ = "Integer32"
_ZxAnPethPsePmMode_Object = MibScalar
zxAnPethPsePmMode = _ZxAnPethPsePmMode_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 300, 1, 1, 1),
    _ZxAnPethPsePmMode_Type()
)
zxAnPethPsePmMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnPethPsePmMode.setStatus("current")
_ZxAnPethPseActualCurrent_Type = Integer32
_ZxAnPethPseActualCurrent_Object = MibScalar
zxAnPethPseActualCurrent = _ZxAnPethPseActualCurrent_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 300, 1, 1, 2),
    _ZxAnPethPseActualCurrent_Type()
)
zxAnPethPseActualCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnPethPseActualCurrent.setStatus("current")
if mibBuilder.loadTexts:
    zxAnPethPseActualCurrent.setUnits("mA")
_ZxAnPethPseActualVoltage_Type = Integer32
_ZxAnPethPseActualVoltage_Object = MibScalar
zxAnPethPseActualVoltage = _ZxAnPethPseActualVoltage_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 300, 1, 1, 3),
    _ZxAnPethPseActualVoltage_Type()
)
zxAnPethPseActualVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnPethPseActualVoltage.setStatus("current")
if mibBuilder.loadTexts:
    zxAnPethPseActualVoltage.setUnits("0.1V")
_ZxAnPethPseChipTemp_Type = Integer32
_ZxAnPethPseChipTemp_Object = MibScalar
zxAnPethPseChipTemp = _ZxAnPethPseChipTemp_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 300, 1, 1, 4),
    _ZxAnPethPseChipTemp_Type()
)
zxAnPethPseChipTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnPethPseChipTemp.setStatus("current")
if mibBuilder.loadTexts:
    zxAnPethPseChipTemp.setUnits("centigrade")


class _ZxAnPethPseChipTempAlmThresh_Type(Integer32):
    """Custom type zxAnPethPseChipTempAlmThresh based on Integer32"""
    defaultValue = 120

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 250),
    )


_ZxAnPethPseChipTempAlmThresh_Type.__name__ = "Integer32"
_ZxAnPethPseChipTempAlmThresh_Object = MibScalar
zxAnPethPseChipTempAlmThresh = _ZxAnPethPseChipTempAlmThresh_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 300, 1, 1, 5),
    _ZxAnPethPseChipTempAlmThresh_Type()
)
zxAnPethPseChipTempAlmThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnPethPseChipTempAlmThresh.setStatus("current")
if mibBuilder.loadTexts:
    zxAnPethPseChipTempAlmThresh.setUnits("centigrade")


class _ZxAnPethPseChipTempTrapEnable_Type(Integer32):
    """Custom type zxAnPethPseChipTempTrapEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_ZxAnPethPseChipTempTrapEnable_Type.__name__ = "Integer32"
_ZxAnPethPseChipTempTrapEnable_Object = MibScalar
zxAnPethPseChipTempTrapEnable = _ZxAnPethPseChipTempTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 300, 1, 1, 6),
    _ZxAnPethPseChipTempTrapEnable_Type()
)
zxAnPethPseChipTempTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnPethPseChipTempTrapEnable.setStatus("current")


class _ZxAnPethPseOutVoltageUpperThresh_Type(Integer32):
    """Custom type zxAnPethPseOutVoltageUpperThresh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(440, 585),
    )


_ZxAnPethPseOutVoltageUpperThresh_Type.__name__ = "Integer32"
_ZxAnPethPseOutVoltageUpperThresh_Object = MibScalar
zxAnPethPseOutVoltageUpperThresh = _ZxAnPethPseOutVoltageUpperThresh_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 300, 1, 1, 7),
    _ZxAnPethPseOutVoltageUpperThresh_Type()
)
zxAnPethPseOutVoltageUpperThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnPethPseOutVoltageUpperThresh.setStatus("current")
if mibBuilder.loadTexts:
    zxAnPethPseOutVoltageUpperThresh.setUnits("0.1V")


class _ZxAnPethPseOutVoltageLowerThresh_Type(Integer32):
    """Custom type zxAnPethPseOutVoltageLowerThresh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(440, 585),
    )


_ZxAnPethPseOutVoltageLowerThresh_Type.__name__ = "Integer32"
_ZxAnPethPseOutVoltageLowerThresh_Object = MibScalar
zxAnPethPseOutVoltageLowerThresh = _ZxAnPethPseOutVoltageLowerThresh_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 300, 1, 1, 8),
    _ZxAnPethPseOutVoltageLowerThresh_Type()
)
zxAnPethPseOutVoltageLowerThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnPethPseOutVoltageLowerThresh.setStatus("current")
if mibBuilder.loadTexts:
    zxAnPethPseOutVoltageLowerThresh.setUnits("0.1V")


class _ZxAnPethPseFirmwareVersion_Type(DisplayString):
    """Custom type zxAnPethPseFirmwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_ZxAnPethPseFirmwareVersion_Type.__name__ = "DisplayString"
_ZxAnPethPseFirmwareVersion_Object = MibScalar
zxAnPethPseFirmwareVersion = _ZxAnPethPseFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 300, 1, 1, 9),
    _ZxAnPethPseFirmwareVersion_Type()
)
zxAnPethPseFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnPethPseFirmwareVersion.setStatus("current")


class _ZxAnPethMainPsePowerLimit_Type(Integer32):
    """Custom type zxAnPethMainPsePowerLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ZxAnPethMainPsePowerLimit_Type.__name__ = "Integer32"
_ZxAnPethMainPsePowerLimit_Object = MibScalar
zxAnPethMainPsePowerLimit = _ZxAnPethMainPsePowerLimit_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 300, 1, 1, 10),
    _ZxAnPethMainPsePowerLimit_Type()
)
zxAnPethMainPsePowerLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnPethMainPsePowerLimit.setStatus("current")
if mibBuilder.loadTexts:
    zxAnPethMainPsePowerLimit.setUnits("0.1Watts")


class _ZxAnPethMainPsePowerUsageThresh_Type(Integer32):
    """Custom type zxAnPethMainPsePowerUsageThresh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ZxAnPethMainPsePowerUsageThresh_Type.__name__ = "Integer32"
_ZxAnPethMainPsePowerUsageThresh_Object = MibScalar
zxAnPethMainPsePowerUsageThresh = _ZxAnPethMainPsePowerUsageThresh_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 300, 1, 1, 11),
    _ZxAnPethMainPsePowerUsageThresh_Type()
)
zxAnPethMainPsePowerUsageThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnPethMainPsePowerUsageThresh.setStatus("current")
if mibBuilder.loadTexts:
    zxAnPethMainPsePowerUsageThresh.setUnits("0.1Watts")
_ZxAnPethPsePortTable_Object = MibTable
zxAnPethPsePortTable = _ZxAnPethPsePortTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 300, 1, 2)
)
if mibBuilder.loadTexts:
    zxAnPethPsePortTable.setStatus("current")
_ZxAnPethPsePortEntry_Object = MibTableRow
zxAnPethPsePortEntry = _ZxAnPethPsePortEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 300, 1, 2, 1)
)
zxAnPethPsePortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    zxAnPethPsePortEntry.setStatus("current")


class _ZxAnPethPsePortForcePowerEnable_Type(Integer32):
    """Custom type zxAnPethPsePortForcePowerEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_ZxAnPethPsePortForcePowerEnable_Type.__name__ = "Integer32"
_ZxAnPethPsePortForcePowerEnable_Object = MibTableColumn
zxAnPethPsePortForcePowerEnable = _ZxAnPethPsePortForcePowerEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 300, 1, 2, 1, 1),
    _ZxAnPethPsePortForcePowerEnable_Type()
)
zxAnPethPsePortForcePowerEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnPethPsePortForcePowerEnable.setStatus("current")
_ZxAnPethPsePortActualVoltage_Type = Integer32
_ZxAnPethPsePortActualVoltage_Object = MibTableColumn
zxAnPethPsePortActualVoltage = _ZxAnPethPsePortActualVoltage_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 300, 1, 2, 1, 2),
    _ZxAnPethPsePortActualVoltage_Type()
)
zxAnPethPsePortActualVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnPethPsePortActualVoltage.setStatus("current")
if mibBuilder.loadTexts:
    zxAnPethPsePortActualVoltage.setUnits("0.1V")
_ZxAnPethPsePortActualCurrent_Type = Integer32
_ZxAnPethPsePortActualCurrent_Object = MibTableColumn
zxAnPethPsePortActualCurrent = _ZxAnPethPsePortActualCurrent_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 300, 1, 2, 1, 3),
    _ZxAnPethPsePortActualCurrent_Type()
)
zxAnPethPsePortActualCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnPethPsePortActualCurrent.setStatus("current")
if mibBuilder.loadTexts:
    zxAnPethPsePortActualCurrent.setUnits("mA")
_ZxAnPethPsePortActualPower_Type = Integer32
_ZxAnPethPsePortActualPower_Object = MibTableColumn
zxAnPethPsePortActualPower = _ZxAnPethPsePortActualPower_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 300, 1, 2, 1, 4),
    _ZxAnPethPsePortActualPower_Type()
)
zxAnPethPsePortActualPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnPethPsePortActualPower.setStatus("current")
if mibBuilder.loadTexts:
    zxAnPethPsePortActualPower.setUnits("0.1W")


class _ZxAnPethPsePortMaxPower_Type(Integer32):
    """Custom type zxAnPethPsePortMaxPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 300),
    )


_ZxAnPethPsePortMaxPower_Type.__name__ = "Integer32"
_ZxAnPethPsePortMaxPower_Object = MibTableColumn
zxAnPethPsePortMaxPower = _ZxAnPethPsePortMaxPower_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 300, 1, 2, 1, 5),
    _ZxAnPethPsePortMaxPower_Type()
)
zxAnPethPsePortMaxPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnPethPsePortMaxPower.setStatus("current")
if mibBuilder.loadTexts:
    zxAnPethPsePortMaxPower.setUnits("0.1W")


class _ZxAnPethPsePortDetectionType_Type(Integer32):
    """Custom type zxAnPethPsePortDetectionType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("noDetection", 1),
          ("legacyOnly", 2),
          ("fourPointOnly", 3),
          ("fourPointLegacy", 4),
          ("twoPointOnly", 5),
          ("twoPointLegacy", 6))
    )


_ZxAnPethPsePortDetectionType_Type.__name__ = "Integer32"
_ZxAnPethPsePortDetectionType_Object = MibTableColumn
zxAnPethPsePortDetectionType = _ZxAnPethPsePortDetectionType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 300, 1, 2, 1, 6),
    _ZxAnPethPsePortDetectionType_Type()
)
zxAnPethPsePortDetectionType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnPethPsePortDetectionType.setStatus("current")


class _ZxAnPethPsePortWorkMode_Type(Integer32):
    """Custom type zxAnPethPsePortWorkMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ieee8023af", 1),
          ("ieee8023at", 2))
    )


_ZxAnPethPsePortWorkMode_Type.__name__ = "Integer32"
_ZxAnPethPsePortWorkMode_Object = MibTableColumn
zxAnPethPsePortWorkMode = _ZxAnPethPsePortWorkMode_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 300, 1, 2, 1, 7),
    _ZxAnPethPsePortWorkMode_Type()
)
zxAnPethPsePortWorkMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnPethPsePortWorkMode.setStatus("current")


class _ZxAnPethPsePortReset_Type(Integer32):
    """Custom type zxAnPethPsePortReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset", 1)
    )


_ZxAnPethPsePortReset_Type.__name__ = "Integer32"
_ZxAnPethPsePortReset_Object = MibTableColumn
zxAnPethPsePortReset = _ZxAnPethPsePortReset_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 300, 1, 2, 1, 8),
    _ZxAnPethPsePortReset_Type()
)
zxAnPethPsePortReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnPethPsePortReset.setStatus("current")


class _ZxAnPethPsePortOperStatus_Type(Integer32):
    """Custom type zxAnPethPsePortOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_ZxAnPethPsePortOperStatus_Type.__name__ = "Integer32"
_ZxAnPethPsePortOperStatus_Object = MibTableColumn
zxAnPethPsePortOperStatus = _ZxAnPethPsePortOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 300, 1, 2, 1, 9),
    _ZxAnPethPsePortOperStatus_Type()
)
zxAnPethPsePortOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnPethPsePortOperStatus.setStatus("current")


class _ZxAnPethPsePortDetailInfo_Type(DisplayString):
    """Custom type zxAnPethPsePortDetailInfo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ZxAnPethPsePortDetailInfo_Type.__name__ = "DisplayString"
_ZxAnPethPsePortDetailInfo_Object = MibTableColumn
zxAnPethPsePortDetailInfo = _ZxAnPethPsePortDetailInfo_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 300, 1, 2, 1, 10),
    _ZxAnPethPsePortDetailInfo_Type()
)
zxAnPethPsePortDetailInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnPethPsePortDetailInfo.setStatus("current")


class _ZxAnPethPsePortTrapEnable_Type(Integer32):
    """Custom type zxAnPethPsePortTrapEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_ZxAnPethPsePortTrapEnable_Type.__name__ = "Integer32"
_ZxAnPethPsePortTrapEnable_Object = MibTableColumn
zxAnPethPsePortTrapEnable = _ZxAnPethPsePortTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 300, 1, 2, 1, 11),
    _ZxAnPethPsePortTrapEnable_Type()
)
zxAnPethPsePortTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnPethPsePortTrapEnable.setStatus("current")
_ZxAnPethPseCardTable_Object = MibTable
zxAnPethPseCardTable = _ZxAnPethPseCardTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 300, 1, 3)
)
if mibBuilder.loadTexts:
    zxAnPethPseCardTable.setStatus("current")
_ZxAnPethPseCardEntry_Object = MibTableRow
zxAnPethPseCardEntry = _ZxAnPethPseCardEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 300, 1, 3, 1)
)
zxAnPethPseCardEntry.setIndexNames(
    (0, "ZTE-AN-PETH-MIB", "zxAnPethPseRack"),
    (0, "ZTE-AN-PETH-MIB", "zxAnPethPseShelf"),
    (0, "ZTE-AN-PETH-MIB", "zxAnPethPseSlot"),
)
if mibBuilder.loadTexts:
    zxAnPethPseCardEntry.setStatus("current")
_ZxAnPethPseRack_Type = Integer32
_ZxAnPethPseRack_Object = MibTableColumn
zxAnPethPseRack = _ZxAnPethPseRack_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 300, 1, 3, 1, 1),
    _ZxAnPethPseRack_Type()
)
zxAnPethPseRack.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnPethPseRack.setStatus("current")
_ZxAnPethPseShelf_Type = Integer32
_ZxAnPethPseShelf_Object = MibTableColumn
zxAnPethPseShelf = _ZxAnPethPseShelf_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 300, 1, 3, 1, 2),
    _ZxAnPethPseShelf_Type()
)
zxAnPethPseShelf.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnPethPseShelf.setStatus("current")
_ZxAnPethPseSlot_Type = Integer32
_ZxAnPethPseSlot_Object = MibTableColumn
zxAnPethPseSlot = _ZxAnPethPseSlot_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 300, 1, 3, 1, 3),
    _ZxAnPethPseSlot_Type()
)
zxAnPethPseSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnPethPseSlot.setStatus("current")
_ZxAnPethPseCardSupportPoe_Type = TruthValue
_ZxAnPethPseCardSupportPoe_Object = MibTableColumn
zxAnPethPseCardSupportPoe = _ZxAnPethPseCardSupportPoe_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 300, 1, 3, 1, 4),
    _ZxAnPethPseCardSupportPoe_Type()
)
zxAnPethPseCardSupportPoe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnPethPseCardSupportPoe.setStatus("current")
_ZxAnPethPdePortTable_Object = MibTable
zxAnPethPdePortTable = _ZxAnPethPdePortTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 300, 1, 4)
)
if mibBuilder.loadTexts:
    zxAnPethPdePortTable.setStatus("current")
_ZxAnPethPdePortEntry_Object = MibTableRow
zxAnPethPdePortEntry = _ZxAnPethPdePortEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 300, 1, 4, 1)
)
zxAnPethPdePortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    zxAnPethPdePortEntry.setStatus("current")


class _ZxAnPethPdePortAutoCheckEnable_Type(Integer32):
    """Custom type zxAnPethPdePortAutoCheckEnable based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_ZxAnPethPdePortAutoCheckEnable_Type.__name__ = "Integer32"
_ZxAnPethPdePortAutoCheckEnable_Object = MibTableColumn
zxAnPethPdePortAutoCheckEnable = _ZxAnPethPdePortAutoCheckEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 300, 1, 4, 1, 1),
    _ZxAnPethPdePortAutoCheckEnable_Type()
)
zxAnPethPdePortAutoCheckEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnPethPdePortAutoCheckEnable.setStatus("current")


class _ZxAnPethPdePortPowerSupplyStatus_Type(Integer32):
    """Custom type zxAnPethPdePortPowerSupplyStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("on", 2),
          ("off", 3))
    )


_ZxAnPethPdePortPowerSupplyStatus_Type.__name__ = "Integer32"
_ZxAnPethPdePortPowerSupplyStatus_Object = MibTableColumn
zxAnPethPdePortPowerSupplyStatus = _ZxAnPethPdePortPowerSupplyStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 300, 1, 4, 1, 2),
    _ZxAnPethPdePortPowerSupplyStatus_Type()
)
zxAnPethPdePortPowerSupplyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnPethPdePortPowerSupplyStatus.setStatus("current")
_ZxAnPethTrapObjects_ObjectIdentity = ObjectIdentity
zxAnPethTrapObjects = _ZxAnPethTrapObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 300, 2)
)

# Managed Objects groups


# Notification objects

zxAnPethPseChipHighTempAlm = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 300, 2, 1)
)
zxAnPethPseChipHighTempAlm.setObjects(
      *(("ZTE-AN-PETH-MIB", "zxAnPethPseChipTemp"),
        ("ZTE-AN-PETH-MIB", "zxAnPethPseChipTempAlmThresh"))
)
if mibBuilder.loadTexts:
    zxAnPethPseChipHighTempAlm.setStatus(
        "current"
    )

zxAnPethPseChipHighTempClr = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 300, 2, 2)
)
zxAnPethPseChipHighTempClr.setObjects(
      *(("ZTE-AN-PETH-MIB", "zxAnPethPseChipTemp"),
        ("ZTE-AN-PETH-MIB", "zxAnPethPseChipTempAlmThresh"))
)
if mibBuilder.loadTexts:
    zxAnPethPseChipHighTempClr.setStatus(
        "current"
    )

zxAnPethPsePortStatusUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 300, 2, 3)
)
zxAnPethPsePortStatusUp.setObjects(
      *(("ZTE-AN-PETH-MIB", "zxAnPethPsePortOperStatus"),
        ("ZTE-AN-PETH-MIB", "zxAnPethPsePortOperStatusDetail"))
)
if mibBuilder.loadTexts:
    zxAnPethPsePortStatusUp.setStatus(
        "current"
    )

zxAnPethPsePortStatusDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 300, 2, 4)
)
zxAnPethPsePortStatusDown.setObjects(
      *(("ZTE-AN-PETH-MIB", "zxAnPethPsePortOperStatus"),
        ("ZTE-AN-PETH-MIB", "zxAnPethPsePortOperStatusDetail"))
)
if mibBuilder.loadTexts:
    zxAnPethPsePortStatusDown.setStatus(
        "current"
    )

zxAnPethPseOverVoltageAlm = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 300, 2, 5)
)
zxAnPethPseOverVoltageAlm.setObjects(
      *(("ZTE-AN-PETH-MIB", "zxAnPethPseActualVoltage"),
        ("ZTE-AN-PETH-MIB", "zxAnPethPseVoltageUpperThresh"))
)
if mibBuilder.loadTexts:
    zxAnPethPseOverVoltageAlm.setStatus(
        "current"
    )

zxAnPethPseOverVoltageClr = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 300, 2, 6)
)
zxAnPethPseOverVoltageClr.setObjects(
      *(("ZTE-AN-PETH-MIB", "zxAnPethPseActualVoltage"),
        ("ZTE-AN-PETH-MIB", "zxAnPethPseVoltageUpperThresh"))
)
if mibBuilder.loadTexts:
    zxAnPethPseOverVoltageClr.setStatus(
        "current"
    )

zxAnPethPseUnderVoltageAlm = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 300, 2, 7)
)
zxAnPethPseUnderVoltageAlm.setObjects(
      *(("ZTE-AN-PETH-MIB", "zxAnPethPseActualVoltage"),
        ("ZTE-AN-PETH-MIB", "zxAnPethPseVoltageLowerThresh"))
)
if mibBuilder.loadTexts:
    zxAnPethPseUnderVoltageAlm.setStatus(
        "current"
    )

zxAnPethPseUnderVoltageClr = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 300, 2, 8)
)
zxAnPethPseUnderVoltageClr.setObjects(
      *(("ZTE-AN-PETH-MIB", "zxAnPethPseActualVoltage"),
        ("ZTE-AN-PETH-MIB", "zxAnPethPseVoltageLowerThresh"))
)
if mibBuilder.loadTexts:
    zxAnPethPseUnderVoltageClr.setStatus(
        "current"
    )

zxAnPethPdePortPowerOffAlm = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 300, 2, 9)
)
zxAnPethPdePortPowerOffAlm.setObjects(
    ("ZTE-AN-PETH-MIB", "zxAnPethPdePortPowerSupplyStatus")
)
if mibBuilder.loadTexts:
    zxAnPethPdePortPowerOffAlm.setStatus(
        "current"
    )

zxAnPethPdePortPowerOffClr = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 300, 2, 10)
)
zxAnPethPdePortPowerOffClr.setObjects(
    ("ZTE-AN-PETH-MIB", "zxAnPethPdePortPowerSupplyStatus")
)
if mibBuilder.loadTexts:
    zxAnPethPdePortPowerOffClr.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZTE-AN-PETH-MIB",
    **{"zxAnPethMib": zxAnPethMib,
       "zxAnPethObjects": zxAnPethObjects,
       "zxAnPethGlobalObjects": zxAnPethGlobalObjects,
       "zxAnPethPsePmMode": zxAnPethPsePmMode,
       "zxAnPethPseActualCurrent": zxAnPethPseActualCurrent,
       "zxAnPethPseActualVoltage": zxAnPethPseActualVoltage,
       "zxAnPethPseChipTemp": zxAnPethPseChipTemp,
       "zxAnPethPseChipTempAlmThresh": zxAnPethPseChipTempAlmThresh,
       "zxAnPethPseChipTempTrapEnable": zxAnPethPseChipTempTrapEnable,
       "zxAnPethPseOutVoltageUpperThresh": zxAnPethPseOutVoltageUpperThresh,
       "zxAnPethPseOutVoltageLowerThresh": zxAnPethPseOutVoltageLowerThresh,
       "zxAnPethPseFirmwareVersion": zxAnPethPseFirmwareVersion,
       "zxAnPethMainPsePowerLimit": zxAnPethMainPsePowerLimit,
       "zxAnPethMainPsePowerUsageThresh": zxAnPethMainPsePowerUsageThresh,
       "zxAnPethPsePortTable": zxAnPethPsePortTable,
       "zxAnPethPsePortEntry": zxAnPethPsePortEntry,
       "zxAnPethPsePortForcePowerEnable": zxAnPethPsePortForcePowerEnable,
       "zxAnPethPsePortActualVoltage": zxAnPethPsePortActualVoltage,
       "zxAnPethPsePortActualCurrent": zxAnPethPsePortActualCurrent,
       "zxAnPethPsePortActualPower": zxAnPethPsePortActualPower,
       "zxAnPethPsePortMaxPower": zxAnPethPsePortMaxPower,
       "zxAnPethPsePortDetectionType": zxAnPethPsePortDetectionType,
       "zxAnPethPsePortWorkMode": zxAnPethPsePortWorkMode,
       "zxAnPethPsePortReset": zxAnPethPsePortReset,
       "zxAnPethPsePortOperStatus": zxAnPethPsePortOperStatus,
       "zxAnPethPsePortDetailInfo": zxAnPethPsePortDetailInfo,
       "zxAnPethPsePortTrapEnable": zxAnPethPsePortTrapEnable,
       "zxAnPethPseCardTable": zxAnPethPseCardTable,
       "zxAnPethPseCardEntry": zxAnPethPseCardEntry,
       "zxAnPethPseRack": zxAnPethPseRack,
       "zxAnPethPseShelf": zxAnPethPseShelf,
       "zxAnPethPseSlot": zxAnPethPseSlot,
       "zxAnPethPseCardSupportPoe": zxAnPethPseCardSupportPoe,
       "zxAnPethPdePortTable": zxAnPethPdePortTable,
       "zxAnPethPdePortEntry": zxAnPethPdePortEntry,
       "zxAnPethPdePortAutoCheckEnable": zxAnPethPdePortAutoCheckEnable,
       "zxAnPethPdePortPowerSupplyStatus": zxAnPethPdePortPowerSupplyStatus,
       "zxAnPethTrapObjects": zxAnPethTrapObjects,
       "zxAnPethPseChipHighTempAlm": zxAnPethPseChipHighTempAlm,
       "zxAnPethPseChipHighTempClr": zxAnPethPseChipHighTempClr,
       "zxAnPethPsePortStatusUp": zxAnPethPsePortStatusUp,
       "zxAnPethPsePortStatusDown": zxAnPethPsePortStatusDown,
       "zxAnPethPseOverVoltageAlm": zxAnPethPseOverVoltageAlm,
       "zxAnPethPseOverVoltageClr": zxAnPethPseOverVoltageClr,
       "zxAnPethPseUnderVoltageAlm": zxAnPethPseUnderVoltageAlm,
       "zxAnPethPseUnderVoltageClr": zxAnPethPseUnderVoltageClr,
       "zxAnPethPdePortPowerOffAlm": zxAnPethPdePortPowerOffAlm,
       "zxAnPethPdePortPowerOffClr": zxAnPethPdePortPowerOffClr}
)
