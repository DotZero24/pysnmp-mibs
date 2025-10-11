# SNMP MIB module (GUDEADS-ATS3020-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/gude/GUDEADS-ATS3020-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:07:00 2025
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
        ("2007-05-23 12:44",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_GadsATS3020_ObjectIdentity = ObjectIdentity
gadsATS3020 = _GadsATS3020_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 40)
)
_Ats3020Events_ObjectIdentity = ObjectIdentity
ats3020Events = _Ats3020Events_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 40, 0)
)
_Ats3020Objects_ObjectIdentity = ObjectIdentity
ats3020Objects = _Ats3020Objects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 40, 1)
)
_Ats3020CommonConfig_ObjectIdentity = ObjectIdentity
ats3020CommonConfig = _Ats3020CommonConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 40, 1, 1)
)
_Ats3020SNMPaccess_ObjectIdentity = ObjectIdentity
ats3020SNMPaccess = _Ats3020SNMPaccess_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 40, 1, 1, 1)
)


class _Ats3020TrapCtrl_Type(Integer32):
    """Custom type ats3020TrapCtrl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_Ats3020TrapCtrl_Type.__name__ = "Integer32"
_Ats3020TrapCtrl_Object = MibScalar
ats3020TrapCtrl = _Ats3020TrapCtrl_Object(
    (1, 3, 6, 1, 4, 1, 28507, 40, 1, 1, 1, 1),
    _Ats3020TrapCtrl_Type()
)
ats3020TrapCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ats3020TrapCtrl.setStatus("current")
_Ats3020TrapIPTable_Object = MibTable
ats3020TrapIPTable = _Ats3020TrapIPTable_Object(
    (1, 3, 6, 1, 4, 1, 28507, 40, 1, 1, 1, 2)
)
if mibBuilder.loadTexts:
    ats3020TrapIPTable.setStatus("current")
_Ats3020TrapIPEntry_Object = MibTableRow
ats3020TrapIPEntry = _Ats3020TrapIPEntry_Object(
    (1, 3, 6, 1, 4, 1, 28507, 40, 1, 1, 1, 2, 1)
)
ats3020TrapIPEntry.setIndexNames(
    (0, "GUDEADS-ATS3020-MIB", "ats3020TrapIPIndex"),
)
if mibBuilder.loadTexts:
    ats3020TrapIPEntry.setStatus("current")


class _Ats3020TrapIPIndex_Type(Integer32):
    """Custom type ats3020TrapIPIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_Ats3020TrapIPIndex_Type.__name__ = "Integer32"
_Ats3020TrapIPIndex_Object = MibTableColumn
ats3020TrapIPIndex = _Ats3020TrapIPIndex_Object(
    (1, 3, 6, 1, 4, 1, 28507, 40, 1, 1, 1, 2, 1, 1),
    _Ats3020TrapIPIndex_Type()
)
ats3020TrapIPIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ats3020TrapIPIndex.setStatus("current")


class _Ats3020TrapAddr_Type(OctetString):
    """Custom type ats3020TrapAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 99),
    )


_Ats3020TrapAddr_Type.__name__ = "OctetString"
_Ats3020TrapAddr_Object = MibTableColumn
ats3020TrapAddr = _Ats3020TrapAddr_Object(
    (1, 3, 6, 1, 4, 1, 28507, 40, 1, 1, 1, 2, 1, 2),
    _Ats3020TrapAddr_Type()
)
ats3020TrapAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ats3020TrapAddr.setStatus("current")
_Ats3020IntActors_ObjectIdentity = ObjectIdentity
ats3020IntActors = _Ats3020IntActors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 40, 1, 3)
)


class _Ats3020Buzzer_Type(Integer32):
    """Custom type ats3020Buzzer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Ats3020Buzzer_Type.__name__ = "Integer32"
_Ats3020Buzzer_Object = MibScalar
ats3020Buzzer = _Ats3020Buzzer_Object(
    (1, 3, 6, 1, 4, 1, 28507, 40, 1, 3, 10),
    _Ats3020Buzzer_Type()
)
ats3020Buzzer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ats3020Buzzer.setStatus("current")
if mibBuilder.loadTexts:
    ats3020Buzzer.setUnits("0 = Off, 1 = On")
_Ats3020IntSensors_ObjectIdentity = ObjectIdentity
ats3020IntSensors = _Ats3020IntSensors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 40, 1, 5)
)
_Ats3020PowerChan_ObjectIdentity = ObjectIdentity
ats3020PowerChan = _Ats3020PowerChan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 40, 1, 5, 1)
)


class _Ats3020ActivePowerChan_Type(Unsigned32):
    """Custom type ats3020ActivePowerChan based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_Ats3020ActivePowerChan_Type.__name__ = "Unsigned32"
_Ats3020ActivePowerChan_Object = MibScalar
ats3020ActivePowerChan = _Ats3020ActivePowerChan_Object(
    (1, 3, 6, 1, 4, 1, 28507, 40, 1, 5, 1, 1),
    _Ats3020ActivePowerChan_Type()
)
ats3020ActivePowerChan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ats3020ActivePowerChan.setStatus("current")
_Ats3020PowerTable_Object = MibTable
ats3020PowerTable = _Ats3020PowerTable_Object(
    (1, 3, 6, 1, 4, 1, 28507, 40, 1, 5, 1, 2)
)
if mibBuilder.loadTexts:
    ats3020PowerTable.setStatus("current")
_Ats3020PowerEntry_Object = MibTableRow
ats3020PowerEntry = _Ats3020PowerEntry_Object(
    (1, 3, 6, 1, 4, 1, 28507, 40, 1, 5, 1, 2, 1)
)
ats3020PowerEntry.setIndexNames(
    (0, "GUDEADS-ATS3020-MIB", "ats3020PowerIndex"),
)
if mibBuilder.loadTexts:
    ats3020PowerEntry.setStatus("current")


class _Ats3020PowerIndex_Type(Integer32):
    """Custom type ats3020PowerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_Ats3020PowerIndex_Type.__name__ = "Integer32"
_Ats3020PowerIndex_Object = MibTableColumn
ats3020PowerIndex = _Ats3020PowerIndex_Object(
    (1, 3, 6, 1, 4, 1, 28507, 40, 1, 5, 1, 2, 1, 1),
    _Ats3020PowerIndex_Type()
)
ats3020PowerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ats3020PowerIndex.setStatus("current")


class _Ats3020ChanStatus_Type(Integer32):
    """Custom type ats3020ChanStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Ats3020ChanStatus_Type.__name__ = "Integer32"
_Ats3020ChanStatus_Object = MibTableColumn
ats3020ChanStatus = _Ats3020ChanStatus_Object(
    (1, 3, 6, 1, 4, 1, 28507, 40, 1, 5, 1, 2, 1, 2),
    _Ats3020ChanStatus_Type()
)
ats3020ChanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ats3020ChanStatus.setStatus("current")
_Ats3020AbsEnergyActive_Type = Unsigned32
_Ats3020AbsEnergyActive_Object = MibTableColumn
ats3020AbsEnergyActive = _Ats3020AbsEnergyActive_Object(
    (1, 3, 6, 1, 4, 1, 28507, 40, 1, 5, 1, 2, 1, 3),
    _Ats3020AbsEnergyActive_Type()
)
ats3020AbsEnergyActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ats3020AbsEnergyActive.setStatus("current")
if mibBuilder.loadTexts:
    ats3020AbsEnergyActive.setUnits("Wh")
_Ats3020PowerActive_Type = Integer32
_Ats3020PowerActive_Object = MibTableColumn
ats3020PowerActive = _Ats3020PowerActive_Object(
    (1, 3, 6, 1, 4, 1, 28507, 40, 1, 5, 1, 2, 1, 4),
    _Ats3020PowerActive_Type()
)
ats3020PowerActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ats3020PowerActive.setStatus("current")
if mibBuilder.loadTexts:
    ats3020PowerActive.setUnits("W")
_Ats3020Current_Type = Unsigned32
_Ats3020Current_Object = MibTableColumn
ats3020Current = _Ats3020Current_Object(
    (1, 3, 6, 1, 4, 1, 28507, 40, 1, 5, 1, 2, 1, 5),
    _Ats3020Current_Type()
)
ats3020Current.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ats3020Current.setStatus("current")
if mibBuilder.loadTexts:
    ats3020Current.setUnits("mA")
_Ats3020Voltage_Type = Unsigned32
_Ats3020Voltage_Object = MibTableColumn
ats3020Voltage = _Ats3020Voltage_Object(
    (1, 3, 6, 1, 4, 1, 28507, 40, 1, 5, 1, 2, 1, 6),
    _Ats3020Voltage_Type()
)
ats3020Voltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ats3020Voltage.setStatus("current")
if mibBuilder.loadTexts:
    ats3020Voltage.setUnits("V")
_Ats3020Frequency_Type = Unsigned32
_Ats3020Frequency_Object = MibTableColumn
ats3020Frequency = _Ats3020Frequency_Object(
    (1, 3, 6, 1, 4, 1, 28507, 40, 1, 5, 1, 2, 1, 7),
    _Ats3020Frequency_Type()
)
ats3020Frequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ats3020Frequency.setStatus("current")
if mibBuilder.loadTexts:
    ats3020Frequency.setUnits("0.01 hz")
_Ats3020PowerFactor_Type = Integer32
_Ats3020PowerFactor_Object = MibTableColumn
ats3020PowerFactor = _Ats3020PowerFactor_Object(
    (1, 3, 6, 1, 4, 1, 28507, 40, 1, 5, 1, 2, 1, 8),
    _Ats3020PowerFactor_Type()
)
ats3020PowerFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ats3020PowerFactor.setStatus("current")
if mibBuilder.loadTexts:
    ats3020PowerFactor.setUnits("0.001")
_Ats3020Pangle_Type = Integer32
_Ats3020Pangle_Object = MibTableColumn
ats3020Pangle = _Ats3020Pangle_Object(
    (1, 3, 6, 1, 4, 1, 28507, 40, 1, 5, 1, 2, 1, 9),
    _Ats3020Pangle_Type()
)
ats3020Pangle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ats3020Pangle.setStatus("current")
if mibBuilder.loadTexts:
    ats3020Pangle.setUnits("0.1 degree")
_Ats3020PowerApparent_Type = Integer32
_Ats3020PowerApparent_Object = MibTableColumn
ats3020PowerApparent = _Ats3020PowerApparent_Object(
    (1, 3, 6, 1, 4, 1, 28507, 40, 1, 5, 1, 2, 1, 10),
    _Ats3020PowerApparent_Type()
)
ats3020PowerApparent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ats3020PowerApparent.setStatus("current")
if mibBuilder.loadTexts:
    ats3020PowerApparent.setUnits("VA")
_Ats3020PowerReactive_Type = Integer32
_Ats3020PowerReactive_Object = MibTableColumn
ats3020PowerReactive = _Ats3020PowerReactive_Object(
    (1, 3, 6, 1, 4, 1, 28507, 40, 1, 5, 1, 2, 1, 11),
    _Ats3020PowerReactive_Type()
)
ats3020PowerReactive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ats3020PowerReactive.setStatus("current")
if mibBuilder.loadTexts:
    ats3020PowerReactive.setUnits("VAR")
_Ats3020AbsEnergyReactive_Type = Unsigned32
_Ats3020AbsEnergyReactive_Object = MibTableColumn
ats3020AbsEnergyReactive = _Ats3020AbsEnergyReactive_Object(
    (1, 3, 6, 1, 4, 1, 28507, 40, 1, 5, 1, 2, 1, 12),
    _Ats3020AbsEnergyReactive_Type()
)
ats3020AbsEnergyReactive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ats3020AbsEnergyReactive.setStatus("current")
if mibBuilder.loadTexts:
    ats3020AbsEnergyReactive.setUnits("VARh")
_Ats3020AbsEnergyActiveResettable_Type = Unsigned32
_Ats3020AbsEnergyActiveResettable_Object = MibTableColumn
ats3020AbsEnergyActiveResettable = _Ats3020AbsEnergyActiveResettable_Object(
    (1, 3, 6, 1, 4, 1, 28507, 40, 1, 5, 1, 2, 1, 13),
    _Ats3020AbsEnergyActiveResettable_Type()
)
ats3020AbsEnergyActiveResettable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ats3020AbsEnergyActiveResettable.setStatus("current")
if mibBuilder.loadTexts:
    ats3020AbsEnergyActiveResettable.setUnits("Wh")
_Ats3020AbsEnergyReactiveResettable_Type = Unsigned32
_Ats3020AbsEnergyReactiveResettable_Object = MibTableColumn
ats3020AbsEnergyReactiveResettable = _Ats3020AbsEnergyReactiveResettable_Object(
    (1, 3, 6, 1, 4, 1, 28507, 40, 1, 5, 1, 2, 1, 14),
    _Ats3020AbsEnergyReactiveResettable_Type()
)
ats3020AbsEnergyReactiveResettable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ats3020AbsEnergyReactiveResettable.setStatus("current")
if mibBuilder.loadTexts:
    ats3020AbsEnergyReactiveResettable.setUnits("VARh")
_Ats3020ResetTime_Type = Unsigned32
_Ats3020ResetTime_Object = MibTableColumn
ats3020ResetTime = _Ats3020ResetTime_Object(
    (1, 3, 6, 1, 4, 1, 28507, 40, 1, 5, 1, 2, 1, 15),
    _Ats3020ResetTime_Type()
)
ats3020ResetTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ats3020ResetTime.setStatus("current")
if mibBuilder.loadTexts:
    ats3020ResetTime.setUnits("s")
_Ats3020ForwEnergyActive_Type = Unsigned32
_Ats3020ForwEnergyActive_Object = MibTableColumn
ats3020ForwEnergyActive = _Ats3020ForwEnergyActive_Object(
    (1, 3, 6, 1, 4, 1, 28507, 40, 1, 5, 1, 2, 1, 16),
    _Ats3020ForwEnergyActive_Type()
)
ats3020ForwEnergyActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ats3020ForwEnergyActive.setStatus("current")
if mibBuilder.loadTexts:
    ats3020ForwEnergyActive.setUnits("Wh")
_Ats3020ForwEnergyReactive_Type = Unsigned32
_Ats3020ForwEnergyReactive_Object = MibTableColumn
ats3020ForwEnergyReactive = _Ats3020ForwEnergyReactive_Object(
    (1, 3, 6, 1, 4, 1, 28507, 40, 1, 5, 1, 2, 1, 17),
    _Ats3020ForwEnergyReactive_Type()
)
ats3020ForwEnergyReactive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ats3020ForwEnergyReactive.setStatus("current")
if mibBuilder.loadTexts:
    ats3020ForwEnergyReactive.setUnits("VARh")
_Ats3020ForwEnergyActiveResettable_Type = Unsigned32
_Ats3020ForwEnergyActiveResettable_Object = MibTableColumn
ats3020ForwEnergyActiveResettable = _Ats3020ForwEnergyActiveResettable_Object(
    (1, 3, 6, 1, 4, 1, 28507, 40, 1, 5, 1, 2, 1, 18),
    _Ats3020ForwEnergyActiveResettable_Type()
)
ats3020ForwEnergyActiveResettable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ats3020ForwEnergyActiveResettable.setStatus("current")
if mibBuilder.loadTexts:
    ats3020ForwEnergyActiveResettable.setUnits("Wh")
_Ats3020ForwEnergyReactiveResettable_Type = Unsigned32
_Ats3020ForwEnergyReactiveResettable_Object = MibTableColumn
ats3020ForwEnergyReactiveResettable = _Ats3020ForwEnergyReactiveResettable_Object(
    (1, 3, 6, 1, 4, 1, 28507, 40, 1, 5, 1, 2, 1, 19),
    _Ats3020ForwEnergyReactiveResettable_Type()
)
ats3020ForwEnergyReactiveResettable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ats3020ForwEnergyReactiveResettable.setStatus("current")
if mibBuilder.loadTexts:
    ats3020ForwEnergyReactiveResettable.setUnits("VARh")
_Ats3020RevEnergyActive_Type = Unsigned32
_Ats3020RevEnergyActive_Object = MibTableColumn
ats3020RevEnergyActive = _Ats3020RevEnergyActive_Object(
    (1, 3, 6, 1, 4, 1, 28507, 40, 1, 5, 1, 2, 1, 20),
    _Ats3020RevEnergyActive_Type()
)
ats3020RevEnergyActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ats3020RevEnergyActive.setStatus("current")
if mibBuilder.loadTexts:
    ats3020RevEnergyActive.setUnits("Wh")
_Ats3020RevEnergyReactive_Type = Unsigned32
_Ats3020RevEnergyReactive_Object = MibTableColumn
ats3020RevEnergyReactive = _Ats3020RevEnergyReactive_Object(
    (1, 3, 6, 1, 4, 1, 28507, 40, 1, 5, 1, 2, 1, 21),
    _Ats3020RevEnergyReactive_Type()
)
ats3020RevEnergyReactive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ats3020RevEnergyReactive.setStatus("current")
if mibBuilder.loadTexts:
    ats3020RevEnergyReactive.setUnits("VARh")
_Ats3020RevEnergyActiveResettable_Type = Unsigned32
_Ats3020RevEnergyActiveResettable_Object = MibTableColumn
ats3020RevEnergyActiveResettable = _Ats3020RevEnergyActiveResettable_Object(
    (1, 3, 6, 1, 4, 1, 28507, 40, 1, 5, 1, 2, 1, 22),
    _Ats3020RevEnergyActiveResettable_Type()
)
ats3020RevEnergyActiveResettable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ats3020RevEnergyActiveResettable.setStatus("current")
if mibBuilder.loadTexts:
    ats3020RevEnergyActiveResettable.setUnits("Wh")
_Ats3020RevEnergyReactiveResettable_Type = Unsigned32
_Ats3020RevEnergyReactiveResettable_Object = MibTableColumn
ats3020RevEnergyReactiveResettable = _Ats3020RevEnergyReactiveResettable_Object(
    (1, 3, 6, 1, 4, 1, 28507, 40, 1, 5, 1, 2, 1, 23),
    _Ats3020RevEnergyReactiveResettable_Type()
)
ats3020RevEnergyReactiveResettable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ats3020RevEnergyReactiveResettable.setStatus("current")
if mibBuilder.loadTexts:
    ats3020RevEnergyReactiveResettable.setUnits("VARh")
_Ats3020PowerInfo_ObjectIdentity = ObjectIdentity
ats3020PowerInfo = _Ats3020PowerInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 40, 1, 5, 11)
)
_Ats3020PrimPowAvail_Type = Integer32
_Ats3020PrimPowAvail_Object = MibScalar
ats3020PrimPowAvail = _Ats3020PrimPowAvail_Object(
    (1, 3, 6, 1, 4, 1, 28507, 40, 1, 5, 11, 1),
    _Ats3020PrimPowAvail_Type()
)
ats3020PrimPowAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ats3020PrimPowAvail.setStatus("current")
_Ats3020SecPowAvail_Type = Integer32
_Ats3020SecPowAvail_Object = MibScalar
ats3020SecPowAvail = _Ats3020SecPowAvail_Object(
    (1, 3, 6, 1, 4, 1, 28507, 40, 1, 5, 11, 2),
    _Ats3020SecPowAvail_Type()
)
ats3020SecPowAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ats3020SecPowAvail.setStatus("current")
_Ats3020PowerSelect_Type = Integer32
_Ats3020PowerSelect_Object = MibScalar
ats3020PowerSelect = _Ats3020PowerSelect_Object(
    (1, 3, 6, 1, 4, 1, 28507, 40, 1, 5, 11, 4),
    _Ats3020PowerSelect_Type()
)
ats3020PowerSelect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ats3020PowerSelect.setStatus("current")
_Ats3020ExtSensors_ObjectIdentity = ObjectIdentity
ats3020ExtSensors = _Ats3020ExtSensors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 40, 1, 6)
)
_Ats3020SensorTable_Object = MibTable
ats3020SensorTable = _Ats3020SensorTable_Object(
    (1, 3, 6, 1, 4, 1, 28507, 40, 1, 6, 1)
)
if mibBuilder.loadTexts:
    ats3020SensorTable.setStatus("current")
_Ats3020SensorEntry_Object = MibTableRow
ats3020SensorEntry = _Ats3020SensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 28507, 40, 1, 6, 1, 1)
)
ats3020SensorEntry.setIndexNames(
    (0, "GUDEADS-ATS3020-MIB", "ats3020SensorIndex"),
)
if mibBuilder.loadTexts:
    ats3020SensorEntry.setStatus("current")


class _Ats3020SensorIndex_Type(Integer32):
    """Custom type ats3020SensorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_Ats3020SensorIndex_Type.__name__ = "Integer32"
_Ats3020SensorIndex_Object = MibTableColumn
ats3020SensorIndex = _Ats3020SensorIndex_Object(
    (1, 3, 6, 1, 4, 1, 28507, 40, 1, 6, 1, 1, 1),
    _Ats3020SensorIndex_Type()
)
ats3020SensorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ats3020SensorIndex.setStatus("current")
_Ats3020TempSensor_Type = Integer32
_Ats3020TempSensor_Object = MibTableColumn
ats3020TempSensor = _Ats3020TempSensor_Object(
    (1, 3, 6, 1, 4, 1, 28507, 40, 1, 6, 1, 1, 2),
    _Ats3020TempSensor_Type()
)
ats3020TempSensor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ats3020TempSensor.setStatus("current")
if mibBuilder.loadTexts:
    ats3020TempSensor.setUnits("0.1 degree Celsius")
_Ats3020HygroSensor_Type = Integer32
_Ats3020HygroSensor_Object = MibTableColumn
ats3020HygroSensor = _Ats3020HygroSensor_Object(
    (1, 3, 6, 1, 4, 1, 28507, 40, 1, 6, 1, 1, 3),
    _Ats3020HygroSensor_Type()
)
ats3020HygroSensor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ats3020HygroSensor.setStatus("current")
if mibBuilder.loadTexts:
    ats3020HygroSensor.setUnits("0.1 percent humidity")


class _Ats3020InputSensor_Type(Integer32):
    """Custom type ats3020InputSensor based on Integer32"""
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


_Ats3020InputSensor_Type.__name__ = "Integer32"
_Ats3020InputSensor_Object = MibTableColumn
ats3020InputSensor = _Ats3020InputSensor_Object(
    (1, 3, 6, 1, 4, 1, 28507, 40, 1, 6, 1, 1, 4),
    _Ats3020InputSensor_Type()
)
ats3020InputSensor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ats3020InputSensor.setStatus("current")
_Ats3020Conf_ObjectIdentity = ObjectIdentity
ats3020Conf = _Ats3020Conf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 40, 3)
)
_Ats3020Groups_ObjectIdentity = ObjectIdentity
ats3020Groups = _Ats3020Groups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 40, 3, 1)
)
_Ats3020Compls_ObjectIdentity = ObjectIdentity
ats3020Compls = _Ats3020Compls_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28507, 40, 3, 2)
)

# Managed Objects groups

ats3020BasicGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 28507, 40, 3, 1, 1)
)
ats3020BasicGroup.setObjects(
      *(("GUDEADS-ATS3020-MIB", "ats3020TrapCtrl"),
        ("GUDEADS-ATS3020-MIB", "ats3020TrapAddr"),
        ("GUDEADS-ATS3020-MIB", "ats3020Buzzer"),
        ("GUDEADS-ATS3020-MIB", "ats3020ActivePowerChan"),
        ("GUDEADS-ATS3020-MIB", "ats3020ChanStatus"),
        ("GUDEADS-ATS3020-MIB", "ats3020AbsEnergyActive"),
        ("GUDEADS-ATS3020-MIB", "ats3020PowerActive"),
        ("GUDEADS-ATS3020-MIB", "ats3020Current"),
        ("GUDEADS-ATS3020-MIB", "ats3020Voltage"),
        ("GUDEADS-ATS3020-MIB", "ats3020Frequency"),
        ("GUDEADS-ATS3020-MIB", "ats3020PowerFactor"),
        ("GUDEADS-ATS3020-MIB", "ats3020Pangle"),
        ("GUDEADS-ATS3020-MIB", "ats3020PowerApparent"),
        ("GUDEADS-ATS3020-MIB", "ats3020PowerReactive"),
        ("GUDEADS-ATS3020-MIB", "ats3020AbsEnergyReactive"),
        ("GUDEADS-ATS3020-MIB", "ats3020AbsEnergyActiveResettable"),
        ("GUDEADS-ATS3020-MIB", "ats3020AbsEnergyReactiveResettable"),
        ("GUDEADS-ATS3020-MIB", "ats3020ResetTime"),
        ("GUDEADS-ATS3020-MIB", "ats3020ForwEnergyActive"),
        ("GUDEADS-ATS3020-MIB", "ats3020ForwEnergyReactive"),
        ("GUDEADS-ATS3020-MIB", "ats3020ForwEnergyActiveResettable"),
        ("GUDEADS-ATS3020-MIB", "ats3020ForwEnergyReactiveResettable"),
        ("GUDEADS-ATS3020-MIB", "ats3020RevEnergyActive"),
        ("GUDEADS-ATS3020-MIB", "ats3020RevEnergyReactive"),
        ("GUDEADS-ATS3020-MIB", "ats3020RevEnergyActiveResettable"),
        ("GUDEADS-ATS3020-MIB", "ats3020RevEnergyReactiveResettable"),
        ("GUDEADS-ATS3020-MIB", "ats3020PrimPowAvail"),
        ("GUDEADS-ATS3020-MIB", "ats3020SecPowAvail"),
        ("GUDEADS-ATS3020-MIB", "ats3020PowerSelect"),
        ("GUDEADS-ATS3020-MIB", "ats3020TempSensor"),
        ("GUDEADS-ATS3020-MIB", "ats3020HygroSensor"),
        ("GUDEADS-ATS3020-MIB", "ats3020InputSensor"))
)
if mibBuilder.loadTexts:
    ats3020BasicGroup.setStatus("current")


# Notification objects

ats3020PrimaryPowerChangeEvt = NotificationType(
    (1, 3, 6, 1, 4, 1, 28507, 40, 0, 1)
)
ats3020PrimaryPowerChangeEvt.setObjects(
    ("GUDEADS-ATS3020-MIB", "ats3020PrimPowAvail")
)
if mibBuilder.loadTexts:
    ats3020PrimaryPowerChangeEvt.setStatus(
        "current"
    )

ats3020SecondaryPowerChangeEvt = NotificationType(
    (1, 3, 6, 1, 4, 1, 28507, 40, 0, 2)
)
ats3020SecondaryPowerChangeEvt.setObjects(
    ("GUDEADS-ATS3020-MIB", "ats3020SecPowAvail")
)
if mibBuilder.loadTexts:
    ats3020SecondaryPowerChangeEvt.setStatus(
        "current"
    )

ats3020PowerSelectEvt = NotificationType(
    (1, 3, 6, 1, 4, 1, 28507, 40, 0, 3)
)
ats3020PowerSelectEvt.setObjects(
    ("GUDEADS-ATS3020-MIB", "ats3020PowerSelect")
)
if mibBuilder.loadTexts:
    ats3020PowerSelectEvt.setStatus(
        "current"
    )

ats3020TempEvtSen1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 28507, 40, 0, 4)
)
ats3020TempEvtSen1.setObjects(
    ("GUDEADS-ATS3020-MIB", "ats3020TempSensor")
)
if mibBuilder.loadTexts:
    ats3020TempEvtSen1.setStatus(
        "current"
    )

ats3020HygroEvtSen1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 28507, 40, 0, 5)
)
ats3020HygroEvtSen1.setObjects(
    ("GUDEADS-ATS3020-MIB", "ats3020HygroSensor")
)
if mibBuilder.loadTexts:
    ats3020HygroEvtSen1.setStatus(
        "current"
    )

ats3020InputEvtSen1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 28507, 40, 0, 6)
)
ats3020InputEvtSen1.setObjects(
    ("GUDEADS-ATS3020-MIB", "ats3020InputSensor")
)
if mibBuilder.loadTexts:
    ats3020InputEvtSen1.setStatus(
        "current"
    )

ats3020AmperageEvt1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 28507, 40, 0, 7)
)
ats3020AmperageEvt1.setObjects(
      *(("GUDEADS-ATS3020-MIB", "ats3020PowerActive"),
        ("GUDEADS-ATS3020-MIB", "ats3020Current"),
        ("GUDEADS-ATS3020-MIB", "ats3020Voltage"),
        ("GUDEADS-ATS3020-MIB", "ats3020Frequency"),
        ("GUDEADS-ATS3020-MIB", "ats3020PowerApparent"),
        ("GUDEADS-ATS3020-MIB", "ats3020PowerReactive"))
)
if mibBuilder.loadTexts:
    ats3020AmperageEvt1.setStatus(
        "current"
    )


# Notifications groups

ats3020NotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 28507, 40, 3, 1, 2)
)
ats3020NotificationGroup.setObjects(
      *(("GUDEADS-ATS3020-MIB", "ats3020PrimaryPowerChangeEvt"),
        ("GUDEADS-ATS3020-MIB", "ats3020SecondaryPowerChangeEvt"),
        ("GUDEADS-ATS3020-MIB", "ats3020PowerSelectEvt"),
        ("GUDEADS-ATS3020-MIB", "ats3020TempEvtSen1"),
        ("GUDEADS-ATS3020-MIB", "ats3020HygroEvtSen1"),
        ("GUDEADS-ATS3020-MIB", "ats3020InputEvtSen1"),
        ("GUDEADS-ATS3020-MIB", "ats3020AmperageEvt1"))
)
if mibBuilder.loadTexts:
    ats3020NotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "GUDEADS-ATS3020-MIB",
    **{"gudeads": gudeads,
       "gadsATS3020": gadsATS3020,
       "ats3020Events": ats3020Events,
       "ats3020PrimaryPowerChangeEvt": ats3020PrimaryPowerChangeEvt,
       "ats3020SecondaryPowerChangeEvt": ats3020SecondaryPowerChangeEvt,
       "ats3020PowerSelectEvt": ats3020PowerSelectEvt,
       "ats3020TempEvtSen1": ats3020TempEvtSen1,
       "ats3020HygroEvtSen1": ats3020HygroEvtSen1,
       "ats3020InputEvtSen1": ats3020InputEvtSen1,
       "ats3020AmperageEvt1": ats3020AmperageEvt1,
       "ats3020Objects": ats3020Objects,
       "ats3020CommonConfig": ats3020CommonConfig,
       "ats3020SNMPaccess": ats3020SNMPaccess,
       "ats3020TrapCtrl": ats3020TrapCtrl,
       "ats3020TrapIPTable": ats3020TrapIPTable,
       "ats3020TrapIPEntry": ats3020TrapIPEntry,
       "ats3020TrapIPIndex": ats3020TrapIPIndex,
       "ats3020TrapAddr": ats3020TrapAddr,
       "ats3020IntActors": ats3020IntActors,
       "ats3020Buzzer": ats3020Buzzer,
       "ats3020IntSensors": ats3020IntSensors,
       "ats3020PowerChan": ats3020PowerChan,
       "ats3020ActivePowerChan": ats3020ActivePowerChan,
       "ats3020PowerTable": ats3020PowerTable,
       "ats3020PowerEntry": ats3020PowerEntry,
       "ats3020PowerIndex": ats3020PowerIndex,
       "ats3020ChanStatus": ats3020ChanStatus,
       "ats3020AbsEnergyActive": ats3020AbsEnergyActive,
       "ats3020PowerActive": ats3020PowerActive,
       "ats3020Current": ats3020Current,
       "ats3020Voltage": ats3020Voltage,
       "ats3020Frequency": ats3020Frequency,
       "ats3020PowerFactor": ats3020PowerFactor,
       "ats3020Pangle": ats3020Pangle,
       "ats3020PowerApparent": ats3020PowerApparent,
       "ats3020PowerReactive": ats3020PowerReactive,
       "ats3020AbsEnergyReactive": ats3020AbsEnergyReactive,
       "ats3020AbsEnergyActiveResettable": ats3020AbsEnergyActiveResettable,
       "ats3020AbsEnergyReactiveResettable": ats3020AbsEnergyReactiveResettable,
       "ats3020ResetTime": ats3020ResetTime,
       "ats3020ForwEnergyActive": ats3020ForwEnergyActive,
       "ats3020ForwEnergyReactive": ats3020ForwEnergyReactive,
       "ats3020ForwEnergyActiveResettable": ats3020ForwEnergyActiveResettable,
       "ats3020ForwEnergyReactiveResettable": ats3020ForwEnergyReactiveResettable,
       "ats3020RevEnergyActive": ats3020RevEnergyActive,
       "ats3020RevEnergyReactive": ats3020RevEnergyReactive,
       "ats3020RevEnergyActiveResettable": ats3020RevEnergyActiveResettable,
       "ats3020RevEnergyReactiveResettable": ats3020RevEnergyReactiveResettable,
       "ats3020PowerInfo": ats3020PowerInfo,
       "ats3020PrimPowAvail": ats3020PrimPowAvail,
       "ats3020SecPowAvail": ats3020SecPowAvail,
       "ats3020PowerSelect": ats3020PowerSelect,
       "ats3020ExtSensors": ats3020ExtSensors,
       "ats3020SensorTable": ats3020SensorTable,
       "ats3020SensorEntry": ats3020SensorEntry,
       "ats3020SensorIndex": ats3020SensorIndex,
       "ats3020TempSensor": ats3020TempSensor,
       "ats3020HygroSensor": ats3020HygroSensor,
       "ats3020InputSensor": ats3020InputSensor,
       "ats3020Conf": ats3020Conf,
       "ats3020Groups": ats3020Groups,
       "ats3020BasicGroup": ats3020BasicGroup,
       "ats3020NotificationGroup": ats3020NotificationGroup,
       "ats3020Compls": ats3020Compls}
)
