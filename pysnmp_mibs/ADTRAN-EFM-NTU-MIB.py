# SNMP MIB module (ADTRAN-EFM-NTU-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/adtran/ADTRAN-EFM-NTU-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:32:15 2025
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

(adGenPortTrapIdentifier,) = mibBuilder.importSymbols(
    "ADTRAN-GENPORT-MIB",
    "adGenPortTrapIdentifier")

(adGenSlotInfoIndex,) = mibBuilder.importSymbols(
    "ADTRAN-GENSLOT-MIB",
    "adGenSlotInfoIndex")

(adTrapInformSeqNum,) = mibBuilder.importSymbols(
    "ADTRAN-GENTRAPINFORM-MIB",
    "adTrapInformSeqNum")

(AdGenTrapVersion,) = mibBuilder.importSymbols(
    "ADTRAN-SHARED-CND-SYSTEM-TC-MIB",
    "AdGenTrapVersion")

(adGenEfmNtu,
 adGenEfmNtuID) = mibBuilder.importSymbols(
    "ADTRAN-SHARED-EFM-MIB",
    "adGenEfmNtu",
    "adGenEfmNtuID")

(EntryStatus,) = mibBuilder.importSymbols(
    "ADTRAN-TC",
    "EntryStatus")

(InterfaceIndex,
 ifDescr,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifDescr",
    "ifIndex")

(InetAddressIPv4,
 InetAddressIPv6,
 InetAddressPrefixLength) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddressIPv4",
    "InetAddressIPv6",
    "InetAddressPrefixLength")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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

adGenEfmNtuMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 66, 2, 1)
)
if mibBuilder.loadTexts:
    adGenEfmNtuMIB.setRevisions(
        ("2014-09-22 00:00",
         "2014-05-16 00:00",
         "2007-08-31 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AdGenEfmNtuConfiguration_ObjectIdentity = ObjectIdentity
adGenEfmNtuConfiguration = _AdGenEfmNtuConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 2, 1)
)
_AdGenEfmNtuProvisioning_ObjectIdentity = ObjectIdentity
adGenEfmNtuProvisioning = _AdGenEfmNtuProvisioning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 2, 2)
)
_AdGenEfmNtuProvTable_Object = MibTable
adGenEfmNtuProvTable = _AdGenEfmNtuProvTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 2, 2, 1)
)
if mibBuilder.loadTexts:
    adGenEfmNtuProvTable.setStatus("current")
_AdGenEfmNtuProvEntry_Object = MibTableRow
adGenEfmNtuProvEntry = _AdGenEfmNtuProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 2, 2, 1, 1)
)
adGenEfmNtuProvEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adGenEfmNtuProvEntry.setStatus("current")


class _AdGenEfmNtuProvRestoreDefaults_Type(Integer32):
    """Custom type adGenEfmNtuProvRestoreDefaults based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("restoreDefaults", 1)
    )


_AdGenEfmNtuProvRestoreDefaults_Type.__name__ = "Integer32"
_AdGenEfmNtuProvRestoreDefaults_Object = MibTableColumn
adGenEfmNtuProvRestoreDefaults = _AdGenEfmNtuProvRestoreDefaults_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 2, 2, 1, 1, 1),
    _AdGenEfmNtuProvRestoreDefaults_Type()
)
adGenEfmNtuProvRestoreDefaults.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenEfmNtuProvRestoreDefaults.setStatus("current")


class _AdGenEfmNtuProvReset_Type(Integer32):
    """Custom type adGenEfmNtuProvReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset", 1)
    )


_AdGenEfmNtuProvReset_Type.__name__ = "Integer32"
_AdGenEfmNtuProvReset_Object = MibTableColumn
adGenEfmNtuProvReset = _AdGenEfmNtuProvReset_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 2, 2, 1, 1, 2),
    _AdGenEfmNtuProvReset_Type()
)
adGenEfmNtuProvReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenEfmNtuProvReset.setStatus("current")


class _AdGenEfmNtuProvSwDownloadStart_Type(Integer32):
    """Custom type adGenEfmNtuProvSwDownloadStart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("start", 1)
    )


_AdGenEfmNtuProvSwDownloadStart_Type.__name__ = "Integer32"
_AdGenEfmNtuProvSwDownloadStart_Object = MibTableColumn
adGenEfmNtuProvSwDownloadStart = _AdGenEfmNtuProvSwDownloadStart_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 2, 2, 1, 1, 3),
    _AdGenEfmNtuProvSwDownloadStart_Type()
)
adGenEfmNtuProvSwDownloadStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenEfmNtuProvSwDownloadStart.setStatus("current")
_AdGenEfmNtuProvSwDownloadFilename_Type = OctetString
_AdGenEfmNtuProvSwDownloadFilename_Object = MibTableColumn
adGenEfmNtuProvSwDownloadFilename = _AdGenEfmNtuProvSwDownloadFilename_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 2, 2, 1, 1, 4),
    _AdGenEfmNtuProvSwDownloadFilename_Type()
)
adGenEfmNtuProvSwDownloadFilename.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenEfmNtuProvSwDownloadFilename.setStatus("current")
_AdGenEfmNtuProvSwDownloadStatus_Type = OctetString
_AdGenEfmNtuProvSwDownloadStatus_Object = MibTableColumn
adGenEfmNtuProvSwDownloadStatus = _AdGenEfmNtuProvSwDownloadStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 2, 2, 1, 1, 5),
    _AdGenEfmNtuProvSwDownloadStatus_Type()
)
adGenEfmNtuProvSwDownloadStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEfmNtuProvSwDownloadStatus.setStatus("current")
_AdGenEfmNtuProvCustId_Type = OctetString
_AdGenEfmNtuProvCustId_Object = MibTableColumn
adGenEfmNtuProvCustId = _AdGenEfmNtuProvCustId_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 2, 2, 1, 1, 6),
    _AdGenEfmNtuProvCustId_Type()
)
adGenEfmNtuProvCustId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenEfmNtuProvCustId.setStatus("current")


class _AdGenEfmNtuProvCustIfAutoNeg_Type(Integer32):
    """Custom type adGenEfmNtuProvCustIfAutoNeg based on Integer32"""
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


_AdGenEfmNtuProvCustIfAutoNeg_Type.__name__ = "Integer32"
_AdGenEfmNtuProvCustIfAutoNeg_Object = MibTableColumn
adGenEfmNtuProvCustIfAutoNeg = _AdGenEfmNtuProvCustIfAutoNeg_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 2, 2, 1, 1, 7),
    _AdGenEfmNtuProvCustIfAutoNeg_Type()
)
adGenEfmNtuProvCustIfAutoNeg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenEfmNtuProvCustIfAutoNeg.setStatus("current")


class _AdGenEfmNtuProvCustIfSpeed_Type(Integer32):
    """Custom type adGenEfmNtuProvCustIfSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("tenBaseT", 1),
          ("hundredBaseT", 2))
    )


_AdGenEfmNtuProvCustIfSpeed_Type.__name__ = "Integer32"
_AdGenEfmNtuProvCustIfSpeed_Object = MibTableColumn
adGenEfmNtuProvCustIfSpeed = _AdGenEfmNtuProvCustIfSpeed_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 2, 2, 1, 1, 8),
    _AdGenEfmNtuProvCustIfSpeed_Type()
)
adGenEfmNtuProvCustIfSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenEfmNtuProvCustIfSpeed.setStatus("current")


class _AdGenEfmNtuProvCustIfDuplex_Type(Integer32):
    """Custom type adGenEfmNtuProvCustIfDuplex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("halfDuplex", 1),
          ("fullDuplex", 2))
    )


_AdGenEfmNtuProvCustIfDuplex_Type.__name__ = "Integer32"
_AdGenEfmNtuProvCustIfDuplex_Object = MibTableColumn
adGenEfmNtuProvCustIfDuplex = _AdGenEfmNtuProvCustIfDuplex_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 2, 2, 1, 1, 9),
    _AdGenEfmNtuProvCustIfDuplex_Type()
)
adGenEfmNtuProvCustIfDuplex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenEfmNtuProvCustIfDuplex.setStatus("current")


class _AdGenEfmNtuProvCustIfFlowControl_Type(Integer32):
    """Custom type adGenEfmNtuProvCustIfFlowControl based on Integer32"""
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


_AdGenEfmNtuProvCustIfFlowControl_Type.__name__ = "Integer32"
_AdGenEfmNtuProvCustIfFlowControl_Object = MibTableColumn
adGenEfmNtuProvCustIfFlowControl = _AdGenEfmNtuProvCustIfFlowControl_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 2, 2, 1, 1, 10),
    _AdGenEfmNtuProvCustIfFlowControl_Type()
)
adGenEfmNtuProvCustIfFlowControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenEfmNtuProvCustIfFlowControl.setStatus("current")
_AdGenEfmNtuProvEnablePassword_Type = OctetString
_AdGenEfmNtuProvEnablePassword_Object = MibTableColumn
adGenEfmNtuProvEnablePassword = _AdGenEfmNtuProvEnablePassword_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 2, 2, 1, 1, 11),
    _AdGenEfmNtuProvEnablePassword_Type()
)
adGenEfmNtuProvEnablePassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenEfmNtuProvEnablePassword.setStatus("current")
_AdGenEfmNtuProvMacTableSize_Type = Integer32
_AdGenEfmNtuProvMacTableSize_Object = MibTableColumn
adGenEfmNtuProvMacTableSize = _AdGenEfmNtuProvMacTableSize_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 2, 2, 1, 1, 12),
    _AdGenEfmNtuProvMacTableSize_Type()
)
adGenEfmNtuProvMacTableSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenEfmNtuProvMacTableSize.setStatus("current")
_AdGenEfmNtuProvMacAging_Type = Integer32
_AdGenEfmNtuProvMacAging_Object = MibTableColumn
adGenEfmNtuProvMacAging = _AdGenEfmNtuProvMacAging_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 2, 2, 1, 1, 13),
    _AdGenEfmNtuProvMacAging_Type()
)
adGenEfmNtuProvMacAging.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenEfmNtuProvMacAging.setStatus("current")


class _AdGenEfmNtuProvLinkStateAware_Type(Integer32):
    """Custom type adGenEfmNtuProvLinkStateAware based on Integer32"""
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


_AdGenEfmNtuProvLinkStateAware_Type.__name__ = "Integer32"
_AdGenEfmNtuProvLinkStateAware_Object = MibTableColumn
adGenEfmNtuProvLinkStateAware = _AdGenEfmNtuProvLinkStateAware_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 2, 2, 1, 1, 14),
    _AdGenEfmNtuProvLinkStateAware_Type()
)
adGenEfmNtuProvLinkStateAware.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenEfmNtuProvLinkStateAware.setStatus("current")


class _AdGenEfmNtuAutoDiscoverMode_Type(TruthValue):
    """Custom type adGenEfmNtuAutoDiscoverMode based on TruthValue"""
    defaultValue = 2


_AdGenEfmNtuAutoDiscoverMode_Type.__name__ = "TruthValue"
_AdGenEfmNtuAutoDiscoverMode_Object = MibTableColumn
adGenEfmNtuAutoDiscoverMode = _AdGenEfmNtuAutoDiscoverMode_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 2, 2, 1, 1, 15),
    _AdGenEfmNtuAutoDiscoverMode_Type()
)
adGenEfmNtuAutoDiscoverMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenEfmNtuAutoDiscoverMode.setStatus("current")


class _AdGenEfmNtuAutoDiscoverAck_Type(TruthValue):
    """Custom type adGenEfmNtuAutoDiscoverAck based on TruthValue"""
    defaultValue = 2


_AdGenEfmNtuAutoDiscoverAck_Type.__name__ = "TruthValue"
_AdGenEfmNtuAutoDiscoverAck_Object = MibTableColumn
adGenEfmNtuAutoDiscoverAck = _AdGenEfmNtuAutoDiscoverAck_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 2, 2, 1, 1, 16),
    _AdGenEfmNtuAutoDiscoverAck_Type()
)
adGenEfmNtuAutoDiscoverAck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenEfmNtuAutoDiscoverAck.setStatus("current")
_AdGenEfmNtuProvCfmTable_Object = MibTable
adGenEfmNtuProvCfmTable = _AdGenEfmNtuProvCfmTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 2, 2, 2)
)
if mibBuilder.loadTexts:
    adGenEfmNtuProvCfmTable.setStatus("current")
_AdGenEfmNtuProvCfmEntry_Object = MibTableRow
adGenEfmNtuProvCfmEntry = _AdGenEfmNtuProvCfmEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 2, 2, 2, 1)
)
adGenEfmNtuProvCfmEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adGenEfmNtuProvCfmEntry.setStatus("current")
_AdGenEfmNtuProvCfmMdName_Type = OctetString
_AdGenEfmNtuProvCfmMdName_Object = MibTableColumn
adGenEfmNtuProvCfmMdName = _AdGenEfmNtuProvCfmMdName_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 2, 2, 2, 1, 1),
    _AdGenEfmNtuProvCfmMdName_Type()
)
adGenEfmNtuProvCfmMdName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenEfmNtuProvCfmMdName.setStatus("current")
_AdGenEfmNtuProvCfmMaName_Type = OctetString
_AdGenEfmNtuProvCfmMaName_Object = MibTableColumn
adGenEfmNtuProvCfmMaName = _AdGenEfmNtuProvCfmMaName_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 2, 2, 2, 1, 2),
    _AdGenEfmNtuProvCfmMaName_Type()
)
adGenEfmNtuProvCfmMaName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenEfmNtuProvCfmMaName.setStatus("current")
_AdGenEfmNtuProvCfmLocalMepId_Type = Integer32
_AdGenEfmNtuProvCfmLocalMepId_Object = MibTableColumn
adGenEfmNtuProvCfmLocalMepId = _AdGenEfmNtuProvCfmLocalMepId_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 2, 2, 2, 1, 3),
    _AdGenEfmNtuProvCfmLocalMepId_Type()
)
adGenEfmNtuProvCfmLocalMepId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenEfmNtuProvCfmLocalMepId.setStatus("current")
_AdGenEfmNtuProvCfmMdLevel_Type = Integer32
_AdGenEfmNtuProvCfmMdLevel_Object = MibTableColumn
adGenEfmNtuProvCfmMdLevel = _AdGenEfmNtuProvCfmMdLevel_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 2, 2, 2, 1, 4),
    _AdGenEfmNtuProvCfmMdLevel_Type()
)
adGenEfmNtuProvCfmMdLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenEfmNtuProvCfmMdLevel.setStatus("current")
_AdGenEfmNtuProvCfmVlanId_Type = Integer32
_AdGenEfmNtuProvCfmVlanId_Object = MibTableColumn
adGenEfmNtuProvCfmVlanId = _AdGenEfmNtuProvCfmVlanId_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 2, 2, 2, 1, 5),
    _AdGenEfmNtuProvCfmVlanId_Type()
)
adGenEfmNtuProvCfmVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenEfmNtuProvCfmVlanId.setStatus("current")
_AdGenEfmNtuProvCfmCcmInterval_Type = Integer32
_AdGenEfmNtuProvCfmCcmInterval_Object = MibTableColumn
adGenEfmNtuProvCfmCcmInterval = _AdGenEfmNtuProvCfmCcmInterval_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 2, 2, 2, 1, 6),
    _AdGenEfmNtuProvCfmCcmInterval_Type()
)
adGenEfmNtuProvCfmCcmInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenEfmNtuProvCfmCcmInterval.setStatus("current")
_AdGenEfmNtuProvCfmMepTableNextIndex_Type = Integer32
_AdGenEfmNtuProvCfmMepTableNextIndex_Object = MibTableColumn
adGenEfmNtuProvCfmMepTableNextIndex = _AdGenEfmNtuProvCfmMepTableNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 2, 2, 2, 1, 7),
    _AdGenEfmNtuProvCfmMepTableNextIndex_Type()
)
adGenEfmNtuProvCfmMepTableNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEfmNtuProvCfmMepTableNextIndex.setStatus("current")
_AdGenEfmNtuProvCfmMepTable_Object = MibTable
adGenEfmNtuProvCfmMepTable = _AdGenEfmNtuProvCfmMepTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 2, 2, 3)
)
if mibBuilder.loadTexts:
    adGenEfmNtuProvCfmMepTable.setStatus("current")
_AdGenEfmNtuProvCfmMepEntry_Object = MibTableRow
adGenEfmNtuProvCfmMepEntry = _AdGenEfmNtuProvCfmMepEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 2, 2, 3, 1)
)
adGenEfmNtuProvCfmMepEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ADTRAN-EFM-NTU-MIB", "adGenEfmNtuProvCfmMepIndex"),
)
if mibBuilder.loadTexts:
    adGenEfmNtuProvCfmMepEntry.setStatus("current")
_AdGenEfmNtuProvCfmMepIndex_Type = Integer32
_AdGenEfmNtuProvCfmMepIndex_Object = MibTableColumn
adGenEfmNtuProvCfmMepIndex = _AdGenEfmNtuProvCfmMepIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 2, 2, 3, 1, 1),
    _AdGenEfmNtuProvCfmMepIndex_Type()
)
adGenEfmNtuProvCfmMepIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEfmNtuProvCfmMepIndex.setStatus("current")
_AdGenEfmNtuProvCfmMepId_Type = Integer32
_AdGenEfmNtuProvCfmMepId_Object = MibTableColumn
adGenEfmNtuProvCfmMepId = _AdGenEfmNtuProvCfmMepId_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 2, 2, 3, 1, 2),
    _AdGenEfmNtuProvCfmMepId_Type()
)
adGenEfmNtuProvCfmMepId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenEfmNtuProvCfmMepId.setStatus("current")
_AdGenEfmNtuProvCfmMepEntryStatus_Type = EntryStatus
_AdGenEfmNtuProvCfmMepEntryStatus_Object = MibTableColumn
adGenEfmNtuProvCfmMepEntryStatus = _AdGenEfmNtuProvCfmMepEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 2, 2, 3, 1, 3),
    _AdGenEfmNtuProvCfmMepEntryStatus_Type()
)
adGenEfmNtuProvCfmMepEntryStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenEfmNtuProvCfmMepEntryStatus.setStatus("current")
_AdGenEfmNtuProvMgmtIpTable_Object = MibTable
adGenEfmNtuProvMgmtIpTable = _AdGenEfmNtuProvMgmtIpTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 2, 2, 4)
)
if mibBuilder.loadTexts:
    adGenEfmNtuProvMgmtIpTable.setStatus("current")
_AdGenEfmNtuProvMgmtIpEntry_Object = MibTableRow
adGenEfmNtuProvMgmtIpEntry = _AdGenEfmNtuProvMgmtIpEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 2, 2, 4, 1)
)
adGenEfmNtuProvMgmtIpEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adGenEfmNtuProvMgmtIpEntry.setStatus("current")
_AdGenEfmNtuProvMgmtIpAddress_Type = IpAddress
_AdGenEfmNtuProvMgmtIpAddress_Object = MibTableColumn
adGenEfmNtuProvMgmtIpAddress = _AdGenEfmNtuProvMgmtIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 2, 2, 4, 1, 1),
    _AdGenEfmNtuProvMgmtIpAddress_Type()
)
adGenEfmNtuProvMgmtIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenEfmNtuProvMgmtIpAddress.setStatus("current")
_AdGenEfmNtuProvMgmtIpSubnetMask_Type = IpAddress
_AdGenEfmNtuProvMgmtIpSubnetMask_Object = MibTableColumn
adGenEfmNtuProvMgmtIpSubnetMask = _AdGenEfmNtuProvMgmtIpSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 2, 2, 4, 1, 2),
    _AdGenEfmNtuProvMgmtIpSubnetMask_Type()
)
adGenEfmNtuProvMgmtIpSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenEfmNtuProvMgmtIpSubnetMask.setStatus("current")
_AdGenEfmNtuProvMgmtIpGateway_Type = IpAddress
_AdGenEfmNtuProvMgmtIpGateway_Object = MibTableColumn
adGenEfmNtuProvMgmtIpGateway = _AdGenEfmNtuProvMgmtIpGateway_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 2, 2, 4, 1, 3),
    _AdGenEfmNtuProvMgmtIpGateway_Type()
)
adGenEfmNtuProvMgmtIpGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenEfmNtuProvMgmtIpGateway.setStatus("current")
_AdGenEfmNtuProvMgmtIpVlan_Type = Integer32
_AdGenEfmNtuProvMgmtIpVlan_Object = MibTableColumn
adGenEfmNtuProvMgmtIpVlan = _AdGenEfmNtuProvMgmtIpVlan_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 2, 2, 4, 1, 4),
    _AdGenEfmNtuProvMgmtIpVlan_Type()
)
adGenEfmNtuProvMgmtIpVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenEfmNtuProvMgmtIpVlan.setStatus("current")
_AdGenEfmNtuProvMgmtTftpServer_Type = IpAddress
_AdGenEfmNtuProvMgmtTftpServer_Object = MibTableColumn
adGenEfmNtuProvMgmtTftpServer = _AdGenEfmNtuProvMgmtTftpServer_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 2, 2, 4, 1, 5),
    _AdGenEfmNtuProvMgmtTftpServer_Type()
)
adGenEfmNtuProvMgmtTftpServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenEfmNtuProvMgmtTftpServer.setStatus("current")
_AdGenEfmNtuProvMgmtSnmpWriteCommunity_Type = DisplayString
_AdGenEfmNtuProvMgmtSnmpWriteCommunity_Object = MibTableColumn
adGenEfmNtuProvMgmtSnmpWriteCommunity = _AdGenEfmNtuProvMgmtSnmpWriteCommunity_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 2, 2, 4, 1, 6),
    _AdGenEfmNtuProvMgmtSnmpWriteCommunity_Type()
)
adGenEfmNtuProvMgmtSnmpWriteCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenEfmNtuProvMgmtSnmpWriteCommunity.setStatus("current")
_AdGenEfmNtuProvMgmtSnmpReadCommunity_Type = DisplayString
_AdGenEfmNtuProvMgmtSnmpReadCommunity_Object = MibTableColumn
adGenEfmNtuProvMgmtSnmpReadCommunity = _AdGenEfmNtuProvMgmtSnmpReadCommunity_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 2, 2, 4, 1, 7),
    _AdGenEfmNtuProvMgmtSnmpReadCommunity_Type()
)
adGenEfmNtuProvMgmtSnmpReadCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenEfmNtuProvMgmtSnmpReadCommunity.setStatus("current")
_AdGenEfmNtuProvMgmtSysName_Type = DisplayString
_AdGenEfmNtuProvMgmtSysName_Object = MibTableColumn
adGenEfmNtuProvMgmtSysName = _AdGenEfmNtuProvMgmtSysName_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 2, 2, 4, 1, 8),
    _AdGenEfmNtuProvMgmtSysName_Type()
)
adGenEfmNtuProvMgmtSysName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenEfmNtuProvMgmtSysName.setStatus("current")
_AdGenEfmNtuProvMgmtFarEndIfIndex_Type = InterfaceIndex
_AdGenEfmNtuProvMgmtFarEndIfIndex_Object = MibTableColumn
adGenEfmNtuProvMgmtFarEndIfIndex = _AdGenEfmNtuProvMgmtFarEndIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 2, 2, 4, 1, 9),
    _AdGenEfmNtuProvMgmtFarEndIfIndex_Type()
)
adGenEfmNtuProvMgmtFarEndIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEfmNtuProvMgmtFarEndIfIndex.setStatus("current")
_AdGenEfmNtuProvMgmtFarEndIpAddress_Type = IpAddress
_AdGenEfmNtuProvMgmtFarEndIpAddress_Object = MibTableColumn
adGenEfmNtuProvMgmtFarEndIpAddress = _AdGenEfmNtuProvMgmtFarEndIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 2, 2, 4, 1, 10),
    _AdGenEfmNtuProvMgmtFarEndIpAddress_Type()
)
adGenEfmNtuProvMgmtFarEndIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEfmNtuProvMgmtFarEndIpAddress.setStatus("current")
_AdGenEfmNtuProvMgmtFarEndSysName_Type = DisplayString
_AdGenEfmNtuProvMgmtFarEndSysName_Object = MibTableColumn
adGenEfmNtuProvMgmtFarEndSysName = _AdGenEfmNtuProvMgmtFarEndSysName_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 2, 2, 4, 1, 11),
    _AdGenEfmNtuProvMgmtFarEndSysName_Type()
)
adGenEfmNtuProvMgmtFarEndSysName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEfmNtuProvMgmtFarEndSysName.setStatus("current")
_AdGenEfmNtuProvMgmtPriority_Type = Integer32
_AdGenEfmNtuProvMgmtPriority_Object = MibTableColumn
adGenEfmNtuProvMgmtPriority = _AdGenEfmNtuProvMgmtPriority_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 2, 2, 4, 1, 12),
    _AdGenEfmNtuProvMgmtPriority_Type()
)
adGenEfmNtuProvMgmtPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenEfmNtuProvMgmtPriority.setStatus("current")
_AdGenEfmNtuProvMgmtSnmpSysLocation_Type = DisplayString
_AdGenEfmNtuProvMgmtSnmpSysLocation_Object = MibTableColumn
adGenEfmNtuProvMgmtSnmpSysLocation = _AdGenEfmNtuProvMgmtSnmpSysLocation_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 2, 2, 4, 1, 13),
    _AdGenEfmNtuProvMgmtSnmpSysLocation_Type()
)
adGenEfmNtuProvMgmtSnmpSysLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenEfmNtuProvMgmtSnmpSysLocation.setStatus("current")
_AdGenEfmNtuProvMgmtEzProvHostOneIpAddress_Type = IpAddress
_AdGenEfmNtuProvMgmtEzProvHostOneIpAddress_Object = MibTableColumn
adGenEfmNtuProvMgmtEzProvHostOneIpAddress = _AdGenEfmNtuProvMgmtEzProvHostOneIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 2, 2, 4, 1, 14),
    _AdGenEfmNtuProvMgmtEzProvHostOneIpAddress_Type()
)
adGenEfmNtuProvMgmtEzProvHostOneIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenEfmNtuProvMgmtEzProvHostOneIpAddress.setStatus("current")
_AdGenEfmNtuProvMgmtEzProvHostOneTrapVersion_Type = AdGenTrapVersion
_AdGenEfmNtuProvMgmtEzProvHostOneTrapVersion_Object = MibTableColumn
adGenEfmNtuProvMgmtEzProvHostOneTrapVersion = _AdGenEfmNtuProvMgmtEzProvHostOneTrapVersion_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 2, 2, 4, 1, 15),
    _AdGenEfmNtuProvMgmtEzProvHostOneTrapVersion_Type()
)
adGenEfmNtuProvMgmtEzProvHostOneTrapVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenEfmNtuProvMgmtEzProvHostOneTrapVersion.setStatus("current")
_AdGenEfmNtuProvMgmtEzProvHostTwoIpAddress_Type = IpAddress
_AdGenEfmNtuProvMgmtEzProvHostTwoIpAddress_Object = MibTableColumn
adGenEfmNtuProvMgmtEzProvHostTwoIpAddress = _AdGenEfmNtuProvMgmtEzProvHostTwoIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 2, 2, 4, 1, 16),
    _AdGenEfmNtuProvMgmtEzProvHostTwoIpAddress_Type()
)
adGenEfmNtuProvMgmtEzProvHostTwoIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenEfmNtuProvMgmtEzProvHostTwoIpAddress.setStatus("current")
_AdGenEfmNtuProvMgmtEzProvHostTwoTrapVersion_Type = AdGenTrapVersion
_AdGenEfmNtuProvMgmtEzProvHostTwoTrapVersion_Object = MibTableColumn
adGenEfmNtuProvMgmtEzProvHostTwoTrapVersion = _AdGenEfmNtuProvMgmtEzProvHostTwoTrapVersion_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 2, 2, 4, 1, 17),
    _AdGenEfmNtuProvMgmtEzProvHostTwoTrapVersion_Type()
)
adGenEfmNtuProvMgmtEzProvHostTwoTrapVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenEfmNtuProvMgmtEzProvHostTwoTrapVersion.setStatus("current")
_AdGenEfmNtuProvMgmtEzProvEnabled_Type = TruthValue
_AdGenEfmNtuProvMgmtEzProvEnabled_Object = MibTableColumn
adGenEfmNtuProvMgmtEzProvEnabled = _AdGenEfmNtuProvMgmtEzProvEnabled_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 2, 2, 4, 1, 18),
    _AdGenEfmNtuProvMgmtEzProvEnabled_Type()
)
adGenEfmNtuProvMgmtEzProvEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenEfmNtuProvMgmtEzProvEnabled.setStatus("current")
_AdGenEfmNtuProvMgmtIpv6AddressPrefixLength_Type = InetAddressPrefixLength
_AdGenEfmNtuProvMgmtIpv6AddressPrefixLength_Object = MibTableColumn
adGenEfmNtuProvMgmtIpv6AddressPrefixLength = _AdGenEfmNtuProvMgmtIpv6AddressPrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 2, 2, 4, 1, 19),
    _AdGenEfmNtuProvMgmtIpv6AddressPrefixLength_Type()
)
adGenEfmNtuProvMgmtIpv6AddressPrefixLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenEfmNtuProvMgmtIpv6AddressPrefixLength.setStatus("current")
_AdGenEfmNtuProvMgmtIpv6AddressEui64_Type = TruthValue
_AdGenEfmNtuProvMgmtIpv6AddressEui64_Object = MibTableColumn
adGenEfmNtuProvMgmtIpv6AddressEui64 = _AdGenEfmNtuProvMgmtIpv6AddressEui64_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 2, 2, 4, 1, 20),
    _AdGenEfmNtuProvMgmtIpv6AddressEui64_Type()
)
adGenEfmNtuProvMgmtIpv6AddressEui64.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenEfmNtuProvMgmtIpv6AddressEui64.setStatus("current")
_AdGenEfmNtuProvMgmtIpv6Address_Type = InetAddressIPv6
_AdGenEfmNtuProvMgmtIpv6Address_Object = MibTableColumn
adGenEfmNtuProvMgmtIpv6Address = _AdGenEfmNtuProvMgmtIpv6Address_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 2, 2, 4, 1, 21),
    _AdGenEfmNtuProvMgmtIpv6Address_Type()
)
adGenEfmNtuProvMgmtIpv6Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenEfmNtuProvMgmtIpv6Address.setStatus("current")
_AdGenEfmNtuProvMgmtIpv6AddressLinkLocal_Type = InetAddressIPv6
_AdGenEfmNtuProvMgmtIpv6AddressLinkLocal_Object = MibTableColumn
adGenEfmNtuProvMgmtIpv6AddressLinkLocal = _AdGenEfmNtuProvMgmtIpv6AddressLinkLocal_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 2, 2, 4, 1, 22),
    _AdGenEfmNtuProvMgmtIpv6AddressLinkLocal_Type()
)
adGenEfmNtuProvMgmtIpv6AddressLinkLocal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenEfmNtuProvMgmtIpv6AddressLinkLocal.setStatus("current")


class _AdGenEfmNtuProvMgmtAutoConfigMode_Type(TruthValue):
    """Custom type adGenEfmNtuProvMgmtAutoConfigMode based on TruthValue"""
    defaultValue = 2


_AdGenEfmNtuProvMgmtAutoConfigMode_Type.__name__ = "TruthValue"
_AdGenEfmNtuProvMgmtAutoConfigMode_Object = MibTableColumn
adGenEfmNtuProvMgmtAutoConfigMode = _AdGenEfmNtuProvMgmtAutoConfigMode_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 2, 2, 4, 1, 23),
    _AdGenEfmNtuProvMgmtAutoConfigMode_Type()
)
adGenEfmNtuProvMgmtAutoConfigMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenEfmNtuProvMgmtAutoConfigMode.setStatus("current")


class _AdGenEfmNtuProvMgmtAutoConfigFilename_Type(DisplayString):
    """Custom type adGenEfmNtuProvMgmtAutoConfigFilename based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_AdGenEfmNtuProvMgmtAutoConfigFilename_Type.__name__ = "DisplayString"
_AdGenEfmNtuProvMgmtAutoConfigFilename_Object = MibTableColumn
adGenEfmNtuProvMgmtAutoConfigFilename = _AdGenEfmNtuProvMgmtAutoConfigFilename_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 2, 2, 4, 1, 24),
    _AdGenEfmNtuProvMgmtAutoConfigFilename_Type()
)
adGenEfmNtuProvMgmtAutoConfigFilename.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenEfmNtuProvMgmtAutoConfigFilename.setStatus("current")


class _AdGenEfmNtuProvMgmtAutoConfigGroupName_Type(DisplayString):
    """Custom type adGenEfmNtuProvMgmtAutoConfigGroupName based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_AdGenEfmNtuProvMgmtAutoConfigGroupName_Type.__name__ = "DisplayString"
_AdGenEfmNtuProvMgmtAutoConfigGroupName_Object = MibTableColumn
adGenEfmNtuProvMgmtAutoConfigGroupName = _AdGenEfmNtuProvMgmtAutoConfigGroupName_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 2, 2, 4, 1, 25),
    _AdGenEfmNtuProvMgmtAutoConfigGroupName_Type()
)
adGenEfmNtuProvMgmtAutoConfigGroupName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenEfmNtuProvMgmtAutoConfigGroupName.setStatus("current")
_AdGenEfmNtuProvMgmtAutoConfigHostIpv4_Type = InetAddressIPv4
_AdGenEfmNtuProvMgmtAutoConfigHostIpv4_Object = MibTableColumn
adGenEfmNtuProvMgmtAutoConfigHostIpv4 = _AdGenEfmNtuProvMgmtAutoConfigHostIpv4_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 2, 2, 4, 1, 26),
    _AdGenEfmNtuProvMgmtAutoConfigHostIpv4_Type()
)
adGenEfmNtuProvMgmtAutoConfigHostIpv4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenEfmNtuProvMgmtAutoConfigHostIpv4.setStatus("current")
_AdGenEfmNtuProvMgmtAutoConfigHostIpv6_Type = InetAddressIPv6
_AdGenEfmNtuProvMgmtAutoConfigHostIpv6_Object = MibTableColumn
adGenEfmNtuProvMgmtAutoConfigHostIpv6 = _AdGenEfmNtuProvMgmtAutoConfigHostIpv6_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 2, 2, 4, 1, 27),
    _AdGenEfmNtuProvMgmtAutoConfigHostIpv6_Type()
)
adGenEfmNtuProvMgmtAutoConfigHostIpv6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenEfmNtuProvMgmtAutoConfigHostIpv6.setStatus("current")
_AdGenEfmNtuStatus_ObjectIdentity = ObjectIdentity
adGenEfmNtuStatus = _AdGenEfmNtuStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 2, 3)
)
_AdGenEfmNtuStatTable_Object = MibTable
adGenEfmNtuStatTable = _AdGenEfmNtuStatTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 2, 3, 1)
)
if mibBuilder.loadTexts:
    adGenEfmNtuStatTable.setStatus("current")
_AdGenEfmNtuStatEntry_Object = MibTableRow
adGenEfmNtuStatEntry = _AdGenEfmNtuStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 2, 3, 1, 1)
)
adGenEfmNtuStatEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adGenEfmNtuStatEntry.setStatus("current")
_AdGenEfmNtuStatUpTime_Type = TimeTicks
_AdGenEfmNtuStatUpTime_Object = MibTableColumn
adGenEfmNtuStatUpTime = _AdGenEfmNtuStatUpTime_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 2, 3, 1, 1, 1),
    _AdGenEfmNtuStatUpTime_Type()
)
adGenEfmNtuStatUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEfmNtuStatUpTime.setStatus("current")


class _AdGenEfmNtuStatLinkStateAware_Type(Integer32):
    """Custom type adGenEfmNtuStatLinkStateAware based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 1),
          ("up", 2))
    )


_AdGenEfmNtuStatLinkStateAware_Type.__name__ = "Integer32"
_AdGenEfmNtuStatLinkStateAware_Object = MibTableColumn
adGenEfmNtuStatLinkStateAware = _AdGenEfmNtuStatLinkStateAware_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 2, 3, 1, 1, 2),
    _AdGenEfmNtuStatLinkStateAware_Type()
)
adGenEfmNtuStatLinkStateAware.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEfmNtuStatLinkStateAware.setStatus("current")


class _AdGenEfmNtuStatCustIf_Type(Integer32):
    """Custom type adGenEfmNtuStatCustIf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 1),
          ("up", 2))
    )


_AdGenEfmNtuStatCustIf_Type.__name__ = "Integer32"
_AdGenEfmNtuStatCustIf_Object = MibTableColumn
adGenEfmNtuStatCustIf = _AdGenEfmNtuStatCustIf_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 2, 3, 1, 1, 3),
    _AdGenEfmNtuStatCustIf_Type()
)
adGenEfmNtuStatCustIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEfmNtuStatCustIf.setStatus("current")
_AdGenEfmNtuTest_ObjectIdentity = ObjectIdentity
adGenEfmNtuTest = _AdGenEfmNtuTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 2, 4)
)
_AdGenEfmNtuPerformance_ObjectIdentity = ObjectIdentity
adGenEfmNtuPerformance = _AdGenEfmNtuPerformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 2, 5)
)
_AdGenEfmNtuPerfTable_Object = MibTable
adGenEfmNtuPerfTable = _AdGenEfmNtuPerfTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 2, 5, 1)
)
if mibBuilder.loadTexts:
    adGenEfmNtuPerfTable.setStatus("current")
_AdGenEfmNtuPerfEntry_Object = MibTableRow
adGenEfmNtuPerfEntry = _AdGenEfmNtuPerfEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 2, 5, 1, 1)
)
adGenEfmNtuPerfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adGenEfmNtuPerfEntry.setStatus("current")
_AdGenEfmNtuPerfCustIfTxOctets_Type = Gauge32
_AdGenEfmNtuPerfCustIfTxOctets_Object = MibTableColumn
adGenEfmNtuPerfCustIfTxOctets = _AdGenEfmNtuPerfCustIfTxOctets_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 2, 5, 1, 1, 1),
    _AdGenEfmNtuPerfCustIfTxOctets_Type()
)
adGenEfmNtuPerfCustIfTxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEfmNtuPerfCustIfTxOctets.setStatus("current")
_AdGenEfmNtuPerfCustIfTxFrames_Type = Gauge32
_AdGenEfmNtuPerfCustIfTxFrames_Object = MibTableColumn
adGenEfmNtuPerfCustIfTxFrames = _AdGenEfmNtuPerfCustIfTxFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 2, 5, 1, 1, 2),
    _AdGenEfmNtuPerfCustIfTxFrames_Type()
)
adGenEfmNtuPerfCustIfTxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEfmNtuPerfCustIfTxFrames.setStatus("current")
_AdGenEfmNtuPerfCustIfRxOctets_Type = Gauge32
_AdGenEfmNtuPerfCustIfRxOctets_Object = MibTableColumn
adGenEfmNtuPerfCustIfRxOctets = _AdGenEfmNtuPerfCustIfRxOctets_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 2, 5, 1, 1, 3),
    _AdGenEfmNtuPerfCustIfRxOctets_Type()
)
adGenEfmNtuPerfCustIfRxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEfmNtuPerfCustIfRxOctets.setStatus("current")
_AdGenEfmNtuPerfCustIfRxFrames_Type = Gauge32
_AdGenEfmNtuPerfCustIfRxFrames_Object = MibTableColumn
adGenEfmNtuPerfCustIfRxFrames = _AdGenEfmNtuPerfCustIfRxFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 2, 5, 1, 1, 4),
    _AdGenEfmNtuPerfCustIfRxFrames_Type()
)
adGenEfmNtuPerfCustIfRxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEfmNtuPerfCustIfRxFrames.setStatus("current")
_AdGenEfmNtuPerfCustIfRxErroredFrames_Type = Gauge32
_AdGenEfmNtuPerfCustIfRxErroredFrames_Object = MibTableColumn
adGenEfmNtuPerfCustIfRxErroredFrames = _AdGenEfmNtuPerfCustIfRxErroredFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 2, 5, 1, 1, 5),
    _AdGenEfmNtuPerfCustIfRxErroredFrames_Type()
)
adGenEfmNtuPerfCustIfRxErroredFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEfmNtuPerfCustIfRxErroredFrames.setStatus("current")
_AdGenEfmNtuPerfCustIfRxDiscardedFrames_Type = Gauge32
_AdGenEfmNtuPerfCustIfRxDiscardedFrames_Object = MibTableColumn
adGenEfmNtuPerfCustIfRxDiscardedFrames = _AdGenEfmNtuPerfCustIfRxDiscardedFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 2, 5, 1, 1, 6),
    _AdGenEfmNtuPerfCustIfRxDiscardedFrames_Type()
)
adGenEfmNtuPerfCustIfRxDiscardedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEfmNtuPerfCustIfRxDiscardedFrames.setStatus("current")
_AdGenEfmNtuMibConformance_ObjectIdentity = ObjectIdentity
adGenEfmNtuMibConformance = _AdGenEfmNtuMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 2, 7)
)
_AdGenEfmNtuMibGroups_ObjectIdentity = ObjectIdentity
adGenEfmNtuMibGroups = _AdGenEfmNtuMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 2, 7, 1)
)
_AdGenEfmNtuAlarmsPrefix_ObjectIdentity = ObjectIdentity
adGenEfmNtuAlarmsPrefix = _AdGenEfmNtuAlarmsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 2, 10)
)
_AdGenEfmNtuAlarms_ObjectIdentity = ObjectIdentity
adGenEfmNtuAlarms = _AdGenEfmNtuAlarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 2, 10, 0)
)

# Managed Objects groups

adGenEfmNtuProvGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 2, 7, 1, 1)
)
adGenEfmNtuProvGroup.setObjects(
      *(("ADTRAN-EFM-NTU-MIB", "adGenEfmNtuProvRestoreDefaults"),
        ("ADTRAN-EFM-NTU-MIB", "adGenEfmNtuProvReset"),
        ("ADTRAN-EFM-NTU-MIB", "adGenEfmNtuProvSwDownloadStart"),
        ("ADTRAN-EFM-NTU-MIB", "adGenEfmNtuProvSwDownloadFilename"),
        ("ADTRAN-EFM-NTU-MIB", "adGenEfmNtuProvSwDownloadStatus"),
        ("ADTRAN-EFM-NTU-MIB", "adGenEfmNtuProvCustId"),
        ("ADTRAN-EFM-NTU-MIB", "adGenEfmNtuProvCustIfAutoNeg"),
        ("ADTRAN-EFM-NTU-MIB", "adGenEfmNtuProvCustIfSpeed"),
        ("ADTRAN-EFM-NTU-MIB", "adGenEfmNtuProvCustIfDuplex"),
        ("ADTRAN-EFM-NTU-MIB", "adGenEfmNtuProvCustIfFlowControl"),
        ("ADTRAN-EFM-NTU-MIB", "adGenEfmNtuProvEnablePassword"),
        ("ADTRAN-EFM-NTU-MIB", "adGenEfmNtuProvMacTableSize"),
        ("ADTRAN-EFM-NTU-MIB", "adGenEfmNtuProvMacAging"),
        ("ADTRAN-EFM-NTU-MIB", "adGenEfmNtuProvLinkStateAware"),
        ("ADTRAN-EFM-NTU-MIB", "adGenEfmNtuAutoDiscoverMode"),
        ("ADTRAN-EFM-NTU-MIB", "adGenEfmNtuAutoDiscoverAck"))
)
if mibBuilder.loadTexts:
    adGenEfmNtuProvGroup.setStatus("current")

adGenEfmNtuProvCfmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 2, 7, 1, 2)
)
adGenEfmNtuProvCfmGroup.setObjects(
      *(("ADTRAN-EFM-NTU-MIB", "adGenEfmNtuProvCfmMdName"),
        ("ADTRAN-EFM-NTU-MIB", "adGenEfmNtuProvCfmMaName"),
        ("ADTRAN-EFM-NTU-MIB", "adGenEfmNtuProvCfmLocalMepId"),
        ("ADTRAN-EFM-NTU-MIB", "adGenEfmNtuProvCfmMdLevel"),
        ("ADTRAN-EFM-NTU-MIB", "adGenEfmNtuProvCfmVlanId"),
        ("ADTRAN-EFM-NTU-MIB", "adGenEfmNtuProvCfmCcmInterval"),
        ("ADTRAN-EFM-NTU-MIB", "adGenEfmNtuProvCfmMepTableNextIndex"))
)
if mibBuilder.loadTexts:
    adGenEfmNtuProvCfmGroup.setStatus("current")

adGenEfmNtuProvCfmMepGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 2, 7, 1, 3)
)
adGenEfmNtuProvCfmMepGroup.setObjects(
      *(("ADTRAN-EFM-NTU-MIB", "adGenEfmNtuProvCfmMepIndex"),
        ("ADTRAN-EFM-NTU-MIB", "adGenEfmNtuProvCfmMepId"),
        ("ADTRAN-EFM-NTU-MIB", "adGenEfmNtuProvCfmMepEntryStatus"))
)
if mibBuilder.loadTexts:
    adGenEfmNtuProvCfmMepGroup.setStatus("current")

adGenEfmNtuProvMgmtGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 2, 7, 1, 4)
)
adGenEfmNtuProvMgmtGroup.setObjects(
      *(("ADTRAN-EFM-NTU-MIB", "adGenEfmNtuProvMgmtIpAddress"),
        ("ADTRAN-EFM-NTU-MIB", "adGenEfmNtuProvMgmtIpSubnetMask"),
        ("ADTRAN-EFM-NTU-MIB", "adGenEfmNtuProvMgmtIpGateway"),
        ("ADTRAN-EFM-NTU-MIB", "adGenEfmNtuProvMgmtIpVlan"),
        ("ADTRAN-EFM-NTU-MIB", "adGenEfmNtuProvMgmtTftpServer"),
        ("ADTRAN-EFM-NTU-MIB", "adGenEfmNtuProvMgmtSysName"),
        ("ADTRAN-EFM-NTU-MIB", "adGenEfmNtuProvMgmtFarEndIfIndex"),
        ("ADTRAN-EFM-NTU-MIB", "adGenEfmNtuProvMgmtFarEndIpAddress"),
        ("ADTRAN-EFM-NTU-MIB", "adGenEfmNtuProvMgmtFarEndSysName"),
        ("ADTRAN-EFM-NTU-MIB", "adGenEfmNtuProvMgmtSnmpWriteCommunity"),
        ("ADTRAN-EFM-NTU-MIB", "adGenEfmNtuProvMgmtSnmpReadCommunity"),
        ("ADTRAN-EFM-NTU-MIB", "adGenEfmNtuProvMgmtPriority"),
        ("ADTRAN-EFM-NTU-MIB", "adGenEfmNtuProvMgmtSnmpSysLocation"),
        ("ADTRAN-EFM-NTU-MIB", "adGenEfmNtuProvMgmtEzProvHostOneIpAddress"),
        ("ADTRAN-EFM-NTU-MIB", "adGenEfmNtuProvMgmtEzProvHostOneTrapVersion"),
        ("ADTRAN-EFM-NTU-MIB", "adGenEfmNtuProvMgmtEzProvHostTwoIpAddress"),
        ("ADTRAN-EFM-NTU-MIB", "adGenEfmNtuProvMgmtEzProvHostTwoTrapVersion"),
        ("ADTRAN-EFM-NTU-MIB", "adGenEfmNtuProvMgmtEzProvEnabled"),
        ("ADTRAN-EFM-NTU-MIB", "adGenEfmNtuProvMgmtIpv6AddressPrefixLength"),
        ("ADTRAN-EFM-NTU-MIB", "adGenEfmNtuProvMgmtIpv6AddressEui64"),
        ("ADTRAN-EFM-NTU-MIB", "adGenEfmNtuProvMgmtIpv6Address"),
        ("ADTRAN-EFM-NTU-MIB", "adGenEfmNtuProvMgmtIpv6AddressLinkLocal"),
        ("ADTRAN-EFM-NTU-MIB", "adGenEfmNtuProvMgmtAutoConfigMode"),
        ("ADTRAN-EFM-NTU-MIB", "adGenEfmNtuProvMgmtAutoConfigFilename"),
        ("ADTRAN-EFM-NTU-MIB", "adGenEfmNtuProvMgmtAutoConfigGroupName"),
        ("ADTRAN-EFM-NTU-MIB", "adGenEfmNtuProvMgmtAutoConfigHostIpv4"),
        ("ADTRAN-EFM-NTU-MIB", "adGenEfmNtuProvMgmtAutoConfigHostIpv6"))
)
if mibBuilder.loadTexts:
    adGenEfmNtuProvMgmtGroup.setStatus("current")

adGenEfmNtuStatGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 2, 7, 1, 5)
)
adGenEfmNtuStatGroup.setObjects(
      *(("ADTRAN-EFM-NTU-MIB", "adGenEfmNtuStatUpTime"),
        ("ADTRAN-EFM-NTU-MIB", "adGenEfmNtuStatLinkStateAware"),
        ("ADTRAN-EFM-NTU-MIB", "adGenEfmNtuStatCustIf"))
)
if mibBuilder.loadTexts:
    adGenEfmNtuStatGroup.setStatus("current")

adGenEfmNtuPerfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 2, 7, 1, 6)
)
adGenEfmNtuPerfGroup.setObjects(
      *(("ADTRAN-EFM-NTU-MIB", "adGenEfmNtuPerfCustIfTxOctets"),
        ("ADTRAN-EFM-NTU-MIB", "adGenEfmNtuPerfCustIfTxFrames"),
        ("ADTRAN-EFM-NTU-MIB", "adGenEfmNtuPerfCustIfRxOctets"),
        ("ADTRAN-EFM-NTU-MIB", "adGenEfmNtuPerfCustIfRxFrames"),
        ("ADTRAN-EFM-NTU-MIB", "adGenEfmNtuPerfCustIfRxErroredFrames"),
        ("ADTRAN-EFM-NTU-MIB", "adGenEfmNtuPerfCustIfRxDiscardedFrames"))
)
if mibBuilder.loadTexts:
    adGenEfmNtuPerfGroup.setStatus("current")


# Notification objects

adGenEfmNtuCraftLoginSuccess = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 2, 10, 0, 1)
)
adGenEfmNtuCraftLoginSuccess.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-EFM-NTU-MIB", "adGenEfmNtuProvCustId"))
)
if mibBuilder.loadTexts:
    adGenEfmNtuCraftLoginSuccess.setStatus(
        "current"
    )

adGenEfmNtuCraftLoginFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 2, 10, 0, 2)
)
adGenEfmNtuCraftLoginFail.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-EFM-NTU-MIB", "adGenEfmNtuProvCustId"))
)
if mibBuilder.loadTexts:
    adGenEfmNtuCraftLoginFail.setStatus(
        "current"
    )

adGenEfmNtuSwDownloadFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 2, 10, 0, 3)
)
adGenEfmNtuSwDownloadFail.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-EFM-NTU-MIB", "adGenEfmNtuProvCustId"),
        ("ADTRAN-EFM-NTU-MIB", "adGenEfmNtuProvSwDownloadStatus"))
)
if mibBuilder.loadTexts:
    adGenEfmNtuSwDownloadFail.setStatus(
        "current"
    )

adGenEfmNtuCorruptConfiguration = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 2, 10, 0, 4)
)
adGenEfmNtuCorruptConfiguration.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-EFM-NTU-MIB", "adGenEfmNtuProvCustId"))
)
if mibBuilder.loadTexts:
    adGenEfmNtuCorruptConfiguration.setStatus(
        "current"
    )

adGenEfmNtuMACTableExhaust = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 2, 10, 0, 5)
)
adGenEfmNtuMACTableExhaust.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-EFM-NTU-MIB", "adGenEfmNtuProvCustId"))
)
if mibBuilder.loadTexts:
    adGenEfmNtuMACTableExhaust.setStatus(
        "current"
    )

adGenEfmNtuCustIfDownClr = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 2, 10, 0, 10)
)
adGenEfmNtuCustIfDownClr.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-EFM-NTU-MIB", "adGenEfmNtuProvCustId"))
)
if mibBuilder.loadTexts:
    adGenEfmNtuCustIfDownClr.setStatus(
        "current"
    )

adGenEfmNtuCustIfDownAct = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 2, 10, 0, 11)
)
adGenEfmNtuCustIfDownAct.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-EFM-NTU-MIB", "adGenEfmNtuProvCustId"))
)
if mibBuilder.loadTexts:
    adGenEfmNtuCustIfDownAct.setStatus(
        "current"
    )

adGenEfmNtuAutoDiscover = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 2, 10, 0, 12)
)
adGenEfmNtuAutoDiscover.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("IF-MIB", "ifDescr"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenEfmNtuAutoDiscover.setStatus(
        "current"
    )


# Notifications groups

adGenEfmNtuEventGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 2, 7, 1, 7)
)
adGenEfmNtuEventGroup.setObjects(
      *(("ADTRAN-EFM-NTU-MIB", "adGenEfmNtuCraftLoginSuccess"),
        ("ADTRAN-EFM-NTU-MIB", "adGenEfmNtuCraftLoginFail"),
        ("ADTRAN-EFM-NTU-MIB", "adGenEfmNtuSwDownloadFail"),
        ("ADTRAN-EFM-NTU-MIB", "adGenEfmNtuCorruptConfiguration"),
        ("ADTRAN-EFM-NTU-MIB", "adGenEfmNtuMACTableExhaust"),
        ("ADTRAN-EFM-NTU-MIB", "adGenEfmNtuCustIfDownClr"),
        ("ADTRAN-EFM-NTU-MIB", "adGenEfmNtuCustIfDownAct"),
        ("ADTRAN-EFM-NTU-MIB", "adGenEfmNtuAutoDiscover"))
)
if mibBuilder.loadTexts:
    adGenEfmNtuEventGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ADTRAN-EFM-NTU-MIB",
    **{"adGenEfmNtuConfiguration": adGenEfmNtuConfiguration,
       "adGenEfmNtuProvisioning": adGenEfmNtuProvisioning,
       "adGenEfmNtuProvTable": adGenEfmNtuProvTable,
       "adGenEfmNtuProvEntry": adGenEfmNtuProvEntry,
       "adGenEfmNtuProvRestoreDefaults": adGenEfmNtuProvRestoreDefaults,
       "adGenEfmNtuProvReset": adGenEfmNtuProvReset,
       "adGenEfmNtuProvSwDownloadStart": adGenEfmNtuProvSwDownloadStart,
       "adGenEfmNtuProvSwDownloadFilename": adGenEfmNtuProvSwDownloadFilename,
       "adGenEfmNtuProvSwDownloadStatus": adGenEfmNtuProvSwDownloadStatus,
       "adGenEfmNtuProvCustId": adGenEfmNtuProvCustId,
       "adGenEfmNtuProvCustIfAutoNeg": adGenEfmNtuProvCustIfAutoNeg,
       "adGenEfmNtuProvCustIfSpeed": adGenEfmNtuProvCustIfSpeed,
       "adGenEfmNtuProvCustIfDuplex": adGenEfmNtuProvCustIfDuplex,
       "adGenEfmNtuProvCustIfFlowControl": adGenEfmNtuProvCustIfFlowControl,
       "adGenEfmNtuProvEnablePassword": adGenEfmNtuProvEnablePassword,
       "adGenEfmNtuProvMacTableSize": adGenEfmNtuProvMacTableSize,
       "adGenEfmNtuProvMacAging": adGenEfmNtuProvMacAging,
       "adGenEfmNtuProvLinkStateAware": adGenEfmNtuProvLinkStateAware,
       "adGenEfmNtuAutoDiscoverMode": adGenEfmNtuAutoDiscoverMode,
       "adGenEfmNtuAutoDiscoverAck": adGenEfmNtuAutoDiscoverAck,
       "adGenEfmNtuProvCfmTable": adGenEfmNtuProvCfmTable,
       "adGenEfmNtuProvCfmEntry": adGenEfmNtuProvCfmEntry,
       "adGenEfmNtuProvCfmMdName": adGenEfmNtuProvCfmMdName,
       "adGenEfmNtuProvCfmMaName": adGenEfmNtuProvCfmMaName,
       "adGenEfmNtuProvCfmLocalMepId": adGenEfmNtuProvCfmLocalMepId,
       "adGenEfmNtuProvCfmMdLevel": adGenEfmNtuProvCfmMdLevel,
       "adGenEfmNtuProvCfmVlanId": adGenEfmNtuProvCfmVlanId,
       "adGenEfmNtuProvCfmCcmInterval": adGenEfmNtuProvCfmCcmInterval,
       "adGenEfmNtuProvCfmMepTableNextIndex": adGenEfmNtuProvCfmMepTableNextIndex,
       "adGenEfmNtuProvCfmMepTable": adGenEfmNtuProvCfmMepTable,
       "adGenEfmNtuProvCfmMepEntry": adGenEfmNtuProvCfmMepEntry,
       "adGenEfmNtuProvCfmMepIndex": adGenEfmNtuProvCfmMepIndex,
       "adGenEfmNtuProvCfmMepId": adGenEfmNtuProvCfmMepId,
       "adGenEfmNtuProvCfmMepEntryStatus": adGenEfmNtuProvCfmMepEntryStatus,
       "adGenEfmNtuProvMgmtIpTable": adGenEfmNtuProvMgmtIpTable,
       "adGenEfmNtuProvMgmtIpEntry": adGenEfmNtuProvMgmtIpEntry,
       "adGenEfmNtuProvMgmtIpAddress": adGenEfmNtuProvMgmtIpAddress,
       "adGenEfmNtuProvMgmtIpSubnetMask": adGenEfmNtuProvMgmtIpSubnetMask,
       "adGenEfmNtuProvMgmtIpGateway": adGenEfmNtuProvMgmtIpGateway,
       "adGenEfmNtuProvMgmtIpVlan": adGenEfmNtuProvMgmtIpVlan,
       "adGenEfmNtuProvMgmtTftpServer": adGenEfmNtuProvMgmtTftpServer,
       "adGenEfmNtuProvMgmtSnmpWriteCommunity": adGenEfmNtuProvMgmtSnmpWriteCommunity,
       "adGenEfmNtuProvMgmtSnmpReadCommunity": adGenEfmNtuProvMgmtSnmpReadCommunity,
       "adGenEfmNtuProvMgmtSysName": adGenEfmNtuProvMgmtSysName,
       "adGenEfmNtuProvMgmtFarEndIfIndex": adGenEfmNtuProvMgmtFarEndIfIndex,
       "adGenEfmNtuProvMgmtFarEndIpAddress": adGenEfmNtuProvMgmtFarEndIpAddress,
       "adGenEfmNtuProvMgmtFarEndSysName": adGenEfmNtuProvMgmtFarEndSysName,
       "adGenEfmNtuProvMgmtPriority": adGenEfmNtuProvMgmtPriority,
       "adGenEfmNtuProvMgmtSnmpSysLocation": adGenEfmNtuProvMgmtSnmpSysLocation,
       "adGenEfmNtuProvMgmtEzProvHostOneIpAddress": adGenEfmNtuProvMgmtEzProvHostOneIpAddress,
       "adGenEfmNtuProvMgmtEzProvHostOneTrapVersion": adGenEfmNtuProvMgmtEzProvHostOneTrapVersion,
       "adGenEfmNtuProvMgmtEzProvHostTwoIpAddress": adGenEfmNtuProvMgmtEzProvHostTwoIpAddress,
       "adGenEfmNtuProvMgmtEzProvHostTwoTrapVersion": adGenEfmNtuProvMgmtEzProvHostTwoTrapVersion,
       "adGenEfmNtuProvMgmtEzProvEnabled": adGenEfmNtuProvMgmtEzProvEnabled,
       "adGenEfmNtuProvMgmtIpv6AddressPrefixLength": adGenEfmNtuProvMgmtIpv6AddressPrefixLength,
       "adGenEfmNtuProvMgmtIpv6AddressEui64": adGenEfmNtuProvMgmtIpv6AddressEui64,
       "adGenEfmNtuProvMgmtIpv6Address": adGenEfmNtuProvMgmtIpv6Address,
       "adGenEfmNtuProvMgmtIpv6AddressLinkLocal": adGenEfmNtuProvMgmtIpv6AddressLinkLocal,
       "adGenEfmNtuProvMgmtAutoConfigMode": adGenEfmNtuProvMgmtAutoConfigMode,
       "adGenEfmNtuProvMgmtAutoConfigFilename": adGenEfmNtuProvMgmtAutoConfigFilename,
       "adGenEfmNtuProvMgmtAutoConfigGroupName": adGenEfmNtuProvMgmtAutoConfigGroupName,
       "adGenEfmNtuProvMgmtAutoConfigHostIpv4": adGenEfmNtuProvMgmtAutoConfigHostIpv4,
       "adGenEfmNtuProvMgmtAutoConfigHostIpv6": adGenEfmNtuProvMgmtAutoConfigHostIpv6,
       "adGenEfmNtuStatus": adGenEfmNtuStatus,
       "adGenEfmNtuStatTable": adGenEfmNtuStatTable,
       "adGenEfmNtuStatEntry": adGenEfmNtuStatEntry,
       "adGenEfmNtuStatUpTime": adGenEfmNtuStatUpTime,
       "adGenEfmNtuStatLinkStateAware": adGenEfmNtuStatLinkStateAware,
       "adGenEfmNtuStatCustIf": adGenEfmNtuStatCustIf,
       "adGenEfmNtuTest": adGenEfmNtuTest,
       "adGenEfmNtuPerformance": adGenEfmNtuPerformance,
       "adGenEfmNtuPerfTable": adGenEfmNtuPerfTable,
       "adGenEfmNtuPerfEntry": adGenEfmNtuPerfEntry,
       "adGenEfmNtuPerfCustIfTxOctets": adGenEfmNtuPerfCustIfTxOctets,
       "adGenEfmNtuPerfCustIfTxFrames": adGenEfmNtuPerfCustIfTxFrames,
       "adGenEfmNtuPerfCustIfRxOctets": adGenEfmNtuPerfCustIfRxOctets,
       "adGenEfmNtuPerfCustIfRxFrames": adGenEfmNtuPerfCustIfRxFrames,
       "adGenEfmNtuPerfCustIfRxErroredFrames": adGenEfmNtuPerfCustIfRxErroredFrames,
       "adGenEfmNtuPerfCustIfRxDiscardedFrames": adGenEfmNtuPerfCustIfRxDiscardedFrames,
       "adGenEfmNtuMibConformance": adGenEfmNtuMibConformance,
       "adGenEfmNtuMibGroups": adGenEfmNtuMibGroups,
       "adGenEfmNtuProvGroup": adGenEfmNtuProvGroup,
       "adGenEfmNtuProvCfmGroup": adGenEfmNtuProvCfmGroup,
       "adGenEfmNtuProvCfmMepGroup": adGenEfmNtuProvCfmMepGroup,
       "adGenEfmNtuProvMgmtGroup": adGenEfmNtuProvMgmtGroup,
       "adGenEfmNtuStatGroup": adGenEfmNtuStatGroup,
       "adGenEfmNtuPerfGroup": adGenEfmNtuPerfGroup,
       "adGenEfmNtuEventGroup": adGenEfmNtuEventGroup,
       "adGenEfmNtuAlarmsPrefix": adGenEfmNtuAlarmsPrefix,
       "adGenEfmNtuAlarms": adGenEfmNtuAlarms,
       "adGenEfmNtuCraftLoginSuccess": adGenEfmNtuCraftLoginSuccess,
       "adGenEfmNtuCraftLoginFail": adGenEfmNtuCraftLoginFail,
       "adGenEfmNtuSwDownloadFail": adGenEfmNtuSwDownloadFail,
       "adGenEfmNtuCorruptConfiguration": adGenEfmNtuCorruptConfiguration,
       "adGenEfmNtuMACTableExhaust": adGenEfmNtuMACTableExhaust,
       "adGenEfmNtuCustIfDownClr": adGenEfmNtuCustIfDownClr,
       "adGenEfmNtuCustIfDownAct": adGenEfmNtuCustIfDownAct,
       "adGenEfmNtuAutoDiscover": adGenEfmNtuAutoDiscover,
       "adGenEfmNtuMIB": adGenEfmNtuMIB}
)
