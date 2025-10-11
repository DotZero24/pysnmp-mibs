# SNMP MIB module (MAIPU-TERMINAL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/maipu/MAIPU-TERMINAL-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:11:12 2025
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

(mpMgmt,) = mibBuilder.importSymbols(
    "MAIPU-SMI",
    "mpMgmt")

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

mpTerminalMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5651, 3, 602)
)
if mibBuilder.loadTexts:
    mpTerminalMib.setRevisions(
        ("2007-03-14 15:07",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MpTermMIBObjects_ObjectIdentity = ObjectIdentity
mpTermMIBObjects = _MpTermMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5651, 3, 602, 1)
)
_MpTermConfigs_ObjectIdentity = ObjectIdentity
mpTermConfigs = _MpTermConfigs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5651, 3, 602, 1, 1)
)
_MpTermInfo_ObjectIdentity = ObjectIdentity
mpTermInfo = _MpTermInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5651, 3, 602, 1, 2)
)
_MpTermStateTable_Object = MibTable
mpTermStateTable = _MpTermStateTable_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 602, 1, 2, 1)
)
if mibBuilder.loadTexts:
    mpTermStateTable.setStatus("current")
_MpTermStateEntry_Object = MibTableRow
mpTermStateEntry = _MpTermStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 602, 1, 2, 1, 1)
)
mpTermStateEntry.setIndexNames(
    (0, "MAIPU-TERMINAL-MIB", "mpTermStateInterface"),
)
if mibBuilder.loadTexts:
    mpTermStateEntry.setStatus("current")


class _MpTermStateInterface_Type(DisplayString):
    """Custom type mpTermStateInterface based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 59),
    )


_MpTermStateInterface_Type.__name__ = "DisplayString"
_MpTermStateInterface_Object = MibTableColumn
mpTermStateInterface = _MpTermStateInterface_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 602, 1, 2, 1, 1, 1),
    _MpTermStateInterface_Type()
)
mpTermStateInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpTermStateInterface.setStatus("current")


class _MpTermStateTermType_Type(Integer32):
    """Custom type mpTermStateTermType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("terminal", 1),
          ("mpdlc", 2),
          ("pad", 3))
    )


_MpTermStateTermType_Type.__name__ = "Integer32"
_MpTermStateTermType_Object = MibTableColumn
mpTermStateTermType = _MpTermStateTermType_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 602, 1, 2, 1, 1, 2),
    _MpTermStateTermType_Type()
)
mpTermStateTermType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpTermStateTermType.setStatus("current")
_MpTermStateCOM_Type = Integer32
_MpTermStateCOM_Object = MibTableColumn
mpTermStateCOM = _MpTermStateCOM_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 602, 1, 2, 1, 1, 3),
    _MpTermStateCOM_Type()
)
mpTermStateCOM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpTermStateCOM.setStatus("current")
_MpTermStateTERM_Type = Integer32
_MpTermStateTERM_Object = MibTableColumn
mpTermStateTERM = _MpTermStateTERM_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 602, 1, 2, 1, 1, 4),
    _MpTermStateTERM_Type()
)
mpTermStateTERM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpTermStateTERM.setStatus("current")


class _MpTermStateTcpServerPort_Type(Integer32):
    """Custom type mpTermStateTcpServerPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MpTermStateTcpServerPort_Type.__name__ = "Integer32"
_MpTermStateTcpServerPort_Object = MibTableColumn
mpTermStateTcpServerPort = _MpTermStateTcpServerPort_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 602, 1, 2, 1, 1, 5),
    _MpTermStateTcpServerPort_Type()
)
mpTermStateTcpServerPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpTermStateTcpServerPort.setStatus("current")


class _MpTermStateTerminalState_Type(Integer32):
    """Custom type mpTermStateTerminalState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("closed", 1),
          ("initial", 2),
          ("prompt", 3),
          ("running", 4),
          ("waiting", 5))
    )


_MpTermStateTerminalState_Type.__name__ = "Integer32"
_MpTermStateTerminalState_Object = MibTableColumn
mpTermStateTerminalState = _MpTermStateTerminalState_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 602, 1, 2, 1, 1, 6),
    _MpTermStateTerminalState_Type()
)
mpTermStateTerminalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpTermStateTerminalState.setStatus("current")


class _MpTermStateTemplateName_Type(DisplayString):
    """Custom type mpTermStateTemplateName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_MpTermStateTemplateName_Type.__name__ = "DisplayString"
_MpTermStateTemplateName_Object = MibTableColumn
mpTermStateTemplateName = _MpTermStateTemplateName_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 602, 1, 2, 1, 1, 7),
    _MpTermStateTemplateName_Type()
)
mpTermStateTemplateName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpTermStateTemplateName.setStatus("current")


class _MpTermStateActiveRHIndex_Type(Integer32):
    """Custom type mpTermStateActiveRHIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 9),
    )


_MpTermStateActiveRHIndex_Type.__name__ = "Integer32"
_MpTermStateActiveRHIndex_Object = MibTableColumn
mpTermStateActiveRHIndex = _MpTermStateActiveRHIndex_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 602, 1, 2, 1, 1, 8),
    _MpTermStateActiveRHIndex_Type()
)
mpTermStateActiveRHIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpTermStateActiveRHIndex.setStatus("current")
_MpTermRHStateTable_Object = MibTable
mpTermRHStateTable = _MpTermRHStateTable_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 602, 1, 2, 2)
)
if mibBuilder.loadTexts:
    mpTermRHStateTable.setStatus("current")
_MpTermRHStateEntry_Object = MibTableRow
mpTermRHStateEntry = _MpTermRHStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 602, 1, 2, 2, 1)
)
mpTermRHStateEntry.setIndexNames(
    (0, "MAIPU-TERMINAL-MIB", "mpTermRHStateInterface"),
    (0, "MAIPU-TERMINAL-MIB", "mpTermRHStateRHIndex"),
)
if mibBuilder.loadTexts:
    mpTermRHStateEntry.setStatus("current")


class _MpTermRHStateInterface_Type(DisplayString):
    """Custom type mpTermRHStateInterface based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 59),
    )


_MpTermRHStateInterface_Type.__name__ = "DisplayString"
_MpTermRHStateInterface_Object = MibTableColumn
mpTermRHStateInterface = _MpTermRHStateInterface_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 602, 1, 2, 2, 1, 1),
    _MpTermRHStateInterface_Type()
)
mpTermRHStateInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpTermRHStateInterface.setStatus("current")


class _MpTermRHStateRHIndex_Type(Integer32):
    """Custom type mpTermRHStateRHIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_MpTermRHStateRHIndex_Type.__name__ = "Integer32"
_MpTermRHStateRHIndex_Object = MibTableColumn
mpTermRHStateRHIndex = _MpTermRHStateRHIndex_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 602, 1, 2, 2, 1, 2),
    _MpTermRHStateRHIndex_Type()
)
mpTermRHStateRHIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpTermRHStateRHIndex.setStatus("current")


class _MpTermRHStateTemplateName_Type(DisplayString):
    """Custom type mpTermRHStateTemplateName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_MpTermRHStateTemplateName_Type.__name__ = "DisplayString"
_MpTermRHStateTemplateName_Object = MibTableColumn
mpTermRHStateTemplateName = _MpTermRHStateTemplateName_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 602, 1, 2, 2, 1, 3),
    _MpTermRHStateTemplateName_Type()
)
mpTermRHStateTemplateName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpTermRHStateTemplateName.setStatus("current")


class _MpTermRHStateRemoteState_Type(Integer32):
    """Custom type mpTermRHStateRemoteState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disconnect", 1),
          ("connecting", 2),
          ("connected", 3))
    )


_MpTermRHStateRemoteState_Type.__name__ = "Integer32"
_MpTermRHStateRemoteState_Object = MibTableColumn
mpTermRHStateRemoteState = _MpTermRHStateRemoteState_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 602, 1, 2, 2, 1, 4),
    _MpTermRHStateRemoteState_Type()
)
mpTermRHStateRemoteState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpTermRHStateRemoteState.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MAIPU-TERMINAL-MIB",
    **{"mpTerminalMib": mpTerminalMib,
       "mpTermMIBObjects": mpTermMIBObjects,
       "mpTermConfigs": mpTermConfigs,
       "mpTermInfo": mpTermInfo,
       "mpTermStateTable": mpTermStateTable,
       "mpTermStateEntry": mpTermStateEntry,
       "mpTermStateInterface": mpTermStateInterface,
       "mpTermStateTermType": mpTermStateTermType,
       "mpTermStateCOM": mpTermStateCOM,
       "mpTermStateTERM": mpTermStateTERM,
       "mpTermStateTcpServerPort": mpTermStateTcpServerPort,
       "mpTermStateTerminalState": mpTermStateTerminalState,
       "mpTermStateTemplateName": mpTermStateTemplateName,
       "mpTermStateActiveRHIndex": mpTermStateActiveRHIndex,
       "mpTermRHStateTable": mpTermRHStateTable,
       "mpTermRHStateEntry": mpTermRHStateEntry,
       "mpTermRHStateInterface": mpTermRHStateInterface,
       "mpTermRHStateRHIndex": mpTermRHStateRHIndex,
       "mpTermRHStateTemplateName": mpTermRHStateTemplateName,
       "mpTermRHStateRemoteState": mpTermRHStateRemoteState}
)
