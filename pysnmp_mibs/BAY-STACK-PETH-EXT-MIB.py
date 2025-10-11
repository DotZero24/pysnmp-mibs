# SNMP MIB module (BAY-STACK-PETH-EXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/nortel/BAY-STACK-PETH-EXT-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:20:54 2025
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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")

(bayStackMibs,) = mibBuilder.importSymbols(
    "SYNOPTICS-ROOT-MIB",
    "bayStackMibs")


# MODULE-IDENTITY

bayStackPethExtMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 45, 5, 8)
)
if mibBuilder.loadTexts:
    bayStackPethExtMib.setRevisions(
        ("2020-03-17 00:00",
         "2019-11-21 00:00",
         "2016-03-03 00:00",
         "2015-12-09 00:00",
         "2015-11-17 00:00",
         "2015-07-06 00:00",
         "2012-01-25 00:00",
         "2011-07-20 00:00",
         "2011-01-10 00:00",
         "2004-11-11 00:00",
         "2004-10-18 00:00",
         "2004-09-14 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_BspeNotifications_ObjectIdentity = ObjectIdentity
bspeNotifications = _BspeNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 5, 8, 0)
)
_BspeObjects_ObjectIdentity = ObjectIdentity
bspeObjects = _BspeObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 5, 8, 1)
)
_BspePethPsePortExtTable_Object = MibTable
bspePethPsePortExtTable = _BspePethPsePortExtTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 8, 1, 1)
)
if mibBuilder.loadTexts:
    bspePethPsePortExtTable.setStatus("current")
_BspePethPsePortExtEntry_Object = MibTableRow
bspePethPsePortExtEntry = _BspePethPsePortExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 8, 1, 1, 1)
)
bspePethPsePortExtEntry.setIndexNames(
    (0, "BAY-STACK-PETH-EXT-MIB", "bspePethPsePortExtGroupIndex"),
    (0, "BAY-STACK-PETH-EXT-MIB", "bspePethPsePortExtIndex"),
)
if mibBuilder.loadTexts:
    bspePethPsePortExtEntry.setStatus("current")


class _BspePethPsePortExtGroupIndex_Type(Integer32):
    """Custom type bspePethPsePortExtGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_BspePethPsePortExtGroupIndex_Type.__name__ = "Integer32"
_BspePethPsePortExtGroupIndex_Object = MibTableColumn
bspePethPsePortExtGroupIndex = _BspePethPsePortExtGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 8, 1, 1, 1, 1),
    _BspePethPsePortExtGroupIndex_Type()
)
bspePethPsePortExtGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bspePethPsePortExtGroupIndex.setStatus("current")


class _BspePethPsePortExtIndex_Type(Integer32):
    """Custom type bspePethPsePortExtIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_BspePethPsePortExtIndex_Type.__name__ = "Integer32"
_BspePethPsePortExtIndex_Object = MibTableColumn
bspePethPsePortExtIndex = _BspePethPsePortExtIndex_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 8, 1, 1, 1, 2),
    _BspePethPsePortExtIndex_Type()
)
bspePethPsePortExtIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bspePethPsePortExtIndex.setStatus("current")


class _BspePethPsePortExtPowerLimit_Type(Integer32):
    """Custom type bspePethPsePortExtPowerLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 98),
    )


_BspePethPsePortExtPowerLimit_Type.__name__ = "Integer32"
_BspePethPsePortExtPowerLimit_Object = MibTableColumn
bspePethPsePortExtPowerLimit = _BspePethPsePortExtPowerLimit_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 8, 1, 1, 1, 3),
    _BspePethPsePortExtPowerLimit_Type()
)
bspePethPsePortExtPowerLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bspePethPsePortExtPowerLimit.setStatus("current")
if mibBuilder.loadTexts:
    bspePethPsePortExtPowerLimit.setUnits("watts")


class _BspePethPsePortExtDetailedStatus_Type(Integer32):
    """Custom type bspePethPsePortExtDetailedStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
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
              16)
        )
    )
    namedValues = NamedValues(
        *(("poweredResistiveDiscovery", 1),
          ("poweredCapacitiveDiscovery", 2),
          ("poweredCiscoLegacyDiscovery", 3),
          ("invalidPD", 4),
          ("overloadFault", 5),
          ("underloadFault", 6),
          ("uvovFault", 7),
          ("powerManaged", 8),
          ("limitOverloadFault", 9),
          ("discoveryDisabled", 10),
          ("unableToResetTps", 11),
          ("unableToInitializeTps", 12),
          ("uninitialized", 13),
          ("nonexistent", 14),
          ("otherFault", 15),
          ("detectionStatus", 16))
    )


_BspePethPsePortExtDetailedStatus_Type.__name__ = "Integer32"
_BspePethPsePortExtDetailedStatus_Object = MibTableColumn
bspePethPsePortExtDetailedStatus = _BspePethPsePortExtDetailedStatus_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 8, 1, 1, 1, 4),
    _BspePethPsePortExtDetailedStatus_Type()
)
bspePethPsePortExtDetailedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bspePethPsePortExtDetailedStatus.setStatus("current")


class _BspePethPsePortExtMeasuredVoltage_Type(Gauge32):
    """Custom type bspePethPsePortExtMeasuredVoltage based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(400, 580),
    )


_BspePethPsePortExtMeasuredVoltage_Type.__name__ = "Gauge32"
_BspePethPsePortExtMeasuredVoltage_Object = MibTableColumn
bspePethPsePortExtMeasuredVoltage = _BspePethPsePortExtMeasuredVoltage_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 8, 1, 1, 1, 5),
    _BspePethPsePortExtMeasuredVoltage_Type()
)
bspePethPsePortExtMeasuredVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bspePethPsePortExtMeasuredVoltage.setStatus("current")
if mibBuilder.loadTexts:
    bspePethPsePortExtMeasuredVoltage.setUnits("decivolts")


class _BspePethPsePortExtMeasuredCurrent_Type(Gauge32):
    """Custom type bspePethPsePortExtMeasuredCurrent based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1920),
    )


_BspePethPsePortExtMeasuredCurrent_Type.__name__ = "Gauge32"
_BspePethPsePortExtMeasuredCurrent_Object = MibTableColumn
bspePethPsePortExtMeasuredCurrent = _BspePethPsePortExtMeasuredCurrent_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 8, 1, 1, 1, 6),
    _BspePethPsePortExtMeasuredCurrent_Type()
)
bspePethPsePortExtMeasuredCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bspePethPsePortExtMeasuredCurrent.setStatus("current")
if mibBuilder.loadTexts:
    bspePethPsePortExtMeasuredCurrent.setUnits("milliamps")


class _BspePethPsePortExtMeasuredPower_Type(Gauge32):
    """Custom type bspePethPsePortExtMeasuredPower based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 98000),
    )


_BspePethPsePortExtMeasuredPower_Type.__name__ = "Gauge32"
_BspePethPsePortExtMeasuredPower_Object = MibTableColumn
bspePethPsePortExtMeasuredPower = _BspePethPsePortExtMeasuredPower_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 8, 1, 1, 1, 7),
    _BspePethPsePortExtMeasuredPower_Type()
)
bspePethPsePortExtMeasuredPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bspePethPsePortExtMeasuredPower.setStatus("current")
if mibBuilder.loadTexts:
    bspePethPsePortExtMeasuredPower.setUnits("milliwatts")


class _BspePethPsePortExtCurrentStatus_Type(Integer32):
    """Custom type bspePethPsePortExtCurrentStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("ok", 1),
          ("underCurrent", 2),
          ("overCurrent", 3),
          ("both", 4))
    )


_BspePethPsePortExtCurrentStatus_Type.__name__ = "Integer32"
_BspePethPsePortExtCurrentStatus_Object = MibTableColumn
bspePethPsePortExtCurrentStatus = _BspePethPsePortExtCurrentStatus_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 8, 1, 1, 1, 8),
    _BspePethPsePortExtCurrentStatus_Type()
)
bspePethPsePortExtCurrentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bspePethPsePortExtCurrentStatus.setStatus("current")


class _BspePethPsePortExtCurrentStatusClear_Type(Integer32):
    """Custom type bspePethPsePortExtCurrentStatusClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 1),
          ("off", 2))
    )


_BspePethPsePortExtCurrentStatusClear_Type.__name__ = "Integer32"
_BspePethPsePortExtCurrentStatusClear_Object = MibTableColumn
bspePethPsePortExtCurrentStatusClear = _BspePethPsePortExtCurrentStatusClear_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 8, 1, 1, 1, 9),
    _BspePethPsePortExtCurrentStatusClear_Type()
)
bspePethPsePortExtCurrentStatusClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bspePethPsePortExtCurrentStatusClear.setStatus("current")


class _BspePethPsePortExtPowerUpMode_Type(Integer32):
    """Custom type bspePethPsePortExtPowerUpMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("dot3af", 1),
          ("highInrush", 2),
          ("pre802dot3at", 3),
          ("dot3at", 4))
    )


_BspePethPsePortExtPowerUpMode_Type.__name__ = "Integer32"
_BspePethPsePortExtPowerUpMode_Object = MibTableColumn
bspePethPsePortExtPowerUpMode = _BspePethPsePortExtPowerUpMode_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 8, 1, 1, 1, 10),
    _BspePethPsePortExtPowerUpMode_Type()
)
bspePethPsePortExtPowerUpMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bspePethPsePortExtPowerUpMode.setStatus("current")


class _BspePethPsePortExtPowerPairs_Type(Integer32):
    """Custom type bspePethPsePortExtPowerPairs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("signal", 1),
          ("spare", 2),
          ("both", 3))
    )


_BspePethPsePortExtPowerPairs_Type.__name__ = "Integer32"
_BspePethPsePortExtPowerPairs_Object = MibTableColumn
bspePethPsePortExtPowerPairs = _BspePethPsePortExtPowerPairs_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 8, 1, 1, 1, 11),
    _BspePethPsePortExtPowerPairs_Type()
)
bspePethPsePortExtPowerPairs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bspePethPsePortExtPowerPairs.setStatus("current")


class _BspePethPsePortExtLldp_Type(Integer32):
    """Custom type bspePethPsePortExtLldp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_BspePethPsePortExtLldp_Type.__name__ = "Integer32"
_BspePethPsePortExtLldp_Object = MibTableColumn
bspePethPsePortExtLldp = _BspePethPsePortExtLldp_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 8, 1, 1, 1, 12),
    _BspePethPsePortExtLldp_Type()
)
bspePethPsePortExtLldp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bspePethPsePortExtLldp.setStatus("current")
_BspePethPsePortFastPoeEnable_Type = TruthValue
_BspePethPsePortFastPoeEnable_Object = MibTableColumn
bspePethPsePortFastPoeEnable = _BspePethPsePortFastPoeEnable_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 8, 1, 1, 1, 13),
    _BspePethPsePortFastPoeEnable_Type()
)
bspePethPsePortFastPoeEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bspePethPsePortFastPoeEnable.setStatus("current")
_BspePethPsePortPerpetualPoeEnable_Type = TruthValue
_BspePethPsePortPerpetualPoeEnable_Object = MibTableColumn
bspePethPsePortPerpetualPoeEnable = _BspePethPsePortPerpetualPoeEnable_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 8, 1, 1, 1, 14),
    _BspePethPsePortPerpetualPoeEnable_Type()
)
bspePethPsePortPerpetualPoeEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bspePethPsePortPerpetualPoeEnable.setStatus("current")


class _BspePethPsePortPowerClassifications_Type(Integer32):
    """Custom type bspePethPsePortPowerClassifications based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("class0", 1),
          ("class1", 2),
          ("class2", 3),
          ("class3", 4),
          ("class4", 5),
          ("class5", 6),
          ("class6", 7),
          ("class7", 8),
          ("class8", 9))
    )


_BspePethPsePortPowerClassifications_Type.__name__ = "Integer32"
_BspePethPsePortPowerClassifications_Object = MibTableColumn
bspePethPsePortPowerClassifications = _BspePethPsePortPowerClassifications_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 8, 1, 1, 1, 15),
    _BspePethPsePortPowerClassifications_Type()
)
bspePethPsePortPowerClassifications.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bspePethPsePortPowerClassifications.setStatus("current")
_BspePethMainPseExtTable_Object = MibTable
bspePethMainPseExtTable = _BspePethMainPseExtTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 8, 1, 2)
)
if mibBuilder.loadTexts:
    bspePethMainPseExtTable.setStatus("current")
_BspePethMainPseExtEntry_Object = MibTableRow
bspePethMainPseExtEntry = _BspePethMainPseExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 8, 1, 2, 1)
)
bspePethMainPseExtEntry.setIndexNames(
    (0, "BAY-STACK-PETH-EXT-MIB", "bspePethMainPseExtGroupIndex"),
)
if mibBuilder.loadTexts:
    bspePethMainPseExtEntry.setStatus("current")


class _BspePethMainPseExtGroupIndex_Type(Integer32):
    """Custom type bspePethMainPseExtGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_BspePethMainPseExtGroupIndex_Type.__name__ = "Integer32"
_BspePethMainPseExtGroupIndex_Object = MibTableColumn
bspePethMainPseExtGroupIndex = _BspePethMainPseExtGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 8, 1, 2, 1, 1),
    _BspePethMainPseExtGroupIndex_Type()
)
bspePethMainPseExtGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bspePethMainPseExtGroupIndex.setStatus("current")


class _BspePethMainPseExtPowerPresent_Type(Integer32):
    """Custom type bspePethMainPseExtPowerPresent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("acOnly", 1),
          ("dcOnly", 2),
          ("acDc", 3))
    )


_BspePethMainPseExtPowerPresent_Type.__name__ = "Integer32"
_BspePethMainPseExtPowerPresent_Object = MibTableColumn
bspePethMainPseExtPowerPresent = _BspePethMainPseExtPowerPresent_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 8, 1, 2, 1, 2),
    _BspePethMainPseExtPowerPresent_Type()
)
bspePethMainPseExtPowerPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bspePethMainPseExtPowerPresent.setStatus("current")


class _BspePethMainPseExtDisconnectScheme_Type(Integer32):
    """Custom type bspePethMainPseExtDisconnectScheme based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("acDisconnect", 1),
          ("dcDisconnect", 2))
    )


_BspePethMainPseExtDisconnectScheme_Type.__name__ = "Integer32"
_BspePethMainPseExtDisconnectScheme_Object = MibTableColumn
bspePethMainPseExtDisconnectScheme = _BspePethMainPseExtDisconnectScheme_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 8, 1, 2, 1, 3),
    _BspePethMainPseExtDisconnectScheme_Type()
)
bspePethMainPseExtDisconnectScheme.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bspePethMainPseExtDisconnectScheme.setStatus("current")
_BspePethMainPseFastPoeEnable_Type = TruthValue
_BspePethMainPseFastPoeEnable_Object = MibTableColumn
bspePethMainPseFastPoeEnable = _BspePethMainPseFastPoeEnable_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 8, 1, 2, 1, 4),
    _BspePethMainPseFastPoeEnable_Type()
)
bspePethMainPseFastPoeEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bspePethMainPseFastPoeEnable.setStatus("current")
_BspePethMainPsePerpetualPoeEnable_Type = TruthValue
_BspePethMainPsePerpetualPoeEnable_Object = MibTableColumn
bspePethMainPsePerpetualPoeEnable = _BspePethMainPsePerpetualPoeEnable_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 8, 1, 2, 1, 5),
    _BspePethMainPsePerpetualPoeEnable_Type()
)
bspePethMainPsePerpetualPoeEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bspePethMainPsePerpetualPoeEnable.setStatus("current")
_BspeScalars_ObjectIdentity = ObjectIdentity
bspeScalars = _BspeScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 5, 8, 1, 3)
)


class _BspeIpPhonePowerLimit_Type(Integer32):
    """Custom type bspeIpPhonePowerLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(3, 32),
    )


_BspeIpPhonePowerLimit_Type.__name__ = "Integer32"
_BspeIpPhonePowerLimit_Object = MibScalar
bspeIpPhonePowerLimit = _BspeIpPhonePowerLimit_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 8, 1, 3, 1),
    _BspeIpPhonePowerLimit_Type()
)
bspeIpPhonePowerLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bspeIpPhonePowerLimit.setStatus("current")
if mibBuilder.loadTexts:
    bspeIpPhonePowerLimit.setUnits("watts")


class _BspeIpPhonePowerPriority_Type(Integer32):
    """Custom type bspeIpPhonePowerPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("critical", 1),
          ("high", 2),
          ("low", 3),
          ("notApplicable", 4))
    )


_BspeIpPhonePowerPriority_Type.__name__ = "Integer32"
_BspeIpPhonePowerPriority_Object = MibScalar
bspeIpPhonePowerPriority = _BspeIpPhonePowerPriority_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 8, 1, 3, 2),
    _BspeIpPhonePowerPriority_Type()
)
bspeIpPhonePowerPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bspeIpPhonePowerPriority.setStatus("current")


class _BspePoEPowerMode_Type(Integer32):
    """Custom type bspePoEPowerMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("lowPowerBudget", 1),
          ("highPowerBudget", 2))
    )


_BspePoEPowerMode_Type.__name__ = "Integer32"
_BspePoEPowerMode_Object = MibScalar
bspePoEPowerMode = _BspePoEPowerMode_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 8, 1, 3, 3),
    _BspePoEPowerMode_Type()
)
bspePoEPowerMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bspePoEPowerMode.setStatus("current")

# Managed Objects groups


# Notification objects

bspePethPsePortCurrentStatusNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 5, 8, 0, 1)
)
bspePethPsePortCurrentStatusNotification.setObjects(
    ("BAY-STACK-PETH-EXT-MIB", "bspePethPsePortExtCurrentStatus")
)
if mibBuilder.loadTexts:
    bspePethPsePortCurrentStatusNotification.setStatus(
        "current"
    )

bspeIpPhonePowerLimitNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 5, 8, 0, 2)
)
bspeIpPhonePowerLimitNotification.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("BAY-STACK-PETH-EXT-MIB", "bspeIpPhonePowerLimit"))
)
if mibBuilder.loadTexts:
    bspeIpPhonePowerLimitNotification.setStatus(
        "current"
    )

bspeIpPhonePowerPriorityNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 5, 8, 0, 3)
)
bspeIpPhonePowerPriorityNotification.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("BAY-STACK-PETH-EXT-MIB", "bspeIpPhonePowerPriority"))
)
if mibBuilder.loadTexts:
    bspeIpPhonePowerPriorityNotification.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BAY-STACK-PETH-EXT-MIB",
    **{"bayStackPethExtMib": bayStackPethExtMib,
       "bspeNotifications": bspeNotifications,
       "bspePethPsePortCurrentStatusNotification": bspePethPsePortCurrentStatusNotification,
       "bspeIpPhonePowerLimitNotification": bspeIpPhonePowerLimitNotification,
       "bspeIpPhonePowerPriorityNotification": bspeIpPhonePowerPriorityNotification,
       "bspeObjects": bspeObjects,
       "bspePethPsePortExtTable": bspePethPsePortExtTable,
       "bspePethPsePortExtEntry": bspePethPsePortExtEntry,
       "bspePethPsePortExtGroupIndex": bspePethPsePortExtGroupIndex,
       "bspePethPsePortExtIndex": bspePethPsePortExtIndex,
       "bspePethPsePortExtPowerLimit": bspePethPsePortExtPowerLimit,
       "bspePethPsePortExtDetailedStatus": bspePethPsePortExtDetailedStatus,
       "bspePethPsePortExtMeasuredVoltage": bspePethPsePortExtMeasuredVoltage,
       "bspePethPsePortExtMeasuredCurrent": bspePethPsePortExtMeasuredCurrent,
       "bspePethPsePortExtMeasuredPower": bspePethPsePortExtMeasuredPower,
       "bspePethPsePortExtCurrentStatus": bspePethPsePortExtCurrentStatus,
       "bspePethPsePortExtCurrentStatusClear": bspePethPsePortExtCurrentStatusClear,
       "bspePethPsePortExtPowerUpMode": bspePethPsePortExtPowerUpMode,
       "bspePethPsePortExtPowerPairs": bspePethPsePortExtPowerPairs,
       "bspePethPsePortExtLldp": bspePethPsePortExtLldp,
       "bspePethPsePortFastPoeEnable": bspePethPsePortFastPoeEnable,
       "bspePethPsePortPerpetualPoeEnable": bspePethPsePortPerpetualPoeEnable,
       "bspePethPsePortPowerClassifications": bspePethPsePortPowerClassifications,
       "bspePethMainPseExtTable": bspePethMainPseExtTable,
       "bspePethMainPseExtEntry": bspePethMainPseExtEntry,
       "bspePethMainPseExtGroupIndex": bspePethMainPseExtGroupIndex,
       "bspePethMainPseExtPowerPresent": bspePethMainPseExtPowerPresent,
       "bspePethMainPseExtDisconnectScheme": bspePethMainPseExtDisconnectScheme,
       "bspePethMainPseFastPoeEnable": bspePethMainPseFastPoeEnable,
       "bspePethMainPsePerpetualPoeEnable": bspePethMainPsePerpetualPoeEnable,
       "bspeScalars": bspeScalars,
       "bspeIpPhonePowerLimit": bspeIpPhonePowerLimit,
       "bspeIpPhonePowerPriority": bspeIpPhonePowerPriority,
       "bspePoEPowerMode": bspePoEPowerMode}
)
