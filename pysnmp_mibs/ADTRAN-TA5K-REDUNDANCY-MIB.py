# SNMP MIB module (ADTRAN-TA5K-REDUNDANCY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/adtran/ADTRAN-TA5K-REDUNDANCY-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:31:16 2025
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

(adGenSlotInfoIndex,) = mibBuilder.importSymbols(
    "ADTRAN-GENSLOT-MIB",
    "adGenSlotInfoIndex")

(adGenTa5kRedundancy,
 adGenTa5kRedundancyID) = mibBuilder.importSymbols(
    "ADTRAN-GENTA5K-MIB",
    "adGenTa5kRedundancy",
    "adGenTa5kRedundancyID")

(adTrapInformSeqNum,) = mibBuilder.importSymbols(
    "ADTRAN-GENTRAPINFORM-MIB",
    "adTrapInformSeqNum")

(adIdentity,
 adIdentityShared,
 adMgmt,
 adProducts) = mibBuilder.importSymbols(
    "ADTRAN-MIB",
    "adIdentity",
    "adIdentityShared",
    "adMgmt",
    "adProducts")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(sysName,) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysName")

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

(DisplayString,
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

adTa5kRedundancyModuleIdentity = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 67, 1, 1, 1)
)
if mibBuilder.loadTexts:
    adTa5kRedundancyModuleIdentity.setRevisions(
        ("2011-10-12 14:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AdTa5kEquipmentRedundancy_ObjectIdentity = ObjectIdentity
adTa5kEquipmentRedundancy = _AdTa5kEquipmentRedundancy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 1, 1)
)
_AdTa5kEquipmentRedundancyTable_Object = MibTable
adTa5kEquipmentRedundancyTable = _AdTa5kEquipmentRedundancyTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    adTa5kEquipmentRedundancyTable.setStatus("current")
_AdTa5kEquipmentRedundancyEntry_Object = MibTableRow
adTa5kEquipmentRedundancyEntry = _AdTa5kEquipmentRedundancyEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 1, 1, 1, 1)
)
adTa5kEquipmentRedundancyEntry.setIndexNames(
    (0, "ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
)
if mibBuilder.loadTexts:
    adTa5kEquipmentRedundancyEntry.setStatus("current")


class _AdTa5kEquipmentRedundancySupported_Type(Integer32):
    """Custom type adTa5kEquipmentRedundancySupported based on Integer32"""
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
        *(("true", 1),
          ("peerNotResponding", 2),
          ("peerIncompatible", 3),
          ("peerNotPresent", 4),
          ("peerNotReady", 5))
    )


_AdTa5kEquipmentRedundancySupported_Type.__name__ = "Integer32"
_AdTa5kEquipmentRedundancySupported_Object = MibTableColumn
adTa5kEquipmentRedundancySupported = _AdTa5kEquipmentRedundancySupported_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 1, 1, 1, 1, 1),
    _AdTa5kEquipmentRedundancySupported_Type()
)
adTa5kEquipmentRedundancySupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTa5kEquipmentRedundancySupported.setStatus("current")


class _AdTa5kEquipmentRedundancyRevertive_Type(Integer32):
    """Custom type adTa5kEquipmentRedundancyRevertive based on Integer32"""
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


_AdTa5kEquipmentRedundancyRevertive_Type.__name__ = "Integer32"
_AdTa5kEquipmentRedundancyRevertive_Object = MibTableColumn
adTa5kEquipmentRedundancyRevertive = _AdTa5kEquipmentRedundancyRevertive_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 1, 1, 1, 1, 2),
    _AdTa5kEquipmentRedundancyRevertive_Type()
)
adTa5kEquipmentRedundancyRevertive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTa5kEquipmentRedundancyRevertive.setStatus("current")
_AdTa5kEquipmentRedundancyRevertiveTimeout_Type = Integer32
_AdTa5kEquipmentRedundancyRevertiveTimeout_Object = MibTableColumn
adTa5kEquipmentRedundancyRevertiveTimeout = _AdTa5kEquipmentRedundancyRevertiveTimeout_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 1, 1, 1, 1, 3),
    _AdTa5kEquipmentRedundancyRevertiveTimeout_Type()
)
adTa5kEquipmentRedundancyRevertiveTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTa5kEquipmentRedundancyRevertiveTimeout.setStatus("current")


class _AdTa5kEquipmentRedundancyForceFailover_Type(Integer32):
    """Custom type adTa5kEquipmentRedundancyForceFailover based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("failover", 1),
          ("notapplicable", 2))
    )


_AdTa5kEquipmentRedundancyForceFailover_Type.__name__ = "Integer32"
_AdTa5kEquipmentRedundancyForceFailover_Object = MibTableColumn
adTa5kEquipmentRedundancyForceFailover = _AdTa5kEquipmentRedundancyForceFailover_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 1, 1, 1, 1, 4),
    _AdTa5kEquipmentRedundancyForceFailover_Type()
)
adTa5kEquipmentRedundancyForceFailover.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTa5kEquipmentRedundancyForceFailover.setStatus("current")


class _AdTa5kEquipmentRedundancyState_Type(Integer32):
    """Custom type adTa5kEquipmentRedundancyState based on Integer32"""
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
        *(("active", 1),
          ("standby", 2),
          ("standbyNotReady", 3),
          ("notApplicable", 4))
    )


_AdTa5kEquipmentRedundancyState_Type.__name__ = "Integer32"
_AdTa5kEquipmentRedundancyState_Object = MibTableColumn
adTa5kEquipmentRedundancyState = _AdTa5kEquipmentRedundancyState_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 1, 1, 1, 1, 5),
    _AdTa5kEquipmentRedundancyState_Type()
)
adTa5kEquipmentRedundancyState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTa5kEquipmentRedundancyState.setStatus("current")
_AdTa5kEquipmentRedundancyPeerSlot_Type = Integer32
_AdTa5kEquipmentRedundancyPeerSlot_Object = MibTableColumn
adTa5kEquipmentRedundancyPeerSlot = _AdTa5kEquipmentRedundancyPeerSlot_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 1, 1, 1, 1, 6),
    _AdTa5kEquipmentRedundancyPeerSlot_Type()
)
adTa5kEquipmentRedundancyPeerSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTa5kEquipmentRedundancyPeerSlot.setStatus("current")


class _AdTa5kEquipmentRedundancyFeatureEnabled_Type(Integer32):
    """Custom type adTa5kEquipmentRedundancyFeatureEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_AdTa5kEquipmentRedundancyFeatureEnabled_Type.__name__ = "Integer32"
_AdTa5kEquipmentRedundancyFeatureEnabled_Object = MibTableColumn
adTa5kEquipmentRedundancyFeatureEnabled = _AdTa5kEquipmentRedundancyFeatureEnabled_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 1, 1, 1, 1, 7),
    _AdTa5kEquipmentRedundancyFeatureEnabled_Type()
)
adTa5kEquipmentRedundancyFeatureEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTa5kEquipmentRedundancyFeatureEnabled.setStatus("current")


class _AdTa5kEquipmentRedundancyFacilityType_Type(Integer32):
    """Custom type adTa5kEquipmentRedundancyFacilityType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("sharedFacilities", 0),
          ("dualFacilities", 1),
          ("separateFacilities", 2))
    )


_AdTa5kEquipmentRedundancyFacilityType_Type.__name__ = "Integer32"
_AdTa5kEquipmentRedundancyFacilityType_Object = MibTableColumn
adTa5kEquipmentRedundancyFacilityType = _AdTa5kEquipmentRedundancyFacilityType_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 1, 1, 1, 1, 8),
    _AdTa5kEquipmentRedundancyFacilityType_Type()
)
adTa5kEquipmentRedundancyFacilityType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTa5kEquipmentRedundancyFacilityType.setStatus("current")
_AdTa5kEquipmentRedundancyStandbyReasonsCount_Type = Integer32
_AdTa5kEquipmentRedundancyStandbyReasonsCount_Object = MibTableColumn
adTa5kEquipmentRedundancyStandbyReasonsCount = _AdTa5kEquipmentRedundancyStandbyReasonsCount_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 1, 1, 1, 1, 9),
    _AdTa5kEquipmentRedundancyStandbyReasonsCount_Type()
)
adTa5kEquipmentRedundancyStandbyReasonsCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTa5kEquipmentRedundancyStandbyReasonsCount.setStatus("current")
_AdTa5kStandbyNotReadyReasonsTable_Object = MibTable
adTa5kStandbyNotReadyReasonsTable = _AdTa5kStandbyNotReadyReasonsTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 1, 1, 3)
)
if mibBuilder.loadTexts:
    adTa5kStandbyNotReadyReasonsTable.setStatus("current")
_AdTa5kStandbyNotReadyReasonEntry_Object = MibTableRow
adTa5kStandbyNotReadyReasonEntry = _AdTa5kStandbyNotReadyReasonEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 1, 1, 3, 1)
)
adTa5kStandbyNotReadyReasonEntry.setIndexNames(
    (0, "ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
    (0, "ADTRAN-TA5K-REDUNDANCY-MIB", "adTa5kStandbyNotReadyReasonIndex"),
)
if mibBuilder.loadTexts:
    adTa5kStandbyNotReadyReasonEntry.setStatus("current")
_AdTa5kStandbyNotReadyReasonIndex_Type = Integer32
_AdTa5kStandbyNotReadyReasonIndex_Object = MibTableColumn
adTa5kStandbyNotReadyReasonIndex = _AdTa5kStandbyNotReadyReasonIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 1, 1, 3, 1, 1),
    _AdTa5kStandbyNotReadyReasonIndex_Type()
)
adTa5kStandbyNotReadyReasonIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adTa5kStandbyNotReadyReasonIndex.setStatus("current")
_AdTa5kStandbyNotReadyReason_Type = DisplayString
_AdTa5kStandbyNotReadyReason_Object = MibTableColumn
adTa5kStandbyNotReadyReason = _AdTa5kStandbyNotReadyReason_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 1, 1, 3, 1, 2),
    _AdTa5kStandbyNotReadyReason_Type()
)
adTa5kStandbyNotReadyReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTa5kStandbyNotReadyReason.setStatus("current")
_AdTa5kFacilityRedundancy_ObjectIdentity = ObjectIdentity
adTa5kFacilityRedundancy = _AdTa5kFacilityRedundancy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 1, 2)
)
_AdTa5kFacilityRedundancyTable_Object = MibTable
adTa5kFacilityRedundancyTable = _AdTa5kFacilityRedundancyTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    adTa5kFacilityRedundancyTable.setStatus("current")
_AdTa5kFacilityRedundancyEntry_Object = MibTableRow
adTa5kFacilityRedundancyEntry = _AdTa5kFacilityRedundancyEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 1, 2, 1, 1)
)
adTa5kFacilityRedundancyEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adTa5kFacilityRedundancyEntry.setStatus("current")


class _AdTa5kFacilityRedundancySupported_Type(Integer32):
    """Custom type adTa5kFacilityRedundancySupported based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("protected", 1),
          ("redundantFacilityNotPresent", 2),
          ("redundantFacilityNotCompatible", 3),
          ("redundantFacilityAdminDown", 4),
          ("redundantFacilityLinkDown", 5),
          ("redundantFacilityInUse", 6),
          ("redundantEquipmentAdminDown", 7))
    )


_AdTa5kFacilityRedundancySupported_Type.__name__ = "Integer32"
_AdTa5kFacilityRedundancySupported_Object = MibTableColumn
adTa5kFacilityRedundancySupported = _AdTa5kFacilityRedundancySupported_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 1, 2, 1, 1, 1),
    _AdTa5kFacilityRedundancySupported_Type()
)
adTa5kFacilityRedundancySupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTa5kFacilityRedundancySupported.setStatus("current")


class _AdTa5kFacilityRedundancyState_Type(Integer32):
    """Custom type adTa5kFacilityRedundancyState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("standby", 2))
    )


_AdTa5kFacilityRedundancyState_Type.__name__ = "Integer32"
_AdTa5kFacilityRedundancyState_Object = MibTableColumn
adTa5kFacilityRedundancyState = _AdTa5kFacilityRedundancyState_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 1, 2, 1, 1, 2),
    _AdTa5kFacilityRedundancyState_Type()
)
adTa5kFacilityRedundancyState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTa5kFacilityRedundancyState.setStatus("current")
_AdTa5kFacilityRedundancyForceProtect_Type = Integer32
_AdTa5kFacilityRedundancyForceProtect_Object = MibTableColumn
adTa5kFacilityRedundancyForceProtect = _AdTa5kFacilityRedundancyForceProtect_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 1, 2, 1, 1, 3),
    _AdTa5kFacilityRedundancyForceProtect_Type()
)
adTa5kFacilityRedundancyForceProtect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTa5kFacilityRedundancyForceProtect.setStatus("current")
_AdTa5kFacilityRedundancyProtectedByIfIndex_Type = Integer32
_AdTa5kFacilityRedundancyProtectedByIfIndex_Object = MibTableColumn
adTa5kFacilityRedundancyProtectedByIfIndex = _AdTa5kFacilityRedundancyProtectedByIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 1, 2, 1, 1, 4),
    _AdTa5kFacilityRedundancyProtectedByIfIndex_Type()
)
adTa5kFacilityRedundancyProtectedByIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTa5kFacilityRedundancyProtectedByIfIndex.setStatus("current")
_AdTa5kRedundancyAlarmPrefix_ObjectIdentity = ObjectIdentity
adTa5kRedundancyAlarmPrefix = _AdTa5kRedundancyAlarmPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 1, 3)
)
_AdTa5kRedundancyAlarms_ObjectIdentity = ObjectIdentity
adTa5kRedundancyAlarms = _AdTa5kRedundancyAlarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 1, 3, 0)
)
_AdTa5kRedundancyAlarmProv_ObjectIdentity = ObjectIdentity
adTa5kRedundancyAlarmProv = _AdTa5kRedundancyAlarmProv_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 1, 4)
)
_AdTa5kRedundancyAlarmProvTable_Object = MibTable
adTa5kRedundancyAlarmProvTable = _AdTa5kRedundancyAlarmProvTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 1, 4, 1)
)
if mibBuilder.loadTexts:
    adTa5kRedundancyAlarmProvTable.setStatus("current")
_AdTa5kRedundancyAlarmProvEntry_Object = MibTableRow
adTa5kRedundancyAlarmProvEntry = _AdTa5kRedundancyAlarmProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 1, 4, 1, 1)
)
adTa5kRedundancyAlarmProvEntry.setIndexNames(
    (0, "ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
)
if mibBuilder.loadTexts:
    adTa5kRedundancyAlarmProvEntry.setStatus("current")


class _AdTa5kRedundancyAlarmProvCardActiveEnable_Type(TruthValue):
    """Custom type adTa5kRedundancyAlarmProvCardActiveEnable based on TruthValue"""
    defaultValue = 1


_AdTa5kRedundancyAlarmProvCardActiveEnable_Type.__name__ = "TruthValue"
_AdTa5kRedundancyAlarmProvCardActiveEnable_Object = MibTableColumn
adTa5kRedundancyAlarmProvCardActiveEnable = _AdTa5kRedundancyAlarmProvCardActiveEnable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 1, 4, 1, 1, 1),
    _AdTa5kRedundancyAlarmProvCardActiveEnable_Type()
)
adTa5kRedundancyAlarmProvCardActiveEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTa5kRedundancyAlarmProvCardActiveEnable.setStatus("current")


class _AdTa5kRedundancyAlarmProvProtectionUnavailableEnable_Type(TruthValue):
    """Custom type adTa5kRedundancyAlarmProvProtectionUnavailableEnable based on TruthValue"""
    defaultValue = 1


_AdTa5kRedundancyAlarmProvProtectionUnavailableEnable_Type.__name__ = "TruthValue"
_AdTa5kRedundancyAlarmProvProtectionUnavailableEnable_Object = MibTableColumn
adTa5kRedundancyAlarmProvProtectionUnavailableEnable = _AdTa5kRedundancyAlarmProvProtectionUnavailableEnable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 1, 4, 1, 1, 2),
    _AdTa5kRedundancyAlarmProvProtectionUnavailableEnable_Type()
)
adTa5kRedundancyAlarmProvProtectionUnavailableEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTa5kRedundancyAlarmProvProtectionUnavailableEnable.setStatus("current")


class _AdTa5kRedundancyAlarmProvPeerCodeVersionMismatchEnable_Type(TruthValue):
    """Custom type adTa5kRedundancyAlarmProvPeerCodeVersionMismatchEnable based on TruthValue"""
    defaultValue = 1


_AdTa5kRedundancyAlarmProvPeerCodeVersionMismatchEnable_Type.__name__ = "TruthValue"
_AdTa5kRedundancyAlarmProvPeerCodeVersionMismatchEnable_Object = MibTableColumn
adTa5kRedundancyAlarmProvPeerCodeVersionMismatchEnable = _AdTa5kRedundancyAlarmProvPeerCodeVersionMismatchEnable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 1, 4, 1, 1, 3),
    _AdTa5kRedundancyAlarmProvPeerCodeVersionMismatchEnable_Type()
)
adTa5kRedundancyAlarmProvPeerCodeVersionMismatchEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTa5kRedundancyAlarmProvPeerCodeVersionMismatchEnable.setStatus("current")


class _AdTa5kRedundancyAlarmProvPeerDbMirroringSyncInProgressEnable_Type(TruthValue):
    """Custom type adTa5kRedundancyAlarmProvPeerDbMirroringSyncInProgressEnable based on TruthValue"""
    defaultValue = 1


_AdTa5kRedundancyAlarmProvPeerDbMirroringSyncInProgressEnable_Type.__name__ = "TruthValue"
_AdTa5kRedundancyAlarmProvPeerDbMirroringSyncInProgressEnable_Object = MibTableColumn
adTa5kRedundancyAlarmProvPeerDbMirroringSyncInProgressEnable = _AdTa5kRedundancyAlarmProvPeerDbMirroringSyncInProgressEnable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 1, 4, 1, 1, 4),
    _AdTa5kRedundancyAlarmProvPeerDbMirroringSyncInProgressEnable_Type()
)
adTa5kRedundancyAlarmProvPeerDbMirroringSyncInProgressEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTa5kRedundancyAlarmProvPeerDbMirroringSyncInProgressEnable.setStatus("current")


class _AdTa5kRedundancyAlarmProvPeerRemoteDatabaseSyncInProgressEnable_Type(TruthValue):
    """Custom type adTa5kRedundancyAlarmProvPeerRemoteDatabaseSyncInProgressEnable based on TruthValue"""
    defaultValue = 1


_AdTa5kRedundancyAlarmProvPeerRemoteDatabaseSyncInProgressEnable_Type.__name__ = "TruthValue"
_AdTa5kRedundancyAlarmProvPeerRemoteDatabaseSyncInProgressEnable_Object = MibTableColumn
adTa5kRedundancyAlarmProvPeerRemoteDatabaseSyncInProgressEnable = _AdTa5kRedundancyAlarmProvPeerRemoteDatabaseSyncInProgressEnable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 1, 4, 1, 1, 5),
    _AdTa5kRedundancyAlarmProvPeerRemoteDatabaseSyncInProgressEnable_Type()
)
adTa5kRedundancyAlarmProvPeerRemoteDatabaseSyncInProgressEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTa5kRedundancyAlarmProvPeerRemoteDatabaseSyncInProgressEnable.setStatus("current")


class _AdTa5kRedundancyAlarmProvManualSwitchEnable_Type(TruthValue):
    """Custom type adTa5kRedundancyAlarmProvManualSwitchEnable based on TruthValue"""
    defaultValue = 1


_AdTa5kRedundancyAlarmProvManualSwitchEnable_Type.__name__ = "TruthValue"
_AdTa5kRedundancyAlarmProvManualSwitchEnable_Object = MibTableColumn
adTa5kRedundancyAlarmProvManualSwitchEnable = _AdTa5kRedundancyAlarmProvManualSwitchEnable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 1, 4, 1, 1, 6),
    _AdTa5kRedundancyAlarmProvManualSwitchEnable_Type()
)
adTa5kRedundancyAlarmProvManualSwitchEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTa5kRedundancyAlarmProvManualSwitchEnable.setStatus("current")


class _AdTa5kRedundancyAlarmProvSwitchToProtectEnable_Type(TruthValue):
    """Custom type adTa5kRedundancyAlarmProvSwitchToProtectEnable based on TruthValue"""
    defaultValue = 1


_AdTa5kRedundancyAlarmProvSwitchToProtectEnable_Type.__name__ = "TruthValue"
_AdTa5kRedundancyAlarmProvSwitchToProtectEnable_Object = MibTableColumn
adTa5kRedundancyAlarmProvSwitchToProtectEnable = _AdTa5kRedundancyAlarmProvSwitchToProtectEnable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 1, 4, 1, 1, 7),
    _AdTa5kRedundancyAlarmProvSwitchToProtectEnable_Type()
)
adTa5kRedundancyAlarmProvSwitchToProtectEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTa5kRedundancyAlarmProvSwitchToProtectEnable.setStatus("current")


class _AdTa5kRedundancyAlarmProvAutomaticSwitchEnable_Type(TruthValue):
    """Custom type adTa5kRedundancyAlarmProvAutomaticSwitchEnable based on TruthValue"""
    defaultValue = 1


_AdTa5kRedundancyAlarmProvAutomaticSwitchEnable_Type.__name__ = "TruthValue"
_AdTa5kRedundancyAlarmProvAutomaticSwitchEnable_Object = MibTableColumn
adTa5kRedundancyAlarmProvAutomaticSwitchEnable = _AdTa5kRedundancyAlarmProvAutomaticSwitchEnable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 1, 4, 1, 1, 8),
    _AdTa5kRedundancyAlarmProvAutomaticSwitchEnable_Type()
)
adTa5kRedundancyAlarmProvAutomaticSwitchEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTa5kRedundancyAlarmProvAutomaticSwitchEnable.setStatus("current")

# Managed Objects groups


# Notification objects

adTa5kRedundancyCardActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 1, 3, 0, 1)
)
adTa5kRedundancyCardActive.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"))
)
if mibBuilder.loadTexts:
    adTa5kRedundancyCardActive.setStatus(
        "current"
    )

adTa5kRedundancyProtectionAvailable = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 1, 3, 0, 2)
)
adTa5kRedundancyProtectionAvailable.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"))
)
if mibBuilder.loadTexts:
    adTa5kRedundancyProtectionAvailable.setStatus(
        "current"
    )

adTa5kRedundancyProtectionUnavailable = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 1, 3, 0, 3)
)
adTa5kRedundancyProtectionUnavailable.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"))
)
if mibBuilder.loadTexts:
    adTa5kRedundancyProtectionUnavailable.setStatus(
        "current"
    )

adTa5kRedundancyPeerCodeVersionMismatchClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 1, 3, 0, 4)
)
adTa5kRedundancyPeerCodeVersionMismatchClear.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"))
)
if mibBuilder.loadTexts:
    adTa5kRedundancyPeerCodeVersionMismatchClear.setStatus(
        "current"
    )

adTa5kRedundancyPeerCodeVersionMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 1, 3, 0, 5)
)
adTa5kRedundancyPeerCodeVersionMismatch.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"))
)
if mibBuilder.loadTexts:
    adTa5kRedundancyPeerCodeVersionMismatch.setStatus(
        "current"
    )

adTa5kRedundancyPeerDatabaseMirroringInSync = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 1, 3, 0, 6)
)
adTa5kRedundancyPeerDatabaseMirroringInSync.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"))
)
if mibBuilder.loadTexts:
    adTa5kRedundancyPeerDatabaseMirroringInSync.setStatus(
        "current"
    )

adTa5kRedundancyPeerDbMirroringSyncInProgress = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 1, 3, 0, 7)
)
adTa5kRedundancyPeerDbMirroringSyncInProgress.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"))
)
if mibBuilder.loadTexts:
    adTa5kRedundancyPeerDbMirroringSyncInProgress.setStatus(
        "current"
    )

adTa5kRedundancyPeerRemoteDatabaseSyncInProgress = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 1, 3, 0, 8)
)
adTa5kRedundancyPeerRemoteDatabaseSyncInProgress.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"))
)
if mibBuilder.loadTexts:
    adTa5kRedundancyPeerRemoteDatabaseSyncInProgress.setStatus(
        "current"
    )

adTa5kRedundancyPeerRemoteDatabaseInSync = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 1, 3, 0, 9)
)
adTa5kRedundancyPeerRemoteDatabaseInSync.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"))
)
if mibBuilder.loadTexts:
    adTa5kRedundancyPeerRemoteDatabaseInSync.setStatus(
        "current"
    )

adTa5kRedundancyManualSwitch = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 1, 3, 0, 10)
)
adTa5kRedundancyManualSwitch.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"))
)
if mibBuilder.loadTexts:
    adTa5kRedundancyManualSwitch.setStatus(
        "current"
    )

adTa5kEquipmentRedundancySwitchToProtectClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 1, 3, 0, 12)
)
adTa5kEquipmentRedundancySwitchToProtectClear.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"))
)
if mibBuilder.loadTexts:
    adTa5kEquipmentRedundancySwitchToProtectClear.setStatus(
        "current"
    )

adTa5kEquipmentRedundancySwitchToProtect = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 1, 3, 0, 13)
)
adTa5kEquipmentRedundancySwitchToProtect.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"))
)
if mibBuilder.loadTexts:
    adTa5kEquipmentRedundancySwitchToProtect.setStatus(
        "current"
    )

adTa5kRedundancyAutomaticSwitch = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 1, 3, 0, 14)
)
adTa5kRedundancyAutomaticSwitch.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"))
)
if mibBuilder.loadTexts:
    adTa5kRedundancyAutomaticSwitch.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ADTRAN-TA5K-REDUNDANCY-MIB",
    **{"adTa5kEquipmentRedundancy": adTa5kEquipmentRedundancy,
       "adTa5kEquipmentRedundancyTable": adTa5kEquipmentRedundancyTable,
       "adTa5kEquipmentRedundancyEntry": adTa5kEquipmentRedundancyEntry,
       "adTa5kEquipmentRedundancySupported": adTa5kEquipmentRedundancySupported,
       "adTa5kEquipmentRedundancyRevertive": adTa5kEquipmentRedundancyRevertive,
       "adTa5kEquipmentRedundancyRevertiveTimeout": adTa5kEquipmentRedundancyRevertiveTimeout,
       "adTa5kEquipmentRedundancyForceFailover": adTa5kEquipmentRedundancyForceFailover,
       "adTa5kEquipmentRedundancyState": adTa5kEquipmentRedundancyState,
       "adTa5kEquipmentRedundancyPeerSlot": adTa5kEquipmentRedundancyPeerSlot,
       "adTa5kEquipmentRedundancyFeatureEnabled": adTa5kEquipmentRedundancyFeatureEnabled,
       "adTa5kEquipmentRedundancyFacilityType": adTa5kEquipmentRedundancyFacilityType,
       "adTa5kEquipmentRedundancyStandbyReasonsCount": adTa5kEquipmentRedundancyStandbyReasonsCount,
       "adTa5kStandbyNotReadyReasonsTable": adTa5kStandbyNotReadyReasonsTable,
       "adTa5kStandbyNotReadyReasonEntry": adTa5kStandbyNotReadyReasonEntry,
       "adTa5kStandbyNotReadyReasonIndex": adTa5kStandbyNotReadyReasonIndex,
       "adTa5kStandbyNotReadyReason": adTa5kStandbyNotReadyReason,
       "adTa5kFacilityRedundancy": adTa5kFacilityRedundancy,
       "adTa5kFacilityRedundancyTable": adTa5kFacilityRedundancyTable,
       "adTa5kFacilityRedundancyEntry": adTa5kFacilityRedundancyEntry,
       "adTa5kFacilityRedundancySupported": adTa5kFacilityRedundancySupported,
       "adTa5kFacilityRedundancyState": adTa5kFacilityRedundancyState,
       "adTa5kFacilityRedundancyForceProtect": adTa5kFacilityRedundancyForceProtect,
       "adTa5kFacilityRedundancyProtectedByIfIndex": adTa5kFacilityRedundancyProtectedByIfIndex,
       "adTa5kRedundancyAlarmPrefix": adTa5kRedundancyAlarmPrefix,
       "adTa5kRedundancyAlarms": adTa5kRedundancyAlarms,
       "adTa5kRedundancyCardActive": adTa5kRedundancyCardActive,
       "adTa5kRedundancyProtectionAvailable": adTa5kRedundancyProtectionAvailable,
       "adTa5kRedundancyProtectionUnavailable": adTa5kRedundancyProtectionUnavailable,
       "adTa5kRedundancyPeerCodeVersionMismatchClear": adTa5kRedundancyPeerCodeVersionMismatchClear,
       "adTa5kRedundancyPeerCodeVersionMismatch": adTa5kRedundancyPeerCodeVersionMismatch,
       "adTa5kRedundancyPeerDatabaseMirroringInSync": adTa5kRedundancyPeerDatabaseMirroringInSync,
       "adTa5kRedundancyPeerDbMirroringSyncInProgress": adTa5kRedundancyPeerDbMirroringSyncInProgress,
       "adTa5kRedundancyPeerRemoteDatabaseSyncInProgress": adTa5kRedundancyPeerRemoteDatabaseSyncInProgress,
       "adTa5kRedundancyPeerRemoteDatabaseInSync": adTa5kRedundancyPeerRemoteDatabaseInSync,
       "adTa5kRedundancyManualSwitch": adTa5kRedundancyManualSwitch,
       "adTa5kEquipmentRedundancySwitchToProtectClear": adTa5kEquipmentRedundancySwitchToProtectClear,
       "adTa5kEquipmentRedundancySwitchToProtect": adTa5kEquipmentRedundancySwitchToProtect,
       "adTa5kRedundancyAutomaticSwitch": adTa5kRedundancyAutomaticSwitch,
       "adTa5kRedundancyAlarmProv": adTa5kRedundancyAlarmProv,
       "adTa5kRedundancyAlarmProvTable": adTa5kRedundancyAlarmProvTable,
       "adTa5kRedundancyAlarmProvEntry": adTa5kRedundancyAlarmProvEntry,
       "adTa5kRedundancyAlarmProvCardActiveEnable": adTa5kRedundancyAlarmProvCardActiveEnable,
       "adTa5kRedundancyAlarmProvProtectionUnavailableEnable": adTa5kRedundancyAlarmProvProtectionUnavailableEnable,
       "adTa5kRedundancyAlarmProvPeerCodeVersionMismatchEnable": adTa5kRedundancyAlarmProvPeerCodeVersionMismatchEnable,
       "adTa5kRedundancyAlarmProvPeerDbMirroringSyncInProgressEnable": adTa5kRedundancyAlarmProvPeerDbMirroringSyncInProgressEnable,
       "adTa5kRedundancyAlarmProvPeerRemoteDatabaseSyncInProgressEnable": adTa5kRedundancyAlarmProvPeerRemoteDatabaseSyncInProgressEnable,
       "adTa5kRedundancyAlarmProvManualSwitchEnable": adTa5kRedundancyAlarmProvManualSwitchEnable,
       "adTa5kRedundancyAlarmProvSwitchToProtectEnable": adTa5kRedundancyAlarmProvSwitchToProtectEnable,
       "adTa5kRedundancyAlarmProvAutomaticSwitchEnable": adTa5kRedundancyAlarmProvAutomaticSwitchEnable,
       "adTa5kRedundancyModuleIdentity": adTa5kRedundancyModuleIdentity}
)
