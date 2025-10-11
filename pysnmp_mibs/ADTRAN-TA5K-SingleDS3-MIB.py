# SNMP MIB module (ADTRAN-TA5K-SingleDS3-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/adtran/ADTRAN-TA5K-SingleDS3-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:30:43 2025
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

(adGenPortInfoIndex,
 adGenPortTrapIdentifier) = mibBuilder.importSymbols(
    "ADTRAN-GENPORT-MIB",
    "adGenPortInfoIndex",
    "adGenPortTrapIdentifier")

(adGenSlotAlarmStatus,
 adGenSlotInfoIndex) = mibBuilder.importSymbols(
    "ADTRAN-GENSLOT-MIB",
    "adGenSlotAlarmStatus",
    "adGenSlotInfoIndex")

(adTrapInformSeqNum,) = mibBuilder.importSymbols(
    "ADTRAN-GENTRAPINFORM-MIB",
    "adTrapInformSeqNum")

(adIdentity,
 adMgmt,
 adProducts) = mibBuilder.importSymbols(
    "ADTRAN-MIB",
    "adIdentity",
    "adMgmt",
    "adProducts")

(adTAeSCUTrapAlarmLevel,) = mibBuilder.importSymbols(
    "ADTRAN-TAeSCUEXT1-MIB",
    "adTAeSCUTrapAlarmLevel")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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
 PhysAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

adTa5kSingleDs3ModuleIdentity = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 664, 6, 896)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AdTa5kSingleDs3TrapsPrefix_ObjectIdentity = ObjectIdentity
adTa5kSingleDs3TrapsPrefix = _AdTa5kSingleDs3TrapsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 1, 896)
)
_AdTa5kSingleDS3Traps_ObjectIdentity = ObjectIdentity
adTa5kSingleDS3Traps = _AdTa5kSingleDS3Traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 1, 896, 0)
)
_AdTa5kSingleDs3_ObjectIdentity = ObjectIdentity
adTa5kSingleDs3 = _AdTa5kSingleDs3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 2, 896)
)
_AdTa5kSingleDS3PortProv_ObjectIdentity = ObjectIdentity
adTa5kSingleDS3PortProv = _AdTa5kSingleDS3PortProv_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 2, 896, 1)
)
_AdTa5kSingleDS3PortProvTable_Object = MibTable
adTa5kSingleDS3PortProvTable = _AdTa5kSingleDS3PortProvTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 896, 1, 1)
)
if mibBuilder.loadTexts:
    adTa5kSingleDS3PortProvTable.setStatus("current")
_AdTa5kSingleDS3PortProvEntry_Object = MibTableRow
adTa5kSingleDS3PortProvEntry = _AdTa5kSingleDS3PortProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 896, 1, 1, 1)
)
adTa5kSingleDS3PortProvEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adTa5kSingleDS3PortProvEntry.setStatus("current")


class _AdTa5kSingleDS3PortLineType_Type(Integer32):
    """Custom type adTa5kSingleDS3PortLineType based on Integer32"""
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
              8,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("dsx3other", 1),
          ("dsx3M23", 2),
          ("dsx3SYNTRAN", 3),
          ("dsx3CbitParity", 4),
          ("dsx3ClearChannel", 5),
          ("e3other", 6),
          ("e3Framed", 7),
          ("e3Plcp", 8),
          ("dsx3CbitParityPlcp", 9),
          ("dsx3M23Plcp", 10))
    )


_AdTa5kSingleDS3PortLineType_Type.__name__ = "Integer32"
_AdTa5kSingleDS3PortLineType_Object = MibTableColumn
adTa5kSingleDS3PortLineType = _AdTa5kSingleDS3PortLineType_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 896, 1, 1, 1, 1),
    _AdTa5kSingleDS3PortLineType_Type()
)
adTa5kSingleDS3PortLineType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTa5kSingleDS3PortLineType.setStatus("current")


class _AdTa5kSingleDS3PortScrambler_Type(Integer32):
    """Custom type adTa5kSingleDS3PortScrambler based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2))
    )


_AdTa5kSingleDS3PortScrambler_Type.__name__ = "Integer32"
_AdTa5kSingleDS3PortScrambler_Object = MibTableColumn
adTa5kSingleDS3PortScrambler = _AdTa5kSingleDS3PortScrambler_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 896, 1, 1, 1, 2),
    _AdTa5kSingleDS3PortScrambler_Type()
)
adTa5kSingleDS3PortScrambler.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTa5kSingleDS3PortScrambler.setStatus("current")
_AdTa5kSingleDS3AlmProv_ObjectIdentity = ObjectIdentity
adTa5kSingleDS3AlmProv = _AdTa5kSingleDS3AlmProv_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 2, 896, 3)
)
_AdTa5kSingleDS3EnhancedAlmSlotProvTable_Object = MibTable
adTa5kSingleDS3EnhancedAlmSlotProvTable = _AdTa5kSingleDS3EnhancedAlmSlotProvTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 896, 3, 1)
)
if mibBuilder.loadTexts:
    adTa5kSingleDS3EnhancedAlmSlotProvTable.setStatus("current")
_AdTa5kSingleDS3EnhancedAlmSlotProvEntry_Object = MibTableRow
adTa5kSingleDS3EnhancedAlmSlotProvEntry = _AdTa5kSingleDS3EnhancedAlmSlotProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 896, 3, 1, 1)
)
adTa5kSingleDS3EnhancedAlmSlotProvEntry.setIndexNames(
    (0, "ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
)
if mibBuilder.loadTexts:
    adTa5kSingleDS3EnhancedAlmSlotProvEntry.setStatus("current")


class _AdSingleDs3EnhancedAlmSlotLOSSeverity_Type(Integer32):
    """Custom type adSingleDs3EnhancedAlmSlotLOSSeverity based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("info", 2),
          ("alert", 3),
          ("minor", 4),
          ("major", 5),
          ("critical", 6))
    )


_AdSingleDs3EnhancedAlmSlotLOSSeverity_Type.__name__ = "Integer32"
_AdSingleDs3EnhancedAlmSlotLOSSeverity_Object = MibTableColumn
adSingleDs3EnhancedAlmSlotLOSSeverity = _AdSingleDs3EnhancedAlmSlotLOSSeverity_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 896, 3, 1, 1, 1),
    _AdSingleDs3EnhancedAlmSlotLOSSeverity_Type()
)
adSingleDs3EnhancedAlmSlotLOSSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adSingleDs3EnhancedAlmSlotLOSSeverity.setStatus("current")


class _AdSingleDs3EnhancedAlmSlotLOSSuppression_Type(Integer32):
    """Custom type adSingleDs3EnhancedAlmSlotLOSSuppression based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_AdSingleDs3EnhancedAlmSlotLOSSuppression_Type.__name__ = "Integer32"
_AdSingleDs3EnhancedAlmSlotLOSSuppression_Object = MibTableColumn
adSingleDs3EnhancedAlmSlotLOSSuppression = _AdSingleDs3EnhancedAlmSlotLOSSuppression_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 896, 3, 1, 1, 2),
    _AdSingleDs3EnhancedAlmSlotLOSSuppression_Type()
)
adSingleDs3EnhancedAlmSlotLOSSuppression.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adSingleDs3EnhancedAlmSlotLOSSuppression.setStatus("current")


class _AdSingleDs3EnhancedAlmSlotLOFSeverity_Type(Integer32):
    """Custom type adSingleDs3EnhancedAlmSlotLOFSeverity based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("info", 2),
          ("alert", 3),
          ("minor", 4),
          ("major", 5),
          ("critical", 6))
    )


_AdSingleDs3EnhancedAlmSlotLOFSeverity_Type.__name__ = "Integer32"
_AdSingleDs3EnhancedAlmSlotLOFSeverity_Object = MibTableColumn
adSingleDs3EnhancedAlmSlotLOFSeverity = _AdSingleDs3EnhancedAlmSlotLOFSeverity_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 896, 3, 1, 1, 3),
    _AdSingleDs3EnhancedAlmSlotLOFSeverity_Type()
)
adSingleDs3EnhancedAlmSlotLOFSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adSingleDs3EnhancedAlmSlotLOFSeverity.setStatus("current")


class _AdSingleDs3EnhancedAlmSlotLOFSuppression_Type(Integer32):
    """Custom type adSingleDs3EnhancedAlmSlotLOFSuppression based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_AdSingleDs3EnhancedAlmSlotLOFSuppression_Type.__name__ = "Integer32"
_AdSingleDs3EnhancedAlmSlotLOFSuppression_Object = MibTableColumn
adSingleDs3EnhancedAlmSlotLOFSuppression = _AdSingleDs3EnhancedAlmSlotLOFSuppression_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 896, 3, 1, 1, 4),
    _AdSingleDs3EnhancedAlmSlotLOFSuppression_Type()
)
adSingleDs3EnhancedAlmSlotLOFSuppression.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adSingleDs3EnhancedAlmSlotLOFSuppression.setStatus("current")


class _AdSingleDs3EnhancedAlmSlotAISSeverity_Type(Integer32):
    """Custom type adSingleDs3EnhancedAlmSlotAISSeverity based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("info", 2),
          ("alert", 3),
          ("minor", 4),
          ("major", 5),
          ("critical", 6))
    )


_AdSingleDs3EnhancedAlmSlotAISSeverity_Type.__name__ = "Integer32"
_AdSingleDs3EnhancedAlmSlotAISSeverity_Object = MibTableColumn
adSingleDs3EnhancedAlmSlotAISSeverity = _AdSingleDs3EnhancedAlmSlotAISSeverity_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 896, 3, 1, 1, 5),
    _AdSingleDs3EnhancedAlmSlotAISSeverity_Type()
)
adSingleDs3EnhancedAlmSlotAISSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adSingleDs3EnhancedAlmSlotAISSeverity.setStatus("current")


class _AdSingleDs3EnhancedAlmSlotAISSuppression_Type(Integer32):
    """Custom type adSingleDs3EnhancedAlmSlotAISSuppression based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_AdSingleDs3EnhancedAlmSlotAISSuppression_Type.__name__ = "Integer32"
_AdSingleDs3EnhancedAlmSlotAISSuppression_Object = MibTableColumn
adSingleDs3EnhancedAlmSlotAISSuppression = _AdSingleDs3EnhancedAlmSlotAISSuppression_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 896, 3, 1, 1, 6),
    _AdSingleDs3EnhancedAlmSlotAISSuppression_Type()
)
adSingleDs3EnhancedAlmSlotAISSuppression.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adSingleDs3EnhancedAlmSlotAISSuppression.setStatus("current")


class _AdSingleDs3EnhancedAlmSlotRAISeverity_Type(Integer32):
    """Custom type adSingleDs3EnhancedAlmSlotRAISeverity based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("info", 2),
          ("alert", 3),
          ("minor", 4),
          ("major", 5),
          ("critical", 6))
    )


_AdSingleDs3EnhancedAlmSlotRAISeverity_Type.__name__ = "Integer32"
_AdSingleDs3EnhancedAlmSlotRAISeverity_Object = MibTableColumn
adSingleDs3EnhancedAlmSlotRAISeverity = _AdSingleDs3EnhancedAlmSlotRAISeverity_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 896, 3, 1, 1, 7),
    _AdSingleDs3EnhancedAlmSlotRAISeverity_Type()
)
adSingleDs3EnhancedAlmSlotRAISeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adSingleDs3EnhancedAlmSlotRAISeverity.setStatus("current")


class _AdSingleDs3EnhancedAlmSlotRAISuppression_Type(Integer32):
    """Custom type adSingleDs3EnhancedAlmSlotRAISuppression based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_AdSingleDs3EnhancedAlmSlotRAISuppression_Type.__name__ = "Integer32"
_AdSingleDs3EnhancedAlmSlotRAISuppression_Object = MibTableColumn
adSingleDs3EnhancedAlmSlotRAISuppression = _AdSingleDs3EnhancedAlmSlotRAISuppression_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 896, 3, 1, 1, 8),
    _AdSingleDs3EnhancedAlmSlotRAISuppression_Type()
)
adSingleDs3EnhancedAlmSlotRAISuppression.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adSingleDs3EnhancedAlmSlotRAISuppression.setStatus("current")


class _AdSingleDS3EnhancedAlmSlotLOSEnable_Type(TruthValue):
    """Custom type adSingleDS3EnhancedAlmSlotLOSEnable based on TruthValue"""
    defaultValue = 1


_AdSingleDS3EnhancedAlmSlotLOSEnable_Type.__name__ = "TruthValue"
_AdSingleDS3EnhancedAlmSlotLOSEnable_Object = MibTableColumn
adSingleDS3EnhancedAlmSlotLOSEnable = _AdSingleDS3EnhancedAlmSlotLOSEnable_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 896, 3, 1, 1, 9),
    _AdSingleDS3EnhancedAlmSlotLOSEnable_Type()
)
adSingleDS3EnhancedAlmSlotLOSEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adSingleDS3EnhancedAlmSlotLOSEnable.setStatus("current")


class _AdSingleDS3EnhancedAlmSlotLOFEnable_Type(TruthValue):
    """Custom type adSingleDS3EnhancedAlmSlotLOFEnable based on TruthValue"""
    defaultValue = 1


_AdSingleDS3EnhancedAlmSlotLOFEnable_Type.__name__ = "TruthValue"
_AdSingleDS3EnhancedAlmSlotLOFEnable_Object = MibTableColumn
adSingleDS3EnhancedAlmSlotLOFEnable = _AdSingleDS3EnhancedAlmSlotLOFEnable_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 896, 3, 1, 1, 10),
    _AdSingleDS3EnhancedAlmSlotLOFEnable_Type()
)
adSingleDS3EnhancedAlmSlotLOFEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adSingleDS3EnhancedAlmSlotLOFEnable.setStatus("current")


class _AdSingleDS3EnhancedAlmSlotAISEnable_Type(TruthValue):
    """Custom type adSingleDS3EnhancedAlmSlotAISEnable based on TruthValue"""
    defaultValue = 1


_AdSingleDS3EnhancedAlmSlotAISEnable_Type.__name__ = "TruthValue"
_AdSingleDS3EnhancedAlmSlotAISEnable_Object = MibTableColumn
adSingleDS3EnhancedAlmSlotAISEnable = _AdSingleDS3EnhancedAlmSlotAISEnable_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 896, 3, 1, 1, 11),
    _AdSingleDS3EnhancedAlmSlotAISEnable_Type()
)
adSingleDS3EnhancedAlmSlotAISEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adSingleDS3EnhancedAlmSlotAISEnable.setStatus("current")


class _AdSingleDS3EnhancedAlmSlotRAIEnable_Type(TruthValue):
    """Custom type adSingleDS3EnhancedAlmSlotRAIEnable based on TruthValue"""
    defaultValue = 1


_AdSingleDS3EnhancedAlmSlotRAIEnable_Type.__name__ = "TruthValue"
_AdSingleDS3EnhancedAlmSlotRAIEnable_Object = MibTableColumn
adSingleDS3EnhancedAlmSlotRAIEnable = _AdSingleDS3EnhancedAlmSlotRAIEnable_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 896, 3, 1, 1, 12),
    _AdSingleDS3EnhancedAlmSlotRAIEnable_Type()
)
adSingleDS3EnhancedAlmSlotRAIEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adSingleDS3EnhancedAlmSlotRAIEnable.setStatus("current")
_AdTa5kSingleDS3MibConformance_ObjectIdentity = ObjectIdentity
adTa5kSingleDS3MibConformance = _AdTa5kSingleDS3MibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 2, 896, 6)
)
_AdTa5kSingleDS3MibGroups_ObjectIdentity = ObjectIdentity
adTa5kSingleDS3MibGroups = _AdTa5kSingleDS3MibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 2, 896, 6, 1)
)

# Managed Objects groups

adTa5kSingleDS3PortProvGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 664, 2, 896, 6, 1, 1)
)
adTa5kSingleDS3PortProvGroup.setObjects(
      *(("ADTRAN-TA5K-SingleDS3-MIB", "adTa5kSingleDS3PortLineType"),
        ("ADTRAN-TA5K-SingleDS3-MIB", "adTa5kSingleDS3PortScrambler"))
)
if mibBuilder.loadTexts:
    adTa5kSingleDS3PortProvGroup.setStatus("current")


# Notification objects

adSingleDs3LOSTrapClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 1, 896, 0, 2)
)
adSingleDs3LOSTrapClear.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortInfoIndex"))
)
if mibBuilder.loadTexts:
    adSingleDs3LOSTrapClear.setStatus(
        "current"
    )

adSingleDs3LOSTrapActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 1, 896, 0, 3)
)
adSingleDs3LOSTrapActive.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortInfoIndex"))
)
if mibBuilder.loadTexts:
    adSingleDs3LOSTrapActive.setStatus(
        "current"
    )

adSingleDs3LOFTrapClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 1, 896, 0, 4)
)
adSingleDs3LOFTrapClear.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortInfoIndex"))
)
if mibBuilder.loadTexts:
    adSingleDs3LOFTrapClear.setStatus(
        "current"
    )

adSingleDs3LOFTrapActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 1, 896, 0, 5)
)
adSingleDs3LOFTrapActive.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortInfoIndex"))
)
if mibBuilder.loadTexts:
    adSingleDs3LOFTrapActive.setStatus(
        "current"
    )

adSingleDs3RAITrapClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 1, 896, 0, 6)
)
adSingleDs3RAITrapClear.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortInfoIndex"))
)
if mibBuilder.loadTexts:
    adSingleDs3RAITrapClear.setStatus(
        "current"
    )

adSingleDs3RAITrapActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 1, 896, 0, 7)
)
adSingleDs3RAITrapActive.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortInfoIndex"))
)
if mibBuilder.loadTexts:
    adSingleDs3RAITrapActive.setStatus(
        "current"
    )

adSingleDs3AISTrapClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 1, 896, 0, 8)
)
adSingleDs3AISTrapClear.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortInfoIndex"))
)
if mibBuilder.loadTexts:
    adSingleDs3AISTrapClear.setStatus(
        "current"
    )

adSingleDs3AISTrapActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 1, 896, 0, 9)
)
adSingleDs3AISTrapActive.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortInfoIndex"))
)
if mibBuilder.loadTexts:
    adSingleDs3AISTrapActive.setStatus(
        "current"
    )

adSingleDs3LoopTrapClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 1, 896, 0, 10)
)
adSingleDs3LoopTrapClear.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortInfoIndex"))
)
if mibBuilder.loadTexts:
    adSingleDs3LoopTrapClear.setStatus(
        "current"
    )

adSingleDs3LoopTrapActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 1, 896, 0, 11)
)
adSingleDs3LoopTrapActive.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortInfoIndex"))
)
if mibBuilder.loadTexts:
    adSingleDs3LoopTrapActive.setStatus(
        "current"
    )

adSingleDs3IdleTrapClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 1, 896, 0, 12)
)
adSingleDs3IdleTrapClear.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortInfoIndex"))
)
if mibBuilder.loadTexts:
    adSingleDs3IdleTrapClear.setStatus(
        "current"
    )

adSingleDs3IdleTrapActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 1, 896, 0, 13)
)
adSingleDs3IdleTrapActive.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortInfoIndex"))
)
if mibBuilder.loadTexts:
    adSingleDs3IdleTrapActive.setStatus(
        "current"
    )

adSingleDs3EnhancedLOSTrapClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 1, 896, 0, 14)
)
adSingleDs3EnhancedLOSTrapClear.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortInfoIndex"),
        ("ADTRAN-TAeSCUEXT1-MIB", "adTAeSCUTrapAlarmLevel"))
)
if mibBuilder.loadTexts:
    adSingleDs3EnhancedLOSTrapClear.setStatus(
        "current"
    )

adSingleDs3EnhancedLOSTrapActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 1, 896, 0, 15)
)
adSingleDs3EnhancedLOSTrapActive.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortInfoIndex"),
        ("ADTRAN-TAeSCUEXT1-MIB", "adTAeSCUTrapAlarmLevel"))
)
if mibBuilder.loadTexts:
    adSingleDs3EnhancedLOSTrapActive.setStatus(
        "current"
    )

adSingleDs3EnhancedLOFTrapClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 1, 896, 0, 16)
)
adSingleDs3EnhancedLOFTrapClear.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortInfoIndex"),
        ("ADTRAN-TAeSCUEXT1-MIB", "adTAeSCUTrapAlarmLevel"))
)
if mibBuilder.loadTexts:
    adSingleDs3EnhancedLOFTrapClear.setStatus(
        "current"
    )

adSingleDs3EnhancedLOFTrapActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 1, 896, 0, 17)
)
adSingleDs3EnhancedLOFTrapActive.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortInfoIndex"),
        ("ADTRAN-TAeSCUEXT1-MIB", "adTAeSCUTrapAlarmLevel"))
)
if mibBuilder.loadTexts:
    adSingleDs3EnhancedLOFTrapActive.setStatus(
        "current"
    )

adSingleDs3EnhancedRAITrapClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 1, 896, 0, 18)
)
adSingleDs3EnhancedRAITrapClear.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortInfoIndex"),
        ("ADTRAN-TAeSCUEXT1-MIB", "adTAeSCUTrapAlarmLevel"))
)
if mibBuilder.loadTexts:
    adSingleDs3EnhancedRAITrapClear.setStatus(
        "current"
    )

adSingleDs3EnhancedRAITrapActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 1, 896, 0, 19)
)
adSingleDs3EnhancedRAITrapActive.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortInfoIndex"),
        ("ADTRAN-TAeSCUEXT1-MIB", "adTAeSCUTrapAlarmLevel"))
)
if mibBuilder.loadTexts:
    adSingleDs3EnhancedRAITrapActive.setStatus(
        "current"
    )

adSingleDs3EnhancedAISTrapClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 1, 896, 0, 20)
)
adSingleDs3EnhancedAISTrapClear.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortInfoIndex"),
        ("ADTRAN-TAeSCUEXT1-MIB", "adTAeSCUTrapAlarmLevel"))
)
if mibBuilder.loadTexts:
    adSingleDs3EnhancedAISTrapClear.setStatus(
        "current"
    )

adSingleDs3EnhancedAISTrapActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 1, 896, 0, 21)
)
adSingleDs3EnhancedAISTrapActive.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortInfoIndex"),
        ("ADTRAN-TAeSCUEXT1-MIB", "adTAeSCUTrapAlarmLevel"))
)
if mibBuilder.loadTexts:
    adSingleDs3EnhancedAISTrapActive.setStatus(
        "current"
    )


# Notifications groups

adTa5kSingleDS3TrapGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 664, 2, 896, 6, 1, 2)
)
adTa5kSingleDS3TrapGroup.setObjects(
      *(("ADTRAN-TA5K-SingleDS3-MIB", "adSingleDs3LOSTrapClear"),
        ("ADTRAN-TA5K-SingleDS3-MIB", "adSingleDs3LOSTrapActive"),
        ("ADTRAN-TA5K-SingleDS3-MIB", "adSingleDs3LOFTrapClear"),
        ("ADTRAN-TA5K-SingleDS3-MIB", "adSingleDs3LOFTrapActive"),
        ("ADTRAN-TA5K-SingleDS3-MIB", "adSingleDs3RAITrapClear"),
        ("ADTRAN-TA5K-SingleDS3-MIB", "adSingleDs3RAITrapActive"),
        ("ADTRAN-TA5K-SingleDS3-MIB", "adSingleDs3AISTrapClear"),
        ("ADTRAN-TA5K-SingleDS3-MIB", "adSingleDs3AISTrapActive"),
        ("ADTRAN-TA5K-SingleDS3-MIB", "adSingleDs3LoopTrapClear"),
        ("ADTRAN-TA5K-SingleDS3-MIB", "adSingleDs3LoopTrapActive"),
        ("ADTRAN-TA5K-SingleDS3-MIB", "adSingleDs3IdleTrapClear"),
        ("ADTRAN-TA5K-SingleDS3-MIB", "adSingleDs3IdleTrapActive"),
        ("ADTRAN-TA5K-SingleDS3-MIB", "adSingleDs3EnhancedLOSTrapClear"),
        ("ADTRAN-TA5K-SingleDS3-MIB", "adSingleDs3EnhancedLOSTrapActive"),
        ("ADTRAN-TA5K-SingleDS3-MIB", "adSingleDs3EnhancedLOFTrapClear"),
        ("ADTRAN-TA5K-SingleDS3-MIB", "adSingleDs3EnhancedLOFTrapActive"),
        ("ADTRAN-TA5K-SingleDS3-MIB", "adSingleDs3EnhancedRAITrapClear"),
        ("ADTRAN-TA5K-SingleDS3-MIB", "adSingleDs3EnhancedRAITrapActive"),
        ("ADTRAN-TA5K-SingleDS3-MIB", "adSingleDs3EnhancedAISTrapClear"),
        ("ADTRAN-TA5K-SingleDS3-MIB", "adSingleDs3EnhancedAISTrapActive"))
)
if mibBuilder.loadTexts:
    adTa5kSingleDS3TrapGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ADTRAN-TA5K-SingleDS3-MIB",
    **{"adTa5kSingleDs3TrapsPrefix": adTa5kSingleDs3TrapsPrefix,
       "adTa5kSingleDS3Traps": adTa5kSingleDS3Traps,
       "adSingleDs3LOSTrapClear": adSingleDs3LOSTrapClear,
       "adSingleDs3LOSTrapActive": adSingleDs3LOSTrapActive,
       "adSingleDs3LOFTrapClear": adSingleDs3LOFTrapClear,
       "adSingleDs3LOFTrapActive": adSingleDs3LOFTrapActive,
       "adSingleDs3RAITrapClear": adSingleDs3RAITrapClear,
       "adSingleDs3RAITrapActive": adSingleDs3RAITrapActive,
       "adSingleDs3AISTrapClear": adSingleDs3AISTrapClear,
       "adSingleDs3AISTrapActive": adSingleDs3AISTrapActive,
       "adSingleDs3LoopTrapClear": adSingleDs3LoopTrapClear,
       "adSingleDs3LoopTrapActive": adSingleDs3LoopTrapActive,
       "adSingleDs3IdleTrapClear": adSingleDs3IdleTrapClear,
       "adSingleDs3IdleTrapActive": adSingleDs3IdleTrapActive,
       "adSingleDs3EnhancedLOSTrapClear": adSingleDs3EnhancedLOSTrapClear,
       "adSingleDs3EnhancedLOSTrapActive": adSingleDs3EnhancedLOSTrapActive,
       "adSingleDs3EnhancedLOFTrapClear": adSingleDs3EnhancedLOFTrapClear,
       "adSingleDs3EnhancedLOFTrapActive": adSingleDs3EnhancedLOFTrapActive,
       "adSingleDs3EnhancedRAITrapClear": adSingleDs3EnhancedRAITrapClear,
       "adSingleDs3EnhancedRAITrapActive": adSingleDs3EnhancedRAITrapActive,
       "adSingleDs3EnhancedAISTrapClear": adSingleDs3EnhancedAISTrapClear,
       "adSingleDs3EnhancedAISTrapActive": adSingleDs3EnhancedAISTrapActive,
       "adTa5kSingleDs3": adTa5kSingleDs3,
       "adTa5kSingleDS3PortProv": adTa5kSingleDS3PortProv,
       "adTa5kSingleDS3PortProvTable": adTa5kSingleDS3PortProvTable,
       "adTa5kSingleDS3PortProvEntry": adTa5kSingleDS3PortProvEntry,
       "adTa5kSingleDS3PortLineType": adTa5kSingleDS3PortLineType,
       "adTa5kSingleDS3PortScrambler": adTa5kSingleDS3PortScrambler,
       "adTa5kSingleDS3AlmProv": adTa5kSingleDS3AlmProv,
       "adTa5kSingleDS3EnhancedAlmSlotProvTable": adTa5kSingleDS3EnhancedAlmSlotProvTable,
       "adTa5kSingleDS3EnhancedAlmSlotProvEntry": adTa5kSingleDS3EnhancedAlmSlotProvEntry,
       "adSingleDs3EnhancedAlmSlotLOSSeverity": adSingleDs3EnhancedAlmSlotLOSSeverity,
       "adSingleDs3EnhancedAlmSlotLOSSuppression": adSingleDs3EnhancedAlmSlotLOSSuppression,
       "adSingleDs3EnhancedAlmSlotLOFSeverity": adSingleDs3EnhancedAlmSlotLOFSeverity,
       "adSingleDs3EnhancedAlmSlotLOFSuppression": adSingleDs3EnhancedAlmSlotLOFSuppression,
       "adSingleDs3EnhancedAlmSlotAISSeverity": adSingleDs3EnhancedAlmSlotAISSeverity,
       "adSingleDs3EnhancedAlmSlotAISSuppression": adSingleDs3EnhancedAlmSlotAISSuppression,
       "adSingleDs3EnhancedAlmSlotRAISeverity": adSingleDs3EnhancedAlmSlotRAISeverity,
       "adSingleDs3EnhancedAlmSlotRAISuppression": adSingleDs3EnhancedAlmSlotRAISuppression,
       "adSingleDS3EnhancedAlmSlotLOSEnable": adSingleDS3EnhancedAlmSlotLOSEnable,
       "adSingleDS3EnhancedAlmSlotLOFEnable": adSingleDS3EnhancedAlmSlotLOFEnable,
       "adSingleDS3EnhancedAlmSlotAISEnable": adSingleDS3EnhancedAlmSlotAISEnable,
       "adSingleDS3EnhancedAlmSlotRAIEnable": adSingleDS3EnhancedAlmSlotRAIEnable,
       "adTa5kSingleDS3MibConformance": adTa5kSingleDS3MibConformance,
       "adTa5kSingleDS3MibGroups": adTa5kSingleDS3MibGroups,
       "adTa5kSingleDS3PortProvGroup": adTa5kSingleDS3PortProvGroup,
       "adTa5kSingleDS3TrapGroup": adTa5kSingleDS3TrapGroup,
       "adTa5kSingleDs3ModuleIdentity": adTa5kSingleDs3ModuleIdentity}
)
