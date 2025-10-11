# SNMP MIB module (H3C-NPV-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/h3c/H3C-NPV-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:20:49 2025
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

(H3cFcVsanIndex,) = mibBuilder.importSymbols(
    "H3C-FC-TC-MIB",
    "H3cFcVsanIndex")

(h3cSan,
 h3cVsanIndex) = mibBuilder.importSymbols(
    "H3C-VSAN-MIB",
    "h3cSan",
    "h3cVsanIndex")

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex")

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
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

h3cNpv = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 6)
)
if mibBuilder.loadTexts:
    h3cNpv.setRevisions(
        ("2014-07-21 00:00",
         "2013-04-02 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class H3cNpvIfIndexList(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 65535),
    )



# MIB Managed Objects in the order of their OIDs

_H3cNpvMibObjects_ObjectIdentity = ObjectIdentity
h3cNpvMibObjects = _H3cNpvMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 6, 1)
)
_H3cNpvConfiguration_ObjectIdentity = ObjectIdentity
h3cNpvConfiguration = _H3cNpvConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 6, 1, 1)
)
_H3cNpvGlobalObjects_ObjectIdentity = ObjectIdentity
h3cNpvGlobalObjects = _H3cNpvGlobalObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 6, 1, 1, 1)
)
_H3cNpvLoadbalanceVsan_Type = H3cFcVsanIndex
_H3cNpvLoadbalanceVsan_Object = MibScalar
h3cNpvLoadbalanceVsan = _H3cNpvLoadbalanceVsan_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 6, 1, 1, 1, 1),
    _H3cNpvLoadbalanceVsan_Type()
)
h3cNpvLoadbalanceVsan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cNpvLoadbalanceVsan.setStatus("current")
_H3cNpvTrafficMapConfigTable_Object = MibTable
h3cNpvTrafficMapConfigTable = _H3cNpvTrafficMapConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 6, 1, 1, 2)
)
if mibBuilder.loadTexts:
    h3cNpvTrafficMapConfigTable.setStatus("current")
_H3cNpvTrafficMapConfigEntry_Object = MibTableRow
h3cNpvTrafficMapConfigEntry = _H3cNpvTrafficMapConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 6, 1, 1, 2, 1)
)
h3cNpvTrafficMapConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "H3C-VSAN-MIB", "h3cVsanIndex"),
)
if mibBuilder.loadTexts:
    h3cNpvTrafficMapConfigEntry.setStatus("current")
_H3cNpvTrafficMapExternalIfIndexList_Type = H3cNpvIfIndexList
_H3cNpvTrafficMapExternalIfIndexList_Object = MibTableColumn
h3cNpvTrafficMapExternalIfIndexList = _H3cNpvTrafficMapExternalIfIndexList_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 6, 1, 1, 2, 1, 1),
    _H3cNpvTrafficMapExternalIfIndexList_Type()
)
h3cNpvTrafficMapExternalIfIndexList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cNpvTrafficMapExternalIfIndexList.setStatus("current")
_H3cNpvTrafficMapLastChange_Type = TimeStamp
_H3cNpvTrafficMapLastChange_Object = MibTableColumn
h3cNpvTrafficMapLastChange = _H3cNpvTrafficMapLastChange_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 6, 1, 1, 2, 1, 2),
    _H3cNpvTrafficMapLastChange_Type()
)
h3cNpvTrafficMapLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cNpvTrafficMapLastChange.setStatus("current")
_H3cNpvTrafficMapRowStatus_Type = RowStatus
_H3cNpvTrafficMapRowStatus_Object = MibTableColumn
h3cNpvTrafficMapRowStatus = _H3cNpvTrafficMapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 6, 1, 1, 2, 1, 3),
    _H3cNpvTrafficMapRowStatus_Type()
)
h3cNpvTrafficMapRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cNpvTrafficMapRowStatus.setStatus("current")
_H3cNpvServerIfTable_Object = MibTable
h3cNpvServerIfTable = _H3cNpvServerIfTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 6, 1, 1, 3)
)
if mibBuilder.loadTexts:
    h3cNpvServerIfTable.setStatus("current")
_H3cNpvServerIfEntry_Object = MibTableRow
h3cNpvServerIfEntry = _H3cNpvServerIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 6, 1, 1, 3, 1)
)
h3cNpvServerIfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "H3C-VSAN-MIB", "h3cVsanIndex"),
)
if mibBuilder.loadTexts:
    h3cNpvServerIfEntry.setStatus("current")
_H3cNpvExternalIfIndex_Type = InterfaceIndex
_H3cNpvExternalIfIndex_Object = MibTableColumn
h3cNpvExternalIfIndex = _H3cNpvExternalIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 6, 1, 1, 3, 1, 1),
    _H3cNpvExternalIfIndex_Type()
)
h3cNpvExternalIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cNpvExternalIfIndex.setStatus("current")
_H3cNpvLoadBalanceTable_Object = MibTable
h3cNpvLoadBalanceTable = _H3cNpvLoadBalanceTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 6, 1, 1, 4)
)
if mibBuilder.loadTexts:
    h3cNpvLoadBalanceTable.setStatus("current")
_H3cNpvLoadBalanceEntry_Object = MibTableRow
h3cNpvLoadBalanceEntry = _H3cNpvLoadBalanceEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 6, 1, 1, 4, 1)
)
h3cNpvLoadBalanceEntry.setIndexNames(
    (0, "H3C-VSAN-MIB", "h3cVsanIndex"),
)
if mibBuilder.loadTexts:
    h3cNpvLoadBalanceEntry.setStatus("current")


class _H3cNpvAutoLoadBalanceEnable_Type(TruthValue):
    """Custom type h3cNpvAutoLoadBalanceEnable based on TruthValue"""
    defaultValue = 2


_H3cNpvAutoLoadBalanceEnable_Type.__name__ = "TruthValue"
_H3cNpvAutoLoadBalanceEnable_Object = MibTableColumn
h3cNpvAutoLoadBalanceEnable = _H3cNpvAutoLoadBalanceEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 6, 1, 1, 4, 1, 1),
    _H3cNpvAutoLoadBalanceEnable_Type()
)
h3cNpvAutoLoadBalanceEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cNpvAutoLoadBalanceEnable.setStatus("current")


class _H3cNpvAutoLoadBalanceInterval_Type(Unsigned32):
    """Custom type h3cNpvAutoLoadBalanceInterval based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 300),
    )


_H3cNpvAutoLoadBalanceInterval_Type.__name__ = "Unsigned32"
_H3cNpvAutoLoadBalanceInterval_Object = MibTableColumn
h3cNpvAutoLoadBalanceInterval = _H3cNpvAutoLoadBalanceInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 6, 1, 1, 4, 1, 2),
    _H3cNpvAutoLoadBalanceInterval_Type()
)
h3cNpvAutoLoadBalanceInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cNpvAutoLoadBalanceInterval.setStatus("current")
if mibBuilder.loadTexts:
    h3cNpvAutoLoadBalanceInterval.setUnits("seconds")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "H3C-NPV-MIB",
    **{"H3cNpvIfIndexList": H3cNpvIfIndexList,
       "h3cNpv": h3cNpv,
       "h3cNpvMibObjects": h3cNpvMibObjects,
       "h3cNpvConfiguration": h3cNpvConfiguration,
       "h3cNpvGlobalObjects": h3cNpvGlobalObjects,
       "h3cNpvLoadbalanceVsan": h3cNpvLoadbalanceVsan,
       "h3cNpvTrafficMapConfigTable": h3cNpvTrafficMapConfigTable,
       "h3cNpvTrafficMapConfigEntry": h3cNpvTrafficMapConfigEntry,
       "h3cNpvTrafficMapExternalIfIndexList": h3cNpvTrafficMapExternalIfIndexList,
       "h3cNpvTrafficMapLastChange": h3cNpvTrafficMapLastChange,
       "h3cNpvTrafficMapRowStatus": h3cNpvTrafficMapRowStatus,
       "h3cNpvServerIfTable": h3cNpvServerIfTable,
       "h3cNpvServerIfEntry": h3cNpvServerIfEntry,
       "h3cNpvExternalIfIndex": h3cNpvExternalIfIndex,
       "h3cNpvLoadBalanceTable": h3cNpvLoadBalanceTable,
       "h3cNpvLoadBalanceEntry": h3cNpvLoadBalanceEntry,
       "h3cNpvAutoLoadBalanceEnable": h3cNpvAutoLoadBalanceEnable,
       "h3cNpvAutoLoadBalanceInterval": h3cNpvAutoLoadBalanceInterval}
)
