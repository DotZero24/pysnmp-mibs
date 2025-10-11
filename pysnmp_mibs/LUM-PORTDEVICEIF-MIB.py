# SNMP MIB module (LUM-PORTDEVICEIF-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/LUM-PORTDEVICEIF-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:14:47 2025
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

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(lumModules,
 lumPortdeviceIfMIB) = mibBuilder.importSymbols(
    "LUM-REG",
    "lumModules",
    "lumPortdeviceIfMIB")

(AdminStatus,
 BoardOrInterfaceOperStatus,
 FaultStatus,
 LambdaFrequency,
 MgmtNameString,
 OnOff,
 SlotNumber,
 SubrackNumber,
 TrxMedia) = mibBuilder.importSymbols(
    "LUM-TC",
    "AdminStatus",
    "BoardOrInterfaceOperStatus",
    "FaultStatus",
    "LambdaFrequency",
    "MgmtNameString",
    "OnOff",
    "SlotNumber",
    "SubrackNumber",
    "TrxMedia")

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

lumPortdeviceIfMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 1, 1, 58)
)
if mibBuilder.loadTexts:
    lumPortdeviceIfMIBModule.setRevisions(
        ("2017-06-15 00:00",
         "2013-05-31 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class LumPortDeviceDuplexMode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("halfDuplex", 0),
          ("fullDuplex", 1),
          ("autoDuplex", 2),
          ("incomplete", 3),
          ("duplexNotAvailable", 254),
          ("duplexNotApplicable", 255))
    )



class LumPortDeviceInterfaceSpeed(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("fastEthernet", 0),
          ("gbE", 1))
    )



class LumPortDeviceMasterSlaveRole(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("msMaster", 0),
          ("msSlave", 1),
          ("msAuto", 2),
          ("msNotAvailable", 254),
          ("msNotApplicable", 255))
    )



class LumPortDeviceMdixMode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("mdi", 0),
          ("mdix", 1),
          ("mdiNotAvailable", 254),
          ("mdiNotApplicable", 255))
    )



class LumPortDevicePauseMode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("pauseDisabled", 0),
          ("pauseEnabled", 1),
          ("pauseTxEnabledRxDisabled", 2),
          ("pauseTxDisabledRxEnabled", 3),
          ("pauseAuto", 4),
          ("pauseNotAvailable", 254),
          ("pauseNotApplicable", 255))
    )



class LumPortDeviceInterface(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("interfaceNone", 0),
          ("ifNif", 1),
          ("ifCifA", 2),
          ("ifCifB", 3))
    )



# MIB Managed Objects in the order of their OIDs

_LumPortdeviceIfConfs_ObjectIdentity = ObjectIdentity
lumPortdeviceIfConfs = _LumPortdeviceIfConfs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 58, 1)
)
_LumPortdeviceIfGroups_ObjectIdentity = ObjectIdentity
lumPortdeviceIfGroups = _LumPortdeviceIfGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 58, 1, 1)
)
_LumPortdeviceIfCompl_ObjectIdentity = ObjectIdentity
lumPortdeviceIfCompl = _LumPortdeviceIfCompl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 58, 1, 2)
)
_LumPortdeviceIfMIBObjects_ObjectIdentity = ObjectIdentity
lumPortdeviceIfMIBObjects = _LumPortdeviceIfMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 58, 2)
)
_PortDevIfGeneral_ObjectIdentity = ObjectIdentity
portDevIfGeneral = _PortDevIfGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 58, 2, 1)
)
_PortDevIfGeneralLastChangeTime_Type = DateAndTime
_PortDevIfGeneralLastChangeTime_Object = MibScalar
portDevIfGeneralLastChangeTime = _PortDevIfGeneralLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 58, 2, 1, 1),
    _PortDevIfGeneralLastChangeTime_Type()
)
portDevIfGeneralLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portDevIfGeneralLastChangeTime.setStatus("current")
_PortDevIfGeneralStateLastChangeTime_Type = DateAndTime
_PortDevIfGeneralStateLastChangeTime_Object = MibScalar
portDevIfGeneralStateLastChangeTime = _PortDevIfGeneralStateLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 58, 2, 1, 2),
    _PortDevIfGeneralStateLastChangeTime_Type()
)
portDevIfGeneralStateLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portDevIfGeneralStateLastChangeTime.setStatus("current")
_PortDevIfL1TableSize_Type = Unsigned32
_PortDevIfL1TableSize_Object = MibScalar
portDevIfL1TableSize = _PortDevIfL1TableSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 58, 2, 1, 3),
    _PortDevIfL1TableSize_Type()
)
portDevIfL1TableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portDevIfL1TableSize.setStatus("current")
_PortDevIfL2TableSize_Type = Unsigned32
_PortDevIfL2TableSize_Object = MibScalar
portDevIfL2TableSize = _PortDevIfL2TableSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 58, 2, 1, 4),
    _PortDevIfL2TableSize_Type()
)
portDevIfL2TableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portDevIfL2TableSize.setStatus("current")
_PortDevIfL1List_ObjectIdentity = ObjectIdentity
portDevIfL1List = _PortDevIfL1List_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 58, 2, 2)
)
_PortDevIfL1Table_Object = MibTable
portDevIfL1Table = _PortDevIfL1Table_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 58, 2, 2, 1)
)
if mibBuilder.loadTexts:
    portDevIfL1Table.setStatus("current")
_PortDevIfL1Entry_Object = MibTableRow
portDevIfL1Entry = _PortDevIfL1Entry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 58, 2, 2, 1, 1)
)
portDevIfL1Entry.setIndexNames(
    (0, "LUM-PORTDEVICEIF-MIB", "portDevIfIndex"),
)
if mibBuilder.loadTexts:
    portDevIfL1Entry.setStatus("current")
_PortDevIfIndex_Type = InterfaceIndex
_PortDevIfIndex_Object = MibTableColumn
portDevIfIndex = _PortDevIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 58, 2, 2, 1, 1, 1),
    _PortDevIfIndex_Type()
)
portDevIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portDevIfIndex.setStatus("current")
_PortDevIfL1Name_Type = MgmtNameString
_PortDevIfL1Name_Object = MibTableColumn
portDevIfL1Name = _PortDevIfL1Name_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 58, 2, 2, 1, 1, 2),
    _PortDevIfL1Name_Type()
)
portDevIfL1Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portDevIfL1Name.setStatus("current")


class _PortDevIfL1Descr_Type(DisplayString):
    """Custom type portDevIfL1Descr based on DisplayString"""
    defaultValue = OctetString("")


_PortDevIfL1Descr_Type.__name__ = "DisplayString"
_PortDevIfL1Descr_Object = MibTableColumn
portDevIfL1Descr = _PortDevIfL1Descr_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 58, 2, 2, 1, 1, 3),
    _PortDevIfL1Descr_Type()
)
portDevIfL1Descr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portDevIfL1Descr.setStatus("current")


class _PortDevIfL1AdminStatus_Type(AdminStatus):
    """Custom type portDevIfL1AdminStatus based on AdminStatus"""
    defaultValue = 2


_PortDevIfL1AdminStatus_Type.__name__ = "AdminStatus"
_PortDevIfL1AdminStatus_Object = MibTableColumn
portDevIfL1AdminStatus = _PortDevIfL1AdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 58, 2, 2, 1, 1, 4),
    _PortDevIfL1AdminStatus_Type()
)
portDevIfL1AdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portDevIfL1AdminStatus.setStatus("current")


class _PortDevIfL1OperStatus_Type(BoardOrInterfaceOperStatus):
    """Custom type portDevIfL1OperStatus based on BoardOrInterfaceOperStatus"""
    defaultValue = 3


_PortDevIfL1OperStatus_Type.__name__ = "BoardOrInterfaceOperStatus"
_PortDevIfL1OperStatus_Object = MibTableColumn
portDevIfL1OperStatus = _PortDevIfL1OperStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 58, 2, 2, 1, 1, 5),
    _PortDevIfL1OperStatus_Type()
)
portDevIfL1OperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portDevIfL1OperStatus.setStatus("current")


class _PortDevIfL1PortDevId_Type(Unsigned32):
    """Custom type portDevIfL1PortDevId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PortDevIfL1PortDevId_Type.__name__ = "Unsigned32"
_PortDevIfL1PortDevId_Object = MibTableColumn
portDevIfL1PortDevId = _PortDevIfL1PortDevId_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 58, 2, 2, 1, 1, 6),
    _PortDevIfL1PortDevId_Type()
)
portDevIfL1PortDevId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    portDevIfL1PortDevId.setStatus("current")
_PortDevIfL1Subrack_Type = SubrackNumber
_PortDevIfL1Subrack_Object = MibTableColumn
portDevIfL1Subrack = _PortDevIfL1Subrack_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 58, 2, 2, 1, 1, 7),
    _PortDevIfL1Subrack_Type()
)
portDevIfL1Subrack.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    portDevIfL1Subrack.setStatus("current")
_PortDevIfL1Slot_Type = SlotNumber
_PortDevIfL1Slot_Object = MibTableColumn
portDevIfL1Slot = _PortDevIfL1Slot_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 58, 2, 2, 1, 1, 8),
    _PortDevIfL1Slot_Type()
)
portDevIfL1Slot.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    portDevIfL1Slot.setStatus("current")


class _PortDevIfL1LocalPort_Type(Unsigned32):
    """Custom type portDevIfL1LocalPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_PortDevIfL1LocalPort_Type.__name__ = "Unsigned32"
_PortDevIfL1LocalPort_Object = MibTableColumn
portDevIfL1LocalPort = _PortDevIfL1LocalPort_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 58, 2, 2, 1, 1, 9),
    _PortDevIfL1LocalPort_Type()
)
portDevIfL1LocalPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    portDevIfL1LocalPort.setStatus("current")


class _PortDevIfL1VlanId_Type(Unsigned32):
    """Custom type portDevIfL1VlanId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_PortDevIfL1VlanId_Type.__name__ = "Unsigned32"
_PortDevIfL1VlanId_Object = MibTableColumn
portDevIfL1VlanId = _PortDevIfL1VlanId_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 58, 2, 2, 1, 1, 10),
    _PortDevIfL1VlanId_Type()
)
portDevIfL1VlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    portDevIfL1VlanId.setStatus("current")
_PortDevIfL1NidPort_Type = LumPortDeviceInterface
_PortDevIfL1NidPort_Object = MibTableColumn
portDevIfL1NidPort = _PortDevIfL1NidPort_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 58, 2, 2, 1, 1, 11),
    _PortDevIfL1NidPort_Type()
)
portDevIfL1NidPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    portDevIfL1NidPort.setStatus("current")


class _PortDevIfL1InternalReference_Type(Unsigned32):
    """Custom type portDevIfL1InternalReference based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_PortDevIfL1InternalReference_Type.__name__ = "Unsigned32"
_PortDevIfL1InternalReference_Object = MibTableColumn
portDevIfL1InternalReference = _PortDevIfL1InternalReference_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 58, 2, 2, 1, 1, 12),
    _PortDevIfL1InternalReference_Type()
)
portDevIfL1InternalReference.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    portDevIfL1InternalReference.setStatus("current")


class _PortDevIfL1LaserStatus_Type(Integer32):
    """Custom type portDevIfL1LaserStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_PortDevIfL1LaserStatus_Type.__name__ = "Integer32"
_PortDevIfL1LaserStatus_Object = MibTableColumn
portDevIfL1LaserStatus = _PortDevIfL1LaserStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 58, 2, 2, 1, 1, 13),
    _PortDevIfL1LaserStatus_Type()
)
portDevIfL1LaserStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portDevIfL1LaserStatus.setStatus("current")
_PortDevIfL1LaserBias_Type = Unsigned32
_PortDevIfL1LaserBias_Object = MibTableColumn
portDevIfL1LaserBias = _PortDevIfL1LaserBias_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 58, 2, 2, 1, 1, 14),
    _PortDevIfL1LaserBias_Type()
)
portDevIfL1LaserBias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portDevIfL1LaserBias.setStatus("current")
_PortDevIfL1LaserTempActual_Type = Integer32
_PortDevIfL1LaserTempActual_Object = MibTableColumn
portDevIfL1LaserTempActual = _PortDevIfL1LaserTempActual_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 58, 2, 2, 1, 1, 15),
    _PortDevIfL1LaserTempActual_Type()
)
portDevIfL1LaserTempActual.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portDevIfL1LaserTempActual.setStatus("current")
_PortDevIfL1TxFrequency_Type = LambdaFrequency
_PortDevIfL1TxFrequency_Object = MibTableColumn
portDevIfL1TxFrequency = _PortDevIfL1TxFrequency_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 58, 2, 2, 1, 1, 16),
    _PortDevIfL1TxFrequency_Type()
)
portDevIfL1TxFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portDevIfL1TxFrequency.setStatus("current")


class _PortDevIfL1ExpectedTxFrequency_Type(LambdaFrequency):
    """Custom type portDevIfL1ExpectedTxFrequency based on LambdaFrequency"""
    defaultValue = 0


_PortDevIfL1ExpectedTxFrequency_Type.__name__ = "LambdaFrequency"
_PortDevIfL1ExpectedTxFrequency_Object = MibTableColumn
portDevIfL1ExpectedTxFrequency = _PortDevIfL1ExpectedTxFrequency_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 58, 2, 2, 1, 1, 17),
    _PortDevIfL1ExpectedTxFrequency_Type()
)
portDevIfL1ExpectedTxFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portDevIfL1ExpectedTxFrequency.setStatus("current")


class _PortDevIfL1SignalFormat_Type(LumPortDeviceInterfaceSpeed):
    """Custom type portDevIfL1SignalFormat based on LumPortDeviceInterfaceSpeed"""
    defaultValue = 1


_PortDevIfL1SignalFormat_Type.__name__ = "LumPortDeviceInterfaceSpeed"
_PortDevIfL1SignalFormat_Object = MibTableColumn
portDevIfL1SignalFormat = _PortDevIfL1SignalFormat_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 58, 2, 2, 1, 1, 18),
    _PortDevIfL1SignalFormat_Type()
)
portDevIfL1SignalFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portDevIfL1SignalFormat.setStatus("current")


class _PortDevIfL1TrxMedia_Type(TrxMedia):
    """Custom type portDevIfL1TrxMedia based on TrxMedia"""
    defaultValue = 1


_PortDevIfL1TrxMedia_Type.__name__ = "TrxMedia"
_PortDevIfL1TrxMedia_Object = MibTableColumn
portDevIfL1TrxMedia = _PortDevIfL1TrxMedia_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 58, 2, 2, 1, 1, 19),
    _PortDevIfL1TrxMedia_Type()
)
portDevIfL1TrxMedia.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    portDevIfL1TrxMedia.setStatus("current")
_PortDevIfL1ReceiverSensitivity_Type = Integer32
_PortDevIfL1ReceiverSensitivity_Object = MibTableColumn
portDevIfL1ReceiverSensitivity = _PortDevIfL1ReceiverSensitivity_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 58, 2, 2, 1, 1, 20),
    _PortDevIfL1ReceiverSensitivity_Type()
)
portDevIfL1ReceiverSensitivity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portDevIfL1ReceiverSensitivity.setStatus("current")
_PortDevIfL1PowerLevel_Type = Integer32
_PortDevIfL1PowerLevel_Object = MibTableColumn
portDevIfL1PowerLevel = _PortDevIfL1PowerLevel_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 58, 2, 2, 1, 1, 21),
    _PortDevIfL1PowerLevel_Type()
)
portDevIfL1PowerLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portDevIfL1PowerLevel.setStatus("current")


class _PortDevIfL1PowerLevelLowRelativeThreshold_Type(Integer32):
    """Custom type portDevIfL1PowerLevelLowRelativeThreshold based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-50, 100),
    )


_PortDevIfL1PowerLevelLowRelativeThreshold_Type.__name__ = "Integer32"
_PortDevIfL1PowerLevelLowRelativeThreshold_Object = MibTableColumn
portDevIfL1PowerLevelLowRelativeThreshold = _PortDevIfL1PowerLevelLowRelativeThreshold_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 58, 2, 2, 1, 1, 22),
    _PortDevIfL1PowerLevelLowRelativeThreshold_Type()
)
portDevIfL1PowerLevelLowRelativeThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portDevIfL1PowerLevelLowRelativeThreshold.setStatus("current")
_PortDevIfL1TxPowerLevel_Type = Integer32
_PortDevIfL1TxPowerLevel_Object = MibTableColumn
portDevIfL1TxPowerLevel = _PortDevIfL1TxPowerLevel_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 58, 2, 2, 1, 1, 23),
    _PortDevIfL1TxPowerLevel_Type()
)
portDevIfL1TxPowerLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portDevIfL1TxPowerLevel.setStatus("current")
_PortDevIfL1RxHighPower_Type = Integer32
_PortDevIfL1RxHighPower_Object = MibTableColumn
portDevIfL1RxHighPower = _PortDevIfL1RxHighPower_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 58, 2, 2, 1, 1, 24),
    _PortDevIfL1RxHighPower_Type()
)
portDevIfL1RxHighPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portDevIfL1RxHighPower.setStatus("current")


class _PortDevIfL1TrxClass_Type(DisplayString):
    """Custom type portDevIfL1TrxClass based on DisplayString"""
    defaultValue = OctetString("")


_PortDevIfL1TrxClass_Type.__name__ = "DisplayString"
_PortDevIfL1TrxClass_Object = MibTableColumn
portDevIfL1TrxClass = _PortDevIfL1TrxClass_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 58, 2, 2, 1, 1, 25),
    _PortDevIfL1TrxClass_Type()
)
portDevIfL1TrxClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portDevIfL1TrxClass.setStatus("current")
_PortDevIfL1LossOfSignal_Type = FaultStatus
_PortDevIfL1LossOfSignal_Object = MibTableColumn
portDevIfL1LossOfSignal = _PortDevIfL1LossOfSignal_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 58, 2, 2, 1, 1, 26),
    _PortDevIfL1LossOfSignal_Type()
)
portDevIfL1LossOfSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portDevIfL1LossOfSignal.setStatus("current")
_PortDevIfL1TrxMissing_Type = FaultStatus
_PortDevIfL1TrxMissing_Object = MibTableColumn
portDevIfL1TrxMissing = _PortDevIfL1TrxMissing_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 58, 2, 2, 1, 1, 27),
    _PortDevIfL1TrxMissing_Type()
)
portDevIfL1TrxMissing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portDevIfL1TrxMissing.setStatus("current")
_PortDevIfL1ReceivedPowerLow_Type = FaultStatus
_PortDevIfL1ReceivedPowerLow_Object = MibTableColumn
portDevIfL1ReceivedPowerLow = _PortDevIfL1ReceivedPowerLow_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 58, 2, 2, 1, 1, 28),
    _PortDevIfL1ReceivedPowerLow_Type()
)
portDevIfL1ReceivedPowerLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portDevIfL1ReceivedPowerLow.setStatus("current")
_PortDevIfL1ReceivedPowerHigh_Type = FaultStatus
_PortDevIfL1ReceivedPowerHigh_Object = MibTableColumn
portDevIfL1ReceivedPowerHigh = _PortDevIfL1ReceivedPowerHigh_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 58, 2, 2, 1, 1, 29),
    _PortDevIfL1ReceivedPowerHigh_Type()
)
portDevIfL1ReceivedPowerHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portDevIfL1ReceivedPowerHigh.setStatus("current")
_PortDevIfL2List_ObjectIdentity = ObjectIdentity
portDevIfL2List = _PortDevIfL2List_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 58, 2, 3)
)
_PortDevIfL2Table_Object = MibTable
portDevIfL2Table = _PortDevIfL2Table_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 58, 2, 3, 1)
)
if mibBuilder.loadTexts:
    portDevIfL2Table.setStatus("current")
_PortDevIfL2Entry_Object = MibTableRow
portDevIfL2Entry = _PortDevIfL2Entry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 58, 2, 3, 1, 1)
)
portDevIfL2Entry.setIndexNames(
    (0, "LUM-PORTDEVICEIF-MIB", "portDevIfL2Index"),
)
if mibBuilder.loadTexts:
    portDevIfL2Entry.setStatus("current")
_PortDevIfL2Index_Type = InterfaceIndex
_PortDevIfL2Index_Object = MibTableColumn
portDevIfL2Index = _PortDevIfL2Index_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 58, 2, 3, 1, 1, 1),
    _PortDevIfL2Index_Type()
)
portDevIfL2Index.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    portDevIfL2Index.setStatus("current")
_PortDevIfL2Name_Type = MgmtNameString
_PortDevIfL2Name_Object = MibTableColumn
portDevIfL2Name = _PortDevIfL2Name_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 58, 2, 3, 1, 1, 2),
    _PortDevIfL2Name_Type()
)
portDevIfL2Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portDevIfL2Name.setStatus("current")


class _PortDevIfL2Descr_Type(DisplayString):
    """Custom type portDevIfL2Descr based on DisplayString"""
    defaultValue = OctetString("")


_PortDevIfL2Descr_Type.__name__ = "DisplayString"
_PortDevIfL2Descr_Object = MibTableColumn
portDevIfL2Descr = _PortDevIfL2Descr_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 58, 2, 3, 1, 1, 3),
    _PortDevIfL2Descr_Type()
)
portDevIfL2Descr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portDevIfL2Descr.setStatus("current")


class _PortDevIfL2PortDevId_Type(Unsigned32):
    """Custom type portDevIfL2PortDevId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PortDevIfL2PortDevId_Type.__name__ = "Unsigned32"
_PortDevIfL2PortDevId_Object = MibTableColumn
portDevIfL2PortDevId = _PortDevIfL2PortDevId_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 58, 2, 3, 1, 1, 4),
    _PortDevIfL2PortDevId_Type()
)
portDevIfL2PortDevId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    portDevIfL2PortDevId.setStatus("current")
_PortDevIfL2Subrack_Type = SubrackNumber
_PortDevIfL2Subrack_Object = MibTableColumn
portDevIfL2Subrack = _PortDevIfL2Subrack_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 58, 2, 3, 1, 1, 5),
    _PortDevIfL2Subrack_Type()
)
portDevIfL2Subrack.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    portDevIfL2Subrack.setStatus("current")
_PortDevIfL2Slot_Type = SlotNumber
_PortDevIfL2Slot_Object = MibTableColumn
portDevIfL2Slot = _PortDevIfL2Slot_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 58, 2, 3, 1, 1, 6),
    _PortDevIfL2Slot_Type()
)
portDevIfL2Slot.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    portDevIfL2Slot.setStatus("current")


class _PortDevIfL2LocalPort_Type(Unsigned32):
    """Custom type portDevIfL2LocalPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_PortDevIfL2LocalPort_Type.__name__ = "Unsigned32"
_PortDevIfL2LocalPort_Object = MibTableColumn
portDevIfL2LocalPort = _PortDevIfL2LocalPort_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 58, 2, 3, 1, 1, 7),
    _PortDevIfL2LocalPort_Type()
)
portDevIfL2LocalPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    portDevIfL2LocalPort.setStatus("current")


class _PortDevIfL2VlanId_Type(Unsigned32):
    """Custom type portDevIfL2VlanId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_PortDevIfL2VlanId_Type.__name__ = "Unsigned32"
_PortDevIfL2VlanId_Object = MibTableColumn
portDevIfL2VlanId = _PortDevIfL2VlanId_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 58, 2, 3, 1, 1, 8),
    _PortDevIfL2VlanId_Type()
)
portDevIfL2VlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    portDevIfL2VlanId.setStatus("current")
_PortDevIfL2NidPort_Type = LumPortDeviceInterface
_PortDevIfL2NidPort_Object = MibTableColumn
portDevIfL2NidPort = _PortDevIfL2NidPort_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 58, 2, 3, 1, 1, 9),
    _PortDevIfL2NidPort_Type()
)
portDevIfL2NidPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    portDevIfL2NidPort.setStatus("current")


class _PortDevIfL2InternalReference_Type(Unsigned32):
    """Custom type portDevIfL2InternalReference based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_PortDevIfL2InternalReference_Type.__name__ = "Unsigned32"
_PortDevIfL2InternalReference_Object = MibTableColumn
portDevIfL2InternalReference = _PortDevIfL2InternalReference_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 58, 2, 3, 1, 1, 10),
    _PortDevIfL2InternalReference_Type()
)
portDevIfL2InternalReference.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    portDevIfL2InternalReference.setStatus("current")


class _PortDevIfL2AutoNegotiation_Type(OnOff):
    """Custom type portDevIfL2AutoNegotiation based on OnOff"""
    defaultValue = 2


_PortDevIfL2AutoNegotiation_Type.__name__ = "OnOff"
_PortDevIfL2AutoNegotiation_Object = MibTableColumn
portDevIfL2AutoNegotiation = _PortDevIfL2AutoNegotiation_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 58, 2, 3, 1, 1, 11),
    _PortDevIfL2AutoNegotiation_Type()
)
portDevIfL2AutoNegotiation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portDevIfL2AutoNegotiation.setStatus("current")


class _PortDevIfL2AutoNegotiationStatus_Type(LumPortDeviceDuplexMode):
    """Custom type portDevIfL2AutoNegotiationStatus based on LumPortDeviceDuplexMode"""
    defaultValue = 3


_PortDevIfL2AutoNegotiationStatus_Type.__name__ = "LumPortDeviceDuplexMode"
_PortDevIfL2AutoNegotiationStatus_Object = MibTableColumn
portDevIfL2AutoNegotiationStatus = _PortDevIfL2AutoNegotiationStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 58, 2, 3, 1, 1, 12),
    _PortDevIfL2AutoNegotiationStatus_Type()
)
portDevIfL2AutoNegotiationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portDevIfL2AutoNegotiationStatus.setStatus("current")

# Managed Objects groups

portDevIfGeneralGroupV1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 58, 1, 1, 1)
)
portDevIfGeneralGroupV1.setObjects(
      *(("LUM-PORTDEVICEIF-MIB", "portDevIfGeneralLastChangeTime"),
        ("LUM-PORTDEVICEIF-MIB", "portDevIfGeneralStateLastChangeTime"),
        ("LUM-PORTDEVICEIF-MIB", "portDevIfL1TableSize"),
        ("LUM-PORTDEVICEIF-MIB", "portDevIfL2TableSize"))
)
if mibBuilder.loadTexts:
    portDevIfGeneralGroupV1.setStatus("current")

portDevIfL1GroupV1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 58, 1, 1, 2)
)
portDevIfL1GroupV1.setObjects(
      *(("LUM-PORTDEVICEIF-MIB", "portDevIfIndex"),
        ("LUM-PORTDEVICEIF-MIB", "portDevIfL1Name"),
        ("LUM-PORTDEVICEIF-MIB", "portDevIfL1Descr"),
        ("LUM-PORTDEVICEIF-MIB", "portDevIfL1AdminStatus"),
        ("LUM-PORTDEVICEIF-MIB", "portDevIfL1OperStatus"),
        ("LUM-PORTDEVICEIF-MIB", "portDevIfL1PortDevId"),
        ("LUM-PORTDEVICEIF-MIB", "portDevIfL1Subrack"),
        ("LUM-PORTDEVICEIF-MIB", "portDevIfL1Slot"),
        ("LUM-PORTDEVICEIF-MIB", "portDevIfL1LocalPort"),
        ("LUM-PORTDEVICEIF-MIB", "portDevIfL1VlanId"),
        ("LUM-PORTDEVICEIF-MIB", "portDevIfL1NidPort"),
        ("LUM-PORTDEVICEIF-MIB", "portDevIfL1InternalReference"),
        ("LUM-PORTDEVICEIF-MIB", "portDevIfL1LaserStatus"),
        ("LUM-PORTDEVICEIF-MIB", "portDevIfL1LaserBias"),
        ("LUM-PORTDEVICEIF-MIB", "portDevIfL1LaserTempActual"),
        ("LUM-PORTDEVICEIF-MIB", "portDevIfL1TxFrequency"),
        ("LUM-PORTDEVICEIF-MIB", "portDevIfL1ExpectedTxFrequency"),
        ("LUM-PORTDEVICEIF-MIB", "portDevIfL1SignalFormat"),
        ("LUM-PORTDEVICEIF-MIB", "portDevIfL1TrxMedia"),
        ("LUM-PORTDEVICEIF-MIB", "portDevIfL1ReceiverSensitivity"),
        ("LUM-PORTDEVICEIF-MIB", "portDevIfL1PowerLevel"),
        ("LUM-PORTDEVICEIF-MIB", "portDevIfL1PowerLevelLowRelativeThreshold"),
        ("LUM-PORTDEVICEIF-MIB", "portDevIfL1TxPowerLevel"),
        ("LUM-PORTDEVICEIF-MIB", "portDevIfL1RxHighPower"),
        ("LUM-PORTDEVICEIF-MIB", "portDevIfL1TrxClass"),
        ("LUM-PORTDEVICEIF-MIB", "portDevIfL1LossOfSignal"),
        ("LUM-PORTDEVICEIF-MIB", "portDevIfL1TrxMissing"),
        ("LUM-PORTDEVICEIF-MIB", "portDevIfL1ReceivedPowerLow"),
        ("LUM-PORTDEVICEIF-MIB", "portDevIfL1ReceivedPowerHigh"))
)
if mibBuilder.loadTexts:
    portDevIfL1GroupV1.setStatus("current")

portDevIfL2GroupV1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 58, 1, 1, 3)
)
portDevIfL2GroupV1.setObjects(
      *(("LUM-PORTDEVICEIF-MIB", "portDevIfL2Index"),
        ("LUM-PORTDEVICEIF-MIB", "portDevIfL2Name"),
        ("LUM-PORTDEVICEIF-MIB", "portDevIfL2Descr"),
        ("LUM-PORTDEVICEIF-MIB", "portDevIfL2PortDevId"),
        ("LUM-PORTDEVICEIF-MIB", "portDevIfL2Subrack"),
        ("LUM-PORTDEVICEIF-MIB", "portDevIfL2Slot"),
        ("LUM-PORTDEVICEIF-MIB", "portDevIfL2LocalPort"),
        ("LUM-PORTDEVICEIF-MIB", "portDevIfL2VlanId"),
        ("LUM-PORTDEVICEIF-MIB", "portDevIfL2NidPort"),
        ("LUM-PORTDEVICEIF-MIB", "portDevIfL2InternalReference"),
        ("LUM-PORTDEVICEIF-MIB", "portDevIfL2AutoNegotiation"),
        ("LUM-PORTDEVICEIF-MIB", "portDevIfL2AutoNegotiationStatus"))
)
if mibBuilder.loadTexts:
    portDevIfL2GroupV1.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

lumPortDeviceBasicComplV1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 58, 1, 2, 1)
)
lumPortDeviceBasicComplV1.setObjects(
      *(("LUM-PORTDEVICEIF-MIB", "portDevIfGeneralGroupV1"),
        ("LUM-PORTDEVICEIF-MIB", "portDevIfL1GroupV1"),
        ("LUM-PORTDEVICEIF-MIB", "portDevIfL2GroupV1"))
)
if mibBuilder.loadTexts:
    lumPortDeviceBasicComplV1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LUM-PORTDEVICEIF-MIB",
    **{"LumPortDeviceDuplexMode": LumPortDeviceDuplexMode,
       "LumPortDeviceInterfaceSpeed": LumPortDeviceInterfaceSpeed,
       "LumPortDeviceMasterSlaveRole": LumPortDeviceMasterSlaveRole,
       "LumPortDeviceMdixMode": LumPortDeviceMdixMode,
       "LumPortDevicePauseMode": LumPortDevicePauseMode,
       "LumPortDeviceInterface": LumPortDeviceInterface,
       "lumPortdeviceIfMIBModule": lumPortdeviceIfMIBModule,
       "lumPortdeviceIfConfs": lumPortdeviceIfConfs,
       "lumPortdeviceIfGroups": lumPortdeviceIfGroups,
       "portDevIfGeneralGroupV1": portDevIfGeneralGroupV1,
       "portDevIfL1GroupV1": portDevIfL1GroupV1,
       "portDevIfL2GroupV1": portDevIfL2GroupV1,
       "lumPortdeviceIfCompl": lumPortdeviceIfCompl,
       "lumPortDeviceBasicComplV1": lumPortDeviceBasicComplV1,
       "lumPortdeviceIfMIBObjects": lumPortdeviceIfMIBObjects,
       "portDevIfGeneral": portDevIfGeneral,
       "portDevIfGeneralLastChangeTime": portDevIfGeneralLastChangeTime,
       "portDevIfGeneralStateLastChangeTime": portDevIfGeneralStateLastChangeTime,
       "portDevIfL1TableSize": portDevIfL1TableSize,
       "portDevIfL2TableSize": portDevIfL2TableSize,
       "portDevIfL1List": portDevIfL1List,
       "portDevIfL1Table": portDevIfL1Table,
       "portDevIfL1Entry": portDevIfL1Entry,
       "portDevIfIndex": portDevIfIndex,
       "portDevIfL1Name": portDevIfL1Name,
       "portDevIfL1Descr": portDevIfL1Descr,
       "portDevIfL1AdminStatus": portDevIfL1AdminStatus,
       "portDevIfL1OperStatus": portDevIfL1OperStatus,
       "portDevIfL1PortDevId": portDevIfL1PortDevId,
       "portDevIfL1Subrack": portDevIfL1Subrack,
       "portDevIfL1Slot": portDevIfL1Slot,
       "portDevIfL1LocalPort": portDevIfL1LocalPort,
       "portDevIfL1VlanId": portDevIfL1VlanId,
       "portDevIfL1NidPort": portDevIfL1NidPort,
       "portDevIfL1InternalReference": portDevIfL1InternalReference,
       "portDevIfL1LaserStatus": portDevIfL1LaserStatus,
       "portDevIfL1LaserBias": portDevIfL1LaserBias,
       "portDevIfL1LaserTempActual": portDevIfL1LaserTempActual,
       "portDevIfL1TxFrequency": portDevIfL1TxFrequency,
       "portDevIfL1ExpectedTxFrequency": portDevIfL1ExpectedTxFrequency,
       "portDevIfL1SignalFormat": portDevIfL1SignalFormat,
       "portDevIfL1TrxMedia": portDevIfL1TrxMedia,
       "portDevIfL1ReceiverSensitivity": portDevIfL1ReceiverSensitivity,
       "portDevIfL1PowerLevel": portDevIfL1PowerLevel,
       "portDevIfL1PowerLevelLowRelativeThreshold": portDevIfL1PowerLevelLowRelativeThreshold,
       "portDevIfL1TxPowerLevel": portDevIfL1TxPowerLevel,
       "portDevIfL1RxHighPower": portDevIfL1RxHighPower,
       "portDevIfL1TrxClass": portDevIfL1TrxClass,
       "portDevIfL1LossOfSignal": portDevIfL1LossOfSignal,
       "portDevIfL1TrxMissing": portDevIfL1TrxMissing,
       "portDevIfL1ReceivedPowerLow": portDevIfL1ReceivedPowerLow,
       "portDevIfL1ReceivedPowerHigh": portDevIfL1ReceivedPowerHigh,
       "portDevIfL2List": portDevIfL2List,
       "portDevIfL2Table": portDevIfL2Table,
       "portDevIfL2Entry": portDevIfL2Entry,
       "portDevIfL2Index": portDevIfL2Index,
       "portDevIfL2Name": portDevIfL2Name,
       "portDevIfL2Descr": portDevIfL2Descr,
       "portDevIfL2PortDevId": portDevIfL2PortDevId,
       "portDevIfL2Subrack": portDevIfL2Subrack,
       "portDevIfL2Slot": portDevIfL2Slot,
       "portDevIfL2LocalPort": portDevIfL2LocalPort,
       "portDevIfL2VlanId": portDevIfL2VlanId,
       "portDevIfL2NidPort": portDevIfL2NidPort,
       "portDevIfL2InternalReference": portDevIfL2InternalReference,
       "portDevIfL2AutoNegotiation": portDevIfL2AutoNegotiation,
       "portDevIfL2AutoNegotiationStatus": portDevIfL2AutoNegotiationStatus}
)
