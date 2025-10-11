# SNMP MIB module (GUDEADS-PDU8306-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/gude/GUDEADS-PDU8306-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:07:06 2025
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

_GadsPDU8306_ObjectIdentity = ObjectIdentity
gadsPDU8306 = _GadsPDU8306_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 44)
)
_Events_ObjectIdentity = ObjectIdentity
events = _Events_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 44, 0)
)
_Pdu8306Objects_ObjectIdentity = ObjectIdentity
pdu8306Objects = _Pdu8306Objects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 44, 1)
)
_Pdu8306CommonConfig_ObjectIdentity = ObjectIdentity
pdu8306CommonConfig = _Pdu8306CommonConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 44, 1, 1)
)
_Pdu8306SNMPaccess_ObjectIdentity = ObjectIdentity
pdu8306SNMPaccess = _Pdu8306SNMPaccess_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 44, 1, 1, 1)
)


class _Pdu8306TrapCtrl_Type(Integer32):
    """Custom type pdu8306TrapCtrl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_Pdu8306TrapCtrl_Type.__name__ = "Integer32"
_Pdu8306TrapCtrl_Object = MibScalar
pdu8306TrapCtrl = _Pdu8306TrapCtrl_Object(
    (1, 3, 6, 1, 4, 1, 28507, 44, 1, 1, 1, 1),
    _Pdu8306TrapCtrl_Type()
)
pdu8306TrapCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdu8306TrapCtrl.setStatus("current")
_Pdu8306TrapIPTable_Object = MibTable
pdu8306TrapIPTable = _Pdu8306TrapIPTable_Object(
    (1, 3, 6, 1, 4, 1, 28507, 44, 1, 1, 1, 2)
)
if mibBuilder.loadTexts:
    pdu8306TrapIPTable.setStatus("current")
_Pdu8306TrapIPEntry_Object = MibTableRow
pdu8306TrapIPEntry = _Pdu8306TrapIPEntry_Object(
    (1, 3, 6, 1, 4, 1, 28507, 44, 1, 1, 1, 2, 1)
)
pdu8306TrapIPEntry.setIndexNames(
    (0, "GUDEADS-PDU8306-MIB", "pdu8306TrapIPIndex"),
)
if mibBuilder.loadTexts:
    pdu8306TrapIPEntry.setStatus("current")


class _Pdu8306TrapIPIndex_Type(Integer32):
    """Custom type pdu8306TrapIPIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_Pdu8306TrapIPIndex_Type.__name__ = "Integer32"
_Pdu8306TrapIPIndex_Object = MibTableColumn
pdu8306TrapIPIndex = _Pdu8306TrapIPIndex_Object(
    (1, 3, 6, 1, 4, 1, 28507, 44, 1, 1, 1, 2, 1, 1),
    _Pdu8306TrapIPIndex_Type()
)
pdu8306TrapIPIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pdu8306TrapIPIndex.setStatus("current")


class _Pdu8306TrapAddr_Type(OctetString):
    """Custom type pdu8306TrapAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 99),
    )


_Pdu8306TrapAddr_Type.__name__ = "OctetString"
_Pdu8306TrapAddr_Object = MibTableColumn
pdu8306TrapAddr = _Pdu8306TrapAddr_Object(
    (1, 3, 6, 1, 4, 1, 28507, 44, 1, 1, 1, 2, 1, 2),
    _Pdu8306TrapAddr_Type()
)
pdu8306TrapAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdu8306TrapAddr.setStatus("current")
_Pdu8306DeviceConfig_ObjectIdentity = ObjectIdentity
pdu8306DeviceConfig = _Pdu8306DeviceConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 44, 1, 2)
)
_Pdu8306IntActors_ObjectIdentity = ObjectIdentity
pdu8306IntActors = _Pdu8306IntActors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 44, 1, 3)
)
_Pdu8306ExtActors_ObjectIdentity = ObjectIdentity
pdu8306ExtActors = _Pdu8306ExtActors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 44, 1, 4)
)
_Pdu8306IntSensors_ObjectIdentity = ObjectIdentity
pdu8306IntSensors = _Pdu8306IntSensors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 44, 1, 5)
)
_Pdu8306PowerChan_ObjectIdentity = ObjectIdentity
pdu8306PowerChan = _Pdu8306PowerChan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 44, 1, 5, 1)
)


class _Pdu8306ActivePowerChan_Type(Unsigned32):
    """Custom type pdu8306ActivePowerChan based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_Pdu8306ActivePowerChan_Type.__name__ = "Unsigned32"
_Pdu8306ActivePowerChan_Object = MibScalar
pdu8306ActivePowerChan = _Pdu8306ActivePowerChan_Object(
    (1, 3, 6, 1, 4, 1, 28507, 44, 1, 5, 1, 1),
    _Pdu8306ActivePowerChan_Type()
)
pdu8306ActivePowerChan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu8306ActivePowerChan.setStatus("current")
_Pdu8306PowerTable_Object = MibTable
pdu8306PowerTable = _Pdu8306PowerTable_Object(
    (1, 3, 6, 1, 4, 1, 28507, 44, 1, 5, 1, 2)
)
if mibBuilder.loadTexts:
    pdu8306PowerTable.setStatus("current")
_Pdu8306PowerEntry_Object = MibTableRow
pdu8306PowerEntry = _Pdu8306PowerEntry_Object(
    (1, 3, 6, 1, 4, 1, 28507, 44, 1, 5, 1, 2, 1)
)
pdu8306PowerEntry.setIndexNames(
    (0, "GUDEADS-PDU8306-MIB", "pdu8306PowerIndex"),
)
if mibBuilder.loadTexts:
    pdu8306PowerEntry.setStatus("current")


class _Pdu8306PowerIndex_Type(Integer32):
    """Custom type pdu8306PowerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_Pdu8306PowerIndex_Type.__name__ = "Integer32"
_Pdu8306PowerIndex_Object = MibTableColumn
pdu8306PowerIndex = _Pdu8306PowerIndex_Object(
    (1, 3, 6, 1, 4, 1, 28507, 44, 1, 5, 1, 2, 1, 1),
    _Pdu8306PowerIndex_Type()
)
pdu8306PowerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pdu8306PowerIndex.setStatus("current")


class _Pdu8306ChanStatus_Type(Integer32):
    """Custom type pdu8306ChanStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Pdu8306ChanStatus_Type.__name__ = "Integer32"
_Pdu8306ChanStatus_Object = MibTableColumn
pdu8306ChanStatus = _Pdu8306ChanStatus_Object(
    (1, 3, 6, 1, 4, 1, 28507, 44, 1, 5, 1, 2, 1, 2),
    _Pdu8306ChanStatus_Type()
)
pdu8306ChanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu8306ChanStatus.setStatus("current")
_Pdu8306AbsEnergyActive_Type = Unsigned32
_Pdu8306AbsEnergyActive_Object = MibTableColumn
pdu8306AbsEnergyActive = _Pdu8306AbsEnergyActive_Object(
    (1, 3, 6, 1, 4, 1, 28507, 44, 1, 5, 1, 2, 1, 3),
    _Pdu8306AbsEnergyActive_Type()
)
pdu8306AbsEnergyActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu8306AbsEnergyActive.setStatus("current")
if mibBuilder.loadTexts:
    pdu8306AbsEnergyActive.setUnits("Wh")
_Pdu8306PowerActive_Type = Integer32
_Pdu8306PowerActive_Object = MibTableColumn
pdu8306PowerActive = _Pdu8306PowerActive_Object(
    (1, 3, 6, 1, 4, 1, 28507, 44, 1, 5, 1, 2, 1, 4),
    _Pdu8306PowerActive_Type()
)
pdu8306PowerActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu8306PowerActive.setStatus("current")
if mibBuilder.loadTexts:
    pdu8306PowerActive.setUnits("W")
_Pdu8306Current_Type = Unsigned32
_Pdu8306Current_Object = MibTableColumn
pdu8306Current = _Pdu8306Current_Object(
    (1, 3, 6, 1, 4, 1, 28507, 44, 1, 5, 1, 2, 1, 5),
    _Pdu8306Current_Type()
)
pdu8306Current.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu8306Current.setStatus("current")
if mibBuilder.loadTexts:
    pdu8306Current.setUnits("mA")
_Pdu8306Voltage_Type = Unsigned32
_Pdu8306Voltage_Object = MibTableColumn
pdu8306Voltage = _Pdu8306Voltage_Object(
    (1, 3, 6, 1, 4, 1, 28507, 44, 1, 5, 1, 2, 1, 6),
    _Pdu8306Voltage_Type()
)
pdu8306Voltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu8306Voltage.setStatus("current")
if mibBuilder.loadTexts:
    pdu8306Voltage.setUnits("V")
_Pdu8306Frequency_Type = Unsigned32
_Pdu8306Frequency_Object = MibTableColumn
pdu8306Frequency = _Pdu8306Frequency_Object(
    (1, 3, 6, 1, 4, 1, 28507, 44, 1, 5, 1, 2, 1, 7),
    _Pdu8306Frequency_Type()
)
pdu8306Frequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu8306Frequency.setStatus("current")
if mibBuilder.loadTexts:
    pdu8306Frequency.setUnits("0.01 hz")
_Pdu8306PowerFactor_Type = Integer32
_Pdu8306PowerFactor_Object = MibTableColumn
pdu8306PowerFactor = _Pdu8306PowerFactor_Object(
    (1, 3, 6, 1, 4, 1, 28507, 44, 1, 5, 1, 2, 1, 8),
    _Pdu8306PowerFactor_Type()
)
pdu8306PowerFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu8306PowerFactor.setStatus("current")
if mibBuilder.loadTexts:
    pdu8306PowerFactor.setUnits("0.001")
_Pdu8306Pangle_Type = Integer32
_Pdu8306Pangle_Object = MibTableColumn
pdu8306Pangle = _Pdu8306Pangle_Object(
    (1, 3, 6, 1, 4, 1, 28507, 44, 1, 5, 1, 2, 1, 9),
    _Pdu8306Pangle_Type()
)
pdu8306Pangle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu8306Pangle.setStatus("current")
if mibBuilder.loadTexts:
    pdu8306Pangle.setUnits("0.1 degree")
_Pdu8306PowerApparent_Type = Integer32
_Pdu8306PowerApparent_Object = MibTableColumn
pdu8306PowerApparent = _Pdu8306PowerApparent_Object(
    (1, 3, 6, 1, 4, 1, 28507, 44, 1, 5, 1, 2, 1, 10),
    _Pdu8306PowerApparent_Type()
)
pdu8306PowerApparent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu8306PowerApparent.setStatus("current")
if mibBuilder.loadTexts:
    pdu8306PowerApparent.setUnits("VA")
_Pdu8306PowerReactive_Type = Integer32
_Pdu8306PowerReactive_Object = MibTableColumn
pdu8306PowerReactive = _Pdu8306PowerReactive_Object(
    (1, 3, 6, 1, 4, 1, 28507, 44, 1, 5, 1, 2, 1, 11),
    _Pdu8306PowerReactive_Type()
)
pdu8306PowerReactive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu8306PowerReactive.setStatus("current")
if mibBuilder.loadTexts:
    pdu8306PowerReactive.setUnits("VAR")
_Pdu8306EnergyReactive_Type = Unsigned32
_Pdu8306EnergyReactive_Object = MibTableColumn
pdu8306EnergyReactive = _Pdu8306EnergyReactive_Object(
    (1, 3, 6, 1, 4, 1, 28507, 44, 1, 5, 1, 2, 1, 12),
    _Pdu8306EnergyReactive_Type()
)
pdu8306EnergyReactive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu8306EnergyReactive.setStatus("current")
if mibBuilder.loadTexts:
    pdu8306EnergyReactive.setUnits("VARh")
_Pdu8306EnergyActiveResettable_Type = Unsigned32
_Pdu8306EnergyActiveResettable_Object = MibTableColumn
pdu8306EnergyActiveResettable = _Pdu8306EnergyActiveResettable_Object(
    (1, 3, 6, 1, 4, 1, 28507, 44, 1, 5, 1, 2, 1, 13),
    _Pdu8306EnergyActiveResettable_Type()
)
pdu8306EnergyActiveResettable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu8306EnergyActiveResettable.setStatus("current")
if mibBuilder.loadTexts:
    pdu8306EnergyActiveResettable.setUnits("Wh")
_Pdu8306EnergyReactiveResettable_Type = Unsigned32
_Pdu8306EnergyReactiveResettable_Object = MibTableColumn
pdu8306EnergyReactiveResettable = _Pdu8306EnergyReactiveResettable_Object(
    (1, 3, 6, 1, 4, 1, 28507, 44, 1, 5, 1, 2, 1, 14),
    _Pdu8306EnergyReactiveResettable_Type()
)
pdu8306EnergyReactiveResettable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu8306EnergyReactiveResettable.setStatus("current")
if mibBuilder.loadTexts:
    pdu8306EnergyReactiveResettable.setUnits("VARh")
_Pdu8306ResetTime_Type = Unsigned32
_Pdu8306ResetTime_Object = MibTableColumn
pdu8306ResetTime = _Pdu8306ResetTime_Object(
    (1, 3, 6, 1, 4, 1, 28507, 44, 1, 5, 1, 2, 1, 15),
    _Pdu8306ResetTime_Type()
)
pdu8306ResetTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu8306ResetTime.setStatus("current")
if mibBuilder.loadTexts:
    pdu8306ResetTime.setUnits("s")


class _Pdu8306MeasurementBoxConnected_Type(Integer32):
    """Custom type pdu8306MeasurementBoxConnected based on Integer32"""
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


_Pdu8306MeasurementBoxConnected_Type.__name__ = "Integer32"
_Pdu8306MeasurementBoxConnected_Object = MibScalar
pdu8306MeasurementBoxConnected = _Pdu8306MeasurementBoxConnected_Object(
    (1, 3, 6, 1, 4, 1, 28507, 44, 1, 5, 12),
    _Pdu8306MeasurementBoxConnected_Type()
)
pdu8306MeasurementBoxConnected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu8306MeasurementBoxConnected.setStatus("current")
_Pdu8306ExtSensors_ObjectIdentity = ObjectIdentity
pdu8306ExtSensors = _Pdu8306ExtSensors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 44, 1, 6)
)
_Pdu8306SensorTable_Object = MibTable
pdu8306SensorTable = _Pdu8306SensorTable_Object(
    (1, 3, 6, 1, 4, 1, 28507, 44, 1, 6, 1)
)
if mibBuilder.loadTexts:
    pdu8306SensorTable.setStatus("current")
_Pdu8306SensorEntry_Object = MibTableRow
pdu8306SensorEntry = _Pdu8306SensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 28507, 44, 1, 6, 1, 1)
)
pdu8306SensorEntry.setIndexNames(
    (0, "GUDEADS-PDU8306-MIB", "pdu8306SensorIndex"),
)
if mibBuilder.loadTexts:
    pdu8306SensorEntry.setStatus("current")


class _Pdu8306SensorIndex_Type(Integer32):
    """Custom type pdu8306SensorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_Pdu8306SensorIndex_Type.__name__ = "Integer32"
_Pdu8306SensorIndex_Object = MibTableColumn
pdu8306SensorIndex = _Pdu8306SensorIndex_Object(
    (1, 3, 6, 1, 4, 1, 28507, 44, 1, 6, 1, 1, 1),
    _Pdu8306SensorIndex_Type()
)
pdu8306SensorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pdu8306SensorIndex.setStatus("current")
_Pdu8306TempSensor_Type = Integer32
_Pdu8306TempSensor_Object = MibTableColumn
pdu8306TempSensor = _Pdu8306TempSensor_Object(
    (1, 3, 6, 1, 4, 1, 28507, 44, 1, 6, 1, 1, 2),
    _Pdu8306TempSensor_Type()
)
pdu8306TempSensor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu8306TempSensor.setStatus("current")
if mibBuilder.loadTexts:
    pdu8306TempSensor.setUnits("0.1 degree Celsius")
_Pdu8306HygroSensor_Type = Integer32
_Pdu8306HygroSensor_Object = MibTableColumn
pdu8306HygroSensor = _Pdu8306HygroSensor_Object(
    (1, 3, 6, 1, 4, 1, 28507, 44, 1, 6, 1, 1, 3),
    _Pdu8306HygroSensor_Type()
)
pdu8306HygroSensor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu8306HygroSensor.setStatus("current")
if mibBuilder.loadTexts:
    pdu8306HygroSensor.setUnits("0.1 percent humidity")


class _Pdu8306InputSensor_Type(Integer32):
    """Custom type pdu8306InputSensor based on Integer32"""
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


_Pdu8306InputSensor_Type.__name__ = "Integer32"
_Pdu8306InputSensor_Object = MibTableColumn
pdu8306InputSensor = _Pdu8306InputSensor_Object(
    (1, 3, 6, 1, 4, 1, 28507, 44, 1, 6, 1, 1, 4),
    _Pdu8306InputSensor_Type()
)
pdu8306InputSensor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu8306InputSensor.setStatus("current")
_Pdu8306Conf_ObjectIdentity = ObjectIdentity
pdu8306Conf = _Pdu8306Conf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 44, 2)
)
_Pdu8306Groups_ObjectIdentity = ObjectIdentity
pdu8306Groups = _Pdu8306Groups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 44, 2, 1)
)
_Pdu8306Compls_ObjectIdentity = ObjectIdentity
pdu8306Compls = _Pdu8306Compls_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 44, 2, 2)
)

# Managed Objects groups

pdu8306BasicGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 28507, 44, 2, 1, 1)
)
pdu8306BasicGroup.setObjects(
      *(("GUDEADS-PDU8306-MIB", "pdu8306TrapCtrl"),
        ("GUDEADS-PDU8306-MIB", "pdu8306TrapAddr"),
        ("GUDEADS-PDU8306-MIB", "pdu8306ActivePowerChan"),
        ("GUDEADS-PDU8306-MIB", "pdu8306ChanStatus"),
        ("GUDEADS-PDU8306-MIB", "pdu8306AbsEnergyActive"),
        ("GUDEADS-PDU8306-MIB", "pdu8306PowerActive"),
        ("GUDEADS-PDU8306-MIB", "pdu8306Current"),
        ("GUDEADS-PDU8306-MIB", "pdu8306Voltage"),
        ("GUDEADS-PDU8306-MIB", "pdu8306Frequency"),
        ("GUDEADS-PDU8306-MIB", "pdu8306PowerFactor"),
        ("GUDEADS-PDU8306-MIB", "pdu8306Pangle"),
        ("GUDEADS-PDU8306-MIB", "pdu8306PowerApparent"),
        ("GUDEADS-PDU8306-MIB", "pdu8306PowerReactive"),
        ("GUDEADS-PDU8306-MIB", "pdu8306EnergyReactive"),
        ("GUDEADS-PDU8306-MIB", "pdu8306EnergyActiveResettable"),
        ("GUDEADS-PDU8306-MIB", "pdu8306EnergyReactiveResettable"),
        ("GUDEADS-PDU8306-MIB", "pdu8306ResetTime"),
        ("GUDEADS-PDU8306-MIB", "pdu8306MeasurementBoxConnected"),
        ("GUDEADS-PDU8306-MIB", "pdu8306TempSensor"),
        ("GUDEADS-PDU8306-MIB", "pdu8306HygroSensor"),
        ("GUDEADS-PDU8306-MIB", "pdu8306InputSensor"))
)
if mibBuilder.loadTexts:
    pdu8306BasicGroup.setStatus("current")


# Notification objects

pdu8306TempEvtSen1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 28507, 44, 0, 1)
)
pdu8306TempEvtSen1.setObjects(
    ("GUDEADS-PDU8306-MIB", "pdu8306TempSensor")
)
if mibBuilder.loadTexts:
    pdu8306TempEvtSen1.setStatus(
        "current"
    )

pdu8306HygroEvtSen1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 28507, 44, 0, 2)
)
pdu8306HygroEvtSen1.setObjects(
    ("GUDEADS-PDU8306-MIB", "pdu8306HygroSensor")
)
if mibBuilder.loadTexts:
    pdu8306HygroEvtSen1.setStatus(
        "current"
    )

pdu8306MeasurementBoxEvt = NotificationType(
    (1, 3, 6, 1, 4, 1, 28507, 44, 0, 3)
)
pdu8306MeasurementBoxEvt.setObjects(
    ("GUDEADS-PDU8306-MIB", "pdu8306MeasurementBoxConnected")
)
if mibBuilder.loadTexts:
    pdu8306MeasurementBoxEvt.setStatus(
        "current"
    )


# Notifications groups

pdu8306NotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 28507, 44, 2, 1, 2)
)
pdu8306NotificationGroup.setObjects(
      *(("GUDEADS-PDU8306-MIB", "pdu8306TempEvtSen1"),
        ("GUDEADS-PDU8306-MIB", "pdu8306HygroEvtSen1"),
        ("GUDEADS-PDU8306-MIB", "pdu8306MeasurementBoxEvt"))
)
if mibBuilder.loadTexts:
    pdu8306NotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "GUDEADS-PDU8306-MIB",
    **{"gudeads": gudeads,
       "gadsPDU8306": gadsPDU8306,
       "events": events,
       "pdu8306TempEvtSen1": pdu8306TempEvtSen1,
       "pdu8306HygroEvtSen1": pdu8306HygroEvtSen1,
       "pdu8306MeasurementBoxEvt": pdu8306MeasurementBoxEvt,
       "pdu8306Objects": pdu8306Objects,
       "pdu8306CommonConfig": pdu8306CommonConfig,
       "pdu8306SNMPaccess": pdu8306SNMPaccess,
       "pdu8306TrapCtrl": pdu8306TrapCtrl,
       "pdu8306TrapIPTable": pdu8306TrapIPTable,
       "pdu8306TrapIPEntry": pdu8306TrapIPEntry,
       "pdu8306TrapIPIndex": pdu8306TrapIPIndex,
       "pdu8306TrapAddr": pdu8306TrapAddr,
       "pdu8306DeviceConfig": pdu8306DeviceConfig,
       "pdu8306IntActors": pdu8306IntActors,
       "pdu8306ExtActors": pdu8306ExtActors,
       "pdu8306IntSensors": pdu8306IntSensors,
       "pdu8306PowerChan": pdu8306PowerChan,
       "pdu8306ActivePowerChan": pdu8306ActivePowerChan,
       "pdu8306PowerTable": pdu8306PowerTable,
       "pdu8306PowerEntry": pdu8306PowerEntry,
       "pdu8306PowerIndex": pdu8306PowerIndex,
       "pdu8306ChanStatus": pdu8306ChanStatus,
       "pdu8306AbsEnergyActive": pdu8306AbsEnergyActive,
       "pdu8306PowerActive": pdu8306PowerActive,
       "pdu8306Current": pdu8306Current,
       "pdu8306Voltage": pdu8306Voltage,
       "pdu8306Frequency": pdu8306Frequency,
       "pdu8306PowerFactor": pdu8306PowerFactor,
       "pdu8306Pangle": pdu8306Pangle,
       "pdu8306PowerApparent": pdu8306PowerApparent,
       "pdu8306PowerReactive": pdu8306PowerReactive,
       "pdu8306EnergyReactive": pdu8306EnergyReactive,
       "pdu8306EnergyActiveResettable": pdu8306EnergyActiveResettable,
       "pdu8306EnergyReactiveResettable": pdu8306EnergyReactiveResettable,
       "pdu8306ResetTime": pdu8306ResetTime,
       "pdu8306MeasurementBoxConnected": pdu8306MeasurementBoxConnected,
       "pdu8306ExtSensors": pdu8306ExtSensors,
       "pdu8306SensorTable": pdu8306SensorTable,
       "pdu8306SensorEntry": pdu8306SensorEntry,
       "pdu8306SensorIndex": pdu8306SensorIndex,
       "pdu8306TempSensor": pdu8306TempSensor,
       "pdu8306HygroSensor": pdu8306HygroSensor,
       "pdu8306InputSensor": pdu8306InputSensor,
       "pdu8306Conf": pdu8306Conf,
       "pdu8306Groups": pdu8306Groups,
       "pdu8306BasicGroup": pdu8306BasicGroup,
       "pdu8306NotificationGroup": pdu8306NotificationGroup,
       "pdu8306Compls": pdu8306Compls}
)
