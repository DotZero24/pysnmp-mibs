# SNMP MIB module (ARICENT-TAC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/aricent/ARICENT-TAC-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:44:43 2025
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

fstac = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 29601, 2, 8)
)
if mibBuilder.loadTexts:
    fstac.setRevisions(
        ("2012-09-05 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FsTacScalars_ObjectIdentity = ObjectIdentity
fsTacScalars = _FsTacScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29601, 2, 8, 1)
)


class _FsTacMcastChannelDefaultBandwidth_Type(Unsigned32):
    """Custom type fsTacMcastChannelDefaultBandwidth based on Unsigned32"""
    defaultValue = 2000


_FsTacMcastChannelDefaultBandwidth_Type.__name__ = "Unsigned32"
_FsTacMcastChannelDefaultBandwidth_Object = MibScalar
fsTacMcastChannelDefaultBandwidth = _FsTacMcastChannelDefaultBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 8, 1, 1),
    _FsTacMcastChannelDefaultBandwidth_Type()
)
fsTacMcastChannelDefaultBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsTacMcastChannelDefaultBandwidth.setStatus("current")
_FsTacTraceOption_Type = Unsigned32
_FsTacTraceOption_Object = MibScalar
fsTacTraceOption = _FsTacTraceOption_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 8, 1, 2),
    _FsTacTraceOption_Type()
)
fsTacTraceOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsTacTraceOption.setStatus("current")


class _FsTacStatus_Type(Integer32):
    """Custom type fsTacStatus based on Integer32"""
    defaultValue = 1

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


_FsTacStatus_Type.__name__ = "Integer32"
_FsTacStatus_Object = MibScalar
fsTacStatus = _FsTacStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 8, 1, 3),
    _FsTacStatus_Type()
)
fsTacStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsTacStatus.setStatus("current")
_FsTacProfile_ObjectIdentity = ObjectIdentity
fsTacProfile = _FsTacProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29601, 2, 8, 2)
)
_FsTacMcastProfileTable_Object = MibTable
fsTacMcastProfileTable = _FsTacMcastProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 8, 2, 1)
)
if mibBuilder.loadTexts:
    fsTacMcastProfileTable.setStatus("current")
_FsTacMcastProfileEntry_Object = MibTableRow
fsTacMcastProfileEntry = _FsTacMcastProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 8, 2, 1, 1)
)
fsTacMcastProfileEntry.setIndexNames(
    (0, "ARICENT-TAC-MIB", "fsTacMcastProfileId"),
    (0, "ARICENT-TAC-MIB", "fsTacMcastProfileAddrType"),
)
if mibBuilder.loadTexts:
    fsTacMcastProfileEntry.setStatus("current")


class _FsTacMcastProfileId_Type(Unsigned32):
    """Custom type fsTacMcastProfileId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_FsTacMcastProfileId_Type.__name__ = "Unsigned32"
_FsTacMcastProfileId_Object = MibTableColumn
fsTacMcastProfileId = _FsTacMcastProfileId_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 8, 2, 1, 1, 1),
    _FsTacMcastProfileId_Type()
)
fsTacMcastProfileId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsTacMcastProfileId.setStatus("current")
_FsTacMcastProfileAddrType_Type = InetAddressType
_FsTacMcastProfileAddrType_Object = MibTableColumn
fsTacMcastProfileAddrType = _FsTacMcastProfileAddrType_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 8, 2, 1, 1, 2),
    _FsTacMcastProfileAddrType_Type()
)
fsTacMcastProfileAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsTacMcastProfileAddrType.setStatus("current")


class _FsTacMcastProfileAction_Type(Integer32):
    """Custom type fsTacMcastProfileAction based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("permit", 1),
          ("deny", 2))
    )


_FsTacMcastProfileAction_Type.__name__ = "Integer32"
_FsTacMcastProfileAction_Object = MibTableColumn
fsTacMcastProfileAction = _FsTacMcastProfileAction_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 8, 2, 1, 1, 3),
    _FsTacMcastProfileAction_Type()
)
fsTacMcastProfileAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsTacMcastProfileAction.setStatus("current")


class _FsTacMcastProfileDescription_Type(DisplayString):
    """Custom type fsTacMcastProfileDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_FsTacMcastProfileDescription_Type.__name__ = "DisplayString"
_FsTacMcastProfileDescription_Object = MibTableColumn
fsTacMcastProfileDescription = _FsTacMcastProfileDescription_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 8, 2, 1, 1, 4),
    _FsTacMcastProfileDescription_Type()
)
fsTacMcastProfileDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsTacMcastProfileDescription.setStatus("current")
_FsTacMcastProfileStatus_Type = RowStatus
_FsTacMcastProfileStatus_Object = MibTableColumn
fsTacMcastProfileStatus = _FsTacMcastProfileStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 8, 2, 1, 1, 5),
    _FsTacMcastProfileStatus_Type()
)
fsTacMcastProfileStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsTacMcastProfileStatus.setStatus("current")
_FsTacMcastPrfFilterTable_Object = MibTable
fsTacMcastPrfFilterTable = _FsTacMcastPrfFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 8, 2, 2)
)
if mibBuilder.loadTexts:
    fsTacMcastPrfFilterTable.setStatus("current")
_FsTacMcastPrfFilterEntry_Object = MibTableRow
fsTacMcastPrfFilterEntry = _FsTacMcastPrfFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 8, 2, 2, 1)
)
fsTacMcastPrfFilterEntry.setIndexNames(
    (0, "ARICENT-TAC-MIB", "fsTacMcastProfileId"),
    (0, "ARICENT-TAC-MIB", "fsTacMcastProfileAddrType"),
    (0, "ARICENT-TAC-MIB", "fsTacMcastPrfFilterGrpStartAddr"),
    (0, "ARICENT-TAC-MIB", "fsTacMcastPrfFilterGrpEndAddr"),
    (0, "ARICENT-TAC-MIB", "fsTacMcastPrfFilterSrcStartAddr"),
    (0, "ARICENT-TAC-MIB", "fsTacMcastPrfFilterSrcEndAddr"),
)
if mibBuilder.loadTexts:
    fsTacMcastPrfFilterEntry.setStatus("current")


class _FsTacMcastPrfFilterGrpStartAddr_Type(InetAddress):
    """Custom type fsTacMcastPrfFilterGrpStartAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 16),
    )


_FsTacMcastPrfFilterGrpStartAddr_Type.__name__ = "InetAddress"
_FsTacMcastPrfFilterGrpStartAddr_Object = MibTableColumn
fsTacMcastPrfFilterGrpStartAddr = _FsTacMcastPrfFilterGrpStartAddr_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 8, 2, 2, 1, 1),
    _FsTacMcastPrfFilterGrpStartAddr_Type()
)
fsTacMcastPrfFilterGrpStartAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsTacMcastPrfFilterGrpStartAddr.setStatus("current")


class _FsTacMcastPrfFilterGrpEndAddr_Type(InetAddress):
    """Custom type fsTacMcastPrfFilterGrpEndAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 16),
    )


_FsTacMcastPrfFilterGrpEndAddr_Type.__name__ = "InetAddress"
_FsTacMcastPrfFilterGrpEndAddr_Object = MibTableColumn
fsTacMcastPrfFilterGrpEndAddr = _FsTacMcastPrfFilterGrpEndAddr_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 8, 2, 2, 1, 2),
    _FsTacMcastPrfFilterGrpEndAddr_Type()
)
fsTacMcastPrfFilterGrpEndAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsTacMcastPrfFilterGrpEndAddr.setStatus("current")


class _FsTacMcastPrfFilterSrcStartAddr_Type(InetAddress):
    """Custom type fsTacMcastPrfFilterSrcStartAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 16),
    )


_FsTacMcastPrfFilterSrcStartAddr_Type.__name__ = "InetAddress"
_FsTacMcastPrfFilterSrcStartAddr_Object = MibTableColumn
fsTacMcastPrfFilterSrcStartAddr = _FsTacMcastPrfFilterSrcStartAddr_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 8, 2, 2, 1, 3),
    _FsTacMcastPrfFilterSrcStartAddr_Type()
)
fsTacMcastPrfFilterSrcStartAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsTacMcastPrfFilterSrcStartAddr.setStatus("current")


class _FsTacMcastPrfFilterSrcEndAddr_Type(InetAddress):
    """Custom type fsTacMcastPrfFilterSrcEndAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 16),
    )


_FsTacMcastPrfFilterSrcEndAddr_Type.__name__ = "InetAddress"
_FsTacMcastPrfFilterSrcEndAddr_Object = MibTableColumn
fsTacMcastPrfFilterSrcEndAddr = _FsTacMcastPrfFilterSrcEndAddr_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 8, 2, 2, 1, 4),
    _FsTacMcastPrfFilterSrcEndAddr_Type()
)
fsTacMcastPrfFilterSrcEndAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsTacMcastPrfFilterSrcEndAddr.setStatus("current")


class _FsTacMcastPrfFilterMode_Type(Integer32):
    """Custom type fsTacMcastPrfFilterMode based on Integer32"""
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
        *(("include", 1),
          ("exclude", 2),
          ("any", 3))
    )


_FsTacMcastPrfFilterMode_Type.__name__ = "Integer32"
_FsTacMcastPrfFilterMode_Object = MibTableColumn
fsTacMcastPrfFilterMode = _FsTacMcastPrfFilterMode_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 8, 2, 2, 1, 5),
    _FsTacMcastPrfFilterMode_Type()
)
fsTacMcastPrfFilterMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsTacMcastPrfFilterMode.setStatus("current")
_FsTacMcastPrfFilterStatus_Type = RowStatus
_FsTacMcastPrfFilterStatus_Object = MibTableColumn
fsTacMcastPrfFilterStatus = _FsTacMcastPrfFilterStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 8, 2, 2, 1, 6),
    _FsTacMcastPrfFilterStatus_Type()
)
fsTacMcastPrfFilterStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsTacMcastPrfFilterStatus.setStatus("current")
_FsTacChannels_ObjectIdentity = ObjectIdentity
fsTacChannels = _FsTacChannels_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29601, 2, 8, 3)
)
_FsTacMcastChannelTable_Object = MibTable
fsTacMcastChannelTable = _FsTacMcastChannelTable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 8, 3, 1)
)
if mibBuilder.loadTexts:
    fsTacMcastChannelTable.setStatus("current")
_FsTacMcastChannelEntry_Object = MibTableRow
fsTacMcastChannelEntry = _FsTacMcastChannelEntry_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 8, 3, 1, 1)
)
fsTacMcastChannelEntry.setIndexNames(
    (0, "ARICENT-TAC-MIB", "fsTacMcastChannelAddressType"),
    (0, "ARICENT-TAC-MIB", "fsTacMcastChannelGrpAddress"),
    (0, "ARICENT-TAC-MIB", "fsTacMcastChannelSrcAddress"),
)
if mibBuilder.loadTexts:
    fsTacMcastChannelEntry.setStatus("current")
_FsTacMcastChannelAddressType_Type = InetAddressType
_FsTacMcastChannelAddressType_Object = MibTableColumn
fsTacMcastChannelAddressType = _FsTacMcastChannelAddressType_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 8, 3, 1, 1, 1),
    _FsTacMcastChannelAddressType_Type()
)
fsTacMcastChannelAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsTacMcastChannelAddressType.setStatus("current")


class _FsTacMcastChannelGrpAddress_Type(InetAddress):
    """Custom type fsTacMcastChannelGrpAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 16),
    )


_FsTacMcastChannelGrpAddress_Type.__name__ = "InetAddress"
_FsTacMcastChannelGrpAddress_Object = MibTableColumn
fsTacMcastChannelGrpAddress = _FsTacMcastChannelGrpAddress_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 8, 3, 1, 1, 2),
    _FsTacMcastChannelGrpAddress_Type()
)
fsTacMcastChannelGrpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsTacMcastChannelGrpAddress.setStatus("current")


class _FsTacMcastChannelSrcAddress_Type(InetAddress):
    """Custom type fsTacMcastChannelSrcAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 16),
    )


_FsTacMcastChannelSrcAddress_Type.__name__ = "InetAddress"
_FsTacMcastChannelSrcAddress_Object = MibTableColumn
fsTacMcastChannelSrcAddress = _FsTacMcastChannelSrcAddress_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 8, 3, 1, 1, 3),
    _FsTacMcastChannelSrcAddress_Type()
)
fsTacMcastChannelSrcAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsTacMcastChannelSrcAddress.setStatus("current")


class _FsTacMcastChannelBandWidth_Type(Unsigned32):
    """Custom type fsTacMcastChannelBandWidth based on Unsigned32"""
    defaultValue = 2000


_FsTacMcastChannelBandWidth_Type.__name__ = "Unsigned32"
_FsTacMcastChannelBandWidth_Object = MibTableColumn
fsTacMcastChannelBandWidth = _FsTacMcastChannelBandWidth_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 8, 3, 1, 1, 4),
    _FsTacMcastChannelBandWidth_Type()
)
fsTacMcastChannelBandWidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsTacMcastChannelBandWidth.setStatus("current")
_FsTacMcastChannelRowStatus_Type = RowStatus
_FsTacMcastChannelRowStatus_Object = MibTableColumn
fsTacMcastChannelRowStatus = _FsTacMcastChannelRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 8, 3, 1, 1, 5),
    _FsTacMcastChannelRowStatus_Type()
)
fsTacMcastChannelRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsTacMcastChannelRowStatus.setStatus("current")
_FsTacStatistics_ObjectIdentity = ObjectIdentity
fsTacStatistics = _FsTacStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29601, 2, 8, 4)
)
_FsTacMcastPrfStatsTable_Object = MibTable
fsTacMcastPrfStatsTable = _FsTacMcastPrfStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 8, 4, 1)
)
if mibBuilder.loadTexts:
    fsTacMcastPrfStatsTable.setStatus("current")
_FsTacMcastPrfStatsEntry_Object = MibTableRow
fsTacMcastPrfStatsEntry = _FsTacMcastPrfStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 8, 4, 1, 1)
)
fsTacMcastPrfStatsEntry.setIndexNames(
    (0, "ARICENT-TAC-MIB", "fsTacMcastProfileId"),
    (0, "ARICENT-TAC-MIB", "fsTacMcastProfileAddrType"),
)
if mibBuilder.loadTexts:
    fsTacMcastPrfStatsEntry.setStatus("current")
_FsTacMcastPrfStatsPortRefCnt_Type = Unsigned32
_FsTacMcastPrfStatsPortRefCnt_Object = MibTableColumn
fsTacMcastPrfStatsPortRefCnt = _FsTacMcastPrfStatsPortRefCnt_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 8, 4, 1, 1, 1),
    _FsTacMcastPrfStatsPortRefCnt_Type()
)
fsTacMcastPrfStatsPortRefCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsTacMcastPrfStatsPortRefCnt.setStatus("current")
_FsTacMcastPrfStatsVlanRefCnt_Type = Unsigned32
_FsTacMcastPrfStatsVlanRefCnt_Object = MibTableColumn
fsTacMcastPrfStatsVlanRefCnt = _FsTacMcastPrfStatsVlanRefCnt_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 8, 4, 1, 1, 2),
    _FsTacMcastPrfStatsVlanRefCnt_Type()
)
fsTacMcastPrfStatsVlanRefCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsTacMcastPrfStatsVlanRefCnt.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ARICENT-TAC-MIB",
    **{"fstac": fstac,
       "fsTacScalars": fsTacScalars,
       "fsTacMcastChannelDefaultBandwidth": fsTacMcastChannelDefaultBandwidth,
       "fsTacTraceOption": fsTacTraceOption,
       "fsTacStatus": fsTacStatus,
       "fsTacProfile": fsTacProfile,
       "fsTacMcastProfileTable": fsTacMcastProfileTable,
       "fsTacMcastProfileEntry": fsTacMcastProfileEntry,
       "fsTacMcastProfileId": fsTacMcastProfileId,
       "fsTacMcastProfileAddrType": fsTacMcastProfileAddrType,
       "fsTacMcastProfileAction": fsTacMcastProfileAction,
       "fsTacMcastProfileDescription": fsTacMcastProfileDescription,
       "fsTacMcastProfileStatus": fsTacMcastProfileStatus,
       "fsTacMcastPrfFilterTable": fsTacMcastPrfFilterTable,
       "fsTacMcastPrfFilterEntry": fsTacMcastPrfFilterEntry,
       "fsTacMcastPrfFilterGrpStartAddr": fsTacMcastPrfFilterGrpStartAddr,
       "fsTacMcastPrfFilterGrpEndAddr": fsTacMcastPrfFilterGrpEndAddr,
       "fsTacMcastPrfFilterSrcStartAddr": fsTacMcastPrfFilterSrcStartAddr,
       "fsTacMcastPrfFilterSrcEndAddr": fsTacMcastPrfFilterSrcEndAddr,
       "fsTacMcastPrfFilterMode": fsTacMcastPrfFilterMode,
       "fsTacMcastPrfFilterStatus": fsTacMcastPrfFilterStatus,
       "fsTacChannels": fsTacChannels,
       "fsTacMcastChannelTable": fsTacMcastChannelTable,
       "fsTacMcastChannelEntry": fsTacMcastChannelEntry,
       "fsTacMcastChannelAddressType": fsTacMcastChannelAddressType,
       "fsTacMcastChannelGrpAddress": fsTacMcastChannelGrpAddress,
       "fsTacMcastChannelSrcAddress": fsTacMcastChannelSrcAddress,
       "fsTacMcastChannelBandWidth": fsTacMcastChannelBandWidth,
       "fsTacMcastChannelRowStatus": fsTacMcastChannelRowStatus,
       "fsTacStatistics": fsTacStatistics,
       "fsTacMcastPrfStatsTable": fsTacMcastPrfStatsTable,
       "fsTacMcastPrfStatsEntry": fsTacMcastPrfStatsEntry,
       "fsTacMcastPrfStatsPortRefCnt": fsTacMcastPrfStatsPortRefCnt,
       "fsTacMcastPrfStatsVlanRefCnt": fsTacMcastPrfStatsVlanRefCnt}
)
