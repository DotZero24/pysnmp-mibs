# SNMP MIB module (TERACOM-TCW181B-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/teracom/TERACOM-TCW181B-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:59:52 2025
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
 iso,
 snmpModules) = mibBuilder.importSymbols(
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
    "iso",
    "snmpModules")

(DisplayString,
 MacAddress,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

snmpMIB = ModuleIdentity(
    (1, 3, 6, 1, 6, 3, 1)
)
if mibBuilder.loadTexts:
    snmpMIB.setRevisions(
        ("2017-01-26 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Teracom_ObjectIdentity = ObjectIdentity
teracom = _Teracom_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38783)
)
_TrapNotifications_ObjectIdentity = ObjectIdentity
trapNotifications = _TrapNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38783, 0)
)
_Product_ObjectIdentity = ObjectIdentity
product = _Product_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38783, 1)
)
_Name_Type = DisplayString
_Name_Object = MibScalar
name = _Name_Object(
    (1, 3, 6, 1, 4, 1, 38783, 1, 1),
    _Name_Type()
)
name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    name.setStatus("current")
_Version_Type = DisplayString
_Version_Object = MibScalar
version = _Version_Object(
    (1, 3, 6, 1, 4, 1, 38783, 1, 2),
    _Version_Type()
)
version.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    version.setStatus("current")
_Date_Type = DisplayString
_Date_Object = MibScalar
date = _Date_Object(
    (1, 3, 6, 1, 4, 1, 38783, 1, 3),
    _Date_Type()
)
date.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    date.setStatus("current")
_SnmpSetup_ObjectIdentity = ObjectIdentity
snmpSetup = _SnmpSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38783, 2)
)


class _TrapEnabled_Type(Integer32):
    """Custom type trapEnabled based on Integer32"""
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


_TrapEnabled_Type.__name__ = "Integer32"
_TrapEnabled_Object = MibScalar
trapEnabled = _TrapEnabled_Object(
    (1, 3, 6, 1, 4, 1, 38783, 2, 1),
    _TrapEnabled_Type()
)
trapEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapEnabled.setStatus("current")
_TrapReceiverIPAddress_Type = IpAddress
_TrapReceiverIPAddress_Object = MibScalar
trapReceiverIPAddress = _TrapReceiverIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 38783, 2, 2),
    _TrapReceiverIPAddress_Type()
)
trapReceiverIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapReceiverIPAddress.setStatus("current")


class _TrapCommunity_Type(DisplayString):
    """Custom type trapCommunity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 13),
    )


_TrapCommunity_Type.__name__ = "DisplayString"
_TrapCommunity_Object = MibScalar
trapCommunity = _TrapCommunity_Object(
    (1, 3, 6, 1, 4, 1, 38783, 2, 3),
    _TrapCommunity_Type()
)
trapCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapCommunity.setStatus("current")
_MonitorNcontrol_ObjectIdentity = ObjectIdentity
monitorNcontrol = _MonitorNcontrol_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38783, 3)
)


class _DigitalInput_Type(Integer32):
    """Custom type digitalInput based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("closed", 0),
          ("open", 1))
    )


_DigitalInput_Type.__name__ = "Integer32"
_DigitalInput_Object = MibScalar
digitalInput = _DigitalInput_Object(
    (1, 3, 6, 1, 4, 1, 38783, 3, 1),
    _DigitalInput_Type()
)
digitalInput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalInput.setStatus("current")


class _Relay1_Type(Integer32):
    """Custom type relay1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_Relay1_Type.__name__ = "Integer32"
_Relay1_Object = MibScalar
relay1 = _Relay1_Object(
    (1, 3, 6, 1, 4, 1, 38783, 3, 2),
    _Relay1_Type()
)
relay1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    relay1.setStatus("current")


class _Relay2_Type(Integer32):
    """Custom type relay2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_Relay2_Type.__name__ = "Integer32"
_Relay2_Object = MibScalar
relay2 = _Relay2_Object(
    (1, 3, 6, 1, 4, 1, 38783, 3, 3),
    _Relay2_Type()
)
relay2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    relay2.setStatus("current")


class _Relay3_Type(Integer32):
    """Custom type relay3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_Relay3_Type.__name__ = "Integer32"
_Relay3_Object = MibScalar
relay3 = _Relay3_Object(
    (1, 3, 6, 1, 4, 1, 38783, 3, 4),
    _Relay3_Type()
)
relay3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    relay3.setStatus("current")


class _Relay4_Type(Integer32):
    """Custom type relay4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_Relay4_Type.__name__ = "Integer32"
_Relay4_Object = MibScalar
relay4 = _Relay4_Object(
    (1, 3, 6, 1, 4, 1, 38783, 3, 5),
    _Relay4_Type()
)
relay4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    relay4.setStatus("current")


class _Relay5_Type(Integer32):
    """Custom type relay5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_Relay5_Type.__name__ = "Integer32"
_Relay5_Object = MibScalar
relay5 = _Relay5_Object(
    (1, 3, 6, 1, 4, 1, 38783, 3, 6),
    _Relay5_Type()
)
relay5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    relay5.setStatus("current")


class _Relay6_Type(Integer32):
    """Custom type relay6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_Relay6_Type.__name__ = "Integer32"
_Relay6_Object = MibScalar
relay6 = _Relay6_Object(
    (1, 3, 6, 1, 4, 1, 38783, 3, 7),
    _Relay6_Type()
)
relay6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    relay6.setStatus("current")


class _Relay7_Type(Integer32):
    """Custom type relay7 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_Relay7_Type.__name__ = "Integer32"
_Relay7_Object = MibScalar
relay7 = _Relay7_Object(
    (1, 3, 6, 1, 4, 1, 38783, 3, 8),
    _Relay7_Type()
)
relay7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    relay7.setStatus("current")


class _Relay8_Type(Integer32):
    """Custom type relay8 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_Relay8_Type.__name__ = "Integer32"
_Relay8_Object = MibScalar
relay8 = _Relay8_Object(
    (1, 3, 6, 1, 4, 1, 38783, 3, 9),
    _Relay8_Type()
)
relay8.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    relay8.setStatus("current")


class _Pulse1_Type(Integer32):
    """Custom type pulse1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_Pulse1_Type.__name__ = "Integer32"
_Pulse1_Object = MibScalar
pulse1 = _Pulse1_Object(
    (1, 3, 6, 1, 4, 1, 38783, 3, 10),
    _Pulse1_Type()
)
pulse1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pulse1.setStatus("current")


class _Pulse2_Type(Integer32):
    """Custom type pulse2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_Pulse2_Type.__name__ = "Integer32"
_Pulse2_Object = MibScalar
pulse2 = _Pulse2_Object(
    (1, 3, 6, 1, 4, 1, 38783, 3, 11),
    _Pulse2_Type()
)
pulse2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pulse2.setStatus("current")


class _Pulse3_Type(Integer32):
    """Custom type pulse3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_Pulse3_Type.__name__ = "Integer32"
_Pulse3_Object = MibScalar
pulse3 = _Pulse3_Object(
    (1, 3, 6, 1, 4, 1, 38783, 3, 12),
    _Pulse3_Type()
)
pulse3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pulse3.setStatus("current")


class _Pulse4_Type(Integer32):
    """Custom type pulse4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_Pulse4_Type.__name__ = "Integer32"
_Pulse4_Object = MibScalar
pulse4 = _Pulse4_Object(
    (1, 3, 6, 1, 4, 1, 38783, 3, 13),
    _Pulse4_Type()
)
pulse4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pulse4.setStatus("current")


class _Pulse5_Type(Integer32):
    """Custom type pulse5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_Pulse5_Type.__name__ = "Integer32"
_Pulse5_Object = MibScalar
pulse5 = _Pulse5_Object(
    (1, 3, 6, 1, 4, 1, 38783, 3, 14),
    _Pulse5_Type()
)
pulse5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pulse5.setStatus("current")


class _Pulse6_Type(Integer32):
    """Custom type pulse6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_Pulse6_Type.__name__ = "Integer32"
_Pulse6_Object = MibScalar
pulse6 = _Pulse6_Object(
    (1, 3, 6, 1, 4, 1, 38783, 3, 15),
    _Pulse6_Type()
)
pulse6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pulse6.setStatus("current")


class _Pulse7_Type(Integer32):
    """Custom type pulse7 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_Pulse7_Type.__name__ = "Integer32"
_Pulse7_Object = MibScalar
pulse7 = _Pulse7_Object(
    (1, 3, 6, 1, 4, 1, 38783, 3, 16),
    _Pulse7_Type()
)
pulse7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pulse7.setStatus("current")


class _Pulse8_Type(Integer32):
    """Custom type pulse8 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_Pulse8_Type.__name__ = "Integer32"
_Pulse8_Object = MibScalar
pulse8 = _Pulse8_Object(
    (1, 3, 6, 1, 4, 1, 38783, 3, 17),
    _Pulse8_Type()
)
pulse8.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pulse8.setStatus("current")


class _AllOn_Type(Integer32):
    """Custom type allOn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_AllOn_Type.__name__ = "Integer32"
_AllOn_Object = MibScalar
allOn = _AllOn_Object(
    (1, 3, 6, 1, 4, 1, 38783, 3, 18),
    _AllOn_Type()
)
allOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    allOn.setStatus("current")


class _AllOff_Type(Integer32):
    """Custom type allOff based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_AllOff_Type.__name__ = "Integer32"
_AllOff_Object = MibScalar
allOff = _AllOff_Object(
    (1, 3, 6, 1, 4, 1, 38783, 3, 19),
    _AllOff_Type()
)
allOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    allOff.setStatus("current")


class _AllPulse_Type(Integer32):
    """Custom type allPulse based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_AllPulse_Type.__name__ = "Integer32"
_AllPulse_Object = MibScalar
allPulse = _AllPulse_Object(
    (1, 3, 6, 1, 4, 1, 38783, 3, 20),
    _AllPulse_Type()
)
allPulse.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    allPulse.setStatus("current")
_Network_ObjectIdentity = ObjectIdentity
network = _Network_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38783, 4)
)
_DeviceIPAddress_Type = IpAddress
_DeviceIPAddress_Object = MibScalar
deviceIPAddress = _DeviceIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 38783, 4, 1),
    _DeviceIPAddress_Type()
)
deviceIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    deviceIPAddress.setStatus("current")
_SubnetMask_Type = IpAddress
_SubnetMask_Object = MibScalar
subnetMask = _SubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 38783, 4, 2),
    _SubnetMask_Type()
)
subnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    subnetMask.setStatus("current")
_Gateway_Type = IpAddress
_Gateway_Object = MibScalar
gateway = _Gateway_Object(
    (1, 3, 6, 1, 4, 1, 38783, 4, 3),
    _Gateway_Type()
)
gateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gateway.setStatus("current")
_DeviceMACAddress_Type = MacAddress
_DeviceMACAddress_Object = MibScalar
deviceMACAddress = _DeviceMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 38783, 4, 4),
    _DeviceMACAddress_Type()
)
deviceMACAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    deviceMACAddress.setStatus("current")


class _DhcpConfig_Type(Integer32):
    """Custom type dhcpConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_DhcpConfig_Type.__name__ = "Integer32"
_DhcpConfig_Object = MibScalar
dhcpConfig = _DhcpConfig_Object(
    (1, 3, 6, 1, 4, 1, 38783, 4, 5),
    _DhcpConfig_Type()
)
dhcpConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpConfig.setStatus("current")
_IoSetup_ObjectIdentity = ObjectIdentity
ioSetup = _IoSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38783, 5)
)


class _Relay1PulseDuration_Type(Integer32):
    """Custom type relay1PulseDuration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 253),
    )


_Relay1PulseDuration_Type.__name__ = "Integer32"
_Relay1PulseDuration_Object = MibScalar
relay1PulseDuration = _Relay1PulseDuration_Object(
    (1, 3, 6, 1, 4, 1, 38783, 5, 1),
    _Relay1PulseDuration_Type()
)
relay1PulseDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    relay1PulseDuration.setStatus("current")


class _Relay2PulseDuration_Type(Integer32):
    """Custom type relay2PulseDuration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 253),
    )


_Relay2PulseDuration_Type.__name__ = "Integer32"
_Relay2PulseDuration_Object = MibScalar
relay2PulseDuration = _Relay2PulseDuration_Object(
    (1, 3, 6, 1, 4, 1, 38783, 5, 2),
    _Relay2PulseDuration_Type()
)
relay2PulseDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    relay2PulseDuration.setStatus("current")


class _Relay3PulseDuration_Type(Integer32):
    """Custom type relay3PulseDuration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 253),
    )


_Relay3PulseDuration_Type.__name__ = "Integer32"
_Relay3PulseDuration_Object = MibScalar
relay3PulseDuration = _Relay3PulseDuration_Object(
    (1, 3, 6, 1, 4, 1, 38783, 5, 3),
    _Relay3PulseDuration_Type()
)
relay3PulseDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    relay3PulseDuration.setStatus("current")


class _Relay4PulseDuration_Type(Integer32):
    """Custom type relay4PulseDuration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 253),
    )


_Relay4PulseDuration_Type.__name__ = "Integer32"
_Relay4PulseDuration_Object = MibScalar
relay4PulseDuration = _Relay4PulseDuration_Object(
    (1, 3, 6, 1, 4, 1, 38783, 5, 4),
    _Relay4PulseDuration_Type()
)
relay4PulseDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    relay4PulseDuration.setStatus("current")


class _Relay5PulseDuration_Type(Integer32):
    """Custom type relay5PulseDuration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 253),
    )


_Relay5PulseDuration_Type.__name__ = "Integer32"
_Relay5PulseDuration_Object = MibScalar
relay5PulseDuration = _Relay5PulseDuration_Object(
    (1, 3, 6, 1, 4, 1, 38783, 5, 5),
    _Relay5PulseDuration_Type()
)
relay5PulseDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    relay5PulseDuration.setStatus("current")


class _Relay6PulseDuration_Type(Integer32):
    """Custom type relay6PulseDuration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 253),
    )


_Relay6PulseDuration_Type.__name__ = "Integer32"
_Relay6PulseDuration_Object = MibScalar
relay6PulseDuration = _Relay6PulseDuration_Object(
    (1, 3, 6, 1, 4, 1, 38783, 5, 6),
    _Relay6PulseDuration_Type()
)
relay6PulseDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    relay6PulseDuration.setStatus("current")


class _Relay7PulseDuration_Type(Integer32):
    """Custom type relay7PulseDuration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 253),
    )


_Relay7PulseDuration_Type.__name__ = "Integer32"
_Relay7PulseDuration_Object = MibScalar
relay7PulseDuration = _Relay7PulseDuration_Object(
    (1, 3, 6, 1, 4, 1, 38783, 5, 7),
    _Relay7PulseDuration_Type()
)
relay7PulseDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    relay7PulseDuration.setStatus("current")


class _Relay8PulseDuration_Type(Integer32):
    """Custom type relay8PulseDuration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 253),
    )


_Relay8PulseDuration_Type.__name__ = "Integer32"
_Relay8PulseDuration_Object = MibScalar
relay8PulseDuration = _Relay8PulseDuration_Object(
    (1, 3, 6, 1, 4, 1, 38783, 5, 8),
    _Relay8PulseDuration_Type()
)
relay8PulseDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    relay8PulseDuration.setStatus("current")


class _Relay1description_Type(DisplayString):
    """Custom type relay1description based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 11),
    )


_Relay1description_Type.__name__ = "DisplayString"
_Relay1description_Object = MibScalar
relay1description = _Relay1description_Object(
    (1, 3, 6, 1, 4, 1, 38783, 5, 9),
    _Relay1description_Type()
)
relay1description.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    relay1description.setStatus("current")


class _Relay2description_Type(DisplayString):
    """Custom type relay2description based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 11),
    )


_Relay2description_Type.__name__ = "DisplayString"
_Relay2description_Object = MibScalar
relay2description = _Relay2description_Object(
    (1, 3, 6, 1, 4, 1, 38783, 5, 10),
    _Relay2description_Type()
)
relay2description.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    relay2description.setStatus("current")


class _Relay3description_Type(DisplayString):
    """Custom type relay3description based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 11),
    )


_Relay3description_Type.__name__ = "DisplayString"
_Relay3description_Object = MibScalar
relay3description = _Relay3description_Object(
    (1, 3, 6, 1, 4, 1, 38783, 5, 11),
    _Relay3description_Type()
)
relay3description.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    relay3description.setStatus("current")


class _Relay4description_Type(DisplayString):
    """Custom type relay4description based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 11),
    )


_Relay4description_Type.__name__ = "DisplayString"
_Relay4description_Object = MibScalar
relay4description = _Relay4description_Object(
    (1, 3, 6, 1, 4, 1, 38783, 5, 12),
    _Relay4description_Type()
)
relay4description.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    relay4description.setStatus("current")


class _Relay5description_Type(DisplayString):
    """Custom type relay5description based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 11),
    )


_Relay5description_Type.__name__ = "DisplayString"
_Relay5description_Object = MibScalar
relay5description = _Relay5description_Object(
    (1, 3, 6, 1, 4, 1, 38783, 5, 13),
    _Relay5description_Type()
)
relay5description.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    relay5description.setStatus("current")


class _Relay6description_Type(DisplayString):
    """Custom type relay6description based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 11),
    )


_Relay6description_Type.__name__ = "DisplayString"
_Relay6description_Object = MibScalar
relay6description = _Relay6description_Object(
    (1, 3, 6, 1, 4, 1, 38783, 5, 14),
    _Relay6description_Type()
)
relay6description.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    relay6description.setStatus("current")


class _Relay7description_Type(DisplayString):
    """Custom type relay7description based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 11),
    )


_Relay7description_Type.__name__ = "DisplayString"
_Relay7description_Object = MibScalar
relay7description = _Relay7description_Object(
    (1, 3, 6, 1, 4, 1, 38783, 5, 15),
    _Relay7description_Type()
)
relay7description.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    relay7description.setStatus("current")


class _Relay8description_Type(DisplayString):
    """Custom type relay8description based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 11),
    )


_Relay8description_Type.__name__ = "DisplayString"
_Relay8description_Object = MibScalar
relay8description = _Relay8description_Object(
    (1, 3, 6, 1, 4, 1, 38783, 5, 16),
    _Relay8description_Type()
)
relay8description.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    relay8description.setStatus("current")


class _DigitalInputAction_Type(Integer32):
    """Custom type digitalInputAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noAction", 0),
          ("mailIfOpenToClosed", 1),
          ("mailIfClosedToOpen", 2))
    )


_DigitalInputAction_Type.__name__ = "Integer32"
_DigitalInputAction_Object = MibScalar
digitalInputAction = _DigitalInputAction_Object(
    (1, 3, 6, 1, 4, 1, 38783, 5, 17),
    _DigitalInputAction_Type()
)
digitalInputAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    digitalInputAction.setStatus("current")


class _DigitalInputTo_Type(DisplayString):
    """Custom type digitalInputTo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 38),
    )


_DigitalInputTo_Type.__name__ = "DisplayString"
_DigitalInputTo_Object = MibScalar
digitalInputTo = _DigitalInputTo_Object(
    (1, 3, 6, 1, 4, 1, 38783, 5, 18),
    _DigitalInputTo_Type()
)
digitalInputTo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    digitalInputTo.setStatus("current")


class _DigitalInputSubject_Type(DisplayString):
    """Custom type digitalInputSubject based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 11),
    )


_DigitalInputSubject_Type.__name__ = "DisplayString"
_DigitalInputSubject_Object = MibScalar
digitalInputSubject = _DigitalInputSubject_Object(
    (1, 3, 6, 1, 4, 1, 38783, 5, 19),
    _DigitalInputSubject_Type()
)
digitalInputSubject.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    digitalInputSubject.setStatus("current")


class _DigitalInputBody_Type(DisplayString):
    """Custom type digitalInputBody based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 22),
    )


_DigitalInputBody_Type.__name__ = "DisplayString"
_DigitalInputBody_Object = MibScalar
digitalInputBody = _DigitalInputBody_Object(
    (1, 3, 6, 1, 4, 1, 38783, 5, 20),
    _DigitalInputBody_Type()
)
digitalInputBody.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    digitalInputBody.setStatus("current")


class _Relay1PulseDurationMs_Type(Integer32):
    """Custom type relay1PulseDurationMs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_Relay1PulseDurationMs_Type.__name__ = "Integer32"
_Relay1PulseDurationMs_Object = MibScalar
relay1PulseDurationMs = _Relay1PulseDurationMs_Object(
    (1, 3, 6, 1, 4, 1, 38783, 5, 21),
    _Relay1PulseDurationMs_Type()
)
relay1PulseDurationMs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    relay1PulseDurationMs.setStatus("current")


class _Relay2PulseDurationMs_Type(Integer32):
    """Custom type relay2PulseDurationMs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_Relay2PulseDurationMs_Type.__name__ = "Integer32"
_Relay2PulseDurationMs_Object = MibScalar
relay2PulseDurationMs = _Relay2PulseDurationMs_Object(
    (1, 3, 6, 1, 4, 1, 38783, 5, 22),
    _Relay2PulseDurationMs_Type()
)
relay2PulseDurationMs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    relay2PulseDurationMs.setStatus("current")


class _Relay3PulseDurationMs_Type(Integer32):
    """Custom type relay3PulseDurationMs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_Relay3PulseDurationMs_Type.__name__ = "Integer32"
_Relay3PulseDurationMs_Object = MibScalar
relay3PulseDurationMs = _Relay3PulseDurationMs_Object(
    (1, 3, 6, 1, 4, 1, 38783, 5, 23),
    _Relay3PulseDurationMs_Type()
)
relay3PulseDurationMs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    relay3PulseDurationMs.setStatus("current")


class _Relay4PulseDurationMs_Type(Integer32):
    """Custom type relay4PulseDurationMs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_Relay4PulseDurationMs_Type.__name__ = "Integer32"
_Relay4PulseDurationMs_Object = MibScalar
relay4PulseDurationMs = _Relay4PulseDurationMs_Object(
    (1, 3, 6, 1, 4, 1, 38783, 5, 24),
    _Relay4PulseDurationMs_Type()
)
relay4PulseDurationMs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    relay4PulseDurationMs.setStatus("current")


class _Relay5PulseDurationMs_Type(Integer32):
    """Custom type relay5PulseDurationMs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_Relay5PulseDurationMs_Type.__name__ = "Integer32"
_Relay5PulseDurationMs_Object = MibScalar
relay5PulseDurationMs = _Relay5PulseDurationMs_Object(
    (1, 3, 6, 1, 4, 1, 38783, 5, 25),
    _Relay5PulseDurationMs_Type()
)
relay5PulseDurationMs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    relay5PulseDurationMs.setStatus("current")


class _Relay6PulseDurationMs_Type(Integer32):
    """Custom type relay6PulseDurationMs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_Relay6PulseDurationMs_Type.__name__ = "Integer32"
_Relay6PulseDurationMs_Object = MibScalar
relay6PulseDurationMs = _Relay6PulseDurationMs_Object(
    (1, 3, 6, 1, 4, 1, 38783, 5, 26),
    _Relay6PulseDurationMs_Type()
)
relay6PulseDurationMs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    relay6PulseDurationMs.setStatus("current")


class _Relay7PulseDurationMs_Type(Integer32):
    """Custom type relay7PulseDurationMs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_Relay7PulseDurationMs_Type.__name__ = "Integer32"
_Relay7PulseDurationMs_Object = MibScalar
relay7PulseDurationMs = _Relay7PulseDurationMs_Object(
    (1, 3, 6, 1, 4, 1, 38783, 5, 27),
    _Relay7PulseDurationMs_Type()
)
relay7PulseDurationMs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    relay7PulseDurationMs.setStatus("current")


class _Relay8PulseDurationMs_Type(Integer32):
    """Custom type relay8PulseDurationMs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_Relay8PulseDurationMs_Type.__name__ = "Integer32"
_Relay8PulseDurationMs_Object = MibScalar
relay8PulseDurationMs = _Relay8PulseDurationMs_Object(
    (1, 3, 6, 1, 4, 1, 38783, 5, 28),
    _Relay8PulseDurationMs_Type()
)
relay8PulseDurationMs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    relay8PulseDurationMs.setStatus("current")


class _DigitalInputDescription_Type(DisplayString):
    """Custom type digitalInputDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 11),
    )


_DigitalInputDescription_Type.__name__ = "DisplayString"
_DigitalInputDescription_Object = MibScalar
digitalInputDescription = _DigitalInputDescription_Object(
    (1, 3, 6, 1, 4, 1, 38783, 5, 29),
    _DigitalInputDescription_Type()
)
digitalInputDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    digitalInputDescription.setStatus("current")


class _ConfigurationSaved_Type(Integer32):
    """Custom type configurationSaved based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("unsaved", 0),
          ("saved", 1))
    )


_ConfigurationSaved_Type.__name__ = "Integer32"
_ConfigurationSaved_Object = MibScalar
configurationSaved = _ConfigurationSaved_Object(
    (1, 3, 6, 1, 4, 1, 38783, 6),
    _ConfigurationSaved_Type()
)
configurationSaved.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configurationSaved.setStatus("current")


class _RestartDevice_Type(Integer32):
    """Custom type restartDevice based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("cancel", 0),
          ("restart", 1))
    )


_RestartDevice_Type.__name__ = "Integer32"
_RestartDevice_Object = MibScalar
restartDevice = _RestartDevice_Object(
    (1, 3, 6, 1, 4, 1, 38783, 7),
    _RestartDevice_Type()
)
restartDevice.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    restartDevice.setStatus("current")
_Tcw181bMIBConformance_ObjectIdentity = ObjectIdentity
tcw181bMIBConformance = _Tcw181bMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38783, 8)
)
_Tcw181bMIBCompliances_ObjectIdentity = ObjectIdentity
tcw181bMIBCompliances = _Tcw181bMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38783, 8, 1)
)
_Tcw181bMIBGroups_ObjectIdentity = ObjectIdentity
tcw181bMIBGroups = _Tcw181bMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38783, 8, 2)
)

# Managed Objects groups

tcw181bProductGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 38783, 8, 2, 1)
)
tcw181bProductGroup.setObjects(
      *(("TERACOM-TCW181B-MIB", "name"),
        ("TERACOM-TCW181B-MIB", "version"),
        ("TERACOM-TCW181B-MIB", "date"))
)
if mibBuilder.loadTexts:
    tcw181bProductGroup.setStatus("current")

tcw181bSnmpSetupGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 38783, 8, 2, 2)
)
tcw181bSnmpSetupGroup.setObjects(
      *(("TERACOM-TCW181B-MIB", "trapEnabled"),
        ("TERACOM-TCW181B-MIB", "trapReceiverIPAddress"),
        ("TERACOM-TCW181B-MIB", "trapCommunity"))
)
if mibBuilder.loadTexts:
    tcw181bSnmpSetupGroup.setStatus("current")

tcw181bMonitorGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 38783, 8, 2, 3)
)
tcw181bMonitorGroup.setObjects(
      *(("TERACOM-TCW181B-MIB", "digitalInput"),
        ("TERACOM-TCW181B-MIB", "relay1"),
        ("TERACOM-TCW181B-MIB", "relay2"),
        ("TERACOM-TCW181B-MIB", "relay3"),
        ("TERACOM-TCW181B-MIB", "relay4"),
        ("TERACOM-TCW181B-MIB", "relay5"),
        ("TERACOM-TCW181B-MIB", "relay6"),
        ("TERACOM-TCW181B-MIB", "relay7"),
        ("TERACOM-TCW181B-MIB", "relay8"),
        ("TERACOM-TCW181B-MIB", "pulse1"),
        ("TERACOM-TCW181B-MIB", "pulse2"),
        ("TERACOM-TCW181B-MIB", "pulse3"),
        ("TERACOM-TCW181B-MIB", "pulse4"),
        ("TERACOM-TCW181B-MIB", "pulse5"),
        ("TERACOM-TCW181B-MIB", "pulse6"),
        ("TERACOM-TCW181B-MIB", "pulse7"),
        ("TERACOM-TCW181B-MIB", "pulse8"),
        ("TERACOM-TCW181B-MIB", "allOn"),
        ("TERACOM-TCW181B-MIB", "allOff"),
        ("TERACOM-TCW181B-MIB", "allPulse"))
)
if mibBuilder.loadTexts:
    tcw181bMonitorGroup.setStatus("current")

tcw181bNetworkGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 38783, 8, 2, 4)
)
tcw181bNetworkGroup.setObjects(
      *(("TERACOM-TCW181B-MIB", "deviceIPAddress"),
        ("TERACOM-TCW181B-MIB", "subnetMask"),
        ("TERACOM-TCW181B-MIB", "gateway"),
        ("TERACOM-TCW181B-MIB", "deviceMACAddress"),
        ("TERACOM-TCW181B-MIB", "dhcpConfig"))
)
if mibBuilder.loadTexts:
    tcw181bNetworkGroup.setStatus("current")

tcw181bIOSetupGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 38783, 8, 2, 5)
)
tcw181bIOSetupGroup.setObjects(
      *(("TERACOM-TCW181B-MIB", "relay1PulseDuration"),
        ("TERACOM-TCW181B-MIB", "relay2PulseDuration"),
        ("TERACOM-TCW181B-MIB", "relay3PulseDuration"),
        ("TERACOM-TCW181B-MIB", "relay4PulseDuration"),
        ("TERACOM-TCW181B-MIB", "relay5PulseDuration"),
        ("TERACOM-TCW181B-MIB", "relay6PulseDuration"),
        ("TERACOM-TCW181B-MIB", "relay7PulseDuration"),
        ("TERACOM-TCW181B-MIB", "relay8PulseDuration"),
        ("TERACOM-TCW181B-MIB", "relay1description"),
        ("TERACOM-TCW181B-MIB", "relay2description"),
        ("TERACOM-TCW181B-MIB", "relay3description"),
        ("TERACOM-TCW181B-MIB", "relay4description"),
        ("TERACOM-TCW181B-MIB", "relay5description"),
        ("TERACOM-TCW181B-MIB", "relay6description"),
        ("TERACOM-TCW181B-MIB", "relay7description"),
        ("TERACOM-TCW181B-MIB", "relay8description"),
        ("TERACOM-TCW181B-MIB", "digitalInputAction"),
        ("TERACOM-TCW181B-MIB", "digitalInputTo"),
        ("TERACOM-TCW181B-MIB", "digitalInputSubject"),
        ("TERACOM-TCW181B-MIB", "digitalInputBody"),
        ("TERACOM-TCW181B-MIB", "relay1PulseDurationMs"),
        ("TERACOM-TCW181B-MIB", "relay2PulseDurationMs"),
        ("TERACOM-TCW181B-MIB", "relay3PulseDurationMs"),
        ("TERACOM-TCW181B-MIB", "relay4PulseDurationMs"),
        ("TERACOM-TCW181B-MIB", "relay5PulseDurationMs"),
        ("TERACOM-TCW181B-MIB", "relay6PulseDurationMs"),
        ("TERACOM-TCW181B-MIB", "relay7PulseDurationMs"),
        ("TERACOM-TCW181B-MIB", "relay8PulseDurationMs"),
        ("TERACOM-TCW181B-MIB", "digitalInputDescription"),
        ("TERACOM-TCW181B-MIB", "configurationSaved"),
        ("TERACOM-TCW181B-MIB", "restartDevice"))
)
if mibBuilder.loadTexts:
    tcw181bIOSetupGroup.setStatus("current")


# Notification objects

snmp_trap_notification = NotificationType(
    (1, 3, 6, 1, 4, 1, 38783, 0, 1)
)
snmp_trap_notification.setObjects(
      *(("TERACOM-TCW181B-MIB", "digitalInput"),
        ("TERACOM-TCW181B-MIB", "restartDevice"))
)
if mibBuilder.loadTexts:
    snmp_trap_notification.setStatus(
        "current"
    )


# Notifications groups

tcw181bTrapGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 38783, 8, 2, 8)
)
tcw181bTrapGroup.setObjects(
    ("TERACOM-TCW181B-MIB", "snmp-trap-notification")
)
if mibBuilder.loadTexts:
    tcw181bTrapGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

tcw181bMIBCompliances1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 38783, 8, 1, 1)
)
tcw181bMIBCompliances1.setObjects(
      *(("TERACOM-TCW181B-MIB", "tcw181bProductGroup"),
        ("TERACOM-TCW181B-MIB", "tcw181bSnmpSetupGroup"),
        ("TERACOM-TCW181B-MIB", "tcw181bMonitorGroup"),
        ("TERACOM-TCW181B-MIB", "tcw181bNetworkGroup"),
        ("TERACOM-TCW181B-MIB", "tcw181bIOSetupGroup"),
        ("TERACOM-TCW181B-MIB", "tcw181bTrapGroup"))
)
if mibBuilder.loadTexts:
    tcw181bMIBCompliances1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TERACOM-TCW181B-MIB",
    **{"teracom": teracom,
       "trapNotifications": trapNotifications,
       "snmp-trap-notification": snmp_trap_notification,
       "product": product,
       "name": name,
       "version": version,
       "date": date,
       "snmpSetup": snmpSetup,
       "trapEnabled": trapEnabled,
       "trapReceiverIPAddress": trapReceiverIPAddress,
       "trapCommunity": trapCommunity,
       "monitorNcontrol": monitorNcontrol,
       "digitalInput": digitalInput,
       "relay1": relay1,
       "relay2": relay2,
       "relay3": relay3,
       "relay4": relay4,
       "relay5": relay5,
       "relay6": relay6,
       "relay7": relay7,
       "relay8": relay8,
       "pulse1": pulse1,
       "pulse2": pulse2,
       "pulse3": pulse3,
       "pulse4": pulse4,
       "pulse5": pulse5,
       "pulse6": pulse6,
       "pulse7": pulse7,
       "pulse8": pulse8,
       "allOn": allOn,
       "allOff": allOff,
       "allPulse": allPulse,
       "network": network,
       "deviceIPAddress": deviceIPAddress,
       "subnetMask": subnetMask,
       "gateway": gateway,
       "deviceMACAddress": deviceMACAddress,
       "dhcpConfig": dhcpConfig,
       "ioSetup": ioSetup,
       "relay1PulseDuration": relay1PulseDuration,
       "relay2PulseDuration": relay2PulseDuration,
       "relay3PulseDuration": relay3PulseDuration,
       "relay4PulseDuration": relay4PulseDuration,
       "relay5PulseDuration": relay5PulseDuration,
       "relay6PulseDuration": relay6PulseDuration,
       "relay7PulseDuration": relay7PulseDuration,
       "relay8PulseDuration": relay8PulseDuration,
       "relay1description": relay1description,
       "relay2description": relay2description,
       "relay3description": relay3description,
       "relay4description": relay4description,
       "relay5description": relay5description,
       "relay6description": relay6description,
       "relay7description": relay7description,
       "relay8description": relay8description,
       "digitalInputAction": digitalInputAction,
       "digitalInputTo": digitalInputTo,
       "digitalInputSubject": digitalInputSubject,
       "digitalInputBody": digitalInputBody,
       "relay1PulseDurationMs": relay1PulseDurationMs,
       "relay2PulseDurationMs": relay2PulseDurationMs,
       "relay3PulseDurationMs": relay3PulseDurationMs,
       "relay4PulseDurationMs": relay4PulseDurationMs,
       "relay5PulseDurationMs": relay5PulseDurationMs,
       "relay6PulseDurationMs": relay6PulseDurationMs,
       "relay7PulseDurationMs": relay7PulseDurationMs,
       "relay8PulseDurationMs": relay8PulseDurationMs,
       "digitalInputDescription": digitalInputDescription,
       "configurationSaved": configurationSaved,
       "restartDevice": restartDevice,
       "tcw181bMIBConformance": tcw181bMIBConformance,
       "tcw181bMIBCompliances": tcw181bMIBCompliances,
       "tcw181bMIBCompliances1": tcw181bMIBCompliances1,
       "tcw181bMIBGroups": tcw181bMIBGroups,
       "tcw181bProductGroup": tcw181bProductGroup,
       "tcw181bSnmpSetupGroup": tcw181bSnmpSetupGroup,
       "tcw181bMonitorGroup": tcw181bMonitorGroup,
       "tcw181bNetworkGroup": tcw181bNetworkGroup,
       "tcw181bIOSetupGroup": tcw181bIOSetupGroup,
       "tcw181bTrapGroup": tcw181bTrapGroup,
       "snmpMIB": snmpMIB}
)
