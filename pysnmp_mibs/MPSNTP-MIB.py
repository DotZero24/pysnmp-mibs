# SNMP MIB module (MPSNTP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/maipu/MPSNTP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:11:11 2025
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

(mpMgmt,) = mibBuilder.importSymbols(
    "MAIPU-SMI",
    "mpMgmt")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

mpSntpMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5651, 3, 28)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SntpGlobal_ObjectIdentity = ObjectIdentity
sntpGlobal = _SntpGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5651, 3, 28, 1)
)


class _SntpBroadcast_Type(Integer32):
    """Custom type sntpBroadcast based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_SntpBroadcast_Type.__name__ = "Integer32"
_SntpBroadcast_Object = MibScalar
sntpBroadcast = _SntpBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 28, 1, 1),
    _SntpBroadcast_Type()
)
sntpBroadcast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sntpBroadcast.setStatus("current")


class _SntpInterval_Type(Integer32):
    """Custom type sntpInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 3600),
    )


_SntpInterval_Type.__name__ = "Integer32"
_SntpInterval_Object = MibScalar
sntpInterval = _SntpInterval_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 28, 1, 2),
    _SntpInterval_Type()
)
sntpInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sntpInterval.setStatus("current")
_SntpSvrName_Type = OctetString
_SntpSvrName_Object = MibScalar
sntpSvrName = _SntpSvrName_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 28, 1, 3),
    _SntpSvrName_Type()
)
sntpSvrName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sntpSvrName.setStatus("current")


class _SntpTimeout_Type(Integer32):
    """Custom type sntpTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(300, 600),
    )


_SntpTimeout_Type.__name__ = "Integer32"
_SntpTimeout_Object = MibScalar
sntpTimeout = _SntpTimeout_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 28, 1, 4),
    _SntpTimeout_Type()
)
sntpTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sntpTimeout.setStatus("current")
_SntpLeapVerMode_Type = Integer32
_SntpLeapVerMode_Object = MibScalar
sntpLeapVerMode = _SntpLeapVerMode_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 28, 1, 5),
    _SntpLeapVerMode_Type()
)
sntpLeapVerMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sntpLeapVerMode.setStatus("current")
_SntpStratum_Type = Integer32
_SntpStratum_Object = MibScalar
sntpStratum = _SntpStratum_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 28, 1, 6),
    _SntpStratum_Type()
)
sntpStratum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sntpStratum.setStatus("current")
_SntpPoll_Type = Integer32
_SntpPoll_Object = MibScalar
sntpPoll = _SntpPoll_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 28, 1, 7),
    _SntpPoll_Type()
)
sntpPoll.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sntpPoll.setStatus("current")
_SntpPrecision_Type = Integer32
_SntpPrecision_Object = MibScalar
sntpPrecision = _SntpPrecision_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 28, 1, 8),
    _SntpPrecision_Type()
)
sntpPrecision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sntpPrecision.setStatus("current")
_SntpRootDelay_Type = Integer32
_SntpRootDelay_Object = MibScalar
sntpRootDelay = _SntpRootDelay_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 28, 1, 9),
    _SntpRootDelay_Type()
)
sntpRootDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sntpRootDelay.setStatus("current")
_SntpRootDispersion_Type = Integer32
_SntpRootDispersion_Object = MibScalar
sntpRootDispersion = _SntpRootDispersion_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 28, 1, 10),
    _SntpRootDispersion_Type()
)
sntpRootDispersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sntpRootDispersion.setStatus("current")
_SntpReferenceIdentifier_Type = Integer32
_SntpReferenceIdentifier_Object = MibScalar
sntpReferenceIdentifier = _SntpReferenceIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 28, 1, 11),
    _SntpReferenceIdentifier_Type()
)
sntpReferenceIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sntpReferenceIdentifier.setStatus("current")
_SntpReferencetimestampsec_Type = Integer32
_SntpReferencetimestampsec_Object = MibScalar
sntpReferencetimestampsec = _SntpReferencetimestampsec_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 28, 1, 12),
    _SntpReferencetimestampsec_Type()
)
sntpReferencetimestampsec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sntpReferencetimestampsec.setStatus("current")
_SntpOriginateTimestampSec_Type = Integer32
_SntpOriginateTimestampSec_Object = MibScalar
sntpOriginateTimestampSec = _SntpOriginateTimestampSec_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 28, 1, 13),
    _SntpOriginateTimestampSec_Type()
)
sntpOriginateTimestampSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sntpOriginateTimestampSec.setStatus("current")
_SntpReveiveTimestampSec_Type = Integer32
_SntpReveiveTimestampSec_Object = MibScalar
sntpReveiveTimestampSec = _SntpReveiveTimestampSec_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 28, 1, 14),
    _SntpReveiveTimestampSec_Type()
)
sntpReveiveTimestampSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sntpReveiveTimestampSec.setStatus("current")
_SntpTransmitTimestampSec_Type = Integer32
_SntpTransmitTimestampSec_Object = MibScalar
sntpTransmitTimestampSec = _SntpTransmitTimestampSec_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 28, 1, 15),
    _SntpTransmitTimestampSec_Type()
)
sntpTransmitTimestampSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sntpTransmitTimestampSec.setStatus("current")


class _SntpSysTimeStatus_Type(OctetString):
    """Custom type sntpSysTimeStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_SntpSysTimeStatus_Type.__name__ = "OctetString"
_SntpSysTimeStatus_Object = MibScalar
sntpSysTimeStatus = _SntpSysTimeStatus_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 28, 1, 16),
    _SntpSysTimeStatus_Type()
)
sntpSysTimeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sntpSysTimeStatus.setStatus("current")
_SntpUpdataSysTime_Type = OctetString
_SntpUpdataSysTime_Object = MibScalar
sntpUpdataSysTime = _SntpUpdataSysTime_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 28, 1, 17),
    _SntpUpdataSysTime_Type()
)
sntpUpdataSysTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sntpUpdataSysTime.setStatus("current")
_SntpToNowSec_Type = Integer32
_SntpToNowSec_Object = MibScalar
sntpToNowSec = _SntpToNowSec_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 28, 1, 18),
    _SntpToNowSec_Type()
)
sntpToNowSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sntpToNowSec.setStatus("current")
_SntpRoundtripTime_Type = Integer32
_SntpRoundtripTime_Object = MibScalar
sntpRoundtripTime = _SntpRoundtripTime_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 28, 1, 19),
    _SntpRoundtripTime_Type()
)
sntpRoundtripTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sntpRoundtripTime.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MPSNTP-MIB",
    **{"mpSntpMib": mpSntpMib,
       "sntpGlobal": sntpGlobal,
       "sntpBroadcast": sntpBroadcast,
       "sntpInterval": sntpInterval,
       "sntpSvrName": sntpSvrName,
       "sntpTimeout": sntpTimeout,
       "sntpLeapVerMode": sntpLeapVerMode,
       "sntpStratum": sntpStratum,
       "sntpPoll": sntpPoll,
       "sntpPrecision": sntpPrecision,
       "sntpRootDelay": sntpRootDelay,
       "sntpRootDispersion": sntpRootDispersion,
       "sntpReferenceIdentifier": sntpReferenceIdentifier,
       "sntpReferencetimestampsec": sntpReferencetimestampsec,
       "sntpOriginateTimestampSec": sntpOriginateTimestampSec,
       "sntpReveiveTimestampSec": sntpReveiveTimestampSec,
       "sntpTransmitTimestampSec": sntpTransmitTimestampSec,
       "sntpSysTimeStatus": sntpSysTimeStatus,
       "sntpUpdataSysTime": sntpUpdataSysTime,
       "sntpToNowSec": sntpToNowSec,
       "sntpRoundtripTime": sntpRoundtripTime}
)
