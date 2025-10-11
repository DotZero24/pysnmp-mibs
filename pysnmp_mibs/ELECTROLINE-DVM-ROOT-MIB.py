# SNMP MIB module (ELECTROLINE-DVM-ROOT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/electroline/ELECTROLINE-DVM-ROOT-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:07:09 2025
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

(electrolineHardwareProducts,) = mibBuilder.importSymbols(
    "ELECTROLINE-GLOBAL-REG",
    "electrolineHardwareProducts")

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

electrolineDVM = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 3)
)
if mibBuilder.loadTexts:
    electrolineDVM.setRevisions(
        ("2003-03-20 00:00",)
    )


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

_DvmInventory_ObjectIdentity = ObjectIdentity
dvmInventory = _DvmInventory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 3, 1)
)
if mibBuilder.loadTexts:
    dvmInventory.setStatus("current")
_DvmConfiguration_ObjectIdentity = ObjectIdentity
dvmConfiguration = _DvmConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 3, 2)
)
if mibBuilder.loadTexts:
    dvmConfiguration.setStatus("current")
_DvmStatus_ObjectIdentity = ObjectIdentity
dvmStatus = _DvmStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 3, 3)
)
if mibBuilder.loadTexts:
    dvmStatus.setStatus("current")
_DvmPrivate_ObjectIdentity = ObjectIdentity
dvmPrivate = _DvmPrivate_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 3, 4)
)
if mibBuilder.loadTexts:
    dvmPrivate.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ELECTROLINE-DVM-ROOT-MIB",
    **{"ModulationType": ModulationType,
       "electrolineDVM": electrolineDVM,
       "dvmInventory": dvmInventory,
       "dvmConfiguration": dvmConfiguration,
       "dvmStatus": dvmStatus,
       "dvmPrivate": dvmPrivate}
)
