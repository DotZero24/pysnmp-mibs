# SNMP MIB module (NSCRTV-EPON-UNI-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/fscom/NSCRTV-EPON-UNI-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:13:18 2025
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

(AutoNegotiationTechAbility,
 EponAlarmCode,
 EponAlarmInstance,
 EponCardIndex,
 EponDeviceIndex,
 EponPortIndex,
 EponSeverityType,
 EponStats15MinRecordType,
 EponStats24HourRecordType,
 EponStatsThresholdType,
 TAddress,
 uniObjects) = mibBuilder.importSymbols(
    "NSCRTV-EPONEOC-EPON-MIB",
    "AutoNegotiationTechAbility",
    "EponAlarmCode",
    "EponAlarmInstance",
    "EponCardIndex",
    "EponDeviceIndex",
    "EponPortIndex",
    "EponSeverityType",
    "EponStats15MinRecordType",
    "EponStats24HourRecordType",
    "EponStatsThresholdType",
    "TAddress",
    "uniObjects")

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
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_UniAttributeTable_Object = MibTable
uniAttributeTable = _UniAttributeTable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 5, 1)
)
if mibBuilder.loadTexts:
    uniAttributeTable.setStatus("current")
_UniAttributeEntry_Object = MibTableRow
uniAttributeEntry = _UniAttributeEntry_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 5, 1, 1)
)
uniAttributeEntry.setIndexNames(
    (0, "NSCRTV-EPON-UNI-MIB", "uniAttributeDeviceIndex"),
    (0, "NSCRTV-EPON-UNI-MIB", "uniAttributeCardIndex"),
    (0, "NSCRTV-EPON-UNI-MIB", "uniAttributePortIndex"),
)
if mibBuilder.loadTexts:
    uniAttributeEntry.setStatus("current")
_UniAttributeDeviceIndex_Type = EponDeviceIndex
_UniAttributeDeviceIndex_Object = MibTableColumn
uniAttributeDeviceIndex = _UniAttributeDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 5, 1, 1, 1),
    _UniAttributeDeviceIndex_Type()
)
uniAttributeDeviceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    uniAttributeDeviceIndex.setStatus("current")
_UniAttributeCardIndex_Type = EponCardIndex
_UniAttributeCardIndex_Object = MibTableColumn
uniAttributeCardIndex = _UniAttributeCardIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 5, 1, 1, 2),
    _UniAttributeCardIndex_Type()
)
uniAttributeCardIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    uniAttributeCardIndex.setStatus("current")
_UniAttributePortIndex_Type = EponPortIndex
_UniAttributePortIndex_Object = MibTableColumn
uniAttributePortIndex = _UniAttributePortIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 5, 1, 1, 3),
    _UniAttributePortIndex_Type()
)
uniAttributePortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    uniAttributePortIndex.setStatus("current")


class _UniAdminStatus_Type(Integer32):
    """Custom type uniAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2),
          ("testing", 3))
    )


_UniAdminStatus_Type.__name__ = "Integer32"
_UniAdminStatus_Object = MibTableColumn
uniAdminStatus = _UniAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 5, 1, 1, 4),
    _UniAdminStatus_Type()
)
uniAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uniAdminStatus.setStatus("current")


class _UniOperationStatus_Type(Integer32):
    """Custom type uniOperationStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2),
          ("testing", 3))
    )


_UniOperationStatus_Type.__name__ = "Integer32"
_UniOperationStatus_Object = MibTableColumn
uniOperationStatus = _UniOperationStatus_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 5, 1, 1, 5),
    _UniOperationStatus_Type()
)
uniOperationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uniOperationStatus.setStatus("current")
_UniAutoNegotiationEnable_Type = TruthValue
_UniAutoNegotiationEnable_Object = MibTableColumn
uniAutoNegotiationEnable = _UniAutoNegotiationEnable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 5, 1, 1, 6),
    _UniAutoNegotiationEnable_Type()
)
uniAutoNegotiationEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uniAutoNegotiationEnable.setStatus("current")
_UniAutoNegotiationLocalTechAbility_Type = AutoNegotiationTechAbility
_UniAutoNegotiationLocalTechAbility_Object = MibTableColumn
uniAutoNegotiationLocalTechAbility = _UniAutoNegotiationLocalTechAbility_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 5, 1, 1, 7),
    _UniAutoNegotiationLocalTechAbility_Type()
)
uniAutoNegotiationLocalTechAbility.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uniAutoNegotiationLocalTechAbility.setStatus("current")


class _UniAutoNegotiationRestart_Type(Integer32):
    """Custom type uniAutoNegotiationRestart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("restart", 1)
    )


_UniAutoNegotiationRestart_Type.__name__ = "Integer32"
_UniAutoNegotiationRestart_Object = MibTableColumn
uniAutoNegotiationRestart = _UniAutoNegotiationRestart_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 5, 1, 1, 9),
    _UniAutoNegotiationRestart_Type()
)
uniAutoNegotiationRestart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uniAutoNegotiationRestart.setStatus("current")
_UniMacAddressManagement_ObjectIdentity = ObjectIdentity
uniMacAddressManagement = _UniMacAddressManagement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 5, 2)
)
if mibBuilder.loadTexts:
    uniMacAddressManagement.setStatus("current")
_UniMacAddressManagementNode_ObjectIdentity = ObjectIdentity
uniMacAddressManagementNode = _UniMacAddressManagementNode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 5, 2, 1)
)
if mibBuilder.loadTexts:
    uniMacAddressManagementNode.setStatus("current")
_UniMacAddrAgingTime_Type = Integer32
_UniMacAddrAgingTime_Object = MibScalar
uniMacAddrAgingTime = _UniMacAddrAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 5, 2, 1, 1),
    _UniMacAddrAgingTime_Type()
)
uniMacAddrAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uniMacAddrAgingTime.setStatus("current")
if mibBuilder.loadTexts:
    uniMacAddrAgingTime.setUnits("Seconds")


class _UniMacAddrClear_Type(Integer32):
    """Custom type uniMacAddrClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("allDynamic", 1)
    )


_UniMacAddrClear_Type.__name__ = "Integer32"
_UniMacAddrClear_Object = MibScalar
uniMacAddrClear = _UniMacAddrClear_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 5, 2, 1, 2),
    _UniMacAddrClear_Type()
)
uniMacAddrClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uniMacAddrClear.setStatus("current")
_UniMacAddressTable_Object = MibTable
uniMacAddressTable = _UniMacAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 5, 2, 2)
)
if mibBuilder.loadTexts:
    uniMacAddressTable.setStatus("current")
_UniMacAddressEntry_Object = MibTableRow
uniMacAddressEntry = _UniMacAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 5, 2, 2, 1)
)
uniMacAddressEntry.setIndexNames(
    (0, "NSCRTV-EPON-UNI-MIB", "uniMacAddrIndex"),
    (0, "NSCRTV-EPON-UNI-MIB", "uniMacAddrVlanIdIndex"),
)
if mibBuilder.loadTexts:
    uniMacAddressEntry.setStatus("current")
_UniMacAddrIndex_Type = MacAddress
_UniMacAddrIndex_Object = MibTableColumn
uniMacAddrIndex = _UniMacAddrIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 5, 2, 2, 1, 1),
    _UniMacAddrIndex_Type()
)
uniMacAddrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    uniMacAddrIndex.setStatus("current")
_UniMacAddrVlanIdIndex_Type = Integer32
_UniMacAddrVlanIdIndex_Object = MibTableColumn
uniMacAddrVlanIdIndex = _UniMacAddrVlanIdIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 5, 2, 2, 1, 2),
    _UniMacAddrVlanIdIndex_Type()
)
uniMacAddrVlanIdIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    uniMacAddrVlanIdIndex.setStatus("current")


class _UniMacAddrType_Type(Integer32):
    """Custom type uniMacAddrType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("static", 1),
          ("dynamic", 2),
          ("other", 3))
    )


_UniMacAddrType_Type.__name__ = "Integer32"
_UniMacAddrType_Object = MibTableColumn
uniMacAddrType = _UniMacAddrType_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 5, 2, 2, 1, 3),
    _UniMacAddrType_Type()
)
uniMacAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    uniMacAddrType.setStatus("current")


class _UniMacAddrPortId_Type(OctetString):
    """Custom type uniMacAddrPortId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )
    fixed_length = 2


_UniMacAddrPortId_Type.__name__ = "OctetString"
_UniMacAddrPortId_Object = MibTableColumn
uniMacAddrPortId = _UniMacAddrPortId_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 5, 2, 2, 1, 4),
    _UniMacAddrPortId_Type()
)
uniMacAddrPortId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    uniMacAddrPortId.setStatus("current")
_UniMacAddrRowStatus_Type = RowStatus
_UniMacAddrRowStatus_Object = MibTableColumn
uniMacAddrRowStatus = _UniMacAddrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 5, 2, 2, 1, 5),
    _UniMacAddrRowStatus_Type()
)
uniMacAddrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    uniMacAddrRowStatus.setStatus("current")
_UniTrunkManagement_ObjectIdentity = ObjectIdentity
uniTrunkManagement = _UniTrunkManagement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 5, 3)
)
if mibBuilder.loadTexts:
    uniTrunkManagement.setStatus("current")
_UniTrunkGroupConfigTable_Object = MibTable
uniTrunkGroupConfigTable = _UniTrunkGroupConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 5, 3, 1)
)
if mibBuilder.loadTexts:
    uniTrunkGroupConfigTable.setStatus("current")
_UniTrunkGroupConfigEntry_Object = MibTableRow
uniTrunkGroupConfigEntry = _UniTrunkGroupConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 5, 3, 1, 1)
)
uniTrunkGroupConfigEntry.setIndexNames(
    (0, "NSCRTV-EPON-UNI-MIB", "uniTrunkGroupConfigIndex"),
)
if mibBuilder.loadTexts:
    uniTrunkGroupConfigEntry.setStatus("current")
_UniTrunkGroupConfigIndex_Type = Integer32
_UniTrunkGroupConfigIndex_Object = MibTableColumn
uniTrunkGroupConfigIndex = _UniTrunkGroupConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 5, 3, 1, 1, 1),
    _UniTrunkGroupConfigIndex_Type()
)
uniTrunkGroupConfigIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    uniTrunkGroupConfigIndex.setStatus("current")
_UniTrunkGroupConfigName_Type = DisplayString
_UniTrunkGroupConfigName_Object = MibTableColumn
uniTrunkGroupConfigName = _UniTrunkGroupConfigName_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 5, 3, 1, 1, 2),
    _UniTrunkGroupConfigName_Type()
)
uniTrunkGroupConfigName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    uniTrunkGroupConfigName.setStatus("current")
_UniTrunkGroupConfigMember_Type = OctetString
_UniTrunkGroupConfigMember_Object = MibTableColumn
uniTrunkGroupConfigMember = _UniTrunkGroupConfigMember_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 5, 3, 1, 1, 3),
    _UniTrunkGroupConfigMember_Type()
)
uniTrunkGroupConfigMember.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    uniTrunkGroupConfigMember.setStatus("current")


class _UniTrunkGroupConfigPolicy_Type(Integer32):
    """Custom type uniTrunkGroupConfigPolicy based on Integer32"""
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
        *(("srcMac", 1),
          ("destMac", 2),
          ("srcMacNDestMac", 3),
          ("srcIp", 4),
          ("destIp", 5),
          ("srcIpNDestIp", 6))
    )


_UniTrunkGroupConfigPolicy_Type.__name__ = "Integer32"
_UniTrunkGroupConfigPolicy_Object = MibTableColumn
uniTrunkGroupConfigPolicy = _UniTrunkGroupConfigPolicy_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 5, 3, 1, 1, 4),
    _UniTrunkGroupConfigPolicy_Type()
)
uniTrunkGroupConfigPolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    uniTrunkGroupConfigPolicy.setStatus("current")
_UniTrunkGroupConfigRowstatus_Type = RowStatus
_UniTrunkGroupConfigRowstatus_Object = MibTableColumn
uniTrunkGroupConfigRowstatus = _UniTrunkGroupConfigRowstatus_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 5, 3, 1, 1, 5),
    _UniTrunkGroupConfigRowstatus_Type()
)
uniTrunkGroupConfigRowstatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    uniTrunkGroupConfigRowstatus.setStatus("current")
_UniTrunkGroupTable_Object = MibTable
uniTrunkGroupTable = _UniTrunkGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 5, 3, 2)
)
if mibBuilder.loadTexts:
    uniTrunkGroupTable.setStatus("current")
_UniTrunkGroupEntry_Object = MibTableRow
uniTrunkGroupEntry = _UniTrunkGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 5, 3, 2, 1)
)
uniTrunkGroupEntry.setIndexNames(
    (0, "NSCRTV-EPON-UNI-MIB", "uniTrunkGroupIndex"),
)
if mibBuilder.loadTexts:
    uniTrunkGroupEntry.setStatus("current")
_UniTrunkGroupIndex_Type = Integer32
_UniTrunkGroupIndex_Object = MibTableColumn
uniTrunkGroupIndex = _UniTrunkGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 5, 3, 2, 1, 1),
    _UniTrunkGroupIndex_Type()
)
uniTrunkGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    uniTrunkGroupIndex.setStatus("current")


class _UniTrunkGroupOperationStatus_Type(Integer32):
    """Custom type uniTrunkGroupOperationStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2),
          ("testing", 3))
    )


_UniTrunkGroupOperationStatus_Type.__name__ = "Integer32"
_UniTrunkGroupOperationStatus_Object = MibTableColumn
uniTrunkGroupOperationStatus = _UniTrunkGroupOperationStatus_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 5, 3, 2, 1, 2),
    _UniTrunkGroupOperationStatus_Type()
)
uniTrunkGroupOperationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uniTrunkGroupOperationStatus.setStatus("current")
_UniTrunkGroupActualSpeed_Type = Integer32
_UniTrunkGroupActualSpeed_Object = MibTableColumn
uniTrunkGroupActualSpeed = _UniTrunkGroupActualSpeed_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 5, 3, 2, 1, 3),
    _UniTrunkGroupActualSpeed_Type()
)
uniTrunkGroupActualSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uniTrunkGroupActualSpeed.setStatus("current")
if mibBuilder.loadTexts:
    uniTrunkGroupActualSpeed.setUnits("Mbps")


class _UniTrunkGroupAdminStatus_Type(Integer32):
    """Custom type uniTrunkGroupAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2),
          ("testing", 3))
    )


_UniTrunkGroupAdminStatus_Type.__name__ = "Integer32"
_UniTrunkGroupAdminStatus_Object = MibTableColumn
uniTrunkGroupAdminStatus = _UniTrunkGroupAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 5, 3, 2, 1, 4),
    _UniTrunkGroupAdminStatus_Type()
)
uniTrunkGroupAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uniTrunkGroupAdminStatus.setStatus("current")
_UniPortRateLimitTable_Object = MibTable
uniPortRateLimitTable = _UniPortRateLimitTable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 5, 4)
)
if mibBuilder.loadTexts:
    uniPortRateLimitTable.setStatus("current")
_UniPortRateLimitEntry_Object = MibTableRow
uniPortRateLimitEntry = _UniPortRateLimitEntry_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 5, 4, 1)
)
uniPortRateLimitEntry.setIndexNames(
    (0, "NSCRTV-EPON-UNI-MIB", "uniPortRateLimitDeviceIndex"),
    (0, "NSCRTV-EPON-UNI-MIB", "uniPortRateLimitCardIndex"),
    (0, "NSCRTV-EPON-UNI-MIB", "uniPortRateLimitPortIndex"),
)
if mibBuilder.loadTexts:
    uniPortRateLimitEntry.setStatus("current")
_UniPortRateLimitDeviceIndex_Type = EponDeviceIndex
_UniPortRateLimitDeviceIndex_Object = MibTableColumn
uniPortRateLimitDeviceIndex = _UniPortRateLimitDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 5, 4, 1, 1),
    _UniPortRateLimitDeviceIndex_Type()
)
uniPortRateLimitDeviceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    uniPortRateLimitDeviceIndex.setStatus("current")
_UniPortRateLimitCardIndex_Type = EponCardIndex
_UniPortRateLimitCardIndex_Object = MibTableColumn
uniPortRateLimitCardIndex = _UniPortRateLimitCardIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 5, 4, 1, 2),
    _UniPortRateLimitCardIndex_Type()
)
uniPortRateLimitCardIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    uniPortRateLimitCardIndex.setStatus("current")
_UniPortRateLimitPortIndex_Type = EponPortIndex
_UniPortRateLimitPortIndex_Object = MibTableColumn
uniPortRateLimitPortIndex = _UniPortRateLimitPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 5, 4, 1, 3),
    _UniPortRateLimitPortIndex_Type()
)
uniPortRateLimitPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    uniPortRateLimitPortIndex.setStatus("current")
_UniPortInCIR_Type = Integer32
_UniPortInCIR_Object = MibTableColumn
uniPortInCIR = _UniPortInCIR_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 5, 4, 1, 4),
    _UniPortInCIR_Type()
)
uniPortInCIR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uniPortInCIR.setStatus("current")
if mibBuilder.loadTexts:
    uniPortInCIR.setUnits("kbps")
_UniPortInCBS_Type = Integer32
_UniPortInCBS_Object = MibTableColumn
uniPortInCBS = _UniPortInCBS_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 5, 4, 1, 5),
    _UniPortInCBS_Type()
)
uniPortInCBS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uniPortInCBS.setStatus("current")
if mibBuilder.loadTexts:
    uniPortInCBS.setUnits("Kbytes")
_UniPortInEBS_Type = Integer32
_UniPortInEBS_Object = MibTableColumn
uniPortInEBS = _UniPortInEBS_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 5, 4, 1, 6),
    _UniPortInEBS_Type()
)
uniPortInEBS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uniPortInEBS.setStatus("current")
if mibBuilder.loadTexts:
    uniPortInEBS.setUnits("Kbytes")
_UniPortOutCIR_Type = Integer32
_UniPortOutCIR_Object = MibTableColumn
uniPortOutCIR = _UniPortOutCIR_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 5, 4, 1, 7),
    _UniPortOutCIR_Type()
)
uniPortOutCIR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uniPortOutCIR.setStatus("current")
if mibBuilder.loadTexts:
    uniPortOutCIR.setUnits("Kbps")
_UniPortOutPIR_Type = Integer32
_UniPortOutPIR_Object = MibTableColumn
uniPortOutPIR = _UniPortOutPIR_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 5, 4, 1, 8),
    _UniPortOutPIR_Type()
)
uniPortOutPIR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uniPortOutPIR.setStatus("current")
if mibBuilder.loadTexts:
    uniPortOutPIR.setUnits("Kbps")
_UniPortInRateLimitEnable_Type = TruthValue
_UniPortInRateLimitEnable_Object = MibTableColumn
uniPortInRateLimitEnable = _UniPortInRateLimitEnable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 5, 4, 1, 9),
    _UniPortInRateLimitEnable_Type()
)
uniPortInRateLimitEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uniPortInRateLimitEnable.setStatus("current")
_UniPortOutRateLimitEnable_Type = TruthValue
_UniPortOutRateLimitEnable_Object = MibTableColumn
uniPortOutRateLimitEnable = _UniPortOutRateLimitEnable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 5, 4, 1, 10),
    _UniPortOutRateLimitEnable_Type()
)
uniPortOutRateLimitEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uniPortOutRateLimitEnable.setStatus("current")
_UniMirrorTable_Object = MibTable
uniMirrorTable = _UniMirrorTable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 5, 5)
)
if mibBuilder.loadTexts:
    uniMirrorTable.setStatus("current")
_UniMirrorEntry_Object = MibTableRow
uniMirrorEntry = _UniMirrorEntry_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 5, 5, 1)
)
uniMirrorEntry.setIndexNames(
    (0, "NSCRTV-EPON-UNI-MIB", "uniMirrorGroupIndex"),
)
if mibBuilder.loadTexts:
    uniMirrorEntry.setStatus("current")
_UniMirrorGroupIndex_Type = Integer32
_UniMirrorGroupIndex_Object = MibTableColumn
uniMirrorGroupIndex = _UniMirrorGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 5, 5, 1, 1),
    _UniMirrorGroupIndex_Type()
)
uniMirrorGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    uniMirrorGroupIndex.setStatus("current")
_UniMirrorGroupName_Type = DisplayString
_UniMirrorGroupName_Object = MibTableColumn
uniMirrorGroupName = _UniMirrorGroupName_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 5, 5, 1, 2),
    _UniMirrorGroupName_Type()
)
uniMirrorGroupName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    uniMirrorGroupName.setStatus("current")
_UniMirrorGroupDstPortList_Type = OctetString
_UniMirrorGroupDstPortList_Object = MibTableColumn
uniMirrorGroupDstPortList = _UniMirrorGroupDstPortList_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 5, 5, 1, 3),
    _UniMirrorGroupDstPortList_Type()
)
uniMirrorGroupDstPortList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    uniMirrorGroupDstPortList.setStatus("current")
_UniMirrorGroupSrcInPortList_Type = OctetString
_UniMirrorGroupSrcInPortList_Object = MibTableColumn
uniMirrorGroupSrcInPortList = _UniMirrorGroupSrcInPortList_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 5, 5, 1, 4),
    _UniMirrorGroupSrcInPortList_Type()
)
uniMirrorGroupSrcInPortList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    uniMirrorGroupSrcInPortList.setStatus("current")
_UniMirrorGroupSrcOutPortList_Type = OctetString
_UniMirrorGroupSrcOutPortList_Object = MibTableColumn
uniMirrorGroupSrcOutPortList = _UniMirrorGroupSrcOutPortList_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 5, 5, 1, 5),
    _UniMirrorGroupSrcOutPortList_Type()
)
uniMirrorGroupSrcOutPortList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    uniMirrorGroupSrcOutPortList.setStatus("current")
_UniMirrorGroupRowstatus_Type = RowStatus
_UniMirrorGroupRowstatus_Object = MibTableColumn
uniMirrorGroupRowstatus = _UniMirrorGroupRowstatus_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 5, 5, 1, 6),
    _UniMirrorGroupRowstatus_Type()
)
uniMirrorGroupRowstatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    uniMirrorGroupRowstatus.setStatus("current")
_UniBroadcastStormSuppressionTable_Object = MibTable
uniBroadcastStormSuppressionTable = _UniBroadcastStormSuppressionTable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 5, 6)
)
if mibBuilder.loadTexts:
    uniBroadcastStormSuppressionTable.setStatus("current")
_UniBroadcastStormSuppressionEntry_Object = MibTableRow
uniBroadcastStormSuppressionEntry = _UniBroadcastStormSuppressionEntry_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 5, 6, 1)
)
uniBroadcastStormSuppressionEntry.setIndexNames(
    (0, "NSCRTV-EPON-UNI-MIB", "uniBroadcastStormSuppressionCardIndex"),
    (0, "NSCRTV-EPON-UNI-MIB", "uniBroadcastStormSuppressionPortIndex"),
)
if mibBuilder.loadTexts:
    uniBroadcastStormSuppressionEntry.setStatus("current")
_UniBroadcastStormSuppressionCardIndex_Type = EponCardIndex
_UniBroadcastStormSuppressionCardIndex_Object = MibTableColumn
uniBroadcastStormSuppressionCardIndex = _UniBroadcastStormSuppressionCardIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 5, 6, 1, 1),
    _UniBroadcastStormSuppressionCardIndex_Type()
)
uniBroadcastStormSuppressionCardIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    uniBroadcastStormSuppressionCardIndex.setStatus("current")
_UniBroadcastStormSuppressionPortIndex_Type = EponPortIndex
_UniBroadcastStormSuppressionPortIndex_Object = MibTableColumn
uniBroadcastStormSuppressionPortIndex = _UniBroadcastStormSuppressionPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 5, 6, 1, 2),
    _UniBroadcastStormSuppressionPortIndex_Type()
)
uniBroadcastStormSuppressionPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    uniBroadcastStormSuppressionPortIndex.setStatus("current")
_UniUnicastStormEnable_Type = TruthValue
_UniUnicastStormEnable_Object = MibTableColumn
uniUnicastStormEnable = _UniUnicastStormEnable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 5, 6, 1, 3),
    _UniUnicastStormEnable_Type()
)
uniUnicastStormEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uniUnicastStormEnable.setStatus("current")
_UniUnicastStormInPacketRate_Type = Integer32
_UniUnicastStormInPacketRate_Object = MibTableColumn
uniUnicastStormInPacketRate = _UniUnicastStormInPacketRate_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 5, 6, 1, 4),
    _UniUnicastStormInPacketRate_Type()
)
uniUnicastStormInPacketRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uniUnicastStormInPacketRate.setStatus("current")
if mibBuilder.loadTexts:
    uniUnicastStormInPacketRate.setUnits("pps")
_UniUnicastStormOutPacketRate_Type = Integer32
_UniUnicastStormOutPacketRate_Object = MibTableColumn
uniUnicastStormOutPacketRate = _UniUnicastStormOutPacketRate_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 5, 6, 1, 5),
    _UniUnicastStormOutPacketRate_Type()
)
uniUnicastStormOutPacketRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uniUnicastStormOutPacketRate.setStatus("current")
if mibBuilder.loadTexts:
    uniUnicastStormOutPacketRate.setUnits("pps")
_UniMulticastStormEnable_Type = TruthValue
_UniMulticastStormEnable_Object = MibTableColumn
uniMulticastStormEnable = _UniMulticastStormEnable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 5, 6, 1, 6),
    _UniMulticastStormEnable_Type()
)
uniMulticastStormEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uniMulticastStormEnable.setStatus("current")
_UniMulticastStormInPacketRate_Type = Integer32
_UniMulticastStormInPacketRate_Object = MibTableColumn
uniMulticastStormInPacketRate = _UniMulticastStormInPacketRate_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 5, 6, 1, 7),
    _UniMulticastStormInPacketRate_Type()
)
uniMulticastStormInPacketRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uniMulticastStormInPacketRate.setStatus("current")
if mibBuilder.loadTexts:
    uniMulticastStormInPacketRate.setUnits("pps")
_UniMulticastStormOutPacketRate_Type = Integer32
_UniMulticastStormOutPacketRate_Object = MibTableColumn
uniMulticastStormOutPacketRate = _UniMulticastStormOutPacketRate_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 5, 6, 1, 8),
    _UniMulticastStormOutPacketRate_Type()
)
uniMulticastStormOutPacketRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uniMulticastStormOutPacketRate.setStatus("current")
if mibBuilder.loadTexts:
    uniMulticastStormOutPacketRate.setUnits("pps")
_UniBroadcastStormEnable_Type = TruthValue
_UniBroadcastStormEnable_Object = MibTableColumn
uniBroadcastStormEnable = _UniBroadcastStormEnable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 5, 6, 1, 9),
    _UniBroadcastStormEnable_Type()
)
uniBroadcastStormEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uniBroadcastStormEnable.setStatus("current")
_UniBroadcastStormInPacketRate_Type = Integer32
_UniBroadcastStormInPacketRate_Object = MibTableColumn
uniBroadcastStormInPacketRate = _UniBroadcastStormInPacketRate_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 5, 6, 1, 10),
    _UniBroadcastStormInPacketRate_Type()
)
uniBroadcastStormInPacketRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uniBroadcastStormInPacketRate.setStatus("current")
if mibBuilder.loadTexts:
    uniBroadcastStormInPacketRate.setUnits("pps")
_UniBroadcastStormOutPacketRate_Type = Integer32
_UniBroadcastStormOutPacketRate_Object = MibTableColumn
uniBroadcastStormOutPacketRate = _UniBroadcastStormOutPacketRate_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 5, 6, 1, 11),
    _UniBroadcastStormOutPacketRate_Type()
)
uniBroadcastStormOutPacketRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uniBroadcastStormOutPacketRate.setStatus("current")
if mibBuilder.loadTexts:
    uniBroadcastStormOutPacketRate.setUnits("pps")
_UniExtAttributeTable_Object = MibTable
uniExtAttributeTable = _UniExtAttributeTable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 5, 7)
)
if mibBuilder.loadTexts:
    uniExtAttributeTable.setStatus("current")
_UniExtAttributeEntry_Object = MibTableRow
uniExtAttributeEntry = _UniExtAttributeEntry_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 5, 7, 1)
)
uniExtAttributeEntry.setIndexNames(
    (0, "NSCRTV-EPON-UNI-MIB", "uniExtAttributeCardIndex"),
    (0, "NSCRTV-EPON-UNI-MIB", "uniExtAttributePortIndex"),
)
if mibBuilder.loadTexts:
    uniExtAttributeEntry.setStatus("current")
_UniExtAttributeCardIndex_Type = EponCardIndex
_UniExtAttributeCardIndex_Object = MibTableColumn
uniExtAttributeCardIndex = _UniExtAttributeCardIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 5, 7, 1, 1),
    _UniExtAttributeCardIndex_Type()
)
uniExtAttributeCardIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    uniExtAttributeCardIndex.setStatus("current")
_UniExtAttributePortIndex_Type = EponPortIndex
_UniExtAttributePortIndex_Object = MibTableColumn
uniExtAttributePortIndex = _UniExtAttributePortIndex_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 5, 7, 1, 2),
    _UniExtAttributePortIndex_Type()
)
uniExtAttributePortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    uniExtAttributePortIndex.setStatus("current")
_UniPerfStats15minuteEnable_Type = TruthValue
_UniPerfStats15minuteEnable_Object = MibTableColumn
uniPerfStats15minuteEnable = _UniPerfStats15minuteEnable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 5, 7, 1, 3),
    _UniPerfStats15minuteEnable_Type()
)
uniPerfStats15minuteEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uniPerfStats15minuteEnable.setStatus("current")
_UniPerfStats24hourEnable_Type = TruthValue
_UniPerfStats24hourEnable_Object = MibTableColumn
uniPerfStats24hourEnable = _UniPerfStats24hourEnable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 5, 7, 1, 4),
    _UniPerfStats24hourEnable_Type()
)
uniPerfStats24hourEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uniPerfStats24hourEnable.setStatus("current")
_UniLastChangeTime_Type = TimeTicks
_UniLastChangeTime_Object = MibTableColumn
uniLastChangeTime = _UniLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 5, 7, 1, 5),
    _UniLastChangeTime_Type()
)
uniLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uniLastChangeTime.setStatus("current")
_UniIsolationEnable_Type = TruthValue
_UniIsolationEnable_Object = MibTableColumn
uniIsolationEnable = _UniIsolationEnable_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 5, 7, 1, 6),
    _UniIsolationEnable_Type()
)
uniIsolationEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uniIsolationEnable.setStatus("current")
_UniMacAddrLearnMaxNum_Type = Integer32
_UniMacAddrLearnMaxNum_Object = MibTableColumn
uniMacAddrLearnMaxNum = _UniMacAddrLearnMaxNum_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 5, 7, 1, 7),
    _UniMacAddrLearnMaxNum_Type()
)
uniMacAddrLearnMaxNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uniMacAddrLearnMaxNum.setStatus("current")
_UniAutoNegotiationAdvertisedTechAbility_Type = AutoNegotiationTechAbility
_UniAutoNegotiationAdvertisedTechAbility_Object = MibTableColumn
uniAutoNegotiationAdvertisedTechAbility = _UniAutoNegotiationAdvertisedTechAbility_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 5, 7, 1, 8),
    _UniAutoNegotiationAdvertisedTechAbility_Type()
)
uniAutoNegotiationAdvertisedTechAbility.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uniAutoNegotiationAdvertisedTechAbility.setStatus("current")


class _UniMacAddrClearByPort_Type(Integer32):
    """Custom type uniMacAddrClearByPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("clearDynamic", 1)
    )


_UniMacAddrClearByPort_Type.__name__ = "Integer32"
_UniMacAddrClearByPort_Object = MibTableColumn
uniMacAddrClearByPort = _UniMacAddrClearByPort_Object(
    (1, 3, 6, 1, 4, 1, 17409, 2, 3, 5, 7, 1, 9),
    _UniMacAddrClearByPort_Type()
)
uniMacAddrClearByPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uniMacAddrClearByPort.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NSCRTV-EPON-UNI-MIB",
    **{"uniAttributeTable": uniAttributeTable,
       "uniAttributeEntry": uniAttributeEntry,
       "uniAttributeDeviceIndex": uniAttributeDeviceIndex,
       "uniAttributeCardIndex": uniAttributeCardIndex,
       "uniAttributePortIndex": uniAttributePortIndex,
       "uniAdminStatus": uniAdminStatus,
       "uniOperationStatus": uniOperationStatus,
       "uniAutoNegotiationEnable": uniAutoNegotiationEnable,
       "uniAutoNegotiationLocalTechAbility": uniAutoNegotiationLocalTechAbility,
       "uniAutoNegotiationRestart": uniAutoNegotiationRestart,
       "uniMacAddressManagement": uniMacAddressManagement,
       "uniMacAddressManagementNode": uniMacAddressManagementNode,
       "uniMacAddrAgingTime": uniMacAddrAgingTime,
       "uniMacAddrClear": uniMacAddrClear,
       "uniMacAddressTable": uniMacAddressTable,
       "uniMacAddressEntry": uniMacAddressEntry,
       "uniMacAddrIndex": uniMacAddrIndex,
       "uniMacAddrVlanIdIndex": uniMacAddrVlanIdIndex,
       "uniMacAddrType": uniMacAddrType,
       "uniMacAddrPortId": uniMacAddrPortId,
       "uniMacAddrRowStatus": uniMacAddrRowStatus,
       "uniTrunkManagement": uniTrunkManagement,
       "uniTrunkGroupConfigTable": uniTrunkGroupConfigTable,
       "uniTrunkGroupConfigEntry": uniTrunkGroupConfigEntry,
       "uniTrunkGroupConfigIndex": uniTrunkGroupConfigIndex,
       "uniTrunkGroupConfigName": uniTrunkGroupConfigName,
       "uniTrunkGroupConfigMember": uniTrunkGroupConfigMember,
       "uniTrunkGroupConfigPolicy": uniTrunkGroupConfigPolicy,
       "uniTrunkGroupConfigRowstatus": uniTrunkGroupConfigRowstatus,
       "uniTrunkGroupTable": uniTrunkGroupTable,
       "uniTrunkGroupEntry": uniTrunkGroupEntry,
       "uniTrunkGroupIndex": uniTrunkGroupIndex,
       "uniTrunkGroupOperationStatus": uniTrunkGroupOperationStatus,
       "uniTrunkGroupActualSpeed": uniTrunkGroupActualSpeed,
       "uniTrunkGroupAdminStatus": uniTrunkGroupAdminStatus,
       "uniPortRateLimitTable": uniPortRateLimitTable,
       "uniPortRateLimitEntry": uniPortRateLimitEntry,
       "uniPortRateLimitDeviceIndex": uniPortRateLimitDeviceIndex,
       "uniPortRateLimitCardIndex": uniPortRateLimitCardIndex,
       "uniPortRateLimitPortIndex": uniPortRateLimitPortIndex,
       "uniPortInCIR": uniPortInCIR,
       "uniPortInCBS": uniPortInCBS,
       "uniPortInEBS": uniPortInEBS,
       "uniPortOutCIR": uniPortOutCIR,
       "uniPortOutPIR": uniPortOutPIR,
       "uniPortInRateLimitEnable": uniPortInRateLimitEnable,
       "uniPortOutRateLimitEnable": uniPortOutRateLimitEnable,
       "uniMirrorTable": uniMirrorTable,
       "uniMirrorEntry": uniMirrorEntry,
       "uniMirrorGroupIndex": uniMirrorGroupIndex,
       "uniMirrorGroupName": uniMirrorGroupName,
       "uniMirrorGroupDstPortList": uniMirrorGroupDstPortList,
       "uniMirrorGroupSrcInPortList": uniMirrorGroupSrcInPortList,
       "uniMirrorGroupSrcOutPortList": uniMirrorGroupSrcOutPortList,
       "uniMirrorGroupRowstatus": uniMirrorGroupRowstatus,
       "uniBroadcastStormSuppressionTable": uniBroadcastStormSuppressionTable,
       "uniBroadcastStormSuppressionEntry": uniBroadcastStormSuppressionEntry,
       "uniBroadcastStormSuppressionCardIndex": uniBroadcastStormSuppressionCardIndex,
       "uniBroadcastStormSuppressionPortIndex": uniBroadcastStormSuppressionPortIndex,
       "uniUnicastStormEnable": uniUnicastStormEnable,
       "uniUnicastStormInPacketRate": uniUnicastStormInPacketRate,
       "uniUnicastStormOutPacketRate": uniUnicastStormOutPacketRate,
       "uniMulticastStormEnable": uniMulticastStormEnable,
       "uniMulticastStormInPacketRate": uniMulticastStormInPacketRate,
       "uniMulticastStormOutPacketRate": uniMulticastStormOutPacketRate,
       "uniBroadcastStormEnable": uniBroadcastStormEnable,
       "uniBroadcastStormInPacketRate": uniBroadcastStormInPacketRate,
       "uniBroadcastStormOutPacketRate": uniBroadcastStormOutPacketRate,
       "uniExtAttributeTable": uniExtAttributeTable,
       "uniExtAttributeEntry": uniExtAttributeEntry,
       "uniExtAttributeCardIndex": uniExtAttributeCardIndex,
       "uniExtAttributePortIndex": uniExtAttributePortIndex,
       "uniPerfStats15minuteEnable": uniPerfStats15minuteEnable,
       "uniPerfStats24hourEnable": uniPerfStats24hourEnable,
       "uniLastChangeTime": uniLastChangeTime,
       "uniIsolationEnable": uniIsolationEnable,
       "uniMacAddrLearnMaxNum": uniMacAddrLearnMaxNum,
       "uniAutoNegotiationAdvertisedTechAbility": uniAutoNegotiationAdvertisedTechAbility,
       "uniMacAddrClearByPort": uniMacAddrClearByPort}
)
