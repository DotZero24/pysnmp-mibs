# SNMP MIB module (INFINERA-TP-PXMLSP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/INFINERA-TP-PXMLSP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:14:19 2025
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(terminationPoint,) = mibBuilder.importSymbols(
    "INFINERA-REG-MIB",
    "terminationPoint")

(InfnEnableDisable,
 InfnLSPLoopBackBehaviour,
 InfnLSPType,
 InfnMplsQosModel) = mibBuilder.importSymbols(
    "INFINERA-TC-MIB",
    "InfnEnableDisable",
    "InfnLSPLoopBackBehaviour",
    "InfnLSPType",
    "InfnMplsQosModel")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

lspMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 71)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_LspTable_Object = MibTable
lspTable = _LspTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 71, 1)
)
if mibBuilder.loadTexts:
    lspTable.setStatus("current")
_LspEntry_Object = MibTableRow
lspEntry = _LspEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 71, 1, 1)
)
lspEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    lspEntry.setStatus("current")
_LspType_Type = InfnLSPType
_LspType_Object = MibTableColumn
lspType = _LspType_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 71, 1, 1, 1),
    _LspType_Type()
)
lspType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lspType.setStatus("current")
_LspIncomingLabel_Type = Integer32
_LspIncomingLabel_Object = MibTableColumn
lspIncomingLabel = _LspIncomingLabel_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 71, 1, 1, 2),
    _LspIncomingLabel_Type()
)
lspIncomingLabel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lspIncomingLabel.setStatus("current")
_LspOutgoingLabel_Type = Integer32
_LspOutgoingLabel_Object = MibTableColumn
lspOutgoingLabel = _LspOutgoingLabel_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 71, 1, 1, 3),
    _LspOutgoingLabel_Type()
)
lspOutgoingLabel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lspOutgoingLabel.setStatus("current")
_LspQOSModel_Type = InfnMplsQosModel
_LspQOSModel_Object = MibTableColumn
lspQOSModel = _LspQOSModel_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 71, 1, 1, 4),
    _LspQOSModel_Type()
)
lspQOSModel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lspQOSModel.setStatus("current")
_LspConfiguredTTL_Type = Integer32
_LspConfiguredTTL_Object = MibTableColumn
lspConfiguredTTL = _LspConfiguredTTL_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 71, 1, 1, 5),
    _LspConfiguredTTL_Type()
)
lspConfiguredTTL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lspConfiguredTTL.setStatus("current")
_LspConfiguredTrafficClass_Type = Integer32
_LspConfiguredTrafficClass_Object = MibTableColumn
lspConfiguredTrafficClass = _LspConfiguredTrafficClass_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 71, 1, 1, 6),
    _LspConfiguredTrafficClass_Type()
)
lspConfiguredTrafficClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lspConfiguredTrafficClass.setStatus("current")
_LspMaxReservableBw_Type = Integer32
_LspMaxReservableBw_Object = MibTableColumn
lspMaxReservableBw = _LspMaxReservableBw_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 71, 1, 1, 7),
    _LspMaxReservableBw_Type()
)
lspMaxReservableBw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lspMaxReservableBw.setStatus("current")
_LspAvailableBW_Type = Integer32
_LspAvailableBW_Object = MibTableColumn
lspAvailableBW = _LspAvailableBW_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 71, 1, 1, 8),
    _LspAvailableBW_Type()
)
lspAvailableBW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lspAvailableBW.setStatus("current")
_LspLoopBack_Type = InfnEnableDisable
_LspLoopBack_Object = MibTableColumn
lspLoopBack = _LspLoopBack_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 71, 1, 1, 9),
    _LspLoopBack_Type()
)
lspLoopBack.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lspLoopBack.setStatus("current")
_LspLoopBackbehaviour_Type = InfnLSPLoopBackBehaviour
_LspLoopBackbehaviour_Object = MibTableColumn
lspLoopBackbehaviour = _LspLoopBackbehaviour_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 71, 1, 1, 10),
    _LspLoopBackbehaviour_Type()
)
lspLoopBackbehaviour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lspLoopBackbehaviour.setStatus("current")
_LspId_Type = DisplayString
_LspId_Object = MibTableColumn
lspId = _LspId_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 71, 1, 1, 11),
    _LspId_Type()
)
lspId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lspId.setStatus("current")
_LspSupportingEqptAid_Type = DisplayString
_LspSupportingEqptAid_Object = MibTableColumn
lspSupportingEqptAid = _LspSupportingEqptAid_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 71, 1, 1, 12),
    _LspSupportingEqptAid_Type()
)
lspSupportingEqptAid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lspSupportingEqptAid.setStatus("current")
_LspNum_Type = Integer32
_LspNum_Object = MibTableColumn
lspNum = _LspNum_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 71, 1, 1, 13),
    _LspNum_Type()
)
lspNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lspNum.setStatus("current")
_LspNextHop_Type = DisplayString
_LspNextHop_Object = MibTableColumn
lspNextHop = _LspNextHop_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 71, 1, 1, 14),
    _LspNextHop_Type()
)
lspNextHop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lspNextHop.setStatus("current")
_LspAssociatedPeerLSP_Type = DisplayString
_LspAssociatedPeerLSP_Object = MibTableColumn
lspAssociatedPeerLSP = _LspAssociatedPeerLSP_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 71, 1, 1, 15),
    _LspAssociatedPeerLSP_Type()
)
lspAssociatedPeerLSP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lspAssociatedPeerLSP.setStatus("current")
_LspAssociatedMplsTunnel_Type = DisplayString
_LspAssociatedMplsTunnel_Object = MibTableColumn
lspAssociatedMplsTunnel = _LspAssociatedMplsTunnel_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 71, 1, 1, 16),
    _LspAssociatedMplsTunnel_Type()
)
lspAssociatedMplsTunnel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lspAssociatedMplsTunnel.setStatus("current")
_LspConformance_ObjectIdentity = ObjectIdentity
lspConformance = _LspConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 71, 3)
)
_LspCompliances_ObjectIdentity = ObjectIdentity
lspCompliances = _LspCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 71, 3, 1)
)
_LspGroups_ObjectIdentity = ObjectIdentity
lspGroups = _LspGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 71, 3, 2)
)

# Managed Objects groups

lspGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 71, 3, 2, 1)
)
lspGroup.setObjects(
      *(("INFINERA-TP-PXMLSP-MIB", "lspType"),
        ("INFINERA-TP-PXMLSP-MIB", "lspIncomingLabel"),
        ("INFINERA-TP-PXMLSP-MIB", "lspOutgoingLabel"),
        ("INFINERA-TP-PXMLSP-MIB", "lspQOSModel"),
        ("INFINERA-TP-PXMLSP-MIB", "lspConfiguredTTL"),
        ("INFINERA-TP-PXMLSP-MIB", "lspConfiguredTrafficClass"),
        ("INFINERA-TP-PXMLSP-MIB", "lspMaxReservableBw"),
        ("INFINERA-TP-PXMLSP-MIB", "lspAvailableBW"),
        ("INFINERA-TP-PXMLSP-MIB", "lspLoopBack"),
        ("INFINERA-TP-PXMLSP-MIB", "lspLoopBackbehaviour"),
        ("INFINERA-TP-PXMLSP-MIB", "lspId"),
        ("INFINERA-TP-PXMLSP-MIB", "lspSupportingEqptAid"),
        ("INFINERA-TP-PXMLSP-MIB", "lspNum"),
        ("INFINERA-TP-PXMLSP-MIB", "lspNextHop"),
        ("INFINERA-TP-PXMLSP-MIB", "lspAssociatedPeerLSP"),
        ("INFINERA-TP-PXMLSP-MIB", "lspAssociatedMplsTunnel"))
)
if mibBuilder.loadTexts:
    lspGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

lspCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 71, 3, 1, 1)
)
lspCompliance.setObjects(
    ("INFINERA-TP-PXMLSP-MIB", "lspGroup")
)
if mibBuilder.loadTexts:
    lspCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INFINERA-TP-PXMLSP-MIB",
    **{"lspMIB": lspMIB,
       "lspTable": lspTable,
       "lspEntry": lspEntry,
       "lspType": lspType,
       "lspIncomingLabel": lspIncomingLabel,
       "lspOutgoingLabel": lspOutgoingLabel,
       "lspQOSModel": lspQOSModel,
       "lspConfiguredTTL": lspConfiguredTTL,
       "lspConfiguredTrafficClass": lspConfiguredTrafficClass,
       "lspMaxReservableBw": lspMaxReservableBw,
       "lspAvailableBW": lspAvailableBW,
       "lspLoopBack": lspLoopBack,
       "lspLoopBackbehaviour": lspLoopBackbehaviour,
       "lspId": lspId,
       "lspSupportingEqptAid": lspSupportingEqptAid,
       "lspNum": lspNum,
       "lspNextHop": lspNextHop,
       "lspAssociatedPeerLSP": lspAssociatedPeerLSP,
       "lspAssociatedMplsTunnel": lspAssociatedMplsTunnel,
       "lspConformance": lspConformance,
       "lspCompliances": lspCompliances,
       "lspCompliance": lspCompliance,
       "lspGroups": lspGroups,
       "lspGroup": lspGroup}
)
