# SNMP MIB module (ELTEX-POLICY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/eltex/ELTEX-POLICY-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:50:19 2025
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

(diffServClassifierEntry,) = mibBuilder.importSymbols(
    "DIFF-SERV-MIB",
    "diffServClassifierEntry")

(eltMes,) = mibBuilder.importSymbols(
    "ELTEX-MES",
    "eltMes")

(InterfaceIndex,
 InterfaceIndexOrZero) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero")

(PortList,
 VlanId) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "PortList",
    "VlanId")

(Percents,
 VlanPriority) = mibBuilder.importSymbols(
    "RADLAN-MIB",
    "Percents",
    "VlanPriority")

(rlPolicyActionEntry,
 rlPolicyClassifierEntry,
 rlPolicyMeteringClassEntry,
 rlPolicyTrustModeEntry,
 rlPolicyVlanCfgEntry) = mibBuilder.importSymbols(
    "RADLAN-POLICY-MIB",
    "rlPolicyActionEntry",
    "rlPolicyClassifierEntry",
    "rlPolicyMeteringClassEntry",
    "rlPolicyTrustModeEntry",
    "rlPolicyVlanCfgEntry")

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
 iso,
 zeroDotZero) = mibBuilder.importSymbols(
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
    "iso",
    "zeroDotZero")

(DisplayString,
 PhysAddress,
 RowPointer,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowPointer",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

eltMesPolicy = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 59)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class EltPolicyTrustTypes(TextualConvention, Integer32):
    status = "current"
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
        *(("none", 0),
          ("cos", 1),
          ("dscp", 2),
          ("cos-dscp", 3))
    )



# MIB Managed Objects in the order of their OIDs

_EltPolicyClassifier_ObjectIdentity = ObjectIdentity
eltPolicyClassifier = _EltPolicyClassifier_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 59, 2)
)
_EltPolicyClassifierTable_Object = MibTable
eltPolicyClassifierTable = _EltPolicyClassifierTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 59, 2, 4)
)
if mibBuilder.loadTexts:
    eltPolicyClassifierTable.setStatus("current")
_EltPolicyClassifierEntry_Object = MibTableRow
eltPolicyClassifierEntry = _EltPolicyClassifierEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 59, 2, 4, 1)
)
if mibBuilder.loadTexts:
    eltPolicyClassifierEntry.setStatus("current")
_EltPolicyClassifierInListVlanId1To1024_Type = OctetString
_EltPolicyClassifierInListVlanId1To1024_Object = MibTableColumn
eltPolicyClassifierInListVlanId1To1024 = _EltPolicyClassifierInListVlanId1To1024_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 59, 2, 4, 1, 1),
    _EltPolicyClassifierInListVlanId1To1024_Type()
)
eltPolicyClassifierInListVlanId1To1024.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltPolicyClassifierInListVlanId1To1024.setStatus("current")
_EltPolicyClassifierInListVlanId1025To2048_Type = OctetString
_EltPolicyClassifierInListVlanId1025To2048_Object = MibTableColumn
eltPolicyClassifierInListVlanId1025To2048 = _EltPolicyClassifierInListVlanId1025To2048_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 59, 2, 4, 1, 2),
    _EltPolicyClassifierInListVlanId1025To2048_Type()
)
eltPolicyClassifierInListVlanId1025To2048.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltPolicyClassifierInListVlanId1025To2048.setStatus("current")
_EltPolicyClassifierInListVlanId2049To3072_Type = OctetString
_EltPolicyClassifierInListVlanId2049To3072_Object = MibTableColumn
eltPolicyClassifierInListVlanId2049To3072 = _EltPolicyClassifierInListVlanId2049To3072_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 59, 2, 4, 1, 3),
    _EltPolicyClassifierInListVlanId2049To3072_Type()
)
eltPolicyClassifierInListVlanId2049To3072.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltPolicyClassifierInListVlanId2049To3072.setStatus("current")
_EltPolicyClassifierInListVlanId3073To4096_Type = OctetString
_EltPolicyClassifierInListVlanId3073To4096_Object = MibTableColumn
eltPolicyClassifierInListVlanId3073To4096 = _EltPolicyClassifierInListVlanId3073To4096_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 59, 2, 4, 1, 4),
    _EltPolicyClassifierInListVlanId3073To4096_Type()
)
eltPolicyClassifierInListVlanId3073To4096.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltPolicyClassifierInListVlanId3073To4096.setStatus("current")
_EltPolicyMapping_ObjectIdentity = ObjectIdentity
eltPolicyMapping = _EltPolicyMapping_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 59, 3)
)
_EltPolicyVptDscpTable_Object = MibTable
eltPolicyVptDscpTable = _EltPolicyVptDscpTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 59, 3, 1)
)
if mibBuilder.loadTexts:
    eltPolicyVptDscpTable.setStatus("current")
_EltPolicyVptDscpEntry_Object = MibTableRow
eltPolicyVptDscpEntry = _EltPolicyVptDscpEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 59, 3, 1, 1)
)
eltPolicyVptDscpEntry.setIndexNames(
    (0, "ELTEX-POLICY-MIB", "eltPolicyVptValue"),
)
if mibBuilder.loadTexts:
    eltPolicyVptDscpEntry.setStatus("current")


class _EltPolicyVptValue_Type(Integer32):
    """Custom type eltPolicyVptValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_EltPolicyVptValue_Type.__name__ = "Integer32"
_EltPolicyVptValue_Object = MibTableColumn
eltPolicyVptValue = _EltPolicyVptValue_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 59, 3, 1, 1, 1),
    _EltPolicyVptValue_Type()
)
eltPolicyVptValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltPolicyVptValue.setStatus("current")


class _EltPolicyDscpValue_Type(Integer32):
    """Custom type eltPolicyDscpValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_EltPolicyDscpValue_Type.__name__ = "Integer32"
_EltPolicyDscpValue_Object = MibTableColumn
eltPolicyDscpValue = _EltPolicyDscpValue_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 59, 3, 1, 1, 2),
    _EltPolicyDscpValue_Type()
)
eltPolicyDscpValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltPolicyDscpValue.setStatus("current")
_EltPolicyVptDscpStatus_Type = RowStatus
_EltPolicyVptDscpStatus_Object = MibTableColumn
eltPolicyVptDscpStatus = _EltPolicyVptDscpStatus_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 59, 3, 1, 1, 3),
    _EltPolicyVptDscpStatus_Type()
)
eltPolicyVptDscpStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltPolicyVptDscpStatus.setStatus("current")
_EltPolicyTrustModeTable_Object = MibTable
eltPolicyTrustModeTable = _EltPolicyTrustModeTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 59, 3, 2)
)
if mibBuilder.loadTexts:
    eltPolicyTrustModeTable.setStatus("current")
_EltPolicyTrustModeEntry_Object = MibTableRow
eltPolicyTrustModeEntry = _EltPolicyTrustModeEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 59, 3, 2, 1)
)
if mibBuilder.loadTexts:
    eltPolicyTrustModeEntry.setStatus("current")
_EltPolicyTrustModePortMode_Type = EltPolicyTrustTypes
_EltPolicyTrustModePortMode_Object = MibTableColumn
eltPolicyTrustModePortMode = _EltPolicyTrustModePortMode_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 59, 3, 2, 1, 1),
    _EltPolicyTrustModePortMode_Type()
)
eltPolicyTrustModePortMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltPolicyTrustModePortMode.setStatus("current")
_EltPolicyVlanConfiguration_ObjectIdentity = ObjectIdentity
eltPolicyVlanConfiguration = _EltPolicyVlanConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 59, 5)
)
_EltPolicyVlanConfigurationTable_Object = MibTable
eltPolicyVlanConfigurationTable = _EltPolicyVlanConfigurationTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 59, 5, 1)
)
if mibBuilder.loadTexts:
    eltPolicyVlanConfigurationTable.setStatus("current")
_EltPolicyVlanCfgEntry_Object = MibTableRow
eltPolicyVlanCfgEntry = _EltPolicyVlanCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 59, 5, 1, 1)
)
if mibBuilder.loadTexts:
    eltPolicyVlanCfgEntry.setStatus("current")


class _EltPolicyVlanCfgCirPortRateLimitPps_Type(Unsigned32):
    """Custom type eltPolicyVlanCfgCirPortRateLimitPps based on Unsigned32"""
    defaultValue = 0


_EltPolicyVlanCfgCirPortRateLimitPps_Type.__name__ = "Unsigned32"
_EltPolicyVlanCfgCirPortRateLimitPps_Object = MibTableColumn
eltPolicyVlanCfgCirPortRateLimitPps = _EltPolicyVlanCfgCirPortRateLimitPps_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 59, 5, 1, 1, 1),
    _EltPolicyVlanCfgCirPortRateLimitPps_Type()
)
eltPolicyVlanCfgCirPortRateLimitPps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltPolicyVlanCfgCirPortRateLimitPps.setStatus("current")


class _EltPolicyVlanCfgCbsPortRateLimitPackets_Type(Unsigned32):
    """Custom type eltPolicyVlanCfgCbsPortRateLimitPackets based on Unsigned32"""
    defaultValue = 0


_EltPolicyVlanCfgCbsPortRateLimitPackets_Type.__name__ = "Unsigned32"
_EltPolicyVlanCfgCbsPortRateLimitPackets_Object = MibTableColumn
eltPolicyVlanCfgCbsPortRateLimitPackets = _EltPolicyVlanCfgCbsPortRateLimitPackets_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 59, 5, 1, 1, 2),
    _EltPolicyVlanCfgCbsPortRateLimitPackets_Type()
)
eltPolicyVlanCfgCbsPortRateLimitPackets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltPolicyVlanCfgCbsPortRateLimitPackets.setStatus("current")
_EltPolicyMeterClass_ObjectIdentity = ObjectIdentity
eltPolicyMeterClass = _EltPolicyMeterClass_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 59, 6)
)
_EltPolicyMeterClassTable_Object = MibTable
eltPolicyMeterClassTable = _EltPolicyMeterClassTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 59, 6, 1)
)
if mibBuilder.loadTexts:
    eltPolicyMeterClassTable.setStatus("current")
_EltPolicyMeteringClassEntry_Object = MibTableRow
eltPolicyMeteringClassEntry = _EltPolicyMeteringClassEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 59, 6, 1, 1)
)
if mibBuilder.loadTexts:
    eltPolicyMeteringClassEntry.setStatus("current")


class _EltPolicyMeteringClassAggregateMeterRatePps_Type(Unsigned32):
    """Custom type eltPolicyMeteringClassAggregateMeterRatePps based on Unsigned32"""
    defaultValue = 0


_EltPolicyMeteringClassAggregateMeterRatePps_Type.__name__ = "Unsigned32"
_EltPolicyMeteringClassAggregateMeterRatePps_Object = MibTableColumn
eltPolicyMeteringClassAggregateMeterRatePps = _EltPolicyMeteringClassAggregateMeterRatePps_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 59, 6, 1, 1, 1),
    _EltPolicyMeteringClassAggregateMeterRatePps_Type()
)
eltPolicyMeteringClassAggregateMeterRatePps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltPolicyMeteringClassAggregateMeterRatePps.setStatus("current")


class _EltPolicyMeteringClassAggregateMeterBurstSizePackets_Type(Unsigned32):
    """Custom type eltPolicyMeteringClassAggregateMeterBurstSizePackets based on Unsigned32"""
    defaultValue = 0


_EltPolicyMeteringClassAggregateMeterBurstSizePackets_Type.__name__ = "Unsigned32"
_EltPolicyMeteringClassAggregateMeterBurstSizePackets_Object = MibTableColumn
eltPolicyMeteringClassAggregateMeterBurstSizePackets = _EltPolicyMeteringClassAggregateMeterBurstSizePackets_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 59, 6, 1, 1, 2),
    _EltPolicyMeteringClassAggregateMeterBurstSizePackets_Type()
)
eltPolicyMeteringClassAggregateMeterBurstSizePackets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltPolicyMeteringClassAggregateMeterBurstSizePackets.setStatus("current")
_EltPolicyAction_ObjectIdentity = ObjectIdentity
eltPolicyAction = _EltPolicyAction_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 59, 7)
)
_EltPolicyActionTable_Object = MibTable
eltPolicyActionTable = _EltPolicyActionTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 59, 7, 2)
)
if mibBuilder.loadTexts:
    eltPolicyActionTable.setStatus("current")
_EltPolicyActionEntry_Object = MibTableRow
eltPolicyActionEntry = _EltPolicyActionEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 59, 7, 2, 1)
)
if mibBuilder.loadTexts:
    eltPolicyActionEntry.setStatus("current")


class _EltPolicyPpsActionNonDsOutProfileDropPrecedence_Type(Integer32):
    """Custom type eltPolicyPpsActionNonDsOutProfileDropPrecedence based on Integer32"""
    defaultValue = 1

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
        *(("low", 1),
          ("medium", 2),
          ("high", 3),
          ("drop", 4))
    )


_EltPolicyPpsActionNonDsOutProfileDropPrecedence_Type.__name__ = "Integer32"
_EltPolicyPpsActionNonDsOutProfileDropPrecedence_Object = MibTableColumn
eltPolicyPpsActionNonDsOutProfileDropPrecedence = _EltPolicyPpsActionNonDsOutProfileDropPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 59, 7, 2, 1, 1),
    _EltPolicyPpsActionNonDsOutProfileDropPrecedence_Type()
)
eltPolicyPpsActionNonDsOutProfileDropPrecedence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltPolicyPpsActionNonDsOutProfileDropPrecedence.setStatus("current")


class _EltPolicyPpsActionChangeDscpNonConform_Type(TruthValue):
    """Custom type eltPolicyPpsActionChangeDscpNonConform based on TruthValue"""
    defaultValue = 2


_EltPolicyPpsActionChangeDscpNonConform_Type.__name__ = "TruthValue"
_EltPolicyPpsActionChangeDscpNonConform_Object = MibTableColumn
eltPolicyPpsActionChangeDscpNonConform = _EltPolicyPpsActionChangeDscpNonConform_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 59, 7, 2, 1, 2),
    _EltPolicyPpsActionChangeDscpNonConform_Type()
)
eltPolicyPpsActionChangeDscpNonConform.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltPolicyPpsActionChangeDscpNonConform.setStatus("current")
rlPolicyClassifierEntry.registerAugmentions(
    ("ELTEX-POLICY-MIB",
     "eltPolicyClassifierEntry")
)
eltPolicyClassifierEntry.setIndexNames(*rlPolicyClassifierEntry.getIndexNames())
rlPolicyTrustModeEntry.registerAugmentions(
    ("ELTEX-POLICY-MIB",
     "eltPolicyTrustModeEntry")
)
eltPolicyTrustModeEntry.setIndexNames(*rlPolicyTrustModeEntry.getIndexNames())
rlPolicyVlanCfgEntry.registerAugmentions(
    ("ELTEX-POLICY-MIB",
     "eltPolicyVlanCfgEntry")
)
eltPolicyVlanCfgEntry.setIndexNames(*rlPolicyVlanCfgEntry.getIndexNames())
rlPolicyMeteringClassEntry.registerAugmentions(
    ("ELTEX-POLICY-MIB",
     "eltPolicyMeteringClassEntry")
)
eltPolicyMeteringClassEntry.setIndexNames(*rlPolicyMeteringClassEntry.getIndexNames())
rlPolicyActionEntry.registerAugmentions(
    ("ELTEX-POLICY-MIB",
     "eltPolicyActionEntry")
)
eltPolicyActionEntry.setIndexNames(*rlPolicyActionEntry.getIndexNames())

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ELTEX-POLICY-MIB",
    **{"EltPolicyTrustTypes": EltPolicyTrustTypes,
       "eltMesPolicy": eltMesPolicy,
       "eltPolicyClassifier": eltPolicyClassifier,
       "eltPolicyClassifierTable": eltPolicyClassifierTable,
       "eltPolicyClassifierEntry": eltPolicyClassifierEntry,
       "eltPolicyClassifierInListVlanId1To1024": eltPolicyClassifierInListVlanId1To1024,
       "eltPolicyClassifierInListVlanId1025To2048": eltPolicyClassifierInListVlanId1025To2048,
       "eltPolicyClassifierInListVlanId2049To3072": eltPolicyClassifierInListVlanId2049To3072,
       "eltPolicyClassifierInListVlanId3073To4096": eltPolicyClassifierInListVlanId3073To4096,
       "eltPolicyMapping": eltPolicyMapping,
       "eltPolicyVptDscpTable": eltPolicyVptDscpTable,
       "eltPolicyVptDscpEntry": eltPolicyVptDscpEntry,
       "eltPolicyVptValue": eltPolicyVptValue,
       "eltPolicyDscpValue": eltPolicyDscpValue,
       "eltPolicyVptDscpStatus": eltPolicyVptDscpStatus,
       "eltPolicyTrustModeTable": eltPolicyTrustModeTable,
       "eltPolicyTrustModeEntry": eltPolicyTrustModeEntry,
       "eltPolicyTrustModePortMode": eltPolicyTrustModePortMode,
       "eltPolicyVlanConfiguration": eltPolicyVlanConfiguration,
       "eltPolicyVlanConfigurationTable": eltPolicyVlanConfigurationTable,
       "eltPolicyVlanCfgEntry": eltPolicyVlanCfgEntry,
       "eltPolicyVlanCfgCirPortRateLimitPps": eltPolicyVlanCfgCirPortRateLimitPps,
       "eltPolicyVlanCfgCbsPortRateLimitPackets": eltPolicyVlanCfgCbsPortRateLimitPackets,
       "eltPolicyMeterClass": eltPolicyMeterClass,
       "eltPolicyMeterClassTable": eltPolicyMeterClassTable,
       "eltPolicyMeteringClassEntry": eltPolicyMeteringClassEntry,
       "eltPolicyMeteringClassAggregateMeterRatePps": eltPolicyMeteringClassAggregateMeterRatePps,
       "eltPolicyMeteringClassAggregateMeterBurstSizePackets": eltPolicyMeteringClassAggregateMeterBurstSizePackets,
       "eltPolicyAction": eltPolicyAction,
       "eltPolicyActionTable": eltPolicyActionTable,
       "eltPolicyActionEntry": eltPolicyActionEntry,
       "eltPolicyPpsActionNonDsOutProfileDropPrecedence": eltPolicyPpsActionNonDsOutProfileDropPrecedence,
       "eltPolicyPpsActionChangeDscpNonConform": eltPolicyPpsActionChangeDscpNonConform}
)
