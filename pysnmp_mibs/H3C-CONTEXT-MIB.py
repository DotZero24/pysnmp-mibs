# SNMP MIB module (H3C-CONTEXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/h3c/H3C-CONTEXT-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:18:50 2025
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

(h3cCommon,) = mibBuilder.importSymbols(
    "HUAWEI-3COM-OID-MIB",
    "h3cCommon")

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

h3cContext = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 154)
)
if mibBuilder.loadTexts:
    h3cContext.setRevisions(
        ("2014-03-18 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_H3cContextTables_ObjectIdentity = ObjectIdentity
h3cContextTables = _H3cContextTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 154, 1)
)
_H3cContextControl_ObjectIdentity = ObjectIdentity
h3cContextControl = _H3cContextControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 154, 1, 1)
)
_H3cContextControlTable_Object = MibTable
h3cContextControlTable = _H3cContextControlTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 154, 1, 1, 1)
)
if mibBuilder.loadTexts:
    h3cContextControlTable.setStatus("current")
_H3cContextControlEntry_Object = MibTableRow
h3cContextControlEntry = _H3cContextControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 154, 1, 1, 1, 1)
)
h3cContextControlEntry.setIndexNames(
    (0, "H3C-CONTEXT-MIB", "h3cContextIndex"),
)
if mibBuilder.loadTexts:
    h3cContextControlEntry.setStatus("current")


class _H3cContextIndex_Type(Integer32):
    """Custom type h3cContextIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_H3cContextIndex_Type.__name__ = "Integer32"
_H3cContextIndex_Object = MibTableColumn
h3cContextIndex = _H3cContextIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 154, 1, 1, 1, 1, 1),
    _H3cContextIndex_Type()
)
h3cContextIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cContextIndex.setStatus("current")


class _H3cContextName_Type(DisplayString):
    """Custom type h3cContextName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_H3cContextName_Type.__name__ = "DisplayString"
_H3cContextName_Object = MibTableColumn
h3cContextName = _H3cContextName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 154, 1, 1, 1, 1, 2),
    _H3cContextName_Type()
)
h3cContextName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cContextName.setStatus("current")
_H3cContextNotification_ObjectIdentity = ObjectIdentity
h3cContextNotification = _H3cContextNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 154, 8)
)
_H3cContextNotificationObjects_ObjectIdentity = ObjectIdentity
h3cContextNotificationObjects = _H3cContextNotificationObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 154, 8, 0)
)

# Managed Objects groups


# Notification objects

h3cContextStateChangeToActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 154, 8, 0, 1)
)
h3cContextStateChangeToActive.setObjects(
      *(("H3C-CONTEXT-MIB", "h3cContextIndex"),
        ("H3C-CONTEXT-MIB", "h3cContextName"))
)
if mibBuilder.loadTexts:
    h3cContextStateChangeToActive.setStatus(
        "current"
    )

h3cContextStateChangeToInactive = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 154, 8, 0, 2)
)
h3cContextStateChangeToInactive.setObjects(
      *(("H3C-CONTEXT-MIB", "h3cContextIndex"),
        ("H3C-CONTEXT-MIB", "h3cContextName"))
)
if mibBuilder.loadTexts:
    h3cContextStateChangeToInactive.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "H3C-CONTEXT-MIB",
    **{"h3cContext": h3cContext,
       "h3cContextTables": h3cContextTables,
       "h3cContextControl": h3cContextControl,
       "h3cContextControlTable": h3cContextControlTable,
       "h3cContextControlEntry": h3cContextControlEntry,
       "h3cContextIndex": h3cContextIndex,
       "h3cContextName": h3cContextName,
       "h3cContextNotification": h3cContextNotification,
       "h3cContextNotificationObjects": h3cContextNotificationObjects,
       "h3cContextStateChangeToActive": h3cContextStateChangeToActive,
       "h3cContextStateChangeToInactive": h3cContextStateChangeToInactive}
)
