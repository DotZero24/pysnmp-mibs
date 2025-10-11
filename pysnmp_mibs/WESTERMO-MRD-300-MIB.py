# SNMP MIB module (WESTERMO-MRD-300-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/westermo/WESTERMO-MRD-300-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:54:25 2025
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

westermo = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 16177)
)
if mibBuilder.loadTexts:
    westermo.setRevisions(
        ("2009-01-26 12:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Products_ObjectIdentity = ObjectIdentity
products = _Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16177, 1)
)
_Mrd_ObjectIdentity = ObjectIdentity
mrd = _Mrd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16177, 1, 200)
)
_Config_ObjectIdentity = ObjectIdentity
config = _Config_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16177, 1, 200, 1)
)
_ConfigModelName_Type = DisplayString
_ConfigModelName_Object = MibScalar
configModelName = _ConfigModelName_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 200, 1, 1),
    _ConfigModelName_Type()
)
configModelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configModelName.setStatus("current")
_ConfigSerialNumber_Type = DisplayString
_ConfigSerialNumber_Object = MibScalar
configSerialNumber = _ConfigSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 200, 1, 2),
    _ConfigSerialNumber_Type()
)
configSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configSerialNumber.setStatus("current")
_ConfigFirmwareRev_Type = DisplayString
_ConfigFirmwareRev_Object = MibScalar
configFirmwareRev = _ConfigFirmwareRev_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 200, 1, 3),
    _ConfigFirmwareRev_Type()
)
configFirmwareRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configFirmwareRev.setStatus("current")
_Status_ObjectIdentity = ObjectIdentity
status = _Status_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16177, 1, 200, 2)
)


class _StatusSelfTest_Type(Integer32):
    """Custom type statusSelfTest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("failed", 0),
          ("passed", 1))
    )


_StatusSelfTest_Type.__name__ = "Integer32"
_StatusSelfTest_Object = MibScalar
statusSelfTest = _StatusSelfTest_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 200, 2, 1),
    _StatusSelfTest_Type()
)
statusSelfTest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusSelfTest.setStatus("current")
_StatusTemperature_Type = Integer32
_StatusTemperature_Object = MibScalar
statusTemperature = _StatusTemperature_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 200, 2, 2),
    _StatusTemperature_Type()
)
statusTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusTemperature.setStatus("current")
_Wireless_ObjectIdentity = ObjectIdentity
wireless = _Wireless_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16177, 1, 200, 3)
)


class _WirelessOperatingMode_Type(Integer32):
    """Custom type wirelessOperatingMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("packet", 0),
          ("csd", 1),
          ("disabled", 2))
    )


_WirelessOperatingMode_Type.__name__ = "Integer32"
_WirelessOperatingMode_Object = MibScalar
wirelessOperatingMode = _WirelessOperatingMode_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 200, 3, 1),
    _WirelessOperatingMode_Type()
)
wirelessOperatingMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessOperatingMode.setStatus("current")


class _WirelessNetworkReg_Type(Integer32):
    """Custom type wirelessNetworkReg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_WirelessNetworkReg_Type.__name__ = "Integer32"
_WirelessNetworkReg_Object = MibScalar
wirelessNetworkReg = _WirelessNetworkReg_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 200, 3, 2),
    _WirelessNetworkReg_Type()
)
wirelessNetworkReg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessNetworkReg.setStatus("current")


class _WirelessRFLevel_Type(Integer32):
    """Custom type wirelessRFLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30),
    )


_WirelessRFLevel_Type.__name__ = "Integer32"
_WirelessRFLevel_Object = MibScalar
wirelessRFLevel = _WirelessRFLevel_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 200, 3, 3),
    _WirelessRFLevel_Type()
)
wirelessRFLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessRFLevel.setStatus("current")
_WirelessProvider_Type = DisplayString
_WirelessProvider_Object = MibScalar
wirelessProvider = _WirelessProvider_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 200, 3, 4),
    _WirelessProvider_Type()
)
wirelessProvider.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessProvider.setStatus("current")
_WirelessLocationID_Type = DisplayString
_WirelessLocationID_Object = MibScalar
wirelessLocationID = _WirelessLocationID_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 200, 3, 5),
    _WirelessLocationID_Type()
)
wirelessLocationID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessLocationID.setStatus("current")
_WirelessCellID_Type = DisplayString
_WirelessCellID_Object = MibScalar
wirelessCellID = _WirelessCellID_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 200, 3, 6),
    _WirelessCellID_Type()
)
wirelessCellID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessCellID.setStatus("current")
_WirelessPacket_ObjectIdentity = ObjectIdentity
wirelessPacket = _WirelessPacket_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16177, 1, 200, 3, 15)
)


class _WirelessPacketState_Type(Integer32):
    """Custom type wirelessPacketState based on Integer32"""
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
        *(("disabled", 0),
          ("errored", 1),
          ("waitingForActivity", 2),
          ("connecting", 3),
          ("connected", 4),
          ("csdFallback", 5))
    )


_WirelessPacketState_Type.__name__ = "Integer32"
_WirelessPacketState_Object = MibScalar
wirelessPacketState = _WirelessPacketState_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 200, 3, 15, 1),
    _WirelessPacketState_Type()
)
wirelessPacketState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessPacketState.setStatus("current")
_WirelessPacketCurrentSessionTime_Type = TimeTicks
_WirelessPacketCurrentSessionTime_Object = MibScalar
wirelessPacketCurrentSessionTime = _WirelessPacketCurrentSessionTime_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 200, 3, 15, 2),
    _WirelessPacketCurrentSessionTime_Type()
)
wirelessPacketCurrentSessionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessPacketCurrentSessionTime.setStatus("current")
_WirelessPacketTotalSessionTime_Type = TimeTicks
_WirelessPacketTotalSessionTime_Object = MibScalar
wirelessPacketTotalSessionTime = _WirelessPacketTotalSessionTime_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 200, 3, 15, 3),
    _WirelessPacketTotalSessionTime_Type()
)
wirelessPacketTotalSessionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessPacketTotalSessionTime.setStatus("current")
_WirelessCSD_ObjectIdentity = ObjectIdentity
wirelessCSD = _WirelessCSD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16177, 1, 200, 3, 16)
)


class _WirelessCSDState_Type(Integer32):
    """Custom type wirelessCSDState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("offline", 0),
          ("dialing", 1),
          ("ringing", 2),
          ("answering", 3),
          ("online", 4))
    )


_WirelessCSDState_Type.__name__ = "Integer32"
_WirelessCSDState_Object = MibScalar
wirelessCSDState = _WirelessCSDState_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 200, 3, 16, 1),
    _WirelessCSDState_Type()
)
wirelessCSDState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessCSDState.setStatus("current")
_WirelessCSDSessions_Type = Integer32
_WirelessCSDSessions_Object = MibScalar
wirelessCSDSessions = _WirelessCSDSessions_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 200, 3, 16, 2),
    _WirelessCSDSessions_Type()
)
wirelessCSDSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessCSDSessions.setStatus("current")
_WirelessCSDCurrentSessionTime_Type = TimeTicks
_WirelessCSDCurrentSessionTime_Object = MibScalar
wirelessCSDCurrentSessionTime = _WirelessCSDCurrentSessionTime_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 200, 3, 16, 3),
    _WirelessCSDCurrentSessionTime_Type()
)
wirelessCSDCurrentSessionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessCSDCurrentSessionTime.setStatus("current")
_WirelessCSDTotalSessionTime_Type = TimeTicks
_WirelessCSDTotalSessionTime_Object = MibScalar
wirelessCSDTotalSessionTime = _WirelessCSDTotalSessionTime_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 200, 3, 16, 4),
    _WirelessCSDTotalSessionTime_Type()
)
wirelessCSDTotalSessionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wirelessCSDTotalSessionTime.setStatus("current")
_SerialServer_ObjectIdentity = ObjectIdentity
serialServer = _SerialServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16177, 1, 200, 4)
)
_SerialServerTable_Object = MibTable
serialServerTable = _SerialServerTable_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 200, 4, 1)
)
if mibBuilder.loadTexts:
    serialServerTable.setStatus("current")
_SerialServerEntry_Object = MibTableRow
serialServerEntry = _SerialServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 200, 4, 1, 1)
)
serialServerEntry.setIndexNames(
    (0, "WESTERMO-MRD-300-MIB", "serialServerIndex"),
)
if mibBuilder.loadTexts:
    serialServerEntry.setStatus("current")


class _SerialServerIndex_Type(Integer32):
    """Custom type serialServerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_SerialServerIndex_Type.__name__ = "Integer32"
_SerialServerIndex_Object = MibTableColumn
serialServerIndex = _SerialServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 200, 4, 1, 1, 1),
    _SerialServerIndex_Type()
)
serialServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    serialServerIndex.setStatus("current")


class _SerialServerFunction_Type(Integer32):
    """Custom type serialServerFunction based on Integer32"""
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
        *(("disabled", 0),
          ("rawTCPorUDP", 1),
          ("modemEmulator", 2),
          ("dnp3Gateway", 3),
          ("telnetServer", 4),
          ("modbusGateway", 5))
    )


_SerialServerFunction_Type.__name__ = "Integer32"
_SerialServerFunction_Object = MibTableColumn
serialServerFunction = _SerialServerFunction_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 200, 4, 1, 1, 2),
    _SerialServerFunction_Type()
)
serialServerFunction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serialServerFunction.setStatus("current")


class _SerialServerNetState_Type(Integer32):
    """Custom type serialServerNetState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notConnected", 0),
          ("connecting", 1),
          ("connected", 2))
    )


_SerialServerNetState_Type.__name__ = "Integer32"
_SerialServerNetState_Object = MibTableColumn
serialServerNetState = _SerialServerNetState_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 200, 4, 1, 1, 3),
    _SerialServerNetState_Type()
)
serialServerNetState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serialServerNetState.setStatus("current")
_SerialServerRemoteAddress_Type = IpAddress
_SerialServerRemoteAddress_Object = MibTableColumn
serialServerRemoteAddress = _SerialServerRemoteAddress_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 200, 4, 1, 1, 4),
    _SerialServerRemoteAddress_Type()
)
serialServerRemoteAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serialServerRemoteAddress.setStatus("current")
_SerialServerUptime_Type = TimeTicks
_SerialServerUptime_Object = MibTableColumn
serialServerUptime = _SerialServerUptime_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 200, 4, 1, 1, 5),
    _SerialServerUptime_Type()
)
serialServerUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serialServerUptime.setStatus("current")
_SerialServerBytesTx_Type = Counter32
_SerialServerBytesTx_Object = MibTableColumn
serialServerBytesTx = _SerialServerBytesTx_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 200, 4, 1, 1, 6),
    _SerialServerBytesTx_Type()
)
serialServerBytesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serialServerBytesTx.setStatus("current")
_SerialServerBytesRx_Type = Counter32
_SerialServerBytesRx_Object = MibTableColumn
serialServerBytesRx = _SerialServerBytesRx_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 200, 4, 1, 1, 7),
    _SerialServerBytesRx_Type()
)
serialServerBytesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serialServerBytesRx.setStatus("current")
_SerialServerFramingErrors_Type = Counter32
_SerialServerFramingErrors_Object = MibTableColumn
serialServerFramingErrors = _SerialServerFramingErrors_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 200, 4, 1, 1, 8),
    _SerialServerFramingErrors_Type()
)
serialServerFramingErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serialServerFramingErrors.setStatus("current")
_SerialServerOverrunErrors_Type = Counter32
_SerialServerOverrunErrors_Object = MibTableColumn
serialServerOverrunErrors = _SerialServerOverrunErrors_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 200, 4, 1, 1, 9),
    _SerialServerOverrunErrors_Type()
)
serialServerOverrunErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serialServerOverrunErrors.setStatus("current")
_SerialServerParityErrors_Type = Counter32
_SerialServerParityErrors_Object = MibTableColumn
serialServerParityErrors = _SerialServerParityErrors_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 200, 4, 1, 1, 10),
    _SerialServerParityErrors_Type()
)
serialServerParityErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serialServerParityErrors.setStatus("current")
_SerialServerBreaks_Type = Counter32
_SerialServerBreaks_Object = MibTableColumn
serialServerBreaks = _SerialServerBreaks_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 200, 4, 1, 1, 11),
    _SerialServerBreaks_Type()
)
serialServerBreaks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serialServerBreaks.setStatus("current")
_Gpio_ObjectIdentity = ObjectIdentity
gpio = _Gpio_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16177, 1, 200, 5)
)
_GpioInputsTable_Object = MibTable
gpioInputsTable = _GpioInputsTable_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 200, 5, 1)
)
if mibBuilder.loadTexts:
    gpioInputsTable.setStatus("current")
_GpioInputsTableEntry_Object = MibTableRow
gpioInputsTableEntry = _GpioInputsTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 200, 5, 1, 1)
)
gpioInputsTableEntry.setIndexNames(
    (0, "WESTERMO-MRD-300-MIB", "gpioInputsIndex"),
)
if mibBuilder.loadTexts:
    gpioInputsTableEntry.setStatus("current")


class _GpioInputsIndex_Type(Integer32):
    """Custom type gpioInputsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_GpioInputsIndex_Type.__name__ = "Integer32"
_GpioInputsIndex_Object = MibTableColumn
gpioInputsIndex = _GpioInputsIndex_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 200, 5, 1, 1, 1),
    _GpioInputsIndex_Type()
)
gpioInputsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gpioInputsIndex.setStatus("current")
_GpioInputsLabel_Type = DisplayString
_GpioInputsLabel_Object = MibTableColumn
gpioInputsLabel = _GpioInputsLabel_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 200, 5, 1, 1, 2),
    _GpioInputsLabel_Type()
)
gpioInputsLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpioInputsLabel.setStatus("current")


class _GpioInputsState_Type(Integer32):
    """Custom type gpioInputsState based on Integer32"""
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


_GpioInputsState_Type.__name__ = "Integer32"
_GpioInputsState_Object = MibTableColumn
gpioInputsState = _GpioInputsState_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 200, 5, 1, 1, 3),
    _GpioInputsState_Type()
)
gpioInputsState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpioInputsState.setStatus("current")
_GpioInputsToggles_Type = Counter32
_GpioInputsToggles_Object = MibTableColumn
gpioInputsToggles = _GpioInputsToggles_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 200, 5, 1, 1, 4),
    _GpioInputsToggles_Type()
)
gpioInputsToggles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpioInputsToggles.setStatus("current")
_GpioInputsClosedTime_Type = TimeTicks
_GpioInputsClosedTime_Object = MibTableColumn
gpioInputsClosedTime = _GpioInputsClosedTime_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 200, 5, 1, 1, 5),
    _GpioInputsClosedTime_Type()
)
gpioInputsClosedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpioInputsClosedTime.setStatus("current")
_GpioOutputsTable_Object = MibTable
gpioOutputsTable = _GpioOutputsTable_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 200, 5, 2)
)
if mibBuilder.loadTexts:
    gpioOutputsTable.setStatus("current")
_GpioOutputsTableEntry_Object = MibTableRow
gpioOutputsTableEntry = _GpioOutputsTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 200, 5, 2, 1)
)
gpioOutputsTableEntry.setIndexNames(
    (0, "WESTERMO-MRD-300-MIB", "gpioOutputsIndex"),
)
if mibBuilder.loadTexts:
    gpioOutputsTableEntry.setStatus("current")


class _GpioOutputsIndex_Type(Integer32):
    """Custom type gpioOutputsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_GpioOutputsIndex_Type.__name__ = "Integer32"
_GpioOutputsIndex_Object = MibTableColumn
gpioOutputsIndex = _GpioOutputsIndex_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 200, 5, 2, 1, 1),
    _GpioOutputsIndex_Type()
)
gpioOutputsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gpioOutputsIndex.setStatus("current")
_GpioOutputsLabel_Type = DisplayString
_GpioOutputsLabel_Object = MibTableColumn
gpioOutputsLabel = _GpioOutputsLabel_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 200, 5, 2, 1, 2),
    _GpioOutputsLabel_Type()
)
gpioOutputsLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpioOutputsLabel.setStatus("current")


class _GpioOutputsState_Type(Integer32):
    """Custom type gpioOutputsState based on Integer32"""
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


_GpioOutputsState_Type.__name__ = "Integer32"
_GpioOutputsState_Object = MibTableColumn
gpioOutputsState = _GpioOutputsState_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 200, 5, 2, 1, 3),
    _GpioOutputsState_Type()
)
gpioOutputsState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gpioOutputsState.setStatus("current")
_GpioOutputsToggles_Type = Counter32
_GpioOutputsToggles_Object = MibTableColumn
gpioOutputsToggles = _GpioOutputsToggles_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 200, 5, 2, 1, 4),
    _GpioOutputsToggles_Type()
)
gpioOutputsToggles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpioOutputsToggles.setStatus("current")
_GpioOutputsClosedTime_Type = TimeTicks
_GpioOutputsClosedTime_Object = MibTableColumn
gpioOutputsClosedTime = _GpioOutputsClosedTime_Object(
    (1, 3, 6, 1, 4, 1, 16177, 1, 200, 5, 2, 1, 5),
    _GpioOutputsClosedTime_Type()
)
gpioOutputsClosedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpioOutputsClosedTime.setStatus("current")
_MrdTraps_ObjectIdentity = ObjectIdentity
mrdTraps = _MrdTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16177, 1, 200, 20)
)
_MrdTrapsNode_ObjectIdentity = ObjectIdentity
mrdTrapsNode = _MrdTrapsNode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 16177, 1, 200, 20, 0)
)

# Managed Objects groups


# Notification objects

wirelessState = NotificationType(
    (1, 3, 6, 1, 4, 1, 16177, 1, 200, 20, 0, 1)
)
wirelessState.setObjects(
      *(("WESTERMO-MRD-300-MIB", "wirelessNetworkReg"),
        ("WESTERMO-MRD-300-MIB", "wirelessRFLevel"),
        ("WESTERMO-MRD-300-MIB", "wirelessProvider"),
        ("WESTERMO-MRD-300-MIB", "wirelessLocationID"),
        ("WESTERMO-MRD-300-MIB", "wirelessCellID"))
)
if mibBuilder.loadTexts:
    wirelessState.setStatus(
        "current"
    )

gpioInputState = NotificationType(
    (1, 3, 6, 1, 4, 1, 16177, 1, 200, 20, 0, 10)
)
gpioInputState.setObjects(
      *(("WESTERMO-MRD-300-MIB", "gpioInputsState"),
        ("WESTERMO-MRD-300-MIB", "gpioInputsToggles"))
)
if mibBuilder.loadTexts:
    gpioInputState.setStatus(
        "current"
    )

gpioOutputState = NotificationType(
    (1, 3, 6, 1, 4, 1, 16177, 1, 200, 20, 0, 11)
)
gpioOutputState.setObjects(
      *(("WESTERMO-MRD-300-MIB", "gpioOutputsState"),
        ("WESTERMO-MRD-300-MIB", "gpioOutputsToggles"))
)
if mibBuilder.loadTexts:
    gpioOutputState.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WESTERMO-MRD-300-MIB",
    **{"westermo": westermo,
       "products": products,
       "mrd": mrd,
       "config": config,
       "configModelName": configModelName,
       "configSerialNumber": configSerialNumber,
       "configFirmwareRev": configFirmwareRev,
       "status": status,
       "statusSelfTest": statusSelfTest,
       "statusTemperature": statusTemperature,
       "wireless": wireless,
       "wirelessOperatingMode": wirelessOperatingMode,
       "wirelessNetworkReg": wirelessNetworkReg,
       "wirelessRFLevel": wirelessRFLevel,
       "wirelessProvider": wirelessProvider,
       "wirelessLocationID": wirelessLocationID,
       "wirelessCellID": wirelessCellID,
       "wirelessPacket": wirelessPacket,
       "wirelessPacketState": wirelessPacketState,
       "wirelessPacketCurrentSessionTime": wirelessPacketCurrentSessionTime,
       "wirelessPacketTotalSessionTime": wirelessPacketTotalSessionTime,
       "wirelessCSD": wirelessCSD,
       "wirelessCSDState": wirelessCSDState,
       "wirelessCSDSessions": wirelessCSDSessions,
       "wirelessCSDCurrentSessionTime": wirelessCSDCurrentSessionTime,
       "wirelessCSDTotalSessionTime": wirelessCSDTotalSessionTime,
       "serialServer": serialServer,
       "serialServerTable": serialServerTable,
       "serialServerEntry": serialServerEntry,
       "serialServerIndex": serialServerIndex,
       "serialServerFunction": serialServerFunction,
       "serialServerNetState": serialServerNetState,
       "serialServerRemoteAddress": serialServerRemoteAddress,
       "serialServerUptime": serialServerUptime,
       "serialServerBytesTx": serialServerBytesTx,
       "serialServerBytesRx": serialServerBytesRx,
       "serialServerFramingErrors": serialServerFramingErrors,
       "serialServerOverrunErrors": serialServerOverrunErrors,
       "serialServerParityErrors": serialServerParityErrors,
       "serialServerBreaks": serialServerBreaks,
       "gpio": gpio,
       "gpioInputsTable": gpioInputsTable,
       "gpioInputsTableEntry": gpioInputsTableEntry,
       "gpioInputsIndex": gpioInputsIndex,
       "gpioInputsLabel": gpioInputsLabel,
       "gpioInputsState": gpioInputsState,
       "gpioInputsToggles": gpioInputsToggles,
       "gpioInputsClosedTime": gpioInputsClosedTime,
       "gpioOutputsTable": gpioOutputsTable,
       "gpioOutputsTableEntry": gpioOutputsTableEntry,
       "gpioOutputsIndex": gpioOutputsIndex,
       "gpioOutputsLabel": gpioOutputsLabel,
       "gpioOutputsState": gpioOutputsState,
       "gpioOutputsToggles": gpioOutputsToggles,
       "gpioOutputsClosedTime": gpioOutputsClosedTime,
       "mrdTraps": mrdTraps,
       "mrdTrapsNode": mrdTrapsNode,
       "wirelessState": wirelessState,
       "gpioInputState": gpioInputState,
       "gpioOutputState": gpioOutputState}
)
