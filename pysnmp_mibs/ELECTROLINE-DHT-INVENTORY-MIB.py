# SNMP MIB module (ELECTROLINE-DHT-INVENTORY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/electroline/ELECTROLINE-DHT-INVENTORY-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:07:08 2025
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

(dhtInventory,) = mibBuilder.importSymbols(
    "ELECTROLINE-DHT-ROOT-MIB",
    "dhtInventory")

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

_DhtInvHwType_Type = Integer32
_DhtInvHwType_Object = MibScalar
dhtInvHwType = _DhtInvHwType_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 1, 1),
    _DhtInvHwType_Type()
)
dhtInvHwType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhtInvHwType.setStatus("current")
_DhtInvHwMinorRev_Type = Integer32
_DhtInvHwMinorRev_Object = MibScalar
dhtInvHwMinorRev = _DhtInvHwMinorRev_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 1, 2),
    _DhtInvHwMinorRev_Type()
)
dhtInvHwMinorRev.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhtInvHwMinorRev.setStatus("current")
_DhtInvHwMajorRev_Type = Integer32
_DhtInvHwMajorRev_Object = MibScalar
dhtInvHwMajorRev = _DhtInvHwMajorRev_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 1, 3),
    _DhtInvHwMajorRev_Type()
)
dhtInvHwMajorRev.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhtInvHwMajorRev.setStatus("current")
_DhtInvHwDrvRev_Type = Integer32
_DhtInvHwDrvRev_Object = MibScalar
dhtInvHwDrvRev = _DhtInvHwDrvRev_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 1, 4),
    _DhtInvHwDrvRev_Type()
)
dhtInvHwDrvRev.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhtInvHwDrvRev.setStatus("current")


class _DhtModelNumber_Type(OctetString):
    """Custom type dhtModelNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DhtModelNumber_Type.__name__ = "OctetString"
_DhtModelNumber_Object = MibScalar
dhtModelNumber = _DhtModelNumber_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 1, 5),
    _DhtModelNumber_Type()
)
dhtModelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhtModelNumber.setStatus("current")
_DhtManufacturingInfo_ObjectIdentity = ObjectIdentity
dhtManufacturingInfo = _DhtManufacturingInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 1, 10)
)
if mibBuilder.loadTexts:
    dhtManufacturingInfo.setStatus("current")
_DhtMfcDateTime_Type = DateAndTime
_DhtMfcDateTime_Object = MibScalar
dhtMfcDateTime = _DhtMfcDateTime_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 1, 10, 1),
    _DhtMfcDateTime_Type()
)
dhtMfcDateTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhtMfcDateTime.setStatus("current")
_DhtMfcTestSwVersion_Type = OctetString
_DhtMfcTestSwVersion_Object = MibScalar
dhtMfcTestSwVersion = _DhtMfcTestSwVersion_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 1, 10, 2),
    _DhtMfcTestSwVersion_Type()
)
dhtMfcTestSwVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhtMfcTestSwVersion.setStatus("current")
_DhtMfcJobNumber_Type = OctetString
_DhtMfcJobNumber_Object = MibScalar
dhtMfcJobNumber = _DhtMfcJobNumber_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 1, 10, 3),
    _DhtMfcJobNumber_Type()
)
dhtMfcJobNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhtMfcJobNumber.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ELECTROLINE-DHT-INVENTORY-MIB",
    **{"dhtInvHwType": dhtInvHwType,
       "dhtInvHwMinorRev": dhtInvHwMinorRev,
       "dhtInvHwMajorRev": dhtInvHwMajorRev,
       "dhtInvHwDrvRev": dhtInvHwDrvRev,
       "dhtModelNumber": dhtModelNumber,
       "dhtManufacturingInfo": dhtManufacturingInfo,
       "dhtMfcDateTime": dhtMfcDateTime,
       "dhtMfcTestSwVersion": dhtMfcTestSwVersion,
       "dhtMfcJobNumber": dhtMfcJobNumber}
)
