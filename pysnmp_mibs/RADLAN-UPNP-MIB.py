# SNMP MIB module (RADLAN-UPNP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/radlan/RADLAN-UPNP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:11:21 2025
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

(rnd,) = mibBuilder.importSymbols(
    "RADLAN-MIB",
    "rnd")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

rlUPnP = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 89, 109)
)
if mibBuilder.loadTexts:
    rlUPnP.setRevisions(
        ("2006-03-26 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RlUPnPUniqueDeviceName_Type = DisplayString
_RlUPnPUniqueDeviceName_Object = MibScalar
rlUPnPUniqueDeviceName = _RlUPnPUniqueDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 89, 109, 1),
    _RlUPnPUniqueDeviceName_Type()
)
rlUPnPUniqueDeviceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlUPnPUniqueDeviceName.setStatus("current")


class _RlUPnPEnabling_Type(Integer32):
    """Custom type rlUPnPEnabling based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_RlUPnPEnabling_Type.__name__ = "Integer32"
_RlUPnPEnabling_Object = MibScalar
rlUPnPEnabling = _RlUPnPEnabling_Object(
    (1, 3, 6, 1, 4, 1, 89, 109, 2),
    _RlUPnPEnabling_Type()
)
rlUPnPEnabling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlUPnPEnabling.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RADLAN-UPNP-MIB",
    **{"rlUPnP": rlUPnP,
       "rlUPnPUniqueDeviceName": rlUPnPUniqueDeviceName,
       "rlUPnPEnabling": rlUPnPEnabling}
)
