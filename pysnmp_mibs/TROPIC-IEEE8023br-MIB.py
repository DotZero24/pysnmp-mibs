# SNMP MIB module (TROPIC-IEEE8023br-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/nokia/TROPIC-IEEE8023br-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:53:03 2025
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
 PhysAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")

(TmnxPortID,) = mibBuilder.importSymbols(
    "TN-TC-MIB",
    "TmnxPortID")

(tnIEEE8023brMIB,
 tnPortModules) = mibBuilder.importSymbols(
    "TROPIC-GLOBAL-REG",
    "tnIEEE8023brMIB",
    "tnPortModules")


# MODULE-IDENTITY

tnIEEE8023brMibModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 1, 1, 2, 2, 4, 9)
)
if mibBuilder.loadTexts:
    tnIEEE8023brMibModule.setRevisions(
        ("2016-08-15 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TnIEEE8023brEquipmentObjectsNotifications_ObjectIdentity = ObjectIdentity
tnIEEE8023brEquipmentObjectsNotifications = _TnIEEE8023brEquipmentObjectsNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 11, 0)
)
_TnIEEE8023brObjects_ObjectIdentity = ObjectIdentity
tnIEEE8023brObjects = _TnIEEE8023brObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 11, 1)
)
_TnIEEE8023brObjectsParameters_ObjectIdentity = ObjectIdentity
tnIEEE8023brObjectsParameters = _TnIEEE8023brObjectsParameters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 11, 1, 1)
)
_LldpXdot3LocSystemsGroupTable_Object = MibTable
lldpXdot3LocSystemsGroupTable = _LldpXdot3LocSystemsGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 11, 1, 1, 1)
)
if mibBuilder.loadTexts:
    lldpXdot3LocSystemsGroupTable.setStatus("current")
_LldpXdot3LocSystemsGroupEntry_Object = MibTableRow
lldpXdot3LocSystemsGroupEntry = _LldpXdot3LocSystemsGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 11, 1, 1, 1, 1)
)
lldpXdot3LocSystemsGroupEntry.setIndexNames(
    (0, "TROPIC-IEEE8023br-MIB", "aLldpXdot3LocPortID"),
)
if mibBuilder.loadTexts:
    lldpXdot3LocSystemsGroupEntry.setStatus("current")
_ALldpXdot3LocPortID_Type = TmnxPortID
_ALldpXdot3LocPortID_Object = MibTableColumn
aLldpXdot3LocPortID = _ALldpXdot3LocPortID_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 11, 1, 1, 1, 1, 1),
    _ALldpXdot3LocPortID_Type()
)
aLldpXdot3LocPortID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aLldpXdot3LocPortID.setStatus("current")
_ALldpXdot3LocPreemptSupported_Type = TruthValue
_ALldpXdot3LocPreemptSupported_Object = MibTableColumn
aLldpXdot3LocPreemptSupported = _ALldpXdot3LocPreemptSupported_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 11, 1, 1, 1, 1, 2),
    _ALldpXdot3LocPreemptSupported_Type()
)
aLldpXdot3LocPreemptSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aLldpXdot3LocPreemptSupported.setStatus("current")
_ALldpXdot3LocPreemptEnabled_Type = TruthValue
_ALldpXdot3LocPreemptEnabled_Object = MibTableColumn
aLldpXdot3LocPreemptEnabled = _ALldpXdot3LocPreemptEnabled_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 11, 1, 1, 1, 1, 3),
    _ALldpXdot3LocPreemptEnabled_Type()
)
aLldpXdot3LocPreemptEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aLldpXdot3LocPreemptEnabled.setStatus("current")
_ALldpXdot3LocPreemptActive_Type = TruthValue
_ALldpXdot3LocPreemptActive_Object = MibTableColumn
aLldpXdot3LocPreemptActive = _ALldpXdot3LocPreemptActive_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 11, 1, 1, 1, 1, 4),
    _ALldpXdot3LocPreemptActive_Type()
)
aLldpXdot3LocPreemptActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aLldpXdot3LocPreemptActive.setStatus("current")
_ALldpXdot3LocAddFragSize_Type = TruthValue
_ALldpXdot3LocAddFragSize_Object = MibTableColumn
aLldpXdot3LocAddFragSize = _ALldpXdot3LocAddFragSize_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 11, 1, 1, 1, 1, 5),
    _ALldpXdot3LocAddFragSize_Type()
)
aLldpXdot3LocAddFragSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aLldpXdot3LocAddFragSize.setStatus("current")
_LldpXdot3RemSystemsGroupTable_Object = MibTable
lldpXdot3RemSystemsGroupTable = _LldpXdot3RemSystemsGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 11, 1, 1, 2)
)
if mibBuilder.loadTexts:
    lldpXdot3RemSystemsGroupTable.setStatus("current")
_LldpXdot3RemSystemsGroupEntry_Object = MibTableRow
lldpXdot3RemSystemsGroupEntry = _LldpXdot3RemSystemsGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 11, 1, 1, 2, 1)
)
lldpXdot3RemSystemsGroupEntry.setIndexNames(
    (0, "TROPIC-IEEE8023br-MIB", "aLldpXdot3RemPortID"),
)
if mibBuilder.loadTexts:
    lldpXdot3RemSystemsGroupEntry.setStatus("current")
_ALldpXdot3RemPortID_Type = TmnxPortID
_ALldpXdot3RemPortID_Object = MibTableColumn
aLldpXdot3RemPortID = _ALldpXdot3RemPortID_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 11, 1, 1, 2, 1, 1),
    _ALldpXdot3RemPortID_Type()
)
aLldpXdot3RemPortID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aLldpXdot3RemPortID.setStatus("current")
_ALldpXdot3RemPreemptSupported_Type = TruthValue
_ALldpXdot3RemPreemptSupported_Object = MibTableColumn
aLldpXdot3RemPreemptSupported = _ALldpXdot3RemPreemptSupported_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 11, 1, 1, 2, 1, 2),
    _ALldpXdot3RemPreemptSupported_Type()
)
aLldpXdot3RemPreemptSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aLldpXdot3RemPreemptSupported.setStatus("current")
_ALldpXdot3RemPreemptEnabled_Type = TruthValue
_ALldpXdot3RemPreemptEnabled_Object = MibTableColumn
aLldpXdot3RemPreemptEnabled = _ALldpXdot3RemPreemptEnabled_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 11, 1, 1, 2, 1, 3),
    _ALldpXdot3RemPreemptEnabled_Type()
)
aLldpXdot3RemPreemptEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aLldpXdot3RemPreemptEnabled.setStatus("current")
_ALldpXdot3RemPreemptActive_Type = TruthValue
_ALldpXdot3RemPreemptActive_Object = MibTableColumn
aLldpXdot3RemPreemptActive = _ALldpXdot3RemPreemptActive_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 11, 1, 1, 2, 1, 4),
    _ALldpXdot3RemPreemptActive_Type()
)
aLldpXdot3RemPreemptActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aLldpXdot3RemPreemptActive.setStatus("current")
_ALldpXdot3RemAddFragSize_Type = TruthValue
_ALldpXdot3RemAddFragSize_Object = MibTableColumn
aLldpXdot3RemAddFragSize = _ALldpXdot3RemAddFragSize_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 11, 1, 1, 2, 1, 5),
    _ALldpXdot3RemAddFragSize_Type()
)
aLldpXdot3RemAddFragSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aLldpXdot3RemAddFragSize.setStatus("current")
_MacMergeEntityTable_Object = MibTable
macMergeEntityTable = _MacMergeEntityTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 11, 1, 1, 3)
)
if mibBuilder.loadTexts:
    macMergeEntityTable.setStatus("current")
_MacMergeEntityEntry_Object = MibTableRow
macMergeEntityEntry = _MacMergeEntityEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 11, 1, 1, 3, 1)
)
macMergeEntityEntry.setIndexNames(
    (0, "TROPIC-IEEE8023br-MIB", "aMACMergePortID"),
)
if mibBuilder.loadTexts:
    macMergeEntityEntry.setStatus("current")
_AMACMergePortID_Type = TmnxPortID
_AMACMergePortID_Object = MibTableColumn
aMACMergePortID = _AMACMergePortID_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 11, 1, 1, 3, 1, 1),
    _AMACMergePortID_Type()
)
aMACMergePortID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aMACMergePortID.setStatus("current")


class _AMACMergeSupport_Type(Integer32):
    """Custom type aMACMergeSupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2))
    )


_AMACMergeSupport_Type.__name__ = "Integer32"
_AMACMergeSupport_Object = MibTableColumn
aMACMergeSupport = _AMACMergeSupport_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 11, 1, 1, 3, 1, 2),
    _AMACMergeSupport_Type()
)
aMACMergeSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aMACMergeSupport.setStatus("current")


class _AMACMergeStatusVerify_Type(Integer32):
    """Custom type aMACMergeStatusVerify based on Integer32"""
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
        *(("unknown", 0),
          ("initial", 1),
          ("verifying", 2),
          ("succeeded", 3),
          ("failed", 4),
          ("disabled", 5))
    )


_AMACMergeStatusVerify_Type.__name__ = "Integer32"
_AMACMergeStatusVerify_Object = MibTableColumn
aMACMergeStatusVerify = _AMACMergeStatusVerify_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 11, 1, 1, 3, 1, 3),
    _AMACMergeStatusVerify_Type()
)
aMACMergeStatusVerify.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aMACMergeStatusVerify.setStatus("current")


class _AMACMergeEnableTx_Type(Integer32):
    """Custom type aMACMergeEnableTx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2))
    )


_AMACMergeEnableTx_Type.__name__ = "Integer32"
_AMACMergeEnableTx_Object = MibTableColumn
aMACMergeEnableTx = _AMACMergeEnableTx_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 11, 1, 1, 3, 1, 4),
    _AMACMergeEnableTx_Type()
)
aMACMergeEnableTx.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aMACMergeEnableTx.setStatus("current")


class _AMACMergeVerifyDisableTx_Type(Integer32):
    """Custom type aMACMergeVerifyDisableTx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2))
    )


_AMACMergeVerifyDisableTx_Type.__name__ = "Integer32"
_AMACMergeVerifyDisableTx_Object = MibTableColumn
aMACMergeVerifyDisableTx = _AMACMergeVerifyDisableTx_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 11, 1, 1, 3, 1, 5),
    _AMACMergeVerifyDisableTx_Type()
)
aMACMergeVerifyDisableTx.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aMACMergeVerifyDisableTx.setStatus("current")


class _AMACMergeStatusTx_Type(Integer32):
    """Custom type aMACMergeStatusTx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("inactive", 1),
          ("active", 2))
    )


_AMACMergeStatusTx_Type.__name__ = "Integer32"
_AMACMergeStatusTx_Object = MibTableColumn
aMACMergeStatusTx = _AMACMergeStatusTx_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 11, 1, 1, 3, 1, 6),
    _AMACMergeStatusTx_Type()
)
aMACMergeStatusTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aMACMergeStatusTx.setStatus("current")


class _AMACMergeVerifyTime_Type(Integer32):
    """Custom type aMACMergeVerifyTime based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_AMACMergeVerifyTime_Type.__name__ = "Integer32"
_AMACMergeVerifyTime_Object = MibTableColumn
aMACMergeVerifyTime = _AMACMergeVerifyTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 11, 1, 1, 3, 1, 7),
    _AMACMergeVerifyTime_Type()
)
aMACMergeVerifyTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aMACMergeVerifyTime.setStatus("current")


class _AMACMergeAddFragSize_Type(Integer32):
    """Custom type aMACMergeAddFragSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_AMACMergeAddFragSize_Type.__name__ = "Integer32"
_AMACMergeAddFragSize_Object = MibTableColumn
aMACMergeAddFragSize = _AMACMergeAddFragSize_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 11, 1, 1, 3, 1, 8),
    _AMACMergeAddFragSize_Type()
)
aMACMergeAddFragSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aMACMergeAddFragSize.setStatus("current")
_AMACMergeFrameAssErrorCount_Type = Counter64
_AMACMergeFrameAssErrorCount_Object = MibTableColumn
aMACMergeFrameAssErrorCount = _AMACMergeFrameAssErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 11, 1, 1, 3, 1, 9),
    _AMACMergeFrameAssErrorCount_Type()
)
aMACMergeFrameAssErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aMACMergeFrameAssErrorCount.setStatus("current")
_AMACMergeFrameSmdErrorCount_Type = Counter64
_AMACMergeFrameSmdErrorCount_Object = MibTableColumn
aMACMergeFrameSmdErrorCount = _AMACMergeFrameSmdErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 11, 1, 1, 3, 1, 10),
    _AMACMergeFrameSmdErrorCount_Type()
)
aMACMergeFrameSmdErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aMACMergeFrameSmdErrorCount.setStatus("current")
_AMACMergeFrameAssOkCount_Type = Counter64
_AMACMergeFrameAssOkCount_Object = MibTableColumn
aMACMergeFrameAssOkCount = _AMACMergeFrameAssOkCount_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 11, 1, 1, 3, 1, 11),
    _AMACMergeFrameAssOkCount_Type()
)
aMACMergeFrameAssOkCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aMACMergeFrameAssOkCount.setStatus("current")
_AMACMergeFragCountRx_Type = Counter64
_AMACMergeFragCountRx_Object = MibTableColumn
aMACMergeFragCountRx = _AMACMergeFragCountRx_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 11, 1, 1, 3, 1, 12),
    _AMACMergeFragCountRx_Type()
)
aMACMergeFragCountRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aMACMergeFragCountRx.setStatus("current")
_AMACMergeFragCountTx_Type = Counter64
_AMACMergeFragCountTx_Object = MibTableColumn
aMACMergeFragCountTx = _AMACMergeFragCountTx_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 11, 1, 1, 3, 1, 13),
    _AMACMergeFragCountTx_Type()
)
aMACMergeFragCountTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aMACMergeFragCountTx.setStatus("current")
_AMACMergeHoldCount_Type = Counter64
_AMACMergeHoldCount_Object = MibTableColumn
aMACMergeHoldCount = _AMACMergeHoldCount_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 11, 1, 1, 3, 1, 14),
    _AMACMergeHoldCount_Type()
)
aMACMergeHoldCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aMACMergeHoldCount.setStatus("current")


class _AMACMergeAcctPolicyId_Type(Unsigned32):
    """Custom type aMACMergeAcctPolicyId based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_AMACMergeAcctPolicyId_Type.__name__ = "Unsigned32"
_AMACMergeAcctPolicyId_Object = MibTableColumn
aMACMergeAcctPolicyId = _AMACMergeAcctPolicyId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 11, 1, 1, 3, 1, 15),
    _AMACMergeAcctPolicyId_Type()
)
aMACMergeAcctPolicyId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aMACMergeAcctPolicyId.setStatus("current")
_TnIEEE8023brObjectsConformance_ObjectIdentity = ObjectIdentity
tnIEEE8023brObjectsConformance = _TnIEEE8023brObjectsConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 11, 2)
)
_Ieee8023brCompliances_ObjectIdentity = ObjectIdentity
ieee8023brCompliances = _Ieee8023brCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 11, 2, 1)
)
_Ieee8023brGroups_ObjectIdentity = ObjectIdentity
ieee8023brGroups = _Ieee8023brGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 11, 2, 2)
)

# Managed Objects groups

ieee8023brGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 11, 2, 2, 1)
)
ieee8023brGroup.setObjects(
      *(("TROPIC-IEEE8023br-MIB", "aLldpXdot3LocPreemptSupported"),
        ("TROPIC-IEEE8023br-MIB", "aLldpXdot3LocPreemptEnabled"),
        ("TROPIC-IEEE8023br-MIB", "aLldpXdot3LocPreemptActive"),
        ("TROPIC-IEEE8023br-MIB", "aLldpXdot3LocAddFragSize"),
        ("TROPIC-IEEE8023br-MIB", "aLldpXdot3RemPreemptSupported"),
        ("TROPIC-IEEE8023br-MIB", "aLldpXdot3RemPreemptEnabled"),
        ("TROPIC-IEEE8023br-MIB", "aLldpXdot3RemPreemptActive"),
        ("TROPIC-IEEE8023br-MIB", "aLldpXdot3RemAddFragSize"),
        ("TROPIC-IEEE8023br-MIB", "aMACMergeSupport"),
        ("TROPIC-IEEE8023br-MIB", "aMACMergeStatusVerify"),
        ("TROPIC-IEEE8023br-MIB", "aMACMergeEnableTx"),
        ("TROPIC-IEEE8023br-MIB", "aMACMergeVerifyDisableTx"),
        ("TROPIC-IEEE8023br-MIB", "aMACMergeStatusTx"),
        ("TROPIC-IEEE8023br-MIB", "aMACMergeVerifyTime"),
        ("TROPIC-IEEE8023br-MIB", "aMACMergeAddFragSize"),
        ("TROPIC-IEEE8023br-MIB", "aMACMergeFrameAssErrorCount"),
        ("TROPIC-IEEE8023br-MIB", "aMACMergeFrameSmdErrorCount"),
        ("TROPIC-IEEE8023br-MIB", "aMACMergeFrameAssOkCount"),
        ("TROPIC-IEEE8023br-MIB", "aMACMergeFragCountRx"),
        ("TROPIC-IEEE8023br-MIB", "aMACMergeFragCountTx"),
        ("TROPIC-IEEE8023br-MIB", "aMACMergeHoldCount"),
        ("TROPIC-IEEE8023br-MIB", "aMACMergeAcctPolicyId"))
)
if mibBuilder.loadTexts:
    ieee8023brGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ieee8023brCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 7483, 2, 2, 4, 11, 2, 1, 1)
)
ieee8023brCompliance.setObjects(
    ("TROPIC-IEEE8023br-MIB", "ieee8023brGroup")
)
if mibBuilder.loadTexts:
    ieee8023brCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TROPIC-IEEE8023br-MIB",
    **{"tnIEEE8023brMibModule": tnIEEE8023brMibModule,
       "tnIEEE8023brEquipmentObjectsNotifications": tnIEEE8023brEquipmentObjectsNotifications,
       "tnIEEE8023brObjects": tnIEEE8023brObjects,
       "tnIEEE8023brObjectsParameters": tnIEEE8023brObjectsParameters,
       "lldpXdot3LocSystemsGroupTable": lldpXdot3LocSystemsGroupTable,
       "lldpXdot3LocSystemsGroupEntry": lldpXdot3LocSystemsGroupEntry,
       "aLldpXdot3LocPortID": aLldpXdot3LocPortID,
       "aLldpXdot3LocPreemptSupported": aLldpXdot3LocPreemptSupported,
       "aLldpXdot3LocPreemptEnabled": aLldpXdot3LocPreemptEnabled,
       "aLldpXdot3LocPreemptActive": aLldpXdot3LocPreemptActive,
       "aLldpXdot3LocAddFragSize": aLldpXdot3LocAddFragSize,
       "lldpXdot3RemSystemsGroupTable": lldpXdot3RemSystemsGroupTable,
       "lldpXdot3RemSystemsGroupEntry": lldpXdot3RemSystemsGroupEntry,
       "aLldpXdot3RemPortID": aLldpXdot3RemPortID,
       "aLldpXdot3RemPreemptSupported": aLldpXdot3RemPreemptSupported,
       "aLldpXdot3RemPreemptEnabled": aLldpXdot3RemPreemptEnabled,
       "aLldpXdot3RemPreemptActive": aLldpXdot3RemPreemptActive,
       "aLldpXdot3RemAddFragSize": aLldpXdot3RemAddFragSize,
       "macMergeEntityTable": macMergeEntityTable,
       "macMergeEntityEntry": macMergeEntityEntry,
       "aMACMergePortID": aMACMergePortID,
       "aMACMergeSupport": aMACMergeSupport,
       "aMACMergeStatusVerify": aMACMergeStatusVerify,
       "aMACMergeEnableTx": aMACMergeEnableTx,
       "aMACMergeVerifyDisableTx": aMACMergeVerifyDisableTx,
       "aMACMergeStatusTx": aMACMergeStatusTx,
       "aMACMergeVerifyTime": aMACMergeVerifyTime,
       "aMACMergeAddFragSize": aMACMergeAddFragSize,
       "aMACMergeFrameAssErrorCount": aMACMergeFrameAssErrorCount,
       "aMACMergeFrameSmdErrorCount": aMACMergeFrameSmdErrorCount,
       "aMACMergeFrameAssOkCount": aMACMergeFrameAssOkCount,
       "aMACMergeFragCountRx": aMACMergeFragCountRx,
       "aMACMergeFragCountTx": aMACMergeFragCountTx,
       "aMACMergeHoldCount": aMACMergeHoldCount,
       "aMACMergeAcctPolicyId": aMACMergeAcctPolicyId,
       "tnIEEE8023brObjectsConformance": tnIEEE8023brObjectsConformance,
       "ieee8023brCompliances": ieee8023brCompliances,
       "ieee8023brCompliance": ieee8023brCompliance,
       "ieee8023brGroups": ieee8023brGroups,
       "ieee8023brGroup": ieee8023brGroup}
)
