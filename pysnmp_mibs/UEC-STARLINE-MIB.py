# SNMP MIB module (UEC-STARLINE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/uec/UEC-STARLINE-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:05:25 2025
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

(DateAndTime,
 DisplayString,
 MacAddress,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

uecStarline = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 35774)
)
if mibBuilder.loadTexts:
    uecStarline.setRevisions(
        ("2017-10-11 15:24",
         "2017-05-31 11:47",
         "2016-03-21 18:51",
         "2015-03-25 03:33",
         "2014-06-03 16:16",
         "2014-01-20 16:17",
         "2013-10-14 14:00",
         "2013-09-09 13:50",
         "2013-08-26 16:20",
         "2013-08-22 16:15",
         "2013-08-07 20:05",
         "2013-08-07 17:03",
         "2013-08-07 14:42",
         "2013-08-06 18:29",
         "2013-05-30 21:11",
         "2013-05-21 15:39",
         "2013-03-26 19:49",
         "2013-03-08 13:43",
         "2013-03-06 17:28",
         "2013-03-01 20:32",
         "2013-02-27 22:23",
         "2013-02-25 21:05",
         "2013-02-22 19:04",
         "2013-02-20 16:03",
         "2013-02-14 14:02",
         "2012-06-13 18:01",
         "2011-04-25 17:00")
    )


# Types definitions



class DisplayString(OctetString):
    """Custom type DisplayString based on OctetString"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Cpm_ObjectIdentity = ObjectIdentity
cpm = _Cpm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35774, 2)
)
_CpmAcMeter_ObjectIdentity = ObjectIdentity
cpmAcMeter = _CpmAcMeter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35774, 2, 1)
)
_CpmAcGeneral_ObjectIdentity = ObjectIdentity
cpmAcGeneral = _CpmAcGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35774, 2, 1, 1)
)
_CpmAcDeviceName_Type = DisplayString
_CpmAcDeviceName_Object = MibScalar
cpmAcDeviceName = _CpmAcDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 1, 1, 1),
    _CpmAcDeviceName_Type()
)
cpmAcDeviceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpmAcDeviceName.setStatus("current")
_CpmAcDeviceLocation_Type = DisplayString
_CpmAcDeviceLocation_Object = MibScalar
cpmAcDeviceLocation = _CpmAcDeviceLocation_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 1, 1, 2),
    _CpmAcDeviceLocation_Type()
)
cpmAcDeviceLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpmAcDeviceLocation.setStatus("current")
_CpmAcDeviceId_Type = DisplayString
_CpmAcDeviceId_Object = MibScalar
cpmAcDeviceId = _CpmAcDeviceId_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 1, 1, 3),
    _CpmAcDeviceId_Type()
)
cpmAcDeviceId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpmAcDeviceId.setStatus("current")
_CpmAcModelNumber_Type = DisplayString
_CpmAcModelNumber_Object = MibScalar
cpmAcModelNumber = _CpmAcModelNumber_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 1, 1, 4),
    _CpmAcModelNumber_Type()
)
cpmAcModelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmAcModelNumber.setStatus("current")
_CpmAcSerialNumber_Type = DisplayString
_CpmAcSerialNumber_Object = MibScalar
cpmAcSerialNumber = _CpmAcSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 1, 1, 5),
    _CpmAcSerialNumber_Type()
)
cpmAcSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmAcSerialNumber.setStatus("current")
_CpmAcCatalogNumber_Type = DisplayString
_CpmAcCatalogNumber_Object = MibScalar
cpmAcCatalogNumber = _CpmAcCatalogNumber_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 1, 1, 6),
    _CpmAcCatalogNumber_Type()
)
cpmAcCatalogNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmAcCatalogNumber.setStatus("current")
_CpmAcFirmwareVersion_Type = DisplayString
_CpmAcFirmwareVersion_Object = MibScalar
cpmAcFirmwareVersion = _CpmAcFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 1, 1, 7),
    _CpmAcFirmwareVersion_Type()
)
cpmAcFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmAcFirmwareVersion.setStatus("current")
_CpmAcCalibrationDate_Type = DisplayString
_CpmAcCalibrationDate_Object = MibScalar
cpmAcCalibrationDate = _CpmAcCalibrationDate_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 1, 1, 8),
    _CpmAcCalibrationDate_Type()
)
cpmAcCalibrationDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmAcCalibrationDate.setStatus("current")
_CpmAcEnergyReset_Type = DisplayString
_CpmAcEnergyReset_Object = MibScalar
cpmAcEnergyReset = _CpmAcEnergyReset_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 1, 1, 9),
    _CpmAcEnergyReset_Type()
)
cpmAcEnergyReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpmAcEnergyReset.setStatus("current")
_CpmAcGroupReset_Type = DisplayString
_CpmAcGroupReset_Object = MibScalar
cpmAcGroupReset = _CpmAcGroupReset_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 1, 1, 10),
    _CpmAcGroupReset_Type()
)
cpmAcGroupReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpmAcGroupReset.setStatus("current")
_CpmAcInterfaces_ObjectIdentity = ObjectIdentity
cpmAcInterfaces = _CpmAcInterfaces_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35774, 2, 1, 2)
)
_CpmAcEthernet_ObjectIdentity = ObjectIdentity
cpmAcEthernet = _CpmAcEthernet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35774, 2, 1, 2, 1)
)
_CpmAcEnetMacAddress_Type = DisplayString
_CpmAcEnetMacAddress_Object = MibScalar
cpmAcEnetMacAddress = _CpmAcEnetMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 1, 2, 1, 1),
    _CpmAcEnetMacAddress_Type()
)
cpmAcEnetMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmAcEnetMacAddress.setStatus("current")
_CpmAcEnetIpAddress_Type = DisplayString
_CpmAcEnetIpAddress_Object = MibScalar
cpmAcEnetIpAddress = _CpmAcEnetIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 1, 2, 1, 2),
    _CpmAcEnetIpAddress_Type()
)
cpmAcEnetIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmAcEnetIpAddress.setStatus("current")
_CpmAcEnetIpNetmask_Type = DisplayString
_CpmAcEnetIpNetmask_Object = MibScalar
cpmAcEnetIpNetmask = _CpmAcEnetIpNetmask_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 1, 2, 1, 3),
    _CpmAcEnetIpNetmask_Type()
)
cpmAcEnetIpNetmask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmAcEnetIpNetmask.setStatus("current")
_CpmAcEnetIpGateway_Type = DisplayString
_CpmAcEnetIpGateway_Object = MibScalar
cpmAcEnetIpGateway = _CpmAcEnetIpGateway_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 1, 2, 1, 4),
    _CpmAcEnetIpGateway_Type()
)
cpmAcEnetIpGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmAcEnetIpGateway.setStatus("current")
_CpmAcEnetEnableDHCP_Type = DisplayString
_CpmAcEnetEnableDHCP_Object = MibScalar
cpmAcEnetEnableDHCP = _CpmAcEnetEnableDHCP_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 1, 2, 1, 5),
    _CpmAcEnetEnableDHCP_Type()
)
cpmAcEnetEnableDHCP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpmAcEnetEnableDHCP.setStatus("current")
_CpmAcEnetStaticIpAddress_Type = DisplayString
_CpmAcEnetStaticIpAddress_Object = MibScalar
cpmAcEnetStaticIpAddress = _CpmAcEnetStaticIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 1, 2, 1, 6),
    _CpmAcEnetStaticIpAddress_Type()
)
cpmAcEnetStaticIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpmAcEnetStaticIpAddress.setStatus("current")
_CpmAcEnetStaticIpNetmask_Type = DisplayString
_CpmAcEnetStaticIpNetmask_Object = MibScalar
cpmAcEnetStaticIpNetmask = _CpmAcEnetStaticIpNetmask_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 1, 2, 1, 7),
    _CpmAcEnetStaticIpNetmask_Type()
)
cpmAcEnetStaticIpNetmask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpmAcEnetStaticIpNetmask.setStatus("current")
_CpmAcEnetStaticIpGateway_Type = DisplayString
_CpmAcEnetStaticIpGateway_Object = MibScalar
cpmAcEnetStaticIpGateway = _CpmAcEnetStaticIpGateway_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 1, 2, 1, 8),
    _CpmAcEnetStaticIpGateway_Type()
)
cpmAcEnetStaticIpGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpmAcEnetStaticIpGateway.setStatus("current")
_CpmAcWifi_ObjectIdentity = ObjectIdentity
cpmAcWifi = _CpmAcWifi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35774, 2, 1, 2, 2)
)
_CpmAcWifiMacAddress_Type = DisplayString
_CpmAcWifiMacAddress_Object = MibScalar
cpmAcWifiMacAddress = _CpmAcWifiMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 1, 2, 2, 1),
    _CpmAcWifiMacAddress_Type()
)
cpmAcWifiMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmAcWifiMacAddress.setStatus("current")
_CpmAcWifiIpAddress_Type = DisplayString
_CpmAcWifiIpAddress_Object = MibScalar
cpmAcWifiIpAddress = _CpmAcWifiIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 1, 2, 2, 2),
    _CpmAcWifiIpAddress_Type()
)
cpmAcWifiIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmAcWifiIpAddress.setStatus("current")
_CpmAcWifiIpNetmask_Type = DisplayString
_CpmAcWifiIpNetmask_Object = MibScalar
cpmAcWifiIpNetmask = _CpmAcWifiIpNetmask_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 1, 2, 2, 3),
    _CpmAcWifiIpNetmask_Type()
)
cpmAcWifiIpNetmask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmAcWifiIpNetmask.setStatus("current")
_CpmAcWifiIpGateway_Type = DisplayString
_CpmAcWifiIpGateway_Object = MibScalar
cpmAcWifiIpGateway = _CpmAcWifiIpGateway_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 1, 2, 2, 4),
    _CpmAcWifiIpGateway_Type()
)
cpmAcWifiIpGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmAcWifiIpGateway.setStatus("current")
_CpmAcWifiEnableDHCP_Type = DisplayString
_CpmAcWifiEnableDHCP_Object = MibScalar
cpmAcWifiEnableDHCP = _CpmAcWifiEnableDHCP_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 1, 2, 2, 5),
    _CpmAcWifiEnableDHCP_Type()
)
cpmAcWifiEnableDHCP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpmAcWifiEnableDHCP.setStatus("current")
_CpmAcWifiStaticIpAddress_Type = DisplayString
_CpmAcWifiStaticIpAddress_Object = MibScalar
cpmAcWifiStaticIpAddress = _CpmAcWifiStaticIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 1, 2, 2, 6),
    _CpmAcWifiStaticIpAddress_Type()
)
cpmAcWifiStaticIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpmAcWifiStaticIpAddress.setStatus("current")
_CpmAcWifiStaticIpNetmask_Type = DisplayString
_CpmAcWifiStaticIpNetmask_Object = MibScalar
cpmAcWifiStaticIpNetmask = _CpmAcWifiStaticIpNetmask_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 1, 2, 2, 7),
    _CpmAcWifiStaticIpNetmask_Type()
)
cpmAcWifiStaticIpNetmask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpmAcWifiStaticIpNetmask.setStatus("current")
_CpmAcWifiStaticIpGateway_Type = DisplayString
_CpmAcWifiStaticIpGateway_Object = MibScalar
cpmAcWifiStaticIpGateway = _CpmAcWifiStaticIpGateway_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 1, 2, 2, 8),
    _CpmAcWifiStaticIpGateway_Type()
)
cpmAcWifiStaticIpGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpmAcWifiStaticIpGateway.setStatus("current")
_CpmAcWifiSSID_Type = DisplayString
_CpmAcWifiSSID_Object = MibScalar
cpmAcWifiSSID = _CpmAcWifiSSID_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 1, 2, 2, 9),
    _CpmAcWifiSSID_Type()
)
cpmAcWifiSSID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpmAcWifiSSID.setStatus("current")
_CpmAcWifiEncryptionType_Type = DisplayString
_CpmAcWifiEncryptionType_Object = MibScalar
cpmAcWifiEncryptionType = _CpmAcWifiEncryptionType_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 1, 2, 2, 10),
    _CpmAcWifiEncryptionType_Type()
)
cpmAcWifiEncryptionType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpmAcWifiEncryptionType.setStatus("current")
_CpmAcModbus_ObjectIdentity = ObjectIdentity
cpmAcModbus = _CpmAcModbus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35774, 2, 1, 2, 3)
)
_CpmAcModbusAddress_Type = DisplayString
_CpmAcModbusAddress_Object = MibScalar
cpmAcModbusAddress = _CpmAcModbusAddress_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 1, 2, 3, 1),
    _CpmAcModbusAddress_Type()
)
cpmAcModbusAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpmAcModbusAddress.setStatus("current")
_CpmAcModbusBaudRate_Type = DisplayString
_CpmAcModbusBaudRate_Object = MibScalar
cpmAcModbusBaudRate = _CpmAcModbusBaudRate_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 1, 2, 3, 2),
    _CpmAcModbusBaudRate_Type()
)
cpmAcModbusBaudRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpmAcModbusBaudRate.setStatus("current")
_CpmAcModbusStopBits_Type = DisplayString
_CpmAcModbusStopBits_Object = MibScalar
cpmAcModbusStopBits = _CpmAcModbusStopBits_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 1, 2, 3, 3),
    _CpmAcModbusStopBits_Type()
)
cpmAcModbusStopBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpmAcModbusStopBits.setStatus("current")
_CpmAcModbusParity_Type = DisplayString
_CpmAcModbusParity_Object = MibScalar
cpmAcModbusParity = _CpmAcModbusParity_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 1, 2, 3, 4),
    _CpmAcModbusParity_Type()
)
cpmAcModbusParity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpmAcModbusParity.setStatus("current")
_CpmAcDigitalIo_Object = MibTable
cpmAcDigitalIo = _CpmAcDigitalIo_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 1, 2, 4)
)
if mibBuilder.loadTexts:
    cpmAcDigitalIo.setStatus("current")
_CpmAcDigitalIoEntry_Object = MibTableRow
cpmAcDigitalIoEntry = _CpmAcDigitalIoEntry_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 1, 2, 4, 1)
)
cpmAcDigitalIoEntry.setIndexNames(
    (0, "UEC-STARLINE-MIB", "cpmAcDigitalIoIndex"),
)
if mibBuilder.loadTexts:
    cpmAcDigitalIoEntry.setStatus("current")


class _CpmAcDigitalIoIndex_Type(Integer32):
    """Custom type cpmAcDigitalIoIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("port1", 1),
          ("port2", 2))
    )


_CpmAcDigitalIoIndex_Type.__name__ = "Integer32"
_CpmAcDigitalIoIndex_Object = MibTableColumn
cpmAcDigitalIoIndex = _CpmAcDigitalIoIndex_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 1, 2, 4, 1, 1),
    _CpmAcDigitalIoIndex_Type()
)
cpmAcDigitalIoIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cpmAcDigitalIoIndex.setStatus("current")
_CpmAcDigitalIoName_Type = DisplayString
_CpmAcDigitalIoName_Object = MibTableColumn
cpmAcDigitalIoName = _CpmAcDigitalIoName_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 1, 2, 4, 1, 2),
    _CpmAcDigitalIoName_Type()
)
cpmAcDigitalIoName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpmAcDigitalIoName.setStatus("current")
_CpmAcDigitalIoValue_Type = DisplayString
_CpmAcDigitalIoValue_Object = MibTableColumn
cpmAcDigitalIoValue = _CpmAcDigitalIoValue_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 1, 2, 4, 1, 3),
    _CpmAcDigitalIoValue_Type()
)
cpmAcDigitalIoValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpmAcDigitalIoValue.setStatus("current")
_CpmAcDigitalIoDirection_Type = DisplayString
_CpmAcDigitalIoDirection_Object = MibTableColumn
cpmAcDigitalIoDirection = _CpmAcDigitalIoDirection_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 1, 2, 4, 1, 4),
    _CpmAcDigitalIoDirection_Type()
)
cpmAcDigitalIoDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpmAcDigitalIoDirection.setStatus("current")
_CpmAcDigitalIoLevel_Type = DisplayString
_CpmAcDigitalIoLevel_Object = MibTableColumn
cpmAcDigitalIoLevel = _CpmAcDigitalIoLevel_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 1, 2, 4, 1, 5),
    _CpmAcDigitalIoLevel_Type()
)
cpmAcDigitalIoLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpmAcDigitalIoLevel.setStatus("current")
_CpmAcDigitalIoAlarm_Type = DisplayString
_CpmAcDigitalIoAlarm_Object = MibTableColumn
cpmAcDigitalIoAlarm = _CpmAcDigitalIoAlarm_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 1, 2, 4, 1, 6),
    _CpmAcDigitalIoAlarm_Type()
)
cpmAcDigitalIoAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpmAcDigitalIoAlarm.setStatus("current")
_CpmAcAnalogIo_ObjectIdentity = ObjectIdentity
cpmAcAnalogIo = _CpmAcAnalogIo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35774, 2, 1, 2, 5)
)
_CpmAc4to20maPortName_Type = DisplayString
_CpmAc4to20maPortName_Object = MibScalar
cpmAc4to20maPortName = _CpmAc4to20maPortName_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 1, 2, 5, 1),
    _CpmAc4to20maPortName_Type()
)
cpmAc4to20maPortName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpmAc4to20maPortName.setStatus("current")
_CpmAc4to20maValue_Type = DisplayString
_CpmAc4to20maValue_Object = MibScalar
cpmAc4to20maValue = _CpmAc4to20maValue_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 1, 2, 5, 2),
    _CpmAc4to20maValue_Type()
)
cpmAc4to20maValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmAc4to20maValue.setStatus("current")
_CpmAcProtocols_ObjectIdentity = ObjectIdentity
cpmAcProtocols = _CpmAcProtocols_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35774, 2, 1, 3)
)
_CpmAcSnmp_ObjectIdentity = ObjectIdentity
cpmAcSnmp = _CpmAcSnmp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35774, 2, 1, 3, 1)
)
_CpmAcSnmpTrapDestAddr1_Type = DisplayString
_CpmAcSnmpTrapDestAddr1_Object = MibScalar
cpmAcSnmpTrapDestAddr1 = _CpmAcSnmpTrapDestAddr1_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 1, 3, 1, 1),
    _CpmAcSnmpTrapDestAddr1_Type()
)
cpmAcSnmpTrapDestAddr1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpmAcSnmpTrapDestAddr1.setStatus("current")
_CpmAcSnmpTrapDestAddr2_Type = DisplayString
_CpmAcSnmpTrapDestAddr2_Object = MibScalar
cpmAcSnmpTrapDestAddr2 = _CpmAcSnmpTrapDestAddr2_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 1, 3, 1, 2),
    _CpmAcSnmpTrapDestAddr2_Type()
)
cpmAcSnmpTrapDestAddr2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpmAcSnmpTrapDestAddr2.setStatus("current")
_CpmAcEmail_ObjectIdentity = ObjectIdentity
cpmAcEmail = _CpmAcEmail_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35774, 2, 1, 3, 2)
)
_CpmAcEmailFromAddress_Type = DisplayString
_CpmAcEmailFromAddress_Object = MibScalar
cpmAcEmailFromAddress = _CpmAcEmailFromAddress_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 1, 3, 2, 1),
    _CpmAcEmailFromAddress_Type()
)
cpmAcEmailFromAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpmAcEmailFromAddress.setStatus("current")
_CpmAcEmailToAddress_Type = DisplayString
_CpmAcEmailToAddress_Object = MibScalar
cpmAcEmailToAddress = _CpmAcEmailToAddress_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 1, 3, 2, 2),
    _CpmAcEmailToAddress_Type()
)
cpmAcEmailToAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpmAcEmailToAddress.setStatus("current")
_CpmAcEmailServer_Type = DisplayString
_CpmAcEmailServer_Object = MibScalar
cpmAcEmailServer = _CpmAcEmailServer_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 1, 3, 2, 3),
    _CpmAcEmailServer_Type()
)
cpmAcEmailServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpmAcEmailServer.setStatus("current")
_CpmAcEmailPort_Type = DisplayString
_CpmAcEmailPort_Object = MibScalar
cpmAcEmailPort = _CpmAcEmailPort_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 1, 3, 2, 4),
    _CpmAcEmailPort_Type()
)
cpmAcEmailPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpmAcEmailPort.setStatus("current")
_CpmAcEmailAuthEnable_Type = DisplayString
_CpmAcEmailAuthEnable_Object = MibScalar
cpmAcEmailAuthEnable = _CpmAcEmailAuthEnable_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 1, 3, 2, 5),
    _CpmAcEmailAuthEnable_Type()
)
cpmAcEmailAuthEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpmAcEmailAuthEnable.setStatus("current")
_CpmAcEmailLogin_Type = DisplayString
_CpmAcEmailLogin_Object = MibScalar
cpmAcEmailLogin = _CpmAcEmailLogin_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 1, 3, 2, 6),
    _CpmAcEmailLogin_Type()
)
cpmAcEmailLogin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpmAcEmailLogin.setStatus("current")
_CpmAcEmailPassword_Type = DisplayString
_CpmAcEmailPassword_Object = MibScalar
cpmAcEmailPassword = _CpmAcEmailPassword_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 1, 3, 2, 7),
    _CpmAcEmailPassword_Type()
)
cpmAcEmailPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpmAcEmailPassword.setStatus("current")
_CpmAcSntp_ObjectIdentity = ObjectIdentity
cpmAcSntp = _CpmAcSntp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35774, 2, 1, 3, 3)
)
_CpmAcSntpServer_Type = DisplayString
_CpmAcSntpServer_Object = MibScalar
cpmAcSntpServer = _CpmAcSntpServer_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 1, 3, 3, 1),
    _CpmAcSntpServer_Type()
)
cpmAcSntpServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpmAcSntpServer.setStatus("current")
_CpmAcTelnet_ObjectIdentity = ObjectIdentity
cpmAcTelnet = _CpmAcTelnet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35774, 2, 1, 3, 4)
)
_CpmAcInfeed_ObjectIdentity = ObjectIdentity
cpmAcInfeed = _CpmAcInfeed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35774, 2, 1, 4)
)
_CpmAcInfLineToNeutVoltAve_Type = DisplayString
_CpmAcInfLineToNeutVoltAve_Object = MibScalar
cpmAcInfLineToNeutVoltAve = _CpmAcInfLineToNeutVoltAve_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 1, 4, 1),
    _CpmAcInfLineToNeutVoltAve_Type()
)
cpmAcInfLineToNeutVoltAve.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmAcInfLineToNeutVoltAve.setStatus("current")
if mibBuilder.loadTexts:
    cpmAcInfLineToNeutVoltAve.setUnits("Volts (rms)")
_CpmAcInfLineToLineVoltAve_Type = DisplayString
_CpmAcInfLineToLineVoltAve_Object = MibScalar
cpmAcInfLineToLineVoltAve = _CpmAcInfLineToLineVoltAve_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 1, 4, 2),
    _CpmAcInfLineToLineVoltAve_Type()
)
cpmAcInfLineToLineVoltAve.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmAcInfLineToLineVoltAve.setStatus("current")
if mibBuilder.loadTexts:
    cpmAcInfLineToLineVoltAve.setUnits("Volts (rms)")
_CpmAcInfLineCurrentAve_Type = DisplayString
_CpmAcInfLineCurrentAve_Object = MibScalar
cpmAcInfLineCurrentAve = _CpmAcInfLineCurrentAve_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 1, 4, 3),
    _CpmAcInfLineCurrentAve_Type()
)
cpmAcInfLineCurrentAve.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmAcInfLineCurrentAve.setStatus("current")
if mibBuilder.loadTexts:
    cpmAcInfLineCurrentAve.setUnits("Amps (rms)")
_CpmAcInfTotLineCurrDemand_Type = DisplayString
_CpmAcInfTotLineCurrDemand_Object = MibScalar
cpmAcInfTotLineCurrDemand = _CpmAcInfTotLineCurrDemand_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 1, 4, 4),
    _CpmAcInfTotLineCurrDemand_Type()
)
cpmAcInfTotLineCurrDemand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpmAcInfTotLineCurrDemand.setStatus("current")
if mibBuilder.loadTexts:
    cpmAcInfTotLineCurrDemand.setUnits("Amps (rms)")
_CpmAcInfTotLineCurrPeakDmd_Type = DisplayString
_CpmAcInfTotLineCurrPeakDmd_Object = MibScalar
cpmAcInfTotLineCurrPeakDmd = _CpmAcInfTotLineCurrPeakDmd_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 1, 4, 5),
    _CpmAcInfTotLineCurrPeakDmd_Type()
)
cpmAcInfTotLineCurrPeakDmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpmAcInfTotLineCurrPeakDmd.setStatus("current")
if mibBuilder.loadTexts:
    cpmAcInfTotLineCurrPeakDmd.setUnits("Amps (rms)")
_CpmAcInfDemandTime_Type = DisplayString
_CpmAcInfDemandTime_Object = MibScalar
cpmAcInfDemandTime = _CpmAcInfDemandTime_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 1, 4, 6),
    _CpmAcInfDemandTime_Type()
)
cpmAcInfDemandTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpmAcInfDemandTime.setStatus("current")
if mibBuilder.loadTexts:
    cpmAcInfDemandTime.setUnits("minutes")
_CpmAcInfTotalActivePower_Type = DisplayString
_CpmAcInfTotalActivePower_Object = MibScalar
cpmAcInfTotalActivePower = _CpmAcInfTotalActivePower_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 1, 4, 7),
    _CpmAcInfTotalActivePower_Type()
)
cpmAcInfTotalActivePower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmAcInfTotalActivePower.setStatus("current")
if mibBuilder.loadTexts:
    cpmAcInfTotalActivePower.setUnits("W")
_CpmAcInfPeakTotalActivePower_Type = DisplayString
_CpmAcInfPeakTotalActivePower_Object = MibScalar
cpmAcInfPeakTotalActivePower = _CpmAcInfPeakTotalActivePower_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 1, 4, 8),
    _CpmAcInfPeakTotalActivePower_Type()
)
cpmAcInfPeakTotalActivePower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpmAcInfPeakTotalActivePower.setStatus("current")
if mibBuilder.loadTexts:
    cpmAcInfPeakTotalActivePower.setUnits("W")
_CpmAcInfTotalActivePwrDemand_Type = DisplayString
_CpmAcInfTotalActivePwrDemand_Object = MibScalar
cpmAcInfTotalActivePwrDemand = _CpmAcInfTotalActivePwrDemand_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 1, 4, 9),
    _CpmAcInfTotalActivePwrDemand_Type()
)
cpmAcInfTotalActivePwrDemand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpmAcInfTotalActivePwrDemand.setStatus("current")
if mibBuilder.loadTexts:
    cpmAcInfTotalActivePwrDemand.setUnits("W per demand interval")
_CpmAcInfPeakTotActPwrDemand_Type = DisplayString
_CpmAcInfPeakTotActPwrDemand_Object = MibScalar
cpmAcInfPeakTotActPwrDemand = _CpmAcInfPeakTotActPwrDemand_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 1, 4, 10),
    _CpmAcInfPeakTotActPwrDemand_Type()
)
cpmAcInfPeakTotActPwrDemand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpmAcInfPeakTotActPwrDemand.setStatus("current")
if mibBuilder.loadTexts:
    cpmAcInfPeakTotActPwrDemand.setUnits("W per demand interval")
_CpmAcInfTotalReactivePower_Type = DisplayString
_CpmAcInfTotalReactivePower_Object = MibScalar
cpmAcInfTotalReactivePower = _CpmAcInfTotalReactivePower_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 1, 4, 11),
    _CpmAcInfTotalReactivePower_Type()
)
cpmAcInfTotalReactivePower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmAcInfTotalReactivePower.setStatus("current")
if mibBuilder.loadTexts:
    cpmAcInfTotalReactivePower.setUnits("var per demand interval")
_CpmAcInfTotReactivePwrDemand_Type = DisplayString
_CpmAcInfTotReactivePwrDemand_Object = MibScalar
cpmAcInfTotReactivePwrDemand = _CpmAcInfTotReactivePwrDemand_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 1, 4, 12),
    _CpmAcInfTotReactivePwrDemand_Type()
)
cpmAcInfTotReactivePwrDemand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpmAcInfTotReactivePwrDemand.setStatus("current")
if mibBuilder.loadTexts:
    cpmAcInfTotReactivePwrDemand.setUnits("var per demand interval")
_CpmAcInfPeakTotReactPwrDmd_Type = DisplayString
_CpmAcInfPeakTotReactPwrDmd_Object = MibScalar
cpmAcInfPeakTotReactPwrDmd = _CpmAcInfPeakTotReactPwrDmd_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 1, 4, 13),
    _CpmAcInfPeakTotReactPwrDmd_Type()
)
cpmAcInfPeakTotReactPwrDmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpmAcInfPeakTotReactPwrDmd.setStatus("current")
if mibBuilder.loadTexts:
    cpmAcInfPeakTotReactPwrDmd.setUnits("var per demand interval")
_CpmAcInfTotalApparentPower_Type = DisplayString
_CpmAcInfTotalApparentPower_Object = MibScalar
cpmAcInfTotalApparentPower = _CpmAcInfTotalApparentPower_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 1, 4, 14),
    _CpmAcInfTotalApparentPower_Type()
)
cpmAcInfTotalApparentPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmAcInfTotalApparentPower.setStatus("current")
if mibBuilder.loadTexts:
    cpmAcInfTotalApparentPower.setUnits("VA")
_CpmAcInfTotApparentPwrDemand_Type = DisplayString
_CpmAcInfTotApparentPwrDemand_Object = MibScalar
cpmAcInfTotApparentPwrDemand = _CpmAcInfTotApparentPwrDemand_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 1, 4, 15),
    _CpmAcInfTotApparentPwrDemand_Type()
)
cpmAcInfTotApparentPwrDemand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpmAcInfTotApparentPwrDemand.setStatus("current")
if mibBuilder.loadTexts:
    cpmAcInfTotApparentPwrDemand.setUnits("VA per demand interval")
_CpmAcInfPeakTotApparPwrDmd_Type = DisplayString
_CpmAcInfPeakTotApparPwrDmd_Object = MibScalar
cpmAcInfPeakTotApparPwrDmd = _CpmAcInfPeakTotApparPwrDmd_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 1, 4, 16),
    _CpmAcInfPeakTotApparPwrDmd_Type()
)
cpmAcInfPeakTotApparPwrDmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpmAcInfPeakTotApparPwrDmd.setStatus("current")
if mibBuilder.loadTexts:
    cpmAcInfPeakTotApparPwrDmd.setUnits("VA per demand interval")
_CpmAcInfTotalPowerFactor_Type = DisplayString
_CpmAcInfTotalPowerFactor_Object = MibScalar
cpmAcInfTotalPowerFactor = _CpmAcInfTotalPowerFactor_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 1, 4, 17),
    _CpmAcInfTotalPowerFactor_Type()
)
cpmAcInfTotalPowerFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmAcInfTotalPowerFactor.setStatus("current")
_CpmAcInfFrequency_Type = DisplayString
_CpmAcInfFrequency_Object = MibScalar
cpmAcInfFrequency = _CpmAcInfFrequency_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 1, 4, 18),
    _CpmAcInfFrequency_Type()
)
cpmAcInfFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmAcInfFrequency.setStatus("current")
if mibBuilder.loadTexts:
    cpmAcInfFrequency.setUnits("Hz")
_CpmAcInfTotalEnergy_Type = DisplayString
_CpmAcInfTotalEnergy_Object = MibScalar
cpmAcInfTotalEnergy = _CpmAcInfTotalEnergy_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 1, 4, 19),
    _CpmAcInfTotalEnergy_Type()
)
cpmAcInfTotalEnergy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmAcInfTotalEnergy.setStatus("current")
if mibBuilder.loadTexts:
    cpmAcInfTotalEnergy.setUnits("kWh")
_CpmAcInfLineCurrentRating_Type = DisplayString
_CpmAcInfLineCurrentRating_Object = MibScalar
cpmAcInfLineCurrentRating = _CpmAcInfLineCurrentRating_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 1, 4, 20),
    _CpmAcInfLineCurrentRating_Type()
)
cpmAcInfLineCurrentRating.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpmAcInfLineCurrentRating.setStatus("current")
if mibBuilder.loadTexts:
    cpmAcInfLineCurrentRating.setUnits("amps (rms)")
_CpmAcInfMeasuredNeutralCurr_Type = DisplayString
_CpmAcInfMeasuredNeutralCurr_Object = MibScalar
cpmAcInfMeasuredNeutralCurr = _CpmAcInfMeasuredNeutralCurr_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 1, 4, 21),
    _CpmAcInfMeasuredNeutralCurr_Type()
)
cpmAcInfMeasuredNeutralCurr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmAcInfMeasuredNeutralCurr.setStatus("current")
if mibBuilder.loadTexts:
    cpmAcInfMeasuredNeutralCurr.setUnits("Amps (rms)")
_CpmAcInfFrequencyMin_Type = DisplayString
_CpmAcInfFrequencyMin_Object = MibScalar
cpmAcInfFrequencyMin = _CpmAcInfFrequencyMin_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 1, 4, 22),
    _CpmAcInfFrequencyMin_Type()
)
cpmAcInfFrequencyMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpmAcInfFrequencyMin.setStatus("current")
if mibBuilder.loadTexts:
    cpmAcInfFrequencyMin.setUnits("Hz")
_CpmAcInfFrequencyMax_Type = DisplayString
_CpmAcInfFrequencyMax_Object = MibScalar
cpmAcInfFrequencyMax = _CpmAcInfFrequencyMax_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 1, 4, 23),
    _CpmAcInfFrequencyMax_Type()
)
cpmAcInfFrequencyMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpmAcInfFrequencyMax.setStatus("current")
if mibBuilder.loadTexts:
    cpmAcInfFrequencyMax.setUnits("Hz")
_CpmAcInfeedLine_Object = MibTable
cpmAcInfeedLine = _CpmAcInfeedLine_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 1, 5)
)
if mibBuilder.loadTexts:
    cpmAcInfeedLine.setStatus("current")
_CpmAcInfeedLineEntry_Object = MibTableRow
cpmAcInfeedLineEntry = _CpmAcInfeedLineEntry_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 1, 5, 1)
)
cpmAcInfeedLineEntry.setIndexNames(
    (0, "UEC-STARLINE-MIB", "cpmAcInfeedLineIndex"),
)
if mibBuilder.loadTexts:
    cpmAcInfeedLineEntry.setStatus("current")


class _CpmAcInfeedLineIndex_Type(Integer32):
    """Custom type cpmAcInfeedLineIndex based on Integer32"""
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
        *(("line1", 1),
          ("line2", 2),
          ("line3", 3),
          ("neutralC", 4),
          ("neutralM", 5))
    )


_CpmAcInfeedLineIndex_Type.__name__ = "Integer32"
_CpmAcInfeedLineIndex_Object = MibTableColumn
cpmAcInfeedLineIndex = _CpmAcInfeedLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 1, 5, 1, 1),
    _CpmAcInfeedLineIndex_Type()
)
cpmAcInfeedLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmAcInfeedLineIndex.setStatus("current")
_CpmAcInfLineCurrent_Type = DisplayString
_CpmAcInfLineCurrent_Object = MibTableColumn
cpmAcInfLineCurrent = _CpmAcInfLineCurrent_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 1, 5, 1, 3),
    _CpmAcInfLineCurrent_Type()
)
cpmAcInfLineCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmAcInfLineCurrent.setStatus("current")
if mibBuilder.loadTexts:
    cpmAcInfLineCurrent.setUnits("amps (rms)")
_CpmAcInfLineCurrentMin_Type = DisplayString
_CpmAcInfLineCurrentMin_Object = MibTableColumn
cpmAcInfLineCurrentMin = _CpmAcInfLineCurrentMin_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 1, 5, 1, 4),
    _CpmAcInfLineCurrentMin_Type()
)
cpmAcInfLineCurrentMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpmAcInfLineCurrentMin.setStatus("current")
if mibBuilder.loadTexts:
    cpmAcInfLineCurrentMin.setUnits("amps (rms)")
_CpmAcInfLineCurrentMax_Type = DisplayString
_CpmAcInfLineCurrentMax_Object = MibTableColumn
cpmAcInfLineCurrentMax = _CpmAcInfLineCurrentMax_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 1, 5, 1, 5),
    _CpmAcInfLineCurrentMax_Type()
)
cpmAcInfLineCurrentMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpmAcInfLineCurrentMax.setStatus("current")
if mibBuilder.loadTexts:
    cpmAcInfLineCurrentMax.setUnits("amps (rms)")
_CpmAcInfLineCurrRatPctOf_Type = DisplayString
_CpmAcInfLineCurrRatPctOf_Object = MibTableColumn
cpmAcInfLineCurrRatPctOf = _CpmAcInfLineCurrRatPctOf_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 1, 5, 1, 6),
    _CpmAcInfLineCurrRatPctOf_Type()
)
cpmAcInfLineCurrRatPctOf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmAcInfLineCurrRatPctOf.setStatus("current")
if mibBuilder.loadTexts:
    cpmAcInfLineCurrRatPctOf.setUnits("% of rated")
_CpmAcInfLineCurrMinAlarm_Type = DisplayString
_CpmAcInfLineCurrMinAlarm_Object = MibTableColumn
cpmAcInfLineCurrMinAlarm = _CpmAcInfLineCurrMinAlarm_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 1, 5, 1, 7),
    _CpmAcInfLineCurrMinAlarm_Type()
)
cpmAcInfLineCurrMinAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpmAcInfLineCurrMinAlarm.setStatus("current")
if mibBuilder.loadTexts:
    cpmAcInfLineCurrMinAlarm.setUnits("amps (RMS)")
_CpmAcInfLineCurrMaxAlarm_Type = DisplayString
_CpmAcInfLineCurrMaxAlarm_Object = MibTableColumn
cpmAcInfLineCurrMaxAlarm = _CpmAcInfLineCurrMaxAlarm_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 1, 5, 1, 8),
    _CpmAcInfLineCurrMaxAlarm_Type()
)
cpmAcInfLineCurrMaxAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpmAcInfLineCurrMaxAlarm.setStatus("current")
if mibBuilder.loadTexts:
    cpmAcInfLineCurrMaxAlarm.setUnits("amps (RMS)")
_CpmAcInfLineCurrDemand_Type = DisplayString
_CpmAcInfLineCurrDemand_Object = MibTableColumn
cpmAcInfLineCurrDemand = _CpmAcInfLineCurrDemand_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 1, 5, 1, 9),
    _CpmAcInfLineCurrDemand_Type()
)
cpmAcInfLineCurrDemand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpmAcInfLineCurrDemand.setStatus("current")
if mibBuilder.loadTexts:
    cpmAcInfLineCurrDemand.setUnits("amps per demand interval")
_CpmAcInfLineCurrPeakDmd_Type = DisplayString
_CpmAcInfLineCurrPeakDmd_Object = MibTableColumn
cpmAcInfLineCurrPeakDmd = _CpmAcInfLineCurrPeakDmd_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 1, 5, 1, 10),
    _CpmAcInfLineCurrPeakDmd_Type()
)
cpmAcInfLineCurrPeakDmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpmAcInfLineCurrPeakDmd.setStatus("current")
if mibBuilder.loadTexts:
    cpmAcInfLineCurrPeakDmd.setUnits("amps per demand interval")
_CpmAcInfeedPhase_Object = MibTable
cpmAcInfeedPhase = _CpmAcInfeedPhase_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 1, 6)
)
if mibBuilder.loadTexts:
    cpmAcInfeedPhase.setStatus("current")
_CpmAcInfeedPhaseEntry_Object = MibTableRow
cpmAcInfeedPhaseEntry = _CpmAcInfeedPhaseEntry_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 1, 6, 1)
)
cpmAcInfeedPhaseEntry.setIndexNames(
    (0, "UEC-STARLINE-MIB", "cpmAcInfeedPhaseIndex"),
)
if mibBuilder.loadTexts:
    cpmAcInfeedPhaseEntry.setStatus("current")


class _CpmAcInfeedPhaseIndex_Type(Integer32):
    """Custom type cpmAcInfeedPhaseIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("phaseA", 1),
          ("phaseB", 2),
          ("phaseC", 3))
    )


_CpmAcInfeedPhaseIndex_Type.__name__ = "Integer32"
_CpmAcInfeedPhaseIndex_Object = MibTableColumn
cpmAcInfeedPhaseIndex = _CpmAcInfeedPhaseIndex_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 1, 6, 1, 1),
    _CpmAcInfeedPhaseIndex_Type()
)
cpmAcInfeedPhaseIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmAcInfeedPhaseIndex.setStatus("current")
_CpmAcLineToNeutVoltage_Type = DisplayString
_CpmAcLineToNeutVoltage_Object = MibTableColumn
cpmAcLineToNeutVoltage = _CpmAcLineToNeutVoltage_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 1, 6, 1, 2),
    _CpmAcLineToNeutVoltage_Type()
)
cpmAcLineToNeutVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmAcLineToNeutVoltage.setStatus("current")
if mibBuilder.loadTexts:
    cpmAcLineToNeutVoltage.setUnits("volts (rms)")
_CpmAcLineToLineVoltage_Type = DisplayString
_CpmAcLineToLineVoltage_Object = MibTableColumn
cpmAcLineToLineVoltage = _CpmAcLineToLineVoltage_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 1, 6, 1, 3),
    _CpmAcLineToLineVoltage_Type()
)
cpmAcLineToLineVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmAcLineToLineVoltage.setStatus("current")
if mibBuilder.loadTexts:
    cpmAcLineToLineVoltage.setUnits("volts (rms)")
_CpmAcLineToLineVoltMin_Type = DisplayString
_CpmAcLineToLineVoltMin_Object = MibTableColumn
cpmAcLineToLineVoltMin = _CpmAcLineToLineVoltMin_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 1, 6, 1, 4),
    _CpmAcLineToLineVoltMin_Type()
)
cpmAcLineToLineVoltMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpmAcLineToLineVoltMin.setStatus("current")
if mibBuilder.loadTexts:
    cpmAcLineToLineVoltMin.setUnits("volts (rms)")
_CpmAcLineToLineVoltMax_Type = DisplayString
_CpmAcLineToLineVoltMax_Object = MibTableColumn
cpmAcLineToLineVoltMax = _CpmAcLineToLineVoltMax_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 1, 6, 1, 5),
    _CpmAcLineToLineVoltMax_Type()
)
cpmAcLineToLineVoltMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpmAcLineToLineVoltMax.setStatus("current")
if mibBuilder.loadTexts:
    cpmAcLineToLineVoltMax.setUnits("volts (rms)")
_CpmAcLinToLinVoltMinAlm_Type = DisplayString
_CpmAcLinToLinVoltMinAlm_Object = MibTableColumn
cpmAcLinToLinVoltMinAlm = _CpmAcLinToLinVoltMinAlm_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 1, 6, 1, 6),
    _CpmAcLinToLinVoltMinAlm_Type()
)
cpmAcLinToLinVoltMinAlm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpmAcLinToLinVoltMinAlm.setStatus("current")
if mibBuilder.loadTexts:
    cpmAcLinToLinVoltMinAlm.setUnits("volts (rms)")
_CpmAcLinToLinVoltMaxAlm_Type = DisplayString
_CpmAcLinToLinVoltMaxAlm_Object = MibTableColumn
cpmAcLinToLinVoltMaxAlm = _CpmAcLinToLinVoltMaxAlm_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 1, 6, 1, 7),
    _CpmAcLinToLinVoltMaxAlm_Type()
)
cpmAcLinToLinVoltMaxAlm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpmAcLinToLinVoltMaxAlm.setStatus("current")
if mibBuilder.loadTexts:
    cpmAcLinToLinVoltMaxAlm.setUnits("volts (rms)")
_CpmAcInfPhasePowerFactor_Type = DisplayString
_CpmAcInfPhasePowerFactor_Object = MibTableColumn
cpmAcInfPhasePowerFactor = _CpmAcInfPhasePowerFactor_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 1, 6, 1, 8),
    _CpmAcInfPhasePowerFactor_Type()
)
cpmAcInfPhasePowerFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmAcInfPhasePowerFactor.setStatus("current")
_CpmAcInfPhaseApparentPwr_Type = DisplayString
_CpmAcInfPhaseApparentPwr_Object = MibTableColumn
cpmAcInfPhaseApparentPwr = _CpmAcInfPhaseApparentPwr_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 1, 6, 1, 9),
    _CpmAcInfPhaseApparentPwr_Type()
)
cpmAcInfPhaseApparentPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmAcInfPhaseApparentPwr.setStatus("current")
if mibBuilder.loadTexts:
    cpmAcInfPhaseApparentPwr.setUnits("VA")
_CpmAcInfPhaseActivePower_Type = DisplayString
_CpmAcInfPhaseActivePower_Object = MibTableColumn
cpmAcInfPhaseActivePower = _CpmAcInfPhaseActivePower_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 1, 6, 1, 10),
    _CpmAcInfPhaseActivePower_Type()
)
cpmAcInfPhaseActivePower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmAcInfPhaseActivePower.setStatus("current")
if mibBuilder.loadTexts:
    cpmAcInfPhaseActivePower.setUnits("W")
_CpmAcInfPhasePeakActPwr_Type = DisplayString
_CpmAcInfPhasePeakActPwr_Object = MibTableColumn
cpmAcInfPhasePeakActPwr = _CpmAcInfPhasePeakActPwr_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 1, 6, 1, 11),
    _CpmAcInfPhasePeakActPwr_Type()
)
cpmAcInfPhasePeakActPwr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpmAcInfPhasePeakActPwr.setStatus("current")
if mibBuilder.loadTexts:
    cpmAcInfPhasePeakActPwr.setUnits("W")
_CpmAcInfPhaseReactivePwr_Type = DisplayString
_CpmAcInfPhaseReactivePwr_Object = MibTableColumn
cpmAcInfPhaseReactivePwr = _CpmAcInfPhaseReactivePwr_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 1, 6, 1, 12),
    _CpmAcInfPhaseReactivePwr_Type()
)
cpmAcInfPhaseReactivePwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmAcInfPhaseReactivePwr.setStatus("current")
if mibBuilder.loadTexts:
    cpmAcInfPhaseReactivePwr.setUnits("var")
_CpmAcInfPhaseEnergy_Type = DisplayString
_CpmAcInfPhaseEnergy_Object = MibTableColumn
cpmAcInfPhaseEnergy = _CpmAcInfPhaseEnergy_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 1, 6, 1, 13),
    _CpmAcInfPhaseEnergy_Type()
)
cpmAcInfPhaseEnergy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmAcInfPhaseEnergy.setStatus("current")
if mibBuilder.loadTexts:
    cpmAcInfPhaseEnergy.setUnits("kWh")
_CpmAcLineToNeutVoltMin_Type = DisplayString
_CpmAcLineToNeutVoltMin_Object = MibTableColumn
cpmAcLineToNeutVoltMin = _CpmAcLineToNeutVoltMin_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 1, 6, 1, 14),
    _CpmAcLineToNeutVoltMin_Type()
)
cpmAcLineToNeutVoltMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpmAcLineToNeutVoltMin.setStatus("current")
if mibBuilder.loadTexts:
    cpmAcLineToNeutVoltMin.setUnits("volts (rms)")
_CpmAcLineToNeutVoltMax_Type = DisplayString
_CpmAcLineToNeutVoltMax_Object = MibTableColumn
cpmAcLineToNeutVoltMax = _CpmAcLineToNeutVoltMax_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 1, 6, 1, 15),
    _CpmAcLineToNeutVoltMax_Type()
)
cpmAcLineToNeutVoltMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpmAcLineToNeutVoltMax.setStatus("current")
if mibBuilder.loadTexts:
    cpmAcLineToNeutVoltMax.setUnits("volts (rms)")
_CpmAcLinToNeutVoltMinAlm_Type = DisplayString
_CpmAcLinToNeutVoltMinAlm_Object = MibTableColumn
cpmAcLinToNeutVoltMinAlm = _CpmAcLinToNeutVoltMinAlm_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 1, 6, 1, 16),
    _CpmAcLinToNeutVoltMinAlm_Type()
)
cpmAcLinToNeutVoltMinAlm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpmAcLinToNeutVoltMinAlm.setStatus("current")
if mibBuilder.loadTexts:
    cpmAcLinToNeutVoltMinAlm.setUnits("volts (rms)")
_CpmAcLinToNeutVoltMaxAlm_Type = DisplayString
_CpmAcLinToNeutVoltMaxAlm_Object = MibTableColumn
cpmAcLinToNeutVoltMaxAlm = _CpmAcLinToNeutVoltMaxAlm_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 1, 6, 1, 17),
    _CpmAcLinToNeutVoltMaxAlm_Type()
)
cpmAcLinToNeutVoltMaxAlm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpmAcLinToNeutVoltMaxAlm.setStatus("current")
if mibBuilder.loadTexts:
    cpmAcLinToNeutVoltMaxAlm.setUnits("volts (rms)")
_CpmAcOutlet_Object = MibTable
cpmAcOutlet = _CpmAcOutlet_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 1, 7)
)
if mibBuilder.loadTexts:
    cpmAcOutlet.setStatus("current")
_CpmAcOutletEntry_Object = MibTableRow
cpmAcOutletEntry = _CpmAcOutletEntry_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 1, 7, 1)
)
cpmAcOutletEntry.setIndexNames(
    (0, "UEC-STARLINE-MIB", "cpmAcOutletIndex"),
)
if mibBuilder.loadTexts:
    cpmAcOutletEntry.setStatus("current")


class _CpmAcOutletIndex_Type(Integer32):
    """Custom type cpmAcOutletIndex based on Integer32"""
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
        *(("outlet1", 1),
          ("outlet2", 2),
          ("outlet3", 3),
          ("outlet4", 4),
          ("outlet5", 5),
          ("outlet6", 6))
    )


_CpmAcOutletIndex_Type.__name__ = "Integer32"
_CpmAcOutletIndex_Object = MibTableColumn
cpmAcOutletIndex = _CpmAcOutletIndex_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 1, 7, 1, 1),
    _CpmAcOutletIndex_Type()
)
cpmAcOutletIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmAcOutletIndex.setStatus("current")
_CpmAcOutletId_Type = DisplayString
_CpmAcOutletId_Object = MibTableColumn
cpmAcOutletId = _CpmAcOutletId_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 1, 7, 1, 2),
    _CpmAcOutletId_Type()
)
cpmAcOutletId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpmAcOutletId.setStatus("current")
_CpmAcOtlLineCurrRating_Type = DisplayString
_CpmAcOtlLineCurrRating_Object = MibTableColumn
cpmAcOtlLineCurrRating = _CpmAcOtlLineCurrRating_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 1, 7, 1, 3),
    _CpmAcOtlLineCurrRating_Type()
)
cpmAcOtlLineCurrRating.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmAcOtlLineCurrRating.setStatus("current")
if mibBuilder.loadTexts:
    cpmAcOtlLineCurrRating.setUnits("amps (rms)")
_CpmAcOtlDemandTime_Type = DisplayString
_CpmAcOtlDemandTime_Object = MibTableColumn
cpmAcOtlDemandTime = _CpmAcOtlDemandTime_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 1, 7, 1, 4),
    _CpmAcOtlDemandTime_Type()
)
cpmAcOtlDemandTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpmAcOtlDemandTime.setStatus("current")
if mibBuilder.loadTexts:
    cpmAcOtlDemandTime.setUnits("minutes")
_CpmAcOtlTotalActivePower_Type = DisplayString
_CpmAcOtlTotalActivePower_Object = MibTableColumn
cpmAcOtlTotalActivePower = _CpmAcOtlTotalActivePower_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 1, 7, 1, 5),
    _CpmAcOtlTotalActivePower_Type()
)
cpmAcOtlTotalActivePower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmAcOtlTotalActivePower.setStatus("current")
if mibBuilder.loadTexts:
    cpmAcOtlTotalActivePower.setUnits("W")
_CpmAcOtlPeakTotActivePwr_Type = DisplayString
_CpmAcOtlPeakTotActivePwr_Object = MibTableColumn
cpmAcOtlPeakTotActivePwr = _CpmAcOtlPeakTotActivePwr_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 1, 7, 1, 6),
    _CpmAcOtlPeakTotActivePwr_Type()
)
cpmAcOtlPeakTotActivePwr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpmAcOtlPeakTotActivePwr.setStatus("current")
if mibBuilder.loadTexts:
    cpmAcOtlPeakTotActivePwr.setUnits("W")
_CpmAcOtlTotalReactivePwr_Type = DisplayString
_CpmAcOtlTotalReactivePwr_Object = MibTableColumn
cpmAcOtlTotalReactivePwr = _CpmAcOtlTotalReactivePwr_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 1, 7, 1, 7),
    _CpmAcOtlTotalReactivePwr_Type()
)
cpmAcOtlTotalReactivePwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmAcOtlTotalReactivePwr.setStatus("current")
if mibBuilder.loadTexts:
    cpmAcOtlTotalReactivePwr.setUnits("var")
_CpmAcOtlTotalApparentPwr_Type = DisplayString
_CpmAcOtlTotalApparentPwr_Object = MibTableColumn
cpmAcOtlTotalApparentPwr = _CpmAcOtlTotalApparentPwr_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 1, 7, 1, 8),
    _CpmAcOtlTotalApparentPwr_Type()
)
cpmAcOtlTotalApparentPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmAcOtlTotalApparentPwr.setStatus("current")
if mibBuilder.loadTexts:
    cpmAcOtlTotalApparentPwr.setUnits("VA")
_CpmAcOtlTotalPowerFactor_Type = DisplayString
_CpmAcOtlTotalPowerFactor_Object = MibTableColumn
cpmAcOtlTotalPowerFactor = _CpmAcOtlTotalPowerFactor_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 1, 7, 1, 9),
    _CpmAcOtlTotalPowerFactor_Type()
)
cpmAcOtlTotalPowerFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmAcOtlTotalPowerFactor.setStatus("current")
_CpmAcOtlTotalEnergy_Type = DisplayString
_CpmAcOtlTotalEnergy_Object = MibTableColumn
cpmAcOtlTotalEnergy = _CpmAcOtlTotalEnergy_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 1, 7, 1, 10),
    _CpmAcOtlTotalEnergy_Type()
)
cpmAcOtlTotalEnergy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmAcOtlTotalEnergy.setStatus("current")
if mibBuilder.loadTexts:
    cpmAcOtlTotalEnergy.setUnits("kWh")
_CpmAcOtlCurrentMinAlarm_Type = DisplayString
_CpmAcOtlCurrentMinAlarm_Object = MibTableColumn
cpmAcOtlCurrentMinAlarm = _CpmAcOtlCurrentMinAlarm_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 1, 7, 1, 11),
    _CpmAcOtlCurrentMinAlarm_Type()
)
cpmAcOtlCurrentMinAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpmAcOtlCurrentMinAlarm.setStatus("current")
if mibBuilder.loadTexts:
    cpmAcOtlCurrentMinAlarm.setUnits("amps (rms)")
_CpmAcOtlCurrentMaxAlarm_Type = DisplayString
_CpmAcOtlCurrentMaxAlarm_Object = MibTableColumn
cpmAcOtlCurrentMaxAlarm = _CpmAcOtlCurrentMaxAlarm_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 1, 7, 1, 12),
    _CpmAcOtlCurrentMaxAlarm_Type()
)
cpmAcOtlCurrentMaxAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpmAcOtlCurrentMaxAlarm.setStatus("current")
if mibBuilder.loadTexts:
    cpmAcOtlCurrentMaxAlarm.setUnits("amps (rms)")
_CpmAcOutletLine_Object = MibTable
cpmAcOutletLine = _CpmAcOutletLine_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 1, 8)
)
if mibBuilder.loadTexts:
    cpmAcOutletLine.setStatus("current")
_CpmAcOutletLineEntry_Object = MibTableRow
cpmAcOutletLineEntry = _CpmAcOutletLineEntry_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 1, 8, 1)
)
cpmAcOutletLineEntry.setIndexNames(
    (0, "UEC-STARLINE-MIB", "cpmAcOutletOutletIndex"),
    (0, "UEC-STARLINE-MIB", "cpmAcOutletLineIndex"),
)
if mibBuilder.loadTexts:
    cpmAcOutletLineEntry.setStatus("current")


class _CpmAcOutletOutletIndex_Type(Integer32):
    """Custom type cpmAcOutletOutletIndex based on Integer32"""
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
        *(("outlet1", 1),
          ("outlet2", 2),
          ("outlet3", 3),
          ("outlet4", 4),
          ("outlet5", 5),
          ("outlet6", 6))
    )


_CpmAcOutletOutletIndex_Type.__name__ = "Integer32"
_CpmAcOutletOutletIndex_Object = MibTableColumn
cpmAcOutletOutletIndex = _CpmAcOutletOutletIndex_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 1, 8, 1, 1),
    _CpmAcOutletOutletIndex_Type()
)
cpmAcOutletOutletIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmAcOutletOutletIndex.setStatus("current")


class _CpmAcOutletLineIndex_Type(Integer32):
    """Custom type cpmAcOutletLineIndex based on Integer32"""
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
        *(("line1", 1),
          ("line2", 2),
          ("line3", 3),
          ("neutral", 4))
    )


_CpmAcOutletLineIndex_Type.__name__ = "Integer32"
_CpmAcOutletLineIndex_Object = MibTableColumn
cpmAcOutletLineIndex = _CpmAcOutletLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 1, 8, 1, 2),
    _CpmAcOutletLineIndex_Type()
)
cpmAcOutletLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmAcOutletLineIndex.setStatus("current")
_CpmAcOtlPhaseId_Type = DisplayString
_CpmAcOtlPhaseId_Object = MibTableColumn
cpmAcOtlPhaseId = _CpmAcOtlPhaseId_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 1, 8, 1, 3),
    _CpmAcOtlPhaseId_Type()
)
cpmAcOtlPhaseId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpmAcOtlPhaseId.setStatus("current")
_CpmAcOtlLineCurrent_Type = DisplayString
_CpmAcOtlLineCurrent_Object = MibTableColumn
cpmAcOtlLineCurrent = _CpmAcOtlLineCurrent_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 1, 8, 1, 4),
    _CpmAcOtlLineCurrent_Type()
)
cpmAcOtlLineCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmAcOtlLineCurrent.setStatus("current")
if mibBuilder.loadTexts:
    cpmAcOtlLineCurrent.setUnits("amps (rms)")
_CpmAcOtlLineCurrRatPctOf_Type = DisplayString
_CpmAcOtlLineCurrRatPctOf_Object = MibTableColumn
cpmAcOtlLineCurrRatPctOf = _CpmAcOtlLineCurrRatPctOf_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 1, 8, 1, 5),
    _CpmAcOtlLineCurrRatPctOf_Type()
)
cpmAcOtlLineCurrRatPctOf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmAcOtlLineCurrRatPctOf.setStatus("current")
if mibBuilder.loadTexts:
    cpmAcOtlLineCurrRatPctOf.setUnits("% of rated")
_CpmAcOtlLineCurrDemand_Type = DisplayString
_CpmAcOtlLineCurrDemand_Object = MibTableColumn
cpmAcOtlLineCurrDemand = _CpmAcOtlLineCurrDemand_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 1, 8, 1, 6),
    _CpmAcOtlLineCurrDemand_Type()
)
cpmAcOtlLineCurrDemand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpmAcOtlLineCurrDemand.setStatus("current")
if mibBuilder.loadTexts:
    cpmAcOtlLineCurrDemand.setUnits("amps (rms) per demand interval")
_CpmAcOtlLineCurrPeakDmd_Type = DisplayString
_CpmAcOtlLineCurrPeakDmd_Object = MibTableColumn
cpmAcOtlLineCurrPeakDmd = _CpmAcOtlLineCurrPeakDmd_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 1, 8, 1, 7),
    _CpmAcOtlLineCurrPeakDmd_Type()
)
cpmAcOtlLineCurrPeakDmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpmAcOtlLineCurrPeakDmd.setStatus("current")
if mibBuilder.loadTexts:
    cpmAcOtlLineCurrPeakDmd.setUnits("amps (rms) per demand interval")
_CpmAcOtlLineCurrentMin_Type = DisplayString
_CpmAcOtlLineCurrentMin_Object = MibTableColumn
cpmAcOtlLineCurrentMin = _CpmAcOtlLineCurrentMin_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 1, 8, 1, 8),
    _CpmAcOtlLineCurrentMin_Type()
)
cpmAcOtlLineCurrentMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpmAcOtlLineCurrentMin.setStatus("current")
if mibBuilder.loadTexts:
    cpmAcOtlLineCurrentMin.setUnits("amps (rms) per demand interval")
_CpmAcOtlLineCurrentMax_Type = DisplayString
_CpmAcOtlLineCurrentMax_Object = MibTableColumn
cpmAcOtlLineCurrentMax = _CpmAcOtlLineCurrentMax_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 1, 8, 1, 9),
    _CpmAcOtlLineCurrentMax_Type()
)
cpmAcOtlLineCurrentMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpmAcOtlLineCurrentMax.setStatus("current")
if mibBuilder.loadTexts:
    cpmAcOtlLineCurrentMax.setUnits("amps (rms) per demand interval")
_CpmAcAlarms_ObjectIdentity = ObjectIdentity
cpmAcAlarms = _CpmAcAlarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35774, 2, 1, 9)
)
_CpmAcInfeedAlarmStatus_Type = DisplayString
_CpmAcInfeedAlarmStatus_Object = MibScalar
cpmAcInfeedAlarmStatus = _CpmAcInfeedAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 1, 9, 1),
    _CpmAcInfeedAlarmStatus_Type()
)
cpmAcInfeedAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmAcInfeedAlarmStatus.setStatus("current")
_CpmAcOutletAlarmStatus_Type = DisplayString
_CpmAcOutletAlarmStatus_Object = MibScalar
cpmAcOutletAlarmStatus = _CpmAcOutletAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 1, 9, 2),
    _CpmAcOutletAlarmStatus_Type()
)
cpmAcOutletAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmAcOutletAlarmStatus.setStatus("current")
_CpmAcOutletAlarmStatus2_Type = DisplayString
_CpmAcOutletAlarmStatus2_Object = MibScalar
cpmAcOutletAlarmStatus2 = _CpmAcOutletAlarmStatus2_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 1, 9, 3),
    _CpmAcOutletAlarmStatus2_Type()
)
cpmAcOutletAlarmStatus2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmAcOutletAlarmStatus2.setStatus("current")
_CpmAcTempAlarmStatus_Type = DisplayString
_CpmAcTempAlarmStatus_Object = MibScalar
cpmAcTempAlarmStatus = _CpmAcTempAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 1, 9, 4),
    _CpmAcTempAlarmStatus_Type()
)
cpmAcTempAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmAcTempAlarmStatus.setStatus("current")
_CpmAcDiagnostics_ObjectIdentity = ObjectIdentity
cpmAcDiagnostics = _CpmAcDiagnostics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35774, 2, 1, 10)
)
_CpmAcFirstErrorMessage_Type = DisplayString
_CpmAcFirstErrorMessage_Object = MibScalar
cpmAcFirstErrorMessage = _CpmAcFirstErrorMessage_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 1, 10, 1),
    _CpmAcFirstErrorMessage_Type()
)
cpmAcFirstErrorMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmAcFirstErrorMessage.setStatus("current")
_CpmAcLastErrorMessage_Type = DisplayString
_CpmAcLastErrorMessage_Object = MibScalar
cpmAcLastErrorMessage = _CpmAcLastErrorMessage_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 1, 10, 2),
    _CpmAcLastErrorMessage_Type()
)
cpmAcLastErrorMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmAcLastErrorMessage.setStatus("current")
_CpmAcTempMonitor_ObjectIdentity = ObjectIdentity
cpmAcTempMonitor = _CpmAcTempMonitor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35774, 2, 1, 11)
)
_CpmAcEnclosureTemp_Type = DisplayString
_CpmAcEnclosureTemp_Object = MibScalar
cpmAcEnclosureTemp = _CpmAcEnclosureTemp_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 1, 11, 1),
    _CpmAcEnclosureTemp_Type()
)
cpmAcEnclosureTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmAcEnclosureTemp.setStatus("current")
if mibBuilder.loadTexts:
    cpmAcEnclosureTemp.setUnits("degrees")
_CpmAcEnclosureTempMax_Type = DisplayString
_CpmAcEnclosureTempMax_Object = MibScalar
cpmAcEnclosureTempMax = _CpmAcEnclosureTempMax_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 1, 11, 2),
    _CpmAcEnclosureTempMax_Type()
)
cpmAcEnclosureTempMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpmAcEnclosureTempMax.setStatus("current")
if mibBuilder.loadTexts:
    cpmAcEnclosureTempMax.setUnits("degrees")
_CpmAcEncSysMaxTempAlmThr_Type = DisplayString
_CpmAcEncSysMaxTempAlmThr_Object = MibScalar
cpmAcEncSysMaxTempAlmThr = _CpmAcEncSysMaxTempAlmThr_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 1, 11, 3),
    _CpmAcEncSysMaxTempAlmThr_Type()
)
cpmAcEncSysMaxTempAlmThr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmAcEncSysMaxTempAlmThr.setStatus("current")
if mibBuilder.loadTexts:
    cpmAcEncSysMaxTempAlmThr.setUnits("degrees")
_CpmAcEncUsrMaxTempAlmThr_Type = DisplayString
_CpmAcEncUsrMaxTempAlmThr_Object = MibScalar
cpmAcEncUsrMaxTempAlmThr = _CpmAcEncUsrMaxTempAlmThr_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 1, 11, 4),
    _CpmAcEncUsrMaxTempAlmThr_Type()
)
cpmAcEncUsrMaxTempAlmThr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpmAcEncUsrMaxTempAlmThr.setStatus("current")
if mibBuilder.loadTexts:
    cpmAcEncUsrMaxTempAlmThr.setUnits("degrees")
_CpmAcBatVoltMinAlmThr_Type = DisplayString
_CpmAcBatVoltMinAlmThr_Object = MibScalar
cpmAcBatVoltMinAlmThr = _CpmAcBatVoltMinAlmThr_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 1, 11, 5),
    _CpmAcBatVoltMinAlmThr_Type()
)
cpmAcBatVoltMinAlmThr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmAcBatVoltMinAlmThr.setStatus("current")
if mibBuilder.loadTexts:
    cpmAcBatVoltMinAlmThr.setUnits("volts")
_CpmAcTempNode_Object = MibTable
cpmAcTempNode = _CpmAcTempNode_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 1, 12)
)
if mibBuilder.loadTexts:
    cpmAcTempNode.setStatus("current")
_CpmAcTempNodeEntry_Object = MibTableRow
cpmAcTempNodeEntry = _CpmAcTempNodeEntry_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 1, 12, 1)
)
cpmAcTempNodeEntry.setIndexNames(
    (0, "UEC-STARLINE-MIB", "cpmAcNodeIndex"),
)
if mibBuilder.loadTexts:
    cpmAcTempNodeEntry.setStatus("current")


class _CpmAcNodeIndex_Type(Integer32):
    """Custom type cpmAcNodeIndex based on Integer32"""
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
        *(("tempNode1", 1),
          ("tempNode2", 2),
          ("tempNode3", 3),
          ("tempNode4", 4))
    )


_CpmAcNodeIndex_Type.__name__ = "Integer32"
_CpmAcNodeIndex_Object = MibTableColumn
cpmAcNodeIndex = _CpmAcNodeIndex_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 1, 12, 1, 1),
    _CpmAcNodeIndex_Type()
)
cpmAcNodeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmAcNodeIndex.setStatus("current")
_CpmAcNodeId_Type = DisplayString
_CpmAcNodeId_Object = MibTableColumn
cpmAcNodeId = _CpmAcNodeId_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 1, 12, 1, 2),
    _CpmAcNodeId_Type()
)
cpmAcNodeId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpmAcNodeId.setStatus("current")
_CpmAcNodeTemperature_Type = DisplayString
_CpmAcNodeTemperature_Object = MibTableColumn
cpmAcNodeTemperature = _CpmAcNodeTemperature_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 1, 12, 1, 3),
    _CpmAcNodeTemperature_Type()
)
cpmAcNodeTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmAcNodeTemperature.setStatus("current")
if mibBuilder.loadTexts:
    cpmAcNodeTemperature.setUnits("degrees")
_CpmAcNodeTemperatureMax_Type = DisplayString
_CpmAcNodeTemperatureMax_Object = MibTableColumn
cpmAcNodeTemperatureMax = _CpmAcNodeTemperatureMax_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 1, 12, 1, 4),
    _CpmAcNodeTemperatureMax_Type()
)
cpmAcNodeTemperatureMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpmAcNodeTemperatureMax.setStatus("current")
if mibBuilder.loadTexts:
    cpmAcNodeTemperatureMax.setUnits("degrees")
_CpmAcNodeSysMaxAlmThresh_Type = DisplayString
_CpmAcNodeSysMaxAlmThresh_Object = MibTableColumn
cpmAcNodeSysMaxAlmThresh = _CpmAcNodeSysMaxAlmThresh_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 1, 12, 1, 5),
    _CpmAcNodeSysMaxAlmThresh_Type()
)
cpmAcNodeSysMaxAlmThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmAcNodeSysMaxAlmThresh.setStatus("current")
if mibBuilder.loadTexts:
    cpmAcNodeSysMaxAlmThresh.setUnits("degrees")
_CpmAcNodeUsrMaxAlmThresh_Type = DisplayString
_CpmAcNodeUsrMaxAlmThresh_Object = MibTableColumn
cpmAcNodeUsrMaxAlmThresh = _CpmAcNodeUsrMaxAlmThresh_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 1, 12, 1, 6),
    _CpmAcNodeUsrMaxAlmThresh_Type()
)
cpmAcNodeUsrMaxAlmThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpmAcNodeUsrMaxAlmThresh.setStatus("current")
if mibBuilder.loadTexts:
    cpmAcNodeUsrMaxAlmThresh.setUnits("degrees")
_CpmAcNodeBatteryVoltage_Type = DisplayString
_CpmAcNodeBatteryVoltage_Object = MibTableColumn
cpmAcNodeBatteryVoltage = _CpmAcNodeBatteryVoltage_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 1, 12, 1, 7),
    _CpmAcNodeBatteryVoltage_Type()
)
cpmAcNodeBatteryVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmAcNodeBatteryVoltage.setStatus("current")
if mibBuilder.loadTexts:
    cpmAcNodeBatteryVoltage.setUnits("volts")
_CpmAcNotifications_ObjectIdentity = ObjectIdentity
cpmAcNotifications = _CpmAcNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35774, 2, 1, 50)
)
_CpmAcEvents_ObjectIdentity = ObjectIdentity
cpmAcEvents = _CpmAcEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35774, 2, 1, 50, 0)
)
_CpmDcMeter_ObjectIdentity = ObjectIdentity
cpmDcMeter = _CpmDcMeter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35774, 2, 2)
)
_CpmDcGeneral_ObjectIdentity = ObjectIdentity
cpmDcGeneral = _CpmDcGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35774, 2, 2, 1)
)
_CpmDcDeviceName_Type = DisplayString
_CpmDcDeviceName_Object = MibScalar
cpmDcDeviceName = _CpmDcDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 2, 1, 1),
    _CpmDcDeviceName_Type()
)
cpmDcDeviceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpmDcDeviceName.setStatus("current")
_CpmDcDeviceLocation_Type = DisplayString
_CpmDcDeviceLocation_Object = MibScalar
cpmDcDeviceLocation = _CpmDcDeviceLocation_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 2, 1, 2),
    _CpmDcDeviceLocation_Type()
)
cpmDcDeviceLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpmDcDeviceLocation.setStatus("current")
_CpmDcDeviceId_Type = DisplayString
_CpmDcDeviceId_Object = MibScalar
cpmDcDeviceId = _CpmDcDeviceId_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 2, 1, 3),
    _CpmDcDeviceId_Type()
)
cpmDcDeviceId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpmDcDeviceId.setStatus("current")
_CpmDcModelNumber_Type = DisplayString
_CpmDcModelNumber_Object = MibScalar
cpmDcModelNumber = _CpmDcModelNumber_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 2, 1, 4),
    _CpmDcModelNumber_Type()
)
cpmDcModelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmDcModelNumber.setStatus("current")
_CpmDcSerialNumber_Type = DisplayString
_CpmDcSerialNumber_Object = MibScalar
cpmDcSerialNumber = _CpmDcSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 2, 1, 5),
    _CpmDcSerialNumber_Type()
)
cpmDcSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmDcSerialNumber.setStatus("current")
_CpmDcCatalogNumber_Type = DisplayString
_CpmDcCatalogNumber_Object = MibScalar
cpmDcCatalogNumber = _CpmDcCatalogNumber_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 2, 1, 6),
    _CpmDcCatalogNumber_Type()
)
cpmDcCatalogNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmDcCatalogNumber.setStatus("current")
_CpmDcFirmwareVersion_Type = DisplayString
_CpmDcFirmwareVersion_Object = MibScalar
cpmDcFirmwareVersion = _CpmDcFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 2, 1, 7),
    _CpmDcFirmwareVersion_Type()
)
cpmDcFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmDcFirmwareVersion.setStatus("current")
_CpmDcEnergyReset_Type = DisplayString
_CpmDcEnergyReset_Object = MibScalar
cpmDcEnergyReset = _CpmDcEnergyReset_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 2, 1, 8),
    _CpmDcEnergyReset_Type()
)
cpmDcEnergyReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpmDcEnergyReset.setStatus("current")
_CpmDcInterfaces_ObjectIdentity = ObjectIdentity
cpmDcInterfaces = _CpmDcInterfaces_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35774, 2, 2, 2)
)
_CpmDcEthernet_ObjectIdentity = ObjectIdentity
cpmDcEthernet = _CpmDcEthernet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35774, 2, 2, 2, 1)
)
_CpmDcEnetMacAddress_Type = DisplayString
_CpmDcEnetMacAddress_Object = MibScalar
cpmDcEnetMacAddress = _CpmDcEnetMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 2, 2, 1, 1),
    _CpmDcEnetMacAddress_Type()
)
cpmDcEnetMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmDcEnetMacAddress.setStatus("current")
_CpmDcEnetIpAddress_Type = DisplayString
_CpmDcEnetIpAddress_Object = MibScalar
cpmDcEnetIpAddress = _CpmDcEnetIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 2, 2, 1, 2),
    _CpmDcEnetIpAddress_Type()
)
cpmDcEnetIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmDcEnetIpAddress.setStatus("current")
_CpmDcEnetIpNetmask_Type = DisplayString
_CpmDcEnetIpNetmask_Object = MibScalar
cpmDcEnetIpNetmask = _CpmDcEnetIpNetmask_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 2, 2, 1, 3),
    _CpmDcEnetIpNetmask_Type()
)
cpmDcEnetIpNetmask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmDcEnetIpNetmask.setStatus("current")
_CpmDcEnetIpGateway_Type = DisplayString
_CpmDcEnetIpGateway_Object = MibScalar
cpmDcEnetIpGateway = _CpmDcEnetIpGateway_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 2, 2, 1, 4),
    _CpmDcEnetIpGateway_Type()
)
cpmDcEnetIpGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmDcEnetIpGateway.setStatus("current")
_CpmDcEnetEnableDHCP_Type = DisplayString
_CpmDcEnetEnableDHCP_Object = MibScalar
cpmDcEnetEnableDHCP = _CpmDcEnetEnableDHCP_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 2, 2, 1, 5),
    _CpmDcEnetEnableDHCP_Type()
)
cpmDcEnetEnableDHCP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpmDcEnetEnableDHCP.setStatus("current")
_CpmDcEnetStaticIpAddress_Type = DisplayString
_CpmDcEnetStaticIpAddress_Object = MibScalar
cpmDcEnetStaticIpAddress = _CpmDcEnetStaticIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 2, 2, 1, 6),
    _CpmDcEnetStaticIpAddress_Type()
)
cpmDcEnetStaticIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpmDcEnetStaticIpAddress.setStatus("current")
_CpmDcEnetStaticIpNetmask_Type = DisplayString
_CpmDcEnetStaticIpNetmask_Object = MibScalar
cpmDcEnetStaticIpNetmask = _CpmDcEnetStaticIpNetmask_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 2, 2, 1, 7),
    _CpmDcEnetStaticIpNetmask_Type()
)
cpmDcEnetStaticIpNetmask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpmDcEnetStaticIpNetmask.setStatus("current")
_CpmDcEnetStaticIpGateway_Type = DisplayString
_CpmDcEnetStaticIpGateway_Object = MibScalar
cpmDcEnetStaticIpGateway = _CpmDcEnetStaticIpGateway_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 2, 2, 1, 8),
    _CpmDcEnetStaticIpGateway_Type()
)
cpmDcEnetStaticIpGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpmDcEnetStaticIpGateway.setStatus("current")
_CpmDcWifi_ObjectIdentity = ObjectIdentity
cpmDcWifi = _CpmDcWifi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35774, 2, 2, 2, 2)
)
_CpmDcWifiMacAddress_Type = DisplayString
_CpmDcWifiMacAddress_Object = MibScalar
cpmDcWifiMacAddress = _CpmDcWifiMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 2, 2, 2, 1),
    _CpmDcWifiMacAddress_Type()
)
cpmDcWifiMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmDcWifiMacAddress.setStatus("current")
_CpmDcWifiIpAddress_Type = DisplayString
_CpmDcWifiIpAddress_Object = MibScalar
cpmDcWifiIpAddress = _CpmDcWifiIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 2, 2, 2, 2),
    _CpmDcWifiIpAddress_Type()
)
cpmDcWifiIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmDcWifiIpAddress.setStatus("current")
_CpmDcWifiIpNetmask_Type = DisplayString
_CpmDcWifiIpNetmask_Object = MibScalar
cpmDcWifiIpNetmask = _CpmDcWifiIpNetmask_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 2, 2, 2, 3),
    _CpmDcWifiIpNetmask_Type()
)
cpmDcWifiIpNetmask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmDcWifiIpNetmask.setStatus("current")
_CpmDcWifiIpGateway_Type = DisplayString
_CpmDcWifiIpGateway_Object = MibScalar
cpmDcWifiIpGateway = _CpmDcWifiIpGateway_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 2, 2, 2, 4),
    _CpmDcWifiIpGateway_Type()
)
cpmDcWifiIpGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmDcWifiIpGateway.setStatus("current")
_CpmDcWifiEnableDHCP_Type = DisplayString
_CpmDcWifiEnableDHCP_Object = MibScalar
cpmDcWifiEnableDHCP = _CpmDcWifiEnableDHCP_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 2, 2, 2, 5),
    _CpmDcWifiEnableDHCP_Type()
)
cpmDcWifiEnableDHCP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpmDcWifiEnableDHCP.setStatus("current")
_CpmDcWifiStaticIpAddress_Type = DisplayString
_CpmDcWifiStaticIpAddress_Object = MibScalar
cpmDcWifiStaticIpAddress = _CpmDcWifiStaticIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 2, 2, 2, 6),
    _CpmDcWifiStaticIpAddress_Type()
)
cpmDcWifiStaticIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpmDcWifiStaticIpAddress.setStatus("current")
_CpmDcWifiStaticIpNetmask_Type = DisplayString
_CpmDcWifiStaticIpNetmask_Object = MibScalar
cpmDcWifiStaticIpNetmask = _CpmDcWifiStaticIpNetmask_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 2, 2, 2, 7),
    _CpmDcWifiStaticIpNetmask_Type()
)
cpmDcWifiStaticIpNetmask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpmDcWifiStaticIpNetmask.setStatus("current")
_CpmDcWifiStaticIpGateway_Type = DisplayString
_CpmDcWifiStaticIpGateway_Object = MibScalar
cpmDcWifiStaticIpGateway = _CpmDcWifiStaticIpGateway_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 2, 2, 2, 8),
    _CpmDcWifiStaticIpGateway_Type()
)
cpmDcWifiStaticIpGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpmDcWifiStaticIpGateway.setStatus("current")
_CpmDcWifiSSID_Type = DisplayString
_CpmDcWifiSSID_Object = MibScalar
cpmDcWifiSSID = _CpmDcWifiSSID_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 2, 2, 2, 9),
    _CpmDcWifiSSID_Type()
)
cpmDcWifiSSID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpmDcWifiSSID.setStatus("current")
_CpmDcWifiEncryptionType_Type = DisplayString
_CpmDcWifiEncryptionType_Object = MibScalar
cpmDcWifiEncryptionType = _CpmDcWifiEncryptionType_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 2, 2, 2, 10),
    _CpmDcWifiEncryptionType_Type()
)
cpmDcWifiEncryptionType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpmDcWifiEncryptionType.setStatus("current")
_CpmDcModbus_ObjectIdentity = ObjectIdentity
cpmDcModbus = _CpmDcModbus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35774, 2, 2, 2, 3)
)
_CpmDcModbusAddress_Type = DisplayString
_CpmDcModbusAddress_Object = MibScalar
cpmDcModbusAddress = _CpmDcModbusAddress_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 2, 2, 3, 1),
    _CpmDcModbusAddress_Type()
)
cpmDcModbusAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpmDcModbusAddress.setStatus("current")
_CpmDcModbusBaudRate_Type = DisplayString
_CpmDcModbusBaudRate_Object = MibScalar
cpmDcModbusBaudRate = _CpmDcModbusBaudRate_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 2, 2, 3, 2),
    _CpmDcModbusBaudRate_Type()
)
cpmDcModbusBaudRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpmDcModbusBaudRate.setStatus("current")
_CpmDcModbusStopBits_Type = DisplayString
_CpmDcModbusStopBits_Object = MibScalar
cpmDcModbusStopBits = _CpmDcModbusStopBits_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 2, 2, 3, 3),
    _CpmDcModbusStopBits_Type()
)
cpmDcModbusStopBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpmDcModbusStopBits.setStatus("current")
_CpmDcModbusParity_Type = DisplayString
_CpmDcModbusParity_Object = MibScalar
cpmDcModbusParity = _CpmDcModbusParity_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 2, 2, 3, 4),
    _CpmDcModbusParity_Type()
)
cpmDcModbusParity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpmDcModbusParity.setStatus("current")
_CpmDcDigitalIo_Object = MibTable
cpmDcDigitalIo = _CpmDcDigitalIo_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 2, 2, 4)
)
if mibBuilder.loadTexts:
    cpmDcDigitalIo.setStatus("current")
_CpmDcDigitalIoEntry_Object = MibTableRow
cpmDcDigitalIoEntry = _CpmDcDigitalIoEntry_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 2, 2, 4, 1)
)
cpmDcDigitalIoEntry.setIndexNames(
    (0, "UEC-STARLINE-MIB", "cpmDcDigitalIoIndex"),
)
if mibBuilder.loadTexts:
    cpmDcDigitalIoEntry.setStatus("current")


class _CpmDcDigitalIoIndex_Type(Integer32):
    """Custom type cpmDcDigitalIoIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("port1", 1),
          ("port2", 2))
    )


_CpmDcDigitalIoIndex_Type.__name__ = "Integer32"
_CpmDcDigitalIoIndex_Object = MibTableColumn
cpmDcDigitalIoIndex = _CpmDcDigitalIoIndex_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 2, 2, 4, 1, 1),
    _CpmDcDigitalIoIndex_Type()
)
cpmDcDigitalIoIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cpmDcDigitalIoIndex.setStatus("current")
_CpmDcDigitalIoName_Type = DisplayString
_CpmDcDigitalIoName_Object = MibTableColumn
cpmDcDigitalIoName = _CpmDcDigitalIoName_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 2, 2, 4, 1, 2),
    _CpmDcDigitalIoName_Type()
)
cpmDcDigitalIoName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpmDcDigitalIoName.setStatus("current")
_CpmDcDigitalIoValue_Type = DisplayString
_CpmDcDigitalIoValue_Object = MibTableColumn
cpmDcDigitalIoValue = _CpmDcDigitalIoValue_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 2, 2, 4, 1, 3),
    _CpmDcDigitalIoValue_Type()
)
cpmDcDigitalIoValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpmDcDigitalIoValue.setStatus("current")
_CpmDcDigitalIoDirection_Type = DisplayString
_CpmDcDigitalIoDirection_Object = MibTableColumn
cpmDcDigitalIoDirection = _CpmDcDigitalIoDirection_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 2, 2, 4, 1, 4),
    _CpmDcDigitalIoDirection_Type()
)
cpmDcDigitalIoDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpmDcDigitalIoDirection.setStatus("current")
_CpmDcDigitalIoLevel_Type = DisplayString
_CpmDcDigitalIoLevel_Object = MibTableColumn
cpmDcDigitalIoLevel = _CpmDcDigitalIoLevel_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 2, 2, 4, 1, 5),
    _CpmDcDigitalIoLevel_Type()
)
cpmDcDigitalIoLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpmDcDigitalIoLevel.setStatus("current")
_CpmDcDigitalIoAlarm_Type = DisplayString
_CpmDcDigitalIoAlarm_Object = MibTableColumn
cpmDcDigitalIoAlarm = _CpmDcDigitalIoAlarm_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 2, 2, 4, 1, 6),
    _CpmDcDigitalIoAlarm_Type()
)
cpmDcDigitalIoAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpmDcDigitalIoAlarm.setStatus("current")
_CpmDcAnalogIo_ObjectIdentity = ObjectIdentity
cpmDcAnalogIo = _CpmDcAnalogIo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35774, 2, 2, 2, 5)
)
_CpmDc4to20maPortName_Type = DisplayString
_CpmDc4to20maPortName_Object = MibScalar
cpmDc4to20maPortName = _CpmDc4to20maPortName_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 2, 2, 5, 1),
    _CpmDc4to20maPortName_Type()
)
cpmDc4to20maPortName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpmDc4to20maPortName.setStatus("current")
_CpmDc4to20maValue_Type = DisplayString
_CpmDc4to20maValue_Object = MibScalar
cpmDc4to20maValue = _CpmDc4to20maValue_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 2, 2, 5, 2),
    _CpmDc4to20maValue_Type()
)
cpmDc4to20maValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmDc4to20maValue.setStatus("current")
_CpmDcProtocols_ObjectIdentity = ObjectIdentity
cpmDcProtocols = _CpmDcProtocols_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35774, 2, 2, 3)
)
_CpmDcSnmp_ObjectIdentity = ObjectIdentity
cpmDcSnmp = _CpmDcSnmp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35774, 2, 2, 3, 1)
)
_CpmDcSnmpTrapDestAddr1_Type = DisplayString
_CpmDcSnmpTrapDestAddr1_Object = MibScalar
cpmDcSnmpTrapDestAddr1 = _CpmDcSnmpTrapDestAddr1_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 2, 3, 1, 1),
    _CpmDcSnmpTrapDestAddr1_Type()
)
cpmDcSnmpTrapDestAddr1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpmDcSnmpTrapDestAddr1.setStatus("current")
_CpmDcSnmpTrapDestAddr2_Type = DisplayString
_CpmDcSnmpTrapDestAddr2_Object = MibScalar
cpmDcSnmpTrapDestAddr2 = _CpmDcSnmpTrapDestAddr2_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 2, 3, 1, 2),
    _CpmDcSnmpTrapDestAddr2_Type()
)
cpmDcSnmpTrapDestAddr2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpmDcSnmpTrapDestAddr2.setStatus("current")
_CpmDcEmail_ObjectIdentity = ObjectIdentity
cpmDcEmail = _CpmDcEmail_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35774, 2, 2, 3, 2)
)
_CpmDcEmailFromAddress_Type = DisplayString
_CpmDcEmailFromAddress_Object = MibScalar
cpmDcEmailFromAddress = _CpmDcEmailFromAddress_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 2, 3, 2, 1),
    _CpmDcEmailFromAddress_Type()
)
cpmDcEmailFromAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpmDcEmailFromAddress.setStatus("current")
_CpmDcEmailToAddress_Type = DisplayString
_CpmDcEmailToAddress_Object = MibScalar
cpmDcEmailToAddress = _CpmDcEmailToAddress_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 2, 3, 2, 2),
    _CpmDcEmailToAddress_Type()
)
cpmDcEmailToAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpmDcEmailToAddress.setStatus("current")
_CpmDcEmailServer_Type = DisplayString
_CpmDcEmailServer_Object = MibScalar
cpmDcEmailServer = _CpmDcEmailServer_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 2, 3, 2, 3),
    _CpmDcEmailServer_Type()
)
cpmDcEmailServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpmDcEmailServer.setStatus("current")
_CpmDcEmailPort_Type = DisplayString
_CpmDcEmailPort_Object = MibScalar
cpmDcEmailPort = _CpmDcEmailPort_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 2, 3, 2, 4),
    _CpmDcEmailPort_Type()
)
cpmDcEmailPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpmDcEmailPort.setStatus("current")
_CpmDcEmailAuthEnable_Type = DisplayString
_CpmDcEmailAuthEnable_Object = MibScalar
cpmDcEmailAuthEnable = _CpmDcEmailAuthEnable_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 2, 3, 2, 5),
    _CpmDcEmailAuthEnable_Type()
)
cpmDcEmailAuthEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpmDcEmailAuthEnable.setStatus("current")
_CpmDcEmailLogin_Type = DisplayString
_CpmDcEmailLogin_Object = MibScalar
cpmDcEmailLogin = _CpmDcEmailLogin_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 2, 3, 2, 6),
    _CpmDcEmailLogin_Type()
)
cpmDcEmailLogin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpmDcEmailLogin.setStatus("current")
_CpmDcEmailPassword_Type = DisplayString
_CpmDcEmailPassword_Object = MibScalar
cpmDcEmailPassword = _CpmDcEmailPassword_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 2, 3, 2, 7),
    _CpmDcEmailPassword_Type()
)
cpmDcEmailPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpmDcEmailPassword.setStatus("current")
_CpmDcSntp_ObjectIdentity = ObjectIdentity
cpmDcSntp = _CpmDcSntp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35774, 2, 2, 3, 3)
)
_CpmDcSntpServer_Type = DisplayString
_CpmDcSntpServer_Object = MibScalar
cpmDcSntpServer = _CpmDcSntpServer_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 2, 3, 3, 1),
    _CpmDcSntpServer_Type()
)
cpmDcSntpServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpmDcSntpServer.setStatus("current")
_CpmDcTelnet_ObjectIdentity = ObjectIdentity
cpmDcTelnet = _CpmDcTelnet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35774, 2, 2, 3, 4)
)
_CpmDcInfeed_ObjectIdentity = ObjectIdentity
cpmDcInfeed = _CpmDcInfeed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35774, 2, 2, 4)
)
_CpmDcInfDemandTime_Type = DisplayString
_CpmDcInfDemandTime_Object = MibScalar
cpmDcInfDemandTime = _CpmDcInfDemandTime_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 2, 4, 1),
    _CpmDcInfDemandTime_Type()
)
cpmDcInfDemandTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpmDcInfDemandTime.setStatus("current")
if mibBuilder.loadTexts:
    cpmDcInfDemandTime.setUnits("minutes")
_CpmDcInfCktCurrRating_Type = DisplayString
_CpmDcInfCktCurrRating_Object = MibScalar
cpmDcInfCktCurrRating = _CpmDcInfCktCurrRating_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 2, 4, 2),
    _CpmDcInfCktCurrRating_Type()
)
cpmDcInfCktCurrRating.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpmDcInfCktCurrRating.setStatus("current")
if mibBuilder.loadTexts:
    cpmDcInfCktCurrRating.setUnits("amps (rms)")
_CpmDcInfCircuit_Object = MibTable
cpmDcInfCircuit = _CpmDcInfCircuit_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 2, 5)
)
if mibBuilder.loadTexts:
    cpmDcInfCircuit.setStatus("current")
_CpmDcInfCircuitEntry_Object = MibTableRow
cpmDcInfCircuitEntry = _CpmDcInfCircuitEntry_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 2, 5, 1)
)
cpmDcInfCircuitEntry.setIndexNames(
    (0, "UEC-STARLINE-MIB", "cpmDcInfeedCircuitIndex"),
)
if mibBuilder.loadTexts:
    cpmDcInfCircuitEntry.setStatus("current")


class _CpmDcInfeedCircuitIndex_Type(Integer32):
    """Custom type cpmDcInfeedCircuitIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("circuit1", 1),
          ("circuit2", 2))
    )


_CpmDcInfeedCircuitIndex_Type.__name__ = "Integer32"
_CpmDcInfeedCircuitIndex_Object = MibTableColumn
cpmDcInfeedCircuitIndex = _CpmDcInfeedCircuitIndex_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 2, 5, 1, 1),
    _CpmDcInfeedCircuitIndex_Type()
)
cpmDcInfeedCircuitIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmDcInfeedCircuitIndex.setStatus("current")
_CpmDcCktVoltage_Type = DisplayString
_CpmDcCktVoltage_Object = MibTableColumn
cpmDcCktVoltage = _CpmDcCktVoltage_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 2, 5, 1, 2),
    _CpmDcCktVoltage_Type()
)
cpmDcCktVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmDcCktVoltage.setStatus("current")
if mibBuilder.loadTexts:
    cpmDcCktVoltage.setUnits("volts (rms)")
_CpmDcCktVoltageMin_Type = DisplayString
_CpmDcCktVoltageMin_Object = MibTableColumn
cpmDcCktVoltageMin = _CpmDcCktVoltageMin_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 2, 5, 1, 3),
    _CpmDcCktVoltageMin_Type()
)
cpmDcCktVoltageMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpmDcCktVoltageMin.setStatus("current")
if mibBuilder.loadTexts:
    cpmDcCktVoltageMin.setUnits("volts (rms)")
_CpmDcCktVoltageMax_Type = DisplayString
_CpmDcCktVoltageMax_Object = MibTableColumn
cpmDcCktVoltageMax = _CpmDcCktVoltageMax_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 2, 5, 1, 4),
    _CpmDcCktVoltageMax_Type()
)
cpmDcCktVoltageMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpmDcCktVoltageMax.setStatus("current")
if mibBuilder.loadTexts:
    cpmDcCktVoltageMax.setUnits("volts (rms)")
_CpmDcCktVoltageMinAlarm_Type = DisplayString
_CpmDcCktVoltageMinAlarm_Object = MibTableColumn
cpmDcCktVoltageMinAlarm = _CpmDcCktVoltageMinAlarm_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 2, 5, 1, 5),
    _CpmDcCktVoltageMinAlarm_Type()
)
cpmDcCktVoltageMinAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpmDcCktVoltageMinAlarm.setStatus("current")
if mibBuilder.loadTexts:
    cpmDcCktVoltageMinAlarm.setUnits("volts (rms)")
_CpmDcCktVoltageMaxAlarm_Type = DisplayString
_CpmDcCktVoltageMaxAlarm_Object = MibTableColumn
cpmDcCktVoltageMaxAlarm = _CpmDcCktVoltageMaxAlarm_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 2, 5, 1, 6),
    _CpmDcCktVoltageMaxAlarm_Type()
)
cpmDcCktVoltageMaxAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpmDcCktVoltageMaxAlarm.setStatus("current")
if mibBuilder.loadTexts:
    cpmDcCktVoltageMaxAlarm.setUnits("volts (rms)")
_CpmDcInfCktPower_Type = DisplayString
_CpmDcInfCktPower_Object = MibTableColumn
cpmDcInfCktPower = _CpmDcInfCktPower_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 2, 5, 1, 7),
    _CpmDcInfCktPower_Type()
)
cpmDcInfCktPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmDcInfCktPower.setStatus("current")
if mibBuilder.loadTexts:
    cpmDcInfCktPower.setUnits("W")
_CpmDcInfCktPeakPower_Type = DisplayString
_CpmDcInfCktPeakPower_Object = MibTableColumn
cpmDcInfCktPeakPower = _CpmDcInfCktPeakPower_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 2, 5, 1, 8),
    _CpmDcInfCktPeakPower_Type()
)
cpmDcInfCktPeakPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpmDcInfCktPeakPower.setStatus("current")
if mibBuilder.loadTexts:
    cpmDcInfCktPeakPower.setUnits("W")
_CpmDcInfCktEnergyDelivrd_Type = DisplayString
_CpmDcInfCktEnergyDelivrd_Object = MibTableColumn
cpmDcInfCktEnergyDelivrd = _CpmDcInfCktEnergyDelivrd_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 2, 5, 1, 9),
    _CpmDcInfCktEnergyDelivrd_Type()
)
cpmDcInfCktEnergyDelivrd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmDcInfCktEnergyDelivrd.setStatus("current")
if mibBuilder.loadTexts:
    cpmDcInfCktEnergyDelivrd.setUnits("kWh")
_CpmDcInfCktEnergyRcvd_Type = DisplayString
_CpmDcInfCktEnergyRcvd_Object = MibTableColumn
cpmDcInfCktEnergyRcvd = _CpmDcInfCktEnergyRcvd_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 2, 5, 1, 10),
    _CpmDcInfCktEnergyRcvd_Type()
)
cpmDcInfCktEnergyRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmDcInfCktEnergyRcvd.setStatus("current")
if mibBuilder.loadTexts:
    cpmDcInfCktEnergyRcvd.setUnits("kWh")
_CpmDcInfCktCurrent_Type = DisplayString
_CpmDcInfCktCurrent_Object = MibTableColumn
cpmDcInfCktCurrent = _CpmDcInfCktCurrent_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 2, 5, 1, 11),
    _CpmDcInfCktCurrent_Type()
)
cpmDcInfCktCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmDcInfCktCurrent.setStatus("current")
if mibBuilder.loadTexts:
    cpmDcInfCktCurrent.setUnits("amps (rms)")
_CpmDcInfCktCurrentMin_Type = DisplayString
_CpmDcInfCktCurrentMin_Object = MibTableColumn
cpmDcInfCktCurrentMin = _CpmDcInfCktCurrentMin_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 2, 5, 1, 12),
    _CpmDcInfCktCurrentMin_Type()
)
cpmDcInfCktCurrentMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpmDcInfCktCurrentMin.setStatus("current")
if mibBuilder.loadTexts:
    cpmDcInfCktCurrentMin.setUnits("amps (rms)")
_CpmDcInfCktCurrentMax_Type = DisplayString
_CpmDcInfCktCurrentMax_Object = MibTableColumn
cpmDcInfCktCurrentMax = _CpmDcInfCktCurrentMax_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 2, 5, 1, 13),
    _CpmDcInfCktCurrentMax_Type()
)
cpmDcInfCktCurrentMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpmDcInfCktCurrentMax.setStatus("current")
if mibBuilder.loadTexts:
    cpmDcInfCktCurrentMax.setUnits("amps (rms)")
_CpmDcInfCktCurrRatPctOf_Type = DisplayString
_CpmDcInfCktCurrRatPctOf_Object = MibTableColumn
cpmDcInfCktCurrRatPctOf = _CpmDcInfCktCurrRatPctOf_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 2, 5, 1, 14),
    _CpmDcInfCktCurrRatPctOf_Type()
)
cpmDcInfCktCurrRatPctOf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmDcInfCktCurrRatPctOf.setStatus("current")
if mibBuilder.loadTexts:
    cpmDcInfCktCurrRatPctOf.setUnits("% of rated")
_CpmDcInfCktCurrMinAlarm_Type = DisplayString
_CpmDcInfCktCurrMinAlarm_Object = MibTableColumn
cpmDcInfCktCurrMinAlarm = _CpmDcInfCktCurrMinAlarm_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 2, 5, 1, 15),
    _CpmDcInfCktCurrMinAlarm_Type()
)
cpmDcInfCktCurrMinAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpmDcInfCktCurrMinAlarm.setStatus("current")
if mibBuilder.loadTexts:
    cpmDcInfCktCurrMinAlarm.setUnits("amps (RMS)")
_CpmDcInfCktCurrMaxAlarm_Type = DisplayString
_CpmDcInfCktCurrMaxAlarm_Object = MibTableColumn
cpmDcInfCktCurrMaxAlarm = _CpmDcInfCktCurrMaxAlarm_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 2, 5, 1, 16),
    _CpmDcInfCktCurrMaxAlarm_Type()
)
cpmDcInfCktCurrMaxAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpmDcInfCktCurrMaxAlarm.setStatus("current")
if mibBuilder.loadTexts:
    cpmDcInfCktCurrMaxAlarm.setUnits("amps (RMS)")
_CpmDcInfCktCurrDemand_Type = DisplayString
_CpmDcInfCktCurrDemand_Object = MibTableColumn
cpmDcInfCktCurrDemand = _CpmDcInfCktCurrDemand_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 2, 5, 1, 17),
    _CpmDcInfCktCurrDemand_Type()
)
cpmDcInfCktCurrDemand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpmDcInfCktCurrDemand.setStatus("current")
if mibBuilder.loadTexts:
    cpmDcInfCktCurrDemand.setUnits("amps per demand interval")
_CpmDcInfCktCurrPeakDmd_Type = DisplayString
_CpmDcInfCktCurrPeakDmd_Object = MibTableColumn
cpmDcInfCktCurrPeakDmd = _CpmDcInfCktCurrPeakDmd_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 2, 5, 1, 18),
    _CpmDcInfCktCurrPeakDmd_Type()
)
cpmDcInfCktCurrPeakDmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpmDcInfCktCurrPeakDmd.setStatus("current")
if mibBuilder.loadTexts:
    cpmDcInfCktCurrPeakDmd.setUnits("amps per demand interval")
_CpmDcOutlet_Object = MibTable
cpmDcOutlet = _CpmDcOutlet_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 2, 6)
)
if mibBuilder.loadTexts:
    cpmDcOutlet.setStatus("current")
_CpmDcOutletEntry_Object = MibTableRow
cpmDcOutletEntry = _CpmDcOutletEntry_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 2, 6, 1)
)
cpmDcOutletEntry.setIndexNames(
    (0, "UEC-STARLINE-MIB", "cpmDcOutletIndex"),
)
if mibBuilder.loadTexts:
    cpmDcOutletEntry.setStatus("current")


class _CpmDcOutletIndex_Type(Integer32):
    """Custom type cpmDcOutletIndex based on Integer32"""
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
        *(("outlet1", 1),
          ("outlet2", 2),
          ("outlet3", 3),
          ("outlet4", 4))
    )


_CpmDcOutletIndex_Type.__name__ = "Integer32"
_CpmDcOutletIndex_Object = MibTableColumn
cpmDcOutletIndex = _CpmDcOutletIndex_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 2, 6, 1, 1),
    _CpmDcOutletIndex_Type()
)
cpmDcOutletIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmDcOutletIndex.setStatus("current")
_CpmDcOutletId_Type = DisplayString
_CpmDcOutletId_Object = MibTableColumn
cpmDcOutletId = _CpmDcOutletId_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 2, 6, 1, 2),
    _CpmDcOutletId_Type()
)
cpmDcOutletId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpmDcOutletId.setStatus("current")
_CpmDcOtlCktCurrRating_Type = DisplayString
_CpmDcOtlCktCurrRating_Object = MibTableColumn
cpmDcOtlCktCurrRating = _CpmDcOtlCktCurrRating_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 2, 6, 1, 3),
    _CpmDcOtlCktCurrRating_Type()
)
cpmDcOtlCktCurrRating.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmDcOtlCktCurrRating.setStatus("current")
if mibBuilder.loadTexts:
    cpmDcOtlCktCurrRating.setUnits("amps (rms)")
_CpmDcOtlDemandTime_Type = DisplayString
_CpmDcOtlDemandTime_Object = MibTableColumn
cpmDcOtlDemandTime = _CpmDcOtlDemandTime_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 2, 6, 1, 4),
    _CpmDcOtlDemandTime_Type()
)
cpmDcOtlDemandTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpmDcOtlDemandTime.setStatus("current")
if mibBuilder.loadTexts:
    cpmDcOtlDemandTime.setUnits("minutes")
_CpmDcOtlCurrentMinAlarm_Type = DisplayString
_CpmDcOtlCurrentMinAlarm_Object = MibTableColumn
cpmDcOtlCurrentMinAlarm = _CpmDcOtlCurrentMinAlarm_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 2, 6, 1, 5),
    _CpmDcOtlCurrentMinAlarm_Type()
)
cpmDcOtlCurrentMinAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpmDcOtlCurrentMinAlarm.setStatus("current")
if mibBuilder.loadTexts:
    cpmDcOtlCurrentMinAlarm.setUnits("amps (rms)")
_CpmDcOtlCurrentMaxAlarm_Type = DisplayString
_CpmDcOtlCurrentMaxAlarm_Object = MibTableColumn
cpmDcOtlCurrentMaxAlarm = _CpmDcOtlCurrentMaxAlarm_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 2, 6, 1, 6),
    _CpmDcOtlCurrentMaxAlarm_Type()
)
cpmDcOtlCurrentMaxAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpmDcOtlCurrentMaxAlarm.setStatus("current")
if mibBuilder.loadTexts:
    cpmDcOtlCurrentMaxAlarm.setUnits("amps (rms)")
_CpmDcOutletCircuit_Object = MibTable
cpmDcOutletCircuit = _CpmDcOutletCircuit_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 2, 7)
)
if mibBuilder.loadTexts:
    cpmDcOutletCircuit.setStatus("current")
_CpmDcOutletCircuitEntry_Object = MibTableRow
cpmDcOutletCircuitEntry = _CpmDcOutletCircuitEntry_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 2, 7, 1)
)
cpmDcOutletCircuitEntry.setIndexNames(
    (0, "UEC-STARLINE-MIB", "cpmDcOutletOutletIndex"),
    (0, "UEC-STARLINE-MIB", "cpmDcOutletCircuitIndex"),
)
if mibBuilder.loadTexts:
    cpmDcOutletCircuitEntry.setStatus("current")


class _CpmDcOutletOutletIndex_Type(Integer32):
    """Custom type cpmDcOutletOutletIndex based on Integer32"""
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
        *(("outlet1", 1),
          ("outlet2", 2),
          ("outlet3", 3),
          ("outlet4", 4))
    )


_CpmDcOutletOutletIndex_Type.__name__ = "Integer32"
_CpmDcOutletOutletIndex_Object = MibTableColumn
cpmDcOutletOutletIndex = _CpmDcOutletOutletIndex_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 2, 7, 1, 1),
    _CpmDcOutletOutletIndex_Type()
)
cpmDcOutletOutletIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmDcOutletOutletIndex.setStatus("current")


class _CpmDcOutletCircuitIndex_Type(Integer32):
    """Custom type cpmDcOutletCircuitIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("circuit1", 1),
          ("circuit2", 2))
    )


_CpmDcOutletCircuitIndex_Type.__name__ = "Integer32"
_CpmDcOutletCircuitIndex_Object = MibTableColumn
cpmDcOutletCircuitIndex = _CpmDcOutletCircuitIndex_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 2, 7, 1, 2),
    _CpmDcOutletCircuitIndex_Type()
)
cpmDcOutletCircuitIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmDcOutletCircuitIndex.setStatus("current")
_CpmDcOtlCktCurrent_Type = DisplayString
_CpmDcOtlCktCurrent_Object = MibTableColumn
cpmDcOtlCktCurrent = _CpmDcOtlCktCurrent_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 2, 7, 1, 3),
    _CpmDcOtlCktCurrent_Type()
)
cpmDcOtlCktCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmDcOtlCktCurrent.setStatus("current")
if mibBuilder.loadTexts:
    cpmDcOtlCktCurrent.setUnits("amps (rms)")
_CpmDcOtlCktCurrRatPctOf_Type = DisplayString
_CpmDcOtlCktCurrRatPctOf_Object = MibTableColumn
cpmDcOtlCktCurrRatPctOf = _CpmDcOtlCktCurrRatPctOf_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 2, 7, 1, 4),
    _CpmDcOtlCktCurrRatPctOf_Type()
)
cpmDcOtlCktCurrRatPctOf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmDcOtlCktCurrRatPctOf.setStatus("current")
if mibBuilder.loadTexts:
    cpmDcOtlCktCurrRatPctOf.setUnits("% of rated")
_CpmDcOtlCktCurrentDemand_Type = DisplayString
_CpmDcOtlCktCurrentDemand_Object = MibTableColumn
cpmDcOtlCktCurrentDemand = _CpmDcOtlCktCurrentDemand_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 2, 7, 1, 5),
    _CpmDcOtlCktCurrentDemand_Type()
)
cpmDcOtlCktCurrentDemand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpmDcOtlCktCurrentDemand.setStatus("current")
if mibBuilder.loadTexts:
    cpmDcOtlCktCurrentDemand.setUnits("amps (rms) per demand interval")
_CpmDcOtlCktCurrPeakDmd_Type = DisplayString
_CpmDcOtlCktCurrPeakDmd_Object = MibTableColumn
cpmDcOtlCktCurrPeakDmd = _CpmDcOtlCktCurrPeakDmd_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 2, 7, 1, 6),
    _CpmDcOtlCktCurrPeakDmd_Type()
)
cpmDcOtlCktCurrPeakDmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpmDcOtlCktCurrPeakDmd.setStatus("current")
if mibBuilder.loadTexts:
    cpmDcOtlCktCurrPeakDmd.setUnits("amps (rms) per demand interval")
_CpmDcOtlCktCurrentMin_Type = DisplayString
_CpmDcOtlCktCurrentMin_Object = MibTableColumn
cpmDcOtlCktCurrentMin = _CpmDcOtlCktCurrentMin_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 2, 7, 1, 7),
    _CpmDcOtlCktCurrentMin_Type()
)
cpmDcOtlCktCurrentMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpmDcOtlCktCurrentMin.setStatus("current")
if mibBuilder.loadTexts:
    cpmDcOtlCktCurrentMin.setUnits("amps (rms) per demand interval")
_CpmDcOtlCktCurrentMax_Type = DisplayString
_CpmDcOtlCktCurrentMax_Object = MibTableColumn
cpmDcOtlCktCurrentMax = _CpmDcOtlCktCurrentMax_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 2, 7, 1, 8),
    _CpmDcOtlCktCurrentMax_Type()
)
cpmDcOtlCktCurrentMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpmDcOtlCktCurrentMax.setStatus("current")
if mibBuilder.loadTexts:
    cpmDcOtlCktCurrentMax.setUnits("amps (rms) per demand interval")
_CpmDcOtlCktPower_Type = DisplayString
_CpmDcOtlCktPower_Object = MibTableColumn
cpmDcOtlCktPower = _CpmDcOtlCktPower_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 2, 7, 1, 9),
    _CpmDcOtlCktPower_Type()
)
cpmDcOtlCktPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmDcOtlCktPower.setStatus("current")
if mibBuilder.loadTexts:
    cpmDcOtlCktPower.setUnits("W")
_CpmDcOtlCktPeakPower_Type = DisplayString
_CpmDcOtlCktPeakPower_Object = MibTableColumn
cpmDcOtlCktPeakPower = _CpmDcOtlCktPeakPower_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 2, 7, 1, 10),
    _CpmDcOtlCktPeakPower_Type()
)
cpmDcOtlCktPeakPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpmDcOtlCktPeakPower.setStatus("current")
if mibBuilder.loadTexts:
    cpmDcOtlCktPeakPower.setUnits("W")
_CpmDcOtlCktEnergyDelivrd_Type = DisplayString
_CpmDcOtlCktEnergyDelivrd_Object = MibTableColumn
cpmDcOtlCktEnergyDelivrd = _CpmDcOtlCktEnergyDelivrd_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 2, 7, 1, 11),
    _CpmDcOtlCktEnergyDelivrd_Type()
)
cpmDcOtlCktEnergyDelivrd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmDcOtlCktEnergyDelivrd.setStatus("current")
if mibBuilder.loadTexts:
    cpmDcOtlCktEnergyDelivrd.setUnits("kWh")
_CpmDcOtlCktEnergyRcvd_Type = DisplayString
_CpmDcOtlCktEnergyRcvd_Object = MibTableColumn
cpmDcOtlCktEnergyRcvd = _CpmDcOtlCktEnergyRcvd_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 2, 7, 1, 12),
    _CpmDcOtlCktEnergyRcvd_Type()
)
cpmDcOtlCktEnergyRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmDcOtlCktEnergyRcvd.setStatus("current")
if mibBuilder.loadTexts:
    cpmDcOtlCktEnergyRcvd.setUnits("kWh")
_CpmDcAlarms_ObjectIdentity = ObjectIdentity
cpmDcAlarms = _CpmDcAlarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35774, 2, 2, 8)
)
_CpmDcInfeedAlarmStatus_Type = DisplayString
_CpmDcInfeedAlarmStatus_Object = MibScalar
cpmDcInfeedAlarmStatus = _CpmDcInfeedAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 2, 8, 1),
    _CpmDcInfeedAlarmStatus_Type()
)
cpmDcInfeedAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmDcInfeedAlarmStatus.setStatus("current")
_CpmDcOutletAlarmStatus_Type = DisplayString
_CpmDcOutletAlarmStatus_Object = MibScalar
cpmDcOutletAlarmStatus = _CpmDcOutletAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 2, 8, 2),
    _CpmDcOutletAlarmStatus_Type()
)
cpmDcOutletAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmDcOutletAlarmStatus.setStatus("current")
_CpmDcDiagnostics_ObjectIdentity = ObjectIdentity
cpmDcDiagnostics = _CpmDcDiagnostics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35774, 2, 2, 9)
)
_CpmDcFirstErrorMessage_Type = DisplayString
_CpmDcFirstErrorMessage_Object = MibScalar
cpmDcFirstErrorMessage = _CpmDcFirstErrorMessage_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 2, 9, 1),
    _CpmDcFirstErrorMessage_Type()
)
cpmDcFirstErrorMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmDcFirstErrorMessage.setStatus("current")
_CpmDcLastErrorMessage_Type = DisplayString
_CpmDcLastErrorMessage_Object = MibScalar
cpmDcLastErrorMessage = _CpmDcLastErrorMessage_Object(
    (1, 3, 6, 1, 4, 1, 35774, 2, 2, 9, 2),
    _CpmDcLastErrorMessage_Type()
)
cpmDcLastErrorMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpmDcLastErrorMessage.setStatus("current")
_CpmDcNotifications_ObjectIdentity = ObjectIdentity
cpmDcNotifications = _CpmDcNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35774, 2, 2, 50)
)
_CpmDcEvents_ObjectIdentity = ObjectIdentity
cpmDcEvents = _CpmDcEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35774, 2, 2, 50, 0)
)

# Managed Objects groups


# Notification objects

cpmAcInfOvCurrAssertEv = NotificationType(
    (1, 3, 6, 1, 4, 1, 35774, 2, 1, 50, 0, 1)
)
cpmAcInfOvCurrAssertEv.setObjects(
      *(("UEC-STARLINE-MIB", "cpmAcDeviceName"),
        ("UEC-STARLINE-MIB", "cpmAcSerialNumber"),
        ("UEC-STARLINE-MIB", "cpmAcDeviceLocation"),
        ("UEC-STARLINE-MIB", "cpmAcInfeedLineIndex"))
)
if mibBuilder.loadTexts:
    cpmAcInfOvCurrAssertEv.setStatus(
        "current"
    )

cpmAcInfOvCurrDeassertEv = NotificationType(
    (1, 3, 6, 1, 4, 1, 35774, 2, 1, 50, 0, 2)
)
cpmAcInfOvCurrDeassertEv.setObjects(
      *(("UEC-STARLINE-MIB", "cpmAcDeviceName"),
        ("UEC-STARLINE-MIB", "cpmAcSerialNumber"),
        ("UEC-STARLINE-MIB", "cpmAcDeviceLocation"),
        ("UEC-STARLINE-MIB", "cpmAcInfeedLineIndex"))
)
if mibBuilder.loadTexts:
    cpmAcInfOvCurrDeassertEv.setStatus(
        "current"
    )

cpmAcInfUnCurrAssertEv = NotificationType(
    (1, 3, 6, 1, 4, 1, 35774, 2, 1, 50, 0, 3)
)
cpmAcInfUnCurrAssertEv.setObjects(
      *(("UEC-STARLINE-MIB", "cpmAcDeviceName"),
        ("UEC-STARLINE-MIB", "cpmAcSerialNumber"),
        ("UEC-STARLINE-MIB", "cpmAcDeviceLocation"),
        ("UEC-STARLINE-MIB", "cpmAcInfeedLineIndex"))
)
if mibBuilder.loadTexts:
    cpmAcInfUnCurrAssertEv.setStatus(
        "current"
    )

cpmAcInfUnCurrDeassertEv = NotificationType(
    (1, 3, 6, 1, 4, 1, 35774, 2, 1, 50, 0, 4)
)
cpmAcInfUnCurrDeassertEv.setObjects(
      *(("UEC-STARLINE-MIB", "cpmAcDeviceName"),
        ("UEC-STARLINE-MIB", "cpmAcSerialNumber"),
        ("UEC-STARLINE-MIB", "cpmAcDeviceLocation"),
        ("UEC-STARLINE-MIB", "cpmAcInfeedLineIndex"))
)
if mibBuilder.loadTexts:
    cpmAcInfUnCurrDeassertEv.setStatus(
        "current"
    )

cpmAcInfOvVoltAssertEv = NotificationType(
    (1, 3, 6, 1, 4, 1, 35774, 2, 1, 50, 0, 5)
)
cpmAcInfOvVoltAssertEv.setObjects(
      *(("UEC-STARLINE-MIB", "cpmAcDeviceName"),
        ("UEC-STARLINE-MIB", "cpmAcSerialNumber"),
        ("UEC-STARLINE-MIB", "cpmAcDeviceLocation"),
        ("UEC-STARLINE-MIB", "cpmAcInfeedPhaseIndex"))
)
if mibBuilder.loadTexts:
    cpmAcInfOvVoltAssertEv.setStatus(
        "current"
    )

cpmAcInfOvVoltDeassertEv = NotificationType(
    (1, 3, 6, 1, 4, 1, 35774, 2, 1, 50, 0, 6)
)
cpmAcInfOvVoltDeassertEv.setObjects(
      *(("UEC-STARLINE-MIB", "cpmAcDeviceName"),
        ("UEC-STARLINE-MIB", "cpmAcSerialNumber"),
        ("UEC-STARLINE-MIB", "cpmAcDeviceLocation"),
        ("UEC-STARLINE-MIB", "cpmAcInfeedPhaseIndex"))
)
if mibBuilder.loadTexts:
    cpmAcInfOvVoltDeassertEv.setStatus(
        "current"
    )

cpmAcInfUnVoltAssertEv = NotificationType(
    (1, 3, 6, 1, 4, 1, 35774, 2, 1, 50, 0, 7)
)
cpmAcInfUnVoltAssertEv.setObjects(
      *(("UEC-STARLINE-MIB", "cpmAcDeviceName"),
        ("UEC-STARLINE-MIB", "cpmAcSerialNumber"),
        ("UEC-STARLINE-MIB", "cpmAcDeviceLocation"),
        ("UEC-STARLINE-MIB", "cpmAcInfeedPhaseIndex"))
)
if mibBuilder.loadTexts:
    cpmAcInfUnVoltAssertEv.setStatus(
        "current"
    )

cpmAcInfUnVoltDeassertEv = NotificationType(
    (1, 3, 6, 1, 4, 1, 35774, 2, 1, 50, 0, 8)
)
cpmAcInfUnVoltDeassertEv.setObjects(
      *(("UEC-STARLINE-MIB", "cpmAcDeviceName"),
        ("UEC-STARLINE-MIB", "cpmAcSerialNumber"),
        ("UEC-STARLINE-MIB", "cpmAcDeviceLocation"),
        ("UEC-STARLINE-MIB", "cpmAcInfeedPhaseIndex"))
)
if mibBuilder.loadTexts:
    cpmAcInfUnVoltDeassertEv.setStatus(
        "current"
    )

cpmAcOtlOvCurrAssertEv = NotificationType(
    (1, 3, 6, 1, 4, 1, 35774, 2, 1, 50, 0, 9)
)
cpmAcOtlOvCurrAssertEv.setObjects(
      *(("UEC-STARLINE-MIB", "cpmAcDeviceName"),
        ("UEC-STARLINE-MIB", "cpmAcSerialNumber"),
        ("UEC-STARLINE-MIB", "cpmAcDeviceLocation"),
        ("UEC-STARLINE-MIB", "cpmAcOutletOutletIndex"),
        ("UEC-STARLINE-MIB", "cpmAcOutletLineIndex"))
)
if mibBuilder.loadTexts:
    cpmAcOtlOvCurrAssertEv.setStatus(
        "current"
    )

cpmAcOtlOvCurrDeassertEv = NotificationType(
    (1, 3, 6, 1, 4, 1, 35774, 2, 1, 50, 0, 10)
)
cpmAcOtlOvCurrDeassertEv.setObjects(
      *(("UEC-STARLINE-MIB", "cpmAcDeviceName"),
        ("UEC-STARLINE-MIB", "cpmAcSerialNumber"),
        ("UEC-STARLINE-MIB", "cpmAcDeviceLocation"),
        ("UEC-STARLINE-MIB", "cpmAcOutletOutletIndex"),
        ("UEC-STARLINE-MIB", "cpmAcOutletLineIndex"))
)
if mibBuilder.loadTexts:
    cpmAcOtlOvCurrDeassertEv.setStatus(
        "current"
    )

cpmAcOtlUnCurrAssertEv = NotificationType(
    (1, 3, 6, 1, 4, 1, 35774, 2, 1, 50, 0, 11)
)
cpmAcOtlUnCurrAssertEv.setObjects(
      *(("UEC-STARLINE-MIB", "cpmAcDeviceName"),
        ("UEC-STARLINE-MIB", "cpmAcSerialNumber"),
        ("UEC-STARLINE-MIB", "cpmAcDeviceLocation"),
        ("UEC-STARLINE-MIB", "cpmAcOutletOutletIndex"),
        ("UEC-STARLINE-MIB", "cpmAcOutletLineIndex"))
)
if mibBuilder.loadTexts:
    cpmAcOtlUnCurrAssertEv.setStatus(
        "current"
    )

cpmAcOtlUnCurrDeassertEv = NotificationType(
    (1, 3, 6, 1, 4, 1, 35774, 2, 1, 50, 0, 12)
)
cpmAcOtlUnCurrDeassertEv.setObjects(
      *(("UEC-STARLINE-MIB", "cpmAcDeviceName"),
        ("UEC-STARLINE-MIB", "cpmAcSerialNumber"),
        ("UEC-STARLINE-MIB", "cpmAcDeviceLocation"),
        ("UEC-STARLINE-MIB", "cpmAcOutletOutletIndex"),
        ("UEC-STARLINE-MIB", "cpmAcOutletLineIndex"))
)
if mibBuilder.loadTexts:
    cpmAcOtlUnCurrDeassertEv.setStatus(
        "current"
    )

cpmAcOvTempAssertEv = NotificationType(
    (1, 3, 6, 1, 4, 1, 35774, 2, 1, 50, 0, 13)
)
cpmAcOvTempAssertEv.setObjects(
      *(("UEC-STARLINE-MIB", "cpmAcDeviceName"),
        ("UEC-STARLINE-MIB", "cpmAcSerialNumber"),
        ("UEC-STARLINE-MIB", "cpmAcDeviceLocation"))
)
if mibBuilder.loadTexts:
    cpmAcOvTempAssertEv.setStatus(
        "current"
    )

cpmAcOvTempDeassertEv = NotificationType(
    (1, 3, 6, 1, 4, 1, 35774, 2, 1, 50, 0, 14)
)
cpmAcOvTempDeassertEv.setObjects(
      *(("UEC-STARLINE-MIB", "cpmAcDeviceName"),
        ("UEC-STARLINE-MIB", "cpmAcSerialNumber"),
        ("UEC-STARLINE-MIB", "cpmAcDeviceLocation"))
)
if mibBuilder.loadTexts:
    cpmAcOvTempDeassertEv.setStatus(
        "current"
    )

cpmAcBatVoltLowAssertEv = NotificationType(
    (1, 3, 6, 1, 4, 1, 35774, 2, 1, 50, 0, 15)
)
cpmAcBatVoltLowAssertEv.setObjects(
      *(("UEC-STARLINE-MIB", "cpmAcDeviceName"),
        ("UEC-STARLINE-MIB", "cpmAcSerialNumber"),
        ("UEC-STARLINE-MIB", "cpmAcDeviceLocation"),
        ("UEC-STARLINE-MIB", "cpmAcNodeIndex"))
)
if mibBuilder.loadTexts:
    cpmAcBatVoltLowAssertEv.setStatus(
        "current"
    )

cpmAcBatVoltLowDeassertEv = NotificationType(
    (1, 3, 6, 1, 4, 1, 35774, 2, 1, 50, 0, 16)
)
cpmAcBatVoltLowDeassertEv.setObjects(
      *(("UEC-STARLINE-MIB", "cpmAcDeviceName"),
        ("UEC-STARLINE-MIB", "cpmAcSerialNumber"),
        ("UEC-STARLINE-MIB", "cpmAcDeviceLocation"),
        ("UEC-STARLINE-MIB", "cpmAcNodeIndex"))
)
if mibBuilder.loadTexts:
    cpmAcBatVoltLowDeassertEv.setStatus(
        "current"
    )

cpmDcInfOvCurrAssertEv = NotificationType(
    (1, 3, 6, 1, 4, 1, 35774, 2, 2, 50, 0, 1)
)
cpmDcInfOvCurrAssertEv.setObjects(
      *(("UEC-STARLINE-MIB", "cpmDcDeviceName"),
        ("UEC-STARLINE-MIB", "cpmDcSerialNumber"),
        ("UEC-STARLINE-MIB", "cpmDcDeviceLocation"),
        ("UEC-STARLINE-MIB", "cpmDcInfeedCircuitIndex"))
)
if mibBuilder.loadTexts:
    cpmDcInfOvCurrAssertEv.setStatus(
        "current"
    )

cpmDcInfOvCurrDeassertEv = NotificationType(
    (1, 3, 6, 1, 4, 1, 35774, 2, 2, 50, 0, 2)
)
cpmDcInfOvCurrDeassertEv.setObjects(
      *(("UEC-STARLINE-MIB", "cpmDcDeviceName"),
        ("UEC-STARLINE-MIB", "cpmDcSerialNumber"),
        ("UEC-STARLINE-MIB", "cpmDcDeviceLocation"),
        ("UEC-STARLINE-MIB", "cpmDcInfeedCircuitIndex"))
)
if mibBuilder.loadTexts:
    cpmDcInfOvCurrDeassertEv.setStatus(
        "current"
    )

cpmDcInfUnCurrAssertEv = NotificationType(
    (1, 3, 6, 1, 4, 1, 35774, 2, 2, 50, 0, 3)
)
cpmDcInfUnCurrAssertEv.setObjects(
      *(("UEC-STARLINE-MIB", "cpmDcDeviceName"),
        ("UEC-STARLINE-MIB", "cpmDcSerialNumber"),
        ("UEC-STARLINE-MIB", "cpmDcDeviceLocation"),
        ("UEC-STARLINE-MIB", "cpmDcInfeedCircuitIndex"))
)
if mibBuilder.loadTexts:
    cpmDcInfUnCurrAssertEv.setStatus(
        "current"
    )

cpmDcInfUnCurrDeassertEv = NotificationType(
    (1, 3, 6, 1, 4, 1, 35774, 2, 2, 50, 0, 4)
)
cpmDcInfUnCurrDeassertEv.setObjects(
      *(("UEC-STARLINE-MIB", "cpmDcDeviceName"),
        ("UEC-STARLINE-MIB", "cpmDcSerialNumber"),
        ("UEC-STARLINE-MIB", "cpmDcDeviceLocation"),
        ("UEC-STARLINE-MIB", "cpmDcInfeedCircuitIndex"))
)
if mibBuilder.loadTexts:
    cpmDcInfUnCurrDeassertEv.setStatus(
        "current"
    )

cpmDcInfOvVoltAssertEv = NotificationType(
    (1, 3, 6, 1, 4, 1, 35774, 2, 2, 50, 0, 5)
)
cpmDcInfOvVoltAssertEv.setObjects(
      *(("UEC-STARLINE-MIB", "cpmDcDeviceName"),
        ("UEC-STARLINE-MIB", "cpmDcSerialNumber"),
        ("UEC-STARLINE-MIB", "cpmDcDeviceLocation"),
        ("UEC-STARLINE-MIB", "cpmDcInfeedCircuitIndex"))
)
if mibBuilder.loadTexts:
    cpmDcInfOvVoltAssertEv.setStatus(
        "current"
    )

cpmDcInfOvVoltDeassertEv = NotificationType(
    (1, 3, 6, 1, 4, 1, 35774, 2, 2, 50, 0, 6)
)
cpmDcInfOvVoltDeassertEv.setObjects(
      *(("UEC-STARLINE-MIB", "cpmDcDeviceName"),
        ("UEC-STARLINE-MIB", "cpmDcSerialNumber"),
        ("UEC-STARLINE-MIB", "cpmDcDeviceLocation"),
        ("UEC-STARLINE-MIB", "cpmDcInfeedCircuitIndex"))
)
if mibBuilder.loadTexts:
    cpmDcInfOvVoltDeassertEv.setStatus(
        "current"
    )

cpmDcInfUnVoltAssertEv = NotificationType(
    (1, 3, 6, 1, 4, 1, 35774, 2, 2, 50, 0, 7)
)
cpmDcInfUnVoltAssertEv.setObjects(
      *(("UEC-STARLINE-MIB", "cpmDcDeviceName"),
        ("UEC-STARLINE-MIB", "cpmDcSerialNumber"),
        ("UEC-STARLINE-MIB", "cpmDcDeviceLocation"),
        ("UEC-STARLINE-MIB", "cpmDcInfeedCircuitIndex"))
)
if mibBuilder.loadTexts:
    cpmDcInfUnVoltAssertEv.setStatus(
        "current"
    )

cpmDcInfUnVoltDeassertEv = NotificationType(
    (1, 3, 6, 1, 4, 1, 35774, 2, 2, 50, 0, 8)
)
cpmDcInfUnVoltDeassertEv.setObjects(
      *(("UEC-STARLINE-MIB", "cpmDcDeviceName"),
        ("UEC-STARLINE-MIB", "cpmDcSerialNumber"),
        ("UEC-STARLINE-MIB", "cpmDcDeviceLocation"),
        ("UEC-STARLINE-MIB", "cpmDcInfeedCircuitIndex"))
)
if mibBuilder.loadTexts:
    cpmDcInfUnVoltDeassertEv.setStatus(
        "current"
    )

cpmDcOtlOvCurrAssertEv = NotificationType(
    (1, 3, 6, 1, 4, 1, 35774, 2, 2, 50, 0, 9)
)
cpmDcOtlOvCurrAssertEv.setObjects(
      *(("UEC-STARLINE-MIB", "cpmDcDeviceName"),
        ("UEC-STARLINE-MIB", "cpmDcSerialNumber"),
        ("UEC-STARLINE-MIB", "cpmDcDeviceLocation"),
        ("UEC-STARLINE-MIB", "cpmDcOutletOutletIndex"),
        ("UEC-STARLINE-MIB", "cpmDcOutletCircuitIndex"))
)
if mibBuilder.loadTexts:
    cpmDcOtlOvCurrAssertEv.setStatus(
        "current"
    )

cpmDcOtlOvCurrDeassertEv = NotificationType(
    (1, 3, 6, 1, 4, 1, 35774, 2, 2, 50, 0, 10)
)
cpmDcOtlOvCurrDeassertEv.setObjects(
      *(("UEC-STARLINE-MIB", "cpmDcDeviceName"),
        ("UEC-STARLINE-MIB", "cpmDcSerialNumber"),
        ("UEC-STARLINE-MIB", "cpmDcDeviceLocation"),
        ("UEC-STARLINE-MIB", "cpmDcOutletOutletIndex"),
        ("UEC-STARLINE-MIB", "cpmDcOutletCircuitIndex"))
)
if mibBuilder.loadTexts:
    cpmDcOtlOvCurrDeassertEv.setStatus(
        "current"
    )

cpmDcOtlUnCurrAssertEv = NotificationType(
    (1, 3, 6, 1, 4, 1, 35774, 2, 2, 50, 0, 11)
)
cpmDcOtlUnCurrAssertEv.setObjects(
      *(("UEC-STARLINE-MIB", "cpmDcDeviceName"),
        ("UEC-STARLINE-MIB", "cpmDcSerialNumber"),
        ("UEC-STARLINE-MIB", "cpmDcDeviceLocation"),
        ("UEC-STARLINE-MIB", "cpmDcOutletOutletIndex"),
        ("UEC-STARLINE-MIB", "cpmDcOutletCircuitIndex"))
)
if mibBuilder.loadTexts:
    cpmDcOtlUnCurrAssertEv.setStatus(
        "current"
    )

cpmDcOtlUnCurrDeassertEv = NotificationType(
    (1, 3, 6, 1, 4, 1, 35774, 2, 2, 50, 0, 12)
)
cpmDcOtlUnCurrDeassertEv.setObjects(
      *(("UEC-STARLINE-MIB", "cpmDcDeviceName"),
        ("UEC-STARLINE-MIB", "cpmDcSerialNumber"),
        ("UEC-STARLINE-MIB", "cpmDcDeviceLocation"),
        ("UEC-STARLINE-MIB", "cpmDcOutletOutletIndex"),
        ("UEC-STARLINE-MIB", "cpmDcOutletCircuitIndex"))
)
if mibBuilder.loadTexts:
    cpmDcOtlUnCurrDeassertEv.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "UEC-STARLINE-MIB",
    **{"DisplayString": DisplayString,
       "uecStarline": uecStarline,
       "cpm": cpm,
       "cpmAcMeter": cpmAcMeter,
       "cpmAcGeneral": cpmAcGeneral,
       "cpmAcDeviceName": cpmAcDeviceName,
       "cpmAcDeviceLocation": cpmAcDeviceLocation,
       "cpmAcDeviceId": cpmAcDeviceId,
       "cpmAcModelNumber": cpmAcModelNumber,
       "cpmAcSerialNumber": cpmAcSerialNumber,
       "cpmAcCatalogNumber": cpmAcCatalogNumber,
       "cpmAcFirmwareVersion": cpmAcFirmwareVersion,
       "cpmAcCalibrationDate": cpmAcCalibrationDate,
       "cpmAcEnergyReset": cpmAcEnergyReset,
       "cpmAcGroupReset": cpmAcGroupReset,
       "cpmAcInterfaces": cpmAcInterfaces,
       "cpmAcEthernet": cpmAcEthernet,
       "cpmAcEnetMacAddress": cpmAcEnetMacAddress,
       "cpmAcEnetIpAddress": cpmAcEnetIpAddress,
       "cpmAcEnetIpNetmask": cpmAcEnetIpNetmask,
       "cpmAcEnetIpGateway": cpmAcEnetIpGateway,
       "cpmAcEnetEnableDHCP": cpmAcEnetEnableDHCP,
       "cpmAcEnetStaticIpAddress": cpmAcEnetStaticIpAddress,
       "cpmAcEnetStaticIpNetmask": cpmAcEnetStaticIpNetmask,
       "cpmAcEnetStaticIpGateway": cpmAcEnetStaticIpGateway,
       "cpmAcWifi": cpmAcWifi,
       "cpmAcWifiMacAddress": cpmAcWifiMacAddress,
       "cpmAcWifiIpAddress": cpmAcWifiIpAddress,
       "cpmAcWifiIpNetmask": cpmAcWifiIpNetmask,
       "cpmAcWifiIpGateway": cpmAcWifiIpGateway,
       "cpmAcWifiEnableDHCP": cpmAcWifiEnableDHCP,
       "cpmAcWifiStaticIpAddress": cpmAcWifiStaticIpAddress,
       "cpmAcWifiStaticIpNetmask": cpmAcWifiStaticIpNetmask,
       "cpmAcWifiStaticIpGateway": cpmAcWifiStaticIpGateway,
       "cpmAcWifiSSID": cpmAcWifiSSID,
       "cpmAcWifiEncryptionType": cpmAcWifiEncryptionType,
       "cpmAcModbus": cpmAcModbus,
       "cpmAcModbusAddress": cpmAcModbusAddress,
       "cpmAcModbusBaudRate": cpmAcModbusBaudRate,
       "cpmAcModbusStopBits": cpmAcModbusStopBits,
       "cpmAcModbusParity": cpmAcModbusParity,
       "cpmAcDigitalIo": cpmAcDigitalIo,
       "cpmAcDigitalIoEntry": cpmAcDigitalIoEntry,
       "cpmAcDigitalIoIndex": cpmAcDigitalIoIndex,
       "cpmAcDigitalIoName": cpmAcDigitalIoName,
       "cpmAcDigitalIoValue": cpmAcDigitalIoValue,
       "cpmAcDigitalIoDirection": cpmAcDigitalIoDirection,
       "cpmAcDigitalIoLevel": cpmAcDigitalIoLevel,
       "cpmAcDigitalIoAlarm": cpmAcDigitalIoAlarm,
       "cpmAcAnalogIo": cpmAcAnalogIo,
       "cpmAc4to20maPortName": cpmAc4to20maPortName,
       "cpmAc4to20maValue": cpmAc4to20maValue,
       "cpmAcProtocols": cpmAcProtocols,
       "cpmAcSnmp": cpmAcSnmp,
       "cpmAcSnmpTrapDestAddr1": cpmAcSnmpTrapDestAddr1,
       "cpmAcSnmpTrapDestAddr2": cpmAcSnmpTrapDestAddr2,
       "cpmAcEmail": cpmAcEmail,
       "cpmAcEmailFromAddress": cpmAcEmailFromAddress,
       "cpmAcEmailToAddress": cpmAcEmailToAddress,
       "cpmAcEmailServer": cpmAcEmailServer,
       "cpmAcEmailPort": cpmAcEmailPort,
       "cpmAcEmailAuthEnable": cpmAcEmailAuthEnable,
       "cpmAcEmailLogin": cpmAcEmailLogin,
       "cpmAcEmailPassword": cpmAcEmailPassword,
       "cpmAcSntp": cpmAcSntp,
       "cpmAcSntpServer": cpmAcSntpServer,
       "cpmAcTelnet": cpmAcTelnet,
       "cpmAcInfeed": cpmAcInfeed,
       "cpmAcInfLineToNeutVoltAve": cpmAcInfLineToNeutVoltAve,
       "cpmAcInfLineToLineVoltAve": cpmAcInfLineToLineVoltAve,
       "cpmAcInfLineCurrentAve": cpmAcInfLineCurrentAve,
       "cpmAcInfTotLineCurrDemand": cpmAcInfTotLineCurrDemand,
       "cpmAcInfTotLineCurrPeakDmd": cpmAcInfTotLineCurrPeakDmd,
       "cpmAcInfDemandTime": cpmAcInfDemandTime,
       "cpmAcInfTotalActivePower": cpmAcInfTotalActivePower,
       "cpmAcInfPeakTotalActivePower": cpmAcInfPeakTotalActivePower,
       "cpmAcInfTotalActivePwrDemand": cpmAcInfTotalActivePwrDemand,
       "cpmAcInfPeakTotActPwrDemand": cpmAcInfPeakTotActPwrDemand,
       "cpmAcInfTotalReactivePower": cpmAcInfTotalReactivePower,
       "cpmAcInfTotReactivePwrDemand": cpmAcInfTotReactivePwrDemand,
       "cpmAcInfPeakTotReactPwrDmd": cpmAcInfPeakTotReactPwrDmd,
       "cpmAcInfTotalApparentPower": cpmAcInfTotalApparentPower,
       "cpmAcInfTotApparentPwrDemand": cpmAcInfTotApparentPwrDemand,
       "cpmAcInfPeakTotApparPwrDmd": cpmAcInfPeakTotApparPwrDmd,
       "cpmAcInfTotalPowerFactor": cpmAcInfTotalPowerFactor,
       "cpmAcInfFrequency": cpmAcInfFrequency,
       "cpmAcInfTotalEnergy": cpmAcInfTotalEnergy,
       "cpmAcInfLineCurrentRating": cpmAcInfLineCurrentRating,
       "cpmAcInfMeasuredNeutralCurr": cpmAcInfMeasuredNeutralCurr,
       "cpmAcInfFrequencyMin": cpmAcInfFrequencyMin,
       "cpmAcInfFrequencyMax": cpmAcInfFrequencyMax,
       "cpmAcInfeedLine": cpmAcInfeedLine,
       "cpmAcInfeedLineEntry": cpmAcInfeedLineEntry,
       "cpmAcInfeedLineIndex": cpmAcInfeedLineIndex,
       "cpmAcInfLineCurrent": cpmAcInfLineCurrent,
       "cpmAcInfLineCurrentMin": cpmAcInfLineCurrentMin,
       "cpmAcInfLineCurrentMax": cpmAcInfLineCurrentMax,
       "cpmAcInfLineCurrRatPctOf": cpmAcInfLineCurrRatPctOf,
       "cpmAcInfLineCurrMinAlarm": cpmAcInfLineCurrMinAlarm,
       "cpmAcInfLineCurrMaxAlarm": cpmAcInfLineCurrMaxAlarm,
       "cpmAcInfLineCurrDemand": cpmAcInfLineCurrDemand,
       "cpmAcInfLineCurrPeakDmd": cpmAcInfLineCurrPeakDmd,
       "cpmAcInfeedPhase": cpmAcInfeedPhase,
       "cpmAcInfeedPhaseEntry": cpmAcInfeedPhaseEntry,
       "cpmAcInfeedPhaseIndex": cpmAcInfeedPhaseIndex,
       "cpmAcLineToNeutVoltage": cpmAcLineToNeutVoltage,
       "cpmAcLineToLineVoltage": cpmAcLineToLineVoltage,
       "cpmAcLineToLineVoltMin": cpmAcLineToLineVoltMin,
       "cpmAcLineToLineVoltMax": cpmAcLineToLineVoltMax,
       "cpmAcLinToLinVoltMinAlm": cpmAcLinToLinVoltMinAlm,
       "cpmAcLinToLinVoltMaxAlm": cpmAcLinToLinVoltMaxAlm,
       "cpmAcInfPhasePowerFactor": cpmAcInfPhasePowerFactor,
       "cpmAcInfPhaseApparentPwr": cpmAcInfPhaseApparentPwr,
       "cpmAcInfPhaseActivePower": cpmAcInfPhaseActivePower,
       "cpmAcInfPhasePeakActPwr": cpmAcInfPhasePeakActPwr,
       "cpmAcInfPhaseReactivePwr": cpmAcInfPhaseReactivePwr,
       "cpmAcInfPhaseEnergy": cpmAcInfPhaseEnergy,
       "cpmAcLineToNeutVoltMin": cpmAcLineToNeutVoltMin,
       "cpmAcLineToNeutVoltMax": cpmAcLineToNeutVoltMax,
       "cpmAcLinToNeutVoltMinAlm": cpmAcLinToNeutVoltMinAlm,
       "cpmAcLinToNeutVoltMaxAlm": cpmAcLinToNeutVoltMaxAlm,
       "cpmAcOutlet": cpmAcOutlet,
       "cpmAcOutletEntry": cpmAcOutletEntry,
       "cpmAcOutletIndex": cpmAcOutletIndex,
       "cpmAcOutletId": cpmAcOutletId,
       "cpmAcOtlLineCurrRating": cpmAcOtlLineCurrRating,
       "cpmAcOtlDemandTime": cpmAcOtlDemandTime,
       "cpmAcOtlTotalActivePower": cpmAcOtlTotalActivePower,
       "cpmAcOtlPeakTotActivePwr": cpmAcOtlPeakTotActivePwr,
       "cpmAcOtlTotalReactivePwr": cpmAcOtlTotalReactivePwr,
       "cpmAcOtlTotalApparentPwr": cpmAcOtlTotalApparentPwr,
       "cpmAcOtlTotalPowerFactor": cpmAcOtlTotalPowerFactor,
       "cpmAcOtlTotalEnergy": cpmAcOtlTotalEnergy,
       "cpmAcOtlCurrentMinAlarm": cpmAcOtlCurrentMinAlarm,
       "cpmAcOtlCurrentMaxAlarm": cpmAcOtlCurrentMaxAlarm,
       "cpmAcOutletLine": cpmAcOutletLine,
       "cpmAcOutletLineEntry": cpmAcOutletLineEntry,
       "cpmAcOutletOutletIndex": cpmAcOutletOutletIndex,
       "cpmAcOutletLineIndex": cpmAcOutletLineIndex,
       "cpmAcOtlPhaseId": cpmAcOtlPhaseId,
       "cpmAcOtlLineCurrent": cpmAcOtlLineCurrent,
       "cpmAcOtlLineCurrRatPctOf": cpmAcOtlLineCurrRatPctOf,
       "cpmAcOtlLineCurrDemand": cpmAcOtlLineCurrDemand,
       "cpmAcOtlLineCurrPeakDmd": cpmAcOtlLineCurrPeakDmd,
       "cpmAcOtlLineCurrentMin": cpmAcOtlLineCurrentMin,
       "cpmAcOtlLineCurrentMax": cpmAcOtlLineCurrentMax,
       "cpmAcAlarms": cpmAcAlarms,
       "cpmAcInfeedAlarmStatus": cpmAcInfeedAlarmStatus,
       "cpmAcOutletAlarmStatus": cpmAcOutletAlarmStatus,
       "cpmAcOutletAlarmStatus2": cpmAcOutletAlarmStatus2,
       "cpmAcTempAlarmStatus": cpmAcTempAlarmStatus,
       "cpmAcDiagnostics": cpmAcDiagnostics,
       "cpmAcFirstErrorMessage": cpmAcFirstErrorMessage,
       "cpmAcLastErrorMessage": cpmAcLastErrorMessage,
       "cpmAcTempMonitor": cpmAcTempMonitor,
       "cpmAcEnclosureTemp": cpmAcEnclosureTemp,
       "cpmAcEnclosureTempMax": cpmAcEnclosureTempMax,
       "cpmAcEncSysMaxTempAlmThr": cpmAcEncSysMaxTempAlmThr,
       "cpmAcEncUsrMaxTempAlmThr": cpmAcEncUsrMaxTempAlmThr,
       "cpmAcBatVoltMinAlmThr": cpmAcBatVoltMinAlmThr,
       "cpmAcTempNode": cpmAcTempNode,
       "cpmAcTempNodeEntry": cpmAcTempNodeEntry,
       "cpmAcNodeIndex": cpmAcNodeIndex,
       "cpmAcNodeId": cpmAcNodeId,
       "cpmAcNodeTemperature": cpmAcNodeTemperature,
       "cpmAcNodeTemperatureMax": cpmAcNodeTemperatureMax,
       "cpmAcNodeSysMaxAlmThresh": cpmAcNodeSysMaxAlmThresh,
       "cpmAcNodeUsrMaxAlmThresh": cpmAcNodeUsrMaxAlmThresh,
       "cpmAcNodeBatteryVoltage": cpmAcNodeBatteryVoltage,
       "cpmAcNotifications": cpmAcNotifications,
       "cpmAcEvents": cpmAcEvents,
       "cpmAcInfOvCurrAssertEv": cpmAcInfOvCurrAssertEv,
       "cpmAcInfOvCurrDeassertEv": cpmAcInfOvCurrDeassertEv,
       "cpmAcInfUnCurrAssertEv": cpmAcInfUnCurrAssertEv,
       "cpmAcInfUnCurrDeassertEv": cpmAcInfUnCurrDeassertEv,
       "cpmAcInfOvVoltAssertEv": cpmAcInfOvVoltAssertEv,
       "cpmAcInfOvVoltDeassertEv": cpmAcInfOvVoltDeassertEv,
       "cpmAcInfUnVoltAssertEv": cpmAcInfUnVoltAssertEv,
       "cpmAcInfUnVoltDeassertEv": cpmAcInfUnVoltDeassertEv,
       "cpmAcOtlOvCurrAssertEv": cpmAcOtlOvCurrAssertEv,
       "cpmAcOtlOvCurrDeassertEv": cpmAcOtlOvCurrDeassertEv,
       "cpmAcOtlUnCurrAssertEv": cpmAcOtlUnCurrAssertEv,
       "cpmAcOtlUnCurrDeassertEv": cpmAcOtlUnCurrDeassertEv,
       "cpmAcOvTempAssertEv": cpmAcOvTempAssertEv,
       "cpmAcOvTempDeassertEv": cpmAcOvTempDeassertEv,
       "cpmAcBatVoltLowAssertEv": cpmAcBatVoltLowAssertEv,
       "cpmAcBatVoltLowDeassertEv": cpmAcBatVoltLowDeassertEv,
       "cpmDcMeter": cpmDcMeter,
       "cpmDcGeneral": cpmDcGeneral,
       "cpmDcDeviceName": cpmDcDeviceName,
       "cpmDcDeviceLocation": cpmDcDeviceLocation,
       "cpmDcDeviceId": cpmDcDeviceId,
       "cpmDcModelNumber": cpmDcModelNumber,
       "cpmDcSerialNumber": cpmDcSerialNumber,
       "cpmDcCatalogNumber": cpmDcCatalogNumber,
       "cpmDcFirmwareVersion": cpmDcFirmwareVersion,
       "cpmDcEnergyReset": cpmDcEnergyReset,
       "cpmDcInterfaces": cpmDcInterfaces,
       "cpmDcEthernet": cpmDcEthernet,
       "cpmDcEnetMacAddress": cpmDcEnetMacAddress,
       "cpmDcEnetIpAddress": cpmDcEnetIpAddress,
       "cpmDcEnetIpNetmask": cpmDcEnetIpNetmask,
       "cpmDcEnetIpGateway": cpmDcEnetIpGateway,
       "cpmDcEnetEnableDHCP": cpmDcEnetEnableDHCP,
       "cpmDcEnetStaticIpAddress": cpmDcEnetStaticIpAddress,
       "cpmDcEnetStaticIpNetmask": cpmDcEnetStaticIpNetmask,
       "cpmDcEnetStaticIpGateway": cpmDcEnetStaticIpGateway,
       "cpmDcWifi": cpmDcWifi,
       "cpmDcWifiMacAddress": cpmDcWifiMacAddress,
       "cpmDcWifiIpAddress": cpmDcWifiIpAddress,
       "cpmDcWifiIpNetmask": cpmDcWifiIpNetmask,
       "cpmDcWifiIpGateway": cpmDcWifiIpGateway,
       "cpmDcWifiEnableDHCP": cpmDcWifiEnableDHCP,
       "cpmDcWifiStaticIpAddress": cpmDcWifiStaticIpAddress,
       "cpmDcWifiStaticIpNetmask": cpmDcWifiStaticIpNetmask,
       "cpmDcWifiStaticIpGateway": cpmDcWifiStaticIpGateway,
       "cpmDcWifiSSID": cpmDcWifiSSID,
       "cpmDcWifiEncryptionType": cpmDcWifiEncryptionType,
       "cpmDcModbus": cpmDcModbus,
       "cpmDcModbusAddress": cpmDcModbusAddress,
       "cpmDcModbusBaudRate": cpmDcModbusBaudRate,
       "cpmDcModbusStopBits": cpmDcModbusStopBits,
       "cpmDcModbusParity": cpmDcModbusParity,
       "cpmDcDigitalIo": cpmDcDigitalIo,
       "cpmDcDigitalIoEntry": cpmDcDigitalIoEntry,
       "cpmDcDigitalIoIndex": cpmDcDigitalIoIndex,
       "cpmDcDigitalIoName": cpmDcDigitalIoName,
       "cpmDcDigitalIoValue": cpmDcDigitalIoValue,
       "cpmDcDigitalIoDirection": cpmDcDigitalIoDirection,
       "cpmDcDigitalIoLevel": cpmDcDigitalIoLevel,
       "cpmDcDigitalIoAlarm": cpmDcDigitalIoAlarm,
       "cpmDcAnalogIo": cpmDcAnalogIo,
       "cpmDc4to20maPortName": cpmDc4to20maPortName,
       "cpmDc4to20maValue": cpmDc4to20maValue,
       "cpmDcProtocols": cpmDcProtocols,
       "cpmDcSnmp": cpmDcSnmp,
       "cpmDcSnmpTrapDestAddr1": cpmDcSnmpTrapDestAddr1,
       "cpmDcSnmpTrapDestAddr2": cpmDcSnmpTrapDestAddr2,
       "cpmDcEmail": cpmDcEmail,
       "cpmDcEmailFromAddress": cpmDcEmailFromAddress,
       "cpmDcEmailToAddress": cpmDcEmailToAddress,
       "cpmDcEmailServer": cpmDcEmailServer,
       "cpmDcEmailPort": cpmDcEmailPort,
       "cpmDcEmailAuthEnable": cpmDcEmailAuthEnable,
       "cpmDcEmailLogin": cpmDcEmailLogin,
       "cpmDcEmailPassword": cpmDcEmailPassword,
       "cpmDcSntp": cpmDcSntp,
       "cpmDcSntpServer": cpmDcSntpServer,
       "cpmDcTelnet": cpmDcTelnet,
       "cpmDcInfeed": cpmDcInfeed,
       "cpmDcInfDemandTime": cpmDcInfDemandTime,
       "cpmDcInfCktCurrRating": cpmDcInfCktCurrRating,
       "cpmDcInfCircuit": cpmDcInfCircuit,
       "cpmDcInfCircuitEntry": cpmDcInfCircuitEntry,
       "cpmDcInfeedCircuitIndex": cpmDcInfeedCircuitIndex,
       "cpmDcCktVoltage": cpmDcCktVoltage,
       "cpmDcCktVoltageMin": cpmDcCktVoltageMin,
       "cpmDcCktVoltageMax": cpmDcCktVoltageMax,
       "cpmDcCktVoltageMinAlarm": cpmDcCktVoltageMinAlarm,
       "cpmDcCktVoltageMaxAlarm": cpmDcCktVoltageMaxAlarm,
       "cpmDcInfCktPower": cpmDcInfCktPower,
       "cpmDcInfCktPeakPower": cpmDcInfCktPeakPower,
       "cpmDcInfCktEnergyDelivrd": cpmDcInfCktEnergyDelivrd,
       "cpmDcInfCktEnergyRcvd": cpmDcInfCktEnergyRcvd,
       "cpmDcInfCktCurrent": cpmDcInfCktCurrent,
       "cpmDcInfCktCurrentMin": cpmDcInfCktCurrentMin,
       "cpmDcInfCktCurrentMax": cpmDcInfCktCurrentMax,
       "cpmDcInfCktCurrRatPctOf": cpmDcInfCktCurrRatPctOf,
       "cpmDcInfCktCurrMinAlarm": cpmDcInfCktCurrMinAlarm,
       "cpmDcInfCktCurrMaxAlarm": cpmDcInfCktCurrMaxAlarm,
       "cpmDcInfCktCurrDemand": cpmDcInfCktCurrDemand,
       "cpmDcInfCktCurrPeakDmd": cpmDcInfCktCurrPeakDmd,
       "cpmDcOutlet": cpmDcOutlet,
       "cpmDcOutletEntry": cpmDcOutletEntry,
       "cpmDcOutletIndex": cpmDcOutletIndex,
       "cpmDcOutletId": cpmDcOutletId,
       "cpmDcOtlCktCurrRating": cpmDcOtlCktCurrRating,
       "cpmDcOtlDemandTime": cpmDcOtlDemandTime,
       "cpmDcOtlCurrentMinAlarm": cpmDcOtlCurrentMinAlarm,
       "cpmDcOtlCurrentMaxAlarm": cpmDcOtlCurrentMaxAlarm,
       "cpmDcOutletCircuit": cpmDcOutletCircuit,
       "cpmDcOutletCircuitEntry": cpmDcOutletCircuitEntry,
       "cpmDcOutletOutletIndex": cpmDcOutletOutletIndex,
       "cpmDcOutletCircuitIndex": cpmDcOutletCircuitIndex,
       "cpmDcOtlCktCurrent": cpmDcOtlCktCurrent,
       "cpmDcOtlCktCurrRatPctOf": cpmDcOtlCktCurrRatPctOf,
       "cpmDcOtlCktCurrentDemand": cpmDcOtlCktCurrentDemand,
       "cpmDcOtlCktCurrPeakDmd": cpmDcOtlCktCurrPeakDmd,
       "cpmDcOtlCktCurrentMin": cpmDcOtlCktCurrentMin,
       "cpmDcOtlCktCurrentMax": cpmDcOtlCktCurrentMax,
       "cpmDcOtlCktPower": cpmDcOtlCktPower,
       "cpmDcOtlCktPeakPower": cpmDcOtlCktPeakPower,
       "cpmDcOtlCktEnergyDelivrd": cpmDcOtlCktEnergyDelivrd,
       "cpmDcOtlCktEnergyRcvd": cpmDcOtlCktEnergyRcvd,
       "cpmDcAlarms": cpmDcAlarms,
       "cpmDcInfeedAlarmStatus": cpmDcInfeedAlarmStatus,
       "cpmDcOutletAlarmStatus": cpmDcOutletAlarmStatus,
       "cpmDcDiagnostics": cpmDcDiagnostics,
       "cpmDcFirstErrorMessage": cpmDcFirstErrorMessage,
       "cpmDcLastErrorMessage": cpmDcLastErrorMessage,
       "cpmDcNotifications": cpmDcNotifications,
       "cpmDcEvents": cpmDcEvents,
       "cpmDcInfOvCurrAssertEv": cpmDcInfOvCurrAssertEv,
       "cpmDcInfOvCurrDeassertEv": cpmDcInfOvCurrDeassertEv,
       "cpmDcInfUnCurrAssertEv": cpmDcInfUnCurrAssertEv,
       "cpmDcInfUnCurrDeassertEv": cpmDcInfUnCurrDeassertEv,
       "cpmDcInfOvVoltAssertEv": cpmDcInfOvVoltAssertEv,
       "cpmDcInfOvVoltDeassertEv": cpmDcInfOvVoltDeassertEv,
       "cpmDcInfUnVoltAssertEv": cpmDcInfUnVoltAssertEv,
       "cpmDcInfUnVoltDeassertEv": cpmDcInfUnVoltDeassertEv,
       "cpmDcOtlOvCurrAssertEv": cpmDcOtlOvCurrAssertEv,
       "cpmDcOtlOvCurrDeassertEv": cpmDcOtlOvCurrDeassertEv,
       "cpmDcOtlUnCurrAssertEv": cpmDcOtlUnCurrAssertEv,
       "cpmDcOtlUnCurrDeassertEv": cpmDcOtlUnCurrDeassertEv}
)
