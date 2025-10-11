# SNMP MIB module (ELECTROLINE-DVM-INVENTORY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/electroline/ELECTROLINE-DVM-INVENTORY-MIB
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

(dvmInventory,) = mibBuilder.importSymbols(
    "ELECTROLINE-DVM-ROOT-MIB",
    "dvmInventory")

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

_DvmInvHwType_Type = Integer32
_DvmInvHwType_Object = MibScalar
dvmInvHwType = _DvmInvHwType_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 3, 1, 1),
    _DvmInvHwType_Type()
)
dvmInvHwType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvmInvHwType.setStatus("current")
_DvmInvHwMinorRev_Type = Integer32
_DvmInvHwMinorRev_Object = MibScalar
dvmInvHwMinorRev = _DvmInvHwMinorRev_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 3, 1, 2),
    _DvmInvHwMinorRev_Type()
)
dvmInvHwMinorRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvmInvHwMinorRev.setStatus("current")
_DvmInvHwMajorRev_Type = Integer32
_DvmInvHwMajorRev_Object = MibScalar
dvmInvHwMajorRev = _DvmInvHwMajorRev_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 3, 1, 3),
    _DvmInvHwMajorRev_Type()
)
dvmInvHwMajorRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvmInvHwMajorRev.setStatus("current")
_DvmInvHwDrvRev_Type = Integer32
_DvmInvHwDrvRev_Object = MibScalar
dvmInvHwDrvRev = _DvmInvHwDrvRev_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 3, 1, 4),
    _DvmInvHwDrvRev_Type()
)
dvmInvHwDrvRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvmInvHwDrvRev.setStatus("current")


class _DvmModelNumber_Type(OctetString):
    """Custom type dvmModelNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DvmModelNumber_Type.__name__ = "OctetString"
_DvmModelNumber_Object = MibScalar
dvmModelNumber = _DvmModelNumber_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 3, 1, 5),
    _DvmModelNumber_Type()
)
dvmModelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvmModelNumber.setStatus("current")
_DvmManufacturingInfo_ObjectIdentity = ObjectIdentity
dvmManufacturingInfo = _DvmManufacturingInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 3, 1, 10)
)
if mibBuilder.loadTexts:
    dvmManufacturingInfo.setStatus("current")
_DvmMfcDateTime_Type = DateAndTime
_DvmMfcDateTime_Object = MibScalar
dvmMfcDateTime = _DvmMfcDateTime_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 3, 1, 10, 1),
    _DvmMfcDateTime_Type()
)
dvmMfcDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvmMfcDateTime.setStatus("current")
_DvmMfcTestSwVersion_Type = OctetString
_DvmMfcTestSwVersion_Object = MibScalar
dvmMfcTestSwVersion = _DvmMfcTestSwVersion_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 3, 1, 10, 2),
    _DvmMfcTestSwVersion_Type()
)
dvmMfcTestSwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvmMfcTestSwVersion.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ELECTROLINE-DVM-INVENTORY-MIB",
    **{"dvmInvHwType": dvmInvHwType,
       "dvmInvHwMinorRev": dvmInvHwMinorRev,
       "dvmInvHwMajorRev": dvmInvHwMajorRev,
       "dvmInvHwDrvRev": dvmInvHwDrvRev,
       "dvmModelNumber": dvmModelNumber,
       "dvmManufacturingInfo": dvmManufacturingInfo,
       "dvmMfcDateTime": dvmMfcDateTime,
       "dvmMfcTestSwVersion": dvmMfcTestSwVersion}
)
