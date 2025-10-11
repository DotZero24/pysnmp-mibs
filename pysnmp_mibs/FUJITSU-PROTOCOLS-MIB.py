# SNMP MIB module (FUJITSU-PROTOCOLS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/fujitsu/FUJITSU-PROTOCOLS-MIB
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

fUJITSU_PROTOCOLS_MIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 1100, 1000)
)
if mibBuilder.loadTexts:
    fUJITSU_PROTOCOLS_MIB.setRevisions(
        ("2016-04-01 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class ConfdString(TextualConvention, OctetString):
    status = "current"
    displayHint = "1t"


class String(TextualConvention, OctetString):
    status = "current"
    displayHint = "1t"


# MIB Managed Objects in the order of their OIDs

_Protocols_ObjectIdentity = ObjectIdentity
protocols = _Protocols_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 1100, 1000, 1)
)
_ProtocolsProtocolTable_Object = MibTable
protocolsProtocolTable = _ProtocolsProtocolTable_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 1100, 1000, 1, 1)
)
if mibBuilder.loadTexts:
    protocolsProtocolTable.setStatus("current")
_ProtocolsProtocolEntry_Object = MibTableRow
protocolsProtocolEntry = _ProtocolsProtocolEntry_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 1100, 1000, 1, 1, 1)
)
protocolsProtocolEntry.setIndexNames(
    (1, "FUJITSU-PROTOCOLS-MIB", "protocolsProtocolName"),
)
if mibBuilder.loadTexts:
    protocolsProtocolEntry.setStatus("current")
_ProtocolsProtocolName_Type = String
_ProtocolsProtocolName_Object = MibTableColumn
protocolsProtocolName = _ProtocolsProtocolName_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 1100, 1000, 1, 1, 1, 1),
    _ProtocolsProtocolName_Type()
)
protocolsProtocolName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    protocolsProtocolName.setStatus("current")
_ProtocolsProtocolType_Type = ConfdString
_ProtocolsProtocolType_Object = MibTableColumn
protocolsProtocolType = _ProtocolsProtocolType_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 1100, 1000, 1, 1, 1, 2),
    _ProtocolsProtocolType_Type()
)
protocolsProtocolType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    protocolsProtocolType.setStatus("current")
_ProtocolsProtocolRowstatus_Type = RowStatus
_ProtocolsProtocolRowstatus_Object = MibTableColumn
protocolsProtocolRowstatus = _ProtocolsProtocolRowstatus_Object(
    (1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 1100, 1000, 1, 1, 1, 3),
    _ProtocolsProtocolRowstatus_Type()
)
protocolsProtocolRowstatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    protocolsProtocolRowstatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FUJITSU-PROTOCOLS-MIB",
    **{"ConfdString": ConfdString,
       "String": String,
       "fUJITSU-PROTOCOLS-MIB": fUJITSU_PROTOCOLS_MIB,
       "protocols": protocols,
       "protocolsProtocolTable": protocolsProtocolTable,
       "protocolsProtocolEntry": protocolsProtocolEntry,
       "protocolsProtocolName": protocolsProtocolName,
       "protocolsProtocolType": protocolsProtocolType,
       "protocolsProtocolRowstatus": protocolsProtocolRowstatus}
)
