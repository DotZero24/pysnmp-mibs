# SNMP MIB module (ADTRAN-GEN-DSL-PROXY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/adtran/ADTRAN-GEN-DSL-PROXY-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:32:19 2025
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

(adGenDslProxy,
 adGenDslProxyID) = mibBuilder.importSymbols(
    "ADTRAN-SHARED-SHDSL-MIB",
    "adGenDslProxy",
    "adGenDslProxyID")

(adEShdslInvIndex,) = mibBuilder.importSymbols(
    "ADTRAN-SHDSL-MIB",
    "adEShdslInvIndex")

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

adGenDslProxyMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 59, 4, 1)
)
if mibBuilder.loadTexts:
    adGenDslProxyMIB.setRevisions(
        ("2009-06-08 00:00",)
    )


# Types definitions



class AdGenDslProxyInitiate(Integer32):
    """Custom type AdGenDslProxyInitiate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("initiate", 1)
    )





class AdGenDslProxyStatus(Integer32):
    """Custom type AdGenDslProxyStatus based on Integer32"""
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
        *(("neverActivated", 1),
          ("inProgress", 2),
          ("resultsValid", 3),
          ("error", 4))
    )





class AdGenDslProxyLastTime(TimeTicks):
    """Custom type AdGenDslProxyLastTime based on TimeTicks"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AdGenDslProxyCommands_ObjectIdentity = ObjectIdentity
adGenDslProxyCommands = _AdGenDslProxyCommands_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 4, 1)
)
_AdGenDslProxyCommandTable_Object = MibTable
adGenDslProxyCommandTable = _AdGenDslProxyCommandTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 4, 1, 1)
)
if mibBuilder.loadTexts:
    adGenDslProxyCommandTable.setStatus("current")
_AdGenDslProxyCommandEntry_Object = MibTableRow
adGenDslProxyCommandEntry = _AdGenDslProxyCommandEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 4, 1, 1, 1)
)
adGenDslProxyCommandEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adGenDslProxyCommandEntry.setStatus("current")
_AdGenDslProxySystemTypeInitiate_Type = AdGenDslProxyInitiate
_AdGenDslProxySystemTypeInitiate_Object = MibTableColumn
adGenDslProxySystemTypeInitiate = _AdGenDslProxySystemTypeInitiate_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 4, 1, 1, 1, 1),
    _AdGenDslProxySystemTypeInitiate_Type()
)
adGenDslProxySystemTypeInitiate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenDslProxySystemTypeInitiate.setStatus("current")
_AdGenDslProxySystemTypeStatus_Type = AdGenDslProxyStatus
_AdGenDslProxySystemTypeStatus_Object = MibTableColumn
adGenDslProxySystemTypeStatus = _AdGenDslProxySystemTypeStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 4, 1, 1, 1, 2),
    _AdGenDslProxySystemTypeStatus_Type()
)
adGenDslProxySystemTypeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenDslProxySystemTypeStatus.setStatus("current")
_AdGenDslProxySystemTypeLastTime_Type = AdGenDslProxyLastTime
_AdGenDslProxySystemTypeLastTime_Object = MibTableColumn
adGenDslProxySystemTypeLastTime = _AdGenDslProxySystemTypeLastTime_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 4, 1, 1, 1, 3),
    _AdGenDslProxySystemTypeLastTime_Type()
)
adGenDslProxySystemTypeLastTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenDslProxySystemTypeLastTime.setStatus("current")
_AdGenDslProxyLoopbackStatusInitiate_Type = AdGenDslProxyInitiate
_AdGenDslProxyLoopbackStatusInitiate_Object = MibTableColumn
adGenDslProxyLoopbackStatusInitiate = _AdGenDslProxyLoopbackStatusInitiate_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 4, 1, 1, 1, 4),
    _AdGenDslProxyLoopbackStatusInitiate_Type()
)
adGenDslProxyLoopbackStatusInitiate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenDslProxyLoopbackStatusInitiate.setStatus("current")
_AdGenDslProxyLoopbackStatusStatus_Type = AdGenDslProxyStatus
_AdGenDslProxyLoopbackStatusStatus_Object = MibTableColumn
adGenDslProxyLoopbackStatusStatus = _AdGenDslProxyLoopbackStatusStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 4, 1, 1, 1, 5),
    _AdGenDslProxyLoopbackStatusStatus_Type()
)
adGenDslProxyLoopbackStatusStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenDslProxyLoopbackStatusStatus.setStatus("current")
_AdGenDslProxyLoopbackStatusLastTime_Type = AdGenDslProxyLastTime
_AdGenDslProxyLoopbackStatusLastTime_Object = MibTableColumn
adGenDslProxyLoopbackStatusLastTime = _AdGenDslProxyLoopbackStatusLastTime_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 4, 1, 1, 1, 6),
    _AdGenDslProxyLoopbackStatusLastTime_Type()
)
adGenDslProxyLoopbackStatusLastTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenDslProxyLoopbackStatusLastTime.setStatus("current")
_AdGenDslProxySpliceDetectInitiate_Type = AdGenDslProxyInitiate
_AdGenDslProxySpliceDetectInitiate_Object = MibTableColumn
adGenDslProxySpliceDetectInitiate = _AdGenDslProxySpliceDetectInitiate_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 4, 1, 1, 1, 7),
    _AdGenDslProxySpliceDetectInitiate_Type()
)
adGenDslProxySpliceDetectInitiate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenDslProxySpliceDetectInitiate.setStatus("current")
_AdGenDslProxySpliceDetectStatus_Type = AdGenDslProxyStatus
_AdGenDslProxySpliceDetectStatus_Object = MibTableColumn
adGenDslProxySpliceDetectStatus = _AdGenDslProxySpliceDetectStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 4, 1, 1, 1, 8),
    _AdGenDslProxySpliceDetectStatus_Type()
)
adGenDslProxySpliceDetectStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenDslProxySpliceDetectStatus.setStatus("current")
_AdGenDslProxySpliceDetectLastTime_Type = AdGenDslProxyLastTime
_AdGenDslProxySpliceDetectLastTime_Object = MibTableColumn
adGenDslProxySpliceDetectLastTime = _AdGenDslProxySpliceDetectLastTime_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 4, 1, 1, 1, 9),
    _AdGenDslProxySpliceDetectLastTime_Type()
)
adGenDslProxySpliceDetectLastTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenDslProxySpliceDetectLastTime.setStatus("current")
_AdGenDslProxyFrameGroundInitiate_Type = AdGenDslProxyInitiate
_AdGenDslProxyFrameGroundInitiate_Object = MibTableColumn
adGenDslProxyFrameGroundInitiate = _AdGenDslProxyFrameGroundInitiate_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 4, 1, 1, 1, 10),
    _AdGenDslProxyFrameGroundInitiate_Type()
)
adGenDslProxyFrameGroundInitiate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenDslProxyFrameGroundInitiate.setStatus("current")
_AdGenDslProxyFrameGroundStatus_Type = AdGenDslProxyStatus
_AdGenDslProxyFrameGroundStatus_Object = MibTableColumn
adGenDslProxyFrameGroundStatus = _AdGenDslProxyFrameGroundStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 4, 1, 1, 1, 11),
    _AdGenDslProxyFrameGroundStatus_Type()
)
adGenDslProxyFrameGroundStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenDslProxyFrameGroundStatus.setStatus("current")
_AdGenDslProxyFrameGroundLastTime_Type = AdGenDslProxyLastTime
_AdGenDslProxyFrameGroundLastTime_Object = MibTableColumn
adGenDslProxyFrameGroundLastTime = _AdGenDslProxyFrameGroundLastTime_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 4, 1, 1, 1, 12),
    _AdGenDslProxyFrameGroundLastTime_Type()
)
adGenDslProxyFrameGroundLastTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenDslProxyFrameGroundLastTime.setStatus("current")
_AdGenDslProxyResults_ObjectIdentity = ObjectIdentity
adGenDslProxyResults = _AdGenDslProxyResults_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 4, 2)
)
_AdGenDslProxySystemTable_Object = MibTable
adGenDslProxySystemTable = _AdGenDslProxySystemTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 4, 2, 1)
)
if mibBuilder.loadTexts:
    adGenDslProxySystemTable.setStatus("current")
_AdGenDslProxySystemEntry_Object = MibTableRow
adGenDslProxySystemEntry = _AdGenDslProxySystemEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 4, 2, 1, 1)
)
adGenDslProxySystemEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adGenDslProxySystemEntry.setStatus("current")


class _AdGenDslProxySystemValid_Type(Integer32):
    """Custom type adGenDslProxySystemValid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("valid", 2),
          ("invalid", 3))
    )


_AdGenDslProxySystemValid_Type.__name__ = "Integer32"
_AdGenDslProxySystemValid_Object = MibTableColumn
adGenDslProxySystemValid = _AdGenDslProxySystemValid_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 4, 2, 1, 1, 1),
    _AdGenDslProxySystemValid_Type()
)
adGenDslProxySystemValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenDslProxySystemValid.setStatus("current")
_AdGenDslProxySystemLastError_Type = DisplayString
_AdGenDslProxySystemLastError_Object = MibTableColumn
adGenDslProxySystemLastError = _AdGenDslProxySystemLastError_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 4, 2, 1, 1, 2),
    _AdGenDslProxySystemLastError_Type()
)
adGenDslProxySystemLastError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenDslProxySystemLastError.setStatus("current")


class _AdGenDslProxySystemType_Type(Integer32):
    """Custom type adGenDslProxySystemType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("twoWire", 1),
          ("fourWire", 2))
    )


_AdGenDslProxySystemType_Type.__name__ = "Integer32"
_AdGenDslProxySystemType_Object = MibTableColumn
adGenDslProxySystemType = _AdGenDslProxySystemType_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 4, 2, 1, 1, 3),
    _AdGenDslProxySystemType_Type()
)
adGenDslProxySystemType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenDslProxySystemType.setStatus("current")
_AdGenDslProxyNumRepeaters_Type = Integer32
_AdGenDslProxyNumRepeaters_Object = MibTableColumn
adGenDslProxyNumRepeaters = _AdGenDslProxyNumRepeaters_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 4, 2, 1, 1, 4),
    _AdGenDslProxyNumRepeaters_Type()
)
adGenDslProxyNumRepeaters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenDslProxyNumRepeaters.setStatus("current")
_AdGenDslProxyLoopbackTable_Object = MibTable
adGenDslProxyLoopbackTable = _AdGenDslProxyLoopbackTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 4, 2, 2)
)
if mibBuilder.loadTexts:
    adGenDslProxyLoopbackTable.setStatus("current")
_AdGenDslProxyLoopbackEntry_Object = MibTableRow
adGenDslProxyLoopbackEntry = _AdGenDslProxyLoopbackEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 4, 2, 2, 1)
)
adGenDslProxyLoopbackEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ADTRAN-SHDSL-MIB", "adEShdslInvIndex"),
)
if mibBuilder.loadTexts:
    adGenDslProxyLoopbackEntry.setStatus("current")


class _AdGenDslProxySetLoopback_Type(Integer32):
    """Custom type adGenDslProxySetLoopback based on Integer32"""
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
        *(("none", 1),
          ("network", 2),
          ("customer", 3),
          ("bilateral", 4))
    )


_AdGenDslProxySetLoopback_Type.__name__ = "Integer32"
_AdGenDslProxySetLoopback_Object = MibTableColumn
adGenDslProxySetLoopback = _AdGenDslProxySetLoopback_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 4, 2, 2, 1, 1),
    _AdGenDslProxySetLoopback_Type()
)
adGenDslProxySetLoopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenDslProxySetLoopback.setStatus("current")


class _AdGenDslProxyLoopbackStatus_Type(Integer32):
    """Custom type adGenDslProxyLoopbackStatus based on Integer32"""
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
        *(("none", 1),
          ("network", 2),
          ("customer", 3),
          ("bilateral", 4))
    )


_AdGenDslProxyLoopbackStatus_Type.__name__ = "Integer32"
_AdGenDslProxyLoopbackStatus_Object = MibTableColumn
adGenDslProxyLoopbackStatus = _AdGenDslProxyLoopbackStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 4, 2, 2, 1, 2),
    _AdGenDslProxyLoopbackStatus_Type()
)
adGenDslProxyLoopbackStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenDslProxyLoopbackStatus.setStatus("current")
_AdGenDslProxyFrameGroundTable_Object = MibTable
adGenDslProxyFrameGroundTable = _AdGenDslProxyFrameGroundTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 4, 2, 3)
)
if mibBuilder.loadTexts:
    adGenDslProxyFrameGroundTable.setStatus("current")
_AdGenDslProxyFrameGroundEntry_Object = MibTableRow
adGenDslProxyFrameGroundEntry = _AdGenDslProxyFrameGroundEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 4, 2, 3, 1)
)
adGenDslProxyFrameGroundEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adGenDslProxyFrameGroundEntry.setStatus("current")


class _AdGenDslProxyFrameGroundResult_Type(Integer32):
    """Custom type adGenDslProxyFrameGroundResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("goodGround", 1),
          ("badGround", 2))
    )


_AdGenDslProxyFrameGroundResult_Type.__name__ = "Integer32"
_AdGenDslProxyFrameGroundResult_Object = MibTableColumn
adGenDslProxyFrameGroundResult = _AdGenDslProxyFrameGroundResult_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 4, 2, 3, 1, 1),
    _AdGenDslProxyFrameGroundResult_Type()
)
adGenDslProxyFrameGroundResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenDslProxyFrameGroundResult.setStatus("current")
_AdGenDslProxyMibConformance_ObjectIdentity = ObjectIdentity
adGenDslProxyMibConformance = _AdGenDslProxyMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 4, 10)
)
_AdGenDslProxyMibGroups_ObjectIdentity = ObjectIdentity
adGenDslProxyMibGroups = _AdGenDslProxyMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 4, 10, 1)
)

# Managed Objects groups

adGenDslProxyCommandGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 4, 10, 1, 1)
)
adGenDslProxyCommandGroup.setObjects(
      *(("ADTRAN-GEN-DSL-PROXY-MIB", "adGenDslProxySystemTypeInitiate"),
        ("ADTRAN-GEN-DSL-PROXY-MIB", "adGenDslProxySystemTypeStatus"),
        ("ADTRAN-GEN-DSL-PROXY-MIB", "adGenDslProxySystemTypeLastTime"),
        ("ADTRAN-GEN-DSL-PROXY-MIB", "adGenDslProxyLoopbackStatusInitiate"),
        ("ADTRAN-GEN-DSL-PROXY-MIB", "adGenDslProxyLoopbackStatusStatus"),
        ("ADTRAN-GEN-DSL-PROXY-MIB", "adGenDslProxyLoopbackStatusLastTime"),
        ("ADTRAN-GEN-DSL-PROXY-MIB", "adGenDslProxySpliceDetectInitiate"),
        ("ADTRAN-GEN-DSL-PROXY-MIB", "adGenDslProxySpliceDetectStatus"),
        ("ADTRAN-GEN-DSL-PROXY-MIB", "adGenDslProxySpliceDetectLastTime"),
        ("ADTRAN-GEN-DSL-PROXY-MIB", "adGenDslProxyFrameGroundInitiate"),
        ("ADTRAN-GEN-DSL-PROXY-MIB", "adGenDslProxyFrameGroundStatus"),
        ("ADTRAN-GEN-DSL-PROXY-MIB", "adGenDslProxyFrameGroundLastTime"))
)
if mibBuilder.loadTexts:
    adGenDslProxyCommandGroup.setStatus("current")

adGenDslProxySystemGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 4, 10, 1, 2)
)
adGenDslProxySystemGroup.setObjects(
      *(("ADTRAN-GEN-DSL-PROXY-MIB", "adGenDslProxySystemValid"),
        ("ADTRAN-GEN-DSL-PROXY-MIB", "adGenDslProxySystemLastError"),
        ("ADTRAN-GEN-DSL-PROXY-MIB", "adGenDslProxySystemType"),
        ("ADTRAN-GEN-DSL-PROXY-MIB", "adGenDslProxyNumRepeaters"))
)
if mibBuilder.loadTexts:
    adGenDslProxySystemGroup.setStatus("current")

adGenDslProxyLoopbackGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 4, 10, 1, 3)
)
adGenDslProxyLoopbackGroup.setObjects(
      *(("ADTRAN-GEN-DSL-PROXY-MIB", "adGenDslProxySetLoopback"),
        ("ADTRAN-GEN-DSL-PROXY-MIB", "adGenDslProxyLoopbackStatus"))
)
if mibBuilder.loadTexts:
    adGenDslProxyLoopbackGroup.setStatus("current")

adGenDslProxyFrameGroundGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 664, 5, 59, 4, 10, 1, 4)
)
adGenDslProxyFrameGroundGroup.setObjects(
    ("ADTRAN-GEN-DSL-PROXY-MIB", "adGenDslProxyFrameGroundStatus")
)
if mibBuilder.loadTexts:
    adGenDslProxyFrameGroundGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ADTRAN-GEN-DSL-PROXY-MIB",
    **{"AdGenDslProxyInitiate": AdGenDslProxyInitiate,
       "AdGenDslProxyStatus": AdGenDslProxyStatus,
       "AdGenDslProxyLastTime": AdGenDslProxyLastTime,
       "adGenDslProxyCommands": adGenDslProxyCommands,
       "adGenDslProxyCommandTable": adGenDslProxyCommandTable,
       "adGenDslProxyCommandEntry": adGenDslProxyCommandEntry,
       "adGenDslProxySystemTypeInitiate": adGenDslProxySystemTypeInitiate,
       "adGenDslProxySystemTypeStatus": adGenDslProxySystemTypeStatus,
       "adGenDslProxySystemTypeLastTime": adGenDslProxySystemTypeLastTime,
       "adGenDslProxyLoopbackStatusInitiate": adGenDslProxyLoopbackStatusInitiate,
       "adGenDslProxyLoopbackStatusStatus": adGenDslProxyLoopbackStatusStatus,
       "adGenDslProxyLoopbackStatusLastTime": adGenDslProxyLoopbackStatusLastTime,
       "adGenDslProxySpliceDetectInitiate": adGenDslProxySpliceDetectInitiate,
       "adGenDslProxySpliceDetectStatus": adGenDslProxySpliceDetectStatus,
       "adGenDslProxySpliceDetectLastTime": adGenDslProxySpliceDetectLastTime,
       "adGenDslProxyFrameGroundInitiate": adGenDslProxyFrameGroundInitiate,
       "adGenDslProxyFrameGroundStatus": adGenDslProxyFrameGroundStatus,
       "adGenDslProxyFrameGroundLastTime": adGenDslProxyFrameGroundLastTime,
       "adGenDslProxyResults": adGenDslProxyResults,
       "adGenDslProxySystemTable": adGenDslProxySystemTable,
       "adGenDslProxySystemEntry": adGenDslProxySystemEntry,
       "adGenDslProxySystemValid": adGenDslProxySystemValid,
       "adGenDslProxySystemLastError": adGenDslProxySystemLastError,
       "adGenDslProxySystemType": adGenDslProxySystemType,
       "adGenDslProxyNumRepeaters": adGenDslProxyNumRepeaters,
       "adGenDslProxyLoopbackTable": adGenDslProxyLoopbackTable,
       "adGenDslProxyLoopbackEntry": adGenDslProxyLoopbackEntry,
       "adGenDslProxySetLoopback": adGenDslProxySetLoopback,
       "adGenDslProxyLoopbackStatus": adGenDslProxyLoopbackStatus,
       "adGenDslProxyFrameGroundTable": adGenDslProxyFrameGroundTable,
       "adGenDslProxyFrameGroundEntry": adGenDslProxyFrameGroundEntry,
       "adGenDslProxyFrameGroundResult": adGenDslProxyFrameGroundResult,
       "adGenDslProxyMibConformance": adGenDslProxyMibConformance,
       "adGenDslProxyMibGroups": adGenDslProxyMibGroups,
       "adGenDslProxyCommandGroup": adGenDslProxyCommandGroup,
       "adGenDslProxySystemGroup": adGenDslProxySystemGroup,
       "adGenDslProxyLoopbackGroup": adGenDslProxyLoopbackGroup,
       "adGenDslProxyFrameGroundGroup": adGenDslProxyFrameGroundGroup,
       "adGenDslProxyMIB": adGenDslProxyMIB}
)
