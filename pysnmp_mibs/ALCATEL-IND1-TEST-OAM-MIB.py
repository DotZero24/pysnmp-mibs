# SNMP MIB module (ALCATEL-IND1-TEST-OAM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/alcatel/ALCATEL-IND1-TEST-OAM-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:08:17 2025
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

(softentIND1TestOam,) = mibBuilder.importSymbols(
    "ALCATEL-IND1-BASE",
    "softentIND1TestOam")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(VlanId,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "VlanId")

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
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

alcatelIND1TestOamMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 65, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1TestOamMIB.setRevisions(
        ("2010-03-25 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AlaTestOamNotifications_ObjectIdentity = ObjectIdentity
alaTestOamNotifications = _AlaTestOamNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 65, 1, 0)
)
_AlaTestOamMIBObjects_ObjectIdentity = ObjectIdentity
alaTestOamMIBObjects = _AlaTestOamMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 65, 1, 1)
)
_AlaTestOamClearStats_ObjectIdentity = ObjectIdentity
alaTestOamClearStats = _AlaTestOamClearStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 65, 1, 1, 1)
)


class _AlaTestOamGlobalClearStats_Type(Integer32):
    """Custom type alaTestOamGlobalClearStats based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("default", 1),
          ("reset", 2))
    )


_AlaTestOamGlobalClearStats_Type.__name__ = "Integer32"
_AlaTestOamGlobalClearStats_Object = MibScalar
alaTestOamGlobalClearStats = _AlaTestOamGlobalClearStats_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 65, 1, 1, 1, 1),
    _AlaTestOamGlobalClearStats_Type()
)
alaTestOamGlobalClearStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaTestOamGlobalClearStats.setStatus("current")
_AlaTestOamStatus_ObjectIdentity = ObjectIdentity
alaTestOamStatus = _AlaTestOamStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 65, 1, 1, 2)
)
_AlaTestOamConfig_ObjectIdentity = ObjectIdentity
alaTestOamConfig = _AlaTestOamConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 65, 1, 1, 3)
)
_AlaTestOamConfigTable_Object = MibTable
alaTestOamConfigTable = _AlaTestOamConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 65, 1, 1, 3, 1)
)
if mibBuilder.loadTexts:
    alaTestOamConfigTable.setStatus("current")
_AlaTestOamConfigEntry_Object = MibTableRow
alaTestOamConfigEntry = _AlaTestOamConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 65, 1, 1, 3, 1, 1)
)
alaTestOamConfigEntry.setIndexNames(
    (0, "ALCATEL-IND1-TEST-OAM-MIB", "alaTestOamConfigTestId"),
)
if mibBuilder.loadTexts:
    alaTestOamConfigEntry.setStatus("current")


class _AlaTestOamConfigTestId_Type(SnmpAdminString):
    """Custom type alaTestOamConfigTestId based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AlaTestOamConfigTestId_Type.__name__ = "SnmpAdminString"
_AlaTestOamConfigTestId_Object = MibTableColumn
alaTestOamConfigTestId = _AlaTestOamConfigTestId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 65, 1, 1, 3, 1, 1, 1),
    _AlaTestOamConfigTestId_Type()
)
alaTestOamConfigTestId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alaTestOamConfigTestId.setStatus("current")


class _AlaTestOamConfigSourceEndpoint_Type(SnmpAdminString):
    """Custom type alaTestOamConfigSourceEndpoint based on SnmpAdminString"""
    defaultValue = OctetString("DEFAULT")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AlaTestOamConfigSourceEndpoint_Type.__name__ = "SnmpAdminString"
_AlaTestOamConfigSourceEndpoint_Object = MibTableColumn
alaTestOamConfigSourceEndpoint = _AlaTestOamConfigSourceEndpoint_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 65, 1, 1, 3, 1, 1, 2),
    _AlaTestOamConfigSourceEndpoint_Type()
)
alaTestOamConfigSourceEndpoint.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaTestOamConfigSourceEndpoint.setStatus("current")


class _AlaTestOamConfigDestinationEndpoint_Type(SnmpAdminString):
    """Custom type alaTestOamConfigDestinationEndpoint based on SnmpAdminString"""
    defaultValue = OctetString("DEFAULT")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AlaTestOamConfigDestinationEndpoint_Type.__name__ = "SnmpAdminString"
_AlaTestOamConfigDestinationEndpoint_Object = MibTableColumn
alaTestOamConfigDestinationEndpoint = _AlaTestOamConfigDestinationEndpoint_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 65, 1, 1, 3, 1, 1, 3),
    _AlaTestOamConfigDestinationEndpoint_Type()
)
alaTestOamConfigDestinationEndpoint.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaTestOamConfigDestinationEndpoint.setStatus("current")


class _AlaTestOamConfigTestDescription_Type(SnmpAdminString):
    """Custom type alaTestOamConfigTestDescription based on SnmpAdminString"""
    defaultValue = OctetString("DEFAULT")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AlaTestOamConfigTestDescription_Type.__name__ = "SnmpAdminString"
_AlaTestOamConfigTestDescription_Object = MibTableColumn
alaTestOamConfigTestDescription = _AlaTestOamConfigTestDescription_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 65, 1, 1, 3, 1, 1, 4),
    _AlaTestOamConfigTestDescription_Type()
)
alaTestOamConfigTestDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaTestOamConfigTestDescription.setStatus("current")


class _AlaTestOamConfigGeneratorTestMode_Type(Integer32):
    """Custom type alaTestOamConfigGeneratorTestMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("ingressUniOutOfService", 1)
    )


_AlaTestOamConfigGeneratorTestMode_Type.__name__ = "Integer32"
_AlaTestOamConfigGeneratorTestMode_Object = MibTableColumn
alaTestOamConfigGeneratorTestMode = _AlaTestOamConfigGeneratorTestMode_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 65, 1, 1, 3, 1, 1, 5),
    _AlaTestOamConfigGeneratorTestMode_Type()
)
alaTestOamConfigGeneratorTestMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaTestOamConfigGeneratorTestMode.setStatus("current")


class _AlaTestOamConfigAnalyzerTestMode_Type(Integer32):
    """Custom type alaTestOamConfigAnalyzerTestMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("ingressNni", 1)
    )


_AlaTestOamConfigAnalyzerTestMode_Type.__name__ = "Integer32"
_AlaTestOamConfigAnalyzerTestMode_Object = MibTableColumn
alaTestOamConfigAnalyzerTestMode = _AlaTestOamConfigAnalyzerTestMode_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 65, 1, 1, 3, 1, 1, 6),
    _AlaTestOamConfigAnalyzerTestMode_Type()
)
alaTestOamConfigAnalyzerTestMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaTestOamConfigAnalyzerTestMode.setStatus("current")


class _AlaTestOamConfigLoopbackTestMode_Type(Integer32):
    """Custom type alaTestOamConfigLoopbackTestMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("egressUni", 1)
    )


_AlaTestOamConfigLoopbackTestMode_Type.__name__ = "Integer32"
_AlaTestOamConfigLoopbackTestMode_Object = MibTableColumn
alaTestOamConfigLoopbackTestMode = _AlaTestOamConfigLoopbackTestMode_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 65, 1, 1, 3, 1, 1, 7),
    _AlaTestOamConfigLoopbackTestMode_Type()
)
alaTestOamConfigLoopbackTestMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaTestOamConfigLoopbackTestMode.setStatus("current")


class _AlaTestOamConfigDirection_Type(Integer32):
    """Custom type alaTestOamConfigDirection based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("uniDirectional", 1),
          ("biDirectional", 2))
    )


_AlaTestOamConfigDirection_Type.__name__ = "Integer32"
_AlaTestOamConfigDirection_Object = MibTableColumn
alaTestOamConfigDirection = _AlaTestOamConfigDirection_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 65, 1, 1, 3, 1, 1, 8),
    _AlaTestOamConfigDirection_Type()
)
alaTestOamConfigDirection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaTestOamConfigDirection.setStatus("current")
_AlaTestOamConfigFrameSrcMacAddress_Type = MacAddress
_AlaTestOamConfigFrameSrcMacAddress_Object = MibTableColumn
alaTestOamConfigFrameSrcMacAddress = _AlaTestOamConfigFrameSrcMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 65, 1, 1, 3, 1, 1, 9),
    _AlaTestOamConfigFrameSrcMacAddress_Type()
)
alaTestOamConfigFrameSrcMacAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaTestOamConfigFrameSrcMacAddress.setStatus("current")
_AlaTestOamConfigFrameDstMacAddress_Type = MacAddress
_AlaTestOamConfigFrameDstMacAddress_Object = MibTableColumn
alaTestOamConfigFrameDstMacAddress = _AlaTestOamConfigFrameDstMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 65, 1, 1, 3, 1, 1, 10),
    _AlaTestOamConfigFrameDstMacAddress_Type()
)
alaTestOamConfigFrameDstMacAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaTestOamConfigFrameDstMacAddress.setStatus("current")


class _AlaTestOamConfigDuration_Type(Integer32):
    """Custom type alaTestOamConfigDuration based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 3600),
    )


_AlaTestOamConfigDuration_Type.__name__ = "Integer32"
_AlaTestOamConfigDuration_Object = MibTableColumn
alaTestOamConfigDuration = _AlaTestOamConfigDuration_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 65, 1, 1, 3, 1, 1, 11),
    _AlaTestOamConfigDuration_Type()
)
alaTestOamConfigDuration.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaTestOamConfigDuration.setStatus("current")
if mibBuilder.loadTexts:
    alaTestOamConfigDuration.setUnits("seconds")
_AlaTestOamConfigVlan_Type = VlanId
_AlaTestOamConfigVlan_Object = MibTableColumn
alaTestOamConfigVlan = _AlaTestOamConfigVlan_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 65, 1, 1, 3, 1, 1, 12),
    _AlaTestOamConfigVlan_Type()
)
alaTestOamConfigVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaTestOamConfigVlan.setStatus("current")


class _AlaTestOamConfigRole_Type(Integer32):
    """Custom type alaTestOamConfigRole based on Integer32"""
    defaultValue = 0

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
        *(("none", 0),
          ("generator", 1),
          ("analyzer", 2),
          ("loopback", 3))
    )


_AlaTestOamConfigRole_Type.__name__ = "Integer32"
_AlaTestOamConfigRole_Object = MibTableColumn
alaTestOamConfigRole = _AlaTestOamConfigRole_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 65, 1, 1, 3, 1, 1, 13),
    _AlaTestOamConfigRole_Type()
)
alaTestOamConfigRole.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaTestOamConfigRole.setStatus("current")
_AlaTestOamConfigPort_Type = InterfaceIndex
_AlaTestOamConfigPort_Object = MibTableColumn
alaTestOamConfigPort = _AlaTestOamConfigPort_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 65, 1, 1, 3, 1, 1, 14),
    _AlaTestOamConfigPort_Type()
)
alaTestOamConfigPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaTestOamConfigPort.setStatus("current")


class _AlaTestOamConfigSourceLearningStatus_Type(Integer32):
    """Custom type alaTestOamConfigSourceLearningStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_AlaTestOamConfigSourceLearningStatus_Type.__name__ = "Integer32"
_AlaTestOamConfigSourceLearningStatus_Object = MibTableColumn
alaTestOamConfigSourceLearningStatus = _AlaTestOamConfigSourceLearningStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 65, 1, 1, 3, 1, 1, 15),
    _AlaTestOamConfigSourceLearningStatus_Type()
)
alaTestOamConfigSourceLearningStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaTestOamConfigSourceLearningStatus.setStatus("current")


class _AlaTestOamConfigGeneratorMode_Type(Integer32):
    """Custom type alaTestOamConfigGeneratorMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("stream", 1)
    )


_AlaTestOamConfigGeneratorMode_Type.__name__ = "Integer32"
_AlaTestOamConfigGeneratorMode_Object = MibTableColumn
alaTestOamConfigGeneratorMode = _AlaTestOamConfigGeneratorMode_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 65, 1, 1, 3, 1, 1, 16),
    _AlaTestOamConfigGeneratorMode_Type()
)
alaTestOamConfigGeneratorMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaTestOamConfigGeneratorMode.setStatus("current")


class _AlaTestOamConfigGeneratorBandwidth_Type(Integer32):
    """Custom type alaTestOamConfigGeneratorBandwidth based on Integer32"""
    defaultValue = 8

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(8, 1000000),
    )


_AlaTestOamConfigGeneratorBandwidth_Type.__name__ = "Integer32"
_AlaTestOamConfigGeneratorBandwidth_Object = MibTableColumn
alaTestOamConfigGeneratorBandwidth = _AlaTestOamConfigGeneratorBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 65, 1, 1, 3, 1, 1, 17),
    _AlaTestOamConfigGeneratorBandwidth_Type()
)
alaTestOamConfigGeneratorBandwidth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaTestOamConfigGeneratorBandwidth.setStatus("current")


class _AlaTestOamConfigGeneratorPacketSize_Type(Integer32):
    """Custom type alaTestOamConfigGeneratorPacketSize based on Integer32"""
    defaultValue = 64

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(64, 9212),
    )


_AlaTestOamConfigGeneratorPacketSize_Type.__name__ = "Integer32"
_AlaTestOamConfigGeneratorPacketSize_Object = MibTableColumn
alaTestOamConfigGeneratorPacketSize = _AlaTestOamConfigGeneratorPacketSize_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 65, 1, 1, 3, 1, 1, 18),
    _AlaTestOamConfigGeneratorPacketSize_Type()
)
alaTestOamConfigGeneratorPacketSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaTestOamConfigGeneratorPacketSize.setStatus("current")


class _AlaTestOamConfigTestIdState_Type(Integer32):
    """Custom type alaTestOamConfigTestIdState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("start", 1),
          ("stop", 2))
    )


_AlaTestOamConfigTestIdState_Type.__name__ = "Integer32"
_AlaTestOamConfigTestIdState_Object = MibTableColumn
alaTestOamConfigTestIdState = _AlaTestOamConfigTestIdState_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 65, 1, 1, 3, 1, 1, 19),
    _AlaTestOamConfigTestIdState_Type()
)
alaTestOamConfigTestIdState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaTestOamConfigTestIdState.setStatus("current")


class _AlaTestOamConfigTestIdStatus_Type(Integer32):
    """Custom type alaTestOamConfigTestIdStatus based on Integer32"""
    defaultValue = 1

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
        *(("notstarted", 1),
          ("running", 2),
          ("stopped", 3),
          ("ended", 4))
    )


_AlaTestOamConfigTestIdStatus_Type.__name__ = "Integer32"
_AlaTestOamConfigTestIdStatus_Object = MibTableColumn
alaTestOamConfigTestIdStatus = _AlaTestOamConfigTestIdStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 65, 1, 1, 3, 1, 1, 20),
    _AlaTestOamConfigTestIdStatus_Type()
)
alaTestOamConfigTestIdStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaTestOamConfigTestIdStatus.setStatus("current")


class _AlaTestOamConfigFrameType_Type(Integer32):
    """Custom type alaTestOamConfigFrameType based on Integer32"""
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
        *(("none", 0),
          ("ether", 1),
          ("ipv4", 2))
    )


_AlaTestOamConfigFrameType_Type.__name__ = "Integer32"
_AlaTestOamConfigFrameType_Object = MibTableColumn
alaTestOamConfigFrameType = _AlaTestOamConfigFrameType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 65, 1, 1, 3, 1, 1, 21),
    _AlaTestOamConfigFrameType_Type()
)
alaTestOamConfigFrameType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaTestOamConfigFrameType.setStatus("current")
_AlaTestOamConfigRowStatus_Type = RowStatus
_AlaTestOamConfigRowStatus_Object = MibTableColumn
alaTestOamConfigRowStatus = _AlaTestOamConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 65, 1, 1, 3, 1, 1, 23),
    _AlaTestOamConfigRowStatus_Type()
)
alaTestOamConfigRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaTestOamConfigRowStatus.setStatus("current")


class _AlaTestOamConfigRemoteStatsFetchState_Type(Integer32):
    """Custom type alaTestOamConfigRemoteStatsFetchState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("set", 1),
          ("unset", 2))
    )


_AlaTestOamConfigRemoteStatsFetchState_Type.__name__ = "Integer32"
_AlaTestOamConfigRemoteStatsFetchState_Object = MibTableColumn
alaTestOamConfigRemoteStatsFetchState = _AlaTestOamConfigRemoteStatsFetchState_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 65, 1, 1, 3, 1, 1, 24),
    _AlaTestOamConfigRemoteStatsFetchState_Type()
)
alaTestOamConfigRemoteStatsFetchState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaTestOamConfigRemoteStatsFetchState.setStatus("current")
_AlaTestOamConfigRemoteSysMacAddress_Type = MacAddress
_AlaTestOamConfigRemoteSysMacAddress_Object = MibTableColumn
alaTestOamConfigRemoteSysMacAddress = _AlaTestOamConfigRemoteSysMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 65, 1, 1, 3, 1, 1, 25),
    _AlaTestOamConfigRemoteSysMacAddress_Type()
)
alaTestOamConfigRemoteSysMacAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaTestOamConfigRemoteSysMacAddress.setStatus("current")
_AlaTestOamEtherConfigTable_Object = MibTable
alaTestOamEtherConfigTable = _AlaTestOamEtherConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 65, 1, 1, 3, 2)
)
if mibBuilder.loadTexts:
    alaTestOamEtherConfigTable.setStatus("current")
_AlaTestOamEtherConfigEntry_Object = MibTableRow
alaTestOamEtherConfigEntry = _AlaTestOamEtherConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 65, 1, 1, 3, 2, 1)
)
alaTestOamEtherConfigEntry.setIndexNames(
    (0, "ALCATEL-IND1-TEST-OAM-MIB", "alaTestOamConfigTestId"),
)
if mibBuilder.loadTexts:
    alaTestOamEtherConfigEntry.setStatus("current")
_AlaTestOamEtherConfigVlan_Type = VlanId
_AlaTestOamEtherConfigVlan_Object = MibTableColumn
alaTestOamEtherConfigVlan = _AlaTestOamEtherConfigVlan_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 65, 1, 1, 3, 2, 1, 1),
    _AlaTestOamEtherConfigVlan_Type()
)
alaTestOamEtherConfigVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaTestOamEtherConfigVlan.setStatus("current")


class _AlaTestOamEtherConfig8021p_Type(Unsigned32):
    """Custom type alaTestOamEtherConfig8021p based on Unsigned32"""
    defaultValue = 7

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AlaTestOamEtherConfig8021p_Type.__name__ = "Unsigned32"
_AlaTestOamEtherConfig8021p_Object = MibTableColumn
alaTestOamEtherConfig8021p = _AlaTestOamEtherConfig8021p_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 65, 1, 1, 3, 2, 1, 2),
    _AlaTestOamEtherConfig8021p_Type()
)
alaTestOamEtherConfig8021p.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaTestOamEtherConfig8021p.setStatus("current")


class _AlaTestOamEtherConfigDataPattern_Type(OctetString):
    """Custom type alaTestOamEtherConfigDataPattern based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )
    fixed_length = 2


_AlaTestOamEtherConfigDataPattern_Type.__name__ = "OctetString"
_AlaTestOamEtherConfigDataPattern_Object = MibTableColumn
alaTestOamEtherConfigDataPattern = _AlaTestOamEtherConfigDataPattern_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 65, 1, 1, 3, 2, 1, 3),
    _AlaTestOamEtherConfigDataPattern_Type()
)
alaTestOamEtherConfigDataPattern.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaTestOamEtherConfigDataPattern.setStatus("current")


class _AlaTestOamEtherConfigEtherType_Type(Integer32):
    """Custom type alaTestOamEtherConfigEtherType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlaTestOamEtherConfigEtherType_Type.__name__ = "Integer32"
_AlaTestOamEtherConfigEtherType_Object = MibTableColumn
alaTestOamEtherConfigEtherType = _AlaTestOamEtherConfigEtherType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 65, 1, 1, 3, 2, 1, 4),
    _AlaTestOamEtherConfigEtherType_Type()
)
alaTestOamEtherConfigEtherType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaTestOamEtherConfigEtherType.setStatus("current")


class _AlaTestOamEtherConfigCfi_Type(TruthValue):
    """Custom type alaTestOamEtherConfigCfi based on TruthValue"""
    defaultValue = 2


_AlaTestOamEtherConfigCfi_Type.__name__ = "TruthValue"
_AlaTestOamEtherConfigCfi_Object = MibTableColumn
alaTestOamEtherConfigCfi = _AlaTestOamEtherConfigCfi_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 65, 1, 1, 3, 2, 1, 5),
    _AlaTestOamEtherConfigCfi_Type()
)
alaTestOamEtherConfigCfi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaTestOamEtherConfigCfi.setStatus("current")
_AlaTestOamEtherConfigRowStatus_Type = RowStatus
_AlaTestOamEtherConfigRowStatus_Object = MibTableColumn
alaTestOamEtherConfigRowStatus = _AlaTestOamEtherConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 65, 1, 1, 3, 2, 1, 6),
    _AlaTestOamEtherConfigRowStatus_Type()
)
alaTestOamEtherConfigRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaTestOamEtherConfigRowStatus.setStatus("current")
_AlaTestOamIpv4ConfigTable_Object = MibTable
alaTestOamIpv4ConfigTable = _AlaTestOamIpv4ConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 65, 1, 1, 3, 3)
)
if mibBuilder.loadTexts:
    alaTestOamIpv4ConfigTable.setStatus("current")
_AlaTestOamIpv4ConfigEntry_Object = MibTableRow
alaTestOamIpv4ConfigEntry = _AlaTestOamIpv4ConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 65, 1, 1, 3, 3, 1)
)
alaTestOamIpv4ConfigEntry.setIndexNames(
    (0, "ALCATEL-IND1-TEST-OAM-MIB", "alaTestOamConfigTestId"),
)
if mibBuilder.loadTexts:
    alaTestOamIpv4ConfigEntry.setStatus("current")
_AlaTestOamIpv4ConfigVlan_Type = VlanId
_AlaTestOamIpv4ConfigVlan_Object = MibTableColumn
alaTestOamIpv4ConfigVlan = _AlaTestOamIpv4ConfigVlan_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 65, 1, 1, 3, 3, 1, 1),
    _AlaTestOamIpv4ConfigVlan_Type()
)
alaTestOamIpv4ConfigVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaTestOamIpv4ConfigVlan.setStatus("current")


class _AlaTestOamIpv4Config8021p_Type(Unsigned32):
    """Custom type alaTestOamIpv4Config8021p based on Unsigned32"""
    defaultValue = 7

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AlaTestOamIpv4Config8021p_Type.__name__ = "Unsigned32"
_AlaTestOamIpv4Config8021p_Object = MibTableColumn
alaTestOamIpv4Config8021p = _AlaTestOamIpv4Config8021p_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 65, 1, 1, 3, 3, 1, 2),
    _AlaTestOamIpv4Config8021p_Type()
)
alaTestOamIpv4Config8021p.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaTestOamIpv4Config8021p.setStatus("current")


class _AlaTestOamIpv4ConfigDataPattern_Type(OctetString):
    """Custom type alaTestOamIpv4ConfigDataPattern based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )
    fixed_length = 2


_AlaTestOamIpv4ConfigDataPattern_Type.__name__ = "OctetString"
_AlaTestOamIpv4ConfigDataPattern_Object = MibTableColumn
alaTestOamIpv4ConfigDataPattern = _AlaTestOamIpv4ConfigDataPattern_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 65, 1, 1, 3, 3, 1, 3),
    _AlaTestOamIpv4ConfigDataPattern_Type()
)
alaTestOamIpv4ConfigDataPattern.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaTestOamIpv4ConfigDataPattern.setStatus("current")


class _AlaTestOamIpv4ConfigCfi_Type(TruthValue):
    """Custom type alaTestOamIpv4ConfigCfi based on TruthValue"""
    defaultValue = 2


_AlaTestOamIpv4ConfigCfi_Type.__name__ = "TruthValue"
_AlaTestOamIpv4ConfigCfi_Object = MibTableColumn
alaTestOamIpv4ConfigCfi = _AlaTestOamIpv4ConfigCfi_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 65, 1, 1, 3, 3, 1, 4),
    _AlaTestOamIpv4ConfigCfi_Type()
)
alaTestOamIpv4ConfigCfi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaTestOamIpv4ConfigCfi.setStatus("current")


class _AlaTestOamIpv4ConfigSrcIpType_Type(InetAddressType):
    """Custom type alaTestOamIpv4ConfigSrcIpType based on InetAddressType"""
    defaultValue = 1

    subtypeSpec = InetAddressType.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
    )


_AlaTestOamIpv4ConfigSrcIpType_Type.__name__ = "InetAddressType"
_AlaTestOamIpv4ConfigSrcIpType_Object = MibTableColumn
alaTestOamIpv4ConfigSrcIpType = _AlaTestOamIpv4ConfigSrcIpType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 65, 1, 1, 3, 3, 1, 5),
    _AlaTestOamIpv4ConfigSrcIpType_Type()
)
alaTestOamIpv4ConfigSrcIpType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaTestOamIpv4ConfigSrcIpType.setStatus("current")
_AlaTestOamIpv4ConfigSrcIp_Type = InetAddress
_AlaTestOamIpv4ConfigSrcIp_Object = MibTableColumn
alaTestOamIpv4ConfigSrcIp = _AlaTestOamIpv4ConfigSrcIp_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 65, 1, 1, 3, 3, 1, 6),
    _AlaTestOamIpv4ConfigSrcIp_Type()
)
alaTestOamIpv4ConfigSrcIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaTestOamIpv4ConfigSrcIp.setStatus("current")


class _AlaTestOamIpv4ConfigDstIpType_Type(InetAddressType):
    """Custom type alaTestOamIpv4ConfigDstIpType based on InetAddressType"""
    defaultValue = 1

    subtypeSpec = InetAddressType.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
    )


_AlaTestOamIpv4ConfigDstIpType_Type.__name__ = "InetAddressType"
_AlaTestOamIpv4ConfigDstIpType_Object = MibTableColumn
alaTestOamIpv4ConfigDstIpType = _AlaTestOamIpv4ConfigDstIpType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 65, 1, 1, 3, 3, 1, 7),
    _AlaTestOamIpv4ConfigDstIpType_Type()
)
alaTestOamIpv4ConfigDstIpType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaTestOamIpv4ConfigDstIpType.setStatus("current")
_AlaTestOamIpv4ConfigDstIp_Type = InetAddress
_AlaTestOamIpv4ConfigDstIp_Object = MibTableColumn
alaTestOamIpv4ConfigDstIp = _AlaTestOamIpv4ConfigDstIp_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 65, 1, 1, 3, 3, 1, 8),
    _AlaTestOamIpv4ConfigDstIp_Type()
)
alaTestOamIpv4ConfigDstIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaTestOamIpv4ConfigDstIp.setStatus("current")


class _AlaTestOamIpv4ConfigSrcPort_Type(Integer32):
    """Custom type alaTestOamIpv4ConfigSrcPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlaTestOamIpv4ConfigSrcPort_Type.__name__ = "Integer32"
_AlaTestOamIpv4ConfigSrcPort_Object = MibTableColumn
alaTestOamIpv4ConfigSrcPort = _AlaTestOamIpv4ConfigSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 65, 1, 1, 3, 3, 1, 9),
    _AlaTestOamIpv4ConfigSrcPort_Type()
)
alaTestOamIpv4ConfigSrcPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaTestOamIpv4ConfigSrcPort.setStatus("current")


class _AlaTestOamIpv4ConfigDstPort_Type(Integer32):
    """Custom type alaTestOamIpv4ConfigDstPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlaTestOamIpv4ConfigDstPort_Type.__name__ = "Integer32"
_AlaTestOamIpv4ConfigDstPort_Object = MibTableColumn
alaTestOamIpv4ConfigDstPort = _AlaTestOamIpv4ConfigDstPort_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 65, 1, 1, 3, 3, 1, 10),
    _AlaTestOamIpv4ConfigDstPort_Type()
)
alaTestOamIpv4ConfigDstPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaTestOamIpv4ConfigDstPort.setStatus("current")


class _AlaTestOamIpv4ConfigNxtHeader_Type(Integer32):
    """Custom type alaTestOamIpv4ConfigNxtHeader based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(6,
              17,
              255)
        )
    )
    namedValues = NamedValues(
        *(("tcp", 6),
          ("udp", 17),
          ("reserved", 255))
    )


_AlaTestOamIpv4ConfigNxtHeader_Type.__name__ = "Integer32"
_AlaTestOamIpv4ConfigNxtHeader_Object = MibTableColumn
alaTestOamIpv4ConfigNxtHeader = _AlaTestOamIpv4ConfigNxtHeader_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 65, 1, 1, 3, 3, 1, 11),
    _AlaTestOamIpv4ConfigNxtHeader_Type()
)
alaTestOamIpv4ConfigNxtHeader.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaTestOamIpv4ConfigNxtHeader.setStatus("current")


class _AlaTestOamIpv4ConfigTtl_Type(Integer32):
    """Custom type alaTestOamIpv4ConfigTtl based on Integer32"""
    defaultValue = 64

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaTestOamIpv4ConfigTtl_Type.__name__ = "Integer32"
_AlaTestOamIpv4ConfigTtl_Object = MibTableColumn
alaTestOamIpv4ConfigTtl = _AlaTestOamIpv4ConfigTtl_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 65, 1, 1, 3, 3, 1, 12),
    _AlaTestOamIpv4ConfigTtl_Type()
)
alaTestOamIpv4ConfigTtl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaTestOamIpv4ConfigTtl.setStatus("current")


class _AlaTestOamIpv4ConfigTos_Type(Integer32):
    """Custom type alaTestOamIpv4ConfigTos based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaTestOamIpv4ConfigTos_Type.__name__ = "Integer32"
_AlaTestOamIpv4ConfigTos_Object = MibTableColumn
alaTestOamIpv4ConfigTos = _AlaTestOamIpv4ConfigTos_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 65, 1, 1, 3, 3, 1, 13),
    _AlaTestOamIpv4ConfigTos_Type()
)
alaTestOamIpv4ConfigTos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaTestOamIpv4ConfigTos.setStatus("current")
_AlaTestOamIpv4ConfigRowStatus_Type = RowStatus
_AlaTestOamIpv4ConfigRowStatus_Object = MibTableColumn
alaTestOamIpv4ConfigRowStatus = _AlaTestOamIpv4ConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 65, 1, 1, 3, 3, 1, 14),
    _AlaTestOamIpv4ConfigRowStatus_Type()
)
alaTestOamIpv4ConfigRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaTestOamIpv4ConfigRowStatus.setStatus("current")


class _AlaTestOamIPConfigFlowLabel_Type(Integer32):
    """Custom type alaTestOamIPConfigFlowLabel based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1048575),
    )


_AlaTestOamIPConfigFlowLabel_Type.__name__ = "Integer32"
_AlaTestOamIPConfigFlowLabel_Object = MibTableColumn
alaTestOamIPConfigFlowLabel = _AlaTestOamIPConfigFlowLabel_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 65, 1, 1, 3, 3, 1, 15),
    _AlaTestOamIPConfigFlowLabel_Type()
)
alaTestOamIPConfigFlowLabel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaTestOamIPConfigFlowLabel.setStatus("current")
_AlaTestOamStats_ObjectIdentity = ObjectIdentity
alaTestOamStats = _AlaTestOamStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 65, 1, 1, 4)
)
_AlaTestOamStatsTable_Object = MibTable
alaTestOamStatsTable = _AlaTestOamStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 65, 1, 1, 4, 1)
)
if mibBuilder.loadTexts:
    alaTestOamStatsTable.setStatus("current")
_AlaTestOamStatsEntry_Object = MibTableRow
alaTestOamStatsEntry = _AlaTestOamStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 65, 1, 1, 4, 1, 1)
)
alaTestOamStatsEntry.setIndexNames(
    (0, "ALCATEL-IND1-TEST-OAM-MIB", "alaTestOamConfigTestId"),
)
if mibBuilder.loadTexts:
    alaTestOamStatsEntry.setStatus("current")


class _AlaTestOamStatsClearStats_Type(Integer32):
    """Custom type alaTestOamStatsClearStats based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("default", 1),
          ("reset", 2))
    )


_AlaTestOamStatsClearStats_Type.__name__ = "Integer32"
_AlaTestOamStatsClearStats_Object = MibTableColumn
alaTestOamStatsClearStats = _AlaTestOamStatsClearStats_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 65, 1, 1, 4, 1, 1, 1),
    _AlaTestOamStatsClearStats_Type()
)
alaTestOamStatsClearStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaTestOamStatsClearStats.setStatus("current")
_AlaTestOamTxIngressCounter_Type = Counter64
_AlaTestOamTxIngressCounter_Object = MibTableColumn
alaTestOamTxIngressCounter = _AlaTestOamTxIngressCounter_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 65, 1, 1, 4, 1, 1, 2),
    _AlaTestOamTxIngressCounter_Type()
)
alaTestOamTxIngressCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaTestOamTxIngressCounter.setStatus("current")
_AlaTestOamTxEgressCounter_Type = Counter64
_AlaTestOamTxEgressCounter_Object = MibTableColumn
alaTestOamTxEgressCounter = _AlaTestOamTxEgressCounter_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 65, 1, 1, 4, 1, 1, 3),
    _AlaTestOamTxEgressCounter_Type()
)
alaTestOamTxEgressCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaTestOamTxEgressCounter.setStatus("current")
_AlaTestOamRxIngressCounter_Type = Counter64
_AlaTestOamRxIngressCounter_Object = MibTableColumn
alaTestOamRxIngressCounter = _AlaTestOamRxIngressCounter_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 65, 1, 1, 4, 1, 1, 4),
    _AlaTestOamRxIngressCounter_Type()
)
alaTestOamRxIngressCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaTestOamRxIngressCounter.setStatus("current")
_AlaTestOamRemoteStatsCounter_Type = Counter64
_AlaTestOamRemoteStatsCounter_Object = MibTableColumn
alaTestOamRemoteStatsCounter = _AlaTestOamRemoteStatsCounter_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 65, 1, 1, 4, 1, 1, 5),
    _AlaTestOamRemoteStatsCounter_Type()
)
alaTestOamRemoteStatsCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaTestOamRemoteStatsCounter.setStatus("current")
_AlaTestOamBandwidthThroughput_Type = Integer32
_AlaTestOamBandwidthThroughput_Object = MibTableColumn
alaTestOamBandwidthThroughput = _AlaTestOamBandwidthThroughput_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 65, 1, 1, 4, 1, 1, 6),
    _AlaTestOamBandwidthThroughput_Type()
)
alaTestOamBandwidthThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaTestOamBandwidthThroughput.setStatus("current")
_AlaTestOamBandwidthThroughputStr_Type = SnmpAdminString
_AlaTestOamBandwidthThroughputStr_Object = MibTableColumn
alaTestOamBandwidthThroughputStr = _AlaTestOamBandwidthThroughputStr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 65, 1, 1, 4, 1, 1, 7),
    _AlaTestOamBandwidthThroughputStr_Type()
)
alaTestOamBandwidthThroughputStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaTestOamBandwidthThroughputStr.setStatus("current")
_AlaTestOamGroupClearStats_ObjectIdentity = ObjectIdentity
alaTestOamGroupClearStats = _AlaTestOamGroupClearStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 65, 1, 1, 5)
)


class _AlaTestOamGlobalGroupClearStats_Type(Integer32):
    """Custom type alaTestOamGlobalGroupClearStats based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("default", 1),
          ("reset", 2))
    )


_AlaTestOamGlobalGroupClearStats_Type.__name__ = "Integer32"
_AlaTestOamGlobalGroupClearStats_Object = MibScalar
alaTestOamGlobalGroupClearStats = _AlaTestOamGlobalGroupClearStats_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 65, 1, 1, 5, 1),
    _AlaTestOamGlobalGroupClearStats_Type()
)
alaTestOamGlobalGroupClearStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaTestOamGlobalGroupClearStats.setStatus("current")
_AlaTestOamFeederPort_ObjectIdentity = ObjectIdentity
alaTestOamFeederPort = _AlaTestOamFeederPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 65, 1, 1, 6)
)
_AlaTestOamGlobalFeederPort_Type = InterfaceIndex
_AlaTestOamGlobalFeederPort_Object = MibScalar
alaTestOamGlobalFeederPort = _AlaTestOamGlobalFeederPort_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 65, 1, 1, 6, 1),
    _AlaTestOamGlobalFeederPort_Type()
)
alaTestOamGlobalFeederPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaTestOamGlobalFeederPort.setStatus("current")
_AlaTestOamGroupConfig_ObjectIdentity = ObjectIdentity
alaTestOamGroupConfig = _AlaTestOamGroupConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 65, 1, 1, 7)
)
_AlaTestOamGroupConfigTable_Object = MibTable
alaTestOamGroupConfigTable = _AlaTestOamGroupConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 65, 1, 1, 7, 1)
)
if mibBuilder.loadTexts:
    alaTestOamGroupConfigTable.setStatus("current")
_AlaTestOamGroupConfigEntry_Object = MibTableRow
alaTestOamGroupConfigEntry = _AlaTestOamGroupConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 65, 1, 1, 7, 1, 1)
)
alaTestOamGroupConfigEntry.setIndexNames(
    (0, "ALCATEL-IND1-TEST-OAM-MIB", "alaTestOamConfigGroupId"),
)
if mibBuilder.loadTexts:
    alaTestOamGroupConfigEntry.setStatus("current")


class _AlaTestOamConfigGroupId_Type(SnmpAdminString):
    """Custom type alaTestOamConfigGroupId based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AlaTestOamConfigGroupId_Type.__name__ = "SnmpAdminString"
_AlaTestOamConfigGroupId_Object = MibTableColumn
alaTestOamConfigGroupId = _AlaTestOamConfigGroupId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 65, 1, 1, 7, 1, 1, 1),
    _AlaTestOamConfigGroupId_Type()
)
alaTestOamConfigGroupId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alaTestOamConfigGroupId.setStatus("current")


class _AlaTestOamGroupConfigSourceEndpoint_Type(SnmpAdminString):
    """Custom type alaTestOamGroupConfigSourceEndpoint based on SnmpAdminString"""
    defaultValue = OctetString("DEFAULT")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AlaTestOamGroupConfigSourceEndpoint_Type.__name__ = "SnmpAdminString"
_AlaTestOamGroupConfigSourceEndpoint_Object = MibTableColumn
alaTestOamGroupConfigSourceEndpoint = _AlaTestOamGroupConfigSourceEndpoint_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 65, 1, 1, 7, 1, 1, 2),
    _AlaTestOamGroupConfigSourceEndpoint_Type()
)
alaTestOamGroupConfigSourceEndpoint.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaTestOamGroupConfigSourceEndpoint.setStatus("current")


class _AlaTestOamGroupConfigDestinationEndpoint_Type(SnmpAdminString):
    """Custom type alaTestOamGroupConfigDestinationEndpoint based on SnmpAdminString"""
    defaultValue = OctetString("DEFAULT")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AlaTestOamGroupConfigDestinationEndpoint_Type.__name__ = "SnmpAdminString"
_AlaTestOamGroupConfigDestinationEndpoint_Object = MibTableColumn
alaTestOamGroupConfigDestinationEndpoint = _AlaTestOamGroupConfigDestinationEndpoint_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 65, 1, 1, 7, 1, 1, 3),
    _AlaTestOamGroupConfigDestinationEndpoint_Type()
)
alaTestOamGroupConfigDestinationEndpoint.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaTestOamGroupConfigDestinationEndpoint.setStatus("current")


class _AlaTestOamConfigGroupDescription_Type(SnmpAdminString):
    """Custom type alaTestOamConfigGroupDescription based on SnmpAdminString"""
    defaultValue = OctetString("DEFAULT")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AlaTestOamConfigGroupDescription_Type.__name__ = "SnmpAdminString"
_AlaTestOamConfigGroupDescription_Object = MibTableColumn
alaTestOamConfigGroupDescription = _AlaTestOamConfigGroupDescription_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 65, 1, 1, 7, 1, 1, 4),
    _AlaTestOamConfigGroupDescription_Type()
)
alaTestOamConfigGroupDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaTestOamConfigGroupDescription.setStatus("current")


class _AlaTestOamGroupConfigDirection_Type(Integer32):
    """Custom type alaTestOamGroupConfigDirection based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("uniDirectional", 1),
          ("biDirectional", 2))
    )


_AlaTestOamGroupConfigDirection_Type.__name__ = "Integer32"
_AlaTestOamGroupConfigDirection_Object = MibTableColumn
alaTestOamGroupConfigDirection = _AlaTestOamGroupConfigDirection_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 65, 1, 1, 7, 1, 1, 5),
    _AlaTestOamGroupConfigDirection_Type()
)
alaTestOamGroupConfigDirection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaTestOamGroupConfigDirection.setStatus("current")


class _AlaTestOamGroupConfigDuration_Type(Integer32):
    """Custom type alaTestOamGroupConfigDuration based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 3600),
    )


_AlaTestOamGroupConfigDuration_Type.__name__ = "Integer32"
_AlaTestOamGroupConfigDuration_Object = MibTableColumn
alaTestOamGroupConfigDuration = _AlaTestOamGroupConfigDuration_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 65, 1, 1, 7, 1, 1, 6),
    _AlaTestOamGroupConfigDuration_Type()
)
alaTestOamGroupConfigDuration.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaTestOamGroupConfigDuration.setStatus("current")
if mibBuilder.loadTexts:
    alaTestOamGroupConfigDuration.setUnits("seconds")


class _AlaTestOamGroupConfigRole_Type(Integer32):
    """Custom type alaTestOamGroupConfigRole based on Integer32"""
    defaultValue = 0

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
        *(("none", 0),
          ("generator", 1),
          ("analyzer", 2),
          ("loopback", 3))
    )


_AlaTestOamGroupConfigRole_Type.__name__ = "Integer32"
_AlaTestOamGroupConfigRole_Object = MibTableColumn
alaTestOamGroupConfigRole = _AlaTestOamGroupConfigRole_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 65, 1, 1, 7, 1, 1, 7),
    _AlaTestOamGroupConfigRole_Type()
)
alaTestOamGroupConfigRole.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaTestOamGroupConfigRole.setStatus("current")
_AlaTestOamGroupConfigPort_Type = InterfaceIndex
_AlaTestOamGroupConfigPort_Object = MibTableColumn
alaTestOamGroupConfigPort = _AlaTestOamGroupConfigPort_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 65, 1, 1, 7, 1, 1, 8),
    _AlaTestOamGroupConfigPort_Type()
)
alaTestOamGroupConfigPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaTestOamGroupConfigPort.setStatus("current")


class _AlaTestOamGroupConfigGeneratorBandwidth_Type(Integer32):
    """Custom type alaTestOamGroupConfigGeneratorBandwidth based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_AlaTestOamGroupConfigGeneratorBandwidth_Type.__name__ = "Integer32"
_AlaTestOamGroupConfigGeneratorBandwidth_Object = MibTableColumn
alaTestOamGroupConfigGeneratorBandwidth = _AlaTestOamGroupConfigGeneratorBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 65, 1, 1, 7, 1, 1, 9),
    _AlaTestOamGroupConfigGeneratorBandwidth_Type()
)
alaTestOamGroupConfigGeneratorBandwidth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaTestOamGroupConfigGeneratorBandwidth.setStatus("current")


class _AlaTestOamGroupConfigState_Type(Integer32):
    """Custom type alaTestOamGroupConfigState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("start", 1),
          ("stop", 2))
    )


_AlaTestOamGroupConfigState_Type.__name__ = "Integer32"
_AlaTestOamGroupConfigState_Object = MibTableColumn
alaTestOamGroupConfigState = _AlaTestOamGroupConfigState_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 65, 1, 1, 7, 1, 1, 10),
    _AlaTestOamGroupConfigState_Type()
)
alaTestOamGroupConfigState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaTestOamGroupConfigState.setStatus("current")


class _AlaTestOamGroupConfigStatus_Type(Integer32):
    """Custom type alaTestOamGroupConfigStatus based on Integer32"""
    defaultValue = 1

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
        *(("notstarted", 1),
          ("running", 2),
          ("stopped", 3),
          ("ended", 4))
    )


_AlaTestOamGroupConfigStatus_Type.__name__ = "Integer32"
_AlaTestOamGroupConfigStatus_Object = MibTableColumn
alaTestOamGroupConfigStatus = _AlaTestOamGroupConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 65, 1, 1, 7, 1, 1, 11),
    _AlaTestOamGroupConfigStatus_Type()
)
alaTestOamGroupConfigStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaTestOamGroupConfigStatus.setStatus("current")
_AlaTestOamGroupConfigFlowCount_Type = Integer32
_AlaTestOamGroupConfigFlowCount_Object = MibTableColumn
alaTestOamGroupConfigFlowCount = _AlaTestOamGroupConfigFlowCount_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 65, 1, 1, 7, 1, 1, 12),
    _AlaTestOamGroupConfigFlowCount_Type()
)
alaTestOamGroupConfigFlowCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaTestOamGroupConfigFlowCount.setStatus("current")


class _AlaTestOamGroupConfigStatsClear_Type(Integer32):
    """Custom type alaTestOamGroupConfigStatsClear based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("default", 1),
          ("reset", 2))
    )


_AlaTestOamGroupConfigStatsClear_Type.__name__ = "Integer32"
_AlaTestOamGroupConfigStatsClear_Object = MibTableColumn
alaTestOamGroupConfigStatsClear = _AlaTestOamGroupConfigStatsClear_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 65, 1, 1, 7, 1, 1, 13),
    _AlaTestOamGroupConfigStatsClear_Type()
)
alaTestOamGroupConfigStatsClear.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaTestOamGroupConfigStatsClear.setStatus("current")
_AlaTestOamGroupConfigRowStatus_Type = RowStatus
_AlaTestOamGroupConfigRowStatus_Object = MibTableColumn
alaTestOamGroupConfigRowStatus = _AlaTestOamGroupConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 65, 1, 1, 7, 1, 1, 14),
    _AlaTestOamGroupConfigRowStatus_Type()
)
alaTestOamGroupConfigRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaTestOamGroupConfigRowStatus.setStatus("current")


class _AlaTestOamGroupConfigRemoteStatsFetchState_Type(Integer32):
    """Custom type alaTestOamGroupConfigRemoteStatsFetchState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("set", 1),
          ("unset", 2))
    )


_AlaTestOamGroupConfigRemoteStatsFetchState_Type.__name__ = "Integer32"
_AlaTestOamGroupConfigRemoteStatsFetchState_Object = MibTableColumn
alaTestOamGroupConfigRemoteStatsFetchState = _AlaTestOamGroupConfigRemoteStatsFetchState_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 65, 1, 1, 7, 1, 1, 15),
    _AlaTestOamGroupConfigRemoteStatsFetchState_Type()
)
alaTestOamGroupConfigRemoteStatsFetchState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaTestOamGroupConfigRemoteStatsFetchState.setStatus("current")
_AlaTestOamGroupConfigRemoteSysMacAddress_Type = MacAddress
_AlaTestOamGroupConfigRemoteSysMacAddress_Object = MibTableColumn
alaTestOamGroupConfigRemoteSysMacAddress = _AlaTestOamGroupConfigRemoteSysMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 65, 1, 1, 7, 1, 1, 16),
    _AlaTestOamGroupConfigRemoteSysMacAddress_Type()
)
alaTestOamGroupConfigRemoteSysMacAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaTestOamGroupConfigRemoteSysMacAddress.setStatus("current")
_AlaTestOamGroupFlowConfig_ObjectIdentity = ObjectIdentity
alaTestOamGroupFlowConfig = _AlaTestOamGroupFlowConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 65, 1, 1, 8)
)
_AlaTestOamGroupFlowConfigTable_Object = MibTable
alaTestOamGroupFlowConfigTable = _AlaTestOamGroupFlowConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 65, 1, 1, 8, 1)
)
if mibBuilder.loadTexts:
    alaTestOamGroupFlowConfigTable.setStatus("current")
_AlaTestOamGroupFlowConfigEntry_Object = MibTableRow
alaTestOamGroupFlowConfigEntry = _AlaTestOamGroupFlowConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 65, 1, 1, 8, 1, 1)
)
alaTestOamGroupFlowConfigEntry.setIndexNames(
    (0, "ALCATEL-IND1-TEST-OAM-MIB", "alaTestOamConfigGroupId"),
    (0, "ALCATEL-IND1-TEST-OAM-MIB", "alaTestOamConfigTestId"),
)
if mibBuilder.loadTexts:
    alaTestOamGroupFlowConfigEntry.setStatus("current")
_AlaTestOamGroupFlowFrameSrcMacAddress_Type = MacAddress
_AlaTestOamGroupFlowFrameSrcMacAddress_Object = MibTableColumn
alaTestOamGroupFlowFrameSrcMacAddress = _AlaTestOamGroupFlowFrameSrcMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 65, 1, 1, 8, 1, 1, 1),
    _AlaTestOamGroupFlowFrameSrcMacAddress_Type()
)
alaTestOamGroupFlowFrameSrcMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaTestOamGroupFlowFrameSrcMacAddress.setStatus("current")
_AlaTestOamGroupFlowFrameDstMacAddress_Type = MacAddress
_AlaTestOamGroupFlowFrameDstMacAddress_Object = MibTableColumn
alaTestOamGroupFlowFrameDstMacAddress = _AlaTestOamGroupFlowFrameDstMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 65, 1, 1, 8, 1, 1, 2),
    _AlaTestOamGroupFlowFrameDstMacAddress_Type()
)
alaTestOamGroupFlowFrameDstMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaTestOamGroupFlowFrameDstMacAddress.setStatus("current")
_AlaTestOamGroupFlowVlan_Type = VlanId
_AlaTestOamGroupFlowVlan_Object = MibTableColumn
alaTestOamGroupFlowVlan = _AlaTestOamGroupFlowVlan_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 65, 1, 1, 8, 1, 1, 3),
    _AlaTestOamGroupFlowVlan_Type()
)
alaTestOamGroupFlowVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaTestOamGroupFlowVlan.setStatus("current")


class _AlaTestOamGroupFlowGeneratorBandwidth_Type(Integer32):
    """Custom type alaTestOamGroupFlowGeneratorBandwidth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(8, 1000000),
    )


_AlaTestOamGroupFlowGeneratorBandwidth_Type.__name__ = "Integer32"
_AlaTestOamGroupFlowGeneratorBandwidth_Object = MibTableColumn
alaTestOamGroupFlowGeneratorBandwidth = _AlaTestOamGroupFlowGeneratorBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 65, 1, 1, 8, 1, 1, 4),
    _AlaTestOamGroupFlowGeneratorBandwidth_Type()
)
alaTestOamGroupFlowGeneratorBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaTestOamGroupFlowGeneratorBandwidth.setStatus("current")


class _AlaTestOamGroupFlowGeneratorPacketSize_Type(Integer32):
    """Custom type alaTestOamGroupFlowGeneratorPacketSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(64, 9212),
    )


_AlaTestOamGroupFlowGeneratorPacketSize_Type.__name__ = "Integer32"
_AlaTestOamGroupFlowGeneratorPacketSize_Object = MibTableColumn
alaTestOamGroupFlowGeneratorPacketSize = _AlaTestOamGroupFlowGeneratorPacketSize_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 65, 1, 1, 8, 1, 1, 5),
    _AlaTestOamGroupFlowGeneratorPacketSize_Type()
)
alaTestOamGroupFlowGeneratorPacketSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaTestOamGroupFlowGeneratorPacketSize.setStatus("current")
_AlaTestOamGroupFlowConfigRowStatus_Type = RowStatus
_AlaTestOamGroupFlowConfigRowStatus_Object = MibTableColumn
alaTestOamGroupFlowConfigRowStatus = _AlaTestOamGroupFlowConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 65, 1, 1, 8, 1, 1, 6),
    _AlaTestOamGroupFlowConfigRowStatus_Type()
)
alaTestOamGroupFlowConfigRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaTestOamGroupFlowConfigRowStatus.setStatus("current")
_AlaTestOamGroupFlowStats_ObjectIdentity = ObjectIdentity
alaTestOamGroupFlowStats = _AlaTestOamGroupFlowStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 65, 1, 1, 9)
)
_AlaTestOamGroupFlowStatsTable_Object = MibTable
alaTestOamGroupFlowStatsTable = _AlaTestOamGroupFlowStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 65, 1, 1, 9, 1)
)
if mibBuilder.loadTexts:
    alaTestOamGroupFlowStatsTable.setStatus("current")
_AlaTestOamGroupFlowStatsEntry_Object = MibTableRow
alaTestOamGroupFlowStatsEntry = _AlaTestOamGroupFlowStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 65, 1, 1, 9, 1, 1)
)
alaTestOamGroupFlowStatsEntry.setIndexNames(
    (0, "ALCATEL-IND1-TEST-OAM-MIB", "alaTestOamConfigGroupId"),
    (0, "ALCATEL-IND1-TEST-OAM-MIB", "alaTestOamConfigTestId"),
)
if mibBuilder.loadTexts:
    alaTestOamGroupFlowStatsEntry.setStatus("current")
_AlaTestOamGroupFlowTxIngressCounter_Type = Counter64
_AlaTestOamGroupFlowTxIngressCounter_Object = MibTableColumn
alaTestOamGroupFlowTxIngressCounter = _AlaTestOamGroupFlowTxIngressCounter_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 65, 1, 1, 9, 1, 1, 1),
    _AlaTestOamGroupFlowTxIngressCounter_Type()
)
alaTestOamGroupFlowTxIngressCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaTestOamGroupFlowTxIngressCounter.setStatus("current")
_AlaTestOamGroupFlowTxEgressCounter_Type = Counter64
_AlaTestOamGroupFlowTxEgressCounter_Object = MibTableColumn
alaTestOamGroupFlowTxEgressCounter = _AlaTestOamGroupFlowTxEgressCounter_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 65, 1, 1, 9, 1, 1, 2),
    _AlaTestOamGroupFlowTxEgressCounter_Type()
)
alaTestOamGroupFlowTxEgressCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaTestOamGroupFlowTxEgressCounter.setStatus("current")
_AlaTestOamGroupFlowRxIngressCounter_Type = Counter64
_AlaTestOamGroupFlowRxIngressCounter_Object = MibTableColumn
alaTestOamGroupFlowRxIngressCounter = _AlaTestOamGroupFlowRxIngressCounter_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 65, 1, 1, 9, 1, 1, 3),
    _AlaTestOamGroupFlowRxIngressCounter_Type()
)
alaTestOamGroupFlowRxIngressCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaTestOamGroupFlowRxIngressCounter.setStatus("current")
_AlaTestOamGroupFlowRemoteStatsCounter_Type = Counter64
_AlaTestOamGroupFlowRemoteStatsCounter_Object = MibTableColumn
alaTestOamGroupFlowRemoteStatsCounter = _AlaTestOamGroupFlowRemoteStatsCounter_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 65, 1, 1, 9, 1, 1, 4),
    _AlaTestOamGroupFlowRemoteStatsCounter_Type()
)
alaTestOamGroupFlowRemoteStatsCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaTestOamGroupFlowRemoteStatsCounter.setStatus("current")
_AlaTestOamGroupBandwidthThroughput_Type = Integer32
_AlaTestOamGroupBandwidthThroughput_Object = MibTableColumn
alaTestOamGroupBandwidthThroughput = _AlaTestOamGroupBandwidthThroughput_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 65, 1, 1, 9, 1, 1, 5),
    _AlaTestOamGroupBandwidthThroughput_Type()
)
alaTestOamGroupBandwidthThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaTestOamGroupBandwidthThroughput.setStatus("current")
_AlaTestOamGroupBandwidthThroughputStr_Type = SnmpAdminString
_AlaTestOamGroupBandwidthThroughputStr_Object = MibTableColumn
alaTestOamGroupBandwidthThroughputStr = _AlaTestOamGroupBandwidthThroughputStr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 65, 1, 1, 9, 1, 1, 6),
    _AlaTestOamGroupBandwidthThroughputStr_Type()
)
alaTestOamGroupBandwidthThroughputStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaTestOamGroupBandwidthThroughputStr.setStatus("current")
_AlaTestOamSaaConfig_ObjectIdentity = ObjectIdentity
alaTestOamSaaConfig = _AlaTestOamSaaConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 65, 1, 1, 10)
)
_AlaTestOamSaaConfigTable_Object = MibTable
alaTestOamSaaConfigTable = _AlaTestOamSaaConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 65, 1, 1, 10, 1)
)
if mibBuilder.loadTexts:
    alaTestOamSaaConfigTable.setStatus("current")
_AlaTestOamSaaConfigEntry_Object = MibTableRow
alaTestOamSaaConfigEntry = _AlaTestOamSaaConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 65, 1, 1, 10, 1, 1)
)
alaTestOamSaaConfigEntry.setIndexNames(
    (0, "ALCATEL-IND1-TEST-OAM-MIB", "alaTestOamConfigTestId"),
)
if mibBuilder.loadTexts:
    alaTestOamSaaConfigEntry.setStatus("current")


class _AlaTestOamSaaConfigDropEligible_Type(TruthValue):
    """Custom type alaTestOamSaaConfigDropEligible based on TruthValue"""
    defaultValue = 2


_AlaTestOamSaaConfigDropEligible_Type.__name__ = "TruthValue"
_AlaTestOamSaaConfigDropEligible_Object = MibTableColumn
alaTestOamSaaConfigDropEligible = _AlaTestOamSaaConfigDropEligible_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 65, 1, 1, 10, 1, 1, 1),
    _AlaTestOamSaaConfigDropEligible_Type()
)
alaTestOamSaaConfigDropEligible.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaTestOamSaaConfigDropEligible.setStatus("current")


class _AlaTestOamSaaConfigPayloadSize_Type(Integer32):
    """Custom type alaTestOamSaaConfigPayloadSize based on Integer32"""
    defaultValue = 36

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(32, 1500),
    )


_AlaTestOamSaaConfigPayloadSize_Type.__name__ = "Integer32"
_AlaTestOamSaaConfigPayloadSize_Object = MibTableColumn
alaTestOamSaaConfigPayloadSize = _AlaTestOamSaaConfigPayloadSize_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 65, 1, 1, 10, 1, 1, 2),
    _AlaTestOamSaaConfigPayloadSize_Type()
)
alaTestOamSaaConfigPayloadSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaTestOamSaaConfigPayloadSize.setStatus("current")


class _AlaTestOamSaaConfigNumPkts_Type(Integer32):
    """Custom type alaTestOamSaaConfigNumPkts based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_AlaTestOamSaaConfigNumPkts_Type.__name__ = "Integer32"
_AlaTestOamSaaConfigNumPkts_Object = MibTableColumn
alaTestOamSaaConfigNumPkts = _AlaTestOamSaaConfigNumPkts_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 65, 1, 1, 10, 1, 1, 3),
    _AlaTestOamSaaConfigNumPkts_Type()
)
alaTestOamSaaConfigNumPkts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaTestOamSaaConfigNumPkts.setStatus("current")


class _AlaTestOamSaaConfigInterPktDelay_Type(Integer32):
    """Custom type alaTestOamSaaConfigInterPktDelay based on Integer32"""
    defaultValue = 1000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 1000),
    )


_AlaTestOamSaaConfigInterPktDelay_Type.__name__ = "Integer32"
_AlaTestOamSaaConfigInterPktDelay_Object = MibTableColumn
alaTestOamSaaConfigInterPktDelay = _AlaTestOamSaaConfigInterPktDelay_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 65, 1, 1, 10, 1, 1, 4),
    _AlaTestOamSaaConfigInterPktDelay_Type()
)
alaTestOamSaaConfigInterPktDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaTestOamSaaConfigInterPktDelay.setStatus("current")
if mibBuilder.loadTexts:
    alaTestOamSaaConfigInterPktDelay.setUnits("milli-seconds")


class _AlaTestOamSaaConfigVlanPriority_Type(Integer32):
    """Custom type alaTestOamSaaConfigVlanPriority based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AlaTestOamSaaConfigVlanPriority_Type.__name__ = "Integer32"
_AlaTestOamSaaConfigVlanPriority_Object = MibTableColumn
alaTestOamSaaConfigVlanPriority = _AlaTestOamSaaConfigVlanPriority_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 65, 1, 1, 10, 1, 1, 5),
    _AlaTestOamSaaConfigVlanPriority_Type()
)
alaTestOamSaaConfigVlanPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaTestOamSaaConfigVlanPriority.setStatus("current")
if mibBuilder.loadTexts:
    alaTestOamSaaConfigVlanPriority.setUnits("milli-seconds")
_AlaTestOamSaaConfigRowStatus_Type = RowStatus
_AlaTestOamSaaConfigRowStatus_Object = MibTableColumn
alaTestOamSaaConfigRowStatus = _AlaTestOamSaaConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 65, 1, 1, 10, 1, 1, 6),
    _AlaTestOamSaaConfigRowStatus_Type()
)
alaTestOamSaaConfigRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaTestOamSaaConfigRowStatus.setStatus("current")


class _AlaTestOamSaaContinuous_Type(Integer32):
    """Custom type alaTestOamSaaContinuous based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_AlaTestOamSaaContinuous_Type.__name__ = "Integer32"
_AlaTestOamSaaContinuous_Object = MibTableColumn
alaTestOamSaaContinuous = _AlaTestOamSaaContinuous_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 65, 1, 1, 10, 1, 1, 7),
    _AlaTestOamSaaContinuous_Type()
)
alaTestOamSaaContinuous.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaTestOamSaaContinuous.setStatus("current")
_AlaTestOamSaaStats_ObjectIdentity = ObjectIdentity
alaTestOamSaaStats = _AlaTestOamSaaStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 65, 1, 1, 11)
)
_AlaTestOamSaaStatsTable_Object = MibTable
alaTestOamSaaStatsTable = _AlaTestOamSaaStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 65, 1, 1, 11, 1)
)
if mibBuilder.loadTexts:
    alaTestOamSaaStatsTable.setStatus("current")
_AlaTestOamSaaStatsEntry_Object = MibTableRow
alaTestOamSaaStatsEntry = _AlaTestOamSaaStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 65, 1, 1, 11, 1, 1)
)
alaTestOamSaaStatsEntry.setIndexNames(
    (0, "ALCATEL-IND1-TEST-OAM-MIB", "alaTestOamConfigTestId"),
)
if mibBuilder.loadTexts:
    alaTestOamSaaStatsEntry.setStatus("current")
_AlaTestOamSaaPktsSent_Type = Unsigned32
_AlaTestOamSaaPktsSent_Object = MibTableColumn
alaTestOamSaaPktsSent = _AlaTestOamSaaPktsSent_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 65, 1, 1, 11, 1, 1, 1),
    _AlaTestOamSaaPktsSent_Type()
)
alaTestOamSaaPktsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaTestOamSaaPktsSent.setStatus("current")
_AlaTestOamSaaPktsRcvd_Type = Unsigned32
_AlaTestOamSaaPktsRcvd_Object = MibTableColumn
alaTestOamSaaPktsRcvd = _AlaTestOamSaaPktsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 65, 1, 1, 11, 1, 1, 2),
    _AlaTestOamSaaPktsRcvd_Type()
)
alaTestOamSaaPktsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaTestOamSaaPktsRcvd.setStatus("current")
_AlaTestOamSaaRunTime_Type = DateAndTime
_AlaTestOamSaaRunTime_Object = MibTableColumn
alaTestOamSaaRunTime = _AlaTestOamSaaRunTime_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 65, 1, 1, 11, 1, 1, 3),
    _AlaTestOamSaaRunTime_Type()
)
alaTestOamSaaRunTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaTestOamSaaRunTime.setStatus("current")
_AlaTestOamSaaMinRTT_Type = Integer32
_AlaTestOamSaaMinRTT_Object = MibTableColumn
alaTestOamSaaMinRTT = _AlaTestOamSaaMinRTT_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 65, 1, 1, 11, 1, 1, 4),
    _AlaTestOamSaaMinRTT_Type()
)
alaTestOamSaaMinRTT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaTestOamSaaMinRTT.setStatus("current")
if mibBuilder.loadTexts:
    alaTestOamSaaMinRTT.setUnits("micro-seconds")
_AlaTestOamSaaAvgRTT_Type = Integer32
_AlaTestOamSaaAvgRTT_Object = MibTableColumn
alaTestOamSaaAvgRTT = _AlaTestOamSaaAvgRTT_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 65, 1, 1, 11, 1, 1, 5),
    _AlaTestOamSaaAvgRTT_Type()
)
alaTestOamSaaAvgRTT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaTestOamSaaAvgRTT.setStatus("current")
if mibBuilder.loadTexts:
    alaTestOamSaaAvgRTT.setUnits("micro-seconds")
_AlaTestOamSaaMaxRTT_Type = Integer32
_AlaTestOamSaaMaxRTT_Object = MibTableColumn
alaTestOamSaaMaxRTT = _AlaTestOamSaaMaxRTT_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 65, 1, 1, 11, 1, 1, 6),
    _AlaTestOamSaaMaxRTT_Type()
)
alaTestOamSaaMaxRTT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaTestOamSaaMaxRTT.setStatus("current")
if mibBuilder.loadTexts:
    alaTestOamSaaMaxRTT.setUnits("micro-seconds")
_AlaTestOamSaaMinJitter_Type = Integer32
_AlaTestOamSaaMinJitter_Object = MibTableColumn
alaTestOamSaaMinJitter = _AlaTestOamSaaMinJitter_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 65, 1, 1, 11, 1, 1, 7),
    _AlaTestOamSaaMinJitter_Type()
)
alaTestOamSaaMinJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaTestOamSaaMinJitter.setStatus("current")
_AlaTestOamSaaAvgJitter_Type = Integer32
_AlaTestOamSaaAvgJitter_Object = MibTableColumn
alaTestOamSaaAvgJitter = _AlaTestOamSaaAvgJitter_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 65, 1, 1, 11, 1, 1, 8),
    _AlaTestOamSaaAvgJitter_Type()
)
alaTestOamSaaAvgJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaTestOamSaaAvgJitter.setStatus("current")
_AlaTestOamSaaMaxJitter_Type = Integer32
_AlaTestOamSaaMaxJitter_Object = MibTableColumn
alaTestOamSaaMaxJitter = _AlaTestOamSaaMaxJitter_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 65, 1, 1, 11, 1, 1, 9),
    _AlaTestOamSaaMaxJitter_Type()
)
alaTestOamSaaMaxJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaTestOamSaaMaxJitter.setStatus("current")
_AlaTestOamGroupFlowSaaStats_ObjectIdentity = ObjectIdentity
alaTestOamGroupFlowSaaStats = _AlaTestOamGroupFlowSaaStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 65, 1, 1, 12)
)
_AlaTestOamGroupFlowSaaStatsTable_Object = MibTable
alaTestOamGroupFlowSaaStatsTable = _AlaTestOamGroupFlowSaaStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 65, 1, 1, 12, 1)
)
if mibBuilder.loadTexts:
    alaTestOamGroupFlowSaaStatsTable.setStatus("current")
_AlaTestOamGroupFlowSaaStatsEntry_Object = MibTableRow
alaTestOamGroupFlowSaaStatsEntry = _AlaTestOamGroupFlowSaaStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 65, 1, 1, 12, 1, 1)
)
alaTestOamGroupFlowSaaStatsEntry.setIndexNames(
    (0, "ALCATEL-IND1-TEST-OAM-MIB", "alaTestOamConfigGroupId"),
    (0, "ALCATEL-IND1-TEST-OAM-MIB", "alaTestOamConfigTestId"),
)
if mibBuilder.loadTexts:
    alaTestOamGroupFlowSaaStatsEntry.setStatus("current")
_AlaTestOamGroupFlowSaaPktsSent_Type = Unsigned32
_AlaTestOamGroupFlowSaaPktsSent_Object = MibTableColumn
alaTestOamGroupFlowSaaPktsSent = _AlaTestOamGroupFlowSaaPktsSent_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 65, 1, 1, 12, 1, 1, 1),
    _AlaTestOamGroupFlowSaaPktsSent_Type()
)
alaTestOamGroupFlowSaaPktsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaTestOamGroupFlowSaaPktsSent.setStatus("current")
_AlaTestOamGroupFlowSaaPktsRcvd_Type = Unsigned32
_AlaTestOamGroupFlowSaaPktsRcvd_Object = MibTableColumn
alaTestOamGroupFlowSaaPktsRcvd = _AlaTestOamGroupFlowSaaPktsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 65, 1, 1, 12, 1, 1, 2),
    _AlaTestOamGroupFlowSaaPktsRcvd_Type()
)
alaTestOamGroupFlowSaaPktsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaTestOamGroupFlowSaaPktsRcvd.setStatus("current")
_AlaTestOamGroupFlowSaaRunTime_Type = DateAndTime
_AlaTestOamGroupFlowSaaRunTime_Object = MibTableColumn
alaTestOamGroupFlowSaaRunTime = _AlaTestOamGroupFlowSaaRunTime_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 65, 1, 1, 12, 1, 1, 3),
    _AlaTestOamGroupFlowSaaRunTime_Type()
)
alaTestOamGroupFlowSaaRunTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaTestOamGroupFlowSaaRunTime.setStatus("current")
_AlaTestOamGroupFlowSaaMinRTT_Type = Integer32
_AlaTestOamGroupFlowSaaMinRTT_Object = MibTableColumn
alaTestOamGroupFlowSaaMinRTT = _AlaTestOamGroupFlowSaaMinRTT_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 65, 1, 1, 12, 1, 1, 4),
    _AlaTestOamGroupFlowSaaMinRTT_Type()
)
alaTestOamGroupFlowSaaMinRTT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaTestOamGroupFlowSaaMinRTT.setStatus("current")
if mibBuilder.loadTexts:
    alaTestOamGroupFlowSaaMinRTT.setUnits("micro-seconds")
_AlaTestOamGroupFlowSaaAvgRTT_Type = Integer32
_AlaTestOamGroupFlowSaaAvgRTT_Object = MibTableColumn
alaTestOamGroupFlowSaaAvgRTT = _AlaTestOamGroupFlowSaaAvgRTT_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 65, 1, 1, 12, 1, 1, 5),
    _AlaTestOamGroupFlowSaaAvgRTT_Type()
)
alaTestOamGroupFlowSaaAvgRTT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaTestOamGroupFlowSaaAvgRTT.setStatus("current")
if mibBuilder.loadTexts:
    alaTestOamGroupFlowSaaAvgRTT.setUnits("micro-seconds")
_AlaTestOamGroupFlowSaaMaxRTT_Type = Integer32
_AlaTestOamGroupFlowSaaMaxRTT_Object = MibTableColumn
alaTestOamGroupFlowSaaMaxRTT = _AlaTestOamGroupFlowSaaMaxRTT_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 65, 1, 1, 12, 1, 1, 6),
    _AlaTestOamGroupFlowSaaMaxRTT_Type()
)
alaTestOamGroupFlowSaaMaxRTT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaTestOamGroupFlowSaaMaxRTT.setStatus("current")
if mibBuilder.loadTexts:
    alaTestOamGroupFlowSaaMaxRTT.setUnits("micro-seconds")
_AlaTestOamGroupFlowSaaMinJitter_Type = Integer32
_AlaTestOamGroupFlowSaaMinJitter_Object = MibTableColumn
alaTestOamGroupFlowSaaMinJitter = _AlaTestOamGroupFlowSaaMinJitter_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 65, 1, 1, 12, 1, 1, 7),
    _AlaTestOamGroupFlowSaaMinJitter_Type()
)
alaTestOamGroupFlowSaaMinJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaTestOamGroupFlowSaaMinJitter.setStatus("current")
_AlaTestOamGroupFlowSaaAvgJitter_Type = Integer32
_AlaTestOamGroupFlowSaaAvgJitter_Object = MibTableColumn
alaTestOamGroupFlowSaaAvgJitter = _AlaTestOamGroupFlowSaaAvgJitter_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 65, 1, 1, 12, 1, 1, 8),
    _AlaTestOamGroupFlowSaaAvgJitter_Type()
)
alaTestOamGroupFlowSaaAvgJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaTestOamGroupFlowSaaAvgJitter.setStatus("current")
_AlaTestOamGroupFlowSaaMaxJitter_Type = Integer32
_AlaTestOamGroupFlowSaaMaxJitter_Object = MibTableColumn
alaTestOamGroupFlowSaaMaxJitter = _AlaTestOamGroupFlowSaaMaxJitter_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 65, 1, 1, 12, 1, 1, 9),
    _AlaTestOamGroupFlowSaaMaxJitter_Type()
)
alaTestOamGroupFlowSaaMaxJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaTestOamGroupFlowSaaMaxJitter.setStatus("current")
_AlaTestOamStatsFlashSave_ObjectIdentity = ObjectIdentity
alaTestOamStatsFlashSave = _AlaTestOamStatsFlashSave_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 65, 1, 1, 13)
)


class _AlaTestOamGlobalStatsFlashSave_Type(Integer32):
    """Custom type alaTestOamGlobalStatsFlashSave based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_AlaTestOamGlobalStatsFlashSave_Type.__name__ = "Integer32"
_AlaTestOamGlobalStatsFlashSave_Object = MibScalar
alaTestOamGlobalStatsFlashSave = _AlaTestOamGlobalStatsFlashSave_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 65, 1, 1, 13, 1),
    _AlaTestOamGlobalStatsFlashSave_Type()
)
alaTestOamGlobalStatsFlashSave.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaTestOamGlobalStatsFlashSave.setStatus("current")
_AlaTestOamTrapObj_ObjectIdentity = ObjectIdentity
alaTestOamTrapObj = _AlaTestOamTrapObj_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 65, 1, 1, 14)
)
_AlaTestOamStatsWriteDoneTrapStr_Type = SnmpAdminString
_AlaTestOamStatsWriteDoneTrapStr_Object = MibScalar
alaTestOamStatsWriteDoneTrapStr = _AlaTestOamStatsWriteDoneTrapStr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 65, 1, 1, 14, 1),
    _AlaTestOamStatsWriteDoneTrapStr_Type()
)
alaTestOamStatsWriteDoneTrapStr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alaTestOamStatsWriteDoneTrapStr.setStatus("current")
_AlaTestOamConformance_ObjectIdentity = ObjectIdentity
alaTestOamConformance = _AlaTestOamConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 65, 1, 2)
)
_AlaTestOamMIBCompliances_ObjectIdentity = ObjectIdentity
alaTestOamMIBCompliances = _AlaTestOamMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 65, 1, 2, 1)
)
_AlaTestOamMIBGroups_ObjectIdentity = ObjectIdentity
alaTestOamMIBGroups = _AlaTestOamMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 65, 1, 2, 2)
)

# Managed Objects groups

alaTestOamGlobalClearStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 65, 1, 2, 2, 1)
)
alaTestOamGlobalClearStatsGroup.setObjects(
    ("ALCATEL-IND1-TEST-OAM-MIB", "alaTestOamGlobalClearStats")
)
if mibBuilder.loadTexts:
    alaTestOamGlobalClearStatsGroup.setStatus("current")

alaTestOamConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 65, 1, 2, 2, 2)
)
alaTestOamConfigGroup.setObjects(
      *(("ALCATEL-IND1-TEST-OAM-MIB", "alaTestOamConfigSourceEndpoint"),
        ("ALCATEL-IND1-TEST-OAM-MIB", "alaTestOamConfigDestinationEndpoint"),
        ("ALCATEL-IND1-TEST-OAM-MIB", "alaTestOamConfigTestDescription"),
        ("ALCATEL-IND1-TEST-OAM-MIB", "alaTestOamConfigGeneratorTestMode"),
        ("ALCATEL-IND1-TEST-OAM-MIB", "alaTestOamConfigAnalyzerTestMode"),
        ("ALCATEL-IND1-TEST-OAM-MIB", "alaTestOamConfigLoopbackTestMode"),
        ("ALCATEL-IND1-TEST-OAM-MIB", "alaTestOamConfigDirection"),
        ("ALCATEL-IND1-TEST-OAM-MIB", "alaTestOamConfigFrameSrcMacAddress"),
        ("ALCATEL-IND1-TEST-OAM-MIB", "alaTestOamConfigFrameDstMacAddress"),
        ("ALCATEL-IND1-TEST-OAM-MIB", "alaTestOamConfigDuration"),
        ("ALCATEL-IND1-TEST-OAM-MIB", "alaTestOamConfigVlan"),
        ("ALCATEL-IND1-TEST-OAM-MIB", "alaTestOamConfigRole"),
        ("ALCATEL-IND1-TEST-OAM-MIB", "alaTestOamConfigPort"),
        ("ALCATEL-IND1-TEST-OAM-MIB", "alaTestOamConfigSourceLearningStatus"),
        ("ALCATEL-IND1-TEST-OAM-MIB", "alaTestOamConfigGeneratorMode"),
        ("ALCATEL-IND1-TEST-OAM-MIB", "alaTestOamConfigGeneratorBandwidth"),
        ("ALCATEL-IND1-TEST-OAM-MIB", "alaTestOamConfigGeneratorPacketSize"),
        ("ALCATEL-IND1-TEST-OAM-MIB", "alaTestOamConfigTestIdState"),
        ("ALCATEL-IND1-TEST-OAM-MIB", "alaTestOamConfigTestIdStatus"),
        ("ALCATEL-IND1-TEST-OAM-MIB", "alaTestOamConfigFrameType"),
        ("ALCATEL-IND1-TEST-OAM-MIB", "alaTestOamConfigRowStatus"),
        ("ALCATEL-IND1-TEST-OAM-MIB", "alaTestOamEtherConfigVlan"),
        ("ALCATEL-IND1-TEST-OAM-MIB", "alaTestOamEtherConfig8021p"),
        ("ALCATEL-IND1-TEST-OAM-MIB", "alaTestOamEtherConfigDataPattern"),
        ("ALCATEL-IND1-TEST-OAM-MIB", "alaTestOamEtherConfigEtherType"),
        ("ALCATEL-IND1-TEST-OAM-MIB", "alaTestOamEtherConfigCfi"),
        ("ALCATEL-IND1-TEST-OAM-MIB", "alaTestOamEtherConfigRowStatus"),
        ("ALCATEL-IND1-TEST-OAM-MIB", "alaTestOamIpv4ConfigVlan"),
        ("ALCATEL-IND1-TEST-OAM-MIB", "alaTestOamIpv4Config8021p"),
        ("ALCATEL-IND1-TEST-OAM-MIB", "alaTestOamIpv4ConfigDataPattern"),
        ("ALCATEL-IND1-TEST-OAM-MIB", "alaTestOamIpv4ConfigCfi"),
        ("ALCATEL-IND1-TEST-OAM-MIB", "alaTestOamIpv4ConfigSrcIpType"),
        ("ALCATEL-IND1-TEST-OAM-MIB", "alaTestOamIpv4ConfigSrcIp"),
        ("ALCATEL-IND1-TEST-OAM-MIB", "alaTestOamIpv4ConfigDstIpType"),
        ("ALCATEL-IND1-TEST-OAM-MIB", "alaTestOamIpv4ConfigDstIp"),
        ("ALCATEL-IND1-TEST-OAM-MIB", "alaTestOamIpv4ConfigSrcPort"),
        ("ALCATEL-IND1-TEST-OAM-MIB", "alaTestOamIpv4ConfigDstPort"),
        ("ALCATEL-IND1-TEST-OAM-MIB", "alaTestOamIpv4ConfigNxtHeader"),
        ("ALCATEL-IND1-TEST-OAM-MIB", "alaTestOamIpv4ConfigTtl"),
        ("ALCATEL-IND1-TEST-OAM-MIB", "alaTestOamIpv4ConfigTos"),
        ("ALCATEL-IND1-TEST-OAM-MIB", "alaTestOamIpv4ConfigRowStatus"),
        ("ALCATEL-IND1-TEST-OAM-MIB", "alaTestOamIPConfigFlowLabel"),
        ("ALCATEL-IND1-TEST-OAM-MIB", "alaTestOamSaaConfigDropEligible"),
        ("ALCATEL-IND1-TEST-OAM-MIB", "alaTestOamSaaConfigPayloadSize"),
        ("ALCATEL-IND1-TEST-OAM-MIB", "alaTestOamSaaConfigNumPkts"),
        ("ALCATEL-IND1-TEST-OAM-MIB", "alaTestOamSaaConfigInterPktDelay"),
        ("ALCATEL-IND1-TEST-OAM-MIB", "alaTestOamSaaConfigVlanPriority"),
        ("ALCATEL-IND1-TEST-OAM-MIB", "alaTestOamSaaConfigRowStatus"),
        ("ALCATEL-IND1-TEST-OAM-MIB", "alaTestOamSaaContinuous"))
)
if mibBuilder.loadTexts:
    alaTestOamConfigGroup.setStatus("current")

alaTestOamStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 65, 1, 2, 2, 3)
)
alaTestOamStatsGroup.setObjects(
      *(("ALCATEL-IND1-TEST-OAM-MIB", "alaTestOamStatsClearStats"),
        ("ALCATEL-IND1-TEST-OAM-MIB", "alaTestOamTxIngressCounter"),
        ("ALCATEL-IND1-TEST-OAM-MIB", "alaTestOamTxEgressCounter"),
        ("ALCATEL-IND1-TEST-OAM-MIB", "alaTestOamRxIngressCounter"),
        ("ALCATEL-IND1-TEST-OAM-MIB", "alaTestOamRemoteStatsCounter"))
)
if mibBuilder.loadTexts:
    alaTestOamStatsGroup.setStatus("current")

alaTestOamGlobalGroupClearStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 65, 1, 2, 2, 5)
)
alaTestOamGlobalGroupClearStatsGroup.setObjects(
    ("ALCATEL-IND1-TEST-OAM-MIB", "alaTestOamGlobalGroupClearStats")
)
if mibBuilder.loadTexts:
    alaTestOamGlobalGroupClearStatsGroup.setStatus("current")

alaTestOamGlobalFeederPortGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 65, 1, 2, 2, 6)
)
alaTestOamGlobalFeederPortGroup.setObjects(
    ("ALCATEL-IND1-TEST-OAM-MIB", "alaTestOamGlobalFeederPort")
)
if mibBuilder.loadTexts:
    alaTestOamGlobalFeederPortGroup.setStatus("current")

alaTestOamGroupConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 65, 1, 2, 2, 7)
)
alaTestOamGroupConfigGroup.setObjects(
      *(("ALCATEL-IND1-TEST-OAM-MIB", "alaTestOamGroupConfigSourceEndpoint"),
        ("ALCATEL-IND1-TEST-OAM-MIB", "alaTestOamGroupConfigDestinationEndpoint"),
        ("ALCATEL-IND1-TEST-OAM-MIB", "alaTestOamConfigGroupDescription"),
        ("ALCATEL-IND1-TEST-OAM-MIB", "alaTestOamGroupConfigDirection"),
        ("ALCATEL-IND1-TEST-OAM-MIB", "alaTestOamGroupConfigDuration"),
        ("ALCATEL-IND1-TEST-OAM-MIB", "alaTestOamGroupConfigRole"),
        ("ALCATEL-IND1-TEST-OAM-MIB", "alaTestOamGroupConfigPort"),
        ("ALCATEL-IND1-TEST-OAM-MIB", "alaTestOamGroupConfigGeneratorBandwidth"),
        ("ALCATEL-IND1-TEST-OAM-MIB", "alaTestOamGroupConfigState"),
        ("ALCATEL-IND1-TEST-OAM-MIB", "alaTestOamGroupConfigStatus"),
        ("ALCATEL-IND1-TEST-OAM-MIB", "alaTestOamGroupConfigFlowCount"),
        ("ALCATEL-IND1-TEST-OAM-MIB", "alaTestOamGroupConfigStatsClear"),
        ("ALCATEL-IND1-TEST-OAM-MIB", "alaTestOamGroupConfigRowStatus"))
)
if mibBuilder.loadTexts:
    alaTestOamGroupConfigGroup.setStatus("current")

alaTestOamGroupFlowConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 65, 1, 2, 2, 8)
)
alaTestOamGroupFlowConfigGroup.setObjects(
      *(("ALCATEL-IND1-TEST-OAM-MIB", "alaTestOamGroupFlowFrameSrcMacAddress"),
        ("ALCATEL-IND1-TEST-OAM-MIB", "alaTestOamGroupFlowFrameDstMacAddress"),
        ("ALCATEL-IND1-TEST-OAM-MIB", "alaTestOamGroupFlowVlan"),
        ("ALCATEL-IND1-TEST-OAM-MIB", "alaTestOamGroupFlowGeneratorBandwidth"),
        ("ALCATEL-IND1-TEST-OAM-MIB", "alaTestOamGroupFlowGeneratorPacketSize"),
        ("ALCATEL-IND1-TEST-OAM-MIB", "alaTestOamGroupFlowConfigRowStatus"))
)
if mibBuilder.loadTexts:
    alaTestOamGroupFlowConfigGroup.setStatus("current")

alaTestOamGroupFlowStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 65, 1, 2, 2, 9)
)
alaTestOamGroupFlowStatsGroup.setObjects(
      *(("ALCATEL-IND1-TEST-OAM-MIB", "alaTestOamGroupFlowTxIngressCounter"),
        ("ALCATEL-IND1-TEST-OAM-MIB", "alaTestOamGroupFlowTxEgressCounter"),
        ("ALCATEL-IND1-TEST-OAM-MIB", "alaTestOamGroupFlowRxIngressCounter"),
        ("ALCATEL-IND1-TEST-OAM-MIB", "alaTestOamGroupFlowRemoteStatsCounter"),
        ("ALCATEL-IND1-TEST-OAM-MIB", "alaTestOamGroupBandwidthThroughput"),
        ("ALCATEL-IND1-TEST-OAM-MIB", "alaTestOamGroupBandwidthThroughputStr"))
)
if mibBuilder.loadTexts:
    alaTestOamGroupFlowStatsGroup.setStatus("current")

alaTestOamSaaStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 65, 1, 2, 2, 10)
)
alaTestOamSaaStatsGroup.setObjects(
      *(("ALCATEL-IND1-TEST-OAM-MIB", "alaTestOamSaaPktsSent"),
        ("ALCATEL-IND1-TEST-OAM-MIB", "alaTestOamSaaPktsRcvd"),
        ("ALCATEL-IND1-TEST-OAM-MIB", "alaTestOamSaaRunTime"),
        ("ALCATEL-IND1-TEST-OAM-MIB", "alaTestOamSaaMinRTT"),
        ("ALCATEL-IND1-TEST-OAM-MIB", "alaTestOamSaaAvgRTT"),
        ("ALCATEL-IND1-TEST-OAM-MIB", "alaTestOamSaaMaxRTT"),
        ("ALCATEL-IND1-TEST-OAM-MIB", "alaTestOamSaaMinJitter"),
        ("ALCATEL-IND1-TEST-OAM-MIB", "alaTestOamSaaAvgJitter"),
        ("ALCATEL-IND1-TEST-OAM-MIB", "alaTestOamSaaMaxJitter"))
)
if mibBuilder.loadTexts:
    alaTestOamSaaStatsGroup.setStatus("current")

alaTestOamGroupFlowSaaStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 65, 1, 2, 2, 11)
)
alaTestOamGroupFlowSaaStatsGroup.setObjects(
      *(("ALCATEL-IND1-TEST-OAM-MIB", "alaTestOamGroupFlowSaaPktsSent"),
        ("ALCATEL-IND1-TEST-OAM-MIB", "alaTestOamGroupFlowSaaPktsRcvd"),
        ("ALCATEL-IND1-TEST-OAM-MIB", "alaTestOamGroupFlowSaaRunTime"),
        ("ALCATEL-IND1-TEST-OAM-MIB", "alaTestOamGroupFlowSaaMinRTT"),
        ("ALCATEL-IND1-TEST-OAM-MIB", "alaTestOamGroupFlowSaaAvgRTT"),
        ("ALCATEL-IND1-TEST-OAM-MIB", "alaTestOamGroupFlowSaaMaxRTT"),
        ("ALCATEL-IND1-TEST-OAM-MIB", "alaTestOamGroupFlowSaaMinJitter"),
        ("ALCATEL-IND1-TEST-OAM-MIB", "alaTestOamGroupFlowSaaAvgJitter"),
        ("ALCATEL-IND1-TEST-OAM-MIB", "alaTestOamGroupFlowSaaMaxJitter"))
)
if mibBuilder.loadTexts:
    alaTestOamGroupFlowSaaStatsGroup.setStatus("current")

alaTestOamGlobalStatsFlashSaveGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 65, 1, 2, 2, 12)
)
alaTestOamGlobalStatsFlashSaveGroup.setObjects(
    ("ALCATEL-IND1-TEST-OAM-MIB", "alaTestOamGlobalStatsFlashSave")
)
if mibBuilder.loadTexts:
    alaTestOamGlobalStatsFlashSaveGroup.setStatus("current")


# Notification objects

alaTestOamTxDoneTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 65, 1, 0, 1)
)
alaTestOamTxDoneTrap.setObjects(
      *(("ALCATEL-IND1-TEST-OAM-MIB", "alaTestOamConfigTestId"),
        ("ALCATEL-IND1-TEST-OAM-MIB", "alaTestOamConfigSourceEndpoint"),
        ("ALCATEL-IND1-TEST-OAM-MIB", "alaTestOamConfigTestIdStatus"))
)
if mibBuilder.loadTexts:
    alaTestOamTxDoneTrap.setStatus(
        "current"
    )

alaTestOamRxReadyTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 65, 1, 0, 2)
)
alaTestOamRxReadyTrap.setObjects(
      *(("ALCATEL-IND1-TEST-OAM-MIB", "alaTestOamConfigTestId"),
        ("ALCATEL-IND1-TEST-OAM-MIB", "alaTestOamConfigDestinationEndpoint"),
        ("ALCATEL-IND1-TEST-OAM-MIB", "alaTestOamConfigTestIdStatus"))
)
if mibBuilder.loadTexts:
    alaTestOamRxReadyTrap.setStatus(
        "current"
    )

alaTestOamTestAbortTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 65, 1, 0, 3)
)
alaTestOamTestAbortTrap.setObjects(
    ("ALCATEL-IND1-TEST-OAM-MIB", "alaTestOamConfigTestId")
)
if mibBuilder.loadTexts:
    alaTestOamTestAbortTrap.setStatus(
        "current"
    )

alaTestOamGroupTxDoneTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 65, 1, 0, 4)
)
alaTestOamGroupTxDoneTrap.setObjects(
      *(("ALCATEL-IND1-TEST-OAM-MIB", "alaTestOamConfigGroupId"),
        ("ALCATEL-IND1-TEST-OAM-MIB", "alaTestOamGroupConfigSourceEndpoint"),
        ("ALCATEL-IND1-TEST-OAM-MIB", "alaTestOamGroupConfigStatus"))
)
if mibBuilder.loadTexts:
    alaTestOamGroupTxDoneTrap.setStatus(
        "current"
    )

alaTestOamGroupRxReadyTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 65, 1, 0, 5)
)
alaTestOamGroupRxReadyTrap.setObjects(
      *(("ALCATEL-IND1-TEST-OAM-MIB", "alaTestOamConfigGroupId"),
        ("ALCATEL-IND1-TEST-OAM-MIB", "alaTestOamGroupConfigDestinationEndpoint"),
        ("ALCATEL-IND1-TEST-OAM-MIB", "alaTestOamGroupConfigStatus"))
)
if mibBuilder.loadTexts:
    alaTestOamGroupRxReadyTrap.setStatus(
        "current"
    )

alaTestOamGroupAbortTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 65, 1, 0, 6)
)
alaTestOamGroupAbortTrap.setObjects(
    ("ALCATEL-IND1-TEST-OAM-MIB", "alaTestOamConfigGroupId")
)
if mibBuilder.loadTexts:
    alaTestOamGroupAbortTrap.setStatus(
        "current"
    )

alaTestOamStatsWriteDoneTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 65, 1, 0, 7)
)
alaTestOamStatsWriteDoneTrap.setObjects(
    ("ALCATEL-IND1-TEST-OAM-MIB", "alaTestOamStatsWriteDoneTrapStr")
)
if mibBuilder.loadTexts:
    alaTestOamStatsWriteDoneTrap.setStatus(
        "current"
    )


# Notifications groups

alaTestOamNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 65, 1, 2, 2, 4)
)
alaTestOamNotificationGroup.setObjects(
      *(("ALCATEL-IND1-TEST-OAM-MIB", "alaTestOamTxDoneTrap"),
        ("ALCATEL-IND1-TEST-OAM-MIB", "alaTestOamRxReadyTrap"),
        ("ALCATEL-IND1-TEST-OAM-MIB", "alaTestOamTestAbortTrap"),
        ("ALCATEL-IND1-TEST-OAM-MIB", "alaTestOamGroupTxDoneTrap"),
        ("ALCATEL-IND1-TEST-OAM-MIB", "alaTestOamGroupRxReadyTrap"),
        ("ALCATEL-IND1-TEST-OAM-MIB", "alaTestOamGroupAbortTrap"),
        ("ALCATEL-IND1-TEST-OAM-MIB", "alaTestOamStatsWriteDoneTrap"))
)
if mibBuilder.loadTexts:
    alaTestOamNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

alaTestOamCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 65, 1, 2, 1, 1)
)
alaTestOamCompliance.setObjects(
      *(("ALCATEL-IND1-TEST-OAM-MIB", "alaTestOamGlobalClearStatsGroup"),
        ("ALCATEL-IND1-TEST-OAM-MIB", "alaTestOamConfigGroup"),
        ("ALCATEL-IND1-TEST-OAM-MIB", "alaTestOamStatsGroup"),
        ("ALCATEL-IND1-TEST-OAM-MIB", "alaTestOamNotificationGroup"),
        ("ALCATEL-IND1-TEST-OAM-MIB", "alaTestOamGlobalGroupClearStatsGroup"),
        ("ALCATEL-IND1-TEST-OAM-MIB", "alaTestOamGlobalFeederPortGroup"),
        ("ALCATEL-IND1-TEST-OAM-MIB", "alaTestOamGroupConfigGroup"),
        ("ALCATEL-IND1-TEST-OAM-MIB", "alaTestOamGroupFlowConfigGroup"),
        ("ALCATEL-IND1-TEST-OAM-MIB", "alaTestOamGroupFlowStatsGroup"))
)
if mibBuilder.loadTexts:
    alaTestOamCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALCATEL-IND1-TEST-OAM-MIB",
    **{"alcatelIND1TestOamMIB": alcatelIND1TestOamMIB,
       "alaTestOamNotifications": alaTestOamNotifications,
       "alaTestOamTxDoneTrap": alaTestOamTxDoneTrap,
       "alaTestOamRxReadyTrap": alaTestOamRxReadyTrap,
       "alaTestOamTestAbortTrap": alaTestOamTestAbortTrap,
       "alaTestOamGroupTxDoneTrap": alaTestOamGroupTxDoneTrap,
       "alaTestOamGroupRxReadyTrap": alaTestOamGroupRxReadyTrap,
       "alaTestOamGroupAbortTrap": alaTestOamGroupAbortTrap,
       "alaTestOamStatsWriteDoneTrap": alaTestOamStatsWriteDoneTrap,
       "alaTestOamMIBObjects": alaTestOamMIBObjects,
       "alaTestOamClearStats": alaTestOamClearStats,
       "alaTestOamGlobalClearStats": alaTestOamGlobalClearStats,
       "alaTestOamStatus": alaTestOamStatus,
       "alaTestOamConfig": alaTestOamConfig,
       "alaTestOamConfigTable": alaTestOamConfigTable,
       "alaTestOamConfigEntry": alaTestOamConfigEntry,
       "alaTestOamConfigTestId": alaTestOamConfigTestId,
       "alaTestOamConfigSourceEndpoint": alaTestOamConfigSourceEndpoint,
       "alaTestOamConfigDestinationEndpoint": alaTestOamConfigDestinationEndpoint,
       "alaTestOamConfigTestDescription": alaTestOamConfigTestDescription,
       "alaTestOamConfigGeneratorTestMode": alaTestOamConfigGeneratorTestMode,
       "alaTestOamConfigAnalyzerTestMode": alaTestOamConfigAnalyzerTestMode,
       "alaTestOamConfigLoopbackTestMode": alaTestOamConfigLoopbackTestMode,
       "alaTestOamConfigDirection": alaTestOamConfigDirection,
       "alaTestOamConfigFrameSrcMacAddress": alaTestOamConfigFrameSrcMacAddress,
       "alaTestOamConfigFrameDstMacAddress": alaTestOamConfigFrameDstMacAddress,
       "alaTestOamConfigDuration": alaTestOamConfigDuration,
       "alaTestOamConfigVlan": alaTestOamConfigVlan,
       "alaTestOamConfigRole": alaTestOamConfigRole,
       "alaTestOamConfigPort": alaTestOamConfigPort,
       "alaTestOamConfigSourceLearningStatus": alaTestOamConfigSourceLearningStatus,
       "alaTestOamConfigGeneratorMode": alaTestOamConfigGeneratorMode,
       "alaTestOamConfigGeneratorBandwidth": alaTestOamConfigGeneratorBandwidth,
       "alaTestOamConfigGeneratorPacketSize": alaTestOamConfigGeneratorPacketSize,
       "alaTestOamConfigTestIdState": alaTestOamConfigTestIdState,
       "alaTestOamConfigTestIdStatus": alaTestOamConfigTestIdStatus,
       "alaTestOamConfigFrameType": alaTestOamConfigFrameType,
       "alaTestOamConfigRowStatus": alaTestOamConfigRowStatus,
       "alaTestOamConfigRemoteStatsFetchState": alaTestOamConfigRemoteStatsFetchState,
       "alaTestOamConfigRemoteSysMacAddress": alaTestOamConfigRemoteSysMacAddress,
       "alaTestOamEtherConfigTable": alaTestOamEtherConfigTable,
       "alaTestOamEtherConfigEntry": alaTestOamEtherConfigEntry,
       "alaTestOamEtherConfigVlan": alaTestOamEtherConfigVlan,
       "alaTestOamEtherConfig8021p": alaTestOamEtherConfig8021p,
       "alaTestOamEtherConfigDataPattern": alaTestOamEtherConfigDataPattern,
       "alaTestOamEtherConfigEtherType": alaTestOamEtherConfigEtherType,
       "alaTestOamEtherConfigCfi": alaTestOamEtherConfigCfi,
       "alaTestOamEtherConfigRowStatus": alaTestOamEtherConfigRowStatus,
       "alaTestOamIpv4ConfigTable": alaTestOamIpv4ConfigTable,
       "alaTestOamIpv4ConfigEntry": alaTestOamIpv4ConfigEntry,
       "alaTestOamIpv4ConfigVlan": alaTestOamIpv4ConfigVlan,
       "alaTestOamIpv4Config8021p": alaTestOamIpv4Config8021p,
       "alaTestOamIpv4ConfigDataPattern": alaTestOamIpv4ConfigDataPattern,
       "alaTestOamIpv4ConfigCfi": alaTestOamIpv4ConfigCfi,
       "alaTestOamIpv4ConfigSrcIpType": alaTestOamIpv4ConfigSrcIpType,
       "alaTestOamIpv4ConfigSrcIp": alaTestOamIpv4ConfigSrcIp,
       "alaTestOamIpv4ConfigDstIpType": alaTestOamIpv4ConfigDstIpType,
       "alaTestOamIpv4ConfigDstIp": alaTestOamIpv4ConfigDstIp,
       "alaTestOamIpv4ConfigSrcPort": alaTestOamIpv4ConfigSrcPort,
       "alaTestOamIpv4ConfigDstPort": alaTestOamIpv4ConfigDstPort,
       "alaTestOamIpv4ConfigNxtHeader": alaTestOamIpv4ConfigNxtHeader,
       "alaTestOamIpv4ConfigTtl": alaTestOamIpv4ConfigTtl,
       "alaTestOamIpv4ConfigTos": alaTestOamIpv4ConfigTos,
       "alaTestOamIpv4ConfigRowStatus": alaTestOamIpv4ConfigRowStatus,
       "alaTestOamIPConfigFlowLabel": alaTestOamIPConfigFlowLabel,
       "alaTestOamStats": alaTestOamStats,
       "alaTestOamStatsTable": alaTestOamStatsTable,
       "alaTestOamStatsEntry": alaTestOamStatsEntry,
       "alaTestOamStatsClearStats": alaTestOamStatsClearStats,
       "alaTestOamTxIngressCounter": alaTestOamTxIngressCounter,
       "alaTestOamTxEgressCounter": alaTestOamTxEgressCounter,
       "alaTestOamRxIngressCounter": alaTestOamRxIngressCounter,
       "alaTestOamRemoteStatsCounter": alaTestOamRemoteStatsCounter,
       "alaTestOamBandwidthThroughput": alaTestOamBandwidthThroughput,
       "alaTestOamBandwidthThroughputStr": alaTestOamBandwidthThroughputStr,
       "alaTestOamGroupClearStats": alaTestOamGroupClearStats,
       "alaTestOamGlobalGroupClearStats": alaTestOamGlobalGroupClearStats,
       "alaTestOamFeederPort": alaTestOamFeederPort,
       "alaTestOamGlobalFeederPort": alaTestOamGlobalFeederPort,
       "alaTestOamGroupConfig": alaTestOamGroupConfig,
       "alaTestOamGroupConfigTable": alaTestOamGroupConfigTable,
       "alaTestOamGroupConfigEntry": alaTestOamGroupConfigEntry,
       "alaTestOamConfigGroupId": alaTestOamConfigGroupId,
       "alaTestOamGroupConfigSourceEndpoint": alaTestOamGroupConfigSourceEndpoint,
       "alaTestOamGroupConfigDestinationEndpoint": alaTestOamGroupConfigDestinationEndpoint,
       "alaTestOamConfigGroupDescription": alaTestOamConfigGroupDescription,
       "alaTestOamGroupConfigDirection": alaTestOamGroupConfigDirection,
       "alaTestOamGroupConfigDuration": alaTestOamGroupConfigDuration,
       "alaTestOamGroupConfigRole": alaTestOamGroupConfigRole,
       "alaTestOamGroupConfigPort": alaTestOamGroupConfigPort,
       "alaTestOamGroupConfigGeneratorBandwidth": alaTestOamGroupConfigGeneratorBandwidth,
       "alaTestOamGroupConfigState": alaTestOamGroupConfigState,
       "alaTestOamGroupConfigStatus": alaTestOamGroupConfigStatus,
       "alaTestOamGroupConfigFlowCount": alaTestOamGroupConfigFlowCount,
       "alaTestOamGroupConfigStatsClear": alaTestOamGroupConfigStatsClear,
       "alaTestOamGroupConfigRowStatus": alaTestOamGroupConfigRowStatus,
       "alaTestOamGroupConfigRemoteStatsFetchState": alaTestOamGroupConfigRemoteStatsFetchState,
       "alaTestOamGroupConfigRemoteSysMacAddress": alaTestOamGroupConfigRemoteSysMacAddress,
       "alaTestOamGroupFlowConfig": alaTestOamGroupFlowConfig,
       "alaTestOamGroupFlowConfigTable": alaTestOamGroupFlowConfigTable,
       "alaTestOamGroupFlowConfigEntry": alaTestOamGroupFlowConfigEntry,
       "alaTestOamGroupFlowFrameSrcMacAddress": alaTestOamGroupFlowFrameSrcMacAddress,
       "alaTestOamGroupFlowFrameDstMacAddress": alaTestOamGroupFlowFrameDstMacAddress,
       "alaTestOamGroupFlowVlan": alaTestOamGroupFlowVlan,
       "alaTestOamGroupFlowGeneratorBandwidth": alaTestOamGroupFlowGeneratorBandwidth,
       "alaTestOamGroupFlowGeneratorPacketSize": alaTestOamGroupFlowGeneratorPacketSize,
       "alaTestOamGroupFlowConfigRowStatus": alaTestOamGroupFlowConfigRowStatus,
       "alaTestOamGroupFlowStats": alaTestOamGroupFlowStats,
       "alaTestOamGroupFlowStatsTable": alaTestOamGroupFlowStatsTable,
       "alaTestOamGroupFlowStatsEntry": alaTestOamGroupFlowStatsEntry,
       "alaTestOamGroupFlowTxIngressCounter": alaTestOamGroupFlowTxIngressCounter,
       "alaTestOamGroupFlowTxEgressCounter": alaTestOamGroupFlowTxEgressCounter,
       "alaTestOamGroupFlowRxIngressCounter": alaTestOamGroupFlowRxIngressCounter,
       "alaTestOamGroupFlowRemoteStatsCounter": alaTestOamGroupFlowRemoteStatsCounter,
       "alaTestOamGroupBandwidthThroughput": alaTestOamGroupBandwidthThroughput,
       "alaTestOamGroupBandwidthThroughputStr": alaTestOamGroupBandwidthThroughputStr,
       "alaTestOamSaaConfig": alaTestOamSaaConfig,
       "alaTestOamSaaConfigTable": alaTestOamSaaConfigTable,
       "alaTestOamSaaConfigEntry": alaTestOamSaaConfigEntry,
       "alaTestOamSaaConfigDropEligible": alaTestOamSaaConfigDropEligible,
       "alaTestOamSaaConfigPayloadSize": alaTestOamSaaConfigPayloadSize,
       "alaTestOamSaaConfigNumPkts": alaTestOamSaaConfigNumPkts,
       "alaTestOamSaaConfigInterPktDelay": alaTestOamSaaConfigInterPktDelay,
       "alaTestOamSaaConfigVlanPriority": alaTestOamSaaConfigVlanPriority,
       "alaTestOamSaaConfigRowStatus": alaTestOamSaaConfigRowStatus,
       "alaTestOamSaaContinuous": alaTestOamSaaContinuous,
       "alaTestOamSaaStats": alaTestOamSaaStats,
       "alaTestOamSaaStatsTable": alaTestOamSaaStatsTable,
       "alaTestOamSaaStatsEntry": alaTestOamSaaStatsEntry,
       "alaTestOamSaaPktsSent": alaTestOamSaaPktsSent,
       "alaTestOamSaaPktsRcvd": alaTestOamSaaPktsRcvd,
       "alaTestOamSaaRunTime": alaTestOamSaaRunTime,
       "alaTestOamSaaMinRTT": alaTestOamSaaMinRTT,
       "alaTestOamSaaAvgRTT": alaTestOamSaaAvgRTT,
       "alaTestOamSaaMaxRTT": alaTestOamSaaMaxRTT,
       "alaTestOamSaaMinJitter": alaTestOamSaaMinJitter,
       "alaTestOamSaaAvgJitter": alaTestOamSaaAvgJitter,
       "alaTestOamSaaMaxJitter": alaTestOamSaaMaxJitter,
       "alaTestOamGroupFlowSaaStats": alaTestOamGroupFlowSaaStats,
       "alaTestOamGroupFlowSaaStatsTable": alaTestOamGroupFlowSaaStatsTable,
       "alaTestOamGroupFlowSaaStatsEntry": alaTestOamGroupFlowSaaStatsEntry,
       "alaTestOamGroupFlowSaaPktsSent": alaTestOamGroupFlowSaaPktsSent,
       "alaTestOamGroupFlowSaaPktsRcvd": alaTestOamGroupFlowSaaPktsRcvd,
       "alaTestOamGroupFlowSaaRunTime": alaTestOamGroupFlowSaaRunTime,
       "alaTestOamGroupFlowSaaMinRTT": alaTestOamGroupFlowSaaMinRTT,
       "alaTestOamGroupFlowSaaAvgRTT": alaTestOamGroupFlowSaaAvgRTT,
       "alaTestOamGroupFlowSaaMaxRTT": alaTestOamGroupFlowSaaMaxRTT,
       "alaTestOamGroupFlowSaaMinJitter": alaTestOamGroupFlowSaaMinJitter,
       "alaTestOamGroupFlowSaaAvgJitter": alaTestOamGroupFlowSaaAvgJitter,
       "alaTestOamGroupFlowSaaMaxJitter": alaTestOamGroupFlowSaaMaxJitter,
       "alaTestOamStatsFlashSave": alaTestOamStatsFlashSave,
       "alaTestOamGlobalStatsFlashSave": alaTestOamGlobalStatsFlashSave,
       "alaTestOamTrapObj": alaTestOamTrapObj,
       "alaTestOamStatsWriteDoneTrapStr": alaTestOamStatsWriteDoneTrapStr,
       "alaTestOamConformance": alaTestOamConformance,
       "alaTestOamMIBCompliances": alaTestOamMIBCompliances,
       "alaTestOamCompliance": alaTestOamCompliance,
       "alaTestOamMIBGroups": alaTestOamMIBGroups,
       "alaTestOamGlobalClearStatsGroup": alaTestOamGlobalClearStatsGroup,
       "alaTestOamConfigGroup": alaTestOamConfigGroup,
       "alaTestOamStatsGroup": alaTestOamStatsGroup,
       "alaTestOamNotificationGroup": alaTestOamNotificationGroup,
       "alaTestOamGlobalGroupClearStatsGroup": alaTestOamGlobalGroupClearStatsGroup,
       "alaTestOamGlobalFeederPortGroup": alaTestOamGlobalFeederPortGroup,
       "alaTestOamGroupConfigGroup": alaTestOamGroupConfigGroup,
       "alaTestOamGroupFlowConfigGroup": alaTestOamGroupFlowConfigGroup,
       "alaTestOamGroupFlowStatsGroup": alaTestOamGroupFlowStatsGroup,
       "alaTestOamSaaStatsGroup": alaTestOamSaaStatsGroup,
       "alaTestOamGroupFlowSaaStatsGroup": alaTestOamGroupFlowSaaStatsGroup,
       "alaTestOamGlobalStatsFlashSaveGroup": alaTestOamGlobalStatsFlashSaveGroup}
)
