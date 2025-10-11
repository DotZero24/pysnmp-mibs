# SNMP MIB module (SNMP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/nortel/SNMP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:19:12 2025
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

(ntEnterpriseDataTasmanMgmt,) = mibBuilder.importSymbols(
    "NT-ENTERPRISE-DATA-MIB",
    "ntEnterpriseDataTasmanMgmt")

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

nnsnmpMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 5)
)
if mibBuilder.loadTexts:
    nnsnmpMib.setRevisions(
        ("1999-04-23 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NnsnmpObjects_ObjectIdentity = ObjectIdentity
nnsnmpObjects = _NnsnmpObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 5, 1)
)


class _NnsnmpAgentType_Type(Integer32):
    """Custom type nnsnmpAgentType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("snmpV1", 2),
          ("snmpV2V1", 3),
          ("snmpV2cV1", 4))
    )


_NnsnmpAgentType_Type.__name__ = "Integer32"
_NnsnmpAgentType_Object = MibScalar
nnsnmpAgentType = _NnsnmpAgentType_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 5, 1, 1),
    _NnsnmpAgentType_Type()
)
nnsnmpAgentType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnsnmpAgentType.setStatus("current")


class _NnsnmpRmonSupported_Type(Integer32):
    """Custom type nnsnmpRmonSupported based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("supported", 1),
          ("not-supported", 2))
    )


_NnsnmpRmonSupported_Type.__name__ = "Integer32"
_NnsnmpRmonSupported_Object = MibScalar
nnsnmpRmonSupported = _NnsnmpRmonSupported_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 5, 1, 2),
    _NnsnmpRmonSupported_Type()
)
nnsnmpRmonSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnsnmpRmonSupported.setStatus("current")
_NnsnmpSourceAddress_Type = IpAddress
_NnsnmpSourceAddress_Object = MibScalar
nnsnmpSourceAddress = _NnsnmpSourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 5, 1, 3),
    _NnsnmpSourceAddress_Type()
)
nnsnmpSourceAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nnsnmpSourceAddress.setStatus("current")
_NnsnmpTrapRcvrTable_Object = MibTable
nnsnmpTrapRcvrTable = _NnsnmpTrapRcvrTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 5, 1, 4)
)
if mibBuilder.loadTexts:
    nnsnmpTrapRcvrTable.setStatus("current")
_NnsnmpTrapRcvrEntry_Object = MibTableRow
nnsnmpTrapRcvrEntry = _NnsnmpTrapRcvrEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 5, 1, 4, 1)
)
nnsnmpTrapRcvrEntry.setIndexNames(
    (0, "SNMP-MIB", "nnsnmpTrapRcvrIndex"),
)
if mibBuilder.loadTexts:
    nnsnmpTrapRcvrEntry.setStatus("current")
_NnsnmpTrapRcvrIndex_Type = Integer32
_NnsnmpTrapRcvrIndex_Object = MibTableColumn
nnsnmpTrapRcvrIndex = _NnsnmpTrapRcvrIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 5, 1, 4, 1, 1),
    _NnsnmpTrapRcvrIndex_Type()
)
nnsnmpTrapRcvrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnsnmpTrapRcvrIndex.setStatus("current")


class _NnsnmpTrapRcvrEntryStatus_Type(Integer32):
    """Custom type nnsnmpTrapRcvrEntryStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("valid", 1),
          ("invalid", 2))
    )


_NnsnmpTrapRcvrEntryStatus_Type.__name__ = "Integer32"
_NnsnmpTrapRcvrEntryStatus_Object = MibTableColumn
nnsnmpTrapRcvrEntryStatus = _NnsnmpTrapRcvrEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 5, 1, 4, 1, 2),
    _NnsnmpTrapRcvrEntryStatus_Type()
)
nnsnmpTrapRcvrEntryStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nnsnmpTrapRcvrEntryStatus.setStatus("current")
_NnsnmpTrapRcvrAddress_Type = IpAddress
_NnsnmpTrapRcvrAddress_Object = MibTableColumn
nnsnmpTrapRcvrAddress = _NnsnmpTrapRcvrAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 5, 1, 4, 1, 3),
    _NnsnmpTrapRcvrAddress_Type()
)
nnsnmpTrapRcvrAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nnsnmpTrapRcvrAddress.setStatus("current")


class _NnsnmpTrapRcvrCommunity_Type(DisplayString):
    """Custom type nnsnmpTrapRcvrCommunity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_NnsnmpTrapRcvrCommunity_Type.__name__ = "DisplayString"
_NnsnmpTrapRcvrCommunity_Object = MibTableColumn
nnsnmpTrapRcvrCommunity = _NnsnmpTrapRcvrCommunity_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 5, 1, 4, 1, 4),
    _NnsnmpTrapRcvrCommunity_Type()
)
nnsnmpTrapRcvrCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nnsnmpTrapRcvrCommunity.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SNMP-MIB",
    **{"nnsnmpMib": nnsnmpMib,
       "nnsnmpObjects": nnsnmpObjects,
       "nnsnmpAgentType": nnsnmpAgentType,
       "nnsnmpRmonSupported": nnsnmpRmonSupported,
       "nnsnmpSourceAddress": nnsnmpSourceAddress,
       "nnsnmpTrapRcvrTable": nnsnmpTrapRcvrTable,
       "nnsnmpTrapRcvrEntry": nnsnmpTrapRcvrEntry,
       "nnsnmpTrapRcvrIndex": nnsnmpTrapRcvrIndex,
       "nnsnmpTrapRcvrEntryStatus": nnsnmpTrapRcvrEntryStatus,
       "nnsnmpTrapRcvrAddress": nnsnmpTrapRcvrAddress,
       "nnsnmpTrapRcvrCommunity": nnsnmpTrapRcvrCommunity}
)
