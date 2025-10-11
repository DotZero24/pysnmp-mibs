# SNMP MIB module (ELECTROLINE-DHT-ENET-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/electroline/ELECTROLINE-DHT-ENET-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:06:49 2025
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

(dhtExtensionsMibObjects,) = mibBuilder.importSymbols(
    "ELECTROLINE-DHT-EXTENSIONS-MIB",
    "dhtExtensionsMibObjects")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

dhtEnetMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 12)
)
if mibBuilder.loadTexts:
    dhtEnetMib.setRevisions(
        ("2006-07-20 00:00",
         "2006-07-27 00:00",
         "2006-08-01 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class Rfactor(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 120),
        ValueRangeConstraint(127, 127),
    )



class ScaledMOSscore(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 50),
        ValueRangeConstraint(127, 127),
    )



class ScaledPercentage(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )



# MIB Managed Objects in the order of their OIDs

_DhtEnetMibObjects_ObjectIdentity = ObjectIdentity
dhtEnetMibObjects = _DhtEnetMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 12, 1)
)
_DhtEnetCapabilities_ObjectIdentity = ObjectIdentity
dhtEnetCapabilities = _DhtEnetCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 12, 1, 1)
)
_EnetSupport_Type = TruthValue
_EnetSupport_Object = MibScalar
enetSupport = _EnetSupport_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 12, 1, 1, 1),
    _EnetSupport_Type()
)
enetSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enetSupport.setStatus("current")
_EnetModuleVersion_Type = OctetString
_EnetModuleVersion_Object = MibScalar
enetModuleVersion = _EnetModuleVersion_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 12, 1, 1, 2),
    _EnetModuleVersion_Type()
)
enetModuleVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enetModuleVersion.setStatus("current")
_EnetMaxTestInstance_Type = Unsigned32
_EnetMaxTestInstance_Object = MibScalar
enetMaxTestInstance = _EnetMaxTestInstance_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 12, 1, 1, 3),
    _EnetMaxTestInstance_Type()
)
enetMaxTestInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enetMaxTestInstance.setStatus("current")
_EnetPerFeatureSupport_ObjectIdentity = ObjectIdentity
enetPerFeatureSupport = _EnetPerFeatureSupport_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 12, 1, 1, 11)
)


class _EnetConstellationDisplaySupport_Type(Integer32):
    """Custom type enetConstellationDisplaySupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 0),
          ("notLicensed", 1),
          ("active", 2))
    )


_EnetConstellationDisplaySupport_Type.__name__ = "Integer32"
_EnetConstellationDisplaySupport_Object = MibScalar
enetConstellationDisplaySupport = _EnetConstellationDisplaySupport_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 12, 1, 1, 11, 1),
    _EnetConstellationDisplaySupport_Type()
)
enetConstellationDisplaySupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enetConstellationDisplaySupport.setStatus("current")


class _EnetUDPTestSupport_Type(Integer32):
    """Custom type enetUDPTestSupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 0),
          ("notLicensed", 1),
          ("active", 2))
    )


_EnetUDPTestSupport_Type.__name__ = "Integer32"
_EnetUDPTestSupport_Object = MibScalar
enetUDPTestSupport = _EnetUDPTestSupport_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 12, 1, 1, 11, 2),
    _EnetUDPTestSupport_Type()
)
enetUDPTestSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enetUDPTestSupport.setStatus("current")


class _EnetVOIPTestSupport_Type(Integer32):
    """Custom type enetVOIPTestSupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 0),
          ("notLicensed", 1),
          ("active", 2))
    )


_EnetVOIPTestSupport_Type.__name__ = "Integer32"
_EnetVOIPTestSupport_Object = MibScalar
enetVOIPTestSupport = _EnetVOIPTestSupport_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 12, 1, 1, 11, 3),
    _EnetVOIPTestSupport_Type()
)
enetVOIPTestSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enetVOIPTestSupport.setStatus("current")


class _EnetSMRPTestSupport_Type(Integer32):
    """Custom type enetSMRPTestSupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 0),
          ("notLicensed", 1),
          ("active", 2))
    )


_EnetSMRPTestSupport_Type.__name__ = "Integer32"
_EnetSMRPTestSupport_Object = MibScalar
enetSMRPTestSupport = _EnetSMRPTestSupport_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 12, 1, 1, 11, 4),
    _EnetSMRPTestSupport_Type()
)
enetSMRPTestSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enetSMRPTestSupport.setStatus("current")
_DhtEnetGlobalControls_ObjectIdentity = ObjectIdentity
dhtEnetGlobalControls = _DhtEnetGlobalControls_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 12, 1, 2)
)
_EnetLicenseKey_Type = OctetString
_EnetLicenseKey_Object = MibScalar
enetLicenseKey = _EnetLicenseKey_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 12, 1, 2, 1),
    _EnetLicenseKey_Type()
)
enetLicenseKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enetLicenseKey.setStatus("current")


class _EnetPollingInterval_Type(Integer32):
    """Custom type enetPollingInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1000, 10000),
    )


_EnetPollingInterval_Type.__name__ = "Integer32"
_EnetPollingInterval_Object = MibScalar
enetPollingInterval = _EnetPollingInterval_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 12, 1, 2, 2),
    _EnetPollingInterval_Type()
)
enetPollingInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enetPollingInterval.setStatus("current")
_DhtEnetPacketTests_ObjectIdentity = ObjectIdentity
dhtEnetPacketTests = _DhtEnetPacketTests_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 12, 1, 3)
)
_DhtEnetPktTestControls_ObjectIdentity = ObjectIdentity
dhtEnetPktTestControls = _DhtEnetPktTestControls_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 12, 1, 3, 1)
)
_EnetTestControlTable_Object = MibTable
enetTestControlTable = _EnetTestControlTable_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 12, 1, 3, 1, 1)
)
if mibBuilder.loadTexts:
    enetTestControlTable.setStatus("current")
_EnetTestControlEntry_Object = MibTableRow
enetTestControlEntry = _EnetTestControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 12, 1, 3, 1, 1, 1)
)
enetTestControlEntry.setIndexNames(
    (0, "ELECTROLINE-DHT-ENET-MIB", "enetTestIndex"),
)
if mibBuilder.loadTexts:
    enetTestControlEntry.setStatus("current")
_EnetTestIndex_Type = Integer32
_EnetTestIndex_Object = MibTableColumn
enetTestIndex = _EnetTestIndex_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 12, 1, 3, 1, 1, 1, 1),
    _EnetTestIndex_Type()
)
enetTestIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    enetTestIndex.setStatus("current")
_EnetTestIdString_Type = OctetString
_EnetTestIdString_Object = MibTableColumn
enetTestIdString = _EnetTestIdString_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 12, 1, 3, 1, 1, 1, 2),
    _EnetTestIdString_Type()
)
enetTestIdString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enetTestIdString.setStatus("current")


class _EnetTestControl_Type(Integer32):
    """Custom type enetTestControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("stopTest", 1),
          ("setupTest", 2),
          ("startTest", 3))
    )


_EnetTestControl_Type.__name__ = "Integer32"
_EnetTestControl_Object = MibTableColumn
enetTestControl = _EnetTestControl_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 12, 1, 3, 1, 1, 1, 3),
    _EnetTestControl_Type()
)
enetTestControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enetTestControl.setStatus("current")
_EnetTestSenderIP_Type = IpAddress
_EnetTestSenderIP_Object = MibTableColumn
enetTestSenderIP = _EnetTestSenderIP_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 12, 1, 3, 1, 1, 1, 4),
    _EnetTestSenderIP_Type()
)
enetTestSenderIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enetTestSenderIP.setStatus("current")


class _EnetTestSenderUDPPort_Type(Gauge32):
    """Custom type enetTestSenderUDPPort based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_EnetTestSenderUDPPort_Type.__name__ = "Gauge32"
_EnetTestSenderUDPPort_Object = MibTableColumn
enetTestSenderUDPPort = _EnetTestSenderUDPPort_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 12, 1, 3, 1, 1, 1, 5),
    _EnetTestSenderUDPPort_Type()
)
enetTestSenderUDPPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enetTestSenderUDPPort.setStatus("current")
_EnetTestReceiverIP_Type = IpAddress
_EnetTestReceiverIP_Object = MibTableColumn
enetTestReceiverIP = _EnetTestReceiverIP_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 12, 1, 3, 1, 1, 1, 6),
    _EnetTestReceiverIP_Type()
)
enetTestReceiverIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enetTestReceiverIP.setStatus("current")


class _EnetTestReceiverUDPPort_Type(Gauge32):
    """Custom type enetTestReceiverUDPPort based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_EnetTestReceiverUDPPort_Type.__name__ = "Gauge32"
_EnetTestReceiverUDPPort_Object = MibTableColumn
enetTestReceiverUDPPort = _EnetTestReceiverUDPPort_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 12, 1, 3, 1, 1, 1, 7),
    _EnetTestReceiverUDPPort_Type()
)
enetTestReceiverUDPPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enetTestReceiverUDPPort.setStatus("current")


class _EnetTestType_Type(Integer32):
    """Custom type enetTestType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("voip", 1),
          ("packetLoss", 2))
    )


_EnetTestType_Type.__name__ = "Integer32"
_EnetTestType_Object = MibTableColumn
enetTestType = _EnetTestType_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 12, 1, 3, 1, 1, 1, 8),
    _EnetTestType_Type()
)
enetTestType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enetTestType.setStatus("current")


class _EnetTestPacketSize_Type(Integer32):
    """Custom type enetTestPacketSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(64, 1514),
    )


_EnetTestPacketSize_Type.__name__ = "Integer32"
_EnetTestPacketSize_Object = MibTableColumn
enetTestPacketSize = _EnetTestPacketSize_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 12, 1, 3, 1, 1, 1, 9),
    _EnetTestPacketSize_Type()
)
enetTestPacketSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enetTestPacketSize.setStatus("current")


class _EnetTestPacketInterval_Type(Integer32):
    """Custom type enetTestPacketInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 10),
        ValueRangeConstraint(20, 20),
        ValueRangeConstraint(30, 30),
    )


_EnetTestPacketInterval_Type.__name__ = "Integer32"
_EnetTestPacketInterval_Object = MibTableColumn
enetTestPacketInterval = _EnetTestPacketInterval_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 12, 1, 3, 1, 1, 1, 10),
    _EnetTestPacketInterval_Type()
)
enetTestPacketInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enetTestPacketInterval.setStatus("current")


class _EnetTestPacketRate_Type(Integer32):
    """Custom type enetTestPacketRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255000),
    )


_EnetTestPacketRate_Type.__name__ = "Integer32"
_EnetTestPacketRate_Object = MibTableColumn
enetTestPacketRate = _EnetTestPacketRate_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 12, 1, 3, 1, 1, 1, 11),
    _EnetTestPacketRate_Type()
)
enetTestPacketRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enetTestPacketRate.setStatus("current")


class _EnetTestNumOfPackets_Type(Unsigned32):
    """Custom type enetTestNumOfPackets based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_EnetTestNumOfPackets_Type.__name__ = "Unsigned32"
_EnetTestNumOfPackets_Object = MibTableColumn
enetTestNumOfPackets = _EnetTestNumOfPackets_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 12, 1, 3, 1, 1, 1, 12),
    _EnetTestNumOfPackets_Type()
)
enetTestNumOfPackets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enetTestNumOfPackets.setStatus("current")


class _EnetTestJitterBufferSize_Type(Integer32):
    """Custom type enetTestJitterBufferSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200),
    )


_EnetTestJitterBufferSize_Type.__name__ = "Integer32"
_EnetTestJitterBufferSize_Object = MibTableColumn
enetTestJitterBufferSize = _EnetTestJitterBufferSize_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 12, 1, 3, 1, 1, 1, 13),
    _EnetTestJitterBufferSize_Type()
)
enetTestJitterBufferSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enetTestJitterBufferSize.setStatus("current")


class _EnetTestQosControl_Type(Integer32):
    """Custom type enetTestQosControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("preestablished", 2),
          ("dsa", 3))
    )


_EnetTestQosControl_Type.__name__ = "Integer32"
_EnetTestQosControl_Object = MibTableColumn
enetTestQosControl = _EnetTestQosControl_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 12, 1, 3, 1, 1, 1, 14),
    _EnetTestQosControl_Type()
)
enetTestQosControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enetTestQosControl.setStatus("current")


class _EnetTestCodecType_Type(Integer32):
    """Custom type enetTestCodecType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("na", 0),
          ("g711", 1))
    )


_EnetTestCodecType_Type.__name__ = "Integer32"
_EnetTestCodecType_Object = MibTableColumn
enetTestCodecType = _EnetTestCodecType_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 12, 1, 3, 1, 1, 1, 15),
    _EnetTestCodecType_Type()
)
enetTestCodecType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enetTestCodecType.setStatus("current")


class _EnetTestTosByte_Type(Integer32):
    """Custom type enetTestTosByte based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_EnetTestTosByte_Type.__name__ = "Integer32"
_EnetTestTosByte_Object = MibTableColumn
enetTestTosByte = _EnetTestTosByte_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 12, 1, 3, 1, 1, 1, 16),
    _EnetTestTosByte_Type()
)
enetTestTosByte.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enetTestTosByte.setStatus("current")


class _EnetTestRoundTripTimeEstimate_Type(Integer32):
    """Custom type enetTestRoundTripTimeEstimate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60000),
    )


_EnetTestRoundTripTimeEstimate_Type.__name__ = "Integer32"
_EnetTestRoundTripTimeEstimate_Object = MibTableColumn
enetTestRoundTripTimeEstimate = _EnetTestRoundTripTimeEstimate_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 12, 1, 3, 1, 1, 1, 17),
    _EnetTestRoundTripTimeEstimate_Type()
)
enetTestRoundTripTimeEstimate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enetTestRoundTripTimeEstimate.setStatus("current")


class _EnetTestStatus_Type(Integer32):
    """Custom type enetTestStatus based on Integer32"""
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
        *(("na", 0),
          ("running", 1),
          ("completed", 2),
          ("ressourceUnavailable", 3),
          ("invalidParameter", 4),
          ("ready", 5))
    )


_EnetTestStatus_Type.__name__ = "Integer32"
_EnetTestStatus_Object = MibTableColumn
enetTestStatus = _EnetTestStatus_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 12, 1, 3, 1, 1, 1, 18),
    _EnetTestStatus_Type()
)
enetTestStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enetTestStatus.setStatus("current")


class _EnetTestStatusString_Type(OctetString):
    """Custom type enetTestStatusString based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_EnetTestStatusString_Type.__name__ = "OctetString"
_EnetTestStatusString_Object = MibTableColumn
enetTestStatusString = _EnetTestStatusString_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 12, 1, 3, 1, 1, 1, 19),
    _EnetTestStatusString_Type()
)
enetTestStatusString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enetTestStatusString.setStatus("current")
_DhtEnetPktTestResults_ObjectIdentity = ObjectIdentity
dhtEnetPktTestResults = _DhtEnetPktTestResults_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 12, 1, 3, 3)
)
_EnetCurrentResultsTable_Object = MibTable
enetCurrentResultsTable = _EnetCurrentResultsTable_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 12, 1, 3, 3, 1)
)
if mibBuilder.loadTexts:
    enetCurrentResultsTable.setStatus("current")
_EnetCurrentResultsEntry_Object = MibTableRow
enetCurrentResultsEntry = _EnetCurrentResultsEntry_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 12, 1, 3, 3, 1, 1)
)
enetCurrentResultsEntry.setIndexNames(
    (0, "ELECTROLINE-DHT-ENET-MIB", "enetResultsIndex"),
)
if mibBuilder.loadTexts:
    enetCurrentResultsEntry.setStatus("current")


class _EnetResultsIndex_Type(Unsigned32):
    """Custom type enetResultsIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_EnetResultsIndex_Type.__name__ = "Unsigned32"
_EnetResultsIndex_Object = MibTableColumn
enetResultsIndex = _EnetResultsIndex_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 12, 1, 3, 3, 1, 1, 1),
    _EnetResultsIndex_Type()
)
enetResultsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    enetResultsIndex.setStatus("current")
_EnetResultsIdString_Type = OctetString
_EnetResultsIdString_Object = MibTableColumn
enetResultsIdString = _EnetResultsIdString_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 12, 1, 3, 3, 1, 1, 2),
    _EnetResultsIdString_Type()
)
enetResultsIdString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enetResultsIdString.setStatus("current")


class _EnetResultsStatus_Type(Integer32):
    """Custom type enetResultsStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inconsistent", 0),
          ("partial", 1),
          ("complete", 2))
    )


_EnetResultsStatus_Type.__name__ = "Integer32"
_EnetResultsStatus_Object = MibTableColumn
enetResultsStatus = _EnetResultsStatus_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 12, 1, 3, 3, 1, 1, 3),
    _EnetResultsStatus_Type()
)
enetResultsStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enetResultsStatus.setStatus("current")
_EnetResultsDuration_Type = Unsigned32
_EnetResultsDuration_Object = MibTableColumn
enetResultsDuration = _EnetResultsDuration_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 12, 1, 3, 3, 1, 1, 4),
    _EnetResultsDuration_Type()
)
enetResultsDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enetResultsDuration.setStatus("current")
_EnetResultsStartTime_Type = DateAndTime
_EnetResultsStartTime_Object = MibTableColumn
enetResultsStartTime = _EnetResultsStartTime_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 12, 1, 3, 3, 1, 1, 5),
    _EnetResultsStartTime_Type()
)
enetResultsStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enetResultsStartTime.setStatus("current")
_EnetResultsStopTime_Type = DateAndTime
_EnetResultsStopTime_Object = MibTableColumn
enetResultsStopTime = _EnetResultsStopTime_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 12, 1, 3, 3, 1, 1, 6),
    _EnetResultsStopTime_Type()
)
enetResultsStopTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enetResultsStopTime.setStatus("current")
_EnetResultsProcessedPacketCount_Type = Gauge32
_EnetResultsProcessedPacketCount_Object = MibTableColumn
enetResultsProcessedPacketCount = _EnetResultsProcessedPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 12, 1, 3, 3, 1, 1, 7),
    _EnetResultsProcessedPacketCount_Type()
)
enetResultsProcessedPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enetResultsProcessedPacketCount.setStatus("current")
_EnetResultsLossPacketCount_Type = Gauge32
_EnetResultsLossPacketCount_Object = MibTableColumn
enetResultsLossPacketCount = _EnetResultsLossPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 12, 1, 3, 3, 1, 1, 8),
    _EnetResultsLossPacketCount_Type()
)
enetResultsLossPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enetResultsLossPacketCount.setStatus("current")
_EnetResultsDiscardedPacketCount_Type = Gauge32
_EnetResultsDiscardedPacketCount_Object = MibTableColumn
enetResultsDiscardedPacketCount = _EnetResultsDiscardedPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 12, 1, 3, 3, 1, 1, 9),
    _EnetResultsDiscardedPacketCount_Type()
)
enetResultsDiscardedPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enetResultsDiscardedPacketCount.setStatus("current")
_EnetResultsPacketLossRate_Type = ScaledPercentage
_EnetResultsPacketLossRate_Object = MibTableColumn
enetResultsPacketLossRate = _EnetResultsPacketLossRate_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 12, 1, 3, 3, 1, 1, 10),
    _EnetResultsPacketLossRate_Type()
)
enetResultsPacketLossRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enetResultsPacketLossRate.setStatus("current")
_EnetResultsPacketDiscardRate_Type = ScaledPercentage
_EnetResultsPacketDiscardRate_Object = MibTableColumn
enetResultsPacketDiscardRate = _EnetResultsPacketDiscardRate_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 12, 1, 3, 3, 1, 1, 11),
    _EnetResultsPacketDiscardRate_Type()
)
enetResultsPacketDiscardRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enetResultsPacketDiscardRate.setStatus("current")
_EnetResultsMinInstantJitter_Type = Gauge32
_EnetResultsMinInstantJitter_Object = MibTableColumn
enetResultsMinInstantJitter = _EnetResultsMinInstantJitter_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 12, 1, 3, 3, 1, 1, 12),
    _EnetResultsMinInstantJitter_Type()
)
enetResultsMinInstantJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enetResultsMinInstantJitter.setStatus("current")
_EnetResultsMaxInstantJitter_Type = Gauge32
_EnetResultsMaxInstantJitter_Object = MibTableColumn
enetResultsMaxInstantJitter = _EnetResultsMaxInstantJitter_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 12, 1, 3, 3, 1, 1, 13),
    _EnetResultsMaxInstantJitter_Type()
)
enetResultsMaxInstantJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enetResultsMaxInstantJitter.setStatus("current")
_EnetResultsAvgInstantJitter_Type = Gauge32
_EnetResultsAvgInstantJitter_Object = MibTableColumn
enetResultsAvgInstantJitter = _EnetResultsAvgInstantJitter_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 12, 1, 3, 3, 1, 1, 14),
    _EnetResultsAvgInstantJitter_Type()
)
enetResultsAvgInstantJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enetResultsAvgInstantJitter.setStatus("current")
_EnetResultsMinRfcJitterLevel_Type = Gauge32
_EnetResultsMinRfcJitterLevel_Object = MibTableColumn
enetResultsMinRfcJitterLevel = _EnetResultsMinRfcJitterLevel_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 12, 1, 3, 3, 1, 1, 15),
    _EnetResultsMinRfcJitterLevel_Type()
)
enetResultsMinRfcJitterLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enetResultsMinRfcJitterLevel.setStatus("current")
_EnetResultsMaxRfcJitterLevel_Type = Gauge32
_EnetResultsMaxRfcJitterLevel_Object = MibTableColumn
enetResultsMaxRfcJitterLevel = _EnetResultsMaxRfcJitterLevel_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 12, 1, 3, 3, 1, 1, 16),
    _EnetResultsMaxRfcJitterLevel_Type()
)
enetResultsMaxRfcJitterLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enetResultsMaxRfcJitterLevel.setStatus("current")
_EnetResultsAvgRfcJitterLevel_Type = Gauge32
_EnetResultsAvgRfcJitterLevel_Object = MibTableColumn
enetResultsAvgRfcJitterLevel = _EnetResultsAvgRfcJitterLevel_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 12, 1, 3, 3, 1, 1, 17),
    _EnetResultsAvgRfcJitterLevel_Type()
)
enetResultsAvgRfcJitterLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enetResultsAvgRfcJitterLevel.setStatus("current")
_EnetResultsRCQ_Type = Rfactor
_EnetResultsRCQ_Object = MibTableColumn
enetResultsRCQ = _EnetResultsRCQ_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 12, 1, 3, 3, 1, 1, 18),
    _EnetResultsRCQ_Type()
)
enetResultsRCQ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enetResultsRCQ.setStatus("current")
_EnetResultsRLQ_Type = Rfactor
_EnetResultsRLQ_Object = MibTableColumn
enetResultsRLQ = _EnetResultsRLQ_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 12, 1, 3, 3, 1, 1, 19),
    _EnetResultsRLQ_Type()
)
enetResultsRLQ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enetResultsRLQ.setStatus("current")
_EnetResultsMOSCQ_Type = ScaledMOSscore
_EnetResultsMOSCQ_Object = MibTableColumn
enetResultsMOSCQ = _EnetResultsMOSCQ_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 12, 1, 3, 3, 1, 1, 20),
    _EnetResultsMOSCQ_Type()
)
enetResultsMOSCQ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enetResultsMOSCQ.setStatus("current")
_EnetResultsMOSLQ_Type = ScaledMOSscore
_EnetResultsMOSLQ_Object = MibTableColumn
enetResultsMOSLQ = _EnetResultsMOSLQ_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 12, 1, 3, 3, 1, 1, 21),
    _EnetResultsMOSLQ_Type()
)
enetResultsMOSLQ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enetResultsMOSLQ.setStatus("current")
_DhtEnetDOCSISMonitoring_ObjectIdentity = ObjectIdentity
dhtEnetDOCSISMonitoring = _DhtEnetDOCSISMonitoring_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 12, 1, 4)
)


class _EnetDocsisMonResetCounters_Type(Integer32):
    """Custom type enetDocsisMonResetCounters based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset", 1)
    )


_EnetDocsisMonResetCounters_Type.__name__ = "Integer32"
_EnetDocsisMonResetCounters_Object = MibScalar
enetDocsisMonResetCounters = _EnetDocsisMonResetCounters_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 12, 1, 4, 1),
    _EnetDocsisMonResetCounters_Type()
)
enetDocsisMonResetCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enetDocsisMonResetCounters.setStatus("current")
_EnetDocsisMonPreFECErrorRate_Type = OctetString
_EnetDocsisMonPreFECErrorRate_Object = MibScalar
enetDocsisMonPreFECErrorRate = _EnetDocsisMonPreFECErrorRate_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 12, 1, 4, 2),
    _EnetDocsisMonPreFECErrorRate_Type()
)
enetDocsisMonPreFECErrorRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enetDocsisMonPreFECErrorRate.setStatus("current")
_EnetDocsisMonPostFECErrorRate_Type = OctetString
_EnetDocsisMonPostFECErrorRate_Object = MibScalar
enetDocsisMonPostFECErrorRate = _EnetDocsisMonPostFECErrorRate_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 12, 1, 4, 3),
    _EnetDocsisMonPostFECErrorRate_Type()
)
enetDocsisMonPostFECErrorRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enetDocsisMonPostFECErrorRate.setStatus("current")
_EnetDocsisMonErroredSeconds_Type = Gauge32
_EnetDocsisMonErroredSeconds_Object = MibScalar
enetDocsisMonErroredSeconds = _EnetDocsisMonErroredSeconds_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 12, 1, 4, 4),
    _EnetDocsisMonErroredSeconds_Type()
)
enetDocsisMonErroredSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enetDocsisMonErroredSeconds.setStatus("current")
_EnetDocsisMonSeverelyErroredSeconds_Type = Gauge32
_EnetDocsisMonSeverelyErroredSeconds_Object = MibScalar
enetDocsisMonSeverelyErroredSeconds = _EnetDocsisMonSeverelyErroredSeconds_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 12, 1, 4, 5),
    _EnetDocsisMonSeverelyErroredSeconds_Type()
)
enetDocsisMonSeverelyErroredSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enetDocsisMonSeverelyErroredSeconds.setStatus("current")
_EnetDocsisMonTimeElapsed_Type = Gauge32
_EnetDocsisMonTimeElapsed_Object = MibScalar
enetDocsisMonTimeElapsed = _EnetDocsisMonTimeElapsed_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 5, 1, 12, 1, 4, 6),
    _EnetDocsisMonTimeElapsed_Type()
)
enetDocsisMonTimeElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enetDocsisMonTimeElapsed.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ELECTROLINE-DHT-ENET-MIB",
    **{"Rfactor": Rfactor,
       "ScaledMOSscore": ScaledMOSscore,
       "ScaledPercentage": ScaledPercentage,
       "dhtEnetMib": dhtEnetMib,
       "dhtEnetMibObjects": dhtEnetMibObjects,
       "dhtEnetCapabilities": dhtEnetCapabilities,
       "enetSupport": enetSupport,
       "enetModuleVersion": enetModuleVersion,
       "enetMaxTestInstance": enetMaxTestInstance,
       "enetPerFeatureSupport": enetPerFeatureSupport,
       "enetConstellationDisplaySupport": enetConstellationDisplaySupport,
       "enetUDPTestSupport": enetUDPTestSupport,
       "enetVOIPTestSupport": enetVOIPTestSupport,
       "enetSMRPTestSupport": enetSMRPTestSupport,
       "dhtEnetGlobalControls": dhtEnetGlobalControls,
       "enetLicenseKey": enetLicenseKey,
       "enetPollingInterval": enetPollingInterval,
       "dhtEnetPacketTests": dhtEnetPacketTests,
       "dhtEnetPktTestControls": dhtEnetPktTestControls,
       "enetTestControlTable": enetTestControlTable,
       "enetTestControlEntry": enetTestControlEntry,
       "enetTestIndex": enetTestIndex,
       "enetTestIdString": enetTestIdString,
       "enetTestControl": enetTestControl,
       "enetTestSenderIP": enetTestSenderIP,
       "enetTestSenderUDPPort": enetTestSenderUDPPort,
       "enetTestReceiverIP": enetTestReceiverIP,
       "enetTestReceiverUDPPort": enetTestReceiverUDPPort,
       "enetTestType": enetTestType,
       "enetTestPacketSize": enetTestPacketSize,
       "enetTestPacketInterval": enetTestPacketInterval,
       "enetTestPacketRate": enetTestPacketRate,
       "enetTestNumOfPackets": enetTestNumOfPackets,
       "enetTestJitterBufferSize": enetTestJitterBufferSize,
       "enetTestQosControl": enetTestQosControl,
       "enetTestCodecType": enetTestCodecType,
       "enetTestTosByte": enetTestTosByte,
       "enetTestRoundTripTimeEstimate": enetTestRoundTripTimeEstimate,
       "enetTestStatus": enetTestStatus,
       "enetTestStatusString": enetTestStatusString,
       "dhtEnetPktTestResults": dhtEnetPktTestResults,
       "enetCurrentResultsTable": enetCurrentResultsTable,
       "enetCurrentResultsEntry": enetCurrentResultsEntry,
       "enetResultsIndex": enetResultsIndex,
       "enetResultsIdString": enetResultsIdString,
       "enetResultsStatus": enetResultsStatus,
       "enetResultsDuration": enetResultsDuration,
       "enetResultsStartTime": enetResultsStartTime,
       "enetResultsStopTime": enetResultsStopTime,
       "enetResultsProcessedPacketCount": enetResultsProcessedPacketCount,
       "enetResultsLossPacketCount": enetResultsLossPacketCount,
       "enetResultsDiscardedPacketCount": enetResultsDiscardedPacketCount,
       "enetResultsPacketLossRate": enetResultsPacketLossRate,
       "enetResultsPacketDiscardRate": enetResultsPacketDiscardRate,
       "enetResultsMinInstantJitter": enetResultsMinInstantJitter,
       "enetResultsMaxInstantJitter": enetResultsMaxInstantJitter,
       "enetResultsAvgInstantJitter": enetResultsAvgInstantJitter,
       "enetResultsMinRfcJitterLevel": enetResultsMinRfcJitterLevel,
       "enetResultsMaxRfcJitterLevel": enetResultsMaxRfcJitterLevel,
       "enetResultsAvgRfcJitterLevel": enetResultsAvgRfcJitterLevel,
       "enetResultsRCQ": enetResultsRCQ,
       "enetResultsRLQ": enetResultsRLQ,
       "enetResultsMOSCQ": enetResultsMOSCQ,
       "enetResultsMOSLQ": enetResultsMOSLQ,
       "dhtEnetDOCSISMonitoring": dhtEnetDOCSISMonitoring,
       "enetDocsisMonResetCounters": enetDocsisMonResetCounters,
       "enetDocsisMonPreFECErrorRate": enetDocsisMonPreFECErrorRate,
       "enetDocsisMonPostFECErrorRate": enetDocsisMonPostFECErrorRate,
       "enetDocsisMonErroredSeconds": enetDocsisMonErroredSeconds,
       "enetDocsisMonSeverelyErroredSeconds": enetDocsisMonSeverelyErroredSeconds,
       "enetDocsisMonTimeElapsed": enetDocsisMonTimeElapsed}
)
