# SNMP MIB module (LUM-SOAM-PM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/LUM-SOAM-PM-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:12:57 2025
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

(Dot1agCfmMepIdOrZero,) = mibBuilder.importSymbols(
    "IEEE8021-CFM-MIB",
    "Dot1agCfmMepIdOrZero")

(IEEE8021PriorityValue,) = mibBuilder.importSymbols(
    "IEEE8021-TC-MIB",
    "IEEE8021PriorityValue")

(lumModules,
 lumSoamPmMIB) = mibBuilder.importSymbols(
    "LUM-REG",
    "lumModules",
    "lumSoamPmMIB")

(BoardOrInterfaceAdminStatus,
 BoardOrInterfaceOperStatus,
 CommandString,
 FaultStatus,
 MgmtNameString,
 SlotNumber,
 SubrackNumber,
 Unsigned32WithNA) = mibBuilder.importSymbols(
    "LUM-TC",
    "BoardOrInterfaceAdminStatus",
    "BoardOrInterfaceOperStatus",
    "CommandString",
    "FaultStatus",
    "MgmtNameString",
    "SlotNumber",
    "SubrackNumber",
    "Unsigned32WithNA")

(MefSoamTcSessionType,
 MefSoamTcStatusType) = mibBuilder.importSymbols(
    "MEF-SOAM-TC-MIB",
    "MefSoamTcSessionType",
    "MefSoamTcStatusType")

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
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TimeInterval,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TimeInterval",
    "TruthValue")


# MODULE-IDENTITY

lumSoamPmMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 1, 1, 60)
)
if mibBuilder.loadTexts:
    lumSoamPmMIBModule.setRevisions(
        ("2017-06-15 00:00",
         "2016-01-11 00:00",
         "2015-01-14 00:00",
         "2014-05-16 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_LumSoamPmConfs_ObjectIdentity = ObjectIdentity
lumSoamPmConfs = _LumSoamPmConfs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 60, 1)
)
_LumSoamPmGroups_ObjectIdentity = ObjectIdentity
lumSoamPmGroups = _LumSoamPmGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 60, 1, 1)
)
_LumSoamPmCompliances_ObjectIdentity = ObjectIdentity
lumSoamPmCompliances = _LumSoamPmCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 60, 1, 2)
)
_LumSoamPmMIBObjects_ObjectIdentity = ObjectIdentity
lumSoamPmMIBObjects = _LumSoamPmMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 60, 2)
)
_SoamPmGeneral_ObjectIdentity = ObjectIdentity
soamPmGeneral = _SoamPmGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 60, 2, 1)
)
_SoamPmGeneralLastChangeTime_Type = DateAndTime
_SoamPmGeneralLastChangeTime_Object = MibScalar
soamPmGeneralLastChangeTime = _SoamPmGeneralLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 60, 2, 1, 1),
    _SoamPmGeneralLastChangeTime_Type()
)
soamPmGeneralLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    soamPmGeneralLastChangeTime.setStatus("current")
_SoamPmGeneralLmStateLastChangeTime_Type = DateAndTime
_SoamPmGeneralLmStateLastChangeTime_Object = MibScalar
soamPmGeneralLmStateLastChangeTime = _SoamPmGeneralLmStateLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 60, 2, 1, 2),
    _SoamPmGeneralLmStateLastChangeTime_Type()
)
soamPmGeneralLmStateLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    soamPmGeneralLmStateLastChangeTime.setStatus("current")
_SoamPmGeneralLmObjectsTableSize_Type = Unsigned32
_SoamPmGeneralLmObjectsTableSize_Object = MibScalar
soamPmGeneralLmObjectsTableSize = _SoamPmGeneralLmObjectsTableSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 60, 2, 1, 3),
    _SoamPmGeneralLmObjectsTableSize_Type()
)
soamPmGeneralLmObjectsTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    soamPmGeneralLmObjectsTableSize.setStatus("current")
_SoamPmGeneralDmObjectsTableSize_Type = Unsigned32
_SoamPmGeneralDmObjectsTableSize_Object = MibScalar
soamPmGeneralDmObjectsTableSize = _SoamPmGeneralDmObjectsTableSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 60, 2, 1, 4),
    _SoamPmGeneralDmObjectsTableSize_Type()
)
soamPmGeneralDmObjectsTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    soamPmGeneralDmObjectsTableSize.setStatus("current")
_SoamPmLmObjects_ObjectIdentity = ObjectIdentity
soamPmLmObjects = _SoamPmLmObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 60, 2, 2)
)
_SoamPmLmCfgTable_Object = MibTable
soamPmLmCfgTable = _SoamPmLmCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 60, 2, 2, 1)
)
if mibBuilder.loadTexts:
    soamPmLmCfgTable.setStatus("current")
_SoamPmLmCfgEntry_Object = MibTableRow
soamPmLmCfgEntry = _SoamPmLmCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 60, 2, 2, 1, 1)
)
soamPmLmCfgEntry.setIndexNames(
    (0, "LUM-SOAM-PM-MIB", "soamPmLmCfgIndex"),
)
if mibBuilder.loadTexts:
    soamPmLmCfgEntry.setStatus("current")


class _SoamPmLmCfgIndex_Type(Unsigned32):
    """Custom type soamPmLmCfgIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_SoamPmLmCfgIndex_Type.__name__ = "Unsigned32"
_SoamPmLmCfgIndex_Object = MibTableColumn
soamPmLmCfgIndex = _SoamPmLmCfgIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 60, 2, 2, 1, 1, 1),
    _SoamPmLmCfgIndex_Type()
)
soamPmLmCfgIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    soamPmLmCfgIndex.setStatus("current")
_SoamPmLmCfgName_Type = MgmtNameString
_SoamPmLmCfgName_Object = MibTableColumn
soamPmLmCfgName = _SoamPmLmCfgName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 60, 2, 2, 1, 1, 2),
    _SoamPmLmCfgName_Type()
)
soamPmLmCfgName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    soamPmLmCfgName.setStatus("current")


class _SoamPmLmCfgDescr_Type(DisplayString):
    """Custom type soamPmLmCfgDescr based on DisplayString"""
    defaultValue = OctetString("")


_SoamPmLmCfgDescr_Type.__name__ = "DisplayString"
_SoamPmLmCfgDescr_Object = MibTableColumn
soamPmLmCfgDescr = _SoamPmLmCfgDescr_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 60, 2, 2, 1, 1, 3),
    _SoamPmLmCfgDescr_Type()
)
soamPmLmCfgDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    soamPmLmCfgDescr.setStatus("current")
_SoamPmLmCfgSubrack_Type = SubrackNumber
_SoamPmLmCfgSubrack_Object = MibTableColumn
soamPmLmCfgSubrack = _SoamPmLmCfgSubrack_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 60, 2, 2, 1, 1, 4),
    _SoamPmLmCfgSubrack_Type()
)
soamPmLmCfgSubrack.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    soamPmLmCfgSubrack.setStatus("current")
_SoamPmLmCfgSlot_Type = SlotNumber
_SoamPmLmCfgSlot_Object = MibTableColumn
soamPmLmCfgSlot = _SoamPmLmCfgSlot_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 60, 2, 2, 1, 1, 5),
    _SoamPmLmCfgSlot_Type()
)
soamPmLmCfgSlot.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    soamPmLmCfgSlot.setStatus("current")


class _SoamPmLmCfgEnabled_Type(TruthValue):
    """Custom type soamPmLmCfgEnabled based on TruthValue"""
    defaultValue = 1


_SoamPmLmCfgEnabled_Type.__name__ = "TruthValue"
_SoamPmLmCfgEnabled_Object = MibTableColumn
soamPmLmCfgEnabled = _SoamPmLmCfgEnabled_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 60, 2, 2, 1, 1, 6),
    _SoamPmLmCfgEnabled_Type()
)
soamPmLmCfgEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    soamPmLmCfgEnabled.setStatus("current")


class _SoamPmLmCfgMessagePeriod_Type(Integer32):
    """Custom type soamPmLmCfgMessagePeriod based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("interval100ms", 0),
          ("interval1s", 1),
          ("interval10s", 2))
    )


_SoamPmLmCfgMessagePeriod_Type.__name__ = "Integer32"
_SoamPmLmCfgMessagePeriod_Object = MibTableColumn
soamPmLmCfgMessagePeriod = _SoamPmLmCfgMessagePeriod_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 60, 2, 2, 1, 1, 7),
    _SoamPmLmCfgMessagePeriod_Type()
)
soamPmLmCfgMessagePeriod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    soamPmLmCfgMessagePeriod.setStatus("current")
_SoamPmLmCfgDestMacAddress_Type = MacAddress
_SoamPmLmCfgDestMacAddress_Object = MibTableColumn
soamPmLmCfgDestMacAddress = _SoamPmLmCfgDestMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 60, 2, 2, 1, 1, 8),
    _SoamPmLmCfgDestMacAddress_Type()
)
soamPmLmCfgDestMacAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    soamPmLmCfgDestMacAddress.setStatus("current")
_SoamPmLmCfgMepName_Type = DisplayString
_SoamPmLmCfgMepName_Object = MibTableColumn
soamPmLmCfgMepName = _SoamPmLmCfgMepName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 60, 2, 2, 1, 1, 9),
    _SoamPmLmCfgMepName_Type()
)
soamPmLmCfgMepName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    soamPmLmCfgMepName.setStatus("current")


class _SoamPmLmCfgMaidIdentifier_Type(DisplayString):
    """Custom type soamPmLmCfgMaidIdentifier based on DisplayString"""
    defaultValue = OctetString("")


_SoamPmLmCfgMaidIdentifier_Type.__name__ = "DisplayString"
_SoamPmLmCfgMaidIdentifier_Object = MibTableColumn
soamPmLmCfgMaidIdentifier = _SoamPmLmCfgMaidIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 60, 2, 2, 1, 1, 10),
    _SoamPmLmCfgMaidIdentifier_Type()
)
soamPmLmCfgMaidIdentifier.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    soamPmLmCfgMaidIdentifier.setStatus("current")


class _SoamPmLmCfgDestMepId_Type(Dot1agCfmMepIdOrZero):
    """Custom type soamPmLmCfgDestMepId based on Dot1agCfmMepIdOrZero"""
    defaultValue = 0


_SoamPmLmCfgDestMepId_Type.__name__ = "Dot1agCfmMepIdOrZero"
_SoamPmLmCfgDestMepId_Object = MibTableColumn
soamPmLmCfgDestMepId = _SoamPmLmCfgDestMepId_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 60, 2, 2, 1, 1, 11),
    _SoamPmLmCfgDestMepId_Type()
)
soamPmLmCfgDestMepId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    soamPmLmCfgDestMepId.setStatus("current")


class _SoamPmLmCfgDestIsMepId_Type(TruthValue):
    """Custom type soamPmLmCfgDestIsMepId based on TruthValue"""
    defaultValue = 1


_SoamPmLmCfgDestIsMepId_Type.__name__ = "TruthValue"
_SoamPmLmCfgDestIsMepId_Object = MibTableColumn
soamPmLmCfgDestIsMepId = _SoamPmLmCfgDestIsMepId_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 60, 2, 2, 1, 1, 12),
    _SoamPmLmCfgDestIsMepId_Type()
)
soamPmLmCfgDestIsMepId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    soamPmLmCfgDestIsMepId.setStatus("current")


class _SoamPmLmCfgInternalReference_Type(Unsigned32):
    """Custom type soamPmLmCfgInternalReference based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SoamPmLmCfgInternalReference_Type.__name__ = "Unsigned32"
_SoamPmLmCfgInternalReference_Object = MibTableColumn
soamPmLmCfgInternalReference = _SoamPmLmCfgInternalReference_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 60, 2, 2, 1, 1, 13),
    _SoamPmLmCfgInternalReference_Type()
)
soamPmLmCfgInternalReference.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    soamPmLmCfgInternalReference.setStatus("current")


class _SoamPmLmCfgLocalDeviceType_Type(Integer32):
    """Custom type soamPmLmCfgLocalDeviceType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("emxp", 1),
          ("nidGe", 2))
    )


_SoamPmLmCfgLocalDeviceType_Type.__name__ = "Integer32"
_SoamPmLmCfgLocalDeviceType_Object = MibTableColumn
soamPmLmCfgLocalDeviceType = _SoamPmLmCfgLocalDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 60, 2, 2, 1, 1, 14),
    _SoamPmLmCfgLocalDeviceType_Type()
)
soamPmLmCfgLocalDeviceType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    soamPmLmCfgLocalDeviceType.setStatus("current")


class _SoamPmLmCfgType_Type(Integer32):
    """Custom type soamPmLmCfgType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("lmLmm", 1),
          ("lmSlm", 2),
          ("lmCcm", 3))
    )


_SoamPmLmCfgType_Type.__name__ = "Integer32"
_SoamPmLmCfgType_Object = MibTableColumn
soamPmLmCfgType = _SoamPmLmCfgType_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 60, 2, 2, 1, 1, 15),
    _SoamPmLmCfgType_Type()
)
soamPmLmCfgType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    soamPmLmCfgType.setStatus("current")


class _SoamPmLmCfgPriority_Type(IEEE8021PriorityValue):
    """Custom type soamPmLmCfgPriority based on IEEE8021PriorityValue"""
    defaultValue = 0


_SoamPmLmCfgPriority_Type.__name__ = "IEEE8021PriorityValue"
_SoamPmLmCfgPriority_Object = MibTableColumn
soamPmLmCfgPriority = _SoamPmLmCfgPriority_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 60, 2, 2, 1, 1, 16),
    _SoamPmLmCfgPriority_Type()
)
soamPmLmCfgPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    soamPmLmCfgPriority.setStatus("current")


class _SoamPmLmCfgAvailabilityFlrThreshold_Type(Unsigned32):
    """Custom type soamPmLmCfgAvailabilityFlrThreshold based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_SoamPmLmCfgAvailabilityFlrThreshold_Type.__name__ = "Unsigned32"
_SoamPmLmCfgAvailabilityFlrThreshold_Object = MibTableColumn
soamPmLmCfgAvailabilityFlrThreshold = _SoamPmLmCfgAvailabilityFlrThreshold_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 60, 2, 2, 1, 1, 17),
    _SoamPmLmCfgAvailabilityFlrThreshold_Type()
)
soamPmLmCfgAvailabilityFlrThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    soamPmLmCfgAvailabilityFlrThreshold.setStatus("current")


class _SoamPmLmCfgAvailabilityUasAlarmThreshold_Type(Unsigned32):
    """Custom type soamPmLmCfgAvailabilityUasAlarmThreshold based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 900),
    )


_SoamPmLmCfgAvailabilityUasAlarmThreshold_Type.__name__ = "Unsigned32"
_SoamPmLmCfgAvailabilityUasAlarmThreshold_Object = MibTableColumn
soamPmLmCfgAvailabilityUasAlarmThreshold = _SoamPmLmCfgAvailabilityUasAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 60, 2, 2, 1, 1, 18),
    _SoamPmLmCfgAvailabilityUasAlarmThreshold_Type()
)
soamPmLmCfgAvailabilityUasAlarmThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    soamPmLmCfgAvailabilityUasAlarmThreshold.setStatus("current")


class _SoamPmLmCfgSessionType_Type(MefSoamTcSessionType):
    """Custom type soamPmLmCfgSessionType based on MefSoamTcSessionType"""
    defaultValue = 1


_SoamPmLmCfgSessionType_Type.__name__ = "MefSoamTcSessionType"
_SoamPmLmCfgSessionType_Object = MibTableColumn
soamPmLmCfgSessionType = _SoamPmLmCfgSessionType_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 60, 2, 2, 1, 1, 19),
    _SoamPmLmCfgSessionType_Type()
)
soamPmLmCfgSessionType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    soamPmLmCfgSessionType.setStatus("current")
_SoamPmLmCfgSessionStatus_Type = MefSoamTcStatusType
_SoamPmLmCfgSessionStatus_Object = MibTableColumn
soamPmLmCfgSessionStatus = _SoamPmLmCfgSessionStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 60, 2, 2, 1, 1, 20),
    _SoamPmLmCfgSessionStatus_Type()
)
soamPmLmCfgSessionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    soamPmLmCfgSessionStatus.setStatus("current")


class _SoamPmLmCfgCosAwareness_Type(Integer32):
    """Custom type soamPmLmCfgCosAwareness based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("priorityBlind", 1),
          ("priorityAware", 2))
    )


_SoamPmLmCfgCosAwareness_Type.__name__ = "Integer32"
_SoamPmLmCfgCosAwareness_Object = MibTableColumn
soamPmLmCfgCosAwareness = _SoamPmLmCfgCosAwareness_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 60, 2, 2, 1, 1, 21),
    _SoamPmLmCfgCosAwareness_Type()
)
soamPmLmCfgCosAwareness.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    soamPmLmCfgCosAwareness.setStatus("current")
_SoamPmLmCfgRowStatus_Type = RowStatus
_SoamPmLmCfgRowStatus_Object = MibTableColumn
soamPmLmCfgRowStatus = _SoamPmLmCfgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 60, 2, 2, 1, 1, 22),
    _SoamPmLmCfgRowStatus_Type()
)
soamPmLmCfgRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    soamPmLmCfgRowStatus.setStatus("current")


class _SoamPmLmCfgAdminStatus_Type(BoardOrInterfaceAdminStatus):
    """Custom type soamPmLmCfgAdminStatus based on BoardOrInterfaceAdminStatus"""
    defaultValue = 3


_SoamPmLmCfgAdminStatus_Type.__name__ = "BoardOrInterfaceAdminStatus"
_SoamPmLmCfgAdminStatus_Object = MibTableColumn
soamPmLmCfgAdminStatus = _SoamPmLmCfgAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 60, 2, 2, 1, 1, 23),
    _SoamPmLmCfgAdminStatus_Type()
)
soamPmLmCfgAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    soamPmLmCfgAdminStatus.setStatus("current")


class _SoamPmLmCfgOperStatus_Type(BoardOrInterfaceOperStatus):
    """Custom type soamPmLmCfgOperStatus based on BoardOrInterfaceOperStatus"""
    defaultValue = 1


_SoamPmLmCfgOperStatus_Type.__name__ = "BoardOrInterfaceOperStatus"
_SoamPmLmCfgOperStatus_Object = MibTableColumn
soamPmLmCfgOperStatus = _SoamPmLmCfgOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 60, 2, 2, 1, 1, 24),
    _SoamPmLmCfgOperStatus_Type()
)
soamPmLmCfgOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    soamPmLmCfgOperStatus.setStatus("current")
_SoamPmLmCfgStats_Type = CommandString
_SoamPmLmCfgStats_Object = MibTableColumn
soamPmLmCfgStats = _SoamPmLmCfgStats_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 60, 2, 2, 1, 1, 25),
    _SoamPmLmCfgStats_Type()
)
soamPmLmCfgStats.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    soamPmLmCfgStats.setStatus("current")
_SoamPmLmStatsTable_Object = MibTable
soamPmLmStatsTable = _SoamPmLmStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 60, 2, 2, 2)
)
if mibBuilder.loadTexts:
    soamPmLmStatsTable.setStatus("current")
_SoamPmLmStatsEntry_Object = MibTableRow
soamPmLmStatsEntry = _SoamPmLmStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 60, 2, 2, 2, 1)
)
soamPmLmStatsEntry.setIndexNames(
    (0, "LUM-SOAM-PM-MIB", "soamPmLmStatsIndex"),
)
if mibBuilder.loadTexts:
    soamPmLmStatsEntry.setStatus("current")
_SoamPmLmStatsIndex_Type = Unsigned32
_SoamPmLmStatsIndex_Object = MibTableColumn
soamPmLmStatsIndex = _SoamPmLmStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 60, 2, 2, 2, 1, 1),
    _SoamPmLmStatsIndex_Type()
)
soamPmLmStatsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    soamPmLmStatsIndex.setStatus("current")


class _SoamPmLmStatsLocalDeviceType_Type(Integer32):
    """Custom type soamPmLmStatsLocalDeviceType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("emxp", 1),
          ("nidGe", 2))
    )


_SoamPmLmStatsLocalDeviceType_Type.__name__ = "Integer32"
_SoamPmLmStatsLocalDeviceType_Object = MibTableColumn
soamPmLmStatsLocalDeviceType = _SoamPmLmStatsLocalDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 60, 2, 2, 2, 1, 2),
    _SoamPmLmStatsLocalDeviceType_Type()
)
soamPmLmStatsLocalDeviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    soamPmLmStatsLocalDeviceType.setStatus("current")
_SoamPmLmStatsName_Type = MgmtNameString
_SoamPmLmStatsName_Object = MibTableColumn
soamPmLmStatsName = _SoamPmLmStatsName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 60, 2, 2, 2, 1, 3),
    _SoamPmLmStatsName_Type()
)
soamPmLmStatsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    soamPmLmStatsName.setStatus("current")
_SoamPmLmStatsSubrack_Type = SubrackNumber
_SoamPmLmStatsSubrack_Object = MibTableColumn
soamPmLmStatsSubrack = _SoamPmLmStatsSubrack_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 60, 2, 2, 2, 1, 4),
    _SoamPmLmStatsSubrack_Type()
)
soamPmLmStatsSubrack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    soamPmLmStatsSubrack.setStatus("current")
_SoamPmLmStatsSlot_Type = SlotNumber
_SoamPmLmStatsSlot_Object = MibTableColumn
soamPmLmStatsSlot = _SoamPmLmStatsSlot_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 60, 2, 2, 2, 1, 5),
    _SoamPmLmStatsSlot_Type()
)
soamPmLmStatsSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    soamPmLmStatsSlot.setStatus("current")


class _SoamPmLmStatsMaidIdentifier_Type(DisplayString):
    """Custom type soamPmLmStatsMaidIdentifier based on DisplayString"""
    defaultValue = OctetString("")


_SoamPmLmStatsMaidIdentifier_Type.__name__ = "DisplayString"
_SoamPmLmStatsMaidIdentifier_Object = MibTableColumn
soamPmLmStatsMaidIdentifier = _SoamPmLmStatsMaidIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 60, 2, 2, 2, 1, 6),
    _SoamPmLmStatsMaidIdentifier_Type()
)
soamPmLmStatsMaidIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    soamPmLmStatsMaidIdentifier.setStatus("current")


class _SoamPmLmStatsDestMepId_Type(Dot1agCfmMepIdOrZero):
    """Custom type soamPmLmStatsDestMepId based on Dot1agCfmMepIdOrZero"""
    defaultValue = 0


_SoamPmLmStatsDestMepId_Type.__name__ = "Dot1agCfmMepIdOrZero"
_SoamPmLmStatsDestMepId_Object = MibTableColumn
soamPmLmStatsDestMepId = _SoamPmLmStatsDestMepId_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 60, 2, 2, 2, 1, 7),
    _SoamPmLmStatsDestMepId_Type()
)
soamPmLmStatsDestMepId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    soamPmLmStatsDestMepId.setStatus("current")


class _SoamPmLmStatsInternalReference_Type(Unsigned32):
    """Custom type soamPmLmStatsInternalReference based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SoamPmLmStatsInternalReference_Type.__name__ = "Unsigned32"
_SoamPmLmStatsInternalReference_Object = MibTableColumn
soamPmLmStatsInternalReference = _SoamPmLmStatsInternalReference_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 60, 2, 2, 2, 1, 8),
    _SoamPmLmStatsInternalReference_Type()
)
soamPmLmStatsInternalReference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    soamPmLmStatsInternalReference.setStatus("current")
_SoamPmLmStatsMepName_Type = DisplayString
_SoamPmLmStatsMepName_Object = MibTableColumn
soamPmLmStatsMepName = _SoamPmLmStatsMepName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 60, 2, 2, 2, 1, 9),
    _SoamPmLmStatsMepName_Type()
)
soamPmLmStatsMepName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    soamPmLmStatsMepName.setStatus("current")
_SoamPmLmStatsSuspect15Min_Type = TruthValue
_SoamPmLmStatsSuspect15Min_Object = MibTableColumn
soamPmLmStatsSuspect15Min = _SoamPmLmStatsSuspect15Min_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 60, 2, 2, 2, 1, 10),
    _SoamPmLmStatsSuspect15Min_Type()
)
soamPmLmStatsSuspect15Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    soamPmLmStatsSuspect15Min.setStatus("current")
_SoamPmLmStatsSuspectPrevious15Min_Type = TruthValue
_SoamPmLmStatsSuspectPrevious15Min_Object = MibTableColumn
soamPmLmStatsSuspectPrevious15Min = _SoamPmLmStatsSuspectPrevious15Min_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 60, 2, 2, 2, 1, 11),
    _SoamPmLmStatsSuspectPrevious15Min_Type()
)
soamPmLmStatsSuspectPrevious15Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    soamPmLmStatsSuspectPrevious15Min.setStatus("current")
_SoamPmLmStatsSuspect24H_Type = TruthValue
_SoamPmLmStatsSuspect24H_Object = MibTableColumn
soamPmLmStatsSuspect24H = _SoamPmLmStatsSuspect24H_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 60, 2, 2, 2, 1, 12),
    _SoamPmLmStatsSuspect24H_Type()
)
soamPmLmStatsSuspect24H.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    soamPmLmStatsSuspect24H.setStatus("current")


class _SoamPmLmStatsReset15Min_Type(Integer32):
    """Custom type soamPmLmStatsReset15Min based on Integer32"""
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
          ("reset", 2))
    )


_SoamPmLmStatsReset15Min_Type.__name__ = "Integer32"
_SoamPmLmStatsReset15Min_Object = MibTableColumn
soamPmLmStatsReset15Min = _SoamPmLmStatsReset15Min_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 60, 2, 2, 2, 1, 13),
    _SoamPmLmStatsReset15Min_Type()
)
soamPmLmStatsReset15Min.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    soamPmLmStatsReset15Min.setStatus("current")


class _SoamPmLmStatsReset24H_Type(Integer32):
    """Custom type soamPmLmStatsReset24H based on Integer32"""
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
          ("reset", 2))
    )


_SoamPmLmStatsReset24H_Type.__name__ = "Integer32"
_SoamPmLmStatsReset24H_Object = MibTableColumn
soamPmLmStatsReset24H = _SoamPmLmStatsReset24H_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 60, 2, 2, 2, 1, 14),
    _SoamPmLmStatsReset24H_Type()
)
soamPmLmStatsReset24H.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    soamPmLmStatsReset24H.setStatus("current")
_SoamPmLmStatsStartTime15Min_Type = DateAndTime
_SoamPmLmStatsStartTime15Min_Object = MibTableColumn
soamPmLmStatsStartTime15Min = _SoamPmLmStatsStartTime15Min_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 60, 2, 2, 2, 1, 15),
    _SoamPmLmStatsStartTime15Min_Type()
)
soamPmLmStatsStartTime15Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    soamPmLmStatsStartTime15Min.setStatus("current")
_SoamPmLmStatsElapsedTime15Min_Type = TimeInterval
_SoamPmLmStatsElapsedTime15Min_Object = MibTableColumn
soamPmLmStatsElapsedTime15Min = _SoamPmLmStatsElapsedTime15Min_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 60, 2, 2, 2, 1, 16),
    _SoamPmLmStatsElapsedTime15Min_Type()
)
soamPmLmStatsElapsedTime15Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    soamPmLmStatsElapsedTime15Min.setStatus("current")
_SoamPmLmStatsForwardTransmittedFrames15Min_Type = Counter64
_SoamPmLmStatsForwardTransmittedFrames15Min_Object = MibTableColumn
soamPmLmStatsForwardTransmittedFrames15Min = _SoamPmLmStatsForwardTransmittedFrames15Min_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 60, 2, 2, 2, 1, 17),
    _SoamPmLmStatsForwardTransmittedFrames15Min_Type()
)
soamPmLmStatsForwardTransmittedFrames15Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    soamPmLmStatsForwardTransmittedFrames15Min.setStatus("current")
_SoamPmLmStatsForwardReceivedFrames15Min_Type = Counter64
_SoamPmLmStatsForwardReceivedFrames15Min_Object = MibTableColumn
soamPmLmStatsForwardReceivedFrames15Min = _SoamPmLmStatsForwardReceivedFrames15Min_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 60, 2, 2, 2, 1, 18),
    _SoamPmLmStatsForwardReceivedFrames15Min_Type()
)
soamPmLmStatsForwardReceivedFrames15Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    soamPmLmStatsForwardReceivedFrames15Min.setStatus("current")


class _SoamPmLmStatsForwardMinFlr15Min_Type(Unsigned32WithNA):
    """Custom type soamPmLmStatsForwardMinFlr15Min based on Unsigned32WithNA"""
    defaultValue = 4294967294

    subtypeSpec = Unsigned32WithNA.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
        ValueRangeConstraint(4294967294, 4294967294),
    )


_SoamPmLmStatsForwardMinFlr15Min_Type.__name__ = "Unsigned32WithNA"
_SoamPmLmStatsForwardMinFlr15Min_Object = MibTableColumn
soamPmLmStatsForwardMinFlr15Min = _SoamPmLmStatsForwardMinFlr15Min_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 60, 2, 2, 2, 1, 19),
    _SoamPmLmStatsForwardMinFlr15Min_Type()
)
soamPmLmStatsForwardMinFlr15Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    soamPmLmStatsForwardMinFlr15Min.setStatus("current")


class _SoamPmLmStatsForwardMaxFlr15Min_Type(Unsigned32):
    """Custom type soamPmLmStatsForwardMaxFlr15Min based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_SoamPmLmStatsForwardMaxFlr15Min_Type.__name__ = "Unsigned32"
_SoamPmLmStatsForwardMaxFlr15Min_Object = MibTableColumn
soamPmLmStatsForwardMaxFlr15Min = _SoamPmLmStatsForwardMaxFlr15Min_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 60, 2, 2, 2, 1, 20),
    _SoamPmLmStatsForwardMaxFlr15Min_Type()
)
soamPmLmStatsForwardMaxFlr15Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    soamPmLmStatsForwardMaxFlr15Min.setStatus("current")


class _SoamPmLmStatsForwardAvgFlr15Min_Type(Unsigned32):
    """Custom type soamPmLmStatsForwardAvgFlr15Min based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_SoamPmLmStatsForwardAvgFlr15Min_Type.__name__ = "Unsigned32"
_SoamPmLmStatsForwardAvgFlr15Min_Object = MibTableColumn
soamPmLmStatsForwardAvgFlr15Min = _SoamPmLmStatsForwardAvgFlr15Min_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 60, 2, 2, 2, 1, 21),
    _SoamPmLmStatsForwardAvgFlr15Min_Type()
)
soamPmLmStatsForwardAvgFlr15Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    soamPmLmStatsForwardAvgFlr15Min.setStatus("current")
_SoamPmLmStatsForwardHighLoss15Min_Type = Unsigned32
_SoamPmLmStatsForwardHighLoss15Min_Object = MibTableColumn
soamPmLmStatsForwardHighLoss15Min = _SoamPmLmStatsForwardHighLoss15Min_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 60, 2, 2, 2, 1, 22),
    _SoamPmLmStatsForwardHighLoss15Min_Type()
)
soamPmLmStatsForwardHighLoss15Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    soamPmLmStatsForwardHighLoss15Min.setStatus("current")
_SoamPmLmStatsBackwardTransmittedFrames15Min_Type = Counter64
_SoamPmLmStatsBackwardTransmittedFrames15Min_Object = MibTableColumn
soamPmLmStatsBackwardTransmittedFrames15Min = _SoamPmLmStatsBackwardTransmittedFrames15Min_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 60, 2, 2, 2, 1, 23),
    _SoamPmLmStatsBackwardTransmittedFrames15Min_Type()
)
soamPmLmStatsBackwardTransmittedFrames15Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    soamPmLmStatsBackwardTransmittedFrames15Min.setStatus("current")
_SoamPmLmStatsBackwardReceivedFrames15Min_Type = Counter64
_SoamPmLmStatsBackwardReceivedFrames15Min_Object = MibTableColumn
soamPmLmStatsBackwardReceivedFrames15Min = _SoamPmLmStatsBackwardReceivedFrames15Min_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 60, 2, 2, 2, 1, 24),
    _SoamPmLmStatsBackwardReceivedFrames15Min_Type()
)
soamPmLmStatsBackwardReceivedFrames15Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    soamPmLmStatsBackwardReceivedFrames15Min.setStatus("current")


class _SoamPmLmStatsBackwardMinFlr15Min_Type(Unsigned32WithNA):
    """Custom type soamPmLmStatsBackwardMinFlr15Min based on Unsigned32WithNA"""
    defaultValue = 4294967294

    subtypeSpec = Unsigned32WithNA.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
        ValueRangeConstraint(4294967294, 4294967294),
    )


_SoamPmLmStatsBackwardMinFlr15Min_Type.__name__ = "Unsigned32WithNA"
_SoamPmLmStatsBackwardMinFlr15Min_Object = MibTableColumn
soamPmLmStatsBackwardMinFlr15Min = _SoamPmLmStatsBackwardMinFlr15Min_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 60, 2, 2, 2, 1, 25),
    _SoamPmLmStatsBackwardMinFlr15Min_Type()
)
soamPmLmStatsBackwardMinFlr15Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    soamPmLmStatsBackwardMinFlr15Min.setStatus("current")


class _SoamPmLmStatsBackwardMaxFlr15Min_Type(Unsigned32):
    """Custom type soamPmLmStatsBackwardMaxFlr15Min based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_SoamPmLmStatsBackwardMaxFlr15Min_Type.__name__ = "Unsigned32"
_SoamPmLmStatsBackwardMaxFlr15Min_Object = MibTableColumn
soamPmLmStatsBackwardMaxFlr15Min = _SoamPmLmStatsBackwardMaxFlr15Min_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 60, 2, 2, 2, 1, 26),
    _SoamPmLmStatsBackwardMaxFlr15Min_Type()
)
soamPmLmStatsBackwardMaxFlr15Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    soamPmLmStatsBackwardMaxFlr15Min.setStatus("current")


class _SoamPmLmStatsBackwardAvgFlr15Min_Type(Unsigned32):
    """Custom type soamPmLmStatsBackwardAvgFlr15Min based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
        ValueRangeConstraint(4294967295, 4294967295),
    )


_SoamPmLmStatsBackwardAvgFlr15Min_Type.__name__ = "Unsigned32"
_SoamPmLmStatsBackwardAvgFlr15Min_Object = MibTableColumn
soamPmLmStatsBackwardAvgFlr15Min = _SoamPmLmStatsBackwardAvgFlr15Min_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 60, 2, 2, 2, 1, 27),
    _SoamPmLmStatsBackwardAvgFlr15Min_Type()
)
soamPmLmStatsBackwardAvgFlr15Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    soamPmLmStatsBackwardAvgFlr15Min.setStatus("current")
_SoamPmLmStatsBackwardHighLoss15Min_Type = Unsigned32
_SoamPmLmStatsBackwardHighLoss15Min_Object = MibTableColumn
soamPmLmStatsBackwardHighLoss15Min = _SoamPmLmStatsBackwardHighLoss15Min_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 60, 2, 2, 2, 1, 28),
    _SoamPmLmStatsBackwardHighLoss15Min_Type()
)
soamPmLmStatsBackwardHighLoss15Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    soamPmLmStatsBackwardHighLoss15Min.setStatus("current")
_SoamPmLmStatsUnavailableSeconds15Min_Type = Unsigned32
_SoamPmLmStatsUnavailableSeconds15Min_Object = MibTableColumn
soamPmLmStatsUnavailableSeconds15Min = _SoamPmLmStatsUnavailableSeconds15Min_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 60, 2, 2, 2, 1, 29),
    _SoamPmLmStatsUnavailableSeconds15Min_Type()
)
soamPmLmStatsUnavailableSeconds15Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    soamPmLmStatsUnavailableSeconds15Min.setStatus("current")
_SoamPmLmStatsStartTimePrevious15Min_Type = DateAndTime
_SoamPmLmStatsStartTimePrevious15Min_Object = MibTableColumn
soamPmLmStatsStartTimePrevious15Min = _SoamPmLmStatsStartTimePrevious15Min_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 60, 2, 2, 2, 1, 30),
    _SoamPmLmStatsStartTimePrevious15Min_Type()
)
soamPmLmStatsStartTimePrevious15Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    soamPmLmStatsStartTimePrevious15Min.setStatus("current")
_SoamPmLmStatsElapsedTimePrevious15Min_Type = TimeInterval
_SoamPmLmStatsElapsedTimePrevious15Min_Object = MibTableColumn
soamPmLmStatsElapsedTimePrevious15Min = _SoamPmLmStatsElapsedTimePrevious15Min_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 60, 2, 2, 2, 1, 31),
    _SoamPmLmStatsElapsedTimePrevious15Min_Type()
)
soamPmLmStatsElapsedTimePrevious15Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    soamPmLmStatsElapsedTimePrevious15Min.setStatus("current")
_SoamPmLmStatsForwardTransmittedFramesPrevious15Min_Type = Counter64
_SoamPmLmStatsForwardTransmittedFramesPrevious15Min_Object = MibTableColumn
soamPmLmStatsForwardTransmittedFramesPrevious15Min = _SoamPmLmStatsForwardTransmittedFramesPrevious15Min_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 60, 2, 2, 2, 1, 32),
    _SoamPmLmStatsForwardTransmittedFramesPrevious15Min_Type()
)
soamPmLmStatsForwardTransmittedFramesPrevious15Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    soamPmLmStatsForwardTransmittedFramesPrevious15Min.setStatus("current")
_SoamPmLmStatsForwardReceivedFramesPrevious15Min_Type = Counter64
_SoamPmLmStatsForwardReceivedFramesPrevious15Min_Object = MibTableColumn
soamPmLmStatsForwardReceivedFramesPrevious15Min = _SoamPmLmStatsForwardReceivedFramesPrevious15Min_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 60, 2, 2, 2, 1, 33),
    _SoamPmLmStatsForwardReceivedFramesPrevious15Min_Type()
)
soamPmLmStatsForwardReceivedFramesPrevious15Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    soamPmLmStatsForwardReceivedFramesPrevious15Min.setStatus("current")


class _SoamPmLmStatsForwardMinFlrPrevious15Min_Type(Unsigned32WithNA):
    """Custom type soamPmLmStatsForwardMinFlrPrevious15Min based on Unsigned32WithNA"""
    defaultValue = 4294967294

    subtypeSpec = Unsigned32WithNA.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
        ValueRangeConstraint(4294967294, 4294967294),
    )


_SoamPmLmStatsForwardMinFlrPrevious15Min_Type.__name__ = "Unsigned32WithNA"
_SoamPmLmStatsForwardMinFlrPrevious15Min_Object = MibTableColumn
soamPmLmStatsForwardMinFlrPrevious15Min = _SoamPmLmStatsForwardMinFlrPrevious15Min_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 60, 2, 2, 2, 1, 34),
    _SoamPmLmStatsForwardMinFlrPrevious15Min_Type()
)
soamPmLmStatsForwardMinFlrPrevious15Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    soamPmLmStatsForwardMinFlrPrevious15Min.setStatus("current")


class _SoamPmLmStatsForwardMaxFlrPrevious15Min_Type(Unsigned32):
    """Custom type soamPmLmStatsForwardMaxFlrPrevious15Min based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_SoamPmLmStatsForwardMaxFlrPrevious15Min_Type.__name__ = "Unsigned32"
_SoamPmLmStatsForwardMaxFlrPrevious15Min_Object = MibTableColumn
soamPmLmStatsForwardMaxFlrPrevious15Min = _SoamPmLmStatsForwardMaxFlrPrevious15Min_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 60, 2, 2, 2, 1, 35),
    _SoamPmLmStatsForwardMaxFlrPrevious15Min_Type()
)
soamPmLmStatsForwardMaxFlrPrevious15Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    soamPmLmStatsForwardMaxFlrPrevious15Min.setStatus("current")


class _SoamPmLmStatsForwardAvgFlrPrevious15Min_Type(Unsigned32):
    """Custom type soamPmLmStatsForwardAvgFlrPrevious15Min based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_SoamPmLmStatsForwardAvgFlrPrevious15Min_Type.__name__ = "Unsigned32"
_SoamPmLmStatsForwardAvgFlrPrevious15Min_Object = MibTableColumn
soamPmLmStatsForwardAvgFlrPrevious15Min = _SoamPmLmStatsForwardAvgFlrPrevious15Min_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 60, 2, 2, 2, 1, 36),
    _SoamPmLmStatsForwardAvgFlrPrevious15Min_Type()
)
soamPmLmStatsForwardAvgFlrPrevious15Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    soamPmLmStatsForwardAvgFlrPrevious15Min.setStatus("current")
_SoamPmLmStatsForwardHighLossPrevious15Min_Type = Unsigned32
_SoamPmLmStatsForwardHighLossPrevious15Min_Object = MibTableColumn
soamPmLmStatsForwardHighLossPrevious15Min = _SoamPmLmStatsForwardHighLossPrevious15Min_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 60, 2, 2, 2, 1, 37),
    _SoamPmLmStatsForwardHighLossPrevious15Min_Type()
)
soamPmLmStatsForwardHighLossPrevious15Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    soamPmLmStatsForwardHighLossPrevious15Min.setStatus("current")
_SoamPmLmStatsBackwardTransmittedFramesPrevious15Min_Type = Counter64
_SoamPmLmStatsBackwardTransmittedFramesPrevious15Min_Object = MibTableColumn
soamPmLmStatsBackwardTransmittedFramesPrevious15Min = _SoamPmLmStatsBackwardTransmittedFramesPrevious15Min_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 60, 2, 2, 2, 1, 38),
    _SoamPmLmStatsBackwardTransmittedFramesPrevious15Min_Type()
)
soamPmLmStatsBackwardTransmittedFramesPrevious15Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    soamPmLmStatsBackwardTransmittedFramesPrevious15Min.setStatus("current")
_SoamPmLmStatsBackwardReceivedFramesPrevious15Min_Type = Counter64
_SoamPmLmStatsBackwardReceivedFramesPrevious15Min_Object = MibTableColumn
soamPmLmStatsBackwardReceivedFramesPrevious15Min = _SoamPmLmStatsBackwardReceivedFramesPrevious15Min_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 60, 2, 2, 2, 1, 39),
    _SoamPmLmStatsBackwardReceivedFramesPrevious15Min_Type()
)
soamPmLmStatsBackwardReceivedFramesPrevious15Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    soamPmLmStatsBackwardReceivedFramesPrevious15Min.setStatus("current")


class _SoamPmLmStatsBackwardMinFlrPrevious15Min_Type(Unsigned32WithNA):
    """Custom type soamPmLmStatsBackwardMinFlrPrevious15Min based on Unsigned32WithNA"""
    defaultValue = 4294967294

    subtypeSpec = Unsigned32WithNA.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
        ValueRangeConstraint(4294967294, 4294967294),
    )


_SoamPmLmStatsBackwardMinFlrPrevious15Min_Type.__name__ = "Unsigned32WithNA"
_SoamPmLmStatsBackwardMinFlrPrevious15Min_Object = MibTableColumn
soamPmLmStatsBackwardMinFlrPrevious15Min = _SoamPmLmStatsBackwardMinFlrPrevious15Min_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 60, 2, 2, 2, 1, 40),
    _SoamPmLmStatsBackwardMinFlrPrevious15Min_Type()
)
soamPmLmStatsBackwardMinFlrPrevious15Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    soamPmLmStatsBackwardMinFlrPrevious15Min.setStatus("current")


class _SoamPmLmStatsBackwardMaxFlrPrevious15Min_Type(Unsigned32):
    """Custom type soamPmLmStatsBackwardMaxFlrPrevious15Min based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_SoamPmLmStatsBackwardMaxFlrPrevious15Min_Type.__name__ = "Unsigned32"
_SoamPmLmStatsBackwardMaxFlrPrevious15Min_Object = MibTableColumn
soamPmLmStatsBackwardMaxFlrPrevious15Min = _SoamPmLmStatsBackwardMaxFlrPrevious15Min_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 60, 2, 2, 2, 1, 41),
    _SoamPmLmStatsBackwardMaxFlrPrevious15Min_Type()
)
soamPmLmStatsBackwardMaxFlrPrevious15Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    soamPmLmStatsBackwardMaxFlrPrevious15Min.setStatus("current")


class _SoamPmLmStatsBackwardAvgFlrPrevious15Min_Type(Unsigned32):
    """Custom type soamPmLmStatsBackwardAvgFlrPrevious15Min based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_SoamPmLmStatsBackwardAvgFlrPrevious15Min_Type.__name__ = "Unsigned32"
_SoamPmLmStatsBackwardAvgFlrPrevious15Min_Object = MibTableColumn
soamPmLmStatsBackwardAvgFlrPrevious15Min = _SoamPmLmStatsBackwardAvgFlrPrevious15Min_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 60, 2, 2, 2, 1, 42),
    _SoamPmLmStatsBackwardAvgFlrPrevious15Min_Type()
)
soamPmLmStatsBackwardAvgFlrPrevious15Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    soamPmLmStatsBackwardAvgFlrPrevious15Min.setStatus("current")
_SoamPmLmStatsBackwardHighLossPrevious15Min_Type = Unsigned32
_SoamPmLmStatsBackwardHighLossPrevious15Min_Object = MibTableColumn
soamPmLmStatsBackwardHighLossPrevious15Min = _SoamPmLmStatsBackwardHighLossPrevious15Min_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 60, 2, 2, 2, 1, 43),
    _SoamPmLmStatsBackwardHighLossPrevious15Min_Type()
)
soamPmLmStatsBackwardHighLossPrevious15Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    soamPmLmStatsBackwardHighLossPrevious15Min.setStatus("current")
_SoamPmLmStatsStartTime24H_Type = DateAndTime
_SoamPmLmStatsStartTime24H_Object = MibTableColumn
soamPmLmStatsStartTime24H = _SoamPmLmStatsStartTime24H_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 60, 2, 2, 2, 1, 44),
    _SoamPmLmStatsStartTime24H_Type()
)
soamPmLmStatsStartTime24H.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    soamPmLmStatsStartTime24H.setStatus("current")
_SoamPmLmStatsElapsedTime24H_Type = TimeInterval
_SoamPmLmStatsElapsedTime24H_Object = MibTableColumn
soamPmLmStatsElapsedTime24H = _SoamPmLmStatsElapsedTime24H_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 60, 2, 2, 2, 1, 45),
    _SoamPmLmStatsElapsedTime24H_Type()
)
soamPmLmStatsElapsedTime24H.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    soamPmLmStatsElapsedTime24H.setStatus("current")
_SoamPmLmStatsForwardTransmittedFrames24H_Type = Counter64
_SoamPmLmStatsForwardTransmittedFrames24H_Object = MibTableColumn
soamPmLmStatsForwardTransmittedFrames24H = _SoamPmLmStatsForwardTransmittedFrames24H_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 60, 2, 2, 2, 1, 46),
    _SoamPmLmStatsForwardTransmittedFrames24H_Type()
)
soamPmLmStatsForwardTransmittedFrames24H.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    soamPmLmStatsForwardTransmittedFrames24H.setStatus("current")
_SoamPmLmStatsForwardReceivedFrames24H_Type = Counter64
_SoamPmLmStatsForwardReceivedFrames24H_Object = MibTableColumn
soamPmLmStatsForwardReceivedFrames24H = _SoamPmLmStatsForwardReceivedFrames24H_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 60, 2, 2, 2, 1, 47),
    _SoamPmLmStatsForwardReceivedFrames24H_Type()
)
soamPmLmStatsForwardReceivedFrames24H.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    soamPmLmStatsForwardReceivedFrames24H.setStatus("current")


class _SoamPmLmStatsForwardMinFlr24H_Type(Unsigned32WithNA):
    """Custom type soamPmLmStatsForwardMinFlr24H based on Unsigned32WithNA"""
    defaultValue = 4294967294

    subtypeSpec = Unsigned32WithNA.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
        ValueRangeConstraint(4294967294, 4294967294),
    )


_SoamPmLmStatsForwardMinFlr24H_Type.__name__ = "Unsigned32WithNA"
_SoamPmLmStatsForwardMinFlr24H_Object = MibTableColumn
soamPmLmStatsForwardMinFlr24H = _SoamPmLmStatsForwardMinFlr24H_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 60, 2, 2, 2, 1, 48),
    _SoamPmLmStatsForwardMinFlr24H_Type()
)
soamPmLmStatsForwardMinFlr24H.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    soamPmLmStatsForwardMinFlr24H.setStatus("current")


class _SoamPmLmStatsForwardMaxFlr24H_Type(Unsigned32):
    """Custom type soamPmLmStatsForwardMaxFlr24H based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_SoamPmLmStatsForwardMaxFlr24H_Type.__name__ = "Unsigned32"
_SoamPmLmStatsForwardMaxFlr24H_Object = MibTableColumn
soamPmLmStatsForwardMaxFlr24H = _SoamPmLmStatsForwardMaxFlr24H_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 60, 2, 2, 2, 1, 49),
    _SoamPmLmStatsForwardMaxFlr24H_Type()
)
soamPmLmStatsForwardMaxFlr24H.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    soamPmLmStatsForwardMaxFlr24H.setStatus("current")


class _SoamPmLmStatsForwardAvgFlr24H_Type(Unsigned32):
    """Custom type soamPmLmStatsForwardAvgFlr24H based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_SoamPmLmStatsForwardAvgFlr24H_Type.__name__ = "Unsigned32"
_SoamPmLmStatsForwardAvgFlr24H_Object = MibTableColumn
soamPmLmStatsForwardAvgFlr24H = _SoamPmLmStatsForwardAvgFlr24H_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 60, 2, 2, 2, 1, 50),
    _SoamPmLmStatsForwardAvgFlr24H_Type()
)
soamPmLmStatsForwardAvgFlr24H.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    soamPmLmStatsForwardAvgFlr24H.setStatus("current")
_SoamPmLmStatsForwardHighLoss24H_Type = Unsigned32
_SoamPmLmStatsForwardHighLoss24H_Object = MibTableColumn
soamPmLmStatsForwardHighLoss24H = _SoamPmLmStatsForwardHighLoss24H_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 60, 2, 2, 2, 1, 51),
    _SoamPmLmStatsForwardHighLoss24H_Type()
)
soamPmLmStatsForwardHighLoss24H.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    soamPmLmStatsForwardHighLoss24H.setStatus("current")
_SoamPmLmStatsBackwardTransmittedFrames24H_Type = Counter64
_SoamPmLmStatsBackwardTransmittedFrames24H_Object = MibTableColumn
soamPmLmStatsBackwardTransmittedFrames24H = _SoamPmLmStatsBackwardTransmittedFrames24H_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 60, 2, 2, 2, 1, 52),
    _SoamPmLmStatsBackwardTransmittedFrames24H_Type()
)
soamPmLmStatsBackwardTransmittedFrames24H.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    soamPmLmStatsBackwardTransmittedFrames24H.setStatus("current")
_SoamPmLmStatsBackwardReceivedFrames24H_Type = Counter64
_SoamPmLmStatsBackwardReceivedFrames24H_Object = MibTableColumn
soamPmLmStatsBackwardReceivedFrames24H = _SoamPmLmStatsBackwardReceivedFrames24H_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 60, 2, 2, 2, 1, 53),
    _SoamPmLmStatsBackwardReceivedFrames24H_Type()
)
soamPmLmStatsBackwardReceivedFrames24H.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    soamPmLmStatsBackwardReceivedFrames24H.setStatus("current")


class _SoamPmLmStatsBackwardMinFlr24H_Type(Unsigned32WithNA):
    """Custom type soamPmLmStatsBackwardMinFlr24H based on Unsigned32WithNA"""
    defaultValue = 4294967294

    subtypeSpec = Unsigned32WithNA.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
        ValueRangeConstraint(4294967294, 4294967294),
    )


_SoamPmLmStatsBackwardMinFlr24H_Type.__name__ = "Unsigned32WithNA"
_SoamPmLmStatsBackwardMinFlr24H_Object = MibTableColumn
soamPmLmStatsBackwardMinFlr24H = _SoamPmLmStatsBackwardMinFlr24H_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 60, 2, 2, 2, 1, 54),
    _SoamPmLmStatsBackwardMinFlr24H_Type()
)
soamPmLmStatsBackwardMinFlr24H.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    soamPmLmStatsBackwardMinFlr24H.setStatus("current")


class _SoamPmLmStatsBackwardMaxFlr24H_Type(Unsigned32):
    """Custom type soamPmLmStatsBackwardMaxFlr24H based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_SoamPmLmStatsBackwardMaxFlr24H_Type.__name__ = "Unsigned32"
_SoamPmLmStatsBackwardMaxFlr24H_Object = MibTableColumn
soamPmLmStatsBackwardMaxFlr24H = _SoamPmLmStatsBackwardMaxFlr24H_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 60, 2, 2, 2, 1, 55),
    _SoamPmLmStatsBackwardMaxFlr24H_Type()
)
soamPmLmStatsBackwardMaxFlr24H.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    soamPmLmStatsBackwardMaxFlr24H.setStatus("current")


class _SoamPmLmStatsBackwardAvgFlr24H_Type(Unsigned32):
    """Custom type soamPmLmStatsBackwardAvgFlr24H based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_SoamPmLmStatsBackwardAvgFlr24H_Type.__name__ = "Unsigned32"
_SoamPmLmStatsBackwardAvgFlr24H_Object = MibTableColumn
soamPmLmStatsBackwardAvgFlr24H = _SoamPmLmStatsBackwardAvgFlr24H_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 60, 2, 2, 2, 1, 56),
    _SoamPmLmStatsBackwardAvgFlr24H_Type()
)
soamPmLmStatsBackwardAvgFlr24H.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    soamPmLmStatsBackwardAvgFlr24H.setStatus("current")
_SoamPmLmStatsBackwardHighLoss24H_Type = Unsigned32
_SoamPmLmStatsBackwardHighLoss24H_Object = MibTableColumn
soamPmLmStatsBackwardHighLoss24H = _SoamPmLmStatsBackwardHighLoss24H_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 60, 2, 2, 2, 1, 57),
    _SoamPmLmStatsBackwardHighLoss24H_Type()
)
soamPmLmStatsBackwardHighLoss24H.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    soamPmLmStatsBackwardHighLoss24H.setStatus("current")
_SoamPmLmStatsUas_Type = FaultStatus
_SoamPmLmStatsUas_Object = MibTableColumn
soamPmLmStatsUas = _SoamPmLmStatsUas_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 60, 2, 2, 2, 1, 58),
    _SoamPmLmStatsUas_Type()
)
soamPmLmStatsUas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    soamPmLmStatsUas.setStatus("current")


class _SoamPmLmStatsPriority_Type(IEEE8021PriorityValue):
    """Custom type soamPmLmStatsPriority based on IEEE8021PriorityValue"""
    defaultValue = 0


_SoamPmLmStatsPriority_Type.__name__ = "IEEE8021PriorityValue"
_SoamPmLmStatsPriority_Object = MibTableColumn
soamPmLmStatsPriority = _SoamPmLmStatsPriority_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 60, 2, 2, 2, 1, 59),
    _SoamPmLmStatsPriority_Type()
)
soamPmLmStatsPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    soamPmLmStatsPriority.setStatus("current")
_SoamPmDmObjects_ObjectIdentity = ObjectIdentity
soamPmDmObjects = _SoamPmDmObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 60, 2, 3)
)
_SoamPmDmCfgTable_Object = MibTable
soamPmDmCfgTable = _SoamPmDmCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 60, 2, 3, 1)
)
if mibBuilder.loadTexts:
    soamPmDmCfgTable.setStatus("current")
_SoamPmDmCfgEntry_Object = MibTableRow
soamPmDmCfgEntry = _SoamPmDmCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 60, 2, 3, 1, 1)
)
soamPmDmCfgEntry.setIndexNames(
    (0, "LUM-SOAM-PM-MIB", "soamPmDmCfgIndex"),
)
if mibBuilder.loadTexts:
    soamPmDmCfgEntry.setStatus("current")


class _SoamPmDmCfgIndex_Type(Unsigned32):
    """Custom type soamPmDmCfgIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_SoamPmDmCfgIndex_Type.__name__ = "Unsigned32"
_SoamPmDmCfgIndex_Object = MibTableColumn
soamPmDmCfgIndex = _SoamPmDmCfgIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 60, 2, 3, 1, 1, 1),
    _SoamPmDmCfgIndex_Type()
)
soamPmDmCfgIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    soamPmDmCfgIndex.setStatus("current")
_SoamPmDmCfgName_Type = MgmtNameString
_SoamPmDmCfgName_Object = MibTableColumn
soamPmDmCfgName = _SoamPmDmCfgName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 60, 2, 3, 1, 1, 2),
    _SoamPmDmCfgName_Type()
)
soamPmDmCfgName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    soamPmDmCfgName.setStatus("current")


class _SoamPmDmCfgDescr_Type(DisplayString):
    """Custom type soamPmDmCfgDescr based on DisplayString"""
    defaultValue = OctetString("")


_SoamPmDmCfgDescr_Type.__name__ = "DisplayString"
_SoamPmDmCfgDescr_Object = MibTableColumn
soamPmDmCfgDescr = _SoamPmDmCfgDescr_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 60, 2, 3, 1, 1, 3),
    _SoamPmDmCfgDescr_Type()
)
soamPmDmCfgDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    soamPmDmCfgDescr.setStatus("current")
_SoamPmDmCfgSubrack_Type = SubrackNumber
_SoamPmDmCfgSubrack_Object = MibTableColumn
soamPmDmCfgSubrack = _SoamPmDmCfgSubrack_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 60, 2, 3, 1, 1, 4),
    _SoamPmDmCfgSubrack_Type()
)
soamPmDmCfgSubrack.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    soamPmDmCfgSubrack.setStatus("current")
_SoamPmDmCfgSlot_Type = SlotNumber
_SoamPmDmCfgSlot_Object = MibTableColumn
soamPmDmCfgSlot = _SoamPmDmCfgSlot_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 60, 2, 3, 1, 1, 5),
    _SoamPmDmCfgSlot_Type()
)
soamPmDmCfgSlot.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    soamPmDmCfgSlot.setStatus("current")


class _SoamPmDmCfgInternalReference_Type(Unsigned32):
    """Custom type soamPmDmCfgInternalReference based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_SoamPmDmCfgInternalReference_Type.__name__ = "Unsigned32"
_SoamPmDmCfgInternalReference_Object = MibTableColumn
soamPmDmCfgInternalReference = _SoamPmDmCfgInternalReference_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 60, 2, 3, 1, 1, 6),
    _SoamPmDmCfgInternalReference_Type()
)
soamPmDmCfgInternalReference.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    soamPmDmCfgInternalReference.setStatus("current")


class _SoamPmDmCfgLocalDeviceType_Type(Integer32):
    """Custom type soamPmDmCfgLocalDeviceType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("emxp", 1),
          ("nidGe", 2))
    )


_SoamPmDmCfgLocalDeviceType_Type.__name__ = "Integer32"
_SoamPmDmCfgLocalDeviceType_Object = MibTableColumn
soamPmDmCfgLocalDeviceType = _SoamPmDmCfgLocalDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 60, 2, 3, 1, 1, 7),
    _SoamPmDmCfgLocalDeviceType_Type()
)
soamPmDmCfgLocalDeviceType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    soamPmDmCfgLocalDeviceType.setStatus("current")


class _SoamPmDmCfgDropEligible_Type(TruthValue):
    """Custom type soamPmDmCfgDropEligible based on TruthValue"""
    defaultValue = 2


_SoamPmDmCfgDropEligible_Type.__name__ = "TruthValue"
_SoamPmDmCfgDropEligible_Object = MibTableColumn
soamPmDmCfgDropEligible = _SoamPmDmCfgDropEligible_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 60, 2, 3, 1, 1, 8),
    _SoamPmDmCfgDropEligible_Type()
)
soamPmDmCfgDropEligible.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    soamPmDmCfgDropEligible.setStatus("current")


class _SoamPmDmCfgType_Type(Integer32):
    """Custom type soamPmDmCfgType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dmDmm", 1),
          ("dm1DmTx", 2),
          ("dm1DmRx", 3))
    )


_SoamPmDmCfgType_Type.__name__ = "Integer32"
_SoamPmDmCfgType_Object = MibTableColumn
soamPmDmCfgType = _SoamPmDmCfgType_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 60, 2, 3, 1, 1, 9),
    _SoamPmDmCfgType_Type()
)
soamPmDmCfgType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    soamPmDmCfgType.setStatus("current")


class _SoamPmDmCfgEnabled_Type(TruthValue):
    """Custom type soamPmDmCfgEnabled based on TruthValue"""
    defaultValue = 1


_SoamPmDmCfgEnabled_Type.__name__ = "TruthValue"
_SoamPmDmCfgEnabled_Object = MibTableColumn
soamPmDmCfgEnabled = _SoamPmDmCfgEnabled_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 60, 2, 3, 1, 1, 10),
    _SoamPmDmCfgEnabled_Type()
)
soamPmDmCfgEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    soamPmDmCfgEnabled.setStatus("current")


class _SoamPmDmCfgMessagePeriod_Type(Integer32):
    """Custom type soamPmDmCfgMessagePeriod based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("interval100ms", 0),
          ("interval1s", 1),
          ("interval10s", 2))
    )


_SoamPmDmCfgMessagePeriod_Type.__name__ = "Integer32"
_SoamPmDmCfgMessagePeriod_Object = MibTableColumn
soamPmDmCfgMessagePeriod = _SoamPmDmCfgMessagePeriod_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 60, 2, 3, 1, 1, 11),
    _SoamPmDmCfgMessagePeriod_Type()
)
soamPmDmCfgMessagePeriod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    soamPmDmCfgMessagePeriod.setStatus("current")


class _SoamPmDmCfgPriority_Type(IEEE8021PriorityValue):
    """Custom type soamPmDmCfgPriority based on IEEE8021PriorityValue"""
    defaultValue = 0


_SoamPmDmCfgPriority_Type.__name__ = "IEEE8021PriorityValue"
_SoamPmDmCfgPriority_Object = MibTableColumn
soamPmDmCfgPriority = _SoamPmDmCfgPriority_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 60, 2, 3, 1, 1, 12),
    _SoamPmDmCfgPriority_Type()
)
soamPmDmCfgPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    soamPmDmCfgPriority.setStatus("current")
_SoamPmDmCfgDestMacAddress_Type = MacAddress
_SoamPmDmCfgDestMacAddress_Object = MibTableColumn
soamPmDmCfgDestMacAddress = _SoamPmDmCfgDestMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 60, 2, 3, 1, 1, 13),
    _SoamPmDmCfgDestMacAddress_Type()
)
soamPmDmCfgDestMacAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    soamPmDmCfgDestMacAddress.setStatus("current")
_SoamPmDmCfgMepName_Type = DisplayString
_SoamPmDmCfgMepName_Object = MibTableColumn
soamPmDmCfgMepName = _SoamPmDmCfgMepName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 60, 2, 3, 1, 1, 14),
    _SoamPmDmCfgMepName_Type()
)
soamPmDmCfgMepName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    soamPmDmCfgMepName.setStatus("current")


class _SoamPmDmCfgMaidIdentifier_Type(DisplayString):
    """Custom type soamPmDmCfgMaidIdentifier based on DisplayString"""
    defaultValue = OctetString("")


_SoamPmDmCfgMaidIdentifier_Type.__name__ = "DisplayString"
_SoamPmDmCfgMaidIdentifier_Object = MibTableColumn
soamPmDmCfgMaidIdentifier = _SoamPmDmCfgMaidIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 60, 2, 3, 1, 1, 15),
    _SoamPmDmCfgMaidIdentifier_Type()
)
soamPmDmCfgMaidIdentifier.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    soamPmDmCfgMaidIdentifier.setStatus("current")


class _SoamPmDmCfgDestMepId_Type(Dot1agCfmMepIdOrZero):
    """Custom type soamPmDmCfgDestMepId based on Dot1agCfmMepIdOrZero"""
    defaultValue = 0


_SoamPmDmCfgDestMepId_Type.__name__ = "Dot1agCfmMepIdOrZero"
_SoamPmDmCfgDestMepId_Object = MibTableColumn
soamPmDmCfgDestMepId = _SoamPmDmCfgDestMepId_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 60, 2, 3, 1, 1, 16),
    _SoamPmDmCfgDestMepId_Type()
)
soamPmDmCfgDestMepId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    soamPmDmCfgDestMepId.setStatus("current")


class _SoamPmDmCfgDestIsMepId_Type(TruthValue):
    """Custom type soamPmDmCfgDestIsMepId based on TruthValue"""
    defaultValue = 1


_SoamPmDmCfgDestIsMepId_Type.__name__ = "TruthValue"
_SoamPmDmCfgDestIsMepId_Object = MibTableColumn
soamPmDmCfgDestIsMepId = _SoamPmDmCfgDestIsMepId_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 60, 2, 3, 1, 1, 17),
    _SoamPmDmCfgDestIsMepId_Type()
)
soamPmDmCfgDestIsMepId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    soamPmDmCfgDestIsMepId.setStatus("current")


class _SoamPmDmCfgSessionType_Type(MefSoamTcSessionType):
    """Custom type soamPmDmCfgSessionType based on MefSoamTcSessionType"""
    defaultValue = 1


_SoamPmDmCfgSessionType_Type.__name__ = "MefSoamTcSessionType"
_SoamPmDmCfgSessionType_Object = MibTableColumn
soamPmDmCfgSessionType = _SoamPmDmCfgSessionType_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 60, 2, 3, 1, 1, 18),
    _SoamPmDmCfgSessionType_Type()
)
soamPmDmCfgSessionType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    soamPmDmCfgSessionType.setStatus("current")
_SoamPmDmCfgSessionStatus_Type = MefSoamTcStatusType
_SoamPmDmCfgSessionStatus_Object = MibTableColumn
soamPmDmCfgSessionStatus = _SoamPmDmCfgSessionStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 60, 2, 3, 1, 1, 19),
    _SoamPmDmCfgSessionStatus_Type()
)
soamPmDmCfgSessionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    soamPmDmCfgSessionStatus.setStatus("current")
_SoamPmDmCfgRowStatus_Type = RowStatus
_SoamPmDmCfgRowStatus_Object = MibTableColumn
soamPmDmCfgRowStatus = _SoamPmDmCfgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 60, 2, 3, 1, 1, 20),
    _SoamPmDmCfgRowStatus_Type()
)
soamPmDmCfgRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    soamPmDmCfgRowStatus.setStatus("current")


class _SoamPmDmCfgAdminStatus_Type(BoardOrInterfaceAdminStatus):
    """Custom type soamPmDmCfgAdminStatus based on BoardOrInterfaceAdminStatus"""
    defaultValue = 3


_SoamPmDmCfgAdminStatus_Type.__name__ = "BoardOrInterfaceAdminStatus"
_SoamPmDmCfgAdminStatus_Object = MibTableColumn
soamPmDmCfgAdminStatus = _SoamPmDmCfgAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 60, 2, 3, 1, 1, 21),
    _SoamPmDmCfgAdminStatus_Type()
)
soamPmDmCfgAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    soamPmDmCfgAdminStatus.setStatus("current")
_SoamPmDmCfgOperStatus_Type = BoardOrInterfaceOperStatus
_SoamPmDmCfgOperStatus_Object = MibTableColumn
soamPmDmCfgOperStatus = _SoamPmDmCfgOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 60, 2, 3, 1, 1, 22),
    _SoamPmDmCfgOperStatus_Type()
)
soamPmDmCfgOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    soamPmDmCfgOperStatus.setStatus("current")
_SoamPmDmCfgStats_Type = CommandString
_SoamPmDmCfgStats_Object = MibTableColumn
soamPmDmCfgStats = _SoamPmDmCfgStats_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 60, 2, 3, 1, 1, 23),
    _SoamPmDmCfgStats_Type()
)
soamPmDmCfgStats.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    soamPmDmCfgStats.setStatus("current")
_SoamPmDmStatsTable_Object = MibTable
soamPmDmStatsTable = _SoamPmDmStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 60, 2, 3, 2)
)
if mibBuilder.loadTexts:
    soamPmDmStatsTable.setStatus("current")
_SoamPmDmStatsEntry_Object = MibTableRow
soamPmDmStatsEntry = _SoamPmDmStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 60, 2, 3, 2, 1)
)
soamPmDmStatsEntry.setIndexNames(
    (0, "LUM-SOAM-PM-MIB", "soamPmDmStatsIndex"),
)
if mibBuilder.loadTexts:
    soamPmDmStatsEntry.setStatus("current")
_SoamPmDmStatsIndex_Type = Unsigned32
_SoamPmDmStatsIndex_Object = MibTableColumn
soamPmDmStatsIndex = _SoamPmDmStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 60, 2, 3, 2, 1, 1),
    _SoamPmDmStatsIndex_Type()
)
soamPmDmStatsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    soamPmDmStatsIndex.setStatus("current")


class _SoamPmDmStatsLocalDeviceType_Type(Integer32):
    """Custom type soamPmDmStatsLocalDeviceType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("emxp", 1),
          ("nidGe", 2))
    )


_SoamPmDmStatsLocalDeviceType_Type.__name__ = "Integer32"
_SoamPmDmStatsLocalDeviceType_Object = MibTableColumn
soamPmDmStatsLocalDeviceType = _SoamPmDmStatsLocalDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 60, 2, 3, 2, 1, 2),
    _SoamPmDmStatsLocalDeviceType_Type()
)
soamPmDmStatsLocalDeviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    soamPmDmStatsLocalDeviceType.setStatus("current")
_SoamPmDmStatsName_Type = MgmtNameString
_SoamPmDmStatsName_Object = MibTableColumn
soamPmDmStatsName = _SoamPmDmStatsName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 60, 2, 3, 2, 1, 3),
    _SoamPmDmStatsName_Type()
)
soamPmDmStatsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    soamPmDmStatsName.setStatus("current")
_SoamPmDmStatsSubrack_Type = SubrackNumber
_SoamPmDmStatsSubrack_Object = MibTableColumn
soamPmDmStatsSubrack = _SoamPmDmStatsSubrack_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 60, 2, 3, 2, 1, 4),
    _SoamPmDmStatsSubrack_Type()
)
soamPmDmStatsSubrack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    soamPmDmStatsSubrack.setStatus("current")
_SoamPmDmStatsSlot_Type = SlotNumber
_SoamPmDmStatsSlot_Object = MibTableColumn
soamPmDmStatsSlot = _SoamPmDmStatsSlot_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 60, 2, 3, 2, 1, 5),
    _SoamPmDmStatsSlot_Type()
)
soamPmDmStatsSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    soamPmDmStatsSlot.setStatus("current")


class _SoamPmDmStatsMaidIdentifier_Type(DisplayString):
    """Custom type soamPmDmStatsMaidIdentifier based on DisplayString"""
    defaultValue = OctetString("")


_SoamPmDmStatsMaidIdentifier_Type.__name__ = "DisplayString"
_SoamPmDmStatsMaidIdentifier_Object = MibTableColumn
soamPmDmStatsMaidIdentifier = _SoamPmDmStatsMaidIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 60, 2, 3, 2, 1, 6),
    _SoamPmDmStatsMaidIdentifier_Type()
)
soamPmDmStatsMaidIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    soamPmDmStatsMaidIdentifier.setStatus("current")


class _SoamPmDmStatsDestMepId_Type(Dot1agCfmMepIdOrZero):
    """Custom type soamPmDmStatsDestMepId based on Dot1agCfmMepIdOrZero"""
    defaultValue = 0


_SoamPmDmStatsDestMepId_Type.__name__ = "Dot1agCfmMepIdOrZero"
_SoamPmDmStatsDestMepId_Object = MibTableColumn
soamPmDmStatsDestMepId = _SoamPmDmStatsDestMepId_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 60, 2, 3, 2, 1, 7),
    _SoamPmDmStatsDestMepId_Type()
)
soamPmDmStatsDestMepId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    soamPmDmStatsDestMepId.setStatus("current")


class _SoamPmDmStatsInternalReference_Type(Unsigned32):
    """Custom type soamPmDmStatsInternalReference based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_SoamPmDmStatsInternalReference_Type.__name__ = "Unsigned32"
_SoamPmDmStatsInternalReference_Object = MibTableColumn
soamPmDmStatsInternalReference = _SoamPmDmStatsInternalReference_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 60, 2, 3, 2, 1, 8),
    _SoamPmDmStatsInternalReference_Type()
)
soamPmDmStatsInternalReference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    soamPmDmStatsInternalReference.setStatus("current")
_SoamPmDmStatsMepName_Type = DisplayString
_SoamPmDmStatsMepName_Object = MibTableColumn
soamPmDmStatsMepName = _SoamPmDmStatsMepName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 60, 2, 3, 2, 1, 9),
    _SoamPmDmStatsMepName_Type()
)
soamPmDmStatsMepName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    soamPmDmStatsMepName.setStatus("current")
_SoamPmDmStatsSuspect15Min_Type = TruthValue
_SoamPmDmStatsSuspect15Min_Object = MibTableColumn
soamPmDmStatsSuspect15Min = _SoamPmDmStatsSuspect15Min_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 60, 2, 3, 2, 1, 10),
    _SoamPmDmStatsSuspect15Min_Type()
)
soamPmDmStatsSuspect15Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    soamPmDmStatsSuspect15Min.setStatus("current")
_SoamPmDmStatsSuspectPrevious15Min_Type = TruthValue
_SoamPmDmStatsSuspectPrevious15Min_Object = MibTableColumn
soamPmDmStatsSuspectPrevious15Min = _SoamPmDmStatsSuspectPrevious15Min_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 60, 2, 3, 2, 1, 11),
    _SoamPmDmStatsSuspectPrevious15Min_Type()
)
soamPmDmStatsSuspectPrevious15Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    soamPmDmStatsSuspectPrevious15Min.setStatus("current")
_SoamPmDmStatsSuspect24H_Type = TruthValue
_SoamPmDmStatsSuspect24H_Object = MibTableColumn
soamPmDmStatsSuspect24H = _SoamPmDmStatsSuspect24H_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 60, 2, 3, 2, 1, 12),
    _SoamPmDmStatsSuspect24H_Type()
)
soamPmDmStatsSuspect24H.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    soamPmDmStatsSuspect24H.setStatus("current")


class _SoamPmDmStatsReset15Min_Type(Integer32):
    """Custom type soamPmDmStatsReset15Min based on Integer32"""
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
          ("reset", 2))
    )


_SoamPmDmStatsReset15Min_Type.__name__ = "Integer32"
_SoamPmDmStatsReset15Min_Object = MibTableColumn
soamPmDmStatsReset15Min = _SoamPmDmStatsReset15Min_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 60, 2, 3, 2, 1, 13),
    _SoamPmDmStatsReset15Min_Type()
)
soamPmDmStatsReset15Min.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    soamPmDmStatsReset15Min.setStatus("current")


class _SoamPmDmStatsReset24H_Type(Integer32):
    """Custom type soamPmDmStatsReset24H based on Integer32"""
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
          ("reset", 2))
    )


_SoamPmDmStatsReset24H_Type.__name__ = "Integer32"
_SoamPmDmStatsReset24H_Object = MibTableColumn
soamPmDmStatsReset24H = _SoamPmDmStatsReset24H_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 60, 2, 3, 2, 1, 14),
    _SoamPmDmStatsReset24H_Type()
)
soamPmDmStatsReset24H.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    soamPmDmStatsReset24H.setStatus("current")
_SoamPmDmStatsStartTime15Min_Type = DateAndTime
_SoamPmDmStatsStartTime15Min_Object = MibTableColumn
soamPmDmStatsStartTime15Min = _SoamPmDmStatsStartTime15Min_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 60, 2, 3, 2, 1, 15),
    _SoamPmDmStatsStartTime15Min_Type()
)
soamPmDmStatsStartTime15Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    soamPmDmStatsStartTime15Min.setStatus("current")
_SoamPmDmStatsElapsedTime15Min_Type = TimeInterval
_SoamPmDmStatsElapsedTime15Min_Object = MibTableColumn
soamPmDmStatsElapsedTime15Min = _SoamPmDmStatsElapsedTime15Min_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 60, 2, 3, 2, 1, 16),
    _SoamPmDmStatsElapsedTime15Min_Type()
)
soamPmDmStatsElapsedTime15Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    soamPmDmStatsElapsedTime15Min.setStatus("current")


class _SoamPmDmStatsFrameDelayTwoWayMin15Min_Type(Unsigned32WithNA):
    """Custom type soamPmDmStatsFrameDelayTwoWayMin15Min based on Unsigned32WithNA"""
    defaultValue = 4294967294

    subtypeSpec = Unsigned32WithNA.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
        ValueRangeConstraint(4294967294, 4294967294),
    )


_SoamPmDmStatsFrameDelayTwoWayMin15Min_Type.__name__ = "Unsigned32WithNA"
_SoamPmDmStatsFrameDelayTwoWayMin15Min_Object = MibTableColumn
soamPmDmStatsFrameDelayTwoWayMin15Min = _SoamPmDmStatsFrameDelayTwoWayMin15Min_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 60, 2, 3, 2, 1, 17),
    _SoamPmDmStatsFrameDelayTwoWayMin15Min_Type()
)
soamPmDmStatsFrameDelayTwoWayMin15Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    soamPmDmStatsFrameDelayTwoWayMin15Min.setStatus("current")
_SoamPmDmStatsFrameDelayTwoWayMax15Min_Type = Unsigned32
_SoamPmDmStatsFrameDelayTwoWayMax15Min_Object = MibTableColumn
soamPmDmStatsFrameDelayTwoWayMax15Min = _SoamPmDmStatsFrameDelayTwoWayMax15Min_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 60, 2, 3, 2, 1, 18),
    _SoamPmDmStatsFrameDelayTwoWayMax15Min_Type()
)
soamPmDmStatsFrameDelayTwoWayMax15Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    soamPmDmStatsFrameDelayTwoWayMax15Min.setStatus("current")
_SoamPmDmStatsFrameDelayTwoWayAvg15Min_Type = Unsigned32
_SoamPmDmStatsFrameDelayTwoWayAvg15Min_Object = MibTableColumn
soamPmDmStatsFrameDelayTwoWayAvg15Min = _SoamPmDmStatsFrameDelayTwoWayAvg15Min_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 60, 2, 3, 2, 1, 19),
    _SoamPmDmStatsFrameDelayTwoWayAvg15Min_Type()
)
soamPmDmStatsFrameDelayTwoWayAvg15Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    soamPmDmStatsFrameDelayTwoWayAvg15Min.setStatus("current")


class _SoamPmDmStatsIfdvTwoWayMin15Min_Type(Unsigned32WithNA):
    """Custom type soamPmDmStatsIfdvTwoWayMin15Min based on Unsigned32WithNA"""
    defaultValue = 4294967294


_SoamPmDmStatsIfdvTwoWayMin15Min_Type.__name__ = "Unsigned32WithNA"
_SoamPmDmStatsIfdvTwoWayMin15Min_Object = MibTableColumn
soamPmDmStatsIfdvTwoWayMin15Min = _SoamPmDmStatsIfdvTwoWayMin15Min_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 60, 2, 3, 2, 1, 20),
    _SoamPmDmStatsIfdvTwoWayMin15Min_Type()
)
soamPmDmStatsIfdvTwoWayMin15Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    soamPmDmStatsIfdvTwoWayMin15Min.setStatus("current")
_SoamPmDmStatsIfdvTwoWayMax15Min_Type = Unsigned32
_SoamPmDmStatsIfdvTwoWayMax15Min_Object = MibTableColumn
soamPmDmStatsIfdvTwoWayMax15Min = _SoamPmDmStatsIfdvTwoWayMax15Min_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 60, 2, 3, 2, 1, 21),
    _SoamPmDmStatsIfdvTwoWayMax15Min_Type()
)
soamPmDmStatsIfdvTwoWayMax15Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    soamPmDmStatsIfdvTwoWayMax15Min.setStatus("current")
_SoamPmDmStatsIfdvTwoWayAvg15Min_Type = Unsigned32
_SoamPmDmStatsIfdvTwoWayAvg15Min_Object = MibTableColumn
soamPmDmStatsIfdvTwoWayAvg15Min = _SoamPmDmStatsIfdvTwoWayAvg15Min_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 60, 2, 3, 2, 1, 22),
    _SoamPmDmStatsIfdvTwoWayAvg15Min_Type()
)
soamPmDmStatsIfdvTwoWayAvg15Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    soamPmDmStatsIfdvTwoWayAvg15Min.setStatus("current")
_SoamPmDmStatsStartTimePrevious15Min_Type = DateAndTime
_SoamPmDmStatsStartTimePrevious15Min_Object = MibTableColumn
soamPmDmStatsStartTimePrevious15Min = _SoamPmDmStatsStartTimePrevious15Min_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 60, 2, 3, 2, 1, 23),
    _SoamPmDmStatsStartTimePrevious15Min_Type()
)
soamPmDmStatsStartTimePrevious15Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    soamPmDmStatsStartTimePrevious15Min.setStatus("current")
_SoamPmDmStatsElapsedTimePrevious15Min_Type = TimeInterval
_SoamPmDmStatsElapsedTimePrevious15Min_Object = MibTableColumn
soamPmDmStatsElapsedTimePrevious15Min = _SoamPmDmStatsElapsedTimePrevious15Min_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 60, 2, 3, 2, 1, 24),
    _SoamPmDmStatsElapsedTimePrevious15Min_Type()
)
soamPmDmStatsElapsedTimePrevious15Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    soamPmDmStatsElapsedTimePrevious15Min.setStatus("current")


class _SoamPmDmStatsFrameDelayTwoWayMinPrevious15Min_Type(Unsigned32WithNA):
    """Custom type soamPmDmStatsFrameDelayTwoWayMinPrevious15Min based on Unsigned32WithNA"""
    defaultValue = 4294967294


_SoamPmDmStatsFrameDelayTwoWayMinPrevious15Min_Type.__name__ = "Unsigned32WithNA"
_SoamPmDmStatsFrameDelayTwoWayMinPrevious15Min_Object = MibTableColumn
soamPmDmStatsFrameDelayTwoWayMinPrevious15Min = _SoamPmDmStatsFrameDelayTwoWayMinPrevious15Min_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 60, 2, 3, 2, 1, 25),
    _SoamPmDmStatsFrameDelayTwoWayMinPrevious15Min_Type()
)
soamPmDmStatsFrameDelayTwoWayMinPrevious15Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    soamPmDmStatsFrameDelayTwoWayMinPrevious15Min.setStatus("current")
_SoamPmDmStatsFrameDelayTwoWayMaxPrevious15Min_Type = Unsigned32
_SoamPmDmStatsFrameDelayTwoWayMaxPrevious15Min_Object = MibTableColumn
soamPmDmStatsFrameDelayTwoWayMaxPrevious15Min = _SoamPmDmStatsFrameDelayTwoWayMaxPrevious15Min_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 60, 2, 3, 2, 1, 26),
    _SoamPmDmStatsFrameDelayTwoWayMaxPrevious15Min_Type()
)
soamPmDmStatsFrameDelayTwoWayMaxPrevious15Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    soamPmDmStatsFrameDelayTwoWayMaxPrevious15Min.setStatus("current")
_SoamPmDmStatsFrameDelayTwoWayAvgPrevious15Min_Type = Unsigned32
_SoamPmDmStatsFrameDelayTwoWayAvgPrevious15Min_Object = MibTableColumn
soamPmDmStatsFrameDelayTwoWayAvgPrevious15Min = _SoamPmDmStatsFrameDelayTwoWayAvgPrevious15Min_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 60, 2, 3, 2, 1, 27),
    _SoamPmDmStatsFrameDelayTwoWayAvgPrevious15Min_Type()
)
soamPmDmStatsFrameDelayTwoWayAvgPrevious15Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    soamPmDmStatsFrameDelayTwoWayAvgPrevious15Min.setStatus("current")


class _SoamPmDmStatsIfdvTwoWayMinPrevious15Min_Type(Unsigned32WithNA):
    """Custom type soamPmDmStatsIfdvTwoWayMinPrevious15Min based on Unsigned32WithNA"""
    defaultValue = 4294967294


_SoamPmDmStatsIfdvTwoWayMinPrevious15Min_Type.__name__ = "Unsigned32WithNA"
_SoamPmDmStatsIfdvTwoWayMinPrevious15Min_Object = MibTableColumn
soamPmDmStatsIfdvTwoWayMinPrevious15Min = _SoamPmDmStatsIfdvTwoWayMinPrevious15Min_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 60, 2, 3, 2, 1, 28),
    _SoamPmDmStatsIfdvTwoWayMinPrevious15Min_Type()
)
soamPmDmStatsIfdvTwoWayMinPrevious15Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    soamPmDmStatsIfdvTwoWayMinPrevious15Min.setStatus("current")
_SoamPmDmStatsIfdvTwoWayMaxPrevious15Min_Type = Unsigned32
_SoamPmDmStatsIfdvTwoWayMaxPrevious15Min_Object = MibTableColumn
soamPmDmStatsIfdvTwoWayMaxPrevious15Min = _SoamPmDmStatsIfdvTwoWayMaxPrevious15Min_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 60, 2, 3, 2, 1, 29),
    _SoamPmDmStatsIfdvTwoWayMaxPrevious15Min_Type()
)
soamPmDmStatsIfdvTwoWayMaxPrevious15Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    soamPmDmStatsIfdvTwoWayMaxPrevious15Min.setStatus("current")
_SoamPmDmStatsIfdvTwoWayAvgPrevious15Min_Type = Unsigned32
_SoamPmDmStatsIfdvTwoWayAvgPrevious15Min_Object = MibTableColumn
soamPmDmStatsIfdvTwoWayAvgPrevious15Min = _SoamPmDmStatsIfdvTwoWayAvgPrevious15Min_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 60, 2, 3, 2, 1, 30),
    _SoamPmDmStatsIfdvTwoWayAvgPrevious15Min_Type()
)
soamPmDmStatsIfdvTwoWayAvgPrevious15Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    soamPmDmStatsIfdvTwoWayAvgPrevious15Min.setStatus("current")
_SoamPmDmStatsStartTime24H_Type = DateAndTime
_SoamPmDmStatsStartTime24H_Object = MibTableColumn
soamPmDmStatsStartTime24H = _SoamPmDmStatsStartTime24H_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 60, 2, 3, 2, 1, 31),
    _SoamPmDmStatsStartTime24H_Type()
)
soamPmDmStatsStartTime24H.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    soamPmDmStatsStartTime24H.setStatus("current")
_SoamPmDmStatsElapsedTime24H_Type = TimeInterval
_SoamPmDmStatsElapsedTime24H_Object = MibTableColumn
soamPmDmStatsElapsedTime24H = _SoamPmDmStatsElapsedTime24H_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 60, 2, 3, 2, 1, 32),
    _SoamPmDmStatsElapsedTime24H_Type()
)
soamPmDmStatsElapsedTime24H.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    soamPmDmStatsElapsedTime24H.setStatus("current")


class _SoamPmDmStatsFrameDelayTwoWayMin24H_Type(Unsigned32WithNA):
    """Custom type soamPmDmStatsFrameDelayTwoWayMin24H based on Unsigned32WithNA"""
    defaultValue = 4294967294


_SoamPmDmStatsFrameDelayTwoWayMin24H_Type.__name__ = "Unsigned32WithNA"
_SoamPmDmStatsFrameDelayTwoWayMin24H_Object = MibTableColumn
soamPmDmStatsFrameDelayTwoWayMin24H = _SoamPmDmStatsFrameDelayTwoWayMin24H_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 60, 2, 3, 2, 1, 33),
    _SoamPmDmStatsFrameDelayTwoWayMin24H_Type()
)
soamPmDmStatsFrameDelayTwoWayMin24H.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    soamPmDmStatsFrameDelayTwoWayMin24H.setStatus("current")
_SoamPmDmStatsFrameDelayTwoWayMax24H_Type = Unsigned32
_SoamPmDmStatsFrameDelayTwoWayMax24H_Object = MibTableColumn
soamPmDmStatsFrameDelayTwoWayMax24H = _SoamPmDmStatsFrameDelayTwoWayMax24H_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 60, 2, 3, 2, 1, 34),
    _SoamPmDmStatsFrameDelayTwoWayMax24H_Type()
)
soamPmDmStatsFrameDelayTwoWayMax24H.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    soamPmDmStatsFrameDelayTwoWayMax24H.setStatus("current")
_SoamPmDmStatsFrameDelayTwoWayAvg24H_Type = Unsigned32
_SoamPmDmStatsFrameDelayTwoWayAvg24H_Object = MibTableColumn
soamPmDmStatsFrameDelayTwoWayAvg24H = _SoamPmDmStatsFrameDelayTwoWayAvg24H_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 60, 2, 3, 2, 1, 35),
    _SoamPmDmStatsFrameDelayTwoWayAvg24H_Type()
)
soamPmDmStatsFrameDelayTwoWayAvg24H.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    soamPmDmStatsFrameDelayTwoWayAvg24H.setStatus("current")


class _SoamPmDmStatsIfdvTwoWayMin24H_Type(Unsigned32WithNA):
    """Custom type soamPmDmStatsIfdvTwoWayMin24H based on Unsigned32WithNA"""
    defaultValue = 4294967294


_SoamPmDmStatsIfdvTwoWayMin24H_Type.__name__ = "Unsigned32WithNA"
_SoamPmDmStatsIfdvTwoWayMin24H_Object = MibTableColumn
soamPmDmStatsIfdvTwoWayMin24H = _SoamPmDmStatsIfdvTwoWayMin24H_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 60, 2, 3, 2, 1, 36),
    _SoamPmDmStatsIfdvTwoWayMin24H_Type()
)
soamPmDmStatsIfdvTwoWayMin24H.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    soamPmDmStatsIfdvTwoWayMin24H.setStatus("current")
_SoamPmDmStatsIfdvTwoWayMax24H_Type = Unsigned32
_SoamPmDmStatsIfdvTwoWayMax24H_Object = MibTableColumn
soamPmDmStatsIfdvTwoWayMax24H = _SoamPmDmStatsIfdvTwoWayMax24H_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 60, 2, 3, 2, 1, 37),
    _SoamPmDmStatsIfdvTwoWayMax24H_Type()
)
soamPmDmStatsIfdvTwoWayMax24H.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    soamPmDmStatsIfdvTwoWayMax24H.setStatus("current")
_SoamPmDmStatsIfdvTwoWayAvg24H_Type = Unsigned32
_SoamPmDmStatsIfdvTwoWayAvg24H_Object = MibTableColumn
soamPmDmStatsIfdvTwoWayAvg24H = _SoamPmDmStatsIfdvTwoWayAvg24H_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 60, 2, 3, 2, 1, 38),
    _SoamPmDmStatsIfdvTwoWayAvg24H_Type()
)
soamPmDmStatsIfdvTwoWayAvg24H.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    soamPmDmStatsIfdvTwoWayAvg24H.setStatus("current")


class _SoamPmDmStatsPriority_Type(IEEE8021PriorityValue):
    """Custom type soamPmDmStatsPriority based on IEEE8021PriorityValue"""
    defaultValue = 0


_SoamPmDmStatsPriority_Type.__name__ = "IEEE8021PriorityValue"
_SoamPmDmStatsPriority_Object = MibTableColumn
soamPmDmStatsPriority = _SoamPmDmStatsPriority_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 60, 2, 3, 2, 1, 39),
    _SoamPmDmStatsPriority_Type()
)
soamPmDmStatsPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    soamPmDmStatsPriority.setStatus("current")

# Managed Objects groups

soamPmGeneralGroupV1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 60, 1, 1, 1)
)
soamPmGeneralGroupV1.setObjects(
      *(("LUM-SOAM-PM-MIB", "soamPmGeneralLastChangeTime"),
        ("LUM-SOAM-PM-MIB", "soamPmGeneralLmStateLastChangeTime"),
        ("LUM-SOAM-PM-MIB", "soamPmGeneralLmObjectsTableSize"),
        ("LUM-SOAM-PM-MIB", "soamPmGeneralDmObjectsTableSize"))
)
if mibBuilder.loadTexts:
    soamPmGeneralGroupV1.setStatus("current")

soamPmLmCfgGroupV1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 60, 1, 1, 2)
)
soamPmLmCfgGroupV1.setObjects(
      *(("LUM-SOAM-PM-MIB", "soamPmLmCfgIndex"),
        ("LUM-SOAM-PM-MIB", "soamPmLmCfgName"),
        ("LUM-SOAM-PM-MIB", "soamPmLmCfgDescr"),
        ("LUM-SOAM-PM-MIB", "soamPmLmCfgSubrack"),
        ("LUM-SOAM-PM-MIB", "soamPmLmCfgSlot"),
        ("LUM-SOAM-PM-MIB", "soamPmLmCfgInternalReference"),
        ("LUM-SOAM-PM-MIB", "soamPmLmCfgLocalDeviceType"),
        ("LUM-SOAM-PM-MIB", "soamPmLmCfgType"),
        ("LUM-SOAM-PM-MIB", "soamPmLmCfgEnabled"),
        ("LUM-SOAM-PM-MIB", "soamPmLmCfgMessagePeriod"),
        ("LUM-SOAM-PM-MIB", "soamPmLmCfgPriority"),
        ("LUM-SOAM-PM-MIB", "soamPmLmCfgDestMacAddress"),
        ("LUM-SOAM-PM-MIB", "soamPmLmCfgMepName"),
        ("LUM-SOAM-PM-MIB", "soamPmLmCfgMaidIdentifier"),
        ("LUM-SOAM-PM-MIB", "soamPmLmCfgDestMepId"),
        ("LUM-SOAM-PM-MIB", "soamPmLmCfgDestIsMepId"),
        ("LUM-SOAM-PM-MIB", "soamPmLmCfgAvailabilityFlrThreshold"),
        ("LUM-SOAM-PM-MIB", "soamPmLmCfgAvailabilityUasAlarmThreshold"),
        ("LUM-SOAM-PM-MIB", "soamPmLmCfgSessionType"),
        ("LUM-SOAM-PM-MIB", "soamPmLmCfgSessionStatus"))
)
if mibBuilder.loadTexts:
    soamPmLmCfgGroupV1.setStatus("current")

soamPmLmStatsGroupV1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 60, 1, 1, 3)
)
soamPmLmStatsGroupV1.setObjects(
      *(("LUM-SOAM-PM-MIB", "soamPmLmStatsIndex"),
        ("LUM-SOAM-PM-MIB", "soamPmLmStatsLocalDeviceType"),
        ("LUM-SOAM-PM-MIB", "soamPmLmStatsName"),
        ("LUM-SOAM-PM-MIB", "soamPmLmStatsSubrack"),
        ("LUM-SOAM-PM-MIB", "soamPmLmStatsSlot"),
        ("LUM-SOAM-PM-MIB", "soamPmLmStatsDestMepId"),
        ("LUM-SOAM-PM-MIB", "soamPmLmStatsMaidIdentifier"),
        ("LUM-SOAM-PM-MIB", "soamPmLmStatsInternalReference"),
        ("LUM-SOAM-PM-MIB", "soamPmLmStatsMepName"),
        ("LUM-SOAM-PM-MIB", "soamPmLmStatsSuspect15Min"),
        ("LUM-SOAM-PM-MIB", "soamPmLmStatsSuspectPrevious15Min"),
        ("LUM-SOAM-PM-MIB", "soamPmLmStatsSuspect24H"),
        ("LUM-SOAM-PM-MIB", "soamPmLmStatsReset15Min"),
        ("LUM-SOAM-PM-MIB", "soamPmLmStatsReset24H"),
        ("LUM-SOAM-PM-MIB", "soamPmLmStatsStartTime15Min"),
        ("LUM-SOAM-PM-MIB", "soamPmLmStatsElapsedTime15Min"),
        ("LUM-SOAM-PM-MIB", "soamPmLmStatsForwardTransmittedFrames15Min"),
        ("LUM-SOAM-PM-MIB", "soamPmLmStatsForwardReceivedFrames15Min"),
        ("LUM-SOAM-PM-MIB", "soamPmLmStatsForwardMinFlr15Min"),
        ("LUM-SOAM-PM-MIB", "soamPmLmStatsForwardMaxFlr15Min"),
        ("LUM-SOAM-PM-MIB", "soamPmLmStatsForwardAvgFlr15Min"),
        ("LUM-SOAM-PM-MIB", "soamPmLmStatsForwardHighLoss15Min"),
        ("LUM-SOAM-PM-MIB", "soamPmLmStatsBackwardTransmittedFrames15Min"),
        ("LUM-SOAM-PM-MIB", "soamPmLmStatsBackwardReceivedFrames15Min"),
        ("LUM-SOAM-PM-MIB", "soamPmLmStatsBackwardMinFlr15Min"),
        ("LUM-SOAM-PM-MIB", "soamPmLmStatsBackwardMaxFlr15Min"),
        ("LUM-SOAM-PM-MIB", "soamPmLmStatsBackwardAvgFlr15Min"),
        ("LUM-SOAM-PM-MIB", "soamPmLmStatsBackwardHighLoss15Min"),
        ("LUM-SOAM-PM-MIB", "soamPmLmStatsUnavailableSeconds15Min"),
        ("LUM-SOAM-PM-MIB", "soamPmLmStatsStartTimePrevious15Min"),
        ("LUM-SOAM-PM-MIB", "soamPmLmStatsElapsedTimePrevious15Min"),
        ("LUM-SOAM-PM-MIB", "soamPmLmStatsForwardTransmittedFramesPrevious15Min"),
        ("LUM-SOAM-PM-MIB", "soamPmLmStatsForwardReceivedFramesPrevious15Min"),
        ("LUM-SOAM-PM-MIB", "soamPmLmStatsForwardMinFlrPrevious15Min"),
        ("LUM-SOAM-PM-MIB", "soamPmLmStatsForwardMaxFlrPrevious15Min"),
        ("LUM-SOAM-PM-MIB", "soamPmLmStatsForwardAvgFlrPrevious15Min"),
        ("LUM-SOAM-PM-MIB", "soamPmLmStatsForwardHighLossPrevious15Min"),
        ("LUM-SOAM-PM-MIB", "soamPmLmStatsBackwardTransmittedFramesPrevious15Min"),
        ("LUM-SOAM-PM-MIB", "soamPmLmStatsBackwardReceivedFramesPrevious15Min"),
        ("LUM-SOAM-PM-MIB", "soamPmLmStatsBackwardMinFlrPrevious15Min"),
        ("LUM-SOAM-PM-MIB", "soamPmLmStatsBackwardMaxFlrPrevious15Min"),
        ("LUM-SOAM-PM-MIB", "soamPmLmStatsBackwardAvgFlrPrevious15Min"),
        ("LUM-SOAM-PM-MIB", "soamPmLmStatsBackwardHighLossPrevious15Min"),
        ("LUM-SOAM-PM-MIB", "soamPmLmStatsStartTime24H"),
        ("LUM-SOAM-PM-MIB", "soamPmLmStatsElapsedTime24H"),
        ("LUM-SOAM-PM-MIB", "soamPmLmStatsForwardTransmittedFrames24H"),
        ("LUM-SOAM-PM-MIB", "soamPmLmStatsForwardReceivedFrames24H"),
        ("LUM-SOAM-PM-MIB", "soamPmLmStatsForwardMinFlr24H"),
        ("LUM-SOAM-PM-MIB", "soamPmLmStatsForwardMaxFlr24H"),
        ("LUM-SOAM-PM-MIB", "soamPmLmStatsForwardAvgFlr24H"),
        ("LUM-SOAM-PM-MIB", "soamPmLmStatsForwardHighLoss24H"),
        ("LUM-SOAM-PM-MIB", "soamPmLmStatsBackwardTransmittedFrames24H"),
        ("LUM-SOAM-PM-MIB", "soamPmLmStatsBackwardReceivedFrames24H"),
        ("LUM-SOAM-PM-MIB", "soamPmLmStatsBackwardMinFlr24H"),
        ("LUM-SOAM-PM-MIB", "soamPmLmStatsBackwardMaxFlr24H"),
        ("LUM-SOAM-PM-MIB", "soamPmLmStatsBackwardAvgFlr24H"),
        ("LUM-SOAM-PM-MIB", "soamPmLmStatsBackwardHighLoss24H"),
        ("LUM-SOAM-PM-MIB", "soamPmLmStatsUas"))
)
if mibBuilder.loadTexts:
    soamPmLmStatsGroupV1.setStatus("current")

soamPmDmCfgGroupV1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 60, 1, 1, 4)
)
soamPmDmCfgGroupV1.setObjects(
      *(("LUM-SOAM-PM-MIB", "soamPmDmCfgIndex"),
        ("LUM-SOAM-PM-MIB", "soamPmDmCfgName"),
        ("LUM-SOAM-PM-MIB", "soamPmDmCfgDescr"),
        ("LUM-SOAM-PM-MIB", "soamPmDmCfgSubrack"),
        ("LUM-SOAM-PM-MIB", "soamPmDmCfgSlot"),
        ("LUM-SOAM-PM-MIB", "soamPmDmCfgInternalReference"),
        ("LUM-SOAM-PM-MIB", "soamPmDmCfgLocalDeviceType"),
        ("LUM-SOAM-PM-MIB", "soamPmDmCfgDropEligible"),
        ("LUM-SOAM-PM-MIB", "soamPmDmCfgType"),
        ("LUM-SOAM-PM-MIB", "soamPmDmCfgEnabled"),
        ("LUM-SOAM-PM-MIB", "soamPmDmCfgMessagePeriod"),
        ("LUM-SOAM-PM-MIB", "soamPmDmCfgPriority"),
        ("LUM-SOAM-PM-MIB", "soamPmDmCfgDestMacAddress"),
        ("LUM-SOAM-PM-MIB", "soamPmDmCfgMepName"),
        ("LUM-SOAM-PM-MIB", "soamPmDmCfgMaidIdentifier"),
        ("LUM-SOAM-PM-MIB", "soamPmDmCfgDestMepId"),
        ("LUM-SOAM-PM-MIB", "soamPmDmCfgDestIsMepId"),
        ("LUM-SOAM-PM-MIB", "soamPmDmCfgSessionType"),
        ("LUM-SOAM-PM-MIB", "soamPmDmCfgSessionStatus"))
)
if mibBuilder.loadTexts:
    soamPmDmCfgGroupV1.setStatus("current")

soamPmDmStatsGroupV1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 60, 1, 1, 5)
)
soamPmDmStatsGroupV1.setObjects(
      *(("LUM-SOAM-PM-MIB", "soamPmDmStatsIndex"),
        ("LUM-SOAM-PM-MIB", "soamPmDmStatsLocalDeviceType"),
        ("LUM-SOAM-PM-MIB", "soamPmDmStatsName"),
        ("LUM-SOAM-PM-MIB", "soamPmDmStatsSubrack"),
        ("LUM-SOAM-PM-MIB", "soamPmDmStatsSlot"),
        ("LUM-SOAM-PM-MIB", "soamPmDmStatsDestMepId"),
        ("LUM-SOAM-PM-MIB", "soamPmDmStatsMaidIdentifier"),
        ("LUM-SOAM-PM-MIB", "soamPmDmStatsInternalReference"),
        ("LUM-SOAM-PM-MIB", "soamPmDmStatsMepName"),
        ("LUM-SOAM-PM-MIB", "soamPmDmStatsSuspect15Min"),
        ("LUM-SOAM-PM-MIB", "soamPmDmStatsSuspectPrevious15Min"),
        ("LUM-SOAM-PM-MIB", "soamPmDmStatsSuspect24H"),
        ("LUM-SOAM-PM-MIB", "soamPmDmStatsReset15Min"),
        ("LUM-SOAM-PM-MIB", "soamPmDmStatsReset24H"),
        ("LUM-SOAM-PM-MIB", "soamPmDmStatsStartTime15Min"),
        ("LUM-SOAM-PM-MIB", "soamPmDmStatsElapsedTime15Min"),
        ("LUM-SOAM-PM-MIB", "soamPmDmStatsFrameDelayTwoWayMin15Min"),
        ("LUM-SOAM-PM-MIB", "soamPmDmStatsFrameDelayTwoWayMax15Min"),
        ("LUM-SOAM-PM-MIB", "soamPmDmStatsFrameDelayTwoWayAvg15Min"),
        ("LUM-SOAM-PM-MIB", "soamPmDmStatsIfdvTwoWayMin15Min"),
        ("LUM-SOAM-PM-MIB", "soamPmDmStatsIfdvTwoWayMax15Min"),
        ("LUM-SOAM-PM-MIB", "soamPmDmStatsIfdvTwoWayAvg15Min"),
        ("LUM-SOAM-PM-MIB", "soamPmDmStatsStartTimePrevious15Min"),
        ("LUM-SOAM-PM-MIB", "soamPmDmStatsElapsedTimePrevious15Min"),
        ("LUM-SOAM-PM-MIB", "soamPmDmStatsFrameDelayTwoWayMinPrevious15Min"),
        ("LUM-SOAM-PM-MIB", "soamPmDmStatsFrameDelayTwoWayMaxPrevious15Min"),
        ("LUM-SOAM-PM-MIB", "soamPmDmStatsFrameDelayTwoWayAvgPrevious15Min"),
        ("LUM-SOAM-PM-MIB", "soamPmDmStatsIfdvTwoWayMinPrevious15Min"),
        ("LUM-SOAM-PM-MIB", "soamPmDmStatsIfdvTwoWayMaxPrevious15Min"),
        ("LUM-SOAM-PM-MIB", "soamPmDmStatsIfdvTwoWayAvgPrevious15Min"),
        ("LUM-SOAM-PM-MIB", "soamPmDmStatsStartTime24H"),
        ("LUM-SOAM-PM-MIB", "soamPmDmStatsElapsedTime24H"),
        ("LUM-SOAM-PM-MIB", "soamPmDmStatsFrameDelayTwoWayMin24H"),
        ("LUM-SOAM-PM-MIB", "soamPmDmStatsFrameDelayTwoWayMax24H"),
        ("LUM-SOAM-PM-MIB", "soamPmDmStatsFrameDelayTwoWayAvg24H"),
        ("LUM-SOAM-PM-MIB", "soamPmDmStatsIfdvTwoWayMin24H"),
        ("LUM-SOAM-PM-MIB", "soamPmDmStatsIfdvTwoWayMax24H"),
        ("LUM-SOAM-PM-MIB", "soamPmDmStatsIfdvTwoWayAvg24H"))
)
if mibBuilder.loadTexts:
    soamPmDmStatsGroupV1.setStatus("current")

soamPmLmCfgGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 60, 1, 1, 6)
)
soamPmLmCfgGroupV2.setObjects(
      *(("LUM-SOAM-PM-MIB", "soamPmLmCfgIndex"),
        ("LUM-SOAM-PM-MIB", "soamPmLmCfgName"),
        ("LUM-SOAM-PM-MIB", "soamPmLmCfgDescr"),
        ("LUM-SOAM-PM-MIB", "soamPmLmCfgSubrack"),
        ("LUM-SOAM-PM-MIB", "soamPmLmCfgSlot"),
        ("LUM-SOAM-PM-MIB", "soamPmLmCfgInternalReference"),
        ("LUM-SOAM-PM-MIB", "soamPmLmCfgLocalDeviceType"),
        ("LUM-SOAM-PM-MIB", "soamPmLmCfgType"),
        ("LUM-SOAM-PM-MIB", "soamPmLmCfgEnabled"),
        ("LUM-SOAM-PM-MIB", "soamPmLmCfgMessagePeriod"),
        ("LUM-SOAM-PM-MIB", "soamPmLmCfgPriority"),
        ("LUM-SOAM-PM-MIB", "soamPmLmCfgDestMacAddress"),
        ("LUM-SOAM-PM-MIB", "soamPmLmCfgMepName"),
        ("LUM-SOAM-PM-MIB", "soamPmLmCfgMaidIdentifier"),
        ("LUM-SOAM-PM-MIB", "soamPmLmCfgDestMepId"),
        ("LUM-SOAM-PM-MIB", "soamPmLmCfgDestIsMepId"),
        ("LUM-SOAM-PM-MIB", "soamPmLmCfgAvailabilityFlrThreshold"),
        ("LUM-SOAM-PM-MIB", "soamPmLmCfgAvailabilityUasAlarmThreshold"),
        ("LUM-SOAM-PM-MIB", "soamPmLmCfgSessionType"),
        ("LUM-SOAM-PM-MIB", "soamPmLmCfgSessionStatus"),
        ("LUM-SOAM-PM-MIB", "soamPmLmCfgCosAwareness"),
        ("LUM-SOAM-PM-MIB", "soamPmLmCfgRowStatus"),
        ("LUM-SOAM-PM-MIB", "soamPmLmCfgAdminStatus"),
        ("LUM-SOAM-PM-MIB", "soamPmLmCfgOperStatus"))
)
if mibBuilder.loadTexts:
    soamPmLmCfgGroupV2.setStatus("current")

soamPmDmCfgGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 60, 1, 1, 7)
)
soamPmDmCfgGroupV2.setObjects(
      *(("LUM-SOAM-PM-MIB", "soamPmDmCfgIndex"),
        ("LUM-SOAM-PM-MIB", "soamPmDmCfgName"),
        ("LUM-SOAM-PM-MIB", "soamPmDmCfgDescr"),
        ("LUM-SOAM-PM-MIB", "soamPmDmCfgSubrack"),
        ("LUM-SOAM-PM-MIB", "soamPmDmCfgSlot"),
        ("LUM-SOAM-PM-MIB", "soamPmDmCfgInternalReference"),
        ("LUM-SOAM-PM-MIB", "soamPmDmCfgLocalDeviceType"),
        ("LUM-SOAM-PM-MIB", "soamPmDmCfgDropEligible"),
        ("LUM-SOAM-PM-MIB", "soamPmDmCfgType"),
        ("LUM-SOAM-PM-MIB", "soamPmDmCfgEnabled"),
        ("LUM-SOAM-PM-MIB", "soamPmDmCfgMessagePeriod"),
        ("LUM-SOAM-PM-MIB", "soamPmDmCfgPriority"),
        ("LUM-SOAM-PM-MIB", "soamPmDmCfgDestMacAddress"),
        ("LUM-SOAM-PM-MIB", "soamPmDmCfgMepName"),
        ("LUM-SOAM-PM-MIB", "soamPmDmCfgMaidIdentifier"),
        ("LUM-SOAM-PM-MIB", "soamPmDmCfgDestMepId"),
        ("LUM-SOAM-PM-MIB", "soamPmDmCfgDestIsMepId"),
        ("LUM-SOAM-PM-MIB", "soamPmDmCfgSessionType"),
        ("LUM-SOAM-PM-MIB", "soamPmDmCfgSessionStatus"),
        ("LUM-SOAM-PM-MIB", "soamPmDmCfgRowStatus"),
        ("LUM-SOAM-PM-MIB", "soamPmDmCfgAdminStatus"),
        ("LUM-SOAM-PM-MIB", "soamPmDmCfgOperStatus"))
)
if mibBuilder.loadTexts:
    soamPmDmCfgGroupV2.setStatus("current")

soamPmLmStatsGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 60, 1, 1, 8)
)
soamPmLmStatsGroupV2.setObjects(
      *(("LUM-SOAM-PM-MIB", "soamPmLmStatsIndex"),
        ("LUM-SOAM-PM-MIB", "soamPmLmStatsLocalDeviceType"),
        ("LUM-SOAM-PM-MIB", "soamPmLmStatsName"),
        ("LUM-SOAM-PM-MIB", "soamPmLmStatsSubrack"),
        ("LUM-SOAM-PM-MIB", "soamPmLmStatsSlot"),
        ("LUM-SOAM-PM-MIB", "soamPmLmStatsDestMepId"),
        ("LUM-SOAM-PM-MIB", "soamPmLmStatsMaidIdentifier"),
        ("LUM-SOAM-PM-MIB", "soamPmLmStatsInternalReference"),
        ("LUM-SOAM-PM-MIB", "soamPmLmStatsMepName"),
        ("LUM-SOAM-PM-MIB", "soamPmLmStatsSuspect15Min"),
        ("LUM-SOAM-PM-MIB", "soamPmLmStatsSuspectPrevious15Min"),
        ("LUM-SOAM-PM-MIB", "soamPmLmStatsSuspect24H"),
        ("LUM-SOAM-PM-MIB", "soamPmLmStatsReset15Min"),
        ("LUM-SOAM-PM-MIB", "soamPmLmStatsReset24H"),
        ("LUM-SOAM-PM-MIB", "soamPmLmStatsStartTime15Min"),
        ("LUM-SOAM-PM-MIB", "soamPmLmStatsElapsedTime15Min"),
        ("LUM-SOAM-PM-MIB", "soamPmLmStatsForwardTransmittedFrames15Min"),
        ("LUM-SOAM-PM-MIB", "soamPmLmStatsForwardReceivedFrames15Min"),
        ("LUM-SOAM-PM-MIB", "soamPmLmStatsForwardMinFlr15Min"),
        ("LUM-SOAM-PM-MIB", "soamPmLmStatsForwardMaxFlr15Min"),
        ("LUM-SOAM-PM-MIB", "soamPmLmStatsForwardAvgFlr15Min"),
        ("LUM-SOAM-PM-MIB", "soamPmLmStatsForwardHighLoss15Min"),
        ("LUM-SOAM-PM-MIB", "soamPmLmStatsBackwardTransmittedFrames15Min"),
        ("LUM-SOAM-PM-MIB", "soamPmLmStatsBackwardReceivedFrames15Min"),
        ("LUM-SOAM-PM-MIB", "soamPmLmStatsBackwardMinFlr15Min"),
        ("LUM-SOAM-PM-MIB", "soamPmLmStatsBackwardMaxFlr15Min"),
        ("LUM-SOAM-PM-MIB", "soamPmLmStatsBackwardAvgFlr15Min"),
        ("LUM-SOAM-PM-MIB", "soamPmLmStatsBackwardHighLoss15Min"),
        ("LUM-SOAM-PM-MIB", "soamPmLmStatsUnavailableSeconds15Min"),
        ("LUM-SOAM-PM-MIB", "soamPmLmStatsStartTimePrevious15Min"),
        ("LUM-SOAM-PM-MIB", "soamPmLmStatsElapsedTimePrevious15Min"),
        ("LUM-SOAM-PM-MIB", "soamPmLmStatsForwardTransmittedFramesPrevious15Min"),
        ("LUM-SOAM-PM-MIB", "soamPmLmStatsForwardReceivedFramesPrevious15Min"),
        ("LUM-SOAM-PM-MIB", "soamPmLmStatsForwardMinFlrPrevious15Min"),
        ("LUM-SOAM-PM-MIB", "soamPmLmStatsForwardMaxFlrPrevious15Min"),
        ("LUM-SOAM-PM-MIB", "soamPmLmStatsForwardAvgFlrPrevious15Min"),
        ("LUM-SOAM-PM-MIB", "soamPmLmStatsForwardHighLossPrevious15Min"),
        ("LUM-SOAM-PM-MIB", "soamPmLmStatsBackwardTransmittedFramesPrevious15Min"),
        ("LUM-SOAM-PM-MIB", "soamPmLmStatsBackwardReceivedFramesPrevious15Min"),
        ("LUM-SOAM-PM-MIB", "soamPmLmStatsBackwardMinFlrPrevious15Min"),
        ("LUM-SOAM-PM-MIB", "soamPmLmStatsBackwardMaxFlrPrevious15Min"),
        ("LUM-SOAM-PM-MIB", "soamPmLmStatsBackwardAvgFlrPrevious15Min"),
        ("LUM-SOAM-PM-MIB", "soamPmLmStatsBackwardHighLossPrevious15Min"),
        ("LUM-SOAM-PM-MIB", "soamPmLmStatsStartTime24H"),
        ("LUM-SOAM-PM-MIB", "soamPmLmStatsElapsedTime24H"),
        ("LUM-SOAM-PM-MIB", "soamPmLmStatsForwardTransmittedFrames24H"),
        ("LUM-SOAM-PM-MIB", "soamPmLmStatsForwardReceivedFrames24H"),
        ("LUM-SOAM-PM-MIB", "soamPmLmStatsForwardMinFlr24H"),
        ("LUM-SOAM-PM-MIB", "soamPmLmStatsForwardMaxFlr24H"),
        ("LUM-SOAM-PM-MIB", "soamPmLmStatsForwardAvgFlr24H"),
        ("LUM-SOAM-PM-MIB", "soamPmLmStatsForwardHighLoss24H"),
        ("LUM-SOAM-PM-MIB", "soamPmLmStatsBackwardTransmittedFrames24H"),
        ("LUM-SOAM-PM-MIB", "soamPmLmStatsBackwardReceivedFrames24H"),
        ("LUM-SOAM-PM-MIB", "soamPmLmStatsBackwardMinFlr24H"),
        ("LUM-SOAM-PM-MIB", "soamPmLmStatsBackwardMaxFlr24H"),
        ("LUM-SOAM-PM-MIB", "soamPmLmStatsBackwardAvgFlr24H"),
        ("LUM-SOAM-PM-MIB", "soamPmLmStatsBackwardHighLoss24H"),
        ("LUM-SOAM-PM-MIB", "soamPmLmStatsUas"),
        ("LUM-SOAM-PM-MIB", "soamPmLmStatsPriority"))
)
if mibBuilder.loadTexts:
    soamPmLmStatsGroupV2.setStatus("current")

soamPmDmStatsGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 60, 1, 1, 9)
)
soamPmDmStatsGroupV2.setObjects(
      *(("LUM-SOAM-PM-MIB", "soamPmDmStatsIndex"),
        ("LUM-SOAM-PM-MIB", "soamPmDmStatsLocalDeviceType"),
        ("LUM-SOAM-PM-MIB", "soamPmDmStatsName"),
        ("LUM-SOAM-PM-MIB", "soamPmDmStatsSubrack"),
        ("LUM-SOAM-PM-MIB", "soamPmDmStatsSlot"),
        ("LUM-SOAM-PM-MIB", "soamPmDmStatsDestMepId"),
        ("LUM-SOAM-PM-MIB", "soamPmDmStatsMaidIdentifier"),
        ("LUM-SOAM-PM-MIB", "soamPmDmStatsInternalReference"),
        ("LUM-SOAM-PM-MIB", "soamPmDmStatsMepName"),
        ("LUM-SOAM-PM-MIB", "soamPmDmStatsSuspect15Min"),
        ("LUM-SOAM-PM-MIB", "soamPmDmStatsSuspectPrevious15Min"),
        ("LUM-SOAM-PM-MIB", "soamPmDmStatsSuspect24H"),
        ("LUM-SOAM-PM-MIB", "soamPmDmStatsReset15Min"),
        ("LUM-SOAM-PM-MIB", "soamPmDmStatsReset24H"),
        ("LUM-SOAM-PM-MIB", "soamPmDmStatsStartTime15Min"),
        ("LUM-SOAM-PM-MIB", "soamPmDmStatsElapsedTime15Min"),
        ("LUM-SOAM-PM-MIB", "soamPmDmStatsFrameDelayTwoWayMin15Min"),
        ("LUM-SOAM-PM-MIB", "soamPmDmStatsFrameDelayTwoWayMax15Min"),
        ("LUM-SOAM-PM-MIB", "soamPmDmStatsFrameDelayTwoWayAvg15Min"),
        ("LUM-SOAM-PM-MIB", "soamPmDmStatsIfdvTwoWayMin15Min"),
        ("LUM-SOAM-PM-MIB", "soamPmDmStatsIfdvTwoWayMax15Min"),
        ("LUM-SOAM-PM-MIB", "soamPmDmStatsIfdvTwoWayAvg15Min"),
        ("LUM-SOAM-PM-MIB", "soamPmDmStatsStartTimePrevious15Min"),
        ("LUM-SOAM-PM-MIB", "soamPmDmStatsElapsedTimePrevious15Min"),
        ("LUM-SOAM-PM-MIB", "soamPmDmStatsFrameDelayTwoWayMinPrevious15Min"),
        ("LUM-SOAM-PM-MIB", "soamPmDmStatsFrameDelayTwoWayMaxPrevious15Min"),
        ("LUM-SOAM-PM-MIB", "soamPmDmStatsFrameDelayTwoWayAvgPrevious15Min"),
        ("LUM-SOAM-PM-MIB", "soamPmDmStatsIfdvTwoWayMinPrevious15Min"),
        ("LUM-SOAM-PM-MIB", "soamPmDmStatsIfdvTwoWayMaxPrevious15Min"),
        ("LUM-SOAM-PM-MIB", "soamPmDmStatsIfdvTwoWayAvgPrevious15Min"),
        ("LUM-SOAM-PM-MIB", "soamPmDmStatsStartTime24H"),
        ("LUM-SOAM-PM-MIB", "soamPmDmStatsElapsedTime24H"),
        ("LUM-SOAM-PM-MIB", "soamPmDmStatsFrameDelayTwoWayMin24H"),
        ("LUM-SOAM-PM-MIB", "soamPmDmStatsFrameDelayTwoWayMax24H"),
        ("LUM-SOAM-PM-MIB", "soamPmDmStatsFrameDelayTwoWayAvg24H"),
        ("LUM-SOAM-PM-MIB", "soamPmDmStatsIfdvTwoWayMin24H"),
        ("LUM-SOAM-PM-MIB", "soamPmDmStatsIfdvTwoWayMax24H"),
        ("LUM-SOAM-PM-MIB", "soamPmDmStatsIfdvTwoWayAvg24H"),
        ("LUM-SOAM-PM-MIB", "soamPmDmStatsPriority"))
)
if mibBuilder.loadTexts:
    soamPmDmStatsGroupV2.setStatus("current")

soamPmLmCfgGroupV3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 60, 1, 1, 10)
)
soamPmLmCfgGroupV3.setObjects(
      *(("LUM-SOAM-PM-MIB", "soamPmLmCfgIndex"),
        ("LUM-SOAM-PM-MIB", "soamPmLmCfgName"),
        ("LUM-SOAM-PM-MIB", "soamPmLmCfgDescr"),
        ("LUM-SOAM-PM-MIB", "soamPmLmCfgSubrack"),
        ("LUM-SOAM-PM-MIB", "soamPmLmCfgSlot"),
        ("LUM-SOAM-PM-MIB", "soamPmLmCfgInternalReference"),
        ("LUM-SOAM-PM-MIB", "soamPmLmCfgLocalDeviceType"),
        ("LUM-SOAM-PM-MIB", "soamPmLmCfgType"),
        ("LUM-SOAM-PM-MIB", "soamPmLmCfgEnabled"),
        ("LUM-SOAM-PM-MIB", "soamPmLmCfgMessagePeriod"),
        ("LUM-SOAM-PM-MIB", "soamPmLmCfgPriority"),
        ("LUM-SOAM-PM-MIB", "soamPmLmCfgDestMacAddress"),
        ("LUM-SOAM-PM-MIB", "soamPmLmCfgMepName"),
        ("LUM-SOAM-PM-MIB", "soamPmLmCfgMaidIdentifier"),
        ("LUM-SOAM-PM-MIB", "soamPmLmCfgDestMepId"),
        ("LUM-SOAM-PM-MIB", "soamPmLmCfgDestIsMepId"),
        ("LUM-SOAM-PM-MIB", "soamPmLmCfgAvailabilityFlrThreshold"),
        ("LUM-SOAM-PM-MIB", "soamPmLmCfgAvailabilityUasAlarmThreshold"),
        ("LUM-SOAM-PM-MIB", "soamPmLmCfgSessionType"),
        ("LUM-SOAM-PM-MIB", "soamPmLmCfgSessionStatus"),
        ("LUM-SOAM-PM-MIB", "soamPmLmCfgCosAwareness"),
        ("LUM-SOAM-PM-MIB", "soamPmLmCfgRowStatus"),
        ("LUM-SOAM-PM-MIB", "soamPmLmCfgAdminStatus"),
        ("LUM-SOAM-PM-MIB", "soamPmLmCfgOperStatus"),
        ("LUM-SOAM-PM-MIB", "soamPmLmCfgStats"))
)
if mibBuilder.loadTexts:
    soamPmLmCfgGroupV3.setStatus("current")

soamPmDmCfgGroupV3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 60, 1, 1, 11)
)
soamPmDmCfgGroupV3.setObjects(
      *(("LUM-SOAM-PM-MIB", "soamPmDmCfgIndex"),
        ("LUM-SOAM-PM-MIB", "soamPmDmCfgName"),
        ("LUM-SOAM-PM-MIB", "soamPmDmCfgDescr"),
        ("LUM-SOAM-PM-MIB", "soamPmDmCfgSubrack"),
        ("LUM-SOAM-PM-MIB", "soamPmDmCfgSlot"),
        ("LUM-SOAM-PM-MIB", "soamPmDmCfgInternalReference"),
        ("LUM-SOAM-PM-MIB", "soamPmDmCfgLocalDeviceType"),
        ("LUM-SOAM-PM-MIB", "soamPmDmCfgDropEligible"),
        ("LUM-SOAM-PM-MIB", "soamPmDmCfgType"),
        ("LUM-SOAM-PM-MIB", "soamPmDmCfgEnabled"),
        ("LUM-SOAM-PM-MIB", "soamPmDmCfgMessagePeriod"),
        ("LUM-SOAM-PM-MIB", "soamPmDmCfgPriority"),
        ("LUM-SOAM-PM-MIB", "soamPmDmCfgDestMacAddress"),
        ("LUM-SOAM-PM-MIB", "soamPmDmCfgMepName"),
        ("LUM-SOAM-PM-MIB", "soamPmDmCfgMaidIdentifier"),
        ("LUM-SOAM-PM-MIB", "soamPmDmCfgDestMepId"),
        ("LUM-SOAM-PM-MIB", "soamPmDmCfgDestIsMepId"),
        ("LUM-SOAM-PM-MIB", "soamPmDmCfgSessionType"),
        ("LUM-SOAM-PM-MIB", "soamPmDmCfgSessionStatus"),
        ("LUM-SOAM-PM-MIB", "soamPmDmCfgRowStatus"),
        ("LUM-SOAM-PM-MIB", "soamPmDmCfgAdminStatus"),
        ("LUM-SOAM-PM-MIB", "soamPmDmCfgOperStatus"),
        ("LUM-SOAM-PM-MIB", "soamPmDmCfgStats"))
)
if mibBuilder.loadTexts:
    soamPmDmCfgGroupV3.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

soamPmBasicComplV1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 60, 1, 2, 1)
)
soamPmBasicComplV1.setObjects(
      *(("LUM-SOAM-PM-MIB", "soamPmGeneralGroupV1"),
        ("LUM-SOAM-PM-MIB", "soamPmLmCfgGroupV1"),
        ("LUM-SOAM-PM-MIB", "soamPmLmStatsGroupV1"),
        ("LUM-SOAM-PM-MIB", "soamPmDmCfgGroupV1"),
        ("LUM-SOAM-PM-MIB", "soamPmDmStatsGroupV1"))
)
if mibBuilder.loadTexts:
    soamPmBasicComplV1.setStatus(
        "current"
    )

soamPmBasicComplV2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 60, 1, 2, 2)
)
soamPmBasicComplV2.setObjects(
      *(("LUM-SOAM-PM-MIB", "soamPmGeneralGroupV1"),
        ("LUM-SOAM-PM-MIB", "soamPmLmCfgGroupV2"),
        ("LUM-SOAM-PM-MIB", "soamPmLmStatsGroupV2"),
        ("LUM-SOAM-PM-MIB", "soamPmDmCfgGroupV2"),
        ("LUM-SOAM-PM-MIB", "soamPmDmStatsGroupV2"))
)
if mibBuilder.loadTexts:
    soamPmBasicComplV2.setStatus(
        "current"
    )

soamPmBasicComplV3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 60, 1, 2, 3)
)
soamPmBasicComplV3.setObjects(
      *(("LUM-SOAM-PM-MIB", "soamPmGeneralGroupV1"),
        ("LUM-SOAM-PM-MIB", "soamPmLmCfgGroupV3"),
        ("LUM-SOAM-PM-MIB", "soamPmLmStatsGroupV2"),
        ("LUM-SOAM-PM-MIB", "soamPmDmCfgGroupV3"),
        ("LUM-SOAM-PM-MIB", "soamPmDmStatsGroupV2"))
)
if mibBuilder.loadTexts:
    soamPmBasicComplV3.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LUM-SOAM-PM-MIB",
    **{"lumSoamPmMIBModule": lumSoamPmMIBModule,
       "lumSoamPmConfs": lumSoamPmConfs,
       "lumSoamPmGroups": lumSoamPmGroups,
       "soamPmGeneralGroupV1": soamPmGeneralGroupV1,
       "soamPmLmCfgGroupV1": soamPmLmCfgGroupV1,
       "soamPmLmStatsGroupV1": soamPmLmStatsGroupV1,
       "soamPmDmCfgGroupV1": soamPmDmCfgGroupV1,
       "soamPmDmStatsGroupV1": soamPmDmStatsGroupV1,
       "soamPmLmCfgGroupV2": soamPmLmCfgGroupV2,
       "soamPmDmCfgGroupV2": soamPmDmCfgGroupV2,
       "soamPmLmStatsGroupV2": soamPmLmStatsGroupV2,
       "soamPmDmStatsGroupV2": soamPmDmStatsGroupV2,
       "soamPmLmCfgGroupV3": soamPmLmCfgGroupV3,
       "soamPmDmCfgGroupV3": soamPmDmCfgGroupV3,
       "lumSoamPmCompliances": lumSoamPmCompliances,
       "soamPmBasicComplV1": soamPmBasicComplV1,
       "soamPmBasicComplV2": soamPmBasicComplV2,
       "soamPmBasicComplV3": soamPmBasicComplV3,
       "lumSoamPmMIBObjects": lumSoamPmMIBObjects,
       "soamPmGeneral": soamPmGeneral,
       "soamPmGeneralLastChangeTime": soamPmGeneralLastChangeTime,
       "soamPmGeneralLmStateLastChangeTime": soamPmGeneralLmStateLastChangeTime,
       "soamPmGeneralLmObjectsTableSize": soamPmGeneralLmObjectsTableSize,
       "soamPmGeneralDmObjectsTableSize": soamPmGeneralDmObjectsTableSize,
       "soamPmLmObjects": soamPmLmObjects,
       "soamPmLmCfgTable": soamPmLmCfgTable,
       "soamPmLmCfgEntry": soamPmLmCfgEntry,
       "soamPmLmCfgIndex": soamPmLmCfgIndex,
       "soamPmLmCfgName": soamPmLmCfgName,
       "soamPmLmCfgDescr": soamPmLmCfgDescr,
       "soamPmLmCfgSubrack": soamPmLmCfgSubrack,
       "soamPmLmCfgSlot": soamPmLmCfgSlot,
       "soamPmLmCfgEnabled": soamPmLmCfgEnabled,
       "soamPmLmCfgMessagePeriod": soamPmLmCfgMessagePeriod,
       "soamPmLmCfgDestMacAddress": soamPmLmCfgDestMacAddress,
       "soamPmLmCfgMepName": soamPmLmCfgMepName,
       "soamPmLmCfgMaidIdentifier": soamPmLmCfgMaidIdentifier,
       "soamPmLmCfgDestMepId": soamPmLmCfgDestMepId,
       "soamPmLmCfgDestIsMepId": soamPmLmCfgDestIsMepId,
       "soamPmLmCfgInternalReference": soamPmLmCfgInternalReference,
       "soamPmLmCfgLocalDeviceType": soamPmLmCfgLocalDeviceType,
       "soamPmLmCfgType": soamPmLmCfgType,
       "soamPmLmCfgPriority": soamPmLmCfgPriority,
       "soamPmLmCfgAvailabilityFlrThreshold": soamPmLmCfgAvailabilityFlrThreshold,
       "soamPmLmCfgAvailabilityUasAlarmThreshold": soamPmLmCfgAvailabilityUasAlarmThreshold,
       "soamPmLmCfgSessionType": soamPmLmCfgSessionType,
       "soamPmLmCfgSessionStatus": soamPmLmCfgSessionStatus,
       "soamPmLmCfgCosAwareness": soamPmLmCfgCosAwareness,
       "soamPmLmCfgRowStatus": soamPmLmCfgRowStatus,
       "soamPmLmCfgAdminStatus": soamPmLmCfgAdminStatus,
       "soamPmLmCfgOperStatus": soamPmLmCfgOperStatus,
       "soamPmLmCfgStats": soamPmLmCfgStats,
       "soamPmLmStatsTable": soamPmLmStatsTable,
       "soamPmLmStatsEntry": soamPmLmStatsEntry,
       "soamPmLmStatsIndex": soamPmLmStatsIndex,
       "soamPmLmStatsLocalDeviceType": soamPmLmStatsLocalDeviceType,
       "soamPmLmStatsName": soamPmLmStatsName,
       "soamPmLmStatsSubrack": soamPmLmStatsSubrack,
       "soamPmLmStatsSlot": soamPmLmStatsSlot,
       "soamPmLmStatsMaidIdentifier": soamPmLmStatsMaidIdentifier,
       "soamPmLmStatsDestMepId": soamPmLmStatsDestMepId,
       "soamPmLmStatsInternalReference": soamPmLmStatsInternalReference,
       "soamPmLmStatsMepName": soamPmLmStatsMepName,
       "soamPmLmStatsSuspect15Min": soamPmLmStatsSuspect15Min,
       "soamPmLmStatsSuspectPrevious15Min": soamPmLmStatsSuspectPrevious15Min,
       "soamPmLmStatsSuspect24H": soamPmLmStatsSuspect24H,
       "soamPmLmStatsReset15Min": soamPmLmStatsReset15Min,
       "soamPmLmStatsReset24H": soamPmLmStatsReset24H,
       "soamPmLmStatsStartTime15Min": soamPmLmStatsStartTime15Min,
       "soamPmLmStatsElapsedTime15Min": soamPmLmStatsElapsedTime15Min,
       "soamPmLmStatsForwardTransmittedFrames15Min": soamPmLmStatsForwardTransmittedFrames15Min,
       "soamPmLmStatsForwardReceivedFrames15Min": soamPmLmStatsForwardReceivedFrames15Min,
       "soamPmLmStatsForwardMinFlr15Min": soamPmLmStatsForwardMinFlr15Min,
       "soamPmLmStatsForwardMaxFlr15Min": soamPmLmStatsForwardMaxFlr15Min,
       "soamPmLmStatsForwardAvgFlr15Min": soamPmLmStatsForwardAvgFlr15Min,
       "soamPmLmStatsForwardHighLoss15Min": soamPmLmStatsForwardHighLoss15Min,
       "soamPmLmStatsBackwardTransmittedFrames15Min": soamPmLmStatsBackwardTransmittedFrames15Min,
       "soamPmLmStatsBackwardReceivedFrames15Min": soamPmLmStatsBackwardReceivedFrames15Min,
       "soamPmLmStatsBackwardMinFlr15Min": soamPmLmStatsBackwardMinFlr15Min,
       "soamPmLmStatsBackwardMaxFlr15Min": soamPmLmStatsBackwardMaxFlr15Min,
       "soamPmLmStatsBackwardAvgFlr15Min": soamPmLmStatsBackwardAvgFlr15Min,
       "soamPmLmStatsBackwardHighLoss15Min": soamPmLmStatsBackwardHighLoss15Min,
       "soamPmLmStatsUnavailableSeconds15Min": soamPmLmStatsUnavailableSeconds15Min,
       "soamPmLmStatsStartTimePrevious15Min": soamPmLmStatsStartTimePrevious15Min,
       "soamPmLmStatsElapsedTimePrevious15Min": soamPmLmStatsElapsedTimePrevious15Min,
       "soamPmLmStatsForwardTransmittedFramesPrevious15Min": soamPmLmStatsForwardTransmittedFramesPrevious15Min,
       "soamPmLmStatsForwardReceivedFramesPrevious15Min": soamPmLmStatsForwardReceivedFramesPrevious15Min,
       "soamPmLmStatsForwardMinFlrPrevious15Min": soamPmLmStatsForwardMinFlrPrevious15Min,
       "soamPmLmStatsForwardMaxFlrPrevious15Min": soamPmLmStatsForwardMaxFlrPrevious15Min,
       "soamPmLmStatsForwardAvgFlrPrevious15Min": soamPmLmStatsForwardAvgFlrPrevious15Min,
       "soamPmLmStatsForwardHighLossPrevious15Min": soamPmLmStatsForwardHighLossPrevious15Min,
       "soamPmLmStatsBackwardTransmittedFramesPrevious15Min": soamPmLmStatsBackwardTransmittedFramesPrevious15Min,
       "soamPmLmStatsBackwardReceivedFramesPrevious15Min": soamPmLmStatsBackwardReceivedFramesPrevious15Min,
       "soamPmLmStatsBackwardMinFlrPrevious15Min": soamPmLmStatsBackwardMinFlrPrevious15Min,
       "soamPmLmStatsBackwardMaxFlrPrevious15Min": soamPmLmStatsBackwardMaxFlrPrevious15Min,
       "soamPmLmStatsBackwardAvgFlrPrevious15Min": soamPmLmStatsBackwardAvgFlrPrevious15Min,
       "soamPmLmStatsBackwardHighLossPrevious15Min": soamPmLmStatsBackwardHighLossPrevious15Min,
       "soamPmLmStatsStartTime24H": soamPmLmStatsStartTime24H,
       "soamPmLmStatsElapsedTime24H": soamPmLmStatsElapsedTime24H,
       "soamPmLmStatsForwardTransmittedFrames24H": soamPmLmStatsForwardTransmittedFrames24H,
       "soamPmLmStatsForwardReceivedFrames24H": soamPmLmStatsForwardReceivedFrames24H,
       "soamPmLmStatsForwardMinFlr24H": soamPmLmStatsForwardMinFlr24H,
       "soamPmLmStatsForwardMaxFlr24H": soamPmLmStatsForwardMaxFlr24H,
       "soamPmLmStatsForwardAvgFlr24H": soamPmLmStatsForwardAvgFlr24H,
       "soamPmLmStatsForwardHighLoss24H": soamPmLmStatsForwardHighLoss24H,
       "soamPmLmStatsBackwardTransmittedFrames24H": soamPmLmStatsBackwardTransmittedFrames24H,
       "soamPmLmStatsBackwardReceivedFrames24H": soamPmLmStatsBackwardReceivedFrames24H,
       "soamPmLmStatsBackwardMinFlr24H": soamPmLmStatsBackwardMinFlr24H,
       "soamPmLmStatsBackwardMaxFlr24H": soamPmLmStatsBackwardMaxFlr24H,
       "soamPmLmStatsBackwardAvgFlr24H": soamPmLmStatsBackwardAvgFlr24H,
       "soamPmLmStatsBackwardHighLoss24H": soamPmLmStatsBackwardHighLoss24H,
       "soamPmLmStatsUas": soamPmLmStatsUas,
       "soamPmLmStatsPriority": soamPmLmStatsPriority,
       "soamPmDmObjects": soamPmDmObjects,
       "soamPmDmCfgTable": soamPmDmCfgTable,
       "soamPmDmCfgEntry": soamPmDmCfgEntry,
       "soamPmDmCfgIndex": soamPmDmCfgIndex,
       "soamPmDmCfgName": soamPmDmCfgName,
       "soamPmDmCfgDescr": soamPmDmCfgDescr,
       "soamPmDmCfgSubrack": soamPmDmCfgSubrack,
       "soamPmDmCfgSlot": soamPmDmCfgSlot,
       "soamPmDmCfgInternalReference": soamPmDmCfgInternalReference,
       "soamPmDmCfgLocalDeviceType": soamPmDmCfgLocalDeviceType,
       "soamPmDmCfgDropEligible": soamPmDmCfgDropEligible,
       "soamPmDmCfgType": soamPmDmCfgType,
       "soamPmDmCfgEnabled": soamPmDmCfgEnabled,
       "soamPmDmCfgMessagePeriod": soamPmDmCfgMessagePeriod,
       "soamPmDmCfgPriority": soamPmDmCfgPriority,
       "soamPmDmCfgDestMacAddress": soamPmDmCfgDestMacAddress,
       "soamPmDmCfgMepName": soamPmDmCfgMepName,
       "soamPmDmCfgMaidIdentifier": soamPmDmCfgMaidIdentifier,
       "soamPmDmCfgDestMepId": soamPmDmCfgDestMepId,
       "soamPmDmCfgDestIsMepId": soamPmDmCfgDestIsMepId,
       "soamPmDmCfgSessionType": soamPmDmCfgSessionType,
       "soamPmDmCfgSessionStatus": soamPmDmCfgSessionStatus,
       "soamPmDmCfgRowStatus": soamPmDmCfgRowStatus,
       "soamPmDmCfgAdminStatus": soamPmDmCfgAdminStatus,
       "soamPmDmCfgOperStatus": soamPmDmCfgOperStatus,
       "soamPmDmCfgStats": soamPmDmCfgStats,
       "soamPmDmStatsTable": soamPmDmStatsTable,
       "soamPmDmStatsEntry": soamPmDmStatsEntry,
       "soamPmDmStatsIndex": soamPmDmStatsIndex,
       "soamPmDmStatsLocalDeviceType": soamPmDmStatsLocalDeviceType,
       "soamPmDmStatsName": soamPmDmStatsName,
       "soamPmDmStatsSubrack": soamPmDmStatsSubrack,
       "soamPmDmStatsSlot": soamPmDmStatsSlot,
       "soamPmDmStatsMaidIdentifier": soamPmDmStatsMaidIdentifier,
       "soamPmDmStatsDestMepId": soamPmDmStatsDestMepId,
       "soamPmDmStatsInternalReference": soamPmDmStatsInternalReference,
       "soamPmDmStatsMepName": soamPmDmStatsMepName,
       "soamPmDmStatsSuspect15Min": soamPmDmStatsSuspect15Min,
       "soamPmDmStatsSuspectPrevious15Min": soamPmDmStatsSuspectPrevious15Min,
       "soamPmDmStatsSuspect24H": soamPmDmStatsSuspect24H,
       "soamPmDmStatsReset15Min": soamPmDmStatsReset15Min,
       "soamPmDmStatsReset24H": soamPmDmStatsReset24H,
       "soamPmDmStatsStartTime15Min": soamPmDmStatsStartTime15Min,
       "soamPmDmStatsElapsedTime15Min": soamPmDmStatsElapsedTime15Min,
       "soamPmDmStatsFrameDelayTwoWayMin15Min": soamPmDmStatsFrameDelayTwoWayMin15Min,
       "soamPmDmStatsFrameDelayTwoWayMax15Min": soamPmDmStatsFrameDelayTwoWayMax15Min,
       "soamPmDmStatsFrameDelayTwoWayAvg15Min": soamPmDmStatsFrameDelayTwoWayAvg15Min,
       "soamPmDmStatsIfdvTwoWayMin15Min": soamPmDmStatsIfdvTwoWayMin15Min,
       "soamPmDmStatsIfdvTwoWayMax15Min": soamPmDmStatsIfdvTwoWayMax15Min,
       "soamPmDmStatsIfdvTwoWayAvg15Min": soamPmDmStatsIfdvTwoWayAvg15Min,
       "soamPmDmStatsStartTimePrevious15Min": soamPmDmStatsStartTimePrevious15Min,
       "soamPmDmStatsElapsedTimePrevious15Min": soamPmDmStatsElapsedTimePrevious15Min,
       "soamPmDmStatsFrameDelayTwoWayMinPrevious15Min": soamPmDmStatsFrameDelayTwoWayMinPrevious15Min,
       "soamPmDmStatsFrameDelayTwoWayMaxPrevious15Min": soamPmDmStatsFrameDelayTwoWayMaxPrevious15Min,
       "soamPmDmStatsFrameDelayTwoWayAvgPrevious15Min": soamPmDmStatsFrameDelayTwoWayAvgPrevious15Min,
       "soamPmDmStatsIfdvTwoWayMinPrevious15Min": soamPmDmStatsIfdvTwoWayMinPrevious15Min,
       "soamPmDmStatsIfdvTwoWayMaxPrevious15Min": soamPmDmStatsIfdvTwoWayMaxPrevious15Min,
       "soamPmDmStatsIfdvTwoWayAvgPrevious15Min": soamPmDmStatsIfdvTwoWayAvgPrevious15Min,
       "soamPmDmStatsStartTime24H": soamPmDmStatsStartTime24H,
       "soamPmDmStatsElapsedTime24H": soamPmDmStatsElapsedTime24H,
       "soamPmDmStatsFrameDelayTwoWayMin24H": soamPmDmStatsFrameDelayTwoWayMin24H,
       "soamPmDmStatsFrameDelayTwoWayMax24H": soamPmDmStatsFrameDelayTwoWayMax24H,
       "soamPmDmStatsFrameDelayTwoWayAvg24H": soamPmDmStatsFrameDelayTwoWayAvg24H,
       "soamPmDmStatsIfdvTwoWayMin24H": soamPmDmStatsIfdvTwoWayMin24H,
       "soamPmDmStatsIfdvTwoWayMax24H": soamPmDmStatsIfdvTwoWayMax24H,
       "soamPmDmStatsIfdvTwoWayAvg24H": soamPmDmStatsIfdvTwoWayAvg24H,
       "soamPmDmStatsPriority": soamPmDmStatsPriority}
)
