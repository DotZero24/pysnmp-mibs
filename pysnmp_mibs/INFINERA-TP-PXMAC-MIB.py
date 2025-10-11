# SNMP MIB module (INFINERA-TP-PXMAC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/INFINERA-TP-PXMAC-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:16:53 2025
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

(FloatTenths,
 InfnActionOnVlan,
 InfnCreationType,
 InfnEgressActionPriority,
 InfnFlapActionClear,
 InfnIngressMatchCriteria,
 InfnLoopback,
 InfnLoopbackBehavior,
 InfnPmHistStatsControl) = mibBuilder.importSymbols(
    "INFINERA-TC-MIB",
    "FloatTenths",
    "InfnActionOnVlan",
    "InfnCreationType",
    "InfnEgressActionPriority",
    "InfnFlapActionClear",
    "InfnIngressMatchCriteria",
    "InfnLoopback",
    "InfnLoopbackBehavior",
    "InfnPmHistStatsControl")

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

pxmAcMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 72)
)
if mibBuilder.loadTexts:
    pxmAcMIB.setRevisions(
        ("2016-05-15 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_PxmAcTable_Object = MibTable
pxmAcTable = _PxmAcTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 72, 1)
)
if mibBuilder.loadTexts:
    pxmAcTable.setStatus("current")
_PxmAcEntry_Object = MibTableRow
pxmAcEntry = _PxmAcEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 72, 1, 1)
)
pxmAcEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    pxmAcEntry.setStatus("current")
_PxmAcIngressMatchCriteria_Type = InfnIngressMatchCriteria
_PxmAcIngressMatchCriteria_Object = MibTableColumn
pxmAcIngressMatchCriteria = _PxmAcIngressMatchCriteria_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 72, 1, 1, 1),
    _PxmAcIngressMatchCriteria_Type()
)
pxmAcIngressMatchCriteria.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pxmAcIngressMatchCriteria.setStatus("current")
_PxmAcIngressMatchOuterVlanId_Type = DisplayString
_PxmAcIngressMatchOuterVlanId_Object = MibTableColumn
pxmAcIngressMatchOuterVlanId = _PxmAcIngressMatchOuterVlanId_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 72, 1, 1, 2),
    _PxmAcIngressMatchOuterVlanId_Type()
)
pxmAcIngressMatchOuterVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pxmAcIngressMatchOuterVlanId.setStatus("current")
_PxmAcIngressMatchInnerVlanId_Type = DisplayString
_PxmAcIngressMatchInnerVlanId_Object = MibTableColumn
pxmAcIngressMatchInnerVlanId = _PxmAcIngressMatchInnerVlanId_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 72, 1, 1, 3),
    _PxmAcIngressMatchInnerVlanId_Type()
)
pxmAcIngressMatchInnerVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pxmAcIngressMatchInnerVlanId.setStatus("current")
_PxmAcIngressMatchOuterPriority_Type = DisplayString
_PxmAcIngressMatchOuterPriority_Object = MibTableColumn
pxmAcIngressMatchOuterPriority = _PxmAcIngressMatchOuterPriority_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 72, 1, 1, 4),
    _PxmAcIngressMatchOuterPriority_Type()
)
pxmAcIngressMatchOuterPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pxmAcIngressMatchOuterPriority.setStatus("current")
_PxmAcIngressActionOuterVlan_Type = InfnActionOnVlan
_PxmAcIngressActionOuterVlan_Object = MibTableColumn
pxmAcIngressActionOuterVlan = _PxmAcIngressActionOuterVlan_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 72, 1, 1, 5),
    _PxmAcIngressActionOuterVlan_Type()
)
pxmAcIngressActionOuterVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pxmAcIngressActionOuterVlan.setStatus("current")
_PxmAcIngressRewriteOuterVlanId_Type = Integer32
_PxmAcIngressRewriteOuterVlanId_Object = MibTableColumn
pxmAcIngressRewriteOuterVlanId = _PxmAcIngressRewriteOuterVlanId_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 72, 1, 1, 6),
    _PxmAcIngressRewriteOuterVlanId_Type()
)
pxmAcIngressRewriteOuterVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pxmAcIngressRewriteOuterVlanId.setStatus("current")
_PxmAcEgressActionOuterVlan_Type = InfnActionOnVlan
_PxmAcEgressActionOuterVlan_Object = MibTableColumn
pxmAcEgressActionOuterVlan = _PxmAcEgressActionOuterVlan_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 72, 1, 1, 7),
    _PxmAcEgressActionOuterVlan_Type()
)
pxmAcEgressActionOuterVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pxmAcEgressActionOuterVlan.setStatus("current")
_PxmAcEgressRewriteOuterVlanId_Type = Integer32
_PxmAcEgressRewriteOuterVlanId_Object = MibTableColumn
pxmAcEgressRewriteOuterVlanId = _PxmAcEgressRewriteOuterVlanId_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 72, 1, 1, 8),
    _PxmAcEgressRewriteOuterVlanId_Type()
)
pxmAcEgressRewriteOuterVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pxmAcEgressRewriteOuterVlanId.setStatus("current")
_PxmAcEgressActionInnerVlan_Type = InfnActionOnVlan
_PxmAcEgressActionInnerVlan_Object = MibTableColumn
pxmAcEgressActionInnerVlan = _PxmAcEgressActionInnerVlan_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 72, 1, 1, 9),
    _PxmAcEgressActionInnerVlan_Type()
)
pxmAcEgressActionInnerVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pxmAcEgressActionInnerVlan.setStatus("current")
_PxmAcEgressRewriteInnerVlanId_Type = Integer32
_PxmAcEgressRewriteInnerVlanId_Object = MibTableColumn
pxmAcEgressRewriteInnerVlanId = _PxmAcEgressRewriteInnerVlanId_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 72, 1, 1, 10),
    _PxmAcEgressRewriteInnerVlanId_Type()
)
pxmAcEgressRewriteInnerVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pxmAcEgressRewriteInnerVlanId.setStatus("current")
_PxmAcEgressActionOuterPriority_Type = InfnEgressActionPriority
_PxmAcEgressActionOuterPriority_Object = MibTableColumn
pxmAcEgressActionOuterPriority = _PxmAcEgressActionOuterPriority_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 72, 1, 1, 11),
    _PxmAcEgressActionOuterPriority_Type()
)
pxmAcEgressActionOuterPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pxmAcEgressActionOuterPriority.setStatus("current")
_PxmAcEgressRewriteOuterPriority_Type = Integer32
_PxmAcEgressRewriteOuterPriority_Object = MibTableColumn
pxmAcEgressRewriteOuterPriority = _PxmAcEgressRewriteOuterPriority_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 72, 1, 1, 12),
    _PxmAcEgressRewriteOuterPriority_Type()
)
pxmAcEgressRewriteOuterPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pxmAcEgressRewriteOuterPriority.setStatus("current")
_PxmAcEgressActionInnerPriority_Type = InfnEgressActionPriority
_PxmAcEgressActionInnerPriority_Object = MibTableColumn
pxmAcEgressActionInnerPriority = _PxmAcEgressActionInnerPriority_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 72, 1, 1, 13),
    _PxmAcEgressActionInnerPriority_Type()
)
pxmAcEgressActionInnerPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pxmAcEgressActionInnerPriority.setStatus("current")
_PxmAcEgressRewriteInnerPriority_Type = Integer32
_PxmAcEgressRewriteInnerPriority_Object = MibTableColumn
pxmAcEgressRewriteInnerPriority = _PxmAcEgressRewriteInnerPriority_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 72, 1, 1, 14),
    _PxmAcEgressRewriteInnerPriority_Type()
)
pxmAcEgressRewriteInnerPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pxmAcEgressRewriteInnerPriority.setStatus("current")
_PxmAcIngressTrafficClass_Type = Integer32
_PxmAcIngressTrafficClass_Object = MibTableColumn
pxmAcIngressTrafficClass = _PxmAcIngressTrafficClass_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 72, 1, 1, 15),
    _PxmAcIngressTrafficClass_Type()
)
pxmAcIngressTrafficClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pxmAcIngressTrafficClass.setStatus("current")
_PxmAcLoopback_Type = InfnLoopback
_PxmAcLoopback_Object = MibTableColumn
pxmAcLoopback = _PxmAcLoopback_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 72, 1, 1, 16),
    _PxmAcLoopback_Type()
)
pxmAcLoopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pxmAcLoopback.setStatus("current")
_PxmAcLoopbackBehavior_Type = InfnLoopbackBehavior
_PxmAcLoopbackBehavior_Object = MibTableColumn
pxmAcLoopbackBehavior = _PxmAcLoopbackBehavior_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 72, 1, 1, 17),
    _PxmAcLoopbackBehavior_Type()
)
pxmAcLoopbackBehavior.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pxmAcLoopbackBehavior.setStatus("current")
_PxmAcCreationType_Type = InfnCreationType
_PxmAcCreationType_Object = MibTableColumn
pxmAcCreationType = _PxmAcCreationType_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 72, 1, 1, 18),
    _PxmAcCreationType_Type()
)
pxmAcCreationType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pxmAcCreationType.setStatus("current")
_PxmAcPmHistStatsEnable_Type = InfnPmHistStatsControl
_PxmAcPmHistStatsEnable_Object = MibTableColumn
pxmAcPmHistStatsEnable = _PxmAcPmHistStatsEnable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 72, 1, 1, 19),
    _PxmAcPmHistStatsEnable_Type()
)
pxmAcPmHistStatsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pxmAcPmHistStatsEnable.setStatus("current")
_PxmAcSplitHorizonGroupID_Type = Integer32
_PxmAcSplitHorizonGroupID_Object = MibTableColumn
pxmAcSplitHorizonGroupID = _PxmAcSplitHorizonGroupID_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 72, 1, 1, 20),
    _PxmAcSplitHorizonGroupID_Type()
)
pxmAcSplitHorizonGroupID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pxmAcSplitHorizonGroupID.setStatus("current")
_PxmAcFlapActionClear_Type = InfnFlapActionClear
_PxmAcFlapActionClear_Object = MibTableColumn
pxmAcFlapActionClear = _PxmAcFlapActionClear_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 72, 1, 1, 21),
    _PxmAcFlapActionClear_Type()
)
pxmAcFlapActionClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pxmAcFlapActionClear.setStatus("current")
_PxmAcConformance_ObjectIdentity = ObjectIdentity
pxmAcConformance = _PxmAcConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 72, 3)
)
_PxmAcCompliances_ObjectIdentity = ObjectIdentity
pxmAcCompliances = _PxmAcCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 72, 3, 1)
)
_PxmAcGroups_ObjectIdentity = ObjectIdentity
pxmAcGroups = _PxmAcGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 72, 3, 2)
)

# Managed Objects groups

pxmAcGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 72, 3, 2, 1)
)
pxmAcGroup.setObjects(
      *(("INFINERA-TP-PXMAC-MIB", "pxmAcIngressMatchCriteria"),
        ("INFINERA-TP-PXMAC-MIB", "pxmAcIngressMatchOuterVlanId"),
        ("INFINERA-TP-PXMAC-MIB", "pxmAcIngressMatchInnerVlanId"),
        ("INFINERA-TP-PXMAC-MIB", "pxmAcIngressMatchOuterPriority"),
        ("INFINERA-TP-PXMAC-MIB", "pxmAcIngressActionOuterVlan"),
        ("INFINERA-TP-PXMAC-MIB", "pxmAcIngressRewriteOuterVlanId"),
        ("INFINERA-TP-PXMAC-MIB", "pxmAcEgressActionOuterVlan"),
        ("INFINERA-TP-PXMAC-MIB", "pxmAcEgressRewriteOuterVlanId"),
        ("INFINERA-TP-PXMAC-MIB", "pxmAcEgressActionInnerVlan"),
        ("INFINERA-TP-PXMAC-MIB", "pxmAcEgressRewriteInnerVlanId"),
        ("INFINERA-TP-PXMAC-MIB", "pxmAcEgressActionOuterPriority"),
        ("INFINERA-TP-PXMAC-MIB", "pxmAcEgressRewriteOuterPriority"),
        ("INFINERA-TP-PXMAC-MIB", "pxmAcEgressActionInnerPriority"),
        ("INFINERA-TP-PXMAC-MIB", "pxmAcEgressRewriteInnerPriority"),
        ("INFINERA-TP-PXMAC-MIB", "pxmAcIngressTrafficClass"),
        ("INFINERA-TP-PXMAC-MIB", "pxmAcLoopback"),
        ("INFINERA-TP-PXMAC-MIB", "pxmAcLoopbackBehavior"),
        ("INFINERA-TP-PXMAC-MIB", "pxmAcCreationType"),
        ("INFINERA-TP-PXMAC-MIB", "pxmAcPmHistStatsEnable"),
        ("INFINERA-TP-PXMAC-MIB", "pxmAcSplitHorizonGroupID"),
        ("INFINERA-TP-PXMAC-MIB", "pxmAcFlapActionClear"))
)
if mibBuilder.loadTexts:
    pxmAcGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

pxmAcCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 72, 3, 1, 1)
)
pxmAcCompliance.setObjects(
    ("INFINERA-TP-PXMAC-MIB", "pxmAcGroup")
)
if mibBuilder.loadTexts:
    pxmAcCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INFINERA-TP-PXMAC-MIB",
    **{"pxmAcMIB": pxmAcMIB,
       "pxmAcTable": pxmAcTable,
       "pxmAcEntry": pxmAcEntry,
       "pxmAcIngressMatchCriteria": pxmAcIngressMatchCriteria,
       "pxmAcIngressMatchOuterVlanId": pxmAcIngressMatchOuterVlanId,
       "pxmAcIngressMatchInnerVlanId": pxmAcIngressMatchInnerVlanId,
       "pxmAcIngressMatchOuterPriority": pxmAcIngressMatchOuterPriority,
       "pxmAcIngressActionOuterVlan": pxmAcIngressActionOuterVlan,
       "pxmAcIngressRewriteOuterVlanId": pxmAcIngressRewriteOuterVlanId,
       "pxmAcEgressActionOuterVlan": pxmAcEgressActionOuterVlan,
       "pxmAcEgressRewriteOuterVlanId": pxmAcEgressRewriteOuterVlanId,
       "pxmAcEgressActionInnerVlan": pxmAcEgressActionInnerVlan,
       "pxmAcEgressRewriteInnerVlanId": pxmAcEgressRewriteInnerVlanId,
       "pxmAcEgressActionOuterPriority": pxmAcEgressActionOuterPriority,
       "pxmAcEgressRewriteOuterPriority": pxmAcEgressRewriteOuterPriority,
       "pxmAcEgressActionInnerPriority": pxmAcEgressActionInnerPriority,
       "pxmAcEgressRewriteInnerPriority": pxmAcEgressRewriteInnerPriority,
       "pxmAcIngressTrafficClass": pxmAcIngressTrafficClass,
       "pxmAcLoopback": pxmAcLoopback,
       "pxmAcLoopbackBehavior": pxmAcLoopbackBehavior,
       "pxmAcCreationType": pxmAcCreationType,
       "pxmAcPmHistStatsEnable": pxmAcPmHistStatsEnable,
       "pxmAcSplitHorizonGroupID": pxmAcSplitHorizonGroupID,
       "pxmAcFlapActionClear": pxmAcFlapActionClear,
       "pxmAcConformance": pxmAcConformance,
       "pxmAcCompliances": pxmAcCompliances,
       "pxmAcCompliance": pxmAcCompliance,
       "pxmAcGroups": pxmAcGroups,
       "pxmAcGroup": pxmAcGroup}
)
