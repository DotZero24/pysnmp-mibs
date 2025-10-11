# SNMP MIB module (TRANZEO-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/tranzeo/TRANZEO-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:33:54 2025
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


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Tranzeo_ObjectIdentity = ObjectIdentity
tranzeo = _Tranzeo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24575)
)
_Signal_ObjectIdentity = ObjectIdentity
signal = _Signal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 24575, 1)
)


class _Rssi_Type(Integer32):
    """Custom type rssi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-110, 0),
    )


_Rssi_Type.__name__ = "Integer32"
_Rssi_Object = MibScalar
rssi = _Rssi_Object(
    (1, 3, 6, 1, 4, 1, 24575, 1, 1),
    _Rssi_Type()
)
rssi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rssi.setStatus("mandatory")


class _Signallow_Type(Integer32):
    """Custom type signallow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-110, 0),
    )


_Signallow_Type.__name__ = "Integer32"
_Signallow_Object = MibScalar
signallow = _Signallow_Object(
    (1, 3, 6, 1, 4, 1, 24575, 1, 1, 1),
    _Signallow_Type()
)
signallow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    signallow.setStatus("mandatory")


class _Signalaverage_Type(Integer32):
    """Custom type signalaverage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-110, 0),
    )


_Signalaverage_Type.__name__ = "Integer32"
_Signalaverage_Object = MibScalar
signalaverage = _Signalaverage_Object(
    (1, 3, 6, 1, 4, 1, 24575, 1, 1, 2),
    _Signalaverage_Type()
)
signalaverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    signalaverage.setStatus("mandatory")


class _Signalhigh_Type(Integer32):
    """Custom type signalhigh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-110, 0),
    )


_Signalhigh_Type.__name__ = "Integer32"
_Signalhigh_Object = MibScalar
signalhigh = _Signalhigh_Object(
    (1, 3, 6, 1, 4, 1, 24575, 1, 1, 3),
    _Signalhigh_Type()
)
signalhigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    signalhigh.setStatus("mandatory")


class _Noise_Type(Integer32):
    """Custom type noise based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-110, 0),
    )


_Noise_Type.__name__ = "Integer32"
_Noise_Object = MibScalar
noise = _Noise_Object(
    (1, 3, 6, 1, 4, 1, 24575, 1, 2),
    _Noise_Type()
)
noise.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    noise.setStatus("mandatory")


class _Noiselow_Type(Integer32):
    """Custom type noiselow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-110, 0),
    )


_Noiselow_Type.__name__ = "Integer32"
_Noiselow_Object = MibScalar
noiselow = _Noiselow_Object(
    (1, 3, 6, 1, 4, 1, 24575, 1, 2, 1),
    _Noiselow_Type()
)
noiselow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    noiselow.setStatus("mandatory")


class _Noiseaverage_Type(Integer32):
    """Custom type noiseaverage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-110, 0),
    )


_Noiseaverage_Type.__name__ = "Integer32"
_Noiseaverage_Object = MibScalar
noiseaverage = _Noiseaverage_Object(
    (1, 3, 6, 1, 4, 1, 24575, 1, 2, 2),
    _Noiseaverage_Type()
)
noiseaverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    noiseaverage.setStatus("mandatory")


class _Noisehigh_Type(Integer32):
    """Custom type noisehigh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-110, 0),
    )


_Noisehigh_Type.__name__ = "Integer32"
_Noisehigh_Object = MibScalar
noisehigh = _Noisehigh_Object(
    (1, 3, 6, 1, 4, 1, 24575, 1, 2, 3),
    _Noisehigh_Type()
)
noisehigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    noisehigh.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TRANZEO-MIB",
    **{"tranzeo": tranzeo,
       "signal": signal,
       "rssi": rssi,
       "signallow": signallow,
       "signalaverage": signalaverage,
       "signalhigh": signalhigh,
       "noise": noise,
       "noiselow": noiselow,
       "noiseaverage": noiseaverage,
       "noisehigh": noisehigh}
)
