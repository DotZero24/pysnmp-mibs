# SNMP MIB module (ISCSI-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/equallogic/ISCSI-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:21:59 2025
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

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 experimental,
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
    "experimental",
    "iso")

(DisplayString,
 PhysAddress,
 RowPointer,
 RowStatus,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowPointer",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

iscsiModule = ModuleIdentity(
    (1, 3, 6, 1, 3, 9999)
)
if mibBuilder.loadTexts:
    iscsiModule.setRevisions(
        ("2002-06-26 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class IscsiTransportProtocols(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )



class IscsiDigestMethod(TextualConvention, Integer32):
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
        *(("none", 1),
          ("other", 2),
          ("noDigest", 3),
          ("crc32c", 4))
    )



# MIB Managed Objects in the order of their OIDs

_IscsiObjects_ObjectIdentity = ObjectIdentity
iscsiObjects = _IscsiObjects_ObjectIdentity(
    (1, 3, 6, 1, 3, 9999, 1)
)
_IscsiDescriptors_ObjectIdentity = ObjectIdentity
iscsiDescriptors = _IscsiDescriptors_ObjectIdentity(
    (1, 3, 6, 1, 3, 9999, 1, 1)
)
_IscsiHeaderIntegrityTypes_ObjectIdentity = ObjectIdentity
iscsiHeaderIntegrityTypes = _IscsiHeaderIntegrityTypes_ObjectIdentity(
    (1, 3, 6, 1, 3, 9999, 1, 1, 1)
)
_IscsiHdrIntegrityNone_ObjectIdentity = ObjectIdentity
iscsiHdrIntegrityNone = _IscsiHdrIntegrityNone_ObjectIdentity(
    (1, 3, 6, 1, 3, 9999, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    iscsiHdrIntegrityNone.setStatus("current")
_IscsiHdrIntegrityCrc32c_ObjectIdentity = ObjectIdentity
iscsiHdrIntegrityCrc32c = _IscsiHdrIntegrityCrc32c_ObjectIdentity(
    (1, 3, 6, 1, 3, 9999, 1, 1, 1, 2)
)
if mibBuilder.loadTexts:
    iscsiHdrIntegrityCrc32c.setStatus("current")
_IscsiDataIntegrityTypes_ObjectIdentity = ObjectIdentity
iscsiDataIntegrityTypes = _IscsiDataIntegrityTypes_ObjectIdentity(
    (1, 3, 6, 1, 3, 9999, 1, 1, 2)
)
_IscsiDataIntegrityNone_ObjectIdentity = ObjectIdentity
iscsiDataIntegrityNone = _IscsiDataIntegrityNone_ObjectIdentity(
    (1, 3, 6, 1, 3, 9999, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    iscsiDataIntegrityNone.setStatus("current")
_IscsiDataIntegrityCrc32c_ObjectIdentity = ObjectIdentity
iscsiDataIntegrityCrc32c = _IscsiDataIntegrityCrc32c_ObjectIdentity(
    (1, 3, 6, 1, 3, 9999, 1, 1, 2, 2)
)
if mibBuilder.loadTexts:
    iscsiDataIntegrityCrc32c.setStatus("current")
_IscsiInstance_ObjectIdentity = ObjectIdentity
iscsiInstance = _IscsiInstance_ObjectIdentity(
    (1, 3, 6, 1, 3, 9999, 1, 2)
)
_IscsiInstanceAttributesTable_Object = MibTable
iscsiInstanceAttributesTable = _IscsiInstanceAttributesTable_Object(
    (1, 3, 6, 1, 3, 9999, 1, 2, 1)
)
if mibBuilder.loadTexts:
    iscsiInstanceAttributesTable.setStatus("current")
_IscsiInstanceAttributesEntry_Object = MibTableRow
iscsiInstanceAttributesEntry = _IscsiInstanceAttributesEntry_Object(
    (1, 3, 6, 1, 3, 9999, 1, 2, 1, 1)
)
iscsiInstanceAttributesEntry.setIndexNames(
    (0, "ISCSI-MIB", "iscsiInstIndex"),
)
if mibBuilder.loadTexts:
    iscsiInstanceAttributesEntry.setStatus("current")


class _IscsiInstIndex_Type(Unsigned32):
    """Custom type iscsiInstIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_IscsiInstIndex_Type.__name__ = "Unsigned32"
_IscsiInstIndex_Object = MibTableColumn
iscsiInstIndex = _IscsiInstIndex_Object(
    (1, 3, 6, 1, 3, 9999, 1, 2, 1, 1, 1),
    _IscsiInstIndex_Type()
)
iscsiInstIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    iscsiInstIndex.setStatus("current")
_IscsiInstDescr_Type = SnmpAdminString
_IscsiInstDescr_Object = MibTableColumn
iscsiInstDescr = _IscsiInstDescr_Object(
    (1, 3, 6, 1, 3, 9999, 1, 2, 1, 1, 2),
    _IscsiInstDescr_Type()
)
iscsiInstDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsiInstDescr.setStatus("current")


class _IscsiInstVersionMin_Type(Integer32):
    """Custom type iscsiInstVersionMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IscsiInstVersionMin_Type.__name__ = "Integer32"
_IscsiInstVersionMin_Object = MibTableColumn
iscsiInstVersionMin = _IscsiInstVersionMin_Object(
    (1, 3, 6, 1, 3, 9999, 1, 2, 1, 1, 3),
    _IscsiInstVersionMin_Type()
)
iscsiInstVersionMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsiInstVersionMin.setStatus("current")


class _IscsiInstVersionMax_Type(Integer32):
    """Custom type iscsiInstVersionMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IscsiInstVersionMax_Type.__name__ = "Integer32"
_IscsiInstVersionMax_Object = MibTableColumn
iscsiInstVersionMax = _IscsiInstVersionMax_Object(
    (1, 3, 6, 1, 3, 9999, 1, 2, 1, 1, 4),
    _IscsiInstVersionMax_Type()
)
iscsiInstVersionMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsiInstVersionMax.setStatus("current")
_IscsiInstVendorID_Type = SnmpAdminString
_IscsiInstVendorID_Object = MibTableColumn
iscsiInstVendorID = _IscsiInstVendorID_Object(
    (1, 3, 6, 1, 3, 9999, 1, 2, 1, 1, 5),
    _IscsiInstVendorID_Type()
)
iscsiInstVendorID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsiInstVendorID.setStatus("current")
_IscsiInstVendorVersion_Type = SnmpAdminString
_IscsiInstVendorVersion_Object = MibTableColumn
iscsiInstVendorVersion = _IscsiInstVendorVersion_Object(
    (1, 3, 6, 1, 3, 9999, 1, 2, 1, 1, 6),
    _IscsiInstVendorVersion_Type()
)
iscsiInstVendorVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsiInstVendorVersion.setStatus("current")


class _IscsiInstPortalNumber_Type(Unsigned32):
    """Custom type iscsiInstPortalNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_IscsiInstPortalNumber_Type.__name__ = "Unsigned32"
_IscsiInstPortalNumber_Object = MibTableColumn
iscsiInstPortalNumber = _IscsiInstPortalNumber_Object(
    (1, 3, 6, 1, 3, 9999, 1, 2, 1, 1, 7),
    _IscsiInstPortalNumber_Type()
)
iscsiInstPortalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsiInstPortalNumber.setStatus("current")
if mibBuilder.loadTexts:
    iscsiInstPortalNumber.setUnits("transport endpoints")


class _IscsiInstNodeNumber_Type(Unsigned32):
    """Custom type iscsiInstNodeNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_IscsiInstNodeNumber_Type.__name__ = "Unsigned32"
_IscsiInstNodeNumber_Object = MibTableColumn
iscsiInstNodeNumber = _IscsiInstNodeNumber_Object(
    (1, 3, 6, 1, 3, 9999, 1, 2, 1, 1, 8),
    _IscsiInstNodeNumber_Type()
)
iscsiInstNodeNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsiInstNodeNumber.setStatus("current")
if mibBuilder.loadTexts:
    iscsiInstNodeNumber.setUnits("Internet Network Addresses")


class _IscsiInstSessionNumber_Type(Unsigned32):
    """Custom type iscsiInstSessionNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_IscsiInstSessionNumber_Type.__name__ = "Unsigned32"
_IscsiInstSessionNumber_Object = MibTableColumn
iscsiInstSessionNumber = _IscsiInstSessionNumber_Object(
    (1, 3, 6, 1, 3, 9999, 1, 2, 1, 1, 9),
    _IscsiInstSessionNumber_Type()
)
iscsiInstSessionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsiInstSessionNumber.setStatus("current")
if mibBuilder.loadTexts:
    iscsiInstSessionNumber.setUnits("sessions")
_IscsiInstSsnFailures_Type = Counter32
_IscsiInstSsnFailures_Object = MibTableColumn
iscsiInstSsnFailures = _IscsiInstSsnFailures_Object(
    (1, 3, 6, 1, 3, 9999, 1, 2, 1, 1, 10),
    _IscsiInstSsnFailures_Type()
)
iscsiInstSsnFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsiInstSsnFailures.setStatus("current")
if mibBuilder.loadTexts:
    iscsiInstSsnFailures.setUnits("sessions")
_IscsiInstLastSsnFailureType_Type = Integer32
_IscsiInstLastSsnFailureType_Object = MibTableColumn
iscsiInstLastSsnFailureType = _IscsiInstLastSsnFailureType_Object(
    (1, 3, 6, 1, 3, 9999, 1, 2, 1, 1, 11),
    _IscsiInstLastSsnFailureType_Type()
)
iscsiInstLastSsnFailureType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsiInstLastSsnFailureType.setStatus("current")
_IscsiInstLastSsnRmtNodeName_Type = SnmpAdminString
_IscsiInstLastSsnRmtNodeName_Object = MibTableColumn
iscsiInstLastSsnRmtNodeName = _IscsiInstLastSsnRmtNodeName_Object(
    (1, 3, 6, 1, 3, 9999, 1, 2, 1, 1, 12),
    _IscsiInstLastSsnRmtNodeName_Type()
)
iscsiInstLastSsnRmtNodeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsiInstLastSsnRmtNodeName.setStatus("current")
_IscsiInstanceSsnErrorStatsTable_Object = MibTable
iscsiInstanceSsnErrorStatsTable = _IscsiInstanceSsnErrorStatsTable_Object(
    (1, 3, 6, 1, 3, 9999, 1, 2, 2)
)
if mibBuilder.loadTexts:
    iscsiInstanceSsnErrorStatsTable.setStatus("current")
_IscsiInstanceSsnErrorStatsEntry_Object = MibTableRow
iscsiInstanceSsnErrorStatsEntry = _IscsiInstanceSsnErrorStatsEntry_Object(
    (1, 3, 6, 1, 3, 9999, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    iscsiInstanceSsnErrorStatsEntry.setStatus("current")
_IscsiInstSsnDigestErrors_Type = Counter32
_IscsiInstSsnDigestErrors_Object = MibTableColumn
iscsiInstSsnDigestErrors = _IscsiInstSsnDigestErrors_Object(
    (1, 3, 6, 1, 3, 9999, 1, 2, 2, 1, 1),
    _IscsiInstSsnDigestErrors_Type()
)
iscsiInstSsnDigestErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsiInstSsnDigestErrors.setStatus("current")
if mibBuilder.loadTexts:
    iscsiInstSsnDigestErrors.setUnits("sessions")
_IscsiInstSsnCxnTimeoutErrors_Type = Counter32
_IscsiInstSsnCxnTimeoutErrors_Object = MibTableColumn
iscsiInstSsnCxnTimeoutErrors = _IscsiInstSsnCxnTimeoutErrors_Object(
    (1, 3, 6, 1, 3, 9999, 1, 2, 2, 1, 2),
    _IscsiInstSsnCxnTimeoutErrors_Type()
)
iscsiInstSsnCxnTimeoutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsiInstSsnCxnTimeoutErrors.setStatus("current")
if mibBuilder.loadTexts:
    iscsiInstSsnCxnTimeoutErrors.setUnits("sessions")
_IscsiInstSsnFormatErrors_Type = Counter32
_IscsiInstSsnFormatErrors_Object = MibTableColumn
iscsiInstSsnFormatErrors = _IscsiInstSsnFormatErrors_Object(
    (1, 3, 6, 1, 3, 9999, 1, 2, 2, 1, 3),
    _IscsiInstSsnFormatErrors_Type()
)
iscsiInstSsnFormatErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsiInstSsnFormatErrors.setStatus("current")
if mibBuilder.loadTexts:
    iscsiInstSsnFormatErrors.setUnits("sessions")
_IscsiPortal_ObjectIdentity = ObjectIdentity
iscsiPortal = _IscsiPortal_ObjectIdentity(
    (1, 3, 6, 1, 3, 9999, 1, 3)
)
_IscsiPortalAttributesTable_Object = MibTable
iscsiPortalAttributesTable = _IscsiPortalAttributesTable_Object(
    (1, 3, 6, 1, 3, 9999, 1, 3, 1)
)
if mibBuilder.loadTexts:
    iscsiPortalAttributesTable.setStatus("current")
_IscsiPortalAttributesEntry_Object = MibTableRow
iscsiPortalAttributesEntry = _IscsiPortalAttributesEntry_Object(
    (1, 3, 6, 1, 3, 9999, 1, 3, 1, 1)
)
iscsiPortalAttributesEntry.setIndexNames(
    (0, "ISCSI-MIB", "iscsiInstIndex"),
    (0, "ISCSI-MIB", "iscsiPortalIndex"),
)
if mibBuilder.loadTexts:
    iscsiPortalAttributesEntry.setStatus("current")


class _IscsiPortalIndex_Type(Unsigned32):
    """Custom type iscsiPortalIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_IscsiPortalIndex_Type.__name__ = "Unsigned32"
_IscsiPortalIndex_Object = MibTableColumn
iscsiPortalIndex = _IscsiPortalIndex_Object(
    (1, 3, 6, 1, 3, 9999, 1, 3, 1, 1, 1),
    _IscsiPortalIndex_Type()
)
iscsiPortalIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    iscsiPortalIndex.setStatus("current")


class _IscsiPortalRoles_Type(Bits):
    """Custom type iscsiPortalRoles based on Bits"""
    namedValues = NamedValues(
        *(("targetTypePortal", 0),
          ("initiatorTypePortal", 1))
    )

_IscsiPortalRoles_Type.__name__ = "Bits"
_IscsiPortalRoles_Object = MibTableColumn
iscsiPortalRoles = _IscsiPortalRoles_Object(
    (1, 3, 6, 1, 3, 9999, 1, 3, 1, 1, 3),
    _IscsiPortalRoles_Type()
)
iscsiPortalRoles.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    iscsiPortalRoles.setStatus("current")
_IscsiPortalAddrType_Type = InetAddressType
_IscsiPortalAddrType_Object = MibTableColumn
iscsiPortalAddrType = _IscsiPortalAddrType_Object(
    (1, 3, 6, 1, 3, 9999, 1, 3, 1, 1, 4),
    _IscsiPortalAddrType_Type()
)
iscsiPortalAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    iscsiPortalAddrType.setStatus("current")
_IscsiPortalAddr_Type = InetAddress
_IscsiPortalAddr_Object = MibTableColumn
iscsiPortalAddr = _IscsiPortalAddr_Object(
    (1, 3, 6, 1, 3, 9999, 1, 3, 1, 1, 5),
    _IscsiPortalAddr_Type()
)
iscsiPortalAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    iscsiPortalAddr.setStatus("current")


class _IscsiPortalProtocol_Type(IscsiTransportProtocols):
    """Custom type iscsiPortalProtocol based on IscsiTransportProtocols"""
    defaultValue = 6


_IscsiPortalProtocol_Type.__name__ = "IscsiTransportProtocols"
_IscsiPortalProtocol_Object = MibTableColumn
iscsiPortalProtocol = _IscsiPortalProtocol_Object(
    (1, 3, 6, 1, 3, 9999, 1, 3, 1, 1, 6),
    _IscsiPortalProtocol_Type()
)
iscsiPortalProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    iscsiPortalProtocol.setStatus("current")


class _IscsiPortalMaxRecvDataSegLength_Type(Integer32):
    """Custom type iscsiPortalMaxRecvDataSegLength based on Integer32"""
    defaultValue = 8192

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(512, 16777215),
    )


_IscsiPortalMaxRecvDataSegLength_Type.__name__ = "Integer32"
_IscsiPortalMaxRecvDataSegLength_Object = MibTableColumn
iscsiPortalMaxRecvDataSegLength = _IscsiPortalMaxRecvDataSegLength_Object(
    (1, 3, 6, 1, 3, 9999, 1, 3, 1, 1, 7),
    _IscsiPortalMaxRecvDataSegLength_Type()
)
iscsiPortalMaxRecvDataSegLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    iscsiPortalMaxRecvDataSegLength.setStatus("current")


class _IscsiPortalPrimaryHdrDigest_Type(IscsiDigestMethod):
    """Custom type iscsiPortalPrimaryHdrDigest based on IscsiDigestMethod"""
    defaultValue = 3


_IscsiPortalPrimaryHdrDigest_Type.__name__ = "IscsiDigestMethod"
_IscsiPortalPrimaryHdrDigest_Object = MibTableColumn
iscsiPortalPrimaryHdrDigest = _IscsiPortalPrimaryHdrDigest_Object(
    (1, 3, 6, 1, 3, 9999, 1, 3, 1, 1, 8),
    _IscsiPortalPrimaryHdrDigest_Type()
)
iscsiPortalPrimaryHdrDigest.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    iscsiPortalPrimaryHdrDigest.setStatus("current")


class _IscsiPortalPrimaryDataDigest_Type(IscsiDigestMethod):
    """Custom type iscsiPortalPrimaryDataDigest based on IscsiDigestMethod"""
    defaultValue = 3


_IscsiPortalPrimaryDataDigest_Type.__name__ = "IscsiDigestMethod"
_IscsiPortalPrimaryDataDigest_Object = MibTableColumn
iscsiPortalPrimaryDataDigest = _IscsiPortalPrimaryDataDigest_Object(
    (1, 3, 6, 1, 3, 9999, 1, 3, 1, 1, 9),
    _IscsiPortalPrimaryDataDigest_Type()
)
iscsiPortalPrimaryDataDigest.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    iscsiPortalPrimaryDataDigest.setStatus("current")


class _IscsiPortalSecondaryHdrDigest_Type(IscsiDigestMethod):
    """Custom type iscsiPortalSecondaryHdrDigest based on IscsiDigestMethod"""
    defaultValue = 1


_IscsiPortalSecondaryHdrDigest_Type.__name__ = "IscsiDigestMethod"
_IscsiPortalSecondaryHdrDigest_Object = MibTableColumn
iscsiPortalSecondaryHdrDigest = _IscsiPortalSecondaryHdrDigest_Object(
    (1, 3, 6, 1, 3, 9999, 1, 3, 1, 1, 10),
    _IscsiPortalSecondaryHdrDigest_Type()
)
iscsiPortalSecondaryHdrDigest.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    iscsiPortalSecondaryHdrDigest.setStatus("current")


class _IscsiPortalSecondaryDataDigest_Type(IscsiDigestMethod):
    """Custom type iscsiPortalSecondaryDataDigest based on IscsiDigestMethod"""
    defaultValue = 1


_IscsiPortalSecondaryDataDigest_Type.__name__ = "IscsiDigestMethod"
_IscsiPortalSecondaryDataDigest_Object = MibTableColumn
iscsiPortalSecondaryDataDigest = _IscsiPortalSecondaryDataDigest_Object(
    (1, 3, 6, 1, 3, 9999, 1, 3, 1, 1, 11),
    _IscsiPortalSecondaryDataDigest_Type()
)
iscsiPortalSecondaryDataDigest.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    iscsiPortalSecondaryDataDigest.setStatus("current")
_IscsiPortalRecvMarker_Type = TruthValue
_IscsiPortalRecvMarker_Object = MibTableColumn
iscsiPortalRecvMarker = _IscsiPortalRecvMarker_Object(
    (1, 3, 6, 1, 3, 9999, 1, 3, 1, 1, 12),
    _IscsiPortalRecvMarker_Type()
)
iscsiPortalRecvMarker.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    iscsiPortalRecvMarker.setStatus("current")
_IscsiTargetPortal_ObjectIdentity = ObjectIdentity
iscsiTargetPortal = _IscsiTargetPortal_ObjectIdentity(
    (1, 3, 6, 1, 3, 9999, 1, 4)
)
_IscsiTgtPortalAttributesTable_Object = MibTable
iscsiTgtPortalAttributesTable = _IscsiTgtPortalAttributesTable_Object(
    (1, 3, 6, 1, 3, 9999, 1, 4, 1)
)
if mibBuilder.loadTexts:
    iscsiTgtPortalAttributesTable.setStatus("current")
_IscsiTgtPortalAttributesEntry_Object = MibTableRow
iscsiTgtPortalAttributesEntry = _IscsiTgtPortalAttributesEntry_Object(
    (1, 3, 6, 1, 3, 9999, 1, 4, 1, 1)
)
iscsiTgtPortalAttributesEntry.setIndexNames(
    (0, "ISCSI-MIB", "iscsiInstIndex"),
    (0, "ISCSI-MIB", "iscsiPortalIndex"),
)
if mibBuilder.loadTexts:
    iscsiTgtPortalAttributesEntry.setStatus("current")


class _IscsiTgtPortalPort_Type(Unsigned32):
    """Custom type iscsiTgtPortalPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_IscsiTgtPortalPort_Type.__name__ = "Unsigned32"
_IscsiTgtPortalPort_Object = MibTableColumn
iscsiTgtPortalPort = _IscsiTgtPortalPort_Object(
    (1, 3, 6, 1, 3, 9999, 1, 4, 1, 1, 1),
    _IscsiTgtPortalPort_Type()
)
iscsiTgtPortalPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iscsiTgtPortalPort.setStatus("current")


class _IscsiTgtPortalTag_Type(Integer32):
    """Custom type iscsiTgtPortalTag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_IscsiTgtPortalTag_Type.__name__ = "Integer32"
_IscsiTgtPortalTag_Object = MibTableColumn
iscsiTgtPortalTag = _IscsiTgtPortalTag_Object(
    (1, 3, 6, 1, 3, 9999, 1, 4, 1, 1, 2),
    _IscsiTgtPortalTag_Type()
)
iscsiTgtPortalTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iscsiTgtPortalTag.setStatus("current")
_IscsiInitiatorPortal_ObjectIdentity = ObjectIdentity
iscsiInitiatorPortal = _IscsiInitiatorPortal_ObjectIdentity(
    (1, 3, 6, 1, 3, 9999, 1, 5)
)
_IscsiIntrPortalAttributesTable_Object = MibTable
iscsiIntrPortalAttributesTable = _IscsiIntrPortalAttributesTable_Object(
    (1, 3, 6, 1, 3, 9999, 1, 5, 1)
)
if mibBuilder.loadTexts:
    iscsiIntrPortalAttributesTable.setStatus("current")
_IscsiIntrPortalAttributesEntry_Object = MibTableRow
iscsiIntrPortalAttributesEntry = _IscsiIntrPortalAttributesEntry_Object(
    (1, 3, 6, 1, 3, 9999, 1, 5, 1, 1)
)
iscsiIntrPortalAttributesEntry.setIndexNames(
    (0, "ISCSI-MIB", "iscsiInstIndex"),
    (0, "ISCSI-MIB", "iscsiPortalIndex"),
)
if mibBuilder.loadTexts:
    iscsiIntrPortalAttributesEntry.setStatus("current")


class _IscsiIntrPortalTag_Type(Integer32):
    """Custom type iscsiIntrPortalTag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_IscsiIntrPortalTag_Type.__name__ = "Integer32"
_IscsiIntrPortalTag_Object = MibTableColumn
iscsiIntrPortalTag = _IscsiIntrPortalTag_Object(
    (1, 3, 6, 1, 3, 9999, 1, 5, 1, 1, 1),
    _IscsiIntrPortalTag_Type()
)
iscsiIntrPortalTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iscsiIntrPortalTag.setStatus("current")
_IscsiNode_ObjectIdentity = ObjectIdentity
iscsiNode = _IscsiNode_ObjectIdentity(
    (1, 3, 6, 1, 3, 9999, 1, 6)
)
_IscsiNodeAttributesTable_Object = MibTable
iscsiNodeAttributesTable = _IscsiNodeAttributesTable_Object(
    (1, 3, 6, 1, 3, 9999, 1, 6, 1)
)
if mibBuilder.loadTexts:
    iscsiNodeAttributesTable.setStatus("current")
_IscsiNodeAttributesEntry_Object = MibTableRow
iscsiNodeAttributesEntry = _IscsiNodeAttributesEntry_Object(
    (1, 3, 6, 1, 3, 9999, 1, 6, 1, 1)
)
iscsiNodeAttributesEntry.setIndexNames(
    (0, "ISCSI-MIB", "iscsiInstIndex"),
    (0, "ISCSI-MIB", "iscsiNodeIndex"),
)
if mibBuilder.loadTexts:
    iscsiNodeAttributesEntry.setStatus("current")


class _IscsiNodeIndex_Type(Unsigned32):
    """Custom type iscsiNodeIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_IscsiNodeIndex_Type.__name__ = "Unsigned32"
_IscsiNodeIndex_Object = MibTableColumn
iscsiNodeIndex = _IscsiNodeIndex_Object(
    (1, 3, 6, 1, 3, 9999, 1, 6, 1, 1, 1),
    _IscsiNodeIndex_Type()
)
iscsiNodeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    iscsiNodeIndex.setStatus("current")
_IscsiNodeName_Type = SnmpAdminString
_IscsiNodeName_Object = MibTableColumn
iscsiNodeName = _IscsiNodeName_Object(
    (1, 3, 6, 1, 3, 9999, 1, 6, 1, 1, 2),
    _IscsiNodeName_Type()
)
iscsiNodeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsiNodeName.setStatus("current")
_IscsiNodeAlias_Type = SnmpAdminString
_IscsiNodeAlias_Object = MibTableColumn
iscsiNodeAlias = _IscsiNodeAlias_Object(
    (1, 3, 6, 1, 3, 9999, 1, 6, 1, 1, 3),
    _IscsiNodeAlias_Type()
)
iscsiNodeAlias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsiNodeAlias.setStatus("current")


class _IscsiNodeRoles_Type(Bits):
    """Custom type iscsiNodeRoles based on Bits"""
    namedValues = NamedValues(
        *(("targetTypeNode", 0),
          ("initiatorTypeNode", 1))
    )

_IscsiNodeRoles_Type.__name__ = "Bits"
_IscsiNodeRoles_Object = MibTableColumn
iscsiNodeRoles = _IscsiNodeRoles_Object(
    (1, 3, 6, 1, 3, 9999, 1, 6, 1, 1, 4),
    _IscsiNodeRoles_Type()
)
iscsiNodeRoles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsiNodeRoles.setStatus("current")
_IscsiNodeTransportType_Type = RowPointer
_IscsiNodeTransportType_Object = MibTableColumn
iscsiNodeTransportType = _IscsiNodeTransportType_Object(
    (1, 3, 6, 1, 3, 9999, 1, 6, 1, 1, 5),
    _IscsiNodeTransportType_Type()
)
iscsiNodeTransportType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsiNodeTransportType.setStatus("current")


class _IscsiNodeInitialR2T_Type(TruthValue):
    """Custom type iscsiNodeInitialR2T based on TruthValue"""
    defaultValue = 1


_IscsiNodeInitialR2T_Type.__name__ = "TruthValue"
_IscsiNodeInitialR2T_Object = MibTableColumn
iscsiNodeInitialR2T = _IscsiNodeInitialR2T_Object(
    (1, 3, 6, 1, 3, 9999, 1, 6, 1, 1, 6),
    _IscsiNodeInitialR2T_Type()
)
iscsiNodeInitialR2T.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsiNodeInitialR2T.setStatus("current")


class _IscsiNodeBidiInitialR2T_Type(TruthValue):
    """Custom type iscsiNodeBidiInitialR2T based on TruthValue"""
    defaultValue = 1


_IscsiNodeBidiInitialR2T_Type.__name__ = "TruthValue"
_IscsiNodeBidiInitialR2T_Object = MibTableColumn
iscsiNodeBidiInitialR2T = _IscsiNodeBidiInitialR2T_Object(
    (1, 3, 6, 1, 3, 9999, 1, 6, 1, 1, 7),
    _IscsiNodeBidiInitialR2T_Type()
)
iscsiNodeBidiInitialR2T.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsiNodeBidiInitialR2T.setStatus("current")


class _IscsiNodeImmediateData_Type(TruthValue):
    """Custom type iscsiNodeImmediateData based on TruthValue"""
    defaultValue = 1


_IscsiNodeImmediateData_Type.__name__ = "TruthValue"
_IscsiNodeImmediateData_Object = MibTableColumn
iscsiNodeImmediateData = _IscsiNodeImmediateData_Object(
    (1, 3, 6, 1, 3, 9999, 1, 6, 1, 1, 8),
    _IscsiNodeImmediateData_Type()
)
iscsiNodeImmediateData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iscsiNodeImmediateData.setStatus("current")


class _IscsiNodeMaxOutstandingR2T_Type(Integer32):
    """Custom type iscsiNodeMaxOutstandingR2T based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_IscsiNodeMaxOutstandingR2T_Type.__name__ = "Integer32"
_IscsiNodeMaxOutstandingR2T_Object = MibTableColumn
iscsiNodeMaxOutstandingR2T = _IscsiNodeMaxOutstandingR2T_Object(
    (1, 3, 6, 1, 3, 9999, 1, 6, 1, 1, 9),
    _IscsiNodeMaxOutstandingR2T_Type()
)
iscsiNodeMaxOutstandingR2T.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iscsiNodeMaxOutstandingR2T.setStatus("current")


class _IscsiNodeFirstBurstSize_Type(Integer32):
    """Custom type iscsiNodeFirstBurstSize based on Integer32"""
    defaultValue = 65536

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(512, 16777215),
    )


_IscsiNodeFirstBurstSize_Type.__name__ = "Integer32"
_IscsiNodeFirstBurstSize_Object = MibTableColumn
iscsiNodeFirstBurstSize = _IscsiNodeFirstBurstSize_Object(
    (1, 3, 6, 1, 3, 9999, 1, 6, 1, 1, 10),
    _IscsiNodeFirstBurstSize_Type()
)
iscsiNodeFirstBurstSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iscsiNodeFirstBurstSize.setStatus("current")
if mibBuilder.loadTexts:
    iscsiNodeFirstBurstSize.setUnits("bytes")


class _IscsiNodeMaxBurstSize_Type(Integer32):
    """Custom type iscsiNodeMaxBurstSize based on Integer32"""
    defaultValue = 262144

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(512, 16777215),
    )


_IscsiNodeMaxBurstSize_Type.__name__ = "Integer32"
_IscsiNodeMaxBurstSize_Object = MibTableColumn
iscsiNodeMaxBurstSize = _IscsiNodeMaxBurstSize_Object(
    (1, 3, 6, 1, 3, 9999, 1, 6, 1, 1, 11),
    _IscsiNodeMaxBurstSize_Type()
)
iscsiNodeMaxBurstSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iscsiNodeMaxBurstSize.setStatus("current")
if mibBuilder.loadTexts:
    iscsiNodeMaxBurstSize.setUnits("bytes")


class _IscsiNodeMaxConnections_Type(Integer32):
    """Custom type iscsiNodeMaxConnections based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_IscsiNodeMaxConnections_Type.__name__ = "Integer32"
_IscsiNodeMaxConnections_Object = MibTableColumn
iscsiNodeMaxConnections = _IscsiNodeMaxConnections_Object(
    (1, 3, 6, 1, 3, 9999, 1, 6, 1, 1, 12),
    _IscsiNodeMaxConnections_Type()
)
iscsiNodeMaxConnections.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iscsiNodeMaxConnections.setStatus("current")
if mibBuilder.loadTexts:
    iscsiNodeMaxConnections.setUnits("connections")


class _IscsiNodeDataSequenceInOrder_Type(TruthValue):
    """Custom type iscsiNodeDataSequenceInOrder based on TruthValue"""
    defaultValue = 1


_IscsiNodeDataSequenceInOrder_Type.__name__ = "TruthValue"
_IscsiNodeDataSequenceInOrder_Object = MibTableColumn
iscsiNodeDataSequenceInOrder = _IscsiNodeDataSequenceInOrder_Object(
    (1, 3, 6, 1, 3, 9999, 1, 6, 1, 1, 13),
    _IscsiNodeDataSequenceInOrder_Type()
)
iscsiNodeDataSequenceInOrder.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iscsiNodeDataSequenceInOrder.setStatus("current")


class _IscsiNodeDataPduInOrder_Type(TruthValue):
    """Custom type iscsiNodeDataPduInOrder based on TruthValue"""
    defaultValue = 1


_IscsiNodeDataPduInOrder_Type.__name__ = "TruthValue"
_IscsiNodeDataPduInOrder_Object = MibTableColumn
iscsiNodeDataPduInOrder = _IscsiNodeDataPduInOrder_Object(
    (1, 3, 6, 1, 3, 9999, 1, 6, 1, 1, 14),
    _IscsiNodeDataPduInOrder_Type()
)
iscsiNodeDataPduInOrder.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iscsiNodeDataPduInOrder.setStatus("current")


class _IscsiNodeDefaultTime2Wait_Type(Integer32):
    """Custom type iscsiNodeDefaultTime2Wait based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_IscsiNodeDefaultTime2Wait_Type.__name__ = "Integer32"
_IscsiNodeDefaultTime2Wait_Object = MibTableColumn
iscsiNodeDefaultTime2Wait = _IscsiNodeDefaultTime2Wait_Object(
    (1, 3, 6, 1, 3, 9999, 1, 6, 1, 1, 15),
    _IscsiNodeDefaultTime2Wait_Type()
)
iscsiNodeDefaultTime2Wait.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iscsiNodeDefaultTime2Wait.setStatus("current")


class _IscsiNodeDefaultTime2Retain_Type(Integer32):
    """Custom type iscsiNodeDefaultTime2Retain based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_IscsiNodeDefaultTime2Retain_Type.__name__ = "Integer32"
_IscsiNodeDefaultTime2Retain_Object = MibTableColumn
iscsiNodeDefaultTime2Retain = _IscsiNodeDefaultTime2Retain_Object(
    (1, 3, 6, 1, 3, 9999, 1, 6, 1, 1, 16),
    _IscsiNodeDefaultTime2Retain_Type()
)
iscsiNodeDefaultTime2Retain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iscsiNodeDefaultTime2Retain.setStatus("current")


class _IscsiNodeErrorRecoveryLevel_Type(Integer32):
    """Custom type iscsiNodeErrorRecoveryLevel based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IscsiNodeErrorRecoveryLevel_Type.__name__ = "Integer32"
_IscsiNodeErrorRecoveryLevel_Object = MibTableColumn
iscsiNodeErrorRecoveryLevel = _IscsiNodeErrorRecoveryLevel_Object(
    (1, 3, 6, 1, 3, 9999, 1, 6, 1, 1, 17),
    _IscsiNodeErrorRecoveryLevel_Type()
)
iscsiNodeErrorRecoveryLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iscsiNodeErrorRecoveryLevel.setStatus("current")
_IscsiTarget_ObjectIdentity = ObjectIdentity
iscsiTarget = _IscsiTarget_ObjectIdentity(
    (1, 3, 6, 1, 3, 9999, 1, 7)
)
_IscsiTargetAttributesTable_Object = MibTable
iscsiTargetAttributesTable = _IscsiTargetAttributesTable_Object(
    (1, 3, 6, 1, 3, 9999, 1, 7, 1)
)
if mibBuilder.loadTexts:
    iscsiTargetAttributesTable.setStatus("current")
_IscsiTargetAttributesEntry_Object = MibTableRow
iscsiTargetAttributesEntry = _IscsiTargetAttributesEntry_Object(
    (1, 3, 6, 1, 3, 9999, 1, 7, 1, 1)
)
iscsiTargetAttributesEntry.setIndexNames(
    (0, "ISCSI-MIB", "iscsiInstIndex"),
    (0, "ISCSI-MIB", "iscsiNodeIndex"),
)
if mibBuilder.loadTexts:
    iscsiTargetAttributesEntry.setStatus("current")
_IscsiTgtLoginFailures_Type = Counter32
_IscsiTgtLoginFailures_Object = MibTableColumn
iscsiTgtLoginFailures = _IscsiTgtLoginFailures_Object(
    (1, 3, 6, 1, 3, 9999, 1, 7, 1, 1, 1),
    _IscsiTgtLoginFailures_Type()
)
iscsiTgtLoginFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsiTgtLoginFailures.setStatus("current")
if mibBuilder.loadTexts:
    iscsiTgtLoginFailures.setUnits("failed login attempts")
_IscsiTgtLastFailureTime_Type = TimeStamp
_IscsiTgtLastFailureTime_Object = MibTableColumn
iscsiTgtLastFailureTime = _IscsiTgtLastFailureTime_Object(
    (1, 3, 6, 1, 3, 9999, 1, 7, 1, 1, 2),
    _IscsiTgtLastFailureTime_Type()
)
iscsiTgtLastFailureTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsiTgtLastFailureTime.setStatus("current")
_IscsiTgtLastFailureType_Type = Integer32
_IscsiTgtLastFailureType_Object = MibTableColumn
iscsiTgtLastFailureType = _IscsiTgtLastFailureType_Object(
    (1, 3, 6, 1, 3, 9999, 1, 7, 1, 1, 3),
    _IscsiTgtLastFailureType_Type()
)
iscsiTgtLastFailureType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsiTgtLastFailureType.setStatus("current")
_IscsiTgtLastIntrFailureName_Type = SnmpAdminString
_IscsiTgtLastIntrFailureName_Object = MibTableColumn
iscsiTgtLastIntrFailureName = _IscsiTgtLastIntrFailureName_Object(
    (1, 3, 6, 1, 3, 9999, 1, 7, 1, 1, 4),
    _IscsiTgtLastIntrFailureName_Type()
)
iscsiTgtLastIntrFailureName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsiTgtLastIntrFailureName.setStatus("current")
_IscsiTgtLastIntrFailureAddrType_Type = InetAddressType
_IscsiTgtLastIntrFailureAddrType_Object = MibTableColumn
iscsiTgtLastIntrFailureAddrType = _IscsiTgtLastIntrFailureAddrType_Object(
    (1, 3, 6, 1, 3, 9999, 1, 7, 1, 1, 5),
    _IscsiTgtLastIntrFailureAddrType_Type()
)
iscsiTgtLastIntrFailureAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsiTgtLastIntrFailureAddrType.setStatus("current")
_IscsiTgtLastIntrFailureAddr_Type = InetAddress
_IscsiTgtLastIntrFailureAddr_Object = MibTableColumn
iscsiTgtLastIntrFailureAddr = _IscsiTgtLastIntrFailureAddr_Object(
    (1, 3, 6, 1, 3, 9999, 1, 7, 1, 1, 6),
    _IscsiTgtLastIntrFailureAddr_Type()
)
iscsiTgtLastIntrFailureAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsiTgtLastIntrFailureAddr.setStatus("current")
_IscsiTargetLoginStatsTable_Object = MibTable
iscsiTargetLoginStatsTable = _IscsiTargetLoginStatsTable_Object(
    (1, 3, 6, 1, 3, 9999, 1, 7, 2)
)
if mibBuilder.loadTexts:
    iscsiTargetLoginStatsTable.setStatus("current")
_IscsiTargetLoginStatsEntry_Object = MibTableRow
iscsiTargetLoginStatsEntry = _IscsiTargetLoginStatsEntry_Object(
    (1, 3, 6, 1, 3, 9999, 1, 7, 2, 1)
)
if mibBuilder.loadTexts:
    iscsiTargetLoginStatsEntry.setStatus("current")
_IscsiTgtLoginAccepts_Type = Counter32
_IscsiTgtLoginAccepts_Object = MibTableColumn
iscsiTgtLoginAccepts = _IscsiTgtLoginAccepts_Object(
    (1, 3, 6, 1, 3, 9999, 1, 7, 2, 1, 1),
    _IscsiTgtLoginAccepts_Type()
)
iscsiTgtLoginAccepts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsiTgtLoginAccepts.setStatus("current")
if mibBuilder.loadTexts:
    iscsiTgtLoginAccepts.setUnits("successful logins")
_IscsiTgtLoginOtherFails_Type = Counter32
_IscsiTgtLoginOtherFails_Object = MibTableColumn
iscsiTgtLoginOtherFails = _IscsiTgtLoginOtherFails_Object(
    (1, 3, 6, 1, 3, 9999, 1, 7, 2, 1, 2),
    _IscsiTgtLoginOtherFails_Type()
)
iscsiTgtLoginOtherFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsiTgtLoginOtherFails.setStatus("current")
if mibBuilder.loadTexts:
    iscsiTgtLoginOtherFails.setUnits("failed logins")
_IscsiTgtLoginRedirects_Type = Counter32
_IscsiTgtLoginRedirects_Object = MibTableColumn
iscsiTgtLoginRedirects = _IscsiTgtLoginRedirects_Object(
    (1, 3, 6, 1, 3, 9999, 1, 7, 2, 1, 3),
    _IscsiTgtLoginRedirects_Type()
)
iscsiTgtLoginRedirects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsiTgtLoginRedirects.setStatus("current")
if mibBuilder.loadTexts:
    iscsiTgtLoginRedirects.setUnits("failed logins")
_IscsiTgtLoginAuthorizeFails_Type = Counter32
_IscsiTgtLoginAuthorizeFails_Object = MibTableColumn
iscsiTgtLoginAuthorizeFails = _IscsiTgtLoginAuthorizeFails_Object(
    (1, 3, 6, 1, 3, 9999, 1, 7, 2, 1, 4),
    _IscsiTgtLoginAuthorizeFails_Type()
)
iscsiTgtLoginAuthorizeFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsiTgtLoginAuthorizeFails.setStatus("current")
if mibBuilder.loadTexts:
    iscsiTgtLoginAuthorizeFails.setUnits("failed logins")
_IscsiTgtLoginAuthenticateFails_Type = Counter32
_IscsiTgtLoginAuthenticateFails_Object = MibTableColumn
iscsiTgtLoginAuthenticateFails = _IscsiTgtLoginAuthenticateFails_Object(
    (1, 3, 6, 1, 3, 9999, 1, 7, 2, 1, 5),
    _IscsiTgtLoginAuthenticateFails_Type()
)
iscsiTgtLoginAuthenticateFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsiTgtLoginAuthenticateFails.setStatus("current")
if mibBuilder.loadTexts:
    iscsiTgtLoginAuthenticateFails.setUnits("failed logins")
_IscsiTgtLoginNegotiateFails_Type = Counter32
_IscsiTgtLoginNegotiateFails_Object = MibTableColumn
iscsiTgtLoginNegotiateFails = _IscsiTgtLoginNegotiateFails_Object(
    (1, 3, 6, 1, 3, 9999, 1, 7, 2, 1, 6),
    _IscsiTgtLoginNegotiateFails_Type()
)
iscsiTgtLoginNegotiateFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsiTgtLoginNegotiateFails.setStatus("current")
if mibBuilder.loadTexts:
    iscsiTgtLoginNegotiateFails.setUnits("failed logins")
_IscsiTargetLogoutStatsTable_Object = MibTable
iscsiTargetLogoutStatsTable = _IscsiTargetLogoutStatsTable_Object(
    (1, 3, 6, 1, 3, 9999, 1, 7, 3)
)
if mibBuilder.loadTexts:
    iscsiTargetLogoutStatsTable.setStatus("current")
_IscsiTargetLogoutStatsEntry_Object = MibTableRow
iscsiTargetLogoutStatsEntry = _IscsiTargetLogoutStatsEntry_Object(
    (1, 3, 6, 1, 3, 9999, 1, 7, 3, 1)
)
if mibBuilder.loadTexts:
    iscsiTargetLogoutStatsEntry.setStatus("current")
_IscsiTgtLogoutNormals_Type = Counter32
_IscsiTgtLogoutNormals_Object = MibTableColumn
iscsiTgtLogoutNormals = _IscsiTgtLogoutNormals_Object(
    (1, 3, 6, 1, 3, 9999, 1, 7, 3, 1, 1),
    _IscsiTgtLogoutNormals_Type()
)
iscsiTgtLogoutNormals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsiTgtLogoutNormals.setStatus("current")
if mibBuilder.loadTexts:
    iscsiTgtLogoutNormals.setUnits("normal logouts")
_IscsiTgtLogoutOthers_Type = Counter32
_IscsiTgtLogoutOthers_Object = MibTableColumn
iscsiTgtLogoutOthers = _IscsiTgtLogoutOthers_Object(
    (1, 3, 6, 1, 3, 9999, 1, 7, 3, 1, 2),
    _IscsiTgtLogoutOthers_Type()
)
iscsiTgtLogoutOthers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsiTgtLogoutOthers.setStatus("current")
if mibBuilder.loadTexts:
    iscsiTgtLogoutOthers.setUnits("abnormal logouts")
_IscsiTgtAuthorization_ObjectIdentity = ObjectIdentity
iscsiTgtAuthorization = _IscsiTgtAuthorization_ObjectIdentity(
    (1, 3, 6, 1, 3, 9999, 1, 8)
)
_IscsiTgtAuthAttributesTable_Object = MibTable
iscsiTgtAuthAttributesTable = _IscsiTgtAuthAttributesTable_Object(
    (1, 3, 6, 1, 3, 9999, 1, 8, 1)
)
if mibBuilder.loadTexts:
    iscsiTgtAuthAttributesTable.setStatus("current")
_IscsiTgtAuthAttributesEntry_Object = MibTableRow
iscsiTgtAuthAttributesEntry = _IscsiTgtAuthAttributesEntry_Object(
    (1, 3, 6, 1, 3, 9999, 1, 8, 1, 1)
)
iscsiTgtAuthAttributesEntry.setIndexNames(
    (0, "ISCSI-MIB", "iscsiInstIndex"),
    (0, "ISCSI-MIB", "iscsiNodeIndex"),
    (0, "ISCSI-MIB", "iscsiTgtAuthIndex"),
)
if mibBuilder.loadTexts:
    iscsiTgtAuthAttributesEntry.setStatus("current")


class _IscsiTgtAuthIndex_Type(Unsigned32):
    """Custom type iscsiTgtAuthIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_IscsiTgtAuthIndex_Type.__name__ = "Unsigned32"
_IscsiTgtAuthIndex_Object = MibTableColumn
iscsiTgtAuthIndex = _IscsiTgtAuthIndex_Object(
    (1, 3, 6, 1, 3, 9999, 1, 8, 1, 1, 1),
    _IscsiTgtAuthIndex_Type()
)
iscsiTgtAuthIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    iscsiTgtAuthIndex.setStatus("current")
_IscsiTgtAuthRowStatus_Type = RowStatus
_IscsiTgtAuthRowStatus_Object = MibTableColumn
iscsiTgtAuthRowStatus = _IscsiTgtAuthRowStatus_Object(
    (1, 3, 6, 1, 3, 9999, 1, 8, 1, 1, 2),
    _IscsiTgtAuthRowStatus_Type()
)
iscsiTgtAuthRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    iscsiTgtAuthRowStatus.setStatus("current")
_IscsiTgtAuthIdentity_Type = RowPointer
_IscsiTgtAuthIdentity_Object = MibTableColumn
iscsiTgtAuthIdentity = _IscsiTgtAuthIdentity_Object(
    (1, 3, 6, 1, 3, 9999, 1, 8, 1, 1, 3),
    _IscsiTgtAuthIdentity_Type()
)
iscsiTgtAuthIdentity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    iscsiTgtAuthIdentity.setStatus("current")
_IscsiInitiator_ObjectIdentity = ObjectIdentity
iscsiInitiator = _IscsiInitiator_ObjectIdentity(
    (1, 3, 6, 1, 3, 9999, 1, 9)
)
_IscsiInitiatorAttributesTable_Object = MibTable
iscsiInitiatorAttributesTable = _IscsiInitiatorAttributesTable_Object(
    (1, 3, 6, 1, 3, 9999, 1, 9, 1)
)
if mibBuilder.loadTexts:
    iscsiInitiatorAttributesTable.setStatus("current")
_IscsiInitiatorAttributesEntry_Object = MibTableRow
iscsiInitiatorAttributesEntry = _IscsiInitiatorAttributesEntry_Object(
    (1, 3, 6, 1, 3, 9999, 1, 9, 1, 1)
)
iscsiInitiatorAttributesEntry.setIndexNames(
    (0, "ISCSI-MIB", "iscsiInstIndex"),
    (0, "ISCSI-MIB", "iscsiNodeIndex"),
)
if mibBuilder.loadTexts:
    iscsiInitiatorAttributesEntry.setStatus("current")
_IscsiIntrLoginFailures_Type = Counter32
_IscsiIntrLoginFailures_Object = MibTableColumn
iscsiIntrLoginFailures = _IscsiIntrLoginFailures_Object(
    (1, 3, 6, 1, 3, 9999, 1, 9, 1, 1, 1),
    _IscsiIntrLoginFailures_Type()
)
iscsiIntrLoginFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsiIntrLoginFailures.setStatus("current")
if mibBuilder.loadTexts:
    iscsiIntrLoginFailures.setUnits("failed logins")
_IscsiIntrLastFailureTime_Type = TimeStamp
_IscsiIntrLastFailureTime_Object = MibTableColumn
iscsiIntrLastFailureTime = _IscsiIntrLastFailureTime_Object(
    (1, 3, 6, 1, 3, 9999, 1, 9, 1, 1, 2),
    _IscsiIntrLastFailureTime_Type()
)
iscsiIntrLastFailureTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsiIntrLastFailureTime.setStatus("current")
_IscsiIntrLastFailureType_Type = Integer32
_IscsiIntrLastFailureType_Object = MibTableColumn
iscsiIntrLastFailureType = _IscsiIntrLastFailureType_Object(
    (1, 3, 6, 1, 3, 9999, 1, 9, 1, 1, 3),
    _IscsiIntrLastFailureType_Type()
)
iscsiIntrLastFailureType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsiIntrLastFailureType.setStatus("current")
_IscsiIntrLastTgtFailureName_Type = SnmpAdminString
_IscsiIntrLastTgtFailureName_Object = MibTableColumn
iscsiIntrLastTgtFailureName = _IscsiIntrLastTgtFailureName_Object(
    (1, 3, 6, 1, 3, 9999, 1, 9, 1, 1, 4),
    _IscsiIntrLastTgtFailureName_Type()
)
iscsiIntrLastTgtFailureName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsiIntrLastTgtFailureName.setStatus("current")
_IscsiIntrLastTgtFailureAddrType_Type = InetAddressType
_IscsiIntrLastTgtFailureAddrType_Object = MibTableColumn
iscsiIntrLastTgtFailureAddrType = _IscsiIntrLastTgtFailureAddrType_Object(
    (1, 3, 6, 1, 3, 9999, 1, 9, 1, 1, 5),
    _IscsiIntrLastTgtFailureAddrType_Type()
)
iscsiIntrLastTgtFailureAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsiIntrLastTgtFailureAddrType.setStatus("current")
_IscsiIntrLastTgtFailureAddr_Type = InetAddress
_IscsiIntrLastTgtFailureAddr_Object = MibTableColumn
iscsiIntrLastTgtFailureAddr = _IscsiIntrLastTgtFailureAddr_Object(
    (1, 3, 6, 1, 3, 9999, 1, 9, 1, 1, 6),
    _IscsiIntrLastTgtFailureAddr_Type()
)
iscsiIntrLastTgtFailureAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsiIntrLastTgtFailureAddr.setStatus("current")
_IscsiInitiatorLoginStatsTable_Object = MibTable
iscsiInitiatorLoginStatsTable = _IscsiInitiatorLoginStatsTable_Object(
    (1, 3, 6, 1, 3, 9999, 1, 9, 2)
)
if mibBuilder.loadTexts:
    iscsiInitiatorLoginStatsTable.setStatus("current")
_IscsiInitiatorLoginStatsEntry_Object = MibTableRow
iscsiInitiatorLoginStatsEntry = _IscsiInitiatorLoginStatsEntry_Object(
    (1, 3, 6, 1, 3, 9999, 1, 9, 2, 1)
)
if mibBuilder.loadTexts:
    iscsiInitiatorLoginStatsEntry.setStatus("current")
_IscsiIntrLoginAcceptRsps_Type = Counter32
_IscsiIntrLoginAcceptRsps_Object = MibTableColumn
iscsiIntrLoginAcceptRsps = _IscsiIntrLoginAcceptRsps_Object(
    (1, 3, 6, 1, 3, 9999, 1, 9, 2, 1, 1),
    _IscsiIntrLoginAcceptRsps_Type()
)
iscsiIntrLoginAcceptRsps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsiIntrLoginAcceptRsps.setStatus("current")
if mibBuilder.loadTexts:
    iscsiIntrLoginAcceptRsps.setUnits("successful logins")
_IscsiIntrLoginOtherFailRsps_Type = Counter32
_IscsiIntrLoginOtherFailRsps_Object = MibTableColumn
iscsiIntrLoginOtherFailRsps = _IscsiIntrLoginOtherFailRsps_Object(
    (1, 3, 6, 1, 3, 9999, 1, 9, 2, 1, 2),
    _IscsiIntrLoginOtherFailRsps_Type()
)
iscsiIntrLoginOtherFailRsps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsiIntrLoginOtherFailRsps.setStatus("current")
if mibBuilder.loadTexts:
    iscsiIntrLoginOtherFailRsps.setUnits("failed logins")
_IscsiIntrLoginRedirectRsps_Type = Counter32
_IscsiIntrLoginRedirectRsps_Object = MibTableColumn
iscsiIntrLoginRedirectRsps = _IscsiIntrLoginRedirectRsps_Object(
    (1, 3, 6, 1, 3, 9999, 1, 9, 2, 1, 3),
    _IscsiIntrLoginRedirectRsps_Type()
)
iscsiIntrLoginRedirectRsps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsiIntrLoginRedirectRsps.setStatus("current")
if mibBuilder.loadTexts:
    iscsiIntrLoginRedirectRsps.setUnits("failed logins")
_IscsiIntrLoginAuthFailRsps_Type = Counter32
_IscsiIntrLoginAuthFailRsps_Object = MibTableColumn
iscsiIntrLoginAuthFailRsps = _IscsiIntrLoginAuthFailRsps_Object(
    (1, 3, 6, 1, 3, 9999, 1, 9, 2, 1, 4),
    _IscsiIntrLoginAuthFailRsps_Type()
)
iscsiIntrLoginAuthFailRsps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsiIntrLoginAuthFailRsps.setStatus("current")
if mibBuilder.loadTexts:
    iscsiIntrLoginAuthFailRsps.setUnits("failed logins")
_IscsiIntrLoginAuthenticateFails_Type = Counter32
_IscsiIntrLoginAuthenticateFails_Object = MibTableColumn
iscsiIntrLoginAuthenticateFails = _IscsiIntrLoginAuthenticateFails_Object(
    (1, 3, 6, 1, 3, 9999, 1, 9, 2, 1, 5),
    _IscsiIntrLoginAuthenticateFails_Type()
)
iscsiIntrLoginAuthenticateFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsiIntrLoginAuthenticateFails.setStatus("current")
if mibBuilder.loadTexts:
    iscsiIntrLoginAuthenticateFails.setUnits("failed logins")
_IscsiIntrLoginNegotiateFails_Type = Counter32
_IscsiIntrLoginNegotiateFails_Object = MibTableColumn
iscsiIntrLoginNegotiateFails = _IscsiIntrLoginNegotiateFails_Object(
    (1, 3, 6, 1, 3, 9999, 1, 9, 2, 1, 6),
    _IscsiIntrLoginNegotiateFails_Type()
)
iscsiIntrLoginNegotiateFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsiIntrLoginNegotiateFails.setStatus("current")
if mibBuilder.loadTexts:
    iscsiIntrLoginNegotiateFails.setUnits("failed logins")
_IscsiInitiatorLogoutStatsTable_Object = MibTable
iscsiInitiatorLogoutStatsTable = _IscsiInitiatorLogoutStatsTable_Object(
    (1, 3, 6, 1, 3, 9999, 1, 9, 3)
)
if mibBuilder.loadTexts:
    iscsiInitiatorLogoutStatsTable.setStatus("current")
_IscsiInitiatorLogoutStatsEntry_Object = MibTableRow
iscsiInitiatorLogoutStatsEntry = _IscsiInitiatorLogoutStatsEntry_Object(
    (1, 3, 6, 1, 3, 9999, 1, 9, 3, 1)
)
if mibBuilder.loadTexts:
    iscsiInitiatorLogoutStatsEntry.setStatus("current")
_IscsiIntrLogoutNormals_Type = Counter32
_IscsiIntrLogoutNormals_Object = MibTableColumn
iscsiIntrLogoutNormals = _IscsiIntrLogoutNormals_Object(
    (1, 3, 6, 1, 3, 9999, 1, 9, 3, 1, 1),
    _IscsiIntrLogoutNormals_Type()
)
iscsiIntrLogoutNormals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsiIntrLogoutNormals.setStatus("current")
if mibBuilder.loadTexts:
    iscsiIntrLogoutNormals.setUnits("normal logouts")
_IscsiIntrLogoutOthers_Type = Counter32
_IscsiIntrLogoutOthers_Object = MibTableColumn
iscsiIntrLogoutOthers = _IscsiIntrLogoutOthers_Object(
    (1, 3, 6, 1, 3, 9999, 1, 9, 3, 1, 2),
    _IscsiIntrLogoutOthers_Type()
)
iscsiIntrLogoutOthers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsiIntrLogoutOthers.setStatus("current")
if mibBuilder.loadTexts:
    iscsiIntrLogoutOthers.setUnits("abnormal logouts")
_IscsiIntrAuthorization_ObjectIdentity = ObjectIdentity
iscsiIntrAuthorization = _IscsiIntrAuthorization_ObjectIdentity(
    (1, 3, 6, 1, 3, 9999, 1, 10)
)
_IscsiIntrAuthAttributesTable_Object = MibTable
iscsiIntrAuthAttributesTable = _IscsiIntrAuthAttributesTable_Object(
    (1, 3, 6, 1, 3, 9999, 1, 10, 1)
)
if mibBuilder.loadTexts:
    iscsiIntrAuthAttributesTable.setStatus("current")
_IscsiIntrAuthAttributesEntry_Object = MibTableRow
iscsiIntrAuthAttributesEntry = _IscsiIntrAuthAttributesEntry_Object(
    (1, 3, 6, 1, 3, 9999, 1, 10, 1, 1)
)
iscsiIntrAuthAttributesEntry.setIndexNames(
    (0, "ISCSI-MIB", "iscsiInstIndex"),
    (0, "ISCSI-MIB", "iscsiNodeIndex"),
    (0, "ISCSI-MIB", "iscsiIntrAuthIndex"),
)
if mibBuilder.loadTexts:
    iscsiIntrAuthAttributesEntry.setStatus("current")


class _IscsiIntrAuthIndex_Type(Unsigned32):
    """Custom type iscsiIntrAuthIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_IscsiIntrAuthIndex_Type.__name__ = "Unsigned32"
_IscsiIntrAuthIndex_Object = MibTableColumn
iscsiIntrAuthIndex = _IscsiIntrAuthIndex_Object(
    (1, 3, 6, 1, 3, 9999, 1, 10, 1, 1, 1),
    _IscsiIntrAuthIndex_Type()
)
iscsiIntrAuthIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    iscsiIntrAuthIndex.setStatus("current")
_IscsiIntrAuthRowStatus_Type = RowStatus
_IscsiIntrAuthRowStatus_Object = MibTableColumn
iscsiIntrAuthRowStatus = _IscsiIntrAuthRowStatus_Object(
    (1, 3, 6, 1, 3, 9999, 1, 10, 1, 1, 2),
    _IscsiIntrAuthRowStatus_Type()
)
iscsiIntrAuthRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsiIntrAuthRowStatus.setStatus("current")
_IscsiIntrAuthIdentity_Type = RowPointer
_IscsiIntrAuthIdentity_Object = MibTableColumn
iscsiIntrAuthIdentity = _IscsiIntrAuthIdentity_Object(
    (1, 3, 6, 1, 3, 9999, 1, 10, 1, 1, 3),
    _IscsiIntrAuthIdentity_Type()
)
iscsiIntrAuthIdentity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsiIntrAuthIdentity.setStatus("current")
_IscsiSession_ObjectIdentity = ObjectIdentity
iscsiSession = _IscsiSession_ObjectIdentity(
    (1, 3, 6, 1, 3, 9999, 1, 11)
)
_IscsiSessionAttributesTable_Object = MibTable
iscsiSessionAttributesTable = _IscsiSessionAttributesTable_Object(
    (1, 3, 6, 1, 3, 9999, 1, 11, 1)
)
if mibBuilder.loadTexts:
    iscsiSessionAttributesTable.setStatus("current")
_IscsiSessionAttributesEntry_Object = MibTableRow
iscsiSessionAttributesEntry = _IscsiSessionAttributesEntry_Object(
    (1, 3, 6, 1, 3, 9999, 1, 11, 1, 1)
)
iscsiSessionAttributesEntry.setIndexNames(
    (0, "ISCSI-MIB", "iscsiInstIndex"),
    (0, "ISCSI-MIB", "iscsiNodeIndex"),
    (0, "ISCSI-MIB", "iscsiSsnIndex"),
)
if mibBuilder.loadTexts:
    iscsiSessionAttributesEntry.setStatus("current")


class _IscsiSsnIndex_Type(Unsigned32):
    """Custom type iscsiSsnIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_IscsiSsnIndex_Type.__name__ = "Unsigned32"
_IscsiSsnIndex_Object = MibTableColumn
iscsiSsnIndex = _IscsiSsnIndex_Object(
    (1, 3, 6, 1, 3, 9999, 1, 11, 1, 1, 1),
    _IscsiSsnIndex_Type()
)
iscsiSsnIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    iscsiSsnIndex.setStatus("current")


class _IscsiSsnDirection_Type(Integer32):
    """Custom type iscsiSsnDirection based on Integer32"""
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


_IscsiSsnDirection_Type.__name__ = "Integer32"
_IscsiSsnDirection_Object = MibTableColumn
iscsiSsnDirection = _IscsiSsnDirection_Object(
    (1, 3, 6, 1, 3, 9999, 1, 11, 1, 1, 2),
    _IscsiSsnDirection_Type()
)
iscsiSsnDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsiSsnDirection.setStatus("current")
_IscsiSsnInitiatorName_Type = SnmpAdminString
_IscsiSsnInitiatorName_Object = MibTableColumn
iscsiSsnInitiatorName = _IscsiSsnInitiatorName_Object(
    (1, 3, 6, 1, 3, 9999, 1, 11, 1, 1, 3),
    _IscsiSsnInitiatorName_Type()
)
iscsiSsnInitiatorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsiSsnInitiatorName.setStatus("current")
_IscsiSsnTargetName_Type = SnmpAdminString
_IscsiSsnTargetName_Object = MibTableColumn
iscsiSsnTargetName = _IscsiSsnTargetName_Object(
    (1, 3, 6, 1, 3, 9999, 1, 11, 1, 1, 4),
    _IscsiSsnTargetName_Type()
)
iscsiSsnTargetName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsiSsnTargetName.setStatus("current")


class _IscsiSsnTsih_Type(Integer32):
    """Custom type iscsiSsnTsih based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_IscsiSsnTsih_Type.__name__ = "Integer32"
_IscsiSsnTsih_Object = MibTableColumn
iscsiSsnTsih = _IscsiSsnTsih_Object(
    (1, 3, 6, 1, 3, 9999, 1, 11, 1, 1, 5),
    _IscsiSsnTsih_Type()
)
iscsiSsnTsih.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsiSsnTsih.setStatus("current")


class _IscsiSsnIsid_Type(OctetString):
    """Custom type iscsiSsnIsid based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )
    fixed_length = 6


_IscsiSsnIsid_Type.__name__ = "OctetString"
_IscsiSsnIsid_Object = MibTableColumn
iscsiSsnIsid = _IscsiSsnIsid_Object(
    (1, 3, 6, 1, 3, 9999, 1, 11, 1, 1, 6),
    _IscsiSsnIsid_Type()
)
iscsiSsnIsid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsiSsnIsid.setStatus("current")
_IscsiSsnInitiatorAlias_Type = SnmpAdminString
_IscsiSsnInitiatorAlias_Object = MibTableColumn
iscsiSsnInitiatorAlias = _IscsiSsnInitiatorAlias_Object(
    (1, 3, 6, 1, 3, 9999, 1, 11, 1, 1, 7),
    _IscsiSsnInitiatorAlias_Type()
)
iscsiSsnInitiatorAlias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsiSsnInitiatorAlias.setStatus("current")
_IscsiSsnTargetAlias_Type = SnmpAdminString
_IscsiSsnTargetAlias_Object = MibTableColumn
iscsiSsnTargetAlias = _IscsiSsnTargetAlias_Object(
    (1, 3, 6, 1, 3, 9999, 1, 11, 1, 1, 8),
    _IscsiSsnTargetAlias_Type()
)
iscsiSsnTargetAlias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsiSsnTargetAlias.setStatus("current")
_IscsiSsnInitialR2T_Type = TruthValue
_IscsiSsnInitialR2T_Object = MibTableColumn
iscsiSsnInitialR2T = _IscsiSsnInitialR2T_Object(
    (1, 3, 6, 1, 3, 9999, 1, 11, 1, 1, 9),
    _IscsiSsnInitialR2T_Type()
)
iscsiSsnInitialR2T.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsiSsnInitialR2T.setStatus("current")
_IscsiSsnBidiInitialR2T_Type = TruthValue
_IscsiSsnBidiInitialR2T_Object = MibTableColumn
iscsiSsnBidiInitialR2T = _IscsiSsnBidiInitialR2T_Object(
    (1, 3, 6, 1, 3, 9999, 1, 11, 1, 1, 10),
    _IscsiSsnBidiInitialR2T_Type()
)
iscsiSsnBidiInitialR2T.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsiSsnBidiInitialR2T.setStatus("current")
_IscsiSsnImmediateData_Type = TruthValue
_IscsiSsnImmediateData_Object = MibTableColumn
iscsiSsnImmediateData = _IscsiSsnImmediateData_Object(
    (1, 3, 6, 1, 3, 9999, 1, 11, 1, 1, 11),
    _IscsiSsnImmediateData_Type()
)
iscsiSsnImmediateData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsiSsnImmediateData.setStatus("current")


class _IscsiSsnType_Type(Integer32):
    """Custom type iscsiSsnType based on Integer32"""
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


_IscsiSsnType_Type.__name__ = "Integer32"
_IscsiSsnType_Object = MibTableColumn
iscsiSsnType = _IscsiSsnType_Object(
    (1, 3, 6, 1, 3, 9999, 1, 11, 1, 1, 12),
    _IscsiSsnType_Type()
)
iscsiSsnType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsiSsnType.setStatus("current")


class _IscsiSsnMaxOutstandingR2T_Type(Integer32):
    """Custom type iscsiSsnMaxOutstandingR2T based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_IscsiSsnMaxOutstandingR2T_Type.__name__ = "Integer32"
_IscsiSsnMaxOutstandingR2T_Object = MibTableColumn
iscsiSsnMaxOutstandingR2T = _IscsiSsnMaxOutstandingR2T_Object(
    (1, 3, 6, 1, 3, 9999, 1, 11, 1, 1, 13),
    _IscsiSsnMaxOutstandingR2T_Type()
)
iscsiSsnMaxOutstandingR2T.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsiSsnMaxOutstandingR2T.setStatus("current")


class _IscsiSsnFirstBurstSize_Type(Integer32):
    """Custom type iscsiSsnFirstBurstSize based on Integer32"""
    defaultValue = 65536

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(512, 16777215),
    )


_IscsiSsnFirstBurstSize_Type.__name__ = "Integer32"
_IscsiSsnFirstBurstSize_Object = MibTableColumn
iscsiSsnFirstBurstSize = _IscsiSsnFirstBurstSize_Object(
    (1, 3, 6, 1, 3, 9999, 1, 11, 1, 1, 14),
    _IscsiSsnFirstBurstSize_Type()
)
iscsiSsnFirstBurstSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsiSsnFirstBurstSize.setStatus("current")
if mibBuilder.loadTexts:
    iscsiSsnFirstBurstSize.setUnits("bytes")


class _IscsiSsnMaxBurstSize_Type(Integer32):
    """Custom type iscsiSsnMaxBurstSize based on Integer32"""
    defaultValue = 262144

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(512, 16777215),
    )


_IscsiSsnMaxBurstSize_Type.__name__ = "Integer32"
_IscsiSsnMaxBurstSize_Object = MibTableColumn
iscsiSsnMaxBurstSize = _IscsiSsnMaxBurstSize_Object(
    (1, 3, 6, 1, 3, 9999, 1, 11, 1, 1, 15),
    _IscsiSsnMaxBurstSize_Type()
)
iscsiSsnMaxBurstSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsiSsnMaxBurstSize.setStatus("current")
if mibBuilder.loadTexts:
    iscsiSsnMaxBurstSize.setUnits("bytes")


class _IscsiSsnConnectionNumber_Type(Gauge32):
    """Custom type iscsiSsnConnectionNumber based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_IscsiSsnConnectionNumber_Type.__name__ = "Gauge32"
_IscsiSsnConnectionNumber_Object = MibTableColumn
iscsiSsnConnectionNumber = _IscsiSsnConnectionNumber_Object(
    (1, 3, 6, 1, 3, 9999, 1, 11, 1, 1, 16),
    _IscsiSsnConnectionNumber_Type()
)
iscsiSsnConnectionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsiSsnConnectionNumber.setStatus("current")
if mibBuilder.loadTexts:
    iscsiSsnConnectionNumber.setUnits("connections")
_IscsiSsnAuthIdentity_Type = RowPointer
_IscsiSsnAuthIdentity_Object = MibTableColumn
iscsiSsnAuthIdentity = _IscsiSsnAuthIdentity_Object(
    (1, 3, 6, 1, 3, 9999, 1, 11, 1, 1, 17),
    _IscsiSsnAuthIdentity_Type()
)
iscsiSsnAuthIdentity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsiSsnAuthIdentity.setStatus("current")
_IscsiSsnDataSequenceInOrder_Type = TruthValue
_IscsiSsnDataSequenceInOrder_Object = MibTableColumn
iscsiSsnDataSequenceInOrder = _IscsiSsnDataSequenceInOrder_Object(
    (1, 3, 6, 1, 3, 9999, 1, 11, 1, 1, 18),
    _IscsiSsnDataSequenceInOrder_Type()
)
iscsiSsnDataSequenceInOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsiSsnDataSequenceInOrder.setStatus("current")
_IscsiSsnDataPduInOrder_Type = TruthValue
_IscsiSsnDataPduInOrder_Object = MibTableColumn
iscsiSsnDataPduInOrder = _IscsiSsnDataPduInOrder_Object(
    (1, 3, 6, 1, 3, 9999, 1, 11, 1, 1, 19),
    _IscsiSsnDataPduInOrder_Type()
)
iscsiSsnDataPduInOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsiSsnDataPduInOrder.setStatus("current")


class _IscsiSsnErrorRecoveryLevel_Type(Integer32):
    """Custom type iscsiSsnErrorRecoveryLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IscsiSsnErrorRecoveryLevel_Type.__name__ = "Integer32"
_IscsiSsnErrorRecoveryLevel_Object = MibTableColumn
iscsiSsnErrorRecoveryLevel = _IscsiSsnErrorRecoveryLevel_Object(
    (1, 3, 6, 1, 3, 9999, 1, 11, 1, 1, 20),
    _IscsiSsnErrorRecoveryLevel_Type()
)
iscsiSsnErrorRecoveryLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsiSsnErrorRecoveryLevel.setStatus("current")
_IscsiSessionStatsTable_Object = MibTable
iscsiSessionStatsTable = _IscsiSessionStatsTable_Object(
    (1, 3, 6, 1, 3, 9999, 1, 11, 2)
)
if mibBuilder.loadTexts:
    iscsiSessionStatsTable.setStatus("current")
_IscsiSessionStatsEntry_Object = MibTableRow
iscsiSessionStatsEntry = _IscsiSessionStatsEntry_Object(
    (1, 3, 6, 1, 3, 9999, 1, 11, 2, 1)
)
if mibBuilder.loadTexts:
    iscsiSessionStatsEntry.setStatus("current")
_IscsiSsnCmdPdus_Type = Counter32
_IscsiSsnCmdPdus_Object = MibTableColumn
iscsiSsnCmdPdus = _IscsiSsnCmdPdus_Object(
    (1, 3, 6, 1, 3, 9999, 1, 11, 2, 1, 1),
    _IscsiSsnCmdPdus_Type()
)
iscsiSsnCmdPdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsiSsnCmdPdus.setStatus("current")
if mibBuilder.loadTexts:
    iscsiSsnCmdPdus.setUnits("PDUs")
_IscsiSsnRspPdus_Type = Counter32
_IscsiSsnRspPdus_Object = MibTableColumn
iscsiSsnRspPdus = _IscsiSsnRspPdus_Object(
    (1, 3, 6, 1, 3, 9999, 1, 11, 2, 1, 2),
    _IscsiSsnRspPdus_Type()
)
iscsiSsnRspPdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsiSsnRspPdus.setStatus("current")
if mibBuilder.loadTexts:
    iscsiSsnRspPdus.setUnits("PDUs")
_IscsiSsnTxDataOctets_Type = Counter64
_IscsiSsnTxDataOctets_Object = MibTableColumn
iscsiSsnTxDataOctets = _IscsiSsnTxDataOctets_Object(
    (1, 3, 6, 1, 3, 9999, 1, 11, 2, 1, 3),
    _IscsiSsnTxDataOctets_Type()
)
iscsiSsnTxDataOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsiSsnTxDataOctets.setStatus("current")
if mibBuilder.loadTexts:
    iscsiSsnTxDataOctets.setUnits("octets")
_IscsiSsnRxDataOctets_Type = Counter64
_IscsiSsnRxDataOctets_Object = MibTableColumn
iscsiSsnRxDataOctets = _IscsiSsnRxDataOctets_Object(
    (1, 3, 6, 1, 3, 9999, 1, 11, 2, 1, 4),
    _IscsiSsnRxDataOctets_Type()
)
iscsiSsnRxDataOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsiSsnRxDataOctets.setStatus("current")
if mibBuilder.loadTexts:
    iscsiSsnRxDataOctets.setUnits("octets")
_IscsiSessionCxnErrorStatsTable_Object = MibTable
iscsiSessionCxnErrorStatsTable = _IscsiSessionCxnErrorStatsTable_Object(
    (1, 3, 6, 1, 3, 9999, 1, 11, 3)
)
if mibBuilder.loadTexts:
    iscsiSessionCxnErrorStatsTable.setStatus("current")
_IscsiSessionCxnErrorStatsEntry_Object = MibTableRow
iscsiSessionCxnErrorStatsEntry = _IscsiSessionCxnErrorStatsEntry_Object(
    (1, 3, 6, 1, 3, 9999, 1, 11, 3, 1)
)
if mibBuilder.loadTexts:
    iscsiSessionCxnErrorStatsEntry.setStatus("current")
_IscsiSsnDigestErrors_Type = Counter32
_IscsiSsnDigestErrors_Object = MibTableColumn
iscsiSsnDigestErrors = _IscsiSsnDigestErrors_Object(
    (1, 3, 6, 1, 3, 9999, 1, 11, 3, 1, 1),
    _IscsiSsnDigestErrors_Type()
)
iscsiSsnDigestErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsiSsnDigestErrors.setStatus("current")
if mibBuilder.loadTexts:
    iscsiSsnDigestErrors.setUnits("PDUs")
_IscsiSsnCxnTimeoutErrors_Type = Counter32
_IscsiSsnCxnTimeoutErrors_Object = MibTableColumn
iscsiSsnCxnTimeoutErrors = _IscsiSsnCxnTimeoutErrors_Object(
    (1, 3, 6, 1, 3, 9999, 1, 11, 3, 1, 2),
    _IscsiSsnCxnTimeoutErrors_Type()
)
iscsiSsnCxnTimeoutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsiSsnCxnTimeoutErrors.setStatus("current")
if mibBuilder.loadTexts:
    iscsiSsnCxnTimeoutErrors.setUnits("sequences")
_IscsiConnection_ObjectIdentity = ObjectIdentity
iscsiConnection = _IscsiConnection_ObjectIdentity(
    (1, 3, 6, 1, 3, 9999, 1, 12)
)
_IscsiConnectionAttributesTable_Object = MibTable
iscsiConnectionAttributesTable = _IscsiConnectionAttributesTable_Object(
    (1, 3, 6, 1, 3, 9999, 1, 12, 1)
)
if mibBuilder.loadTexts:
    iscsiConnectionAttributesTable.setStatus("current")
_IscsiConnectionAttributesEntry_Object = MibTableRow
iscsiConnectionAttributesEntry = _IscsiConnectionAttributesEntry_Object(
    (1, 3, 6, 1, 3, 9999, 1, 12, 1, 1)
)
iscsiConnectionAttributesEntry.setIndexNames(
    (0, "ISCSI-MIB", "iscsiInstIndex"),
    (0, "ISCSI-MIB", "iscsiNodeIndex"),
    (0, "ISCSI-MIB", "iscsiSsnIndex"),
    (0, "ISCSI-MIB", "iscsiCxnIndex"),
)
if mibBuilder.loadTexts:
    iscsiConnectionAttributesEntry.setStatus("current")


class _IscsiCxnIndex_Type(Unsigned32):
    """Custom type iscsiCxnIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_IscsiCxnIndex_Type.__name__ = "Unsigned32"
_IscsiCxnIndex_Object = MibTableColumn
iscsiCxnIndex = _IscsiCxnIndex_Object(
    (1, 3, 6, 1, 3, 9999, 1, 12, 1, 1, 1),
    _IscsiCxnIndex_Type()
)
iscsiCxnIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    iscsiCxnIndex.setStatus("current")


class _IscsiCxnCid_Type(Integer32):
    """Custom type iscsiCxnCid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_IscsiCxnCid_Type.__name__ = "Integer32"
_IscsiCxnCid_Object = MibTableColumn
iscsiCxnCid = _IscsiCxnCid_Object(
    (1, 3, 6, 1, 3, 9999, 1, 12, 1, 1, 2),
    _IscsiCxnCid_Type()
)
iscsiCxnCid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsiCxnCid.setStatus("current")


class _IscsiCxnState_Type(Integer32):
    """Custom type iscsiCxnState based on Integer32"""
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


_IscsiCxnState_Type.__name__ = "Integer32"
_IscsiCxnState_Object = MibTableColumn
iscsiCxnState = _IscsiCxnState_Object(
    (1, 3, 6, 1, 3, 9999, 1, 12, 1, 1, 3),
    _IscsiCxnState_Type()
)
iscsiCxnState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsiCxnState.setStatus("current")
_IscsiCxnLocalAddrType_Type = InetAddressType
_IscsiCxnLocalAddrType_Object = MibTableColumn
iscsiCxnLocalAddrType = _IscsiCxnLocalAddrType_Object(
    (1, 3, 6, 1, 3, 9999, 1, 12, 1, 1, 4),
    _IscsiCxnLocalAddrType_Type()
)
iscsiCxnLocalAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsiCxnLocalAddrType.setStatus("current")
_IscsiCxnLocalAddr_Type = InetAddress
_IscsiCxnLocalAddr_Object = MibTableColumn
iscsiCxnLocalAddr = _IscsiCxnLocalAddr_Object(
    (1, 3, 6, 1, 3, 9999, 1, 12, 1, 1, 5),
    _IscsiCxnLocalAddr_Type()
)
iscsiCxnLocalAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsiCxnLocalAddr.setStatus("current")


class _IscsiCxnProtocol_Type(IscsiTransportProtocols):
    """Custom type iscsiCxnProtocol based on IscsiTransportProtocols"""
    defaultValue = 6


_IscsiCxnProtocol_Type.__name__ = "IscsiTransportProtocols"
_IscsiCxnProtocol_Object = MibTableColumn
iscsiCxnProtocol = _IscsiCxnProtocol_Object(
    (1, 3, 6, 1, 3, 9999, 1, 12, 1, 1, 6),
    _IscsiCxnProtocol_Type()
)
iscsiCxnProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsiCxnProtocol.setStatus("current")
_IscsiCxnLocalPort_Type = Unsigned32
_IscsiCxnLocalPort_Object = MibTableColumn
iscsiCxnLocalPort = _IscsiCxnLocalPort_Object(
    (1, 3, 6, 1, 3, 9999, 1, 12, 1, 1, 7),
    _IscsiCxnLocalPort_Type()
)
iscsiCxnLocalPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsiCxnLocalPort.setStatus("current")
_IscsiCxnRemoteAddrType_Type = InetAddressType
_IscsiCxnRemoteAddrType_Object = MibTableColumn
iscsiCxnRemoteAddrType = _IscsiCxnRemoteAddrType_Object(
    (1, 3, 6, 1, 3, 9999, 1, 12, 1, 1, 8),
    _IscsiCxnRemoteAddrType_Type()
)
iscsiCxnRemoteAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsiCxnRemoteAddrType.setStatus("current")
_IscsiCxnRemoteAddr_Type = InetAddress
_IscsiCxnRemoteAddr_Object = MibTableColumn
iscsiCxnRemoteAddr = _IscsiCxnRemoteAddr_Object(
    (1, 3, 6, 1, 3, 9999, 1, 12, 1, 1, 9),
    _IscsiCxnRemoteAddr_Type()
)
iscsiCxnRemoteAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsiCxnRemoteAddr.setStatus("current")
_IscsiCxnRemotePort_Type = Unsigned32
_IscsiCxnRemotePort_Object = MibTableColumn
iscsiCxnRemotePort = _IscsiCxnRemotePort_Object(
    (1, 3, 6, 1, 3, 9999, 1, 12, 1, 1, 10),
    _IscsiCxnRemotePort_Type()
)
iscsiCxnRemotePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsiCxnRemotePort.setStatus("current")


class _IscsiCxnMaxRecvDataSegLength_Type(Integer32):
    """Custom type iscsiCxnMaxRecvDataSegLength based on Integer32"""
    defaultValue = 8192

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(512, 16777215),
    )


_IscsiCxnMaxRecvDataSegLength_Type.__name__ = "Integer32"
_IscsiCxnMaxRecvDataSegLength_Object = MibTableColumn
iscsiCxnMaxRecvDataSegLength = _IscsiCxnMaxRecvDataSegLength_Object(
    (1, 3, 6, 1, 3, 9999, 1, 12, 1, 1, 11),
    _IscsiCxnMaxRecvDataSegLength_Type()
)
iscsiCxnMaxRecvDataSegLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsiCxnMaxRecvDataSegLength.setStatus("current")
if mibBuilder.loadTexts:
    iscsiCxnMaxRecvDataSegLength.setUnits("bytes")
_IscsiCxnHeaderIntegrity_Type = IscsiDigestMethod
_IscsiCxnHeaderIntegrity_Object = MibTableColumn
iscsiCxnHeaderIntegrity = _IscsiCxnHeaderIntegrity_Object(
    (1, 3, 6, 1, 3, 9999, 1, 12, 1, 1, 12),
    _IscsiCxnHeaderIntegrity_Type()
)
iscsiCxnHeaderIntegrity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsiCxnHeaderIntegrity.setStatus("current")
_IscsiCxnDataIntegrity_Type = IscsiDigestMethod
_IscsiCxnDataIntegrity_Object = MibTableColumn
iscsiCxnDataIntegrity = _IscsiCxnDataIntegrity_Object(
    (1, 3, 6, 1, 3, 9999, 1, 12, 1, 1, 13),
    _IscsiCxnDataIntegrity_Type()
)
iscsiCxnDataIntegrity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsiCxnDataIntegrity.setStatus("current")
_IscsiCxnRecvMarker_Type = TruthValue
_IscsiCxnRecvMarker_Object = MibTableColumn
iscsiCxnRecvMarker = _IscsiCxnRecvMarker_Object(
    (1, 3, 6, 1, 3, 9999, 1, 12, 1, 1, 14),
    _IscsiCxnRecvMarker_Type()
)
iscsiCxnRecvMarker.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsiCxnRecvMarker.setStatus("current")
_IscsiCxnSendMarker_Type = TruthValue
_IscsiCxnSendMarker_Object = MibTableColumn
iscsiCxnSendMarker = _IscsiCxnSendMarker_Object(
    (1, 3, 6, 1, 3, 9999, 1, 12, 1, 1, 15),
    _IscsiCxnSendMarker_Type()
)
iscsiCxnSendMarker.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsiCxnSendMarker.setStatus("current")
_IscsiNotifications_ObjectIdentity = ObjectIdentity
iscsiNotifications = _IscsiNotifications_ObjectIdentity(
    (1, 3, 6, 1, 3, 9999, 2)
)
_IscsiNotificationsPrefix_ObjectIdentity = ObjectIdentity
iscsiNotificationsPrefix = _IscsiNotificationsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 3, 9999, 2, 0)
)
_IscsiConformance_ObjectIdentity = ObjectIdentity
iscsiConformance = _IscsiConformance_ObjectIdentity(
    (1, 3, 6, 1, 3, 9999, 3)
)
_IscsiGroups_ObjectIdentity = ObjectIdentity
iscsiGroups = _IscsiGroups_ObjectIdentity(
    (1, 3, 6, 1, 3, 9999, 3, 1)
)
_IscsiCompliances_ObjectIdentity = ObjectIdentity
iscsiCompliances = _IscsiCompliances_ObjectIdentity(
    (1, 3, 6, 1, 3, 9999, 3, 2)
)
iscsiInstanceAttributesEntry.registerAugmentions(
    ("ISCSI-MIB",
     "iscsiInstanceSsnErrorStatsEntry")
)
iscsiInstanceSsnErrorStatsEntry.setIndexNames(*iscsiInstanceAttributesEntry.getIndexNames())
iscsiTargetAttributesEntry.registerAugmentions(
    ("ISCSI-MIB",
     "iscsiTargetLoginStatsEntry")
)
iscsiTargetLoginStatsEntry.setIndexNames(*iscsiTargetAttributesEntry.getIndexNames())
iscsiTargetAttributesEntry.registerAugmentions(
    ("ISCSI-MIB",
     "iscsiTargetLogoutStatsEntry")
)
iscsiTargetLogoutStatsEntry.setIndexNames(*iscsiTargetAttributesEntry.getIndexNames())
iscsiInitiatorAttributesEntry.registerAugmentions(
    ("ISCSI-MIB",
     "iscsiInitiatorLoginStatsEntry")
)
iscsiInitiatorLoginStatsEntry.setIndexNames(*iscsiInitiatorAttributesEntry.getIndexNames())
iscsiInitiatorAttributesEntry.registerAugmentions(
    ("ISCSI-MIB",
     "iscsiInitiatorLogoutStatsEntry")
)
iscsiInitiatorLogoutStatsEntry.setIndexNames(*iscsiInitiatorAttributesEntry.getIndexNames())
iscsiSessionAttributesEntry.registerAugmentions(
    ("ISCSI-MIB",
     "iscsiSessionStatsEntry")
)
iscsiSessionStatsEntry.setIndexNames(*iscsiSessionAttributesEntry.getIndexNames())
iscsiSessionAttributesEntry.registerAugmentions(
    ("ISCSI-MIB",
     "iscsiSessionCxnErrorStatsEntry")
)
iscsiSessionCxnErrorStatsEntry.setIndexNames(*iscsiSessionAttributesEntry.getIndexNames())

# Managed Objects groups

iscsiInstanceAttributesGroup = ObjectGroup(
    (1, 3, 6, 1, 3, 9999, 3, 1, 1)
)
iscsiInstanceAttributesGroup.setObjects(
      *(("ISCSI-MIB", "iscsiInstDescr"),
        ("ISCSI-MIB", "iscsiInstVersionMin"),
        ("ISCSI-MIB", "iscsiInstVersionMax"),
        ("ISCSI-MIB", "iscsiInstVendorID"),
        ("ISCSI-MIB", "iscsiInstVendorVersion"),
        ("ISCSI-MIB", "iscsiInstPortalNumber"),
        ("ISCSI-MIB", "iscsiInstNodeNumber"),
        ("ISCSI-MIB", "iscsiInstSessionNumber"),
        ("ISCSI-MIB", "iscsiInstSsnFailures"),
        ("ISCSI-MIB", "iscsiInstLastSsnFailureType"),
        ("ISCSI-MIB", "iscsiInstLastSsnRmtNodeName"))
)
if mibBuilder.loadTexts:
    iscsiInstanceAttributesGroup.setStatus("current")

iscsiInstanceSsnErrorStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 3, 9999, 3, 1, 2)
)
iscsiInstanceSsnErrorStatsGroup.setObjects(
      *(("ISCSI-MIB", "iscsiInstSsnDigestErrors"),
        ("ISCSI-MIB", "iscsiInstSsnCxnTimeoutErrors"),
        ("ISCSI-MIB", "iscsiInstSsnFormatErrors"))
)
if mibBuilder.loadTexts:
    iscsiInstanceSsnErrorStatsGroup.setStatus("current")

iscsiPortalAttributesGroup = ObjectGroup(
    (1, 3, 6, 1, 3, 9999, 3, 1, 3)
)
iscsiPortalAttributesGroup.setObjects(
      *(("ISCSI-MIB", "iscsiPortalRoles"),
        ("ISCSI-MIB", "iscsiPortalAddrType"),
        ("ISCSI-MIB", "iscsiPortalAddr"),
        ("ISCSI-MIB", "iscsiPortalProtocol"),
        ("ISCSI-MIB", "iscsiPortalMaxRecvDataSegLength"),
        ("ISCSI-MIB", "iscsiPortalPrimaryHdrDigest"),
        ("ISCSI-MIB", "iscsiPortalPrimaryDataDigest"),
        ("ISCSI-MIB", "iscsiPortalSecondaryHdrDigest"),
        ("ISCSI-MIB", "iscsiPortalSecondaryDataDigest"),
        ("ISCSI-MIB", "iscsiPortalRecvMarker"))
)
if mibBuilder.loadTexts:
    iscsiPortalAttributesGroup.setStatus("current")

iscsiTgtPortalAttributesGroup = ObjectGroup(
    (1, 3, 6, 1, 3, 9999, 3, 1, 4)
)
iscsiTgtPortalAttributesGroup.setObjects(
      *(("ISCSI-MIB", "iscsiTgtPortalPort"),
        ("ISCSI-MIB", "iscsiTgtPortalTag"))
)
if mibBuilder.loadTexts:
    iscsiTgtPortalAttributesGroup.setStatus("current")

iscsiIntrPortalAttributesGroup = ObjectGroup(
    (1, 3, 6, 1, 3, 9999, 3, 1, 5)
)
iscsiIntrPortalAttributesGroup.setObjects(
    ("ISCSI-MIB", "iscsiIntrPortalTag")
)
if mibBuilder.loadTexts:
    iscsiIntrPortalAttributesGroup.setStatus("current")

iscsiNodeAttributesGroup = ObjectGroup(
    (1, 3, 6, 1, 3, 9999, 3, 1, 6)
)
iscsiNodeAttributesGroup.setObjects(
      *(("ISCSI-MIB", "iscsiNodeName"),
        ("ISCSI-MIB", "iscsiNodeAlias"),
        ("ISCSI-MIB", "iscsiNodeRoles"),
        ("ISCSI-MIB", "iscsiNodeTransportType"),
        ("ISCSI-MIB", "iscsiNodeInitialR2T"),
        ("ISCSI-MIB", "iscsiNodeBidiInitialR2T"),
        ("ISCSI-MIB", "iscsiNodeImmediateData"),
        ("ISCSI-MIB", "iscsiNodeMaxOutstandingR2T"),
        ("ISCSI-MIB", "iscsiNodeFirstBurstSize"),
        ("ISCSI-MIB", "iscsiNodeMaxBurstSize"),
        ("ISCSI-MIB", "iscsiNodeMaxConnections"),
        ("ISCSI-MIB", "iscsiNodeDataSequenceInOrder"),
        ("ISCSI-MIB", "iscsiNodeDataPduInOrder"),
        ("ISCSI-MIB", "iscsiNodeDefaultTime2Wait"),
        ("ISCSI-MIB", "iscsiNodeDefaultTime2Retain"),
        ("ISCSI-MIB", "iscsiNodeErrorRecoveryLevel"))
)
if mibBuilder.loadTexts:
    iscsiNodeAttributesGroup.setStatus("current")

iscsiTargetAttributesGroup = ObjectGroup(
    (1, 3, 6, 1, 3, 9999, 3, 1, 7)
)
iscsiTargetAttributesGroup.setObjects(
      *(("ISCSI-MIB", "iscsiTgtLoginFailures"),
        ("ISCSI-MIB", "iscsiTgtLastFailureTime"),
        ("ISCSI-MIB", "iscsiTgtLastFailureType"),
        ("ISCSI-MIB", "iscsiTgtLastIntrFailureName"),
        ("ISCSI-MIB", "iscsiTgtLastIntrFailureAddrType"),
        ("ISCSI-MIB", "iscsiTgtLastIntrFailureAddr"))
)
if mibBuilder.loadTexts:
    iscsiTargetAttributesGroup.setStatus("current")

iscsiTargetLoginStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 3, 9999, 3, 1, 8)
)
iscsiTargetLoginStatsGroup.setObjects(
      *(("ISCSI-MIB", "iscsiTgtLoginAccepts"),
        ("ISCSI-MIB", "iscsiTgtLoginOtherFails"),
        ("ISCSI-MIB", "iscsiTgtLoginRedirects"),
        ("ISCSI-MIB", "iscsiTgtLoginAuthorizeFails"),
        ("ISCSI-MIB", "iscsiTgtLoginAuthenticateFails"),
        ("ISCSI-MIB", "iscsiTgtLoginNegotiateFails"))
)
if mibBuilder.loadTexts:
    iscsiTargetLoginStatsGroup.setStatus("current")

iscsiTargetLogoutStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 3, 9999, 3, 1, 9)
)
iscsiTargetLogoutStatsGroup.setObjects(
      *(("ISCSI-MIB", "iscsiTgtLogoutNormals"),
        ("ISCSI-MIB", "iscsiTgtLogoutOthers"))
)
if mibBuilder.loadTexts:
    iscsiTargetLogoutStatsGroup.setStatus("current")

iscsiTargetAuthGroup = ObjectGroup(
    (1, 3, 6, 1, 3, 9999, 3, 1, 10)
)
iscsiTargetAuthGroup.setObjects(
      *(("ISCSI-MIB", "iscsiTgtAuthRowStatus"),
        ("ISCSI-MIB", "iscsiTgtAuthIdentity"))
)
if mibBuilder.loadTexts:
    iscsiTargetAuthGroup.setStatus("current")

iscsiInitiatorAttributesGroup = ObjectGroup(
    (1, 3, 6, 1, 3, 9999, 3, 1, 11)
)
iscsiInitiatorAttributesGroup.setObjects(
      *(("ISCSI-MIB", "iscsiIntrLoginFailures"),
        ("ISCSI-MIB", "iscsiIntrLastFailureTime"),
        ("ISCSI-MIB", "iscsiIntrLastFailureType"),
        ("ISCSI-MIB", "iscsiIntrLastTgtFailureName"),
        ("ISCSI-MIB", "iscsiIntrLastTgtFailureAddrType"),
        ("ISCSI-MIB", "iscsiIntrLastTgtFailureAddr"))
)
if mibBuilder.loadTexts:
    iscsiInitiatorAttributesGroup.setStatus("current")

iscsiInitiatorLoginStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 3, 9999, 3, 1, 12)
)
iscsiInitiatorLoginStatsGroup.setObjects(
      *(("ISCSI-MIB", "iscsiIntrLoginAcceptRsps"),
        ("ISCSI-MIB", "iscsiIntrLoginOtherFailRsps"),
        ("ISCSI-MIB", "iscsiIntrLoginRedirectRsps"),
        ("ISCSI-MIB", "iscsiIntrLoginAuthFailRsps"),
        ("ISCSI-MIB", "iscsiIntrLoginAuthenticateFails"),
        ("ISCSI-MIB", "iscsiIntrLoginNegotiateFails"))
)
if mibBuilder.loadTexts:
    iscsiInitiatorLoginStatsGroup.setStatus("current")

iscsiInitiatorLogoutStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 3, 9999, 3, 1, 13)
)
iscsiInitiatorLogoutStatsGroup.setObjects(
      *(("ISCSI-MIB", "iscsiIntrLogoutNormals"),
        ("ISCSI-MIB", "iscsiIntrLogoutOthers"))
)
if mibBuilder.loadTexts:
    iscsiInitiatorLogoutStatsGroup.setStatus("current")

iscsiInitiatorAuthGroup = ObjectGroup(
    (1, 3, 6, 1, 3, 9999, 3, 1, 14)
)
iscsiInitiatorAuthGroup.setObjects(
      *(("ISCSI-MIB", "iscsiIntrAuthRowStatus"),
        ("ISCSI-MIB", "iscsiIntrAuthIdentity"))
)
if mibBuilder.loadTexts:
    iscsiInitiatorAuthGroup.setStatus("current")

iscsiSessionAttributesGroup = ObjectGroup(
    (1, 3, 6, 1, 3, 9999, 3, 1, 15)
)
iscsiSessionAttributesGroup.setObjects(
      *(("ISCSI-MIB", "iscsiSsnDirection"),
        ("ISCSI-MIB", "iscsiSsnInitiatorName"),
        ("ISCSI-MIB", "iscsiSsnTargetName"),
        ("ISCSI-MIB", "iscsiSsnTsih"),
        ("ISCSI-MIB", "iscsiSsnIsid"),
        ("ISCSI-MIB", "iscsiSsnInitiatorAlias"),
        ("ISCSI-MIB", "iscsiSsnTargetAlias"),
        ("ISCSI-MIB", "iscsiSsnInitialR2T"),
        ("ISCSI-MIB", "iscsiSsnBidiInitialR2T"),
        ("ISCSI-MIB", "iscsiSsnImmediateData"),
        ("ISCSI-MIB", "iscsiSsnType"),
        ("ISCSI-MIB", "iscsiSsnMaxOutstandingR2T"),
        ("ISCSI-MIB", "iscsiSsnFirstBurstSize"),
        ("ISCSI-MIB", "iscsiSsnMaxBurstSize"),
        ("ISCSI-MIB", "iscsiSsnConnectionNumber"),
        ("ISCSI-MIB", "iscsiSsnAuthIdentity"),
        ("ISCSI-MIB", "iscsiSsnDataSequenceInOrder"),
        ("ISCSI-MIB", "iscsiSsnDataPduInOrder"),
        ("ISCSI-MIB", "iscsiSsnErrorRecoveryLevel"))
)
if mibBuilder.loadTexts:
    iscsiSessionAttributesGroup.setStatus("current")

iscsiSessionStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 3, 9999, 3, 1, 16)
)
iscsiSessionStatsGroup.setObjects(
      *(("ISCSI-MIB", "iscsiSsnCmdPdus"),
        ("ISCSI-MIB", "iscsiSsnRspPdus"),
        ("ISCSI-MIB", "iscsiSsnTxDataOctets"),
        ("ISCSI-MIB", "iscsiSsnRxDataOctets"))
)
if mibBuilder.loadTexts:
    iscsiSessionStatsGroup.setStatus("current")

iscsiSessionCxnErrorStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 3, 9999, 3, 1, 17)
)
iscsiSessionCxnErrorStatsGroup.setObjects(
      *(("ISCSI-MIB", "iscsiSsnDigestErrors"),
        ("ISCSI-MIB", "iscsiSsnCxnTimeoutErrors"))
)
if mibBuilder.loadTexts:
    iscsiSessionCxnErrorStatsGroup.setStatus("current")

iscsiConnectionAttributesGroup = ObjectGroup(
    (1, 3, 6, 1, 3, 9999, 3, 1, 18)
)
iscsiConnectionAttributesGroup.setObjects(
      *(("ISCSI-MIB", "iscsiCxnCid"),
        ("ISCSI-MIB", "iscsiCxnState"),
        ("ISCSI-MIB", "iscsiCxnProtocol"),
        ("ISCSI-MIB", "iscsiCxnLocalAddrType"),
        ("ISCSI-MIB", "iscsiCxnLocalAddr"),
        ("ISCSI-MIB", "iscsiCxnLocalPort"),
        ("ISCSI-MIB", "iscsiCxnRemoteAddrType"),
        ("ISCSI-MIB", "iscsiCxnRemoteAddr"),
        ("ISCSI-MIB", "iscsiCxnRemotePort"),
        ("ISCSI-MIB", "iscsiCxnMaxRecvDataSegLength"),
        ("ISCSI-MIB", "iscsiCxnHeaderIntegrity"),
        ("ISCSI-MIB", "iscsiCxnDataIntegrity"),
        ("ISCSI-MIB", "iscsiCxnRecvMarker"),
        ("ISCSI-MIB", "iscsiCxnSendMarker"))
)
if mibBuilder.loadTexts:
    iscsiConnectionAttributesGroup.setStatus("current")


# Notification objects

iscsiTgtLoginFailure = NotificationType(
    (1, 3, 6, 1, 3, 9999, 2, 0, 1)
)
iscsiTgtLoginFailure.setObjects(
      *(("ISCSI-MIB", "iscsiTgtLoginFailures"),
        ("ISCSI-MIB", "iscsiTgtLastFailureType"),
        ("ISCSI-MIB", "iscsiTgtLastIntrFailureName"),
        ("ISCSI-MIB", "iscsiTgtLastIntrFailureAddrType"),
        ("ISCSI-MIB", "iscsiTgtLastIntrFailureAddr"))
)
if mibBuilder.loadTexts:
    iscsiTgtLoginFailure.setStatus(
        "current"
    )

iscsiIntrLoginFailure = NotificationType(
    (1, 3, 6, 1, 3, 9999, 2, 0, 2)
)
iscsiIntrLoginFailure.setObjects(
      *(("ISCSI-MIB", "iscsiIntrLoginFailures"),
        ("ISCSI-MIB", "iscsiIntrLastFailureType"),
        ("ISCSI-MIB", "iscsiIntrLastTgtFailureName"),
        ("ISCSI-MIB", "iscsiIntrLastTgtFailureAddrType"),
        ("ISCSI-MIB", "iscsiIntrLastTgtFailureAddr"))
)
if mibBuilder.loadTexts:
    iscsiIntrLoginFailure.setStatus(
        "current"
    )

iscsiInstSessionFailure = NotificationType(
    (1, 3, 6, 1, 3, 9999, 2, 0, 3)
)
iscsiInstSessionFailure.setObjects(
      *(("ISCSI-MIB", "iscsiInstSsnFailures"),
        ("ISCSI-MIB", "iscsiInstLastSsnFailureType"),
        ("ISCSI-MIB", "iscsiInstLastSsnRmtNodeName"))
)
if mibBuilder.loadTexts:
    iscsiInstSessionFailure.setStatus(
        "current"
    )


# Notifications groups

iscsiTgtLgnNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 3, 9999, 3, 1, 19)
)
iscsiTgtLgnNotificationsGroup.setObjects(
    ("ISCSI-MIB", "iscsiTgtLoginFailure")
)
if mibBuilder.loadTexts:
    iscsiTgtLgnNotificationsGroup.setStatus(
        "current"
    )

iscsiIntrLgnNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 3, 9999, 3, 1, 20)
)
iscsiIntrLgnNotificationsGroup.setObjects(
    ("ISCSI-MIB", "iscsiIntrLoginFailure")
)
if mibBuilder.loadTexts:
    iscsiIntrLgnNotificationsGroup.setStatus(
        "current"
    )

iscsiSsnFlrNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 3, 9999, 3, 1, 21)
)
iscsiSsnFlrNotificationsGroup.setObjects(
    ("ISCSI-MIB", "iscsiInstSessionFailure")
)
if mibBuilder.loadTexts:
    iscsiSsnFlrNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

iscsiComplianceV1 = ModuleCompliance(
    (1, 3, 6, 1, 3, 9999, 3, 2, 1)
)
iscsiComplianceV1.setObjects(
      *(("ISCSI-MIB", "iscsiInstanceAttributesGroup"),
        ("ISCSI-MIB", "iscsiPortalAttributesGroup"),
        ("ISCSI-MIB", "iscsiNodeAttributesGroup"),
        ("ISCSI-MIB", "iscsiSessionAttributesGroup"),
        ("ISCSI-MIB", "iscsiSessionStatsGroup"),
        ("ISCSI-MIB", "iscsiSessionCxnErrorStatsGroup"),
        ("ISCSI-MIB", "iscsiConnectionAttributesGroup"),
        ("ISCSI-MIB", "iscsiSsnFlrNotificationsGroup"),
        ("ISCSI-MIB", "iscsiTgtPortalAttributesGroup"),
        ("ISCSI-MIB", "iscsiTargetAttributesGroup"),
        ("ISCSI-MIB", "iscsiTargetLoginStatsGroup"),
        ("ISCSI-MIB", "iscsiTargetLogoutStatsGroup"),
        ("ISCSI-MIB", "iscsiTgtLgnNotificationsGroup"),
        ("ISCSI-MIB", "iscsiTargetAuthGroup"),
        ("ISCSI-MIB", "iscsiIntrPortalAttributesGroup"),
        ("ISCSI-MIB", "iscsiInitiatorAttributesGroup"),
        ("ISCSI-MIB", "iscsiInitiatorLoginStatsGroup"),
        ("ISCSI-MIB", "iscsiInitiatorLogoutStatsGroup"),
        ("ISCSI-MIB", "iscsiIntrLgnNotificationsGroup"),
        ("ISCSI-MIB", "iscsiInitiatorAuthGroup"))
)
if mibBuilder.loadTexts:
    iscsiComplianceV1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ISCSI-MIB",
    **{"IscsiTransportProtocols": IscsiTransportProtocols,
       "IscsiDigestMethod": IscsiDigestMethod,
       "iscsiModule": iscsiModule,
       "iscsiObjects": iscsiObjects,
       "iscsiDescriptors": iscsiDescriptors,
       "iscsiHeaderIntegrityTypes": iscsiHeaderIntegrityTypes,
       "iscsiHdrIntegrityNone": iscsiHdrIntegrityNone,
       "iscsiHdrIntegrityCrc32c": iscsiHdrIntegrityCrc32c,
       "iscsiDataIntegrityTypes": iscsiDataIntegrityTypes,
       "iscsiDataIntegrityNone": iscsiDataIntegrityNone,
       "iscsiDataIntegrityCrc32c": iscsiDataIntegrityCrc32c,
       "iscsiInstance": iscsiInstance,
       "iscsiInstanceAttributesTable": iscsiInstanceAttributesTable,
       "iscsiInstanceAttributesEntry": iscsiInstanceAttributesEntry,
       "iscsiInstIndex": iscsiInstIndex,
       "iscsiInstDescr": iscsiInstDescr,
       "iscsiInstVersionMin": iscsiInstVersionMin,
       "iscsiInstVersionMax": iscsiInstVersionMax,
       "iscsiInstVendorID": iscsiInstVendorID,
       "iscsiInstVendorVersion": iscsiInstVendorVersion,
       "iscsiInstPortalNumber": iscsiInstPortalNumber,
       "iscsiInstNodeNumber": iscsiInstNodeNumber,
       "iscsiInstSessionNumber": iscsiInstSessionNumber,
       "iscsiInstSsnFailures": iscsiInstSsnFailures,
       "iscsiInstLastSsnFailureType": iscsiInstLastSsnFailureType,
       "iscsiInstLastSsnRmtNodeName": iscsiInstLastSsnRmtNodeName,
       "iscsiInstanceSsnErrorStatsTable": iscsiInstanceSsnErrorStatsTable,
       "iscsiInstanceSsnErrorStatsEntry": iscsiInstanceSsnErrorStatsEntry,
       "iscsiInstSsnDigestErrors": iscsiInstSsnDigestErrors,
       "iscsiInstSsnCxnTimeoutErrors": iscsiInstSsnCxnTimeoutErrors,
       "iscsiInstSsnFormatErrors": iscsiInstSsnFormatErrors,
       "iscsiPortal": iscsiPortal,
       "iscsiPortalAttributesTable": iscsiPortalAttributesTable,
       "iscsiPortalAttributesEntry": iscsiPortalAttributesEntry,
       "iscsiPortalIndex": iscsiPortalIndex,
       "iscsiPortalRoles": iscsiPortalRoles,
       "iscsiPortalAddrType": iscsiPortalAddrType,
       "iscsiPortalAddr": iscsiPortalAddr,
       "iscsiPortalProtocol": iscsiPortalProtocol,
       "iscsiPortalMaxRecvDataSegLength": iscsiPortalMaxRecvDataSegLength,
       "iscsiPortalPrimaryHdrDigest": iscsiPortalPrimaryHdrDigest,
       "iscsiPortalPrimaryDataDigest": iscsiPortalPrimaryDataDigest,
       "iscsiPortalSecondaryHdrDigest": iscsiPortalSecondaryHdrDigest,
       "iscsiPortalSecondaryDataDigest": iscsiPortalSecondaryDataDigest,
       "iscsiPortalRecvMarker": iscsiPortalRecvMarker,
       "iscsiTargetPortal": iscsiTargetPortal,
       "iscsiTgtPortalAttributesTable": iscsiTgtPortalAttributesTable,
       "iscsiTgtPortalAttributesEntry": iscsiTgtPortalAttributesEntry,
       "iscsiTgtPortalPort": iscsiTgtPortalPort,
       "iscsiTgtPortalTag": iscsiTgtPortalTag,
       "iscsiInitiatorPortal": iscsiInitiatorPortal,
       "iscsiIntrPortalAttributesTable": iscsiIntrPortalAttributesTable,
       "iscsiIntrPortalAttributesEntry": iscsiIntrPortalAttributesEntry,
       "iscsiIntrPortalTag": iscsiIntrPortalTag,
       "iscsiNode": iscsiNode,
       "iscsiNodeAttributesTable": iscsiNodeAttributesTable,
       "iscsiNodeAttributesEntry": iscsiNodeAttributesEntry,
       "iscsiNodeIndex": iscsiNodeIndex,
       "iscsiNodeName": iscsiNodeName,
       "iscsiNodeAlias": iscsiNodeAlias,
       "iscsiNodeRoles": iscsiNodeRoles,
       "iscsiNodeTransportType": iscsiNodeTransportType,
       "iscsiNodeInitialR2T": iscsiNodeInitialR2T,
       "iscsiNodeBidiInitialR2T": iscsiNodeBidiInitialR2T,
       "iscsiNodeImmediateData": iscsiNodeImmediateData,
       "iscsiNodeMaxOutstandingR2T": iscsiNodeMaxOutstandingR2T,
       "iscsiNodeFirstBurstSize": iscsiNodeFirstBurstSize,
       "iscsiNodeMaxBurstSize": iscsiNodeMaxBurstSize,
       "iscsiNodeMaxConnections": iscsiNodeMaxConnections,
       "iscsiNodeDataSequenceInOrder": iscsiNodeDataSequenceInOrder,
       "iscsiNodeDataPduInOrder": iscsiNodeDataPduInOrder,
       "iscsiNodeDefaultTime2Wait": iscsiNodeDefaultTime2Wait,
       "iscsiNodeDefaultTime2Retain": iscsiNodeDefaultTime2Retain,
       "iscsiNodeErrorRecoveryLevel": iscsiNodeErrorRecoveryLevel,
       "iscsiTarget": iscsiTarget,
       "iscsiTargetAttributesTable": iscsiTargetAttributesTable,
       "iscsiTargetAttributesEntry": iscsiTargetAttributesEntry,
       "iscsiTgtLoginFailures": iscsiTgtLoginFailures,
       "iscsiTgtLastFailureTime": iscsiTgtLastFailureTime,
       "iscsiTgtLastFailureType": iscsiTgtLastFailureType,
       "iscsiTgtLastIntrFailureName": iscsiTgtLastIntrFailureName,
       "iscsiTgtLastIntrFailureAddrType": iscsiTgtLastIntrFailureAddrType,
       "iscsiTgtLastIntrFailureAddr": iscsiTgtLastIntrFailureAddr,
       "iscsiTargetLoginStatsTable": iscsiTargetLoginStatsTable,
       "iscsiTargetLoginStatsEntry": iscsiTargetLoginStatsEntry,
       "iscsiTgtLoginAccepts": iscsiTgtLoginAccepts,
       "iscsiTgtLoginOtherFails": iscsiTgtLoginOtherFails,
       "iscsiTgtLoginRedirects": iscsiTgtLoginRedirects,
       "iscsiTgtLoginAuthorizeFails": iscsiTgtLoginAuthorizeFails,
       "iscsiTgtLoginAuthenticateFails": iscsiTgtLoginAuthenticateFails,
       "iscsiTgtLoginNegotiateFails": iscsiTgtLoginNegotiateFails,
       "iscsiTargetLogoutStatsTable": iscsiTargetLogoutStatsTable,
       "iscsiTargetLogoutStatsEntry": iscsiTargetLogoutStatsEntry,
       "iscsiTgtLogoutNormals": iscsiTgtLogoutNormals,
       "iscsiTgtLogoutOthers": iscsiTgtLogoutOthers,
       "iscsiTgtAuthorization": iscsiTgtAuthorization,
       "iscsiTgtAuthAttributesTable": iscsiTgtAuthAttributesTable,
       "iscsiTgtAuthAttributesEntry": iscsiTgtAuthAttributesEntry,
       "iscsiTgtAuthIndex": iscsiTgtAuthIndex,
       "iscsiTgtAuthRowStatus": iscsiTgtAuthRowStatus,
       "iscsiTgtAuthIdentity": iscsiTgtAuthIdentity,
       "iscsiInitiator": iscsiInitiator,
       "iscsiInitiatorAttributesTable": iscsiInitiatorAttributesTable,
       "iscsiInitiatorAttributesEntry": iscsiInitiatorAttributesEntry,
       "iscsiIntrLoginFailures": iscsiIntrLoginFailures,
       "iscsiIntrLastFailureTime": iscsiIntrLastFailureTime,
       "iscsiIntrLastFailureType": iscsiIntrLastFailureType,
       "iscsiIntrLastTgtFailureName": iscsiIntrLastTgtFailureName,
       "iscsiIntrLastTgtFailureAddrType": iscsiIntrLastTgtFailureAddrType,
       "iscsiIntrLastTgtFailureAddr": iscsiIntrLastTgtFailureAddr,
       "iscsiInitiatorLoginStatsTable": iscsiInitiatorLoginStatsTable,
       "iscsiInitiatorLoginStatsEntry": iscsiInitiatorLoginStatsEntry,
       "iscsiIntrLoginAcceptRsps": iscsiIntrLoginAcceptRsps,
       "iscsiIntrLoginOtherFailRsps": iscsiIntrLoginOtherFailRsps,
       "iscsiIntrLoginRedirectRsps": iscsiIntrLoginRedirectRsps,
       "iscsiIntrLoginAuthFailRsps": iscsiIntrLoginAuthFailRsps,
       "iscsiIntrLoginAuthenticateFails": iscsiIntrLoginAuthenticateFails,
       "iscsiIntrLoginNegotiateFails": iscsiIntrLoginNegotiateFails,
       "iscsiInitiatorLogoutStatsTable": iscsiInitiatorLogoutStatsTable,
       "iscsiInitiatorLogoutStatsEntry": iscsiInitiatorLogoutStatsEntry,
       "iscsiIntrLogoutNormals": iscsiIntrLogoutNormals,
       "iscsiIntrLogoutOthers": iscsiIntrLogoutOthers,
       "iscsiIntrAuthorization": iscsiIntrAuthorization,
       "iscsiIntrAuthAttributesTable": iscsiIntrAuthAttributesTable,
       "iscsiIntrAuthAttributesEntry": iscsiIntrAuthAttributesEntry,
       "iscsiIntrAuthIndex": iscsiIntrAuthIndex,
       "iscsiIntrAuthRowStatus": iscsiIntrAuthRowStatus,
       "iscsiIntrAuthIdentity": iscsiIntrAuthIdentity,
       "iscsiSession": iscsiSession,
       "iscsiSessionAttributesTable": iscsiSessionAttributesTable,
       "iscsiSessionAttributesEntry": iscsiSessionAttributesEntry,
       "iscsiSsnIndex": iscsiSsnIndex,
       "iscsiSsnDirection": iscsiSsnDirection,
       "iscsiSsnInitiatorName": iscsiSsnInitiatorName,
       "iscsiSsnTargetName": iscsiSsnTargetName,
       "iscsiSsnTsih": iscsiSsnTsih,
       "iscsiSsnIsid": iscsiSsnIsid,
       "iscsiSsnInitiatorAlias": iscsiSsnInitiatorAlias,
       "iscsiSsnTargetAlias": iscsiSsnTargetAlias,
       "iscsiSsnInitialR2T": iscsiSsnInitialR2T,
       "iscsiSsnBidiInitialR2T": iscsiSsnBidiInitialR2T,
       "iscsiSsnImmediateData": iscsiSsnImmediateData,
       "iscsiSsnType": iscsiSsnType,
       "iscsiSsnMaxOutstandingR2T": iscsiSsnMaxOutstandingR2T,
       "iscsiSsnFirstBurstSize": iscsiSsnFirstBurstSize,
       "iscsiSsnMaxBurstSize": iscsiSsnMaxBurstSize,
       "iscsiSsnConnectionNumber": iscsiSsnConnectionNumber,
       "iscsiSsnAuthIdentity": iscsiSsnAuthIdentity,
       "iscsiSsnDataSequenceInOrder": iscsiSsnDataSequenceInOrder,
       "iscsiSsnDataPduInOrder": iscsiSsnDataPduInOrder,
       "iscsiSsnErrorRecoveryLevel": iscsiSsnErrorRecoveryLevel,
       "iscsiSessionStatsTable": iscsiSessionStatsTable,
       "iscsiSessionStatsEntry": iscsiSessionStatsEntry,
       "iscsiSsnCmdPdus": iscsiSsnCmdPdus,
       "iscsiSsnRspPdus": iscsiSsnRspPdus,
       "iscsiSsnTxDataOctets": iscsiSsnTxDataOctets,
       "iscsiSsnRxDataOctets": iscsiSsnRxDataOctets,
       "iscsiSessionCxnErrorStatsTable": iscsiSessionCxnErrorStatsTable,
       "iscsiSessionCxnErrorStatsEntry": iscsiSessionCxnErrorStatsEntry,
       "iscsiSsnDigestErrors": iscsiSsnDigestErrors,
       "iscsiSsnCxnTimeoutErrors": iscsiSsnCxnTimeoutErrors,
       "iscsiConnection": iscsiConnection,
       "iscsiConnectionAttributesTable": iscsiConnectionAttributesTable,
       "iscsiConnectionAttributesEntry": iscsiConnectionAttributesEntry,
       "iscsiCxnIndex": iscsiCxnIndex,
       "iscsiCxnCid": iscsiCxnCid,
       "iscsiCxnState": iscsiCxnState,
       "iscsiCxnLocalAddrType": iscsiCxnLocalAddrType,
       "iscsiCxnLocalAddr": iscsiCxnLocalAddr,
       "iscsiCxnProtocol": iscsiCxnProtocol,
       "iscsiCxnLocalPort": iscsiCxnLocalPort,
       "iscsiCxnRemoteAddrType": iscsiCxnRemoteAddrType,
       "iscsiCxnRemoteAddr": iscsiCxnRemoteAddr,
       "iscsiCxnRemotePort": iscsiCxnRemotePort,
       "iscsiCxnMaxRecvDataSegLength": iscsiCxnMaxRecvDataSegLength,
       "iscsiCxnHeaderIntegrity": iscsiCxnHeaderIntegrity,
       "iscsiCxnDataIntegrity": iscsiCxnDataIntegrity,
       "iscsiCxnRecvMarker": iscsiCxnRecvMarker,
       "iscsiCxnSendMarker": iscsiCxnSendMarker,
       "iscsiNotifications": iscsiNotifications,
       "iscsiNotificationsPrefix": iscsiNotificationsPrefix,
       "iscsiTgtLoginFailure": iscsiTgtLoginFailure,
       "iscsiIntrLoginFailure": iscsiIntrLoginFailure,
       "iscsiInstSessionFailure": iscsiInstSessionFailure,
       "iscsiConformance": iscsiConformance,
       "iscsiGroups": iscsiGroups,
       "iscsiInstanceAttributesGroup": iscsiInstanceAttributesGroup,
       "iscsiInstanceSsnErrorStatsGroup": iscsiInstanceSsnErrorStatsGroup,
       "iscsiPortalAttributesGroup": iscsiPortalAttributesGroup,
       "iscsiTgtPortalAttributesGroup": iscsiTgtPortalAttributesGroup,
       "iscsiIntrPortalAttributesGroup": iscsiIntrPortalAttributesGroup,
       "iscsiNodeAttributesGroup": iscsiNodeAttributesGroup,
       "iscsiTargetAttributesGroup": iscsiTargetAttributesGroup,
       "iscsiTargetLoginStatsGroup": iscsiTargetLoginStatsGroup,
       "iscsiTargetLogoutStatsGroup": iscsiTargetLogoutStatsGroup,
       "iscsiTargetAuthGroup": iscsiTargetAuthGroup,
       "iscsiInitiatorAttributesGroup": iscsiInitiatorAttributesGroup,
       "iscsiInitiatorLoginStatsGroup": iscsiInitiatorLoginStatsGroup,
       "iscsiInitiatorLogoutStatsGroup": iscsiInitiatorLogoutStatsGroup,
       "iscsiInitiatorAuthGroup": iscsiInitiatorAuthGroup,
       "iscsiSessionAttributesGroup": iscsiSessionAttributesGroup,
       "iscsiSessionStatsGroup": iscsiSessionStatsGroup,
       "iscsiSessionCxnErrorStatsGroup": iscsiSessionCxnErrorStatsGroup,
       "iscsiConnectionAttributesGroup": iscsiConnectionAttributesGroup,
       "iscsiTgtLgnNotificationsGroup": iscsiTgtLgnNotificationsGroup,
       "iscsiIntrLgnNotificationsGroup": iscsiIntrLgnNotificationsGroup,
       "iscsiSsnFlrNotificationsGroup": iscsiSsnFlrNotificationsGroup,
       "iscsiCompliances": iscsiCompliances,
       "iscsiComplianceV1": iscsiComplianceV1}
)
