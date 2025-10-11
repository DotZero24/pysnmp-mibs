# SNMP MIB module (DC-CR-LDP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/mrv/DC-CR-LDP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:05:13 2025
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

(InterfaceIndexOrZero,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

dccrldp = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 629, 10, 15)
)
if mibBuilder.loadTexts:
    dccrldp.setRevisions(
        ("2014-12-21 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class DcCrldpAdminStatus(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )



class DcCrldpOperStatus(TextualConvention, Integer32):
    status = "current"
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
        *(("up", 1),
          ("down", 2),
          ("goingUp", 3),
          ("goingDown", 4),
          ("actFailed", 5))
    )



class DcCrldpIndex(TextualConvention, Unsigned32):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_Nbase_ObjectIdentity = ObjectIdentity
nbase = _Nbase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629)
)
_Opx_ObjectIdentity = ObjectIdentity
opx = _Opx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 10)
)
_DccrldpObjects_ObjectIdentity = ObjectIdentity
dccrldpObjects = _DccrldpObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 10, 15, 1)
)
_DccrldpSigTable_Object = MibTable
dccrldpSigTable = _DccrldpSigTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 15, 1, 1)
)
if mibBuilder.loadTexts:
    dccrldpSigTable.setStatus("current")
_DccrldpSigEntry_Object = MibTableRow
dccrldpSigEntry = _DccrldpSigEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 15, 1, 1, 1)
)
dccrldpSigEntry.setIndexNames(
    (0, "DC-CR-LDP-MIB", "dccrldpSigIndex"),
)
if mibBuilder.loadTexts:
    dccrldpSigEntry.setStatus("current")
_DccrldpSigIndex_Type = DcCrldpIndex
_DccrldpSigIndex_Object = MibTableColumn
dccrldpSigIndex = _DccrldpSigIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 15, 1, 1, 1, 1),
    _DccrldpSigIndex_Type()
)
dccrldpSigIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dccrldpSigIndex.setStatus("current")


class _DccrldpSigPathManagerIndex_Type(DcCrldpIndex):
    """Custom type dccrldpSigPathManagerIndex based on DcCrldpIndex"""
    defaultValue = 0


_DccrldpSigPathManagerIndex_Type.__name__ = "DcCrldpIndex"
_DccrldpSigPathManagerIndex_Object = MibTableColumn
dccrldpSigPathManagerIndex = _DccrldpSigPathManagerIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 15, 1, 1, 1, 2),
    _DccrldpSigPathManagerIndex_Type()
)
dccrldpSigPathManagerIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dccrldpSigPathManagerIndex.setStatus("current")


class _DccrldpSigLsrIndex_Type(Unsigned32):
    """Custom type dccrldpSigLsrIndex based on Unsigned32"""
    defaultValue = 0


_DccrldpSigLsrIndex_Type.__name__ = "Unsigned32"
_DccrldpSigLsrIndex_Object = MibTableColumn
dccrldpSigLsrIndex = _DccrldpSigLsrIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 15, 1, 1, 1, 3),
    _DccrldpSigLsrIndex_Type()
)
dccrldpSigLsrIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dccrldpSigLsrIndex.setStatus("current")


class _DccrldpSigSocketIfIndex_Type(InterfaceIndexOrZero):
    """Custom type dccrldpSigSocketIfIndex based on InterfaceIndexOrZero"""
    defaultValue = 0


_DccrldpSigSocketIfIndex_Type.__name__ = "InterfaceIndexOrZero"
_DccrldpSigSocketIfIndex_Object = MibTableColumn
dccrldpSigSocketIfIndex = _DccrldpSigSocketIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 15, 1, 1, 1, 4),
    _DccrldpSigSocketIfIndex_Type()
)
dccrldpSigSocketIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dccrldpSigSocketIfIndex.setStatus("current")


class _DccrldpSigSessionBufPoolSize_Type(Integer32):
    """Custom type dccrldpSigSessionBufPoolSize based on Integer32"""
    defaultValue = 8


_DccrldpSigSessionBufPoolSize_Type.__name__ = "Integer32"
_DccrldpSigSessionBufPoolSize_Object = MibTableColumn
dccrldpSigSessionBufPoolSize = _DccrldpSigSessionBufPoolSize_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 15, 1, 1, 1, 5),
    _DccrldpSigSessionBufPoolSize_Type()
)
dccrldpSigSessionBufPoolSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dccrldpSigSessionBufPoolSize.setStatus("current")


class _DccrldpSigEMBufPoolSize_Type(Integer32):
    """Custom type dccrldpSigEMBufPoolSize based on Integer32"""
    defaultValue = 8


_DccrldpSigEMBufPoolSize_Type.__name__ = "Integer32"
_DccrldpSigEMBufPoolSize_Object = MibTableColumn
dccrldpSigEMBufPoolSize = _DccrldpSigEMBufPoolSize_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 15, 1, 1, 1, 6),
    _DccrldpSigEMBufPoolSize_Type()
)
dccrldpSigEMBufPoolSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dccrldpSigEMBufPoolSize.setStatus("current")


class _DccrldpSigAMBufPoolSize_Type(Integer32):
    """Custom type dccrldpSigAMBufPoolSize based on Integer32"""
    defaultValue = 8


_DccrldpSigAMBufPoolSize_Type.__name__ = "Integer32"
_DccrldpSigAMBufPoolSize_Object = MibTableColumn
dccrldpSigAMBufPoolSize = _DccrldpSigAMBufPoolSize_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 15, 1, 1, 1, 7),
    _DccrldpSigAMBufPoolSize_Type()
)
dccrldpSigAMBufPoolSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dccrldpSigAMBufPoolSize.setStatus("current")


class _DccrldpSigAdminStatus_Type(DcCrldpAdminStatus):
    """Custom type dccrldpSigAdminStatus based on DcCrldpAdminStatus"""
    defaultValue = 1


_DccrldpSigAdminStatus_Type.__name__ = "DcCrldpAdminStatus"
_DccrldpSigAdminStatus_Object = MibTableColumn
dccrldpSigAdminStatus = _DccrldpSigAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 15, 1, 1, 1, 8),
    _DccrldpSigAdminStatus_Type()
)
dccrldpSigAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dccrldpSigAdminStatus.setStatus("current")
_DccrldpSigOperStatus_Type = DcCrldpOperStatus
_DccrldpSigOperStatus_Object = MibTableColumn
dccrldpSigOperStatus = _DccrldpSigOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 15, 1, 1, 1, 9),
    _DccrldpSigOperStatus_Type()
)
dccrldpSigOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dccrldpSigOperStatus.setStatus("current")
_DccrldpSigRowStatus_Type = RowStatus
_DccrldpSigRowStatus_Object = MibTableColumn
dccrldpSigRowStatus = _DccrldpSigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 15, 1, 1, 1, 10),
    _DccrldpSigRowStatus_Type()
)
dccrldpSigRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dccrldpSigRowStatus.setStatus("current")


class _DccrldpSigUseI3Interface_Type(TruthValue):
    """Custom type dccrldpSigUseI3Interface based on TruthValue"""
    defaultValue = 2


_DccrldpSigUseI3Interface_Type.__name__ = "TruthValue"
_DccrldpSigUseI3Interface_Object = MibTableColumn
dccrldpSigUseI3Interface = _DccrldpSigUseI3Interface_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 15, 1, 1, 1, 11),
    _DccrldpSigUseI3Interface_Type()
)
dccrldpSigUseI3Interface.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dccrldpSigUseI3Interface.setStatus("current")


class _DccrldpSigConformanceFlags_Type(Bits):
    """Custom type dccrldpSigConformanceFlags based on Bits"""
    defaultBinValue = "0"

    namedValues = NamedValues(
        ("maxPduLen", 0)
    )

_DccrldpSigConformanceFlags_Type.__name__ = "Bits"
_DccrldpSigConformanceFlags_Object = MibTableColumn
dccrldpSigConformanceFlags = _DccrldpSigConformanceFlags_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 15, 1, 1, 1, 12),
    _DccrldpSigConformanceFlags_Type()
)
dccrldpSigConformanceFlags.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dccrldpSigConformanceFlags.setStatus("current")


class _DccrldpSigUseIPv6Transport_Type(TruthValue):
    """Custom type dccrldpSigUseIPv6Transport based on TruthValue"""
    defaultValue = 2


_DccrldpSigUseIPv6Transport_Type.__name__ = "TruthValue"
_DccrldpSigUseIPv6Transport_Object = MibTableColumn
dccrldpSigUseIPv6Transport = _DccrldpSigUseIPv6Transport_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 15, 1, 1, 1, 13),
    _DccrldpSigUseIPv6Transport_Type()
)
dccrldpSigUseIPv6Transport.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dccrldpSigUseIPv6Transport.setStatus("current")


class _DccrldpSigSessStatusTrapEnable_Type(TruthValue):
    """Custom type dccrldpSigSessStatusTrapEnable based on TruthValue"""
    defaultValue = 2


_DccrldpSigSessStatusTrapEnable_Type.__name__ = "TruthValue"
_DccrldpSigSessStatusTrapEnable_Object = MibTableColumn
dccrldpSigSessStatusTrapEnable = _DccrldpSigSessStatusTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 15, 1, 1, 1, 14),
    _DccrldpSigSessStatusTrapEnable_Type()
)
dccrldpSigSessStatusTrapEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dccrldpSigSessStatusTrapEnable.setStatus("current")


class _DccrldpSigSessThreshTrapEnable_Type(TruthValue):
    """Custom type dccrldpSigSessThreshTrapEnable based on TruthValue"""
    defaultValue = 2


_DccrldpSigSessThreshTrapEnable_Type.__name__ = "TruthValue"
_DccrldpSigSessThreshTrapEnable_Object = MibTableColumn
dccrldpSigSessThreshTrapEnable = _DccrldpSigSessThreshTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 15, 1, 1, 1, 15),
    _DccrldpSigSessThreshTrapEnable_Type()
)
dccrldpSigSessThreshTrapEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dccrldpSigSessThreshTrapEnable.setStatus("current")


class _DccrldpSigPathVecLimitTrapEnable_Type(TruthValue):
    """Custom type dccrldpSigPathVecLimitTrapEnable based on TruthValue"""
    defaultValue = 2


_DccrldpSigPathVecLimitTrapEnable_Type.__name__ = "TruthValue"
_DccrldpSigPathVecLimitTrapEnable_Object = MibTableColumn
dccrldpSigPathVecLimitTrapEnable = _DccrldpSigPathVecLimitTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 15, 1, 1, 1, 16),
    _DccrldpSigPathVecLimitTrapEnable_Type()
)
dccrldpSigPathVecLimitTrapEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dccrldpSigPathVecLimitTrapEnable.setStatus("current")


class _DccrldpSigBfdProviderIndex_Type(Integer32):
    """Custom type dccrldpSigBfdProviderIndex based on Integer32"""
    defaultValue = 0


_DccrldpSigBfdProviderIndex_Type.__name__ = "Integer32"
_DccrldpSigBfdProviderIndex_Object = MibTableColumn
dccrldpSigBfdProviderIndex = _DccrldpSigBfdProviderIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 15, 1, 1, 1, 17),
    _DccrldpSigBfdProviderIndex_Type()
)
dccrldpSigBfdProviderIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dccrldpSigBfdProviderIndex.setStatus("current")
_DccrldpPmTable_Object = MibTable
dccrldpPmTable = _DccrldpPmTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 15, 1, 2)
)
if mibBuilder.loadTexts:
    dccrldpPmTable.setStatus("current")
_DccrldpPmEntry_Object = MibTableRow
dccrldpPmEntry = _DccrldpPmEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 15, 1, 2, 1)
)
dccrldpPmEntry.setIndexNames(
    (0, "DC-CR-LDP-MIB", "dccrldpPmIndex"),
)
if mibBuilder.loadTexts:
    dccrldpPmEntry.setStatus("current")
_DccrldpPmIndex_Type = DcCrldpIndex
_DccrldpPmIndex_Object = MibTableColumn
dccrldpPmIndex = _DccrldpPmIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 15, 1, 2, 1, 1),
    _DccrldpPmIndex_Type()
)
dccrldpPmIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dccrldpPmIndex.setStatus("current")


class _DccrldpPmLsrIndex_Type(Unsigned32):
    """Custom type dccrldpPmLsrIndex based on Unsigned32"""
    defaultValue = 0


_DccrldpPmLsrIndex_Type.__name__ = "Unsigned32"
_DccrldpPmLsrIndex_Object = MibTableColumn
dccrldpPmLsrIndex = _DccrldpPmLsrIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 15, 1, 2, 1, 2),
    _DccrldpPmLsrIndex_Type()
)
dccrldpPmLsrIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dccrldpPmLsrIndex.setStatus("current")


class _DccrldpPmLdpEntityAutoCreate_Type(TruthValue):
    """Custom type dccrldpPmLdpEntityAutoCreate based on TruthValue"""
    defaultValue = 1


_DccrldpPmLdpEntityAutoCreate_Type.__name__ = "TruthValue"
_DccrldpPmLdpEntityAutoCreate_Object = MibTableColumn
dccrldpPmLdpEntityAutoCreate = _DccrldpPmLdpEntityAutoCreate_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 15, 1, 2, 1, 3),
    _DccrldpPmLdpEntityAutoCreate_Type()
)
dccrldpPmLdpEntityAutoCreate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dccrldpPmLdpEntityAutoCreate.setStatus("current")


class _DccrldpPmLdpEntityAutoStart_Type(TruthValue):
    """Custom type dccrldpPmLdpEntityAutoStart based on TruthValue"""
    defaultValue = 1


_DccrldpPmLdpEntityAutoStart_Type.__name__ = "TruthValue"
_DccrldpPmLdpEntityAutoStart_Object = MibTableColumn
dccrldpPmLdpEntityAutoStart = _DccrldpPmLdpEntityAutoStart_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 15, 1, 2, 1, 4),
    _DccrldpPmLdpEntityAutoStart_Type()
)
dccrldpPmLdpEntityAutoStart.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dccrldpPmLdpEntityAutoStart.setStatus("current")


class _DccrldpPmLdpEntityReuse_Type(TruthValue):
    """Custom type dccrldpPmLdpEntityReuse based on TruthValue"""
    defaultValue = 1


_DccrldpPmLdpEntityReuse_Type.__name__ = "TruthValue"
_DccrldpPmLdpEntityReuse_Object = MibTableColumn
dccrldpPmLdpEntityReuse = _DccrldpPmLdpEntityReuse_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 15, 1, 2, 1, 5),
    _DccrldpPmLdpEntityReuse_Type()
)
dccrldpPmLdpEntityReuse.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dccrldpPmLdpEntityReuse.setStatus("current")


class _DccrldpPmLdpVersion_Type(Integer32):
    """Custom type dccrldpPmLdpVersion based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("version1", 1)
    )


_DccrldpPmLdpVersion_Type.__name__ = "Integer32"
_DccrldpPmLdpVersion_Object = MibTableColumn
dccrldpPmLdpVersion = _DccrldpPmLdpVersion_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 15, 1, 2, 1, 6),
    _DccrldpPmLdpVersion_Type()
)
dccrldpPmLdpVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dccrldpPmLdpVersion.setStatus("current")


class _DccrldpPmUseLdpFt_Type(TruthValue):
    """Custom type dccrldpPmUseLdpFt based on TruthValue"""
    defaultValue = 2


_DccrldpPmUseLdpFt_Type.__name__ = "TruthValue"
_DccrldpPmUseLdpFt_Object = MibTableColumn
dccrldpPmUseLdpFt = _DccrldpPmUseLdpFt_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 15, 1, 2, 1, 7),
    _DccrldpPmUseLdpFt_Type()
)
dccrldpPmUseLdpFt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dccrldpPmUseLdpFt.setStatus("current")


class _DccrldpPmAsNumber_Type(Integer32):
    """Custom type dccrldpPmAsNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DccrldpPmAsNumber_Type.__name__ = "Integer32"
_DccrldpPmAsNumber_Object = MibTableColumn
dccrldpPmAsNumber = _DccrldpPmAsNumber_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 15, 1, 2, 1, 8),
    _DccrldpPmAsNumber_Type()
)
dccrldpPmAsNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dccrldpPmAsNumber.setStatus("current")


class _DccrldpPmIprBufPoolSize_Type(Integer32):
    """Custom type dccrldpPmIprBufPoolSize based on Integer32"""
    defaultValue = 8


_DccrldpPmIprBufPoolSize_Type.__name__ = "Integer32"
_DccrldpPmIprBufPoolSize_Object = MibTableColumn
dccrldpPmIprBufPoolSize = _DccrldpPmIprBufPoolSize_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 15, 1, 2, 1, 9),
    _DccrldpPmIprBufPoolSize_Type()
)
dccrldpPmIprBufPoolSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dccrldpPmIprBufPoolSize.setStatus("current")


class _DccrldpPmLdpSupported_Type(TruthValue):
    """Custom type dccrldpPmLdpSupported based on TruthValue"""
    defaultValue = 2


_DccrldpPmLdpSupported_Type.__name__ = "TruthValue"
_DccrldpPmLdpSupported_Object = MibTableColumn
dccrldpPmLdpSupported = _DccrldpPmLdpSupported_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 15, 1, 2, 1, 10),
    _DccrldpPmLdpSupported_Type()
)
dccrldpPmLdpSupported.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dccrldpPmLdpSupported.setStatus("current")


class _DccrldpPmCrLdpSupported_Type(TruthValue):
    """Custom type dccrldpPmCrLdpSupported based on TruthValue"""
    defaultValue = 2


_DccrldpPmCrLdpSupported_Type.__name__ = "TruthValue"
_DccrldpPmCrLdpSupported_Object = MibTableColumn
dccrldpPmCrLdpSupported = _DccrldpPmCrLdpSupported_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 15, 1, 2, 1, 11),
    _DccrldpPmCrLdpSupported_Type()
)
dccrldpPmCrLdpSupported.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dccrldpPmCrLdpSupported.setStatus("current")


class _DccrldpPmQueryFECSupported_Type(TruthValue):
    """Custom type dccrldpPmQueryFECSupported based on TruthValue"""
    defaultValue = 2


_DccrldpPmQueryFECSupported_Type.__name__ = "TruthValue"
_DccrldpPmQueryFECSupported_Object = MibTableColumn
dccrldpPmQueryFECSupported = _DccrldpPmQueryFECSupported_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 15, 1, 2, 1, 12),
    _DccrldpPmQueryFECSupported_Type()
)
dccrldpPmQueryFECSupported.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dccrldpPmQueryFECSupported.setStatus("current")


class _DccrldpPmAdminStatus_Type(DcCrldpAdminStatus):
    """Custom type dccrldpPmAdminStatus based on DcCrldpAdminStatus"""
    defaultValue = 1


_DccrldpPmAdminStatus_Type.__name__ = "DcCrldpAdminStatus"
_DccrldpPmAdminStatus_Object = MibTableColumn
dccrldpPmAdminStatus = _DccrldpPmAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 15, 1, 2, 1, 13),
    _DccrldpPmAdminStatus_Type()
)
dccrldpPmAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dccrldpPmAdminStatus.setStatus("current")
_DccrldpPmOperStatus_Type = DcCrldpOperStatus
_DccrldpPmOperStatus_Object = MibTableColumn
dccrldpPmOperStatus = _DccrldpPmOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 15, 1, 2, 1, 14),
    _DccrldpPmOperStatus_Type()
)
dccrldpPmOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dccrldpPmOperStatus.setStatus("current")
_DccrldpPmRowStatus_Type = RowStatus
_DccrldpPmRowStatus_Object = MibTableColumn
dccrldpPmRowStatus = _DccrldpPmRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 15, 1, 2, 1, 15),
    _DccrldpPmRowStatus_Type()
)
dccrldpPmRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dccrldpPmRowStatus.setStatus("current")


class _DccrldpPmRestartCapable_Type(TruthValue):
    """Custom type dccrldpPmRestartCapable based on TruthValue"""
    defaultValue = 2


_DccrldpPmRestartCapable_Type.__name__ = "TruthValue"
_DccrldpPmRestartCapable_Object = MibTableColumn
dccrldpPmRestartCapable = _DccrldpPmRestartCapable_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 15, 1, 2, 1, 16),
    _DccrldpPmRestartCapable_Type()
)
dccrldpPmRestartCapable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dccrldpPmRestartCapable.setStatus("current")


class _DccrldpPmReconnectTime_Type(Integer32):
    """Custom type dccrldpPmReconnectTime based on Integer32"""
    defaultValue = 60000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_DccrldpPmReconnectTime_Type.__name__ = "Integer32"
_DccrldpPmReconnectTime_Object = MibTableColumn
dccrldpPmReconnectTime = _DccrldpPmReconnectTime_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 15, 1, 2, 1, 17),
    _DccrldpPmReconnectTime_Type()
)
dccrldpPmReconnectTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dccrldpPmReconnectTime.setStatus("current")
if mibBuilder.loadTexts:
    dccrldpPmReconnectTime.setUnits("milliseconds")


class _DccrldpPmRecoveryTime_Type(Integer32):
    """Custom type dccrldpPmRecoveryTime based on Integer32"""
    defaultValue = 180000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_DccrldpPmRecoveryTime_Type.__name__ = "Integer32"
_DccrldpPmRecoveryTime_Object = MibTableColumn
dccrldpPmRecoveryTime = _DccrldpPmRecoveryTime_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 15, 1, 2, 1, 18),
    _DccrldpPmRecoveryTime_Type()
)
dccrldpPmRecoveryTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dccrldpPmRecoveryTime.setStatus("current")
if mibBuilder.loadTexts:
    dccrldpPmRecoveryTime.setUnits("milliseconds")


class _DccrldpPmMaxPeerReconnect_Type(Integer32):
    """Custom type dccrldpPmMaxPeerReconnect based on Integer32"""
    defaultValue = 180000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_DccrldpPmMaxPeerReconnect_Type.__name__ = "Integer32"
_DccrldpPmMaxPeerReconnect_Object = MibTableColumn
dccrldpPmMaxPeerReconnect = _DccrldpPmMaxPeerReconnect_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 15, 1, 2, 1, 19),
    _DccrldpPmMaxPeerReconnect_Type()
)
dccrldpPmMaxPeerReconnect.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dccrldpPmMaxPeerReconnect.setStatus("current")
if mibBuilder.loadTexts:
    dccrldpPmMaxPeerReconnect.setUnits("milliseconds")


class _DccrldpPmMaxPeerRecovery_Type(Integer32):
    """Custom type dccrldpPmMaxPeerRecovery based on Integer32"""
    defaultValue = 240000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_DccrldpPmMaxPeerRecovery_Type.__name__ = "Integer32"
_DccrldpPmMaxPeerRecovery_Object = MibTableColumn
dccrldpPmMaxPeerRecovery = _DccrldpPmMaxPeerRecovery_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 15, 1, 2, 1, 20),
    _DccrldpPmMaxPeerRecovery_Type()
)
dccrldpPmMaxPeerRecovery.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dccrldpPmMaxPeerRecovery.setStatus("current")
if mibBuilder.loadTexts:
    dccrldpPmMaxPeerRecovery.setUnits("milliseconds")


class _DccrldpPmAdjDwnHoldTime_Type(Integer32):
    """Custom type dccrldpPmAdjDwnHoldTime based on Integer32"""
    defaultValue = 3000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_DccrldpPmAdjDwnHoldTime_Type.__name__ = "Integer32"
_DccrldpPmAdjDwnHoldTime_Object = MibTableColumn
dccrldpPmAdjDwnHoldTime = _DccrldpPmAdjDwnHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 15, 1, 2, 1, 21),
    _DccrldpPmAdjDwnHoldTime_Type()
)
dccrldpPmAdjDwnHoldTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dccrldpPmAdjDwnHoldTime.setStatus("current")
if mibBuilder.loadTexts:
    dccrldpPmAdjDwnHoldTime.setUnits("milliseconds")


class _DccrldpPmOutSegProgOrder_Type(Integer32):
    """Custom type dccrldpPmOutSegProgOrder based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("default", 0),
          ("connFirst", 1))
    )


_DccrldpPmOutSegProgOrder_Type.__name__ = "Integer32"
_DccrldpPmOutSegProgOrder_Object = MibTableColumn
dccrldpPmOutSegProgOrder = _DccrldpPmOutSegProgOrder_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 15, 1, 2, 1, 22),
    _DccrldpPmOutSegProgOrder_Type()
)
dccrldpPmOutSegProgOrder.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dccrldpPmOutSegProgOrder.setStatus("current")


class _DccrldpPmSupportIpv6_Type(TruthValue):
    """Custom type dccrldpPmSupportIpv6 based on TruthValue"""
    defaultValue = 2


_DccrldpPmSupportIpv6_Type.__name__ = "TruthValue"
_DccrldpPmSupportIpv6_Object = MibTableColumn
dccrldpPmSupportIpv6 = _DccrldpPmSupportIpv6_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 15, 1, 2, 1, 23),
    _DccrldpPmSupportIpv6_Type()
)
dccrldpPmSupportIpv6.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dccrldpPmSupportIpv6.setStatus("current")


class _DccrldpPmPolicySupportFlags_Type(Bits):
    """Custom type dccrldpPmPolicySupportFlags based on Bits"""
    namedValues = NamedValues(
        *(("policySupported", 0),
          ("perFecOptimizationSupported", 1),
          ("suppressAddressPolicy", 2),
          ("policyForVCFECs", 3))
    )

_DccrldpPmPolicySupportFlags_Type.__name__ = "Bits"
_DccrldpPmPolicySupportFlags_Object = MibTableColumn
dccrldpPmPolicySupportFlags = _DccrldpPmPolicySupportFlags_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 15, 1, 2, 1, 24),
    _DccrldpPmPolicySupportFlags_Type()
)
dccrldpPmPolicySupportFlags.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dccrldpPmPolicySupportFlags.setStatus("current")


class _DccrldpPmCheckOutSegIntfaceStat_Type(TruthValue):
    """Custom type dccrldpPmCheckOutSegIntfaceStat based on TruthValue"""
    defaultValue = 2


_DccrldpPmCheckOutSegIntfaceStat_Type.__name__ = "TruthValue"
_DccrldpPmCheckOutSegIntfaceStat_Object = MibTableColumn
dccrldpPmCheckOutSegIntfaceStat = _DccrldpPmCheckOutSegIntfaceStat_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 15, 1, 2, 1, 25),
    _DccrldpPmCheckOutSegIntfaceStat_Type()
)
dccrldpPmCheckOutSegIntfaceStat.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dccrldpPmCheckOutSegIntfaceStat.setStatus("current")


class _DccrldpPmLdpEntityCreateNhrLdb_Type(TruthValue):
    """Custom type dccrldpPmLdpEntityCreateNhrLdb based on TruthValue"""
    defaultValue = 1


_DccrldpPmLdpEntityCreateNhrLdb_Type.__name__ = "TruthValue"
_DccrldpPmLdpEntityCreateNhrLdb_Object = MibTableColumn
dccrldpPmLdpEntityCreateNhrLdb = _DccrldpPmLdpEntityCreateNhrLdb_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 15, 1, 2, 1, 26),
    _DccrldpPmLdpEntityCreateNhrLdb_Type()
)
dccrldpPmLdpEntityCreateNhrLdb.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dccrldpPmLdpEntityCreateNhrLdb.setStatus("current")


class _DccrldpPmLdpEntityCreatePsiJoin_Type(TruthValue):
    """Custom type dccrldpPmLdpEntityCreatePsiJoin based on TruthValue"""
    defaultValue = 2


_DccrldpPmLdpEntityCreatePsiJoin_Type.__name__ = "TruthValue"
_DccrldpPmLdpEntityCreatePsiJoin_Object = MibTableColumn
dccrldpPmLdpEntityCreatePsiJoin = _DccrldpPmLdpEntityCreatePsiJoin_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 15, 1, 2, 1, 27),
    _DccrldpPmLdpEntityCreatePsiJoin_Type()
)
dccrldpPmLdpEntityCreatePsiJoin.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dccrldpPmLdpEntityCreatePsiJoin.setStatus("current")


class _DccrldpPmRedundancySwitchIntvl_Type(Integer32):
    """Custom type dccrldpPmRedundancySwitchIntvl based on Integer32"""
    defaultValue = 20000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_DccrldpPmRedundancySwitchIntvl_Type.__name__ = "Integer32"
_DccrldpPmRedundancySwitchIntvl_Object = MibTableColumn
dccrldpPmRedundancySwitchIntvl = _DccrldpPmRedundancySwitchIntvl_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 15, 1, 2, 1, 28),
    _DccrldpPmRedundancySwitchIntvl_Type()
)
dccrldpPmRedundancySwitchIntvl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dccrldpPmRedundancySwitchIntvl.setStatus("current")
if mibBuilder.loadTexts:
    dccrldpPmRedundancySwitchIntvl.setUnits("milliseconds")


class _DccrldpPmLabelWithdrawDelay_Type(Integer32):
    """Custom type dccrldpPmLabelWithdrawDelay based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000),
    )


_DccrldpPmLabelWithdrawDelay_Type.__name__ = "Integer32"
_DccrldpPmLabelWithdrawDelay_Object = MibTableColumn
dccrldpPmLabelWithdrawDelay = _DccrldpPmLabelWithdrawDelay_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 15, 1, 2, 1, 29),
    _DccrldpPmLabelWithdrawDelay_Type()
)
dccrldpPmLabelWithdrawDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dccrldpPmLabelWithdrawDelay.setStatus("current")
if mibBuilder.loadTexts:
    dccrldpPmLabelWithdrawDelay.setUnits("seconds")


class _DccrldpPmImplicitXcVcFecs_Type(TruthValue):
    """Custom type dccrldpPmImplicitXcVcFecs based on TruthValue"""
    defaultValue = 2


_DccrldpPmImplicitXcVcFecs_Type.__name__ = "TruthValue"
_DccrldpPmImplicitXcVcFecs_Object = MibTableColumn
dccrldpPmImplicitXcVcFecs = _DccrldpPmImplicitXcVcFecs_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 15, 1, 2, 1, 30),
    _DccrldpPmImplicitXcVcFecs_Type()
)
dccrldpPmImplicitXcVcFecs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dccrldpPmImplicitXcVcFecs.setStatus("current")


class _DccrldpPmWthdrwDownstreamLbl_Type(TruthValue):
    """Custom type dccrldpPmWthdrwDownstreamLbl based on TruthValue"""
    defaultValue = 2


_DccrldpPmWthdrwDownstreamLbl_Type.__name__ = "TruthValue"
_DccrldpPmWthdrwDownstreamLbl_Object = MibTableColumn
dccrldpPmWthdrwDownstreamLbl = _DccrldpPmWthdrwDownstreamLbl_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 15, 1, 2, 1, 31),
    _DccrldpPmWthdrwDownstreamLbl_Type()
)
dccrldpPmWthdrwDownstreamLbl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dccrldpPmWthdrwDownstreamLbl.setStatus("current")


class _DccrldpPmIngressReleaseDelay_Type(TruthValue):
    """Custom type dccrldpPmIngressReleaseDelay based on TruthValue"""
    defaultValue = 2


_DccrldpPmIngressReleaseDelay_Type.__name__ = "TruthValue"
_DccrldpPmIngressReleaseDelay_Object = MibTableColumn
dccrldpPmIngressReleaseDelay = _DccrldpPmIngressReleaseDelay_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 15, 1, 2, 1, 32),
    _DccrldpPmIngressReleaseDelay_Type()
)
dccrldpPmIngressReleaseDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dccrldpPmIngressReleaseDelay.setStatus("current")


class _DccrldpPmPwFastUpstreamRelease_Type(TruthValue):
    """Custom type dccrldpPmPwFastUpstreamRelease based on TruthValue"""
    defaultValue = 2


_DccrldpPmPwFastUpstreamRelease_Type.__name__ = "TruthValue"
_DccrldpPmPwFastUpstreamRelease_Object = MibTableColumn
dccrldpPmPwFastUpstreamRelease = _DccrldpPmPwFastUpstreamRelease_Object(
    (1, 3, 6, 1, 4, 1, 629, 10, 15, 1, 2, 1, 33),
    _DccrldpPmPwFastUpstreamRelease_Type()
)
dccrldpPmPwFastUpstreamRelease.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dccrldpPmPwFastUpstreamRelease.setStatus("current")
_DccrldpConformance_ObjectIdentity = ObjectIdentity
dccrldpConformance = _DccrldpConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 10, 15, 2)
)
_DccrldpCompliances_ObjectIdentity = ObjectIdentity
dccrldpCompliances = _DccrldpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 10, 15, 2, 1)
)
_DccrldpGroups_ObjectIdentity = ObjectIdentity
dccrldpGroups = _DccrldpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 10, 15, 2, 2)
)

# Managed Objects groups

dccrldpMandatoryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 629, 10, 15, 2, 2, 2)
)
dccrldpMandatoryGroup.setObjects(
      *(("DC-CR-LDP-MIB", "dccrldpSigPathManagerIndex"),
        ("DC-CR-LDP-MIB", "dccrldpSigLsrIndex"),
        ("DC-CR-LDP-MIB", "dccrldpSigSocketIfIndex"),
        ("DC-CR-LDP-MIB", "dccrldpSigRowStatus"),
        ("DC-CR-LDP-MIB", "dccrldpPmLsrIndex"),
        ("DC-CR-LDP-MIB", "dccrldpPmRowStatus"))
)
if mibBuilder.loadTexts:
    dccrldpMandatoryGroup.setStatus("current")

dccrldpOptionalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 629, 10, 15, 2, 2, 3)
)
dccrldpOptionalGroup.setObjects(
      *(("DC-CR-LDP-MIB", "dccrldpSigSessionBufPoolSize"),
        ("DC-CR-LDP-MIB", "dccrldpSigEMBufPoolSize"),
        ("DC-CR-LDP-MIB", "dccrldpSigAMBufPoolSize"),
        ("DC-CR-LDP-MIB", "dccrldpSigAdminStatus"),
        ("DC-CR-LDP-MIB", "dccrldpSigOperStatus"),
        ("DC-CR-LDP-MIB", "dccrldpSigRowStatus"),
        ("DC-CR-LDP-MIB", "dccrldpSigUseI3Interface"),
        ("DC-CR-LDP-MIB", "dccrldpSigConformanceFlags"),
        ("DC-CR-LDP-MIB", "dccrldpSigUseIPv6Transport"),
        ("DC-CR-LDP-MIB", "dccrldpSigSessStatusTrapEnable"),
        ("DC-CR-LDP-MIB", "dccrldpSigSessThreshTrapEnable"),
        ("DC-CR-LDP-MIB", "dccrldpSigPathVecLimitTrapEnable"),
        ("DC-CR-LDP-MIB", "dccrldpSigBfdProviderIndex"),
        ("DC-CR-LDP-MIB", "dccrldpPmLdpEntityAutoCreate"),
        ("DC-CR-LDP-MIB", "dccrldpPmLdpEntityAutoStart"),
        ("DC-CR-LDP-MIB", "dccrldpPmLdpEntityReuse"),
        ("DC-CR-LDP-MIB", "dccrldpPmLdpVersion"),
        ("DC-CR-LDP-MIB", "dccrldpPmUseLdpFt"),
        ("DC-CR-LDP-MIB", "dccrldpPmAsNumber"),
        ("DC-CR-LDP-MIB", "dccrldpPmIprBufPoolSize"),
        ("DC-CR-LDP-MIB", "dccrldpPmLdpSupported"),
        ("DC-CR-LDP-MIB", "dccrldpPmCrLdpSupported"),
        ("DC-CR-LDP-MIB", "dccrldpPmQueryFECSupported"),
        ("DC-CR-LDP-MIB", "dccrldpPmAdminStatus"),
        ("DC-CR-LDP-MIB", "dccrldpPmOperStatus"),
        ("DC-CR-LDP-MIB", "dccrldpPmRowStatus"),
        ("DC-CR-LDP-MIB", "dccrldpPmRestartCapable"),
        ("DC-CR-LDP-MIB", "dccrldpPmReconnectTime"),
        ("DC-CR-LDP-MIB", "dccrldpPmRecoveryTime"),
        ("DC-CR-LDP-MIB", "dccrldpPmMaxPeerReconnect"),
        ("DC-CR-LDP-MIB", "dccrldpPmMaxPeerRecovery"),
        ("DC-CR-LDP-MIB", "dccrldpPmAdjDwnHoldTime"),
        ("DC-CR-LDP-MIB", "dccrldpPmOutSegProgOrder"),
        ("DC-CR-LDP-MIB", "dccrldpPmSupportIpv6"),
        ("DC-CR-LDP-MIB", "dccrldpPmPolicySupportFlags"),
        ("DC-CR-LDP-MIB", "dccrldpPmCheckOutSegIntfaceStat"),
        ("DC-CR-LDP-MIB", "dccrldpPmLdpEntityCreateNhrLdb"),
        ("DC-CR-LDP-MIB", "dccrldpPmLdpEntityCreatePsiJoin"),
        ("DC-CR-LDP-MIB", "dccrldpPmRedundancySwitchIntvl"),
        ("DC-CR-LDP-MIB", "dccrldpPmLabelWithdrawDelay"),
        ("DC-CR-LDP-MIB", "dccrldpPmImplicitXcVcFecs"),
        ("DC-CR-LDP-MIB", "dccrldpPmWthdrwDownstreamLbl"),
        ("DC-CR-LDP-MIB", "dccrldpPmIngressReleaseDelay"),
        ("DC-CR-LDP-MIB", "dccrldpPmPwFastUpstreamRelease"))
)
if mibBuilder.loadTexts:
    dccrldpOptionalGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

dccrldpMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 629, 10, 15, 2, 1, 1)
)
dccrldpMibCompliance.setObjects(
      *(("DC-CR-LDP-MIB", "dccrldpMandatoryGroup"),
        ("DC-CR-LDP-MIB", "dccrldpOptionalGroup"))
)
if mibBuilder.loadTexts:
    dccrldpMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DC-CR-LDP-MIB",
    **{"DcCrldpAdminStatus": DcCrldpAdminStatus,
       "DcCrldpOperStatus": DcCrldpOperStatus,
       "DcCrldpIndex": DcCrldpIndex,
       "nbase": nbase,
       "opx": opx,
       "dccrldp": dccrldp,
       "dccrldpObjects": dccrldpObjects,
       "dccrldpSigTable": dccrldpSigTable,
       "dccrldpSigEntry": dccrldpSigEntry,
       "dccrldpSigIndex": dccrldpSigIndex,
       "dccrldpSigPathManagerIndex": dccrldpSigPathManagerIndex,
       "dccrldpSigLsrIndex": dccrldpSigLsrIndex,
       "dccrldpSigSocketIfIndex": dccrldpSigSocketIfIndex,
       "dccrldpSigSessionBufPoolSize": dccrldpSigSessionBufPoolSize,
       "dccrldpSigEMBufPoolSize": dccrldpSigEMBufPoolSize,
       "dccrldpSigAMBufPoolSize": dccrldpSigAMBufPoolSize,
       "dccrldpSigAdminStatus": dccrldpSigAdminStatus,
       "dccrldpSigOperStatus": dccrldpSigOperStatus,
       "dccrldpSigRowStatus": dccrldpSigRowStatus,
       "dccrldpSigUseI3Interface": dccrldpSigUseI3Interface,
       "dccrldpSigConformanceFlags": dccrldpSigConformanceFlags,
       "dccrldpSigUseIPv6Transport": dccrldpSigUseIPv6Transport,
       "dccrldpSigSessStatusTrapEnable": dccrldpSigSessStatusTrapEnable,
       "dccrldpSigSessThreshTrapEnable": dccrldpSigSessThreshTrapEnable,
       "dccrldpSigPathVecLimitTrapEnable": dccrldpSigPathVecLimitTrapEnable,
       "dccrldpSigBfdProviderIndex": dccrldpSigBfdProviderIndex,
       "dccrldpPmTable": dccrldpPmTable,
       "dccrldpPmEntry": dccrldpPmEntry,
       "dccrldpPmIndex": dccrldpPmIndex,
       "dccrldpPmLsrIndex": dccrldpPmLsrIndex,
       "dccrldpPmLdpEntityAutoCreate": dccrldpPmLdpEntityAutoCreate,
       "dccrldpPmLdpEntityAutoStart": dccrldpPmLdpEntityAutoStart,
       "dccrldpPmLdpEntityReuse": dccrldpPmLdpEntityReuse,
       "dccrldpPmLdpVersion": dccrldpPmLdpVersion,
       "dccrldpPmUseLdpFt": dccrldpPmUseLdpFt,
       "dccrldpPmAsNumber": dccrldpPmAsNumber,
       "dccrldpPmIprBufPoolSize": dccrldpPmIprBufPoolSize,
       "dccrldpPmLdpSupported": dccrldpPmLdpSupported,
       "dccrldpPmCrLdpSupported": dccrldpPmCrLdpSupported,
       "dccrldpPmQueryFECSupported": dccrldpPmQueryFECSupported,
       "dccrldpPmAdminStatus": dccrldpPmAdminStatus,
       "dccrldpPmOperStatus": dccrldpPmOperStatus,
       "dccrldpPmRowStatus": dccrldpPmRowStatus,
       "dccrldpPmRestartCapable": dccrldpPmRestartCapable,
       "dccrldpPmReconnectTime": dccrldpPmReconnectTime,
       "dccrldpPmRecoveryTime": dccrldpPmRecoveryTime,
       "dccrldpPmMaxPeerReconnect": dccrldpPmMaxPeerReconnect,
       "dccrldpPmMaxPeerRecovery": dccrldpPmMaxPeerRecovery,
       "dccrldpPmAdjDwnHoldTime": dccrldpPmAdjDwnHoldTime,
       "dccrldpPmOutSegProgOrder": dccrldpPmOutSegProgOrder,
       "dccrldpPmSupportIpv6": dccrldpPmSupportIpv6,
       "dccrldpPmPolicySupportFlags": dccrldpPmPolicySupportFlags,
       "dccrldpPmCheckOutSegIntfaceStat": dccrldpPmCheckOutSegIntfaceStat,
       "dccrldpPmLdpEntityCreateNhrLdb": dccrldpPmLdpEntityCreateNhrLdb,
       "dccrldpPmLdpEntityCreatePsiJoin": dccrldpPmLdpEntityCreatePsiJoin,
       "dccrldpPmRedundancySwitchIntvl": dccrldpPmRedundancySwitchIntvl,
       "dccrldpPmLabelWithdrawDelay": dccrldpPmLabelWithdrawDelay,
       "dccrldpPmImplicitXcVcFecs": dccrldpPmImplicitXcVcFecs,
       "dccrldpPmWthdrwDownstreamLbl": dccrldpPmWthdrwDownstreamLbl,
       "dccrldpPmIngressReleaseDelay": dccrldpPmIngressReleaseDelay,
       "dccrldpPmPwFastUpstreamRelease": dccrldpPmPwFastUpstreamRelease,
       "dccrldpConformance": dccrldpConformance,
       "dccrldpCompliances": dccrldpCompliances,
       "dccrldpMibCompliance": dccrldpMibCompliance,
       "dccrldpGroups": dccrldpGroups,
       "dccrldpMandatoryGroup": dccrldpMandatoryGroup,
       "dccrldpOptionalGroup": dccrldpOptionalGroup}
)
