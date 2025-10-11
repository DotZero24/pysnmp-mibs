# SNMP MIB module (INFINERA-TP-PXMTUNNEL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/INFINERA-TP-PXMTUNNEL-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:14:14 2025
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

pxmTunnelMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 69)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_PxmTunnelTable_Object = MibTable
pxmTunnelTable = _PxmTunnelTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 69, 1)
)
if mibBuilder.loadTexts:
    pxmTunnelTable.setStatus("current")
_PxmTunnelEntry_Object = MibTableRow
pxmTunnelEntry = _PxmTunnelEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 69, 1, 1)
)
pxmTunnelEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    pxmTunnelEntry.setStatus("current")
_PxmTunnelMTUSize_Type = Integer32
_PxmTunnelMTUSize_Object = MibTableColumn
pxmTunnelMTUSize = _PxmTunnelMTUSize_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 69, 1, 1, 1),
    _PxmTunnelMTUSize_Type()
)
pxmTunnelMTUSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pxmTunnelMTUSize.setStatus("current")
_PxmTunnelNum_Type = Integer32
_PxmTunnelNum_Object = MibTableColumn
pxmTunnelNum = _PxmTunnelNum_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 69, 1, 1, 2),
    _PxmTunnelNum_Type()
)
pxmTunnelNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pxmTunnelNum.setStatus("current")
_PxmTunnelId_Type = DisplayString
_PxmTunnelId_Object = MibTableColumn
pxmTunnelId = _PxmTunnelId_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 69, 1, 1, 3),
    _PxmTunnelId_Type()
)
pxmTunnelId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pxmTunnelId.setStatus("current")
_PxmTunnelSupportingEqptAid_Type = DisplayString
_PxmTunnelSupportingEqptAid_Object = MibTableColumn
pxmTunnelSupportingEqptAid = _PxmTunnelSupportingEqptAid_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 69, 1, 1, 4),
    _PxmTunnelSupportingEqptAid_Type()
)
pxmTunnelSupportingEqptAid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pxmTunnelSupportingEqptAid.setStatus("current")
_PxmTunnelAssociatedLSPList_Type = DisplayString
_PxmTunnelAssociatedLSPList_Object = MibTableColumn
pxmTunnelAssociatedLSPList = _PxmTunnelAssociatedLSPList_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 69, 1, 1, 5),
    _PxmTunnelAssociatedLSPList_Type()
)
pxmTunnelAssociatedLSPList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmTunnelAssociatedLSPList.setStatus("current")
_PxmTunnelConformance_ObjectIdentity = ObjectIdentity
pxmTunnelConformance = _PxmTunnelConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 69, 3)
)
_PxmTunnelCompliances_ObjectIdentity = ObjectIdentity
pxmTunnelCompliances = _PxmTunnelCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 69, 3, 1)
)
_PxmTunnelGroups_ObjectIdentity = ObjectIdentity
pxmTunnelGroups = _PxmTunnelGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 69, 3, 2)
)

# Managed Objects groups

pxmTunnelGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 69, 3, 2, 1)
)
pxmTunnelGroup.setObjects(
      *(("INFINERA-TP-PXMTUNNEL-MIB", "pxmTunnelMTUSize"),
        ("INFINERA-TP-PXMTUNNEL-MIB", "pxmTunnelNum"),
        ("INFINERA-TP-PXMTUNNEL-MIB", "pxmTunnelId"),
        ("INFINERA-TP-PXMTUNNEL-MIB", "pxmTunnelSupportingEqptAid"),
        ("INFINERA-TP-PXMTUNNEL-MIB", "pxmTunnelAssociatedLSPList"))
)
if mibBuilder.loadTexts:
    pxmTunnelGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

pxmTunnelCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 69, 3, 1, 1)
)
pxmTunnelCompliance.setObjects(
    ("INFINERA-TP-PXMTUNNEL-MIB", "pxmTunnelGroup")
)
if mibBuilder.loadTexts:
    pxmTunnelCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INFINERA-TP-PXMTUNNEL-MIB",
    **{"pxmTunnelMIB": pxmTunnelMIB,
       "pxmTunnelTable": pxmTunnelTable,
       "pxmTunnelEntry": pxmTunnelEntry,
       "pxmTunnelMTUSize": pxmTunnelMTUSize,
       "pxmTunnelNum": pxmTunnelNum,
       "pxmTunnelId": pxmTunnelId,
       "pxmTunnelSupportingEqptAid": pxmTunnelSupportingEqptAid,
       "pxmTunnelAssociatedLSPList": pxmTunnelAssociatedLSPList,
       "pxmTunnelConformance": pxmTunnelConformance,
       "pxmTunnelCompliances": pxmTunnelCompliances,
       "pxmTunnelCompliance": pxmTunnelCompliance,
       "pxmTunnelGroups": pxmTunnelGroups,
       "pxmTunnelGroup": pxmTunnelGroup}
)
