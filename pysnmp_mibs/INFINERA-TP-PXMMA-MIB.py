# SNMP MIB module (INFINERA-TP-PXMMA-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/INFINERA-TP-PXMMA-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:17:05 2025
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

(InfnCcmInterval,
 InfnMANameFormat,
 InfnSenderIDTLV) = mibBuilder.importSymbols(
    "INFINERA-TC-MIB",
    "InfnCcmInterval",
    "InfnMANameFormat",
    "InfnSenderIDTLV")

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


# MODULE-IDENTITY

pxmMaMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 79)
)
if mibBuilder.loadTexts:
    pxmMaMIB.setRevisions(
        ("2016-05-30 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_PxmMaTable_Object = MibTable
pxmMaTable = _PxmMaTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 79, 1)
)
if mibBuilder.loadTexts:
    pxmMaTable.setStatus("current")
_PxmMaEntry_Object = MibTableRow
pxmMaEntry = _PxmMaEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 79, 1, 1)
)
pxmMaEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    pxmMaEntry.setStatus("current")
_PxmMaMAName_Type = DisplayString
_PxmMaMAName_Object = MibTableColumn
pxmMaMAName = _PxmMaMAName_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 79, 1, 1, 1),
    _PxmMaMAName_Type()
)
pxmMaMAName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pxmMaMAName.setStatus("current")
_PxmMaRMepAgeOutInterval_Type = Integer32
_PxmMaRMepAgeOutInterval_Object = MibTableColumn
pxmMaRMepAgeOutInterval = _PxmMaRMepAgeOutInterval_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 79, 1, 1, 2),
    _PxmMaRMepAgeOutInterval_Type()
)
pxmMaRMepAgeOutInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pxmMaRMepAgeOutInterval.setStatus("current")
_PxmMaMDAid_Type = DisplayString
_PxmMaMDAid_Object = MibTableColumn
pxmMaMDAid = _PxmMaMDAid_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 79, 1, 1, 3),
    _PxmMaMDAid_Type()
)
pxmMaMDAid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmMaMDAid.setStatus("current")
_PxmMaCcmInterval_Type = InfnCcmInterval
_PxmMaCcmInterval_Object = MibTableColumn
pxmMaCcmInterval = _PxmMaCcmInterval_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 79, 1, 1, 4),
    _PxmMaCcmInterval_Type()
)
pxmMaCcmInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pxmMaCcmInterval.setStatus("current")
_PxmMaMANameFormat_Type = InfnMANameFormat
_PxmMaMANameFormat_Object = MibTableColumn
pxmMaMANameFormat = _PxmMaMANameFormat_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 79, 1, 1, 5),
    _PxmMaMANameFormat_Type()
)
pxmMaMANameFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pxmMaMANameFormat.setStatus("current")
_PxmMaSenderIDTLV_Type = InfnSenderIDTLV
_PxmMaSenderIDTLV_Object = MibTableColumn
pxmMaSenderIDTLV = _PxmMaSenderIDTLV_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 79, 1, 1, 6),
    _PxmMaSenderIDTLV_Type()
)
pxmMaSenderIDTLV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmMaSenderIDTLV.setStatus("current")
_PxmMaMDName_Type = DisplayString
_PxmMaMDName_Object = MibTableColumn
pxmMaMDName = _PxmMaMDName_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 79, 1, 1, 7),
    _PxmMaMDName_Type()
)
pxmMaMDName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmMaMDName.setStatus("current")
_PxmMaMDLevel_Type = Integer32
_PxmMaMDLevel_Object = MibTableColumn
pxmMaMDLevel = _PxmMaMDLevel_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 79, 1, 1, 8),
    _PxmMaMDLevel_Type()
)
pxmMaMDLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxmMaMDLevel.setStatus("current")
_PxmMaConformance_ObjectIdentity = ObjectIdentity
pxmMaConformance = _PxmMaConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 79, 3)
)
_PxmMaCompliances_ObjectIdentity = ObjectIdentity
pxmMaCompliances = _PxmMaCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 79, 3, 1)
)
_PxmMaGroups_ObjectIdentity = ObjectIdentity
pxmMaGroups = _PxmMaGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 79, 3, 2)
)

# Managed Objects groups

pxmMaGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 79, 3, 2, 1)
)
pxmMaGroup.setObjects(
      *(("INFINERA-TP-PXMMA-MIB", "pxmMaMAName"),
        ("INFINERA-TP-PXMMA-MIB", "pxmMaRMepAgeOutInterval"),
        ("INFINERA-TP-PXMMA-MIB", "pxmMaMDAid"),
        ("INFINERA-TP-PXMMA-MIB", "pxmMaCcmInterval"),
        ("INFINERA-TP-PXMMA-MIB", "pxmMaMANameFormat"),
        ("INFINERA-TP-PXMMA-MIB", "pxmMaSenderIDTLV"),
        ("INFINERA-TP-PXMMA-MIB", "pxmMaMDName"),
        ("INFINERA-TP-PXMMA-MIB", "pxmMaMDLevel"))
)
if mibBuilder.loadTexts:
    pxmMaGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

pxmMaCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 79, 3, 1, 1)
)
pxmMaCompliance.setObjects(
    ("INFINERA-TP-PXMMA-MIB", "pxmMaGroup")
)
if mibBuilder.loadTexts:
    pxmMaCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INFINERA-TP-PXMMA-MIB",
    **{"pxmMaMIB": pxmMaMIB,
       "pxmMaTable": pxmMaTable,
       "pxmMaEntry": pxmMaEntry,
       "pxmMaMAName": pxmMaMAName,
       "pxmMaRMepAgeOutInterval": pxmMaRMepAgeOutInterval,
       "pxmMaMDAid": pxmMaMDAid,
       "pxmMaCcmInterval": pxmMaCcmInterval,
       "pxmMaMANameFormat": pxmMaMANameFormat,
       "pxmMaSenderIDTLV": pxmMaSenderIDTLV,
       "pxmMaMDName": pxmMaMDName,
       "pxmMaMDLevel": pxmMaMDLevel,
       "pxmMaConformance": pxmMaConformance,
       "pxmMaCompliances": pxmMaCompliances,
       "pxmMaCompliance": pxmMaCompliance,
       "pxmMaGroups": pxmMaGroups,
       "pxmMaGroup": pxmMaGroup}
)
