# SNMP MIB module (BRCM-USB-FACTORY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/broadcom/BRCM-USB-FACTORY-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:08:34 2025
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

(cableDataFactory,) = mibBuilder.importSymbols(
    "BRCM-CABLEDATA-FACTORY-MIB",
    "cableDataFactory")

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
 MacAddress,
 PhysAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

usbFactory = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 2, 8)
)
if mibBuilder.loadTexts:
    usbFactory.setRevisions(
        ("2007-02-05 00:00",
         "2004-11-12 00:00",
         "2004-08-25 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_UsbFactMacAddress_Type = MacAddress
_UsbFactMacAddress_Object = MibScalar
usbFactMacAddress = _UsbFactMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 2, 8, 1),
    _UsbFactMacAddress_Type()
)
usbFactMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usbFactMacAddress.setStatus("current")
_UsbFactVendorId_Type = Unsigned32
_UsbFactVendorId_Object = MibScalar
usbFactVendorId = _UsbFactVendorId_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 2, 8, 2),
    _UsbFactVendorId_Type()
)
usbFactVendorId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usbFactVendorId.setStatus("current")
_UsbFactDeviceId_Type = Unsigned32
_UsbFactDeviceId_Object = MibScalar
usbFactDeviceId = _UsbFactDeviceId_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 2, 8, 3),
    _UsbFactDeviceId_Type()
)
usbFactDeviceId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usbFactDeviceId.setStatus("current")
_UsbFactRNDISDriverEnable_Type = TruthValue
_UsbFactRNDISDriverEnable_Object = MibScalar
usbFactRNDISDriverEnable = _UsbFactRNDISDriverEnable_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 2, 8, 4),
    _UsbFactRNDISDriverEnable_Type()
)
usbFactRNDISDriverEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usbFactRNDISDriverEnable.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BRCM-USB-FACTORY-MIB",
    **{"usbFactory": usbFactory,
       "usbFactMacAddress": usbFactMacAddress,
       "usbFactVendorId": usbFactVendorId,
       "usbFactDeviceId": usbFactDeviceId,
       "usbFactRNDISDriverEnable": usbFactRNDISDriverEnable}
)
