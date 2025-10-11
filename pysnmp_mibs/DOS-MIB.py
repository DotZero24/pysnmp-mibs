# SNMP MIB module (DOS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/radware/DOS-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:15:34 2025
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

(rndErrorDesc,
 rndErrorSeverity,
 rsDOS) = mibBuilder.importSymbols(
    "RADWARE-MIB",
    "rndErrorDesc",
    "rndErrorSeverity",
    "rsDOS")

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



class _RsDOSSamplingRatio_Type(Integer32):
    """Custom type rsDOSSamplingRatio based on Integer32"""
    defaultValue = 100


_RsDOSSamplingRatio_Type.__name__ = "Integer32"
_RsDOSSamplingRatio_Object = MibScalar
rsDOSSamplingRatio = _RsDOSSamplingRatio_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 117, 1),
    _RsDOSSamplingRatio_Type()
)
rsDOSSamplingRatio.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsDOSSamplingRatio.setStatus("mandatory")


class _RsDOSSamplerOverloadMode_Type(Integer32):
    """Custom type rsDOSSamplerOverloadMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("forward", 1),
          ("discard", 2))
    )


_RsDOSSamplerOverloadMode_Type.__name__ = "Integer32"
_RsDOSSamplerOverloadMode_Object = MibScalar
rsDOSSamplerOverloadMode = _RsDOSSamplerOverloadMode_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 117, 2),
    _RsDOSSamplerOverloadMode_Type()
)
rsDOSSamplerOverloadMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsDOSSamplerOverloadMode.setStatus("mandatory")

# Managed Objects groups


# Notification objects

rsDOSOverloadTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 117, 0, 1)
)
rsDOSOverloadTrap.setObjects(
      *(("RADWARE-MIB", "rndErrorDesc"),
        ("RADWARE-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    rsDOSOverloadTrap.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DOS-MIB",
    **{"rsDOSOverloadTrap": rsDOSOverloadTrap,
       "rsDOSSamplingRatio": rsDOSSamplingRatio,
       "rsDOSSamplerOverloadMode": rsDOSSamplerOverloadMode}
)
