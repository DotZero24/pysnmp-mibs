# SNMP MIB module (BEGEMOT-NTP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/bsd/BEGEMOT-NTP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:21:32 2025
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

(begemot,) = mibBuilder.importSymbols(
    "BEGEMOT-MIB",
    "begemot")

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

begemotNtp = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 12325, 1, 201)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_BegemotNtpObjects_ObjectIdentity = ObjectIdentity
begemotNtpObjects = _BegemotNtpObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12325, 1, 201, 1)
)
_BegemotNtpHost_Type = OctetString
_BegemotNtpHost_Object = MibScalar
begemotNtpHost = _BegemotNtpHost_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 201, 1, 1),
    _BegemotNtpHost_Type()
)
begemotNtpHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    begemotNtpHost.setStatus("current")
_BegemotNtpPort_Type = OctetString
_BegemotNtpPort_Object = MibScalar
begemotNtpPort = _BegemotNtpPort_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 201, 1, 2),
    _BegemotNtpPort_Type()
)
begemotNtpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    begemotNtpPort.setStatus("current")
_BegemotNtpTimeout_Type = TimeTicks
_BegemotNtpTimeout_Object = MibScalar
begemotNtpTimeout = _BegemotNtpTimeout_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 201, 1, 3),
    _BegemotNtpTimeout_Type()
)
begemotNtpTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    begemotNtpTimeout.setStatus("current")
_BegemotNtpDebug_Type = Unsigned32
_BegemotNtpDebug_Object = MibScalar
begemotNtpDebug = _BegemotNtpDebug_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 201, 1, 4),
    _BegemotNtpDebug_Type()
)
begemotNtpDebug.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    begemotNtpDebug.setStatus("current")
_BegemotNtpJitter_Type = Counter64
_BegemotNtpJitter_Object = MibScalar
begemotNtpJitter = _BegemotNtpJitter_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 201, 1, 5),
    _BegemotNtpJitter_Type()
)
begemotNtpJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    begemotNtpJitter.setStatus("current")
_BegemotNtpStability_Type = Counter64
_BegemotNtpStability_Object = MibScalar
begemotNtpStability = _BegemotNtpStability_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 201, 1, 6),
    _BegemotNtpStability_Type()
)
begemotNtpStability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    begemotNtpStability.setStatus("current")
_BegemotNtpJitterThresh_Type = Counter64
_BegemotNtpJitterThresh_Object = MibScalar
begemotNtpJitterThresh = _BegemotNtpJitterThresh_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 201, 1, 7),
    _BegemotNtpJitterThresh_Type()
)
begemotNtpJitterThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    begemotNtpJitterThresh.setStatus("current")
_BegemotNtpStabilityThresh_Type = Counter64
_BegemotNtpStabilityThresh_Object = MibScalar
begemotNtpStabilityThresh = _BegemotNtpStabilityThresh_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 201, 1, 8),
    _BegemotNtpStabilityThresh_Type()
)
begemotNtpStabilityThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    begemotNtpStabilityThresh.setStatus("current")
_BegemotNtpTrapEnable_Type = TruthValue
_BegemotNtpTrapEnable_Object = MibScalar
begemotNtpTrapEnable = _BegemotNtpTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 12325, 1, 201, 1, 9),
    _BegemotNtpTrapEnable_Type()
)
begemotNtpTrapEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    begemotNtpTrapEnable.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BEGEMOT-NTP-MIB",
    **{"begemotNtp": begemotNtp,
       "begemotNtpObjects": begemotNtpObjects,
       "begemotNtpHost": begemotNtpHost,
       "begemotNtpPort": begemotNtpPort,
       "begemotNtpTimeout": begemotNtpTimeout,
       "begemotNtpDebug": begemotNtpDebug,
       "begemotNtpJitter": begemotNtpJitter,
       "begemotNtpStability": begemotNtpStability,
       "begemotNtpJitterThresh": begemotNtpJitterThresh,
       "begemotNtpStabilityThresh": begemotNtpStabilityThresh,
       "begemotNtpTrapEnable": begemotNtpTrapEnable}
)
