# SNMP MIB module (ELECTROLINE-COMMON-INVENTORY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/electroline/ELECTROLINE-COMMON-INVENTORY-MIB
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

(commonInventory,) = mibBuilder.importSymbols(
    "ELECTROLINE-COMMON-ROOT-MIB",
    "commonInventory")

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

_InvHwType_Type = Integer32
_InvHwType_Object = MibScalar
invHwType = _InvHwType_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 4, 1, 1),
    _InvHwType_Type()
)
invHwType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    invHwType.setStatus("current")
_InvHwMinorRev_Type = Integer32
_InvHwMinorRev_Object = MibScalar
invHwMinorRev = _InvHwMinorRev_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 4, 1, 2),
    _InvHwMinorRev_Type()
)
invHwMinorRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    invHwMinorRev.setStatus("current")
_InvHwMajorRev_Type = Integer32
_InvHwMajorRev_Object = MibScalar
invHwMajorRev = _InvHwMajorRev_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 4, 1, 3),
    _InvHwMajorRev_Type()
)
invHwMajorRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    invHwMajorRev.setStatus("current")
_InvHwDrvRev_Type = Integer32
_InvHwDrvRev_Object = MibScalar
invHwDrvRev = _InvHwDrvRev_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 4, 1, 4),
    _InvHwDrvRev_Type()
)
invHwDrvRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    invHwDrvRev.setStatus("current")


class _ModelNumber_Type(OctetString):
    """Custom type modelNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ModelNumber_Type.__name__ = "OctetString"
_ModelNumber_Object = MibScalar
modelNumber = _ModelNumber_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 4, 1, 5),
    _ModelNumber_Type()
)
modelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modelNumber.setStatus("current")
_ManufacturingInfo_ObjectIdentity = ObjectIdentity
manufacturingInfo = _ManufacturingInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 4, 1, 10)
)
if mibBuilder.loadTexts:
    manufacturingInfo.setStatus("current")
_MfcDateTime_Type = DateAndTime
_MfcDateTime_Object = MibScalar
mfcDateTime = _MfcDateTime_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 4, 1, 10, 1),
    _MfcDateTime_Type()
)
mfcDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfcDateTime.setStatus("current")
_MfcTestSwVersion_Type = OctetString
_MfcTestSwVersion_Object = MibScalar
mfcTestSwVersion = _MfcTestSwVersion_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 4, 1, 10, 2),
    _MfcTestSwVersion_Type()
)
mfcTestSwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mfcTestSwVersion.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ELECTROLINE-COMMON-INVENTORY-MIB",
    **{"invHwType": invHwType,
       "invHwMinorRev": invHwMinorRev,
       "invHwMajorRev": invHwMajorRev,
       "invHwDrvRev": invHwDrvRev,
       "modelNumber": modelNumber,
       "manufacturingInfo": manufacturingInfo,
       "mfcDateTime": mfcDateTime,
       "mfcTestSwVersion": mfcTestSwVersion}
)
