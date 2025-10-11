# SNMP MIB module (G6-CLI-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/microsens/G6-CLI-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:54:14 2025
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

(g6,) = mibBuilder.importSymbols(
    "MICROSENS-G6-MIB",
    "g6")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

management = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3)
)
if mibBuilder.loadTexts:
    management.setRevisions(
        ("2018-02-12 16:19",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Cli_ObjectIdentity = ObjectIdentity
cli = _Cli_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 62)
)


class _CliEnableTelnet_Type(Integer32):
    """Custom type cliEnableTelnet based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_CliEnableTelnet_Type.__name__ = "Integer32"
_CliEnableTelnet_Object = MibScalar
cliEnableTelnet = _CliEnableTelnet_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 62, 1),
    _CliEnableTelnet_Type()
)
cliEnableTelnet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cliEnableTelnet.setStatus("current")


class _CliEnableSsh_Type(Integer32):
    """Custom type cliEnableSsh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_CliEnableSsh_Type.__name__ = "Integer32"
_CliEnableSsh_Object = MibScalar
cliEnableSsh = _CliEnableSsh_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 62, 2),
    _CliEnableSsh_Type()
)
cliEnableSsh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cliEnableSsh.setStatus("current")


class _CliPromptSource_Type(Integer32):
    """Custom type cliPromptSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("hostname", 0),
          ("deviceLocation", 1),
          ("userName", 2),
          ("userDefined", 3))
    )


_CliPromptSource_Type.__name__ = "Integer32"
_CliPromptSource_Object = MibScalar
cliPromptSource = _CliPromptSource_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 62, 3),
    _CliPromptSource_Type()
)
cliPromptSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cliPromptSource.setStatus("current")
_CliWelcomeMessage_Type = DisplayString
_CliWelcomeMessage_Object = MibScalar
cliWelcomeMessage = _CliWelcomeMessage_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 62, 4),
    _CliWelcomeMessage_Type()
)
cliWelcomeMessage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cliWelcomeMessage.setStatus("current")
_CliUserPrompt_Type = DisplayString
_CliUserPrompt_Object = MibScalar
cliUserPrompt = _CliUserPrompt_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 62, 5),
    _CliUserPrompt_Type()
)
cliUserPrompt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cliUserPrompt.setStatus("current")


class _CliColors_Type(Integer32):
    """Custom type cliColors based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_CliColors_Type.__name__ = "Integer32"
_CliColors_Object = MibScalar
cliColors = _CliColors_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 62, 6),
    _CliColors_Type()
)
cliColors.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cliColors.setStatus("current")


class _CliScriptMode_Type(Integer32):
    """Custom type cliScriptMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_CliScriptMode_Type.__name__ = "Integer32"
_CliScriptMode_Object = MibScalar
cliScriptMode = _CliScriptMode_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 62, 7),
    _CliScriptMode_Type()
)
cliScriptMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cliScriptMode.setStatus("current")


class _CliAutoTextExpansion_Type(Integer32):
    """Custom type cliAutoTextExpansion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_CliAutoTextExpansion_Type.__name__ = "Integer32"
_CliAutoTextExpansion_Object = MibScalar
cliAutoTextExpansion = _CliAutoTextExpansion_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 62, 8),
    _CliAutoTextExpansion_Type()
)
cliAutoTextExpansion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cliAutoTextExpansion.setStatus("current")


class _CliDontAskQuestions_Type(Integer32):
    """Custom type cliDontAskQuestions based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_CliDontAskQuestions_Type.__name__ = "Integer32"
_CliDontAskQuestions_Object = MibScalar
cliDontAskQuestions = _CliDontAskQuestions_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 62, 9),
    _CliDontAskQuestions_Type()
)
cliDontAskQuestions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cliDontAskQuestions.setStatus("current")


class _CliInactivityTimeout_Type(Integer32):
    """Custom type cliInactivityTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CliInactivityTimeout_Type.__name__ = "Integer32"
_CliInactivityTimeout_Object = MibScalar
cliInactivityTimeout = _CliInactivityTimeout_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 62, 10),
    _CliInactivityTimeout_Type()
)
cliInactivityTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cliInactivityTimeout.setStatus("current")


class _CliMicroscriptTracing_Type(Integer32):
    """Custom type cliMicroscriptTracing based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_CliMicroscriptTracing_Type.__name__ = "Integer32"
_CliMicroscriptTracing_Object = MibScalar
cliMicroscriptTracing = _CliMicroscriptTracing_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 62, 11),
    _CliMicroscriptTracing_Type()
)
cliMicroscriptTracing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cliMicroscriptTracing.setStatus("current")


class _CliNamedStatusSelection_Type(Integer32):
    """Custom type cliNamedStatusSelection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_CliNamedStatusSelection_Type.__name__ = "Integer32"
_CliNamedStatusSelection_Object = MibScalar
cliNamedStatusSelection = _CliNamedStatusSelection_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 62, 12),
    _CliNamedStatusSelection_Type()
)
cliNamedStatusSelection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cliNamedStatusSelection.setStatus("current")


class _CliLiveHelp_Type(Integer32):
    """Custom type cliLiveHelp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_CliLiveHelp_Type.__name__ = "Integer32"
_CliLiveHelp_Object = MibScalar
cliLiveHelp = _CliLiveHelp_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 62, 13),
    _CliLiveHelp_Type()
)
cliLiveHelp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cliLiveHelp.setStatus("current")
_FavoritesTable_Object = MibTable
favoritesTable = _FavoritesTable_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 62, 14)
)
if mibBuilder.loadTexts:
    favoritesTable.setStatus("current")
_FavoritesEntry_Object = MibTableRow
favoritesEntry = _FavoritesEntry_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 62, 14, 1)
)
favoritesEntry.setIndexNames(
    (0, "G6-CLI-MIB", "favoritesIndex"),
)
if mibBuilder.loadTexts:
    favoritesEntry.setStatus("current")


class _FavoritesIndex_Type(Integer32):
    """Custom type favoritesIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_FavoritesIndex_Type.__name__ = "Integer32"
_FavoritesIndex_Object = MibTableColumn
favoritesIndex = _FavoritesIndex_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 62, 14, 1, 1),
    _FavoritesIndex_Type()
)
favoritesIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    favoritesIndex.setStatus("current")
_FavoritesCommandLine_Type = DisplayString
_FavoritesCommandLine_Object = MibTableColumn
favoritesCommandLine = _FavoritesCommandLine_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 62, 14, 1, 2),
    _FavoritesCommandLine_Type()
)
favoritesCommandLine.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    favoritesCommandLine.setStatus("current")


class _CliLastInstance_Type(Integer32):
    """Custom type cliLastInstance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CliLastInstance_Type.__name__ = "Integer32"
_CliLastInstance_Object = MibScalar
cliLastInstance = _CliLastInstance_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 62, 100),
    _CliLastInstance_Type()
)
cliLastInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cliLastInstance.setStatus("current")
_ScriptStatusTable_Object = MibTable
scriptStatusTable = _ScriptStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 62, 101)
)
if mibBuilder.loadTexts:
    scriptStatusTable.setStatus("current")
_ScriptStatusEntry_Object = MibTableRow
scriptStatusEntry = _ScriptStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 62, 101, 1)
)
scriptStatusEntry.setIndexNames(
    (0, "G6-CLI-MIB", "scriptStatusIndex"),
)
if mibBuilder.loadTexts:
    scriptStatusEntry.setStatus("current")


class _ScriptStatusIndex_Type(Integer32):
    """Custom type scriptStatusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
    )


_ScriptStatusIndex_Type.__name__ = "Integer32"
_ScriptStatusIndex_Object = MibTableColumn
scriptStatusIndex = _ScriptStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 62, 101, 1, 1),
    _ScriptStatusIndex_Type()
)
scriptStatusIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    scriptStatusIndex.setStatus("current")
_ScriptStatusLastScriptName_Type = DisplayString
_ScriptStatusLastScriptName_Object = MibTableColumn
scriptStatusLastScriptName = _ScriptStatusLastScriptName_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 62, 101, 1, 2),
    _ScriptStatusLastScriptName_Type()
)
scriptStatusLastScriptName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scriptStatusLastScriptName.setStatus("current")
_ScriptStatusExecutedFiles_Type = Unsigned32
_ScriptStatusExecutedFiles_Object = MibTableColumn
scriptStatusExecutedFiles = _ScriptStatusExecutedFiles_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 62, 101, 1, 3),
    _ScriptStatusExecutedFiles_Type()
)
scriptStatusExecutedFiles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scriptStatusExecutedFiles.setStatus("current")
_ScriptStatusExecutedCommands_Type = Unsigned32
_ScriptStatusExecutedCommands_Object = MibTableColumn
scriptStatusExecutedCommands = _ScriptStatusExecutedCommands_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 62, 101, 1, 4),
    _ScriptStatusExecutedCommands_Type()
)
scriptStatusExecutedCommands.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scriptStatusExecutedCommands.setStatus("current")
_ScriptStatusCommandErrors_Type = Unsigned32
_ScriptStatusCommandErrors_Object = MibTableColumn
scriptStatusCommandErrors = _ScriptStatusCommandErrors_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 62, 101, 1, 5),
    _ScriptStatusCommandErrors_Type()
)
scriptStatusCommandErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scriptStatusCommandErrors.setStatus("current")
_CompareStatusTable_Object = MibTable
compareStatusTable = _CompareStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 62, 102)
)
if mibBuilder.loadTexts:
    compareStatusTable.setStatus("current")
_CompareStatusEntry_Object = MibTableRow
compareStatusEntry = _CompareStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 62, 102, 1)
)
compareStatusEntry.setIndexNames(
    (0, "G6-CLI-MIB", "compareStatusIndex"),
)
if mibBuilder.loadTexts:
    compareStatusEntry.setStatus("current")


class _CompareStatusIndex_Type(Integer32):
    """Custom type compareStatusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
    )


_CompareStatusIndex_Type.__name__ = "Integer32"
_CompareStatusIndex_Object = MibTableColumn
compareStatusIndex = _CompareStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 62, 102, 1, 1),
    _CompareStatusIndex_Type()
)
compareStatusIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    compareStatusIndex.setStatus("current")
_CompareStatusLastDotstring_Type = DisplayString
_CompareStatusLastDotstring_Object = MibTableColumn
compareStatusLastDotstring = _CompareStatusLastDotstring_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 62, 102, 1, 2),
    _CompareStatusLastDotstring_Type()
)
compareStatusLastDotstring.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    compareStatusLastDotstring.setStatus("current")


class _CompareStatusMatched_Type(Integer32):
    """Custom type compareStatusMatched based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_CompareStatusMatched_Type.__name__ = "Integer32"
_CompareStatusMatched_Object = MibTableColumn
compareStatusMatched = _CompareStatusMatched_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 62, 102, 1, 3),
    _CompareStatusMatched_Type()
)
compareStatusMatched.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    compareStatusMatched.setStatus("current")
_CompareStatusItemsCompared_Type = Unsigned32
_CompareStatusItemsCompared_Object = MibTableColumn
compareStatusItemsCompared = _CompareStatusItemsCompared_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 62, 102, 1, 4),
    _CompareStatusItemsCompared_Type()
)
compareStatusItemsCompared.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    compareStatusItemsCompared.setStatus("current")
_CompareStatusItemsDifferent_Type = Unsigned32
_CompareStatusItemsDifferent_Object = MibTableColumn
compareStatusItemsDifferent = _CompareStatusItemsDifferent_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 62, 102, 1, 5),
    _CompareStatusItemsDifferent_Type()
)
compareStatusItemsDifferent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    compareStatusItemsDifferent.setStatus("current")
_ScriptMonitorTable_Object = MibTable
scriptMonitorTable = _ScriptMonitorTable_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 62, 103)
)
if mibBuilder.loadTexts:
    scriptMonitorTable.setStatus("current")
_ScriptMonitorEntry_Object = MibTableRow
scriptMonitorEntry = _ScriptMonitorEntry_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 62, 103, 1)
)
scriptMonitorEntry.setIndexNames(
    (0, "G6-CLI-MIB", "scriptMonitorIndex"),
)
if mibBuilder.loadTexts:
    scriptMonitorEntry.setStatus("current")


class _ScriptMonitorIndex_Type(Integer32):
    """Custom type scriptMonitorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_ScriptMonitorIndex_Type.__name__ = "Integer32"
_ScriptMonitorIndex_Object = MibTableColumn
scriptMonitorIndex = _ScriptMonitorIndex_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 62, 103, 1, 1),
    _ScriptMonitorIndex_Type()
)
scriptMonitorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    scriptMonitorIndex.setStatus("current")


class _ScriptMonitorState_Type(Integer32):
    """Custom type scriptMonitorState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unused", 0),
          ("history", 1),
          ("running", 2))
    )


_ScriptMonitorState_Type.__name__ = "Integer32"
_ScriptMonitorState_Object = MibTableColumn
scriptMonitorState = _ScriptMonitorState_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 62, 103, 1, 2),
    _ScriptMonitorState_Type()
)
scriptMonitorState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scriptMonitorState.setStatus("current")
_ScriptMonitorScriptName_Type = DisplayString
_ScriptMonitorScriptName_Object = MibTableColumn
scriptMonitorScriptName = _ScriptMonitorScriptName_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 62, 103, 1, 3),
    _ScriptMonitorScriptName_Type()
)
scriptMonitorScriptName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scriptMonitorScriptName.setStatus("current")
_ScriptMonitorLaunchedBy_Type = DisplayString
_ScriptMonitorLaunchedBy_Object = MibTableColumn
scriptMonitorLaunchedBy = _ScriptMonitorLaunchedBy_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 62, 103, 1, 4),
    _ScriptMonitorLaunchedBy_Type()
)
scriptMonitorLaunchedBy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scriptMonitorLaunchedBy.setStatus("current")
_ScriptMonitorCliInstance_Type = Unsigned32
_ScriptMonitorCliInstance_Object = MibTableColumn
scriptMonitorCliInstance = _ScriptMonitorCliInstance_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 62, 103, 1, 5),
    _ScriptMonitorCliInstance_Type()
)
scriptMonitorCliInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scriptMonitorCliInstance.setStatus("current")
_ScriptMonitorLaunchTimeStamp_Type = Counter32
_ScriptMonitorLaunchTimeStamp_Object = MibTableColumn
scriptMonitorLaunchTimeStamp = _ScriptMonitorLaunchTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 62, 103, 1, 6),
    _ScriptMonitorLaunchTimeStamp_Type()
)
scriptMonitorLaunchTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scriptMonitorLaunchTimeStamp.setStatus("current")
_ScriptMonitorRunTime_Type = Counter32
_ScriptMonitorRunTime_Object = MibTableColumn
scriptMonitorRunTime = _ScriptMonitorRunTime_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 62, 103, 1, 7),
    _ScriptMonitorRunTime_Type()
)
scriptMonitorRunTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scriptMonitorRunTime.setStatus("current")
_ScriptMonitorCurrentFile_Type = DisplayString
_ScriptMonitorCurrentFile_Object = MibTableColumn
scriptMonitorCurrentFile = _ScriptMonitorCurrentFile_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 62, 103, 1, 8),
    _ScriptMonitorCurrentFile_Type()
)
scriptMonitorCurrentFile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scriptMonitorCurrentFile.setStatus("current")
_ScriptMonitorCurrentSubroutine_Type = DisplayString
_ScriptMonitorCurrentSubroutine_Object = MibTableColumn
scriptMonitorCurrentSubroutine = _ScriptMonitorCurrentSubroutine_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 62, 103, 1, 9),
    _ScriptMonitorCurrentSubroutine_Type()
)
scriptMonitorCurrentSubroutine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scriptMonitorCurrentSubroutine.setStatus("current")
_ScriptMonitorLinesExecuted_Type = Unsigned32
_ScriptMonitorLinesExecuted_Object = MibTableColumn
scriptMonitorLinesExecuted = _ScriptMonitorLinesExecuted_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 62, 103, 1, 10),
    _ScriptMonitorLinesExecuted_Type()
)
scriptMonitorLinesExecuted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scriptMonitorLinesExecuted.setStatus("current")
_ScriptMonitorCurrentLineNumber_Type = Unsigned32
_ScriptMonitorCurrentLineNumber_Object = MibTableColumn
scriptMonitorCurrentLineNumber = _ScriptMonitorCurrentLineNumber_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 62, 103, 1, 11),
    _ScriptMonitorCurrentLineNumber_Type()
)
scriptMonitorCurrentLineNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scriptMonitorCurrentLineNumber.setStatus("current")
_ScriptMonitorScriptErrors_Type = Unsigned32
_ScriptMonitorScriptErrors_Object = MibTableColumn
scriptMonitorScriptErrors = _ScriptMonitorScriptErrors_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 62, 103, 1, 12),
    _ScriptMonitorScriptErrors_Type()
)
scriptMonitorScriptErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scriptMonitorScriptErrors.setStatus("current")
_InstancesTable_Object = MibTable
instancesTable = _InstancesTable_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 62, 104)
)
if mibBuilder.loadTexts:
    instancesTable.setStatus("current")
_InstancesEntry_Object = MibTableRow
instancesEntry = _InstancesEntry_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 62, 104, 1)
)
instancesEntry.setIndexNames(
    (0, "G6-CLI-MIB", "instancesIndex"),
)
if mibBuilder.loadTexts:
    instancesEntry.setStatus("current")


class _InstancesIndex_Type(Integer32):
    """Custom type instancesIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_InstancesIndex_Type.__name__ = "Integer32"
_InstancesIndex_Object = MibTableColumn
instancesIndex = _InstancesIndex_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 62, 104, 1, 1),
    _InstancesIndex_Type()
)
instancesIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    instancesIndex.setStatus("current")
_InstancesUserName_Type = DisplayString
_InstancesUserName_Object = MibTableColumn
instancesUserName = _InstancesUserName_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 62, 104, 1, 2),
    _InstancesUserName_Type()
)
instancesUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    instancesUserName.setStatus("current")
_InstancesCommandLine_Type = DisplayString
_InstancesCommandLine_Object = MibTableColumn
instancesCommandLine = _InstancesCommandLine_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 62, 104, 1, 3),
    _InstancesCommandLine_Type()
)
instancesCommandLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    instancesCommandLine.setStatus("current")
_InstancesProcessId_Type = Unsigned32
_InstancesProcessId_Object = MibTableColumn
instancesProcessId = _InstancesProcessId_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 62, 104, 1, 4),
    _InstancesProcessId_Type()
)
instancesProcessId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    instancesProcessId.setStatus("current")
_InstancesLaunchTimeStamp_Type = Counter32
_InstancesLaunchTimeStamp_Object = MibTableColumn
instancesLaunchTimeStamp = _InstancesLaunchTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 62, 104, 1, 5),
    _InstancesLaunchTimeStamp_Type()
)
instancesLaunchTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    instancesLaunchTimeStamp.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "G6-CLI-MIB",
    **{"management": management,
       "cli": cli,
       "cliEnableTelnet": cliEnableTelnet,
       "cliEnableSsh": cliEnableSsh,
       "cliPromptSource": cliPromptSource,
       "cliWelcomeMessage": cliWelcomeMessage,
       "cliUserPrompt": cliUserPrompt,
       "cliColors": cliColors,
       "cliScriptMode": cliScriptMode,
       "cliAutoTextExpansion": cliAutoTextExpansion,
       "cliDontAskQuestions": cliDontAskQuestions,
       "cliInactivityTimeout": cliInactivityTimeout,
       "cliMicroscriptTracing": cliMicroscriptTracing,
       "cliNamedStatusSelection": cliNamedStatusSelection,
       "cliLiveHelp": cliLiveHelp,
       "favoritesTable": favoritesTable,
       "favoritesEntry": favoritesEntry,
       "favoritesIndex": favoritesIndex,
       "favoritesCommandLine": favoritesCommandLine,
       "cliLastInstance": cliLastInstance,
       "scriptStatusTable": scriptStatusTable,
       "scriptStatusEntry": scriptStatusEntry,
       "scriptStatusIndex": scriptStatusIndex,
       "scriptStatusLastScriptName": scriptStatusLastScriptName,
       "scriptStatusExecutedFiles": scriptStatusExecutedFiles,
       "scriptStatusExecutedCommands": scriptStatusExecutedCommands,
       "scriptStatusCommandErrors": scriptStatusCommandErrors,
       "compareStatusTable": compareStatusTable,
       "compareStatusEntry": compareStatusEntry,
       "compareStatusIndex": compareStatusIndex,
       "compareStatusLastDotstring": compareStatusLastDotstring,
       "compareStatusMatched": compareStatusMatched,
       "compareStatusItemsCompared": compareStatusItemsCompared,
       "compareStatusItemsDifferent": compareStatusItemsDifferent,
       "scriptMonitorTable": scriptMonitorTable,
       "scriptMonitorEntry": scriptMonitorEntry,
       "scriptMonitorIndex": scriptMonitorIndex,
       "scriptMonitorState": scriptMonitorState,
       "scriptMonitorScriptName": scriptMonitorScriptName,
       "scriptMonitorLaunchedBy": scriptMonitorLaunchedBy,
       "scriptMonitorCliInstance": scriptMonitorCliInstance,
       "scriptMonitorLaunchTimeStamp": scriptMonitorLaunchTimeStamp,
       "scriptMonitorRunTime": scriptMonitorRunTime,
       "scriptMonitorCurrentFile": scriptMonitorCurrentFile,
       "scriptMonitorCurrentSubroutine": scriptMonitorCurrentSubroutine,
       "scriptMonitorLinesExecuted": scriptMonitorLinesExecuted,
       "scriptMonitorCurrentLineNumber": scriptMonitorCurrentLineNumber,
       "scriptMonitorScriptErrors": scriptMonitorScriptErrors,
       "instancesTable": instancesTable,
       "instancesEntry": instancesEntry,
       "instancesIndex": instancesIndex,
       "instancesUserName": instancesUserName,
       "instancesCommandLine": instancesCommandLine,
       "instancesProcessId": instancesProcessId,
       "instancesLaunchTimeStamp": instancesLaunchTimeStamp}
)
