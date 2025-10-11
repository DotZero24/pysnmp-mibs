# SNMP MIB module (ELECTROLINE-DHT-GLOBAL-FIBERNODE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/electroline/ELECTROLINE-DHT-GLOBAL-FIBERNODE-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:07:07 2025
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

(dhtExtensionsMibObjects,) = mibBuilder.importSymbols(
    "ELECTROLINE-DHT-EXTENSIONS-MIB",
    "dhtExtensionsMibObjects")

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


# MODULE-IDENTITY

dhtGlobalFnIdentMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 14)
)
if mibBuilder.loadTexts:
    dhtGlobalFnIdentMIB.setRevisions(
        ("2004-12-10 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_GlobalFnIdentObjects_ObjectIdentity = ObjectIdentity
globalFnIdentObjects = _GlobalFnIdentObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 14, 1)
)


class _GlobalFnNumberReturnLaser_Type(Integer32):
    """Custom type globalFnNumberReturnLaser based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_GlobalFnNumberReturnLaser_Type.__name__ = "Integer32"
_GlobalFnNumberReturnLaser_Object = MibScalar
globalFnNumberReturnLaser = _GlobalFnNumberReturnLaser_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 14, 1, 1),
    _GlobalFnNumberReturnLaser_Type()
)
globalFnNumberReturnLaser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalFnNumberReturnLaser.setStatus("current")
_GlobalFnReturnLaserTable_Object = MibTable
globalFnReturnLaserTable = _GlobalFnReturnLaserTable_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 14, 1, 2)
)
if mibBuilder.loadTexts:
    globalFnReturnLaserTable.setStatus("current")
_GlobalFnReturnLaserTableEntry_Object = MibTableRow
globalFnReturnLaserTableEntry = _GlobalFnReturnLaserTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 14, 1, 2, 1)
)
globalFnReturnLaserTableEntry.setIndexNames(
    (0, "ELECTROLINE-DHT-GLOBAL-FIBERNODE-MIB", "globalFnReturnLaserIndex"),
)
if mibBuilder.loadTexts:
    globalFnReturnLaserTableEntry.setStatus("current")
_GlobalFnReturnLaserIndex_Type = Integer32
_GlobalFnReturnLaserIndex_Object = MibTableColumn
globalFnReturnLaserIndex = _GlobalFnReturnLaserIndex_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 14, 1, 2, 1, 1),
    _GlobalFnReturnLaserIndex_Type()
)
globalFnReturnLaserIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalFnReturnLaserIndex.setStatus("current")


class _GlobalFnReturnLaserState_Type(Integer32):
    """Custom type globalFnReturnLaserState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unavailable", 1),
          ("available", 2))
    )


_GlobalFnReturnLaserState_Type.__name__ = "Integer32"
_GlobalFnReturnLaserState_Object = MibTableColumn
globalFnReturnLaserState = _GlobalFnReturnLaserState_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 14, 1, 2, 1, 2),
    _GlobalFnReturnLaserState_Type()
)
globalFnReturnLaserState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalFnReturnLaserState.setStatus("current")
_GlobalFnReturnLaserRFLevel_Type = Integer32
_GlobalFnReturnLaserRFLevel_Object = MibTableColumn
globalFnReturnLaserRFLevel = _GlobalFnReturnLaserRFLevel_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 14, 1, 2, 1, 3),
    _GlobalFnReturnLaserRFLevel_Type()
)
globalFnReturnLaserRFLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalFnReturnLaserRFLevel.setStatus("current")


class _GlobalFnReturnLaserRFControl_Type(Integer32):
    """Custom type globalFnReturnLaserRFControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_GlobalFnReturnLaserRFControl_Type.__name__ = "Integer32"
_GlobalFnReturnLaserRFControl_Object = MibTableColumn
globalFnReturnLaserRFControl = _GlobalFnReturnLaserRFControl_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 14, 1, 2, 1, 4),
    _GlobalFnReturnLaserRFControl_Type()
)
globalFnReturnLaserRFControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    globalFnReturnLaserRFControl.setStatus("current")
_GlobalFnReturnLaserElecAttenuator_Type = Integer32
_GlobalFnReturnLaserElecAttenuator_Object = MibTableColumn
globalFnReturnLaserElecAttenuator = _GlobalFnReturnLaserElecAttenuator_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 14, 1, 2, 1, 5),
    _GlobalFnReturnLaserElecAttenuator_Type()
)
globalFnReturnLaserElecAttenuator.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    globalFnReturnLaserElecAttenuator.setStatus("current")


class _GlobalFnNumberOpticalReceiver_Type(Integer32):
    """Custom type globalFnNumberOpticalReceiver based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_GlobalFnNumberOpticalReceiver_Type.__name__ = "Integer32"
_GlobalFnNumberOpticalReceiver_Object = MibScalar
globalFnNumberOpticalReceiver = _GlobalFnNumberOpticalReceiver_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 14, 1, 3),
    _GlobalFnNumberOpticalReceiver_Type()
)
globalFnNumberOpticalReceiver.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalFnNumberOpticalReceiver.setStatus("current")


class _GlobalFnOpticalReceiverAGCState_Type(Integer32):
    """Custom type globalFnOpticalReceiverAGCState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_GlobalFnOpticalReceiverAGCState_Type.__name__ = "Integer32"
_GlobalFnOpticalReceiverAGCState_Object = MibScalar
globalFnOpticalReceiverAGCState = _GlobalFnOpticalReceiverAGCState_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 14, 1, 4),
    _GlobalFnOpticalReceiverAGCState_Type()
)
globalFnOpticalReceiverAGCState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalFnOpticalReceiverAGCState.setStatus("current")


class _GlobalFnOpticalReceiverAGCControl_Type(Integer32):
    """Custom type globalFnOpticalReceiverAGCControl based on Integer32"""
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
        *(("frx1-agc-off", 1),
          ("frx1-agc-on", 2),
          ("frx2-agc-off", 3),
          ("frx2-agc-on", 4))
    )


_GlobalFnOpticalReceiverAGCControl_Type.__name__ = "Integer32"
_GlobalFnOpticalReceiverAGCControl_Object = MibScalar
globalFnOpticalReceiverAGCControl = _GlobalFnOpticalReceiverAGCControl_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 14, 1, 5),
    _GlobalFnOpticalReceiverAGCControl_Type()
)
globalFnOpticalReceiverAGCControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    globalFnOpticalReceiverAGCControl.setStatus("current")
_GlobalFnOpticalReceiverTable_Object = MibTable
globalFnOpticalReceiverTable = _GlobalFnOpticalReceiverTable_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 14, 1, 6)
)
if mibBuilder.loadTexts:
    globalFnOpticalReceiverTable.setStatus("current")
_GlobalFnOpticalReceiverTableEntry_Object = MibTableRow
globalFnOpticalReceiverTableEntry = _GlobalFnOpticalReceiverTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 14, 1, 6, 1)
)
globalFnOpticalReceiverTableEntry.setIndexNames(
    (0, "ELECTROLINE-DHT-GLOBAL-FIBERNODE-MIB", "globalFnOpticalReceiverIndex"),
)
if mibBuilder.loadTexts:
    globalFnOpticalReceiverTableEntry.setStatus("current")
_GlobalFnOpticalReceiverIndex_Type = Integer32
_GlobalFnOpticalReceiverIndex_Object = MibTableColumn
globalFnOpticalReceiverIndex = _GlobalFnOpticalReceiverIndex_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 14, 1, 6, 1, 1),
    _GlobalFnOpticalReceiverIndex_Type()
)
globalFnOpticalReceiverIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalFnOpticalReceiverIndex.setStatus("current")


class _GlobalFnOpticalReceiverState_Type(Integer32):
    """Custom type globalFnOpticalReceiverState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unavailable", 1),
          ("available", 2))
    )


_GlobalFnOpticalReceiverState_Type.__name__ = "Integer32"
_GlobalFnOpticalReceiverState_Object = MibTableColumn
globalFnOpticalReceiverState = _GlobalFnOpticalReceiverState_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 14, 1, 6, 1, 2),
    _GlobalFnOpticalReceiverState_Type()
)
globalFnOpticalReceiverState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalFnOpticalReceiverState.setStatus("current")


class _GlobalFnOpticalReceiverType_Type(DisplayString):
    """Custom type globalFnOpticalReceiverType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_GlobalFnOpticalReceiverType_Type.__name__ = "DisplayString"
_GlobalFnOpticalReceiverType_Object = MibTableColumn
globalFnOpticalReceiverType = _GlobalFnOpticalReceiverType_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 14, 1, 6, 1, 3),
    _GlobalFnOpticalReceiverType_Type()
)
globalFnOpticalReceiverType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalFnOpticalReceiverType.setStatus("optional")
_GlobalFnOpticalReceiverRFLevel_Type = Integer32
_GlobalFnOpticalReceiverRFLevel_Object = MibTableColumn
globalFnOpticalReceiverRFLevel = _GlobalFnOpticalReceiverRFLevel_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 14, 1, 6, 1, 4),
    _GlobalFnOpticalReceiverRFLevel_Type()
)
globalFnOpticalReceiverRFLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalFnOpticalReceiverRFLevel.setStatus("current")


class _GlobalFnOpticalReceiverRFControl_Type(Integer32):
    """Custom type globalFnOpticalReceiverRFControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_GlobalFnOpticalReceiverRFControl_Type.__name__ = "Integer32"
_GlobalFnOpticalReceiverRFControl_Object = MibTableColumn
globalFnOpticalReceiverRFControl = _GlobalFnOpticalReceiverRFControl_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 14, 1, 6, 1, 5),
    _GlobalFnOpticalReceiverRFControl_Type()
)
globalFnOpticalReceiverRFControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    globalFnOpticalReceiverRFControl.setStatus("current")
_GlobalFnOpticalReceiverElecAttenuator_Type = Integer32
_GlobalFnOpticalReceiverElecAttenuator_Object = MibTableColumn
globalFnOpticalReceiverElecAttenuator = _GlobalFnOpticalReceiverElecAttenuator_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 14, 1, 6, 1, 6),
    _GlobalFnOpticalReceiverElecAttenuator_Type()
)
globalFnOpticalReceiverElecAttenuator.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    globalFnOpticalReceiverElecAttenuator.setStatus("current")


class _GlobalFnNumberWingSwitch_Type(Integer32):
    """Custom type globalFnNumberWingSwitch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_GlobalFnNumberWingSwitch_Type.__name__ = "Integer32"
_GlobalFnNumberWingSwitch_Object = MibScalar
globalFnNumberWingSwitch = _GlobalFnNumberWingSwitch_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 14, 1, 7),
    _GlobalFnNumberWingSwitch_Type()
)
globalFnNumberWingSwitch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalFnNumberWingSwitch.setStatus("current")
_GlobalFnWingSwitchTable_Object = MibTable
globalFnWingSwitchTable = _GlobalFnWingSwitchTable_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 14, 1, 8)
)
if mibBuilder.loadTexts:
    globalFnWingSwitchTable.setStatus("current")
_GlobalFnWingSwitchTableEntry_Object = MibTableRow
globalFnWingSwitchTableEntry = _GlobalFnWingSwitchTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 14, 1, 8, 1)
)
globalFnWingSwitchTableEntry.setIndexNames(
    (0, "ELECTROLINE-DHT-GLOBAL-FIBERNODE-MIB", "globalFnWingSwitchIndex"),
)
if mibBuilder.loadTexts:
    globalFnWingSwitchTableEntry.setStatus("current")
_GlobalFnWingSwitchIndex_Type = Integer32
_GlobalFnWingSwitchIndex_Object = MibTableColumn
globalFnWingSwitchIndex = _GlobalFnWingSwitchIndex_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 14, 1, 8, 1, 1),
    _GlobalFnWingSwitchIndex_Type()
)
globalFnWingSwitchIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalFnWingSwitchIndex.setStatus("current")


class _GlobalFnWingSwitchState_Type(Integer32):
    """Custom type globalFnWingSwitchState based on Integer32"""
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
        *(("unavailable", 0),
          ("off", 1),
          ("sixDb", 2),
          ("normal", 3))
    )


_GlobalFnWingSwitchState_Type.__name__ = "Integer32"
_GlobalFnWingSwitchState_Object = MibTableColumn
globalFnWingSwitchState = _GlobalFnWingSwitchState_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 14, 1, 8, 1, 2),
    _GlobalFnWingSwitchState_Type()
)
globalFnWingSwitchState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalFnWingSwitchState.setStatus("current")


class _GlobalFnWingSwitchControl_Type(Integer32):
    """Custom type globalFnWingSwitchControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("sixDb", 2),
          ("normal", 3))
    )


_GlobalFnWingSwitchControl_Type.__name__ = "Integer32"
_GlobalFnWingSwitchControl_Object = MibTableColumn
globalFnWingSwitchControl = _GlobalFnWingSwitchControl_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 14, 1, 8, 1, 3),
    _GlobalFnWingSwitchControl_Type()
)
globalFnWingSwitchControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    globalFnWingSwitchControl.setStatus("current")


class _GlobalFnNumberRFRouter_Type(Integer32):
    """Custom type globalFnNumberRFRouter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_GlobalFnNumberRFRouter_Type.__name__ = "Integer32"
_GlobalFnNumberRFRouter_Object = MibScalar
globalFnNumberRFRouter = _GlobalFnNumberRFRouter_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 14, 1, 9),
    _GlobalFnNumberRFRouter_Type()
)
globalFnNumberRFRouter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalFnNumberRFRouter.setStatus("current")
_GlobalFnRFRouterTable_Object = MibTable
globalFnRFRouterTable = _GlobalFnRFRouterTable_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 14, 1, 10)
)
if mibBuilder.loadTexts:
    globalFnRFRouterTable.setStatus("current")
_GlobalRFRouterTableEntry_Object = MibTableRow
globalRFRouterTableEntry = _GlobalRFRouterTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 14, 1, 10, 1)
)
globalRFRouterTableEntry.setIndexNames(
    (0, "ELECTROLINE-DHT-GLOBAL-FIBERNODE-MIB", "globalFnRFRouterIndex"),
)
if mibBuilder.loadTexts:
    globalRFRouterTableEntry.setStatus("current")
_GlobalFnRFRouterIndex_Type = Integer32
_GlobalFnRFRouterIndex_Object = MibTableColumn
globalFnRFRouterIndex = _GlobalFnRFRouterIndex_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 14, 1, 10, 1, 1),
    _GlobalFnRFRouterIndex_Type()
)
globalFnRFRouterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalFnRFRouterIndex.setStatus("current")


class _GlobalFnRFRouterType_Type(DisplayString):
    """Custom type globalFnRFRouterType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_GlobalFnRFRouterType_Type.__name__ = "DisplayString"
_GlobalFnRFRouterType_Object = MibTableColumn
globalFnRFRouterType = _GlobalFnRFRouterType_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 14, 1, 10, 1, 2),
    _GlobalFnRFRouterType_Type()
)
globalFnRFRouterType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalFnRFRouterType.setStatus("current")


class _GlobalFnRFRouterDownstreamSwitchState_Type(Integer32):
    """Custom type globalFnRFRouterDownstreamSwitchState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unavailable", 0),
          ("redundantMode", 1),
          ("segmentation", 2))
    )


_GlobalFnRFRouterDownstreamSwitchState_Type.__name__ = "Integer32"
_GlobalFnRFRouterDownstreamSwitchState_Object = MibTableColumn
globalFnRFRouterDownstreamSwitchState = _GlobalFnRFRouterDownstreamSwitchState_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 14, 1, 10, 1, 3),
    _GlobalFnRFRouterDownstreamSwitchState_Type()
)
globalFnRFRouterDownstreamSwitchState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalFnRFRouterDownstreamSwitchState.setStatus("current")


class _GlobalFnRFRouterDownstreamSwitchControl_Type(Integer32):
    """Custom type globalFnRFRouterDownstreamSwitchControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("redundantMode", 1),
          ("segmentation", 2))
    )


_GlobalFnRFRouterDownstreamSwitchControl_Type.__name__ = "Integer32"
_GlobalFnRFRouterDownstreamSwitchControl_Object = MibTableColumn
globalFnRFRouterDownstreamSwitchControl = _GlobalFnRFRouterDownstreamSwitchControl_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 14, 1, 10, 1, 4),
    _GlobalFnRFRouterDownstreamSwitchControl_Type()
)
globalFnRFRouterDownstreamSwitchControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    globalFnRFRouterDownstreamSwitchControl.setStatus("current")


class _GlobalFnRFRouterDownstreamControlTypeState_Type(Integer32):
    """Custom type globalFnRFRouterDownstreamControlTypeState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("remote", 0),
          ("local", 1))
    )


_GlobalFnRFRouterDownstreamControlTypeState_Type.__name__ = "Integer32"
_GlobalFnRFRouterDownstreamControlTypeState_Object = MibTableColumn
globalFnRFRouterDownstreamControlTypeState = _GlobalFnRFRouterDownstreamControlTypeState_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 14, 1, 10, 1, 5),
    _GlobalFnRFRouterDownstreamControlTypeState_Type()
)
globalFnRFRouterDownstreamControlTypeState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalFnRFRouterDownstreamControlTypeState.setStatus("current")


class _GlobalFnRFRouterDownstreamControlTypeSetting_Type(Integer32):
    """Custom type globalFnRFRouterDownstreamControlTypeSetting based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("remote", 0),
          ("local", 1))
    )


_GlobalFnRFRouterDownstreamControlTypeSetting_Type.__name__ = "Integer32"
_GlobalFnRFRouterDownstreamControlTypeSetting_Object = MibTableColumn
globalFnRFRouterDownstreamControlTypeSetting = _GlobalFnRFRouterDownstreamControlTypeSetting_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 14, 1, 10, 1, 6),
    _GlobalFnRFRouterDownstreamControlTypeSetting_Type()
)
globalFnRFRouterDownstreamControlTypeSetting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    globalFnRFRouterDownstreamControlTypeSetting.setStatus("current")


class _GlobalFnRFRouterUptreamSwitchState_Type(Integer32):
    """Custom type globalFnRFRouterUptreamSwitchState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unavailable", 0),
          ("redundantMode", 1),
          ("segmentation", 2))
    )


_GlobalFnRFRouterUptreamSwitchState_Type.__name__ = "Integer32"
_GlobalFnRFRouterUptreamSwitchState_Object = MibTableColumn
globalFnRFRouterUptreamSwitchState = _GlobalFnRFRouterUptreamSwitchState_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 14, 1, 10, 1, 7),
    _GlobalFnRFRouterUptreamSwitchState_Type()
)
globalFnRFRouterUptreamSwitchState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalFnRFRouterUptreamSwitchState.setStatus("current")


class _GlobalFnRFRouterUptreamSwitchControl_Type(Integer32):
    """Custom type globalFnRFRouterUptreamSwitchControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("redundantMode", 1),
          ("segmentation", 2))
    )


_GlobalFnRFRouterUptreamSwitchControl_Type.__name__ = "Integer32"
_GlobalFnRFRouterUptreamSwitchControl_Object = MibTableColumn
globalFnRFRouterUptreamSwitchControl = _GlobalFnRFRouterUptreamSwitchControl_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 14, 1, 10, 1, 8),
    _GlobalFnRFRouterUptreamSwitchControl_Type()
)
globalFnRFRouterUptreamSwitchControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    globalFnRFRouterUptreamSwitchControl.setStatus("current")


class _GlobalFnRFRouterUpstreamControlTypeState_Type(Integer32):
    """Custom type globalFnRFRouterUpstreamControlTypeState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("remote", 0),
          ("local", 1))
    )


_GlobalFnRFRouterUpstreamControlTypeState_Type.__name__ = "Integer32"
_GlobalFnRFRouterUpstreamControlTypeState_Object = MibTableColumn
globalFnRFRouterUpstreamControlTypeState = _GlobalFnRFRouterUpstreamControlTypeState_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 14, 1, 10, 1, 9),
    _GlobalFnRFRouterUpstreamControlTypeState_Type()
)
globalFnRFRouterUpstreamControlTypeState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalFnRFRouterUpstreamControlTypeState.setStatus("current")


class _GlobalFnRFRouterUpstreamControlTypeSetting_Type(Integer32):
    """Custom type globalFnRFRouterUpstreamControlTypeSetting based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("remote", 0),
          ("local", 1))
    )


_GlobalFnRFRouterUpstreamControlTypeSetting_Type.__name__ = "Integer32"
_GlobalFnRFRouterUpstreamControlTypeSetting_Object = MibTableColumn
globalFnRFRouterUpstreamControlTypeSetting = _GlobalFnRFRouterUpstreamControlTypeSetting_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 14, 1, 10, 1, 10),
    _GlobalFnRFRouterUpstreamControlTypeSetting_Type()
)
globalFnRFRouterUpstreamControlTypeSetting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    globalFnRFRouterUpstreamControlTypeSetting.setStatus("current")


class _GlobalFnNumberRFPort_Type(Integer32):
    """Custom type globalFnNumberRFPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_GlobalFnNumberRFPort_Type.__name__ = "Integer32"
_GlobalFnNumberRFPort_Object = MibScalar
globalFnNumberRFPort = _GlobalFnNumberRFPort_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 14, 1, 11),
    _GlobalFnNumberRFPort_Type()
)
globalFnNumberRFPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalFnNumberRFPort.setStatus("current")


class _GlobalRFLinkSwitchState_Type(Integer32):
    """Custom type globalRFLinkSwitchState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_GlobalRFLinkSwitchState_Type.__name__ = "Integer32"
_GlobalRFLinkSwitchState_Object = MibScalar
globalRFLinkSwitchState = _GlobalRFLinkSwitchState_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 14, 1, 12),
    _GlobalRFLinkSwitchState_Type()
)
globalRFLinkSwitchState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalRFLinkSwitchState.setStatus("current")


class _GlobalReverseRFLinkSwitchState_Type(Integer32):
    """Custom type globalReverseRFLinkSwitchState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_GlobalReverseRFLinkSwitchState_Type.__name__ = "Integer32"
_GlobalReverseRFLinkSwitchState_Object = MibScalar
globalReverseRFLinkSwitchState = _GlobalReverseRFLinkSwitchState_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 14, 1, 13),
    _GlobalReverseRFLinkSwitchState_Type()
)
globalReverseRFLinkSwitchState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalReverseRFLinkSwitchState.setStatus("current")


class _GlobalReverseRFLinkSwitchControl_Type(Integer32):
    """Custom type globalReverseRFLinkSwitchControl based on Integer32"""
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
        *(("path1-off", 1),
          ("path1-on", 2),
          ("path2-off", 3),
          ("path2-on", 4),
          ("path3-off", 5),
          ("path3-on", 6))
    )


_GlobalReverseRFLinkSwitchControl_Type.__name__ = "Integer32"
_GlobalReverseRFLinkSwitchControl_Object = MibScalar
globalReverseRFLinkSwitchControl = _GlobalReverseRFLinkSwitchControl_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 14, 1, 14),
    _GlobalReverseRFLinkSwitchControl_Type()
)
globalReverseRFLinkSwitchControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    globalReverseRFLinkSwitchControl.setStatus("current")
_GlobalFnRFPortTable_Object = MibTable
globalFnRFPortTable = _GlobalFnRFPortTable_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 14, 1, 15)
)
if mibBuilder.loadTexts:
    globalFnRFPortTable.setStatus("current")
_GlobalFnRFPortTableEntry_Object = MibTableRow
globalFnRFPortTableEntry = _GlobalFnRFPortTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 14, 1, 15, 1)
)
globalFnRFPortTableEntry.setIndexNames(
    (0, "ELECTROLINE-DHT-GLOBAL-FIBERNODE-MIB", "globalFnRFPortIndex"),
)
if mibBuilder.loadTexts:
    globalFnRFPortTableEntry.setStatus("current")
_GlobalFnRFPortIndex_Type = Integer32
_GlobalFnRFPortIndex_Object = MibTableColumn
globalFnRFPortIndex = _GlobalFnRFPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 14, 1, 15, 1, 1),
    _GlobalFnRFPortIndex_Type()
)
globalFnRFPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalFnRFPortIndex.setStatus("current")
_GlobalUpStreamRFLevel_Type = Integer32
_GlobalUpStreamRFLevel_Object = MibTableColumn
globalUpStreamRFLevel = _GlobalUpStreamRFLevel_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 14, 1, 15, 1, 2),
    _GlobalUpStreamRFLevel_Type()
)
globalUpStreamRFLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalUpStreamRFLevel.setStatus("current")
_GlobalFnDownStreamRFLevel_Type = Integer32
_GlobalFnDownStreamRFLevel_Object = MibTableColumn
globalFnDownStreamRFLevel = _GlobalFnDownStreamRFLevel_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 14, 1, 15, 1, 3),
    _GlobalFnDownStreamRFLevel_Type()
)
globalFnDownStreamRFLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalFnDownStreamRFLevel.setStatus("current")


class _GlobalFnNumberElecAttenuator_Type(Integer32):
    """Custom type globalFnNumberElecAttenuator based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_GlobalFnNumberElecAttenuator_Type.__name__ = "Integer32"
_GlobalFnNumberElecAttenuator_Object = MibScalar
globalFnNumberElecAttenuator = _GlobalFnNumberElecAttenuator_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 14, 1, 16),
    _GlobalFnNumberElecAttenuator_Type()
)
globalFnNumberElecAttenuator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalFnNumberElecAttenuator.setStatus("current")
_GlobalFnElecAttenuatorTable_Object = MibTable
globalFnElecAttenuatorTable = _GlobalFnElecAttenuatorTable_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 14, 1, 17)
)
if mibBuilder.loadTexts:
    globalFnElecAttenuatorTable.setStatus("current")
_GlobalFnElecAttenuatorTableEntry_Object = MibTableRow
globalFnElecAttenuatorTableEntry = _GlobalFnElecAttenuatorTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 14, 1, 17, 1)
)
globalFnElecAttenuatorTableEntry.setIndexNames(
    (0, "ELECTROLINE-DHT-GLOBAL-FIBERNODE-MIB", "globalFnElecAttenuatorIndex"),
)
if mibBuilder.loadTexts:
    globalFnElecAttenuatorTableEntry.setStatus("current")
_GlobalFnElecAttenuatorIndex_Type = Integer32
_GlobalFnElecAttenuatorIndex_Object = MibTableColumn
globalFnElecAttenuatorIndex = _GlobalFnElecAttenuatorIndex_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 14, 1, 17, 1, 1),
    _GlobalFnElecAttenuatorIndex_Type()
)
globalFnElecAttenuatorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalFnElecAttenuatorIndex.setStatus("current")
_GlobalFnElecAttenuatorValue_Type = Integer32
_GlobalFnElecAttenuatorValue_Object = MibTableColumn
globalFnElecAttenuatorValue = _GlobalFnElecAttenuatorValue_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 14, 1, 17, 1, 2),
    _GlobalFnElecAttenuatorValue_Type()
)
globalFnElecAttenuatorValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    globalFnElecAttenuatorValue.setStatus("current")


class _GlobalFnNumberElecEqualizer_Type(Integer32):
    """Custom type globalFnNumberElecEqualizer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_GlobalFnNumberElecEqualizer_Type.__name__ = "Integer32"
_GlobalFnNumberElecEqualizer_Object = MibScalar
globalFnNumberElecEqualizer = _GlobalFnNumberElecEqualizer_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 14, 1, 18),
    _GlobalFnNumberElecEqualizer_Type()
)
globalFnNumberElecEqualizer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalFnNumberElecEqualizer.setStatus("current")
_GlobalFnElecEqualizerTable_Object = MibTable
globalFnElecEqualizerTable = _GlobalFnElecEqualizerTable_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 14, 1, 19)
)
if mibBuilder.loadTexts:
    globalFnElecEqualizerTable.setStatus("current")
_GlobalFnElecEqualizerTableEntry_Object = MibTableRow
globalFnElecEqualizerTableEntry = _GlobalFnElecEqualizerTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 14, 1, 19, 1)
)
globalFnElecEqualizerTableEntry.setIndexNames(
    (0, "ELECTROLINE-DHT-GLOBAL-FIBERNODE-MIB", "globalFnElecEqualizerIndex"),
)
if mibBuilder.loadTexts:
    globalFnElecEqualizerTableEntry.setStatus("current")
_GlobalFnElecEqualizerIndex_Type = Integer32
_GlobalFnElecEqualizerIndex_Object = MibTableColumn
globalFnElecEqualizerIndex = _GlobalFnElecEqualizerIndex_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 14, 1, 19, 1, 1),
    _GlobalFnElecEqualizerIndex_Type()
)
globalFnElecEqualizerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalFnElecEqualizerIndex.setStatus("current")
_GlobalFnElecEqualizerValue_Type = Integer32
_GlobalFnElecEqualizerValue_Object = MibTableColumn
globalFnElecEqualizerValue = _GlobalFnElecEqualizerValue_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 14, 1, 19, 1, 2),
    _GlobalFnElecEqualizerValue_Type()
)
globalFnElecEqualizerValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    globalFnElecEqualizerValue.setStatus("current")
_GlobalFnAGCOffsetValue_Type = Integer32
_GlobalFnAGCOffsetValue_Object = MibScalar
globalFnAGCOffsetValue = _GlobalFnAGCOffsetValue_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 14, 1, 20),
    _GlobalFnAGCOffsetValue_Type()
)
globalFnAGCOffsetValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    globalFnAGCOffsetValue.setStatus("current")
_GlobalFnAGCRfLevel_Type = Integer32
_GlobalFnAGCRfLevel_Object = MibScalar
globalFnAGCRfLevel = _GlobalFnAGCRfLevel_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 14, 1, 21),
    _GlobalFnAGCRfLevel_Type()
)
globalFnAGCRfLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    globalFnAGCRfLevel.setStatus("current")
_GlobalFnRfLevelOffsetValue_Type = Integer32
_GlobalFnRfLevelOffsetValue_Object = MibScalar
globalFnRfLevelOffsetValue = _GlobalFnRfLevelOffsetValue_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 14, 1, 22),
    _GlobalFnRfLevelOffsetValue_Type()
)
globalFnRfLevelOffsetValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    globalFnRfLevelOffsetValue.setStatus("current")
_GlobalFnTemperature_Type = Integer32
_GlobalFnTemperature_Object = MibScalar
globalFnTemperature = _GlobalFnTemperature_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 14, 1, 23),
    _GlobalFnTemperature_Type()
)
globalFnTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalFnTemperature.setStatus("current")


class _GlobalFnReset_Type(Integer32):
    """Custom type globalFnReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset", 1)
    )


_GlobalFnReset_Type.__name__ = "Integer32"
_GlobalFnReset_Object = MibScalar
globalFnReset = _GlobalFnReset_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 14, 1, 24),
    _GlobalFnReset_Type()
)
globalFnReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    globalFnReset.setStatus("current")


class _GlobalFnResetFrxRtx_Type(Integer32):
    """Custom type globalFnResetFrxRtx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset", 1)
    )


_GlobalFnResetFrxRtx_Type.__name__ = "Integer32"
_GlobalFnResetFrxRtx_Object = MibScalar
globalFnResetFrxRtx = _GlobalFnResetFrxRtx_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 14, 1, 25),
    _GlobalFnResetFrxRtx_Type()
)
globalFnResetFrxRtx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    globalFnResetFrxRtx.setStatus("current")


class _GlobalFnTypeOfPowerSupply_Type(Integer32):
    """Custom type globalFnTypeOfPowerSupply based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("not-defined", 0),
          ("linePower", 1),
          ("mainPower", 2))
    )


_GlobalFnTypeOfPowerSupply_Type.__name__ = "Integer32"
_GlobalFnTypeOfPowerSupply_Object = MibScalar
globalFnTypeOfPowerSupply = _GlobalFnTypeOfPowerSupply_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 14, 1, 26),
    _GlobalFnTypeOfPowerSupply_Type()
)
globalFnTypeOfPowerSupply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalFnTypeOfPowerSupply.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ELECTROLINE-DHT-GLOBAL-FIBERNODE-MIB",
    **{"dhtGlobalFnIdentMIB": dhtGlobalFnIdentMIB,
       "globalFnIdentObjects": globalFnIdentObjects,
       "globalFnNumberReturnLaser": globalFnNumberReturnLaser,
       "globalFnReturnLaserTable": globalFnReturnLaserTable,
       "globalFnReturnLaserTableEntry": globalFnReturnLaserTableEntry,
       "globalFnReturnLaserIndex": globalFnReturnLaserIndex,
       "globalFnReturnLaserState": globalFnReturnLaserState,
       "globalFnReturnLaserRFLevel": globalFnReturnLaserRFLevel,
       "globalFnReturnLaserRFControl": globalFnReturnLaserRFControl,
       "globalFnReturnLaserElecAttenuator": globalFnReturnLaserElecAttenuator,
       "globalFnNumberOpticalReceiver": globalFnNumberOpticalReceiver,
       "globalFnOpticalReceiverAGCState": globalFnOpticalReceiverAGCState,
       "globalFnOpticalReceiverAGCControl": globalFnOpticalReceiverAGCControl,
       "globalFnOpticalReceiverTable": globalFnOpticalReceiverTable,
       "globalFnOpticalReceiverTableEntry": globalFnOpticalReceiverTableEntry,
       "globalFnOpticalReceiverIndex": globalFnOpticalReceiverIndex,
       "globalFnOpticalReceiverState": globalFnOpticalReceiverState,
       "globalFnOpticalReceiverType": globalFnOpticalReceiverType,
       "globalFnOpticalReceiverRFLevel": globalFnOpticalReceiverRFLevel,
       "globalFnOpticalReceiverRFControl": globalFnOpticalReceiverRFControl,
       "globalFnOpticalReceiverElecAttenuator": globalFnOpticalReceiverElecAttenuator,
       "globalFnNumberWingSwitch": globalFnNumberWingSwitch,
       "globalFnWingSwitchTable": globalFnWingSwitchTable,
       "globalFnWingSwitchTableEntry": globalFnWingSwitchTableEntry,
       "globalFnWingSwitchIndex": globalFnWingSwitchIndex,
       "globalFnWingSwitchState": globalFnWingSwitchState,
       "globalFnWingSwitchControl": globalFnWingSwitchControl,
       "globalFnNumberRFRouter": globalFnNumberRFRouter,
       "globalFnRFRouterTable": globalFnRFRouterTable,
       "globalRFRouterTableEntry": globalRFRouterTableEntry,
       "globalFnRFRouterIndex": globalFnRFRouterIndex,
       "globalFnRFRouterType": globalFnRFRouterType,
       "globalFnRFRouterDownstreamSwitchState": globalFnRFRouterDownstreamSwitchState,
       "globalFnRFRouterDownstreamSwitchControl": globalFnRFRouterDownstreamSwitchControl,
       "globalFnRFRouterDownstreamControlTypeState": globalFnRFRouterDownstreamControlTypeState,
       "globalFnRFRouterDownstreamControlTypeSetting": globalFnRFRouterDownstreamControlTypeSetting,
       "globalFnRFRouterUptreamSwitchState": globalFnRFRouterUptreamSwitchState,
       "globalFnRFRouterUptreamSwitchControl": globalFnRFRouterUptreamSwitchControl,
       "globalFnRFRouterUpstreamControlTypeState": globalFnRFRouterUpstreamControlTypeState,
       "globalFnRFRouterUpstreamControlTypeSetting": globalFnRFRouterUpstreamControlTypeSetting,
       "globalFnNumberRFPort": globalFnNumberRFPort,
       "globalRFLinkSwitchState": globalRFLinkSwitchState,
       "globalReverseRFLinkSwitchState": globalReverseRFLinkSwitchState,
       "globalReverseRFLinkSwitchControl": globalReverseRFLinkSwitchControl,
       "globalFnRFPortTable": globalFnRFPortTable,
       "globalFnRFPortTableEntry": globalFnRFPortTableEntry,
       "globalFnRFPortIndex": globalFnRFPortIndex,
       "globalUpStreamRFLevel": globalUpStreamRFLevel,
       "globalFnDownStreamRFLevel": globalFnDownStreamRFLevel,
       "globalFnNumberElecAttenuator": globalFnNumberElecAttenuator,
       "globalFnElecAttenuatorTable": globalFnElecAttenuatorTable,
       "globalFnElecAttenuatorTableEntry": globalFnElecAttenuatorTableEntry,
       "globalFnElecAttenuatorIndex": globalFnElecAttenuatorIndex,
       "globalFnElecAttenuatorValue": globalFnElecAttenuatorValue,
       "globalFnNumberElecEqualizer": globalFnNumberElecEqualizer,
       "globalFnElecEqualizerTable": globalFnElecEqualizerTable,
       "globalFnElecEqualizerTableEntry": globalFnElecEqualizerTableEntry,
       "globalFnElecEqualizerIndex": globalFnElecEqualizerIndex,
       "globalFnElecEqualizerValue": globalFnElecEqualizerValue,
       "globalFnAGCOffsetValue": globalFnAGCOffsetValue,
       "globalFnAGCRfLevel": globalFnAGCRfLevel,
       "globalFnRfLevelOffsetValue": globalFnRfLevelOffsetValue,
       "globalFnTemperature": globalFnTemperature,
       "globalFnReset": globalFnReset,
       "globalFnResetFrxRtx": globalFnResetFrxRtx,
       "globalFnTypeOfPowerSupply": globalFnTypeOfPowerSupply}
)
