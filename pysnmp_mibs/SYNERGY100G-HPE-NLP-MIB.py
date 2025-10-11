# SNMP MIB module (SYNERGY100G-HPE-NLP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/hp/SYNERGY100G-HPE-NLP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:43:34 2025
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

(hpVCSE_100Gb_F32_Module,) = mibBuilder.importSymbols(
    "HPSVRMGMT-OID",
    "hpVCSE-100Gb-F32-Module")

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

syn100GhpeNLPMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 9, 1, 4060)
)
if mibBuilder.loadTexts:
    syn100GhpeNLPMIB.setRevisions(
        ("2019-03-05 00:00",
         "2015-07-07 18:31")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Syn100GhpeSynergyVCMIBObjects_ObjectIdentity = ObjectIdentity
syn100GhpeSynergyVCMIBObjects = _Syn100GhpeSynergyVCMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 9, 1)
)


class _Syn100GhpeNLPModuleConfig_Type(Integer32):
    """Custom type syn100GhpeNLPModuleConfig based on Integer32"""
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


_Syn100GhpeNLPModuleConfig_Type.__name__ = "Integer32"
_Syn100GhpeNLPModuleConfig_Object = MibScalar
syn100GhpeNLPModuleConfig = _Syn100GhpeNLPModuleConfig_Object(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 9, 1, 4060, 1),
    _Syn100GhpeNLPModuleConfig_Type()
)
syn100GhpeNLPModuleConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syn100GhpeNLPModuleConfig.setStatus("current")


class _Syn100GhpeNLPResetLoopDetection_Type(TruthValue):
    """Custom type syn100GhpeNLPResetLoopDetection based on TruthValue"""
    defaultValue = 2


_Syn100GhpeNLPResetLoopDetection_Type.__name__ = "TruthValue"
_Syn100GhpeNLPResetLoopDetection_Object = MibScalar
syn100GhpeNLPResetLoopDetection = _Syn100GhpeNLPResetLoopDetection_Object(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 9, 1, 4060, 2),
    _Syn100GhpeNLPResetLoopDetection_Type()
)
syn100GhpeNLPResetLoopDetection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syn100GhpeNLPResetLoopDetection.setStatus("current")


class _Syn100GhpeNLPTransmitInterval_Type(Integer32):
    """Custom type syn100GhpeNLPTransmitInterval based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 10),
    )


_Syn100GhpeNLPTransmitInterval_Type.__name__ = "Integer32"
_Syn100GhpeNLPTransmitInterval_Object = MibScalar
syn100GhpeNLPTransmitInterval = _Syn100GhpeNLPTransmitInterval_Object(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 9, 1, 4060, 3),
    _Syn100GhpeNLPTransmitInterval_Type()
)
syn100GhpeNLPTransmitInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syn100GhpeNLPTransmitInterval.setStatus("current")


class _Syn100GhpeNLPEnableTrap_Type(Integer32):
    """Custom type syn100GhpeNLPEnableTrap based on Integer32"""
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


_Syn100GhpeNLPEnableTrap_Type.__name__ = "Integer32"
_Syn100GhpeNLPEnableTrap_Object = MibScalar
syn100GhpeNLPEnableTrap = _Syn100GhpeNLPEnableTrap_Object(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 9, 1, 4060, 4),
    _Syn100GhpeNLPEnableTrap_Type()
)
syn100GhpeNLPEnableTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syn100GhpeNLPEnableTrap.setStatus("current")
_Syn100GhpeNLPServerPortTable_Object = MibTable
syn100GhpeNLPServerPortTable = _Syn100GhpeNLPServerPortTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 9, 1, 4060, 5)
)
if mibBuilder.loadTexts:
    syn100GhpeNLPServerPortTable.setStatus("current")
_Syn100GhpeNLPServerPortEntry_Object = MibTableRow
syn100GhpeNLPServerPortEntry = _Syn100GhpeNLPServerPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 9, 1, 4060, 5, 1)
)
syn100GhpeNLPServerPortEntry.setIndexNames(
    (0, "SYNERGY100G-HPE-NLP-MIB", "syn100GhpeNLPServerPortNumber"),
)
if mibBuilder.loadTexts:
    syn100GhpeNLPServerPortEntry.setStatus("current")


class _Syn100GhpeNLPServerPortNumber_Type(Unsigned32):
    """Custom type syn100GhpeNLPServerPortNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_Syn100GhpeNLPServerPortNumber_Type.__name__ = "Unsigned32"
_Syn100GhpeNLPServerPortNumber_Object = MibTableColumn
syn100GhpeNLPServerPortNumber = _Syn100GhpeNLPServerPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 9, 1, 4060, 5, 1, 1),
    _Syn100GhpeNLPServerPortNumber_Type()
)
syn100GhpeNLPServerPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syn100GhpeNLPServerPortNumber.setStatus("current")


class _Syn100GhpeNLPServerPortResetLoopDetection_Type(TruthValue):
    """Custom type syn100GhpeNLPServerPortResetLoopDetection based on TruthValue"""
    defaultValue = 2


_Syn100GhpeNLPServerPortResetLoopDetection_Type.__name__ = "TruthValue"
_Syn100GhpeNLPServerPortResetLoopDetection_Object = MibTableColumn
syn100GhpeNLPServerPortResetLoopDetection = _Syn100GhpeNLPServerPortResetLoopDetection_Object(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 9, 1, 4060, 5, 1, 2),
    _Syn100GhpeNLPServerPortResetLoopDetection_Type()
)
syn100GhpeNLPServerPortResetLoopDetection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syn100GhpeNLPServerPortResetLoopDetection.setStatus("current")


class _Syn100GhpeNLPServerPortEnableTrap_Type(Integer32):
    """Custom type syn100GhpeNLPServerPortEnableTrap based on Integer32"""
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


_Syn100GhpeNLPServerPortEnableTrap_Type.__name__ = "Integer32"
_Syn100GhpeNLPServerPortEnableTrap_Object = MibTableColumn
syn100GhpeNLPServerPortEnableTrap = _Syn100GhpeNLPServerPortEnableTrap_Object(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 9, 1, 4060, 5, 1, 3),
    _Syn100GhpeNLPServerPortEnableTrap_Type()
)
syn100GhpeNLPServerPortEnableTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syn100GhpeNLPServerPortEnableTrap.setStatus("current")
_Syn100GhpeNLPServerPortStatsTable_Object = MibTable
syn100GhpeNLPServerPortStatsTable = _Syn100GhpeNLPServerPortStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 9, 1, 4060, 6)
)
if mibBuilder.loadTexts:
    syn100GhpeNLPServerPortStatsTable.setStatus("current")
_Syn100GhpeNLPServerPortStatsEntry_Object = MibTableRow
syn100GhpeNLPServerPortStatsEntry = _Syn100GhpeNLPServerPortStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 9, 1, 4060, 6, 1)
)
syn100GhpeNLPServerPortStatsEntry.setIndexNames(
    (0, "SYNERGY100G-HPE-NLP-MIB", "syn100GhpeNLPStatsPortNumber"),
)
if mibBuilder.loadTexts:
    syn100GhpeNLPServerPortStatsEntry.setStatus("current")


class _Syn100GhpeNLPStatsPortNumber_Type(Unsigned32):
    """Custom type syn100GhpeNLPStatsPortNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_Syn100GhpeNLPStatsPortNumber_Type.__name__ = "Unsigned32"
_Syn100GhpeNLPStatsPortNumber_Object = MibTableColumn
syn100GhpeNLPStatsPortNumber = _Syn100GhpeNLPStatsPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 9, 1, 4060, 6, 1, 1),
    _Syn100GhpeNLPStatsPortNumber_Type()
)
syn100GhpeNLPStatsPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syn100GhpeNLPStatsPortNumber.setStatus("current")


class _Syn100GhpeNLPLoopDetectedStatus_Type(Integer32):
    """Custom type syn100GhpeNLPLoopDetectedStatus based on Integer32"""
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


_Syn100GhpeNLPLoopDetectedStatus_Type.__name__ = "Integer32"
_Syn100GhpeNLPLoopDetectedStatus_Object = MibTableColumn
syn100GhpeNLPLoopDetectedStatus = _Syn100GhpeNLPLoopDetectedStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 9, 1, 4060, 6, 1, 2),
    _Syn100GhpeNLPLoopDetectedStatus_Type()
)
syn100GhpeNLPLoopDetectedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syn100GhpeNLPLoopDetectedStatus.setStatus("current")
_Syn100GhpeNLPLoopDetectedCount_Type = Integer32
_Syn100GhpeNLPLoopDetectedCount_Object = MibTableColumn
syn100GhpeNLPLoopDetectedCount = _Syn100GhpeNLPLoopDetectedCount_Object(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 9, 1, 4060, 6, 1, 3),
    _Syn100GhpeNLPLoopDetectedCount_Type()
)
syn100GhpeNLPLoopDetectedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syn100GhpeNLPLoopDetectedCount.setStatus("current")
_Syn100GhpeNLPLastLoopDetectTimeStamp_Type = TimeTicks
_Syn100GhpeNLPLastLoopDetectTimeStamp_Object = MibTableColumn
syn100GhpeNLPLastLoopDetectTimeStamp = _Syn100GhpeNLPLastLoopDetectTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 9, 1, 4060, 6, 1, 4),
    _Syn100GhpeNLPLastLoopDetectTimeStamp_Type()
)
syn100GhpeNLPLastLoopDetectTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syn100GhpeNLPLastLoopDetectTimeStamp.setStatus("current")
_Syn100Gtraps_ObjectIdentity = ObjectIdentity
syn100Gtraps = _Syn100Gtraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 9, 1, 4060, 7)
)
_Syn100GtrapPrefix_ObjectIdentity = ObjectIdentity
syn100GtrapPrefix = _Syn100GtrapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 9, 1, 4060, 7, 0)
)

# Managed Objects groups


# Notification objects

syn100GhpeNLPLoopDetect = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 9, 1, 4060, 7, 0, 1)
)
syn100GhpeNLPLoopDetect.setObjects(
      *(("SYNERGY100G-HPE-NLP-MIB", "syn100GhpeNLPServerPortNumber"),
        ("SYNERGY100G-HPE-NLP-MIB", "syn100GhpeNLPLoopDetectedStatus"))
)
if mibBuilder.loadTexts:
    syn100GhpeNLPLoopDetect.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SYNERGY100G-HPE-NLP-MIB",
    **{"syn100GhpeSynergyVCMIBObjects": syn100GhpeSynergyVCMIBObjects,
       "syn100GhpeNLPMIB": syn100GhpeNLPMIB,
       "syn100GhpeNLPModuleConfig": syn100GhpeNLPModuleConfig,
       "syn100GhpeNLPResetLoopDetection": syn100GhpeNLPResetLoopDetection,
       "syn100GhpeNLPTransmitInterval": syn100GhpeNLPTransmitInterval,
       "syn100GhpeNLPEnableTrap": syn100GhpeNLPEnableTrap,
       "syn100GhpeNLPServerPortTable": syn100GhpeNLPServerPortTable,
       "syn100GhpeNLPServerPortEntry": syn100GhpeNLPServerPortEntry,
       "syn100GhpeNLPServerPortNumber": syn100GhpeNLPServerPortNumber,
       "syn100GhpeNLPServerPortResetLoopDetection": syn100GhpeNLPServerPortResetLoopDetection,
       "syn100GhpeNLPServerPortEnableTrap": syn100GhpeNLPServerPortEnableTrap,
       "syn100GhpeNLPServerPortStatsTable": syn100GhpeNLPServerPortStatsTable,
       "syn100GhpeNLPServerPortStatsEntry": syn100GhpeNLPServerPortStatsEntry,
       "syn100GhpeNLPStatsPortNumber": syn100GhpeNLPStatsPortNumber,
       "syn100GhpeNLPLoopDetectedStatus": syn100GhpeNLPLoopDetectedStatus,
       "syn100GhpeNLPLoopDetectedCount": syn100GhpeNLPLoopDetectedCount,
       "syn100GhpeNLPLastLoopDetectTimeStamp": syn100GhpeNLPLastLoopDetectTimeStamp,
       "syn100Gtraps": syn100Gtraps,
       "syn100GtrapPrefix": syn100GtrapPrefix,
       "syn100GhpeNLPLoopDetect": syn100GhpeNLPLoopDetect}
)
