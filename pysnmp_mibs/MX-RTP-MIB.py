# SNMP MIB module (MX-RTP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/media5/MX-RTP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:06:43 2025
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

(mediatrixConfig,
 mediatrixMgmt) = mibBuilder.importSymbols(
    "MX-SMI",
    "mediatrixConfig",
    "mediatrixMgmt")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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

rtpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 10, 50)
)
if mibBuilder.loadTexts:
    rtpMIB.setRevisions(
        ("1903-10-27 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RtpMIBObjects_ObjectIdentity = ObjectIdentity
rtpMIBObjects = _RtpMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 10, 50, 1)
)
_RtpStats_ObjectIdentity = ObjectIdentity
rtpStats = _RtpStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 10, 50, 1, 2)
)
_RtpStatsLastConnectionStatistics_ObjectIdentity = ObjectIdentity
rtpStatsLastConnectionStatistics = _RtpStatsLastConnectionStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 10, 50, 1, 2, 5)
)
_RtpStatsLastConnNumberOctetsTransmitted_Type = Unsigned32
_RtpStatsLastConnNumberOctetsTransmitted_Object = MibScalar
rtpStatsLastConnNumberOctetsTransmitted = _RtpStatsLastConnNumberOctetsTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 4935, 10, 50, 1, 2, 5, 1),
    _RtpStatsLastConnNumberOctetsTransmitted_Type()
)
rtpStatsLastConnNumberOctetsTransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtpStatsLastConnNumberOctetsTransmitted.setStatus("current")
_RtpStatsLastConnNumberOctetsReceived_Type = Unsigned32
_RtpStatsLastConnNumberOctetsReceived_Object = MibScalar
rtpStatsLastConnNumberOctetsReceived = _RtpStatsLastConnNumberOctetsReceived_Object(
    (1, 3, 6, 1, 4, 1, 4935, 10, 50, 1, 2, 5, 2),
    _RtpStatsLastConnNumberOctetsReceived_Type()
)
rtpStatsLastConnNumberOctetsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtpStatsLastConnNumberOctetsReceived.setStatus("current")
_RtpStatsLastConnNumberPacketsTransmitted_Type = Unsigned32
_RtpStatsLastConnNumberPacketsTransmitted_Object = MibScalar
rtpStatsLastConnNumberPacketsTransmitted = _RtpStatsLastConnNumberPacketsTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 4935, 10, 50, 1, 2, 5, 3),
    _RtpStatsLastConnNumberPacketsTransmitted_Type()
)
rtpStatsLastConnNumberPacketsTransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtpStatsLastConnNumberPacketsTransmitted.setStatus("current")
_RtpStatsLastConnNumberPacketsReceived_Type = Unsigned32
_RtpStatsLastConnNumberPacketsReceived_Object = MibScalar
rtpStatsLastConnNumberPacketsReceived = _RtpStatsLastConnNumberPacketsReceived_Object(
    (1, 3, 6, 1, 4, 1, 4935, 10, 50, 1, 2, 5, 4),
    _RtpStatsLastConnNumberPacketsReceived_Type()
)
rtpStatsLastConnNumberPacketsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtpStatsLastConnNumberPacketsReceived.setStatus("current")
_RtpStatsLastConnNumberPacketsLost_Type = Integer32
_RtpStatsLastConnNumberPacketsLost_Object = MibScalar
rtpStatsLastConnNumberPacketsLost = _RtpStatsLastConnNumberPacketsLost_Object(
    (1, 3, 6, 1, 4, 1, 4935, 10, 50, 1, 2, 5, 5),
    _RtpStatsLastConnNumberPacketsLost_Type()
)
rtpStatsLastConnNumberPacketsLost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtpStatsLastConnNumberPacketsLost.setStatus("current")


class _RtpStatsLastConnPercentPacketsLost_Type(Unsigned32):
    """Custom type rtpStatsLastConnPercentPacketsLost based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_RtpStatsLastConnPercentPacketsLost_Type.__name__ = "Unsigned32"
_RtpStatsLastConnPercentPacketsLost_Object = MibScalar
rtpStatsLastConnPercentPacketsLost = _RtpStatsLastConnPercentPacketsLost_Object(
    (1, 3, 6, 1, 4, 1, 4935, 10, 50, 1, 2, 5, 6),
    _RtpStatsLastConnPercentPacketsLost_Type()
)
rtpStatsLastConnPercentPacketsLost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtpStatsLastConnPercentPacketsLost.setStatus("current")
_RtpStatsLastConnInterarrivalJitterMin_Type = Unsigned32
_RtpStatsLastConnInterarrivalJitterMin_Object = MibScalar
rtpStatsLastConnInterarrivalJitterMin = _RtpStatsLastConnInterarrivalJitterMin_Object(
    (1, 3, 6, 1, 4, 1, 4935, 10, 50, 1, 2, 5, 7),
    _RtpStatsLastConnInterarrivalJitterMin_Type()
)
rtpStatsLastConnInterarrivalJitterMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtpStatsLastConnInterarrivalJitterMin.setStatus("current")
_RtpStatsLastConnInterarrivalJitterMax_Type = Unsigned32
_RtpStatsLastConnInterarrivalJitterMax_Object = MibScalar
rtpStatsLastConnInterarrivalJitterMax = _RtpStatsLastConnInterarrivalJitterMax_Object(
    (1, 3, 6, 1, 4, 1, 4935, 10, 50, 1, 2, 5, 8),
    _RtpStatsLastConnInterarrivalJitterMax_Type()
)
rtpStatsLastConnInterarrivalJitterMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtpStatsLastConnInterarrivalJitterMax.setStatus("current")
_RtpStatsLastConnInterarrivalJitterAvg_Type = Unsigned32
_RtpStatsLastConnInterarrivalJitterAvg_Object = MibScalar
rtpStatsLastConnInterarrivalJitterAvg = _RtpStatsLastConnInterarrivalJitterAvg_Object(
    (1, 3, 6, 1, 4, 1, 4935, 10, 50, 1, 2, 5, 9),
    _RtpStatsLastConnInterarrivalJitterAvg_Type()
)
rtpStatsLastConnInterarrivalJitterAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtpStatsLastConnInterarrivalJitterAvg.setStatus("current")
_RtpStatsLastConnLatencyMin_Type = Unsigned32
_RtpStatsLastConnLatencyMin_Object = MibScalar
rtpStatsLastConnLatencyMin = _RtpStatsLastConnLatencyMin_Object(
    (1, 3, 6, 1, 4, 1, 4935, 10, 50, 1, 2, 5, 10),
    _RtpStatsLastConnLatencyMin_Type()
)
rtpStatsLastConnLatencyMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtpStatsLastConnLatencyMin.setStatus("current")
_RtpStatsLastConnLatencyMax_Type = Unsigned32
_RtpStatsLastConnLatencyMax_Object = MibScalar
rtpStatsLastConnLatencyMax = _RtpStatsLastConnLatencyMax_Object(
    (1, 3, 6, 1, 4, 1, 4935, 10, 50, 1, 2, 5, 11),
    _RtpStatsLastConnLatencyMax_Type()
)
rtpStatsLastConnLatencyMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtpStatsLastConnLatencyMax.setStatus("current")
_RtpStatsLastConnLatencyAvg_Type = Unsigned32
_RtpStatsLastConnLatencyAvg_Object = MibScalar
rtpStatsLastConnLatencyAvg = _RtpStatsLastConnLatencyAvg_Object(
    (1, 3, 6, 1, 4, 1, 4935, 10, 50, 1, 2, 5, 12),
    _RtpStatsLastConnLatencyAvg_Type()
)
rtpStatsLastConnLatencyAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtpStatsLastConnLatencyAvg.setStatus("current")
_RtpStatsCurrentStatistics_ObjectIdentity = ObjectIdentity
rtpStatsCurrentStatistics = _RtpStatsCurrentStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 10, 50, 1, 2, 10)
)
_RtpStatsCurrentTotalOctetsTransmitted_Type = Unsigned32
_RtpStatsCurrentTotalOctetsTransmitted_Object = MibScalar
rtpStatsCurrentTotalOctetsTransmitted = _RtpStatsCurrentTotalOctetsTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 4935, 10, 50, 1, 2, 10, 1),
    _RtpStatsCurrentTotalOctetsTransmitted_Type()
)
rtpStatsCurrentTotalOctetsTransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtpStatsCurrentTotalOctetsTransmitted.setStatus("current")
_RtpStatsCurrentTotalOctetsReceived_Type = Unsigned32
_RtpStatsCurrentTotalOctetsReceived_Object = MibScalar
rtpStatsCurrentTotalOctetsReceived = _RtpStatsCurrentTotalOctetsReceived_Object(
    (1, 3, 6, 1, 4, 1, 4935, 10, 50, 1, 2, 10, 2),
    _RtpStatsCurrentTotalOctetsReceived_Type()
)
rtpStatsCurrentTotalOctetsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtpStatsCurrentTotalOctetsReceived.setStatus("current")
_RtpStatsCurrentTotalPacketsTransmitted_Type = Unsigned32
_RtpStatsCurrentTotalPacketsTransmitted_Object = MibScalar
rtpStatsCurrentTotalPacketsTransmitted = _RtpStatsCurrentTotalPacketsTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 4935, 10, 50, 1, 2, 10, 3),
    _RtpStatsCurrentTotalPacketsTransmitted_Type()
)
rtpStatsCurrentTotalPacketsTransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtpStatsCurrentTotalPacketsTransmitted.setStatus("current")
_RtpStatsCurrentTotalPacketsReceived_Type = Unsigned32
_RtpStatsCurrentTotalPacketsReceived_Object = MibScalar
rtpStatsCurrentTotalPacketsReceived = _RtpStatsCurrentTotalPacketsReceived_Object(
    (1, 3, 6, 1, 4, 1, 4935, 10, 50, 1, 2, 10, 4),
    _RtpStatsCurrentTotalPacketsReceived_Type()
)
rtpStatsCurrentTotalPacketsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtpStatsCurrentTotalPacketsReceived.setStatus("current")
_RtpStatsCurrentTotalPacketsLost_Type = Integer32
_RtpStatsCurrentTotalPacketsLost_Object = MibScalar
rtpStatsCurrentTotalPacketsLost = _RtpStatsCurrentTotalPacketsLost_Object(
    (1, 3, 6, 1, 4, 1, 4935, 10, 50, 1, 2, 10, 5),
    _RtpStatsCurrentTotalPacketsLost_Type()
)
rtpStatsCurrentTotalPacketsLost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtpStatsCurrentTotalPacketsLost.setStatus("current")


class _RtpStatsCurrentTotalPercentPacketsLost_Type(Unsigned32):
    """Custom type rtpStatsCurrentTotalPercentPacketsLost based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_RtpStatsCurrentTotalPercentPacketsLost_Type.__name__ = "Unsigned32"
_RtpStatsCurrentTotalPercentPacketsLost_Object = MibScalar
rtpStatsCurrentTotalPercentPacketsLost = _RtpStatsCurrentTotalPercentPacketsLost_Object(
    (1, 3, 6, 1, 4, 1, 4935, 10, 50, 1, 2, 10, 6),
    _RtpStatsCurrentTotalPercentPacketsLost_Type()
)
rtpStatsCurrentTotalPercentPacketsLost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtpStatsCurrentTotalPercentPacketsLost.setStatus("current")
_RtpStatsCurrentTotalInterarrivalJitterMin_Type = Unsigned32
_RtpStatsCurrentTotalInterarrivalJitterMin_Object = MibScalar
rtpStatsCurrentTotalInterarrivalJitterMin = _RtpStatsCurrentTotalInterarrivalJitterMin_Object(
    (1, 3, 6, 1, 4, 1, 4935, 10, 50, 1, 2, 10, 7),
    _RtpStatsCurrentTotalInterarrivalJitterMin_Type()
)
rtpStatsCurrentTotalInterarrivalJitterMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtpStatsCurrentTotalInterarrivalJitterMin.setStatus("current")
_RtpStatsCurrentTotalInterarrivalJitterMax_Type = Unsigned32
_RtpStatsCurrentTotalInterarrivalJitterMax_Object = MibScalar
rtpStatsCurrentTotalInterarrivalJitterMax = _RtpStatsCurrentTotalInterarrivalJitterMax_Object(
    (1, 3, 6, 1, 4, 1, 4935, 10, 50, 1, 2, 10, 8),
    _RtpStatsCurrentTotalInterarrivalJitterMax_Type()
)
rtpStatsCurrentTotalInterarrivalJitterMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtpStatsCurrentTotalInterarrivalJitterMax.setStatus("current")
_RtpStatsCurrentTotalInterarrivalJitterAvg_Type = Unsigned32
_RtpStatsCurrentTotalInterarrivalJitterAvg_Object = MibScalar
rtpStatsCurrentTotalInterarrivalJitterAvg = _RtpStatsCurrentTotalInterarrivalJitterAvg_Object(
    (1, 3, 6, 1, 4, 1, 4935, 10, 50, 1, 2, 10, 9),
    _RtpStatsCurrentTotalInterarrivalJitterAvg_Type()
)
rtpStatsCurrentTotalInterarrivalJitterAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtpStatsCurrentTotalInterarrivalJitterAvg.setStatus("current")
_RtpStatsCurrentTotalLatencyMin_Type = Unsigned32
_RtpStatsCurrentTotalLatencyMin_Object = MibScalar
rtpStatsCurrentTotalLatencyMin = _RtpStatsCurrentTotalLatencyMin_Object(
    (1, 3, 6, 1, 4, 1, 4935, 10, 50, 1, 2, 10, 10),
    _RtpStatsCurrentTotalLatencyMin_Type()
)
rtpStatsCurrentTotalLatencyMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtpStatsCurrentTotalLatencyMin.setStatus("current")
_RtpStatsCurrentTotalLatencyMax_Type = Unsigned32
_RtpStatsCurrentTotalLatencyMax_Object = MibScalar
rtpStatsCurrentTotalLatencyMax = _RtpStatsCurrentTotalLatencyMax_Object(
    (1, 3, 6, 1, 4, 1, 4935, 10, 50, 1, 2, 10, 11),
    _RtpStatsCurrentTotalLatencyMax_Type()
)
rtpStatsCurrentTotalLatencyMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtpStatsCurrentTotalLatencyMax.setStatus("current")
_RtpStatsCurrentTotalLatencyAvg_Type = Unsigned32
_RtpStatsCurrentTotalLatencyAvg_Object = MibScalar
rtpStatsCurrentTotalLatencyAvg = _RtpStatsCurrentTotalLatencyAvg_Object(
    (1, 3, 6, 1, 4, 1, 4935, 10, 50, 1, 2, 10, 12),
    _RtpStatsCurrentTotalLatencyAvg_Type()
)
rtpStatsCurrentTotalLatencyAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtpStatsCurrentTotalLatencyAvg.setStatus("current")
_RtpStatsCumulatedStatistics_ObjectIdentity = ObjectIdentity
rtpStatsCumulatedStatistics = _RtpStatsCumulatedStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 10, 50, 1, 2, 15)
)
_RtpStatsCumulatedTotalOctetsTransmitted_Type = Unsigned32
_RtpStatsCumulatedTotalOctetsTransmitted_Object = MibScalar
rtpStatsCumulatedTotalOctetsTransmitted = _RtpStatsCumulatedTotalOctetsTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 4935, 10, 50, 1, 2, 15, 1),
    _RtpStatsCumulatedTotalOctetsTransmitted_Type()
)
rtpStatsCumulatedTotalOctetsTransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtpStatsCumulatedTotalOctetsTransmitted.setStatus("current")
_RtpStatsCumulatedTotalOctetsReceived_Type = Unsigned32
_RtpStatsCumulatedTotalOctetsReceived_Object = MibScalar
rtpStatsCumulatedTotalOctetsReceived = _RtpStatsCumulatedTotalOctetsReceived_Object(
    (1, 3, 6, 1, 4, 1, 4935, 10, 50, 1, 2, 15, 2),
    _RtpStatsCumulatedTotalOctetsReceived_Type()
)
rtpStatsCumulatedTotalOctetsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtpStatsCumulatedTotalOctetsReceived.setStatus("current")
_RtpStatsCumulatedTotalPacketsTransmitted_Type = Unsigned32
_RtpStatsCumulatedTotalPacketsTransmitted_Object = MibScalar
rtpStatsCumulatedTotalPacketsTransmitted = _RtpStatsCumulatedTotalPacketsTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 4935, 10, 50, 1, 2, 15, 3),
    _RtpStatsCumulatedTotalPacketsTransmitted_Type()
)
rtpStatsCumulatedTotalPacketsTransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtpStatsCumulatedTotalPacketsTransmitted.setStatus("current")
_RtpStatsCumulatedTotalPacketsReceived_Type = Unsigned32
_RtpStatsCumulatedTotalPacketsReceived_Object = MibScalar
rtpStatsCumulatedTotalPacketsReceived = _RtpStatsCumulatedTotalPacketsReceived_Object(
    (1, 3, 6, 1, 4, 1, 4935, 10, 50, 1, 2, 15, 4),
    _RtpStatsCumulatedTotalPacketsReceived_Type()
)
rtpStatsCumulatedTotalPacketsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtpStatsCumulatedTotalPacketsReceived.setStatus("current")
_RtpStatsCumulatedTotalPacketsLost_Type = Integer32
_RtpStatsCumulatedTotalPacketsLost_Object = MibScalar
rtpStatsCumulatedTotalPacketsLost = _RtpStatsCumulatedTotalPacketsLost_Object(
    (1, 3, 6, 1, 4, 1, 4935, 10, 50, 1, 2, 15, 5),
    _RtpStatsCumulatedTotalPacketsLost_Type()
)
rtpStatsCumulatedTotalPacketsLost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtpStatsCumulatedTotalPacketsLost.setStatus("current")


class _RtpStatsCumulatedTotalPercentPacketsLost_Type(Unsigned32):
    """Custom type rtpStatsCumulatedTotalPercentPacketsLost based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_RtpStatsCumulatedTotalPercentPacketsLost_Type.__name__ = "Unsigned32"
_RtpStatsCumulatedTotalPercentPacketsLost_Object = MibScalar
rtpStatsCumulatedTotalPercentPacketsLost = _RtpStatsCumulatedTotalPercentPacketsLost_Object(
    (1, 3, 6, 1, 4, 1, 4935, 10, 50, 1, 2, 15, 6),
    _RtpStatsCumulatedTotalPercentPacketsLost_Type()
)
rtpStatsCumulatedTotalPercentPacketsLost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtpStatsCumulatedTotalPercentPacketsLost.setStatus("current")
_RtpStatsCumulatedTotalInterarrivalJitterMin_Type = Unsigned32
_RtpStatsCumulatedTotalInterarrivalJitterMin_Object = MibScalar
rtpStatsCumulatedTotalInterarrivalJitterMin = _RtpStatsCumulatedTotalInterarrivalJitterMin_Object(
    (1, 3, 6, 1, 4, 1, 4935, 10, 50, 1, 2, 15, 7),
    _RtpStatsCumulatedTotalInterarrivalJitterMin_Type()
)
rtpStatsCumulatedTotalInterarrivalJitterMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtpStatsCumulatedTotalInterarrivalJitterMin.setStatus("current")
_RtpStatsCumulatedTotalInterarrivalJitterMax_Type = Unsigned32
_RtpStatsCumulatedTotalInterarrivalJitterMax_Object = MibScalar
rtpStatsCumulatedTotalInterarrivalJitterMax = _RtpStatsCumulatedTotalInterarrivalJitterMax_Object(
    (1, 3, 6, 1, 4, 1, 4935, 10, 50, 1, 2, 15, 8),
    _RtpStatsCumulatedTotalInterarrivalJitterMax_Type()
)
rtpStatsCumulatedTotalInterarrivalJitterMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtpStatsCumulatedTotalInterarrivalJitterMax.setStatus("current")
_RtpStatsCumulatedTotalInterarrivalJitterAvg_Type = Unsigned32
_RtpStatsCumulatedTotalInterarrivalJitterAvg_Object = MibScalar
rtpStatsCumulatedTotalInterarrivalJitterAvg = _RtpStatsCumulatedTotalInterarrivalJitterAvg_Object(
    (1, 3, 6, 1, 4, 1, 4935, 10, 50, 1, 2, 15, 9),
    _RtpStatsCumulatedTotalInterarrivalJitterAvg_Type()
)
rtpStatsCumulatedTotalInterarrivalJitterAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtpStatsCumulatedTotalInterarrivalJitterAvg.setStatus("current")
_RtpStatsCumulatedTotalLatencyMin_Type = Unsigned32
_RtpStatsCumulatedTotalLatencyMin_Object = MibScalar
rtpStatsCumulatedTotalLatencyMin = _RtpStatsCumulatedTotalLatencyMin_Object(
    (1, 3, 6, 1, 4, 1, 4935, 10, 50, 1, 2, 15, 10),
    _RtpStatsCumulatedTotalLatencyMin_Type()
)
rtpStatsCumulatedTotalLatencyMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtpStatsCumulatedTotalLatencyMin.setStatus("current")
_RtpStatsCumulatedTotalLatencyMax_Type = Unsigned32
_RtpStatsCumulatedTotalLatencyMax_Object = MibScalar
rtpStatsCumulatedTotalLatencyMax = _RtpStatsCumulatedTotalLatencyMax_Object(
    (1, 3, 6, 1, 4, 1, 4935, 10, 50, 1, 2, 15, 11),
    _RtpStatsCumulatedTotalLatencyMax_Type()
)
rtpStatsCumulatedTotalLatencyMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtpStatsCumulatedTotalLatencyMax.setStatus("current")
_RtpStatsCumulatedTotalLatencyAvg_Type = Unsigned32
_RtpStatsCumulatedTotalLatencyAvg_Object = MibScalar
rtpStatsCumulatedTotalLatencyAvg = _RtpStatsCumulatedTotalLatencyAvg_Object(
    (1, 3, 6, 1, 4, 1, 4935, 10, 50, 1, 2, 15, 12),
    _RtpStatsCumulatedTotalLatencyAvg_Type()
)
rtpStatsCumulatedTotalLatencyAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtpStatsCumulatedTotalLatencyAvg.setStatus("current")
_RtpConformance_ObjectIdentity = ObjectIdentity
rtpConformance = _RtpConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 10, 50, 2)
)
_RtpCompliances_ObjectIdentity = ObjectIdentity
rtpCompliances = _RtpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 10, 50, 2, 1)
)
_RtpGroups_ObjectIdentity = ObjectIdentity
rtpGroups = _RtpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 10, 50, 2, 2)
)
_RtpConfig_ObjectIdentity = ObjectIdentity
rtpConfig = _RtpConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 115)
)
if mibBuilder.loadTexts:
    rtpConfig.setStatus("current")


class _RtpConfigBasePort_Type(Unsigned32):
    """Custom type rtpConfigBasePort based on Unsigned32"""
    defaultValue = 5004

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1025, 64535),
    )


_RtpConfigBasePort_Type.__name__ = "Unsigned32"
_RtpConfigBasePort_Object = MibScalar
rtpConfigBasePort = _RtpConfigBasePort_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 115, 5),
    _RtpConfigBasePort_Type()
)
rtpConfigBasePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtpConfigBasePort.setStatus("current")

# Managed Objects groups

rtpStatsBasicGroupVer1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4935, 10, 50, 2, 2, 1)
)
rtpStatsBasicGroupVer1.setObjects(
      *(("MX-RTP-MIB", "rtpStatsLastConnNumberOctetsTransmitted"),
        ("MX-RTP-MIB", "rtpStatsLastConnNumberOctetsReceived"),
        ("MX-RTP-MIB", "rtpStatsLastConnNumberPacketsTransmitted"),
        ("MX-RTP-MIB", "rtpStatsLastConnNumberPacketsReceived"),
        ("MX-RTP-MIB", "rtpStatsLastConnNumberPacketsLost"),
        ("MX-RTP-MIB", "rtpStatsLastConnPercentPacketsLost"),
        ("MX-RTP-MIB", "rtpStatsLastConnInterarrivalJitterMin"),
        ("MX-RTP-MIB", "rtpStatsLastConnInterarrivalJitterMax"),
        ("MX-RTP-MIB", "rtpStatsLastConnInterarrivalJitterAvg"),
        ("MX-RTP-MIB", "rtpStatsLastConnLatencyMin"),
        ("MX-RTP-MIB", "rtpStatsLastConnLatencyMax"),
        ("MX-RTP-MIB", "rtpStatsLastConnLatencyAvg"),
        ("MX-RTP-MIB", "rtpStatsCurrentTotalOctetsTransmitted"),
        ("MX-RTP-MIB", "rtpStatsCurrentTotalOctetsReceived"),
        ("MX-RTP-MIB", "rtpStatsCurrentTotalPacketsTransmitted"),
        ("MX-RTP-MIB", "rtpStatsCurrentTotalPacketsReceived"),
        ("MX-RTP-MIB", "rtpStatsCurrentTotalPacketsLost"),
        ("MX-RTP-MIB", "rtpStatsCurrentTotalPercentPacketsLost"),
        ("MX-RTP-MIB", "rtpStatsCurrentTotalInterarrivalJitterMin"),
        ("MX-RTP-MIB", "rtpStatsCurrentTotalInterarrivalJitterMax"),
        ("MX-RTP-MIB", "rtpStatsCurrentTotalInterarrivalJitterAvg"),
        ("MX-RTP-MIB", "rtpStatsCurrentTotalLatencyMin"),
        ("MX-RTP-MIB", "rtpStatsCurrentTotalLatencyMax"),
        ("MX-RTP-MIB", "rtpStatsCurrentTotalLatencyAvg"),
        ("MX-RTP-MIB", "rtpStatsCumulatedTotalOctetsTransmitted"),
        ("MX-RTP-MIB", "rtpStatsCumulatedTotalOctetsReceived"),
        ("MX-RTP-MIB", "rtpStatsCumulatedTotalPacketsTransmitted"),
        ("MX-RTP-MIB", "rtpStatsCumulatedTotalPacketsReceived"),
        ("MX-RTP-MIB", "rtpStatsCumulatedTotalPacketsLost"),
        ("MX-RTP-MIB", "rtpStatsCumulatedTotalPercentPacketsLost"),
        ("MX-RTP-MIB", "rtpStatsCumulatedTotalInterarrivalJitterMin"),
        ("MX-RTP-MIB", "rtpStatsCumulatedTotalInterarrivalJitterMax"),
        ("MX-RTP-MIB", "rtpStatsCumulatedTotalInterarrivalJitterAvg"),
        ("MX-RTP-MIB", "rtpStatsCumulatedTotalLatencyMin"),
        ("MX-RTP-MIB", "rtpStatsCumulatedTotalLatencyMax"),
        ("MX-RTP-MIB", "rtpStatsCumulatedTotalLatencyAvg"))
)
if mibBuilder.loadTexts:
    rtpStatsBasicGroupVer1.setStatus("current")

rtpConfigBasicGroupVer1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4935, 10, 50, 2, 2, 2)
)
rtpConfigBasicGroupVer1.setObjects(
    ("MX-RTP-MIB", "rtpConfigBasePort")
)
if mibBuilder.loadTexts:
    rtpConfigBasicGroupVer1.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

rtpBasicComplVer1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4935, 10, 50, 2, 1, 1)
)
rtpBasicComplVer1.setObjects(
      *(("MX-RTP-MIB", "rtpStatsBasicGroupVer1"),
        ("MX-RTP-MIB", "rtpConfigBasicGroupVer1"))
)
if mibBuilder.loadTexts:
    rtpBasicComplVer1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MX-RTP-MIB",
    **{"rtpMIB": rtpMIB,
       "rtpMIBObjects": rtpMIBObjects,
       "rtpStats": rtpStats,
       "rtpStatsLastConnectionStatistics": rtpStatsLastConnectionStatistics,
       "rtpStatsLastConnNumberOctetsTransmitted": rtpStatsLastConnNumberOctetsTransmitted,
       "rtpStatsLastConnNumberOctetsReceived": rtpStatsLastConnNumberOctetsReceived,
       "rtpStatsLastConnNumberPacketsTransmitted": rtpStatsLastConnNumberPacketsTransmitted,
       "rtpStatsLastConnNumberPacketsReceived": rtpStatsLastConnNumberPacketsReceived,
       "rtpStatsLastConnNumberPacketsLost": rtpStatsLastConnNumberPacketsLost,
       "rtpStatsLastConnPercentPacketsLost": rtpStatsLastConnPercentPacketsLost,
       "rtpStatsLastConnInterarrivalJitterMin": rtpStatsLastConnInterarrivalJitterMin,
       "rtpStatsLastConnInterarrivalJitterMax": rtpStatsLastConnInterarrivalJitterMax,
       "rtpStatsLastConnInterarrivalJitterAvg": rtpStatsLastConnInterarrivalJitterAvg,
       "rtpStatsLastConnLatencyMin": rtpStatsLastConnLatencyMin,
       "rtpStatsLastConnLatencyMax": rtpStatsLastConnLatencyMax,
       "rtpStatsLastConnLatencyAvg": rtpStatsLastConnLatencyAvg,
       "rtpStatsCurrentStatistics": rtpStatsCurrentStatistics,
       "rtpStatsCurrentTotalOctetsTransmitted": rtpStatsCurrentTotalOctetsTransmitted,
       "rtpStatsCurrentTotalOctetsReceived": rtpStatsCurrentTotalOctetsReceived,
       "rtpStatsCurrentTotalPacketsTransmitted": rtpStatsCurrentTotalPacketsTransmitted,
       "rtpStatsCurrentTotalPacketsReceived": rtpStatsCurrentTotalPacketsReceived,
       "rtpStatsCurrentTotalPacketsLost": rtpStatsCurrentTotalPacketsLost,
       "rtpStatsCurrentTotalPercentPacketsLost": rtpStatsCurrentTotalPercentPacketsLost,
       "rtpStatsCurrentTotalInterarrivalJitterMin": rtpStatsCurrentTotalInterarrivalJitterMin,
       "rtpStatsCurrentTotalInterarrivalJitterMax": rtpStatsCurrentTotalInterarrivalJitterMax,
       "rtpStatsCurrentTotalInterarrivalJitterAvg": rtpStatsCurrentTotalInterarrivalJitterAvg,
       "rtpStatsCurrentTotalLatencyMin": rtpStatsCurrentTotalLatencyMin,
       "rtpStatsCurrentTotalLatencyMax": rtpStatsCurrentTotalLatencyMax,
       "rtpStatsCurrentTotalLatencyAvg": rtpStatsCurrentTotalLatencyAvg,
       "rtpStatsCumulatedStatistics": rtpStatsCumulatedStatistics,
       "rtpStatsCumulatedTotalOctetsTransmitted": rtpStatsCumulatedTotalOctetsTransmitted,
       "rtpStatsCumulatedTotalOctetsReceived": rtpStatsCumulatedTotalOctetsReceived,
       "rtpStatsCumulatedTotalPacketsTransmitted": rtpStatsCumulatedTotalPacketsTransmitted,
       "rtpStatsCumulatedTotalPacketsReceived": rtpStatsCumulatedTotalPacketsReceived,
       "rtpStatsCumulatedTotalPacketsLost": rtpStatsCumulatedTotalPacketsLost,
       "rtpStatsCumulatedTotalPercentPacketsLost": rtpStatsCumulatedTotalPercentPacketsLost,
       "rtpStatsCumulatedTotalInterarrivalJitterMin": rtpStatsCumulatedTotalInterarrivalJitterMin,
       "rtpStatsCumulatedTotalInterarrivalJitterMax": rtpStatsCumulatedTotalInterarrivalJitterMax,
       "rtpStatsCumulatedTotalInterarrivalJitterAvg": rtpStatsCumulatedTotalInterarrivalJitterAvg,
       "rtpStatsCumulatedTotalLatencyMin": rtpStatsCumulatedTotalLatencyMin,
       "rtpStatsCumulatedTotalLatencyMax": rtpStatsCumulatedTotalLatencyMax,
       "rtpStatsCumulatedTotalLatencyAvg": rtpStatsCumulatedTotalLatencyAvg,
       "rtpConformance": rtpConformance,
       "rtpCompliances": rtpCompliances,
       "rtpBasicComplVer1": rtpBasicComplVer1,
       "rtpGroups": rtpGroups,
       "rtpStatsBasicGroupVer1": rtpStatsBasicGroupVer1,
       "rtpConfigBasicGroupVer1": rtpConfigBasicGroupVer1,
       "rtpConfig": rtpConfig,
       "rtpConfigBasePort": rtpConfigBasePort}
)
