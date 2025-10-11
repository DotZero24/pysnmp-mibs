# SNMP MIB module (BWM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/radware/BWM-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:15:12 2025
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

(DpsSessionType,) = mibBuilder.importSymbols(
    "GENERIC-MIB",
    "DpsSessionType")

(ipAddrEntry,) = mibBuilder.importSymbols(
    "IP-MIB",
    "ipAddrEntry")

(Ipv6Address,) = mibBuilder.importSymbols(
    "IPV6-TC",
    "Ipv6Address")

(FeatureStatus,
 RowStatus,
 TruthValue,
 rndErrorDesc,
 rndErrorSeverity,
 rsBWM) = mibBuilder.importSymbols(
    "RADWARE-MIB",
    "FeatureStatus",
    "RowStatus",
    "TruthValue",
    "rndErrorDesc",
    "rndErrorSeverity",
    "rsBWM")

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
 NotificationType,
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
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DisplayString,
 MacAddress,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions



class NetNumber(OctetString):
    """Custom type NetNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RsBWMRulesTable_Object = MibTable
rsBWMRulesTable = _RsBWMRulesTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 1)
)
if mibBuilder.loadTexts:
    rsBWMRulesTable.setStatus("mandatory")
_RsBWMRulesEntry_Object = MibTableRow
rsBWMRulesEntry = _RsBWMRulesEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 1, 1)
)
rsBWMRulesEntry.setIndexNames(
    (0, "BWM-MIB", "rsBWMRulesName"),
)
if mibBuilder.loadTexts:
    rsBWMRulesEntry.setStatus("mandatory")
_RsBWMRulesIndex_Type = Integer32
_RsBWMRulesIndex_Object = MibTableColumn
rsBWMRulesIndex = _RsBWMRulesIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 1, 1, 1),
    _RsBWMRulesIndex_Type()
)
rsBWMRulesIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMRulesIndex.setStatus("mandatory")


class _RsBWMRulesName_Type(DisplayString):
    """Custom type rsBWMRulesName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_RsBWMRulesName_Type.__name__ = "DisplayString"
_RsBWMRulesName_Object = MibTableColumn
rsBWMRulesName = _RsBWMRulesName_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 1, 1, 2),
    _RsBWMRulesName_Type()
)
rsBWMRulesName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMRulesName.setStatus("mandatory")


class _RsBWMRulesDestination_Type(DisplayString):
    """Custom type rsBWMRulesDestination based on DisplayString"""
    defaultValue = OctetString("any")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 46),
    )


_RsBWMRulesDestination_Type.__name__ = "DisplayString"
_RsBWMRulesDestination_Object = MibTableColumn
rsBWMRulesDestination = _RsBWMRulesDestination_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 1, 1, 3),
    _RsBWMRulesDestination_Type()
)
rsBWMRulesDestination.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMRulesDestination.setStatus("mandatory")


class _RsBWMRulesSource_Type(DisplayString):
    """Custom type rsBWMRulesSource based on DisplayString"""
    defaultValue = OctetString("any")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 46),
    )


_RsBWMRulesSource_Type.__name__ = "DisplayString"
_RsBWMRulesSource_Object = MibTableColumn
rsBWMRulesSource = _RsBWMRulesSource_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 1, 1, 4),
    _RsBWMRulesSource_Type()
)
rsBWMRulesSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMRulesSource.setStatus("mandatory")
_RsBWMRulesStatus_Type = RowStatus
_RsBWMRulesStatus_Object = MibTableColumn
rsBWMRulesStatus = _RsBWMRulesStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 1, 1, 5),
    _RsBWMRulesStatus_Type()
)
rsBWMRulesStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMRulesStatus.setStatus("mandatory")


class _RsBWMRulesAction_Type(Integer32):
    """Custom type rsBWMRulesAction based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("forward", 1),
          ("block", 2),
          ("blockAndReset", 3),
          ("blockAndBiDirectionalReset", 4),
          ("monitorHTTP", 5),
          ("monitorHTTPS", 6),
          ("monitorTCP", 7))
    )


_RsBWMRulesAction_Type.__name__ = "Integer32"
_RsBWMRulesAction_Object = MibTableColumn
rsBWMRulesAction = _RsBWMRulesAction_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 1, 1, 6),
    _RsBWMRulesAction_Type()
)
rsBWMRulesAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMRulesAction.setStatus("mandatory")


class _RsBWMRulesDirection_Type(Integer32):
    """Custom type rsBWMRulesDirection based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("oneway", 1),
          ("twoway", 2),
          ("session", 3))
    )


_RsBWMRulesDirection_Type.__name__ = "Integer32"
_RsBWMRulesDirection_Object = MibTableColumn
rsBWMRulesDirection = _RsBWMRulesDirection_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 1, 1, 7),
    _RsBWMRulesDirection_Type()
)
rsBWMRulesDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMRulesDirection.setStatus("mandatory")


class _RsBWMRulesPriority_Type(Integer32):
    """Custom type rsBWMRulesPriority based on Integer32"""
    defaultValue = 65535


_RsBWMRulesPriority_Type.__name__ = "Integer32"
_RsBWMRulesPriority_Object = MibTableColumn
rsBWMRulesPriority = _RsBWMRulesPriority_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 1, 1, 8),
    _RsBWMRulesPriority_Type()
)
rsBWMRulesPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMRulesPriority.setStatus("mandatory")


class _RsBWMRulesPhysicalPort_Type(Integer32):
    """Custom type rsBWMRulesPhysicalPort based on Integer32"""
    defaultValue = 0


_RsBWMRulesPhysicalPort_Type.__name__ = "Integer32"
_RsBWMRulesPhysicalPort_Object = MibTableColumn
rsBWMRulesPhysicalPort = _RsBWMRulesPhysicalPort_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 1, 1, 9),
    _RsBWMRulesPhysicalPort_Type()
)
rsBWMRulesPhysicalPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMRulesPhysicalPort.setStatus("mandatory")


class _RsBWMRulesType_Type(Integer32):
    """Custom type rsBWMRulesType based on Integer32"""
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
        *(("facsBandwidth", 1),
          ("counter", 2),
          ("ids", 3),
          ("chain", 4))
    )


_RsBWMRulesType_Type.__name__ = "Integer32"
_RsBWMRulesType_Object = MibTableColumn
rsBWMRulesType = _RsBWMRulesType_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 1, 1, 10),
    _RsBWMRulesType_Type()
)
rsBWMRulesType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMRulesType.setStatus("mandatory")


class _RsBWMRulesDescription_Type(DisplayString):
    """Custom type rsBWMRulesDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 19),
    )


_RsBWMRulesDescription_Type.__name__ = "DisplayString"
_RsBWMRulesDescription_Object = MibTableColumn
rsBWMRulesDescription = _RsBWMRulesDescription_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 1, 1, 11),
    _RsBWMRulesDescription_Type()
)
rsBWMRulesDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMRulesDescription.setStatus("mandatory")


class _RsBWMRulesGuaranteedBW_Type(Integer32):
    """Custom type rsBWMRulesGuaranteedBW based on Integer32"""
    defaultValue = 0


_RsBWMRulesGuaranteedBW_Type.__name__ = "Integer32"
_RsBWMRulesGuaranteedBW_Object = MibTableColumn
rsBWMRulesGuaranteedBW = _RsBWMRulesGuaranteedBW_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 1, 1, 12),
    _RsBWMRulesGuaranteedBW_Type()
)
rsBWMRulesGuaranteedBW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMRulesGuaranteedBW.setStatus("mandatory")


class _RsBWMRulesPolicyType_Type(Integer32):
    """Custom type rsBWMRulesPolicyType based on Integer32"""
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
        *(("none", 1),
          ("filter", 2),
          ("group", 3),
          ("policy", 4))
    )


_RsBWMRulesPolicyType_Type.__name__ = "Integer32"
_RsBWMRulesPolicyType_Object = MibTableColumn
rsBWMRulesPolicyType = _RsBWMRulesPolicyType_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 1, 1, 13),
    _RsBWMRulesPolicyType_Type()
)
rsBWMRulesPolicyType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMRulesPolicyType.setStatus("mandatory")


class _RsBWMRulesPolicy_Type(DisplayString):
    """Custom type rsBWMRulesPolicy based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 29),
    )


_RsBWMRulesPolicy_Type.__name__ = "DisplayString"
_RsBWMRulesPolicy_Object = MibTableColumn
rsBWMRulesPolicy = _RsBWMRulesPolicy_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 1, 1, 14),
    _RsBWMRulesPolicy_Type()
)
rsBWMRulesPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMRulesPolicy.setStatus("mandatory")


class _RsBWMRulesOperationalStatus_Type(Integer32):
    """Custom type rsBWMRulesOperationalStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_RsBWMRulesOperationalStatus_Type.__name__ = "Integer32"
_RsBWMRulesOperationalStatus_Object = MibTableColumn
rsBWMRulesOperationalStatus = _RsBWMRulesOperationalStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 1, 1, 15),
    _RsBWMRulesOperationalStatus_Type()
)
rsBWMRulesOperationalStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMRulesOperationalStatus.setStatus("mandatory")


class _RsBWMRulesDSCPMarking_Type(Integer32):
    """Custom type rsBWMRulesDSCPMarking based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 63),
    )


_RsBWMRulesDSCPMarking_Type.__name__ = "Integer32"
_RsBWMRulesDSCPMarking_Object = MibTableColumn
rsBWMRulesDSCPMarking = _RsBWMRulesDSCPMarking_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 1, 1, 16),
    _RsBWMRulesDSCPMarking_Type()
)
rsBWMRulesDSCPMarking.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMRulesDSCPMarking.setStatus("mandatory")


class _RsBWMRulesReportBlockedPackets_Type(Integer32):
    """Custom type rsBWMRulesReportBlockedPackets based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1),
          ("securityEvent", 2))
    )


_RsBWMRulesReportBlockedPackets_Type.__name__ = "Integer32"
_RsBWMRulesReportBlockedPackets_Object = MibTableColumn
rsBWMRulesReportBlockedPackets = _RsBWMRulesReportBlockedPackets_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 1, 1, 17),
    _RsBWMRulesReportBlockedPackets_Type()
)
rsBWMRulesReportBlockedPackets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMRulesReportBlockedPackets.setStatus("mandatory")


class _RsBWMRulesMaxBW_Type(Integer32):
    """Custom type rsBWMRulesMaxBW based on Integer32"""
    defaultValue = 2147483647


_RsBWMRulesMaxBW_Type.__name__ = "Integer32"
_RsBWMRulesMaxBW_Object = MibTableColumn
rsBWMRulesMaxBW = _RsBWMRulesMaxBW_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 1, 1, 18),
    _RsBWMRulesMaxBW_Type()
)
rsBWMRulesMaxBW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMRulesMaxBW.setStatus("mandatory")


class _RsBWMRulesSpecific_Type(DisplayString):
    """Custom type rsBWMRulesSpecific based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 19),
    )


_RsBWMRulesSpecific_Type.__name__ = "DisplayString"
_RsBWMRulesSpecific_Object = MibTableColumn
rsBWMRulesSpecific = _RsBWMRulesSpecific_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 1, 1, 19),
    _RsBWMRulesSpecific_Type()
)
rsBWMRulesSpecific.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMRulesSpecific.setStatus("mandatory")


class _RsBWMRulesPhysicalPortGroup_Type(DisplayString):
    """Custom type rsBWMRulesPhysicalPortGroup based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 19),
    )


_RsBWMRulesPhysicalPortGroup_Type.__name__ = "DisplayString"
_RsBWMRulesPhysicalPortGroup_Object = MibTableColumn
rsBWMRulesPhysicalPortGroup = _RsBWMRulesPhysicalPortGroup_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 1, 1, 20),
    _RsBWMRulesPhysicalPortGroup_Type()
)
rsBWMRulesPhysicalPortGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMRulesPhysicalPortGroup.setStatus("mandatory")


class _RsBWMRulesVLANTagGroup_Type(DisplayString):
    """Custom type rsBWMRulesVLANTagGroup based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 19),
    )


_RsBWMRulesVLANTagGroup_Type.__name__ = "DisplayString"
_RsBWMRulesVLANTagGroup_Object = MibTableColumn
rsBWMRulesVLANTagGroup = _RsBWMRulesVLANTagGroup_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 1, 1, 21),
    _RsBWMRulesVLANTagGroup_Type()
)
rsBWMRulesVLANTagGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMRulesVLANTagGroup.setStatus("mandatory")


class _RsBWMRulesTrafficIdentification_Type(Integer32):
    """Custom type rsBWMRulesTrafficIdentification based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("client", 1),
          ("session", 2),
          ("connection", 3),
          ("fullL4Session", 4),
          ("sessionCookie", 5))
    )


_RsBWMRulesTrafficIdentification_Type.__name__ = "Integer32"
_RsBWMRulesTrafficIdentification_Object = MibTableColumn
rsBWMRulesTrafficIdentification = _RsBWMRulesTrafficIdentification_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 1, 1, 22),
    _RsBWMRulesTrafficIdentification_Type()
)
rsBWMRulesTrafficIdentification.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMRulesTrafficIdentification.setStatus("mandatory")
_RsBWMRulesTrafficFlowMaxBW_Type = Integer32
_RsBWMRulesTrafficFlowMaxBW_Object = MibTableColumn
rsBWMRulesTrafficFlowMaxBW = _RsBWMRulesTrafficFlowMaxBW_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 1, 1, 23),
    _RsBWMRulesTrafficFlowMaxBW_Type()
)
rsBWMRulesTrafficFlowMaxBW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMRulesTrafficFlowMaxBW.setStatus("mandatory")
_RsBWMRulesMaxConcurrentSessions_Type = Integer32
_RsBWMRulesMaxConcurrentSessions_Object = MibTableColumn
rsBWMRulesMaxConcurrentSessions = _RsBWMRulesMaxConcurrentSessions_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 1, 1, 24),
    _RsBWMRulesMaxConcurrentSessions_Type()
)
rsBWMRulesMaxConcurrentSessions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMRulesMaxConcurrentSessions.setStatus("mandatory")


class _RsBWMRulesTrafficIDCookieField_Type(DisplayString):
    """Custom type rsBWMRulesTrafficIDCookieField based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 19),
    )


_RsBWMRulesTrafficIDCookieField_Type.__name__ = "DisplayString"
_RsBWMRulesTrafficIDCookieField_Object = MibTableColumn
rsBWMRulesTrafficIDCookieField = _RsBWMRulesTrafficIDCookieField_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 1, 1, 25),
    _RsBWMRulesTrafficIDCookieField_Type()
)
rsBWMRulesTrafficIDCookieField.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMRulesTrafficIDCookieField.setStatus("mandatory")


class _RsBWMRulesPolicyGroup_Type(DisplayString):
    """Custom type rsBWMRulesPolicyGroup based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 19),
    )


_RsBWMRulesPolicyGroup_Type.__name__ = "DisplayString"
_RsBWMRulesPolicyGroup_Object = MibTableColumn
rsBWMRulesPolicyGroup = _RsBWMRulesPolicyGroup_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 1, 1, 26),
    _RsBWMRulesPolicyGroup_Type()
)
rsBWMRulesPolicyGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMRulesPolicyGroup.setStatus("mandatory")


class _RsBWMRulesRadiusRule_Type(DisplayString):
    """Custom type rsBWMRulesRadiusRule based on DisplayString"""
    defaultValue = OctetString("any")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_RsBWMRulesRadiusRule_Type.__name__ = "DisplayString"
_RsBWMRulesRadiusRule_Object = MibTableColumn
rsBWMRulesRadiusRule = _RsBWMRulesRadiusRule_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 1, 1, 27),
    _RsBWMRulesRadiusRule_Type()
)
rsBWMRulesRadiusRule.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMRulesRadiusRule.setStatus("mandatory")
_RsBWMRulesIPObjectTable_Object = MibTable
rsBWMRulesIPObjectTable = _RsBWMRulesIPObjectTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 2)
)
if mibBuilder.loadTexts:
    rsBWMRulesIPObjectTable.setStatus("mandatory")
_RsBWMRulesIPObjectEntry_Object = MibTableRow
rsBWMRulesIPObjectEntry = _RsBWMRulesIPObjectEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 2, 1)
)
rsBWMRulesIPObjectEntry.setIndexNames(
    (0, "BWM-MIB", "rsBWMRulesIPObjectName"),
    (0, "BWM-MIB", "rsBWMRulesIPObjectSubIndex"),
)
if mibBuilder.loadTexts:
    rsBWMRulesIPObjectEntry.setStatus("mandatory")


class _RsBWMRulesIPObjectName_Type(DisplayString):
    """Custom type rsBWMRulesIPObjectName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 19),
    )


_RsBWMRulesIPObjectName_Type.__name__ = "DisplayString"
_RsBWMRulesIPObjectName_Object = MibTableColumn
rsBWMRulesIPObjectName = _RsBWMRulesIPObjectName_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 2, 1, 1),
    _RsBWMRulesIPObjectName_Type()
)
rsBWMRulesIPObjectName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMRulesIPObjectName.setStatus("mandatory")


class _RsBWMRulesIPObjectSubIndex_Type(Integer32):
    """Custom type rsBWMRulesIPObjectSubIndex based on Integer32"""
    defaultValue = 0


_RsBWMRulesIPObjectSubIndex_Type.__name__ = "Integer32"
_RsBWMRulesIPObjectSubIndex_Object = MibTableColumn
rsBWMRulesIPObjectSubIndex = _RsBWMRulesIPObjectSubIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 2, 1, 2),
    _RsBWMRulesIPObjectSubIndex_Type()
)
rsBWMRulesIPObjectSubIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMRulesIPObjectSubIndex.setStatus("mandatory")
_RsBWMRulesIPObjectAddress_Type = IpAddress
_RsBWMRulesIPObjectAddress_Object = MibTableColumn
rsBWMRulesIPObjectAddress = _RsBWMRulesIPObjectAddress_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 2, 1, 3),
    _RsBWMRulesIPObjectAddress_Type()
)
rsBWMRulesIPObjectAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMRulesIPObjectAddress.setStatus("mandatory")
_RsBWMRulesIPObjectMask_Type = IpAddress
_RsBWMRulesIPObjectMask_Object = MibTableColumn
rsBWMRulesIPObjectMask = _RsBWMRulesIPObjectMask_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 2, 1, 4),
    _RsBWMRulesIPObjectMask_Type()
)
rsBWMRulesIPObjectMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMRulesIPObjectMask.setStatus("mandatory")
_RsBWMRulesIPObjectFromIP_Type = IpAddress
_RsBWMRulesIPObjectFromIP_Object = MibTableColumn
rsBWMRulesIPObjectFromIP = _RsBWMRulesIPObjectFromIP_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 2, 1, 5),
    _RsBWMRulesIPObjectFromIP_Type()
)
rsBWMRulesIPObjectFromIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMRulesIPObjectFromIP.setStatus("mandatory")
_RsBWMRulesIPObjectToIP_Type = IpAddress
_RsBWMRulesIPObjectToIP_Object = MibTableColumn
rsBWMRulesIPObjectToIP = _RsBWMRulesIPObjectToIP_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 2, 1, 6),
    _RsBWMRulesIPObjectToIP_Type()
)
rsBWMRulesIPObjectToIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMRulesIPObjectToIP.setStatus("mandatory")


class _RsBWMRulesIPObjectMode_Type(Integer32):
    """Custom type rsBWMRulesIPObjectMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ipMask", 1),
          ("ipRange", 2),
          ("dynamic", 3))
    )


_RsBWMRulesIPObjectMode_Type.__name__ = "Integer32"
_RsBWMRulesIPObjectMode_Object = MibTableColumn
rsBWMRulesIPObjectMode = _RsBWMRulesIPObjectMode_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 2, 1, 7),
    _RsBWMRulesIPObjectMode_Type()
)
rsBWMRulesIPObjectMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMRulesIPObjectMode.setStatus("mandatory")
_RsBWMRulesIPObjectStatus_Type = RowStatus
_RsBWMRulesIPObjectStatus_Object = MibTableColumn
rsBWMRulesIPObjectStatus = _RsBWMRulesIPObjectStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 2, 1, 8),
    _RsBWMRulesIPObjectStatus_Type()
)
rsBWMRulesIPObjectStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMRulesIPObjectStatus.setStatus("mandatory")


class _RsBWMCBQMode_Type(Integer32):
    """Custom type rsBWMCBQMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cyclic", 1),
          ("cbq", 2))
    )


_RsBWMCBQMode_Type.__name__ = "Integer32"
_RsBWMCBQMode_Object = MibScalar
rsBWMCBQMode = _RsBWMCBQMode_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 3),
    _RsBWMCBQMode_Type()
)
rsBWMCBQMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMCBQMode.setStatus("mandatory")


class _RsBWMActualQueueSize_Type(Integer32):
    """Custom type rsBWMActualQueueSize based on Integer32"""
    defaultValue = 0


_RsBWMActualQueueSize_Type.__name__ = "Integer32"
_RsBWMActualQueueSize_Object = MibScalar
rsBWMActualQueueSize = _RsBWMActualQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 4),
    _RsBWMActualQueueSize_Type()
)
rsBWMActualQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMActualQueueSize.setStatus("mandatory")


class _RsBWMAverageQueueSize_Type(Integer32):
    """Custom type rsBWMAverageQueueSize based on Integer32"""
    defaultValue = 0


_RsBWMAverageQueueSize_Type.__name__ = "Integer32"
_RsBWMAverageQueueSize_Object = MibScalar
rsBWMAverageQueueSize = _RsBWMAverageQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 5),
    _RsBWMAverageQueueSize_Type()
)
rsBWMAverageQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMAverageQueueSize.setStatus("mandatory")


class _RsBWMQueueRedDropped_Type(Integer32):
    """Custom type rsBWMQueueRedDropped based on Integer32"""
    defaultValue = 0


_RsBWMQueueRedDropped_Type.__name__ = "Integer32"
_RsBWMQueueRedDropped_Object = MibScalar
rsBWMQueueRedDropped = _RsBWMQueueRedDropped_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 6),
    _RsBWMQueueRedDropped_Type()
)
rsBWMQueueRedDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMQueueRedDropped.setStatus("mandatory")
_RsBWMPriorityTable_Object = MibTable
rsBWMPriorityTable = _RsBWMPriorityTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 7)
)
if mibBuilder.loadTexts:
    rsBWMPriorityTable.setStatus("mandatory")
_RsBWMPriorityEntry_Object = MibTableRow
rsBWMPriorityEntry = _RsBWMPriorityEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 7, 1)
)
rsBWMPriorityEntry.setIndexNames(
    (0, "BWM-MIB", "rsBWMPriority"),
)
if mibBuilder.loadTexts:
    rsBWMPriorityEntry.setStatus("mandatory")
_RsBWMPriority_Type = Integer32
_RsBWMPriority_Object = MibTableColumn
rsBWMPriority = _RsBWMPriority_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 7, 1, 1),
    _RsBWMPriority_Type()
)
rsBWMPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMPriority.setStatus("mandatory")
_RsBWMPacketsSent_Type = Integer32
_RsBWMPacketsSent_Object = MibTableColumn
rsBWMPacketsSent = _RsBWMPacketsSent_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 7, 1, 2),
    _RsBWMPacketsSent_Type()
)
rsBWMPacketsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMPacketsSent.setStatus("mandatory")


class _RsBWMRedMode_Type(Integer32):
    """Custom type rsBWMRedMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("global", 2),
          ("weighted", 3))
    )


_RsBWMRedMode_Type.__name__ = "Integer32"
_RsBWMRedMode_Object = MibScalar
rsBWMRedMode = _RsBWMRedMode_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 8),
    _RsBWMRedMode_Type()
)
rsBWMRedMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMRedMode.setStatus("mandatory")
_RsBWMCurrentRulesTable_Object = MibTable
rsBWMCurrentRulesTable = _RsBWMCurrentRulesTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 9)
)
if mibBuilder.loadTexts:
    rsBWMCurrentRulesTable.setStatus("mandatory")
_RsBWMCurrentRulesEntry_Object = MibTableRow
rsBWMCurrentRulesEntry = _RsBWMCurrentRulesEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 9, 1)
)
rsBWMCurrentRulesEntry.setIndexNames(
    (0, "BWM-MIB", "rsBWMCurrentRulesName"),
)
if mibBuilder.loadTexts:
    rsBWMCurrentRulesEntry.setStatus("mandatory")
_RsBWMCurrentRulesIndex_Type = Integer32
_RsBWMCurrentRulesIndex_Object = MibTableColumn
rsBWMCurrentRulesIndex = _RsBWMCurrentRulesIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 9, 1, 1),
    _RsBWMCurrentRulesIndex_Type()
)
rsBWMCurrentRulesIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMCurrentRulesIndex.setStatus("mandatory")


class _RsBWMCurrentRulesName_Type(DisplayString):
    """Custom type rsBWMCurrentRulesName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_RsBWMCurrentRulesName_Type.__name__ = "DisplayString"
_RsBWMCurrentRulesName_Object = MibTableColumn
rsBWMCurrentRulesName = _RsBWMCurrentRulesName_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 9, 1, 2),
    _RsBWMCurrentRulesName_Type()
)
rsBWMCurrentRulesName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMCurrentRulesName.setStatus("mandatory")


class _RsBWMCurrentRulesDestination_Type(DisplayString):
    """Custom type rsBWMCurrentRulesDestination based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 46),
    )


_RsBWMCurrentRulesDestination_Type.__name__ = "DisplayString"
_RsBWMCurrentRulesDestination_Object = MibTableColumn
rsBWMCurrentRulesDestination = _RsBWMCurrentRulesDestination_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 9, 1, 3),
    _RsBWMCurrentRulesDestination_Type()
)
rsBWMCurrentRulesDestination.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMCurrentRulesDestination.setStatus("mandatory")


class _RsBWMCurrentRulesSource_Type(DisplayString):
    """Custom type rsBWMCurrentRulesSource based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 46),
    )


_RsBWMCurrentRulesSource_Type.__name__ = "DisplayString"
_RsBWMCurrentRulesSource_Object = MibTableColumn
rsBWMCurrentRulesSource = _RsBWMCurrentRulesSource_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 9, 1, 4),
    _RsBWMCurrentRulesSource_Type()
)
rsBWMCurrentRulesSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMCurrentRulesSource.setStatus("mandatory")


class _RsBWMCurrentRulesAction_Type(Integer32):
    """Custom type rsBWMCurrentRulesAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("forward", 1),
          ("block", 2),
          ("blockAndReset", 3),
          ("blockAndBiDirectionalReset", 4),
          ("monitorHTTP", 5),
          ("monitorHTTPS", 6),
          ("monitorTCP", 7))
    )


_RsBWMCurrentRulesAction_Type.__name__ = "Integer32"
_RsBWMCurrentRulesAction_Object = MibTableColumn
rsBWMCurrentRulesAction = _RsBWMCurrentRulesAction_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 9, 1, 5),
    _RsBWMCurrentRulesAction_Type()
)
rsBWMCurrentRulesAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMCurrentRulesAction.setStatus("mandatory")


class _RsBWMCurrentRulesDirection_Type(Integer32):
    """Custom type rsBWMCurrentRulesDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("oneway", 1),
          ("twoway", 2),
          ("session", 3))
    )


_RsBWMCurrentRulesDirection_Type.__name__ = "Integer32"
_RsBWMCurrentRulesDirection_Object = MibTableColumn
rsBWMCurrentRulesDirection = _RsBWMCurrentRulesDirection_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 9, 1, 6),
    _RsBWMCurrentRulesDirection_Type()
)
rsBWMCurrentRulesDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMCurrentRulesDirection.setStatus("mandatory")
_RsBWMCurrentRulesPriority_Type = Integer32
_RsBWMCurrentRulesPriority_Object = MibTableColumn
rsBWMCurrentRulesPriority = _RsBWMCurrentRulesPriority_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 9, 1, 7),
    _RsBWMCurrentRulesPriority_Type()
)
rsBWMCurrentRulesPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMCurrentRulesPriority.setStatus("mandatory")
_RsBWMCurrentRulesPhysicalPort_Type = Integer32
_RsBWMCurrentRulesPhysicalPort_Object = MibTableColumn
rsBWMCurrentRulesPhysicalPort = _RsBWMCurrentRulesPhysicalPort_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 9, 1, 8),
    _RsBWMCurrentRulesPhysicalPort_Type()
)
rsBWMCurrentRulesPhysicalPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMCurrentRulesPhysicalPort.setStatus("mandatory")


class _RsBWMCurrentRulesType_Type(Integer32):
    """Custom type rsBWMCurrentRulesType based on Integer32"""
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
        *(("facsBandwidth", 1),
          ("counter", 2),
          ("ids", 3),
          ("chain", 4))
    )


_RsBWMCurrentRulesType_Type.__name__ = "Integer32"
_RsBWMCurrentRulesType_Object = MibTableColumn
rsBWMCurrentRulesType = _RsBWMCurrentRulesType_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 9, 1, 9),
    _RsBWMCurrentRulesType_Type()
)
rsBWMCurrentRulesType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMCurrentRulesType.setStatus("mandatory")


class _RsBWMCurrentRulesDescription_Type(DisplayString):
    """Custom type rsBWMCurrentRulesDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 19),
    )


_RsBWMCurrentRulesDescription_Type.__name__ = "DisplayString"
_RsBWMCurrentRulesDescription_Object = MibTableColumn
rsBWMCurrentRulesDescription = _RsBWMCurrentRulesDescription_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 9, 1, 10),
    _RsBWMCurrentRulesDescription_Type()
)
rsBWMCurrentRulesDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMCurrentRulesDescription.setStatus("mandatory")
_RsBWMCurrentRulesGuaranteedBW_Type = Counter32
_RsBWMCurrentRulesGuaranteedBW_Object = MibTableColumn
rsBWMCurrentRulesGuaranteedBW = _RsBWMCurrentRulesGuaranteedBW_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 9, 1, 11),
    _RsBWMCurrentRulesGuaranteedBW_Type()
)
rsBWMCurrentRulesGuaranteedBW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMCurrentRulesGuaranteedBW.setStatus("mandatory")
_RsBWMCurrentRulesMaxBW_Type = Counter32
_RsBWMCurrentRulesMaxBW_Object = MibTableColumn
rsBWMCurrentRulesMaxBW = _RsBWMCurrentRulesMaxBW_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 9, 1, 12),
    _RsBWMCurrentRulesMaxBW_Type()
)
rsBWMCurrentRulesMaxBW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMCurrentRulesMaxBW.setStatus("mandatory")


class _RsBWMCurrentRulesPolicyType_Type(Integer32):
    """Custom type rsBWMCurrentRulesPolicyType based on Integer32"""
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
        *(("none", 1),
          ("filter", 2),
          ("group", 3),
          ("policy", 4))
    )


_RsBWMCurrentRulesPolicyType_Type.__name__ = "Integer32"
_RsBWMCurrentRulesPolicyType_Object = MibTableColumn
rsBWMCurrentRulesPolicyType = _RsBWMCurrentRulesPolicyType_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 9, 1, 13),
    _RsBWMCurrentRulesPolicyType_Type()
)
rsBWMCurrentRulesPolicyType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMCurrentRulesPolicyType.setStatus("mandatory")


class _RsBWMCurrentRulesPolicy_Type(DisplayString):
    """Custom type rsBWMCurrentRulesPolicy based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 29),
    )


_RsBWMCurrentRulesPolicy_Type.__name__ = "DisplayString"
_RsBWMCurrentRulesPolicy_Object = MibTableColumn
rsBWMCurrentRulesPolicy = _RsBWMCurrentRulesPolicy_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 9, 1, 14),
    _RsBWMCurrentRulesPolicy_Type()
)
rsBWMCurrentRulesPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMCurrentRulesPolicy.setStatus("mandatory")


class _RsBWMCurrentRulesDSCPMarking_Type(Integer32):
    """Custom type rsBWMCurrentRulesDSCPMarking based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 63),
    )


_RsBWMCurrentRulesDSCPMarking_Type.__name__ = "Integer32"
_RsBWMCurrentRulesDSCPMarking_Object = MibTableColumn
rsBWMCurrentRulesDSCPMarking = _RsBWMCurrentRulesDSCPMarking_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 9, 1, 15),
    _RsBWMCurrentRulesDSCPMarking_Type()
)
rsBWMCurrentRulesDSCPMarking.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMCurrentRulesDSCPMarking.setStatus("mandatory")


class _RsBWMCurrentRulesReportBlockedPackets_Type(Integer32):
    """Custom type rsBWMCurrentRulesReportBlockedPackets based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1),
          ("securityEvent", 2))
    )


_RsBWMCurrentRulesReportBlockedPackets_Type.__name__ = "Integer32"
_RsBWMCurrentRulesReportBlockedPackets_Object = MibTableColumn
rsBWMCurrentRulesReportBlockedPackets = _RsBWMCurrentRulesReportBlockedPackets_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 9, 1, 16),
    _RsBWMCurrentRulesReportBlockedPackets_Type()
)
rsBWMCurrentRulesReportBlockedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMCurrentRulesReportBlockedPackets.setStatus("mandatory")


class _RsBWMCurrentRulesSpecific_Type(DisplayString):
    """Custom type rsBWMCurrentRulesSpecific based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 19),
    )


_RsBWMCurrentRulesSpecific_Type.__name__ = "DisplayString"
_RsBWMCurrentRulesSpecific_Object = MibTableColumn
rsBWMCurrentRulesSpecific = _RsBWMCurrentRulesSpecific_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 9, 1, 17),
    _RsBWMCurrentRulesSpecific_Type()
)
rsBWMCurrentRulesSpecific.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMCurrentRulesSpecific.setStatus("mandatory")


class _RsBWMCurrentRulesPhysicalPortGroup_Type(DisplayString):
    """Custom type rsBWMCurrentRulesPhysicalPortGroup based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 19),
    )


_RsBWMCurrentRulesPhysicalPortGroup_Type.__name__ = "DisplayString"
_RsBWMCurrentRulesPhysicalPortGroup_Object = MibTableColumn
rsBWMCurrentRulesPhysicalPortGroup = _RsBWMCurrentRulesPhysicalPortGroup_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 9, 1, 18),
    _RsBWMCurrentRulesPhysicalPortGroup_Type()
)
rsBWMCurrentRulesPhysicalPortGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMCurrentRulesPhysicalPortGroup.setStatus("mandatory")


class _RsBWMCurrentRulesVLANTagGroup_Type(DisplayString):
    """Custom type rsBWMCurrentRulesVLANTagGroup based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 19),
    )


_RsBWMCurrentRulesVLANTagGroup_Type.__name__ = "DisplayString"
_RsBWMCurrentRulesVLANTagGroup_Object = MibTableColumn
rsBWMCurrentRulesVLANTagGroup = _RsBWMCurrentRulesVLANTagGroup_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 9, 1, 19),
    _RsBWMCurrentRulesVLANTagGroup_Type()
)
rsBWMCurrentRulesVLANTagGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMCurrentRulesVLANTagGroup.setStatus("mandatory")


class _RsBWMCurrentRulesTrafficIdentification_Type(Integer32):
    """Custom type rsBWMCurrentRulesTrafficIdentification based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("client", 1),
          ("session", 2),
          ("connection", 3),
          ("fullL4Session", 4),
          ("sessionCookie", 5))
    )


_RsBWMCurrentRulesTrafficIdentification_Type.__name__ = "Integer32"
_RsBWMCurrentRulesTrafficIdentification_Object = MibTableColumn
rsBWMCurrentRulesTrafficIdentification = _RsBWMCurrentRulesTrafficIdentification_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 9, 1, 20),
    _RsBWMCurrentRulesTrafficIdentification_Type()
)
rsBWMCurrentRulesTrafficIdentification.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMCurrentRulesTrafficIdentification.setStatus("mandatory")
_RsBWMCurrentRulesTrafficFlowMaxBW_Type = Integer32
_RsBWMCurrentRulesTrafficFlowMaxBW_Object = MibTableColumn
rsBWMCurrentRulesTrafficFlowMaxBW = _RsBWMCurrentRulesTrafficFlowMaxBW_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 9, 1, 21),
    _RsBWMCurrentRulesTrafficFlowMaxBW_Type()
)
rsBWMCurrentRulesTrafficFlowMaxBW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMCurrentRulesTrafficFlowMaxBW.setStatus("mandatory")
_RsBWMCurrentRulesMaxConcurrentSessions_Type = Integer32
_RsBWMCurrentRulesMaxConcurrentSessions_Object = MibTableColumn
rsBWMCurrentRulesMaxConcurrentSessions = _RsBWMCurrentRulesMaxConcurrentSessions_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 9, 1, 22),
    _RsBWMCurrentRulesMaxConcurrentSessions_Type()
)
rsBWMCurrentRulesMaxConcurrentSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMCurrentRulesMaxConcurrentSessions.setStatus("mandatory")


class _RsBWMCurrentRulesTrafficIDCookieField_Type(DisplayString):
    """Custom type rsBWMCurrentRulesTrafficIDCookieField based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 19),
    )


_RsBWMCurrentRulesTrafficIDCookieField_Type.__name__ = "DisplayString"
_RsBWMCurrentRulesTrafficIDCookieField_Object = MibTableColumn
rsBWMCurrentRulesTrafficIDCookieField = _RsBWMCurrentRulesTrafficIDCookieField_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 9, 1, 23),
    _RsBWMCurrentRulesTrafficIDCookieField_Type()
)
rsBWMCurrentRulesTrafficIDCookieField.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMCurrentRulesTrafficIDCookieField.setStatus("mandatory")


class _RsBWMCurrentRulesPolicyGroup_Type(DisplayString):
    """Custom type rsBWMCurrentRulesPolicyGroup based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 19),
    )


_RsBWMCurrentRulesPolicyGroup_Type.__name__ = "DisplayString"
_RsBWMCurrentRulesPolicyGroup_Object = MibTableColumn
rsBWMCurrentRulesPolicyGroup = _RsBWMCurrentRulesPolicyGroup_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 9, 1, 24),
    _RsBWMCurrentRulesPolicyGroup_Type()
)
rsBWMCurrentRulesPolicyGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMCurrentRulesPolicyGroup.setStatus("mandatory")


class _RsBWMCurrentRulesRadiusRule_Type(DisplayString):
    """Custom type rsBWMCurrentRulesRadiusRule based on DisplayString"""
    defaultValue = OctetString("any")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_RsBWMCurrentRulesRadiusRule_Type.__name__ = "DisplayString"
_RsBWMCurrentRulesRadiusRule_Object = MibTableColumn
rsBWMCurrentRulesRadiusRule = _RsBWMCurrentRulesRadiusRule_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 9, 1, 25),
    _RsBWMCurrentRulesRadiusRule_Type()
)
rsBWMCurrentRulesRadiusRule.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMCurrentRulesRadiusRule.setStatus("mandatory")
_RsBWMCurrentRulesIPObjectTable_Object = MibTable
rsBWMCurrentRulesIPObjectTable = _RsBWMCurrentRulesIPObjectTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 10)
)
if mibBuilder.loadTexts:
    rsBWMCurrentRulesIPObjectTable.setStatus("mandatory")
_RsBWMCurrentRulesIPObjectEntry_Object = MibTableRow
rsBWMCurrentRulesIPObjectEntry = _RsBWMCurrentRulesIPObjectEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 10, 1)
)
rsBWMCurrentRulesIPObjectEntry.setIndexNames(
    (0, "BWM-MIB", "rsBWMCurrentRulesIPObjectName"),
    (0, "BWM-MIB", "rsBWMCurrentRulesIPObjectSubIndex"),
)
if mibBuilder.loadTexts:
    rsBWMCurrentRulesIPObjectEntry.setStatus("mandatory")


class _RsBWMCurrentRulesIPObjectName_Type(DisplayString):
    """Custom type rsBWMCurrentRulesIPObjectName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 19),
    )


_RsBWMCurrentRulesIPObjectName_Type.__name__ = "DisplayString"
_RsBWMCurrentRulesIPObjectName_Object = MibTableColumn
rsBWMCurrentRulesIPObjectName = _RsBWMCurrentRulesIPObjectName_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 10, 1, 1),
    _RsBWMCurrentRulesIPObjectName_Type()
)
rsBWMCurrentRulesIPObjectName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMCurrentRulesIPObjectName.setStatus("mandatory")
_RsBWMCurrentRulesIPObjectSubIndex_Type = Integer32
_RsBWMCurrentRulesIPObjectSubIndex_Object = MibTableColumn
rsBWMCurrentRulesIPObjectSubIndex = _RsBWMCurrentRulesIPObjectSubIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 10, 1, 2),
    _RsBWMCurrentRulesIPObjectSubIndex_Type()
)
rsBWMCurrentRulesIPObjectSubIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMCurrentRulesIPObjectSubIndex.setStatus("mandatory")
_RsBWMCurrentRulesIPObjectAddress_Type = IpAddress
_RsBWMCurrentRulesIPObjectAddress_Object = MibTableColumn
rsBWMCurrentRulesIPObjectAddress = _RsBWMCurrentRulesIPObjectAddress_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 10, 1, 3),
    _RsBWMCurrentRulesIPObjectAddress_Type()
)
rsBWMCurrentRulesIPObjectAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMCurrentRulesIPObjectAddress.setStatus("mandatory")
_RsBWMCurrentRulesIPObjectMask_Type = IpAddress
_RsBWMCurrentRulesIPObjectMask_Object = MibTableColumn
rsBWMCurrentRulesIPObjectMask = _RsBWMCurrentRulesIPObjectMask_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 10, 1, 4),
    _RsBWMCurrentRulesIPObjectMask_Type()
)
rsBWMCurrentRulesIPObjectMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMCurrentRulesIPObjectMask.setStatus("mandatory")
_RsBWMCurrentRulesIPObjectFromIP_Type = IpAddress
_RsBWMCurrentRulesIPObjectFromIP_Object = MibTableColumn
rsBWMCurrentRulesIPObjectFromIP = _RsBWMCurrentRulesIPObjectFromIP_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 10, 1, 5),
    _RsBWMCurrentRulesIPObjectFromIP_Type()
)
rsBWMCurrentRulesIPObjectFromIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMCurrentRulesIPObjectFromIP.setStatus("mandatory")
_RsBWMCurrentRulesIPObjectToIP_Type = IpAddress
_RsBWMCurrentRulesIPObjectToIP_Object = MibTableColumn
rsBWMCurrentRulesIPObjectToIP = _RsBWMCurrentRulesIPObjectToIP_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 10, 1, 6),
    _RsBWMCurrentRulesIPObjectToIP_Type()
)
rsBWMCurrentRulesIPObjectToIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMCurrentRulesIPObjectToIP.setStatus("mandatory")


class _RsBWMCurrentRulesIPObjectMode_Type(Integer32):
    """Custom type rsBWMCurrentRulesIPObjectMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ipMask", 1),
          ("ipRange", 2),
          ("dynamic", 3))
    )


_RsBWMCurrentRulesIPObjectMode_Type.__name__ = "Integer32"
_RsBWMCurrentRulesIPObjectMode_Object = MibTableColumn
rsBWMCurrentRulesIPObjectMode = _RsBWMCurrentRulesIPObjectMode_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 10, 1, 7),
    _RsBWMCurrentRulesIPObjectMode_Type()
)
rsBWMCurrentRulesIPObjectMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMCurrentRulesIPObjectMode.setStatus("mandatory")


class _RsBWMClassificationMode_Type(Integer32):
    """Custom type rsBWMClassificationMode based on Integer32"""
    defaultValue = 2

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
        *(("policies", 1),
          ("disabled", 2),
          ("diffserv", 3),
          ("tos", 4))
    )


_RsBWMClassificationMode_Type.__name__ = "Integer32"
_RsBWMClassificationMode_Object = MibScalar
rsBWMClassificationMode = _RsBWMClassificationMode_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 11),
    _RsBWMClassificationMode_Type()
)
rsBWMClassificationMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMClassificationMode.setStatus("mandatory")
_RsBWMMaximumBandwidth_Type = Counter32
_RsBWMMaximumBandwidth_Object = MibScalar
rsBWMMaximumBandwidth = _RsBWMMaximumBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 12),
    _RsBWMMaximumBandwidth_Type()
)
rsBWMMaximumBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMMaximumBandwidth.setStatus("mandatory")


class _RsBWMBandwidthBorrowingMode_Type(Integer32):
    """Custom type rsBWMBandwidthBorrowingMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_RsBWMBandwidthBorrowingMode_Type.__name__ = "Integer32"
_RsBWMBandwidthBorrowingMode_Object = MibScalar
rsBWMBandwidthBorrowingMode = _RsBWMBandwidthBorrowingMode_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 13),
    _RsBWMBandwidthBorrowingMode_Type()
)
rsBWMBandwidthBorrowingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMBandwidthBorrowingMode.setStatus("mandatory")


class _RsBWMActions_Type(Integer32):
    """Custom type rsBWMActions based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("updateRules", 1),
          ("defaultDSCPs", 2))
    )


_RsBWMActions_Type.__name__ = "Integer32"
_RsBWMActions_Object = MibScalar
rsBWMActions = _RsBWMActions_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 14),
    _RsBWMActions_Type()
)
rsBWMActions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMActions.setStatus("mandatory")
_RsBWMFilterEntryTable_Object = MibTable
rsBWMFilterEntryTable = _RsBWMFilterEntryTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 15)
)
if mibBuilder.loadTexts:
    rsBWMFilterEntryTable.setStatus("mandatory")
_RsBWMFilterEntry_Object = MibTableRow
rsBWMFilterEntry = _RsBWMFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 15, 1)
)
rsBWMFilterEntry.setIndexNames(
    (0, "BWM-MIB", "rsBWMFilterName"),
)
if mibBuilder.loadTexts:
    rsBWMFilterEntry.setStatus("mandatory")


class _RsBWMFilterName_Type(DisplayString):
    """Custom type rsBWMFilterName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 29),
    )


_RsBWMFilterName_Type.__name__ = "DisplayString"
_RsBWMFilterName_Object = MibTableColumn
rsBWMFilterName = _RsBWMFilterName_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 15, 1, 1),
    _RsBWMFilterName_Type()
)
rsBWMFilterName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMFilterName.setStatus("mandatory")


class _RsBWMFilterDescription_Type(DisplayString):
    """Custom type rsBWMFilterDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 29),
    )


_RsBWMFilterDescription_Type.__name__ = "DisplayString"
_RsBWMFilterDescription_Object = MibTableColumn
rsBWMFilterDescription = _RsBWMFilterDescription_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 15, 1, 2),
    _RsBWMFilterDescription_Type()
)
rsBWMFilterDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMFilterDescription.setStatus("mandatory")


class _RsBWMFilterProtocol_Type(Integer32):
    """Custom type rsBWMFilterProtocol based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("ip", 1),
          ("tcp", 2),
          ("udp", 3),
          ("icmp", 4),
          ("nonIp", 5),
          ("icmpv6", 6),
          ("sctp", 7))
    )


_RsBWMFilterProtocol_Type.__name__ = "Integer32"
_RsBWMFilterProtocol_Object = MibTableColumn
rsBWMFilterProtocol = _RsBWMFilterProtocol_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 15, 1, 3),
    _RsBWMFilterProtocol_Type()
)
rsBWMFilterProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMFilterProtocol.setStatus("mandatory")
_RsBWMFilterDestinationPort_Type = Integer32
_RsBWMFilterDestinationPort_Object = MibTableColumn
rsBWMFilterDestinationPort = _RsBWMFilterDestinationPort_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 15, 1, 4),
    _RsBWMFilterDestinationPort_Type()
)
rsBWMFilterDestinationPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMFilterDestinationPort.setStatus("mandatory")
_RsBWMFilterSourceFromPort_Type = Integer32
_RsBWMFilterSourceFromPort_Object = MibTableColumn
rsBWMFilterSourceFromPort = _RsBWMFilterSourceFromPort_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 15, 1, 5),
    _RsBWMFilterSourceFromPort_Type()
)
rsBWMFilterSourceFromPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMFilterSourceFromPort.setStatus("mandatory")
_RsBWMFilterSourceToPort_Type = Integer32
_RsBWMFilterSourceToPort_Object = MibTableColumn
rsBWMFilterSourceToPort = _RsBWMFilterSourceToPort_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 15, 1, 6),
    _RsBWMFilterSourceToPort_Type()
)
rsBWMFilterSourceToPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMFilterSourceToPort.setStatus("mandatory")
_RsBWMFilterOMPCOffset_Type = Integer32
_RsBWMFilterOMPCOffset_Object = MibTableColumn
rsBWMFilterOMPCOffset = _RsBWMFilterOMPCOffset_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 15, 1, 7),
    _RsBWMFilterOMPCOffset_Type()
)
rsBWMFilterOMPCOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMFilterOMPCOffset.setStatus("mandatory")


class _RsBWMFilterOMPCMask_Type(OctetString):
    """Custom type rsBWMFilterOMPCMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4


_RsBWMFilterOMPCMask_Type.__name__ = "OctetString"
_RsBWMFilterOMPCMask_Object = MibTableColumn
rsBWMFilterOMPCMask = _RsBWMFilterOMPCMask_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 15, 1, 8),
    _RsBWMFilterOMPCMask_Type()
)
rsBWMFilterOMPCMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMFilterOMPCMask.setStatus("mandatory")


class _RsBWMFilterOMPCPattern_Type(OctetString):
    """Custom type rsBWMFilterOMPCPattern based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4


_RsBWMFilterOMPCPattern_Type.__name__ = "OctetString"
_RsBWMFilterOMPCPattern_Object = MibTableColumn
rsBWMFilterOMPCPattern = _RsBWMFilterOMPCPattern_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 15, 1, 9),
    _RsBWMFilterOMPCPattern_Type()
)
rsBWMFilterOMPCPattern.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMFilterOMPCPattern.setStatus("mandatory")


class _RsBWMFilterOMPCCondition_Type(Integer32):
    """Custom type rsBWMFilterOMPCCondition based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("equal", 2),
          ("notEqual", 3),
          ("greaterThan", 4),
          ("lessThan", 5))
    )


_RsBWMFilterOMPCCondition_Type.__name__ = "Integer32"
_RsBWMFilterOMPCCondition_Object = MibTableColumn
rsBWMFilterOMPCCondition = _RsBWMFilterOMPCCondition_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 15, 1, 10),
    _RsBWMFilterOMPCCondition_Type()
)
rsBWMFilterOMPCCondition.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMFilterOMPCCondition.setStatus("mandatory")


class _RsBWMFilterOMPCLength_Type(Integer32):
    """Custom type rsBWMFilterOMPCLength based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("oneByte", 1),
          ("twoBytes", 2),
          ("threeBytes", 3),
          ("fourBytes", 4),
          ("notApplicable", 5))
    )


_RsBWMFilterOMPCLength_Type.__name__ = "Integer32"
_RsBWMFilterOMPCLength_Object = MibTableColumn
rsBWMFilterOMPCLength = _RsBWMFilterOMPCLength_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 15, 1, 11),
    _RsBWMFilterOMPCLength_Type()
)
rsBWMFilterOMPCLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMFilterOMPCLength.setStatus("mandatory")
_RsBWMFilterContentOffset_Type = Integer32
_RsBWMFilterContentOffset_Object = MibTableColumn
rsBWMFilterContentOffset = _RsBWMFilterContentOffset_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 15, 1, 12),
    _RsBWMFilterContentOffset_Type()
)
rsBWMFilterContentOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMFilterContentOffset.setStatus("mandatory")


class _RsBWMFilterContent_Type(DisplayString):
    """Custom type rsBWMFilterContent based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_RsBWMFilterContent_Type.__name__ = "DisplayString"
_RsBWMFilterContent_Object = MibTableColumn
rsBWMFilterContent = _RsBWMFilterContent_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 15, 1, 13),
    _RsBWMFilterContent_Type()
)
rsBWMFilterContent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMFilterContent.setStatus("mandatory")


class _RsBWMFilterContentType_Type(Integer32):
    """Custom type rsBWMFilterContentType based on Integer32"""
    defaultValue = 1

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
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("url", 2),
          ("text", 3),
          ("hostname", 4),
          ("headertype", 5),
          ("expression", 6),
          ("maildomain", 7),
          ("mailto", 8),
          ("mailfrom", 9),
          ("mailsubject", 10),
          ("filetype", 11),
          ("cookiedata", 12),
          ("idsurl", 13),
          ("pop3user", 14),
          ("urilength", 15),
          ("ftp", 16),
          ("ftpcontent", 17),
          ("rpc", 18),
          ("dceRPC", 19),
          ("genericUrl", 20),
          ("genericHeader", 21),
          ("genericCookie", 22),
          ("sipcallfrom", 23),
          ("sipcallto", 24),
          ("sipcaller", 25))
    )


_RsBWMFilterContentType_Type.__name__ = "Integer32"
_RsBWMFilterContentType_Object = MibTableColumn
rsBWMFilterContentType = _RsBWMFilterContentType_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 15, 1, 14),
    _RsBWMFilterContentType_Type()
)
rsBWMFilterContentType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMFilterContentType.setStatus("mandatory")


class _RsBWMFilterType_Type(Integer32):
    """Custom type rsBWMFilterType based on Integer32"""
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
        *(("regular", 1),
          ("static", 2),
          ("ids", 3),
          ("idsStatic", 4))
    )


_RsBWMFilterType_Type.__name__ = "Integer32"
_RsBWMFilterType_Object = MibTableColumn
rsBWMFilterType = _RsBWMFilterType_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 15, 1, 15),
    _RsBWMFilterType_Type()
)
rsBWMFilterType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMFilterType.setStatus("mandatory")
_RsBWMFilterStatus_Type = RowStatus
_RsBWMFilterStatus_Object = MibTableColumn
rsBWMFilterStatus = _RsBWMFilterStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 15, 1, 16),
    _RsBWMFilterStatus_Type()
)
rsBWMFilterStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMFilterStatus.setStatus("mandatory")
_RsBWMFilterContentEnd_Type = Integer32
_RsBWMFilterContentEnd_Object = MibTableColumn
rsBWMFilterContentEnd = _RsBWMFilterContentEnd_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 15, 1, 17),
    _RsBWMFilterContentEnd_Type()
)
rsBWMFilterContentEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMFilterContentEnd.setStatus("mandatory")


class _RsBWMFilterContentData_Type(DisplayString):
    """Custom type rsBWMFilterContentData based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_RsBWMFilterContentData_Type.__name__ = "DisplayString"
_RsBWMFilterContentData_Object = MibTableColumn
rsBWMFilterContentData = _RsBWMFilterContentData_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 15, 1, 18),
    _RsBWMFilterContentData_Type()
)
rsBWMFilterContentData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMFilterContentData.setStatus("mandatory")


class _RsBWMFilterContentCoding_Type(Integer32):
    """Custom type rsBWMFilterContentCoding based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("caseInsensitive", 2),
          ("caseSensitive", 3),
          ("hex", 4),
          ("international", 5))
    )


_RsBWMFilterContentCoding_Type.__name__ = "Integer32"
_RsBWMFilterContentCoding_Object = MibTableColumn
rsBWMFilterContentCoding = _RsBWMFilterContentCoding_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 15, 1, 19),
    _RsBWMFilterContentCoding_Type()
)
rsBWMFilterContentCoding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMFilterContentCoding.setStatus("mandatory")


class _RsBWMFilterContentDataCoding_Type(Integer32):
    """Custom type rsBWMFilterContentDataCoding based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("caseInsensitive", 2),
          ("caseSensitive", 3),
          ("hex", 4),
          ("international", 5))
    )


_RsBWMFilterContentDataCoding_Type.__name__ = "Integer32"
_RsBWMFilterContentDataCoding_Object = MibTableColumn
rsBWMFilterContentDataCoding = _RsBWMFilterContentDataCoding_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 15, 1, 20),
    _RsBWMFilterContentDataCoding_Type()
)
rsBWMFilterContentDataCoding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMFilterContentDataCoding.setStatus("mandatory")


class _RsBWMFilterOMPCOffsetBase_Type(Integer32):
    """Custom type rsBWMFilterOMPCOffsetBase based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("ipHeader", 1),
          ("ipData", 2),
          ("tcpData", 3),
          ("asn1", 4),
          ("ethernet", 5),
          ("l4Header", 6),
          ("ipv6Header", 7))
    )


_RsBWMFilterOMPCOffsetBase_Type.__name__ = "Integer32"
_RsBWMFilterOMPCOffsetBase_Object = MibTableColumn
rsBWMFilterOMPCOffsetBase = _RsBWMFilterOMPCOffsetBase_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 15, 1, 21),
    _RsBWMFilterOMPCOffsetBase_Type()
)
rsBWMFilterOMPCOffsetBase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMFilterOMPCOffsetBase.setStatus("mandatory")
_RsBWMFilterDestinationMaxPort_Type = Integer32
_RsBWMFilterDestinationMaxPort_Object = MibTableColumn
rsBWMFilterDestinationMaxPort = _RsBWMFilterDestinationMaxPort_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 15, 1, 22),
    _RsBWMFilterDestinationMaxPort_Type()
)
rsBWMFilterDestinationMaxPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMFilterDestinationMaxPort.setStatus("mandatory")


class _RsBWMFilterSourceAppPortGroup_Type(DisplayString):
    """Custom type rsBWMFilterSourceAppPortGroup based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 29),
    )


_RsBWMFilterSourceAppPortGroup_Type.__name__ = "DisplayString"
_RsBWMFilterSourceAppPortGroup_Object = MibTableColumn
rsBWMFilterSourceAppPortGroup = _RsBWMFilterSourceAppPortGroup_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 15, 1, 23),
    _RsBWMFilterSourceAppPortGroup_Type()
)
rsBWMFilterSourceAppPortGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMFilterSourceAppPortGroup.setStatus("mandatory")


class _RsBWMFilterDestinationAppPortGroup_Type(DisplayString):
    """Custom type rsBWMFilterDestinationAppPortGroup based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 29),
    )


_RsBWMFilterDestinationAppPortGroup_Type.__name__ = "DisplayString"
_RsBWMFilterDestinationAppPortGroup_Object = MibTableColumn
rsBWMFilterDestinationAppPortGroup = _RsBWMFilterDestinationAppPortGroup_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 15, 1, 24),
    _RsBWMFilterDestinationAppPortGroup_Type()
)
rsBWMFilterDestinationAppPortGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMFilterDestinationAppPortGroup.setStatus("mandatory")


class _RsBWMFilterSessionType_Type(DpsSessionType):
    """Custom type rsBWMFilterSessionType based on DpsSessionType"""
    defaultValue = 0


_RsBWMFilterSessionType_Type.__name__ = "DpsSessionType"
_RsBWMFilterSessionType_Object = MibTableColumn
rsBWMFilterSessionType = _RsBWMFilterSessionType_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 15, 1, 25),
    _RsBWMFilterSessionType_Type()
)
rsBWMFilterSessionType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMFilterSessionType.setStatus("mandatory")


class _RsBWMFilterSessionTypeDirection_Type(Integer32):
    """Custom type rsBWMFilterSessionTypeDirection based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("all", 0),
          ("rqst", 1),
          ("rply", 2))
    )


_RsBWMFilterSessionTypeDirection_Type.__name__ = "Integer32"
_RsBWMFilterSessionTypeDirection_Object = MibTableColumn
rsBWMFilterSessionTypeDirection = _RsBWMFilterSessionTypeDirection_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 15, 1, 26),
    _RsBWMFilterSessionTypeDirection_Type()
)
rsBWMFilterSessionTypeDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMFilterSessionTypeDirection.setStatus("mandatory")
_RsBWMCurrentFilterEntryTable_Object = MibTable
rsBWMCurrentFilterEntryTable = _RsBWMCurrentFilterEntryTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 16)
)
if mibBuilder.loadTexts:
    rsBWMCurrentFilterEntryTable.setStatus("mandatory")
_RsBWMCurrentFilterEntry_Object = MibTableRow
rsBWMCurrentFilterEntry = _RsBWMCurrentFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 16, 1)
)
rsBWMCurrentFilterEntry.setIndexNames(
    (0, "BWM-MIB", "rsBWMCurrentFilterName"),
)
if mibBuilder.loadTexts:
    rsBWMCurrentFilterEntry.setStatus("mandatory")


class _RsBWMCurrentFilterName_Type(DisplayString):
    """Custom type rsBWMCurrentFilterName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 29),
    )


_RsBWMCurrentFilterName_Type.__name__ = "DisplayString"
_RsBWMCurrentFilterName_Object = MibTableColumn
rsBWMCurrentFilterName = _RsBWMCurrentFilterName_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 16, 1, 1),
    _RsBWMCurrentFilterName_Type()
)
rsBWMCurrentFilterName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMCurrentFilterName.setStatus("mandatory")


class _RsBWMCurrentFilterDescription_Type(DisplayString):
    """Custom type rsBWMCurrentFilterDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 29),
    )


_RsBWMCurrentFilterDescription_Type.__name__ = "DisplayString"
_RsBWMCurrentFilterDescription_Object = MibTableColumn
rsBWMCurrentFilterDescription = _RsBWMCurrentFilterDescription_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 16, 1, 2),
    _RsBWMCurrentFilterDescription_Type()
)
rsBWMCurrentFilterDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMCurrentFilterDescription.setStatus("mandatory")


class _RsBWMCurrentFilterProtocol_Type(Integer32):
    """Custom type rsBWMCurrentFilterProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("ip", 1),
          ("tcp", 2),
          ("udp", 3),
          ("icmp", 4),
          ("nonIp", 5),
          ("icmpv6", 6),
          ("sctp", 7))
    )


_RsBWMCurrentFilterProtocol_Type.__name__ = "Integer32"
_RsBWMCurrentFilterProtocol_Object = MibTableColumn
rsBWMCurrentFilterProtocol = _RsBWMCurrentFilterProtocol_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 16, 1, 3),
    _RsBWMCurrentFilterProtocol_Type()
)
rsBWMCurrentFilterProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMCurrentFilterProtocol.setStatus("mandatory")
_RsBWMCurrentFilterDestinationPort_Type = Integer32
_RsBWMCurrentFilterDestinationPort_Object = MibTableColumn
rsBWMCurrentFilterDestinationPort = _RsBWMCurrentFilterDestinationPort_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 16, 1, 4),
    _RsBWMCurrentFilterDestinationPort_Type()
)
rsBWMCurrentFilterDestinationPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMCurrentFilterDestinationPort.setStatus("mandatory")
_RsBWMCurrentFilterSourceFromPort_Type = Integer32
_RsBWMCurrentFilterSourceFromPort_Object = MibTableColumn
rsBWMCurrentFilterSourceFromPort = _RsBWMCurrentFilterSourceFromPort_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 16, 1, 5),
    _RsBWMCurrentFilterSourceFromPort_Type()
)
rsBWMCurrentFilterSourceFromPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMCurrentFilterSourceFromPort.setStatus("mandatory")
_RsBWMCurrentFilterSourceToPort_Type = Integer32
_RsBWMCurrentFilterSourceToPort_Object = MibTableColumn
rsBWMCurrentFilterSourceToPort = _RsBWMCurrentFilterSourceToPort_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 16, 1, 6),
    _RsBWMCurrentFilterSourceToPort_Type()
)
rsBWMCurrentFilterSourceToPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMCurrentFilterSourceToPort.setStatus("mandatory")
_RsBWMCurrentFilterOMPCOffset_Type = Integer32
_RsBWMCurrentFilterOMPCOffset_Object = MibTableColumn
rsBWMCurrentFilterOMPCOffset = _RsBWMCurrentFilterOMPCOffset_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 16, 1, 7),
    _RsBWMCurrentFilterOMPCOffset_Type()
)
rsBWMCurrentFilterOMPCOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMCurrentFilterOMPCOffset.setStatus("mandatory")


class _RsBWMCurrentFilterOMPCMask_Type(OctetString):
    """Custom type rsBWMCurrentFilterOMPCMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4


_RsBWMCurrentFilterOMPCMask_Type.__name__ = "OctetString"
_RsBWMCurrentFilterOMPCMask_Object = MibTableColumn
rsBWMCurrentFilterOMPCMask = _RsBWMCurrentFilterOMPCMask_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 16, 1, 8),
    _RsBWMCurrentFilterOMPCMask_Type()
)
rsBWMCurrentFilterOMPCMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMCurrentFilterOMPCMask.setStatus("mandatory")


class _RsBWMCurrentFilterOMPCPattern_Type(OctetString):
    """Custom type rsBWMCurrentFilterOMPCPattern based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4


_RsBWMCurrentFilterOMPCPattern_Type.__name__ = "OctetString"
_RsBWMCurrentFilterOMPCPattern_Object = MibTableColumn
rsBWMCurrentFilterOMPCPattern = _RsBWMCurrentFilterOMPCPattern_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 16, 1, 9),
    _RsBWMCurrentFilterOMPCPattern_Type()
)
rsBWMCurrentFilterOMPCPattern.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMCurrentFilterOMPCPattern.setStatus("mandatory")


class _RsBWMCurrentFilterOMPCCondition_Type(Integer32):
    """Custom type rsBWMCurrentFilterOMPCCondition based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("equal", 2),
          ("notEqual", 3),
          ("greaterThan", 4),
          ("lessThan", 5))
    )


_RsBWMCurrentFilterOMPCCondition_Type.__name__ = "Integer32"
_RsBWMCurrentFilterOMPCCondition_Object = MibTableColumn
rsBWMCurrentFilterOMPCCondition = _RsBWMCurrentFilterOMPCCondition_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 16, 1, 10),
    _RsBWMCurrentFilterOMPCCondition_Type()
)
rsBWMCurrentFilterOMPCCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMCurrentFilterOMPCCondition.setStatus("mandatory")


class _RsBWMCurrentFilterOMPCLength_Type(Integer32):
    """Custom type rsBWMCurrentFilterOMPCLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("oneByte", 1),
          ("twoBytes", 2),
          ("threeBytes", 3),
          ("fourBytes", 4),
          ("notApplicable", 5))
    )


_RsBWMCurrentFilterOMPCLength_Type.__name__ = "Integer32"
_RsBWMCurrentFilterOMPCLength_Object = MibTableColumn
rsBWMCurrentFilterOMPCLength = _RsBWMCurrentFilterOMPCLength_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 16, 1, 11),
    _RsBWMCurrentFilterOMPCLength_Type()
)
rsBWMCurrentFilterOMPCLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMCurrentFilterOMPCLength.setStatus("mandatory")
_RsBWMCurrentFilterContentOffset_Type = Integer32
_RsBWMCurrentFilterContentOffset_Object = MibTableColumn
rsBWMCurrentFilterContentOffset = _RsBWMCurrentFilterContentOffset_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 16, 1, 12),
    _RsBWMCurrentFilterContentOffset_Type()
)
rsBWMCurrentFilterContentOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMCurrentFilterContentOffset.setStatus("mandatory")


class _RsBWMCurrentFilterContent_Type(DisplayString):
    """Custom type rsBWMCurrentFilterContent based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_RsBWMCurrentFilterContent_Type.__name__ = "DisplayString"
_RsBWMCurrentFilterContent_Object = MibTableColumn
rsBWMCurrentFilterContent = _RsBWMCurrentFilterContent_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 16, 1, 13),
    _RsBWMCurrentFilterContent_Type()
)
rsBWMCurrentFilterContent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMCurrentFilterContent.setStatus("mandatory")


class _RsBWMCurrentFilterContentType_Type(Integer32):
    """Custom type rsBWMCurrentFilterContentType based on Integer32"""
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
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("url", 2),
          ("text", 3),
          ("hostname", 4),
          ("headertype", 5),
          ("expression", 6),
          ("maildomain", 7),
          ("mailto", 8),
          ("mailfrom", 9),
          ("mailsubject", 10),
          ("filetype", 11),
          ("cookiedata", 12),
          ("idsurl", 13),
          ("pop3user", 14),
          ("urilength", 15),
          ("ftp", 16),
          ("ftpcontent", 17),
          ("rpc", 18),
          ("dceRPC", 19),
          ("genericUrl", 20),
          ("genericHeader", 21),
          ("genericCookie", 22),
          ("sipcallfrom", 23),
          ("sipcallto", 24),
          ("sipcaller", 25))
    )


_RsBWMCurrentFilterContentType_Type.__name__ = "Integer32"
_RsBWMCurrentFilterContentType_Object = MibTableColumn
rsBWMCurrentFilterContentType = _RsBWMCurrentFilterContentType_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 16, 1, 14),
    _RsBWMCurrentFilterContentType_Type()
)
rsBWMCurrentFilterContentType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMCurrentFilterContentType.setStatus("mandatory")


class _RsBWMCurrentFilterType_Type(Integer32):
    """Custom type rsBWMCurrentFilterType based on Integer32"""
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
        *(("regular", 1),
          ("static", 2),
          ("ids", 3),
          ("idsStatic", 4))
    )


_RsBWMCurrentFilterType_Type.__name__ = "Integer32"
_RsBWMCurrentFilterType_Object = MibTableColumn
rsBWMCurrentFilterType = _RsBWMCurrentFilterType_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 16, 1, 15),
    _RsBWMCurrentFilterType_Type()
)
rsBWMCurrentFilterType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMCurrentFilterType.setStatus("mandatory")
_RsBWMCurrentFilterContentEnd_Type = Integer32
_RsBWMCurrentFilterContentEnd_Object = MibTableColumn
rsBWMCurrentFilterContentEnd = _RsBWMCurrentFilterContentEnd_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 16, 1, 16),
    _RsBWMCurrentFilterContentEnd_Type()
)
rsBWMCurrentFilterContentEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMCurrentFilterContentEnd.setStatus("mandatory")


class _RsBWMCurrentFilterContentData_Type(DisplayString):
    """Custom type rsBWMCurrentFilterContentData based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_RsBWMCurrentFilterContentData_Type.__name__ = "DisplayString"
_RsBWMCurrentFilterContentData_Object = MibTableColumn
rsBWMCurrentFilterContentData = _RsBWMCurrentFilterContentData_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 16, 1, 17),
    _RsBWMCurrentFilterContentData_Type()
)
rsBWMCurrentFilterContentData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMCurrentFilterContentData.setStatus("mandatory")


class _RsBWMCurrentFilterContentCoding_Type(Integer32):
    """Custom type rsBWMCurrentFilterContentCoding based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("caseInsensitive", 2),
          ("caseSensitive", 3),
          ("hex", 4),
          ("international", 5))
    )


_RsBWMCurrentFilterContentCoding_Type.__name__ = "Integer32"
_RsBWMCurrentFilterContentCoding_Object = MibTableColumn
rsBWMCurrentFilterContentCoding = _RsBWMCurrentFilterContentCoding_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 16, 1, 18),
    _RsBWMCurrentFilterContentCoding_Type()
)
rsBWMCurrentFilterContentCoding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMCurrentFilterContentCoding.setStatus("mandatory")


class _RsBWMCurrentFilterContentDataCoding_Type(Integer32):
    """Custom type rsBWMCurrentFilterContentDataCoding based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("caseInsensitive", 2),
          ("caseSensitive", 3),
          ("hex", 4),
          ("international", 5))
    )


_RsBWMCurrentFilterContentDataCoding_Type.__name__ = "Integer32"
_RsBWMCurrentFilterContentDataCoding_Object = MibTableColumn
rsBWMCurrentFilterContentDataCoding = _RsBWMCurrentFilterContentDataCoding_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 16, 1, 19),
    _RsBWMCurrentFilterContentDataCoding_Type()
)
rsBWMCurrentFilterContentDataCoding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMCurrentFilterContentDataCoding.setStatus("mandatory")


class _RsBWMCurrentFilterOMPCOffsetBase_Type(Integer32):
    """Custom type rsBWMCurrentFilterOMPCOffsetBase based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("ipHeader", 1),
          ("ipData", 2),
          ("tcpData", 3),
          ("asn1", 4),
          ("ethernet", 5),
          ("l4Header", 6),
          ("ipv6Header", 7))
    )


_RsBWMCurrentFilterOMPCOffsetBase_Type.__name__ = "Integer32"
_RsBWMCurrentFilterOMPCOffsetBase_Object = MibTableColumn
rsBWMCurrentFilterOMPCOffsetBase = _RsBWMCurrentFilterOMPCOffsetBase_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 16, 1, 20),
    _RsBWMCurrentFilterOMPCOffsetBase_Type()
)
rsBWMCurrentFilterOMPCOffsetBase.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMCurrentFilterOMPCOffsetBase.setStatus("mandatory")
_RsBWMCurrentFilterDestinationMaxPort_Type = Integer32
_RsBWMCurrentFilterDestinationMaxPort_Object = MibTableColumn
rsBWMCurrentFilterDestinationMaxPort = _RsBWMCurrentFilterDestinationMaxPort_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 16, 1, 21),
    _RsBWMCurrentFilterDestinationMaxPort_Type()
)
rsBWMCurrentFilterDestinationMaxPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMCurrentFilterDestinationMaxPort.setStatus("mandatory")


class _RsBWMCurrentFilterSourceAppPortGroup_Type(DisplayString):
    """Custom type rsBWMCurrentFilterSourceAppPortGroup based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 29),
    )


_RsBWMCurrentFilterSourceAppPortGroup_Type.__name__ = "DisplayString"
_RsBWMCurrentFilterSourceAppPortGroup_Object = MibTableColumn
rsBWMCurrentFilterSourceAppPortGroup = _RsBWMCurrentFilterSourceAppPortGroup_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 16, 1, 22),
    _RsBWMCurrentFilterSourceAppPortGroup_Type()
)
rsBWMCurrentFilterSourceAppPortGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMCurrentFilterSourceAppPortGroup.setStatus("mandatory")


class _RsBWMCurrentFilterDestinationAppPortGroup_Type(DisplayString):
    """Custom type rsBWMCurrentFilterDestinationAppPortGroup based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 29),
    )


_RsBWMCurrentFilterDestinationAppPortGroup_Type.__name__ = "DisplayString"
_RsBWMCurrentFilterDestinationAppPortGroup_Object = MibTableColumn
rsBWMCurrentFilterDestinationAppPortGroup = _RsBWMCurrentFilterDestinationAppPortGroup_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 16, 1, 23),
    _RsBWMCurrentFilterDestinationAppPortGroup_Type()
)
rsBWMCurrentFilterDestinationAppPortGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMCurrentFilterDestinationAppPortGroup.setStatus("mandatory")
_RsBWMCurrentFilterSessionType_Type = DpsSessionType
_RsBWMCurrentFilterSessionType_Object = MibTableColumn
rsBWMCurrentFilterSessionType = _RsBWMCurrentFilterSessionType_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 16, 1, 24),
    _RsBWMCurrentFilterSessionType_Type()
)
rsBWMCurrentFilterSessionType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMCurrentFilterSessionType.setStatus("mandatory")


class _RsBWMCurrentFilterSessionTypeDirection_Type(Integer32):
    """Custom type rsBWMCurrentFilterSessionTypeDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("all", 0),
          ("rqst", 1),
          ("rply", 2))
    )


_RsBWMCurrentFilterSessionTypeDirection_Type.__name__ = "Integer32"
_RsBWMCurrentFilterSessionTypeDirection_Object = MibTableColumn
rsBWMCurrentFilterSessionTypeDirection = _RsBWMCurrentFilterSessionTypeDirection_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 16, 1, 25),
    _RsBWMCurrentFilterSessionTypeDirection_Type()
)
rsBWMCurrentFilterSessionTypeDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMCurrentFilterSessionTypeDirection.setStatus("mandatory")
_RsBWMFilterGroupTable_Object = MibTable
rsBWMFilterGroupTable = _RsBWMFilterGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 17)
)
if mibBuilder.loadTexts:
    rsBWMFilterGroupTable.setStatus("mandatory")
_RsBWMFilterGroup_Object = MibTableRow
rsBWMFilterGroup = _RsBWMFilterGroup_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 17, 1)
)
rsBWMFilterGroup.setIndexNames(
    (0, "BWM-MIB", "rsBWMFilterGroupName"),
    (0, "BWM-MIB", "rsBWMFilterEntryName"),
)
if mibBuilder.loadTexts:
    rsBWMFilterGroup.setStatus("mandatory")


class _RsBWMFilterGroupName_Type(DisplayString):
    """Custom type rsBWMFilterGroupName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 29),
    )


_RsBWMFilterGroupName_Type.__name__ = "DisplayString"
_RsBWMFilterGroupName_Object = MibTableColumn
rsBWMFilterGroupName = _RsBWMFilterGroupName_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 17, 1, 1),
    _RsBWMFilterGroupName_Type()
)
rsBWMFilterGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMFilterGroupName.setStatus("mandatory")


class _RsBWMFilterEntryName_Type(DisplayString):
    """Custom type rsBWMFilterEntryName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 29),
    )


_RsBWMFilterEntryName_Type.__name__ = "DisplayString"
_RsBWMFilterEntryName_Object = MibTableColumn
rsBWMFilterEntryName = _RsBWMFilterEntryName_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 17, 1, 2),
    _RsBWMFilterEntryName_Type()
)
rsBWMFilterEntryName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMFilterEntryName.setStatus("mandatory")


class _RsBWMFilterGroupType_Type(Integer32):
    """Custom type rsBWMFilterGroupType based on Integer32"""
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
        *(("regular", 1),
          ("static", 2),
          ("ids", 3),
          ("idsStatic", 4))
    )


_RsBWMFilterGroupType_Type.__name__ = "Integer32"
_RsBWMFilterGroupType_Object = MibTableColumn
rsBWMFilterGroupType = _RsBWMFilterGroupType_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 17, 1, 3),
    _RsBWMFilterGroupType_Type()
)
rsBWMFilterGroupType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMFilterGroupType.setStatus("mandatory")
_RsBWMFilterGroupStatus_Type = RowStatus
_RsBWMFilterGroupStatus_Object = MibTableColumn
rsBWMFilterGroupStatus = _RsBWMFilterGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 17, 1, 4),
    _RsBWMFilterGroupStatus_Type()
)
rsBWMFilterGroupStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMFilterGroupStatus.setStatus("mandatory")
_RsBWMCurrentFilterGroupTable_Object = MibTable
rsBWMCurrentFilterGroupTable = _RsBWMCurrentFilterGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 18)
)
if mibBuilder.loadTexts:
    rsBWMCurrentFilterGroupTable.setStatus("mandatory")
_RsBWMCurrentFilterGroup_Object = MibTableRow
rsBWMCurrentFilterGroup = _RsBWMCurrentFilterGroup_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 18, 1)
)
rsBWMCurrentFilterGroup.setIndexNames(
    (0, "BWM-MIB", "rsBWMCurrentFilterGroupName"),
    (0, "BWM-MIB", "rsBWMCurrentFilterEntryName"),
)
if mibBuilder.loadTexts:
    rsBWMCurrentFilterGroup.setStatus("mandatory")


class _RsBWMCurrentFilterGroupName_Type(DisplayString):
    """Custom type rsBWMCurrentFilterGroupName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 29),
    )


_RsBWMCurrentFilterGroupName_Type.__name__ = "DisplayString"
_RsBWMCurrentFilterGroupName_Object = MibTableColumn
rsBWMCurrentFilterGroupName = _RsBWMCurrentFilterGroupName_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 18, 1, 1),
    _RsBWMCurrentFilterGroupName_Type()
)
rsBWMCurrentFilterGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMCurrentFilterGroupName.setStatus("mandatory")


class _RsBWMCurrentFilterEntryName_Type(DisplayString):
    """Custom type rsBWMCurrentFilterEntryName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 29),
    )


_RsBWMCurrentFilterEntryName_Type.__name__ = "DisplayString"
_RsBWMCurrentFilterEntryName_Object = MibTableColumn
rsBWMCurrentFilterEntryName = _RsBWMCurrentFilterEntryName_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 18, 1, 2),
    _RsBWMCurrentFilterEntryName_Type()
)
rsBWMCurrentFilterEntryName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMCurrentFilterEntryName.setStatus("mandatory")


class _RsBWMCurrentFilterGroupType_Type(Integer32):
    """Custom type rsBWMCurrentFilterGroupType based on Integer32"""
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
        *(("regular", 1),
          ("static", 2),
          ("ids", 3),
          ("idsStatic", 4))
    )


_RsBWMCurrentFilterGroupType_Type.__name__ = "Integer32"
_RsBWMCurrentFilterGroupType_Object = MibTableColumn
rsBWMCurrentFilterGroupType = _RsBWMCurrentFilterGroupType_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 18, 1, 3),
    _RsBWMCurrentFilterGroupType_Type()
)
rsBWMCurrentFilterGroupType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMCurrentFilterGroupType.setStatus("mandatory")
_RsBWMFilterPolicyTable_Object = MibTable
rsBWMFilterPolicyTable = _RsBWMFilterPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 19)
)
if mibBuilder.loadTexts:
    rsBWMFilterPolicyTable.setStatus("mandatory")
_RsBWMFilterPolicyEntry_Object = MibTableRow
rsBWMFilterPolicyEntry = _RsBWMFilterPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 19, 1)
)
rsBWMFilterPolicyEntry.setIndexNames(
    (0, "BWM-MIB", "rsBWMFilterPolicyName"),
    (0, "BWM-MIB", "rsBWMFilterPolicyEntryName"),
)
if mibBuilder.loadTexts:
    rsBWMFilterPolicyEntry.setStatus("mandatory")


class _RsBWMFilterPolicyName_Type(DisplayString):
    """Custom type rsBWMFilterPolicyName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 29),
    )


_RsBWMFilterPolicyName_Type.__name__ = "DisplayString"
_RsBWMFilterPolicyName_Object = MibTableColumn
rsBWMFilterPolicyName = _RsBWMFilterPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 19, 1, 1),
    _RsBWMFilterPolicyName_Type()
)
rsBWMFilterPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMFilterPolicyName.setStatus("mandatory")


class _RsBWMFilterPolicyEntryName_Type(DisplayString):
    """Custom type rsBWMFilterPolicyEntryName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 29),
    )


_RsBWMFilterPolicyEntryName_Type.__name__ = "DisplayString"
_RsBWMFilterPolicyEntryName_Object = MibTableColumn
rsBWMFilterPolicyEntryName = _RsBWMFilterPolicyEntryName_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 19, 1, 2),
    _RsBWMFilterPolicyEntryName_Type()
)
rsBWMFilterPolicyEntryName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMFilterPolicyEntryName.setStatus("mandatory")


class _RsBWMFilterPolicyType_Type(Integer32):
    """Custom type rsBWMFilterPolicyType based on Integer32"""
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
        *(("regular", 1),
          ("static", 2),
          ("ids", 3),
          ("idsStatic", 4))
    )


_RsBWMFilterPolicyType_Type.__name__ = "Integer32"
_RsBWMFilterPolicyType_Object = MibTableColumn
rsBWMFilterPolicyType = _RsBWMFilterPolicyType_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 19, 1, 3),
    _RsBWMFilterPolicyType_Type()
)
rsBWMFilterPolicyType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMFilterPolicyType.setStatus("mandatory")
_RsBWMFilterPolicyStatus_Type = RowStatus
_RsBWMFilterPolicyStatus_Object = MibTableColumn
rsBWMFilterPolicyStatus = _RsBWMFilterPolicyStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 19, 1, 4),
    _RsBWMFilterPolicyStatus_Type()
)
rsBWMFilterPolicyStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMFilterPolicyStatus.setStatus("mandatory")


class _RsBWMFilterPolicyEntryType_Type(Integer32):
    """Custom type rsBWMFilterPolicyEntryType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("basic", 1),
          ("advanced", 2))
    )


_RsBWMFilterPolicyEntryType_Type.__name__ = "Integer32"
_RsBWMFilterPolicyEntryType_Object = MibTableColumn
rsBWMFilterPolicyEntryType = _RsBWMFilterPolicyEntryType_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 19, 1, 5),
    _RsBWMFilterPolicyEntryType_Type()
)
rsBWMFilterPolicyEntryType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMFilterPolicyEntryType.setStatus("mandatory")
_RsBWMCurrentFilterPolicyTable_Object = MibTable
rsBWMCurrentFilterPolicyTable = _RsBWMCurrentFilterPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 20)
)
if mibBuilder.loadTexts:
    rsBWMCurrentFilterPolicyTable.setStatus("mandatory")
_RsBWMCurrentFilterPolicyEntry_Object = MibTableRow
rsBWMCurrentFilterPolicyEntry = _RsBWMCurrentFilterPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 20, 1)
)
rsBWMCurrentFilterPolicyEntry.setIndexNames(
    (0, "BWM-MIB", "rsBWMCurrentFilterPolicyName"),
    (0, "BWM-MIB", "rsBWMCurrentFilterPolicyEntryName"),
)
if mibBuilder.loadTexts:
    rsBWMCurrentFilterPolicyEntry.setStatus("mandatory")


class _RsBWMCurrentFilterPolicyName_Type(DisplayString):
    """Custom type rsBWMCurrentFilterPolicyName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 29),
    )


_RsBWMCurrentFilterPolicyName_Type.__name__ = "DisplayString"
_RsBWMCurrentFilterPolicyName_Object = MibTableColumn
rsBWMCurrentFilterPolicyName = _RsBWMCurrentFilterPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 20, 1, 1),
    _RsBWMCurrentFilterPolicyName_Type()
)
rsBWMCurrentFilterPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMCurrentFilterPolicyName.setStatus("mandatory")


class _RsBWMCurrentFilterPolicyEntryName_Type(DisplayString):
    """Custom type rsBWMCurrentFilterPolicyEntryName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 29),
    )


_RsBWMCurrentFilterPolicyEntryName_Type.__name__ = "DisplayString"
_RsBWMCurrentFilterPolicyEntryName_Object = MibTableColumn
rsBWMCurrentFilterPolicyEntryName = _RsBWMCurrentFilterPolicyEntryName_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 20, 1, 2),
    _RsBWMCurrentFilterPolicyEntryName_Type()
)
rsBWMCurrentFilterPolicyEntryName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMCurrentFilterPolicyEntryName.setStatus("mandatory")


class _RsBWMCurrentFilterPolicyType_Type(Integer32):
    """Custom type rsBWMCurrentFilterPolicyType based on Integer32"""
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
        *(("regular", 1),
          ("static", 2),
          ("ids", 3),
          ("idsStatic", 4))
    )


_RsBWMCurrentFilterPolicyType_Type.__name__ = "Integer32"
_RsBWMCurrentFilterPolicyType_Object = MibTableColumn
rsBWMCurrentFilterPolicyType = _RsBWMCurrentFilterPolicyType_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 20, 1, 3),
    _RsBWMCurrentFilterPolicyType_Type()
)
rsBWMCurrentFilterPolicyType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMCurrentFilterPolicyType.setStatus("mandatory")


class _RsBWMCurrentFilterPolicyEntryType_Type(Integer32):
    """Custom type rsBWMCurrentFilterPolicyEntryType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("basic", 1),
          ("advanced", 2))
    )


_RsBWMCurrentFilterPolicyEntryType_Type.__name__ = "Integer32"
_RsBWMCurrentFilterPolicyEntryType_Object = MibTableColumn
rsBWMCurrentFilterPolicyEntryType = _RsBWMCurrentFilterPolicyEntryType_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 20, 1, 4),
    _RsBWMCurrentFilterPolicyEntryType_Type()
)
rsBWMCurrentFilterPolicyEntryType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMCurrentFilterPolicyEntryType.setStatus("mandatory")


class _RsBWMApplicationClassification_Type(Integer32):
    """Custom type rsBWMApplicationClassification based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_RsBWMApplicationClassification_Type.__name__ = "Integer32"
_RsBWMApplicationClassification_Object = MibScalar
rsBWMApplicationClassification = _RsBWMApplicationClassification_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 21),
    _RsBWMApplicationClassification_Type()
)
rsBWMApplicationClassification.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMApplicationClassification.setStatus("mandatory")
_RsBWMPortBandwidthEntryTable_Object = MibTable
rsBWMPortBandwidthEntryTable = _RsBWMPortBandwidthEntryTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 22)
)
if mibBuilder.loadTexts:
    rsBWMPortBandwidthEntryTable.setStatus("mandatory")
_RsBWMPortBandwidthEntry_Object = MibTableRow
rsBWMPortBandwidthEntry = _RsBWMPortBandwidthEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 22, 1)
)
rsBWMPortBandwidthEntry.setIndexNames(
    (0, "BWM-MIB", "rsBWMPortIndex"),
)
if mibBuilder.loadTexts:
    rsBWMPortBandwidthEntry.setStatus("mandatory")
_RsBWMPortIndex_Type = Integer32
_RsBWMPortIndex_Object = MibTableColumn
rsBWMPortIndex = _RsBWMPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 22, 1, 1),
    _RsBWMPortIndex_Type()
)
rsBWMPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMPortIndex.setStatus("mandatory")
_RsBWMPortBandwidth_Type = Integer32
_RsBWMPortBandwidth_Object = MibTableColumn
rsBWMPortBandwidth = _RsBWMPortBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 22, 1, 2),
    _RsBWMPortBandwidth_Type()
)
rsBWMPortBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMPortBandwidth.setStatus("mandatory")
_RsBwmPortUsedBandwidth_Type = Integer32
_RsBwmPortUsedBandwidth_Object = MibTableColumn
rsBwmPortUsedBandwidth = _RsBwmPortUsedBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 22, 1, 3),
    _RsBwmPortUsedBandwidth_Type()
)
rsBwmPortUsedBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBwmPortUsedBandwidth.setStatus("mandatory")
_RsBWMTuning_ObjectIdentity = ObjectIdentity
rsBWMTuning = _RsBWMTuning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 23)
)
_RsBWMPolicyTuning_ObjectIdentity = ObjectIdentity
rsBWMPolicyTuning = _RsBWMPolicyTuning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 23, 1)
)
_RsBWMPolicyEntries_Type = Integer32
_RsBWMPolicyEntries_Object = MibScalar
rsBWMPolicyEntries = _RsBWMPolicyEntries_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 23, 1, 1),
    _RsBWMPolicyEntries_Type()
)
rsBWMPolicyEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMPolicyEntries.setStatus("mandatory")
_RsBWMPolicyEntriesAfterReset_Type = Integer32
_RsBWMPolicyEntriesAfterReset_Object = MibScalar
rsBWMPolicyEntriesAfterReset = _RsBWMPolicyEntriesAfterReset_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 23, 1, 2),
    _RsBWMPolicyEntriesAfterReset_Type()
)
rsBWMPolicyEntriesAfterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMPolicyEntriesAfterReset.setStatus("mandatory")
_RsBWMPolicyLeavesPercent_Type = Integer32
_RsBWMPolicyLeavesPercent_Object = MibScalar
rsBWMPolicyLeavesPercent = _RsBWMPolicyLeavesPercent_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 23, 1, 3),
    _RsBWMPolicyLeavesPercent_Type()
)
rsBWMPolicyLeavesPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMPolicyLeavesPercent.setStatus("mandatory")
_RsBWMPolicyLeavesPercentAfterReset_Type = Integer32
_RsBWMPolicyLeavesPercentAfterReset_Object = MibScalar
rsBWMPolicyLeavesPercentAfterReset = _RsBWMPolicyLeavesPercentAfterReset_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 23, 1, 4),
    _RsBWMPolicyLeavesPercentAfterReset_Type()
)
rsBWMPolicyLeavesPercentAfterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMPolicyLeavesPercentAfterReset.setStatus("mandatory")
_RsBWMNetworkTuning_ObjectIdentity = ObjectIdentity
rsBWMNetworkTuning = _RsBWMNetworkTuning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 23, 2)
)
_RsBWMNetworkEntries_Type = Integer32
_RsBWMNetworkEntries_Object = MibScalar
rsBWMNetworkEntries = _RsBWMNetworkEntries_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 23, 2, 1),
    _RsBWMNetworkEntries_Type()
)
rsBWMNetworkEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMNetworkEntries.setStatus("mandatory")
_RsBWMNetworkEntriesAfterReset_Type = Integer32
_RsBWMNetworkEntriesAfterReset_Object = MibScalar
rsBWMNetworkEntriesAfterReset = _RsBWMNetworkEntriesAfterReset_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 23, 2, 2),
    _RsBWMNetworkEntriesAfterReset_Type()
)
rsBWMNetworkEntriesAfterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMNetworkEntriesAfterReset.setStatus("mandatory")
_RsBWMFilterTuning_ObjectIdentity = ObjectIdentity
rsBWMFilterTuning = _RsBWMFilterTuning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 23, 3)
)
_RsBWMFilterEntries_Type = Integer32
_RsBWMFilterEntries_Object = MibScalar
rsBWMFilterEntries = _RsBWMFilterEntries_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 23, 3, 1),
    _RsBWMFilterEntries_Type()
)
rsBWMFilterEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMFilterEntries.setStatus("mandatory")
_RsBWMFilterEntriesAfterReset_Type = Integer32
_RsBWMFilterEntriesAfterReset_Object = MibScalar
rsBWMFilterEntriesAfterReset = _RsBWMFilterEntriesAfterReset_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 23, 3, 2),
    _RsBWMFilterEntriesAfterReset_Type()
)
rsBWMFilterEntriesAfterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMFilterEntriesAfterReset.setStatus("mandatory")
_RsBWMAdvancedTuning_ObjectIdentity = ObjectIdentity
rsBWMAdvancedTuning = _RsBWMAdvancedTuning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 23, 4)
)
_RsBWMAdvancedEntries_Type = Integer32
_RsBWMAdvancedEntries_Object = MibScalar
rsBWMAdvancedEntries = _RsBWMAdvancedEntries_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 23, 4, 1),
    _RsBWMAdvancedEntries_Type()
)
rsBWMAdvancedEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMAdvancedEntries.setStatus("mandatory")
_RsBWMAdvancedEntriesAfterReset_Type = Integer32
_RsBWMAdvancedEntriesAfterReset_Object = MibScalar
rsBWMAdvancedEntriesAfterReset = _RsBWMAdvancedEntriesAfterReset_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 23, 4, 2),
    _RsBWMAdvancedEntriesAfterReset_Type()
)
rsBWMAdvancedEntriesAfterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMAdvancedEntriesAfterReset.setStatus("mandatory")
_RsBWMGroupTuning_ObjectIdentity = ObjectIdentity
rsBWMGroupTuning = _RsBWMGroupTuning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 23, 5)
)
_RsBWMGroupEntries_Type = Integer32
_RsBWMGroupEntries_Object = MibScalar
rsBWMGroupEntries = _RsBWMGroupEntries_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 23, 5, 1),
    _RsBWMGroupEntries_Type()
)
rsBWMGroupEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMGroupEntries.setStatus("mandatory")
_RsBWMGroupEntriesAfterReset_Type = Integer32
_RsBWMGroupEntriesAfterReset_Object = MibScalar
rsBWMGroupEntriesAfterReset = _RsBWMGroupEntriesAfterReset_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 23, 5, 2),
    _RsBWMGroupEntriesAfterReset_Type()
)
rsBWMGroupEntriesAfterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMGroupEntriesAfterReset.setStatus("mandatory")
_RsBWMDestinationTuning_ObjectIdentity = ObjectIdentity
rsBWMDestinationTuning = _RsBWMDestinationTuning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 23, 6)
)
_RsBWMDestinationEntries_Type = Integer32
_RsBWMDestinationEntries_Object = MibScalar
rsBWMDestinationEntries = _RsBWMDestinationEntries_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 23, 6, 1),
    _RsBWMDestinationEntries_Type()
)
rsBWMDestinationEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMDestinationEntries.setStatus("mandatory")
_RsBWMDestinationEntriesAfterReset_Type = Integer32
_RsBWMDestinationEntriesAfterReset_Object = MibScalar
rsBWMDestinationEntriesAfterReset = _RsBWMDestinationEntriesAfterReset_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 23, 6, 2),
    _RsBWMDestinationEntriesAfterReset_Type()
)
rsBWMDestinationEntriesAfterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMDestinationEntriesAfterReset.setStatus("mandatory")
_RsBWMSessionTuning_ObjectIdentity = ObjectIdentity
rsBWMSessionTuning = _RsBWMSessionTuning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 23, 7)
)
_RsBWMSessionEntries_Type = Integer32
_RsBWMSessionEntries_Object = MibScalar
rsBWMSessionEntries = _RsBWMSessionEntries_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 23, 7, 1),
    _RsBWMSessionEntries_Type()
)
rsBWMSessionEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMSessionEntries.setStatus("mandatory")
_RsBWMSessionEntriesAfterReset_Type = Integer32
_RsBWMSessionEntriesAfterReset_Object = MibScalar
rsBWMSessionEntriesAfterReset = _RsBWMSessionEntriesAfterReset_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 23, 7, 2),
    _RsBWMSessionEntriesAfterReset_Type()
)
rsBWMSessionEntriesAfterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMSessionEntriesAfterReset.setStatus("mandatory")
_RsBWMChainTuning_ObjectIdentity = ObjectIdentity
rsBWMChainTuning = _RsBWMChainTuning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 23, 8)
)
_RsBWMMaxChainPolicies_Type = Integer32
_RsBWMMaxChainPolicies_Object = MibScalar
rsBWMMaxChainPolicies = _RsBWMMaxChainPolicies_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 23, 8, 1),
    _RsBWMMaxChainPolicies_Type()
)
rsBWMMaxChainPolicies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMMaxChainPolicies.setStatus("mandatory")
_RsBWMMaxChainPoliciesAfterReset_Type = Integer32
_RsBWMMaxChainPoliciesAfterReset_Object = MibScalar
rsBWMMaxChainPoliciesAfterReset = _RsBWMMaxChainPoliciesAfterReset_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 23, 8, 2),
    _RsBWMMaxChainPoliciesAfterReset_Type()
)
rsBWMMaxChainPoliciesAfterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMMaxChainPoliciesAfterReset.setStatus("mandatory")
_RsBWMContentTuning_ObjectIdentity = ObjectIdentity
rsBWMContentTuning = _RsBWMContentTuning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 23, 9)
)
_RsBWMContentEntries_Type = Integer32
_RsBWMContentEntries_Object = MibScalar
rsBWMContentEntries = _RsBWMContentEntries_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 23, 9, 1),
    _RsBWMContentEntries_Type()
)
rsBWMContentEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMContentEntries.setStatus("mandatory")
_RsBWMContentEntriesAfterReset_Type = Integer32
_RsBWMContentEntriesAfterReset_Object = MibScalar
rsBWMContentEntriesAfterReset = _RsBWMContentEntriesAfterReset_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 23, 9, 2),
    _RsBWMContentEntriesAfterReset_Type()
)
rsBWMContentEntriesAfterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMContentEntriesAfterReset.setStatus("mandatory")
_RsBWMNetworkIPTuning_ObjectIdentity = ObjectIdentity
rsBWMNetworkIPTuning = _RsBWMNetworkIPTuning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 23, 10)
)
_RsBWMNetworkIPHashEntries_Type = Integer32
_RsBWMNetworkIPHashEntries_Object = MibScalar
rsBWMNetworkIPHashEntries = _RsBWMNetworkIPHashEntries_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 23, 10, 1),
    _RsBWMNetworkIPHashEntries_Type()
)
rsBWMNetworkIPHashEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMNetworkIPHashEntries.setStatus("mandatory")
_RsBWMNetworkIPHashEntriesAfterReset_Type = Integer32
_RsBWMNetworkIPHashEntriesAfterReset_Object = MibScalar
rsBWMNetworkIPHashEntriesAfterReset = _RsBWMNetworkIPHashEntriesAfterReset_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 23, 10, 2),
    _RsBWMNetworkIPHashEntriesAfterReset_Type()
)
rsBWMNetworkIPHashEntriesAfterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMNetworkIPHashEntriesAfterReset.setStatus("mandatory")
_RsBWMNetworkRangeTuning_ObjectIdentity = ObjectIdentity
rsBWMNetworkRangeTuning = _RsBWMNetworkRangeTuning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 23, 11)
)
_RsBWMNetworkRangeEntries_Type = Integer32
_RsBWMNetworkRangeEntries_Object = MibScalar
rsBWMNetworkRangeEntries = _RsBWMNetworkRangeEntries_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 23, 11, 1),
    _RsBWMNetworkRangeEntries_Type()
)
rsBWMNetworkRangeEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMNetworkRangeEntries.setStatus("mandatory")
_RsBWMNetworkRangeEntriesAfterReset_Type = Integer32
_RsBWMNetworkRangeEntriesAfterReset_Object = MibScalar
rsBWMNetworkRangeEntriesAfterReset = _RsBWMNetworkRangeEntriesAfterReset_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 23, 11, 2),
    _RsBWMNetworkRangeEntriesAfterReset_Type()
)
rsBWMNetworkRangeEntriesAfterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMNetworkRangeEntriesAfterReset.setStatus("mandatory")
_RsBWMDynamicNetworkTuning_ObjectIdentity = ObjectIdentity
rsBWMDynamicNetworkTuning = _RsBWMDynamicNetworkTuning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 23, 12)
)
_RsBWMDynamicNetworkEntries_Type = Integer32
_RsBWMDynamicNetworkEntries_Object = MibScalar
rsBWMDynamicNetworkEntries = _RsBWMDynamicNetworkEntries_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 23, 12, 1),
    _RsBWMDynamicNetworkEntries_Type()
)
rsBWMDynamicNetworkEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMDynamicNetworkEntries.setStatus("mandatory")
_RsBWMDynamicNetworkEntriesAfterReset_Type = Integer32
_RsBWMDynamicNetworkEntriesAfterReset_Object = MibScalar
rsBWMDynamicNetworkEntriesAfterReset = _RsBWMDynamicNetworkEntriesAfterReset_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 23, 12, 2),
    _RsBWMDynamicNetworkEntriesAfterReset_Type()
)
rsBWMDynamicNetworkEntriesAfterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMDynamicNetworkEntriesAfterReset.setStatus("mandatory")
_RsBWMDynamicNetworkIPTuning_ObjectIdentity = ObjectIdentity
rsBWMDynamicNetworkIPTuning = _RsBWMDynamicNetworkIPTuning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 23, 13)
)
_RsBWMDynamicNetworkIPHashEntries_Type = Integer32
_RsBWMDynamicNetworkIPHashEntries_Object = MibScalar
rsBWMDynamicNetworkIPHashEntries = _RsBWMDynamicNetworkIPHashEntries_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 23, 13, 1),
    _RsBWMDynamicNetworkIPHashEntries_Type()
)
rsBWMDynamicNetworkIPHashEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMDynamicNetworkIPHashEntries.setStatus("mandatory")
_RsBWMDynamicNetworkIPHashEntriesAfterReset_Type = Integer32
_RsBWMDynamicNetworkIPHashEntriesAfterReset_Object = MibScalar
rsBWMDynamicNetworkIPHashEntriesAfterReset = _RsBWMDynamicNetworkIPHashEntriesAfterReset_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 23, 13, 2),
    _RsBWMDynamicNetworkIPHashEntriesAfterReset_Type()
)
rsBWMDynamicNetworkIPHashEntriesAfterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMDynamicNetworkIPHashEntriesAfterReset.setStatus("mandatory")
_RsBWMDynamicNetworkRangeTuning_ObjectIdentity = ObjectIdentity
rsBWMDynamicNetworkRangeTuning = _RsBWMDynamicNetworkRangeTuning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 23, 14)
)
_RsBWMDynamicNetworkRangeEntries_Type = Integer32
_RsBWMDynamicNetworkRangeEntries_Object = MibScalar
rsBWMDynamicNetworkRangeEntries = _RsBWMDynamicNetworkRangeEntries_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 23, 14, 1),
    _RsBWMDynamicNetworkRangeEntries_Type()
)
rsBWMDynamicNetworkRangeEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMDynamicNetworkRangeEntries.setStatus("mandatory")
_RsBWMDynamicNetworkRangeEntriesAfterReset_Type = Integer32
_RsBWMDynamicNetworkRangeEntriesAfterReset_Object = MibScalar
rsBWMDynamicNetworkRangeEntriesAfterReset = _RsBWMDynamicNetworkRangeEntriesAfterReset_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 23, 14, 2),
    _RsBWMDynamicNetworkRangeEntriesAfterReset_Type()
)
rsBWMDynamicNetworkRangeEntriesAfterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMDynamicNetworkRangeEntriesAfterReset.setStatus("mandatory")
_RsBWMMacGroupTuning_ObjectIdentity = ObjectIdentity
rsBWMMacGroupTuning = _RsBWMMacGroupTuning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 23, 15)
)
_RsBWMMacGroupEntries_Type = Integer32
_RsBWMMacGroupEntries_Object = MibScalar
rsBWMMacGroupEntries = _RsBWMMacGroupEntries_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 23, 15, 1),
    _RsBWMMacGroupEntries_Type()
)
rsBWMMacGroupEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMMacGroupEntries.setStatus("obsolete")
_RsBWMMacGroupEntriesAfterReset_Type = Integer32
_RsBWMMacGroupEntriesAfterReset_Object = MibScalar
rsBWMMacGroupEntriesAfterReset = _RsBWMMacGroupEntriesAfterReset_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 23, 15, 2),
    _RsBWMMacGroupEntriesAfterReset_Type()
)
rsBWMMacGroupEntriesAfterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMMacGroupEntriesAfterReset.setStatus("obsolete")
_RsBWMParallelStringSearchMemoryTuning_ObjectIdentity = ObjectIdentity
rsBWMParallelStringSearchMemoryTuning = _RsBWMParallelStringSearchMemoryTuning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 23, 18)
)
_RsBWMParallelStringSearchMemory_Type = Integer32
_RsBWMParallelStringSearchMemory_Object = MibScalar
rsBWMParallelStringSearchMemory = _RsBWMParallelStringSearchMemory_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 23, 18, 1),
    _RsBWMParallelStringSearchMemory_Type()
)
rsBWMParallelStringSearchMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMParallelStringSearchMemory.setStatus("mandatory")
_RsBWMParallelStringSearchMemoryAfterReset_Type = Integer32
_RsBWMParallelStringSearchMemoryAfterReset_Object = MibScalar
rsBWMParallelStringSearchMemoryAfterReset = _RsBWMParallelStringSearchMemoryAfterReset_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 23, 18, 2),
    _RsBWMParallelStringSearchMemoryAfterReset_Type()
)
rsBWMParallelStringSearchMemoryAfterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMParallelStringSearchMemoryAfterReset.setStatus("mandatory")
_RsBWMTrafficFlowBWTuning_ObjectIdentity = ObjectIdentity
rsBWMTrafficFlowBWTuning = _RsBWMTrafficFlowBWTuning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 23, 19)
)
_RsBWMTrafficFlowBWEntries_Type = Integer32
_RsBWMTrafficFlowBWEntries_Object = MibScalar
rsBWMTrafficFlowBWEntries = _RsBWMTrafficFlowBWEntries_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 23, 19, 1),
    _RsBWMTrafficFlowBWEntries_Type()
)
rsBWMTrafficFlowBWEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMTrafficFlowBWEntries.setStatus("mandatory")
_RsBWMTrafficFlowBWEntriesAfterReset_Type = Integer32
_RsBWMTrafficFlowBWEntriesAfterReset_Object = MibScalar
rsBWMTrafficFlowBWEntriesAfterReset = _RsBWMTrafficFlowBWEntriesAfterReset_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 23, 19, 2),
    _RsBWMTrafficFlowBWEntriesAfterReset_Type()
)
rsBWMTrafficFlowBWEntriesAfterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMTrafficFlowBWEntriesAfterReset.setStatus("mandatory")
_RsBWMAppPortGroupTuning_ObjectIdentity = ObjectIdentity
rsBWMAppPortGroupTuning = _RsBWMAppPortGroupTuning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 23, 20)
)
_RsBWMAppPortGroupTuningEntries_Type = Integer32
_RsBWMAppPortGroupTuningEntries_Object = MibScalar
rsBWMAppPortGroupTuningEntries = _RsBWMAppPortGroupTuningEntries_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 23, 20, 1),
    _RsBWMAppPortGroupTuningEntries_Type()
)
rsBWMAppPortGroupTuningEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMAppPortGroupTuningEntries.setStatus("mandatory")
_RsBWMAppPortGroupTuningEntriesAfterReset_Type = Integer32
_RsBWMAppPortGroupTuningEntriesAfterReset_Object = MibScalar
rsBWMAppPortGroupTuningEntriesAfterReset = _RsBWMAppPortGroupTuningEntriesAfterReset_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 23, 20, 2),
    _RsBWMAppPortGroupTuningEntriesAfterReset_Type()
)
rsBWMAppPortGroupTuningEntriesAfterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMAppPortGroupTuningEntriesAfterReset.setStatus("mandatory")
_RsBWMFarmsClassifyListsTuning_ObjectIdentity = ObjectIdentity
rsBWMFarmsClassifyListsTuning = _RsBWMFarmsClassifyListsTuning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 23, 21)
)
_RsBWMFarmsClassifyListsTuningEntries_Type = Integer32
_RsBWMFarmsClassifyListsTuningEntries_Object = MibScalar
rsBWMFarmsClassifyListsTuningEntries = _RsBWMFarmsClassifyListsTuningEntries_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 23, 21, 1),
    _RsBWMFarmsClassifyListsTuningEntries_Type()
)
rsBWMFarmsClassifyListsTuningEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMFarmsClassifyListsTuningEntries.setStatus("mandatory")
_RsBWMFarmsClassifyListsTuningEntriesAfterReset_Type = Integer32
_RsBWMFarmsClassifyListsTuningEntriesAfterReset_Object = MibScalar
rsBWMFarmsClassifyListsTuningEntriesAfterReset = _RsBWMFarmsClassifyListsTuningEntriesAfterReset_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 23, 21, 2),
    _RsBWMFarmsClassifyListsTuningEntriesAfterReset_Type()
)
rsBWMFarmsClassifyListsTuningEntriesAfterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMFarmsClassifyListsTuningEntriesAfterReset.setStatus("mandatory")
_RsBWMDSCPEntryTable_Object = MibTable
rsBWMDSCPEntryTable = _RsBWMDSCPEntryTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 24)
)
if mibBuilder.loadTexts:
    rsBWMDSCPEntryTable.setStatus("mandatory")
_RsBWMDSCPEntry_Object = MibTableRow
rsBWMDSCPEntry = _RsBWMDSCPEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 24, 1)
)
rsBWMDSCPEntry.setIndexNames(
    (0, "BWM-MIB", "rsBWMDSCP"),
)
if mibBuilder.loadTexts:
    rsBWMDSCPEntry.setStatus("mandatory")


class _RsBWMDSCP_Type(Integer32):
    """Custom type rsBWMDSCP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_RsBWMDSCP_Type.__name__ = "Integer32"
_RsBWMDSCP_Object = MibTableColumn
rsBWMDSCP = _RsBWMDSCP_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 24, 1, 1),
    _RsBWMDSCP_Type()
)
rsBWMDSCP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMDSCP.setStatus("mandatory")


class _RsBWMDSCPPriority_Type(Integer32):
    """Custom type rsBWMDSCPPriority based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(65535, 65535),
        ValueRangeConstraint(0, 7),
    )


_RsBWMDSCPPriority_Type.__name__ = "Integer32"
_RsBWMDSCPPriority_Object = MibTableColumn
rsBWMDSCPPriority = _RsBWMDSCPPriority_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 24, 1, 2),
    _RsBWMDSCPPriority_Type()
)
rsBWMDSCPPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMDSCPPriority.setStatus("mandatory")
_RsBWMDSCPGuaranteedBW_Type = Integer32
_RsBWMDSCPGuaranteedBW_Object = MibTableColumn
rsBWMDSCPGuaranteedBW = _RsBWMDSCPGuaranteedBW_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 24, 1, 3),
    _RsBWMDSCPGuaranteedBW_Type()
)
rsBWMDSCPGuaranteedBW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMDSCPGuaranteedBW.setStatus("mandatory")
_RsBWMDSCPMaxBW_Type = Integer32
_RsBWMDSCPMaxBW_Object = MibTableColumn
rsBWMDSCPMaxBW = _RsBWMDSCPMaxBW_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 24, 1, 4),
    _RsBWMDSCPMaxBW_Type()
)
rsBWMDSCPMaxBW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMDSCPMaxBW.setStatus("mandatory")
_RsBWMCurrentDSCPEntryTable_Object = MibTable
rsBWMCurrentDSCPEntryTable = _RsBWMCurrentDSCPEntryTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 25)
)
if mibBuilder.loadTexts:
    rsBWMCurrentDSCPEntryTable.setStatus("mandatory")
_RsBWMCurrentDSCPEntry_Object = MibTableRow
rsBWMCurrentDSCPEntry = _RsBWMCurrentDSCPEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 25, 1)
)
rsBWMCurrentDSCPEntry.setIndexNames(
    (0, "BWM-MIB", "rsBWMCurrentDSCP"),
)
if mibBuilder.loadTexts:
    rsBWMCurrentDSCPEntry.setStatus("mandatory")


class _RsBWMCurrentDSCP_Type(Integer32):
    """Custom type rsBWMCurrentDSCP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_RsBWMCurrentDSCP_Type.__name__ = "Integer32"
_RsBWMCurrentDSCP_Object = MibTableColumn
rsBWMCurrentDSCP = _RsBWMCurrentDSCP_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 25, 1, 1),
    _RsBWMCurrentDSCP_Type()
)
rsBWMCurrentDSCP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMCurrentDSCP.setStatus("mandatory")


class _RsBWMCurrentDSCPPriority_Type(Integer32):
    """Custom type rsBWMCurrentDSCPPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(65535, 65535),
        ValueRangeConstraint(0, 7),
    )


_RsBWMCurrentDSCPPriority_Type.__name__ = "Integer32"
_RsBWMCurrentDSCPPriority_Object = MibTableColumn
rsBWMCurrentDSCPPriority = _RsBWMCurrentDSCPPriority_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 25, 1, 2),
    _RsBWMCurrentDSCPPriority_Type()
)
rsBWMCurrentDSCPPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMCurrentDSCPPriority.setStatus("mandatory")
_RsBWMCurrentDSCPGuaranteedBW_Type = Counter32
_RsBWMCurrentDSCPGuaranteedBW_Object = MibTableColumn
rsBWMCurrentDSCPGuaranteedBW = _RsBWMCurrentDSCPGuaranteedBW_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 25, 1, 3),
    _RsBWMCurrentDSCPGuaranteedBW_Type()
)
rsBWMCurrentDSCPGuaranteedBW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMCurrentDSCPGuaranteedBW.setStatus("mandatory")
_RsBWMCurrentDSCPMaxBW_Type = Counter32
_RsBWMCurrentDSCPMaxBW_Object = MibTableColumn
rsBWMCurrentDSCPMaxBW = _RsBWMCurrentDSCPMaxBW_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 25, 1, 4),
    _RsBWMCurrentDSCPMaxBW_Type()
)
rsBWMCurrentDSCPMaxBW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMCurrentDSCPMaxBW.setStatus("mandatory")


class _RsBWMVersion_Type(DisplayString):
    """Custom type rsBWMVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_RsBWMVersion_Type.__name__ = "DisplayString"
_RsBWMVersion_Object = MibScalar
rsBWMVersion = _RsBWMVersion_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 26),
    _RsBWMVersion_Type()
)
rsBWMVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMVersion.setStatus("mandatory")
_RsBWMBwmPortOperationTable_Object = MibTable
rsBWMBwmPortOperationTable = _RsBWMBwmPortOperationTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 27)
)
if mibBuilder.loadTexts:
    rsBWMBwmPortOperationTable.setStatus("mandatory")
_RsBWMBwmPortOperationEntry_Object = MibTableRow
rsBWMBwmPortOperationEntry = _RsBWMBwmPortOperationEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 27, 1)
)
rsBWMBwmPortOperationEntry.setIndexNames(
    (0, "BWM-MIB", "rsBWMBwmInboundPort"),
    (0, "BWM-MIB", "rsBWMBwmOutboundPort"),
)
if mibBuilder.loadTexts:
    rsBWMBwmPortOperationEntry.setStatus("mandatory")
_RsBWMBwmInboundPort_Type = Integer32
_RsBWMBwmInboundPort_Object = MibTableColumn
rsBWMBwmInboundPort = _RsBWMBwmInboundPort_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 27, 1, 1),
    _RsBWMBwmInboundPort_Type()
)
rsBWMBwmInboundPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMBwmInboundPort.setStatus("mandatory")
_RsBWMBwmOutboundPort_Type = Integer32
_RsBWMBwmOutboundPort_Object = MibTableColumn
rsBWMBwmOutboundPort = _RsBWMBwmOutboundPort_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 27, 1, 2),
    _RsBWMBwmOutboundPort_Type()
)
rsBWMBwmOutboundPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMBwmOutboundPort.setStatus("mandatory")


class _RsBWMBwmDirection_Type(Integer32):
    """Custom type rsBWMBwmDirection based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("oneway", 1),
          ("twoway", 2))
    )


_RsBWMBwmDirection_Type.__name__ = "Integer32"
_RsBWMBwmDirection_Object = MibTableColumn
rsBWMBwmDirection = _RsBWMBwmDirection_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 27, 1, 3),
    _RsBWMBwmDirection_Type()
)
rsBWMBwmDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMBwmDirection.setStatus("mandatory")
_RsBWMBwmOperationStatus_Type = RowStatus
_RsBWMBwmOperationStatus_Object = MibTableColumn
rsBWMBwmOperationStatus = _RsBWMBwmOperationStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 27, 1, 4),
    _RsBWMBwmOperationStatus_Type()
)
rsBWMBwmOperationStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMBwmOperationStatus.setStatus("mandatory")
_RsBWMBwmVLANOperationTable_Object = MibTable
rsBWMBwmVLANOperationTable = _RsBWMBwmVLANOperationTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 28)
)
if mibBuilder.loadTexts:
    rsBWMBwmVLANOperationTable.setStatus("mandatory")
_RsBWMBwmVLANOperationEntry_Object = MibTableRow
rsBWMBwmVLANOperationEntry = _RsBWMBwmVLANOperationEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 28, 1)
)
rsBWMBwmVLANOperationEntry.setIndexNames(
    (0, "BWM-MIB", "rsBWMBwmVLAN"),
)
if mibBuilder.loadTexts:
    rsBWMBwmVLANOperationEntry.setStatus("mandatory")
_RsBWMBwmVLAN_Type = Integer32
_RsBWMBwmVLAN_Object = MibTableColumn
rsBWMBwmVLAN = _RsBWMBwmVLAN_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 28, 1, 1),
    _RsBWMBwmVLAN_Type()
)
rsBWMBwmVLAN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMBwmVLAN.setStatus("mandatory")
_RsBWMBwmVLANOperationStatus_Type = RowStatus
_RsBWMBwmVLANOperationStatus_Object = MibTableColumn
rsBWMBwmVLANOperationStatus = _RsBWMBwmVLANOperationStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 28, 1, 2),
    _RsBWMBwmVLANOperationStatus_Type()
)
rsBWMBwmVLANOperationStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMBwmVLANOperationStatus.setStatus("mandatory")
_RsBWMSessionAgingTime_Type = Integer32
_RsBWMSessionAgingTime_Object = MibScalar
rsBWMSessionAgingTime = _RsBWMSessionAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 29),
    _RsBWMSessionAgingTime_Type()
)
rsBWMSessionAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMSessionAgingTime.setStatus("mandatory")
_RsBWMStatisticsTable_Object = MibTable
rsBWMStatisticsTable = _RsBWMStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 30)
)
if mibBuilder.loadTexts:
    rsBWMStatisticsTable.setStatus("mandatory")
_RsBWMStatisticsEntry_Object = MibTableRow
rsBWMStatisticsEntry = _RsBWMStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 30, 1)
)
rsBWMStatisticsEntry.setIndexNames(
    (0, "BWM-MIB", "rsBWMStatisticsPolicyName"),
)
if mibBuilder.loadTexts:
    rsBWMStatisticsEntry.setStatus("mandatory")


class _RsBWMStatisticsPolicyName_Type(DisplayString):
    """Custom type rsBWMStatisticsPolicyName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_RsBWMStatisticsPolicyName_Type.__name__ = "DisplayString"
_RsBWMStatisticsPolicyName_Object = MibTableColumn
rsBWMStatisticsPolicyName = _RsBWMStatisticsPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 30, 1, 1),
    _RsBWMStatisticsPolicyName_Type()
)
rsBWMStatisticsPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMStatisticsPolicyName.setStatus("mandatory")
_RsBWMStatisticsBandwidthUsedLastSec_Type = Counter32
_RsBWMStatisticsBandwidthUsedLastSec_Object = MibTableColumn
rsBWMStatisticsBandwidthUsedLastSec = _RsBWMStatisticsBandwidthUsedLastSec_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 30, 1, 2),
    _RsBWMStatisticsBandwidthUsedLastSec_Type()
)
rsBWMStatisticsBandwidthUsedLastSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMStatisticsBandwidthUsedLastSec.setStatus("mandatory")
_RsBWMStatisticsPacketNumberLastSec_Type = Counter32
_RsBWMStatisticsPacketNumberLastSec_Object = MibTableColumn
rsBWMStatisticsPacketNumberLastSec = _RsBWMStatisticsPacketNumberLastSec_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 30, 1, 3),
    _RsBWMStatisticsPacketNumberLastSec_Type()
)
rsBWMStatisticsPacketNumberLastSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMStatisticsPacketNumberLastSec.setStatus("mandatory")
_RsBWMStatisticsFullQueueFailuresBWLastSec_Type = Counter32
_RsBWMStatisticsFullQueueFailuresBWLastSec_Object = MibTableColumn
rsBWMStatisticsFullQueueFailuresBWLastSec = _RsBWMStatisticsFullQueueFailuresBWLastSec_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 30, 1, 4),
    _RsBWMStatisticsFullQueueFailuresBWLastSec_Type()
)
rsBWMStatisticsFullQueueFailuresBWLastSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMStatisticsFullQueueFailuresBWLastSec.setStatus("mandatory")
_RsBWMStatisticsAgedPacketsFailuresBWLastSec_Type = Counter32
_RsBWMStatisticsAgedPacketsFailuresBWLastSec_Object = MibTableColumn
rsBWMStatisticsAgedPacketsFailuresBWLastSec = _RsBWMStatisticsAgedPacketsFailuresBWLastSec_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 30, 1, 5),
    _RsBWMStatisticsAgedPacketsFailuresBWLastSec_Type()
)
rsBWMStatisticsAgedPacketsFailuresBWLastSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMStatisticsAgedPacketsFailuresBWLastSec.setStatus("mandatory")
_RsBWMStatisticsGuaranteedReachedLastSec_Type = TruthValue
_RsBWMStatisticsGuaranteedReachedLastSec_Object = MibTableColumn
rsBWMStatisticsGuaranteedReachedLastSec = _RsBWMStatisticsGuaranteedReachedLastSec_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 30, 1, 6),
    _RsBWMStatisticsGuaranteedReachedLastSec_Type()
)
rsBWMStatisticsGuaranteedReachedLastSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMStatisticsGuaranteedReachedLastSec.setStatus("mandatory")
_RsBWMStatisticsMaximumReachedLastSec_Type = TruthValue
_RsBWMStatisticsMaximumReachedLastSec_Object = MibTableColumn
rsBWMStatisticsMaximumReachedLastSec = _RsBWMStatisticsMaximumReachedLastSec_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 30, 1, 7),
    _RsBWMStatisticsMaximumReachedLastSec_Type()
)
rsBWMStatisticsMaximumReachedLastSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMStatisticsMaximumReachedLastSec.setStatus("mandatory")
_RsBWMStatisticsBandwidthUsedLastPeriod_Type = Counter32
_RsBWMStatisticsBandwidthUsedLastPeriod_Object = MibTableColumn
rsBWMStatisticsBandwidthUsedLastPeriod = _RsBWMStatisticsBandwidthUsedLastPeriod_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 30, 1, 8),
    _RsBWMStatisticsBandwidthUsedLastPeriod_Type()
)
rsBWMStatisticsBandwidthUsedLastPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMStatisticsBandwidthUsedLastPeriod.setStatus("mandatory")
_RsBWMStatisticsPeakBandwidthLastPeriod_Type = Counter32
_RsBWMStatisticsPeakBandwidthLastPeriod_Object = MibTableColumn
rsBWMStatisticsPeakBandwidthLastPeriod = _RsBWMStatisticsPeakBandwidthLastPeriod_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 30, 1, 9),
    _RsBWMStatisticsPeakBandwidthLastPeriod_Type()
)
rsBWMStatisticsPeakBandwidthLastPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMStatisticsPeakBandwidthLastPeriod.setStatus("mandatory")
_RsBWMStatisticsPacketNumberLastPeriod_Type = Counter32
_RsBWMStatisticsPacketNumberLastPeriod_Object = MibTableColumn
rsBWMStatisticsPacketNumberLastPeriod = _RsBWMStatisticsPacketNumberLastPeriod_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 30, 1, 10),
    _RsBWMStatisticsPacketNumberLastPeriod_Type()
)
rsBWMStatisticsPacketNumberLastPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMStatisticsPacketNumberLastPeriod.setStatus("mandatory")
_RsBWMStatisticsFullQueueFailuresBWLastPeriod_Type = Counter32
_RsBWMStatisticsFullQueueFailuresBWLastPeriod_Object = MibTableColumn
rsBWMStatisticsFullQueueFailuresBWLastPeriod = _RsBWMStatisticsFullQueueFailuresBWLastPeriod_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 30, 1, 11),
    _RsBWMStatisticsFullQueueFailuresBWLastPeriod_Type()
)
rsBWMStatisticsFullQueueFailuresBWLastPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMStatisticsFullQueueFailuresBWLastPeriod.setStatus("mandatory")
_RsBWMStatisticsAgedPacketsFailuresBWLastPeriod_Type = Counter32
_RsBWMStatisticsAgedPacketsFailuresBWLastPeriod_Object = MibTableColumn
rsBWMStatisticsAgedPacketsFailuresBWLastPeriod = _RsBWMStatisticsAgedPacketsFailuresBWLastPeriod_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 30, 1, 12),
    _RsBWMStatisticsAgedPacketsFailuresBWLastPeriod_Type()
)
rsBWMStatisticsAgedPacketsFailuresBWLastPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMStatisticsAgedPacketsFailuresBWLastPeriod.setStatus("mandatory")
_RsBWMStatisticsGuaranteedReachedCounterLastPeriod_Type = Integer32
_RsBWMStatisticsGuaranteedReachedCounterLastPeriod_Object = MibTableColumn
rsBWMStatisticsGuaranteedReachedCounterLastPeriod = _RsBWMStatisticsGuaranteedReachedCounterLastPeriod_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 30, 1, 13),
    _RsBWMStatisticsGuaranteedReachedCounterLastPeriod_Type()
)
rsBWMStatisticsGuaranteedReachedCounterLastPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMStatisticsGuaranteedReachedCounterLastPeriod.setStatus("mandatory")
_RsBWMStatisticsMaximumReachedCounterLastPeriod_Type = Integer32
_RsBWMStatisticsMaximumReachedCounterLastPeriod_Object = MibTableColumn
rsBWMStatisticsMaximumReachedCounterLastPeriod = _RsBWMStatisticsMaximumReachedCounterLastPeriod_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 30, 1, 14),
    _RsBWMStatisticsMaximumReachedCounterLastPeriod_Type()
)
rsBWMStatisticsMaximumReachedCounterLastPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMStatisticsMaximumReachedCounterLastPeriod.setStatus("mandatory")
_RsBWMStatisticsMatchedBandwidthLastSec_Type = Counter32
_RsBWMStatisticsMatchedBandwidthLastSec_Object = MibTableColumn
rsBWMStatisticsMatchedBandwidthLastSec = _RsBWMStatisticsMatchedBandwidthLastSec_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 30, 1, 15),
    _RsBWMStatisticsMatchedBandwidthLastSec_Type()
)
rsBWMStatisticsMatchedBandwidthLastSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMStatisticsMatchedBandwidthLastSec.setStatus("mandatory")
_RsBWMStatisticsMatchedBandwidthLastPeriod_Type = Counter32
_RsBWMStatisticsMatchedBandwidthLastPeriod_Object = MibTableColumn
rsBWMStatisticsMatchedBandwidthLastPeriod = _RsBWMStatisticsMatchedBandwidthLastPeriod_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 30, 1, 16),
    _RsBWMStatisticsMatchedBandwidthLastPeriod_Type()
)
rsBWMStatisticsMatchedBandwidthLastPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMStatisticsMatchedBandwidthLastPeriod.setStatus("mandatory")
_RsBWMStatisticsInboundBandwidthUsedLastSec_Type = Counter32
_RsBWMStatisticsInboundBandwidthUsedLastSec_Object = MibTableColumn
rsBWMStatisticsInboundBandwidthUsedLastSec = _RsBWMStatisticsInboundBandwidthUsedLastSec_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 30, 1, 17),
    _RsBWMStatisticsInboundBandwidthUsedLastSec_Type()
)
rsBWMStatisticsInboundBandwidthUsedLastSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMStatisticsInboundBandwidthUsedLastSec.setStatus("mandatory")
_RsBWMStatisticsInboundBandwidthUsedLastPeriod_Type = Counter32
_RsBWMStatisticsInboundBandwidthUsedLastPeriod_Object = MibTableColumn
rsBWMStatisticsInboundBandwidthUsedLastPeriod = _RsBWMStatisticsInboundBandwidthUsedLastPeriod_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 30, 1, 18),
    _RsBWMStatisticsInboundBandwidthUsedLastPeriod_Type()
)
rsBWMStatisticsInboundBandwidthUsedLastPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMStatisticsInboundBandwidthUsedLastPeriod.setStatus("mandatory")
_RsBWMStatisticsInboundMatchedBandwidthLastSec_Type = Counter32
_RsBWMStatisticsInboundMatchedBandwidthLastSec_Object = MibTableColumn
rsBWMStatisticsInboundMatchedBandwidthLastSec = _RsBWMStatisticsInboundMatchedBandwidthLastSec_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 30, 1, 19),
    _RsBWMStatisticsInboundMatchedBandwidthLastSec_Type()
)
rsBWMStatisticsInboundMatchedBandwidthLastSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMStatisticsInboundMatchedBandwidthLastSec.setStatus("mandatory")
_RsBWMStatisticsInboundMatchedBandwidthLastPeriod_Type = Counter32
_RsBWMStatisticsInboundMatchedBandwidthLastPeriod_Object = MibTableColumn
rsBWMStatisticsInboundMatchedBandwidthLastPeriod = _RsBWMStatisticsInboundMatchedBandwidthLastPeriod_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 30, 1, 20),
    _RsBWMStatisticsInboundMatchedBandwidthLastPeriod_Type()
)
rsBWMStatisticsInboundMatchedBandwidthLastPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMStatisticsInboundMatchedBandwidthLastPeriod.setStatus("mandatory")
_RsBWMStatisticsInboundPacketNumberLastSec_Type = Counter32
_RsBWMStatisticsInboundPacketNumberLastSec_Object = MibTableColumn
rsBWMStatisticsInboundPacketNumberLastSec = _RsBWMStatisticsInboundPacketNumberLastSec_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 30, 1, 21),
    _RsBWMStatisticsInboundPacketNumberLastSec_Type()
)
rsBWMStatisticsInboundPacketNumberLastSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMStatisticsInboundPacketNumberLastSec.setStatus("mandatory")
_RsBWMStatisticsInboundPacketNumberLastPeriod_Type = Counter32
_RsBWMStatisticsInboundPacketNumberLastPeriod_Object = MibTableColumn
rsBWMStatisticsInboundPacketNumberLastPeriod = _RsBWMStatisticsInboundPacketNumberLastPeriod_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 30, 1, 22),
    _RsBWMStatisticsInboundPacketNumberLastPeriod_Type()
)
rsBWMStatisticsInboundPacketNumberLastPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMStatisticsInboundPacketNumberLastPeriod.setStatus("mandatory")
_RsBWMStatisticsOutboundBandwidthUsedLastSec_Type = Counter32
_RsBWMStatisticsOutboundBandwidthUsedLastSec_Object = MibTableColumn
rsBWMStatisticsOutboundBandwidthUsedLastSec = _RsBWMStatisticsOutboundBandwidthUsedLastSec_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 30, 1, 23),
    _RsBWMStatisticsOutboundBandwidthUsedLastSec_Type()
)
rsBWMStatisticsOutboundBandwidthUsedLastSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMStatisticsOutboundBandwidthUsedLastSec.setStatus("mandatory")
_RsBWMStatisticsOutboundBandwidthUsedLastPeriod_Type = Counter32
_RsBWMStatisticsOutboundBandwidthUsedLastPeriod_Object = MibTableColumn
rsBWMStatisticsOutboundBandwidthUsedLastPeriod = _RsBWMStatisticsOutboundBandwidthUsedLastPeriod_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 30, 1, 24),
    _RsBWMStatisticsOutboundBandwidthUsedLastPeriod_Type()
)
rsBWMStatisticsOutboundBandwidthUsedLastPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMStatisticsOutboundBandwidthUsedLastPeriod.setStatus("mandatory")
_RsBWMStatisticsOutboundMatchedBandwidthLastSec_Type = Counter32
_RsBWMStatisticsOutboundMatchedBandwidthLastSec_Object = MibTableColumn
rsBWMStatisticsOutboundMatchedBandwidthLastSec = _RsBWMStatisticsOutboundMatchedBandwidthLastSec_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 30, 1, 25),
    _RsBWMStatisticsOutboundMatchedBandwidthLastSec_Type()
)
rsBWMStatisticsOutboundMatchedBandwidthLastSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMStatisticsOutboundMatchedBandwidthLastSec.setStatus("mandatory")
_RsBWMStatisticsOutboundMatchedBandwidthLastPeriod_Type = Counter32
_RsBWMStatisticsOutboundMatchedBandwidthLastPeriod_Object = MibTableColumn
rsBWMStatisticsOutboundMatchedBandwidthLastPeriod = _RsBWMStatisticsOutboundMatchedBandwidthLastPeriod_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 30, 1, 26),
    _RsBWMStatisticsOutboundMatchedBandwidthLastPeriod_Type()
)
rsBWMStatisticsOutboundMatchedBandwidthLastPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMStatisticsOutboundMatchedBandwidthLastPeriod.setStatus("mandatory")
_RsBWMStatisticsOutboundPacketNumberLastSec_Type = Counter32
_RsBWMStatisticsOutboundPacketNumberLastSec_Object = MibTableColumn
rsBWMStatisticsOutboundPacketNumberLastSec = _RsBWMStatisticsOutboundPacketNumberLastSec_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 30, 1, 27),
    _RsBWMStatisticsOutboundPacketNumberLastSec_Type()
)
rsBWMStatisticsOutboundPacketNumberLastSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMStatisticsOutboundPacketNumberLastSec.setStatus("mandatory")
_RsBWMStatisticsOutboundPacketNumberLastPeriod_Type = Counter32
_RsBWMStatisticsOutboundPacketNumberLastPeriod_Object = MibTableColumn
rsBWMStatisticsOutboundPacketNumberLastPeriod = _RsBWMStatisticsOutboundPacketNumberLastPeriod_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 30, 1, 28),
    _RsBWMStatisticsOutboundPacketNumberLastPeriod_Type()
)
rsBWMStatisticsOutboundPacketNumberLastPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMStatisticsOutboundPacketNumberLastPeriod.setStatus("mandatory")
_RsBWMStatisticsNewTCPConnectionsLastSec_Type = Counter32
_RsBWMStatisticsNewTCPConnectionsLastSec_Object = MibTableColumn
rsBWMStatisticsNewTCPConnectionsLastSec = _RsBWMStatisticsNewTCPConnectionsLastSec_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 30, 1, 29),
    _RsBWMStatisticsNewTCPConnectionsLastSec_Type()
)
rsBWMStatisticsNewTCPConnectionsLastSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMStatisticsNewTCPConnectionsLastSec.setStatus("mandatory")
_RsBWMStatisticsNewTCPConnectionsLastPeriod_Type = Counter32
_RsBWMStatisticsNewTCPConnectionsLastPeriod_Object = MibTableColumn
rsBWMStatisticsNewTCPConnectionsLastPeriod = _RsBWMStatisticsNewTCPConnectionsLastPeriod_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 30, 1, 30),
    _RsBWMStatisticsNewTCPConnectionsLastPeriod_Type()
)
rsBWMStatisticsNewTCPConnectionsLastPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMStatisticsNewTCPConnectionsLastPeriod.setStatus("mandatory")
_RsBWMStatisticsNewUDPConnectionsLastSec_Type = Counter32
_RsBWMStatisticsNewUDPConnectionsLastSec_Object = MibTableColumn
rsBWMStatisticsNewUDPConnectionsLastSec = _RsBWMStatisticsNewUDPConnectionsLastSec_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 30, 1, 31),
    _RsBWMStatisticsNewUDPConnectionsLastSec_Type()
)
rsBWMStatisticsNewUDPConnectionsLastSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMStatisticsNewUDPConnectionsLastSec.setStatus("mandatory")
_RsBWMStatisticsNewUDPConnectionsLastPeriod_Type = Counter32
_RsBWMStatisticsNewUDPConnectionsLastPeriod_Object = MibTableColumn
rsBWMStatisticsNewUDPConnectionsLastPeriod = _RsBWMStatisticsNewUDPConnectionsLastPeriod_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 30, 1, 32),
    _RsBWMStatisticsNewUDPConnectionsLastPeriod_Type()
)
rsBWMStatisticsNewUDPConnectionsLastPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMStatisticsNewUDPConnectionsLastPeriod.setStatus("mandatory")
_RsBWMStatisticsQueuedBWLastSec_Type = Counter32
_RsBWMStatisticsQueuedBWLastSec_Object = MibTableColumn
rsBWMStatisticsQueuedBWLastSec = _RsBWMStatisticsQueuedBWLastSec_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 30, 1, 33),
    _RsBWMStatisticsQueuedBWLastSec_Type()
)
rsBWMStatisticsQueuedBWLastSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMStatisticsQueuedBWLastSec.setStatus("mandatory")
_RsBWMStatisticsQueuedBWLastPeriod_Type = Counter32
_RsBWMStatisticsQueuedBWLastPeriod_Object = MibTableColumn
rsBWMStatisticsQueuedBWLastPeriod = _RsBWMStatisticsQueuedBWLastPeriod_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 30, 1, 34),
    _RsBWMStatisticsQueuedBWLastPeriod_Type()
)
rsBWMStatisticsQueuedBWLastPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMStatisticsQueuedBWLastPeriod.setStatus("mandatory")


class _RsBWMStatisticsMonitorPolicy_Type(Integer32):
    """Custom type rsBWMStatisticsMonitorPolicy based on Integer32"""
    defaultValue = 2

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


_RsBWMStatisticsMonitorPolicy_Type.__name__ = "Integer32"
_RsBWMStatisticsMonitorPolicy_Object = MibScalar
rsBWMStatisticsMonitorPolicy = _RsBWMStatisticsMonitorPolicy_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 30, 2),
    _RsBWMStatisticsMonitorPolicy_Type()
)
rsBWMStatisticsMonitorPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMStatisticsMonitorPolicy.setStatus("mandatory")


class _RsBWMStatisticsTableUseSRP_Type(TruthValue):
    """Custom type rsBWMStatisticsTableUseSRP based on TruthValue"""
    defaultValue = 2


_RsBWMStatisticsTableUseSRP_Type.__name__ = "TruthValue"
_RsBWMStatisticsTableUseSRP_Object = MibScalar
rsBWMStatisticsTableUseSRP = _RsBWMStatisticsTableUseSRP_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 30, 3),
    _RsBWMStatisticsTableUseSRP_Type()
)
rsBWMStatisticsTableUseSRP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMStatisticsTableUseSRP.setStatus("mandatory")


class _RsBWMStatisticsReportingPeriod_Type(Integer32):
    """Custom type rsBWMStatisticsReportingPeriod based on Integer32"""
    defaultValue = 60


_RsBWMStatisticsReportingPeriod_Type.__name__ = "Integer32"
_RsBWMStatisticsReportingPeriod_Object = MibScalar
rsBWMStatisticsReportingPeriod = _RsBWMStatisticsReportingPeriod_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 30, 4),
    _RsBWMStatisticsReportingPeriod_Type()
)
rsBWMStatisticsReportingPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMStatisticsReportingPeriod.setStatus("mandatory")


class _RsBWMSamplingRatio_Type(Integer32):
    """Custom type rsBWMSamplingRatio based on Integer32"""
    defaultValue = 100


_RsBWMSamplingRatio_Type.__name__ = "Integer32"
_RsBWMSamplingRatio_Object = MibScalar
rsBWMSamplingRatio = _RsBWMSamplingRatio_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 31),
    _RsBWMSamplingRatio_Type()
)
rsBWMSamplingRatio.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMSamplingRatio.setStatus("mandatory")


class _RsBWMSamplerOverloadMode_Type(Integer32):
    """Custom type rsBWMSamplerOverloadMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("forward", 1),
          ("discard", 2))
    )


_RsBWMSamplerOverloadMode_Type.__name__ = "Integer32"
_RsBWMSamplerOverloadMode_Object = MibScalar
rsBWMSamplerOverloadMode = _RsBWMSamplerOverloadMode_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 32),
    _RsBWMSamplerOverloadMode_Type()
)
rsBWMSamplerOverloadMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMSamplerOverloadMode.setStatus("mandatory")
_RsBWMChainRulesTable_Object = MibTable
rsBWMChainRulesTable = _RsBWMChainRulesTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 33)
)
if mibBuilder.loadTexts:
    rsBWMChainRulesTable.setStatus("mandatory")
_RsBWMChainRulesEntry_Object = MibTableRow
rsBWMChainRulesEntry = _RsBWMChainRulesEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 33, 1)
)
rsBWMChainRulesEntry.setIndexNames(
    (0, "BWM-MIB", "rsBWMChainRulesName"),
)
if mibBuilder.loadTexts:
    rsBWMChainRulesEntry.setStatus("mandatory")


class _RsBWMChainRulesIndex_Type(Integer32):
    """Custom type rsBWMChainRulesIndex based on Integer32"""
    defaultValue = 1


_RsBWMChainRulesIndex_Type.__name__ = "Integer32"
_RsBWMChainRulesIndex_Object = MibTableColumn
rsBWMChainRulesIndex = _RsBWMChainRulesIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 33, 1, 1),
    _RsBWMChainRulesIndex_Type()
)
rsBWMChainRulesIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMChainRulesIndex.setStatus("mandatory")


class _RsBWMChainRulesName_Type(DisplayString):
    """Custom type rsBWMChainRulesName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_RsBWMChainRulesName_Type.__name__ = "DisplayString"
_RsBWMChainRulesName_Object = MibTableColumn
rsBWMChainRulesName = _RsBWMChainRulesName_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 33, 1, 2),
    _RsBWMChainRulesName_Type()
)
rsBWMChainRulesName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMChainRulesName.setStatus("mandatory")


class _RsBWMChainRulesDestination_Type(DisplayString):
    """Custom type rsBWMChainRulesDestination based on DisplayString"""
    defaultValue = OctetString("any")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 46),
    )


_RsBWMChainRulesDestination_Type.__name__ = "DisplayString"
_RsBWMChainRulesDestination_Object = MibTableColumn
rsBWMChainRulesDestination = _RsBWMChainRulesDestination_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 33, 1, 3),
    _RsBWMChainRulesDestination_Type()
)
rsBWMChainRulesDestination.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMChainRulesDestination.setStatus("mandatory")


class _RsBWMChainRulesSource_Type(DisplayString):
    """Custom type rsBWMChainRulesSource based on DisplayString"""
    defaultValue = OctetString("any")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 46),
    )


_RsBWMChainRulesSource_Type.__name__ = "DisplayString"
_RsBWMChainRulesSource_Object = MibTableColumn
rsBWMChainRulesSource = _RsBWMChainRulesSource_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 33, 1, 4),
    _RsBWMChainRulesSource_Type()
)
rsBWMChainRulesSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMChainRulesSource.setStatus("mandatory")
_RsBWMChainRulesStatus_Type = RowStatus
_RsBWMChainRulesStatus_Object = MibTableColumn
rsBWMChainRulesStatus = _RsBWMChainRulesStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 33, 1, 5),
    _RsBWMChainRulesStatus_Type()
)
rsBWMChainRulesStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMChainRulesStatus.setStatus("mandatory")


class _RsBWMChainRulesDirection_Type(Integer32):
    """Custom type rsBWMChainRulesDirection based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("oneway", 1),
          ("twoway", 2))
    )


_RsBWMChainRulesDirection_Type.__name__ = "Integer32"
_RsBWMChainRulesDirection_Object = MibTableColumn
rsBWMChainRulesDirection = _RsBWMChainRulesDirection_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 33, 1, 6),
    _RsBWMChainRulesDirection_Type()
)
rsBWMChainRulesDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMChainRulesDirection.setStatus("mandatory")


class _RsBWMChainRulesDescription_Type(DisplayString):
    """Custom type rsBWMChainRulesDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 19),
    )


_RsBWMChainRulesDescription_Type.__name__ = "DisplayString"
_RsBWMChainRulesDescription_Object = MibTableColumn
rsBWMChainRulesDescription = _RsBWMChainRulesDescription_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 33, 1, 7),
    _RsBWMChainRulesDescription_Type()
)
rsBWMChainRulesDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMChainRulesDescription.setStatus("mandatory")


class _RsBWMChainRulesPolicyType_Type(Integer32):
    """Custom type rsBWMChainRulesPolicyType based on Integer32"""
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
        *(("none", 1),
          ("filter", 2),
          ("group", 3),
          ("policy", 4))
    )


_RsBWMChainRulesPolicyType_Type.__name__ = "Integer32"
_RsBWMChainRulesPolicyType_Object = MibTableColumn
rsBWMChainRulesPolicyType = _RsBWMChainRulesPolicyType_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 33, 1, 8),
    _RsBWMChainRulesPolicyType_Type()
)
rsBWMChainRulesPolicyType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMChainRulesPolicyType.setStatus("mandatory")


class _RsBWMChainRulesPolicy_Type(DisplayString):
    """Custom type rsBWMChainRulesPolicy based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 29),
    )


_RsBWMChainRulesPolicy_Type.__name__ = "DisplayString"
_RsBWMChainRulesPolicy_Object = MibTableColumn
rsBWMChainRulesPolicy = _RsBWMChainRulesPolicy_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 33, 1, 9),
    _RsBWMChainRulesPolicy_Type()
)
rsBWMChainRulesPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMChainRulesPolicy.setStatus("mandatory")


class _RsBWMChainRulesOperationalStatus_Type(Integer32):
    """Custom type rsBWMChainRulesOperationalStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_RsBWMChainRulesOperationalStatus_Type.__name__ = "Integer32"
_RsBWMChainRulesOperationalStatus_Object = MibTableColumn
rsBWMChainRulesOperationalStatus = _RsBWMChainRulesOperationalStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 33, 1, 10),
    _RsBWMChainRulesOperationalStatus_Type()
)
rsBWMChainRulesOperationalStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMChainRulesOperationalStatus.setStatus("mandatory")


class _RsBWMChainRulesSpecific_Type(DisplayString):
    """Custom type rsBWMChainRulesSpecific based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 19),
    )


_RsBWMChainRulesSpecific_Type.__name__ = "DisplayString"
_RsBWMChainRulesSpecific_Object = MibTableColumn
rsBWMChainRulesSpecific = _RsBWMChainRulesSpecific_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 33, 1, 11),
    _RsBWMChainRulesSpecific_Type()
)
rsBWMChainRulesSpecific.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMChainRulesSpecific.setStatus("mandatory")


class _RsBWMChainRulesPhysicalPortGroup_Type(DisplayString):
    """Custom type rsBWMChainRulesPhysicalPortGroup based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 19),
    )


_RsBWMChainRulesPhysicalPortGroup_Type.__name__ = "DisplayString"
_RsBWMChainRulesPhysicalPortGroup_Object = MibTableColumn
rsBWMChainRulesPhysicalPortGroup = _RsBWMChainRulesPhysicalPortGroup_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 33, 1, 12),
    _RsBWMChainRulesPhysicalPortGroup_Type()
)
rsBWMChainRulesPhysicalPortGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMChainRulesPhysicalPortGroup.setStatus("mandatory")


class _RsBWMChainRulesVLANTagGroup_Type(DisplayString):
    """Custom type rsBWMChainRulesVLANTagGroup based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 19),
    )


_RsBWMChainRulesVLANTagGroup_Type.__name__ = "DisplayString"
_RsBWMChainRulesVLANTagGroup_Object = MibTableColumn
rsBWMChainRulesVLANTagGroup = _RsBWMChainRulesVLANTagGroup_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 33, 1, 13),
    _RsBWMChainRulesVLANTagGroup_Type()
)
rsBWMChainRulesVLANTagGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMChainRulesVLANTagGroup.setStatus("mandatory")


class _RsBWMChainRulesDSCPMarking_Type(Integer32):
    """Custom type rsBWMChainRulesDSCPMarking based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 63),
    )


_RsBWMChainRulesDSCPMarking_Type.__name__ = "Integer32"
_RsBWMChainRulesDSCPMarking_Object = MibTableColumn
rsBWMChainRulesDSCPMarking = _RsBWMChainRulesDSCPMarking_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 33, 1, 14),
    _RsBWMChainRulesDSCPMarking_Type()
)
rsBWMChainRulesDSCPMarking.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMChainRulesDSCPMarking.setStatus("mandatory")


class _RsBWMChainRulesRadiusRule_Type(DisplayString):
    """Custom type rsBWMChainRulesRadiusRule based on DisplayString"""
    defaultValue = OctetString("any")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_RsBWMChainRulesRadiusRule_Type.__name__ = "DisplayString"
_RsBWMChainRulesRadiusRule_Object = MibTableColumn
rsBWMChainRulesRadiusRule = _RsBWMChainRulesRadiusRule_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 33, 1, 15),
    _RsBWMChainRulesRadiusRule_Type()
)
rsBWMChainRulesRadiusRule.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMChainRulesRadiusRule.setStatus("mandatory")
_RsBWMCurrentChainRulesTable_Object = MibTable
rsBWMCurrentChainRulesTable = _RsBWMCurrentChainRulesTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 34)
)
if mibBuilder.loadTexts:
    rsBWMCurrentChainRulesTable.setStatus("mandatory")
_RsBWMCurrentChainRulesEntry_Object = MibTableRow
rsBWMCurrentChainRulesEntry = _RsBWMCurrentChainRulesEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 34, 1)
)
rsBWMCurrentChainRulesEntry.setIndexNames(
    (0, "BWM-MIB", "rsBWMCurrentChainRulesName"),
)
if mibBuilder.loadTexts:
    rsBWMCurrentChainRulesEntry.setStatus("mandatory")
_RsBWMCurrentChainRulesIndex_Type = Integer32
_RsBWMCurrentChainRulesIndex_Object = MibTableColumn
rsBWMCurrentChainRulesIndex = _RsBWMCurrentChainRulesIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 34, 1, 1),
    _RsBWMCurrentChainRulesIndex_Type()
)
rsBWMCurrentChainRulesIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMCurrentChainRulesIndex.setStatus("mandatory")


class _RsBWMCurrentChainRulesName_Type(DisplayString):
    """Custom type rsBWMCurrentChainRulesName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_RsBWMCurrentChainRulesName_Type.__name__ = "DisplayString"
_RsBWMCurrentChainRulesName_Object = MibTableColumn
rsBWMCurrentChainRulesName = _RsBWMCurrentChainRulesName_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 34, 1, 2),
    _RsBWMCurrentChainRulesName_Type()
)
rsBWMCurrentChainRulesName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMCurrentChainRulesName.setStatus("mandatory")


class _RsBWMCurrentChainRulesDestination_Type(DisplayString):
    """Custom type rsBWMCurrentChainRulesDestination based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 46),
    )


_RsBWMCurrentChainRulesDestination_Type.__name__ = "DisplayString"
_RsBWMCurrentChainRulesDestination_Object = MibTableColumn
rsBWMCurrentChainRulesDestination = _RsBWMCurrentChainRulesDestination_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 34, 1, 3),
    _RsBWMCurrentChainRulesDestination_Type()
)
rsBWMCurrentChainRulesDestination.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMCurrentChainRulesDestination.setStatus("mandatory")


class _RsBWMCurrentChainRulesSource_Type(DisplayString):
    """Custom type rsBWMCurrentChainRulesSource based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 46),
    )


_RsBWMCurrentChainRulesSource_Type.__name__ = "DisplayString"
_RsBWMCurrentChainRulesSource_Object = MibTableColumn
rsBWMCurrentChainRulesSource = _RsBWMCurrentChainRulesSource_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 34, 1, 4),
    _RsBWMCurrentChainRulesSource_Type()
)
rsBWMCurrentChainRulesSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMCurrentChainRulesSource.setStatus("mandatory")


class _RsBWMCurrentChainRulesDirection_Type(Integer32):
    """Custom type rsBWMCurrentChainRulesDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("oneway", 1),
          ("twoway", 2))
    )


_RsBWMCurrentChainRulesDirection_Type.__name__ = "Integer32"
_RsBWMCurrentChainRulesDirection_Object = MibTableColumn
rsBWMCurrentChainRulesDirection = _RsBWMCurrentChainRulesDirection_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 34, 1, 5),
    _RsBWMCurrentChainRulesDirection_Type()
)
rsBWMCurrentChainRulesDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMCurrentChainRulesDirection.setStatus("mandatory")


class _RsBWMCurrentChainRulesDescription_Type(DisplayString):
    """Custom type rsBWMCurrentChainRulesDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 19),
    )


_RsBWMCurrentChainRulesDescription_Type.__name__ = "DisplayString"
_RsBWMCurrentChainRulesDescription_Object = MibTableColumn
rsBWMCurrentChainRulesDescription = _RsBWMCurrentChainRulesDescription_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 34, 1, 6),
    _RsBWMCurrentChainRulesDescription_Type()
)
rsBWMCurrentChainRulesDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMCurrentChainRulesDescription.setStatus("mandatory")


class _RsBWMCurrentChainRulesPolicyType_Type(Integer32):
    """Custom type rsBWMCurrentChainRulesPolicyType based on Integer32"""
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
        *(("none", 1),
          ("filter", 2),
          ("group", 3),
          ("policy", 4))
    )


_RsBWMCurrentChainRulesPolicyType_Type.__name__ = "Integer32"
_RsBWMCurrentChainRulesPolicyType_Object = MibTableColumn
rsBWMCurrentChainRulesPolicyType = _RsBWMCurrentChainRulesPolicyType_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 34, 1, 7),
    _RsBWMCurrentChainRulesPolicyType_Type()
)
rsBWMCurrentChainRulesPolicyType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMCurrentChainRulesPolicyType.setStatus("mandatory")


class _RsBWMCurrentChainRulesPolicy_Type(DisplayString):
    """Custom type rsBWMCurrentChainRulesPolicy based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 29),
    )


_RsBWMCurrentChainRulesPolicy_Type.__name__ = "DisplayString"
_RsBWMCurrentChainRulesPolicy_Object = MibTableColumn
rsBWMCurrentChainRulesPolicy = _RsBWMCurrentChainRulesPolicy_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 34, 1, 8),
    _RsBWMCurrentChainRulesPolicy_Type()
)
rsBWMCurrentChainRulesPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMCurrentChainRulesPolicy.setStatus("mandatory")


class _RsBWMCurrentChainRulesSpecific_Type(DisplayString):
    """Custom type rsBWMCurrentChainRulesSpecific based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 19),
    )


_RsBWMCurrentChainRulesSpecific_Type.__name__ = "DisplayString"
_RsBWMCurrentChainRulesSpecific_Object = MibTableColumn
rsBWMCurrentChainRulesSpecific = _RsBWMCurrentChainRulesSpecific_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 34, 1, 9),
    _RsBWMCurrentChainRulesSpecific_Type()
)
rsBWMCurrentChainRulesSpecific.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMCurrentChainRulesSpecific.setStatus("mandatory")
_RsBWMCurrentChainBandwidthLastSec_Type = Counter32
_RsBWMCurrentChainBandwidthLastSec_Object = MibTableColumn
rsBWMCurrentChainBandwidthLastSec = _RsBWMCurrentChainBandwidthLastSec_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 34, 1, 10),
    _RsBWMCurrentChainBandwidthLastSec_Type()
)
rsBWMCurrentChainBandwidthLastSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMCurrentChainBandwidthLastSec.setStatus("mandatory")
_RsBWMCurrentChainPacketsLastSec_Type = Counter32
_RsBWMCurrentChainPacketsLastSec_Object = MibTableColumn
rsBWMCurrentChainPacketsLastSec = _RsBWMCurrentChainPacketsLastSec_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 34, 1, 11),
    _RsBWMCurrentChainPacketsLastSec_Type()
)
rsBWMCurrentChainPacketsLastSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMCurrentChainPacketsLastSec.setStatus("mandatory")


class _RsBWMCurrentChainRulesPhysicalPortGroup_Type(DisplayString):
    """Custom type rsBWMCurrentChainRulesPhysicalPortGroup based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 19),
    )


_RsBWMCurrentChainRulesPhysicalPortGroup_Type.__name__ = "DisplayString"
_RsBWMCurrentChainRulesPhysicalPortGroup_Object = MibTableColumn
rsBWMCurrentChainRulesPhysicalPortGroup = _RsBWMCurrentChainRulesPhysicalPortGroup_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 34, 1, 12),
    _RsBWMCurrentChainRulesPhysicalPortGroup_Type()
)
rsBWMCurrentChainRulesPhysicalPortGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMCurrentChainRulesPhysicalPortGroup.setStatus("mandatory")


class _RsBWMCurrentChainRulesVLANTagGroup_Type(DisplayString):
    """Custom type rsBWMCurrentChainRulesVLANTagGroup based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 19),
    )


_RsBWMCurrentChainRulesVLANTagGroup_Type.__name__ = "DisplayString"
_RsBWMCurrentChainRulesVLANTagGroup_Object = MibTableColumn
rsBWMCurrentChainRulesVLANTagGroup = _RsBWMCurrentChainRulesVLANTagGroup_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 34, 1, 13),
    _RsBWMCurrentChainRulesVLANTagGroup_Type()
)
rsBWMCurrentChainRulesVLANTagGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMCurrentChainRulesVLANTagGroup.setStatus("mandatory")


class _RsBWMCurrentChainRulesDSCPMarking_Type(Integer32):
    """Custom type rsBWMCurrentChainRulesDSCPMarking based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 63),
    )


_RsBWMCurrentChainRulesDSCPMarking_Type.__name__ = "Integer32"
_RsBWMCurrentChainRulesDSCPMarking_Object = MibTableColumn
rsBWMCurrentChainRulesDSCPMarking = _RsBWMCurrentChainRulesDSCPMarking_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 34, 1, 14),
    _RsBWMCurrentChainRulesDSCPMarking_Type()
)
rsBWMCurrentChainRulesDSCPMarking.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMCurrentChainRulesDSCPMarking.setStatus("mandatory")


class _RsBWMCurrentChainRulesRadiusRule_Type(DisplayString):
    """Custom type rsBWMCurrentChainRulesRadiusRule based on DisplayString"""
    defaultValue = OctetString("any")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_RsBWMCurrentChainRulesRadiusRule_Type.__name__ = "DisplayString"
_RsBWMCurrentChainRulesRadiusRule_Object = MibTableColumn
rsBWMCurrentChainRulesRadiusRule = _RsBWMCurrentChainRulesRadiusRule_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 34, 1, 15),
    _RsBWMCurrentChainRulesRadiusRule_Type()
)
rsBWMCurrentChainRulesRadiusRule.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMCurrentChainRulesRadiusRule.setStatus("mandatory")
_RsBWMPPCInboundPortOnlyTable_Object = MibTable
rsBWMPPCInboundPortOnlyTable = _RsBWMPPCInboundPortOnlyTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 35)
)
if mibBuilder.loadTexts:
    rsBWMPPCInboundPortOnlyTable.setStatus("mandatory")
_RsBWMPPCInboundPortOnlyEntry_Object = MibTableRow
rsBWMPPCInboundPortOnlyEntry = _RsBWMPPCInboundPortOnlyEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 35, 1)
)
rsBWMPPCInboundPortOnlyEntry.setIndexNames(
    (0, "BWM-MIB", "rsBWMPPCInboundPort"),
)
if mibBuilder.loadTexts:
    rsBWMPPCInboundPortOnlyEntry.setStatus("mandatory")
_RsBWMPPCInboundPort_Type = Integer32
_RsBWMPPCInboundPort_Object = MibTableColumn
rsBWMPPCInboundPort = _RsBWMPPCInboundPort_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 35, 1, 1),
    _RsBWMPPCInboundPort_Type()
)
rsBWMPPCInboundPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMPPCInboundPort.setStatus("mandatory")
_RsBWMPPCOperationStatus_Type = RowStatus
_RsBWMPPCOperationStatus_Object = MibTableColumn
rsBWMPPCOperationStatus = _RsBWMPPCOperationStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 35, 1, 2),
    _RsBWMPPCOperationStatus_Type()
)
rsBWMPPCOperationStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMPPCOperationStatus.setStatus("mandatory")
_RsBWMPhysicalPortGroupTable_Object = MibTable
rsBWMPhysicalPortGroupTable = _RsBWMPhysicalPortGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 36)
)
if mibBuilder.loadTexts:
    rsBWMPhysicalPortGroupTable.setStatus("mandatory")
_RsBWMPhysicalPortGroupEntry_Object = MibTableRow
rsBWMPhysicalPortGroupEntry = _RsBWMPhysicalPortGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 36, 1)
)
rsBWMPhysicalPortGroupEntry.setIndexNames(
    (0, "BWM-MIB", "rsBWMPhysicalPortGroupName"),
    (0, "BWM-MIB", "rsBWMPhysicalPortGroupPort"),
)
if mibBuilder.loadTexts:
    rsBWMPhysicalPortGroupEntry.setStatus("mandatory")


class _RsBWMPhysicalPortGroupName_Type(DisplayString):
    """Custom type rsBWMPhysicalPortGroupName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 19),
    )


_RsBWMPhysicalPortGroupName_Type.__name__ = "DisplayString"
_RsBWMPhysicalPortGroupName_Object = MibTableColumn
rsBWMPhysicalPortGroupName = _RsBWMPhysicalPortGroupName_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 36, 1, 1),
    _RsBWMPhysicalPortGroupName_Type()
)
rsBWMPhysicalPortGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMPhysicalPortGroupName.setStatus("mandatory")
_RsBWMPhysicalPortGroupPort_Type = Integer32
_RsBWMPhysicalPortGroupPort_Object = MibTableColumn
rsBWMPhysicalPortGroupPort = _RsBWMPhysicalPortGroupPort_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 36, 1, 2),
    _RsBWMPhysicalPortGroupPort_Type()
)
rsBWMPhysicalPortGroupPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMPhysicalPortGroupPort.setStatus("mandatory")
_RsBWMPhysicalPortGroupOperationStatus_Type = RowStatus
_RsBWMPhysicalPortGroupOperationStatus_Object = MibTableColumn
rsBWMPhysicalPortGroupOperationStatus = _RsBWMPhysicalPortGroupOperationStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 36, 1, 3),
    _RsBWMPhysicalPortGroupOperationStatus_Type()
)
rsBWMPhysicalPortGroupOperationStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMPhysicalPortGroupOperationStatus.setStatus("mandatory")
_RsBWMCurrentPhysicalPortGroupTable_Object = MibTable
rsBWMCurrentPhysicalPortGroupTable = _RsBWMCurrentPhysicalPortGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 37)
)
if mibBuilder.loadTexts:
    rsBWMCurrentPhysicalPortGroupTable.setStatus("mandatory")
_RsBWMCurrentPhysicalPortGroupEntry_Object = MibTableRow
rsBWMCurrentPhysicalPortGroupEntry = _RsBWMCurrentPhysicalPortGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 37, 1)
)
rsBWMCurrentPhysicalPortGroupEntry.setIndexNames(
    (0, "BWM-MIB", "rsBWMCurrentPhysicalPortGroupName"),
    (0, "BWM-MIB", "rsBWMCurrentPhysicalPortGroupPort"),
)
if mibBuilder.loadTexts:
    rsBWMCurrentPhysicalPortGroupEntry.setStatus("mandatory")


class _RsBWMCurrentPhysicalPortGroupName_Type(DisplayString):
    """Custom type rsBWMCurrentPhysicalPortGroupName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 19),
    )


_RsBWMCurrentPhysicalPortGroupName_Type.__name__ = "DisplayString"
_RsBWMCurrentPhysicalPortGroupName_Object = MibTableColumn
rsBWMCurrentPhysicalPortGroupName = _RsBWMCurrentPhysicalPortGroupName_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 37, 1, 1),
    _RsBWMCurrentPhysicalPortGroupName_Type()
)
rsBWMCurrentPhysicalPortGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMCurrentPhysicalPortGroupName.setStatus("mandatory")
_RsBWMCurrentPhysicalPortGroupPort_Type = Integer32
_RsBWMCurrentPhysicalPortGroupPort_Object = MibTableColumn
rsBWMCurrentPhysicalPortGroupPort = _RsBWMCurrentPhysicalPortGroupPort_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 37, 1, 2),
    _RsBWMCurrentPhysicalPortGroupPort_Type()
)
rsBWMCurrentPhysicalPortGroupPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMCurrentPhysicalPortGroupPort.setStatus("mandatory")
_RsBWMFarmRulesTable_Object = MibTable
rsBWMFarmRulesTable = _RsBWMFarmRulesTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 38)
)
if mibBuilder.loadTexts:
    rsBWMFarmRulesTable.setStatus("mandatory")
_RsBWMFarmRulesEntry_Object = MibTableRow
rsBWMFarmRulesEntry = _RsBWMFarmRulesEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 38, 1)
)
rsBWMFarmRulesEntry.setIndexNames(
    (0, "BWM-MIB", "rsBWMFarmRulesName"),
)
if mibBuilder.loadTexts:
    rsBWMFarmRulesEntry.setStatus("mandatory")
_RsBWMFarmRulesIndex_Type = Integer32
_RsBWMFarmRulesIndex_Object = MibTableColumn
rsBWMFarmRulesIndex = _RsBWMFarmRulesIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 38, 1, 1),
    _RsBWMFarmRulesIndex_Type()
)
rsBWMFarmRulesIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMFarmRulesIndex.setStatus("mandatory")


class _RsBWMFarmRulesName_Type(DisplayString):
    """Custom type rsBWMFarmRulesName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_RsBWMFarmRulesName_Type.__name__ = "DisplayString"
_RsBWMFarmRulesName_Object = MibTableColumn
rsBWMFarmRulesName = _RsBWMFarmRulesName_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 38, 1, 2),
    _RsBWMFarmRulesName_Type()
)
rsBWMFarmRulesName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMFarmRulesName.setStatus("mandatory")


class _RsBWMFarmRulesDestination_Type(DisplayString):
    """Custom type rsBWMFarmRulesDestination based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 46),
    )


_RsBWMFarmRulesDestination_Type.__name__ = "DisplayString"
_RsBWMFarmRulesDestination_Object = MibTableColumn
rsBWMFarmRulesDestination = _RsBWMFarmRulesDestination_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 38, 1, 3),
    _RsBWMFarmRulesDestination_Type()
)
rsBWMFarmRulesDestination.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMFarmRulesDestination.setStatus("mandatory")


class _RsBWMFarmRulesSource_Type(DisplayString):
    """Custom type rsBWMFarmRulesSource based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 46),
    )


_RsBWMFarmRulesSource_Type.__name__ = "DisplayString"
_RsBWMFarmRulesSource_Object = MibTableColumn
rsBWMFarmRulesSource = _RsBWMFarmRulesSource_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 38, 1, 4),
    _RsBWMFarmRulesSource_Type()
)
rsBWMFarmRulesSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMFarmRulesSource.setStatus("mandatory")
_RsBWMFarmRulesStatus_Type = RowStatus
_RsBWMFarmRulesStatus_Object = MibTableColumn
rsBWMFarmRulesStatus = _RsBWMFarmRulesStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 38, 1, 5),
    _RsBWMFarmRulesStatus_Type()
)
rsBWMFarmRulesStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMFarmRulesStatus.setStatus("mandatory")


class _RsBWMFarmRulesDirection_Type(Integer32):
    """Custom type rsBWMFarmRulesDirection based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("oneway", 1),
          ("twoway", 2))
    )


_RsBWMFarmRulesDirection_Type.__name__ = "Integer32"
_RsBWMFarmRulesDirection_Object = MibTableColumn
rsBWMFarmRulesDirection = _RsBWMFarmRulesDirection_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 38, 1, 6),
    _RsBWMFarmRulesDirection_Type()
)
rsBWMFarmRulesDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMFarmRulesDirection.setStatus("mandatory")


class _RsBWMFarmRulesDescription_Type(DisplayString):
    """Custom type rsBWMFarmRulesDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 19),
    )


_RsBWMFarmRulesDescription_Type.__name__ = "DisplayString"
_RsBWMFarmRulesDescription_Object = MibTableColumn
rsBWMFarmRulesDescription = _RsBWMFarmRulesDescription_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 38, 1, 7),
    _RsBWMFarmRulesDescription_Type()
)
rsBWMFarmRulesDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMFarmRulesDescription.setStatus("mandatory")


class _RsBWMFarmRulesPolicyType_Type(Integer32):
    """Custom type rsBWMFarmRulesPolicyType based on Integer32"""
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
        *(("none", 1),
          ("filter", 2),
          ("group", 3),
          ("policy", 4))
    )


_RsBWMFarmRulesPolicyType_Type.__name__ = "Integer32"
_RsBWMFarmRulesPolicyType_Object = MibTableColumn
rsBWMFarmRulesPolicyType = _RsBWMFarmRulesPolicyType_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 38, 1, 8),
    _RsBWMFarmRulesPolicyType_Type()
)
rsBWMFarmRulesPolicyType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMFarmRulesPolicyType.setStatus("mandatory")


class _RsBWMFarmRulesPolicy_Type(DisplayString):
    """Custom type rsBWMFarmRulesPolicy based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 29),
    )


_RsBWMFarmRulesPolicy_Type.__name__ = "DisplayString"
_RsBWMFarmRulesPolicy_Object = MibTableColumn
rsBWMFarmRulesPolicy = _RsBWMFarmRulesPolicy_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 38, 1, 9),
    _RsBWMFarmRulesPolicy_Type()
)
rsBWMFarmRulesPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMFarmRulesPolicy.setStatus("mandatory")


class _RsBWMFarmRulesOperationalStatus_Type(Integer32):
    """Custom type rsBWMFarmRulesOperationalStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_RsBWMFarmRulesOperationalStatus_Type.__name__ = "Integer32"
_RsBWMFarmRulesOperationalStatus_Object = MibTableColumn
rsBWMFarmRulesOperationalStatus = _RsBWMFarmRulesOperationalStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 38, 1, 10),
    _RsBWMFarmRulesOperationalStatus_Type()
)
rsBWMFarmRulesOperationalStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMFarmRulesOperationalStatus.setStatus("mandatory")


class _RsBWMFarmRulesSpecific_Type(DisplayString):
    """Custom type rsBWMFarmRulesSpecific based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 19),
    )


_RsBWMFarmRulesSpecific_Type.__name__ = "DisplayString"
_RsBWMFarmRulesSpecific_Object = MibTableColumn
rsBWMFarmRulesSpecific = _RsBWMFarmRulesSpecific_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 38, 1, 11),
    _RsBWMFarmRulesSpecific_Type()
)
rsBWMFarmRulesSpecific.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMFarmRulesSpecific.setStatus("mandatory")


class _RsBWMFarmRulesPhysicalPortGroup_Type(DisplayString):
    """Custom type rsBWMFarmRulesPhysicalPortGroup based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 19),
    )


_RsBWMFarmRulesPhysicalPortGroup_Type.__name__ = "DisplayString"
_RsBWMFarmRulesPhysicalPortGroup_Object = MibTableColumn
rsBWMFarmRulesPhysicalPortGroup = _RsBWMFarmRulesPhysicalPortGroup_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 38, 1, 12),
    _RsBWMFarmRulesPhysicalPortGroup_Type()
)
rsBWMFarmRulesPhysicalPortGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMFarmRulesPhysicalPortGroup.setStatus("mandatory")


class _RsBWMFarmRulesVLANTagGroup_Type(DisplayString):
    """Custom type rsBWMFarmRulesVLANTagGroup based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 19),
    )


_RsBWMFarmRulesVLANTagGroup_Type.__name__ = "DisplayString"
_RsBWMFarmRulesVLANTagGroup_Object = MibTableColumn
rsBWMFarmRulesVLANTagGroup = _RsBWMFarmRulesVLANTagGroup_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 38, 1, 13),
    _RsBWMFarmRulesVLANTagGroup_Type()
)
rsBWMFarmRulesVLANTagGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMFarmRulesVLANTagGroup.setStatus("mandatory")


class _RsBWMFarmRulesDSCPMarking_Type(Integer32):
    """Custom type rsBWMFarmRulesDSCPMarking based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 63),
    )


_RsBWMFarmRulesDSCPMarking_Type.__name__ = "Integer32"
_RsBWMFarmRulesDSCPMarking_Object = MibTableColumn
rsBWMFarmRulesDSCPMarking = _RsBWMFarmRulesDSCPMarking_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 38, 1, 14),
    _RsBWMFarmRulesDSCPMarking_Type()
)
rsBWMFarmRulesDSCPMarking.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMFarmRulesDSCPMarking.setStatus("mandatory")
_RsBWMCurrentFarmRulesTable_Object = MibTable
rsBWMCurrentFarmRulesTable = _RsBWMCurrentFarmRulesTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 39)
)
if mibBuilder.loadTexts:
    rsBWMCurrentFarmRulesTable.setStatus("mandatory")
_RsBWMCurrentFarmRulesEntry_Object = MibTableRow
rsBWMCurrentFarmRulesEntry = _RsBWMCurrentFarmRulesEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 39, 1)
)
rsBWMCurrentFarmRulesEntry.setIndexNames(
    (0, "BWM-MIB", "rsBWMCurrentFarmRulesName"),
)
if mibBuilder.loadTexts:
    rsBWMCurrentFarmRulesEntry.setStatus("mandatory")
_RsBWMCurrentFarmRulesIndex_Type = Integer32
_RsBWMCurrentFarmRulesIndex_Object = MibTableColumn
rsBWMCurrentFarmRulesIndex = _RsBWMCurrentFarmRulesIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 39, 1, 1),
    _RsBWMCurrentFarmRulesIndex_Type()
)
rsBWMCurrentFarmRulesIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMCurrentFarmRulesIndex.setStatus("mandatory")


class _RsBWMCurrentFarmRulesName_Type(DisplayString):
    """Custom type rsBWMCurrentFarmRulesName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_RsBWMCurrentFarmRulesName_Type.__name__ = "DisplayString"
_RsBWMCurrentFarmRulesName_Object = MibTableColumn
rsBWMCurrentFarmRulesName = _RsBWMCurrentFarmRulesName_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 39, 1, 2),
    _RsBWMCurrentFarmRulesName_Type()
)
rsBWMCurrentFarmRulesName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMCurrentFarmRulesName.setStatus("mandatory")


class _RsBWMCurrentFarmRulesDestination_Type(DisplayString):
    """Custom type rsBWMCurrentFarmRulesDestination based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 46),
    )


_RsBWMCurrentFarmRulesDestination_Type.__name__ = "DisplayString"
_RsBWMCurrentFarmRulesDestination_Object = MibTableColumn
rsBWMCurrentFarmRulesDestination = _RsBWMCurrentFarmRulesDestination_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 39, 1, 3),
    _RsBWMCurrentFarmRulesDestination_Type()
)
rsBWMCurrentFarmRulesDestination.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMCurrentFarmRulesDestination.setStatus("mandatory")


class _RsBWMCurrentFarmRulesSource_Type(DisplayString):
    """Custom type rsBWMCurrentFarmRulesSource based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 46),
    )


_RsBWMCurrentFarmRulesSource_Type.__name__ = "DisplayString"
_RsBWMCurrentFarmRulesSource_Object = MibTableColumn
rsBWMCurrentFarmRulesSource = _RsBWMCurrentFarmRulesSource_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 39, 1, 4),
    _RsBWMCurrentFarmRulesSource_Type()
)
rsBWMCurrentFarmRulesSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMCurrentFarmRulesSource.setStatus("mandatory")


class _RsBWMCurrentFarmRulesDirection_Type(Integer32):
    """Custom type rsBWMCurrentFarmRulesDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("oneway", 1),
          ("twoway", 2))
    )


_RsBWMCurrentFarmRulesDirection_Type.__name__ = "Integer32"
_RsBWMCurrentFarmRulesDirection_Object = MibTableColumn
rsBWMCurrentFarmRulesDirection = _RsBWMCurrentFarmRulesDirection_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 39, 1, 5),
    _RsBWMCurrentFarmRulesDirection_Type()
)
rsBWMCurrentFarmRulesDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMCurrentFarmRulesDirection.setStatus("mandatory")


class _RsBWMCurrentFarmRulesDescription_Type(DisplayString):
    """Custom type rsBWMCurrentFarmRulesDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 19),
    )


_RsBWMCurrentFarmRulesDescription_Type.__name__ = "DisplayString"
_RsBWMCurrentFarmRulesDescription_Object = MibTableColumn
rsBWMCurrentFarmRulesDescription = _RsBWMCurrentFarmRulesDescription_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 39, 1, 6),
    _RsBWMCurrentFarmRulesDescription_Type()
)
rsBWMCurrentFarmRulesDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMCurrentFarmRulesDescription.setStatus("mandatory")


class _RsBWMCurrentFarmRulesPolicyType_Type(Integer32):
    """Custom type rsBWMCurrentFarmRulesPolicyType based on Integer32"""
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
        *(("none", 1),
          ("filter", 2),
          ("group", 3),
          ("policy", 4))
    )


_RsBWMCurrentFarmRulesPolicyType_Type.__name__ = "Integer32"
_RsBWMCurrentFarmRulesPolicyType_Object = MibTableColumn
rsBWMCurrentFarmRulesPolicyType = _RsBWMCurrentFarmRulesPolicyType_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 39, 1, 7),
    _RsBWMCurrentFarmRulesPolicyType_Type()
)
rsBWMCurrentFarmRulesPolicyType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMCurrentFarmRulesPolicyType.setStatus("mandatory")


class _RsBWMCurrentFarmRulesPolicy_Type(DisplayString):
    """Custom type rsBWMCurrentFarmRulesPolicy based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 29),
    )


_RsBWMCurrentFarmRulesPolicy_Type.__name__ = "DisplayString"
_RsBWMCurrentFarmRulesPolicy_Object = MibTableColumn
rsBWMCurrentFarmRulesPolicy = _RsBWMCurrentFarmRulesPolicy_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 39, 1, 8),
    _RsBWMCurrentFarmRulesPolicy_Type()
)
rsBWMCurrentFarmRulesPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMCurrentFarmRulesPolicy.setStatus("mandatory")


class _RsBWMCurrentFarmRulesSpecific_Type(DisplayString):
    """Custom type rsBWMCurrentFarmRulesSpecific based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 19),
    )


_RsBWMCurrentFarmRulesSpecific_Type.__name__ = "DisplayString"
_RsBWMCurrentFarmRulesSpecific_Object = MibTableColumn
rsBWMCurrentFarmRulesSpecific = _RsBWMCurrentFarmRulesSpecific_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 39, 1, 9),
    _RsBWMCurrentFarmRulesSpecific_Type()
)
rsBWMCurrentFarmRulesSpecific.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMCurrentFarmRulesSpecific.setStatus("mandatory")
_RsBWMCurrentFarmBandwidthLastSec_Type = Counter32
_RsBWMCurrentFarmBandwidthLastSec_Object = MibTableColumn
rsBWMCurrentFarmBandwidthLastSec = _RsBWMCurrentFarmBandwidthLastSec_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 39, 1, 10),
    _RsBWMCurrentFarmBandwidthLastSec_Type()
)
rsBWMCurrentFarmBandwidthLastSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMCurrentFarmBandwidthLastSec.setStatus("mandatory")
_RsBWMCurrentFarmPacketsLastSec_Type = Counter32
_RsBWMCurrentFarmPacketsLastSec_Object = MibTableColumn
rsBWMCurrentFarmPacketsLastSec = _RsBWMCurrentFarmPacketsLastSec_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 39, 1, 11),
    _RsBWMCurrentFarmPacketsLastSec_Type()
)
rsBWMCurrentFarmPacketsLastSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMCurrentFarmPacketsLastSec.setStatus("mandatory")


class _RsBWMCurrentFarmRulesPhysicalPortGroup_Type(DisplayString):
    """Custom type rsBWMCurrentFarmRulesPhysicalPortGroup based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 19),
    )


_RsBWMCurrentFarmRulesPhysicalPortGroup_Type.__name__ = "DisplayString"
_RsBWMCurrentFarmRulesPhysicalPortGroup_Object = MibTableColumn
rsBWMCurrentFarmRulesPhysicalPortGroup = _RsBWMCurrentFarmRulesPhysicalPortGroup_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 39, 1, 12),
    _RsBWMCurrentFarmRulesPhysicalPortGroup_Type()
)
rsBWMCurrentFarmRulesPhysicalPortGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMCurrentFarmRulesPhysicalPortGroup.setStatus("mandatory")


class _RsBWMCurrentFarmRulesVLANTagGroup_Type(DisplayString):
    """Custom type rsBWMCurrentFarmRulesVLANTagGroup based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 19),
    )


_RsBWMCurrentFarmRulesVLANTagGroup_Type.__name__ = "DisplayString"
_RsBWMCurrentFarmRulesVLANTagGroup_Object = MibTableColumn
rsBWMCurrentFarmRulesVLANTagGroup = _RsBWMCurrentFarmRulesVLANTagGroup_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 39, 1, 13),
    _RsBWMCurrentFarmRulesVLANTagGroup_Type()
)
rsBWMCurrentFarmRulesVLANTagGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMCurrentFarmRulesVLANTagGroup.setStatus("mandatory")


class _RsBWMCurrentFarmRulesDSCPMarking_Type(Integer32):
    """Custom type rsBWMCurrentFarmRulesDSCPMarking based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 63),
    )


_RsBWMCurrentFarmRulesDSCPMarking_Type.__name__ = "Integer32"
_RsBWMCurrentFarmRulesDSCPMarking_Object = MibTableColumn
rsBWMCurrentFarmRulesDSCPMarking = _RsBWMCurrentFarmRulesDSCPMarking_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 39, 1, 14),
    _RsBWMCurrentFarmRulesDSCPMarking_Type()
)
rsBWMCurrentFarmRulesDSCPMarking.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMCurrentFarmRulesDSCPMarking.setStatus("mandatory")
_RsBWMOMPCHashTableOffset_Type = Integer32
_RsBWMOMPCHashTableOffset_Object = MibScalar
rsBWMOMPCHashTableOffset = _RsBWMOMPCHashTableOffset_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 40),
    _RsBWMOMPCHashTableOffset_Type()
)
rsBWMOMPCHashTableOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMOMPCHashTableOffset.setStatus("mandatory")
_RsBWMOMPCHashTableMask_Type = OctetString
_RsBWMOMPCHashTableMask_Object = MibScalar
rsBWMOMPCHashTableMask = _RsBWMOMPCHashTableMask_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 41),
    _RsBWMOMPCHashTableMask_Type()
)
rsBWMOMPCHashTableMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMOMPCHashTableMask.setStatus("mandatory")


class _RsBWMNoSaveMode_Type(Integer32):
    """Custom type rsBWMNoSaveMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_RsBWMNoSaveMode_Type.__name__ = "Integer32"
_RsBWMNoSaveMode_Object = MibScalar
rsBWMNoSaveMode = _RsBWMNoSaveMode_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 42),
    _RsBWMNoSaveMode_Type()
)
rsBWMNoSaveMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMNoSaveMode.setStatus("mandatory")


class _RsBWMStringSearchMode_Type(Integer32):
    """Custom type rsBWMStringSearchMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("regular", 1),
          ("parallel", 2))
    )


_RsBWMStringSearchMode_Type.__name__ = "Integer32"
_RsBWMStringSearchMode_Object = MibScalar
rsBWMStringSearchMode = _RsBWMStringSearchMode_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 46),
    _RsBWMStringSearchMode_Type()
)
rsBWMStringSearchMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMStringSearchMode.setStatus("mandatory")
_RsBWMVLANTagGroupTable_Object = MibTable
rsBWMVLANTagGroupTable = _RsBWMVLANTagGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 47)
)
if mibBuilder.loadTexts:
    rsBWMVLANTagGroupTable.setStatus("mandatory")
_RsBWMVLANTagGroupEntry_Object = MibTableRow
rsBWMVLANTagGroupEntry = _RsBWMVLANTagGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 47, 1)
)
rsBWMVLANTagGroupEntry.setIndexNames(
    (0, "BWM-MIB", "rsBWMVLANTagGroupName"),
    (0, "BWM-MIB", "rsBWMVLANTagGroupVLANTag"),
    (0, "BWM-MIB", "rsBWMVLANTagGroupVLANTagFrom"),
)
if mibBuilder.loadTexts:
    rsBWMVLANTagGroupEntry.setStatus("mandatory")


class _RsBWMVLANTagGroupName_Type(DisplayString):
    """Custom type rsBWMVLANTagGroupName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 19),
    )


_RsBWMVLANTagGroupName_Type.__name__ = "DisplayString"
_RsBWMVLANTagGroupName_Object = MibTableColumn
rsBWMVLANTagGroupName = _RsBWMVLANTagGroupName_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 47, 1, 1),
    _RsBWMVLANTagGroupName_Type()
)
rsBWMVLANTagGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMVLANTagGroupName.setStatus("mandatory")
_RsBWMVLANTagGroupVLANTag_Type = Integer32
_RsBWMVLANTagGroupVLANTag_Object = MibTableColumn
rsBWMVLANTagGroupVLANTag = _RsBWMVLANTagGroupVLANTag_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 47, 1, 2),
    _RsBWMVLANTagGroupVLANTag_Type()
)
rsBWMVLANTagGroupVLANTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMVLANTagGroupVLANTag.setStatus("mandatory")
_RsBWMVLANTagGroupVLANTagFrom_Type = Integer32
_RsBWMVLANTagGroupVLANTagFrom_Object = MibTableColumn
rsBWMVLANTagGroupVLANTagFrom = _RsBWMVLANTagGroupVLANTagFrom_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 47, 1, 3),
    _RsBWMVLANTagGroupVLANTagFrom_Type()
)
rsBWMVLANTagGroupVLANTagFrom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMVLANTagGroupVLANTagFrom.setStatus("mandatory")


class _RsBWMVLANTagGroupVLANTagTo_Type(Integer32):
    """Custom type rsBWMVLANTagGroupVLANTagTo based on Integer32"""
    defaultValue = 65536


_RsBWMVLANTagGroupVLANTagTo_Type.__name__ = "Integer32"
_RsBWMVLANTagGroupVLANTagTo_Object = MibTableColumn
rsBWMVLANTagGroupVLANTagTo = _RsBWMVLANTagGroupVLANTagTo_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 47, 1, 4),
    _RsBWMVLANTagGroupVLANTagTo_Type()
)
rsBWMVLANTagGroupVLANTagTo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMVLANTagGroupVLANTagTo.setStatus("mandatory")


class _RsBWMVLANTagGroupMode_Type(Integer32):
    """Custom type rsBWMVLANTagGroupMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("discrete", 1),
          ("range", 2))
    )


_RsBWMVLANTagGroupMode_Type.__name__ = "Integer32"
_RsBWMVLANTagGroupMode_Object = MibTableColumn
rsBWMVLANTagGroupMode = _RsBWMVLANTagGroupMode_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 47, 1, 5),
    _RsBWMVLANTagGroupMode_Type()
)
rsBWMVLANTagGroupMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMVLANTagGroupMode.setStatus("mandatory")
_RsBWMVLANTagGroupStatus_Type = RowStatus
_RsBWMVLANTagGroupStatus_Object = MibTableColumn
rsBWMVLANTagGroupStatus = _RsBWMVLANTagGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 47, 1, 6),
    _RsBWMVLANTagGroupStatus_Type()
)
rsBWMVLANTagGroupStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMVLANTagGroupStatus.setStatus("mandatory")
_RsBWMCurrentVLANTagGroupTable_Object = MibTable
rsBWMCurrentVLANTagGroupTable = _RsBWMCurrentVLANTagGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 48)
)
if mibBuilder.loadTexts:
    rsBWMCurrentVLANTagGroupTable.setStatus("mandatory")
_RsBWMCurrentVLANTagGroupEntry_Object = MibTableRow
rsBWMCurrentVLANTagGroupEntry = _RsBWMCurrentVLANTagGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 48, 1)
)
rsBWMCurrentVLANTagGroupEntry.setIndexNames(
    (0, "BWM-MIB", "rsBWMCurrentVLANTagGroupName"),
    (0, "BWM-MIB", "rsBWMCurrentVLANTagGroupVLANTag"),
    (0, "BWM-MIB", "rsBWMCurrentVLANTagGroupVLANTagFrom"),
)
if mibBuilder.loadTexts:
    rsBWMCurrentVLANTagGroupEntry.setStatus("mandatory")


class _RsBWMCurrentVLANTagGroupName_Type(DisplayString):
    """Custom type rsBWMCurrentVLANTagGroupName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 19),
    )


_RsBWMCurrentVLANTagGroupName_Type.__name__ = "DisplayString"
_RsBWMCurrentVLANTagGroupName_Object = MibTableColumn
rsBWMCurrentVLANTagGroupName = _RsBWMCurrentVLANTagGroupName_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 48, 1, 1),
    _RsBWMCurrentVLANTagGroupName_Type()
)
rsBWMCurrentVLANTagGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMCurrentVLANTagGroupName.setStatus("mandatory")
_RsBWMCurrentVLANTagGroupVLANTag_Type = Integer32
_RsBWMCurrentVLANTagGroupVLANTag_Object = MibTableColumn
rsBWMCurrentVLANTagGroupVLANTag = _RsBWMCurrentVLANTagGroupVLANTag_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 48, 1, 2),
    _RsBWMCurrentVLANTagGroupVLANTag_Type()
)
rsBWMCurrentVLANTagGroupVLANTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMCurrentVLANTagGroupVLANTag.setStatus("mandatory")
_RsBWMCurrentVLANTagGroupVLANTagFrom_Type = Integer32
_RsBWMCurrentVLANTagGroupVLANTagFrom_Object = MibTableColumn
rsBWMCurrentVLANTagGroupVLANTagFrom = _RsBWMCurrentVLANTagGroupVLANTagFrom_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 48, 1, 3),
    _RsBWMCurrentVLANTagGroupVLANTagFrom_Type()
)
rsBWMCurrentVLANTagGroupVLANTagFrom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMCurrentVLANTagGroupVLANTagFrom.setStatus("mandatory")
_RsBWMCurrentVLANTagGroupVLANTagTo_Type = Integer32
_RsBWMCurrentVLANTagGroupVLANTagTo_Object = MibTableColumn
rsBWMCurrentVLANTagGroupVLANTagTo = _RsBWMCurrentVLANTagGroupVLANTagTo_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 48, 1, 4),
    _RsBWMCurrentVLANTagGroupVLANTagTo_Type()
)
rsBWMCurrentVLANTagGroupVLANTagTo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMCurrentVLANTagGroupVLANTagTo.setStatus("mandatory")


class _RsBWMCurrentVLANTagGroupMode_Type(Integer32):
    """Custom type rsBWMCurrentVLANTagGroupMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("discrete", 1),
          ("range", 2))
    )


_RsBWMCurrentVLANTagGroupMode_Type.__name__ = "Integer32"
_RsBWMCurrentVLANTagGroupMode_Object = MibTableColumn
rsBWMCurrentVLANTagGroupMode = _RsBWMCurrentVLANTagGroupMode_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 48, 1, 5),
    _RsBWMCurrentVLANTagGroupMode_Type()
)
rsBWMCurrentVLANTagGroupMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMCurrentVLANTagGroupMode.setStatus("mandatory")
_RsBWMMacGroupTable_Object = MibTable
rsBWMMacGroupTable = _RsBWMMacGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 49)
)
if mibBuilder.loadTexts:
    rsBWMMacGroupTable.setStatus("mandatory")
_RsBWMMacGroupEntry_Object = MibTableRow
rsBWMMacGroupEntry = _RsBWMMacGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 49, 1)
)
rsBWMMacGroupEntry.setIndexNames(
    (0, "BWM-MIB", "rsBWMMacGroupEntryName"),
    (0, "BWM-MIB", "rsBWMMacGroupEntryAddress"),
)
if mibBuilder.loadTexts:
    rsBWMMacGroupEntry.setStatus("mandatory")


class _RsBWMMacGroupEntryName_Type(DisplayString):
    """Custom type rsBWMMacGroupEntryName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 19),
    )


_RsBWMMacGroupEntryName_Type.__name__ = "DisplayString"
_RsBWMMacGroupEntryName_Object = MibTableColumn
rsBWMMacGroupEntryName = _RsBWMMacGroupEntryName_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 49, 1, 1),
    _RsBWMMacGroupEntryName_Type()
)
rsBWMMacGroupEntryName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMMacGroupEntryName.setStatus("mandatory")
_RsBWMMacGroupEntryAddress_Type = MacAddress
_RsBWMMacGroupEntryAddress_Object = MibTableColumn
rsBWMMacGroupEntryAddress = _RsBWMMacGroupEntryAddress_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 49, 1, 2),
    _RsBWMMacGroupEntryAddress_Type()
)
rsBWMMacGroupEntryAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMMacGroupEntryAddress.setStatus("mandatory")
_RsBWMMacGroupEntryStatus_Type = RowStatus
_RsBWMMacGroupEntryStatus_Object = MibTableColumn
rsBWMMacGroupEntryStatus = _RsBWMMacGroupEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 49, 1, 3),
    _RsBWMMacGroupEntryStatus_Type()
)
rsBWMMacGroupEntryStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMMacGroupEntryStatus.setStatus("mandatory")
_RsBWMMacGroupCurrentTable_Object = MibTable
rsBWMMacGroupCurrentTable = _RsBWMMacGroupCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 50)
)
if mibBuilder.loadTexts:
    rsBWMMacGroupCurrentTable.setStatus("mandatory")
_RsBWMMacGroupCurrentEntry_Object = MibTableRow
rsBWMMacGroupCurrentEntry = _RsBWMMacGroupCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 50, 1)
)
rsBWMMacGroupCurrentEntry.setIndexNames(
    (0, "BWM-MIB", "rsBWMMacGroupCurrentEntryName"),
    (0, "BWM-MIB", "rsBWMMacGroupCurrentEntryAddress"),
)
if mibBuilder.loadTexts:
    rsBWMMacGroupCurrentEntry.setStatus("mandatory")


class _RsBWMMacGroupCurrentEntryName_Type(DisplayString):
    """Custom type rsBWMMacGroupCurrentEntryName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 19),
    )


_RsBWMMacGroupCurrentEntryName_Type.__name__ = "DisplayString"
_RsBWMMacGroupCurrentEntryName_Object = MibTableColumn
rsBWMMacGroupCurrentEntryName = _RsBWMMacGroupCurrentEntryName_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 50, 1, 1),
    _RsBWMMacGroupCurrentEntryName_Type()
)
rsBWMMacGroupCurrentEntryName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMMacGroupCurrentEntryName.setStatus("mandatory")
_RsBWMMacGroupCurrentEntryAddress_Type = MacAddress
_RsBWMMacGroupCurrentEntryAddress_Object = MibTableColumn
rsBWMMacGroupCurrentEntryAddress = _RsBWMMacGroupCurrentEntryAddress_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 50, 1, 2),
    _RsBWMMacGroupCurrentEntryAddress_Type()
)
rsBWMMacGroupCurrentEntryAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMMacGroupCurrentEntryAddress.setStatus("mandatory")


class _RsBWMQueueSize_Type(Integer32):
    """Custom type rsBWMQueueSize based on Integer32"""
    defaultValue = 512


_RsBWMQueueSize_Type.__name__ = "Integer32"
_RsBWMQueueSize_Object = MibScalar
rsBWMQueueSize = _RsBWMQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 51),
    _RsBWMQueueSize_Type()
)
rsBWMQueueSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMQueueSize.setStatus("mandatory")
_RsBWMTrafficFlowBWAgingTime_Type = Integer32
_RsBWMTrafficFlowBWAgingTime_Object = MibScalar
rsBWMTrafficFlowBWAgingTime = _RsBWMTrafficFlowBWAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 52),
    _RsBWMTrafficFlowBWAgingTime_Type()
)
rsBWMTrafficFlowBWAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMTrafficFlowBWAgingTime.setStatus("mandatory")
_RsBWMServiceTable_Object = MibTable
rsBWMServiceTable = _RsBWMServiceTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 53)
)
if mibBuilder.loadTexts:
    rsBWMServiceTable.setStatus("mandatory")
_RsBWMServiceEntry_Object = MibTableRow
rsBWMServiceEntry = _RsBWMServiceEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 53, 1)
)
rsBWMServiceEntry.setIndexNames(
    (0, "BWM-MIB", "rsBWMServiceTableType"),
    (0, "BWM-MIB", "rsBWMServiceType"),
    (0, "BWM-MIB", "rsBWMServiceName"),
)
if mibBuilder.loadTexts:
    rsBWMServiceEntry.setStatus("mandatory")


class _RsBWMServiceTableType_Type(Integer32):
    """Custom type rsBWMServiceTableType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("filterActive", 1),
          ("filterModify", 2),
          ("advancedActive", 3),
          ("advancedModify", 4),
          ("groupActive", 5),
          ("groupModify", 6))
    )


_RsBWMServiceTableType_Type.__name__ = "Integer32"
_RsBWMServiceTableType_Object = MibTableColumn
rsBWMServiceTableType = _RsBWMServiceTableType_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 53, 1, 1),
    _RsBWMServiceTableType_Type()
)
rsBWMServiceTableType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMServiceTableType.setStatus("mandatory")


class _RsBWMServiceType_Type(Integer32):
    """Custom type rsBWMServiceType based on Integer32"""
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
        *(("regular", 1),
          ("static", 2),
          ("ids", 3),
          ("idsStatic", 4))
    )


_RsBWMServiceType_Type.__name__ = "Integer32"
_RsBWMServiceType_Object = MibTableColumn
rsBWMServiceType = _RsBWMServiceType_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 53, 1, 2),
    _RsBWMServiceType_Type()
)
rsBWMServiceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMServiceType.setStatus("mandatory")


class _RsBWMServiceName_Type(DisplayString):
    """Custom type rsBWMServiceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 29),
    )


_RsBWMServiceName_Type.__name__ = "DisplayString"
_RsBWMServiceName_Object = MibTableColumn
rsBWMServiceName = _RsBWMServiceName_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 53, 1, 3),
    _RsBWMServiceName_Type()
)
rsBWMServiceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMServiceName.setStatus("mandatory")
_RsBWMPolicyGroupTable_Object = MibTable
rsBWMPolicyGroupTable = _RsBWMPolicyGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 54)
)
if mibBuilder.loadTexts:
    rsBWMPolicyGroupTable.setStatus("mandatory")
_RsBWMPolicyGroupEntry_Object = MibTableRow
rsBWMPolicyGroupEntry = _RsBWMPolicyGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 54, 1)
)
rsBWMPolicyGroupEntry.setIndexNames(
    (0, "BWM-MIB", "rsBWMPolicyGroupEntryName"),
)
if mibBuilder.loadTexts:
    rsBWMPolicyGroupEntry.setStatus("mandatory")


class _RsBWMPolicyGroupEntryName_Type(DisplayString):
    """Custom type rsBWMPolicyGroupEntryName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 19),
    )


_RsBWMPolicyGroupEntryName_Type.__name__ = "DisplayString"
_RsBWMPolicyGroupEntryName_Object = MibTableColumn
rsBWMPolicyGroupEntryName = _RsBWMPolicyGroupEntryName_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 54, 1, 1),
    _RsBWMPolicyGroupEntryName_Type()
)
rsBWMPolicyGroupEntryName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMPolicyGroupEntryName.setStatus("mandatory")
_RsBWMPolicyGroupEntryStatus_Type = RowStatus
_RsBWMPolicyGroupEntryStatus_Object = MibTableColumn
rsBWMPolicyGroupEntryStatus = _RsBWMPolicyGroupEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 54, 1, 2),
    _RsBWMPolicyGroupEntryStatus_Type()
)
rsBWMPolicyGroupEntryStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMPolicyGroupEntryStatus.setStatus("mandatory")
_RsBWMPolicyGroupCurrentTable_Object = MibTable
rsBWMPolicyGroupCurrentTable = _RsBWMPolicyGroupCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 55)
)
if mibBuilder.loadTexts:
    rsBWMPolicyGroupCurrentTable.setStatus("mandatory")
_RsBWMPolicyGroupCurrentEntry_Object = MibTableRow
rsBWMPolicyGroupCurrentEntry = _RsBWMPolicyGroupCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 55, 1)
)
rsBWMPolicyGroupCurrentEntry.setIndexNames(
    (0, "BWM-MIB", "rsBWMPolicyGroupCurrentEntryName"),
)
if mibBuilder.loadTexts:
    rsBWMPolicyGroupCurrentEntry.setStatus("mandatory")


class _RsBWMPolicyGroupCurrentEntryName_Type(DisplayString):
    """Custom type rsBWMPolicyGroupCurrentEntryName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 19),
    )


_RsBWMPolicyGroupCurrentEntryName_Type.__name__ = "DisplayString"
_RsBWMPolicyGroupCurrentEntryName_Object = MibTableColumn
rsBWMPolicyGroupCurrentEntryName = _RsBWMPolicyGroupCurrentEntryName_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 55, 1, 1),
    _RsBWMPolicyGroupCurrentEntryName_Type()
)
rsBWMPolicyGroupCurrentEntryName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMPolicyGroupCurrentEntryName.setStatus("mandatory")
_RsBWMAppPortGroupEntryTable_Object = MibTable
rsBWMAppPortGroupEntryTable = _RsBWMAppPortGroupEntryTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 56)
)
if mibBuilder.loadTexts:
    rsBWMAppPortGroupEntryTable.setStatus("mandatory")
_RsBWMAppPortGroupEntry_Object = MibTableRow
rsBWMAppPortGroupEntry = _RsBWMAppPortGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 56, 1)
)
rsBWMAppPortGroupEntry.setIndexNames(
    (0, "BWM-MIB", "rsBWMAppPortGroupName"),
    (0, "BWM-MIB", "rsBWMAppPortGroupFromPort"),
    (0, "BWM-MIB", "rsBWMAppPortGroupToPort"),
)
if mibBuilder.loadTexts:
    rsBWMAppPortGroupEntry.setStatus("mandatory")


class _RsBWMAppPortGroupName_Type(DisplayString):
    """Custom type rsBWMAppPortGroupName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 29),
    )


_RsBWMAppPortGroupName_Type.__name__ = "DisplayString"
_RsBWMAppPortGroupName_Object = MibTableColumn
rsBWMAppPortGroupName = _RsBWMAppPortGroupName_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 56, 1, 1),
    _RsBWMAppPortGroupName_Type()
)
rsBWMAppPortGroupName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMAppPortGroupName.setStatus("mandatory")
_RsBWMAppPortGroupFromPort_Type = Integer32
_RsBWMAppPortGroupFromPort_Object = MibTableColumn
rsBWMAppPortGroupFromPort = _RsBWMAppPortGroupFromPort_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 56, 1, 2),
    _RsBWMAppPortGroupFromPort_Type()
)
rsBWMAppPortGroupFromPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMAppPortGroupFromPort.setStatus("mandatory")
_RsBWMAppPortGroupToPort_Type = Integer32
_RsBWMAppPortGroupToPort_Object = MibTableColumn
rsBWMAppPortGroupToPort = _RsBWMAppPortGroupToPort_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 56, 1, 3),
    _RsBWMAppPortGroupToPort_Type()
)
rsBWMAppPortGroupToPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMAppPortGroupToPort.setStatus("mandatory")


class _RsBWMAppPortGroupType_Type(Integer32):
    """Custom type rsBWMAppPortGroupType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("regular", 1),
          ("static", 2))
    )


_RsBWMAppPortGroupType_Type.__name__ = "Integer32"
_RsBWMAppPortGroupType_Object = MibTableColumn
rsBWMAppPortGroupType = _RsBWMAppPortGroupType_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 56, 1, 4),
    _RsBWMAppPortGroupType_Type()
)
rsBWMAppPortGroupType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMAppPortGroupType.setStatus("mandatory")
_RsBWMAppPortGroupStatus_Type = RowStatus
_RsBWMAppPortGroupStatus_Object = MibTableColumn
rsBWMAppPortGroupStatus = _RsBWMAppPortGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 56, 1, 5),
    _RsBWMAppPortGroupStatus_Type()
)
rsBWMAppPortGroupStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMAppPortGroupStatus.setStatus("mandatory")
_RsBWMCurrentAppPortGroupEntryTable_Object = MibTable
rsBWMCurrentAppPortGroupEntryTable = _RsBWMCurrentAppPortGroupEntryTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 57)
)
if mibBuilder.loadTexts:
    rsBWMCurrentAppPortGroupEntryTable.setStatus("mandatory")
_RsBWMCurrentAppPortGroupEntry_Object = MibTableRow
rsBWMCurrentAppPortGroupEntry = _RsBWMCurrentAppPortGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 57, 1)
)
rsBWMCurrentAppPortGroupEntry.setIndexNames(
    (0, "BWM-MIB", "rsBWMCurrentAppPortGroupName"),
    (0, "BWM-MIB", "rsBWMCurrentAppPortGroupFromPort"),
    (0, "BWM-MIB", "rsBWMCurrentAppPortGroupToPort"),
)
if mibBuilder.loadTexts:
    rsBWMCurrentAppPortGroupEntry.setStatus("mandatory")


class _RsBWMCurrentAppPortGroupName_Type(DisplayString):
    """Custom type rsBWMCurrentAppPortGroupName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 29),
    )


_RsBWMCurrentAppPortGroupName_Type.__name__ = "DisplayString"
_RsBWMCurrentAppPortGroupName_Object = MibTableColumn
rsBWMCurrentAppPortGroupName = _RsBWMCurrentAppPortGroupName_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 57, 1, 1),
    _RsBWMCurrentAppPortGroupName_Type()
)
rsBWMCurrentAppPortGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMCurrentAppPortGroupName.setStatus("mandatory")
_RsBWMCurrentAppPortGroupFromPort_Type = Integer32
_RsBWMCurrentAppPortGroupFromPort_Object = MibTableColumn
rsBWMCurrentAppPortGroupFromPort = _RsBWMCurrentAppPortGroupFromPort_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 57, 1, 2),
    _RsBWMCurrentAppPortGroupFromPort_Type()
)
rsBWMCurrentAppPortGroupFromPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMCurrentAppPortGroupFromPort.setStatus("mandatory")
_RsBWMCurrentAppPortGroupToPort_Type = Integer32
_RsBWMCurrentAppPortGroupToPort_Object = MibTableColumn
rsBWMCurrentAppPortGroupToPort = _RsBWMCurrentAppPortGroupToPort_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 57, 1, 3),
    _RsBWMCurrentAppPortGroupToPort_Type()
)
rsBWMCurrentAppPortGroupToPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMCurrentAppPortGroupToPort.setStatus("mandatory")


class _RsBWMCurrentAppPortGroupType_Type(Integer32):
    """Custom type rsBWMCurrentAppPortGroupType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("regular", 1),
          ("static", 2))
    )


_RsBWMCurrentAppPortGroupType_Type.__name__ = "Integer32"
_RsBWMCurrentAppPortGroupType_Object = MibTableColumn
rsBWMCurrentAppPortGroupType = _RsBWMCurrentAppPortGroupType_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 57, 1, 4),
    _RsBWMCurrentAppPortGroupType_Type()
)
rsBWMCurrentAppPortGroupType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMCurrentAppPortGroupType.setStatus("mandatory")


class _RsBWMDefaultGatewayClassificatiomMode_Type(Integer32):
    """Custom type rsBWMDefaultGatewayClassificatiomMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_RsBWMDefaultGatewayClassificatiomMode_Type.__name__ = "Integer32"
_RsBWMDefaultGatewayClassificatiomMode_Object = MibScalar
rsBWMDefaultGatewayClassificatiomMode = _RsBWMDefaultGatewayClassificatiomMode_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 58),
    _RsBWMDefaultGatewayClassificatiomMode_Type()
)
rsBWMDefaultGatewayClassificatiomMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMDefaultGatewayClassificatiomMode.setStatus("mandatory")
_RsBWMExtRulesTable_Object = MibTable
rsBWMExtRulesTable = _RsBWMExtRulesTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 59)
)
if mibBuilder.loadTexts:
    rsBWMExtRulesTable.setStatus("mandatory")
_RsBWMExtRulesEntry_Object = MibTableRow
rsBWMExtRulesEntry = _RsBWMExtRulesEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 59, 1)
)
rsBWMExtRulesEntry.setIndexNames(
    (0, "BWM-MIB", "rsBWMExtRulesName"),
)
if mibBuilder.loadTexts:
    rsBWMExtRulesEntry.setStatus("mandatory")


class _RsBWMExtRulesName_Type(DisplayString):
    """Custom type rsBWMExtRulesName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_RsBWMExtRulesName_Type.__name__ = "DisplayString"
_RsBWMExtRulesName_Object = MibTableColumn
rsBWMExtRulesName = _RsBWMExtRulesName_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 59, 1, 1),
    _RsBWMExtRulesName_Type()
)
rsBWMExtRulesName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMExtRulesName.setStatus("mandatory")


class _RsBWMExtRulesFromFarm_Type(DisplayString):
    """Custom type rsBWMExtRulesFromFarm based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 19),
    )


_RsBWMExtRulesFromFarm_Type.__name__ = "DisplayString"
_RsBWMExtRulesFromFarm_Object = MibTableColumn
rsBWMExtRulesFromFarm = _RsBWMExtRulesFromFarm_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 59, 1, 2),
    _RsBWMExtRulesFromFarm_Type()
)
rsBWMExtRulesFromFarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMExtRulesFromFarm.setStatus("mandatory")


class _RsBWMExtRulesToFarm_Type(DisplayString):
    """Custom type rsBWMExtRulesToFarm based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 19),
    )


_RsBWMExtRulesToFarm_Type.__name__ = "DisplayString"
_RsBWMExtRulesToFarm_Object = MibTableColumn
rsBWMExtRulesToFarm = _RsBWMExtRulesToFarm_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 59, 1, 3),
    _RsBWMExtRulesToFarm_Type()
)
rsBWMExtRulesToFarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMExtRulesToFarm.setStatus("mandatory")


class _RsBWMExtRulesClassificationPoint_Type(Integer32):
    """Custom type rsBWMExtRulesClassificationPoint based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("beforeChanges", 1),
          ("afterChanges", 2))
    )


_RsBWMExtRulesClassificationPoint_Type.__name__ = "Integer32"
_RsBWMExtRulesClassificationPoint_Object = MibTableColumn
rsBWMExtRulesClassificationPoint = _RsBWMExtRulesClassificationPoint_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 59, 1, 4),
    _RsBWMExtRulesClassificationPoint_Type()
)
rsBWMExtRulesClassificationPoint.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMExtRulesClassificationPoint.setStatus("mandatory")


class _RsBWMExtRulesTrafficIdentification_Type(Integer32):
    """Custom type rsBWMExtRulesTrafficIdentification based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("client", 1),
          ("session", 2),
          ("connection", 3),
          ("fullL4Session", 4),
          ("sessionCookie", 5),
          ("sipCallID", 6))
    )


_RsBWMExtRulesTrafficIdentification_Type.__name__ = "Integer32"
_RsBWMExtRulesTrafficIdentification_Object = MibTableColumn
rsBWMExtRulesTrafficIdentification = _RsBWMExtRulesTrafficIdentification_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 59, 1, 5),
    _RsBWMExtRulesTrafficIdentification_Type()
)
rsBWMExtRulesTrafficIdentification.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMExtRulesTrafficIdentification.setStatus("mandatory")
_RsBWMExtRulesTrafficFlowMaxBW_Type = Integer32
_RsBWMExtRulesTrafficFlowMaxBW_Object = MibTableColumn
rsBWMExtRulesTrafficFlowMaxBW = _RsBWMExtRulesTrafficFlowMaxBW_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 59, 1, 6),
    _RsBWMExtRulesTrafficFlowMaxBW_Type()
)
rsBWMExtRulesTrafficFlowMaxBW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMExtRulesTrafficFlowMaxBW.setStatus("mandatory")
_RsBWMExtRulesMaxConcurrentSessions_Type = Integer32
_RsBWMExtRulesMaxConcurrentSessions_Object = MibTableColumn
rsBWMExtRulesMaxConcurrentSessions = _RsBWMExtRulesMaxConcurrentSessions_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 59, 1, 7),
    _RsBWMExtRulesMaxConcurrentSessions_Type()
)
rsBWMExtRulesMaxConcurrentSessions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMExtRulesMaxConcurrentSessions.setStatus("mandatory")
_RsBWMExtRulesMaxRqstsPerSec_Type = Integer32
_RsBWMExtRulesMaxRqstsPerSec_Object = MibTableColumn
rsBWMExtRulesMaxRqstsPerSec = _RsBWMExtRulesMaxRqstsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 59, 1, 8),
    _RsBWMExtRulesMaxRqstsPerSec_Type()
)
rsBWMExtRulesMaxRqstsPerSec.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMExtRulesMaxRqstsPerSec.setStatus("mandatory")


class _RsBWMExtRulesTrafficIDCookieField_Type(DisplayString):
    """Custom type rsBWMExtRulesTrafficIDCookieField based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 19),
    )


_RsBWMExtRulesTrafficIDCookieField_Type.__name__ = "DisplayString"
_RsBWMExtRulesTrafficIDCookieField_Object = MibTableColumn
rsBWMExtRulesTrafficIDCookieField = _RsBWMExtRulesTrafficIDCookieField_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 59, 1, 9),
    _RsBWMExtRulesTrafficIDCookieField_Type()
)
rsBWMExtRulesTrafficIDCookieField.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMExtRulesTrafficIDCookieField.setStatus("mandatory")
_RsBWMExtRulesStatus_Type = RowStatus
_RsBWMExtRulesStatus_Object = MibTableColumn
rsBWMExtRulesStatus = _RsBWMExtRulesStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 59, 1, 10),
    _RsBWMExtRulesStatus_Type()
)
rsBWMExtRulesStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMExtRulesStatus.setStatus("mandatory")


class _RsBWMExtRulesActivate_Type(DisplayString):
    """Custom type rsBWMExtRulesActivate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 29),
    )


_RsBWMExtRulesActivate_Type.__name__ = "DisplayString"
_RsBWMExtRulesActivate_Object = MibTableColumn
rsBWMExtRulesActivate = _RsBWMExtRulesActivate_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 59, 1, 11),
    _RsBWMExtRulesActivate_Type()
)
rsBWMExtRulesActivate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMExtRulesActivate.setStatus("mandatory")


class _RsBWMExtRulesInactivate_Type(DisplayString):
    """Custom type rsBWMExtRulesInactivate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 29),
    )


_RsBWMExtRulesInactivate_Type.__name__ = "DisplayString"
_RsBWMExtRulesInactivate_Object = MibTableColumn
rsBWMExtRulesInactivate = _RsBWMExtRulesInactivate_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 59, 1, 12),
    _RsBWMExtRulesInactivate_Type()
)
rsBWMExtRulesInactivate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMExtRulesInactivate.setStatus("mandatory")


class _RsBWMExtRulesForceBestFit_Type(Integer32):
    """Custom type rsBWMExtRulesForceBestFit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_RsBWMExtRulesForceBestFit_Type.__name__ = "Integer32"
_RsBWMExtRulesForceBestFit_Object = MibTableColumn
rsBWMExtRulesForceBestFit = _RsBWMExtRulesForceBestFit_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 59, 1, 13),
    _RsBWMExtRulesForceBestFit_Type()
)
rsBWMExtRulesForceBestFit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMExtRulesForceBestFit.setStatus("mandatory")


class _RsBWMExtRulesPacketMarkingType_Type(Integer32):
    """Custom type rsBWMExtRulesPacketMarkingType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("dscp", 2),
          ("tos", 3))
    )


_RsBWMExtRulesPacketMarkingType_Type.__name__ = "Integer32"
_RsBWMExtRulesPacketMarkingType_Object = MibTableColumn
rsBWMExtRulesPacketMarkingType = _RsBWMExtRulesPacketMarkingType_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 59, 1, 14),
    _RsBWMExtRulesPacketMarkingType_Type()
)
rsBWMExtRulesPacketMarkingType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMExtRulesPacketMarkingType.setStatus("mandatory")


class _RsBWMExtRulesPacketMarkingValue_Type(Integer32):
    """Custom type rsBWMExtRulesPacketMarkingValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 63),
    )


_RsBWMExtRulesPacketMarkingValue_Type.__name__ = "Integer32"
_RsBWMExtRulesPacketMarkingValue_Object = MibTableColumn
rsBWMExtRulesPacketMarkingValue = _RsBWMExtRulesPacketMarkingValue_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 59, 1, 15),
    _RsBWMExtRulesPacketMarkingValue_Type()
)
rsBWMExtRulesPacketMarkingValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMExtRulesPacketMarkingValue.setStatus("mandatory")


class _RsBWMExtRulesReportMaxBw_Type(Integer32):
    """Custom type rsBWMExtRulesReportMaxBw based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_RsBWMExtRulesReportMaxBw_Type.__name__ = "Integer32"
_RsBWMExtRulesReportMaxBw_Object = MibTableColumn
rsBWMExtRulesReportMaxBw = _RsBWMExtRulesReportMaxBw_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 59, 1, 16),
    _RsBWMExtRulesReportMaxBw_Type()
)
rsBWMExtRulesReportMaxBw.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMExtRulesReportMaxBw.setStatus("mandatory")
_RsBWMCurrentExtRulesTable_Object = MibTable
rsBWMCurrentExtRulesTable = _RsBWMCurrentExtRulesTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 60)
)
if mibBuilder.loadTexts:
    rsBWMCurrentExtRulesTable.setStatus("mandatory")
_RsBWMCurrentExtRulesEntry_Object = MibTableRow
rsBWMCurrentExtRulesEntry = _RsBWMCurrentExtRulesEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 60, 1)
)
rsBWMCurrentExtRulesEntry.setIndexNames(
    (0, "BWM-MIB", "rsBWMCurrentExtRulesName"),
)
if mibBuilder.loadTexts:
    rsBWMCurrentExtRulesEntry.setStatus("mandatory")


class _RsBWMCurrentExtRulesName_Type(DisplayString):
    """Custom type rsBWMCurrentExtRulesName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_RsBWMCurrentExtRulesName_Type.__name__ = "DisplayString"
_RsBWMCurrentExtRulesName_Object = MibTableColumn
rsBWMCurrentExtRulesName = _RsBWMCurrentExtRulesName_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 60, 1, 1),
    _RsBWMCurrentExtRulesName_Type()
)
rsBWMCurrentExtRulesName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMCurrentExtRulesName.setStatus("mandatory")


class _RsBWMCurrentExtRulesFromFarm_Type(DisplayString):
    """Custom type rsBWMCurrentExtRulesFromFarm based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 19),
    )


_RsBWMCurrentExtRulesFromFarm_Type.__name__ = "DisplayString"
_RsBWMCurrentExtRulesFromFarm_Object = MibTableColumn
rsBWMCurrentExtRulesFromFarm = _RsBWMCurrentExtRulesFromFarm_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 60, 1, 2),
    _RsBWMCurrentExtRulesFromFarm_Type()
)
rsBWMCurrentExtRulesFromFarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMCurrentExtRulesFromFarm.setStatus("mandatory")


class _RsBWMCurrentExtRulesToFarm_Type(DisplayString):
    """Custom type rsBWMCurrentExtRulesToFarm based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 19),
    )


_RsBWMCurrentExtRulesToFarm_Type.__name__ = "DisplayString"
_RsBWMCurrentExtRulesToFarm_Object = MibTableColumn
rsBWMCurrentExtRulesToFarm = _RsBWMCurrentExtRulesToFarm_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 60, 1, 3),
    _RsBWMCurrentExtRulesToFarm_Type()
)
rsBWMCurrentExtRulesToFarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMCurrentExtRulesToFarm.setStatus("mandatory")


class _RsBWMCurrentExtRulesClassificationPoint_Type(Integer32):
    """Custom type rsBWMCurrentExtRulesClassificationPoint based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("beforeChanges", 1),
          ("afterChanges", 2))
    )


_RsBWMCurrentExtRulesClassificationPoint_Type.__name__ = "Integer32"
_RsBWMCurrentExtRulesClassificationPoint_Object = MibTableColumn
rsBWMCurrentExtRulesClassificationPoint = _RsBWMCurrentExtRulesClassificationPoint_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 60, 1, 4),
    _RsBWMCurrentExtRulesClassificationPoint_Type()
)
rsBWMCurrentExtRulesClassificationPoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMCurrentExtRulesClassificationPoint.setStatus("mandatory")


class _RsBWMCurrentExtRulesTrafficIdentification_Type(Integer32):
    """Custom type rsBWMCurrentExtRulesTrafficIdentification based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("client", 1),
          ("session", 2),
          ("connection", 3),
          ("fullL4Session", 4),
          ("sessionCookie", 5),
          ("sipCallID", 6))
    )


_RsBWMCurrentExtRulesTrafficIdentification_Type.__name__ = "Integer32"
_RsBWMCurrentExtRulesTrafficIdentification_Object = MibTableColumn
rsBWMCurrentExtRulesTrafficIdentification = _RsBWMCurrentExtRulesTrafficIdentification_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 60, 1, 5),
    _RsBWMCurrentExtRulesTrafficIdentification_Type()
)
rsBWMCurrentExtRulesTrafficIdentification.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMCurrentExtRulesTrafficIdentification.setStatus("mandatory")
_RsBWMCurrentExtRulesTrafficFlowMaxBW_Type = Integer32
_RsBWMCurrentExtRulesTrafficFlowMaxBW_Object = MibTableColumn
rsBWMCurrentExtRulesTrafficFlowMaxBW = _RsBWMCurrentExtRulesTrafficFlowMaxBW_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 60, 1, 6),
    _RsBWMCurrentExtRulesTrafficFlowMaxBW_Type()
)
rsBWMCurrentExtRulesTrafficFlowMaxBW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMCurrentExtRulesTrafficFlowMaxBW.setStatus("mandatory")
_RsBWMCurrentExtRulesMaxConcurrentSessions_Type = Integer32
_RsBWMCurrentExtRulesMaxConcurrentSessions_Object = MibTableColumn
rsBWMCurrentExtRulesMaxConcurrentSessions = _RsBWMCurrentExtRulesMaxConcurrentSessions_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 60, 1, 7),
    _RsBWMCurrentExtRulesMaxConcurrentSessions_Type()
)
rsBWMCurrentExtRulesMaxConcurrentSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMCurrentExtRulesMaxConcurrentSessions.setStatus("mandatory")
_RsBWMCurrentExtRulesMaxRqstsPerSec_Type = Integer32
_RsBWMCurrentExtRulesMaxRqstsPerSec_Object = MibTableColumn
rsBWMCurrentExtRulesMaxRqstsPerSec = _RsBWMCurrentExtRulesMaxRqstsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 60, 1, 8),
    _RsBWMCurrentExtRulesMaxRqstsPerSec_Type()
)
rsBWMCurrentExtRulesMaxRqstsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMCurrentExtRulesMaxRqstsPerSec.setStatus("mandatory")


class _RsBWMCurrentExtRulesTrafficIDCookieField_Type(DisplayString):
    """Custom type rsBWMCurrentExtRulesTrafficIDCookieField based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 19),
    )


_RsBWMCurrentExtRulesTrafficIDCookieField_Type.__name__ = "DisplayString"
_RsBWMCurrentExtRulesTrafficIDCookieField_Object = MibTableColumn
rsBWMCurrentExtRulesTrafficIDCookieField = _RsBWMCurrentExtRulesTrafficIDCookieField_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 60, 1, 9),
    _RsBWMCurrentExtRulesTrafficIDCookieField_Type()
)
rsBWMCurrentExtRulesTrafficIDCookieField.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMCurrentExtRulesTrafficIDCookieField.setStatus("mandatory")


class _RsBWMCurrentExtRulesActivate_Type(DisplayString):
    """Custom type rsBWMCurrentExtRulesActivate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 29),
    )


_RsBWMCurrentExtRulesActivate_Type.__name__ = "DisplayString"
_RsBWMCurrentExtRulesActivate_Object = MibTableColumn
rsBWMCurrentExtRulesActivate = _RsBWMCurrentExtRulesActivate_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 60, 1, 10),
    _RsBWMCurrentExtRulesActivate_Type()
)
rsBWMCurrentExtRulesActivate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMCurrentExtRulesActivate.setStatus("mandatory")


class _RsBWMCurrentExtRulesInactivate_Type(DisplayString):
    """Custom type rsBWMCurrentExtRulesInactivate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 29),
    )


_RsBWMCurrentExtRulesInactivate_Type.__name__ = "DisplayString"
_RsBWMCurrentExtRulesInactivate_Object = MibTableColumn
rsBWMCurrentExtRulesInactivate = _RsBWMCurrentExtRulesInactivate_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 60, 1, 11),
    _RsBWMCurrentExtRulesInactivate_Type()
)
rsBWMCurrentExtRulesInactivate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMCurrentExtRulesInactivate.setStatus("mandatory")


class _RsBWMCurrentExtRulesForceBestFit_Type(Integer32):
    """Custom type rsBWMCurrentExtRulesForceBestFit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_RsBWMCurrentExtRulesForceBestFit_Type.__name__ = "Integer32"
_RsBWMCurrentExtRulesForceBestFit_Object = MibTableColumn
rsBWMCurrentExtRulesForceBestFit = _RsBWMCurrentExtRulesForceBestFit_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 60, 1, 12),
    _RsBWMCurrentExtRulesForceBestFit_Type()
)
rsBWMCurrentExtRulesForceBestFit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMCurrentExtRulesForceBestFit.setStatus("mandatory")


class _RsBWMCurrentExtRulesPacketMarkingType_Type(Integer32):
    """Custom type rsBWMCurrentExtRulesPacketMarkingType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("dscp", 2),
          ("tos", 3))
    )


_RsBWMCurrentExtRulesPacketMarkingType_Type.__name__ = "Integer32"
_RsBWMCurrentExtRulesPacketMarkingType_Object = MibTableColumn
rsBWMCurrentExtRulesPacketMarkingType = _RsBWMCurrentExtRulesPacketMarkingType_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 60, 1, 13),
    _RsBWMCurrentExtRulesPacketMarkingType_Type()
)
rsBWMCurrentExtRulesPacketMarkingType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMCurrentExtRulesPacketMarkingType.setStatus("mandatory")


class _RsBWMCurrentExtRulesPacketMarkingValue_Type(Integer32):
    """Custom type rsBWMCurrentExtRulesPacketMarkingValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 63),
    )


_RsBWMCurrentExtRulesPacketMarkingValue_Type.__name__ = "Integer32"
_RsBWMCurrentExtRulesPacketMarkingValue_Object = MibTableColumn
rsBWMCurrentExtRulesPacketMarkingValue = _RsBWMCurrentExtRulesPacketMarkingValue_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 60, 1, 14),
    _RsBWMCurrentExtRulesPacketMarkingValue_Type()
)
rsBWMCurrentExtRulesPacketMarkingValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMCurrentExtRulesPacketMarkingValue.setStatus("mandatory")


class _RsBWMCurrentExtRulesReportMaxBw_Type(Integer32):
    """Custom type rsBWMCurrentExtRulesReportMaxBw based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_RsBWMCurrentExtRulesReportMaxBw_Type.__name__ = "Integer32"
_RsBWMCurrentExtRulesReportMaxBw_Object = MibTableColumn
rsBWMCurrentExtRulesReportMaxBw = _RsBWMCurrentExtRulesReportMaxBw_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 60, 1, 15),
    _RsBWMCurrentExtRulesReportMaxBw_Type()
)
rsBWMCurrentExtRulesReportMaxBw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMCurrentExtRulesReportMaxBw.setStatus("mandatory")
_RsBWMRulesTreeManager_ObjectIdentity = ObjectIdentity
rsBWMRulesTreeManager = _RsBWMRulesTreeManager_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 61)
)


class _RsBWMRulesTreeName_Type(DisplayString):
    """Custom type rsBWMRulesTreeName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_RsBWMRulesTreeName_Type.__name__ = "DisplayString"
_RsBWMRulesTreeName_Object = MibScalar
rsBWMRulesTreeName = _RsBWMRulesTreeName_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 61, 1),
    _RsBWMRulesTreeName_Type()
)
rsBWMRulesTreeName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMRulesTreeName.setStatus("mandatory")


class _RsBWMRulesTreeNewParentName_Type(DisplayString):
    """Custom type rsBWMRulesTreeNewParentName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_RsBWMRulesTreeNewParentName_Type.__name__ = "DisplayString"
_RsBWMRulesTreeNewParentName_Object = MibScalar
rsBWMRulesTreeNewParentName = _RsBWMRulesTreeNewParentName_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 61, 2),
    _RsBWMRulesTreeNewParentName_Type()
)
rsBWMRulesTreeNewParentName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMRulesTreeNewParentName.setStatus("mandatory")


class _RsBWMRulesTreeAction_Type(Integer32):
    """Custom type rsBWMRulesTreeAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("copy", 1),
          ("move", 2))
    )


_RsBWMRulesTreeAction_Type.__name__ = "Integer32"
_RsBWMRulesTreeAction_Object = MibScalar
rsBWMRulesTreeAction = _RsBWMRulesTreeAction_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 61, 3),
    _RsBWMRulesTreeAction_Type()
)
rsBWMRulesTreeAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMRulesTreeAction.setStatus("mandatory")


class _RsBWMTCPSessionClassification_Type(Integer32):
    """Custom type rsBWMTCPSessionClassification based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_RsBWMTCPSessionClassification_Type.__name__ = "Integer32"
_RsBWMTCPSessionClassification_Object = MibScalar
rsBWMTCPSessionClassification = _RsBWMTCPSessionClassification_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 62),
    _RsBWMTCPSessionClassification_Type()
)
rsBWMTCPSessionClassification.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMTCPSessionClassification.setStatus("mandatory")
_RsBWMNetworkTable_Object = MibTable
rsBWMNetworkTable = _RsBWMNetworkTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 63)
)
if mibBuilder.loadTexts:
    rsBWMNetworkTable.setStatus("mandatory")
_RsBWMNetworkEntry_Object = MibTableRow
rsBWMNetworkEntry = _RsBWMNetworkEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 63, 1)
)
rsBWMNetworkEntry.setIndexNames(
    (0, "BWM-MIB", "rsBWMNetworkName"),
    (0, "BWM-MIB", "rsBWMNetworkSubIndex"),
)
if mibBuilder.loadTexts:
    rsBWMNetworkEntry.setStatus("mandatory")


class _RsBWMNetworkName_Type(DisplayString):
    """Custom type rsBWMNetworkName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 19),
    )


_RsBWMNetworkName_Type.__name__ = "DisplayString"
_RsBWMNetworkName_Object = MibTableColumn
rsBWMNetworkName = _RsBWMNetworkName_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 63, 1, 1),
    _RsBWMNetworkName_Type()
)
rsBWMNetworkName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMNetworkName.setStatus("mandatory")


class _RsBWMNetworkSubIndex_Type(Integer32):
    """Custom type rsBWMNetworkSubIndex based on Integer32"""
    defaultValue = 0


_RsBWMNetworkSubIndex_Type.__name__ = "Integer32"
_RsBWMNetworkSubIndex_Object = MibTableColumn
rsBWMNetworkSubIndex = _RsBWMNetworkSubIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 63, 1, 2),
    _RsBWMNetworkSubIndex_Type()
)
rsBWMNetworkSubIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMNetworkSubIndex.setStatus("mandatory")
_RsBWMNetworkAddress_Type = Ipv6Address
_RsBWMNetworkAddress_Object = MibTableColumn
rsBWMNetworkAddress = _RsBWMNetworkAddress_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 63, 1, 3),
    _RsBWMNetworkAddress_Type()
)
rsBWMNetworkAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMNetworkAddress.setStatus("mandatory")


class _RsBWMNetworkMask_Type(DisplayString):
    """Custom type rsBWMNetworkMask based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 46),
    )


_RsBWMNetworkMask_Type.__name__ = "DisplayString"
_RsBWMNetworkMask_Object = MibTableColumn
rsBWMNetworkMask = _RsBWMNetworkMask_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 63, 1, 4),
    _RsBWMNetworkMask_Type()
)
rsBWMNetworkMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMNetworkMask.setStatus("mandatory")
_RsBWMNetworkFromIP_Type = Ipv6Address
_RsBWMNetworkFromIP_Object = MibTableColumn
rsBWMNetworkFromIP = _RsBWMNetworkFromIP_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 63, 1, 5),
    _RsBWMNetworkFromIP_Type()
)
rsBWMNetworkFromIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMNetworkFromIP.setStatus("mandatory")
_RsBWMNetworkToIP_Type = Ipv6Address
_RsBWMNetworkToIP_Object = MibTableColumn
rsBWMNetworkToIP = _RsBWMNetworkToIP_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 63, 1, 6),
    _RsBWMNetworkToIP_Type()
)
rsBWMNetworkToIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMNetworkToIP.setStatus("mandatory")


class _RsBWMNetworkMode_Type(Integer32):
    """Custom type rsBWMNetworkMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ipMask", 1),
          ("ipRange", 2),
          ("dynamic", 3))
    )


_RsBWMNetworkMode_Type.__name__ = "Integer32"
_RsBWMNetworkMode_Object = MibTableColumn
rsBWMNetworkMode = _RsBWMNetworkMode_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 63, 1, 7),
    _RsBWMNetworkMode_Type()
)
rsBWMNetworkMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMNetworkMode.setStatus("mandatory")
_RsBWMNetworkStatus_Type = RowStatus
_RsBWMNetworkStatus_Object = MibTableColumn
rsBWMNetworkStatus = _RsBWMNetworkStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 63, 1, 8),
    _RsBWMNetworkStatus_Type()
)
rsBWMNetworkStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMNetworkStatus.setStatus("mandatory")
_RsBWMCurrentNetworkTable_Object = MibTable
rsBWMCurrentNetworkTable = _RsBWMCurrentNetworkTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 64)
)
if mibBuilder.loadTexts:
    rsBWMCurrentNetworkTable.setStatus("mandatory")
_RsBWMCurrentNetworkEntry_Object = MibTableRow
rsBWMCurrentNetworkEntry = _RsBWMCurrentNetworkEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 64, 1)
)
rsBWMCurrentNetworkEntry.setIndexNames(
    (0, "BWM-MIB", "rsBWMCurrentNetworkName"),
    (0, "BWM-MIB", "rsBWMCurrentNetworkSubIndex"),
)
if mibBuilder.loadTexts:
    rsBWMCurrentNetworkEntry.setStatus("mandatory")


class _RsBWMCurrentNetworkName_Type(DisplayString):
    """Custom type rsBWMCurrentNetworkName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_RsBWMCurrentNetworkName_Type.__name__ = "DisplayString"
_RsBWMCurrentNetworkName_Object = MibTableColumn
rsBWMCurrentNetworkName = _RsBWMCurrentNetworkName_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 64, 1, 1),
    _RsBWMCurrentNetworkName_Type()
)
rsBWMCurrentNetworkName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMCurrentNetworkName.setStatus("mandatory")
_RsBWMCurrentNetworkSubIndex_Type = Integer32
_RsBWMCurrentNetworkSubIndex_Object = MibTableColumn
rsBWMCurrentNetworkSubIndex = _RsBWMCurrentNetworkSubIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 64, 1, 2),
    _RsBWMCurrentNetworkSubIndex_Type()
)
rsBWMCurrentNetworkSubIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMCurrentNetworkSubIndex.setStatus("mandatory")
_RsBWMCurrentNetworkAddress_Type = Ipv6Address
_RsBWMCurrentNetworkAddress_Object = MibTableColumn
rsBWMCurrentNetworkAddress = _RsBWMCurrentNetworkAddress_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 64, 1, 3),
    _RsBWMCurrentNetworkAddress_Type()
)
rsBWMCurrentNetworkAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMCurrentNetworkAddress.setStatus("mandatory")


class _RsBWMCurrentNetworkMask_Type(DisplayString):
    """Custom type rsBWMCurrentNetworkMask based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 46),
    )


_RsBWMCurrentNetworkMask_Type.__name__ = "DisplayString"
_RsBWMCurrentNetworkMask_Object = MibTableColumn
rsBWMCurrentNetworkMask = _RsBWMCurrentNetworkMask_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 64, 1, 4),
    _RsBWMCurrentNetworkMask_Type()
)
rsBWMCurrentNetworkMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMCurrentNetworkMask.setStatus("mandatory")
_RsBWMCurrentNetworkFromIP_Type = Ipv6Address
_RsBWMCurrentNetworkFromIP_Object = MibTableColumn
rsBWMCurrentNetworkFromIP = _RsBWMCurrentNetworkFromIP_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 64, 1, 5),
    _RsBWMCurrentNetworkFromIP_Type()
)
rsBWMCurrentNetworkFromIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMCurrentNetworkFromIP.setStatus("mandatory")
_RsBWMCurrentNetworkToIP_Type = Ipv6Address
_RsBWMCurrentNetworkToIP_Object = MibTableColumn
rsBWMCurrentNetworkToIP = _RsBWMCurrentNetworkToIP_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 64, 1, 6),
    _RsBWMCurrentNetworkToIP_Type()
)
rsBWMCurrentNetworkToIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMCurrentNetworkToIP.setStatus("mandatory")


class _RsBWMCurrentNetworkMode_Type(Integer32):
    """Custom type rsBWMCurrentNetworkMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ipMask", 1),
          ("ipRange", 2),
          ("dynamic", 3))
    )


_RsBWMCurrentNetworkMode_Type.__name__ = "Integer32"
_RsBWMCurrentNetworkMode_Object = MibTableColumn
rsBWMCurrentNetworkMode = _RsBWMCurrentNetworkMode_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 64, 1, 7),
    _RsBWMCurrentNetworkMode_Type()
)
rsBWMCurrentNetworkMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMCurrentNetworkMode.setStatus("mandatory")
_RsBWMStatisticsNewTable_Object = MibTable
rsBWMStatisticsNewTable = _RsBWMStatisticsNewTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 65)
)
if mibBuilder.loadTexts:
    rsBWMStatisticsNewTable.setStatus("mandatory")
_RsBWMStatisticsNewEntry_Object = MibTableRow
rsBWMStatisticsNewEntry = _RsBWMStatisticsNewEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 65, 1)
)
rsBWMStatisticsNewEntry.setIndexNames(
    (0, "BWM-MIB", "rsBWMStatisticsPolicyKey"),
)
if mibBuilder.loadTexts:
    rsBWMStatisticsNewEntry.setStatus("mandatory")
_RsBWMStatisticsPolicyKey_Type = Integer32
_RsBWMStatisticsPolicyKey_Object = MibTableColumn
rsBWMStatisticsPolicyKey = _RsBWMStatisticsPolicyKey_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 65, 1, 1),
    _RsBWMStatisticsPolicyKey_Type()
)
rsBWMStatisticsPolicyKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMStatisticsPolicyKey.setStatus("mandatory")


class _RsBWMStatisticsPolicyNameSec_Type(DisplayString):
    """Custom type rsBWMStatisticsPolicyNameSec based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_RsBWMStatisticsPolicyNameSec_Type.__name__ = "DisplayString"
_RsBWMStatisticsPolicyNameSec_Object = MibTableColumn
rsBWMStatisticsPolicyNameSec = _RsBWMStatisticsPolicyNameSec_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 65, 1, 2),
    _RsBWMStatisticsPolicyNameSec_Type()
)
rsBWMStatisticsPolicyNameSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMStatisticsPolicyNameSec.setStatus("mandatory")
_RsBWMStatisticsBandwidthUsedSecond_Type = Counter32
_RsBWMStatisticsBandwidthUsedSecond_Object = MibTableColumn
rsBWMStatisticsBandwidthUsedSecond = _RsBWMStatisticsBandwidthUsedSecond_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 65, 1, 3),
    _RsBWMStatisticsBandwidthUsedSecond_Type()
)
rsBWMStatisticsBandwidthUsedSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMStatisticsBandwidthUsedSecond.setStatus("mandatory")
_RsBWMStatisticsPacketNumberSecond_Type = Counter32
_RsBWMStatisticsPacketNumberSecond_Object = MibTableColumn
rsBWMStatisticsPacketNumberSecond = _RsBWMStatisticsPacketNumberSecond_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 65, 1, 4),
    _RsBWMStatisticsPacketNumberSecond_Type()
)
rsBWMStatisticsPacketNumberSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMStatisticsPacketNumberSecond.setStatus("mandatory")
_RsBWMStatisticsGuaranteedReachedSecond_Type = TruthValue
_RsBWMStatisticsGuaranteedReachedSecond_Object = MibTableColumn
rsBWMStatisticsGuaranteedReachedSecond = _RsBWMStatisticsGuaranteedReachedSecond_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 65, 1, 5),
    _RsBWMStatisticsGuaranteedReachedSecond_Type()
)
rsBWMStatisticsGuaranteedReachedSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMStatisticsGuaranteedReachedSecond.setStatus("mandatory")
_RsBWMStatisticsMaximumReachedSecond_Type = TruthValue
_RsBWMStatisticsMaximumReachedSecond_Object = MibTableColumn
rsBWMStatisticsMaximumReachedSecond = _RsBWMStatisticsMaximumReachedSecond_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 65, 1, 6),
    _RsBWMStatisticsMaximumReachedSecond_Type()
)
rsBWMStatisticsMaximumReachedSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMStatisticsMaximumReachedSecond.setStatus("mandatory")
_RsBWMStatisticsMatchedBandwidthSecond_Type = Counter32
_RsBWMStatisticsMatchedBandwidthSecond_Object = MibTableColumn
rsBWMStatisticsMatchedBandwidthSecond = _RsBWMStatisticsMatchedBandwidthSecond_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 65, 1, 7),
    _RsBWMStatisticsMatchedBandwidthSecond_Type()
)
rsBWMStatisticsMatchedBandwidthSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMStatisticsMatchedBandwidthSecond.setStatus("mandatory")
_RsBWMStatisticsInboundBandwidthUsedSecond_Type = Counter32
_RsBWMStatisticsInboundBandwidthUsedSecond_Object = MibTableColumn
rsBWMStatisticsInboundBandwidthUsedSecond = _RsBWMStatisticsInboundBandwidthUsedSecond_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 65, 1, 8),
    _RsBWMStatisticsInboundBandwidthUsedSecond_Type()
)
rsBWMStatisticsInboundBandwidthUsedSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMStatisticsInboundBandwidthUsedSecond.setStatus("mandatory")
_RsBWMStatisticsInboundMatchedBandwidthSecond_Type = Counter32
_RsBWMStatisticsInboundMatchedBandwidthSecond_Object = MibTableColumn
rsBWMStatisticsInboundMatchedBandwidthSecond = _RsBWMStatisticsInboundMatchedBandwidthSecond_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 65, 1, 9),
    _RsBWMStatisticsInboundMatchedBandwidthSecond_Type()
)
rsBWMStatisticsInboundMatchedBandwidthSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMStatisticsInboundMatchedBandwidthSecond.setStatus("mandatory")
_RsBWMStatisticsInboundPacketNumberSecond_Type = Counter32
_RsBWMStatisticsInboundPacketNumberSecond_Object = MibTableColumn
rsBWMStatisticsInboundPacketNumberSecond = _RsBWMStatisticsInboundPacketNumberSecond_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 65, 1, 10),
    _RsBWMStatisticsInboundPacketNumberSecond_Type()
)
rsBWMStatisticsInboundPacketNumberSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMStatisticsInboundPacketNumberSecond.setStatus("mandatory")
_RsBWMStatisticsOutboundBandwidthUsedSecond_Type = Counter32
_RsBWMStatisticsOutboundBandwidthUsedSecond_Object = MibTableColumn
rsBWMStatisticsOutboundBandwidthUsedSecond = _RsBWMStatisticsOutboundBandwidthUsedSecond_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 65, 1, 11),
    _RsBWMStatisticsOutboundBandwidthUsedSecond_Type()
)
rsBWMStatisticsOutboundBandwidthUsedSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMStatisticsOutboundBandwidthUsedSecond.setStatus("mandatory")
_RsBWMStatisticsOutboundMatchedBandwidthSecond_Type = Counter32
_RsBWMStatisticsOutboundMatchedBandwidthSecond_Object = MibTableColumn
rsBWMStatisticsOutboundMatchedBandwidthSecond = _RsBWMStatisticsOutboundMatchedBandwidthSecond_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 65, 1, 12),
    _RsBWMStatisticsOutboundMatchedBandwidthSecond_Type()
)
rsBWMStatisticsOutboundMatchedBandwidthSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMStatisticsOutboundMatchedBandwidthSecond.setStatus("mandatory")
_RsBWMStatisticsOutboundPacketNumberSecond_Type = Counter32
_RsBWMStatisticsOutboundPacketNumberSecond_Object = MibTableColumn
rsBWMStatisticsOutboundPacketNumberSecond = _RsBWMStatisticsOutboundPacketNumberSecond_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 65, 1, 13),
    _RsBWMStatisticsOutboundPacketNumberSecond_Type()
)
rsBWMStatisticsOutboundPacketNumberSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMStatisticsOutboundPacketNumberSecond.setStatus("mandatory")
_RsBWMStatisticsNewTCPConnectionsSecond_Type = Counter32
_RsBWMStatisticsNewTCPConnectionsSecond_Object = MibTableColumn
rsBWMStatisticsNewTCPConnectionsSecond = _RsBWMStatisticsNewTCPConnectionsSecond_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 65, 1, 14),
    _RsBWMStatisticsNewTCPConnectionsSecond_Type()
)
rsBWMStatisticsNewTCPConnectionsSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMStatisticsNewTCPConnectionsSecond.setStatus("mandatory")
_RsBWMStatisticsNewUDPConnectionsSecond_Type = Counter32
_RsBWMStatisticsNewUDPConnectionsSecond_Object = MibTableColumn
rsBWMStatisticsNewUDPConnectionsSecond = _RsBWMStatisticsNewUDPConnectionsSecond_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 65, 1, 15),
    _RsBWMStatisticsNewUDPConnectionsSecond_Type()
)
rsBWMStatisticsNewUDPConnectionsSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMStatisticsNewUDPConnectionsSecond.setStatus("mandatory")
_RsBWMStatisticsQueuedBWSecond_Type = Counter32
_RsBWMStatisticsQueuedBWSecond_Object = MibTableColumn
rsBWMStatisticsQueuedBWSecond = _RsBWMStatisticsQueuedBWSecond_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 65, 1, 16),
    _RsBWMStatisticsQueuedBWSecond_Type()
)
rsBWMStatisticsQueuedBWSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMStatisticsQueuedBWSecond.setStatus("mandatory")
_RsBWMStatisticsBandwidthUsedPeriod_Type = Counter32
_RsBWMStatisticsBandwidthUsedPeriod_Object = MibTableColumn
rsBWMStatisticsBandwidthUsedPeriod = _RsBWMStatisticsBandwidthUsedPeriod_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 65, 1, 17),
    _RsBWMStatisticsBandwidthUsedPeriod_Type()
)
rsBWMStatisticsBandwidthUsedPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMStatisticsBandwidthUsedPeriod.setStatus("mandatory")
_RsBWMStatisticsPeakBandwidthPeriod_Type = Counter32
_RsBWMStatisticsPeakBandwidthPeriod_Object = MibTableColumn
rsBWMStatisticsPeakBandwidthPeriod = _RsBWMStatisticsPeakBandwidthPeriod_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 65, 1, 18),
    _RsBWMStatisticsPeakBandwidthPeriod_Type()
)
rsBWMStatisticsPeakBandwidthPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMStatisticsPeakBandwidthPeriod.setStatus("mandatory")
_RsBWMStatisticsPacketNumberPeriod_Type = Counter32
_RsBWMStatisticsPacketNumberPeriod_Object = MibTableColumn
rsBWMStatisticsPacketNumberPeriod = _RsBWMStatisticsPacketNumberPeriod_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 65, 1, 19),
    _RsBWMStatisticsPacketNumberPeriod_Type()
)
rsBWMStatisticsPacketNumberPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMStatisticsPacketNumberPeriod.setStatus("mandatory")
_RsBWMStatisticsGuaranteedReachedCounterPeriod_Type = Integer32
_RsBWMStatisticsGuaranteedReachedCounterPeriod_Object = MibTableColumn
rsBWMStatisticsGuaranteedReachedCounterPeriod = _RsBWMStatisticsGuaranteedReachedCounterPeriod_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 65, 1, 20),
    _RsBWMStatisticsGuaranteedReachedCounterPeriod_Type()
)
rsBWMStatisticsGuaranteedReachedCounterPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMStatisticsGuaranteedReachedCounterPeriod.setStatus("mandatory")
_RsBWMStatisticsMaximumReachedCounterPeriod_Type = Integer32
_RsBWMStatisticsMaximumReachedCounterPeriod_Object = MibTableColumn
rsBWMStatisticsMaximumReachedCounterPeriod = _RsBWMStatisticsMaximumReachedCounterPeriod_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 65, 1, 21),
    _RsBWMStatisticsMaximumReachedCounterPeriod_Type()
)
rsBWMStatisticsMaximumReachedCounterPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMStatisticsMaximumReachedCounterPeriod.setStatus("mandatory")
_RsBWMStatisticsMatchedBandwidthPeriod_Type = Counter32
_RsBWMStatisticsMatchedBandwidthPeriod_Object = MibTableColumn
rsBWMStatisticsMatchedBandwidthPeriod = _RsBWMStatisticsMatchedBandwidthPeriod_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 65, 1, 22),
    _RsBWMStatisticsMatchedBandwidthPeriod_Type()
)
rsBWMStatisticsMatchedBandwidthPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMStatisticsMatchedBandwidthPeriod.setStatus("mandatory")
_RsBWMStatisticsInboundBandwidthUsedPeriod_Type = Counter32
_RsBWMStatisticsInboundBandwidthUsedPeriod_Object = MibTableColumn
rsBWMStatisticsInboundBandwidthUsedPeriod = _RsBWMStatisticsInboundBandwidthUsedPeriod_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 65, 1, 23),
    _RsBWMStatisticsInboundBandwidthUsedPeriod_Type()
)
rsBWMStatisticsInboundBandwidthUsedPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMStatisticsInboundBandwidthUsedPeriod.setStatus("mandatory")
_RsBWMStatisticsInboundMatchedBandwidthPeriod_Type = Counter32
_RsBWMStatisticsInboundMatchedBandwidthPeriod_Object = MibTableColumn
rsBWMStatisticsInboundMatchedBandwidthPeriod = _RsBWMStatisticsInboundMatchedBandwidthPeriod_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 65, 1, 24),
    _RsBWMStatisticsInboundMatchedBandwidthPeriod_Type()
)
rsBWMStatisticsInboundMatchedBandwidthPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMStatisticsInboundMatchedBandwidthPeriod.setStatus("mandatory")
_RsBWMStatisticsInboundPacketNumberPeriod_Type = Counter32
_RsBWMStatisticsInboundPacketNumberPeriod_Object = MibTableColumn
rsBWMStatisticsInboundPacketNumberPeriod = _RsBWMStatisticsInboundPacketNumberPeriod_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 65, 1, 25),
    _RsBWMStatisticsInboundPacketNumberPeriod_Type()
)
rsBWMStatisticsInboundPacketNumberPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMStatisticsInboundPacketNumberPeriod.setStatus("mandatory")
_RsBWMStatisticsOutboundBandwidthUsedPeriod_Type = Counter32
_RsBWMStatisticsOutboundBandwidthUsedPeriod_Object = MibTableColumn
rsBWMStatisticsOutboundBandwidthUsedPeriod = _RsBWMStatisticsOutboundBandwidthUsedPeriod_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 65, 1, 26),
    _RsBWMStatisticsOutboundBandwidthUsedPeriod_Type()
)
rsBWMStatisticsOutboundBandwidthUsedPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMStatisticsOutboundBandwidthUsedPeriod.setStatus("mandatory")
_RsBWMStatisticsOutboundMatchedBandwidthPeriod_Type = Counter32
_RsBWMStatisticsOutboundMatchedBandwidthPeriod_Object = MibTableColumn
rsBWMStatisticsOutboundMatchedBandwidthPeriod = _RsBWMStatisticsOutboundMatchedBandwidthPeriod_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 65, 1, 27),
    _RsBWMStatisticsOutboundMatchedBandwidthPeriod_Type()
)
rsBWMStatisticsOutboundMatchedBandwidthPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMStatisticsOutboundMatchedBandwidthPeriod.setStatus("mandatory")
_RsBWMStatisticsOutboundPacketNumberPeriod_Type = Counter32
_RsBWMStatisticsOutboundPacketNumberPeriod_Object = MibTableColumn
rsBWMStatisticsOutboundPacketNumberPeriod = _RsBWMStatisticsOutboundPacketNumberPeriod_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 65, 1, 28),
    _RsBWMStatisticsOutboundPacketNumberPeriod_Type()
)
rsBWMStatisticsOutboundPacketNumberPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMStatisticsOutboundPacketNumberPeriod.setStatus("mandatory")
_RsBWMStatisticsNewTCPConnectionsPeriod_Type = Counter32
_RsBWMStatisticsNewTCPConnectionsPeriod_Object = MibTableColumn
rsBWMStatisticsNewTCPConnectionsPeriod = _RsBWMStatisticsNewTCPConnectionsPeriod_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 65, 1, 29),
    _RsBWMStatisticsNewTCPConnectionsPeriod_Type()
)
rsBWMStatisticsNewTCPConnectionsPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMStatisticsNewTCPConnectionsPeriod.setStatus("mandatory")
_RsBWMStatisticsNewUDPConnectionsPeriod_Type = Counter32
_RsBWMStatisticsNewUDPConnectionsPeriod_Object = MibTableColumn
rsBWMStatisticsNewUDPConnectionsPeriod = _RsBWMStatisticsNewUDPConnectionsPeriod_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 65, 1, 30),
    _RsBWMStatisticsNewUDPConnectionsPeriod_Type()
)
rsBWMStatisticsNewUDPConnectionsPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMStatisticsNewUDPConnectionsPeriod.setStatus("mandatory")
_RsBWMStatisticsQueuedBWPeriod_Type = Counter32
_RsBWMStatisticsQueuedBWPeriod_Object = MibTableColumn
rsBWMStatisticsQueuedBWPeriod = _RsBWMStatisticsQueuedBWPeriod_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 65, 1, 31),
    _RsBWMStatisticsQueuedBWPeriod_Type()
)
rsBWMStatisticsQueuedBWPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMStatisticsQueuedBWPeriod.setStatus("mandatory")
_RsBWMPoliciesTable_Object = MibTable
rsBWMPoliciesTable = _RsBWMPoliciesTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 66)
)
if mibBuilder.loadTexts:
    rsBWMPoliciesTable.setStatus("mandatory")
_RsBWMPolicyEntry_Object = MibTableRow
rsBWMPolicyEntry = _RsBWMPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 66, 1)
)
rsBWMPolicyEntry.setIndexNames(
    (0, "BWM-MIB", "rsBWMPolicyKey"),
)
if mibBuilder.loadTexts:
    rsBWMPolicyEntry.setStatus("mandatory")
_RsBWMPolicyKey_Type = Integer32
_RsBWMPolicyKey_Object = MibTableColumn
rsBWMPolicyKey = _RsBWMPolicyKey_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 66, 1, 1),
    _RsBWMPolicyKey_Type()
)
rsBWMPolicyKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMPolicyKey.setStatus("mandatory")


class _RsBWMPolicyName_Type(DisplayString):
    """Custom type rsBWMPolicyName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_RsBWMPolicyName_Type.__name__ = "DisplayString"
_RsBWMPolicyName_Object = MibTableColumn
rsBWMPolicyName = _RsBWMPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 66, 1, 2),
    _RsBWMPolicyName_Type()
)
rsBWMPolicyName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMPolicyName.setStatus("mandatory")
_RsBWMPolicyIndex_Type = Integer32
_RsBWMPolicyIndex_Object = MibTableColumn
rsBWMPolicyIndex = _RsBWMPolicyIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 66, 1, 3),
    _RsBWMPolicyIndex_Type()
)
rsBWMPolicyIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMPolicyIndex.setStatus("mandatory")


class _RsBWMPolicyDestination_Type(DisplayString):
    """Custom type rsBWMPolicyDestination based on DisplayString"""
    defaultValue = OctetString("any")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 46),
    )


_RsBWMPolicyDestination_Type.__name__ = "DisplayString"
_RsBWMPolicyDestination_Object = MibTableColumn
rsBWMPolicyDestination = _RsBWMPolicyDestination_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 66, 1, 4),
    _RsBWMPolicyDestination_Type()
)
rsBWMPolicyDestination.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMPolicyDestination.setStatus("mandatory")


class _RsBWMPolicySource_Type(DisplayString):
    """Custom type rsBWMPolicySource based on DisplayString"""
    defaultValue = OctetString("any")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 46),
    )


_RsBWMPolicySource_Type.__name__ = "DisplayString"
_RsBWMPolicySource_Object = MibTableColumn
rsBWMPolicySource = _RsBWMPolicySource_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 66, 1, 5),
    _RsBWMPolicySource_Type()
)
rsBWMPolicySource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMPolicySource.setStatus("mandatory")


class _RsBWMPolicyAction_Type(Integer32):
    """Custom type rsBWMPolicyAction based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("forward", 1),
          ("block", 2),
          ("blockAndReset", 3),
          ("blockAndBiDirectionalReset", 4),
          ("monitorHTTP", 5),
          ("monitorHTTPS", 6),
          ("monitorTCP", 7))
    )


_RsBWMPolicyAction_Type.__name__ = "Integer32"
_RsBWMPolicyAction_Object = MibTableColumn
rsBWMPolicyAction = _RsBWMPolicyAction_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 66, 1, 6),
    _RsBWMPolicyAction_Type()
)
rsBWMPolicyAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMPolicyAction.setStatus("mandatory")


class _RsBWMPolicyDirection_Type(Integer32):
    """Custom type rsBWMPolicyDirection based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("oneway", 1),
          ("twoway", 2),
          ("session", 3))
    )


_RsBWMPolicyDirection_Type.__name__ = "Integer32"
_RsBWMPolicyDirection_Object = MibTableColumn
rsBWMPolicyDirection = _RsBWMPolicyDirection_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 66, 1, 7),
    _RsBWMPolicyDirection_Type()
)
rsBWMPolicyDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMPolicyDirection.setStatus("mandatory")


class _RsBWMPolicyPriority_Type(Integer32):
    """Custom type rsBWMPolicyPriority based on Integer32"""
    defaultValue = 65535


_RsBWMPolicyPriority_Type.__name__ = "Integer32"
_RsBWMPolicyPriority_Object = MibTableColumn
rsBWMPolicyPriority = _RsBWMPolicyPriority_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 66, 1, 8),
    _RsBWMPolicyPriority_Type()
)
rsBWMPolicyPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMPolicyPriority.setStatus("mandatory")


class _RsBWMPolicyType_Type(Integer32):
    """Custom type rsBWMPolicyType based on Integer32"""
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
        *(("facsBandwidth", 1),
          ("counter", 2),
          ("ids", 3),
          ("chain", 4))
    )


_RsBWMPolicyType_Type.__name__ = "Integer32"
_RsBWMPolicyType_Object = MibTableColumn
rsBWMPolicyType = _RsBWMPolicyType_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 66, 1, 9),
    _RsBWMPolicyType_Type()
)
rsBWMPolicyType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMPolicyType.setStatus("mandatory")


class _RsBWMPolicyDescription_Type(DisplayString):
    """Custom type rsBWMPolicyDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_RsBWMPolicyDescription_Type.__name__ = "DisplayString"
_RsBWMPolicyDescription_Object = MibTableColumn
rsBWMPolicyDescription = _RsBWMPolicyDescription_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 66, 1, 10),
    _RsBWMPolicyDescription_Type()
)
rsBWMPolicyDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMPolicyDescription.setStatus("mandatory")


class _RsBWMPolicyGuaranteedBW_Type(Integer32):
    """Custom type rsBWMPolicyGuaranteedBW based on Integer32"""
    defaultValue = 0


_RsBWMPolicyGuaranteedBW_Type.__name__ = "Integer32"
_RsBWMPolicyGuaranteedBW_Object = MibTableColumn
rsBWMPolicyGuaranteedBW = _RsBWMPolicyGuaranteedBW_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 66, 1, 11),
    _RsBWMPolicyGuaranteedBW_Type()
)
rsBWMPolicyGuaranteedBW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMPolicyGuaranteedBW.setStatus("mandatory")


class _RsBWMPolicyFilterType_Type(Integer32):
    """Custom type rsBWMPolicyFilterType based on Integer32"""
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
        *(("none", 1),
          ("filter", 2),
          ("group", 3),
          ("policy", 4))
    )


_RsBWMPolicyFilterType_Type.__name__ = "Integer32"
_RsBWMPolicyFilterType_Object = MibTableColumn
rsBWMPolicyFilterType = _RsBWMPolicyFilterType_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 66, 1, 12),
    _RsBWMPolicyFilterType_Type()
)
rsBWMPolicyFilterType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMPolicyFilterType.setStatus("mandatory")


class _RsBWMPolicyFilter_Type(DisplayString):
    """Custom type rsBWMPolicyFilter based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_RsBWMPolicyFilter_Type.__name__ = "DisplayString"
_RsBWMPolicyFilter_Object = MibTableColumn
rsBWMPolicyFilter = _RsBWMPolicyFilter_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 66, 1, 13),
    _RsBWMPolicyFilter_Type()
)
rsBWMPolicyFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMPolicyFilter.setStatus("mandatory")


class _RsBWMPolicyOperationalStatus_Type(Integer32):
    """Custom type rsBWMPolicyOperationalStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_RsBWMPolicyOperationalStatus_Type.__name__ = "Integer32"
_RsBWMPolicyOperationalStatus_Object = MibTableColumn
rsBWMPolicyOperationalStatus = _RsBWMPolicyOperationalStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 66, 1, 14),
    _RsBWMPolicyOperationalStatus_Type()
)
rsBWMPolicyOperationalStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMPolicyOperationalStatus.setStatus("mandatory")


class _RsBWMPolicyReportBlockedPackets_Type(Integer32):
    """Custom type rsBWMPolicyReportBlockedPackets based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1),
          ("securityEvent", 2))
    )


_RsBWMPolicyReportBlockedPackets_Type.__name__ = "Integer32"
_RsBWMPolicyReportBlockedPackets_Object = MibTableColumn
rsBWMPolicyReportBlockedPackets = _RsBWMPolicyReportBlockedPackets_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 66, 1, 15),
    _RsBWMPolicyReportBlockedPackets_Type()
)
rsBWMPolicyReportBlockedPackets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMPolicyReportBlockedPackets.setStatus("mandatory")


class _RsBWMPolicyMaxBW_Type(Integer32):
    """Custom type rsBWMPolicyMaxBW based on Integer32"""
    defaultValue = 0


_RsBWMPolicyMaxBW_Type.__name__ = "Integer32"
_RsBWMPolicyMaxBW_Object = MibTableColumn
rsBWMPolicyMaxBW = _RsBWMPolicyMaxBW_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 66, 1, 16),
    _RsBWMPolicyMaxBW_Type()
)
rsBWMPolicyMaxBW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMPolicyMaxBW.setStatus("mandatory")


class _RsBWMPolicyPhysicalPortGroup_Type(DisplayString):
    """Custom type rsBWMPolicyPhysicalPortGroup based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_RsBWMPolicyPhysicalPortGroup_Type.__name__ = "DisplayString"
_RsBWMPolicyPhysicalPortGroup_Object = MibTableColumn
rsBWMPolicyPhysicalPortGroup = _RsBWMPolicyPhysicalPortGroup_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 66, 1, 17),
    _RsBWMPolicyPhysicalPortGroup_Type()
)
rsBWMPolicyPhysicalPortGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMPolicyPhysicalPortGroup.setStatus("mandatory")


class _RsBWMPolicyVLANTagGroup_Type(DisplayString):
    """Custom type rsBWMPolicyVLANTagGroup based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_RsBWMPolicyVLANTagGroup_Type.__name__ = "DisplayString"
_RsBWMPolicyVLANTagGroup_Object = MibTableColumn
rsBWMPolicyVLANTagGroup = _RsBWMPolicyVLANTagGroup_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 66, 1, 18),
    _RsBWMPolicyVLANTagGroup_Type()
)
rsBWMPolicyVLANTagGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMPolicyVLANTagGroup.setStatus("mandatory")


class _RsBWMPolicySpecific_Type(DisplayString):
    """Custom type rsBWMPolicySpecific based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_RsBWMPolicySpecific_Type.__name__ = "DisplayString"
_RsBWMPolicySpecific_Object = MibTableColumn
rsBWMPolicySpecific = _RsBWMPolicySpecific_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 66, 1, 19),
    _RsBWMPolicySpecific_Type()
)
rsBWMPolicySpecific.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMPolicySpecific.setStatus("mandatory")
_RsBWMPolicyStatus_Type = RowStatus
_RsBWMPolicyStatus_Object = MibTableColumn
rsBWMPolicyStatus = _RsBWMPolicyStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 66, 1, 20),
    _RsBWMPolicyStatus_Type()
)
rsBWMPolicyStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMPolicyStatus.setStatus("mandatory")


class _RsBWMPolicyRadiusRule_Type(DisplayString):
    """Custom type rsBWMPolicyRadiusRule based on DisplayString"""
    defaultValue = OctetString("any")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_RsBWMPolicyRadiusRule_Type.__name__ = "DisplayString"
_RsBWMPolicyRadiusRule_Object = MibTableColumn
rsBWMPolicyRadiusRule = _RsBWMPolicyRadiusRule_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 66, 1, 21),
    _RsBWMPolicyRadiusRule_Type()
)
rsBWMPolicyRadiusRule.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMPolicyRadiusRule.setStatus("mandatory")
_RsBWMCurrentPoliciesTable_Object = MibTable
rsBWMCurrentPoliciesTable = _RsBWMCurrentPoliciesTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 67)
)
if mibBuilder.loadTexts:
    rsBWMCurrentPoliciesTable.setStatus("mandatory")
_RsBWMCurrentPolicyEntry_Object = MibTableRow
rsBWMCurrentPolicyEntry = _RsBWMCurrentPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 67, 1)
)
rsBWMCurrentPolicyEntry.setIndexNames(
    (0, "BWM-MIB", "rsBWMCurrentPolicyKey"),
)
if mibBuilder.loadTexts:
    rsBWMCurrentPolicyEntry.setStatus("mandatory")
_RsBWMCurrentPolicyKey_Type = Integer32
_RsBWMCurrentPolicyKey_Object = MibTableColumn
rsBWMCurrentPolicyKey = _RsBWMCurrentPolicyKey_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 67, 1, 1),
    _RsBWMCurrentPolicyKey_Type()
)
rsBWMCurrentPolicyKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMCurrentPolicyKey.setStatus("mandatory")


class _RsBWMCurrentPolicyName_Type(DisplayString):
    """Custom type rsBWMCurrentPolicyName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_RsBWMCurrentPolicyName_Type.__name__ = "DisplayString"
_RsBWMCurrentPolicyName_Object = MibTableColumn
rsBWMCurrentPolicyName = _RsBWMCurrentPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 67, 1, 2),
    _RsBWMCurrentPolicyName_Type()
)
rsBWMCurrentPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMCurrentPolicyName.setStatus("mandatory")
_RsBWMCurrentPolicyIndex_Type = Integer32
_RsBWMCurrentPolicyIndex_Object = MibTableColumn
rsBWMCurrentPolicyIndex = _RsBWMCurrentPolicyIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 67, 1, 3),
    _RsBWMCurrentPolicyIndex_Type()
)
rsBWMCurrentPolicyIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMCurrentPolicyIndex.setStatus("mandatory")


class _RsBWMCurrentPolicyDestination_Type(DisplayString):
    """Custom type rsBWMCurrentPolicyDestination based on DisplayString"""
    defaultValue = OctetString("any")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 46),
    )


_RsBWMCurrentPolicyDestination_Type.__name__ = "DisplayString"
_RsBWMCurrentPolicyDestination_Object = MibTableColumn
rsBWMCurrentPolicyDestination = _RsBWMCurrentPolicyDestination_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 67, 1, 4),
    _RsBWMCurrentPolicyDestination_Type()
)
rsBWMCurrentPolicyDestination.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMCurrentPolicyDestination.setStatus("mandatory")


class _RsBWMCurrentPolicySource_Type(DisplayString):
    """Custom type rsBWMCurrentPolicySource based on DisplayString"""
    defaultValue = OctetString("any")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 46),
    )


_RsBWMCurrentPolicySource_Type.__name__ = "DisplayString"
_RsBWMCurrentPolicySource_Object = MibTableColumn
rsBWMCurrentPolicySource = _RsBWMCurrentPolicySource_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 67, 1, 5),
    _RsBWMCurrentPolicySource_Type()
)
rsBWMCurrentPolicySource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMCurrentPolicySource.setStatus("mandatory")


class _RsBWMCurrentPolicyAction_Type(Integer32):
    """Custom type rsBWMCurrentPolicyAction based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("forward", 1),
          ("block", 2),
          ("blockAndReset", 3),
          ("blockAndBiDirectionalReset", 4),
          ("monitorHTTP", 5),
          ("monitorHTTPS", 6),
          ("monitorTCP", 7))
    )


_RsBWMCurrentPolicyAction_Type.__name__ = "Integer32"
_RsBWMCurrentPolicyAction_Object = MibTableColumn
rsBWMCurrentPolicyAction = _RsBWMCurrentPolicyAction_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 67, 1, 6),
    _RsBWMCurrentPolicyAction_Type()
)
rsBWMCurrentPolicyAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMCurrentPolicyAction.setStatus("mandatory")


class _RsBWMCurrentPolicyDirection_Type(Integer32):
    """Custom type rsBWMCurrentPolicyDirection based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("oneway", 1),
          ("twoway", 2),
          ("session", 3))
    )


_RsBWMCurrentPolicyDirection_Type.__name__ = "Integer32"
_RsBWMCurrentPolicyDirection_Object = MibTableColumn
rsBWMCurrentPolicyDirection = _RsBWMCurrentPolicyDirection_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 67, 1, 7),
    _RsBWMCurrentPolicyDirection_Type()
)
rsBWMCurrentPolicyDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMCurrentPolicyDirection.setStatus("mandatory")


class _RsBWMCurrentPolicyPriority_Type(Integer32):
    """Custom type rsBWMCurrentPolicyPriority based on Integer32"""
    defaultValue = 65535


_RsBWMCurrentPolicyPriority_Type.__name__ = "Integer32"
_RsBWMCurrentPolicyPriority_Object = MibTableColumn
rsBWMCurrentPolicyPriority = _RsBWMCurrentPolicyPriority_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 67, 1, 8),
    _RsBWMCurrentPolicyPriority_Type()
)
rsBWMCurrentPolicyPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMCurrentPolicyPriority.setStatus("mandatory")


class _RsBWMCurrentPolicyType_Type(Integer32):
    """Custom type rsBWMCurrentPolicyType based on Integer32"""
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
        *(("facsBandwidth", 1),
          ("counter", 2),
          ("ids", 3),
          ("chain", 4))
    )


_RsBWMCurrentPolicyType_Type.__name__ = "Integer32"
_RsBWMCurrentPolicyType_Object = MibTableColumn
rsBWMCurrentPolicyType = _RsBWMCurrentPolicyType_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 67, 1, 9),
    _RsBWMCurrentPolicyType_Type()
)
rsBWMCurrentPolicyType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMCurrentPolicyType.setStatus("mandatory")


class _RsBWMCurrentPolicyDescription_Type(DisplayString):
    """Custom type rsBWMCurrentPolicyDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_RsBWMCurrentPolicyDescription_Type.__name__ = "DisplayString"
_RsBWMCurrentPolicyDescription_Object = MibTableColumn
rsBWMCurrentPolicyDescription = _RsBWMCurrentPolicyDescription_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 67, 1, 10),
    _RsBWMCurrentPolicyDescription_Type()
)
rsBWMCurrentPolicyDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMCurrentPolicyDescription.setStatus("mandatory")


class _RsBWMCurrentPolicyGuaranteedBW_Type(Integer32):
    """Custom type rsBWMCurrentPolicyGuaranteedBW based on Integer32"""
    defaultValue = 0


_RsBWMCurrentPolicyGuaranteedBW_Type.__name__ = "Integer32"
_RsBWMCurrentPolicyGuaranteedBW_Object = MibTableColumn
rsBWMCurrentPolicyGuaranteedBW = _RsBWMCurrentPolicyGuaranteedBW_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 67, 1, 11),
    _RsBWMCurrentPolicyGuaranteedBW_Type()
)
rsBWMCurrentPolicyGuaranteedBW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMCurrentPolicyGuaranteedBW.setStatus("mandatory")


class _RsBWMCurrentPolicyFilterType_Type(Integer32):
    """Custom type rsBWMCurrentPolicyFilterType based on Integer32"""
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
        *(("none", 1),
          ("filter", 2),
          ("group", 3),
          ("policy", 4))
    )


_RsBWMCurrentPolicyFilterType_Type.__name__ = "Integer32"
_RsBWMCurrentPolicyFilterType_Object = MibTableColumn
rsBWMCurrentPolicyFilterType = _RsBWMCurrentPolicyFilterType_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 67, 1, 12),
    _RsBWMCurrentPolicyFilterType_Type()
)
rsBWMCurrentPolicyFilterType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMCurrentPolicyFilterType.setStatus("mandatory")


class _RsBWMCurrentPolicyFilter_Type(DisplayString):
    """Custom type rsBWMCurrentPolicyFilter based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_RsBWMCurrentPolicyFilter_Type.__name__ = "DisplayString"
_RsBWMCurrentPolicyFilter_Object = MibTableColumn
rsBWMCurrentPolicyFilter = _RsBWMCurrentPolicyFilter_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 67, 1, 13),
    _RsBWMCurrentPolicyFilter_Type()
)
rsBWMCurrentPolicyFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMCurrentPolicyFilter.setStatus("mandatory")


class _RsBWMCurrentPolicyReportBlockedPackets_Type(Integer32):
    """Custom type rsBWMCurrentPolicyReportBlockedPackets based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1),
          ("securityEvent", 2))
    )


_RsBWMCurrentPolicyReportBlockedPackets_Type.__name__ = "Integer32"
_RsBWMCurrentPolicyReportBlockedPackets_Object = MibTableColumn
rsBWMCurrentPolicyReportBlockedPackets = _RsBWMCurrentPolicyReportBlockedPackets_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 67, 1, 14),
    _RsBWMCurrentPolicyReportBlockedPackets_Type()
)
rsBWMCurrentPolicyReportBlockedPackets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMCurrentPolicyReportBlockedPackets.setStatus("mandatory")


class _RsBWMCurrentPolicyMaxBW_Type(Integer32):
    """Custom type rsBWMCurrentPolicyMaxBW based on Integer32"""
    defaultValue = 0


_RsBWMCurrentPolicyMaxBW_Type.__name__ = "Integer32"
_RsBWMCurrentPolicyMaxBW_Object = MibTableColumn
rsBWMCurrentPolicyMaxBW = _RsBWMCurrentPolicyMaxBW_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 67, 1, 15),
    _RsBWMCurrentPolicyMaxBW_Type()
)
rsBWMCurrentPolicyMaxBW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMCurrentPolicyMaxBW.setStatus("mandatory")


class _RsBWMCurrentPolicyPhysicalPortGroup_Type(DisplayString):
    """Custom type rsBWMCurrentPolicyPhysicalPortGroup based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_RsBWMCurrentPolicyPhysicalPortGroup_Type.__name__ = "DisplayString"
_RsBWMCurrentPolicyPhysicalPortGroup_Object = MibTableColumn
rsBWMCurrentPolicyPhysicalPortGroup = _RsBWMCurrentPolicyPhysicalPortGroup_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 67, 1, 16),
    _RsBWMCurrentPolicyPhysicalPortGroup_Type()
)
rsBWMCurrentPolicyPhysicalPortGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMCurrentPolicyPhysicalPortGroup.setStatus("mandatory")


class _RsBWMCurrentPolicyVLANTagGroup_Type(DisplayString):
    """Custom type rsBWMCurrentPolicyVLANTagGroup based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_RsBWMCurrentPolicyVLANTagGroup_Type.__name__ = "DisplayString"
_RsBWMCurrentPolicyVLANTagGroup_Object = MibTableColumn
rsBWMCurrentPolicyVLANTagGroup = _RsBWMCurrentPolicyVLANTagGroup_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 67, 1, 17),
    _RsBWMCurrentPolicyVLANTagGroup_Type()
)
rsBWMCurrentPolicyVLANTagGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMCurrentPolicyVLANTagGroup.setStatus("mandatory")


class _RsBWMCurrentPolicySpecific_Type(DisplayString):
    """Custom type rsBWMCurrentPolicySpecific based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_RsBWMCurrentPolicySpecific_Type.__name__ = "DisplayString"
_RsBWMCurrentPolicySpecific_Object = MibTableColumn
rsBWMCurrentPolicySpecific = _RsBWMCurrentPolicySpecific_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 67, 1, 18),
    _RsBWMCurrentPolicySpecific_Type()
)
rsBWMCurrentPolicySpecific.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMCurrentPolicySpecific.setStatus("mandatory")


class _RsBWMCurrentPolicyRadiusRule_Type(DisplayString):
    """Custom type rsBWMCurrentPolicyRadiusRule based on DisplayString"""
    defaultValue = OctetString("any")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_RsBWMCurrentPolicyRadiusRule_Type.__name__ = "DisplayString"
_RsBWMCurrentPolicyRadiusRule_Object = MibTableColumn
rsBWMCurrentPolicyRadiusRule = _RsBWMCurrentPolicyRadiusRule_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 67, 1, 19),
    _RsBWMCurrentPolicyRadiusRule_Type()
)
rsBWMCurrentPolicyRadiusRule.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMCurrentPolicyRadiusRule.setStatus("mandatory")
_RsBWMExtPoliciesTable_Object = MibTable
rsBWMExtPoliciesTable = _RsBWMExtPoliciesTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 68)
)
if mibBuilder.loadTexts:
    rsBWMExtPoliciesTable.setStatus("mandatory")
_RsBWMExtPolicyEntry_Object = MibTableRow
rsBWMExtPolicyEntry = _RsBWMExtPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 68, 1)
)
rsBWMExtPolicyEntry.setIndexNames(
    (0, "BWM-MIB", "rsBWMExtPolicyKey"),
)
if mibBuilder.loadTexts:
    rsBWMExtPolicyEntry.setStatus("mandatory")
_RsBWMExtPolicyKey_Type = Integer32
_RsBWMExtPolicyKey_Object = MibTableColumn
rsBWMExtPolicyKey = _RsBWMExtPolicyKey_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 68, 1, 1),
    _RsBWMExtPolicyKey_Type()
)
rsBWMExtPolicyKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMExtPolicyKey.setStatus("mandatory")


class _RsBWMExtPolicyName_Type(DisplayString):
    """Custom type rsBWMExtPolicyName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_RsBWMExtPolicyName_Type.__name__ = "DisplayString"
_RsBWMExtPolicyName_Object = MibTableColumn
rsBWMExtPolicyName = _RsBWMExtPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 68, 1, 2),
    _RsBWMExtPolicyName_Type()
)
rsBWMExtPolicyName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMExtPolicyName.setStatus("mandatory")


class _RsBWMExtPolicyFromFarm_Type(DisplayString):
    """Custom type rsBWMExtPolicyFromFarm based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 19),
    )


_RsBWMExtPolicyFromFarm_Type.__name__ = "DisplayString"
_RsBWMExtPolicyFromFarm_Object = MibTableColumn
rsBWMExtPolicyFromFarm = _RsBWMExtPolicyFromFarm_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 68, 1, 3),
    _RsBWMExtPolicyFromFarm_Type()
)
rsBWMExtPolicyFromFarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMExtPolicyFromFarm.setStatus("mandatory")


class _RsBWMExtPolicyToFarm_Type(DisplayString):
    """Custom type rsBWMExtPolicyToFarm based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 19),
    )


_RsBWMExtPolicyToFarm_Type.__name__ = "DisplayString"
_RsBWMExtPolicyToFarm_Object = MibTableColumn
rsBWMExtPolicyToFarm = _RsBWMExtPolicyToFarm_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 68, 1, 4),
    _RsBWMExtPolicyToFarm_Type()
)
rsBWMExtPolicyToFarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMExtPolicyToFarm.setStatus("mandatory")


class _RsBWMExtPolicyClassificationPoint_Type(Integer32):
    """Custom type rsBWMExtPolicyClassificationPoint based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("beforeChanges", 1),
          ("afterChanges", 2))
    )


_RsBWMExtPolicyClassificationPoint_Type.__name__ = "Integer32"
_RsBWMExtPolicyClassificationPoint_Object = MibTableColumn
rsBWMExtPolicyClassificationPoint = _RsBWMExtPolicyClassificationPoint_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 68, 1, 5),
    _RsBWMExtPolicyClassificationPoint_Type()
)
rsBWMExtPolicyClassificationPoint.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMExtPolicyClassificationPoint.setStatus("mandatory")


class _RsBWMExtPolicyTrafficIdentification_Type(Integer32):
    """Custom type rsBWMExtPolicyTrafficIdentification based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("client", 1),
          ("session", 2),
          ("connection", 3),
          ("fullL4Session", 4),
          ("sessionCookie", 5),
          ("sipCallID", 6))
    )


_RsBWMExtPolicyTrafficIdentification_Type.__name__ = "Integer32"
_RsBWMExtPolicyTrafficIdentification_Object = MibTableColumn
rsBWMExtPolicyTrafficIdentification = _RsBWMExtPolicyTrafficIdentification_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 68, 1, 6),
    _RsBWMExtPolicyTrafficIdentification_Type()
)
rsBWMExtPolicyTrafficIdentification.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMExtPolicyTrafficIdentification.setStatus("mandatory")
_RsBWMExtPolicyTrafficFlowMaxBW_Type = Integer32
_RsBWMExtPolicyTrafficFlowMaxBW_Object = MibTableColumn
rsBWMExtPolicyTrafficFlowMaxBW = _RsBWMExtPolicyTrafficFlowMaxBW_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 68, 1, 7),
    _RsBWMExtPolicyTrafficFlowMaxBW_Type()
)
rsBWMExtPolicyTrafficFlowMaxBW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMExtPolicyTrafficFlowMaxBW.setStatus("mandatory")
_RsBWMExtPolicyMaxConcurrentSessions_Type = Integer32
_RsBWMExtPolicyMaxConcurrentSessions_Object = MibTableColumn
rsBWMExtPolicyMaxConcurrentSessions = _RsBWMExtPolicyMaxConcurrentSessions_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 68, 1, 8),
    _RsBWMExtPolicyMaxConcurrentSessions_Type()
)
rsBWMExtPolicyMaxConcurrentSessions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMExtPolicyMaxConcurrentSessions.setStatus("mandatory")
_RsBWMExtPolicyMaxRqstsPerSec_Type = Integer32
_RsBWMExtPolicyMaxRqstsPerSec_Object = MibTableColumn
rsBWMExtPolicyMaxRqstsPerSec = _RsBWMExtPolicyMaxRqstsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 68, 1, 9),
    _RsBWMExtPolicyMaxRqstsPerSec_Type()
)
rsBWMExtPolicyMaxRqstsPerSec.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMExtPolicyMaxRqstsPerSec.setStatus("mandatory")


class _RsBWMExtPolicyTrafficIDCookieField_Type(DisplayString):
    """Custom type rsBWMExtPolicyTrafficIDCookieField based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_RsBWMExtPolicyTrafficIDCookieField_Type.__name__ = "DisplayString"
_RsBWMExtPolicyTrafficIDCookieField_Object = MibTableColumn
rsBWMExtPolicyTrafficIDCookieField = _RsBWMExtPolicyTrafficIDCookieField_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 68, 1, 10),
    _RsBWMExtPolicyTrafficIDCookieField_Type()
)
rsBWMExtPolicyTrafficIDCookieField.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMExtPolicyTrafficIDCookieField.setStatus("mandatory")
_RsBWMExtPolicyStatus_Type = RowStatus
_RsBWMExtPolicyStatus_Object = MibTableColumn
rsBWMExtPolicyStatus = _RsBWMExtPolicyStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 68, 1, 11),
    _RsBWMExtPolicyStatus_Type()
)
rsBWMExtPolicyStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMExtPolicyStatus.setStatus("mandatory")


class _RsBWMExtPolicyActivate_Type(DisplayString):
    """Custom type rsBWMExtPolicyActivate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 29),
    )


_RsBWMExtPolicyActivate_Type.__name__ = "DisplayString"
_RsBWMExtPolicyActivate_Object = MibTableColumn
rsBWMExtPolicyActivate = _RsBWMExtPolicyActivate_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 68, 1, 12),
    _RsBWMExtPolicyActivate_Type()
)
rsBWMExtPolicyActivate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMExtPolicyActivate.setStatus("mandatory")


class _RsBWMExtPolicyInactivate_Type(DisplayString):
    """Custom type rsBWMExtPolicyInactivate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 29),
    )


_RsBWMExtPolicyInactivate_Type.__name__ = "DisplayString"
_RsBWMExtPolicyInactivate_Object = MibTableColumn
rsBWMExtPolicyInactivate = _RsBWMExtPolicyInactivate_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 68, 1, 13),
    _RsBWMExtPolicyInactivate_Type()
)
rsBWMExtPolicyInactivate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMExtPolicyInactivate.setStatus("mandatory")


class _RsBWMExtPolicyForceBestFit_Type(Integer32):
    """Custom type rsBWMExtPolicyForceBestFit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_RsBWMExtPolicyForceBestFit_Type.__name__ = "Integer32"
_RsBWMExtPolicyForceBestFit_Object = MibTableColumn
rsBWMExtPolicyForceBestFit = _RsBWMExtPolicyForceBestFit_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 68, 1, 14),
    _RsBWMExtPolicyForceBestFit_Type()
)
rsBWMExtPolicyForceBestFit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMExtPolicyForceBestFit.setStatus("mandatory")


class _RsBWMExtPolicyPacketMarkingType_Type(Integer32):
    """Custom type rsBWMExtPolicyPacketMarkingType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("dscp", 2),
          ("tos", 3))
    )


_RsBWMExtPolicyPacketMarkingType_Type.__name__ = "Integer32"
_RsBWMExtPolicyPacketMarkingType_Object = MibTableColumn
rsBWMExtPolicyPacketMarkingType = _RsBWMExtPolicyPacketMarkingType_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 68, 1, 15),
    _RsBWMExtPolicyPacketMarkingType_Type()
)
rsBWMExtPolicyPacketMarkingType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMExtPolicyPacketMarkingType.setStatus("mandatory")


class _RsBWMExtPolicyPacketMarkingValue_Type(Integer32):
    """Custom type rsBWMExtPolicyPacketMarkingValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 63),
    )


_RsBWMExtPolicyPacketMarkingValue_Type.__name__ = "Integer32"
_RsBWMExtPolicyPacketMarkingValue_Object = MibTableColumn
rsBWMExtPolicyPacketMarkingValue = _RsBWMExtPolicyPacketMarkingValue_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 68, 1, 16),
    _RsBWMExtPolicyPacketMarkingValue_Type()
)
rsBWMExtPolicyPacketMarkingValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMExtPolicyPacketMarkingValue.setStatus("mandatory")


class _RsBWMExtPolicyReportMaxBw_Type(Integer32):
    """Custom type rsBWMExtPolicyReportMaxBw based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_RsBWMExtPolicyReportMaxBw_Type.__name__ = "Integer32"
_RsBWMExtPolicyReportMaxBw_Object = MibTableColumn
rsBWMExtPolicyReportMaxBw = _RsBWMExtPolicyReportMaxBw_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 68, 1, 17),
    _RsBWMExtPolicyReportMaxBw_Type()
)
rsBWMExtPolicyReportMaxBw.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMExtPolicyReportMaxBw.setStatus("mandatory")
_RsBWMCurrentExtPoliciesTable_Object = MibTable
rsBWMCurrentExtPoliciesTable = _RsBWMCurrentExtPoliciesTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 69)
)
if mibBuilder.loadTexts:
    rsBWMCurrentExtPoliciesTable.setStatus("mandatory")
_RsBWMCurrentExtPolicyEntry_Object = MibTableRow
rsBWMCurrentExtPolicyEntry = _RsBWMCurrentExtPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 69, 1)
)
rsBWMCurrentExtPolicyEntry.setIndexNames(
    (0, "BWM-MIB", "rsBWMCurrentExtPolicyKey"),
)
if mibBuilder.loadTexts:
    rsBWMCurrentExtPolicyEntry.setStatus("mandatory")
_RsBWMCurrentExtPolicyKey_Type = Integer32
_RsBWMCurrentExtPolicyKey_Object = MibTableColumn
rsBWMCurrentExtPolicyKey = _RsBWMCurrentExtPolicyKey_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 69, 1, 1),
    _RsBWMCurrentExtPolicyKey_Type()
)
rsBWMCurrentExtPolicyKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMCurrentExtPolicyKey.setStatus("mandatory")


class _RsBWMCurrentExtPolicyName_Type(DisplayString):
    """Custom type rsBWMCurrentExtPolicyName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_RsBWMCurrentExtPolicyName_Type.__name__ = "DisplayString"
_RsBWMCurrentExtPolicyName_Object = MibTableColumn
rsBWMCurrentExtPolicyName = _RsBWMCurrentExtPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 69, 1, 2),
    _RsBWMCurrentExtPolicyName_Type()
)
rsBWMCurrentExtPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMCurrentExtPolicyName.setStatus("mandatory")


class _RsBWMCurrentExtPolicyFromFarm_Type(DisplayString):
    """Custom type rsBWMCurrentExtPolicyFromFarm based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 19),
    )


_RsBWMCurrentExtPolicyFromFarm_Type.__name__ = "DisplayString"
_RsBWMCurrentExtPolicyFromFarm_Object = MibTableColumn
rsBWMCurrentExtPolicyFromFarm = _RsBWMCurrentExtPolicyFromFarm_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 69, 1, 3),
    _RsBWMCurrentExtPolicyFromFarm_Type()
)
rsBWMCurrentExtPolicyFromFarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMCurrentExtPolicyFromFarm.setStatus("mandatory")


class _RsBWMCurrentExtPolicyToFarm_Type(DisplayString):
    """Custom type rsBWMCurrentExtPolicyToFarm based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 19),
    )


_RsBWMCurrentExtPolicyToFarm_Type.__name__ = "DisplayString"
_RsBWMCurrentExtPolicyToFarm_Object = MibTableColumn
rsBWMCurrentExtPolicyToFarm = _RsBWMCurrentExtPolicyToFarm_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 69, 1, 4),
    _RsBWMCurrentExtPolicyToFarm_Type()
)
rsBWMCurrentExtPolicyToFarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMCurrentExtPolicyToFarm.setStatus("mandatory")


class _RsBWMCurrentExtPolicyClassificationPoint_Type(Integer32):
    """Custom type rsBWMCurrentExtPolicyClassificationPoint based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("beforeChanges", 1),
          ("afterChanges", 2))
    )


_RsBWMCurrentExtPolicyClassificationPoint_Type.__name__ = "Integer32"
_RsBWMCurrentExtPolicyClassificationPoint_Object = MibTableColumn
rsBWMCurrentExtPolicyClassificationPoint = _RsBWMCurrentExtPolicyClassificationPoint_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 69, 1, 5),
    _RsBWMCurrentExtPolicyClassificationPoint_Type()
)
rsBWMCurrentExtPolicyClassificationPoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMCurrentExtPolicyClassificationPoint.setStatus("mandatory")


class _RsBWMCurrentExtPolicyTrafficIdentification_Type(Integer32):
    """Custom type rsBWMCurrentExtPolicyTrafficIdentification based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("client", 1),
          ("session", 2),
          ("connection", 3),
          ("fullL4Session", 4),
          ("sessionCookie", 5),
          ("sipCallID", 6))
    )


_RsBWMCurrentExtPolicyTrafficIdentification_Type.__name__ = "Integer32"
_RsBWMCurrentExtPolicyTrafficIdentification_Object = MibTableColumn
rsBWMCurrentExtPolicyTrafficIdentification = _RsBWMCurrentExtPolicyTrafficIdentification_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 69, 1, 6),
    _RsBWMCurrentExtPolicyTrafficIdentification_Type()
)
rsBWMCurrentExtPolicyTrafficIdentification.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMCurrentExtPolicyTrafficIdentification.setStatus("mandatory")
_RsBWMCurrentExtPolicyTrafficFlowMaxBW_Type = Integer32
_RsBWMCurrentExtPolicyTrafficFlowMaxBW_Object = MibTableColumn
rsBWMCurrentExtPolicyTrafficFlowMaxBW = _RsBWMCurrentExtPolicyTrafficFlowMaxBW_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 69, 1, 7),
    _RsBWMCurrentExtPolicyTrafficFlowMaxBW_Type()
)
rsBWMCurrentExtPolicyTrafficFlowMaxBW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMCurrentExtPolicyTrafficFlowMaxBW.setStatus("mandatory")
_RsBWMCurrentExtPolicyMaxConcurrentSessions_Type = Integer32
_RsBWMCurrentExtPolicyMaxConcurrentSessions_Object = MibTableColumn
rsBWMCurrentExtPolicyMaxConcurrentSessions = _RsBWMCurrentExtPolicyMaxConcurrentSessions_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 69, 1, 8),
    _RsBWMCurrentExtPolicyMaxConcurrentSessions_Type()
)
rsBWMCurrentExtPolicyMaxConcurrentSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMCurrentExtPolicyMaxConcurrentSessions.setStatus("mandatory")
_RsBWMCurrentExtPolicyMaxRqstsPerSec_Type = Integer32
_RsBWMCurrentExtPolicyMaxRqstsPerSec_Object = MibTableColumn
rsBWMCurrentExtPolicyMaxRqstsPerSec = _RsBWMCurrentExtPolicyMaxRqstsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 69, 1, 9),
    _RsBWMCurrentExtPolicyMaxRqstsPerSec_Type()
)
rsBWMCurrentExtPolicyMaxRqstsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMCurrentExtPolicyMaxRqstsPerSec.setStatus("mandatory")


class _RsBWMCurrentExtPolicyTrafficIDCookieField_Type(DisplayString):
    """Custom type rsBWMCurrentExtPolicyTrafficIDCookieField based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_RsBWMCurrentExtPolicyTrafficIDCookieField_Type.__name__ = "DisplayString"
_RsBWMCurrentExtPolicyTrafficIDCookieField_Object = MibTableColumn
rsBWMCurrentExtPolicyTrafficIDCookieField = _RsBWMCurrentExtPolicyTrafficIDCookieField_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 69, 1, 10),
    _RsBWMCurrentExtPolicyTrafficIDCookieField_Type()
)
rsBWMCurrentExtPolicyTrafficIDCookieField.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMCurrentExtPolicyTrafficIDCookieField.setStatus("mandatory")


class _RsBWMCurrentExtPolicyActivate_Type(DisplayString):
    """Custom type rsBWMCurrentExtPolicyActivate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 29),
    )


_RsBWMCurrentExtPolicyActivate_Type.__name__ = "DisplayString"
_RsBWMCurrentExtPolicyActivate_Object = MibTableColumn
rsBWMCurrentExtPolicyActivate = _RsBWMCurrentExtPolicyActivate_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 69, 1, 11),
    _RsBWMCurrentExtPolicyActivate_Type()
)
rsBWMCurrentExtPolicyActivate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMCurrentExtPolicyActivate.setStatus("mandatory")


class _RsBWMCurrentExtPolicyInactivate_Type(DisplayString):
    """Custom type rsBWMCurrentExtPolicyInactivate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 29),
    )


_RsBWMCurrentExtPolicyInactivate_Type.__name__ = "DisplayString"
_RsBWMCurrentExtPolicyInactivate_Object = MibTableColumn
rsBWMCurrentExtPolicyInactivate = _RsBWMCurrentExtPolicyInactivate_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 69, 1, 12),
    _RsBWMCurrentExtPolicyInactivate_Type()
)
rsBWMCurrentExtPolicyInactivate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMCurrentExtPolicyInactivate.setStatus("mandatory")


class _RsBWMCurrentExtPolicyForceBestFit_Type(Integer32):
    """Custom type rsBWMCurrentExtPolicyForceBestFit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_RsBWMCurrentExtPolicyForceBestFit_Type.__name__ = "Integer32"
_RsBWMCurrentExtPolicyForceBestFit_Object = MibTableColumn
rsBWMCurrentExtPolicyForceBestFit = _RsBWMCurrentExtPolicyForceBestFit_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 69, 1, 13),
    _RsBWMCurrentExtPolicyForceBestFit_Type()
)
rsBWMCurrentExtPolicyForceBestFit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMCurrentExtPolicyForceBestFit.setStatus("mandatory")


class _RsBWMCurrentExtPolicyPacketMarkingType_Type(Integer32):
    """Custom type rsBWMCurrentExtPolicyPacketMarkingType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("dscp", 2),
          ("tos", 3))
    )


_RsBWMCurrentExtPolicyPacketMarkingType_Type.__name__ = "Integer32"
_RsBWMCurrentExtPolicyPacketMarkingType_Object = MibTableColumn
rsBWMCurrentExtPolicyPacketMarkingType = _RsBWMCurrentExtPolicyPacketMarkingType_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 69, 1, 14),
    _RsBWMCurrentExtPolicyPacketMarkingType_Type()
)
rsBWMCurrentExtPolicyPacketMarkingType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMCurrentExtPolicyPacketMarkingType.setStatus("mandatory")


class _RsBWMCurrentExtPolicyPacketMarkingValue_Type(Integer32):
    """Custom type rsBWMCurrentExtPolicyPacketMarkingValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 63),
    )


_RsBWMCurrentExtPolicyPacketMarkingValue_Type.__name__ = "Integer32"
_RsBWMCurrentExtPolicyPacketMarkingValue_Object = MibTableColumn
rsBWMCurrentExtPolicyPacketMarkingValue = _RsBWMCurrentExtPolicyPacketMarkingValue_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 69, 1, 15),
    _RsBWMCurrentExtPolicyPacketMarkingValue_Type()
)
rsBWMCurrentExtPolicyPacketMarkingValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMCurrentExtPolicyPacketMarkingValue.setStatus("mandatory")


class _RsBWMCurrentExtPolicyReportMaxBw_Type(Integer32):
    """Custom type rsBWMCurrentExtPolicyReportMaxBw based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_RsBWMCurrentExtPolicyReportMaxBw_Type.__name__ = "Integer32"
_RsBWMCurrentExtPolicyReportMaxBw_Object = MibTableColumn
rsBWMCurrentExtPolicyReportMaxBw = _RsBWMCurrentExtPolicyReportMaxBw_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 69, 1, 16),
    _RsBWMCurrentExtPolicyReportMaxBw_Type()
)
rsBWMCurrentExtPolicyReportMaxBw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMCurrentExtPolicyReportMaxBw.setStatus("mandatory")


class _RsBWMMaxPacketsForClassification_Type(Integer32):
    """Custom type rsBWMMaxPacketsForClassification based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_RsBWMMaxPacketsForClassification_Type.__name__ = "Integer32"
_RsBWMMaxPacketsForClassification_Object = MibScalar
rsBWMMaxPacketsForClassification = _RsBWMMaxPacketsForClassification_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 70),
    _RsBWMMaxPacketsForClassification_Type()
)
rsBWMMaxPacketsForClassification.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMMaxPacketsForClassification.setStatus("mandatory")
_RsBWMACL_ObjectIdentity = ObjectIdentity
rsBWMACL = _RsBWMACL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 71)
)
_RsBWMACLModifyPoliciesTable_Object = MibTable
rsBWMACLModifyPoliciesTable = _RsBWMACLModifyPoliciesTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 71, 1)
)
if mibBuilder.loadTexts:
    rsBWMACLModifyPoliciesTable.setStatus("mandatory")
_RsBWMACLModifyPolicyEntry_Object = MibTableRow
rsBWMACLModifyPolicyEntry = _RsBWMACLModifyPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 71, 1, 1)
)
rsBWMACLModifyPolicyEntry.setIndexNames(
    (0, "BWM-MIB", "rsBWMACLModifyPolicyName"),
)
if mibBuilder.loadTexts:
    rsBWMACLModifyPolicyEntry.setStatus("mandatory")


class _RsBWMACLModifyPolicyName_Type(DisplayString):
    """Custom type rsBWMACLModifyPolicyName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_RsBWMACLModifyPolicyName_Type.__name__ = "DisplayString"
_RsBWMACLModifyPolicyName_Object = MibTableColumn
rsBWMACLModifyPolicyName = _RsBWMACLModifyPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 71, 1, 1, 1),
    _RsBWMACLModifyPolicyName_Type()
)
rsBWMACLModifyPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMACLModifyPolicyName.setStatus("mandatory")


class _RsBWMACLModifyPolicyIndex_Type(Integer32):
    """Custom type rsBWMACLModifyPolicyIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_RsBWMACLModifyPolicyIndex_Type.__name__ = "Integer32"
_RsBWMACLModifyPolicyIndex_Object = MibTableColumn
rsBWMACLModifyPolicyIndex = _RsBWMACLModifyPolicyIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 71, 1, 1, 2),
    _RsBWMACLModifyPolicyIndex_Type()
)
rsBWMACLModifyPolicyIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMACLModifyPolicyIndex.setStatus("mandatory")


class _RsBWMACLModifyPolicyDescription_Type(DisplayString):
    """Custom type rsBWMACLModifyPolicyDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 19),
    )


_RsBWMACLModifyPolicyDescription_Type.__name__ = "DisplayString"
_RsBWMACLModifyPolicyDescription_Object = MibTableColumn
rsBWMACLModifyPolicyDescription = _RsBWMACLModifyPolicyDescription_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 71, 1, 1, 3),
    _RsBWMACLModifyPolicyDescription_Type()
)
rsBWMACLModifyPolicyDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMACLModifyPolicyDescription.setStatus("mandatory")


class _RsBWMACLModifyPolicyDestination_Type(DisplayString):
    """Custom type rsBWMACLModifyPolicyDestination based on DisplayString"""
    defaultValue = OctetString("any")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 46),
    )


_RsBWMACLModifyPolicyDestination_Type.__name__ = "DisplayString"
_RsBWMACLModifyPolicyDestination_Object = MibTableColumn
rsBWMACLModifyPolicyDestination = _RsBWMACLModifyPolicyDestination_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 71, 1, 1, 4),
    _RsBWMACLModifyPolicyDestination_Type()
)
rsBWMACLModifyPolicyDestination.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMACLModifyPolicyDestination.setStatus("mandatory")


class _RsBWMACLModifyPolicySource_Type(DisplayString):
    """Custom type rsBWMACLModifyPolicySource based on DisplayString"""
    defaultValue = OctetString("any")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 46),
    )


_RsBWMACLModifyPolicySource_Type.__name__ = "DisplayString"
_RsBWMACLModifyPolicySource_Object = MibTableColumn
rsBWMACLModifyPolicySource = _RsBWMACLModifyPolicySource_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 71, 1, 1, 5),
    _RsBWMACLModifyPolicySource_Type()
)
rsBWMACLModifyPolicySource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMACLModifyPolicySource.setStatus("mandatory")


class _RsBWMACLModifyPolicyService_Type(DisplayString):
    """Custom type rsBWMACLModifyPolicyService based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 19),
    )


_RsBWMACLModifyPolicyService_Type.__name__ = "DisplayString"
_RsBWMACLModifyPolicyService_Object = MibTableColumn
rsBWMACLModifyPolicyService = _RsBWMACLModifyPolicyService_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 71, 1, 1, 6),
    _RsBWMACLModifyPolicyService_Type()
)
rsBWMACLModifyPolicyService.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMACLModifyPolicyService.setStatus("mandatory")


class _RsBWMACLModifyPolicyVLANTagGroup_Type(DisplayString):
    """Custom type rsBWMACLModifyPolicyVLANTagGroup based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 19),
    )


_RsBWMACLModifyPolicyVLANTagGroup_Type.__name__ = "DisplayString"
_RsBWMACLModifyPolicyVLANTagGroup_Object = MibTableColumn
rsBWMACLModifyPolicyVLANTagGroup = _RsBWMACLModifyPolicyVLANTagGroup_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 71, 1, 1, 7),
    _RsBWMACLModifyPolicyVLANTagGroup_Type()
)
rsBWMACLModifyPolicyVLANTagGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMACLModifyPolicyVLANTagGroup.setStatus("mandatory")


class _RsBWMACLModifyPolicyPortGroup_Type(DisplayString):
    """Custom type rsBWMACLModifyPolicyPortGroup based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 19),
    )


_RsBWMACLModifyPolicyPortGroup_Type.__name__ = "DisplayString"
_RsBWMACLModifyPolicyPortGroup_Object = MibTableColumn
rsBWMACLModifyPolicyPortGroup = _RsBWMACLModifyPolicyPortGroup_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 71, 1, 1, 8),
    _RsBWMACLModifyPolicyPortGroup_Type()
)
rsBWMACLModifyPolicyPortGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMACLModifyPolicyPortGroup.setStatus("mandatory")


class _RsBWMACLModifyPolicyActivate_Type(DisplayString):
    """Custom type rsBWMACLModifyPolicyActivate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 29),
    )


_RsBWMACLModifyPolicyActivate_Type.__name__ = "DisplayString"
_RsBWMACLModifyPolicyActivate_Object = MibTableColumn
rsBWMACLModifyPolicyActivate = _RsBWMACLModifyPolicyActivate_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 71, 1, 1, 9),
    _RsBWMACLModifyPolicyActivate_Type()
)
rsBWMACLModifyPolicyActivate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMACLModifyPolicyActivate.setStatus("mandatory")


class _RsBWMACLModifyPolicyInactivate_Type(DisplayString):
    """Custom type rsBWMACLModifyPolicyInactivate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 29),
    )


_RsBWMACLModifyPolicyInactivate_Type.__name__ = "DisplayString"
_RsBWMACLModifyPolicyInactivate_Object = MibTableColumn
rsBWMACLModifyPolicyInactivate = _RsBWMACLModifyPolicyInactivate_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 71, 1, 1, 10),
    _RsBWMACLModifyPolicyInactivate_Type()
)
rsBWMACLModifyPolicyInactivate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMACLModifyPolicyInactivate.setStatus("mandatory")


class _RsBWMACLModifyPolicyAction_Type(Integer32):
    """Custom type rsBWMACLModifyPolicyAction based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("accept", 1),
          ("drop", 2),
          ("dropAndResetSource", 3))
    )


_RsBWMACLModifyPolicyAction_Type.__name__ = "Integer32"
_RsBWMACLModifyPolicyAction_Object = MibTableColumn
rsBWMACLModifyPolicyAction = _RsBWMACLModifyPolicyAction_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 71, 1, 1, 11),
    _RsBWMACLModifyPolicyAction_Type()
)
rsBWMACLModifyPolicyAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMACLModifyPolicyAction.setStatus("mandatory")


class _RsBWMACLModifyPolicyProtocol_Type(Integer32):
    """Custom type rsBWMACLModifyPolicyProtocol based on Integer32"""
    defaultValue = 5

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
        *(("tcp", 1),
          ("udp", 2),
          ("icmp", 3),
          ("other", 4),
          ("any", 5),
          ("gre", 6),
          ("sctp", 7),
          ("l2tp", 8),
          ("gtp", 9),
          ("ipinip", 10))
    )


_RsBWMACLModifyPolicyProtocol_Type.__name__ = "Integer32"
_RsBWMACLModifyPolicyProtocol_Object = MibTableColumn
rsBWMACLModifyPolicyProtocol = _RsBWMACLModifyPolicyProtocol_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 71, 1, 1, 12),
    _RsBWMACLModifyPolicyProtocol_Type()
)
rsBWMACLModifyPolicyProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMACLModifyPolicyProtocol.setStatus("mandatory")


class _RsBWMACLModifyPolicyIcmpFlags_Type(DisplayString):
    """Custom type rsBWMACLModifyPolicyIcmpFlags based on DisplayString"""
    defaultValue = OctetString("11111111111111111111")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_RsBWMACLModifyPolicyIcmpFlags_Type.__name__ = "DisplayString"
_RsBWMACLModifyPolicyIcmpFlags_Object = MibTableColumn
rsBWMACLModifyPolicyIcmpFlags = _RsBWMACLModifyPolicyIcmpFlags_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 71, 1, 1, 13),
    _RsBWMACLModifyPolicyIcmpFlags_Type()
)
rsBWMACLModifyPolicyIcmpFlags.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMACLModifyPolicyIcmpFlags.setStatus("mandatory")


class _RsBWMACLModifyPolicyClassificationPoint_Type(Integer32):
    """Custom type rsBWMACLModifyPolicyClassificationPoint based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("beforeChanges", 1),
          ("afterChanges", 2))
    )


_RsBWMACLModifyPolicyClassificationPoint_Type.__name__ = "Integer32"
_RsBWMACLModifyPolicyClassificationPoint_Object = MibTableColumn
rsBWMACLModifyPolicyClassificationPoint = _RsBWMACLModifyPolicyClassificationPoint_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 71, 1, 1, 14),
    _RsBWMACLModifyPolicyClassificationPoint_Type()
)
rsBWMACLModifyPolicyClassificationPoint.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMACLModifyPolicyClassificationPoint.setStatus("mandatory")


class _RsBWMACLModifyPolicyOperationalStatus_Type(Integer32):
    """Custom type rsBWMACLModifyPolicyOperationalStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_RsBWMACLModifyPolicyOperationalStatus_Type.__name__ = "Integer32"
_RsBWMACLModifyPolicyOperationalStatus_Object = MibTableColumn
rsBWMACLModifyPolicyOperationalStatus = _RsBWMACLModifyPolicyOperationalStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 71, 1, 1, 15),
    _RsBWMACLModifyPolicyOperationalStatus_Type()
)
rsBWMACLModifyPolicyOperationalStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMACLModifyPolicyOperationalStatus.setStatus("mandatory")
_RsBWMACLModifyPolicyStatus_Type = RowStatus
_RsBWMACLModifyPolicyStatus_Object = MibTableColumn
rsBWMACLModifyPolicyStatus = _RsBWMACLModifyPolicyStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 71, 1, 1, 16),
    _RsBWMACLModifyPolicyStatus_Type()
)
rsBWMACLModifyPolicyStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMACLModifyPolicyStatus.setStatus("mandatory")


class _RsBWMACLModifyPolicyPacketReportStatus_Type(Integer32):
    """Custom type rsBWMACLModifyPolicyPacketReportStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_RsBWMACLModifyPolicyPacketReportStatus_Type.__name__ = "Integer32"
_RsBWMACLModifyPolicyPacketReportStatus_Object = MibTableColumn
rsBWMACLModifyPolicyPacketReportStatus = _RsBWMACLModifyPolicyPacketReportStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 71, 1, 1, 17),
    _RsBWMACLModifyPolicyPacketReportStatus_Type()
)
rsBWMACLModifyPolicyPacketReportStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMACLModifyPolicyPacketReportStatus.setStatus("mandatory")
_RsBWMACLActualPoliciesTable_Object = MibTable
rsBWMACLActualPoliciesTable = _RsBWMACLActualPoliciesTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 71, 2)
)
if mibBuilder.loadTexts:
    rsBWMACLActualPoliciesTable.setStatus("mandatory")
_RsBWMACLActualPolicyEntry_Object = MibTableRow
rsBWMACLActualPolicyEntry = _RsBWMACLActualPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 71, 2, 1)
)
rsBWMACLActualPolicyEntry.setIndexNames(
    (0, "BWM-MIB", "rsBWMACLActualPolicyName"),
)
if mibBuilder.loadTexts:
    rsBWMACLActualPolicyEntry.setStatus("mandatory")


class _RsBWMACLActualPolicyName_Type(DisplayString):
    """Custom type rsBWMACLActualPolicyName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_RsBWMACLActualPolicyName_Type.__name__ = "DisplayString"
_RsBWMACLActualPolicyName_Object = MibTableColumn
rsBWMACLActualPolicyName = _RsBWMACLActualPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 71, 2, 1, 1),
    _RsBWMACLActualPolicyName_Type()
)
rsBWMACLActualPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMACLActualPolicyName.setStatus("mandatory")
_RsBWMACLActualPolicyIndex_Type = Integer32
_RsBWMACLActualPolicyIndex_Object = MibTableColumn
rsBWMACLActualPolicyIndex = _RsBWMACLActualPolicyIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 71, 2, 1, 2),
    _RsBWMACLActualPolicyIndex_Type()
)
rsBWMACLActualPolicyIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMACLActualPolicyIndex.setStatus("mandatory")


class _RsBWMACLActualPolicyDescription_Type(DisplayString):
    """Custom type rsBWMACLActualPolicyDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 19),
    )


_RsBWMACLActualPolicyDescription_Type.__name__ = "DisplayString"
_RsBWMACLActualPolicyDescription_Object = MibTableColumn
rsBWMACLActualPolicyDescription = _RsBWMACLActualPolicyDescription_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 71, 2, 1, 3),
    _RsBWMACLActualPolicyDescription_Type()
)
rsBWMACLActualPolicyDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMACLActualPolicyDescription.setStatus("mandatory")


class _RsBWMACLActualPolicyDestination_Type(DisplayString):
    """Custom type rsBWMACLActualPolicyDestination based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 46),
    )


_RsBWMACLActualPolicyDestination_Type.__name__ = "DisplayString"
_RsBWMACLActualPolicyDestination_Object = MibTableColumn
rsBWMACLActualPolicyDestination = _RsBWMACLActualPolicyDestination_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 71, 2, 1, 4),
    _RsBWMACLActualPolicyDestination_Type()
)
rsBWMACLActualPolicyDestination.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMACLActualPolicyDestination.setStatus("mandatory")


class _RsBWMACLActualPolicySource_Type(DisplayString):
    """Custom type rsBWMACLActualPolicySource based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 46),
    )


_RsBWMACLActualPolicySource_Type.__name__ = "DisplayString"
_RsBWMACLActualPolicySource_Object = MibTableColumn
rsBWMACLActualPolicySource = _RsBWMACLActualPolicySource_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 71, 2, 1, 5),
    _RsBWMACLActualPolicySource_Type()
)
rsBWMACLActualPolicySource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMACLActualPolicySource.setStatus("mandatory")


class _RsBWMACLActualPolicyService_Type(DisplayString):
    """Custom type rsBWMACLActualPolicyService based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 19),
    )


_RsBWMACLActualPolicyService_Type.__name__ = "DisplayString"
_RsBWMACLActualPolicyService_Object = MibTableColumn
rsBWMACLActualPolicyService = _RsBWMACLActualPolicyService_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 71, 2, 1, 6),
    _RsBWMACLActualPolicyService_Type()
)
rsBWMACLActualPolicyService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMACLActualPolicyService.setStatus("mandatory")


class _RsBWMACLActualPolicyVLANTagGroup_Type(DisplayString):
    """Custom type rsBWMACLActualPolicyVLANTagGroup based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 19),
    )


_RsBWMACLActualPolicyVLANTagGroup_Type.__name__ = "DisplayString"
_RsBWMACLActualPolicyVLANTagGroup_Object = MibTableColumn
rsBWMACLActualPolicyVLANTagGroup = _RsBWMACLActualPolicyVLANTagGroup_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 71, 2, 1, 7),
    _RsBWMACLActualPolicyVLANTagGroup_Type()
)
rsBWMACLActualPolicyVLANTagGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMACLActualPolicyVLANTagGroup.setStatus("mandatory")


class _RsBWMACLActualPolicyPortGroup_Type(DisplayString):
    """Custom type rsBWMACLActualPolicyPortGroup based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 19),
    )


_RsBWMACLActualPolicyPortGroup_Type.__name__ = "DisplayString"
_RsBWMACLActualPolicyPortGroup_Object = MibTableColumn
rsBWMACLActualPolicyPortGroup = _RsBWMACLActualPolicyPortGroup_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 71, 2, 1, 8),
    _RsBWMACLActualPolicyPortGroup_Type()
)
rsBWMACLActualPolicyPortGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMACLActualPolicyPortGroup.setStatus("mandatory")


class _RsBWMACLActualPolicyActivate_Type(DisplayString):
    """Custom type rsBWMACLActualPolicyActivate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 29),
    )


_RsBWMACLActualPolicyActivate_Type.__name__ = "DisplayString"
_RsBWMACLActualPolicyActivate_Object = MibTableColumn
rsBWMACLActualPolicyActivate = _RsBWMACLActualPolicyActivate_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 71, 2, 1, 9),
    _RsBWMACLActualPolicyActivate_Type()
)
rsBWMACLActualPolicyActivate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMACLActualPolicyActivate.setStatus("mandatory")


class _RsBWMACLActualPolicyInactivate_Type(DisplayString):
    """Custom type rsBWMACLActualPolicyInactivate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 29),
    )


_RsBWMACLActualPolicyInactivate_Type.__name__ = "DisplayString"
_RsBWMACLActualPolicyInactivate_Object = MibTableColumn
rsBWMACLActualPolicyInactivate = _RsBWMACLActualPolicyInactivate_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 71, 2, 1, 10),
    _RsBWMACLActualPolicyInactivate_Type()
)
rsBWMACLActualPolicyInactivate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMACLActualPolicyInactivate.setStatus("mandatory")


class _RsBWMACLActualPolicyAction_Type(Integer32):
    """Custom type rsBWMACLActualPolicyAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("accept", 1),
          ("drop", 2),
          ("dropAndResetSource", 3))
    )


_RsBWMACLActualPolicyAction_Type.__name__ = "Integer32"
_RsBWMACLActualPolicyAction_Object = MibTableColumn
rsBWMACLActualPolicyAction = _RsBWMACLActualPolicyAction_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 71, 2, 1, 11),
    _RsBWMACLActualPolicyAction_Type()
)
rsBWMACLActualPolicyAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMACLActualPolicyAction.setStatus("mandatory")


class _RsBWMACLActualPolicyProtocol_Type(Integer32):
    """Custom type rsBWMACLActualPolicyProtocol based on Integer32"""
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
        *(("tcp", 1),
          ("udp", 2),
          ("icmp", 3),
          ("other", 4),
          ("any", 5),
          ("gre", 6),
          ("sctp", 7),
          ("l2tp", 8),
          ("gtp", 9),
          ("ipinip", 10))
    )


_RsBWMACLActualPolicyProtocol_Type.__name__ = "Integer32"
_RsBWMACLActualPolicyProtocol_Object = MibTableColumn
rsBWMACLActualPolicyProtocol = _RsBWMACLActualPolicyProtocol_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 71, 2, 1, 12),
    _RsBWMACLActualPolicyProtocol_Type()
)
rsBWMACLActualPolicyProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMACLActualPolicyProtocol.setStatus("mandatory")


class _RsBWMACLActualPolicyIcmpFlags_Type(DisplayString):
    """Custom type rsBWMACLActualPolicyIcmpFlags based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_RsBWMACLActualPolicyIcmpFlags_Type.__name__ = "DisplayString"
_RsBWMACLActualPolicyIcmpFlags_Object = MibTableColumn
rsBWMACLActualPolicyIcmpFlags = _RsBWMACLActualPolicyIcmpFlags_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 71, 2, 1, 13),
    _RsBWMACLActualPolicyIcmpFlags_Type()
)
rsBWMACLActualPolicyIcmpFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMACLActualPolicyIcmpFlags.setStatus("mandatory")


class _RsBWMACLActualPolicyClassificationPoint_Type(Integer32):
    """Custom type rsBWMACLActualPolicyClassificationPoint based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("beforeChanges", 1),
          ("afterChanges", 2))
    )


_RsBWMACLActualPolicyClassificationPoint_Type.__name__ = "Integer32"
_RsBWMACLActualPolicyClassificationPoint_Object = MibTableColumn
rsBWMACLActualPolicyClassificationPoint = _RsBWMACLActualPolicyClassificationPoint_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 71, 2, 1, 14),
    _RsBWMACLActualPolicyClassificationPoint_Type()
)
rsBWMACLActualPolicyClassificationPoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMACLActualPolicyClassificationPoint.setStatus("mandatory")


class _RsBWMACLActualPolicyOperationalStatus_Type(Integer32):
    """Custom type rsBWMACLActualPolicyOperationalStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_RsBWMACLActualPolicyOperationalStatus_Type.__name__ = "Integer32"
_RsBWMACLActualPolicyOperationalStatus_Object = MibTableColumn
rsBWMACLActualPolicyOperationalStatus = _RsBWMACLActualPolicyOperationalStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 71, 2, 1, 15),
    _RsBWMACLActualPolicyOperationalStatus_Type()
)
rsBWMACLActualPolicyOperationalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMACLActualPolicyOperationalStatus.setStatus("mandatory")


class _RsBWMACLActualPolicyPacketReportStatus_Type(Integer32):
    """Custom type rsBWMACLActualPolicyPacketReportStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_RsBWMACLActualPolicyPacketReportStatus_Type.__name__ = "Integer32"
_RsBWMACLActualPolicyPacketReportStatus_Object = MibTableColumn
rsBWMACLActualPolicyPacketReportStatus = _RsBWMACLActualPolicyPacketReportStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 71, 2, 1, 16),
    _RsBWMACLActualPolicyPacketReportStatus_Type()
)
rsBWMACLActualPolicyPacketReportStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMACLActualPolicyPacketReportStatus.setStatus("mandatory")
_RsBWMACLStatus_Type = FeatureStatus
_RsBWMACLStatus_Object = MibScalar
rsBWMACLStatus = _RsBWMACLStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 71, 3),
    _RsBWMACLStatus_Type()
)
rsBWMACLStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMACLStatus.setStatus("mandatory")


class _RsBWMACLLearningPeriod_Type(Integer32):
    """Custom type rsBWMACLLearningPeriod based on Integer32"""
    defaultValue = 1800

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_RsBWMACLLearningPeriod_Type.__name__ = "Integer32"
_RsBWMACLLearningPeriod_Object = MibScalar
rsBWMACLLearningPeriod = _RsBWMACLLearningPeriod_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 71, 4),
    _RsBWMACLLearningPeriod_Type()
)
rsBWMACLLearningPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMACLLearningPeriod.setStatus("mandatory")


class _RsBWMACLTCPHandshakeTimeout_Type(Integer32):
    """Custom type rsBWMACLTCPHandshakeTimeout based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 600),
    )


_RsBWMACLTCPHandshakeTimeout_Type.__name__ = "Integer32"
_RsBWMACLTCPHandshakeTimeout_Object = MibScalar
rsBWMACLTCPHandshakeTimeout = _RsBWMACLTCPHandshakeTimeout_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 71, 5),
    _RsBWMACLTCPHandshakeTimeout_Type()
)
rsBWMACLTCPHandshakeTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMACLTCPHandshakeTimeout.setStatus("mandatory")


class _RsBWMACLTCPEstablishedTimeout_Type(Integer32):
    """Custom type rsBWMACLTCPEstablishedTimeout based on Integer32"""
    defaultValue = 3600

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 7200),
    )


_RsBWMACLTCPEstablishedTimeout_Type.__name__ = "Integer32"
_RsBWMACLTCPEstablishedTimeout_Object = MibScalar
rsBWMACLTCPEstablishedTimeout = _RsBWMACLTCPEstablishedTimeout_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 71, 6),
    _RsBWMACLTCPEstablishedTimeout_Type()
)
rsBWMACLTCPEstablishedTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMACLTCPEstablishedTimeout.setStatus("mandatory")


class _RsBWMACLTCPFinTimeout_Type(Integer32):
    """Custom type rsBWMACLTCPFinTimeout based on Integer32"""
    defaultValue = 120

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 600),
    )


_RsBWMACLTCPFinTimeout_Type.__name__ = "Integer32"
_RsBWMACLTCPFinTimeout_Object = MibScalar
rsBWMACLTCPFinTimeout = _RsBWMACLTCPFinTimeout_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 71, 7),
    _RsBWMACLTCPFinTimeout_Type()
)
rsBWMACLTCPFinTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMACLTCPFinTimeout.setStatus("mandatory")


class _RsBWMACLTCPRstTimeout_Type(Integer32):
    """Custom type rsBWMACLTCPRstTimeout based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 600),
    )


_RsBWMACLTCPRstTimeout_Type.__name__ = "Integer32"
_RsBWMACLTCPRstTimeout_Object = MibScalar
rsBWMACLTCPRstTimeout = _RsBWMACLTCPRstTimeout_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 71, 8),
    _RsBWMACLTCPRstTimeout_Type()
)
rsBWMACLTCPRstTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMACLTCPRstTimeout.setStatus("mandatory")


class _RsBWMACLTCPMidSessMode_Type(Integer32):
    """Custom type rsBWMACLTCPMidSessMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("drop", 1),
          ("allow", 2))
    )


_RsBWMACLTCPMidSessMode_Type.__name__ = "Integer32"
_RsBWMACLTCPMidSessMode_Object = MibScalar
rsBWMACLTCPMidSessMode = _RsBWMACLTCPMidSessMode_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 71, 9),
    _RsBWMACLTCPMidSessMode_Type()
)
rsBWMACLTCPMidSessMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMACLTCPMidSessMode.setStatus("mandatory")


class _RsBWMACLTCPRstValidationMode_Type(Integer32):
    """Custom type rsBWMACLTCPRstValidationMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("drop", 1),
          ("allow", 2),
          ("reportOnly", 3))
    )


_RsBWMACLTCPRstValidationMode_Type.__name__ = "Integer32"
_RsBWMACLTCPRstValidationMode_Object = MibScalar
rsBWMACLTCPRstValidationMode = _RsBWMACLTCPRstValidationMode_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 71, 10),
    _RsBWMACLTCPRstValidationMode_Type()
)
rsBWMACLTCPRstValidationMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMACLTCPRstValidationMode.setStatus("mandatory")


class _RsBWMACLUDPTimeout_Type(Integer32):
    """Custom type rsBWMACLUDPTimeout based on Integer32"""
    defaultValue = 600

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_RsBWMACLUDPTimeout_Type.__name__ = "Integer32"
_RsBWMACLUDPTimeout_Object = MibScalar
rsBWMACLUDPTimeout = _RsBWMACLUDPTimeout_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 71, 11),
    _RsBWMACLUDPTimeout_Type()
)
rsBWMACLUDPTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMACLUDPTimeout.setStatus("mandatory")


class _RsBWMACLICMPTimeout_Type(Integer32):
    """Custom type rsBWMACLICMPTimeout based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 300),
    )


_RsBWMACLICMPTimeout_Type.__name__ = "Integer32"
_RsBWMACLICMPTimeout_Object = MibScalar
rsBWMACLICMPTimeout = _RsBWMACLICMPTimeout_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 71, 12),
    _RsBWMACLICMPTimeout_Type()
)
rsBWMACLICMPTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMACLICMPTimeout.setStatus("mandatory")


class _RsBWMACLOtherTimeout_Type(Integer32):
    """Custom type rsBWMACLOtherTimeout based on Integer32"""
    defaultValue = 600

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7200),
    )


_RsBWMACLOtherTimeout_Type.__name__ = "Integer32"
_RsBWMACLOtherTimeout_Object = MibScalar
rsBWMACLOtherTimeout = _RsBWMACLOtherTimeout_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 71, 13),
    _RsBWMACLOtherTimeout_Type()
)
rsBWMACLOtherTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMACLOtherTimeout.setStatus("mandatory")
_RsBWMACLSummaryReportsTable_Object = MibTable
rsBWMACLSummaryReportsTable = _RsBWMACLSummaryReportsTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 71, 14)
)
if mibBuilder.loadTexts:
    rsBWMACLSummaryReportsTable.setStatus("mandatory")
_RsBWMACLSummaryReportsEntry_Object = MibTableRow
rsBWMACLSummaryReportsEntry = _RsBWMACLSummaryReportsEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 71, 14, 1)
)
rsBWMACLSummaryReportsEntry.setIndexNames(
    (0, "BWM-MIB", "rsBWMACLSummaryReportsPolicyName"),
)
if mibBuilder.loadTexts:
    rsBWMACLSummaryReportsEntry.setStatus("mandatory")


class _RsBWMACLSummaryReportsPolicyName_Type(DisplayString):
    """Custom type rsBWMACLSummaryReportsPolicyName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_RsBWMACLSummaryReportsPolicyName_Type.__name__ = "DisplayString"
_RsBWMACLSummaryReportsPolicyName_Object = MibTableColumn
rsBWMACLSummaryReportsPolicyName = _RsBWMACLSummaryReportsPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 71, 14, 1, 1),
    _RsBWMACLSummaryReportsPolicyName_Type()
)
rsBWMACLSummaryReportsPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMACLSummaryReportsPolicyName.setStatus("mandatory")
_RsBWMACLSummaryReportsTCPAllow_Type = Integer32
_RsBWMACLSummaryReportsTCPAllow_Object = MibTableColumn
rsBWMACLSummaryReportsTCPAllow = _RsBWMACLSummaryReportsTCPAllow_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 71, 14, 1, 2),
    _RsBWMACLSummaryReportsTCPAllow_Type()
)
rsBWMACLSummaryReportsTCPAllow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMACLSummaryReportsTCPAllow.setStatus("mandatory")
_RsBWMACLSummaryReportsTCPDrop_Type = Integer32
_RsBWMACLSummaryReportsTCPDrop_Object = MibTableColumn
rsBWMACLSummaryReportsTCPDrop = _RsBWMACLSummaryReportsTCPDrop_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 71, 14, 1, 3),
    _RsBWMACLSummaryReportsTCPDrop_Type()
)
rsBWMACLSummaryReportsTCPDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMACLSummaryReportsTCPDrop.setStatus("mandatory")
_RsBWMACLSummaryReportsUDPAllow_Type = Integer32
_RsBWMACLSummaryReportsUDPAllow_Object = MibTableColumn
rsBWMACLSummaryReportsUDPAllow = _RsBWMACLSummaryReportsUDPAllow_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 71, 14, 1, 4),
    _RsBWMACLSummaryReportsUDPAllow_Type()
)
rsBWMACLSummaryReportsUDPAllow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMACLSummaryReportsUDPAllow.setStatus("mandatory")
_RsBWMACLSummaryReportsUDPDrop_Type = Integer32
_RsBWMACLSummaryReportsUDPDrop_Object = MibTableColumn
rsBWMACLSummaryReportsUDPDrop = _RsBWMACLSummaryReportsUDPDrop_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 71, 14, 1, 5),
    _RsBWMACLSummaryReportsUDPDrop_Type()
)
rsBWMACLSummaryReportsUDPDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMACLSummaryReportsUDPDrop.setStatus("mandatory")
_RsBWMACLSummaryReportsICMPAllow_Type = Integer32
_RsBWMACLSummaryReportsICMPAllow_Object = MibTableColumn
rsBWMACLSummaryReportsICMPAllow = _RsBWMACLSummaryReportsICMPAllow_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 71, 14, 1, 6),
    _RsBWMACLSummaryReportsICMPAllow_Type()
)
rsBWMACLSummaryReportsICMPAllow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMACLSummaryReportsICMPAllow.setStatus("mandatory")
_RsBWMACLSummaryReportsICMPDrop_Type = Integer32
_RsBWMACLSummaryReportsICMPDrop_Object = MibTableColumn
rsBWMACLSummaryReportsICMPDrop = _RsBWMACLSummaryReportsICMPDrop_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 71, 14, 1, 7),
    _RsBWMACLSummaryReportsICMPDrop_Type()
)
rsBWMACLSummaryReportsICMPDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMACLSummaryReportsICMPDrop.setStatus("mandatory")
_RsBWMACLSummaryReportsOtherAllow_Type = Integer32
_RsBWMACLSummaryReportsOtherAllow_Object = MibTableColumn
rsBWMACLSummaryReportsOtherAllow = _RsBWMACLSummaryReportsOtherAllow_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 71, 14, 1, 8),
    _RsBWMACLSummaryReportsOtherAllow_Type()
)
rsBWMACLSummaryReportsOtherAllow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMACLSummaryReportsOtherAllow.setStatus("mandatory")
_RsBWMACLSummaryReportsOtherDrop_Type = Integer32
_RsBWMACLSummaryReportsOtherDrop_Object = MibTableColumn
rsBWMACLSummaryReportsOtherDrop = _RsBWMACLSummaryReportsOtherDrop_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 71, 14, 1, 9),
    _RsBWMACLSummaryReportsOtherDrop_Type()
)
rsBWMACLSummaryReportsOtherDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMACLSummaryReportsOtherDrop.setStatus("mandatory")
_RsBWMACLSummaryReportsTCPMidSess_Type = Integer32
_RsBWMACLSummaryReportsTCPMidSess_Object = MibTableColumn
rsBWMACLSummaryReportsTCPMidSess = _RsBWMACLSummaryReportsTCPMidSess_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 71, 14, 1, 10),
    _RsBWMACLSummaryReportsTCPMidSess_Type()
)
rsBWMACLSummaryReportsTCPMidSess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMACLSummaryReportsTCPMidSess.setStatus("mandatory")
_RsBWMACLSummaryReportsTCPRstInvalid_Type = Integer32
_RsBWMACLSummaryReportsTCPRstInvalid_Object = MibTableColumn
rsBWMACLSummaryReportsTCPRstInvalid = _RsBWMACLSummaryReportsTCPRstInvalid_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 71, 14, 1, 11),
    _RsBWMACLSummaryReportsTCPRstInvalid_Type()
)
rsBWMACLSummaryReportsTCPRstInvalid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMACLSummaryReportsTCPRstInvalid.setStatus("mandatory")
_RsBWMACLSummaryReportsTCPHandshakeViolation_Type = Integer32
_RsBWMACLSummaryReportsTCPHandshakeViolation_Object = MibTableColumn
rsBWMACLSummaryReportsTCPHandshakeViolation = _RsBWMACLSummaryReportsTCPHandshakeViolation_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 71, 14, 1, 12),
    _RsBWMACLSummaryReportsTCPHandshakeViolation_Type()
)
rsBWMACLSummaryReportsTCPHandshakeViolation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMACLSummaryReportsTCPHandshakeViolation.setStatus("mandatory")
_RsBWMACLSummaryReportsICMPSmurf_Type = Integer32
_RsBWMACLSummaryReportsICMPSmurf_Object = MibTableColumn
rsBWMACLSummaryReportsICMPSmurf = _RsBWMACLSummaryReportsICMPSmurf_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 71, 14, 1, 13),
    _RsBWMACLSummaryReportsICMPSmurf_Type()
)
rsBWMACLSummaryReportsICMPSmurf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMACLSummaryReportsICMPSmurf.setStatus("mandatory")
_RsBWMACLSummaryReportsICMPPacketAnomaly_Type = Integer32
_RsBWMACLSummaryReportsICMPPacketAnomaly_Object = MibTableColumn
rsBWMACLSummaryReportsICMPPacketAnomaly = _RsBWMACLSummaryReportsICMPPacketAnomaly_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 71, 14, 1, 14),
    _RsBWMACLSummaryReportsICMPPacketAnomaly_Type()
)
rsBWMACLSummaryReportsICMPPacketAnomaly.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMACLSummaryReportsICMPPacketAnomaly.setStatus("mandatory")
_RsBWMACLSummaryReportsGREAllow_Type = Integer32
_RsBWMACLSummaryReportsGREAllow_Object = MibTableColumn
rsBWMACLSummaryReportsGREAllow = _RsBWMACLSummaryReportsGREAllow_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 71, 14, 1, 15),
    _RsBWMACLSummaryReportsGREAllow_Type()
)
rsBWMACLSummaryReportsGREAllow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMACLSummaryReportsGREAllow.setStatus("mandatory")
_RsBWMACLSummaryReportsGREDrop_Type = Integer32
_RsBWMACLSummaryReportsGREDrop_Object = MibTableColumn
rsBWMACLSummaryReportsGREDrop = _RsBWMACLSummaryReportsGREDrop_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 71, 14, 1, 16),
    _RsBWMACLSummaryReportsGREDrop_Type()
)
rsBWMACLSummaryReportsGREDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMACLSummaryReportsGREDrop.setStatus("mandatory")
_RsBWMACLSummaryReportsSCTPAllow_Type = Integer32
_RsBWMACLSummaryReportsSCTPAllow_Object = MibTableColumn
rsBWMACLSummaryReportsSCTPAllow = _RsBWMACLSummaryReportsSCTPAllow_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 71, 14, 1, 17),
    _RsBWMACLSummaryReportsSCTPAllow_Type()
)
rsBWMACLSummaryReportsSCTPAllow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMACLSummaryReportsSCTPAllow.setStatus("mandatory")
_RsBWMACLSummaryReportsSCTPDrop_Type = Integer32
_RsBWMACLSummaryReportsSCTPDrop_Object = MibTableColumn
rsBWMACLSummaryReportsSCTPDrop = _RsBWMACLSummaryReportsSCTPDrop_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 71, 14, 1, 18),
    _RsBWMACLSummaryReportsSCTPDrop_Type()
)
rsBWMACLSummaryReportsSCTPDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMACLSummaryReportsSCTPDrop.setStatus("mandatory")
_RsBWMACLSummaryReportsL2TPAllow_Type = Integer32
_RsBWMACLSummaryReportsL2TPAllow_Object = MibTableColumn
rsBWMACLSummaryReportsL2TPAllow = _RsBWMACLSummaryReportsL2TPAllow_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 71, 14, 1, 19),
    _RsBWMACLSummaryReportsL2TPAllow_Type()
)
rsBWMACLSummaryReportsL2TPAllow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMACLSummaryReportsL2TPAllow.setStatus("mandatory")
_RsBWMACLSummaryReportsL2TPDrop_Type = Integer32
_RsBWMACLSummaryReportsL2TPDrop_Object = MibTableColumn
rsBWMACLSummaryReportsL2TPDrop = _RsBWMACLSummaryReportsL2TPDrop_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 71, 14, 1, 20),
    _RsBWMACLSummaryReportsL2TPDrop_Type()
)
rsBWMACLSummaryReportsL2TPDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMACLSummaryReportsL2TPDrop.setStatus("mandatory")
_RsBWMACLSummaryReportsGTPAllow_Type = Integer32
_RsBWMACLSummaryReportsGTPAllow_Object = MibTableColumn
rsBWMACLSummaryReportsGTPAllow = _RsBWMACLSummaryReportsGTPAllow_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 71, 14, 1, 21),
    _RsBWMACLSummaryReportsGTPAllow_Type()
)
rsBWMACLSummaryReportsGTPAllow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMACLSummaryReportsGTPAllow.setStatus("mandatory")
_RsBWMACLSummaryReportsGTPDrop_Type = Integer32
_RsBWMACLSummaryReportsGTPDrop_Object = MibTableColumn
rsBWMACLSummaryReportsGTPDrop = _RsBWMACLSummaryReportsGTPDrop_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 71, 14, 1, 22),
    _RsBWMACLSummaryReportsGTPDrop_Type()
)
rsBWMACLSummaryReportsGTPDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMACLSummaryReportsGTPDrop.setStatus("mandatory")
_RsBWMACLSummaryReportsIPinIPAllow_Type = Integer32
_RsBWMACLSummaryReportsIPinIPAllow_Object = MibTableColumn
rsBWMACLSummaryReportsIPinIPAllow = _RsBWMACLSummaryReportsIPinIPAllow_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 71, 14, 1, 23),
    _RsBWMACLSummaryReportsIPinIPAllow_Type()
)
rsBWMACLSummaryReportsIPinIPAllow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMACLSummaryReportsIPinIPAllow.setStatus("mandatory")
_RsBWMACLSummaryReportsIPinIPDrop_Type = Integer32
_RsBWMACLSummaryReportsIPinIPDrop_Object = MibTableColumn
rsBWMACLSummaryReportsIPinIPDrop = _RsBWMACLSummaryReportsIPinIPDrop_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 71, 14, 1, 24),
    _RsBWMACLSummaryReportsIPinIPDrop_Type()
)
rsBWMACLSummaryReportsIPinIPDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMACLSummaryReportsIPinIPDrop.setStatus("mandatory")


class _RsBWMACLReportMaxTraps_Type(Integer32):
    """Custom type rsBWMACLReportMaxTraps based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_RsBWMACLReportMaxTraps_Type.__name__ = "Integer32"
_RsBWMACLReportMaxTraps_Object = MibScalar
rsBWMACLReportMaxTraps = _RsBWMACLReportMaxTraps_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 71, 15),
    _RsBWMACLReportMaxTraps_Type()
)
rsBWMACLReportMaxTraps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMACLReportMaxTraps.setStatus("mandatory")


class _RsBWMACLReportPeriod_Type(Integer32):
    """Custom type rsBWMACLReportPeriod based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 600),
    )


_RsBWMACLReportPeriod_Type.__name__ = "Integer32"
_RsBWMACLReportPeriod_Object = MibScalar
rsBWMACLReportPeriod = _RsBWMACLReportPeriod_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 71, 16),
    _RsBWMACLReportPeriod_Type()
)
rsBWMACLReportPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMACLReportPeriod.setStatus("mandatory")


class _RsBWMACLReportSendSrp_Type(TruthValue):
    """Custom type rsBWMACLReportSendSrp based on TruthValue"""
    defaultValue = 2


_RsBWMACLReportSendSrp_Type.__name__ = "TruthValue"
_RsBWMACLReportSendSrp_Object = MibScalar
rsBWMACLReportSendSrp = _RsBWMACLReportSendSrp_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 71, 17),
    _RsBWMACLReportSendSrp_Type()
)
rsBWMACLReportSendSrp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMACLReportSendSrp.setStatus("mandatory")


class _RsBWMACLDetailedReportType_Type(Integer32):
    """Custom type rsBWMACLDetailedReportType based on Integer32"""
    defaultValue = 4

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
        *(("disable", 1),
          ("drop", 2),
          ("allow", 3),
          ("all", 4))
    )


_RsBWMACLDetailedReportType_Type.__name__ = "Integer32"
_RsBWMACLDetailedReportType_Object = MibScalar
rsBWMACLDetailedReportType = _RsBWMACLDetailedReportType_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 71, 18),
    _RsBWMACLDetailedReportType_Type()
)
rsBWMACLDetailedReportType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMACLDetailedReportType.setStatus("mandatory")


class _RsBWMACLGRETimeout_Type(Integer32):
    """Custom type rsBWMACLGRETimeout based on Integer32"""
    defaultValue = 3600

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7200),
    )


_RsBWMACLGRETimeout_Type.__name__ = "Integer32"
_RsBWMACLGRETimeout_Object = MibScalar
rsBWMACLGRETimeout = _RsBWMACLGRETimeout_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 71, 19),
    _RsBWMACLGRETimeout_Type()
)
rsBWMACLGRETimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMACLGRETimeout.setStatus("mandatory")


class _RsBWMACLSCTPTimeout_Type(Integer32):
    """Custom type rsBWMACLSCTPTimeout based on Integer32"""
    defaultValue = 3600

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7200),
    )


_RsBWMACLSCTPTimeout_Type.__name__ = "Integer32"
_RsBWMACLSCTPTimeout_Object = MibScalar
rsBWMACLSCTPTimeout = _RsBWMACLSCTPTimeout_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 71, 20),
    _RsBWMACLSCTPTimeout_Type()
)
rsBWMACLSCTPTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMACLSCTPTimeout.setStatus("mandatory")


class _RsBWMACLAllowICMPSmurf_Type(TruthValue):
    """Custom type rsBWMACLAllowICMPSmurf based on TruthValue"""
    defaultValue = 2


_RsBWMACLAllowICMPSmurf_Type.__name__ = "TruthValue"
_RsBWMACLAllowICMPSmurf_Object = MibScalar
rsBWMACLAllowICMPSmurf = _RsBWMACLAllowICMPSmurf_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 71, 21),
    _RsBWMACLAllowICMPSmurf_Type()
)
rsBWMACLAllowICMPSmurf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMACLAllowICMPSmurf.setStatus("mandatory")


class _RsBWMACLL2TPTimeout_Type(Integer32):
    """Custom type rsBWMACLL2TPTimeout based on Integer32"""
    defaultValue = 3600

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7200),
    )


_RsBWMACLL2TPTimeout_Type.__name__ = "Integer32"
_RsBWMACLL2TPTimeout_Object = MibScalar
rsBWMACLL2TPTimeout = _RsBWMACLL2TPTimeout_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 71, 22),
    _RsBWMACLL2TPTimeout_Type()
)
rsBWMACLL2TPTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMACLL2TPTimeout.setStatus("mandatory")


class _RsBWMACLGTPTimeout_Type(Integer32):
    """Custom type rsBWMACLGTPTimeout based on Integer32"""
    defaultValue = 3600

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7200),
    )


_RsBWMACLGTPTimeout_Type.__name__ = "Integer32"
_RsBWMACLGTPTimeout_Object = MibScalar
rsBWMACLGTPTimeout = _RsBWMACLGTPTimeout_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 71, 23),
    _RsBWMACLGTPTimeout_Type()
)
rsBWMACLGTPTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMACLGTPTimeout.setStatus("mandatory")
_RsBWMACLPacketTraceStatus_Type = FeatureStatus
_RsBWMACLPacketTraceStatus_Object = MibScalar
rsBWMACLPacketTraceStatus = _RsBWMACLPacketTraceStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 71, 24),
    _RsBWMACLPacketTraceStatus_Type()
)
rsBWMACLPacketTraceStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMACLPacketTraceStatus.setStatus("mandatory")


class _RsBWMACLIPinIPTimeout_Type(Integer32):
    """Custom type rsBWMACLIPinIPTimeout based on Integer32"""
    defaultValue = 3600

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7200),
    )


_RsBWMACLIPinIPTimeout_Type.__name__ = "Integer32"
_RsBWMACLIPinIPTimeout_Object = MibScalar
rsBWMACLIPinIPTimeout = _RsBWMACLIPinIPTimeout_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 71, 25),
    _RsBWMACLIPinIPTimeout_Type()
)
rsBWMACLIPinIPTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMACLIPinIPTimeout.setStatus("mandatory")


class _RsBWMACLDefaultAction_Type(Integer32):
    """Custom type rsBWMACLDefaultAction based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("accept", 1),
          ("drop", 2),
          ("current", 3))
    )


_RsBWMACLDefaultAction_Type.__name__ = "Integer32"
_RsBWMACLDefaultAction_Object = MibScalar
rsBWMACLDefaultAction = _RsBWMACLDefaultAction_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 71, 26),
    _RsBWMACLDefaultAction_Type()
)
rsBWMACLDefaultAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMACLDefaultAction.setStatus("mandatory")
_RsBWMSecGroupTable_Object = MibTable
rsBWMSecGroupTable = _RsBWMSecGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 73)
)
if mibBuilder.loadTexts:
    rsBWMSecGroupTable.setStatus("mandatory")
_RsBWMModifySecGrpTag_Object = MibTableRow
rsBWMModifySecGrpTag = _RsBWMModifySecGrpTag_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 73, 1)
)
rsBWMModifySecGrpTag.setIndexNames(
    (0, "BWM-MIB", "rsBWMSecGroupEntryName"),
)
if mibBuilder.loadTexts:
    rsBWMModifySecGrpTag.setStatus("mandatory")


class _RsBWMSecGroupEntryName_Type(DisplayString):
    """Custom type rsBWMSecGroupEntryName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 19),
    )


_RsBWMSecGroupEntryName_Type.__name__ = "DisplayString"
_RsBWMSecGroupEntryName_Object = MibTableColumn
rsBWMSecGroupEntryName = _RsBWMSecGroupEntryName_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 73, 1, 1),
    _RsBWMSecGroupEntryName_Type()
)
rsBWMSecGroupEntryName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMSecGroupEntryName.setStatus("mandatory")


class _RsBWMSecGroupEntryValue_Type(Integer32):
    """Custom type rsBWMSecGroupEntryValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RsBWMSecGroupEntryValue_Type.__name__ = "Integer32"
_RsBWMSecGroupEntryValue_Object = MibTableColumn
rsBWMSecGroupEntryValue = _RsBWMSecGroupEntryValue_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 73, 1, 2),
    _RsBWMSecGroupEntryValue_Type()
)
rsBWMSecGroupEntryValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMSecGroupEntryValue.setStatus("mandatory")


class _RsBWMSecGroupEntryStatus_Type(Integer32):
    """Custom type rsBWMSecGroupEntryStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_RsBWMSecGroupEntryStatus_Type.__name__ = "Integer32"
_RsBWMSecGroupEntryStatus_Object = MibTableColumn
rsBWMSecGroupEntryStatus = _RsBWMSecGroupEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 73, 1, 3),
    _RsBWMSecGroupEntryStatus_Type()
)
rsBWMSecGroupEntryStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMSecGroupEntryStatus.setStatus("mandatory")
_RsBWMSecGroupEntryRowStatus_Type = RowStatus
_RsBWMSecGroupEntryRowStatus_Object = MibTableColumn
rsBWMSecGroupEntryRowStatus = _RsBWMSecGroupEntryRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 73, 1, 4),
    _RsBWMSecGroupEntryRowStatus_Type()
)
rsBWMSecGroupEntryRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsBWMSecGroupEntryRowStatus.setStatus("mandatory")
_RsBWMSecGroupCurrentTable_Object = MibTable
rsBWMSecGroupCurrentTable = _RsBWMSecGroupCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 74)
)
if mibBuilder.loadTexts:
    rsBWMSecGroupCurrentTable.setStatus("mandatory")
_RsBWMActiveSecGrpTag_Object = MibTableRow
rsBWMActiveSecGrpTag = _RsBWMActiveSecGrpTag_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 74, 1)
)
rsBWMActiveSecGrpTag.setIndexNames(
    (0, "BWM-MIB", "rsBWMSecGroupActiveEntryName"),
)
if mibBuilder.loadTexts:
    rsBWMActiveSecGrpTag.setStatus("mandatory")


class _RsBWMSecGroupActiveEntryName_Type(DisplayString):
    """Custom type rsBWMSecGroupActiveEntryName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 19),
    )


_RsBWMSecGroupActiveEntryName_Type.__name__ = "DisplayString"
_RsBWMSecGroupActiveEntryName_Object = MibTableColumn
rsBWMSecGroupActiveEntryName = _RsBWMSecGroupActiveEntryName_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 74, 1, 1),
    _RsBWMSecGroupActiveEntryName_Type()
)
rsBWMSecGroupActiveEntryName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMSecGroupActiveEntryName.setStatus("mandatory")
_RsBWMSecGroupEntryActiveValue_Type = Integer32
_RsBWMSecGroupEntryActiveValue_Object = MibTableColumn
rsBWMSecGroupEntryActiveValue = _RsBWMSecGroupEntryActiveValue_Object(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 74, 1, 2),
    _RsBWMSecGroupEntryActiveValue_Type()
)
rsBWMSecGroupEntryActiveValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsBWMSecGroupEntryActiveValue.setStatus("mandatory")

# Managed Objects groups


# Notification objects

rsBWMPacketBlocked = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 0, 1)
)
rsBWMPacketBlocked.setObjects(
      *(("RADWARE-MIB", "rndErrorDesc"),
        ("RADWARE-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    rsBWMPacketBlocked.setStatus(
        ""
    )

rsBWMTrafficFlowBWTablesFull = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 0, 2)
)
rsBWMTrafficFlowBWTablesFull.setObjects(
      *(("RADWARE-MIB", "rndErrorDesc"),
        ("RADWARE-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    rsBWMTrafficFlowBWTablesFull.setStatus(
        ""
    )

rsBWMFilterCreationFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 0, 3)
)
rsBWMFilterCreationFailed.setObjects(
      *(("RADWARE-MIB", "rndErrorDesc"),
        ("RADWARE-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    rsBWMFilterCreationFailed.setStatus(
        ""
    )

rsBWMNoDefaultGatewayForClassification = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 0, 4)
)
rsBWMNoDefaultGatewayForClassification.setObjects(
      *(("RADWARE-MIB", "rndErrorDesc"),
        ("RADWARE-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    rsBWMNoDefaultGatewayForClassification.setStatus(
        ""
    )

rsBWMAttackReportTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 35, 1, 60, 0, 5)
)
rsBWMAttackReportTrap.setObjects(
      *(("RADWARE-MIB", "rndErrorDesc"),
        ("RADWARE-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    rsBWMAttackReportTrap.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BWM-MIB",
    **{"NetNumber": NetNumber,
       "rsBWMPacketBlocked": rsBWMPacketBlocked,
       "rsBWMTrafficFlowBWTablesFull": rsBWMTrafficFlowBWTablesFull,
       "rsBWMFilterCreationFailed": rsBWMFilterCreationFailed,
       "rsBWMNoDefaultGatewayForClassification": rsBWMNoDefaultGatewayForClassification,
       "rsBWMAttackReportTrap": rsBWMAttackReportTrap,
       "rsBWMRulesTable": rsBWMRulesTable,
       "rsBWMRulesEntry": rsBWMRulesEntry,
       "rsBWMRulesIndex": rsBWMRulesIndex,
       "rsBWMRulesName": rsBWMRulesName,
       "rsBWMRulesDestination": rsBWMRulesDestination,
       "rsBWMRulesSource": rsBWMRulesSource,
       "rsBWMRulesStatus": rsBWMRulesStatus,
       "rsBWMRulesAction": rsBWMRulesAction,
       "rsBWMRulesDirection": rsBWMRulesDirection,
       "rsBWMRulesPriority": rsBWMRulesPriority,
       "rsBWMRulesPhysicalPort": rsBWMRulesPhysicalPort,
       "rsBWMRulesType": rsBWMRulesType,
       "rsBWMRulesDescription": rsBWMRulesDescription,
       "rsBWMRulesGuaranteedBW": rsBWMRulesGuaranteedBW,
       "rsBWMRulesPolicyType": rsBWMRulesPolicyType,
       "rsBWMRulesPolicy": rsBWMRulesPolicy,
       "rsBWMRulesOperationalStatus": rsBWMRulesOperationalStatus,
       "rsBWMRulesDSCPMarking": rsBWMRulesDSCPMarking,
       "rsBWMRulesReportBlockedPackets": rsBWMRulesReportBlockedPackets,
       "rsBWMRulesMaxBW": rsBWMRulesMaxBW,
       "rsBWMRulesSpecific": rsBWMRulesSpecific,
       "rsBWMRulesPhysicalPortGroup": rsBWMRulesPhysicalPortGroup,
       "rsBWMRulesVLANTagGroup": rsBWMRulesVLANTagGroup,
       "rsBWMRulesTrafficIdentification": rsBWMRulesTrafficIdentification,
       "rsBWMRulesTrafficFlowMaxBW": rsBWMRulesTrafficFlowMaxBW,
       "rsBWMRulesMaxConcurrentSessions": rsBWMRulesMaxConcurrentSessions,
       "rsBWMRulesTrafficIDCookieField": rsBWMRulesTrafficIDCookieField,
       "rsBWMRulesPolicyGroup": rsBWMRulesPolicyGroup,
       "rsBWMRulesRadiusRule": rsBWMRulesRadiusRule,
       "rsBWMRulesIPObjectTable": rsBWMRulesIPObjectTable,
       "rsBWMRulesIPObjectEntry": rsBWMRulesIPObjectEntry,
       "rsBWMRulesIPObjectName": rsBWMRulesIPObjectName,
       "rsBWMRulesIPObjectSubIndex": rsBWMRulesIPObjectSubIndex,
       "rsBWMRulesIPObjectAddress": rsBWMRulesIPObjectAddress,
       "rsBWMRulesIPObjectMask": rsBWMRulesIPObjectMask,
       "rsBWMRulesIPObjectFromIP": rsBWMRulesIPObjectFromIP,
       "rsBWMRulesIPObjectToIP": rsBWMRulesIPObjectToIP,
       "rsBWMRulesIPObjectMode": rsBWMRulesIPObjectMode,
       "rsBWMRulesIPObjectStatus": rsBWMRulesIPObjectStatus,
       "rsBWMCBQMode": rsBWMCBQMode,
       "rsBWMActualQueueSize": rsBWMActualQueueSize,
       "rsBWMAverageQueueSize": rsBWMAverageQueueSize,
       "rsBWMQueueRedDropped": rsBWMQueueRedDropped,
       "rsBWMPriorityTable": rsBWMPriorityTable,
       "rsBWMPriorityEntry": rsBWMPriorityEntry,
       "rsBWMPriority": rsBWMPriority,
       "rsBWMPacketsSent": rsBWMPacketsSent,
       "rsBWMRedMode": rsBWMRedMode,
       "rsBWMCurrentRulesTable": rsBWMCurrentRulesTable,
       "rsBWMCurrentRulesEntry": rsBWMCurrentRulesEntry,
       "rsBWMCurrentRulesIndex": rsBWMCurrentRulesIndex,
       "rsBWMCurrentRulesName": rsBWMCurrentRulesName,
       "rsBWMCurrentRulesDestination": rsBWMCurrentRulesDestination,
       "rsBWMCurrentRulesSource": rsBWMCurrentRulesSource,
       "rsBWMCurrentRulesAction": rsBWMCurrentRulesAction,
       "rsBWMCurrentRulesDirection": rsBWMCurrentRulesDirection,
       "rsBWMCurrentRulesPriority": rsBWMCurrentRulesPriority,
       "rsBWMCurrentRulesPhysicalPort": rsBWMCurrentRulesPhysicalPort,
       "rsBWMCurrentRulesType": rsBWMCurrentRulesType,
       "rsBWMCurrentRulesDescription": rsBWMCurrentRulesDescription,
       "rsBWMCurrentRulesGuaranteedBW": rsBWMCurrentRulesGuaranteedBW,
       "rsBWMCurrentRulesMaxBW": rsBWMCurrentRulesMaxBW,
       "rsBWMCurrentRulesPolicyType": rsBWMCurrentRulesPolicyType,
       "rsBWMCurrentRulesPolicy": rsBWMCurrentRulesPolicy,
       "rsBWMCurrentRulesDSCPMarking": rsBWMCurrentRulesDSCPMarking,
       "rsBWMCurrentRulesReportBlockedPackets": rsBWMCurrentRulesReportBlockedPackets,
       "rsBWMCurrentRulesSpecific": rsBWMCurrentRulesSpecific,
       "rsBWMCurrentRulesPhysicalPortGroup": rsBWMCurrentRulesPhysicalPortGroup,
       "rsBWMCurrentRulesVLANTagGroup": rsBWMCurrentRulesVLANTagGroup,
       "rsBWMCurrentRulesTrafficIdentification": rsBWMCurrentRulesTrafficIdentification,
       "rsBWMCurrentRulesTrafficFlowMaxBW": rsBWMCurrentRulesTrafficFlowMaxBW,
       "rsBWMCurrentRulesMaxConcurrentSessions": rsBWMCurrentRulesMaxConcurrentSessions,
       "rsBWMCurrentRulesTrafficIDCookieField": rsBWMCurrentRulesTrafficIDCookieField,
       "rsBWMCurrentRulesPolicyGroup": rsBWMCurrentRulesPolicyGroup,
       "rsBWMCurrentRulesRadiusRule": rsBWMCurrentRulesRadiusRule,
       "rsBWMCurrentRulesIPObjectTable": rsBWMCurrentRulesIPObjectTable,
       "rsBWMCurrentRulesIPObjectEntry": rsBWMCurrentRulesIPObjectEntry,
       "rsBWMCurrentRulesIPObjectName": rsBWMCurrentRulesIPObjectName,
       "rsBWMCurrentRulesIPObjectSubIndex": rsBWMCurrentRulesIPObjectSubIndex,
       "rsBWMCurrentRulesIPObjectAddress": rsBWMCurrentRulesIPObjectAddress,
       "rsBWMCurrentRulesIPObjectMask": rsBWMCurrentRulesIPObjectMask,
       "rsBWMCurrentRulesIPObjectFromIP": rsBWMCurrentRulesIPObjectFromIP,
       "rsBWMCurrentRulesIPObjectToIP": rsBWMCurrentRulesIPObjectToIP,
       "rsBWMCurrentRulesIPObjectMode": rsBWMCurrentRulesIPObjectMode,
       "rsBWMClassificationMode": rsBWMClassificationMode,
       "rsBWMMaximumBandwidth": rsBWMMaximumBandwidth,
       "rsBWMBandwidthBorrowingMode": rsBWMBandwidthBorrowingMode,
       "rsBWMActions": rsBWMActions,
       "rsBWMFilterEntryTable": rsBWMFilterEntryTable,
       "rsBWMFilterEntry": rsBWMFilterEntry,
       "rsBWMFilterName": rsBWMFilterName,
       "rsBWMFilterDescription": rsBWMFilterDescription,
       "rsBWMFilterProtocol": rsBWMFilterProtocol,
       "rsBWMFilterDestinationPort": rsBWMFilterDestinationPort,
       "rsBWMFilterSourceFromPort": rsBWMFilterSourceFromPort,
       "rsBWMFilterSourceToPort": rsBWMFilterSourceToPort,
       "rsBWMFilterOMPCOffset": rsBWMFilterOMPCOffset,
       "rsBWMFilterOMPCMask": rsBWMFilterOMPCMask,
       "rsBWMFilterOMPCPattern": rsBWMFilterOMPCPattern,
       "rsBWMFilterOMPCCondition": rsBWMFilterOMPCCondition,
       "rsBWMFilterOMPCLength": rsBWMFilterOMPCLength,
       "rsBWMFilterContentOffset": rsBWMFilterContentOffset,
       "rsBWMFilterContent": rsBWMFilterContent,
       "rsBWMFilterContentType": rsBWMFilterContentType,
       "rsBWMFilterType": rsBWMFilterType,
       "rsBWMFilterStatus": rsBWMFilterStatus,
       "rsBWMFilterContentEnd": rsBWMFilterContentEnd,
       "rsBWMFilterContentData": rsBWMFilterContentData,
       "rsBWMFilterContentCoding": rsBWMFilterContentCoding,
       "rsBWMFilterContentDataCoding": rsBWMFilterContentDataCoding,
       "rsBWMFilterOMPCOffsetBase": rsBWMFilterOMPCOffsetBase,
       "rsBWMFilterDestinationMaxPort": rsBWMFilterDestinationMaxPort,
       "rsBWMFilterSourceAppPortGroup": rsBWMFilterSourceAppPortGroup,
       "rsBWMFilterDestinationAppPortGroup": rsBWMFilterDestinationAppPortGroup,
       "rsBWMFilterSessionType": rsBWMFilterSessionType,
       "rsBWMFilterSessionTypeDirection": rsBWMFilterSessionTypeDirection,
       "rsBWMCurrentFilterEntryTable": rsBWMCurrentFilterEntryTable,
       "rsBWMCurrentFilterEntry": rsBWMCurrentFilterEntry,
       "rsBWMCurrentFilterName": rsBWMCurrentFilterName,
       "rsBWMCurrentFilterDescription": rsBWMCurrentFilterDescription,
       "rsBWMCurrentFilterProtocol": rsBWMCurrentFilterProtocol,
       "rsBWMCurrentFilterDestinationPort": rsBWMCurrentFilterDestinationPort,
       "rsBWMCurrentFilterSourceFromPort": rsBWMCurrentFilterSourceFromPort,
       "rsBWMCurrentFilterSourceToPort": rsBWMCurrentFilterSourceToPort,
       "rsBWMCurrentFilterOMPCOffset": rsBWMCurrentFilterOMPCOffset,
       "rsBWMCurrentFilterOMPCMask": rsBWMCurrentFilterOMPCMask,
       "rsBWMCurrentFilterOMPCPattern": rsBWMCurrentFilterOMPCPattern,
       "rsBWMCurrentFilterOMPCCondition": rsBWMCurrentFilterOMPCCondition,
       "rsBWMCurrentFilterOMPCLength": rsBWMCurrentFilterOMPCLength,
       "rsBWMCurrentFilterContentOffset": rsBWMCurrentFilterContentOffset,
       "rsBWMCurrentFilterContent": rsBWMCurrentFilterContent,
       "rsBWMCurrentFilterContentType": rsBWMCurrentFilterContentType,
       "rsBWMCurrentFilterType": rsBWMCurrentFilterType,
       "rsBWMCurrentFilterContentEnd": rsBWMCurrentFilterContentEnd,
       "rsBWMCurrentFilterContentData": rsBWMCurrentFilterContentData,
       "rsBWMCurrentFilterContentCoding": rsBWMCurrentFilterContentCoding,
       "rsBWMCurrentFilterContentDataCoding": rsBWMCurrentFilterContentDataCoding,
       "rsBWMCurrentFilterOMPCOffsetBase": rsBWMCurrentFilterOMPCOffsetBase,
       "rsBWMCurrentFilterDestinationMaxPort": rsBWMCurrentFilterDestinationMaxPort,
       "rsBWMCurrentFilterSourceAppPortGroup": rsBWMCurrentFilterSourceAppPortGroup,
       "rsBWMCurrentFilterDestinationAppPortGroup": rsBWMCurrentFilterDestinationAppPortGroup,
       "rsBWMCurrentFilterSessionType": rsBWMCurrentFilterSessionType,
       "rsBWMCurrentFilterSessionTypeDirection": rsBWMCurrentFilterSessionTypeDirection,
       "rsBWMFilterGroupTable": rsBWMFilterGroupTable,
       "rsBWMFilterGroup": rsBWMFilterGroup,
       "rsBWMFilterGroupName": rsBWMFilterGroupName,
       "rsBWMFilterEntryName": rsBWMFilterEntryName,
       "rsBWMFilterGroupType": rsBWMFilterGroupType,
       "rsBWMFilterGroupStatus": rsBWMFilterGroupStatus,
       "rsBWMCurrentFilterGroupTable": rsBWMCurrentFilterGroupTable,
       "rsBWMCurrentFilterGroup": rsBWMCurrentFilterGroup,
       "rsBWMCurrentFilterGroupName": rsBWMCurrentFilterGroupName,
       "rsBWMCurrentFilterEntryName": rsBWMCurrentFilterEntryName,
       "rsBWMCurrentFilterGroupType": rsBWMCurrentFilterGroupType,
       "rsBWMFilterPolicyTable": rsBWMFilterPolicyTable,
       "rsBWMFilterPolicyEntry": rsBWMFilterPolicyEntry,
       "rsBWMFilterPolicyName": rsBWMFilterPolicyName,
       "rsBWMFilterPolicyEntryName": rsBWMFilterPolicyEntryName,
       "rsBWMFilterPolicyType": rsBWMFilterPolicyType,
       "rsBWMFilterPolicyStatus": rsBWMFilterPolicyStatus,
       "rsBWMFilterPolicyEntryType": rsBWMFilterPolicyEntryType,
       "rsBWMCurrentFilterPolicyTable": rsBWMCurrentFilterPolicyTable,
       "rsBWMCurrentFilterPolicyEntry": rsBWMCurrentFilterPolicyEntry,
       "rsBWMCurrentFilterPolicyName": rsBWMCurrentFilterPolicyName,
       "rsBWMCurrentFilterPolicyEntryName": rsBWMCurrentFilterPolicyEntryName,
       "rsBWMCurrentFilterPolicyType": rsBWMCurrentFilterPolicyType,
       "rsBWMCurrentFilterPolicyEntryType": rsBWMCurrentFilterPolicyEntryType,
       "rsBWMApplicationClassification": rsBWMApplicationClassification,
       "rsBWMPortBandwidthEntryTable": rsBWMPortBandwidthEntryTable,
       "rsBWMPortBandwidthEntry": rsBWMPortBandwidthEntry,
       "rsBWMPortIndex": rsBWMPortIndex,
       "rsBWMPortBandwidth": rsBWMPortBandwidth,
       "rsBwmPortUsedBandwidth": rsBwmPortUsedBandwidth,
       "rsBWMTuning": rsBWMTuning,
       "rsBWMPolicyTuning": rsBWMPolicyTuning,
       "rsBWMPolicyEntries": rsBWMPolicyEntries,
       "rsBWMPolicyEntriesAfterReset": rsBWMPolicyEntriesAfterReset,
       "rsBWMPolicyLeavesPercent": rsBWMPolicyLeavesPercent,
       "rsBWMPolicyLeavesPercentAfterReset": rsBWMPolicyLeavesPercentAfterReset,
       "rsBWMNetworkTuning": rsBWMNetworkTuning,
       "rsBWMNetworkEntries": rsBWMNetworkEntries,
       "rsBWMNetworkEntriesAfterReset": rsBWMNetworkEntriesAfterReset,
       "rsBWMFilterTuning": rsBWMFilterTuning,
       "rsBWMFilterEntries": rsBWMFilterEntries,
       "rsBWMFilterEntriesAfterReset": rsBWMFilterEntriesAfterReset,
       "rsBWMAdvancedTuning": rsBWMAdvancedTuning,
       "rsBWMAdvancedEntries": rsBWMAdvancedEntries,
       "rsBWMAdvancedEntriesAfterReset": rsBWMAdvancedEntriesAfterReset,
       "rsBWMGroupTuning": rsBWMGroupTuning,
       "rsBWMGroupEntries": rsBWMGroupEntries,
       "rsBWMGroupEntriesAfterReset": rsBWMGroupEntriesAfterReset,
       "rsBWMDestinationTuning": rsBWMDestinationTuning,
       "rsBWMDestinationEntries": rsBWMDestinationEntries,
       "rsBWMDestinationEntriesAfterReset": rsBWMDestinationEntriesAfterReset,
       "rsBWMSessionTuning": rsBWMSessionTuning,
       "rsBWMSessionEntries": rsBWMSessionEntries,
       "rsBWMSessionEntriesAfterReset": rsBWMSessionEntriesAfterReset,
       "rsBWMChainTuning": rsBWMChainTuning,
       "rsBWMMaxChainPolicies": rsBWMMaxChainPolicies,
       "rsBWMMaxChainPoliciesAfterReset": rsBWMMaxChainPoliciesAfterReset,
       "rsBWMContentTuning": rsBWMContentTuning,
       "rsBWMContentEntries": rsBWMContentEntries,
       "rsBWMContentEntriesAfterReset": rsBWMContentEntriesAfterReset,
       "rsBWMNetworkIPTuning": rsBWMNetworkIPTuning,
       "rsBWMNetworkIPHashEntries": rsBWMNetworkIPHashEntries,
       "rsBWMNetworkIPHashEntriesAfterReset": rsBWMNetworkIPHashEntriesAfterReset,
       "rsBWMNetworkRangeTuning": rsBWMNetworkRangeTuning,
       "rsBWMNetworkRangeEntries": rsBWMNetworkRangeEntries,
       "rsBWMNetworkRangeEntriesAfterReset": rsBWMNetworkRangeEntriesAfterReset,
       "rsBWMDynamicNetworkTuning": rsBWMDynamicNetworkTuning,
       "rsBWMDynamicNetworkEntries": rsBWMDynamicNetworkEntries,
       "rsBWMDynamicNetworkEntriesAfterReset": rsBWMDynamicNetworkEntriesAfterReset,
       "rsBWMDynamicNetworkIPTuning": rsBWMDynamicNetworkIPTuning,
       "rsBWMDynamicNetworkIPHashEntries": rsBWMDynamicNetworkIPHashEntries,
       "rsBWMDynamicNetworkIPHashEntriesAfterReset": rsBWMDynamicNetworkIPHashEntriesAfterReset,
       "rsBWMDynamicNetworkRangeTuning": rsBWMDynamicNetworkRangeTuning,
       "rsBWMDynamicNetworkRangeEntries": rsBWMDynamicNetworkRangeEntries,
       "rsBWMDynamicNetworkRangeEntriesAfterReset": rsBWMDynamicNetworkRangeEntriesAfterReset,
       "rsBWMMacGroupTuning": rsBWMMacGroupTuning,
       "rsBWMMacGroupEntries": rsBWMMacGroupEntries,
       "rsBWMMacGroupEntriesAfterReset": rsBWMMacGroupEntriesAfterReset,
       "rsBWMParallelStringSearchMemoryTuning": rsBWMParallelStringSearchMemoryTuning,
       "rsBWMParallelStringSearchMemory": rsBWMParallelStringSearchMemory,
       "rsBWMParallelStringSearchMemoryAfterReset": rsBWMParallelStringSearchMemoryAfterReset,
       "rsBWMTrafficFlowBWTuning": rsBWMTrafficFlowBWTuning,
       "rsBWMTrafficFlowBWEntries": rsBWMTrafficFlowBWEntries,
       "rsBWMTrafficFlowBWEntriesAfterReset": rsBWMTrafficFlowBWEntriesAfterReset,
       "rsBWMAppPortGroupTuning": rsBWMAppPortGroupTuning,
       "rsBWMAppPortGroupTuningEntries": rsBWMAppPortGroupTuningEntries,
       "rsBWMAppPortGroupTuningEntriesAfterReset": rsBWMAppPortGroupTuningEntriesAfterReset,
       "rsBWMFarmsClassifyListsTuning": rsBWMFarmsClassifyListsTuning,
       "rsBWMFarmsClassifyListsTuningEntries": rsBWMFarmsClassifyListsTuningEntries,
       "rsBWMFarmsClassifyListsTuningEntriesAfterReset": rsBWMFarmsClassifyListsTuningEntriesAfterReset,
       "rsBWMDSCPEntryTable": rsBWMDSCPEntryTable,
       "rsBWMDSCPEntry": rsBWMDSCPEntry,
       "rsBWMDSCP": rsBWMDSCP,
       "rsBWMDSCPPriority": rsBWMDSCPPriority,
       "rsBWMDSCPGuaranteedBW": rsBWMDSCPGuaranteedBW,
       "rsBWMDSCPMaxBW": rsBWMDSCPMaxBW,
       "rsBWMCurrentDSCPEntryTable": rsBWMCurrentDSCPEntryTable,
       "rsBWMCurrentDSCPEntry": rsBWMCurrentDSCPEntry,
       "rsBWMCurrentDSCP": rsBWMCurrentDSCP,
       "rsBWMCurrentDSCPPriority": rsBWMCurrentDSCPPriority,
       "rsBWMCurrentDSCPGuaranteedBW": rsBWMCurrentDSCPGuaranteedBW,
       "rsBWMCurrentDSCPMaxBW": rsBWMCurrentDSCPMaxBW,
       "rsBWMVersion": rsBWMVersion,
       "rsBWMBwmPortOperationTable": rsBWMBwmPortOperationTable,
       "rsBWMBwmPortOperationEntry": rsBWMBwmPortOperationEntry,
       "rsBWMBwmInboundPort": rsBWMBwmInboundPort,
       "rsBWMBwmOutboundPort": rsBWMBwmOutboundPort,
       "rsBWMBwmDirection": rsBWMBwmDirection,
       "rsBWMBwmOperationStatus": rsBWMBwmOperationStatus,
       "rsBWMBwmVLANOperationTable": rsBWMBwmVLANOperationTable,
       "rsBWMBwmVLANOperationEntry": rsBWMBwmVLANOperationEntry,
       "rsBWMBwmVLAN": rsBWMBwmVLAN,
       "rsBWMBwmVLANOperationStatus": rsBWMBwmVLANOperationStatus,
       "rsBWMSessionAgingTime": rsBWMSessionAgingTime,
       "rsBWMStatisticsTable": rsBWMStatisticsTable,
       "rsBWMStatisticsEntry": rsBWMStatisticsEntry,
       "rsBWMStatisticsPolicyName": rsBWMStatisticsPolicyName,
       "rsBWMStatisticsBandwidthUsedLastSec": rsBWMStatisticsBandwidthUsedLastSec,
       "rsBWMStatisticsPacketNumberLastSec": rsBWMStatisticsPacketNumberLastSec,
       "rsBWMStatisticsFullQueueFailuresBWLastSec": rsBWMStatisticsFullQueueFailuresBWLastSec,
       "rsBWMStatisticsAgedPacketsFailuresBWLastSec": rsBWMStatisticsAgedPacketsFailuresBWLastSec,
       "rsBWMStatisticsGuaranteedReachedLastSec": rsBWMStatisticsGuaranteedReachedLastSec,
       "rsBWMStatisticsMaximumReachedLastSec": rsBWMStatisticsMaximumReachedLastSec,
       "rsBWMStatisticsBandwidthUsedLastPeriod": rsBWMStatisticsBandwidthUsedLastPeriod,
       "rsBWMStatisticsPeakBandwidthLastPeriod": rsBWMStatisticsPeakBandwidthLastPeriod,
       "rsBWMStatisticsPacketNumberLastPeriod": rsBWMStatisticsPacketNumberLastPeriod,
       "rsBWMStatisticsFullQueueFailuresBWLastPeriod": rsBWMStatisticsFullQueueFailuresBWLastPeriod,
       "rsBWMStatisticsAgedPacketsFailuresBWLastPeriod": rsBWMStatisticsAgedPacketsFailuresBWLastPeriod,
       "rsBWMStatisticsGuaranteedReachedCounterLastPeriod": rsBWMStatisticsGuaranteedReachedCounterLastPeriod,
       "rsBWMStatisticsMaximumReachedCounterLastPeriod": rsBWMStatisticsMaximumReachedCounterLastPeriod,
       "rsBWMStatisticsMatchedBandwidthLastSec": rsBWMStatisticsMatchedBandwidthLastSec,
       "rsBWMStatisticsMatchedBandwidthLastPeriod": rsBWMStatisticsMatchedBandwidthLastPeriod,
       "rsBWMStatisticsInboundBandwidthUsedLastSec": rsBWMStatisticsInboundBandwidthUsedLastSec,
       "rsBWMStatisticsInboundBandwidthUsedLastPeriod": rsBWMStatisticsInboundBandwidthUsedLastPeriod,
       "rsBWMStatisticsInboundMatchedBandwidthLastSec": rsBWMStatisticsInboundMatchedBandwidthLastSec,
       "rsBWMStatisticsInboundMatchedBandwidthLastPeriod": rsBWMStatisticsInboundMatchedBandwidthLastPeriod,
       "rsBWMStatisticsInboundPacketNumberLastSec": rsBWMStatisticsInboundPacketNumberLastSec,
       "rsBWMStatisticsInboundPacketNumberLastPeriod": rsBWMStatisticsInboundPacketNumberLastPeriod,
       "rsBWMStatisticsOutboundBandwidthUsedLastSec": rsBWMStatisticsOutboundBandwidthUsedLastSec,
       "rsBWMStatisticsOutboundBandwidthUsedLastPeriod": rsBWMStatisticsOutboundBandwidthUsedLastPeriod,
       "rsBWMStatisticsOutboundMatchedBandwidthLastSec": rsBWMStatisticsOutboundMatchedBandwidthLastSec,
       "rsBWMStatisticsOutboundMatchedBandwidthLastPeriod": rsBWMStatisticsOutboundMatchedBandwidthLastPeriod,
       "rsBWMStatisticsOutboundPacketNumberLastSec": rsBWMStatisticsOutboundPacketNumberLastSec,
       "rsBWMStatisticsOutboundPacketNumberLastPeriod": rsBWMStatisticsOutboundPacketNumberLastPeriod,
       "rsBWMStatisticsNewTCPConnectionsLastSec": rsBWMStatisticsNewTCPConnectionsLastSec,
       "rsBWMStatisticsNewTCPConnectionsLastPeriod": rsBWMStatisticsNewTCPConnectionsLastPeriod,
       "rsBWMStatisticsNewUDPConnectionsLastSec": rsBWMStatisticsNewUDPConnectionsLastSec,
       "rsBWMStatisticsNewUDPConnectionsLastPeriod": rsBWMStatisticsNewUDPConnectionsLastPeriod,
       "rsBWMStatisticsQueuedBWLastSec": rsBWMStatisticsQueuedBWLastSec,
       "rsBWMStatisticsQueuedBWLastPeriod": rsBWMStatisticsQueuedBWLastPeriod,
       "rsBWMStatisticsMonitorPolicy": rsBWMStatisticsMonitorPolicy,
       "rsBWMStatisticsTableUseSRP": rsBWMStatisticsTableUseSRP,
       "rsBWMStatisticsReportingPeriod": rsBWMStatisticsReportingPeriod,
       "rsBWMSamplingRatio": rsBWMSamplingRatio,
       "rsBWMSamplerOverloadMode": rsBWMSamplerOverloadMode,
       "rsBWMChainRulesTable": rsBWMChainRulesTable,
       "rsBWMChainRulesEntry": rsBWMChainRulesEntry,
       "rsBWMChainRulesIndex": rsBWMChainRulesIndex,
       "rsBWMChainRulesName": rsBWMChainRulesName,
       "rsBWMChainRulesDestination": rsBWMChainRulesDestination,
       "rsBWMChainRulesSource": rsBWMChainRulesSource,
       "rsBWMChainRulesStatus": rsBWMChainRulesStatus,
       "rsBWMChainRulesDirection": rsBWMChainRulesDirection,
       "rsBWMChainRulesDescription": rsBWMChainRulesDescription,
       "rsBWMChainRulesPolicyType": rsBWMChainRulesPolicyType,
       "rsBWMChainRulesPolicy": rsBWMChainRulesPolicy,
       "rsBWMChainRulesOperationalStatus": rsBWMChainRulesOperationalStatus,
       "rsBWMChainRulesSpecific": rsBWMChainRulesSpecific,
       "rsBWMChainRulesPhysicalPortGroup": rsBWMChainRulesPhysicalPortGroup,
       "rsBWMChainRulesVLANTagGroup": rsBWMChainRulesVLANTagGroup,
       "rsBWMChainRulesDSCPMarking": rsBWMChainRulesDSCPMarking,
       "rsBWMChainRulesRadiusRule": rsBWMChainRulesRadiusRule,
       "rsBWMCurrentChainRulesTable": rsBWMCurrentChainRulesTable,
       "rsBWMCurrentChainRulesEntry": rsBWMCurrentChainRulesEntry,
       "rsBWMCurrentChainRulesIndex": rsBWMCurrentChainRulesIndex,
       "rsBWMCurrentChainRulesName": rsBWMCurrentChainRulesName,
       "rsBWMCurrentChainRulesDestination": rsBWMCurrentChainRulesDestination,
       "rsBWMCurrentChainRulesSource": rsBWMCurrentChainRulesSource,
       "rsBWMCurrentChainRulesDirection": rsBWMCurrentChainRulesDirection,
       "rsBWMCurrentChainRulesDescription": rsBWMCurrentChainRulesDescription,
       "rsBWMCurrentChainRulesPolicyType": rsBWMCurrentChainRulesPolicyType,
       "rsBWMCurrentChainRulesPolicy": rsBWMCurrentChainRulesPolicy,
       "rsBWMCurrentChainRulesSpecific": rsBWMCurrentChainRulesSpecific,
       "rsBWMCurrentChainBandwidthLastSec": rsBWMCurrentChainBandwidthLastSec,
       "rsBWMCurrentChainPacketsLastSec": rsBWMCurrentChainPacketsLastSec,
       "rsBWMCurrentChainRulesPhysicalPortGroup": rsBWMCurrentChainRulesPhysicalPortGroup,
       "rsBWMCurrentChainRulesVLANTagGroup": rsBWMCurrentChainRulesVLANTagGroup,
       "rsBWMCurrentChainRulesDSCPMarking": rsBWMCurrentChainRulesDSCPMarking,
       "rsBWMCurrentChainRulesRadiusRule": rsBWMCurrentChainRulesRadiusRule,
       "rsBWMPPCInboundPortOnlyTable": rsBWMPPCInboundPortOnlyTable,
       "rsBWMPPCInboundPortOnlyEntry": rsBWMPPCInboundPortOnlyEntry,
       "rsBWMPPCInboundPort": rsBWMPPCInboundPort,
       "rsBWMPPCOperationStatus": rsBWMPPCOperationStatus,
       "rsBWMPhysicalPortGroupTable": rsBWMPhysicalPortGroupTable,
       "rsBWMPhysicalPortGroupEntry": rsBWMPhysicalPortGroupEntry,
       "rsBWMPhysicalPortGroupName": rsBWMPhysicalPortGroupName,
       "rsBWMPhysicalPortGroupPort": rsBWMPhysicalPortGroupPort,
       "rsBWMPhysicalPortGroupOperationStatus": rsBWMPhysicalPortGroupOperationStatus,
       "rsBWMCurrentPhysicalPortGroupTable": rsBWMCurrentPhysicalPortGroupTable,
       "rsBWMCurrentPhysicalPortGroupEntry": rsBWMCurrentPhysicalPortGroupEntry,
       "rsBWMCurrentPhysicalPortGroupName": rsBWMCurrentPhysicalPortGroupName,
       "rsBWMCurrentPhysicalPortGroupPort": rsBWMCurrentPhysicalPortGroupPort,
       "rsBWMFarmRulesTable": rsBWMFarmRulesTable,
       "rsBWMFarmRulesEntry": rsBWMFarmRulesEntry,
       "rsBWMFarmRulesIndex": rsBWMFarmRulesIndex,
       "rsBWMFarmRulesName": rsBWMFarmRulesName,
       "rsBWMFarmRulesDestination": rsBWMFarmRulesDestination,
       "rsBWMFarmRulesSource": rsBWMFarmRulesSource,
       "rsBWMFarmRulesStatus": rsBWMFarmRulesStatus,
       "rsBWMFarmRulesDirection": rsBWMFarmRulesDirection,
       "rsBWMFarmRulesDescription": rsBWMFarmRulesDescription,
       "rsBWMFarmRulesPolicyType": rsBWMFarmRulesPolicyType,
       "rsBWMFarmRulesPolicy": rsBWMFarmRulesPolicy,
       "rsBWMFarmRulesOperationalStatus": rsBWMFarmRulesOperationalStatus,
       "rsBWMFarmRulesSpecific": rsBWMFarmRulesSpecific,
       "rsBWMFarmRulesPhysicalPortGroup": rsBWMFarmRulesPhysicalPortGroup,
       "rsBWMFarmRulesVLANTagGroup": rsBWMFarmRulesVLANTagGroup,
       "rsBWMFarmRulesDSCPMarking": rsBWMFarmRulesDSCPMarking,
       "rsBWMCurrentFarmRulesTable": rsBWMCurrentFarmRulesTable,
       "rsBWMCurrentFarmRulesEntry": rsBWMCurrentFarmRulesEntry,
       "rsBWMCurrentFarmRulesIndex": rsBWMCurrentFarmRulesIndex,
       "rsBWMCurrentFarmRulesName": rsBWMCurrentFarmRulesName,
       "rsBWMCurrentFarmRulesDestination": rsBWMCurrentFarmRulesDestination,
       "rsBWMCurrentFarmRulesSource": rsBWMCurrentFarmRulesSource,
       "rsBWMCurrentFarmRulesDirection": rsBWMCurrentFarmRulesDirection,
       "rsBWMCurrentFarmRulesDescription": rsBWMCurrentFarmRulesDescription,
       "rsBWMCurrentFarmRulesPolicyType": rsBWMCurrentFarmRulesPolicyType,
       "rsBWMCurrentFarmRulesPolicy": rsBWMCurrentFarmRulesPolicy,
       "rsBWMCurrentFarmRulesSpecific": rsBWMCurrentFarmRulesSpecific,
       "rsBWMCurrentFarmBandwidthLastSec": rsBWMCurrentFarmBandwidthLastSec,
       "rsBWMCurrentFarmPacketsLastSec": rsBWMCurrentFarmPacketsLastSec,
       "rsBWMCurrentFarmRulesPhysicalPortGroup": rsBWMCurrentFarmRulesPhysicalPortGroup,
       "rsBWMCurrentFarmRulesVLANTagGroup": rsBWMCurrentFarmRulesVLANTagGroup,
       "rsBWMCurrentFarmRulesDSCPMarking": rsBWMCurrentFarmRulesDSCPMarking,
       "rsBWMOMPCHashTableOffset": rsBWMOMPCHashTableOffset,
       "rsBWMOMPCHashTableMask": rsBWMOMPCHashTableMask,
       "rsBWMNoSaveMode": rsBWMNoSaveMode,
       "rsBWMStringSearchMode": rsBWMStringSearchMode,
       "rsBWMVLANTagGroupTable": rsBWMVLANTagGroupTable,
       "rsBWMVLANTagGroupEntry": rsBWMVLANTagGroupEntry,
       "rsBWMVLANTagGroupName": rsBWMVLANTagGroupName,
       "rsBWMVLANTagGroupVLANTag": rsBWMVLANTagGroupVLANTag,
       "rsBWMVLANTagGroupVLANTagFrom": rsBWMVLANTagGroupVLANTagFrom,
       "rsBWMVLANTagGroupVLANTagTo": rsBWMVLANTagGroupVLANTagTo,
       "rsBWMVLANTagGroupMode": rsBWMVLANTagGroupMode,
       "rsBWMVLANTagGroupStatus": rsBWMVLANTagGroupStatus,
       "rsBWMCurrentVLANTagGroupTable": rsBWMCurrentVLANTagGroupTable,
       "rsBWMCurrentVLANTagGroupEntry": rsBWMCurrentVLANTagGroupEntry,
       "rsBWMCurrentVLANTagGroupName": rsBWMCurrentVLANTagGroupName,
       "rsBWMCurrentVLANTagGroupVLANTag": rsBWMCurrentVLANTagGroupVLANTag,
       "rsBWMCurrentVLANTagGroupVLANTagFrom": rsBWMCurrentVLANTagGroupVLANTagFrom,
       "rsBWMCurrentVLANTagGroupVLANTagTo": rsBWMCurrentVLANTagGroupVLANTagTo,
       "rsBWMCurrentVLANTagGroupMode": rsBWMCurrentVLANTagGroupMode,
       "rsBWMMacGroupTable": rsBWMMacGroupTable,
       "rsBWMMacGroupEntry": rsBWMMacGroupEntry,
       "rsBWMMacGroupEntryName": rsBWMMacGroupEntryName,
       "rsBWMMacGroupEntryAddress": rsBWMMacGroupEntryAddress,
       "rsBWMMacGroupEntryStatus": rsBWMMacGroupEntryStatus,
       "rsBWMMacGroupCurrentTable": rsBWMMacGroupCurrentTable,
       "rsBWMMacGroupCurrentEntry": rsBWMMacGroupCurrentEntry,
       "rsBWMMacGroupCurrentEntryName": rsBWMMacGroupCurrentEntryName,
       "rsBWMMacGroupCurrentEntryAddress": rsBWMMacGroupCurrentEntryAddress,
       "rsBWMQueueSize": rsBWMQueueSize,
       "rsBWMTrafficFlowBWAgingTime": rsBWMTrafficFlowBWAgingTime,
       "rsBWMServiceTable": rsBWMServiceTable,
       "rsBWMServiceEntry": rsBWMServiceEntry,
       "rsBWMServiceTableType": rsBWMServiceTableType,
       "rsBWMServiceType": rsBWMServiceType,
       "rsBWMServiceName": rsBWMServiceName,
       "rsBWMPolicyGroupTable": rsBWMPolicyGroupTable,
       "rsBWMPolicyGroupEntry": rsBWMPolicyGroupEntry,
       "rsBWMPolicyGroupEntryName": rsBWMPolicyGroupEntryName,
       "rsBWMPolicyGroupEntryStatus": rsBWMPolicyGroupEntryStatus,
       "rsBWMPolicyGroupCurrentTable": rsBWMPolicyGroupCurrentTable,
       "rsBWMPolicyGroupCurrentEntry": rsBWMPolicyGroupCurrentEntry,
       "rsBWMPolicyGroupCurrentEntryName": rsBWMPolicyGroupCurrentEntryName,
       "rsBWMAppPortGroupEntryTable": rsBWMAppPortGroupEntryTable,
       "rsBWMAppPortGroupEntry": rsBWMAppPortGroupEntry,
       "rsBWMAppPortGroupName": rsBWMAppPortGroupName,
       "rsBWMAppPortGroupFromPort": rsBWMAppPortGroupFromPort,
       "rsBWMAppPortGroupToPort": rsBWMAppPortGroupToPort,
       "rsBWMAppPortGroupType": rsBWMAppPortGroupType,
       "rsBWMAppPortGroupStatus": rsBWMAppPortGroupStatus,
       "rsBWMCurrentAppPortGroupEntryTable": rsBWMCurrentAppPortGroupEntryTable,
       "rsBWMCurrentAppPortGroupEntry": rsBWMCurrentAppPortGroupEntry,
       "rsBWMCurrentAppPortGroupName": rsBWMCurrentAppPortGroupName,
       "rsBWMCurrentAppPortGroupFromPort": rsBWMCurrentAppPortGroupFromPort,
       "rsBWMCurrentAppPortGroupToPort": rsBWMCurrentAppPortGroupToPort,
       "rsBWMCurrentAppPortGroupType": rsBWMCurrentAppPortGroupType,
       "rsBWMDefaultGatewayClassificatiomMode": rsBWMDefaultGatewayClassificatiomMode,
       "rsBWMExtRulesTable": rsBWMExtRulesTable,
       "rsBWMExtRulesEntry": rsBWMExtRulesEntry,
       "rsBWMExtRulesName": rsBWMExtRulesName,
       "rsBWMExtRulesFromFarm": rsBWMExtRulesFromFarm,
       "rsBWMExtRulesToFarm": rsBWMExtRulesToFarm,
       "rsBWMExtRulesClassificationPoint": rsBWMExtRulesClassificationPoint,
       "rsBWMExtRulesTrafficIdentification": rsBWMExtRulesTrafficIdentification,
       "rsBWMExtRulesTrafficFlowMaxBW": rsBWMExtRulesTrafficFlowMaxBW,
       "rsBWMExtRulesMaxConcurrentSessions": rsBWMExtRulesMaxConcurrentSessions,
       "rsBWMExtRulesMaxRqstsPerSec": rsBWMExtRulesMaxRqstsPerSec,
       "rsBWMExtRulesTrafficIDCookieField": rsBWMExtRulesTrafficIDCookieField,
       "rsBWMExtRulesStatus": rsBWMExtRulesStatus,
       "rsBWMExtRulesActivate": rsBWMExtRulesActivate,
       "rsBWMExtRulesInactivate": rsBWMExtRulesInactivate,
       "rsBWMExtRulesForceBestFit": rsBWMExtRulesForceBestFit,
       "rsBWMExtRulesPacketMarkingType": rsBWMExtRulesPacketMarkingType,
       "rsBWMExtRulesPacketMarkingValue": rsBWMExtRulesPacketMarkingValue,
       "rsBWMExtRulesReportMaxBw": rsBWMExtRulesReportMaxBw,
       "rsBWMCurrentExtRulesTable": rsBWMCurrentExtRulesTable,
       "rsBWMCurrentExtRulesEntry": rsBWMCurrentExtRulesEntry,
       "rsBWMCurrentExtRulesName": rsBWMCurrentExtRulesName,
       "rsBWMCurrentExtRulesFromFarm": rsBWMCurrentExtRulesFromFarm,
       "rsBWMCurrentExtRulesToFarm": rsBWMCurrentExtRulesToFarm,
       "rsBWMCurrentExtRulesClassificationPoint": rsBWMCurrentExtRulesClassificationPoint,
       "rsBWMCurrentExtRulesTrafficIdentification": rsBWMCurrentExtRulesTrafficIdentification,
       "rsBWMCurrentExtRulesTrafficFlowMaxBW": rsBWMCurrentExtRulesTrafficFlowMaxBW,
       "rsBWMCurrentExtRulesMaxConcurrentSessions": rsBWMCurrentExtRulesMaxConcurrentSessions,
       "rsBWMCurrentExtRulesMaxRqstsPerSec": rsBWMCurrentExtRulesMaxRqstsPerSec,
       "rsBWMCurrentExtRulesTrafficIDCookieField": rsBWMCurrentExtRulesTrafficIDCookieField,
       "rsBWMCurrentExtRulesActivate": rsBWMCurrentExtRulesActivate,
       "rsBWMCurrentExtRulesInactivate": rsBWMCurrentExtRulesInactivate,
       "rsBWMCurrentExtRulesForceBestFit": rsBWMCurrentExtRulesForceBestFit,
       "rsBWMCurrentExtRulesPacketMarkingType": rsBWMCurrentExtRulesPacketMarkingType,
       "rsBWMCurrentExtRulesPacketMarkingValue": rsBWMCurrentExtRulesPacketMarkingValue,
       "rsBWMCurrentExtRulesReportMaxBw": rsBWMCurrentExtRulesReportMaxBw,
       "rsBWMRulesTreeManager": rsBWMRulesTreeManager,
       "rsBWMRulesTreeName": rsBWMRulesTreeName,
       "rsBWMRulesTreeNewParentName": rsBWMRulesTreeNewParentName,
       "rsBWMRulesTreeAction": rsBWMRulesTreeAction,
       "rsBWMTCPSessionClassification": rsBWMTCPSessionClassification,
       "rsBWMNetworkTable": rsBWMNetworkTable,
       "rsBWMNetworkEntry": rsBWMNetworkEntry,
       "rsBWMNetworkName": rsBWMNetworkName,
       "rsBWMNetworkSubIndex": rsBWMNetworkSubIndex,
       "rsBWMNetworkAddress": rsBWMNetworkAddress,
       "rsBWMNetworkMask": rsBWMNetworkMask,
       "rsBWMNetworkFromIP": rsBWMNetworkFromIP,
       "rsBWMNetworkToIP": rsBWMNetworkToIP,
       "rsBWMNetworkMode": rsBWMNetworkMode,
       "rsBWMNetworkStatus": rsBWMNetworkStatus,
       "rsBWMCurrentNetworkTable": rsBWMCurrentNetworkTable,
       "rsBWMCurrentNetworkEntry": rsBWMCurrentNetworkEntry,
       "rsBWMCurrentNetworkName": rsBWMCurrentNetworkName,
       "rsBWMCurrentNetworkSubIndex": rsBWMCurrentNetworkSubIndex,
       "rsBWMCurrentNetworkAddress": rsBWMCurrentNetworkAddress,
       "rsBWMCurrentNetworkMask": rsBWMCurrentNetworkMask,
       "rsBWMCurrentNetworkFromIP": rsBWMCurrentNetworkFromIP,
       "rsBWMCurrentNetworkToIP": rsBWMCurrentNetworkToIP,
       "rsBWMCurrentNetworkMode": rsBWMCurrentNetworkMode,
       "rsBWMStatisticsNewTable": rsBWMStatisticsNewTable,
       "rsBWMStatisticsNewEntry": rsBWMStatisticsNewEntry,
       "rsBWMStatisticsPolicyKey": rsBWMStatisticsPolicyKey,
       "rsBWMStatisticsPolicyNameSec": rsBWMStatisticsPolicyNameSec,
       "rsBWMStatisticsBandwidthUsedSecond": rsBWMStatisticsBandwidthUsedSecond,
       "rsBWMStatisticsPacketNumberSecond": rsBWMStatisticsPacketNumberSecond,
       "rsBWMStatisticsGuaranteedReachedSecond": rsBWMStatisticsGuaranteedReachedSecond,
       "rsBWMStatisticsMaximumReachedSecond": rsBWMStatisticsMaximumReachedSecond,
       "rsBWMStatisticsMatchedBandwidthSecond": rsBWMStatisticsMatchedBandwidthSecond,
       "rsBWMStatisticsInboundBandwidthUsedSecond": rsBWMStatisticsInboundBandwidthUsedSecond,
       "rsBWMStatisticsInboundMatchedBandwidthSecond": rsBWMStatisticsInboundMatchedBandwidthSecond,
       "rsBWMStatisticsInboundPacketNumberSecond": rsBWMStatisticsInboundPacketNumberSecond,
       "rsBWMStatisticsOutboundBandwidthUsedSecond": rsBWMStatisticsOutboundBandwidthUsedSecond,
       "rsBWMStatisticsOutboundMatchedBandwidthSecond": rsBWMStatisticsOutboundMatchedBandwidthSecond,
       "rsBWMStatisticsOutboundPacketNumberSecond": rsBWMStatisticsOutboundPacketNumberSecond,
       "rsBWMStatisticsNewTCPConnectionsSecond": rsBWMStatisticsNewTCPConnectionsSecond,
       "rsBWMStatisticsNewUDPConnectionsSecond": rsBWMStatisticsNewUDPConnectionsSecond,
       "rsBWMStatisticsQueuedBWSecond": rsBWMStatisticsQueuedBWSecond,
       "rsBWMStatisticsBandwidthUsedPeriod": rsBWMStatisticsBandwidthUsedPeriod,
       "rsBWMStatisticsPeakBandwidthPeriod": rsBWMStatisticsPeakBandwidthPeriod,
       "rsBWMStatisticsPacketNumberPeriod": rsBWMStatisticsPacketNumberPeriod,
       "rsBWMStatisticsGuaranteedReachedCounterPeriod": rsBWMStatisticsGuaranteedReachedCounterPeriod,
       "rsBWMStatisticsMaximumReachedCounterPeriod": rsBWMStatisticsMaximumReachedCounterPeriod,
       "rsBWMStatisticsMatchedBandwidthPeriod": rsBWMStatisticsMatchedBandwidthPeriod,
       "rsBWMStatisticsInboundBandwidthUsedPeriod": rsBWMStatisticsInboundBandwidthUsedPeriod,
       "rsBWMStatisticsInboundMatchedBandwidthPeriod": rsBWMStatisticsInboundMatchedBandwidthPeriod,
       "rsBWMStatisticsInboundPacketNumberPeriod": rsBWMStatisticsInboundPacketNumberPeriod,
       "rsBWMStatisticsOutboundBandwidthUsedPeriod": rsBWMStatisticsOutboundBandwidthUsedPeriod,
       "rsBWMStatisticsOutboundMatchedBandwidthPeriod": rsBWMStatisticsOutboundMatchedBandwidthPeriod,
       "rsBWMStatisticsOutboundPacketNumberPeriod": rsBWMStatisticsOutboundPacketNumberPeriod,
       "rsBWMStatisticsNewTCPConnectionsPeriod": rsBWMStatisticsNewTCPConnectionsPeriod,
       "rsBWMStatisticsNewUDPConnectionsPeriod": rsBWMStatisticsNewUDPConnectionsPeriod,
       "rsBWMStatisticsQueuedBWPeriod": rsBWMStatisticsQueuedBWPeriod,
       "rsBWMPoliciesTable": rsBWMPoliciesTable,
       "rsBWMPolicyEntry": rsBWMPolicyEntry,
       "rsBWMPolicyKey": rsBWMPolicyKey,
       "rsBWMPolicyName": rsBWMPolicyName,
       "rsBWMPolicyIndex": rsBWMPolicyIndex,
       "rsBWMPolicyDestination": rsBWMPolicyDestination,
       "rsBWMPolicySource": rsBWMPolicySource,
       "rsBWMPolicyAction": rsBWMPolicyAction,
       "rsBWMPolicyDirection": rsBWMPolicyDirection,
       "rsBWMPolicyPriority": rsBWMPolicyPriority,
       "rsBWMPolicyType": rsBWMPolicyType,
       "rsBWMPolicyDescription": rsBWMPolicyDescription,
       "rsBWMPolicyGuaranteedBW": rsBWMPolicyGuaranteedBW,
       "rsBWMPolicyFilterType": rsBWMPolicyFilterType,
       "rsBWMPolicyFilter": rsBWMPolicyFilter,
       "rsBWMPolicyOperationalStatus": rsBWMPolicyOperationalStatus,
       "rsBWMPolicyReportBlockedPackets": rsBWMPolicyReportBlockedPackets,
       "rsBWMPolicyMaxBW": rsBWMPolicyMaxBW,
       "rsBWMPolicyPhysicalPortGroup": rsBWMPolicyPhysicalPortGroup,
       "rsBWMPolicyVLANTagGroup": rsBWMPolicyVLANTagGroup,
       "rsBWMPolicySpecific": rsBWMPolicySpecific,
       "rsBWMPolicyStatus": rsBWMPolicyStatus,
       "rsBWMPolicyRadiusRule": rsBWMPolicyRadiusRule,
       "rsBWMCurrentPoliciesTable": rsBWMCurrentPoliciesTable,
       "rsBWMCurrentPolicyEntry": rsBWMCurrentPolicyEntry,
       "rsBWMCurrentPolicyKey": rsBWMCurrentPolicyKey,
       "rsBWMCurrentPolicyName": rsBWMCurrentPolicyName,
       "rsBWMCurrentPolicyIndex": rsBWMCurrentPolicyIndex,
       "rsBWMCurrentPolicyDestination": rsBWMCurrentPolicyDestination,
       "rsBWMCurrentPolicySource": rsBWMCurrentPolicySource,
       "rsBWMCurrentPolicyAction": rsBWMCurrentPolicyAction,
       "rsBWMCurrentPolicyDirection": rsBWMCurrentPolicyDirection,
       "rsBWMCurrentPolicyPriority": rsBWMCurrentPolicyPriority,
       "rsBWMCurrentPolicyType": rsBWMCurrentPolicyType,
       "rsBWMCurrentPolicyDescription": rsBWMCurrentPolicyDescription,
       "rsBWMCurrentPolicyGuaranteedBW": rsBWMCurrentPolicyGuaranteedBW,
       "rsBWMCurrentPolicyFilterType": rsBWMCurrentPolicyFilterType,
       "rsBWMCurrentPolicyFilter": rsBWMCurrentPolicyFilter,
       "rsBWMCurrentPolicyReportBlockedPackets": rsBWMCurrentPolicyReportBlockedPackets,
       "rsBWMCurrentPolicyMaxBW": rsBWMCurrentPolicyMaxBW,
       "rsBWMCurrentPolicyPhysicalPortGroup": rsBWMCurrentPolicyPhysicalPortGroup,
       "rsBWMCurrentPolicyVLANTagGroup": rsBWMCurrentPolicyVLANTagGroup,
       "rsBWMCurrentPolicySpecific": rsBWMCurrentPolicySpecific,
       "rsBWMCurrentPolicyRadiusRule": rsBWMCurrentPolicyRadiusRule,
       "rsBWMExtPoliciesTable": rsBWMExtPoliciesTable,
       "rsBWMExtPolicyEntry": rsBWMExtPolicyEntry,
       "rsBWMExtPolicyKey": rsBWMExtPolicyKey,
       "rsBWMExtPolicyName": rsBWMExtPolicyName,
       "rsBWMExtPolicyFromFarm": rsBWMExtPolicyFromFarm,
       "rsBWMExtPolicyToFarm": rsBWMExtPolicyToFarm,
       "rsBWMExtPolicyClassificationPoint": rsBWMExtPolicyClassificationPoint,
       "rsBWMExtPolicyTrafficIdentification": rsBWMExtPolicyTrafficIdentification,
       "rsBWMExtPolicyTrafficFlowMaxBW": rsBWMExtPolicyTrafficFlowMaxBW,
       "rsBWMExtPolicyMaxConcurrentSessions": rsBWMExtPolicyMaxConcurrentSessions,
       "rsBWMExtPolicyMaxRqstsPerSec": rsBWMExtPolicyMaxRqstsPerSec,
       "rsBWMExtPolicyTrafficIDCookieField": rsBWMExtPolicyTrafficIDCookieField,
       "rsBWMExtPolicyStatus": rsBWMExtPolicyStatus,
       "rsBWMExtPolicyActivate": rsBWMExtPolicyActivate,
       "rsBWMExtPolicyInactivate": rsBWMExtPolicyInactivate,
       "rsBWMExtPolicyForceBestFit": rsBWMExtPolicyForceBestFit,
       "rsBWMExtPolicyPacketMarkingType": rsBWMExtPolicyPacketMarkingType,
       "rsBWMExtPolicyPacketMarkingValue": rsBWMExtPolicyPacketMarkingValue,
       "rsBWMExtPolicyReportMaxBw": rsBWMExtPolicyReportMaxBw,
       "rsBWMCurrentExtPoliciesTable": rsBWMCurrentExtPoliciesTable,
       "rsBWMCurrentExtPolicyEntry": rsBWMCurrentExtPolicyEntry,
       "rsBWMCurrentExtPolicyKey": rsBWMCurrentExtPolicyKey,
       "rsBWMCurrentExtPolicyName": rsBWMCurrentExtPolicyName,
       "rsBWMCurrentExtPolicyFromFarm": rsBWMCurrentExtPolicyFromFarm,
       "rsBWMCurrentExtPolicyToFarm": rsBWMCurrentExtPolicyToFarm,
       "rsBWMCurrentExtPolicyClassificationPoint": rsBWMCurrentExtPolicyClassificationPoint,
       "rsBWMCurrentExtPolicyTrafficIdentification": rsBWMCurrentExtPolicyTrafficIdentification,
       "rsBWMCurrentExtPolicyTrafficFlowMaxBW": rsBWMCurrentExtPolicyTrafficFlowMaxBW,
       "rsBWMCurrentExtPolicyMaxConcurrentSessions": rsBWMCurrentExtPolicyMaxConcurrentSessions,
       "rsBWMCurrentExtPolicyMaxRqstsPerSec": rsBWMCurrentExtPolicyMaxRqstsPerSec,
       "rsBWMCurrentExtPolicyTrafficIDCookieField": rsBWMCurrentExtPolicyTrafficIDCookieField,
       "rsBWMCurrentExtPolicyActivate": rsBWMCurrentExtPolicyActivate,
       "rsBWMCurrentExtPolicyInactivate": rsBWMCurrentExtPolicyInactivate,
       "rsBWMCurrentExtPolicyForceBestFit": rsBWMCurrentExtPolicyForceBestFit,
       "rsBWMCurrentExtPolicyPacketMarkingType": rsBWMCurrentExtPolicyPacketMarkingType,
       "rsBWMCurrentExtPolicyPacketMarkingValue": rsBWMCurrentExtPolicyPacketMarkingValue,
       "rsBWMCurrentExtPolicyReportMaxBw": rsBWMCurrentExtPolicyReportMaxBw,
       "rsBWMMaxPacketsForClassification": rsBWMMaxPacketsForClassification,
       "rsBWMACL": rsBWMACL,
       "rsBWMACLModifyPoliciesTable": rsBWMACLModifyPoliciesTable,
       "rsBWMACLModifyPolicyEntry": rsBWMACLModifyPolicyEntry,
       "rsBWMACLModifyPolicyName": rsBWMACLModifyPolicyName,
       "rsBWMACLModifyPolicyIndex": rsBWMACLModifyPolicyIndex,
       "rsBWMACLModifyPolicyDescription": rsBWMACLModifyPolicyDescription,
       "rsBWMACLModifyPolicyDestination": rsBWMACLModifyPolicyDestination,
       "rsBWMACLModifyPolicySource": rsBWMACLModifyPolicySource,
       "rsBWMACLModifyPolicyService": rsBWMACLModifyPolicyService,
       "rsBWMACLModifyPolicyVLANTagGroup": rsBWMACLModifyPolicyVLANTagGroup,
       "rsBWMACLModifyPolicyPortGroup": rsBWMACLModifyPolicyPortGroup,
       "rsBWMACLModifyPolicyActivate": rsBWMACLModifyPolicyActivate,
       "rsBWMACLModifyPolicyInactivate": rsBWMACLModifyPolicyInactivate,
       "rsBWMACLModifyPolicyAction": rsBWMACLModifyPolicyAction,
       "rsBWMACLModifyPolicyProtocol": rsBWMACLModifyPolicyProtocol,
       "rsBWMACLModifyPolicyIcmpFlags": rsBWMACLModifyPolicyIcmpFlags,
       "rsBWMACLModifyPolicyClassificationPoint": rsBWMACLModifyPolicyClassificationPoint,
       "rsBWMACLModifyPolicyOperationalStatus": rsBWMACLModifyPolicyOperationalStatus,
       "rsBWMACLModifyPolicyStatus": rsBWMACLModifyPolicyStatus,
       "rsBWMACLModifyPolicyPacketReportStatus": rsBWMACLModifyPolicyPacketReportStatus,
       "rsBWMACLActualPoliciesTable": rsBWMACLActualPoliciesTable,
       "rsBWMACLActualPolicyEntry": rsBWMACLActualPolicyEntry,
       "rsBWMACLActualPolicyName": rsBWMACLActualPolicyName,
       "rsBWMACLActualPolicyIndex": rsBWMACLActualPolicyIndex,
       "rsBWMACLActualPolicyDescription": rsBWMACLActualPolicyDescription,
       "rsBWMACLActualPolicyDestination": rsBWMACLActualPolicyDestination,
       "rsBWMACLActualPolicySource": rsBWMACLActualPolicySource,
       "rsBWMACLActualPolicyService": rsBWMACLActualPolicyService,
       "rsBWMACLActualPolicyVLANTagGroup": rsBWMACLActualPolicyVLANTagGroup,
       "rsBWMACLActualPolicyPortGroup": rsBWMACLActualPolicyPortGroup,
       "rsBWMACLActualPolicyActivate": rsBWMACLActualPolicyActivate,
       "rsBWMACLActualPolicyInactivate": rsBWMACLActualPolicyInactivate,
       "rsBWMACLActualPolicyAction": rsBWMACLActualPolicyAction,
       "rsBWMACLActualPolicyProtocol": rsBWMACLActualPolicyProtocol,
       "rsBWMACLActualPolicyIcmpFlags": rsBWMACLActualPolicyIcmpFlags,
       "rsBWMACLActualPolicyClassificationPoint": rsBWMACLActualPolicyClassificationPoint,
       "rsBWMACLActualPolicyOperationalStatus": rsBWMACLActualPolicyOperationalStatus,
       "rsBWMACLActualPolicyPacketReportStatus": rsBWMACLActualPolicyPacketReportStatus,
       "rsBWMACLStatus": rsBWMACLStatus,
       "rsBWMACLLearningPeriod": rsBWMACLLearningPeriod,
       "rsBWMACLTCPHandshakeTimeout": rsBWMACLTCPHandshakeTimeout,
       "rsBWMACLTCPEstablishedTimeout": rsBWMACLTCPEstablishedTimeout,
       "rsBWMACLTCPFinTimeout": rsBWMACLTCPFinTimeout,
       "rsBWMACLTCPRstTimeout": rsBWMACLTCPRstTimeout,
       "rsBWMACLTCPMidSessMode": rsBWMACLTCPMidSessMode,
       "rsBWMACLTCPRstValidationMode": rsBWMACLTCPRstValidationMode,
       "rsBWMACLUDPTimeout": rsBWMACLUDPTimeout,
       "rsBWMACLICMPTimeout": rsBWMACLICMPTimeout,
       "rsBWMACLOtherTimeout": rsBWMACLOtherTimeout,
       "rsBWMACLSummaryReportsTable": rsBWMACLSummaryReportsTable,
       "rsBWMACLSummaryReportsEntry": rsBWMACLSummaryReportsEntry,
       "rsBWMACLSummaryReportsPolicyName": rsBWMACLSummaryReportsPolicyName,
       "rsBWMACLSummaryReportsTCPAllow": rsBWMACLSummaryReportsTCPAllow,
       "rsBWMACLSummaryReportsTCPDrop": rsBWMACLSummaryReportsTCPDrop,
       "rsBWMACLSummaryReportsUDPAllow": rsBWMACLSummaryReportsUDPAllow,
       "rsBWMACLSummaryReportsUDPDrop": rsBWMACLSummaryReportsUDPDrop,
       "rsBWMACLSummaryReportsICMPAllow": rsBWMACLSummaryReportsICMPAllow,
       "rsBWMACLSummaryReportsICMPDrop": rsBWMACLSummaryReportsICMPDrop,
       "rsBWMACLSummaryReportsOtherAllow": rsBWMACLSummaryReportsOtherAllow,
       "rsBWMACLSummaryReportsOtherDrop": rsBWMACLSummaryReportsOtherDrop,
       "rsBWMACLSummaryReportsTCPMidSess": rsBWMACLSummaryReportsTCPMidSess,
       "rsBWMACLSummaryReportsTCPRstInvalid": rsBWMACLSummaryReportsTCPRstInvalid,
       "rsBWMACLSummaryReportsTCPHandshakeViolation": rsBWMACLSummaryReportsTCPHandshakeViolation,
       "rsBWMACLSummaryReportsICMPSmurf": rsBWMACLSummaryReportsICMPSmurf,
       "rsBWMACLSummaryReportsICMPPacketAnomaly": rsBWMACLSummaryReportsICMPPacketAnomaly,
       "rsBWMACLSummaryReportsGREAllow": rsBWMACLSummaryReportsGREAllow,
       "rsBWMACLSummaryReportsGREDrop": rsBWMACLSummaryReportsGREDrop,
       "rsBWMACLSummaryReportsSCTPAllow": rsBWMACLSummaryReportsSCTPAllow,
       "rsBWMACLSummaryReportsSCTPDrop": rsBWMACLSummaryReportsSCTPDrop,
       "rsBWMACLSummaryReportsL2TPAllow": rsBWMACLSummaryReportsL2TPAllow,
       "rsBWMACLSummaryReportsL2TPDrop": rsBWMACLSummaryReportsL2TPDrop,
       "rsBWMACLSummaryReportsGTPAllow": rsBWMACLSummaryReportsGTPAllow,
       "rsBWMACLSummaryReportsGTPDrop": rsBWMACLSummaryReportsGTPDrop,
       "rsBWMACLSummaryReportsIPinIPAllow": rsBWMACLSummaryReportsIPinIPAllow,
       "rsBWMACLSummaryReportsIPinIPDrop": rsBWMACLSummaryReportsIPinIPDrop,
       "rsBWMACLReportMaxTraps": rsBWMACLReportMaxTraps,
       "rsBWMACLReportPeriod": rsBWMACLReportPeriod,
       "rsBWMACLReportSendSrp": rsBWMACLReportSendSrp,
       "rsBWMACLDetailedReportType": rsBWMACLDetailedReportType,
       "rsBWMACLGRETimeout": rsBWMACLGRETimeout,
       "rsBWMACLSCTPTimeout": rsBWMACLSCTPTimeout,
       "rsBWMACLAllowICMPSmurf": rsBWMACLAllowICMPSmurf,
       "rsBWMACLL2TPTimeout": rsBWMACLL2TPTimeout,
       "rsBWMACLGTPTimeout": rsBWMACLGTPTimeout,
       "rsBWMACLPacketTraceStatus": rsBWMACLPacketTraceStatus,
       "rsBWMACLIPinIPTimeout": rsBWMACLIPinIPTimeout,
       "rsBWMACLDefaultAction": rsBWMACLDefaultAction,
       "rsBWMSecGroupTable": rsBWMSecGroupTable,
       "rsBWMModifySecGrpTag": rsBWMModifySecGrpTag,
       "rsBWMSecGroupEntryName": rsBWMSecGroupEntryName,
       "rsBWMSecGroupEntryValue": rsBWMSecGroupEntryValue,
       "rsBWMSecGroupEntryStatus": rsBWMSecGroupEntryStatus,
       "rsBWMSecGroupEntryRowStatus": rsBWMSecGroupEntryRowStatus,
       "rsBWMSecGroupCurrentTable": rsBWMSecGroupCurrentTable,
       "rsBWMActiveSecGrpTag": rsBWMActiveSecGrpTag,
       "rsBWMSecGroupActiveEntryName": rsBWMSecGroupActiveEntryName,
       "rsBWMSecGroupEntryActiveValue": rsBWMSecGroupEntryActiveValue}
)
