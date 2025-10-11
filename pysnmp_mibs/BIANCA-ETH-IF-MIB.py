# SNMP MIB module (BIANCA-ETH-IF-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/bintec/BIANCA-ETH-IF-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:07:08 2025
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions



class Date(Integer32):
    """Custom type Date based on Integer32"""




class HexValue(Integer32):
    """Custom type HexValue based on Integer32"""




class PhysAddress(OctetString):
    """Custom type PhysAddress based on OctetString"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Bintec_ObjectIdentity = ObjectIdentity
bintec = _Bintec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 272)
)
_Bibo_ObjectIdentity = ObjectIdentity
bibo = _Bibo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 272, 4)
)
_Eth_ObjectIdentity = ObjectIdentity
eth = _Eth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 272, 4, 37)
)
_EthIfTable_Object = MibTable
ethIfTable = _EthIfTable_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 37, 1)
)
if mibBuilder.loadTexts:
    ethIfTable.setStatus("mandatory")
_EthIfEntry_Object = MibTableRow
ethIfEntry = _EthIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 37, 1, 1)
)
ethIfEntry.setIndexNames(
    (0, "BIANCA-ETH-IF-MIB", "ethIfIndex"),
)
if mibBuilder.loadTexts:
    ethIfEntry.setStatus("mandatory")
_EthIfIndex_Type = Integer32
_EthIfIndex_Object = MibTableColumn
ethIfIndex = _EthIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 37, 1, 1, 1),
    _EthIfIndex_Type()
)
ethIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethIfIndex.setStatus("mandatory")


class _EthIfPortGroup_Type(Integer32):
    """Custom type ethIfPortGroup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_EthIfPortGroup_Type.__name__ = "Integer32"
_EthIfPortGroup_Object = MibTableColumn
ethIfPortGroup = _EthIfPortGroup_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 37, 1, 1, 4),
    _EthIfPortGroup_Type()
)
ethIfPortGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethIfPortGroup.setStatus("mandatory")


class _EthIfMACSlot_Type(Integer32):
    """Custom type ethIfMACSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_EthIfMACSlot_Type.__name__ = "Integer32"
_EthIfMACSlot_Object = MibTableColumn
ethIfMACSlot = _EthIfMACSlot_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 37, 1, 1, 5),
    _EthIfMACSlot_Type()
)
ethIfMACSlot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethIfMACSlot.setStatus("mandatory")


class _EthIfMACUnit_Type(Integer32):
    """Custom type ethIfMACUnit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_EthIfMACUnit_Type.__name__ = "Integer32"
_EthIfMACUnit_Object = MibTableColumn
ethIfMACUnit = _EthIfMACUnit_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 37, 1, 1, 6),
    _EthIfMACUnit_Type()
)
ethIfMACUnit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethIfMACUnit.setStatus("mandatory")


class _EthIfAdminStatus_Type(Integer32):
    """Custom type ethIfAdminStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 1),
          ("up", 2))
    )


_EthIfAdminStatus_Type.__name__ = "Integer32"
_EthIfAdminStatus_Object = MibTableColumn
ethIfAdminStatus = _EthIfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 37, 1, 1, 7),
    _EthIfAdminStatus_Type()
)
ethIfAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethIfAdminStatus.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BIANCA-ETH-IF-MIB",
    **{"Date": Date,
       "HexValue": HexValue,
       "PhysAddress": PhysAddress,
       "bintec": bintec,
       "bibo": bibo,
       "eth": eth,
       "ethIfTable": ethIfTable,
       "ethIfEntry": ethIfEntry,
       "ethIfIndex": ethIfIndex,
       "ethIfPortGroup": ethIfPortGroup,
       "ethIfMACSlot": ethIfMACSlot,
       "ethIfMACUnit": ethIfMACUnit,
       "ethIfAdminStatus": ethIfAdminStatus}
)
