# SNMP MIB module (ARICENT-IPV6-MLD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/aricent/ARICENT-IPV6-MLD-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:42:52 2025
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

futuremld = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 70)
)
if mibBuilder.loadTexts:
    futuremld.setRevisions(
        ("2012-09-05 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FsmldScalars_ObjectIdentity = ObjectIdentity
fsmldScalars = _FsmldScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 70, 1)
)
_FsmldNoOfCacheEntries_Type = Unsigned32
_FsmldNoOfCacheEntries_Object = MibScalar
fsmldNoOfCacheEntries = _FsmldNoOfCacheEntries_Object(
    (1, 3, 6, 1, 4, 1, 2076, 70, 1, 1),
    _FsmldNoOfCacheEntries_Type()
)
fsmldNoOfCacheEntries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsmldNoOfCacheEntries.setStatus("deprecated")
_FsmldNoOfRoutingProtocols_Type = Unsigned32
_FsmldNoOfRoutingProtocols_Object = MibScalar
fsmldNoOfRoutingProtocols = _FsmldNoOfRoutingProtocols_Object(
    (1, 3, 6, 1, 4, 1, 2076, 70, 1, 2),
    _FsmldNoOfRoutingProtocols_Type()
)
fsmldNoOfRoutingProtocols.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsmldNoOfRoutingProtocols.setStatus("deprecated")
_FsmldTraceDebug_Type = Unsigned32
_FsmldTraceDebug_Object = MibScalar
fsmldTraceDebug = _FsmldTraceDebug_Object(
    (1, 3, 6, 1, 4, 1, 2076, 70, 1, 3),
    _FsmldTraceDebug_Type()
)
fsmldTraceDebug.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsmldTraceDebug.setStatus("current")
_FsmldDebugLevel_Type = Unsigned32
_FsmldDebugLevel_Object = MibScalar
fsmldDebugLevel = _FsmldDebugLevel_Object(
    (1, 3, 6, 1, 4, 1, 2076, 70, 1, 4),
    _FsmldDebugLevel_Type()
)
fsmldDebugLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsmldDebugLevel.setStatus("current")


class _FsmldMode_Type(Integer32):
    """Custom type fsmldMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("mldrouter", 1),
          ("mldhost", 2),
          ("mldrouterhost", 3))
    )


_FsmldMode_Type.__name__ = "Integer32"
_FsmldMode_Object = MibScalar
fsmldMode = _FsmldMode_Object(
    (1, 3, 6, 1, 4, 1, 2076, 70, 1, 5),
    _FsmldMode_Type()
)
fsmldMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsmldMode.setStatus("current")


class _FsmldProtocolUpDown_Type(Integer32):
    """Custom type fsmldProtocolUpDown based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mldinit", 1),
          ("mldshutdown", 2))
    )


_FsmldProtocolUpDown_Type.__name__ = "Integer32"
_FsmldProtocolUpDown_Object = MibScalar
fsmldProtocolUpDown = _FsmldProtocolUpDown_Object(
    (1, 3, 6, 1, 4, 1, 2076, 70, 1, 6),
    _FsmldProtocolUpDown_Type()
)
fsmldProtocolUpDown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsmldProtocolUpDown.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ARICENT-IPV6-MLD-MIB",
    **{"futuremld": futuremld,
       "fsmldScalars": fsmldScalars,
       "fsmldNoOfCacheEntries": fsmldNoOfCacheEntries,
       "fsmldNoOfRoutingProtocols": fsmldNoOfRoutingProtocols,
       "fsmldTraceDebug": fsmldTraceDebug,
       "fsmldDebugLevel": fsmldDebugLevel,
       "fsmldMode": fsmldMode,
       "fsmldProtocolUpDown": fsmldProtocolUpDown}
)
