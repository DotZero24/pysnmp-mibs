# SNMP MIB module (AricentDCS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/aricent/AricentDCS-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:42:11 2025
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

fsDcsMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 29601, 2, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class EnabledStatus(TextualConvention, Integer32):
    status = "current"
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



# MIB Managed Objects in the order of their OIDs

_FsDcsSystem_ObjectIdentity = ObjectIdentity
fsDcsSystem = _FsDcsSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29601, 2, 1, 1)
)


class _FsDcsDefCircuitIDFormatConfig_Type(Integer32):
    """Custom type fsDcsDefCircuitIDFormatConfig based on Integer32"""
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


_FsDcsDefCircuitIDFormatConfig_Type.__name__ = "Integer32"
_FsDcsDefCircuitIDFormatConfig_Object = MibScalar
fsDcsDefCircuitIDFormatConfig = _FsDcsDefCircuitIDFormatConfig_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 1, 1, 1),
    _FsDcsDefCircuitIDFormatConfig_Type()
)
fsDcsDefCircuitIDFormatConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDcsDefCircuitIDFormatConfig.setStatus("current")


class _FsDcsDefCircuitIDFormatString_Type(DisplayString):
    """Custom type fsDcsDefCircuitIDFormatString based on DisplayString"""
    defaultValue = OctetString("NULL")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 48),
    )


_FsDcsDefCircuitIDFormatString_Type.__name__ = "DisplayString"
_FsDcsDefCircuitIDFormatString_Object = MibScalar
fsDcsDefCircuitIDFormatString = _FsDcsDefCircuitIDFormatString_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 1, 1, 2),
    _FsDcsDefCircuitIDFormatString_Type()
)
fsDcsDefCircuitIDFormatString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDcsDefCircuitIDFormatString.setStatus("current")


class _FsDcsDefCircuitIDFormatOption_Type(Integer32):
    """Custom type fsDcsDefCircuitIDFormatOption based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("sp", 1),
          ("sv", 2),
          ("pv", 3),
          ("spv", 4))
    )


_FsDcsDefCircuitIDFormatOption_Type.__name__ = "Integer32"
_FsDcsDefCircuitIDFormatOption_Object = MibScalar
fsDcsDefCircuitIDFormatOption = _FsDcsDefCircuitIDFormatOption_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 1, 1, 3),
    _FsDcsDefCircuitIDFormatOption_Type()
)
fsDcsDefCircuitIDFormatOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDcsDefCircuitIDFormatOption.setStatus("current")


class _FsDcsDefCircuitIDFormatDelimiter_Type(Integer32):
    """Custom type fsDcsDefCircuitIDFormatDelimiter based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("hash", 1),
          ("dot", 2),
          ("comma", 3),
          ("semicolon", 4),
          ("rightslash", 5),
          ("space", 6))
    )


_FsDcsDefCircuitIDFormatDelimiter_Type.__name__ = "Integer32"
_FsDcsDefCircuitIDFormatDelimiter_Object = MibScalar
fsDcsDefCircuitIDFormatDelimiter = _FsDcsDefCircuitIDFormatDelimiter_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 1, 1, 4),
    _FsDcsDefCircuitIDFormatDelimiter_Type()
)
fsDcsDefCircuitIDFormatDelimiter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDcsDefCircuitIDFormatDelimiter.setStatus("current")
_FsDcsConfigControl_ObjectIdentity = ObjectIdentity
fsDcsConfigControl = _FsDcsConfigControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29601, 2, 1, 2)
)
_FsDcsPortCtrlTable_Object = MibTable
fsDcsPortCtrlTable = _FsDcsPortCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 1, 2, 1)
)
if mibBuilder.loadTexts:
    fsDcsPortCtrlTable.setStatus("current")
_FsDcsPortCtrlEntry_Object = MibTableRow
fsDcsPortCtrlEntry = _FsDcsPortCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 1, 2, 1, 1)
)
fsDcsPortCtrlEntry.setIndexNames(
    (0, "AricentDCS-MIB", "fsDcsPortCtrlIndex"),
    (0, "AricentDCS-MIB", "fsDcsPortCtrlVlanId"),
)
if mibBuilder.loadTexts:
    fsDcsPortCtrlEntry.setStatus("current")
_FsDcsPortCtrlIndex_Type = InterfaceIndex
_FsDcsPortCtrlIndex_Object = MibTableColumn
fsDcsPortCtrlIndex = _FsDcsPortCtrlIndex_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 1, 2, 1, 1, 1),
    _FsDcsPortCtrlIndex_Type()
)
fsDcsPortCtrlIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsDcsPortCtrlIndex.setStatus("current")


class _FsDcsPortCtrlVlanId_Type(Integer32):
    """Custom type fsDcsPortCtrlVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_FsDcsPortCtrlVlanId_Type.__name__ = "Integer32"
_FsDcsPortCtrlVlanId_Object = MibTableColumn
fsDcsPortCtrlVlanId = _FsDcsPortCtrlVlanId_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 1, 2, 1, 1, 2),
    _FsDcsPortCtrlVlanId_Type()
)
fsDcsPortCtrlVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsDcsPortCtrlVlanId.setStatus("current")


class _FsDcsPortCtrlRemoteAgentIdentifier_Type(DisplayString):
    """Custom type fsDcsPortCtrlRemoteAgentIdentifier based on DisplayString"""
    defaultValue = OctetString("NULL")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_FsDcsPortCtrlRemoteAgentIdentifier_Type.__name__ = "DisplayString"
_FsDcsPortCtrlRemoteAgentIdentifier_Object = MibTableColumn
fsDcsPortCtrlRemoteAgentIdentifier = _FsDcsPortCtrlRemoteAgentIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 1, 2, 1, 1, 3),
    _FsDcsPortCtrlRemoteAgentIdentifier_Type()
)
fsDcsPortCtrlRemoteAgentIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDcsPortCtrlRemoteAgentIdentifier.setStatus("current")


class _FsDcsPortCtrlRemoteAgentIDStatus_Type(EnabledStatus):
    """Custom type fsDcsPortCtrlRemoteAgentIDStatus based on EnabledStatus"""
    defaultValue = 2


_FsDcsPortCtrlRemoteAgentIDStatus_Type.__name__ = "EnabledStatus"
_FsDcsPortCtrlRemoteAgentIDStatus_Object = MibTableColumn
fsDcsPortCtrlRemoteAgentIDStatus = _FsDcsPortCtrlRemoteAgentIDStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 1, 2, 1, 1, 4),
    _FsDcsPortCtrlRemoteAgentIDStatus_Type()
)
fsDcsPortCtrlRemoteAgentIDStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDcsPortCtrlRemoteAgentIDStatus.setStatus("current")


class _FsDcsPortCtrlAccessLoopStatus_Type(EnabledStatus):
    """Custom type fsDcsPortCtrlAccessLoopStatus based on EnabledStatus"""
    defaultValue = 2


_FsDcsPortCtrlAccessLoopStatus_Type.__name__ = "EnabledStatus"
_FsDcsPortCtrlAccessLoopStatus_Object = MibTableColumn
fsDcsPortCtrlAccessLoopStatus = _FsDcsPortCtrlAccessLoopStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 1, 2, 1, 1, 5),
    _FsDcsPortCtrlAccessLoopStatus_Type()
)
fsDcsPortCtrlAccessLoopStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDcsPortCtrlAccessLoopStatus.setStatus("current")


class _FsDcsPortCtrlAgentCircuitID_Type(DisplayString):
    """Custom type fsDcsPortCtrlAgentCircuitID based on DisplayString"""
    defaultValue = OctetString("NULL")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_FsDcsPortCtrlAgentCircuitID_Type.__name__ = "DisplayString"
_FsDcsPortCtrlAgentCircuitID_Object = MibTableColumn
fsDcsPortCtrlAgentCircuitID = _FsDcsPortCtrlAgentCircuitID_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 1, 2, 1, 1, 6),
    _FsDcsPortCtrlAgentCircuitID_Type()
)
fsDcsPortCtrlAgentCircuitID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDcsPortCtrlAgentCircuitID.setStatus("current")
_FsDcsPortCtrlVlanRowStatus_Type = RowStatus
_FsDcsPortCtrlVlanRowStatus_Object = MibTableColumn
fsDcsPortCtrlVlanRowStatus = _FsDcsPortCtrlVlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 1, 2, 1, 1, 7),
    _FsDcsPortCtrlVlanRowStatus_Type()
)
fsDcsPortCtrlVlanRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsDcsPortCtrlVlanRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AricentDCS-MIB",
    **{"EnabledStatus": EnabledStatus,
       "fsDcsMIB": fsDcsMIB,
       "fsDcsSystem": fsDcsSystem,
       "fsDcsDefCircuitIDFormatConfig": fsDcsDefCircuitIDFormatConfig,
       "fsDcsDefCircuitIDFormatString": fsDcsDefCircuitIDFormatString,
       "fsDcsDefCircuitIDFormatOption": fsDcsDefCircuitIDFormatOption,
       "fsDcsDefCircuitIDFormatDelimiter": fsDcsDefCircuitIDFormatDelimiter,
       "fsDcsConfigControl": fsDcsConfigControl,
       "fsDcsPortCtrlTable": fsDcsPortCtrlTable,
       "fsDcsPortCtrlEntry": fsDcsPortCtrlEntry,
       "fsDcsPortCtrlIndex": fsDcsPortCtrlIndex,
       "fsDcsPortCtrlVlanId": fsDcsPortCtrlVlanId,
       "fsDcsPortCtrlRemoteAgentIdentifier": fsDcsPortCtrlRemoteAgentIdentifier,
       "fsDcsPortCtrlRemoteAgentIDStatus": fsDcsPortCtrlRemoteAgentIDStatus,
       "fsDcsPortCtrlAccessLoopStatus": fsDcsPortCtrlAccessLoopStatus,
       "fsDcsPortCtrlAgentCircuitID": fsDcsPortCtrlAgentCircuitID,
       "fsDcsPortCtrlVlanRowStatus": fsDcsPortCtrlVlanRowStatus}
)
