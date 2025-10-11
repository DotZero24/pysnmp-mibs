# SNMP MIB module (HIRSCHMANN-WAN-GPS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/hirschmann/HIRSCHMANN-WAN-GPS-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 18:54:38 2025
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

(hmWanMgmt,) = mibBuilder.importSymbols(
    "HIRSCHMANN-WAN-MIB",
    "hmWanMgmt")

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

hmWanGpsMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 248, 40, 1, 7)
)
if mibBuilder.loadTexts:
    hmWanGpsMib.setRevisions(
        ("2015-02-13 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HmWanGpsTimeUTC_Type = OctetString
_HmWanGpsTimeUTC_Object = MibScalar
hmWanGpsTimeUTC = _HmWanGpsTimeUTC_Object(
    (1, 3, 6, 1, 4, 1, 248, 40, 1, 7, 1),
    _HmWanGpsTimeUTC_Type()
)
hmWanGpsTimeUTC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmWanGpsTimeUTC.setStatus("current")
_HmWanGpsLatitude_Type = OctetString
_HmWanGpsLatitude_Object = MibScalar
hmWanGpsLatitude = _HmWanGpsLatitude_Object(
    (1, 3, 6, 1, 4, 1, 248, 40, 1, 7, 2),
    _HmWanGpsLatitude_Type()
)
hmWanGpsLatitude.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmWanGpsLatitude.setStatus("current")
_HmWanGpsLongitude_Type = OctetString
_HmWanGpsLongitude_Object = MibScalar
hmWanGpsLongitude = _HmWanGpsLongitude_Object(
    (1, 3, 6, 1, 4, 1, 248, 40, 1, 7, 3),
    _HmWanGpsLongitude_Type()
)
hmWanGpsLongitude.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmWanGpsLongitude.setStatus("current")
_HmWanGpsAltitude_Type = OctetString
_HmWanGpsAltitude_Object = MibScalar
hmWanGpsAltitude = _HmWanGpsAltitude_Object(
    (1, 3, 6, 1, 4, 1, 248, 40, 1, 7, 4),
    _HmWanGpsAltitude_Type()
)
hmWanGpsAltitude.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmWanGpsAltitude.setStatus("current")
_HmWanGpsSatellites_Type = Integer32
_HmWanGpsSatellites_Object = MibScalar
hmWanGpsSatellites = _HmWanGpsSatellites_Object(
    (1, 3, 6, 1, 4, 1, 248, 40, 1, 7, 5),
    _HmWanGpsSatellites_Type()
)
hmWanGpsSatellites.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmWanGpsSatellites.setStatus("current")
_HmWanGpsFixStatus_Type = OctetString
_HmWanGpsFixStatus_Object = MibScalar
hmWanGpsFixStatus = _HmWanGpsFixStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 40, 1, 7, 6),
    _HmWanGpsFixStatus_Type()
)
hmWanGpsFixStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmWanGpsFixStatus.setStatus("current")
_HmWanGpsSpeedOverGround_Type = OctetString
_HmWanGpsSpeedOverGround_Object = MibScalar
hmWanGpsSpeedOverGround = _HmWanGpsSpeedOverGround_Object(
    (1, 3, 6, 1, 4, 1, 248, 40, 1, 7, 7),
    _HmWanGpsSpeedOverGround_Type()
)
hmWanGpsSpeedOverGround.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmWanGpsSpeedOverGround.setStatus("current")
_HmWanGpsCourseOverGround_Type = OctetString
_HmWanGpsCourseOverGround_Object = MibScalar
hmWanGpsCourseOverGround = _HmWanGpsCourseOverGround_Object(
    (1, 3, 6, 1, 4, 1, 248, 40, 1, 7, 8),
    _HmWanGpsCourseOverGround_Type()
)
hmWanGpsCourseOverGround.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmWanGpsCourseOverGround.setStatus("current")
_HmWanGpsDate_Type = OctetString
_HmWanGpsDate_Object = MibScalar
hmWanGpsDate = _HmWanGpsDate_Object(
    (1, 3, 6, 1, 4, 1, 248, 40, 1, 7, 9),
    _HmWanGpsDate_Type()
)
hmWanGpsDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmWanGpsDate.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HIRSCHMANN-WAN-GPS-MIB",
    **{"hmWanGpsMib": hmWanGpsMib,
       "hmWanGpsTimeUTC": hmWanGpsTimeUTC,
       "hmWanGpsLatitude": hmWanGpsLatitude,
       "hmWanGpsLongitude": hmWanGpsLongitude,
       "hmWanGpsAltitude": hmWanGpsAltitude,
       "hmWanGpsSatellites": hmWanGpsSatellites,
       "hmWanGpsFixStatus": hmWanGpsFixStatus,
       "hmWanGpsSpeedOverGround": hmWanGpsSpeedOverGround,
       "hmWanGpsCourseOverGround": hmWanGpsCourseOverGround,
       "hmWanGpsDate": hmWanGpsDate}
)
