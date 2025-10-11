# SNMP MIB module (FUJITSU-LLDP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/fujitsu/FUJITSU-LLDP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:51:33 2025
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

(fssProtocols,) = mibBuilder.importSymbols(
    "FSS-COMMON-SMI",
    "fssProtocols")

(protocolsProtocolEntry,
 protocolsProtocolName) = mibBuilder.importSymbols(
    "FUJITSU-PROTOCOLS-MIB",
    "protocolsProtocolEntry",
    "protocolsProtocolName")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

fssLLDP = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 1100, 1100)
)
if mibBuilder.loadTexts:
    fssLLDP.setRevisions(
        ("2016-11-03 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class UnsignedByte(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )



class UnsignedShort(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



class InetAddressIP(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )



class String(TextualConvention, OctetString):
    status = "current"
    displayHint = "1t"


# MIB Managed Objects in the order of their OIDs

_ProtocolsProtocolFssLLDPTable_Object = MibTable
protocolsProtocolFssLLDPTable = _ProtocolsProtocolFssLLDPTable_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 1100, 1100, 1)
)
if mibBuilder.loadTexts:
    protocolsProtocolFssLLDPTable.setStatus("current")
_ProtocolsProtocolFssLLDPEntry_Object = MibTableRow
protocolsProtocolFssLLDPEntry = _ProtocolsProtocolFssLLDPEntry_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 1100, 1100, 1, 1)
)
if mibBuilder.loadTexts:
    protocolsProtocolFssLLDPEntry.setStatus("current")


class _Lldp_instanceGlobal_configAdminStatus_Type(Integer32):
    """Custom type lldp_instanceGlobal_configAdminStatus based on Integer32"""
    defaultValue = 1

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


_Lldp_instanceGlobal_configAdminStatus_Type.__name__ = "Integer32"
_Lldp_instanceGlobal_configAdminStatus_Object = MibTableColumn
lldp_instanceGlobal_configAdminStatus = _Lldp_instanceGlobal_configAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 1100, 1100, 1, 1, 1),
    _Lldp_instanceGlobal_configAdminStatus_Type()
)
lldp_instanceGlobal_configAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldp_instanceGlobal_configAdminStatus.setStatus("current")


class _Lldp_instanceGlobal_configMsgTxInterval_Type(UnsignedShort):
    """Custom type lldp_instanceGlobal_configMsgTxInterval based on UnsignedShort"""
    defaultValue = 30

    subtypeSpec = UnsignedShort.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 32768),
    )


_Lldp_instanceGlobal_configMsgTxInterval_Type.__name__ = "UnsignedShort"
_Lldp_instanceGlobal_configMsgTxInterval_Object = MibTableColumn
lldp_instanceGlobal_configMsgTxInterval = _Lldp_instanceGlobal_configMsgTxInterval_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 1100, 1100, 1, 1, 2),
    _Lldp_instanceGlobal_configMsgTxInterval_Type()
)
lldp_instanceGlobal_configMsgTxInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldp_instanceGlobal_configMsgTxInterval.setStatus("current")


class _Lldp_instanceGlobal_configMsgTxHoldMultiplier_Type(UnsignedByte):
    """Custom type lldp_instanceGlobal_configMsgTxHoldMultiplier based on UnsignedByte"""
    defaultValue = 4

    subtypeSpec = UnsignedByte.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 10),
    )


_Lldp_instanceGlobal_configMsgTxHoldMultiplier_Type.__name__ = "UnsignedByte"
_Lldp_instanceGlobal_configMsgTxHoldMultiplier_Object = MibTableColumn
lldp_instanceGlobal_configMsgTxHoldMultiplier = _Lldp_instanceGlobal_configMsgTxHoldMultiplier_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 1100, 1100, 1, 1, 3),
    _Lldp_instanceGlobal_configMsgTxHoldMultiplier_Type()
)
lldp_instanceGlobal_configMsgTxHoldMultiplier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldp_instanceGlobal_configMsgTxHoldMultiplier.setStatus("current")
_Lldp_instancePortTable_Object = MibTable
lldp_instancePortTable = _Lldp_instancePortTable_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 1100, 1100, 2)
)
if mibBuilder.loadTexts:
    lldp_instancePortTable.setStatus("current")
_Lldp_instancePortEntry_Object = MibTableRow
lldp_instancePortEntry = _Lldp_instancePortEntry_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 1100, 1100, 2, 1)
)
lldp_instancePortEntry.setIndexNames(
    (0, "FUJITSU-PROTOCOLS-MIB", "protocolsProtocolName"),
    (0, "FUJITSU-LLDP-MIB", "lldp-instancePortIfIndex"),
)
if mibBuilder.loadTexts:
    lldp_instancePortEntry.setStatus("current")


class _Lldp_instancePortIfIndex_Type(Integer32):
    """Custom type lldp_instancePortIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Lldp_instancePortIfIndex_Type.__name__ = "Integer32"
_Lldp_instancePortIfIndex_Object = MibTableColumn
lldp_instancePortIfIndex = _Lldp_instancePortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 1100, 1100, 2, 1, 1),
    _Lldp_instancePortIfIndex_Type()
)
lldp_instancePortIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lldp_instancePortIfIndex.setStatus("current")


class _Lldp_instancePortAdminStatus_Type(Integer32):
    """Custom type lldp_instancePortAdminStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("txandrx", 1),
          ("txonly", 2),
          ("rxonly", 3))
    )


_Lldp_instancePortAdminStatus_Type.__name__ = "Integer32"
_Lldp_instancePortAdminStatus_Object = MibTableColumn
lldp_instancePortAdminStatus = _Lldp_instancePortAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 1100, 1100, 2, 1, 2),
    _Lldp_instancePortAdminStatus_Type()
)
lldp_instancePortAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lldp_instancePortAdminStatus.setStatus("current")
_Lldp_instancePortRowstatus_Type = RowStatus
_Lldp_instancePortRowstatus_Object = MibTableColumn
lldp_instancePortRowstatus = _Lldp_instancePortRowstatus_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 1100, 1100, 2, 1, 3),
    _Lldp_instancePortRowstatus_Type()
)
lldp_instancePortRowstatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lldp_instancePortRowstatus.setStatus("current")
protocolsProtocolEntry.registerAugmentions(
    ("FUJITSU-LLDP-MIB",
     "protocolsProtocolFssLLDPEntry")
)
protocolsProtocolFssLLDPEntry.setIndexNames(*protocolsProtocolEntry.getIndexNames())

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FUJITSU-LLDP-MIB",
    **{"UnsignedByte": UnsignedByte,
       "UnsignedShort": UnsignedShort,
       "InetAddressIP": InetAddressIP,
       "String": String,
       "fssLLDP": fssLLDP,
       "protocolsProtocolFssLLDPTable": protocolsProtocolFssLLDPTable,
       "protocolsProtocolFssLLDPEntry": protocolsProtocolFssLLDPEntry,
       "lldp-instanceGlobal-configAdminStatus": lldp_instanceGlobal_configAdminStatus,
       "lldp-instanceGlobal-configMsgTxInterval": lldp_instanceGlobal_configMsgTxInterval,
       "lldp-instanceGlobal-configMsgTxHoldMultiplier": lldp_instanceGlobal_configMsgTxHoldMultiplier,
       "lldp-instancePortTable": lldp_instancePortTable,
       "lldp-instancePortEntry": lldp_instancePortEntry,
       "lldp-instancePortIfIndex": lldp_instancePortIfIndex,
       "lldp-instancePortAdminStatus": lldp_instancePortAdminStatus,
       "lldp-instancePortRowstatus": lldp_instancePortRowstatus}
)
