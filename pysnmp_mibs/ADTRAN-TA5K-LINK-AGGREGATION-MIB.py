# SNMP MIB module (ADTRAN-TA5K-LINK-AGGREGATION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/adtran/ADTRAN-TA5K-LINK-AGGREGATION-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:31:00 2025
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

(adGenPortTrapIdentifier,) = mibBuilder.importSymbols(
    "ADTRAN-GENPORT-MIB",
    "adGenPortTrapIdentifier")

(adGenSlotInfoIndex,) = mibBuilder.importSymbols(
    "ADTRAN-GENSLOT-MIB",
    "adGenSlotInfoIndex")

(adTa5kLinkAggregation,
 adTa5kLinkAggregationID) = mibBuilder.importSymbols(
    "ADTRAN-GENTA5K-MIB",
    "adTa5kLinkAggregation",
    "adTa5kLinkAggregationID")

(adTrapInformSeqNum,) = mibBuilder.importSymbols(
    "ADTRAN-GENTRAPINFORM-MIB",
    "adTrapInformSeqNum")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(sysName,) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysName")

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
 MacAddress,
 PhysAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

adTa5kLinkAggregationModuleIdentity = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 67, 1, 33, 1)
)
if mibBuilder.loadTexts:
    adTa5kLinkAggregationModuleIdentity.setRevisions(
        ("2014-07-23 00:00",
         "2013-09-25 00:00",
         "2011-11-30 19:18",
         "2011-10-26 18:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AdTa5kLinkAggregationAlarmPrefix_ObjectIdentity = ObjectIdentity
adTa5kLinkAggregationAlarmPrefix = _AdTa5kLinkAggregationAlarmPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 33, 1)
)
_AdTa5kLinkAggregationAlarms_ObjectIdentity = ObjectIdentity
adTa5kLinkAggregationAlarms = _AdTa5kLinkAggregationAlarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 33, 1, 0)
)
_AdTa5kLinkAggregationProvisioning_ObjectIdentity = ObjectIdentity
adTa5kLinkAggregationProvisioning = _AdTa5kLinkAggregationProvisioning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 33, 2)
)
_AdTa5kLinkAggLACPProvTable_Object = MibTable
adTa5kLinkAggLACPProvTable = _AdTa5kLinkAggLACPProvTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 33, 2, 1)
)
if mibBuilder.loadTexts:
    adTa5kLinkAggLACPProvTable.setStatus("current")
_AdTa5kLinkAggLACPProvEntry_Object = MibTableRow
adTa5kLinkAggLACPProvEntry = _AdTa5kLinkAggLACPProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 33, 2, 1, 1)
)
adTa5kLinkAggLACPProvEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adTa5kLinkAggLACPProvEntry.setStatus("current")


class _AdTa5kLinkAggLACPMode_Type(Integer32):
    """Custom type adTa5kLinkAggLACPMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("active", 2),
          ("passive", 3))
    )


_AdTa5kLinkAggLACPMode_Type.__name__ = "Integer32"
_AdTa5kLinkAggLACPMode_Object = MibTableColumn
adTa5kLinkAggLACPMode = _AdTa5kLinkAggLACPMode_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 33, 2, 1, 1, 1),
    _AdTa5kLinkAggLACPMode_Type()
)
adTa5kLinkAggLACPMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTa5kLinkAggLACPMode.setStatus("current")


class _AdTa5kLinkAggLACPGrammar_Type(Integer32):
    """Custom type adTa5kLinkAggLACPGrammar based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("standbyAggregation", 1),
          ("noStandbyAggregation", 2))
    )


_AdTa5kLinkAggLACPGrammar_Type.__name__ = "Integer32"
_AdTa5kLinkAggLACPGrammar_Object = MibTableColumn
adTa5kLinkAggLACPGrammar = _AdTa5kLinkAggLACPGrammar_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 33, 2, 1, 1, 2),
    _AdTa5kLinkAggLACPGrammar_Type()
)
adTa5kLinkAggLACPGrammar.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTa5kLinkAggLACPGrammar.setStatus("current")
_AdTa5kLinkAggAlarmProvTable_Object = MibTable
adTa5kLinkAggAlarmProvTable = _AdTa5kLinkAggAlarmProvTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 33, 2, 2)
)
if mibBuilder.loadTexts:
    adTa5kLinkAggAlarmProvTable.setStatus("current")
_AdTa5kLinkAggAlarmProvEntry_Object = MibTableRow
adTa5kLinkAggAlarmProvEntry = _AdTa5kLinkAggAlarmProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 33, 2, 2, 1)
)
adTa5kLinkAggAlarmProvEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adTa5kLinkAggAlarmProvEntry.setStatus("current")


class _AdTa5kLinkAggLACPTimeOutAlarmEnable_Type(TruthValue):
    """Custom type adTa5kLinkAggLACPTimeOutAlarmEnable based on TruthValue"""
    defaultValue = 1


_AdTa5kLinkAggLACPTimeOutAlarmEnable_Type.__name__ = "TruthValue"
_AdTa5kLinkAggLACPTimeOutAlarmEnable_Object = MibTableColumn
adTa5kLinkAggLACPTimeOutAlarmEnable = _AdTa5kLinkAggLACPTimeOutAlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 33, 2, 2, 1, 1),
    _AdTa5kLinkAggLACPTimeOutAlarmEnable_Type()
)
adTa5kLinkAggLACPTimeOutAlarmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTa5kLinkAggLACPTimeOutAlarmEnable.setStatus("current")


class _AdTa5kLinkAggMinimumActiveLnkAlarmEnable_Type(TruthValue):
    """Custom type adTa5kLinkAggMinimumActiveLnkAlarmEnable based on TruthValue"""
    defaultValue = 1


_AdTa5kLinkAggMinimumActiveLnkAlarmEnable_Type.__name__ = "TruthValue"
_AdTa5kLinkAggMinimumActiveLnkAlarmEnable_Object = MibTableColumn
adTa5kLinkAggMinimumActiveLnkAlarmEnable = _AdTa5kLinkAggMinimumActiveLnkAlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 33, 2, 2, 1, 2),
    _AdTa5kLinkAggMinimumActiveLnkAlarmEnable_Type()
)
adTa5kLinkAggMinimumActiveLnkAlarmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTa5kLinkAggMinimumActiveLnkAlarmEnable.setStatus("current")
_AdTa5kLinkAggLACPSlotProvTable_Object = MibTable
adTa5kLinkAggLACPSlotProvTable = _AdTa5kLinkAggLACPSlotProvTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 33, 2, 3)
)
if mibBuilder.loadTexts:
    adTa5kLinkAggLACPSlotProvTable.setStatus("current")
_AdTa5kLinkAggLACPSlotProvEntry_Object = MibTableRow
adTa5kLinkAggLACPSlotProvEntry = _AdTa5kLinkAggLACPSlotProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 33, 2, 3, 1)
)
adTa5kLinkAggLACPSlotProvEntry.setIndexNames(
    (0, "ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
)
if mibBuilder.loadTexts:
    adTa5kLinkAggLACPSlotProvEntry.setStatus("current")


class _AdTa5kLinkAggLACPResponseMode_Type(Integer32):
    """Custom type adTa5kLinkAggLACPResponseMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("reporterOnly", 1),
          ("interactive", 2))
    )


_AdTa5kLinkAggLACPResponseMode_Type.__name__ = "Integer32"
_AdTa5kLinkAggLACPResponseMode_Object = MibTableColumn
adTa5kLinkAggLACPResponseMode = _AdTa5kLinkAggLACPResponseMode_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 33, 2, 3, 1, 1),
    _AdTa5kLinkAggLACPResponseMode_Type()
)
adTa5kLinkAggLACPResponseMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTa5kLinkAggLACPResponseMode.setStatus("current")


class _AdTa5kLinkAggLACPSlotSystemPriority_Type(Integer32):
    """Custom type adTa5kLinkAggLACPSlotSystemPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 35535),
    )


_AdTa5kLinkAggLACPSlotSystemPriority_Type.__name__ = "Integer32"
_AdTa5kLinkAggLACPSlotSystemPriority_Object = MibTableColumn
adTa5kLinkAggLACPSlotSystemPriority = _AdTa5kLinkAggLACPSlotSystemPriority_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 33, 2, 3, 1, 2),
    _AdTa5kLinkAggLACPSlotSystemPriority_Type()
)
adTa5kLinkAggLACPSlotSystemPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTa5kLinkAggLACPSlotSystemPriority.setStatus("current")
_AdTa5kLinkAggregationPerformance_ObjectIdentity = ObjectIdentity
adTa5kLinkAggregationPerformance = _AdTa5kLinkAggregationPerformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 33, 3)
)
_AdTa5kLinkAggLACPPortStatsTable_Object = MibTable
adTa5kLinkAggLACPPortStatsTable = _AdTa5kLinkAggLACPPortStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 33, 3, 1)
)
if mibBuilder.loadTexts:
    adTa5kLinkAggLACPPortStatsTable.setStatus("current")
_AdTa5kLinkAggLACPPortStatsEntry_Object = MibTableRow
adTa5kLinkAggLACPPortStatsEntry = _AdTa5kLinkAggLACPPortStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 33, 3, 1, 1)
)
adTa5kLinkAggLACPPortStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adTa5kLinkAggLACPPortStatsEntry.setStatus("current")
_AdTa5kLinkAggPortStatsLACPDUsTx_Type = Gauge32
_AdTa5kLinkAggPortStatsLACPDUsTx_Object = MibTableColumn
adTa5kLinkAggPortStatsLACPDUsTx = _AdTa5kLinkAggPortStatsLACPDUsTx_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 33, 3, 1, 1, 1),
    _AdTa5kLinkAggPortStatsLACPDUsTx_Type()
)
adTa5kLinkAggPortStatsLACPDUsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTa5kLinkAggPortStatsLACPDUsTx.setStatus("current")
_AdTa5kLinkAggPortStatsLACPDUsRx_Type = Gauge32
_AdTa5kLinkAggPortStatsLACPDUsRx_Object = MibTableColumn
adTa5kLinkAggPortStatsLACPDUsRx = _AdTa5kLinkAggPortStatsLACPDUsRx_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 33, 3, 1, 1, 2),
    _AdTa5kLinkAggPortStatsLACPDUsRx_Type()
)
adTa5kLinkAggPortStatsLACPDUsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTa5kLinkAggPortStatsLACPDUsRx.setStatus("current")
_AdTa5kLinkAggPortStatsMarkerPDUsRx_Type = Gauge32
_AdTa5kLinkAggPortStatsMarkerPDUsRx_Object = MibTableColumn
adTa5kLinkAggPortStatsMarkerPDUsRx = _AdTa5kLinkAggPortStatsMarkerPDUsRx_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 33, 3, 1, 1, 3),
    _AdTa5kLinkAggPortStatsMarkerPDUsRx_Type()
)
adTa5kLinkAggPortStatsMarkerPDUsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTa5kLinkAggPortStatsMarkerPDUsRx.setStatus("current")
_AdTa5kLinkAggPortStatsMarkerResponsePDUsTx_Type = Gauge32
_AdTa5kLinkAggPortStatsMarkerResponsePDUsTx_Object = MibTableColumn
adTa5kLinkAggPortStatsMarkerResponsePDUsTx = _AdTa5kLinkAggPortStatsMarkerResponsePDUsTx_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 33, 3, 1, 1, 4),
    _AdTa5kLinkAggPortStatsMarkerResponsePDUsTx_Type()
)
adTa5kLinkAggPortStatsMarkerResponsePDUsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTa5kLinkAggPortStatsMarkerResponsePDUsTx.setStatus("current")
_AdTa5kLinkAggregationStatus_ObjectIdentity = ObjectIdentity
adTa5kLinkAggregationStatus = _AdTa5kLinkAggregationStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 33, 4)
)
_AdTa5kLinkAggLACPStatusTable_Object = MibTable
adTa5kLinkAggLACPStatusTable = _AdTa5kLinkAggLACPStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 33, 4, 1)
)
if mibBuilder.loadTexts:
    adTa5kLinkAggLACPStatusTable.setStatus("current")
_AdTa5kLinkAggLACPStatusEntry_Object = MibTableRow
adTa5kLinkAggLACPStatusEntry = _AdTa5kLinkAggLACPStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 33, 4, 1, 1)
)
adTa5kLinkAggLACPStatusEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adTa5kLinkAggLACPStatusEntry.setStatus("current")
_AdTa5kLinkAggLACPSystemID_Type = MacAddress
_AdTa5kLinkAggLACPSystemID_Object = MibTableColumn
adTa5kLinkAggLACPSystemID = _AdTa5kLinkAggLACPSystemID_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 33, 4, 1, 1, 1),
    _AdTa5kLinkAggLACPSystemID_Type()
)
adTa5kLinkAggLACPSystemID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTa5kLinkAggLACPSystemID.setStatus("current")


class _AdTa5kLinkAggLACPSystemPriority_Type(Integer32):
    """Custom type adTa5kLinkAggLACPSystemPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AdTa5kLinkAggLACPSystemPriority_Type.__name__ = "Integer32"
_AdTa5kLinkAggLACPSystemPriority_Object = MibTableColumn
adTa5kLinkAggLACPSystemPriority = _AdTa5kLinkAggLACPSystemPriority_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 33, 4, 1, 1, 2),
    _AdTa5kLinkAggLACPSystemPriority_Type()
)
adTa5kLinkAggLACPSystemPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTa5kLinkAggLACPSystemPriority.setStatus("current")
_AdTa5kLinkAggLACPPortStatusTable_Object = MibTable
adTa5kLinkAggLACPPortStatusTable = _AdTa5kLinkAggLACPPortStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 33, 4, 2)
)
if mibBuilder.loadTexts:
    adTa5kLinkAggLACPPortStatusTable.setStatus("current")
_AdTa5kLinkAggLACPPortStatusEntry_Object = MibTableRow
adTa5kLinkAggLACPPortStatusEntry = _AdTa5kLinkAggLACPPortStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 33, 4, 2, 1)
)
adTa5kLinkAggLACPPortStatusEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adTa5kLinkAggLACPPortStatusEntry.setStatus("current")


class _AdTa5kLinkAggLACPActorPortState_Type(Bits):
    """Custom type adTa5kLinkAggLACPActorPortState based on Bits"""
    namedValues = NamedValues(
        *(("lacpActivity", 0),
          ("lacpTimeout", 1),
          ("aggregation", 2),
          ("synchronization", 3),
          ("collecting", 4),
          ("distributing", 5),
          ("defaulted", 6),
          ("expired", 7))
    )

_AdTa5kLinkAggLACPActorPortState_Type.__name__ = "Bits"
_AdTa5kLinkAggLACPActorPortState_Object = MibTableColumn
adTa5kLinkAggLACPActorPortState = _AdTa5kLinkAggLACPActorPortState_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 33, 4, 2, 1, 1),
    _AdTa5kLinkAggLACPActorPortState_Type()
)
adTa5kLinkAggLACPActorPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTa5kLinkAggLACPActorPortState.setStatus("current")


class _AdTa5kLinkAggLACPActorPortID_Type(Integer32):
    """Custom type adTa5kLinkAggLACPActorPortID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AdTa5kLinkAggLACPActorPortID_Type.__name__ = "Integer32"
_AdTa5kLinkAggLACPActorPortID_Object = MibTableColumn
adTa5kLinkAggLACPActorPortID = _AdTa5kLinkAggLACPActorPortID_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 33, 4, 2, 1, 2),
    _AdTa5kLinkAggLACPActorPortID_Type()
)
adTa5kLinkAggLACPActorPortID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTa5kLinkAggLACPActorPortID.setStatus("current")


class _AdTa5kLinkAggLACPActorPortKey_Type(Integer32):
    """Custom type adTa5kLinkAggLACPActorPortKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AdTa5kLinkAggLACPActorPortKey_Type.__name__ = "Integer32"
_AdTa5kLinkAggLACPActorPortKey_Object = MibTableColumn
adTa5kLinkAggLACPActorPortKey = _AdTa5kLinkAggLACPActorPortKey_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 33, 4, 2, 1, 3),
    _AdTa5kLinkAggLACPActorPortKey_Type()
)
adTa5kLinkAggLACPActorPortKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTa5kLinkAggLACPActorPortKey.setStatus("current")


class _AdTa5kLinkAggLACPActorPortPriority_Type(Integer32):
    """Custom type adTa5kLinkAggLACPActorPortPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AdTa5kLinkAggLACPActorPortPriority_Type.__name__ = "Integer32"
_AdTa5kLinkAggLACPActorPortPriority_Object = MibTableColumn
adTa5kLinkAggLACPActorPortPriority = _AdTa5kLinkAggLACPActorPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 33, 4, 2, 1, 4),
    _AdTa5kLinkAggLACPActorPortPriority_Type()
)
adTa5kLinkAggLACPActorPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTa5kLinkAggLACPActorPortPriority.setStatus("current")


class _AdTa5kLinkAggLACPPartnerPortState_Type(Bits):
    """Custom type adTa5kLinkAggLACPPartnerPortState based on Bits"""
    namedValues = NamedValues(
        *(("lacpActivity", 0),
          ("lacpTimeout", 1),
          ("aggregation", 2),
          ("synchronization", 3),
          ("collecting", 4),
          ("distributing", 5),
          ("defaulted", 6),
          ("expired", 7))
    )

_AdTa5kLinkAggLACPPartnerPortState_Type.__name__ = "Bits"
_AdTa5kLinkAggLACPPartnerPortState_Object = MibTableColumn
adTa5kLinkAggLACPPartnerPortState = _AdTa5kLinkAggLACPPartnerPortState_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 33, 4, 2, 1, 5),
    _AdTa5kLinkAggLACPPartnerPortState_Type()
)
adTa5kLinkAggLACPPartnerPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTa5kLinkAggLACPPartnerPortState.setStatus("current")


class _AdTa5kLinkAggLACPPartnerPortID_Type(Integer32):
    """Custom type adTa5kLinkAggLACPPartnerPortID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AdTa5kLinkAggLACPPartnerPortID_Type.__name__ = "Integer32"
_AdTa5kLinkAggLACPPartnerPortID_Object = MibTableColumn
adTa5kLinkAggLACPPartnerPortID = _AdTa5kLinkAggLACPPartnerPortID_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 33, 4, 2, 1, 6),
    _AdTa5kLinkAggLACPPartnerPortID_Type()
)
adTa5kLinkAggLACPPartnerPortID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTa5kLinkAggLACPPartnerPortID.setStatus("current")


class _AdTa5kLinkAggLACPPartnerPortKey_Type(Integer32):
    """Custom type adTa5kLinkAggLACPPartnerPortKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AdTa5kLinkAggLACPPartnerPortKey_Type.__name__ = "Integer32"
_AdTa5kLinkAggLACPPartnerPortKey_Object = MibTableColumn
adTa5kLinkAggLACPPartnerPortKey = _AdTa5kLinkAggLACPPartnerPortKey_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 33, 4, 2, 1, 7),
    _AdTa5kLinkAggLACPPartnerPortKey_Type()
)
adTa5kLinkAggLACPPartnerPortKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTa5kLinkAggLACPPartnerPortKey.setStatus("current")


class _AdTa5kLinkAggLACPPartnerPortPriority_Type(Integer32):
    """Custom type adTa5kLinkAggLACPPartnerPortPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AdTa5kLinkAggLACPPartnerPortPriority_Type.__name__ = "Integer32"
_AdTa5kLinkAggLACPPartnerPortPriority_Object = MibTableColumn
adTa5kLinkAggLACPPartnerPortPriority = _AdTa5kLinkAggLACPPartnerPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 33, 4, 2, 1, 8),
    _AdTa5kLinkAggLACPPartnerPortPriority_Type()
)
adTa5kLinkAggLACPPartnerPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTa5kLinkAggLACPPartnerPortPriority.setStatus("current")
_AdTa5kLinkAggLACPPartnerPortSystemID_Type = MacAddress
_AdTa5kLinkAggLACPPartnerPortSystemID_Object = MibTableColumn
adTa5kLinkAggLACPPartnerPortSystemID = _AdTa5kLinkAggLACPPartnerPortSystemID_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 33, 4, 2, 1, 9),
    _AdTa5kLinkAggLACPPartnerPortSystemID_Type()
)
adTa5kLinkAggLACPPartnerPortSystemID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTa5kLinkAggLACPPartnerPortSystemID.setStatus("current")


class _AdTa5kLinkAggLACPPartnerPortSystemPriority_Type(Integer32):
    """Custom type adTa5kLinkAggLACPPartnerPortSystemPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AdTa5kLinkAggLACPPartnerPortSystemPriority_Type.__name__ = "Integer32"
_AdTa5kLinkAggLACPPartnerPortSystemPriority_Object = MibTableColumn
adTa5kLinkAggLACPPartnerPortSystemPriority = _AdTa5kLinkAggLACPPartnerPortSystemPriority_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 33, 4, 2, 1, 10),
    _AdTa5kLinkAggLACPPartnerPortSystemPriority_Type()
)
adTa5kLinkAggLACPPartnerPortSystemPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTa5kLinkAggLACPPartnerPortSystemPriority.setStatus("current")
_AdTa5kLinkAggLACPStateMachineTable_Object = MibTable
adTa5kLinkAggLACPStateMachineTable = _AdTa5kLinkAggLACPStateMachineTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 33, 4, 3)
)
if mibBuilder.loadTexts:
    adTa5kLinkAggLACPStateMachineTable.setStatus("current")
_AdTa5kLinkAggLACPStateMachineEntry_Object = MibTableRow
adTa5kLinkAggLACPStateMachineEntry = _AdTa5kLinkAggLACPStateMachineEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 33, 4, 3, 1)
)
adTa5kLinkAggLACPStateMachineEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adTa5kLinkAggLACPStateMachineEntry.setStatus("current")


class _AdTa5kLinkAggLACPSelectedState_Type(Integer32):
    """Custom type adTa5kLinkAggLACPSelectedState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("unselected", 0),
          ("selected", 1),
          ("standby", 2),
          ("notAvailable", 255))
    )


_AdTa5kLinkAggLACPSelectedState_Type.__name__ = "Integer32"
_AdTa5kLinkAggLACPSelectedState_Object = MibTableColumn
adTa5kLinkAggLACPSelectedState = _AdTa5kLinkAggLACPSelectedState_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 33, 4, 3, 1, 1),
    _AdTa5kLinkAggLACPSelectedState_Type()
)
adTa5kLinkAggLACPSelectedState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTa5kLinkAggLACPSelectedState.setStatus("current")


class _AdTa5kLinkAggLACPReceiveState_Type(Integer32):
    """Custom type adTa5kLinkAggLACPReceiveState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              255)
        )
    )
    namedValues = NamedValues(
        *(("initialize", 0),
          ("portDisabled", 1),
          ("expired", 2),
          ("lacpDisabled", 3),
          ("defaulted", 4),
          ("current", 5),
          ("notAvailable", 255))
    )


_AdTa5kLinkAggLACPReceiveState_Type.__name__ = "Integer32"
_AdTa5kLinkAggLACPReceiveState_Object = MibTableColumn
adTa5kLinkAggLACPReceiveState = _AdTa5kLinkAggLACPReceiveState_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 33, 4, 3, 1, 2),
    _AdTa5kLinkAggLACPReceiveState_Type()
)
adTa5kLinkAggLACPReceiveState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTa5kLinkAggLACPReceiveState.setStatus("current")


class _AdTa5kLinkAggLACPPeriodicTxState_Type(Integer32):
    """Custom type adTa5kLinkAggLACPPeriodicTxState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              255)
        )
    )
    namedValues = NamedValues(
        *(("noPeriodic", 0),
          ("fastPeriodic", 1),
          ("slowPeriodic", 2),
          ("periodicTx", 3),
          ("notAvailable", 255))
    )


_AdTa5kLinkAggLACPPeriodicTxState_Type.__name__ = "Integer32"
_AdTa5kLinkAggLACPPeriodicTxState_Object = MibTableColumn
adTa5kLinkAggLACPPeriodicTxState = _AdTa5kLinkAggLACPPeriodicTxState_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 33, 4, 3, 1, 3),
    _AdTa5kLinkAggLACPPeriodicTxState_Type()
)
adTa5kLinkAggLACPPeriodicTxState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTa5kLinkAggLACPPeriodicTxState.setStatus("current")


class _AdTa5kLinkAggLACPMuxState_Type(Integer32):
    """Custom type adTa5kLinkAggLACPMuxState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              255)
        )
    )
    namedValues = NamedValues(
        *(("detached", 0),
          ("waiting", 1),
          ("attached", 2),
          ("collecting", 3),
          ("distributing", 4),
          ("notAvailable", 255))
    )


_AdTa5kLinkAggLACPMuxState_Type.__name__ = "Integer32"
_AdTa5kLinkAggLACPMuxState_Object = MibTableColumn
adTa5kLinkAggLACPMuxState = _AdTa5kLinkAggLACPMuxState_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 33, 4, 3, 1, 4),
    _AdTa5kLinkAggLACPMuxState_Type()
)
adTa5kLinkAggLACPMuxState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTa5kLinkAggLACPMuxState.setStatus("current")

# Managed Objects groups


# Notification objects

adTa5kSmLACPTimeOutClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 33, 1, 0, 2)
)
adTa5kSmLACPTimeOutClear.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"))
)
if mibBuilder.loadTexts:
    adTa5kSmLACPTimeOutClear.setStatus(
        "current"
    )

adTa5kSmLACPTimeOutActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 33, 1, 0, 3)
)
adTa5kSmLACPTimeOutActive.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"))
)
if mibBuilder.loadTexts:
    adTa5kSmLACPTimeOutActive.setStatus(
        "current"
    )

adTa5kSmUnderMiniActiveLnkClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 33, 1, 0, 4)
)
adTa5kSmUnderMiniActiveLnkClear.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adTa5kSmUnderMiniActiveLnkClear.setStatus(
        "current"
    )

adTa5kSmUnderMiniActiveLnk = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 33, 1, 0, 5)
)
adTa5kSmUnderMiniActiveLnk.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adTa5kSmUnderMiniActiveLnk.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ADTRAN-TA5K-LINK-AGGREGATION-MIB",
    **{"adTa5kLinkAggregationAlarmPrefix": adTa5kLinkAggregationAlarmPrefix,
       "adTa5kLinkAggregationAlarms": adTa5kLinkAggregationAlarms,
       "adTa5kSmLACPTimeOutClear": adTa5kSmLACPTimeOutClear,
       "adTa5kSmLACPTimeOutActive": adTa5kSmLACPTimeOutActive,
       "adTa5kSmUnderMiniActiveLnkClear": adTa5kSmUnderMiniActiveLnkClear,
       "adTa5kSmUnderMiniActiveLnk": adTa5kSmUnderMiniActiveLnk,
       "adTa5kLinkAggregationProvisioning": adTa5kLinkAggregationProvisioning,
       "adTa5kLinkAggLACPProvTable": adTa5kLinkAggLACPProvTable,
       "adTa5kLinkAggLACPProvEntry": adTa5kLinkAggLACPProvEntry,
       "adTa5kLinkAggLACPMode": adTa5kLinkAggLACPMode,
       "adTa5kLinkAggLACPGrammar": adTa5kLinkAggLACPGrammar,
       "adTa5kLinkAggAlarmProvTable": adTa5kLinkAggAlarmProvTable,
       "adTa5kLinkAggAlarmProvEntry": adTa5kLinkAggAlarmProvEntry,
       "adTa5kLinkAggLACPTimeOutAlarmEnable": adTa5kLinkAggLACPTimeOutAlarmEnable,
       "adTa5kLinkAggMinimumActiveLnkAlarmEnable": adTa5kLinkAggMinimumActiveLnkAlarmEnable,
       "adTa5kLinkAggLACPSlotProvTable": adTa5kLinkAggLACPSlotProvTable,
       "adTa5kLinkAggLACPSlotProvEntry": adTa5kLinkAggLACPSlotProvEntry,
       "adTa5kLinkAggLACPResponseMode": adTa5kLinkAggLACPResponseMode,
       "adTa5kLinkAggLACPSlotSystemPriority": adTa5kLinkAggLACPSlotSystemPriority,
       "adTa5kLinkAggregationPerformance": adTa5kLinkAggregationPerformance,
       "adTa5kLinkAggLACPPortStatsTable": adTa5kLinkAggLACPPortStatsTable,
       "adTa5kLinkAggLACPPortStatsEntry": adTa5kLinkAggLACPPortStatsEntry,
       "adTa5kLinkAggPortStatsLACPDUsTx": adTa5kLinkAggPortStatsLACPDUsTx,
       "adTa5kLinkAggPortStatsLACPDUsRx": adTa5kLinkAggPortStatsLACPDUsRx,
       "adTa5kLinkAggPortStatsMarkerPDUsRx": adTa5kLinkAggPortStatsMarkerPDUsRx,
       "adTa5kLinkAggPortStatsMarkerResponsePDUsTx": adTa5kLinkAggPortStatsMarkerResponsePDUsTx,
       "adTa5kLinkAggregationStatus": adTa5kLinkAggregationStatus,
       "adTa5kLinkAggLACPStatusTable": adTa5kLinkAggLACPStatusTable,
       "adTa5kLinkAggLACPStatusEntry": adTa5kLinkAggLACPStatusEntry,
       "adTa5kLinkAggLACPSystemID": adTa5kLinkAggLACPSystemID,
       "adTa5kLinkAggLACPSystemPriority": adTa5kLinkAggLACPSystemPriority,
       "adTa5kLinkAggLACPPortStatusTable": adTa5kLinkAggLACPPortStatusTable,
       "adTa5kLinkAggLACPPortStatusEntry": adTa5kLinkAggLACPPortStatusEntry,
       "adTa5kLinkAggLACPActorPortState": adTa5kLinkAggLACPActorPortState,
       "adTa5kLinkAggLACPActorPortID": adTa5kLinkAggLACPActorPortID,
       "adTa5kLinkAggLACPActorPortKey": adTa5kLinkAggLACPActorPortKey,
       "adTa5kLinkAggLACPActorPortPriority": adTa5kLinkAggLACPActorPortPriority,
       "adTa5kLinkAggLACPPartnerPortState": adTa5kLinkAggLACPPartnerPortState,
       "adTa5kLinkAggLACPPartnerPortID": adTa5kLinkAggLACPPartnerPortID,
       "adTa5kLinkAggLACPPartnerPortKey": adTa5kLinkAggLACPPartnerPortKey,
       "adTa5kLinkAggLACPPartnerPortPriority": adTa5kLinkAggLACPPartnerPortPriority,
       "adTa5kLinkAggLACPPartnerPortSystemID": adTa5kLinkAggLACPPartnerPortSystemID,
       "adTa5kLinkAggLACPPartnerPortSystemPriority": adTa5kLinkAggLACPPartnerPortSystemPriority,
       "adTa5kLinkAggLACPStateMachineTable": adTa5kLinkAggLACPStateMachineTable,
       "adTa5kLinkAggLACPStateMachineEntry": adTa5kLinkAggLACPStateMachineEntry,
       "adTa5kLinkAggLACPSelectedState": adTa5kLinkAggLACPSelectedState,
       "adTa5kLinkAggLACPReceiveState": adTa5kLinkAggLACPReceiveState,
       "adTa5kLinkAggLACPPeriodicTxState": adTa5kLinkAggLACPPeriodicTxState,
       "adTa5kLinkAggLACPMuxState": adTa5kLinkAggLACPMuxState,
       "adTa5kLinkAggregationModuleIdentity": adTa5kLinkAggregationModuleIdentity}
)
