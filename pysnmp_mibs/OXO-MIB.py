# SNMP MIB module (OXO-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/alcatel/OXO-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:08:34 2025
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

oxoMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 64, 4200, 1)
)
if mibBuilder.loadTexts:
    oxoMIB.setRevisions(
        ("2015-03-20 14:24",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class PhysicalAddress(TextualConvention, OctetString):
    status = "current"
    displayHint = "1d.1d.1d"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )
    fixed_length = 3



class EventSeverity(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("reserved", 0),
          ("critical", 1),
          ("major", 2),
          ("minor", 3),
          ("warning", 4),
          ("indeterminate", 5),
          ("clear", 6))
    )



class ActivationStatus(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 0),
          ("active", 1),
          ("unknown", 2))
    )



# MIB Managed Objects in the order of their OIDs

_Ale_ObjectIdentity = ObjectIdentity
ale = _Ale_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486)
)
_AleCommunication_ObjectIdentity = ObjectIdentity
aleCommunication = _AleCommunication_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 64)
)
_AleCommunicationOXO_ObjectIdentity = ObjectIdentity
aleCommunicationOXO = _AleCommunicationOXO_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 64, 4200)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "OXO-MIB",
    **{"PhysicalAddress": PhysicalAddress,
       "EventSeverity": EventSeverity,
       "ActivationStatus": ActivationStatus,
       "ale": ale,
       "aleCommunication": aleCommunication,
       "aleCommunicationOXO": aleCommunicationOXO,
       "oxoMIB": oxoMIB}
)
