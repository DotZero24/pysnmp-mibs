# SNMP MIB module (MAIPU-MODEM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/maipu/MAIPU-MODEM-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:10:59 2025
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

mpModemMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5651, 3, 15)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ModemConfTable_Object = MibTable
modemConfTable = _ModemConfTable_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 15, 1)
)
if mibBuilder.loadTexts:
    modemConfTable.setStatus("current")
_ModemConfEntry_Object = MibTableRow
modemConfEntry = _ModemConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 15, 1, 1)
)
modemConfEntry.setIndexNames(
    (0, "MAIPU-MODEM-MIB", "modemIfIndex"),
)
if mibBuilder.loadTexts:
    modemConfEntry.setStatus("current")
_ModemIfIndex_Type = Integer32
_ModemIfIndex_Object = MibTableColumn
modemIfIndex = _ModemIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 15, 1, 1, 1),
    _ModemIfIndex_Type()
)
modemIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemIfIndex.setStatus("current")


class _ModemLocation_Type(Integer32):
    """Custom type modemLocation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("inner", 1),
          ("outer", 2),
          ("noOuter", 3))
    )


_ModemLocation_Type.__name__ = "Integer32"
_ModemLocation_Object = MibTableColumn
modemLocation = _ModemLocation_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 15, 1, 1, 2),
    _ModemLocation_Type()
)
modemLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modemLocation.setStatus("current")


class _ModemActive_Type(Integer32):
    """Custom type modemActive based on Integer32"""
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


_ModemActive_Type.__name__ = "Integer32"
_ModemActive_Object = MibTableColumn
modemActive = _ModemActive_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 15, 1, 1, 3),
    _ModemActive_Type()
)
modemActive.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    modemActive.setStatus("current")


class _ModemLine_Type(Integer32):
    """Custom type modemLine based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("leased", 1),
          ("nonLeased", 2))
    )


_ModemLine_Type.__name__ = "Integer32"
_ModemLine_Object = MibTableColumn
modemLine = _ModemLine_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 15, 1, 1, 4),
    _ModemLine_Type()
)
modemLine.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    modemLine.setStatus("current")


class _ModemParty_Type(Integer32):
    """Custom type modemParty based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("originate", 1),
          ("answer", 2),
          ("none", 3))
    )


_ModemParty_Type.__name__ = "Integer32"
_ModemParty_Object = MibTableColumn
modemParty = _ModemParty_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 15, 1, 1, 5),
    _ModemParty_Type()
)
modemParty.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    modemParty.setStatus("current")


class _ModemAsyncMode_Type(Integer32):
    """Custom type modemAsyncMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("buffer", 1),
          ("direct", 2),
          ("errorCorrect", 3))
    )


_ModemAsyncMode_Type.__name__ = "Integer32"
_ModemAsyncMode_Object = MibTableColumn
modemAsyncMode = _ModemAsyncMode_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 15, 1, 1, 6),
    _ModemAsyncMode_Type()
)
modemAsyncMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    modemAsyncMode.setStatus("current")


class _ModemClockMode_Type(Integer32):
    """Custom type modemClockMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("internal", 1),
          ("external", 2),
          ("slave", 3))
    )


_ModemClockMode_Type.__name__ = "Integer32"
_ModemClockMode_Object = MibTableColumn
modemClockMode = _ModemClockMode_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 15, 1, 1, 7),
    _ModemClockMode_Type()
)
modemClockMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    modemClockMode.setStatus("current")
_ModemClockRate_Type = Integer32
_ModemClockRate_Object = MibTableColumn
modemClockRate = _ModemClockRate_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 15, 1, 1, 8),
    _ModemClockRate_Type()
)
modemClockRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    modemClockRate.setStatus("current")


class _ModemStatus_Type(Integer32):
    """Custom type modemStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("unconfig", 1),
          ("idle", 2),
          ("atMode", 3),
          ("dialout", 4),
          ("answer", 5),
          ("connect", 6),
          ("config", 7),
          ("hangUp", 8))
    )


_ModemStatus_Type.__name__ = "Integer32"
_ModemStatus_Object = MibTableColumn
modemStatus = _ModemStatus_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 15, 1, 1, 9),
    _ModemStatus_Type()
)
modemStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemStatus.setStatus("current")
_ModemDialerTable_Object = MibTable
modemDialerTable = _ModemDialerTable_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 15, 2)
)
if mibBuilder.loadTexts:
    modemDialerTable.setStatus("current")
_ModemDialerEntry_Object = MibTableRow
modemDialerEntry = _ModemDialerEntry_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 15, 2, 1)
)
modemDialerEntry.setIndexNames(
    (0, "MAIPU-MODEM-MIB", "modemDialerIfIndex"),
    (0, "MAIPU-MODEM-MIB", "modemDialerString"),
)
if mibBuilder.loadTexts:
    modemDialerEntry.setStatus("current")
_ModemDialerIfIndex_Type = Integer32
_ModemDialerIfIndex_Object = MibTableColumn
modemDialerIfIndex = _ModemDialerIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 15, 2, 1, 1),
    _ModemDialerIfIndex_Type()
)
modemDialerIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    modemDialerIfIndex.setStatus("current")
_ModemDialerString_Type = OctetString
_ModemDialerString_Object = MibTableColumn
modemDialerString = _ModemDialerString_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 15, 2, 1, 2),
    _ModemDialerString_Type()
)
modemDialerString.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    modemDialerString.setStatus("current")
_ModemDialerStatus_Type = RowStatus
_ModemDialerStatus_Object = MibTableColumn
modemDialerStatus = _ModemDialerStatus_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 15, 2, 1, 3),
    _ModemDialerStatus_Type()
)
modemDialerStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    modemDialerStatus.setStatus("current")
_ModemScriptTable_Object = MibTable
modemScriptTable = _ModemScriptTable_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 15, 3)
)
if mibBuilder.loadTexts:
    modemScriptTable.setStatus("current")
_ModemScriptEntry_Object = MibTableRow
modemScriptEntry = _ModemScriptEntry_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 15, 3, 1)
)
modemScriptEntry.setIndexNames(
    (0, "MAIPU-MODEM-MIB", "modemScriptName"),
)
if mibBuilder.loadTexts:
    modemScriptEntry.setStatus("current")
_ModemScriptName_Type = OctetString
_ModemScriptName_Object = MibTableColumn
modemScriptName = _ModemScriptName_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 15, 3, 1, 1),
    _ModemScriptName_Type()
)
modemScriptName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    modemScriptName.setStatus("current")
_ModemScriptString_Type = OctetString
_ModemScriptString_Object = MibTableColumn
modemScriptString = _ModemScriptString_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 15, 3, 1, 2),
    _ModemScriptString_Type()
)
modemScriptString.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    modemScriptString.setStatus("current")
_ModemScriptStatus_Type = RowStatus
_ModemScriptStatus_Object = MibTableColumn
modemScriptStatus = _ModemScriptStatus_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 15, 3, 1, 3),
    _ModemScriptStatus_Type()
)
modemScriptStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    modemScriptStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MAIPU-MODEM-MIB",
    **{"mpModemMib": mpModemMib,
       "modemConfTable": modemConfTable,
       "modemConfEntry": modemConfEntry,
       "modemIfIndex": modemIfIndex,
       "modemLocation": modemLocation,
       "modemActive": modemActive,
       "modemLine": modemLine,
       "modemParty": modemParty,
       "modemAsyncMode": modemAsyncMode,
       "modemClockMode": modemClockMode,
       "modemClockRate": modemClockRate,
       "modemStatus": modemStatus,
       "modemDialerTable": modemDialerTable,
       "modemDialerEntry": modemDialerEntry,
       "modemDialerIfIndex": modemDialerIfIndex,
       "modemDialerString": modemDialerString,
       "modemDialerStatus": modemDialerStatus,
       "modemScriptTable": modemScriptTable,
       "modemScriptEntry": modemScriptEntry,
       "modemScriptName": modemScriptName,
       "modemScriptString": modemScriptString,
       "modemScriptStatus": modemScriptStatus}
)
