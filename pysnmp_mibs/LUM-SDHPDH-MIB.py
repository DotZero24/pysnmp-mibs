# SNMP MIB module (LUM-SDHPDH-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/LUM-SDHPDH-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:17:18 2025
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

(lumModules,
 lumSdhpdhMIB) = mibBuilder.importSymbols(
    "LUM-REG",
    "lumModules",
    "lumSdhpdhMIB")

(BoardOrInterfaceAdminStatus,
 BoardOrInterfaceOperStatus,
 CommandString,
 FaultStatus,
 MgmtNameString) = mibBuilder.importSymbols(
    "LUM-TC",
    "BoardOrInterfaceAdminStatus",
    "BoardOrInterfaceOperStatus",
    "CommandString",
    "FaultStatus",
    "MgmtNameString")

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

lumSdhpdhMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 1, 1, 35)
)
if mibBuilder.loadTexts:
    lumSdhpdhMIBModule.setRevisions(
        ("2017-06-15 00:00",
         "2016-01-11 00:00",
         "2011-06-15 00:00",
         "2009-06-15 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_LumSdhpdhConfs_ObjectIdentity = ObjectIdentity
lumSdhpdhConfs = _LumSdhpdhConfs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 35, 1)
)
_LumSdhpdhGroups_ObjectIdentity = ObjectIdentity
lumSdhpdhGroups = _LumSdhpdhGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 35, 1, 1)
)
_LumSdhpdhCompl_ObjectIdentity = ObjectIdentity
lumSdhpdhCompl = _LumSdhpdhCompl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 35, 1, 2)
)
_LumSdhpdhMIBObjects_ObjectIdentity = ObjectIdentity
lumSdhpdhMIBObjects = _LumSdhpdhMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 35, 2)
)
_SdhpdhGeneral_ObjectIdentity = ObjectIdentity
sdhpdhGeneral = _SdhpdhGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 35, 2, 1)
)
_SdhpdhGeneralLastChangeTime_Type = DateAndTime
_SdhpdhGeneralLastChangeTime_Object = MibScalar
sdhpdhGeneralLastChangeTime = _SdhpdhGeneralLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 35, 2, 1, 1),
    _SdhpdhGeneralLastChangeTime_Type()
)
sdhpdhGeneralLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdhpdhGeneralLastChangeTime.setStatus("current")
_SdhpdhGeneralStateLastChangeTime_Type = DateAndTime
_SdhpdhGeneralStateLastChangeTime_Object = MibScalar
sdhpdhGeneralStateLastChangeTime = _SdhpdhGeneralStateLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 35, 2, 1, 2),
    _SdhpdhGeneralStateLastChangeTime_Type()
)
sdhpdhGeneralStateLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdhpdhGeneralStateLastChangeTime.setStatus("current")
_SdhpdhGeneralE1t1TableSize_Type = Unsigned32
_SdhpdhGeneralE1t1TableSize_Object = MibScalar
sdhpdhGeneralE1t1TableSize = _SdhpdhGeneralE1t1TableSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 35, 2, 1, 3),
    _SdhpdhGeneralE1t1TableSize_Type()
)
sdhpdhGeneralE1t1TableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdhpdhGeneralE1t1TableSize.setStatus("current")
_SdhpdhGeneralEquipmentTableSize_Type = Unsigned32
_SdhpdhGeneralEquipmentTableSize_Object = MibScalar
sdhpdhGeneralEquipmentTableSize = _SdhpdhGeneralEquipmentTableSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 35, 2, 1, 4),
    _SdhpdhGeneralEquipmentTableSize_Type()
)
sdhpdhGeneralEquipmentTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdhpdhGeneralEquipmentTableSize.setStatus("current")
_SdhpdhE1t1List_ObjectIdentity = ObjectIdentity
sdhpdhE1t1List = _SdhpdhE1t1List_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 35, 2, 2)
)
_SdhpdhE1t1Table_Object = MibTable
sdhpdhE1t1Table = _SdhpdhE1t1Table_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 35, 2, 2, 1)
)
if mibBuilder.loadTexts:
    sdhpdhE1t1Table.setStatus("current")
_SdhpdhE1t1Entry_Object = MibTableRow
sdhpdhE1t1Entry = _SdhpdhE1t1Entry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 35, 2, 2, 1, 1)
)
sdhpdhE1t1Entry.setIndexNames(
    (0, "LUM-SDHPDH-MIB", "sdhpdhE1t1Index"),
)
if mibBuilder.loadTexts:
    sdhpdhE1t1Entry.setStatus("current")


class _SdhpdhE1t1Index_Type(Unsigned32):
    """Custom type sdhpdhE1t1Index based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_SdhpdhE1t1Index_Type.__name__ = "Unsigned32"
_SdhpdhE1t1Index_Object = MibTableColumn
sdhpdhE1t1Index = _SdhpdhE1t1Index_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 35, 2, 2, 1, 1, 1),
    _SdhpdhE1t1Index_Type()
)
sdhpdhE1t1Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdhpdhE1t1Index.setStatus("current")


class _SdhpdhE1t1Name_Type(MgmtNameString):
    """Custom type sdhpdhE1t1Name based on MgmtNameString"""
    defaultValue = OctetString("")


_SdhpdhE1t1Name_Type.__name__ = "MgmtNameString"
_SdhpdhE1t1Name_Object = MibTableColumn
sdhpdhE1t1Name = _SdhpdhE1t1Name_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 35, 2, 2, 1, 1, 2),
    _SdhpdhE1t1Name_Type()
)
sdhpdhE1t1Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdhpdhE1t1Name.setStatus("current")


class _SdhpdhE1t1Descr_Type(DisplayString):
    """Custom type sdhpdhE1t1Descr based on DisplayString"""
    defaultValue = OctetString("")


_SdhpdhE1t1Descr_Type.__name__ = "DisplayString"
_SdhpdhE1t1Descr_Object = MibTableColumn
sdhpdhE1t1Descr = _SdhpdhE1t1Descr_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 35, 2, 2, 1, 1, 6),
    _SdhpdhE1t1Descr_Type()
)
sdhpdhE1t1Descr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdhpdhE1t1Descr.setStatus("current")


class _SdhpdhE1t1AdminStatus_Type(BoardOrInterfaceAdminStatus):
    """Custom type sdhpdhE1t1AdminStatus based on BoardOrInterfaceAdminStatus"""
    defaultValue = 3


_SdhpdhE1t1AdminStatus_Type.__name__ = "BoardOrInterfaceAdminStatus"
_SdhpdhE1t1AdminStatus_Object = MibTableColumn
sdhpdhE1t1AdminStatus = _SdhpdhE1t1AdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 35, 2, 2, 1, 1, 7),
    _SdhpdhE1t1AdminStatus_Type()
)
sdhpdhE1t1AdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdhpdhE1t1AdminStatus.setStatus("current")


class _SdhpdhE1t1OperStatus_Type(BoardOrInterfaceOperStatus):
    """Custom type sdhpdhE1t1OperStatus based on BoardOrInterfaceOperStatus"""
    defaultValue = 1


_SdhpdhE1t1OperStatus_Type.__name__ = "BoardOrInterfaceOperStatus"
_SdhpdhE1t1OperStatus_Object = MibTableColumn
sdhpdhE1t1OperStatus = _SdhpdhE1t1OperStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 35, 2, 2, 1, 1, 8),
    _SdhpdhE1t1OperStatus_Type()
)
sdhpdhE1t1OperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdhpdhE1t1OperStatus.setStatus("current")
_SdhpdhE1t1AlarmIndicationSignalW2C_Type = FaultStatus
_SdhpdhE1t1AlarmIndicationSignalW2C_Object = MibTableColumn
sdhpdhE1t1AlarmIndicationSignalW2C = _SdhpdhE1t1AlarmIndicationSignalW2C_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 35, 2, 2, 1, 1, 9),
    _SdhpdhE1t1AlarmIndicationSignalW2C_Type()
)
sdhpdhE1t1AlarmIndicationSignalW2C.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdhpdhE1t1AlarmIndicationSignalW2C.setStatus("current")
_SdhpdhE1t1AlarmIndicationSignalC2W_Type = FaultStatus
_SdhpdhE1t1AlarmIndicationSignalC2W_Object = MibTableColumn
sdhpdhE1t1AlarmIndicationSignalC2W = _SdhpdhE1t1AlarmIndicationSignalC2W_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 35, 2, 2, 1, 1, 10),
    _SdhpdhE1t1AlarmIndicationSignalC2W_Type()
)
sdhpdhE1t1AlarmIndicationSignalC2W.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdhpdhE1t1AlarmIndicationSignalC2W.setStatus("current")
_SdhpdhE1t1LossOfFrameC2W_Type = FaultStatus
_SdhpdhE1t1LossOfFrameC2W_Object = MibTableColumn
sdhpdhE1t1LossOfFrameC2W = _SdhpdhE1t1LossOfFrameC2W_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 35, 2, 2, 1, 1, 11),
    _SdhpdhE1t1LossOfFrameC2W_Type()
)
sdhpdhE1t1LossOfFrameC2W.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdhpdhE1t1LossOfFrameC2W.setStatus("current")
_SdhpdhE1t1LossOfFrameW2C_Type = FaultStatus
_SdhpdhE1t1LossOfFrameW2C_Object = MibTableColumn
sdhpdhE1t1LossOfFrameW2C = _SdhpdhE1t1LossOfFrameW2C_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 35, 2, 2, 1, 1, 12),
    _SdhpdhE1t1LossOfFrameW2C_Type()
)
sdhpdhE1t1LossOfFrameW2C.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdhpdhE1t1LossOfFrameW2C.setStatus("current")
_SdhpdhE1t1UnEquipped_Type = FaultStatus
_SdhpdhE1t1UnEquipped_Object = MibTableColumn
sdhpdhE1t1UnEquipped = _SdhpdhE1t1UnEquipped_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 35, 2, 2, 1, 1, 13),
    _SdhpdhE1t1UnEquipped_Type()
)
sdhpdhE1t1UnEquipped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdhpdhE1t1UnEquipped.setStatus("current")


class _SdhpdhE1t1ConnectionStatus_Type(DisplayString):
    """Custom type sdhpdhE1t1ConnectionStatus based on DisplayString"""
    defaultValue = OctetString("Not connected")


_SdhpdhE1t1ConnectionStatus_Type.__name__ = "DisplayString"
_SdhpdhE1t1ConnectionStatus_Object = MibTableColumn
sdhpdhE1t1ConnectionStatus = _SdhpdhE1t1ConnectionStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 35, 2, 2, 1, 1, 14),
    _SdhpdhE1t1ConnectionStatus_Type()
)
sdhpdhE1t1ConnectionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdhpdhE1t1ConnectionStatus.setStatus("current")
_SdhpdhE1t1SubChannelId_Type = Unsigned32
_SdhpdhE1t1SubChannelId_Object = MibTableColumn
sdhpdhE1t1SubChannelId = _SdhpdhE1t1SubChannelId_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 35, 2, 2, 1, 1, 15),
    _SdhpdhE1t1SubChannelId_Type()
)
sdhpdhE1t1SubChannelId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdhpdhE1t1SubChannelId.setStatus("current")


class _SdhpdhE1t1MultiplexingInformation_Type(DisplayString):
    """Custom type sdhpdhE1t1MultiplexingInformation based on DisplayString"""
    defaultValue = OctetString("")


_SdhpdhE1t1MultiplexingInformation_Type.__name__ = "DisplayString"
_SdhpdhE1t1MultiplexingInformation_Object = MibTableColumn
sdhpdhE1t1MultiplexingInformation = _SdhpdhE1t1MultiplexingInformation_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 35, 2, 2, 1, 1, 16),
    _SdhpdhE1t1MultiplexingInformation_Type()
)
sdhpdhE1t1MultiplexingInformation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdhpdhE1t1MultiplexingInformation.setStatus("current")


class _SdhpdhE1t1RxSignalStatus_Type(Integer32):
    """Custom type sdhpdhE1t1RxSignalStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 1),
          ("degraded", 2),
          ("up", 3))
    )


_SdhpdhE1t1RxSignalStatus_Type.__name__ = "Integer32"
_SdhpdhE1t1RxSignalStatus_Object = MibTableColumn
sdhpdhE1t1RxSignalStatus = _SdhpdhE1t1RxSignalStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 35, 2, 2, 1, 1, 17),
    _SdhpdhE1t1RxSignalStatus_Type()
)
sdhpdhE1t1RxSignalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdhpdhE1t1RxSignalStatus.setStatus("current")


class _SdhpdhE1t1TxSignalStatus_Type(Integer32):
    """Custom type sdhpdhE1t1TxSignalStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 1),
          ("degraded", 2),
          ("up", 3))
    )


_SdhpdhE1t1TxSignalStatus_Type.__name__ = "Integer32"
_SdhpdhE1t1TxSignalStatus_Object = MibTableColumn
sdhpdhE1t1TxSignalStatus = _SdhpdhE1t1TxSignalStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 35, 2, 2, 1, 1, 18),
    _SdhpdhE1t1TxSignalStatus_Type()
)
sdhpdhE1t1TxSignalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdhpdhE1t1TxSignalStatus.setStatus("current")
_SdhpdhE1t1VcIndex_Type = Unsigned32
_SdhpdhE1t1VcIndex_Object = MibTableColumn
sdhpdhE1t1VcIndex = _SdhpdhE1t1VcIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 35, 2, 2, 1, 1, 19),
    _SdhpdhE1t1VcIndex_Type()
)
sdhpdhE1t1VcIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdhpdhE1t1VcIndex.setStatus("current")
_SdhpdhE1t1ClockDomain_Type = DisplayString
_SdhpdhE1t1ClockDomain_Object = MibTableColumn
sdhpdhE1t1ClockDomain = _SdhpdhE1t1ClockDomain_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 35, 2, 2, 1, 1, 20),
    _SdhpdhE1t1ClockDomain_Type()
)
sdhpdhE1t1ClockDomain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdhpdhE1t1ClockDomain.setStatus("current")
_SdhpdhE1t1TuAlarmIndicationSignalC2W_Type = FaultStatus
_SdhpdhE1t1TuAlarmIndicationSignalC2W_Object = MibTableColumn
sdhpdhE1t1TuAlarmIndicationSignalC2W = _SdhpdhE1t1TuAlarmIndicationSignalC2W_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 35, 2, 2, 1, 1, 21),
    _SdhpdhE1t1TuAlarmIndicationSignalC2W_Type()
)
sdhpdhE1t1TuAlarmIndicationSignalC2W.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdhpdhE1t1TuAlarmIndicationSignalC2W.setStatus("current")
_SdhpdhE1t1TuLossOfPointerC2W_Type = FaultStatus
_SdhpdhE1t1TuLossOfPointerC2W_Object = MibTableColumn
sdhpdhE1t1TuLossOfPointerC2W = _SdhpdhE1t1TuLossOfPointerC2W_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 35, 2, 2, 1, 1, 22),
    _SdhpdhE1t1TuLossOfPointerC2W_Type()
)
sdhpdhE1t1TuLossOfPointerC2W.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdhpdhE1t1TuLossOfPointerC2W.setStatus("current")


class _SdhpdhE1t1FrameFormat_Type(Integer32):
    """Custom type sdhpdhE1t1FrameFormat based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("sf", 1),
          ("esf", 2))
    )


_SdhpdhE1t1FrameFormat_Type.__name__ = "Integer32"
_SdhpdhE1t1FrameFormat_Object = MibTableColumn
sdhpdhE1t1FrameFormat = _SdhpdhE1t1FrameFormat_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 35, 2, 2, 1, 1, 23),
    _SdhpdhE1t1FrameFormat_Type()
)
sdhpdhE1t1FrameFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdhpdhE1t1FrameFormat.setStatus("current")
_SdhpdhE1t1EquipmentIndex_Type = Unsigned32
_SdhpdhE1t1EquipmentIndex_Object = MibTableColumn
sdhpdhE1t1EquipmentIndex = _SdhpdhE1t1EquipmentIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 35, 2, 2, 1, 1, 24),
    _SdhpdhE1t1EquipmentIndex_Type()
)
sdhpdhE1t1EquipmentIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdhpdhE1t1EquipmentIndex.setStatus("current")


class _SdhpdhE1t1SignalLabel_Type(Integer32):
    """Custom type sdhpdhE1t1SignalLabel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("unequipped", 0),
          ("equippedNonspecific", 1),
          ("asynchronous", 2),
          ("bitSynchronous", 3),
          ("byteSynchronous", 4),
          ("reserved", 5),
          ("testSignal", 6),
          ("vcAis", 7))
    )


_SdhpdhE1t1SignalLabel_Type.__name__ = "Integer32"
_SdhpdhE1t1SignalLabel_Object = MibTableColumn
sdhpdhE1t1SignalLabel = _SdhpdhE1t1SignalLabel_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 35, 2, 2, 1, 1, 25),
    _SdhpdhE1t1SignalLabel_Type()
)
sdhpdhE1t1SignalLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdhpdhE1t1SignalLabel.setStatus("current")
_SdhpdhEquipmentList_ObjectIdentity = ObjectIdentity
sdhpdhEquipmentList = _SdhpdhEquipmentList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 35, 2, 3)
)
_SdhpdhEquipmentTable_Object = MibTable
sdhpdhEquipmentTable = _SdhpdhEquipmentTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 35, 2, 3, 1)
)
if mibBuilder.loadTexts:
    sdhpdhEquipmentTable.setStatus("current")
_SdhpdhEquipmentEntry_Object = MibTableRow
sdhpdhEquipmentEntry = _SdhpdhEquipmentEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 35, 2, 3, 1, 1)
)
sdhpdhEquipmentEntry.setIndexNames(
    (0, "LUM-SDHPDH-MIB", "sdhpdhEquipmentIndex"),
)
if mibBuilder.loadTexts:
    sdhpdhEquipmentEntry.setStatus("current")


class _SdhpdhEquipmentIndex_Type(Unsigned32):
    """Custom type sdhpdhEquipmentIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_SdhpdhEquipmentIndex_Type.__name__ = "Unsigned32"
_SdhpdhEquipmentIndex_Object = MibTableColumn
sdhpdhEquipmentIndex = _SdhpdhEquipmentIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 35, 2, 3, 1, 1, 1),
    _SdhpdhEquipmentIndex_Type()
)
sdhpdhEquipmentIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdhpdhEquipmentIndex.setStatus("current")
_SdhpdhEquipmentName_Type = MgmtNameString
_SdhpdhEquipmentName_Object = MibTableColumn
sdhpdhEquipmentName = _SdhpdhEquipmentName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 35, 2, 3, 1, 1, 2),
    _SdhpdhEquipmentName_Type()
)
sdhpdhEquipmentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdhpdhEquipmentName.setStatus("current")


class _SdhpdhEquipmentMultiplexingStructure_Type(Integer32):
    """Custom type sdhpdhEquipmentMultiplexingStructure based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("vc3", 1),
          ("vc4", 2))
    )


_SdhpdhEquipmentMultiplexingStructure_Type.__name__ = "Integer32"
_SdhpdhEquipmentMultiplexingStructure_Object = MibTableColumn
sdhpdhEquipmentMultiplexingStructure = _SdhpdhEquipmentMultiplexingStructure_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 35, 2, 3, 1, 1, 3),
    _SdhpdhEquipmentMultiplexingStructure_Type()
)
sdhpdhEquipmentMultiplexingStructure.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdhpdhEquipmentMultiplexingStructure.setStatus("current")
_SdhpdhEquipmentChangeMultiplexStructureCommand_Type = CommandString
_SdhpdhEquipmentChangeMultiplexStructureCommand_Object = MibTableColumn
sdhpdhEquipmentChangeMultiplexStructureCommand = _SdhpdhEquipmentChangeMultiplexStructureCommand_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 35, 2, 3, 1, 1, 4),
    _SdhpdhEquipmentChangeMultiplexStructureCommand_Type()
)
sdhpdhEquipmentChangeMultiplexStructureCommand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdhpdhEquipmentChangeMultiplexStructureCommand.setStatus("current")

# Managed Objects groups

sdhpdhGeneralGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 35, 1, 1, 1)
)
sdhpdhGeneralGroup.setObjects(
      *(("LUM-SDHPDH-MIB", "sdhpdhGeneralLastChangeTime"),
        ("LUM-SDHPDH-MIB", "sdhpdhGeneralStateLastChangeTime"),
        ("LUM-SDHPDH-MIB", "sdhpdhGeneralE1t1TableSize"),
        ("LUM-SDHPDH-MIB", "sdhpdhGeneralEquipmentTableSize"))
)
if mibBuilder.loadTexts:
    sdhpdhGeneralGroup.setStatus("current")

sdhpdhE1t1Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 35, 1, 1, 2)
)
sdhpdhE1t1Group.setObjects(
      *(("LUM-SDHPDH-MIB", "sdhpdhE1t1Index"),
        ("LUM-SDHPDH-MIB", "sdhpdhE1t1Name"),
        ("LUM-SDHPDH-MIB", "sdhpdhE1t1Descr"),
        ("LUM-SDHPDH-MIB", "sdhpdhE1t1AdminStatus"),
        ("LUM-SDHPDH-MIB", "sdhpdhE1t1OperStatus"),
        ("LUM-SDHPDH-MIB", "sdhpdhE1t1AlarmIndicationSignalW2C"),
        ("LUM-SDHPDH-MIB", "sdhpdhE1t1AlarmIndicationSignalC2W"),
        ("LUM-SDHPDH-MIB", "sdhpdhE1t1LossOfFrameC2W"),
        ("LUM-SDHPDH-MIB", "sdhpdhE1t1LossOfFrameW2C"),
        ("LUM-SDHPDH-MIB", "sdhpdhE1t1UnEquipped"),
        ("LUM-SDHPDH-MIB", "sdhpdhE1t1ConnectionStatus"),
        ("LUM-SDHPDH-MIB", "sdhpdhE1t1SubChannelId"),
        ("LUM-SDHPDH-MIB", "sdhpdhE1t1MultiplexingInformation"),
        ("LUM-SDHPDH-MIB", "sdhpdhE1t1RxSignalStatus"),
        ("LUM-SDHPDH-MIB", "sdhpdhE1t1TxSignalStatus"),
        ("LUM-SDHPDH-MIB", "sdhpdhE1t1VcIndex"),
        ("LUM-SDHPDH-MIB", "sdhpdhE1t1ClockDomain"),
        ("LUM-SDHPDH-MIB", "sdhpdhE1t1TuAlarmIndicationSignalC2W"),
        ("LUM-SDHPDH-MIB", "sdhpdhE1t1TuLossOfPointerC2W"),
        ("LUM-SDHPDH-MIB", "sdhpdhE1t1FrameFormat"))
)
if mibBuilder.loadTexts:
    sdhpdhE1t1Group.setStatus("deprecated")

sdhpdhEquipmentGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 35, 1, 1, 3)
)
sdhpdhEquipmentGroup.setObjects(
      *(("LUM-SDHPDH-MIB", "sdhpdhEquipmentIndex"),
        ("LUM-SDHPDH-MIB", "sdhpdhEquipmentName"),
        ("LUM-SDHPDH-MIB", "sdhpdhEquipmentMultiplexingStructure"),
        ("LUM-SDHPDH-MIB", "sdhpdhEquipmentChangeMultiplexStructureCommand"))
)
if mibBuilder.loadTexts:
    sdhpdhEquipmentGroup.setStatus("current")

sdhpdhE1t1GroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 35, 1, 1, 4)
)
sdhpdhE1t1GroupV2.setObjects(
      *(("LUM-SDHPDH-MIB", "sdhpdhE1t1Index"),
        ("LUM-SDHPDH-MIB", "sdhpdhE1t1Name"),
        ("LUM-SDHPDH-MIB", "sdhpdhE1t1Descr"),
        ("LUM-SDHPDH-MIB", "sdhpdhE1t1AdminStatus"),
        ("LUM-SDHPDH-MIB", "sdhpdhE1t1OperStatus"),
        ("LUM-SDHPDH-MIB", "sdhpdhE1t1AlarmIndicationSignalW2C"),
        ("LUM-SDHPDH-MIB", "sdhpdhE1t1AlarmIndicationSignalC2W"),
        ("LUM-SDHPDH-MIB", "sdhpdhE1t1LossOfFrameC2W"),
        ("LUM-SDHPDH-MIB", "sdhpdhE1t1LossOfFrameW2C"),
        ("LUM-SDHPDH-MIB", "sdhpdhE1t1UnEquipped"),
        ("LUM-SDHPDH-MIB", "sdhpdhE1t1ConnectionStatus"),
        ("LUM-SDHPDH-MIB", "sdhpdhE1t1SubChannelId"),
        ("LUM-SDHPDH-MIB", "sdhpdhE1t1MultiplexingInformation"),
        ("LUM-SDHPDH-MIB", "sdhpdhE1t1RxSignalStatus"),
        ("LUM-SDHPDH-MIB", "sdhpdhE1t1TxSignalStatus"),
        ("LUM-SDHPDH-MIB", "sdhpdhE1t1VcIndex"),
        ("LUM-SDHPDH-MIB", "sdhpdhE1t1ClockDomain"),
        ("LUM-SDHPDH-MIB", "sdhpdhE1t1TuAlarmIndicationSignalC2W"),
        ("LUM-SDHPDH-MIB", "sdhpdhE1t1TuLossOfPointerC2W"),
        ("LUM-SDHPDH-MIB", "sdhpdhE1t1FrameFormat"),
        ("LUM-SDHPDH-MIB", "sdhpdhE1t1EquipmentIndex"),
        ("LUM-SDHPDH-MIB", "sdhpdhE1t1SignalLabel"))
)
if mibBuilder.loadTexts:
    sdhpdhE1t1GroupV2.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

lumSdhpdhBasicCompl1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 35, 1, 2, 1)
)
lumSdhpdhBasicCompl1.setObjects(
      *(("LUM-SDHPDH-MIB", "sdhpdhGeneralGroup"),
        ("LUM-SDHPDH-MIB", "sdhpdhE1t1Group"),
        ("LUM-SDHPDH-MIB", "sdhpdhEquipmentGroup"))
)
if mibBuilder.loadTexts:
    lumSdhpdhBasicCompl1.setStatus(
        "deprecated"
    )

lumSdhpdhBasicCompl2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 35, 1, 2, 2)
)
lumSdhpdhBasicCompl2.setObjects(
      *(("LUM-SDHPDH-MIB", "sdhpdhGeneralGroup"),
        ("LUM-SDHPDH-MIB", "sdhpdhE1t1GroupV2"),
        ("LUM-SDHPDH-MIB", "sdhpdhEquipmentGroup"))
)
if mibBuilder.loadTexts:
    lumSdhpdhBasicCompl2.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LUM-SDHPDH-MIB",
    **{"lumSdhpdhMIBModule": lumSdhpdhMIBModule,
       "lumSdhpdhConfs": lumSdhpdhConfs,
       "lumSdhpdhGroups": lumSdhpdhGroups,
       "sdhpdhGeneralGroup": sdhpdhGeneralGroup,
       "sdhpdhE1t1Group": sdhpdhE1t1Group,
       "sdhpdhEquipmentGroup": sdhpdhEquipmentGroup,
       "sdhpdhE1t1GroupV2": sdhpdhE1t1GroupV2,
       "lumSdhpdhCompl": lumSdhpdhCompl,
       "lumSdhpdhBasicCompl1": lumSdhpdhBasicCompl1,
       "lumSdhpdhBasicCompl2": lumSdhpdhBasicCompl2,
       "lumSdhpdhMIBObjects": lumSdhpdhMIBObjects,
       "sdhpdhGeneral": sdhpdhGeneral,
       "sdhpdhGeneralLastChangeTime": sdhpdhGeneralLastChangeTime,
       "sdhpdhGeneralStateLastChangeTime": sdhpdhGeneralStateLastChangeTime,
       "sdhpdhGeneralE1t1TableSize": sdhpdhGeneralE1t1TableSize,
       "sdhpdhGeneralEquipmentTableSize": sdhpdhGeneralEquipmentTableSize,
       "sdhpdhE1t1List": sdhpdhE1t1List,
       "sdhpdhE1t1Table": sdhpdhE1t1Table,
       "sdhpdhE1t1Entry": sdhpdhE1t1Entry,
       "sdhpdhE1t1Index": sdhpdhE1t1Index,
       "sdhpdhE1t1Name": sdhpdhE1t1Name,
       "sdhpdhE1t1Descr": sdhpdhE1t1Descr,
       "sdhpdhE1t1AdminStatus": sdhpdhE1t1AdminStatus,
       "sdhpdhE1t1OperStatus": sdhpdhE1t1OperStatus,
       "sdhpdhE1t1AlarmIndicationSignalW2C": sdhpdhE1t1AlarmIndicationSignalW2C,
       "sdhpdhE1t1AlarmIndicationSignalC2W": sdhpdhE1t1AlarmIndicationSignalC2W,
       "sdhpdhE1t1LossOfFrameC2W": sdhpdhE1t1LossOfFrameC2W,
       "sdhpdhE1t1LossOfFrameW2C": sdhpdhE1t1LossOfFrameW2C,
       "sdhpdhE1t1UnEquipped": sdhpdhE1t1UnEquipped,
       "sdhpdhE1t1ConnectionStatus": sdhpdhE1t1ConnectionStatus,
       "sdhpdhE1t1SubChannelId": sdhpdhE1t1SubChannelId,
       "sdhpdhE1t1MultiplexingInformation": sdhpdhE1t1MultiplexingInformation,
       "sdhpdhE1t1RxSignalStatus": sdhpdhE1t1RxSignalStatus,
       "sdhpdhE1t1TxSignalStatus": sdhpdhE1t1TxSignalStatus,
       "sdhpdhE1t1VcIndex": sdhpdhE1t1VcIndex,
       "sdhpdhE1t1ClockDomain": sdhpdhE1t1ClockDomain,
       "sdhpdhE1t1TuAlarmIndicationSignalC2W": sdhpdhE1t1TuAlarmIndicationSignalC2W,
       "sdhpdhE1t1TuLossOfPointerC2W": sdhpdhE1t1TuLossOfPointerC2W,
       "sdhpdhE1t1FrameFormat": sdhpdhE1t1FrameFormat,
       "sdhpdhE1t1EquipmentIndex": sdhpdhE1t1EquipmentIndex,
       "sdhpdhE1t1SignalLabel": sdhpdhE1t1SignalLabel,
       "sdhpdhEquipmentList": sdhpdhEquipmentList,
       "sdhpdhEquipmentTable": sdhpdhEquipmentTable,
       "sdhpdhEquipmentEntry": sdhpdhEquipmentEntry,
       "sdhpdhEquipmentIndex": sdhpdhEquipmentIndex,
       "sdhpdhEquipmentName": sdhpdhEquipmentName,
       "sdhpdhEquipmentMultiplexingStructure": sdhpdhEquipmentMultiplexingStructure,
       "sdhpdhEquipmentChangeMultiplexStructureCommand": sdhpdhEquipmentChangeMultiplexStructureCommand}
)
