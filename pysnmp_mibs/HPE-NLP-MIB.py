# SNMP MIB module (HPE-NLP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/hp/HPE-NLP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:36:40 2025
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

(hpVCSE_40Gb_F8_Module,) = mibBuilder.importSymbols(
    "HPSVRMGMT-OID",
    "hpVCSE-40Gb-F8-Module")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(snmpTraps,) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "snmpTraps")

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
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

hpeNLPMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 8, 1, 4060)
)
if mibBuilder.loadTexts:
    hpeNLPMIB.setRevisions(
        ("2019-03-05 00:00",
         "2015-07-07 18:31")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HpeSynergyVCMIBObjects_ObjectIdentity = ObjectIdentity
hpeSynergyVCMIBObjects = _HpeSynergyVCMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 8, 1)
)


class _HpeNLPModuleConfig_Type(Integer32):
    """Custom type hpeNLPModuleConfig based on Integer32"""
    defaultValue = 1

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


_HpeNLPModuleConfig_Type.__name__ = "Integer32"
_HpeNLPModuleConfig_Object = MibScalar
hpeNLPModuleConfig = _HpeNLPModuleConfig_Object(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 8, 1, 4060, 1),
    _HpeNLPModuleConfig_Type()
)
hpeNLPModuleConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpeNLPModuleConfig.setStatus("current")


class _HpeNLPResetLoopDetection_Type(TruthValue):
    """Custom type hpeNLPResetLoopDetection based on TruthValue"""
    defaultValue = 2


_HpeNLPResetLoopDetection_Type.__name__ = "TruthValue"
_HpeNLPResetLoopDetection_Object = MibScalar
hpeNLPResetLoopDetection = _HpeNLPResetLoopDetection_Object(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 8, 1, 4060, 2),
    _HpeNLPResetLoopDetection_Type()
)
hpeNLPResetLoopDetection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpeNLPResetLoopDetection.setStatus("current")


class _HpeNLPTransmitInterval_Type(Integer32):
    """Custom type hpeNLPTransmitInterval based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 10),
    )


_HpeNLPTransmitInterval_Type.__name__ = "Integer32"
_HpeNLPTransmitInterval_Object = MibScalar
hpeNLPTransmitInterval = _HpeNLPTransmitInterval_Object(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 8, 1, 4060, 3),
    _HpeNLPTransmitInterval_Type()
)
hpeNLPTransmitInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpeNLPTransmitInterval.setStatus("current")


class _HpeNLPEnableTrap_Type(Integer32):
    """Custom type hpeNLPEnableTrap based on Integer32"""
    defaultValue = 1

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


_HpeNLPEnableTrap_Type.__name__ = "Integer32"
_HpeNLPEnableTrap_Object = MibScalar
hpeNLPEnableTrap = _HpeNLPEnableTrap_Object(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 8, 1, 4060, 4),
    _HpeNLPEnableTrap_Type()
)
hpeNLPEnableTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpeNLPEnableTrap.setStatus("current")
_HpeNLPServerPortTable_Object = MibTable
hpeNLPServerPortTable = _HpeNLPServerPortTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 8, 1, 4060, 5)
)
if mibBuilder.loadTexts:
    hpeNLPServerPortTable.setStatus("current")
_HpeNLPServerPortEntry_Object = MibTableRow
hpeNLPServerPortEntry = _HpeNLPServerPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 8, 1, 4060, 5, 1)
)
hpeNLPServerPortEntry.setIndexNames(
    (0, "HPE-NLP-MIB", "hpeNLPServerPortNumber"),
)
if mibBuilder.loadTexts:
    hpeNLPServerPortEntry.setStatus("current")


class _HpeNLPServerPortNumber_Type(Unsigned32):
    """Custom type hpeNLPServerPortNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_HpeNLPServerPortNumber_Type.__name__ = "Unsigned32"
_HpeNLPServerPortNumber_Object = MibTableColumn
hpeNLPServerPortNumber = _HpeNLPServerPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 8, 1, 4060, 5, 1, 1),
    _HpeNLPServerPortNumber_Type()
)
hpeNLPServerPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpeNLPServerPortNumber.setStatus("current")


class _HpeNLPServerPortResetLoopDetection_Type(TruthValue):
    """Custom type hpeNLPServerPortResetLoopDetection based on TruthValue"""
    defaultValue = 2


_HpeNLPServerPortResetLoopDetection_Type.__name__ = "TruthValue"
_HpeNLPServerPortResetLoopDetection_Object = MibTableColumn
hpeNLPServerPortResetLoopDetection = _HpeNLPServerPortResetLoopDetection_Object(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 8, 1, 4060, 5, 1, 2),
    _HpeNLPServerPortResetLoopDetection_Type()
)
hpeNLPServerPortResetLoopDetection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpeNLPServerPortResetLoopDetection.setStatus("current")


class _HpeNLPServerPortEnableTrap_Type(Integer32):
    """Custom type hpeNLPServerPortEnableTrap based on Integer32"""
    defaultValue = 1

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


_HpeNLPServerPortEnableTrap_Type.__name__ = "Integer32"
_HpeNLPServerPortEnableTrap_Object = MibTableColumn
hpeNLPServerPortEnableTrap = _HpeNLPServerPortEnableTrap_Object(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 8, 1, 4060, 5, 1, 3),
    _HpeNLPServerPortEnableTrap_Type()
)
hpeNLPServerPortEnableTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpeNLPServerPortEnableTrap.setStatus("current")
_HpeNLPServerPortStats_Object = MibTable
hpeNLPServerPortStats = _HpeNLPServerPortStats_Object(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 8, 1, 4060, 6)
)
if mibBuilder.loadTexts:
    hpeNLPServerPortStats.setStatus("current")
_HpeNLPServerPortStatsEntry_Object = MibTableRow
hpeNLPServerPortStatsEntry = _HpeNLPServerPortStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 8, 1, 4060, 6, 1)
)
hpeNLPServerPortStatsEntry.setIndexNames(
    (0, "HPE-NLP-MIB", "hpeNLPStatsPortNumber"),
)
if mibBuilder.loadTexts:
    hpeNLPServerPortStatsEntry.setStatus("current")


class _HpeNLPStatsPortNumber_Type(Unsigned32):
    """Custom type hpeNLPStatsPortNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_HpeNLPStatsPortNumber_Type.__name__ = "Unsigned32"
_HpeNLPStatsPortNumber_Object = MibTableColumn
hpeNLPStatsPortNumber = _HpeNLPStatsPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 8, 1, 4060, 6, 1, 1),
    _HpeNLPStatsPortNumber_Type()
)
hpeNLPStatsPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpeNLPStatsPortNumber.setStatus("current")


class _HpeNLPLoopDetectedStatus_Type(Integer32):
    """Custom type hpeNLPLoopDetectedStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_HpeNLPLoopDetectedStatus_Type.__name__ = "Integer32"
_HpeNLPLoopDetectedStatus_Object = MibTableColumn
hpeNLPLoopDetectedStatus = _HpeNLPLoopDetectedStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 8, 1, 4060, 6, 1, 2),
    _HpeNLPLoopDetectedStatus_Type()
)
hpeNLPLoopDetectedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpeNLPLoopDetectedStatus.setStatus("current")
_HpeNLPLoopDetectedCount_Type = Integer32
_HpeNLPLoopDetectedCount_Object = MibTableColumn
hpeNLPLoopDetectedCount = _HpeNLPLoopDetectedCount_Object(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 8, 1, 4060, 6, 1, 3),
    _HpeNLPLoopDetectedCount_Type()
)
hpeNLPLoopDetectedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpeNLPLoopDetectedCount.setStatus("current")
_HpeNLPLastLoopDetectTimeStamp_Type = TimeTicks
_HpeNLPLastLoopDetectTimeStamp_Object = MibTableColumn
hpeNLPLastLoopDetectTimeStamp = _HpeNLPLastLoopDetectTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 8, 1, 4060, 6, 1, 4),
    _HpeNLPLastLoopDetectTimeStamp_Type()
)
hpeNLPLastLoopDetectTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpeNLPLastLoopDetectTimeStamp.setStatus("current")
_Traps_ObjectIdentity = ObjectIdentity
traps = _Traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 8, 1, 4060, 7)
)
_TrapPrefix_ObjectIdentity = ObjectIdentity
trapPrefix = _TrapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 8, 1, 4060, 7, 0)
)

# Managed Objects groups


# Notification objects

hpeNLPLoopDetect = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 8, 1, 4060, 7, 0, 1)
)
hpeNLPLoopDetect.setObjects(
      *(("HPE-NLP-MIB", "hpeNLPServerPortNumber"),
        ("HPE-NLP-MIB", "hpeNLPLoopDetectedStatus"))
)
if mibBuilder.loadTexts:
    hpeNLPLoopDetect.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPE-NLP-MIB",
    **{"hpeSynergyVCMIBObjects": hpeSynergyVCMIBObjects,
       "hpeNLPMIB": hpeNLPMIB,
       "hpeNLPModuleConfig": hpeNLPModuleConfig,
       "hpeNLPResetLoopDetection": hpeNLPResetLoopDetection,
       "hpeNLPTransmitInterval": hpeNLPTransmitInterval,
       "hpeNLPEnableTrap": hpeNLPEnableTrap,
       "hpeNLPServerPortTable": hpeNLPServerPortTable,
       "hpeNLPServerPortEntry": hpeNLPServerPortEntry,
       "hpeNLPServerPortNumber": hpeNLPServerPortNumber,
       "hpeNLPServerPortResetLoopDetection": hpeNLPServerPortResetLoopDetection,
       "hpeNLPServerPortEnableTrap": hpeNLPServerPortEnableTrap,
       "hpeNLPServerPortStats": hpeNLPServerPortStats,
       "hpeNLPServerPortStatsEntry": hpeNLPServerPortStatsEntry,
       "hpeNLPStatsPortNumber": hpeNLPStatsPortNumber,
       "hpeNLPLoopDetectedStatus": hpeNLPLoopDetectedStatus,
       "hpeNLPLoopDetectedCount": hpeNLPLoopDetectedCount,
       "hpeNLPLastLoopDetectTimeStamp": hpeNLPLastLoopDetectTimeStamp,
       "traps": traps,
       "trapPrefix": trapPrefix,
       "hpeNLPLoopDetect": hpeNLPLoopDetect}
)
