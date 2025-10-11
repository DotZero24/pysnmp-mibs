# SNMP MIB module (LUM-COMMLINK-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/LUM-COMMLINK-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:15:16 2025
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

(lumCommlinkMIB,
 lumModules) = mibBuilder.importSymbols(
    "LUM-REG",
    "lumCommlinkMIB",
    "lumModules")

(FaultStatusWithNA,
 MgmtNameString,
 SignalStatusWithNA,
 Unsigned32WithNA) = mibBuilder.importSymbols(
    "LUM-TC",
    "FaultStatusWithNA",
    "MgmtNameString",
    "SignalStatusWithNA",
    "Unsigned32WithNA")

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
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

lumCommlinkMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 1, 1, 72)
)
if mibBuilder.loadTexts:
    lumCommlinkMIBModule.setRevisions(
        ("2018-06-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_LumCommlinkConfs_ObjectIdentity = ObjectIdentity
lumCommlinkConfs = _LumCommlinkConfs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 74, 1)
)
_LumCommlinkGroups_ObjectIdentity = ObjectIdentity
lumCommlinkGroups = _LumCommlinkGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 74, 1, 1)
)
_LumCommlinkCompl_ObjectIdentity = ObjectIdentity
lumCommlinkCompl = _LumCommlinkCompl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 74, 1, 2)
)
_LumCommlinkMIBObjects_ObjectIdentity = ObjectIdentity
lumCommlinkMIBObjects = _LumCommlinkMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 74, 2)
)
_CommlinkGeneral_ObjectIdentity = ObjectIdentity
commlinkGeneral = _CommlinkGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 74, 2, 1)
)
_CommlinkGeneralConfigLastChangeTime_Type = DateAndTime
_CommlinkGeneralConfigLastChangeTime_Object = MibScalar
commlinkGeneralConfigLastChangeTime = _CommlinkGeneralConfigLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 74, 2, 1, 1),
    _CommlinkGeneralConfigLastChangeTime_Type()
)
commlinkGeneralConfigLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    commlinkGeneralConfigLastChangeTime.setStatus("current")
_CommlinkGeneralStateLastChangeTime_Type = DateAndTime
_CommlinkGeneralStateLastChangeTime_Object = MibScalar
commlinkGeneralStateLastChangeTime = _CommlinkGeneralStateLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 74, 2, 1, 2),
    _CommlinkGeneralStateLastChangeTime_Type()
)
commlinkGeneralStateLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    commlinkGeneralStateLastChangeTime.setStatus("current")
_CommlinkGeneralCommlinkAggregatedLinkTableSize_Type = Unsigned32
_CommlinkGeneralCommlinkAggregatedLinkTableSize_Object = MibScalar
commlinkGeneralCommlinkAggregatedLinkTableSize = _CommlinkGeneralCommlinkAggregatedLinkTableSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 74, 2, 1, 3),
    _CommlinkGeneralCommlinkAggregatedLinkTableSize_Type()
)
commlinkGeneralCommlinkAggregatedLinkTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    commlinkGeneralCommlinkAggregatedLinkTableSize.setStatus("current")
_CommlinkGeneralCommlinkAggregatedLinkConfigLastChangeTime_Type = DateAndTime
_CommlinkGeneralCommlinkAggregatedLinkConfigLastChangeTime_Object = MibScalar
commlinkGeneralCommlinkAggregatedLinkConfigLastChangeTime = _CommlinkGeneralCommlinkAggregatedLinkConfigLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 74, 2, 1, 4),
    _CommlinkGeneralCommlinkAggregatedLinkConfigLastChangeTime_Type()
)
commlinkGeneralCommlinkAggregatedLinkConfigLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    commlinkGeneralCommlinkAggregatedLinkConfigLastChangeTime.setStatus("current")
_CommlinkGeneralCommlinkAggregatedLinkStateLastChangeTime_Type = DateAndTime
_CommlinkGeneralCommlinkAggregatedLinkStateLastChangeTime_Object = MibScalar
commlinkGeneralCommlinkAggregatedLinkStateLastChangeTime = _CommlinkGeneralCommlinkAggregatedLinkStateLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 74, 2, 1, 5),
    _CommlinkGeneralCommlinkAggregatedLinkStateLastChangeTime_Type()
)
commlinkGeneralCommlinkAggregatedLinkStateLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    commlinkGeneralCommlinkAggregatedLinkStateLastChangeTime.setStatus("current")
_CommlinkGeneralCommlinkComponentLinkTableSize_Type = Unsigned32
_CommlinkGeneralCommlinkComponentLinkTableSize_Object = MibScalar
commlinkGeneralCommlinkComponentLinkTableSize = _CommlinkGeneralCommlinkComponentLinkTableSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 74, 2, 1, 6),
    _CommlinkGeneralCommlinkComponentLinkTableSize_Type()
)
commlinkGeneralCommlinkComponentLinkTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    commlinkGeneralCommlinkComponentLinkTableSize.setStatus("current")
_CommlinkGeneralCommlinkComponentLinkConfigLastChangeTime_Type = DateAndTime
_CommlinkGeneralCommlinkComponentLinkConfigLastChangeTime_Object = MibScalar
commlinkGeneralCommlinkComponentLinkConfigLastChangeTime = _CommlinkGeneralCommlinkComponentLinkConfigLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 74, 2, 1, 7),
    _CommlinkGeneralCommlinkComponentLinkConfigLastChangeTime_Type()
)
commlinkGeneralCommlinkComponentLinkConfigLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    commlinkGeneralCommlinkComponentLinkConfigLastChangeTime.setStatus("current")
_CommlinkGeneralCommlinkComponentLinkStateLastChangeTime_Type = DateAndTime
_CommlinkGeneralCommlinkComponentLinkStateLastChangeTime_Object = MibScalar
commlinkGeneralCommlinkComponentLinkStateLastChangeTime = _CommlinkGeneralCommlinkComponentLinkStateLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 74, 2, 1, 8),
    _CommlinkGeneralCommlinkComponentLinkStateLastChangeTime_Type()
)
commlinkGeneralCommlinkComponentLinkStateLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    commlinkGeneralCommlinkComponentLinkStateLastChangeTime.setStatus("current")
_CommlinkAggregatedLinkList_ObjectIdentity = ObjectIdentity
commlinkAggregatedLinkList = _CommlinkAggregatedLinkList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 74, 2, 2)
)
_CommlinkAggregatedLinkTable_Object = MibTable
commlinkAggregatedLinkTable = _CommlinkAggregatedLinkTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 74, 2, 2, 1)
)
if mibBuilder.loadTexts:
    commlinkAggregatedLinkTable.setStatus("current")
_CommlinkAggregatedLinkEntry_Object = MibTableRow
commlinkAggregatedLinkEntry = _CommlinkAggregatedLinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 74, 2, 2, 1, 1)
)
commlinkAggregatedLinkEntry.setIndexNames(
    (0, "LUM-COMMLINK-MIB", "commlinkAggregatedLinkIndex"),
)
if mibBuilder.loadTexts:
    commlinkAggregatedLinkEntry.setStatus("current")
_CommlinkAggregatedLinkIndex_Type = Unsigned32
_CommlinkAggregatedLinkIndex_Object = MibTableColumn
commlinkAggregatedLinkIndex = _CommlinkAggregatedLinkIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 74, 2, 2, 1, 1, 1),
    _CommlinkAggregatedLinkIndex_Type()
)
commlinkAggregatedLinkIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    commlinkAggregatedLinkIndex.setStatus("current")
_CommlinkAggregatedLinkUId_Type = Unsigned32
_CommlinkAggregatedLinkUId_Object = MibTableColumn
commlinkAggregatedLinkUId = _CommlinkAggregatedLinkUId_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 74, 2, 2, 1, 1, 2),
    _CommlinkAggregatedLinkUId_Type()
)
commlinkAggregatedLinkUId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    commlinkAggregatedLinkUId.setStatus("current")
_CommlinkAggregatedLinkName_Type = MgmtNameString
_CommlinkAggregatedLinkName_Object = MibTableColumn
commlinkAggregatedLinkName = _CommlinkAggregatedLinkName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 74, 2, 2, 1, 1, 3),
    _CommlinkAggregatedLinkName_Type()
)
commlinkAggregatedLinkName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    commlinkAggregatedLinkName.setStatus("current")


class _CommlinkAggregatedLinkState_Type(Integer32):
    """Custom type commlinkAggregatedLinkState based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("assigned", 1),
          ("unassigned", 2))
    )


_CommlinkAggregatedLinkState_Type.__name__ = "Integer32"
_CommlinkAggregatedLinkState_Object = MibTableColumn
commlinkAggregatedLinkState = _CommlinkAggregatedLinkState_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 74, 2, 2, 1, 1, 4),
    _CommlinkAggregatedLinkState_Type()
)
commlinkAggregatedLinkState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    commlinkAggregatedLinkState.setStatus("current")


class _CommlinkAggregatedLinkStatus_Type(Integer32):
    """Custom type commlinkAggregatedLinkStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_CommlinkAggregatedLinkStatus_Type.__name__ = "Integer32"
_CommlinkAggregatedLinkStatus_Object = MibTableColumn
commlinkAggregatedLinkStatus = _CommlinkAggregatedLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 74, 2, 2, 1, 1, 5),
    _CommlinkAggregatedLinkStatus_Type()
)
commlinkAggregatedLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    commlinkAggregatedLinkStatus.setStatus("current")
_CommlinkAggregatedLinkLocalAutoIP_Type = IpAddress
_CommlinkAggregatedLinkLocalAutoIP_Object = MibTableColumn
commlinkAggregatedLinkLocalAutoIP = _CommlinkAggregatedLinkLocalAutoIP_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 74, 2, 2, 1, 1, 6),
    _CommlinkAggregatedLinkLocalAutoIP_Type()
)
commlinkAggregatedLinkLocalAutoIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    commlinkAggregatedLinkLocalAutoIP.setStatus("current")
_CommlinkAggregatedLinkPeerAutoIP_Type = IpAddress
_CommlinkAggregatedLinkPeerAutoIP_Object = MibTableColumn
commlinkAggregatedLinkPeerAutoIP = _CommlinkAggregatedLinkPeerAutoIP_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 74, 2, 2, 1, 1, 7),
    _CommlinkAggregatedLinkPeerAutoIP_Type()
)
commlinkAggregatedLinkPeerAutoIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    commlinkAggregatedLinkPeerAutoIP.setStatus("current")
_CommlinkAggregatedLinkFailure_Type = FaultStatusWithNA
_CommlinkAggregatedLinkFailure_Object = MibTableColumn
commlinkAggregatedLinkFailure = _CommlinkAggregatedLinkFailure_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 74, 2, 2, 1, 1, 8),
    _CommlinkAggregatedLinkFailure_Type()
)
commlinkAggregatedLinkFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    commlinkAggregatedLinkFailure.setStatus("current")
_CommlinkComponentLinkList_ObjectIdentity = ObjectIdentity
commlinkComponentLinkList = _CommlinkComponentLinkList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 74, 2, 3)
)
_CommlinkComponentLinkTable_Object = MibTable
commlinkComponentLinkTable = _CommlinkComponentLinkTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 74, 2, 3, 1)
)
if mibBuilder.loadTexts:
    commlinkComponentLinkTable.setStatus("current")
_CommlinkComponentLinkEntry_Object = MibTableRow
commlinkComponentLinkEntry = _CommlinkComponentLinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 74, 2, 3, 1, 1)
)
commlinkComponentLinkEntry.setIndexNames(
    (0, "LUM-COMMLINK-MIB", "commlinkComponentLinkIndex"),
)
if mibBuilder.loadTexts:
    commlinkComponentLinkEntry.setStatus("current")
_CommlinkComponentLinkIndex_Type = Unsigned32
_CommlinkComponentLinkIndex_Object = MibTableColumn
commlinkComponentLinkIndex = _CommlinkComponentLinkIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 74, 2, 3, 1, 1, 1),
    _CommlinkComponentLinkIndex_Type()
)
commlinkComponentLinkIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    commlinkComponentLinkIndex.setStatus("current")
_CommlinkComponentLinkUId_Type = Unsigned32
_CommlinkComponentLinkUId_Object = MibTableColumn
commlinkComponentLinkUId = _CommlinkComponentLinkUId_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 74, 2, 3, 1, 1, 2),
    _CommlinkComponentLinkUId_Type()
)
commlinkComponentLinkUId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    commlinkComponentLinkUId.setStatus("current")
_CommlinkComponentLinkName_Type = MgmtNameString
_CommlinkComponentLinkName_Object = MibTableColumn
commlinkComponentLinkName = _CommlinkComponentLinkName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 74, 2, 3, 1, 1, 3),
    _CommlinkComponentLinkName_Type()
)
commlinkComponentLinkName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    commlinkComponentLinkName.setStatus("current")


class _CommlinkComponentLinkGccSelection_Type(Integer32):
    """Custom type commlinkComponentLinkGccSelection based on Integer32"""
    defaultValue = 2147483647

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              2147483647)
        )
    )
    namedValues = NamedValues(
        *(("gcc1", 1),
          ("gcc2", 2),
          ("undefined", 2147483647))
    )


_CommlinkComponentLinkGccSelection_Type.__name__ = "Integer32"
_CommlinkComponentLinkGccSelection_Object = MibTableColumn
commlinkComponentLinkGccSelection = _CommlinkComponentLinkGccSelection_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 74, 2, 3, 1, 1, 4),
    _CommlinkComponentLinkGccSelection_Type()
)
commlinkComponentLinkGccSelection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    commlinkComponentLinkGccSelection.setStatus("current")


class _CommlinkComponentLinkStatus_Type(Integer32):
    """Custom type commlinkComponentLinkStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_CommlinkComponentLinkStatus_Type.__name__ = "Integer32"
_CommlinkComponentLinkStatus_Object = MibTableColumn
commlinkComponentLinkStatus = _CommlinkComponentLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 74, 2, 3, 1, 1, 5),
    _CommlinkComponentLinkStatus_Type()
)
commlinkComponentLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    commlinkComponentLinkStatus.setStatus("current")


class _CommlinkComponentLinkAdminStatus_Type(Integer32):
    """Custom type commlinkComponentLinkAdminStatus based on Integer32"""
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
        *(("up", 1),
          ("service", 2),
          ("down", 3))
    )


_CommlinkComponentLinkAdminStatus_Type.__name__ = "Integer32"
_CommlinkComponentLinkAdminStatus_Object = MibTableColumn
commlinkComponentLinkAdminStatus = _CommlinkComponentLinkAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 74, 2, 3, 1, 1, 6),
    _CommlinkComponentLinkAdminStatus_Type()
)
commlinkComponentLinkAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    commlinkComponentLinkAdminStatus.setStatus("current")
_CommlinkComponentLinkAggrLinkId_Type = MgmtNameString
_CommlinkComponentLinkAggrLinkId_Object = MibTableColumn
commlinkComponentLinkAggrLinkId = _CommlinkComponentLinkAggrLinkId_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 74, 2, 3, 1, 1, 7),
    _CommlinkComponentLinkAggrLinkId_Type()
)
commlinkComponentLinkAggrLinkId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    commlinkComponentLinkAggrLinkId.setStatus("current")
_CommlinkComponentLinkHostId_Type = MgmtNameString
_CommlinkComponentLinkHostId_Object = MibTableColumn
commlinkComponentLinkHostId = _CommlinkComponentLinkHostId_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 74, 2, 3, 1, 1, 8),
    _CommlinkComponentLinkHostId_Type()
)
commlinkComponentLinkHostId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    commlinkComponentLinkHostId.setStatus("current")
_CommlinkComponentLinkExpectedHostId_Type = MgmtNameString
_CommlinkComponentLinkExpectedHostId_Object = MibTableColumn
commlinkComponentLinkExpectedHostId = _CommlinkComponentLinkExpectedHostId_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 74, 2, 3, 1, 1, 9),
    _CommlinkComponentLinkExpectedHostId_Type()
)
commlinkComponentLinkExpectedHostId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    commlinkComponentLinkExpectedHostId.setStatus("current")
_CommlinkComponentLinkDiscoveredHostId_Type = MgmtNameString
_CommlinkComponentLinkDiscoveredHostId_Object = MibTableColumn
commlinkComponentLinkDiscoveredHostId = _CommlinkComponentLinkDiscoveredHostId_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 74, 2, 3, 1, 1, 10),
    _CommlinkComponentLinkDiscoveredHostId_Type()
)
commlinkComponentLinkDiscoveredHostId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    commlinkComponentLinkDiscoveredHostId.setStatus("current")
_CommlinkComponentLinkHostLinkId_Type = MgmtNameString
_CommlinkComponentLinkHostLinkId_Object = MibTableColumn
commlinkComponentLinkHostLinkId = _CommlinkComponentLinkHostLinkId_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 74, 2, 3, 1, 1, 11),
    _CommlinkComponentLinkHostLinkId_Type()
)
commlinkComponentLinkHostLinkId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    commlinkComponentLinkHostLinkId.setStatus("current")
_CommlinkComponentLinkExpectedPeerLinkId_Type = MgmtNameString
_CommlinkComponentLinkExpectedPeerLinkId_Object = MibTableColumn
commlinkComponentLinkExpectedPeerLinkId = _CommlinkComponentLinkExpectedPeerLinkId_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 74, 2, 3, 1, 1, 13),
    _CommlinkComponentLinkExpectedPeerLinkId_Type()
)
commlinkComponentLinkExpectedPeerLinkId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    commlinkComponentLinkExpectedPeerLinkId.setStatus("current")
_CommlinkComponentLinkDiscoveredPeerLinkId_Type = MgmtNameString
_CommlinkComponentLinkDiscoveredPeerLinkId_Object = MibTableColumn
commlinkComponentLinkDiscoveredPeerLinkId = _CommlinkComponentLinkDiscoveredPeerLinkId_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 74, 2, 3, 1, 1, 14),
    _CommlinkComponentLinkDiscoveredPeerLinkId_Type()
)
commlinkComponentLinkDiscoveredPeerLinkId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    commlinkComponentLinkDiscoveredPeerLinkId.setStatus("current")
_CommlinkComponentLinkPeerNotResponding_Type = FaultStatusWithNA
_CommlinkComponentLinkPeerNotResponding_Object = MibTableColumn
commlinkComponentLinkPeerNotResponding = _CommlinkComponentLinkPeerNotResponding_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 74, 2, 3, 1, 1, 15),
    _CommlinkComponentLinkPeerNotResponding_Type()
)
commlinkComponentLinkPeerNotResponding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    commlinkComponentLinkPeerNotResponding.setStatus("current")
_CommlinkComponentLinkPeerHostIdMismatch_Type = FaultStatusWithNA
_CommlinkComponentLinkPeerHostIdMismatch_Object = MibTableColumn
commlinkComponentLinkPeerHostIdMismatch = _CommlinkComponentLinkPeerHostIdMismatch_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 74, 2, 3, 1, 1, 16),
    _CommlinkComponentLinkPeerHostIdMismatch_Type()
)
commlinkComponentLinkPeerHostIdMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    commlinkComponentLinkPeerHostIdMismatch.setStatus("current")
_CommlinkComponentLinkPeerLinkIdMismatch_Type = FaultStatusWithNA
_CommlinkComponentLinkPeerLinkIdMismatch_Object = MibTableColumn
commlinkComponentLinkPeerLinkIdMismatch = _CommlinkComponentLinkPeerLinkIdMismatch_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 74, 2, 3, 1, 1, 17),
    _CommlinkComponentLinkPeerLinkIdMismatch_Type()
)
commlinkComponentLinkPeerLinkIdMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    commlinkComponentLinkPeerLinkIdMismatch.setStatus("current")

# Managed Objects groups

commlinkGeneralGroupV1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 74, 1, 1, 1)
)
commlinkGeneralGroupV1.setObjects(
      *(("LUM-COMMLINK-MIB", "commlinkGeneralConfigLastChangeTime"),
        ("LUM-COMMLINK-MIB", "commlinkGeneralStateLastChangeTime"),
        ("LUM-COMMLINK-MIB", "commlinkGeneralCommlinkAggregatedLinkTableSize"),
        ("LUM-COMMLINK-MIB", "commlinkGeneralCommlinkAggregatedLinkConfigLastChangeTime"),
        ("LUM-COMMLINK-MIB", "commlinkGeneralCommlinkAggregatedLinkStateLastChangeTime"),
        ("LUM-COMMLINK-MIB", "commlinkGeneralCommlinkComponentLinkTableSize"),
        ("LUM-COMMLINK-MIB", "commlinkGeneralCommlinkComponentLinkConfigLastChangeTime"),
        ("LUM-COMMLINK-MIB", "commlinkGeneralCommlinkComponentLinkStateLastChangeTime"))
)
if mibBuilder.loadTexts:
    commlinkGeneralGroupV1.setStatus("current")

commlinkAggregatedLinkGroupV1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 74, 1, 1, 2)
)
commlinkAggregatedLinkGroupV1.setObjects(
      *(("LUM-COMMLINK-MIB", "commlinkAggregatedLinkIndex"),
        ("LUM-COMMLINK-MIB", "commlinkAggregatedLinkUId"),
        ("LUM-COMMLINK-MIB", "commlinkAggregatedLinkName"),
        ("LUM-COMMLINK-MIB", "commlinkAggregatedLinkState"),
        ("LUM-COMMLINK-MIB", "commlinkAggregatedLinkStatus"),
        ("LUM-COMMLINK-MIB", "commlinkAggregatedLinkLocalAutoIP"),
        ("LUM-COMMLINK-MIB", "commlinkAggregatedLinkPeerAutoIP"),
        ("LUM-COMMLINK-MIB", "commlinkAggregatedLinkFailure"))
)
if mibBuilder.loadTexts:
    commlinkAggregatedLinkGroupV1.setStatus("current")

commlinkComponentLinkGroupV1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 74, 1, 1, 3)
)
commlinkComponentLinkGroupV1.setObjects(
      *(("LUM-COMMLINK-MIB", "commlinkComponentLinkIndex"),
        ("LUM-COMMLINK-MIB", "commlinkComponentLinkUId"),
        ("LUM-COMMLINK-MIB", "commlinkComponentLinkName"),
        ("LUM-COMMLINK-MIB", "commlinkComponentLinkGccSelection"),
        ("LUM-COMMLINK-MIB", "commlinkComponentLinkStatus"),
        ("LUM-COMMLINK-MIB", "commlinkComponentLinkAdminStatus"),
        ("LUM-COMMLINK-MIB", "commlinkComponentLinkHostId"),
        ("LUM-COMMLINK-MIB", "commlinkComponentLinkExpectedHostId"),
        ("LUM-COMMLINK-MIB", "commlinkComponentLinkDiscoveredHostId"),
        ("LUM-COMMLINK-MIB", "commlinkComponentLinkAggrLinkId"),
        ("LUM-COMMLINK-MIB", "commlinkComponentLinkHostLinkId"),
        ("LUM-COMMLINK-MIB", "commlinkComponentLinkExpectedPeerLinkId"),
        ("LUM-COMMLINK-MIB", "commlinkComponentLinkDiscoveredPeerLinkId"),
        ("LUM-COMMLINK-MIB", "commlinkComponentLinkPeerNotResponding"),
        ("LUM-COMMLINK-MIB", "commlinkComponentLinkPeerHostIdMismatch"),
        ("LUM-COMMLINK-MIB", "commlinkComponentLinkPeerLinkIdMismatch"))
)
if mibBuilder.loadTexts:
    commlinkComponentLinkGroupV1.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

lumCommlinkComplV1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 74, 1, 2, 1)
)
lumCommlinkComplV1.setObjects(
      *(("LUM-COMMLINK-MIB", "commlinkGeneralGroupV1"),
        ("LUM-COMMLINK-MIB", "commlinkAggregatedLinkGroupV1"),
        ("LUM-COMMLINK-MIB", "commlinkComponentLinkGroupV1"))
)
if mibBuilder.loadTexts:
    lumCommlinkComplV1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LUM-COMMLINK-MIB",
    **{"lumCommlinkMIBModule": lumCommlinkMIBModule,
       "lumCommlinkConfs": lumCommlinkConfs,
       "lumCommlinkGroups": lumCommlinkGroups,
       "commlinkGeneralGroupV1": commlinkGeneralGroupV1,
       "commlinkAggregatedLinkGroupV1": commlinkAggregatedLinkGroupV1,
       "commlinkComponentLinkGroupV1": commlinkComponentLinkGroupV1,
       "lumCommlinkCompl": lumCommlinkCompl,
       "lumCommlinkComplV1": lumCommlinkComplV1,
       "lumCommlinkMIBObjects": lumCommlinkMIBObjects,
       "commlinkGeneral": commlinkGeneral,
       "commlinkGeneralConfigLastChangeTime": commlinkGeneralConfigLastChangeTime,
       "commlinkGeneralStateLastChangeTime": commlinkGeneralStateLastChangeTime,
       "commlinkGeneralCommlinkAggregatedLinkTableSize": commlinkGeneralCommlinkAggregatedLinkTableSize,
       "commlinkGeneralCommlinkAggregatedLinkConfigLastChangeTime": commlinkGeneralCommlinkAggregatedLinkConfigLastChangeTime,
       "commlinkGeneralCommlinkAggregatedLinkStateLastChangeTime": commlinkGeneralCommlinkAggregatedLinkStateLastChangeTime,
       "commlinkGeneralCommlinkComponentLinkTableSize": commlinkGeneralCommlinkComponentLinkTableSize,
       "commlinkGeneralCommlinkComponentLinkConfigLastChangeTime": commlinkGeneralCommlinkComponentLinkConfigLastChangeTime,
       "commlinkGeneralCommlinkComponentLinkStateLastChangeTime": commlinkGeneralCommlinkComponentLinkStateLastChangeTime,
       "commlinkAggregatedLinkList": commlinkAggregatedLinkList,
       "commlinkAggregatedLinkTable": commlinkAggregatedLinkTable,
       "commlinkAggregatedLinkEntry": commlinkAggregatedLinkEntry,
       "commlinkAggregatedLinkIndex": commlinkAggregatedLinkIndex,
       "commlinkAggregatedLinkUId": commlinkAggregatedLinkUId,
       "commlinkAggregatedLinkName": commlinkAggregatedLinkName,
       "commlinkAggregatedLinkState": commlinkAggregatedLinkState,
       "commlinkAggregatedLinkStatus": commlinkAggregatedLinkStatus,
       "commlinkAggregatedLinkLocalAutoIP": commlinkAggregatedLinkLocalAutoIP,
       "commlinkAggregatedLinkPeerAutoIP": commlinkAggregatedLinkPeerAutoIP,
       "commlinkAggregatedLinkFailure": commlinkAggregatedLinkFailure,
       "commlinkComponentLinkList": commlinkComponentLinkList,
       "commlinkComponentLinkTable": commlinkComponentLinkTable,
       "commlinkComponentLinkEntry": commlinkComponentLinkEntry,
       "commlinkComponentLinkIndex": commlinkComponentLinkIndex,
       "commlinkComponentLinkUId": commlinkComponentLinkUId,
       "commlinkComponentLinkName": commlinkComponentLinkName,
       "commlinkComponentLinkGccSelection": commlinkComponentLinkGccSelection,
       "commlinkComponentLinkStatus": commlinkComponentLinkStatus,
       "commlinkComponentLinkAdminStatus": commlinkComponentLinkAdminStatus,
       "commlinkComponentLinkAggrLinkId": commlinkComponentLinkAggrLinkId,
       "commlinkComponentLinkHostId": commlinkComponentLinkHostId,
       "commlinkComponentLinkExpectedHostId": commlinkComponentLinkExpectedHostId,
       "commlinkComponentLinkDiscoveredHostId": commlinkComponentLinkDiscoveredHostId,
       "commlinkComponentLinkHostLinkId": commlinkComponentLinkHostLinkId,
       "commlinkComponentLinkExpectedPeerLinkId": commlinkComponentLinkExpectedPeerLinkId,
       "commlinkComponentLinkDiscoveredPeerLinkId": commlinkComponentLinkDiscoveredPeerLinkId,
       "commlinkComponentLinkPeerNotResponding": commlinkComponentLinkPeerNotResponding,
       "commlinkComponentLinkPeerHostIdMismatch": commlinkComponentLinkPeerHostIdMismatch,
       "commlinkComponentLinkPeerLinkIdMismatch": commlinkComponentLinkPeerLinkIdMismatch}
)
