# SNMP MIB module (RUGGEDCOM-IRIGB-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/siemens/RUGGEDCOM-IRIGB-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:06:44 2025
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

(ruggedcomMgmt,
 ruggedcomTraps) = mibBuilder.importSymbols(
    "RUGGEDCOM-MIB",
    "ruggedcomMgmt",
    "ruggedcomTraps")

(RcTimeSyncStatus,) = mibBuilder.importSymbols(
    "RUGGEDCOM-TIMECONFIG-MIB",
    "RcTimeSyncStatus")

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

rcIrigb = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 15004, 4, 10)
)
if mibBuilder.loadTexts:
    rcIrigb.setRevisions(
        ("2015-10-30 17:00",
         "2014-12-01 17:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class RcTimeStamp(TextualConvention, OctetString):
    status = "current"
    displayHint = "4d.4d"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8



# MIB Managed Objects in the order of their OIDs

_RcIrigbBase_ObjectIdentity = ObjectIdentity
rcIrigbBase = _RcIrigbBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15004, 4, 10, 1)
)
_RcIrigbStatus_Type = RcTimeSyncStatus
_RcIrigbStatus_Object = MibScalar
rcIrigbStatus = _RcIrigbStatus_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 10, 1, 1),
    _RcIrigbStatus_Type()
)
rcIrigbStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcIrigbStatus.setStatus("current")


class _RcIrigbAMOutput_Type(Integer32):
    """Custom type rcIrigbAMOutput based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              4)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("am", 4))
    )


_RcIrigbAMOutput_Type.__name__ = "Integer32"
_RcIrigbAMOutput_Object = MibScalar
rcIrigbAMOutput = _RcIrigbAMOutput_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 10, 1, 2),
    _RcIrigbAMOutput_Type()
)
rcIrigbAMOutput.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcIrigbAMOutput.setStatus("current")


class _RcIrigbTimeCode_Type(Integer32):
    """Custom type rcIrigbTimeCode based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("bxx0", 1),
          ("bxx1", 2),
          ("bxx2", 3),
          ("bxx3", 4),
          ("bxx4", 5),
          ("bxx5", 6),
          ("bxx6", 7),
          ("bxx7", 8))
    )


_RcIrigbTimeCode_Type.__name__ = "Integer32"
_RcIrigbTimeCode_Object = MibScalar
rcIrigbTimeCode = _RcIrigbTimeCode_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 10, 1, 3),
    _RcIrigbTimeCode_Type()
)
rcIrigbTimeCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcIrigbTimeCode.setStatus("current")


class _RcIrigbExt_Type(Integer32):
    """Custom type rcIrigbExt based on Integer32"""
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
        *(("off", 1),
          ("ieee1344", 2),
          ("c37-118-2005", 3),
          ("c37-118-2011", 4))
    )


_RcIrigbExt_Type.__name__ = "Integer32"
_RcIrigbExt_Object = MibScalar
rcIrigbExt = _RcIrigbExt_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 10, 1, 4),
    _RcIrigbExt_Type()
)
rcIrigbExt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcIrigbExt.setStatus("current")


class _RcIrigbInput_Type(Integer32):
    """Custom type rcIrigbInput based on Integer32"""
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
        *(("off", 1),
          ("pwm", 2),
          ("pps", 3),
          ("am", 4))
    )


_RcIrigbInput_Type.__name__ = "Integer32"
_RcIrigbInput_Object = MibScalar
rcIrigbInput = _RcIrigbInput_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 10, 1, 5),
    _RcIrigbInput_Type()
)
rcIrigbInput.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcIrigbInput.setStatus("current")


class _RcIrigbLockInt_Type(Integer32):
    """Custom type rcIrigbLockInt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 120),
    )


_RcIrigbLockInt_Type.__name__ = "Integer32"
_RcIrigbLockInt_Object = MibScalar
rcIrigbLockInt = _RcIrigbLockInt_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 10, 1, 6),
    _RcIrigbLockInt_Type()
)
rcIrigbLockInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcIrigbLockInt.setStatus("current")


class _RcIrigbCableComp_Type(Integer32):
    """Custom type rcIrigbCableComp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50000),
    )


_RcIrigbCableComp_Type.__name__ = "Integer32"
_RcIrigbCableComp_Object = MibScalar
rcIrigbCableComp = _RcIrigbCableComp_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 10, 1, 7),
    _RcIrigbCableComp_Type()
)
rcIrigbCableComp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcIrigbCableComp.setStatus("current")


class _RcIrigbOFM_Type(Integer32):
    """Custom type rcIrigbOFM based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483647, 2147483647),
    )


_RcIrigbOFM_Type.__name__ = "Integer32"
_RcIrigbOFM_Object = MibScalar
rcIrigbOFM = _RcIrigbOFM_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 10, 1, 8),
    _RcIrigbOFM_Type()
)
rcIrigbOFM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcIrigbOFM.setStatus("current")


class _RcIrigbFreqAdj_Type(Integer32):
    """Custom type rcIrigbFreqAdj based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483647, 2147483647),
    )


_RcIrigbFreqAdj_Type.__name__ = "Integer32"
_RcIrigbFreqAdj_Object = MibScalar
rcIrigbFreqAdj = _RcIrigbFreqAdj_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 10, 1, 9),
    _RcIrigbFreqAdj_Type()
)
rcIrigbFreqAdj.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcIrigbFreqAdj.setStatus("current")


class _RcIrigbOutputPWM1_Type(Integer32):
    """Custom type rcIrigbOutputPWM1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              5)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("pwm", 2),
          ("pps", 3),
          ("ppx", 5))
    )


_RcIrigbOutputPWM1_Type.__name__ = "Integer32"
_RcIrigbOutputPWM1_Object = MibScalar
rcIrigbOutputPWM1 = _RcIrigbOutputPWM1_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 10, 1, 10),
    _RcIrigbOutputPWM1_Type()
)
rcIrigbOutputPWM1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcIrigbOutputPWM1.setStatus("current")


class _RcIrigbPulseInterval1_Type(Integer32):
    """Custom type rcIrigbPulseInterval1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 86400),
    )


_RcIrigbPulseInterval1_Type.__name__ = "Integer32"
_RcIrigbPulseInterval1_Object = MibScalar
rcIrigbPulseInterval1 = _RcIrigbPulseInterval1_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 10, 1, 11),
    _RcIrigbPulseInterval1_Type()
)
rcIrigbPulseInterval1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcIrigbPulseInterval1.setStatus("current")


class _RcIrigbPulseWidth1_Type(Integer32):
    """Custom type rcIrigbPulseWidth1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200),
    )


_RcIrigbPulseWidth1_Type.__name__ = "Integer32"
_RcIrigbPulseWidth1_Object = MibScalar
rcIrigbPulseWidth1 = _RcIrigbPulseWidth1_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 10, 1, 12),
    _RcIrigbPulseWidth1_Type()
)
rcIrigbPulseWidth1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcIrigbPulseWidth1.setStatus("current")
_RcIrigbStartTime1_Type = RcTimeStamp
_RcIrigbStartTime1_Object = MibScalar
rcIrigbStartTime1 = _RcIrigbStartTime1_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 10, 1, 13),
    _RcIrigbStartTime1_Type()
)
rcIrigbStartTime1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcIrigbStartTime1.setStatus("current")


class _RcIrigbOutputPWM2_Type(Integer32):
    """Custom type rcIrigbOutputPWM2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              5)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("pwm", 2),
          ("pps", 3),
          ("ppx", 5))
    )


_RcIrigbOutputPWM2_Type.__name__ = "Integer32"
_RcIrigbOutputPWM2_Object = MibScalar
rcIrigbOutputPWM2 = _RcIrigbOutputPWM2_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 10, 1, 14),
    _RcIrigbOutputPWM2_Type()
)
rcIrigbOutputPWM2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcIrigbOutputPWM2.setStatus("current")


class _RcIrigbPulseInterval2_Type(Integer32):
    """Custom type rcIrigbPulseInterval2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 86400),
    )


_RcIrigbPulseInterval2_Type.__name__ = "Integer32"
_RcIrigbPulseInterval2_Object = MibScalar
rcIrigbPulseInterval2 = _RcIrigbPulseInterval2_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 10, 1, 15),
    _RcIrigbPulseInterval2_Type()
)
rcIrigbPulseInterval2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcIrigbPulseInterval2.setStatus("current")


class _RcIrigbPulseWidth2_Type(Integer32):
    """Custom type rcIrigbPulseWidth2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200),
    )


_RcIrigbPulseWidth2_Type.__name__ = "Integer32"
_RcIrigbPulseWidth2_Object = MibScalar
rcIrigbPulseWidth2 = _RcIrigbPulseWidth2_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 10, 1, 16),
    _RcIrigbPulseWidth2_Type()
)
rcIrigbPulseWidth2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcIrigbPulseWidth2.setStatus("current")
_RcIrigbStartTime2_Type = RcTimeStamp
_RcIrigbStartTime2_Object = MibScalar
rcIrigbStartTime2 = _RcIrigbStartTime2_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 10, 1, 17),
    _RcIrigbStartTime2_Type()
)
rcIrigbStartTime2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcIrigbStartTime2.setStatus("current")
_RcIrigbConformance_ObjectIdentity = ObjectIdentity
rcIrigbConformance = _RcIrigbConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15004, 4, 10, 2)
)
_RcIrigbGroups_ObjectIdentity = ObjectIdentity
rcIrigbGroups = _RcIrigbGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15004, 4, 10, 2, 2)
)

# Managed Objects groups

rcIrigbBaseGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 15004, 4, 10, 2, 2, 1)
)
rcIrigbBaseGroup.setObjects(
    ("RUGGEDCOM-IRIGB-MIB", "rcIrigbStatus")
)
if mibBuilder.loadTexts:
    rcIrigbBaseGroup.setStatus("current")

rcIrigbNotifyGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 15004, 4, 10, 2, 2, 2)
)
rcIrigbNotifyGroup.setObjects(
    ("RUGGEDCOM-IRIGB-MIB", "rcIrigbStatusChange")
)
if mibBuilder.loadTexts:
    rcIrigbNotifyGroup.setStatus("current")

rcIrigbCommonGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 15004, 4, 10, 2, 2, 3)
)
rcIrigbCommonGroup.setObjects(
      *(("RUGGEDCOM-IRIGB-MIB", "rcIrigbStatus"),
        ("RUGGEDCOM-IRIGB-MIB", "rcIrigbTimeCode"),
        ("RUGGEDCOM-IRIGB-MIB", "rcIrigbExt"),
        ("RUGGEDCOM-IRIGB-MIB", "rcIrigbLockInt"),
        ("RUGGEDCOM-IRIGB-MIB", "rcIrigbCableComp"),
        ("RUGGEDCOM-IRIGB-MIB", "rcIrigbOFM"),
        ("RUGGEDCOM-IRIGB-MIB", "rcIrigbFreqAdj"))
)
if mibBuilder.loadTexts:
    rcIrigbCommonGroup.setStatus("current")

rcIrigbAMOutGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 15004, 4, 10, 2, 2, 4)
)
rcIrigbAMOutGroup.setObjects(
    ("RUGGEDCOM-IRIGB-MIB", "rcIrigbAMOutput")
)
if mibBuilder.loadTexts:
    rcIrigbAMOutGroup.setStatus("current")

rcIrigbInputGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 15004, 4, 10, 2, 2, 5)
)
rcIrigbInputGroup.setObjects(
    ("RUGGEDCOM-IRIGB-MIB", "rcIrigbInput")
)
if mibBuilder.loadTexts:
    rcIrigbInputGroup.setStatus("current")

rcIrigbTTLOutput01Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 15004, 4, 10, 2, 2, 6)
)
rcIrigbTTLOutput01Group.setObjects(
      *(("RUGGEDCOM-IRIGB-MIB", "rcIrigbOutputPWM1"),
        ("RUGGEDCOM-IRIGB-MIB", "rcIrigbPulseInterval1"),
        ("RUGGEDCOM-IRIGB-MIB", "rcIrigbPulseWidth1"),
        ("RUGGEDCOM-IRIGB-MIB", "rcIrigbStartTime1"))
)
if mibBuilder.loadTexts:
    rcIrigbTTLOutput01Group.setStatus("current")

rcIrigbTTLOutput02Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 15004, 4, 10, 2, 2, 7)
)
rcIrigbTTLOutput02Group.setObjects(
      *(("RUGGEDCOM-IRIGB-MIB", "rcIrigbOutputPWM2"),
        ("RUGGEDCOM-IRIGB-MIB", "rcIrigbPulseInterval2"),
        ("RUGGEDCOM-IRIGB-MIB", "rcIrigbPulseWidth2"),
        ("RUGGEDCOM-IRIGB-MIB", "rcIrigbStartTime2"))
)
if mibBuilder.loadTexts:
    rcIrigbTTLOutput02Group.setStatus("current")


# Notification objects

rcIrigbStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 15004, 5, 35)
)
rcIrigbStatusChange.setObjects(
    ("RUGGEDCOM-IRIGB-MIB", "rcIrigbStatus")
)
if mibBuilder.loadTexts:
    rcIrigbStatusChange.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RUGGEDCOM-IRIGB-MIB",
    **{"RcTimeStamp": RcTimeStamp,
       "rcIrigb": rcIrigb,
       "rcIrigbBase": rcIrigbBase,
       "rcIrigbStatus": rcIrigbStatus,
       "rcIrigbAMOutput": rcIrigbAMOutput,
       "rcIrigbTimeCode": rcIrigbTimeCode,
       "rcIrigbExt": rcIrigbExt,
       "rcIrigbInput": rcIrigbInput,
       "rcIrigbLockInt": rcIrigbLockInt,
       "rcIrigbCableComp": rcIrigbCableComp,
       "rcIrigbOFM": rcIrigbOFM,
       "rcIrigbFreqAdj": rcIrigbFreqAdj,
       "rcIrigbOutputPWM1": rcIrigbOutputPWM1,
       "rcIrigbPulseInterval1": rcIrigbPulseInterval1,
       "rcIrigbPulseWidth1": rcIrigbPulseWidth1,
       "rcIrigbStartTime1": rcIrigbStartTime1,
       "rcIrigbOutputPWM2": rcIrigbOutputPWM2,
       "rcIrigbPulseInterval2": rcIrigbPulseInterval2,
       "rcIrigbPulseWidth2": rcIrigbPulseWidth2,
       "rcIrigbStartTime2": rcIrigbStartTime2,
       "rcIrigbConformance": rcIrigbConformance,
       "rcIrigbGroups": rcIrigbGroups,
       "rcIrigbBaseGroup": rcIrigbBaseGroup,
       "rcIrigbNotifyGroup": rcIrigbNotifyGroup,
       "rcIrigbCommonGroup": rcIrigbCommonGroup,
       "rcIrigbAMOutGroup": rcIrigbAMOutGroup,
       "rcIrigbInputGroup": rcIrigbInputGroup,
       "rcIrigbTTLOutput01Group": rcIrigbTTLOutput01Group,
       "rcIrigbTTLOutput02Group": rcIrigbTTLOutput02Group,
       "rcIrigbStatusChange": rcIrigbStatusChange}
)
