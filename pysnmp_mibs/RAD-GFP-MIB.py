# SNMP MIB module (RAD-GFP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/rad/RAD-GFP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:19:06 2025
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

(ifAlias,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifAlias",
    "ifIndex")

(alarmEventLogAlarmOrEventId,
 alarmEventLogDateAndTime,
 alarmEventLogDescription,
 alarmEventLogSeverity,
 alarmEventLogSourceName,
 alarmEventReason) = mibBuilder.importSymbols(
    "RAD-GEN-MIB",
    "alarmEventLogAlarmOrEventId",
    "alarmEventLogDateAndTime",
    "alarmEventLogDescription",
    "alarmEventLogSeverity",
    "alarmEventLogSourceName",
    "alarmEventReason")

(agnt,) = mibBuilder.importSymbols(
    "RAD-SMI-MIB",
    "agnt")

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

gfp = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 55)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_GfpEvents_ObjectIdentity = ObjectIdentity
gfpEvents = _GfpEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 55, 0)
)
_GfpCnfgTable_Object = MibTable
gfpCnfgTable = _GfpCnfgTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 55, 1)
)
if mibBuilder.loadTexts:
    gfpCnfgTable.setStatus("current")
_GfpCnfgEntry_Object = MibTableRow
gfpCnfgEntry = _GfpCnfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 55, 1, 1)
)
gfpCnfgEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "RAD-GFP-MIB", "gfpCnfgIdx"),
)
if mibBuilder.loadTexts:
    gfpCnfgEntry.setStatus("current")
_GfpCnfgIdx_Type = Unsigned32
_GfpCnfgIdx_Object = MibTableColumn
gfpCnfgIdx = _GfpCnfgIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 55, 1, 1, 1),
    _GfpCnfgIdx_Type()
)
gfpCnfgIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gfpCnfgIdx.setStatus("current")


class _GfpPayloadFcs_Type(Integer32):
    """Custom type gfpPayloadFcs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 3))
    )


_GfpPayloadFcs_Type.__name__ = "Integer32"
_GfpPayloadFcs_Object = MibTableColumn
gfpPayloadFcs = _GfpPayloadFcs_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 55, 1, 1, 2),
    _GfpPayloadFcs_Type()
)
gfpPayloadFcs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gfpPayloadFcs.setStatus("current")


class _GfpRxTxScramble_Type(Integer32):
    """Custom type gfpRxTxScramble based on Integer32"""
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
        *(("noScramble", 1),
          ("rxTxScramble", 2),
          ("rxOnlyScramble", 3),
          ("txOnlyScramble", 4))
    )


_GfpRxTxScramble_Type.__name__ = "Integer32"
_GfpRxTxScramble_Object = MibTableColumn
gfpRxTxScramble = _GfpRxTxScramble_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 55, 1, 1, 3),
    _GfpRxTxScramble_Type()
)
gfpRxTxScramble.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gfpRxTxScramble.setStatus("current")


class _GfpVcatHeader_Type(Integer32):
    """Custom type gfpVcatHeader based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("disable", 2),
          ("enable", 3))
    )


_GfpVcatHeader_Type.__name__ = "Integer32"
_GfpVcatHeader_Object = MibTableColumn
gfpVcatHeader = _GfpVcatHeader_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 55, 1, 1, 4),
    _GfpVcatHeader_Type()
)
gfpVcatHeader.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gfpVcatHeader.setStatus("current")

# Managed Objects groups


# Notification objects

gfpLof = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 55, 0, 1)
)
gfpLof.setObjects(
      *(("RAD-GEN-MIB", "alarmEventLogSourceName"),
        ("RAD-GEN-MIB", "alarmEventLogAlarmOrEventId"),
        ("RAD-GEN-MIB", "alarmEventLogDescription"),
        ("RAD-GEN-MIB", "alarmEventLogSeverity"),
        ("RAD-GEN-MIB", "alarmEventLogDateAndTime"),
        ("RAD-GEN-MIB", "alarmEventReason"),
        ("IF-MIB", "ifAlias"))
)
if mibBuilder.loadTexts:
    gfpLof.setStatus(
        "current"
    )

gfpCsf = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 55, 0, 2)
)
gfpCsf.setObjects(
      *(("RAD-GEN-MIB", "alarmEventLogSourceName"),
        ("RAD-GEN-MIB", "alarmEventLogAlarmOrEventId"),
        ("RAD-GEN-MIB", "alarmEventLogDescription"),
        ("RAD-GEN-MIB", "alarmEventLogSeverity"),
        ("RAD-GEN-MIB", "alarmEventLogDateAndTime"),
        ("RAD-GEN-MIB", "alarmEventReason"),
        ("IF-MIB", "ifAlias"))
)
if mibBuilder.loadTexts:
    gfpCsf.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RAD-GFP-MIB",
    **{"gfp": gfp,
       "gfpEvents": gfpEvents,
       "gfpLof": gfpLof,
       "gfpCsf": gfpCsf,
       "gfpCnfgTable": gfpCnfgTable,
       "gfpCnfgEntry": gfpCnfgEntry,
       "gfpCnfgIdx": gfpCnfgIdx,
       "gfpPayloadFcs": gfpPayloadFcs,
       "gfpRxTxScramble": gfpRxTxScramble,
       "gfpVcatHeader": gfpVcatHeader}
)
