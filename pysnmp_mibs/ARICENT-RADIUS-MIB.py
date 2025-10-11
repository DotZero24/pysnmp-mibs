# SNMP MIB module (ARICENT-RADIUS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/aricent/ARICENT-RADIUS-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:42:09 2025
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
 PhysAddress,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

futureRADIUSMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 25)
)
if mibBuilder.loadTexts:
    futureRADIUSMIB.setRevisions(
        ("2012-09-05 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RadiusExtClient_ObjectIdentity = ObjectIdentity
radiusExtClient = _RadiusExtClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 25, 1)
)
_RadiusExtDebugMask_Type = Integer32
_RadiusExtDebugMask_Object = MibScalar
radiusExtDebugMask = _RadiusExtDebugMask_Object(
    (1, 3, 6, 1, 4, 1, 2076, 25, 1, 1),
    _RadiusExtDebugMask_Type()
)
radiusExtDebugMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusExtDebugMask.setStatus("current")


class _RadiusMaxNoOfUserEntries_Type(Integer32):
    """Custom type radiusMaxNoOfUserEntries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_RadiusMaxNoOfUserEntries_Type.__name__ = "Integer32"
_RadiusMaxNoOfUserEntries_Object = MibScalar
radiusMaxNoOfUserEntries = _RadiusMaxNoOfUserEntries_Object(
    (1, 3, 6, 1, 4, 1, 2076, 25, 1, 2),
    _RadiusMaxNoOfUserEntries_Type()
)
radiusMaxNoOfUserEntries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusMaxNoOfUserEntries.setStatus("current")
_RadiusExtServerTable_Object = MibTable
radiusExtServerTable = _RadiusExtServerTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 25, 1, 3)
)
if mibBuilder.loadTexts:
    radiusExtServerTable.setStatus("current")
_RadiusExtServerEntry_Object = MibTableRow
radiusExtServerEntry = _RadiusExtServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 25, 1, 3, 1)
)
radiusExtServerEntry.setIndexNames(
    (0, "ARICENT-RADIUS-MIB", "radiusExtServerIndex"),
)
if mibBuilder.loadTexts:
    radiusExtServerEntry.setStatus("current")
_RadiusExtServerIndex_Type = InterfaceIndex
_RadiusExtServerIndex_Object = MibTableColumn
radiusExtServerIndex = _RadiusExtServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 2076, 25, 1, 3, 1, 1),
    _RadiusExtServerIndex_Type()
)
radiusExtServerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusExtServerIndex.setStatus("current")
_RadiusExtServerAddress_Type = IpAddress
_RadiusExtServerAddress_Object = MibTableColumn
radiusExtServerAddress = _RadiusExtServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 2076, 25, 1, 3, 1, 2),
    _RadiusExtServerAddress_Type()
)
radiusExtServerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusExtServerAddress.setStatus("current")


class _RadiusExtServerType_Type(Integer32):
    """Custom type radiusExtServerType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auth", 1),
          ("acct", 2),
          ("both", 3))
    )


_RadiusExtServerType_Type.__name__ = "Integer32"
_RadiusExtServerType_Object = MibTableColumn
radiusExtServerType = _RadiusExtServerType_Object(
    (1, 3, 6, 1, 4, 1, 2076, 25, 1, 3, 1, 3),
    _RadiusExtServerType_Type()
)
radiusExtServerType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusExtServerType.setStatus("current")
_RadiusExtServerSharedSecret_Type = DisplayString
_RadiusExtServerSharedSecret_Object = MibTableColumn
radiusExtServerSharedSecret = _RadiusExtServerSharedSecret_Object(
    (1, 3, 6, 1, 4, 1, 2076, 25, 1, 3, 1, 4),
    _RadiusExtServerSharedSecret_Type()
)
radiusExtServerSharedSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusExtServerSharedSecret.setStatus("current")


class _RadiusExtServerEnabled_Type(Integer32):
    """Custom type radiusExtServerEnabled based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2),
          ("destroy", 3))
    )


_RadiusExtServerEnabled_Type.__name__ = "Integer32"
_RadiusExtServerEnabled_Object = MibTableColumn
radiusExtServerEnabled = _RadiusExtServerEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2076, 25, 1, 3, 1, 5),
    _RadiusExtServerEnabled_Type()
)
radiusExtServerEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusExtServerEnabled.setStatus("current")


class _RadiusExtServerResponseTime_Type(Integer32):
    """Custom type radiusExtServerResponseTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 120),
    )


_RadiusExtServerResponseTime_Type.__name__ = "Integer32"
_RadiusExtServerResponseTime_Object = MibTableColumn
radiusExtServerResponseTime = _RadiusExtServerResponseTime_Object(
    (1, 3, 6, 1, 4, 1, 2076, 25, 1, 3, 1, 6),
    _RadiusExtServerResponseTime_Type()
)
radiusExtServerResponseTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusExtServerResponseTime.setStatus("current")


class _RadiusExtServerMaximumRetransmission_Type(Integer32):
    """Custom type radiusExtServerMaximumRetransmission based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 254),
    )


_RadiusExtServerMaximumRetransmission_Type.__name__ = "Integer32"
_RadiusExtServerMaximumRetransmission_Object = MibTableColumn
radiusExtServerMaximumRetransmission = _RadiusExtServerMaximumRetransmission_Object(
    (1, 3, 6, 1, 4, 1, 2076, 25, 1, 3, 1, 7),
    _RadiusExtServerMaximumRetransmission_Type()
)
radiusExtServerMaximumRetransmission.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusExtServerMaximumRetransmission.setStatus("current")
_RadiusExtServerEntryStatus_Type = RowStatus
_RadiusExtServerEntryStatus_Object = MibTableColumn
radiusExtServerEntryStatus = _RadiusExtServerEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 25, 1, 3, 1, 8),
    _RadiusExtServerEntryStatus_Type()
)
radiusExtServerEntryStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusExtServerEntryStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ARICENT-RADIUS-MIB",
    **{"futureRADIUSMIB": futureRADIUSMIB,
       "radiusExtClient": radiusExtClient,
       "radiusExtDebugMask": radiusExtDebugMask,
       "radiusMaxNoOfUserEntries": radiusMaxNoOfUserEntries,
       "radiusExtServerTable": radiusExtServerTable,
       "radiusExtServerEntry": radiusExtServerEntry,
       "radiusExtServerIndex": radiusExtServerIndex,
       "radiusExtServerAddress": radiusExtServerAddress,
       "radiusExtServerType": radiusExtServerType,
       "radiusExtServerSharedSecret": radiusExtServerSharedSecret,
       "radiusExtServerEnabled": radiusExtServerEnabled,
       "radiusExtServerResponseTime": radiusExtServerResponseTime,
       "radiusExtServerMaximumRetransmission": radiusExtServerMaximumRetransmission,
       "radiusExtServerEntryStatus": radiusExtServerEntryStatus}
)
