# SNMP MIB module (ZXCESCARDPROP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/zte/ZXCESCARDPROP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:45:14 2025
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

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")

(zxPwCETH,) = mibBuilder.importSymbols(
    "ZTE-MASTER-MIB",
    "zxPwCETH")


# MODULE-IDENTITY

zxCesCardPropMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 3, 1, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ZxCesCardPropTable_Object = MibTable
zxCesCardPropTable = _ZxCesCardPropTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 3, 1, 1, 1)
)
if mibBuilder.loadTexts:
    zxCesCardPropTable.setStatus("current")
_ZxCesCardPropEntry_Object = MibTableRow
zxCesCardPropEntry = _ZxCesCardPropEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 3, 1, 1, 1, 1)
)
zxCesCardPropEntry.setIndexNames(
    (0, "ZXCESCARDPROP-MIB", "zxCesCardIndex"),
)
if mibBuilder.loadTexts:
    zxCesCardPropEntry.setStatus("current")
_ZxCesCardIndex_Type = InterfaceIndex
_ZxCesCardIndex_Object = MibTableColumn
zxCesCardIndex = _ZxCesCardIndex_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 3, 1, 1, 1, 1, 1),
    _ZxCesCardIndex_Type()
)
zxCesCardIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxCesCardIndex.setStatus("current")
_ZxCesCardPhysAddress_Type = PhysAddress
_ZxCesCardPhysAddress_Object = MibTableColumn
zxCesCardPhysAddress = _ZxCesCardPhysAddress_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 3, 1, 1, 1, 1, 2),
    _ZxCesCardPhysAddress_Type()
)
zxCesCardPhysAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxCesCardPhysAddress.setStatus("current")


class _ZxCesCardAddrType_Type(InetAddressType):
    """Custom type zxCesCardAddrType based on InetAddressType"""
    defaultValue = 1


_ZxCesCardAddrType_Type.__name__ = "InetAddressType"
_ZxCesCardAddrType_Object = MibTableColumn
zxCesCardAddrType = _ZxCesCardAddrType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 3, 1, 1, 1, 1, 3),
    _ZxCesCardAddrType_Type()
)
zxCesCardAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxCesCardAddrType.setStatus("current")
_ZxCesCardAddress_Type = InetAddress
_ZxCesCardAddress_Object = MibTableColumn
zxCesCardAddress = _ZxCesCardAddress_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 3, 1, 1, 1, 1, 4),
    _ZxCesCardAddress_Type()
)
zxCesCardAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxCesCardAddress.setStatus("current")
_ZxCesCardCfgInfoSend_Type = TruthValue
_ZxCesCardCfgInfoSend_Object = MibTableColumn
zxCesCardCfgInfoSend = _ZxCesCardCfgInfoSend_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 3, 1, 1, 1, 1, 5),
    _ZxCesCardCfgInfoSend_Type()
)
zxCesCardCfgInfoSend.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxCesCardCfgInfoSend.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZXCESCARDPROP-MIB",
    **{"zxCesCardPropMIB": zxCesCardPropMIB,
       "zxCesCardPropTable": zxCesCardPropTable,
       "zxCesCardPropEntry": zxCesCardPropEntry,
       "zxCesCardIndex": zxCesCardIndex,
       "zxCesCardPhysAddress": zxCesCardPhysAddress,
       "zxCesCardAddrType": zxCesCardAddrType,
       "zxCesCardAddress": zxCesCardAddress,
       "zxCesCardCfgInfoSend": zxCesCardCfgInfoSend}
)
