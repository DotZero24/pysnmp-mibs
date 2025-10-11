# SNMP MIB module (PDN-DEVICE-TIME-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/paradyne/PDN-DEVICE-TIME-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:00:46 2025
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

(pdn_time,) = mibBuilder.importSymbols(
    "PDN-HEADER-MIB",
    "pdn-time")

(NTPMode,) = mibBuilder.importSymbols(
    "PDN-TC",
    "NTPMode")

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

(DateAndTime,
 DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_DevTimeMIBObjects_ObjectIdentity = ObjectIdentity
devTimeMIBObjects = _DevTimeMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 20, 1)
)
_DevTimeAndDate_ObjectIdentity = ObjectIdentity
devTimeAndDate = _DevTimeAndDate_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 20, 1, 1)
)
_DevDateAndTime_Type = DateAndTime
_DevDateAndTime_Object = MibScalar
devDateAndTime = _DevDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 20, 1, 1, 1),
    _DevDateAndTime_Type()
)
devDateAndTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    devDateAndTime.setStatus("mandatory")
_DevNTP_ObjectIdentity = ObjectIdentity
devNTP = _DevNTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 20, 1, 2)
)
_DevNTPServerIP_Type = IpAddress
_DevNTPServerIP_Object = MibScalar
devNTPServerIP = _DevNTPServerIP_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 20, 1, 2, 1),
    _DevNTPServerIP_Type()
)
devNTPServerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    devNTPServerIP.setStatus("mandatory")
_DevNTPMode_Type = NTPMode
_DevNTPMode_Object = MibScalar
devNTPMode = _DevNTPMode_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 20, 1, 2, 2),
    _DevNTPMode_Type()
)
devNTPMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    devNTPMode.setStatus("mandatory")


class _DevNTPSynchronised_Type(Integer32):
    """Custom type devNTPSynchronised based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_DevNTPSynchronised_Type.__name__ = "Integer32"
_DevNTPSynchronised_Object = MibScalar
devNTPSynchronised = _DevNTPSynchronised_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 20, 1, 2, 3),
    _DevNTPSynchronised_Type()
)
devNTPSynchronised.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    devNTPSynchronised.setStatus("mandatory")


class _DevNTPEnable_Type(Integer32):
    """Custom type devNTPEnable based on Integer32"""
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


_DevNTPEnable_Type.__name__ = "Integer32"
_DevNTPEnable_Object = MibScalar
devNTPEnable = _DevNTPEnable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 20, 1, 2, 4),
    _DevNTPEnable_Type()
)
devNTPEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    devNTPEnable.setStatus("mandatory")
_DevNTPOffsetFromUTC_Type = Integer32
_DevNTPOffsetFromUTC_Object = MibScalar
devNTPOffsetFromUTC = _DevNTPOffsetFromUTC_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 20, 1, 2, 5),
    _DevNTPOffsetFromUTC_Type()
)
devNTPOffsetFromUTC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    devNTPOffsetFromUTC.setStatus("mandatory")
_DevTimeMIBTraps_ObjectIdentity = ObjectIdentity
devTimeMIBTraps = _DevTimeMIBTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 20, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PDN-DEVICE-TIME-MIB",
    **{"devTimeMIBObjects": devTimeMIBObjects,
       "devTimeAndDate": devTimeAndDate,
       "devDateAndTime": devDateAndTime,
       "devNTP": devNTP,
       "devNTPServerIP": devNTPServerIP,
       "devNTPMode": devNTPMode,
       "devNTPSynchronised": devNTPSynchronised,
       "devNTPEnable": devNTPEnable,
       "devNTPOffsetFromUTC": devNTPOffsetFromUTC,
       "devTimeMIBTraps": devTimeMIBTraps}
)
