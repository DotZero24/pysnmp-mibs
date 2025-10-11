# SNMP MIB module (ARICENT-FIPS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/aricent/ARICENT-FIPS-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:44:58 2025
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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

fsFips = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 29601, 2, 63)
)
if mibBuilder.loadTexts:
    fsFips.setRevisions(
        ("2012-09-05 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FsFipsConfigurations_ObjectIdentity = ObjectIdentity
fsFipsConfigurations = _FsFipsConfigurations_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29601, 2, 63, 1)
)


class _FsFipsOperMode_Type(Integer32):
    """Custom type fsFipsOperMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fips", 1),
          ("nonfips", 2))
    )


_FsFipsOperMode_Type.__name__ = "Integer32"
_FsFipsOperMode_Object = MibScalar
fsFipsOperMode = _FsFipsOperMode_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 63, 1, 1),
    _FsFipsOperMode_Type()
)
fsFipsOperMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsFipsOperMode.setStatus("current")


class _FsFipsTestAlgo_Type(Integer32):
    """Custom type fsFipsTestAlgo based on Integer32"""
    defaultValue = 0


_FsFipsTestAlgo_Type.__name__ = "Integer32"
_FsFipsTestAlgo_Object = MibScalar
fsFipsTestAlgo = _FsFipsTestAlgo_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 63, 1, 2),
    _FsFipsTestAlgo_Type()
)
fsFipsTestAlgo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsFipsTestAlgo.setStatus("current")


class _FsfipsZeroizeCryptoKeys_Type(TruthValue):
    """Custom type fsfipsZeroizeCryptoKeys based on TruthValue"""
    defaultValue = 2


_FsfipsZeroizeCryptoKeys_Type.__name__ = "TruthValue"
_FsfipsZeroizeCryptoKeys_Object = MibScalar
fsfipsZeroizeCryptoKeys = _FsfipsZeroizeCryptoKeys_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 63, 1, 3),
    _FsfipsZeroizeCryptoKeys_Type()
)
fsfipsZeroizeCryptoKeys.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsfipsZeroizeCryptoKeys.setStatus("current")


class _FsFipsTraceLevel_Type(Integer32):
    """Custom type fsFipsTraceLevel based on Integer32"""
    defaultValue = 0


_FsFipsTraceLevel_Type.__name__ = "Integer32"
_FsFipsTraceLevel_Object = MibScalar
fsFipsTraceLevel = _FsFipsTraceLevel_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 63, 1, 4),
    _FsFipsTraceLevel_Type()
)
fsFipsTraceLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsFipsTraceLevel.setStatus("current")


class _FsFipsTestExecutionResult_Type(Integer32):
    """Custom type fsFipsTestExecutionResult based on Integer32"""
    defaultValue = 0


_FsFipsTestExecutionResult_Type.__name__ = "Integer32"
_FsFipsTestExecutionResult_Object = MibScalar
fsFipsTestExecutionResult = _FsFipsTestExecutionResult_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 63, 1, 5),
    _FsFipsTestExecutionResult_Type()
)
fsFipsTestExecutionResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFipsTestExecutionResult.setStatus("current")


class _FsFipsFailedAlgorithm_Type(Integer32):
    """Custom type fsFipsFailedAlgorithm based on Integer32"""
    defaultValue = 0


_FsFipsFailedAlgorithm_Type.__name__ = "Integer32"
_FsFipsFailedAlgorithm_Object = MibScalar
fsFipsFailedAlgorithm = _FsFipsFailedAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 63, 1, 6),
    _FsFipsFailedAlgorithm_Type()
)
fsFipsFailedAlgorithm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFipsFailedAlgorithm.setStatus("current")


class _FsFipsBypassCapability_Type(Integer32):
    """Custom type fsFipsBypassCapability based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bypassCapability", 1),
          ("noBypassCapability", 2))
    )


_FsFipsBypassCapability_Type.__name__ = "Integer32"
_FsFipsBypassCapability_Object = MibScalar
fsFipsBypassCapability = _FsFipsBypassCapability_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 63, 1, 7),
    _FsFipsBypassCapability_Type()
)
fsFipsBypassCapability.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsFipsBypassCapability.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ARICENT-FIPS-MIB",
    **{"fsFips": fsFips,
       "fsFipsConfigurations": fsFipsConfigurations,
       "fsFipsOperMode": fsFipsOperMode,
       "fsFipsTestAlgo": fsFipsTestAlgo,
       "fsfipsZeroizeCryptoKeys": fsfipsZeroizeCryptoKeys,
       "fsFipsTraceLevel": fsFipsTraceLevel,
       "fsFipsTestExecutionResult": fsFipsTestExecutionResult,
       "fsFipsFailedAlgorithm": fsFipsFailedAlgorithm,
       "fsFipsBypassCapability": fsFipsBypassCapability}
)
