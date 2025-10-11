# SNMP MIB module (ELTEX-MES-ISS-MST-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/eltex/ELTEX-MES-ISS-MST-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:50:48 2025
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

(fsMstMstiPortEntry,) = mibBuilder.importSymbols(
    "ARICENT-MST-MIB",
    "fsMstMstiPortEntry")

(eltMesIssBridgeMIBObjects,) = mibBuilder.importSymbols(
    "ELTEX-MES-ISS-BRIDGE-MIB",
    "eltMesIssBridgeMIBObjects")

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


# MODULE-IDENTITY

eltMesIssMstMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 14, 1, 1)
)
if mibBuilder.loadTexts:
    eltMesIssMstMIB.setRevisions(
        ("2020-09-22 00:00",
         "2019-06-03 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class EltMesIssMstPendingConfigAction(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("commit", 1),
          ("revert", 2))
    )



# MIB Managed Objects in the order of their OIDs

_EltMesIssMstMIBObjects_ObjectIdentity = ObjectIdentity
eltMesIssMstMIBObjects = _EltMesIssMstMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 14, 1, 1, 1)
)
_EltMesIssMstGlobals_ObjectIdentity = ObjectIdentity
eltMesIssMstGlobals = _EltMesIssMstGlobals_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 14, 1, 1, 1, 1)
)
_EltMesIssMstConfigPending_ObjectIdentity = ObjectIdentity
eltMesIssMstConfigPending = _EltMesIssMstConfigPending_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 14, 1, 1, 1, 1, 1)
)
_EltMesIssMstPendingConfigAction_Type = EltMesIssMstPendingConfigAction
_EltMesIssMstPendingConfigAction_Object = MibScalar
eltMesIssMstPendingConfigAction = _EltMesIssMstPendingConfigAction_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 14, 1, 1, 1, 1, 1, 1),
    _EltMesIssMstPendingConfigAction_Type()
)
eltMesIssMstPendingConfigAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltMesIssMstPendingConfigAction.setStatus("current")


class _EltMesIssMstRegnNamePending_Type(OctetString):
    """Custom type eltMesIssMstRegnNamePending based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_EltMesIssMstRegnNamePending_Type.__name__ = "OctetString"
_EltMesIssMstRegnNamePending_Object = MibScalar
eltMesIssMstRegnNamePending = _EltMesIssMstRegnNamePending_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 14, 1, 1, 1, 1, 1, 2),
    _EltMesIssMstRegnNamePending_Type()
)
eltMesIssMstRegnNamePending.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltMesIssMstRegnNamePending.setStatus("current")


class _EltMesIssMstRegnVersionPending_Type(Integer32):
    """Custom type eltMesIssMstRegnVersionPending based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_EltMesIssMstRegnVersionPending_Type.__name__ = "Integer32"
_EltMesIssMstRegnVersionPending_Object = MibScalar
eltMesIssMstRegnVersionPending = _EltMesIssMstRegnVersionPending_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 14, 1, 1, 1, 1, 1, 3),
    _EltMesIssMstRegnVersionPending_Type()
)
eltMesIssMstRegnVersionPending.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltMesIssMstRegnVersionPending.setStatus("current")
_EltMesIssMstVlanMapPendingTable_Object = MibTable
eltMesIssMstVlanMapPendingTable = _EltMesIssMstVlanMapPendingTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 14, 1, 1, 1, 1, 1, 4)
)
if mibBuilder.loadTexts:
    eltMesIssMstVlanMapPendingTable.setStatus("current")
_EltMesIssMstVlanMapPendingEntry_Object = MibTableRow
eltMesIssMstVlanMapPendingEntry = _EltMesIssMstVlanMapPendingEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 14, 1, 1, 1, 1, 1, 4, 1)
)
eltMesIssMstVlanMapPendingEntry.setIndexNames(
    (0, "ELTEX-MES-ISS-MST-MIB", "eltMesIssMstInstanceId"),
)
if mibBuilder.loadTexts:
    eltMesIssMstVlanMapPendingEntry.setStatus("current")


class _EltMesIssMstInstanceId_Type(Integer32):
    """Custom type eltMesIssMstInstanceId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
        ValueRangeConstraint(4094, 4094),
    )


_EltMesIssMstInstanceId_Type.__name__ = "Integer32"
_EltMesIssMstInstanceId_Object = MibTableColumn
eltMesIssMstInstanceId = _EltMesIssMstInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 14, 1, 1, 1, 1, 1, 4, 1, 1),
    _EltMesIssMstInstanceId_Type()
)
eltMesIssMstInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eltMesIssMstInstanceId.setStatus("current")


class _EltMesIssMstVlanMapPending_Type(OctetString):
    """Custom type eltMesIssMstVlanMapPending based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_EltMesIssMstVlanMapPending_Type.__name__ = "OctetString"
_EltMesIssMstVlanMapPending_Object = MibTableColumn
eltMesIssMstVlanMapPending = _EltMesIssMstVlanMapPending_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 14, 1, 1, 1, 1, 1, 4, 1, 2),
    _EltMesIssMstVlanMapPending_Type()
)
eltMesIssMstVlanMapPending.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltMesIssMstVlanMapPending.setStatus("current")


class _EltMesIssMstVlanMap2kPending_Type(OctetString):
    """Custom type eltMesIssMstVlanMap2kPending based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_EltMesIssMstVlanMap2kPending_Type.__name__ = "OctetString"
_EltMesIssMstVlanMap2kPending_Object = MibTableColumn
eltMesIssMstVlanMap2kPending = _EltMesIssMstVlanMap2kPending_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 14, 1, 1, 1, 1, 1, 4, 1, 3),
    _EltMesIssMstVlanMap2kPending_Type()
)
eltMesIssMstVlanMap2kPending.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltMesIssMstVlanMap2kPending.setStatus("current")


class _EltMesIssMstVlanMap3kPending_Type(OctetString):
    """Custom type eltMesIssMstVlanMap3kPending based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_EltMesIssMstVlanMap3kPending_Type.__name__ = "OctetString"
_EltMesIssMstVlanMap3kPending_Object = MibTableColumn
eltMesIssMstVlanMap3kPending = _EltMesIssMstVlanMap3kPending_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 14, 1, 1, 1, 1, 1, 4, 1, 4),
    _EltMesIssMstVlanMap3kPending_Type()
)
eltMesIssMstVlanMap3kPending.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltMesIssMstVlanMap3kPending.setStatus("current")


class _EltMesIssMstVlanMap4kPending_Type(OctetString):
    """Custom type eltMesIssMstVlanMap4kPending based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_EltMesIssMstVlanMap4kPending_Type.__name__ = "OctetString"
_EltMesIssMstVlanMap4kPending_Object = MibTableColumn
eltMesIssMstVlanMap4kPending = _EltMesIssMstVlanMap4kPending_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 14, 1, 1, 1, 1, 1, 4, 1, 5),
    _EltMesIssMstVlanMap4kPending_Type()
)
eltMesIssMstVlanMap4kPending.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltMesIssMstVlanMap4kPending.setStatus("current")
_EltMesIssMstMstiConfig_ObjectIdentity = ObjectIdentity
eltMesIssMstMstiConfig = _EltMesIssMstMstiConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 14, 1, 1, 1, 1, 2)
)
_EltMesIssMstMstiPortTable_Object = MibTable
eltMesIssMstMstiPortTable = _EltMesIssMstMstiPortTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 14, 1, 1, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    eltMesIssMstMstiPortTable.setStatus("current")
_EltMesIssMstMstiPortEntry_Object = MibTableRow
eltMesIssMstMstiPortEntry = _EltMesIssMstMstiPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 14, 1, 1, 1, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    eltMesIssMstMstiPortEntry.setStatus("current")
_EltMesIssMstMstiRootGuard_Type = TruthValue
_EltMesIssMstMstiRootGuard_Object = MibTableColumn
eltMesIssMstMstiRootGuard = _EltMesIssMstMstiRootGuard_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 14, 1, 1, 1, 1, 2, 1, 1, 1),
    _EltMesIssMstMstiRootGuard_Type()
)
eltMesIssMstMstiRootGuard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltMesIssMstMstiRootGuard.setStatus("current")
fsMstMstiPortEntry.registerAugmentions(
    ("ELTEX-MES-ISS-MST-MIB",
     "eltMesIssMstMstiPortEntry")
)
eltMesIssMstMstiPortEntry.setIndexNames(*fsMstMstiPortEntry.getIndexNames())

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ELTEX-MES-ISS-MST-MIB",
    **{"EltMesIssMstPendingConfigAction": EltMesIssMstPendingConfigAction,
       "eltMesIssMstMIB": eltMesIssMstMIB,
       "eltMesIssMstMIBObjects": eltMesIssMstMIBObjects,
       "eltMesIssMstGlobals": eltMesIssMstGlobals,
       "eltMesIssMstConfigPending": eltMesIssMstConfigPending,
       "eltMesIssMstPendingConfigAction": eltMesIssMstPendingConfigAction,
       "eltMesIssMstRegnNamePending": eltMesIssMstRegnNamePending,
       "eltMesIssMstRegnVersionPending": eltMesIssMstRegnVersionPending,
       "eltMesIssMstVlanMapPendingTable": eltMesIssMstVlanMapPendingTable,
       "eltMesIssMstVlanMapPendingEntry": eltMesIssMstVlanMapPendingEntry,
       "eltMesIssMstInstanceId": eltMesIssMstInstanceId,
       "eltMesIssMstVlanMapPending": eltMesIssMstVlanMapPending,
       "eltMesIssMstVlanMap2kPending": eltMesIssMstVlanMap2kPending,
       "eltMesIssMstVlanMap3kPending": eltMesIssMstVlanMap3kPending,
       "eltMesIssMstVlanMap4kPending": eltMesIssMstVlanMap4kPending,
       "eltMesIssMstMstiConfig": eltMesIssMstMstiConfig,
       "eltMesIssMstMstiPortTable": eltMesIssMstMstiPortTable,
       "eltMesIssMstMstiPortEntry": eltMesIssMstMstiPortEntry,
       "eltMesIssMstMstiRootGuard": eltMesIssMstMstiRootGuard}
)
