# SNMP MIB module (CAMBIUM-NETWORKS-INTERF-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/cambium/CAMBIUM-NETWORKS-INTERF-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:07:44 2025
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
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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

(DateAndTime,
 DisplayString,
 PhysAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

cnInterfaces = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 17713, 24, 11)
)
if mibBuilder.loadTexts:
    cnInterfaces.setRevisions(
        ("2022-05-26 00:00",
         "2021-11-30 00:00",
         "2021-04-08 18:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_IfCnTablePortLinkTransitions_Object = MibTable
ifCnTablePortLinkTransitions = _IfCnTablePortLinkTransitions_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 11, 1)
)
if mibBuilder.loadTexts:
    ifCnTablePortLinkTransitions.setStatus("current")
_IfCnEntry_Object = MibTableRow
ifCnEntry = _IfCnEntry_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 11, 1, 1)
)
ifCnEntry.setIndexNames(
    (0, "CAMBIUM-NETWORKS-INTERF-MIB", "ifCnIndex"),
)
if mibBuilder.loadTexts:
    ifCnEntry.setStatus("current")


class _IfCnIndex_Type(Integer32):
    """Custom type ifCnIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_IfCnIndex_Type.__name__ = "Integer32"
_IfCnIndex_Object = MibTableColumn
ifCnIndex = _IfCnIndex_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 11, 1, 1, 1),
    _IfCnIndex_Type()
)
ifCnIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifCnIndex.setStatus("current")
_IfCnPortLinkTransitions_Type = Gauge32
_IfCnPortLinkTransitions_Object = MibTableColumn
ifCnPortLinkTransitions = _IfCnPortLinkTransitions_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 11, 1, 1, 2),
    _IfCnPortLinkTransitions_Type()
)
ifCnPortLinkTransitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifCnPortLinkTransitions.setStatus("current")
_IfCnPortCpuStatisticsTable_Object = MibTable
ifCnPortCpuStatisticsTable = _IfCnPortCpuStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 11, 2)
)
if mibBuilder.loadTexts:
    ifCnPortCpuStatisticsTable.setStatus("current")
_IfCnCpuEntry_Object = MibTableRow
ifCnCpuEntry = _IfCnCpuEntry_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 11, 2, 1)
)
ifCnCpuEntry.setIndexNames(
    (0, "CAMBIUM-NETWORKS-INTERF-MIB", "ifCnCpuIndex"),
)
if mibBuilder.loadTexts:
    ifCnCpuEntry.setStatus("current")


class _IfCnCpuIndex_Type(Integer32):
    """Custom type ifCnCpuIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_IfCnCpuIndex_Type.__name__ = "Integer32"
_IfCnCpuIndex_Object = MibTableColumn
ifCnCpuIndex = _IfCnCpuIndex_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 11, 2, 1, 1),
    _IfCnCpuIndex_Type()
)
ifCnCpuIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifCnCpuIndex.setStatus("current")
_IfCnCpuRxUcastPkts_Type = Counter32
_IfCnCpuRxUcastPkts_Object = MibTableColumn
ifCnCpuRxUcastPkts = _IfCnCpuRxUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 11, 2, 1, 2),
    _IfCnCpuRxUcastPkts_Type()
)
ifCnCpuRxUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifCnCpuRxUcastPkts.setStatus("current")
_IfCnCpuRxMcastPkts_Type = Counter32
_IfCnCpuRxMcastPkts_Object = MibTableColumn
ifCnCpuRxMcastPkts = _IfCnCpuRxMcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 11, 2, 1, 3),
    _IfCnCpuRxMcastPkts_Type()
)
ifCnCpuRxMcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifCnCpuRxMcastPkts.setStatus("current")
_IfCnCpuRxBcastPkts_Type = Counter32
_IfCnCpuRxBcastPkts_Object = MibTableColumn
ifCnCpuRxBcastPkts = _IfCnCpuRxBcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 11, 2, 1, 4),
    _IfCnCpuRxBcastPkts_Type()
)
ifCnCpuRxBcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifCnCpuRxBcastPkts.setStatus("current")
_IfCnCpuRxArpPkts_Type = Counter32
_IfCnCpuRxArpPkts_Object = MibTableColumn
ifCnCpuRxArpPkts = _IfCnCpuRxArpPkts_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 11, 2, 1, 5),
    _IfCnCpuRxArpPkts_Type()
)
ifCnCpuRxArpPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifCnCpuRxArpPkts.setStatus("current")
_IfCnCpuRxIgmpPkts_Type = Counter32
_IfCnCpuRxIgmpPkts_Object = MibTableColumn
ifCnCpuRxIgmpPkts = _IfCnCpuRxIgmpPkts_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 11, 2, 1, 6),
    _IfCnCpuRxIgmpPkts_Type()
)
ifCnCpuRxIgmpPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifCnCpuRxIgmpPkts.setStatus("current")
_IfCnCpuRxIpMcastPkts_Type = Counter32
_IfCnCpuRxIpMcastPkts_Object = MibTableColumn
ifCnCpuRxIpMcastPkts = _IfCnCpuRxIpMcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 11, 2, 1, 7),
    _IfCnCpuRxIpMcastPkts_Type()
)
ifCnCpuRxIpMcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifCnCpuRxIpMcastPkts.setStatus("current")
_IfCnCpuRxStpPkts_Type = Counter32
_IfCnCpuRxStpPkts_Object = MibTableColumn
ifCnCpuRxStpPkts = _IfCnCpuRxStpPkts_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 11, 2, 1, 8),
    _IfCnCpuRxStpPkts_Type()
)
ifCnCpuRxStpPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifCnCpuRxStpPkts.setStatus("current")
_IfCnCpuRxLldpPkts_Type = Counter32
_IfCnCpuRxLldpPkts_Object = MibTableColumn
ifCnCpuRxLldpPkts = _IfCnCpuRxLldpPkts_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 11, 2, 1, 9),
    _IfCnCpuRxLldpPkts_Type()
)
ifCnCpuRxLldpPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifCnCpuRxLldpPkts.setStatus("current")
_IfCnCpuRxDhcpPkts_Type = Counter32
_IfCnCpuRxDhcpPkts_Object = MibTableColumn
ifCnCpuRxDhcpPkts = _IfCnCpuRxDhcpPkts_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 11, 2, 1, 10),
    _IfCnCpuRxDhcpPkts_Type()
)
ifCnCpuRxDhcpPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifCnCpuRxDhcpPkts.setStatus("current")
_IfCnCpuRxOtherPkts_Type = Counter32
_IfCnCpuRxOtherPkts_Object = MibTableColumn
ifCnCpuRxOtherPkts = _IfCnCpuRxOtherPkts_Object(
    (1, 3, 6, 1, 4, 1, 17713, 24, 11, 2, 1, 11),
    _IfCnCpuRxOtherPkts_Type()
)
ifCnCpuRxOtherPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifCnCpuRxOtherPkts.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CAMBIUM-NETWORKS-INTERF-MIB",
    **{"cnInterfaces": cnInterfaces,
       "ifCnTablePortLinkTransitions": ifCnTablePortLinkTransitions,
       "ifCnEntry": ifCnEntry,
       "ifCnIndex": ifCnIndex,
       "ifCnPortLinkTransitions": ifCnPortLinkTransitions,
       "ifCnPortCpuStatisticsTable": ifCnPortCpuStatisticsTable,
       "ifCnCpuEntry": ifCnCpuEntry,
       "ifCnCpuIndex": ifCnCpuIndex,
       "ifCnCpuRxUcastPkts": ifCnCpuRxUcastPkts,
       "ifCnCpuRxMcastPkts": ifCnCpuRxMcastPkts,
       "ifCnCpuRxBcastPkts": ifCnCpuRxBcastPkts,
       "ifCnCpuRxArpPkts": ifCnCpuRxArpPkts,
       "ifCnCpuRxIgmpPkts": ifCnCpuRxIgmpPkts,
       "ifCnCpuRxIpMcastPkts": ifCnCpuRxIpMcastPkts,
       "ifCnCpuRxStpPkts": ifCnCpuRxStpPkts,
       "ifCnCpuRxLldpPkts": ifCnCpuRxLldpPkts,
       "ifCnCpuRxDhcpPkts": ifCnCpuRxDhcpPkts,
       "ifCnCpuRxOtherPkts": ifCnCpuRxOtherPkts}
)
