# SNMP MIB module (ELTEX-MES-ISS-IPDB-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/eltex/ELTEX-MES-ISS-IPDB-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:48:15 2025
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

(fsIpDbBindingEntry,
 fsIpDbv6BindingEntry) = mibBuilder.importSymbols(
    "ARICENT-IPDB-MIB",
    "fsIpDbBindingEntry",
    "fsIpDbv6BindingEntry")

(eltMesIss,) = mibBuilder.importSymbols(
    "ELTEX-MES-ISS-MIB",
    "eltMesIss")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

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
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

eltMesIssIpDbMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 9)
)
if mibBuilder.loadTexts:
    eltMesIssIpDbMIB.setRevisions(
        ("2022-06-10 00:00",
         "2022-03-17 00:00",
         "2022-03-04 00:00",
         "2020-05-21 00:00",
         "2019-02-06 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_EltMesIssIpDbObjects_ObjectIdentity = ObjectIdentity
eltMesIssIpDbObjects = _EltMesIssIpDbObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 9, 1)
)
_EltMesIssIpDbInterfaces_ObjectIdentity = ObjectIdentity
eltMesIssIpDbInterfaces = _EltMesIssIpDbInterfaces_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 9, 1, 1)
)
_EltMesIssIpDbIntfConfTable_Object = MibTable
eltMesIssIpDbIntfConfTable = _EltMesIssIpDbIntfConfTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 9, 1, 1, 1)
)
if mibBuilder.loadTexts:
    eltMesIssIpDbIntfConfTable.setStatus("current")
_EltMesIssIpDbIntfConfEntry_Object = MibTableRow
eltMesIssIpDbIntfConfEntry = _EltMesIssIpDbIntfConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 9, 1, 1, 1, 1)
)
eltMesIssIpDbIntfConfEntry.setIndexNames(
    (0, "ELTEX-MES-ISS-IPDB-MIB", "eltMesIssIpDbIntfConfIndex"),
)
if mibBuilder.loadTexts:
    eltMesIssIpDbIntfConfEntry.setStatus("current")
_EltMesIssIpDbIntfConfIndex_Type = InterfaceIndex
_EltMesIssIpDbIntfConfIndex_Object = MibTableColumn
eltMesIssIpDbIntfConfIndex = _EltMesIssIpDbIntfConfIndex_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 9, 1, 1, 1, 1, 1),
    _EltMesIssIpDbIntfConfIndex_Type()
)
eltMesIssIpDbIntfConfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eltMesIssIpDbIntfConfIndex.setStatus("current")


class _EltMesIssIpDbIntfConfBindingLimit_Type(Unsigned32):
    """Custom type eltMesIssIpDbIntfConfBindingLimit based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_EltMesIssIpDbIntfConfBindingLimit_Type.__name__ = "Unsigned32"
_EltMesIssIpDbIntfConfBindingLimit_Object = MibTableColumn
eltMesIssIpDbIntfConfBindingLimit = _EltMesIssIpDbIntfConfBindingLimit_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 9, 1, 1, 1, 1, 2),
    _EltMesIssIpDbIntfConfBindingLimit_Type()
)
eltMesIssIpDbIntfConfBindingLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltMesIssIpDbIntfConfBindingLimit.setStatus("current")


class _EltMesIssIpDbIntfConfBindingLimitControl_Type(Integer32):
    """Custom type eltMesIssIpDbIntfConfBindingLimitControl based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_EltMesIssIpDbIntfConfBindingLimitControl_Type.__name__ = "Integer32"
_EltMesIssIpDbIntfConfBindingLimitControl_Object = MibTableColumn
eltMesIssIpDbIntfConfBindingLimitControl = _EltMesIssIpDbIntfConfBindingLimitControl_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 9, 1, 1, 1, 1, 3),
    _EltMesIssIpDbIntfConfBindingLimitControl_Type()
)
eltMesIssIpDbIntfConfBindingLimitControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltMesIssIpDbIntfConfBindingLimitControl.setStatus("current")
_EltMesIssIpDbIntfStatTable_Object = MibTable
eltMesIssIpDbIntfStatTable = _EltMesIssIpDbIntfStatTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 9, 1, 1, 2)
)
if mibBuilder.loadTexts:
    eltMesIssIpDbIntfStatTable.setStatus("current")
_EltMesIssIpDbIntfStatEntry_Object = MibTableRow
eltMesIssIpDbIntfStatEntry = _EltMesIssIpDbIntfStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 9, 1, 1, 2, 1)
)
eltMesIssIpDbIntfStatEntry.setIndexNames(
    (0, "ELTEX-MES-ISS-IPDB-MIB", "eltMesIssIpDbIntfStatIndex"),
)
if mibBuilder.loadTexts:
    eltMesIssIpDbIntfStatEntry.setStatus("current")
_EltMesIssIpDbIntfStatIndex_Type = InterfaceIndex
_EltMesIssIpDbIntfStatIndex_Object = MibTableColumn
eltMesIssIpDbIntfStatIndex = _EltMesIssIpDbIntfStatIndex_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 9, 1, 1, 2, 1, 1),
    _EltMesIssIpDbIntfStatIndex_Type()
)
eltMesIssIpDbIntfStatIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eltMesIssIpDbIntfStatIndex.setStatus("current")
_EltMesIssIpDbIntfStatNoOfStaticBindings_Type = Counter32
_EltMesIssIpDbIntfStatNoOfStaticBindings_Object = MibTableColumn
eltMesIssIpDbIntfStatNoOfStaticBindings = _EltMesIssIpDbIntfStatNoOfStaticBindings_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 9, 1, 1, 2, 1, 2),
    _EltMesIssIpDbIntfStatNoOfStaticBindings_Type()
)
eltMesIssIpDbIntfStatNoOfStaticBindings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltMesIssIpDbIntfStatNoOfStaticBindings.setStatus("current")
_EltMesIssIpDbIntfStatNoOfDHCPBindings_Type = Counter32
_EltMesIssIpDbIntfStatNoOfDHCPBindings_Object = MibTableColumn
eltMesIssIpDbIntfStatNoOfDHCPBindings = _EltMesIssIpDbIntfStatNoOfDHCPBindings_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 9, 1, 1, 2, 1, 3),
    _EltMesIssIpDbIntfStatNoOfDHCPBindings_Type()
)
eltMesIssIpDbIntfStatNoOfDHCPBindings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltMesIssIpDbIntfStatNoOfDHCPBindings.setStatus("current")
_EltMesIssIpDbSrcGuardVlanTable_Object = MibTable
eltMesIssIpDbSrcGuardVlanTable = _EltMesIssIpDbSrcGuardVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 9, 1, 1, 3)
)
if mibBuilder.loadTexts:
    eltMesIssIpDbSrcGuardVlanTable.setStatus("current")
_EltMesIssIpDbSrcGuardVlanEntry_Object = MibTableRow
eltMesIssIpDbSrcGuardVlanEntry = _EltMesIssIpDbSrcGuardVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 9, 1, 1, 3, 1)
)
eltMesIssIpDbSrcGuardVlanEntry.setIndexNames(
    (0, "ELTEX-MES-ISS-IPDB-MIB", "eltMesIssIpDbSrcGuardVlanId"),
)
if mibBuilder.loadTexts:
    eltMesIssIpDbSrcGuardVlanEntry.setStatus("current")


class _EltMesIssIpDbSrcGuardVlanId_Type(Integer32):
    """Custom type eltMesIssIpDbSrcGuardVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_EltMesIssIpDbSrcGuardVlanId_Type.__name__ = "Integer32"
_EltMesIssIpDbSrcGuardVlanId_Object = MibTableColumn
eltMesIssIpDbSrcGuardVlanId = _EltMesIssIpDbSrcGuardVlanId_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 9, 1, 1, 3, 1, 1),
    _EltMesIssIpDbSrcGuardVlanId_Type()
)
eltMesIssIpDbSrcGuardVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eltMesIssIpDbSrcGuardVlanId.setStatus("current")


class _EltMesIssIpDbSrcGuardVlanStatus_Type(Integer32):
    """Custom type eltMesIssIpDbSrcGuardVlanStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_EltMesIssIpDbSrcGuardVlanStatus_Type.__name__ = "Integer32"
_EltMesIssIpDbSrcGuardVlanStatus_Object = MibTableColumn
eltMesIssIpDbSrcGuardVlanStatus = _EltMesIssIpDbSrcGuardVlanStatus_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 9, 1, 1, 3, 1, 2),
    _EltMesIssIpDbSrcGuardVlanStatus_Type()
)
eltMesIssIpDbSrcGuardVlanStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltMesIssIpDbSrcGuardVlanStatus.setStatus("current")


class _EltMesIssIpDbv6SrcGuardVlanStatus_Type(Integer32):
    """Custom type eltMesIssIpDbv6SrcGuardVlanStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_EltMesIssIpDbv6SrcGuardVlanStatus_Type.__name__ = "Integer32"
_EltMesIssIpDbv6SrcGuardVlanStatus_Object = MibTableColumn
eltMesIssIpDbv6SrcGuardVlanStatus = _EltMesIssIpDbv6SrcGuardVlanStatus_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 9, 1, 1, 3, 1, 3),
    _EltMesIssIpDbv6SrcGuardVlanStatus_Type()
)
eltMesIssIpDbv6SrcGuardVlanStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltMesIssIpDbv6SrcGuardVlanStatus.setStatus("current")
_EltMesIssIpDbBinding_ObjectIdentity = ObjectIdentity
eltMesIssIpDbBinding = _EltMesIssIpDbBinding_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 9, 1, 2)
)
_EltMesIssIpDbBindingTable_Object = MibTable
eltMesIssIpDbBindingTable = _EltMesIssIpDbBindingTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 9, 1, 2, 1)
)
if mibBuilder.loadTexts:
    eltMesIssIpDbBindingTable.setStatus("current")
_EltMesIssIpDbBindingEntry_Object = MibTableRow
eltMesIssIpDbBindingEntry = _EltMesIssIpDbBindingEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 9, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    eltMesIssIpDbBindingEntry.setStatus("current")


class _EltMesIssIpDbBindingEntryClearFlag_Type(TruthValue):
    """Custom type eltMesIssIpDbBindingEntryClearFlag based on TruthValue"""
    defaultValue = 2


_EltMesIssIpDbBindingEntryClearFlag_Type.__name__ = "TruthValue"
_EltMesIssIpDbBindingEntryClearFlag_Object = MibTableColumn
eltMesIssIpDbBindingEntryClearFlag = _EltMesIssIpDbBindingEntryClearFlag_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 9, 1, 2, 1, 1, 1),
    _EltMesIssIpDbBindingEntryClearFlag_Type()
)
eltMesIssIpDbBindingEntryClearFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltMesIssIpDbBindingEntryClearFlag.setStatus("current")


class _EltMesIssIpDbBindingDynamicEntriesPortDownAction_Type(Integer32):
    """Custom type eltMesIssIpDbBindingDynamicEntriesPortDownAction based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("retain", 1),
          ("clear", 2))
    )


_EltMesIssIpDbBindingDynamicEntriesPortDownAction_Type.__name__ = "Integer32"
_EltMesIssIpDbBindingDynamicEntriesPortDownAction_Object = MibScalar
eltMesIssIpDbBindingDynamicEntriesPortDownAction = _EltMesIssIpDbBindingDynamicEntriesPortDownAction_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 9, 1, 2, 2),
    _EltMesIssIpDbBindingDynamicEntriesPortDownAction_Type()
)
eltMesIssIpDbBindingDynamicEntriesPortDownAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltMesIssIpDbBindingDynamicEntriesPortDownAction.setStatus("current")
_EltMesIssIpDbv6Binding_ObjectIdentity = ObjectIdentity
eltMesIssIpDbv6Binding = _EltMesIssIpDbv6Binding_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 9, 1, 3)
)
_EltMesIssIpDbv6BindingTable_Object = MibTable
eltMesIssIpDbv6BindingTable = _EltMesIssIpDbv6BindingTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 9, 1, 3, 1)
)
if mibBuilder.loadTexts:
    eltMesIssIpDbv6BindingTable.setStatus("current")
_EltMesIssIpDbv6BindingEntry_Object = MibTableRow
eltMesIssIpDbv6BindingEntry = _EltMesIssIpDbv6BindingEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 9, 1, 3, 1, 1)
)
if mibBuilder.loadTexts:
    eltMesIssIpDbv6BindingEntry.setStatus("current")


class _EltMesIssIpDbv6BindingEntryClearFlag_Type(TruthValue):
    """Custom type eltMesIssIpDbv6BindingEntryClearFlag based on TruthValue"""
    defaultValue = 2


_EltMesIssIpDbv6BindingEntryClearFlag_Type.__name__ = "TruthValue"
_EltMesIssIpDbv6BindingEntryClearFlag_Object = MibTableColumn
eltMesIssIpDbv6BindingEntryClearFlag = _EltMesIssIpDbv6BindingEntryClearFlag_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 9, 1, 3, 1, 1, 1),
    _EltMesIssIpDbv6BindingEntryClearFlag_Type()
)
eltMesIssIpDbv6BindingEntryClearFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltMesIssIpDbv6BindingEntryClearFlag.setStatus("current")
_EltMesIssIpDbNotifications_ObjectIdentity = ObjectIdentity
eltMesIssIpDbNotifications = _EltMesIssIpDbNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 9, 2)
)
fsIpDbBindingEntry.registerAugmentions(
    ("ELTEX-MES-ISS-IPDB-MIB",
     "eltMesIssIpDbBindingEntry")
)
eltMesIssIpDbBindingEntry.setIndexNames(*fsIpDbBindingEntry.getIndexNames())
fsIpDbv6BindingEntry.registerAugmentions(
    ("ELTEX-MES-ISS-IPDB-MIB",
     "eltMesIssIpDbv6BindingEntry")
)
eltMesIssIpDbv6BindingEntry.setIndexNames(*fsIpDbv6BindingEntry.getIndexNames())

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ELTEX-MES-ISS-IPDB-MIB",
    **{"eltMesIssIpDbMIB": eltMesIssIpDbMIB,
       "eltMesIssIpDbObjects": eltMesIssIpDbObjects,
       "eltMesIssIpDbInterfaces": eltMesIssIpDbInterfaces,
       "eltMesIssIpDbIntfConfTable": eltMesIssIpDbIntfConfTable,
       "eltMesIssIpDbIntfConfEntry": eltMesIssIpDbIntfConfEntry,
       "eltMesIssIpDbIntfConfIndex": eltMesIssIpDbIntfConfIndex,
       "eltMesIssIpDbIntfConfBindingLimit": eltMesIssIpDbIntfConfBindingLimit,
       "eltMesIssIpDbIntfConfBindingLimitControl": eltMesIssIpDbIntfConfBindingLimitControl,
       "eltMesIssIpDbIntfStatTable": eltMesIssIpDbIntfStatTable,
       "eltMesIssIpDbIntfStatEntry": eltMesIssIpDbIntfStatEntry,
       "eltMesIssIpDbIntfStatIndex": eltMesIssIpDbIntfStatIndex,
       "eltMesIssIpDbIntfStatNoOfStaticBindings": eltMesIssIpDbIntfStatNoOfStaticBindings,
       "eltMesIssIpDbIntfStatNoOfDHCPBindings": eltMesIssIpDbIntfStatNoOfDHCPBindings,
       "eltMesIssIpDbSrcGuardVlanTable": eltMesIssIpDbSrcGuardVlanTable,
       "eltMesIssIpDbSrcGuardVlanEntry": eltMesIssIpDbSrcGuardVlanEntry,
       "eltMesIssIpDbSrcGuardVlanId": eltMesIssIpDbSrcGuardVlanId,
       "eltMesIssIpDbSrcGuardVlanStatus": eltMesIssIpDbSrcGuardVlanStatus,
       "eltMesIssIpDbv6SrcGuardVlanStatus": eltMesIssIpDbv6SrcGuardVlanStatus,
       "eltMesIssIpDbBinding": eltMesIssIpDbBinding,
       "eltMesIssIpDbBindingTable": eltMesIssIpDbBindingTable,
       "eltMesIssIpDbBindingEntry": eltMesIssIpDbBindingEntry,
       "eltMesIssIpDbBindingEntryClearFlag": eltMesIssIpDbBindingEntryClearFlag,
       "eltMesIssIpDbBindingDynamicEntriesPortDownAction": eltMesIssIpDbBindingDynamicEntriesPortDownAction,
       "eltMesIssIpDbv6Binding": eltMesIssIpDbv6Binding,
       "eltMesIssIpDbv6BindingTable": eltMesIssIpDbv6BindingTable,
       "eltMesIssIpDbv6BindingEntry": eltMesIssIpDbv6BindingEntry,
       "eltMesIssIpDbv6BindingEntryClearFlag": eltMesIssIpDbv6BindingEntryClearFlag,
       "eltMesIssIpDbNotifications": eltMesIssIpDbNotifications}
)
