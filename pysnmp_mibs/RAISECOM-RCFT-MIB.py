# SNMP MIB module (RAISECOM-RCFT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/raisecom/RAISECOM-RCFT-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:37:04 2025
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
 NotificationType,
 TimeTicks,
 Unsigned32,
 enterprises,
 iso,
 mib_2) = mibBuilder.importSymbols(
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
    "iso",
    "mib-2")

(DisplayString,
 PhysAddress,
 TextualConvention,
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TimeStamp")


# MODULE-IDENTITY

raiseCom = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8886)
)
if mibBuilder.loadTexts:
    raiseCom.setRevisions(
        ("1903-07-28 00:00",
         "1909-01-09 00:00",
         "1909-03-24 00:00",
         "1909-05-19 00:00",
         "1909-05-26 00:00",
         "2009-06-04 00:00",
         "2009-06-09 00:00",
         "2009-08-28 00:00",
         "1909-09-03 11:30",
         "1909-09-09 11:30",
         "0909-10-30 09:43",
         "1910-01-27 11:23",
         "1910-03-03 00:00",
         "1910-03-10 00:00",
         "1910-03-10 00:00",
         "1910-05-13 16:32",
         "1910-07-02 00:00",
         "1910-10-22 16:38",
         "1910-11-15 00:00",
         "1912-08-10 00:00",
         "1913-05-08 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Rc002_ObjectIdentity = ObjectIdentity
rc002 = _Rc002_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 2)
)
_RcftTraps_ObjectIdentity = ObjectIdentity
rcftTraps = _RcftTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 2, 0)
)
_RcftMibObjects_ObjectIdentity = ObjectIdentity
rcftMibObjects = _RcftMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1)
)
_RcftSystem_ObjectIdentity = ObjectIdentity
rcftSystem = _RcftSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 1)
)
_RcftSysId_Type = Integer32
_RcftSysId_Object = MibScalar
rcftSysId = _RcftSysId_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 1, 1),
    _RcftSysId_Type()
)
rcftSysId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftSysId.setStatus("current")


class _RcftSysLevel_Type(Integer32):
    """Custom type rcftSysLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("kernal", 1),
          ("convergence", 2),
          ("subordinate", 3))
    )


_RcftSysLevel_Type.__name__ = "Integer32"
_RcftSysLevel_Object = MibScalar
rcftSysLevel = _RcftSysLevel_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 1, 2),
    _RcftSysLevel_Type()
)
rcftSysLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftSysLevel.setStatus("current")
_RcftSysChassisNum_Type = Integer32
_RcftSysChassisNum_Object = MibScalar
rcftSysChassisNum = _RcftSysChassisNum_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 1, 3),
    _RcftSysChassisNum_Type()
)
rcftSysChassisNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftSysChassisNum.setStatus("current")


class _RcftSysAlarm_Type(Integer32):
    """Custom type rcftSysAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("minor", 2),
          ("serious", 3))
    )


_RcftSysAlarm_Type.__name__ = "Integer32"
_RcftSysAlarm_Object = MibScalar
rcftSysAlarm = _RcftSysAlarm_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 1, 4),
    _RcftSysAlarm_Type()
)
rcftSysAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftSysAlarm.setStatus("current")
_RcftSysTmptAlarmThreshold_Type = Integer32
_RcftSysTmptAlarmThreshold_Object = MibScalar
rcftSysTmptAlarmThreshold = _RcftSysTmptAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 1, 5),
    _RcftSysTmptAlarmThreshold_Type()
)
rcftSysTmptAlarmThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftSysTmptAlarmThreshold.setStatus("current")


class _RcftSysTrapEnable_Type(Integer32):
    """Custom type rcftSysTrapEnable based on Integer32"""
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


_RcftSysTrapEnable_Type.__name__ = "Integer32"
_RcftSysTrapEnable_Object = MibScalar
rcftSysTrapEnable = _RcftSysTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 1, 6),
    _RcftSysTrapEnable_Type()
)
rcftSysTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftSysTrapEnable.setStatus("current")
_RcftSysTrapTarget_ObjectIdentity = ObjectIdentity
rcftSysTrapTarget = _RcftSysTrapTarget_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 1, 7)
)
_RcftSysTrapTargetEntry_ObjectIdentity = ObjectIdentity
rcftSysTrapTargetEntry = _RcftSysTrapTargetEntry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 1, 7, 1)
)
_RcftTrapSink1_Type = IpAddress
_RcftTrapSink1_Object = MibScalar
rcftTrapSink1 = _RcftTrapSink1_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 1, 7, 1, 1),
    _RcftTrapSink1_Type()
)
rcftTrapSink1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftTrapSink1.setStatus("current")
_RcftTrapSink2_Type = IpAddress
_RcftTrapSink2_Object = MibScalar
rcftTrapSink2 = _RcftTrapSink2_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 1, 7, 1, 2),
    _RcftTrapSink2_Type()
)
rcftTrapSink2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftTrapSink2.setStatus("current")
_RcftTrapSink3_Type = IpAddress
_RcftTrapSink3_Object = MibScalar
rcftTrapSink3 = _RcftTrapSink3_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 1, 7, 1, 3),
    _RcftTrapSink3_Type()
)
rcftTrapSink3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftTrapSink3.setStatus("current")
_RcftTrapSink4_Type = IpAddress
_RcftTrapSink4_Object = MibScalar
rcftTrapSink4 = _RcftTrapSink4_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 1, 7, 1, 4),
    _RcftTrapSink4_Type()
)
rcftTrapSink4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftTrapSink4.setStatus("current")
_RcftTrapSink5_Type = IpAddress
_RcftTrapSink5_Object = MibScalar
rcftTrapSink5 = _RcftTrapSink5_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 1, 7, 1, 5),
    _RcftTrapSink5_Type()
)
rcftTrapSink5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftTrapSink5.setStatus("current")
_RcftTrapSink6_Type = IpAddress
_RcftTrapSink6_Object = MibScalar
rcftTrapSink6 = _RcftTrapSink6_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 1, 7, 1, 6),
    _RcftTrapSink6_Type()
)
rcftTrapSink6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftTrapSink6.setStatus("current")
_RcftTrapSink7_Type = IpAddress
_RcftTrapSink7_Object = MibScalar
rcftTrapSink7 = _RcftTrapSink7_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 1, 7, 1, 7),
    _RcftTrapSink7_Type()
)
rcftTrapSink7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftTrapSink7.setStatus("current")
_RcftTrapSink8_Type = IpAddress
_RcftTrapSink8_Object = MibScalar
rcftTrapSink8 = _RcftTrapSink8_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 1, 7, 1, 8),
    _RcftTrapSink8_Type()
)
rcftTrapSink8.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftTrapSink8.setStatus("current")
_RcftRSlotTmptAlarmThreshold_Type = Integer32
_RcftRSlotTmptAlarmThreshold_Object = MibScalar
rcftRSlotTmptAlarmThreshold = _RcftRSlotTmptAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 1, 8),
    _RcftRSlotTmptAlarmThreshold_Type()
)
rcftRSlotTmptAlarmThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftRSlotTmptAlarmThreshold.setStatus("current")
_RcftSysTrapPort_ObjectIdentity = ObjectIdentity
rcftSysTrapPort = _RcftSysTrapPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 1, 9)
)
_RcftSysTrapPortEntry_ObjectIdentity = ObjectIdentity
rcftSysTrapPortEntry = _RcftSysTrapPortEntry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 1, 9, 1)
)
_RcftTrapPort1_Type = Integer32
_RcftTrapPort1_Object = MibScalar
rcftTrapPort1 = _RcftTrapPort1_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 1, 9, 1, 1),
    _RcftTrapPort1_Type()
)
rcftTrapPort1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftTrapPort1.setStatus("current")
_RcftTrapPort2_Type = Integer32
_RcftTrapPort2_Object = MibScalar
rcftTrapPort2 = _RcftTrapPort2_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 1, 9, 1, 2),
    _RcftTrapPort2_Type()
)
rcftTrapPort2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftTrapPort2.setStatus("current")
_RcftTrapPort3_Type = Integer32
_RcftTrapPort3_Object = MibScalar
rcftTrapPort3 = _RcftTrapPort3_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 1, 9, 1, 3),
    _RcftTrapPort3_Type()
)
rcftTrapPort3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftTrapPort3.setStatus("current")
_RcftTrapPort4_Type = Integer32
_RcftTrapPort4_Object = MibScalar
rcftTrapPort4 = _RcftTrapPort4_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 1, 9, 1, 4),
    _RcftTrapPort4_Type()
)
rcftTrapPort4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftTrapPort4.setStatus("current")
_RcftTrapPort5_Type = Integer32
_RcftTrapPort5_Object = MibScalar
rcftTrapPort5 = _RcftTrapPort5_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 1, 9, 1, 5),
    _RcftTrapPort5_Type()
)
rcftTrapPort5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftTrapPort5.setStatus("current")
_RcftTrapPort6_Type = Integer32
_RcftTrapPort6_Object = MibScalar
rcftTrapPort6 = _RcftTrapPort6_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 1, 9, 1, 6),
    _RcftTrapPort6_Type()
)
rcftTrapPort6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftTrapPort6.setStatus("current")
_RcftTrapPort7_Type = Integer32
_RcftTrapPort7_Object = MibScalar
rcftTrapPort7 = _RcftTrapPort7_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 1, 9, 1, 7),
    _RcftTrapPort7_Type()
)
rcftTrapPort7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftTrapPort7.setStatus("current")
_RcftTrapPort8_Type = Integer32
_RcftTrapPort8_Object = MibScalar
rcftTrapPort8 = _RcftTrapPort8_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 1, 9, 1, 8),
    _RcftTrapPort8_Type()
)
rcftTrapPort8.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftTrapPort8.setStatus("current")
_RcftChassis_ObjectIdentity = ObjectIdentity
rcftChassis = _RcftChassis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 2)
)
_RcftChassisTable_Object = MibTable
rcftChassisTable = _RcftChassisTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 2, 1)
)
if mibBuilder.loadTexts:
    rcftChassisTable.setStatus("current")
_RcftChassisEntry_Object = MibTableRow
rcftChassisEntry = _RcftChassisEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 2, 1, 1)
)
rcftChassisEntry.setIndexNames(
    (0, "RAISECOM-RCFT-MIB", "rcftChassisIndex"),
)
if mibBuilder.loadTexts:
    rcftChassisEntry.setStatus("current")
_RcftChassisIndex_Type = Integer32
_RcftChassisIndex_Object = MibTableColumn
rcftChassisIndex = _RcftChassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 2, 1, 1, 1),
    _RcftChassisIndex_Type()
)
rcftChassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftChassisIndex.setStatus("current")


class _RcftChassisExist_Type(Integer32):
    """Custom type rcftChassisExist based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("exist", 1),
          ("notExist", 2))
    )


_RcftChassisExist_Type.__name__ = "Integer32"
_RcftChassisExist_Object = MibTableColumn
rcftChassisExist = _RcftChassisExist_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 2, 1, 1, 2),
    _RcftChassisExist_Type()
)
rcftChassisExist.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftChassisExist.setStatus("current")
_RcftChassisTmpt_Type = Integer32
_RcftChassisTmpt_Object = MibTableColumn
rcftChassisTmpt = _RcftChassisTmpt_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 2, 1, 1, 3),
    _RcftChassisTmpt_Type()
)
rcftChassisTmpt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftChassisTmpt.setStatus("current")
_RcftPowerNum_Type = Integer32
_RcftPowerNum_Object = MibTableColumn
rcftPowerNum = _RcftPowerNum_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 2, 1, 1, 4),
    _RcftPowerNum_Type()
)
rcftPowerNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftPowerNum.setStatus("current")


class _RcftChassisType_Type(Integer32):
    """Custom type rcftChassisType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("rcChassis16BP-REV-C", 1),
          ("rcChassis16BP-REV-D", 2),
          ("rcChassis4BP-REV-A", 3),
          ("rcChassis16BP-REV-E", 4),
          ("rcChassisRC001-1M-NMS-REV-A", 5),
          ("rcChassisRC001-1M-NMS-REV-B", 6),
          ("rcChassisRC001-2M-NMS-REV-A", 7))
    )


_RcftChassisType_Type.__name__ = "Integer32"
_RcftChassisType_Object = MibTableColumn
rcftChassisType = _RcftChassisType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 2, 1, 1, 5),
    _RcftChassisType_Type()
)
rcftChassisType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftChassisType.setStatus("current")
_RcftChassisDescr_Type = DisplayString
_RcftChassisDescr_Object = MibTableColumn
rcftChassisDescr = _RcftChassisDescr_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 2, 1, 1, 6),
    _RcftChassisDescr_Type()
)
rcftChassisDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftChassisDescr.setStatus("current")
_RcftPower_ObjectIdentity = ObjectIdentity
rcftPower = _RcftPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 3)
)
_RcftPowerTable_Object = MibTable
rcftPowerTable = _RcftPowerTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 3, 1)
)
if mibBuilder.loadTexts:
    rcftPowerTable.setStatus("current")
_RcftPowerEntry_Object = MibTableRow
rcftPowerEntry = _RcftPowerEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 3, 1, 1)
)
rcftPowerEntry.setIndexNames(
    (0, "RAISECOM-RCFT-MIB", "rcftChassisIndex"),
    (0, "RAISECOM-RCFT-MIB", "rcftPowerIndex"),
)
if mibBuilder.loadTexts:
    rcftPowerEntry.setStatus("current")
_RcftPowerIndex_Type = Integer32
_RcftPowerIndex_Object = MibTableColumn
rcftPowerIndex = _RcftPowerIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 3, 1, 1, 1),
    _RcftPowerIndex_Type()
)
rcftPowerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftPowerIndex.setStatus("current")


class _RcftPowerExist_Type(Integer32):
    """Custom type rcftPowerExist based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("exist", 1),
          ("notExist", 2))
    )


_RcftPowerExist_Type.__name__ = "Integer32"
_RcftPowerExist_Object = MibTableColumn
rcftPowerExist = _RcftPowerExist_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 3, 1, 1, 2),
    _RcftPowerExist_Type()
)
rcftPowerExist.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftPowerExist.setStatus("current")


class _Rcft5vStatus_Type(Integer32):
    """Custom type rcft5vStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("abnormal", 2))
    )


_Rcft5vStatus_Type.__name__ = "Integer32"
_Rcft5vStatus_Object = MibTableColumn
rcft5vStatus = _Rcft5vStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 3, 1, 1, 3),
    _Rcft5vStatus_Type()
)
rcft5vStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcft5vStatus.setStatus("current")


class _Rcft12vStatus_Type(Integer32):
    """Custom type rcft12vStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("abnormal", 2))
    )


_Rcft12vStatus_Type.__name__ = "Integer32"
_Rcft12vStatus_Object = MibTableColumn
rcft12vStatus = _Rcft12vStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 3, 1, 1, 4),
    _Rcft12vStatus_Type()
)
rcft12vStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcft12vStatus.setStatus("current")


class _Rcft5vAC_Type(Integer32):
    """Custom type rcft5vAC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ac", 1),
          ("dc", 2))
    )


_Rcft5vAC_Type.__name__ = "Integer32"
_Rcft5vAC_Object = MibTableColumn
rcft5vAC = _Rcft5vAC_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 3, 1, 1, 5),
    _Rcft5vAC_Type()
)
rcft5vAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcft5vAC.setStatus("current")


class _Rcft12vAC_Type(Integer32):
    """Custom type rcft12vAC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ac", 1),
          ("dc", 2))
    )


_Rcft12vAC_Type.__name__ = "Integer32"
_Rcft12vAC_Object = MibTableColumn
rcft12vAC = _Rcft12vAC_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 3, 1, 1, 6),
    _Rcft12vAC_Type()
)
rcft12vAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcft12vAC.setStatus("current")
_RcftFan_ObjectIdentity = ObjectIdentity
rcftFan = _RcftFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 4)
)
_RcftFanTable_Object = MibTable
rcftFanTable = _RcftFanTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 4, 1)
)
if mibBuilder.loadTexts:
    rcftFanTable.setStatus("current")
_RcftFanEntry_Object = MibTableRow
rcftFanEntry = _RcftFanEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 4, 1, 1)
)
rcftFanEntry.setIndexNames(
    (0, "RAISECOM-RCFT-MIB", "rcftChassisIndex"),
    (0, "RAISECOM-RCFT-MIB", "rcftFanIndex"),
)
if mibBuilder.loadTexts:
    rcftFanEntry.setStatus("current")
_RcftFanIndex_Type = Integer32
_RcftFanIndex_Object = MibTableColumn
rcftFanIndex = _RcftFanIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 4, 1, 1, 1),
    _RcftFanIndex_Type()
)
rcftFanIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftFanIndex.setStatus("current")


class _RcftFanLoc_Type(Integer32):
    """Custom type rcftFanLoc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fixed", 1),
          ("ps1", 2),
          ("ps2", 3))
    )


_RcftFanLoc_Type.__name__ = "Integer32"
_RcftFanLoc_Object = MibTableColumn
rcftFanLoc = _RcftFanLoc_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 4, 1, 1, 2),
    _RcftFanLoc_Type()
)
rcftFanLoc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftFanLoc.setStatus("current")


class _RcftFanStatus_Type(Integer32):
    """Custom type rcftFanStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("abnormal", 2))
    )


_RcftFanStatus_Type.__name__ = "Integer32"
_RcftFanStatus_Object = MibTableColumn
rcftFanStatus = _RcftFanStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 4, 1, 1, 3),
    _RcftFanStatus_Type()
)
rcftFanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftFanStatus.setStatus("current")
_RcftSlotStat_ObjectIdentity = ObjectIdentity
rcftSlotStat = _RcftSlotStat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5)
)
_RcftSlotStatTable_Object = MibTable
rcftSlotStatTable = _RcftSlotStatTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1)
)
if mibBuilder.loadTexts:
    rcftSlotStatTable.setStatus("current")
_RcftSlotStatEntry_Object = MibTableRow
rcftSlotStatEntry = _RcftSlotStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1)
)
rcftSlotStatEntry.setIndexNames(
    (0, "RAISECOM-RCFT-MIB", "rcftChassisIndex"),
    (0, "RAISECOM-RCFT-MIB", "rcftSlotIndex"),
)
if mibBuilder.loadTexts:
    rcftSlotStatEntry.setStatus("current")
_RcftSlotIndex_Type = Integer32
_RcftSlotIndex_Object = MibTableColumn
rcftSlotIndex = _RcftSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 1),
    _RcftSlotIndex_Type()
)
rcftSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftSlotIndex.setStatus("current")


class _RcftSlotExist_Type(Integer32):
    """Custom type rcftSlotExist based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("exist", 1),
          ("notExist", 2))
    )


_RcftSlotExist_Type.__name__ = "Integer32"
_RcftSlotExist_Object = MibTableColumn
rcftSlotExist = _RcftSlotExist_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 2),
    _RcftSlotExist_Type()
)
rcftSlotExist.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftSlotExist.setStatus("current")


class _RcftSlotType_Type(Integer32):
    """Custom type rcftSlotType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              50,
              51,
              52,
              53,
              54,
              55,
              56,
              57,
              58,
              59,
              64,
              65,
              66,
              67,
              72,
              73,
              74,
              75,
              76,
              77,
              78,
              79,
              80,
              81,
              82,
              83,
              84,
              85,
              86,
              87,
              88,
              89,
              90,
              91,
              92,
              93,
              94,
              95,
              100,
              101,
              102,
              103,
              104,
              105,
              106,
              107,
              112,
              113,
              114,
              115,
              116,
              117,
              118,
              119,
              124,
              125,
              126,
              127,
              132,
              133,
              134,
              135,
              136,
              137,
              138,
              139,
              140,
              141,
              142,
              143,
              152,
              153,
              154,
              155,
              156,
              157,
              158,
              159,
              164,
              165,
              166,
              167,
              172,
              173,
              174,
              175,
              180,
              181,
              182,
              183,
              184,
              185,
              186,
              187,
              188,
              189,
              190,
              191,
              192,
              193,
              194,
              195,
              200,
              201,
              202,
              203,
              204,
              205,
              206,
              207,
              208,
              209,
              210,
              211,
              216,
              217,
              218,
              219,
              224,
              225,
              226,
              227,
              228,
              229,
              230,
              231,
              236,
              237,
              238,
              239,
              252,
              256,
              268,
              269,
              270,
              271,
              272,
              273,
              274,
              275,
              276,
              277,
              278,
              279,
              280,
              284,
              288,
              289,
              290,
              291,
              292,
              293,
              294,
              295,
              296,
              297,
              298,
              299,
              304,
              305,
              306,
              307,
              312,
              313,
              314,
              315,
              320,
              321,
              322,
              323,
              328,
              329,
              330,
              331,
              336,
              337,
              338,
              339,
              340,
              341,
              342,
              343,
              344,
              345,
              346,
              347,
              348,
              349,
              350,
              351,
              368,
              369,
              370,
              371,
              372,
              373,
              374,
              375,
              376,
              377,
              378,
              379,
              380,
              381,
              382,
              383,
              400,
              401,
              402,
              403,
              404,
              408,
              412,
              416,
              417,
              418,
              419,
              424,
              425,
              426,
              427,
              428,
              429,
              430,
              431,
              432,
              433,
              434,
              435,
              436,
              437,
              438,
              439,
              440,
              441,
              442,
              443,
              444,
              445,
              446,
              447,
              448,
              449,
              450,
              451,
              452,
              453,
              454,
              455,
              456,
              457,
              458,
              459,
              460,
              461,
              462,
              463,
              476,
              477,
              478,
              479,
              488,
              489,
              490,
              491,
              500,
              501,
              502,
              503,
              508,
              509,
              510,
              511,
              512,
              513,
              514,
              515,
              516,
              517,
              518,
              519,
              520,
              521,
              522,
              523,
              524,
              525,
              526,
              527,
              532,
              533,
              534,
              535,
              544,
              545,
              546,
              547,
              548,
              549,
              550,
              551,
              556,
              557,
              558,
              559,
              564,
              565,
              566,
              567,
              568,
              569,
              570,
              571,
              572,
              573,
              574,
              575,
              576,
              580,
              584,
              588,
              592,
              596,
              597,
              598,
              599,
              600,
              604,
              620,
              621,
              622,
              623,
              624,
              625,
              626,
              627,
              628,
              629,
              630,
              631,
              640,
              641,
              642,
              643,
              644,
              645,
              646,
              647,
              648,
              652,
              653,
              654,
              655,
              657,
              658,
              672,
              684,
              688,
              692,
              728,
              752,
              753,
              754,
              755,
              756,
              757,
              758,
              759,
              760,
              761,
              762,
              763,
              999,
              1501,
              1502,
              2001,
              2002,
              2005,
              2006,
              10002,
              10003,
              10004,
              10006,
              10007,
              10016,
              10018,
              10019,
              10021,
              10022,
              10023,
              10024,
              10027,
              10028,
              10031,
              10033,
              10038,
              10039,
              10040,
              10041,
              10042,
              10043,
              10044,
              10046,
              10047,
              10048,
              10050,
              10052,
              10053,
              10054,
              10055,
              10056,
              10057,
              10058,
              10059,
              10061,
              10062,
              10063,
              10064,
              10065,
              10067,
              10069,
              10071,
              10072,
              10074,
              10076,
              10077,
              10078,
              10079,
              10080,
              10082,
              10084,
              10085,
              10086,
              10088,
              10091,
              10092,
              10094,
              10101,
              10103,
              10104,
              10106,
              10107,
              10112,
              10113,
              10122,
              10123,
              10124,
              10125,
              10127,
              10128,
              10130,
              10131,
              10133,
              10136,
              10137,
              10138,
              10139,
              10141,
              10142,
              10143,
              10144,
              10145,
              10146,
              10147,
              10148,
              10153,
              10154,
              10159,
              10160,
              10161,
              10162,
              10163,
              10164,
              10166,
              10167,
              10169,
              10170,
              10172,
              10175,
              10176,
              10177,
              10181,
              10182,
              10183,
              10184,
              10186,
              10187,
              10188,
              10189,
              10190,
              10194,
              10197,
              10198,
              10201,
              10203,
              11013,
              11014,
              11022,
              11023,
              11024,
              11026,
              11028,
              11031,
              11032,
              12015,
              12016,
              12017,
              12018,
              12019,
              12020,
              13055,
              13056,
              13057,
              13058,
              13059,
              13065,
              13066,
              13070,
              13071,
              13072,
              13073,
              13074,
              13075,
              13081,
              13082,
              13083,
              13084,
              15001,
              15003,
              15005,
              15006,
              17008,
              17011,
              17099,
              17100,
              18008,
              18011,
              18099,
              18100,
              62469,
              62470,
              62512,
              62513,
              62516,
              62517,
              62519,
              62520,
              62523,
              62525,
              62527,
              62528,
              62530,
              62531,
              62534,
              62535,
              62537,
              62538,
              62541,
              62542,
              62544,
              62545,
              62547,
              62548,
              62551,
              62552,
              62555,
              62556,
              62558,
              62559,
              62561,
              62562,
              62564,
              62565,
              62568,
              62570,
              62572,
              62573,
              62574,
              62576,
              62577,
              62579,
              62580,
              62581,
              62587,
              62588,
              62590,
              62591,
              62593,
              62594,
              62596,
              62597,
              62601,
              62602,
              62604,
              62605,
              62609,
              62610,
              62612,
              62613,
              162466,
              162467,
              162468)
        )
    )
    namedValues = NamedValues(
        *(("rcftTypeRC202-E-M", 8),
          ("rcftTypeRC202-E-S1", 9),
          ("rcftTypeRC202-E-S2", 10),
          ("rcftTypeRC202-E-S3", 11),
          ("rcftTypeRC202-FE-M", 12),
          ("rcftTypeRC202-FE-S1", 13),
          ("rcftTypeRC202-FE-S2", 14),
          ("rcftTypeRC202-FE-S3", 15),
          ("rcftTypeRC102-FE-M", 16),
          ("rcftTypeRC102-FE-S1", 17),
          ("rcftTypeRC102-FE-S2", 18),
          ("rcftTypeRC102-FE-S3", 19),
          ("rcftTypeRC202-GE-M", 20),
          ("rcftTypeRC202-GE-S1", 21),
          ("rcftTypeRC202-GE-S2", 22),
          ("rcftTypeRC202-GE-S3", 23),
          ("rcftTypeRC303-4-FE-M", 24),
          ("rcftTypeRC303-4-FE-S1", 25),
          ("rcftTypeRC303-4-FE-S2", 26),
          ("rcftTypeRC303-4-FE-S3", 27),
          ("rcftTypeRC302-FE-M", 28),
          ("rcftTypeRC302-FE-S1", 29),
          ("rcftTypeRC302-FE-S2", 30),
          ("rcftTypeRC302-FE-S3", 31),
          ("rcftTypeRC402-Gb-M", 32),
          ("rcftTypeRC402-Gb-S1", 33),
          ("rcftTypeRC402-Gb-S2", 34),
          ("rcftTypeRC402-Gb-S3", 35),
          ("rcftTypeRC402-C3-M", 36),
          ("rcftTypeRC402-C3-S1", 37),
          ("rcftTypeRC402-C3-S2", 38),
          ("rcftTypeRC402-C3-S3", 39),
          ("rcftTypeRC303-4-E-M", 40),
          ("rcftTypeRC303-4-E-S1", 41),
          ("rcftTypeRC303-4-E-S2", 42),
          ("rcftTypeRC303-4-E-S3", 43),
          ("rcftTypeRC602-FE-M-REV-A", 44),
          ("rcftTypeRC602-FE-S1-REV-A", 45),
          ("rcftTypeRC602-FE-S2-REV-A", 46),
          ("rcftTypeRC602-FE-S3-REV-A", 47),
          ("rcftTypeRC303-4-GE-M", 48),
          ("rcftTypeRC303-4-GE-S1", 49),
          ("rcftTypeRC303-4-GE-S2", 50),
          ("rcftTypeRC303-4-GE-S3", 51),
          ("rcftTypeRC305-6-FE-M", 52),
          ("rcftTypeRC305-6-FE-S1", 53),
          ("rcftTypeRC305-6-FE-S2", 54),
          ("rcftTypeRC305-6-FE-S3", 55),
          ("rcftTypeRC307-8-C3-M", 56),
          ("rcftTypeRC307-8-C3-S1", 57),
          ("rcftTypeRC307-8-C3-S2", 58),
          ("rcftTypeRC307-8-C3-S3", 59),
          ("rcftTypeRC307-8-Gb-M", 64),
          ("rcftTypeRC307-8-Gb-S1", 65),
          ("rcftTypeRC307-8-Gb-S2", 66),
          ("rcftTypeRC307-8-Gb-S3", 67),
          ("rcftTypeRC502-FE-M-REV-B", 72),
          ("rcftTypeRC502-FE-S1-REV-B", 73),
          ("rcftTypeRC502-FE-S2-REV-B", 74),
          ("rcftTypeRC502-FE-S3-REV-B", 75),
          ("rcftTypeRC102-FE-M-REV-E", 76),
          ("rcftTypeRC102-FE-S1-REV-E", 77),
          ("rcftTypeRC102-FE-S2-REV-E", 78),
          ("rcftTypeRC102-FE-S3-REV-E", 79),
          ("rcftTypeRC202-FE-M-REV-F", 80),
          ("rcftTypeRC202-FE-S1-REV-F", 81),
          ("rcftTypeRC202-FE-S2-REV-F", 82),
          ("rcftTypeRC202-FE-S3-REV-F", 83),
          ("rcftTypeRC102-FE-M-REV-F", 84),
          ("rcftTypeRC102-FE-S1-REV-F", 85),
          ("rcftTypeRC102-FE-S2-REV-F", 86),
          ("rcftTypeRC102-FE-S3-REV-F", 87),
          ("rcftTypeRC202-FE-M-REV-G", 88),
          ("rcftTypeRC202-FE-S1-REV-G", 89),
          ("rcftTypeRC202-FE-S2-REV-G", 90),
          ("rcftTypeRC202-FE-S3-REV-G", 91),
          ("rcftTypeRC602-FE-M-REV-C", 92),
          ("rcftTypeRC602-FE-S1-REV-C", 93),
          ("rcftTypeRC602-FE-S2-REV-C", 94),
          ("rcftTypeRC602-FE-S3-REV-C", 95),
          ("rcftTypeRC305-6-FE-M-REV-B", 100),
          ("rcftTypeRC305-6-FE-S1-REV-B", 101),
          ("rcftTypeRC305-6-FE-S2-REV-B", 102),
          ("rcftTypeRC305-6-FE-S3-REV-B", 103),
          ("rcftTypeRC502-FE-M-REV-C", 104),
          ("rcftTypeRC502-FE-S1-REV-C", 105),
          ("rcftTypeRC502-FE-S2-REV-C", 106),
          ("rcftTypeRC502-FE-S3-REV-C", 107),
          ("rcftTypeRC404-Gb-M", 112),
          ("rcftTypeRC404-Gb-S1", 113),
          ("rcftTypeRC404-Gb-S2", 114),
          ("rcftTypeRC404-Gb-S3", 115),
          ("rcftTypeRC404-C3-M", 116),
          ("rcftTypeRC404-C3-S1", 117),
          ("rcftTypeRC404-C3-S2", 118),
          ("rcftTypeRC404-C3-S3", 119),
          ("rcftTypeRC302-E-M", 124),
          ("rcftTypeRC302-E-S1", 125),
          ("rcftTypeRC302-E-S2", 126),
          ("rcftTypeRC302-E-S3", 127),
          ("rcftTypeRC302-GE-M", 132),
          ("rcftTypeRC302-GE-S1", 133),
          ("rcftTypeRC302-GE-S2", 134),
          ("rcftTypeRC302-GE-S3", 135),
          ("rcftTypeRC302-FE-M-REV-B", 136),
          ("rcftTypeRC302-FE-S1-REV-B", 137),
          ("rcftTypeRC302-FE-S2-REV-B", 138),
          ("rcftTypeRC302-FE-S3-REV-B", 139),
          ("rcftTypeRC301-FE-M-REV-A", 140),
          ("rcftTypeRC301-FE-S1-REV-A", 141),
          ("rcftTypeRC301-FE-S2-REV-A", 142),
          ("rcftTypeRC301-FE-S3-REV-A", 143),
          ("rcftTypeRC303-4-FE-M-REV-B", 152),
          ("rcftTypeRC303-4-FE-S1-REV-B", 153),
          ("rcftTypeRC303-4-FE-S2-REV-B", 154),
          ("rcftTypeRC303-4-FE-S3-REV-B", 155),
          ("rcftTypeRC604-FE-M-REV-C", 156),
          ("rcftTypeRC604-FE-S1-REV-C", 157),
          ("rcftTypeRC604-FE-S2-REV-C", 158),
          ("rcftTypeRC604-FE-S3-REV-C", 159),
          ("rcftTypeRC504-FE-M-REV-C", 164),
          ("rcftTypeRC504-FE-S1-REV-C", 165),
          ("rcftTypeRC504-FE-S2-REV-C", 166),
          ("rcftTypeRC504-FE-S3-REV-C", 167),
          ("rcftTypeRC504-E-M-REV-C", 172),
          ("rcftTypeRC504-E-S1-REV-C", 173),
          ("rcftTypeRC504-E-S2-REV-C", 174),
          ("rcftTypeRC504-E-S3-REV-C", 175),
          ("rcftTypeRC302-C3-M-REV-A", 180),
          ("rcftTypeRC302-C3-S1-REV-A", 181),
          ("rcftTypeRC302-C3-S2-REV-A", 182),
          ("rcftTypeRC302-C3-S3-REV-A", 183),
          ("rcftTypeRC302-Gb-M-REV-A", 184),
          ("rcftTypeRC302-Gb-S1-REV-A", 185),
          ("rcftTypeRC302-Gb-S2-REV-A", 186),
          ("rcftTypeRC302-Gb-S3-REV-A", 187),
          ("rcftTypeRC302-C12-M-REV-A", 188),
          ("rcftTypeRC302-C12-S1-REV-A", 189),
          ("rcftTypeRC302-C12-S2-REV-A", 190),
          ("rcftTypeRC302-C12-S3-REV-A", 191),
          ("rcftTypeRC402-C12-M-REV-A", 192),
          ("rcftTypeRC402-C12-S1-REV-A", 193),
          ("rcftTypeRC402-C12-S2-REV-A", 194),
          ("rcftTypeRC402-C12-S3-REV-A", 195),
          ("rcftTypeRC404-C12-M-REV-A", 200),
          ("rcftTypeRC404-C12-S1-REV-A", 201),
          ("rcftTypeRC404-C12-S2-REV-A", 202),
          ("rcftTypeRC404-C12-S3-REV-A", 203),
          ("rcftTypeRC307-8-C12-M", 204),
          ("rcftTypeRC307-8-C12-S1", 205),
          ("rcftTypeRC307-8-C12-S2", 206),
          ("rcftTypeRC307-8-C12-S3", 207),
          ("rcftTypeRC606-FE-M-REV-C", 208),
          ("rcftTypeRC606-FE-S1-REV-C", 209),
          ("rcftTypeRC606-FE-S2-REV-C", 210),
          ("rcftTypeRC606-FE-S3-REV-C", 211),
          ("rcftTypeRC506-FE-M-REV-C", 216),
          ("rcftTypeRC506-FE-S1-REV-C", 217),
          ("rcftTypeRC506-FE-S2-REV-C", 218),
          ("rcftTypeRC506-FE-S3-REV-C", 219),
          ("rcftTypeRC802-30-G703E1-M", 224),
          ("rcftTypeRC802-30-G703E1-S1", 225),
          ("rcftTypeRC802-30-G703E1-S2", 226),
          ("rcftTypeRC802-30-G703E1-S3", 227),
          ("rcftTypeRC502-E-M-REV-C", 228),
          ("rcftTypeRC502-E-S1-REV-C", 229),
          ("rcftTypeRC502-E-S2-REV-C", 230),
          ("rcftTypeRC502-E-S3-REV-C", 231),
          ("rcftTypeRC506-E-M-REV-C", 236),
          ("rcftTypeRC506-E-S1-REV-C", 237),
          ("rcftTypeRC506-E-S2-REV-C", 238),
          ("rcftTypeRC506-E-S3-REV-C", 239),
          ("rcftTypeRC902-EE1-REV-B", 252),
          ("rcftTypeRC904-V35E1-REV-A", 256),
          ("rcftTypeRC102-2FE-M-REV-A", 268),
          ("rcftTypeRC102-2FE-S1-REV-A", 269),
          ("rcftTypeRC102-2FE-S2-REV-A", 270),
          ("rcftTypeRC102-2FE-S3-REV-A", 271),
          ("rcftTypeRC305-6-2FE-M-REV-A", 272),
          ("rcftTypeRC305-6-2FE-S1-REV-A", 273),
          ("rcftTypeRC305-6-2FE-S2-REV-A", 274),
          ("rcftTypeRC305-6-2FE-S3-REV-A", 275),
          ("rcftTypeRC802-30-G703-M-REV-B", 276),
          ("rcftTypeRC802-30-G703-S1-REV-B", 277),
          ("rcftTypeRC802-30-G703-S2-REV-B", 278),
          ("rcftTypeRC802-30-G703-S3-REV-B", 279),
          ("rcftTypeRC904-V35FE1-REV-B", 280),
          ("rcftTypeRC906-EE1-REV-A", 284),
          ("rcftTypeRC804-30-G703-M-REV-B", 288),
          ("rcftTypeRC804-30-G703-S1-REV-B", 289),
          ("rcftTypeRC804-30-G703-S2-REV-B", 290),
          ("rcftTypeRC804-30-G703-S3-REV-B", 291),
          ("rcftTypeRC802-60B-G703-M-REV-A", 292),
          ("rcftTypeRC802-60B-G703-S1-REV-A", 293),
          ("rcftTypeRC802-60B-G703-S2-REV-A", 294),
          ("rcftTypeRC802-60B-G703-S3-REV-A", 295),
          ("rcftTypeRC804-60B-G703-M-REV-A", 296),
          ("rcftTypeRC804-60B-G703-S1-REV-A", 297),
          ("rcftTypeRC804-60B-G703-S2-REV-A", 298),
          ("rcftTypeRC804-60B-G703-S3-REV-A", 299),
          ("rcftTypeRC608-FE-M-REV-C", 304),
          ("rcftTypeRC608-FE-S1-REV-C", 305),
          ("rcftTypeRC608-FE-S2-REV-C", 306),
          ("rcftTypeRC608-FE-S3-REV-C", 307),
          ("rcftTypeRC512-FE-M-REV-A", 312),
          ("rcftTypeRC512-FE-S1-REV-A", 313),
          ("rcftTypeRC512-FE-S2-REV-A", 314),
          ("rcftTypeRC512-FE-S3-REV-A", 315),
          ("rcftTypeRC609-FE-M-REV-C", 320),
          ("rcftTypeRC609-FE-S1-REV-C", 321),
          ("rcftTypeRC609-FE-S2-REV-C", 322),
          ("rcftTypeRC609-FE-S3-REV-C", 323),
          ("rcftTypeRC514-FE-M-REV-A", 328),
          ("rcftTypeRC514-FE-S1-REV-A", 329),
          ("rcftTypeRC514-FE-S2-REV-A", 330),
          ("rcftTypeRC514-FE-S3-REV-A", 331),
          ("rcftTypeRC102-FE-M-REV-G", 336),
          ("rcftTypeRC102-FE-S1-REV-G", 337),
          ("rcftTypeRC102-FE-S2-REV-G", 338),
          ("rcftTypeRC102-FE-S3-REV-G", 339),
          ("rcftTypeRC305-6-FE-M-REV-C", 340),
          ("rcftTypeRC305-6-FE-S1-REV-C", 341),
          ("rcftTypeRC305-6-FE-S2-REV-C", 342),
          ("rcftTypeRC305-6-FE-S3-REV-C", 343),
          ("rcftTypeRC112-FE-M-REV-A", 344),
          ("rcftTypeRC112-FE-S1-REV-A", 345),
          ("rcftTypeRC112-FE-S2-REV-A", 346),
          ("rcftTypeRC112-FE-S3-REV-A", 347),
          ("rcftTypeRC315-6-FE-M-REV-A", 348),
          ("rcftTypeRC315-6-FE-S1-REV-A", 349),
          ("rcftTypeRC315-6-FE-S2-REV-A", 350),
          ("rcftTypeRC315-6-FE-S3-REV-A", 351),
          ("rcftTypeRC202-C3-FE-M-REV-A", 368),
          ("rcftTypeRC202-C3-FE-S1-REV-A", 369),
          ("rcftTypeRC202-C3-FE-S2-REV-A", 370),
          ("rcftTypeRC202-C3-FE-S3-REV-A", 371),
          ("rcftTypeRC303-4-C3-FE-M-REV-A", 372),
          ("rcftTypeRC303-4-C3-FE-S1-REV-A", 373),
          ("rcftTypeRC303-4-C3-FE-S2-REV-A", 374),
          ("rcftTypeRC303-4-C3-FE-S3-REV-A", 375),
          ("rcftTypeRC802-30B-FV35-M-REV-A", 376),
          ("rcftTypeRC802-30B-FV35-S1-REV-A", 377),
          ("rcftTypeRC802-30B-FV35-S2-REV-A", 378),
          ("rcftTypeRC802-30B-FV35-S3-REV-A", 379),
          ("rcftTypeRC804-30B-FV35-M-REV-A", 380),
          ("rcftTypeRC804-30B-FV35-S1-REV-A", 381),
          ("rcftTypeRC804-30B-FV35-S2-REV-A", 382),
          ("rcftTypeRC804-30B-FV35-S3-REV-A", 383),
          ("rcftTypeRC512-FE-M-REV-A-SLAVE", 400),
          ("rcftTypeRC512-FE-S1-REV-A-SLAVE", 401),
          ("rcftTypeRC512-FE-S2-REV-A-SLAVE", 402),
          ("rcftTypeRC512-FE-S3-REV-A-SLAVE", 403),
          ("rcftTypeRC906-FE1-REV-B", 404),
          ("rcftTypeRC902-FE4E1-REV-A", 408),
          ("rcftTypeRC908-EV35-REV-B", 412),
          ("rcftTypeRC112-2FE-M-REV-A", 416),
          ("rcftTypeRC112-2FE-S1-REV-A", 417),
          ("rcftTypeRC112-2FE-S2-REV-A", 418),
          ("rcftTypeRC112-2FE-S3-REV-A", 419),
          ("rcftTypeRC315-6-2FE-M-REV-A", 424),
          ("rcftTypeRC315-6-2FE-S1-REV-A", 425),
          ("rcftTypeRC315-6-2FE-S2-REV-A", 426),
          ("rcftTypeRC315-6-2FE-S3-REV-A", 427),
          ("rcftTypeRCMS2201-30-REV-A", 428),
          ("rcftTypeRCMS2201-30-S1-REV-A", 429),
          ("rcftTypeRCMS2201-30-S2-REV-A", 430),
          ("rcftTypeRCMS2201-30-S3-REV-A", 431),
          ("rcftTypeRCMS2401-30-M-REV-A", 432),
          ("rcftTypeRCMS2401-30-S1-REV-A", 433),
          ("rcftTypeRCMS2401-30-S2-REV-A", 434),
          ("rcftTypeRCMS2401-30-S3-REV-A", 435),
          ("rcftTypeRCMS2601-30-M-REV-A", 436),
          ("rcftTypeRCMS2601-30-S1-REV-A", 437),
          ("rcftTypeRCMS2601-30-S2-REV-A", 438),
          ("rcftTypeRCMS2601-30-S3-REV-A", 439),
          ("rcftTypeRCMS2101-30-FV35-M-REV-A", 440),
          ("rcftTypeRCMS2101-30-FV35-S1-REV-A", 441),
          ("rcftTypeRCMS2101-30-FV35-S2-REV-A", 442),
          ("rcftTypeRCMS2101-30-FV35-S3-REV-A", 443),
          ("rcftTypeRCMS2501-30-FV35-M-REV-A", 444),
          ("rcftTypeRCMS2501-30-FV35-S1-REV-A", 445),
          ("rcftTypeRCMS2501-30-FV35-S2-REV-A", 446),
          ("rcftTypeRCMS2501-30-FV35-S3-REV-A", 447),
          ("rcftTypeRC202-FE-M-NEW-REV-G", 448),
          ("rcftTypeRC202-FE-S1-NEW-REV-G", 449),
          ("rcftTypeRC202-FE-S2-NEW-REV-G", 450),
          ("rcftTypeRC202-FE-S3-NEW-REV-G", 451),
          ("rcftTypeRC522-FE-M-REV-A", 452),
          ("rcftTypeRC522-FE-S1-REV-A", 453),
          ("rcftTypeRC522-FE-S2-REV-A", 454),
          ("rcftTypeRC522-FE-S3-REV-A", 455),
          ("rcftTypeRC522-FE-SDM-REV-A", 456),
          ("rcftTypeRC522-FE-SDS1-REV-A", 457),
          ("rcftTypeRC522-FE-SDS2-REV-A", 458),
          ("rcftTypeRC522-FE-SDS3-REV-A", 459),
          ("rcftTypeRC522-FE-SSM-REV-A", 460),
          ("rcftTypeRC522-FE-SSS1-REV-A", 461),
          ("rcftTypeRC522-FE-SSS2-REV-A", 462),
          ("rcftTypeRC522-FE-SSS3-REV-A", 463),
          ("rcftTypeRC802-30B-FV35-M-REV-M", 476),
          ("rcftTypeRC802-30B-FV35-S1-REV-M", 477),
          ("rcftTypeRC802-30B-FV35-S2-REV-M", 478),
          ("rcftTypeRC802-30B-FV35-S3-REV-M", 479),
          ("rcftTypeRC804-30B-FV35-M-REV-M", 488),
          ("rcftTypeRC804-30B-FV35-S1-REV-M", 489),
          ("rcftTypeRC804-30B-FV35-S2-REV-M", 490),
          ("rcftTypeRC804-30B-FV35-S3-REV-M", 491),
          ("rcftTypeRC602-FE-M-REV-E", 500),
          ("rcftTypeRC602-FE-S1-REV-E", 501),
          ("rcftTypeRC602-FE-S2-REV-E", 502),
          ("rcftTypeRC602-FE-S3-REV-E", 503),
          ("rcftTypeRCMS2201-60-REV-A", 508),
          ("rcftTypeRCMS2201-60-S1-REV-A", 509),
          ("rcftTypeRCMS2201-60-S2-REV-A", 510),
          ("rcftTypeRCMS2201-60-S3-REV-A", 511),
          ("rcftTypeRCMS2401-60-M-REV-A", 512),
          ("rcftTypeRCMS2401-60-S1-REV-A", 513),
          ("rcftTypeRCMS2401-60-S2-REV-A", 514),
          ("rcftTypeRCMS2401-60-S3-REV-A", 515),
          ("rcftTypeRCMS2601-60-M-REV-A", 516),
          ("rcftTypeRCMS2601-60-S1-REV-A", 517),
          ("rcftTypeRCMS2601-60-S2-REV-A", 518),
          ("rcftTypeRCMS2601-60-S3-REV-A", 519),
          ("rcftTypeRC303-4-FE-M-REV-G", 520),
          ("rcftTypeRC303-4-FE-S1-REV-G", 521),
          ("rcftTypeRC303-4-FE-S2-REV-G", 522),
          ("rcftTypeRC303-4-FE-S3-REV-G", 523),
          ("rcftTypeRC301-2-FE-M-REV-G", 524),
          ("rcftTypeRC301-2-FE-S1-REV-G", 525),
          ("rcftTypeRC301-2-FE-S2-REV-G", 526),
          ("rcftTypeRC301-2-FE-S3-REV-G", 527),
          ("rcftTypeRC516-FE-M-REV-A", 532),
          ("rcftTypeRC516-FE-S1-REV-A", 533),
          ("rcftTypeRC516-FE-S2-REV-A", 534),
          ("rcftTypeRC516-FE-S3-REV-A", 535),
          ("rcftTypeRC312-FE-M-REV-A", 544),
          ("rcftTypeRC312-FE-S1-REV-A", 545),
          ("rcftTypeRC312-FE-S2-REV-A", 546),
          ("rcftTypeRC312-FE-S3-REV-A", 547),
          ("rcftTypeRC604-FE-M-REV-E", 548),
          ("rcftTypeRC604-FE-S1-REV-E", 549),
          ("rcftTypeRC604-FE-S2-REV-E", 550),
          ("rcftTypeRC604-FE-S3-REV-E", 551),
          ("rcftTypeRC606-FE-M-REV-E", 556),
          ("rcftTypeRC606-FE-S1-REV-E", 557),
          ("rcftTypeRC606-FE-S2-REV-E", 558),
          ("rcftTypeRC606-FE-S3-REV-E", 559),
          ("rcftTypeRC802-30-G703-M-REV-M", 564),
          ("rcftTypeRC802-30-G703-S1-REV-M", 565),
          ("rcftTypeRC802-30-G703-S2-REV-M", 566),
          ("rcftTypeRC802-30-G703-S3-REV-M", 567),
          ("rcftTypeRC804-30-G703-M-REV-M", 568),
          ("rcftTypeRC804-30-G703-S1-REV-M", 569),
          ("rcftTypeRC804-30-G703-S2-REV-M", 570),
          ("rcftTypeRC804-30-G703-S3-REV-M", 571),
          ("rcftTypeRC806-30-G703-M-REV-M", 572),
          ("rcftTypeRC806-30-G703-S1-REV-M", 573),
          ("rcftTypeRC806-30-G703-S2-REV-M", 574),
          ("rcftTypeRC806-30-G703-S3-REV-M", 575),
          ("rcftTypeOPCOM200-OTU1-2R-REV-A", 576),
          ("rcftTypeOPCOM200-OTU1-3R-REV-A", 580),
          ("rcftTypeRC906-FXE1-REV-A", 584),
          ("rcftTypeRC916-FXE1-REV-A", 588),
          ("rcftTypeOPCOM200-OTU2-2R-REV-A", 592),
          ("rcftTypeRC806-30B-FV35-M-REV-M", 596),
          ("rcftTypeRC806-30B-FV35-S1-REV-M", 597),
          ("rcftTypeRC806-30B-FV35-S2-REV-M", 598),
          ("rcftTypeRC806-30B-FV35-S3-REV-M", 599),
          ("rcftTypeOPCOM200-OTU2-3R-REV-A", 600),
          ("rcftTypeRC512-FE-SLAVE", 604),
          ("rcftTypeRC802-60B-M-REV-M", 620),
          ("rcftTypeRC802-60B-S1-REV-M", 621),
          ("rcftTypeRC802-60B-S2-REV-M", 622),
          ("rcftTypeRC802-60B-S3-REV-M", 623),
          ("rcftTypeRC804-60B-M-REV-M", 624),
          ("rcftTypeRC804-60B-S1-REV-M", 625),
          ("rcftTypeRC804-60B-S2-REV-M", 626),
          ("rcftTypeRC804-60B-S3-REV-M", 627),
          ("rcftTypeRC806-60B-M-REV-M", 628),
          ("rcftTypeRC806-60B-S1-REV-M", 629),
          ("rcftTypeRC806-60B-S2-REV-M", 630),
          ("rcftTypeRC806-60B-S3-REV-M", 631),
          ("rcftTypeRC906-FXE1-M-REV-M", 640),
          ("rcftTypeRC906-FXE1-S1-REV-M", 641),
          ("rcftTypeRC906-FXE1-S2-REV-M", 642),
          ("rcftTypeRC906-FXE1-S3-REV-M", 643),
          ("rcftTypeRC916-FXE1-M-REV-M", 644),
          ("rcftTypeRC916-FXE1-S1-REV-M", 645),
          ("rcftTypeRC916-FXE1-S2-REV-M", 646),
          ("rcftTypeRC916-FXE1-S3-REV-M", 647),
          ("rcftTypeRC906-EE1-REV-M", 648),
          ("rcftTypeRC902-FX4E1-M-REV-A", 652),
          ("rcftTypeRC902-FX4E1-S1-REV-A", 653),
          ("rcftTypeRC902-FX4E1-S2-REV-A", 654),
          ("rcftTypeRC902-FX4E1-S3-REV-A", 655),
          ("rcftTypeRC912-FX4E1-S1-REV-A", 657),
          ("rcftTypeRC912-FX4E1-S2-REV-A", 658),
          ("rcftTypeRC512-FE-MASTER", 672),
          ("rcftTypeRC802-30B-FV35-REV-N", 684),
          ("rcftTypeRC804-30B-FV35-REV-N", 688),
          ("rcftTypeRC806-30B-FV35-REV-N", 692),
          ("rcftTypeRC202-C3-FE-REV-B", 728),
          ("rcftTypeRC512-FE-noOptical1", 752),
          ("rcftTypeRC512-FE-SS15-REV-A", 753),
          ("rcftTypeRC512-FE-SS25-REV-A", 754),
          ("rcftTypeRC512-FE-SS35-REV-A", 755),
          ("rcftTypeRC512-FE-SS-noOptical1", 756),
          ("rcftTypeRC512-FE-SS13-SLAVE", 757),
          ("rcftTypeRC512-FE-SS23-SLAVE", 758),
          ("rcftTypeRC512-FE-SS34-SLAVE", 759),
          ("rcftTypeRC202-FE-M-REV-H", 760),
          ("rcftTypeRC202-FE-S1-REV-H", 761),
          ("rcftTypeRC202-FE-S2-REV-H", 762),
          ("rcftTypeRC202-FE-S3-REV-H", 763),
          ("rcftUnknownType", 999),
          ("rcftTypeRC906H-FEE1-REV-A-SLAVE", 1501),
          ("rcftTypeRC906H-FXE1-REV-A-SLAVE", 1502),
          ("rcftTypeRC906H-FEE1-REV-A-MASTER", 2001),
          ("rcftTypeRC906H-FXE1-REV-A-MASTER", 2002),
          ("rcftTypeRC602-GEF-REV-C-MASTER", 2005),
          ("rcftTypeRC602-GEF-REV-C-SLAVE", 2006),
          ("rcftTypeOPCOM200-OMU4E-REV-A", 10002),
          ("rcftTypeOPCOM200-FEU1-REV-A-MASTER", 10003),
          ("rcftTypeOPCOM200-FEU1-REV-A-SLAVE", 10004),
          ("rcftTypeRC952-FXE1-REV-A-SLAVE", 10006),
          ("rcftTypeRC952-FEE1-REV-A-SLAVE", 10007),
          ("rcftTypeRC202-GE-REV-C", 10016),
          ("rcftTypeOPCOM200-FEU2-REV-A-MASTER", 10018),
          ("rcftTypeOPCOM200-FEU2-REV-A-SLAVE", 10019),
          ("rcftTypeRC552-FE-REV-A-SLAVE", 10021),
          ("rcftTypeRC952-FXE1-REV-C-SLAVE", 10022),
          ("rcftTypeRC952-FEE1-REV-B-SLAVE", 10023),
          ("rcftTypeRC906H-FEE1-SLAVE-PRIVATE", 10024),
          ("rcftTypeRC212-GE-REV-A", 10027),
          ("rcftTypeRC414-REV-A", 10028),
          ("rcftTypeRC602-GE-REV-A-SLAVE", 10031),
          ("rcftTypeRC112-GE-REV-A", 10033),
          ("rcftTypeRC1102-FE-REV-A-SLAVE", 10038),
          ("rcftTypeRC1102-FE-REV-A-MASTER", 10039),
          ("rcftTypeRC152-FE-REV-A", 10040),
          ("rcftTypeRC522-FE-REV-B", 10041),
          ("rcftTypeRC132-FE-REV-A", 10042),
          ("rcftTypeRC552-FE-REV-A-MASTER", 10043),
          ("rcftTypeRC522-FE-REV-D-SLAVE", 10044),
          ("rcftTypeRC1102-E1-REV-B-SLAVE", 10046),
          ("rcftTypeRC1102-E1-REV-B-MASTER", 10047),
          ("rcftTypeRC602-GEF-REV-A-SLAVE", 10048),
          ("rcftTypeOPCOM200-GEU1-REV-A-SLAVE", 10050),
          ("rcftTypeRC522-FE-REV-C-MASTER", 10052),
          ("rcftTypeRC522-FE-REV-C-SLAVE", 10053),
          ("rcftTypeRC602-GE-REV-A-MASTER", 10054),
          ("rcftTypeRC1102-V35-REV-B-MASTER", 10055),
          ("rcftTypeRC2002-30FE-REV-A", 10056),
          ("rcftTypeRC602-GEF-REV-A-MASTER", 10057),
          ("rcftTypeOPCOM200-2GEM-REV-A", 10058),
          ("rcftTypeOPCOM200-GEU1-REV-A-MASTER", 10059),
          ("rcftTypeOPCOM200-2GEM-REV-NEW", 10061),
          ("rcftTypeRC1102-V35-MASTER-REV-A", 10062),
          ("rcftTypeRC952-FXE1-REV-A", 10063),
          ("rcftTypeRC952-FEE1-REV-A", 10064),
          ("rcftTypeRC904-V35FE1-REV-C", 10065),
          ("rcftTypeRC1102-V35-SLAVE-REV-A", 10067),
          ("rcftTypeRC904-V35FE1-BL-REV-C", 10069),
          ("rcftTypeRC852-30-REV-A", 10071),
          ("rcftTypeRC852-30-FV35-REV-A", 10072),
          ("rcftTypeRC902-FE4E1-REV-B", 10074),
          ("rcftTypeRC532-2FE-REV-A-MASTER", 10076),
          ("rcftTypeOPCOM200-2GEM-REV-A2", 10077),
          ("rcftTypeRC1102-E1-BL-REV-A-MASTER", 10078),
          ("rcftTypeRC1102-V35-REV-B-SLAVE", 10079),
          ("rcftTypeRC532-FE-REV-A-MASTER", 10080),
          ("rcftTypeRC522-FE-REV-D-MASTER", 10082),
          ("rcftTypeRC532-2FE-REV-A-SLAVE", 10084),
          ("rcftTypeRC1102-E1-BL-REV-A-SLAVE", 10085),
          ("rcftTypeRC112-FE-REV-B", 10086),
          ("rcftTypeRC906H-FEE1-MASTER-PRIVATE", 10088),
          ("rcftTypeRC602-GEF-REV-B-SLAVE", 10091),
          ("rcftTypeRC532-FE-REV-A-SLAVE", 10092),
          ("rcftTypeRC802-120L-REV-M", 10094),
          ("rcftTypeRC852-30-BL-REV-A", 10101),
          ("rcftTypeOPCOM200-OLP-T-REV-A", 10103),
          ("rcftTypeRC1102-E1-BL-REV-A2-MASTER", 10104),
          ("rcftTypeRC1102-V35-REV-A1-MASTER", 10106),
          ("rcftTypeRC904-V35FE1-REV-D", 10107),
          ("rcftTypeRC552-GE-REV-A-SLAVE", 10112),
          ("rcftTypeRC552-GE-REV-A-MASTER", 10113),
          ("rcftTypeRC902-FX4E1-BL-REV-B", 10122),
          ("rcftTypeRC1102-E1-BL-REV-A2-SLAVE", 10123),
          ("rcftTypeRC1102-V35-REV-A1-SLAVE", 10124),
          ("rcftTypeRC552-FE-REV-A-MASTER-NEW", 10125),
          ("rcftTypeRC802-120L-BL-REV-M", 10127),
          ("rcftTypeOPCOM200-OCP1-REV-A", 10128),
          ("rcftTypeRC552-FE-REV-A-SLAVE-NEW", 10130),
          ("rcftTypeRC1102-E1-SLAVE-REV-B1", 10131),
          ("rcftTypeRC1102-E1-MASTER-REV-B1", 10133),
          ("rcftTypeRC1102-E1-SLAVE-BL-REV-A1", 10136),
          ("rcftTypeRC1102-E1-MASTER-BL-REV-A1", 10137),
          ("rcftTypeRC602-GE-SLAVE-REV-B", 10138),
          ("rcftTypeRC602-GE-MASTER-REV-B", 10139),
          ("rcftTypeRC954-FE-4E1-REV-A", 10141),
          ("rcftTypeRC954-FX-4E1-REV-A", 10142),
          ("rcftTypeOPCOM200-OSC-REV-A", 10143),
          ("rcftTypeOPCOM200-OTU1-REV-B", 10144),
          ("rcftTypeRC602-GEF-REV-B-MASTER", 10145),
          ("rcftTypeRCVS1000-801A-1DD-REV-A", 10146),
          ("rcftTypeRCVS1000-601A-1DD-REV-A", 10147),
          ("rcftTypeOPCOM200-OTU2-REV-B", 10148),
          ("rcftTypeRC1102-E1-REV-B2-MASTER", 10153),
          ("rcftTypeRC1102-E1-REV-B2-SLAVE", 10154),
          ("rcftTypeRC902-FE4E1-BL-REV-A", 10159),
          ("rcftTypeRC802-DS3E3-REV-A", 10160),
          ("rcftTypeRC954-FE4E1-BL-REV-A", 10161),
          ("rcftTypeRC954-FX4E1-BL-REV-A", 10162),
          ("rcftTypeRC902-FX4E1-REV-B", 10163),
          ("rcftTypeRC954-2FE4E1-BL-REV-A", 10164),
          ("rcftTypeRC954-2FE8E1-BL-REV-A", 10166),
          ("rcftTypeOPCOM200-OLP-R-REV-A", 10167),
          ("rcftTypeRC954-FX8E1-REV-A-MASTER", 10169),
          ("rcftTypeRC954-FX8E1-REV-A-SLAVE", 10170),
          ("rcftTypeRC952-FE-DS1-MASTER-REV-A", 10172),
          ("rcftTypeRC852-30-REV-B-MASTER", 10175),
          ("rcftTypeRC952-FE-DS3E3-F-REV-A-MASTER", 10176),
          ("rcftTypeRC852-30-FV35-REV-B-MASTER", 10177),
          ("rcftTypeRC552-GE-REV-B-MASTER", 10181),
          ("rcftTypeRC552-GE-REV-B-SLAVE", 10182),
          ("rcftTypeRC952-FXE1-REV-C-MASTER", 10183),
          ("rcftTypeRC952-FEE1-REV-B-MASTER", 10184),
          ("rcftTypeRC552-GE-REV-C-MASTER", 10186),
          ("rcftTypeRC552-GE-REV-C-SLAVE", 10187),
          ("rcftTypeRC954-FE8E1-REV-A", 10188),
          ("rcftTypeRC952-FE-DS3E3-REV-A-MASTER", 10189),
          ("rcftTypeRC802-DS1-REV-A-MASTER", 10190),
          ("rcftTypeRC522E-FE-MASTER", 10194),
          ("rcftTypeRC522E-FE-SLAVE", 10197),
          ("rcftTypeRC904-V35FE1-E", 10198),
          ("rcftTypeRC552-FE-REV-B-MASTER", 10201),
          ("rcftTypeRC552-FE-REV-B-SLAVE", 10203),
          ("rcftTypeRC954-FE-4E1-REV-A-SLAVE", 11013),
          ("rcftTypeRC954-FX-4E1-REV-A-SLAVE", 11014),
          ("rcftTypeRC952-FE-DS3E3-REV-A-SLAVE", 11022),
          ("rcftTypeRC802-DS1-REV-A-SLAVE", 11023),
          ("rcftTypeRC952-FE-DS1-REV-A-SLAVE", 11024),
          ("rcftTypeRC952-FE-DS3E3-F-REV-A-SLAVE", 11026),
          ("rcftTypeRC852-30-REV-B-SLAVE", 11028),
          ("rcftTypeRC602E-GE-MASTER", 11031),
          ("rcftTypeRC602E-GE-SLAVE", 11032),
          ("rcftTypeRC954-2FE4E1-BL-REV-A-SLAVE", 12015),
          ("rcftTypeRC954-FE4E1-BL-REV-A-SLAVE", 12016),
          ("rcftTypeRC954-FX4E1-BL-REV-A-SLAVE", 12017),
          ("rcftTypeRC954-2FE8E1-BL-REV-A-SLAVE", 12018),
          ("rcftTypeRC802-DS3E3-REV-A-SLAVE", 12019),
          ("rcftTypeRC954-FE8E1-REV-A-SLAVE", 12020),
          ("rcftTypeRC832-30-REV-A-MASTER", 13055),
          ("rcftTypeRC832-30-FV35-REV-A-MASTER", 13056),
          ("rcftTypeRC832-60-REV-A-MASTER", 13057),
          ("rcftTypeRC832-120L-REV-A-MASTER", 13058),
          ("rcftTypeRC832-240L-REV-A-MASTER", 13059),
          ("rcftTypeRCMS2802-30FE-REV-A-MASTER", 13065),
          ("rcftTypeRCMS2802-60FE-REV-A-MASTER", 13066),
          ("rcftTypeRCMS2802-120LFE-REV-A-MASTER", 13070),
          ("rcftTypeRCMS2802-240LFE-REV-A-MASTER", 13071),
          ("rcftTypeRC832-30-FV35-REV-B-MASTER", 13072),
          ("rcftTypeRC804-30B-S1-REV-A-MASTER", 13073),
          ("rcftTypeRC806-30B-S1-REV-A-MASTER", 13074),
          ("rcftTypeRC832-30-FV35-REV-A1-MASTER", 13075),
          ("rcftTypeRCMS2802-2T1-FE-REV-A", 13081),
          ("rcftTypeRCMS2802-4T1-FE-REV-A", 13082),
          ("rcftTypeRCMS2802-8T1-FE-REV-A", 13083),
          ("rcftTypeRCMS2802-60FX-REV-A", 13084),
          ("rcftTypeRC1102-FE-REV-B-MASTER", 15001),
          ("rcftTypeRC1102-FE-4W-REV-A-MASTER", 15003),
          ("rcftTypeRC1102-FE-REV-B-SLAVE", 15005),
          ("rcftTypeRC1102-FE-4W-REV-A-SLAVE", 15006),
          ("rcftTypeRCMS2802-120LGE-BL-REV-A-MASTER", 17008),
          ("rcftTypeRCMS2802-240LGE-BL-REV-A-MASTER", 17011),
          ("rcftTypeRCMS2802-60GE-BL-REV-A-MASTER", 17099),
          ("rcftTypeRCMS2802-30GE-BL-REV-A-MASTER", 17100),
          ("rcftTypeRCMS2802-120LGE-BL-REV-A-SLAVE", 18008),
          ("rcftTypeRCMS2802-240LGE-BL-REV-A-SLAVE", 18011),
          ("rcftTypeRCMS2802-60GE-BL-REV-A-SLAVE", 18099),
          ("rcftTypeRCMS2802-30GE-BL-REV-A-SLAVE", 18100),
          ("rcftTypeRCMS2802-60GE-BL-REV-B-MASTER", 62469),
          ("rcftTypeRCMS2802-60GE-BL-REV-B-SLAVE", 62470),
          ("rcftTypeRC904-PE1-MSTER", 62512),
          ("rcftTypeRC904-PE1-SLAVE", 62513),
          ("rcftTypeRCMS2802-120LGE-BL-REV-B-MASTER", 62516),
          ("rcftTypeRCMS2802-120LGE-BL-REV-B-SLAVE", 62517),
          ("rcftTypeRCMS2802-240LGE-BL-REV-B-MASTER", 62519),
          ("rcftTypeRCMS2802-240LGE-BL-REV-B-SLAVE", 62520),
          ("rcftTypeRC958-FE4E1-REV-A-Master", 62523),
          ("rcftTypeRC958-FE4E1-REV-A-SLAVE", 62525),
          ("rcftTypeRC958-FE8E1-REV-A-MASTER", 62527),
          ("rcftTypeRC958-FE8E1-REV-A-SLAVE", 62528),
          ("rcftTypeRC958-FX4E1-REV-A-MASTER", 62530),
          ("rcftTypeRC958-FX4E1-REV-A-SLAVE", 62531),
          ("rcftTypeRC958-FX8E1-REV-A-MASTER", 62534),
          ("rcftTypeRC958-FX8E1-REV-A-SLAVE", 62535),
          ("rcftTypeRC908-FEV35-REV-A-MASTER", 62537),
          ("rcftTypeRC908-FEV35-REV-A-SLAVE", 62538),
          ("rcftTypeRC958-FEE1-REV-A-Master", 62541),
          ("rcftTypeRC958-FEE1-REV-A-SLAVE", 62542),
          ("rcftTypeRC958-FXE1-REV-A-MASTER", 62544),
          ("rcftTypeRC958-FXE1-REV-A-SLAVE", 62545),
          ("rcftTypeRC906G-FE4E1-MASTER", 62547),
          ("rcftTypeRC906G-FE4E1-SLAVE", 62548),
          ("rcftTypeRC906G-FX4E1-MASTER", 62551),
          ("rcftTypeRC906G-FX4E1-SLAVE", 62552),
          ("rcftTypeRC906G-FEE1-MASTER", 62555),
          ("rcftTypeRC906G-FEE1-SLAVE", 62556),
          ("rcftTypeRC906G-FXE1-MASTER", 62558),
          ("rcftTypeRC906G-FXE1-SLAVE", 62559),
          ("rcftTypeRC906G-FE8E1-MASTER", 62561),
          ("rcftTypeRC906G-FE8E1-SLAVE", 62562),
          ("rcftTypeRC906G-FX8E1-MASTER", 62564),
          ("rcftTypeRC906G-FX8E1-SLAVE", 62565),
          ("rcftTypeRC414-REV-B", 62568),
          ("rcftTypeRCVS1000-901NL", 62570),
          ("rcftTypeRCVS1000-901UL", 62572),
          ("rcftTypeRCMS2912-4E1T1GE-REV-A-MASTER", 62573),
          ("rcftTypeRCMS2912-4E1T1GE-REV-A-SLAVE", 62574),
          ("rcftTypeRCMS2912-8E1T1GE-REV-A-MASTER", 62576),
          ("rcftTypeRCMS2912-8E1T1GE-REV-A-SLAVE", 62577),
          ("rcftTypeOPCOM200_OTU1_A20", 62579),
          ("rcftTypeRC952-SE1M-MASTER", 62580),
          ("rcftTypeRC952-SE1M-SLAVE", 62581),
          ("rcftTypeRCMS2902-120LFE-MASTER", 62587),
          ("rcftTypeRCMS2902-120LFE-SLAVE", 62588),
          ("rcftTypeRCMS2902-240LFE-MASTER", 62590),
          ("rcftTypeRCMS2902-240LFE-SLAVE", 62591),
          ("rcftTypeRCMS2902-60FE-MASTER", 62593),
          ("rcftTypeRCMS2902-60FE-SLAVE", 62594),
          ("rcftTypeRC862-60-MASTER", 62596),
          ("rcftTypeRC862-60-SLAVE", 62597),
          ("rcftTypeRC862-30-MASTER", 62601),
          ("rcftTypeRC862-30-SLAVE", 62602),
          ("rcftTypeRC952-CSE1M-MASTER", 62604),
          ("rcftTypeRC952-CSE1M-SLAVE", 62605),
          ("rcftTypeRCMS2912-480FE-MASTER", 62609),
          ("rcftTypeRCMS2912-480FE-SLAVE", 62610),
          ("rcftTypeRCMS2912-240FE-MASTER", 62612),
          ("rcftTypeRCMS2912-240FE-SLAVE", 62613),
          ("rcftTypeRCVS1000-604AL", 162466),
          ("rcftTypeRCVS1000-602BL", 162467),
          ("rcftTypeRCVS1000-601BL", 162468))
    )


_RcftSlotType_Type.__name__ = "Integer32"
_RcftSlotType_Object = MibTableColumn
rcftSlotType = _RcftSlotType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 3),
    _RcftSlotType_Type()
)
rcftSlotType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftSlotType.setStatus("current")


class _RcftSlotFaultPass_Type(Integer32):
    """Custom type rcftSlotFaultPass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("support", 1),
          ("notSupport", 2))
    )


_RcftSlotFaultPass_Type.__name__ = "Integer32"
_RcftSlotFaultPass_Object = MibTableColumn
rcftSlotFaultPass = _RcftSlotFaultPass_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 4),
    _RcftSlotFaultPass_Type()
)
rcftSlotFaultPass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftSlotFaultPass.setStatus("current")


class _RcftSlotVLAN_Type(Integer32):
    """Custom type rcftSlotVLAN based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("support", 1),
          ("notSupport", 2))
    )


_RcftSlotVLAN_Type.__name__ = "Integer32"
_RcftSlotVLAN_Object = MibTableColumn
rcftSlotVLAN = _RcftSlotVLAN_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 5),
    _RcftSlotVLAN_Type()
)
rcftSlotVLAN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftSlotVLAN.setStatus("current")


class _RcftSlotConfigStatus_Type(Integer32):
    """Custom type rcftSlotConfigStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("abnormal", 2))
    )


_RcftSlotConfigStatus_Type.__name__ = "Integer32"
_RcftSlotConfigStatus_Object = MibTableColumn
rcftSlotConfigStatus = _RcftSlotConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 6),
    _RcftSlotConfigStatus_Type()
)
rcftSlotConfigStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftSlotConfigStatus.setStatus("current")


class _RcftSlotELink_Type(Integer32):
    """Custom type rcftSlotELink based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("linkup", 1),
          ("linkdown", 2))
    )


_RcftSlotELink_Type.__name__ = "Integer32"
_RcftSlotELink_Object = MibTableColumn
rcftSlotELink = _RcftSlotELink_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 7),
    _RcftSlotELink_Type()
)
rcftSlotELink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftSlotELink.setStatus("current")


class _RcftSlotEAutoNegotiation_Type(Integer32):
    """Custom type rcftSlotEAutoNegotiation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("manul", 2))
    )


_RcftSlotEAutoNegotiation_Type.__name__ = "Integer32"
_RcftSlotEAutoNegotiation_Object = MibTableColumn
rcftSlotEAutoNegotiation = _RcftSlotEAutoNegotiation_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 8),
    _RcftSlotEAutoNegotiation_Type()
)
rcftSlotEAutoNegotiation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftSlotEAutoNegotiation.setStatus("current")


class _RcftSlotEDuplex_Type(Integer32):
    """Custom type rcftSlotEDuplex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("full-duplex", 1),
          ("half-duplex", 2),
          ("auto", 3))
    )


_RcftSlotEDuplex_Type.__name__ = "Integer32"
_RcftSlotEDuplex_Object = MibTableColumn
rcftSlotEDuplex = _RcftSlotEDuplex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 9),
    _RcftSlotEDuplex_Type()
)
rcftSlotEDuplex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftSlotEDuplex.setStatus("current")


class _RcftSlotECollCount_Type(Integer32):
    """Custom type rcftSlotECollCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("exist", 1),
          ("notExist", 2))
    )


_RcftSlotECollCount_Type.__name__ = "Integer32"
_RcftSlotECollCount_Object = MibTableColumn
rcftSlotECollCount = _RcftSlotECollCount_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 10),
    _RcftSlotECollCount_Type()
)
rcftSlotECollCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftSlotECollCount.setStatus("current")


class _RcftSlotESpeed_Type(Integer32):
    """Custom type rcftSlotESpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              16)
        )
    )
    namedValues = NamedValues(
        *(("rcft10Mbps", 1),
          ("rcft100Mbps", 2),
          ("rcft1000Mbps", 3),
          ("rcft10Gbps", 4),
          ("other", 16))
    )


_RcftSlotESpeed_Type.__name__ = "Integer32"
_RcftSlotESpeed_Object = MibTableColumn
rcftSlotESpeed = _RcftSlotESpeed_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 11),
    _RcftSlotESpeed_Type()
)
rcftSlotESpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftSlotESpeed.setStatus("current")


class _RcftSlotETxStatus_Type(Integer32):
    """Custom type rcftSlotETxStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("package", 1),
          ("noPackage", 2))
    )


_RcftSlotETxStatus_Type.__name__ = "Integer32"
_RcftSlotETxStatus_Object = MibTableColumn
rcftSlotETxStatus = _RcftSlotETxStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 12),
    _RcftSlotETxStatus_Type()
)
rcftSlotETxStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftSlotETxStatus.setStatus("current")


class _RcftSlotERxStatus_Type(Integer32):
    """Custom type rcftSlotERxStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("package", 1),
          ("noPackage", 2))
    )


_RcftSlotERxStatus_Type.__name__ = "Integer32"
_RcftSlotERxStatus_Object = MibTableColumn
rcftSlotERxStatus = _RcftSlotERxStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 13),
    _RcftSlotERxStatus_Type()
)
rcftSlotERxStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftSlotERxStatus.setStatus("current")


class _RcftSlotOLink_Type(Integer32):
    """Custom type rcftSlotOLink based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("linkup", 1),
          ("linkdown", 2))
    )


_RcftSlotOLink_Type.__name__ = "Integer32"
_RcftSlotOLink_Object = MibTableColumn
rcftSlotOLink = _RcftSlotOLink_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 14),
    _RcftSlotOLink_Type()
)
rcftSlotOLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftSlotOLink.setStatus("current")


class _RcftSlotODuplex_Type(Integer32):
    """Custom type rcftSlotODuplex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("full-duplex", 1),
          ("half-duplex", 2),
          ("auto", 3))
    )


_RcftSlotODuplex_Type.__name__ = "Integer32"
_RcftSlotODuplex_Object = MibTableColumn
rcftSlotODuplex = _RcftSlotODuplex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 15),
    _RcftSlotODuplex_Type()
)
rcftSlotODuplex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftSlotODuplex.setStatus("current")


class _RcftSlotOSpeed_Type(Integer32):
    """Custom type rcftSlotOSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              16)
        )
    )
    namedValues = NamedValues(
        *(("rcft10Mbps", 1),
          ("rcft100Mbps", 2),
          ("rcft1GBps", 3),
          ("rcft10Gbps", 4),
          ("other", 16))
    )


_RcftSlotOSpeed_Type.__name__ = "Integer32"
_RcftSlotOSpeed_Object = MibTableColumn
rcftSlotOSpeed = _RcftSlotOSpeed_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 16),
    _RcftSlotOSpeed_Type()
)
rcftSlotOSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftSlotOSpeed.setStatus("current")


class _RcftSlotOTxStatus_Type(Integer32):
    """Custom type rcftSlotOTxStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("package", 1),
          ("noPackage", 2))
    )


_RcftSlotOTxStatus_Type.__name__ = "Integer32"
_RcftSlotOTxStatus_Object = MibTableColumn
rcftSlotOTxStatus = _RcftSlotOTxStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 17),
    _RcftSlotOTxStatus_Type()
)
rcftSlotOTxStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftSlotOTxStatus.setStatus("current")


class _RcftSlotORxStatus_Type(Integer32):
    """Custom type rcftSlotORxStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("package", 1),
          ("noPackage", 2))
    )


_RcftSlotORxStatus_Type.__name__ = "Integer32"
_RcftSlotORxStatus_Object = MibTableColumn
rcftSlotORxStatus = _RcftSlotORxStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 18),
    _RcftSlotORxStatus_Type()
)
rcftSlotORxStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftSlotORxStatus.setStatus("current")


class _RcftSlotDescr_Type(OctetString):
    """Custom type rcftSlotDescr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_RcftSlotDescr_Type.__name__ = "OctetString"
_RcftSlotDescr_Object = MibTableColumn
rcftSlotDescr = _RcftSlotDescr_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 19),
    _RcftSlotDescr_Type()
)
rcftSlotDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftSlotDescr.setStatus("current")


class _RcftSlotORLnk_Type(Integer32):
    """Custom type rcftSlotORLnk based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("linkup", 1),
          ("linkdown", 2))
    )


_RcftSlotORLnk_Type.__name__ = "Integer32"
_RcftSlotORLnk_Object = MibTableColumn
rcftSlotORLnk = _RcftSlotORLnk_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 20),
    _RcftSlotORLnk_Type()
)
rcftSlotORLnk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftSlotORLnk.setStatus("current")


class _RcftSlotOTLnk_Type(Integer32):
    """Custom type rcftSlotOTLnk based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("linkup", 1),
          ("linkdown", 2))
    )


_RcftSlotOTLnk_Type.__name__ = "Integer32"
_RcftSlotOTLnk_Object = MibTableColumn
rcftSlotOTLnk = _RcftSlotOTLnk_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 21),
    _RcftSlotOTLnk_Type()
)
rcftSlotOTLnk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftSlotOTLnk.setStatus("current")


class _RcftSlotORmd_Type(Integer32):
    """Custom type rcftSlotORmd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("package", 1),
          ("nopackage", 2))
    )


_RcftSlotORmd_Type.__name__ = "Integer32"
_RcftSlotORmd_Object = MibTableColumn
rcftSlotORmd = _RcftSlotORmd_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 22),
    _RcftSlotORmd_Type()
)
rcftSlotORmd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftSlotORmd.setStatus("current")


class _RcftSlotOFxAct_Type(Integer32):
    """Custom type rcftSlotOFxAct based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("package", 1),
          ("nopackage", 2))
    )


_RcftSlotOFxAct_Type.__name__ = "Integer32"
_RcftSlotOFxAct_Object = MibTableColumn
rcftSlotOFxAct = _RcftSlotOFxAct_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 23),
    _RcftSlotOFxAct_Type()
)
rcftSlotOFxAct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftSlotOFxAct.setStatus("current")


class _RcftSlotETxAct_Type(Integer32):
    """Custom type rcftSlotETxAct based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("package", 1),
          ("nopackage", 2))
    )


_RcftSlotETxAct_Type.__name__ = "Integer32"
_RcftSlotETxAct_Object = MibTableColumn
rcftSlotETxAct = _RcftSlotETxAct_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 24),
    _RcftSlotETxAct_Type()
)
rcftSlotETxAct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftSlotETxAct.setStatus("current")


class _RcftSlotRemManage_Type(Integer32):
    """Custom type rcftSlotRemManage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("manage-enable", 1),
          ("manage-disable", 2))
    )


_RcftSlotRemManage_Type.__name__ = "Integer32"
_RcftSlotRemManage_Object = MibTableColumn
rcftSlotRemManage = _RcftSlotRemManage_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 25),
    _RcftSlotRemManage_Type()
)
rcftSlotRemManage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftSlotRemManage.setStatus("current")


class _RcftSlotLBKTest_Type(Integer32):
    """Custom type rcftSlotLBKTest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("loopbacktest-enable", 1),
          ("loopbacktest-disable", 2))
    )


_RcftSlotLBKTest_Type.__name__ = "Integer32"
_RcftSlotLBKTest_Object = MibTableColumn
rcftSlotLBKTest = _RcftSlotLBKTest_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 26),
    _RcftSlotLBKTest_Type()
)
rcftSlotLBKTest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftSlotLBKTest.setStatus("current")


class _RcftSlotVOLimit_Type(Integer32):
    """Custom type rcftSlotVOLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("voltageoverlimit", 2))
    )


_RcftSlotVOLimit_Type.__name__ = "Integer32"
_RcftSlotVOLimit_Object = MibTableColumn
rcftSlotVOLimit = _RcftSlotVOLimit_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 27),
    _RcftSlotVOLimit_Type()
)
rcftSlotVOLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftSlotVOLimit.setStatus("current")


class _RcftSlotVBLimit_Type(Integer32):
    """Custom type rcftSlotVBLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("voltagebelowlimit", 2))
    )


_RcftSlotVBLimit_Type.__name__ = "Integer32"
_RcftSlotVBLimit_Object = MibTableColumn
rcftSlotVBLimit = _RcftSlotVBLimit_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 28),
    _RcftSlotVBLimit_Type()
)
rcftSlotVBLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftSlotVBLimit.setStatus("current")


class _RcftSlotLBKTestOk_Type(Integer32):
    """Custom type rcftSlotLBKTestOk based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("loopbacktestok", 1),
          ("loopbacktestfault", 2))
    )


_RcftSlotLBKTestOk_Type.__name__ = "Integer32"
_RcftSlotLBKTestOk_Object = MibTableColumn
rcftSlotLBKTestOk = _RcftSlotLBKTestOk_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 29),
    _RcftSlotLBKTestOk_Type()
)
rcftSlotLBKTestOk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftSlotLBKTestOk.setStatus("current")


class _RcftSlotEPort_Type(Integer32):
    """Custom type rcftSlotEPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("open", 1),
          ("close", 2))
    )


_RcftSlotEPort_Type.__name__ = "Integer32"
_RcftSlotEPort_Object = MibTableColumn
rcftSlotEPort = _RcftSlotEPort_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 30),
    _RcftSlotEPort_Type()
)
rcftSlotEPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftSlotEPort.setStatus("current")


class _RcftSlotOSendPower_Type(Integer32):
    """Custom type rcftSlotOSendPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("abnormal", 2))
    )


_RcftSlotOSendPower_Type.__name__ = "Integer32"
_RcftSlotOSendPower_Object = MibTableColumn
rcftSlotOSendPower = _RcftSlotOSendPower_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 31),
    _RcftSlotOSendPower_Type()
)
rcftSlotOSendPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftSlotOSendPower.setStatus("current")


class _RcftSlotOReceSen_Type(Integer32):
    """Custom type rcftSlotOReceSen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("abnormal", 2))
    )


_RcftSlotOReceSen_Type.__name__ = "Integer32"
_RcftSlotOReceSen_Object = MibTableColumn
rcftSlotOReceSen = _RcftSlotOReceSen_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 32),
    _RcftSlotOReceSen_Type()
)
rcftSlotOReceSen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftSlotOReceSen.setStatus("current")


class _RcftSlotOLaser_Type(Integer32):
    """Custom type rcftSlotOLaser based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("abnormal", 2))
    )


_RcftSlotOLaser_Type.__name__ = "Integer32"
_RcftSlotOLaser_Object = MibTableColumn
rcftSlotOLaser = _RcftSlotOLaser_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 33),
    _RcftSlotOLaser_Type()
)
rcftSlotOLaser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftSlotOLaser.setStatus("current")


class _RcftSlotOSD_Type(Integer32):
    """Custom type rcftSlotOSD based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("abnormal", 2))
    )


_RcftSlotOSD_Type.__name__ = "Integer32"
_RcftSlotOSD_Object = MibTableColumn
rcftSlotOSD = _RcftSlotOSD_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 34),
    _RcftSlotOSD_Type()
)
rcftSlotOSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftSlotOSD.setStatus("current")


class _RcftSlotOPort_Type(Integer32):
    """Custom type rcftSlotOPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("open", 1),
          ("close", 2))
    )


_RcftSlotOPort_Type.__name__ = "Integer32"
_RcftSlotOPort_Object = MibTableColumn
rcftSlotOPort = _RcftSlotOPort_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 35),
    _RcftSlotOPort_Type()
)
rcftSlotOPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftSlotOPort.setStatus("current")


class _RcftSlotOrder_Type(Integer32):
    """Custom type rcftSlotOrder based on Integer32"""
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
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              50,
              51,
              52,
              53,
              54,
              55,
              56,
              57,
              58,
              59,
              60,
              61,
              62,
              63,
              64,
              65,
              66,
              67,
              68,
              69,
              70,
              71,
              72,
              73,
              74,
              75,
              76,
              77,
              78,
              79,
              80,
              81,
              82,
              83,
              84,
              85,
              86,
              87,
              88,
              89,
              90,
              91,
              92,
              93,
              94,
              95,
              96,
              97,
              98,
              99,
              100,
              101,
              102,
              103,
              104,
              105,
              106,
              107,
              108,
              109,
              110,
              111,
              112,
              113,
              114,
              115,
              116,
              117,
              118,
              119)
        )
    )
    namedValues = NamedValues(
        *(("localreset", 1),
          ("olooptestenable", 2),
          ("olooptestdisable", 3),
          ("v35looptestenable", 4),
          ("v35looptestdisable", 5),
          ("e1port1remotelooptestenable", 6),
          ("e1port1remotelooptestdisable", 7),
          ("e1locallooptestenable", 8),
          ("e1locallooptestdisable", 9),
          ("v35remotelooptestenable", 10),
          ("v35remotelooptestdisable", 11),
          ("e1port2remotelooptestenable", 12),
          ("e1port2remotelooptestdisable", 13),
          ("eltwoportremotelooptestenable", 14),
          ("e1twoportremotelooptestdisable", 15),
          ("resetLocalEthPort", 16),
          ("resetRemoteEthPort", 17),
          ("resetLocalRemoteEthPort", 18),
          ("allE1RemoteLoop", 19),
          ("allE1RemoteNormal", 20),
          ("localInsideLoopEnable", 21),
          ("localInsideLoopDisable", 22),
          ("remoteOutsideLoopEnable", 23),
          ("remoteOutsideLoopDisable", 24),
          ("localDoubleLoopEnable", 25),
          ("localDoubleLoopDisable", 26),
          ("cwdmClientLoopEnable", 27),
          ("cwdmClientLoopDisable", 28),
          ("cwdmLineLoopEnable", 29),
          ("cwdmLineLoopDisable", 30),
          ("cwdmcdrReset", 31),
          ("e1port1DoubleLoopEnable", 32),
          ("e1port2DoubleLoopEnable", 33),
          ("startRequestInfo", 34),
          ("stopRequestInfo", 35),
          ("errCodeFunctionOpen", 36),
          ("errCodeFunctionClose", 37),
          ("remoteDoubleLoopDisable", 38),
          ("linePortInsideLoopEnable", 39),
          ("linePortOutsideLoopEnable", 40),
          ("linePortInsideLoopDisable", 41),
          ("linePortOutsideLoopDisable", 42),
          ("remoteInsideLoopEnable", 43),
          ("remoteInsideLoopDisable", 44),
          ("e1port1OutsideLoopEnable", 45),
          ("e1port2OutsideLoopEnable", 46),
          ("e1port3OutsideLoopEnable", 47),
          ("e1port4OutsideLoopEnable", 48),
          ("allE1OutsideLoopEnable", 49),
          ("allE1OutsideLoopDisable", 50),
          ("e1port1InsideLoopEnable", 51),
          ("e1port2InsideLoopEnable", 52),
          ("e1port3InsideLoopEnable", 53),
          ("e1port4InsideLoopEnable", 54),
          ("allE1InsideLoopEnable", 55),
          ("allE1InsideLoopDisable", 56),
          ("opticalRateAjustEnable", 57),
          ("opticalRateAjustDisable", 58),
          ("e1port1OutsideLoopDisable", 59),
          ("e1port2OutsideLoopDisable", 60),
          ("e1port3OutsideLoopDisable", 61),
          ("e1port4OutsideLoopDisable", 62),
          ("remotee1port1OutsideLoopEnable", 63),
          ("remotee1port2OutsideLoopEnable", 64),
          ("remotee1port3OutsideLoopEnable", 65),
          ("remotee1port4OutsideLoopEnable", 66),
          ("remoteallE1OutsideLoopEnable", 67),
          ("remotee1port1OutsideLoopDisable", 68),
          ("remotee1port2OutsideLoopDisable", 69),
          ("remotee1port3OutsideLoopDisable", 70),
          ("remotee1port4OutsideLoopDisable", 71),
          ("remoteallE1OutsideLoopDisable", 72),
          ("e1port1errCodeFunctionOpen", 73),
          ("e1port2errCodeFunctionOpen", 74),
          ("e1port3errCodeFunctionOpen", 75),
          ("e1port4errCodeFunctionOpen", 76),
          ("allE1errCodeFunctionOpen", 77),
          ("e1port1errCodeFunctionClose", 78),
          ("e1port2errCodeFunctionClose", 79),
          ("e1port3errCodeFunctionClose", 80),
          ("e1port4errCodeFunctionClose", 81),
          ("allE1errCodeFunctionClose", 82),
          ("remoteE1Port1InsideLoopEnable", 83),
          ("remoteE1Port2InsideLoopEnable", 84),
          ("remoteE1Port3InsideLoopEnable", 85),
          ("remoteE1Port4InsideLoopEnable", 86),
          ("remoteAllE1InsideLoopEnable", 87),
          ("remoteE1Port1InsideLoopDisable", 88),
          ("remoteE1Port2InsideLoopDisable", 89),
          ("remoteE1Port3InsideLoopDisable", 90),
          ("remoteE1Port4InsideLoopDisable", 91),
          ("remoteAllE1InsideLoopDisable", 92),
          ("e1port5OutsideLoopEnable", 93),
          ("e1port6OutsideLoopEnable", 94),
          ("e1port7OutsideLoopEnable", 95),
          ("e1port8OutsideLoopEnable", 96),
          ("e1port5OutsideLoopDisable", 97),
          ("e1port6OutsideLoopDisable", 98),
          ("e1port7OutsideLoopDisable", 99),
          ("e1port8OutsideLoopDisable", 100),
          ("remotee5port1OutsideLoopEnable", 101),
          ("remotee6port2OutsideLoopEnable", 102),
          ("remotee7port3OutsideLoopEnable", 103),
          ("remotee8port4OutsideLoopEnable", 104),
          ("remotee5port1OutsideLoopDisable", 105),
          ("remotee6port2OutsideLoopDisable", 106),
          ("remotee7port3OutsideLoopDisable", 107),
          ("remotee8port4OutsideLoopDisable", 108),
          ("e1port5errCodeFunctionOpen", 109),
          ("e1port6errCodeFunctionOpen", 110),
          ("e1port7errCodeFunctionOpen", 111),
          ("e1port8errCodeFunctionOpen", 112),
          ("e1port5errCodeFunctionClose", 113),
          ("e1port6errCodeFunctionClose", 114),
          ("e1port7errCodeFunctionClose", 115),
          ("e1port8errCodeFunctionClose", 116),
          ("e1UnUsedAlarmMask", 117),
          ("e1UnUsedAlarmUnMask", 118),
          ("localStatisticsClear", 119))
    )


_RcftSlotOrder_Type.__name__ = "Integer32"
_RcftSlotOrder_Object = MibTableColumn
rcftSlotOrder = _RcftSlotOrder_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 36),
    _RcftSlotOrder_Type()
)
rcftSlotOrder.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftSlotOrder.setStatus("current")


class _RcftRSlotExist_Type(Integer32):
    """Custom type rcftRSlotExist based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("exist", 1),
          ("notExist", 2))
    )


_RcftRSlotExist_Type.__name__ = "Integer32"
_RcftRSlotExist_Object = MibTableColumn
rcftRSlotExist = _RcftRSlotExist_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 37),
    _RcftRSlotExist_Type()
)
rcftRSlotExist.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRSlotExist.setStatus("current")


class _RcftRSlotEAutoNegotiation_Type(Integer32):
    """Custom type rcftRSlotEAutoNegotiation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("manul", 2))
    )


_RcftRSlotEAutoNegotiation_Type.__name__ = "Integer32"
_RcftRSlotEAutoNegotiation_Object = MibTableColumn
rcftRSlotEAutoNegotiation = _RcftRSlotEAutoNegotiation_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 38),
    _RcftRSlotEAutoNegotiation_Type()
)
rcftRSlotEAutoNegotiation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftRSlotEAutoNegotiation.setStatus("current")


class _RcftRSlotEDuplex_Type(Integer32):
    """Custom type rcftRSlotEDuplex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("full-duplex", 1),
          ("half-duplex", 2),
          ("auto", 3))
    )


_RcftRSlotEDuplex_Type.__name__ = "Integer32"
_RcftRSlotEDuplex_Object = MibTableColumn
rcftRSlotEDuplex = _RcftRSlotEDuplex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 39),
    _RcftRSlotEDuplex_Type()
)
rcftRSlotEDuplex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftRSlotEDuplex.setStatus("current")


class _RcftRSlotELink_Type(Integer32):
    """Custom type rcftRSlotELink based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("linkup", 1),
          ("linkdown", 2))
    )


_RcftRSlotELink_Type.__name__ = "Integer32"
_RcftRSlotELink_Object = MibTableColumn
rcftRSlotELink = _RcftRSlotELink_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 40),
    _RcftRSlotELink_Type()
)
rcftRSlotELink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRSlotELink.setStatus("current")


class _RcftRSlotFaultPass_Type(Integer32):
    """Custom type rcftRSlotFaultPass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("support", 1),
          ("notSupport", 2))
    )


_RcftRSlotFaultPass_Type.__name__ = "Integer32"
_RcftRSlotFaultPass_Object = MibTableColumn
rcftRSlotFaultPass = _RcftRSlotFaultPass_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 41),
    _RcftRSlotFaultPass_Type()
)
rcftRSlotFaultPass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftRSlotFaultPass.setStatus("current")


class _RcftRSlotEPort_Type(Integer32):
    """Custom type rcftRSlotEPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("open", 1),
          ("close", 2))
    )


_RcftRSlotEPort_Type.__name__ = "Integer32"
_RcftRSlotEPort_Object = MibTableColumn
rcftRSlotEPort = _RcftRSlotEPort_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 42),
    _RcftRSlotEPort_Type()
)
rcftRSlotEPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftRSlotEPort.setStatus("current")


class _RcftRSlotRemManage_Type(Integer32):
    """Custom type rcftRSlotRemManage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("manage-enable", 1),
          ("manage-disable", 2))
    )


_RcftRSlotRemManage_Type.__name__ = "Integer32"
_RcftRSlotRemManage_Object = MibTableColumn
rcftRSlotRemManage = _RcftRSlotRemManage_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 43),
    _RcftRSlotRemManage_Type()
)
rcftRSlotRemManage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftRSlotRemManage.setStatus("current")


class _RcftRSlotVOLimit_Type(Integer32):
    """Custom type rcftRSlotVOLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("voltageoverlimit", 2))
    )


_RcftRSlotVOLimit_Type.__name__ = "Integer32"
_RcftRSlotVOLimit_Object = MibTableColumn
rcftRSlotVOLimit = _RcftRSlotVOLimit_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 44),
    _RcftRSlotVOLimit_Type()
)
rcftRSlotVOLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRSlotVOLimit.setStatus("current")


class _RcftRSlotVBLimit_Type(Integer32):
    """Custom type rcftRSlotVBLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("voltagebelowlimit", 2))
    )


_RcftRSlotVBLimit_Type.__name__ = "Integer32"
_RcftRSlotVBLimit_Object = MibTableColumn
rcftRSlotVBLimit = _RcftRSlotVBLimit_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 45),
    _RcftRSlotVBLimit_Type()
)
rcftRSlotVBLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRSlotVBLimit.setStatus("current")


class _RcftRSlotOSendPower_Type(Integer32):
    """Custom type rcftRSlotOSendPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("abnormal", 2))
    )


_RcftRSlotOSendPower_Type.__name__ = "Integer32"
_RcftRSlotOSendPower_Object = MibTableColumn
rcftRSlotOSendPower = _RcftRSlotOSendPower_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 46),
    _RcftRSlotOSendPower_Type()
)
rcftRSlotOSendPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRSlotOSendPower.setStatus("current")


class _RcftRSlotOReceSen_Type(Integer32):
    """Custom type rcftRSlotOReceSen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("abnormal", 2))
    )


_RcftRSlotOReceSen_Type.__name__ = "Integer32"
_RcftRSlotOReceSen_Object = MibTableColumn
rcftRSlotOReceSen = _RcftRSlotOReceSen_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 47),
    _RcftRSlotOReceSen_Type()
)
rcftRSlotOReceSen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRSlotOReceSen.setStatus("current")


class _RcftRSlotOLaser_Type(Integer32):
    """Custom type rcftRSlotOLaser based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("abnormal", 2))
    )


_RcftRSlotOLaser_Type.__name__ = "Integer32"
_RcftRSlotOLaser_Object = MibTableColumn
rcftRSlotOLaser = _RcftRSlotOLaser_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 48),
    _RcftRSlotOLaser_Type()
)
rcftRSlotOLaser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRSlotOLaser.setStatus("current")


class _RcftRSlotOSD_Type(Integer32):
    """Custom type rcftRSlotOSD based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("abnormal", 2))
    )


_RcftRSlotOSD_Type.__name__ = "Integer32"
_RcftRSlotOSD_Object = MibTableColumn
rcftRSlotOSD = _RcftRSlotOSD_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 49),
    _RcftRSlotOSD_Type()
)
rcftRSlotOSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRSlotOSD.setStatus("current")


class _RcftRSlotOLink_Type(Integer32):
    """Custom type rcftRSlotOLink based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("link", 1),
          ("unlink", 2))
    )


_RcftRSlotOLink_Type.__name__ = "Integer32"
_RcftRSlotOLink_Object = MibTableColumn
rcftRSlotOLink = _RcftRSlotOLink_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 50),
    _RcftRSlotOLink_Type()
)
rcftRSlotOLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRSlotOLink.setStatus("current")


class _RcftRSlotOrder_Type(Integer32):
    """Custom type rcftRSlotOrder based on Integer32"""
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
              12,
              13,
              14,
              15,
              25,
              26,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              45,
              46,
              47,
              48,
              49,
              50,
              51,
              52,
              53,
              54,
              55,
              56,
              57,
              58,
              59,
              60,
              61,
              62,
              63,
              64,
              65,
              66,
              67,
              68,
              69,
              70,
              71,
              72)
        )
    )
    namedValues = NamedValues(
        *(("remotereset", 1),
          ("resetEthPort", 2),
          ("localInsideLoopEnable", 3),
          ("localInsideLoopDisable", 4),
          ("e1port1LocalOutsideLoopEnable", 5),
          ("e1port1LocalOutsideLoopDisable", 6),
          ("pollingTemperature", 7),
          ("e1port2Locallooptestenable", 12),
          ("e1port2Locallooptestdisable", 13),
          ("eltwoportLocallooptestenable", 14),
          ("e1twoportLocallooptestdisable", 15),
          ("localDoubleLoopEnable", 25),
          ("localDoubleLoopDisable", 26),
          ("e1port1DoubleLoopEnable", 32),
          ("e1port2DoubleLoopEnable", 33),
          ("requestInfoStart", 34),
          ("requestInfoStop", 35),
          ("errCodeFunctionOpen", 36),
          ("errCodeFunctionClose", 37),
          ("remoteDoubleLoopDisable", 38),
          ("linePortInsideLoopEnable", 39),
          ("linePortOutsideLoopEnable", 40),
          ("linePortInsideLoopDisable", 41),
          ("linePortOutsideLoopDisable", 42),
          ("localV35InsideLoopEnable", 43),
          ("e1port1OutsideLoopEnable", 45),
          ("e1port2OutsideLoopEnable", 46),
          ("e1port3OutsideLoopEnable", 47),
          ("e1port4OutsideLoopEnable", 48),
          ("allE1OutsideLoopEnable", 49),
          ("allE1OutsideLoopDisable", 50),
          ("e1port1InsideLoopEnable", 51),
          ("e1port2InsideLoopEnable", 52),
          ("e1port3InsideLoopEnable", 53),
          ("e1port4InsideLoopEnable", 54),
          ("allE1InsideLoopEnable", 55),
          ("allE1InsideLoopDisable", 56),
          ("saveDeviceConfig", 57),
          ("deleteDeviceConfig", 58),
          ("maskUnusedE1Alarm", 59),
          ("unmaskUnusedAlarm", 60),
          ("deviceRestart", 61),
          ("localE1Port1InsideLoopEnable", 62),
          ("localE1Port2InsideLoopEnable", 63),
          ("localE1Port3InsideLoopEnable", 64),
          ("localE1Port4InsideLoopEnable", 65),
          ("localAllE1PortInsideLoopEnable", 66),
          ("localE1Port1InsideLoopDisable", 67),
          ("localE1Port2InsideLoopDisable", 68),
          ("localE1Port3InsideLoopDisable", 69),
          ("localE1Port4InsideLoopDisable", 70),
          ("localAllE1PortInsideLoopDisable", 71),
          ("allE1PortLoopDisable", 72))
    )


_RcftRSlotOrder_Type.__name__ = "Integer32"
_RcftRSlotOrder_Object = MibTableColumn
rcftRSlotOrder = _RcftRSlotOrder_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 51),
    _RcftRSlotOrder_Type()
)
rcftRSlotOrder.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftRSlotOrder.setStatus("current")


class _RcftSlotRowStatus_Type(Integer32):
    """Custom type rcftSlotRowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("active", 1)
    )


_RcftSlotRowStatus_Type.__name__ = "Integer32"
_RcftSlotRowStatus_Object = MibTableColumn
rcftSlotRowStatus = _RcftSlotRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 52),
    _RcftSlotRowStatus_Type()
)
rcftSlotRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftSlotRowStatus.setStatus("current")


class _RcftRSlotType_Type(Integer32):
    """Custom type rcftRSlotType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(60,
              68,
              96,
              97,
              98,
              99,
              108,
              109,
              110,
              111,
              120,
              160,
              161,
              162,
              163,
              168,
              169,
              170,
              171,
              176,
              177,
              178,
              179,
              212,
              213,
              214,
              215,
              220,
              221,
              222,
              223,
              232,
              233,
              234,
              235,
              244,
              245,
              246,
              247,
              308,
              309,
              310,
              311,
              316,
              317,
              318,
              319,
              324,
              325,
              326,
              327,
              352,
              353,
              354,
              355,
              356,
              357,
              358,
              359,
              364,
              365,
              366,
              367,
              384,
              385,
              386,
              387,
              388,
              389,
              390,
              391,
              392,
              393,
              394,
              395,
              396,
              397,
              398,
              399,
              420,
              421,
              422,
              423,
              472,
              473,
              474,
              475,
              484,
              485,
              486,
              487,
              492,
              493,
              494,
              495,
              496,
              497,
              498,
              499,
              504,
              505,
              506,
              507,
              528,
              529,
              530,
              531,
              552,
              553,
              554,
              555,
              560,
              561,
              562,
              563,
              612,
              613,
              614,
              615,
              632,
              633,
              634,
              635,
              636,
              637,
              638,
              639,
              696,
              700,
              704,
              708,
              712,
              716,
              720,
              724,
              725,
              726,
              727,
              732,
              733,
              734,
              735,
              736,
              737,
              738,
              739,
              740,
              744,
              745,
              746,
              747,
              748,
              749,
              750,
              751,
              808,
              999,
              1000,
              1001,
              1002,
              1003,
              1004,
              1005,
              1006,
              1007,
              1008,
              1009,
              1010,
              1011,
              1012,
              1013,
              1014,
              1015,
              1016,
              1017,
              1018,
              1019,
              1020,
              1021,
              1022,
              1023,
              1024,
              1025,
              1026,
              1027,
              1028,
              1029,
              1030,
              1031,
              1032,
              1033,
              1034,
              1035,
              1036,
              1037,
              1038,
              1039,
              1040,
              1041,
              1042,
              1043,
              1044,
              1045,
              1046,
              1047,
              1048,
              1049,
              1050,
              1051,
              1052,
              1053,
              1054,
              1055,
              1056,
              1057,
              1058,
              1059,
              1060,
              1061,
              1062,
              1063,
              1064,
              1065,
              1066,
              1067,
              1068,
              1072,
              1076,
              1080,
              1084,
              1088,
              1092,
              1096,
              1100,
              10001,
              10005,
              10008,
              10009,
              10010,
              10015,
              10020,
              10029,
              10035,
              10051,
              10068,
              10073,
              10087,
              10095,
              10157,
              10178,
              11000,
              11001,
              11002,
              11003,
              11004,
              11005,
              11006,
              11007,
              11008,
              11009,
              11010,
              11011,
              11012,
              11015,
              11016,
              11017,
              11018,
              11019,
              11020,
              11021,
              11025,
              11027,
              11029,
              11030,
              11033,
              20071,
              20072)
        )
    )
    namedValues = NamedValues(
        *(("rcftTypeRC902-FE4E1-REV-A", 60),
          ("rcftTypeRC901-FE4E1-REV-D", 68),
          ("rcftTypeRC601-FE-M-REV-C", 96),
          ("rcftTypeRC601-FE-S1-REV-C", 97),
          ("rcftTypeRC601-FE-S2-REV-C", 98),
          ("rcftTypeRC601-FE-S3-REV-C", 99),
          ("rcftTypeRC501-FE-M-REV-C", 108),
          ("rcftTypeRC501-FE-S1-REV-C", 109),
          ("rcftTypeRC501-FE-S2-REV-C", 110),
          ("rcftTypeRC501-FE-S3-REV-C", 111),
          ("rcftTypeRC901-FE4E1-REV-B", 120),
          ("rcftTypeRC603-FE-M-REV-C", 160),
          ("rcftTypeRC603-FE-S1-REV-C", 161),
          ("rcftTypeRC603-FE-S2-REV-C", 162),
          ("rcftTypeRC603-FE-S3-REV-C", 163),
          ("rcftTypeRC503-FE-M-REV-C", 168),
          ("rcftTypeRC503-FE-S1-REV-C", 169),
          ("rcftTypeRC503-FE-S2-REV-C", 170),
          ("rcftTypeRC503-FE-S3-REV-C", 171),
          ("rcftTypeRC503-E-M-REV-C", 176),
          ("rcftTypeRC503-E-S1-REV-C", 177),
          ("rcftTypeRC503-E-S2-REV-C", 178),
          ("rcftTypeRC503-E-S3-REV-C", 179),
          ("rcftTypeRC605-FE-M-REV-C", 212),
          ("rcftTypeRC605-FE-S1-REV-C", 213),
          ("rcftTypeRC605-FE-S2-REV-C", 214),
          ("rcftTypeRC605-FE-S3-REV-C", 215),
          ("rcftTypeRC505-FE-M-REV-C", 220),
          ("rcftTypeRC505-FE-S1-REV-C", 221),
          ("rcftTypeRC505-FE-S2-REV-C", 222),
          ("rcftTypeRC505-FE-S3-REV-C", 223),
          ("rcftTypeRC501-E-M-REV-C", 232),
          ("rcftTypeRC501-E-S1-REV-C", 233),
          ("rcftTypeRC501-E-S2-REV-C", 234),
          ("rcftTypeRC501-E-S3-REV-C", 235),
          ("rcftTypeRC505-E-M-REV-C", 244),
          ("rcftTypeRC505-E-S1-REV-C", 245),
          ("rcftTypeRC505-E-S2-REV-C", 246),
          ("rcftTypeRC505-E-S3-REV-C", 247),
          ("rcftTypeRC511-FE-M-REV-A", 308),
          ("rcftTypeRC511-FE-S1-REV-A", 309),
          ("rcftTypeRC511-FE-S2-REV-A", 310),
          ("rcftTypeRC511-FE-S3-REV-A", 311),
          ("rcftTypeRC503-8FE-M-REV-C", 316),
          ("rcftTypeRC503-8FE-S1-REV-C", 317),
          ("rcftTypeRC503-8FE-S2-REV-C", 318),
          ("rcftTypeRC503-8FE-S3-REV-C", 319),
          ("rcftTypeRC513-FE-M-REV-A", 324),
          ("rcftTypeRC513-FE-S1-REV-A", 325),
          ("rcftTypeRC513-FE-S2-REV-A", 326),
          ("rcftTypeRC513-FE-S3-REV-A", 327),
          ("rcftTypeRC501-8FE-M-REV-C", 352),
          ("rcftTypeRC501-8FE-S1-REV-C", 353),
          ("rcftTypeRC501-8FE-S2-REV-C", 354),
          ("rcftTypeRC501-8FE-S3-REV-C", 355),
          ("rcftTypeRC501-16FE-M-REV-C", 356),
          ("rcftTypeRC501-16FE-S1-REV-C", 357),
          ("rcftTypeRC501-16FE-S2-REV-C", 358),
          ("rcftTypeRC501-16FE-S3-REV-C", 359),
          ("rcftTypeRC503-16FE-M-REV-C", 364),
          ("rcftTypeRC503-16FE-S1-REV-C", 365),
          ("rcftTypeRC503-16FE-S2-REV-C", 366),
          ("rcftTypeRC503-16FE-S3-REV-C", 367),
          ("rcftTypeRC501-8FE-M-REV-C1", 384),
          ("rcftTypeRC501-8FE-S1-REV-C1", 385),
          ("rcftTypeRC501-8FE-S2-REV-C1", 386),
          ("rcftTypeRC501-8FE-S3-REV-C1", 387),
          ("rcftTypeRC501-16FE-M-REV-C1", 388),
          ("rcftTypeRC501-16FE-S1-REV-C1", 389),
          ("rcftTypeRC501-16FE-S2-REV-C1", 390),
          ("rcftTypeRC501-16FE-S3-REV-C1", 391),
          ("rcftTypeRC503-8FE-M-REV-C1", 392),
          ("rcftTypeRC503-8FE-S1-REV-C1", 393),
          ("rcftTypeRC503-8FE-S2-REV-C1", 394),
          ("rcftTypeRC503-8FE-S3-REV-C1", 395),
          ("rcftTypeRC503-16FE-M-REV-C1", 396),
          ("rcftTypeRC503-16FE-S1-REV-C1", 397),
          ("rcftTypeRC503-16FE-S2-REV-C1", 398),
          ("rcftTypeRC503-16FE-S3-REV-C1", 399),
          ("rcftTypeRemote-RC512-FE-M-REV-A-SLAVE", 420),
          ("rcftTypeRemote-RC512-FE-S1-REV-A-SLAVE", 421),
          ("rcftTypeRemote-RC512-FE-S2-REV-A-SLAVE", 422),
          ("rcftTypeRemote-RC512-FE-S3-REV-A-SLAVE", 423),
          ("rcftTypeRC801-30B-FV35-M-REV-M", 472),
          ("rcftTypeRC801-30B-FV35-S1-REV-M", 473),
          ("rcftTypeRC801-30B-FV35-S2-REV-M", 474),
          ("rcftTypeRC801-30B-FV35-S3-REV-M", 475),
          ("rcftTypeRC805-30B-FV35-M-REV-M", 484),
          ("rcftTypeRC805-30B-FV35-S1-REV-M", 485),
          ("rcftTypeRC805-30B-FV35-S2-REV-M", 486),
          ("rcftTypeRC805-30B-FV35-S3-REV-M", 487),
          ("rcftTypeRC511-FE-M-C-REV-A", 492),
          ("rcftTypeRC511-FE-S1-C-REV-A", 493),
          ("rcftTypeRC511-FE-S2-C-REV-A", 494),
          ("rcftTypeRC511-FE-S3-C-REV-A", 495),
          ("rcftTypeRC513-FE-M-C-REV-A", 496),
          ("rcftTypeRC513-FE-S1-C-REV-A", 497),
          ("rcftTypeRC513-FE-S2-C-REV-A", 498),
          ("rcftTypeRC513-FE-S3-C-REV-A", 499),
          ("rcftTypeRC601-FE-M-REV-E", 504),
          ("rcftTypeRC601-FE-S1-REV-E", 505),
          ("rcftTypeRC601-FE-S2-REV-E", 506),
          ("rcftTypeRC601-FE-S3-REV-E", 507),
          ("rcftTypeRC515-FE-M-REV-A", 528),
          ("rcftTypeRC515-FE-S1-REV-A", 529),
          ("rcftTypeRC515-FE-S2-REV-A", 530),
          ("rcftTypeRC515-FE-S3-REV-A", 531),
          ("rcftTypeRC603-FE-M-REV-E", 552),
          ("rcftTypeRC603-FE-S1-REV-E", 553),
          ("rcftTypeRC603-FE-S2-REV-E", 554),
          ("rcftTypeRC603-FE-S3-REV-E", 555),
          ("rcftTypeRC605-FE-M-REV-E", 560),
          ("rcftTypeRC605-FE-S1-REV-E", 561),
          ("rcftTypeRC605-FE-S2-REV-E", 562),
          ("rcftTypeRC605-FE-S3-REV-E", 563),
          ("rcftTypeRemote-RC512-FE-noOptical1-SLAVE", 612),
          ("rcftTypeRemote-RC512-FE-SS13-SLAVE", 613),
          ("rcftTypeRemote-RC512-FE-SS23-SLAVE", 614),
          ("rcftTypeRemote-RC512-FE-SS34-SLAVE", 615),
          ("rcftTypeRC801-60B-FV35-M-REV-M", 632),
          ("rcftTypeRC801-60B-FV35-S1-REV-M", 633),
          ("rcftTypeRC801-60B-FV35-S2-REV-M", 634),
          ("rcftTypeRC801-60B-FV35-S3-REV-M", 635),
          ("rcftTypeRC805-60B-FV35-M-REV-M", 636),
          ("rcftTypeRC805-60B-FV35-S1-REV-M", 637),
          ("rcftTypeRC805-60B-FV35-S2-REV-M", 638),
          ("rcftTypeRC805-60B-FV35-S3-REV-M", 639),
          ("rcftTypeRC801-30B-FV35-REV-N", 696),
          ("rcftTypeRC803-30B-FV35-REV-N", 700),
          ("rcftTypeRC805-30B-FV35-REV-N", 704),
          ("rcftTypeRC801-60B-FV35-REV-N", 708),
          ("rcftTypeRC803-60B-FV35-REV-N", 712),
          ("rcftTypeRC805-60B-FV35-REV-N", 716),
          ("rcftTypeRC901", 720),
          ("rcftTypeRC601-FE-C-M-REV-E", 724),
          ("rcftTypeRC601-FE-C-S1-REV-E", 725),
          ("rcftTypeRC601-FE-C-S2-REV-E", 726),
          ("rcftTypeRC601-FE-C-S3-REV-E", 727),
          ("rcftTypeRC512-FE-S-M-REV-A", 732),
          ("rcftTypeRC512-FE-S-S1-REV-A", 733),
          ("rcftTypeRC512-FE-S-S2-REV-A", 734),
          ("rcftTypeRC512-FE-S-S3-REV-A", 735),
          ("rcftTypeRC512-FE-S-noOptical1-REV-A", 736),
          ("rcftTypeRC512-FE-S-SS13-REV-A", 737),
          ("rcftTypeRC512-FE-S-SS23-REV-A", 738),
          ("rcftTypeRC512-FE-S-SS34-REV-A", 739),
          ("rcftTypeRC512-FE-SLAVE", 740),
          ("rcftTypeRC512-FE-C-M-REV-A", 744),
          ("rcftTypeRC512-FE-C-S1-REV-A", 745),
          ("rcftTypeRC512-FE-C-S2-REV-A", 746),
          ("rcftTypeRC512-FE-C-S3-REV-A", 747),
          ("rcftTypeRC512-FE-C-noOptical1-REV-A", 748),
          ("rcftTypeRC512-FE-C-SS13-REV-A", 749),
          ("rcftTypeRC512-FE-C-SS23-REV-A", 750),
          ("rcftTypeRC512-FE-C-SS34-REV-A", 751),
          ("rcftTypeRC512-FE", 808),
          ("rcftUnknownType", 999),
          ("rcftTypeRCMS2201-30-M-REV-A", 1000),
          ("rcftTypeRCMS2201-30-S1-REV-A", 1001),
          ("rcftTypeRCMS2201-30-S2-REV-A", 1002),
          ("rcftTypeRCMS2201-30-S3-REV-A", 1003),
          ("rcftTypeRCMS2401-30-M-REV-A", 1004),
          ("rcftTypeRCMS2401-30-S1-REV-A", 1005),
          ("rcftTypeRCMS2401-30-S2-REV-A", 1006),
          ("rcftTypeRCMS2401-30-S3-REV-A", 1007),
          ("rcftTypeRCMS2601-30-M-REV-A", 1008),
          ("rcftTypeRCMS2601-30-S1-REV-A", 1009),
          ("rcftTypeRCMS2601-30-S2-REV-A", 1010),
          ("rcftTypeRCMS2601-30-S3-REV-A", 1011),
          ("rcftTypeRCMS2101-30-FV35-M-REV-A", 1012),
          ("rcftTypeRCMS2101-30-FV35-S1-REV-A", 1013),
          ("rcftTypeRCMS2101-30-FV35-S2-REV-A", 1014),
          ("rcftTypeRCMS2101-30-FV35-S3-REV-A", 1015),
          ("rcftTypeRCMS2501-30-FV35-M-REV-A", 1016),
          ("rcftTypeRCMS2501-30-FV35-S1-REV-A", 1017),
          ("rcftTypeRCMS2501-30-FV35-S2-REV-A", 1018),
          ("rcftTypeRCMS2501-30-FV35-S3-REV-A", 1019),
          ("rcftTypeRCMS2201-60-M-REV-A", 1020),
          ("rcftTypeRCMS2201-60-S1-REV-A", 1021),
          ("rcftTypeRCMS2201-60-S2-REV-A", 1022),
          ("rcftTypeRCMS2201-60-S3-REV-A", 1023),
          ("rcftTypeRCMS2401-60-M-REV-A", 1024),
          ("rcftTypeRCMS2401-60-S1-REV-A", 1025),
          ("rcftTypeRCMS2401-60-S2-REV-A", 1026),
          ("rcftTypeRCMS2401-60-S3-REV-A", 1027),
          ("rcftTypeRCMS2601-60-M-REV-A", 1028),
          ("rcftTypeRCMS2601-60-S1-REV-A", 1029),
          ("rcftTypeRCMS2601-60-S2-REV-A", 1030),
          ("rcftTypeRCMS2601-60-S3-REV-A", 1031),
          ("rcftTypeRC802-30-G703-M-REV-M", 1032),
          ("rcftTypeRC802-30-G703-S1-REV-M", 1033),
          ("rcftTypeRC802-30-G703-S2-REV-M", 1034),
          ("rcftTypeRC802-30-G703-S3-REV-M", 1035),
          ("rcftTypeRC804-30-G703-M-REV-M", 1036),
          ("rcftTypeRC804-30-G703-S1-REV-M", 1037),
          ("rcftTypeRC804-30-G703-S2-REV-M", 1038),
          ("rcftTypeRC804-30-G703-S3-REV-M", 1039),
          ("rcftTypeRC806-30-G703-M-REV-M", 1040),
          ("rcftTypeRC806-30-G703-S1-REV-M", 1041),
          ("rcftTypeRC806-30-G703-S2-REV-M", 1042),
          ("rcftTypeRC806-30-G703-S3-REV-M", 1043),
          ("rcftTypeRC802-30B-FV35-M-REV-M", 1044),
          ("rcftTypeRC802-30B-FV35-S1-REV-M", 1045),
          ("rcftTypeRC802-30B-FV35-S2-REV-M", 1046),
          ("rcftTypeRC802-30B-FV35-S3-REV-M", 1047),
          ("rcftTypeRC804-30B-FV35-M-REV-M", 1048),
          ("rcftTypeRC804-30B-FV35-S1-REV-M", 1049),
          ("rcftTypeRC804-30B-FV35-S2-REV-M", 1050),
          ("rcftTypeRC804-30B-FV35-S3-REV-M", 1051),
          ("rcftTypeRC806-30B-FV35-M-REV-M", 1052),
          ("rcftTypeRC806-30B-FV35-S1-REV-M", 1053),
          ("rcftTypeRC806-30B-FV35-S2-REV-M", 1054),
          ("rcftTypeRC806-30B-FV35-S3-REV-M", 1055),
          ("rcftTypeRC802-60B-M-REV-M", 1056),
          ("rcftTypeRC802-60B-S1-REV-M", 1057),
          ("rcftTypeRC802-60B-S2-REV-M", 1058),
          ("rcftTypeRC802-60B-S3-REV-M", 1059),
          ("rcftTypeRC804-60B-M-REV-M", 1060),
          ("rcftTypeRC804-60B-S1-REV-M", 1061),
          ("rcftTypeRC804-60B-S2-REV-M", 1062),
          ("rcftTypeRC804-60B-S3-REV-M", 1063),
          ("rcftTypeRC806-60B-M-REV-M", 1064),
          ("rcftTypeRC806-60B-S1-REV-M", 1065),
          ("rcftTypeRC806-60B-S2-REV-M", 1066),
          ("rcftTypeRC806-60B-S3-REV-M", 1067),
          ("rcftTypeRC906-FXE1-REV-M", 1068),
          ("rcftTypeRC916-FXE1-REV-M", 1072),
          ("rcftTypeRC906-EE1-REV-M", 1076),
          ("rcftTypeRC905-EE1-REV-M", 1080),
          ("rcftTypeRC905-4EE1-REV-M", 1084),
          ("rcftTypeRC902", 1088),
          ("rcftTypeRC802-30B-FV35-REV-N", 1092),
          ("rcftTypeRC804-30B-FV35-REV-N", 1096),
          ("rcftTypeRC806-30B-FV35-REV-N", 1100),
          ("rcftTypeOPCOM200-FEU2-REV-A-SLAVE", 10001),
          ("rcftTypeOPCOM200-FEU1-REV-A-SLAVE", 10005),
          ("rcftTypeRC2002-30FE-REV-A", 10008),
          ("rcftTypeRC602-GE-REV-A-SLAVE", 10009),
          ("rcftTypeRC852-30-REV-A", 10010),
          ("rcftTypeRC521-FE-REV-D", 10015),
          ("rcftTypeRC511-4FE-REV-A", 10020),
          ("rcftTypeRC581-FE-REV-A", 10029),
          ("rcftTypeRC601-GEF-REV-A", 10035),
          ("rcftTypeRC521-FE-REV-C", 10051),
          ("rcftTypeRC581-GE-REV-A", 10068),
          ("rcftTypeRC3101", 10073),
          ("rcftTypeRC531-FE-REV-A", 10087),
          ("rcftTypeRC851-30-FV35-REV-A", 10095),
          ("rcftTypeRCVS1000-501A", 10157),
          ("rcftTypeRC851-30-FV35-REV-B", 10178),
          ("rcftTypeRC1102-FE-REV-A-SLAVE", 11000),
          ("rcftTypeRC852-30-FV35-REV-A", 11001),
          ("rcftTypeRC1102-E1-REV-B-SLAVE", 11002),
          ("rcftTypeRC801-120B-REV-M", 11003),
          ("rcftTypeRC805-120B-REV-M", 11004),
          ("rcftTypeRC552-FE-REV-A-SLAVE", 11005),
          ("rcftTypeRC602-GEF-REV-A-SLAVE", 11006),
          ("rcftTypeOPCOM200-GEU1-SLAVE-REV-A", 11007),
          ("rcftTypeRC852-30-BL-REV-A", 11008),
          ("rcftTypeRC1102-V35-SLAVE-REV-A", 11009),
          ("rcftTypeRC532-2FE-REV-A-SLAVE", 11010),
          ("rcftTypeRC1102-E1-BL-REV-A-SLAVE", 11011),
          ("rcftTypeRC532-FE-REV-A-SLAVE", 11012),
          ("rcftTypeRCVS1000-801A-1DD-REV-A", 11015),
          ("rcftTypeRCVS1000-601A-1DD-REV-A", 11016),
          ("rcftTypeRC802-120L-BL-REV-M", 11017),
          ("rcftTypeRC552-GE-REV-A-SLAVE", 11018),
          ("rcftTypeRC552-FE-REV-A-SLAVE-NEW", 11019),
          ("rcftTypeRC602-GE-REV-B-SLAVE", 11020),
          ("rcftTypeRC551L-FE-REV-A-SLAVE", 11021),
          ("rcftTypeRC552-GE-REV-B-SLAVE", 11025),
          ("rcftTypeRC852-30-FV35-REV-A1-SLAVE", 11027),
          ("rcftTypeRC522-FE-REV-D-SLAVE", 11029),
          ("rcftTypeRC522-FE-REV-C-SLAVE", 11030),
          ("rcftTypeRC602E-GE", 11033),
          ("rcftTypeRC521H-FE-DoubleFiber-S", 20071),
          ("rcftTypeRC521H-FE-SingleFiber-S", 20072))
    )


_RcftRSlotType_Type.__name__ = "Integer32"
_RcftRSlotType_Object = MibTableColumn
rcftRSlotType = _RcftRSlotType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 53),
    _RcftRSlotType_Type()
)
rcftRSlotType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRSlotType.setStatus("current")
_RcftRSlotChassisTmpt_Type = Integer32
_RcftRSlotChassisTmpt_Object = MibTableColumn
rcftRSlotChassisTmpt = _RcftRSlotChassisTmpt_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 54),
    _RcftRSlotChassisTmpt_Type()
)
rcftRSlotChassisTmpt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRSlotChassisTmpt.setStatus("current")
_RcftSlotExSwitchMode_Type = Integer32
_RcftSlotExSwitchMode_Object = MibTableColumn
rcftSlotExSwitchMode = _RcftSlotExSwitchMode_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 55),
    _RcftSlotExSwitchMode_Type()
)
rcftSlotExSwitchMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftSlotExSwitchMode.setStatus("current")
_RcftSlotRevFluxCount_Type = Counter32
_RcftSlotRevFluxCount_Object = MibTableColumn
rcftSlotRevFluxCount = _RcftSlotRevFluxCount_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 56),
    _RcftSlotRevFluxCount_Type()
)
rcftSlotRevFluxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftSlotRevFluxCount.setStatus("current")
_RcftSlotSedFluxCount_Type = Counter32
_RcftSlotSedFluxCount_Object = MibTableColumn
rcftSlotSedFluxCount = _RcftSlotSedFluxCount_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 57),
    _RcftSlotSedFluxCount_Type()
)
rcftSlotSedFluxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftSlotSedFluxCount.setStatus("current")
_RcftSlotRevFluxTimer_Type = Counter32
_RcftSlotRevFluxTimer_Object = MibTableColumn
rcftSlotRevFluxTimer = _RcftSlotRevFluxTimer_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 58),
    _RcftSlotRevFluxTimer_Type()
)
rcftSlotRevFluxTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftSlotRevFluxTimer.setStatus("current")
_RcftSlotSedFluxTimer_Type = Counter32
_RcftSlotSedFluxTimer_Object = MibTableColumn
rcftSlotSedFluxTimer = _RcftSlotSedFluxTimer_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 59),
    _RcftSlotSedFluxTimer_Type()
)
rcftSlotSedFluxTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftSlotSedFluxTimer.setStatus("current")


class _RcftRSlotESpeed_Type(Integer32):
    """Custom type rcftRSlotESpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              16)
        )
    )
    namedValues = NamedValues(
        *(("rcft10Mbps", 1),
          ("rcft100Mbps", 2),
          ("rcft1000Mbps", 3),
          ("rcft10Gbps", 4),
          ("other", 16))
    )


_RcftRSlotESpeed_Type.__name__ = "Integer32"
_RcftRSlotESpeed_Object = MibTableColumn
rcftRSlotESpeed = _RcftRSlotESpeed_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 60),
    _RcftRSlotESpeed_Type()
)
rcftRSlotESpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftRSlotESpeed.setStatus("current")


class _RcftRSlotOSpeed_Type(Integer32):
    """Custom type rcftRSlotOSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              16)
        )
    )
    namedValues = NamedValues(
        *(("rcft10Mbps", 1),
          ("rcft100Mbps", 2),
          ("rcft1000Mbps", 3),
          ("rcft10Gbps", 4),
          ("other", 16))
    )


_RcftRSlotOSpeed_Type.__name__ = "Integer32"
_RcftRSlotOSpeed_Object = MibTableColumn
rcftRSlotOSpeed = _RcftRSlotOSpeed_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 61),
    _RcftRSlotOSpeed_Type()
)
rcftRSlotOSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRSlotOSpeed.setStatus("current")


class _RcftRSlotORLnk_Type(Integer32):
    """Custom type rcftRSlotORLnk based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("linkup", 1),
          ("linkdown", 2))
    )


_RcftRSlotORLnk_Type.__name__ = "Integer32"
_RcftRSlotORLnk_Object = MibTableColumn
rcftRSlotORLnk = _RcftRSlotORLnk_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 62),
    _RcftRSlotORLnk_Type()
)
rcftRSlotORLnk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRSlotORLnk.setStatus("current")


class _RcftRSlotOTLnk_Type(Integer32):
    """Custom type rcftRSlotOTLnk based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("linkup", 1),
          ("linkdown", 2))
    )


_RcftRSlotOTLnk_Type.__name__ = "Integer32"
_RcftRSlotOTLnk_Object = MibTableColumn
rcftRSlotOTLnk = _RcftRSlotOTLnk_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 63),
    _RcftRSlotOTLnk_Type()
)
rcftRSlotOTLnk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRSlotOTLnk.setStatus("current")


class _RcftSlotE1LOS_Type(Integer32):
    """Custom type rcftSlotE1LOS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("disappear", 2))
    )


_RcftSlotE1LOS_Type.__name__ = "Integer32"
_RcftSlotE1LOS_Object = MibTableColumn
rcftSlotE1LOS = _RcftSlotE1LOS_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 64),
    _RcftSlotE1LOS_Type()
)
rcftSlotE1LOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftSlotE1LOS.setStatus("current")


class _RcftSlotOLOS_Type(Integer32):
    """Custom type rcftSlotOLOS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("disappear", 2))
    )


_RcftSlotOLOS_Type.__name__ = "Integer32"
_RcftSlotOLOS_Object = MibTableColumn
rcftSlotOLOS = _RcftSlotOLOS_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 65),
    _RcftSlotOLOS_Type()
)
rcftSlotOLOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftSlotOLOS.setStatus("current")


class _RcftSlotOSync_Type(Integer32):
    """Custom type rcftSlotOSync based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("loss", 2))
    )


_RcftSlotOSync_Type.__name__ = "Integer32"
_RcftSlotOSync_Object = MibTableColumn
rcftSlotOSync = _RcftSlotOSync_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 66),
    _RcftSlotOSync_Type()
)
rcftSlotOSync.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftSlotOSync.setStatus("current")


class _RcftSlotOTransErrorCode_Type(Integer32):
    """Custom type rcftSlotOTransErrorCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("less10E-6", 1),
          ("more10E-6", 2),
          ("more10E-3", 3))
    )


_RcftSlotOTransErrorCode_Type.__name__ = "Integer32"
_RcftSlotOTransErrorCode_Object = MibTableColumn
rcftSlotOTransErrorCode = _RcftSlotOTransErrorCode_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 67),
    _RcftSlotOTransErrorCode_Type()
)
rcftSlotOTransErrorCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftSlotOTransErrorCode.setStatus("current")


class _RcftRSlotE1LOS_Type(Integer32):
    """Custom type rcftRSlotE1LOS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("disappear", 2))
    )


_RcftRSlotE1LOS_Type.__name__ = "Integer32"
_RcftRSlotE1LOS_Object = MibTableColumn
rcftRSlotE1LOS = _RcftRSlotE1LOS_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 68),
    _RcftRSlotE1LOS_Type()
)
rcftRSlotE1LOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRSlotE1LOS.setStatus("current")


class _RcftRSlotOLOS_Type(Integer32):
    """Custom type rcftRSlotOLOS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("disappear", 2))
    )


_RcftRSlotOLOS_Type.__name__ = "Integer32"
_RcftRSlotOLOS_Object = MibTableColumn
rcftRSlotOLOS = _RcftRSlotOLOS_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 69),
    _RcftRSlotOLOS_Type()
)
rcftRSlotOLOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRSlotOLOS.setStatus("current")


class _RcftRSlotOSync_Type(Integer32):
    """Custom type rcftRSlotOSync based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("loss", 2))
    )


_RcftRSlotOSync_Type.__name__ = "Integer32"
_RcftRSlotOSync_Object = MibTableColumn
rcftRSlotOSync = _RcftRSlotOSync_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 70),
    _RcftRSlotOSync_Type()
)
rcftRSlotOSync.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRSlotOSync.setStatus("current")


class _RcftRSlotOTransErrorCode_Type(Integer32):
    """Custom type rcftRSlotOTransErrorCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("less10E-6", 1),
          ("more10E-6", 2),
          ("more10E-3", 3))
    )


_RcftRSlotOTransErrorCode_Type.__name__ = "Integer32"
_RcftRSlotOTransErrorCode_Object = MibTableColumn
rcftRSlotOTransErrorCode = _RcftRSlotOTransErrorCode_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 71),
    _RcftRSlotOTransErrorCode_Type()
)
rcftRSlotOTransErrorCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRSlotOTransErrorCode.setStatus("current")


class _RcftSlotE1LOF_Type(Integer32):
    """Custom type rcftSlotE1LOF based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("loss", 2))
    )


_RcftSlotE1LOF_Type.__name__ = "Integer32"
_RcftSlotE1LOF_Object = MibTableColumn
rcftSlotE1LOF = _RcftSlotE1LOF_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 72),
    _RcftSlotE1LOF_Type()
)
rcftSlotE1LOF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftSlotE1LOF.setStatus("current")


class _RcftSlotE1CRC_Type(Integer32):
    """Custom type rcftSlotE1CRC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("error", 2))
    )


_RcftSlotE1CRC_Type.__name__ = "Integer32"
_RcftSlotE1CRC_Object = MibTableColumn
rcftSlotE1CRC = _RcftSlotE1CRC_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 73),
    _RcftSlotE1CRC_Type()
)
rcftSlotE1CRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftSlotE1CRC.setStatus("current")
_RcftSlotHardWareDescr_Type = DisplayString
_RcftSlotHardWareDescr_Object = MibTableColumn
rcftSlotHardWareDescr = _RcftSlotHardWareDescr_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 74),
    _RcftSlotHardWareDescr_Type()
)
rcftSlotHardWareDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftSlotHardWareDescr.setStatus("current")
_RcftSlotSigleChipDescr_Type = DisplayString
_RcftSlotSigleChipDescr_Object = MibTableColumn
rcftSlotSigleChipDescr = _RcftSlotSigleChipDescr_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 75),
    _RcftSlotSigleChipDescr_Type()
)
rcftSlotSigleChipDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftSlotSigleChipDescr.setStatus("current")


class _RcftSlotV35Port_Type(Integer32):
    """Custom type rcftSlotV35Port based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("close", 1),
          ("open", 2))
    )


_RcftSlotV35Port_Type.__name__ = "Integer32"
_RcftSlotV35Port_Object = MibTableColumn
rcftSlotV35Port = _RcftSlotV35Port_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 76),
    _RcftSlotV35Port_Type()
)
rcftSlotV35Port.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftSlotV35Port.setStatus("current")


class _RcftSlotV35RTS_Type(Integer32):
    """Custom type rcftSlotV35RTS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inefficient", 1),
          ("efficient", 2))
    )


_RcftSlotV35RTS_Type.__name__ = "Integer32"
_RcftSlotV35RTS_Object = MibTableColumn
rcftSlotV35RTS = _RcftSlotV35RTS_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 77),
    _RcftSlotV35RTS_Type()
)
rcftSlotV35RTS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftSlotV35RTS.setStatus("current")


class _RcftSlotV35DTR_Type(Integer32):
    """Custom type rcftSlotV35DTR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inefficient", 1),
          ("efficient", 2))
    )


_RcftSlotV35DTR_Type.__name__ = "Integer32"
_RcftSlotV35DTR_Object = MibTableColumn
rcftSlotV35DTR = _RcftSlotV35DTR_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 78),
    _RcftSlotV35DTR_Type()
)
rcftSlotV35DTR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftSlotV35DTR.setStatus("current")


class _RcftSlotE1LoopStatus_Type(Integer32):
    """Custom type rcftSlotE1LoopStatus based on Integer32"""
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
        *(("e1port1loop", 1),
          ("e1twoportnormal", 2),
          ("e1port2loop", 3),
          ("e1twoportloop", 4))
    )


_RcftSlotE1LoopStatus_Type.__name__ = "Integer32"
_RcftSlotE1LoopStatus_Object = MibTableColumn
rcftSlotE1LoopStatus = _RcftSlotE1LoopStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 79),
    _RcftSlotE1LoopStatus_Type()
)
rcftSlotE1LoopStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftSlotE1LoopStatus.setStatus("current")


class _RcftSlotE1LoopSwitchStatus_Type(Integer32):
    """Custom type rcftSlotE1LoopSwitchStatus based on Integer32"""
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
        *(("e1port1loop", 1),
          ("e1twoportnormal", 2),
          ("e1port2loop", 3),
          ("e1twoportloop", 4))
    )


_RcftSlotE1LoopSwitchStatus_Type.__name__ = "Integer32"
_RcftSlotE1LoopSwitchStatus_Object = MibTableColumn
rcftSlotE1LoopSwitchStatus = _RcftSlotE1LoopSwitchStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 80),
    _RcftSlotE1LoopSwitchStatus_Type()
)
rcftSlotE1LoopSwitchStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftSlotE1LoopSwitchStatus.setStatus("current")


class _RcftSlotV35LoopStatus_Type(Integer32):
    """Custom type rcftSlotV35LoopStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("v35loopok", 1),
          ("v35loopnormal", 2))
    )


_RcftSlotV35LoopStatus_Type.__name__ = "Integer32"
_RcftSlotV35LoopStatus_Object = MibTableColumn
rcftSlotV35LoopStatus = _RcftSlotV35LoopStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 81),
    _RcftSlotV35LoopStatus_Type()
)
rcftSlotV35LoopStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftSlotV35LoopStatus.setStatus("current")


class _RcftSlotV35LoopSwitchStatus_Type(Integer32):
    """Custom type rcftSlotV35LoopSwitchStatus based on Integer32"""
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


_RcftSlotV35LoopSwitchStatus_Type.__name__ = "Integer32"
_RcftSlotV35LoopSwitchStatus_Object = MibTableColumn
rcftSlotV35LoopSwitchStatus = _RcftSlotV35LoopSwitchStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 82),
    _RcftSlotV35LoopSwitchStatus_Type()
)
rcftSlotV35LoopSwitchStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftSlotV35LoopSwitchStatus.setStatus("current")


class _RcftSlotEPort1Link_Type(Integer32):
    """Custom type rcftSlotEPort1Link based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("link", 1),
          ("unlink", 2))
    )


_RcftSlotEPort1Link_Type.__name__ = "Integer32"
_RcftSlotEPort1Link_Object = MibTableColumn
rcftSlotEPort1Link = _RcftSlotEPort1Link_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 83),
    _RcftSlotEPort1Link_Type()
)
rcftSlotEPort1Link.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftSlotEPort1Link.setStatus("current")


class _RcftSlotEPort1AutoNegotiation_Type(Integer32):
    """Custom type rcftSlotEPort1AutoNegotiation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("manul", 2))
    )


_RcftSlotEPort1AutoNegotiation_Type.__name__ = "Integer32"
_RcftSlotEPort1AutoNegotiation_Object = MibTableColumn
rcftSlotEPort1AutoNegotiation = _RcftSlotEPort1AutoNegotiation_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 84),
    _RcftSlotEPort1AutoNegotiation_Type()
)
rcftSlotEPort1AutoNegotiation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftSlotEPort1AutoNegotiation.setStatus("current")


class _RcftSlotEPort1Duplex_Type(Integer32):
    """Custom type rcftSlotEPort1Duplex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("full-duplex", 1),
          ("half-duplex", 2),
          ("auto", 3))
    )


_RcftSlotEPort1Duplex_Type.__name__ = "Integer32"
_RcftSlotEPort1Duplex_Object = MibTableColumn
rcftSlotEPort1Duplex = _RcftSlotEPort1Duplex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 85),
    _RcftSlotEPort1Duplex_Type()
)
rcftSlotEPort1Duplex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftSlotEPort1Duplex.setStatus("current")


class _RcftSlotEPort1Speed_Type(Integer32):
    """Custom type rcftSlotEPort1Speed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              16)
        )
    )
    namedValues = NamedValues(
        *(("rcft10Mbps", 1),
          ("rcft100Mbps", 2),
          ("rcft1000Mbps", 3),
          ("rcft10Gbps", 4),
          ("other", 16))
    )


_RcftSlotEPort1Speed_Type.__name__ = "Integer32"
_RcftSlotEPort1Speed_Object = MibTableColumn
rcftSlotEPort1Speed = _RcftSlotEPort1Speed_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 86),
    _RcftSlotEPort1Speed_Type()
)
rcftSlotEPort1Speed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftSlotEPort1Speed.setStatus("current")


class _RcftSlotEPort1Port_Type(Integer32):
    """Custom type rcftSlotEPort1Port based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("open", 1),
          ("close", 2))
    )


_RcftSlotEPort1Port_Type.__name__ = "Integer32"
_RcftSlotEPort1Port_Object = MibTableColumn
rcftSlotEPort1Port = _RcftSlotEPort1Port_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 87),
    _RcftSlotEPort1Port_Type()
)
rcftSlotEPort1Port.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftSlotEPort1Port.setStatus("current")


class _RcftSlotE2PortBandWidth_Type(Integer32):
    """Custom type rcftSlotE2PortBandWidth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              10,
              12,
              15,
              20)
        )
    )
    namedValues = NamedValues(
        *(("ratioOfOneToOne", 1),
          ("ratioOfTwoToOne", 2),
          ("ratioOfThreeToOne", 3),
          ("ratioOfFourToOne", 4),
          ("ratioOfFiveToOne", 5),
          ("ratioOfTenToOne", 10),
          ("ratioOfOneToTwo", 12),
          ("ratioOfOneToFive", 15),
          ("ratioOfOneToTen", 20))
    )


_RcftSlotE2PortBandWidth_Type.__name__ = "Integer32"
_RcftSlotE2PortBandWidth_Object = MibTableColumn
rcftSlotE2PortBandWidth = _RcftSlotE2PortBandWidth_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 88),
    _RcftSlotE2PortBandWidth_Type()
)
rcftSlotE2PortBandWidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftSlotE2PortBandWidth.setStatus("current")
_RcftSlotV35Speed_Type = Integer32
_RcftSlotV35Speed_Object = MibTableColumn
rcftSlotV35Speed = _RcftSlotV35Speed_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 89),
    _RcftSlotV35Speed_Type()
)
rcftSlotV35Speed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftSlotV35Speed.setStatus("current")


class _RcftSlotV35RateCfg_Type(Integer32):
    """Custom type rcftSlotV35RateCfg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("master", 1),
          ("secondary", 2))
    )


_RcftSlotV35RateCfg_Type.__name__ = "Integer32"
_RcftSlotV35RateCfg_Object = MibTableColumn
rcftSlotV35RateCfg = _RcftSlotV35RateCfg_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 90),
    _RcftSlotV35RateCfg_Type()
)
rcftSlotV35RateCfg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftSlotV35RateCfg.setStatus("current")


class _RcftSlotV35RxClk_Type(Integer32):
    """Custom type rcftSlotV35RxClk based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("negative", 1),
          ("positive", 2))
    )


_RcftSlotV35RxClk_Type.__name__ = "Integer32"
_RcftSlotV35RxClk_Object = MibTableColumn
rcftSlotV35RxClk = _RcftSlotV35RxClk_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 91),
    _RcftSlotV35RxClk_Type()
)
rcftSlotV35RxClk.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftSlotV35RxClk.setStatus("current")


class _RcftSlotV35TxClk_Type(Integer32):
    """Custom type rcftSlotV35TxClk based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("negative", 1),
          ("positive", 2))
    )


_RcftSlotV35TxClk_Type.__name__ = "Integer32"
_RcftSlotV35TxClk_Object = MibTableColumn
rcftSlotV35TxClk = _RcftSlotV35TxClk_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 92),
    _RcftSlotV35TxClk_Type()
)
rcftSlotV35TxClk.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftSlotV35TxClk.setStatus("current")


class _RcftSlotV35LoopTest_Type(Integer32):
    """Custom type rcftSlotV35LoopTest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("open", 1),
          ("normal", 2))
    )


_RcftSlotV35LoopTest_Type.__name__ = "Integer32"
_RcftSlotV35LoopTest_Object = MibTableColumn
rcftSlotV35LoopTest = _RcftSlotV35LoopTest_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 93),
    _RcftSlotV35LoopTest_Type()
)
rcftSlotV35LoopTest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftSlotV35LoopTest.setStatus("current")


class _RcftSlotRE1LoopTest_Type(Integer32):
    """Custom type rcftSlotRE1LoopTest based on Integer32"""
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
        *(("e1port1loop", 1),
          ("e1twoportnormal", 2),
          ("e1port2loop", 3),
          ("e1twoportloop", 4))
    )


_RcftSlotRE1LoopTest_Type.__name__ = "Integer32"
_RcftSlotRE1LoopTest_Object = MibTableColumn
rcftSlotRE1LoopTest = _RcftSlotRE1LoopTest_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 94),
    _RcftSlotRE1LoopTest_Type()
)
rcftSlotRE1LoopTest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftSlotRE1LoopTest.setStatus("current")


class _RcftSlotRE1LoopStatus_Type(Integer32):
    """Custom type rcftSlotRE1LoopStatus based on Integer32"""
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
        *(("e1port1loop", 1),
          ("e1twoportnormal", 2),
          ("e1port2loop", 3),
          ("e1twoportloop", 4))
    )


_RcftSlotRE1LoopStatus_Type.__name__ = "Integer32"
_RcftSlotRE1LoopStatus_Object = MibTableColumn
rcftSlotRE1LoopStatus = _RcftSlotRE1LoopStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 95),
    _RcftSlotRE1LoopStatus_Type()
)
rcftSlotRE1LoopStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftSlotRE1LoopStatus.setStatus("current")


class _RcftSlotLoopTestEn_Type(Integer32):
    """Custom type rcftSlotLoopTestEn based on Integer32"""
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


_RcftSlotLoopTestEn_Type.__name__ = "Integer32"
_RcftSlotLoopTestEn_Object = MibTableColumn
rcftSlotLoopTestEn = _RcftSlotLoopTestEn_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 96),
    _RcftSlotLoopTestEn_Type()
)
rcftSlotLoopTestEn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftSlotLoopTestEn.setStatus("current")


class _RcftSlotCLKMode_Type(Integer32):
    """Custom type rcftSlotCLKMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("secondary", 1),
          ("v35terminal", 2),
          ("master", 3),
          ("reserved", 4),
          ("e1PortClk", 5),
          ("gPortClk", 6),
          ("transparent", 7))
    )


_RcftSlotCLKMode_Type.__name__ = "Integer32"
_RcftSlotCLKMode_Object = MibTableColumn
rcftSlotCLKMode = _RcftSlotCLKMode_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 97),
    _RcftSlotCLKMode_Type()
)
rcftSlotCLKMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftSlotCLKMode.setStatus("current")


class _RcftSlotCfgCmdEn_Type(Integer32):
    """Custom type rcftSlotCfgCmdEn based on Integer32"""
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


_RcftSlotCfgCmdEn_Type.__name__ = "Integer32"
_RcftSlotCfgCmdEn_Object = MibTableColumn
rcftSlotCfgCmdEn = _RcftSlotCfgCmdEn_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 98),
    _RcftSlotCfgCmdEn_Type()
)
rcftSlotCfgCmdEn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftSlotCfgCmdEn.setStatus("current")


class _RcftSlotE1PCM_Type(Integer32):
    """Custom type rcftSlotE1PCM based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("pcm31", 1),
          ("pcm30", 2))
    )


_RcftSlotE1PCM_Type.__name__ = "Integer32"
_RcftSlotE1PCM_Object = MibTableColumn
rcftSlotE1PCM = _RcftSlotE1PCM_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 99),
    _RcftSlotE1PCM_Type()
)
rcftSlotE1PCM.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftSlotE1PCM.setStatus("current")


class _RcftSlotE1CRCEn_Type(Integer32):
    """Custom type rcftSlotE1CRCEn based on Integer32"""
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


_RcftSlotE1CRCEn_Type.__name__ = "Integer32"
_RcftSlotE1CRCEn_Object = MibTableColumn
rcftSlotE1CRCEn = _RcftSlotE1CRCEn_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 100),
    _RcftSlotE1CRCEn_Type()
)
rcftSlotE1CRCEn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftSlotE1CRCEn.setStatus("current")


class _RcftSlotE1AIS_Type(Integer32):
    """Custom type rcftSlotE1AIS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("loss", 2))
    )


_RcftSlotE1AIS_Type.__name__ = "Integer32"
_RcftSlotE1AIS_Object = MibTableColumn
rcftSlotE1AIS = _RcftSlotE1AIS_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 101),
    _RcftSlotE1AIS_Type()
)
rcftSlotE1AIS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftSlotE1AIS.setStatus("current")


class _RcftSlotRALM_Type(Integer32):
    """Custom type rcftSlotRALM based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("loss", 2))
    )


_RcftSlotRALM_Type.__name__ = "Integer32"
_RcftSlotRALM_Object = MibTableColumn
rcftSlotRALM = _RcftSlotRALM_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 102),
    _RcftSlotRALM_Type()
)
rcftSlotRALM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftSlotRALM.setStatus("current")


class _RcftSlotE1Transparent_Type(Integer32):
    """Custom type rcftSlotE1Transparent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("transparent", 1),
          ("pcm", 2))
    )


_RcftSlotE1Transparent_Type.__name__ = "Integer32"
_RcftSlotE1Transparent_Object = MibTableColumn
rcftSlotE1Transparent = _RcftSlotE1Transparent_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 103),
    _RcftSlotE1Transparent_Type()
)
rcftSlotE1Transparent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftSlotE1Transparent.setStatus("current")
_RcftSlotEthTransmitSpeed_Type = Integer32
_RcftSlotEthTransmitSpeed_Object = MibTableColumn
rcftSlotEthTransmitSpeed = _RcftSlotEthTransmitSpeed_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 104),
    _RcftSlotEthTransmitSpeed_Type()
)
rcftSlotEthTransmitSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftSlotEthTransmitSpeed.setStatus("current")


class _RcftSlotE1Port2LOS_Type(Integer32):
    """Custom type rcftSlotE1Port2LOS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("disappear", 2))
    )


_RcftSlotE1Port2LOS_Type.__name__ = "Integer32"
_RcftSlotE1Port2LOS_Object = MibTableColumn
rcftSlotE1Port2LOS = _RcftSlotE1Port2LOS_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 105),
    _RcftSlotE1Port2LOS_Type()
)
rcftSlotE1Port2LOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftSlotE1Port2LOS.setStatus("current")


class _RcftRSlotE1Port2LOS_Type(Integer32):
    """Custom type rcftRSlotE1Port2LOS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("disappear", 2))
    )


_RcftRSlotE1Port2LOS_Type.__name__ = "Integer32"
_RcftRSlotE1Port2LOS_Object = MibTableColumn
rcftRSlotE1Port2LOS = _RcftRSlotE1Port2LOS_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 106),
    _RcftRSlotE1Port2LOS_Type()
)
rcftRSlotE1Port2LOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRSlotE1Port2LOS.setStatus("current")


class _RcftSlotRE1LoopSwitchStatus_Type(Integer32):
    """Custom type rcftSlotRE1LoopSwitchStatus based on Integer32"""
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
        *(("e1port1loop", 1),
          ("e1twoportnormal", 2),
          ("e1port2loop", 3),
          ("e1twoportloop", 4))
    )


_RcftSlotRE1LoopSwitchStatus_Type.__name__ = "Integer32"
_RcftSlotRE1LoopSwitchStatus_Object = MibTableColumn
rcftSlotRE1LoopSwitchStatus = _RcftSlotRE1LoopSwitchStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 107),
    _RcftSlotRE1LoopSwitchStatus_Type()
)
rcftSlotRE1LoopSwitchStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftSlotRE1LoopSwitchStatus.setStatus("current")


class _RcftSlotFrameLength_Type(Integer32):
    """Custom type rcftSlotFrameLength based on Integer32"""
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
        *(("framelen1916B", 1),
          ("framelen1536B", 2),
          ("framelen9728B", 3),
          ("framelen1518B", 4),
          ("framelen9kB", 5),
          ("framelen2048", 6))
    )


_RcftSlotFrameLength_Type.__name__ = "Integer32"
_RcftSlotFrameLength_Object = MibTableColumn
rcftSlotFrameLength = _RcftSlotFrameLength_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 108),
    _RcftSlotFrameLength_Type()
)
rcftSlotFrameLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftSlotFrameLength.setStatus("current")
_RcftSlotRecvRestrictSpeed_Type = Integer32
_RcftSlotRecvRestrictSpeed_Object = MibTableColumn
rcftSlotRecvRestrictSpeed = _RcftSlotRecvRestrictSpeed_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 109),
    _RcftSlotRecvRestrictSpeed_Type()
)
rcftSlotRecvRestrictSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftSlotRecvRestrictSpeed.setStatus("current")
_RcftSlotSendRestrictSpeed_Type = Integer32
_RcftSlotSendRestrictSpeed_Object = MibTableColumn
rcftSlotSendRestrictSpeed = _RcftSlotSendRestrictSpeed_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 110),
    _RcftSlotSendRestrictSpeed_Type()
)
rcftSlotSendRestrictSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftSlotSendRestrictSpeed.setStatus("current")


class _RcftRSlotFrameLength_Type(Integer32):
    """Custom type rcftRSlotFrameLength based on Integer32"""
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
        *(("framelen1916B", 1),
          ("framelen1536B", 2),
          ("framelen9728B", 3),
          ("framelen1518B", 4),
          ("framelen9kB", 5),
          ("framelen2048B", 6))
    )


_RcftRSlotFrameLength_Type.__name__ = "Integer32"
_RcftRSlotFrameLength_Object = MibTableColumn
rcftRSlotFrameLength = _RcftRSlotFrameLength_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 111),
    _RcftRSlotFrameLength_Type()
)
rcftRSlotFrameLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftRSlotFrameLength.setStatus("current")


class _RcftRSlotVLAN_Type(Integer32):
    """Custom type rcftRSlotVLAN based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("port-vlan", 1),
          ("not-support", 2),
          ("tag-vlan", 3))
    )


_RcftRSlotVLAN_Type.__name__ = "Integer32"
_RcftRSlotVLAN_Object = MibTableColumn
rcftRSlotVLAN = _RcftRSlotVLAN_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 112),
    _RcftRSlotVLAN_Type()
)
rcftRSlotVLAN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftRSlotVLAN.setStatus("current")


class _RcftSlotLALM_Type(Integer32):
    """Custom type rcftSlotLALM based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("loss", 2))
    )


_RcftSlotLALM_Type.__name__ = "Integer32"
_RcftSlotLALM_Object = MibTableColumn
rcftSlotLALM = _RcftSlotLALM_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 113),
    _RcftSlotLALM_Type()
)
rcftSlotLALM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftSlotLALM.setStatus("current")


class _RcftSlotChipOpMode_Type(Integer32):
    """Custom type rcftSlotChipOpMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("old", 1),
          ("new", 2))
    )


_RcftSlotChipOpMode_Type.__name__ = "Integer32"
_RcftSlotChipOpMode_Object = MibTableColumn
rcftSlotChipOpMode = _RcftSlotChipOpMode_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 114),
    _RcftSlotChipOpMode_Type()
)
rcftSlotChipOpMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftSlotChipOpMode.setStatus("current")


class _RcftSlotAutoCutErrLineEn_Type(Integer32):
    """Custom type rcftSlotAutoCutErrLineEn based on Integer32"""
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


_RcftSlotAutoCutErrLineEn_Type.__name__ = "Integer32"
_RcftSlotAutoCutErrLineEn_Object = MibTableColumn
rcftSlotAutoCutErrLineEn = _RcftSlotAutoCutErrLineEn_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 115),
    _RcftSlotAutoCutErrLineEn_Type()
)
rcftSlotAutoCutErrLineEn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftSlotAutoCutErrLineEn.setStatus("current")


class _RcftSlotRamBD_Type(Integer32):
    """Custom type rcftSlotRamBD based on Integer32"""
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
        *(("less256Kbps", 1),
          ("more256Kbps", 2),
          ("more512Kbps", 3),
          ("more1Mbps", 4),
          ("more2Mbps", 5))
    )


_RcftSlotRamBD_Type.__name__ = "Integer32"
_RcftSlotRamBD_Object = MibTableColumn
rcftSlotRamBD = _RcftSlotRamBD_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 116),
    _RcftSlotRamBD_Type()
)
rcftSlotRamBD.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftSlotRamBD.setStatus("current")


class _RcftSlotV35DSR_Type(Integer32):
    """Custom type rcftSlotV35DSR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("signal", 1),
          ("nosignal", 2))
    )


_RcftSlotV35DSR_Type.__name__ = "Integer32"
_RcftSlotV35DSR_Object = MibTableColumn
rcftSlotV35DSR = _RcftSlotV35DSR_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 117),
    _RcftSlotV35DSR_Type()
)
rcftSlotV35DSR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftSlotV35DSR.setStatus("current")


class _RcftSlotV35DCD_Type(Integer32):
    """Custom type rcftSlotV35DCD based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("signal", 1),
          ("nosignal", 2))
    )


_RcftSlotV35DCD_Type.__name__ = "Integer32"
_RcftSlotV35DCD_Object = MibTableColumn
rcftSlotV35DCD = _RcftSlotV35DCD_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 118),
    _RcftSlotV35DCD_Type()
)
rcftSlotV35DCD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftSlotV35DCD.setStatus("current")
_RcftRSlotRecvRestrictSpeed_Type = Integer32
_RcftRSlotRecvRestrictSpeed_Object = MibTableColumn
rcftRSlotRecvRestrictSpeed = _RcftRSlotRecvRestrictSpeed_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 119),
    _RcftRSlotRecvRestrictSpeed_Type()
)
rcftRSlotRecvRestrictSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftRSlotRecvRestrictSpeed.setStatus("current")
_RcftRSlotSendRestrictSpeed_Type = Integer32
_RcftRSlotSendRestrictSpeed_Object = MibTableColumn
rcftRSlotSendRestrictSpeed = _RcftRSlotSendRestrictSpeed_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 120),
    _RcftRSlotSendRestrictSpeed_Type()
)
rcftRSlotSendRestrictSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftRSlotSendRestrictSpeed.setStatus("current")
_RcftRSlotV35Speed_Type = Integer32
_RcftRSlotV35Speed_Object = MibTableColumn
rcftRSlotV35Speed = _RcftRSlotV35Speed_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 121),
    _RcftRSlotV35Speed_Type()
)
rcftRSlotV35Speed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftRSlotV35Speed.setStatus("current")


class _RcftRSlotCLKMode_Type(Integer32):
    """Custom type rcftRSlotCLKMode based on Integer32"""
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
        *(("secondary", 1),
          ("v35terminal", 2),
          ("master", 3),
          ("reserved", 4))
    )


_RcftRSlotCLKMode_Type.__name__ = "Integer32"
_RcftRSlotCLKMode_Object = MibTableColumn
rcftRSlotCLKMode = _RcftRSlotCLKMode_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 122),
    _RcftRSlotCLKMode_Type()
)
rcftRSlotCLKMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftRSlotCLKMode.setStatus("current")
_RcftSlotWorkStatus_Type = Integer32
_RcftSlotWorkStatus_Object = MibTableColumn
rcftSlotWorkStatus = _RcftSlotWorkStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 123),
    _RcftSlotWorkStatus_Type()
)
rcftSlotWorkStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftSlotWorkStatus.setStatus("current")
_RcftTxWorkStatus_Type = Integer32
_RcftTxWorkStatus_Object = MibTableColumn
rcftTxWorkStatus = _RcftTxWorkStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 124),
    _RcftTxWorkStatus_Type()
)
rcftTxWorkStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftTxWorkStatus.setStatus("current")
_RcftFxWorkStatus_Type = Integer32
_RcftFxWorkStatus_Object = MibTableColumn
rcftFxWorkStatus = _RcftFxWorkStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 125),
    _RcftFxWorkStatus_Type()
)
rcftFxWorkStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftFxWorkStatus.setStatus("current")
_RcftE1WorkStatus_Type = Integer32
_RcftE1WorkStatus_Object = MibTableColumn
rcftE1WorkStatus = _RcftE1WorkStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 126),
    _RcftE1WorkStatus_Type()
)
rcftE1WorkStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftE1WorkStatus.setStatus("current")
_RcftV35WorkStatus_Type = Integer32
_RcftV35WorkStatus_Object = MibTableColumn
rcftV35WorkStatus = _RcftV35WorkStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 127),
    _RcftV35WorkStatus_Type()
)
rcftV35WorkStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftV35WorkStatus.setStatus("current")
_RcftAllLoopSwitch_Type = Integer32
_RcftAllLoopSwitch_Object = MibTableColumn
rcftAllLoopSwitch = _RcftAllLoopSwitch_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 128),
    _RcftAllLoopSwitch_Type()
)
rcftAllLoopSwitch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftAllLoopSwitch.setStatus("current")
_RcftSlotE1PortAlarm_Type = Integer32
_RcftSlotE1PortAlarm_Object = MibTableColumn
rcftSlotE1PortAlarm = _RcftSlotE1PortAlarm_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 129),
    _RcftSlotE1PortAlarm_Type()
)
rcftSlotE1PortAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftSlotE1PortAlarm.setStatus("current")
_RcftRSlotE1PortAlarm_Type = Integer32
_RcftRSlotE1PortAlarm_Object = MibTableColumn
rcftRSlotE1PortAlarm = _RcftRSlotE1PortAlarm_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 130),
    _RcftRSlotE1PortAlarm_Type()
)
rcftRSlotE1PortAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftRSlotE1PortAlarm.setStatus("current")
_RcftRSlotHardWareDescr_Type = DisplayString
_RcftRSlotHardWareDescr_Object = MibTableColumn
rcftRSlotHardWareDescr = _RcftRSlotHardWareDescr_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 131),
    _RcftRSlotHardWareDescr_Type()
)
rcftRSlotHardWareDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRSlotHardWareDescr.setStatus("current")
_RcftRSlotSigleChipDescr_Type = DisplayString
_RcftRSlotSigleChipDescr_Object = MibTableColumn
rcftRSlotSigleChipDescr = _RcftRSlotSigleChipDescr_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 132),
    _RcftRSlotSigleChipDescr_Type()
)
rcftRSlotSigleChipDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRSlotSigleChipDescr.setStatus("current")
_RcftSlotConfCardType_Type = Integer32
_RcftSlotConfCardType_Object = MibTableColumn
rcftSlotConfCardType = _RcftSlotConfCardType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 133),
    _RcftSlotConfCardType_Type()
)
rcftSlotConfCardType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftSlotConfCardType.setStatus("current")


class _RcftSlotLineStatus_Type(Integer32):
    """Custom type rcftSlotLineStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("remoteNoPower", 1),
          ("remotePowerNormal", 2))
    )


_RcftSlotLineStatus_Type.__name__ = "Integer32"
_RcftSlotLineStatus_Object = MibTableColumn
rcftSlotLineStatus = _RcftSlotLineStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 134),
    _RcftSlotLineStatus_Type()
)
rcftSlotLineStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftSlotLineStatus.setStatus("current")
_RcftV35E1PortExtendStatus_Type = Integer32
_RcftV35E1PortExtendStatus_Object = MibTableColumn
rcftV35E1PortExtendStatus = _RcftV35E1PortExtendStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 135),
    _RcftV35E1PortExtendStatus_Type()
)
rcftV35E1PortExtendStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftV35E1PortExtendStatus.setStatus("current")


class _RcftSlotDoubleLoopSwitch_Type(Integer32):
    """Custom type rcftSlotDoubleLoopSwitch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("localDoubleLoop", 1),
          ("remoteDoubleLoop", 2),
          ("normal", 3),
          ("port2localDoubleLoop", 4),
          ("port2remoteDoubleLoop", 5),
          ("port1localDoubleLoop", 6),
          ("port1remoteDoubleLoop", 7))
    )


_RcftSlotDoubleLoopSwitch_Type.__name__ = "Integer32"
_RcftSlotDoubleLoopSwitch_Object = MibTableColumn
rcftSlotDoubleLoopSwitch = _RcftSlotDoubleLoopSwitch_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 136),
    _RcftSlotDoubleLoopSwitch_Type()
)
rcftSlotDoubleLoopSwitch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftSlotDoubleLoopSwitch.setStatus("current")


class _RcftRSlotDoubleLoopSwitch_Type(Integer32):
    """Custom type rcftRSlotDoubleLoopSwitch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("localDoubleLoop", 1),
          ("remoteDoubleLoop", 2),
          ("normal", 3),
          ("port2localDoubleLoop", 4),
          ("port2remoteDoubleLoop", 5),
          ("port1localDoubleLoop", 6),
          ("port1remoteDoubleLoop", 7))
    )


_RcftRSlotDoubleLoopSwitch_Type.__name__ = "Integer32"
_RcftRSlotDoubleLoopSwitch_Object = MibTableColumn
rcftRSlotDoubleLoopSwitch = _RcftRSlotDoubleLoopSwitch_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 137),
    _RcftRSlotDoubleLoopSwitch_Type()
)
rcftRSlotDoubleLoopSwitch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRSlotDoubleLoopSwitch.setStatus("current")


class _RcftRSlotOport_Type(Integer32):
    """Custom type rcftRSlotOport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("open", 1),
          ("close", 2))
    )


_RcftRSlotOport_Type.__name__ = "Integer32"
_RcftRSlotOport_Object = MibTableColumn
rcftRSlotOport = _RcftRSlotOport_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 138),
    _RcftRSlotOport_Type()
)
rcftRSlotOport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftRSlotOport.setStatus("current")


class _CwdmClientWorkSpeed_Type(Integer32):
    """Custom type cwdmClientWorkSpeed based on Integer32"""
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
              11)
        )
    )
    namedValues = NamedValues(
        *(("stm16-C48", 1),
          ("ge-Gb", 2),
          ("stm4-C12", 3),
          ("stm1-C3", 4),
          ("fe", 5),
          ("auto", 6),
          ("reserved", 7),
          ("speed2fc", 8),
          ("speedfc", 9),
          ("bypass", 10),
          ("stm16-fec", 11))
    )


_CwdmClientWorkSpeed_Type.__name__ = "Integer32"
_CwdmClientWorkSpeed_Object = MibTableColumn
cwdmClientWorkSpeed = _CwdmClientWorkSpeed_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 139),
    _CwdmClientWorkSpeed_Type()
)
cwdmClientWorkSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwdmClientWorkSpeed.setStatus("current")
_CwdmCWDMWorkStatus_Type = Integer32
_CwdmCWDMWorkStatus_Object = MibTableColumn
cwdmCWDMWorkStatus = _CwdmCWDMWorkStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 140),
    _CwdmCWDMWorkStatus_Type()
)
cwdmCWDMWorkStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwdmCWDMWorkStatus.setStatus("current")
_CwdmCWDMModuleMaxSpeed_Type = Integer32
_CwdmCWDMModuleMaxSpeed_Object = MibTableColumn
cwdmCWDMModuleMaxSpeed = _CwdmCWDMModuleMaxSpeed_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 141),
    _CwdmCWDMModuleMaxSpeed_Type()
)
cwdmCWDMModuleMaxSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwdmCWDMModuleMaxSpeed.setStatus("current")
_CwdmCWDMModuleTransLen_Type = Integer32
_CwdmCWDMModuleTransLen_Object = MibTableColumn
cwdmCWDMModuleTransLen = _CwdmCWDMModuleTransLen_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 142),
    _CwdmCWDMModuleTransLen_Type()
)
cwdmCWDMModuleTransLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwdmCWDMModuleTransLen.setStatus("current")
_CwdmCWDMModuleWaveLen_Type = Integer32
_CwdmCWDMModuleWaveLen_Object = MibTableColumn
cwdmCWDMModuleWaveLen = _CwdmCWDMModuleWaveLen_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 143),
    _CwdmCWDMModuleWaveLen_Type()
)
cwdmCWDMModuleWaveLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwdmCWDMModuleWaveLen.setStatus("current")


class _CwdmCWDMModuleManufacturer_Type(OctetString):
    """Custom type cwdmCWDMModuleManufacturer based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_CwdmCWDMModuleManufacturer_Type.__name__ = "OctetString"
_CwdmCWDMModuleManufacturer_Object = MibTableColumn
cwdmCWDMModuleManufacturer = _CwdmCWDMModuleManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 144),
    _CwdmCWDMModuleManufacturer_Type()
)
cwdmCWDMModuleManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwdmCWDMModuleManufacturer.setStatus("current")


class _CwdmCWDMModuleDescr_Type(OctetString):
    """Custom type cwdmCWDMModuleDescr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_CwdmCWDMModuleDescr_Type.__name__ = "OctetString"
_CwdmCWDMModuleDescr_Object = MibTableColumn
cwdmCWDMModuleDescr = _CwdmCWDMModuleDescr_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 145),
    _CwdmCWDMModuleDescr_Type()
)
cwdmCWDMModuleDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwdmCWDMModuleDescr.setStatus("current")


class _CwdmCWDMModuleVersion_Type(OctetString):
    """Custom type cwdmCWDMModuleVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_CwdmCWDMModuleVersion_Type.__name__ = "OctetString"
_CwdmCWDMModuleVersion_Object = MibTableColumn
cwdmCWDMModuleVersion = _CwdmCWDMModuleVersion_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 146),
    _CwdmCWDMModuleVersion_Type()
)
cwdmCWDMModuleVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwdmCWDMModuleVersion.setStatus("current")


class _CwdmCWDMModuleSerialNumber_Type(OctetString):
    """Custom type cwdmCWDMModuleSerialNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_CwdmCWDMModuleSerialNumber_Type.__name__ = "OctetString"
_CwdmCWDMModuleSerialNumber_Object = MibTableColumn
cwdmCWDMModuleSerialNumber = _CwdmCWDMModuleSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 147),
    _CwdmCWDMModuleSerialNumber_Type()
)
cwdmCWDMModuleSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwdmCWDMModuleSerialNumber.setStatus("current")
_CwdmClientWorkStatus_Type = Integer32
_CwdmClientWorkStatus_Object = MibTableColumn
cwdmClientWorkStatus = _CwdmClientWorkStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 148),
    _CwdmClientWorkStatus_Type()
)
cwdmClientWorkStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwdmClientWorkStatus.setStatus("current")
_CwdmClientModuleMaxSpeed_Type = Integer32
_CwdmClientModuleMaxSpeed_Object = MibTableColumn
cwdmClientModuleMaxSpeed = _CwdmClientModuleMaxSpeed_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 149),
    _CwdmClientModuleMaxSpeed_Type()
)
cwdmClientModuleMaxSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwdmClientModuleMaxSpeed.setStatus("current")
_CwdmClientModuleInterfaceType_Type = Integer32
_CwdmClientModuleInterfaceType_Object = MibTableColumn
cwdmClientModuleInterfaceType = _CwdmClientModuleInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 150),
    _CwdmClientModuleInterfaceType_Type()
)
cwdmClientModuleInterfaceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwdmClientModuleInterfaceType.setStatus("current")
_CwdmClientModuleTransLen_Type = Integer32
_CwdmClientModuleTransLen_Object = MibTableColumn
cwdmClientModuleTransLen = _CwdmClientModuleTransLen_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 151),
    _CwdmClientModuleTransLen_Type()
)
cwdmClientModuleTransLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwdmClientModuleTransLen.setStatus("current")
_CwdmClientModuleWaveLen_Type = Integer32
_CwdmClientModuleWaveLen_Object = MibTableColumn
cwdmClientModuleWaveLen = _CwdmClientModuleWaveLen_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 152),
    _CwdmClientModuleWaveLen_Type()
)
cwdmClientModuleWaveLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwdmClientModuleWaveLen.setStatus("current")


class _CwdmClientModuleManufacturer_Type(OctetString):
    """Custom type cwdmClientModuleManufacturer based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_CwdmClientModuleManufacturer_Type.__name__ = "OctetString"
_CwdmClientModuleManufacturer_Object = MibTableColumn
cwdmClientModuleManufacturer = _CwdmClientModuleManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 153),
    _CwdmClientModuleManufacturer_Type()
)
cwdmClientModuleManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwdmClientModuleManufacturer.setStatus("current")


class _CwdmClientModuleDescr_Type(OctetString):
    """Custom type cwdmClientModuleDescr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_CwdmClientModuleDescr_Type.__name__ = "OctetString"
_CwdmClientModuleDescr_Object = MibTableColumn
cwdmClientModuleDescr = _CwdmClientModuleDescr_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 154),
    _CwdmClientModuleDescr_Type()
)
cwdmClientModuleDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwdmClientModuleDescr.setStatus("current")


class _CwdmClientModuleVersion_Type(OctetString):
    """Custom type cwdmClientModuleVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_CwdmClientModuleVersion_Type.__name__ = "OctetString"
_CwdmClientModuleVersion_Object = MibTableColumn
cwdmClientModuleVersion = _CwdmClientModuleVersion_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 155),
    _CwdmClientModuleVersion_Type()
)
cwdmClientModuleVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwdmClientModuleVersion.setStatus("current")


class _CwdmClientModuleSerialNumber_Type(OctetString):
    """Custom type cwdmClientModuleSerialNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_CwdmClientModuleSerialNumber_Type.__name__ = "OctetString"
_CwdmClientModuleSerialNumber_Object = MibTableColumn
cwdmClientModuleSerialNumber = _CwdmClientModuleSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 156),
    _CwdmClientModuleSerialNumber_Type()
)
cwdmClientModuleSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwdmClientModuleSerialNumber.setStatus("current")


class _CwdmCWDMWorkSpeed_Type(Integer32):
    """Custom type cwdmCWDMWorkSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("stm16-C48", 1),
          ("ge-Gb", 2),
          ("stm4-C12", 3),
          ("stm1-C3", 4),
          ("fe", 5),
          ("auto", 6),
          ("reserved", 7))
    )


_CwdmCWDMWorkSpeed_Type.__name__ = "Integer32"
_CwdmCWDMWorkSpeed_Object = MibTableColumn
cwdmCWDMWorkSpeed = _CwdmCWDMWorkSpeed_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 157),
    _CwdmCWDMWorkSpeed_Type()
)
cwdmCWDMWorkSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwdmCWDMWorkSpeed.setStatus("current")


class _OpticalModuleType_Type(Integer32):
    """Custom type opticalModuleType based on Integer32"""
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
              12,
              15,
              50,
              51,
              52,
              53,
              100)
        )
    )
    namedValues = NamedValues(
        *(("optical-M", 1),
          ("optical-S1", 2),
          ("optical-S2", 3),
          ("optical-S3", 4),
          ("optical-SS13", 5),
          ("optical-SS15", 6),
          ("optical-SS23", 7),
          ("optical-SS25", 8),
          ("optical-SS34", 9),
          ("optical-SS35", 10),
          ("optical-S15", 12),
          ("optical-SFP", 15),
          ("optical-S1FC", 50),
          ("optical-S1A", 51),
          ("optical-S2A", 52),
          ("optical-S3A", 53),
          ("unknown-type", 100))
    )


_OpticalModuleType_Type.__name__ = "Integer32"
_OpticalModuleType_Object = MibTableColumn
opticalModuleType = _OpticalModuleType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 158),
    _OpticalModuleType_Type()
)
opticalModuleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    opticalModuleType.setStatus("current")


class _RcftSlotInformation_Type(OctetString):
    """Custom type rcftSlotInformation based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_RcftSlotInformation_Type.__name__ = "OctetString"
_RcftSlotInformation_Object = MibTableColumn
rcftSlotInformation = _RcftSlotInformation_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 159),
    _RcftSlotInformation_Type()
)
rcftSlotInformation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftSlotInformation.setStatus("current")


class _RemoteOpticalModuleType_Type(Integer32):
    """Custom type remoteOpticalModuleType based on Integer32"""
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
              12,
              15,
              50,
              51,
              52,
              53,
              100)
        )
    )
    namedValues = NamedValues(
        *(("optical-M", 1),
          ("optical-S1", 2),
          ("optical-S2", 3),
          ("optical-S3", 4),
          ("optical-SS13", 5),
          ("optical-SS15", 6),
          ("optical-SS23", 7),
          ("optical-SS25", 8),
          ("optical-SS34", 9),
          ("optical-SS35", 10),
          ("optical-S15", 12),
          ("optical-SFP", 15),
          ("optical-S1FC", 50),
          ("optical-S1A", 51),
          ("optical-S2A", 52),
          ("optical-S3A", 53),
          ("unknown-type", 100))
    )


_RemoteOpticalModuleType_Type.__name__ = "Integer32"
_RemoteOpticalModuleType_Object = MibTableColumn
remoteOpticalModuleType = _RemoteOpticalModuleType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 160),
    _RemoteOpticalModuleType_Type()
)
remoteOpticalModuleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteOpticalModuleType.setStatus("current")


class _RcftRSlotInformation_Type(OctetString):
    """Custom type rcftRSlotInformation based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_RcftRSlotInformation_Type.__name__ = "OctetString"
_RcftRSlotInformation_Object = MibTableColumn
rcftRSlotInformation = _RcftRSlotInformation_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 161),
    _RcftRSlotInformation_Type()
)
rcftRSlotInformation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRSlotInformation.setStatus("current")
_RcftRSlotRevFluxCount_Type = Integer32
_RcftRSlotRevFluxCount_Object = MibTableColumn
rcftRSlotRevFluxCount = _RcftRSlotRevFluxCount_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 162),
    _RcftRSlotRevFluxCount_Type()
)
rcftRSlotRevFluxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRSlotRevFluxCount.setStatus("current")
_RcftRSlotSedFluxCount_Type = Integer32
_RcftRSlotSedFluxCount_Object = MibTableColumn
rcftRSlotSedFluxCount = _RcftRSlotSedFluxCount_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 163),
    _RcftRSlotSedFluxCount_Type()
)
rcftRSlotSedFluxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRSlotSedFluxCount.setStatus("current")
_RcftRSlotRevFluxTimer_Type = Integer32
_RcftRSlotRevFluxTimer_Object = MibTableColumn
rcftRSlotRevFluxTimer = _RcftRSlotRevFluxTimer_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 164),
    _RcftRSlotRevFluxTimer_Type()
)
rcftRSlotRevFluxTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRSlotRevFluxTimer.setStatus("current")
_RcftRSlotSedFluxTimer_Type = Integer32
_RcftRSlotSedFluxTimer_Object = MibTableColumn
rcftRSlotSedFluxTimer = _RcftRSlotSedFluxTimer_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 165),
    _RcftRSlotSedFluxTimer_Type()
)
rcftRSlotSedFluxTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRSlotSedFluxTimer.setStatus("current")
_RcftSlotRevErrFluxCnt_Type = Integer32
_RcftSlotRevErrFluxCnt_Object = MibTableColumn
rcftSlotRevErrFluxCnt = _RcftSlotRevErrFluxCnt_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 166),
    _RcftSlotRevErrFluxCnt_Type()
)
rcftSlotRevErrFluxCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftSlotRevErrFluxCnt.setStatus("current")
_RcftSlotSedErrFluxCnt_Type = Integer32
_RcftSlotSedErrFluxCnt_Object = MibTableColumn
rcftSlotSedErrFluxCnt = _RcftSlotSedErrFluxCnt_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 167),
    _RcftSlotSedErrFluxCnt_Type()
)
rcftSlotSedErrFluxCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftSlotSedErrFluxCnt.setStatus("current")


class _CwdmOMUmoduleType_Type(Integer32):
    """Custom type cwdmOMUmoduleType based on Integer32"""
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
        *(("wave-seperate", 1),
          ("wave-unite", 2),
          ("wave-coupling-4", 3),
          ("reserved", 4))
    )


_CwdmOMUmoduleType_Type.__name__ = "Integer32"
_CwdmOMUmoduleType_Object = MibTableColumn
cwdmOMUmoduleType = _CwdmOMUmoduleType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 168),
    _CwdmOMUmoduleType_Type()
)
cwdmOMUmoduleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwdmOMUmoduleType.setStatus("current")
_RcftSlotE1TimeSlot_Type = Unsigned32
_RcftSlotE1TimeSlot_Object = MibTableColumn
rcftSlotE1TimeSlot = _RcftSlotE1TimeSlot_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 169),
    _RcftSlotE1TimeSlot_Type()
)
rcftSlotE1TimeSlot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftSlotE1TimeSlot.setStatus("current")
_RcftSlotWANRevFluxPacket_Type = Integer32
_RcftSlotWANRevFluxPacket_Object = MibTableColumn
rcftSlotWANRevFluxPacket = _RcftSlotWANRevFluxPacket_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 170),
    _RcftSlotWANRevFluxPacket_Type()
)
rcftSlotWANRevFluxPacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftSlotWANRevFluxPacket.setStatus("current")
_RcftSlotWANRevFluxCount_Type = Integer32
_RcftSlotWANRevFluxCount_Object = MibTableColumn
rcftSlotWANRevFluxCount = _RcftSlotWANRevFluxCount_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 171),
    _RcftSlotWANRevFluxCount_Type()
)
rcftSlotWANRevFluxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftSlotWANRevFluxCount.setStatus("current")
_RcftSlotWANSedFluxPacket_Type = Integer32
_RcftSlotWANSedFluxPacket_Object = MibTableColumn
rcftSlotWANSedFluxPacket = _RcftSlotWANSedFluxPacket_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 172),
    _RcftSlotWANSedFluxPacket_Type()
)
rcftSlotWANSedFluxPacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftSlotWANSedFluxPacket.setStatus("current")
_RcftSlotWANSedFluxCount_Type = Integer32
_RcftSlotWANSedFluxCount_Object = MibTableColumn
rcftSlotWANSedFluxCount = _RcftSlotWANSedFluxCount_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 173),
    _RcftSlotWANSedFluxCount_Type()
)
rcftSlotWANSedFluxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftSlotWANSedFluxCount.setStatus("current")
_RcftSlotWANRevErrFluxPacket_Type = Integer32
_RcftSlotWANRevErrFluxPacket_Object = MibTableColumn
rcftSlotWANRevErrFluxPacket = _RcftSlotWANRevErrFluxPacket_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 174),
    _RcftSlotWANRevErrFluxPacket_Type()
)
rcftSlotWANRevErrFluxPacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftSlotWANRevErrFluxPacket.setStatus("current")
_RcftSlotRevFluxPacket_Type = Integer32
_RcftSlotRevFluxPacket_Object = MibTableColumn
rcftSlotRevFluxPacket = _RcftSlotRevFluxPacket_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 175),
    _RcftSlotRevFluxPacket_Type()
)
rcftSlotRevFluxPacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftSlotRevFluxPacket.setStatus("current")
_RcftSlotSedFluxPacket_Type = Integer32
_RcftSlotSedFluxPacket_Object = MibTableColumn
rcftSlotSedFluxPacket = _RcftSlotSedFluxPacket_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 176),
    _RcftSlotSedFluxPacket_Type()
)
rcftSlotSedFluxPacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftSlotSedFluxPacket.setStatus("current")
_RcftRSlotE1TimeSlot_Type = Unsigned32
_RcftRSlotE1TimeSlot_Object = MibTableColumn
rcftRSlotE1TimeSlot = _RcftRSlotE1TimeSlot_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 177),
    _RcftRSlotE1TimeSlot_Type()
)
rcftRSlotE1TimeSlot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftRSlotE1TimeSlot.setStatus("current")
_RcftRSlotWANRevFluxPacket_Type = Integer32
_RcftRSlotWANRevFluxPacket_Object = MibTableColumn
rcftRSlotWANRevFluxPacket = _RcftRSlotWANRevFluxPacket_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 178),
    _RcftRSlotWANRevFluxPacket_Type()
)
rcftRSlotWANRevFluxPacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRSlotWANRevFluxPacket.setStatus("current")
_RcftRSlotWANRevFluxCount_Type = Integer32
_RcftRSlotWANRevFluxCount_Object = MibTableColumn
rcftRSlotWANRevFluxCount = _RcftRSlotWANRevFluxCount_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 179),
    _RcftRSlotWANRevFluxCount_Type()
)
rcftRSlotWANRevFluxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRSlotWANRevFluxCount.setStatus("current")
_RcftRSlotWANSedFluxPacket_Type = Integer32
_RcftRSlotWANSedFluxPacket_Object = MibTableColumn
rcftRSlotWANSedFluxPacket = _RcftRSlotWANSedFluxPacket_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 180),
    _RcftRSlotWANSedFluxPacket_Type()
)
rcftRSlotWANSedFluxPacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRSlotWANSedFluxPacket.setStatus("current")
_RcftRSlotWANSedFluxCount_Type = Integer32
_RcftRSlotWANSedFluxCount_Object = MibTableColumn
rcftRSlotWANSedFluxCount = _RcftRSlotWANSedFluxCount_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 181),
    _RcftRSlotWANSedFluxCount_Type()
)
rcftRSlotWANSedFluxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRSlotWANSedFluxCount.setStatus("current")
_RcftRSlotWANRevErrFluxPacket_Type = Integer32
_RcftRSlotWANRevErrFluxPacket_Object = MibTableColumn
rcftRSlotWANRevErrFluxPacket = _RcftRSlotWANRevErrFluxPacket_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 182),
    _RcftRSlotWANRevErrFluxPacket_Type()
)
rcftRSlotWANRevErrFluxPacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRSlotWANRevErrFluxPacket.setStatus("current")
_RcftRSlotRevFluxPacket_Type = Integer32
_RcftRSlotRevFluxPacket_Object = MibTableColumn
rcftRSlotRevFluxPacket = _RcftRSlotRevFluxPacket_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 183),
    _RcftRSlotRevFluxPacket_Type()
)
rcftRSlotRevFluxPacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRSlotRevFluxPacket.setStatus("current")
_RcftRSlotSedFluxPacket_Type = Integer32
_RcftRSlotSedFluxPacket_Object = MibTableColumn
rcftRSlotSedFluxPacket = _RcftRSlotSedFluxPacket_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 184),
    _RcftRSlotSedFluxPacket_Type()
)
rcftRSlotSedFluxPacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRSlotSedFluxPacket.setStatus("current")
_RcftRSlotRevErrFluxCnt_Type = Integer32
_RcftRSlotRevErrFluxCnt_Object = MibTableColumn
rcftRSlotRevErrFluxCnt = _RcftRSlotRevErrFluxCnt_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 185),
    _RcftRSlotRevErrFluxCnt_Type()
)
rcftRSlotRevErrFluxCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRSlotRevErrFluxCnt.setStatus("current")
_RcftExtentWorkStatus_Type = Integer32
_RcftExtentWorkStatus_Object = MibTableColumn
rcftExtentWorkStatus = _RcftExtentWorkStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 186),
    _RcftExtentWorkStatus_Type()
)
rcftExtentWorkStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftExtentWorkStatus.setStatus("current")
_RcftSlotE1ESCnt_Type = Integer32
_RcftSlotE1ESCnt_Object = MibTableColumn
rcftSlotE1ESCnt = _RcftSlotE1ESCnt_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 187),
    _RcftSlotE1ESCnt_Type()
)
rcftSlotE1ESCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftSlotE1ESCnt.setStatus("current")
_RcftSlotE1SESCnt_Type = Integer32
_RcftSlotE1SESCnt_Object = MibTableColumn
rcftSlotE1SESCnt = _RcftSlotE1SESCnt_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 188),
    _RcftSlotE1SESCnt_Type()
)
rcftSlotE1SESCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftSlotE1SESCnt.setStatus("current")
_RcftRSlotE1ESCnt_Type = Integer32
_RcftRSlotE1ESCnt_Object = MibTableColumn
rcftRSlotE1ESCnt = _RcftRSlotE1ESCnt_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 189),
    _RcftRSlotE1ESCnt_Type()
)
rcftRSlotE1ESCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRSlotE1ESCnt.setStatus("current")
_RcftRSlotE1SESCnt_Type = Integer32
_RcftRSlotE1SESCnt_Object = MibTableColumn
rcftRSlotE1SESCnt = _RcftRSlotE1SESCnt_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 190),
    _RcftRSlotE1SESCnt_Type()
)
rcftRSlotE1SESCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRSlotE1SESCnt.setStatus("current")
_RcftRSlotCWDMModuleMaxSpeed_Type = Integer32
_RcftRSlotCWDMModuleMaxSpeed_Object = MibTableColumn
rcftRSlotCWDMModuleMaxSpeed = _RcftRSlotCWDMModuleMaxSpeed_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 191),
    _RcftRSlotCWDMModuleMaxSpeed_Type()
)
rcftRSlotCWDMModuleMaxSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRSlotCWDMModuleMaxSpeed.setStatus("current")
_RcftRSlotCWDMModuleTransLen_Type = Integer32
_RcftRSlotCWDMModuleTransLen_Object = MibTableColumn
rcftRSlotCWDMModuleTransLen = _RcftRSlotCWDMModuleTransLen_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 192),
    _RcftRSlotCWDMModuleTransLen_Type()
)
rcftRSlotCWDMModuleTransLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRSlotCWDMModuleTransLen.setStatus("current")
_RcftRSlotCWDMModuleWaveLen_Type = Integer32
_RcftRSlotCWDMModuleWaveLen_Object = MibTableColumn
rcftRSlotCWDMModuleWaveLen = _RcftRSlotCWDMModuleWaveLen_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 193),
    _RcftRSlotCWDMModuleWaveLen_Type()
)
rcftRSlotCWDMModuleWaveLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRSlotCWDMModuleWaveLen.setStatus("current")


class _RcftRSlotCWDMModuleManufacturer_Type(OctetString):
    """Custom type rcftRSlotCWDMModuleManufacturer based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_RcftRSlotCWDMModuleManufacturer_Type.__name__ = "OctetString"
_RcftRSlotCWDMModuleManufacturer_Object = MibTableColumn
rcftRSlotCWDMModuleManufacturer = _RcftRSlotCWDMModuleManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 194),
    _RcftRSlotCWDMModuleManufacturer_Type()
)
rcftRSlotCWDMModuleManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRSlotCWDMModuleManufacturer.setStatus("current")


class _RcftRSlotCWDMModuleDescr_Type(OctetString):
    """Custom type rcftRSlotCWDMModuleDescr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_RcftRSlotCWDMModuleDescr_Type.__name__ = "OctetString"
_RcftRSlotCWDMModuleDescr_Object = MibTableColumn
rcftRSlotCWDMModuleDescr = _RcftRSlotCWDMModuleDescr_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 195),
    _RcftRSlotCWDMModuleDescr_Type()
)
rcftRSlotCWDMModuleDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRSlotCWDMModuleDescr.setStatus("current")


class _RcftRSlotCWDMModuleVersion_Type(OctetString):
    """Custom type rcftRSlotCWDMModuleVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_RcftRSlotCWDMModuleVersion_Type.__name__ = "OctetString"
_RcftRSlotCWDMModuleVersion_Object = MibTableColumn
rcftRSlotCWDMModuleVersion = _RcftRSlotCWDMModuleVersion_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 196),
    _RcftRSlotCWDMModuleVersion_Type()
)
rcftRSlotCWDMModuleVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRSlotCWDMModuleVersion.setStatus("current")


class _RcftRSlotCWDMModuleSerialNumber_Type(OctetString):
    """Custom type rcftRSlotCWDMModuleSerialNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_RcftRSlotCWDMModuleSerialNumber_Type.__name__ = "OctetString"
_RcftRSlotCWDMModuleSerialNumber_Object = MibTableColumn
rcftRSlotCWDMModuleSerialNumber = _RcftRSlotCWDMModuleSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 197),
    _RcftRSlotCWDMModuleSerialNumber_Type()
)
rcftRSlotCWDMModuleSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRSlotCWDMModuleSerialNumber.setStatus("current")


class _RcftSlotLANOPortModuleType_Type(Integer32):
    """Custom type rcftSlotLANOPortModuleType based on Integer32"""
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
              100)
        )
    )
    namedValues = NamedValues(
        *(("optical-M", 1),
          ("optical-S1", 2),
          ("optical-S2", 3),
          ("optical-S3", 4),
          ("optical-SS13", 5),
          ("optical-SS15", 6),
          ("optical-SS23", 7),
          ("optical-SS25", 8),
          ("optical-SS35", 9),
          ("unknown-type", 100))
    )


_RcftSlotLANOPortModuleType_Type.__name__ = "Integer32"
_RcftSlotLANOPortModuleType_Object = MibTableColumn
rcftSlotLANOPortModuleType = _RcftSlotLANOPortModuleType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 198),
    _RcftSlotLANOPortModuleType_Type()
)
rcftSlotLANOPortModuleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftSlotLANOPortModuleType.setStatus("current")


class _RcftSlotWANOPortModuleType_Type(Integer32):
    """Custom type rcftSlotWANOPortModuleType based on Integer32"""
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
              100)
        )
    )
    namedValues = NamedValues(
        *(("optical-M", 1),
          ("optical-S1", 2),
          ("optical-S2", 3),
          ("optical-S3", 4),
          ("optical-SS13", 5),
          ("optical-SS15", 6),
          ("optical-SS23", 7),
          ("optical-SS25", 8),
          ("optical-SS35", 9),
          ("unknown-type", 100))
    )


_RcftSlotWANOPortModuleType_Type.__name__ = "Integer32"
_RcftSlotWANOPortModuleType_Object = MibTableColumn
rcftSlotWANOPortModuleType = _RcftSlotWANOPortModuleType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 199),
    _RcftSlotWANOPortModuleType_Type()
)
rcftSlotWANOPortModuleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftSlotWANOPortModuleType.setStatus("current")


class _RcftSlotCDRSpeed_Type(Integer32):
    """Custom type rcftSlotCDRSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("stm16-C48", 1),
          ("ge-Gb", 2),
          ("stm4-C12", 3),
          ("stm1-C3", 4),
          ("fe", 5),
          ("auto", 6),
          ("reserved", 7))
    )


_RcftSlotCDRSpeed_Type.__name__ = "Integer32"
_RcftSlotCDRSpeed_Object = MibTableColumn
rcftSlotCDRSpeed = _RcftSlotCDRSpeed_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 200),
    _RcftSlotCDRSpeed_Type()
)
rcftSlotCDRSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftSlotCDRSpeed.setStatus("current")


class _RcftRSlotManufacturer_Type(OctetString):
    """Custom type rcftRSlotManufacturer based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 60),
    )


_RcftRSlotManufacturer_Type.__name__ = "OctetString"
_RcftRSlotManufacturer_Object = MibTableColumn
rcftRSlotManufacturer = _RcftRSlotManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 201),
    _RcftRSlotManufacturer_Type()
)
rcftRSlotManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRSlotManufacturer.setStatus("current")


class _RcftRSlotSoftwareVersion_Type(OctetString):
    """Custom type rcftRSlotSoftwareVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_RcftRSlotSoftwareVersion_Type.__name__ = "OctetString"
_RcftRSlotSoftwareVersion_Object = MibTableColumn
rcftRSlotSoftwareVersion = _RcftRSlotSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 202),
    _RcftRSlotSoftwareVersion_Type()
)
rcftRSlotSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRSlotSoftwareVersion.setStatus("current")
_RcftRSlotVoltageValue_Type = Unsigned32
_RcftRSlotVoltageValue_Object = MibTableColumn
rcftRSlotVoltageValue = _RcftRSlotVoltageValue_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 203),
    _RcftRSlotVoltageValue_Type()
)
rcftRSlotVoltageValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRSlotVoltageValue.setStatus("current")


class _RcftRSlotCommunityRW_Type(Integer32):
    """Custom type rcftRSlotCommunityRW based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("read", 1),
          ("readwrite", 2),
          ("reserved", 3))
    )


_RcftRSlotCommunityRW_Type.__name__ = "Integer32"
_RcftRSlotCommunityRW_Object = MibTableColumn
rcftRSlotCommunityRW = _RcftRSlotCommunityRW_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 204),
    _RcftRSlotCommunityRW_Type()
)
rcftRSlotCommunityRW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRSlotCommunityRW.setStatus("current")


class _RcftRSlotCommunity_Type(OctetString):
    """Custom type rcftRSlotCommunity based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_RcftRSlotCommunity_Type.__name__ = "OctetString"
_RcftRSlotCommunity_Object = MibTableColumn
rcftRSlotCommunity = _RcftRSlotCommunity_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 205),
    _RcftRSlotCommunity_Type()
)
rcftRSlotCommunity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRSlotCommunity.setStatus("current")


class _RcftRSlotDeviceIP_Type(OctetString):
    """Custom type rcftRSlotDeviceIP based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_RcftRSlotDeviceIP_Type.__name__ = "OctetString"
_RcftRSlotDeviceIP_Object = MibTableColumn
rcftRSlotDeviceIP = _RcftRSlotDeviceIP_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 206),
    _RcftRSlotDeviceIP_Type()
)
rcftRSlotDeviceIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRSlotDeviceIP.setStatus("current")
_RcftSlotLinePortSpeed_Type = Integer32
_RcftSlotLinePortSpeed_Object = MibTableColumn
rcftSlotLinePortSpeed = _RcftSlotLinePortSpeed_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 207),
    _RcftSlotLinePortSpeed_Type()
)
rcftSlotLinePortSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftSlotLinePortSpeed.setStatus("current")
_RcftSlotLinePortMaxSpeed_Type = Integer32
_RcftSlotLinePortMaxSpeed_Object = MibTableColumn
rcftSlotLinePortMaxSpeed = _RcftSlotLinePortMaxSpeed_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 208),
    _RcftSlotLinePortMaxSpeed_Type()
)
rcftSlotLinePortMaxSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftSlotLinePortMaxSpeed.setStatus("current")
_RcftSlotLinePortMinSpeed_Type = Integer32
_RcftSlotLinePortMinSpeed_Object = MibTableColumn
rcftSlotLinePortMinSpeed = _RcftSlotLinePortMinSpeed_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 209),
    _RcftSlotLinePortMinSpeed_Type()
)
rcftSlotLinePortMinSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftSlotLinePortMinSpeed.setStatus("current")
_RcftSlotLinePortSNR_Type = Integer32
_RcftSlotLinePortSNR_Object = MibTableColumn
rcftSlotLinePortSNR = _RcftSlotLinePortSNR_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 210),
    _RcftSlotLinePortSNR_Type()
)
rcftSlotLinePortSNR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftSlotLinePortSNR.setStatus("current")
_RcftSlotLinePortLinkUpTime_Type = Unsigned32
_RcftSlotLinePortLinkUpTime_Object = MibTableColumn
rcftSlotLinePortLinkUpTime = _RcftSlotLinePortLinkUpTime_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 211),
    _RcftSlotLinePortLinkUpTime_Type()
)
rcftSlotLinePortLinkUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftSlotLinePortLinkUpTime.setStatus("current")
_RcftRSlotLinePortSNR_Type = Integer32
_RcftRSlotLinePortSNR_Object = MibTableColumn
rcftRSlotLinePortSNR = _RcftRSlotLinePortSNR_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 212),
    _RcftRSlotLinePortSNR_Type()
)
rcftRSlotLinePortSNR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftRSlotLinePortSNR.setStatus("current")
_RcftRSlotLinePortLinkUpTime_Type = Unsigned32
_RcftRSlotLinePortLinkUpTime_Object = MibTableColumn
rcftRSlotLinePortLinkUpTime = _RcftRSlotLinePortLinkUpTime_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 213),
    _RcftRSlotLinePortLinkUpTime_Type()
)
rcftRSlotLinePortLinkUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRSlotLinePortLinkUpTime.setStatus("current")
_RcftRSlotLinePortSpeed_Type = Integer32
_RcftRSlotLinePortSpeed_Object = MibTableColumn
rcftRSlotLinePortSpeed = _RcftRSlotLinePortSpeed_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 214),
    _RcftRSlotLinePortSpeed_Type()
)
rcftRSlotLinePortSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftRSlotLinePortSpeed.setStatus("current")
_RcftSlotOrderParameter_Type = Integer32
_RcftSlotOrderParameter_Object = MibTableColumn
rcftSlotOrderParameter = _RcftSlotOrderParameter_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 215),
    _RcftSlotOrderParameter_Type()
)
rcftSlotOrderParameter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftSlotOrderParameter.setStatus("current")
_RcftRSlotOrderParameter_Type = Integer32
_RcftRSlotOrderParameter_Object = MibTableColumn
rcftRSlotOrderParameter = _RcftRSlotOrderParameter_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 216),
    _RcftRSlotOrderParameter_Type()
)
rcftRSlotOrderParameter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftRSlotOrderParameter.setStatus("current")
_RcftSlotRevErrFluxPacket_Type = Integer32
_RcftSlotRevErrFluxPacket_Object = MibTableColumn
rcftSlotRevErrFluxPacket = _RcftSlotRevErrFluxPacket_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 217),
    _RcftSlotRevErrFluxPacket_Type()
)
rcftSlotRevErrFluxPacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftSlotRevErrFluxPacket.setStatus("current")
_RcftRSlotRevErrFluxPacket_Type = Integer32
_RcftRSlotRevErrFluxPacket_Object = MibTableColumn
rcftRSlotRevErrFluxPacket = _RcftRSlotRevErrFluxPacket_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 218),
    _RcftRSlotRevErrFluxPacket_Type()
)
rcftRSlotRevErrFluxPacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRSlotRevErrFluxPacket.setStatus("current")


class _RcftRSlotLinePortType_Type(Integer32):
    """Custom type rcftRSlotLinePortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              10)
        )
    )
    namedValues = NamedValues(
        *(("e1", 1),
          ("opt", 2),
          ("ghdsl", 3),
          ("reserved", 10))
    )


_RcftRSlotLinePortType_Type.__name__ = "Integer32"
_RcftRSlotLinePortType_Object = MibTableColumn
rcftRSlotLinePortType = _RcftRSlotLinePortType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 219),
    _RcftRSlotLinePortType_Type()
)
rcftRSlotLinePortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRSlotLinePortType.setStatus("current")


class _RcftRSlotManageChannelSel_Type(Integer32):
    """Custom type rcftRSlotManageChannelSel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("aloneTimeSlot", 1),
          ("optChannels", 2),
          ("saChannels", 3))
    )


_RcftRSlotManageChannelSel_Type.__name__ = "Integer32"
_RcftRSlotManageChannelSel_Object = MibTableColumn
rcftRSlotManageChannelSel = _RcftRSlotManageChannelSel_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 220),
    _RcftRSlotManageChannelSel_Type()
)
rcftRSlotManageChannelSel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftRSlotManageChannelSel.setStatus("current")
_RcftRSlotManageChannelTSNum_Type = Integer32
_RcftRSlotManageChannelTSNum_Object = MibTableColumn
rcftRSlotManageChannelTSNum = _RcftRSlotManageChannelTSNum_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 221),
    _RcftRSlotManageChannelTSNum_Type()
)
rcftRSlotManageChannelTSNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftRSlotManageChannelTSNum.setStatus("current")
_RcftRSlotV35TimeSlots_Type = Unsigned32
_RcftRSlotV35TimeSlots_Object = MibTableColumn
rcftRSlotV35TimeSlots = _RcftRSlotV35TimeSlots_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 222),
    _RcftRSlotV35TimeSlots_Type()
)
rcftRSlotV35TimeSlots.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftRSlotV35TimeSlots.setStatus("current")
_RcftSlotLinePortSNRConf_Type = Integer32
_RcftSlotLinePortSNRConf_Object = MibTableColumn
rcftSlotLinePortSNRConf = _RcftSlotLinePortSNRConf_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 223),
    _RcftSlotLinePortSNRConf_Type()
)
rcftSlotLinePortSNRConf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftSlotLinePortSNRConf.setStatus("current")


class _RcftRSlotLANOPortModuleType_Type(Integer32):
    """Custom type rcftRSlotLANOPortModuleType based on Integer32"""
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
              100)
        )
    )
    namedValues = NamedValues(
        *(("optical-M", 1),
          ("optical-S1", 2),
          ("optical-S2", 3),
          ("optical-S3", 4),
          ("optical-SS13", 5),
          ("optical-SS15", 6),
          ("optical-SS23", 7),
          ("optical-SS25", 8),
          ("optical-SS35", 9),
          ("unknown-type", 100))
    )


_RcftRSlotLANOPortModuleType_Type.__name__ = "Integer32"
_RcftRSlotLANOPortModuleType_Object = MibTableColumn
rcftRSlotLANOPortModuleType = _RcftRSlotLANOPortModuleType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 224),
    _RcftRSlotLANOPortModuleType_Type()
)
rcftRSlotLANOPortModuleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRSlotLANOPortModuleType.setStatus("current")
_RcftRSlotConfigFlag_Type = Integer32
_RcftRSlotConfigFlag_Object = MibTableColumn
rcftRSlotConfigFlag = _RcftRSlotConfigFlag_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 225),
    _RcftRSlotConfigFlag_Type()
)
rcftRSlotConfigFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftRSlotConfigFlag.setStatus("current")
_RcftSlotOpticalDeviceStatus_Type = Integer32
_RcftSlotOpticalDeviceStatus_Object = MibTableColumn
rcftSlotOpticalDeviceStatus = _RcftSlotOpticalDeviceStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 226),
    _RcftSlotOpticalDeviceStatus_Type()
)
rcftSlotOpticalDeviceStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftSlotOpticalDeviceStatus.setStatus("current")
_RcftSlotPrimaryAdjustFactor_Type = Integer32
_RcftSlotPrimaryAdjustFactor_Object = MibTableColumn
rcftSlotPrimaryAdjustFactor = _RcftSlotPrimaryAdjustFactor_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 227),
    _RcftSlotPrimaryAdjustFactor_Type()
)
rcftSlotPrimaryAdjustFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftSlotPrimaryAdjustFactor.setStatus("current")


class _RcftSlotPrimaryOpticalRate_Type(OctetString):
    """Custom type rcftSlotPrimaryOpticalRate based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_RcftSlotPrimaryOpticalRate_Type.__name__ = "OctetString"
_RcftSlotPrimaryOpticalRate_Object = MibTableColumn
rcftSlotPrimaryOpticalRate = _RcftSlotPrimaryOpticalRate_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 228),
    _RcftSlotPrimaryOpticalRate_Type()
)
rcftSlotPrimaryOpticalRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftSlotPrimaryOpticalRate.setStatus("current")


class _RcftSlotPrimaryTrapThreshold_Type(OctetString):
    """Custom type rcftSlotPrimaryTrapThreshold based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_RcftSlotPrimaryTrapThreshold_Type.__name__ = "OctetString"
_RcftSlotPrimaryTrapThreshold_Object = MibTableColumn
rcftSlotPrimaryTrapThreshold = _RcftSlotPrimaryTrapThreshold_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 229),
    _RcftSlotPrimaryTrapThreshold_Type()
)
rcftSlotPrimaryTrapThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftSlotPrimaryTrapThreshold.setStatus("current")
_RcftSlotSecondaryAdjustFactor_Type = Integer32
_RcftSlotSecondaryAdjustFactor_Object = MibTableColumn
rcftSlotSecondaryAdjustFactor = _RcftSlotSecondaryAdjustFactor_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 230),
    _RcftSlotSecondaryAdjustFactor_Type()
)
rcftSlotSecondaryAdjustFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftSlotSecondaryAdjustFactor.setStatus("current")


class _RcftSlotSecondaryOpticalRate_Type(OctetString):
    """Custom type rcftSlotSecondaryOpticalRate based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_RcftSlotSecondaryOpticalRate_Type.__name__ = "OctetString"
_RcftSlotSecondaryOpticalRate_Object = MibTableColumn
rcftSlotSecondaryOpticalRate = _RcftSlotSecondaryOpticalRate_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 231),
    _RcftSlotSecondaryOpticalRate_Type()
)
rcftSlotSecondaryOpticalRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftSlotSecondaryOpticalRate.setStatus("current")


class _RcftSlotSecondaryTrapThreshold_Type(OctetString):
    """Custom type rcftSlotSecondaryTrapThreshold based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_RcftSlotSecondaryTrapThreshold_Type.__name__ = "OctetString"
_RcftSlotSecondaryTrapThreshold_Object = MibTableColumn
rcftSlotSecondaryTrapThreshold = _RcftSlotSecondaryTrapThreshold_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 232),
    _RcftSlotSecondaryTrapThreshold_Type()
)
rcftSlotSecondaryTrapThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftSlotSecondaryTrapThreshold.setStatus("current")
_RcftSlotWANSendErrFluxPacket_Type = Integer32
_RcftSlotWANSendErrFluxPacket_Object = MibTableColumn
rcftSlotWANSendErrFluxPacket = _RcftSlotWANSendErrFluxPacket_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 233),
    _RcftSlotWANSendErrFluxPacket_Type()
)
rcftSlotWANSendErrFluxPacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftSlotWANSendErrFluxPacket.setStatus("current")
_RcftRSlotWANSendErrFluxPacket_Type = Integer32
_RcftRSlotWANSendErrFluxPacket_Object = MibTableColumn
rcftRSlotWANSendErrFluxPacket = _RcftRSlotWANSendErrFluxPacket_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 234),
    _RcftRSlotWANSendErrFluxPacket_Type()
)
rcftRSlotWANSendErrFluxPacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRSlotWANSendErrFluxPacket.setStatus("current")


class _RcftSlotOpticalDeviceType_Type(Integer32):
    """Custom type rcftSlotOpticalDeviceType based on Integer32"""
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
        *(("splitter-50-50", 1),
          ("wdm-1310nm-1550nm", 2),
          ("fwdm-1550nm", 3),
          ("cwdm-1490nm", 4))
    )


_RcftSlotOpticalDeviceType_Type.__name__ = "Integer32"
_RcftSlotOpticalDeviceType_Object = MibTableColumn
rcftSlotOpticalDeviceType = _RcftSlotOpticalDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 235),
    _RcftSlotOpticalDeviceType_Type()
)
rcftSlotOpticalDeviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftSlotOpticalDeviceType.setStatus("current")


class _RcftRSlotCardOrderInfor_Type(OctetString):
    """Custom type rcftRSlotCardOrderInfor based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_RcftRSlotCardOrderInfor_Type.__name__ = "OctetString"
_RcftRSlotCardOrderInfor_Object = MibTableColumn
rcftRSlotCardOrderInfor = _RcftRSlotCardOrderInfor_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 236),
    _RcftRSlotCardOrderInfor_Type()
)
rcftRSlotCardOrderInfor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRSlotCardOrderInfor.setStatus("current")


class _RcftRSlotTimeSlots_Type(OctetString):
    """Custom type rcftRSlotTimeSlots based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 16),
    )


_RcftRSlotTimeSlots_Type.__name__ = "OctetString"
_RcftRSlotTimeSlots_Object = MibTableColumn
rcftRSlotTimeSlots = _RcftRSlotTimeSlots_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 237),
    _RcftRSlotTimeSlots_Type()
)
rcftRSlotTimeSlots.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftRSlotTimeSlots.setStatus("current")


class _RcftRSlotServiceConnectMode_Type(Integer32):
    """Custom type rcftRSlotServiceConnectMode based on Integer32"""
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
        *(("mode1", 1),
          ("mode2", 2),
          ("mode3", 3),
          ("reserve", 4))
    )


_RcftRSlotServiceConnectMode_Type.__name__ = "Integer32"
_RcftRSlotServiceConnectMode_Object = MibTableColumn
rcftRSlotServiceConnectMode = _RcftRSlotServiceConnectMode_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 238),
    _RcftRSlotServiceConnectMode_Type()
)
rcftRSlotServiceConnectMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftRSlotServiceConnectMode.setStatus("current")
_RcftSlotSendErrFluxPacket_Type = Integer32
_RcftSlotSendErrFluxPacket_Object = MibTableColumn
rcftSlotSendErrFluxPacket = _RcftSlotSendErrFluxPacket_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 239),
    _RcftSlotSendErrFluxPacket_Type()
)
rcftSlotSendErrFluxPacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftSlotSendErrFluxPacket.setStatus("current")
_RcftRSlotSendErrFluxPacket_Type = Integer32
_RcftRSlotSendErrFluxPacket_Object = MibTableColumn
rcftRSlotSendErrFluxPacket = _RcftRSlotSendErrFluxPacket_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 240),
    _RcftRSlotSendErrFluxPacket_Type()
)
rcftRSlotSendErrFluxPacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRSlotSendErrFluxPacket.setStatus("current")
_CwdmSecondaryCWDMModuleMaxSpeed_Type = Integer32
_CwdmSecondaryCWDMModuleMaxSpeed_Object = MibTableColumn
cwdmSecondaryCWDMModuleMaxSpeed = _CwdmSecondaryCWDMModuleMaxSpeed_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 241),
    _CwdmSecondaryCWDMModuleMaxSpeed_Type()
)
cwdmSecondaryCWDMModuleMaxSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwdmSecondaryCWDMModuleMaxSpeed.setStatus("current")
_CwdmSecondaryCWDMModuleTransLen_Type = Integer32
_CwdmSecondaryCWDMModuleTransLen_Object = MibTableColumn
cwdmSecondaryCWDMModuleTransLen = _CwdmSecondaryCWDMModuleTransLen_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 242),
    _CwdmSecondaryCWDMModuleTransLen_Type()
)
cwdmSecondaryCWDMModuleTransLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwdmSecondaryCWDMModuleTransLen.setStatus("current")
_CwdmSecondaryCWDMModuleWaveLen_Type = Integer32
_CwdmSecondaryCWDMModuleWaveLen_Object = MibTableColumn
cwdmSecondaryCWDMModuleWaveLen = _CwdmSecondaryCWDMModuleWaveLen_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 243),
    _CwdmSecondaryCWDMModuleWaveLen_Type()
)
cwdmSecondaryCWDMModuleWaveLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwdmSecondaryCWDMModuleWaveLen.setStatus("current")


class _CwdmSecondaryCWDMModuleManufacturer_Type(OctetString):
    """Custom type cwdmSecondaryCWDMModuleManufacturer based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_CwdmSecondaryCWDMModuleManufacturer_Type.__name__ = "OctetString"
_CwdmSecondaryCWDMModuleManufacturer_Object = MibTableColumn
cwdmSecondaryCWDMModuleManufacturer = _CwdmSecondaryCWDMModuleManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 244),
    _CwdmSecondaryCWDMModuleManufacturer_Type()
)
cwdmSecondaryCWDMModuleManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwdmSecondaryCWDMModuleManufacturer.setStatus("current")


class _CwdmSecondaryCWDMModuleDescr_Type(OctetString):
    """Custom type cwdmSecondaryCWDMModuleDescr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_CwdmSecondaryCWDMModuleDescr_Type.__name__ = "OctetString"
_CwdmSecondaryCWDMModuleDescr_Object = MibTableColumn
cwdmSecondaryCWDMModuleDescr = _CwdmSecondaryCWDMModuleDescr_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 245),
    _CwdmSecondaryCWDMModuleDescr_Type()
)
cwdmSecondaryCWDMModuleDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwdmSecondaryCWDMModuleDescr.setStatus("current")


class _CwdmSecondaryCWDMModuleVersion_Type(OctetString):
    """Custom type cwdmSecondaryCWDMModuleVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_CwdmSecondaryCWDMModuleVersion_Type.__name__ = "OctetString"
_CwdmSecondaryCWDMModuleVersion_Object = MibTableColumn
cwdmSecondaryCWDMModuleVersion = _CwdmSecondaryCWDMModuleVersion_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 246),
    _CwdmSecondaryCWDMModuleVersion_Type()
)
cwdmSecondaryCWDMModuleVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwdmSecondaryCWDMModuleVersion.setStatus("current")


class _CwdmSecondaryCWDMModuleSerialNumber_Type(OctetString):
    """Custom type cwdmSecondaryCWDMModuleSerialNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_CwdmSecondaryCWDMModuleSerialNumber_Type.__name__ = "OctetString"
_CwdmSecondaryCWDMModuleSerialNumber_Object = MibTableColumn
cwdmSecondaryCWDMModuleSerialNumber = _CwdmSecondaryCWDMModuleSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 247),
    _CwdmSecondaryCWDMModuleSerialNumber_Type()
)
cwdmSecondaryCWDMModuleSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwdmSecondaryCWDMModuleSerialNumber.setStatus("current")


class _RcftSlotVLANTagDirection_Type(Integer32):
    """Custom type rcftSlotVLANTagDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fxtotx", 1),
          ("txtofx", 2))
    )


_RcftSlotVLANTagDirection_Type.__name__ = "Integer32"
_RcftSlotVLANTagDirection_Object = MibTableColumn
rcftSlotVLANTagDirection = _RcftSlotVLANTagDirection_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 248),
    _RcftSlotVLANTagDirection_Type()
)
rcftSlotVLANTagDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftSlotVLANTagDirection.setStatus("current")


class _RcftRSlotVLANTagDirection_Type(Integer32):
    """Custom type rcftRSlotVLANTagDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fxtotx", 1),
          ("txtofx", 2))
    )


_RcftRSlotVLANTagDirection_Type.__name__ = "Integer32"
_RcftRSlotVLANTagDirection_Object = MibTableColumn
rcftRSlotVLANTagDirection = _RcftRSlotVLANTagDirection_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 249),
    _RcftRSlotVLANTagDirection_Type()
)
rcftRSlotVLANTagDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftRSlotVLANTagDirection.setStatus("current")


class _RcftSlotVLANTagModule_Type(Integer32):
    """Custom type rcftSlotVLANTagModule based on Integer32"""
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
        *(("notag", 1),
          ("onetag", 2),
          ("twotag", 3),
          ("reserve", 4))
    )


_RcftSlotVLANTagModule_Type.__name__ = "Integer32"
_RcftSlotVLANTagModule_Object = MibTableColumn
rcftSlotVLANTagModule = _RcftSlotVLANTagModule_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 250),
    _RcftSlotVLANTagModule_Type()
)
rcftSlotVLANTagModule.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftSlotVLANTagModule.setStatus("current")


class _RcftRSlotVLANTagModule_Type(Integer32):
    """Custom type rcftRSlotVLANTagModule based on Integer32"""
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
        *(("notag", 1),
          ("onetag", 2),
          ("twotag", 3),
          ("reserve", 4))
    )


_RcftRSlotVLANTagModule_Type.__name__ = "Integer32"
_RcftRSlotVLANTagModule_Object = MibTableColumn
rcftRSlotVLANTagModule = _RcftRSlotVLANTagModule_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 251),
    _RcftRSlotVLANTagModule_Type()
)
rcftRSlotVLANTagModule.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftRSlotVLANTagModule.setStatus("current")
_RcftSlotVLANID_Type = Integer32
_RcftSlotVLANID_Object = MibTableColumn
rcftSlotVLANID = _RcftSlotVLANID_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 252),
    _RcftSlotVLANID_Type()
)
rcftSlotVLANID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftSlotVLANID.setStatus("current")
_RcftRSlotVLANID_Type = Integer32
_RcftRSlotVLANID_Object = MibTableColumn
rcftRSlotVLANID = _RcftRSlotVLANID_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 253),
    _RcftRSlotVLANID_Type()
)
rcftRSlotVLANID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftRSlotVLANID.setStatus("current")
_RcftSlotISPTPID_Type = Integer32
_RcftSlotISPTPID_Object = MibTableColumn
rcftSlotISPTPID = _RcftSlotISPTPID_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 254),
    _RcftSlotISPTPID_Type()
)
rcftSlotISPTPID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftSlotISPTPID.setStatus("current")
_RcftRSlotISPTPID_Type = Integer32
_RcftRSlotISPTPID_Object = MibTableColumn
rcftRSlotISPTPID = _RcftRSlotISPTPID_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 255),
    _RcftRSlotISPTPID_Type()
)
rcftRSlotISPTPID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftRSlotISPTPID.setStatus("current")
_RcftSlotE1SubCardType_Type = Integer32
_RcftSlotE1SubCardType_Object = MibTableColumn
rcftSlotE1SubCardType = _RcftSlotE1SubCardType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 256),
    _RcftSlotE1SubCardType_Type()
)
rcftSlotE1SubCardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftSlotE1SubCardType.setStatus("current")


class _RcftSlotMultiE1LoopOrder_Type(OctetString):
    """Custom type rcftSlotMultiE1LoopOrder based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_RcftSlotMultiE1LoopOrder_Type.__name__ = "OctetString"
_RcftSlotMultiE1LoopOrder_Object = MibTableColumn
rcftSlotMultiE1LoopOrder = _RcftSlotMultiE1LoopOrder_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 257),
    _RcftSlotMultiE1LoopOrder_Type()
)
rcftSlotMultiE1LoopOrder.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftSlotMultiE1LoopOrder.setStatus("current")
_RcftSlotSubModuleExist_Type = Integer32
_RcftSlotSubModuleExist_Object = MibTableColumn
rcftSlotSubModuleExist = _RcftSlotSubModuleExist_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 258),
    _RcftSlotSubModuleExist_Type()
)
rcftSlotSubModuleExist.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftSlotSubModuleExist.setStatus("current")
_RcftSlotOrderTimeParameter_Type = Integer32
_RcftSlotOrderTimeParameter_Object = MibTableColumn
rcftSlotOrderTimeParameter = _RcftSlotOrderTimeParameter_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 259),
    _RcftSlotOrderTimeParameter_Type()
)
rcftSlotOrderTimeParameter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftSlotOrderTimeParameter.setStatus("current")
_RcftSlotRLPStatus_Type = Integer32
_RcftSlotRLPStatus_Object = MibTableColumn
rcftSlotRLPStatus = _RcftSlotRLPStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 260),
    _RcftSlotRLPStatus_Type()
)
rcftSlotRLPStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftSlotRLPStatus.setStatus("current")
_RcftSlotSFPDiagnosticsInfo_Type = Integer32
_RcftSlotSFPDiagnosticsInfo_Object = MibTableColumn
rcftSlotSFPDiagnosticsInfo = _RcftSlotSFPDiagnosticsInfo_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 261),
    _RcftSlotSFPDiagnosticsInfo_Type()
)
rcftSlotSFPDiagnosticsInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftSlotSFPDiagnosticsInfo.setStatus("current")
_RcftRSlotSFPDiagnosticsInfo_Type = Integer32
_RcftRSlotSFPDiagnosticsInfo_Object = MibTableColumn
rcftRSlotSFPDiagnosticsInfo = _RcftRSlotSFPDiagnosticsInfo_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 262),
    _RcftRSlotSFPDiagnosticsInfo_Type()
)
rcftRSlotSFPDiagnosticsInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRSlotSFPDiagnosticsInfo.setStatus("current")
_RcftSlotTemp_Type = Integer32
_RcftSlotTemp_Object = MibTableColumn
rcftSlotTemp = _RcftSlotTemp_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 263),
    _RcftSlotTemp_Type()
)
rcftSlotTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftSlotTemp.setStatus("current")
_RcftSlotLALStatus_Type = Integer32
_RcftSlotLALStatus_Object = MibTableColumn
rcftSlotLALStatus = _RcftSlotLALStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 264),
    _RcftSlotLALStatus_Type()
)
rcftSlotLALStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftSlotLALStatus.setStatus("current")
_RcftSlotRALStatus_Type = Integer32
_RcftSlotRALStatus_Object = MibTableColumn
rcftSlotRALStatus = _RcftSlotRALStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 265),
    _RcftSlotRALStatus_Type()
)
rcftSlotRALStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftSlotRALStatus.setStatus("current")


class _RcftSlotCardInformation_Type(OctetString):
    """Custom type rcftSlotCardInformation based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_RcftSlotCardInformation_Type.__name__ = "OctetString"
_RcftSlotCardInformation_Object = MibTableColumn
rcftSlotCardInformation = _RcftSlotCardInformation_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 266),
    _RcftSlotCardInformation_Type()
)
rcftSlotCardInformation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftSlotCardInformation.setStatus("current")
_RcftSlotVoltage_Type = Integer32
_RcftSlotVoltage_Object = MibTableColumn
rcftSlotVoltage = _RcftSlotVoltage_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 267),
    _RcftSlotVoltage_Type()
)
rcftSlotVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftSlotVoltage.setStatus("current")
_RcftSlotVoltageHighLimit_Type = Integer32
_RcftSlotVoltageHighLimit_Object = MibTableColumn
rcftSlotVoltageHighLimit = _RcftSlotVoltageHighLimit_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 268),
    _RcftSlotVoltageHighLimit_Type()
)
rcftSlotVoltageHighLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftSlotVoltageHighLimit.setStatus("current")
_RcftSlotVoltageLowLimit_Type = Integer32
_RcftSlotVoltageLowLimit_Object = MibTableColumn
rcftSlotVoltageLowLimit = _RcftSlotVoltageLowLimit_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 269),
    _RcftSlotVoltageLowLimit_Type()
)
rcftSlotVoltageLowLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftSlotVoltageLowLimit.setStatus("current")
_RcftSlotTempHighLimit_Type = Integer32
_RcftSlotTempHighLimit_Object = MibTableColumn
rcftSlotTempHighLimit = _RcftSlotTempHighLimit_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 270),
    _RcftSlotTempHighLimit_Type()
)
rcftSlotTempHighLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftSlotTempHighLimit.setStatus("current")
_RcftSlotTempLowLimit_Type = Integer32
_RcftSlotTempLowLimit_Object = MibTableColumn
rcftSlotTempLowLimit = _RcftSlotTempLowLimit_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 271),
    _RcftSlotTempLowLimit_Type()
)
rcftSlotTempLowLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftSlotTempLowLimit.setStatus("current")
_RcftSlotHumidity_Type = Integer32
_RcftSlotHumidity_Object = MibTableColumn
rcftSlotHumidity = _RcftSlotHumidity_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 272),
    _RcftSlotHumidity_Type()
)
rcftSlotHumidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftSlotHumidity.setStatus("current")
_RcftSlotHumidityHighLimit_Type = Integer32
_RcftSlotHumidityHighLimit_Object = MibTableColumn
rcftSlotHumidityHighLimit = _RcftSlotHumidityHighLimit_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 273),
    _RcftSlotHumidityHighLimit_Type()
)
rcftSlotHumidityHighLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftSlotHumidityHighLimit.setStatus("current")
_RcftSlotHumidityLowLimit_Type = Integer32
_RcftSlotHumidityLowLimit_Object = MibTableColumn
rcftSlotHumidityLowLimit = _RcftSlotHumidityLowLimit_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 274),
    _RcftSlotHumidityLowLimit_Type()
)
rcftSlotHumidityLowLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftSlotHumidityLowLimit.setStatus("current")


class _RcftSlotMultiE1AlarmRejectOrder_Type(OctetString):
    """Custom type rcftSlotMultiE1AlarmRejectOrder based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_RcftSlotMultiE1AlarmRejectOrder_Type.__name__ = "OctetString"
_RcftSlotMultiE1AlarmRejectOrder_Object = MibTableColumn
rcftSlotMultiE1AlarmRejectOrder = _RcftSlotMultiE1AlarmRejectOrder_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 275),
    _RcftSlotMultiE1AlarmRejectOrder_Type()
)
rcftSlotMultiE1AlarmRejectOrder.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftSlotMultiE1AlarmRejectOrder.setStatus("current")
_RcftT1PortPulseWaveForm_Type = Integer32
_RcftT1PortPulseWaveForm_Object = MibTableColumn
rcftT1PortPulseWaveForm = _RcftT1PortPulseWaveForm_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 276),
    _RcftT1PortPulseWaveForm_Type()
)
rcftT1PortPulseWaveForm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftT1PortPulseWaveForm.setStatus("current")
_RcftT1PortCodeType_Type = Integer32
_RcftT1PortCodeType_Object = MibTableColumn
rcftT1PortCodeType = _RcftT1PortCodeType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 277),
    _RcftT1PortCodeType_Type()
)
rcftT1PortCodeType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftT1PortCodeType.setStatus("current")
_RcftSlotSDRAM_Type = Integer32
_RcftSlotSDRAM_Object = MibTableColumn
rcftSlotSDRAM = _RcftSlotSDRAM_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 278),
    _RcftSlotSDRAM_Type()
)
rcftSlotSDRAM.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftSlotSDRAM.setStatus("current")
_RcftSlotSabitMode_Type = Integer32
_RcftSlotSabitMode_Object = MibTableColumn
rcftSlotSabitMode = _RcftSlotSabitMode_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 279),
    _RcftSlotSabitMode_Type()
)
rcftSlotSabitMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftSlotSabitMode.setStatus("current")


class _RcftSlotApsWaitToRestore_Type(Integer32):
    """Custom type rcftSlotApsWaitToRestore based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RcftSlotApsWaitToRestore_Type.__name__ = "Integer32"
_RcftSlotApsWaitToRestore_Object = MibTableColumn
rcftSlotApsWaitToRestore = _RcftSlotApsWaitToRestore_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 280),
    _RcftSlotApsWaitToRestore_Type()
)
rcftSlotApsWaitToRestore.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftSlotApsWaitToRestore.setStatus("current")
_RcftSlotCLKChannel_Type = Integer32
_RcftSlotCLKChannel_Object = MibTableColumn
rcftSlotCLKChannel = _RcftSlotCLKChannel_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 281),
    _RcftSlotCLKChannel_Type()
)
rcftSlotCLKChannel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftSlotCLKChannel.setStatus("current")
_RcftSlotRmcChannelType_Type = Integer32
_RcftSlotRmcChannelType_Object = MibTableColumn
rcftSlotRmcChannelType = _RcftSlotRmcChannelType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 282),
    _RcftSlotRmcChannelType_Type()
)
rcftSlotRmcChannelType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftSlotRmcChannelType.setStatus("current")
_RcftSlotApsE3SwitchDelay_Type = Integer32
_RcftSlotApsE3SwitchDelay_Object = MibTableColumn
rcftSlotApsE3SwitchDelay = _RcftSlotApsE3SwitchDelay_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 283),
    _RcftSlotApsE3SwitchDelay_Type()
)
rcftSlotApsE3SwitchDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftSlotApsE3SwitchDelay.setStatus("current")
_RcftSlotApsE6SwitchDelay_Type = Integer32
_RcftSlotApsE6SwitchDelay_Object = MibTableColumn
rcftSlotApsE6SwitchDelay = _RcftSlotApsE6SwitchDelay_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 284),
    _RcftSlotApsE6SwitchDelay_Type()
)
rcftSlotApsE6SwitchDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftSlotApsE6SwitchDelay.setStatus("current")
_RcftE1DS1PortType_Type = Integer32
_RcftE1DS1PortType_Object = MibTableColumn
rcftE1DS1PortType = _RcftE1DS1PortType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 285),
    _RcftE1DS1PortType_Type()
)
rcftE1DS1PortType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftE1DS1PortType.setStatus("current")
_RcftSlotManageID_Type = Integer32
_RcftSlotManageID_Object = MibTableColumn
rcftSlotManageID = _RcftSlotManageID_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 286),
    _RcftSlotManageID_Type()
)
rcftSlotManageID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftSlotManageID.setStatus("current")
_RcftSlotE1PortNumber_Type = Integer32
_RcftSlotE1PortNumber_Object = MibTableColumn
rcftSlotE1PortNumber = _RcftSlotE1PortNumber_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 287),
    _RcftSlotE1PortNumber_Type()
)
rcftSlotE1PortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftSlotE1PortNumber.setStatus("current")
_RcftSlotQoS_Type = Integer32
_RcftSlotQoS_Object = MibTableColumn
rcftSlotQoS = _RcftSlotQoS_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 288),
    _RcftSlotQoS_Type()
)
rcftSlotQoS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftSlotQoS.setStatus("current")
_RcftSlotTPIDRemark_Type = Integer32
_RcftSlotTPIDRemark_Object = MibTableColumn
rcftSlotTPIDRemark = _RcftSlotTPIDRemark_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 289),
    _RcftSlotTPIDRemark_Type()
)
rcftSlotTPIDRemark.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftSlotTPIDRemark.setStatus("current")
_RcftRSlotTPIDRemark_Type = Integer32
_RcftRSlotTPIDRemark_Object = MibTableColumn
rcftRSlotTPIDRemark = _RcftRSlotTPIDRemark_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 290),
    _RcftRSlotTPIDRemark_Type()
)
rcftRSlotTPIDRemark.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftRSlotTPIDRemark.setStatus("current")


class _RcftSlotDeviceMibUse_Type(Integer32):
    """Custom type rcftSlotDeviceMibUse based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mib002", 1),
          ("rccomlib", 2))
    )


_RcftSlotDeviceMibUse_Type.__name__ = "Integer32"
_RcftSlotDeviceMibUse_Object = MibTableColumn
rcftSlotDeviceMibUse = _RcftSlotDeviceMibUse_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 291),
    _RcftSlotDeviceMibUse_Type()
)
rcftSlotDeviceMibUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftSlotDeviceMibUse.setStatus("current")


class _RcftSlotApsSwitchDelay_Type(Integer32):
    """Custom type rcftSlotApsSwitchDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RcftSlotApsSwitchDelay_Type.__name__ = "Integer32"
_RcftSlotApsSwitchDelay_Object = MibTableColumn
rcftSlotApsSwitchDelay = _RcftSlotApsSwitchDelay_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 1, 1, 292),
    _RcftSlotApsSwitchDelay_Type()
)
rcftSlotApsSwitchDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftSlotApsSwitchDelay.setStatus("current")
_RcftInterfaceStatTable_Object = MibTable
rcftInterfaceStatTable = _RcftInterfaceStatTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 2)
)
if mibBuilder.loadTexts:
    rcftInterfaceStatTable.setStatus("current")
_RcftInterfaceStatEntry_Object = MibTableRow
rcftInterfaceStatEntry = _RcftInterfaceStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 2, 1)
)
rcftInterfaceStatEntry.setIndexNames(
    (0, "RAISECOM-RCFT-MIB", "rcftChassisIndex"),
    (0, "RAISECOM-RCFT-MIB", "rcftSlotIndex"),
    (0, "RAISECOM-RCFT-MIB", "rcftInterfaceType"),
    (0, "RAISECOM-RCFT-MIB", "rcftInterfaceIndex"),
)
if mibBuilder.loadTexts:
    rcftInterfaceStatEntry.setStatus("current")


class _RcftInterfaceType_Type(Integer32):
    """Custom type rcftInterfaceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ethport", 1),
          ("audioChannel", 2),
          ("e1port", 3))
    )


_RcftInterfaceType_Type.__name__ = "Integer32"
_RcftInterfaceType_Object = MibTableColumn
rcftInterfaceType = _RcftInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 2, 1, 1),
    _RcftInterfaceType_Type()
)
rcftInterfaceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftInterfaceType.setStatus("current")


class _RcftInterfaceIndex_Type(Integer32):
    """Custom type rcftInterfaceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_RcftInterfaceIndex_Type.__name__ = "Integer32"
_RcftInterfaceIndex_Object = MibTableColumn
rcftInterfaceIndex = _RcftInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 2, 1, 2),
    _RcftInterfaceIndex_Type()
)
rcftInterfaceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftInterfaceIndex.setStatus("current")


class _RcftInterfaceRLink_Type(Integer32):
    """Custom type rcftInterfaceRLink based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("link-up", 1),
          ("link-down", 2))
    )


_RcftInterfaceRLink_Type.__name__ = "Integer32"
_RcftInterfaceRLink_Object = MibTableColumn
rcftInterfaceRLink = _RcftInterfaceRLink_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 2, 1, 3),
    _RcftInterfaceRLink_Type()
)
rcftInterfaceRLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftInterfaceRLink.setStatus("current")


class _RcftInterfaceRAutoNegotiation_Type(Integer32):
    """Custom type rcftInterfaceRAutoNegotiation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("manul", 2))
    )


_RcftInterfaceRAutoNegotiation_Type.__name__ = "Integer32"
_RcftInterfaceRAutoNegotiation_Object = MibTableColumn
rcftInterfaceRAutoNegotiation = _RcftInterfaceRAutoNegotiation_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 2, 1, 4),
    _RcftInterfaceRAutoNegotiation_Type()
)
rcftInterfaceRAutoNegotiation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftInterfaceRAutoNegotiation.setStatus("current")


class _RcftInterfaceRDuplex_Type(Integer32):
    """Custom type rcftInterfaceRDuplex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("full-duplex", 1),
          ("half-duplex", 2),
          ("auto", 3))
    )


_RcftInterfaceRDuplex_Type.__name__ = "Integer32"
_RcftInterfaceRDuplex_Object = MibTableColumn
rcftInterfaceRDuplex = _RcftInterfaceRDuplex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 2, 1, 5),
    _RcftInterfaceRDuplex_Type()
)
rcftInterfaceRDuplex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftInterfaceRDuplex.setStatus("current")


class _RcftInterfaceRSpeed_Type(Integer32):
    """Custom type rcftInterfaceRSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              16)
        )
    )
    namedValues = NamedValues(
        *(("rcft10Mbps", 1),
          ("rcft100Mbps", 2),
          ("rcft1000Mbps", 3),
          ("rcft10Gbps", 4),
          ("other", 16))
    )


_RcftInterfaceRSpeed_Type.__name__ = "Integer32"
_RcftInterfaceRSpeed_Object = MibTableColumn
rcftInterfaceRSpeed = _RcftInterfaceRSpeed_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 2, 1, 6),
    _RcftInterfaceRSpeed_Type()
)
rcftInterfaceRSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftInterfaceRSpeed.setStatus("current")


class _RcftInterfaceRStat_Type(Integer32):
    """Custom type rcftInterfaceRStat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("open", 1),
          ("close", 2))
    )


_RcftInterfaceRStat_Type.__name__ = "Integer32"
_RcftInterfaceRStat_Object = MibTableColumn
rcftInterfaceRStat = _RcftInterfaceRStat_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 2, 1, 7),
    _RcftInterfaceRStat_Type()
)
rcftInterfaceRStat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftInterfaceRStat.setStatus("current")


class _RcftInterfaceLOS_Type(Integer32):
    """Custom type rcftInterfaceLOS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("alarm", 2))
    )


_RcftInterfaceLOS_Type.__name__ = "Integer32"
_RcftInterfaceLOS_Object = MibTableColumn
rcftInterfaceLOS = _RcftInterfaceLOS_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 2, 1, 8),
    _RcftInterfaceLOS_Type()
)
rcftInterfaceLOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftInterfaceLOS.setStatus("current")


class _RcftInterfaceCV_Type(Integer32):
    """Custom type rcftInterfaceCV based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("alarm", 2))
    )


_RcftInterfaceCV_Type.__name__ = "Integer32"
_RcftInterfaceCV_Object = MibTableColumn
rcftInterfaceCV = _RcftInterfaceCV_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 2, 1, 9),
    _RcftInterfaceCV_Type()
)
rcftInterfaceCV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftInterfaceCV.setStatus("current")


class _RcftInterfaceAIS_Type(Integer32):
    """Custom type rcftInterfaceAIS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("alarm", 2))
    )


_RcftInterfaceAIS_Type.__name__ = "Integer32"
_RcftInterfaceAIS_Object = MibTableColumn
rcftInterfaceAIS = _RcftInterfaceAIS_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 2, 1, 10),
    _RcftInterfaceAIS_Type()
)
rcftInterfaceAIS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftInterfaceAIS.setStatus("current")


class _RcftInterfaceLOF_Type(Integer32):
    """Custom type rcftInterfaceLOF based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("alarm", 2))
    )


_RcftInterfaceLOF_Type.__name__ = "Integer32"
_RcftInterfaceLOF_Object = MibTableColumn
rcftInterfaceLOF = _RcftInterfaceLOF_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 2, 1, 11),
    _RcftInterfaceLOF_Type()
)
rcftInterfaceLOF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftInterfaceLOF.setStatus("current")


class _RcftInterfaceCRC_Type(Integer32):
    """Custom type rcftInterfaceCRC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("alarm", 2))
    )


_RcftInterfaceCRC_Type.__name__ = "Integer32"
_RcftInterfaceCRC_Object = MibTableColumn
rcftInterfaceCRC = _RcftInterfaceCRC_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 2, 1, 12),
    _RcftInterfaceCRC_Type()
)
rcftInterfaceCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftInterfaceCRC.setStatus("current")


class _RcftInterfaceE5_Type(Integer32):
    """Custom type rcftInterfaceE5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("alarm", 2))
    )


_RcftInterfaceE5_Type.__name__ = "Integer32"
_RcftInterfaceE5_Object = MibTableColumn
rcftInterfaceE5 = _RcftInterfaceE5_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 2, 1, 13),
    _RcftInterfaceE5_Type()
)
rcftInterfaceE5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftInterfaceE5.setStatus("current")


class _RcftInterfaceRLOS_Type(Integer32):
    """Custom type rcftInterfaceRLOS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("alarm", 2))
    )


_RcftInterfaceRLOS_Type.__name__ = "Integer32"
_RcftInterfaceRLOS_Object = MibTableColumn
rcftInterfaceRLOS = _RcftInterfaceRLOS_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 2, 1, 14),
    _RcftInterfaceRLOS_Type()
)
rcftInterfaceRLOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftInterfaceRLOS.setStatus("current")


class _RcftInterfaceRCV_Type(Integer32):
    """Custom type rcftInterfaceRCV based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("alarm", 2))
    )


_RcftInterfaceRCV_Type.__name__ = "Integer32"
_RcftInterfaceRCV_Object = MibTableColumn
rcftInterfaceRCV = _RcftInterfaceRCV_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 2, 1, 15),
    _RcftInterfaceRCV_Type()
)
rcftInterfaceRCV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftInterfaceRCV.setStatus("current")


class _RcftInterfaceRAIS_Type(Integer32):
    """Custom type rcftInterfaceRAIS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("alarm", 2))
    )


_RcftInterfaceRAIS_Type.__name__ = "Integer32"
_RcftInterfaceRAIS_Object = MibTableColumn
rcftInterfaceRAIS = _RcftInterfaceRAIS_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 2, 1, 16),
    _RcftInterfaceRAIS_Type()
)
rcftInterfaceRAIS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftInterfaceRAIS.setStatus("current")


class _RcftInterfaceRLOF_Type(Integer32):
    """Custom type rcftInterfaceRLOF based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("alarm", 2))
    )


_RcftInterfaceRLOF_Type.__name__ = "Integer32"
_RcftInterfaceRLOF_Object = MibTableColumn
rcftInterfaceRLOF = _RcftInterfaceRLOF_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 2, 1, 17),
    _RcftInterfaceRLOF_Type()
)
rcftInterfaceRLOF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftInterfaceRLOF.setStatus("current")


class _RcftInterfaceRCRC_Type(Integer32):
    """Custom type rcftInterfaceRCRC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("alarm", 2))
    )


_RcftInterfaceRCRC_Type.__name__ = "Integer32"
_RcftInterfaceRCRC_Object = MibTableColumn
rcftInterfaceRCRC = _RcftInterfaceRCRC_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 2, 1, 18),
    _RcftInterfaceRCRC_Type()
)
rcftInterfaceRCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftInterfaceRCRC.setStatus("current")


class _RcftInterfaceUnUsed_Type(Integer32):
    """Custom type rcftInterfaceUnUsed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unused", 1),
          ("used", 2))
    )


_RcftInterfaceUnUsed_Type.__name__ = "Integer32"
_RcftInterfaceUnUsed_Object = MibTableColumn
rcftInterfaceUnUsed = _RcftInterfaceUnUsed_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 2, 1, 19),
    _RcftInterfaceUnUsed_Type()
)
rcftInterfaceUnUsed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftInterfaceUnUsed.setStatus("current")


class _RcftInterfaceStat_Type(Integer32):
    """Custom type rcftInterfaceStat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("open", 1),
          ("close", 2))
    )


_RcftInterfaceStat_Type.__name__ = "Integer32"
_RcftInterfaceStat_Object = MibTableColumn
rcftInterfaceStat = _RcftInterfaceStat_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 2, 1, 20),
    _RcftInterfaceStat_Type()
)
rcftInterfaceStat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftInterfaceStat.setStatus("current")


class _RcftInterfaceLink_Type(Integer32):
    """Custom type rcftInterfaceLink based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("link", 1),
          ("unlink", 2))
    )


_RcftInterfaceLink_Type.__name__ = "Integer32"
_RcftInterfaceLink_Object = MibTableColumn
rcftInterfaceLink = _RcftInterfaceLink_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 2, 1, 21),
    _RcftInterfaceLink_Type()
)
rcftInterfaceLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftInterfaceLink.setStatus("current")


class _RcftInterfaceAutoNegotiation_Type(Integer32):
    """Custom type rcftInterfaceAutoNegotiation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("manul", 2))
    )


_RcftInterfaceAutoNegotiation_Type.__name__ = "Integer32"
_RcftInterfaceAutoNegotiation_Object = MibTableColumn
rcftInterfaceAutoNegotiation = _RcftInterfaceAutoNegotiation_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 2, 1, 22),
    _RcftInterfaceAutoNegotiation_Type()
)
rcftInterfaceAutoNegotiation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftInterfaceAutoNegotiation.setStatus("current")


class _RcftInterfaceDuplex_Type(Integer32):
    """Custom type rcftInterfaceDuplex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("full-duplex", 1),
          ("half-duplex", 2),
          ("auto", 3))
    )


_RcftInterfaceDuplex_Type.__name__ = "Integer32"
_RcftInterfaceDuplex_Object = MibTableColumn
rcftInterfaceDuplex = _RcftInterfaceDuplex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 2, 1, 23),
    _RcftInterfaceDuplex_Type()
)
rcftInterfaceDuplex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftInterfaceDuplex.setStatus("current")


class _RcftInterfaceSpeed_Type(Integer32):
    """Custom type rcftInterfaceSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              16)
        )
    )
    namedValues = NamedValues(
        *(("rcft10Mbps", 1),
          ("rcft100Mbps", 2),
          ("rcft1000Mbps", 3),
          ("rcft10Gbps", 4),
          ("other", 16))
    )


_RcftInterfaceSpeed_Type.__name__ = "Integer32"
_RcftInterfaceSpeed_Object = MibTableColumn
rcftInterfaceSpeed = _RcftInterfaceSpeed_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 2, 1, 24),
    _RcftInterfaceSpeed_Type()
)
rcftInterfaceSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftInterfaceSpeed.setStatus("current")


class _RcftInterfaceTag_Type(Integer32):
    """Custom type rcftInterfaceTag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("tag", 1),
          ("untag", 2))
    )


_RcftInterfaceTag_Type.__name__ = "Integer32"
_RcftInterfaceTag_Object = MibTableColumn
rcftInterfaceTag = _RcftInterfaceTag_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 2, 1, 25),
    _RcftInterfaceTag_Type()
)
rcftInterfaceTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftInterfaceTag.setStatus("current")
_RcftInterfaceRecvRestrictSpeed_Type = Integer32
_RcftInterfaceRecvRestrictSpeed_Object = MibTableColumn
rcftInterfaceRecvRestrictSpeed = _RcftInterfaceRecvRestrictSpeed_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 2, 1, 26),
    _RcftInterfaceRecvRestrictSpeed_Type()
)
rcftInterfaceRecvRestrictSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftInterfaceRecvRestrictSpeed.setStatus("current")
_RcftInterfaceSendRestrictSpeed_Type = Integer32
_RcftInterfaceSendRestrictSpeed_Object = MibTableColumn
rcftInterfaceSendRestrictSpeed = _RcftInterfaceSendRestrictSpeed_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 2, 1, 27),
    _RcftInterfaceSendRestrictSpeed_Type()
)
rcftInterfaceSendRestrictSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftInterfaceSendRestrictSpeed.setStatus("current")


class _RcftInterfaceRTag_Type(Integer32):
    """Custom type rcftInterfaceRTag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("tag", 1),
          ("untag", 2))
    )


_RcftInterfaceRTag_Type.__name__ = "Integer32"
_RcftInterfaceRTag_Object = MibTableColumn
rcftInterfaceRTag = _RcftInterfaceRTag_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 2, 1, 28),
    _RcftInterfaceRTag_Type()
)
rcftInterfaceRTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftInterfaceRTag.setStatus("current")
_RcftInterfaceRRecvFluxCount_Type = Integer32
_RcftInterfaceRRecvFluxCount_Object = MibTableColumn
rcftInterfaceRRecvFluxCount = _RcftInterfaceRRecvFluxCount_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 2, 1, 29),
    _RcftInterfaceRRecvFluxCount_Type()
)
rcftInterfaceRRecvFluxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftInterfaceRRecvFluxCount.setStatus("current")
_RcftInterfaceRSendFluxCount_Type = Integer32
_RcftInterfaceRSendFluxCount_Object = MibTableColumn
rcftInterfaceRSendFluxCount = _RcftInterfaceRSendFluxCount_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 2, 1, 30),
    _RcftInterfaceRSendFluxCount_Type()
)
rcftInterfaceRSendFluxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftInterfaceRSendFluxCount.setStatus("current")
_RcftInterfaceRRecvFluxTimer_Type = Counter32
_RcftInterfaceRRecvFluxTimer_Object = MibTableColumn
rcftInterfaceRRecvFluxTimer = _RcftInterfaceRRecvFluxTimer_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 2, 1, 31),
    _RcftInterfaceRRecvFluxTimer_Type()
)
rcftInterfaceRRecvFluxTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftInterfaceRRecvFluxTimer.setStatus("current")
_RcftInterfaceRSendFluxTimer_Type = Counter32
_RcftInterfaceRSendFluxTimer_Object = MibTableColumn
rcftInterfaceRSendFluxTimer = _RcftInterfaceRSendFluxTimer_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 2, 1, 32),
    _RcftInterfaceRSendFluxTimer_Type()
)
rcftInterfaceRSendFluxTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftInterfaceRSendFluxTimer.setStatus("current")


class _RcftInterfaceRpriority_Type(Integer32):
    """Custom type rcftInterfaceRpriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("high", 1),
          ("low", 2))
    )


_RcftInterfaceRpriority_Type.__name__ = "Integer32"
_RcftInterfaceRpriority_Object = MibTableColumn
rcftInterfaceRpriority = _RcftInterfaceRpriority_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 2, 1, 33),
    _RcftInterfaceRpriority_Type()
)
rcftInterfaceRpriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftInterfaceRpriority.setStatus("current")


class _RcftInterfaceRMDIXAuto_Type(Integer32):
    """Custom type rcftInterfaceRMDIXAuto based on Integer32"""
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


_RcftInterfaceRMDIXAuto_Type.__name__ = "Integer32"
_RcftInterfaceRMDIXAuto_Object = MibTableColumn
rcftInterfaceRMDIXAuto = _RcftInterfaceRMDIXAuto_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 2, 1, 34),
    _RcftInterfaceRMDIXAuto_Type()
)
rcftInterfaceRMDIXAuto.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftInterfaceRMDIXAuto.setStatus("current")
_RcftInterfaceRRecvRestrictSpeed_Type = Integer32
_RcftInterfaceRRecvRestrictSpeed_Object = MibTableColumn
rcftInterfaceRRecvRestrictSpeed = _RcftInterfaceRRecvRestrictSpeed_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 2, 1, 35),
    _RcftInterfaceRRecvRestrictSpeed_Type()
)
rcftInterfaceRRecvRestrictSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftInterfaceRRecvRestrictSpeed.setStatus("current")


class _RcftInterfaceRFlowCtrl_Type(Integer32):
    """Custom type rcftInterfaceRFlowCtrl based on Integer32"""
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


_RcftInterfaceRFlowCtrl_Type.__name__ = "Integer32"
_RcftInterfaceRFlowCtrl_Object = MibTableColumn
rcftInterfaceRFlowCtrl = _RcftInterfaceRFlowCtrl_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 2, 1, 36),
    _RcftInterfaceRFlowCtrl_Type()
)
rcftInterfaceRFlowCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftInterfaceRFlowCtrl.setStatus("current")


class _RcftInterfaceRAudioType_Type(Integer32):
    """Custom type rcftInterfaceRAudioType based on Integer32"""
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
        *(("magnet", 1),
          ("fxo", 2),
          ("fxs", 3),
          ("reserved", 4))
    )


_RcftInterfaceRAudioType_Type.__name__ = "Integer32"
_RcftInterfaceRAudioType_Object = MibTableColumn
rcftInterfaceRAudioType = _RcftInterfaceRAudioType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 2, 1, 37),
    _RcftInterfaceRAudioType_Type()
)
rcftInterfaceRAudioType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftInterfaceRAudioType.setStatus("current")
_RcftInterfaceRAudioTimeSlots_Type = Unsigned32
_RcftInterfaceRAudioTimeSlots_Object = MibTableColumn
rcftInterfaceRAudioTimeSlots = _RcftInterfaceRAudioTimeSlots_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 2, 1, 38),
    _RcftInterfaceRAudioTimeSlots_Type()
)
rcftInterfaceRAudioTimeSlots.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftInterfaceRAudioTimeSlots.setStatus("current")


class _RcftInterfaceRAudioInSignalingSymbol_Type(Integer32):
    """Custom type rcftInterfaceRAudioInSignalingSymbol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("originalSignaling", 1),
          ("reverseSignaling", 2))
    )


_RcftInterfaceRAudioInSignalingSymbol_Type.__name__ = "Integer32"
_RcftInterfaceRAudioInSignalingSymbol_Object = MibTableColumn
rcftInterfaceRAudioInSignalingSymbol = _RcftInterfaceRAudioInSignalingSymbol_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 2, 1, 39),
    _RcftInterfaceRAudioInSignalingSymbol_Type()
)
rcftInterfaceRAudioInSignalingSymbol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftInterfaceRAudioInSignalingSymbol.setStatus("current")


class _RcftInterfaceRAudioOutSignalingSymbol_Type(Integer32):
    """Custom type rcftInterfaceRAudioOutSignalingSymbol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("originalSignaling", 1),
          ("reverseSignaling", 2))
    )


_RcftInterfaceRAudioOutSignalingSymbol_Type.__name__ = "Integer32"
_RcftInterfaceRAudioOutSignalingSymbol_Object = MibTableColumn
rcftInterfaceRAudioOutSignalingSymbol = _RcftInterfaceRAudioOutSignalingSymbol_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 2, 1, 40),
    _RcftInterfaceRAudioOutSignalingSymbol_Type()
)
rcftInterfaceRAudioOutSignalingSymbol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftInterfaceRAudioOutSignalingSymbol.setStatus("current")


class _RcftInterfaceRAudioInSignalingType_Type(Integer32):
    """Custom type rcftInterfaceRAudioInSignalingType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("aBit", 1),
          ("bBit", 2))
    )


_RcftInterfaceRAudioInSignalingType_Type.__name__ = "Integer32"
_RcftInterfaceRAudioInSignalingType_Object = MibTableColumn
rcftInterfaceRAudioInSignalingType = _RcftInterfaceRAudioInSignalingType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 2, 1, 41),
    _RcftInterfaceRAudioInSignalingType_Type()
)
rcftInterfaceRAudioInSignalingType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftInterfaceRAudioInSignalingType.setStatus("current")


class _RcftInterfaceRAudioOutSignalingType_Type(Integer32):
    """Custom type rcftInterfaceRAudioOutSignalingType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("aBit", 1),
          ("bBit", 2))
    )


_RcftInterfaceRAudioOutSignalingType_Type.__name__ = "Integer32"
_RcftInterfaceRAudioOutSignalingType_Object = MibTableColumn
rcftInterfaceRAudioOutSignalingType = _RcftInterfaceRAudioOutSignalingType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 2, 1, 42),
    _RcftInterfaceRAudioOutSignalingType_Type()
)
rcftInterfaceRAudioOutSignalingType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftInterfaceRAudioOutSignalingType.setStatus("current")


class _RcftInterfaceRAudioInSignalingStatus_Type(Integer32):
    """Custom type rcftInterfaceRAudioInSignalingStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("idle", 1),
          ("occupied", 2))
    )


_RcftInterfaceRAudioInSignalingStatus_Type.__name__ = "Integer32"
_RcftInterfaceRAudioInSignalingStatus_Object = MibTableColumn
rcftInterfaceRAudioInSignalingStatus = _RcftInterfaceRAudioInSignalingStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 2, 1, 43),
    _RcftInterfaceRAudioInSignalingStatus_Type()
)
rcftInterfaceRAudioInSignalingStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftInterfaceRAudioInSignalingStatus.setStatus("current")


class _RcftInterfaceRAudioOutSignalingStatus_Type(Integer32):
    """Custom type rcftInterfaceRAudioOutSignalingStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("idle", 1),
          ("occupied", 2))
    )


_RcftInterfaceRAudioOutSignalingStatus_Type.__name__ = "Integer32"
_RcftInterfaceRAudioOutSignalingStatus_Object = MibTableColumn
rcftInterfaceRAudioOutSignalingStatus = _RcftInterfaceRAudioOutSignalingStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 2, 1, 44),
    _RcftInterfaceRAudioOutSignalingStatus_Type()
)
rcftInterfaceRAudioOutSignalingStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftInterfaceRAudioOutSignalingStatus.setStatus("current")


class _RcftInterfaceRAudioUseEnable_Type(Integer32):
    """Custom type rcftInterfaceRAudioUseEnable based on Integer32"""
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


_RcftInterfaceRAudioUseEnable_Type.__name__ = "Integer32"
_RcftInterfaceRAudioUseEnable_Object = MibTableColumn
rcftInterfaceRAudioUseEnable = _RcftInterfaceRAudioUseEnable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 2, 1, 45),
    _RcftInterfaceRAudioUseEnable_Type()
)
rcftInterfaceRAudioUseEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftInterfaceRAudioUseEnable.setStatus("current")


class _RcftInterfaceWANToLANFPEnWANDownLANPortStatus_Type(Integer32):
    """Custom type rcftInterfaceWANToLANFPEnWANDownLANPortStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("linkup", 1),
          ("linkdown", 2))
    )


_RcftInterfaceWANToLANFPEnWANDownLANPortStatus_Type.__name__ = "Integer32"
_RcftInterfaceWANToLANFPEnWANDownLANPortStatus_Object = MibTableColumn
rcftInterfaceWANToLANFPEnWANDownLANPortStatus = _RcftInterfaceWANToLANFPEnWANDownLANPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 2, 1, 46),
    _RcftInterfaceWANToLANFPEnWANDownLANPortStatus_Type()
)
rcftInterfaceWANToLANFPEnWANDownLANPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftInterfaceWANToLANFPEnWANDownLANPortStatus.setStatus("current")


class _RcftInterfaceWANTOLANFPEnRemoteLANDownLANPortStatus_Type(Integer32):
    """Custom type rcftInterfaceWANTOLANFPEnRemoteLANDownLANPortStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("linkup", 1),
          ("linkdown", 2))
    )


_RcftInterfaceWANTOLANFPEnRemoteLANDownLANPortStatus_Type.__name__ = "Integer32"
_RcftInterfaceWANTOLANFPEnRemoteLANDownLANPortStatus_Object = MibTableColumn
rcftInterfaceWANTOLANFPEnRemoteLANDownLANPortStatus = _RcftInterfaceWANTOLANFPEnRemoteLANDownLANPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 2, 1, 47),
    _RcftInterfaceWANTOLANFPEnRemoteLANDownLANPortStatus_Type()
)
rcftInterfaceWANTOLANFPEnRemoteLANDownLANPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftInterfaceWANTOLANFPEnRemoteLANDownLANPortStatus.setStatus("current")
_RcftInterfaceRecvFluxCount_Type = Integer32
_RcftInterfaceRecvFluxCount_Object = MibTableColumn
rcftInterfaceRecvFluxCount = _RcftInterfaceRecvFluxCount_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 2, 1, 48),
    _RcftInterfaceRecvFluxCount_Type()
)
rcftInterfaceRecvFluxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftInterfaceRecvFluxCount.setStatus("current")
_RcftInterfaceSendFluxCount_Type = Integer32
_RcftInterfaceSendFluxCount_Object = MibTableColumn
rcftInterfaceSendFluxCount = _RcftInterfaceSendFluxCount_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 2, 1, 49),
    _RcftInterfaceSendFluxCount_Type()
)
rcftInterfaceSendFluxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftInterfaceSendFluxCount.setStatus("current")
_RcftInterfaceRecvFluxPacket_Type = Integer32
_RcftInterfaceRecvFluxPacket_Object = MibTableColumn
rcftInterfaceRecvFluxPacket = _RcftInterfaceRecvFluxPacket_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 2, 1, 50),
    _RcftInterfaceRecvFluxPacket_Type()
)
rcftInterfaceRecvFluxPacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftInterfaceRecvFluxPacket.setStatus("current")
_RcftInterfaceSendFluxPacket_Type = Integer32
_RcftInterfaceSendFluxPacket_Object = MibTableColumn
rcftInterfaceSendFluxPacket = _RcftInterfaceSendFluxPacket_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 2, 1, 51),
    _RcftInterfaceSendFluxPacket_Type()
)
rcftInterfaceSendFluxPacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftInterfaceSendFluxPacket.setStatus("current")
_RcftInterfaceRecvErrFluxPacket_Type = Integer32
_RcftInterfaceRecvErrFluxPacket_Object = MibTableColumn
rcftInterfaceRecvErrFluxPacket = _RcftInterfaceRecvErrFluxPacket_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 2, 1, 52),
    _RcftInterfaceRecvErrFluxPacket_Type()
)
rcftInterfaceRecvErrFluxPacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftInterfaceRecvErrFluxPacket.setStatus("current")
_RcftInterfaceSendErrFluxPacket_Type = Integer32
_RcftInterfaceSendErrFluxPacket_Object = MibTableColumn
rcftInterfaceSendErrFluxPacket = _RcftInterfaceSendErrFluxPacket_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 2, 1, 53),
    _RcftInterfaceSendErrFluxPacket_Type()
)
rcftInterfaceSendErrFluxPacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftInterfaceSendErrFluxPacket.setStatus("current")
_RcftInterfaceRecvFluxTimer_Type = Counter32
_RcftInterfaceRecvFluxTimer_Object = MibTableColumn
rcftInterfaceRecvFluxTimer = _RcftInterfaceRecvFluxTimer_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 2, 1, 54),
    _RcftInterfaceRecvFluxTimer_Type()
)
rcftInterfaceRecvFluxTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftInterfaceRecvFluxTimer.setStatus("current")
_RcftInterfaceSendFluxTimer_Type = Counter32
_RcftInterfaceSendFluxTimer_Object = MibTableColumn
rcftInterfaceSendFluxTimer = _RcftInterfaceSendFluxTimer_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 2, 1, 55),
    _RcftInterfaceSendFluxTimer_Type()
)
rcftInterfaceSendFluxTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftInterfaceSendFluxTimer.setStatus("current")
_RcftInterfaceRSendRestrictSpeed_Type = Integer32
_RcftInterfaceRSendRestrictSpeed_Object = MibTableColumn
rcftInterfaceRSendRestrictSpeed = _RcftInterfaceRSendRestrictSpeed_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 2, 1, 56),
    _RcftInterfaceRSendRestrictSpeed_Type()
)
rcftInterfaceRSendRestrictSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftInterfaceRSendRestrictSpeed.setStatus("current")


class _RcftInterfaceRWANToLANFPEnWANDownLANPortStatus_Type(Integer32):
    """Custom type rcftInterfaceRWANToLANFPEnWANDownLANPortStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("open", 1),
          ("close", 2))
    )


_RcftInterfaceRWANToLANFPEnWANDownLANPortStatus_Type.__name__ = "Integer32"
_RcftInterfaceRWANToLANFPEnWANDownLANPortStatus_Object = MibTableColumn
rcftInterfaceRWANToLANFPEnWANDownLANPortStatus = _RcftInterfaceRWANToLANFPEnWANDownLANPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 2, 1, 57),
    _RcftInterfaceRWANToLANFPEnWANDownLANPortStatus_Type()
)
rcftInterfaceRWANToLANFPEnWANDownLANPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftInterfaceRWANToLANFPEnWANDownLANPortStatus.setStatus("current")


class _RcftInterfaceRWANTOLANFPEnRemoteLANDownLANPortStatus_Type(Integer32):
    """Custom type rcftInterfaceRWANTOLANFPEnRemoteLANDownLANPortStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("open", 1),
          ("close", 2))
    )


_RcftInterfaceRWANTOLANFPEnRemoteLANDownLANPortStatus_Type.__name__ = "Integer32"
_RcftInterfaceRWANTOLANFPEnRemoteLANDownLANPortStatus_Object = MibTableColumn
rcftInterfaceRWANTOLANFPEnRemoteLANDownLANPortStatus = _RcftInterfaceRWANTOLANFPEnRemoteLANDownLANPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 2, 1, 58),
    _RcftInterfaceRWANTOLANFPEnRemoteLANDownLANPortStatus_Type()
)
rcftInterfaceRWANTOLANFPEnRemoteLANDownLANPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftInterfaceRWANTOLANFPEnRemoteLANDownLANPortStatus.setStatus("current")
_RcftInterfaceRRecvFluxPacket_Type = Integer32
_RcftInterfaceRRecvFluxPacket_Object = MibTableColumn
rcftInterfaceRRecvFluxPacket = _RcftInterfaceRRecvFluxPacket_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 2, 1, 59),
    _RcftInterfaceRRecvFluxPacket_Type()
)
rcftInterfaceRRecvFluxPacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftInterfaceRRecvFluxPacket.setStatus("current")
_RcftInterfaceRSendFluxPacket_Type = Integer32
_RcftInterfaceRSendFluxPacket_Object = MibTableColumn
rcftInterfaceRSendFluxPacket = _RcftInterfaceRSendFluxPacket_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 2, 1, 60),
    _RcftInterfaceRSendFluxPacket_Type()
)
rcftInterfaceRSendFluxPacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftInterfaceRSendFluxPacket.setStatus("current")
_RcftInterfaceRRecvErrFluxPacket_Type = Integer32
_RcftInterfaceRRecvErrFluxPacket_Object = MibTableColumn
rcftInterfaceRRecvErrFluxPacket = _RcftInterfaceRRecvErrFluxPacket_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 2, 1, 61),
    _RcftInterfaceRRecvErrFluxPacket_Type()
)
rcftInterfaceRRecvErrFluxPacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftInterfaceRRecvErrFluxPacket.setStatus("current")
_RcftInterfaceRSendErrFluxPacket_Type = Integer32
_RcftInterfaceRSendErrFluxPacket_Object = MibTableColumn
rcftInterfaceRSendErrFluxPacket = _RcftInterfaceRSendErrFluxPacket_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 2, 1, 62),
    _RcftInterfaceRSendErrFluxPacket_Type()
)
rcftInterfaceRSendErrFluxPacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftInterfaceRSendErrFluxPacket.setStatus("current")


class _RcftInterfaceFoundLink_Type(Integer32):
    """Custom type rcftInterfaceFoundLink based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              100)
        )
    )
    namedValues = NamedValues(
        *(("success", 1),
          ("failForDelay", 2),
          ("failForOtherReason", 100))
    )


_RcftInterfaceFoundLink_Type.__name__ = "Integer32"
_RcftInterfaceFoundLink_Object = MibTableColumn
rcftInterfaceFoundLink = _RcftInterfaceFoundLink_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 2, 1, 63),
    _RcftInterfaceFoundLink_Type()
)
rcftInterfaceFoundLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftInterfaceFoundLink.setStatus("current")


class _RcftInterfaceBERT_Type(Integer32):
    """Custom type rcftInterfaceBERT based on Integer32"""
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


_RcftInterfaceBERT_Type.__name__ = "Integer32"
_RcftInterfaceBERT_Object = MibTableColumn
rcftInterfaceBERT = _RcftInterfaceBERT_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 2, 1, 64),
    _RcftInterfaceBERT_Type()
)
rcftInterfaceBERT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftInterfaceBERT.setStatus("current")


class _RcftInterfaceCLKMode_Type(Integer32):
    """Custom type rcftInterfaceCLKMode based on Integer32"""
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
        *(("secondary", 1),
          ("v35terminal", 2),
          ("master", 3),
          ("reserved", 4))
    )


_RcftInterfaceCLKMode_Type.__name__ = "Integer32"
_RcftInterfaceCLKMode_Object = MibTableColumn
rcftInterfaceCLKMode = _RcftInterfaceCLKMode_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 2, 1, 65),
    _RcftInterfaceCLKMode_Type()
)
rcftInterfaceCLKMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftInterfaceCLKMode.setStatus("current")


class _RcftInterfaceCRCStatus_Type(Integer32):
    """Custom type rcftInterfaceCRCStatus based on Integer32"""
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


_RcftInterfaceCRCStatus_Type.__name__ = "Integer32"
_RcftInterfaceCRCStatus_Object = MibTableColumn
rcftInterfaceCRCStatus = _RcftInterfaceCRCStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 2, 1, 66),
    _RcftInterfaceCRCStatus_Type()
)
rcftInterfaceCRCStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftInterfaceCRCStatus.setStatus("current")


class _RcftInterfaceCRCEnable_Type(Integer32):
    """Custom type rcftInterfaceCRCEnable based on Integer32"""
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


_RcftInterfaceCRCEnable_Type.__name__ = "Integer32"
_RcftInterfaceCRCEnable_Object = MibTableColumn
rcftInterfaceCRCEnable = _RcftInterfaceCRCEnable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 2, 1, 67),
    _RcftInterfaceCRCEnable_Type()
)
rcftInterfaceCRCEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftInterfaceCRCEnable.setStatus("current")


class _RcftInterfaceLocalLoopEn_Type(Integer32):
    """Custom type rcftInterfaceLocalLoopEn based on Integer32"""
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


_RcftInterfaceLocalLoopEn_Type.__name__ = "Integer32"
_RcftInterfaceLocalLoopEn_Object = MibTableColumn
rcftInterfaceLocalLoopEn = _RcftInterfaceLocalLoopEn_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 2, 1, 68),
    _RcftInterfaceLocalLoopEn_Type()
)
rcftInterfaceLocalLoopEn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftInterfaceLocalLoopEn.setStatus("current")


class _RcftInterfaceRemoteLoopEn_Type(Integer32):
    """Custom type rcftInterfaceRemoteLoopEn based on Integer32"""
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


_RcftInterfaceRemoteLoopEn_Type.__name__ = "Integer32"
_RcftInterfaceRemoteLoopEn_Object = MibTableColumn
rcftInterfaceRemoteLoopEn = _RcftInterfaceRemoteLoopEn_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 2, 1, 69),
    _RcftInterfaceRemoteLoopEn_Type()
)
rcftInterfaceRemoteLoopEn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftInterfaceRemoteLoopEn.setStatus("current")


class _RcftInterfaceTransErrorCode_Type(Integer32):
    """Custom type rcftInterfaceTransErrorCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("less10E-6", 1),
          ("more10E-6", 2),
          ("more10E-3", 3))
    )


_RcftInterfaceTransErrorCode_Type.__name__ = "Integer32"
_RcftInterfaceTransErrorCode_Object = MibTableColumn
rcftInterfaceTransErrorCode = _RcftInterfaceTransErrorCode_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 2, 1, 70),
    _RcftInterfaceTransErrorCode_Type()
)
rcftInterfaceTransErrorCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftInterfaceTransErrorCode.setStatus("current")


class _RcftInterfaceE1Location_Type(Integer32):
    """Custom type rcftInterfaceE1Location based on Integer32"""
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
              100)
        )
    )
    namedValues = NamedValues(
        *(("e1-1", 1),
          ("e1-2", 2),
          ("e1-3", 3),
          ("e1-4", 4),
          ("e1-5", 5),
          ("e1-6", 6),
          ("e1-7", 7),
          ("e1-8", 8),
          ("unknown", 100))
    )


_RcftInterfaceE1Location_Type.__name__ = "Integer32"
_RcftInterfaceE1Location_Object = MibTableColumn
rcftInterfaceE1Location = _RcftInterfaceE1Location_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 2, 1, 71),
    _RcftInterfaceE1Location_Type()
)
rcftInterfaceE1Location.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftInterfaceE1Location.setStatus("current")
_RcftInterfaceE1ESCnt_Type = Integer32
_RcftInterfaceE1ESCnt_Object = MibTableColumn
rcftInterfaceE1ESCnt = _RcftInterfaceE1ESCnt_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 2, 1, 72),
    _RcftInterfaceE1ESCnt_Type()
)
rcftInterfaceE1ESCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftInterfaceE1ESCnt.setStatus("current")
_RcftInterfaceE1SESCnt_Type = Integer32
_RcftInterfaceE1SESCnt_Object = MibTableColumn
rcftInterfaceE1SESCnt = _RcftInterfaceE1SESCnt_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 2, 1, 73),
    _RcftInterfaceE1SESCnt_Type()
)
rcftInterfaceE1SESCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftInterfaceE1SESCnt.setStatus("current")
_RcftInterfaceE1TimeSlot_Type = Unsigned32
_RcftInterfaceE1TimeSlot_Object = MibTableColumn
rcftInterfaceE1TimeSlot = _RcftInterfaceE1TimeSlot_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 2, 1, 74),
    _RcftInterfaceE1TimeSlot_Type()
)
rcftInterfaceE1TimeSlot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftInterfaceE1TimeSlot.setStatus("current")


class _RcftInterfaceE1Transparent_Type(Integer32):
    """Custom type rcftInterfaceE1Transparent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("transparent", 1),
          ("pcm", 2))
    )


_RcftInterfaceE1Transparent_Type.__name__ = "Integer32"
_RcftInterfaceE1Transparent_Object = MibTableColumn
rcftInterfaceE1Transparent = _RcftInterfaceE1Transparent_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 2, 1, 75),
    _RcftInterfaceE1Transparent_Type()
)
rcftInterfaceE1Transparent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftInterfaceE1Transparent.setStatus("current")
_RcftStmStatTable_Object = MibTable
rcftStmStatTable = _RcftStmStatTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 3)
)
if mibBuilder.loadTexts:
    rcftStmStatTable.setStatus("current")
_RcftStmStatEntry_Object = MibTableRow
rcftStmStatEntry = _RcftStmStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 3, 1)
)
rcftStmStatEntry.setIndexNames(
    (0, "RAISECOM-RCFT-MIB", "rcftChassisIndex"),
    (0, "RAISECOM-RCFT-MIB", "rcftSlotIndex"),
)
if mibBuilder.loadTexts:
    rcftStmStatEntry.setStatus("current")


class _RcftStmAdminStatus_Type(Integer32):
    """Custom type rcftStmAdminStatus based on Integer32"""
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
        *(("fiberPortLoopbackTestMode1Enable", 1),
          ("fiberPortLoopbackTestDisable", 2),
          ("fiberPortLoopbackTestMode2Enable", 3),
          ("bncPortLoopbackTestMode1Enable", 4),
          ("bncPortLoopbackTestDisable", 5),
          ("bncPortLoopbackTestMode2Enable", 6))
    )


_RcftStmAdminStatus_Type.__name__ = "Integer32"
_RcftStmAdminStatus_Object = MibTableColumn
rcftStmAdminStatus = _RcftStmAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 3, 1, 1),
    _RcftStmAdminStatus_Type()
)
rcftStmAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftStmAdminStatus.setStatus("current")


class _RcftStmFiberPort_Type(Integer32):
    """Custom type rcftStmFiberPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("open", 1),
          ("close", 2))
    )


_RcftStmFiberPort_Type.__name__ = "Integer32"
_RcftStmFiberPort_Object = MibTableColumn
rcftStmFiberPort = _RcftStmFiberPort_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 3, 1, 2),
    _RcftStmFiberPort_Type()
)
rcftStmFiberPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftStmFiberPort.setStatus("current")


class _RcftStmFiberRxPllUnlck_Type(Integer32):
    """Custom type rcftStmFiberRxPllUnlck based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("alarm", 2))
    )


_RcftStmFiberRxPllUnlck_Type.__name__ = "Integer32"
_RcftStmFiberRxPllUnlck_Object = MibTableColumn
rcftStmFiberRxPllUnlck = _RcftStmFiberRxPllUnlck_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 3, 1, 3),
    _RcftStmFiberRxPllUnlck_Type()
)
rcftStmFiberRxPllUnlck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftStmFiberRxPllUnlck.setStatus("current")


class _RcftStmFiberTxClkLos_Type(Integer32):
    """Custom type rcftStmFiberTxClkLos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("alarm", 2))
    )


_RcftStmFiberTxClkLos_Type.__name__ = "Integer32"
_RcftStmFiberTxClkLos_Object = MibTableColumn
rcftStmFiberTxClkLos = _RcftStmFiberTxClkLos_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 3, 1, 4),
    _RcftStmFiberTxClkLos_Type()
)
rcftStmFiberTxClkLos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftStmFiberTxClkLos.setStatus("current")


class _RcftStmFiberAnalogLos_Type(Integer32):
    """Custom type rcftStmFiberAnalogLos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("alarm", 2))
    )


_RcftStmFiberAnalogLos_Type.__name__ = "Integer32"
_RcftStmFiberAnalogLos_Object = MibTableColumn
rcftStmFiberAnalogLos = _RcftStmFiberAnalogLos_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 3, 1, 5),
    _RcftStmFiberAnalogLos_Type()
)
rcftStmFiberAnalogLos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftStmFiberAnalogLos.setStatus("current")


class _RcftStmFiberDigitalLos_Type(Integer32):
    """Custom type rcftStmFiberDigitalLos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("alarm", 2))
    )


_RcftStmFiberDigitalLos_Type.__name__ = "Integer32"
_RcftStmFiberDigitalLos_Object = MibTableColumn
rcftStmFiberDigitalLos = _RcftStmFiberDigitalLos_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 3, 1, 6),
    _RcftStmFiberDigitalLos_Type()
)
rcftStmFiberDigitalLos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftStmFiberDigitalLos.setStatus("current")


class _RcftStmFiberSyncLos_Type(Integer32):
    """Custom type rcftStmFiberSyncLos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("alarm", 2))
    )


_RcftStmFiberSyncLos_Type.__name__ = "Integer32"
_RcftStmFiberSyncLos_Object = MibTableColumn
rcftStmFiberSyncLos = _RcftStmFiberSyncLos_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 3, 1, 7),
    _RcftStmFiberSyncLos_Type()
)
rcftStmFiberSyncLos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftStmFiberSyncLos.setStatus("current")


class _RcftStmBncPort_Type(Integer32):
    """Custom type rcftStmBncPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("open", 1),
          ("close", 2))
    )


_RcftStmBncPort_Type.__name__ = "Integer32"
_RcftStmBncPort_Object = MibTableColumn
rcftStmBncPort = _RcftStmBncPort_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 3, 1, 8),
    _RcftStmBncPort_Type()
)
rcftStmBncPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftStmBncPort.setStatus("current")


class _RcftStmBncRxPllUnlck_Type(Integer32):
    """Custom type rcftStmBncRxPllUnlck based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("alarm", 2))
    )


_RcftStmBncRxPllUnlck_Type.__name__ = "Integer32"
_RcftStmBncRxPllUnlck_Object = MibTableColumn
rcftStmBncRxPllUnlck = _RcftStmBncRxPllUnlck_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 3, 1, 9),
    _RcftStmBncRxPllUnlck_Type()
)
rcftStmBncRxPllUnlck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftStmBncRxPllUnlck.setStatus("current")


class _RcftStmBncTxClkLos_Type(Integer32):
    """Custom type rcftStmBncTxClkLos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("alarm", 2))
    )


_RcftStmBncTxClkLos_Type.__name__ = "Integer32"
_RcftStmBncTxClkLos_Object = MibTableColumn
rcftStmBncTxClkLos = _RcftStmBncTxClkLos_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 3, 1, 10),
    _RcftStmBncTxClkLos_Type()
)
rcftStmBncTxClkLos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftStmBncTxClkLos.setStatus("current")


class _RcftStmBncAnalogLos_Type(Integer32):
    """Custom type rcftStmBncAnalogLos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("alarm", 2))
    )


_RcftStmBncAnalogLos_Type.__name__ = "Integer32"
_RcftStmBncAnalogLos_Object = MibTableColumn
rcftStmBncAnalogLos = _RcftStmBncAnalogLos_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 3, 1, 11),
    _RcftStmBncAnalogLos_Type()
)
rcftStmBncAnalogLos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftStmBncAnalogLos.setStatus("current")


class _RcftStmBncDigitalLos_Type(Integer32):
    """Custom type rcftStmBncDigitalLos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("alarm", 2))
    )


_RcftStmBncDigitalLos_Type.__name__ = "Integer32"
_RcftStmBncDigitalLos_Object = MibTableColumn
rcftStmBncDigitalLos = _RcftStmBncDigitalLos_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 3, 1, 12),
    _RcftStmBncDigitalLos_Type()
)
rcftStmBncDigitalLos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftStmBncDigitalLos.setStatus("current")


class _RcftStmBncSyncLos_Type(Integer32):
    """Custom type rcftStmBncSyncLos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("alarm", 2))
    )


_RcftStmBncSyncLos_Type.__name__ = "Integer32"
_RcftStmBncSyncLos_Object = MibTableColumn
rcftStmBncSyncLos = _RcftStmBncSyncLos_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 3, 1, 13),
    _RcftStmBncSyncLos_Type()
)
rcftStmBncSyncLos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftStmBncSyncLos.setStatus("current")
_RcftConfigFlagTable_Object = MibTable
rcftConfigFlagTable = _RcftConfigFlagTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 11)
)
if mibBuilder.loadTexts:
    rcftConfigFlagTable.setStatus("current")
_RcftConfigFlagEntry_Object = MibTableRow
rcftConfigFlagEntry = _RcftConfigFlagEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 11, 1)
)
rcftConfigFlagEntry.setIndexNames(
    (0, "RAISECOM-RCFT-MIB", "rcftChassisIndex"),
    (0, "RAISECOM-RCFT-MIB", "rcftSlotIndex"),
)
if mibBuilder.loadTexts:
    rcftConfigFlagEntry.setStatus("current")
_RcftLocalDeviceConfigFinishFlag_Type = Integer32
_RcftLocalDeviceConfigFinishFlag_Object = MibTableColumn
rcftLocalDeviceConfigFinishFlag = _RcftLocalDeviceConfigFinishFlag_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 11, 1, 1),
    _RcftLocalDeviceConfigFinishFlag_Type()
)
rcftLocalDeviceConfigFinishFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftLocalDeviceConfigFinishFlag.setStatus("current")
_RcftSlotConfStatTable_Object = MibTable
rcftSlotConfStatTable = _RcftSlotConfStatTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 12)
)
if mibBuilder.loadTexts:
    rcftSlotConfStatTable.setStatus("current")
_RcftSlotConfStatEntry_Object = MibTableRow
rcftSlotConfStatEntry = _RcftSlotConfStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 12, 1)
)
rcftSlotConfStatEntry.setIndexNames(
    (0, "RAISECOM-RCFT-MIB", "rcftChassisIndex"),
    (0, "RAISECOM-RCFT-MIB", "rcftSlotIndex"),
)
if mibBuilder.loadTexts:
    rcftSlotConfStatEntry.setStatus("current")


class _RcftSlotConfEDuplex_Type(Integer32):
    """Custom type rcftSlotConfEDuplex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("full-duplex", 1),
          ("half-duplex", 2),
          ("auto", 3))
    )


_RcftSlotConfEDuplex_Type.__name__ = "Integer32"
_RcftSlotConfEDuplex_Object = MibTableColumn
rcftSlotConfEDuplex = _RcftSlotConfEDuplex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 12, 1, 1),
    _RcftSlotConfEDuplex_Type()
)
rcftSlotConfEDuplex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftSlotConfEDuplex.setStatus("current")


class _RcftSlotConfESpeed_Type(Integer32):
    """Custom type rcftSlotConfESpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              16)
        )
    )
    namedValues = NamedValues(
        *(("rcft10Mbps", 1),
          ("rcft100Mbps", 2),
          ("rcft1000Mbps", 3),
          ("rcft10Gbps", 4),
          ("other", 16))
    )


_RcftSlotConfESpeed_Type.__name__ = "Integer32"
_RcftSlotConfESpeed_Object = MibTableColumn
rcftSlotConfESpeed = _RcftSlotConfESpeed_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 12, 1, 2),
    _RcftSlotConfESpeed_Type()
)
rcftSlotConfESpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftSlotConfESpeed.setStatus("current")


class _RcftRSlotConfEDuplex_Type(Integer32):
    """Custom type rcftRSlotConfEDuplex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("full-duplex", 1),
          ("half-duplex", 2),
          ("auto", 3))
    )


_RcftRSlotConfEDuplex_Type.__name__ = "Integer32"
_RcftRSlotConfEDuplex_Object = MibTableColumn
rcftRSlotConfEDuplex = _RcftRSlotConfEDuplex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 12, 1, 3),
    _RcftRSlotConfEDuplex_Type()
)
rcftRSlotConfEDuplex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftRSlotConfEDuplex.setStatus("current")


class _RcftRSlotConfESpeed_Type(Integer32):
    """Custom type rcftRSlotConfESpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              16)
        )
    )
    namedValues = NamedValues(
        *(("rcft10Mbps", 1),
          ("rcft100Mbps", 2),
          ("rcft1000Mbps", 3),
          ("rcft10Gbps", 4),
          ("other", 16))
    )


_RcftRSlotConfESpeed_Type.__name__ = "Integer32"
_RcftRSlotConfESpeed_Object = MibTableColumn
rcftRSlotConfESpeed = _RcftRSlotConfESpeed_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 12, 1, 4),
    _RcftRSlotConfESpeed_Type()
)
rcftRSlotConfESpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftRSlotConfESpeed.setStatus("current")
_RcftConfTxWorkStatus_Type = Integer32
_RcftConfTxWorkStatus_Object = MibTableColumn
rcftConfTxWorkStatus = _RcftConfTxWorkStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 12, 1, 5),
    _RcftConfTxWorkStatus_Type()
)
rcftConfTxWorkStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftConfTxWorkStatus.setStatus("current")

# Managed Objects groups


# Notification objects

rcft5VPowerTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 0, 1)
)
rcft5VPowerTrap.setObjects(
    ("RAISECOM-RCFT-MIB", "rcft5vStatus")
)
if mibBuilder.loadTexts:
    rcft5VPowerTrap.setStatus(
        "current"
    )

rcft12VPowerTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 0, 2)
)
rcft12VPowerTrap.setObjects(
    ("RAISECOM-RCFT-MIB", "rcft12vStatus")
)
if mibBuilder.loadTexts:
    rcft12VPowerTrap.setStatus(
        "current"
    )

rcftFanTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 0, 3)
)
rcftFanTrap.setObjects(
    ("RAISECOM-RCFT-MIB", "rcftFanStatus")
)
if mibBuilder.loadTexts:
    rcftFanTrap.setStatus(
        "current"
    )

rcftTmptTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 0, 4)
)
rcftTmptTrap.setObjects(
    ("RAISECOM-RCFT-MIB", "rcftChassisTmpt")
)
if mibBuilder.loadTexts:
    rcftTmptTrap.setStatus(
        "current"
    )

rcftChassisTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 0, 5)
)
rcftChassisTrap.setObjects(
    ("RAISECOM-RCFT-MIB", "rcftChassisExist")
)
if mibBuilder.loadTexts:
    rcftChassisTrap.setStatus(
        "current"
    )

rcftELinkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 0, 6)
)
rcftELinkTrap.setObjects(
    ("RAISECOM-RCFT-MIB", "rcftSlotELink")
)
if mibBuilder.loadTexts:
    rcftELinkTrap.setStatus(
        "current"
    )

rcftRELinkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 0, 7)
)
rcftRELinkTrap.setObjects(
    ("RAISECOM-RCFT-MIB", "rcftRSlotELink")
)
if mibBuilder.loadTexts:
    rcftRELinkTrap.setStatus(
        "current"
    )

rcftOLinkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 0, 8)
)
rcftOLinkTrap.setObjects(
    ("RAISECOM-RCFT-MIB", "rcftSlotOLink")
)
if mibBuilder.loadTexts:
    rcftOLinkTrap.setStatus(
        "current"
    )

rcftORLnkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 0, 9)
)
rcftORLnkTrap.setObjects(
    ("RAISECOM-RCFT-MIB", "rcftSlotORLnk")
)
if mibBuilder.loadTexts:
    rcftORLnkTrap.setStatus(
        "current"
    )

rcftOTLnkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 0, 10)
)
rcftOTLnkTrap.setObjects(
    ("RAISECOM-RCFT-MIB", "rcftSlotOTLnk")
)
if mibBuilder.loadTexts:
    rcftOTLnkTrap.setStatus(
        "current"
    )

rcftROLinkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 0, 11)
)
rcftROLinkTrap.setObjects(
    ("RAISECOM-RCFT-MIB", "rcftRSlotOLink")
)
if mibBuilder.loadTexts:
    rcftROLinkTrap.setStatus(
        "current"
    )

rcftESpeedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 0, 12)
)
rcftESpeedTrap.setObjects(
    ("RAISECOM-RCFT-MIB", "rcftSlotESpeed")
)
if mibBuilder.loadTexts:
    rcftESpeedTrap.setStatus(
        "current"
    )

rcftSlotTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 0, 13)
)
rcftSlotTrap.setObjects(
    ("RAISECOM-RCFT-MIB", "rcftSlotExist")
)
if mibBuilder.loadTexts:
    rcftSlotTrap.setStatus(
        "current"
    )

rcftBackplaneLossTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 0, 14)
)
rcftBackplaneLossTrap.setObjects(
    ("RAISECOM-RCFT-MIB", "rcftChassisExist")
)
if mibBuilder.loadTexts:
    rcftBackplaneLossTrap.setStatus(
        "current"
    )

rcftVOLimitTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 0, 15)
)
rcftVOLimitTrap.setObjects(
    ("RAISECOM-RCFT-MIB", "rcftSlotVOLimit")
)
if mibBuilder.loadTexts:
    rcftVOLimitTrap.setStatus(
        "current"
    )

rcftVBLimitTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 0, 16)
)
rcftVBLimitTrap.setObjects(
    ("RAISECOM-RCFT-MIB", "rcftSlotVBLimit")
)
if mibBuilder.loadTexts:
    rcftVBLimitTrap.setStatus(
        "current"
    )

rcftRVOLimitTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 0, 17)
)
rcftRVOLimitTrap.setObjects(
    ("RAISECOM-RCFT-MIB", "rcftRSlotVOLimit")
)
if mibBuilder.loadTexts:
    rcftRVOLimitTrap.setStatus(
        "current"
    )

rcftRVBLimitTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 0, 18)
)
rcftRVBLimitTrap.setObjects(
    ("RAISECOM-RCFT-MIB", "rcftRSlotVBLimit")
)
if mibBuilder.loadTexts:
    rcftRVBLimitTrap.setStatus(
        "current"
    )

rcftOSendPowerTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 0, 19)
)
rcftOSendPowerTrap.setObjects(
    ("RAISECOM-RCFT-MIB", "rcftSlotOSendPower")
)
if mibBuilder.loadTexts:
    rcftOSendPowerTrap.setStatus(
        "current"
    )

rcftROSendPowerTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 0, 20)
)
rcftROSendPowerTrap.setObjects(
    ("RAISECOM-RCFT-MIB", "rcftRSlotOSendPower")
)
if mibBuilder.loadTexts:
    rcftROSendPowerTrap.setStatus(
        "current"
    )

rcftOReceSenTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 0, 21)
)
rcftOReceSenTrap.setObjects(
    ("RAISECOM-RCFT-MIB", "rcftSlotOReceSen")
)
if mibBuilder.loadTexts:
    rcftOReceSenTrap.setStatus(
        "current"
    )

rcftROReceSenTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 0, 22)
)
rcftROReceSenTrap.setObjects(
    ("RAISECOM-RCFT-MIB", "rcftRSlotOReceSen")
)
if mibBuilder.loadTexts:
    rcftROReceSenTrap.setStatus(
        "current"
    )

rcftOLaserTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 0, 23)
)
rcftOLaserTrap.setObjects(
    ("RAISECOM-RCFT-MIB", "rcftSlotOLaser")
)
if mibBuilder.loadTexts:
    rcftOLaserTrap.setStatus(
        "current"
    )

rcftROLaserTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 0, 24)
)
rcftROLaserTrap.setObjects(
    ("RAISECOM-RCFT-MIB", "rcftRSlotOLaser")
)
if mibBuilder.loadTexts:
    rcftROLaserTrap.setStatus(
        "current"
    )

rcftOSDTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 0, 25)
)
rcftOSDTrap.setObjects(
    ("RAISECOM-RCFT-MIB", "rcftSlotOSD")
)
if mibBuilder.loadTexts:
    rcftOSDTrap.setStatus(
        "current"
    )

rcftROSDTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 0, 26)
)
rcftROSDTrap.setObjects(
    ("RAISECOM-RCFT-MIB", "rcftRSlotOSD")
)
if mibBuilder.loadTexts:
    rcftROSDTrap.setStatus(
        "current"
    )

rcftRSlotChassisTmptTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 0, 27)
)
rcftRSlotChassisTmptTrap.setObjects(
    ("RAISECOM-RCFT-MIB", "rcftRSlotChassisTmpt")
)
if mibBuilder.loadTexts:
    rcftRSlotChassisTmptTrap.setStatus(
        "current"
    )

rcftRSlotFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 0, 28)
)
rcftRSlotFault.setObjects(
    ("RAISECOM-RCFT-MIB", "rcftRSlotExist")
)
if mibBuilder.loadTexts:
    rcftRSlotFault.setStatus(
        "current"
    )

rcftSlotFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 0, 29)
)
rcftSlotFault.setObjects(
    ("RAISECOM-RCFT-MIB", "rcftSlotExist")
)
if mibBuilder.loadTexts:
    rcftSlotFault.setStatus(
        "current"
    )

rcftRSlotExistNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 0, 30)
)
rcftRSlotExistNotify.setObjects(
    ("RAISECOM-RCFT-MIB", "rcftRSlotExist")
)
if mibBuilder.loadTexts:
    rcftRSlotExistNotify.setStatus(
        "current"
    )

rcftSlotE1LOSTRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 0, 31)
)
rcftSlotE1LOSTRAP.setObjects(
    ("RAISECOM-RCFT-MIB", "rcftSlotE1LOS")
)
if mibBuilder.loadTexts:
    rcftSlotE1LOSTRAP.setStatus(
        "current"
    )

rcftSlotOLOSTRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 0, 32)
)
rcftSlotOLOSTRAP.setObjects(
    ("RAISECOM-RCFT-MIB", "rcftSlotOLOS")
)
if mibBuilder.loadTexts:
    rcftSlotOLOSTRAP.setStatus(
        "current"
    )

rcftSlotOSyncLOSTRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 0, 33)
)
rcftSlotOSyncLOSTRAP.setObjects(
    ("RAISECOM-RCFT-MIB", "rcftSlotOSync")
)
if mibBuilder.loadTexts:
    rcftSlotOSyncLOSTRAP.setStatus(
        "current"
    )

rcftSlotOTransErrorCodeMore10E_3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 0, 34)
)
rcftSlotOTransErrorCodeMore10E_3.setObjects(
    ("RAISECOM-RCFT-MIB", "rcftSlotOTransErrorCode")
)
if mibBuilder.loadTexts:
    rcftSlotOTransErrorCodeMore10E_3.setStatus(
        "current"
    )

rcftSlotOTransErrorCodeMore10E_6 = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 0, 35)
)
rcftSlotOTransErrorCodeMore10E_6.setObjects(
    ("RAISECOM-RCFT-MIB", "rcftSlotOTransErrorCode")
)
if mibBuilder.loadTexts:
    rcftSlotOTransErrorCodeMore10E_6.setStatus(
        "current"
    )

rcftRSlotE1LOSTRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 0, 36)
)
rcftRSlotE1LOSTRAP.setObjects(
    ("RAISECOM-RCFT-MIB", "rcftRSlotE1LOS")
)
if mibBuilder.loadTexts:
    rcftRSlotE1LOSTRAP.setStatus(
        "current"
    )

rcftRSlotOLOSTRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 0, 37)
)
rcftRSlotOLOSTRAP.setObjects(
    ("RAISECOM-RCFT-MIB", "rcftRSlotOLOS")
)
if mibBuilder.loadTexts:
    rcftRSlotOLOSTRAP.setStatus(
        "current"
    )

rcftRSlotOSyncLOSTRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 0, 38)
)
rcftRSlotOSyncLOSTRAP.setObjects(
    ("RAISECOM-RCFT-MIB", "rcftRSlotOSync")
)
if mibBuilder.loadTexts:
    rcftRSlotOSyncLOSTRAP.setStatus(
        "current"
    )

rcftRSlotOTransErrorCodeMore10E_3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 0, 39)
)
rcftRSlotOTransErrorCodeMore10E_3.setObjects(
    ("RAISECOM-RCFT-MIB", "rcftRSlotOTransErrorCode")
)
if mibBuilder.loadTexts:
    rcftRSlotOTransErrorCodeMore10E_3.setStatus(
        "current"
    )

rcftRSlotOTransErrorCodeMore10E_6 = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 0, 40)
)
rcftRSlotOTransErrorCodeMore10E_6.setObjects(
    ("RAISECOM-RCFT-MIB", "rcftRSlotOTransErrorCode")
)
if mibBuilder.loadTexts:
    rcftRSlotOTransErrorCodeMore10E_6.setStatus(
        "current"
    )

rcftSlotE1LOFTRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 0, 41)
)
rcftSlotE1LOFTRAP.setObjects(
    ("RAISECOM-RCFT-MIB", "rcftSlotE1LOF")
)
if mibBuilder.loadTexts:
    rcftSlotE1LOFTRAP.setStatus(
        "current"
    )

rcftSlotE1CRCTRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 0, 42)
)
rcftSlotE1CRCTRAP.setObjects(
    ("RAISECOM-RCFT-MIB", "rcftSlotE1CRC")
)
if mibBuilder.loadTexts:
    rcftSlotE1CRCTRAP.setStatus(
        "current"
    )

rcftSlotSOLinkTRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 0, 43)
)
rcftSlotSOLinkTRAP.setObjects(
    ("RAISECOM-RCFT-MIB", "rcftSlotOLink")
)
if mibBuilder.loadTexts:
    rcftSlotSOLinkTRAP.setStatus(
        "current"
    )

rcftSlotMOLinkTRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 0, 44)
)
rcftSlotMOLinkTRAP.setObjects(
    ("RAISECOM-RCFT-MIB", "rcftSlotELink")
)
if mibBuilder.loadTexts:
    rcftSlotMOLinkTRAP.setStatus(
        "current"
    )

rcftEPort1LinkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 0, 45)
)
rcftEPort1LinkTrap.setObjects(
    ("RAISECOM-RCFT-MIB", "rcftSlotEPort1Link")
)
if mibBuilder.loadTexts:
    rcftEPort1LinkTrap.setStatus(
        "current"
    )

rcftSlotE1AISTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 0, 46)
)
rcftSlotE1AISTrap.setObjects(
    ("RAISECOM-RCFT-MIB", "rcftSlotE1AIS")
)
if mibBuilder.loadTexts:
    rcftSlotE1AISTrap.setStatus(
        "current"
    )

rcftSlotRALMTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 0, 47)
)
rcftSlotRALMTrap.setObjects(
    ("RAISECOM-RCFT-MIB", "rcftSlotRALM")
)
if mibBuilder.loadTexts:
    rcftSlotRALMTrap.setStatus(
        "current"
    )

rcftSlotE1Port2LOSTRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 0, 48)
)
rcftSlotE1Port2LOSTRAP.setObjects(
    ("RAISECOM-RCFT-MIB", "rcftSlotE1Port2LOS")
)
if mibBuilder.loadTexts:
    rcftSlotE1Port2LOSTRAP.setStatus(
        "current"
    )

rcftRSlotE1Port2LOSTRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 0, 49)
)
rcftRSlotE1Port2LOSTRAP.setObjects(
    ("RAISECOM-RCFT-MIB", "rcftRSlotE1Port2LOS")
)
if mibBuilder.loadTexts:
    rcftRSlotE1Port2LOSTRAP.setStatus(
        "current"
    )

rcftRESpeedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 0, 50)
)
rcftRESpeedTrap.setObjects(
    ("RAISECOM-RCFT-MIB", "rcftInterfaceRSpeed")
)
if mibBuilder.loadTexts:
    rcftRESpeedTrap.setStatus(
        "current"
    )

rcftREDuplexTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 0, 51)
)
rcftREDuplexTrap.setObjects(
    ("RAISECOM-RCFT-MIB", "rcftInterfaceRDuplex")
)
if mibBuilder.loadTexts:
    rcftREDuplexTrap.setStatus(
        "current"
    )

rcftInterfaceRLinkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 0, 52)
)
rcftInterfaceRLinkTrap.setObjects(
    ("RAISECOM-RCFT-MIB", "rcftInterfaceRLink")
)
if mibBuilder.loadTexts:
    rcftInterfaceRLinkTrap.setStatus(
        "current"
    )

rcftSlotLALMTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 0, 53)
)
rcftSlotLALMTrap.setObjects(
    ("RAISECOM-RCFT-MIB", "rcftSlotLALM")
)
if mibBuilder.loadTexts:
    rcftSlotLALMTrap.setStatus(
        "current"
    )

rcftStmFiberRxPllUnlckTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 0, 54)
)
rcftStmFiberRxPllUnlckTrap.setObjects(
    ("RAISECOM-RCFT-MIB", "rcftStmFiberRxPllUnlck")
)
if mibBuilder.loadTexts:
    rcftStmFiberRxPllUnlckTrap.setStatus(
        "current"
    )

rcftStmFiberTxClkLosTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 0, 55)
)
rcftStmFiberTxClkLosTrap.setObjects(
    ("RAISECOM-RCFT-MIB", "rcftStmFiberTxClkLos")
)
if mibBuilder.loadTexts:
    rcftStmFiberTxClkLosTrap.setStatus(
        "current"
    )

rcftStmFiberAnalogLosTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 0, 56)
)
rcftStmFiberAnalogLosTrap.setObjects(
    ("RAISECOM-RCFT-MIB", "rcftStmFiberAnalogLos")
)
if mibBuilder.loadTexts:
    rcftStmFiberAnalogLosTrap.setStatus(
        "current"
    )

rcftStmFiberDigitalLosTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 0, 57)
)
rcftStmFiberDigitalLosTrap.setObjects(
    ("RAISECOM-RCFT-MIB", "rcftStmFiberDigitalLos")
)
if mibBuilder.loadTexts:
    rcftStmFiberDigitalLosTrap.setStatus(
        "current"
    )

rcftStmFiberSyncLosTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 0, 58)
)
rcftStmFiberSyncLosTrap.setObjects(
    ("RAISECOM-RCFT-MIB", "rcftStmFiberSyncLos")
)
if mibBuilder.loadTexts:
    rcftStmFiberSyncLosTrap.setStatus(
        "current"
    )

rcftStmBncRxPllUnlckTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 0, 59)
)
rcftStmBncRxPllUnlckTrap.setObjects(
    ("RAISECOM-RCFT-MIB", "rcftStmBncRxPllUnlck")
)
if mibBuilder.loadTexts:
    rcftStmBncRxPllUnlckTrap.setStatus(
        "current"
    )

rcftStmBncTxClkLosTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 0, 60)
)
rcftStmBncTxClkLosTrap.setObjects(
    ("RAISECOM-RCFT-MIB", "rcftStmBncTxClkLos")
)
if mibBuilder.loadTexts:
    rcftStmBncTxClkLosTrap.setStatus(
        "current"
    )

rcftStmBncAnalogLosTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 0, 61)
)
rcftStmBncAnalogLosTrap.setObjects(
    ("RAISECOM-RCFT-MIB", "rcftStmBncAnalogLos")
)
if mibBuilder.loadTexts:
    rcftStmBncAnalogLosTrap.setStatus(
        "current"
    )

rcftStmBncDigitalLosTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 0, 62)
)
rcftStmBncDigitalLosTrap.setObjects(
    ("RAISECOM-RCFT-MIB", "rcftStmBncDigitalLos")
)
if mibBuilder.loadTexts:
    rcftStmBncDigitalLosTrap.setStatus(
        "current"
    )

rcftStmBncSyncLosTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 0, 63)
)
rcftStmBncSyncLosTrap.setObjects(
    ("RAISECOM-RCFT-MIB", "rcftStmBncSyncLos")
)
if mibBuilder.loadTexts:
    rcftStmBncSyncLosTrap.setStatus(
        "current"
    )

rcftInterfaceLOSTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 0, 64)
)
rcftInterfaceLOSTrap.setObjects(
    ("RAISECOM-RCFT-MIB", "rcftInterfaceLOS")
)
if mibBuilder.loadTexts:
    rcftInterfaceLOSTrap.setStatus(
        "current"
    )

rcftInterfaceCVTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 0, 65)
)
rcftInterfaceCVTrap.setObjects(
    ("RAISECOM-RCFT-MIB", "rcftInterfaceCV")
)
if mibBuilder.loadTexts:
    rcftInterfaceCVTrap.setStatus(
        "current"
    )

rcftInterfaceAISTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 0, 66)
)
rcftInterfaceAISTrap.setObjects(
    ("RAISECOM-RCFT-MIB", "rcftInterfaceAIS")
)
if mibBuilder.loadTexts:
    rcftInterfaceAISTrap.setStatus(
        "current"
    )

rcftInterfaceLOFTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 0, 67)
)
rcftInterfaceLOFTrap.setObjects(
    ("RAISECOM-RCFT-MIB", "rcftInterfaceLOF")
)
if mibBuilder.loadTexts:
    rcftInterfaceLOFTrap.setStatus(
        "current"
    )

rcftInterfaceCRCTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 0, 68)
)
rcftInterfaceCRCTrap.setObjects(
    ("RAISECOM-RCFT-MIB", "rcftInterfaceCRC")
)
if mibBuilder.loadTexts:
    rcftInterfaceCRCTrap.setStatus(
        "current"
    )

rcftInterfaceE5Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 0, 69)
)
rcftInterfaceE5Trap.setObjects(
    ("RAISECOM-RCFT-MIB", "rcftInterfaceE5")
)
if mibBuilder.loadTexts:
    rcftInterfaceE5Trap.setStatus(
        "current"
    )

rcftInterfaceRLOSTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 0, 70)
)
rcftInterfaceRLOSTrap.setObjects(
    ("RAISECOM-RCFT-MIB", "rcftInterfaceRLOS")
)
if mibBuilder.loadTexts:
    rcftInterfaceRLOSTrap.setStatus(
        "current"
    )

rcftInterfaceRCVTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 0, 71)
)
rcftInterfaceRCVTrap.setObjects(
    ("RAISECOM-RCFT-MIB", "rcftInterfaceRCV")
)
if mibBuilder.loadTexts:
    rcftInterfaceRCVTrap.setStatus(
        "current"
    )

rcftInterfaceRAISTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 0, 72)
)
rcftInterfaceRAISTrap.setObjects(
    ("RAISECOM-RCFT-MIB", "rcftInterfaceRAIS")
)
if mibBuilder.loadTexts:
    rcftInterfaceRAISTrap.setStatus(
        "current"
    )

rcftInterfaceRLOFTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 0, 73)
)
rcftInterfaceRLOFTrap.setObjects(
    ("RAISECOM-RCFT-MIB", "rcftInterfaceRLOF")
)
if mibBuilder.loadTexts:
    rcftInterfaceRLOFTrap.setStatus(
        "current"
    )

rcftInterfaceRCRCTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 0, 74)
)
rcftInterfaceRCRCTrap.setObjects(
    ("RAISECOM-RCFT-MIB", "rcftInterfaceRCRC")
)
if mibBuilder.loadTexts:
    rcftInterfaceRCRCTrap.setStatus(
        "current"
    )

rcftInterfaceLinkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 0, 75)
)
rcftInterfaceLinkTrap.setObjects(
    ("RAISECOM-RCFT-MIB", "rcftInterfaceLink")
)
if mibBuilder.loadTexts:
    rcftInterfaceLinkTrap.setStatus(
        "current"
    )

rcftRSlotE1AISTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 0, 76)
)
rcftRSlotE1AISTrap.setObjects(
    ("RAISECOM-RCFT-MIB", "rcftRSlotE1PortAlarm")
)
if mibBuilder.loadTexts:
    rcftRSlotE1AISTrap.setStatus(
        "current"
    )

rcftRSlotE1LOFTRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 0, 77)
)
rcftRSlotE1LOFTRAP.setObjects(
    ("RAISECOM-RCFT-MIB", "rcftRSlotE1PortAlarm")
)
if mibBuilder.loadTexts:
    rcftRSlotE1LOFTRAP.setStatus(
        "current"
    )

rcftRSlotE1CRCTRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 0, 78)
)
rcftRSlotE1CRCTRAP.setObjects(
    ("RAISECOM-RCFT-MIB", "rcftRSlotE1PortAlarm")
)
if mibBuilder.loadTexts:
    rcftRSlotE1CRCTRAP.setStatus(
        "current"
    )

rcftRSlotRALMTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 0, 79)
)
rcftRSlotRALMTrap.setObjects(
    ("RAISECOM-RCFT-MIB", "rcftRSlotE1PortAlarm")
)
if mibBuilder.loadTexts:
    rcftRSlotRALMTrap.setStatus(
        "current"
    )

rcftRSlotLALMTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 0, 80)
)
rcftRSlotLALMTrap.setObjects(
    ("RAISECOM-RCFT-MIB", "rcftV35E1PortExtendStatus")
)
if mibBuilder.loadTexts:
    rcftRSlotLALMTrap.setStatus(
        "current"
    )

cwdmTransmitLOLTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 0, 81)
)
cwdmTransmitLOLTrap.setObjects(
    ("RAISECOM-RCFT-MIB", "rcftSlotWorkStatus")
)
if mibBuilder.loadTexts:
    cwdmTransmitLOLTrap.setStatus(
        "current"
    )

cwdmTransmitLOATrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 0, 82)
)
cwdmTransmitLOATrap.setObjects(
    ("RAISECOM-RCFT-MIB", "rcftSlotWorkStatus")
)
if mibBuilder.loadTexts:
    cwdmTransmitLOATrap.setStatus(
        "current"
    )

cwdmReceiveLOLTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 0, 83)
)
cwdmReceiveLOLTrap.setObjects(
    ("RAISECOM-RCFT-MIB", "rcftSlotWorkStatus")
)
if mibBuilder.loadTexts:
    cwdmReceiveLOLTrap.setStatus(
        "current"
    )

cwdmReceiveLOATrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 0, 84)
)
cwdmReceiveLOATrap.setObjects(
    ("RAISECOM-RCFT-MIB", "rcftSlotWorkStatus")
)
if mibBuilder.loadTexts:
    cwdmReceiveLOATrap.setStatus(
        "current"
    )

cwdmCWDMLaserTxfaultTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 0, 85)
)
cwdmCWDMLaserTxfaultTrap.setObjects(
    ("RAISECOM-RCFT-MIB", "cwdmCWDMWorkStatus")
)
if mibBuilder.loadTexts:
    cwdmCWDMLaserTxfaultTrap.setStatus(
        "current"
    )

cwdmCWDMInputSignalLosTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 0, 86)
)
cwdmCWDMInputSignalLosTrap.setObjects(
    ("RAISECOM-RCFT-MIB", "cwdmCWDMWorkStatus")
)
if mibBuilder.loadTexts:
    cwdmCWDMInputSignalLosTrap.setStatus(
        "current"
    )

cwdmCWDMModuleExistTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 0, 87)
)
cwdmCWDMModuleExistTrap.setObjects(
    ("RAISECOM-RCFT-MIB", "cwdmCWDMWorkStatus")
)
if mibBuilder.loadTexts:
    cwdmCWDMModuleExistTrap.setStatus(
        "current"
    )

cwdmClientLaserTxfaultTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 0, 88)
)
cwdmClientLaserTxfaultTrap.setObjects(
    ("RAISECOM-RCFT-MIB", "cwdmClientWorkStatus")
)
if mibBuilder.loadTexts:
    cwdmClientLaserTxfaultTrap.setStatus(
        "current"
    )

cwdmClientInputSignalLosTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 0, 89)
)
cwdmClientInputSignalLosTrap.setObjects(
    ("RAISECOM-RCFT-MIB", "cwdmClientWorkStatus")
)
if mibBuilder.loadTexts:
    cwdmClientInputSignalLosTrap.setStatus(
        "current"
    )

cwdmClientModuleExistTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 0, 90)
)
cwdmClientModuleExistTrap.setObjects(
    ("RAISECOM-RCFT-MIB", "cwdmClientWorkStatus")
)
if mibBuilder.loadTexts:
    cwdmClientModuleExistTrap.setStatus(
        "current"
    )

rcftRSlotORLnkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 0, 91)
)
rcftRSlotORLnkTrap.setObjects(
    ("RAISECOM-RCFT-MIB", "rcftRSlotORLnk")
)
if mibBuilder.loadTexts:
    rcftRSlotORLnkTrap.setStatus(
        "current"
    )

rcftRSlotOTLnkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 0, 92)
)
rcftRSlotOTLnkTrap.setObjects(
    ("RAISECOM-RCFT-MIB", "rcftRSlotOTLnk")
)
if mibBuilder.loadTexts:
    rcftRSlotOTLnkTrap.setStatus(
        "current"
    )

cwdmSpeedUnmatchedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 0, 93)
)
cwdmSpeedUnmatchedTrap.setObjects(
    ("RAISECOM-RCFT-MIB", "rcftSlotWorkStatus")
)
if mibBuilder.loadTexts:
    cwdmSpeedUnmatchedTrap.setStatus(
        "current"
    )

remotecwdmCWDMLaserTxfaultTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 0, 94)
)
remotecwdmCWDMLaserTxfaultTrap.setObjects(
    ("RAISECOM-RCFT-MIB", "cwdmCWDMWorkStatus")
)
if mibBuilder.loadTexts:
    remotecwdmCWDMLaserTxfaultTrap.setStatus(
        "current"
    )

remotecwdmCWDMInputSignalLosTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 0, 95)
)
remotecwdmCWDMInputSignalLosTrap.setObjects(
    ("RAISECOM-RCFT-MIB", "cwdmCWDMWorkStatus")
)
if mibBuilder.loadTexts:
    remotecwdmCWDMInputSignalLosTrap.setStatus(
        "current"
    )

remotecwdmCWDMModuleExistTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 0, 96)
)
remotecwdmCWDMModuleExistTrap.setObjects(
    ("RAISECOM-RCFT-MIB", "cwdmCWDMWorkStatus")
)
if mibBuilder.loadTexts:
    remotecwdmCWDMModuleExistTrap.setStatus(
        "current"
    )

rcftSlotE1LOMFTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 0, 97)
)
rcftSlotE1LOMFTrap.setObjects(
    ("RAISECOM-RCFT-MIB", "rcftSlotE1PortAlarm")
)
if mibBuilder.loadTexts:
    rcftSlotE1LOMFTrap.setStatus(
        "current"
    )

rcftRSlotE1LOMFTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 0, 98)
)
rcftRSlotE1LOMFTrap.setObjects(
    ("RAISECOM-RCFT-MIB", "rcftRSlotE1PortAlarm")
)
if mibBuilder.loadTexts:
    rcftRSlotE1LOMFTrap.setStatus(
        "current"
    )

rcftSlotE1CVTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 0, 99)
)
rcftSlotE1CVTrap.setObjects(
    ("RAISECOM-RCFT-MIB", "rcftSlotE1PortAlarm")
)
if mibBuilder.loadTexts:
    rcftSlotE1CVTrap.setStatus(
        "current"
    )

rcftRSlotE1CVTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 0, 100)
)
rcftRSlotE1CVTrap.setObjects(
    ("RAISECOM-RCFT-MIB", "rcftRSlotE1PortAlarm")
)
if mibBuilder.loadTexts:
    rcftRSlotE1CVTrap.setStatus(
        "current"
    )

rcftSlotSHDSLLosTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 0, 101)
)
rcftSlotSHDSLLosTrap.setObjects(
    ("RAISECOM-RCFT-MIB", "rcftFxWorkStatus")
)
if mibBuilder.loadTexts:
    rcftSlotSHDSLLosTrap.setStatus(
        "current"
    )

rcftSlotSHDSLLOFTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 0, 102)
)
rcftSlotSHDSLLOFTrap.setObjects(
    ("RAISECOM-RCFT-MIB", "rcftFxWorkStatus")
)
if mibBuilder.loadTexts:
    rcftSlotSHDSLLOFTrap.setStatus(
        "current"
    )

rcftRSlotSHDSLLosTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 0, 103)
)
rcftRSlotSHDSLLosTrap.setObjects(
    ("RAISECOM-RCFT-MIB", "rcftFxWorkStatus")
)
if mibBuilder.loadTexts:
    rcftRSlotSHDSLLosTrap.setStatus(
        "current"
    )

rcftRSlotSHDSLLOFTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 0, 104)
)
rcftRSlotSHDSLLOFTrap.setObjects(
    ("RAISECOM-RCFT-MIB", "rcftFxWorkStatus")
)
if mibBuilder.loadTexts:
    rcftRSlotSHDSLLOFTrap.setStatus(
        "current"
    )

rcftSlotSHDSLLinkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 0, 105)
)
rcftSlotSHDSLLinkTrap.setObjects(
    ("RAISECOM-RCFT-MIB", "rcftSlotOLink")
)
if mibBuilder.loadTexts:
    rcftSlotSHDSLLinkTrap.setStatus(
        "current"
    )

rcftRSlotSHDSLLinkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 0, 106)
)
rcftRSlotSHDSLLinkTrap.setObjects(
    ("RAISECOM-RCFT-MIB", "rcftRSlotOLink")
)
if mibBuilder.loadTexts:
    rcftRSlotSHDSLLinkTrap.setStatus(
        "current"
    )

rcftClientOLinkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 0, 107)
)
rcftClientOLinkTrap.setObjects(
    ("RAISECOM-RCFT-MIB", "rcftFxWorkStatus")
)
if mibBuilder.loadTexts:
    rcftClientOLinkTrap.setStatus(
        "current"
    )

rcftClientOSDTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 0, 108)
)
rcftClientOSDTrap.setObjects(
    ("RAISECOM-RCFT-MIB", "rcftFxWorkStatus")
)
if mibBuilder.loadTexts:
    rcftClientOSDTrap.setStatus(
        "current"
    )

rcftRClientOLinkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 0, 109)
)
rcftRClientOLinkTrap.setObjects(
    ("RAISECOM-RCFT-MIB", "rcftFxWorkStatus")
)
if mibBuilder.loadTexts:
    rcftRClientOLinkTrap.setStatus(
        "current"
    )

rcftRClientOSDTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 0, 110)
)
rcftRClientOSDTrap.setObjects(
    ("RAISECOM-RCFT-MIB", "rcftFxWorkStatus")
)
if mibBuilder.loadTexts:
    rcftRClientOSDTrap.setStatus(
        "current"
    )

cwdmPrimaryCWDMInputSignalLosTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 0, 111)
)
cwdmPrimaryCWDMInputSignalLosTrap.setObjects(
    ("RAISECOM-RCFT-MIB", "cwdmCWDMWorkStatus")
)
if mibBuilder.loadTexts:
    cwdmPrimaryCWDMInputSignalLosTrap.setStatus(
        "current"
    )

cwdmPrimaryCWDMModuleExistTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 0, 112)
)
cwdmPrimaryCWDMModuleExistTrap.setObjects(
    ("RAISECOM-RCFT-MIB", "cwdmCWDMWorkStatus")
)
if mibBuilder.loadTexts:
    cwdmPrimaryCWDMModuleExistTrap.setStatus(
        "current"
    )

rcftSlotPSChannelOTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 0, 113)
)
rcftSlotPSChannelOTrap.setObjects(
    ("RAISECOM-RCFT-MIB", "rcftSlotOpticalDeviceStatus")
)
if mibBuilder.loadTexts:
    rcftSlotPSChannelOTrap.setStatus(
        "current"
    )

rcftInterfaceRELinkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 0, 114)
)
rcftInterfaceRELinkTrap.setObjects(
    ("RAISECOM-RCFT-MIB", "rcftInterfaceRLink")
)
if mibBuilder.loadTexts:
    rcftInterfaceRELinkTrap.setStatus(
        "current"
    )

cwdmSecondaryReceiveLOLTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 0, 115)
)
cwdmSecondaryReceiveLOLTrap.setObjects(
    ("RAISECOM-RCFT-MIB", "rcftSlotWorkStatus")
)
if mibBuilder.loadTexts:
    cwdmSecondaryReceiveLOLTrap.setStatus(
        "current"
    )

cwdmSecondaryCWDMInputSignalLosTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 0, 116)
)
cwdmSecondaryCWDMInputSignalLosTrap.setObjects(
    ("RAISECOM-RCFT-MIB", "cwdmCWDMWorkStatus")
)
if mibBuilder.loadTexts:
    cwdmSecondaryCWDMInputSignalLosTrap.setStatus(
        "current"
    )

cwdmSecondaryCWDMModuleExistTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 0, 117)
)
cwdmSecondaryCWDMModuleExistTrap.setObjects(
    ("RAISECOM-RCFT-MIB", "cwdmCWDMWorkStatus")
)
if mibBuilder.loadTexts:
    cwdmSecondaryCWDMModuleExistTrap.setStatus(
        "current"
    )

rcftInterfaceLToRLOSTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 0, 118)
)
rcftInterfaceLToRLOSTrap.setObjects(
    ("RAISECOM-RCFT-MIB", "rcftInterfaceRLOS")
)
if mibBuilder.loadTexts:
    rcftInterfaceLToRLOSTrap.setStatus(
        "current"
    )

rcftInterfaceLtoRAISTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 0, 119)
)
rcftInterfaceLtoRAISTrap.setObjects(
    ("RAISECOM-RCFT-MIB", "rcftInterfaceRAIS")
)
if mibBuilder.loadTexts:
    rcftInterfaceLtoRAISTrap.setStatus(
        "current"
    )

rcftInterfaceLtoRLOFTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 0, 120)
)
rcftInterfaceLtoRLOFTrap.setObjects(
    ("RAISECOM-RCFT-MIB", "rcftInterfaceRLOF")
)
if mibBuilder.loadTexts:
    rcftInterfaceLtoRLOFTrap.setStatus(
        "current"
    )

rcftInterfaceLtoRCRCTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 0, 121)
)
rcftInterfaceLtoRCRCTrap.setObjects(
    ("RAISECOM-RCFT-MIB", "rcftInterfaceRCRC")
)
if mibBuilder.loadTexts:
    rcftInterfaceLtoRCRCTrap.setStatus(
        "current"
    )

rcftSlotRemotePowerDownTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 0, 122)
)
rcftSlotRemotePowerDownTrap.setObjects(
    ("RAISECOM-RCFT-MIB", "rcftSlotLineStatus")
)
if mibBuilder.loadTexts:
    rcftSlotRemotePowerDownTrap.setStatus(
        "current"
    )

rcftSlotVideoLosTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 0, 123)
)
rcftSlotVideoLosTrap.setObjects(
    ("RAISECOM-RCFT-MIB", "rcftFxWorkStatus")
)
if mibBuilder.loadTexts:
    rcftSlotVideoLosTrap.setStatus(
        "current"
    )

rcftRSlotVideoLosTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 0, 124)
)
rcftRSlotVideoLosTrap.setObjects(
    ("RAISECOM-RCFT-MIB", "rcftFxWorkStatus")
)
if mibBuilder.loadTexts:
    rcftRSlotVideoLosTrap.setStatus(
        "current"
    )

rcftSlotLocalToRemoteE1CRCTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 0, 125)
)
rcftSlotLocalToRemoteE1CRCTrap.setObjects(
    ("RAISECOM-RCFT-MIB", "rcftSlotE1PortAlarm")
)
if mibBuilder.loadTexts:
    rcftSlotLocalToRemoteE1CRCTrap.setStatus(
        "current"
    )

rcftSlotLocalToRemoteE1LOFTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 0, 126)
)
rcftSlotLocalToRemoteE1LOFTrap.setObjects(
    ("RAISECOM-RCFT-MIB", "rcftSlotE1PortAlarm")
)
if mibBuilder.loadTexts:
    rcftSlotLocalToRemoteE1LOFTrap.setStatus(
        "current"
    )

rcftSlotLocalToRemoteE1AISTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 0, 127)
)
rcftSlotLocalToRemoteE1AISTrap.setObjects(
    ("RAISECOM-RCFT-MIB", "rcftSlotE1PortAlarm")
)
if mibBuilder.loadTexts:
    rcftSlotLocalToRemoteE1AISTrap.setStatus(
        "current"
    )

rcftSlotLocalToRemoteE1LOSTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 0, 128)
)
rcftSlotLocalToRemoteE1LOSTrap.setObjects(
    ("RAISECOM-RCFT-MIB", "rcftSlotE1PortAlarm")
)
if mibBuilder.loadTexts:
    rcftSlotLocalToRemoteE1LOSTrap.setStatus(
        "current"
    )

cwdmPrimaryReceiveLOLTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 0, 129)
)
cwdmPrimaryReceiveLOLTrap.setObjects(
    ("RAISECOM-RCFT-MIB", "rcftSlotWorkStatus")
)
if mibBuilder.loadTexts:
    cwdmPrimaryReceiveLOLTrap.setStatus(
        "current"
    )

rcftClientPortLOLTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 0, 130)
)
rcftClientPortLOLTrap.setObjects(
    ("RAISECOM-RCFT-MIB", "rcftSlotWorkStatus")
)
if mibBuilder.loadTexts:
    rcftClientPortLOLTrap.setStatus(
        "current"
    )

rcftLinePortLOLTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 0, 131)
)
rcftLinePortLOLTrap.setObjects(
    ("RAISECOM-RCFT-MIB", "rcftSlotWorkStatus")
)
if mibBuilder.loadTexts:
    rcftLinePortLOLTrap.setStatus(
        "current"
    )

rcftSlotSPChannelOTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 0, 132)
)
rcftSlotSPChannelOTrap.setObjects(
    ("RAISECOM-RCFT-MIB", "rcftSlotOpticalDeviceStatus")
)
if mibBuilder.loadTexts:
    rcftSlotSPChannelOTrap.setStatus(
        "current"
    )

rcftSaveConfigFileFinishedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 0, 133)
)
if mibBuilder.loadTexts:
    rcftSaveConfigFileFinishedTrap.setStatus(
        "current"
    )

rcftRSlotLinePortLOLTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 0, 134)
)
rcftRSlotLinePortLOLTrap.setObjects(
    ("RAISECOM-RCFT-MIB", "rcftSlotWorkStatus")
)
if mibBuilder.loadTexts:
    rcftRSlotLinePortLOLTrap.setStatus(
        "current"
    )

rcftSlotSFPModuleTempHighTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 0, 135)
)
rcftSlotSFPModuleTempHighTrap.setObjects(
    ("RAISECOM-RCFT-MIB", "rcftSlotSFPDiagnosticsInfo")
)
if mibBuilder.loadTexts:
    rcftSlotSFPModuleTempHighTrap.setStatus(
        "current"
    )

rcftSlotSFPModuleTempLowTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 0, 136)
)
rcftSlotSFPModuleTempLowTrap.setObjects(
    ("RAISECOM-RCFT-MIB", "rcftSlotSFPDiagnosticsInfo")
)
if mibBuilder.loadTexts:
    rcftSlotSFPModuleTempLowTrap.setStatus(
        "current"
    )

rcftSlotSFPModuleVoltageHighTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 0, 137)
)
rcftSlotSFPModuleVoltageHighTrap.setObjects(
    ("RAISECOM-RCFT-MIB", "rcftSlotSFPDiagnosticsInfo")
)
if mibBuilder.loadTexts:
    rcftSlotSFPModuleVoltageHighTrap.setStatus(
        "current"
    )

rcftSlotSFPModuleVoltageLowTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 0, 138)
)
rcftSlotSFPModuleVoltageLowTrap.setObjects(
    ("RAISECOM-RCFT-MIB", "rcftSlotSFPDiagnosticsInfo")
)
if mibBuilder.loadTexts:
    rcftSlotSFPModuleVoltageLowTrap.setStatus(
        "current"
    )

rcftSlotSFPModuleOffsetCurrHighTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 0, 139)
)
rcftSlotSFPModuleOffsetCurrHighTrap.setObjects(
    ("RAISECOM-RCFT-MIB", "rcftSlotSFPDiagnosticsInfo")
)
if mibBuilder.loadTexts:
    rcftSlotSFPModuleOffsetCurrHighTrap.setStatus(
        "current"
    )

rcftSlotSFPModuleOffsetCurrLowTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 0, 140)
)
rcftSlotSFPModuleOffsetCurrLowTrap.setObjects(
    ("RAISECOM-RCFT-MIB", "rcftSlotSFPDiagnosticsInfo")
)
if mibBuilder.loadTexts:
    rcftSlotSFPModuleOffsetCurrLowTrap.setStatus(
        "current"
    )

rcftSlotSFPModuleSendPowerHighTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 0, 141)
)
rcftSlotSFPModuleSendPowerHighTrap.setObjects(
    ("RAISECOM-RCFT-MIB", "rcftSlotSFPDiagnosticsInfo")
)
if mibBuilder.loadTexts:
    rcftSlotSFPModuleSendPowerHighTrap.setStatus(
        "current"
    )

rcftSlotSFPModuleSendPowerLowTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 0, 142)
)
rcftSlotSFPModuleSendPowerLowTrap.setObjects(
    ("RAISECOM-RCFT-MIB", "rcftSlotSFPDiagnosticsInfo")
)
if mibBuilder.loadTexts:
    rcftSlotSFPModuleSendPowerLowTrap.setStatus(
        "current"
    )

rcftSlotSFPModuleRecvPowerHighTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 0, 143)
)
rcftSlotSFPModuleRecvPowerHighTrap.setObjects(
    ("RAISECOM-RCFT-MIB", "rcftSlotSFPDiagnosticsInfo")
)
if mibBuilder.loadTexts:
    rcftSlotSFPModuleRecvPowerHighTrap.setStatus(
        "current"
    )

rcftSlotSFPModuleRecvPowerLowTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 0, 144)
)
rcftSlotSFPModuleRecvPowerLowTrap.setObjects(
    ("RAISECOM-RCFT-MIB", "rcftSlotSFPDiagnosticsInfo")
)
if mibBuilder.loadTexts:
    rcftSlotSFPModuleRecvPowerLowTrap.setStatus(
        "current"
    )

rcftRSlotSFPModuleTempHighTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 0, 145)
)
rcftRSlotSFPModuleTempHighTrap.setObjects(
    ("RAISECOM-RCFT-MIB", "rcftRSlotSFPDiagnosticsInfo")
)
if mibBuilder.loadTexts:
    rcftRSlotSFPModuleTempHighTrap.setStatus(
        "current"
    )

rcftRSlotSFPModuleTempLowTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 0, 146)
)
rcftRSlotSFPModuleTempLowTrap.setObjects(
    ("RAISECOM-RCFT-MIB", "rcftRSlotSFPDiagnosticsInfo")
)
if mibBuilder.loadTexts:
    rcftRSlotSFPModuleTempLowTrap.setStatus(
        "current"
    )

rcftRSlotSFPModuleVoltageHighTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 0, 147)
)
rcftRSlotSFPModuleVoltageHighTrap.setObjects(
    ("RAISECOM-RCFT-MIB", "rcftRSlotSFPDiagnosticsInfo")
)
if mibBuilder.loadTexts:
    rcftRSlotSFPModuleVoltageHighTrap.setStatus(
        "current"
    )

rcftRSlotSFPModuleVoltageLowTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 0, 148)
)
rcftRSlotSFPModuleVoltageLowTrap.setObjects(
    ("RAISECOM-RCFT-MIB", "rcftRSlotSFPDiagnosticsInfo")
)
if mibBuilder.loadTexts:
    rcftRSlotSFPModuleVoltageLowTrap.setStatus(
        "current"
    )

rcftRSlotSFPModuleOffsetCurrHighTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 0, 149)
)
rcftRSlotSFPModuleOffsetCurrHighTrap.setObjects(
    ("RAISECOM-RCFT-MIB", "rcftRSlotSFPDiagnosticsInfo")
)
if mibBuilder.loadTexts:
    rcftRSlotSFPModuleOffsetCurrHighTrap.setStatus(
        "current"
    )

rcftRSlotSFPModuleOffsetCurrLowTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 0, 150)
)
rcftRSlotSFPModuleOffsetCurrLowTrap.setObjects(
    ("RAISECOM-RCFT-MIB", "rcftRSlotSFPDiagnosticsInfo")
)
if mibBuilder.loadTexts:
    rcftRSlotSFPModuleOffsetCurrLowTrap.setStatus(
        "current"
    )

rcftRSlotSFPModuleSendPowerHighTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 0, 151)
)
rcftRSlotSFPModuleSendPowerHighTrap.setObjects(
    ("RAISECOM-RCFT-MIB", "rcftRSlotSFPDiagnosticsInfo")
)
if mibBuilder.loadTexts:
    rcftRSlotSFPModuleSendPowerHighTrap.setStatus(
        "current"
    )

rcftRSlotSFPModuleSendPowerLowTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 0, 152)
)
rcftRSlotSFPModuleSendPowerLowTrap.setObjects(
    ("RAISECOM-RCFT-MIB", "rcftRSlotSFPDiagnosticsInfo")
)
if mibBuilder.loadTexts:
    rcftRSlotSFPModuleSendPowerLowTrap.setStatus(
        "current"
    )

rcftRSlotSFPModuleRecvPowerHighTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 0, 153)
)
rcftRSlotSFPModuleRecvPowerHighTrap.setObjects(
    ("RAISECOM-RCFT-MIB", "rcftRSlotSFPDiagnosticsInfo")
)
if mibBuilder.loadTexts:
    rcftRSlotSFPModuleRecvPowerHighTrap.setStatus(
        "current"
    )

rcftRSlotSFPModuleRecvPowerLowTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 0, 154)
)
rcftRSlotSFPModuleRecvPowerLowTrap.setObjects(
    ("RAISECOM-RCFT-MIB", "rcftRSlotSFPDiagnosticsInfo")
)
if mibBuilder.loadTexts:
    rcftRSlotSFPModuleRecvPowerLowTrap.setStatus(
        "current"
    )

rcftSlotTempHighLimitTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 0, 155)
)
rcftSlotTempHighLimitTrap.setObjects(
    ("RAISECOM-RCFT-MIB", "rcftSlotTempHighLimit")
)
if mibBuilder.loadTexts:
    rcftSlotTempHighLimitTrap.setStatus(
        "current"
    )

rcftSlotTempLowLimitTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 0, 156)
)
rcftSlotTempLowLimitTrap.setObjects(
    ("RAISECOM-RCFT-MIB", "rcftSlotTempLowLimit")
)
if mibBuilder.loadTexts:
    rcftSlotTempLowLimitTrap.setStatus(
        "current"
    )

rcftSlotHumidityHighLimitTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 0, 157)
)
rcftSlotHumidityHighLimitTrap.setObjects(
    ("RAISECOM-RCFT-MIB", "rcftSlotHumidityHighLimit")
)
if mibBuilder.loadTexts:
    rcftSlotHumidityHighLimitTrap.setStatus(
        "current"
    )

rcftSlotHumidityLowLimitTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 0, 158)
)
rcftSlotHumidityLowLimitTrap.setObjects(
    ("RAISECOM-RCFT-MIB", "rcftSlotHumidityLowLimit")
)
if mibBuilder.loadTexts:
    rcftSlotHumidityLowLimitTrap.setStatus(
        "current"
    )

rcftSlotPSChannelTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 0, 159)
)
rcftSlotPSChannelTrap.setObjects(
    ("RAISECOM-RCFT-MIB", "rcftSlotOpticalDeviceStatus")
)
if mibBuilder.loadTexts:
    rcftSlotPSChannelTrap.setStatus(
        "current"
    )

rcftSlotSPChannelTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 0, 160)
)
rcftSlotSPChannelTrap.setObjects(
    ("RAISECOM-RCFT-MIB", "rcftSlotOpticalDeviceStatus")
)
if mibBuilder.loadTexts:
    rcftSlotSPChannelTrap.setStatus(
        "current"
    )

rcftSlotE1TransErrorCodeMore10E_3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 0, 161)
)
rcftSlotE1TransErrorCodeMore10E_3.setObjects(
    ("RAISECOM-RCFT-MIB", "rcftSlotOTransErrorCode")
)
if mibBuilder.loadTexts:
    rcftSlotE1TransErrorCodeMore10E_3.setStatus(
        "current"
    )

rcftSlotE1TransErrorCodeMore10E_6 = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 0, 162)
)
rcftSlotE1TransErrorCodeMore10E_6.setObjects(
    ("RAISECOM-RCFT-MIB", "rcftSlotOTransErrorCode")
)
if mibBuilder.loadTexts:
    rcftSlotE1TransErrorCodeMore10E_6.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RAISECOM-RCFT-MIB",
    **{"raiseCom": raiseCom,
       "rc002": rc002,
       "rcftTraps": rcftTraps,
       "rcft5VPowerTrap": rcft5VPowerTrap,
       "rcft12VPowerTrap": rcft12VPowerTrap,
       "rcftFanTrap": rcftFanTrap,
       "rcftTmptTrap": rcftTmptTrap,
       "rcftChassisTrap": rcftChassisTrap,
       "rcftELinkTrap": rcftELinkTrap,
       "rcftRELinkTrap": rcftRELinkTrap,
       "rcftOLinkTrap": rcftOLinkTrap,
       "rcftORLnkTrap": rcftORLnkTrap,
       "rcftOTLnkTrap": rcftOTLnkTrap,
       "rcftROLinkTrap": rcftROLinkTrap,
       "rcftESpeedTrap": rcftESpeedTrap,
       "rcftSlotTrap": rcftSlotTrap,
       "rcftBackplaneLossTrap": rcftBackplaneLossTrap,
       "rcftVOLimitTrap": rcftVOLimitTrap,
       "rcftVBLimitTrap": rcftVBLimitTrap,
       "rcftRVOLimitTrap": rcftRVOLimitTrap,
       "rcftRVBLimitTrap": rcftRVBLimitTrap,
       "rcftOSendPowerTrap": rcftOSendPowerTrap,
       "rcftROSendPowerTrap": rcftROSendPowerTrap,
       "rcftOReceSenTrap": rcftOReceSenTrap,
       "rcftROReceSenTrap": rcftROReceSenTrap,
       "rcftOLaserTrap": rcftOLaserTrap,
       "rcftROLaserTrap": rcftROLaserTrap,
       "rcftOSDTrap": rcftOSDTrap,
       "rcftROSDTrap": rcftROSDTrap,
       "rcftRSlotChassisTmptTrap": rcftRSlotChassisTmptTrap,
       "rcftRSlotFault": rcftRSlotFault,
       "rcftSlotFault": rcftSlotFault,
       "rcftRSlotExistNotify": rcftRSlotExistNotify,
       "rcftSlotE1LOSTRAP": rcftSlotE1LOSTRAP,
       "rcftSlotOLOSTRAP": rcftSlotOLOSTRAP,
       "rcftSlotOSyncLOSTRAP": rcftSlotOSyncLOSTRAP,
       "rcftSlotOTransErrorCodeMore10E-3": rcftSlotOTransErrorCodeMore10E_3,
       "rcftSlotOTransErrorCodeMore10E-6": rcftSlotOTransErrorCodeMore10E_6,
       "rcftRSlotE1LOSTRAP": rcftRSlotE1LOSTRAP,
       "rcftRSlotOLOSTRAP": rcftRSlotOLOSTRAP,
       "rcftRSlotOSyncLOSTRAP": rcftRSlotOSyncLOSTRAP,
       "rcftRSlotOTransErrorCodeMore10E-3": rcftRSlotOTransErrorCodeMore10E_3,
       "rcftRSlotOTransErrorCodeMore10E-6": rcftRSlotOTransErrorCodeMore10E_6,
       "rcftSlotE1LOFTRAP": rcftSlotE1LOFTRAP,
       "rcftSlotE1CRCTRAP": rcftSlotE1CRCTRAP,
       "rcftSlotSOLinkTRAP": rcftSlotSOLinkTRAP,
       "rcftSlotMOLinkTRAP": rcftSlotMOLinkTRAP,
       "rcftEPort1LinkTrap": rcftEPort1LinkTrap,
       "rcftSlotE1AISTrap": rcftSlotE1AISTrap,
       "rcftSlotRALMTrap": rcftSlotRALMTrap,
       "rcftSlotE1Port2LOSTRAP": rcftSlotE1Port2LOSTRAP,
       "rcftRSlotE1Port2LOSTRAP": rcftRSlotE1Port2LOSTRAP,
       "rcftRESpeedTrap": rcftRESpeedTrap,
       "rcftREDuplexTrap": rcftREDuplexTrap,
       "rcftInterfaceRLinkTrap": rcftInterfaceRLinkTrap,
       "rcftSlotLALMTrap": rcftSlotLALMTrap,
       "rcftStmFiberRxPllUnlckTrap": rcftStmFiberRxPllUnlckTrap,
       "rcftStmFiberTxClkLosTrap": rcftStmFiberTxClkLosTrap,
       "rcftStmFiberAnalogLosTrap": rcftStmFiberAnalogLosTrap,
       "rcftStmFiberDigitalLosTrap": rcftStmFiberDigitalLosTrap,
       "rcftStmFiberSyncLosTrap": rcftStmFiberSyncLosTrap,
       "rcftStmBncRxPllUnlckTrap": rcftStmBncRxPllUnlckTrap,
       "rcftStmBncTxClkLosTrap": rcftStmBncTxClkLosTrap,
       "rcftStmBncAnalogLosTrap": rcftStmBncAnalogLosTrap,
       "rcftStmBncDigitalLosTrap": rcftStmBncDigitalLosTrap,
       "rcftStmBncSyncLosTrap": rcftStmBncSyncLosTrap,
       "rcftInterfaceLOSTrap": rcftInterfaceLOSTrap,
       "rcftInterfaceCVTrap": rcftInterfaceCVTrap,
       "rcftInterfaceAISTrap": rcftInterfaceAISTrap,
       "rcftInterfaceLOFTrap": rcftInterfaceLOFTrap,
       "rcftInterfaceCRCTrap": rcftInterfaceCRCTrap,
       "rcftInterfaceE5Trap": rcftInterfaceE5Trap,
       "rcftInterfaceRLOSTrap": rcftInterfaceRLOSTrap,
       "rcftInterfaceRCVTrap": rcftInterfaceRCVTrap,
       "rcftInterfaceRAISTrap": rcftInterfaceRAISTrap,
       "rcftInterfaceRLOFTrap": rcftInterfaceRLOFTrap,
       "rcftInterfaceRCRCTrap": rcftInterfaceRCRCTrap,
       "rcftInterfaceLinkTrap": rcftInterfaceLinkTrap,
       "rcftRSlotE1AISTrap": rcftRSlotE1AISTrap,
       "rcftRSlotE1LOFTRAP": rcftRSlotE1LOFTRAP,
       "rcftRSlotE1CRCTRAP": rcftRSlotE1CRCTRAP,
       "rcftRSlotRALMTrap": rcftRSlotRALMTrap,
       "rcftRSlotLALMTrap": rcftRSlotLALMTrap,
       "cwdmTransmitLOLTrap": cwdmTransmitLOLTrap,
       "cwdmTransmitLOATrap": cwdmTransmitLOATrap,
       "cwdmReceiveLOLTrap": cwdmReceiveLOLTrap,
       "cwdmReceiveLOATrap": cwdmReceiveLOATrap,
       "cwdmCWDMLaserTxfaultTrap": cwdmCWDMLaserTxfaultTrap,
       "cwdmCWDMInputSignalLosTrap": cwdmCWDMInputSignalLosTrap,
       "cwdmCWDMModuleExistTrap": cwdmCWDMModuleExistTrap,
       "cwdmClientLaserTxfaultTrap": cwdmClientLaserTxfaultTrap,
       "cwdmClientInputSignalLosTrap": cwdmClientInputSignalLosTrap,
       "cwdmClientModuleExistTrap": cwdmClientModuleExistTrap,
       "rcftRSlotORLnkTrap": rcftRSlotORLnkTrap,
       "rcftRSlotOTLnkTrap": rcftRSlotOTLnkTrap,
       "cwdmSpeedUnmatchedTrap": cwdmSpeedUnmatchedTrap,
       "remotecwdmCWDMLaserTxfaultTrap": remotecwdmCWDMLaserTxfaultTrap,
       "remotecwdmCWDMInputSignalLosTrap": remotecwdmCWDMInputSignalLosTrap,
       "remotecwdmCWDMModuleExistTrap": remotecwdmCWDMModuleExistTrap,
       "rcftSlotE1LOMFTrap": rcftSlotE1LOMFTrap,
       "rcftRSlotE1LOMFTrap": rcftRSlotE1LOMFTrap,
       "rcftSlotE1CVTrap": rcftSlotE1CVTrap,
       "rcftRSlotE1CVTrap": rcftRSlotE1CVTrap,
       "rcftSlotSHDSLLosTrap": rcftSlotSHDSLLosTrap,
       "rcftSlotSHDSLLOFTrap": rcftSlotSHDSLLOFTrap,
       "rcftRSlotSHDSLLosTrap": rcftRSlotSHDSLLosTrap,
       "rcftRSlotSHDSLLOFTrap": rcftRSlotSHDSLLOFTrap,
       "rcftSlotSHDSLLinkTrap": rcftSlotSHDSLLinkTrap,
       "rcftRSlotSHDSLLinkTrap": rcftRSlotSHDSLLinkTrap,
       "rcftClientOLinkTrap": rcftClientOLinkTrap,
       "rcftClientOSDTrap": rcftClientOSDTrap,
       "rcftRClientOLinkTrap": rcftRClientOLinkTrap,
       "rcftRClientOSDTrap": rcftRClientOSDTrap,
       "cwdmPrimaryCWDMInputSignalLosTrap": cwdmPrimaryCWDMInputSignalLosTrap,
       "cwdmPrimaryCWDMModuleExistTrap": cwdmPrimaryCWDMModuleExistTrap,
       "rcftSlotPSChannelOTrap": rcftSlotPSChannelOTrap,
       "rcftInterfaceRELinkTrap": rcftInterfaceRELinkTrap,
       "cwdmSecondaryReceiveLOLTrap": cwdmSecondaryReceiveLOLTrap,
       "cwdmSecondaryCWDMInputSignalLosTrap": cwdmSecondaryCWDMInputSignalLosTrap,
       "cwdmSecondaryCWDMModuleExistTrap": cwdmSecondaryCWDMModuleExistTrap,
       "rcftInterfaceLToRLOSTrap": rcftInterfaceLToRLOSTrap,
       "rcftInterfaceLtoRAISTrap": rcftInterfaceLtoRAISTrap,
       "rcftInterfaceLtoRLOFTrap": rcftInterfaceLtoRLOFTrap,
       "rcftInterfaceLtoRCRCTrap": rcftInterfaceLtoRCRCTrap,
       "rcftSlotRemotePowerDownTrap": rcftSlotRemotePowerDownTrap,
       "rcftSlotVideoLosTrap": rcftSlotVideoLosTrap,
       "rcftRSlotVideoLosTrap": rcftRSlotVideoLosTrap,
       "rcftSlotLocalToRemoteE1CRCTrap": rcftSlotLocalToRemoteE1CRCTrap,
       "rcftSlotLocalToRemoteE1LOFTrap": rcftSlotLocalToRemoteE1LOFTrap,
       "rcftSlotLocalToRemoteE1AISTrap": rcftSlotLocalToRemoteE1AISTrap,
       "rcftSlotLocalToRemoteE1LOSTrap": rcftSlotLocalToRemoteE1LOSTrap,
       "cwdmPrimaryReceiveLOLTrap": cwdmPrimaryReceiveLOLTrap,
       "rcftClientPortLOLTrap": rcftClientPortLOLTrap,
       "rcftLinePortLOLTrap": rcftLinePortLOLTrap,
       "rcftSlotSPChannelOTrap": rcftSlotSPChannelOTrap,
       "rcftSaveConfigFileFinishedTrap": rcftSaveConfigFileFinishedTrap,
       "rcftRSlotLinePortLOLTrap": rcftRSlotLinePortLOLTrap,
       "rcftSlotSFPModuleTempHighTrap": rcftSlotSFPModuleTempHighTrap,
       "rcftSlotSFPModuleTempLowTrap": rcftSlotSFPModuleTempLowTrap,
       "rcftSlotSFPModuleVoltageHighTrap": rcftSlotSFPModuleVoltageHighTrap,
       "rcftSlotSFPModuleVoltageLowTrap": rcftSlotSFPModuleVoltageLowTrap,
       "rcftSlotSFPModuleOffsetCurrHighTrap": rcftSlotSFPModuleOffsetCurrHighTrap,
       "rcftSlotSFPModuleOffsetCurrLowTrap": rcftSlotSFPModuleOffsetCurrLowTrap,
       "rcftSlotSFPModuleSendPowerHighTrap": rcftSlotSFPModuleSendPowerHighTrap,
       "rcftSlotSFPModuleSendPowerLowTrap": rcftSlotSFPModuleSendPowerLowTrap,
       "rcftSlotSFPModuleRecvPowerHighTrap": rcftSlotSFPModuleRecvPowerHighTrap,
       "rcftSlotSFPModuleRecvPowerLowTrap": rcftSlotSFPModuleRecvPowerLowTrap,
       "rcftRSlotSFPModuleTempHighTrap": rcftRSlotSFPModuleTempHighTrap,
       "rcftRSlotSFPModuleTempLowTrap": rcftRSlotSFPModuleTempLowTrap,
       "rcftRSlotSFPModuleVoltageHighTrap": rcftRSlotSFPModuleVoltageHighTrap,
       "rcftRSlotSFPModuleVoltageLowTrap": rcftRSlotSFPModuleVoltageLowTrap,
       "rcftRSlotSFPModuleOffsetCurrHighTrap": rcftRSlotSFPModuleOffsetCurrHighTrap,
       "rcftRSlotSFPModuleOffsetCurrLowTrap": rcftRSlotSFPModuleOffsetCurrLowTrap,
       "rcftRSlotSFPModuleSendPowerHighTrap": rcftRSlotSFPModuleSendPowerHighTrap,
       "rcftRSlotSFPModuleSendPowerLowTrap": rcftRSlotSFPModuleSendPowerLowTrap,
       "rcftRSlotSFPModuleRecvPowerHighTrap": rcftRSlotSFPModuleRecvPowerHighTrap,
       "rcftRSlotSFPModuleRecvPowerLowTrap": rcftRSlotSFPModuleRecvPowerLowTrap,
       "rcftSlotTempHighLimitTrap": rcftSlotTempHighLimitTrap,
       "rcftSlotTempLowLimitTrap": rcftSlotTempLowLimitTrap,
       "rcftSlotHumidityHighLimitTrap": rcftSlotHumidityHighLimitTrap,
       "rcftSlotHumidityLowLimitTrap": rcftSlotHumidityLowLimitTrap,
       "rcftSlotPSChannelTrap": rcftSlotPSChannelTrap,
       "rcftSlotSPChannelTrap": rcftSlotSPChannelTrap,
       "rcftSlotE1TransErrorCodeMore10E-3": rcftSlotE1TransErrorCodeMore10E_3,
       "rcftSlotE1TransErrorCodeMore10E-6": rcftSlotE1TransErrorCodeMore10E_6,
       "rcftMibObjects": rcftMibObjects,
       "rcftSystem": rcftSystem,
       "rcftSysId": rcftSysId,
       "rcftSysLevel": rcftSysLevel,
       "rcftSysChassisNum": rcftSysChassisNum,
       "rcftSysAlarm": rcftSysAlarm,
       "rcftSysTmptAlarmThreshold": rcftSysTmptAlarmThreshold,
       "rcftSysTrapEnable": rcftSysTrapEnable,
       "rcftSysTrapTarget": rcftSysTrapTarget,
       "rcftSysTrapTargetEntry": rcftSysTrapTargetEntry,
       "rcftTrapSink1": rcftTrapSink1,
       "rcftTrapSink2": rcftTrapSink2,
       "rcftTrapSink3": rcftTrapSink3,
       "rcftTrapSink4": rcftTrapSink4,
       "rcftTrapSink5": rcftTrapSink5,
       "rcftTrapSink6": rcftTrapSink6,
       "rcftTrapSink7": rcftTrapSink7,
       "rcftTrapSink8": rcftTrapSink8,
       "rcftRSlotTmptAlarmThreshold": rcftRSlotTmptAlarmThreshold,
       "rcftSysTrapPort": rcftSysTrapPort,
       "rcftSysTrapPortEntry": rcftSysTrapPortEntry,
       "rcftTrapPort1": rcftTrapPort1,
       "rcftTrapPort2": rcftTrapPort2,
       "rcftTrapPort3": rcftTrapPort3,
       "rcftTrapPort4": rcftTrapPort4,
       "rcftTrapPort5": rcftTrapPort5,
       "rcftTrapPort6": rcftTrapPort6,
       "rcftTrapPort7": rcftTrapPort7,
       "rcftTrapPort8": rcftTrapPort8,
       "rcftChassis": rcftChassis,
       "rcftChassisTable": rcftChassisTable,
       "rcftChassisEntry": rcftChassisEntry,
       "rcftChassisIndex": rcftChassisIndex,
       "rcftChassisExist": rcftChassisExist,
       "rcftChassisTmpt": rcftChassisTmpt,
       "rcftPowerNum": rcftPowerNum,
       "rcftChassisType": rcftChassisType,
       "rcftChassisDescr": rcftChassisDescr,
       "rcftPower": rcftPower,
       "rcftPowerTable": rcftPowerTable,
       "rcftPowerEntry": rcftPowerEntry,
       "rcftPowerIndex": rcftPowerIndex,
       "rcftPowerExist": rcftPowerExist,
       "rcft5vStatus": rcft5vStatus,
       "rcft12vStatus": rcft12vStatus,
       "rcft5vAC": rcft5vAC,
       "rcft12vAC": rcft12vAC,
       "rcftFan": rcftFan,
       "rcftFanTable": rcftFanTable,
       "rcftFanEntry": rcftFanEntry,
       "rcftFanIndex": rcftFanIndex,
       "rcftFanLoc": rcftFanLoc,
       "rcftFanStatus": rcftFanStatus,
       "rcftSlotStat": rcftSlotStat,
       "rcftSlotStatTable": rcftSlotStatTable,
       "rcftSlotStatEntry": rcftSlotStatEntry,
       "rcftSlotIndex": rcftSlotIndex,
       "rcftSlotExist": rcftSlotExist,
       "rcftSlotType": rcftSlotType,
       "rcftSlotFaultPass": rcftSlotFaultPass,
       "rcftSlotVLAN": rcftSlotVLAN,
       "rcftSlotConfigStatus": rcftSlotConfigStatus,
       "rcftSlotELink": rcftSlotELink,
       "rcftSlotEAutoNegotiation": rcftSlotEAutoNegotiation,
       "rcftSlotEDuplex": rcftSlotEDuplex,
       "rcftSlotECollCount": rcftSlotECollCount,
       "rcftSlotESpeed": rcftSlotESpeed,
       "rcftSlotETxStatus": rcftSlotETxStatus,
       "rcftSlotERxStatus": rcftSlotERxStatus,
       "rcftSlotOLink": rcftSlotOLink,
       "rcftSlotODuplex": rcftSlotODuplex,
       "rcftSlotOSpeed": rcftSlotOSpeed,
       "rcftSlotOTxStatus": rcftSlotOTxStatus,
       "rcftSlotORxStatus": rcftSlotORxStatus,
       "rcftSlotDescr": rcftSlotDescr,
       "rcftSlotORLnk": rcftSlotORLnk,
       "rcftSlotOTLnk": rcftSlotOTLnk,
       "rcftSlotORmd": rcftSlotORmd,
       "rcftSlotOFxAct": rcftSlotOFxAct,
       "rcftSlotETxAct": rcftSlotETxAct,
       "rcftSlotRemManage": rcftSlotRemManage,
       "rcftSlotLBKTest": rcftSlotLBKTest,
       "rcftSlotVOLimit": rcftSlotVOLimit,
       "rcftSlotVBLimit": rcftSlotVBLimit,
       "rcftSlotLBKTestOk": rcftSlotLBKTestOk,
       "rcftSlotEPort": rcftSlotEPort,
       "rcftSlotOSendPower": rcftSlotOSendPower,
       "rcftSlotOReceSen": rcftSlotOReceSen,
       "rcftSlotOLaser": rcftSlotOLaser,
       "rcftSlotOSD": rcftSlotOSD,
       "rcftSlotOPort": rcftSlotOPort,
       "rcftSlotOrder": rcftSlotOrder,
       "rcftRSlotExist": rcftRSlotExist,
       "rcftRSlotEAutoNegotiation": rcftRSlotEAutoNegotiation,
       "rcftRSlotEDuplex": rcftRSlotEDuplex,
       "rcftRSlotELink": rcftRSlotELink,
       "rcftRSlotFaultPass": rcftRSlotFaultPass,
       "rcftRSlotEPort": rcftRSlotEPort,
       "rcftRSlotRemManage": rcftRSlotRemManage,
       "rcftRSlotVOLimit": rcftRSlotVOLimit,
       "rcftRSlotVBLimit": rcftRSlotVBLimit,
       "rcftRSlotOSendPower": rcftRSlotOSendPower,
       "rcftRSlotOReceSen": rcftRSlotOReceSen,
       "rcftRSlotOLaser": rcftRSlotOLaser,
       "rcftRSlotOSD": rcftRSlotOSD,
       "rcftRSlotOLink": rcftRSlotOLink,
       "rcftRSlotOrder": rcftRSlotOrder,
       "rcftSlotRowStatus": rcftSlotRowStatus,
       "rcftRSlotType": rcftRSlotType,
       "rcftRSlotChassisTmpt": rcftRSlotChassisTmpt,
       "rcftSlotExSwitchMode": rcftSlotExSwitchMode,
       "rcftSlotRevFluxCount": rcftSlotRevFluxCount,
       "rcftSlotSedFluxCount": rcftSlotSedFluxCount,
       "rcftSlotRevFluxTimer": rcftSlotRevFluxTimer,
       "rcftSlotSedFluxTimer": rcftSlotSedFluxTimer,
       "rcftRSlotESpeed": rcftRSlotESpeed,
       "rcftRSlotOSpeed": rcftRSlotOSpeed,
       "rcftRSlotORLnk": rcftRSlotORLnk,
       "rcftRSlotOTLnk": rcftRSlotOTLnk,
       "rcftSlotE1LOS": rcftSlotE1LOS,
       "rcftSlotOLOS": rcftSlotOLOS,
       "rcftSlotOSync": rcftSlotOSync,
       "rcftSlotOTransErrorCode": rcftSlotOTransErrorCode,
       "rcftRSlotE1LOS": rcftRSlotE1LOS,
       "rcftRSlotOLOS": rcftRSlotOLOS,
       "rcftRSlotOSync": rcftRSlotOSync,
       "rcftRSlotOTransErrorCode": rcftRSlotOTransErrorCode,
       "rcftSlotE1LOF": rcftSlotE1LOF,
       "rcftSlotE1CRC": rcftSlotE1CRC,
       "rcftSlotHardWareDescr": rcftSlotHardWareDescr,
       "rcftSlotSigleChipDescr": rcftSlotSigleChipDescr,
       "rcftSlotV35Port": rcftSlotV35Port,
       "rcftSlotV35RTS": rcftSlotV35RTS,
       "rcftSlotV35DTR": rcftSlotV35DTR,
       "rcftSlotE1LoopStatus": rcftSlotE1LoopStatus,
       "rcftSlotE1LoopSwitchStatus": rcftSlotE1LoopSwitchStatus,
       "rcftSlotV35LoopStatus": rcftSlotV35LoopStatus,
       "rcftSlotV35LoopSwitchStatus": rcftSlotV35LoopSwitchStatus,
       "rcftSlotEPort1Link": rcftSlotEPort1Link,
       "rcftSlotEPort1AutoNegotiation": rcftSlotEPort1AutoNegotiation,
       "rcftSlotEPort1Duplex": rcftSlotEPort1Duplex,
       "rcftSlotEPort1Speed": rcftSlotEPort1Speed,
       "rcftSlotEPort1Port": rcftSlotEPort1Port,
       "rcftSlotE2PortBandWidth": rcftSlotE2PortBandWidth,
       "rcftSlotV35Speed": rcftSlotV35Speed,
       "rcftSlotV35RateCfg": rcftSlotV35RateCfg,
       "rcftSlotV35RxClk": rcftSlotV35RxClk,
       "rcftSlotV35TxClk": rcftSlotV35TxClk,
       "rcftSlotV35LoopTest": rcftSlotV35LoopTest,
       "rcftSlotRE1LoopTest": rcftSlotRE1LoopTest,
       "rcftSlotRE1LoopStatus": rcftSlotRE1LoopStatus,
       "rcftSlotLoopTestEn": rcftSlotLoopTestEn,
       "rcftSlotCLKMode": rcftSlotCLKMode,
       "rcftSlotCfgCmdEn": rcftSlotCfgCmdEn,
       "rcftSlotE1PCM": rcftSlotE1PCM,
       "rcftSlotE1CRCEn": rcftSlotE1CRCEn,
       "rcftSlotE1AIS": rcftSlotE1AIS,
       "rcftSlotRALM": rcftSlotRALM,
       "rcftSlotE1Transparent": rcftSlotE1Transparent,
       "rcftSlotEthTransmitSpeed": rcftSlotEthTransmitSpeed,
       "rcftSlotE1Port2LOS": rcftSlotE1Port2LOS,
       "rcftRSlotE1Port2LOS": rcftRSlotE1Port2LOS,
       "rcftSlotRE1LoopSwitchStatus": rcftSlotRE1LoopSwitchStatus,
       "rcftSlotFrameLength": rcftSlotFrameLength,
       "rcftSlotRecvRestrictSpeed": rcftSlotRecvRestrictSpeed,
       "rcftSlotSendRestrictSpeed": rcftSlotSendRestrictSpeed,
       "rcftRSlotFrameLength": rcftRSlotFrameLength,
       "rcftRSlotVLAN": rcftRSlotVLAN,
       "rcftSlotLALM": rcftSlotLALM,
       "rcftSlotChipOpMode": rcftSlotChipOpMode,
       "rcftSlotAutoCutErrLineEn": rcftSlotAutoCutErrLineEn,
       "rcftSlotRamBD": rcftSlotRamBD,
       "rcftSlotV35DSR": rcftSlotV35DSR,
       "rcftSlotV35DCD": rcftSlotV35DCD,
       "rcftRSlotRecvRestrictSpeed": rcftRSlotRecvRestrictSpeed,
       "rcftRSlotSendRestrictSpeed": rcftRSlotSendRestrictSpeed,
       "rcftRSlotV35Speed": rcftRSlotV35Speed,
       "rcftRSlotCLKMode": rcftRSlotCLKMode,
       "rcftSlotWorkStatus": rcftSlotWorkStatus,
       "rcftTxWorkStatus": rcftTxWorkStatus,
       "rcftFxWorkStatus": rcftFxWorkStatus,
       "rcftE1WorkStatus": rcftE1WorkStatus,
       "rcftV35WorkStatus": rcftV35WorkStatus,
       "rcftAllLoopSwitch": rcftAllLoopSwitch,
       "rcftSlotE1PortAlarm": rcftSlotE1PortAlarm,
       "rcftRSlotE1PortAlarm": rcftRSlotE1PortAlarm,
       "rcftRSlotHardWareDescr": rcftRSlotHardWareDescr,
       "rcftRSlotSigleChipDescr": rcftRSlotSigleChipDescr,
       "rcftSlotConfCardType": rcftSlotConfCardType,
       "rcftSlotLineStatus": rcftSlotLineStatus,
       "rcftV35E1PortExtendStatus": rcftV35E1PortExtendStatus,
       "rcftSlotDoubleLoopSwitch": rcftSlotDoubleLoopSwitch,
       "rcftRSlotDoubleLoopSwitch": rcftRSlotDoubleLoopSwitch,
       "rcftRSlotOport": rcftRSlotOport,
       "cwdmClientWorkSpeed": cwdmClientWorkSpeed,
       "cwdmCWDMWorkStatus": cwdmCWDMWorkStatus,
       "cwdmCWDMModuleMaxSpeed": cwdmCWDMModuleMaxSpeed,
       "cwdmCWDMModuleTransLen": cwdmCWDMModuleTransLen,
       "cwdmCWDMModuleWaveLen": cwdmCWDMModuleWaveLen,
       "cwdmCWDMModuleManufacturer": cwdmCWDMModuleManufacturer,
       "cwdmCWDMModuleDescr": cwdmCWDMModuleDescr,
       "cwdmCWDMModuleVersion": cwdmCWDMModuleVersion,
       "cwdmCWDMModuleSerialNumber": cwdmCWDMModuleSerialNumber,
       "cwdmClientWorkStatus": cwdmClientWorkStatus,
       "cwdmClientModuleMaxSpeed": cwdmClientModuleMaxSpeed,
       "cwdmClientModuleInterfaceType": cwdmClientModuleInterfaceType,
       "cwdmClientModuleTransLen": cwdmClientModuleTransLen,
       "cwdmClientModuleWaveLen": cwdmClientModuleWaveLen,
       "cwdmClientModuleManufacturer": cwdmClientModuleManufacturer,
       "cwdmClientModuleDescr": cwdmClientModuleDescr,
       "cwdmClientModuleVersion": cwdmClientModuleVersion,
       "cwdmClientModuleSerialNumber": cwdmClientModuleSerialNumber,
       "cwdmCWDMWorkSpeed": cwdmCWDMWorkSpeed,
       "opticalModuleType": opticalModuleType,
       "rcftSlotInformation": rcftSlotInformation,
       "remoteOpticalModuleType": remoteOpticalModuleType,
       "rcftRSlotInformation": rcftRSlotInformation,
       "rcftRSlotRevFluxCount": rcftRSlotRevFluxCount,
       "rcftRSlotSedFluxCount": rcftRSlotSedFluxCount,
       "rcftRSlotRevFluxTimer": rcftRSlotRevFluxTimer,
       "rcftRSlotSedFluxTimer": rcftRSlotSedFluxTimer,
       "rcftSlotRevErrFluxCnt": rcftSlotRevErrFluxCnt,
       "rcftSlotSedErrFluxCnt": rcftSlotSedErrFluxCnt,
       "cwdmOMUmoduleType": cwdmOMUmoduleType,
       "rcftSlotE1TimeSlot": rcftSlotE1TimeSlot,
       "rcftSlotWANRevFluxPacket": rcftSlotWANRevFluxPacket,
       "rcftSlotWANRevFluxCount": rcftSlotWANRevFluxCount,
       "rcftSlotWANSedFluxPacket": rcftSlotWANSedFluxPacket,
       "rcftSlotWANSedFluxCount": rcftSlotWANSedFluxCount,
       "rcftSlotWANRevErrFluxPacket": rcftSlotWANRevErrFluxPacket,
       "rcftSlotRevFluxPacket": rcftSlotRevFluxPacket,
       "rcftSlotSedFluxPacket": rcftSlotSedFluxPacket,
       "rcftRSlotE1TimeSlot": rcftRSlotE1TimeSlot,
       "rcftRSlotWANRevFluxPacket": rcftRSlotWANRevFluxPacket,
       "rcftRSlotWANRevFluxCount": rcftRSlotWANRevFluxCount,
       "rcftRSlotWANSedFluxPacket": rcftRSlotWANSedFluxPacket,
       "rcftRSlotWANSedFluxCount": rcftRSlotWANSedFluxCount,
       "rcftRSlotWANRevErrFluxPacket": rcftRSlotWANRevErrFluxPacket,
       "rcftRSlotRevFluxPacket": rcftRSlotRevFluxPacket,
       "rcftRSlotSedFluxPacket": rcftRSlotSedFluxPacket,
       "rcftRSlotRevErrFluxCnt": rcftRSlotRevErrFluxCnt,
       "rcftExtentWorkStatus": rcftExtentWorkStatus,
       "rcftSlotE1ESCnt": rcftSlotE1ESCnt,
       "rcftSlotE1SESCnt": rcftSlotE1SESCnt,
       "rcftRSlotE1ESCnt": rcftRSlotE1ESCnt,
       "rcftRSlotE1SESCnt": rcftRSlotE1SESCnt,
       "rcftRSlotCWDMModuleMaxSpeed": rcftRSlotCWDMModuleMaxSpeed,
       "rcftRSlotCWDMModuleTransLen": rcftRSlotCWDMModuleTransLen,
       "rcftRSlotCWDMModuleWaveLen": rcftRSlotCWDMModuleWaveLen,
       "rcftRSlotCWDMModuleManufacturer": rcftRSlotCWDMModuleManufacturer,
       "rcftRSlotCWDMModuleDescr": rcftRSlotCWDMModuleDescr,
       "rcftRSlotCWDMModuleVersion": rcftRSlotCWDMModuleVersion,
       "rcftRSlotCWDMModuleSerialNumber": rcftRSlotCWDMModuleSerialNumber,
       "rcftSlotLANOPortModuleType": rcftSlotLANOPortModuleType,
       "rcftSlotWANOPortModuleType": rcftSlotWANOPortModuleType,
       "rcftSlotCDRSpeed": rcftSlotCDRSpeed,
       "rcftRSlotManufacturer": rcftRSlotManufacturer,
       "rcftRSlotSoftwareVersion": rcftRSlotSoftwareVersion,
       "rcftRSlotVoltageValue": rcftRSlotVoltageValue,
       "rcftRSlotCommunityRW": rcftRSlotCommunityRW,
       "rcftRSlotCommunity": rcftRSlotCommunity,
       "rcftRSlotDeviceIP": rcftRSlotDeviceIP,
       "rcftSlotLinePortSpeed": rcftSlotLinePortSpeed,
       "rcftSlotLinePortMaxSpeed": rcftSlotLinePortMaxSpeed,
       "rcftSlotLinePortMinSpeed": rcftSlotLinePortMinSpeed,
       "rcftSlotLinePortSNR": rcftSlotLinePortSNR,
       "rcftSlotLinePortLinkUpTime": rcftSlotLinePortLinkUpTime,
       "rcftRSlotLinePortSNR": rcftRSlotLinePortSNR,
       "rcftRSlotLinePortLinkUpTime": rcftRSlotLinePortLinkUpTime,
       "rcftRSlotLinePortSpeed": rcftRSlotLinePortSpeed,
       "rcftSlotOrderParameter": rcftSlotOrderParameter,
       "rcftRSlotOrderParameter": rcftRSlotOrderParameter,
       "rcftSlotRevErrFluxPacket": rcftSlotRevErrFluxPacket,
       "rcftRSlotRevErrFluxPacket": rcftRSlotRevErrFluxPacket,
       "rcftRSlotLinePortType": rcftRSlotLinePortType,
       "rcftRSlotManageChannelSel": rcftRSlotManageChannelSel,
       "rcftRSlotManageChannelTSNum": rcftRSlotManageChannelTSNum,
       "rcftRSlotV35TimeSlots": rcftRSlotV35TimeSlots,
       "rcftSlotLinePortSNRConf": rcftSlotLinePortSNRConf,
       "rcftRSlotLANOPortModuleType": rcftRSlotLANOPortModuleType,
       "rcftRSlotConfigFlag": rcftRSlotConfigFlag,
       "rcftSlotOpticalDeviceStatus": rcftSlotOpticalDeviceStatus,
       "rcftSlotPrimaryAdjustFactor": rcftSlotPrimaryAdjustFactor,
       "rcftSlotPrimaryOpticalRate": rcftSlotPrimaryOpticalRate,
       "rcftSlotPrimaryTrapThreshold": rcftSlotPrimaryTrapThreshold,
       "rcftSlotSecondaryAdjustFactor": rcftSlotSecondaryAdjustFactor,
       "rcftSlotSecondaryOpticalRate": rcftSlotSecondaryOpticalRate,
       "rcftSlotSecondaryTrapThreshold": rcftSlotSecondaryTrapThreshold,
       "rcftSlotWANSendErrFluxPacket": rcftSlotWANSendErrFluxPacket,
       "rcftRSlotWANSendErrFluxPacket": rcftRSlotWANSendErrFluxPacket,
       "rcftSlotOpticalDeviceType": rcftSlotOpticalDeviceType,
       "rcftRSlotCardOrderInfor": rcftRSlotCardOrderInfor,
       "rcftRSlotTimeSlots": rcftRSlotTimeSlots,
       "rcftRSlotServiceConnectMode": rcftRSlotServiceConnectMode,
       "rcftSlotSendErrFluxPacket": rcftSlotSendErrFluxPacket,
       "rcftRSlotSendErrFluxPacket": rcftRSlotSendErrFluxPacket,
       "cwdmSecondaryCWDMModuleMaxSpeed": cwdmSecondaryCWDMModuleMaxSpeed,
       "cwdmSecondaryCWDMModuleTransLen": cwdmSecondaryCWDMModuleTransLen,
       "cwdmSecondaryCWDMModuleWaveLen": cwdmSecondaryCWDMModuleWaveLen,
       "cwdmSecondaryCWDMModuleManufacturer": cwdmSecondaryCWDMModuleManufacturer,
       "cwdmSecondaryCWDMModuleDescr": cwdmSecondaryCWDMModuleDescr,
       "cwdmSecondaryCWDMModuleVersion": cwdmSecondaryCWDMModuleVersion,
       "cwdmSecondaryCWDMModuleSerialNumber": cwdmSecondaryCWDMModuleSerialNumber,
       "rcftSlotVLANTagDirection": rcftSlotVLANTagDirection,
       "rcftRSlotVLANTagDirection": rcftRSlotVLANTagDirection,
       "rcftSlotVLANTagModule": rcftSlotVLANTagModule,
       "rcftRSlotVLANTagModule": rcftRSlotVLANTagModule,
       "rcftSlotVLANID": rcftSlotVLANID,
       "rcftRSlotVLANID": rcftRSlotVLANID,
       "rcftSlotISPTPID": rcftSlotISPTPID,
       "rcftRSlotISPTPID": rcftRSlotISPTPID,
       "rcftSlotE1SubCardType": rcftSlotE1SubCardType,
       "rcftSlotMultiE1LoopOrder": rcftSlotMultiE1LoopOrder,
       "rcftSlotSubModuleExist": rcftSlotSubModuleExist,
       "rcftSlotOrderTimeParameter": rcftSlotOrderTimeParameter,
       "rcftSlotRLPStatus": rcftSlotRLPStatus,
       "rcftSlotSFPDiagnosticsInfo": rcftSlotSFPDiagnosticsInfo,
       "rcftRSlotSFPDiagnosticsInfo": rcftRSlotSFPDiagnosticsInfo,
       "rcftSlotTemp": rcftSlotTemp,
       "rcftSlotLALStatus": rcftSlotLALStatus,
       "rcftSlotRALStatus": rcftSlotRALStatus,
       "rcftSlotCardInformation": rcftSlotCardInformation,
       "rcftSlotVoltage": rcftSlotVoltage,
       "rcftSlotVoltageHighLimit": rcftSlotVoltageHighLimit,
       "rcftSlotVoltageLowLimit": rcftSlotVoltageLowLimit,
       "rcftSlotTempHighLimit": rcftSlotTempHighLimit,
       "rcftSlotTempLowLimit": rcftSlotTempLowLimit,
       "rcftSlotHumidity": rcftSlotHumidity,
       "rcftSlotHumidityHighLimit": rcftSlotHumidityHighLimit,
       "rcftSlotHumidityLowLimit": rcftSlotHumidityLowLimit,
       "rcftSlotMultiE1AlarmRejectOrder": rcftSlotMultiE1AlarmRejectOrder,
       "rcftT1PortPulseWaveForm": rcftT1PortPulseWaveForm,
       "rcftT1PortCodeType": rcftT1PortCodeType,
       "rcftSlotSDRAM": rcftSlotSDRAM,
       "rcftSlotSabitMode": rcftSlotSabitMode,
       "rcftSlotApsWaitToRestore": rcftSlotApsWaitToRestore,
       "rcftSlotCLKChannel": rcftSlotCLKChannel,
       "rcftSlotRmcChannelType": rcftSlotRmcChannelType,
       "rcftSlotApsE3SwitchDelay": rcftSlotApsE3SwitchDelay,
       "rcftSlotApsE6SwitchDelay": rcftSlotApsE6SwitchDelay,
       "rcftE1DS1PortType": rcftE1DS1PortType,
       "rcftSlotManageID": rcftSlotManageID,
       "rcftSlotE1PortNumber": rcftSlotE1PortNumber,
       "rcftSlotQoS": rcftSlotQoS,
       "rcftSlotTPIDRemark": rcftSlotTPIDRemark,
       "rcftRSlotTPIDRemark": rcftRSlotTPIDRemark,
       "rcftSlotDeviceMibUse": rcftSlotDeviceMibUse,
       "rcftSlotApsSwitchDelay": rcftSlotApsSwitchDelay,
       "rcftInterfaceStatTable": rcftInterfaceStatTable,
       "rcftInterfaceStatEntry": rcftInterfaceStatEntry,
       "rcftInterfaceType": rcftInterfaceType,
       "rcftInterfaceIndex": rcftInterfaceIndex,
       "rcftInterfaceRLink": rcftInterfaceRLink,
       "rcftInterfaceRAutoNegotiation": rcftInterfaceRAutoNegotiation,
       "rcftInterfaceRDuplex": rcftInterfaceRDuplex,
       "rcftInterfaceRSpeed": rcftInterfaceRSpeed,
       "rcftInterfaceRStat": rcftInterfaceRStat,
       "rcftInterfaceLOS": rcftInterfaceLOS,
       "rcftInterfaceCV": rcftInterfaceCV,
       "rcftInterfaceAIS": rcftInterfaceAIS,
       "rcftInterfaceLOF": rcftInterfaceLOF,
       "rcftInterfaceCRC": rcftInterfaceCRC,
       "rcftInterfaceE5": rcftInterfaceE5,
       "rcftInterfaceRLOS": rcftInterfaceRLOS,
       "rcftInterfaceRCV": rcftInterfaceRCV,
       "rcftInterfaceRAIS": rcftInterfaceRAIS,
       "rcftInterfaceRLOF": rcftInterfaceRLOF,
       "rcftInterfaceRCRC": rcftInterfaceRCRC,
       "rcftInterfaceUnUsed": rcftInterfaceUnUsed,
       "rcftInterfaceStat": rcftInterfaceStat,
       "rcftInterfaceLink": rcftInterfaceLink,
       "rcftInterfaceAutoNegotiation": rcftInterfaceAutoNegotiation,
       "rcftInterfaceDuplex": rcftInterfaceDuplex,
       "rcftInterfaceSpeed": rcftInterfaceSpeed,
       "rcftInterfaceTag": rcftInterfaceTag,
       "rcftInterfaceRecvRestrictSpeed": rcftInterfaceRecvRestrictSpeed,
       "rcftInterfaceSendRestrictSpeed": rcftInterfaceSendRestrictSpeed,
       "rcftInterfaceRTag": rcftInterfaceRTag,
       "rcftInterfaceRRecvFluxCount": rcftInterfaceRRecvFluxCount,
       "rcftInterfaceRSendFluxCount": rcftInterfaceRSendFluxCount,
       "rcftInterfaceRRecvFluxTimer": rcftInterfaceRRecvFluxTimer,
       "rcftInterfaceRSendFluxTimer": rcftInterfaceRSendFluxTimer,
       "rcftInterfaceRpriority": rcftInterfaceRpriority,
       "rcftInterfaceRMDIXAuto": rcftInterfaceRMDIXAuto,
       "rcftInterfaceRRecvRestrictSpeed": rcftInterfaceRRecvRestrictSpeed,
       "rcftInterfaceRFlowCtrl": rcftInterfaceRFlowCtrl,
       "rcftInterfaceRAudioType": rcftInterfaceRAudioType,
       "rcftInterfaceRAudioTimeSlots": rcftInterfaceRAudioTimeSlots,
       "rcftInterfaceRAudioInSignalingSymbol": rcftInterfaceRAudioInSignalingSymbol,
       "rcftInterfaceRAudioOutSignalingSymbol": rcftInterfaceRAudioOutSignalingSymbol,
       "rcftInterfaceRAudioInSignalingType": rcftInterfaceRAudioInSignalingType,
       "rcftInterfaceRAudioOutSignalingType": rcftInterfaceRAudioOutSignalingType,
       "rcftInterfaceRAudioInSignalingStatus": rcftInterfaceRAudioInSignalingStatus,
       "rcftInterfaceRAudioOutSignalingStatus": rcftInterfaceRAudioOutSignalingStatus,
       "rcftInterfaceRAudioUseEnable": rcftInterfaceRAudioUseEnable,
       "rcftInterfaceWANToLANFPEnWANDownLANPortStatus": rcftInterfaceWANToLANFPEnWANDownLANPortStatus,
       "rcftInterfaceWANTOLANFPEnRemoteLANDownLANPortStatus": rcftInterfaceWANTOLANFPEnRemoteLANDownLANPortStatus,
       "rcftInterfaceRecvFluxCount": rcftInterfaceRecvFluxCount,
       "rcftInterfaceSendFluxCount": rcftInterfaceSendFluxCount,
       "rcftInterfaceRecvFluxPacket": rcftInterfaceRecvFluxPacket,
       "rcftInterfaceSendFluxPacket": rcftInterfaceSendFluxPacket,
       "rcftInterfaceRecvErrFluxPacket": rcftInterfaceRecvErrFluxPacket,
       "rcftInterfaceSendErrFluxPacket": rcftInterfaceSendErrFluxPacket,
       "rcftInterfaceRecvFluxTimer": rcftInterfaceRecvFluxTimer,
       "rcftInterfaceSendFluxTimer": rcftInterfaceSendFluxTimer,
       "rcftInterfaceRSendRestrictSpeed": rcftInterfaceRSendRestrictSpeed,
       "rcftInterfaceRWANToLANFPEnWANDownLANPortStatus": rcftInterfaceRWANToLANFPEnWANDownLANPortStatus,
       "rcftInterfaceRWANTOLANFPEnRemoteLANDownLANPortStatus": rcftInterfaceRWANTOLANFPEnRemoteLANDownLANPortStatus,
       "rcftInterfaceRRecvFluxPacket": rcftInterfaceRRecvFluxPacket,
       "rcftInterfaceRSendFluxPacket": rcftInterfaceRSendFluxPacket,
       "rcftInterfaceRRecvErrFluxPacket": rcftInterfaceRRecvErrFluxPacket,
       "rcftInterfaceRSendErrFluxPacket": rcftInterfaceRSendErrFluxPacket,
       "rcftInterfaceFoundLink": rcftInterfaceFoundLink,
       "rcftInterfaceBERT": rcftInterfaceBERT,
       "rcftInterfaceCLKMode": rcftInterfaceCLKMode,
       "rcftInterfaceCRCStatus": rcftInterfaceCRCStatus,
       "rcftInterfaceCRCEnable": rcftInterfaceCRCEnable,
       "rcftInterfaceLocalLoopEn": rcftInterfaceLocalLoopEn,
       "rcftInterfaceRemoteLoopEn": rcftInterfaceRemoteLoopEn,
       "rcftInterfaceTransErrorCode": rcftInterfaceTransErrorCode,
       "rcftInterfaceE1Location": rcftInterfaceE1Location,
       "rcftInterfaceE1ESCnt": rcftInterfaceE1ESCnt,
       "rcftInterfaceE1SESCnt": rcftInterfaceE1SESCnt,
       "rcftInterfaceE1TimeSlot": rcftInterfaceE1TimeSlot,
       "rcftInterfaceE1Transparent": rcftInterfaceE1Transparent,
       "rcftStmStatTable": rcftStmStatTable,
       "rcftStmStatEntry": rcftStmStatEntry,
       "rcftStmAdminStatus": rcftStmAdminStatus,
       "rcftStmFiberPort": rcftStmFiberPort,
       "rcftStmFiberRxPllUnlck": rcftStmFiberRxPllUnlck,
       "rcftStmFiberTxClkLos": rcftStmFiberTxClkLos,
       "rcftStmFiberAnalogLos": rcftStmFiberAnalogLos,
       "rcftStmFiberDigitalLos": rcftStmFiberDigitalLos,
       "rcftStmFiberSyncLos": rcftStmFiberSyncLos,
       "rcftStmBncPort": rcftStmBncPort,
       "rcftStmBncRxPllUnlck": rcftStmBncRxPllUnlck,
       "rcftStmBncTxClkLos": rcftStmBncTxClkLos,
       "rcftStmBncAnalogLos": rcftStmBncAnalogLos,
       "rcftStmBncDigitalLos": rcftStmBncDigitalLos,
       "rcftStmBncSyncLos": rcftStmBncSyncLos,
       "rcftConfigFlagTable": rcftConfigFlagTable,
       "rcftConfigFlagEntry": rcftConfigFlagEntry,
       "rcftLocalDeviceConfigFinishFlag": rcftLocalDeviceConfigFinishFlag,
       "rcftSlotConfStatTable": rcftSlotConfStatTable,
       "rcftSlotConfStatEntry": rcftSlotConfStatEntry,
       "rcftSlotConfEDuplex": rcftSlotConfEDuplex,
       "rcftSlotConfESpeed": rcftSlotConfESpeed,
       "rcftRSlotConfEDuplex": rcftRSlotConfEDuplex,
       "rcftRSlotConfESpeed": rcftRSlotConfESpeed,
       "rcftConfTxWorkStatus": rcftConfTxWorkStatus}
)
