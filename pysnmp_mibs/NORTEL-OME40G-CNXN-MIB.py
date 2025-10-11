# SNMP MIB module (NORTEL-OME40G-CNXN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/nortel/NORTEL-OME40G-CNXN-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:20:32 2025
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

(nnOme40G,) = mibBuilder.importSymbols(
    "NORTEL-OME40G-MIB",
    "nnOme40G")

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

nnOme40GConnections = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 562, 68, 11, 3, 2)
)
if mibBuilder.loadTexts:
    nnOme40GConnections.setRevisions(
        ("2007-02-02 00:00",
         "2008-02-07 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NnCrossConnects_ObjectIdentity = ObjectIdentity
nnCrossConnects = _NnCrossConnects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 68, 11, 3, 2, 1)
)
_NnCrossConnectsTable_Object = MibTable
nnCrossConnectsTable = _NnCrossConnectsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 11, 3, 2, 1, 1)
)
if mibBuilder.loadTexts:
    nnCrossConnectsTable.setStatus("current")
_NnCrossConnectsEntry_Object = MibTableRow
nnCrossConnectsEntry = _NnCrossConnectsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 11, 3, 2, 1, 1, 1)
)
nnCrossConnectsEntry.setIndexNames(
    (0, "NORTEL-OME40G-CNXN-MIB", "fromIfIndex"),
    (0, "NORTEL-OME40G-CNXN-MIB", "toIfIndex"),
)
if mibBuilder.loadTexts:
    nnCrossConnectsEntry.setStatus("current")
_FromIfIndex_Type = InterfaceIndex
_FromIfIndex_Object = MibTableColumn
fromIfIndex = _FromIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 11, 3, 2, 1, 1, 1, 1),
    _FromIfIndex_Type()
)
fromIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fromIfIndex.setStatus("current")
_ToIfIndex_Type = InterfaceIndex
_ToIfIndex_Object = MibTableColumn
toIfIndex = _ToIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 11, 3, 2, 1, 1, 1, 2),
    _ToIfIndex_Type()
)
toIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    toIfIndex.setStatus("current")


class _PayloadIndex_Type(Integer32):
    """Custom type payloadIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_PayloadIndex_Type.__name__ = "Integer32"
_PayloadIndex_Object = MibTableColumn
payloadIndex = _PayloadIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 11, 3, 2, 1, 1, 1, 3),
    _PayloadIndex_Type()
)
payloadIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    payloadIndex.setStatus("current")
_XcRowStatus_Type = RowStatus
_XcRowStatus_Object = MibTableColumn
xcRowStatus = _XcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 11, 3, 2, 1, 1, 1, 4),
    _XcRowStatus_Type()
)
xcRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xcRowStatus.setStatus("current")


class _CrossConnectType_Type(Integer32):
    """Custom type crossConnectType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("one-way", 1),
          ("two-way", 2))
    )


_CrossConnectType_Type.__name__ = "Integer32"
_CrossConnectType_Object = MibTableColumn
crossConnectType = _CrossConnectType_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 11, 3, 2, 1, 1, 1, 5),
    _CrossConnectType_Type()
)
crossConnectType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crossConnectType.setStatus("current")
_CrossConnectName_Type = DisplayString
_CrossConnectName_Object = MibTableColumn
crossConnectName = _CrossConnectName_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 11, 3, 2, 1, 1, 1, 6),
    _CrossConnectName_Type()
)
crossConnectName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crossConnectName.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NORTEL-OME40G-CNXN-MIB",
    **{"nnOme40GConnections": nnOme40GConnections,
       "nnCrossConnects": nnCrossConnects,
       "nnCrossConnectsTable": nnCrossConnectsTable,
       "nnCrossConnectsEntry": nnCrossConnectsEntry,
       "fromIfIndex": fromIfIndex,
       "toIfIndex": toIfIndex,
       "payloadIndex": payloadIndex,
       "xcRowStatus": xcRowStatus,
       "crossConnectType": crossConnectType,
       "crossConnectName": crossConnectName}
)
