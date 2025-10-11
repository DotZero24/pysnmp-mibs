# SNMP MIB module (ELTEX-FASTPATH-TRAPS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/eltex/ELTEX-FASTPATH-TRAPS-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:51:30 2025
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

(eltMesFastpath,) = mibBuilder.importSymbols(
    "ELTEX-MES-FASTPATH-MIB",
    "eltMesFastpath")

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

eltFastpathTrapsMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 103, 4)
)
if mibBuilder.loadTexts:
    eltFastpathTrapsMIB.setRevisions(
        ("2017-10-06 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_EfpTrapsObjects_ObjectIdentity = ObjectIdentity
efpTrapsObjects = _EfpTrapsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 103, 4, 1)
)


class _EfpGeneralTestTrapStatus_Type(Integer32):
    """Custom type efpGeneralTestTrapStatus based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("success", 2),
          ("failure", 3),
          ("uninitialized", 4))
    )


_EfpGeneralTestTrapStatus_Type.__name__ = "Integer32"
_EfpGeneralTestTrapStatus_Object = MibScalar
efpGeneralTestTrapStatus = _EfpGeneralTestTrapStatus_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 103, 4, 1, 1),
    _EfpGeneralTestTrapStatus_Type()
)
efpGeneralTestTrapStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    efpGeneralTestTrapStatus.setStatus("current")
_EfpTrapsNotifications_ObjectIdentity = ObjectIdentity
efpTrapsNotifications = _EfpTrapsNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 103, 4, 2)
)
_EfpTrapsNotificationsPrefix_ObjectIdentity = ObjectIdentity
efpTrapsNotificationsPrefix = _EfpTrapsNotificationsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 103, 4, 2, 0)
)
_EfpTrapsConformance_ObjectIdentity = ObjectIdentity
efpTrapsConformance = _EfpTrapsConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 103, 4, 3)
)

# Managed Objects groups


# Notification objects

efpWriteMemoryTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 1, 103, 4, 2, 0, 1)
)
if mibBuilder.loadTexts:
    efpWriteMemoryTrap.setStatus(
        "current"
    )

efpCopyFinishedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 1, 103, 4, 2, 0, 2)
)
if mibBuilder.loadTexts:
    efpCopyFinishedTrap.setStatus(
        "current"
    )

efpCopyFailedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 1, 103, 4, 2, 0, 3)
)
if mibBuilder.loadTexts:
    efpCopyFailedTrap.setStatus(
        "current"
    )

efpGeneralTestTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 1, 103, 4, 2, 0, 4)
)
if mibBuilder.loadTexts:
    efpGeneralTestTrap.setStatus(
        "current"
    )

efpConfigurationReloadedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 1, 103, 4, 2, 0, 5)
)
if mibBuilder.loadTexts:
    efpConfigurationReloadedTrap.setStatus(
        "current"
    )

efpConfigurationReloadFailedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 1, 103, 4, 2, 0, 6)
)
if mibBuilder.loadTexts:
    efpConfigurationReloadFailedTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ELTEX-FASTPATH-TRAPS-MIB",
    **{"eltFastpathTrapsMIB": eltFastpathTrapsMIB,
       "efpTrapsObjects": efpTrapsObjects,
       "efpGeneralTestTrapStatus": efpGeneralTestTrapStatus,
       "efpTrapsNotifications": efpTrapsNotifications,
       "efpTrapsNotificationsPrefix": efpTrapsNotificationsPrefix,
       "efpWriteMemoryTrap": efpWriteMemoryTrap,
       "efpCopyFinishedTrap": efpCopyFinishedTrap,
       "efpCopyFailedTrap": efpCopyFailedTrap,
       "efpGeneralTestTrap": efpGeneralTestTrap,
       "efpConfigurationReloadedTrap": efpConfigurationReloadedTrap,
       "efpConfigurationReloadFailedTrap": efpConfigurationReloadFailedTrap,
       "efpTrapsConformance": efpTrapsConformance}
)
