# SNMP MIB module (ADTRAN-GENBONDING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/adtran/ADTRAN-GENBONDING-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:31:36 2025
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

(adGenBondingID,) = mibBuilder.importSymbols(
    "ADTRAN-GENMINIDSLAM-MIB",
    "adGenBondingID")

(adGenSlotInfoIndex,) = mibBuilder.importSymbols(
    "ADTRAN-GENSLOT-MIB",
    "adGenSlotInfoIndex")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

adGenBonding = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 61, 4, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class AdGenBondingPort(TextualConvention, Integer32):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_AdGenBondingMib_ObjectIdentity = ObjectIdentity
adGenBondingMib = _AdGenBondingMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 61, 4, 1, 1)
)
_AdGenBondingMibObjects_ObjectIdentity = ObjectIdentity
adGenBondingMibObjects = _AdGenBondingMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 61, 4, 1, 1, 1)
)
_AdGenBondingSlotInfoTable_Object = MibTable
adGenBondingSlotInfoTable = _AdGenBondingSlotInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 61, 4, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    adGenBondingSlotInfoTable.setStatus("current")
_AdGenBondingSlotInfoEntry_Object = MibTableRow
adGenBondingSlotInfoEntry = _AdGenBondingSlotInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 61, 4, 1, 1, 1, 1, 1)
)
adGenBondingSlotInfoEntry.setIndexNames(
    (0, "ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
)
if mibBuilder.loadTexts:
    adGenBondingSlotInfoEntry.setStatus("current")
_AdGenBondingGroupNumberNext_Type = Integer32
_AdGenBondingGroupNumberNext_Object = MibTableColumn
adGenBondingGroupNumberNext = _AdGenBondingGroupNumberNext_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 61, 4, 1, 1, 1, 1, 1, 1),
    _AdGenBondingGroupNumberNext_Type()
)
adGenBondingGroupNumberNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenBondingGroupNumberNext.setStatus("current")
_AdGenGenBondingSlotStatus_Type = DisplayString
_AdGenGenBondingSlotStatus_Object = MibTableColumn
adGenGenBondingSlotStatus = _AdGenGenBondingSlotStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 61, 4, 1, 1, 1, 1, 1, 2),
    _AdGenGenBondingSlotStatus_Type()
)
adGenGenBondingSlotStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenGenBondingSlotStatus.setStatus("current")
_AdGenBondingGroupTable_Object = MibTable
adGenBondingGroupTable = _AdGenBondingGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 61, 4, 1, 1, 1, 2)
)
if mibBuilder.loadTexts:
    adGenBondingGroupTable.setStatus("current")
_AdGenBondingGroupEntry_Object = MibTableRow
adGenBondingGroupEntry = _AdGenBondingGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 61, 4, 1, 1, 1, 2, 1)
)
adGenBondingGroupEntry.setIndexNames(
    (0, "ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
    (0, "ADTRAN-GENBONDING-MIB", "adGenBondingGroupIndex"),
)
if mibBuilder.loadTexts:
    adGenBondingGroupEntry.setStatus("current")
_AdGenBondingGroupIndex_Type = Integer32
_AdGenBondingGroupIndex_Object = MibTableColumn
adGenBondingGroupIndex = _AdGenBondingGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 61, 4, 1, 1, 1, 2, 1, 1),
    _AdGenBondingGroupIndex_Type()
)
adGenBondingGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adGenBondingGroupIndex.setStatus("current")
_AdGenBondingGroupRowStatus_Type = RowStatus
_AdGenBondingGroupRowStatus_Object = MibTableColumn
adGenBondingGroupRowStatus = _AdGenBondingGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 61, 4, 1, 1, 1, 2, 1, 2),
    _AdGenBondingGroupRowStatus_Type()
)
adGenBondingGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenBondingGroupRowStatus.setStatus("current")
_AdGenBondingGroupName_Type = DisplayString
_AdGenBondingGroupName_Object = MibTableColumn
adGenBondingGroupName = _AdGenBondingGroupName_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 61, 4, 1, 1, 1, 2, 1, 3),
    _AdGenBondingGroupName_Type()
)
adGenBondingGroupName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenBondingGroupName.setStatus("current")
_AdGenBondingGroupPortsString_Type = DisplayString
_AdGenBondingGroupPortsString_Object = MibTableColumn
adGenBondingGroupPortsString = _AdGenBondingGroupPortsString_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 61, 4, 1, 1, 1, 2, 1, 4),
    _AdGenBondingGroupPortsString_Type()
)
adGenBondingGroupPortsString.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenBondingGroupPortsString.setStatus("current")
_AdGenBondingGroupNumPorts_Type = Integer32
_AdGenBondingGroupNumPorts_Object = MibTableColumn
adGenBondingGroupNumPorts = _AdGenBondingGroupNumPorts_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 61, 4, 1, 1, 1, 2, 1, 5),
    _AdGenBondingGroupNumPorts_Type()
)
adGenBondingGroupNumPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenBondingGroupNumPorts.setStatus("current")
_AdGenBondingPortsTable_Object = MibTable
adGenBondingPortsTable = _AdGenBondingPortsTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 61, 4, 1, 1, 1, 3)
)
if mibBuilder.loadTexts:
    adGenBondingPortsTable.setStatus("current")
_AdGenBondingPortsEntry_Object = MibTableRow
adGenBondingPortsEntry = _AdGenBondingPortsEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 61, 4, 1, 1, 1, 3, 1)
)
adGenBondingPortsEntry.setIndexNames(
    (0, "ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
    (0, "ADTRAN-GENBONDING-MIB", "adGenBondingPortsIndex"),
)
if mibBuilder.loadTexts:
    adGenBondingPortsEntry.setStatus("current")
_AdGenBondingPortsIndex_Type = AdGenBondingPort
_AdGenBondingPortsIndex_Object = MibTableColumn
adGenBondingPortsIndex = _AdGenBondingPortsIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 61, 4, 1, 1, 1, 3, 1, 1),
    _AdGenBondingPortsIndex_Type()
)
adGenBondingPortsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adGenBondingPortsIndex.setStatus("current")
_AdGenBondingPortsGroupMembership_Type = Integer32
_AdGenBondingPortsGroupMembership_Object = MibTableColumn
adGenBondingPortsGroupMembership = _AdGenBondingPortsGroupMembership_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 61, 4, 1, 1, 1, 3, 1, 2),
    _AdGenBondingPortsGroupMembership_Type()
)
adGenBondingPortsGroupMembership.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenBondingPortsGroupMembership.setStatus("current")
_AdGenBondingPortStatusTable_Object = MibTable
adGenBondingPortStatusTable = _AdGenBondingPortStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 61, 4, 1, 1, 1, 4)
)
if mibBuilder.loadTexts:
    adGenBondingPortStatusTable.setStatus("current")
_AdGenBondingPortStatusEntry_Object = MibTableRow
adGenBondingPortStatusEntry = _AdGenBondingPortStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 61, 4, 1, 1, 1, 4, 1)
)
adGenBondingPortStatusEntry.setIndexNames(
    (0, "ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
    (0, "ADTRAN-GENBONDING-MIB", "adGenBondingGroupIndex"),
    (0, "ADTRAN-GENBONDING-MIB", "adGenBondingPortStatusPortIndex"),
)
if mibBuilder.loadTexts:
    adGenBondingPortStatusEntry.setStatus("current")
_AdGenBondingPortStatusPortIndex_Type = AdGenBondingPort
_AdGenBondingPortStatusPortIndex_Object = MibTableColumn
adGenBondingPortStatusPortIndex = _AdGenBondingPortStatusPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 61, 4, 1, 1, 1, 4, 1, 1),
    _AdGenBondingPortStatusPortIndex_Type()
)
adGenBondingPortStatusPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adGenBondingPortStatusPortIndex.setStatus("current")


class _AdGenBondingPortGroupState_Type(Integer32):
    """Custom type adGenBondingPortGroupState based on Integer32"""
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
        *(("notProvisioned", 1),
          ("notUsable", 2),
          ("readyForTraffic", 3),
          ("carryingTraffic", 4))
    )


_AdGenBondingPortGroupState_Type.__name__ = "Integer32"
_AdGenBondingPortGroupState_Object = MibTableColumn
adGenBondingPortGroupState = _AdGenBondingPortGroupState_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 61, 4, 1, 1, 1, 4, 1, 2),
    _AdGenBondingPortGroupState_Type()
)
adGenBondingPortGroupState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenBondingPortGroupState.setStatus("current")
_AdGenBondingPortDiffDelay_Type = Integer32
_AdGenBondingPortDiffDelay_Object = MibTableColumn
adGenBondingPortDiffDelay = _AdGenBondingPortDiffDelay_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 61, 4, 1, 1, 1, 4, 1, 3),
    _AdGenBondingPortDiffDelay_Type()
)
adGenBondingPortDiffDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenBondingPortDiffDelay.setStatus("current")
if mibBuilder.loadTexts:
    adGenBondingPortDiffDelay.setUnits("100 microseconds")
_AdGenBondingPortTxId_Type = Integer32
_AdGenBondingPortTxId_Object = MibTableColumn
adGenBondingPortTxId = _AdGenBondingPortTxId_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 61, 4, 1, 1, 1, 4, 1, 4),
    _AdGenBondingPortTxId_Type()
)
adGenBondingPortTxId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenBondingPortTxId.setStatus("current")
_AdGenBondingPortRxId_Type = Integer32
_AdGenBondingPortRxId_Object = MibTableColumn
adGenBondingPortRxId = _AdGenBondingPortRxId_Object(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 61, 4, 1, 1, 1, 4, 1, 5),
    _AdGenBondingPortRxId_Type()
)
adGenBondingPortRxId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenBondingPortRxId.setStatus("current")
_AdGenBondingMibConformance_ObjectIdentity = ObjectIdentity
adGenBondingMibConformance = _AdGenBondingMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 61, 4, 1, 1, 2)
)
_AdGenBondingMibGroups_ObjectIdentity = ObjectIdentity
adGenBondingMibGroups = _AdGenBondingMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 61, 4, 1, 1, 2, 1)
)
_AdGenBondingMibCompliances_ObjectIdentity = ObjectIdentity
adGenBondingMibCompliances = _AdGenBondingMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 61, 4, 1, 1, 2, 2)
)

# Managed Objects groups

adGenBondingGroupGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 61, 4, 1, 1, 2, 1, 1)
)
adGenBondingGroupGroup.setObjects(
      *(("ADTRAN-GENBONDING-MIB", "adGenBondingGroupNumberNext"),
        ("ADTRAN-GENBONDING-MIB", "adGenBondingGroupRowStatus"),
        ("ADTRAN-GENBONDING-MIB", "adGenBondingGroupPortsString"),
        ("ADTRAN-GENBONDING-MIB", "adGenBondingGroupNumPorts"))
)
if mibBuilder.loadTexts:
    adGenBondingGroupGroup.setStatus("current")

adGenBondingPortsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 61, 4, 1, 1, 2, 1, 2)
)
adGenBondingPortsGroup.setObjects(
    ("ADTRAN-GENBONDING-MIB", "adGenBondingPortsGroupMembership")
)
if mibBuilder.loadTexts:
    adGenBondingPortsGroup.setStatus("current")

adGenBondingPortStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 61, 4, 1, 1, 2, 1, 3)
)
adGenBondingPortStatusGroup.setObjects(
      *(("ADTRAN-GENBONDING-MIB", "adGenBondingPortGroupState"),
        ("ADTRAN-GENBONDING-MIB", "adGenBondingPortDiffDelay"),
        ("ADTRAN-GENBONDING-MIB", "adGenBondingPortTxId"),
        ("ADTRAN-GENBONDING-MIB", "adGenBondingPortRxId"))
)
if mibBuilder.loadTexts:
    adGenBondingPortStatusGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

adGenBondingMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 61, 4, 1, 1, 2, 2, 1)
)
adGenBondingMibCompliance.setObjects(
      *(("ADTRAN-GENBONDING-MIB", "adGenBondingGroupGroup"),
        ("ADTRAN-GENBONDING-MIB", "adGenBondingPortsGroup"),
        ("ADTRAN-GENBONDING-MIB", "adGenBondingPortStatusGroup"))
)
if mibBuilder.loadTexts:
    adGenBondingMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ADTRAN-GENBONDING-MIB",
    **{"AdGenBondingPort": AdGenBondingPort,
       "adGenBonding": adGenBonding,
       "adGenBondingMib": adGenBondingMib,
       "adGenBondingMibObjects": adGenBondingMibObjects,
       "adGenBondingSlotInfoTable": adGenBondingSlotInfoTable,
       "adGenBondingSlotInfoEntry": adGenBondingSlotInfoEntry,
       "adGenBondingGroupNumberNext": adGenBondingGroupNumberNext,
       "adGenGenBondingSlotStatus": adGenGenBondingSlotStatus,
       "adGenBondingGroupTable": adGenBondingGroupTable,
       "adGenBondingGroupEntry": adGenBondingGroupEntry,
       "adGenBondingGroupIndex": adGenBondingGroupIndex,
       "adGenBondingGroupRowStatus": adGenBondingGroupRowStatus,
       "adGenBondingGroupName": adGenBondingGroupName,
       "adGenBondingGroupPortsString": adGenBondingGroupPortsString,
       "adGenBondingGroupNumPorts": adGenBondingGroupNumPorts,
       "adGenBondingPortsTable": adGenBondingPortsTable,
       "adGenBondingPortsEntry": adGenBondingPortsEntry,
       "adGenBondingPortsIndex": adGenBondingPortsIndex,
       "adGenBondingPortsGroupMembership": adGenBondingPortsGroupMembership,
       "adGenBondingPortStatusTable": adGenBondingPortStatusTable,
       "adGenBondingPortStatusEntry": adGenBondingPortStatusEntry,
       "adGenBondingPortStatusPortIndex": adGenBondingPortStatusPortIndex,
       "adGenBondingPortGroupState": adGenBondingPortGroupState,
       "adGenBondingPortDiffDelay": adGenBondingPortDiffDelay,
       "adGenBondingPortTxId": adGenBondingPortTxId,
       "adGenBondingPortRxId": adGenBondingPortRxId,
       "adGenBondingMibConformance": adGenBondingMibConformance,
       "adGenBondingMibGroups": adGenBondingMibGroups,
       "adGenBondingGroupGroup": adGenBondingGroupGroup,
       "adGenBondingPortsGroup": adGenBondingPortsGroup,
       "adGenBondingPortStatusGroup": adGenBondingPortStatusGroup,
       "adGenBondingMibCompliances": adGenBondingMibCompliances,
       "adGenBondingMibCompliance": adGenBondingMibCompliance}
)
