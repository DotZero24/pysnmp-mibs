# SNMP MIB module (AFFIRMED-ALARM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/microsoft/AFFIRMED-ALARM-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:05:42 2025
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

(affirmedSnmpModuleIDs,
 affirmedSnmpObjects) = mibBuilder.importSymbols(
    "AFFIRMED-SNMP-MIB",
    "affirmedSnmpModuleIDs",
    "affirmedSnmpObjects")

(ItuPerceivedSeverity,) = mibBuilder.importSymbols(
    "ITU-ALARM-TC-MIB",
    "ItuPerceivedSeverity")

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

(DateAndTime,
 DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

affirmedAlarmMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 37963, 3, 1, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AffirmedAlarmObjects_ObjectIdentity = ObjectIdentity
affirmedAlarmObjects = _AffirmedAlarmObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37963, 1, 1)
)
_AffirmedAlarmSeqId_Type = Integer32
_AffirmedAlarmSeqId_Object = MibScalar
affirmedAlarmSeqId = _AffirmedAlarmSeqId_Object(
    (1, 3, 6, 1, 4, 1, 37963, 1, 1, 1),
    _AffirmedAlarmSeqId_Type()
)
affirmedAlarmSeqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    affirmedAlarmSeqId.setStatus("current")


class _AffirmedAlarmDateTime_Type(OctetString):
    """Custom type affirmedAlarmDateTime based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_AffirmedAlarmDateTime_Type.__name__ = "OctetString"
_AffirmedAlarmDateTime_Object = MibScalar
affirmedAlarmDateTime = _AffirmedAlarmDateTime_Object(
    (1, 3, 6, 1, 4, 1, 37963, 1, 1, 2),
    _AffirmedAlarmDateTime_Type()
)
affirmedAlarmDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    affirmedAlarmDateTime.setStatus("current")


class _AffirmedAlarmChassisName_Type(OctetString):
    """Custom type affirmedAlarmChassisName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 63),
    )


_AffirmedAlarmChassisName_Type.__name__ = "OctetString"
_AffirmedAlarmChassisName_Object = MibScalar
affirmedAlarmChassisName = _AffirmedAlarmChassisName_Object(
    (1, 3, 6, 1, 4, 1, 37963, 1, 1, 3),
    _AffirmedAlarmChassisName_Type()
)
affirmedAlarmChassisName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    affirmedAlarmChassisName.setStatus("current")


class _AffirmedAlarmSourceId_Type(OctetString):
    """Custom type affirmedAlarmSourceId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_AffirmedAlarmSourceId_Type.__name__ = "OctetString"
_AffirmedAlarmSourceId_Object = MibScalar
affirmedAlarmSourceId = _AffirmedAlarmSourceId_Object(
    (1, 3, 6, 1, 4, 1, 37963, 1, 1, 4),
    _AffirmedAlarmSourceId_Type()
)
affirmedAlarmSourceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    affirmedAlarmSourceId.setStatus("current")
_AffirmedAlarmSeverity_Type = ItuPerceivedSeverity
_AffirmedAlarmSeverity_Object = MibScalar
affirmedAlarmSeverity = _AffirmedAlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 37963, 1, 1, 5),
    _AffirmedAlarmSeverity_Type()
)
affirmedAlarmSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    affirmedAlarmSeverity.setStatus("current")
_AffirmedAlarmRefSeqId_Type = Integer32
_AffirmedAlarmRefSeqId_Object = MibScalar
affirmedAlarmRefSeqId = _AffirmedAlarmRefSeqId_Object(
    (1, 3, 6, 1, 4, 1, 37963, 1, 1, 6),
    _AffirmedAlarmRefSeqId_Type()
)
affirmedAlarmRefSeqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    affirmedAlarmRefSeqId.setStatus("current")


class _AffirmedAlarmDetails_Type(OctetString):
    """Custom type affirmedAlarmDetails based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_AffirmedAlarmDetails_Type.__name__ = "OctetString"
_AffirmedAlarmDetails_Object = MibScalar
affirmedAlarmDetails = _AffirmedAlarmDetails_Object(
    (1, 3, 6, 1, 4, 1, 37963, 1, 1, 7),
    _AffirmedAlarmDetails_Type()
)
affirmedAlarmDetails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    affirmedAlarmDetails.setStatus("current")


class _AffirmedPotentialImpact_Type(OctetString):
    """Custom type affirmedPotentialImpact based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 750),
    )


_AffirmedPotentialImpact_Type.__name__ = "OctetString"
_AffirmedPotentialImpact_Object = MibScalar
affirmedPotentialImpact = _AffirmedPotentialImpact_Object(
    (1, 3, 6, 1, 4, 1, 37963, 1, 1, 8),
    _AffirmedPotentialImpact_Type()
)
affirmedPotentialImpact.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    affirmedPotentialImpact.setStatus("current")


class _AffirmedCorrectiveAction_Type(OctetString):
    """Custom type affirmedCorrectiveAction based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 750),
    )


_AffirmedCorrectiveAction_Type.__name__ = "OctetString"
_AffirmedCorrectiveAction_Object = MibScalar
affirmedCorrectiveAction = _AffirmedCorrectiveAction_Object(
    (1, 3, 6, 1, 4, 1, 37963, 1, 1, 9),
    _AffirmedCorrectiveAction_Type()
)
affirmedCorrectiveAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    affirmedCorrectiveAction.setStatus("current")


class _AffirmedVmSourceIpAddress_Type(OctetString):
    """Custom type affirmedVmSourceIpAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_AffirmedVmSourceIpAddress_Type.__name__ = "OctetString"
_AffirmedVmSourceIpAddress_Object = MibScalar
affirmedVmSourceIpAddress = _AffirmedVmSourceIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 37963, 1, 1, 10),
    _AffirmedVmSourceIpAddress_Type()
)
affirmedVmSourceIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    affirmedVmSourceIpAddress.setStatus("current")


class _AffirmedVmSourceName_Type(OctetString):
    """Custom type affirmedVmSourceName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_AffirmedVmSourceName_Type.__name__ = "OctetString"
_AffirmedVmSourceName_Object = MibScalar
affirmedVmSourceName = _AffirmedVmSourceName_Object(
    (1, 3, 6, 1, 4, 1, 37963, 1, 1, 11),
    _AffirmedVmSourceName_Type()
)
affirmedVmSourceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    affirmedVmSourceName.setStatus("current")


class _Name_Type(OctetString):
    """Custom type name based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_Name_Type.__name__ = "OctetString"
_Name_Object = MibScalar
name = _Name_Object(
    (1, 3, 6, 1, 4, 1, 37963, 1, 1, 12),
    _Name_Type()
)
name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    name.setStatus("current")


class _Chassis_Type(OctetString):
    """Custom type chassis based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_Chassis_Type.__name__ = "OctetString"
_Chassis_Object = MibScalar
chassis = _Chassis_Object(
    (1, 3, 6, 1, 4, 1, 37963, 1, 1, 13),
    _Chassis_Type()
)
chassis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassis.setStatus("current")


class _Slot_Type(OctetString):
    """Custom type slot based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_Slot_Type.__name__ = "OctetString"
_Slot_Object = MibScalar
slot = _Slot_Object(
    (1, 3, 6, 1, 4, 1, 37963, 1, 1, 14),
    _Slot_Type()
)
slot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slot.setStatus("current")


class _Cpu_Type(OctetString):
    """Custom type cpu based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_Cpu_Type.__name__ = "OctetString"
_Cpu_Object = MibScalar
cpu = _Cpu_Object(
    (1, 3, 6, 1, 4, 1, 37963, 1, 1, 15),
    _Cpu_Type()
)
cpu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpu.setStatus("current")


class _Dirname_Type(OctetString):
    """Custom type dirname based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_Dirname_Type.__name__ = "OctetString"
_Dirname_Object = MibScalar
dirname = _Dirname_Object(
    (1, 3, 6, 1, 4, 1, 37963, 1, 1, 16),
    _Dirname_Type()
)
dirname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dirname.setStatus("current")


class _Adminstate_Type(OctetString):
    """Custom type adminstate based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_Adminstate_Type.__name__ = "OctetString"
_Adminstate_Object = MibScalar
adminstate = _Adminstate_Object(
    (1, 3, 6, 1, 4, 1, 37963, 1, 1, 17),
    _Adminstate_Type()
)
adminstate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adminstate.setStatus("current")


class _Resource_Type(OctetString):
    """Custom type resource based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_Resource_Type.__name__ = "OctetString"
_Resource_Object = MibScalar
resource = _Resource_Object(
    (1, 3, 6, 1, 4, 1, 37963, 1, 1, 18),
    _Resource_Type()
)
resource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    resource.setStatus("current")


class _Sensor_Type(OctetString):
    """Custom type sensor based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_Sensor_Type.__name__ = "OctetString"
_Sensor_Object = MibScalar
sensor = _Sensor_Object(
    (1, 3, 6, 1, 4, 1, 37963, 1, 1, 19),
    _Sensor_Type()
)
sensor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor.setStatus("current")


class _Data_Type(OctetString):
    """Custom type data based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_Data_Type.__name__ = "OctetString"
_Data_Object = MibScalar
data = _Data_Object(
    (1, 3, 6, 1, 4, 1, 37963, 1, 1, 20),
    _Data_Type()
)
data.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    data.setStatus("current")


class _Taskname_Type(OctetString):
    """Custom type taskname based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_Taskname_Type.__name__ = "OctetString"
_Taskname_Object = MibScalar
taskname = _Taskname_Object(
    (1, 3, 6, 1, 4, 1, 37963, 1, 1, 21),
    _Taskname_Type()
)
taskname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    taskname.setStatus("current")


class _Cid_Type(OctetString):
    """Custom type cid based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_Cid_Type.__name__ = "OctetString"
_Cid_Object = MibScalar
cid = _Cid_Object(
    (1, 3, 6, 1, 4, 1, 37963, 1, 1, 22),
    _Cid_Type()
)
cid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cid.setStatus("current")


class _Sid_Type(OctetString):
    """Custom type sid based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_Sid_Type.__name__ = "OctetString"
_Sid_Object = MibScalar
sid = _Sid_Object(
    (1, 3, 6, 1, 4, 1, 37963, 1, 1, 23),
    _Sid_Type()
)
sid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sid.setStatus("current")


class _Type_Type(OctetString):
    """Custom type type based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_Type_Type.__name__ = "OctetString"
_Type_Object = MibScalar
type = _Type_Object(
    (1, 3, 6, 1, 4, 1, 37963, 1, 1, 24),
    _Type_Type()
)
type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    type.setStatus("current")


class _Subtype_Type(OctetString):
    """Custom type subtype based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_Subtype_Type.__name__ = "OctetString"
_Subtype_Object = MibScalar
subtype = _Subtype_Object(
    (1, 3, 6, 1, 4, 1, 37963, 1, 1, 25),
    _Subtype_Type()
)
subtype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    subtype.setStatus("current")


class _Level_Type(OctetString):
    """Custom type level based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_Level_Type.__name__ = "OctetString"
_Level_Object = MibScalar
level = _Level_Object(
    (1, 3, 6, 1, 4, 1, 37963, 1, 1, 26),
    _Level_Type()
)
level.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    level.setStatus("current")


class _Time_Type(OctetString):
    """Custom type time based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_Time_Type.__name__ = "OctetString"
_Time_Object = MibScalar
time = _Time_Object(
    (1, 3, 6, 1, 4, 1, 37963, 1, 1, 27),
    _Time_Type()
)
time.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    time.setStatus("current")


class _Services_Type(OctetString):
    """Custom type services based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_Services_Type.__name__ = "OctetString"
_Services_Object = MibScalar
services = _Services_Object(
    (1, 3, 6, 1, 4, 1, 37963, 1, 1, 28),
    _Services_Type()
)
services.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    services.setStatus("current")


class _Actions_Type(OctetString):
    """Custom type actions based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_Actions_Type.__name__ = "OctetString"
_Actions_Object = MibScalar
actions = _Actions_Object(
    (1, 3, 6, 1, 4, 1, 37963, 1, 1, 29),
    _Actions_Type()
)
actions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    actions.setStatus("current")


class _Ledname_Type(OctetString):
    """Custom type ledname based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_Ledname_Type.__name__ = "OctetString"
_Ledname_Object = MibScalar
ledname = _Ledname_Object(
    (1, 3, 6, 1, 4, 1, 37963, 1, 1, 30),
    _Ledname_Type()
)
ledname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ledname.setStatus("current")


class _Ledcolor_Type(OctetString):
    """Custom type ledcolor based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_Ledcolor_Type.__name__ = "OctetString"
_Ledcolor_Object = MibScalar
ledcolor = _Ledcolor_Object(
    (1, 3, 6, 1, 4, 1, 37963, 1, 1, 31),
    _Ledcolor_Type()
)
ledcolor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ledcolor.setStatus("current")


class _Usid_Type(OctetString):
    """Custom type usid based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_Usid_Type.__name__ = "OctetString"
_Usid_Object = MibScalar
usid = _Usid_Object(
    (1, 3, 6, 1, 4, 1, 37963, 1, 1, 32),
    _Usid_Type()
)
usid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usid.setStatus("current")


class _Hardorsoft_Type(OctetString):
    """Custom type hardorsoft based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_Hardorsoft_Type.__name__ = "OctetString"
_Hardorsoft_Object = MibScalar
hardorsoft = _Hardorsoft_Object(
    (1, 3, 6, 1, 4, 1, 37963, 1, 1, 33),
    _Hardorsoft_Type()
)
hardorsoft.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hardorsoft.setStatus("current")


class _Readerrors_Type(OctetString):
    """Custom type readerrors based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_Readerrors_Type.__name__ = "OctetString"
_Readerrors_Object = MibScalar
readerrors = _Readerrors_Object(
    (1, 3, 6, 1, 4, 1, 37963, 1, 1, 34),
    _Readerrors_Type()
)
readerrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    readerrors.setStatus("current")


class _Writeerrors_Type(OctetString):
    """Custom type writeerrors based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_Writeerrors_Type.__name__ = "OctetString"
_Writeerrors_Object = MibScalar
writeerrors = _Writeerrors_Object(
    (1, 3, 6, 1, 4, 1, 37963, 1, 1, 35),
    _Writeerrors_Type()
)
writeerrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    writeerrors.setStatus("current")


class _Slotnumber_Type(OctetString):
    """Custom type slotnumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_Slotnumber_Type.__name__ = "OctetString"
_Slotnumber_Object = MibScalar
slotnumber = _Slotnumber_Object(
    (1, 3, 6, 1, 4, 1, 37963, 1, 1, 36),
    _Slotnumber_Type()
)
slotnumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotnumber.setStatus("current")


class _Failuredescription_Type(OctetString):
    """Custom type failuredescription based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_Failuredescription_Type.__name__ = "OctetString"
_Failuredescription_Object = MibScalar
failuredescription = _Failuredescription_Object(
    (1, 3, 6, 1, 4, 1, 37963, 1, 1, 37),
    _Failuredescription_Type()
)
failuredescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    failuredescription.setStatus("current")


class _Suggestedrecovery_Type(OctetString):
    """Custom type suggestedrecovery based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_Suggestedrecovery_Type.__name__ = "OctetString"
_Suggestedrecovery_Object = MibScalar
suggestedrecovery = _Suggestedrecovery_Object(
    (1, 3, 6, 1, 4, 1, 37963, 1, 1, 38),
    _Suggestedrecovery_Type()
)
suggestedrecovery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    suggestedrecovery.setStatus("current")


class _Netcontext_Type(OctetString):
    """Custom type netcontext based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_Netcontext_Type.__name__ = "OctetString"
_Netcontext_Object = MibScalar
netcontext = _Netcontext_Object(
    (1, 3, 6, 1, 4, 1, 37963, 1, 1, 39),
    _Netcontext_Type()
)
netcontext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netcontext.setStatus("current")


class _Info_Type(OctetString):
    """Custom type info based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_Info_Type.__name__ = "OctetString"
_Info_Object = MibScalar
info = _Info_Object(
    (1, 3, 6, 1, 4, 1, 37963, 1, 1, 40),
    _Info_Type()
)
info.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    info.setStatus("current")


class _Nodename_Type(OctetString):
    """Custom type nodename based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_Nodename_Type.__name__ = "OctetString"
_Nodename_Object = MibScalar
nodename = _Nodename_Object(
    (1, 3, 6, 1, 4, 1, 37963, 1, 1, 41),
    _Nodename_Type()
)
nodename.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodename.setStatus("current")


class _Realmname_Type(OctetString):
    """Custom type realmname based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_Realmname_Type.__name__ = "OctetString"
_Realmname_Object = MibScalar
realmname = _Realmname_Object(
    (1, 3, 6, 1, 4, 1, 37963, 1, 1, 42),
    _Realmname_Type()
)
realmname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    realmname.setStatus("current")


class _Localhostidentity_Type(OctetString):
    """Custom type localhostidentity based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_Localhostidentity_Type.__name__ = "OctetString"
_Localhostidentity_Object = MibScalar
localhostidentity = _Localhostidentity_Object(
    (1, 3, 6, 1, 4, 1, 37963, 1, 1, 43),
    _Localhostidentity_Type()
)
localhostidentity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    localhostidentity.setStatus("current")


class _Peerrealmname_Type(OctetString):
    """Custom type peerrealmname based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_Peerrealmname_Type.__name__ = "OctetString"
_Peerrealmname_Object = MibScalar
peerrealmname = _Peerrealmname_Object(
    (1, 3, 6, 1, 4, 1, 37963, 1, 1, 44),
    _Peerrealmname_Type()
)
peerrealmname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    peerrealmname.setStatus("current")


class _Peerhostidentity_Type(OctetString):
    """Custom type peerhostidentity based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_Peerhostidentity_Type.__name__ = "OctetString"
_Peerhostidentity_Object = MibScalar
peerhostidentity = _Peerhostidentity_Object(
    (1, 3, 6, 1, 4, 1, 37963, 1, 1, 45),
    _Peerhostidentity_Type()
)
peerhostidentity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    peerhostidentity.setStatus("current")


class _Peername_Type(OctetString):
    """Custom type peername based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_Peername_Type.__name__ = "OctetString"
_Peername_Object = MibScalar
peername = _Peername_Object(
    (1, 3, 6, 1, 4, 1, 37963, 1, 1, 46),
    _Peername_Type()
)
peername.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    peername.setStatus("current")


class _Clientid_Type(OctetString):
    """Custom type clientid based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_Clientid_Type.__name__ = "OctetString"
_Clientid_Object = MibScalar
clientid = _Clientid_Object(
    (1, 3, 6, 1, 4, 1, 37963, 1, 1, 47),
    _Clientid_Type()
)
clientid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clientid.setStatus("current")


class _Servicename_Type(OctetString):
    """Custom type servicename based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_Servicename_Type.__name__ = "OctetString"
_Servicename_Object = MibScalar
servicename = _Servicename_Object(
    (1, 3, 6, 1, 4, 1, 37963, 1, 1, 48),
    _Servicename_Type()
)
servicename.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    servicename.setStatus("current")


class _Apnname_Type(OctetString):
    """Custom type apnname based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_Apnname_Type.__name__ = "OctetString"
_Apnname_Object = MibScalar
apnname = _Apnname_Object(
    (1, 3, 6, 1, 4, 1, 37963, 1, 1, 49),
    _Apnname_Type()
)
apnname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apnname.setStatus("current")


class _Imsi_Type(OctetString):
    """Custom type imsi based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_Imsi_Type.__name__ = "OctetString"
_Imsi_Object = MibScalar
imsi = _Imsi_Object(
    (1, 3, 6, 1, 4, 1, 37963, 1, 1, 50),
    _Imsi_Type()
)
imsi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imsi.setStatus("current")


class _Statestring_Type(OctetString):
    """Custom type statestring based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_Statestring_Type.__name__ = "OctetString"
_Statestring_Object = MibScalar
statestring = _Statestring_Object(
    (1, 3, 6, 1, 4, 1, 37963, 1, 1, 51),
    _Statestring_Type()
)
statestring.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statestring.setStatus("current")


class _Filepath_Type(OctetString):
    """Custom type filepath based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_Filepath_Type.__name__ = "OctetString"
_Filepath_Object = MibScalar
filepath = _Filepath_Object(
    (1, 3, 6, 1, 4, 1, 37963, 1, 1, 52),
    _Filepath_Type()
)
filepath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    filepath.setStatus("current")


class _Ip_Type(OctetString):
    """Custom type ip based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_Ip_Type.__name__ = "OctetString"
_Ip_Object = MibScalar
ip = _Ip_Object(
    (1, 3, 6, 1, 4, 1, 37963, 1, 1, 53),
    _Ip_Type()
)
ip.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ip.setStatus("current")


class _Port_Type(OctetString):
    """Custom type port based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_Port_Type.__name__ = "OctetString"
_Port_Object = MibScalar
port = _Port_Object(
    (1, 3, 6, 1, 4, 1, 37963, 1, 1, 54),
    _Port_Type()
)
port.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    port.setStatus("current")


class _Chassisid_Type(OctetString):
    """Custom type chassisid based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_Chassisid_Type.__name__ = "OctetString"
_Chassisid_Object = MibScalar
chassisid = _Chassisid_Object(
    (1, 3, 6, 1, 4, 1, 37963, 1, 1, 55),
    _Chassisid_Type()
)
chassisid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisid.setStatus("current")


class _Slotid_Type(OctetString):
    """Custom type slotid based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_Slotid_Type.__name__ = "OctetString"
_Slotid_Object = MibScalar
slotid = _Slotid_Object(
    (1, 3, 6, 1, 4, 1, 37963, 1, 1, 56),
    _Slotid_Type()
)
slotid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotid.setStatus("current")


class _Cpuid_Type(OctetString):
    """Custom type cpuid based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_Cpuid_Type.__name__ = "OctetString"
_Cpuid_Object = MibScalar
cpuid = _Cpuid_Object(
    (1, 3, 6, 1, 4, 1, 37963, 1, 1, 57),
    _Cpuid_Type()
)
cpuid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuid.setStatus("current")


class _Prefix_Type(OctetString):
    """Custom type prefix based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_Prefix_Type.__name__ = "OctetString"
_Prefix_Object = MibScalar
prefix = _Prefix_Object(
    (1, 3, 6, 1, 4, 1, 37963, 1, 1, 58),
    _Prefix_Type()
)
prefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prefix.setStatus("current")


class _Numpurged_Type(OctetString):
    """Custom type numpurged based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_Numpurged_Type.__name__ = "OctetString"
_Numpurged_Object = MibScalar
numpurged = _Numpurged_Object(
    (1, 3, 6, 1, 4, 1, 37963, 1, 1, 59),
    _Numpurged_Type()
)
numpurged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numpurged.setStatus("current")


class _Node_Type(OctetString):
    """Custom type node based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_Node_Type.__name__ = "OctetString"
_Node_Object = MibScalar
node = _Node_Object(
    (1, 3, 6, 1, 4, 1, 37963, 1, 1, 60),
    _Node_Type()
)
node.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    node.setStatus("current")


class _Diskid_Type(OctetString):
    """Custom type diskid based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_Diskid_Type.__name__ = "OctetString"
_Diskid_Object = MibScalar
diskid = _Diskid_Object(
    (1, 3, 6, 1, 4, 1, 37963, 1, 1, 61),
    _Diskid_Type()
)
diskid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskid.setStatus("current")


class _Interfacename_Type(OctetString):
    """Custom type interfacename based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_Interfacename_Type.__name__ = "OctetString"
_Interfacename_Object = MibScalar
interfacename = _Interfacename_Object(
    (1, 3, 6, 1, 4, 1, 37963, 1, 1, 62),
    _Interfacename_Type()
)
interfacename.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfacename.setStatus("current")


class _Threshold_Type(OctetString):
    """Custom type threshold based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_Threshold_Type.__name__ = "OctetString"
_Threshold_Object = MibScalar
threshold = _Threshold_Object(
    (1, 3, 6, 1, 4, 1, 37963, 1, 1, 63),
    _Threshold_Type()
)
threshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    threshold.setStatus("current")


class _Uepoolutilization_Type(OctetString):
    """Custom type uepoolutilization based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_Uepoolutilization_Type.__name__ = "OctetString"
_Uepoolutilization_Object = MibScalar
uepoolutilization = _Uepoolutilization_Object(
    (1, 3, 6, 1, 4, 1, 37963, 1, 1, 64),
    _Uepoolutilization_Type()
)
uepoolutilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uepoolutilization.setStatus("current")


class _Ipversiontype_Type(OctetString):
    """Custom type ipversiontype based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_Ipversiontype_Type.__name__ = "OctetString"
_Ipversiontype_Object = MibScalar
ipversiontype = _Ipversiontype_Object(
    (1, 3, 6, 1, 4, 1, 37963, 1, 1, 65),
    _Ipversiontype_Type()
)
ipversiontype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipversiontype.setStatus("current")


class _Ifindex_Type(OctetString):
    """Custom type ifindex based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_Ifindex_Type.__name__ = "OctetString"
_Ifindex_Object = MibScalar
ifindex = _Ifindex_Object(
    (1, 3, 6, 1, 4, 1, 37963, 1, 1, 66),
    _Ifindex_Type()
)
ifindex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifindex.setStatus("current")


class _Ifadminstatus_Type(OctetString):
    """Custom type ifadminstatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_Ifadminstatus_Type.__name__ = "OctetString"
_Ifadminstatus_Object = MibScalar
ifadminstatus = _Ifadminstatus_Object(
    (1, 3, 6, 1, 4, 1, 37963, 1, 1, 67),
    _Ifadminstatus_Type()
)
ifadminstatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifadminstatus.setStatus("current")


class _Ifoperstatus_Type(OctetString):
    """Custom type ifoperstatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_Ifoperstatus_Type.__name__ = "OctetString"
_Ifoperstatus_Object = MibScalar
ifoperstatus = _Ifoperstatus_Object(
    (1, 3, 6, 1, 4, 1, 37963, 1, 1, 68),
    _Ifoperstatus_Type()
)
ifoperstatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifoperstatus.setStatus("current")


class _Netctxtname_Type(OctetString):
    """Custom type netctxtname based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_Netctxtname_Type.__name__ = "OctetString"
_Netctxtname_Object = MibScalar
netctxtname = _Netctxtname_Object(
    (1, 3, 6, 1, 4, 1, 37963, 1, 1, 69),
    _Netctxtname_Type()
)
netctxtname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netctxtname.setStatus("current")


class _Peeringname_Type(OctetString):
    """Custom type peeringname based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_Peeringname_Type.__name__ = "OctetString"
_Peeringname_Object = MibScalar
peeringname = _Peeringname_Object(
    (1, 3, 6, 1, 4, 1, 37963, 1, 1, 70),
    _Peeringname_Type()
)
peeringname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    peeringname.setStatus("current")


class _Localpeeripaddr_Type(OctetString):
    """Custom type localpeeripaddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_Localpeeripaddr_Type.__name__ = "OctetString"
_Localpeeripaddr_Object = MibScalar
localpeeripaddr = _Localpeeripaddr_Object(
    (1, 3, 6, 1, 4, 1, 37963, 1, 1, 71),
    _Localpeeripaddr_Type()
)
localpeeripaddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    localpeeripaddr.setStatus("current")


class _Remotepeeripaddr_Type(OctetString):
    """Custom type remotepeeripaddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_Remotepeeripaddr_Type.__name__ = "OctetString"
_Remotepeeripaddr_Object = MibScalar
remotepeeripaddr = _Remotepeeripaddr_Object(
    (1, 3, 6, 1, 4, 1, 37963, 1, 1, 72),
    _Remotepeeripaddr_Type()
)
remotepeeripaddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remotepeeripaddr.setStatus("current")


class _Lasterrorcode_Type(OctetString):
    """Custom type lasterrorcode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_Lasterrorcode_Type.__name__ = "OctetString"
_Lasterrorcode_Object = MibScalar
lasterrorcode = _Lasterrorcode_Object(
    (1, 3, 6, 1, 4, 1, 37963, 1, 1, 73),
    _Lasterrorcode_Type()
)
lasterrorcode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lasterrorcode.setStatus("current")


class _Lasterrosubcode_Type(OctetString):
    """Custom type lasterrosubcode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_Lasterrosubcode_Type.__name__ = "OctetString"
_Lasterrosubcode_Object = MibScalar
lasterrosubcode = _Lasterrosubcode_Object(
    (1, 3, 6, 1, 4, 1, 37963, 1, 1, 74),
    _Lasterrosubcode_Type()
)
lasterrosubcode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lasterrosubcode.setStatus("current")


class _Currentstate_Type(OctetString):
    """Custom type currentstate based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_Currentstate_Type.__name__ = "OctetString"
_Currentstate_Object = MibScalar
currentstate = _Currentstate_Object(
    (1, 3, 6, 1, 4, 1, 37963, 1, 1, 75),
    _Currentstate_Type()
)
currentstate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentstate.setStatus("current")


class _Role_Type(OctetString):
    """Custom type role based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_Role_Type.__name__ = "OctetString"
_Role_Object = MibScalar
role = _Role_Object(
    (1, 3, 6, 1, 4, 1, 37963, 1, 1, 76),
    _Role_Type()
)
role.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    role.setStatus("current")


class _Groupname_Type(OctetString):
    """Custom type groupname based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_Groupname_Type.__name__ = "OctetString"
_Groupname_Object = MibScalar
groupname = _Groupname_Object(
    (1, 3, 6, 1, 4, 1, 37963, 1, 1, 77),
    _Groupname_Type()
)
groupname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    groupname.setStatus("current")


class _Operation_Type(OctetString):
    """Custom type operation based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_Operation_Type.__name__ = "OctetString"
_Operation_Object = MibScalar
operation = _Operation_Object(
    (1, 3, 6, 1, 4, 1, 37963, 1, 1, 78),
    _Operation_Type()
)
operation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    operation.setStatus("current")


class _State_Type(OctetString):
    """Custom type state based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_State_Type.__name__ = "OctetString"
_State_Object = MibScalar
state = _State_Object(
    (1, 3, 6, 1, 4, 1, 37963, 1, 1, 79),
    _State_Type()
)
state.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    state.setStatus("current")


class _Status_Type(OctetString):
    """Custom type status based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_Status_Type.__name__ = "OctetString"
_Status_Object = MibScalar
status = _Status_Object(
    (1, 3, 6, 1, 4, 1, 37963, 1, 1, 80),
    _Status_Type()
)
status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    status.setStatus("current")


class _Activesize_Type(OctetString):
    """Custom type activesize based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_Activesize_Type.__name__ = "OctetString"
_Activesize_Object = MibScalar
activesize = _Activesize_Object(
    (1, 3, 6, 1, 4, 1, 37963, 1, 1, 81),
    _Activesize_Type()
)
activesize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    activesize.setStatus("current")


class _Standbysize_Type(OctetString):
    """Custom type standbysize based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_Standbysize_Type.__name__ = "OctetString"
_Standbysize_Object = MibScalar
standbysize = _Standbysize_Object(
    (1, 3, 6, 1, 4, 1, 37963, 1, 1, 82),
    _Standbysize_Type()
)
standbysize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    standbysize.setStatus("current")


class _Mcmslotnumber_Type(OctetString):
    """Custom type mcmslotnumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_Mcmslotnumber_Type.__name__ = "OctetString"
_Mcmslotnumber_Object = MibScalar
mcmslotnumber = _Mcmslotnumber_Object(
    (1, 3, 6, 1, 4, 1, 37963, 1, 1, 83),
    _Mcmslotnumber_Type()
)
mcmslotnumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmslotnumber.setStatus("current")


class _Requiredsize_Type(OctetString):
    """Custom type requiredsize based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_Requiredsize_Type.__name__ = "OctetString"
_Requiredsize_Object = MibScalar
requiredsize = _Requiredsize_Object(
    (1, 3, 6, 1, 4, 1, 37963, 1, 1, 84),
    _Requiredsize_Type()
)
requiredsize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    requiredsize.setStatus("current")


class _Availablesize_Type(OctetString):
    """Custom type availablesize based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_Availablesize_Type.__name__ = "OctetString"
_Availablesize_Object = MibScalar
availablesize = _Availablesize_Object(
    (1, 3, 6, 1, 4, 1, 37963, 1, 1, 85),
    _Availablesize_Type()
)
availablesize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    availablesize.setStatus("current")


class _Reason_Type(OctetString):
    """Custom type reason based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_Reason_Type.__name__ = "OctetString"
_Reason_Object = MibScalar
reason = _Reason_Object(
    (1, 3, 6, 1, 4, 1, 37963, 1, 1, 86),
    _Reason_Type()
)
reason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reason.setStatus("current")


class _Importnum_Type(OctetString):
    """Custom type importnum based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_Importnum_Type.__name__ = "OctetString"
_Importnum_Object = MibScalar
importnum = _Importnum_Object(
    (1, 3, 6, 1, 4, 1, 37963, 1, 1, 87),
    _Importnum_Type()
)
importnum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    importnum.setStatus("current")


class _Resultstr_Type(OctetString):
    """Custom type resultstr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_Resultstr_Type.__name__ = "OctetString"
_Resultstr_Object = MibScalar
resultstr = _Resultstr_Object(
    (1, 3, 6, 1, 4, 1, 37963, 1, 1, 88),
    _Resultstr_Type()
)
resultstr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    resultstr.setStatus("current")


class _Datetime_Type(OctetString):
    """Custom type datetime based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_Datetime_Type.__name__ = "OctetString"
_Datetime_Object = MibScalar
datetime = _Datetime_Object(
    (1, 3, 6, 1, 4, 1, 37963, 1, 1, 89),
    _Datetime_Type()
)
datetime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    datetime.setStatus("current")


class _Fault_Type(OctetString):
    """Custom type fault based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_Fault_Type.__name__ = "OctetString"
_Fault_Object = MibScalar
fault = _Fault_Object(
    (1, 3, 6, 1, 4, 1, 37963, 1, 1, 90),
    _Fault_Type()
)
fault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fault.setStatus("current")


class _Action_Type(OctetString):
    """Custom type action based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_Action_Type.__name__ = "OctetString"
_Action_Object = MibScalar
action = _Action_Object(
    (1, 3, 6, 1, 4, 1, 37963, 1, 1, 91),
    _Action_Type()
)
action.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    action.setStatus("current")


class _Unused_Type(OctetString):
    """Custom type unused based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_Unused_Type.__name__ = "OctetString"
_Unused_Object = MibScalar
unused = _Unused_Object(
    (1, 3, 6, 1, 4, 1, 37963, 1, 1, 92),
    _Unused_Type()
)
unused.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unused.setStatus("current")


class _Clusterid_Type(OctetString):
    """Custom type clusterid based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_Clusterid_Type.__name__ = "OctetString"
_Clusterid_Object = MibScalar
clusterid = _Clusterid_Object(
    (1, 3, 6, 1, 4, 1, 37963, 1, 1, 93),
    _Clusterid_Type()
)
clusterid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterid.setStatus("current")


class _Nodeid_Type(OctetString):
    """Custom type nodeid based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_Nodeid_Type.__name__ = "OctetString"
_Nodeid_Object = MibScalar
nodeid = _Nodeid_Object(
    (1, 3, 6, 1, 4, 1, 37963, 1, 1, 94),
    _Nodeid_Type()
)
nodeid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeid.setStatus("current")


class _Subsgroupname_Type(OctetString):
    """Custom type subsgroupname based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_Subsgroupname_Type.__name__ = "OctetString"
_Subsgroupname_Object = MibScalar
subsgroupname = _Subsgroupname_Object(
    (1, 3, 6, 1, 4, 1, 37963, 1, 1, 95),
    _Subsgroupname_Type()
)
subsgroupname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    subsgroupname.setStatus("current")


class _Subsidfilename_Type(OctetString):
    """Custom type subsidfilename based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_Subsidfilename_Type.__name__ = "OctetString"
_Subsidfilename_Object = MibScalar
subsidfilename = _Subsidfilename_Object(
    (1, 3, 6, 1, 4, 1, 37963, 1, 1, 96),
    _Subsidfilename_Type()
)
subsidfilename.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    subsidfilename.setStatus("current")


class _Alarmid_Type(OctetString):
    """Custom type alarmid based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_Alarmid_Type.__name__ = "OctetString"
_Alarmid_Object = MibScalar
alarmid = _Alarmid_Object(
    (1, 3, 6, 1, 4, 1, 37963, 1, 1, 97),
    _Alarmid_Type()
)
alarmid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmid.setStatus("current")


class _Xpath_Type(OctetString):
    """Custom type xpath based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_Xpath_Type.__name__ = "OctetString"
_Xpath_Object = MibScalar
xpath = _Xpath_Object(
    (1, 3, 6, 1, 4, 1, 37963, 1, 1, 98),
    _Xpath_Type()
)
xpath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xpath.setStatus("current")


class _Ifname_Type(OctetString):
    """Custom type ifname based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_Ifname_Type.__name__ = "OctetString"
_Ifname_Object = MibScalar
ifname = _Ifname_Object(
    (1, 3, 6, 1, 4, 1, 37963, 1, 1, 99),
    _Ifname_Type()
)
ifname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifname.setStatus("current")


class _Sessionthreshold_Type(OctetString):
    """Custom type sessionthreshold based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_Sessionthreshold_Type.__name__ = "OctetString"
_Sessionthreshold_Object = MibScalar
sessionthreshold = _Sessionthreshold_Object(
    (1, 3, 6, 1, 4, 1, 37963, 1, 1, 100),
    _Sessionthreshold_Type()
)
sessionthreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionthreshold.setStatus("current")


class _Sessionutilization_Type(OctetString):
    """Custom type sessionutilization based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_Sessionutilization_Type.__name__ = "OctetString"
_Sessionutilization_Object = MibScalar
sessionutilization = _Sessionutilization_Object(
    (1, 3, 6, 1, 4, 1, 37963, 1, 1, 101),
    _Sessionutilization_Type()
)
sessionutilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionutilization.setStatus("current")


class _Ipaddressthreshold_Type(OctetString):
    """Custom type ipaddressthreshold based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_Ipaddressthreshold_Type.__name__ = "OctetString"
_Ipaddressthreshold_Object = MibScalar
ipaddressthreshold = _Ipaddressthreshold_Object(
    (1, 3, 6, 1, 4, 1, 37963, 1, 1, 102),
    _Ipaddressthreshold_Type()
)
ipaddressthreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipaddressthreshold.setStatus("current")


class _Ipaddressutilization_Type(OctetString):
    """Custom type ipaddressutilization based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_Ipaddressutilization_Type.__name__ = "OctetString"
_Ipaddressutilization_Object = MibScalar
ipaddressutilization = _Ipaddressutilization_Object(
    (1, 3, 6, 1, 4, 1, 37963, 1, 1, 103),
    _Ipaddressutilization_Type()
)
ipaddressutilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipaddressutilization.setStatus("current")


class _Portchunkthreshold_Type(OctetString):
    """Custom type portchunkthreshold based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_Portchunkthreshold_Type.__name__ = "OctetString"
_Portchunkthreshold_Object = MibScalar
portchunkthreshold = _Portchunkthreshold_Object(
    (1, 3, 6, 1, 4, 1, 37963, 1, 1, 104),
    _Portchunkthreshold_Type()
)
portchunkthreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portchunkthreshold.setStatus("current")


class _Portchunkutilization_Type(OctetString):
    """Custom type portchunkutilization based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_Portchunkutilization_Type.__name__ = "OctetString"
_Portchunkutilization_Object = MibScalar
portchunkutilization = _Portchunkutilization_Object(
    (1, 3, 6, 1, 4, 1, 37963, 1, 1, 105),
    _Portchunkutilization_Type()
)
portchunkutilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portchunkutilization.setStatus("current")


class _Parent_Type(OctetString):
    """Custom type parent based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_Parent_Type.__name__ = "OctetString"
_Parent_Object = MibScalar
parent = _Parent_Object(
    (1, 3, 6, 1, 4, 1, 37963, 1, 1, 106),
    _Parent_Type()
)
parent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    parent.setStatus("current")


class _Destination_Type(OctetString):
    """Custom type destination based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_Destination_Type.__name__ = "OctetString"
_Destination_Object = MibScalar
destination = _Destination_Object(
    (1, 3, 6, 1, 4, 1, 37963, 1, 1, 107),
    _Destination_Type()
)
destination.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    destination.setStatus("current")


class _Peeripaddress_Type(OctetString):
    """Custom type peeripaddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_Peeripaddress_Type.__name__ = "OctetString"
_Peeripaddress_Object = MibScalar
peeripaddress = _Peeripaddress_Object(
    (1, 3, 6, 1, 4, 1, 37963, 1, 1, 108),
    _Peeripaddress_Type()
)
peeripaddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    peeripaddress.setStatus("current")


class _Gatewayname_Type(OctetString):
    """Custom type gatewayname based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_Gatewayname_Type.__name__ = "OctetString"
_Gatewayname_Object = MibScalar
gatewayname = _Gatewayname_Object(
    (1, 3, 6, 1, 4, 1, 37963, 1, 1, 109),
    _Gatewayname_Type()
)
gatewayname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gatewayname.setStatus("current")


class _Gatewayipaddress_Type(OctetString):
    """Custom type gatewayipaddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_Gatewayipaddress_Type.__name__ = "OctetString"
_Gatewayipaddress_Object = MibScalar
gatewayipaddress = _Gatewayipaddress_Object(
    (1, 3, 6, 1, 4, 1, 37963, 1, 1, 110),
    _Gatewayipaddress_Type()
)
gatewayipaddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gatewayipaddress.setStatus("current")


class _Bfdsessiondescription_Type(OctetString):
    """Custom type bfdsessiondescription based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_Bfdsessiondescription_Type.__name__ = "OctetString"
_Bfdsessiondescription_Object = MibScalar
bfdsessiondescription = _Bfdsessiondescription_Object(
    (1, 3, 6, 1, 4, 1, 37963, 1, 1, 111),
    _Bfdsessiondescription_Type()
)
bfdsessiondescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bfdsessiondescription.setStatus("current")


class _Cafilename_Type(OctetString):
    """Custom type cafilename based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_Cafilename_Type.__name__ = "OctetString"
_Cafilename_Object = MibScalar
cafilename = _Cafilename_Object(
    (1, 3, 6, 1, 4, 1, 37963, 1, 1, 112),
    _Cafilename_Type()
)
cafilename.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cafilename.setStatus("current")


class _Expirydate_Type(OctetString):
    """Custom type expirydate based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_Expirydate_Type.__name__ = "OctetString"
_Expirydate_Object = MibScalar
expirydate = _Expirydate_Object(
    (1, 3, 6, 1, 4, 1, 37963, 1, 1, 113),
    _Expirydate_Type()
)
expirydate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expirydate.setStatus("current")


class _Index_Type(OctetString):
    """Custom type index based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_Index_Type.__name__ = "OctetString"
_Index_Object = MibScalar
index = _Index_Object(
    (1, 3, 6, 1, 4, 1, 37963, 1, 1, 114),
    _Index_Type()
)
index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    index.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AFFIRMED-ALARM-MIB",
    **{"affirmedAlarmObjects": affirmedAlarmObjects,
       "affirmedAlarmSeqId": affirmedAlarmSeqId,
       "affirmedAlarmDateTime": affirmedAlarmDateTime,
       "affirmedAlarmChassisName": affirmedAlarmChassisName,
       "affirmedAlarmSourceId": affirmedAlarmSourceId,
       "affirmedAlarmSeverity": affirmedAlarmSeverity,
       "affirmedAlarmRefSeqId": affirmedAlarmRefSeqId,
       "affirmedAlarmDetails": affirmedAlarmDetails,
       "affirmedPotentialImpact": affirmedPotentialImpact,
       "affirmedCorrectiveAction": affirmedCorrectiveAction,
       "affirmedVmSourceIpAddress": affirmedVmSourceIpAddress,
       "affirmedVmSourceName": affirmedVmSourceName,
       "name": name,
       "chassis": chassis,
       "slot": slot,
       "cpu": cpu,
       "dirname": dirname,
       "adminstate": adminstate,
       "resource": resource,
       "sensor": sensor,
       "data": data,
       "taskname": taskname,
       "cid": cid,
       "sid": sid,
       "type": type,
       "subtype": subtype,
       "level": level,
       "time": time,
       "services": services,
       "actions": actions,
       "ledname": ledname,
       "ledcolor": ledcolor,
       "usid": usid,
       "hardorsoft": hardorsoft,
       "readerrors": readerrors,
       "writeerrors": writeerrors,
       "slotnumber": slotnumber,
       "failuredescription": failuredescription,
       "suggestedrecovery": suggestedrecovery,
       "netcontext": netcontext,
       "info": info,
       "nodename": nodename,
       "realmname": realmname,
       "localhostidentity": localhostidentity,
       "peerrealmname": peerrealmname,
       "peerhostidentity": peerhostidentity,
       "peername": peername,
       "clientid": clientid,
       "servicename": servicename,
       "apnname": apnname,
       "imsi": imsi,
       "statestring": statestring,
       "filepath": filepath,
       "ip": ip,
       "port": port,
       "chassisid": chassisid,
       "slotid": slotid,
       "cpuid": cpuid,
       "prefix": prefix,
       "numpurged": numpurged,
       "node": node,
       "diskid": diskid,
       "interfacename": interfacename,
       "threshold": threshold,
       "uepoolutilization": uepoolutilization,
       "ipversiontype": ipversiontype,
       "ifindex": ifindex,
       "ifadminstatus": ifadminstatus,
       "ifoperstatus": ifoperstatus,
       "netctxtname": netctxtname,
       "peeringname": peeringname,
       "localpeeripaddr": localpeeripaddr,
       "remotepeeripaddr": remotepeeripaddr,
       "lasterrorcode": lasterrorcode,
       "lasterrosubcode": lasterrosubcode,
       "currentstate": currentstate,
       "role": role,
       "groupname": groupname,
       "operation": operation,
       "state": state,
       "status": status,
       "activesize": activesize,
       "standbysize": standbysize,
       "mcmslotnumber": mcmslotnumber,
       "requiredsize": requiredsize,
       "availablesize": availablesize,
       "reason": reason,
       "importnum": importnum,
       "resultstr": resultstr,
       "datetime": datetime,
       "fault": fault,
       "action": action,
       "unused": unused,
       "clusterid": clusterid,
       "nodeid": nodeid,
       "subsgroupname": subsgroupname,
       "subsidfilename": subsidfilename,
       "alarmid": alarmid,
       "xpath": xpath,
       "ifname": ifname,
       "sessionthreshold": sessionthreshold,
       "sessionutilization": sessionutilization,
       "ipaddressthreshold": ipaddressthreshold,
       "ipaddressutilization": ipaddressutilization,
       "portchunkthreshold": portchunkthreshold,
       "portchunkutilization": portchunkutilization,
       "parent": parent,
       "destination": destination,
       "peeripaddress": peeripaddress,
       "gatewayname": gatewayname,
       "gatewayipaddress": gatewayipaddress,
       "bfdsessiondescription": bfdsessiondescription,
       "cafilename": cafilename,
       "expirydate": expirydate,
       "index": index,
       "affirmedAlarmMIB": affirmedAlarmMIB}
)
