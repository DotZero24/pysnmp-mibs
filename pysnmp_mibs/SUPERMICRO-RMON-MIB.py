# SNMP MIB module (SUPERMICRO-RMON-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/supermicro/SUPERMICRO-RMON-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:02:16 2025
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

(etherStatsEntry,) = mibBuilder.importSymbols(
    "RMON-MIB",
    "etherStatsEntry")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

futrmon = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 44)
)
if mibBuilder.loadTexts:
    futrmon.setRevisions(
        ("2012-09-05 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RmonDebugType_Type = Unsigned32
_RmonDebugType_Object = MibScalar
rmonDebugType = _RmonDebugType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 44, 1),
    _RmonDebugType_Type()
)
rmonDebugType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmonDebugType.setStatus("current")


class _RmonEnableStatus_Type(Integer32):
    """Custom type rmonEnableStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("rmonenabled", 1),
          ("rmondisabled", 2))
    )


_RmonEnableStatus_Type.__name__ = "Integer32"
_RmonEnableStatus_Object = MibScalar
rmonEnableStatus = _RmonEnableStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 44, 2),
    _RmonEnableStatus_Type()
)
rmonEnableStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmonEnableStatus.setStatus("current")


class _RmonHwStatsSupp_Type(Integer32):
    """Custom type rmonHwStatsSupp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("notsupported", 0),
          ("supported", 1))
    )


_RmonHwStatsSupp_Type.__name__ = "Integer32"
_RmonHwStatsSupp_Object = MibScalar
rmonHwStatsSupp = _RmonHwStatsSupp_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 44, 3),
    _RmonHwStatsSupp_Type()
)
rmonHwStatsSupp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmonHwStatsSupp.setStatus("current")


class _RmonHwHistorySupp_Type(Integer32):
    """Custom type rmonHwHistorySupp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("notsupported", 0),
          ("supported", 1))
    )


_RmonHwHistorySupp_Type.__name__ = "Integer32"
_RmonHwHistorySupp_Object = MibScalar
rmonHwHistorySupp = _RmonHwHistorySupp_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 44, 4),
    _RmonHwHistorySupp_Type()
)
rmonHwHistorySupp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmonHwHistorySupp.setStatus("current")


class _RmonHwAlarmSupp_Type(Integer32):
    """Custom type rmonHwAlarmSupp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("notsupported", 0),
          ("supported", 1))
    )


_RmonHwAlarmSupp_Type.__name__ = "Integer32"
_RmonHwAlarmSupp_Object = MibScalar
rmonHwAlarmSupp = _RmonHwAlarmSupp_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 44, 5),
    _RmonHwAlarmSupp_Type()
)
rmonHwAlarmSupp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmonHwAlarmSupp.setStatus("current")


class _RmonHwHostSupp_Type(Integer32):
    """Custom type rmonHwHostSupp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("notsupported", 0),
          ("supported", 1))
    )


_RmonHwHostSupp_Type.__name__ = "Integer32"
_RmonHwHostSupp_Object = MibScalar
rmonHwHostSupp = _RmonHwHostSupp_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 44, 6),
    _RmonHwHostSupp_Type()
)
rmonHwHostSupp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmonHwHostSupp.setStatus("current")


class _RmonHwHostTopNSupp_Type(Integer32):
    """Custom type rmonHwHostTopNSupp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("notsupported", 0),
          ("supported", 1))
    )


_RmonHwHostTopNSupp_Type.__name__ = "Integer32"
_RmonHwHostTopNSupp_Object = MibScalar
rmonHwHostTopNSupp = _RmonHwHostTopNSupp_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 44, 7),
    _RmonHwHostTopNSupp_Type()
)
rmonHwHostTopNSupp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmonHwHostTopNSupp.setStatus("current")


class _RmonHwMatrixSupp_Type(Integer32):
    """Custom type rmonHwMatrixSupp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("notsupported", 0),
          ("supported", 1))
    )


_RmonHwMatrixSupp_Type.__name__ = "Integer32"
_RmonHwMatrixSupp_Object = MibScalar
rmonHwMatrixSupp = _RmonHwMatrixSupp_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 44, 8),
    _RmonHwMatrixSupp_Type()
)
rmonHwMatrixSupp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmonHwMatrixSupp.setStatus("current")


class _RmonHwEventSupp_Type(Integer32):
    """Custom type rmonHwEventSupp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("notsupported", 0),
          ("supported", 1))
    )


_RmonHwEventSupp_Type.__name__ = "Integer32"
_RmonHwEventSupp_Object = MibScalar
rmonHwEventSupp = _RmonHwEventSupp_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 44, 9),
    _RmonHwEventSupp_Type()
)
rmonHwEventSupp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmonHwEventSupp.setStatus("current")
_RmonStatsTable_Object = MibTable
rmonStatsTable = _RmonStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 44, 10)
)
if mibBuilder.loadTexts:
    rmonStatsTable.setStatus("current")
_RmonStatsEntry_Object = MibTableRow
rmonStatsEntry = _RmonStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 44, 10, 1)
)
if mibBuilder.loadTexts:
    rmonStatsEntry.setStatus("current")
_RmonStatsOutFCSErrors_Type = Counter32
_RmonStatsOutFCSErrors_Object = MibTableColumn
rmonStatsOutFCSErrors = _RmonStatsOutFCSErrors_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 44, 10, 1, 1),
    _RmonStatsOutFCSErrors_Type()
)
rmonStatsOutFCSErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonStatsOutFCSErrors.setStatus("current")
etherStatsEntry.registerAugmentions(
    ("SUPERMICRO-RMON-MIB",
     "rmonStatsEntry")
)
rmonStatsEntry.setIndexNames(*etherStatsEntry.getIndexNames())

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SUPERMICRO-RMON-MIB",
    **{"futrmon": futrmon,
       "rmonDebugType": rmonDebugType,
       "rmonEnableStatus": rmonEnableStatus,
       "rmonHwStatsSupp": rmonHwStatsSupp,
       "rmonHwHistorySupp": rmonHwHistorySupp,
       "rmonHwAlarmSupp": rmonHwAlarmSupp,
       "rmonHwHostSupp": rmonHwHostSupp,
       "rmonHwHostTopNSupp": rmonHwHostTopNSupp,
       "rmonHwMatrixSupp": rmonHwMatrixSupp,
       "rmonHwEventSupp": rmonHwEventSupp,
       "rmonStatsTable": rmonStatsTable,
       "rmonStatsEntry": rmonStatsEntry,
       "rmonStatsOutFCSErrors": rmonStatsOutFCSErrors}
)
