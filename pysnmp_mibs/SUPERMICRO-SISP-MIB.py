# SNMP MIB module (SUPERMICRO-SISP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/supermicro/SUPERMICRO-SISP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:04:24 2025
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

(InterfaceIndex,
 InterfaceIndexOrZero) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero")

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

(VlanId,) = mibBuilder.importSymbols(
    "SUPERMICROQ-BRIDGE-MIB",
    "VlanId")


# MODULE-IDENTITY

fssisp = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 20)
)
if mibBuilder.loadTexts:
    fssisp.setRevisions(
        ("2012-09-05 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FsSispSystemGroup_ObjectIdentity = ObjectIdentity
fsSispSystemGroup = _FsSispSystemGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 20, 1)
)


class _FsSispSystemControl_Type(Integer32):
    """Custom type fsSispSystemControl based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("start", 1),
          ("shutdown", 2))
    )


_FsSispSystemControl_Type.__name__ = "Integer32"
_FsSispSystemControl_Object = MibScalar
fsSispSystemControl = _FsSispSystemControl_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 20, 1, 1),
    _FsSispSystemControl_Type()
)
fsSispSystemControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsSispSystemControl.setStatus("current")
_FsSispConfig_ObjectIdentity = ObjectIdentity
fsSispConfig = _FsSispConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 20, 2)
)
_FsSispPortTable_Object = MibTable
fsSispPortTable = _FsSispPortTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 20, 2, 1)
)
if mibBuilder.loadTexts:
    fsSispPortTable.setStatus("current")
_FsSispPortEntry_Object = MibTableRow
fsSispPortEntry = _FsSispPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 20, 2, 1, 1)
)
fsSispPortEntry.setIndexNames(
    (0, "SUPERMICRO-SISP-MIB", "fsSispPortIndex"),
)
if mibBuilder.loadTexts:
    fsSispPortEntry.setStatus("current")
_FsSispPortIndex_Type = InterfaceIndex
_FsSispPortIndex_Object = MibTableColumn
fsSispPortIndex = _FsSispPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 20, 2, 1, 1, 1),
    _FsSispPortIndex_Type()
)
fsSispPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsSispPortIndex.setStatus("current")


class _FsSispPortCtrlStatus_Type(Integer32):
    """Custom type fsSispPortCtrlStatus based on Integer32"""
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


_FsSispPortCtrlStatus_Type.__name__ = "Integer32"
_FsSispPortCtrlStatus_Object = MibTableColumn
fsSispPortCtrlStatus = _FsSispPortCtrlStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 20, 2, 1, 1, 2),
    _FsSispPortCtrlStatus_Type()
)
fsSispPortCtrlStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsSispPortCtrlStatus.setStatus("current")
_FsSispPortMapTable_Object = MibTable
fsSispPortMapTable = _FsSispPortMapTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 20, 2, 2)
)
if mibBuilder.loadTexts:
    fsSispPortMapTable.setStatus("current")
_FsSispPortMapEntry_Object = MibTableRow
fsSispPortMapEntry = _FsSispPortMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 20, 2, 2, 1)
)
fsSispPortMapEntry.setIndexNames(
    (0, "SUPERMICRO-SISP-MIB", "fsSispPortIndex"),
    (0, "SUPERMICRO-SISP-MIB", "fsSispPortMapContextId"),
)
if mibBuilder.loadTexts:
    fsSispPortMapEntry.setStatus("current")


class _FsSispPortMapContextId_Type(Integer32):
    """Custom type fsSispPortMapContextId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsSispPortMapContextId_Type.__name__ = "Integer32"
_FsSispPortMapContextId_Object = MibTableColumn
fsSispPortMapContextId = _FsSispPortMapContextId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 20, 2, 2, 1, 1),
    _FsSispPortMapContextId_Type()
)
fsSispPortMapContextId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsSispPortMapContextId.setStatus("current")
_FsSispPortMapSharedPort_Type = InterfaceIndex
_FsSispPortMapSharedPort_Object = MibTableColumn
fsSispPortMapSharedPort = _FsSispPortMapSharedPort_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 20, 2, 2, 1, 2),
    _FsSispPortMapSharedPort_Type()
)
fsSispPortMapSharedPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsSispPortMapSharedPort.setStatus("current")
_FsSispPortMapHlPortId_Type = InterfaceIndexOrZero
_FsSispPortMapHlPortId_Object = MibTableColumn
fsSispPortMapHlPortId = _FsSispPortMapHlPortId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 20, 2, 2, 1, 3),
    _FsSispPortMapHlPortId_Type()
)
fsSispPortMapHlPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsSispPortMapHlPortId.setStatus("current")
_FsSispPortMapRowStatus_Type = RowStatus
_FsSispPortMapRowStatus_Object = MibTableColumn
fsSispPortMapRowStatus = _FsSispPortMapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 20, 2, 2, 1, 4),
    _FsSispPortMapRowStatus_Type()
)
fsSispPortMapRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsSispPortMapRowStatus.setStatus("current")
_FsSispInfo_ObjectIdentity = ObjectIdentity
fsSispInfo = _FsSispInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 20, 3)
)
_FsSispCxtClassificationTable_Object = MibTable
fsSispCxtClassificationTable = _FsSispCxtClassificationTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 20, 3, 1)
)
if mibBuilder.loadTexts:
    fsSispCxtClassificationTable.setStatus("current")
_FsSispCxtClassificationEntry_Object = MibTableRow
fsSispCxtClassificationEntry = _FsSispCxtClassificationEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 20, 3, 1, 1)
)
fsSispCxtClassificationEntry.setIndexNames(
    (0, "SUPERMICRO-SISP-MIB", "fsSispPortIndex"),
    (0, "SUPERMICRO-SISP-MIB", "fsSispCxtClassificationVlanId"),
)
if mibBuilder.loadTexts:
    fsSispCxtClassificationEntry.setStatus("current")
_FsSispCxtClassificationVlanId_Type = VlanId
_FsSispCxtClassificationVlanId_Object = MibTableColumn
fsSispCxtClassificationVlanId = _FsSispCxtClassificationVlanId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 20, 3, 1, 1, 1),
    _FsSispCxtClassificationVlanId_Type()
)
fsSispCxtClassificationVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsSispCxtClassificationVlanId.setStatus("current")


class _FsSispCxtClassificationCxtId_Type(Integer32):
    """Custom type fsSispCxtClassificationCxtId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsSispCxtClassificationCxtId_Type.__name__ = "Integer32"
_FsSispCxtClassificationCxtId_Object = MibTableColumn
fsSispCxtClassificationCxtId = _FsSispCxtClassificationCxtId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 20, 3, 1, 1, 2),
    _FsSispCxtClassificationCxtId_Type()
)
fsSispCxtClassificationCxtId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsSispCxtClassificationCxtId.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SUPERMICRO-SISP-MIB",
    **{"fssisp": fssisp,
       "fsSispSystemGroup": fsSispSystemGroup,
       "fsSispSystemControl": fsSispSystemControl,
       "fsSispConfig": fsSispConfig,
       "fsSispPortTable": fsSispPortTable,
       "fsSispPortEntry": fsSispPortEntry,
       "fsSispPortIndex": fsSispPortIndex,
       "fsSispPortCtrlStatus": fsSispPortCtrlStatus,
       "fsSispPortMapTable": fsSispPortMapTable,
       "fsSispPortMapEntry": fsSispPortMapEntry,
       "fsSispPortMapContextId": fsSispPortMapContextId,
       "fsSispPortMapSharedPort": fsSispPortMapSharedPort,
       "fsSispPortMapHlPortId": fsSispPortMapHlPortId,
       "fsSispPortMapRowStatus": fsSispPortMapRowStatus,
       "fsSispInfo": fsSispInfo,
       "fsSispCxtClassificationTable": fsSispCxtClassificationTable,
       "fsSispCxtClassificationEntry": fsSispCxtClassificationEntry,
       "fsSispCxtClassificationVlanId": fsSispCxtClassificationVlanId,
       "fsSispCxtClassificationCxtId": fsSispCxtClassificationCxtId}
)
