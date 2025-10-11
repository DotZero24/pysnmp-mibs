# SNMP MIB module (LUM-IFMC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/LUM-IFMC-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:14:39 2025
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

(lumIfMcMIB,
 lumModules) = mibBuilder.importSymbols(
    "LUM-REG",
    "lumIfMcMIB",
    "lumModules")

(BoardOrInterfaceAdminStatus,
 BoardOrInterfaceOperStatus,
 FaultStatus,
 MgmtNameString,
 PortNumber,
 SlotNumber,
 SubrackNumber) = mibBuilder.importSymbols(
    "LUM-TC",
    "BoardOrInterfaceAdminStatus",
    "BoardOrInterfaceOperStatus",
    "FaultStatus",
    "MgmtNameString",
    "PortNumber",
    "SlotNumber",
    "SubrackNumber")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

lumIfMcMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 1, 1, 64)
)
if mibBuilder.loadTexts:
    lumIfMcMIBModule.setRevisions(
        ("2018-07-09 00:00",
         "2018-04-13 00:00",
         "2017-09-01 00:00",
         "2017-06-15 00:00",
         "2015-03-15 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class IfMcExpectedType(TextualConvention, Integer32):
    status = "current"
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
        *(("ethernet100gLanSR10", 1),
          ("ethernet12x10gLan", 2),
          ("frontplane12x10g", 3),
          ("frontplane100g", 4),
          ("filter10x10g", 5),
          ("notApplicable", 6))
    )



class IfMcMpoCableType(TextualConvention, Integer32):
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
        *(("straight", 1),
          ("completeFanout", 2),
          ("fanout2x5", 3),
          ("notApplicable", 4))
    )



# MIB Managed Objects in the order of their OIDs

_LumIfMcConfs_ObjectIdentity = ObjectIdentity
lumIfMcConfs = _LumIfMcConfs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 64, 1)
)
_LumIfMcGroups_ObjectIdentity = ObjectIdentity
lumIfMcGroups = _LumIfMcGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 64, 1, 1)
)
_LumIfMcCompl_ObjectIdentity = ObjectIdentity
lumIfMcCompl = _LumIfMcCompl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 64, 1, 2)
)
_LumIfMcMIBObjects_ObjectIdentity = ObjectIdentity
lumIfMcMIBObjects = _LumIfMcMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 64, 2)
)
_IfMcGeneral_ObjectIdentity = ObjectIdentity
ifMcGeneral = _IfMcGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 64, 2, 1)
)
_IfMcGeneralConfigLastChangeTime_Type = DateAndTime
_IfMcGeneralConfigLastChangeTime_Object = MibScalar
ifMcGeneralConfigLastChangeTime = _IfMcGeneralConfigLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 64, 2, 1, 1),
    _IfMcGeneralConfigLastChangeTime_Type()
)
ifMcGeneralConfigLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifMcGeneralConfigLastChangeTime.setStatus("current")
_IfMcGeneralStateLastChangeTime_Type = DateAndTime
_IfMcGeneralStateLastChangeTime_Object = MibScalar
ifMcGeneralStateLastChangeTime = _IfMcGeneralStateLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 64, 2, 1, 2),
    _IfMcGeneralStateLastChangeTime_Type()
)
ifMcGeneralStateLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifMcGeneralStateLastChangeTime.setStatus("current")
_IfMcGeneralIfMcPortTableSize_Type = Unsigned32
_IfMcGeneralIfMcPortTableSize_Object = MibScalar
ifMcGeneralIfMcPortTableSize = _IfMcGeneralIfMcPortTableSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 64, 2, 1, 3),
    _IfMcGeneralIfMcPortTableSize_Type()
)
ifMcGeneralIfMcPortTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifMcGeneralIfMcPortTableSize.setStatus("current")
_IfMcGeneralIfMcPortConfigLastChangeTime_Type = DateAndTime
_IfMcGeneralIfMcPortConfigLastChangeTime_Object = MibScalar
ifMcGeneralIfMcPortConfigLastChangeTime = _IfMcGeneralIfMcPortConfigLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 64, 2, 1, 4),
    _IfMcGeneralIfMcPortConfigLastChangeTime_Type()
)
ifMcGeneralIfMcPortConfigLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifMcGeneralIfMcPortConfigLastChangeTime.setStatus("current")
_IfMcGeneralIfMcPortStateLastChangeTime_Type = DateAndTime
_IfMcGeneralIfMcPortStateLastChangeTime_Object = MibScalar
ifMcGeneralIfMcPortStateLastChangeTime = _IfMcGeneralIfMcPortStateLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 64, 2, 1, 5),
    _IfMcGeneralIfMcPortStateLastChangeTime_Type()
)
ifMcGeneralIfMcPortStateLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifMcGeneralIfMcPortStateLastChangeTime.setStatus("current")
_IfMcPortList_ObjectIdentity = ObjectIdentity
ifMcPortList = _IfMcPortList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 64, 2, 2)
)
_IfMcPortTable_Object = MibTable
ifMcPortTable = _IfMcPortTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 64, 2, 2, 1)
)
if mibBuilder.loadTexts:
    ifMcPortTable.setStatus("current")
_IfMcPortEntry_Object = MibTableRow
ifMcPortEntry = _IfMcPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 64, 2, 2, 1, 1)
)
ifMcPortEntry.setIndexNames(
    (0, "LUM-IFMC-MIB", "ifMcPortIndex"),
)
if mibBuilder.loadTexts:
    ifMcPortEntry.setStatus("current")
_IfMcPortName_Type = MgmtNameString
_IfMcPortName_Object = MibTableColumn
ifMcPortName = _IfMcPortName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 64, 2, 2, 1, 1, 1),
    _IfMcPortName_Type()
)
ifMcPortName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ifMcPortName.setStatus("current")


class _IfMcPortIndex_Type(Unsigned32):
    """Custom type ifMcPortIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_IfMcPortIndex_Type.__name__ = "Unsigned32"
_IfMcPortIndex_Object = MibTableColumn
ifMcPortIndex = _IfMcPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 64, 2, 2, 1, 1, 2),
    _IfMcPortIndex_Type()
)
ifMcPortIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ifMcPortIndex.setStatus("current")


class _IfMcPortDescr_Type(DisplayString):
    """Custom type ifMcPortDescr based on DisplayString"""
    defaultValue = OctetString("")


_IfMcPortDescr_Type.__name__ = "DisplayString"
_IfMcPortDescr_Object = MibTableColumn
ifMcPortDescr = _IfMcPortDescr_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 64, 2, 2, 1, 1, 3),
    _IfMcPortDescr_Type()
)
ifMcPortDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifMcPortDescr.setStatus("current")


class _IfMcPortExpectedType_Type(IfMcExpectedType):
    """Custom type ifMcPortExpectedType based on IfMcExpectedType"""
    defaultValue = 1


_IfMcPortExpectedType_Type.__name__ = "IfMcExpectedType"
_IfMcPortExpectedType_Object = MibTableColumn
ifMcPortExpectedType = _IfMcPortExpectedType_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 64, 2, 2, 1, 1, 4),
    _IfMcPortExpectedType_Type()
)
ifMcPortExpectedType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifMcPortExpectedType.setStatus("current")


class _IfMcPortIdx_Type(Integer32):
    """Custom type ifMcPortIdx based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_IfMcPortIdx_Type.__name__ = "Integer32"
_IfMcPortIdx_Object = MibTableColumn
ifMcPortIdx = _IfMcPortIdx_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 64, 2, 2, 1, 1, 5),
    _IfMcPortIdx_Type()
)
ifMcPortIdx.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ifMcPortIdx.setStatus("current")
_IfMcPortSubrack_Type = SubrackNumber
_IfMcPortSubrack_Object = MibTableColumn
ifMcPortSubrack = _IfMcPortSubrack_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 64, 2, 2, 1, 1, 6),
    _IfMcPortSubrack_Type()
)
ifMcPortSubrack.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ifMcPortSubrack.setStatus("current")
_IfMcPortSlot_Type = SlotNumber
_IfMcPortSlot_Object = MibTableColumn
ifMcPortSlot = _IfMcPortSlot_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 64, 2, 2, 1, 1, 7),
    _IfMcPortSlot_Type()
)
ifMcPortSlot.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ifMcPortSlot.setStatus("current")


class _IfMcPortIfNo_Type(PortNumber):
    """Custom type ifMcPortIfNo based on PortNumber"""
    defaultValue = 0


_IfMcPortIfNo_Type.__name__ = "PortNumber"
_IfMcPortIfNo_Object = MibTableColumn
ifMcPortIfNo = _IfMcPortIfNo_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 64, 2, 2, 1, 1, 8),
    _IfMcPortIfNo_Type()
)
ifMcPortIfNo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ifMcPortIfNo.setStatus("current")
_IfMcPortLossOfSignal_Type = FaultStatus
_IfMcPortLossOfSignal_Object = MibTableColumn
ifMcPortLossOfSignal = _IfMcPortLossOfSignal_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 64, 2, 2, 1, 1, 9),
    _IfMcPortLossOfSignal_Type()
)
ifMcPortLossOfSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifMcPortLossOfSignal.setStatus("current")


class _IfMcPortAdminStatus_Type(BoardOrInterfaceAdminStatus):
    """Custom type ifMcPortAdminStatus based on BoardOrInterfaceAdminStatus"""
    defaultValue = 3


_IfMcPortAdminStatus_Type.__name__ = "BoardOrInterfaceAdminStatus"
_IfMcPortAdminStatus_Object = MibTableColumn
ifMcPortAdminStatus = _IfMcPortAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 64, 2, 2, 1, 1, 10),
    _IfMcPortAdminStatus_Type()
)
ifMcPortAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifMcPortAdminStatus.setStatus("current")


class _IfMcPortOperStatus_Type(BoardOrInterfaceOperStatus):
    """Custom type ifMcPortOperStatus based on BoardOrInterfaceOperStatus"""
    defaultValue = 1


_IfMcPortOperStatus_Type.__name__ = "BoardOrInterfaceOperStatus"
_IfMcPortOperStatus_Object = MibTableColumn
ifMcPortOperStatus = _IfMcPortOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 64, 2, 2, 1, 1, 11),
    _IfMcPortOperStatus_Type()
)
ifMcPortOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifMcPortOperStatus.setStatus("current")


class _IfMcPortTrxClass_Type(DisplayString):
    """Custom type ifMcPortTrxClass based on DisplayString"""
    defaultValue = OctetString("")


_IfMcPortTrxClass_Type.__name__ = "DisplayString"
_IfMcPortTrxClass_Object = MibTableColumn
ifMcPortTrxClass = _IfMcPortTrxClass_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 64, 2, 2, 1, 1, 12),
    _IfMcPortTrxClass_Type()
)
ifMcPortTrxClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifMcPortTrxClass.setStatus("current")
_IfMcPortReceivedPowerLow_Type = FaultStatus
_IfMcPortReceivedPowerLow_Object = MibTableColumn
ifMcPortReceivedPowerLow = _IfMcPortReceivedPowerLow_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 64, 2, 2, 1, 1, 13),
    _IfMcPortReceivedPowerLow_Type()
)
ifMcPortReceivedPowerLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifMcPortReceivedPowerLow.setStatus("current")


class _IfMcPortMpoCableType_Type(IfMcMpoCableType):
    """Custom type ifMcPortMpoCableType based on IfMcMpoCableType"""
    defaultValue = 4


_IfMcPortMpoCableType_Type.__name__ = "IfMcMpoCableType"
_IfMcPortMpoCableType_Object = MibTableColumn
ifMcPortMpoCableType = _IfMcPortMpoCableType_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 64, 2, 2, 1, 1, 14),
    _IfMcPortMpoCableType_Type()
)
ifMcPortMpoCableType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifMcPortMpoCableType.setStatus("current")

# Managed Objects groups

ifMcGeneralGroupV1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 64, 1, 1, 1)
)
ifMcGeneralGroupV1.setObjects(
      *(("LUM-IFMC-MIB", "ifMcGeneralConfigLastChangeTime"),
        ("LUM-IFMC-MIB", "ifMcGeneralStateLastChangeTime"),
        ("LUM-IFMC-MIB", "ifMcGeneralIfMcPortTableSize"),
        ("LUM-IFMC-MIB", "ifMcGeneralIfMcPortConfigLastChangeTime"),
        ("LUM-IFMC-MIB", "ifMcGeneralIfMcPortStateLastChangeTime"))
)
if mibBuilder.loadTexts:
    ifMcGeneralGroupV1.setStatus("current")

ifMcPortGroupV1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 64, 1, 1, 2)
)
ifMcPortGroupV1.setObjects(
      *(("LUM-IFMC-MIB", "ifMcPortName"),
        ("LUM-IFMC-MIB", "ifMcPortIndex"),
        ("LUM-IFMC-MIB", "ifMcPortDescr"),
        ("LUM-IFMC-MIB", "ifMcPortExpectedType"),
        ("LUM-IFMC-MIB", "ifMcPortIdx"),
        ("LUM-IFMC-MIB", "ifMcPortSubrack"),
        ("LUM-IFMC-MIB", "ifMcPortSlot"),
        ("LUM-IFMC-MIB", "ifMcPortIfNo"))
)
if mibBuilder.loadTexts:
    ifMcPortGroupV1.setStatus("deprecated")

ifMcPortGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 64, 1, 1, 3)
)
ifMcPortGroupV2.setObjects(
      *(("LUM-IFMC-MIB", "ifMcPortName"),
        ("LUM-IFMC-MIB", "ifMcPortIndex"),
        ("LUM-IFMC-MIB", "ifMcPortDescr"),
        ("LUM-IFMC-MIB", "ifMcPortExpectedType"),
        ("LUM-IFMC-MIB", "ifMcPortIdx"),
        ("LUM-IFMC-MIB", "ifMcPortSubrack"),
        ("LUM-IFMC-MIB", "ifMcPortSlot"),
        ("LUM-IFMC-MIB", "ifMcPortIfNo"),
        ("LUM-IFMC-MIB", "ifMcPortLossOfSignal"))
)
if mibBuilder.loadTexts:
    ifMcPortGroupV2.setStatus("deprecated")

ifMcPortGroupV3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 64, 1, 1, 4)
)
ifMcPortGroupV3.setObjects(
      *(("LUM-IFMC-MIB", "ifMcPortName"),
        ("LUM-IFMC-MIB", "ifMcPortIndex"),
        ("LUM-IFMC-MIB", "ifMcPortDescr"),
        ("LUM-IFMC-MIB", "ifMcPortExpectedType"),
        ("LUM-IFMC-MIB", "ifMcPortIdx"),
        ("LUM-IFMC-MIB", "ifMcPortSubrack"),
        ("LUM-IFMC-MIB", "ifMcPortSlot"),
        ("LUM-IFMC-MIB", "ifMcPortIfNo"),
        ("LUM-IFMC-MIB", "ifMcPortLossOfSignal"),
        ("LUM-IFMC-MIB", "ifMcPortAdminStatus"),
        ("LUM-IFMC-MIB", "ifMcPortOperStatus"),
        ("LUM-IFMC-MIB", "ifMcPortTrxClass"))
)
if mibBuilder.loadTexts:
    ifMcPortGroupV3.setStatus("deprecated")

ifMcPortGroupV4 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 64, 1, 1, 5)
)
ifMcPortGroupV4.setObjects(
      *(("LUM-IFMC-MIB", "ifMcPortName"),
        ("LUM-IFMC-MIB", "ifMcPortIndex"),
        ("LUM-IFMC-MIB", "ifMcPortDescr"),
        ("LUM-IFMC-MIB", "ifMcPortExpectedType"),
        ("LUM-IFMC-MIB", "ifMcPortIdx"),
        ("LUM-IFMC-MIB", "ifMcPortSubrack"),
        ("LUM-IFMC-MIB", "ifMcPortSlot"),
        ("LUM-IFMC-MIB", "ifMcPortIfNo"),
        ("LUM-IFMC-MIB", "ifMcPortLossOfSignal"),
        ("LUM-IFMC-MIB", "ifMcPortAdminStatus"),
        ("LUM-IFMC-MIB", "ifMcPortOperStatus"),
        ("LUM-IFMC-MIB", "ifMcPortTrxClass"),
        ("LUM-IFMC-MIB", "ifMcPortReceivedPowerLow"))
)
if mibBuilder.loadTexts:
    ifMcPortGroupV4.setStatus("deprecated")

ifMcPortGroupV5 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 64, 1, 1, 6)
)
ifMcPortGroupV5.setObjects(
      *(("LUM-IFMC-MIB", "ifMcPortName"),
        ("LUM-IFMC-MIB", "ifMcPortIndex"),
        ("LUM-IFMC-MIB", "ifMcPortDescr"),
        ("LUM-IFMC-MIB", "ifMcPortExpectedType"),
        ("LUM-IFMC-MIB", "ifMcPortIdx"),
        ("LUM-IFMC-MIB", "ifMcPortSubrack"),
        ("LUM-IFMC-MIB", "ifMcPortSlot"),
        ("LUM-IFMC-MIB", "ifMcPortIfNo"),
        ("LUM-IFMC-MIB", "ifMcPortLossOfSignal"),
        ("LUM-IFMC-MIB", "ifMcPortAdminStatus"),
        ("LUM-IFMC-MIB", "ifMcPortOperStatus"),
        ("LUM-IFMC-MIB", "ifMcPortTrxClass"),
        ("LUM-IFMC-MIB", "ifMcPortReceivedPowerLow"),
        ("LUM-IFMC-MIB", "ifMcPortMpoCableType"))
)
if mibBuilder.loadTexts:
    ifMcPortGroupV5.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

lumIfMcComplV1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 64, 1, 2, 1)
)
lumIfMcComplV1.setObjects(
      *(("LUM-IFMC-MIB", "ifMcGeneralGroupV1"),
        ("LUM-IFMC-MIB", "ifMcPortGroupV1"))
)
if mibBuilder.loadTexts:
    lumIfMcComplV1.setStatus(
        "deprecated"
    )

lumIfMcComplV2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 64, 1, 2, 2)
)
lumIfMcComplV2.setObjects(
      *(("LUM-IFMC-MIB", "ifMcGeneralGroupV1"),
        ("LUM-IFMC-MIB", "ifMcPortGroupV2"))
)
if mibBuilder.loadTexts:
    lumIfMcComplV2.setStatus(
        "deprecated"
    )

lumIfMcComplV3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 64, 1, 2, 3)
)
lumIfMcComplV3.setObjects(
      *(("LUM-IFMC-MIB", "ifMcGeneralGroupV1"),
        ("LUM-IFMC-MIB", "ifMcPortGroupV3"))
)
if mibBuilder.loadTexts:
    lumIfMcComplV3.setStatus(
        "deprecated"
    )

lumIfMcComplV4 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 64, 1, 2, 4)
)
lumIfMcComplV4.setObjects(
      *(("LUM-IFMC-MIB", "ifMcGeneralGroupV1"),
        ("LUM-IFMC-MIB", "ifMcPortGroupV4"))
)
if mibBuilder.loadTexts:
    lumIfMcComplV4.setStatus(
        "deprecated"
    )

lumIfMcComplV5 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 64, 1, 2, 5)
)
lumIfMcComplV5.setObjects(
      *(("LUM-IFMC-MIB", "ifMcGeneralGroupV1"),
        ("LUM-IFMC-MIB", "ifMcPortGroupV5"))
)
if mibBuilder.loadTexts:
    lumIfMcComplV5.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LUM-IFMC-MIB",
    **{"IfMcExpectedType": IfMcExpectedType,
       "IfMcMpoCableType": IfMcMpoCableType,
       "lumIfMcMIBModule": lumIfMcMIBModule,
       "lumIfMcConfs": lumIfMcConfs,
       "lumIfMcGroups": lumIfMcGroups,
       "ifMcGeneralGroupV1": ifMcGeneralGroupV1,
       "ifMcPortGroupV1": ifMcPortGroupV1,
       "ifMcPortGroupV2": ifMcPortGroupV2,
       "ifMcPortGroupV3": ifMcPortGroupV3,
       "ifMcPortGroupV4": ifMcPortGroupV4,
       "ifMcPortGroupV5": ifMcPortGroupV5,
       "lumIfMcCompl": lumIfMcCompl,
       "lumIfMcComplV1": lumIfMcComplV1,
       "lumIfMcComplV2": lumIfMcComplV2,
       "lumIfMcComplV3": lumIfMcComplV3,
       "lumIfMcComplV4": lumIfMcComplV4,
       "lumIfMcComplV5": lumIfMcComplV5,
       "lumIfMcMIBObjects": lumIfMcMIBObjects,
       "ifMcGeneral": ifMcGeneral,
       "ifMcGeneralConfigLastChangeTime": ifMcGeneralConfigLastChangeTime,
       "ifMcGeneralStateLastChangeTime": ifMcGeneralStateLastChangeTime,
       "ifMcGeneralIfMcPortTableSize": ifMcGeneralIfMcPortTableSize,
       "ifMcGeneralIfMcPortConfigLastChangeTime": ifMcGeneralIfMcPortConfigLastChangeTime,
       "ifMcGeneralIfMcPortStateLastChangeTime": ifMcGeneralIfMcPortStateLastChangeTime,
       "ifMcPortList": ifMcPortList,
       "ifMcPortTable": ifMcPortTable,
       "ifMcPortEntry": ifMcPortEntry,
       "ifMcPortName": ifMcPortName,
       "ifMcPortIndex": ifMcPortIndex,
       "ifMcPortDescr": ifMcPortDescr,
       "ifMcPortExpectedType": ifMcPortExpectedType,
       "ifMcPortIdx": ifMcPortIdx,
       "ifMcPortSubrack": ifMcPortSubrack,
       "ifMcPortSlot": ifMcPortSlot,
       "ifMcPortIfNo": ifMcPortIfNo,
       "ifMcPortLossOfSignal": ifMcPortLossOfSignal,
       "ifMcPortAdminStatus": ifMcPortAdminStatus,
       "ifMcPortOperStatus": ifMcPortOperStatus,
       "ifMcPortTrxClass": ifMcPortTrxClass,
       "ifMcPortReceivedPowerLow": ifMcPortReceivedPowerLow,
       "ifMcPortMpoCableType": ifMcPortMpoCableType}
)
