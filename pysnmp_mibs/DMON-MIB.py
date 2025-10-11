# SNMP MIB module (DMON-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/electroline/DMON-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:07:00 2025
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

(electrolineCoRoot,) = mibBuilder.importSymbols(
    "ELECTROLINE-GLOBAL-REG",
    "electrolineCoRoot")

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


# Types definitions


# TEXTUAL-CONVENTIONS



class ModulationType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("unknown", -1),
          ("qam16", 0),
          ("qam64", 1),
          ("qam256", 2),
          ("qam1024", 3),
          ("qam32", 4),
          ("qam128", 5),
          ("qpsk", 6))
    )



# MIB Managed Objects in the order of their OIDs

_DmonMib_ObjectIdentity = ObjectIdentity
dmonMib = _DmonMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5802, 999999)
)
_DmonPhyGroup_ObjectIdentity = ObjectIdentity
dmonPhyGroup = _DmonPhyGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5802, 999999, 1)
)
_DmonCommonGroup_ObjectIdentity = ObjectIdentity
dmonCommonGroup = _DmonCommonGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5802, 999999, 2)
)
_DmonDsgMcastRedirectGroup_ObjectIdentity = ObjectIdentity
dmonDsgMcastRedirectGroup = _DmonDsgMcastRedirectGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5802, 999999, 3)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DMON-MIB",
    **{"ModulationType": ModulationType,
       "dmonMib": dmonMib,
       "dmonPhyGroup": dmonPhyGroup,
       "dmonCommonGroup": dmonCommonGroup,
       "dmonDsgMcastRedirectGroup": dmonDsgMcastRedirectGroup}
)
