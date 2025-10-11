# SNMP MIB module (CPQRECOV-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/hp/CPQRECOV-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:36:34 2025
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

(compaq,
 cpqHoTrapFlags) = mibBuilder.importSymbols(
    "CPQHOST-MIB",
    "compaq",
    "cpqHoTrapFlags")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(sysName,) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysName")

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
 NotificationType,
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
    "NotificationType",
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


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CpqRecovery_ObjectIdentity = ObjectIdentity
cpqRecovery = _CpqRecovery_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 13)
)

# Managed Objects groups


# Notification objects

cpqRsPartnerFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13001)
)
cpqRsPartnerFailed.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"))
)
if mibBuilder.loadTexts:
    cpqRsPartnerFailed.setStatus(
        ""
    )

cpqRsStandbyCableFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13002)
)
cpqRsStandbyCableFailure.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"))
)
if mibBuilder.loadTexts:
    cpqRsStandbyCableFailure.setStatus(
        ""
    )

cpqRsStandbyFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13003)
)
cpqRsStandbyFailure.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"))
)
if mibBuilder.loadTexts:
    cpqRsStandbyFailure.setStatus(
        ""
    )

cpqRsOnlineCableFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13004)
)
cpqRsOnlineCableFailure.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"))
)
if mibBuilder.loadTexts:
    cpqRsOnlineCableFailure.setStatus(
        ""
    )

cpqRsFailoverFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 13005)
)
cpqRsFailoverFailed.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"))
)
if mibBuilder.loadTexts:
    cpqRsFailoverFailed.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CPQRECOV-MIB",
    **{"cpqRsPartnerFailed": cpqRsPartnerFailed,
       "cpqRsStandbyCableFailure": cpqRsStandbyCableFailure,
       "cpqRsStandbyFailure": cpqRsStandbyFailure,
       "cpqRsOnlineCableFailure": cpqRsOnlineCableFailure,
       "cpqRsFailoverFailed": cpqRsFailoverFailed,
       "cpqRecovery": cpqRecovery}
)
