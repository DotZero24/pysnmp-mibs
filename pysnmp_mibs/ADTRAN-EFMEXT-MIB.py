# SNMP MIB module (ADTRAN-EFMEXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/adtran/ADTRAN-EFMEXT-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:29:51 2025
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

(adGenSlotInfoIndex,) = mibBuilder.importSymbols(
    "ADTRAN-GENSLOT-MIB",
    "adGenSlotInfoIndex")

(adTrapInformSeqNum,) = mibBuilder.importSymbols(
    "ADTRAN-GENTRAPINFORM-MIB",
    "adTrapInformSeqNum")

(adGenEfmExt,
 adGenEfmExtID) = mibBuilder.importSymbols(
    "ADTRAN-SHARED-EFM-MIB",
    "adGenEfmExt",
    "adGenEfmExtID")

(ifDescr,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifDescr",
    "ifIndex")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

adGenEfmExtMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 66, 3, 1)
)
if mibBuilder.loadTexts:
    adGenEfmExtMIB.setRevisions(
        ("2011-09-28 00:00",
         "2011-08-10 00:00",
         "2011-04-14 00:00",
         "2008-03-24 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AdGenEfmExtStatus_ObjectIdentity = ObjectIdentity
adGenEfmExtStatus = _AdGenEfmExtStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 3, 1)
)
_AdGenEfmExtStatGroupTable_Object = MibTable
adGenEfmExtStatGroupTable = _AdGenEfmExtStatGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 3, 1, 1)
)
if mibBuilder.loadTexts:
    adGenEfmExtStatGroupTable.setStatus("current")
_AdGenEfmExtStatGroupEntry_Object = MibTableRow
adGenEfmExtStatGroupEntry = _AdGenEfmExtStatGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 3, 1, 1, 1)
)
adGenEfmExtStatGroupEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adGenEfmExtStatGroupEntry.setStatus("current")


class _AdGenEfmExtStatGroupStatus_Type(Integer32):
    """Custom type adGenEfmExtStatGroupStatus based on Integer32"""
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
          ("testing", 3),
          ("noLinksInGroup", 4),
          ("upPartial", 5))
    )


_AdGenEfmExtStatGroupStatus_Type.__name__ = "Integer32"
_AdGenEfmExtStatGroupStatus_Object = MibTableColumn
adGenEfmExtStatGroupStatus = _AdGenEfmExtStatGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 3, 1, 1, 1, 1),
    _AdGenEfmExtStatGroupStatus_Type()
)
adGenEfmExtStatGroupStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEfmExtStatGroupStatus.setStatus("current")
_AdGenEfmExtStatGroupSize_Type = Integer32
_AdGenEfmExtStatGroupSize_Object = MibTableColumn
adGenEfmExtStatGroupSize = _AdGenEfmExtStatGroupSize_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 3, 1, 1, 1, 2),
    _AdGenEfmExtStatGroupSize_Type()
)
adGenEfmExtStatGroupSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEfmExtStatGroupSize.setStatus("current")
_AdGenEfmExtStatGroupNumActiveLinks_Type = Integer32
_AdGenEfmExtStatGroupNumActiveLinks_Object = MibTableColumn
adGenEfmExtStatGroupNumActiveLinks = _AdGenEfmExtStatGroupNumActiveLinks_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 3, 1, 1, 1, 3),
    _AdGenEfmExtStatGroupNumActiveLinks_Type()
)
adGenEfmExtStatGroupNumActiveLinks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEfmExtStatGroupNumActiveLinks.setStatus("current")
_AdGenEfmExtStatGroupUAS_Type = Gauge32
_AdGenEfmExtStatGroupUAS_Object = MibTableColumn
adGenEfmExtStatGroupUAS = _AdGenEfmExtStatGroupUAS_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 3, 1, 1, 1, 4),
    _AdGenEfmExtStatGroupUAS_Type()
)
adGenEfmExtStatGroupUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEfmExtStatGroupUAS.setStatus("current")
_AdGenEfmExtStatGroupFailures_Type = Gauge32
_AdGenEfmExtStatGroupFailures_Object = MibTableColumn
adGenEfmExtStatGroupFailures = _AdGenEfmExtStatGroupFailures_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 3, 1, 1, 1, 5),
    _AdGenEfmExtStatGroupFailures_Type()
)
adGenEfmExtStatGroupFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEfmExtStatGroupFailures.setStatus("current")
_AdGenEfmExtStatLinkTable_Object = MibTable
adGenEfmExtStatLinkTable = _AdGenEfmExtStatLinkTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 3, 1, 2)
)
if mibBuilder.loadTexts:
    adGenEfmExtStatLinkTable.setStatus("current")
_AdGenEfmExtStatLinkEntry_Object = MibTableRow
adGenEfmExtStatLinkEntry = _AdGenEfmExtStatLinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 3, 1, 2, 1)
)
adGenEfmExtStatLinkEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adGenEfmExtStatLinkEntry.setStatus("current")


class _AdGenEfmExtStatLinkNeTcSync_Type(Integer32):
    """Custom type adGenEfmExtStatLinkNeTcSync based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_AdGenEfmExtStatLinkNeTcSync_Type.__name__ = "Integer32"
_AdGenEfmExtStatLinkNeTcSync_Object = MibTableColumn
adGenEfmExtStatLinkNeTcSync = _AdGenEfmExtStatLinkNeTcSync_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 3, 1, 2, 1, 1),
    _AdGenEfmExtStatLinkNeTcSync_Type()
)
adGenEfmExtStatLinkNeTcSync.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEfmExtStatLinkNeTcSync.setStatus("current")


class _AdGenEfmExtStatLinkFeTcSync_Type(Integer32):
    """Custom type adGenEfmExtStatLinkFeTcSync based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_AdGenEfmExtStatLinkFeTcSync_Type.__name__ = "Integer32"
_AdGenEfmExtStatLinkFeTcSync_Object = MibTableColumn
adGenEfmExtStatLinkFeTcSync = _AdGenEfmExtStatLinkFeTcSync_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 3, 1, 2, 1, 2),
    _AdGenEfmExtStatLinkFeTcSync_Type()
)
adGenEfmExtStatLinkFeTcSync.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEfmExtStatLinkFeTcSync.setStatus("current")
_AdGenEfmExtStatLinkSkew_Type = Integer32
_AdGenEfmExtStatLinkSkew_Object = MibTableColumn
adGenEfmExtStatLinkSkew = _AdGenEfmExtStatLinkSkew_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 3, 1, 2, 1, 3),
    _AdGenEfmExtStatLinkSkew_Type()
)
adGenEfmExtStatLinkSkew.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEfmExtStatLinkSkew.setStatus("current")
_AdGenEfmExtStatLinkStatus_Type = DisplayString
_AdGenEfmExtStatLinkStatus_Object = MibTableColumn
adGenEfmExtStatLinkStatus = _AdGenEfmExtStatLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 3, 1, 2, 1, 4),
    _AdGenEfmExtStatLinkStatus_Type()
)
adGenEfmExtStatLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEfmExtStatLinkStatus.setStatus("current")
_AdGenEfmExtStatLinkFeId_Type = Integer32
_AdGenEfmExtStatLinkFeId_Object = MibTableColumn
adGenEfmExtStatLinkFeId = _AdGenEfmExtStatLinkFeId_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 3, 1, 2, 1, 5),
    _AdGenEfmExtStatLinkFeId_Type()
)
adGenEfmExtStatLinkFeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEfmExtStatLinkFeId.setStatus("current")
_AdGenEfmExtMibConformance_ObjectIdentity = ObjectIdentity
adGenEfmExtMibConformance = _AdGenEfmExtMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 3, 2)
)
_AdGenEfmExtMibGroups_ObjectIdentity = ObjectIdentity
adGenEfmExtMibGroups = _AdGenEfmExtMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 3, 2, 1)
)
_AdGenEfmExtPerformance_ObjectIdentity = ObjectIdentity
adGenEfmExtPerformance = _AdGenEfmExtPerformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 3, 3)
)
_AdGenEfmExtPerfPortCurr15MinTable_Object = MibTable
adGenEfmExtPerfPortCurr15MinTable = _AdGenEfmExtPerfPortCurr15MinTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 3, 3, 1)
)
if mibBuilder.loadTexts:
    adGenEfmExtPerfPortCurr15MinTable.setStatus("current")
_AdGenEfmExtPerfPortCurr15MinEntry_Object = MibTableRow
adGenEfmExtPerfPortCurr15MinEntry = _AdGenEfmExtPerfPortCurr15MinEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 3, 3, 1, 1)
)
adGenEfmExtPerfPortCurr15MinEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adGenEfmExtPerfPortCurr15MinEntry.setStatus("current")
_AdGenEfmExtPerfPort15MinValidIntervals_Type = Integer32
_AdGenEfmExtPerfPort15MinValidIntervals_Object = MibTableColumn
adGenEfmExtPerfPort15MinValidIntervals = _AdGenEfmExtPerfPort15MinValidIntervals_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 3, 3, 1, 1, 1),
    _AdGenEfmExtPerfPort15MinValidIntervals_Type()
)
adGenEfmExtPerfPort15MinValidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEfmExtPerfPort15MinValidIntervals.setStatus("current")
_AdGenEfmExtPerfPortCurr15MinTxOctets_Type = Gauge32
_AdGenEfmExtPerfPortCurr15MinTxOctets_Object = MibTableColumn
adGenEfmExtPerfPortCurr15MinTxOctets = _AdGenEfmExtPerfPortCurr15MinTxOctets_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 3, 3, 1, 1, 2),
    _AdGenEfmExtPerfPortCurr15MinTxOctets_Type()
)
adGenEfmExtPerfPortCurr15MinTxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEfmExtPerfPortCurr15MinTxOctets.setStatus("current")
_AdGenEfmExtPerfPortCurr15MinTxFrames_Type = Gauge32
_AdGenEfmExtPerfPortCurr15MinTxFrames_Object = MibTableColumn
adGenEfmExtPerfPortCurr15MinTxFrames = _AdGenEfmExtPerfPortCurr15MinTxFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 3, 3, 1, 1, 3),
    _AdGenEfmExtPerfPortCurr15MinTxFrames_Type()
)
adGenEfmExtPerfPortCurr15MinTxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEfmExtPerfPortCurr15MinTxFrames.setStatus("current")
_AdGenEfmExtPerfPortCurr15MinRxOctets_Type = Gauge32
_AdGenEfmExtPerfPortCurr15MinRxOctets_Object = MibTableColumn
adGenEfmExtPerfPortCurr15MinRxOctets = _AdGenEfmExtPerfPortCurr15MinRxOctets_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 3, 3, 1, 1, 4),
    _AdGenEfmExtPerfPortCurr15MinRxOctets_Type()
)
adGenEfmExtPerfPortCurr15MinRxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEfmExtPerfPortCurr15MinRxOctets.setStatus("current")
_AdGenEfmExtPerfPortCurr15MinRxFrames_Type = Gauge32
_AdGenEfmExtPerfPortCurr15MinRxFrames_Object = MibTableColumn
adGenEfmExtPerfPortCurr15MinRxFrames = _AdGenEfmExtPerfPortCurr15MinRxFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 3, 3, 1, 1, 5),
    _AdGenEfmExtPerfPortCurr15MinRxFrames_Type()
)
adGenEfmExtPerfPortCurr15MinRxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEfmExtPerfPortCurr15MinRxFrames.setStatus("current")
_AdGenEfmExtPerfPortCurr15MinRxCodingErrors_Type = Gauge32
_AdGenEfmExtPerfPortCurr15MinRxCodingErrors_Object = MibTableColumn
adGenEfmExtPerfPortCurr15MinRxCodingErrors = _AdGenEfmExtPerfPortCurr15MinRxCodingErrors_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 3, 3, 1, 1, 6),
    _AdGenEfmExtPerfPortCurr15MinRxCodingErrors_Type()
)
adGenEfmExtPerfPortCurr15MinRxCodingErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEfmExtPerfPortCurr15MinRxCodingErrors.setStatus("current")
_AdGenEfmExtPerfPort15MinIntTable_Object = MibTable
adGenEfmExtPerfPort15MinIntTable = _AdGenEfmExtPerfPort15MinIntTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 3, 3, 2)
)
if mibBuilder.loadTexts:
    adGenEfmExtPerfPort15MinIntTable.setStatus("current")
_AdGenEfmExtPerfPort15MinIntEntry_Object = MibTableRow
adGenEfmExtPerfPort15MinIntEntry = _AdGenEfmExtPerfPort15MinIntEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 3, 3, 2, 1)
)
adGenEfmExtPerfPort15MinIntEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ADTRAN-EFMEXT-MIB", "adGenEfmExtPerfPort15MinIntNumber"),
)
if mibBuilder.loadTexts:
    adGenEfmExtPerfPort15MinIntEntry.setStatus("current")
_AdGenEfmExtPerfPort15MinIntNumber_Type = Integer32
_AdGenEfmExtPerfPort15MinIntNumber_Object = MibTableColumn
adGenEfmExtPerfPort15MinIntNumber = _AdGenEfmExtPerfPort15MinIntNumber_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 3, 3, 2, 1, 1),
    _AdGenEfmExtPerfPort15MinIntNumber_Type()
)
adGenEfmExtPerfPort15MinIntNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEfmExtPerfPort15MinIntNumber.setStatus("current")
_AdGenEfmExtPerfPort15MinIntTxOctets_Type = Gauge32
_AdGenEfmExtPerfPort15MinIntTxOctets_Object = MibTableColumn
adGenEfmExtPerfPort15MinIntTxOctets = _AdGenEfmExtPerfPort15MinIntTxOctets_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 3, 3, 2, 1, 2),
    _AdGenEfmExtPerfPort15MinIntTxOctets_Type()
)
adGenEfmExtPerfPort15MinIntTxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEfmExtPerfPort15MinIntTxOctets.setStatus("current")
_AdGenEfmExtPerfPort15MinIntTxFrames_Type = Gauge32
_AdGenEfmExtPerfPort15MinIntTxFrames_Object = MibTableColumn
adGenEfmExtPerfPort15MinIntTxFrames = _AdGenEfmExtPerfPort15MinIntTxFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 3, 3, 2, 1, 3),
    _AdGenEfmExtPerfPort15MinIntTxFrames_Type()
)
adGenEfmExtPerfPort15MinIntTxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEfmExtPerfPort15MinIntTxFrames.setStatus("current")
_AdGenEfmExtPerfPort15MinIntRxOctets_Type = Gauge32
_AdGenEfmExtPerfPort15MinIntRxOctets_Object = MibTableColumn
adGenEfmExtPerfPort15MinIntRxOctets = _AdGenEfmExtPerfPort15MinIntRxOctets_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 3, 3, 2, 1, 4),
    _AdGenEfmExtPerfPort15MinIntRxOctets_Type()
)
adGenEfmExtPerfPort15MinIntRxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEfmExtPerfPort15MinIntRxOctets.setStatus("current")
_AdGenEfmExtPerfPort15MinIntRxFrames_Type = Gauge32
_AdGenEfmExtPerfPort15MinIntRxFrames_Object = MibTableColumn
adGenEfmExtPerfPort15MinIntRxFrames = _AdGenEfmExtPerfPort15MinIntRxFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 3, 3, 2, 1, 5),
    _AdGenEfmExtPerfPort15MinIntRxFrames_Type()
)
adGenEfmExtPerfPort15MinIntRxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEfmExtPerfPort15MinIntRxFrames.setStatus("current")
_AdGenEfmExtPerfPort15MinIntRxCodingErrors_Type = Gauge32
_AdGenEfmExtPerfPort15MinIntRxCodingErrors_Object = MibTableColumn
adGenEfmExtPerfPort15MinIntRxCodingErrors = _AdGenEfmExtPerfPort15MinIntRxCodingErrors_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 3, 3, 2, 1, 6),
    _AdGenEfmExtPerfPort15MinIntRxCodingErrors_Type()
)
adGenEfmExtPerfPort15MinIntRxCodingErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEfmExtPerfPort15MinIntRxCodingErrors.setStatus("current")
_AdGenEfmExtPerfPortCurr24HrTable_Object = MibTable
adGenEfmExtPerfPortCurr24HrTable = _AdGenEfmExtPerfPortCurr24HrTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 3, 3, 3)
)
if mibBuilder.loadTexts:
    adGenEfmExtPerfPortCurr24HrTable.setStatus("current")
_AdGenEfmExtPerfPortCurr24HrEntry_Object = MibTableRow
adGenEfmExtPerfPortCurr24HrEntry = _AdGenEfmExtPerfPortCurr24HrEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 3, 3, 3, 1)
)
adGenEfmExtPerfPortCurr24HrEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adGenEfmExtPerfPortCurr24HrEntry.setStatus("current")
_AdGenEfmExtPerfPort24HrValidIntervals_Type = Integer32
_AdGenEfmExtPerfPort24HrValidIntervals_Object = MibTableColumn
adGenEfmExtPerfPort24HrValidIntervals = _AdGenEfmExtPerfPort24HrValidIntervals_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 3, 3, 3, 1, 1),
    _AdGenEfmExtPerfPort24HrValidIntervals_Type()
)
adGenEfmExtPerfPort24HrValidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEfmExtPerfPort24HrValidIntervals.setStatus("current")
_AdGenEfmExtPerfPortCurr24HrTxOctets_Type = Gauge32
_AdGenEfmExtPerfPortCurr24HrTxOctets_Object = MibTableColumn
adGenEfmExtPerfPortCurr24HrTxOctets = _AdGenEfmExtPerfPortCurr24HrTxOctets_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 3, 3, 3, 1, 2),
    _AdGenEfmExtPerfPortCurr24HrTxOctets_Type()
)
adGenEfmExtPerfPortCurr24HrTxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEfmExtPerfPortCurr24HrTxOctets.setStatus("current")
_AdGenEfmExtPerfPortCurr24HrTxFrames_Type = Gauge32
_AdGenEfmExtPerfPortCurr24HrTxFrames_Object = MibTableColumn
adGenEfmExtPerfPortCurr24HrTxFrames = _AdGenEfmExtPerfPortCurr24HrTxFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 3, 3, 3, 1, 3),
    _AdGenEfmExtPerfPortCurr24HrTxFrames_Type()
)
adGenEfmExtPerfPortCurr24HrTxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEfmExtPerfPortCurr24HrTxFrames.setStatus("current")
_AdGenEfmExtPerfPortCurr24HrRxOctets_Type = Gauge32
_AdGenEfmExtPerfPortCurr24HrRxOctets_Object = MibTableColumn
adGenEfmExtPerfPortCurr24HrRxOctets = _AdGenEfmExtPerfPortCurr24HrRxOctets_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 3, 3, 3, 1, 4),
    _AdGenEfmExtPerfPortCurr24HrRxOctets_Type()
)
adGenEfmExtPerfPortCurr24HrRxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEfmExtPerfPortCurr24HrRxOctets.setStatus("current")
_AdGenEfmExtPerfPortCurr24HrRxFrames_Type = Gauge32
_AdGenEfmExtPerfPortCurr24HrRxFrames_Object = MibTableColumn
adGenEfmExtPerfPortCurr24HrRxFrames = _AdGenEfmExtPerfPortCurr24HrRxFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 3, 3, 3, 1, 5),
    _AdGenEfmExtPerfPortCurr24HrRxFrames_Type()
)
adGenEfmExtPerfPortCurr24HrRxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEfmExtPerfPortCurr24HrRxFrames.setStatus("current")
_AdGenEfmExtPerfPortCurr24HrRxCodingErrors_Type = Gauge32
_AdGenEfmExtPerfPortCurr24HrRxCodingErrors_Object = MibTableColumn
adGenEfmExtPerfPortCurr24HrRxCodingErrors = _AdGenEfmExtPerfPortCurr24HrRxCodingErrors_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 3, 3, 3, 1, 6),
    _AdGenEfmExtPerfPortCurr24HrRxCodingErrors_Type()
)
adGenEfmExtPerfPortCurr24HrRxCodingErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEfmExtPerfPortCurr24HrRxCodingErrors.setStatus("current")
_AdGenEfmExtPerfPort24HrIntTable_Object = MibTable
adGenEfmExtPerfPort24HrIntTable = _AdGenEfmExtPerfPort24HrIntTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 3, 3, 4)
)
if mibBuilder.loadTexts:
    adGenEfmExtPerfPort24HrIntTable.setStatus("current")
_AdGenEfmExtPerfPort24HrIntEntry_Object = MibTableRow
adGenEfmExtPerfPort24HrIntEntry = _AdGenEfmExtPerfPort24HrIntEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 3, 3, 4, 1)
)
adGenEfmExtPerfPort24HrIntEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ADTRAN-EFMEXT-MIB", "adGenEfmExtPerfPort24HrIntNumber"),
)
if mibBuilder.loadTexts:
    adGenEfmExtPerfPort24HrIntEntry.setStatus("current")
_AdGenEfmExtPerfPort24HrIntNumber_Type = Integer32
_AdGenEfmExtPerfPort24HrIntNumber_Object = MibTableColumn
adGenEfmExtPerfPort24HrIntNumber = _AdGenEfmExtPerfPort24HrIntNumber_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 3, 3, 4, 1, 1),
    _AdGenEfmExtPerfPort24HrIntNumber_Type()
)
adGenEfmExtPerfPort24HrIntNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEfmExtPerfPort24HrIntNumber.setStatus("current")
_AdGenEfmExtPerfPort24HrIntTxOctets_Type = Gauge32
_AdGenEfmExtPerfPort24HrIntTxOctets_Object = MibTableColumn
adGenEfmExtPerfPort24HrIntTxOctets = _AdGenEfmExtPerfPort24HrIntTxOctets_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 3, 3, 4, 1, 2),
    _AdGenEfmExtPerfPort24HrIntTxOctets_Type()
)
adGenEfmExtPerfPort24HrIntTxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEfmExtPerfPort24HrIntTxOctets.setStatus("current")
_AdGenEfmExtPerfPort24HrIntTxFrames_Type = Gauge32
_AdGenEfmExtPerfPort24HrIntTxFrames_Object = MibTableColumn
adGenEfmExtPerfPort24HrIntTxFrames = _AdGenEfmExtPerfPort24HrIntTxFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 3, 3, 4, 1, 3),
    _AdGenEfmExtPerfPort24HrIntTxFrames_Type()
)
adGenEfmExtPerfPort24HrIntTxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEfmExtPerfPort24HrIntTxFrames.setStatus("current")
_AdGenEfmExtPerfPort24HrIntRxOctets_Type = Gauge32
_AdGenEfmExtPerfPort24HrIntRxOctets_Object = MibTableColumn
adGenEfmExtPerfPort24HrIntRxOctets = _AdGenEfmExtPerfPort24HrIntRxOctets_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 3, 3, 4, 1, 4),
    _AdGenEfmExtPerfPort24HrIntRxOctets_Type()
)
adGenEfmExtPerfPort24HrIntRxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEfmExtPerfPort24HrIntRxOctets.setStatus("current")
_AdGenEfmExtPerfPort24HrIntRxFrames_Type = Gauge32
_AdGenEfmExtPerfPort24HrIntRxFrames_Object = MibTableColumn
adGenEfmExtPerfPort24HrIntRxFrames = _AdGenEfmExtPerfPort24HrIntRxFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 3, 3, 4, 1, 5),
    _AdGenEfmExtPerfPort24HrIntRxFrames_Type()
)
adGenEfmExtPerfPort24HrIntRxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEfmExtPerfPort24HrIntRxFrames.setStatus("current")
_AdGenEfmExtPerfPort24HrIntRxCodingErrors_Type = Gauge32
_AdGenEfmExtPerfPort24HrIntRxCodingErrors_Object = MibTableColumn
adGenEfmExtPerfPort24HrIntRxCodingErrors = _AdGenEfmExtPerfPort24HrIntRxCodingErrors_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 3, 3, 4, 1, 6),
    _AdGenEfmExtPerfPort24HrIntRxCodingErrors_Type()
)
adGenEfmExtPerfPort24HrIntRxCodingErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEfmExtPerfPort24HrIntRxCodingErrors.setStatus("current")
_AdGenEfmExtPerfPort15MinThreshTable_Object = MibTable
adGenEfmExtPerfPort15MinThreshTable = _AdGenEfmExtPerfPort15MinThreshTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 3, 3, 5)
)
if mibBuilder.loadTexts:
    adGenEfmExtPerfPort15MinThreshTable.setStatus("current")
_AdGenEfmExtPerfPort15MinThreshEntry_Object = MibTableRow
adGenEfmExtPerfPort15MinThreshEntry = _AdGenEfmExtPerfPort15MinThreshEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 3, 3, 5, 1)
)
adGenEfmExtPerfPort15MinThreshEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adGenEfmExtPerfPort15MinThreshEntry.setStatus("current")
_AdGenEfmExtPerfPort15MinThreshRxCodingErrors_Type = Unsigned32
_AdGenEfmExtPerfPort15MinThreshRxCodingErrors_Object = MibTableColumn
adGenEfmExtPerfPort15MinThreshRxCodingErrors = _AdGenEfmExtPerfPort15MinThreshRxCodingErrors_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 3, 3, 5, 1, 6),
    _AdGenEfmExtPerfPort15MinThreshRxCodingErrors_Type()
)
adGenEfmExtPerfPort15MinThreshRxCodingErrors.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenEfmExtPerfPort15MinThreshRxCodingErrors.setStatus("current")
_AdGenEfmExtPerfPort24HrThreshTable_Object = MibTable
adGenEfmExtPerfPort24HrThreshTable = _AdGenEfmExtPerfPort24HrThreshTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 3, 3, 6)
)
if mibBuilder.loadTexts:
    adGenEfmExtPerfPort24HrThreshTable.setStatus("current")
_AdGenEfmExtPerfPort24HrThreshEntry_Object = MibTableRow
adGenEfmExtPerfPort24HrThreshEntry = _AdGenEfmExtPerfPort24HrThreshEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 3, 3, 6, 1)
)
adGenEfmExtPerfPort24HrThreshEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adGenEfmExtPerfPort24HrThreshEntry.setStatus("current")
_AdGenEfmExtPerfPort24HrThreshRxCodingErrors_Type = Unsigned32
_AdGenEfmExtPerfPort24HrThreshRxCodingErrors_Object = MibTableColumn
adGenEfmExtPerfPort24HrThreshRxCodingErrors = _AdGenEfmExtPerfPort24HrThreshRxCodingErrors_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 3, 3, 6, 1, 6),
    _AdGenEfmExtPerfPort24HrThreshRxCodingErrors_Type()
)
adGenEfmExtPerfPort24HrThreshRxCodingErrors.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenEfmExtPerfPort24HrThreshRxCodingErrors.setStatus("current")
_AdGenEfmExtPerfPortResetTable_Object = MibTable
adGenEfmExtPerfPortResetTable = _AdGenEfmExtPerfPortResetTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 3, 3, 7)
)
if mibBuilder.loadTexts:
    adGenEfmExtPerfPortResetTable.setStatus("current")
_AdGenEfmExtPerfPortResetEntry_Object = MibTableRow
adGenEfmExtPerfPortResetEntry = _AdGenEfmExtPerfPortResetEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 3, 3, 7, 1)
)
adGenEfmExtPerfPortResetEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adGenEfmExtPerfPortResetEntry.setStatus("current")


class _AdGenEfmExtPerfPortResetData_Type(Integer32):
    """Custom type adGenEfmExtPerfPortResetData based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset", 1)
    )


_AdGenEfmExtPerfPortResetData_Type.__name__ = "Integer32"
_AdGenEfmExtPerfPortResetData_Object = MibTableColumn
adGenEfmExtPerfPortResetData = _AdGenEfmExtPerfPortResetData_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 3, 3, 7, 1, 1),
    _AdGenEfmExtPerfPortResetData_Type()
)
adGenEfmExtPerfPortResetData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenEfmExtPerfPortResetData.setStatus("current")
_AdGenEfmExtAlarmsPrefix_ObjectIdentity = ObjectIdentity
adGenEfmExtAlarmsPrefix = _AdGenEfmExtAlarmsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 3, 10)
)
_AdGenEfmExtAlarms_ObjectIdentity = ObjectIdentity
adGenEfmExtAlarms = _AdGenEfmExtAlarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 3, 10, 0)
)

# Managed Objects groups

adGenEfmExtStatGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 3, 2, 1, 1)
)
adGenEfmExtStatGroup.setObjects(
      *(("ADTRAN-EFMEXT-MIB", "adGenEfmExtStatGroupStatus"),
        ("ADTRAN-EFMEXT-MIB", "adGenEfmExtStatGroupSize"),
        ("ADTRAN-EFMEXT-MIB", "adGenEfmExtStatGroupNumActiveLinks"),
        ("ADTRAN-EFMEXT-MIB", "adGenEfmExtStatGroupUAS"),
        ("ADTRAN-EFMEXT-MIB", "adGenEfmExtStatGroupFailures"),
        ("ADTRAN-EFMEXT-MIB", "adGenEfmExtStatLinkNeTcSync"),
        ("ADTRAN-EFMEXT-MIB", "adGenEfmExtStatLinkFeTcSync"),
        ("ADTRAN-EFMEXT-MIB", "adGenEfmExtStatLinkSkew"))
)
if mibBuilder.loadTexts:
    adGenEfmExtStatGroup.setStatus("current")


# Notification objects

adGenEfmExtGroupDownClr = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 3, 10, 0, 2)
)
adGenEfmExtGroupDownClr.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("IF-MIB", "ifDescr"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenEfmExtGroupDownClr.setStatus(
        "current"
    )

adGenEfmExtGroupDownAct = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 3, 10, 0, 3)
)
adGenEfmExtGroupDownAct.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("IF-MIB", "ifDescr"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenEfmExtGroupDownAct.setStatus(
        "current"
    )

adGenEfmExtLinkDownClr = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 3, 10, 0, 4)
)
adGenEfmExtLinkDownClr.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("IF-MIB", "ifDescr"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenEfmExtLinkDownClr.setStatus(
        "current"
    )

adGenEfmExtLinkDownAct = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 3, 10, 0, 5)
)
adGenEfmExtLinkDownAct.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("IF-MIB", "ifDescr"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenEfmExtLinkDownAct.setStatus(
        "current"
    )

adGenEfmExtGroupUpPartialClr = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 3, 10, 0, 6)
)
adGenEfmExtGroupUpPartialClr.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("IF-MIB", "ifDescr"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenEfmExtGroupUpPartialClr.setStatus(
        "current"
    )

adGenEfmExtGroupUpPartialAct = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 3, 10, 0, 7)
)
adGenEfmExtGroupUpPartialAct.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("IF-MIB", "ifDescr"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenEfmExtGroupUpPartialAct.setStatus(
        "current"
    )

adGenEfmExtGroupDownstreamBandwidthClr = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 3, 10, 0, 8)
)
adGenEfmExtGroupDownstreamBandwidthClr.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("IF-MIB", "ifDescr"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenEfmExtGroupDownstreamBandwidthClr.setStatus(
        "current"
    )

adGenEfmExtGroupDownstreamBandwidthAct = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 3, 10, 0, 9)
)
adGenEfmExtGroupDownstreamBandwidthAct.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("IF-MIB", "ifDescr"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenEfmExtGroupDownstreamBandwidthAct.setStatus(
        "current"
    )

adGenEfmExtGroupUpstreamBandwidthClr = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 3, 10, 0, 10)
)
adGenEfmExtGroupUpstreamBandwidthClr.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("IF-MIB", "ifDescr"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenEfmExtGroupUpstreamBandwidthClr.setStatus(
        "current"
    )

adGenEfmExtGroupUpstreamBandwidthAct = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 3, 10, 0, 11)
)
adGenEfmExtGroupUpstreamBandwidthAct.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("IF-MIB", "ifDescr"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenEfmExtGroupUpstreamBandwidthAct.setStatus(
        "current"
    )

adGenEfmExtGroupDownstream4xRateViolationClr = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 3, 10, 0, 12)
)
adGenEfmExtGroupDownstream4xRateViolationClr.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("IF-MIB", "ifDescr"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenEfmExtGroupDownstream4xRateViolationClr.setStatus(
        "current"
    )

adGenEfmExtGroupDownstream4xRateViolationAct = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 3, 10, 0, 13)
)
adGenEfmExtGroupDownstream4xRateViolationAct.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("IF-MIB", "ifDescr"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenEfmExtGroupDownstream4xRateViolationAct.setStatus(
        "current"
    )

adGenEfmExtGroupUpstream4xRateViolationClr = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 3, 10, 0, 14)
)
adGenEfmExtGroupUpstream4xRateViolationClr.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("IF-MIB", "ifDescr"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenEfmExtGroupUpstream4xRateViolationClr.setStatus(
        "current"
    )

adGenEfmExtGroupUpstream4xRateViolationAct = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 3, 10, 0, 15)
)
adGenEfmExtGroupUpstream4xRateViolationAct.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("IF-MIB", "ifDescr"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenEfmExtGroupUpstream4xRateViolationAct.setStatus(
        "current"
    )

adGenEfmExtGroupRemoteLoopbackClr = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 3, 10, 0, 16)
)
adGenEfmExtGroupRemoteLoopbackClr.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("IF-MIB", "ifDescr"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenEfmExtGroupRemoteLoopbackClr.setStatus(
        "current"
    )

adGenEfmExtGroupRemoteLoopbackAct = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 3, 10, 0, 17)
)
adGenEfmExtGroupRemoteLoopbackAct.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("IF-MIB", "ifDescr"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenEfmExtGroupRemoteLoopbackAct.setStatus(
        "current"
    )

adGenEfmExtGroupLocalLoopbackClr = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 3, 10, 0, 18)
)
adGenEfmExtGroupLocalLoopbackClr.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("IF-MIB", "ifDescr"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenEfmExtGroupLocalLoopbackClr.setStatus(
        "current"
    )

adGenEfmExtGroupLocalLoopbackAct = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 3, 10, 0, 19)
)
adGenEfmExtGroupLocalLoopbackAct.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("IF-MIB", "ifDescr"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenEfmExtGroupLocalLoopbackAct.setStatus(
        "current"
    )

adGenEfmExtGroup15MinRxBadFragmentsAct = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 3, 10, 0, 20)
)
adGenEfmExtGroup15MinRxBadFragmentsAct.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("IF-MIB", "ifDescr"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenEfmExtGroup15MinRxBadFragmentsAct.setStatus(
        "current"
    )

adGenEfmExtGroup15MinRxLostFragmentsAct = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 3, 10, 0, 21)
)
adGenEfmExtGroup15MinRxLostFragmentsAct.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("IF-MIB", "ifDescr"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenEfmExtGroup15MinRxLostFragmentsAct.setStatus(
        "current"
    )

adGenEfmExtGroup15MinRxLostStartsAct = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 3, 10, 0, 22)
)
adGenEfmExtGroup15MinRxLostStartsAct.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("IF-MIB", "ifDescr"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenEfmExtGroup15MinRxLostStartsAct.setStatus(
        "current"
    )

adGenEfmExtGroup15MinRxLostEndsAct = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 3, 10, 0, 23)
)
adGenEfmExtGroup15MinRxLostEndsAct.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("IF-MIB", "ifDescr"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenEfmExtGroup15MinRxLostEndsAct.setStatus(
        "current"
    )

adGenEfmExtGroup24HrRxBadFragmentsAct = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 3, 10, 0, 24)
)
adGenEfmExtGroup24HrRxBadFragmentsAct.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("IF-MIB", "ifDescr"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenEfmExtGroup24HrRxBadFragmentsAct.setStatus(
        "current"
    )

adGenEfmExtGroup24HrRxLostFragmentsAct = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 3, 10, 0, 25)
)
adGenEfmExtGroup24HrRxLostFragmentsAct.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("IF-MIB", "ifDescr"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenEfmExtGroup24HrRxLostFragmentsAct.setStatus(
        "current"
    )

adGenEfmExtGroup24HrRxLostStartsAct = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 3, 10, 0, 26)
)
adGenEfmExtGroup24HrRxLostStartsAct.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("IF-MIB", "ifDescr"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenEfmExtGroup24HrRxLostStartsAct.setStatus(
        "current"
    )

adGenEfmExtGroup24HrRxLostEndsAct = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 3, 10, 0, 27)
)
adGenEfmExtGroup24HrRxLostEndsAct.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("IF-MIB", "ifDescr"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenEfmExtGroup24HrRxLostEndsAct.setStatus(
        "current"
    )

adGenEfmExtLink15MinRxErroredFragmentsAct = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 3, 10, 0, 28)
)
adGenEfmExtLink15MinRxErroredFragmentsAct.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("IF-MIB", "ifDescr"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenEfmExtLink15MinRxErroredFragmentsAct.setStatus(
        "current"
    )

adGenEfmExtLink15MinRxSmallFragmentsAct = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 3, 10, 0, 29)
)
adGenEfmExtLink15MinRxSmallFragmentsAct.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("IF-MIB", "ifDescr"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenEfmExtLink15MinRxSmallFragmentsAct.setStatus(
        "current"
    )

adGenEfmExtLink15MinRxLargeFragmentsAct = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 3, 10, 0, 30)
)
adGenEfmExtLink15MinRxLargeFragmentsAct.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("IF-MIB", "ifDescr"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenEfmExtLink15MinRxLargeFragmentsAct.setStatus(
        "current"
    )

adGenEfmExtLink15MinRxDiscardedFragmentsAct = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 3, 10, 0, 31)
)
adGenEfmExtLink15MinRxDiscardedFragmentsAct.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("IF-MIB", "ifDescr"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenEfmExtLink15MinRxDiscardedFragmentsAct.setStatus(
        "current"
    )

adGenEfmExtLink15MinRxFcsErrorsAct = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 3, 10, 0, 32)
)
adGenEfmExtLink15MinRxFcsErrorsAct.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("IF-MIB", "ifDescr"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenEfmExtLink15MinRxFcsErrorsAct.setStatus(
        "current"
    )

adGenEfmExtLink15MinRxCodingErrorsAct = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 3, 10, 0, 33)
)
adGenEfmExtLink15MinRxCodingErrorsAct.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("IF-MIB", "ifDescr"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenEfmExtLink15MinRxCodingErrorsAct.setStatus(
        "current"
    )

adGenEfmExtLink24HrRxErroredFragmentsAct = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 3, 10, 0, 34)
)
adGenEfmExtLink24HrRxErroredFragmentsAct.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("IF-MIB", "ifDescr"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenEfmExtLink24HrRxErroredFragmentsAct.setStatus(
        "current"
    )

adGenEfmExtLink24HrRxSmallFragmentsAct = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 3, 10, 0, 35)
)
adGenEfmExtLink24HrRxSmallFragmentsAct.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("IF-MIB", "ifDescr"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenEfmExtLink24HrRxSmallFragmentsAct.setStatus(
        "current"
    )

adGenEfmExtLink24HrRxLargeFragmentsAct = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 3, 10, 0, 36)
)
adGenEfmExtLink24HrRxLargeFragmentsAct.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("IF-MIB", "ifDescr"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenEfmExtLink24HrRxLargeFragmentsAct.setStatus(
        "current"
    )

adGenEfmExtLink24HrRxDiscardedFragmentsAct = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 3, 10, 0, 37)
)
adGenEfmExtLink24HrRxDiscardedFragmentsAct.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("IF-MIB", "ifDescr"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenEfmExtLink24HrRxDiscardedFragmentsAct.setStatus(
        "current"
    )

adGenEfmExtLink24HrRxFcsErrorsAct = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 3, 10, 0, 38)
)
adGenEfmExtLink24HrRxFcsErrorsAct.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("IF-MIB", "ifDescr"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenEfmExtLink24HrRxFcsErrorsAct.setStatus(
        "current"
    )

adGenEfmExtLink24HrRxCodingErrorsAct = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 3, 10, 0, 39)
)
adGenEfmExtLink24HrRxCodingErrorsAct.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("IF-MIB", "ifDescr"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenEfmExtLink24HrRxCodingErrorsAct.setStatus(
        "current"
    )

adGenEfmExtLinkXCVThreshExceededClr = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 3, 10, 0, 50)
)
adGenEfmExtLinkXCVThreshExceededClr.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("IF-MIB", "ifDescr"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenEfmExtLinkXCVThreshExceededClr.setStatus(
        "current"
    )

adGenEfmExtLinkXCVThreshExceededAct = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 3, 10, 0, 51)
)
adGenEfmExtLinkXCVThreshExceededAct.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("IF-MIB", "ifDescr"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenEfmExtLinkXCVThreshExceededAct.setStatus(
        "current"
    )

adGenEfmExtLinkRemovedXCVThreshExceededClr = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 3, 10, 0, 52)
)
adGenEfmExtLinkRemovedXCVThreshExceededClr.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("IF-MIB", "ifDescr"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenEfmExtLinkRemovedXCVThreshExceededClr.setStatus(
        "current"
    )

adGenEfmExtLinkRemovedXCVThreshExceededAct = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 3, 10, 0, 53)
)
adGenEfmExtLinkRemovedXCVThreshExceededAct.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("IF-MIB", "ifDescr"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenEfmExtLinkRemovedXCVThreshExceededAct.setStatus(
        "current"
    )

adGenEfmExtLinkRemovedFarEndLbkDetectedClr = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 3, 10, 0, 54)
)
adGenEfmExtLinkRemovedFarEndLbkDetectedClr.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("IF-MIB", "ifDescr"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenEfmExtLinkRemovedFarEndLbkDetectedClr.setStatus(
        "current"
    )

adGenEfmExtLinkRemovedFarEndLbkDetectedAct = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 3, 10, 0, 55)
)
adGenEfmExtLinkRemovedFarEndLbkDetectedAct.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("IF-MIB", "ifDescr"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenEfmExtLinkRemovedFarEndLbkDetectedAct.setStatus(
        "current"
    )

adGenEfmExtPortDownClr = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 3, 10, 0, 80)
)
adGenEfmExtPortDownClr.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("IF-MIB", "ifDescr"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenEfmExtPortDownClr.setStatus(
        "current"
    )

adGenEfmExtPortDownAct = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 3, 10, 0, 81)
)
adGenEfmExtPortDownAct.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("IF-MIB", "ifDescr"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenEfmExtPortDownAct.setStatus(
        "current"
    )

adGenEfmExtPort15MinRxCodingErrorsAct = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 3, 10, 0, 91)
)
adGenEfmExtPort15MinRxCodingErrorsAct.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("IF-MIB", "ifDescr"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenEfmExtPort15MinRxCodingErrorsAct.setStatus(
        "current"
    )

adGenEfmExtPort24HrRxCodingErrorsAct = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 3, 10, 0, 92)
)
adGenEfmExtPort24HrRxCodingErrorsAct.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("IF-MIB", "ifDescr"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenEfmExtPort24HrRxCodingErrorsAct.setStatus(
        "current"
    )

adGenEfmExtGroupSecondaryDownstreamBandwidthClr = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 3, 10, 0, 93)
)
adGenEfmExtGroupSecondaryDownstreamBandwidthClr.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("IF-MIB", "ifDescr"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenEfmExtGroupSecondaryDownstreamBandwidthClr.setStatus(
        "current"
    )

adGenEfmExtGroupSecondaryDownstreamBandwidthAct = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 3, 10, 0, 94)
)
adGenEfmExtGroupSecondaryDownstreamBandwidthAct.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("IF-MIB", "ifDescr"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenEfmExtGroupSecondaryDownstreamBandwidthAct.setStatus(
        "current"
    )

adGenEfmExtGroupSecondaryUpstreamBandwidthClr = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 3, 10, 0, 95)
)
adGenEfmExtGroupSecondaryUpstreamBandwidthClr.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("IF-MIB", "ifDescr"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenEfmExtGroupSecondaryUpstreamBandwidthClr.setStatus(
        "current"
    )

adGenEfmExtGroupSecondaryUpstreamBandwidthAct = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 3, 10, 0, 96)
)
adGenEfmExtGroupSecondaryUpstreamBandwidthAct.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("IF-MIB", "ifDescr"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenEfmExtGroupSecondaryUpstreamBandwidthAct.setStatus(
        "current"
    )


# Notifications groups

adGenEfmExtEventGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 664, 5, 66, 3, 2, 1, 2)
)
adGenEfmExtEventGroup.setObjects(
      *(("ADTRAN-EFMEXT-MIB", "adGenEfmExtGroupDownClr"),
        ("ADTRAN-EFMEXT-MIB", "adGenEfmExtGroupDownAct"),
        ("ADTRAN-EFMEXT-MIB", "adGenEfmExtLinkDownClr"),
        ("ADTRAN-EFMEXT-MIB", "adGenEfmExtLinkDownAct"),
        ("ADTRAN-EFMEXT-MIB", "adGenEfmExtGroupUpPartialClr"),
        ("ADTRAN-EFMEXT-MIB", "adGenEfmExtGroupUpPartialAct"),
        ("ADTRAN-EFMEXT-MIB", "adGenEfmExtGroupDownstreamBandwidthClr"),
        ("ADTRAN-EFMEXT-MIB", "adGenEfmExtGroupDownstreamBandwidthAct"),
        ("ADTRAN-EFMEXT-MIB", "adGenEfmExtGroupUpstreamBandwidthClr"),
        ("ADTRAN-EFMEXT-MIB", "adGenEfmExtGroupUpstreamBandwidthAct"),
        ("ADTRAN-EFMEXT-MIB", "adGenEfmExtGroupDownstream4xRateViolationClr"),
        ("ADTRAN-EFMEXT-MIB", "adGenEfmExtGroupDownstream4xRateViolationAct"),
        ("ADTRAN-EFMEXT-MIB", "adGenEfmExtGroupUpstream4xRateViolationClr"),
        ("ADTRAN-EFMEXT-MIB", "adGenEfmExtGroupUpstream4xRateViolationAct"),
        ("ADTRAN-EFMEXT-MIB", "adGenEfmExtGroup15MinRxBadFragmentsAct"),
        ("ADTRAN-EFMEXT-MIB", "adGenEfmExtGroup15MinRxLostFragmentsAct"),
        ("ADTRAN-EFMEXT-MIB", "adGenEfmExtGroup15MinRxLostStartsAct"),
        ("ADTRAN-EFMEXT-MIB", "adGenEfmExtGroup15MinRxLostEndsAct"),
        ("ADTRAN-EFMEXT-MIB", "adGenEfmExtGroup24HrRxBadFragmentsAct"),
        ("ADTRAN-EFMEXT-MIB", "adGenEfmExtGroup24HrRxLostFragmentsAct"),
        ("ADTRAN-EFMEXT-MIB", "adGenEfmExtGroup24HrRxLostStartsAct"),
        ("ADTRAN-EFMEXT-MIB", "adGenEfmExtGroup24HrRxLostEndsAct"),
        ("ADTRAN-EFMEXT-MIB", "adGenEfmExtLink15MinRxErroredFragmentsAct"),
        ("ADTRAN-EFMEXT-MIB", "adGenEfmExtLink15MinRxSmallFragmentsAct"),
        ("ADTRAN-EFMEXT-MIB", "adGenEfmExtLink15MinRxLargeFragmentsAct"),
        ("ADTRAN-EFMEXT-MIB", "adGenEfmExtLink15MinRxDiscardedFragmentsAct"),
        ("ADTRAN-EFMEXT-MIB", "adGenEfmExtLink15MinRxFcsErrorsAct"),
        ("ADTRAN-EFMEXT-MIB", "adGenEfmExtLink15MinRxCodingErrorsAct"),
        ("ADTRAN-EFMEXT-MIB", "adGenEfmExtLink24HrRxErroredFragmentsAct"),
        ("ADTRAN-EFMEXT-MIB", "adGenEfmExtLink24HrRxSmallFragmentsAct"),
        ("ADTRAN-EFMEXT-MIB", "adGenEfmExtLink24HrRxLargeFragmentsAct"),
        ("ADTRAN-EFMEXT-MIB", "adGenEfmExtLink24HrRxDiscardedFragmentsAct"),
        ("ADTRAN-EFMEXT-MIB", "adGenEfmExtLink24HrRxFcsErrorsAct"),
        ("ADTRAN-EFMEXT-MIB", "adGenEfmExtLink24HrRxCodingErrorsAct"),
        ("ADTRAN-EFMEXT-MIB", "adGenEfmExtLinkXCVThreshExceededClr"),
        ("ADTRAN-EFMEXT-MIB", "adGenEfmExtLinkXCVThreshExceededAct"),
        ("ADTRAN-EFMEXT-MIB", "adGenEfmExtLinkRemovedXCVThreshExceededClr"),
        ("ADTRAN-EFMEXT-MIB", "adGenEfmExtLinkRemovedXCVThreshExceededAct"),
        ("ADTRAN-EFMEXT-MIB", "adGenEfmExtLinkRemovedFarEndLbkDetectedClr"),
        ("ADTRAN-EFMEXT-MIB", "adGenEfmExtLinkRemovedFarEndLbkDetectedAct"),
        ("ADTRAN-EFMEXT-MIB", "adGenEfmExtGroupRemoteLoopbackClr"),
        ("ADTRAN-EFMEXT-MIB", "adGenEfmExtGroupRemoteLoopbackAct"),
        ("ADTRAN-EFMEXT-MIB", "adGenEfmExtGroupLocalLoopbackClr"),
        ("ADTRAN-EFMEXT-MIB", "adGenEfmExtGroupLocalLoopbackAct"),
        ("ADTRAN-EFMEXT-MIB", "adGenEfmExtGroupSecondaryDownstreamBandwidthClr"),
        ("ADTRAN-EFMEXT-MIB", "adGenEfmExtGroupSecondaryDownstreamBandwidthAct"),
        ("ADTRAN-EFMEXT-MIB", "adGenEfmExtGroupSecondaryUpstreamBandwidthClr"),
        ("ADTRAN-EFMEXT-MIB", "adGenEfmExtGroupSecondaryUpstreamBandwidthAct"))
)
if mibBuilder.loadTexts:
    adGenEfmExtEventGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ADTRAN-EFMEXT-MIB",
    **{"adGenEfmExtStatus": adGenEfmExtStatus,
       "adGenEfmExtStatGroupTable": adGenEfmExtStatGroupTable,
       "adGenEfmExtStatGroupEntry": adGenEfmExtStatGroupEntry,
       "adGenEfmExtStatGroupStatus": adGenEfmExtStatGroupStatus,
       "adGenEfmExtStatGroupSize": adGenEfmExtStatGroupSize,
       "adGenEfmExtStatGroupNumActiveLinks": adGenEfmExtStatGroupNumActiveLinks,
       "adGenEfmExtStatGroupUAS": adGenEfmExtStatGroupUAS,
       "adGenEfmExtStatGroupFailures": adGenEfmExtStatGroupFailures,
       "adGenEfmExtStatLinkTable": adGenEfmExtStatLinkTable,
       "adGenEfmExtStatLinkEntry": adGenEfmExtStatLinkEntry,
       "adGenEfmExtStatLinkNeTcSync": adGenEfmExtStatLinkNeTcSync,
       "adGenEfmExtStatLinkFeTcSync": adGenEfmExtStatLinkFeTcSync,
       "adGenEfmExtStatLinkSkew": adGenEfmExtStatLinkSkew,
       "adGenEfmExtStatLinkStatus": adGenEfmExtStatLinkStatus,
       "adGenEfmExtStatLinkFeId": adGenEfmExtStatLinkFeId,
       "adGenEfmExtMibConformance": adGenEfmExtMibConformance,
       "adGenEfmExtMibGroups": adGenEfmExtMibGroups,
       "adGenEfmExtStatGroup": adGenEfmExtStatGroup,
       "adGenEfmExtEventGroup": adGenEfmExtEventGroup,
       "adGenEfmExtPerformance": adGenEfmExtPerformance,
       "adGenEfmExtPerfPortCurr15MinTable": adGenEfmExtPerfPortCurr15MinTable,
       "adGenEfmExtPerfPortCurr15MinEntry": adGenEfmExtPerfPortCurr15MinEntry,
       "adGenEfmExtPerfPort15MinValidIntervals": adGenEfmExtPerfPort15MinValidIntervals,
       "adGenEfmExtPerfPortCurr15MinTxOctets": adGenEfmExtPerfPortCurr15MinTxOctets,
       "adGenEfmExtPerfPortCurr15MinTxFrames": adGenEfmExtPerfPortCurr15MinTxFrames,
       "adGenEfmExtPerfPortCurr15MinRxOctets": adGenEfmExtPerfPortCurr15MinRxOctets,
       "adGenEfmExtPerfPortCurr15MinRxFrames": adGenEfmExtPerfPortCurr15MinRxFrames,
       "adGenEfmExtPerfPortCurr15MinRxCodingErrors": adGenEfmExtPerfPortCurr15MinRxCodingErrors,
       "adGenEfmExtPerfPort15MinIntTable": adGenEfmExtPerfPort15MinIntTable,
       "adGenEfmExtPerfPort15MinIntEntry": adGenEfmExtPerfPort15MinIntEntry,
       "adGenEfmExtPerfPort15MinIntNumber": adGenEfmExtPerfPort15MinIntNumber,
       "adGenEfmExtPerfPort15MinIntTxOctets": adGenEfmExtPerfPort15MinIntTxOctets,
       "adGenEfmExtPerfPort15MinIntTxFrames": adGenEfmExtPerfPort15MinIntTxFrames,
       "adGenEfmExtPerfPort15MinIntRxOctets": adGenEfmExtPerfPort15MinIntRxOctets,
       "adGenEfmExtPerfPort15MinIntRxFrames": adGenEfmExtPerfPort15MinIntRxFrames,
       "adGenEfmExtPerfPort15MinIntRxCodingErrors": adGenEfmExtPerfPort15MinIntRxCodingErrors,
       "adGenEfmExtPerfPortCurr24HrTable": adGenEfmExtPerfPortCurr24HrTable,
       "adGenEfmExtPerfPortCurr24HrEntry": adGenEfmExtPerfPortCurr24HrEntry,
       "adGenEfmExtPerfPort24HrValidIntervals": adGenEfmExtPerfPort24HrValidIntervals,
       "adGenEfmExtPerfPortCurr24HrTxOctets": adGenEfmExtPerfPortCurr24HrTxOctets,
       "adGenEfmExtPerfPortCurr24HrTxFrames": adGenEfmExtPerfPortCurr24HrTxFrames,
       "adGenEfmExtPerfPortCurr24HrRxOctets": adGenEfmExtPerfPortCurr24HrRxOctets,
       "adGenEfmExtPerfPortCurr24HrRxFrames": adGenEfmExtPerfPortCurr24HrRxFrames,
       "adGenEfmExtPerfPortCurr24HrRxCodingErrors": adGenEfmExtPerfPortCurr24HrRxCodingErrors,
       "adGenEfmExtPerfPort24HrIntTable": adGenEfmExtPerfPort24HrIntTable,
       "adGenEfmExtPerfPort24HrIntEntry": adGenEfmExtPerfPort24HrIntEntry,
       "adGenEfmExtPerfPort24HrIntNumber": adGenEfmExtPerfPort24HrIntNumber,
       "adGenEfmExtPerfPort24HrIntTxOctets": adGenEfmExtPerfPort24HrIntTxOctets,
       "adGenEfmExtPerfPort24HrIntTxFrames": adGenEfmExtPerfPort24HrIntTxFrames,
       "adGenEfmExtPerfPort24HrIntRxOctets": adGenEfmExtPerfPort24HrIntRxOctets,
       "adGenEfmExtPerfPort24HrIntRxFrames": adGenEfmExtPerfPort24HrIntRxFrames,
       "adGenEfmExtPerfPort24HrIntRxCodingErrors": adGenEfmExtPerfPort24HrIntRxCodingErrors,
       "adGenEfmExtPerfPort15MinThreshTable": adGenEfmExtPerfPort15MinThreshTable,
       "adGenEfmExtPerfPort15MinThreshEntry": adGenEfmExtPerfPort15MinThreshEntry,
       "adGenEfmExtPerfPort15MinThreshRxCodingErrors": adGenEfmExtPerfPort15MinThreshRxCodingErrors,
       "adGenEfmExtPerfPort24HrThreshTable": adGenEfmExtPerfPort24HrThreshTable,
       "adGenEfmExtPerfPort24HrThreshEntry": adGenEfmExtPerfPort24HrThreshEntry,
       "adGenEfmExtPerfPort24HrThreshRxCodingErrors": adGenEfmExtPerfPort24HrThreshRxCodingErrors,
       "adGenEfmExtPerfPortResetTable": adGenEfmExtPerfPortResetTable,
       "adGenEfmExtPerfPortResetEntry": adGenEfmExtPerfPortResetEntry,
       "adGenEfmExtPerfPortResetData": adGenEfmExtPerfPortResetData,
       "adGenEfmExtAlarmsPrefix": adGenEfmExtAlarmsPrefix,
       "adGenEfmExtAlarms": adGenEfmExtAlarms,
       "adGenEfmExtGroupDownClr": adGenEfmExtGroupDownClr,
       "adGenEfmExtGroupDownAct": adGenEfmExtGroupDownAct,
       "adGenEfmExtLinkDownClr": adGenEfmExtLinkDownClr,
       "adGenEfmExtLinkDownAct": adGenEfmExtLinkDownAct,
       "adGenEfmExtGroupUpPartialClr": adGenEfmExtGroupUpPartialClr,
       "adGenEfmExtGroupUpPartialAct": adGenEfmExtGroupUpPartialAct,
       "adGenEfmExtGroupDownstreamBandwidthClr": adGenEfmExtGroupDownstreamBandwidthClr,
       "adGenEfmExtGroupDownstreamBandwidthAct": adGenEfmExtGroupDownstreamBandwidthAct,
       "adGenEfmExtGroupUpstreamBandwidthClr": adGenEfmExtGroupUpstreamBandwidthClr,
       "adGenEfmExtGroupUpstreamBandwidthAct": adGenEfmExtGroupUpstreamBandwidthAct,
       "adGenEfmExtGroupDownstream4xRateViolationClr": adGenEfmExtGroupDownstream4xRateViolationClr,
       "adGenEfmExtGroupDownstream4xRateViolationAct": adGenEfmExtGroupDownstream4xRateViolationAct,
       "adGenEfmExtGroupUpstream4xRateViolationClr": adGenEfmExtGroupUpstream4xRateViolationClr,
       "adGenEfmExtGroupUpstream4xRateViolationAct": adGenEfmExtGroupUpstream4xRateViolationAct,
       "adGenEfmExtGroupRemoteLoopbackClr": adGenEfmExtGroupRemoteLoopbackClr,
       "adGenEfmExtGroupRemoteLoopbackAct": adGenEfmExtGroupRemoteLoopbackAct,
       "adGenEfmExtGroupLocalLoopbackClr": adGenEfmExtGroupLocalLoopbackClr,
       "adGenEfmExtGroupLocalLoopbackAct": adGenEfmExtGroupLocalLoopbackAct,
       "adGenEfmExtGroup15MinRxBadFragmentsAct": adGenEfmExtGroup15MinRxBadFragmentsAct,
       "adGenEfmExtGroup15MinRxLostFragmentsAct": adGenEfmExtGroup15MinRxLostFragmentsAct,
       "adGenEfmExtGroup15MinRxLostStartsAct": adGenEfmExtGroup15MinRxLostStartsAct,
       "adGenEfmExtGroup15MinRxLostEndsAct": adGenEfmExtGroup15MinRxLostEndsAct,
       "adGenEfmExtGroup24HrRxBadFragmentsAct": adGenEfmExtGroup24HrRxBadFragmentsAct,
       "adGenEfmExtGroup24HrRxLostFragmentsAct": adGenEfmExtGroup24HrRxLostFragmentsAct,
       "adGenEfmExtGroup24HrRxLostStartsAct": adGenEfmExtGroup24HrRxLostStartsAct,
       "adGenEfmExtGroup24HrRxLostEndsAct": adGenEfmExtGroup24HrRxLostEndsAct,
       "adGenEfmExtLink15MinRxErroredFragmentsAct": adGenEfmExtLink15MinRxErroredFragmentsAct,
       "adGenEfmExtLink15MinRxSmallFragmentsAct": adGenEfmExtLink15MinRxSmallFragmentsAct,
       "adGenEfmExtLink15MinRxLargeFragmentsAct": adGenEfmExtLink15MinRxLargeFragmentsAct,
       "adGenEfmExtLink15MinRxDiscardedFragmentsAct": adGenEfmExtLink15MinRxDiscardedFragmentsAct,
       "adGenEfmExtLink15MinRxFcsErrorsAct": adGenEfmExtLink15MinRxFcsErrorsAct,
       "adGenEfmExtLink15MinRxCodingErrorsAct": adGenEfmExtLink15MinRxCodingErrorsAct,
       "adGenEfmExtLink24HrRxErroredFragmentsAct": adGenEfmExtLink24HrRxErroredFragmentsAct,
       "adGenEfmExtLink24HrRxSmallFragmentsAct": adGenEfmExtLink24HrRxSmallFragmentsAct,
       "adGenEfmExtLink24HrRxLargeFragmentsAct": adGenEfmExtLink24HrRxLargeFragmentsAct,
       "adGenEfmExtLink24HrRxDiscardedFragmentsAct": adGenEfmExtLink24HrRxDiscardedFragmentsAct,
       "adGenEfmExtLink24HrRxFcsErrorsAct": adGenEfmExtLink24HrRxFcsErrorsAct,
       "adGenEfmExtLink24HrRxCodingErrorsAct": adGenEfmExtLink24HrRxCodingErrorsAct,
       "adGenEfmExtLinkXCVThreshExceededClr": adGenEfmExtLinkXCVThreshExceededClr,
       "adGenEfmExtLinkXCVThreshExceededAct": adGenEfmExtLinkXCVThreshExceededAct,
       "adGenEfmExtLinkRemovedXCVThreshExceededClr": adGenEfmExtLinkRemovedXCVThreshExceededClr,
       "adGenEfmExtLinkRemovedXCVThreshExceededAct": adGenEfmExtLinkRemovedXCVThreshExceededAct,
       "adGenEfmExtLinkRemovedFarEndLbkDetectedClr": adGenEfmExtLinkRemovedFarEndLbkDetectedClr,
       "adGenEfmExtLinkRemovedFarEndLbkDetectedAct": adGenEfmExtLinkRemovedFarEndLbkDetectedAct,
       "adGenEfmExtPortDownClr": adGenEfmExtPortDownClr,
       "adGenEfmExtPortDownAct": adGenEfmExtPortDownAct,
       "adGenEfmExtPort15MinRxCodingErrorsAct": adGenEfmExtPort15MinRxCodingErrorsAct,
       "adGenEfmExtPort24HrRxCodingErrorsAct": adGenEfmExtPort24HrRxCodingErrorsAct,
       "adGenEfmExtGroupSecondaryDownstreamBandwidthClr": adGenEfmExtGroupSecondaryDownstreamBandwidthClr,
       "adGenEfmExtGroupSecondaryDownstreamBandwidthAct": adGenEfmExtGroupSecondaryDownstreamBandwidthAct,
       "adGenEfmExtGroupSecondaryUpstreamBandwidthClr": adGenEfmExtGroupSecondaryUpstreamBandwidthClr,
       "adGenEfmExtGroupSecondaryUpstreamBandwidthAct": adGenEfmExtGroupSecondaryUpstreamBandwidthAct,
       "adGenEfmExtMIB": adGenEfmExtMIB}
)
