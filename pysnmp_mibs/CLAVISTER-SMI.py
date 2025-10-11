# SNMP MIB module (CLAVISTER-SMI) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/clavister/CLAVISTER-SMI
# Produced by pysmi-1.6.2 at Fri Oct 10 22:17:15 2025
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

clavisterSmiMibModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5089, 0)
)
if mibBuilder.loadTexts:
    clavisterSmiMibModule.setRevisions(
        ("2012-06-27 09:00",
         "2006-05-19 09:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Clavister_ObjectIdentity = ObjectIdentity
clavister = _Clavister_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5089)
)
_ClavisterOS_ObjectIdentity = ObjectIdentity
clavisterOS = _ClavisterOS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5089, 1)
)
_ClavisterOSTrap_ObjectIdentity = ObjectIdentity
clavisterOSTrap = _ClavisterOSTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5089, 1, 0)
)
_ClavisterOSTrapInfo_ObjectIdentity = ObjectIdentity
clavisterOSTrapInfo = _ClavisterOSTrapInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5089, 1, 1)
)
_ClavisterOSStats_ObjectIdentity = ObjectIdentity
clavisterOSStats = _ClavisterOSStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5089, 1, 2)
)
_ClavisterReg_ObjectIdentity = ObjectIdentity
clavisterReg = _ClavisterReg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5089, 2)
)
_ClavisterMibModules_ObjectIdentity = ObjectIdentity
clavisterMibModules = _ClavisterMibModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5089, 2, 1)
)
_ClavisterMibConfs_ObjectIdentity = ObjectIdentity
clavisterMibConfs = _ClavisterMibConfs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5089, 2, 2)
)
_ClavisterMibObjectGroups_ObjectIdentity = ObjectIdentity
clavisterMibObjectGroups = _ClavisterMibObjectGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5089, 2, 3)
)
_ClavisterSystem_ObjectIdentity = ObjectIdentity
clavisterSystem = _ClavisterSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5089, 3)
)
_ClavisterSystemTrap_ObjectIdentity = ObjectIdentity
clavisterSystemTrap = _ClavisterSystemTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5089, 3, 0)
)
_ClavisterSystemTrapInfo_ObjectIdentity = ObjectIdentity
clavisterSystemTrapInfo = _ClavisterSystemTrapInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5089, 3, 1)
)
_ClavisterSystemStats_ObjectIdentity = ObjectIdentity
clavisterSystemStats = _ClavisterSystemStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5089, 3, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CLAVISTER-SMI",
    **{"clavister": clavister,
       "clavisterSmiMibModule": clavisterSmiMibModule,
       "clavisterOS": clavisterOS,
       "clavisterOSTrap": clavisterOSTrap,
       "clavisterOSTrapInfo": clavisterOSTrapInfo,
       "clavisterOSStats": clavisterOSStats,
       "clavisterReg": clavisterReg,
       "clavisterMibModules": clavisterMibModules,
       "clavisterMibConfs": clavisterMibConfs,
       "clavisterMibObjectGroups": clavisterMibObjectGroups,
       "clavisterSystem": clavisterSystem,
       "clavisterSystemTrap": clavisterSystemTrap,
       "clavisterSystemTrapInfo": clavisterSystemTrapInfo,
       "clavisterSystemStats": clavisterSystemStats}
)
