# SNMP MIB module (SYNOLOGY-GPUINFO-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/synology/SYNOLOGY-GPUINFO-MIB
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

gpuInfo = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6574, 108)
)
if mibBuilder.loadTexts:
    gpuInfo.setRevisions(
        ("2018-12-03 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Synology_ObjectIdentity = ObjectIdentity
synology = _Synology_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6574)
)
_GpuInfoSupported_Type = Integer32
_GpuInfoSupported_Object = MibScalar
gpuInfoSupported = _GpuInfoSupported_Object(
    (1, 3, 6, 1, 4, 1, 6574, 108, 1),
    _GpuInfoSupported_Type()
)
gpuInfoSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpuInfoSupported.setStatus("current")
_GpuUtilization_Type = Integer32
_GpuUtilization_Object = MibScalar
gpuUtilization = _GpuUtilization_Object(
    (1, 3, 6, 1, 4, 1, 6574, 108, 2),
    _GpuUtilization_Type()
)
gpuUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpuUtilization.setStatus("current")
_GpuMemoryUtilization_Type = Integer32
_GpuMemoryUtilization_Object = MibScalar
gpuMemoryUtilization = _GpuMemoryUtilization_Object(
    (1, 3, 6, 1, 4, 1, 6574, 108, 3),
    _GpuMemoryUtilization_Type()
)
gpuMemoryUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpuMemoryUtilization.setStatus("current")
_GpuMemoryFree_Type = Integer32
_GpuMemoryFree_Object = MibScalar
gpuMemoryFree = _GpuMemoryFree_Object(
    (1, 3, 6, 1, 4, 1, 6574, 108, 4),
    _GpuMemoryFree_Type()
)
gpuMemoryFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpuMemoryFree.setStatus("current")
_GpuMemoryUsed_Type = Integer32
_GpuMemoryUsed_Object = MibScalar
gpuMemoryUsed = _GpuMemoryUsed_Object(
    (1, 3, 6, 1, 4, 1, 6574, 108, 5),
    _GpuMemoryUsed_Type()
)
gpuMemoryUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpuMemoryUsed.setStatus("current")
_GpuMemoryTotal_Type = Integer32
_GpuMemoryTotal_Object = MibScalar
gpuMemoryTotal = _GpuMemoryTotal_Object(
    (1, 3, 6, 1, 4, 1, 6574, 108, 6),
    _GpuMemoryTotal_Type()
)
gpuMemoryTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpuMemoryTotal.setStatus("current")
_GpuInfoConformance_ObjectIdentity = ObjectIdentity
gpuInfoConformance = _GpuInfoConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6574, 108, 7)
)
_GpuInfoCompliances_ObjectIdentity = ObjectIdentity
gpuInfoCompliances = _GpuInfoCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6574, 108, 7, 1)
)
_GpuInfoGroups_ObjectIdentity = ObjectIdentity
gpuInfoGroups = _GpuInfoGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6574, 108, 7, 2)
)

# Managed Objects groups

gpuInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6574, 108, 7, 2, 1)
)
gpuInfoGroup.setObjects(
      *(("SYNOLOGY-GPUINFO-MIB", "gpuInfoSupported"),
        ("SYNOLOGY-GPUINFO-MIB", "gpuUtilization"),
        ("SYNOLOGY-GPUINFO-MIB", "gpuMemoryUtilization"),
        ("SYNOLOGY-GPUINFO-MIB", "gpuMemoryFree"),
        ("SYNOLOGY-GPUINFO-MIB", "gpuMemoryUsed"),
        ("SYNOLOGY-GPUINFO-MIB", "gpuMemoryTotal"))
)
if mibBuilder.loadTexts:
    gpuInfoGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

gpuInfoCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6574, 108, 7, 1, 1)
)
gpuInfoCompliance.setObjects(
    ("SYNOLOGY-GPUINFO-MIB", "gpuInfoGroup")
)
if mibBuilder.loadTexts:
    gpuInfoCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SYNOLOGY-GPUINFO-MIB",
    **{"synology": synology,
       "gpuInfo": gpuInfo,
       "gpuInfoSupported": gpuInfoSupported,
       "gpuUtilization": gpuUtilization,
       "gpuMemoryUtilization": gpuMemoryUtilization,
       "gpuMemoryFree": gpuMemoryFree,
       "gpuMemoryUsed": gpuMemoryUsed,
       "gpuMemoryTotal": gpuMemoryTotal,
       "gpuInfoConformance": gpuInfoConformance,
       "gpuInfoCompliances": gpuInfoCompliances,
       "gpuInfoCompliance": gpuInfoCompliance,
       "gpuInfoGroups": gpuInfoGroups,
       "gpuInfoGroup": gpuInfoGroup}
)
