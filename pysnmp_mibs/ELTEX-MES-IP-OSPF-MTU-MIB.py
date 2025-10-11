# SNMP MIB module (ELTEX-MES-IP-OSPF-MTU-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/eltex/ELTEX-MES-IP-OSPF-MTU-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:51:12 2025
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

eltMesIpOspfMtu = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 4)
)
if mibBuilder.loadTexts:
    eltMesIpOspfMtu.setRevisions(
        ("2013-08-30 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_EltIpOspfMtuTable_Object = MibTable
eltIpOspfMtuTable = _EltIpOspfMtuTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 4, 1)
)
if mibBuilder.loadTexts:
    eltIpOspfMtuTable.setStatus("current")
_EltIpOspfMtuEntry_Object = MibTableRow
eltIpOspfMtuEntry = _EltIpOspfMtuEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 4, 1, 1)
)
eltIpOspfMtuEntry.setIndexNames(
    (0, "ELTEX-MES-IP-OSPF-MTU-MIB", "ipAddr"),
)
if mibBuilder.loadTexts:
    eltIpOspfMtuEntry.setStatus("current")
_IpAddr_Type = IpAddress
_IpAddr_Object = MibTableColumn
ipAddr = _IpAddr_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 4, 1, 1, 1),
    _IpAddr_Type()
)
ipAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipAddr.setStatus("deprecated")


class _IpOspfMtu_Type(Integer32):
    """Custom type ipOspfMtu based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(128, 10218),
    )


_IpOspfMtu_Type.__name__ = "Integer32"
_IpOspfMtu_Object = MibTableColumn
ipOspfMtu = _IpOspfMtu_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 4, 1, 1, 2),
    _IpOspfMtu_Type()
)
ipOspfMtu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipOspfMtu.setStatus("deprecated")
_IpOspfMtuRowStatus_Type = RowStatus
_IpOspfMtuRowStatus_Object = MibTableColumn
ipOspfMtuRowStatus = _IpOspfMtuRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 4, 1, 1, 3),
    _IpOspfMtuRowStatus_Type()
)
ipOspfMtuRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipOspfMtuRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ELTEX-MES-IP-OSPF-MTU-MIB",
    **{"eltMesIpOspfMtu": eltMesIpOspfMtu,
       "eltIpOspfMtuTable": eltIpOspfMtuTable,
       "eltIpOspfMtuEntry": eltIpOspfMtuEntry,
       "ipAddr": ipAddr,
       "ipOspfMtu": ipOspfMtu,
       "ipOspfMtuRowStatus": ipOspfMtuRowStatus}
)
