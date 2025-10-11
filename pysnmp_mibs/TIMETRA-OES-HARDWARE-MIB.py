# SNMP MIB module (TIMETRA-OES-HARDWARE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/nokia/TIMETRA-OES-HARDWARE-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:52:29 2025
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

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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

(DateAndTime,
 DisplayString,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")

(TmnxCardRebootType,
 TmnxDeviceState,
 TmnxHwIndex,
 TmnxLEDState,
 TmnxPhysChassisIndex,
 tmnxHwClass,
 tmnxHwIndex) = mibBuilder.importSymbols(
    "TIMETRA-CHASSIS-MIB",
    "TmnxCardRebootType",
    "TmnxDeviceState",
    "TmnxHwIndex",
    "TmnxLEDState",
    "TmnxPhysChassisIndex",
    "tmnxHwClass",
    "tmnxHwIndex")

(timetraSRMIBModules,
 tmnxSRConfs,
 tmnxSRNotifyPrefix,
 tmnxSRObjs) = mibBuilder.importSymbols(
    "TIMETRA-GLOBAL-MIB",
    "timetraSRMIBModules",
    "tmnxSRConfs",
    "tmnxSRNotifyPrefix",
    "tmnxSRObjs")

(TmnxPortOperStatus,
 tmnxPortNotifyPortId) = mibBuilder.importSymbols(
    "TIMETRA-PORT-MIB",
    "TmnxPortOperStatus",
    "tmnxPortNotifyPortId")

(TItemDescription,
 TNamedItem,
 TNamedItemOrEmpty,
 TmnxActionType,
 TmnxAdminState,
 TmnxOperState) = mibBuilder.importSymbols(
    "TIMETRA-TC-MIB",
    "TItemDescription",
    "TNamedItem",
    "TNamedItemOrEmpty",
    "TmnxActionType",
    "TmnxAdminState",
    "TmnxOperState")


# MODULE-IDENTITY

timetraOesHardwareMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 1, 3, 99)
)
if mibBuilder.loadTexts:
    timetraOesHardwareMIBModule.setRevisions(
        ("2013-08-01 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class TmnxOesCardHFD(SnmpAdminString):
    status = "current"
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2),
    )



class TmnxOesHwMktPartNo(SnmpAdminString):
    status = "current"
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )



class TmnxOesHwSWGenLoadName(SnmpAdminString):
    status = "current"
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )



class TmnxOesHwLEDColorType(TextualConvention, Integer32):
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
        *(("unknown", 1),
          ("off", 2),
          ("red", 3),
          ("green", 4),
          ("orange", 5))
    )



class TmnxOesHwLEDStateType(TextualConvention, Integer32):
    status = "current"
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
        *(("unknown", 1),
          ("solid", 2),
          ("fastBlink", 3),
          ("slowBlink", 4))
    )



class TmnxOesSlotNumber(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 40),
    )



class TmnxOesChassisType(TextualConvention, Unsigned32):
    status = "current"


class TmnxOesCardType(TextualConvention, Unsigned32):
    status = "current"


class TmnxOesCardSuppType(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("invalid-card-type", 0),
          ("unassigned", 1),
          ("oes-supp-card-type-2", 2),
          ("oes-supp-card-type-3", 3),
          ("oes-supp-card-type-4", 4),
          ("oes-supp-card-type-5", 5),
          ("oes-supp-card-type-6", 6),
          ("oes-supp-card-type-7", 7),
          ("oes-supp-card-type-8", 8))
    )


class TmnxOesCmnEqpPortNumber(TextualConvention, Unsigned32):
    status = "current"


class TmnxOesPortErrorStatus(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("deviceFailure", 0),
          ("transmissionFailure", 1))
    )


# MIB Managed Objects in the order of their OIDs

_TmnxOesHwConformance_ObjectIdentity = ObjectIdentity
tmnxOesHwConformance = _TmnxOesHwConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 99)
)
_TmnxOesHwCompliances_ObjectIdentity = ObjectIdentity
tmnxOesHwCompliances = _TmnxOesHwCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 99, 1)
)
_TmnxOesHwGroups_ObjectIdentity = ObjectIdentity
tmnxOesHwGroups = _TmnxOesHwGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 99, 2)
)
_TmnxOesHwV14v0Groups_ObjectIdentity = ObjectIdentity
tmnxOesHwV14v0Groups = _TmnxOesHwV14v0Groups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 99, 2, 1)
)
_TmnxOesHwObjs_ObjectIdentity = ObjectIdentity
tmnxOesHwObjs = _TmnxOesHwObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 99)
)
_TmnxOesChassisObjs_ObjectIdentity = ObjectIdentity
tmnxOesChassisObjs = _TmnxOesChassisObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 99, 1)
)
_TmnxOesChassisTypeTable_Object = MibTable
tmnxOesChassisTypeTable = _TmnxOesChassisTypeTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 99, 1, 1)
)
if mibBuilder.loadTexts:
    tmnxOesChassisTypeTable.setStatus("current")
_TmnxOesChassisTypeEntry_Object = MibTableRow
tmnxOesChassisTypeEntry = _TmnxOesChassisTypeEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 99, 1, 1, 1)
)
tmnxOesChassisTypeEntry.setIndexNames(
    (0, "TIMETRA-OES-HARDWARE-MIB", "tmnxOesChassisTypeIndex"),
)
if mibBuilder.loadTexts:
    tmnxOesChassisTypeEntry.setStatus("current")
_TmnxOesChassisTypeIndex_Type = TmnxOesChassisType
_TmnxOesChassisTypeIndex_Object = MibTableColumn
tmnxOesChassisTypeIndex = _TmnxOesChassisTypeIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 99, 1, 1, 1, 1),
    _TmnxOesChassisTypeIndex_Type()
)
tmnxOesChassisTypeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxOesChassisTypeIndex.setStatus("current")
_TmnxOesChassisTypeName_Type = TNamedItemOrEmpty
_TmnxOesChassisTypeName_Object = MibTableColumn
tmnxOesChassisTypeName = _TmnxOesChassisTypeName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 99, 1, 1, 1, 2),
    _TmnxOesChassisTypeName_Type()
)
tmnxOesChassisTypeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOesChassisTypeName.setStatus("current")
_TmnxOesChassisTypeDescription_Type = TItemDescription
_TmnxOesChassisTypeDescription_Object = MibTableColumn
tmnxOesChassisTypeDescription = _TmnxOesChassisTypeDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 99, 1, 1, 1, 3),
    _TmnxOesChassisTypeDescription_Type()
)
tmnxOesChassisTypeDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOesChassisTypeDescription.setStatus("current")
_TmnxOesChassisTypeStatus_Type = TruthValue
_TmnxOesChassisTypeStatus_Object = MibTableColumn
tmnxOesChassisTypeStatus = _TmnxOesChassisTypeStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 99, 1, 1, 1, 4),
    _TmnxOesChassisTypeStatus_Type()
)
tmnxOesChassisTypeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOesChassisTypeStatus.setStatus("current")
_TmnxOesChassisLastChange_Type = TimeStamp
_TmnxOesChassisLastChange_Object = MibScalar
tmnxOesChassisLastChange = _TmnxOesChassisLastChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 99, 1, 2),
    _TmnxOesChassisLastChange_Type()
)
tmnxOesChassisLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOesChassisLastChange.setStatus("current")
_TmnxOesChassisTable_Object = MibTable
tmnxOesChassisTable = _TmnxOesChassisTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 99, 1, 3)
)
if mibBuilder.loadTexts:
    tmnxOesChassisTable.setStatus("current")
_TmnxOesChassisEntry_Object = MibTableRow
tmnxOesChassisEntry = _TmnxOesChassisEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 99, 1, 3, 1)
)
tmnxOesChassisEntry.setIndexNames(
    (0, "TIMETRA-OES-HARDWARE-MIB", "tmnxOesChassisNumber"),
)
if mibBuilder.loadTexts:
    tmnxOesChassisEntry.setStatus("current")
_TmnxOesChassisNumber_Type = TmnxPhysChassisIndex
_TmnxOesChassisNumber_Object = MibTableColumn
tmnxOesChassisNumber = _TmnxOesChassisNumber_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 99, 1, 3, 1, 1),
    _TmnxOesChassisNumber_Type()
)
tmnxOesChassisNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxOesChassisNumber.setStatus("current")
_TmnxOesChassisRowStatus_Type = RowStatus
_TmnxOesChassisRowStatus_Object = MibTableColumn
tmnxOesChassisRowStatus = _TmnxOesChassisRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 99, 1, 3, 1, 2),
    _TmnxOesChassisRowStatus_Type()
)
tmnxOesChassisRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOesChassisRowStatus.setStatus("current")
_TmnxOesChassisRowLastChanged_Type = TimeStamp
_TmnxOesChassisRowLastChanged_Object = MibTableColumn
tmnxOesChassisRowLastChanged = _TmnxOesChassisRowLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 99, 1, 3, 1, 3),
    _TmnxOesChassisRowLastChanged_Type()
)
tmnxOesChassisRowLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOesChassisRowLastChanged.setStatus("current")


class _TmnxOesChassisAssignedType_Type(TmnxOesChassisType):
    """Custom type tmnxOesChassisAssignedType based on TmnxOesChassisType"""
    defaultValue = 1


_TmnxOesChassisAssignedType_Type.__name__ = "TmnxOesChassisType"
_TmnxOesChassisAssignedType_Object = MibTableColumn
tmnxOesChassisAssignedType = _TmnxOesChassisAssignedType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 99, 1, 3, 1, 4),
    _TmnxOesChassisAssignedType_Type()
)
tmnxOesChassisAssignedType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOesChassisAssignedType.setStatus("current")
_TmnxOesChassisEquippedType_Type = TmnxOesChassisType
_TmnxOesChassisEquippedType_Object = MibTableColumn
tmnxOesChassisEquippedType = _TmnxOesChassisEquippedType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 99, 1, 3, 1, 5),
    _TmnxOesChassisEquippedType_Type()
)
tmnxOesChassisEquippedType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOesChassisEquippedType.setStatus("current")


class _TmnxOesChassisActivitySwitch_Type(TmnxActionType):
    """Custom type tmnxOesChassisActivitySwitch based on TmnxActionType"""
    defaultValue = 2


_TmnxOesChassisActivitySwitch_Type.__name__ = "TmnxActionType"
_TmnxOesChassisActivitySwitch_Object = MibTableColumn
tmnxOesChassisActivitySwitch = _TmnxOesChassisActivitySwitch_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 99, 1, 3, 1, 6),
    _TmnxOesChassisActivitySwitch_Type()
)
tmnxOesChassisActivitySwitch.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxOesChassisActivitySwitch.setStatus("current")
_TmnxOesChassisHwEntryIndex_Type = TmnxHwIndex
_TmnxOesChassisHwEntryIndex_Object = MibTableColumn
tmnxOesChassisHwEntryIndex = _TmnxOesChassisHwEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 99, 1, 3, 1, 7),
    _TmnxOesChassisHwEntryIndex_Type()
)
tmnxOesChassisHwEntryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOesChassisHwEntryIndex.setStatus("current")
_TmnxOesPFTable_Object = MibTable
tmnxOesPFTable = _TmnxOesPFTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 99, 1, 4)
)
if mibBuilder.loadTexts:
    tmnxOesPFTable.setStatus("current")
_TmnxOesPFEntry_Object = MibTableRow
tmnxOesPFEntry = _TmnxOesPFEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 99, 1, 4, 1)
)
tmnxOesPFEntry.setIndexNames(
    (0, "TIMETRA-OES-HARDWARE-MIB", "tmnxOesChassisNumber"),
    (0, "TIMETRA-OES-HARDWARE-MIB", "tmnxOesSlotNumber"),
)
if mibBuilder.loadTexts:
    tmnxOesPFEntry.setStatus("current")
_TmnxOesSlotNumber_Type = TmnxOesSlotNumber
_TmnxOesSlotNumber_Object = MibTableColumn
tmnxOesSlotNumber = _TmnxOesSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 99, 1, 4, 1, 1),
    _TmnxOesSlotNumber_Type()
)
tmnxOesSlotNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxOesSlotNumber.setStatus("current")


class _TmnxOesPFType_Type(Integer32):
    """Custom type tmnxOesPFType based on Integer32"""
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


_TmnxOesPFType_Type.__name__ = "Integer32"
_TmnxOesPFType_Object = MibTableColumn
tmnxOesPFType = _TmnxOesPFType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 99, 1, 4, 1, 2),
    _TmnxOesPFType_Type()
)
tmnxOesPFType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOesPFType.setStatus("current")
_TmnxOesPFAmpRating_Type = Unsigned32
_TmnxOesPFAmpRating_Object = MibTableColumn
tmnxOesPFAmpRating = _TmnxOesPFAmpRating_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 99, 1, 4, 1, 3),
    _TmnxOesPFAmpRating_Type()
)
tmnxOesPFAmpRating.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOesPFAmpRating.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOesPFAmpRating.setUnits("deci-amps")
_TmnxOesPFInputCurrent_Type = Unsigned32
_TmnxOesPFInputCurrent_Object = MibTableColumn
tmnxOesPFInputCurrent = _TmnxOesPFInputCurrent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 99, 1, 4, 1, 4),
    _TmnxOesPFInputCurrent_Type()
)
tmnxOesPFInputCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOesPFInputCurrent.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOesPFInputCurrent.setUnits("milli-amps")
_TmnxOesPFInputVoltage_Type = Unsigned32
_TmnxOesPFInputVoltage_Object = MibTableColumn
tmnxOesPFInputVoltage = _TmnxOesPFInputVoltage_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 99, 1, 4, 1, 5),
    _TmnxOesPFInputVoltage_Type()
)
tmnxOesPFInputVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOesPFInputVoltage.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOesPFInputVoltage.setUnits("milli-volts")
_TmnxOesPFInputPower_Type = Unsigned32
_TmnxOesPFInputPower_Object = MibTableColumn
tmnxOesPFInputPower = _TmnxOesPFInputPower_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 99, 1, 4, 1, 6),
    _TmnxOesPFInputPower_Type()
)
tmnxOesPFInputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOesPFInputPower.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOesPFInputPower.setUnits("watts")
_TmnxOesPFClkA_Type = Unsigned32
_TmnxOesPFClkA_Object = MibTableColumn
tmnxOesPFClkA = _TmnxOesPFClkA_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 99, 1, 4, 1, 7),
    _TmnxOesPFClkA_Type()
)
tmnxOesPFClkA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOesPFClkA.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOesPFClkA.setUnits("1/10 parts-per-million")
_TmnxOesPFClkB_Type = Unsigned32
_TmnxOesPFClkB_Object = MibTableColumn
tmnxOesPFClkB = _TmnxOesPFClkB_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 99, 1, 4, 1, 8),
    _TmnxOesPFClkB_Type()
)
tmnxOesPFClkB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOesPFClkB.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOesPFClkB.setUnits("1/10 parts-per-million")
_TmnxOesPFClkDelta_Type = Integer32
_TmnxOesPFClkDelta_Object = MibTableColumn
tmnxOesPFClkDelta = _TmnxOesPFClkDelta_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 99, 1, 4, 1, 9),
    _TmnxOesPFClkDelta_Type()
)
tmnxOesPFClkDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOesPFClkDelta.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOesPFClkDelta.setUnits("1/10 parts-per-million")
_TmnxOesPFState_Type = TmnxDeviceState
_TmnxOesPFState_Object = MibTableColumn
tmnxOesPFState = _TmnxOesPFState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 99, 1, 4, 1, 10),
    _TmnxOesPFState_Type()
)
tmnxOesPFState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOesPFState.setStatus("current")
_TmnxOesPFHwIndex_Type = TmnxHwIndex
_TmnxOesPFHwIndex_Object = MibTableColumn
tmnxOesPFHwIndex = _TmnxOesPFHwIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 99, 1, 4, 1, 11),
    _TmnxOesPFHwIndex_Type()
)
tmnxOesPFHwIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOesPFHwIndex.setStatus("current")
_TmnxOesFanLastChg_Type = TimeStamp
_TmnxOesFanLastChg_Object = MibScalar
tmnxOesFanLastChg = _TmnxOesFanLastChg_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 99, 1, 5),
    _TmnxOesFanLastChg_Type()
)
tmnxOesFanLastChg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOesFanLastChg.setStatus("current")
_TmnxOesFanTable_Object = MibTable
tmnxOesFanTable = _TmnxOesFanTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 99, 1, 6)
)
if mibBuilder.loadTexts:
    tmnxOesFanTable.setStatus("current")
_TmnxOesFanEntry_Object = MibTableRow
tmnxOesFanEntry = _TmnxOesFanEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 99, 1, 6, 1)
)
tmnxOesFanEntry.setIndexNames(
    (0, "TIMETRA-OES-HARDWARE-MIB", "tmnxOesChassisNumber"),
    (0, "TIMETRA-OES-HARDWARE-MIB", "tmnxOesFanSlotNumber"),
)
if mibBuilder.loadTexts:
    tmnxOesFanEntry.setStatus("current")
_TmnxOesFanSlotNumber_Type = TmnxOesSlotNumber
_TmnxOesFanSlotNumber_Object = MibTableColumn
tmnxOesFanSlotNumber = _TmnxOesFanSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 99, 1, 6, 1, 1),
    _TmnxOesFanSlotNumber_Type()
)
tmnxOesFanSlotNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxOesFanSlotNumber.setStatus("current")
_TmnxOesFanState_Type = TmnxDeviceState
_TmnxOesFanState_Object = MibTableColumn
tmnxOesFanState = _TmnxOesFanState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 99, 1, 6, 1, 2),
    _TmnxOesFanState_Type()
)
tmnxOesFanState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOesFanState.setStatus("current")


class _TmnxOesFanSpeedControl_Type(Integer32):
    """Custom type tmnxOesFanSpeedControl based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("maximum", 2))
    )


_TmnxOesFanSpeedControl_Type.__name__ = "Integer32"
_TmnxOesFanSpeedControl_Object = MibTableColumn
tmnxOesFanSpeedControl = _TmnxOesFanSpeedControl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 99, 1, 6, 1, 3),
    _TmnxOesFanSpeedControl_Type()
)
tmnxOesFanSpeedControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxOesFanSpeedControl.setStatus("current")
_TmnxOesFanHwIndex_Type = TmnxHwIndex
_TmnxOesFanHwIndex_Object = MibTableColumn
tmnxOesFanHwIndex = _TmnxOesFanHwIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 99, 1, 6, 1, 4),
    _TmnxOesFanHwIndex_Type()
)
tmnxOesFanHwIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOesFanHwIndex.setStatus("current")
_TmnxOesCardObjs_ObjectIdentity = ObjectIdentity
tmnxOesCardObjs = _TmnxOesCardObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 99, 2)
)
_TmnxOesCardTypeTable_Object = MibTable
tmnxOesCardTypeTable = _TmnxOesCardTypeTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 99, 2, 1)
)
if mibBuilder.loadTexts:
    tmnxOesCardTypeTable.setStatus("current")
_TmnxOesCardTypeEntry_Object = MibTableRow
tmnxOesCardTypeEntry = _TmnxOesCardTypeEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 99, 2, 1, 1)
)
tmnxOesCardTypeEntry.setIndexNames(
    (0, "TIMETRA-OES-HARDWARE-MIB", "tmnxOesCardTypeIndex"),
)
if mibBuilder.loadTexts:
    tmnxOesCardTypeEntry.setStatus("current")
_TmnxOesCardTypeIndex_Type = TmnxOesCardType
_TmnxOesCardTypeIndex_Object = MibTableColumn
tmnxOesCardTypeIndex = _TmnxOesCardTypeIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 99, 2, 1, 1, 1),
    _TmnxOesCardTypeIndex_Type()
)
tmnxOesCardTypeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxOesCardTypeIndex.setStatus("current")


class _TmnxOesCardTypeName_Type(SnmpAdminString):
    """Custom type tmnxOesCardTypeName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_TmnxOesCardTypeName_Type.__name__ = "SnmpAdminString"
_TmnxOesCardTypeName_Object = MibTableColumn
tmnxOesCardTypeName = _TmnxOesCardTypeName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 99, 2, 1, 1, 2),
    _TmnxOesCardTypeName_Type()
)
tmnxOesCardTypeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOesCardTypeName.setStatus("current")


class _TmnxOesCardTypeDescription_Type(SnmpAdminString):
    """Custom type tmnxOesCardTypeDescription based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TmnxOesCardTypeDescription_Type.__name__ = "SnmpAdminString"
_TmnxOesCardTypeDescription_Object = MibTableColumn
tmnxOesCardTypeDescription = _TmnxOesCardTypeDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 99, 2, 1, 1, 3),
    _TmnxOesCardTypeDescription_Type()
)
tmnxOesCardTypeDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOesCardTypeDescription.setStatus("current")
_TmnxOesCardTypeStatus_Type = TruthValue
_TmnxOesCardTypeStatus_Object = MibTableColumn
tmnxOesCardTypeStatus = _TmnxOesCardTypeStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 99, 2, 1, 1, 4),
    _TmnxOesCardTypeStatus_Type()
)
tmnxOesCardTypeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOesCardTypeStatus.setStatus("current")
_TmnxOesCardTypeHeight_Type = Unsigned32
_TmnxOesCardTypeHeight_Object = MibTableColumn
tmnxOesCardTypeHeight = _TmnxOesCardTypeHeight_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 99, 2, 1, 1, 5),
    _TmnxOesCardTypeHeight_Type()
)
tmnxOesCardTypeHeight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOesCardTypeHeight.setStatus("current")
_TmnxOesCardTypeWidth_Type = Unsigned32
_TmnxOesCardTypeWidth_Object = MibTableColumn
tmnxOesCardTypeWidth = _TmnxOesCardTypeWidth_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 99, 2, 1, 1, 6),
    _TmnxOesCardTypeWidth_Type()
)
tmnxOesCardTypeWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOesCardTypeWidth.setStatus("current")
_TmnxOesCardTypeNumPorts_Type = Unsigned32
_TmnxOesCardTypeNumPorts_Object = MibTableColumn
tmnxOesCardTypeNumPorts = _TmnxOesCardTypeNumPorts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 99, 2, 1, 1, 7),
    _TmnxOesCardTypeNumPorts_Type()
)
tmnxOesCardTypeNumPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOesCardTypeNumPorts.setStatus("current")
_TmnxOesCardLastChange_Type = TimeStamp
_TmnxOesCardLastChange_Object = MibScalar
tmnxOesCardLastChange = _TmnxOesCardLastChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 99, 2, 2),
    _TmnxOesCardLastChange_Type()
)
tmnxOesCardLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOesCardLastChange.setStatus("current")
_TmnxOesCardTable_Object = MibTable
tmnxOesCardTable = _TmnxOesCardTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 99, 2, 3)
)
if mibBuilder.loadTexts:
    tmnxOesCardTable.setStatus("current")
_TmnxOesCardEntry_Object = MibTableRow
tmnxOesCardEntry = _TmnxOesCardEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 99, 2, 3, 1)
)
tmnxOesCardEntry.setIndexNames(
    (0, "TIMETRA-OES-HARDWARE-MIB", "tmnxOesChassisNumber"),
    (0, "TIMETRA-OES-HARDWARE-MIB", "tmnxOesSlotNumber"),
)
if mibBuilder.loadTexts:
    tmnxOesCardEntry.setStatus("current")


class _TmnxOesCardAssignedType_Type(TmnxOesCardType):
    """Custom type tmnxOesCardAssignedType based on TmnxOesCardType"""
    defaultValue = 2


_TmnxOesCardAssignedType_Type.__name__ = "TmnxOesCardType"
_TmnxOesCardAssignedType_Object = MibTableColumn
tmnxOesCardAssignedType = _TmnxOesCardAssignedType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 99, 2, 3, 1, 1),
    _TmnxOesCardAssignedType_Type()
)
tmnxOesCardAssignedType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxOesCardAssignedType.setStatus("current")
_TmnxOesCardEquippedType_Type = TmnxOesCardType
_TmnxOesCardEquippedType_Object = MibTableColumn
tmnxOesCardEquippedType = _TmnxOesCardEquippedType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 99, 2, 3, 1, 2),
    _TmnxOesCardEquippedType_Type()
)
tmnxOesCardEquippedType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOesCardEquippedType.setStatus("current")
_TmnxOesCardSupportedTypes_Type = TmnxOesCardSuppType
_TmnxOesCardSupportedTypes_Object = MibTableColumn
tmnxOesCardSupportedTypes = _TmnxOesCardSupportedTypes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 99, 2, 3, 1, 3),
    _TmnxOesCardSupportedTypes_Type()
)
tmnxOesCardSupportedTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOesCardSupportedTypes.setStatus("current")


class _TmnxOesCardReboot_Type(TmnxCardRebootType):
    """Custom type tmnxOesCardReboot based on TmnxCardRebootType"""
    defaultValue = 2


_TmnxOesCardReboot_Type.__name__ = "TmnxCardRebootType"
_TmnxOesCardReboot_Object = MibTableColumn
tmnxOesCardReboot = _TmnxOesCardReboot_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 99, 2, 3, 1, 4),
    _TmnxOesCardReboot_Type()
)
tmnxOesCardReboot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxOesCardReboot.setStatus("current")
_TmnxOesCardHwEntryIndex_Type = TmnxHwIndex
_TmnxOesCardHwEntryIndex_Object = MibTableColumn
tmnxOesCardHwEntryIndex = _TmnxOesCardHwEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 99, 2, 3, 1, 5),
    _TmnxOesCardHwEntryIndex_Type()
)
tmnxOesCardHwEntryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOesCardHwEntryIndex.setStatus("current")
_TmnxOesCardRowLastChanged_Type = TimeStamp
_TmnxOesCardRowLastChanged_Object = MibTableColumn
tmnxOesCardRowLastChanged = _TmnxOesCardRowLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 99, 2, 3, 1, 6),
    _TmnxOesCardRowLastChanged_Type()
)
tmnxOesCardRowLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOesCardRowLastChanged.setStatus("current")
_TmnxOesCardMemorySize_Type = Unsigned32
_TmnxOesCardMemorySize_Object = MibTableColumn
tmnxOesCardMemorySize = _TmnxOesCardMemorySize_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 99, 2, 3, 1, 7),
    _TmnxOesCardMemorySize_Type()
)
tmnxOesCardMemorySize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOesCardMemorySize.setStatus("current")
if mibBuilder.loadTexts:
    tmnxOesCardMemorySize.setUnits("Giga-bytes")
_TmnxOesControlCardTable_Object = MibTable
tmnxOesControlCardTable = _TmnxOesControlCardTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 99, 2, 4)
)
if mibBuilder.loadTexts:
    tmnxOesControlCardTable.setStatus("current")
_TmnxOesControlCardEntry_Object = MibTableRow
tmnxOesControlCardEntry = _TmnxOesControlCardEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 99, 2, 4, 1)
)
tmnxOesControlCardEntry.setIndexNames(
    (0, "TIMETRA-OES-HARDWARE-MIB", "tmnxOesChassisNumber"),
    (0, "TIMETRA-OES-HARDWARE-MIB", "tmnxOesSlotNumber"),
)
if mibBuilder.loadTexts:
    tmnxOesControlCardEntry.setStatus("current")


class _TmnxOesControlCardActState_Type(Integer32):
    """Custom type tmnxOesControlCardActState based on Integer32"""
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
        *(("unknown", 1),
          ("active", 2),
          ("standby", 3),
          ("unequipped", 4))
    )


_TmnxOesControlCardActState_Type.__name__ = "Integer32"
_TmnxOesControlCardActState_Object = MibTableColumn
tmnxOesControlCardActState = _TmnxOesControlCardActState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 99, 2, 4, 1, 1),
    _TmnxOesControlCardActState_Type()
)
tmnxOesControlCardActState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOesControlCardActState.setStatus("current")
_TmnxOesControlCardHwIndex_Type = TmnxHwIndex
_TmnxOesControlCardHwIndex_Object = MibTableColumn
tmnxOesControlCardHwIndex = _TmnxOesControlCardHwIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 99, 2, 4, 1, 2),
    _TmnxOesControlCardHwIndex_Type()
)
tmnxOesControlCardHwIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOesControlCardHwIndex.setStatus("current")
_TmnxOesPortObjs_ObjectIdentity = ObjectIdentity
tmnxOesPortObjs = _TmnxOesPortObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 99, 3)
)
_TmnxOesCmnEqpPortTable_Object = MibTable
tmnxOesCmnEqpPortTable = _TmnxOesCmnEqpPortTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 99, 3, 1)
)
if mibBuilder.loadTexts:
    tmnxOesCmnEqpPortTable.setStatus("current")
_TmnxOesCmnEqpPortEntry_Object = MibTableRow
tmnxOesCmnEqpPortEntry = _TmnxOesCmnEqpPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 99, 3, 1, 1)
)
tmnxOesCmnEqpPortEntry.setIndexNames(
    (0, "TIMETRA-OES-HARDWARE-MIB", "tmnxOesChassisNumber"),
    (0, "TIMETRA-OES-HARDWARE-MIB", "tmnxOesSlotNumber"),
    (0, "TIMETRA-OES-HARDWARE-MIB", "tmnxOesCmnEqpPortNumber"),
)
if mibBuilder.loadTexts:
    tmnxOesCmnEqpPortEntry.setStatus("current")
_TmnxOesCmnEqpPortNumber_Type = TmnxOesCmnEqpPortNumber
_TmnxOesCmnEqpPortNumber_Object = MibTableColumn
tmnxOesCmnEqpPortNumber = _TmnxOesCmnEqpPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 99, 3, 1, 1, 1),
    _TmnxOesCmnEqpPortNumber_Type()
)
tmnxOesCmnEqpPortNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxOesCmnEqpPortNumber.setStatus("current")
_TmnxOesCmnEqpPortCardType_Type = TmnxOesCardType
_TmnxOesCmnEqpPortCardType_Object = MibTableColumn
tmnxOesCmnEqpPortCardType = _TmnxOesCmnEqpPortCardType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 99, 3, 1, 1, 2),
    _TmnxOesCmnEqpPortCardType_Type()
)
tmnxOesCmnEqpPortCardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOesCmnEqpPortCardType.setStatus("current")
_TmnxOesCmnEqpPortOperStatus_Type = TmnxPortOperStatus
_TmnxOesCmnEqpPortOperStatus_Object = MibTableColumn
tmnxOesCmnEqpPortOperStatus = _TmnxOesCmnEqpPortOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 99, 3, 1, 1, 3),
    _TmnxOesCmnEqpPortOperStatus_Type()
)
tmnxOesCmnEqpPortOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOesCmnEqpPortOperStatus.setStatus("current")
_TmnxOesCmnEqpPortTypeTable_Object = MibTable
tmnxOesCmnEqpPortTypeTable = _TmnxOesCmnEqpPortTypeTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 99, 3, 2)
)
if mibBuilder.loadTexts:
    tmnxOesCmnEqpPortTypeTable.setStatus("current")
_TmnxOesCmnEqpPortTypeEntry_Object = MibTableRow
tmnxOesCmnEqpPortTypeEntry = _TmnxOesCmnEqpPortTypeEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 99, 3, 2, 1)
)
tmnxOesCmnEqpPortTypeEntry.setIndexNames(
    (0, "TIMETRA-OES-HARDWARE-MIB", "tmnxOesCardTypeIndex"),
    (0, "TIMETRA-OES-HARDWARE-MIB", "tmnxOesCmnEqpPortNumber"),
)
if mibBuilder.loadTexts:
    tmnxOesCmnEqpPortTypeEntry.setStatus("current")
_TmnxOesCmnEqpPortTypeName_Type = TNamedItem
_TmnxOesCmnEqpPortTypeName_Object = MibTableColumn
tmnxOesCmnEqpPortTypeName = _TmnxOesCmnEqpPortTypeName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 99, 3, 2, 1, 1),
    _TmnxOesCmnEqpPortTypeName_Type()
)
tmnxOesCmnEqpPortTypeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOesCmnEqpPortTypeName.setStatus("current")
_TmnxOesCmnEqpPortTypeDescr_Type = TItemDescription
_TmnxOesCmnEqpPortTypeDescr_Object = MibTableColumn
tmnxOesCmnEqpPortTypeDescr = _TmnxOesCmnEqpPortTypeDescr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 99, 3, 2, 1, 2),
    _TmnxOesCmnEqpPortTypeDescr_Type()
)
tmnxOesCmnEqpPortTypeDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxOesCmnEqpPortTypeDescr.setStatus("current")
_TmnxOesHwNotifyObjs_ObjectIdentity = ObjectIdentity
tmnxOesHwNotifyObjs = _TmnxOesHwNotifyObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 99, 4)
)
_TmnxOesNotifyFailureReason_Type = DisplayString
_TmnxOesNotifyFailureReason_Object = MibScalar
tmnxOesNotifyFailureReason = _TmnxOesNotifyFailureReason_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 99, 4, 1),
    _TmnxOesNotifyFailureReason_Type()
)
tmnxOesNotifyFailureReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxOesNotifyFailureReason.setStatus("current")
_TmnxOesPortNotifyError_Type = TmnxOesPortErrorStatus
_TmnxOesPortNotifyError_Object = MibScalar
tmnxOesPortNotifyError = _TmnxOesPortNotifyError_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 99, 4, 2),
    _TmnxOesPortNotifyError_Type()
)
tmnxOesPortNotifyError.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxOesPortNotifyError.setStatus("current")
_TmnxOesHwMIBNotifyPrefix_ObjectIdentity = ObjectIdentity
tmnxOesHwMIBNotifyPrefix = _TmnxOesHwMIBNotifyPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 99)
)
_TmnxOesHwNotifications_ObjectIdentity = ObjectIdentity
tmnxOesHwNotifications = _TmnxOesHwNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 99, 1)
)

# Managed Objects groups

tmnxOesHwGroupV14v0 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 99, 2, 1, 1)
)
tmnxOesHwGroupV14v0.setObjects(
      *(("TIMETRA-OES-HARDWARE-MIB", "tmnxOesChassisRowLastChanged"),
        ("TIMETRA-OES-HARDWARE-MIB", "tmnxOesChassisRowStatus"),
        ("TIMETRA-OES-HARDWARE-MIB", "tmnxOesChassisTypeName"),
        ("TIMETRA-OES-HARDWARE-MIB", "tmnxOesChassisTypeDescription"),
        ("TIMETRA-OES-HARDWARE-MIB", "tmnxOesChassisTypeStatus"),
        ("TIMETRA-OES-HARDWARE-MIB", "tmnxOesChassisLastChange"),
        ("TIMETRA-OES-HARDWARE-MIB", "tmnxOesChassisAssignedType"),
        ("TIMETRA-OES-HARDWARE-MIB", "tmnxOesChassisEquippedType"),
        ("TIMETRA-OES-HARDWARE-MIB", "tmnxOesChassisActivitySwitch"),
        ("TIMETRA-OES-HARDWARE-MIB", "tmnxOesChassisHwEntryIndex"),
        ("TIMETRA-OES-HARDWARE-MIB", "tmnxOesPFType"),
        ("TIMETRA-OES-HARDWARE-MIB", "tmnxOesPFAmpRating"),
        ("TIMETRA-OES-HARDWARE-MIB", "tmnxOesPFInputCurrent"),
        ("TIMETRA-OES-HARDWARE-MIB", "tmnxOesPFInputVoltage"),
        ("TIMETRA-OES-HARDWARE-MIB", "tmnxOesPFInputPower"),
        ("TIMETRA-OES-HARDWARE-MIB", "tmnxOesPFClkA"),
        ("TIMETRA-OES-HARDWARE-MIB", "tmnxOesPFClkB"),
        ("TIMETRA-OES-HARDWARE-MIB", "tmnxOesPFClkDelta"),
        ("TIMETRA-OES-HARDWARE-MIB", "tmnxOesPFState"),
        ("TIMETRA-OES-HARDWARE-MIB", "tmnxOesPFHwIndex"),
        ("TIMETRA-OES-HARDWARE-MIB", "tmnxOesFanLastChg"),
        ("TIMETRA-OES-HARDWARE-MIB", "tmnxOesFanState"),
        ("TIMETRA-OES-HARDWARE-MIB", "tmnxOesFanSpeedControl"),
        ("TIMETRA-OES-HARDWARE-MIB", "tmnxOesFanHwIndex"),
        ("TIMETRA-OES-HARDWARE-MIB", "tmnxOesCardTypeName"),
        ("TIMETRA-OES-HARDWARE-MIB", "tmnxOesCardTypeDescription"),
        ("TIMETRA-OES-HARDWARE-MIB", "tmnxOesCardTypeStatus"),
        ("TIMETRA-OES-HARDWARE-MIB", "tmnxOesCardTypeHeight"),
        ("TIMETRA-OES-HARDWARE-MIB", "tmnxOesCardTypeWidth"),
        ("TIMETRA-OES-HARDWARE-MIB", "tmnxOesCardTypeNumPorts"),
        ("TIMETRA-OES-HARDWARE-MIB", "tmnxOesCardLastChange"),
        ("TIMETRA-OES-HARDWARE-MIB", "tmnxOesCardAssignedType"),
        ("TIMETRA-OES-HARDWARE-MIB", "tmnxOesCardEquippedType"),
        ("TIMETRA-OES-HARDWARE-MIB", "tmnxOesCardSupportedTypes"),
        ("TIMETRA-OES-HARDWARE-MIB", "tmnxOesCardReboot"),
        ("TIMETRA-OES-HARDWARE-MIB", "tmnxOesCardHwEntryIndex"),
        ("TIMETRA-OES-HARDWARE-MIB", "tmnxOesCardRowLastChanged"),
        ("TIMETRA-OES-HARDWARE-MIB", "tmnxOesCardMemorySize"),
        ("TIMETRA-OES-HARDWARE-MIB", "tmnxOesControlCardActState"),
        ("TIMETRA-OES-HARDWARE-MIB", "tmnxOesControlCardHwIndex"),
        ("TIMETRA-OES-HARDWARE-MIB", "tmnxOesCmnEqpPortCardType"),
        ("TIMETRA-OES-HARDWARE-MIB", "tmnxOesCmnEqpPortOperStatus"),
        ("TIMETRA-OES-HARDWARE-MIB", "tmnxOesCmnEqpPortTypeDescr"),
        ("TIMETRA-OES-HARDWARE-MIB", "tmnxOesCmnEqpPortTypeName"))
)
if mibBuilder.loadTexts:
    tmnxOesHwGroupV14v0.setStatus("current")

tmnxOesHwNotifyObjsGroupV14v0 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 99, 2, 1, 2)
)
tmnxOesHwNotifyObjsGroupV14v0.setObjects(
      *(("TIMETRA-OES-HARDWARE-MIB", "tmnxOesNotifyFailureReason"),
        ("TIMETRA-OES-HARDWARE-MIB", "tmnxOesPortNotifyError"))
)
if mibBuilder.loadTexts:
    tmnxOesHwNotifyObjsGroupV14v0.setStatus("current")


# Notification objects

tmnxOesCtlCardPortDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 99, 1, 1)
)
tmnxOesCtlCardPortDown.setObjects(
    ("TIMETRA-OES-HARDWARE-MIB", "tmnxOesCmnEqpPortOperStatus")
)
if mibBuilder.loadTexts:
    tmnxOesCtlCardPortDown.setStatus(
        "current"
    )

tmnxOesCtlCardPortUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 99, 1, 2)
)
tmnxOesCtlCardPortUp.setObjects(
    ("TIMETRA-OES-HARDWARE-MIB", "tmnxOesCmnEqpPortOperStatus")
)
if mibBuilder.loadTexts:
    tmnxOesCtlCardPortUp.setStatus(
        "current"
    )

tmnxOesUsrpnlPortDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 99, 1, 3)
)
tmnxOesUsrpnlPortDown.setObjects(
    ("TIMETRA-OES-HARDWARE-MIB", "tmnxOesCmnEqpPortOperStatus")
)
if mibBuilder.loadTexts:
    tmnxOesUsrpnlPortDown.setStatus(
        "current"
    )

tmnxOesUsrpnlPortUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 99, 1, 4)
)
tmnxOesUsrpnlPortUp.setObjects(
    ("TIMETRA-OES-HARDWARE-MIB", "tmnxOesCmnEqpPortOperStatus")
)
if mibBuilder.loadTexts:
    tmnxOesUsrpnlPortUp.setStatus(
        "current"
    )

tmnxOesFanRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 99, 1, 5)
)
tmnxOesFanRemoved.setObjects(
    ("TIMETRA-CHASSIS-MIB", "tmnxHwClass")
)
if mibBuilder.loadTexts:
    tmnxOesFanRemoved.setStatus(
        "current"
    )

tmnxOesFanInserted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 99, 1, 6)
)
tmnxOesFanInserted.setObjects(
    ("TIMETRA-CHASSIS-MIB", "tmnxHwClass")
)
if mibBuilder.loadTexts:
    tmnxOesFanInserted.setStatus(
        "current"
    )

tmnxOesFan32HReqd = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 99, 1, 7)
)
tmnxOesFan32HReqd.setObjects(
    ("TIMETRA-CHASSIS-MIB", "tmnxHwClass")
)
if mibBuilder.loadTexts:
    tmnxOesFan32HReqd.setStatus(
        "current"
    )

tmnxOesFan32HReqdClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 99, 1, 8)
)
tmnxOesFan32HReqdClear.setObjects(
    ("TIMETRA-CHASSIS-MIB", "tmnxHwClass")
)
if mibBuilder.loadTexts:
    tmnxOesFan32HReqdClear.setStatus(
        "current"
    )

tmnxOesFanFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 99, 1, 9)
)
tmnxOesFanFailure.setObjects(
      *(("TIMETRA-CHASSIS-MIB", "tmnxHwClass"),
        ("TIMETRA-OES-HARDWARE-MIB", "tmnxOesFanState"),
        ("TIMETRA-OES-HARDWARE-MIB", "tmnxOesNotifyFailureReason"))
)
if mibBuilder.loadTexts:
    tmnxOesFanFailure.setStatus(
        "current"
    )

tmnxOesFanFailureClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 99, 1, 10)
)
tmnxOesFanFailureClear.setObjects(
      *(("TIMETRA-CHASSIS-MIB", "tmnxHwClass"),
        ("TIMETRA-OES-HARDWARE-MIB", "tmnxOesFanState"),
        ("TIMETRA-OES-HARDWARE-MIB", "tmnxOesNotifyFailureReason"))
)
if mibBuilder.loadTexts:
    tmnxOesFanFailureClear.setStatus(
        "current"
    )

tmnxOesPowerSupplyRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 99, 1, 11)
)
tmnxOesPowerSupplyRemoved.setObjects(
    ("TIMETRA-CHASSIS-MIB", "tmnxHwClass")
)
if mibBuilder.loadTexts:
    tmnxOesPowerSupplyRemoved.setStatus(
        "current"
    )

tmnxOesPowerSupplyInserted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 99, 1, 12)
)
tmnxOesPowerSupplyInserted.setObjects(
    ("TIMETRA-CHASSIS-MIB", "tmnxHwClass")
)
if mibBuilder.loadTexts:
    tmnxOesPowerSupplyInserted.setStatus(
        "current"
    )

tmnxOesPowerSupplyFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 99, 1, 13)
)
tmnxOesPowerSupplyFailure.setObjects(
      *(("TIMETRA-CHASSIS-MIB", "tmnxHwClass"),
        ("TIMETRA-OES-HARDWARE-MIB", "tmnxOesPFState"),
        ("TIMETRA-OES-HARDWARE-MIB", "tmnxOesNotifyFailureReason"))
)
if mibBuilder.loadTexts:
    tmnxOesPowerSupplyFailure.setStatus(
        "current"
    )

tmnxOesPowerSupplyFailureClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 99, 1, 14)
)
tmnxOesPowerSupplyFailureClear.setObjects(
      *(("TIMETRA-CHASSIS-MIB", "tmnxHwClass"),
        ("TIMETRA-OES-HARDWARE-MIB", "tmnxOesPFState"),
        ("TIMETRA-OES-HARDWARE-MIB", "tmnxOesNotifyFailureReason"))
)
if mibBuilder.loadTexts:
    tmnxOesPowerSupplyFailureClear.setStatus(
        "current"
    )

tmnxOesPortError = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 99, 1, 15)
)
tmnxOesPortError.setObjects(
      *(("TIMETRA-PORT-MIB", "tmnxPortNotifyPortId"),
        ("TIMETRA-OES-HARDWARE-MIB", "tmnxOesPortNotifyError"))
)
if mibBuilder.loadTexts:
    tmnxOesPortError.setStatus(
        "current"
    )

tmnxOesPortErrorClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 99, 1, 16)
)
tmnxOesPortErrorClear.setObjects(
    ("TIMETRA-PORT-MIB", "tmnxPortNotifyPortId")
)
if mibBuilder.loadTexts:
    tmnxOesPortErrorClear.setStatus(
        "current"
    )

tmnxOesCtlCardActivityChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 99, 1, 17)
)
tmnxOesCtlCardActivityChange.setObjects(
    ("TIMETRA-CHASSIS-MIB", "tmnxHwClass")
)
if mibBuilder.loadTexts:
    tmnxOesCtlCardActivityChange.setStatus(
        "current"
    )

tmnxOesFpgaFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 99, 1, 18)
)
tmnxOesFpgaFail.setObjects(
    ("TIMETRA-CHASSIS-MIB", "tmnxHwClass")
)
if mibBuilder.loadTexts:
    tmnxOesFpgaFail.setStatus(
        "current"
    )

tmnxOesFpgaFailClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 99, 1, 19)
)
tmnxOesFpgaFailClear.setObjects(
    ("TIMETRA-CHASSIS-MIB", "tmnxHwClass")
)
if mibBuilder.loadTexts:
    tmnxOesFpgaFailClear.setStatus(
        "current"
    )

tmnxOesFpgaTimeout = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 99, 1, 20)
)
tmnxOesFpgaTimeout.setObjects(
    ("TIMETRA-CHASSIS-MIB", "tmnxHwClass")
)
if mibBuilder.loadTexts:
    tmnxOesFpgaTimeout.setStatus(
        "current"
    )

tmnxOesFpgaTimeoutClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 99, 1, 21)
)
tmnxOesFpgaTimeoutClear.setObjects(
    ("TIMETRA-CHASSIS-MIB", "tmnxHwClass")
)
if mibBuilder.loadTexts:
    tmnxOesFpgaTimeoutClear.setStatus(
        "current"
    )

tmnxOesOptTrnspndrMiscFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 99, 1, 22)
)
tmnxOesOptTrnspndrMiscFail.setObjects(
    ("TIMETRA-CHASSIS-MIB", "tmnxHwClass")
)
if mibBuilder.loadTexts:
    tmnxOesOptTrnspndrMiscFail.setStatus(
        "current"
    )

tmnxOesCardDegraded = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 99, 1, 23)
)
tmnxOesCardDegraded.setObjects(
    ("TIMETRA-CHASSIS-MIB", "tmnxHwClass")
)
if mibBuilder.loadTexts:
    tmnxOesCardDegraded.setStatus(
        "current"
    )

tmnxOesFanSpeedHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 99, 1, 24)
)
tmnxOesFanSpeedHigh.setObjects(
    ("TIMETRA-CHASSIS-MIB", "tmnxHwClass")
)
if mibBuilder.loadTexts:
    tmnxOesFanSpeedHigh.setStatus(
        "current"
    )

tmnxOesFanSpeedHighClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 99, 1, 25)
)
tmnxOesFanSpeedHighClear.setObjects(
    ("TIMETRA-CHASSIS-MIB", "tmnxHwClass")
)
if mibBuilder.loadTexts:
    tmnxOesFanSpeedHighClear.setStatus(
        "current"
    )

tmnxOesFanSpeedLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 99, 1, 26)
)
tmnxOesFanSpeedLow.setObjects(
    ("TIMETRA-CHASSIS-MIB", "tmnxHwClass")
)
if mibBuilder.loadTexts:
    tmnxOesFanSpeedLow.setStatus(
        "current"
    )

tmnxOesFanSpeedLowClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 99, 1, 27)
)
tmnxOesFanSpeedLowClear.setObjects(
    ("TIMETRA-CHASSIS-MIB", "tmnxHwClass")
)
if mibBuilder.loadTexts:
    tmnxOesFanSpeedLowClear.setStatus(
        "current"
    )

tmnxOesTempLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 99, 1, 28)
)
tmnxOesTempLow.setObjects(
    ("TIMETRA-CHASSIS-MIB", "tmnxHwClass")
)
if mibBuilder.loadTexts:
    tmnxOesTempLow.setStatus(
        "current"
    )

tmnxOesTempLowClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 99, 1, 29)
)
tmnxOesTempLowClear.setObjects(
    ("TIMETRA-CHASSIS-MIB", "tmnxHwClass")
)
if mibBuilder.loadTexts:
    tmnxOesTempLowClear.setStatus(
        "current"
    )

tmnxOesRedundancyFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 99, 1, 30)
)
tmnxOesRedundancyFail.setObjects(
    ("TIMETRA-CHASSIS-MIB", "tmnxHwClass")
)
if mibBuilder.loadTexts:
    tmnxOesRedundancyFail.setStatus(
        "current"
    )

tmnxOesRedundancyReady = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 99, 1, 31)
)
tmnxOesRedundancyReady.setObjects(
    ("TIMETRA-CHASSIS-MIB", "tmnxHwClass")
)
if mibBuilder.loadTexts:
    tmnxOesRedundancyReady.setStatus(
        "current"
    )

tmnxOesCardFirmwareErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 99, 1, 33)
)
tmnxOesCardFirmwareErr.setObjects(
    ("TIMETRA-CHASSIS-MIB", "tmnxHwClass")
)
if mibBuilder.loadTexts:
    tmnxOesCardFirmwareErr.setStatus(
        "current"
    )


# Notifications groups

tmnxOesHwNotificationGroupV14v0 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 99, 2, 1, 3)
)
tmnxOesHwNotificationGroupV14v0.setObjects(
      *(("TIMETRA-OES-HARDWARE-MIB", "tmnxOesCtlCardPortDown"),
        ("TIMETRA-OES-HARDWARE-MIB", "tmnxOesCtlCardPortUp"),
        ("TIMETRA-OES-HARDWARE-MIB", "tmnxOesUsrpnlPortDown"),
        ("TIMETRA-OES-HARDWARE-MIB", "tmnxOesUsrpnlPortUp"),
        ("TIMETRA-OES-HARDWARE-MIB", "tmnxOesFanRemoved"),
        ("TIMETRA-OES-HARDWARE-MIB", "tmnxOesFanInserted"),
        ("TIMETRA-OES-HARDWARE-MIB", "tmnxOesFan32HReqd"),
        ("TIMETRA-OES-HARDWARE-MIB", "tmnxOesFan32HReqdClear"),
        ("TIMETRA-OES-HARDWARE-MIB", "tmnxOesFanFailure"),
        ("TIMETRA-OES-HARDWARE-MIB", "tmnxOesFanFailureClear"),
        ("TIMETRA-OES-HARDWARE-MIB", "tmnxOesPowerSupplyRemoved"),
        ("TIMETRA-OES-HARDWARE-MIB", "tmnxOesPowerSupplyInserted"),
        ("TIMETRA-OES-HARDWARE-MIB", "tmnxOesPowerSupplyFailure"),
        ("TIMETRA-OES-HARDWARE-MIB", "tmnxOesPowerSupplyFailureClear"),
        ("TIMETRA-OES-HARDWARE-MIB", "tmnxOesPortError"),
        ("TIMETRA-OES-HARDWARE-MIB", "tmnxOesPortErrorClear"),
        ("TIMETRA-OES-HARDWARE-MIB", "tmnxOesCtlCardActivityChange"),
        ("TIMETRA-OES-HARDWARE-MIB", "tmnxOesFpgaFail"),
        ("TIMETRA-OES-HARDWARE-MIB", "tmnxOesFpgaFailClear"),
        ("TIMETRA-OES-HARDWARE-MIB", "tmnxOesFpgaTimeout"),
        ("TIMETRA-OES-HARDWARE-MIB", "tmnxOesFpgaTimeoutClear"),
        ("TIMETRA-OES-HARDWARE-MIB", "tmnxOesOptTrnspndrMiscFail"),
        ("TIMETRA-OES-HARDWARE-MIB", "tmnxOesCardDegraded"),
        ("TIMETRA-OES-HARDWARE-MIB", "tmnxOesFanSpeedHigh"),
        ("TIMETRA-OES-HARDWARE-MIB", "tmnxOesFanSpeedHighClear"),
        ("TIMETRA-OES-HARDWARE-MIB", "tmnxOesFanSpeedLow"),
        ("TIMETRA-OES-HARDWARE-MIB", "tmnxOesFanSpeedLowClear"),
        ("TIMETRA-OES-HARDWARE-MIB", "tmnxOesRedundancyFail"),
        ("TIMETRA-OES-HARDWARE-MIB", "tmnxOesRedundancyReady"),
        ("TIMETRA-OES-HARDWARE-MIB", "tmnxOesCardFirmwareErr"),
        ("TIMETRA-OES-HARDWARE-MIB", "tmnxOesTempLow"),
        ("TIMETRA-OES-HARDWARE-MIB", "tmnxOesTempLowClear"))
)
if mibBuilder.loadTexts:
    tmnxOesHwNotificationGroupV14v0.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

tmnxOesHwV14v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 99, 1, 1)
)
tmnxOesHwV14v0Compliance.setObjects(
      *(("TIMETRA-OES-HARDWARE-MIB", "tmnxOesHwGroupV14v0"),
        ("TIMETRA-OES-HARDWARE-MIB", "tmnxOesHwNotifyObjsGroupV14v0"),
        ("TIMETRA-OES-HARDWARE-MIB", "tmnxOesHwNotificationGroupV14v0"))
)
if mibBuilder.loadTexts:
    tmnxOesHwV14v0Compliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TIMETRA-OES-HARDWARE-MIB",
    **{"TmnxOesCardHFD": TmnxOesCardHFD,
       "TmnxOesHwMktPartNo": TmnxOesHwMktPartNo,
       "TmnxOesHwSWGenLoadName": TmnxOesHwSWGenLoadName,
       "TmnxOesHwLEDColorType": TmnxOesHwLEDColorType,
       "TmnxOesHwLEDStateType": TmnxOesHwLEDStateType,
       "TmnxOesSlotNumber": TmnxOesSlotNumber,
       "TmnxOesChassisType": TmnxOesChassisType,
       "TmnxOesCardType": TmnxOesCardType,
       "TmnxOesCardSuppType": TmnxOesCardSuppType,
       "TmnxOesCmnEqpPortNumber": TmnxOesCmnEqpPortNumber,
       "TmnxOesPortErrorStatus": TmnxOesPortErrorStatus,
       "timetraOesHardwareMIBModule": timetraOesHardwareMIBModule,
       "tmnxOesHwConformance": tmnxOesHwConformance,
       "tmnxOesHwCompliances": tmnxOesHwCompliances,
       "tmnxOesHwV14v0Compliance": tmnxOesHwV14v0Compliance,
       "tmnxOesHwGroups": tmnxOesHwGroups,
       "tmnxOesHwV14v0Groups": tmnxOesHwV14v0Groups,
       "tmnxOesHwGroupV14v0": tmnxOesHwGroupV14v0,
       "tmnxOesHwNotifyObjsGroupV14v0": tmnxOesHwNotifyObjsGroupV14v0,
       "tmnxOesHwNotificationGroupV14v0": tmnxOesHwNotificationGroupV14v0,
       "tmnxOesHwObjs": tmnxOesHwObjs,
       "tmnxOesChassisObjs": tmnxOesChassisObjs,
       "tmnxOesChassisTypeTable": tmnxOesChassisTypeTable,
       "tmnxOesChassisTypeEntry": tmnxOesChassisTypeEntry,
       "tmnxOesChassisTypeIndex": tmnxOesChassisTypeIndex,
       "tmnxOesChassisTypeName": tmnxOesChassisTypeName,
       "tmnxOesChassisTypeDescription": tmnxOesChassisTypeDescription,
       "tmnxOesChassisTypeStatus": tmnxOesChassisTypeStatus,
       "tmnxOesChassisLastChange": tmnxOesChassisLastChange,
       "tmnxOesChassisTable": tmnxOesChassisTable,
       "tmnxOesChassisEntry": tmnxOesChassisEntry,
       "tmnxOesChassisNumber": tmnxOesChassisNumber,
       "tmnxOesChassisRowStatus": tmnxOesChassisRowStatus,
       "tmnxOesChassisRowLastChanged": tmnxOesChassisRowLastChanged,
       "tmnxOesChassisAssignedType": tmnxOesChassisAssignedType,
       "tmnxOesChassisEquippedType": tmnxOesChassisEquippedType,
       "tmnxOesChassisActivitySwitch": tmnxOesChassisActivitySwitch,
       "tmnxOesChassisHwEntryIndex": tmnxOesChassisHwEntryIndex,
       "tmnxOesPFTable": tmnxOesPFTable,
       "tmnxOesPFEntry": tmnxOesPFEntry,
       "tmnxOesSlotNumber": tmnxOesSlotNumber,
       "tmnxOesPFType": tmnxOesPFType,
       "tmnxOesPFAmpRating": tmnxOesPFAmpRating,
       "tmnxOesPFInputCurrent": tmnxOesPFInputCurrent,
       "tmnxOesPFInputVoltage": tmnxOesPFInputVoltage,
       "tmnxOesPFInputPower": tmnxOesPFInputPower,
       "tmnxOesPFClkA": tmnxOesPFClkA,
       "tmnxOesPFClkB": tmnxOesPFClkB,
       "tmnxOesPFClkDelta": tmnxOesPFClkDelta,
       "tmnxOesPFState": tmnxOesPFState,
       "tmnxOesPFHwIndex": tmnxOesPFHwIndex,
       "tmnxOesFanLastChg": tmnxOesFanLastChg,
       "tmnxOesFanTable": tmnxOesFanTable,
       "tmnxOesFanEntry": tmnxOesFanEntry,
       "tmnxOesFanSlotNumber": tmnxOesFanSlotNumber,
       "tmnxOesFanState": tmnxOesFanState,
       "tmnxOesFanSpeedControl": tmnxOesFanSpeedControl,
       "tmnxOesFanHwIndex": tmnxOesFanHwIndex,
       "tmnxOesCardObjs": tmnxOesCardObjs,
       "tmnxOesCardTypeTable": tmnxOesCardTypeTable,
       "tmnxOesCardTypeEntry": tmnxOesCardTypeEntry,
       "tmnxOesCardTypeIndex": tmnxOesCardTypeIndex,
       "tmnxOesCardTypeName": tmnxOesCardTypeName,
       "tmnxOesCardTypeDescription": tmnxOesCardTypeDescription,
       "tmnxOesCardTypeStatus": tmnxOesCardTypeStatus,
       "tmnxOesCardTypeHeight": tmnxOesCardTypeHeight,
       "tmnxOesCardTypeWidth": tmnxOesCardTypeWidth,
       "tmnxOesCardTypeNumPorts": tmnxOesCardTypeNumPorts,
       "tmnxOesCardLastChange": tmnxOesCardLastChange,
       "tmnxOesCardTable": tmnxOesCardTable,
       "tmnxOesCardEntry": tmnxOesCardEntry,
       "tmnxOesCardAssignedType": tmnxOesCardAssignedType,
       "tmnxOesCardEquippedType": tmnxOesCardEquippedType,
       "tmnxOesCardSupportedTypes": tmnxOesCardSupportedTypes,
       "tmnxOesCardReboot": tmnxOesCardReboot,
       "tmnxOesCardHwEntryIndex": tmnxOesCardHwEntryIndex,
       "tmnxOesCardRowLastChanged": tmnxOesCardRowLastChanged,
       "tmnxOesCardMemorySize": tmnxOesCardMemorySize,
       "tmnxOesControlCardTable": tmnxOesControlCardTable,
       "tmnxOesControlCardEntry": tmnxOesControlCardEntry,
       "tmnxOesControlCardActState": tmnxOesControlCardActState,
       "tmnxOesControlCardHwIndex": tmnxOesControlCardHwIndex,
       "tmnxOesPortObjs": tmnxOesPortObjs,
       "tmnxOesCmnEqpPortTable": tmnxOesCmnEqpPortTable,
       "tmnxOesCmnEqpPortEntry": tmnxOesCmnEqpPortEntry,
       "tmnxOesCmnEqpPortNumber": tmnxOesCmnEqpPortNumber,
       "tmnxOesCmnEqpPortCardType": tmnxOesCmnEqpPortCardType,
       "tmnxOesCmnEqpPortOperStatus": tmnxOesCmnEqpPortOperStatus,
       "tmnxOesCmnEqpPortTypeTable": tmnxOesCmnEqpPortTypeTable,
       "tmnxOesCmnEqpPortTypeEntry": tmnxOesCmnEqpPortTypeEntry,
       "tmnxOesCmnEqpPortTypeName": tmnxOesCmnEqpPortTypeName,
       "tmnxOesCmnEqpPortTypeDescr": tmnxOesCmnEqpPortTypeDescr,
       "tmnxOesHwNotifyObjs": tmnxOesHwNotifyObjs,
       "tmnxOesNotifyFailureReason": tmnxOesNotifyFailureReason,
       "tmnxOesPortNotifyError": tmnxOesPortNotifyError,
       "tmnxOesHwMIBNotifyPrefix": tmnxOesHwMIBNotifyPrefix,
       "tmnxOesHwNotifications": tmnxOesHwNotifications,
       "tmnxOesCtlCardPortDown": tmnxOesCtlCardPortDown,
       "tmnxOesCtlCardPortUp": tmnxOesCtlCardPortUp,
       "tmnxOesUsrpnlPortDown": tmnxOesUsrpnlPortDown,
       "tmnxOesUsrpnlPortUp": tmnxOesUsrpnlPortUp,
       "tmnxOesFanRemoved": tmnxOesFanRemoved,
       "tmnxOesFanInserted": tmnxOesFanInserted,
       "tmnxOesFan32HReqd": tmnxOesFan32HReqd,
       "tmnxOesFan32HReqdClear": tmnxOesFan32HReqdClear,
       "tmnxOesFanFailure": tmnxOesFanFailure,
       "tmnxOesFanFailureClear": tmnxOesFanFailureClear,
       "tmnxOesPowerSupplyRemoved": tmnxOesPowerSupplyRemoved,
       "tmnxOesPowerSupplyInserted": tmnxOesPowerSupplyInserted,
       "tmnxOesPowerSupplyFailure": tmnxOesPowerSupplyFailure,
       "tmnxOesPowerSupplyFailureClear": tmnxOesPowerSupplyFailureClear,
       "tmnxOesPortError": tmnxOesPortError,
       "tmnxOesPortErrorClear": tmnxOesPortErrorClear,
       "tmnxOesCtlCardActivityChange": tmnxOesCtlCardActivityChange,
       "tmnxOesFpgaFail": tmnxOesFpgaFail,
       "tmnxOesFpgaFailClear": tmnxOesFpgaFailClear,
       "tmnxOesFpgaTimeout": tmnxOesFpgaTimeout,
       "tmnxOesFpgaTimeoutClear": tmnxOesFpgaTimeoutClear,
       "tmnxOesOptTrnspndrMiscFail": tmnxOesOptTrnspndrMiscFail,
       "tmnxOesCardDegraded": tmnxOesCardDegraded,
       "tmnxOesFanSpeedHigh": tmnxOesFanSpeedHigh,
       "tmnxOesFanSpeedHighClear": tmnxOesFanSpeedHighClear,
       "tmnxOesFanSpeedLow": tmnxOesFanSpeedLow,
       "tmnxOesFanSpeedLowClear": tmnxOesFanSpeedLowClear,
       "tmnxOesTempLow": tmnxOesTempLow,
       "tmnxOesTempLowClear": tmnxOesTempLowClear,
       "tmnxOesRedundancyFail": tmnxOesRedundancyFail,
       "tmnxOesRedundancyReady": tmnxOesRedundancyReady,
       "tmnxOesCardFirmwareErr": tmnxOesCardFirmwareErr}
)
