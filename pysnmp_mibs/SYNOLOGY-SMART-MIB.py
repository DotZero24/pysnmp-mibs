# SNMP MIB module (SYNOLOGY-SMART-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/synology/SYNOLOGY-SMART-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 18:58:23 2025
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

synologyDiskSMART = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6574, 5)
)
if mibBuilder.loadTexts:
    synologyDiskSMART.setRevisions(
        ("2016-05-05 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Synology_ObjectIdentity = ObjectIdentity
synology = _Synology_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6574)
)
_DiskSMARTTable_Object = MibTable
diskSMARTTable = _DiskSMARTTable_Object(
    (1, 3, 6, 1, 4, 1, 6574, 5, 1)
)
if mibBuilder.loadTexts:
    diskSMARTTable.setStatus("current")
_DiskSMARTEntry_Object = MibTableRow
diskSMARTEntry = _DiskSMARTEntry_Object(
    (1, 3, 6, 1, 4, 1, 6574, 5, 1, 1)
)
diskSMARTEntry.setIndexNames(
    (0, "SYNOLOGY-SMART-MIB", "diskSMARTInfoIndex"),
)
if mibBuilder.loadTexts:
    diskSMARTEntry.setStatus("current")


class _DiskSMARTInfoIndex_Type(Integer32):
    """Custom type diskSMARTInfoIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_DiskSMARTInfoIndex_Type.__name__ = "Integer32"
_DiskSMARTInfoIndex_Object = MibTableColumn
diskSMARTInfoIndex = _DiskSMARTInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 6574, 5, 1, 1, 1),
    _DiskSMARTInfoIndex_Type()
)
diskSMARTInfoIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    diskSMARTInfoIndex.setStatus("current")
_DiskSMARTInfoDevName_Type = OctetString
_DiskSMARTInfoDevName_Object = MibTableColumn
diskSMARTInfoDevName = _DiskSMARTInfoDevName_Object(
    (1, 3, 6, 1, 4, 1, 6574, 5, 1, 1, 2),
    _DiskSMARTInfoDevName_Type()
)
diskSMARTInfoDevName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskSMARTInfoDevName.setStatus("current")
_DiskSMARTAttrName_Type = OctetString
_DiskSMARTAttrName_Object = MibTableColumn
diskSMARTAttrName = _DiskSMARTAttrName_Object(
    (1, 3, 6, 1, 4, 1, 6574, 5, 1, 1, 3),
    _DiskSMARTAttrName_Type()
)
diskSMARTAttrName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskSMARTAttrName.setStatus("current")
_DiskSMARTAttrId_Type = Integer32
_DiskSMARTAttrId_Object = MibTableColumn
diskSMARTAttrId = _DiskSMARTAttrId_Object(
    (1, 3, 6, 1, 4, 1, 6574, 5, 1, 1, 4),
    _DiskSMARTAttrId_Type()
)
diskSMARTAttrId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskSMARTAttrId.setStatus("current")
_DiskSMARTAttrCurrent_Type = Integer32
_DiskSMARTAttrCurrent_Object = MibTableColumn
diskSMARTAttrCurrent = _DiskSMARTAttrCurrent_Object(
    (1, 3, 6, 1, 4, 1, 6574, 5, 1, 1, 5),
    _DiskSMARTAttrCurrent_Type()
)
diskSMARTAttrCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskSMARTAttrCurrent.setStatus("current")
_DiskSMARTAttrWorst_Type = Integer32
_DiskSMARTAttrWorst_Object = MibTableColumn
diskSMARTAttrWorst = _DiskSMARTAttrWorst_Object(
    (1, 3, 6, 1, 4, 1, 6574, 5, 1, 1, 6),
    _DiskSMARTAttrWorst_Type()
)
diskSMARTAttrWorst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskSMARTAttrWorst.setStatus("current")
_DiskSMARTAttrThreshold_Type = Integer32
_DiskSMARTAttrThreshold_Object = MibTableColumn
diskSMARTAttrThreshold = _DiskSMARTAttrThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6574, 5, 1, 1, 7),
    _DiskSMARTAttrThreshold_Type()
)
diskSMARTAttrThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskSMARTAttrThreshold.setStatus("current")
_DiskSMARTAttrRaw_Type = Integer32
_DiskSMARTAttrRaw_Object = MibTableColumn
diskSMARTAttrRaw = _DiskSMARTAttrRaw_Object(
    (1, 3, 6, 1, 4, 1, 6574, 5, 1, 1, 8),
    _DiskSMARTAttrRaw_Type()
)
diskSMARTAttrRaw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskSMARTAttrRaw.setStatus("current")
_DiskSMARTAttrStatus_Type = OctetString
_DiskSMARTAttrStatus_Object = MibTableColumn
diskSMARTAttrStatus = _DiskSMARTAttrStatus_Object(
    (1, 3, 6, 1, 4, 1, 6574, 5, 1, 1, 9),
    _DiskSMARTAttrStatus_Type()
)
diskSMARTAttrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskSMARTAttrStatus.setStatus("current")
_DiskSMARTAttrRaw64_Type = Counter64
_DiskSMARTAttrRaw64_Object = MibTableColumn
diskSMARTAttrRaw64 = _DiskSMARTAttrRaw64_Object(
    (1, 3, 6, 1, 4, 1, 6574, 5, 1, 1, 10),
    _DiskSMARTAttrRaw64_Type()
)
diskSMARTAttrRaw64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskSMARTAttrRaw64.setStatus("current")
_SynologyDiskSMARTConformance_ObjectIdentity = ObjectIdentity
synologyDiskSMARTConformance = _SynologyDiskSMARTConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6574, 5, 2)
)
_SynologyDiskSMARTCompliances_ObjectIdentity = ObjectIdentity
synologyDiskSMARTCompliances = _SynologyDiskSMARTCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6574, 5, 2, 1)
)
_SynologyDiskSMARTGroups_ObjectIdentity = ObjectIdentity
synologyDiskSMARTGroups = _SynologyDiskSMARTGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6574, 5, 2, 2)
)

# Managed Objects groups

synologyDiskSMARTGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6574, 5, 2, 2, 1)
)
synologyDiskSMARTGroup.setObjects(
      *(("SYNOLOGY-SMART-MIB", "diskSMARTInfoDevName"),
        ("SYNOLOGY-SMART-MIB", "diskSMARTAttrName"),
        ("SYNOLOGY-SMART-MIB", "diskSMARTAttrId"),
        ("SYNOLOGY-SMART-MIB", "diskSMARTAttrCurrent"),
        ("SYNOLOGY-SMART-MIB", "diskSMARTAttrWorst"),
        ("SYNOLOGY-SMART-MIB", "diskSMARTAttrThreshold"),
        ("SYNOLOGY-SMART-MIB", "diskSMARTAttrRaw"),
        ("SYNOLOGY-SMART-MIB", "diskSMARTAttrStatus"),
        ("SYNOLOGY-SMART-MIB", "diskSMARTAttrRaw64"))
)
if mibBuilder.loadTexts:
    synologyDiskSMARTGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

synologyDiskSMARTCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6574, 5, 2, 1, 1)
)
synologyDiskSMARTCompliance.setObjects(
    ("SYNOLOGY-SMART-MIB", "synologyDiskSMARTGroup")
)
if mibBuilder.loadTexts:
    synologyDiskSMARTCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SYNOLOGY-SMART-MIB",
    **{"synology": synology,
       "synologyDiskSMART": synologyDiskSMART,
       "diskSMARTTable": diskSMARTTable,
       "diskSMARTEntry": diskSMARTEntry,
       "diskSMARTInfoIndex": diskSMARTInfoIndex,
       "diskSMARTInfoDevName": diskSMARTInfoDevName,
       "diskSMARTAttrName": diskSMARTAttrName,
       "diskSMARTAttrId": diskSMARTAttrId,
       "diskSMARTAttrCurrent": diskSMARTAttrCurrent,
       "diskSMARTAttrWorst": diskSMARTAttrWorst,
       "diskSMARTAttrThreshold": diskSMARTAttrThreshold,
       "diskSMARTAttrRaw": diskSMARTAttrRaw,
       "diskSMARTAttrStatus": diskSMARTAttrStatus,
       "diskSMARTAttrRaw64": diskSMARTAttrRaw64,
       "synologyDiskSMARTConformance": synologyDiskSMARTConformance,
       "synologyDiskSMARTCompliances": synologyDiskSMARTCompliances,
       "synologyDiskSMARTCompliance": synologyDiskSMARTCompliance,
       "synologyDiskSMARTGroups": synologyDiskSMARTGroups,
       "synologyDiskSMARTGroup": synologyDiskSMARTGroup}
)
