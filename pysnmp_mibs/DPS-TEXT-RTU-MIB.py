# SNMP MIB module (DPS-TEXT-RTU-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/dps/DPS-TEXT-RTU-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:10:57 2025
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

(dpsAlarmControl,) = mibBuilder.importSymbols(
    "DPS-MIB-V38",
    "dpsAlarmControl")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



class AnalogThresholds(TextualConvention, Integer32):
    status = "current"
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
        *(("noAlarms", 0),
          ("minorUnder", 1),
          ("minorOver", 2),
          ("majorUnder", 3),
          ("majorOver", 4),
          ("notDetected", 5))
    )



class RTUCAction(TextualConvention, Integer32):
    status = "current"
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
        *(("latch", 1),
          ("release", 2),
          ("momentary", 3),
          ("syncStanding", 4),
          ("syncAnalogs", 5))
    )



# MIB Managed Objects in the order of their OIDs

_DpsTEXTRTUv2_ObjectIdentity = ObjectIdentity
dpsTEXTRTUv2 = _DpsTEXTRTUv2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2682, 1, 5)
)
_DpsTEXTRTUv2Ident_ObjectIdentity = ObjectIdentity
dpsTEXTRTUv2Ident = _DpsTEXTRTUv2Ident_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2682, 1, 5, 1)
)
_DpsTEXTRTUv2DateTime_Type = DisplayString
_DpsTEXTRTUv2DateTime_Object = MibScalar
dpsTEXTRTUv2DateTime = _DpsTEXTRTUv2DateTime_Object(
    (1, 3, 6, 1, 4, 1, 2682, 1, 5, 1, 1),
    _DpsTEXTRTUv2DateTime_Type()
)
dpsTEXTRTUv2DateTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpsTEXTRTUv2DateTime.setStatus("current")
_DpsTEXTRTUv2DeviceType_Type = DisplayString
_DpsTEXTRTUv2DeviceType_Object = MibScalar
dpsTEXTRTUv2DeviceType = _DpsTEXTRTUv2DeviceType_Object(
    (1, 3, 6, 1, 4, 1, 2682, 1, 5, 1, 2),
    _DpsTEXTRTUv2DeviceType_Type()
)
dpsTEXTRTUv2DeviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpsTEXTRTUv2DeviceType.setStatus("current")
_DpsTEXTRTUv2Phone_Type = DisplayString
_DpsTEXTRTUv2Phone_Object = MibScalar
dpsTEXTRTUv2Phone = _DpsTEXTRTUv2Phone_Object(
    (1, 3, 6, 1, 4, 1, 2682, 1, 5, 1, 3),
    _DpsTEXTRTUv2Phone_Type()
)
dpsTEXTRTUv2Phone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpsTEXTRTUv2Phone.setStatus("current")
_DpsTEXTRTUv2AlarmGrid_ObjectIdentity = ObjectIdentity
dpsTEXTRTUv2AlarmGrid = _DpsTEXTRTUv2AlarmGrid_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2682, 1, 5, 2)
)
_DpsTEXTRTUv2ADisplay_Type = Integer32
_DpsTEXTRTUv2ADisplay_Object = MibScalar
dpsTEXTRTUv2ADisplay = _DpsTEXTRTUv2ADisplay_Object(
    (1, 3, 6, 1, 4, 1, 2682, 1, 5, 2, 1),
    _DpsTEXTRTUv2ADisplay_Type()
)
dpsTEXTRTUv2ADisplay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpsTEXTRTUv2ADisplay.setStatus("current")
_DpsTEXTRTUv2APoint_Type = Integer32
_DpsTEXTRTUv2APoint_Object = MibScalar
dpsTEXTRTUv2APoint = _DpsTEXTRTUv2APoint_Object(
    (1, 3, 6, 1, 4, 1, 2682, 1, 5, 2, 2),
    _DpsTEXTRTUv2APoint_Type()
)
dpsTEXTRTUv2APoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpsTEXTRTUv2APoint.setStatus("current")
_DpsTEXTRTUv2APntDesc_Type = DisplayString
_DpsTEXTRTUv2APntDesc_Object = MibScalar
dpsTEXTRTUv2APntDesc = _DpsTEXTRTUv2APntDesc_Object(
    (1, 3, 6, 1, 4, 1, 2682, 1, 5, 2, 3),
    _DpsTEXTRTUv2APntDesc_Type()
)
dpsTEXTRTUv2APntDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpsTEXTRTUv2APntDesc.setStatus("current")
_DpsTEXTRTUv2AState_Type = DisplayString
_DpsTEXTRTUv2AState_Object = MibScalar
dpsTEXTRTUv2AState = _DpsTEXTRTUv2AState_Object(
    (1, 3, 6, 1, 4, 1, 2682, 1, 5, 2, 4),
    _DpsTEXTRTUv2AState_Type()
)
dpsTEXTRTUv2AState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpsTEXTRTUv2AState.setStatus("current")
_DpsTEXTRTUAnalogvalue_Type = DisplayString
_DpsTEXTRTUAnalogvalue_Object = MibScalar
dpsTEXTRTUAnalogvalue = _DpsTEXTRTUAnalogvalue_Object(
    (1, 3, 6, 1, 4, 1, 2682, 1, 5, 2, 5),
    _DpsTEXTRTUAnalogvalue_Type()
)
dpsTEXTRTUAnalogvalue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpsTEXTRTUAnalogvalue.setStatus("current")
_DpsTEXTRTUAnalogthresholds_Type = AnalogThresholds
_DpsTEXTRTUAnalogthresholds_Object = MibScalar
dpsTEXTRTUAnalogthresholds = _DpsTEXTRTUAnalogthresholds_Object(
    (1, 3, 6, 1, 4, 1, 2682, 1, 5, 2, 6),
    _DpsTEXTRTUAnalogthresholds_Type()
)
dpsTEXTRTUAnalogthresholds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpsTEXTRTUAnalogthresholds.setStatus("current")
_DpsTEXTRTUv2ControlGrid_ObjectIdentity = ObjectIdentity
dpsTEXTRTUv2ControlGrid = _DpsTEXTRTUv2ControlGrid_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2682, 1, 5, 3)
)
_DpsTEXTRTUv2CDisplay_Type = Integer32
_DpsTEXTRTUv2CDisplay_Object = MibScalar
dpsTEXTRTUv2CDisplay = _DpsTEXTRTUv2CDisplay_Object(
    (1, 3, 6, 1, 4, 1, 2682, 1, 5, 3, 1),
    _DpsTEXTRTUv2CDisplay_Type()
)
dpsTEXTRTUv2CDisplay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpsTEXTRTUv2CDisplay.setStatus("current")


class _DpsTEXTRTUv2CPoint_Type(Integer32):
    """Custom type dpsTEXTRTUv2CPoint based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_DpsTEXTRTUv2CPoint_Type.__name__ = "Integer32"
_DpsTEXTRTUv2CPoint_Object = MibScalar
dpsTEXTRTUv2CPoint = _DpsTEXTRTUv2CPoint_Object(
    (1, 3, 6, 1, 4, 1, 2682, 1, 5, 3, 2),
    _DpsTEXTRTUv2CPoint_Type()
)
dpsTEXTRTUv2CPoint.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpsTEXTRTUv2CPoint.setStatus("current")
_DpsTEXTRTUv2CMOMTime_Type = Integer32
_DpsTEXTRTUv2CMOMTime_Object = MibScalar
dpsTEXTRTUv2CMOMTime = _DpsTEXTRTUv2CMOMTime_Object(
    (1, 3, 6, 1, 4, 1, 2682, 1, 5, 3, 3),
    _DpsTEXTRTUv2CMOMTime_Type()
)
dpsTEXTRTUv2CMOMTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpsTEXTRTUv2CMOMTime.setStatus("current")
_DpsTEXTRTUv2CAction_Type = RTUCAction
_DpsTEXTRTUv2CAction_Object = MibScalar
dpsTEXTRTUv2CAction = _DpsTEXTRTUv2CAction_Object(
    (1, 3, 6, 1, 4, 1, 2682, 1, 5, 3, 4),
    _DpsTEXTRTUv2CAction_Type()
)
dpsTEXTRTUv2CAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpsTEXTRTUv2CAction.setStatus("current")

# Managed Objects groups


# Notification objects

dpsTEXTRTUv2AlarmSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 5, 100)
)
dpsTEXTRTUv2AlarmSet.setObjects(
      *(("DPS-TEXT-RTU-MIB", "sysDescr"),
        ("DPS-TEXT-RTU-MIB", "sysLocation"),
        ("DPS-TEXT-RTU-MIB", "dpsTEXTRTUv2DateTime"),
        ("DPS-TEXT-RTU-MIB", "dpsTEXTRTUv2DeviceType"),
        ("DPS-TEXT-RTU-MIB", "dpsTEXTRTUv2Phone"),
        ("DPS-TEXT-RTU-MIB", "dpsTEXTRTUv2ADisplay"),
        ("DPS-TEXT-RTU-MIB", "dpsTEXTRTUv2APoint"),
        ("DPS-TEXT-RTU-MIB", "dpsTEXTRTUv2APntDesc"),
        ("DPS-TEXT-RTU-MIB", "dpsTEXTRTUv2AState"),
        ("DPS-TEXT-RTU-MIB", "dpsTEXTRTUAnalogvalue"))
)
if mibBuilder.loadTexts:
    dpsTEXTRTUv2AlarmSet.setStatus(
        "current"
    )

dpsTEXTRTUv2AlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 5, 200)
)
dpsTEXTRTUv2AlarmClear.setObjects(
      *(("DPS-TEXT-RTU-MIB", "sysDescr"),
        ("DPS-TEXT-RTU-MIB", "sysLocation"),
        ("DPS-TEXT-RTU-MIB", "dpsTEXTRTUv2DateTime"),
        ("DPS-TEXT-RTU-MIB", "dpsTEXTRTUv2DeviceType"),
        ("DPS-TEXT-RTU-MIB", "dpsTEXTRTUv2Phone"),
        ("DPS-TEXT-RTU-MIB", "dpsTEXTRTUv2ADisplay"),
        ("DPS-TEXT-RTU-MIB", "dpsTEXTRTUv2APoint"),
        ("DPS-TEXT-RTU-MIB", "dpsTEXTRTUv2APntDesc"),
        ("DPS-TEXT-RTU-MIB", "dpsTEXTRTUv2AState"),
        ("DPS-TEXT-RTU-MIB", "dpsTEXTRTUAnalogvalue"))
)
if mibBuilder.loadTexts:
    dpsTEXTRTUv2AlarmClear.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DPS-TEXT-RTU-MIB",
    **{"AnalogThresholds": AnalogThresholds,
       "RTUCAction": RTUCAction,
       "dpsTEXTRTUv2": dpsTEXTRTUv2,
       "dpsTEXTRTUv2Ident": dpsTEXTRTUv2Ident,
       "dpsTEXTRTUv2DateTime": dpsTEXTRTUv2DateTime,
       "dpsTEXTRTUv2DeviceType": dpsTEXTRTUv2DeviceType,
       "dpsTEXTRTUv2Phone": dpsTEXTRTUv2Phone,
       "dpsTEXTRTUv2AlarmGrid": dpsTEXTRTUv2AlarmGrid,
       "dpsTEXTRTUv2ADisplay": dpsTEXTRTUv2ADisplay,
       "dpsTEXTRTUv2APoint": dpsTEXTRTUv2APoint,
       "dpsTEXTRTUv2APntDesc": dpsTEXTRTUv2APntDesc,
       "dpsTEXTRTUv2AState": dpsTEXTRTUv2AState,
       "dpsTEXTRTUAnalogvalue": dpsTEXTRTUAnalogvalue,
       "dpsTEXTRTUAnalogthresholds": dpsTEXTRTUAnalogthresholds,
       "dpsTEXTRTUv2ControlGrid": dpsTEXTRTUv2ControlGrid,
       "dpsTEXTRTUv2CDisplay": dpsTEXTRTUv2CDisplay,
       "dpsTEXTRTUv2CPoint": dpsTEXTRTUv2CPoint,
       "dpsTEXTRTUv2CMOMTime": dpsTEXTRTUv2CMOMTime,
       "dpsTEXTRTUv2CAction": dpsTEXTRTUv2CAction,
       "dpsTEXTRTUv2AlarmSet": dpsTEXTRTUv2AlarmSet,
       "dpsTEXTRTUv2AlarmClear": dpsTEXTRTUv2AlarmClear}
)
