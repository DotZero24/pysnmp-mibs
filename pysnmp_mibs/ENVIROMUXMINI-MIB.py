# SNMP MIB module (ENVIROMUXMINI-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/nti/ENVIROMUXMINI-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:06:01 2025
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

enviromuxMini = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3699, 1, 1, 3)
)
if mibBuilder.loadTexts:
    enviromuxMini.setRevisions(
        ("2009-09-24 14:00",
         "2007-04-13 14:00",
         "2005-03-30 14:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class DecimalPointValue(TextualConvention, Integer32):
    status = "current"
    displayHint = "d-1"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1000, 1000),
    )



# MIB Managed Objects in the order of their OIDs

_Nti_ObjectIdentity = ObjectIdentity
nti = _Nti_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3699)
)
_Products_ObjectIdentity = ObjectIdentity
products = _Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3699, 1)
)
_Hardware_ObjectIdentity = ObjectIdentity
hardware = _Hardware_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3699, 1, 1)
)
_Monitoring_ObjectIdentity = ObjectIdentity
monitoring = _Monitoring_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3699, 1, 1, 3, 1)
)
_TemperatureSensor1_ObjectIdentity = ObjectIdentity
temperatureSensor1 = _TemperatureSensor1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3699, 1, 1, 3, 1, 1)
)
_TemperatureSensor1CurrentValue_Type = DecimalPointValue
_TemperatureSensor1CurrentValue_Object = MibScalar
temperatureSensor1CurrentValue = _TemperatureSensor1CurrentValue_Object(
    (1, 3, 6, 1, 4, 1, 3699, 1, 1, 3, 1, 1, 1),
    _TemperatureSensor1CurrentValue_Type()
)
temperatureSensor1CurrentValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureSensor1CurrentValue.setStatus("current")


class _TemperatureSensor1Alert_Type(Integer32):
    """Custom type temperatureSensor1Alert based on Integer32"""
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


_TemperatureSensor1Alert_Type.__name__ = "Integer32"
_TemperatureSensor1Alert_Object = MibScalar
temperatureSensor1Alert = _TemperatureSensor1Alert_Object(
    (1, 3, 6, 1, 4, 1, 3699, 1, 1, 3, 1, 1, 2),
    _TemperatureSensor1Alert_Type()
)
temperatureSensor1Alert.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureSensor1Alert.setStatus("current")
_TemperatureSensor2_ObjectIdentity = ObjectIdentity
temperatureSensor2 = _TemperatureSensor2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3699, 1, 1, 3, 1, 2)
)
_TemperatureSensor2CurrentValue_Type = DecimalPointValue
_TemperatureSensor2CurrentValue_Object = MibScalar
temperatureSensor2CurrentValue = _TemperatureSensor2CurrentValue_Object(
    (1, 3, 6, 1, 4, 1, 3699, 1, 1, 3, 1, 2, 1),
    _TemperatureSensor2CurrentValue_Type()
)
temperatureSensor2CurrentValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureSensor2CurrentValue.setStatus("current")


class _TemperatureSensor2Alert_Type(Integer32):
    """Custom type temperatureSensor2Alert based on Integer32"""
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


_TemperatureSensor2Alert_Type.__name__ = "Integer32"
_TemperatureSensor2Alert_Object = MibScalar
temperatureSensor2Alert = _TemperatureSensor2Alert_Object(
    (1, 3, 6, 1, 4, 1, 3699, 1, 1, 3, 1, 2, 2),
    _TemperatureSensor2Alert_Type()
)
temperatureSensor2Alert.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperatureSensor2Alert.setStatus("current")
_HumiditySensor1_ObjectIdentity = ObjectIdentity
humiditySensor1 = _HumiditySensor1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3699, 1, 1, 3, 1, 3)
)
_HumiditySensor1CurrentValue_Type = DecimalPointValue
_HumiditySensor1CurrentValue_Object = MibScalar
humiditySensor1CurrentValue = _HumiditySensor1CurrentValue_Object(
    (1, 3, 6, 1, 4, 1, 3699, 1, 1, 3, 1, 3, 1),
    _HumiditySensor1CurrentValue_Type()
)
humiditySensor1CurrentValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    humiditySensor1CurrentValue.setStatus("current")


class _HumiditySensor1Alert_Type(Integer32):
    """Custom type humiditySensor1Alert based on Integer32"""
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


_HumiditySensor1Alert_Type.__name__ = "Integer32"
_HumiditySensor1Alert_Object = MibScalar
humiditySensor1Alert = _HumiditySensor1Alert_Object(
    (1, 3, 6, 1, 4, 1, 3699, 1, 1, 3, 1, 3, 2),
    _HumiditySensor1Alert_Type()
)
humiditySensor1Alert.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    humiditySensor1Alert.setStatus("current")
_HumiditySensor2_ObjectIdentity = ObjectIdentity
humiditySensor2 = _HumiditySensor2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3699, 1, 1, 3, 1, 4)
)
_HumiditySensor2CurrentValue_Type = DecimalPointValue
_HumiditySensor2CurrentValue_Object = MibScalar
humiditySensor2CurrentValue = _HumiditySensor2CurrentValue_Object(
    (1, 3, 6, 1, 4, 1, 3699, 1, 1, 3, 1, 4, 1),
    _HumiditySensor2CurrentValue_Type()
)
humiditySensor2CurrentValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    humiditySensor2CurrentValue.setStatus("current")


class _HumiditySensor2Alert_Type(Integer32):
    """Custom type humiditySensor2Alert based on Integer32"""
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


_HumiditySensor2Alert_Type.__name__ = "Integer32"
_HumiditySensor2Alert_Object = MibScalar
humiditySensor2Alert = _HumiditySensor2Alert_Object(
    (1, 3, 6, 1, 4, 1, 3699, 1, 1, 3, 1, 4, 2),
    _HumiditySensor2Alert_Type()
)
humiditySensor2Alert.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    humiditySensor2Alert.setStatus("current")
_DryContact1_ObjectIdentity = ObjectIdentity
dryContact1 = _DryContact1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3699, 1, 1, 3, 1, 5)
)


class _DryContact1Status_Type(Integer32):
    """Custom type dryContact1Status based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("open", 0),
          ("closed", 1))
    )


_DryContact1Status_Type.__name__ = "Integer32"
_DryContact1Status_Object = MibScalar
dryContact1Status = _DryContact1Status_Object(
    (1, 3, 6, 1, 4, 1, 3699, 1, 1, 3, 1, 5, 1),
    _DryContact1Status_Type()
)
dryContact1Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dryContact1Status.setStatus("current")


class _DryContact1Alert_Type(Integer32):
    """Custom type dryContact1Alert based on Integer32"""
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


_DryContact1Alert_Type.__name__ = "Integer32"
_DryContact1Alert_Object = MibScalar
dryContact1Alert = _DryContact1Alert_Object(
    (1, 3, 6, 1, 4, 1, 3699, 1, 1, 3, 1, 5, 2),
    _DryContact1Alert_Type()
)
dryContact1Alert.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dryContact1Alert.setStatus("current")
_DryContact2_ObjectIdentity = ObjectIdentity
dryContact2 = _DryContact2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3699, 1, 1, 3, 1, 6)
)


class _DryContact2Status_Type(Integer32):
    """Custom type dryContact2Status based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("open", 0),
          ("closed", 1))
    )


_DryContact2Status_Type.__name__ = "Integer32"
_DryContact2Status_Object = MibScalar
dryContact2Status = _DryContact2Status_Object(
    (1, 3, 6, 1, 4, 1, 3699, 1, 1, 3, 1, 6, 1),
    _DryContact2Status_Type()
)
dryContact2Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dryContact2Status.setStatus("current")


class _DryContact2Alert_Type(Integer32):
    """Custom type dryContact2Alert based on Integer32"""
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


_DryContact2Alert_Type.__name__ = "Integer32"
_DryContact2Alert_Object = MibScalar
dryContact2Alert = _DryContact2Alert_Object(
    (1, 3, 6, 1, 4, 1, 3699, 1, 1, 3, 1, 6, 2),
    _DryContact2Alert_Type()
)
dryContact2Alert.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dryContact2Alert.setStatus("current")
_DryContact3_ObjectIdentity = ObjectIdentity
dryContact3 = _DryContact3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3699, 1, 1, 3, 1, 7)
)


class _DryContact3Status_Type(Integer32):
    """Custom type dryContact3Status based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("open", 0),
          ("closed", 1))
    )


_DryContact3Status_Type.__name__ = "Integer32"
_DryContact3Status_Object = MibScalar
dryContact3Status = _DryContact3Status_Object(
    (1, 3, 6, 1, 4, 1, 3699, 1, 1, 3, 1, 7, 1),
    _DryContact3Status_Type()
)
dryContact3Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dryContact3Status.setStatus("current")


class _DryContact3Alert_Type(Integer32):
    """Custom type dryContact3Alert based on Integer32"""
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


_DryContact3Alert_Type.__name__ = "Integer32"
_DryContact3Alert_Object = MibScalar
dryContact3Alert = _DryContact3Alert_Object(
    (1, 3, 6, 1, 4, 1, 3699, 1, 1, 3, 1, 7, 2),
    _DryContact3Alert_Type()
)
dryContact3Alert.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dryContact3Alert.setStatus("current")
_DryContact4_ObjectIdentity = ObjectIdentity
dryContact4 = _DryContact4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3699, 1, 1, 3, 1, 8)
)


class _DryContact4Status_Type(Integer32):
    """Custom type dryContact4Status based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("open", 0),
          ("closed", 1))
    )


_DryContact4Status_Type.__name__ = "Integer32"
_DryContact4Status_Object = MibScalar
dryContact4Status = _DryContact4Status_Object(
    (1, 3, 6, 1, 4, 1, 3699, 1, 1, 3, 1, 8, 1),
    _DryContact4Status_Type()
)
dryContact4Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dryContact4Status.setStatus("current")


class _DryContact4Alert_Type(Integer32):
    """Custom type dryContact4Alert based on Integer32"""
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


_DryContact4Alert_Type.__name__ = "Integer32"
_DryContact4Alert_Object = MibScalar
dryContact4Alert = _DryContact4Alert_Object(
    (1, 3, 6, 1, 4, 1, 3699, 1, 1, 3, 1, 8, 2),
    _DryContact4Alert_Type()
)
dryContact4Alert.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dryContact4Alert.setStatus("current")
_WaterSensor_ObjectIdentity = ObjectIdentity
waterSensor = _WaterSensor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3699, 1, 1, 3, 1, 9)
)


class _WaterStatus_Type(Integer32):
    """Custom type waterStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("open", 0),
          ("closed", 1))
    )


_WaterStatus_Type.__name__ = "Integer32"
_WaterStatus_Object = MibScalar
waterStatus = _WaterStatus_Object(
    (1, 3, 6, 1, 4, 1, 3699, 1, 1, 3, 1, 9, 1),
    _WaterStatus_Type()
)
waterStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    waterStatus.setStatus("current")


class _WaterAlert_Type(Integer32):
    """Custom type waterAlert based on Integer32"""
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


_WaterAlert_Type.__name__ = "Integer32"
_WaterAlert_Object = MibScalar
waterAlert = _WaterAlert_Object(
    (1, 3, 6, 1, 4, 1, 3699, 1, 1, 3, 1, 9, 2),
    _WaterAlert_Type()
)
waterAlert.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    waterAlert.setStatus("current")
_Administration_ObjectIdentity = ObjectIdentity
administration = _Administration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3699, 1, 1, 3, 2)
)
_HostSystem_ObjectIdentity = ObjectIdentity
hostSystem = _HostSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3699, 1, 1, 3, 2, 1)
)
_SysName_Type = DisplayString
_SysName_Object = MibScalar
sysName = _SysName_Object(
    (1, 3, 6, 1, 4, 1, 3699, 1, 1, 3, 2, 1, 1),
    _SysName_Type()
)
sysName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysName.setStatus("current")
_SysLocation_Type = DisplayString
_SysLocation_Object = MibScalar
sysLocation = _SysLocation_Object(
    (1, 3, 6, 1, 4, 1, 3699, 1, 1, 3, 2, 1, 2),
    _SysLocation_Type()
)
sysLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysLocation.setStatus("current")
_SysIP_Type = DisplayString
_SysIP_Object = MibScalar
sysIP = _SysIP_Object(
    (1, 3, 6, 1, 4, 1, 3699, 1, 1, 3, 2, 1, 3),
    _SysIP_Type()
)
sysIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysIP.setStatus("current")
_SysMask_Type = DisplayString
_SysMask_Object = MibScalar
sysMask = _SysMask_Object(
    (1, 3, 6, 1, 4, 1, 3699, 1, 1, 3, 2, 1, 4),
    _SysMask_Type()
)
sysMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysMask.setStatus("current")
_SysGateway_Type = DisplayString
_SysGateway_Object = MibScalar
sysGateway = _SysGateway_Object(
    (1, 3, 6, 1, 4, 1, 3699, 1, 1, 3, 2, 1, 5),
    _SysGateway_Type()
)
sysGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysGateway.setStatus("current")
_SysDNS_Type = DisplayString
_SysDNS_Object = MibScalar
sysDNS = _SysDNS_Object(
    (1, 3, 6, 1, 4, 1, 3699, 1, 1, 3, 2, 1, 6),
    _SysDNS_Type()
)
sysDNS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysDNS.setStatus("current")
_TemperatureSensor1Adm_ObjectIdentity = ObjectIdentity
temperatureSensor1Adm = _TemperatureSensor1Adm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3699, 1, 1, 3, 2, 2)
)
_TemperatureSensor1Name_Type = DisplayString
_TemperatureSensor1Name_Object = MibScalar
temperatureSensor1Name = _TemperatureSensor1Name_Object(
    (1, 3, 6, 1, 4, 1, 3699, 1, 1, 3, 2, 2, 1),
    _TemperatureSensor1Name_Type()
)
temperatureSensor1Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    temperatureSensor1Name.setStatus("current")
_TemperatureSensor1Unit_Type = DisplayString
_TemperatureSensor1Unit_Object = MibScalar
temperatureSensor1Unit = _TemperatureSensor1Unit_Object(
    (1, 3, 6, 1, 4, 1, 3699, 1, 1, 3, 2, 2, 2),
    _TemperatureSensor1Unit_Type()
)
temperatureSensor1Unit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    temperatureSensor1Unit.setStatus("current")
_TemperatureSensor1LowThreshold_Type = DisplayString
_TemperatureSensor1LowThreshold_Object = MibScalar
temperatureSensor1LowThreshold = _TemperatureSensor1LowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3699, 1, 1, 3, 2, 2, 3),
    _TemperatureSensor1LowThreshold_Type()
)
temperatureSensor1LowThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    temperatureSensor1LowThreshold.setStatus("current")
_TemperatureSensor1HighThreshold_Type = DisplayString
_TemperatureSensor1HighThreshold_Object = MibScalar
temperatureSensor1HighThreshold = _TemperatureSensor1HighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3699, 1, 1, 3, 2, 2, 4),
    _TemperatureSensor1HighThreshold_Type()
)
temperatureSensor1HighThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    temperatureSensor1HighThreshold.setStatus("current")
_TemperatureSensor2Adm_ObjectIdentity = ObjectIdentity
temperatureSensor2Adm = _TemperatureSensor2Adm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3699, 1, 1, 3, 2, 3)
)
_TemperatureSensor2Name_Type = DisplayString
_TemperatureSensor2Name_Object = MibScalar
temperatureSensor2Name = _TemperatureSensor2Name_Object(
    (1, 3, 6, 1, 4, 1, 3699, 1, 1, 3, 2, 3, 1),
    _TemperatureSensor2Name_Type()
)
temperatureSensor2Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    temperatureSensor2Name.setStatus("current")
_TemperatureSensor2Unit_Type = DisplayString
_TemperatureSensor2Unit_Object = MibScalar
temperatureSensor2Unit = _TemperatureSensor2Unit_Object(
    (1, 3, 6, 1, 4, 1, 3699, 1, 1, 3, 2, 3, 2),
    _TemperatureSensor2Unit_Type()
)
temperatureSensor2Unit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    temperatureSensor2Unit.setStatus("current")
_TemperatureSensor2LowThreshold_Type = DisplayString
_TemperatureSensor2LowThreshold_Object = MibScalar
temperatureSensor2LowThreshold = _TemperatureSensor2LowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3699, 1, 1, 3, 2, 3, 3),
    _TemperatureSensor2LowThreshold_Type()
)
temperatureSensor2LowThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    temperatureSensor2LowThreshold.setStatus("current")
_TemperatureSensor2HighThreshold_Type = DisplayString
_TemperatureSensor2HighThreshold_Object = MibScalar
temperatureSensor2HighThreshold = _TemperatureSensor2HighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3699, 1, 1, 3, 2, 3, 4),
    _TemperatureSensor2HighThreshold_Type()
)
temperatureSensor2HighThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    temperatureSensor2HighThreshold.setStatus("current")
_HumiditySensor1Adm_ObjectIdentity = ObjectIdentity
humiditySensor1Adm = _HumiditySensor1Adm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3699, 1, 1, 3, 2, 4)
)
_HumiditySensor1Name_Type = DisplayString
_HumiditySensor1Name_Object = MibScalar
humiditySensor1Name = _HumiditySensor1Name_Object(
    (1, 3, 6, 1, 4, 1, 3699, 1, 1, 3, 2, 4, 1),
    _HumiditySensor1Name_Type()
)
humiditySensor1Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    humiditySensor1Name.setStatus("current")
_HumiditySensor1LowThreshold_Type = DisplayString
_HumiditySensor1LowThreshold_Object = MibScalar
humiditySensor1LowThreshold = _HumiditySensor1LowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3699, 1, 1, 3, 2, 4, 2),
    _HumiditySensor1LowThreshold_Type()
)
humiditySensor1LowThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    humiditySensor1LowThreshold.setStatus("current")
_HumiditySensor1HighThreshold_Type = DisplayString
_HumiditySensor1HighThreshold_Object = MibScalar
humiditySensor1HighThreshold = _HumiditySensor1HighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3699, 1, 1, 3, 2, 4, 3),
    _HumiditySensor1HighThreshold_Type()
)
humiditySensor1HighThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    humiditySensor1HighThreshold.setStatus("current")
_HumiditySensor2Adm_ObjectIdentity = ObjectIdentity
humiditySensor2Adm = _HumiditySensor2Adm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3699, 1, 1, 3, 2, 5)
)
_HumiditySensor2Name_Type = DisplayString
_HumiditySensor2Name_Object = MibScalar
humiditySensor2Name = _HumiditySensor2Name_Object(
    (1, 3, 6, 1, 4, 1, 3699, 1, 1, 3, 2, 5, 1),
    _HumiditySensor2Name_Type()
)
humiditySensor2Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    humiditySensor2Name.setStatus("current")
_HumiditySensor2LowThreshold_Type = DisplayString
_HumiditySensor2LowThreshold_Object = MibScalar
humiditySensor2LowThreshold = _HumiditySensor2LowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3699, 1, 1, 3, 2, 5, 2),
    _HumiditySensor2LowThreshold_Type()
)
humiditySensor2LowThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    humiditySensor2LowThreshold.setStatus("current")
_HumiditySensor2HighThreshold_Type = DisplayString
_HumiditySensor2HighThreshold_Object = MibScalar
humiditySensor2HighThreshold = _HumiditySensor2HighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3699, 1, 1, 3, 2, 5, 3),
    _HumiditySensor2HighThreshold_Type()
)
humiditySensor2HighThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    humiditySensor2HighThreshold.setStatus("current")
_DryContact1Adm_ObjectIdentity = ObjectIdentity
dryContact1Adm = _DryContact1Adm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3699, 1, 1, 3, 2, 6)
)
_DryContact1Name_Type = DisplayString
_DryContact1Name_Object = MibScalar
dryContact1Name = _DryContact1Name_Object(
    (1, 3, 6, 1, 4, 1, 3699, 1, 1, 3, 2, 6, 1),
    _DryContact1Name_Type()
)
dryContact1Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dryContact1Name.setStatus("current")


class _DryContact1AlertStatus_Type(Integer32):
    """Custom type dryContact1AlertStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("alertWhenOpen", 0),
          ("alertWhenClosed", 1))
    )


_DryContact1AlertStatus_Type.__name__ = "Integer32"
_DryContact1AlertStatus_Object = MibScalar
dryContact1AlertStatus = _DryContact1AlertStatus_Object(
    (1, 3, 6, 1, 4, 1, 3699, 1, 1, 3, 2, 6, 2),
    _DryContact1AlertStatus_Type()
)
dryContact1AlertStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dryContact1AlertStatus.setStatus("current")
_DryContact2Adm_ObjectIdentity = ObjectIdentity
dryContact2Adm = _DryContact2Adm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3699, 1, 1, 3, 2, 7)
)
_DryContact2Name_Type = DisplayString
_DryContact2Name_Object = MibScalar
dryContact2Name = _DryContact2Name_Object(
    (1, 3, 6, 1, 4, 1, 3699, 1, 1, 3, 2, 7, 1),
    _DryContact2Name_Type()
)
dryContact2Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dryContact2Name.setStatus("current")


class _DryContact2AlertStatus_Type(Integer32):
    """Custom type dryContact2AlertStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("alertWhenOpen", 0),
          ("alertWhenClosed", 1))
    )


_DryContact2AlertStatus_Type.__name__ = "Integer32"
_DryContact2AlertStatus_Object = MibScalar
dryContact2AlertStatus = _DryContact2AlertStatus_Object(
    (1, 3, 6, 1, 4, 1, 3699, 1, 1, 3, 2, 7, 2),
    _DryContact2AlertStatus_Type()
)
dryContact2AlertStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dryContact2AlertStatus.setStatus("current")
_DryContact3Adm_ObjectIdentity = ObjectIdentity
dryContact3Adm = _DryContact3Adm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3699, 1, 1, 3, 2, 8)
)
_DryContact3Name_Type = DisplayString
_DryContact3Name_Object = MibScalar
dryContact3Name = _DryContact3Name_Object(
    (1, 3, 6, 1, 4, 1, 3699, 1, 1, 3, 2, 8, 1),
    _DryContact3Name_Type()
)
dryContact3Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dryContact3Name.setStatus("current")


class _DryContact3AlertStatus_Type(Integer32):
    """Custom type dryContact3AlertStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("alertWhenOpen", 0),
          ("alertWhenClosed", 1))
    )


_DryContact3AlertStatus_Type.__name__ = "Integer32"
_DryContact3AlertStatus_Object = MibScalar
dryContact3AlertStatus = _DryContact3AlertStatus_Object(
    (1, 3, 6, 1, 4, 1, 3699, 1, 1, 3, 2, 8, 2),
    _DryContact3AlertStatus_Type()
)
dryContact3AlertStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dryContact3AlertStatus.setStatus("current")
_DryContact4Adm_ObjectIdentity = ObjectIdentity
dryContact4Adm = _DryContact4Adm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3699, 1, 1, 3, 2, 9)
)
_DryContact4Name_Type = DisplayString
_DryContact4Name_Object = MibScalar
dryContact4Name = _DryContact4Name_Object(
    (1, 3, 6, 1, 4, 1, 3699, 1, 1, 3, 2, 9, 1),
    _DryContact4Name_Type()
)
dryContact4Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dryContact4Name.setStatus("current")


class _DryContact4AlertStatus_Type(Integer32):
    """Custom type dryContact4AlertStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("alertWhenOpen", 0),
          ("alertWhenClosed", 1))
    )


_DryContact4AlertStatus_Type.__name__ = "Integer32"
_DryContact4AlertStatus_Object = MibScalar
dryContact4AlertStatus = _DryContact4AlertStatus_Object(
    (1, 3, 6, 1, 4, 1, 3699, 1, 1, 3, 2, 9, 2),
    _DryContact4AlertStatus_Type()
)
dryContact4AlertStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dryContact4AlertStatus.setStatus("current")
_WaterSensorAdm_ObjectIdentity = ObjectIdentity
waterSensorAdm = _WaterSensorAdm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3699, 1, 1, 3, 2, 10)
)
_WaterName_Type = DisplayString
_WaterName_Object = MibScalar
waterName = _WaterName_Object(
    (1, 3, 6, 1, 4, 1, 3699, 1, 1, 3, 2, 10, 1),
    _WaterName_Type()
)
waterName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    waterName.setStatus("current")


class _WaterAlertStatus_Type(Integer32):
    """Custom type waterAlertStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("alertWhenOpen", 0),
          ("alertWhenClosed", 1))
    )


_WaterAlertStatus_Type.__name__ = "Integer32"
_WaterAlertStatus_Object = MibScalar
waterAlertStatus = _WaterAlertStatus_Object(
    (1, 3, 6, 1, 4, 1, 3699, 1, 1, 3, 2, 10, 2),
    _WaterAlertStatus_Type()
)
waterAlertStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    waterAlertStatus.setStatus("current")
_Version_Type = DisplayString
_Version_Object = MibScalar
version = _Version_Object(
    (1, 3, 6, 1, 4, 1, 3699, 1, 1, 3, 3),
    _Version_Type()
)
version.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    version.setStatus("current")
_EnvTraps_ObjectIdentity = ObjectIdentity
envTraps = _EnvTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3699, 1, 1, 3, 100)
)
_EnvGroups_ObjectIdentity = ObjectIdentity
envGroups = _EnvGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3699, 1, 1, 3, 200)
)
_OtherProduct_ObjectIdentity = ObjectIdentity
otherProduct = _OtherProduct_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3699, 1, 1, 200)
)
_Software_ObjectIdentity = ObjectIdentity
software = _Software_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3699, 1, 2)
)

# Managed Objects groups

unitGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3699, 1, 1, 3, 200, 1)
)
unitGroup.setObjects(
      *(("ENVIROMUXMINI-MIB", "version"),
        ("ENVIROMUXMINI-MIB", "temperatureSensor1CurrentValue"),
        ("ENVIROMUXMINI-MIB", "temperatureSensor1Alert"),
        ("ENVIROMUXMINI-MIB", "temperatureSensor1Name"),
        ("ENVIROMUXMINI-MIB", "temperatureSensor1Unit"),
        ("ENVIROMUXMINI-MIB", "temperatureSensor1LowThreshold"),
        ("ENVIROMUXMINI-MIB", "temperatureSensor1HighThreshold"),
        ("ENVIROMUXMINI-MIB", "temperatureSensor2CurrentValue"),
        ("ENVIROMUXMINI-MIB", "temperatureSensor2Alert"),
        ("ENVIROMUXMINI-MIB", "temperatureSensor2Name"),
        ("ENVIROMUXMINI-MIB", "temperatureSensor2Unit"),
        ("ENVIROMUXMINI-MIB", "temperatureSensor2LowThreshold"),
        ("ENVIROMUXMINI-MIB", "temperatureSensor2HighThreshold"),
        ("ENVIROMUXMINI-MIB", "humiditySensor1CurrentValue"),
        ("ENVIROMUXMINI-MIB", "humiditySensor1Alert"),
        ("ENVIROMUXMINI-MIB", "humiditySensor1Name"),
        ("ENVIROMUXMINI-MIB", "humiditySensor1LowThreshold"),
        ("ENVIROMUXMINI-MIB", "humiditySensor1HighThreshold"),
        ("ENVIROMUXMINI-MIB", "humiditySensor2CurrentValue"),
        ("ENVIROMUXMINI-MIB", "humiditySensor2Alert"),
        ("ENVIROMUXMINI-MIB", "humiditySensor2Name"),
        ("ENVIROMUXMINI-MIB", "humiditySensor2LowThreshold"),
        ("ENVIROMUXMINI-MIB", "humiditySensor2HighThreshold"),
        ("ENVIROMUXMINI-MIB", "dryContact1Status"),
        ("ENVIROMUXMINI-MIB", "dryContact1Alert"),
        ("ENVIROMUXMINI-MIB", "dryContact1Name"),
        ("ENVIROMUXMINI-MIB", "dryContact1AlertStatus"),
        ("ENVIROMUXMINI-MIB", "dryContact2Status"),
        ("ENVIROMUXMINI-MIB", "dryContact2Alert"),
        ("ENVIROMUXMINI-MIB", "dryContact2Name"),
        ("ENVIROMUXMINI-MIB", "dryContact2AlertStatus"),
        ("ENVIROMUXMINI-MIB", "dryContact3Status"),
        ("ENVIROMUXMINI-MIB", "dryContact3Alert"),
        ("ENVIROMUXMINI-MIB", "dryContact3Name"),
        ("ENVIROMUXMINI-MIB", "dryContact3AlertStatus"),
        ("ENVIROMUXMINI-MIB", "dryContact4Status"),
        ("ENVIROMUXMINI-MIB", "dryContact4Alert"),
        ("ENVIROMUXMINI-MIB", "dryContact4Name"),
        ("ENVIROMUXMINI-MIB", "dryContact4AlertStatus"),
        ("ENVIROMUXMINI-MIB", "waterStatus"),
        ("ENVIROMUXMINI-MIB", "waterAlert"),
        ("ENVIROMUXMINI-MIB", "waterName"),
        ("ENVIROMUXMINI-MIB", "waterAlertStatus"),
        ("ENVIROMUXMINI-MIB", "sysName"),
        ("ENVIROMUXMINI-MIB", "sysLocation"),
        ("ENVIROMUXMINI-MIB", "sysIP"),
        ("ENVIROMUXMINI-MIB", "sysMask"),
        ("ENVIROMUXMINI-MIB", "sysGateway"),
        ("ENVIROMUXMINI-MIB", "sysDNS"))
)
if mibBuilder.loadTexts:
    unitGroup.setStatus("current")


# Notification objects

temperatureSensor1Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3699, 1, 1, 3, 100, 1)
)
if mibBuilder.loadTexts:
    temperatureSensor1Trap.setStatus(
        "current"
    )

temperatureSensor2Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3699, 1, 1, 3, 100, 2)
)
if mibBuilder.loadTexts:
    temperatureSensor2Trap.setStatus(
        "current"
    )

humiditySensor1Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3699, 1, 1, 3, 100, 3)
)
if mibBuilder.loadTexts:
    humiditySensor1Trap.setStatus(
        "current"
    )

humiditySensor2Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3699, 1, 1, 3, 100, 4)
)
if mibBuilder.loadTexts:
    humiditySensor2Trap.setStatus(
        "current"
    )

dryContactSensor1Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3699, 1, 1, 3, 100, 5)
)
if mibBuilder.loadTexts:
    dryContactSensor1Trap.setStatus(
        "current"
    )

dryContactSensor2Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3699, 1, 1, 3, 100, 6)
)
if mibBuilder.loadTexts:
    dryContactSensor2Trap.setStatus(
        "current"
    )

dryContactSensor3Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3699, 1, 1, 3, 100, 7)
)
if mibBuilder.loadTexts:
    dryContactSensor3Trap.setStatus(
        "current"
    )

dryContactSensor4Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3699, 1, 1, 3, 100, 8)
)
if mibBuilder.loadTexts:
    dryContactSensor4Trap.setStatus(
        "current"
    )

waterSensor1Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3699, 1, 1, 3, 100, 9)
)
if mibBuilder.loadTexts:
    waterSensor1Trap.setStatus(
        "current"
    )

temperatureSensor1RetTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3699, 1, 1, 3, 100, 11)
)
if mibBuilder.loadTexts:
    temperatureSensor1RetTrap.setStatus(
        "current"
    )

temperatureSensor2RetTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3699, 1, 1, 3, 100, 12)
)
if mibBuilder.loadTexts:
    temperatureSensor2RetTrap.setStatus(
        "current"
    )

humiditySensor1RetTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3699, 1, 1, 3, 100, 13)
)
if mibBuilder.loadTexts:
    humiditySensor1RetTrap.setStatus(
        "current"
    )

humiditySensor2RetTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3699, 1, 1, 3, 100, 14)
)
if mibBuilder.loadTexts:
    humiditySensor2RetTrap.setStatus(
        "current"
    )

dryContactSensor1RetTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3699, 1, 1, 3, 100, 15)
)
if mibBuilder.loadTexts:
    dryContactSensor1RetTrap.setStatus(
        "current"
    )

dryContactSensor2RetTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3699, 1, 1, 3, 100, 16)
)
if mibBuilder.loadTexts:
    dryContactSensor2RetTrap.setStatus(
        "current"
    )

dryContactSensor3RetTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3699, 1, 1, 3, 100, 17)
)
if mibBuilder.loadTexts:
    dryContactSensor3RetTrap.setStatus(
        "current"
    )

dryContactSensor4RetTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3699, 1, 1, 3, 100, 18)
)
if mibBuilder.loadTexts:
    dryContactSensor4RetTrap.setStatus(
        "current"
    )

waterSensor1RetTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3699, 1, 1, 3, 100, 19)
)
if mibBuilder.loadTexts:
    waterSensor1RetTrap.setStatus(
        "current"
    )

logTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3699, 1, 1, 3, 100, 100)
)
if mibBuilder.loadTexts:
    logTrap.setStatus(
        "current"
    )

overflowTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3699, 1, 1, 3, 100, 101)
)
if mibBuilder.loadTexts:
    overflowTrap.setStatus(
        "current"
    )


# Notifications groups

envTrapsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 3699, 1, 1, 3, 200, 2)
)
envTrapsGroup.setObjects(
      *(("ENVIROMUXMINI-MIB", "temperatureSensor1Trap"),
        ("ENVIROMUXMINI-MIB", "temperatureSensor2Trap"),
        ("ENVIROMUXMINI-MIB", "humiditySensor1Trap"),
        ("ENVIROMUXMINI-MIB", "humiditySensor2Trap"),
        ("ENVIROMUXMINI-MIB", "dryContactSensor1Trap"),
        ("ENVIROMUXMINI-MIB", "dryContactSensor2Trap"),
        ("ENVIROMUXMINI-MIB", "dryContactSensor3Trap"),
        ("ENVIROMUXMINI-MIB", "dryContactSensor4Trap"),
        ("ENVIROMUXMINI-MIB", "waterSensor1Trap"),
        ("ENVIROMUXMINI-MIB", "logTrap"),
        ("ENVIROMUXMINI-MIB", "overflowTrap"))
)
if mibBuilder.loadTexts:
    envTrapsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ENVIROMUXMINI-MIB",
    **{"DecimalPointValue": DecimalPointValue,
       "nti": nti,
       "products": products,
       "hardware": hardware,
       "enviromuxMini": enviromuxMini,
       "monitoring": monitoring,
       "temperatureSensor1": temperatureSensor1,
       "temperatureSensor1CurrentValue": temperatureSensor1CurrentValue,
       "temperatureSensor1Alert": temperatureSensor1Alert,
       "temperatureSensor2": temperatureSensor2,
       "temperatureSensor2CurrentValue": temperatureSensor2CurrentValue,
       "temperatureSensor2Alert": temperatureSensor2Alert,
       "humiditySensor1": humiditySensor1,
       "humiditySensor1CurrentValue": humiditySensor1CurrentValue,
       "humiditySensor1Alert": humiditySensor1Alert,
       "humiditySensor2": humiditySensor2,
       "humiditySensor2CurrentValue": humiditySensor2CurrentValue,
       "humiditySensor2Alert": humiditySensor2Alert,
       "dryContact1": dryContact1,
       "dryContact1Status": dryContact1Status,
       "dryContact1Alert": dryContact1Alert,
       "dryContact2": dryContact2,
       "dryContact2Status": dryContact2Status,
       "dryContact2Alert": dryContact2Alert,
       "dryContact3": dryContact3,
       "dryContact3Status": dryContact3Status,
       "dryContact3Alert": dryContact3Alert,
       "dryContact4": dryContact4,
       "dryContact4Status": dryContact4Status,
       "dryContact4Alert": dryContact4Alert,
       "waterSensor": waterSensor,
       "waterStatus": waterStatus,
       "waterAlert": waterAlert,
       "administration": administration,
       "hostSystem": hostSystem,
       "sysName": sysName,
       "sysLocation": sysLocation,
       "sysIP": sysIP,
       "sysMask": sysMask,
       "sysGateway": sysGateway,
       "sysDNS": sysDNS,
       "temperatureSensor1Adm": temperatureSensor1Adm,
       "temperatureSensor1Name": temperatureSensor1Name,
       "temperatureSensor1Unit": temperatureSensor1Unit,
       "temperatureSensor1LowThreshold": temperatureSensor1LowThreshold,
       "temperatureSensor1HighThreshold": temperatureSensor1HighThreshold,
       "temperatureSensor2Adm": temperatureSensor2Adm,
       "temperatureSensor2Name": temperatureSensor2Name,
       "temperatureSensor2Unit": temperatureSensor2Unit,
       "temperatureSensor2LowThreshold": temperatureSensor2LowThreshold,
       "temperatureSensor2HighThreshold": temperatureSensor2HighThreshold,
       "humiditySensor1Adm": humiditySensor1Adm,
       "humiditySensor1Name": humiditySensor1Name,
       "humiditySensor1LowThreshold": humiditySensor1LowThreshold,
       "humiditySensor1HighThreshold": humiditySensor1HighThreshold,
       "humiditySensor2Adm": humiditySensor2Adm,
       "humiditySensor2Name": humiditySensor2Name,
       "humiditySensor2LowThreshold": humiditySensor2LowThreshold,
       "humiditySensor2HighThreshold": humiditySensor2HighThreshold,
       "dryContact1Adm": dryContact1Adm,
       "dryContact1Name": dryContact1Name,
       "dryContact1AlertStatus": dryContact1AlertStatus,
       "dryContact2Adm": dryContact2Adm,
       "dryContact2Name": dryContact2Name,
       "dryContact2AlertStatus": dryContact2AlertStatus,
       "dryContact3Adm": dryContact3Adm,
       "dryContact3Name": dryContact3Name,
       "dryContact3AlertStatus": dryContact3AlertStatus,
       "dryContact4Adm": dryContact4Adm,
       "dryContact4Name": dryContact4Name,
       "dryContact4AlertStatus": dryContact4AlertStatus,
       "waterSensorAdm": waterSensorAdm,
       "waterName": waterName,
       "waterAlertStatus": waterAlertStatus,
       "version": version,
       "envTraps": envTraps,
       "temperatureSensor1Trap": temperatureSensor1Trap,
       "temperatureSensor2Trap": temperatureSensor2Trap,
       "humiditySensor1Trap": humiditySensor1Trap,
       "humiditySensor2Trap": humiditySensor2Trap,
       "dryContactSensor1Trap": dryContactSensor1Trap,
       "dryContactSensor2Trap": dryContactSensor2Trap,
       "dryContactSensor3Trap": dryContactSensor3Trap,
       "dryContactSensor4Trap": dryContactSensor4Trap,
       "waterSensor1Trap": waterSensor1Trap,
       "temperatureSensor1RetTrap": temperatureSensor1RetTrap,
       "temperatureSensor2RetTrap": temperatureSensor2RetTrap,
       "humiditySensor1RetTrap": humiditySensor1RetTrap,
       "humiditySensor2RetTrap": humiditySensor2RetTrap,
       "dryContactSensor1RetTrap": dryContactSensor1RetTrap,
       "dryContactSensor2RetTrap": dryContactSensor2RetTrap,
       "dryContactSensor3RetTrap": dryContactSensor3RetTrap,
       "dryContactSensor4RetTrap": dryContactSensor4RetTrap,
       "waterSensor1RetTrap": waterSensor1RetTrap,
       "logTrap": logTrap,
       "overflowTrap": overflowTrap,
       "envGroups": envGroups,
       "unitGroup": unitGroup,
       "envTrapsGroup": envTrapsGroup,
       "otherProduct": otherProduct,
       "software": software}
)
