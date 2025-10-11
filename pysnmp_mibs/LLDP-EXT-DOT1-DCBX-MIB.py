# SNMP MIB module (LLDP-EXT-DOT1-DCBX-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/supermicro/LLDP-EXT-DOT1-DCBX-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:44:17 2025
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

(IEEE8021PriorityValue,) = mibBuilder.importSymbols(
    "IEEE8021-TC-MIB",
    "IEEE8021PriorityValue")

(lldpV2Xdot1MIB,) = mibBuilder.importSymbols(
    "LLDP-EXT-DOT1-V2-MIB",
    "lldpV2Xdot1MIB")

(lldpV2LocPortIfIndex,
 lldpV2PortConfigEntry,
 lldpV2RemIndex,
 lldpV2RemLocalDestMACAddress,
 lldpV2RemLocalIfIndex,
 lldpV2RemTimeMark) = mibBuilder.importSymbols(
    "LLDP-V2-MIB",
    "lldpV2LocPortIfIndex",
    "lldpV2PortConfigEntry",
    "lldpV2RemIndex",
    "lldpV2RemLocalDestMACAddress",
    "lldpV2RemLocalIfIndex",
    "lldpV2RemTimeMark")

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

lldpXdot1dcbxMIB = ModuleIdentity(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5)
)
if mibBuilder.loadTexts:
    lldpXdot1dcbxMIB.setRevisions(
        ("2009-11-25 18:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class LldpXdot1dcbxTrafficClassValue(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )



class LldpXdot1dcbxTrafficClassBandwidthValue(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )



class LldpXdot1dcbxAppSelector(TextualConvention, Integer32):
    status = "current"
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
        *(("asEthertype", 1),
          ("asTCPPortNumber", 2),
          ("asUDPPortNumber", 3),
          ("asTCPUDPPortNumber", 4))
    )



class LldpXdot1dcbxAppProtocol(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



class LldpXdot1dcbxSupportedCapacity(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )



class LldpXdot1dcbxTrafficSelectionAlgorithm(TextualConvention, Integer32):
    status = "current"
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
        *(("tsaStrictPriority", 0),
          ("tsaCreditBasedShaper", 1),
          ("tsaEnhancedTransmission", 2),
          ("tsaVendorSpecific", 255))
    )



# MIB Managed Objects in the order of their OIDs

_LldpXdot1dcbxObjects_ObjectIdentity = ObjectIdentity
lldpXdot1dcbxObjects = _LldpXdot1dcbxObjects_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1)
)
_LldpXdot1dcbxConfig_ObjectIdentity = ObjectIdentity
lldpXdot1dcbxConfig = _LldpXdot1dcbxConfig_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 1)
)
_LldpXdot1dcbxConfigETSConfigurationTable_Object = MibTable
lldpXdot1dcbxConfigETSConfigurationTable = _LldpXdot1dcbxConfigETSConfigurationTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 1, 1)
)
if mibBuilder.loadTexts:
    lldpXdot1dcbxConfigETSConfigurationTable.setStatus("current")
_LldpXdot1dcbxConfigETSConfigurationEntry_Object = MibTableRow
lldpXdot1dcbxConfigETSConfigurationEntry = _LldpXdot1dcbxConfigETSConfigurationEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    lldpXdot1dcbxConfigETSConfigurationEntry.setStatus("current")


class _LldpXdot1dcbxConfigETSConfigurationTxEnable_Type(TruthValue):
    """Custom type lldpXdot1dcbxConfigETSConfigurationTxEnable based on TruthValue"""
    defaultValue = 2


_LldpXdot1dcbxConfigETSConfigurationTxEnable_Type.__name__ = "TruthValue"
_LldpXdot1dcbxConfigETSConfigurationTxEnable_Object = MibTableColumn
lldpXdot1dcbxConfigETSConfigurationTxEnable = _LldpXdot1dcbxConfigETSConfigurationTxEnable_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 1, 1, 1, 1),
    _LldpXdot1dcbxConfigETSConfigurationTxEnable_Type()
)
lldpXdot1dcbxConfigETSConfigurationTxEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpXdot1dcbxConfigETSConfigurationTxEnable.setStatus("current")
_LldpXdot1dcbxConfigETSRecommendationTable_Object = MibTable
lldpXdot1dcbxConfigETSRecommendationTable = _LldpXdot1dcbxConfigETSRecommendationTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 1, 2)
)
if mibBuilder.loadTexts:
    lldpXdot1dcbxConfigETSRecommendationTable.setStatus("current")
_LldpXdot1dcbxConfigETSRecommendationEntry_Object = MibTableRow
lldpXdot1dcbxConfigETSRecommendationEntry = _LldpXdot1dcbxConfigETSRecommendationEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    lldpXdot1dcbxConfigETSRecommendationEntry.setStatus("current")


class _LldpXdot1dcbxConfigETSRecommendationTxEnable_Type(TruthValue):
    """Custom type lldpXdot1dcbxConfigETSRecommendationTxEnable based on TruthValue"""
    defaultValue = 2


_LldpXdot1dcbxConfigETSRecommendationTxEnable_Type.__name__ = "TruthValue"
_LldpXdot1dcbxConfigETSRecommendationTxEnable_Object = MibTableColumn
lldpXdot1dcbxConfigETSRecommendationTxEnable = _LldpXdot1dcbxConfigETSRecommendationTxEnable_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 1, 2, 1, 1),
    _LldpXdot1dcbxConfigETSRecommendationTxEnable_Type()
)
lldpXdot1dcbxConfigETSRecommendationTxEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpXdot1dcbxConfigETSRecommendationTxEnable.setStatus("current")
_LldpXdot1dcbxConfigPFCTable_Object = MibTable
lldpXdot1dcbxConfigPFCTable = _LldpXdot1dcbxConfigPFCTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 1, 3)
)
if mibBuilder.loadTexts:
    lldpXdot1dcbxConfigPFCTable.setStatus("current")
_LldpXdot1dcbxConfigPFCEntry_Object = MibTableRow
lldpXdot1dcbxConfigPFCEntry = _LldpXdot1dcbxConfigPFCEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 1, 3, 1)
)
if mibBuilder.loadTexts:
    lldpXdot1dcbxConfigPFCEntry.setStatus("current")


class _LldpXdot1dcbxConfigPFCTxEnable_Type(TruthValue):
    """Custom type lldpXdot1dcbxConfigPFCTxEnable based on TruthValue"""
    defaultValue = 2


_LldpXdot1dcbxConfigPFCTxEnable_Type.__name__ = "TruthValue"
_LldpXdot1dcbxConfigPFCTxEnable_Object = MibTableColumn
lldpXdot1dcbxConfigPFCTxEnable = _LldpXdot1dcbxConfigPFCTxEnable_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 1, 3, 1, 1),
    _LldpXdot1dcbxConfigPFCTxEnable_Type()
)
lldpXdot1dcbxConfigPFCTxEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpXdot1dcbxConfigPFCTxEnable.setStatus("current")
_LldpXdot1dcbxConfigApplicationPriorityTable_Object = MibTable
lldpXdot1dcbxConfigApplicationPriorityTable = _LldpXdot1dcbxConfigApplicationPriorityTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 1, 4)
)
if mibBuilder.loadTexts:
    lldpXdot1dcbxConfigApplicationPriorityTable.setStatus("current")
_LldpXdot1dcbxConfigApplicationPriorityEntry_Object = MibTableRow
lldpXdot1dcbxConfigApplicationPriorityEntry = _LldpXdot1dcbxConfigApplicationPriorityEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 1, 4, 1)
)
if mibBuilder.loadTexts:
    lldpXdot1dcbxConfigApplicationPriorityEntry.setStatus("current")


class _LldpXdot1dcbxConfigApplicationPriorityTxEnable_Type(TruthValue):
    """Custom type lldpXdot1dcbxConfigApplicationPriorityTxEnable based on TruthValue"""
    defaultValue = 2


_LldpXdot1dcbxConfigApplicationPriorityTxEnable_Type.__name__ = "TruthValue"
_LldpXdot1dcbxConfigApplicationPriorityTxEnable_Object = MibTableColumn
lldpXdot1dcbxConfigApplicationPriorityTxEnable = _LldpXdot1dcbxConfigApplicationPriorityTxEnable_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 1, 4, 1, 1),
    _LldpXdot1dcbxConfigApplicationPriorityTxEnable_Type()
)
lldpXdot1dcbxConfigApplicationPriorityTxEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpXdot1dcbxConfigApplicationPriorityTxEnable.setStatus("current")
_LldpXdot1dcbxLocalData_ObjectIdentity = ObjectIdentity
lldpXdot1dcbxLocalData = _LldpXdot1dcbxLocalData_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 2)
)
_LldpXdot1dcbxLocETSConfiguration_ObjectIdentity = ObjectIdentity
lldpXdot1dcbxLocETSConfiguration = _LldpXdot1dcbxLocETSConfiguration_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 2, 1)
)
_LldpXdot1dcbxLocETSBasicConfigurationTable_Object = MibTable
lldpXdot1dcbxLocETSBasicConfigurationTable = _LldpXdot1dcbxLocETSBasicConfigurationTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    lldpXdot1dcbxLocETSBasicConfigurationTable.setStatus("current")
_LldpXdot1dcbxLocETSBasicConfigurationEntry_Object = MibTableRow
lldpXdot1dcbxLocETSBasicConfigurationEntry = _LldpXdot1dcbxLocETSBasicConfigurationEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 2, 1, 1, 1)
)
lldpXdot1dcbxLocETSBasicConfigurationEntry.setIndexNames(
    (0, "LLDP-V2-MIB", "lldpV2LocPortIfIndex"),
)
if mibBuilder.loadTexts:
    lldpXdot1dcbxLocETSBasicConfigurationEntry.setStatus("current")
_LldpXdot1dcbxLocETSConCreditBasedShaperSupport_Type = TruthValue
_LldpXdot1dcbxLocETSConCreditBasedShaperSupport_Object = MibTableColumn
lldpXdot1dcbxLocETSConCreditBasedShaperSupport = _LldpXdot1dcbxLocETSConCreditBasedShaperSupport_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 2, 1, 1, 1, 1),
    _LldpXdot1dcbxLocETSConCreditBasedShaperSupport_Type()
)
lldpXdot1dcbxLocETSConCreditBasedShaperSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot1dcbxLocETSConCreditBasedShaperSupport.setStatus("current")
_LldpXdot1dcbxLocETSConTrafficClassesSupported_Type = LldpXdot1dcbxSupportedCapacity
_LldpXdot1dcbxLocETSConTrafficClassesSupported_Object = MibTableColumn
lldpXdot1dcbxLocETSConTrafficClassesSupported = _LldpXdot1dcbxLocETSConTrafficClassesSupported_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 2, 1, 1, 1, 2),
    _LldpXdot1dcbxLocETSConTrafficClassesSupported_Type()
)
lldpXdot1dcbxLocETSConTrafficClassesSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot1dcbxLocETSConTrafficClassesSupported.setStatus("current")
_LldpXdot1dcbxLocETSConWilling_Type = TruthValue
_LldpXdot1dcbxLocETSConWilling_Object = MibTableColumn
lldpXdot1dcbxLocETSConWilling = _LldpXdot1dcbxLocETSConWilling_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 2, 1, 1, 1, 3),
    _LldpXdot1dcbxLocETSConWilling_Type()
)
lldpXdot1dcbxLocETSConWilling.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot1dcbxLocETSConWilling.setStatus("current")
_LldpXdot1dcbxLocETSConPriorityAssignmentTable_Object = MibTable
lldpXdot1dcbxLocETSConPriorityAssignmentTable = _LldpXdot1dcbxLocETSConPriorityAssignmentTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 2, 1, 2)
)
if mibBuilder.loadTexts:
    lldpXdot1dcbxLocETSConPriorityAssignmentTable.setStatus("current")
_LldpXdot1dcbxLocETSConPriorityAssignmentEntry_Object = MibTableRow
lldpXdot1dcbxLocETSConPriorityAssignmentEntry = _LldpXdot1dcbxLocETSConPriorityAssignmentEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 2, 1, 2, 1)
)
lldpXdot1dcbxLocETSConPriorityAssignmentEntry.setIndexNames(
    (0, "LLDP-V2-MIB", "lldpV2LocPortIfIndex"),
    (0, "LLDP-EXT-DOT1-DCBX-MIB", "lldpXdot1dcbxLocETSConPriority"),
)
if mibBuilder.loadTexts:
    lldpXdot1dcbxLocETSConPriorityAssignmentEntry.setStatus("current")
_LldpXdot1dcbxLocETSConPriority_Type = IEEE8021PriorityValue
_LldpXdot1dcbxLocETSConPriority_Object = MibTableColumn
lldpXdot1dcbxLocETSConPriority = _LldpXdot1dcbxLocETSConPriority_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 2, 1, 2, 1, 1),
    _LldpXdot1dcbxLocETSConPriority_Type()
)
lldpXdot1dcbxLocETSConPriority.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lldpXdot1dcbxLocETSConPriority.setStatus("current")
_LldpXdot1dcbxLocETSConPriTrafficClass_Type = LldpXdot1dcbxTrafficClassValue
_LldpXdot1dcbxLocETSConPriTrafficClass_Object = MibTableColumn
lldpXdot1dcbxLocETSConPriTrafficClass = _LldpXdot1dcbxLocETSConPriTrafficClass_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 2, 1, 2, 1, 2),
    _LldpXdot1dcbxLocETSConPriTrafficClass_Type()
)
lldpXdot1dcbxLocETSConPriTrafficClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot1dcbxLocETSConPriTrafficClass.setStatus("current")
_LldpXdot1dcbxLocETSConTrafficClassBandwidthTable_Object = MibTable
lldpXdot1dcbxLocETSConTrafficClassBandwidthTable = _LldpXdot1dcbxLocETSConTrafficClassBandwidthTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 2, 1, 3)
)
if mibBuilder.loadTexts:
    lldpXdot1dcbxLocETSConTrafficClassBandwidthTable.setStatus("current")
_LldpXdot1dcbxLocETSConTrafficClassBandwidthEntry_Object = MibTableRow
lldpXdot1dcbxLocETSConTrafficClassBandwidthEntry = _LldpXdot1dcbxLocETSConTrafficClassBandwidthEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 2, 1, 3, 1)
)
lldpXdot1dcbxLocETSConTrafficClassBandwidthEntry.setIndexNames(
    (0, "LLDP-V2-MIB", "lldpV2LocPortIfIndex"),
    (0, "LLDP-EXT-DOT1-DCBX-MIB", "lldpXdot1dcbxLocETSConTrafficClass"),
)
if mibBuilder.loadTexts:
    lldpXdot1dcbxLocETSConTrafficClassBandwidthEntry.setStatus("current")
_LldpXdot1dcbxLocETSConTrafficClass_Type = LldpXdot1dcbxTrafficClassValue
_LldpXdot1dcbxLocETSConTrafficClass_Object = MibTableColumn
lldpXdot1dcbxLocETSConTrafficClass = _LldpXdot1dcbxLocETSConTrafficClass_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 2, 1, 3, 1, 1),
    _LldpXdot1dcbxLocETSConTrafficClass_Type()
)
lldpXdot1dcbxLocETSConTrafficClass.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lldpXdot1dcbxLocETSConTrafficClass.setStatus("current")
_LldpXdot1dcbxLocETSConTrafficClassBandwidth_Type = LldpXdot1dcbxTrafficClassBandwidthValue
_LldpXdot1dcbxLocETSConTrafficClassBandwidth_Object = MibTableColumn
lldpXdot1dcbxLocETSConTrafficClassBandwidth = _LldpXdot1dcbxLocETSConTrafficClassBandwidth_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 2, 1, 3, 1, 2),
    _LldpXdot1dcbxLocETSConTrafficClassBandwidth_Type()
)
lldpXdot1dcbxLocETSConTrafficClassBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot1dcbxLocETSConTrafficClassBandwidth.setStatus("current")
_LldpXdot1dcbxLocETSConTrafficSelectionAlgorithmTable_Object = MibTable
lldpXdot1dcbxLocETSConTrafficSelectionAlgorithmTable = _LldpXdot1dcbxLocETSConTrafficSelectionAlgorithmTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 2, 1, 4)
)
if mibBuilder.loadTexts:
    lldpXdot1dcbxLocETSConTrafficSelectionAlgorithmTable.setStatus("current")
_LldpXdot1dcbxLocETSConTrafficSelectionAlgorithmEntry_Object = MibTableRow
lldpXdot1dcbxLocETSConTrafficSelectionAlgorithmEntry = _LldpXdot1dcbxLocETSConTrafficSelectionAlgorithmEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 2, 1, 4, 1)
)
lldpXdot1dcbxLocETSConTrafficSelectionAlgorithmEntry.setIndexNames(
    (0, "LLDP-V2-MIB", "lldpV2LocPortIfIndex"),
    (0, "LLDP-EXT-DOT1-DCBX-MIB", "lldpXdot1dcbxLocETSConTSATrafficClass"),
)
if mibBuilder.loadTexts:
    lldpXdot1dcbxLocETSConTrafficSelectionAlgorithmEntry.setStatus("current")
_LldpXdot1dcbxLocETSConTSATrafficClass_Type = LldpXdot1dcbxTrafficClassValue
_LldpXdot1dcbxLocETSConTSATrafficClass_Object = MibTableColumn
lldpXdot1dcbxLocETSConTSATrafficClass = _LldpXdot1dcbxLocETSConTSATrafficClass_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 2, 1, 4, 1, 1),
    _LldpXdot1dcbxLocETSConTSATrafficClass_Type()
)
lldpXdot1dcbxLocETSConTSATrafficClass.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lldpXdot1dcbxLocETSConTSATrafficClass.setStatus("current")
_LldpXdot1dcbxLocETSConTrafficSelectionAlgorithm_Type = LldpXdot1dcbxTrafficSelectionAlgorithm
_LldpXdot1dcbxLocETSConTrafficSelectionAlgorithm_Object = MibTableColumn
lldpXdot1dcbxLocETSConTrafficSelectionAlgorithm = _LldpXdot1dcbxLocETSConTrafficSelectionAlgorithm_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 2, 1, 4, 1, 2),
    _LldpXdot1dcbxLocETSConTrafficSelectionAlgorithm_Type()
)
lldpXdot1dcbxLocETSConTrafficSelectionAlgorithm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot1dcbxLocETSConTrafficSelectionAlgorithm.setStatus("current")
_LldpXdot1dcbxLocETSReco_ObjectIdentity = ObjectIdentity
lldpXdot1dcbxLocETSReco = _LldpXdot1dcbxLocETSReco_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 2, 2)
)
_LldpXdot1dcbxLocETSRecoTrafficClassBandwidthTable_Object = MibTable
lldpXdot1dcbxLocETSRecoTrafficClassBandwidthTable = _LldpXdot1dcbxLocETSRecoTrafficClassBandwidthTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    lldpXdot1dcbxLocETSRecoTrafficClassBandwidthTable.setStatus("current")
_LldpXdot1dcbxLocETSRecoTrafficClassBandwidthEntry_Object = MibTableRow
lldpXdot1dcbxLocETSRecoTrafficClassBandwidthEntry = _LldpXdot1dcbxLocETSRecoTrafficClassBandwidthEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 2, 2, 1, 1)
)
lldpXdot1dcbxLocETSRecoTrafficClassBandwidthEntry.setIndexNames(
    (0, "LLDP-V2-MIB", "lldpV2LocPortIfIndex"),
    (0, "LLDP-EXT-DOT1-DCBX-MIB", "lldpXdot1dcbxLocETSRecoTrafficClass"),
)
if mibBuilder.loadTexts:
    lldpXdot1dcbxLocETSRecoTrafficClassBandwidthEntry.setStatus("current")
_LldpXdot1dcbxLocETSRecoTrafficClass_Type = LldpXdot1dcbxTrafficClassValue
_LldpXdot1dcbxLocETSRecoTrafficClass_Object = MibTableColumn
lldpXdot1dcbxLocETSRecoTrafficClass = _LldpXdot1dcbxLocETSRecoTrafficClass_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 2, 2, 1, 1, 1),
    _LldpXdot1dcbxLocETSRecoTrafficClass_Type()
)
lldpXdot1dcbxLocETSRecoTrafficClass.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lldpXdot1dcbxLocETSRecoTrafficClass.setStatus("current")
_LldpXdot1dcbxLocETSRecoTrafficClassBandwidth_Type = LldpXdot1dcbxTrafficClassBandwidthValue
_LldpXdot1dcbxLocETSRecoTrafficClassBandwidth_Object = MibTableColumn
lldpXdot1dcbxLocETSRecoTrafficClassBandwidth = _LldpXdot1dcbxLocETSRecoTrafficClassBandwidth_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 2, 2, 1, 1, 2),
    _LldpXdot1dcbxLocETSRecoTrafficClassBandwidth_Type()
)
lldpXdot1dcbxLocETSRecoTrafficClassBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot1dcbxLocETSRecoTrafficClassBandwidth.setStatus("current")
_LldpXdot1dcbxLocETSRecoTrafficSelectionAlgorithmTable_Object = MibTable
lldpXdot1dcbxLocETSRecoTrafficSelectionAlgorithmTable = _LldpXdot1dcbxLocETSRecoTrafficSelectionAlgorithmTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 2, 2, 2)
)
if mibBuilder.loadTexts:
    lldpXdot1dcbxLocETSRecoTrafficSelectionAlgorithmTable.setStatus("current")
_LldpXdot1dcbxLocETSRecoTrafficSelectionAlgorithmEntry_Object = MibTableRow
lldpXdot1dcbxLocETSRecoTrafficSelectionAlgorithmEntry = _LldpXdot1dcbxLocETSRecoTrafficSelectionAlgorithmEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 2, 2, 2, 1)
)
lldpXdot1dcbxLocETSRecoTrafficSelectionAlgorithmEntry.setIndexNames(
    (0, "LLDP-V2-MIB", "lldpV2LocPortIfIndex"),
    (0, "LLDP-EXT-DOT1-DCBX-MIB", "lldpXdot1dcbxLocETSRecoTSATrafficClass"),
)
if mibBuilder.loadTexts:
    lldpXdot1dcbxLocETSRecoTrafficSelectionAlgorithmEntry.setStatus("current")
_LldpXdot1dcbxLocETSRecoTSATrafficClass_Type = LldpXdot1dcbxTrafficClassValue
_LldpXdot1dcbxLocETSRecoTSATrafficClass_Object = MibTableColumn
lldpXdot1dcbxLocETSRecoTSATrafficClass = _LldpXdot1dcbxLocETSRecoTSATrafficClass_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 2, 2, 2, 1, 1),
    _LldpXdot1dcbxLocETSRecoTSATrafficClass_Type()
)
lldpXdot1dcbxLocETSRecoTSATrafficClass.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lldpXdot1dcbxLocETSRecoTSATrafficClass.setStatus("current")
_LldpXdot1dcbxLocETSRecoTrafficSelectionAlgorithm_Type = LldpXdot1dcbxTrafficSelectionAlgorithm
_LldpXdot1dcbxLocETSRecoTrafficSelectionAlgorithm_Object = MibTableColumn
lldpXdot1dcbxLocETSRecoTrafficSelectionAlgorithm = _LldpXdot1dcbxLocETSRecoTrafficSelectionAlgorithm_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 2, 2, 2, 1, 2),
    _LldpXdot1dcbxLocETSRecoTrafficSelectionAlgorithm_Type()
)
lldpXdot1dcbxLocETSRecoTrafficSelectionAlgorithm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot1dcbxLocETSRecoTrafficSelectionAlgorithm.setStatus("current")
_LldpXdot1dcbxLocPFC_ObjectIdentity = ObjectIdentity
lldpXdot1dcbxLocPFC = _LldpXdot1dcbxLocPFC_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 2, 3)
)
_LldpXdot1dcbxLocPFCBasicTable_Object = MibTable
lldpXdot1dcbxLocPFCBasicTable = _LldpXdot1dcbxLocPFCBasicTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 2, 3, 1)
)
if mibBuilder.loadTexts:
    lldpXdot1dcbxLocPFCBasicTable.setStatus("current")
_LldpXdot1dcbxLocPFCBasicEntry_Object = MibTableRow
lldpXdot1dcbxLocPFCBasicEntry = _LldpXdot1dcbxLocPFCBasicEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 2, 3, 1, 1)
)
lldpXdot1dcbxLocPFCBasicEntry.setIndexNames(
    (0, "LLDP-V2-MIB", "lldpV2LocPortIfIndex"),
)
if mibBuilder.loadTexts:
    lldpXdot1dcbxLocPFCBasicEntry.setStatus("current")
_LldpXdot1dcbxLocPFCWilling_Type = TruthValue
_LldpXdot1dcbxLocPFCWilling_Object = MibTableColumn
lldpXdot1dcbxLocPFCWilling = _LldpXdot1dcbxLocPFCWilling_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 2, 3, 1, 1, 1),
    _LldpXdot1dcbxLocPFCWilling_Type()
)
lldpXdot1dcbxLocPFCWilling.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot1dcbxLocPFCWilling.setStatus("current")
_LldpXdot1dcbxLocPFCMBC_Type = TruthValue
_LldpXdot1dcbxLocPFCMBC_Object = MibTableColumn
lldpXdot1dcbxLocPFCMBC = _LldpXdot1dcbxLocPFCMBC_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 2, 3, 1, 1, 2),
    _LldpXdot1dcbxLocPFCMBC_Type()
)
lldpXdot1dcbxLocPFCMBC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot1dcbxLocPFCMBC.setStatus("current")
_LldpXdot1dcbxLocPFCCap_Type = LldpXdot1dcbxSupportedCapacity
_LldpXdot1dcbxLocPFCCap_Object = MibTableColumn
lldpXdot1dcbxLocPFCCap = _LldpXdot1dcbxLocPFCCap_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 2, 3, 1, 1, 3),
    _LldpXdot1dcbxLocPFCCap_Type()
)
lldpXdot1dcbxLocPFCCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot1dcbxLocPFCCap.setStatus("current")
_LldpXdot1dcbxLocPFCEnableTable_Object = MibTable
lldpXdot1dcbxLocPFCEnableTable = _LldpXdot1dcbxLocPFCEnableTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 2, 3, 2)
)
if mibBuilder.loadTexts:
    lldpXdot1dcbxLocPFCEnableTable.setStatus("current")
_LldpXdot1dcbxLocPFCEnableEntry_Object = MibTableRow
lldpXdot1dcbxLocPFCEnableEntry = _LldpXdot1dcbxLocPFCEnableEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 2, 3, 2, 1)
)
lldpXdot1dcbxLocPFCEnableEntry.setIndexNames(
    (0, "LLDP-V2-MIB", "lldpV2LocPortIfIndex"),
    (0, "LLDP-EXT-DOT1-DCBX-MIB", "lldpXdot1dcbxLocPFCEnablePriority"),
)
if mibBuilder.loadTexts:
    lldpXdot1dcbxLocPFCEnableEntry.setStatus("current")
_LldpXdot1dcbxLocPFCEnablePriority_Type = IEEE8021PriorityValue
_LldpXdot1dcbxLocPFCEnablePriority_Object = MibTableColumn
lldpXdot1dcbxLocPFCEnablePriority = _LldpXdot1dcbxLocPFCEnablePriority_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 2, 3, 2, 1, 1),
    _LldpXdot1dcbxLocPFCEnablePriority_Type()
)
lldpXdot1dcbxLocPFCEnablePriority.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lldpXdot1dcbxLocPFCEnablePriority.setStatus("current")
_LldpXdot1dcbxLocPFCEnableEnabled_Type = TruthValue
_LldpXdot1dcbxLocPFCEnableEnabled_Object = MibTableColumn
lldpXdot1dcbxLocPFCEnableEnabled = _LldpXdot1dcbxLocPFCEnableEnabled_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 2, 3, 2, 1, 2),
    _LldpXdot1dcbxLocPFCEnableEnabled_Type()
)
lldpXdot1dcbxLocPFCEnableEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot1dcbxLocPFCEnableEnabled.setStatus("current")
_LldpXdot1dcbxLocApplicationPriorityAppTable_Object = MibTable
lldpXdot1dcbxLocApplicationPriorityAppTable = _LldpXdot1dcbxLocApplicationPriorityAppTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 2, 4)
)
if mibBuilder.loadTexts:
    lldpXdot1dcbxLocApplicationPriorityAppTable.setStatus("current")
_LldpXdot1dcbxLocApplicationPriorityAppEntry_Object = MibTableRow
lldpXdot1dcbxLocApplicationPriorityAppEntry = _LldpXdot1dcbxLocApplicationPriorityAppEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 2, 4, 1)
)
lldpXdot1dcbxLocApplicationPriorityAppEntry.setIndexNames(
    (0, "LLDP-V2-MIB", "lldpV2LocPortIfIndex"),
    (0, "LLDP-EXT-DOT1-DCBX-MIB", "lldpXdot1dcbxLocApplicationPriorityAESelector"),
    (0, "LLDP-EXT-DOT1-DCBX-MIB", "lldpXdot1dcbxLocApplicationPriorityAEProtocol"),
)
if mibBuilder.loadTexts:
    lldpXdot1dcbxLocApplicationPriorityAppEntry.setStatus("current")
_LldpXdot1dcbxLocApplicationPriorityAESelector_Type = LldpXdot1dcbxAppSelector
_LldpXdot1dcbxLocApplicationPriorityAESelector_Object = MibTableColumn
lldpXdot1dcbxLocApplicationPriorityAESelector = _LldpXdot1dcbxLocApplicationPriorityAESelector_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 2, 4, 1, 1),
    _LldpXdot1dcbxLocApplicationPriorityAESelector_Type()
)
lldpXdot1dcbxLocApplicationPriorityAESelector.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lldpXdot1dcbxLocApplicationPriorityAESelector.setStatus("current")
_LldpXdot1dcbxLocApplicationPriorityAEProtocol_Type = LldpXdot1dcbxAppProtocol
_LldpXdot1dcbxLocApplicationPriorityAEProtocol_Object = MibTableColumn
lldpXdot1dcbxLocApplicationPriorityAEProtocol = _LldpXdot1dcbxLocApplicationPriorityAEProtocol_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 2, 4, 1, 2),
    _LldpXdot1dcbxLocApplicationPriorityAEProtocol_Type()
)
lldpXdot1dcbxLocApplicationPriorityAEProtocol.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lldpXdot1dcbxLocApplicationPriorityAEProtocol.setStatus("current")
_LldpXdot1dcbxLocApplicationPriorityAEPriority_Type = IEEE8021PriorityValue
_LldpXdot1dcbxLocApplicationPriorityAEPriority_Object = MibTableColumn
lldpXdot1dcbxLocApplicationPriorityAEPriority = _LldpXdot1dcbxLocApplicationPriorityAEPriority_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 2, 4, 1, 3),
    _LldpXdot1dcbxLocApplicationPriorityAEPriority_Type()
)
lldpXdot1dcbxLocApplicationPriorityAEPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot1dcbxLocApplicationPriorityAEPriority.setStatus("current")
_LldpXdot1dcbxRemoteData_ObjectIdentity = ObjectIdentity
lldpXdot1dcbxRemoteData = _LldpXdot1dcbxRemoteData_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 3)
)
_LldpXdot1dcbxRemETSConfiguration_ObjectIdentity = ObjectIdentity
lldpXdot1dcbxRemETSConfiguration = _LldpXdot1dcbxRemETSConfiguration_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 3, 1)
)
_LldpXdot1dcbxRemETSBasicConfigurationTable_Object = MibTable
lldpXdot1dcbxRemETSBasicConfigurationTable = _LldpXdot1dcbxRemETSBasicConfigurationTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 3, 1, 1)
)
if mibBuilder.loadTexts:
    lldpXdot1dcbxRemETSBasicConfigurationTable.setStatus("current")
_LldpXdot1dcbxRemETSBasicConfigurationEntry_Object = MibTableRow
lldpXdot1dcbxRemETSBasicConfigurationEntry = _LldpXdot1dcbxRemETSBasicConfigurationEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 3, 1, 1, 1)
)
lldpXdot1dcbxRemETSBasicConfigurationEntry.setIndexNames(
    (0, "LLDP-V2-MIB", "lldpV2RemTimeMark"),
    (0, "LLDP-V2-MIB", "lldpV2RemLocalIfIndex"),
    (0, "LLDP-V2-MIB", "lldpV2RemLocalDestMACAddress"),
    (0, "LLDP-V2-MIB", "lldpV2RemIndex"),
)
if mibBuilder.loadTexts:
    lldpXdot1dcbxRemETSBasicConfigurationEntry.setStatus("current")
_LldpXdot1dcbxRemETSConCreditBasedShaperSupport_Type = TruthValue
_LldpXdot1dcbxRemETSConCreditBasedShaperSupport_Object = MibTableColumn
lldpXdot1dcbxRemETSConCreditBasedShaperSupport = _LldpXdot1dcbxRemETSConCreditBasedShaperSupport_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 3, 1, 1, 1, 1),
    _LldpXdot1dcbxRemETSConCreditBasedShaperSupport_Type()
)
lldpXdot1dcbxRemETSConCreditBasedShaperSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot1dcbxRemETSConCreditBasedShaperSupport.setStatus("current")
_LldpXdot1dcbxRemETSConTrafficClassesSupported_Type = LldpXdot1dcbxSupportedCapacity
_LldpXdot1dcbxRemETSConTrafficClassesSupported_Object = MibTableColumn
lldpXdot1dcbxRemETSConTrafficClassesSupported = _LldpXdot1dcbxRemETSConTrafficClassesSupported_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 3, 1, 1, 1, 2),
    _LldpXdot1dcbxRemETSConTrafficClassesSupported_Type()
)
lldpXdot1dcbxRemETSConTrafficClassesSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot1dcbxRemETSConTrafficClassesSupported.setStatus("current")
_LldpXdot1dcbxRemETSConWilling_Type = TruthValue
_LldpXdot1dcbxRemETSConWilling_Object = MibTableColumn
lldpXdot1dcbxRemETSConWilling = _LldpXdot1dcbxRemETSConWilling_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 3, 1, 1, 1, 3),
    _LldpXdot1dcbxRemETSConWilling_Type()
)
lldpXdot1dcbxRemETSConWilling.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot1dcbxRemETSConWilling.setStatus("current")
_LldpXdot1dcbxRemETSConPriorityAssignmentTable_Object = MibTable
lldpXdot1dcbxRemETSConPriorityAssignmentTable = _LldpXdot1dcbxRemETSConPriorityAssignmentTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 3, 1, 2)
)
if mibBuilder.loadTexts:
    lldpXdot1dcbxRemETSConPriorityAssignmentTable.setStatus("current")
_LldpXdot1dcbxRemETSConPriorityAssignmentEntry_Object = MibTableRow
lldpXdot1dcbxRemETSConPriorityAssignmentEntry = _LldpXdot1dcbxRemETSConPriorityAssignmentEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 3, 1, 2, 1)
)
lldpXdot1dcbxRemETSConPriorityAssignmentEntry.setIndexNames(
    (0, "LLDP-V2-MIB", "lldpV2RemTimeMark"),
    (0, "LLDP-V2-MIB", "lldpV2RemLocalIfIndex"),
    (0, "LLDP-V2-MIB", "lldpV2RemLocalDestMACAddress"),
    (0, "LLDP-V2-MIB", "lldpV2RemIndex"),
    (0, "LLDP-EXT-DOT1-DCBX-MIB", "lldpXdot1dcbxRemETSConPriority"),
)
if mibBuilder.loadTexts:
    lldpXdot1dcbxRemETSConPriorityAssignmentEntry.setStatus("current")
_LldpXdot1dcbxRemETSConPriority_Type = IEEE8021PriorityValue
_LldpXdot1dcbxRemETSConPriority_Object = MibTableColumn
lldpXdot1dcbxRemETSConPriority = _LldpXdot1dcbxRemETSConPriority_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 3, 1, 2, 1, 1),
    _LldpXdot1dcbxRemETSConPriority_Type()
)
lldpXdot1dcbxRemETSConPriority.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lldpXdot1dcbxRemETSConPriority.setStatus("current")
_LldpXdot1dcbxRemETSConPriTrafficClass_Type = LldpXdot1dcbxTrafficClassValue
_LldpXdot1dcbxRemETSConPriTrafficClass_Object = MibTableColumn
lldpXdot1dcbxRemETSConPriTrafficClass = _LldpXdot1dcbxRemETSConPriTrafficClass_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 3, 1, 2, 1, 2),
    _LldpXdot1dcbxRemETSConPriTrafficClass_Type()
)
lldpXdot1dcbxRemETSConPriTrafficClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot1dcbxRemETSConPriTrafficClass.setStatus("current")
_LldpXdot1dcbxRemETSConTrafficClassBandwidthTable_Object = MibTable
lldpXdot1dcbxRemETSConTrafficClassBandwidthTable = _LldpXdot1dcbxRemETSConTrafficClassBandwidthTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 3, 1, 3)
)
if mibBuilder.loadTexts:
    lldpXdot1dcbxRemETSConTrafficClassBandwidthTable.setStatus("current")
_LldpXdot1dcbxRemETSConTrafficClassBandwidthEntry_Object = MibTableRow
lldpXdot1dcbxRemETSConTrafficClassBandwidthEntry = _LldpXdot1dcbxRemETSConTrafficClassBandwidthEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 3, 1, 3, 1)
)
lldpXdot1dcbxRemETSConTrafficClassBandwidthEntry.setIndexNames(
    (0, "LLDP-V2-MIB", "lldpV2RemTimeMark"),
    (0, "LLDP-V2-MIB", "lldpV2RemLocalIfIndex"),
    (0, "LLDP-V2-MIB", "lldpV2RemLocalDestMACAddress"),
    (0, "LLDP-V2-MIB", "lldpV2RemIndex"),
    (0, "LLDP-EXT-DOT1-DCBX-MIB", "lldpXdot1dcbxRemETSConTrafficClass"),
)
if mibBuilder.loadTexts:
    lldpXdot1dcbxRemETSConTrafficClassBandwidthEntry.setStatus("current")
_LldpXdot1dcbxRemETSConTrafficClass_Type = LldpXdot1dcbxTrafficClassValue
_LldpXdot1dcbxRemETSConTrafficClass_Object = MibTableColumn
lldpXdot1dcbxRemETSConTrafficClass = _LldpXdot1dcbxRemETSConTrafficClass_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 3, 1, 3, 1, 1),
    _LldpXdot1dcbxRemETSConTrafficClass_Type()
)
lldpXdot1dcbxRemETSConTrafficClass.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lldpXdot1dcbxRemETSConTrafficClass.setStatus("current")
_LldpXdot1dcbxRemETSConTrafficClassBandwidth_Type = LldpXdot1dcbxTrafficClassBandwidthValue
_LldpXdot1dcbxRemETSConTrafficClassBandwidth_Object = MibTableColumn
lldpXdot1dcbxRemETSConTrafficClassBandwidth = _LldpXdot1dcbxRemETSConTrafficClassBandwidth_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 3, 1, 3, 1, 2),
    _LldpXdot1dcbxRemETSConTrafficClassBandwidth_Type()
)
lldpXdot1dcbxRemETSConTrafficClassBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot1dcbxRemETSConTrafficClassBandwidth.setStatus("current")
_LldpXdot1dcbxRemETSConTrafficSelectionAlgorithmTable_Object = MibTable
lldpXdot1dcbxRemETSConTrafficSelectionAlgorithmTable = _LldpXdot1dcbxRemETSConTrafficSelectionAlgorithmTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 3, 1, 4)
)
if mibBuilder.loadTexts:
    lldpXdot1dcbxRemETSConTrafficSelectionAlgorithmTable.setStatus("current")
_LldpXdot1dcbxRemETSConTrafficSelectionAlgorithmEntry_Object = MibTableRow
lldpXdot1dcbxRemETSConTrafficSelectionAlgorithmEntry = _LldpXdot1dcbxRemETSConTrafficSelectionAlgorithmEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 3, 1, 4, 1)
)
lldpXdot1dcbxRemETSConTrafficSelectionAlgorithmEntry.setIndexNames(
    (0, "LLDP-V2-MIB", "lldpV2RemTimeMark"),
    (0, "LLDP-V2-MIB", "lldpV2RemLocalIfIndex"),
    (0, "LLDP-V2-MIB", "lldpV2RemLocalDestMACAddress"),
    (0, "LLDP-V2-MIB", "lldpV2RemIndex"),
    (0, "LLDP-EXT-DOT1-DCBX-MIB", "lldpXdot1dcbxRemETSConTSATrafficClass"),
)
if mibBuilder.loadTexts:
    lldpXdot1dcbxRemETSConTrafficSelectionAlgorithmEntry.setStatus("current")
_LldpXdot1dcbxRemETSConTSATrafficClass_Type = LldpXdot1dcbxTrafficClassValue
_LldpXdot1dcbxRemETSConTSATrafficClass_Object = MibTableColumn
lldpXdot1dcbxRemETSConTSATrafficClass = _LldpXdot1dcbxRemETSConTSATrafficClass_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 3, 1, 4, 1, 1),
    _LldpXdot1dcbxRemETSConTSATrafficClass_Type()
)
lldpXdot1dcbxRemETSConTSATrafficClass.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lldpXdot1dcbxRemETSConTSATrafficClass.setStatus("current")
_LldpXdot1dcbxRemETSConTrafficSelectionAlgorithm_Type = LldpXdot1dcbxTrafficSelectionAlgorithm
_LldpXdot1dcbxRemETSConTrafficSelectionAlgorithm_Object = MibTableColumn
lldpXdot1dcbxRemETSConTrafficSelectionAlgorithm = _LldpXdot1dcbxRemETSConTrafficSelectionAlgorithm_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 3, 1, 4, 1, 2),
    _LldpXdot1dcbxRemETSConTrafficSelectionAlgorithm_Type()
)
lldpXdot1dcbxRemETSConTrafficSelectionAlgorithm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot1dcbxRemETSConTrafficSelectionAlgorithm.setStatus("current")
_LldpXdot1dcbxRemETSReco_ObjectIdentity = ObjectIdentity
lldpXdot1dcbxRemETSReco = _LldpXdot1dcbxRemETSReco_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 3, 2)
)
_LldpXdot1dcbxRemETSRecoTrafficClassBandwidthTable_Object = MibTable
lldpXdot1dcbxRemETSRecoTrafficClassBandwidthTable = _LldpXdot1dcbxRemETSRecoTrafficClassBandwidthTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 3, 2, 1)
)
if mibBuilder.loadTexts:
    lldpXdot1dcbxRemETSRecoTrafficClassBandwidthTable.setStatus("current")
_LldpXdot1dcbxRemETSRecoTrafficClassBandwidthEntry_Object = MibTableRow
lldpXdot1dcbxRemETSRecoTrafficClassBandwidthEntry = _LldpXdot1dcbxRemETSRecoTrafficClassBandwidthEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 3, 2, 1, 1)
)
lldpXdot1dcbxRemETSRecoTrafficClassBandwidthEntry.setIndexNames(
    (0, "LLDP-V2-MIB", "lldpV2RemTimeMark"),
    (0, "LLDP-V2-MIB", "lldpV2RemLocalIfIndex"),
    (0, "LLDP-V2-MIB", "lldpV2RemLocalDestMACAddress"),
    (0, "LLDP-V2-MIB", "lldpV2RemIndex"),
    (0, "LLDP-EXT-DOT1-DCBX-MIB", "lldpXdot1dcbxRemETSRecoTrafficClass"),
)
if mibBuilder.loadTexts:
    lldpXdot1dcbxRemETSRecoTrafficClassBandwidthEntry.setStatus("current")
_LldpXdot1dcbxRemETSRecoTrafficClass_Type = LldpXdot1dcbxTrafficClassValue
_LldpXdot1dcbxRemETSRecoTrafficClass_Object = MibTableColumn
lldpXdot1dcbxRemETSRecoTrafficClass = _LldpXdot1dcbxRemETSRecoTrafficClass_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 3, 2, 1, 1, 1),
    _LldpXdot1dcbxRemETSRecoTrafficClass_Type()
)
lldpXdot1dcbxRemETSRecoTrafficClass.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lldpXdot1dcbxRemETSRecoTrafficClass.setStatus("current")
_LldpXdot1dcbxRemETSRecoTrafficClassBandwidth_Type = LldpXdot1dcbxTrafficClassBandwidthValue
_LldpXdot1dcbxRemETSRecoTrafficClassBandwidth_Object = MibTableColumn
lldpXdot1dcbxRemETSRecoTrafficClassBandwidth = _LldpXdot1dcbxRemETSRecoTrafficClassBandwidth_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 3, 2, 1, 1, 2),
    _LldpXdot1dcbxRemETSRecoTrafficClassBandwidth_Type()
)
lldpXdot1dcbxRemETSRecoTrafficClassBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot1dcbxRemETSRecoTrafficClassBandwidth.setStatus("current")
_LldpXdot1dcbxRemETSRecoTrafficSelectionAlgorithmTable_Object = MibTable
lldpXdot1dcbxRemETSRecoTrafficSelectionAlgorithmTable = _LldpXdot1dcbxRemETSRecoTrafficSelectionAlgorithmTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 3, 2, 2)
)
if mibBuilder.loadTexts:
    lldpXdot1dcbxRemETSRecoTrafficSelectionAlgorithmTable.setStatus("current")
_LldpXdot1dcbxRemETSRecoTrafficSelectionAlgorithmEntry_Object = MibTableRow
lldpXdot1dcbxRemETSRecoTrafficSelectionAlgorithmEntry = _LldpXdot1dcbxRemETSRecoTrafficSelectionAlgorithmEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 3, 2, 2, 1)
)
lldpXdot1dcbxRemETSRecoTrafficSelectionAlgorithmEntry.setIndexNames(
    (0, "LLDP-V2-MIB", "lldpV2RemTimeMark"),
    (0, "LLDP-V2-MIB", "lldpV2RemLocalIfIndex"),
    (0, "LLDP-V2-MIB", "lldpV2RemLocalDestMACAddress"),
    (0, "LLDP-V2-MIB", "lldpV2RemIndex"),
    (0, "LLDP-EXT-DOT1-DCBX-MIB", "lldpXdot1dcbxRemETSRecoTSATrafficClass"),
)
if mibBuilder.loadTexts:
    lldpXdot1dcbxRemETSRecoTrafficSelectionAlgorithmEntry.setStatus("current")
_LldpXdot1dcbxRemETSRecoTSATrafficClass_Type = LldpXdot1dcbxTrafficClassValue
_LldpXdot1dcbxRemETSRecoTSATrafficClass_Object = MibTableColumn
lldpXdot1dcbxRemETSRecoTSATrafficClass = _LldpXdot1dcbxRemETSRecoTSATrafficClass_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 3, 2, 2, 1, 1),
    _LldpXdot1dcbxRemETSRecoTSATrafficClass_Type()
)
lldpXdot1dcbxRemETSRecoTSATrafficClass.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lldpXdot1dcbxRemETSRecoTSATrafficClass.setStatus("current")
_LldpXdot1dcbxRemETSRecoTrafficSelectionAlgorithm_Type = LldpXdot1dcbxTrafficSelectionAlgorithm
_LldpXdot1dcbxRemETSRecoTrafficSelectionAlgorithm_Object = MibTableColumn
lldpXdot1dcbxRemETSRecoTrafficSelectionAlgorithm = _LldpXdot1dcbxRemETSRecoTrafficSelectionAlgorithm_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 3, 2, 2, 1, 2),
    _LldpXdot1dcbxRemETSRecoTrafficSelectionAlgorithm_Type()
)
lldpXdot1dcbxRemETSRecoTrafficSelectionAlgorithm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot1dcbxRemETSRecoTrafficSelectionAlgorithm.setStatus("current")
_LldpXdot1dcbxRemPFC_ObjectIdentity = ObjectIdentity
lldpXdot1dcbxRemPFC = _LldpXdot1dcbxRemPFC_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 3, 3)
)
_LldpXdot1dcbxRemPFCBasicTable_Object = MibTable
lldpXdot1dcbxRemPFCBasicTable = _LldpXdot1dcbxRemPFCBasicTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 3, 3, 1)
)
if mibBuilder.loadTexts:
    lldpXdot1dcbxRemPFCBasicTable.setStatus("current")
_LldpXdot1dcbxRemPFCBasicEntry_Object = MibTableRow
lldpXdot1dcbxRemPFCBasicEntry = _LldpXdot1dcbxRemPFCBasicEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 3, 3, 1, 1)
)
lldpXdot1dcbxRemPFCBasicEntry.setIndexNames(
    (0, "LLDP-V2-MIB", "lldpV2RemTimeMark"),
    (0, "LLDP-V2-MIB", "lldpV2RemLocalIfIndex"),
    (0, "LLDP-V2-MIB", "lldpV2RemLocalDestMACAddress"),
    (0, "LLDP-V2-MIB", "lldpV2RemIndex"),
)
if mibBuilder.loadTexts:
    lldpXdot1dcbxRemPFCBasicEntry.setStatus("current")
_LldpXdot1dcbxRemPFCWilling_Type = TruthValue
_LldpXdot1dcbxRemPFCWilling_Object = MibTableColumn
lldpXdot1dcbxRemPFCWilling = _LldpXdot1dcbxRemPFCWilling_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 3, 3, 1, 1, 1),
    _LldpXdot1dcbxRemPFCWilling_Type()
)
lldpXdot1dcbxRemPFCWilling.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot1dcbxRemPFCWilling.setStatus("current")
_LldpXdot1dcbxRemPFCMBC_Type = TruthValue
_LldpXdot1dcbxRemPFCMBC_Object = MibTableColumn
lldpXdot1dcbxRemPFCMBC = _LldpXdot1dcbxRemPFCMBC_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 3, 3, 1, 1, 2),
    _LldpXdot1dcbxRemPFCMBC_Type()
)
lldpXdot1dcbxRemPFCMBC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot1dcbxRemPFCMBC.setStatus("current")
_LldpXdot1dcbxRemPFCCap_Type = LldpXdot1dcbxSupportedCapacity
_LldpXdot1dcbxRemPFCCap_Object = MibTableColumn
lldpXdot1dcbxRemPFCCap = _LldpXdot1dcbxRemPFCCap_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 3, 3, 1, 1, 3),
    _LldpXdot1dcbxRemPFCCap_Type()
)
lldpXdot1dcbxRemPFCCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot1dcbxRemPFCCap.setStatus("current")
_LldpXdot1dcbxRemPFCEnableTable_Object = MibTable
lldpXdot1dcbxRemPFCEnableTable = _LldpXdot1dcbxRemPFCEnableTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 3, 3, 2)
)
if mibBuilder.loadTexts:
    lldpXdot1dcbxRemPFCEnableTable.setStatus("current")
_LldpXdot1dcbxRemPFCEnableEntry_Object = MibTableRow
lldpXdot1dcbxRemPFCEnableEntry = _LldpXdot1dcbxRemPFCEnableEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 3, 3, 2, 1)
)
lldpXdot1dcbxRemPFCEnableEntry.setIndexNames(
    (0, "LLDP-V2-MIB", "lldpV2RemTimeMark"),
    (0, "LLDP-V2-MIB", "lldpV2RemLocalIfIndex"),
    (0, "LLDP-V2-MIB", "lldpV2RemLocalDestMACAddress"),
    (0, "LLDP-V2-MIB", "lldpV2RemIndex"),
    (0, "LLDP-EXT-DOT1-DCBX-MIB", "lldpXdot1dcbxRemPFCEnablePriority"),
)
if mibBuilder.loadTexts:
    lldpXdot1dcbxRemPFCEnableEntry.setStatus("current")
_LldpXdot1dcbxRemPFCEnablePriority_Type = IEEE8021PriorityValue
_LldpXdot1dcbxRemPFCEnablePriority_Object = MibTableColumn
lldpXdot1dcbxRemPFCEnablePriority = _LldpXdot1dcbxRemPFCEnablePriority_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 3, 3, 2, 1, 1),
    _LldpXdot1dcbxRemPFCEnablePriority_Type()
)
lldpXdot1dcbxRemPFCEnablePriority.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lldpXdot1dcbxRemPFCEnablePriority.setStatus("current")
_LldpXdot1dcbxRemPFCEnableEnabled_Type = TruthValue
_LldpXdot1dcbxRemPFCEnableEnabled_Object = MibTableColumn
lldpXdot1dcbxRemPFCEnableEnabled = _LldpXdot1dcbxRemPFCEnableEnabled_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 3, 3, 2, 1, 2),
    _LldpXdot1dcbxRemPFCEnableEnabled_Type()
)
lldpXdot1dcbxRemPFCEnableEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot1dcbxRemPFCEnableEnabled.setStatus("current")
_LldpXdot1dcbxRemApplicationPriorityAppTable_Object = MibTable
lldpXdot1dcbxRemApplicationPriorityAppTable = _LldpXdot1dcbxRemApplicationPriorityAppTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 3, 4)
)
if mibBuilder.loadTexts:
    lldpXdot1dcbxRemApplicationPriorityAppTable.setStatus("current")
_LldpXdot1dcbxRemApplicationPriorityAppEntry_Object = MibTableRow
lldpXdot1dcbxRemApplicationPriorityAppEntry = _LldpXdot1dcbxRemApplicationPriorityAppEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 3, 4, 1)
)
lldpXdot1dcbxRemApplicationPriorityAppEntry.setIndexNames(
    (0, "LLDP-V2-MIB", "lldpV2RemTimeMark"),
    (0, "LLDP-V2-MIB", "lldpV2RemLocalIfIndex"),
    (0, "LLDP-V2-MIB", "lldpV2RemLocalDestMACAddress"),
    (0, "LLDP-V2-MIB", "lldpV2RemIndex"),
    (0, "LLDP-EXT-DOT1-DCBX-MIB", "lldpXdot1dcbxRemApplicationPriorityAESelector"),
    (0, "LLDP-EXT-DOT1-DCBX-MIB", "lldpXdot1dcbxRemApplicationPriorityAEProtocol"),
)
if mibBuilder.loadTexts:
    lldpXdot1dcbxRemApplicationPriorityAppEntry.setStatus("current")
_LldpXdot1dcbxRemApplicationPriorityAESelector_Type = LldpXdot1dcbxAppSelector
_LldpXdot1dcbxRemApplicationPriorityAESelector_Object = MibTableColumn
lldpXdot1dcbxRemApplicationPriorityAESelector = _LldpXdot1dcbxRemApplicationPriorityAESelector_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 3, 4, 1, 1),
    _LldpXdot1dcbxRemApplicationPriorityAESelector_Type()
)
lldpXdot1dcbxRemApplicationPriorityAESelector.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lldpXdot1dcbxRemApplicationPriorityAESelector.setStatus("current")
_LldpXdot1dcbxRemApplicationPriorityAEProtocol_Type = LldpXdot1dcbxAppProtocol
_LldpXdot1dcbxRemApplicationPriorityAEProtocol_Object = MibTableColumn
lldpXdot1dcbxRemApplicationPriorityAEProtocol = _LldpXdot1dcbxRemApplicationPriorityAEProtocol_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 3, 4, 1, 2),
    _LldpXdot1dcbxRemApplicationPriorityAEProtocol_Type()
)
lldpXdot1dcbxRemApplicationPriorityAEProtocol.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lldpXdot1dcbxRemApplicationPriorityAEProtocol.setStatus("current")
_LldpXdot1dcbxRemApplicationPriorityAEPriority_Type = IEEE8021PriorityValue
_LldpXdot1dcbxRemApplicationPriorityAEPriority_Object = MibTableColumn
lldpXdot1dcbxRemApplicationPriorityAEPriority = _LldpXdot1dcbxRemApplicationPriorityAEPriority_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 3, 4, 1, 3),
    _LldpXdot1dcbxRemApplicationPriorityAEPriority_Type()
)
lldpXdot1dcbxRemApplicationPriorityAEPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot1dcbxRemApplicationPriorityAEPriority.setStatus("current")
_LldpXdot1dcbxAdminData_ObjectIdentity = ObjectIdentity
lldpXdot1dcbxAdminData = _LldpXdot1dcbxAdminData_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 4)
)
_LldpXdot1dcbxAdminETSConfiguration_ObjectIdentity = ObjectIdentity
lldpXdot1dcbxAdminETSConfiguration = _LldpXdot1dcbxAdminETSConfiguration_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 4, 1)
)
_LldpXdot1dcbxAdminETSBasicConfigurationTable_Object = MibTable
lldpXdot1dcbxAdminETSBasicConfigurationTable = _LldpXdot1dcbxAdminETSBasicConfigurationTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 4, 1, 1)
)
if mibBuilder.loadTexts:
    lldpXdot1dcbxAdminETSBasicConfigurationTable.setStatus("current")
_LldpXdot1dcbxAdminETSBasicConfigurationEntry_Object = MibTableRow
lldpXdot1dcbxAdminETSBasicConfigurationEntry = _LldpXdot1dcbxAdminETSBasicConfigurationEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 4, 1, 1, 1)
)
lldpXdot1dcbxAdminETSBasicConfigurationEntry.setIndexNames(
    (0, "LLDP-V2-MIB", "lldpV2LocPortIfIndex"),
)
if mibBuilder.loadTexts:
    lldpXdot1dcbxAdminETSBasicConfigurationEntry.setStatus("current")
_LldpXdot1dcbxAdminETSConCreditBasedShaperSupport_Type = TruthValue
_LldpXdot1dcbxAdminETSConCreditBasedShaperSupport_Object = MibTableColumn
lldpXdot1dcbxAdminETSConCreditBasedShaperSupport = _LldpXdot1dcbxAdminETSConCreditBasedShaperSupport_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 4, 1, 1, 1, 1),
    _LldpXdot1dcbxAdminETSConCreditBasedShaperSupport_Type()
)
lldpXdot1dcbxAdminETSConCreditBasedShaperSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot1dcbxAdminETSConCreditBasedShaperSupport.setStatus("current")
_LldpXdot1dcbxAdminETSConTrafficClassesSupported_Type = LldpXdot1dcbxSupportedCapacity
_LldpXdot1dcbxAdminETSConTrafficClassesSupported_Object = MibTableColumn
lldpXdot1dcbxAdminETSConTrafficClassesSupported = _LldpXdot1dcbxAdminETSConTrafficClassesSupported_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 4, 1, 1, 1, 2),
    _LldpXdot1dcbxAdminETSConTrafficClassesSupported_Type()
)
lldpXdot1dcbxAdminETSConTrafficClassesSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot1dcbxAdminETSConTrafficClassesSupported.setStatus("current")


class _LldpXdot1dcbxAdminETSConWilling_Type(TruthValue):
    """Custom type lldpXdot1dcbxAdminETSConWilling based on TruthValue"""
    defaultValue = 2


_LldpXdot1dcbxAdminETSConWilling_Type.__name__ = "TruthValue"
_LldpXdot1dcbxAdminETSConWilling_Object = MibTableColumn
lldpXdot1dcbxAdminETSConWilling = _LldpXdot1dcbxAdminETSConWilling_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 4, 1, 1, 1, 3),
    _LldpXdot1dcbxAdminETSConWilling_Type()
)
lldpXdot1dcbxAdminETSConWilling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpXdot1dcbxAdminETSConWilling.setStatus("current")
_LldpXdot1dcbxAdminETSConPriorityAssignmentTable_Object = MibTable
lldpXdot1dcbxAdminETSConPriorityAssignmentTable = _LldpXdot1dcbxAdminETSConPriorityAssignmentTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 4, 1, 2)
)
if mibBuilder.loadTexts:
    lldpXdot1dcbxAdminETSConPriorityAssignmentTable.setStatus("current")
_LldpXdot1dcbxAdminETSConPriorityAssignmentEntry_Object = MibTableRow
lldpXdot1dcbxAdminETSConPriorityAssignmentEntry = _LldpXdot1dcbxAdminETSConPriorityAssignmentEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 4, 1, 2, 1)
)
lldpXdot1dcbxAdminETSConPriorityAssignmentEntry.setIndexNames(
    (0, "LLDP-V2-MIB", "lldpV2LocPortIfIndex"),
    (0, "LLDP-EXT-DOT1-DCBX-MIB", "lldpXdot1dcbxAdminETSConPriority"),
)
if mibBuilder.loadTexts:
    lldpXdot1dcbxAdminETSConPriorityAssignmentEntry.setStatus("current")
_LldpXdot1dcbxAdminETSConPriority_Type = IEEE8021PriorityValue
_LldpXdot1dcbxAdminETSConPriority_Object = MibTableColumn
lldpXdot1dcbxAdminETSConPriority = _LldpXdot1dcbxAdminETSConPriority_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 4, 1, 2, 1, 1),
    _LldpXdot1dcbxAdminETSConPriority_Type()
)
lldpXdot1dcbxAdminETSConPriority.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lldpXdot1dcbxAdminETSConPriority.setStatus("current")


class _LldpXdot1dcbxAdminETSConPriTrafficClass_Type(LldpXdot1dcbxTrafficClassValue):
    """Custom type lldpXdot1dcbxAdminETSConPriTrafficClass based on LldpXdot1dcbxTrafficClassValue"""
    defaultValue = 0


_LldpXdot1dcbxAdminETSConPriTrafficClass_Type.__name__ = "LldpXdot1dcbxTrafficClassValue"
_LldpXdot1dcbxAdminETSConPriTrafficClass_Object = MibTableColumn
lldpXdot1dcbxAdminETSConPriTrafficClass = _LldpXdot1dcbxAdminETSConPriTrafficClass_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 4, 1, 2, 1, 2),
    _LldpXdot1dcbxAdminETSConPriTrafficClass_Type()
)
lldpXdot1dcbxAdminETSConPriTrafficClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpXdot1dcbxAdminETSConPriTrafficClass.setStatus("current")
_LldpXdot1dcbxAdminETSConTrafficClassBandwidthTable_Object = MibTable
lldpXdot1dcbxAdminETSConTrafficClassBandwidthTable = _LldpXdot1dcbxAdminETSConTrafficClassBandwidthTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 4, 1, 3)
)
if mibBuilder.loadTexts:
    lldpXdot1dcbxAdminETSConTrafficClassBandwidthTable.setStatus("current")
_LldpXdot1dcbxAdminETSConTrafficClassBandwidthEntry_Object = MibTableRow
lldpXdot1dcbxAdminETSConTrafficClassBandwidthEntry = _LldpXdot1dcbxAdminETSConTrafficClassBandwidthEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 4, 1, 3, 1)
)
lldpXdot1dcbxAdminETSConTrafficClassBandwidthEntry.setIndexNames(
    (0, "LLDP-V2-MIB", "lldpV2LocPortIfIndex"),
    (0, "LLDP-EXT-DOT1-DCBX-MIB", "lldpXdot1dcbxAdminETSConTrafficClass"),
)
if mibBuilder.loadTexts:
    lldpXdot1dcbxAdminETSConTrafficClassBandwidthEntry.setStatus("current")
_LldpXdot1dcbxAdminETSConTrafficClass_Type = LldpXdot1dcbxTrafficClassValue
_LldpXdot1dcbxAdminETSConTrafficClass_Object = MibTableColumn
lldpXdot1dcbxAdminETSConTrafficClass = _LldpXdot1dcbxAdminETSConTrafficClass_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 4, 1, 3, 1, 1),
    _LldpXdot1dcbxAdminETSConTrafficClass_Type()
)
lldpXdot1dcbxAdminETSConTrafficClass.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lldpXdot1dcbxAdminETSConTrafficClass.setStatus("current")
_LldpXdot1dcbxAdminETSConTrafficClassBandwidth_Type = LldpXdot1dcbxTrafficClassBandwidthValue
_LldpXdot1dcbxAdminETSConTrafficClassBandwidth_Object = MibTableColumn
lldpXdot1dcbxAdminETSConTrafficClassBandwidth = _LldpXdot1dcbxAdminETSConTrafficClassBandwidth_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 4, 1, 3, 1, 2),
    _LldpXdot1dcbxAdminETSConTrafficClassBandwidth_Type()
)
lldpXdot1dcbxAdminETSConTrafficClassBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpXdot1dcbxAdminETSConTrafficClassBandwidth.setStatus("current")
_LldpXdot1dcbxAdminETSConTrafficSelectionAlgorithmTable_Object = MibTable
lldpXdot1dcbxAdminETSConTrafficSelectionAlgorithmTable = _LldpXdot1dcbxAdminETSConTrafficSelectionAlgorithmTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 4, 1, 4)
)
if mibBuilder.loadTexts:
    lldpXdot1dcbxAdminETSConTrafficSelectionAlgorithmTable.setStatus("current")
_LldpXdot1dcbxAdminETSConTrafficSelectionAlgorithmEntry_Object = MibTableRow
lldpXdot1dcbxAdminETSConTrafficSelectionAlgorithmEntry = _LldpXdot1dcbxAdminETSConTrafficSelectionAlgorithmEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 4, 1, 4, 1)
)
lldpXdot1dcbxAdminETSConTrafficSelectionAlgorithmEntry.setIndexNames(
    (0, "LLDP-V2-MIB", "lldpV2LocPortIfIndex"),
    (0, "LLDP-EXT-DOT1-DCBX-MIB", "lldpXdot1dcbxAdminETSConTSATrafficClass"),
)
if mibBuilder.loadTexts:
    lldpXdot1dcbxAdminETSConTrafficSelectionAlgorithmEntry.setStatus("current")
_LldpXdot1dcbxAdminETSConTSATrafficClass_Type = LldpXdot1dcbxTrafficClassValue
_LldpXdot1dcbxAdminETSConTSATrafficClass_Object = MibTableColumn
lldpXdot1dcbxAdminETSConTSATrafficClass = _LldpXdot1dcbxAdminETSConTSATrafficClass_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 4, 1, 4, 1, 1),
    _LldpXdot1dcbxAdminETSConTSATrafficClass_Type()
)
lldpXdot1dcbxAdminETSConTSATrafficClass.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lldpXdot1dcbxAdminETSConTSATrafficClass.setStatus("current")
_LldpXdot1dcbxAdminETSConTrafficSelectionAlgorithm_Type = LldpXdot1dcbxTrafficSelectionAlgorithm
_LldpXdot1dcbxAdminETSConTrafficSelectionAlgorithm_Object = MibTableColumn
lldpXdot1dcbxAdminETSConTrafficSelectionAlgorithm = _LldpXdot1dcbxAdminETSConTrafficSelectionAlgorithm_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 4, 1, 4, 1, 2),
    _LldpXdot1dcbxAdminETSConTrafficSelectionAlgorithm_Type()
)
lldpXdot1dcbxAdminETSConTrafficSelectionAlgorithm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpXdot1dcbxAdminETSConTrafficSelectionAlgorithm.setStatus("current")
_LldpXdot1dcbxAdminETSReco_ObjectIdentity = ObjectIdentity
lldpXdot1dcbxAdminETSReco = _LldpXdot1dcbxAdminETSReco_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 4, 2)
)
_LldpXdot1dcbxAdminETSRecoTrafficClassBandwidthTable_Object = MibTable
lldpXdot1dcbxAdminETSRecoTrafficClassBandwidthTable = _LldpXdot1dcbxAdminETSRecoTrafficClassBandwidthTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 4, 2, 1)
)
if mibBuilder.loadTexts:
    lldpXdot1dcbxAdminETSRecoTrafficClassBandwidthTable.setStatus("current")
_LldpXdot1dcbxAdminETSRecoTrafficClassBandwidthEntry_Object = MibTableRow
lldpXdot1dcbxAdminETSRecoTrafficClassBandwidthEntry = _LldpXdot1dcbxAdminETSRecoTrafficClassBandwidthEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 4, 2, 1, 1)
)
lldpXdot1dcbxAdminETSRecoTrafficClassBandwidthEntry.setIndexNames(
    (0, "LLDP-V2-MIB", "lldpV2LocPortIfIndex"),
    (0, "LLDP-EXT-DOT1-DCBX-MIB", "lldpXdot1dcbxAdminETSRecoTrafficClass"),
)
if mibBuilder.loadTexts:
    lldpXdot1dcbxAdminETSRecoTrafficClassBandwidthEntry.setStatus("current")
_LldpXdot1dcbxAdminETSRecoTrafficClass_Type = LldpXdot1dcbxTrafficClassValue
_LldpXdot1dcbxAdminETSRecoTrafficClass_Object = MibTableColumn
lldpXdot1dcbxAdminETSRecoTrafficClass = _LldpXdot1dcbxAdminETSRecoTrafficClass_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 4, 2, 1, 1, 1),
    _LldpXdot1dcbxAdminETSRecoTrafficClass_Type()
)
lldpXdot1dcbxAdminETSRecoTrafficClass.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lldpXdot1dcbxAdminETSRecoTrafficClass.setStatus("current")
_LldpXdot1dcbxAdminETSRecoTrafficClassBandwidth_Type = LldpXdot1dcbxTrafficClassBandwidthValue
_LldpXdot1dcbxAdminETSRecoTrafficClassBandwidth_Object = MibTableColumn
lldpXdot1dcbxAdminETSRecoTrafficClassBandwidth = _LldpXdot1dcbxAdminETSRecoTrafficClassBandwidth_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 4, 2, 1, 1, 2),
    _LldpXdot1dcbxAdminETSRecoTrafficClassBandwidth_Type()
)
lldpXdot1dcbxAdminETSRecoTrafficClassBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpXdot1dcbxAdminETSRecoTrafficClassBandwidth.setStatus("current")
_LldpXdot1dcbxAdminETSRecoTrafficSelectionAlgorithmTable_Object = MibTable
lldpXdot1dcbxAdminETSRecoTrafficSelectionAlgorithmTable = _LldpXdot1dcbxAdminETSRecoTrafficSelectionAlgorithmTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 4, 2, 2)
)
if mibBuilder.loadTexts:
    lldpXdot1dcbxAdminETSRecoTrafficSelectionAlgorithmTable.setStatus("current")
_LldpXdot1dcbxAdminETSRecoTrafficSelectionAlgorithmEntry_Object = MibTableRow
lldpXdot1dcbxAdminETSRecoTrafficSelectionAlgorithmEntry = _LldpXdot1dcbxAdminETSRecoTrafficSelectionAlgorithmEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 4, 2, 2, 1)
)
lldpXdot1dcbxAdminETSRecoTrafficSelectionAlgorithmEntry.setIndexNames(
    (0, "LLDP-V2-MIB", "lldpV2LocPortIfIndex"),
    (0, "LLDP-EXT-DOT1-DCBX-MIB", "lldpXdot1dcbxAdminETSRecoTSATrafficClass"),
)
if mibBuilder.loadTexts:
    lldpXdot1dcbxAdminETSRecoTrafficSelectionAlgorithmEntry.setStatus("current")
_LldpXdot1dcbxAdminETSRecoTSATrafficClass_Type = LldpXdot1dcbxTrafficClassValue
_LldpXdot1dcbxAdminETSRecoTSATrafficClass_Object = MibTableColumn
lldpXdot1dcbxAdminETSRecoTSATrafficClass = _LldpXdot1dcbxAdminETSRecoTSATrafficClass_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 4, 2, 2, 1, 1),
    _LldpXdot1dcbxAdminETSRecoTSATrafficClass_Type()
)
lldpXdot1dcbxAdminETSRecoTSATrafficClass.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lldpXdot1dcbxAdminETSRecoTSATrafficClass.setStatus("current")
_LldpXdot1dcbxAdminETSRecoTrafficSelectionAlgorithm_Type = LldpXdot1dcbxTrafficSelectionAlgorithm
_LldpXdot1dcbxAdminETSRecoTrafficSelectionAlgorithm_Object = MibTableColumn
lldpXdot1dcbxAdminETSRecoTrafficSelectionAlgorithm = _LldpXdot1dcbxAdminETSRecoTrafficSelectionAlgorithm_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 4, 2, 2, 1, 2),
    _LldpXdot1dcbxAdminETSRecoTrafficSelectionAlgorithm_Type()
)
lldpXdot1dcbxAdminETSRecoTrafficSelectionAlgorithm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpXdot1dcbxAdminETSRecoTrafficSelectionAlgorithm.setStatus("current")
_LldpXdot1dcbxAdminPFC_ObjectIdentity = ObjectIdentity
lldpXdot1dcbxAdminPFC = _LldpXdot1dcbxAdminPFC_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 4, 3)
)
_LldpXdot1dcbxAdminPFCBasicTable_Object = MibTable
lldpXdot1dcbxAdminPFCBasicTable = _LldpXdot1dcbxAdminPFCBasicTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 4, 3, 1)
)
if mibBuilder.loadTexts:
    lldpXdot1dcbxAdminPFCBasicTable.setStatus("current")
_LldpXdot1dcbxAdminPFCBasicEntry_Object = MibTableRow
lldpXdot1dcbxAdminPFCBasicEntry = _LldpXdot1dcbxAdminPFCBasicEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 4, 3, 1, 1)
)
lldpXdot1dcbxAdminPFCBasicEntry.setIndexNames(
    (0, "LLDP-V2-MIB", "lldpV2LocPortIfIndex"),
)
if mibBuilder.loadTexts:
    lldpXdot1dcbxAdminPFCBasicEntry.setStatus("current")


class _LldpXdot1dcbxAdminPFCWilling_Type(TruthValue):
    """Custom type lldpXdot1dcbxAdminPFCWilling based on TruthValue"""
    defaultValue = 2


_LldpXdot1dcbxAdminPFCWilling_Type.__name__ = "TruthValue"
_LldpXdot1dcbxAdminPFCWilling_Object = MibTableColumn
lldpXdot1dcbxAdminPFCWilling = _LldpXdot1dcbxAdminPFCWilling_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 4, 3, 1, 1, 1),
    _LldpXdot1dcbxAdminPFCWilling_Type()
)
lldpXdot1dcbxAdminPFCWilling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpXdot1dcbxAdminPFCWilling.setStatus("current")
_LldpXdot1dcbxAdminPFCMBC_Type = TruthValue
_LldpXdot1dcbxAdminPFCMBC_Object = MibTableColumn
lldpXdot1dcbxAdminPFCMBC = _LldpXdot1dcbxAdminPFCMBC_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 4, 3, 1, 1, 2),
    _LldpXdot1dcbxAdminPFCMBC_Type()
)
lldpXdot1dcbxAdminPFCMBC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot1dcbxAdminPFCMBC.setStatus("current")
_LldpXdot1dcbxAdminPFCCap_Type = LldpXdot1dcbxSupportedCapacity
_LldpXdot1dcbxAdminPFCCap_Object = MibTableColumn
lldpXdot1dcbxAdminPFCCap = _LldpXdot1dcbxAdminPFCCap_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 4, 3, 1, 1, 3),
    _LldpXdot1dcbxAdminPFCCap_Type()
)
lldpXdot1dcbxAdminPFCCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpXdot1dcbxAdminPFCCap.setStatus("current")
_LldpXdot1dcbxAdminPFCEnableTable_Object = MibTable
lldpXdot1dcbxAdminPFCEnableTable = _LldpXdot1dcbxAdminPFCEnableTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 4, 3, 2)
)
if mibBuilder.loadTexts:
    lldpXdot1dcbxAdminPFCEnableTable.setStatus("current")
_LldpXdot1dcbxAdminPFCEnableEntry_Object = MibTableRow
lldpXdot1dcbxAdminPFCEnableEntry = _LldpXdot1dcbxAdminPFCEnableEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 4, 3, 2, 1)
)
lldpXdot1dcbxAdminPFCEnableEntry.setIndexNames(
    (0, "LLDP-V2-MIB", "lldpV2LocPortIfIndex"),
    (0, "LLDP-EXT-DOT1-DCBX-MIB", "lldpXdot1dcbxAdminPFCEnablePriority"),
)
if mibBuilder.loadTexts:
    lldpXdot1dcbxAdminPFCEnableEntry.setStatus("current")
_LldpXdot1dcbxAdminPFCEnablePriority_Type = IEEE8021PriorityValue
_LldpXdot1dcbxAdminPFCEnablePriority_Object = MibTableColumn
lldpXdot1dcbxAdminPFCEnablePriority = _LldpXdot1dcbxAdminPFCEnablePriority_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 4, 3, 2, 1, 1),
    _LldpXdot1dcbxAdminPFCEnablePriority_Type()
)
lldpXdot1dcbxAdminPFCEnablePriority.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lldpXdot1dcbxAdminPFCEnablePriority.setStatus("current")


class _LldpXdot1dcbxAdminPFCEnableEnabled_Type(TruthValue):
    """Custom type lldpXdot1dcbxAdminPFCEnableEnabled based on TruthValue"""
    defaultValue = 2


_LldpXdot1dcbxAdminPFCEnableEnabled_Type.__name__ = "TruthValue"
_LldpXdot1dcbxAdminPFCEnableEnabled_Object = MibTableColumn
lldpXdot1dcbxAdminPFCEnableEnabled = _LldpXdot1dcbxAdminPFCEnableEnabled_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 4, 3, 2, 1, 2),
    _LldpXdot1dcbxAdminPFCEnableEnabled_Type()
)
lldpXdot1dcbxAdminPFCEnableEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpXdot1dcbxAdminPFCEnableEnabled.setStatus("current")
_LldpXdot1dcbxAdminApplicationPriorityAppTable_Object = MibTable
lldpXdot1dcbxAdminApplicationPriorityAppTable = _LldpXdot1dcbxAdminApplicationPriorityAppTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 4, 4)
)
if mibBuilder.loadTexts:
    lldpXdot1dcbxAdminApplicationPriorityAppTable.setStatus("current")
_LldpXdot1dcbxAdminApplicationPriorityAppEntry_Object = MibTableRow
lldpXdot1dcbxAdminApplicationPriorityAppEntry = _LldpXdot1dcbxAdminApplicationPriorityAppEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 4, 4, 1)
)
lldpXdot1dcbxAdminApplicationPriorityAppEntry.setIndexNames(
    (0, "LLDP-V2-MIB", "lldpV2LocPortIfIndex"),
    (0, "LLDP-EXT-DOT1-DCBX-MIB", "lldpXdot1dcbxAdminApplicationPriorityAESelector"),
    (0, "LLDP-EXT-DOT1-DCBX-MIB", "lldpXdot1dcbxAdminApplicationPriorityAEProtocol"),
)
if mibBuilder.loadTexts:
    lldpXdot1dcbxAdminApplicationPriorityAppEntry.setStatus("current")
_LldpXdot1dcbxAdminApplicationPriorityAESelector_Type = LldpXdot1dcbxAppSelector
_LldpXdot1dcbxAdminApplicationPriorityAESelector_Object = MibTableColumn
lldpXdot1dcbxAdminApplicationPriorityAESelector = _LldpXdot1dcbxAdminApplicationPriorityAESelector_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 4, 4, 1, 1),
    _LldpXdot1dcbxAdminApplicationPriorityAESelector_Type()
)
lldpXdot1dcbxAdminApplicationPriorityAESelector.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lldpXdot1dcbxAdminApplicationPriorityAESelector.setStatus("current")
_LldpXdot1dcbxAdminApplicationPriorityAEProtocol_Type = LldpXdot1dcbxAppProtocol
_LldpXdot1dcbxAdminApplicationPriorityAEProtocol_Object = MibTableColumn
lldpXdot1dcbxAdminApplicationPriorityAEProtocol = _LldpXdot1dcbxAdminApplicationPriorityAEProtocol_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 4, 4, 1, 2),
    _LldpXdot1dcbxAdminApplicationPriorityAEProtocol_Type()
)
lldpXdot1dcbxAdminApplicationPriorityAEProtocol.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lldpXdot1dcbxAdminApplicationPriorityAEProtocol.setStatus("current")
_LldpXdot1dcbxAdminApplicationPriorityAEPriority_Type = IEEE8021PriorityValue
_LldpXdot1dcbxAdminApplicationPriorityAEPriority_Object = MibTableColumn
lldpXdot1dcbxAdminApplicationPriorityAEPriority = _LldpXdot1dcbxAdminApplicationPriorityAEPriority_Object(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 5, 1, 4, 4, 1, 3),
    _LldpXdot1dcbxAdminApplicationPriorityAEPriority_Type()
)
lldpXdot1dcbxAdminApplicationPriorityAEPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lldpXdot1dcbxAdminApplicationPriorityAEPriority.setStatus("current")
_LldpXdot1dcbxConformance_ObjectIdentity = ObjectIdentity
lldpXdot1dcbxConformance = _LldpXdot1dcbxConformance_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 6)
)
_LldpXdot1dcbxCompliances_ObjectIdentity = ObjectIdentity
lldpXdot1dcbxCompliances = _LldpXdot1dcbxCompliances_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 6, 1)
)
_LldpXdot1dcbxGroups_ObjectIdentity = ObjectIdentity
lldpXdot1dcbxGroups = _LldpXdot1dcbxGroups_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 6, 2)
)
lldpV2PortConfigEntry.registerAugmentions(
    ("LLDP-EXT-DOT1-DCBX-MIB",
     "lldpXdot1dcbxConfigETSConfigurationEntry")
)
lldpXdot1dcbxConfigETSConfigurationEntry.setIndexNames(*lldpV2PortConfigEntry.getIndexNames())
lldpV2PortConfigEntry.registerAugmentions(
    ("LLDP-EXT-DOT1-DCBX-MIB",
     "lldpXdot1dcbxConfigETSRecommendationEntry")
)
lldpXdot1dcbxConfigETSRecommendationEntry.setIndexNames(*lldpV2PortConfigEntry.getIndexNames())
lldpV2PortConfigEntry.registerAugmentions(
    ("LLDP-EXT-DOT1-DCBX-MIB",
     "lldpXdot1dcbxConfigPFCEntry")
)
lldpXdot1dcbxConfigPFCEntry.setIndexNames(*lldpV2PortConfigEntry.getIndexNames())
lldpV2PortConfigEntry.registerAugmentions(
    ("LLDP-EXT-DOT1-DCBX-MIB",
     "lldpXdot1dcbxConfigApplicationPriorityEntry")
)
lldpXdot1dcbxConfigApplicationPriorityEntry.setIndexNames(*lldpV2PortConfigEntry.getIndexNames())

# Managed Objects groups

lldpXdot1dcbxETSGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 6, 2, 1)
)
lldpXdot1dcbxETSGroup.setObjects(
      *(("LLDP-EXT-DOT1-DCBX-MIB", "lldpXdot1dcbxConfigETSConfigurationTxEnable"),
        ("LLDP-EXT-DOT1-DCBX-MIB", "lldpXdot1dcbxConfigETSRecommendationTxEnable"),
        ("LLDP-EXT-DOT1-DCBX-MIB", "lldpXdot1dcbxLocETSConCreditBasedShaperSupport"),
        ("LLDP-EXT-DOT1-DCBX-MIB", "lldpXdot1dcbxLocETSConTrafficClassesSupported"),
        ("LLDP-EXT-DOT1-DCBX-MIB", "lldpXdot1dcbxLocETSConWilling"),
        ("LLDP-EXT-DOT1-DCBX-MIB", "lldpXdot1dcbxLocETSConPriTrafficClass"),
        ("LLDP-EXT-DOT1-DCBX-MIB", "lldpXdot1dcbxLocETSConTrafficClassBandwidth"),
        ("LLDP-EXT-DOT1-DCBX-MIB", "lldpXdot1dcbxLocETSConTrafficSelectionAlgorithm"),
        ("LLDP-EXT-DOT1-DCBX-MIB", "lldpXdot1dcbxLocETSRecoTrafficClassBandwidth"),
        ("LLDP-EXT-DOT1-DCBX-MIB", "lldpXdot1dcbxLocETSRecoTrafficSelectionAlgorithm"),
        ("LLDP-EXT-DOT1-DCBX-MIB", "lldpXdot1dcbxRemETSConCreditBasedShaperSupport"),
        ("LLDP-EXT-DOT1-DCBX-MIB", "lldpXdot1dcbxRemETSConTrafficClassesSupported"),
        ("LLDP-EXT-DOT1-DCBX-MIB", "lldpXdot1dcbxRemETSConWilling"),
        ("LLDP-EXT-DOT1-DCBX-MIB", "lldpXdot1dcbxRemETSConPriTrafficClass"),
        ("LLDP-EXT-DOT1-DCBX-MIB", "lldpXdot1dcbxRemETSConTrafficClassBandwidth"),
        ("LLDP-EXT-DOT1-DCBX-MIB", "lldpXdot1dcbxRemETSConTrafficSelectionAlgorithm"),
        ("LLDP-EXT-DOT1-DCBX-MIB", "lldpXdot1dcbxRemETSRecoTrafficClassBandwidth"),
        ("LLDP-EXT-DOT1-DCBX-MIB", "lldpXdot1dcbxRemETSRecoTrafficSelectionAlgorithm"),
        ("LLDP-EXT-DOT1-DCBX-MIB", "lldpXdot1dcbxAdminETSConCreditBasedShaperSupport"),
        ("LLDP-EXT-DOT1-DCBX-MIB", "lldpXdot1dcbxAdminETSConTrafficClassesSupported"),
        ("LLDP-EXT-DOT1-DCBX-MIB", "lldpXdot1dcbxAdminETSConWilling"),
        ("LLDP-EXT-DOT1-DCBX-MIB", "lldpXdot1dcbxAdminETSConPriTrafficClass"),
        ("LLDP-EXT-DOT1-DCBX-MIB", "lldpXdot1dcbxAdminETSConTrafficClassBandwidth"),
        ("LLDP-EXT-DOT1-DCBX-MIB", "lldpXdot1dcbxAdminETSConTrafficSelectionAlgorithm"),
        ("LLDP-EXT-DOT1-DCBX-MIB", "lldpXdot1dcbxAdminETSRecoTrafficClassBandwidth"),
        ("LLDP-EXT-DOT1-DCBX-MIB", "lldpXdot1dcbxAdminETSRecoTrafficSelectionAlgorithm"))
)
if mibBuilder.loadTexts:
    lldpXdot1dcbxETSGroup.setStatus("current")

lldpXdot1dcbxPFCGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 6, 2, 2)
)
lldpXdot1dcbxPFCGroup.setObjects(
      *(("LLDP-EXT-DOT1-DCBX-MIB", "lldpXdot1dcbxConfigPFCTxEnable"),
        ("LLDP-EXT-DOT1-DCBX-MIB", "lldpXdot1dcbxLocPFCWilling"),
        ("LLDP-EXT-DOT1-DCBX-MIB", "lldpXdot1dcbxLocPFCMBC"),
        ("LLDP-EXT-DOT1-DCBX-MIB", "lldpXdot1dcbxLocPFCCap"),
        ("LLDP-EXT-DOT1-DCBX-MIB", "lldpXdot1dcbxLocPFCEnableEnabled"),
        ("LLDP-EXT-DOT1-DCBX-MIB", "lldpXdot1dcbxRemPFCWilling"),
        ("LLDP-EXT-DOT1-DCBX-MIB", "lldpXdot1dcbxRemPFCMBC"),
        ("LLDP-EXT-DOT1-DCBX-MIB", "lldpXdot1dcbxRemPFCCap"),
        ("LLDP-EXT-DOT1-DCBX-MIB", "lldpXdot1dcbxRemPFCEnableEnabled"),
        ("LLDP-EXT-DOT1-DCBX-MIB", "lldpXdot1dcbxAdminPFCWilling"),
        ("LLDP-EXT-DOT1-DCBX-MIB", "lldpXdot1dcbxAdminPFCMBC"),
        ("LLDP-EXT-DOT1-DCBX-MIB", "lldpXdot1dcbxAdminPFCCap"),
        ("LLDP-EXT-DOT1-DCBX-MIB", "lldpXdot1dcbxAdminPFCEnableEnabled"))
)
if mibBuilder.loadTexts:
    lldpXdot1dcbxPFCGroup.setStatus("current")

lldpXdot1dcbxApplicationPriorityGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 6, 2, 3)
)
lldpXdot1dcbxApplicationPriorityGroup.setObjects(
      *(("LLDP-EXT-DOT1-DCBX-MIB", "lldpXdot1dcbxConfigApplicationPriorityTxEnable"),
        ("LLDP-EXT-DOT1-DCBX-MIB", "lldpXdot1dcbxLocApplicationPriorityAEPriority"),
        ("LLDP-EXT-DOT1-DCBX-MIB", "lldpXdot1dcbxRemApplicationPriorityAEPriority"),
        ("LLDP-EXT-DOT1-DCBX-MIB", "lldpXdot1dcbxAdminApplicationPriorityAEPriority"))
)
if mibBuilder.loadTexts:
    lldpXdot1dcbxApplicationPriorityGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

lldpXdot1dcbxCompliance = ModuleCompliance(
    (1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 6, 1, 1)
)
lldpXdot1dcbxCompliance.setObjects(
      *(("LLDP-EXT-DOT1-DCBX-MIB", "lldpXdot1dcbxETSGroup"),
        ("LLDP-EXT-DOT1-DCBX-MIB", "lldpXdot1dcbxPFCGroup"),
        ("LLDP-EXT-DOT1-DCBX-MIB", "lldpXdot1dcbxApplicationPriorityGroup"),
        ("LLDP-EXT-DOT1-DCBX-MIB", "ifGeneralInformationGroup"))
)
if mibBuilder.loadTexts:
    lldpXdot1dcbxCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LLDP-EXT-DOT1-DCBX-MIB",
    **{"LldpXdot1dcbxTrafficClassValue": LldpXdot1dcbxTrafficClassValue,
       "LldpXdot1dcbxTrafficClassBandwidthValue": LldpXdot1dcbxTrafficClassBandwidthValue,
       "LldpXdot1dcbxAppSelector": LldpXdot1dcbxAppSelector,
       "LldpXdot1dcbxAppProtocol": LldpXdot1dcbxAppProtocol,
       "LldpXdot1dcbxSupportedCapacity": LldpXdot1dcbxSupportedCapacity,
       "LldpXdot1dcbxTrafficSelectionAlgorithm": LldpXdot1dcbxTrafficSelectionAlgorithm,
       "lldpXdot1dcbxMIB": lldpXdot1dcbxMIB,
       "lldpXdot1dcbxObjects": lldpXdot1dcbxObjects,
       "lldpXdot1dcbxConfig": lldpXdot1dcbxConfig,
       "lldpXdot1dcbxConfigETSConfigurationTable": lldpXdot1dcbxConfigETSConfigurationTable,
       "lldpXdot1dcbxConfigETSConfigurationEntry": lldpXdot1dcbxConfigETSConfigurationEntry,
       "lldpXdot1dcbxConfigETSConfigurationTxEnable": lldpXdot1dcbxConfigETSConfigurationTxEnable,
       "lldpXdot1dcbxConfigETSRecommendationTable": lldpXdot1dcbxConfigETSRecommendationTable,
       "lldpXdot1dcbxConfigETSRecommendationEntry": lldpXdot1dcbxConfigETSRecommendationEntry,
       "lldpXdot1dcbxConfigETSRecommendationTxEnable": lldpXdot1dcbxConfigETSRecommendationTxEnable,
       "lldpXdot1dcbxConfigPFCTable": lldpXdot1dcbxConfigPFCTable,
       "lldpXdot1dcbxConfigPFCEntry": lldpXdot1dcbxConfigPFCEntry,
       "lldpXdot1dcbxConfigPFCTxEnable": lldpXdot1dcbxConfigPFCTxEnable,
       "lldpXdot1dcbxConfigApplicationPriorityTable": lldpXdot1dcbxConfigApplicationPriorityTable,
       "lldpXdot1dcbxConfigApplicationPriorityEntry": lldpXdot1dcbxConfigApplicationPriorityEntry,
       "lldpXdot1dcbxConfigApplicationPriorityTxEnable": lldpXdot1dcbxConfigApplicationPriorityTxEnable,
       "lldpXdot1dcbxLocalData": lldpXdot1dcbxLocalData,
       "lldpXdot1dcbxLocETSConfiguration": lldpXdot1dcbxLocETSConfiguration,
       "lldpXdot1dcbxLocETSBasicConfigurationTable": lldpXdot1dcbxLocETSBasicConfigurationTable,
       "lldpXdot1dcbxLocETSBasicConfigurationEntry": lldpXdot1dcbxLocETSBasicConfigurationEntry,
       "lldpXdot1dcbxLocETSConCreditBasedShaperSupport": lldpXdot1dcbxLocETSConCreditBasedShaperSupport,
       "lldpXdot1dcbxLocETSConTrafficClassesSupported": lldpXdot1dcbxLocETSConTrafficClassesSupported,
       "lldpXdot1dcbxLocETSConWilling": lldpXdot1dcbxLocETSConWilling,
       "lldpXdot1dcbxLocETSConPriorityAssignmentTable": lldpXdot1dcbxLocETSConPriorityAssignmentTable,
       "lldpXdot1dcbxLocETSConPriorityAssignmentEntry": lldpXdot1dcbxLocETSConPriorityAssignmentEntry,
       "lldpXdot1dcbxLocETSConPriority": lldpXdot1dcbxLocETSConPriority,
       "lldpXdot1dcbxLocETSConPriTrafficClass": lldpXdot1dcbxLocETSConPriTrafficClass,
       "lldpXdot1dcbxLocETSConTrafficClassBandwidthTable": lldpXdot1dcbxLocETSConTrafficClassBandwidthTable,
       "lldpXdot1dcbxLocETSConTrafficClassBandwidthEntry": lldpXdot1dcbxLocETSConTrafficClassBandwidthEntry,
       "lldpXdot1dcbxLocETSConTrafficClass": lldpXdot1dcbxLocETSConTrafficClass,
       "lldpXdot1dcbxLocETSConTrafficClassBandwidth": lldpXdot1dcbxLocETSConTrafficClassBandwidth,
       "lldpXdot1dcbxLocETSConTrafficSelectionAlgorithmTable": lldpXdot1dcbxLocETSConTrafficSelectionAlgorithmTable,
       "lldpXdot1dcbxLocETSConTrafficSelectionAlgorithmEntry": lldpXdot1dcbxLocETSConTrafficSelectionAlgorithmEntry,
       "lldpXdot1dcbxLocETSConTSATrafficClass": lldpXdot1dcbxLocETSConTSATrafficClass,
       "lldpXdot1dcbxLocETSConTrafficSelectionAlgorithm": lldpXdot1dcbxLocETSConTrafficSelectionAlgorithm,
       "lldpXdot1dcbxLocETSReco": lldpXdot1dcbxLocETSReco,
       "lldpXdot1dcbxLocETSRecoTrafficClassBandwidthTable": lldpXdot1dcbxLocETSRecoTrafficClassBandwidthTable,
       "lldpXdot1dcbxLocETSRecoTrafficClassBandwidthEntry": lldpXdot1dcbxLocETSRecoTrafficClassBandwidthEntry,
       "lldpXdot1dcbxLocETSRecoTrafficClass": lldpXdot1dcbxLocETSRecoTrafficClass,
       "lldpXdot1dcbxLocETSRecoTrafficClassBandwidth": lldpXdot1dcbxLocETSRecoTrafficClassBandwidth,
       "lldpXdot1dcbxLocETSRecoTrafficSelectionAlgorithmTable": lldpXdot1dcbxLocETSRecoTrafficSelectionAlgorithmTable,
       "lldpXdot1dcbxLocETSRecoTrafficSelectionAlgorithmEntry": lldpXdot1dcbxLocETSRecoTrafficSelectionAlgorithmEntry,
       "lldpXdot1dcbxLocETSRecoTSATrafficClass": lldpXdot1dcbxLocETSRecoTSATrafficClass,
       "lldpXdot1dcbxLocETSRecoTrafficSelectionAlgorithm": lldpXdot1dcbxLocETSRecoTrafficSelectionAlgorithm,
       "lldpXdot1dcbxLocPFC": lldpXdot1dcbxLocPFC,
       "lldpXdot1dcbxLocPFCBasicTable": lldpXdot1dcbxLocPFCBasicTable,
       "lldpXdot1dcbxLocPFCBasicEntry": lldpXdot1dcbxLocPFCBasicEntry,
       "lldpXdot1dcbxLocPFCWilling": lldpXdot1dcbxLocPFCWilling,
       "lldpXdot1dcbxLocPFCMBC": lldpXdot1dcbxLocPFCMBC,
       "lldpXdot1dcbxLocPFCCap": lldpXdot1dcbxLocPFCCap,
       "lldpXdot1dcbxLocPFCEnableTable": lldpXdot1dcbxLocPFCEnableTable,
       "lldpXdot1dcbxLocPFCEnableEntry": lldpXdot1dcbxLocPFCEnableEntry,
       "lldpXdot1dcbxLocPFCEnablePriority": lldpXdot1dcbxLocPFCEnablePriority,
       "lldpXdot1dcbxLocPFCEnableEnabled": lldpXdot1dcbxLocPFCEnableEnabled,
       "lldpXdot1dcbxLocApplicationPriorityAppTable": lldpXdot1dcbxLocApplicationPriorityAppTable,
       "lldpXdot1dcbxLocApplicationPriorityAppEntry": lldpXdot1dcbxLocApplicationPriorityAppEntry,
       "lldpXdot1dcbxLocApplicationPriorityAESelector": lldpXdot1dcbxLocApplicationPriorityAESelector,
       "lldpXdot1dcbxLocApplicationPriorityAEProtocol": lldpXdot1dcbxLocApplicationPriorityAEProtocol,
       "lldpXdot1dcbxLocApplicationPriorityAEPriority": lldpXdot1dcbxLocApplicationPriorityAEPriority,
       "lldpXdot1dcbxRemoteData": lldpXdot1dcbxRemoteData,
       "lldpXdot1dcbxRemETSConfiguration": lldpXdot1dcbxRemETSConfiguration,
       "lldpXdot1dcbxRemETSBasicConfigurationTable": lldpXdot1dcbxRemETSBasicConfigurationTable,
       "lldpXdot1dcbxRemETSBasicConfigurationEntry": lldpXdot1dcbxRemETSBasicConfigurationEntry,
       "lldpXdot1dcbxRemETSConCreditBasedShaperSupport": lldpXdot1dcbxRemETSConCreditBasedShaperSupport,
       "lldpXdot1dcbxRemETSConTrafficClassesSupported": lldpXdot1dcbxRemETSConTrafficClassesSupported,
       "lldpXdot1dcbxRemETSConWilling": lldpXdot1dcbxRemETSConWilling,
       "lldpXdot1dcbxRemETSConPriorityAssignmentTable": lldpXdot1dcbxRemETSConPriorityAssignmentTable,
       "lldpXdot1dcbxRemETSConPriorityAssignmentEntry": lldpXdot1dcbxRemETSConPriorityAssignmentEntry,
       "lldpXdot1dcbxRemETSConPriority": lldpXdot1dcbxRemETSConPriority,
       "lldpXdot1dcbxRemETSConPriTrafficClass": lldpXdot1dcbxRemETSConPriTrafficClass,
       "lldpXdot1dcbxRemETSConTrafficClassBandwidthTable": lldpXdot1dcbxRemETSConTrafficClassBandwidthTable,
       "lldpXdot1dcbxRemETSConTrafficClassBandwidthEntry": lldpXdot1dcbxRemETSConTrafficClassBandwidthEntry,
       "lldpXdot1dcbxRemETSConTrafficClass": lldpXdot1dcbxRemETSConTrafficClass,
       "lldpXdot1dcbxRemETSConTrafficClassBandwidth": lldpXdot1dcbxRemETSConTrafficClassBandwidth,
       "lldpXdot1dcbxRemETSConTrafficSelectionAlgorithmTable": lldpXdot1dcbxRemETSConTrafficSelectionAlgorithmTable,
       "lldpXdot1dcbxRemETSConTrafficSelectionAlgorithmEntry": lldpXdot1dcbxRemETSConTrafficSelectionAlgorithmEntry,
       "lldpXdot1dcbxRemETSConTSATrafficClass": lldpXdot1dcbxRemETSConTSATrafficClass,
       "lldpXdot1dcbxRemETSConTrafficSelectionAlgorithm": lldpXdot1dcbxRemETSConTrafficSelectionAlgorithm,
       "lldpXdot1dcbxRemETSReco": lldpXdot1dcbxRemETSReco,
       "lldpXdot1dcbxRemETSRecoTrafficClassBandwidthTable": lldpXdot1dcbxRemETSRecoTrafficClassBandwidthTable,
       "lldpXdot1dcbxRemETSRecoTrafficClassBandwidthEntry": lldpXdot1dcbxRemETSRecoTrafficClassBandwidthEntry,
       "lldpXdot1dcbxRemETSRecoTrafficClass": lldpXdot1dcbxRemETSRecoTrafficClass,
       "lldpXdot1dcbxRemETSRecoTrafficClassBandwidth": lldpXdot1dcbxRemETSRecoTrafficClassBandwidth,
       "lldpXdot1dcbxRemETSRecoTrafficSelectionAlgorithmTable": lldpXdot1dcbxRemETSRecoTrafficSelectionAlgorithmTable,
       "lldpXdot1dcbxRemETSRecoTrafficSelectionAlgorithmEntry": lldpXdot1dcbxRemETSRecoTrafficSelectionAlgorithmEntry,
       "lldpXdot1dcbxRemETSRecoTSATrafficClass": lldpXdot1dcbxRemETSRecoTSATrafficClass,
       "lldpXdot1dcbxRemETSRecoTrafficSelectionAlgorithm": lldpXdot1dcbxRemETSRecoTrafficSelectionAlgorithm,
       "lldpXdot1dcbxRemPFC": lldpXdot1dcbxRemPFC,
       "lldpXdot1dcbxRemPFCBasicTable": lldpXdot1dcbxRemPFCBasicTable,
       "lldpXdot1dcbxRemPFCBasicEntry": lldpXdot1dcbxRemPFCBasicEntry,
       "lldpXdot1dcbxRemPFCWilling": lldpXdot1dcbxRemPFCWilling,
       "lldpXdot1dcbxRemPFCMBC": lldpXdot1dcbxRemPFCMBC,
       "lldpXdot1dcbxRemPFCCap": lldpXdot1dcbxRemPFCCap,
       "lldpXdot1dcbxRemPFCEnableTable": lldpXdot1dcbxRemPFCEnableTable,
       "lldpXdot1dcbxRemPFCEnableEntry": lldpXdot1dcbxRemPFCEnableEntry,
       "lldpXdot1dcbxRemPFCEnablePriority": lldpXdot1dcbxRemPFCEnablePriority,
       "lldpXdot1dcbxRemPFCEnableEnabled": lldpXdot1dcbxRemPFCEnableEnabled,
       "lldpXdot1dcbxRemApplicationPriorityAppTable": lldpXdot1dcbxRemApplicationPriorityAppTable,
       "lldpXdot1dcbxRemApplicationPriorityAppEntry": lldpXdot1dcbxRemApplicationPriorityAppEntry,
       "lldpXdot1dcbxRemApplicationPriorityAESelector": lldpXdot1dcbxRemApplicationPriorityAESelector,
       "lldpXdot1dcbxRemApplicationPriorityAEProtocol": lldpXdot1dcbxRemApplicationPriorityAEProtocol,
       "lldpXdot1dcbxRemApplicationPriorityAEPriority": lldpXdot1dcbxRemApplicationPriorityAEPriority,
       "lldpXdot1dcbxAdminData": lldpXdot1dcbxAdminData,
       "lldpXdot1dcbxAdminETSConfiguration": lldpXdot1dcbxAdminETSConfiguration,
       "lldpXdot1dcbxAdminETSBasicConfigurationTable": lldpXdot1dcbxAdminETSBasicConfigurationTable,
       "lldpXdot1dcbxAdminETSBasicConfigurationEntry": lldpXdot1dcbxAdminETSBasicConfigurationEntry,
       "lldpXdot1dcbxAdminETSConCreditBasedShaperSupport": lldpXdot1dcbxAdminETSConCreditBasedShaperSupport,
       "lldpXdot1dcbxAdminETSConTrafficClassesSupported": lldpXdot1dcbxAdminETSConTrafficClassesSupported,
       "lldpXdot1dcbxAdminETSConWilling": lldpXdot1dcbxAdminETSConWilling,
       "lldpXdot1dcbxAdminETSConPriorityAssignmentTable": lldpXdot1dcbxAdminETSConPriorityAssignmentTable,
       "lldpXdot1dcbxAdminETSConPriorityAssignmentEntry": lldpXdot1dcbxAdminETSConPriorityAssignmentEntry,
       "lldpXdot1dcbxAdminETSConPriority": lldpXdot1dcbxAdminETSConPriority,
       "lldpXdot1dcbxAdminETSConPriTrafficClass": lldpXdot1dcbxAdminETSConPriTrafficClass,
       "lldpXdot1dcbxAdminETSConTrafficClassBandwidthTable": lldpXdot1dcbxAdminETSConTrafficClassBandwidthTable,
       "lldpXdot1dcbxAdminETSConTrafficClassBandwidthEntry": lldpXdot1dcbxAdminETSConTrafficClassBandwidthEntry,
       "lldpXdot1dcbxAdminETSConTrafficClass": lldpXdot1dcbxAdminETSConTrafficClass,
       "lldpXdot1dcbxAdminETSConTrafficClassBandwidth": lldpXdot1dcbxAdminETSConTrafficClassBandwidth,
       "lldpXdot1dcbxAdminETSConTrafficSelectionAlgorithmTable": lldpXdot1dcbxAdminETSConTrafficSelectionAlgorithmTable,
       "lldpXdot1dcbxAdminETSConTrafficSelectionAlgorithmEntry": lldpXdot1dcbxAdminETSConTrafficSelectionAlgorithmEntry,
       "lldpXdot1dcbxAdminETSConTSATrafficClass": lldpXdot1dcbxAdminETSConTSATrafficClass,
       "lldpXdot1dcbxAdminETSConTrafficSelectionAlgorithm": lldpXdot1dcbxAdminETSConTrafficSelectionAlgorithm,
       "lldpXdot1dcbxAdminETSReco": lldpXdot1dcbxAdminETSReco,
       "lldpXdot1dcbxAdminETSRecoTrafficClassBandwidthTable": lldpXdot1dcbxAdminETSRecoTrafficClassBandwidthTable,
       "lldpXdot1dcbxAdminETSRecoTrafficClassBandwidthEntry": lldpXdot1dcbxAdminETSRecoTrafficClassBandwidthEntry,
       "lldpXdot1dcbxAdminETSRecoTrafficClass": lldpXdot1dcbxAdminETSRecoTrafficClass,
       "lldpXdot1dcbxAdminETSRecoTrafficClassBandwidth": lldpXdot1dcbxAdminETSRecoTrafficClassBandwidth,
       "lldpXdot1dcbxAdminETSRecoTrafficSelectionAlgorithmTable": lldpXdot1dcbxAdminETSRecoTrafficSelectionAlgorithmTable,
       "lldpXdot1dcbxAdminETSRecoTrafficSelectionAlgorithmEntry": lldpXdot1dcbxAdminETSRecoTrafficSelectionAlgorithmEntry,
       "lldpXdot1dcbxAdminETSRecoTSATrafficClass": lldpXdot1dcbxAdminETSRecoTSATrafficClass,
       "lldpXdot1dcbxAdminETSRecoTrafficSelectionAlgorithm": lldpXdot1dcbxAdminETSRecoTrafficSelectionAlgorithm,
       "lldpXdot1dcbxAdminPFC": lldpXdot1dcbxAdminPFC,
       "lldpXdot1dcbxAdminPFCBasicTable": lldpXdot1dcbxAdminPFCBasicTable,
       "lldpXdot1dcbxAdminPFCBasicEntry": lldpXdot1dcbxAdminPFCBasicEntry,
       "lldpXdot1dcbxAdminPFCWilling": lldpXdot1dcbxAdminPFCWilling,
       "lldpXdot1dcbxAdminPFCMBC": lldpXdot1dcbxAdminPFCMBC,
       "lldpXdot1dcbxAdminPFCCap": lldpXdot1dcbxAdminPFCCap,
       "lldpXdot1dcbxAdminPFCEnableTable": lldpXdot1dcbxAdminPFCEnableTable,
       "lldpXdot1dcbxAdminPFCEnableEntry": lldpXdot1dcbxAdminPFCEnableEntry,
       "lldpXdot1dcbxAdminPFCEnablePriority": lldpXdot1dcbxAdminPFCEnablePriority,
       "lldpXdot1dcbxAdminPFCEnableEnabled": lldpXdot1dcbxAdminPFCEnableEnabled,
       "lldpXdot1dcbxAdminApplicationPriorityAppTable": lldpXdot1dcbxAdminApplicationPriorityAppTable,
       "lldpXdot1dcbxAdminApplicationPriorityAppEntry": lldpXdot1dcbxAdminApplicationPriorityAppEntry,
       "lldpXdot1dcbxAdminApplicationPriorityAESelector": lldpXdot1dcbxAdminApplicationPriorityAESelector,
       "lldpXdot1dcbxAdminApplicationPriorityAEProtocol": lldpXdot1dcbxAdminApplicationPriorityAEProtocol,
       "lldpXdot1dcbxAdminApplicationPriorityAEPriority": lldpXdot1dcbxAdminApplicationPriorityAEPriority,
       "lldpXdot1dcbxConformance": lldpXdot1dcbxConformance,
       "lldpXdot1dcbxCompliances": lldpXdot1dcbxCompliances,
       "lldpXdot1dcbxCompliance": lldpXdot1dcbxCompliance,
       "lldpXdot1dcbxGroups": lldpXdot1dcbxGroups,
       "lldpXdot1dcbxETSGroup": lldpXdot1dcbxETSGroup,
       "lldpXdot1dcbxPFCGroup": lldpXdot1dcbxPFCGroup,
       "lldpXdot1dcbxApplicationPriorityGroup": lldpXdot1dcbxApplicationPriorityGroup}
)
