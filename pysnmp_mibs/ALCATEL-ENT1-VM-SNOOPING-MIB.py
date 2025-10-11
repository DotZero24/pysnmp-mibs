# SNMP MIB module (ALCATEL-ENT1-VM-SNOOPING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/alcatel-ent1/ALCATEL-ENT1-VM-SNOOPING-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:09:48 2025
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

(softentIND1VMSnooping,) = mibBuilder.importSymbols(
    "ALCATEL-ENT1-BASE",
    "softentIND1VMSnooping")

(physicalIndex,) = mibBuilder.importSymbols(
    "ALCATEL-ENT1-CHASSIS-MIB",
    "physicalIndex")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

alaVMSnoopingMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 84, 1)
)
if mibBuilder.loadTexts:
    alaVMSnoopingMIB.setRevisions(
        ("2014-07-01 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AlaVMSnoopingMIBNotifications_ObjectIdentity = ObjectIdentity
alaVMSnoopingMIBNotifications = _AlaVMSnoopingMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 84, 1, 0)
)
_AlaVMSnoopingMIBObjects_ObjectIdentity = ObjectIdentity
alaVMSnoopingMIBObjects = _AlaVMSnoopingMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 84, 1, 1)
)
if mibBuilder.loadTexts:
    alaVMSnoopingMIBObjects.setStatus("current")
_AlaVMSnoopingTrapsObj_ObjectIdentity = ObjectIdentity
alaVMSnoopingTrapsObj = _AlaVMSnoopingTrapsObj_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 84, 1, 1, 1)
)
_AlaVMSnoopingLearnedMacAddress_Type = MacAddress
_AlaVMSnoopingLearnedMacAddress_Object = MibScalar
alaVMSnoopingLearnedMacAddress = _AlaVMSnoopingLearnedMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 84, 1, 1, 1, 1),
    _AlaVMSnoopingLearnedMacAddress_Type()
)
alaVMSnoopingLearnedMacAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alaVMSnoopingLearnedMacAddress.setStatus("current")
_AlaVMSnoopingLearnedVxlanUdpPort_Type = Integer32
_AlaVMSnoopingLearnedVxlanUdpPort_Object = MibScalar
alaVMSnoopingLearnedVxlanUdpPort = _AlaVMSnoopingLearnedVxlanUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 84, 1, 1, 1, 2),
    _AlaVMSnoopingLearnedVxlanUdpPort_Type()
)
alaVMSnoopingLearnedVxlanUdpPort.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alaVMSnoopingLearnedVxlanUdpPort.setStatus("current")
_AlaVMSnoopingLearnedVxlanVni_Type = Integer32
_AlaVMSnoopingLearnedVxlanVni_Object = MibScalar
alaVMSnoopingLearnedVxlanVni = _AlaVMSnoopingLearnedVxlanVni_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 84, 1, 1, 1, 3),
    _AlaVMSnoopingLearnedVxlanVni_Type()
)
alaVMSnoopingLearnedVxlanVni.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alaVMSnoopingLearnedVxlanVni.setStatus("current")
_AlaVMSnoopingNiSlot_Type = Integer32
_AlaVMSnoopingNiSlot_Object = MibScalar
alaVMSnoopingNiSlot = _AlaVMSnoopingNiSlot_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 84, 1, 1, 1, 4),
    _AlaVMSnoopingNiSlot_Type()
)
alaVMSnoopingNiSlot.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alaVMSnoopingNiSlot.setStatus("current")
_AlaVMSnoopingHwResourceTotal_Type = Integer32
_AlaVMSnoopingHwResourceTotal_Object = MibScalar
alaVMSnoopingHwResourceTotal = _AlaVMSnoopingHwResourceTotal_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 84, 1, 1, 1, 5),
    _AlaVMSnoopingHwResourceTotal_Type()
)
alaVMSnoopingHwResourceTotal.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alaVMSnoopingHwResourceTotal.setStatus("current")
_AlaVMSnoopingHwResourceUsed_Type = Integer32
_AlaVMSnoopingHwResourceUsed_Object = MibScalar
alaVMSnoopingHwResourceUsed = _AlaVMSnoopingHwResourceUsed_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 84, 1, 1, 1, 6),
    _AlaVMSnoopingHwResourceUsed_Type()
)
alaVMSnoopingHwResourceUsed.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alaVMSnoopingHwResourceUsed.setStatus("current")
_AlaVMSnoopingChassisId_Type = Integer32
_AlaVMSnoopingChassisId_Object = MibScalar
alaVMSnoopingChassisId = _AlaVMSnoopingChassisId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 84, 1, 1, 1, 7),
    _AlaVMSnoopingChassisId_Type()
)
alaVMSnoopingChassisId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alaVMSnoopingChassisId.setStatus("current")
_AlaVMSnoopingConfig_ObjectIdentity = ObjectIdentity
alaVMSnoopingConfig = _AlaVMSnoopingConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 84, 1, 1, 2)
)


class _AlaVMSnoopingAdminStatus_Type(Integer32):
    """Custom type alaVMSnoopingAdminStatus based on Integer32"""
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


_AlaVMSnoopingAdminStatus_Type.__name__ = "Integer32"
_AlaVMSnoopingAdminStatus_Object = MibScalar
alaVMSnoopingAdminStatus = _AlaVMSnoopingAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 84, 1, 1, 2, 1),
    _AlaVMSnoopingAdminStatus_Type()
)
alaVMSnoopingAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaVMSnoopingAdminStatus.setStatus("current")


class _AlaVMSnoopingPolicyMode_Type(Integer32):
    """Custom type alaVMSnoopingPolicyMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("basic", 1),
          ("advance", 2))
    )


_AlaVMSnoopingPolicyMode_Type.__name__ = "Integer32"
_AlaVMSnoopingPolicyMode_Object = MibScalar
alaVMSnoopingPolicyMode = _AlaVMSnoopingPolicyMode_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 84, 1, 1, 2, 2),
    _AlaVMSnoopingPolicyMode_Type()
)
alaVMSnoopingPolicyMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaVMSnoopingPolicyMode.setStatus("current")


class _AlaVMSnoopingPolicyResource_Type(Integer32):
    """Custom type alaVMSnoopingPolicyResource based on Integer32"""
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
          ("extended", 2))
    )


_AlaVMSnoopingPolicyResource_Type.__name__ = "Integer32"
_AlaVMSnoopingPolicyResource_Object = MibScalar
alaVMSnoopingPolicyResource = _AlaVMSnoopingPolicyResource_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 84, 1, 1, 2, 3),
    _AlaVMSnoopingPolicyResource_Type()
)
alaVMSnoopingPolicyResource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaVMSnoopingPolicyResource.setStatus("current")


class _AlaVMSnoopingVMTrafficTagged_Type(Integer32):
    """Custom type alaVMSnoopingVMTrafficTagged based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("tagged", 1),
          ("untagged", 2),
          ("both", 3))
    )


_AlaVMSnoopingVMTrafficTagged_Type.__name__ = "Integer32"
_AlaVMSnoopingVMTrafficTagged_Object = MibScalar
alaVMSnoopingVMTrafficTagged = _AlaVMSnoopingVMTrafficTagged_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 84, 1, 1, 2, 4),
    _AlaVMSnoopingVMTrafficTagged_Type()
)
alaVMSnoopingVMTrafficTagged.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaVMSnoopingVMTrafficTagged.setStatus("current")


class _AlaVMSnoopingTrapStatus_Type(Integer32):
    """Custom type alaVMSnoopingTrapStatus based on Integer32"""
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


_AlaVMSnoopingTrapStatus_Type.__name__ = "Integer32"
_AlaVMSnoopingTrapStatus_Object = MibScalar
alaVMSnoopingTrapStatus = _AlaVMSnoopingTrapStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 84, 1, 1, 2, 5),
    _AlaVMSnoopingTrapStatus_Type()
)
alaVMSnoopingTrapStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaVMSnoopingTrapStatus.setStatus("current")


class _AlaVMSnoopingSamplingRate_Type(Unsigned32):
    """Custom type alaVMSnoopingSamplingRate based on Unsigned32"""
    defaultValue = 1000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967296),
    )


_AlaVMSnoopingSamplingRate_Type.__name__ = "Unsigned32"
_AlaVMSnoopingSamplingRate_Object = MibScalar
alaVMSnoopingSamplingRate = _AlaVMSnoopingSamplingRate_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 84, 1, 1, 2, 6),
    _AlaVMSnoopingSamplingRate_Type()
)
alaVMSnoopingSamplingRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaVMSnoopingSamplingRate.setStatus("current")


class _AlaVMSnoopingAgingTimer_Type(Integer32):
    """Custom type alaVMSnoopingAgingTimer based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_AlaVMSnoopingAgingTimer_Type.__name__ = "Integer32"
_AlaVMSnoopingAgingTimer_Object = MibScalar
alaVMSnoopingAgingTimer = _AlaVMSnoopingAgingTimer_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 84, 1, 1, 2, 7),
    _AlaVMSnoopingAgingTimer_Type()
)
alaVMSnoopingAgingTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaVMSnoopingAgingTimer.setStatus("current")


class _AlaVMSnoopingFilteringResourceTrapThreshold_Type(Integer32):
    """Custom type alaVMSnoopingFilteringResourceTrapThreshold based on Integer32"""
    defaultValue = 80

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_AlaVMSnoopingFilteringResourceTrapThreshold_Type.__name__ = "Integer32"
_AlaVMSnoopingFilteringResourceTrapThreshold_Object = MibScalar
alaVMSnoopingFilteringResourceTrapThreshold = _AlaVMSnoopingFilteringResourceTrapThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 84, 1, 1, 2, 8),
    _AlaVMSnoopingFilteringResourceTrapThreshold_Type()
)
alaVMSnoopingFilteringResourceTrapThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaVMSnoopingFilteringResourceTrapThreshold.setStatus("current")


class _AlaVMSnoopingClearAllData_Type(Integer32):
    """Custom type alaVMSnoopingClearAllData based on Integer32"""
    defaultValue = 4

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
        *(("globalStats", 1),
          ("hardwareStats", 2),
          ("database", 3),
          ("none", 4))
    )


_AlaVMSnoopingClearAllData_Type.__name__ = "Integer32"
_AlaVMSnoopingClearAllData_Object = MibScalar
alaVMSnoopingClearAllData = _AlaVMSnoopingClearAllData_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 84, 1, 1, 2, 9),
    _AlaVMSnoopingClearAllData_Type()
)
alaVMSnoopingClearAllData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaVMSnoopingClearAllData.setStatus("current")


class _AlaVMSnoopingLoggingThresholdFlows_Type(Integer32):
    """Custom type alaVMSnoopingLoggingThresholdFlows based on Integer32"""
    defaultValue = 5000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1000, 600000),
    )


_AlaVMSnoopingLoggingThresholdFlows_Type.__name__ = "Integer32"
_AlaVMSnoopingLoggingThresholdFlows_Object = MibScalar
alaVMSnoopingLoggingThresholdFlows = _AlaVMSnoopingLoggingThresholdFlows_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 84, 1, 1, 2, 10),
    _AlaVMSnoopingLoggingThresholdFlows_Type()
)
alaVMSnoopingLoggingThresholdFlows.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaVMSnoopingLoggingThresholdFlows.setStatus("current")


class _AlaVMSnoopingQosAllocationStatus_Type(Integer32):
    """Custom type alaVMSnoopingQosAllocationStatus based on Integer32"""
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
        *(("none", 1),
          ("inProgress", 2),
          ("success", 3),
          ("failed", 4))
    )


_AlaVMSnoopingQosAllocationStatus_Type.__name__ = "Integer32"
_AlaVMSnoopingQosAllocationStatus_Object = MibScalar
alaVMSnoopingQosAllocationStatus = _AlaVMSnoopingQosAllocationStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 84, 1, 1, 2, 11),
    _AlaVMSnoopingQosAllocationStatus_Type()
)
alaVMSnoopingQosAllocationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaVMSnoopingQosAllocationStatus.setStatus("current")
_AlaVMSnoopingUdpPortTable_Object = MibTable
alaVMSnoopingUdpPortTable = _AlaVMSnoopingUdpPortTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 84, 1, 1, 3)
)
if mibBuilder.loadTexts:
    alaVMSnoopingUdpPortTable.setStatus("current")
_AlaVMSnoopingUdpPortEntry_Object = MibTableRow
alaVMSnoopingUdpPortEntry = _AlaVMSnoopingUdpPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 84, 1, 1, 3, 1)
)
alaVMSnoopingUdpPortEntry.setIndexNames(
    (0, "ALCATEL-ENT1-VM-SNOOPING-MIB", "alaVMSnoopingUdpPortIndex"),
)
if mibBuilder.loadTexts:
    alaVMSnoopingUdpPortEntry.setStatus("current")
_AlaVMSnoopingUdpPortIndex_Type = Unsigned32
_AlaVMSnoopingUdpPortIndex_Object = MibTableColumn
alaVMSnoopingUdpPortIndex = _AlaVMSnoopingUdpPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 84, 1, 1, 3, 1, 1),
    _AlaVMSnoopingUdpPortIndex_Type()
)
alaVMSnoopingUdpPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaVMSnoopingUdpPortIndex.setStatus("current")
_AlaVMSnoopingUdpRowStatus_Type = RowStatus
_AlaVMSnoopingUdpRowStatus_Object = MibTableColumn
alaVMSnoopingUdpRowStatus = _AlaVMSnoopingUdpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 84, 1, 1, 3, 1, 2),
    _AlaVMSnoopingUdpRowStatus_Type()
)
alaVMSnoopingUdpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaVMSnoopingUdpRowStatus.setStatus("current")
_AlaVMSnoopingPortTable_Object = MibTable
alaVMSnoopingPortTable = _AlaVMSnoopingPortTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 84, 1, 1, 4)
)
if mibBuilder.loadTexts:
    alaVMSnoopingPortTable.setStatus("current")
_AlaVMSnoopingPortEntry_Object = MibTableRow
alaVMSnoopingPortEntry = _AlaVMSnoopingPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 84, 1, 1, 4, 1)
)
alaVMSnoopingPortEntry.setIndexNames(
    (0, "ALCATEL-ENT1-VM-SNOOPING-MIB", "alaVMSnoopingPortIndex"),
)
if mibBuilder.loadTexts:
    alaVMSnoopingPortEntry.setStatus("current")
_AlaVMSnoopingPortIndex_Type = InterfaceIndex
_AlaVMSnoopingPortIndex_Object = MibTableColumn
alaVMSnoopingPortIndex = _AlaVMSnoopingPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 84, 1, 1, 4, 1, 1),
    _AlaVMSnoopingPortIndex_Type()
)
alaVMSnoopingPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaVMSnoopingPortIndex.setStatus("current")


class _AlaVMSnoopingPortAdminStatus_Type(Integer32):
    """Custom type alaVMSnoopingPortAdminStatus based on Integer32"""
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


_AlaVMSnoopingPortAdminStatus_Type.__name__ = "Integer32"
_AlaVMSnoopingPortAdminStatus_Object = MibTableColumn
alaVMSnoopingPortAdminStatus = _AlaVMSnoopingPortAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 84, 1, 1, 4, 1, 2),
    _AlaVMSnoopingPortAdminStatus_Type()
)
alaVMSnoopingPortAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaVMSnoopingPortAdminStatus.setStatus("current")


class _AlaVMSnoopingPortIsVNP_Type(Integer32):
    """Custom type alaVMSnoopingPortIsVNP based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_AlaVMSnoopingPortIsVNP_Type.__name__ = "Integer32"
_AlaVMSnoopingPortIsVNP_Object = MibTableColumn
alaVMSnoopingPortIsVNP = _AlaVMSnoopingPortIsVNP_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 84, 1, 1, 4, 1, 3),
    _AlaVMSnoopingPortIsVNP_Type()
)
alaVMSnoopingPortIsVNP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaVMSnoopingPortIsVNP.setStatus("current")
_AlaVMSnoopingPortRowStatus_Type = RowStatus
_AlaVMSnoopingPortRowStatus_Object = MibTableColumn
alaVMSnoopingPortRowStatus = _AlaVMSnoopingPortRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 84, 1, 1, 4, 1, 4),
    _AlaVMSnoopingPortRowStatus_Type()
)
alaVMSnoopingPortRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaVMSnoopingPortRowStatus.setStatus("current")


class _AlaVMSnoopingPortDBClear_Type(Integer32):
    """Custom type alaVMSnoopingPortDBClear based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_AlaVMSnoopingPortDBClear_Type.__name__ = "Integer32"
_AlaVMSnoopingPortDBClear_Object = MibTableColumn
alaVMSnoopingPortDBClear = _AlaVMSnoopingPortDBClear_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 84, 1, 1, 4, 1, 5),
    _AlaVMSnoopingPortDBClear_Type()
)
alaVMSnoopingPortDBClear.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaVMSnoopingPortDBClear.setStatus("current")


class _AlaVMSnoopingPortSamplingClearStats_Type(Integer32):
    """Custom type alaVMSnoopingPortSamplingClearStats based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_AlaVMSnoopingPortSamplingClearStats_Type.__name__ = "Integer32"
_AlaVMSnoopingPortSamplingClearStats_Object = MibTableColumn
alaVMSnoopingPortSamplingClearStats = _AlaVMSnoopingPortSamplingClearStats_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 84, 1, 1, 4, 1, 6),
    _AlaVMSnoopingPortSamplingClearStats_Type()
)
alaVMSnoopingPortSamplingClearStats.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaVMSnoopingPortSamplingClearStats.setStatus("current")
_AlaVMSnoopingDBTable_Object = MibTable
alaVMSnoopingDBTable = _AlaVMSnoopingDBTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 84, 1, 1, 5)
)
if mibBuilder.loadTexts:
    alaVMSnoopingDBTable.setStatus("current")
_AlaVMSnoopingDBEntry_Object = MibTableRow
alaVMSnoopingDBEntry = _AlaVMSnoopingDBEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 84, 1, 1, 5, 1)
)
alaVMSnoopingDBEntry.setIndexNames(
    (0, "ALCATEL-ENT1-VM-SNOOPING-MIB", "alaVMSnoopingDBFlowId"),
)
if mibBuilder.loadTexts:
    alaVMSnoopingDBEntry.setStatus("current")
_AlaVMSnoopingDBFlowId_Type = Unsigned32
_AlaVMSnoopingDBFlowId_Object = MibTableColumn
alaVMSnoopingDBFlowId = _AlaVMSnoopingDBFlowId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 84, 1, 1, 5, 1, 1),
    _AlaVMSnoopingDBFlowId_Type()
)
alaVMSnoopingDBFlowId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaVMSnoopingDBFlowId.setStatus("current")
_AlaVMSnoopingDBIfIndex_Type = InterfaceIndex
_AlaVMSnoopingDBIfIndex_Object = MibTableColumn
alaVMSnoopingDBIfIndex = _AlaVMSnoopingDBIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 84, 1, 1, 5, 1, 2),
    _AlaVMSnoopingDBIfIndex_Type()
)
alaVMSnoopingDBIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaVMSnoopingDBIfIndex.setStatus("current")


class _AlaVMSnoopingDBVxlanUdpDestPort_Type(Integer32):
    """Custom type alaVMSnoopingDBVxlanUdpDestPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlaVMSnoopingDBVxlanUdpDestPort_Type.__name__ = "Integer32"
_AlaVMSnoopingDBVxlanUdpDestPort_Object = MibTableColumn
alaVMSnoopingDBVxlanUdpDestPort = _AlaVMSnoopingDBVxlanUdpDestPort_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 84, 1, 1, 5, 1, 3),
    _AlaVMSnoopingDBVxlanUdpDestPort_Type()
)
alaVMSnoopingDBVxlanUdpDestPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaVMSnoopingDBVxlanUdpDestPort.setStatus("current")


class _AlaVMSnoopingDBVni_Type(Integer32):
    """Custom type alaVMSnoopingDBVni based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlaVMSnoopingDBVni_Type.__name__ = "Integer32"
_AlaVMSnoopingDBVni_Object = MibTableColumn
alaVMSnoopingDBVni = _AlaVMSnoopingDBVni_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 84, 1, 1, 5, 1, 4),
    _AlaVMSnoopingDBVni_Type()
)
alaVMSnoopingDBVni.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaVMSnoopingDBVni.setStatus("current")


class _AlaVMSnoopingDBVtepVlan_Type(Integer32):
    """Custom type alaVMSnoopingDBVtepVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlaVMSnoopingDBVtepVlan_Type.__name__ = "Integer32"
_AlaVMSnoopingDBVtepVlan_Object = MibTableColumn
alaVMSnoopingDBVtepVlan = _AlaVMSnoopingDBVtepVlan_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 84, 1, 1, 5, 1, 5),
    _AlaVMSnoopingDBVtepVlan_Type()
)
alaVMSnoopingDBVtepVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaVMSnoopingDBVtepVlan.setStatus("current")


class _AlaVMSnoopingDBVtepSrcIpAddrType_Type(InetAddressType):
    """Custom type alaVMSnoopingDBVtepSrcIpAddrType based on InetAddressType"""
    subtypeSpec = InetAddressType.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipv4", 1),
          ("ipv6", 2))
    )


_AlaVMSnoopingDBVtepSrcIpAddrType_Type.__name__ = "InetAddressType"
_AlaVMSnoopingDBVtepSrcIpAddrType_Object = MibTableColumn
alaVMSnoopingDBVtepSrcIpAddrType = _AlaVMSnoopingDBVtepSrcIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 84, 1, 1, 5, 1, 6),
    _AlaVMSnoopingDBVtepSrcIpAddrType_Type()
)
alaVMSnoopingDBVtepSrcIpAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaVMSnoopingDBVtepSrcIpAddrType.setStatus("current")


class _AlaVMSnoopingDBVtepSrcIpAddr_Type(InetAddress):
    """Custom type alaVMSnoopingDBVtepSrcIpAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_AlaVMSnoopingDBVtepSrcIpAddr_Type.__name__ = "InetAddress"
_AlaVMSnoopingDBVtepSrcIpAddr_Object = MibTableColumn
alaVMSnoopingDBVtepSrcIpAddr = _AlaVMSnoopingDBVtepSrcIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 84, 1, 1, 5, 1, 7),
    _AlaVMSnoopingDBVtepSrcIpAddr_Type()
)
alaVMSnoopingDBVtepSrcIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaVMSnoopingDBVtepSrcIpAddr.setStatus("current")


class _AlaVMSnoopingDBVtepDestIpAddrType_Type(InetAddressType):
    """Custom type alaVMSnoopingDBVtepDestIpAddrType based on InetAddressType"""
    subtypeSpec = InetAddressType.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipv4", 1),
          ("ipv6", 2))
    )


_AlaVMSnoopingDBVtepDestIpAddrType_Type.__name__ = "InetAddressType"
_AlaVMSnoopingDBVtepDestIpAddrType_Object = MibTableColumn
alaVMSnoopingDBVtepDestIpAddrType = _AlaVMSnoopingDBVtepDestIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 84, 1, 1, 5, 1, 8),
    _AlaVMSnoopingDBVtepDestIpAddrType_Type()
)
alaVMSnoopingDBVtepDestIpAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaVMSnoopingDBVtepDestIpAddrType.setStatus("current")


class _AlaVMSnoopingDBVtepDestIpAddr_Type(InetAddress):
    """Custom type alaVMSnoopingDBVtepDestIpAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_AlaVMSnoopingDBVtepDestIpAddr_Type.__name__ = "InetAddress"
_AlaVMSnoopingDBVtepDestIpAddr_Object = MibTableColumn
alaVMSnoopingDBVtepDestIpAddr = _AlaVMSnoopingDBVtepDestIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 84, 1, 1, 5, 1, 9),
    _AlaVMSnoopingDBVtepDestIpAddr_Type()
)
alaVMSnoopingDBVtepDestIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaVMSnoopingDBVtepDestIpAddr.setStatus("current")
_AlaVMSnoopingDBInnerSrcMacAddr_Type = MacAddress
_AlaVMSnoopingDBInnerSrcMacAddr_Object = MibTableColumn
alaVMSnoopingDBInnerSrcMacAddr = _AlaVMSnoopingDBInnerSrcMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 84, 1, 1, 5, 1, 10),
    _AlaVMSnoopingDBInnerSrcMacAddr_Type()
)
alaVMSnoopingDBInnerSrcMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaVMSnoopingDBInnerSrcMacAddr.setStatus("current")
_AlaVMSnoopingDBInnerDestMacAddr_Type = MacAddress
_AlaVMSnoopingDBInnerDestMacAddr_Object = MibTableColumn
alaVMSnoopingDBInnerDestMacAddr = _AlaVMSnoopingDBInnerDestMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 84, 1, 1, 5, 1, 11),
    _AlaVMSnoopingDBInnerDestMacAddr_Type()
)
alaVMSnoopingDBInnerDestMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaVMSnoopingDBInnerDestMacAddr.setStatus("current")


class _AlaVMSnoopingDBInnerVlan_Type(Integer32):
    """Custom type alaVMSnoopingDBInnerVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlaVMSnoopingDBInnerVlan_Type.__name__ = "Integer32"
_AlaVMSnoopingDBInnerVlan_Object = MibTableColumn
alaVMSnoopingDBInnerVlan = _AlaVMSnoopingDBInnerVlan_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 84, 1, 1, 5, 1, 12),
    _AlaVMSnoopingDBInnerVlan_Type()
)
alaVMSnoopingDBInnerVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaVMSnoopingDBInnerVlan.setStatus("current")


class _AlaVMSnoopingDBInnerSrcIpAddrType_Type(InetAddressType):
    """Custom type alaVMSnoopingDBInnerSrcIpAddrType based on InetAddressType"""
    subtypeSpec = InetAddressType.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipv4", 1),
          ("ipv6", 2))
    )


_AlaVMSnoopingDBInnerSrcIpAddrType_Type.__name__ = "InetAddressType"
_AlaVMSnoopingDBInnerSrcIpAddrType_Object = MibTableColumn
alaVMSnoopingDBInnerSrcIpAddrType = _AlaVMSnoopingDBInnerSrcIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 84, 1, 1, 5, 1, 13),
    _AlaVMSnoopingDBInnerSrcIpAddrType_Type()
)
alaVMSnoopingDBInnerSrcIpAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaVMSnoopingDBInnerSrcIpAddrType.setStatus("current")


class _AlaVMSnoopingDBInnerSrcIpAddr_Type(InetAddress):
    """Custom type alaVMSnoopingDBInnerSrcIpAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_AlaVMSnoopingDBInnerSrcIpAddr_Type.__name__ = "InetAddress"
_AlaVMSnoopingDBInnerSrcIpAddr_Object = MibTableColumn
alaVMSnoopingDBInnerSrcIpAddr = _AlaVMSnoopingDBInnerSrcIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 84, 1, 1, 5, 1, 14),
    _AlaVMSnoopingDBInnerSrcIpAddr_Type()
)
alaVMSnoopingDBInnerSrcIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaVMSnoopingDBInnerSrcIpAddr.setStatus("current")


class _AlaVMSnoopingDBInnerDestIpAddrType_Type(InetAddressType):
    """Custom type alaVMSnoopingDBInnerDestIpAddrType based on InetAddressType"""
    subtypeSpec = InetAddressType.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipv4", 1),
          ("ipv6", 2))
    )


_AlaVMSnoopingDBInnerDestIpAddrType_Type.__name__ = "InetAddressType"
_AlaVMSnoopingDBInnerDestIpAddrType_Object = MibTableColumn
alaVMSnoopingDBInnerDestIpAddrType = _AlaVMSnoopingDBInnerDestIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 84, 1, 1, 5, 1, 15),
    _AlaVMSnoopingDBInnerDestIpAddrType_Type()
)
alaVMSnoopingDBInnerDestIpAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaVMSnoopingDBInnerDestIpAddrType.setStatus("current")


class _AlaVMSnoopingDBInnerDestIpAddr_Type(InetAddress):
    """Custom type alaVMSnoopingDBInnerDestIpAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_AlaVMSnoopingDBInnerDestIpAddr_Type.__name__ = "InetAddress"
_AlaVMSnoopingDBInnerDestIpAddr_Object = MibTableColumn
alaVMSnoopingDBInnerDestIpAddr = _AlaVMSnoopingDBInnerDestIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 84, 1, 1, 5, 1, 16),
    _AlaVMSnoopingDBInnerDestIpAddr_Type()
)
alaVMSnoopingDBInnerDestIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaVMSnoopingDBInnerDestIpAddr.setStatus("current")


class _AlaVMSnoopingDBVInnerL4SrcPort_Type(Integer32):
    """Custom type alaVMSnoopingDBVInnerL4SrcPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlaVMSnoopingDBVInnerL4SrcPort_Type.__name__ = "Integer32"
_AlaVMSnoopingDBVInnerL4SrcPort_Object = MibTableColumn
alaVMSnoopingDBVInnerL4SrcPort = _AlaVMSnoopingDBVInnerL4SrcPort_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 84, 1, 1, 5, 1, 17),
    _AlaVMSnoopingDBVInnerL4SrcPort_Type()
)
alaVMSnoopingDBVInnerL4SrcPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaVMSnoopingDBVInnerL4SrcPort.setStatus("current")


class _AlaVMSnoopingDBVInnerL4DestPort_Type(Integer32):
    """Custom type alaVMSnoopingDBVInnerL4DestPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlaVMSnoopingDBVInnerL4DestPort_Type.__name__ = "Integer32"
_AlaVMSnoopingDBVInnerL4DestPort_Object = MibTableColumn
alaVMSnoopingDBVInnerL4DestPort = _AlaVMSnoopingDBVInnerL4DestPort_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 84, 1, 1, 5, 1, 18),
    _AlaVMSnoopingDBVInnerL4DestPort_Type()
)
alaVMSnoopingDBVInnerL4DestPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaVMSnoopingDBVInnerL4DestPort.setStatus("current")


class _AlaVMSnoopingDBVInnerIPProtocol_Type(Integer32):
    """Custom type alaVMSnoopingDBVInnerIPProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaVMSnoopingDBVInnerIPProtocol_Type.__name__ = "Integer32"
_AlaVMSnoopingDBVInnerIPProtocol_Object = MibTableColumn
alaVMSnoopingDBVInnerIPProtocol = _AlaVMSnoopingDBVInnerIPProtocol_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 84, 1, 1, 5, 1, 19),
    _AlaVMSnoopingDBVInnerIPProtocol_Type()
)
alaVMSnoopingDBVInnerIPProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaVMSnoopingDBVInnerIPProtocol.setStatus("current")


class _AlaVMSnoopingDBPolicyRule_Type(SnmpAdminString):
    """Custom type alaVMSnoopingDBPolicyRule based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AlaVMSnoopingDBPolicyRule_Type.__name__ = "SnmpAdminString"
_AlaVMSnoopingDBPolicyRule_Object = MibTableColumn
alaVMSnoopingDBPolicyRule = _AlaVMSnoopingDBPolicyRule_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 84, 1, 1, 5, 1, 20),
    _AlaVMSnoopingDBPolicyRule_Type()
)
alaVMSnoopingDBPolicyRule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaVMSnoopingDBPolicyRule.setStatus("current")


class _AlaVMSnoopingDBPolicyList_Type(SnmpAdminString):
    """Custom type alaVMSnoopingDBPolicyList based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AlaVMSnoopingDBPolicyList_Type.__name__ = "SnmpAdminString"
_AlaVMSnoopingDBPolicyList_Object = MibTableColumn
alaVMSnoopingDBPolicyList = _AlaVMSnoopingDBPolicyList_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 84, 1, 1, 5, 1, 21),
    _AlaVMSnoopingDBPolicyList_Type()
)
alaVMSnoopingDBPolicyList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaVMSnoopingDBPolicyList.setStatus("current")
_AlaVMSnoopingDBSamplingStatsPackets_Type = Counter64
_AlaVMSnoopingDBSamplingStatsPackets_Object = MibTableColumn
alaVMSnoopingDBSamplingStatsPackets = _AlaVMSnoopingDBSamplingStatsPackets_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 84, 1, 1, 5, 1, 22),
    _AlaVMSnoopingDBSamplingStatsPackets_Type()
)
alaVMSnoopingDBSamplingStatsPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaVMSnoopingDBSamplingStatsPackets.setStatus("current")
_AlaVMSnoopingHardwareStatsTable_Object = MibTable
alaVMSnoopingHardwareStatsTable = _AlaVMSnoopingHardwareStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 84, 1, 1, 6)
)
if mibBuilder.loadTexts:
    alaVMSnoopingHardwareStatsTable.setStatus("current")
_AlaVMSnoopingHardwareStatsEntry_Object = MibTableRow
alaVMSnoopingHardwareStatsEntry = _AlaVMSnoopingHardwareStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 84, 1, 1, 6, 1)
)
alaVMSnoopingHardwareStatsEntry.setIndexNames(
    (0, "ALCATEL-ENT1-VM-SNOOPING-MIB", "alaVMSnoopingHardwareStatsIndex"),
)
if mibBuilder.loadTexts:
    alaVMSnoopingHardwareStatsEntry.setStatus("current")
_AlaVMSnoopingHardwareStatsIndex_Type = Unsigned32
_AlaVMSnoopingHardwareStatsIndex_Object = MibTableColumn
alaVMSnoopingHardwareStatsIndex = _AlaVMSnoopingHardwareStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 84, 1, 1, 6, 1, 1),
    _AlaVMSnoopingHardwareStatsIndex_Type()
)
alaVMSnoopingHardwareStatsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaVMSnoopingHardwareStatsIndex.setStatus("current")


class _AlaVMSnoopingHardwareStatsPolicylist_Type(SnmpAdminString):
    """Custom type alaVMSnoopingHardwareStatsPolicylist based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AlaVMSnoopingHardwareStatsPolicylist_Type.__name__ = "SnmpAdminString"
_AlaVMSnoopingHardwareStatsPolicylist_Object = MibTableColumn
alaVMSnoopingHardwareStatsPolicylist = _AlaVMSnoopingHardwareStatsPolicylist_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 84, 1, 1, 6, 1, 2),
    _AlaVMSnoopingHardwareStatsPolicylist_Type()
)
alaVMSnoopingHardwareStatsPolicylist.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaVMSnoopingHardwareStatsPolicylist.setStatus("current")


class _AlaVMSnoopingHardwareStatsPolicyrule_Type(SnmpAdminString):
    """Custom type alaVMSnoopingHardwareStatsPolicyrule based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AlaVMSnoopingHardwareStatsPolicyrule_Type.__name__ = "SnmpAdminString"
_AlaVMSnoopingHardwareStatsPolicyrule_Object = MibTableColumn
alaVMSnoopingHardwareStatsPolicyrule = _AlaVMSnoopingHardwareStatsPolicyrule_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 84, 1, 1, 6, 1, 3),
    _AlaVMSnoopingHardwareStatsPolicyrule_Type()
)
alaVMSnoopingHardwareStatsPolicyrule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaVMSnoopingHardwareStatsPolicyrule.setStatus("current")
_AlaVMSnoopingHardwareStatsNumOfPackets_Type = Counter64
_AlaVMSnoopingHardwareStatsNumOfPackets_Object = MibTableColumn
alaVMSnoopingHardwareStatsNumOfPackets = _AlaVMSnoopingHardwareStatsNumOfPackets_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 84, 1, 1, 6, 1, 4),
    _AlaVMSnoopingHardwareStatsNumOfPackets_Type()
)
alaVMSnoopingHardwareStatsNumOfPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaVMSnoopingHardwareStatsNumOfPackets.setStatus("current")
_AlaVMSnoopingHardwareStatsNumOfBytes_Type = Counter64
_AlaVMSnoopingHardwareStatsNumOfBytes_Object = MibTableColumn
alaVMSnoopingHardwareStatsNumOfBytes = _AlaVMSnoopingHardwareStatsNumOfBytes_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 84, 1, 1, 6, 1, 5),
    _AlaVMSnoopingHardwareStatsNumOfBytes_Type()
)
alaVMSnoopingHardwareStatsNumOfBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaVMSnoopingHardwareStatsNumOfBytes.setStatus("current")
_AlaVMSnoopingFilterResourceTable_Object = MibTable
alaVMSnoopingFilterResourceTable = _AlaVMSnoopingFilterResourceTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 84, 1, 1, 7)
)
if mibBuilder.loadTexts:
    alaVMSnoopingFilterResourceTable.setStatus("current")
_AlaVMSnoopingFilterResourceEntry_Object = MibTableRow
alaVMSnoopingFilterResourceEntry = _AlaVMSnoopingFilterResourceEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 84, 1, 1, 7, 1)
)
alaVMSnoopingFilterResourceEntry.setIndexNames(
    (0, "ALCATEL-ENT1-VM-SNOOPING-MIB", "alaVMSnoopingFilterResourceChassisId"),
    (0, "ALCATEL-ENT1-VM-SNOOPING-MIB", "alaVMSnoopingFilterResourceSlotNum"),
)
if mibBuilder.loadTexts:
    alaVMSnoopingFilterResourceEntry.setStatus("current")
_AlaVMSnoopingFilterResourceChassisId_Type = Unsigned32
_AlaVMSnoopingFilterResourceChassisId_Object = MibTableColumn
alaVMSnoopingFilterResourceChassisId = _AlaVMSnoopingFilterResourceChassisId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 84, 1, 1, 7, 1, 1),
    _AlaVMSnoopingFilterResourceChassisId_Type()
)
alaVMSnoopingFilterResourceChassisId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaVMSnoopingFilterResourceChassisId.setStatus("current")
_AlaVMSnoopingFilterResourceSlotNum_Type = Unsigned32
_AlaVMSnoopingFilterResourceSlotNum_Object = MibTableColumn
alaVMSnoopingFilterResourceSlotNum = _AlaVMSnoopingFilterResourceSlotNum_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 84, 1, 1, 7, 1, 2),
    _AlaVMSnoopingFilterResourceSlotNum_Type()
)
alaVMSnoopingFilterResourceSlotNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaVMSnoopingFilterResourceSlotNum.setStatus("current")
_AlaVMSnoopingFilterResourceMax_Type = Integer32
_AlaVMSnoopingFilterResourceMax_Object = MibTableColumn
alaVMSnoopingFilterResourceMax = _AlaVMSnoopingFilterResourceMax_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 84, 1, 1, 7, 1, 3),
    _AlaVMSnoopingFilterResourceMax_Type()
)
alaVMSnoopingFilterResourceMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaVMSnoopingFilterResourceMax.setStatus("current")
_AlaVMSnoopingFilterResourceUsed_Type = Integer32
_AlaVMSnoopingFilterResourceUsed_Object = MibTableColumn
alaVMSnoopingFilterResourceUsed = _AlaVMSnoopingFilterResourceUsed_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 84, 1, 1, 7, 1, 4),
    _AlaVMSnoopingFilterResourceUsed_Type()
)
alaVMSnoopingFilterResourceUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaVMSnoopingFilterResourceUsed.setStatus("current")
_AlaVMSnoopingLearntVMTable_Object = MibTable
alaVMSnoopingLearntVMTable = _AlaVMSnoopingLearntVMTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 84, 1, 1, 8)
)
if mibBuilder.loadTexts:
    alaVMSnoopingLearntVMTable.setStatus("current")
_AlaVMSnoopingLearntVMEntry_Object = MibTableRow
alaVMSnoopingLearntVMEntry = _AlaVMSnoopingLearntVMEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 84, 1, 1, 8, 1)
)
alaVMSnoopingLearntVMEntry.setIndexNames(
    (0, "ALCATEL-ENT1-VM-SNOOPING-MIB", "alaVMSnoopingLearntVMIfIndex"),
    (0, "ALCATEL-ENT1-VM-SNOOPING-MIB", "alaVMSnoopingLearntVMSrcMac"),
)
if mibBuilder.loadTexts:
    alaVMSnoopingLearntVMEntry.setStatus("current")
_AlaVMSnoopingLearntVMIfIndex_Type = InterfaceIndex
_AlaVMSnoopingLearntVMIfIndex_Object = MibTableColumn
alaVMSnoopingLearntVMIfIndex = _AlaVMSnoopingLearntVMIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 84, 1, 1, 8, 1, 1),
    _AlaVMSnoopingLearntVMIfIndex_Type()
)
alaVMSnoopingLearntVMIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaVMSnoopingLearntVMIfIndex.setStatus("current")
_AlaVMSnoopingLearntVMSrcMac_Type = MacAddress
_AlaVMSnoopingLearntVMSrcMac_Object = MibTableColumn
alaVMSnoopingLearntVMSrcMac = _AlaVMSnoopingLearntVMSrcMac_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 84, 1, 1, 8, 1, 2),
    _AlaVMSnoopingLearntVMSrcMac_Type()
)
alaVMSnoopingLearntVMSrcMac.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaVMSnoopingLearntVMSrcMac.setStatus("current")
_AlaVMSnoopingLearntVMVlanId_Type = Integer32
_AlaVMSnoopingLearntVMVlanId_Object = MibTableColumn
alaVMSnoopingLearntVMVlanId = _AlaVMSnoopingLearntVMVlanId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 84, 1, 1, 8, 1, 3),
    _AlaVMSnoopingLearntVMVlanId_Type()
)
alaVMSnoopingLearntVMVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaVMSnoopingLearntVMVlanId.setStatus("current")
_AlaVMSnoopingStaticPolicyTable_Object = MibTable
alaVMSnoopingStaticPolicyTable = _AlaVMSnoopingStaticPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 84, 1, 1, 9)
)
if mibBuilder.loadTexts:
    alaVMSnoopingStaticPolicyTable.setStatus("current")
_AlaVMSnoopingStaticPolicyEntry_Object = MibTableRow
alaVMSnoopingStaticPolicyEntry = _AlaVMSnoopingStaticPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 84, 1, 1, 9, 1)
)
alaVMSnoopingStaticPolicyEntry.setIndexNames(
    (0, "ALCATEL-ENT1-VM-SNOOPING-MIB", "alaVMSnoopingStaticPolicyRuleName"),
    (0, "ALCATEL-ENT1-VM-SNOOPING-MIB", "alaVMSnoopingStaticPolicyListName"),
)
if mibBuilder.loadTexts:
    alaVMSnoopingStaticPolicyEntry.setStatus("current")


class _AlaVMSnoopingStaticPolicyRuleName_Type(SnmpAdminString):
    """Custom type alaVMSnoopingStaticPolicyRuleName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AlaVMSnoopingStaticPolicyRuleName_Type.__name__ = "SnmpAdminString"
_AlaVMSnoopingStaticPolicyRuleName_Object = MibTableColumn
alaVMSnoopingStaticPolicyRuleName = _AlaVMSnoopingStaticPolicyRuleName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 84, 1, 1, 9, 1, 1),
    _AlaVMSnoopingStaticPolicyRuleName_Type()
)
alaVMSnoopingStaticPolicyRuleName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaVMSnoopingStaticPolicyRuleName.setStatus("current")


class _AlaVMSnoopingStaticPolicyListName_Type(SnmpAdminString):
    """Custom type alaVMSnoopingStaticPolicyListName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AlaVMSnoopingStaticPolicyListName_Type.__name__ = "SnmpAdminString"
_AlaVMSnoopingStaticPolicyListName_Object = MibTableColumn
alaVMSnoopingStaticPolicyListName = _AlaVMSnoopingStaticPolicyListName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 84, 1, 1, 9, 1, 2),
    _AlaVMSnoopingStaticPolicyListName_Type()
)
alaVMSnoopingStaticPolicyListName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaVMSnoopingStaticPolicyListName.setStatus("current")
_AlaVMSnoopingStaticPolicyRowStatus_Type = RowStatus
_AlaVMSnoopingStaticPolicyRowStatus_Object = MibTableColumn
alaVMSnoopingStaticPolicyRowStatus = _AlaVMSnoopingStaticPolicyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 84, 1, 1, 9, 1, 3),
    _AlaVMSnoopingStaticPolicyRowStatus_Type()
)
alaVMSnoopingStaticPolicyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaVMSnoopingStaticPolicyRowStatus.setStatus("current")
_AlaVMSnoopingMIBConformance_ObjectIdentity = ObjectIdentity
alaVMSnoopingMIBConformance = _AlaVMSnoopingMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 84, 1, 2)
)
if mibBuilder.loadTexts:
    alaVMSnoopingMIBConformance.setStatus("current")
_AlaVMSnoopingMIBGroups_ObjectIdentity = ObjectIdentity
alaVMSnoopingMIBGroups = _AlaVMSnoopingMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 84, 1, 2, 1)
)
if mibBuilder.loadTexts:
    alaVMSnoopingMIBGroups.setStatus("current")
_AlaVMSnoopingMIBCompliances_ObjectIdentity = ObjectIdentity
alaVMSnoopingMIBCompliances = _AlaVMSnoopingMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 84, 1, 2, 2)
)
if mibBuilder.loadTexts:
    alaVMSnoopingMIBCompliances.setStatus("current")

# Managed Objects groups

alaVMSnoopingConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 84, 1, 2, 1, 1)
)
alaVMSnoopingConfigGroup.setObjects(
      *(("ALCATEL-ENT1-VM-SNOOPING-MIB", "alaVMSnoopingAdminStatus"),
        ("ALCATEL-ENT1-VM-SNOOPING-MIB", "alaVMSnoopingPolicyMode"),
        ("ALCATEL-ENT1-VM-SNOOPING-MIB", "alaVMSnoopingPolicyResource"),
        ("ALCATEL-ENT1-VM-SNOOPING-MIB", "alaVMSnoopingVMTrafficTagged"),
        ("ALCATEL-ENT1-VM-SNOOPING-MIB", "alaVMSnoopingTrapStatus"),
        ("ALCATEL-ENT1-VM-SNOOPING-MIB", "alaVMSnoopingSamplingRate"),
        ("ALCATEL-ENT1-VM-SNOOPING-MIB", "alaVMSnoopingAgingTimer"),
        ("ALCATEL-ENT1-VM-SNOOPING-MIB", "alaVMSnoopingFilteringResourceTrapThreshold"),
        ("ALCATEL-ENT1-VM-SNOOPING-MIB", "alaVMSnoopingClearAllData"),
        ("ALCATEL-ENT1-VM-SNOOPING-MIB", "alaVMSnoopingLoggingThresholdFlows"),
        ("ALCATEL-ENT1-VM-SNOOPING-MIB", "alaVMSnoopingQosAllocationStatus"))
)
if mibBuilder.loadTexts:
    alaVMSnoopingConfigGroup.setStatus("current")

alaVMSnoopingUdpPortGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 84, 1, 2, 1, 2)
)
alaVMSnoopingUdpPortGroup.setObjects(
    ("ALCATEL-ENT1-VM-SNOOPING-MIB", "alaVMSnoopingUdpRowStatus")
)
if mibBuilder.loadTexts:
    alaVMSnoopingUdpPortGroup.setStatus("current")

alaVMSnoopingPortGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 84, 1, 2, 1, 3)
)
alaVMSnoopingPortGroup.setObjects(
      *(("ALCATEL-ENT1-VM-SNOOPING-MIB", "alaVMSnoopingPortAdminStatus"),
        ("ALCATEL-ENT1-VM-SNOOPING-MIB", "alaVMSnoopingPortIsVNP"),
        ("ALCATEL-ENT1-VM-SNOOPING-MIB", "alaVMSnoopingPortRowStatus"),
        ("ALCATEL-ENT1-VM-SNOOPING-MIB", "alaVMSnoopingPortDBClear"),
        ("ALCATEL-ENT1-VM-SNOOPING-MIB", "alaVMSnoopingPortSamplingClearStats"))
)
if mibBuilder.loadTexts:
    alaVMSnoopingPortGroup.setStatus("current")

alaVMSnoopingDBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 84, 1, 2, 1, 4)
)
alaVMSnoopingDBGroup.setObjects(
      *(("ALCATEL-ENT1-VM-SNOOPING-MIB", "alaVMSnoopingDBIfIndex"),
        ("ALCATEL-ENT1-VM-SNOOPING-MIB", "alaVMSnoopingDBVxlanUdpDestPort"),
        ("ALCATEL-ENT1-VM-SNOOPING-MIB", "alaVMSnoopingDBVni"),
        ("ALCATEL-ENT1-VM-SNOOPING-MIB", "alaVMSnoopingDBVtepVlan"),
        ("ALCATEL-ENT1-VM-SNOOPING-MIB", "alaVMSnoopingDBVtepSrcIpAddrType"),
        ("ALCATEL-ENT1-VM-SNOOPING-MIB", "alaVMSnoopingDBVtepSrcIpAddr"),
        ("ALCATEL-ENT1-VM-SNOOPING-MIB", "alaVMSnoopingDBVtepDestIpAddrType"),
        ("ALCATEL-ENT1-VM-SNOOPING-MIB", "alaVMSnoopingDBVtepDestIpAddr"),
        ("ALCATEL-ENT1-VM-SNOOPING-MIB", "alaVMSnoopingDBInnerSrcMacAddr"),
        ("ALCATEL-ENT1-VM-SNOOPING-MIB", "alaVMSnoopingDBInnerDestMacAddr"),
        ("ALCATEL-ENT1-VM-SNOOPING-MIB", "alaVMSnoopingDBInnerVlan"),
        ("ALCATEL-ENT1-VM-SNOOPING-MIB", "alaVMSnoopingDBInnerSrcIpAddrType"),
        ("ALCATEL-ENT1-VM-SNOOPING-MIB", "alaVMSnoopingDBInnerSrcIpAddr"),
        ("ALCATEL-ENT1-VM-SNOOPING-MIB", "alaVMSnoopingDBInnerDestIpAddrType"),
        ("ALCATEL-ENT1-VM-SNOOPING-MIB", "alaVMSnoopingDBInnerDestIpAddr"),
        ("ALCATEL-ENT1-VM-SNOOPING-MIB", "alaVMSnoopingDBVInnerL4SrcPort"),
        ("ALCATEL-ENT1-VM-SNOOPING-MIB", "alaVMSnoopingDBVInnerL4DestPort"),
        ("ALCATEL-ENT1-VM-SNOOPING-MIB", "alaVMSnoopingDBVInnerIPProtocol"),
        ("ALCATEL-ENT1-VM-SNOOPING-MIB", "alaVMSnoopingDBPolicyRule"),
        ("ALCATEL-ENT1-VM-SNOOPING-MIB", "alaVMSnoopingDBPolicyList"),
        ("ALCATEL-ENT1-VM-SNOOPING-MIB", "alaVMSnoopingDBSamplingStatsPackets"))
)
if mibBuilder.loadTexts:
    alaVMSnoopingDBGroup.setStatus("current")

alaVMSnoopingHardwareStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 84, 1, 2, 1, 5)
)
alaVMSnoopingHardwareStatsGroup.setObjects(
      *(("ALCATEL-ENT1-VM-SNOOPING-MIB", "alaVMSnoopingHardwareStatsPolicylist"),
        ("ALCATEL-ENT1-VM-SNOOPING-MIB", "alaVMSnoopingHardwareStatsPolicyrule"),
        ("ALCATEL-ENT1-VM-SNOOPING-MIB", "alaVMSnoopingHardwareStatsNumOfPackets"),
        ("ALCATEL-ENT1-VM-SNOOPING-MIB", "alaVMSnoopingHardwareStatsNumOfBytes"))
)
if mibBuilder.loadTexts:
    alaVMSnoopingHardwareStatsGroup.setStatus("current")

alaVMSnoopingFilterResourceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 84, 1, 2, 1, 6)
)
alaVMSnoopingFilterResourceGroup.setObjects(
      *(("ALCATEL-ENT1-VM-SNOOPING-MIB", "alaVMSnoopingFilterResourceMax"),
        ("ALCATEL-ENT1-VM-SNOOPING-MIB", "alaVMSnoopingFilterResourceUsed"))
)
if mibBuilder.loadTexts:
    alaVMSnoopingFilterResourceGroup.setStatus("current")

alaVMSnoopingTrapsObjGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 84, 1, 2, 1, 8)
)
alaVMSnoopingTrapsObjGroup.setObjects(
      *(("ALCATEL-ENT1-VM-SNOOPING-MIB", "alaVMSnoopingLearnedMacAddress"),
        ("ALCATEL-ENT1-VM-SNOOPING-MIB", "alaVMSnoopingLearnedVxlanUdpPort"),
        ("ALCATEL-ENT1-VM-SNOOPING-MIB", "alaVMSnoopingLearnedVxlanVni"),
        ("ALCATEL-ENT1-VM-SNOOPING-MIB", "alaVMSnoopingChassisId"),
        ("ALCATEL-ENT1-VM-SNOOPING-MIB", "alaVMSnoopingNiSlot"),
        ("ALCATEL-ENT1-VM-SNOOPING-MIB", "alaVMSnoopingHwResourceTotal"),
        ("ALCATEL-ENT1-VM-SNOOPING-MIB", "alaVMSnoopingHwResourceUsed"))
)
if mibBuilder.loadTexts:
    alaVMSnoopingTrapsObjGroup.setStatus("current")

alaVMSnoopingLearntVMGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 84, 1, 2, 1, 9)
)
alaVMSnoopingLearntVMGroup.setObjects(
    ("ALCATEL-ENT1-VM-SNOOPING-MIB", "alaVMSnoopingLearntVMVlanId")
)
if mibBuilder.loadTexts:
    alaVMSnoopingLearntVMGroup.setStatus("current")

alaVMSnoopingStaticPolicyGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 84, 1, 2, 1, 10)
)
alaVMSnoopingStaticPolicyGroup.setObjects(
    ("ALCATEL-ENT1-VM-SNOOPING-MIB", "alaVMSnoopingStaticPolicyRowStatus")
)
if mibBuilder.loadTexts:
    alaVMSnoopingStaticPolicyGroup.setStatus("current")


# Notification objects

alaVMSnoopingVMLearntAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 84, 1, 0, 1)
)
alaVMSnoopingVMLearntAlert.setObjects(
      *(("ALCATEL-ENT1-VM-SNOOPING-MIB", "alaVMSnoopingLearnedMacAddress"),
        ("ALCATEL-ENT1-VM-SNOOPING-MIB", "alaVMSnoopingLearnedVxlanUdpPort"),
        ("ALCATEL-ENT1-VM-SNOOPING-MIB", "alaVMSnoopingLearnedVxlanVni"))
)
if mibBuilder.loadTexts:
    alaVMSnoopingVMLearntAlert.setStatus(
        "current"
    )

alaVMSnoopingVMRemovedAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 84, 1, 0, 2)
)
alaVMSnoopingVMRemovedAlert.setObjects(
    ("ALCATEL-ENT1-VM-SNOOPING-MIB", "alaVMSnoopingLearnedMacAddress")
)
if mibBuilder.loadTexts:
    alaVMSnoopingVMRemovedAlert.setStatus(
        "current"
    )

alaVMSnoopingReservedHwResourceLimitAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 84, 1, 0, 3)
)
alaVMSnoopingReservedHwResourceLimitAlert.setObjects(
      *(("ALCATEL-ENT1-VM-SNOOPING-MIB", "alaVMSnoopingChassisId"),
        ("ALCATEL-ENT1-VM-SNOOPING-MIB", "alaVMSnoopingNiSlot"),
        ("ALCATEL-ENT1-VM-SNOOPING-MIB", "alaVMSnoopingHwResourceTotal"),
        ("ALCATEL-ENT1-VM-SNOOPING-MIB", "alaVMSnoopingHwResourceUsed"))
)
if mibBuilder.loadTexts:
    alaVMSnoopingReservedHwResourceLimitAlert.setStatus(
        "current"
    )


# Notifications groups

alaVMSnoopingNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 84, 1, 2, 1, 7)
)
alaVMSnoopingNotificationGroup.setObjects(
      *(("ALCATEL-ENT1-VM-SNOOPING-MIB", "alaVMSnoopingVMLearntAlert"),
        ("ALCATEL-ENT1-VM-SNOOPING-MIB", "alaVMSnoopingVMRemovedAlert"),
        ("ALCATEL-ENT1-VM-SNOOPING-MIB", "alaVMSnoopingReservedHwResourceLimitAlert"))
)
if mibBuilder.loadTexts:
    alaVMSnoopingNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

alaVMSnoopingMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 84, 1, 2, 2, 1)
)
alaVMSnoopingMIBCompliance.setObjects(
      *(("ALCATEL-ENT1-VM-SNOOPING-MIB", "alaVMSnoopingConfigGroup"),
        ("ALCATEL-ENT1-VM-SNOOPING-MIB", "alaVMSnoopingUdpPortGroup"),
        ("ALCATEL-ENT1-VM-SNOOPING-MIB", "alaVMSnoopingPortGroup"),
        ("ALCATEL-ENT1-VM-SNOOPING-MIB", "alaVMSnoopingDBGroup"),
        ("ALCATEL-ENT1-VM-SNOOPING-MIB", "alaVMSnoopingHardwareStatsGroup"),
        ("ALCATEL-ENT1-VM-SNOOPING-MIB", "alaVMSnoopingFilterResourceGroup"),
        ("ALCATEL-ENT1-VM-SNOOPING-MIB", "alaVMSnoopingNotificationGroup"),
        ("ALCATEL-ENT1-VM-SNOOPING-MIB", "alaVMSnoopingTrapsObjGroup"),
        ("ALCATEL-ENT1-VM-SNOOPING-MIB", "alaVMSnoopingLearntVMGroup"),
        ("ALCATEL-ENT1-VM-SNOOPING-MIB", "alaVMSnoopingStaticPolicyGroup"))
)
if mibBuilder.loadTexts:
    alaVMSnoopingMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALCATEL-ENT1-VM-SNOOPING-MIB",
    **{"alaVMSnoopingMIB": alaVMSnoopingMIB,
       "alaVMSnoopingMIBNotifications": alaVMSnoopingMIBNotifications,
       "alaVMSnoopingVMLearntAlert": alaVMSnoopingVMLearntAlert,
       "alaVMSnoopingVMRemovedAlert": alaVMSnoopingVMRemovedAlert,
       "alaVMSnoopingReservedHwResourceLimitAlert": alaVMSnoopingReservedHwResourceLimitAlert,
       "alaVMSnoopingMIBObjects": alaVMSnoopingMIBObjects,
       "alaVMSnoopingTrapsObj": alaVMSnoopingTrapsObj,
       "alaVMSnoopingLearnedMacAddress": alaVMSnoopingLearnedMacAddress,
       "alaVMSnoopingLearnedVxlanUdpPort": alaVMSnoopingLearnedVxlanUdpPort,
       "alaVMSnoopingLearnedVxlanVni": alaVMSnoopingLearnedVxlanVni,
       "alaVMSnoopingNiSlot": alaVMSnoopingNiSlot,
       "alaVMSnoopingHwResourceTotal": alaVMSnoopingHwResourceTotal,
       "alaVMSnoopingHwResourceUsed": alaVMSnoopingHwResourceUsed,
       "alaVMSnoopingChassisId": alaVMSnoopingChassisId,
       "alaVMSnoopingConfig": alaVMSnoopingConfig,
       "alaVMSnoopingAdminStatus": alaVMSnoopingAdminStatus,
       "alaVMSnoopingPolicyMode": alaVMSnoopingPolicyMode,
       "alaVMSnoopingPolicyResource": alaVMSnoopingPolicyResource,
       "alaVMSnoopingVMTrafficTagged": alaVMSnoopingVMTrafficTagged,
       "alaVMSnoopingTrapStatus": alaVMSnoopingTrapStatus,
       "alaVMSnoopingSamplingRate": alaVMSnoopingSamplingRate,
       "alaVMSnoopingAgingTimer": alaVMSnoopingAgingTimer,
       "alaVMSnoopingFilteringResourceTrapThreshold": alaVMSnoopingFilteringResourceTrapThreshold,
       "alaVMSnoopingClearAllData": alaVMSnoopingClearAllData,
       "alaVMSnoopingLoggingThresholdFlows": alaVMSnoopingLoggingThresholdFlows,
       "alaVMSnoopingQosAllocationStatus": alaVMSnoopingQosAllocationStatus,
       "alaVMSnoopingUdpPortTable": alaVMSnoopingUdpPortTable,
       "alaVMSnoopingUdpPortEntry": alaVMSnoopingUdpPortEntry,
       "alaVMSnoopingUdpPortIndex": alaVMSnoopingUdpPortIndex,
       "alaVMSnoopingUdpRowStatus": alaVMSnoopingUdpRowStatus,
       "alaVMSnoopingPortTable": alaVMSnoopingPortTable,
       "alaVMSnoopingPortEntry": alaVMSnoopingPortEntry,
       "alaVMSnoopingPortIndex": alaVMSnoopingPortIndex,
       "alaVMSnoopingPortAdminStatus": alaVMSnoopingPortAdminStatus,
       "alaVMSnoopingPortIsVNP": alaVMSnoopingPortIsVNP,
       "alaVMSnoopingPortRowStatus": alaVMSnoopingPortRowStatus,
       "alaVMSnoopingPortDBClear": alaVMSnoopingPortDBClear,
       "alaVMSnoopingPortSamplingClearStats": alaVMSnoopingPortSamplingClearStats,
       "alaVMSnoopingDBTable": alaVMSnoopingDBTable,
       "alaVMSnoopingDBEntry": alaVMSnoopingDBEntry,
       "alaVMSnoopingDBFlowId": alaVMSnoopingDBFlowId,
       "alaVMSnoopingDBIfIndex": alaVMSnoopingDBIfIndex,
       "alaVMSnoopingDBVxlanUdpDestPort": alaVMSnoopingDBVxlanUdpDestPort,
       "alaVMSnoopingDBVni": alaVMSnoopingDBVni,
       "alaVMSnoopingDBVtepVlan": alaVMSnoopingDBVtepVlan,
       "alaVMSnoopingDBVtepSrcIpAddrType": alaVMSnoopingDBVtepSrcIpAddrType,
       "alaVMSnoopingDBVtepSrcIpAddr": alaVMSnoopingDBVtepSrcIpAddr,
       "alaVMSnoopingDBVtepDestIpAddrType": alaVMSnoopingDBVtepDestIpAddrType,
       "alaVMSnoopingDBVtepDestIpAddr": alaVMSnoopingDBVtepDestIpAddr,
       "alaVMSnoopingDBInnerSrcMacAddr": alaVMSnoopingDBInnerSrcMacAddr,
       "alaVMSnoopingDBInnerDestMacAddr": alaVMSnoopingDBInnerDestMacAddr,
       "alaVMSnoopingDBInnerVlan": alaVMSnoopingDBInnerVlan,
       "alaVMSnoopingDBInnerSrcIpAddrType": alaVMSnoopingDBInnerSrcIpAddrType,
       "alaVMSnoopingDBInnerSrcIpAddr": alaVMSnoopingDBInnerSrcIpAddr,
       "alaVMSnoopingDBInnerDestIpAddrType": alaVMSnoopingDBInnerDestIpAddrType,
       "alaVMSnoopingDBInnerDestIpAddr": alaVMSnoopingDBInnerDestIpAddr,
       "alaVMSnoopingDBVInnerL4SrcPort": alaVMSnoopingDBVInnerL4SrcPort,
       "alaVMSnoopingDBVInnerL4DestPort": alaVMSnoopingDBVInnerL4DestPort,
       "alaVMSnoopingDBVInnerIPProtocol": alaVMSnoopingDBVInnerIPProtocol,
       "alaVMSnoopingDBPolicyRule": alaVMSnoopingDBPolicyRule,
       "alaVMSnoopingDBPolicyList": alaVMSnoopingDBPolicyList,
       "alaVMSnoopingDBSamplingStatsPackets": alaVMSnoopingDBSamplingStatsPackets,
       "alaVMSnoopingHardwareStatsTable": alaVMSnoopingHardwareStatsTable,
       "alaVMSnoopingHardwareStatsEntry": alaVMSnoopingHardwareStatsEntry,
       "alaVMSnoopingHardwareStatsIndex": alaVMSnoopingHardwareStatsIndex,
       "alaVMSnoopingHardwareStatsPolicylist": alaVMSnoopingHardwareStatsPolicylist,
       "alaVMSnoopingHardwareStatsPolicyrule": alaVMSnoopingHardwareStatsPolicyrule,
       "alaVMSnoopingHardwareStatsNumOfPackets": alaVMSnoopingHardwareStatsNumOfPackets,
       "alaVMSnoopingHardwareStatsNumOfBytes": alaVMSnoopingHardwareStatsNumOfBytes,
       "alaVMSnoopingFilterResourceTable": alaVMSnoopingFilterResourceTable,
       "alaVMSnoopingFilterResourceEntry": alaVMSnoopingFilterResourceEntry,
       "alaVMSnoopingFilterResourceChassisId": alaVMSnoopingFilterResourceChassisId,
       "alaVMSnoopingFilterResourceSlotNum": alaVMSnoopingFilterResourceSlotNum,
       "alaVMSnoopingFilterResourceMax": alaVMSnoopingFilterResourceMax,
       "alaVMSnoopingFilterResourceUsed": alaVMSnoopingFilterResourceUsed,
       "alaVMSnoopingLearntVMTable": alaVMSnoopingLearntVMTable,
       "alaVMSnoopingLearntVMEntry": alaVMSnoopingLearntVMEntry,
       "alaVMSnoopingLearntVMIfIndex": alaVMSnoopingLearntVMIfIndex,
       "alaVMSnoopingLearntVMSrcMac": alaVMSnoopingLearntVMSrcMac,
       "alaVMSnoopingLearntVMVlanId": alaVMSnoopingLearntVMVlanId,
       "alaVMSnoopingStaticPolicyTable": alaVMSnoopingStaticPolicyTable,
       "alaVMSnoopingStaticPolicyEntry": alaVMSnoopingStaticPolicyEntry,
       "alaVMSnoopingStaticPolicyRuleName": alaVMSnoopingStaticPolicyRuleName,
       "alaVMSnoopingStaticPolicyListName": alaVMSnoopingStaticPolicyListName,
       "alaVMSnoopingStaticPolicyRowStatus": alaVMSnoopingStaticPolicyRowStatus,
       "alaVMSnoopingMIBConformance": alaVMSnoopingMIBConformance,
       "alaVMSnoopingMIBGroups": alaVMSnoopingMIBGroups,
       "alaVMSnoopingConfigGroup": alaVMSnoopingConfigGroup,
       "alaVMSnoopingUdpPortGroup": alaVMSnoopingUdpPortGroup,
       "alaVMSnoopingPortGroup": alaVMSnoopingPortGroup,
       "alaVMSnoopingDBGroup": alaVMSnoopingDBGroup,
       "alaVMSnoopingHardwareStatsGroup": alaVMSnoopingHardwareStatsGroup,
       "alaVMSnoopingFilterResourceGroup": alaVMSnoopingFilterResourceGroup,
       "alaVMSnoopingNotificationGroup": alaVMSnoopingNotificationGroup,
       "alaVMSnoopingTrapsObjGroup": alaVMSnoopingTrapsObjGroup,
       "alaVMSnoopingLearntVMGroup": alaVMSnoopingLearntVMGroup,
       "alaVMSnoopingStaticPolicyGroup": alaVMSnoopingStaticPolicyGroup,
       "alaVMSnoopingMIBCompliances": alaVMSnoopingMIBCompliances,
       "alaVMSnoopingMIBCompliance": alaVMSnoopingMIBCompliance}
)
