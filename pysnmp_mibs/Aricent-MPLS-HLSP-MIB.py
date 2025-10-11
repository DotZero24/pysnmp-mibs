# SNMP MIB module (Aricent-MPLS-HLSP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/aricent/Aricent-MPLS-HLSP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:44:34 2025
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

(MplsExtendedTunnelId,
 MplsTunnelIndex,
 MplsTunnelInstanceIndex) = mibBuilder.importSymbols(
    "MPLS-TC-STD-MIB",
    "MplsExtendedTunnelId",
    "MplsTunnelIndex",
    "MplsTunnelInstanceIndex")

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
 PhysAddress,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

fsHlspMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 29601, 2, 58)
)
if mibBuilder.loadTexts:
    fsHlspMIB.setRevisions(
        ("2012-09-05 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FsMplsHlspConfigObjects_ObjectIdentity = ObjectIdentity
fsMplsHlspConfigObjects = _FsMplsHlspConfigObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29601, 2, 58, 1)
)
_FsMplsLSPMapTunnelTable_Object = MibTable
fsMplsLSPMapTunnelTable = _FsMplsLSPMapTunnelTable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 58, 1, 1)
)
if mibBuilder.loadTexts:
    fsMplsLSPMapTunnelTable.setStatus("current")
_FsMplsLSPMapTunnelEntry_Object = MibTableRow
fsMplsLSPMapTunnelEntry = _FsMplsLSPMapTunnelEntry_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 58, 1, 1, 1)
)
fsMplsLSPMapTunnelEntry.setIndexNames(
    (0, "Aricent-MPLS-HLSP-MIB", "fsMplsLSPMapTunnelIndex"),
    (0, "Aricent-MPLS-HLSP-MIB", "fsMplsLSPMapTunnelInstance"),
    (0, "Aricent-MPLS-HLSP-MIB", "fsMplsLSPMapTunnelIngressLSRId"),
    (0, "Aricent-MPLS-HLSP-MIB", "fsMplsLSPMapTunnelEgressLSRId"),
    (0, "Aricent-MPLS-HLSP-MIB", "fsMplsLSPMapSubTunnelIndex"),
    (0, "Aricent-MPLS-HLSP-MIB", "fsMplsLSPMapSubTunnelInstance"),
    (0, "Aricent-MPLS-HLSP-MIB", "fsMplsLSPMapSubTunnelIngressLSRId"),
    (0, "Aricent-MPLS-HLSP-MIB", "fsMplsLSPMapSubTunnelEgressLSRId"),
)
if mibBuilder.loadTexts:
    fsMplsLSPMapTunnelEntry.setStatus("current")
_FsMplsLSPMapTunnelIndex_Type = MplsTunnelIndex
_FsMplsLSPMapTunnelIndex_Object = MibTableColumn
fsMplsLSPMapTunnelIndex = _FsMplsLSPMapTunnelIndex_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 58, 1, 1, 1, 1),
    _FsMplsLSPMapTunnelIndex_Type()
)
fsMplsLSPMapTunnelIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMplsLSPMapTunnelIndex.setStatus("current")
_FsMplsLSPMapTunnelInstance_Type = MplsTunnelInstanceIndex
_FsMplsLSPMapTunnelInstance_Object = MibTableColumn
fsMplsLSPMapTunnelInstance = _FsMplsLSPMapTunnelInstance_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 58, 1, 1, 1, 2),
    _FsMplsLSPMapTunnelInstance_Type()
)
fsMplsLSPMapTunnelInstance.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMplsLSPMapTunnelInstance.setStatus("current")
_FsMplsLSPMapTunnelIngressLSRId_Type = MplsExtendedTunnelId
_FsMplsLSPMapTunnelIngressLSRId_Object = MibTableColumn
fsMplsLSPMapTunnelIngressLSRId = _FsMplsLSPMapTunnelIngressLSRId_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 58, 1, 1, 1, 3),
    _FsMplsLSPMapTunnelIngressLSRId_Type()
)
fsMplsLSPMapTunnelIngressLSRId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMplsLSPMapTunnelIngressLSRId.setStatus("current")
_FsMplsLSPMapTunnelEgressLSRId_Type = MplsExtendedTunnelId
_FsMplsLSPMapTunnelEgressLSRId_Object = MibTableColumn
fsMplsLSPMapTunnelEgressLSRId = _FsMplsLSPMapTunnelEgressLSRId_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 58, 1, 1, 1, 4),
    _FsMplsLSPMapTunnelEgressLSRId_Type()
)
fsMplsLSPMapTunnelEgressLSRId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMplsLSPMapTunnelEgressLSRId.setStatus("current")
_FsMplsLSPMapSubTunnelIndex_Type = MplsTunnelIndex
_FsMplsLSPMapSubTunnelIndex_Object = MibTableColumn
fsMplsLSPMapSubTunnelIndex = _FsMplsLSPMapSubTunnelIndex_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 58, 1, 1, 1, 5),
    _FsMplsLSPMapSubTunnelIndex_Type()
)
fsMplsLSPMapSubTunnelIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMplsLSPMapSubTunnelIndex.setStatus("current")
_FsMplsLSPMapSubTunnelInstance_Type = MplsTunnelInstanceIndex
_FsMplsLSPMapSubTunnelInstance_Object = MibTableColumn
fsMplsLSPMapSubTunnelInstance = _FsMplsLSPMapSubTunnelInstance_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 58, 1, 1, 1, 6),
    _FsMplsLSPMapSubTunnelInstance_Type()
)
fsMplsLSPMapSubTunnelInstance.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMplsLSPMapSubTunnelInstance.setStatus("current")
_FsMplsLSPMapSubTunnelIngressLSRId_Type = MplsExtendedTunnelId
_FsMplsLSPMapSubTunnelIngressLSRId_Object = MibTableColumn
fsMplsLSPMapSubTunnelIngressLSRId = _FsMplsLSPMapSubTunnelIngressLSRId_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 58, 1, 1, 1, 7),
    _FsMplsLSPMapSubTunnelIngressLSRId_Type()
)
fsMplsLSPMapSubTunnelIngressLSRId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMplsLSPMapSubTunnelIngressLSRId.setStatus("current")
_FsMplsLSPMapSubTunnelEgressLSRId_Type = MplsExtendedTunnelId
_FsMplsLSPMapSubTunnelEgressLSRId_Object = MibTableColumn
fsMplsLSPMapSubTunnelEgressLSRId = _FsMplsLSPMapSubTunnelEgressLSRId_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 58, 1, 1, 1, 8),
    _FsMplsLSPMapSubTunnelEgressLSRId_Type()
)
fsMplsLSPMapSubTunnelEgressLSRId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMplsLSPMapSubTunnelEgressLSRId.setStatus("current")
_FsMplsLSPMaptunnelOperation_Type = Unsigned32
_FsMplsLSPMaptunnelOperation_Object = MibTableColumn
fsMplsLSPMaptunnelOperation = _FsMplsLSPMaptunnelOperation_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 58, 1, 1, 1, 9),
    _FsMplsLSPMaptunnelOperation_Type()
)
fsMplsLSPMaptunnelOperation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMplsLSPMaptunnelOperation.setStatus("current")
_FsMplsLSPMaptunnelRowStatus_Type = RowStatus
_FsMplsLSPMaptunnelRowStatus_Object = MibTableColumn
fsMplsLSPMaptunnelRowStatus = _FsMplsLSPMaptunnelRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 58, 1, 1, 1, 10),
    _FsMplsLSPMaptunnelRowStatus_Type()
)
fsMplsLSPMaptunnelRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMplsLSPMaptunnelRowStatus.setStatus("current")
_FsMplsHLSPTable_Object = MibTable
fsMplsHLSPTable = _FsMplsHLSPTable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 58, 1, 2)
)
if mibBuilder.loadTexts:
    fsMplsHLSPTable.setStatus("current")
_FsMplsHLSPEntry_Object = MibTableRow
fsMplsHLSPEntry = _FsMplsHLSPEntry_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 58, 1, 2, 1)
)
fsMplsHLSPEntry.setIndexNames(
    (0, "Aricent-MPLS-HLSP-MIB", "fsMplsHLSPIndex"),
    (0, "Aricent-MPLS-HLSP-MIB", "fsMplsHLSPInstance"),
    (0, "Aricent-MPLS-HLSP-MIB", "fsMplsHLSPIngressLSRId"),
    (0, "Aricent-MPLS-HLSP-MIB", "fsMplsHLSPEgressLSRId"),
)
if mibBuilder.loadTexts:
    fsMplsHLSPEntry.setStatus("current")
_FsMplsHLSPIndex_Type = MplsTunnelIndex
_FsMplsHLSPIndex_Object = MibTableColumn
fsMplsHLSPIndex = _FsMplsHLSPIndex_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 58, 1, 2, 1, 1),
    _FsMplsHLSPIndex_Type()
)
fsMplsHLSPIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMplsHLSPIndex.setStatus("current")
_FsMplsHLSPInstance_Type = MplsTunnelInstanceIndex
_FsMplsHLSPInstance_Object = MibTableColumn
fsMplsHLSPInstance = _FsMplsHLSPInstance_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 58, 1, 2, 1, 2),
    _FsMplsHLSPInstance_Type()
)
fsMplsHLSPInstance.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMplsHLSPInstance.setStatus("current")
_FsMplsHLSPIngressLSRId_Type = MplsExtendedTunnelId
_FsMplsHLSPIngressLSRId_Object = MibTableColumn
fsMplsHLSPIngressLSRId = _FsMplsHLSPIngressLSRId_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 58, 1, 2, 1, 3),
    _FsMplsHLSPIngressLSRId_Type()
)
fsMplsHLSPIngressLSRId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMplsHLSPIngressLSRId.setStatus("current")
_FsMplsHLSPEgressLSRId_Type = MplsExtendedTunnelId
_FsMplsHLSPEgressLSRId_Object = MibTableColumn
fsMplsHLSPEgressLSRId = _FsMplsHLSPEgressLSRId_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 58, 1, 2, 1, 4),
    _FsMplsHLSPEgressLSRId_Type()
)
fsMplsHLSPEgressLSRId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMplsHLSPEgressLSRId.setStatus("current")
_FsMplsHLSPAvailableBW_Type = Unsigned32
_FsMplsHLSPAvailableBW_Object = MibTableColumn
fsMplsHLSPAvailableBW = _FsMplsHLSPAvailableBW_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 58, 1, 2, 1, 5),
    _FsMplsHLSPAvailableBW_Type()
)
fsMplsHLSPAvailableBW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMplsHLSPAvailableBW.setStatus("current")
_FsMplsHLSPNoOfStackedTunnels_Type = Unsigned32
_FsMplsHLSPNoOfStackedTunnels_Object = MibTableColumn
fsMplsHLSPNoOfStackedTunnels = _FsMplsHLSPNoOfStackedTunnels_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 58, 1, 2, 1, 6),
    _FsMplsHLSPNoOfStackedTunnels_Type()
)
fsMplsHLSPNoOfStackedTunnels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMplsHLSPNoOfStackedTunnels.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Aricent-MPLS-HLSP-MIB",
    **{"fsHlspMIB": fsHlspMIB,
       "fsMplsHlspConfigObjects": fsMplsHlspConfigObjects,
       "fsMplsLSPMapTunnelTable": fsMplsLSPMapTunnelTable,
       "fsMplsLSPMapTunnelEntry": fsMplsLSPMapTunnelEntry,
       "fsMplsLSPMapTunnelIndex": fsMplsLSPMapTunnelIndex,
       "fsMplsLSPMapTunnelInstance": fsMplsLSPMapTunnelInstance,
       "fsMplsLSPMapTunnelIngressLSRId": fsMplsLSPMapTunnelIngressLSRId,
       "fsMplsLSPMapTunnelEgressLSRId": fsMplsLSPMapTunnelEgressLSRId,
       "fsMplsLSPMapSubTunnelIndex": fsMplsLSPMapSubTunnelIndex,
       "fsMplsLSPMapSubTunnelInstance": fsMplsLSPMapSubTunnelInstance,
       "fsMplsLSPMapSubTunnelIngressLSRId": fsMplsLSPMapSubTunnelIngressLSRId,
       "fsMplsLSPMapSubTunnelEgressLSRId": fsMplsLSPMapSubTunnelEgressLSRId,
       "fsMplsLSPMaptunnelOperation": fsMplsLSPMaptunnelOperation,
       "fsMplsLSPMaptunnelRowStatus": fsMplsLSPMaptunnelRowStatus,
       "fsMplsHLSPTable": fsMplsHLSPTable,
       "fsMplsHLSPEntry": fsMplsHLSPEntry,
       "fsMplsHLSPIndex": fsMplsHLSPIndex,
       "fsMplsHLSPInstance": fsMplsHLSPInstance,
       "fsMplsHLSPIngressLSRId": fsMplsHLSPIngressLSRId,
       "fsMplsHLSPEgressLSRId": fsMplsHLSPEgressLSRId,
       "fsMplsHLSPAvailableBW": fsMplsHLSPAvailableBW,
       "fsMplsHLSPNoOfStackedTunnels": fsMplsHLSPNoOfStackedTunnels}
)
