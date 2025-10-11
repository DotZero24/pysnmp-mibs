# SNMP MIB module (MX-BOOT-BEHAVIOR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/media5/MX-BOOT-BEHAVIOR-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:05:35 2025
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

(mediatrixExperimental,) = mibBuilder.importSymbols(
    "MX-SMI",
    "mediatrixExperimental")

(MxEnableState,) = mibBuilder.importSymbols(
    "MX-TC",
    "MxEnableState")

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

bootBehaviorMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 99, 70)
)
if mibBuilder.loadTexts:
    bootBehaviorMIB.setRevisions(
        ("2004-08-12 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_BootBehaviorMIBObjects_ObjectIdentity = ObjectIdentity
bootBehaviorMIBObjects = _BootBehaviorMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 99, 70, 1)
)


class _CheckTcpIpStackForSuccessfulBoot_Type(MxEnableState):
    """Custom type checkTcpIpStackForSuccessfulBoot based on MxEnableState"""
    defaultValue = 1


_CheckTcpIpStackForSuccessfulBoot_Type.__name__ = "MxEnableState"
_CheckTcpIpStackForSuccessfulBoot_Object = MibScalar
checkTcpIpStackForSuccessfulBoot = _CheckTcpIpStackForSuccessfulBoot_Object(
    (1, 3, 6, 1, 4, 1, 4935, 99, 70, 1, 1),
    _CheckTcpIpStackForSuccessfulBoot_Type()
)
checkTcpIpStackForSuccessfulBoot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    checkTcpIpStackForSuccessfulBoot.setStatus("current")
_BootBehaviorConformance_ObjectIdentity = ObjectIdentity
bootBehaviorConformance = _BootBehaviorConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 99, 70, 2)
)
_BootBehaviorCompliances_ObjectIdentity = ObjectIdentity
bootBehaviorCompliances = _BootBehaviorCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 99, 70, 2, 1)
)
_BootBehaviorGroups_ObjectIdentity = ObjectIdentity
bootBehaviorGroups = _BootBehaviorGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 99, 70, 2, 2)
)

# Managed Objects groups

bootBehaviorGroupVer1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4935, 99, 70, 2, 2, 10)
)
bootBehaviorGroupVer1.setObjects(
    ("MX-BOOT-BEHAVIOR-MIB", "checkTcpIpStackForSuccessfulBoot")
)
if mibBuilder.loadTexts:
    bootBehaviorGroupVer1.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

bootBehaviorComplVer1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4935, 99, 70, 2, 1, 10)
)
bootBehaviorComplVer1.setObjects(
    ("MX-BOOT-BEHAVIOR-MIB", "bootBehaviorGroupVer1")
)
if mibBuilder.loadTexts:
    bootBehaviorComplVer1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MX-BOOT-BEHAVIOR-MIB",
    **{"bootBehaviorMIB": bootBehaviorMIB,
       "bootBehaviorMIBObjects": bootBehaviorMIBObjects,
       "checkTcpIpStackForSuccessfulBoot": checkTcpIpStackForSuccessfulBoot,
       "bootBehaviorConformance": bootBehaviorConformance,
       "bootBehaviorCompliances": bootBehaviorCompliances,
       "bootBehaviorComplVer1": bootBehaviorComplVer1,
       "bootBehaviorGroups": bootBehaviorGroups,
       "bootBehaviorGroupVer1": bootBehaviorGroupVer1}
)
