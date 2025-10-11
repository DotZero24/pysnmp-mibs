# SNMP MIB module (ELTEX-MES-IP-OSPF-IF-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/eltex/ELTEX-MES-IP-OSPF-IF-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:49:21 2025
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

(eltMes,) = mibBuilder.importSymbols(
    "ELTEX-MES",
    "eltMes")

(eltMesOspf,) = mibBuilder.importSymbols(
    "ELTEX-MES-IP",
    "eltMesOspf")

(PortList,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "PortList")

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


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_EltIpOspfIfTable_Object = MibTable
eltIpOspfIfTable = _EltIpOspfIfTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 91, 1, 2)
)
if mibBuilder.loadTexts:
    eltIpOspfIfTable.setStatus("current")
_EltIpOspfIfEntry_Object = MibTableRow
eltIpOspfIfEntry = _EltIpOspfIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 91, 1, 2, 1)
)
eltIpOspfIfEntry.setIndexNames(
    (0, "ELTEX-MES-IP-OSPF-IF-MIB", "eltOspfIfAddress"),
)
if mibBuilder.loadTexts:
    eltIpOspfIfEntry.setStatus("current")
_EltOspfIfAddress_Type = IpAddress
_EltOspfIfAddress_Object = MibTableColumn
eltOspfIfAddress = _EltOspfIfAddress_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 91, 1, 2, 1, 1),
    _EltOspfIfAddress_Type()
)
eltOspfIfAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltOspfIfAddress.setStatus("current")


class _EltOspfIfPassiveDefault_Type(TruthValue):
    """Custom type eltOspfIfPassiveDefault based on TruthValue"""
    defaultValue = 2


_EltOspfIfPassiveDefault_Type.__name__ = "TruthValue"
_EltOspfIfPassiveDefault_Object = MibTableColumn
eltOspfIfPassiveDefault = _EltOspfIfPassiveDefault_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 91, 1, 2, 1, 2),
    _EltOspfIfPassiveDefault_Type()
)
eltOspfIfPassiveDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltOspfIfPassiveDefault.setStatus("current")
_EltOspfIfPassiveList_Type = PortList
_EltOspfIfPassiveList_Object = MibTableColumn
eltOspfIfPassiveList = _EltOspfIfPassiveList_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 91, 1, 2, 1, 3),
    _EltOspfIfPassiveList_Type()
)
eltOspfIfPassiveList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltOspfIfPassiveList.setStatus("current")
_EltOspfIfStatus_Type = RowStatus
_EltOspfIfStatus_Object = MibTableColumn
eltOspfIfStatus = _EltOspfIfStatus_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 91, 1, 2, 1, 4),
    _EltOspfIfStatus_Type()
)
eltOspfIfStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eltOspfIfStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ELTEX-MES-IP-OSPF-IF-MIB",
    **{"eltIpOspfIfTable": eltIpOspfIfTable,
       "eltIpOspfIfEntry": eltIpOspfIfEntry,
       "eltOspfIfAddress": eltOspfIfAddress,
       "eltOspfIfPassiveDefault": eltOspfIfPassiveDefault,
       "eltOspfIfPassiveList": eltOspfIfPassiveList,
       "eltOspfIfStatus": eltOspfIfStatus}
)
