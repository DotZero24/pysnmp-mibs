# SNMP MIB module (RAISECOM-NMS-ACC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/raisecom/RAISECOM-NMS-ACC-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:37:06 2025
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

(raisecomAgent,) = mibBuilder.importSymbols(
    "RAISECOM-BASE-MIB",
    "raisecomAgent")

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
 enterprises,
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
    "enterprises",
    "iso")

(DisplayString,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

raisecomNMSAccessControl = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 1, 5)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RaisecomNMSACPAddressTable_Object = MibTable
raisecomNMSACPAddressTable = _RaisecomNMSACPAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 5, 1)
)
if mibBuilder.loadTexts:
    raisecomNMSACPAddressTable.setStatus("current")
_RaisecomNMSACPAddressEntry_Object = MibTableRow
raisecomNMSACPAddressEntry = _RaisecomNMSACPAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 5, 1, 1)
)
raisecomNMSACPAddressEntry.setIndexNames(
    (0, "RAISECOM-NMS-ACC-MIB", "raisecomNMSACPAddrIndex"),
)
if mibBuilder.loadTexts:
    raisecomNMSACPAddressEntry.setStatus("current")


class _RaisecomNMSACPAddrIndex_Type(Integer32):
    """Custom type raisecomNMSACPAddrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_RaisecomNMSACPAddrIndex_Type.__name__ = "Integer32"
_RaisecomNMSACPAddrIndex_Object = MibTableColumn
raisecomNMSACPAddrIndex = _RaisecomNMSACPAddrIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 5, 1, 1, 1),
    _RaisecomNMSACPAddrIndex_Type()
)
raisecomNMSACPAddrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomNMSACPAddrIndex.setStatus("current")
_RaisecomNMSACPAddrIPAddress_Type = IpAddress
_RaisecomNMSACPAddrIPAddress_Object = MibTableColumn
raisecomNMSACPAddrIPAddress = _RaisecomNMSACPAddrIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 5, 1, 1, 2),
    _RaisecomNMSACPAddrIPAddress_Type()
)
raisecomNMSACPAddrIPAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomNMSACPAddrIPAddress.setStatus("current")
_RaisecomNMSACPAddrNetMask_Type = IpAddress
_RaisecomNMSACPAddrNetMask_Object = MibTableColumn
raisecomNMSACPAddrNetMask = _RaisecomNMSACPAddrNetMask_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 5, 1, 1, 3),
    _RaisecomNMSACPAddrNetMask_Type()
)
raisecomNMSACPAddrNetMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomNMSACPAddrNetMask.setStatus("current")
_RaisecomNMSACPAddrRowStatus_Type = RowStatus
_RaisecomNMSACPAddrRowStatus_Object = MibTableColumn
raisecomNMSACPAddrRowStatus = _RaisecomNMSACPAddrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 5, 1, 1, 4),
    _RaisecomNMSACPAddrRowStatus_Type()
)
raisecomNMSACPAddrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomNMSACPAddrRowStatus.setStatus("current")


class _RaisecomTelnetAccessControlStatus_Type(Integer32):
    """Custom type raisecomTelnetAccessControlStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_RaisecomTelnetAccessControlStatus_Type.__name__ = "Integer32"
_RaisecomTelnetAccessControlStatus_Object = MibScalar
raisecomTelnetAccessControlStatus = _RaisecomTelnetAccessControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 5, 2),
    _RaisecomTelnetAccessControlStatus_Type()
)
raisecomTelnetAccessControlStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomTelnetAccessControlStatus.setStatus("current")


class _RaisecomWebAccessControlStatus_Type(Integer32):
    """Custom type raisecomWebAccessControlStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_RaisecomWebAccessControlStatus_Type.__name__ = "Integer32"
_RaisecomWebAccessControlStatus_Object = MibScalar
raisecomWebAccessControlStatus = _RaisecomWebAccessControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 5, 3),
    _RaisecomWebAccessControlStatus_Type()
)
raisecomWebAccessControlStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomWebAccessControlStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RAISECOM-NMS-ACC-MIB",
    **{"raisecomNMSAccessControl": raisecomNMSAccessControl,
       "raisecomNMSACPAddressTable": raisecomNMSACPAddressTable,
       "raisecomNMSACPAddressEntry": raisecomNMSACPAddressEntry,
       "raisecomNMSACPAddrIndex": raisecomNMSACPAddrIndex,
       "raisecomNMSACPAddrIPAddress": raisecomNMSACPAddrIPAddress,
       "raisecomNMSACPAddrNetMask": raisecomNMSACPAddrNetMask,
       "raisecomNMSACPAddrRowStatus": raisecomNMSACPAddrRowStatus,
       "raisecomTelnetAccessControlStatus": raisecomTelnetAccessControlStatus,
       "raisecomWebAccessControlStatus": raisecomWebAccessControlStatus}
)
