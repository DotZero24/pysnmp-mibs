# SNMP MIB module (SUPERMICRO-ERPS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/supermicro/SUPERMICRO-ERPS-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:02:13 2025
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

(Dot1agCfmMepId,) = mibBuilder.importSymbols(
    "IEEE8021-CFM-MIB",
    "Dot1agCfmMepId")

(InterfaceIndex,
 InterfaceIndexOrZero) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero")

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

(VlanId,) = mibBuilder.importSymbols(
    "SUPERMICROQ-BRIDGE-MIB",
    "VlanId")


# MODULE-IDENTITY

fsErpsMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 40)
)
if mibBuilder.loadTexts:
    fsErpsMIB.setRevisions(
        ("2012-09-05 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class RingId(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )



class RingMonitorMechanismType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cfm", 1),
          ("mplsOam", 2))
    )



class RingIdOrNone(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 4294967295),
    )



class RingServiceType(TextualConvention, Integer32):
    status = "current"
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
        *(("vlan", 1),
          ("mplsLSP", 2),
          ("mplsPW", 3),
          ("mplsLSPPW", 4))
    )



# MIB Managed Objects in the order of their OIDs

_FsErpsContext_ObjectIdentity = ObjectIdentity
fsErpsContext = _FsErpsContext_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 40, 1)
)
_FsErpsContextTable_Object = MibTable
fsErpsContextTable = _FsErpsContextTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 40, 1, 1)
)
if mibBuilder.loadTexts:
    fsErpsContextTable.setStatus("current")
_FsErpsContextEntry_Object = MibTableRow
fsErpsContextEntry = _FsErpsContextEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 40, 1, 1, 1)
)
fsErpsContextEntry.setIndexNames(
    (0, "SUPERMICRO-ERPS-MIB", "fsErpsContextId"),
)
if mibBuilder.loadTexts:
    fsErpsContextEntry.setStatus("current")
_FsErpsContextId_Type = Unsigned32
_FsErpsContextId_Object = MibTableColumn
fsErpsContextId = _FsErpsContextId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 40, 1, 1, 1, 1),
    _FsErpsContextId_Type()
)
fsErpsContextId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsErpsContextId.setStatus("current")


class _FsErpsCtxtName_Type(DisplayString):
    """Custom type fsErpsCtxtName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_FsErpsCtxtName_Type.__name__ = "DisplayString"
_FsErpsCtxtName_Object = MibTableColumn
fsErpsCtxtName = _FsErpsCtxtName_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 40, 1, 1, 1, 2),
    _FsErpsCtxtName_Type()
)
fsErpsCtxtName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsErpsCtxtName.setStatus("current")


class _FsErpsCtxtSystemControl_Type(Integer32):
    """Custom type fsErpsCtxtSystemControl based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("start", 1),
          ("shutdown", 2))
    )


_FsErpsCtxtSystemControl_Type.__name__ = "Integer32"
_FsErpsCtxtSystemControl_Object = MibTableColumn
fsErpsCtxtSystemControl = _FsErpsCtxtSystemControl_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 40, 1, 1, 1, 3),
    _FsErpsCtxtSystemControl_Type()
)
fsErpsCtxtSystemControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsErpsCtxtSystemControl.setStatus("current")


class _FsErpsCtxtModuleStatus_Type(Integer32):
    """Custom type fsErpsCtxtModuleStatus based on Integer32"""
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


_FsErpsCtxtModuleStatus_Type.__name__ = "Integer32"
_FsErpsCtxtModuleStatus_Object = MibTableColumn
fsErpsCtxtModuleStatus = _FsErpsCtxtModuleStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 40, 1, 1, 1, 4),
    _FsErpsCtxtModuleStatus_Type()
)
fsErpsCtxtModuleStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsErpsCtxtModuleStatus.setStatus("current")


class _FsErpsCtxtTraceInput_Type(DisplayString):
    """Custom type fsErpsCtxtTraceInput based on DisplayString"""
    defaultValue = OctetString("critical")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_FsErpsCtxtTraceInput_Type.__name__ = "DisplayString"
_FsErpsCtxtTraceInput_Object = MibTableColumn
fsErpsCtxtTraceInput = _FsErpsCtxtTraceInput_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 40, 1, 1, 1, 5),
    _FsErpsCtxtTraceInput_Type()
)
fsErpsCtxtTraceInput.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsErpsCtxtTraceInput.setStatus("current")


class _FsErpsCtxtTrapStatus_Type(Integer32):
    """Custom type fsErpsCtxtTrapStatus based on Integer32"""
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


_FsErpsCtxtTrapStatus_Type.__name__ = "Integer32"
_FsErpsCtxtTrapStatus_Object = MibTableColumn
fsErpsCtxtTrapStatus = _FsErpsCtxtTrapStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 40, 1, 1, 1, 6),
    _FsErpsCtxtTrapStatus_Type()
)
fsErpsCtxtTrapStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsErpsCtxtTrapStatus.setStatus("current")


class _FsErpsCtxtClearRingStats_Type(TruthValue):
    """Custom type fsErpsCtxtClearRingStats based on TruthValue"""
    defaultValue = 2


_FsErpsCtxtClearRingStats_Type.__name__ = "TruthValue"
_FsErpsCtxtClearRingStats_Object = MibTableColumn
fsErpsCtxtClearRingStats = _FsErpsCtxtClearRingStats_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 40, 1, 1, 1, 7),
    _FsErpsCtxtClearRingStats_Type()
)
fsErpsCtxtClearRingStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsErpsCtxtClearRingStats.setStatus("current")
_FsErpsCtxtRowStatus_Type = RowStatus
_FsErpsCtxtRowStatus_Object = MibTableColumn
fsErpsCtxtRowStatus = _FsErpsCtxtRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 40, 1, 1, 1, 8),
    _FsErpsCtxtRowStatus_Type()
)
fsErpsCtxtRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsErpsCtxtRowStatus.setStatus("current")


class _FsErpsCtxtVlanGroupManager_Type(Integer32):
    """Custom type fsErpsCtxtVlanGroupManager based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mstp", 1),
          ("erps", 2))
    )


_FsErpsCtxtVlanGroupManager_Type.__name__ = "Integer32"
_FsErpsCtxtVlanGroupManager_Object = MibTableColumn
fsErpsCtxtVlanGroupManager = _FsErpsCtxtVlanGroupManager_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 40, 1, 1, 1, 9),
    _FsErpsCtxtVlanGroupManager_Type()
)
fsErpsCtxtVlanGroupManager.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsErpsCtxtVlanGroupManager.setStatus("current")


class _FsErpsCtxtProprietaryClearFS_Type(TruthValue):
    """Custom type fsErpsCtxtProprietaryClearFS based on TruthValue"""
    defaultValue = 2


_FsErpsCtxtProprietaryClearFS_Type.__name__ = "TruthValue"
_FsErpsCtxtProprietaryClearFS_Object = MibTableColumn
fsErpsCtxtProprietaryClearFS = _FsErpsCtxtProprietaryClearFS_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 40, 1, 1, 1, 10),
    _FsErpsCtxtProprietaryClearFS_Type()
)
fsErpsCtxtProprietaryClearFS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsErpsCtxtProprietaryClearFS.setStatus("current")
_FsErpsVlanGroupTable_Object = MibTable
fsErpsVlanGroupTable = _FsErpsVlanGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 40, 1, 2)
)
if mibBuilder.loadTexts:
    fsErpsVlanGroupTable.setStatus("current")
_FsErpsVlanGroupEntry_Object = MibTableRow
fsErpsVlanGroupEntry = _FsErpsVlanGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 40, 1, 2, 1)
)
fsErpsVlanGroupEntry.setIndexNames(
    (0, "SUPERMICRO-ERPS-MIB", "fsErpsContextId"),
    (0, "SUPERMICRO-ERPS-MIB", "fsErpsVlanId"),
    (0, "SUPERMICRO-ERPS-MIB", "fsErpsVlanGroupId"),
)
if mibBuilder.loadTexts:
    fsErpsVlanGroupEntry.setStatus("current")
_FsErpsVlanId_Type = VlanId
_FsErpsVlanId_Object = MibTableColumn
fsErpsVlanId = _FsErpsVlanId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 40, 1, 2, 1, 1),
    _FsErpsVlanId_Type()
)
fsErpsVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsErpsVlanId.setStatus("current")


class _FsErpsVlanGroupId_Type(Integer32):
    """Custom type fsErpsVlanGroupId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_FsErpsVlanGroupId_Type.__name__ = "Integer32"
_FsErpsVlanGroupId_Object = MibTableColumn
fsErpsVlanGroupId = _FsErpsVlanGroupId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 40, 1, 2, 1, 2),
    _FsErpsVlanGroupId_Type()
)
fsErpsVlanGroupId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsErpsVlanGroupId.setStatus("current")
_FsErpsVlanGroupRowStatus_Type = RowStatus
_FsErpsVlanGroupRowStatus_Object = MibTableColumn
fsErpsVlanGroupRowStatus = _FsErpsVlanGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 40, 1, 2, 1, 3),
    _FsErpsVlanGroupRowStatus_Type()
)
fsErpsVlanGroupRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsErpsVlanGroupRowStatus.setStatus("current")
_FsErpsRing_ObjectIdentity = ObjectIdentity
fsErpsRing = _FsErpsRing_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 40, 2)
)
_FsErpsRingTable_Object = MibTable
fsErpsRingTable = _FsErpsRingTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 40, 2, 1)
)
if mibBuilder.loadTexts:
    fsErpsRingTable.setStatus("current")
_FsErpsRingEntry_Object = MibTableRow
fsErpsRingEntry = _FsErpsRingEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 40, 2, 1, 1)
)
fsErpsRingEntry.setIndexNames(
    (0, "SUPERMICRO-ERPS-MIB", "fsErpsContextId"),
    (0, "SUPERMICRO-ERPS-MIB", "fsErpsRingId"),
)
if mibBuilder.loadTexts:
    fsErpsRingEntry.setStatus("current")
_FsErpsRingId_Type = RingId
_FsErpsRingId_Object = MibTableColumn
fsErpsRingId = _FsErpsRingId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 40, 2, 1, 1, 1),
    _FsErpsRingId_Type()
)
fsErpsRingId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsErpsRingId.setStatus("current")
_FsErpsRingVlanId_Type = VlanId
_FsErpsRingVlanId_Object = MibTableColumn
fsErpsRingVlanId = _FsErpsRingVlanId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 40, 2, 1, 1, 2),
    _FsErpsRingVlanId_Type()
)
fsErpsRingVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsErpsRingVlanId.setStatus("current")
_FsErpsRingName_Type = DisplayString
_FsErpsRingName_Object = MibTableColumn
fsErpsRingName = _FsErpsRingName_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 40, 2, 1, 1, 3),
    _FsErpsRingName_Type()
)
fsErpsRingName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsErpsRingName.setStatus("current")
_FsErpsRingPort1_Type = InterfaceIndex
_FsErpsRingPort1_Object = MibTableColumn
fsErpsRingPort1 = _FsErpsRingPort1_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 40, 2, 1, 1, 4),
    _FsErpsRingPort1_Type()
)
fsErpsRingPort1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsErpsRingPort1.setStatus("current")
_FsErpsRingPort2_Type = InterfaceIndexOrZero
_FsErpsRingPort2_Object = MibTableColumn
fsErpsRingPort2 = _FsErpsRingPort2_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 40, 2, 1, 1, 5),
    _FsErpsRingPort2_Type()
)
fsErpsRingPort2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsErpsRingPort2.setStatus("current")


class _FsErpsRingRplPort_Type(InterfaceIndexOrZero):
    """Custom type fsErpsRingRplPort based on InterfaceIndexOrZero"""
    defaultValue = 0


_FsErpsRingRplPort_Type.__name__ = "InterfaceIndexOrZero"
_FsErpsRingRplPort_Object = MibTableColumn
fsErpsRingRplPort = _FsErpsRingRplPort_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 40, 2, 1, 1, 6),
    _FsErpsRingRplPort_Type()
)
fsErpsRingRplPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsErpsRingRplPort.setStatus("current")


class _FsErpsRingPortBlockingOnVcRecovery_Type(TruthValue):
    """Custom type fsErpsRingPortBlockingOnVcRecovery based on TruthValue"""
    defaultValue = 2


_FsErpsRingPortBlockingOnVcRecovery_Type.__name__ = "TruthValue"
_FsErpsRingPortBlockingOnVcRecovery_Object = MibTableColumn
fsErpsRingPortBlockingOnVcRecovery = _FsErpsRingPortBlockingOnVcRecovery_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 40, 2, 1, 1, 7),
    _FsErpsRingPortBlockingOnVcRecovery_Type()
)
fsErpsRingPortBlockingOnVcRecovery.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsErpsRingPortBlockingOnVcRecovery.setStatus("current")


class _FsErpsRingNodeType_Type(Integer32):
    """Custom type fsErpsRingNodeType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("rplOwner", 1),
          ("nonRplOwner", 2))
    )


_FsErpsRingNodeType_Type.__name__ = "Integer32"
_FsErpsRingNodeType_Object = MibTableColumn
fsErpsRingNodeType = _FsErpsRingNodeType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 40, 2, 1, 1, 8),
    _FsErpsRingNodeType_Type()
)
fsErpsRingNodeType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsErpsRingNodeType.setStatus("current")


class _FsErpsRingOperatingMode_Type(Integer32):
    """Custom type fsErpsRingOperatingMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("revertive", 1),
          ("nonRevertive", 2))
    )


_FsErpsRingOperatingMode_Type.__name__ = "Integer32"
_FsErpsRingOperatingMode_Object = MibTableColumn
fsErpsRingOperatingMode = _FsErpsRingOperatingMode_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 40, 2, 1, 1, 9),
    _FsErpsRingOperatingMode_Type()
)
fsErpsRingOperatingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsErpsRingOperatingMode.setStatus("current")


class _FsErpsRingMonitorMechanism_Type(RingMonitorMechanismType):
    """Custom type fsErpsRingMonitorMechanism based on RingMonitorMechanismType"""
    defaultValue = 1


_FsErpsRingMonitorMechanism_Type.__name__ = "RingMonitorMechanismType"
_FsErpsRingMonitorMechanism_Object = MibTableColumn
fsErpsRingMonitorMechanism = _FsErpsRingMonitorMechanism_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 40, 2, 1, 1, 10),
    _FsErpsRingMonitorMechanism_Type()
)
fsErpsRingMonitorMechanism.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsErpsRingMonitorMechanism.setStatus("current")


class _FsErpsRingPort1Status_Type(Integer32):
    """Custom type fsErpsRingPort1Status based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("blocked", 1),
          ("unblocked", 2))
    )


_FsErpsRingPort1Status_Type.__name__ = "Integer32"
_FsErpsRingPort1Status_Object = MibTableColumn
fsErpsRingPort1Status = _FsErpsRingPort1Status_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 40, 2, 1, 1, 11),
    _FsErpsRingPort1Status_Type()
)
fsErpsRingPort1Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsErpsRingPort1Status.setStatus("current")


class _FsErpsRingPort2Status_Type(Integer32):
    """Custom type fsErpsRingPort2Status based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("blocked", 1),
          ("unblocked", 2))
    )


_FsErpsRingPort2Status_Type.__name__ = "Integer32"
_FsErpsRingPort2Status_Object = MibTableColumn
fsErpsRingPort2Status = _FsErpsRingPort2Status_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 40, 2, 1, 1, 12),
    _FsErpsRingPort2Status_Type()
)
fsErpsRingPort2Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsErpsRingPort2Status.setStatus("current")


class _FsErpsRingSemState_Type(Integer32):
    """Custom type fsErpsRingSemState based on Integer32"""
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
          ("idle", 1),
          ("protection", 2),
          ("manualswitch", 3),
          ("forcedswitch", 4),
          ("pending", 5))
    )


_FsErpsRingSemState_Type.__name__ = "Integer32"
_FsErpsRingSemState_Object = MibTableColumn
fsErpsRingSemState = _FsErpsRingSemState_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 40, 2, 1, 1, 13),
    _FsErpsRingSemState_Type()
)
fsErpsRingSemState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsErpsRingSemState.setStatus("current")
_FsErpsRingNodeStatus_Type = Integer32
_FsErpsRingNodeStatus_Object = MibTableColumn
fsErpsRingNodeStatus = _FsErpsRingNodeStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 40, 2, 1, 1, 14),
    _FsErpsRingNodeStatus_Type()
)
fsErpsRingNodeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsErpsRingNodeStatus.setStatus("current")
_FsErpsRingRowStatus_Type = RowStatus
_FsErpsRingRowStatus_Object = MibTableColumn
fsErpsRingRowStatus = _FsErpsRingRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 40, 2, 1, 1, 15),
    _FsErpsRingRowStatus_Type()
)
fsErpsRingRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsErpsRingRowStatus.setStatus("current")


class _FsErpsRingMacId_Type(Integer32):
    """Custom type fsErpsRingMacId based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_FsErpsRingMacId_Type.__name__ = "Integer32"
_FsErpsRingMacId_Object = MibTableColumn
fsErpsRingMacId = _FsErpsRingMacId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 40, 2, 1, 1, 16),
    _FsErpsRingMacId_Type()
)
fsErpsRingMacId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsErpsRingMacId.setStatus("current")


class _FsErpsRingProtectedVlanGroupId_Type(Integer32):
    """Custom type fsErpsRingProtectedVlanGroupId based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_FsErpsRingProtectedVlanGroupId_Type.__name__ = "Integer32"
_FsErpsRingProtectedVlanGroupId_Object = MibTableColumn
fsErpsRingProtectedVlanGroupId = _FsErpsRingProtectedVlanGroupId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 40, 2, 1, 1, 17),
    _FsErpsRingProtectedVlanGroupId_Type()
)
fsErpsRingProtectedVlanGroupId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsErpsRingProtectedVlanGroupId.setStatus("current")


class _FsErpsRingProtectionType_Type(Integer32):
    """Custom type fsErpsRingProtectionType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("portBased", 1),
          ("serviceBased", 2))
    )


_FsErpsRingProtectionType_Type.__name__ = "Integer32"
_FsErpsRingProtectionType_Object = MibTableColumn
fsErpsRingProtectionType = _FsErpsRingProtectionType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 40, 2, 1, 1, 18),
    _FsErpsRingProtectionType_Type()
)
fsErpsRingProtectionType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsErpsRingProtectionType.setStatus("current")


class _FsErpsRingRAPSCompatibleVersion_Type(Integer32):
    """Custom type fsErpsRingRAPSCompatibleVersion based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("v1", 1),
          ("v2", 2))
    )


_FsErpsRingRAPSCompatibleVersion_Type.__name__ = "Integer32"
_FsErpsRingRAPSCompatibleVersion_Object = MibTableColumn
fsErpsRingRAPSCompatibleVersion = _FsErpsRingRAPSCompatibleVersion_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 40, 2, 1, 1, 19),
    _FsErpsRingRAPSCompatibleVersion_Type()
)
fsErpsRingRAPSCompatibleVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsErpsRingRAPSCompatibleVersion.setStatus("current")


class _FsErpsRingRplNeighbourPort_Type(InterfaceIndexOrZero):
    """Custom type fsErpsRingRplNeighbourPort based on InterfaceIndexOrZero"""
    defaultValue = 0


_FsErpsRingRplNeighbourPort_Type.__name__ = "InterfaceIndexOrZero"
_FsErpsRingRplNeighbourPort_Object = MibTableColumn
fsErpsRingRplNeighbourPort = _FsErpsRingRplNeighbourPort_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 40, 2, 1, 1, 20),
    _FsErpsRingRplNeighbourPort_Type()
)
fsErpsRingRplNeighbourPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsErpsRingRplNeighbourPort.setStatus("current")


class _FsErpsRingRAPSSubRingWithoutVC_Type(TruthValue):
    """Custom type fsErpsRingRAPSSubRingWithoutVC based on TruthValue"""
    defaultValue = 2


_FsErpsRingRAPSSubRingWithoutVC_Type.__name__ = "TruthValue"
_FsErpsRingRAPSSubRingWithoutVC_Object = MibTableColumn
fsErpsRingRAPSSubRingWithoutVC = _FsErpsRingRAPSSubRingWithoutVC_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 40, 2, 1, 1, 21),
    _FsErpsRingRAPSSubRingWithoutVC_Type()
)
fsErpsRingRAPSSubRingWithoutVC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsErpsRingRAPSSubRingWithoutVC.setStatus("current")


class _FsErpsRingRplNextNeighbourPort_Type(InterfaceIndexOrZero):
    """Custom type fsErpsRingRplNextNeighbourPort based on InterfaceIndexOrZero"""
    defaultValue = 0


_FsErpsRingRplNextNeighbourPort_Type.__name__ = "InterfaceIndexOrZero"
_FsErpsRingRplNextNeighbourPort_Object = MibTableColumn
fsErpsRingRplNextNeighbourPort = _FsErpsRingRplNextNeighbourPort_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 40, 2, 1, 1, 22),
    _FsErpsRingRplNextNeighbourPort_Type()
)
fsErpsRingRplNextNeighbourPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsErpsRingRplNextNeighbourPort.setStatus("current")
_FsErpsRingPort1NodeID_Type = MacAddress
_FsErpsRingPort1NodeID_Object = MibTableColumn
fsErpsRingPort1NodeID = _FsErpsRingPort1NodeID_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 40, 2, 1, 1, 23),
    _FsErpsRingPort1NodeID_Type()
)
fsErpsRingPort1NodeID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsErpsRingPort1NodeID.setStatus("current")
_FsErpsRingPort2NodeID_Type = MacAddress
_FsErpsRingPort2NodeID_Object = MibTableColumn
fsErpsRingPort2NodeID = _FsErpsRingPort2NodeID_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 40, 2, 1, 1, 24),
    _FsErpsRingPort2NodeID_Type()
)
fsErpsRingPort2NodeID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsErpsRingPort2NodeID.setStatus("current")
_FsErpsRingPort1BPRBitVal_Type = TruthValue
_FsErpsRingPort1BPRBitVal_Object = MibTableColumn
fsErpsRingPort1BPRBitVal = _FsErpsRingPort1BPRBitVal_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 40, 2, 1, 1, 25),
    _FsErpsRingPort1BPRBitVal_Type()
)
fsErpsRingPort1BPRBitVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsErpsRingPort1BPRBitVal.setStatus("current")
_FsErpsRingPort2BPRBitVal_Type = TruthValue
_FsErpsRingPort2BPRBitVal_Object = MibTableColumn
fsErpsRingPort2BPRBitVal = _FsErpsRingPort2BPRBitVal_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 40, 2, 1, 1, 26),
    _FsErpsRingPort2BPRBitVal_Type()
)
fsErpsRingPort2BPRBitVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsErpsRingPort2BPRBitVal.setStatus("current")


class _FsErpsRingProtectedVlanGroupList_Type(OctetString):
    """Custom type fsErpsRingProtectedVlanGroupList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_FsErpsRingProtectedVlanGroupList_Type.__name__ = "OctetString"
_FsErpsRingProtectedVlanGroupList_Object = MibTableColumn
fsErpsRingProtectedVlanGroupList = _FsErpsRingProtectedVlanGroupList_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 40, 2, 1, 1, 27),
    _FsErpsRingProtectedVlanGroupList_Type()
)
fsErpsRingProtectedVlanGroupList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsErpsRingProtectedVlanGroupList.setStatus("current")


class _FsErpsRingServiceType_Type(RingServiceType):
    """Custom type fsErpsRingServiceType based on RingServiceType"""
    defaultValue = 1


_FsErpsRingServiceType_Type.__name__ = "RingServiceType"
_FsErpsRingServiceType_Object = MibTableColumn
fsErpsRingServiceType = _FsErpsRingServiceType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 40, 2, 1, 1, 28),
    _FsErpsRingServiceType_Type()
)
fsErpsRingServiceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsErpsRingServiceType.setStatus("current")


class _FsErpsRingPort1SubPortList_Type(OctetString):
    """Custom type fsErpsRingPort1SubPortList based on OctetString"""
    defaultValue = OctetString("0")


_FsErpsRingPort1SubPortList_Type.__name__ = "OctetString"
_FsErpsRingPort1SubPortList_Object = MibTableColumn
fsErpsRingPort1SubPortList = _FsErpsRingPort1SubPortList_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 40, 2, 1, 1, 29),
    _FsErpsRingPort1SubPortList_Type()
)
fsErpsRingPort1SubPortList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsErpsRingPort1SubPortList.setStatus("current")


class _FsErpsRingPort2SubPortList_Type(OctetString):
    """Custom type fsErpsRingPort2SubPortList based on OctetString"""
    defaultValue = OctetString("0")


_FsErpsRingPort2SubPortList_Type.__name__ = "OctetString"
_FsErpsRingPort2SubPortList_Object = MibTableColumn
fsErpsRingPort2SubPortList = _FsErpsRingPort2SubPortList_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 40, 2, 1, 1, 30),
    _FsErpsRingPort2SubPortList_Type()
)
fsErpsRingPort2SubPortList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsErpsRingPort2SubPortList.setStatus("current")
_FsErpsRingCfmTable_Object = MibTable
fsErpsRingCfmTable = _FsErpsRingCfmTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 40, 2, 2)
)
if mibBuilder.loadTexts:
    fsErpsRingCfmTable.setStatus("current")
_FsErpsRingCfmEntry_Object = MibTableRow
fsErpsRingCfmEntry = _FsErpsRingCfmEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 40, 2, 2, 1)
)
fsErpsRingCfmEntry.setIndexNames(
    (0, "SUPERMICRO-ERPS-MIB", "fsErpsContextId"),
    (0, "SUPERMICRO-ERPS-MIB", "fsErpsRingId"),
)
if mibBuilder.loadTexts:
    fsErpsRingCfmEntry.setStatus("current")
_FsErpsRingMEG1_Type = Unsigned32
_FsErpsRingMEG1_Object = MibTableColumn
fsErpsRingMEG1 = _FsErpsRingMEG1_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 40, 2, 2, 1, 1),
    _FsErpsRingMEG1_Type()
)
fsErpsRingMEG1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsErpsRingMEG1.setStatus("current")
_FsErpsRingCfmME1_Type = Unsigned32
_FsErpsRingCfmME1_Object = MibTableColumn
fsErpsRingCfmME1 = _FsErpsRingCfmME1_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 40, 2, 2, 1, 2),
    _FsErpsRingCfmME1_Type()
)
fsErpsRingCfmME1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsErpsRingCfmME1.setStatus("current")
_FsErpsRingCfmMEP1_Type = Dot1agCfmMepId
_FsErpsRingCfmMEP1_Object = MibTableColumn
fsErpsRingCfmMEP1 = _FsErpsRingCfmMEP1_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 40, 2, 2, 1, 3),
    _FsErpsRingCfmMEP1_Type()
)
fsErpsRingCfmMEP1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsErpsRingCfmMEP1.setStatus("current")
_FsErpsRingMEG2_Type = Unsigned32
_FsErpsRingMEG2_Object = MibTableColumn
fsErpsRingMEG2 = _FsErpsRingMEG2_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 40, 2, 2, 1, 4),
    _FsErpsRingMEG2_Type()
)
fsErpsRingMEG2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsErpsRingMEG2.setStatus("current")
_FsErpsRingCfmME2_Type = Unsigned32
_FsErpsRingCfmME2_Object = MibTableColumn
fsErpsRingCfmME2 = _FsErpsRingCfmME2_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 40, 2, 2, 1, 5),
    _FsErpsRingCfmME2_Type()
)
fsErpsRingCfmME2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsErpsRingCfmME2.setStatus("current")
_FsErpsRingCfmMEP2_Type = Dot1agCfmMepId
_FsErpsRingCfmMEP2_Object = MibTableColumn
fsErpsRingCfmMEP2 = _FsErpsRingCfmMEP2_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 40, 2, 2, 1, 6),
    _FsErpsRingCfmMEP2_Type()
)
fsErpsRingCfmMEP2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsErpsRingCfmMEP2.setStatus("current")
_FsErpsRingCfmRowStatus_Type = RowStatus
_FsErpsRingCfmRowStatus_Object = MibTableColumn
fsErpsRingCfmRowStatus = _FsErpsRingCfmRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 40, 2, 2, 1, 7),
    _FsErpsRingCfmRowStatus_Type()
)
fsErpsRingCfmRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsErpsRingCfmRowStatus.setStatus("current")
_FsErpsRingConfigTable_Object = MibTable
fsErpsRingConfigTable = _FsErpsRingConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 40, 2, 3)
)
if mibBuilder.loadTexts:
    fsErpsRingConfigTable.setStatus("current")
_FsErpsRingConfigEntry_Object = MibTableRow
fsErpsRingConfigEntry = _FsErpsRingConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 40, 2, 3, 1)
)
fsErpsRingConfigEntry.setIndexNames(
    (0, "SUPERMICRO-ERPS-MIB", "fsErpsContextId"),
    (0, "SUPERMICRO-ERPS-MIB", "fsErpsRingId"),
)
if mibBuilder.loadTexts:
    fsErpsRingConfigEntry.setStatus("current")


class _FsErpsRingConfigHoldOffTime_Type(Unsigned32):
    """Custom type fsErpsRingConfigHoldOffTime based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600000),
    )


_FsErpsRingConfigHoldOffTime_Type.__name__ = "Unsigned32"
_FsErpsRingConfigHoldOffTime_Object = MibTableColumn
fsErpsRingConfigHoldOffTime = _FsErpsRingConfigHoldOffTime_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 40, 2, 3, 1, 1),
    _FsErpsRingConfigHoldOffTime_Type()
)
fsErpsRingConfigHoldOffTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsErpsRingConfigHoldOffTime.setStatus("current")
if mibBuilder.loadTexts:
    fsErpsRingConfigHoldOffTime.setUnits("milliseconds")


class _FsErpsRingConfigGuardTime_Type(Unsigned32):
    """Custom type fsErpsRingConfigGuardTime based on Unsigned32"""
    defaultValue = 500

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600000),
    )


_FsErpsRingConfigGuardTime_Type.__name__ = "Unsigned32"
_FsErpsRingConfigGuardTime_Object = MibTableColumn
fsErpsRingConfigGuardTime = _FsErpsRingConfigGuardTime_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 40, 2, 3, 1, 2),
    _FsErpsRingConfigGuardTime_Type()
)
fsErpsRingConfigGuardTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsErpsRingConfigGuardTime.setStatus("current")
if mibBuilder.loadTexts:
    fsErpsRingConfigGuardTime.setUnits("milliseconds")


class _FsErpsRingConfigWTRTime_Type(Unsigned32):
    """Custom type fsErpsRingConfigWTRTime based on Unsigned32"""
    defaultValue = 300000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400000),
    )


_FsErpsRingConfigWTRTime_Type.__name__ = "Unsigned32"
_FsErpsRingConfigWTRTime_Object = MibTableColumn
fsErpsRingConfigWTRTime = _FsErpsRingConfigWTRTime_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 40, 2, 3, 1, 3),
    _FsErpsRingConfigWTRTime_Type()
)
fsErpsRingConfigWTRTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsErpsRingConfigWTRTime.setStatus("current")
if mibBuilder.loadTexts:
    fsErpsRingConfigWTRTime.setUnits("milliseconds")


class _FsErpsRingConfigPeriodicTime_Type(Unsigned32):
    """Custom type fsErpsRingConfigPeriodicTime based on Unsigned32"""
    defaultValue = 5000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600000),
    )


_FsErpsRingConfigPeriodicTime_Type.__name__ = "Unsigned32"
_FsErpsRingConfigPeriodicTime_Object = MibTableColumn
fsErpsRingConfigPeriodicTime = _FsErpsRingConfigPeriodicTime_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 40, 2, 3, 1, 4),
    _FsErpsRingConfigPeriodicTime_Type()
)
fsErpsRingConfigPeriodicTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsErpsRingConfigPeriodicTime.setStatus("current")
if mibBuilder.loadTexts:
    fsErpsRingConfigPeriodicTime.setUnits("milliseconds")


class _FsErpsRingConfigSwitchPort_Type(InterfaceIndexOrZero):
    """Custom type fsErpsRingConfigSwitchPort based on InterfaceIndexOrZero"""
    defaultValue = 0


_FsErpsRingConfigSwitchPort_Type.__name__ = "InterfaceIndexOrZero"
_FsErpsRingConfigSwitchPort_Object = MibTableColumn
fsErpsRingConfigSwitchPort = _FsErpsRingConfigSwitchPort_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 40, 2, 3, 1, 5),
    _FsErpsRingConfigSwitchPort_Type()
)
fsErpsRingConfigSwitchPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsErpsRingConfigSwitchPort.setStatus("current")


class _FsErpsRingConfigSwitchCmd_Type(Integer32):
    """Custom type fsErpsRingConfigSwitchCmd based on Integer32"""
    defaultValue = 1

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
          ("forceSwitch", 2),
          ("manualSwitch", 3))
    )


_FsErpsRingConfigSwitchCmd_Type.__name__ = "Integer32"
_FsErpsRingConfigSwitchCmd_Object = MibTableColumn
fsErpsRingConfigSwitchCmd = _FsErpsRingConfigSwitchCmd_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 40, 2, 3, 1, 6),
    _FsErpsRingConfigSwitchCmd_Type()
)
fsErpsRingConfigSwitchCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsErpsRingConfigSwitchCmd.setStatus("current")


class _FsErpsRingConfigRecoveryMethod_Type(Integer32):
    """Custom type fsErpsRingConfigRecoveryMethod based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("manual", 2))
    )


_FsErpsRingConfigRecoveryMethod_Type.__name__ = "Integer32"
_FsErpsRingConfigRecoveryMethod_Object = MibTableColumn
fsErpsRingConfigRecoveryMethod = _FsErpsRingConfigRecoveryMethod_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 40, 2, 3, 1, 7),
    _FsErpsRingConfigRecoveryMethod_Type()
)
fsErpsRingConfigRecoveryMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsErpsRingConfigRecoveryMethod.setStatus("current")


class _FsErpsRingConfigPropagateTC_Type(Integer32):
    """Custom type fsErpsRingConfigPropagateTC based on Integer32"""
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


_FsErpsRingConfigPropagateTC_Type.__name__ = "Integer32"
_FsErpsRingConfigPropagateTC_Object = MibTableColumn
fsErpsRingConfigPropagateTC = _FsErpsRingConfigPropagateTC_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 40, 2, 3, 1, 8),
    _FsErpsRingConfigPropagateTC_Type()
)
fsErpsRingConfigPropagateTC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsErpsRingConfigPropagateTC.setStatus("current")


class _FsErpsRingConfigWTBTime_Type(Unsigned32):
    """Custom type fsErpsRingConfigWTBTime based on Unsigned32"""
    defaultValue = 5500

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400000),
    )


_FsErpsRingConfigWTBTime_Type.__name__ = "Unsigned32"
_FsErpsRingConfigWTBTime_Object = MibTableColumn
fsErpsRingConfigWTBTime = _FsErpsRingConfigWTBTime_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 40, 2, 3, 1, 9),
    _FsErpsRingConfigWTBTime_Type()
)
fsErpsRingConfigWTBTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsErpsRingConfigWTBTime.setStatus("current")
if mibBuilder.loadTexts:
    fsErpsRingConfigWTBTime.setUnits("milliseconds")


class _FsErpsRingConfigClear_Type(Integer32):
    """Custom type fsErpsRingConfigClear based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("clear", 2))
    )


_FsErpsRingConfigClear_Type.__name__ = "Integer32"
_FsErpsRingConfigClear_Object = MibTableColumn
fsErpsRingConfigClear = _FsErpsRingConfigClear_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 40, 2, 3, 1, 10),
    _FsErpsRingConfigClear_Type()
)
fsErpsRingConfigClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsErpsRingConfigClear.setStatus("current")


class _FsErpsRingConfigInterConnNode_Type(Integer32):
    """Custom type fsErpsRingConfigInterConnNode based on Integer32"""
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
          ("primary", 1),
          ("secondary", 2))
    )


_FsErpsRingConfigInterConnNode_Type.__name__ = "Integer32"
_FsErpsRingConfigInterConnNode_Object = MibTableColumn
fsErpsRingConfigInterConnNode = _FsErpsRingConfigInterConnNode_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 40, 2, 3, 1, 11),
    _FsErpsRingConfigInterConnNode_Type()
)
fsErpsRingConfigInterConnNode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsErpsRingConfigInterConnNode.setStatus("current")


class _FsErpsRingConfigMultipleFailure_Type(Integer32):
    """Custom type fsErpsRingConfigMultipleFailure based on Integer32"""
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
        *(("disabled", 0),
          ("primary", 1),
          ("secondary", 2))
    )


_FsErpsRingConfigMultipleFailure_Type.__name__ = "Integer32"
_FsErpsRingConfigMultipleFailure_Object = MibTableColumn
fsErpsRingConfigMultipleFailure = _FsErpsRingConfigMultipleFailure_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 40, 2, 3, 1, 12),
    _FsErpsRingConfigMultipleFailure_Type()
)
fsErpsRingConfigMultipleFailure.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsErpsRingConfigMultipleFailure.setStatus("current")


class _FsErpsRingConfigIsPort1Present_Type(Integer32):
    """Custom type fsErpsRingConfigIsPort1Present based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("local", 1),
          ("remote", 2))
    )


_FsErpsRingConfigIsPort1Present_Type.__name__ = "Integer32"
_FsErpsRingConfigIsPort1Present_Object = MibTableColumn
fsErpsRingConfigIsPort1Present = _FsErpsRingConfigIsPort1Present_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 40, 2, 3, 1, 13),
    _FsErpsRingConfigIsPort1Present_Type()
)
fsErpsRingConfigIsPort1Present.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsErpsRingConfigIsPort1Present.setStatus("current")


class _FsErpsRingConfigIsPort2Present_Type(Integer32):
    """Custom type fsErpsRingConfigIsPort2Present based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("local", 1),
          ("remote", 2))
    )


_FsErpsRingConfigIsPort2Present_Type.__name__ = "Integer32"
_FsErpsRingConfigIsPort2Present_Object = MibTableColumn
fsErpsRingConfigIsPort2Present = _FsErpsRingConfigIsPort2Present_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 40, 2, 3, 1, 14),
    _FsErpsRingConfigIsPort2Present_Type()
)
fsErpsRingConfigIsPort2Present.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsErpsRingConfigIsPort2Present.setStatus("current")


class _FsErpsRingConfigInfoDistributingPort_Type(InterfaceIndexOrZero):
    """Custom type fsErpsRingConfigInfoDistributingPort based on InterfaceIndexOrZero"""
    defaultValue = 0


_FsErpsRingConfigInfoDistributingPort_Type.__name__ = "InterfaceIndexOrZero"
_FsErpsRingConfigInfoDistributingPort_Object = MibTableColumn
fsErpsRingConfigInfoDistributingPort = _FsErpsRingConfigInfoDistributingPort_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 40, 2, 3, 1, 15),
    _FsErpsRingConfigInfoDistributingPort_Type()
)
fsErpsRingConfigInfoDistributingPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsErpsRingConfigInfoDistributingPort.setStatus("current")


class _FsErpsRingConfigKValue_Type(OctetString):
    """Custom type fsErpsRingConfigKValue based on OctetString"""
    defaultValue = OctetString("3.50")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4


_FsErpsRingConfigKValue_Type.__name__ = "OctetString"
_FsErpsRingConfigKValue_Object = MibTableColumn
fsErpsRingConfigKValue = _FsErpsRingConfigKValue_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 40, 2, 3, 1, 16),
    _FsErpsRingConfigKValue_Type()
)
fsErpsRingConfigKValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsErpsRingConfigKValue.setStatus("current")


class _FsErpsRingConfigFailureOfProtocol_Type(TruthValue):
    """Custom type fsErpsRingConfigFailureOfProtocol based on TruthValue"""
    defaultValue = 2


_FsErpsRingConfigFailureOfProtocol_Type.__name__ = "TruthValue"
_FsErpsRingConfigFailureOfProtocol_Object = MibTableColumn
fsErpsRingConfigFailureOfProtocol = _FsErpsRingConfigFailureOfProtocol_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 40, 2, 3, 1, 17),
    _FsErpsRingConfigFailureOfProtocol_Type()
)
fsErpsRingConfigFailureOfProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsErpsRingConfigFailureOfProtocol.setStatus("current")
_FsErpsRingTcPropTable_Object = MibTable
fsErpsRingTcPropTable = _FsErpsRingTcPropTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 40, 2, 4)
)
if mibBuilder.loadTexts:
    fsErpsRingTcPropTable.setStatus("current")
_FsErpsRingTcPropEntry_Object = MibTableRow
fsErpsRingTcPropEntry = _FsErpsRingTcPropEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 40, 2, 4, 1)
)
fsErpsRingTcPropEntry.setIndexNames(
    (0, "SUPERMICRO-ERPS-MIB", "fsErpsContextId"),
    (0, "SUPERMICRO-ERPS-MIB", "fsErpsRingId"),
    (0, "SUPERMICRO-ERPS-MIB", "fsErpsRingTcPropRingId"),
)
if mibBuilder.loadTexts:
    fsErpsRingTcPropEntry.setStatus("current")
_FsErpsRingTcPropRingId_Type = RingId
_FsErpsRingTcPropRingId_Object = MibTableColumn
fsErpsRingTcPropRingId = _FsErpsRingTcPropRingId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 40, 2, 4, 1, 1),
    _FsErpsRingTcPropRingId_Type()
)
fsErpsRingTcPropRingId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsErpsRingTcPropRingId.setStatus("current")
_FsErpsRingTcPropRowStatus_Type = RowStatus
_FsErpsRingTcPropRowStatus_Object = MibTableColumn
fsErpsRingTcPropRowStatus = _FsErpsRingTcPropRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 40, 2, 4, 1, 2),
    _FsErpsRingTcPropRowStatus_Type()
)
fsErpsRingTcPropRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsErpsRingTcPropRowStatus.setStatus("current")
_FsErpsRingConfigExtTable_Object = MibTable
fsErpsRingConfigExtTable = _FsErpsRingConfigExtTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 40, 2, 5)
)
if mibBuilder.loadTexts:
    fsErpsRingConfigExtTable.setStatus("current")
_FsErpsRingConfigExtEntry_Object = MibTableRow
fsErpsRingConfigExtEntry = _FsErpsRingConfigExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 40, 2, 5, 1)
)
fsErpsRingConfigExtEntry.setIndexNames(
    (0, "SUPERMICRO-ERPS-MIB", "fsErpsContextId"),
    (0, "SUPERMICRO-ERPS-MIB", "fsErpsRingId"),
)
if mibBuilder.loadTexts:
    fsErpsRingConfigExtEntry.setStatus("current")


class _FsErpsRingConfigExtVCRecoveryPeriodicTime_Type(Unsigned32):
    """Custom type fsErpsRingConfigExtVCRecoveryPeriodicTime based on Unsigned32"""
    defaultValue = 5560

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600000),
    )


_FsErpsRingConfigExtVCRecoveryPeriodicTime_Type.__name__ = "Unsigned32"
_FsErpsRingConfigExtVCRecoveryPeriodicTime_Object = MibTableColumn
fsErpsRingConfigExtVCRecoveryPeriodicTime = _FsErpsRingConfigExtVCRecoveryPeriodicTime_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 40, 2, 5, 1, 1),
    _FsErpsRingConfigExtVCRecoveryPeriodicTime_Type()
)
fsErpsRingConfigExtVCRecoveryPeriodicTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsErpsRingConfigExtVCRecoveryPeriodicTime.setStatus("current")
if mibBuilder.loadTexts:
    fsErpsRingConfigExtVCRecoveryPeriodicTime.setUnits("milliseconds")
_FsErpsRingConfigExtMainRingId_Type = RingIdOrNone
_FsErpsRingConfigExtMainRingId_Object = MibTableColumn
fsErpsRingConfigExtMainRingId = _FsErpsRingConfigExtMainRingId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 40, 2, 5, 1, 2),
    _FsErpsRingConfigExtMainRingId_Type()
)
fsErpsRingConfigExtMainRingId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsErpsRingConfigExtMainRingId.setStatus("current")
_FsErpsStats_ObjectIdentity = ObjectIdentity
fsErpsStats = _FsErpsStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 40, 3)
)
_FsErpsMemFailCount_Type = Counter32
_FsErpsMemFailCount_Object = MibScalar
fsErpsMemFailCount = _FsErpsMemFailCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 40, 3, 1),
    _FsErpsMemFailCount_Type()
)
fsErpsMemFailCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsErpsMemFailCount.setStatus("current")
_FsErpsBufFailCount_Type = Counter32
_FsErpsBufFailCount_Object = MibScalar
fsErpsBufFailCount = _FsErpsBufFailCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 40, 3, 2),
    _FsErpsBufFailCount_Type()
)
fsErpsBufFailCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsErpsBufFailCount.setStatus("current")
_FsErpsTimerFailCount_Type = Counter32
_FsErpsTimerFailCount_Object = MibScalar
fsErpsTimerFailCount = _FsErpsTimerFailCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 40, 3, 3),
    _FsErpsTimerFailCount_Type()
)
fsErpsTimerFailCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsErpsTimerFailCount.setStatus("current")
_FsErpsRingStatsTable_Object = MibTable
fsErpsRingStatsTable = _FsErpsRingStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 40, 3, 4)
)
if mibBuilder.loadTexts:
    fsErpsRingStatsTable.setStatus("current")
_FsErpsRingStatsEntry_Object = MibTableRow
fsErpsRingStatsEntry = _FsErpsRingStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 40, 3, 4, 1)
)
fsErpsRingStatsEntry.setIndexNames(
    (0, "SUPERMICRO-ERPS-MIB", "fsErpsContextId"),
    (0, "SUPERMICRO-ERPS-MIB", "fsErpsRingId"),
)
if mibBuilder.loadTexts:
    fsErpsRingStatsEntry.setStatus("current")


class _FsErpsRingClearRingStats_Type(TruthValue):
    """Custom type fsErpsRingClearRingStats based on TruthValue"""
    defaultValue = 2


_FsErpsRingClearRingStats_Type.__name__ = "TruthValue"
_FsErpsRingClearRingStats_Object = MibTableColumn
fsErpsRingClearRingStats = _FsErpsRingClearRingStats_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 40, 3, 4, 1, 1),
    _FsErpsRingClearRingStats_Type()
)
fsErpsRingClearRingStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsErpsRingClearRingStats.setStatus("current")
_FsErpsRingPort1RapsPduSentCount_Type = Counter32
_FsErpsRingPort1RapsPduSentCount_Object = MibTableColumn
fsErpsRingPort1RapsPduSentCount = _FsErpsRingPort1RapsPduSentCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 40, 3, 4, 1, 2),
    _FsErpsRingPort1RapsPduSentCount_Type()
)
fsErpsRingPort1RapsPduSentCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsErpsRingPort1RapsPduSentCount.setStatus("current")
_FsErpsRingPort2RapsPduSentCount_Type = Counter32
_FsErpsRingPort2RapsPduSentCount_Object = MibTableColumn
fsErpsRingPort2RapsPduSentCount = _FsErpsRingPort2RapsPduSentCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 40, 3, 4, 1, 3),
    _FsErpsRingPort2RapsPduSentCount_Type()
)
fsErpsRingPort2RapsPduSentCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsErpsRingPort2RapsPduSentCount.setStatus("current")
_FsErpsRingPort1RapsPduRcvdCount_Type = Counter32
_FsErpsRingPort1RapsPduRcvdCount_Object = MibTableColumn
fsErpsRingPort1RapsPduRcvdCount = _FsErpsRingPort1RapsPduRcvdCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 40, 3, 4, 1, 4),
    _FsErpsRingPort1RapsPduRcvdCount_Type()
)
fsErpsRingPort1RapsPduRcvdCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsErpsRingPort1RapsPduRcvdCount.setStatus("current")
_FsErpsRingPort2RapsPduRcvdCount_Type = Counter32
_FsErpsRingPort2RapsPduRcvdCount_Object = MibTableColumn
fsErpsRingPort2RapsPduRcvdCount = _FsErpsRingPort2RapsPduRcvdCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 40, 3, 4, 1, 5),
    _FsErpsRingPort2RapsPduRcvdCount_Type()
)
fsErpsRingPort2RapsPduRcvdCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsErpsRingPort2RapsPduRcvdCount.setStatus("current")
_FsErpsRingPort1RapsPduDiscardCount_Type = Counter32
_FsErpsRingPort1RapsPduDiscardCount_Object = MibTableColumn
fsErpsRingPort1RapsPduDiscardCount = _FsErpsRingPort1RapsPduDiscardCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 40, 3, 4, 1, 6),
    _FsErpsRingPort1RapsPduDiscardCount_Type()
)
fsErpsRingPort1RapsPduDiscardCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsErpsRingPort1RapsPduDiscardCount.setStatus("current")
_FsErpsRingPort2RapsPduDiscardCount_Type = Counter32
_FsErpsRingPort2RapsPduDiscardCount_Object = MibTableColumn
fsErpsRingPort2RapsPduDiscardCount = _FsErpsRingPort2RapsPduDiscardCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 40, 3, 4, 1, 7),
    _FsErpsRingPort2RapsPduDiscardCount_Type()
)
fsErpsRingPort2RapsPduDiscardCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsErpsRingPort2RapsPduDiscardCount.setStatus("current")
_FsErpsRingPort1BlockedCount_Type = Counter32
_FsErpsRingPort1BlockedCount_Object = MibTableColumn
fsErpsRingPort1BlockedCount = _FsErpsRingPort1BlockedCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 40, 3, 4, 1, 8),
    _FsErpsRingPort1BlockedCount_Type()
)
fsErpsRingPort1BlockedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsErpsRingPort1BlockedCount.setStatus("current")
_FsErpsRingPort2BlockedCount_Type = Counter32
_FsErpsRingPort2BlockedCount_Object = MibTableColumn
fsErpsRingPort2BlockedCount = _FsErpsRingPort2BlockedCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 40, 3, 4, 1, 9),
    _FsErpsRingPort2BlockedCount_Type()
)
fsErpsRingPort2BlockedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsErpsRingPort2BlockedCount.setStatus("current")
_FsErpsRingPort1UnblockedCount_Type = Counter32
_FsErpsRingPort1UnblockedCount_Object = MibTableColumn
fsErpsRingPort1UnblockedCount = _FsErpsRingPort1UnblockedCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 40, 3, 4, 1, 10),
    _FsErpsRingPort1UnblockedCount_Type()
)
fsErpsRingPort1UnblockedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsErpsRingPort1UnblockedCount.setStatus("current")
_FsErpsRingPort2UnblockedCount_Type = Counter32
_FsErpsRingPort2UnblockedCount_Object = MibTableColumn
fsErpsRingPort2UnblockedCount = _FsErpsRingPort2UnblockedCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 40, 3, 4, 1, 11),
    _FsErpsRingPort2UnblockedCount_Type()
)
fsErpsRingPort2UnblockedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsErpsRingPort2UnblockedCount.setStatus("current")
_FsErpsRingPort1FailedCount_Type = Counter32
_FsErpsRingPort1FailedCount_Object = MibTableColumn
fsErpsRingPort1FailedCount = _FsErpsRingPort1FailedCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 40, 3, 4, 1, 12),
    _FsErpsRingPort1FailedCount_Type()
)
fsErpsRingPort1FailedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsErpsRingPort1FailedCount.setStatus("current")
_FsErpsRingPort2FailedCount_Type = Counter32
_FsErpsRingPort2FailedCount_Object = MibTableColumn
fsErpsRingPort2FailedCount = _FsErpsRingPort2FailedCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 40, 3, 4, 1, 13),
    _FsErpsRingPort2FailedCount_Type()
)
fsErpsRingPort2FailedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsErpsRingPort2FailedCount.setStatus("current")
_FsErpsRingPort1RecoveredCount_Type = Counter32
_FsErpsRingPort1RecoveredCount_Object = MibTableColumn
fsErpsRingPort1RecoveredCount = _FsErpsRingPort1RecoveredCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 40, 3, 4, 1, 14),
    _FsErpsRingPort1RecoveredCount_Type()
)
fsErpsRingPort1RecoveredCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsErpsRingPort1RecoveredCount.setStatus("current")
_FsErpsRingPort2RecoveredCount_Type = Counter32
_FsErpsRingPort2RecoveredCount_Object = MibTableColumn
fsErpsRingPort2RecoveredCount = _FsErpsRingPort2RecoveredCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 40, 3, 4, 1, 15),
    _FsErpsRingPort2RecoveredCount_Type()
)
fsErpsRingPort2RecoveredCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsErpsRingPort2RecoveredCount.setStatus("current")
_FsErpsRingPort1VersionDiscardCount_Type = Counter32
_FsErpsRingPort1VersionDiscardCount_Object = MibTableColumn
fsErpsRingPort1VersionDiscardCount = _FsErpsRingPort1VersionDiscardCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 40, 3, 4, 1, 16),
    _FsErpsRingPort1VersionDiscardCount_Type()
)
fsErpsRingPort1VersionDiscardCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsErpsRingPort1VersionDiscardCount.setStatus("current")
_FsErpsRingPort2VersionDiscardCount_Type = Counter32
_FsErpsRingPort2VersionDiscardCount_Object = MibTableColumn
fsErpsRingPort2VersionDiscardCount = _FsErpsRingPort2VersionDiscardCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 40, 3, 4, 1, 17),
    _FsErpsRingPort2VersionDiscardCount_Type()
)
fsErpsRingPort2VersionDiscardCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsErpsRingPort2VersionDiscardCount.setStatus("current")
_FsErpsRingPort1RapsFSPduRxCount_Type = Counter32
_FsErpsRingPort1RapsFSPduRxCount_Object = MibTableColumn
fsErpsRingPort1RapsFSPduRxCount = _FsErpsRingPort1RapsFSPduRxCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 40, 3, 4, 1, 18),
    _FsErpsRingPort1RapsFSPduRxCount_Type()
)
fsErpsRingPort1RapsFSPduRxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsErpsRingPort1RapsFSPduRxCount.setStatus("current")
_FsErpsRingPort1RapsFSPduTxCount_Type = Counter32
_FsErpsRingPort1RapsFSPduTxCount_Object = MibTableColumn
fsErpsRingPort1RapsFSPduTxCount = _FsErpsRingPort1RapsFSPduTxCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 40, 3, 4, 1, 19),
    _FsErpsRingPort1RapsFSPduTxCount_Type()
)
fsErpsRingPort1RapsFSPduTxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsErpsRingPort1RapsFSPduTxCount.setStatus("current")
_FsErpsRingPort2RapsFSPduRxCount_Type = Counter32
_FsErpsRingPort2RapsFSPduRxCount_Object = MibTableColumn
fsErpsRingPort2RapsFSPduRxCount = _FsErpsRingPort2RapsFSPduRxCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 40, 3, 4, 1, 20),
    _FsErpsRingPort2RapsFSPduRxCount_Type()
)
fsErpsRingPort2RapsFSPduRxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsErpsRingPort2RapsFSPduRxCount.setStatus("current")
_FsErpsRingPort2RapsFSPduTxCount_Type = Counter32
_FsErpsRingPort2RapsFSPduTxCount_Object = MibTableColumn
fsErpsRingPort2RapsFSPduTxCount = _FsErpsRingPort2RapsFSPduTxCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 40, 3, 4, 1, 21),
    _FsErpsRingPort2RapsFSPduTxCount_Type()
)
fsErpsRingPort2RapsFSPduTxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsErpsRingPort2RapsFSPduTxCount.setStatus("current")
_FsErpsRingPort1RapsMSPduRxCount_Type = Counter32
_FsErpsRingPort1RapsMSPduRxCount_Object = MibTableColumn
fsErpsRingPort1RapsMSPduRxCount = _FsErpsRingPort1RapsMSPduRxCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 40, 3, 4, 1, 22),
    _FsErpsRingPort1RapsMSPduRxCount_Type()
)
fsErpsRingPort1RapsMSPduRxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsErpsRingPort1RapsMSPduRxCount.setStatus("current")
_FsErpsRingPort1RapsMSPduTxCount_Type = Counter32
_FsErpsRingPort1RapsMSPduTxCount_Object = MibTableColumn
fsErpsRingPort1RapsMSPduTxCount = _FsErpsRingPort1RapsMSPduTxCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 40, 3, 4, 1, 23),
    _FsErpsRingPort1RapsMSPduTxCount_Type()
)
fsErpsRingPort1RapsMSPduTxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsErpsRingPort1RapsMSPduTxCount.setStatus("current")
_FsErpsRingPort2RapsMSPduRxCount_Type = Counter32
_FsErpsRingPort2RapsMSPduRxCount_Object = MibTableColumn
fsErpsRingPort2RapsMSPduRxCount = _FsErpsRingPort2RapsMSPduRxCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 40, 3, 4, 1, 24),
    _FsErpsRingPort2RapsMSPduRxCount_Type()
)
fsErpsRingPort2RapsMSPduRxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsErpsRingPort2RapsMSPduRxCount.setStatus("current")
_FsErpsRingPort2RapsMSPduTxCount_Type = Counter32
_FsErpsRingPort2RapsMSPduTxCount_Object = MibTableColumn
fsErpsRingPort2RapsMSPduTxCount = _FsErpsRingPort2RapsMSPduTxCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 40, 3, 4, 1, 25),
    _FsErpsRingPort2RapsMSPduTxCount_Type()
)
fsErpsRingPort2RapsMSPduTxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsErpsRingPort2RapsMSPduTxCount.setStatus("current")
_FsErpsRingPort1RapsEventPduRxCount_Type = Counter32
_FsErpsRingPort1RapsEventPduRxCount_Object = MibTableColumn
fsErpsRingPort1RapsEventPduRxCount = _FsErpsRingPort1RapsEventPduRxCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 40, 3, 4, 1, 26),
    _FsErpsRingPort1RapsEventPduRxCount_Type()
)
fsErpsRingPort1RapsEventPduRxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsErpsRingPort1RapsEventPduRxCount.setStatus("current")
_FsErpsRingPort1RapsEventPduTxCount_Type = Counter32
_FsErpsRingPort1RapsEventPduTxCount_Object = MibTableColumn
fsErpsRingPort1RapsEventPduTxCount = _FsErpsRingPort1RapsEventPduTxCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 40, 3, 4, 1, 27),
    _FsErpsRingPort1RapsEventPduTxCount_Type()
)
fsErpsRingPort1RapsEventPduTxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsErpsRingPort1RapsEventPduTxCount.setStatus("current")
_FsErpsRingPort2RapsEventPduRxCount_Type = Counter32
_FsErpsRingPort2RapsEventPduRxCount_Object = MibTableColumn
fsErpsRingPort2RapsEventPduRxCount = _FsErpsRingPort2RapsEventPduRxCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 40, 3, 4, 1, 28),
    _FsErpsRingPort2RapsEventPduRxCount_Type()
)
fsErpsRingPort2RapsEventPduRxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsErpsRingPort2RapsEventPduRxCount.setStatus("current")
_FsErpsRingPort2RapsEventPduTxCount_Type = Counter32
_FsErpsRingPort2RapsEventPduTxCount_Object = MibTableColumn
fsErpsRingPort2RapsEventPduTxCount = _FsErpsRingPort2RapsEventPduTxCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 40, 3, 4, 1, 29),
    _FsErpsRingPort2RapsEventPduTxCount_Type()
)
fsErpsRingPort2RapsEventPduTxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsErpsRingPort2RapsEventPduTxCount.setStatus("current")
_FsErpsRingPort1RapsSFPduRxCount_Type = Counter32
_FsErpsRingPort1RapsSFPduRxCount_Object = MibTableColumn
fsErpsRingPort1RapsSFPduRxCount = _FsErpsRingPort1RapsSFPduRxCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 40, 3, 4, 1, 30),
    _FsErpsRingPort1RapsSFPduRxCount_Type()
)
fsErpsRingPort1RapsSFPduRxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsErpsRingPort1RapsSFPduRxCount.setStatus("current")
_FsErpsRingPort1RapsSFPduTxCount_Type = Counter32
_FsErpsRingPort1RapsSFPduTxCount_Object = MibTableColumn
fsErpsRingPort1RapsSFPduTxCount = _FsErpsRingPort1RapsSFPduTxCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 40, 3, 4, 1, 31),
    _FsErpsRingPort1RapsSFPduTxCount_Type()
)
fsErpsRingPort1RapsSFPduTxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsErpsRingPort1RapsSFPduTxCount.setStatus("current")
_FsErpsRingPort2RapsSFPduRxCount_Type = Counter32
_FsErpsRingPort2RapsSFPduRxCount_Object = MibTableColumn
fsErpsRingPort2RapsSFPduRxCount = _FsErpsRingPort2RapsSFPduRxCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 40, 3, 4, 1, 32),
    _FsErpsRingPort2RapsSFPduRxCount_Type()
)
fsErpsRingPort2RapsSFPduRxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsErpsRingPort2RapsSFPduRxCount.setStatus("current")
_FsErpsRingPort2RapsSFPduTxCount_Type = Counter32
_FsErpsRingPort2RapsSFPduTxCount_Object = MibTableColumn
fsErpsRingPort2RapsSFPduTxCount = _FsErpsRingPort2RapsSFPduTxCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 40, 3, 4, 1, 33),
    _FsErpsRingPort2RapsSFPduTxCount_Type()
)
fsErpsRingPort2RapsSFPduTxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsErpsRingPort2RapsSFPduTxCount.setStatus("current")
_FsErpsRingPort1RapsNRPduRxCount_Type = Counter32
_FsErpsRingPort1RapsNRPduRxCount_Object = MibTableColumn
fsErpsRingPort1RapsNRPduRxCount = _FsErpsRingPort1RapsNRPduRxCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 40, 3, 4, 1, 34),
    _FsErpsRingPort1RapsNRPduRxCount_Type()
)
fsErpsRingPort1RapsNRPduRxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsErpsRingPort1RapsNRPduRxCount.setStatus("current")
_FsErpsRingPort1RapsNRPduTxCount_Type = Counter32
_FsErpsRingPort1RapsNRPduTxCount_Object = MibTableColumn
fsErpsRingPort1RapsNRPduTxCount = _FsErpsRingPort1RapsNRPduTxCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 40, 3, 4, 1, 35),
    _FsErpsRingPort1RapsNRPduTxCount_Type()
)
fsErpsRingPort1RapsNRPduTxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsErpsRingPort1RapsNRPduTxCount.setStatus("current")
_FsErpsRingPort2RapsNRPduRxCount_Type = Counter32
_FsErpsRingPort2RapsNRPduRxCount_Object = MibTableColumn
fsErpsRingPort2RapsNRPduRxCount = _FsErpsRingPort2RapsNRPduRxCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 40, 3, 4, 1, 36),
    _FsErpsRingPort2RapsNRPduRxCount_Type()
)
fsErpsRingPort2RapsNRPduRxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsErpsRingPort2RapsNRPduRxCount.setStatus("current")
_FsErpsRingPort2RapsNRPduTxCount_Type = Counter32
_FsErpsRingPort2RapsNRPduTxCount_Object = MibTableColumn
fsErpsRingPort2RapsNRPduTxCount = _FsErpsRingPort2RapsNRPduTxCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 40, 3, 4, 1, 37),
    _FsErpsRingPort2RapsNRPduTxCount_Type()
)
fsErpsRingPort2RapsNRPduTxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsErpsRingPort2RapsNRPduTxCount.setStatus("current")
_FsErpsRingPort1RapsNRRBPduRxCount_Type = Counter32
_FsErpsRingPort1RapsNRRBPduRxCount_Object = MibTableColumn
fsErpsRingPort1RapsNRRBPduRxCount = _FsErpsRingPort1RapsNRRBPduRxCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 40, 3, 4, 1, 38),
    _FsErpsRingPort1RapsNRRBPduRxCount_Type()
)
fsErpsRingPort1RapsNRRBPduRxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsErpsRingPort1RapsNRRBPduRxCount.setStatus("current")
_FsErpsRingPort1RapsNRRBPduTxCount_Type = Counter32
_FsErpsRingPort1RapsNRRBPduTxCount_Object = MibTableColumn
fsErpsRingPort1RapsNRRBPduTxCount = _FsErpsRingPort1RapsNRRBPduTxCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 40, 3, 4, 1, 39),
    _FsErpsRingPort1RapsNRRBPduTxCount_Type()
)
fsErpsRingPort1RapsNRRBPduTxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsErpsRingPort1RapsNRRBPduTxCount.setStatus("current")
_FsErpsRingPort2RapsNRRBPduRxCount_Type = Counter32
_FsErpsRingPort2RapsNRRBPduRxCount_Object = MibTableColumn
fsErpsRingPort2RapsNRRBPduRxCount = _FsErpsRingPort2RapsNRRBPduRxCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 40, 3, 4, 1, 40),
    _FsErpsRingPort2RapsNRRBPduRxCount_Type()
)
fsErpsRingPort2RapsNRRBPduRxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsErpsRingPort2RapsNRRBPduRxCount.setStatus("current")
_FsErpsRingPort2RapsNRRBPduTxCount_Type = Counter32
_FsErpsRingPort2RapsNRRBPduTxCount_Object = MibTableColumn
fsErpsRingPort2RapsNRRBPduTxCount = _FsErpsRingPort2RapsNRRBPduTxCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 40, 3, 4, 1, 41),
    _FsErpsRingPort2RapsNRRBPduTxCount_Type()
)
fsErpsRingPort2RapsNRRBPduTxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsErpsRingPort2RapsNRRBPduTxCount.setStatus("current")
_FsErpsRingGeneratedTrapsCount_Type = Counter32
_FsErpsRingGeneratedTrapsCount_Object = MibTableColumn
fsErpsRingGeneratedTrapsCount = _FsErpsRingGeneratedTrapsCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 40, 3, 4, 1, 42),
    _FsErpsRingGeneratedTrapsCount_Type()
)
fsErpsRingGeneratedTrapsCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsErpsRingGeneratedTrapsCount.setStatus("current")
_FsErpsRingPort1DefectEncTimeSec_Type = Unsigned32
_FsErpsRingPort1DefectEncTimeSec_Object = MibTableColumn
fsErpsRingPort1DefectEncTimeSec = _FsErpsRingPort1DefectEncTimeSec_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 40, 3, 4, 1, 43),
    _FsErpsRingPort1DefectEncTimeSec_Type()
)
fsErpsRingPort1DefectEncTimeSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsErpsRingPort1DefectEncTimeSec.setStatus("current")
_FsErpsRingPort2DefectEncTimeSec_Type = Unsigned32
_FsErpsRingPort2DefectEncTimeSec_Object = MibTableColumn
fsErpsRingPort2DefectEncTimeSec = _FsErpsRingPort2DefectEncTimeSec_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 40, 3, 4, 1, 44),
    _FsErpsRingPort2DefectEncTimeSec_Type()
)
fsErpsRingPort2DefectEncTimeSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsErpsRingPort2DefectEncTimeSec.setStatus("current")
_FsErpsRingPort1DefectClearedTimeSec_Type = Unsigned32
_FsErpsRingPort1DefectClearedTimeSec_Object = MibTableColumn
fsErpsRingPort1DefectClearedTimeSec = _FsErpsRingPort1DefectClearedTimeSec_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 40, 3, 4, 1, 45),
    _FsErpsRingPort1DefectClearedTimeSec_Type()
)
fsErpsRingPort1DefectClearedTimeSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsErpsRingPort1DefectClearedTimeSec.setStatus("current")
_FsErpsRingPort2DefectClearedTimeSec_Type = Unsigned32
_FsErpsRingPort2DefectClearedTimeSec_Object = MibTableColumn
fsErpsRingPort2DefectClearedTimeSec = _FsErpsRingPort2DefectClearedTimeSec_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 40, 3, 4, 1, 46),
    _FsErpsRingPort2DefectClearedTimeSec_Type()
)
fsErpsRingPort2DefectClearedTimeSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsErpsRingPort2DefectClearedTimeSec.setStatus("current")
_FsErpsRingRplPortStatChgTimeSec_Type = Unsigned32
_FsErpsRingRplPortStatChgTimeSec_Object = MibTableColumn
fsErpsRingRplPortStatChgTimeSec = _FsErpsRingRplPortStatChgTimeSec_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 40, 3, 4, 1, 47),
    _FsErpsRingRplPortStatChgTimeSec_Type()
)
fsErpsRingRplPortStatChgTimeSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsErpsRingRplPortStatChgTimeSec.setStatus("current")
_FsErpsRingRplNbrPortStatChgTime_Type = Unsigned32
_FsErpsRingRplNbrPortStatChgTime_Object = MibTableColumn
fsErpsRingRplNbrPortStatChgTime = _FsErpsRingRplNbrPortStatChgTime_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 40, 3, 4, 1, 48),
    _FsErpsRingRplNbrPortStatChgTime_Type()
)
fsErpsRingRplNbrPortStatChgTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsErpsRingRplNbrPortStatChgTime.setStatus("current")
_FsErpsRingDistPortPduRxCount_Type = Counter32
_FsErpsRingDistPortPduRxCount_Object = MibTableColumn
fsErpsRingDistPortPduRxCount = _FsErpsRingDistPortPduRxCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 40, 3, 4, 1, 49),
    _FsErpsRingDistPortPduRxCount_Type()
)
fsErpsRingDistPortPduRxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsErpsRingDistPortPduRxCount.setStatus("current")
_FsErpsRingDistPortPduTxCount_Type = Counter32
_FsErpsRingDistPortPduTxCount_Object = MibTableColumn
fsErpsRingDistPortPduTxCount = _FsErpsRingDistPortPduTxCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 40, 3, 4, 1, 50),
    _FsErpsRingDistPortPduTxCount_Type()
)
fsErpsRingDistPortPduTxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsErpsRingDistPortPduTxCount.setStatus("current")
_FsErpsRingRapsPort1DefectEncTimeNSec_Type = Unsigned32
_FsErpsRingRapsPort1DefectEncTimeNSec_Object = MibTableColumn
fsErpsRingRapsPort1DefectEncTimeNSec = _FsErpsRingRapsPort1DefectEncTimeNSec_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 40, 3, 4, 1, 51),
    _FsErpsRingRapsPort1DefectEncTimeNSec_Type()
)
fsErpsRingRapsPort1DefectEncTimeNSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsErpsRingRapsPort1DefectEncTimeNSec.setStatus("current")
_FsErpsRingRapsPort1DefectClearedTimeNSec_Type = Unsigned32
_FsErpsRingRapsPort1DefectClearedTimeNSec_Object = MibTableColumn
fsErpsRingRapsPort1DefectClearedTimeNSec = _FsErpsRingRapsPort1DefectClearedTimeNSec_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 40, 3, 4, 1, 52),
    _FsErpsRingRapsPort1DefectClearedTimeNSec_Type()
)
fsErpsRingRapsPort1DefectClearedTimeNSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsErpsRingRapsPort1DefectClearedTimeNSec.setStatus("current")
_FsErpsRingRapsPort2DefectEncTimeNSec_Type = Unsigned32
_FsErpsRingRapsPort2DefectEncTimeNSec_Object = MibTableColumn
fsErpsRingRapsPort2DefectEncTimeNSec = _FsErpsRingRapsPort2DefectEncTimeNSec_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 40, 3, 4, 1, 53),
    _FsErpsRingRapsPort2DefectEncTimeNSec_Type()
)
fsErpsRingRapsPort2DefectEncTimeNSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsErpsRingRapsPort2DefectEncTimeNSec.setStatus("current")
_FsErpsRingRapsPort2DefectClearedTimeNSec_Type = Unsigned32
_FsErpsRingRapsPort2DefectClearedTimeNSec_Object = MibTableColumn
fsErpsRingRapsPort2DefectClearedTimeNSec = _FsErpsRingRapsPort2DefectClearedTimeNSec_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 40, 3, 4, 1, 54),
    _FsErpsRingRapsPort2DefectClearedTimeNSec_Type()
)
fsErpsRingRapsPort2DefectClearedTimeNSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsErpsRingRapsPort2DefectClearedTimeNSec.setStatus("current")
_FsErpsRingRapsRplPortStatChgTimeNSec_Type = Unsigned32
_FsErpsRingRapsRplPortStatChgTimeNSec_Object = MibTableColumn
fsErpsRingRapsRplPortStatChgTimeNSec = _FsErpsRingRapsRplPortStatChgTimeNSec_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 40, 3, 4, 1, 55),
    _FsErpsRingRapsRplPortStatChgTimeNSec_Type()
)
fsErpsRingRapsRplPortStatChgTimeNSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsErpsRingRapsRplPortStatChgTimeNSec.setStatus("current")
_FsErpsRingDefectSwitchOverTimeMSec_Type = Unsigned32
_FsErpsRingDefectSwitchOverTimeMSec_Object = MibTableColumn
fsErpsRingDefectSwitchOverTimeMSec = _FsErpsRingDefectSwitchOverTimeMSec_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 40, 3, 4, 1, 56),
    _FsErpsRingDefectSwitchOverTimeMSec_Type()
)
fsErpsRingDefectSwitchOverTimeMSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsErpsRingDefectSwitchOverTimeMSec.setStatus("current")
_FsErpsRingDefectClearedSwitchOverTimeMSec_Type = Unsigned32
_FsErpsRingDefectClearedSwitchOverTimeMSec_Object = MibTableColumn
fsErpsRingDefectClearedSwitchOverTimeMSec = _FsErpsRingDefectClearedSwitchOverTimeMSec_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 40, 3, 4, 1, 57),
    _FsErpsRingDefectClearedSwitchOverTimeMSec_Type()
)
fsErpsRingDefectClearedSwitchOverTimeMSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsErpsRingDefectClearedSwitchOverTimeMSec.setStatus("current")
_FsErpsNotifications_ObjectIdentity = ObjectIdentity
fsErpsNotifications = _FsErpsNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 40, 4)
)
_FsErpsTraps_ObjectIdentity = ObjectIdentity
fsErpsTraps = _FsErpsTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 40, 4, 0)
)


class _FsErpsTypeOfFailure_Type(DisplayString):
    """Custom type fsErpsTypeOfFailure based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_FsErpsTypeOfFailure_Type.__name__ = "DisplayString"
_FsErpsTypeOfFailure_Object = MibScalar
fsErpsTypeOfFailure = _FsErpsTypeOfFailure_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 40, 4, 1),
    _FsErpsTypeOfFailure_Type()
)
fsErpsTypeOfFailure.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsErpsTypeOfFailure.setStatus("current")


class _FsErpsTrapSwitchingMechanism_Type(DisplayString):
    """Custom type fsErpsTrapSwitchingMechanism based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_FsErpsTrapSwitchingMechanism_Type.__name__ = "DisplayString"
_FsErpsTrapSwitchingMechanism_Object = MibScalar
fsErpsTrapSwitchingMechanism = _FsErpsTrapSwitchingMechanism_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 40, 4, 2),
    _FsErpsTrapSwitchingMechanism_Type()
)
fsErpsTrapSwitchingMechanism.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsErpsTrapSwitchingMechanism.setStatus("current")

# Managed Objects groups


# Notification objects

fsErpsStateChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 40, 4, 0, 1)
)
fsErpsStateChangeTrap.setObjects(
      *(("SUPERMICRO-ERPS-MIB", "fsErpsCtxtName"),
        ("SUPERMICRO-ERPS-MIB", "fsErpsRingName"),
        ("SUPERMICRO-ERPS-MIB", "fsErpsTrapSwitchingMechanism"),
        ("SUPERMICRO-ERPS-MIB", "fsErpsRingSemState"),
        ("SUPERMICRO-ERPS-MIB", "fsErpsRingNodeStatus"))
)
if mibBuilder.loadTexts:
    fsErpsStateChangeTrap.setStatus(
        "current"
    )

fsErpsFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 40, 4, 0, 2)
)
fsErpsFailureTrap.setObjects(
      *(("SUPERMICRO-ERPS-MIB", "fsErpsCtxtName"),
        ("SUPERMICRO-ERPS-MIB", "fsErpsRingName"),
        ("SUPERMICRO-ERPS-MIB", "fsErpsTypeOfFailure"))
)
if mibBuilder.loadTexts:
    fsErpsFailureTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SUPERMICRO-ERPS-MIB",
    **{"RingId": RingId,
       "RingMonitorMechanismType": RingMonitorMechanismType,
       "RingIdOrNone": RingIdOrNone,
       "RingServiceType": RingServiceType,
       "fsErpsMIB": fsErpsMIB,
       "fsErpsContext": fsErpsContext,
       "fsErpsContextTable": fsErpsContextTable,
       "fsErpsContextEntry": fsErpsContextEntry,
       "fsErpsContextId": fsErpsContextId,
       "fsErpsCtxtName": fsErpsCtxtName,
       "fsErpsCtxtSystemControl": fsErpsCtxtSystemControl,
       "fsErpsCtxtModuleStatus": fsErpsCtxtModuleStatus,
       "fsErpsCtxtTraceInput": fsErpsCtxtTraceInput,
       "fsErpsCtxtTrapStatus": fsErpsCtxtTrapStatus,
       "fsErpsCtxtClearRingStats": fsErpsCtxtClearRingStats,
       "fsErpsCtxtRowStatus": fsErpsCtxtRowStatus,
       "fsErpsCtxtVlanGroupManager": fsErpsCtxtVlanGroupManager,
       "fsErpsCtxtProprietaryClearFS": fsErpsCtxtProprietaryClearFS,
       "fsErpsVlanGroupTable": fsErpsVlanGroupTable,
       "fsErpsVlanGroupEntry": fsErpsVlanGroupEntry,
       "fsErpsVlanId": fsErpsVlanId,
       "fsErpsVlanGroupId": fsErpsVlanGroupId,
       "fsErpsVlanGroupRowStatus": fsErpsVlanGroupRowStatus,
       "fsErpsRing": fsErpsRing,
       "fsErpsRingTable": fsErpsRingTable,
       "fsErpsRingEntry": fsErpsRingEntry,
       "fsErpsRingId": fsErpsRingId,
       "fsErpsRingVlanId": fsErpsRingVlanId,
       "fsErpsRingName": fsErpsRingName,
       "fsErpsRingPort1": fsErpsRingPort1,
       "fsErpsRingPort2": fsErpsRingPort2,
       "fsErpsRingRplPort": fsErpsRingRplPort,
       "fsErpsRingPortBlockingOnVcRecovery": fsErpsRingPortBlockingOnVcRecovery,
       "fsErpsRingNodeType": fsErpsRingNodeType,
       "fsErpsRingOperatingMode": fsErpsRingOperatingMode,
       "fsErpsRingMonitorMechanism": fsErpsRingMonitorMechanism,
       "fsErpsRingPort1Status": fsErpsRingPort1Status,
       "fsErpsRingPort2Status": fsErpsRingPort2Status,
       "fsErpsRingSemState": fsErpsRingSemState,
       "fsErpsRingNodeStatus": fsErpsRingNodeStatus,
       "fsErpsRingRowStatus": fsErpsRingRowStatus,
       "fsErpsRingMacId": fsErpsRingMacId,
       "fsErpsRingProtectedVlanGroupId": fsErpsRingProtectedVlanGroupId,
       "fsErpsRingProtectionType": fsErpsRingProtectionType,
       "fsErpsRingRAPSCompatibleVersion": fsErpsRingRAPSCompatibleVersion,
       "fsErpsRingRplNeighbourPort": fsErpsRingRplNeighbourPort,
       "fsErpsRingRAPSSubRingWithoutVC": fsErpsRingRAPSSubRingWithoutVC,
       "fsErpsRingRplNextNeighbourPort": fsErpsRingRplNextNeighbourPort,
       "fsErpsRingPort1NodeID": fsErpsRingPort1NodeID,
       "fsErpsRingPort2NodeID": fsErpsRingPort2NodeID,
       "fsErpsRingPort1BPRBitVal": fsErpsRingPort1BPRBitVal,
       "fsErpsRingPort2BPRBitVal": fsErpsRingPort2BPRBitVal,
       "fsErpsRingProtectedVlanGroupList": fsErpsRingProtectedVlanGroupList,
       "fsErpsRingServiceType": fsErpsRingServiceType,
       "fsErpsRingPort1SubPortList": fsErpsRingPort1SubPortList,
       "fsErpsRingPort2SubPortList": fsErpsRingPort2SubPortList,
       "fsErpsRingCfmTable": fsErpsRingCfmTable,
       "fsErpsRingCfmEntry": fsErpsRingCfmEntry,
       "fsErpsRingMEG1": fsErpsRingMEG1,
       "fsErpsRingCfmME1": fsErpsRingCfmME1,
       "fsErpsRingCfmMEP1": fsErpsRingCfmMEP1,
       "fsErpsRingMEG2": fsErpsRingMEG2,
       "fsErpsRingCfmME2": fsErpsRingCfmME2,
       "fsErpsRingCfmMEP2": fsErpsRingCfmMEP2,
       "fsErpsRingCfmRowStatus": fsErpsRingCfmRowStatus,
       "fsErpsRingConfigTable": fsErpsRingConfigTable,
       "fsErpsRingConfigEntry": fsErpsRingConfigEntry,
       "fsErpsRingConfigHoldOffTime": fsErpsRingConfigHoldOffTime,
       "fsErpsRingConfigGuardTime": fsErpsRingConfigGuardTime,
       "fsErpsRingConfigWTRTime": fsErpsRingConfigWTRTime,
       "fsErpsRingConfigPeriodicTime": fsErpsRingConfigPeriodicTime,
       "fsErpsRingConfigSwitchPort": fsErpsRingConfigSwitchPort,
       "fsErpsRingConfigSwitchCmd": fsErpsRingConfigSwitchCmd,
       "fsErpsRingConfigRecoveryMethod": fsErpsRingConfigRecoveryMethod,
       "fsErpsRingConfigPropagateTC": fsErpsRingConfigPropagateTC,
       "fsErpsRingConfigWTBTime": fsErpsRingConfigWTBTime,
       "fsErpsRingConfigClear": fsErpsRingConfigClear,
       "fsErpsRingConfigInterConnNode": fsErpsRingConfigInterConnNode,
       "fsErpsRingConfigMultipleFailure": fsErpsRingConfigMultipleFailure,
       "fsErpsRingConfigIsPort1Present": fsErpsRingConfigIsPort1Present,
       "fsErpsRingConfigIsPort2Present": fsErpsRingConfigIsPort2Present,
       "fsErpsRingConfigInfoDistributingPort": fsErpsRingConfigInfoDistributingPort,
       "fsErpsRingConfigKValue": fsErpsRingConfigKValue,
       "fsErpsRingConfigFailureOfProtocol": fsErpsRingConfigFailureOfProtocol,
       "fsErpsRingTcPropTable": fsErpsRingTcPropTable,
       "fsErpsRingTcPropEntry": fsErpsRingTcPropEntry,
       "fsErpsRingTcPropRingId": fsErpsRingTcPropRingId,
       "fsErpsRingTcPropRowStatus": fsErpsRingTcPropRowStatus,
       "fsErpsRingConfigExtTable": fsErpsRingConfigExtTable,
       "fsErpsRingConfigExtEntry": fsErpsRingConfigExtEntry,
       "fsErpsRingConfigExtVCRecoveryPeriodicTime": fsErpsRingConfigExtVCRecoveryPeriodicTime,
       "fsErpsRingConfigExtMainRingId": fsErpsRingConfigExtMainRingId,
       "fsErpsStats": fsErpsStats,
       "fsErpsMemFailCount": fsErpsMemFailCount,
       "fsErpsBufFailCount": fsErpsBufFailCount,
       "fsErpsTimerFailCount": fsErpsTimerFailCount,
       "fsErpsRingStatsTable": fsErpsRingStatsTable,
       "fsErpsRingStatsEntry": fsErpsRingStatsEntry,
       "fsErpsRingClearRingStats": fsErpsRingClearRingStats,
       "fsErpsRingPort1RapsPduSentCount": fsErpsRingPort1RapsPduSentCount,
       "fsErpsRingPort2RapsPduSentCount": fsErpsRingPort2RapsPduSentCount,
       "fsErpsRingPort1RapsPduRcvdCount": fsErpsRingPort1RapsPduRcvdCount,
       "fsErpsRingPort2RapsPduRcvdCount": fsErpsRingPort2RapsPduRcvdCount,
       "fsErpsRingPort1RapsPduDiscardCount": fsErpsRingPort1RapsPduDiscardCount,
       "fsErpsRingPort2RapsPduDiscardCount": fsErpsRingPort2RapsPduDiscardCount,
       "fsErpsRingPort1BlockedCount": fsErpsRingPort1BlockedCount,
       "fsErpsRingPort2BlockedCount": fsErpsRingPort2BlockedCount,
       "fsErpsRingPort1UnblockedCount": fsErpsRingPort1UnblockedCount,
       "fsErpsRingPort2UnblockedCount": fsErpsRingPort2UnblockedCount,
       "fsErpsRingPort1FailedCount": fsErpsRingPort1FailedCount,
       "fsErpsRingPort2FailedCount": fsErpsRingPort2FailedCount,
       "fsErpsRingPort1RecoveredCount": fsErpsRingPort1RecoveredCount,
       "fsErpsRingPort2RecoveredCount": fsErpsRingPort2RecoveredCount,
       "fsErpsRingPort1VersionDiscardCount": fsErpsRingPort1VersionDiscardCount,
       "fsErpsRingPort2VersionDiscardCount": fsErpsRingPort2VersionDiscardCount,
       "fsErpsRingPort1RapsFSPduRxCount": fsErpsRingPort1RapsFSPduRxCount,
       "fsErpsRingPort1RapsFSPduTxCount": fsErpsRingPort1RapsFSPduTxCount,
       "fsErpsRingPort2RapsFSPduRxCount": fsErpsRingPort2RapsFSPduRxCount,
       "fsErpsRingPort2RapsFSPduTxCount": fsErpsRingPort2RapsFSPduTxCount,
       "fsErpsRingPort1RapsMSPduRxCount": fsErpsRingPort1RapsMSPduRxCount,
       "fsErpsRingPort1RapsMSPduTxCount": fsErpsRingPort1RapsMSPduTxCount,
       "fsErpsRingPort2RapsMSPduRxCount": fsErpsRingPort2RapsMSPduRxCount,
       "fsErpsRingPort2RapsMSPduTxCount": fsErpsRingPort2RapsMSPduTxCount,
       "fsErpsRingPort1RapsEventPduRxCount": fsErpsRingPort1RapsEventPduRxCount,
       "fsErpsRingPort1RapsEventPduTxCount": fsErpsRingPort1RapsEventPduTxCount,
       "fsErpsRingPort2RapsEventPduRxCount": fsErpsRingPort2RapsEventPduRxCount,
       "fsErpsRingPort2RapsEventPduTxCount": fsErpsRingPort2RapsEventPduTxCount,
       "fsErpsRingPort1RapsSFPduRxCount": fsErpsRingPort1RapsSFPduRxCount,
       "fsErpsRingPort1RapsSFPduTxCount": fsErpsRingPort1RapsSFPduTxCount,
       "fsErpsRingPort2RapsSFPduRxCount": fsErpsRingPort2RapsSFPduRxCount,
       "fsErpsRingPort2RapsSFPduTxCount": fsErpsRingPort2RapsSFPduTxCount,
       "fsErpsRingPort1RapsNRPduRxCount": fsErpsRingPort1RapsNRPduRxCount,
       "fsErpsRingPort1RapsNRPduTxCount": fsErpsRingPort1RapsNRPduTxCount,
       "fsErpsRingPort2RapsNRPduRxCount": fsErpsRingPort2RapsNRPduRxCount,
       "fsErpsRingPort2RapsNRPduTxCount": fsErpsRingPort2RapsNRPduTxCount,
       "fsErpsRingPort1RapsNRRBPduRxCount": fsErpsRingPort1RapsNRRBPduRxCount,
       "fsErpsRingPort1RapsNRRBPduTxCount": fsErpsRingPort1RapsNRRBPduTxCount,
       "fsErpsRingPort2RapsNRRBPduRxCount": fsErpsRingPort2RapsNRRBPduRxCount,
       "fsErpsRingPort2RapsNRRBPduTxCount": fsErpsRingPort2RapsNRRBPduTxCount,
       "fsErpsRingGeneratedTrapsCount": fsErpsRingGeneratedTrapsCount,
       "fsErpsRingPort1DefectEncTimeSec": fsErpsRingPort1DefectEncTimeSec,
       "fsErpsRingPort2DefectEncTimeSec": fsErpsRingPort2DefectEncTimeSec,
       "fsErpsRingPort1DefectClearedTimeSec": fsErpsRingPort1DefectClearedTimeSec,
       "fsErpsRingPort2DefectClearedTimeSec": fsErpsRingPort2DefectClearedTimeSec,
       "fsErpsRingRplPortStatChgTimeSec": fsErpsRingRplPortStatChgTimeSec,
       "fsErpsRingRplNbrPortStatChgTime": fsErpsRingRplNbrPortStatChgTime,
       "fsErpsRingDistPortPduRxCount": fsErpsRingDistPortPduRxCount,
       "fsErpsRingDistPortPduTxCount": fsErpsRingDistPortPduTxCount,
       "fsErpsRingRapsPort1DefectEncTimeNSec": fsErpsRingRapsPort1DefectEncTimeNSec,
       "fsErpsRingRapsPort1DefectClearedTimeNSec": fsErpsRingRapsPort1DefectClearedTimeNSec,
       "fsErpsRingRapsPort2DefectEncTimeNSec": fsErpsRingRapsPort2DefectEncTimeNSec,
       "fsErpsRingRapsPort2DefectClearedTimeNSec": fsErpsRingRapsPort2DefectClearedTimeNSec,
       "fsErpsRingRapsRplPortStatChgTimeNSec": fsErpsRingRapsRplPortStatChgTimeNSec,
       "fsErpsRingDefectSwitchOverTimeMSec": fsErpsRingDefectSwitchOverTimeMSec,
       "fsErpsRingDefectClearedSwitchOverTimeMSec": fsErpsRingDefectClearedSwitchOverTimeMSec,
       "fsErpsNotifications": fsErpsNotifications,
       "fsErpsTraps": fsErpsTraps,
       "fsErpsStateChangeTrap": fsErpsStateChangeTrap,
       "fsErpsFailureTrap": fsErpsFailureTrap,
       "fsErpsTypeOfFailure": fsErpsTypeOfFailure,
       "fsErpsTrapSwitchingMechanism": fsErpsTrapSwitchingMechanism}
)
