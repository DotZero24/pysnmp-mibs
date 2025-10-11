# SNMP MIB module (ADTRAN-GENNTP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/adtran/ADTRAN-GENNTP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:33:38 2025
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

(adGenNtp,
 adGenNtpCompliance,
 adGenNtpID) = mibBuilder.importSymbols(
    "ADTRAN-SHARED-CND-SYSTEM-MIB",
    "adGenNtp",
    "adGenNtpCompliance",
    "adGenNtpID")

(InetAddress,) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress")

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

adGenNtpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 70, 5, 1)
)
if mibBuilder.loadTexts:
    adGenNtpMIB.setRevisions(
        ("2014-06-02 00:00",
         "2008-09-17 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AdGenNtpMIBObjects_ObjectIdentity = ObjectIdentity
adGenNtpMIBObjects = _AdGenNtpMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 5, 1)
)
_AdGenNtpEntStatus_ObjectIdentity = ObjectIdentity
adGenNtpEntStatus = _AdGenNtpEntStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 5, 1, 1)
)


class _AdGenNtpEntStatusCurrentMode_Type(DisplayString):
    """Custom type adGenNtpEntStatusCurrentMode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AdGenNtpEntStatusCurrentMode_Type.__name__ = "DisplayString"
_AdGenNtpEntStatusCurrentMode_Object = MibScalar
adGenNtpEntStatusCurrentMode = _AdGenNtpEntStatusCurrentMode_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 5, 1, 1, 1),
    _AdGenNtpEntStatusCurrentMode_Type()
)
adGenNtpEntStatusCurrentMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenNtpEntStatusCurrentMode.setStatus("current")


class _AdGenNtpEntStatusCurrentModeVal_Type(Integer32):
    """Custom type adGenNtpEntStatusCurrentModeVal based on Integer32"""
    defaultValue = 99

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              99)
        )
    )
    namedValues = NamedValues(
        *(("notRunning", 1),
          ("notSynchronized", 2),
          ("noneConfigured", 3),
          ("syncToLocal", 4),
          ("syncToRefclock", 5),
          ("syncToRemoteServer", 6),
          ("unknown", 99))
    )


_AdGenNtpEntStatusCurrentModeVal_Type.__name__ = "Integer32"
_AdGenNtpEntStatusCurrentModeVal_Object = MibScalar
adGenNtpEntStatusCurrentModeVal = _AdGenNtpEntStatusCurrentModeVal_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 5, 1, 1, 2),
    _AdGenNtpEntStatusCurrentModeVal_Type()
)
adGenNtpEntStatusCurrentModeVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenNtpEntStatusCurrentModeVal.setStatus("current")


class _AdGenNtpEntStatusStratum_Type(Integer32):
    """Custom type adGenNtpEntStatusStratum based on Integer32"""
    defaultValue = 16

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_AdGenNtpEntStatusStratum_Type.__name__ = "Integer32"
_AdGenNtpEntStatusStratum_Object = MibScalar
adGenNtpEntStatusStratum = _AdGenNtpEntStatusStratum_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 5, 1, 1, 3),
    _AdGenNtpEntStatusStratum_Type()
)
adGenNtpEntStatusStratum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenNtpEntStatusStratum.setStatus("current")


class _AdGenNtpEntStatusActiveRefSourceId_Type(Integer32):
    """Custom type adGenNtpEntStatusActiveRefSourceId based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99999),
    )


_AdGenNtpEntStatusActiveRefSourceId_Type.__name__ = "Integer32"
_AdGenNtpEntStatusActiveRefSourceId_Object = MibScalar
adGenNtpEntStatusActiveRefSourceId = _AdGenNtpEntStatusActiveRefSourceId_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 5, 1, 1, 4),
    _AdGenNtpEntStatusActiveRefSourceId_Type()
)
adGenNtpEntStatusActiveRefSourceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenNtpEntStatusActiveRefSourceId.setStatus("current")


class _AdGenNtpEntStatusActiveRefSourceName_Type(DisplayString):
    """Custom type adGenNtpEntStatusActiveRefSourceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_AdGenNtpEntStatusActiveRefSourceName_Type.__name__ = "DisplayString"
_AdGenNtpEntStatusActiveRefSourceName_Object = MibScalar
adGenNtpEntStatusActiveRefSourceName = _AdGenNtpEntStatusActiveRefSourceName_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 5, 1, 1, 5),
    _AdGenNtpEntStatusActiveRefSourceName_Type()
)
adGenNtpEntStatusActiveRefSourceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenNtpEntStatusActiveRefSourceName.setStatus("current")


class _AdGenNtpEntStatusActiveOffset_Type(DisplayString):
    """Custom type adGenNtpEntStatusActiveOffset based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 7),
    )


_AdGenNtpEntStatusActiveOffset_Type.__name__ = "DisplayString"
_AdGenNtpEntStatusActiveOffset_Object = MibScalar
adGenNtpEntStatusActiveOffset = _AdGenNtpEntStatusActiveOffset_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 5, 1, 1, 6),
    _AdGenNtpEntStatusActiveOffset_Type()
)
adGenNtpEntStatusActiveOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenNtpEntStatusActiveOffset.setStatus("current")


class _AdGenNtpEntStatusNumberOfRefSources_Type(Integer32):
    """Custom type adGenNtpEntStatusNumberOfRefSources based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_AdGenNtpEntStatusNumberOfRefSources_Type.__name__ = "Integer32"
_AdGenNtpEntStatusNumberOfRefSources_Object = MibScalar
adGenNtpEntStatusNumberOfRefSources = _AdGenNtpEntStatusNumberOfRefSources_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 5, 1, 1, 7),
    _AdGenNtpEntStatusNumberOfRefSources_Type()
)
adGenNtpEntStatusNumberOfRefSources.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenNtpEntStatusNumberOfRefSources.setStatus("current")


class _AdGenNtpEntStatusDispersion_Type(DisplayString):
    """Custom type adGenNtpEntStatusDispersion based on DisplayString"""
    defaultValue = OctetString("n/a")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 7),
    )


_AdGenNtpEntStatusDispersion_Type.__name__ = "DisplayString"
_AdGenNtpEntStatusDispersion_Object = MibScalar
adGenNtpEntStatusDispersion = _AdGenNtpEntStatusDispersion_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 5, 1, 1, 8),
    _AdGenNtpEntStatusDispersion_Type()
)
adGenNtpEntStatusDispersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenNtpEntStatusDispersion.setStatus("current")


class _AdGenNtpEntStatusEntityUptime_Type(Unsigned32):
    """Custom type adGenNtpEntStatusEntityUptime based on Unsigned32"""
    defaultValue = 0


_AdGenNtpEntStatusEntityUptime_Type.__name__ = "Unsigned32"
_AdGenNtpEntStatusEntityUptime_Object = MibScalar
adGenNtpEntStatusEntityUptime = _AdGenNtpEntStatusEntityUptime_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 5, 1, 1, 9),
    _AdGenNtpEntStatusEntityUptime_Type()
)
adGenNtpEntStatusEntityUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenNtpEntStatusEntityUptime.setStatus("current")


class _AdGenNtpEntStatusReferenceNtpTime_Type(DisplayString):
    """Custom type adGenNtpEntStatusReferenceNtpTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AdGenNtpEntStatusReferenceNtpTime_Type.__name__ = "DisplayString"
_AdGenNtpEntStatusReferenceNtpTime_Object = MibScalar
adGenNtpEntStatusReferenceNtpTime = _AdGenNtpEntStatusReferenceNtpTime_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 5, 1, 1, 10),
    _AdGenNtpEntStatusReferenceNtpTime_Type()
)
adGenNtpEntStatusReferenceNtpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenNtpEntStatusReferenceNtpTime.setStatus("current")


class _AdGenNtpEntStatusLeapSecond_Type(Integer32):
    """Custom type adGenNtpEntStatusLeapSecond based on Integer32"""
    defaultValue = 0


_AdGenNtpEntStatusLeapSecond_Type.__name__ = "Integer32"
_AdGenNtpEntStatusLeapSecond_Object = MibScalar
adGenNtpEntStatusLeapSecond = _AdGenNtpEntStatusLeapSecond_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 5, 1, 1, 11),
    _AdGenNtpEntStatusLeapSecond_Type()
)
adGenNtpEntStatusLeapSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenNtpEntStatusLeapSecond.setStatus("current")


class _AdGenNtpEntStatusLeapSecDirection_Type(Integer32):
    """Custom type adGenNtpEntStatusLeapSecDirection based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 1),
    )


_AdGenNtpEntStatusLeapSecDirection_Type.__name__ = "Integer32"
_AdGenNtpEntStatusLeapSecDirection_Object = MibScalar
adGenNtpEntStatusLeapSecDirection = _AdGenNtpEntStatusLeapSecDirection_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 5, 1, 1, 12),
    _AdGenNtpEntStatusLeapSecDirection_Type()
)
adGenNtpEntStatusLeapSecDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenNtpEntStatusLeapSecDirection.setStatus("current")
_AdGenNtpEntStatusInPkts_Type = Counter32
_AdGenNtpEntStatusInPkts_Object = MibScalar
adGenNtpEntStatusInPkts = _AdGenNtpEntStatusInPkts_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 5, 1, 1, 13),
    _AdGenNtpEntStatusInPkts_Type()
)
adGenNtpEntStatusInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenNtpEntStatusInPkts.setStatus("current")
_AdGenNtpEntStatusOutPkts_Type = Counter32
_AdGenNtpEntStatusOutPkts_Object = MibScalar
adGenNtpEntStatusOutPkts = _AdGenNtpEntStatusOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 5, 1, 1, 14),
    _AdGenNtpEntStatusOutPkts_Type()
)
adGenNtpEntStatusOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenNtpEntStatusOutPkts.setStatus("current")


class _AdGenNtpEntStatusMaxNumberOfRefSources_Type(Integer32):
    """Custom type adGenNtpEntStatusMaxNumberOfRefSources based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_AdGenNtpEntStatusMaxNumberOfRefSources_Type.__name__ = "Integer32"
_AdGenNtpEntStatusMaxNumberOfRefSources_Object = MibScalar
adGenNtpEntStatusMaxNumberOfRefSources = _AdGenNtpEntStatusMaxNumberOfRefSources_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 5, 1, 1, 15),
    _AdGenNtpEntStatusMaxNumberOfRefSources_Type()
)
adGenNtpEntStatusMaxNumberOfRefSources.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenNtpEntStatusMaxNumberOfRefSources.setStatus("current")


class _AdGenNtpEntStatusReferenceDateTime_Type(DisplayString):
    """Custom type adGenNtpEntStatusReferenceDateTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AdGenNtpEntStatusReferenceDateTime_Type.__name__ = "DisplayString"
_AdGenNtpEntStatusReferenceDateTime_Object = MibScalar
adGenNtpEntStatusReferenceDateTime = _AdGenNtpEntStatusReferenceDateTime_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 5, 1, 1, 16),
    _AdGenNtpEntStatusReferenceDateTime_Type()
)
adGenNtpEntStatusReferenceDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenNtpEntStatusReferenceDateTime.setStatus("current")
_AdGenNtpAssociation_ObjectIdentity = ObjectIdentity
adGenNtpAssociation = _AdGenNtpAssociation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 5, 1, 2)
)
_AdGenNtpAssociationTable_Object = MibTable
adGenNtpAssociationTable = _AdGenNtpAssociationTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 5, 1, 2, 1)
)
if mibBuilder.loadTexts:
    adGenNtpAssociationTable.setStatus("current")
_AdGenNtpAssociationEntry_Object = MibTableRow
adGenNtpAssociationEntry = _AdGenNtpAssociationEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 5, 1, 2, 1, 1)
)
adGenNtpAssociationEntry.setIndexNames(
    (0, "ADTRAN-GENNTP-MIB", "adGenNtpAssocAddress"),
)
if mibBuilder.loadTexts:
    adGenNtpAssociationEntry.setStatus("current")
_AdGenNtpAssocRowStatus_Type = RowStatus
_AdGenNtpAssocRowStatus_Object = MibTableColumn
adGenNtpAssocRowStatus = _AdGenNtpAssocRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 5, 1, 2, 1, 1, 1),
    _AdGenNtpAssocRowStatus_Type()
)
adGenNtpAssocRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenNtpAssocRowStatus.setStatus("current")
_AdGenNtpAssocAddress_Type = InetAddress
_AdGenNtpAssocAddress_Object = MibTableColumn
adGenNtpAssocAddress = _AdGenNtpAssocAddress_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 5, 1, 2, 1, 1, 2),
    _AdGenNtpAssocAddress_Type()
)
adGenNtpAssocAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adGenNtpAssocAddress.setStatus("current")


class _AdGenNtpAssocVersion_Type(Integer32):
    """Custom type adGenNtpAssocVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 4),
    )


_AdGenNtpAssocVersion_Type.__name__ = "Integer32"
_AdGenNtpAssocVersion_Object = MibTableColumn
adGenNtpAssocVersion = _AdGenNtpAssocVersion_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 5, 1, 2, 1, 1, 3),
    _AdGenNtpAssocVersion_Type()
)
adGenNtpAssocVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenNtpAssocVersion.setStatus("current")
_AdGenNtpAssocPrefer_Type = TruthValue
_AdGenNtpAssocPrefer_Object = MibTableColumn
adGenNtpAssocPrefer = _AdGenNtpAssocPrefer_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 5, 1, 2, 1, 1, 4),
    _AdGenNtpAssocPrefer_Type()
)
adGenNtpAssocPrefer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenNtpAssocPrefer.setStatus("current")


class _AdGenNtpAssocRefId_Type(DisplayString):
    """Custom type adGenNtpAssocRefId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_AdGenNtpAssocRefId_Type.__name__ = "DisplayString"
_AdGenNtpAssocRefId_Object = MibTableColumn
adGenNtpAssocRefId = _AdGenNtpAssocRefId_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 5, 1, 2, 1, 1, 5),
    _AdGenNtpAssocRefId_Type()
)
adGenNtpAssocRefId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenNtpAssocRefId.setStatus("current")


class _AdGenNtpAssocOffset_Type(DisplayString):
    """Custom type adGenNtpAssocOffset based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 7),
    )


_AdGenNtpAssocOffset_Type.__name__ = "DisplayString"
_AdGenNtpAssocOffset_Object = MibTableColumn
adGenNtpAssocOffset = _AdGenNtpAssocOffset_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 5, 1, 2, 1, 1, 6),
    _AdGenNtpAssocOffset_Type()
)
adGenNtpAssocOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenNtpAssocOffset.setStatus("current")


class _AdGenNtpAssocStratum_Type(Integer32):
    """Custom type adGenNtpAssocStratum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_AdGenNtpAssocStratum_Type.__name__ = "Integer32"
_AdGenNtpAssocStratum_Object = MibTableColumn
adGenNtpAssocStratum = _AdGenNtpAssocStratum_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 5, 1, 2, 1, 1, 7),
    _AdGenNtpAssocStratum_Type()
)
adGenNtpAssocStratum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenNtpAssocStratum.setStatus("current")


class _AdGenNtpAssocStatusJitter_Type(DisplayString):
    """Custom type adGenNtpAssocStatusJitter based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 7),
    )


_AdGenNtpAssocStatusJitter_Type.__name__ = "DisplayString"
_AdGenNtpAssocStatusJitter_Object = MibTableColumn
adGenNtpAssocStatusJitter = _AdGenNtpAssocStatusJitter_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 5, 1, 2, 1, 1, 8),
    _AdGenNtpAssocStatusJitter_Type()
)
adGenNtpAssocStatusJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenNtpAssocStatusJitter.setStatus("current")


class _AdGenNtpAssocStatusDelay_Type(DisplayString):
    """Custom type adGenNtpAssocStatusDelay based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 7),
    )


_AdGenNtpAssocStatusDelay_Type.__name__ = "DisplayString"
_AdGenNtpAssocStatusDelay_Object = MibTableColumn
adGenNtpAssocStatusDelay = _AdGenNtpAssocStatusDelay_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 5, 1, 2, 1, 1, 9),
    _AdGenNtpAssocStatusDelay_Type()
)
adGenNtpAssocStatusDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenNtpAssocStatusDelay.setStatus("current")


class _AdGenNtpAssocStatusDispersion_Type(DisplayString):
    """Custom type adGenNtpAssocStatusDispersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 7),
    )


_AdGenNtpAssocStatusDispersion_Type.__name__ = "DisplayString"
_AdGenNtpAssocStatusDispersion_Object = MibTableColumn
adGenNtpAssocStatusDispersion = _AdGenNtpAssocStatusDispersion_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 5, 1, 2, 1, 1, 10),
    _AdGenNtpAssocStatusDispersion_Type()
)
adGenNtpAssocStatusDispersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenNtpAssocStatusDispersion.setStatus("current")
_AdGenNtpAssociationScalars_ObjectIdentity = ObjectIdentity
adGenNtpAssociationScalars = _AdGenNtpAssociationScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 5, 1, 2, 2)
)
_AdGenNtpAssociationBroadcast_Type = TruthValue
_AdGenNtpAssociationBroadcast_Object = MibScalar
adGenNtpAssociationBroadcast = _AdGenNtpAssociationBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 5, 1, 2, 2, 1),
    _AdGenNtpAssociationBroadcast_Type()
)
adGenNtpAssociationBroadcast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenNtpAssociationBroadcast.setStatus("current")
_AdGenNtpAssociationPeriodicVolley_Type = Unsigned32
_AdGenNtpAssociationPeriodicVolley_Object = MibScalar
adGenNtpAssociationPeriodicVolley = _AdGenNtpAssociationPeriodicVolley_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 5, 1, 2, 2, 2),
    _AdGenNtpAssociationPeriodicVolley_Type()
)
adGenNtpAssociationPeriodicVolley.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenNtpAssociationPeriodicVolley.setStatus("current")
_AdGenNtpEntConformance_ObjectIdentity = ObjectIdentity
adGenNtpEntConformance = _AdGenNtpEntConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 99, 10000, 70, 5, 1)
)
_AdGenNtpEntCompliances_ObjectIdentity = ObjectIdentity
adGenNtpEntCompliances = _AdGenNtpEntCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 99, 10000, 70, 5, 1, 1)
)
_AdGenNtpEntGroups_ObjectIdentity = ObjectIdentity
adGenNtpEntGroups = _AdGenNtpEntGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 99, 10000, 70, 5, 1, 2)
)

# Managed Objects groups

adGenNtpEntObjectsGroup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 664, 99, 10000, 70, 5, 1, 2, 1)
)
adGenNtpEntObjectsGroup1.setObjects(
      *(("ADTRAN-GENNTP-MIB", "adGenNtpEntStatusEntityUptime"),
        ("ADTRAN-GENNTP-MIB", "adGenNtpAssocRowStatus"),
        ("ADTRAN-GENNTP-MIB", "adGenNtpAssocVersion"),
        ("ADTRAN-GENNTP-MIB", "adGenNtpAssocPrefer"))
)
if mibBuilder.loadTexts:
    adGenNtpEntObjectsGroup1.setStatus("current")

adGenNtpEntObjectsGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 664, 99, 10000, 70, 5, 1, 2, 2)
)
adGenNtpEntObjectsGroup2.setObjects(
      *(("ADTRAN-GENNTP-MIB", "adGenNtpEntStatusStratum"),
        ("ADTRAN-GENNTP-MIB", "adGenNtpEntStatusActiveRefSourceId"),
        ("ADTRAN-GENNTP-MIB", "adGenNtpEntStatusActiveRefSourceName"),
        ("ADTRAN-GENNTP-MIB", "adGenNtpEntStatusActiveOffset"),
        ("ADTRAN-GENNTP-MIB", "adGenNtpEntStatusNumberOfRefSources"),
        ("ADTRAN-GENNTP-MIB", "adGenNtpEntStatusDispersion"),
        ("ADTRAN-GENNTP-MIB", "adGenNtpEntStatusLeapSecond"),
        ("ADTRAN-GENNTP-MIB", "adGenNtpEntStatusLeapSecDirection"),
        ("ADTRAN-GENNTP-MIB", "adGenNtpEntStatusInPkts"),
        ("ADTRAN-GENNTP-MIB", "adGenNtpEntStatusOutPkts"),
        ("ADTRAN-GENNTP-MIB", "adGenNtpEntStatusMaxNumberOfRefSources"),
        ("ADTRAN-GENNTP-MIB", "adGenNtpEntStatusReferenceDateTime"),
        ("ADTRAN-GENNTP-MIB", "adGenNtpAssocOffset"),
        ("ADTRAN-GENNTP-MIB", "adGenNtpAssocStratum"),
        ("ADTRAN-GENNTP-MIB", "adGenNtpAssocStatusJitter"),
        ("ADTRAN-GENNTP-MIB", "adGenNtpAssocStatusDelay"),
        ("ADTRAN-GENNTP-MIB", "adGenNtpAssocStatusDispersion"))
)
if mibBuilder.loadTexts:
    adGenNtpEntObjectsGroup2.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

adGenNtpEntNTPCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 664, 99, 10000, 70, 5, 1, 1, 1)
)
adGenNtpEntNTPCompliance.setObjects(
      *(("ADTRAN-GENNTP-MIB", "adGenNtpEntObjectsGroup1"),
        ("ADTRAN-GENNTP-MIB", "adGenNtpEntObjectsGroup2"))
)
if mibBuilder.loadTexts:
    adGenNtpEntNTPCompliance.setStatus(
        "current"
    )

adGenNtpEntSNTPCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 664, 99, 10000, 70, 5, 1, 1, 2)
)
adGenNtpEntSNTPCompliance.setObjects(
    ("ADTRAN-GENNTP-MIB", "adGenNtpEntObjectsGroup1")
)
if mibBuilder.loadTexts:
    adGenNtpEntSNTPCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ADTRAN-GENNTP-MIB",
    **{"adGenNtpMIBObjects": adGenNtpMIBObjects,
       "adGenNtpEntStatus": adGenNtpEntStatus,
       "adGenNtpEntStatusCurrentMode": adGenNtpEntStatusCurrentMode,
       "adGenNtpEntStatusCurrentModeVal": adGenNtpEntStatusCurrentModeVal,
       "adGenNtpEntStatusStratum": adGenNtpEntStatusStratum,
       "adGenNtpEntStatusActiveRefSourceId": adGenNtpEntStatusActiveRefSourceId,
       "adGenNtpEntStatusActiveRefSourceName": adGenNtpEntStatusActiveRefSourceName,
       "adGenNtpEntStatusActiveOffset": adGenNtpEntStatusActiveOffset,
       "adGenNtpEntStatusNumberOfRefSources": adGenNtpEntStatusNumberOfRefSources,
       "adGenNtpEntStatusDispersion": adGenNtpEntStatusDispersion,
       "adGenNtpEntStatusEntityUptime": adGenNtpEntStatusEntityUptime,
       "adGenNtpEntStatusReferenceNtpTime": adGenNtpEntStatusReferenceNtpTime,
       "adGenNtpEntStatusLeapSecond": adGenNtpEntStatusLeapSecond,
       "adGenNtpEntStatusLeapSecDirection": adGenNtpEntStatusLeapSecDirection,
       "adGenNtpEntStatusInPkts": adGenNtpEntStatusInPkts,
       "adGenNtpEntStatusOutPkts": adGenNtpEntStatusOutPkts,
       "adGenNtpEntStatusMaxNumberOfRefSources": adGenNtpEntStatusMaxNumberOfRefSources,
       "adGenNtpEntStatusReferenceDateTime": adGenNtpEntStatusReferenceDateTime,
       "adGenNtpAssociation": adGenNtpAssociation,
       "adGenNtpAssociationTable": adGenNtpAssociationTable,
       "adGenNtpAssociationEntry": adGenNtpAssociationEntry,
       "adGenNtpAssocRowStatus": adGenNtpAssocRowStatus,
       "adGenNtpAssocAddress": adGenNtpAssocAddress,
       "adGenNtpAssocVersion": adGenNtpAssocVersion,
       "adGenNtpAssocPrefer": adGenNtpAssocPrefer,
       "adGenNtpAssocRefId": adGenNtpAssocRefId,
       "adGenNtpAssocOffset": adGenNtpAssocOffset,
       "adGenNtpAssocStratum": adGenNtpAssocStratum,
       "adGenNtpAssocStatusJitter": adGenNtpAssocStatusJitter,
       "adGenNtpAssocStatusDelay": adGenNtpAssocStatusDelay,
       "adGenNtpAssocStatusDispersion": adGenNtpAssocStatusDispersion,
       "adGenNtpAssociationScalars": adGenNtpAssociationScalars,
       "adGenNtpAssociationBroadcast": adGenNtpAssociationBroadcast,
       "adGenNtpAssociationPeriodicVolley": adGenNtpAssociationPeriodicVolley,
       "adGenNtpMIB": adGenNtpMIB,
       "adGenNtpEntConformance": adGenNtpEntConformance,
       "adGenNtpEntCompliances": adGenNtpEntCompliances,
       "adGenNtpEntNTPCompliance": adGenNtpEntNTPCompliance,
       "adGenNtpEntSNTPCompliance": adGenNtpEntSNTPCompliance,
       "adGenNtpEntGroups": adGenNtpEntGroups,
       "adGenNtpEntObjectsGroup1": adGenNtpEntObjectsGroup1,
       "adGenNtpEntObjectsGroup2": adGenNtpEntObjectsGroup2}
)
