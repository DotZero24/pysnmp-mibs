# SNMP MIB module (CPQSANAPP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/hp/CPQSANAPP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:34:06 2025
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

_Compaq_ObjectIdentity = ObjectIdentity
compaq = _Compaq_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232)
)
_CpqSanAppliance_ObjectIdentity = ObjectIdentity
cpqSanAppliance = _CpqSanAppliance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 151)
)
_ResourceMonitor_ObjectIdentity = ObjectIdentity
resourceMonitor = _ResourceMonitor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 151, 11)
)


class _SwSystemName_Type(DisplayString):
    """Custom type swSystemName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(255, 255),
    )
    fixed_length = 255


_SwSystemName_Type.__name__ = "DisplayString"
_SwSystemName_Object = MibScalar
swSystemName = _SwSystemName_Object(
    (1, 3, 6, 1, 4, 1, 232, 151, 11, 1),
    _SwSystemName_Type()
)
swSystemName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swSystemName.setStatus("mandatory")


class _SwSystemType_Type(Integer32):
    """Custom type swSystemType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("hsg80", 1),
          ("switch", 2),
          ("appliance", 3))
    )


_SwSystemType_Type.__name__ = "Integer32"
_SwSystemType_Object = MibScalar
swSystemType = _SwSystemType_Object(
    (1, 3, 6, 1, 4, 1, 232, 151, 11, 2),
    _SwSystemType_Type()
)
swSystemType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swSystemType.setStatus("mandatory")


class _SwEventName_Type(DisplayString):
    """Custom type swEventName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(255, 255),
    )
    fixed_length = 255


_SwEventName_Type.__name__ = "DisplayString"
_SwEventName_Object = MibScalar
swEventName = _SwEventName_Object(
    (1, 3, 6, 1, 4, 1, 232, 151, 11, 3),
    _SwEventName_Type()
)
swEventName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swEventName.setStatus("mandatory")


class _SwFailure_Type(DisplayString):
    """Custom type swFailure based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(255, 255),
    )
    fixed_length = 255


_SwFailure_Type.__name__ = "DisplayString"
_SwFailure_Object = MibScalar
swFailure = _SwFailure_Object(
    (1, 3, 6, 1, 4, 1, 232, 151, 11, 4),
    _SwFailure_Type()
)
swFailure.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swFailure.setStatus("mandatory")
_SwSequence_Type = Integer32
_SwSequence_Object = MibScalar
swSequence = _SwSequence_Object(
    (1, 3, 6, 1, 4, 1, 232, 151, 11, 5),
    _SwSequence_Type()
)
swSequence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swSequence.setStatus("mandatory")

# Managed Objects groups


# Notification objects

swFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 151, 11, 0, 1)
)
swFailureTrap.setObjects(
      *(("CPQSANAPP-MIB", "swSystemName"),
        ("CPQSANAPP-MIB", "swSystemType"),
        ("CPQSANAPP-MIB", "swEventName"),
        ("CPQSANAPP-MIB", "swFailure"),
        ("CPQSANAPP-MIB", "swSequence"))
)
if mibBuilder.loadTexts:
    swFailureTrap.setStatus(
        ""
    )

swWarningTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 151, 11, 0, 2)
)
swWarningTrap.setObjects(
      *(("CPQSANAPP-MIB", "swSystemName"),
        ("CPQSANAPP-MIB", "swSystemType"),
        ("CPQSANAPP-MIB", "swEventName"),
        ("CPQSANAPP-MIB", "swFailure"),
        ("CPQSANAPP-MIB", "swSequence"))
)
if mibBuilder.loadTexts:
    swWarningTrap.setStatus(
        ""
    )

swInformationTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 151, 11, 0, 4)
)
swInformationTrap.setObjects(
      *(("CPQSANAPP-MIB", "swSystemName"),
        ("CPQSANAPP-MIB", "swSystemType"),
        ("CPQSANAPP-MIB", "swEventName"),
        ("CPQSANAPP-MIB", "swFailure"),
        ("CPQSANAPP-MIB", "swSequence"))
)
if mibBuilder.loadTexts:
    swInformationTrap.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CPQSANAPP-MIB",
    **{"compaq": compaq,
       "cpqSanAppliance": cpqSanAppliance,
       "resourceMonitor": resourceMonitor,
       "swFailureTrap": swFailureTrap,
       "swWarningTrap": swWarningTrap,
       "swInformationTrap": swInformationTrap,
       "swSystemName": swSystemName,
       "swSystemType": swSystemType,
       "swEventName": swEventName,
       "swFailure": swFailure,
       "swSequence": swSequence}
)
