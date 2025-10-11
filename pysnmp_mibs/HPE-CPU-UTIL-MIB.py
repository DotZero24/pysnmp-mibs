# SNMP MIB module (HPE-CPU-UTIL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/hp/HPE-CPU-UTIL-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:39:13 2025
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

(hpVCSE_40Gb_F8_Module,) = mibBuilder.importSymbols(
    "HPSVRMGMT-OID",
    "hpVCSE-40Gb-F8-Module")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

hpeCpuUtilMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 8, 1, 4130)
)
if mibBuilder.loadTexts:
    hpeCpuUtilMIB.setRevisions(
        ("2019-12-19 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HpeSynergyCpuUtilMIBObjects_ObjectIdentity = ObjectIdentity
hpeSynergyCpuUtilMIBObjects = _HpeSynergyCpuUtilMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 8, 1)
)
_HpeCpuUtilConfig_ObjectIdentity = ObjectIdentity
hpeCpuUtilConfig = _HpeCpuUtilConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 8, 1, 4130, 1)
)


class _HpeSwitchMaxCPUThreshold_Type(Integer32):
    """Custom type hpeSwitchMaxCPUThreshold based on Integer32"""
    defaultValue = 95

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_HpeSwitchMaxCPUThreshold_Type.__name__ = "Integer32"
_HpeSwitchMaxCPUThreshold_Object = MibScalar
hpeSwitchMaxCPUThreshold = _HpeSwitchMaxCPUThreshold_Object(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 8, 1, 4130, 1, 1),
    _HpeSwitchMaxCPUThreshold_Type()
)
hpeSwitchMaxCPUThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpeSwitchMaxCPUThreshold.setStatus("current")


class _HpeSwitchMinCPUThreshold_Type(Integer32):
    """Custom type hpeSwitchMinCPUThreshold based on Integer32"""
    defaultValue = 75

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_HpeSwitchMinCPUThreshold_Type.__name__ = "Integer32"
_HpeSwitchMinCPUThreshold_Object = MibScalar
hpeSwitchMinCPUThreshold = _HpeSwitchMinCPUThreshold_Object(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 8, 1, 4130, 1, 2),
    _HpeSwitchMinCPUThreshold_Type()
)
hpeSwitchMinCPUThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpeSwitchMinCPUThreshold.setStatus("current")
_HpeCpuUtiStatus_ObjectIdentity = ObjectIdentity
hpeCpuUtiStatus = _HpeCpuUtiStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 8, 1, 4130, 2)
)
_HpeSwitchAverageCPUUtilization_Type = Integer32
_HpeSwitchAverageCPUUtilization_Object = MibScalar
hpeSwitchAverageCPUUtilization = _HpeSwitchAverageCPUUtilization_Object(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 8, 1, 4130, 2, 1),
    _HpeSwitchAverageCPUUtilization_Type()
)
hpeSwitchAverageCPUUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpeSwitchAverageCPUUtilization.setStatus("current")
if mibBuilder.loadTexts:
    hpeSwitchAverageCPUUtilization.setUnits("percentage")
_HpeCpuUtilTraps_ObjectIdentity = ObjectIdentity
hpeCpuUtilTraps = _HpeCpuUtilTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 8, 1, 4130, 3)
)

# Managed Objects groups


# Notification objects

hpeTrapMaxCPUThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 8, 1, 4130, 3, 1)
)
hpeTrapMaxCPUThreshold.setObjects(
      *(("HPE-CPU-UTIL-MIB", "hpeSwitchMaxCPUThreshold"),
        ("HPE-CPU-UTIL-MIB", "hpeSwitchAverageCPUUtilization"))
)
if mibBuilder.loadTexts:
    hpeTrapMaxCPUThreshold.setStatus(
        "current"
    )

hpeTrapMinCPUThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 8, 1, 4130, 3, 2)
)
hpeTrapMinCPUThreshold.setObjects(
      *(("HPE-CPU-UTIL-MIB", "hpeSwitchMinCPUThreshold"),
        ("HPE-CPU-UTIL-MIB", "hpeSwitchAverageCPUUtilization"))
)
if mibBuilder.loadTexts:
    hpeTrapMinCPUThreshold.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPE-CPU-UTIL-MIB",
    **{"hpeSynergyCpuUtilMIBObjects": hpeSynergyCpuUtilMIBObjects,
       "hpeCpuUtilMIB": hpeCpuUtilMIB,
       "hpeCpuUtilConfig": hpeCpuUtilConfig,
       "hpeSwitchMaxCPUThreshold": hpeSwitchMaxCPUThreshold,
       "hpeSwitchMinCPUThreshold": hpeSwitchMinCPUThreshold,
       "hpeCpuUtiStatus": hpeCpuUtiStatus,
       "hpeSwitchAverageCPUUtilization": hpeSwitchAverageCPUUtilization,
       "hpeCpuUtilTraps": hpeCpuUtilTraps,
       "hpeTrapMaxCPUThreshold": hpeTrapMaxCPUThreshold,
       "hpeTrapMinCPUThreshold": hpeTrapMinCPUThreshold}
)
