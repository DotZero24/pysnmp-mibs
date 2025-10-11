# SNMP MIB module (SYNERGY100G-HPE-CPU-UTIL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/hp/SYNERGY100G-HPE-CPU-UTIL-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:40:42 2025
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

(hpVCSE_100Gb_F32_Module,) = mibBuilder.importSymbols(
    "HPSVRMGMT-OID",
    "hpVCSE-100Gb-F32-Module")

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

syn100GhpeCpuUtilMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 9, 1, 4130)
)
if mibBuilder.loadTexts:
    syn100GhpeCpuUtilMIB.setRevisions(
        ("2019-12-19 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Syn100GhpeSynergyCpuUtilMIBObjects_ObjectIdentity = ObjectIdentity
syn100GhpeSynergyCpuUtilMIBObjects = _Syn100GhpeSynergyCpuUtilMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 9, 1)
)
_Syn100GhpeCpuUtilConfig_ObjectIdentity = ObjectIdentity
syn100GhpeCpuUtilConfig = _Syn100GhpeCpuUtilConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 9, 1, 4130, 1)
)


class _Syn100GhpeSwitchMaxCPUThreshold_Type(Integer32):
    """Custom type syn100GhpeSwitchMaxCPUThreshold based on Integer32"""
    defaultValue = 95

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_Syn100GhpeSwitchMaxCPUThreshold_Type.__name__ = "Integer32"
_Syn100GhpeSwitchMaxCPUThreshold_Object = MibScalar
syn100GhpeSwitchMaxCPUThreshold = _Syn100GhpeSwitchMaxCPUThreshold_Object(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 9, 1, 4130, 1, 1),
    _Syn100GhpeSwitchMaxCPUThreshold_Type()
)
syn100GhpeSwitchMaxCPUThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syn100GhpeSwitchMaxCPUThreshold.setStatus("current")


class _Syn100GhpeSwitchMinCPUThreshold_Type(Integer32):
    """Custom type syn100GhpeSwitchMinCPUThreshold based on Integer32"""
    defaultValue = 75

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_Syn100GhpeSwitchMinCPUThreshold_Type.__name__ = "Integer32"
_Syn100GhpeSwitchMinCPUThreshold_Object = MibScalar
syn100GhpeSwitchMinCPUThreshold = _Syn100GhpeSwitchMinCPUThreshold_Object(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 9, 1, 4130, 1, 2),
    _Syn100GhpeSwitchMinCPUThreshold_Type()
)
syn100GhpeSwitchMinCPUThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syn100GhpeSwitchMinCPUThreshold.setStatus("current")
_Syn100GhpeCpuUtiStatus_ObjectIdentity = ObjectIdentity
syn100GhpeCpuUtiStatus = _Syn100GhpeCpuUtiStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 9, 1, 4130, 2)
)
_Syn100GhpeSwitchAverageCPUUtilization_Type = Integer32
_Syn100GhpeSwitchAverageCPUUtilization_Object = MibScalar
syn100GhpeSwitchAverageCPUUtilization = _Syn100GhpeSwitchAverageCPUUtilization_Object(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 9, 1, 4130, 2, 1),
    _Syn100GhpeSwitchAverageCPUUtilization_Type()
)
syn100GhpeSwitchAverageCPUUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syn100GhpeSwitchAverageCPUUtilization.setStatus("current")
if mibBuilder.loadTexts:
    syn100GhpeSwitchAverageCPUUtilization.setUnits("percentage")
_Syn100GhpeCpuUtilTraps_ObjectIdentity = ObjectIdentity
syn100GhpeCpuUtilTraps = _Syn100GhpeCpuUtilTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 9, 1, 4130, 3)
)

# Managed Objects groups


# Notification objects

syn100GhpeTrapMaxCPUThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 9, 1, 4130, 3, 1)
)
syn100GhpeTrapMaxCPUThreshold.setObjects(
      *(("SYNERGY100G-HPE-CPU-UTIL-MIB", "syn100GhpeSwitchMaxCPUThreshold"),
        ("SYNERGY100G-HPE-CPU-UTIL-MIB", "syn100GhpeSwitchAverageCPUUtilization"))
)
if mibBuilder.loadTexts:
    syn100GhpeTrapMaxCPUThreshold.setStatus(
        "current"
    )

syn100GhpeTrapMinCPUThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 9, 1, 4130, 3, 2)
)
syn100GhpeTrapMinCPUThreshold.setObjects(
      *(("SYNERGY100G-HPE-CPU-UTIL-MIB", "syn100GhpeSwitchMinCPUThreshold"),
        ("SYNERGY100G-HPE-CPU-UTIL-MIB", "syn100GhpeSwitchAverageCPUUtilization"))
)
if mibBuilder.loadTexts:
    syn100GhpeTrapMinCPUThreshold.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SYNERGY100G-HPE-CPU-UTIL-MIB",
    **{"syn100GhpeSynergyCpuUtilMIBObjects": syn100GhpeSynergyCpuUtilMIBObjects,
       "syn100GhpeCpuUtilMIB": syn100GhpeCpuUtilMIB,
       "syn100GhpeCpuUtilConfig": syn100GhpeCpuUtilConfig,
       "syn100GhpeSwitchMaxCPUThreshold": syn100GhpeSwitchMaxCPUThreshold,
       "syn100GhpeSwitchMinCPUThreshold": syn100GhpeSwitchMinCPUThreshold,
       "syn100GhpeCpuUtiStatus": syn100GhpeCpuUtiStatus,
       "syn100GhpeSwitchAverageCPUUtilization": syn100GhpeSwitchAverageCPUUtilization,
       "syn100GhpeCpuUtilTraps": syn100GhpeCpuUtilTraps,
       "syn100GhpeTrapMaxCPUThreshold": syn100GhpeTrapMaxCPUThreshold,
       "syn100GhpeTrapMinCPUThreshold": syn100GhpeTrapMinCPUThreshold}
)
