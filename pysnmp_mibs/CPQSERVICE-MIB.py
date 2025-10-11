# SNMP MIB module (CPQSERVICE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/hp/CPQSERVICE-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:39:04 2025
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

(compaq,) = mibBuilder.importSymbols(
    "CPQHOST-MIB",
    "compaq")

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
 NotificationType,
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
    "NotificationType",
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


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CpqService_ObjectIdentity = ObjectIdentity
cpqService = _CpqService_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 164)
)
_CpqServiceMibRev_ObjectIdentity = ObjectIdentity
cpqServiceMibRev = _CpqServiceMibRev_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 164, 1)
)


class _CpqServiceMibRevMinor_Type(Integer32):
    """Custom type cpqServiceMibRevMinor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CpqServiceMibRevMinor_Type.__name__ = "Integer32"
_CpqServiceMibRevMinor_Object = MibScalar
cpqServiceMibRevMinor = _CpqServiceMibRevMinor_Object(
    (1, 3, 6, 1, 4, 1, 232, 164, 1, 1),
    _CpqServiceMibRevMinor_Type()
)
cpqServiceMibRevMinor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqServiceMibRevMinor.setStatus("mandatory")


class _CpqServiceMibRevMajor_Type(Integer32):
    """Custom type cpqServiceMibRevMajor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CpqServiceMibRevMajor_Type.__name__ = "Integer32"
_CpqServiceMibRevMajor_Object = MibScalar
cpqServiceMibRevMajor = _CpqServiceMibRevMajor_Object(
    (1, 3, 6, 1, 4, 1, 232, 164, 1, 2),
    _CpqServiceMibRevMajor_Type()
)
cpqServiceMibRevMajor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqServiceMibRevMajor.setStatus("mandatory")
_CpqServiceIncident_ObjectIdentity = ObjectIdentity
cpqServiceIncident = _CpqServiceIncident_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 164, 2)
)


class _CpqServiceIncidentSeverity_Type(Integer32):
    """Custom type cpqServiceIncidentSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("important", 1),
          ("informational", 2))
    )


_CpqServiceIncidentSeverity_Type.__name__ = "Integer32"
_CpqServiceIncidentSeverity_Object = MibScalar
cpqServiceIncidentSeverity = _CpqServiceIncidentSeverity_Object(
    (1, 3, 6, 1, 4, 1, 232, 164, 2, 1),
    _CpqServiceIncidentSeverity_Type()
)
cpqServiceIncidentSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqServiceIncidentSeverity.setStatus("deprecated")


class _CpqServiceIncidentStatus_Type(Integer32):
    """Custom type cpqServiceIncidentStatus based on Integer32"""
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
        *(("other", 1),
          ("intransit", 2),
          ("delivered", 3),
          ("undelivered", 4),
          ("assigned", 5),
          ("closed", 6),
          ("submitted_to_ISEE", 7))
    )


_CpqServiceIncidentStatus_Type.__name__ = "Integer32"
_CpqServiceIncidentStatus_Object = MibScalar
cpqServiceIncidentStatus = _CpqServiceIncidentStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 164, 2, 2),
    _CpqServiceIncidentStatus_Type()
)
cpqServiceIncidentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqServiceIncidentStatus.setStatus("mandatory")


class _CpqServiceIncidentInformation_Type(DisplayString):
    """Custom type cpqServiceIncidentInformation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqServiceIncidentInformation_Type.__name__ = "DisplayString"
_CpqServiceIncidentInformation_Object = MibScalar
cpqServiceIncidentInformation = _CpqServiceIncidentInformation_Object(
    (1, 3, 6, 1, 4, 1, 232, 164, 2, 3),
    _CpqServiceIncidentInformation_Type()
)
cpqServiceIncidentInformation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqServiceIncidentInformation.setStatus("mandatory")


class _CpqServiceIncidentEvent_Type(DisplayString):
    """Custom type cpqServiceIncidentEvent based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqServiceIncidentEvent_Type.__name__ = "DisplayString"
_CpqServiceIncidentEvent_Object = MibScalar
cpqServiceIncidentEvent = _CpqServiceIncidentEvent_Object(
    (1, 3, 6, 1, 4, 1, 232, 164, 2, 4),
    _CpqServiceIncidentEvent_Type()
)
cpqServiceIncidentEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqServiceIncidentEvent.setStatus("mandatory")


class _CpqServiceIncidentUniqueID_Type(DisplayString):
    """Custom type cpqServiceIncidentUniqueID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqServiceIncidentUniqueID_Type.__name__ = "DisplayString"
_CpqServiceIncidentUniqueID_Object = MibScalar
cpqServiceIncidentUniqueID = _CpqServiceIncidentUniqueID_Object(
    (1, 3, 6, 1, 4, 1, 232, 164, 2, 5),
    _CpqServiceIncidentUniqueID_Type()
)
cpqServiceIncidentUniqueID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqServiceIncidentUniqueID.setStatus("mandatory")


class _CpqServiceIncidentTimeofOriginalEvent_Type(DisplayString):
    """Custom type cpqServiceIncidentTimeofOriginalEvent based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqServiceIncidentTimeofOriginalEvent_Type.__name__ = "DisplayString"
_CpqServiceIncidentTimeofOriginalEvent_Object = MibScalar
cpqServiceIncidentTimeofOriginalEvent = _CpqServiceIncidentTimeofOriginalEvent_Object(
    (1, 3, 6, 1, 4, 1, 232, 164, 2, 6),
    _CpqServiceIncidentTimeofOriginalEvent_Type()
)
cpqServiceIncidentTimeofOriginalEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqServiceIncidentTimeofOriginalEvent.setStatus("mandatory")


class _CpqServiceIncidentSourceSystemName_Type(DisplayString):
    """Custom type cpqServiceIncidentSourceSystemName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqServiceIncidentSourceSystemName_Type.__name__ = "DisplayString"
_CpqServiceIncidentSourceSystemName_Object = MibScalar
cpqServiceIncidentSourceSystemName = _CpqServiceIncidentSourceSystemName_Object(
    (1, 3, 6, 1, 4, 1, 232, 164, 2, 7),
    _CpqServiceIncidentSourceSystemName_Type()
)
cpqServiceIncidentSourceSystemName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqServiceIncidentSourceSystemName.setStatus("mandatory")
_CpqServiceIncidentIPAddessOfSource_Type = IpAddress
_CpqServiceIncidentIPAddessOfSource_Object = MibScalar
cpqServiceIncidentIPAddessOfSource = _CpqServiceIncidentIPAddessOfSource_Object(
    (1, 3, 6, 1, 4, 1, 232, 164, 2, 8),
    _CpqServiceIncidentIPAddessOfSource_Type()
)
cpqServiceIncidentIPAddessOfSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqServiceIncidentIPAddessOfSource.setStatus("mandatory")


class _CpqServiceISEEIncidentInformation_Type(DisplayString):
    """Custom type cpqServiceISEEIncidentInformation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqServiceISEEIncidentInformation_Type.__name__ = "DisplayString"
_CpqServiceISEEIncidentInformation_Object = MibScalar
cpqServiceISEEIncidentInformation = _CpqServiceISEEIncidentInformation_Object(
    (1, 3, 6, 1, 4, 1, 232, 164, 2, 9),
    _CpqServiceISEEIncidentInformation_Type()
)
cpqServiceISEEIncidentInformation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqServiceISEEIncidentInformation.setStatus("mandatory")


class _CpqServiceIncidentIdentifier_Type(DisplayString):
    """Custom type cpqServiceIncidentIdentifier based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqServiceIncidentIdentifier_Type.__name__ = "DisplayString"
_CpqServiceIncidentIdentifier_Object = MibScalar
cpqServiceIncidentIdentifier = _CpqServiceIncidentIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 232, 164, 2, 10),
    _CpqServiceIncidentIdentifier_Type()
)
cpqServiceIncidentIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqServiceIncidentIdentifier.setStatus("mandatory")
_CpqServiceIncidentReceiveTrapOID_Type = ObjectIdentifier
_CpqServiceIncidentReceiveTrapOID_Object = MibScalar
cpqServiceIncidentReceiveTrapOID = _CpqServiceIncidentReceiveTrapOID_Object(
    (1, 3, 6, 1, 4, 1, 232, 164, 2, 11),
    _CpqServiceIncidentReceiveTrapOID_Type()
)
cpqServiceIncidentReceiveTrapOID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqServiceIncidentReceiveTrapOID.setStatus("mandatory")
_CpqServiceIncidentFilterOID_Type = ObjectIdentifier
_CpqServiceIncidentFilterOID_Object = MibScalar
cpqServiceIncidentFilterOID = _CpqServiceIncidentFilterOID_Object(
    (1, 3, 6, 1, 4, 1, 232, 164, 2, 12),
    _CpqServiceIncidentFilterOID_Type()
)
cpqServiceIncidentFilterOID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqServiceIncidentFilterOID.setStatus("deprecated")


class _CpqServiceIncidentFilterValue_Type(DisplayString):
    """Custom type cpqServiceIncidentFilterValue based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqServiceIncidentFilterValue_Type.__name__ = "DisplayString"
_CpqServiceIncidentFilterValue_Object = MibScalar
cpqServiceIncidentFilterValue = _CpqServiceIncidentFilterValue_Object(
    (1, 3, 6, 1, 4, 1, 232, 164, 2, 13),
    _CpqServiceIncidentFilterValue_Type()
)
cpqServiceIncidentFilterValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqServiceIncidentFilterValue.setStatus("deprecated")


class _CpqServiceRecommendedAction1_Type(DisplayString):
    """Custom type cpqServiceRecommendedAction1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqServiceRecommendedAction1_Type.__name__ = "DisplayString"
_CpqServiceRecommendedAction1_Object = MibScalar
cpqServiceRecommendedAction1 = _CpqServiceRecommendedAction1_Object(
    (1, 3, 6, 1, 4, 1, 232, 164, 2, 14),
    _CpqServiceRecommendedAction1_Type()
)
cpqServiceRecommendedAction1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqServiceRecommendedAction1.setStatus("mandatory")


class _CpqServiceRecommendedAction2_Type(DisplayString):
    """Custom type cpqServiceRecommendedAction2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqServiceRecommendedAction2_Type.__name__ = "DisplayString"
_CpqServiceRecommendedAction2_Object = MibScalar
cpqServiceRecommendedAction2 = _CpqServiceRecommendedAction2_Object(
    (1, 3, 6, 1, 4, 1, 232, 164, 2, 15),
    _CpqServiceRecommendedAction2_Type()
)
cpqServiceRecommendedAction2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqServiceRecommendedAction2.setStatus("mandatory")


class _CpqServiceRecommendedAction3_Type(DisplayString):
    """Custom type cpqServiceRecommendedAction3 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqServiceRecommendedAction3_Type.__name__ = "DisplayString"
_CpqServiceRecommendedAction3_Object = MibScalar
cpqServiceRecommendedAction3 = _CpqServiceRecommendedAction3_Object(
    (1, 3, 6, 1, 4, 1, 232, 164, 2, 16),
    _CpqServiceRecommendedAction3_Type()
)
cpqServiceRecommendedAction3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqServiceRecommendedAction3.setStatus("mandatory")


class _CpqServiceCustomerSelfRepairInstructionURL_Type(DisplayString):
    """Custom type cpqServiceCustomerSelfRepairInstructionURL based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqServiceCustomerSelfRepairInstructionURL_Type.__name__ = "DisplayString"
_CpqServiceCustomerSelfRepairInstructionURL_Object = MibScalar
cpqServiceCustomerSelfRepairInstructionURL = _CpqServiceCustomerSelfRepairInstructionURL_Object(
    (1, 3, 6, 1, 4, 1, 232, 164, 2, 17),
    _CpqServiceCustomerSelfRepairInstructionURL_Type()
)
cpqServiceCustomerSelfRepairInstructionURL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqServiceCustomerSelfRepairInstructionURL.setStatus("mandatory")


class _CpqServiceEventSeverity_Type(Integer32):
    """Custom type cpqServiceEventSeverity based on Integer32"""
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
        *(("critical", 1),
          ("major", 2),
          ("minor", 3),
          ("warning", 4),
          ("informational", 5))
    )


_CpqServiceEventSeverity_Type.__name__ = "Integer32"
_CpqServiceEventSeverity_Object = MibScalar
cpqServiceEventSeverity = _CpqServiceEventSeverity_Object(
    (1, 3, 6, 1, 4, 1, 232, 164, 2, 18),
    _CpqServiceEventSeverity_Type()
)
cpqServiceEventSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqServiceEventSeverity.setStatus("mandatory")


class _CpqServiceAnalyzerSystemName_Type(DisplayString):
    """Custom type cpqServiceAnalyzerSystemName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqServiceAnalyzerSystemName_Type.__name__ = "DisplayString"
_CpqServiceAnalyzerSystemName_Object = MibScalar
cpqServiceAnalyzerSystemName = _CpqServiceAnalyzerSystemName_Object(
    (1, 3, 6, 1, 4, 1, 232, 164, 2, 19),
    _CpqServiceAnalyzerSystemName_Type()
)
cpqServiceAnalyzerSystemName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqServiceAnalyzerSystemName.setStatus("mandatory")


class _CpqServiceFRUList1_Type(DisplayString):
    """Custom type cpqServiceFRUList1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqServiceFRUList1_Type.__name__ = "DisplayString"
_CpqServiceFRUList1_Object = MibScalar
cpqServiceFRUList1 = _CpqServiceFRUList1_Object(
    (1, 3, 6, 1, 4, 1, 232, 164, 2, 20),
    _CpqServiceFRUList1_Type()
)
cpqServiceFRUList1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqServiceFRUList1.setStatus("mandatory")


class _CpqServiceFRUList2_Type(DisplayString):
    """Custom type cpqServiceFRUList2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqServiceFRUList2_Type.__name__ = "DisplayString"
_CpqServiceFRUList2_Object = MibScalar
cpqServiceFRUList2 = _CpqServiceFRUList2_Object(
    (1, 3, 6, 1, 4, 1, 232, 164, 2, 21),
    _CpqServiceFRUList2_Type()
)
cpqServiceFRUList2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqServiceFRUList2.setStatus("mandatory")


class _CpqServiceFRUList3_Type(DisplayString):
    """Custom type cpqServiceFRUList3 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqServiceFRUList3_Type.__name__ = "DisplayString"
_CpqServiceFRUList3_Object = MibScalar
cpqServiceFRUList3 = _CpqServiceFRUList3_Object(
    (1, 3, 6, 1, 4, 1, 232, 164, 2, 22),
    _CpqServiceFRUList3_Type()
)
cpqServiceFRUList3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqServiceFRUList3.setStatus("mandatory")


class _CpqServiceFRUList4_Type(DisplayString):
    """Custom type cpqServiceFRUList4 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqServiceFRUList4_Type.__name__ = "DisplayString"
_CpqServiceFRUList4_Object = MibScalar
cpqServiceFRUList4 = _CpqServiceFRUList4_Object(
    (1, 3, 6, 1, 4, 1, 232, 164, 2, 23),
    _CpqServiceFRUList4_Type()
)
cpqServiceFRUList4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqServiceFRUList4.setStatus("mandatory")


class _CpqServiceLocation1_Type(DisplayString):
    """Custom type cpqServiceLocation1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqServiceLocation1_Type.__name__ = "DisplayString"
_CpqServiceLocation1_Object = MibScalar
cpqServiceLocation1 = _CpqServiceLocation1_Object(
    (1, 3, 6, 1, 4, 1, 232, 164, 2, 24),
    _CpqServiceLocation1_Type()
)
cpqServiceLocation1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqServiceLocation1.setStatus("mandatory")


class _CpqServiceLocation2_Type(DisplayString):
    """Custom type cpqServiceLocation2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqServiceLocation2_Type.__name__ = "DisplayString"
_CpqServiceLocation2_Object = MibScalar
cpqServiceLocation2 = _CpqServiceLocation2_Object(
    (1, 3, 6, 1, 4, 1, 232, 164, 2, 25),
    _CpqServiceLocation2_Type()
)
cpqServiceLocation2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqServiceLocation2.setStatus("mandatory")
_CpqService3Incident_ObjectIdentity = ObjectIdentity
cpqService3Incident = _CpqService3Incident_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 164, 3)
)


class _CpqService3IncidentSeverity_Type(Integer32):
    """Custom type cpqService3IncidentSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("important", 1),
          ("informational", 2))
    )


_CpqService3IncidentSeverity_Type.__name__ = "Integer32"
_CpqService3IncidentSeverity_Object = MibScalar
cpqService3IncidentSeverity = _CpqService3IncidentSeverity_Object(
    (1, 3, 6, 1, 4, 1, 232, 164, 3, 1),
    _CpqService3IncidentSeverity_Type()
)
cpqService3IncidentSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqService3IncidentSeverity.setStatus("deprecated")


class _CpqService3IncidentStatus_Type(Integer32):
    """Custom type cpqService3IncidentStatus based on Integer32"""
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
        *(("other", 1),
          ("intransit", 2),
          ("delivered", 3),
          ("undelivered", 4),
          ("assigned", 5),
          ("closed", 6),
          ("submitted_to_ISEE", 7))
    )


_CpqService3IncidentStatus_Type.__name__ = "Integer32"
_CpqService3IncidentStatus_Object = MibScalar
cpqService3IncidentStatus = _CpqService3IncidentStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 164, 3, 2),
    _CpqService3IncidentStatus_Type()
)
cpqService3IncidentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqService3IncidentStatus.setStatus("mandatory")


class _CpqService3IncidentInformation_Type(DisplayString):
    """Custom type cpqService3IncidentInformation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqService3IncidentInformation_Type.__name__ = "DisplayString"
_CpqService3IncidentInformation_Object = MibScalar
cpqService3IncidentInformation = _CpqService3IncidentInformation_Object(
    (1, 3, 6, 1, 4, 1, 232, 164, 3, 3),
    _CpqService3IncidentInformation_Type()
)
cpqService3IncidentInformation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqService3IncidentInformation.setStatus("mandatory")


class _CpqService3IncidentEvent_Type(DisplayString):
    """Custom type cpqService3IncidentEvent based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqService3IncidentEvent_Type.__name__ = "DisplayString"
_CpqService3IncidentEvent_Object = MibScalar
cpqService3IncidentEvent = _CpqService3IncidentEvent_Object(
    (1, 3, 6, 1, 4, 1, 232, 164, 3, 4),
    _CpqService3IncidentEvent_Type()
)
cpqService3IncidentEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqService3IncidentEvent.setStatus("mandatory")


class _CpqService3IncidentUniqueID_Type(DisplayString):
    """Custom type cpqService3IncidentUniqueID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqService3IncidentUniqueID_Type.__name__ = "DisplayString"
_CpqService3IncidentUniqueID_Object = MibScalar
cpqService3IncidentUniqueID = _CpqService3IncidentUniqueID_Object(
    (1, 3, 6, 1, 4, 1, 232, 164, 3, 5),
    _CpqService3IncidentUniqueID_Type()
)
cpqService3IncidentUniqueID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqService3IncidentUniqueID.setStatus("mandatory")


class _CpqService3IncidentTimeofOriginalEvent_Type(DisplayString):
    """Custom type cpqService3IncidentTimeofOriginalEvent based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqService3IncidentTimeofOriginalEvent_Type.__name__ = "DisplayString"
_CpqService3IncidentTimeofOriginalEvent_Object = MibScalar
cpqService3IncidentTimeofOriginalEvent = _CpqService3IncidentTimeofOriginalEvent_Object(
    (1, 3, 6, 1, 4, 1, 232, 164, 3, 6),
    _CpqService3IncidentTimeofOriginalEvent_Type()
)
cpqService3IncidentTimeofOriginalEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqService3IncidentTimeofOriginalEvent.setStatus("mandatory")


class _CpqService3IncidentSourceSystemName_Type(DisplayString):
    """Custom type cpqService3IncidentSourceSystemName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqService3IncidentSourceSystemName_Type.__name__ = "DisplayString"
_CpqService3IncidentSourceSystemName_Object = MibScalar
cpqService3IncidentSourceSystemName = _CpqService3IncidentSourceSystemName_Object(
    (1, 3, 6, 1, 4, 1, 232, 164, 3, 7),
    _CpqService3IncidentSourceSystemName_Type()
)
cpqService3IncidentSourceSystemName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqService3IncidentSourceSystemName.setStatus("mandatory")
_CpqService3IncidentIPAddessOfSource_Type = IpAddress
_CpqService3IncidentIPAddessOfSource_Object = MibScalar
cpqService3IncidentIPAddessOfSource = _CpqService3IncidentIPAddessOfSource_Object(
    (1, 3, 6, 1, 4, 1, 232, 164, 3, 8),
    _CpqService3IncidentIPAddessOfSource_Type()
)
cpqService3IncidentIPAddessOfSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqService3IncidentIPAddessOfSource.setStatus("optional")


class _CpqService3ISEEIncidentInformation_Type(DisplayString):
    """Custom type cpqService3ISEEIncidentInformation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqService3ISEEIncidentInformation_Type.__name__ = "DisplayString"
_CpqService3ISEEIncidentInformation_Object = MibScalar
cpqService3ISEEIncidentInformation = _CpqService3ISEEIncidentInformation_Object(
    (1, 3, 6, 1, 4, 1, 232, 164, 3, 9),
    _CpqService3ISEEIncidentInformation_Type()
)
cpqService3ISEEIncidentInformation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqService3ISEEIncidentInformation.setStatus("mandatory")


class _CpqService3IncidentIdentifier_Type(DisplayString):
    """Custom type cpqService3IncidentIdentifier based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqService3IncidentIdentifier_Type.__name__ = "DisplayString"
_CpqService3IncidentIdentifier_Object = MibScalar
cpqService3IncidentIdentifier = _CpqService3IncidentIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 232, 164, 3, 10),
    _CpqService3IncidentIdentifier_Type()
)
cpqService3IncidentIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqService3IncidentIdentifier.setStatus("mandatory")
_CpqService3IncidentReceiveTrapOID_Type = ObjectIdentifier
_CpqService3IncidentReceiveTrapOID_Object = MibScalar
cpqService3IncidentReceiveTrapOID = _CpqService3IncidentReceiveTrapOID_Object(
    (1, 3, 6, 1, 4, 1, 232, 164, 3, 11),
    _CpqService3IncidentReceiveTrapOID_Type()
)
cpqService3IncidentReceiveTrapOID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqService3IncidentReceiveTrapOID.setStatus("optional")
_CpqService3IncidentFilterOID_Type = ObjectIdentifier
_CpqService3IncidentFilterOID_Object = MibScalar
cpqService3IncidentFilterOID = _CpqService3IncidentFilterOID_Object(
    (1, 3, 6, 1, 4, 1, 232, 164, 3, 12),
    _CpqService3IncidentFilterOID_Type()
)
cpqService3IncidentFilterOID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqService3IncidentFilterOID.setStatus("deprecated")


class _CpqService3IncidentFilterValue_Type(DisplayString):
    """Custom type cpqService3IncidentFilterValue based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqService3IncidentFilterValue_Type.__name__ = "DisplayString"
_CpqService3IncidentFilterValue_Object = MibScalar
cpqService3IncidentFilterValue = _CpqService3IncidentFilterValue_Object(
    (1, 3, 6, 1, 4, 1, 232, 164, 3, 13),
    _CpqService3IncidentFilterValue_Type()
)
cpqService3IncidentFilterValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqService3IncidentFilterValue.setStatus("deprecated")


class _CpqService3RecommendedAction1_Type(DisplayString):
    """Custom type cpqService3RecommendedAction1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqService3RecommendedAction1_Type.__name__ = "DisplayString"
_CpqService3RecommendedAction1_Object = MibScalar
cpqService3RecommendedAction1 = _CpqService3RecommendedAction1_Object(
    (1, 3, 6, 1, 4, 1, 232, 164, 3, 14),
    _CpqService3RecommendedAction1_Type()
)
cpqService3RecommendedAction1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqService3RecommendedAction1.setStatus("optional")


class _CpqService3RecommendedAction2_Type(DisplayString):
    """Custom type cpqService3RecommendedAction2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqService3RecommendedAction2_Type.__name__ = "DisplayString"
_CpqService3RecommendedAction2_Object = MibScalar
cpqService3RecommendedAction2 = _CpqService3RecommendedAction2_Object(
    (1, 3, 6, 1, 4, 1, 232, 164, 3, 15),
    _CpqService3RecommendedAction2_Type()
)
cpqService3RecommendedAction2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqService3RecommendedAction2.setStatus("optional")


class _CpqService3RecommendedAction3_Type(DisplayString):
    """Custom type cpqService3RecommendedAction3 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqService3RecommendedAction3_Type.__name__ = "DisplayString"
_CpqService3RecommendedAction3_Object = MibScalar
cpqService3RecommendedAction3 = _CpqService3RecommendedAction3_Object(
    (1, 3, 6, 1, 4, 1, 232, 164, 3, 16),
    _CpqService3RecommendedAction3_Type()
)
cpqService3RecommendedAction3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqService3RecommendedAction3.setStatus("optional")


class _CpqService3CustomerSelfRepairInstructionURL_Type(DisplayString):
    """Custom type cpqService3CustomerSelfRepairInstructionURL based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqService3CustomerSelfRepairInstructionURL_Type.__name__ = "DisplayString"
_CpqService3CustomerSelfRepairInstructionURL_Object = MibScalar
cpqService3CustomerSelfRepairInstructionURL = _CpqService3CustomerSelfRepairInstructionURL_Object(
    (1, 3, 6, 1, 4, 1, 232, 164, 3, 17),
    _CpqService3CustomerSelfRepairInstructionURL_Type()
)
cpqService3CustomerSelfRepairInstructionURL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqService3CustomerSelfRepairInstructionURL.setStatus("optional")


class _CpqService3EventSeverity_Type(Integer32):
    """Custom type cpqService3EventSeverity based on Integer32"""
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
        *(("critical", 1),
          ("major", 2),
          ("minor", 3),
          ("warning", 4),
          ("informational", 5))
    )


_CpqService3EventSeverity_Type.__name__ = "Integer32"
_CpqService3EventSeverity_Object = MibScalar
cpqService3EventSeverity = _CpqService3EventSeverity_Object(
    (1, 3, 6, 1, 4, 1, 232, 164, 3, 18),
    _CpqService3EventSeverity_Type()
)
cpqService3EventSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqService3EventSeverity.setStatus("mandatory")


class _CpqService3AnalyzerSystemName_Type(DisplayString):
    """Custom type cpqService3AnalyzerSystemName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqService3AnalyzerSystemName_Type.__name__ = "DisplayString"
_CpqService3AnalyzerSystemName_Object = MibScalar
cpqService3AnalyzerSystemName = _CpqService3AnalyzerSystemName_Object(
    (1, 3, 6, 1, 4, 1, 232, 164, 3, 19),
    _CpqService3AnalyzerSystemName_Type()
)
cpqService3AnalyzerSystemName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqService3AnalyzerSystemName.setStatus("mandatory")


class _CpqService3FRUList1_Type(DisplayString):
    """Custom type cpqService3FRUList1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqService3FRUList1_Type.__name__ = "DisplayString"
_CpqService3FRUList1_Object = MibScalar
cpqService3FRUList1 = _CpqService3FRUList1_Object(
    (1, 3, 6, 1, 4, 1, 232, 164, 3, 20),
    _CpqService3FRUList1_Type()
)
cpqService3FRUList1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqService3FRUList1.setStatus("optional")


class _CpqService3FRUList2_Type(DisplayString):
    """Custom type cpqService3FRUList2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqService3FRUList2_Type.__name__ = "DisplayString"
_CpqService3FRUList2_Object = MibScalar
cpqService3FRUList2 = _CpqService3FRUList2_Object(
    (1, 3, 6, 1, 4, 1, 232, 164, 3, 21),
    _CpqService3FRUList2_Type()
)
cpqService3FRUList2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqService3FRUList2.setStatus("optional")


class _CpqService3FRUList3_Type(DisplayString):
    """Custom type cpqService3FRUList3 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqService3FRUList3_Type.__name__ = "DisplayString"
_CpqService3FRUList3_Object = MibScalar
cpqService3FRUList3 = _CpqService3FRUList3_Object(
    (1, 3, 6, 1, 4, 1, 232, 164, 3, 22),
    _CpqService3FRUList3_Type()
)
cpqService3FRUList3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqService3FRUList3.setStatus("optional")


class _CpqService3FRUList4_Type(DisplayString):
    """Custom type cpqService3FRUList4 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqService3FRUList4_Type.__name__ = "DisplayString"
_CpqService3FRUList4_Object = MibScalar
cpqService3FRUList4 = _CpqService3FRUList4_Object(
    (1, 3, 6, 1, 4, 1, 232, 164, 3, 23),
    _CpqService3FRUList4_Type()
)
cpqService3FRUList4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqService3FRUList4.setStatus("optional")


class _CpqService3Location1_Type(DisplayString):
    """Custom type cpqService3Location1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqService3Location1_Type.__name__ = "DisplayString"
_CpqService3Location1_Object = MibScalar
cpqService3Location1 = _CpqService3Location1_Object(
    (1, 3, 6, 1, 4, 1, 232, 164, 3, 24),
    _CpqService3Location1_Type()
)
cpqService3Location1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqService3Location1.setStatus("optional")


class _CpqService3Location2_Type(DisplayString):
    """Custom type cpqService3Location2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqService3Location2_Type.__name__ = "DisplayString"
_CpqService3Location2_Object = MibScalar
cpqService3Location2 = _CpqService3Location2_Object(
    (1, 3, 6, 1, 4, 1, 232, 164, 3, 25),
    _CpqService3Location2_Type()
)
cpqService3Location2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqService3Location2.setStatus("optional")


class _CpqService3Incident7Status_Type(Integer32):
    """Custom type cpqService3Incident7Status based on Integer32"""
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
        *(("error", 0),
          ("pending", 1),
          ("submitted", 2),
          ("received", 3),
          ("open", 4),
          ("closed", 5))
    )


_CpqService3Incident7Status_Type.__name__ = "Integer32"
_CpqService3Incident7Status_Object = MibScalar
cpqService3Incident7Status = _CpqService3Incident7Status_Object(
    (1, 3, 6, 1, 4, 1, 232, 164, 3, 26),
    _CpqService3Incident7Status_Type()
)
cpqService3Incident7Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqService3Incident7Status.setStatus("mandatory")


class _CpqService3CaseIdentifier_Type(DisplayString):
    """Custom type cpqService3CaseIdentifier based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqService3CaseIdentifier_Type.__name__ = "DisplayString"
_CpqService3CaseIdentifier_Object = MibScalar
cpqService3CaseIdentifier = _CpqService3CaseIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 232, 164, 3, 27),
    _CpqService3CaseIdentifier_Type()
)
cpqService3CaseIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqService3CaseIdentifier.setStatus("optional")


class _CpqService3IncidentToolName_Type(DisplayString):
    """Custom type cpqService3IncidentToolName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqService3IncidentToolName_Type.__name__ = "DisplayString"
_CpqService3IncidentToolName_Object = MibScalar
cpqService3IncidentToolName = _CpqService3IncidentToolName_Object(
    (1, 3, 6, 1, 4, 1, 232, 164, 3, 28),
    _CpqService3IncidentToolName_Type()
)
cpqService3IncidentToolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqService3IncidentToolName.setStatus("mandatory")


class _CpqService3IncidentToolVersion_Type(DisplayString):
    """Custom type cpqService3IncidentToolVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqService3IncidentToolVersion_Type.__name__ = "DisplayString"
_CpqService3IncidentToolVersion_Object = MibScalar
cpqService3IncidentToolVersion = _CpqService3IncidentToolVersion_Object(
    (1, 3, 6, 1, 4, 1, 232, 164, 3, 29),
    _CpqService3IncidentToolVersion_Type()
)
cpqService3IncidentToolVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqService3IncidentToolVersion.setStatus("mandatory")


class _CpqService3IncidentIPv6AddressOfSource_Type(DisplayString):
    """Custom type cpqService3IncidentIPv6AddressOfSource based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqService3IncidentIPv6AddressOfSource_Type.__name__ = "DisplayString"
_CpqService3IncidentIPv6AddressOfSource_Object = MibScalar
cpqService3IncidentIPv6AddressOfSource = _CpqService3IncidentIPv6AddressOfSource_Object(
    (1, 3, 6, 1, 4, 1, 232, 164, 3, 30),
    _CpqService3IncidentIPv6AddressOfSource_Type()
)
cpqService3IncidentIPv6AddressOfSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqService3IncidentIPv6AddressOfSource.setStatus("optional")


class _CpqService3IncidentSerialNumberOfSource_Type(DisplayString):
    """Custom type cpqService3IncidentSerialNumberOfSource based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqService3IncidentSerialNumberOfSource_Type.__name__ = "DisplayString"
_CpqService3IncidentSerialNumberOfSource_Object = MibScalar
cpqService3IncidentSerialNumberOfSource = _CpqService3IncidentSerialNumberOfSource_Object(
    (1, 3, 6, 1, 4, 1, 232, 164, 3, 31),
    _CpqService3IncidentSerialNumberOfSource_Type()
)
cpqService3IncidentSerialNumberOfSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqService3IncidentSerialNumberOfSource.setStatus("optional")


class _CpqService3IncidentProductNumberOfSource_Type(DisplayString):
    """Custom type cpqService3IncidentProductNumberOfSource based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqService3IncidentProductNumberOfSource_Type.__name__ = "DisplayString"
_CpqService3IncidentProductNumberOfSource_Object = MibScalar
cpqService3IncidentProductNumberOfSource = _CpqService3IncidentProductNumberOfSource_Object(
    (1, 3, 6, 1, 4, 1, 232, 164, 3, 32),
    _CpqService3IncidentProductNumberOfSource_Type()
)
cpqService3IncidentProductNumberOfSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqService3IncidentProductNumberOfSource.setStatus("optional")


class _CpqService3IncidentProductModelOfSource_Type(DisplayString):
    """Custom type cpqService3IncidentProductModelOfSource based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqService3IncidentProductModelOfSource_Type.__name__ = "DisplayString"
_CpqService3IncidentProductModelOfSource_Object = MibScalar
cpqService3IncidentProductModelOfSource = _CpqService3IncidentProductModelOfSource_Object(
    (1, 3, 6, 1, 4, 1, 232, 164, 3, 33),
    _CpqService3IncidentProductModelOfSource_Type()
)
cpqService3IncidentProductModelOfSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqService3IncidentProductModelOfSource.setStatus("optional")


class _CpqService3IncidentUserEnteredSerialNumberOfSource_Type(DisplayString):
    """Custom type cpqService3IncidentUserEnteredSerialNumberOfSource based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqService3IncidentUserEnteredSerialNumberOfSource_Type.__name__ = "DisplayString"
_CpqService3IncidentUserEnteredSerialNumberOfSource_Object = MibScalar
cpqService3IncidentUserEnteredSerialNumberOfSource = _CpqService3IncidentUserEnteredSerialNumberOfSource_Object(
    (1, 3, 6, 1, 4, 1, 232, 164, 3, 34),
    _CpqService3IncidentUserEnteredSerialNumberOfSource_Type()
)
cpqService3IncidentUserEnteredSerialNumberOfSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqService3IncidentUserEnteredSerialNumberOfSource.setStatus("optional")


class _CpqService3IncidentUserEnteredProductNumberOfSource_Type(DisplayString):
    """Custom type cpqService3IncidentUserEnteredProductNumberOfSource based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqService3IncidentUserEnteredProductNumberOfSource_Type.__name__ = "DisplayString"
_CpqService3IncidentUserEnteredProductNumberOfSource_Object = MibScalar
cpqService3IncidentUserEnteredProductNumberOfSource = _CpqService3IncidentUserEnteredProductNumberOfSource_Object(
    (1, 3, 6, 1, 4, 1, 232, 164, 3, 35),
    _CpqService3IncidentUserEnteredProductNumberOfSource_Type()
)
cpqService3IncidentUserEnteredProductNumberOfSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqService3IncidentUserEnteredProductNumberOfSource.setStatus("optional")


class _CpqService3IncidentMgmtNodeName_Type(DisplayString):
    """Custom type cpqService3IncidentMgmtNodeName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqService3IncidentMgmtNodeName_Type.__name__ = "DisplayString"
_CpqService3IncidentMgmtNodeName_Object = MibScalar
cpqService3IncidentMgmtNodeName = _CpqService3IncidentMgmtNodeName_Object(
    (1, 3, 6, 1, 4, 1, 232, 164, 3, 36),
    _CpqService3IncidentMgmtNodeName_Type()
)
cpqService3IncidentMgmtNodeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqService3IncidentMgmtNodeName.setStatus("optional")


class _CpqService3IncidentIPAddressOfMgmtNode_Type(DisplayString):
    """Custom type cpqService3IncidentIPAddressOfMgmtNode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqService3IncidentIPAddressOfMgmtNode_Type.__name__ = "DisplayString"
_CpqService3IncidentIPAddressOfMgmtNode_Object = MibScalar
cpqService3IncidentIPAddressOfMgmtNode = _CpqService3IncidentIPAddressOfMgmtNode_Object(
    (1, 3, 6, 1, 4, 1, 232, 164, 3, 37),
    _CpqService3IncidentIPAddressOfMgmtNode_Type()
)
cpqService3IncidentIPAddressOfMgmtNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqService3IncidentIPAddressOfMgmtNode.setStatus("optional")


class _CpqService3IncidentIPv6AddressOfMgmtNode_Type(DisplayString):
    """Custom type cpqService3IncidentIPv6AddressOfMgmtNode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqService3IncidentIPv6AddressOfMgmtNode_Type.__name__ = "DisplayString"
_CpqService3IncidentIPv6AddressOfMgmtNode_Object = MibScalar
cpqService3IncidentIPv6AddressOfMgmtNode = _CpqService3IncidentIPv6AddressOfMgmtNode_Object(
    (1, 3, 6, 1, 4, 1, 232, 164, 3, 38),
    _CpqService3IncidentIPv6AddressOfMgmtNode_Type()
)
cpqService3IncidentIPv6AddressOfMgmtNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqService3IncidentIPv6AddressOfMgmtNode.setStatus("optional")


class _CpqService3IncidentSerialNumberOfMgmtNode_Type(DisplayString):
    """Custom type cpqService3IncidentSerialNumberOfMgmtNode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqService3IncidentSerialNumberOfMgmtNode_Type.__name__ = "DisplayString"
_CpqService3IncidentSerialNumberOfMgmtNode_Object = MibScalar
cpqService3IncidentSerialNumberOfMgmtNode = _CpqService3IncidentSerialNumberOfMgmtNode_Object(
    (1, 3, 6, 1, 4, 1, 232, 164, 3, 39),
    _CpqService3IncidentSerialNumberOfMgmtNode_Type()
)
cpqService3IncidentSerialNumberOfMgmtNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqService3IncidentSerialNumberOfMgmtNode.setStatus("optional")


class _CpqService3IncidentProductNumberOfMgmtNode_Type(DisplayString):
    """Custom type cpqService3IncidentProductNumberOfMgmtNode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqService3IncidentProductNumberOfMgmtNode_Type.__name__ = "DisplayString"
_CpqService3IncidentProductNumberOfMgmtNode_Object = MibScalar
cpqService3IncidentProductNumberOfMgmtNode = _CpqService3IncidentProductNumberOfMgmtNode_Object(
    (1, 3, 6, 1, 4, 1, 232, 164, 3, 40),
    _CpqService3IncidentProductNumberOfMgmtNode_Type()
)
cpqService3IncidentProductNumberOfMgmtNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqService3IncidentProductNumberOfMgmtNode.setStatus("optional")


class _CpqService3IncidentUserEnteredSerialNumberOfMgmtNode_Type(DisplayString):
    """Custom type cpqService3IncidentUserEnteredSerialNumberOfMgmtNode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqService3IncidentUserEnteredSerialNumberOfMgmtNode_Type.__name__ = "DisplayString"
_CpqService3IncidentUserEnteredSerialNumberOfMgmtNode_Object = MibScalar
cpqService3IncidentUserEnteredSerialNumberOfMgmtNode = _CpqService3IncidentUserEnteredSerialNumberOfMgmtNode_Object(
    (1, 3, 6, 1, 4, 1, 232, 164, 3, 41),
    _CpqService3IncidentUserEnteredSerialNumberOfMgmtNode_Type()
)
cpqService3IncidentUserEnteredSerialNumberOfMgmtNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqService3IncidentUserEnteredSerialNumberOfMgmtNode.setStatus("optional")


class _CpqService3IncidentUserEnteredProductNumberOfMgmtNode_Type(DisplayString):
    """Custom type cpqService3IncidentUserEnteredProductNumberOfMgmtNode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqService3IncidentUserEnteredProductNumberOfMgmtNode_Type.__name__ = "DisplayString"
_CpqService3IncidentUserEnteredProductNumberOfMgmtNode_Object = MibScalar
cpqService3IncidentUserEnteredProductNumberOfMgmtNode = _CpqService3IncidentUserEnteredProductNumberOfMgmtNode_Object(
    (1, 3, 6, 1, 4, 1, 232, 164, 3, 42),
    _CpqService3IncidentUserEnteredProductNumberOfMgmtNode_Type()
)
cpqService3IncidentUserEnteredProductNumberOfMgmtNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqService3IncidentUserEnteredProductNumberOfMgmtNode.setStatus("optional")


class _CpqService3IncidentProductModelOfMgmtNode_Type(DisplayString):
    """Custom type cpqService3IncidentProductModelOfMgmtNode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqService3IncidentProductModelOfMgmtNode_Type.__name__ = "DisplayString"
_CpqService3IncidentProductModelOfMgmtNode_Object = MibScalar
cpqService3IncidentProductModelOfMgmtNode = _CpqService3IncidentProductModelOfMgmtNode_Object(
    (1, 3, 6, 1, 4, 1, 232, 164, 3, 43),
    _CpqService3IncidentProductModelOfMgmtNode_Type()
)
cpqService3IncidentProductModelOfMgmtNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqService3IncidentProductModelOfMgmtNode.setStatus("optional")

# Managed Objects groups


# Notification objects

cpqServiceInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 164, 0, 164001)
)
cpqServiceInformation.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQSERVICE-MIB", "cpqServiceIncidentSeverity"),
        ("CPQSERVICE-MIB", "cpqServiceIncidentStatus"),
        ("CPQSERVICE-MIB", "cpqServiceIncidentInformation"),
        ("CPQSERVICE-MIB", "cpqServiceIncidentEvent"),
        ("CPQSERVICE-MIB", "cpqServiceIncidentUniqueID"),
        ("CPQSERVICE-MIB", "cpqServiceIncidentTimeofOriginalEvent"),
        ("CPQSERVICE-MIB", "cpqServiceIncidentSourceSystemName"),
        ("CPQSERVICE-MIB", "cpqServiceIncidentIPAddessOfSource"),
        ("CPQSERVICE-MIB", "cpqServiceISEEIncidentInformation"),
        ("CPQSERVICE-MIB", "cpqServiceIncidentIdentifier"),
        ("CPQSERVICE-MIB", "cpqServiceIncidentReceiveTrapOID"),
        ("CPQSERVICE-MIB", "cpqServiceIncidentFilterOID"),
        ("CPQSERVICE-MIB", "cpqServiceIncidentFilterValue"))
)
if mibBuilder.loadTexts:
    cpqServiceInformation.setStatus(
        ""
    )

cpqService2Information = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 164, 0, 164002)
)
cpqService2Information.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQSERVICE-MIB", "cpqServiceIncidentStatus"),
        ("CPQSERVICE-MIB", "cpqServiceIncidentInformation"),
        ("CPQSERVICE-MIB", "cpqServiceIncidentEvent"),
        ("CPQSERVICE-MIB", "cpqServiceIncidentUniqueID"),
        ("CPQSERVICE-MIB", "cpqServiceIncidentTimeofOriginalEvent"),
        ("CPQSERVICE-MIB", "cpqServiceIncidentSourceSystemName"),
        ("CPQSERVICE-MIB", "cpqServiceIncidentIPAddessOfSource"),
        ("CPQSERVICE-MIB", "cpqServiceISEEIncidentInformation"),
        ("CPQSERVICE-MIB", "cpqServiceIncidentIdentifier"),
        ("CPQSERVICE-MIB", "cpqServiceIncidentReceiveTrapOID"),
        ("CPQSERVICE-MIB", "cpqServiceRecommendedAction1"),
        ("CPQSERVICE-MIB", "cpqServiceRecommendedAction2"),
        ("CPQSERVICE-MIB", "cpqServiceRecommendedAction3"),
        ("CPQSERVICE-MIB", "cpqServiceCustomerSelfRepairInstructionURL"))
)
if mibBuilder.loadTexts:
    cpqService2Information.setStatus(
        ""
    )

cpqService3Information = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 164, 0, 164003)
)
cpqService3Information.setObjects(
      *(("CPQSERVICE-MIB", "cpqService3IncidentSourceSystemName"),
        ("CPQSERVICE-MIB", "cpqService3IncidentIPAddessOfSource"),
        ("CPQSERVICE-MIB", "cpqService3EventSeverity"),
        ("CPQSERVICE-MIB", "cpqService3IncidentStatus"),
        ("CPQSERVICE-MIB", "cpqService3IncidentInformation"),
        ("CPQSERVICE-MIB", "cpqService3IncidentEvent"),
        ("CPQSERVICE-MIB", "cpqService3IncidentUniqueID"),
        ("CPQSERVICE-MIB", "cpqService3IncidentTimeofOriginalEvent"),
        ("CPQSERVICE-MIB", "cpqService3AnalyzerSystemName"),
        ("CPQSERVICE-MIB", "cpqService3ISEEIncidentInformation"),
        ("CPQSERVICE-MIB", "cpqService3IncidentIdentifier"),
        ("CPQSERVICE-MIB", "cpqService3IncidentReceiveTrapOID"),
        ("CPQSERVICE-MIB", "cpqService3RecommendedAction1"),
        ("CPQSERVICE-MIB", "cpqService3RecommendedAction2"),
        ("CPQSERVICE-MIB", "cpqService3RecommendedAction3"),
        ("CPQSERVICE-MIB", "cpqService3FRUList1"),
        ("CPQSERVICE-MIB", "cpqService3FRUList2"),
        ("CPQSERVICE-MIB", "cpqService3FRUList3"),
        ("CPQSERVICE-MIB", "cpqService3FRUList4"),
        ("CPQSERVICE-MIB", "cpqService3Location1"),
        ("CPQSERVICE-MIB", "cpqService3Location2"),
        ("CPQSERVICE-MIB", "cpqService3CustomerSelfRepairInstructionURL"))
)
if mibBuilder.loadTexts:
    cpqService3Information.setStatus(
        ""
    )

cpqService4Information = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 164, 0, 164004)
)
cpqService4Information.setObjects(
      *(("CPQSERVICE-MIB", "cpqService3IncidentSourceSystemName"),
        ("CPQSERVICE-MIB", "cpqService3IncidentIPAddessOfSource"),
        ("CPQSERVICE-MIB", "cpqService3EventSeverity"),
        ("CPQSERVICE-MIB", "cpqService3Incident7Status"),
        ("CPQSERVICE-MIB", "cpqService3IncidentInformation"),
        ("CPQSERVICE-MIB", "cpqService3IncidentEvent"),
        ("CPQSERVICE-MIB", "cpqService3IncidentUniqueID"),
        ("CPQSERVICE-MIB", "cpqService3IncidentTimeofOriginalEvent"),
        ("CPQSERVICE-MIB", "cpqService3AnalyzerSystemName"),
        ("CPQSERVICE-MIB", "cpqService3ISEEIncidentInformation"),
        ("CPQSERVICE-MIB", "cpqService3IncidentIdentifier"),
        ("CPQSERVICE-MIB", "cpqService3CaseIdentifier"),
        ("CPQSERVICE-MIB", "cpqService3IncidentReceiveTrapOID"),
        ("CPQSERVICE-MIB", "cpqService3RecommendedAction1"),
        ("CPQSERVICE-MIB", "cpqService3RecommendedAction2"),
        ("CPQSERVICE-MIB", "cpqService3RecommendedAction3"),
        ("CPQSERVICE-MIB", "cpqService3FRUList1"),
        ("CPQSERVICE-MIB", "cpqService3FRUList2"),
        ("CPQSERVICE-MIB", "cpqService3FRUList3"),
        ("CPQSERVICE-MIB", "cpqService3FRUList4"),
        ("CPQSERVICE-MIB", "cpqService3Location1"),
        ("CPQSERVICE-MIB", "cpqService3Location2"),
        ("CPQSERVICE-MIB", "cpqService3CustomerSelfRepairInstructionURL"))
)
if mibBuilder.loadTexts:
    cpqService4Information.setStatus(
        ""
    )

cpqService5Information = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 164, 0, 164005)
)
cpqService5Information.setObjects(
      *(("CPQSERVICE-MIB", "cpqService3IncidentSourceSystemName"),
        ("CPQSERVICE-MIB", "cpqService3IncidentIPAddessOfSource"),
        ("CPQSERVICE-MIB", "cpqService3EventSeverity"),
        ("CPQSERVICE-MIB", "cpqService3Incident7Status"),
        ("CPQSERVICE-MIB", "cpqService3IncidentInformation"),
        ("CPQSERVICE-MIB", "cpqService3IncidentEvent"),
        ("CPQSERVICE-MIB", "cpqService3IncidentUniqueID"),
        ("CPQSERVICE-MIB", "cpqService3IncidentTimeofOriginalEvent"),
        ("CPQSERVICE-MIB", "cpqService3AnalyzerSystemName"),
        ("CPQSERVICE-MIB", "cpqService3ISEEIncidentInformation"),
        ("CPQSERVICE-MIB", "cpqService3IncidentIdentifier"),
        ("CPQSERVICE-MIB", "cpqService3CaseIdentifier"),
        ("CPQSERVICE-MIB", "cpqService3IncidentReceiveTrapOID"),
        ("CPQSERVICE-MIB", "cpqService3RecommendedAction1"),
        ("CPQSERVICE-MIB", "cpqService3RecommendedAction2"),
        ("CPQSERVICE-MIB", "cpqService3RecommendedAction3"),
        ("CPQSERVICE-MIB", "cpqService3FRUList1"),
        ("CPQSERVICE-MIB", "cpqService3FRUList2"),
        ("CPQSERVICE-MIB", "cpqService3FRUList3"),
        ("CPQSERVICE-MIB", "cpqService3FRUList4"),
        ("CPQSERVICE-MIB", "cpqService3Location1"),
        ("CPQSERVICE-MIB", "cpqService3Location2"),
        ("CPQSERVICE-MIB", "cpqService3CustomerSelfRepairInstructionURL"),
        ("CPQSERVICE-MIB", "cpqService3IncidentToolName"),
        ("CPQSERVICE-MIB", "cpqService3IncidentToolVersion"),
        ("CPQSERVICE-MIB", "cpqService3IncidentIPv6AddressOfSource"),
        ("CPQSERVICE-MIB", "cpqService3IncidentSerialNumberOfSource"),
        ("CPQSERVICE-MIB", "cpqService3IncidentProductNumberOfSource"),
        ("CPQSERVICE-MIB", "cpqService3IncidentProductModelOfSource"),
        ("CPQSERVICE-MIB", "cpqService3IncidentUserEnteredSerialNumberOfSource"),
        ("CPQSERVICE-MIB", "cpqService3IncidentUserEnteredProductNumberOfSource"),
        ("CPQSERVICE-MIB", "cpqService3IncidentMgmtNodeName"),
        ("CPQSERVICE-MIB", "cpqService3IncidentIPAddressOfMgmtNode"),
        ("CPQSERVICE-MIB", "cpqService3IncidentIPv6AddressOfMgmtNode"),
        ("CPQSERVICE-MIB", "cpqService3IncidentSerialNumberOfMgmtNode"),
        ("CPQSERVICE-MIB", "cpqService3IncidentProductNumberOfMgmtNode"),
        ("CPQSERVICE-MIB", "cpqService3IncidentUserEnteredSerialNumberOfMgmtNode"),
        ("CPQSERVICE-MIB", "cpqService3IncidentUserEnteredProductNumberOfMgmtNode"),
        ("CPQSERVICE-MIB", "cpqService3IncidentProductModelOfMgmtNode"))
)
if mibBuilder.loadTexts:
    cpqService5Information.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CPQSERVICE-MIB",
    **{"cpqService": cpqService,
       "cpqServiceInformation": cpqServiceInformation,
       "cpqService2Information": cpqService2Information,
       "cpqService3Information": cpqService3Information,
       "cpqService4Information": cpqService4Information,
       "cpqService5Information": cpqService5Information,
       "cpqServiceMibRev": cpqServiceMibRev,
       "cpqServiceMibRevMinor": cpqServiceMibRevMinor,
       "cpqServiceMibRevMajor": cpqServiceMibRevMajor,
       "cpqServiceIncident": cpqServiceIncident,
       "cpqServiceIncidentSeverity": cpqServiceIncidentSeverity,
       "cpqServiceIncidentStatus": cpqServiceIncidentStatus,
       "cpqServiceIncidentInformation": cpqServiceIncidentInformation,
       "cpqServiceIncidentEvent": cpqServiceIncidentEvent,
       "cpqServiceIncidentUniqueID": cpqServiceIncidentUniqueID,
       "cpqServiceIncidentTimeofOriginalEvent": cpqServiceIncidentTimeofOriginalEvent,
       "cpqServiceIncidentSourceSystemName": cpqServiceIncidentSourceSystemName,
       "cpqServiceIncidentIPAddessOfSource": cpqServiceIncidentIPAddessOfSource,
       "cpqServiceISEEIncidentInformation": cpqServiceISEEIncidentInformation,
       "cpqServiceIncidentIdentifier": cpqServiceIncidentIdentifier,
       "cpqServiceIncidentReceiveTrapOID": cpqServiceIncidentReceiveTrapOID,
       "cpqServiceIncidentFilterOID": cpqServiceIncidentFilterOID,
       "cpqServiceIncidentFilterValue": cpqServiceIncidentFilterValue,
       "cpqServiceRecommendedAction1": cpqServiceRecommendedAction1,
       "cpqServiceRecommendedAction2": cpqServiceRecommendedAction2,
       "cpqServiceRecommendedAction3": cpqServiceRecommendedAction3,
       "cpqServiceCustomerSelfRepairInstructionURL": cpqServiceCustomerSelfRepairInstructionURL,
       "cpqServiceEventSeverity": cpqServiceEventSeverity,
       "cpqServiceAnalyzerSystemName": cpqServiceAnalyzerSystemName,
       "cpqServiceFRUList1": cpqServiceFRUList1,
       "cpqServiceFRUList2": cpqServiceFRUList2,
       "cpqServiceFRUList3": cpqServiceFRUList3,
       "cpqServiceFRUList4": cpqServiceFRUList4,
       "cpqServiceLocation1": cpqServiceLocation1,
       "cpqServiceLocation2": cpqServiceLocation2,
       "cpqService3Incident": cpqService3Incident,
       "cpqService3IncidentSeverity": cpqService3IncidentSeverity,
       "cpqService3IncidentStatus": cpqService3IncidentStatus,
       "cpqService3IncidentInformation": cpqService3IncidentInformation,
       "cpqService3IncidentEvent": cpqService3IncidentEvent,
       "cpqService3IncidentUniqueID": cpqService3IncidentUniqueID,
       "cpqService3IncidentTimeofOriginalEvent": cpqService3IncidentTimeofOriginalEvent,
       "cpqService3IncidentSourceSystemName": cpqService3IncidentSourceSystemName,
       "cpqService3IncidentIPAddessOfSource": cpqService3IncidentIPAddessOfSource,
       "cpqService3ISEEIncidentInformation": cpqService3ISEEIncidentInformation,
       "cpqService3IncidentIdentifier": cpqService3IncidentIdentifier,
       "cpqService3IncidentReceiveTrapOID": cpqService3IncidentReceiveTrapOID,
       "cpqService3IncidentFilterOID": cpqService3IncidentFilterOID,
       "cpqService3IncidentFilterValue": cpqService3IncidentFilterValue,
       "cpqService3RecommendedAction1": cpqService3RecommendedAction1,
       "cpqService3RecommendedAction2": cpqService3RecommendedAction2,
       "cpqService3RecommendedAction3": cpqService3RecommendedAction3,
       "cpqService3CustomerSelfRepairInstructionURL": cpqService3CustomerSelfRepairInstructionURL,
       "cpqService3EventSeverity": cpqService3EventSeverity,
       "cpqService3AnalyzerSystemName": cpqService3AnalyzerSystemName,
       "cpqService3FRUList1": cpqService3FRUList1,
       "cpqService3FRUList2": cpqService3FRUList2,
       "cpqService3FRUList3": cpqService3FRUList3,
       "cpqService3FRUList4": cpqService3FRUList4,
       "cpqService3Location1": cpqService3Location1,
       "cpqService3Location2": cpqService3Location2,
       "cpqService3Incident7Status": cpqService3Incident7Status,
       "cpqService3CaseIdentifier": cpqService3CaseIdentifier,
       "cpqService3IncidentToolName": cpqService3IncidentToolName,
       "cpqService3IncidentToolVersion": cpqService3IncidentToolVersion,
       "cpqService3IncidentIPv6AddressOfSource": cpqService3IncidentIPv6AddressOfSource,
       "cpqService3IncidentSerialNumberOfSource": cpqService3IncidentSerialNumberOfSource,
       "cpqService3IncidentProductNumberOfSource": cpqService3IncidentProductNumberOfSource,
       "cpqService3IncidentProductModelOfSource": cpqService3IncidentProductModelOfSource,
       "cpqService3IncidentUserEnteredSerialNumberOfSource": cpqService3IncidentUserEnteredSerialNumberOfSource,
       "cpqService3IncidentUserEnteredProductNumberOfSource": cpqService3IncidentUserEnteredProductNumberOfSource,
       "cpqService3IncidentMgmtNodeName": cpqService3IncidentMgmtNodeName,
       "cpqService3IncidentIPAddressOfMgmtNode": cpqService3IncidentIPAddressOfMgmtNode,
       "cpqService3IncidentIPv6AddressOfMgmtNode": cpqService3IncidentIPv6AddressOfMgmtNode,
       "cpqService3IncidentSerialNumberOfMgmtNode": cpqService3IncidentSerialNumberOfMgmtNode,
       "cpqService3IncidentProductNumberOfMgmtNode": cpqService3IncidentProductNumberOfMgmtNode,
       "cpqService3IncidentUserEnteredSerialNumberOfMgmtNode": cpqService3IncidentUserEnteredSerialNumberOfMgmtNode,
       "cpqService3IncidentUserEnteredProductNumberOfMgmtNode": cpqService3IncidentUserEnteredProductNumberOfMgmtNode,
       "cpqService3IncidentProductModelOfMgmtNode": cpqService3IncidentProductModelOfMgmtNode}
)
