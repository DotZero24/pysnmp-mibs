# SNMP MIB module (HIRSCHMANN-WAN-INFO-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/hirschmann/HIRSCHMANN-WAN-INFO-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 18:54:47 2025
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

hmWanInfoMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 248, 40, 1, 6)
)
if mibBuilder.loadTexts:
    hmWanInfoMib.setRevisions(
        ("2016-08-09 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HmWanInfoProduct_Type = DisplayString
_HmWanInfoProduct_Object = MibScalar
hmWanInfoProduct = _HmWanInfoProduct_Object(
    (1, 3, 6, 1, 4, 1, 248, 40, 1, 6, 1),
    _HmWanInfoProduct_Type()
)
hmWanInfoProduct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmWanInfoProduct.setStatus("current")
_HmWanInfoFirmware_Type = DisplayString
_HmWanInfoFirmware_Object = MibScalar
hmWanInfoFirmware = _HmWanInfoFirmware_Object(
    (1, 3, 6, 1, 4, 1, 248, 40, 1, 6, 2),
    _HmWanInfoFirmware_Type()
)
hmWanInfoFirmware.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmWanInfoFirmware.setStatus("current")
_HmWanInfoSN_Type = DisplayString
_HmWanInfoSN_Object = MibScalar
hmWanInfoSN = _HmWanInfoSN_Object(
    (1, 3, 6, 1, 4, 1, 248, 40, 1, 6, 3),
    _HmWanInfoSN_Type()
)
hmWanInfoSN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmWanInfoSN.setStatus("current")
_HmWanInfoIMEI_Type = OctetString
_HmWanInfoIMEI_Object = MibScalar
hmWanInfoIMEI = _HmWanInfoIMEI_Object(
    (1, 3, 6, 1, 4, 1, 248, 40, 1, 6, 4),
    _HmWanInfoIMEI_Type()
)
hmWanInfoIMEI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmWanInfoIMEI.setStatus("current")
_HmWanInfoESN_Type = OctetString
_HmWanInfoESN_Object = MibScalar
hmWanInfoESN = _HmWanInfoESN_Object(
    (1, 3, 6, 1, 4, 1, 248, 40, 1, 6, 5),
    _HmWanInfoESN_Type()
)
hmWanInfoESN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmWanInfoESN.setStatus("current")
_HmWanInfoMEID_Type = OctetString
_HmWanInfoMEID_Object = MibScalar
hmWanInfoMEID = _HmWanInfoMEID_Object(
    (1, 3, 6, 1, 4, 1, 248, 40, 1, 6, 6),
    _HmWanInfoMEID_Type()
)
hmWanInfoMEID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmWanInfoMEID.setStatus("current")
_HmWanInfoICCID_Type = OctetString
_HmWanInfoICCID_Object = MibScalar
hmWanInfoICCID = _HmWanInfoICCID_Object(
    (1, 3, 6, 1, 4, 1, 248, 40, 1, 6, 7),
    _HmWanInfoICCID_Type()
)
hmWanInfoICCID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmWanInfoICCID.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HIRSCHMANN-WAN-INFO-MIB",
    **{"hmWanInfoMib": hmWanInfoMib,
       "hmWanInfoProduct": hmWanInfoProduct,
       "hmWanInfoFirmware": hmWanInfoFirmware,
       "hmWanInfoSN": hmWanInfoSN,
       "hmWanInfoIMEI": hmWanInfoIMEI,
       "hmWanInfoESN": hmWanInfoESN,
       "hmWanInfoMEID": hmWanInfoMEID,
       "hmWanInfoICCID": hmWanInfoICCID}
)
