# SNMP MIB module (INFINERA-PM-OSCCTP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/INFINERA-PM-OSCCTP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:15:21 2025
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(perfMon,) = mibBuilder.importSymbols(
    "INFINERA-REG-MIB",
    "perfMon")

(FloatHundredths,) = mibBuilder.importSymbols(
    "INFINERA-TC-MIB",
    "FloatHundredths")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

oscCtpPmMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 10)
)
if mibBuilder.loadTexts:
    oscCtpPmMIB.setRevisions(
        ("2008-10-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_OscCtpPmRealTable_Object = MibTable
oscCtpPmRealTable = _OscCtpPmRealTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 10, 1)
)
if mibBuilder.loadTexts:
    oscCtpPmRealTable.setStatus("current")
_OscCtpPmRealEntry_Object = MibTableRow
oscCtpPmRealEntry = _OscCtpPmRealEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 10, 1, 1)
)
oscCtpPmRealEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    oscCtpPmRealEntry.setStatus("current")
_OscCtpPmRealOscLBC_Type = FloatHundredths
_OscCtpPmRealOscLBC_Object = MibTableColumn
oscCtpPmRealOscLBC = _OscCtpPmRealOscLBC_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 10, 1, 1, 1),
    _OscCtpPmRealOscLBC_Type()
)
oscCtpPmRealOscLBC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oscCtpPmRealOscLBC.setStatus("current")
_OscCtpPmRealOscOPT_Type = FloatHundredths
_OscCtpPmRealOscOPT_Object = MibTableColumn
oscCtpPmRealOscOPT = _OscCtpPmRealOscOPT_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 10, 1, 1, 2),
    _OscCtpPmRealOscOPT_Type()
)
oscCtpPmRealOscOPT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oscCtpPmRealOscOPT.setStatus("current")
_OscCtpPmRealOscOPR_Type = FloatHundredths
_OscCtpPmRealOscOPR_Object = MibTableColumn
oscCtpPmRealOscOPR = _OscCtpPmRealOscOPR_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 10, 1, 1, 3),
    _OscCtpPmRealOscOPR_Type()
)
oscCtpPmRealOscOPR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oscCtpPmRealOscOPR.setStatus("current")
_OscCtpPmRealOscTxBytes_Type = Counter64
_OscCtpPmRealOscTxBytes_Object = MibTableColumn
oscCtpPmRealOscTxBytes = _OscCtpPmRealOscTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 10, 1, 1, 4),
    _OscCtpPmRealOscTxBytes_Type()
)
oscCtpPmRealOscTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oscCtpPmRealOscTxBytes.setStatus("current")
_OscCtpPmRealOscTxPkts_Type = Counter64
_OscCtpPmRealOscTxPkts_Object = MibTableColumn
oscCtpPmRealOscTxPkts = _OscCtpPmRealOscTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 10, 1, 1, 5),
    _OscCtpPmRealOscTxPkts_Type()
)
oscCtpPmRealOscTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oscCtpPmRealOscTxPkts.setStatus("current")
_OscCtpPmRealOscTxPktsDropped_Type = Counter64
_OscCtpPmRealOscTxPktsDropped_Object = MibTableColumn
oscCtpPmRealOscTxPktsDropped = _OscCtpPmRealOscTxPktsDropped_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 10, 1, 1, 6),
    _OscCtpPmRealOscTxPktsDropped_Type()
)
oscCtpPmRealOscTxPktsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oscCtpPmRealOscTxPktsDropped.setStatus("current")
_OscCtpPmRealOscRxBytes_Type = Counter64
_OscCtpPmRealOscRxBytes_Object = MibTableColumn
oscCtpPmRealOscRxBytes = _OscCtpPmRealOscRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 10, 1, 1, 7),
    _OscCtpPmRealOscRxBytes_Type()
)
oscCtpPmRealOscRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oscCtpPmRealOscRxBytes.setStatus("current")
_OscCtpPmRealOscRxPkts_Type = Counter64
_OscCtpPmRealOscRxPkts_Object = MibTableColumn
oscCtpPmRealOscRxPkts = _OscCtpPmRealOscRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 10, 1, 1, 8),
    _OscCtpPmRealOscRxPkts_Type()
)
oscCtpPmRealOscRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oscCtpPmRealOscRxPkts.setStatus("current")
_OscCtpPmRealOscRxPktsDropped_Type = Counter64
_OscCtpPmRealOscRxPktsDropped_Object = MibTableColumn
oscCtpPmRealOscRxPktsDropped = _OscCtpPmRealOscRxPktsDropped_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 10, 1, 1, 9),
    _OscCtpPmRealOscRxPktsDropped_Type()
)
oscCtpPmRealOscRxPktsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oscCtpPmRealOscRxPktsDropped.setStatus("current")
_OscCtpPmRealOscXOverOPR_Type = FloatHundredths
_OscCtpPmRealOscXOverOPR_Object = MibTableColumn
oscCtpPmRealOscXOverOPR = _OscCtpPmRealOscXOverOPR_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 10, 1, 1, 10),
    _OscCtpPmRealOscXOverOPR_Type()
)
oscCtpPmRealOscXOverOPR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oscCtpPmRealOscXOverOPR.setStatus("current")
_OscCtpPmTable_Object = MibTable
oscCtpPmTable = _OscCtpPmTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 10, 2)
)
if mibBuilder.loadTexts:
    oscCtpPmTable.setStatus("current")
_OscCtpPmEntry_Object = MibTableRow
oscCtpPmEntry = _OscCtpPmEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 10, 2, 1)
)
oscCtpPmEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "INFINERA-PM-OSCCTP-MIB", "oscCtpPmSampleDuration"),
    (0, "INFINERA-PM-OSCCTP-MIB", "oscCtpPmTimestamp"),
)
if mibBuilder.loadTexts:
    oscCtpPmEntry.setStatus("current")


class _OscCtpPmTimestamp_Type(Integer32):
    """Custom type oscCtpPmTimestamp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_OscCtpPmTimestamp_Type.__name__ = "Integer32"
_OscCtpPmTimestamp_Object = MibTableColumn
oscCtpPmTimestamp = _OscCtpPmTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 10, 2, 1, 1),
    _OscCtpPmTimestamp_Type()
)
oscCtpPmTimestamp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    oscCtpPmTimestamp.setStatus("current")


class _OscCtpPmSampleDuration_Type(Integer32):
    """Custom type oscCtpPmSampleDuration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fifteenMinutes", 1),
          ("day", 2))
    )


_OscCtpPmSampleDuration_Type.__name__ = "Integer32"
_OscCtpPmSampleDuration_Object = MibTableColumn
oscCtpPmSampleDuration = _OscCtpPmSampleDuration_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 10, 2, 1, 2),
    _OscCtpPmSampleDuration_Type()
)
oscCtpPmSampleDuration.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    oscCtpPmSampleDuration.setStatus("current")
_OscCtpPmValidity_Type = TruthValue
_OscCtpPmValidity_Object = MibTableColumn
oscCtpPmValidity = _OscCtpPmValidity_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 10, 2, 1, 3),
    _OscCtpPmValidity_Type()
)
oscCtpPmValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oscCtpPmValidity.setStatus("current")
_OscCtpPmOscLBCMin_Type = FloatHundredths
_OscCtpPmOscLBCMin_Object = MibTableColumn
oscCtpPmOscLBCMin = _OscCtpPmOscLBCMin_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 10, 2, 1, 4),
    _OscCtpPmOscLBCMin_Type()
)
oscCtpPmOscLBCMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oscCtpPmOscLBCMin.setStatus("current")
_OscCtpPmOscLBCMax_Type = FloatHundredths
_OscCtpPmOscLBCMax_Object = MibTableColumn
oscCtpPmOscLBCMax = _OscCtpPmOscLBCMax_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 10, 2, 1, 5),
    _OscCtpPmOscLBCMax_Type()
)
oscCtpPmOscLBCMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oscCtpPmOscLBCMax.setStatus("current")
_OscCtpPmOscLBCAve_Type = FloatHundredths
_OscCtpPmOscLBCAve_Object = MibTableColumn
oscCtpPmOscLBCAve = _OscCtpPmOscLBCAve_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 10, 2, 1, 6),
    _OscCtpPmOscLBCAve_Type()
)
oscCtpPmOscLBCAve.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oscCtpPmOscLBCAve.setStatus("current")
_OscCtpPmOscOPTMin_Type = FloatHundredths
_OscCtpPmOscOPTMin_Object = MibTableColumn
oscCtpPmOscOPTMin = _OscCtpPmOscOPTMin_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 10, 2, 1, 7),
    _OscCtpPmOscOPTMin_Type()
)
oscCtpPmOscOPTMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oscCtpPmOscOPTMin.setStatus("current")
_OscCtpPmOscOPTMax_Type = FloatHundredths
_OscCtpPmOscOPTMax_Object = MibTableColumn
oscCtpPmOscOPTMax = _OscCtpPmOscOPTMax_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 10, 2, 1, 8),
    _OscCtpPmOscOPTMax_Type()
)
oscCtpPmOscOPTMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oscCtpPmOscOPTMax.setStatus("current")
_OscCtpPmOscOPTAve_Type = FloatHundredths
_OscCtpPmOscOPTAve_Object = MibTableColumn
oscCtpPmOscOPTAve = _OscCtpPmOscOPTAve_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 10, 2, 1, 9),
    _OscCtpPmOscOPTAve_Type()
)
oscCtpPmOscOPTAve.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oscCtpPmOscOPTAve.setStatus("current")
_OscCtpPmOscOPRMin_Type = FloatHundredths
_OscCtpPmOscOPRMin_Object = MibTableColumn
oscCtpPmOscOPRMin = _OscCtpPmOscOPRMin_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 10, 2, 1, 10),
    _OscCtpPmOscOPRMin_Type()
)
oscCtpPmOscOPRMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oscCtpPmOscOPRMin.setStatus("current")
_OscCtpPmOscOPRMax_Type = FloatHundredths
_OscCtpPmOscOPRMax_Object = MibTableColumn
oscCtpPmOscOPRMax = _OscCtpPmOscOPRMax_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 10, 2, 1, 11),
    _OscCtpPmOscOPRMax_Type()
)
oscCtpPmOscOPRMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oscCtpPmOscOPRMax.setStatus("current")
_OscCtpPmOscOPRAve_Type = FloatHundredths
_OscCtpPmOscOPRAve_Object = MibTableColumn
oscCtpPmOscOPRAve = _OscCtpPmOscOPRAve_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 10, 2, 1, 12),
    _OscCtpPmOscOPRAve_Type()
)
oscCtpPmOscOPRAve.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oscCtpPmOscOPRAve.setStatus("current")
_OscCtpPmConformance_ObjectIdentity = ObjectIdentity
oscCtpPmConformance = _OscCtpPmConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 10, 3)
)
_OscCtpPmCompliances_ObjectIdentity = ObjectIdentity
oscCtpPmCompliances = _OscCtpPmCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 10, 3, 1)
)
_OscCtpPmGroups_ObjectIdentity = ObjectIdentity
oscCtpPmGroups = _OscCtpPmGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 10, 3, 2)
)

# Managed Objects groups

oscCtpPmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 10, 3, 2, 1)
)
oscCtpPmGroup.setObjects(
      *(("INFINERA-PM-OSCCTP-MIB", "oscCtpPmValidity"),
        ("INFINERA-PM-OSCCTP-MIB", "oscCtpPmOscLBCMin"),
        ("INFINERA-PM-OSCCTP-MIB", "oscCtpPmOscLBCMax"),
        ("INFINERA-PM-OSCCTP-MIB", "oscCtpPmOscLBCAve"),
        ("INFINERA-PM-OSCCTP-MIB", "oscCtpPmOscOPTMin"),
        ("INFINERA-PM-OSCCTP-MIB", "oscCtpPmOscOPTMax"),
        ("INFINERA-PM-OSCCTP-MIB", "oscCtpPmOscOPTAve"),
        ("INFINERA-PM-OSCCTP-MIB", "oscCtpPmOscOPRMin"),
        ("INFINERA-PM-OSCCTP-MIB", "oscCtpPmOscOPRMax"),
        ("INFINERA-PM-OSCCTP-MIB", "oscCtpPmOscOPRAve"))
)
if mibBuilder.loadTexts:
    oscCtpPmGroup.setStatus("current")

oscCtpPmRealGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 10, 3, 2, 2)
)
oscCtpPmRealGroup.setObjects(
      *(("INFINERA-PM-OSCCTP-MIB", "oscCtpPmRealOscLBC"),
        ("INFINERA-PM-OSCCTP-MIB", "oscCtpPmRealOscOPT"),
        ("INFINERA-PM-OSCCTP-MIB", "oscCtpPmRealOscOPR"),
        ("INFINERA-PM-OSCCTP-MIB", "oscCtpPmRealOscTxBytes"),
        ("INFINERA-PM-OSCCTP-MIB", "oscCtpPmRealOscTxPkts"),
        ("INFINERA-PM-OSCCTP-MIB", "oscCtpPmRealOscTxPktsDropped"),
        ("INFINERA-PM-OSCCTP-MIB", "oscCtpPmRealOscRxBytes"),
        ("INFINERA-PM-OSCCTP-MIB", "oscCtpPmRealOscRxPkts"),
        ("INFINERA-PM-OSCCTP-MIB", "oscCtpPmRealOscRxPktsDropped"),
        ("INFINERA-PM-OSCCTP-MIB", "oscCtpPmRealOscXOverOPR"))
)
if mibBuilder.loadTexts:
    oscCtpPmRealGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

oscCtpPmCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 10, 3, 1, 1)
)
oscCtpPmCompliance.setObjects(
    ("INFINERA-PM-OSCCTP-MIB", "oscCtpPmGroup")
)
if mibBuilder.loadTexts:
    oscCtpPmCompliance.setStatus(
        "current"
    )

oscCtpPmRealCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 10, 3, 1, 2)
)
oscCtpPmRealCompliance.setObjects(
    ("INFINERA-PM-OSCCTP-MIB", "oscCtpPmRealGroup")
)
if mibBuilder.loadTexts:
    oscCtpPmRealCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INFINERA-PM-OSCCTP-MIB",
    **{"oscCtpPmMIB": oscCtpPmMIB,
       "oscCtpPmRealTable": oscCtpPmRealTable,
       "oscCtpPmRealEntry": oscCtpPmRealEntry,
       "oscCtpPmRealOscLBC": oscCtpPmRealOscLBC,
       "oscCtpPmRealOscOPT": oscCtpPmRealOscOPT,
       "oscCtpPmRealOscOPR": oscCtpPmRealOscOPR,
       "oscCtpPmRealOscTxBytes": oscCtpPmRealOscTxBytes,
       "oscCtpPmRealOscTxPkts": oscCtpPmRealOscTxPkts,
       "oscCtpPmRealOscTxPktsDropped": oscCtpPmRealOscTxPktsDropped,
       "oscCtpPmRealOscRxBytes": oscCtpPmRealOscRxBytes,
       "oscCtpPmRealOscRxPkts": oscCtpPmRealOscRxPkts,
       "oscCtpPmRealOscRxPktsDropped": oscCtpPmRealOscRxPktsDropped,
       "oscCtpPmRealOscXOverOPR": oscCtpPmRealOscXOverOPR,
       "oscCtpPmTable": oscCtpPmTable,
       "oscCtpPmEntry": oscCtpPmEntry,
       "oscCtpPmTimestamp": oscCtpPmTimestamp,
       "oscCtpPmSampleDuration": oscCtpPmSampleDuration,
       "oscCtpPmValidity": oscCtpPmValidity,
       "oscCtpPmOscLBCMin": oscCtpPmOscLBCMin,
       "oscCtpPmOscLBCMax": oscCtpPmOscLBCMax,
       "oscCtpPmOscLBCAve": oscCtpPmOscLBCAve,
       "oscCtpPmOscOPTMin": oscCtpPmOscOPTMin,
       "oscCtpPmOscOPTMax": oscCtpPmOscOPTMax,
       "oscCtpPmOscOPTAve": oscCtpPmOscOPTAve,
       "oscCtpPmOscOPRMin": oscCtpPmOscOPRMin,
       "oscCtpPmOscOPRMax": oscCtpPmOscOPRMax,
       "oscCtpPmOscOPRAve": oscCtpPmOscOPRAve,
       "oscCtpPmConformance": oscCtpPmConformance,
       "oscCtpPmCompliances": oscCtpPmCompliances,
       "oscCtpPmCompliance": oscCtpPmCompliance,
       "oscCtpPmRealCompliance": oscCtpPmRealCompliance,
       "oscCtpPmGroups": oscCtpPmGroups,
       "oscCtpPmGroup": oscCtpPmGroup,
       "oscCtpPmRealGroup": oscCtpPmRealGroup}
)
