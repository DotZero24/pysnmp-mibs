# SNMP MIB module (GUDEADS-PDU835X-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/gude/GUDEADS-PDU835X-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:07:04 2025
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

gudeads = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 28507)
)
if mibBuilder.loadTexts:
    gudeads.setRevisions(
        ("2007-03-05 13:56",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_GadsPDU835X_ObjectIdentity = ObjectIdentity
gadsPDU835X = _GadsPDU835X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 52)
)
_Events_ObjectIdentity = ObjectIdentity
events = _Events_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 52, 0)
)
_Pdu835XObjects_ObjectIdentity = ObjectIdentity
pdu835XObjects = _Pdu835XObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 52, 1)
)
_Pdu835XCommonConfig_ObjectIdentity = ObjectIdentity
pdu835XCommonConfig = _Pdu835XCommonConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 52, 1, 1)
)
_Pdu835XSNMPaccess_ObjectIdentity = ObjectIdentity
pdu835XSNMPaccess = _Pdu835XSNMPaccess_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 52, 1, 1, 1)
)


class _Pdu835XTrapCtrl_Type(Integer32):
    """Custom type pdu835XTrapCtrl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_Pdu835XTrapCtrl_Type.__name__ = "Integer32"
_Pdu835XTrapCtrl_Object = MibScalar
pdu835XTrapCtrl = _Pdu835XTrapCtrl_Object(
    (1, 3, 6, 1, 4, 1, 28507, 52, 1, 1, 1, 1),
    _Pdu835XTrapCtrl_Type()
)
pdu835XTrapCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdu835XTrapCtrl.setStatus("current")
_Pdu835XTrapIPTable_Object = MibTable
pdu835XTrapIPTable = _Pdu835XTrapIPTable_Object(
    (1, 3, 6, 1, 4, 1, 28507, 52, 1, 1, 1, 2)
)
if mibBuilder.loadTexts:
    pdu835XTrapIPTable.setStatus("current")
_Pdu835XTrapIPEntry_Object = MibTableRow
pdu835XTrapIPEntry = _Pdu835XTrapIPEntry_Object(
    (1, 3, 6, 1, 4, 1, 28507, 52, 1, 1, 1, 2, 1)
)
pdu835XTrapIPEntry.setIndexNames(
    (0, "GUDEADS-PDU835X-MIB", "pdu835XTrapIPIndex"),
)
if mibBuilder.loadTexts:
    pdu835XTrapIPEntry.setStatus("current")


class _Pdu835XTrapIPIndex_Type(Integer32):
    """Custom type pdu835XTrapIPIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_Pdu835XTrapIPIndex_Type.__name__ = "Integer32"
_Pdu835XTrapIPIndex_Object = MibTableColumn
pdu835XTrapIPIndex = _Pdu835XTrapIPIndex_Object(
    (1, 3, 6, 1, 4, 1, 28507, 52, 1, 1, 1, 2, 1, 1),
    _Pdu835XTrapIPIndex_Type()
)
pdu835XTrapIPIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pdu835XTrapIPIndex.setStatus("current")


class _Pdu835XTrapAddr_Type(OctetString):
    """Custom type pdu835XTrapAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 99),
    )


_Pdu835XTrapAddr_Type.__name__ = "OctetString"
_Pdu835XTrapAddr_Object = MibTableColumn
pdu835XTrapAddr = _Pdu835XTrapAddr_Object(
    (1, 3, 6, 1, 4, 1, 28507, 52, 1, 1, 1, 2, 1, 2),
    _Pdu835XTrapAddr_Type()
)
pdu835XTrapAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdu835XTrapAddr.setStatus("current")
_Pdu835XDeviceConfig_ObjectIdentity = ObjectIdentity
pdu835XDeviceConfig = _Pdu835XDeviceConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 52, 1, 2)
)
_Pdu835XIntActors_ObjectIdentity = ObjectIdentity
pdu835XIntActors = _Pdu835XIntActors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 52, 1, 3)
)


class _Pdu835XBuzzer_Type(Integer32):
    """Custom type pdu835XBuzzer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Pdu835XBuzzer_Type.__name__ = "Integer32"
_Pdu835XBuzzer_Object = MibScalar
pdu835XBuzzer = _Pdu835XBuzzer_Object(
    (1, 3, 6, 1, 4, 1, 28507, 52, 1, 3, 10),
    _Pdu835XBuzzer_Type()
)
pdu835XBuzzer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdu835XBuzzer.setStatus("current")
if mibBuilder.loadTexts:
    pdu835XBuzzer.setUnits("0 = Off, 1 = On")
_Pdu835XExtActors_ObjectIdentity = ObjectIdentity
pdu835XExtActors = _Pdu835XExtActors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 52, 1, 4)
)
_Pdu835XIntSensors_ObjectIdentity = ObjectIdentity
pdu835XIntSensors = _Pdu835XIntSensors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 52, 1, 5)
)
_Pdu835XPowerChan_ObjectIdentity = ObjectIdentity
pdu835XPowerChan = _Pdu835XPowerChan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 52, 1, 5, 1)
)


class _Pdu835XActivePowerChan_Type(Unsigned32):
    """Custom type pdu835XActivePowerChan based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_Pdu835XActivePowerChan_Type.__name__ = "Unsigned32"
_Pdu835XActivePowerChan_Object = MibScalar
pdu835XActivePowerChan = _Pdu835XActivePowerChan_Object(
    (1, 3, 6, 1, 4, 1, 28507, 52, 1, 5, 1, 1),
    _Pdu835XActivePowerChan_Type()
)
pdu835XActivePowerChan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu835XActivePowerChan.setStatus("current")
_Pdu835XPowerTable_Object = MibTable
pdu835XPowerTable = _Pdu835XPowerTable_Object(
    (1, 3, 6, 1, 4, 1, 28507, 52, 1, 5, 1, 2)
)
if mibBuilder.loadTexts:
    pdu835XPowerTable.setStatus("current")
_Pdu835XPowerEntry_Object = MibTableRow
pdu835XPowerEntry = _Pdu835XPowerEntry_Object(
    (1, 3, 6, 1, 4, 1, 28507, 52, 1, 5, 1, 2, 1)
)
pdu835XPowerEntry.setIndexNames(
    (0, "GUDEADS-PDU835X-MIB", "pdu835XPowerIndex"),
)
if mibBuilder.loadTexts:
    pdu835XPowerEntry.setStatus("current")


class _Pdu835XPowerIndex_Type(Integer32):
    """Custom type pdu835XPowerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_Pdu835XPowerIndex_Type.__name__ = "Integer32"
_Pdu835XPowerIndex_Object = MibTableColumn
pdu835XPowerIndex = _Pdu835XPowerIndex_Object(
    (1, 3, 6, 1, 4, 1, 28507, 52, 1, 5, 1, 2, 1, 1),
    _Pdu835XPowerIndex_Type()
)
pdu835XPowerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pdu835XPowerIndex.setStatus("current")


class _Pdu835XChanStatus_Type(Integer32):
    """Custom type pdu835XChanStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Pdu835XChanStatus_Type.__name__ = "Integer32"
_Pdu835XChanStatus_Object = MibTableColumn
pdu835XChanStatus = _Pdu835XChanStatus_Object(
    (1, 3, 6, 1, 4, 1, 28507, 52, 1, 5, 1, 2, 1, 2),
    _Pdu835XChanStatus_Type()
)
pdu835XChanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu835XChanStatus.setStatus("current")
_Pdu835XAbsEnergyActive_Type = Unsigned32
_Pdu835XAbsEnergyActive_Object = MibTableColumn
pdu835XAbsEnergyActive = _Pdu835XAbsEnergyActive_Object(
    (1, 3, 6, 1, 4, 1, 28507, 52, 1, 5, 1, 2, 1, 3),
    _Pdu835XAbsEnergyActive_Type()
)
pdu835XAbsEnergyActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu835XAbsEnergyActive.setStatus("current")
if mibBuilder.loadTexts:
    pdu835XAbsEnergyActive.setUnits("Wh")
_Pdu835XPowerActive_Type = Integer32
_Pdu835XPowerActive_Object = MibTableColumn
pdu835XPowerActive = _Pdu835XPowerActive_Object(
    (1, 3, 6, 1, 4, 1, 28507, 52, 1, 5, 1, 2, 1, 4),
    _Pdu835XPowerActive_Type()
)
pdu835XPowerActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu835XPowerActive.setStatus("current")
if mibBuilder.loadTexts:
    pdu835XPowerActive.setUnits("W")
_Pdu835XCurrent_Type = Unsigned32
_Pdu835XCurrent_Object = MibTableColumn
pdu835XCurrent = _Pdu835XCurrent_Object(
    (1, 3, 6, 1, 4, 1, 28507, 52, 1, 5, 1, 2, 1, 5),
    _Pdu835XCurrent_Type()
)
pdu835XCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu835XCurrent.setStatus("current")
if mibBuilder.loadTexts:
    pdu835XCurrent.setUnits("mA")
_Pdu835XVoltage_Type = Unsigned32
_Pdu835XVoltage_Object = MibTableColumn
pdu835XVoltage = _Pdu835XVoltage_Object(
    (1, 3, 6, 1, 4, 1, 28507, 52, 1, 5, 1, 2, 1, 6),
    _Pdu835XVoltage_Type()
)
pdu835XVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu835XVoltage.setStatus("current")
if mibBuilder.loadTexts:
    pdu835XVoltage.setUnits("V")
_Pdu835XFrequency_Type = Unsigned32
_Pdu835XFrequency_Object = MibTableColumn
pdu835XFrequency = _Pdu835XFrequency_Object(
    (1, 3, 6, 1, 4, 1, 28507, 52, 1, 5, 1, 2, 1, 7),
    _Pdu835XFrequency_Type()
)
pdu835XFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu835XFrequency.setStatus("current")
if mibBuilder.loadTexts:
    pdu835XFrequency.setUnits("0.01 hz")
_Pdu835XPowerFactor_Type = Integer32
_Pdu835XPowerFactor_Object = MibTableColumn
pdu835XPowerFactor = _Pdu835XPowerFactor_Object(
    (1, 3, 6, 1, 4, 1, 28507, 52, 1, 5, 1, 2, 1, 8),
    _Pdu835XPowerFactor_Type()
)
pdu835XPowerFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu835XPowerFactor.setStatus("current")
if mibBuilder.loadTexts:
    pdu835XPowerFactor.setUnits("0.001")
_Pdu835XPangle_Type = Integer32
_Pdu835XPangle_Object = MibTableColumn
pdu835XPangle = _Pdu835XPangle_Object(
    (1, 3, 6, 1, 4, 1, 28507, 52, 1, 5, 1, 2, 1, 9),
    _Pdu835XPangle_Type()
)
pdu835XPangle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu835XPangle.setStatus("current")
if mibBuilder.loadTexts:
    pdu835XPangle.setUnits("0.1 degree")
_Pdu835XPowerApparent_Type = Integer32
_Pdu835XPowerApparent_Object = MibTableColumn
pdu835XPowerApparent = _Pdu835XPowerApparent_Object(
    (1, 3, 6, 1, 4, 1, 28507, 52, 1, 5, 1, 2, 1, 10),
    _Pdu835XPowerApparent_Type()
)
pdu835XPowerApparent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu835XPowerApparent.setStatus("current")
if mibBuilder.loadTexts:
    pdu835XPowerApparent.setUnits("VA")
_Pdu835XPowerReactive_Type = Integer32
_Pdu835XPowerReactive_Object = MibTableColumn
pdu835XPowerReactive = _Pdu835XPowerReactive_Object(
    (1, 3, 6, 1, 4, 1, 28507, 52, 1, 5, 1, 2, 1, 11),
    _Pdu835XPowerReactive_Type()
)
pdu835XPowerReactive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu835XPowerReactive.setStatus("current")
if mibBuilder.loadTexts:
    pdu835XPowerReactive.setUnits("VAR")
_Pdu835XAbsEnergyReactive_Type = Unsigned32
_Pdu835XAbsEnergyReactive_Object = MibTableColumn
pdu835XAbsEnergyReactive = _Pdu835XAbsEnergyReactive_Object(
    (1, 3, 6, 1, 4, 1, 28507, 52, 1, 5, 1, 2, 1, 12),
    _Pdu835XAbsEnergyReactive_Type()
)
pdu835XAbsEnergyReactive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu835XAbsEnergyReactive.setStatus("current")
if mibBuilder.loadTexts:
    pdu835XAbsEnergyReactive.setUnits("VARh")
_Pdu835XAbsEnergyActiveResettable_Type = Unsigned32
_Pdu835XAbsEnergyActiveResettable_Object = MibTableColumn
pdu835XAbsEnergyActiveResettable = _Pdu835XAbsEnergyActiveResettable_Object(
    (1, 3, 6, 1, 4, 1, 28507, 52, 1, 5, 1, 2, 1, 13),
    _Pdu835XAbsEnergyActiveResettable_Type()
)
pdu835XAbsEnergyActiveResettable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu835XAbsEnergyActiveResettable.setStatus("current")
if mibBuilder.loadTexts:
    pdu835XAbsEnergyActiveResettable.setUnits("Wh")
_Pdu835XAbsEnergyReactiveResettable_Type = Unsigned32
_Pdu835XAbsEnergyReactiveResettable_Object = MibTableColumn
pdu835XAbsEnergyReactiveResettable = _Pdu835XAbsEnergyReactiveResettable_Object(
    (1, 3, 6, 1, 4, 1, 28507, 52, 1, 5, 1, 2, 1, 14),
    _Pdu835XAbsEnergyReactiveResettable_Type()
)
pdu835XAbsEnergyReactiveResettable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu835XAbsEnergyReactiveResettable.setStatus("current")
if mibBuilder.loadTexts:
    pdu835XAbsEnergyReactiveResettable.setUnits("VARh")
_Pdu835XResetTime_Type = Unsigned32
_Pdu835XResetTime_Object = MibTableColumn
pdu835XResetTime = _Pdu835XResetTime_Object(
    (1, 3, 6, 1, 4, 1, 28507, 52, 1, 5, 1, 2, 1, 15),
    _Pdu835XResetTime_Type()
)
pdu835XResetTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu835XResetTime.setStatus("current")
if mibBuilder.loadTexts:
    pdu835XResetTime.setUnits("s")
_Pdu835XForwEnergyActive_Type = Unsigned32
_Pdu835XForwEnergyActive_Object = MibTableColumn
pdu835XForwEnergyActive = _Pdu835XForwEnergyActive_Object(
    (1, 3, 6, 1, 4, 1, 28507, 52, 1, 5, 1, 2, 1, 16),
    _Pdu835XForwEnergyActive_Type()
)
pdu835XForwEnergyActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu835XForwEnergyActive.setStatus("current")
if mibBuilder.loadTexts:
    pdu835XForwEnergyActive.setUnits("Wh")
_Pdu835XForwEnergyReactive_Type = Unsigned32
_Pdu835XForwEnergyReactive_Object = MibTableColumn
pdu835XForwEnergyReactive = _Pdu835XForwEnergyReactive_Object(
    (1, 3, 6, 1, 4, 1, 28507, 52, 1, 5, 1, 2, 1, 17),
    _Pdu835XForwEnergyReactive_Type()
)
pdu835XForwEnergyReactive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu835XForwEnergyReactive.setStatus("current")
if mibBuilder.loadTexts:
    pdu835XForwEnergyReactive.setUnits("VARh")
_Pdu835XForwEnergyActiveResettable_Type = Unsigned32
_Pdu835XForwEnergyActiveResettable_Object = MibTableColumn
pdu835XForwEnergyActiveResettable = _Pdu835XForwEnergyActiveResettable_Object(
    (1, 3, 6, 1, 4, 1, 28507, 52, 1, 5, 1, 2, 1, 18),
    _Pdu835XForwEnergyActiveResettable_Type()
)
pdu835XForwEnergyActiveResettable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu835XForwEnergyActiveResettable.setStatus("current")
if mibBuilder.loadTexts:
    pdu835XForwEnergyActiveResettable.setUnits("Wh")
_Pdu835XForwEnergyReactiveResettable_Type = Unsigned32
_Pdu835XForwEnergyReactiveResettable_Object = MibTableColumn
pdu835XForwEnergyReactiveResettable = _Pdu835XForwEnergyReactiveResettable_Object(
    (1, 3, 6, 1, 4, 1, 28507, 52, 1, 5, 1, 2, 1, 19),
    _Pdu835XForwEnergyReactiveResettable_Type()
)
pdu835XForwEnergyReactiveResettable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu835XForwEnergyReactiveResettable.setStatus("current")
if mibBuilder.loadTexts:
    pdu835XForwEnergyReactiveResettable.setUnits("VARh")
_Pdu835XRevEnergyActive_Type = Unsigned32
_Pdu835XRevEnergyActive_Object = MibTableColumn
pdu835XRevEnergyActive = _Pdu835XRevEnergyActive_Object(
    (1, 3, 6, 1, 4, 1, 28507, 52, 1, 5, 1, 2, 1, 20),
    _Pdu835XRevEnergyActive_Type()
)
pdu835XRevEnergyActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu835XRevEnergyActive.setStatus("current")
if mibBuilder.loadTexts:
    pdu835XRevEnergyActive.setUnits("Wh")
_Pdu835XRevEnergyReactive_Type = Unsigned32
_Pdu835XRevEnergyReactive_Object = MibTableColumn
pdu835XRevEnergyReactive = _Pdu835XRevEnergyReactive_Object(
    (1, 3, 6, 1, 4, 1, 28507, 52, 1, 5, 1, 2, 1, 21),
    _Pdu835XRevEnergyReactive_Type()
)
pdu835XRevEnergyReactive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu835XRevEnergyReactive.setStatus("current")
if mibBuilder.loadTexts:
    pdu835XRevEnergyReactive.setUnits("VARh")
_Pdu835XRevEnergyActiveResettable_Type = Unsigned32
_Pdu835XRevEnergyActiveResettable_Object = MibTableColumn
pdu835XRevEnergyActiveResettable = _Pdu835XRevEnergyActiveResettable_Object(
    (1, 3, 6, 1, 4, 1, 28507, 52, 1, 5, 1, 2, 1, 22),
    _Pdu835XRevEnergyActiveResettable_Type()
)
pdu835XRevEnergyActiveResettable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu835XRevEnergyActiveResettable.setStatus("current")
if mibBuilder.loadTexts:
    pdu835XRevEnergyActiveResettable.setUnits("Wh")
_Pdu835XRevEnergyReactiveResettable_Type = Unsigned32
_Pdu835XRevEnergyReactiveResettable_Object = MibTableColumn
pdu835XRevEnergyReactiveResettable = _Pdu835XRevEnergyReactiveResettable_Object(
    (1, 3, 6, 1, 4, 1, 28507, 52, 1, 5, 1, 2, 1, 23),
    _Pdu835XRevEnergyReactiveResettable_Type()
)
pdu835XRevEnergyReactiveResettable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu835XRevEnergyReactiveResettable.setStatus("current")
if mibBuilder.loadTexts:
    pdu835XRevEnergyReactiveResettable.setUnits("VARh")
_Pdu835XPowerGroup_ObjectIdentity = ObjectIdentity
pdu835XPowerGroup = _Pdu835XPowerGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 52, 1, 5, 3)
)


class _Pdu835XActivePowerGroups_Type(Unsigned32):
    """Custom type pdu835XActivePowerGroups based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_Pdu835XActivePowerGroups_Type.__name__ = "Unsigned32"
_Pdu835XActivePowerGroups_Object = MibScalar
pdu835XActivePowerGroups = _Pdu835XActivePowerGroups_Object(
    (1, 3, 6, 1, 4, 1, 28507, 52, 1, 5, 3, 1),
    _Pdu835XActivePowerGroups_Type()
)
pdu835XActivePowerGroups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu835XActivePowerGroups.setStatus("current")
_Pdu835XPowerGroupTable_Object = MibTable
pdu835XPowerGroupTable = _Pdu835XPowerGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 28507, 52, 1, 5, 3, 2)
)
if mibBuilder.loadTexts:
    pdu835XPowerGroupTable.setStatus("current")
_Pdu835XEntry_Object = MibTableRow
pdu835XEntry = _Pdu835XEntry_Object(
    (1, 3, 6, 1, 4, 1, 28507, 52, 1, 5, 3, 2, 1)
)
pdu835XEntry.setIndexNames(
    (0, "GUDEADS-PDU835X-MIB", "pdu835XPowerGroupIndex"),
)
if mibBuilder.loadTexts:
    pdu835XEntry.setStatus("current")


class _Pdu835XPowerGroupIndex_Type(Integer32):
    """Custom type pdu835XPowerGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Pdu835XPowerGroupIndex_Type.__name__ = "Integer32"
_Pdu835XPowerGroupIndex_Object = MibTableColumn
pdu835XPowerGroupIndex = _Pdu835XPowerGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 28507, 52, 1, 5, 3, 2, 1, 1),
    _Pdu835XPowerGroupIndex_Type()
)
pdu835XPowerGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pdu835XPowerGroupIndex.setStatus("current")
_Pdu835XRCurrent3P_Type = Unsigned32
_Pdu835XRCurrent3P_Object = MibTableColumn
pdu835XRCurrent3P = _Pdu835XRCurrent3P_Object(
    (1, 3, 6, 1, 4, 1, 28507, 52, 1, 5, 3, 2, 1, 2),
    _Pdu835XRCurrent3P_Type()
)
pdu835XRCurrent3P.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu835XRCurrent3P.setStatus("current")
if mibBuilder.loadTexts:
    pdu835XRCurrent3P.setUnits("mA")
_Pdu835XNCurrent3P_Type = Unsigned32
_Pdu835XNCurrent3P_Object = MibTableColumn
pdu835XNCurrent3P = _Pdu835XNCurrent3P_Object(
    (1, 3, 6, 1, 4, 1, 28507, 52, 1, 5, 3, 2, 1, 3),
    _Pdu835XNCurrent3P_Type()
)
pdu835XNCurrent3P.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu835XNCurrent3P.setStatus("current")
if mibBuilder.loadTexts:
    pdu835XNCurrent3P.setUnits("mA")


class _Pdu835XMeasurementBoxConnected_Type(Integer32):
    """Custom type pdu835XMeasurementBoxConnected based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disconnected", 0),
          ("connected", 1))
    )


_Pdu835XMeasurementBoxConnected_Type.__name__ = "Integer32"
_Pdu835XMeasurementBoxConnected_Object = MibTableColumn
pdu835XMeasurementBoxConnected = _Pdu835XMeasurementBoxConnected_Object(
    (1, 3, 6, 1, 4, 1, 28507, 52, 1, 5, 3, 2, 1, 4),
    _Pdu835XMeasurementBoxConnected_Type()
)
pdu835XMeasurementBoxConnected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu835XMeasurementBoxConnected.setStatus("current")
_Pdu835XExtSensors_ObjectIdentity = ObjectIdentity
pdu835XExtSensors = _Pdu835XExtSensors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 52, 1, 6)
)
_Pdu835XSensorTable_Object = MibTable
pdu835XSensorTable = _Pdu835XSensorTable_Object(
    (1, 3, 6, 1, 4, 1, 28507, 52, 1, 6, 1)
)
if mibBuilder.loadTexts:
    pdu835XSensorTable.setStatus("current")
_Pdu835XSensorEntry_Object = MibTableRow
pdu835XSensorEntry = _Pdu835XSensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 28507, 52, 1, 6, 1, 1)
)
pdu835XSensorEntry.setIndexNames(
    (0, "GUDEADS-PDU835X-MIB", "pdu835XSensorIndex"),
)
if mibBuilder.loadTexts:
    pdu835XSensorEntry.setStatus("current")


class _Pdu835XSensorIndex_Type(Integer32):
    """Custom type pdu835XSensorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_Pdu835XSensorIndex_Type.__name__ = "Integer32"
_Pdu835XSensorIndex_Object = MibTableColumn
pdu835XSensorIndex = _Pdu835XSensorIndex_Object(
    (1, 3, 6, 1, 4, 1, 28507, 52, 1, 6, 1, 1, 1),
    _Pdu835XSensorIndex_Type()
)
pdu835XSensorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pdu835XSensorIndex.setStatus("current")
_Pdu835XTempSensor_Type = Integer32
_Pdu835XTempSensor_Object = MibTableColumn
pdu835XTempSensor = _Pdu835XTempSensor_Object(
    (1, 3, 6, 1, 4, 1, 28507, 52, 1, 6, 1, 1, 2),
    _Pdu835XTempSensor_Type()
)
pdu835XTempSensor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu835XTempSensor.setStatus("current")
if mibBuilder.loadTexts:
    pdu835XTempSensor.setUnits("0.1 degree Celsius")
_Pdu835XHygroSensor_Type = Integer32
_Pdu835XHygroSensor_Object = MibTableColumn
pdu835XHygroSensor = _Pdu835XHygroSensor_Object(
    (1, 3, 6, 1, 4, 1, 28507, 52, 1, 6, 1, 1, 3),
    _Pdu835XHygroSensor_Type()
)
pdu835XHygroSensor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu835XHygroSensor.setStatus("current")
if mibBuilder.loadTexts:
    pdu835XHygroSensor.setUnits("0.1 percent humidity")


class _Pdu835XInputSensor_Type(Integer32):
    """Custom type pdu835XInputSensor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_Pdu835XInputSensor_Type.__name__ = "Integer32"
_Pdu835XInputSensor_Object = MibTableColumn
pdu835XInputSensor = _Pdu835XInputSensor_Object(
    (1, 3, 6, 1, 4, 1, 28507, 52, 1, 6, 1, 1, 4),
    _Pdu835XInputSensor_Type()
)
pdu835XInputSensor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu835XInputSensor.setStatus("current")
_Pdu835XConf_ObjectIdentity = ObjectIdentity
pdu835XConf = _Pdu835XConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 52, 2)
)
_Pdu835XGroups_ObjectIdentity = ObjectIdentity
pdu835XGroups = _Pdu835XGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 52, 2, 1)
)
_Pdu835XCompls_ObjectIdentity = ObjectIdentity
pdu835XCompls = _Pdu835XCompls_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 52, 2, 2)
)

# Managed Objects groups

pdu835XBasicGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 28507, 52, 2, 1, 1)
)
pdu835XBasicGroup.setObjects(
      *(("GUDEADS-PDU835X-MIB", "pdu835XTrapCtrl"),
        ("GUDEADS-PDU835X-MIB", "pdu835XTrapAddr"),
        ("GUDEADS-PDU835X-MIB", "pdu835XActivePowerChan"),
        ("GUDEADS-PDU835X-MIB", "pdu835XChanStatus"),
        ("GUDEADS-PDU835X-MIB", "pdu835XAbsEnergyActive"),
        ("GUDEADS-PDU835X-MIB", "pdu835XPowerActive"),
        ("GUDEADS-PDU835X-MIB", "pdu835XCurrent"),
        ("GUDEADS-PDU835X-MIB", "pdu835XVoltage"),
        ("GUDEADS-PDU835X-MIB", "pdu835XFrequency"),
        ("GUDEADS-PDU835X-MIB", "pdu835XPowerFactor"),
        ("GUDEADS-PDU835X-MIB", "pdu835XPangle"),
        ("GUDEADS-PDU835X-MIB", "pdu835XPowerApparent"),
        ("GUDEADS-PDU835X-MIB", "pdu835XPowerReactive"),
        ("GUDEADS-PDU835X-MIB", "pdu835XAbsEnergyReactive"),
        ("GUDEADS-PDU835X-MIB", "pdu835XAbsEnergyActiveResettable"),
        ("GUDEADS-PDU835X-MIB", "pdu835XAbsEnergyReactiveResettable"),
        ("GUDEADS-PDU835X-MIB", "pdu835XResetTime"),
        ("GUDEADS-PDU835X-MIB", "pdu835XForwEnergyActive"),
        ("GUDEADS-PDU835X-MIB", "pdu835XForwEnergyReactive"),
        ("GUDEADS-PDU835X-MIB", "pdu835XForwEnergyActiveResettable"),
        ("GUDEADS-PDU835X-MIB", "pdu835XForwEnergyReactiveResettable"),
        ("GUDEADS-PDU835X-MIB", "pdu835XRevEnergyActive"),
        ("GUDEADS-PDU835X-MIB", "pdu835XRevEnergyReactive"),
        ("GUDEADS-PDU835X-MIB", "pdu835XRevEnergyActiveResettable"),
        ("GUDEADS-PDU835X-MIB", "pdu835XRevEnergyReactiveResettable"),
        ("GUDEADS-PDU835X-MIB", "pdu835XTempSensor"),
        ("GUDEADS-PDU835X-MIB", "pdu835XHygroSensor"),
        ("GUDEADS-PDU835X-MIB", "pdu835XInputSensor"),
        ("GUDEADS-PDU835X-MIB", "pdu835XBuzzer"),
        ("GUDEADS-PDU835X-MIB", "pdu835XNCurrent3P"),
        ("GUDEADS-PDU835X-MIB", "pdu835XRCurrent3P"),
        ("GUDEADS-PDU835X-MIB", "pdu835XMeasurementBoxConnected"),
        ("GUDEADS-PDU835X-MIB", "pdu835XActivePowerGroups"))
)
if mibBuilder.loadTexts:
    pdu835XBasicGroup.setStatus("current")


# Notification objects

pdu835XTempEvtSen1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 28507, 52, 0, 1)
)
pdu835XTempEvtSen1.setObjects(
    ("GUDEADS-PDU835X-MIB", "pdu835XTempSensor")
)
if mibBuilder.loadTexts:
    pdu835XTempEvtSen1.setStatus(
        "current"
    )

pdu835XTempEvtSen2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 28507, 52, 0, 2)
)
pdu835XTempEvtSen2.setObjects(
    ("GUDEADS-PDU835X-MIB", "pdu835XTempSensor")
)
if mibBuilder.loadTexts:
    pdu835XTempEvtSen2.setStatus(
        "current"
    )

pdu835XHygroEvtSen1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 28507, 52, 0, 3)
)
pdu835XHygroEvtSen1.setObjects(
    ("GUDEADS-PDU835X-MIB", "pdu835XHygroSensor")
)
if mibBuilder.loadTexts:
    pdu835XHygroEvtSen1.setStatus(
        "current"
    )

pdu835XHygroEvtSen2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 28507, 52, 0, 4)
)
pdu835XHygroEvtSen2.setObjects(
    ("GUDEADS-PDU835X-MIB", "pdu835XHygroSensor")
)
if mibBuilder.loadTexts:
    pdu835XHygroEvtSen2.setStatus(
        "current"
    )

pdu835XInputEvtSen1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 28507, 52, 0, 5)
)
pdu835XInputEvtSen1.setObjects(
    ("GUDEADS-PDU835X-MIB", "pdu835XInputSensor")
)
if mibBuilder.loadTexts:
    pdu835XInputEvtSen1.setStatus(
        "current"
    )

pdu835XInputEvtSen2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 28507, 52, 0, 6)
)
pdu835XInputEvtSen2.setObjects(
    ("GUDEADS-PDU835X-MIB", "pdu835XInputSensor")
)
if mibBuilder.loadTexts:
    pdu835XInputEvtSen2.setStatus(
        "current"
    )

pdu835XMeasurementBoxEvt1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 28507, 52, 0, 7)
)
pdu835XMeasurementBoxEvt1.setObjects(
    ("GUDEADS-PDU835X-MIB", "pdu835XMeasurementBoxConnected")
)
if mibBuilder.loadTexts:
    pdu835XMeasurementBoxEvt1.setStatus(
        "current"
    )

pdu835XMeasurementBoxEvt2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 28507, 52, 0, 8)
)
if mibBuilder.loadTexts:
    pdu835XMeasurementBoxEvt2.setStatus(
        "current"
    )

pdu835XAmperageEvt1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 28507, 52, 0, 9)
)
pdu835XAmperageEvt1.setObjects(
      *(("GUDEADS-PDU835X-MIB", "pdu835XPowerActive"),
        ("GUDEADS-PDU835X-MIB", "pdu835XCurrent"),
        ("GUDEADS-PDU835X-MIB", "pdu835XVoltage"),
        ("GUDEADS-PDU835X-MIB", "pdu835XFrequency"),
        ("GUDEADS-PDU835X-MIB", "pdu835XPowerApparent"),
        ("GUDEADS-PDU835X-MIB", "pdu835XPowerReactive"))
)
if mibBuilder.loadTexts:
    pdu835XAmperageEvt1.setStatus(
        "current"
    )

pdu835XAmperageEvt2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 28507, 52, 0, 10)
)
pdu835XAmperageEvt2.setObjects(
      *(("GUDEADS-PDU835X-MIB", "pdu835XPowerActive"),
        ("GUDEADS-PDU835X-MIB", "pdu835XCurrent"),
        ("GUDEADS-PDU835X-MIB", "pdu835XVoltage"),
        ("GUDEADS-PDU835X-MIB", "pdu835XFrequency"),
        ("GUDEADS-PDU835X-MIB", "pdu835XPowerApparent"),
        ("GUDEADS-PDU835X-MIB", "pdu835XPowerReactive"))
)
if mibBuilder.loadTexts:
    pdu835XAmperageEvt2.setStatus(
        "current"
    )

pdu835XAmperageEvt3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 28507, 52, 0, 11)
)
pdu835XAmperageEvt3.setObjects(
      *(("GUDEADS-PDU835X-MIB", "pdu835XPowerActive"),
        ("GUDEADS-PDU835X-MIB", "pdu835XCurrent"),
        ("GUDEADS-PDU835X-MIB", "pdu835XVoltage"),
        ("GUDEADS-PDU835X-MIB", "pdu835XFrequency"),
        ("GUDEADS-PDU835X-MIB", "pdu835XPowerApparent"),
        ("GUDEADS-PDU835X-MIB", "pdu835XPowerReactive"))
)
if mibBuilder.loadTexts:
    pdu835XAmperageEvt3.setStatus(
        "current"
    )

pdu835XAmperageEvt4 = NotificationType(
    (1, 3, 6, 1, 4, 1, 28507, 52, 0, 12)
)
pdu835XAmperageEvt4.setObjects(
      *(("GUDEADS-PDU835X-MIB", "pdu835XPowerActive"),
        ("GUDEADS-PDU835X-MIB", "pdu835XCurrent"),
        ("GUDEADS-PDU835X-MIB", "pdu835XVoltage"),
        ("GUDEADS-PDU835X-MIB", "pdu835XFrequency"),
        ("GUDEADS-PDU835X-MIB", "pdu835XPowerApparent"),
        ("GUDEADS-PDU835X-MIB", "pdu835XPowerReactive"))
)
if mibBuilder.loadTexts:
    pdu835XAmperageEvt4.setStatus(
        "current"
    )

pdu835XAmperageEvt5 = NotificationType(
    (1, 3, 6, 1, 4, 1, 28507, 52, 0, 13)
)
pdu835XAmperageEvt5.setObjects(
      *(("GUDEADS-PDU835X-MIB", "pdu835XPowerActive"),
        ("GUDEADS-PDU835X-MIB", "pdu835XCurrent"),
        ("GUDEADS-PDU835X-MIB", "pdu835XVoltage"),
        ("GUDEADS-PDU835X-MIB", "pdu835XFrequency"),
        ("GUDEADS-PDU835X-MIB", "pdu835XPowerApparent"),
        ("GUDEADS-PDU835X-MIB", "pdu835XPowerReactive"))
)
if mibBuilder.loadTexts:
    pdu835XAmperageEvt5.setStatus(
        "current"
    )

pdu835XAmperageEvt6 = NotificationType(
    (1, 3, 6, 1, 4, 1, 28507, 52, 0, 14)
)
pdu835XAmperageEvt6.setObjects(
      *(("GUDEADS-PDU835X-MIB", "pdu835XPowerActive"),
        ("GUDEADS-PDU835X-MIB", "pdu835XCurrent"),
        ("GUDEADS-PDU835X-MIB", "pdu835XVoltage"),
        ("GUDEADS-PDU835X-MIB", "pdu835XFrequency"),
        ("GUDEADS-PDU835X-MIB", "pdu835XPowerApparent"),
        ("GUDEADS-PDU835X-MIB", "pdu835XPowerReactive"))
)
if mibBuilder.loadTexts:
    pdu835XAmperageEvt6.setStatus(
        "current"
    )


# Notifications groups

pdu835XNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 28507, 52, 2, 1, 2)
)
pdu835XNotificationGroup.setObjects(
      *(("GUDEADS-PDU835X-MIB", "pdu835XTempEvtSen1"),
        ("GUDEADS-PDU835X-MIB", "pdu835XTempEvtSen2"),
        ("GUDEADS-PDU835X-MIB", "pdu835XHygroEvtSen1"),
        ("GUDEADS-PDU835X-MIB", "pdu835XHygroEvtSen2"),
        ("GUDEADS-PDU835X-MIB", "pdu835XInputEvtSen1"),
        ("GUDEADS-PDU835X-MIB", "pdu835XInputEvtSen2"),
        ("GUDEADS-PDU835X-MIB", "pdu835XAmperageEvt1"),
        ("GUDEADS-PDU835X-MIB", "pdu835XAmperageEvt2"),
        ("GUDEADS-PDU835X-MIB", "pdu835XAmperageEvt3"),
        ("GUDEADS-PDU835X-MIB", "pdu835XAmperageEvt4"),
        ("GUDEADS-PDU835X-MIB", "pdu835XAmperageEvt5"),
        ("GUDEADS-PDU835X-MIB", "pdu835XAmperageEvt6"),
        ("GUDEADS-PDU835X-MIB", "pdu835XMeasurementBoxEvt1"),
        ("GUDEADS-PDU835X-MIB", "pdu835XMeasurementBoxEvt2"))
)
if mibBuilder.loadTexts:
    pdu835XNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "GUDEADS-PDU835X-MIB",
    **{"gudeads": gudeads,
       "gadsPDU835X": gadsPDU835X,
       "events": events,
       "pdu835XTempEvtSen1": pdu835XTempEvtSen1,
       "pdu835XTempEvtSen2": pdu835XTempEvtSen2,
       "pdu835XHygroEvtSen1": pdu835XHygroEvtSen1,
       "pdu835XHygroEvtSen2": pdu835XHygroEvtSen2,
       "pdu835XInputEvtSen1": pdu835XInputEvtSen1,
       "pdu835XInputEvtSen2": pdu835XInputEvtSen2,
       "pdu835XMeasurementBoxEvt1": pdu835XMeasurementBoxEvt1,
       "pdu835XMeasurementBoxEvt2": pdu835XMeasurementBoxEvt2,
       "pdu835XAmperageEvt1": pdu835XAmperageEvt1,
       "pdu835XAmperageEvt2": pdu835XAmperageEvt2,
       "pdu835XAmperageEvt3": pdu835XAmperageEvt3,
       "pdu835XAmperageEvt4": pdu835XAmperageEvt4,
       "pdu835XAmperageEvt5": pdu835XAmperageEvt5,
       "pdu835XAmperageEvt6": pdu835XAmperageEvt6,
       "pdu835XObjects": pdu835XObjects,
       "pdu835XCommonConfig": pdu835XCommonConfig,
       "pdu835XSNMPaccess": pdu835XSNMPaccess,
       "pdu835XTrapCtrl": pdu835XTrapCtrl,
       "pdu835XTrapIPTable": pdu835XTrapIPTable,
       "pdu835XTrapIPEntry": pdu835XTrapIPEntry,
       "pdu835XTrapIPIndex": pdu835XTrapIPIndex,
       "pdu835XTrapAddr": pdu835XTrapAddr,
       "pdu835XDeviceConfig": pdu835XDeviceConfig,
       "pdu835XIntActors": pdu835XIntActors,
       "pdu835XBuzzer": pdu835XBuzzer,
       "pdu835XExtActors": pdu835XExtActors,
       "pdu835XIntSensors": pdu835XIntSensors,
       "pdu835XPowerChan": pdu835XPowerChan,
       "pdu835XActivePowerChan": pdu835XActivePowerChan,
       "pdu835XPowerTable": pdu835XPowerTable,
       "pdu835XPowerEntry": pdu835XPowerEntry,
       "pdu835XPowerIndex": pdu835XPowerIndex,
       "pdu835XChanStatus": pdu835XChanStatus,
       "pdu835XAbsEnergyActive": pdu835XAbsEnergyActive,
       "pdu835XPowerActive": pdu835XPowerActive,
       "pdu835XCurrent": pdu835XCurrent,
       "pdu835XVoltage": pdu835XVoltage,
       "pdu835XFrequency": pdu835XFrequency,
       "pdu835XPowerFactor": pdu835XPowerFactor,
       "pdu835XPangle": pdu835XPangle,
       "pdu835XPowerApparent": pdu835XPowerApparent,
       "pdu835XPowerReactive": pdu835XPowerReactive,
       "pdu835XAbsEnergyReactive": pdu835XAbsEnergyReactive,
       "pdu835XAbsEnergyActiveResettable": pdu835XAbsEnergyActiveResettable,
       "pdu835XAbsEnergyReactiveResettable": pdu835XAbsEnergyReactiveResettable,
       "pdu835XResetTime": pdu835XResetTime,
       "pdu835XForwEnergyActive": pdu835XForwEnergyActive,
       "pdu835XForwEnergyReactive": pdu835XForwEnergyReactive,
       "pdu835XForwEnergyActiveResettable": pdu835XForwEnergyActiveResettable,
       "pdu835XForwEnergyReactiveResettable": pdu835XForwEnergyReactiveResettable,
       "pdu835XRevEnergyActive": pdu835XRevEnergyActive,
       "pdu835XRevEnergyReactive": pdu835XRevEnergyReactive,
       "pdu835XRevEnergyActiveResettable": pdu835XRevEnergyActiveResettable,
       "pdu835XRevEnergyReactiveResettable": pdu835XRevEnergyReactiveResettable,
       "pdu835XPowerGroup": pdu835XPowerGroup,
       "pdu835XActivePowerGroups": pdu835XActivePowerGroups,
       "pdu835XPowerGroupTable": pdu835XPowerGroupTable,
       "pdu835XEntry": pdu835XEntry,
       "pdu835XPowerGroupIndex": pdu835XPowerGroupIndex,
       "pdu835XRCurrent3P": pdu835XRCurrent3P,
       "pdu835XNCurrent3P": pdu835XNCurrent3P,
       "pdu835XMeasurementBoxConnected": pdu835XMeasurementBoxConnected,
       "pdu835XExtSensors": pdu835XExtSensors,
       "pdu835XSensorTable": pdu835XSensorTable,
       "pdu835XSensorEntry": pdu835XSensorEntry,
       "pdu835XSensorIndex": pdu835XSensorIndex,
       "pdu835XTempSensor": pdu835XTempSensor,
       "pdu835XHygroSensor": pdu835XHygroSensor,
       "pdu835XInputSensor": pdu835XInputSensor,
       "pdu835XConf": pdu835XConf,
       "pdu835XGroups": pdu835XGroups,
       "pdu835XBasicGroup": pdu835XBasicGroup,
       "pdu835XNotificationGroup": pdu835XNotificationGroup,
       "pdu835XCompls": pdu835XCompls}
)
