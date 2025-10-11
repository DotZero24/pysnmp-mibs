# SNMP MIB module (CPQISCSI-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/hp/CPQISCSI-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:39:51 2025
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

(compaq,
 cpqHoTrapFlags) = mibBuilder.importSymbols(
    "CPQHOST-MIB",
    "compaq",
    "cpqHoTrapFlags")

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

_CpqiScsiModule_ObjectIdentity = ObjectIdentity
cpqiScsiModule = _CpqiScsiModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 169)
)
_CpqiScsiMibRev_ObjectIdentity = ObjectIdentity
cpqiScsiMibRev = _CpqiScsiMibRev_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 169, 1)
)


class _CpqiScsiMibRevMajor_Type(Integer32):
    """Custom type cpqiScsiMibRevMajor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CpqiScsiMibRevMajor_Type.__name__ = "Integer32"
_CpqiScsiMibRevMajor_Object = MibScalar
cpqiScsiMibRevMajor = _CpqiScsiMibRevMajor_Object(
    (1, 3, 6, 1, 4, 1, 232, 169, 1, 1),
    _CpqiScsiMibRevMajor_Type()
)
cpqiScsiMibRevMajor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqiScsiMibRevMajor.setStatus("mandatory")


class _CpqiScsiMibRevMinor_Type(Integer32):
    """Custom type cpqiScsiMibRevMinor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CpqiScsiMibRevMinor_Type.__name__ = "Integer32"
_CpqiScsiMibRevMinor_Object = MibScalar
cpqiScsiMibRevMinor = _CpqiScsiMibRevMinor_Object(
    (1, 3, 6, 1, 4, 1, 232, 169, 1, 2),
    _CpqiScsiMibRevMinor_Type()
)
cpqiScsiMibRevMinor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqiScsiMibRevMinor.setStatus("mandatory")


class _CpqiScsiMibCondition_Type(Integer32):
    """Custom type cpqiScsiMibCondition based on Integer32"""
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
        *(("other", 1),
          ("ok", 2),
          ("degraded", 3),
          ("failed", 4))
    )


_CpqiScsiMibCondition_Type.__name__ = "Integer32"
_CpqiScsiMibCondition_Object = MibScalar
cpqiScsiMibCondition = _CpqiScsiMibCondition_Object(
    (1, 3, 6, 1, 4, 1, 232, 169, 1, 3),
    _CpqiScsiMibCondition_Type()
)
cpqiScsiMibCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqiScsiMibCondition.setStatus("mandatory")
_CpqiScsiObjects_ObjectIdentity = ObjectIdentity
cpqiScsiObjects = _CpqiScsiObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 169, 2)
)
_CpqiScsiDescriptors_ObjectIdentity = ObjectIdentity
cpqiScsiDescriptors = _CpqiScsiDescriptors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 169, 2, 1)
)
_CpqiScsiInstance_ObjectIdentity = ObjectIdentity
cpqiScsiInstance = _CpqiScsiInstance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 169, 2, 2)
)
_CpqiScsiInstanceAttributesTable_Object = MibTable
cpqiScsiInstanceAttributesTable = _CpqiScsiInstanceAttributesTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 169, 2, 2, 1)
)
if mibBuilder.loadTexts:
    cpqiScsiInstanceAttributesTable.setStatus("mandatory")
_CpqiScsiInstanceAttributesEntry_Object = MibTableRow
cpqiScsiInstanceAttributesEntry = _CpqiScsiInstanceAttributesEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 169, 2, 2, 1, 1)
)
cpqiScsiInstanceAttributesEntry.setIndexNames(
    (0, "CPQISCSI-MIB", "cpqiScsiInstIndex"),
)
if mibBuilder.loadTexts:
    cpqiScsiInstanceAttributesEntry.setStatus("mandatory")
_CpqiScsiInstIndex_Type = Gauge32
_CpqiScsiInstIndex_Object = MibTableColumn
cpqiScsiInstIndex = _CpqiScsiInstIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 169, 2, 2, 1, 1, 1),
    _CpqiScsiInstIndex_Type()
)
cpqiScsiInstIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqiScsiInstIndex.setStatus("mandatory")
_CpqiScsiInstDescr_Type = DisplayString
_CpqiScsiInstDescr_Object = MibTableColumn
cpqiScsiInstDescr = _CpqiScsiInstDescr_Object(
    (1, 3, 6, 1, 4, 1, 232, 169, 2, 2, 1, 1, 2),
    _CpqiScsiInstDescr_Type()
)
cpqiScsiInstDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqiScsiInstDescr.setStatus("mandatory")


class _CpqiScsiInstVersionMin_Type(Integer32):
    """Custom type cpqiScsiInstVersionMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CpqiScsiInstVersionMin_Type.__name__ = "Integer32"
_CpqiScsiInstVersionMin_Object = MibTableColumn
cpqiScsiInstVersionMin = _CpqiScsiInstVersionMin_Object(
    (1, 3, 6, 1, 4, 1, 232, 169, 2, 2, 1, 1, 3),
    _CpqiScsiInstVersionMin_Type()
)
cpqiScsiInstVersionMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqiScsiInstVersionMin.setStatus("mandatory")


class _CpqiScsiInstVersionMax_Type(Integer32):
    """Custom type cpqiScsiInstVersionMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CpqiScsiInstVersionMax_Type.__name__ = "Integer32"
_CpqiScsiInstVersionMax_Object = MibTableColumn
cpqiScsiInstVersionMax = _CpqiScsiInstVersionMax_Object(
    (1, 3, 6, 1, 4, 1, 232, 169, 2, 2, 1, 1, 4),
    _CpqiScsiInstVersionMax_Type()
)
cpqiScsiInstVersionMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqiScsiInstVersionMax.setStatus("mandatory")
_CpqiScsiInstVendorID_Type = DisplayString
_CpqiScsiInstVendorID_Object = MibTableColumn
cpqiScsiInstVendorID = _CpqiScsiInstVendorID_Object(
    (1, 3, 6, 1, 4, 1, 232, 169, 2, 2, 1, 1, 5),
    _CpqiScsiInstVendorID_Type()
)
cpqiScsiInstVendorID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqiScsiInstVendorID.setStatus("mandatory")
_CpqiScsiInstVendorVersion_Type = DisplayString
_CpqiScsiInstVendorVersion_Object = MibTableColumn
cpqiScsiInstVendorVersion = _CpqiScsiInstVendorVersion_Object(
    (1, 3, 6, 1, 4, 1, 232, 169, 2, 2, 1, 1, 6),
    _CpqiScsiInstVendorVersion_Type()
)
cpqiScsiInstVendorVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqiScsiInstVendorVersion.setStatus("mandatory")
_CpqiScsiInstPortalNumber_Type = Gauge32
_CpqiScsiInstPortalNumber_Object = MibTableColumn
cpqiScsiInstPortalNumber = _CpqiScsiInstPortalNumber_Object(
    (1, 3, 6, 1, 4, 1, 232, 169, 2, 2, 1, 1, 7),
    _CpqiScsiInstPortalNumber_Type()
)
cpqiScsiInstPortalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqiScsiInstPortalNumber.setStatus("mandatory")
_CpqiScsiInstNodeNumber_Type = Gauge32
_CpqiScsiInstNodeNumber_Object = MibTableColumn
cpqiScsiInstNodeNumber = _CpqiScsiInstNodeNumber_Object(
    (1, 3, 6, 1, 4, 1, 232, 169, 2, 2, 1, 1, 8),
    _CpqiScsiInstNodeNumber_Type()
)
cpqiScsiInstNodeNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqiScsiInstNodeNumber.setStatus("mandatory")
_CpqiScsiInstSessionNumber_Type = Gauge32
_CpqiScsiInstSessionNumber_Object = MibTableColumn
cpqiScsiInstSessionNumber = _CpqiScsiInstSessionNumber_Object(
    (1, 3, 6, 1, 4, 1, 232, 169, 2, 2, 1, 1, 9),
    _CpqiScsiInstSessionNumber_Type()
)
cpqiScsiInstSessionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqiScsiInstSessionNumber.setStatus("mandatory")
_CpqiScsiInstSsnFailures_Type = Counter32
_CpqiScsiInstSsnFailures_Object = MibTableColumn
cpqiScsiInstSsnFailures = _CpqiScsiInstSsnFailures_Object(
    (1, 3, 6, 1, 4, 1, 232, 169, 2, 2, 1, 1, 10),
    _CpqiScsiInstSsnFailures_Type()
)
cpqiScsiInstSsnFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqiScsiInstSsnFailures.setStatus("mandatory")
_CpqiScsiInstLastSsnFailureType_Type = ObjectIdentifier
_CpqiScsiInstLastSsnFailureType_Object = MibTableColumn
cpqiScsiInstLastSsnFailureType = _CpqiScsiInstLastSsnFailureType_Object(
    (1, 3, 6, 1, 4, 1, 232, 169, 2, 2, 1, 1, 11),
    _CpqiScsiInstLastSsnFailureType_Type()
)
cpqiScsiInstLastSsnFailureType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqiScsiInstLastSsnFailureType.setStatus("mandatory")
_CpqiScsiInstLastSsnRmtNodeName_Type = DisplayString
_CpqiScsiInstLastSsnRmtNodeName_Object = MibTableColumn
cpqiScsiInstLastSsnRmtNodeName = _CpqiScsiInstLastSsnRmtNodeName_Object(
    (1, 3, 6, 1, 4, 1, 232, 169, 2, 2, 1, 1, 12),
    _CpqiScsiInstLastSsnRmtNodeName_Type()
)
cpqiScsiInstLastSsnRmtNodeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqiScsiInstLastSsnRmtNodeName.setStatus("mandatory")
_CpqiScsiInstanceSsnErrorStatsTable_Object = MibTable
cpqiScsiInstanceSsnErrorStatsTable = _CpqiScsiInstanceSsnErrorStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 169, 2, 2, 2)
)
if mibBuilder.loadTexts:
    cpqiScsiInstanceSsnErrorStatsTable.setStatus("mandatory")
_CpqiScsiInstanceSsnErrorStatsEntry_Object = MibTableRow
cpqiScsiInstanceSsnErrorStatsEntry = _CpqiScsiInstanceSsnErrorStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 169, 2, 2, 2, 1)
)
cpqiScsiInstanceSsnErrorStatsEntry.setIndexNames(
    (0, "CPQISCSI-MIB", "cpqiScsiInstIndex"),
)
if mibBuilder.loadTexts:
    cpqiScsiInstanceSsnErrorStatsEntry.setStatus("mandatory")
_CpqiScsiInstSsnInstIndex_Type = Gauge32
_CpqiScsiInstSsnInstIndex_Object = MibTableColumn
cpqiScsiInstSsnInstIndex = _CpqiScsiInstSsnInstIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 169, 2, 2, 2, 1, 1),
    _CpqiScsiInstSsnInstIndex_Type()
)
cpqiScsiInstSsnInstIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqiScsiInstSsnInstIndex.setStatus("mandatory")
_CpqiScsiInstSsnDigestErrors_Type = Counter32
_CpqiScsiInstSsnDigestErrors_Object = MibTableColumn
cpqiScsiInstSsnDigestErrors = _CpqiScsiInstSsnDigestErrors_Object(
    (1, 3, 6, 1, 4, 1, 232, 169, 2, 2, 2, 1, 2),
    _CpqiScsiInstSsnDigestErrors_Type()
)
cpqiScsiInstSsnDigestErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqiScsiInstSsnDigestErrors.setStatus("mandatory")
_CpqiScsiInstSsnCxnTimeoutErrors_Type = Counter32
_CpqiScsiInstSsnCxnTimeoutErrors_Object = MibTableColumn
cpqiScsiInstSsnCxnTimeoutErrors = _CpqiScsiInstSsnCxnTimeoutErrors_Object(
    (1, 3, 6, 1, 4, 1, 232, 169, 2, 2, 2, 1, 3),
    _CpqiScsiInstSsnCxnTimeoutErrors_Type()
)
cpqiScsiInstSsnCxnTimeoutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqiScsiInstSsnCxnTimeoutErrors.setStatus("mandatory")
_CpqiScsiInstSsnFormatErrors_Type = Counter32
_CpqiScsiInstSsnFormatErrors_Object = MibTableColumn
cpqiScsiInstSsnFormatErrors = _CpqiScsiInstSsnFormatErrors_Object(
    (1, 3, 6, 1, 4, 1, 232, 169, 2, 2, 2, 1, 4),
    _CpqiScsiInstSsnFormatErrors_Type()
)
cpqiScsiInstSsnFormatErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqiScsiInstSsnFormatErrors.setStatus("mandatory")
_CpqiScsiPortal_ObjectIdentity = ObjectIdentity
cpqiScsiPortal = _CpqiScsiPortal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 169, 2, 3)
)
_CpqiScsiPortalAttributesTable_Object = MibTable
cpqiScsiPortalAttributesTable = _CpqiScsiPortalAttributesTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 169, 2, 3, 1)
)
if mibBuilder.loadTexts:
    cpqiScsiPortalAttributesTable.setStatus("mandatory")
_CpqiScsiPortalAttributesEntry_Object = MibTableRow
cpqiScsiPortalAttributesEntry = _CpqiScsiPortalAttributesEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 169, 2, 3, 1, 1)
)
cpqiScsiPortalAttributesEntry.setIndexNames(
    (0, "CPQISCSI-MIB", "cpqiScsiInstIndex"),
    (0, "CPQISCSI-MIB", "cpqiScsiPortalIndex"),
)
if mibBuilder.loadTexts:
    cpqiScsiPortalAttributesEntry.setStatus("mandatory")
_CpqiScsiPortalInstIndex_Type = Gauge32
_CpqiScsiPortalInstIndex_Object = MibTableColumn
cpqiScsiPortalInstIndex = _CpqiScsiPortalInstIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 169, 2, 3, 1, 1, 1),
    _CpqiScsiPortalInstIndex_Type()
)
cpqiScsiPortalInstIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqiScsiPortalInstIndex.setStatus("mandatory")
_CpqiScsiPortalIndex_Type = Gauge32
_CpqiScsiPortalIndex_Object = MibTableColumn
cpqiScsiPortalIndex = _CpqiScsiPortalIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 169, 2, 3, 1, 1, 2),
    _CpqiScsiPortalIndex_Type()
)
cpqiScsiPortalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqiScsiPortalIndex.setStatus("mandatory")


class _CpqiScsiPortalRowStatus_Type(Integer32):
    """Custom type cpqiScsiPortalRowStatus based on Integer32"""
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
        *(("active", 1),
          ("notInService", 2),
          ("notReady", 3),
          ("createAndGo", 4),
          ("createAndWait", 5),
          ("destroy", 6))
    )


_CpqiScsiPortalRowStatus_Type.__name__ = "Integer32"
_CpqiScsiPortalRowStatus_Object = MibTableColumn
cpqiScsiPortalRowStatus = _CpqiScsiPortalRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 169, 2, 3, 1, 1, 3),
    _CpqiScsiPortalRowStatus_Type()
)
cpqiScsiPortalRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqiScsiPortalRowStatus.setStatus("mandatory")


class _CpqiScsiPortalRoles_Type(OctetString):
    """Custom type cpqiScsiPortalRoles based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 2),
    )


_CpqiScsiPortalRoles_Type.__name__ = "OctetString"
_CpqiScsiPortalRoles_Object = MibTableColumn
cpqiScsiPortalRoles = _CpqiScsiPortalRoles_Object(
    (1, 3, 6, 1, 4, 1, 232, 169, 2, 3, 1, 1, 4),
    _CpqiScsiPortalRoles_Type()
)
cpqiScsiPortalRoles.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqiScsiPortalRoles.setStatus("mandatory")


class _CpqiScsiPortalAddrType_Type(Integer32):
    """Custom type cpqiScsiPortalAddrType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              16)
        )
    )
    namedValues = NamedValues(
        *(("ipv4", 1),
          ("ipv6", 2),
          ("ipv4z", 3),
          ("ipv6z", 4),
          ("dns", 16))
    )


_CpqiScsiPortalAddrType_Type.__name__ = "Integer32"
_CpqiScsiPortalAddrType_Object = MibTableColumn
cpqiScsiPortalAddrType = _CpqiScsiPortalAddrType_Object(
    (1, 3, 6, 1, 4, 1, 232, 169, 2, 3, 1, 1, 5),
    _CpqiScsiPortalAddrType_Type()
)
cpqiScsiPortalAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqiScsiPortalAddrType.setStatus("mandatory")


class _CpqiScsiPortalAddr_Type(OctetString):
    """Custom type cpqiScsiPortalAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqiScsiPortalAddr_Type.__name__ = "OctetString"
_CpqiScsiPortalAddr_Object = MibTableColumn
cpqiScsiPortalAddr = _CpqiScsiPortalAddr_Object(
    (1, 3, 6, 1, 4, 1, 232, 169, 2, 3, 1, 1, 6),
    _CpqiScsiPortalAddr_Type()
)
cpqiScsiPortalAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqiScsiPortalAddr.setStatus("mandatory")


class _CpqiScsiPortalProtocol_Type(Integer32):
    """Custom type cpqiScsiPortalProtocol based on Integer32"""
    defaultValue = 6

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
        *(("icmp", 1),
          ("igmp", 2),
          ("ggp", 3),
          ("ip", 4),
          ("st", 5),
          ("tcp", 6))
    )


_CpqiScsiPortalProtocol_Type.__name__ = "Integer32"
_CpqiScsiPortalProtocol_Object = MibTableColumn
cpqiScsiPortalProtocol = _CpqiScsiPortalProtocol_Object(
    (1, 3, 6, 1, 4, 1, 232, 169, 2, 3, 1, 1, 7),
    _CpqiScsiPortalProtocol_Type()
)
cpqiScsiPortalProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqiScsiPortalProtocol.setStatus("mandatory")


class _CpqiScsiPortalMaxRecvDataSegLength_Type(Integer32):
    """Custom type cpqiScsiPortalMaxRecvDataSegLength based on Integer32"""
    defaultValue = 8192

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(512, 16777215),
    )


_CpqiScsiPortalMaxRecvDataSegLength_Type.__name__ = "Integer32"
_CpqiScsiPortalMaxRecvDataSegLength_Object = MibTableColumn
cpqiScsiPortalMaxRecvDataSegLength = _CpqiScsiPortalMaxRecvDataSegLength_Object(
    (1, 3, 6, 1, 4, 1, 232, 169, 2, 3, 1, 1, 8),
    _CpqiScsiPortalMaxRecvDataSegLength_Type()
)
cpqiScsiPortalMaxRecvDataSegLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqiScsiPortalMaxRecvDataSegLength.setStatus("mandatory")


class _CpqiScsiPortalPrimaryHdrDigest_Type(Integer32):
    """Custom type cpqiScsiPortalPrimaryHdrDigest based on Integer32"""
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
        *(("none", 1),
          ("other", 2),
          ("noDigest", 3),
          ("crc32c", 4))
    )


_CpqiScsiPortalPrimaryHdrDigest_Type.__name__ = "Integer32"
_CpqiScsiPortalPrimaryHdrDigest_Object = MibTableColumn
cpqiScsiPortalPrimaryHdrDigest = _CpqiScsiPortalPrimaryHdrDigest_Object(
    (1, 3, 6, 1, 4, 1, 232, 169, 2, 3, 1, 1, 9),
    _CpqiScsiPortalPrimaryHdrDigest_Type()
)
cpqiScsiPortalPrimaryHdrDigest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqiScsiPortalPrimaryHdrDigest.setStatus("mandatory")


class _CpqiScsiPortalPrimaryDataDigest_Type(Integer32):
    """Custom type cpqiScsiPortalPrimaryDataDigest based on Integer32"""
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
        *(("none", 1),
          ("other", 2),
          ("noDigest", 3),
          ("crc32c", 4))
    )


_CpqiScsiPortalPrimaryDataDigest_Type.__name__ = "Integer32"
_CpqiScsiPortalPrimaryDataDigest_Object = MibTableColumn
cpqiScsiPortalPrimaryDataDigest = _CpqiScsiPortalPrimaryDataDigest_Object(
    (1, 3, 6, 1, 4, 1, 232, 169, 2, 3, 1, 1, 10),
    _CpqiScsiPortalPrimaryDataDigest_Type()
)
cpqiScsiPortalPrimaryDataDigest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqiScsiPortalPrimaryDataDigest.setStatus("mandatory")


class _CpqiScsiPortalSecondaryHdrDigest_Type(Integer32):
    """Custom type cpqiScsiPortalSecondaryHdrDigest based on Integer32"""
    defaultValue = 3

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
          ("other", 2),
          ("noDigest", 3),
          ("crc32c", 4))
    )


_CpqiScsiPortalSecondaryHdrDigest_Type.__name__ = "Integer32"
_CpqiScsiPortalSecondaryHdrDigest_Object = MibTableColumn
cpqiScsiPortalSecondaryHdrDigest = _CpqiScsiPortalSecondaryHdrDigest_Object(
    (1, 3, 6, 1, 4, 1, 232, 169, 2, 3, 1, 1, 11),
    _CpqiScsiPortalSecondaryHdrDigest_Type()
)
cpqiScsiPortalSecondaryHdrDigest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqiScsiPortalSecondaryHdrDigest.setStatus("mandatory")


class _CpqiScsiPortalSecondaryDataDigest_Type(Integer32):
    """Custom type cpqiScsiPortalSecondaryDataDigest based on Integer32"""
    defaultValue = 3

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
          ("other", 2),
          ("noDigest", 3),
          ("crc32c", 4))
    )


_CpqiScsiPortalSecondaryDataDigest_Type.__name__ = "Integer32"
_CpqiScsiPortalSecondaryDataDigest_Object = MibTableColumn
cpqiScsiPortalSecondaryDataDigest = _CpqiScsiPortalSecondaryDataDigest_Object(
    (1, 3, 6, 1, 4, 1, 232, 169, 2, 3, 1, 1, 12),
    _CpqiScsiPortalSecondaryDataDigest_Type()
)
cpqiScsiPortalSecondaryDataDigest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqiScsiPortalSecondaryDataDigest.setStatus("mandatory")


class _CpqiScsiPortalRecvMarker_Type(Integer32):
    """Custom type cpqiScsiPortalRecvMarker based on Integer32"""
    defaultValue = 2

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


_CpqiScsiPortalRecvMarker_Type.__name__ = "Integer32"
_CpqiScsiPortalRecvMarker_Object = MibTableColumn
cpqiScsiPortalRecvMarker = _CpqiScsiPortalRecvMarker_Object(
    (1, 3, 6, 1, 4, 1, 232, 169, 2, 3, 1, 1, 13),
    _CpqiScsiPortalRecvMarker_Type()
)
cpqiScsiPortalRecvMarker.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqiScsiPortalRecvMarker.setStatus("mandatory")
_CpqiScsiTargetPortal_ObjectIdentity = ObjectIdentity
cpqiScsiTargetPortal = _CpqiScsiTargetPortal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 169, 2, 4)
)
_CpqiScsiTgtPortalAttributesTable_Object = MibTable
cpqiScsiTgtPortalAttributesTable = _CpqiScsiTgtPortalAttributesTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 169, 2, 4, 1)
)
if mibBuilder.loadTexts:
    cpqiScsiTgtPortalAttributesTable.setStatus("mandatory")
_CpqiScsiTgtPortalAttributesEntry_Object = MibTableRow
cpqiScsiTgtPortalAttributesEntry = _CpqiScsiTgtPortalAttributesEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 169, 2, 4, 1, 1)
)
cpqiScsiTgtPortalAttributesEntry.setIndexNames(
    (0, "CPQISCSI-MIB", "cpqiScsiInstIndex"),
    (0, "CPQISCSI-MIB", "cpqiScsiPortalIndex"),
)
if mibBuilder.loadTexts:
    cpqiScsiTgtPortalAttributesEntry.setStatus("mandatory")
_CpqiScsiTgtPortalInstIndex_Type = Gauge32
_CpqiScsiTgtPortalInstIndex_Object = MibTableColumn
cpqiScsiTgtPortalInstIndex = _CpqiScsiTgtPortalInstIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 169, 2, 4, 1, 1, 1),
    _CpqiScsiTgtPortalInstIndex_Type()
)
cpqiScsiTgtPortalInstIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqiScsiTgtPortalInstIndex.setStatus("mandatory")
_CpqiScsiTgtPortalPortalIndex_Type = Gauge32
_CpqiScsiTgtPortalPortalIndex_Object = MibTableColumn
cpqiScsiTgtPortalPortalIndex = _CpqiScsiTgtPortalPortalIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 169, 2, 4, 1, 1, 2),
    _CpqiScsiTgtPortalPortalIndex_Type()
)
cpqiScsiTgtPortalPortalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqiScsiTgtPortalPortalIndex.setStatus("mandatory")
_CpqiScsiTgtPortalPort_Type = Gauge32
_CpqiScsiTgtPortalPort_Object = MibTableColumn
cpqiScsiTgtPortalPort = _CpqiScsiTgtPortalPort_Object(
    (1, 3, 6, 1, 4, 1, 232, 169, 2, 4, 1, 1, 3),
    _CpqiScsiTgtPortalPort_Type()
)
cpqiScsiTgtPortalPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqiScsiTgtPortalPort.setStatus("mandatory")


class _CpqiScsiTgtPortalTag_Type(Integer32):
    """Custom type cpqiScsiTgtPortalTag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CpqiScsiTgtPortalTag_Type.__name__ = "Integer32"
_CpqiScsiTgtPortalTag_Object = MibTableColumn
cpqiScsiTgtPortalTag = _CpqiScsiTgtPortalTag_Object(
    (1, 3, 6, 1, 4, 1, 232, 169, 2, 4, 1, 1, 4),
    _CpqiScsiTgtPortalTag_Type()
)
cpqiScsiTgtPortalTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqiScsiTgtPortalTag.setStatus("mandatory")
_CpqiScsiInitiatorPortal_ObjectIdentity = ObjectIdentity
cpqiScsiInitiatorPortal = _CpqiScsiInitiatorPortal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 169, 2, 5)
)
_CpqiScsiIntrPortalAttributesTable_Object = MibTable
cpqiScsiIntrPortalAttributesTable = _CpqiScsiIntrPortalAttributesTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 169, 2, 5, 1)
)
if mibBuilder.loadTexts:
    cpqiScsiIntrPortalAttributesTable.setStatus("mandatory")
_CpqiScsiIntrPortalAttributesEntry_Object = MibTableRow
cpqiScsiIntrPortalAttributesEntry = _CpqiScsiIntrPortalAttributesEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 169, 2, 5, 1, 1)
)
cpqiScsiIntrPortalAttributesEntry.setIndexNames(
    (0, "CPQISCSI-MIB", "cpqiScsiInstIndex"),
    (0, "CPQISCSI-MIB", "cpqiScsiPortalIndex"),
)
if mibBuilder.loadTexts:
    cpqiScsiIntrPortalAttributesEntry.setStatus("mandatory")
_CpqiScsiIntrPortalInstIndex_Type = Gauge32
_CpqiScsiIntrPortalInstIndex_Object = MibTableColumn
cpqiScsiIntrPortalInstIndex = _CpqiScsiIntrPortalInstIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 169, 2, 5, 1, 1, 1),
    _CpqiScsiIntrPortalInstIndex_Type()
)
cpqiScsiIntrPortalInstIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqiScsiIntrPortalInstIndex.setStatus("mandatory")
_CpqiScsiIntrPortalPortalIndex_Type = Gauge32
_CpqiScsiIntrPortalPortalIndex_Object = MibTableColumn
cpqiScsiIntrPortalPortalIndex = _CpqiScsiIntrPortalPortalIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 169, 2, 5, 1, 1, 2),
    _CpqiScsiIntrPortalPortalIndex_Type()
)
cpqiScsiIntrPortalPortalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqiScsiIntrPortalPortalIndex.setStatus("mandatory")


class _CpqiScsiIntrPortalTag_Type(Integer32):
    """Custom type cpqiScsiIntrPortalTag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CpqiScsiIntrPortalTag_Type.__name__ = "Integer32"
_CpqiScsiIntrPortalTag_Object = MibTableColumn
cpqiScsiIntrPortalTag = _CpqiScsiIntrPortalTag_Object(
    (1, 3, 6, 1, 4, 1, 232, 169, 2, 5, 1, 1, 3),
    _CpqiScsiIntrPortalTag_Type()
)
cpqiScsiIntrPortalTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqiScsiIntrPortalTag.setStatus("mandatory")
_CpqiScsiNode_ObjectIdentity = ObjectIdentity
cpqiScsiNode = _CpqiScsiNode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 169, 2, 6)
)
_CpqiScsiNodeAttributesTable_Object = MibTable
cpqiScsiNodeAttributesTable = _CpqiScsiNodeAttributesTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 169, 2, 6, 1)
)
if mibBuilder.loadTexts:
    cpqiScsiNodeAttributesTable.setStatus("mandatory")
_CpqiScsiNodeAttributesEntry_Object = MibTableRow
cpqiScsiNodeAttributesEntry = _CpqiScsiNodeAttributesEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 169, 2, 6, 1, 1)
)
cpqiScsiNodeAttributesEntry.setIndexNames(
    (0, "CPQISCSI-MIB", "cpqiScsiNodeInstIndex"),
    (0, "CPQISCSI-MIB", "cpqiScsiNodeNodeIndex"),
)
if mibBuilder.loadTexts:
    cpqiScsiNodeAttributesEntry.setStatus("mandatory")
_CpqiScsiNodeInstIndex_Type = Gauge32
_CpqiScsiNodeInstIndex_Object = MibTableColumn
cpqiScsiNodeInstIndex = _CpqiScsiNodeInstIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 169, 2, 6, 1, 1, 1),
    _CpqiScsiNodeInstIndex_Type()
)
cpqiScsiNodeInstIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqiScsiNodeInstIndex.setStatus("mandatory")
_CpqiScsiNodeNodeIndex_Type = Gauge32
_CpqiScsiNodeNodeIndex_Object = MibTableColumn
cpqiScsiNodeNodeIndex = _CpqiScsiNodeNodeIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 169, 2, 6, 1, 1, 2),
    _CpqiScsiNodeNodeIndex_Type()
)
cpqiScsiNodeNodeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqiScsiNodeNodeIndex.setStatus("mandatory")
_CpqiScsiNodeName_Type = DisplayString
_CpqiScsiNodeName_Object = MibTableColumn
cpqiScsiNodeName = _CpqiScsiNodeName_Object(
    (1, 3, 6, 1, 4, 1, 232, 169, 2, 6, 1, 1, 3),
    _CpqiScsiNodeName_Type()
)
cpqiScsiNodeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqiScsiNodeName.setStatus("mandatory")
_CpqiScsiNodeAlias_Type = DisplayString
_CpqiScsiNodeAlias_Object = MibTableColumn
cpqiScsiNodeAlias = _CpqiScsiNodeAlias_Object(
    (1, 3, 6, 1, 4, 1, 232, 169, 2, 6, 1, 1, 4),
    _CpqiScsiNodeAlias_Type()
)
cpqiScsiNodeAlias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqiScsiNodeAlias.setStatus("mandatory")


class _CpqiScsiNodeRoles_Type(OctetString):
    """Custom type cpqiScsiNodeRoles based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 2),
    )


_CpqiScsiNodeRoles_Type.__name__ = "OctetString"
_CpqiScsiNodeRoles_Object = MibTableColumn
cpqiScsiNodeRoles = _CpqiScsiNodeRoles_Object(
    (1, 3, 6, 1, 4, 1, 232, 169, 2, 6, 1, 1, 5),
    _CpqiScsiNodeRoles_Type()
)
cpqiScsiNodeRoles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqiScsiNodeRoles.setStatus("mandatory")
_CpqiScsiNodeTransportType_Type = ObjectIdentifier
_CpqiScsiNodeTransportType_Object = MibTableColumn
cpqiScsiNodeTransportType = _CpqiScsiNodeTransportType_Object(
    (1, 3, 6, 1, 4, 1, 232, 169, 2, 6, 1, 1, 6),
    _CpqiScsiNodeTransportType_Type()
)
cpqiScsiNodeTransportType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqiScsiNodeTransportType.setStatus("mandatory")


class _CpqiScsiNodeInitialR2T_Type(Integer32):
    """Custom type cpqiScsiNodeInitialR2T based on Integer32"""
    defaultValue = 1

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


_CpqiScsiNodeInitialR2T_Type.__name__ = "Integer32"
_CpqiScsiNodeInitialR2T_Object = MibTableColumn
cpqiScsiNodeInitialR2T = _CpqiScsiNodeInitialR2T_Object(
    (1, 3, 6, 1, 4, 1, 232, 169, 2, 6, 1, 1, 7),
    _CpqiScsiNodeInitialR2T_Type()
)
cpqiScsiNodeInitialR2T.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqiScsiNodeInitialR2T.setStatus("mandatory")


class _CpqiScsiNodeImmediateData_Type(Integer32):
    """Custom type cpqiScsiNodeImmediateData based on Integer32"""
    defaultValue = 1

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


_CpqiScsiNodeImmediateData_Type.__name__ = "Integer32"
_CpqiScsiNodeImmediateData_Object = MibTableColumn
cpqiScsiNodeImmediateData = _CpqiScsiNodeImmediateData_Object(
    (1, 3, 6, 1, 4, 1, 232, 169, 2, 6, 1, 1, 8),
    _CpqiScsiNodeImmediateData_Type()
)
cpqiScsiNodeImmediateData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqiScsiNodeImmediateData.setStatus("mandatory")


class _CpqiScsiNodeMaxOutstandingR2T_Type(Integer32):
    """Custom type cpqiScsiNodeMaxOutstandingR2T based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CpqiScsiNodeMaxOutstandingR2T_Type.__name__ = "Integer32"
_CpqiScsiNodeMaxOutstandingR2T_Object = MibTableColumn
cpqiScsiNodeMaxOutstandingR2T = _CpqiScsiNodeMaxOutstandingR2T_Object(
    (1, 3, 6, 1, 4, 1, 232, 169, 2, 6, 1, 1, 9),
    _CpqiScsiNodeMaxOutstandingR2T_Type()
)
cpqiScsiNodeMaxOutstandingR2T.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqiScsiNodeMaxOutstandingR2T.setStatus("mandatory")


class _CpqiScsiNodeFirstBurstLength_Type(Integer32):
    """Custom type cpqiScsiNodeFirstBurstLength based on Integer32"""
    defaultValue = 65536

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(512, 16777215),
    )


_CpqiScsiNodeFirstBurstLength_Type.__name__ = "Integer32"
_CpqiScsiNodeFirstBurstLength_Object = MibTableColumn
cpqiScsiNodeFirstBurstLength = _CpqiScsiNodeFirstBurstLength_Object(
    (1, 3, 6, 1, 4, 1, 232, 169, 2, 6, 1, 1, 10),
    _CpqiScsiNodeFirstBurstLength_Type()
)
cpqiScsiNodeFirstBurstLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqiScsiNodeFirstBurstLength.setStatus("mandatory")


class _CpqiScsiNodeMaxBurstLength_Type(Integer32):
    """Custom type cpqiScsiNodeMaxBurstLength based on Integer32"""
    defaultValue = 262144

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(512, 16777215),
    )


_CpqiScsiNodeMaxBurstLength_Type.__name__ = "Integer32"
_CpqiScsiNodeMaxBurstLength_Object = MibTableColumn
cpqiScsiNodeMaxBurstLength = _CpqiScsiNodeMaxBurstLength_Object(
    (1, 3, 6, 1, 4, 1, 232, 169, 2, 6, 1, 1, 11),
    _CpqiScsiNodeMaxBurstLength_Type()
)
cpqiScsiNodeMaxBurstLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqiScsiNodeMaxBurstLength.setStatus("mandatory")


class _CpqiScsiNodeMaxConnections_Type(Integer32):
    """Custom type cpqiScsiNodeMaxConnections based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CpqiScsiNodeMaxConnections_Type.__name__ = "Integer32"
_CpqiScsiNodeMaxConnections_Object = MibTableColumn
cpqiScsiNodeMaxConnections = _CpqiScsiNodeMaxConnections_Object(
    (1, 3, 6, 1, 4, 1, 232, 169, 2, 6, 1, 1, 12),
    _CpqiScsiNodeMaxConnections_Type()
)
cpqiScsiNodeMaxConnections.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqiScsiNodeMaxConnections.setStatus("mandatory")


class _CpqiScsiNodeDataSequenceInOrder_Type(Integer32):
    """Custom type cpqiScsiNodeDataSequenceInOrder based on Integer32"""
    defaultValue = 1

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


_CpqiScsiNodeDataSequenceInOrder_Type.__name__ = "Integer32"
_CpqiScsiNodeDataSequenceInOrder_Object = MibTableColumn
cpqiScsiNodeDataSequenceInOrder = _CpqiScsiNodeDataSequenceInOrder_Object(
    (1, 3, 6, 1, 4, 1, 232, 169, 2, 6, 1, 1, 13),
    _CpqiScsiNodeDataSequenceInOrder_Type()
)
cpqiScsiNodeDataSequenceInOrder.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqiScsiNodeDataSequenceInOrder.setStatus("mandatory")


class _CpqiScsiNodeDataPDUInOrder_Type(Integer32):
    """Custom type cpqiScsiNodeDataPDUInOrder based on Integer32"""
    defaultValue = 1

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


_CpqiScsiNodeDataPDUInOrder_Type.__name__ = "Integer32"
_CpqiScsiNodeDataPDUInOrder_Object = MibTableColumn
cpqiScsiNodeDataPDUInOrder = _CpqiScsiNodeDataPDUInOrder_Object(
    (1, 3, 6, 1, 4, 1, 232, 169, 2, 6, 1, 1, 14),
    _CpqiScsiNodeDataPDUInOrder_Type()
)
cpqiScsiNodeDataPDUInOrder.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqiScsiNodeDataPDUInOrder.setStatus("mandatory")


class _CpqiScsiNodeDefaultTime2Wait_Type(Integer32):
    """Custom type cpqiScsiNodeDefaultTime2Wait based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_CpqiScsiNodeDefaultTime2Wait_Type.__name__ = "Integer32"
_CpqiScsiNodeDefaultTime2Wait_Object = MibTableColumn
cpqiScsiNodeDefaultTime2Wait = _CpqiScsiNodeDefaultTime2Wait_Object(
    (1, 3, 6, 1, 4, 1, 232, 169, 2, 6, 1, 1, 15),
    _CpqiScsiNodeDefaultTime2Wait_Type()
)
cpqiScsiNodeDefaultTime2Wait.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqiScsiNodeDefaultTime2Wait.setStatus("mandatory")


class _CpqiScsiNodeDefaultTime2Retain_Type(Integer32):
    """Custom type cpqiScsiNodeDefaultTime2Retain based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_CpqiScsiNodeDefaultTime2Retain_Type.__name__ = "Integer32"
_CpqiScsiNodeDefaultTime2Retain_Object = MibTableColumn
cpqiScsiNodeDefaultTime2Retain = _CpqiScsiNodeDefaultTime2Retain_Object(
    (1, 3, 6, 1, 4, 1, 232, 169, 2, 6, 1, 1, 16),
    _CpqiScsiNodeDefaultTime2Retain_Type()
)
cpqiScsiNodeDefaultTime2Retain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqiScsiNodeDefaultTime2Retain.setStatus("mandatory")


class _CpqiScsiNodeErrorRecoveryLevel_Type(Integer32):
    """Custom type cpqiScsiNodeErrorRecoveryLevel based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CpqiScsiNodeErrorRecoveryLevel_Type.__name__ = "Integer32"
_CpqiScsiNodeErrorRecoveryLevel_Object = MibTableColumn
cpqiScsiNodeErrorRecoveryLevel = _CpqiScsiNodeErrorRecoveryLevel_Object(
    (1, 3, 6, 1, 4, 1, 232, 169, 2, 6, 1, 1, 17),
    _CpqiScsiNodeErrorRecoveryLevel_Type()
)
cpqiScsiNodeErrorRecoveryLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqiScsiNodeErrorRecoveryLevel.setStatus("mandatory")
_CpqiScsiTarget_ObjectIdentity = ObjectIdentity
cpqiScsiTarget = _CpqiScsiTarget_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 169, 2, 7)
)
_CpqiScsiTargetAttributesTable_Object = MibTable
cpqiScsiTargetAttributesTable = _CpqiScsiTargetAttributesTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 169, 2, 7, 1)
)
if mibBuilder.loadTexts:
    cpqiScsiTargetAttributesTable.setStatus("mandatory")
_CpqiScsiTargetAttributesEntry_Object = MibTableRow
cpqiScsiTargetAttributesEntry = _CpqiScsiTargetAttributesEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 169, 2, 7, 1, 1)
)
cpqiScsiTargetAttributesEntry.setIndexNames(
    (0, "CPQISCSI-MIB", "cpqiScsiTgtInstIndex"),
    (0, "CPQISCSI-MIB", "cpqiScsiTgtNodeIndex"),
)
if mibBuilder.loadTexts:
    cpqiScsiTargetAttributesEntry.setStatus("mandatory")
_CpqiScsiTgtInstIndex_Type = Gauge32
_CpqiScsiTgtInstIndex_Object = MibTableColumn
cpqiScsiTgtInstIndex = _CpqiScsiTgtInstIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 169, 2, 7, 1, 1, 1),
    _CpqiScsiTgtInstIndex_Type()
)
cpqiScsiTgtInstIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqiScsiTgtInstIndex.setStatus("mandatory")
_CpqiScsiTgtNodeIndex_Type = Gauge32
_CpqiScsiTgtNodeIndex_Object = MibTableColumn
cpqiScsiTgtNodeIndex = _CpqiScsiTgtNodeIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 169, 2, 7, 1, 1, 2),
    _CpqiScsiTgtNodeIndex_Type()
)
cpqiScsiTgtNodeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqiScsiTgtNodeIndex.setStatus("mandatory")
_CpqiScsiTgtLoginFailures_Type = Counter32
_CpqiScsiTgtLoginFailures_Object = MibTableColumn
cpqiScsiTgtLoginFailures = _CpqiScsiTgtLoginFailures_Object(
    (1, 3, 6, 1, 4, 1, 232, 169, 2, 7, 1, 1, 3),
    _CpqiScsiTgtLoginFailures_Type()
)
cpqiScsiTgtLoginFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqiScsiTgtLoginFailures.setStatus("mandatory")
_CpqiScsiTgtLastFailureTime_Type = TimeTicks
_CpqiScsiTgtLastFailureTime_Object = MibTableColumn
cpqiScsiTgtLastFailureTime = _CpqiScsiTgtLastFailureTime_Object(
    (1, 3, 6, 1, 4, 1, 232, 169, 2, 7, 1, 1, 4),
    _CpqiScsiTgtLastFailureTime_Type()
)
cpqiScsiTgtLastFailureTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqiScsiTgtLastFailureTime.setStatus("mandatory")
_CpqiScsiTgtLastFailureType_Type = ObjectIdentifier
_CpqiScsiTgtLastFailureType_Object = MibTableColumn
cpqiScsiTgtLastFailureType = _CpqiScsiTgtLastFailureType_Object(
    (1, 3, 6, 1, 4, 1, 232, 169, 2, 7, 1, 1, 5),
    _CpqiScsiTgtLastFailureType_Type()
)
cpqiScsiTgtLastFailureType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqiScsiTgtLastFailureType.setStatus("mandatory")
_CpqiScsiTgtLastIntrFailureName_Type = DisplayString
_CpqiScsiTgtLastIntrFailureName_Object = MibTableColumn
cpqiScsiTgtLastIntrFailureName = _CpqiScsiTgtLastIntrFailureName_Object(
    (1, 3, 6, 1, 4, 1, 232, 169, 2, 7, 1, 1, 6),
    _CpqiScsiTgtLastIntrFailureName_Type()
)
cpqiScsiTgtLastIntrFailureName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqiScsiTgtLastIntrFailureName.setStatus("mandatory")


class _CpqiScsiTgtLastIntrFailureAddrType_Type(Integer32):
    """Custom type cpqiScsiTgtLastIntrFailureAddrType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              16)
        )
    )
    namedValues = NamedValues(
        *(("ipv4", 1),
          ("ipv6", 2),
          ("ipv4z", 3),
          ("ipv6z", 4),
          ("dns", 16))
    )


_CpqiScsiTgtLastIntrFailureAddrType_Type.__name__ = "Integer32"
_CpqiScsiTgtLastIntrFailureAddrType_Object = MibTableColumn
cpqiScsiTgtLastIntrFailureAddrType = _CpqiScsiTgtLastIntrFailureAddrType_Object(
    (1, 3, 6, 1, 4, 1, 232, 169, 2, 7, 1, 1, 7),
    _CpqiScsiTgtLastIntrFailureAddrType_Type()
)
cpqiScsiTgtLastIntrFailureAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqiScsiTgtLastIntrFailureAddrType.setStatus("mandatory")


class _CpqiScsiTgtLastIntrFailureAddr_Type(OctetString):
    """Custom type cpqiScsiTgtLastIntrFailureAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqiScsiTgtLastIntrFailureAddr_Type.__name__ = "OctetString"
_CpqiScsiTgtLastIntrFailureAddr_Object = MibTableColumn
cpqiScsiTgtLastIntrFailureAddr = _CpqiScsiTgtLastIntrFailureAddr_Object(
    (1, 3, 6, 1, 4, 1, 232, 169, 2, 7, 1, 1, 8),
    _CpqiScsiTgtLastIntrFailureAddr_Type()
)
cpqiScsiTgtLastIntrFailureAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqiScsiTgtLastIntrFailureAddr.setStatus("mandatory")
_CpqiScsiTargetLoginStatsTable_Object = MibTable
cpqiScsiTargetLoginStatsTable = _CpqiScsiTargetLoginStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 169, 2, 7, 2)
)
if mibBuilder.loadTexts:
    cpqiScsiTargetLoginStatsTable.setStatus("mandatory")
_CpqiScsiTargetLoginStatsEntry_Object = MibTableRow
cpqiScsiTargetLoginStatsEntry = _CpqiScsiTargetLoginStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 169, 2, 7, 2, 1)
)
cpqiScsiTargetLoginStatsEntry.setIndexNames(
    (0, "CPQISCSI-MIB", "cpqiScsiTgtLoginInstIndex"),
    (0, "CPQISCSI-MIB", "cpqiScsiTgtLoginNodeIndex"),
)
if mibBuilder.loadTexts:
    cpqiScsiTargetLoginStatsEntry.setStatus("mandatory")
_CpqiScsiTgtLoginInstIndex_Type = Gauge32
_CpqiScsiTgtLoginInstIndex_Object = MibTableColumn
cpqiScsiTgtLoginInstIndex = _CpqiScsiTgtLoginInstIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 169, 2, 7, 2, 1, 1),
    _CpqiScsiTgtLoginInstIndex_Type()
)
cpqiScsiTgtLoginInstIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqiScsiTgtLoginInstIndex.setStatus("mandatory")
_CpqiScsiTgtLoginNodeIndex_Type = Gauge32
_CpqiScsiTgtLoginNodeIndex_Object = MibTableColumn
cpqiScsiTgtLoginNodeIndex = _CpqiScsiTgtLoginNodeIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 169, 2, 7, 2, 1, 2),
    _CpqiScsiTgtLoginNodeIndex_Type()
)
cpqiScsiTgtLoginNodeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqiScsiTgtLoginNodeIndex.setStatus("mandatory")
_CpqiScsiTgtLoginAccepts_Type = Counter32
_CpqiScsiTgtLoginAccepts_Object = MibTableColumn
cpqiScsiTgtLoginAccepts = _CpqiScsiTgtLoginAccepts_Object(
    (1, 3, 6, 1, 4, 1, 232, 169, 2, 7, 2, 1, 3),
    _CpqiScsiTgtLoginAccepts_Type()
)
cpqiScsiTgtLoginAccepts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqiScsiTgtLoginAccepts.setStatus("mandatory")
_CpqiScsiTgtLoginOtherFails_Type = Counter32
_CpqiScsiTgtLoginOtherFails_Object = MibTableColumn
cpqiScsiTgtLoginOtherFails = _CpqiScsiTgtLoginOtherFails_Object(
    (1, 3, 6, 1, 4, 1, 232, 169, 2, 7, 2, 1, 4),
    _CpqiScsiTgtLoginOtherFails_Type()
)
cpqiScsiTgtLoginOtherFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqiScsiTgtLoginOtherFails.setStatus("mandatory")
_CpqiScsiTgtLoginRedirects_Type = Counter32
_CpqiScsiTgtLoginRedirects_Object = MibTableColumn
cpqiScsiTgtLoginRedirects = _CpqiScsiTgtLoginRedirects_Object(
    (1, 3, 6, 1, 4, 1, 232, 169, 2, 7, 2, 1, 5),
    _CpqiScsiTgtLoginRedirects_Type()
)
cpqiScsiTgtLoginRedirects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqiScsiTgtLoginRedirects.setStatus("mandatory")
_CpqiScsiTgtLoginAuthorizeFails_Type = Counter32
_CpqiScsiTgtLoginAuthorizeFails_Object = MibTableColumn
cpqiScsiTgtLoginAuthorizeFails = _CpqiScsiTgtLoginAuthorizeFails_Object(
    (1, 3, 6, 1, 4, 1, 232, 169, 2, 7, 2, 1, 6),
    _CpqiScsiTgtLoginAuthorizeFails_Type()
)
cpqiScsiTgtLoginAuthorizeFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqiScsiTgtLoginAuthorizeFails.setStatus("mandatory")
_CpqiScsiTgtLoginAuthenticateFails_Type = Counter32
_CpqiScsiTgtLoginAuthenticateFails_Object = MibTableColumn
cpqiScsiTgtLoginAuthenticateFails = _CpqiScsiTgtLoginAuthenticateFails_Object(
    (1, 3, 6, 1, 4, 1, 232, 169, 2, 7, 2, 1, 7),
    _CpqiScsiTgtLoginAuthenticateFails_Type()
)
cpqiScsiTgtLoginAuthenticateFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqiScsiTgtLoginAuthenticateFails.setStatus("mandatory")
_CpqiScsiTgtLoginNegotiateFails_Type = Counter32
_CpqiScsiTgtLoginNegotiateFails_Object = MibTableColumn
cpqiScsiTgtLoginNegotiateFails = _CpqiScsiTgtLoginNegotiateFails_Object(
    (1, 3, 6, 1, 4, 1, 232, 169, 2, 7, 2, 1, 8),
    _CpqiScsiTgtLoginNegotiateFails_Type()
)
cpqiScsiTgtLoginNegotiateFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqiScsiTgtLoginNegotiateFails.setStatus("mandatory")
_CpqiScsiTargetLogoutStatsTable_Object = MibTable
cpqiScsiTargetLogoutStatsTable = _CpqiScsiTargetLogoutStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 169, 2, 7, 3)
)
if mibBuilder.loadTexts:
    cpqiScsiTargetLogoutStatsTable.setStatus("mandatory")
_CpqiScsiTargetLogoutStatsEntry_Object = MibTableRow
cpqiScsiTargetLogoutStatsEntry = _CpqiScsiTargetLogoutStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 169, 2, 7, 3, 1)
)
cpqiScsiTargetLogoutStatsEntry.setIndexNames(
    (0, "CPQISCSI-MIB", "cpqiScsiTgtLogoutInstIndex"),
    (0, "CPQISCSI-MIB", "cpqiScsiTgtLogoutNodeIndex"),
)
if mibBuilder.loadTexts:
    cpqiScsiTargetLogoutStatsEntry.setStatus("mandatory")
_CpqiScsiTgtLogoutInstIndex_Type = Gauge32
_CpqiScsiTgtLogoutInstIndex_Object = MibTableColumn
cpqiScsiTgtLogoutInstIndex = _CpqiScsiTgtLogoutInstIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 169, 2, 7, 3, 1, 1),
    _CpqiScsiTgtLogoutInstIndex_Type()
)
cpqiScsiTgtLogoutInstIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqiScsiTgtLogoutInstIndex.setStatus("mandatory")
_CpqiScsiTgtLogoutNodeIndex_Type = Gauge32
_CpqiScsiTgtLogoutNodeIndex_Object = MibTableColumn
cpqiScsiTgtLogoutNodeIndex = _CpqiScsiTgtLogoutNodeIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 169, 2, 7, 3, 1, 2),
    _CpqiScsiTgtLogoutNodeIndex_Type()
)
cpqiScsiTgtLogoutNodeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqiScsiTgtLogoutNodeIndex.setStatus("mandatory")
_CpqiScsiTgtLogoutNormals_Type = Counter32
_CpqiScsiTgtLogoutNormals_Object = MibTableColumn
cpqiScsiTgtLogoutNormals = _CpqiScsiTgtLogoutNormals_Object(
    (1, 3, 6, 1, 4, 1, 232, 169, 2, 7, 3, 1, 3),
    _CpqiScsiTgtLogoutNormals_Type()
)
cpqiScsiTgtLogoutNormals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqiScsiTgtLogoutNormals.setStatus("mandatory")
_CpqiScsiTgtLogoutOthers_Type = Counter32
_CpqiScsiTgtLogoutOthers_Object = MibTableColumn
cpqiScsiTgtLogoutOthers = _CpqiScsiTgtLogoutOthers_Object(
    (1, 3, 6, 1, 4, 1, 232, 169, 2, 7, 3, 1, 4),
    _CpqiScsiTgtLogoutOthers_Type()
)
cpqiScsiTgtLogoutOthers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqiScsiTgtLogoutOthers.setStatus("mandatory")
_CpqiScsiTgtAuthorization_ObjectIdentity = ObjectIdentity
cpqiScsiTgtAuthorization = _CpqiScsiTgtAuthorization_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 169, 2, 8)
)
_CpqiScsiTgtAuthAttributesTable_Object = MibTable
cpqiScsiTgtAuthAttributesTable = _CpqiScsiTgtAuthAttributesTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 169, 2, 8, 1)
)
if mibBuilder.loadTexts:
    cpqiScsiTgtAuthAttributesTable.setStatus("mandatory")
_CpqiScsiTgtAuthAttributesEntry_Object = MibTableRow
cpqiScsiTgtAuthAttributesEntry = _CpqiScsiTgtAuthAttributesEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 169, 2, 8, 1, 1)
)
cpqiScsiTgtAuthAttributesEntry.setIndexNames(
    (0, "CPQISCSI-MIB", "cpqiScsiTgtAuthInstIndex"),
    (0, "CPQISCSI-MIB", "cpqiScsiTgtAuthNodeIndex"),
    (0, "CPQISCSI-MIB", "cpqiScsiTgtAuthIndex"),
)
if mibBuilder.loadTexts:
    cpqiScsiTgtAuthAttributesEntry.setStatus("mandatory")
_CpqiScsiTgtAuthInstIndex_Type = Gauge32
_CpqiScsiTgtAuthInstIndex_Object = MibTableColumn
cpqiScsiTgtAuthInstIndex = _CpqiScsiTgtAuthInstIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 169, 2, 8, 1, 1, 1),
    _CpqiScsiTgtAuthInstIndex_Type()
)
cpqiScsiTgtAuthInstIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqiScsiTgtAuthInstIndex.setStatus("mandatory")
_CpqiScsiTgtAuthNodeIndex_Type = Gauge32
_CpqiScsiTgtAuthNodeIndex_Object = MibTableColumn
cpqiScsiTgtAuthNodeIndex = _CpqiScsiTgtAuthNodeIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 169, 2, 8, 1, 1, 2),
    _CpqiScsiTgtAuthNodeIndex_Type()
)
cpqiScsiTgtAuthNodeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqiScsiTgtAuthNodeIndex.setStatus("mandatory")
_CpqiScsiTgtAuthIndex_Type = Gauge32
_CpqiScsiTgtAuthIndex_Object = MibTableColumn
cpqiScsiTgtAuthIndex = _CpqiScsiTgtAuthIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 169, 2, 8, 1, 1, 3),
    _CpqiScsiTgtAuthIndex_Type()
)
cpqiScsiTgtAuthIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqiScsiTgtAuthIndex.setStatus("mandatory")


class _CpqiScsiTgtAuthRowStatus_Type(Integer32):
    """Custom type cpqiScsiTgtAuthRowStatus based on Integer32"""
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
        *(("active", 1),
          ("notInService", 2),
          ("notReady", 3),
          ("createAndGo", 4),
          ("createAndWait", 5),
          ("destroy", 6))
    )


_CpqiScsiTgtAuthRowStatus_Type.__name__ = "Integer32"
_CpqiScsiTgtAuthRowStatus_Object = MibTableColumn
cpqiScsiTgtAuthRowStatus = _CpqiScsiTgtAuthRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 169, 2, 8, 1, 1, 4),
    _CpqiScsiTgtAuthRowStatus_Type()
)
cpqiScsiTgtAuthRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqiScsiTgtAuthRowStatus.setStatus("mandatory")
_CpqiScsiTgtAuthIdentity_Type = ObjectIdentifier
_CpqiScsiTgtAuthIdentity_Object = MibTableColumn
cpqiScsiTgtAuthIdentity = _CpqiScsiTgtAuthIdentity_Object(
    (1, 3, 6, 1, 4, 1, 232, 169, 2, 8, 1, 1, 5),
    _CpqiScsiTgtAuthIdentity_Type()
)
cpqiScsiTgtAuthIdentity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqiScsiTgtAuthIdentity.setStatus("mandatory")
_CpqiScsiInitiator_ObjectIdentity = ObjectIdentity
cpqiScsiInitiator = _CpqiScsiInitiator_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 169, 2, 9)
)
_CpqiScsiInitiatorAttributesTable_Object = MibTable
cpqiScsiInitiatorAttributesTable = _CpqiScsiInitiatorAttributesTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 169, 2, 9, 1)
)
if mibBuilder.loadTexts:
    cpqiScsiInitiatorAttributesTable.setStatus("mandatory")
_CpqiScsiInitiatorAttributesEntry_Object = MibTableRow
cpqiScsiInitiatorAttributesEntry = _CpqiScsiInitiatorAttributesEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 169, 2, 9, 1, 1)
)
cpqiScsiInitiatorAttributesEntry.setIndexNames(
    (0, "CPQISCSI-MIB", "cpqiScsiIntrInstIndex"),
    (0, "CPQISCSI-MIB", "cpqiScsiIntrNodeIndex"),
)
if mibBuilder.loadTexts:
    cpqiScsiInitiatorAttributesEntry.setStatus("mandatory")
_CpqiScsiIntrInstIndex_Type = Gauge32
_CpqiScsiIntrInstIndex_Object = MibTableColumn
cpqiScsiIntrInstIndex = _CpqiScsiIntrInstIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 169, 2, 9, 1, 1, 1),
    _CpqiScsiIntrInstIndex_Type()
)
cpqiScsiIntrInstIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqiScsiIntrInstIndex.setStatus("mandatory")
_CpqiScsiIntrNodeIndex_Type = Gauge32
_CpqiScsiIntrNodeIndex_Object = MibTableColumn
cpqiScsiIntrNodeIndex = _CpqiScsiIntrNodeIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 169, 2, 9, 1, 1, 2),
    _CpqiScsiIntrNodeIndex_Type()
)
cpqiScsiIntrNodeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqiScsiIntrNodeIndex.setStatus("mandatory")
_CpqiScsiIntrLoginFailures_Type = Counter32
_CpqiScsiIntrLoginFailures_Object = MibTableColumn
cpqiScsiIntrLoginFailures = _CpqiScsiIntrLoginFailures_Object(
    (1, 3, 6, 1, 4, 1, 232, 169, 2, 9, 1, 1, 3),
    _CpqiScsiIntrLoginFailures_Type()
)
cpqiScsiIntrLoginFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqiScsiIntrLoginFailures.setStatus("mandatory")
_CpqiScsiIntrLastFailureTime_Type = TimeTicks
_CpqiScsiIntrLastFailureTime_Object = MibTableColumn
cpqiScsiIntrLastFailureTime = _CpqiScsiIntrLastFailureTime_Object(
    (1, 3, 6, 1, 4, 1, 232, 169, 2, 9, 1, 1, 4),
    _CpqiScsiIntrLastFailureTime_Type()
)
cpqiScsiIntrLastFailureTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqiScsiIntrLastFailureTime.setStatus("mandatory")
_CpqiScsiIntrLastFailureType_Type = ObjectIdentifier
_CpqiScsiIntrLastFailureType_Object = MibTableColumn
cpqiScsiIntrLastFailureType = _CpqiScsiIntrLastFailureType_Object(
    (1, 3, 6, 1, 4, 1, 232, 169, 2, 9, 1, 1, 5),
    _CpqiScsiIntrLastFailureType_Type()
)
cpqiScsiIntrLastFailureType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqiScsiIntrLastFailureType.setStatus("mandatory")
_CpqiScsiIntrLastTgtFailureName_Type = DisplayString
_CpqiScsiIntrLastTgtFailureName_Object = MibTableColumn
cpqiScsiIntrLastTgtFailureName = _CpqiScsiIntrLastTgtFailureName_Object(
    (1, 3, 6, 1, 4, 1, 232, 169, 2, 9, 1, 1, 6),
    _CpqiScsiIntrLastTgtFailureName_Type()
)
cpqiScsiIntrLastTgtFailureName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqiScsiIntrLastTgtFailureName.setStatus("mandatory")


class _CpqiScsiIntrLastTgtFailureAddrType_Type(Integer32):
    """Custom type cpqiScsiIntrLastTgtFailureAddrType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              16)
        )
    )
    namedValues = NamedValues(
        *(("ipv4", 1),
          ("ipv6", 2),
          ("ipv4z", 3),
          ("ipv6z", 4),
          ("dns", 16))
    )


_CpqiScsiIntrLastTgtFailureAddrType_Type.__name__ = "Integer32"
_CpqiScsiIntrLastTgtFailureAddrType_Object = MibTableColumn
cpqiScsiIntrLastTgtFailureAddrType = _CpqiScsiIntrLastTgtFailureAddrType_Object(
    (1, 3, 6, 1, 4, 1, 232, 169, 2, 9, 1, 1, 7),
    _CpqiScsiIntrLastTgtFailureAddrType_Type()
)
cpqiScsiIntrLastTgtFailureAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqiScsiIntrLastTgtFailureAddrType.setStatus("mandatory")


class _CpqiScsiIntrLastTgtFailureAddr_Type(OctetString):
    """Custom type cpqiScsiIntrLastTgtFailureAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqiScsiIntrLastTgtFailureAddr_Type.__name__ = "OctetString"
_CpqiScsiIntrLastTgtFailureAddr_Object = MibTableColumn
cpqiScsiIntrLastTgtFailureAddr = _CpqiScsiIntrLastTgtFailureAddr_Object(
    (1, 3, 6, 1, 4, 1, 232, 169, 2, 9, 1, 1, 8),
    _CpqiScsiIntrLastTgtFailureAddr_Type()
)
cpqiScsiIntrLastTgtFailureAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqiScsiIntrLastTgtFailureAddr.setStatus("mandatory")
_CpqiScsiInitiatorLoginStatsTable_Object = MibTable
cpqiScsiInitiatorLoginStatsTable = _CpqiScsiInitiatorLoginStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 169, 2, 9, 2)
)
if mibBuilder.loadTexts:
    cpqiScsiInitiatorLoginStatsTable.setStatus("mandatory")
_CpqiScsiInitiatorLoginStatsEntry_Object = MibTableRow
cpqiScsiInitiatorLoginStatsEntry = _CpqiScsiInitiatorLoginStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 169, 2, 9, 2, 1)
)
cpqiScsiInitiatorLoginStatsEntry.setIndexNames(
    (0, "CPQISCSI-MIB", "cpqiScsiIntrLoginInstIndex"),
    (0, "CPQISCSI-MIB", "cpqiScsiIntrLoginNodeIndex"),
)
if mibBuilder.loadTexts:
    cpqiScsiInitiatorLoginStatsEntry.setStatus("mandatory")
_CpqiScsiIntrLoginInstIndex_Type = Gauge32
_CpqiScsiIntrLoginInstIndex_Object = MibTableColumn
cpqiScsiIntrLoginInstIndex = _CpqiScsiIntrLoginInstIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 169, 2, 9, 2, 1, 1),
    _CpqiScsiIntrLoginInstIndex_Type()
)
cpqiScsiIntrLoginInstIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqiScsiIntrLoginInstIndex.setStatus("mandatory")
_CpqiScsiIntrLoginNodeIndex_Type = Gauge32
_CpqiScsiIntrLoginNodeIndex_Object = MibTableColumn
cpqiScsiIntrLoginNodeIndex = _CpqiScsiIntrLoginNodeIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 169, 2, 9, 2, 1, 2),
    _CpqiScsiIntrLoginNodeIndex_Type()
)
cpqiScsiIntrLoginNodeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqiScsiIntrLoginNodeIndex.setStatus("mandatory")
_CpqiScsiIntrLoginAcceptRsps_Type = Counter32
_CpqiScsiIntrLoginAcceptRsps_Object = MibTableColumn
cpqiScsiIntrLoginAcceptRsps = _CpqiScsiIntrLoginAcceptRsps_Object(
    (1, 3, 6, 1, 4, 1, 232, 169, 2, 9, 2, 1, 3),
    _CpqiScsiIntrLoginAcceptRsps_Type()
)
cpqiScsiIntrLoginAcceptRsps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqiScsiIntrLoginAcceptRsps.setStatus("mandatory")
_CpqiScsiIntrLoginOtherFailRsps_Type = Counter32
_CpqiScsiIntrLoginOtherFailRsps_Object = MibTableColumn
cpqiScsiIntrLoginOtherFailRsps = _CpqiScsiIntrLoginOtherFailRsps_Object(
    (1, 3, 6, 1, 4, 1, 232, 169, 2, 9, 2, 1, 4),
    _CpqiScsiIntrLoginOtherFailRsps_Type()
)
cpqiScsiIntrLoginOtherFailRsps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqiScsiIntrLoginOtherFailRsps.setStatus("mandatory")
_CpqiScsiIntrLoginRedirectRsps_Type = Counter32
_CpqiScsiIntrLoginRedirectRsps_Object = MibTableColumn
cpqiScsiIntrLoginRedirectRsps = _CpqiScsiIntrLoginRedirectRsps_Object(
    (1, 3, 6, 1, 4, 1, 232, 169, 2, 9, 2, 1, 5),
    _CpqiScsiIntrLoginRedirectRsps_Type()
)
cpqiScsiIntrLoginRedirectRsps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqiScsiIntrLoginRedirectRsps.setStatus("mandatory")
_CpqiScsiIntrLoginAuthFailRsps_Type = Counter32
_CpqiScsiIntrLoginAuthFailRsps_Object = MibTableColumn
cpqiScsiIntrLoginAuthFailRsps = _CpqiScsiIntrLoginAuthFailRsps_Object(
    (1, 3, 6, 1, 4, 1, 232, 169, 2, 9, 2, 1, 6),
    _CpqiScsiIntrLoginAuthFailRsps_Type()
)
cpqiScsiIntrLoginAuthFailRsps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqiScsiIntrLoginAuthFailRsps.setStatus("mandatory")
_CpqiScsiIntrLoginAuthenticateFails_Type = Counter32
_CpqiScsiIntrLoginAuthenticateFails_Object = MibTableColumn
cpqiScsiIntrLoginAuthenticateFails = _CpqiScsiIntrLoginAuthenticateFails_Object(
    (1, 3, 6, 1, 4, 1, 232, 169, 2, 9, 2, 1, 7),
    _CpqiScsiIntrLoginAuthenticateFails_Type()
)
cpqiScsiIntrLoginAuthenticateFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqiScsiIntrLoginAuthenticateFails.setStatus("mandatory")
_CpqiScsiIntrLoginNegotiateFails_Type = Counter32
_CpqiScsiIntrLoginNegotiateFails_Object = MibTableColumn
cpqiScsiIntrLoginNegotiateFails = _CpqiScsiIntrLoginNegotiateFails_Object(
    (1, 3, 6, 1, 4, 1, 232, 169, 2, 9, 2, 1, 8),
    _CpqiScsiIntrLoginNegotiateFails_Type()
)
cpqiScsiIntrLoginNegotiateFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqiScsiIntrLoginNegotiateFails.setStatus("mandatory")
_CpqiScsiInitiatorLogoutStatsTable_Object = MibTable
cpqiScsiInitiatorLogoutStatsTable = _CpqiScsiInitiatorLogoutStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 169, 2, 9, 3)
)
if mibBuilder.loadTexts:
    cpqiScsiInitiatorLogoutStatsTable.setStatus("mandatory")
_CpqiScsiInitiatorLogoutStatsEntry_Object = MibTableRow
cpqiScsiInitiatorLogoutStatsEntry = _CpqiScsiInitiatorLogoutStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 169, 2, 9, 3, 1)
)
cpqiScsiInitiatorLogoutStatsEntry.setIndexNames(
    (0, "CPQISCSI-MIB", "cpqiScsiIntrLogoutInstIndex"),
    (0, "CPQISCSI-MIB", "cpqiScsiIntrLogoutNodeIndex"),
)
if mibBuilder.loadTexts:
    cpqiScsiInitiatorLogoutStatsEntry.setStatus("mandatory")
_CpqiScsiIntrLogoutInstIndex_Type = Gauge32
_CpqiScsiIntrLogoutInstIndex_Object = MibTableColumn
cpqiScsiIntrLogoutInstIndex = _CpqiScsiIntrLogoutInstIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 169, 2, 9, 3, 1, 1),
    _CpqiScsiIntrLogoutInstIndex_Type()
)
cpqiScsiIntrLogoutInstIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqiScsiIntrLogoutInstIndex.setStatus("mandatory")
_CpqiScsiIntrLogoutNodeIndex_Type = Gauge32
_CpqiScsiIntrLogoutNodeIndex_Object = MibTableColumn
cpqiScsiIntrLogoutNodeIndex = _CpqiScsiIntrLogoutNodeIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 169, 2, 9, 3, 1, 2),
    _CpqiScsiIntrLogoutNodeIndex_Type()
)
cpqiScsiIntrLogoutNodeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqiScsiIntrLogoutNodeIndex.setStatus("mandatory")
_CpqiScsiIntrLogoutNormals_Type = Counter32
_CpqiScsiIntrLogoutNormals_Object = MibTableColumn
cpqiScsiIntrLogoutNormals = _CpqiScsiIntrLogoutNormals_Object(
    (1, 3, 6, 1, 4, 1, 232, 169, 2, 9, 3, 1, 3),
    _CpqiScsiIntrLogoutNormals_Type()
)
cpqiScsiIntrLogoutNormals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqiScsiIntrLogoutNormals.setStatus("mandatory")
_CpqiScsiIntrLogoutOthers_Type = Counter32
_CpqiScsiIntrLogoutOthers_Object = MibTableColumn
cpqiScsiIntrLogoutOthers = _CpqiScsiIntrLogoutOthers_Object(
    (1, 3, 6, 1, 4, 1, 232, 169, 2, 9, 3, 1, 4),
    _CpqiScsiIntrLogoutOthers_Type()
)
cpqiScsiIntrLogoutOthers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqiScsiIntrLogoutOthers.setStatus("mandatory")
_CpqiScsiIntrAuthorization_ObjectIdentity = ObjectIdentity
cpqiScsiIntrAuthorization = _CpqiScsiIntrAuthorization_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 169, 2, 10)
)
_CpqiScsiIntrAuthAttributesTable_Object = MibTable
cpqiScsiIntrAuthAttributesTable = _CpqiScsiIntrAuthAttributesTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 169, 2, 10, 1)
)
if mibBuilder.loadTexts:
    cpqiScsiIntrAuthAttributesTable.setStatus("mandatory")
_CpqiScsiIntrAuthAttributesEntry_Object = MibTableRow
cpqiScsiIntrAuthAttributesEntry = _CpqiScsiIntrAuthAttributesEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 169, 2, 10, 1, 1)
)
cpqiScsiIntrAuthAttributesEntry.setIndexNames(
    (0, "CPQISCSI-MIB", "cpqiScsiIntrAuthInstIndex"),
    (0, "CPQISCSI-MIB", "cpqiScsiIntrAuthNodeIndex"),
    (0, "CPQISCSI-MIB", "cpqiScsiIntrAuthIndex"),
)
if mibBuilder.loadTexts:
    cpqiScsiIntrAuthAttributesEntry.setStatus("mandatory")
_CpqiScsiIntrAuthInstIndex_Type = Gauge32
_CpqiScsiIntrAuthInstIndex_Object = MibTableColumn
cpqiScsiIntrAuthInstIndex = _CpqiScsiIntrAuthInstIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 169, 2, 10, 1, 1, 1),
    _CpqiScsiIntrAuthInstIndex_Type()
)
cpqiScsiIntrAuthInstIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqiScsiIntrAuthInstIndex.setStatus("mandatory")
_CpqiScsiIntrAuthNodeIndex_Type = Gauge32
_CpqiScsiIntrAuthNodeIndex_Object = MibTableColumn
cpqiScsiIntrAuthNodeIndex = _CpqiScsiIntrAuthNodeIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 169, 2, 10, 1, 1, 2),
    _CpqiScsiIntrAuthNodeIndex_Type()
)
cpqiScsiIntrAuthNodeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqiScsiIntrAuthNodeIndex.setStatus("mandatory")
_CpqiScsiIntrAuthIndex_Type = Gauge32
_CpqiScsiIntrAuthIndex_Object = MibTableColumn
cpqiScsiIntrAuthIndex = _CpqiScsiIntrAuthIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 169, 2, 10, 1, 1, 3),
    _CpqiScsiIntrAuthIndex_Type()
)
cpqiScsiIntrAuthIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqiScsiIntrAuthIndex.setStatus("mandatory")


class _CpqiScsiIntrAuthRowStatus_Type(Integer32):
    """Custom type cpqiScsiIntrAuthRowStatus based on Integer32"""
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
        *(("active", 1),
          ("notInService", 2),
          ("notReady", 3),
          ("createAndGo", 4),
          ("createAndWait", 5),
          ("destroy", 6))
    )


_CpqiScsiIntrAuthRowStatus_Type.__name__ = "Integer32"
_CpqiScsiIntrAuthRowStatus_Object = MibTableColumn
cpqiScsiIntrAuthRowStatus = _CpqiScsiIntrAuthRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 169, 2, 10, 1, 1, 4),
    _CpqiScsiIntrAuthRowStatus_Type()
)
cpqiScsiIntrAuthRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqiScsiIntrAuthRowStatus.setStatus("mandatory")
_CpqiScsiIntrAuthIdentity_Type = ObjectIdentifier
_CpqiScsiIntrAuthIdentity_Object = MibTableColumn
cpqiScsiIntrAuthIdentity = _CpqiScsiIntrAuthIdentity_Object(
    (1, 3, 6, 1, 4, 1, 232, 169, 2, 10, 1, 1, 5),
    _CpqiScsiIntrAuthIdentity_Type()
)
cpqiScsiIntrAuthIdentity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqiScsiIntrAuthIdentity.setStatus("mandatory")
_CpqiScsiSession_ObjectIdentity = ObjectIdentity
cpqiScsiSession = _CpqiScsiSession_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 169, 2, 11)
)
_CpqiScsiSessionAttributesTable_Object = MibTable
cpqiScsiSessionAttributesTable = _CpqiScsiSessionAttributesTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 169, 2, 11, 1)
)
if mibBuilder.loadTexts:
    cpqiScsiSessionAttributesTable.setStatus("mandatory")
_CpqiScsiSessionAttributesEntry_Object = MibTableRow
cpqiScsiSessionAttributesEntry = _CpqiScsiSessionAttributesEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 169, 2, 11, 1, 1)
)
cpqiScsiSessionAttributesEntry.setIndexNames(
    (0, "CPQISCSI-MIB", "cpqiScsiSsnInstIndex"),
    (0, "CPQISCSI-MIB", "cpqiScsiSsnNodeIndex"),
    (0, "CPQISCSI-MIB", "cpqiScsiSsnIndex"),
)
if mibBuilder.loadTexts:
    cpqiScsiSessionAttributesEntry.setStatus("mandatory")
_CpqiScsiSsnInstIndex_Type = Gauge32
_CpqiScsiSsnInstIndex_Object = MibTableColumn
cpqiScsiSsnInstIndex = _CpqiScsiSsnInstIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 169, 2, 11, 1, 1, 1),
    _CpqiScsiSsnInstIndex_Type()
)
cpqiScsiSsnInstIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqiScsiSsnInstIndex.setStatus("mandatory")
_CpqiScsiSsnNodeIndex_Type = Gauge32
_CpqiScsiSsnNodeIndex_Object = MibTableColumn
cpqiScsiSsnNodeIndex = _CpqiScsiSsnNodeIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 169, 2, 11, 1, 1, 2),
    _CpqiScsiSsnNodeIndex_Type()
)
cpqiScsiSsnNodeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqiScsiSsnNodeIndex.setStatus("mandatory")
_CpqiScsiSsnIndex_Type = Gauge32
_CpqiScsiSsnIndex_Object = MibTableColumn
cpqiScsiSsnIndex = _CpqiScsiSsnIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 169, 2, 11, 1, 1, 3),
    _CpqiScsiSsnIndex_Type()
)
cpqiScsiSsnIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqiScsiSsnIndex.setStatus("mandatory")


class _CpqiScsiSsnDirection_Type(Integer32):
    """Custom type cpqiScsiSsnDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inboundSession", 1),
          ("outboundSession", 2))
    )


_CpqiScsiSsnDirection_Type.__name__ = "Integer32"
_CpqiScsiSsnDirection_Object = MibTableColumn
cpqiScsiSsnDirection = _CpqiScsiSsnDirection_Object(
    (1, 3, 6, 1, 4, 1, 232, 169, 2, 11, 1, 1, 4),
    _CpqiScsiSsnDirection_Type()
)
cpqiScsiSsnDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqiScsiSsnDirection.setStatus("mandatory")
_CpqiScsiSsnInitiatorName_Type = DisplayString
_CpqiScsiSsnInitiatorName_Object = MibTableColumn
cpqiScsiSsnInitiatorName = _CpqiScsiSsnInitiatorName_Object(
    (1, 3, 6, 1, 4, 1, 232, 169, 2, 11, 1, 1, 5),
    _CpqiScsiSsnInitiatorName_Type()
)
cpqiScsiSsnInitiatorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqiScsiSsnInitiatorName.setStatus("mandatory")
_CpqiScsiSsnTargetName_Type = DisplayString
_CpqiScsiSsnTargetName_Object = MibTableColumn
cpqiScsiSsnTargetName = _CpqiScsiSsnTargetName_Object(
    (1, 3, 6, 1, 4, 1, 232, 169, 2, 11, 1, 1, 6),
    _CpqiScsiSsnTargetName_Type()
)
cpqiScsiSsnTargetName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqiScsiSsnTargetName.setStatus("mandatory")


class _CpqiScsiSsnTSIH_Type(Integer32):
    """Custom type cpqiScsiSsnTSIH based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CpqiScsiSsnTSIH_Type.__name__ = "Integer32"
_CpqiScsiSsnTSIH_Object = MibTableColumn
cpqiScsiSsnTSIH = _CpqiScsiSsnTSIH_Object(
    (1, 3, 6, 1, 4, 1, 232, 169, 2, 11, 1, 1, 7),
    _CpqiScsiSsnTSIH_Type()
)
cpqiScsiSsnTSIH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqiScsiSsnTSIH.setStatus("mandatory")


class _CpqiScsiSsnISID_Type(OctetString):
    """Custom type cpqiScsiSsnISID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )
    fixed_length = 6


_CpqiScsiSsnISID_Type.__name__ = "OctetString"
_CpqiScsiSsnISID_Object = MibTableColumn
cpqiScsiSsnISID = _CpqiScsiSsnISID_Object(
    (1, 3, 6, 1, 4, 1, 232, 169, 2, 11, 1, 1, 8),
    _CpqiScsiSsnISID_Type()
)
cpqiScsiSsnISID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqiScsiSsnISID.setStatus("mandatory")
_CpqiScsiSsnInitiatorAlias_Type = DisplayString
_CpqiScsiSsnInitiatorAlias_Object = MibTableColumn
cpqiScsiSsnInitiatorAlias = _CpqiScsiSsnInitiatorAlias_Object(
    (1, 3, 6, 1, 4, 1, 232, 169, 2, 11, 1, 1, 9),
    _CpqiScsiSsnInitiatorAlias_Type()
)
cpqiScsiSsnInitiatorAlias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqiScsiSsnInitiatorAlias.setStatus("mandatory")
_CpqiScsiSsnTargetAlias_Type = DisplayString
_CpqiScsiSsnTargetAlias_Object = MibTableColumn
cpqiScsiSsnTargetAlias = _CpqiScsiSsnTargetAlias_Object(
    (1, 3, 6, 1, 4, 1, 232, 169, 2, 11, 1, 1, 10),
    _CpqiScsiSsnTargetAlias_Type()
)
cpqiScsiSsnTargetAlias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqiScsiSsnTargetAlias.setStatus("mandatory")


class _CpqiScsiSsnInitialR2T_Type(Integer32):
    """Custom type cpqiScsiSsnInitialR2T based on Integer32"""
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


_CpqiScsiSsnInitialR2T_Type.__name__ = "Integer32"
_CpqiScsiSsnInitialR2T_Object = MibTableColumn
cpqiScsiSsnInitialR2T = _CpqiScsiSsnInitialR2T_Object(
    (1, 3, 6, 1, 4, 1, 232, 169, 2, 11, 1, 1, 11),
    _CpqiScsiSsnInitialR2T_Type()
)
cpqiScsiSsnInitialR2T.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqiScsiSsnInitialR2T.setStatus("mandatory")


class _CpqiScsiSsnImmediateData_Type(Integer32):
    """Custom type cpqiScsiSsnImmediateData based on Integer32"""
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


_CpqiScsiSsnImmediateData_Type.__name__ = "Integer32"
_CpqiScsiSsnImmediateData_Object = MibTableColumn
cpqiScsiSsnImmediateData = _CpqiScsiSsnImmediateData_Object(
    (1, 3, 6, 1, 4, 1, 232, 169, 2, 11, 1, 1, 12),
    _CpqiScsiSsnImmediateData_Type()
)
cpqiScsiSsnImmediateData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqiScsiSsnImmediateData.setStatus("mandatory")


class _CpqiScsiSsnType_Type(Integer32):
    """Custom type cpqiScsiSsnType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normalSession", 1),
          ("discoverySession", 2))
    )


_CpqiScsiSsnType_Type.__name__ = "Integer32"
_CpqiScsiSsnType_Object = MibTableColumn
cpqiScsiSsnType = _CpqiScsiSsnType_Object(
    (1, 3, 6, 1, 4, 1, 232, 169, 2, 11, 1, 1, 13),
    _CpqiScsiSsnType_Type()
)
cpqiScsiSsnType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqiScsiSsnType.setStatus("mandatory")


class _CpqiScsiSsnMaxOutstandingR2T_Type(Integer32):
    """Custom type cpqiScsiSsnMaxOutstandingR2T based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CpqiScsiSsnMaxOutstandingR2T_Type.__name__ = "Integer32"
_CpqiScsiSsnMaxOutstandingR2T_Object = MibTableColumn
cpqiScsiSsnMaxOutstandingR2T = _CpqiScsiSsnMaxOutstandingR2T_Object(
    (1, 3, 6, 1, 4, 1, 232, 169, 2, 11, 1, 1, 14),
    _CpqiScsiSsnMaxOutstandingR2T_Type()
)
cpqiScsiSsnMaxOutstandingR2T.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqiScsiSsnMaxOutstandingR2T.setStatus("mandatory")


class _CpqiScsiSsnFirstBurstLength_Type(Integer32):
    """Custom type cpqiScsiSsnFirstBurstLength based on Integer32"""
    defaultValue = 65536

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(512, 16777215),
    )


_CpqiScsiSsnFirstBurstLength_Type.__name__ = "Integer32"
_CpqiScsiSsnFirstBurstLength_Object = MibTableColumn
cpqiScsiSsnFirstBurstLength = _CpqiScsiSsnFirstBurstLength_Object(
    (1, 3, 6, 1, 4, 1, 232, 169, 2, 11, 1, 1, 15),
    _CpqiScsiSsnFirstBurstLength_Type()
)
cpqiScsiSsnFirstBurstLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqiScsiSsnFirstBurstLength.setStatus("mandatory")


class _CpqiScsiSsnMaxBurstLength_Type(Integer32):
    """Custom type cpqiScsiSsnMaxBurstLength based on Integer32"""
    defaultValue = 262144

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(512, 16777215),
    )


_CpqiScsiSsnMaxBurstLength_Type.__name__ = "Integer32"
_CpqiScsiSsnMaxBurstLength_Object = MibTableColumn
cpqiScsiSsnMaxBurstLength = _CpqiScsiSsnMaxBurstLength_Object(
    (1, 3, 6, 1, 4, 1, 232, 169, 2, 11, 1, 1, 16),
    _CpqiScsiSsnMaxBurstLength_Type()
)
cpqiScsiSsnMaxBurstLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqiScsiSsnMaxBurstLength.setStatus("mandatory")
_CpqiScsiSsnConnectionNumber_Type = Gauge32
_CpqiScsiSsnConnectionNumber_Object = MibTableColumn
cpqiScsiSsnConnectionNumber = _CpqiScsiSsnConnectionNumber_Object(
    (1, 3, 6, 1, 4, 1, 232, 169, 2, 11, 1, 1, 17),
    _CpqiScsiSsnConnectionNumber_Type()
)
cpqiScsiSsnConnectionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqiScsiSsnConnectionNumber.setStatus("mandatory")
_CpqiScsiSsnAuthIdentity_Type = ObjectIdentifier
_CpqiScsiSsnAuthIdentity_Object = MibTableColumn
cpqiScsiSsnAuthIdentity = _CpqiScsiSsnAuthIdentity_Object(
    (1, 3, 6, 1, 4, 1, 232, 169, 2, 11, 1, 1, 18),
    _CpqiScsiSsnAuthIdentity_Type()
)
cpqiScsiSsnAuthIdentity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqiScsiSsnAuthIdentity.setStatus("mandatory")


class _CpqiScsiSsnDataSequenceInOrder_Type(Integer32):
    """Custom type cpqiScsiSsnDataSequenceInOrder based on Integer32"""
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


_CpqiScsiSsnDataSequenceInOrder_Type.__name__ = "Integer32"
_CpqiScsiSsnDataSequenceInOrder_Object = MibTableColumn
cpqiScsiSsnDataSequenceInOrder = _CpqiScsiSsnDataSequenceInOrder_Object(
    (1, 3, 6, 1, 4, 1, 232, 169, 2, 11, 1, 1, 19),
    _CpqiScsiSsnDataSequenceInOrder_Type()
)
cpqiScsiSsnDataSequenceInOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqiScsiSsnDataSequenceInOrder.setStatus("mandatory")


class _CpqiScsiSsnDataPDUInOrder_Type(Integer32):
    """Custom type cpqiScsiSsnDataPDUInOrder based on Integer32"""
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


_CpqiScsiSsnDataPDUInOrder_Type.__name__ = "Integer32"
_CpqiScsiSsnDataPDUInOrder_Object = MibTableColumn
cpqiScsiSsnDataPDUInOrder = _CpqiScsiSsnDataPDUInOrder_Object(
    (1, 3, 6, 1, 4, 1, 232, 169, 2, 11, 1, 1, 20),
    _CpqiScsiSsnDataPDUInOrder_Type()
)
cpqiScsiSsnDataPDUInOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqiScsiSsnDataPDUInOrder.setStatus("mandatory")


class _CpqiScsiSsnErrorRecoveryLevel_Type(Integer32):
    """Custom type cpqiScsiSsnErrorRecoveryLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CpqiScsiSsnErrorRecoveryLevel_Type.__name__ = "Integer32"
_CpqiScsiSsnErrorRecoveryLevel_Object = MibTableColumn
cpqiScsiSsnErrorRecoveryLevel = _CpqiScsiSsnErrorRecoveryLevel_Object(
    (1, 3, 6, 1, 4, 1, 232, 169, 2, 11, 1, 1, 21),
    _CpqiScsiSsnErrorRecoveryLevel_Type()
)
cpqiScsiSsnErrorRecoveryLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqiScsiSsnErrorRecoveryLevel.setStatus("mandatory")


class _CpqiScsiSessionId_Type(DisplayString):
    """Custom type cpqiScsiSessionId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqiScsiSessionId_Type.__name__ = "DisplayString"
_CpqiScsiSessionId_Object = MibTableColumn
cpqiScsiSessionId = _CpqiScsiSessionId_Object(
    (1, 3, 6, 1, 4, 1, 232, 169, 2, 11, 1, 1, 22),
    _CpqiScsiSessionId_Type()
)
cpqiScsiSessionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqiScsiSessionId.setStatus("mandatory")
_CpqiScsiSessionStatsTable_Object = MibTable
cpqiScsiSessionStatsTable = _CpqiScsiSessionStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 169, 2, 11, 2)
)
if mibBuilder.loadTexts:
    cpqiScsiSessionStatsTable.setStatus("mandatory")
_CpqiScsiSessionStatsEntry_Object = MibTableRow
cpqiScsiSessionStatsEntry = _CpqiScsiSessionStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 169, 2, 11, 2, 1)
)
cpqiScsiSessionStatsEntry.setIndexNames(
    (0, "CPQISCSI-MIB", "cpqiScsiSsnStatInstIndex"),
    (0, "CPQISCSI-MIB", "cpqiScsiSsnStatNodeIndex"),
    (0, "CPQISCSI-MIB", "cpqiScsiSsnSessionIndex"),
)
if mibBuilder.loadTexts:
    cpqiScsiSessionStatsEntry.setStatus("mandatory")
_CpqiScsiSsnStatInstIndex_Type = Gauge32
_CpqiScsiSsnStatInstIndex_Object = MibTableColumn
cpqiScsiSsnStatInstIndex = _CpqiScsiSsnStatInstIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 169, 2, 11, 2, 1, 1),
    _CpqiScsiSsnStatInstIndex_Type()
)
cpqiScsiSsnStatInstIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqiScsiSsnStatInstIndex.setStatus("mandatory")
_CpqiScsiSsnStatNodeIndex_Type = Gauge32
_CpqiScsiSsnStatNodeIndex_Object = MibTableColumn
cpqiScsiSsnStatNodeIndex = _CpqiScsiSsnStatNodeIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 169, 2, 11, 2, 1, 2),
    _CpqiScsiSsnStatNodeIndex_Type()
)
cpqiScsiSsnStatNodeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqiScsiSsnStatNodeIndex.setStatus("mandatory")
_CpqiScsiSsnSessionIndex_Type = Gauge32
_CpqiScsiSsnSessionIndex_Object = MibTableColumn
cpqiScsiSsnSessionIndex = _CpqiScsiSsnSessionIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 169, 2, 11, 2, 1, 3),
    _CpqiScsiSsnSessionIndex_Type()
)
cpqiScsiSsnSessionIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqiScsiSsnSessionIndex.setStatus("mandatory")
_CpqiScsiSsnCmdPDUs_Type = Counter32
_CpqiScsiSsnCmdPDUs_Object = MibTableColumn
cpqiScsiSsnCmdPDUs = _CpqiScsiSsnCmdPDUs_Object(
    (1, 3, 6, 1, 4, 1, 232, 169, 2, 11, 2, 1, 4),
    _CpqiScsiSsnCmdPDUs_Type()
)
cpqiScsiSsnCmdPDUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqiScsiSsnCmdPDUs.setStatus("mandatory")
_CpqiScsiSsnRspPDUs_Type = Counter32
_CpqiScsiSsnRspPDUs_Object = MibTableColumn
cpqiScsiSsnRspPDUs = _CpqiScsiSsnRspPDUs_Object(
    (1, 3, 6, 1, 4, 1, 232, 169, 2, 11, 2, 1, 5),
    _CpqiScsiSsnRspPDUs_Type()
)
cpqiScsiSsnRspPDUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqiScsiSsnRspPDUs.setStatus("mandatory")
_CpqiScsiSsnTxDataOctets_Type = Counter32
_CpqiScsiSsnTxDataOctets_Object = MibTableColumn
cpqiScsiSsnTxDataOctets = _CpqiScsiSsnTxDataOctets_Object(
    (1, 3, 6, 1, 4, 1, 232, 169, 2, 11, 2, 1, 6),
    _CpqiScsiSsnTxDataOctets_Type()
)
cpqiScsiSsnTxDataOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqiScsiSsnTxDataOctets.setStatus("mandatory")
_CpqiScsiSsnRxDataOctets_Type = Counter32
_CpqiScsiSsnRxDataOctets_Object = MibTableColumn
cpqiScsiSsnRxDataOctets = _CpqiScsiSsnRxDataOctets_Object(
    (1, 3, 6, 1, 4, 1, 232, 169, 2, 11, 2, 1, 7),
    _CpqiScsiSsnRxDataOctets_Type()
)
cpqiScsiSsnRxDataOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqiScsiSsnRxDataOctets.setStatus("mandatory")
_CpqiScsiSsnLCTxDataOctets_Type = Counter32
_CpqiScsiSsnLCTxDataOctets_Object = MibTableColumn
cpqiScsiSsnLCTxDataOctets = _CpqiScsiSsnLCTxDataOctets_Object(
    (1, 3, 6, 1, 4, 1, 232, 169, 2, 11, 2, 1, 8),
    _CpqiScsiSsnLCTxDataOctets_Type()
)
cpqiScsiSsnLCTxDataOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqiScsiSsnLCTxDataOctets.setStatus("mandatory")
_CpqiScsiSsnLCRxDataOctets_Type = Counter32
_CpqiScsiSsnLCRxDataOctets_Object = MibTableColumn
cpqiScsiSsnLCRxDataOctets = _CpqiScsiSsnLCRxDataOctets_Object(
    (1, 3, 6, 1, 4, 1, 232, 169, 2, 11, 2, 1, 9),
    _CpqiScsiSsnLCRxDataOctets_Type()
)
cpqiScsiSsnLCRxDataOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqiScsiSsnLCRxDataOctets.setStatus("mandatory")
_CpqiScsiSessionCxnErrorStatsTable_Object = MibTable
cpqiScsiSessionCxnErrorStatsTable = _CpqiScsiSessionCxnErrorStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 169, 2, 11, 3)
)
if mibBuilder.loadTexts:
    cpqiScsiSessionCxnErrorStatsTable.setStatus("mandatory")
_CpqiScsiSessionCxnErrorStatsEntry_Object = MibTableRow
cpqiScsiSessionCxnErrorStatsEntry = _CpqiScsiSessionCxnErrorStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 169, 2, 11, 3, 1)
)
cpqiScsiSessionCxnErrorStatsEntry.setIndexNames(
    (0, "CPQISCSI-MIB", "cpqiScsiSsnCxnInstIndex"),
    (0, "CPQISCSI-MIB", "cpqiScsiSsnCxnNodeIndex"),
    (0, "CPQISCSI-MIB", "cpqiScsiSsnCxnIndex"),
)
if mibBuilder.loadTexts:
    cpqiScsiSessionCxnErrorStatsEntry.setStatus("mandatory")
_CpqiScsiSsnCxnInstIndex_Type = Gauge32
_CpqiScsiSsnCxnInstIndex_Object = MibTableColumn
cpqiScsiSsnCxnInstIndex = _CpqiScsiSsnCxnInstIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 169, 2, 11, 3, 1, 1),
    _CpqiScsiSsnCxnInstIndex_Type()
)
cpqiScsiSsnCxnInstIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqiScsiSsnCxnInstIndex.setStatus("mandatory")
_CpqiScsiSsnCxnNodeIndex_Type = Gauge32
_CpqiScsiSsnCxnNodeIndex_Object = MibTableColumn
cpqiScsiSsnCxnNodeIndex = _CpqiScsiSsnCxnNodeIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 169, 2, 11, 3, 1, 2),
    _CpqiScsiSsnCxnNodeIndex_Type()
)
cpqiScsiSsnCxnNodeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqiScsiSsnCxnNodeIndex.setStatus("mandatory")
_CpqiScsiSsnCxnIndex_Type = Gauge32
_CpqiScsiSsnCxnIndex_Object = MibTableColumn
cpqiScsiSsnCxnIndex = _CpqiScsiSsnCxnIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 169, 2, 11, 3, 1, 3),
    _CpqiScsiSsnCxnIndex_Type()
)
cpqiScsiSsnCxnIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqiScsiSsnCxnIndex.setStatus("mandatory")
_CpqiScsiSsnCxnDigestErrors_Type = Counter32
_CpqiScsiSsnCxnDigestErrors_Object = MibTableColumn
cpqiScsiSsnCxnDigestErrors = _CpqiScsiSsnCxnDigestErrors_Object(
    (1, 3, 6, 1, 4, 1, 232, 169, 2, 11, 3, 1, 4),
    _CpqiScsiSsnCxnDigestErrors_Type()
)
cpqiScsiSsnCxnDigestErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqiScsiSsnCxnDigestErrors.setStatus("mandatory")
_CpqiScsiSsnCxnTimeoutErrors_Type = Counter32
_CpqiScsiSsnCxnTimeoutErrors_Object = MibTableColumn
cpqiScsiSsnCxnTimeoutErrors = _CpqiScsiSsnCxnTimeoutErrors_Object(
    (1, 3, 6, 1, 4, 1, 232, 169, 2, 11, 3, 1, 5),
    _CpqiScsiSsnCxnTimeoutErrors_Type()
)
cpqiScsiSsnCxnTimeoutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqiScsiSsnCxnTimeoutErrors.setStatus("mandatory")
_CpqiScsiConnection_ObjectIdentity = ObjectIdentity
cpqiScsiConnection = _CpqiScsiConnection_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 169, 2, 12)
)
_CpqiScsiConnectionAttributesTable_Object = MibTable
cpqiScsiConnectionAttributesTable = _CpqiScsiConnectionAttributesTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 169, 2, 12, 1)
)
if mibBuilder.loadTexts:
    cpqiScsiConnectionAttributesTable.setStatus("mandatory")
_CpqiScsiConnectionAttributesEntry_Object = MibTableRow
cpqiScsiConnectionAttributesEntry = _CpqiScsiConnectionAttributesEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 169, 2, 12, 1, 1)
)
cpqiScsiConnectionAttributesEntry.setIndexNames(
    (0, "CPQISCSI-MIB", "cpqiScsiCxnAttrInstIndex"),
    (0, "CPQISCSI-MIB", "cpqiScsiCxnAttrNodeIndex"),
    (0, "CPQISCSI-MIB", "cpqiScsiCxnAttrSessionIndex"),
    (0, "CPQISCSI-MIB", "cpqiScsiCxnAttrIndex"),
)
if mibBuilder.loadTexts:
    cpqiScsiConnectionAttributesEntry.setStatus("mandatory")
_CpqiScsiCxnAttrInstIndex_Type = Gauge32
_CpqiScsiCxnAttrInstIndex_Object = MibTableColumn
cpqiScsiCxnAttrInstIndex = _CpqiScsiCxnAttrInstIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 169, 2, 12, 1, 1, 1),
    _CpqiScsiCxnAttrInstIndex_Type()
)
cpqiScsiCxnAttrInstIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqiScsiCxnAttrInstIndex.setStatus("mandatory")
_CpqiScsiCxnAttrNodeIndex_Type = Gauge32
_CpqiScsiCxnAttrNodeIndex_Object = MibTableColumn
cpqiScsiCxnAttrNodeIndex = _CpqiScsiCxnAttrNodeIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 169, 2, 12, 1, 1, 2),
    _CpqiScsiCxnAttrNodeIndex_Type()
)
cpqiScsiCxnAttrNodeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqiScsiCxnAttrNodeIndex.setStatus("mandatory")
_CpqiScsiCxnAttrSessionIndex_Type = Gauge32
_CpqiScsiCxnAttrSessionIndex_Object = MibTableColumn
cpqiScsiCxnAttrSessionIndex = _CpqiScsiCxnAttrSessionIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 169, 2, 12, 1, 1, 3),
    _CpqiScsiCxnAttrSessionIndex_Type()
)
cpqiScsiCxnAttrSessionIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqiScsiCxnAttrSessionIndex.setStatus("mandatory")
_CpqiScsiCxnAttrIndex_Type = Gauge32
_CpqiScsiCxnAttrIndex_Object = MibTableColumn
cpqiScsiCxnAttrIndex = _CpqiScsiCxnAttrIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 169, 2, 12, 1, 1, 4),
    _CpqiScsiCxnAttrIndex_Type()
)
cpqiScsiCxnAttrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqiScsiCxnAttrIndex.setStatus("mandatory")


class _CpqiScsiCxnAttrCid_Type(Integer32):
    """Custom type cpqiScsiCxnAttrCid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CpqiScsiCxnAttrCid_Type.__name__ = "Integer32"
_CpqiScsiCxnAttrCid_Object = MibTableColumn
cpqiScsiCxnAttrCid = _CpqiScsiCxnAttrCid_Object(
    (1, 3, 6, 1, 4, 1, 232, 169, 2, 12, 1, 1, 5),
    _CpqiScsiCxnAttrCid_Type()
)
cpqiScsiCxnAttrCid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqiScsiCxnAttrCid.setStatus("mandatory")


class _CpqiScsiCxnAttrState_Type(Integer32):
    """Custom type cpqiScsiCxnAttrState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("login", 1),
          ("full", 2),
          ("logout", 3))
    )


_CpqiScsiCxnAttrState_Type.__name__ = "Integer32"
_CpqiScsiCxnAttrState_Object = MibTableColumn
cpqiScsiCxnAttrState = _CpqiScsiCxnAttrState_Object(
    (1, 3, 6, 1, 4, 1, 232, 169, 2, 12, 1, 1, 6),
    _CpqiScsiCxnAttrState_Type()
)
cpqiScsiCxnAttrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqiScsiCxnAttrState.setStatus("mandatory")


class _CpqiScsiCxnAttrLocalAddrType_Type(Integer32):
    """Custom type cpqiScsiCxnAttrLocalAddrType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              16)
        )
    )
    namedValues = NamedValues(
        *(("ipv4", 1),
          ("ipv6", 2),
          ("ipv4z", 3),
          ("ipv6z", 4),
          ("dns", 16))
    )


_CpqiScsiCxnAttrLocalAddrType_Type.__name__ = "Integer32"
_CpqiScsiCxnAttrLocalAddrType_Object = MibTableColumn
cpqiScsiCxnAttrLocalAddrType = _CpqiScsiCxnAttrLocalAddrType_Object(
    (1, 3, 6, 1, 4, 1, 232, 169, 2, 12, 1, 1, 7),
    _CpqiScsiCxnAttrLocalAddrType_Type()
)
cpqiScsiCxnAttrLocalAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqiScsiCxnAttrLocalAddrType.setStatus("mandatory")


class _CpqiScsiCxnAttrLocalAddr_Type(OctetString):
    """Custom type cpqiScsiCxnAttrLocalAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqiScsiCxnAttrLocalAddr_Type.__name__ = "OctetString"
_CpqiScsiCxnAttrLocalAddr_Object = MibTableColumn
cpqiScsiCxnAttrLocalAddr = _CpqiScsiCxnAttrLocalAddr_Object(
    (1, 3, 6, 1, 4, 1, 232, 169, 2, 12, 1, 1, 8),
    _CpqiScsiCxnAttrLocalAddr_Type()
)
cpqiScsiCxnAttrLocalAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqiScsiCxnAttrLocalAddr.setStatus("mandatory")


class _CpqiScsiCxnAttrProtocol_Type(Integer32):
    """Custom type cpqiScsiCxnAttrProtocol based on Integer32"""
    defaultValue = 6

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
        *(("icmp", 1),
          ("igmp", 2),
          ("ggp", 3),
          ("ip", 4),
          ("st", 5),
          ("tcp", 6))
    )


_CpqiScsiCxnAttrProtocol_Type.__name__ = "Integer32"
_CpqiScsiCxnAttrProtocol_Object = MibTableColumn
cpqiScsiCxnAttrProtocol = _CpqiScsiCxnAttrProtocol_Object(
    (1, 3, 6, 1, 4, 1, 232, 169, 2, 12, 1, 1, 9),
    _CpqiScsiCxnAttrProtocol_Type()
)
cpqiScsiCxnAttrProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqiScsiCxnAttrProtocol.setStatus("mandatory")
_CpqiScsiCxnAttrLocalPort_Type = Gauge32
_CpqiScsiCxnAttrLocalPort_Object = MibTableColumn
cpqiScsiCxnAttrLocalPort = _CpqiScsiCxnAttrLocalPort_Object(
    (1, 3, 6, 1, 4, 1, 232, 169, 2, 12, 1, 1, 10),
    _CpqiScsiCxnAttrLocalPort_Type()
)
cpqiScsiCxnAttrLocalPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqiScsiCxnAttrLocalPort.setStatus("mandatory")


class _CpqiScsiCxnAttrRemoteAddrType_Type(Integer32):
    """Custom type cpqiScsiCxnAttrRemoteAddrType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              16)
        )
    )
    namedValues = NamedValues(
        *(("ipv4", 1),
          ("ipv6", 2),
          ("ipv4z", 3),
          ("ipv6z", 4),
          ("dns", 16))
    )


_CpqiScsiCxnAttrRemoteAddrType_Type.__name__ = "Integer32"
_CpqiScsiCxnAttrRemoteAddrType_Object = MibTableColumn
cpqiScsiCxnAttrRemoteAddrType = _CpqiScsiCxnAttrRemoteAddrType_Object(
    (1, 3, 6, 1, 4, 1, 232, 169, 2, 12, 1, 1, 11),
    _CpqiScsiCxnAttrRemoteAddrType_Type()
)
cpqiScsiCxnAttrRemoteAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqiScsiCxnAttrRemoteAddrType.setStatus("mandatory")


class _CpqiScsiCxnAttrRemoteAddr_Type(OctetString):
    """Custom type cpqiScsiCxnAttrRemoteAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpqiScsiCxnAttrRemoteAddr_Type.__name__ = "OctetString"
_CpqiScsiCxnAttrRemoteAddr_Object = MibTableColumn
cpqiScsiCxnAttrRemoteAddr = _CpqiScsiCxnAttrRemoteAddr_Object(
    (1, 3, 6, 1, 4, 1, 232, 169, 2, 12, 1, 1, 12),
    _CpqiScsiCxnAttrRemoteAddr_Type()
)
cpqiScsiCxnAttrRemoteAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqiScsiCxnAttrRemoteAddr.setStatus("mandatory")
_CpqiScsiCxnAttrRemotePort_Type = Gauge32
_CpqiScsiCxnAttrRemotePort_Object = MibTableColumn
cpqiScsiCxnAttrRemotePort = _CpqiScsiCxnAttrRemotePort_Object(
    (1, 3, 6, 1, 4, 1, 232, 169, 2, 12, 1, 1, 13),
    _CpqiScsiCxnAttrRemotePort_Type()
)
cpqiScsiCxnAttrRemotePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqiScsiCxnAttrRemotePort.setStatus("mandatory")


class _CpqiScsiCxnAttrMaxRecvDataSegLength_Type(Integer32):
    """Custom type cpqiScsiCxnAttrMaxRecvDataSegLength based on Integer32"""
    defaultValue = 8192

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(512, 16777215),
    )


_CpqiScsiCxnAttrMaxRecvDataSegLength_Type.__name__ = "Integer32"
_CpqiScsiCxnAttrMaxRecvDataSegLength_Object = MibTableColumn
cpqiScsiCxnAttrMaxRecvDataSegLength = _CpqiScsiCxnAttrMaxRecvDataSegLength_Object(
    (1, 3, 6, 1, 4, 1, 232, 169, 2, 12, 1, 1, 14),
    _CpqiScsiCxnAttrMaxRecvDataSegLength_Type()
)
cpqiScsiCxnAttrMaxRecvDataSegLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqiScsiCxnAttrMaxRecvDataSegLength.setStatus("mandatory")


class _CpqiScsiCxnAttrMaxXmitDataSegLength_Type(Integer32):
    """Custom type cpqiScsiCxnAttrMaxXmitDataSegLength based on Integer32"""
    defaultValue = 8192

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(512, 16777215),
    )


_CpqiScsiCxnAttrMaxXmitDataSegLength_Type.__name__ = "Integer32"
_CpqiScsiCxnAttrMaxXmitDataSegLength_Object = MibTableColumn
cpqiScsiCxnAttrMaxXmitDataSegLength = _CpqiScsiCxnAttrMaxXmitDataSegLength_Object(
    (1, 3, 6, 1, 4, 1, 232, 169, 2, 12, 1, 1, 15),
    _CpqiScsiCxnAttrMaxXmitDataSegLength_Type()
)
cpqiScsiCxnAttrMaxXmitDataSegLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqiScsiCxnAttrMaxXmitDataSegLength.setStatus("mandatory")


class _CpqiScsiCxnAttrHeaderIntegrity_Type(Integer32):
    """Custom type cpqiScsiCxnAttrHeaderIntegrity based on Integer32"""
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
          ("other", 2),
          ("noDigest", 3),
          ("crc32c", 4))
    )


_CpqiScsiCxnAttrHeaderIntegrity_Type.__name__ = "Integer32"
_CpqiScsiCxnAttrHeaderIntegrity_Object = MibTableColumn
cpqiScsiCxnAttrHeaderIntegrity = _CpqiScsiCxnAttrHeaderIntegrity_Object(
    (1, 3, 6, 1, 4, 1, 232, 169, 2, 12, 1, 1, 16),
    _CpqiScsiCxnAttrHeaderIntegrity_Type()
)
cpqiScsiCxnAttrHeaderIntegrity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqiScsiCxnAttrHeaderIntegrity.setStatus("mandatory")


class _CpqiScsiCxnAttrDataIntegrity_Type(Integer32):
    """Custom type cpqiScsiCxnAttrDataIntegrity based on Integer32"""
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
          ("other", 2),
          ("noDigest", 3),
          ("crc32c", 4))
    )


_CpqiScsiCxnAttrDataIntegrity_Type.__name__ = "Integer32"
_CpqiScsiCxnAttrDataIntegrity_Object = MibTableColumn
cpqiScsiCxnAttrDataIntegrity = _CpqiScsiCxnAttrDataIntegrity_Object(
    (1, 3, 6, 1, 4, 1, 232, 169, 2, 12, 1, 1, 17),
    _CpqiScsiCxnAttrDataIntegrity_Type()
)
cpqiScsiCxnAttrDataIntegrity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqiScsiCxnAttrDataIntegrity.setStatus("mandatory")


class _CpqiScsiCxnAttrRecvMarker_Type(Integer32):
    """Custom type cpqiScsiCxnAttrRecvMarker based on Integer32"""
    defaultValue = 2

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


_CpqiScsiCxnAttrRecvMarker_Type.__name__ = "Integer32"
_CpqiScsiCxnAttrRecvMarker_Object = MibTableColumn
cpqiScsiCxnAttrRecvMarker = _CpqiScsiCxnAttrRecvMarker_Object(
    (1, 3, 6, 1, 4, 1, 232, 169, 2, 12, 1, 1, 18),
    _CpqiScsiCxnAttrRecvMarker_Type()
)
cpqiScsiCxnAttrRecvMarker.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqiScsiCxnAttrRecvMarker.setStatus("mandatory")


class _CpqiScsiCxnAttrSendMarker_Type(Integer32):
    """Custom type cpqiScsiCxnAttrSendMarker based on Integer32"""
    defaultValue = 2

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


_CpqiScsiCxnAttrSendMarker_Type.__name__ = "Integer32"
_CpqiScsiCxnAttrSendMarker_Object = MibTableColumn
cpqiScsiCxnAttrSendMarker = _CpqiScsiCxnAttrSendMarker_Object(
    (1, 3, 6, 1, 4, 1, 232, 169, 2, 12, 1, 1, 19),
    _CpqiScsiCxnAttrSendMarker_Type()
)
cpqiScsiCxnAttrSendMarker.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqiScsiCxnAttrSendMarker.setStatus("mandatory")


class _CpqiScsiCxnAttrVersionActive_Type(Integer32):
    """Custom type cpqiScsiCxnAttrVersionActive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CpqiScsiCxnAttrVersionActive_Type.__name__ = "Integer32"
_CpqiScsiCxnAttrVersionActive_Object = MibTableColumn
cpqiScsiCxnAttrVersionActive = _CpqiScsiCxnAttrVersionActive_Object(
    (1, 3, 6, 1, 4, 1, 232, 169, 2, 12, 1, 1, 20),
    _CpqiScsiCxnAttrVersionActive_Type()
)
cpqiScsiCxnAttrVersionActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqiScsiCxnAttrVersionActive.setStatus("mandatory")

# Managed Objects groups


# Notification objects

cpqiScsiLinkUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 169001)
)
cpqiScsiLinkUp.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQISCSI-MIB", "cpqiScsiInstDescr"))
)
if mibBuilder.loadTexts:
    cpqiScsiLinkUp.setStatus(
        ""
    )

cpqiScsiLinkDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 169002)
)
cpqiScsiLinkDown.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQISCSI-MIB", "cpqiScsiInstDescr"))
)
if mibBuilder.loadTexts:
    cpqiScsiLinkDown.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CPQISCSI-MIB",
    **{"cpqiScsiLinkUp": cpqiScsiLinkUp,
       "cpqiScsiLinkDown": cpqiScsiLinkDown,
       "cpqiScsiModule": cpqiScsiModule,
       "cpqiScsiMibRev": cpqiScsiMibRev,
       "cpqiScsiMibRevMajor": cpqiScsiMibRevMajor,
       "cpqiScsiMibRevMinor": cpqiScsiMibRevMinor,
       "cpqiScsiMibCondition": cpqiScsiMibCondition,
       "cpqiScsiObjects": cpqiScsiObjects,
       "cpqiScsiDescriptors": cpqiScsiDescriptors,
       "cpqiScsiInstance": cpqiScsiInstance,
       "cpqiScsiInstanceAttributesTable": cpqiScsiInstanceAttributesTable,
       "cpqiScsiInstanceAttributesEntry": cpqiScsiInstanceAttributesEntry,
       "cpqiScsiInstIndex": cpqiScsiInstIndex,
       "cpqiScsiInstDescr": cpqiScsiInstDescr,
       "cpqiScsiInstVersionMin": cpqiScsiInstVersionMin,
       "cpqiScsiInstVersionMax": cpqiScsiInstVersionMax,
       "cpqiScsiInstVendorID": cpqiScsiInstVendorID,
       "cpqiScsiInstVendorVersion": cpqiScsiInstVendorVersion,
       "cpqiScsiInstPortalNumber": cpqiScsiInstPortalNumber,
       "cpqiScsiInstNodeNumber": cpqiScsiInstNodeNumber,
       "cpqiScsiInstSessionNumber": cpqiScsiInstSessionNumber,
       "cpqiScsiInstSsnFailures": cpqiScsiInstSsnFailures,
       "cpqiScsiInstLastSsnFailureType": cpqiScsiInstLastSsnFailureType,
       "cpqiScsiInstLastSsnRmtNodeName": cpqiScsiInstLastSsnRmtNodeName,
       "cpqiScsiInstanceSsnErrorStatsTable": cpqiScsiInstanceSsnErrorStatsTable,
       "cpqiScsiInstanceSsnErrorStatsEntry": cpqiScsiInstanceSsnErrorStatsEntry,
       "cpqiScsiInstSsnInstIndex": cpqiScsiInstSsnInstIndex,
       "cpqiScsiInstSsnDigestErrors": cpqiScsiInstSsnDigestErrors,
       "cpqiScsiInstSsnCxnTimeoutErrors": cpqiScsiInstSsnCxnTimeoutErrors,
       "cpqiScsiInstSsnFormatErrors": cpqiScsiInstSsnFormatErrors,
       "cpqiScsiPortal": cpqiScsiPortal,
       "cpqiScsiPortalAttributesTable": cpqiScsiPortalAttributesTable,
       "cpqiScsiPortalAttributesEntry": cpqiScsiPortalAttributesEntry,
       "cpqiScsiPortalInstIndex": cpqiScsiPortalInstIndex,
       "cpqiScsiPortalIndex": cpqiScsiPortalIndex,
       "cpqiScsiPortalRowStatus": cpqiScsiPortalRowStatus,
       "cpqiScsiPortalRoles": cpqiScsiPortalRoles,
       "cpqiScsiPortalAddrType": cpqiScsiPortalAddrType,
       "cpqiScsiPortalAddr": cpqiScsiPortalAddr,
       "cpqiScsiPortalProtocol": cpqiScsiPortalProtocol,
       "cpqiScsiPortalMaxRecvDataSegLength": cpqiScsiPortalMaxRecvDataSegLength,
       "cpqiScsiPortalPrimaryHdrDigest": cpqiScsiPortalPrimaryHdrDigest,
       "cpqiScsiPortalPrimaryDataDigest": cpqiScsiPortalPrimaryDataDigest,
       "cpqiScsiPortalSecondaryHdrDigest": cpqiScsiPortalSecondaryHdrDigest,
       "cpqiScsiPortalSecondaryDataDigest": cpqiScsiPortalSecondaryDataDigest,
       "cpqiScsiPortalRecvMarker": cpqiScsiPortalRecvMarker,
       "cpqiScsiTargetPortal": cpqiScsiTargetPortal,
       "cpqiScsiTgtPortalAttributesTable": cpqiScsiTgtPortalAttributesTable,
       "cpqiScsiTgtPortalAttributesEntry": cpqiScsiTgtPortalAttributesEntry,
       "cpqiScsiTgtPortalInstIndex": cpqiScsiTgtPortalInstIndex,
       "cpqiScsiTgtPortalPortalIndex": cpqiScsiTgtPortalPortalIndex,
       "cpqiScsiTgtPortalPort": cpqiScsiTgtPortalPort,
       "cpqiScsiTgtPortalTag": cpqiScsiTgtPortalTag,
       "cpqiScsiInitiatorPortal": cpqiScsiInitiatorPortal,
       "cpqiScsiIntrPortalAttributesTable": cpqiScsiIntrPortalAttributesTable,
       "cpqiScsiIntrPortalAttributesEntry": cpqiScsiIntrPortalAttributesEntry,
       "cpqiScsiIntrPortalInstIndex": cpqiScsiIntrPortalInstIndex,
       "cpqiScsiIntrPortalPortalIndex": cpqiScsiIntrPortalPortalIndex,
       "cpqiScsiIntrPortalTag": cpqiScsiIntrPortalTag,
       "cpqiScsiNode": cpqiScsiNode,
       "cpqiScsiNodeAttributesTable": cpqiScsiNodeAttributesTable,
       "cpqiScsiNodeAttributesEntry": cpqiScsiNodeAttributesEntry,
       "cpqiScsiNodeInstIndex": cpqiScsiNodeInstIndex,
       "cpqiScsiNodeNodeIndex": cpqiScsiNodeNodeIndex,
       "cpqiScsiNodeName": cpqiScsiNodeName,
       "cpqiScsiNodeAlias": cpqiScsiNodeAlias,
       "cpqiScsiNodeRoles": cpqiScsiNodeRoles,
       "cpqiScsiNodeTransportType": cpqiScsiNodeTransportType,
       "cpqiScsiNodeInitialR2T": cpqiScsiNodeInitialR2T,
       "cpqiScsiNodeImmediateData": cpqiScsiNodeImmediateData,
       "cpqiScsiNodeMaxOutstandingR2T": cpqiScsiNodeMaxOutstandingR2T,
       "cpqiScsiNodeFirstBurstLength": cpqiScsiNodeFirstBurstLength,
       "cpqiScsiNodeMaxBurstLength": cpqiScsiNodeMaxBurstLength,
       "cpqiScsiNodeMaxConnections": cpqiScsiNodeMaxConnections,
       "cpqiScsiNodeDataSequenceInOrder": cpqiScsiNodeDataSequenceInOrder,
       "cpqiScsiNodeDataPDUInOrder": cpqiScsiNodeDataPDUInOrder,
       "cpqiScsiNodeDefaultTime2Wait": cpqiScsiNodeDefaultTime2Wait,
       "cpqiScsiNodeDefaultTime2Retain": cpqiScsiNodeDefaultTime2Retain,
       "cpqiScsiNodeErrorRecoveryLevel": cpqiScsiNodeErrorRecoveryLevel,
       "cpqiScsiTarget": cpqiScsiTarget,
       "cpqiScsiTargetAttributesTable": cpqiScsiTargetAttributesTable,
       "cpqiScsiTargetAttributesEntry": cpqiScsiTargetAttributesEntry,
       "cpqiScsiTgtInstIndex": cpqiScsiTgtInstIndex,
       "cpqiScsiTgtNodeIndex": cpqiScsiTgtNodeIndex,
       "cpqiScsiTgtLoginFailures": cpqiScsiTgtLoginFailures,
       "cpqiScsiTgtLastFailureTime": cpqiScsiTgtLastFailureTime,
       "cpqiScsiTgtLastFailureType": cpqiScsiTgtLastFailureType,
       "cpqiScsiTgtLastIntrFailureName": cpqiScsiTgtLastIntrFailureName,
       "cpqiScsiTgtLastIntrFailureAddrType": cpqiScsiTgtLastIntrFailureAddrType,
       "cpqiScsiTgtLastIntrFailureAddr": cpqiScsiTgtLastIntrFailureAddr,
       "cpqiScsiTargetLoginStatsTable": cpqiScsiTargetLoginStatsTable,
       "cpqiScsiTargetLoginStatsEntry": cpqiScsiTargetLoginStatsEntry,
       "cpqiScsiTgtLoginInstIndex": cpqiScsiTgtLoginInstIndex,
       "cpqiScsiTgtLoginNodeIndex": cpqiScsiTgtLoginNodeIndex,
       "cpqiScsiTgtLoginAccepts": cpqiScsiTgtLoginAccepts,
       "cpqiScsiTgtLoginOtherFails": cpqiScsiTgtLoginOtherFails,
       "cpqiScsiTgtLoginRedirects": cpqiScsiTgtLoginRedirects,
       "cpqiScsiTgtLoginAuthorizeFails": cpqiScsiTgtLoginAuthorizeFails,
       "cpqiScsiTgtLoginAuthenticateFails": cpqiScsiTgtLoginAuthenticateFails,
       "cpqiScsiTgtLoginNegotiateFails": cpqiScsiTgtLoginNegotiateFails,
       "cpqiScsiTargetLogoutStatsTable": cpqiScsiTargetLogoutStatsTable,
       "cpqiScsiTargetLogoutStatsEntry": cpqiScsiTargetLogoutStatsEntry,
       "cpqiScsiTgtLogoutInstIndex": cpqiScsiTgtLogoutInstIndex,
       "cpqiScsiTgtLogoutNodeIndex": cpqiScsiTgtLogoutNodeIndex,
       "cpqiScsiTgtLogoutNormals": cpqiScsiTgtLogoutNormals,
       "cpqiScsiTgtLogoutOthers": cpqiScsiTgtLogoutOthers,
       "cpqiScsiTgtAuthorization": cpqiScsiTgtAuthorization,
       "cpqiScsiTgtAuthAttributesTable": cpqiScsiTgtAuthAttributesTable,
       "cpqiScsiTgtAuthAttributesEntry": cpqiScsiTgtAuthAttributesEntry,
       "cpqiScsiTgtAuthInstIndex": cpqiScsiTgtAuthInstIndex,
       "cpqiScsiTgtAuthNodeIndex": cpqiScsiTgtAuthNodeIndex,
       "cpqiScsiTgtAuthIndex": cpqiScsiTgtAuthIndex,
       "cpqiScsiTgtAuthRowStatus": cpqiScsiTgtAuthRowStatus,
       "cpqiScsiTgtAuthIdentity": cpqiScsiTgtAuthIdentity,
       "cpqiScsiInitiator": cpqiScsiInitiator,
       "cpqiScsiInitiatorAttributesTable": cpqiScsiInitiatorAttributesTable,
       "cpqiScsiInitiatorAttributesEntry": cpqiScsiInitiatorAttributesEntry,
       "cpqiScsiIntrInstIndex": cpqiScsiIntrInstIndex,
       "cpqiScsiIntrNodeIndex": cpqiScsiIntrNodeIndex,
       "cpqiScsiIntrLoginFailures": cpqiScsiIntrLoginFailures,
       "cpqiScsiIntrLastFailureTime": cpqiScsiIntrLastFailureTime,
       "cpqiScsiIntrLastFailureType": cpqiScsiIntrLastFailureType,
       "cpqiScsiIntrLastTgtFailureName": cpqiScsiIntrLastTgtFailureName,
       "cpqiScsiIntrLastTgtFailureAddrType": cpqiScsiIntrLastTgtFailureAddrType,
       "cpqiScsiIntrLastTgtFailureAddr": cpqiScsiIntrLastTgtFailureAddr,
       "cpqiScsiInitiatorLoginStatsTable": cpqiScsiInitiatorLoginStatsTable,
       "cpqiScsiInitiatorLoginStatsEntry": cpqiScsiInitiatorLoginStatsEntry,
       "cpqiScsiIntrLoginInstIndex": cpqiScsiIntrLoginInstIndex,
       "cpqiScsiIntrLoginNodeIndex": cpqiScsiIntrLoginNodeIndex,
       "cpqiScsiIntrLoginAcceptRsps": cpqiScsiIntrLoginAcceptRsps,
       "cpqiScsiIntrLoginOtherFailRsps": cpqiScsiIntrLoginOtherFailRsps,
       "cpqiScsiIntrLoginRedirectRsps": cpqiScsiIntrLoginRedirectRsps,
       "cpqiScsiIntrLoginAuthFailRsps": cpqiScsiIntrLoginAuthFailRsps,
       "cpqiScsiIntrLoginAuthenticateFails": cpqiScsiIntrLoginAuthenticateFails,
       "cpqiScsiIntrLoginNegotiateFails": cpqiScsiIntrLoginNegotiateFails,
       "cpqiScsiInitiatorLogoutStatsTable": cpqiScsiInitiatorLogoutStatsTable,
       "cpqiScsiInitiatorLogoutStatsEntry": cpqiScsiInitiatorLogoutStatsEntry,
       "cpqiScsiIntrLogoutInstIndex": cpqiScsiIntrLogoutInstIndex,
       "cpqiScsiIntrLogoutNodeIndex": cpqiScsiIntrLogoutNodeIndex,
       "cpqiScsiIntrLogoutNormals": cpqiScsiIntrLogoutNormals,
       "cpqiScsiIntrLogoutOthers": cpqiScsiIntrLogoutOthers,
       "cpqiScsiIntrAuthorization": cpqiScsiIntrAuthorization,
       "cpqiScsiIntrAuthAttributesTable": cpqiScsiIntrAuthAttributesTable,
       "cpqiScsiIntrAuthAttributesEntry": cpqiScsiIntrAuthAttributesEntry,
       "cpqiScsiIntrAuthInstIndex": cpqiScsiIntrAuthInstIndex,
       "cpqiScsiIntrAuthNodeIndex": cpqiScsiIntrAuthNodeIndex,
       "cpqiScsiIntrAuthIndex": cpqiScsiIntrAuthIndex,
       "cpqiScsiIntrAuthRowStatus": cpqiScsiIntrAuthRowStatus,
       "cpqiScsiIntrAuthIdentity": cpqiScsiIntrAuthIdentity,
       "cpqiScsiSession": cpqiScsiSession,
       "cpqiScsiSessionAttributesTable": cpqiScsiSessionAttributesTable,
       "cpqiScsiSessionAttributesEntry": cpqiScsiSessionAttributesEntry,
       "cpqiScsiSsnInstIndex": cpqiScsiSsnInstIndex,
       "cpqiScsiSsnNodeIndex": cpqiScsiSsnNodeIndex,
       "cpqiScsiSsnIndex": cpqiScsiSsnIndex,
       "cpqiScsiSsnDirection": cpqiScsiSsnDirection,
       "cpqiScsiSsnInitiatorName": cpqiScsiSsnInitiatorName,
       "cpqiScsiSsnTargetName": cpqiScsiSsnTargetName,
       "cpqiScsiSsnTSIH": cpqiScsiSsnTSIH,
       "cpqiScsiSsnISID": cpqiScsiSsnISID,
       "cpqiScsiSsnInitiatorAlias": cpqiScsiSsnInitiatorAlias,
       "cpqiScsiSsnTargetAlias": cpqiScsiSsnTargetAlias,
       "cpqiScsiSsnInitialR2T": cpqiScsiSsnInitialR2T,
       "cpqiScsiSsnImmediateData": cpqiScsiSsnImmediateData,
       "cpqiScsiSsnType": cpqiScsiSsnType,
       "cpqiScsiSsnMaxOutstandingR2T": cpqiScsiSsnMaxOutstandingR2T,
       "cpqiScsiSsnFirstBurstLength": cpqiScsiSsnFirstBurstLength,
       "cpqiScsiSsnMaxBurstLength": cpqiScsiSsnMaxBurstLength,
       "cpqiScsiSsnConnectionNumber": cpqiScsiSsnConnectionNumber,
       "cpqiScsiSsnAuthIdentity": cpqiScsiSsnAuthIdentity,
       "cpqiScsiSsnDataSequenceInOrder": cpqiScsiSsnDataSequenceInOrder,
       "cpqiScsiSsnDataPDUInOrder": cpqiScsiSsnDataPDUInOrder,
       "cpqiScsiSsnErrorRecoveryLevel": cpqiScsiSsnErrorRecoveryLevel,
       "cpqiScsiSessionId": cpqiScsiSessionId,
       "cpqiScsiSessionStatsTable": cpqiScsiSessionStatsTable,
       "cpqiScsiSessionStatsEntry": cpqiScsiSessionStatsEntry,
       "cpqiScsiSsnStatInstIndex": cpqiScsiSsnStatInstIndex,
       "cpqiScsiSsnStatNodeIndex": cpqiScsiSsnStatNodeIndex,
       "cpqiScsiSsnSessionIndex": cpqiScsiSsnSessionIndex,
       "cpqiScsiSsnCmdPDUs": cpqiScsiSsnCmdPDUs,
       "cpqiScsiSsnRspPDUs": cpqiScsiSsnRspPDUs,
       "cpqiScsiSsnTxDataOctets": cpqiScsiSsnTxDataOctets,
       "cpqiScsiSsnRxDataOctets": cpqiScsiSsnRxDataOctets,
       "cpqiScsiSsnLCTxDataOctets": cpqiScsiSsnLCTxDataOctets,
       "cpqiScsiSsnLCRxDataOctets": cpqiScsiSsnLCRxDataOctets,
       "cpqiScsiSessionCxnErrorStatsTable": cpqiScsiSessionCxnErrorStatsTable,
       "cpqiScsiSessionCxnErrorStatsEntry": cpqiScsiSessionCxnErrorStatsEntry,
       "cpqiScsiSsnCxnInstIndex": cpqiScsiSsnCxnInstIndex,
       "cpqiScsiSsnCxnNodeIndex": cpqiScsiSsnCxnNodeIndex,
       "cpqiScsiSsnCxnIndex": cpqiScsiSsnCxnIndex,
       "cpqiScsiSsnCxnDigestErrors": cpqiScsiSsnCxnDigestErrors,
       "cpqiScsiSsnCxnTimeoutErrors": cpqiScsiSsnCxnTimeoutErrors,
       "cpqiScsiConnection": cpqiScsiConnection,
       "cpqiScsiConnectionAttributesTable": cpqiScsiConnectionAttributesTable,
       "cpqiScsiConnectionAttributesEntry": cpqiScsiConnectionAttributesEntry,
       "cpqiScsiCxnAttrInstIndex": cpqiScsiCxnAttrInstIndex,
       "cpqiScsiCxnAttrNodeIndex": cpqiScsiCxnAttrNodeIndex,
       "cpqiScsiCxnAttrSessionIndex": cpqiScsiCxnAttrSessionIndex,
       "cpqiScsiCxnAttrIndex": cpqiScsiCxnAttrIndex,
       "cpqiScsiCxnAttrCid": cpqiScsiCxnAttrCid,
       "cpqiScsiCxnAttrState": cpqiScsiCxnAttrState,
       "cpqiScsiCxnAttrLocalAddrType": cpqiScsiCxnAttrLocalAddrType,
       "cpqiScsiCxnAttrLocalAddr": cpqiScsiCxnAttrLocalAddr,
       "cpqiScsiCxnAttrProtocol": cpqiScsiCxnAttrProtocol,
       "cpqiScsiCxnAttrLocalPort": cpqiScsiCxnAttrLocalPort,
       "cpqiScsiCxnAttrRemoteAddrType": cpqiScsiCxnAttrRemoteAddrType,
       "cpqiScsiCxnAttrRemoteAddr": cpqiScsiCxnAttrRemoteAddr,
       "cpqiScsiCxnAttrRemotePort": cpqiScsiCxnAttrRemotePort,
       "cpqiScsiCxnAttrMaxRecvDataSegLength": cpqiScsiCxnAttrMaxRecvDataSegLength,
       "cpqiScsiCxnAttrMaxXmitDataSegLength": cpqiScsiCxnAttrMaxXmitDataSegLength,
       "cpqiScsiCxnAttrHeaderIntegrity": cpqiScsiCxnAttrHeaderIntegrity,
       "cpqiScsiCxnAttrDataIntegrity": cpqiScsiCxnAttrDataIntegrity,
       "cpqiScsiCxnAttrRecvMarker": cpqiScsiCxnAttrRecvMarker,
       "cpqiScsiCxnAttrSendMarker": cpqiScsiCxnAttrSendMarker,
       "cpqiScsiCxnAttrVersionActive": cpqiScsiCxnAttrVersionActive}
)
