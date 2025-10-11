# SNMP MIB module (ADTRAN-GEN-FRAME-RELAY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/adtran/ADTRAN-GEN-FRAME-RELAY-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:32:03 2025
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

(adGenFrameRelay,
 adGenFrameRelayID) = mibBuilder.importSymbols(
    "ADTRAN-SHARED-CND-SYSTEM-MIB",
    "adGenFrameRelay",
    "adGenFrameRelayID")

(adTAeSCUTrapAlarmLevel,) = mibBuilder.importSymbols(
    "ADTRAN-TAeSCUEXT1-MIB",
    "adTAeSCUTrapAlarmLevel")

(InterfaceIndex,
 ifIndex,
 ifOperStatus) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex",
    "ifOperStatus")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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

adGenFrameRelayMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 70, 29, 1)
)
if mibBuilder.loadTexts:
    adGenFrameRelayMib.setRevisions(
        ("2010-09-09 00:00",
         "2010-09-02 00:00",
         "2010-06-25 00:00",
         "2010-05-03 00:00",
         "2010-04-30 00:00",
         "2010-03-29 00:00",
         "2010-03-24 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AdGenFrameRelayMIBObjects_ObjectIdentity = ObjectIdentity
adGenFrameRelayMIBObjects = _AdGenFrameRelayMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 29, 1)
)
_AdGenFrGroup_ObjectIdentity = ObjectIdentity
adGenFrGroup = _AdGenFrGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 29, 1, 1)
)
_AdGenFrGroupTable_Object = MibTable
adGenFrGroupTable = _AdGenFrGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 29, 1, 1, 2)
)
if mibBuilder.loadTexts:
    adGenFrGroupTable.setStatus("current")
_AdGenFrGroupEntry_Object = MibTableRow
adGenFrGroupEntry = _AdGenFrGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 29, 1, 1, 2, 1)
)
adGenFrGroupEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adGenFrGroupEntry.setStatus("current")
_AdGenFrGroupRowStatus_Type = RowStatus
_AdGenFrGroupRowStatus_Object = MibTableColumn
adGenFrGroupRowStatus = _AdGenFrGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 29, 1, 1, 2, 1, 1),
    _AdGenFrGroupRowStatus_Type()
)
adGenFrGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenFrGroupRowStatus.setStatus("current")
_AdGenFrGroupStatusString_Type = DisplayString
_AdGenFrGroupStatusString_Object = MibTableColumn
adGenFrGroupStatusString = _AdGenFrGroupStatusString_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 29, 1, 1, 2, 1, 2),
    _AdGenFrGroupStatusString_Type()
)
adGenFrGroupStatusString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenFrGroupStatusString.setStatus("current")


class _AdGenFrGroupAdminStatus_Type(Integer32):
    """Custom type adGenFrGroupAdminStatus based on Integer32"""
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
        *(("up", 1),
          ("down", 2),
          ("testing", 3))
    )


_AdGenFrGroupAdminStatus_Type.__name__ = "Integer32"
_AdGenFrGroupAdminStatus_Object = MibTableColumn
adGenFrGroupAdminStatus = _AdGenFrGroupAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 29, 1, 1, 2, 1, 3),
    _AdGenFrGroupAdminStatus_Type()
)
adGenFrGroupAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenFrGroupAdminStatus.setStatus("current")


class _AdGenFrGroupLmiType_Type(Integer32):
    """Custom type adGenFrGroupLmiType based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("ansi617d1994", 3))
    )


_AdGenFrGroupLmiType_Type.__name__ = "Integer32"
_AdGenFrGroupLmiType_Object = MibTableColumn
adGenFrGroupLmiType = _AdGenFrGroupLmiType_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 29, 1, 1, 2, 1, 5),
    _AdGenFrGroupLmiType_Type()
)
adGenFrGroupLmiType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenFrGroupLmiType.setStatus("current")


class _AdGenFrGroupLmiStatus_Type(Integer32):
    """Custom type adGenFrGroupLmiStatus based on Integer32"""
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


_AdGenFrGroupLmiStatus_Type.__name__ = "Integer32"
_AdGenFrGroupLmiStatus_Object = MibTableColumn
adGenFrGroupLmiStatus = _AdGenFrGroupLmiStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 29, 1, 1, 2, 1, 6),
    _AdGenFrGroupLmiStatus_Type()
)
adGenFrGroupLmiStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenFrGroupLmiStatus.setStatus("current")
_AdGenFrGroupLmiEnquiryIn_Type = Counter32
_AdGenFrGroupLmiEnquiryIn_Object = MibTableColumn
adGenFrGroupLmiEnquiryIn = _AdGenFrGroupLmiEnquiryIn_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 29, 1, 1, 2, 1, 7),
    _AdGenFrGroupLmiEnquiryIn_Type()
)
adGenFrGroupLmiEnquiryIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenFrGroupLmiEnquiryIn.setStatus("current")
_AdGenFrGroupLmiEnquiryOut_Type = Counter32
_AdGenFrGroupLmiEnquiryOut_Object = MibTableColumn
adGenFrGroupLmiEnquiryOut = _AdGenFrGroupLmiEnquiryOut_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 29, 1, 1, 2, 1, 8),
    _AdGenFrGroupLmiEnquiryOut_Type()
)
adGenFrGroupLmiEnquiryOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenFrGroupLmiEnquiryOut.setStatus("current")
_AdGenFrGroupLmiStatusIn_Type = Counter32
_AdGenFrGroupLmiStatusIn_Object = MibTableColumn
adGenFrGroupLmiStatusIn = _AdGenFrGroupLmiStatusIn_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 29, 1, 1, 2, 1, 9),
    _AdGenFrGroupLmiStatusIn_Type()
)
adGenFrGroupLmiStatusIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenFrGroupLmiStatusIn.setStatus("current")
_AdGenFrGroupLmiStatusOut_Type = Counter32
_AdGenFrGroupLmiStatusOut_Object = MibTableColumn
adGenFrGroupLmiStatusOut = _AdGenFrGroupLmiStatusOut_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 29, 1, 1, 2, 1, 10),
    _AdGenFrGroupLmiStatusOut_Type()
)
adGenFrGroupLmiStatusOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenFrGroupLmiStatusOut.setStatus("current")
_AdGenFrGroupLmiInvalidIn_Type = Counter32
_AdGenFrGroupLmiInvalidIn_Object = MibTableColumn
adGenFrGroupLmiInvalidIn = _AdGenFrGroupLmiInvalidIn_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 29, 1, 1, 2, 1, 11),
    _AdGenFrGroupLmiInvalidIn_Type()
)
adGenFrGroupLmiInvalidIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenFrGroupLmiInvalidIn.setStatus("current")
_AdGenFrGroupLmiStatusEnqTimeouts_Type = Counter32
_AdGenFrGroupLmiStatusEnqTimeouts_Object = MibTableColumn
adGenFrGroupLmiStatusEnqTimeouts = _AdGenFrGroupLmiStatusEnqTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 29, 1, 1, 2, 1, 12),
    _AdGenFrGroupLmiStatusEnqTimeouts_Type()
)
adGenFrGroupLmiStatusEnqTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenFrGroupLmiStatusEnqTimeouts.setStatus("current")
_AdGenFrGroupLmiStatusTimeouts_Type = Counter32
_AdGenFrGroupLmiStatusTimeouts_Object = MibTableColumn
adGenFrGroupLmiStatusTimeouts = _AdGenFrGroupLmiStatusTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 29, 1, 1, 2, 1, 13),
    _AdGenFrGroupLmiStatusTimeouts_Type()
)
adGenFrGroupLmiStatusTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenFrGroupLmiStatusTimeouts.setStatus("current")


class _AdGenFrGroupClearCounters_Type(Integer32):
    """Custom type adGenFrGroupClearCounters based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset", 1)
    )


_AdGenFrGroupClearCounters_Type.__name__ = "Integer32"
_AdGenFrGroupClearCounters_Object = MibTableColumn
adGenFrGroupClearCounters = _AdGenFrGroupClearCounters_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 29, 1, 1, 2, 1, 14),
    _AdGenFrGroupClearCounters_Type()
)
adGenFrGroupClearCounters.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenFrGroupClearCounters.setStatus("current")


class _AdGenFrGroupClearPmHistory_Type(Integer32):
    """Custom type adGenFrGroupClearPmHistory based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset", 1)
    )


_AdGenFrGroupClearPmHistory_Type.__name__ = "Integer32"
_AdGenFrGroupClearPmHistory_Object = MibTableColumn
adGenFrGroupClearPmHistory = _AdGenFrGroupClearPmHistory_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 29, 1, 1, 2, 1, 15),
    _AdGenFrGroupClearPmHistory_Type()
)
adGenFrGroupClearPmHistory.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenFrGroupClearPmHistory.setStatus("current")
_AdGenFrGroupLinkLastCreateError_Type = DisplayString
_AdGenFrGroupLinkLastCreateError_Object = MibTableColumn
adGenFrGroupLinkLastCreateError = _AdGenFrGroupLinkLastCreateError_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 29, 1, 1, 2, 1, 16),
    _AdGenFrGroupLinkLastCreateError_Type()
)
adGenFrGroupLinkLastCreateError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenFrGroupLinkLastCreateError.setStatus("current")
_AdGenFrGroupPvcLastCreateError_Type = DisplayString
_AdGenFrGroupPvcLastCreateError_Object = MibTableColumn
adGenFrGroupPvcLastCreateError = _AdGenFrGroupPvcLastCreateError_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 29, 1, 1, 2, 1, 17),
    _AdGenFrGroupPvcLastCreateError_Type()
)
adGenFrGroupPvcLastCreateError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenFrGroupPvcLastCreateError.setStatus("current")
_AdGenFrGroupCurrentTable_Object = MibTable
adGenFrGroupCurrentTable = _AdGenFrGroupCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 29, 1, 1, 3)
)
if mibBuilder.loadTexts:
    adGenFrGroupCurrentTable.setStatus("current")
_AdGenFrGroupCurrentEntry_Object = MibTableRow
adGenFrGroupCurrentEntry = _AdGenFrGroupCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 29, 1, 1, 3, 1)
)
adGenFrGroupCurrentEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adGenFrGroupCurrentEntry.setStatus("current")
_AdGenFrGroupCurrentInOctets_Type = Counter32
_AdGenFrGroupCurrentInOctets_Object = MibTableColumn
adGenFrGroupCurrentInOctets = _AdGenFrGroupCurrentInOctets_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 29, 1, 1, 3, 1, 1),
    _AdGenFrGroupCurrentInOctets_Type()
)
adGenFrGroupCurrentInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenFrGroupCurrentInOctets.setStatus("current")
_AdGenFrGroupCurrentInPkts_Type = Counter32
_AdGenFrGroupCurrentInPkts_Object = MibTableColumn
adGenFrGroupCurrentInPkts = _AdGenFrGroupCurrentInPkts_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 29, 1, 1, 3, 1, 2),
    _AdGenFrGroupCurrentInPkts_Type()
)
adGenFrGroupCurrentInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenFrGroupCurrentInPkts.setStatus("current")
_AdGenFrGroupCurrentInDiscards_Type = Counter32
_AdGenFrGroupCurrentInDiscards_Object = MibTableColumn
adGenFrGroupCurrentInDiscards = _AdGenFrGroupCurrentInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 29, 1, 1, 3, 1, 3),
    _AdGenFrGroupCurrentInDiscards_Type()
)
adGenFrGroupCurrentInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenFrGroupCurrentInDiscards.setStatus("current")
_AdGenFrGroupCurrentInErrors_Type = Counter32
_AdGenFrGroupCurrentInErrors_Object = MibTableColumn
adGenFrGroupCurrentInErrors = _AdGenFrGroupCurrentInErrors_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 29, 1, 1, 3, 1, 4),
    _AdGenFrGroupCurrentInErrors_Type()
)
adGenFrGroupCurrentInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenFrGroupCurrentInErrors.setStatus("current")
_AdGenFrGroupCurrentOutOctets_Type = Counter32
_AdGenFrGroupCurrentOutOctets_Object = MibTableColumn
adGenFrGroupCurrentOutOctets = _AdGenFrGroupCurrentOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 29, 1, 1, 3, 1, 5),
    _AdGenFrGroupCurrentOutOctets_Type()
)
adGenFrGroupCurrentOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenFrGroupCurrentOutOctets.setStatus("current")
_AdGenFrGroupCurrentOutPkts_Type = Counter32
_AdGenFrGroupCurrentOutPkts_Object = MibTableColumn
adGenFrGroupCurrentOutPkts = _AdGenFrGroupCurrentOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 29, 1, 1, 3, 1, 6),
    _AdGenFrGroupCurrentOutPkts_Type()
)
adGenFrGroupCurrentOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenFrGroupCurrentOutPkts.setStatus("current")
_AdGenFrGroupCurrentOutDiscards_Type = Counter32
_AdGenFrGroupCurrentOutDiscards_Object = MibTableColumn
adGenFrGroupCurrentOutDiscards = _AdGenFrGroupCurrentOutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 29, 1, 1, 3, 1, 7),
    _AdGenFrGroupCurrentOutDiscards_Type()
)
adGenFrGroupCurrentOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenFrGroupCurrentOutDiscards.setStatus("current")
_AdGenFrGroupCurrentOutErrors_Type = Counter32
_AdGenFrGroupCurrentOutErrors_Object = MibTableColumn
adGenFrGroupCurrentOutErrors = _AdGenFrGroupCurrentOutErrors_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 29, 1, 1, 3, 1, 8),
    _AdGenFrGroupCurrentOutErrors_Type()
)
adGenFrGroupCurrentOutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenFrGroupCurrentOutErrors.setStatus("current")
_AdGenFrGroupCurrentLmiEnquiryIn_Type = Counter32
_AdGenFrGroupCurrentLmiEnquiryIn_Object = MibTableColumn
adGenFrGroupCurrentLmiEnquiryIn = _AdGenFrGroupCurrentLmiEnquiryIn_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 29, 1, 1, 3, 1, 9),
    _AdGenFrGroupCurrentLmiEnquiryIn_Type()
)
adGenFrGroupCurrentLmiEnquiryIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenFrGroupCurrentLmiEnquiryIn.setStatus("current")
_AdGenFrGroupCurrentLmiEnquiryOut_Type = Counter32
_AdGenFrGroupCurrentLmiEnquiryOut_Object = MibTableColumn
adGenFrGroupCurrentLmiEnquiryOut = _AdGenFrGroupCurrentLmiEnquiryOut_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 29, 1, 1, 3, 1, 10),
    _AdGenFrGroupCurrentLmiEnquiryOut_Type()
)
adGenFrGroupCurrentLmiEnquiryOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenFrGroupCurrentLmiEnquiryOut.setStatus("current")
_AdGenFrGroupCurrentLmiStatusIn_Type = Counter32
_AdGenFrGroupCurrentLmiStatusIn_Object = MibTableColumn
adGenFrGroupCurrentLmiStatusIn = _AdGenFrGroupCurrentLmiStatusIn_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 29, 1, 1, 3, 1, 11),
    _AdGenFrGroupCurrentLmiStatusIn_Type()
)
adGenFrGroupCurrentLmiStatusIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenFrGroupCurrentLmiStatusIn.setStatus("current")
_AdGenFrGroupCurrentLmiStatusOut_Type = Counter32
_AdGenFrGroupCurrentLmiStatusOut_Object = MibTableColumn
adGenFrGroupCurrentLmiStatusOut = _AdGenFrGroupCurrentLmiStatusOut_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 29, 1, 1, 3, 1, 12),
    _AdGenFrGroupCurrentLmiStatusOut_Type()
)
adGenFrGroupCurrentLmiStatusOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenFrGroupCurrentLmiStatusOut.setStatus("current")
_AdGenFrGroupCurrentLmiInvalidIn_Type = Counter32
_AdGenFrGroupCurrentLmiInvalidIn_Object = MibTableColumn
adGenFrGroupCurrentLmiInvalidIn = _AdGenFrGroupCurrentLmiInvalidIn_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 29, 1, 1, 3, 1, 13),
    _AdGenFrGroupCurrentLmiInvalidIn_Type()
)
adGenFrGroupCurrentLmiInvalidIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenFrGroupCurrentLmiInvalidIn.setStatus("current")
_AdGenFrGroupCurrentLmiStatusEnqTimeouts_Type = Counter32
_AdGenFrGroupCurrentLmiStatusEnqTimeouts_Object = MibTableColumn
adGenFrGroupCurrentLmiStatusEnqTimeouts = _AdGenFrGroupCurrentLmiStatusEnqTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 29, 1, 1, 3, 1, 14),
    _AdGenFrGroupCurrentLmiStatusEnqTimeouts_Type()
)
adGenFrGroupCurrentLmiStatusEnqTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenFrGroupCurrentLmiStatusEnqTimeouts.setStatus("current")
_AdGenFrGroupCurrentLmiStatusTimeouts_Type = Counter32
_AdGenFrGroupCurrentLmiStatusTimeouts_Object = MibTableColumn
adGenFrGroupCurrentLmiStatusTimeouts = _AdGenFrGroupCurrentLmiStatusTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 29, 1, 1, 3, 1, 15),
    _AdGenFrGroupCurrentLmiStatusTimeouts_Type()
)
adGenFrGroupCurrentLmiStatusTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenFrGroupCurrentLmiStatusTimeouts.setStatus("current")
_AdGenFrGroupCurrentNetworkInactive_Type = Counter32
_AdGenFrGroupCurrentNetworkInactive_Object = MibTableColumn
adGenFrGroupCurrentNetworkInactive = _AdGenFrGroupCurrentNetworkInactive_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 29, 1, 1, 3, 1, 16),
    _AdGenFrGroupCurrentNetworkInactive_Type()
)
adGenFrGroupCurrentNetworkInactive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenFrGroupCurrentNetworkInactive.setStatus("current")
_AdGenFrGroupIntervalTable_Object = MibTable
adGenFrGroupIntervalTable = _AdGenFrGroupIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 29, 1, 1, 4)
)
if mibBuilder.loadTexts:
    adGenFrGroupIntervalTable.setStatus("current")
_AdGenFrGroupIntervalEntry_Object = MibTableRow
adGenFrGroupIntervalEntry = _AdGenFrGroupIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 29, 1, 1, 4, 1)
)
adGenFrGroupIntervalEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ADTRAN-GEN-FRAME-RELAY-MIB", "adGenFrGroupIntervalNumber"),
)
if mibBuilder.loadTexts:
    adGenFrGroupIntervalEntry.setStatus("current")


class _AdGenFrGroupIntervalNumber_Type(Integer32):
    """Custom type adGenFrGroupIntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_AdGenFrGroupIntervalNumber_Type.__name__ = "Integer32"
_AdGenFrGroupIntervalNumber_Object = MibTableColumn
adGenFrGroupIntervalNumber = _AdGenFrGroupIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 29, 1, 1, 4, 1, 1),
    _AdGenFrGroupIntervalNumber_Type()
)
adGenFrGroupIntervalNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adGenFrGroupIntervalNumber.setStatus("current")
_AdGenFrGroupIntervalTimeStamp_Type = DisplayString
_AdGenFrGroupIntervalTimeStamp_Object = MibTableColumn
adGenFrGroupIntervalTimeStamp = _AdGenFrGroupIntervalTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 29, 1, 1, 4, 1, 2),
    _AdGenFrGroupIntervalTimeStamp_Type()
)
adGenFrGroupIntervalTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenFrGroupIntervalTimeStamp.setStatus("current")
_AdGenFrGroupIntervalInOctets_Type = Counter32
_AdGenFrGroupIntervalInOctets_Object = MibTableColumn
adGenFrGroupIntervalInOctets = _AdGenFrGroupIntervalInOctets_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 29, 1, 1, 4, 1, 3),
    _AdGenFrGroupIntervalInOctets_Type()
)
adGenFrGroupIntervalInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenFrGroupIntervalInOctets.setStatus("current")
_AdGenFrGroupIntervalInPkts_Type = Counter32
_AdGenFrGroupIntervalInPkts_Object = MibTableColumn
adGenFrGroupIntervalInPkts = _AdGenFrGroupIntervalInPkts_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 29, 1, 1, 4, 1, 4),
    _AdGenFrGroupIntervalInPkts_Type()
)
adGenFrGroupIntervalInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenFrGroupIntervalInPkts.setStatus("current")
_AdGenFrGroupIntervalInDiscards_Type = Counter32
_AdGenFrGroupIntervalInDiscards_Object = MibTableColumn
adGenFrGroupIntervalInDiscards = _AdGenFrGroupIntervalInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 29, 1, 1, 4, 1, 5),
    _AdGenFrGroupIntervalInDiscards_Type()
)
adGenFrGroupIntervalInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenFrGroupIntervalInDiscards.setStatus("current")
_AdGenFrGroupIntervalInErrors_Type = Counter32
_AdGenFrGroupIntervalInErrors_Object = MibTableColumn
adGenFrGroupIntervalInErrors = _AdGenFrGroupIntervalInErrors_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 29, 1, 1, 4, 1, 6),
    _AdGenFrGroupIntervalInErrors_Type()
)
adGenFrGroupIntervalInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenFrGroupIntervalInErrors.setStatus("current")
_AdGenFrGroupIntervalOutOctets_Type = Counter32
_AdGenFrGroupIntervalOutOctets_Object = MibTableColumn
adGenFrGroupIntervalOutOctets = _AdGenFrGroupIntervalOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 29, 1, 1, 4, 1, 7),
    _AdGenFrGroupIntervalOutOctets_Type()
)
adGenFrGroupIntervalOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenFrGroupIntervalOutOctets.setStatus("current")
_AdGenFrGroupIntervalOutPkts_Type = Counter32
_AdGenFrGroupIntervalOutPkts_Object = MibTableColumn
adGenFrGroupIntervalOutPkts = _AdGenFrGroupIntervalOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 29, 1, 1, 4, 1, 8),
    _AdGenFrGroupIntervalOutPkts_Type()
)
adGenFrGroupIntervalOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenFrGroupIntervalOutPkts.setStatus("current")
_AdGenFrGroupIntervalOutDiscards_Type = Counter32
_AdGenFrGroupIntervalOutDiscards_Object = MibTableColumn
adGenFrGroupIntervalOutDiscards = _AdGenFrGroupIntervalOutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 29, 1, 1, 4, 1, 9),
    _AdGenFrGroupIntervalOutDiscards_Type()
)
adGenFrGroupIntervalOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenFrGroupIntervalOutDiscards.setStatus("current")
_AdGenFrGroupIntervalOutErrors_Type = Counter32
_AdGenFrGroupIntervalOutErrors_Object = MibTableColumn
adGenFrGroupIntervalOutErrors = _AdGenFrGroupIntervalOutErrors_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 29, 1, 1, 4, 1, 10),
    _AdGenFrGroupIntervalOutErrors_Type()
)
adGenFrGroupIntervalOutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenFrGroupIntervalOutErrors.setStatus("current")
_AdGenFrGroupIntervalLmiEnquiryIn_Type = Counter32
_AdGenFrGroupIntervalLmiEnquiryIn_Object = MibTableColumn
adGenFrGroupIntervalLmiEnquiryIn = _AdGenFrGroupIntervalLmiEnquiryIn_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 29, 1, 1, 4, 1, 11),
    _AdGenFrGroupIntervalLmiEnquiryIn_Type()
)
adGenFrGroupIntervalLmiEnquiryIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenFrGroupIntervalLmiEnquiryIn.setStatus("current")
_AdGenFrGroupIntervalLmiEnquiryOut_Type = Counter32
_AdGenFrGroupIntervalLmiEnquiryOut_Object = MibTableColumn
adGenFrGroupIntervalLmiEnquiryOut = _AdGenFrGroupIntervalLmiEnquiryOut_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 29, 1, 1, 4, 1, 12),
    _AdGenFrGroupIntervalLmiEnquiryOut_Type()
)
adGenFrGroupIntervalLmiEnquiryOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenFrGroupIntervalLmiEnquiryOut.setStatus("current")
_AdGenFrGroupIntervalLmiStatusIn_Type = Counter32
_AdGenFrGroupIntervalLmiStatusIn_Object = MibTableColumn
adGenFrGroupIntervalLmiStatusIn = _AdGenFrGroupIntervalLmiStatusIn_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 29, 1, 1, 4, 1, 13),
    _AdGenFrGroupIntervalLmiStatusIn_Type()
)
adGenFrGroupIntervalLmiStatusIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenFrGroupIntervalLmiStatusIn.setStatus("current")
_AdGenFrGroupIntervalLmiStatusOut_Type = Counter32
_AdGenFrGroupIntervalLmiStatusOut_Object = MibTableColumn
adGenFrGroupIntervalLmiStatusOut = _AdGenFrGroupIntervalLmiStatusOut_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 29, 1, 1, 4, 1, 14),
    _AdGenFrGroupIntervalLmiStatusOut_Type()
)
adGenFrGroupIntervalLmiStatusOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenFrGroupIntervalLmiStatusOut.setStatus("current")
_AdGenFrGroupIntervalLmiInvalidIn_Type = Counter32
_AdGenFrGroupIntervalLmiInvalidIn_Object = MibTableColumn
adGenFrGroupIntervalLmiInvalidIn = _AdGenFrGroupIntervalLmiInvalidIn_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 29, 1, 1, 4, 1, 15),
    _AdGenFrGroupIntervalLmiInvalidIn_Type()
)
adGenFrGroupIntervalLmiInvalidIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenFrGroupIntervalLmiInvalidIn.setStatus("current")
_AdGenFrGroupIntervalLmiStatusEnqTimeouts_Type = Counter32
_AdGenFrGroupIntervalLmiStatusEnqTimeouts_Object = MibTableColumn
adGenFrGroupIntervalLmiStatusEnqTimeouts = _AdGenFrGroupIntervalLmiStatusEnqTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 29, 1, 1, 4, 1, 16),
    _AdGenFrGroupIntervalLmiStatusEnqTimeouts_Type()
)
adGenFrGroupIntervalLmiStatusEnqTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenFrGroupIntervalLmiStatusEnqTimeouts.setStatus("current")
_AdGenFrGroupIntervalLmiStatusTimeouts_Type = Counter32
_AdGenFrGroupIntervalLmiStatusTimeouts_Object = MibTableColumn
adGenFrGroupIntervalLmiStatusTimeouts = _AdGenFrGroupIntervalLmiStatusTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 29, 1, 1, 4, 1, 17),
    _AdGenFrGroupIntervalLmiStatusTimeouts_Type()
)
adGenFrGroupIntervalLmiStatusTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenFrGroupIntervalLmiStatusTimeouts.setStatus("current")
_AdGenFrGroupIntervalNetworkInactive_Type = Counter32
_AdGenFrGroupIntervalNetworkInactive_Object = MibTableColumn
adGenFrGroupIntervalNetworkInactive = _AdGenFrGroupIntervalNetworkInactive_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 29, 1, 1, 4, 1, 18),
    _AdGenFrGroupIntervalNetworkInactive_Type()
)
adGenFrGroupIntervalNetworkInactive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenFrGroupIntervalNetworkInactive.setStatus("current")
_AdGenFrGroupDayCurrentTable_Object = MibTable
adGenFrGroupDayCurrentTable = _AdGenFrGroupDayCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 29, 1, 1, 5)
)
if mibBuilder.loadTexts:
    adGenFrGroupDayCurrentTable.setStatus("current")
_AdGenFrGroupDayCurrentEntry_Object = MibTableRow
adGenFrGroupDayCurrentEntry = _AdGenFrGroupDayCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 29, 1, 1, 5, 1)
)
adGenFrGroupDayCurrentEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adGenFrGroupDayCurrentEntry.setStatus("current")
_AdGenFrGroupDayCurrentInOctets_Type = Counter32
_AdGenFrGroupDayCurrentInOctets_Object = MibTableColumn
adGenFrGroupDayCurrentInOctets = _AdGenFrGroupDayCurrentInOctets_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 29, 1, 1, 5, 1, 1),
    _AdGenFrGroupDayCurrentInOctets_Type()
)
adGenFrGroupDayCurrentInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenFrGroupDayCurrentInOctets.setStatus("current")
_AdGenFrGroupDayCurrentInPkts_Type = Counter32
_AdGenFrGroupDayCurrentInPkts_Object = MibTableColumn
adGenFrGroupDayCurrentInPkts = _AdGenFrGroupDayCurrentInPkts_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 29, 1, 1, 5, 1, 2),
    _AdGenFrGroupDayCurrentInPkts_Type()
)
adGenFrGroupDayCurrentInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenFrGroupDayCurrentInPkts.setStatus("current")
_AdGenFrGroupDayCurrentInDiscards_Type = Counter32
_AdGenFrGroupDayCurrentInDiscards_Object = MibTableColumn
adGenFrGroupDayCurrentInDiscards = _AdGenFrGroupDayCurrentInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 29, 1, 1, 5, 1, 3),
    _AdGenFrGroupDayCurrentInDiscards_Type()
)
adGenFrGroupDayCurrentInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenFrGroupDayCurrentInDiscards.setStatus("current")
_AdGenFrGroupDayCurrentInErrors_Type = Counter32
_AdGenFrGroupDayCurrentInErrors_Object = MibTableColumn
adGenFrGroupDayCurrentInErrors = _AdGenFrGroupDayCurrentInErrors_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 29, 1, 1, 5, 1, 4),
    _AdGenFrGroupDayCurrentInErrors_Type()
)
adGenFrGroupDayCurrentInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenFrGroupDayCurrentInErrors.setStatus("current")
_AdGenFrGroupDayCurrentOutOctets_Type = Counter32
_AdGenFrGroupDayCurrentOutOctets_Object = MibTableColumn
adGenFrGroupDayCurrentOutOctets = _AdGenFrGroupDayCurrentOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 29, 1, 1, 5, 1, 5),
    _AdGenFrGroupDayCurrentOutOctets_Type()
)
adGenFrGroupDayCurrentOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenFrGroupDayCurrentOutOctets.setStatus("current")
_AdGenFrGroupDayCurrentOutPkts_Type = Counter32
_AdGenFrGroupDayCurrentOutPkts_Object = MibTableColumn
adGenFrGroupDayCurrentOutPkts = _AdGenFrGroupDayCurrentOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 29, 1, 1, 5, 1, 6),
    _AdGenFrGroupDayCurrentOutPkts_Type()
)
adGenFrGroupDayCurrentOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenFrGroupDayCurrentOutPkts.setStatus("current")
_AdGenFrGroupDayCurrentOutDiscards_Type = Counter32
_AdGenFrGroupDayCurrentOutDiscards_Object = MibTableColumn
adGenFrGroupDayCurrentOutDiscards = _AdGenFrGroupDayCurrentOutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 29, 1, 1, 5, 1, 7),
    _AdGenFrGroupDayCurrentOutDiscards_Type()
)
adGenFrGroupDayCurrentOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenFrGroupDayCurrentOutDiscards.setStatus("current")
_AdGenFrGroupDayCurrentOutErrors_Type = Counter32
_AdGenFrGroupDayCurrentOutErrors_Object = MibTableColumn
adGenFrGroupDayCurrentOutErrors = _AdGenFrGroupDayCurrentOutErrors_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 29, 1, 1, 5, 1, 8),
    _AdGenFrGroupDayCurrentOutErrors_Type()
)
adGenFrGroupDayCurrentOutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenFrGroupDayCurrentOutErrors.setStatus("current")
_AdGenFrGroupDayCurrentLmiEnquiryIn_Type = Counter32
_AdGenFrGroupDayCurrentLmiEnquiryIn_Object = MibTableColumn
adGenFrGroupDayCurrentLmiEnquiryIn = _AdGenFrGroupDayCurrentLmiEnquiryIn_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 29, 1, 1, 5, 1, 9),
    _AdGenFrGroupDayCurrentLmiEnquiryIn_Type()
)
adGenFrGroupDayCurrentLmiEnquiryIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenFrGroupDayCurrentLmiEnquiryIn.setStatus("current")
_AdGenFrGroupDayCurrentLmiEnquiryOut_Type = Counter32
_AdGenFrGroupDayCurrentLmiEnquiryOut_Object = MibTableColumn
adGenFrGroupDayCurrentLmiEnquiryOut = _AdGenFrGroupDayCurrentLmiEnquiryOut_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 29, 1, 1, 5, 1, 10),
    _AdGenFrGroupDayCurrentLmiEnquiryOut_Type()
)
adGenFrGroupDayCurrentLmiEnquiryOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenFrGroupDayCurrentLmiEnquiryOut.setStatus("current")
_AdGenFrGroupDayCurrentLmiStatusIn_Type = Counter32
_AdGenFrGroupDayCurrentLmiStatusIn_Object = MibTableColumn
adGenFrGroupDayCurrentLmiStatusIn = _AdGenFrGroupDayCurrentLmiStatusIn_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 29, 1, 1, 5, 1, 11),
    _AdGenFrGroupDayCurrentLmiStatusIn_Type()
)
adGenFrGroupDayCurrentLmiStatusIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenFrGroupDayCurrentLmiStatusIn.setStatus("current")
_AdGenFrGroupDayCurrentLmiStatusOut_Type = Counter32
_AdGenFrGroupDayCurrentLmiStatusOut_Object = MibTableColumn
adGenFrGroupDayCurrentLmiStatusOut = _AdGenFrGroupDayCurrentLmiStatusOut_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 29, 1, 1, 5, 1, 12),
    _AdGenFrGroupDayCurrentLmiStatusOut_Type()
)
adGenFrGroupDayCurrentLmiStatusOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenFrGroupDayCurrentLmiStatusOut.setStatus("current")
_AdGenFrGroupDayCurrentLmiInvalidIn_Type = Counter32
_AdGenFrGroupDayCurrentLmiInvalidIn_Object = MibTableColumn
adGenFrGroupDayCurrentLmiInvalidIn = _AdGenFrGroupDayCurrentLmiInvalidIn_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 29, 1, 1, 5, 1, 13),
    _AdGenFrGroupDayCurrentLmiInvalidIn_Type()
)
adGenFrGroupDayCurrentLmiInvalidIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenFrGroupDayCurrentLmiInvalidIn.setStatus("current")
_AdGenFrGroupDayCurrentLmiStatusEnqTimeouts_Type = Counter32
_AdGenFrGroupDayCurrentLmiStatusEnqTimeouts_Object = MibTableColumn
adGenFrGroupDayCurrentLmiStatusEnqTimeouts = _AdGenFrGroupDayCurrentLmiStatusEnqTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 29, 1, 1, 5, 1, 14),
    _AdGenFrGroupDayCurrentLmiStatusEnqTimeouts_Type()
)
adGenFrGroupDayCurrentLmiStatusEnqTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenFrGroupDayCurrentLmiStatusEnqTimeouts.setStatus("current")
_AdGenFrGroupDayCurrentLmiStatusTimeouts_Type = Counter32
_AdGenFrGroupDayCurrentLmiStatusTimeouts_Object = MibTableColumn
adGenFrGroupDayCurrentLmiStatusTimeouts = _AdGenFrGroupDayCurrentLmiStatusTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 29, 1, 1, 5, 1, 15),
    _AdGenFrGroupDayCurrentLmiStatusTimeouts_Type()
)
adGenFrGroupDayCurrentLmiStatusTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenFrGroupDayCurrentLmiStatusTimeouts.setStatus("current")
_AdGenFrGroupDayCurrentNetworkInactive_Type = Counter32
_AdGenFrGroupDayCurrentNetworkInactive_Object = MibTableColumn
adGenFrGroupDayCurrentNetworkInactive = _AdGenFrGroupDayCurrentNetworkInactive_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 29, 1, 1, 5, 1, 16),
    _AdGenFrGroupDayCurrentNetworkInactive_Type()
)
adGenFrGroupDayCurrentNetworkInactive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenFrGroupDayCurrentNetworkInactive.setStatus("current")
_AdGenFrGroupDayIntervalTable_Object = MibTable
adGenFrGroupDayIntervalTable = _AdGenFrGroupDayIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 29, 1, 1, 6)
)
if mibBuilder.loadTexts:
    adGenFrGroupDayIntervalTable.setStatus("current")
_AdGenFrGroupDayIntervalEntry_Object = MibTableRow
adGenFrGroupDayIntervalEntry = _AdGenFrGroupDayIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 29, 1, 1, 6, 1)
)
adGenFrGroupDayIntervalEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ADTRAN-GEN-FRAME-RELAY-MIB", "adGenFrGroupDayIntervalNumber"),
)
if mibBuilder.loadTexts:
    adGenFrGroupDayIntervalEntry.setStatus("current")


class _AdGenFrGroupDayIntervalNumber_Type(Integer32):
    """Custom type adGenFrGroupDayIntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_AdGenFrGroupDayIntervalNumber_Type.__name__ = "Integer32"
_AdGenFrGroupDayIntervalNumber_Object = MibTableColumn
adGenFrGroupDayIntervalNumber = _AdGenFrGroupDayIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 29, 1, 1, 6, 1, 1),
    _AdGenFrGroupDayIntervalNumber_Type()
)
adGenFrGroupDayIntervalNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adGenFrGroupDayIntervalNumber.setStatus("current")
_AdGenFrGroupDayIntervalTimeStamp_Type = DisplayString
_AdGenFrGroupDayIntervalTimeStamp_Object = MibTableColumn
adGenFrGroupDayIntervalTimeStamp = _AdGenFrGroupDayIntervalTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 29, 1, 1, 6, 1, 2),
    _AdGenFrGroupDayIntervalTimeStamp_Type()
)
adGenFrGroupDayIntervalTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenFrGroupDayIntervalTimeStamp.setStatus("current")
_AdGenFrGroupDayIntervalInOctets_Type = Counter32
_AdGenFrGroupDayIntervalInOctets_Object = MibTableColumn
adGenFrGroupDayIntervalInOctets = _AdGenFrGroupDayIntervalInOctets_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 29, 1, 1, 6, 1, 3),
    _AdGenFrGroupDayIntervalInOctets_Type()
)
adGenFrGroupDayIntervalInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenFrGroupDayIntervalInOctets.setStatus("current")
_AdGenFrGroupDayIntervalInPkts_Type = Counter32
_AdGenFrGroupDayIntervalInPkts_Object = MibTableColumn
adGenFrGroupDayIntervalInPkts = _AdGenFrGroupDayIntervalInPkts_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 29, 1, 1, 6, 1, 4),
    _AdGenFrGroupDayIntervalInPkts_Type()
)
adGenFrGroupDayIntervalInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenFrGroupDayIntervalInPkts.setStatus("current")
_AdGenFrGroupDayIntervalInDiscards_Type = Counter32
_AdGenFrGroupDayIntervalInDiscards_Object = MibTableColumn
adGenFrGroupDayIntervalInDiscards = _AdGenFrGroupDayIntervalInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 29, 1, 1, 6, 1, 5),
    _AdGenFrGroupDayIntervalInDiscards_Type()
)
adGenFrGroupDayIntervalInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenFrGroupDayIntervalInDiscards.setStatus("current")
_AdGenFrGroupDayIntervalInErrors_Type = Counter32
_AdGenFrGroupDayIntervalInErrors_Object = MibTableColumn
adGenFrGroupDayIntervalInErrors = _AdGenFrGroupDayIntervalInErrors_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 29, 1, 1, 6, 1, 6),
    _AdGenFrGroupDayIntervalInErrors_Type()
)
adGenFrGroupDayIntervalInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenFrGroupDayIntervalInErrors.setStatus("current")
_AdGenFrGroupDayIntervalOutOctets_Type = Counter32
_AdGenFrGroupDayIntervalOutOctets_Object = MibTableColumn
adGenFrGroupDayIntervalOutOctets = _AdGenFrGroupDayIntervalOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 29, 1, 1, 6, 1, 7),
    _AdGenFrGroupDayIntervalOutOctets_Type()
)
adGenFrGroupDayIntervalOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenFrGroupDayIntervalOutOctets.setStatus("current")
_AdGenFrGroupDayIntervalOutPkts_Type = Counter32
_AdGenFrGroupDayIntervalOutPkts_Object = MibTableColumn
adGenFrGroupDayIntervalOutPkts = _AdGenFrGroupDayIntervalOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 29, 1, 1, 6, 1, 8),
    _AdGenFrGroupDayIntervalOutPkts_Type()
)
adGenFrGroupDayIntervalOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenFrGroupDayIntervalOutPkts.setStatus("current")
_AdGenFrGroupDayIntervalOutDiscards_Type = Counter32
_AdGenFrGroupDayIntervalOutDiscards_Object = MibTableColumn
adGenFrGroupDayIntervalOutDiscards = _AdGenFrGroupDayIntervalOutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 29, 1, 1, 6, 1, 9),
    _AdGenFrGroupDayIntervalOutDiscards_Type()
)
adGenFrGroupDayIntervalOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenFrGroupDayIntervalOutDiscards.setStatus("current")
_AdGenFrGroupDayIntervalOutErrors_Type = Counter32
_AdGenFrGroupDayIntervalOutErrors_Object = MibTableColumn
adGenFrGroupDayIntervalOutErrors = _AdGenFrGroupDayIntervalOutErrors_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 29, 1, 1, 6, 1, 10),
    _AdGenFrGroupDayIntervalOutErrors_Type()
)
adGenFrGroupDayIntervalOutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenFrGroupDayIntervalOutErrors.setStatus("current")
_AdGenFrGroupDayIntervalLmiEnquiryIn_Type = Counter32
_AdGenFrGroupDayIntervalLmiEnquiryIn_Object = MibTableColumn
adGenFrGroupDayIntervalLmiEnquiryIn = _AdGenFrGroupDayIntervalLmiEnquiryIn_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 29, 1, 1, 6, 1, 11),
    _AdGenFrGroupDayIntervalLmiEnquiryIn_Type()
)
adGenFrGroupDayIntervalLmiEnquiryIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenFrGroupDayIntervalLmiEnquiryIn.setStatus("current")
_AdGenFrGroupDayIntervalLmiEnquiryOut_Type = Counter32
_AdGenFrGroupDayIntervalLmiEnquiryOut_Object = MibTableColumn
adGenFrGroupDayIntervalLmiEnquiryOut = _AdGenFrGroupDayIntervalLmiEnquiryOut_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 29, 1, 1, 6, 1, 12),
    _AdGenFrGroupDayIntervalLmiEnquiryOut_Type()
)
adGenFrGroupDayIntervalLmiEnquiryOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenFrGroupDayIntervalLmiEnquiryOut.setStatus("current")
_AdGenFrGroupDayIntervalLmiStatusIn_Type = Counter32
_AdGenFrGroupDayIntervalLmiStatusIn_Object = MibTableColumn
adGenFrGroupDayIntervalLmiStatusIn = _AdGenFrGroupDayIntervalLmiStatusIn_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 29, 1, 1, 6, 1, 13),
    _AdGenFrGroupDayIntervalLmiStatusIn_Type()
)
adGenFrGroupDayIntervalLmiStatusIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenFrGroupDayIntervalLmiStatusIn.setStatus("current")
_AdGenFrGroupDayIntervalLmiStatusOut_Type = Counter32
_AdGenFrGroupDayIntervalLmiStatusOut_Object = MibTableColumn
adGenFrGroupDayIntervalLmiStatusOut = _AdGenFrGroupDayIntervalLmiStatusOut_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 29, 1, 1, 6, 1, 14),
    _AdGenFrGroupDayIntervalLmiStatusOut_Type()
)
adGenFrGroupDayIntervalLmiStatusOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenFrGroupDayIntervalLmiStatusOut.setStatus("current")
_AdGenFrGroupDayIntervalLmiInvalidIn_Type = Counter32
_AdGenFrGroupDayIntervalLmiInvalidIn_Object = MibTableColumn
adGenFrGroupDayIntervalLmiInvalidIn = _AdGenFrGroupDayIntervalLmiInvalidIn_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 29, 1, 1, 6, 1, 15),
    _AdGenFrGroupDayIntervalLmiInvalidIn_Type()
)
adGenFrGroupDayIntervalLmiInvalidIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenFrGroupDayIntervalLmiInvalidIn.setStatus("current")
_AdGenFrGroupDayIntervalLmiStatusEnqTimeouts_Type = Counter32
_AdGenFrGroupDayIntervalLmiStatusEnqTimeouts_Object = MibTableColumn
adGenFrGroupDayIntervalLmiStatusEnqTimeouts = _AdGenFrGroupDayIntervalLmiStatusEnqTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 29, 1, 1, 6, 1, 16),
    _AdGenFrGroupDayIntervalLmiStatusEnqTimeouts_Type()
)
adGenFrGroupDayIntervalLmiStatusEnqTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenFrGroupDayIntervalLmiStatusEnqTimeouts.setStatus("current")
_AdGenFrGroupDayIntervalLmiStatusTimeouts_Type = Counter32
_AdGenFrGroupDayIntervalLmiStatusTimeouts_Object = MibTableColumn
adGenFrGroupDayIntervalLmiStatusTimeouts = _AdGenFrGroupDayIntervalLmiStatusTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 29, 1, 1, 6, 1, 17),
    _AdGenFrGroupDayIntervalLmiStatusTimeouts_Type()
)
adGenFrGroupDayIntervalLmiStatusTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenFrGroupDayIntervalLmiStatusTimeouts.setStatus("current")
_AdGenFrGroupDayIntervalNetworkInactive_Type = Counter32
_AdGenFrGroupDayIntervalNetworkInactive_Object = MibTableColumn
adGenFrGroupDayIntervalNetworkInactive = _AdGenFrGroupDayIntervalNetworkInactive_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 29, 1, 1, 6, 1, 18),
    _AdGenFrGroupDayIntervalNetworkInactive_Type()
)
adGenFrGroupDayIntervalNetworkInactive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenFrGroupDayIntervalNetworkInactive.setStatus("current")
_AdGenFrLink_ObjectIdentity = ObjectIdentity
adGenFrLink = _AdGenFrLink_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 29, 1, 2)
)
_AdGenFrLinkTable_Object = MibTable
adGenFrLinkTable = _AdGenFrLinkTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 29, 1, 2, 2)
)
if mibBuilder.loadTexts:
    adGenFrLinkTable.setStatus("current")
_AdGenFrLinkEntry_Object = MibTableRow
adGenFrLinkEntry = _AdGenFrLinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 29, 1, 2, 2, 1)
)
adGenFrLinkEntry.setIndexNames(
    (0, "ADTRAN-GEN-FRAME-RELAY-MIB", "adGenFrLinkGroupIfIndex"),
    (0, "ADTRAN-GEN-FRAME-RELAY-MIB", "adGenFrLinkIfIndex"),
    (0, "ADTRAN-GEN-FRAME-RELAY-MIB", "adGenFrLinkBundleId"),
)
if mibBuilder.loadTexts:
    adGenFrLinkEntry.setStatus("current")
_AdGenFrLinkGroupIfIndex_Type = InterfaceIndex
_AdGenFrLinkGroupIfIndex_Object = MibTableColumn
adGenFrLinkGroupIfIndex = _AdGenFrLinkGroupIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 29, 1, 2, 2, 1, 1),
    _AdGenFrLinkGroupIfIndex_Type()
)
adGenFrLinkGroupIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adGenFrLinkGroupIfIndex.setStatus("current")
_AdGenFrLinkIfIndex_Type = InterfaceIndex
_AdGenFrLinkIfIndex_Object = MibTableColumn
adGenFrLinkIfIndex = _AdGenFrLinkIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 29, 1, 2, 2, 1, 2),
    _AdGenFrLinkIfIndex_Type()
)
adGenFrLinkIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adGenFrLinkIfIndex.setStatus("current")


class _AdGenFrLinkBundleId_Type(Integer32):
    """Custom type adGenFrLinkBundleId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_AdGenFrLinkBundleId_Type.__name__ = "Integer32"
_AdGenFrLinkBundleId_Object = MibTableColumn
adGenFrLinkBundleId = _AdGenFrLinkBundleId_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 29, 1, 2, 2, 1, 3),
    _AdGenFrLinkBundleId_Type()
)
adGenFrLinkBundleId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adGenFrLinkBundleId.setStatus("current")
_AdGenFrLinkRowStatus_Type = RowStatus
_AdGenFrLinkRowStatus_Object = MibTableColumn
adGenFrLinkRowStatus = _AdGenFrLinkRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 29, 1, 2, 2, 1, 4),
    _AdGenFrLinkRowStatus_Type()
)
adGenFrLinkRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenFrLinkRowStatus.setStatus("current")


class _AdGenFrLinkTimeslots_Type(DisplayString):
    """Custom type adGenFrLinkTimeslots based on DisplayString"""
    defaultValue = OctetString("1-24")


_AdGenFrLinkTimeslots_Type.__name__ = "DisplayString"
_AdGenFrLinkTimeslots_Object = MibTableColumn
adGenFrLinkTimeslots = _AdGenFrLinkTimeslots_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 29, 1, 2, 2, 1, 5),
    _AdGenFrLinkTimeslots_Type()
)
adGenFrLinkTimeslots.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenFrLinkTimeslots.setStatus("current")
_AdGenFrLinkStatusString_Type = DisplayString
_AdGenFrLinkStatusString_Object = MibTableColumn
adGenFrLinkStatusString = _AdGenFrLinkStatusString_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 29, 1, 2, 2, 1, 7),
    _AdGenFrLinkStatusString_Type()
)
adGenFrLinkStatusString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenFrLinkStatusString.setStatus("current")
_AdGenFrPVC_ObjectIdentity = ObjectIdentity
adGenFrPVC = _AdGenFrPVC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 29, 1, 3)
)
_AdGenFrPVCTable_Object = MibTable
adGenFrPVCTable = _AdGenFrPVCTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 29, 1, 3, 4)
)
if mibBuilder.loadTexts:
    adGenFrPVCTable.setStatus("current")
_AdGenFrPVCEntry_Object = MibTableRow
adGenFrPVCEntry = _AdGenFrPVCEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 29, 1, 3, 4, 1)
)
adGenFrPVCEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ADTRAN-GEN-FRAME-RELAY-MIB", "adGenFrPVCDLCIIndex"),
)
if mibBuilder.loadTexts:
    adGenFrPVCEntry.setStatus("current")
_AdGenFrPVCIfIndex_Type = InterfaceIndex
_AdGenFrPVCIfIndex_Object = MibTableColumn
adGenFrPVCIfIndex = _AdGenFrPVCIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 29, 1, 3, 4, 1, 1),
    _AdGenFrPVCIfIndex_Type()
)
adGenFrPVCIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenFrPVCIfIndex.setStatus("current")


class _AdGenFrPVCDLCIIndex_Type(Integer32):
    """Custom type adGenFrPVCDLCIIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 991),
    )


_AdGenFrPVCDLCIIndex_Type.__name__ = "Integer32"
_AdGenFrPVCDLCIIndex_Object = MibTableColumn
adGenFrPVCDLCIIndex = _AdGenFrPVCDLCIIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 29, 1, 3, 4, 1, 2),
    _AdGenFrPVCDLCIIndex_Type()
)
adGenFrPVCDLCIIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenFrPVCDLCIIndex.setStatus("current")
_AdGenFrPVCStatusString_Type = DisplayString
_AdGenFrPVCStatusString_Object = MibTableColumn
adGenFrPVCStatusString = _AdGenFrPVCStatusString_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 29, 1, 3, 4, 1, 3),
    _AdGenFrPVCStatusString_Type()
)
adGenFrPVCStatusString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenFrPVCStatusString.setStatus("current")


class _AdGenFrPVCAdminStatus_Type(Integer32):
    """Custom type adGenFrPVCAdminStatus based on Integer32"""
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
        *(("up", 1),
          ("down", 2),
          ("testing", 3))
    )


_AdGenFrPVCAdminStatus_Type.__name__ = "Integer32"
_AdGenFrPVCAdminStatus_Object = MibTableColumn
adGenFrPVCAdminStatus = _AdGenFrPVCAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 29, 1, 3, 4, 1, 4),
    _AdGenFrPVCAdminStatus_Type()
)
adGenFrPVCAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenFrPVCAdminStatus.setStatus("current")


class _AdGenFrPVCState_Type(Integer32):
    """Custom type adGenFrPVCState based on Integer32"""
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
        *(("new", 1),
          ("none", 2),
          ("active", 3),
          ("inactive", 4),
          ("deleted", 5))
    )


_AdGenFrPVCState_Type.__name__ = "Integer32"
_AdGenFrPVCState_Object = MibTableColumn
adGenFrPVCState = _AdGenFrPVCState_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 29, 1, 3, 4, 1, 5),
    _AdGenFrPVCState_Type()
)
adGenFrPVCState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenFrPVCState.setStatus("current")


class _AdGenFrPVCEncapsulation_Type(Integer32):
    """Custom type adGenFrPVCEncapsulation based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("ipv4", 1)
    )


_AdGenFrPVCEncapsulation_Type.__name__ = "Integer32"
_AdGenFrPVCEncapsulation_Object = MibTableColumn
adGenFrPVCEncapsulation = _AdGenFrPVCEncapsulation_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 29, 1, 3, 4, 1, 6),
    _AdGenFrPVCEncapsulation_Type()
)
adGenFrPVCEncapsulation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenFrPVCEncapsulation.setStatus("current")


class _AdGenFrPVCPrimaryPeerIpAddressType_Type(InetAddressType):
    """Custom type adGenFrPVCPrimaryPeerIpAddressType based on InetAddressType"""
    defaultValue = 1


_AdGenFrPVCPrimaryPeerIpAddressType_Type.__name__ = "InetAddressType"
_AdGenFrPVCPrimaryPeerIpAddressType_Object = MibTableColumn
adGenFrPVCPrimaryPeerIpAddressType = _AdGenFrPVCPrimaryPeerIpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 29, 1, 3, 4, 1, 7),
    _AdGenFrPVCPrimaryPeerIpAddressType_Type()
)
adGenFrPVCPrimaryPeerIpAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenFrPVCPrimaryPeerIpAddressType.setStatus("current")
_AdGenFrPVCPrimaryPeerIpAddress_Type = InetAddress
_AdGenFrPVCPrimaryPeerIpAddress_Object = MibTableColumn
adGenFrPVCPrimaryPeerIpAddress = _AdGenFrPVCPrimaryPeerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 29, 1, 3, 4, 1, 8),
    _AdGenFrPVCPrimaryPeerIpAddress_Type()
)
adGenFrPVCPrimaryPeerIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenFrPVCPrimaryPeerIpAddress.setStatus("current")


class _AdGenFrPVCSecondaryPeerAddressType_Type(InetAddressType):
    """Custom type adGenFrPVCSecondaryPeerAddressType based on InetAddressType"""
    defaultValue = 1


_AdGenFrPVCSecondaryPeerAddressType_Type.__name__ = "InetAddressType"
_AdGenFrPVCSecondaryPeerAddressType_Object = MibTableColumn
adGenFrPVCSecondaryPeerAddressType = _AdGenFrPVCSecondaryPeerAddressType_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 29, 1, 3, 4, 1, 9),
    _AdGenFrPVCSecondaryPeerAddressType_Type()
)
adGenFrPVCSecondaryPeerAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenFrPVCSecondaryPeerAddressType.setStatus("current")
_AdGenFrPVCSecondaryPeerIpAddress_Type = InetAddress
_AdGenFrPVCSecondaryPeerIpAddress_Object = MibTableColumn
adGenFrPVCSecondaryPeerIpAddress = _AdGenFrPVCSecondaryPeerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 29, 1, 3, 4, 1, 10),
    _AdGenFrPVCSecondaryPeerIpAddress_Type()
)
adGenFrPVCSecondaryPeerIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenFrPVCSecondaryPeerIpAddress.setStatus("current")


class _AdGenFrPVCPrimaryGatewayAddressType_Type(InetAddressType):
    """Custom type adGenFrPVCPrimaryGatewayAddressType based on InetAddressType"""
    defaultValue = 1


_AdGenFrPVCPrimaryGatewayAddressType_Type.__name__ = "InetAddressType"
_AdGenFrPVCPrimaryGatewayAddressType_Object = MibTableColumn
adGenFrPVCPrimaryGatewayAddressType = _AdGenFrPVCPrimaryGatewayAddressType_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 29, 1, 3, 4, 1, 11),
    _AdGenFrPVCPrimaryGatewayAddressType_Type()
)
adGenFrPVCPrimaryGatewayAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenFrPVCPrimaryGatewayAddressType.setStatus("current")
_AdGenFrPVCPrimaryGatewayAddress_Type = InetAddress
_AdGenFrPVCPrimaryGatewayAddress_Object = MibTableColumn
adGenFrPVCPrimaryGatewayAddress = _AdGenFrPVCPrimaryGatewayAddress_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 29, 1, 3, 4, 1, 12),
    _AdGenFrPVCPrimaryGatewayAddress_Type()
)
adGenFrPVCPrimaryGatewayAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenFrPVCPrimaryGatewayAddress.setStatus("current")


class _AdGenFrPVCInverseArpEnable_Type(TruthValue):
    """Custom type adGenFrPVCInverseArpEnable based on TruthValue"""
    defaultValue = 1


_AdGenFrPVCInverseArpEnable_Type.__name__ = "TruthValue"
_AdGenFrPVCInverseArpEnable_Object = MibTableColumn
adGenFrPVCInverseArpEnable = _AdGenFrPVCInverseArpEnable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 29, 1, 3, 4, 1, 19),
    _AdGenFrPVCInverseArpEnable_Type()
)
adGenFrPVCInverseArpEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenFrPVCInverseArpEnable.setStatus("current")
_AdGenFrPVCLearnedPrimaryPeerIpAddressType_Type = InetAddressType
_AdGenFrPVCLearnedPrimaryPeerIpAddressType_Object = MibTableColumn
adGenFrPVCLearnedPrimaryPeerIpAddressType = _AdGenFrPVCLearnedPrimaryPeerIpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 29, 1, 3, 4, 1, 20),
    _AdGenFrPVCLearnedPrimaryPeerIpAddressType_Type()
)
adGenFrPVCLearnedPrimaryPeerIpAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenFrPVCLearnedPrimaryPeerIpAddressType.setStatus("current")
_AdGenFrPVCLearnedPrimaryPeerIpAddress_Type = InetAddress
_AdGenFrPVCLearnedPrimaryPeerIpAddress_Object = MibTableColumn
adGenFrPVCLearnedPrimaryPeerIpAddress = _AdGenFrPVCLearnedPrimaryPeerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 29, 1, 3, 4, 1, 21),
    _AdGenFrPVCLearnedPrimaryPeerIpAddress_Type()
)
adGenFrPVCLearnedPrimaryPeerIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenFrPVCLearnedPrimaryPeerIpAddress.setStatus("current")
_AdGenFrPVCLearnedSecondaryPeerAddressType_Type = InetAddressType
_AdGenFrPVCLearnedSecondaryPeerAddressType_Object = MibTableColumn
adGenFrPVCLearnedSecondaryPeerAddressType = _AdGenFrPVCLearnedSecondaryPeerAddressType_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 29, 1, 3, 4, 1, 22),
    _AdGenFrPVCLearnedSecondaryPeerAddressType_Type()
)
adGenFrPVCLearnedSecondaryPeerAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenFrPVCLearnedSecondaryPeerAddressType.setStatus("current")
_AdGenFrPVCLearnedSecondaryPeerIpAddress_Type = InetAddress
_AdGenFrPVCLearnedSecondaryPeerIpAddress_Object = MibTableColumn
adGenFrPVCLearnedSecondaryPeerIpAddress = _AdGenFrPVCLearnedSecondaryPeerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 29, 1, 3, 4, 1, 23),
    _AdGenFrPVCLearnedSecondaryPeerIpAddress_Type()
)
adGenFrPVCLearnedSecondaryPeerIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenFrPVCLearnedSecondaryPeerIpAddress.setStatus("current")


class _AdGenFrPVCClearCounters_Type(Integer32):
    """Custom type adGenFrPVCClearCounters based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset", 1)
    )


_AdGenFrPVCClearCounters_Type.__name__ = "Integer32"
_AdGenFrPVCClearCounters_Object = MibTableColumn
adGenFrPVCClearCounters = _AdGenFrPVCClearCounters_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 29, 1, 3, 4, 1, 24),
    _AdGenFrPVCClearCounters_Type()
)
adGenFrPVCClearCounters.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenFrPVCClearCounters.setStatus("current")


class _AdGenFrPVCClearPmHistory_Type(Integer32):
    """Custom type adGenFrPVCClearPmHistory based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset", 1)
    )


_AdGenFrPVCClearPmHistory_Type.__name__ = "Integer32"
_AdGenFrPVCClearPmHistory_Object = MibTableColumn
adGenFrPVCClearPmHistory = _AdGenFrPVCClearPmHistory_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 29, 1, 3, 4, 1, 25),
    _AdGenFrPVCClearPmHistory_Type()
)
adGenFrPVCClearPmHistory.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenFrPVCClearPmHistory.setStatus("current")


class _AdGenFrPVCOperStatus_Type(Integer32):
    """Custom type adGenFrPVCOperStatus based on Integer32"""
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
        *(("up", 1),
          ("down", 2),
          ("testing", 3),
          ("unknown", 4),
          ("dormant", 5),
          ("notPresent", 6),
          ("lowerLayerDown", 7))
    )


_AdGenFrPVCOperStatus_Type.__name__ = "Integer32"
_AdGenFrPVCOperStatus_Object = MibTableColumn
adGenFrPVCOperStatus = _AdGenFrPVCOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 29, 1, 3, 4, 1, 26),
    _AdGenFrPVCOperStatus_Type()
)
adGenFrPVCOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenFrPVCOperStatus.setStatus("current")
_AdGenFrPVCLastChange_Type = TimeTicks
_AdGenFrPVCLastChange_Object = MibTableColumn
adGenFrPVCLastChange = _AdGenFrPVCLastChange_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 29, 1, 3, 4, 1, 27),
    _AdGenFrPVCLastChange_Type()
)
adGenFrPVCLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenFrPVCLastChange.setStatus("current")
_AdGenFrPVCDescription_Type = DisplayString
_AdGenFrPVCDescription_Object = MibTableColumn
adGenFrPVCDescription = _AdGenFrPVCDescription_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 29, 1, 3, 4, 1, 28),
    _AdGenFrPVCDescription_Type()
)
adGenFrPVCDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenFrPVCDescription.setStatus("current")


class _AdGenFrPVCMtu_Type(Integer32):
    """Custom type adGenFrPVCMtu based on Integer32"""
    defaultValue = 1500

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(262, 1600),
    )


_AdGenFrPVCMtu_Type.__name__ = "Integer32"
_AdGenFrPVCMtu_Object = MibTableColumn
adGenFrPVCMtu = _AdGenFrPVCMtu_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 29, 1, 3, 4, 1, 29),
    _AdGenFrPVCMtu_Type()
)
adGenFrPVCMtu.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenFrPVCMtu.setStatus("current")
if mibBuilder.loadTexts:
    adGenFrPVCMtu.setUnits("Octets")
_AdGenFrPVCCurrentTable_Object = MibTable
adGenFrPVCCurrentTable = _AdGenFrPVCCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 29, 1, 3, 5)
)
if mibBuilder.loadTexts:
    adGenFrPVCCurrentTable.setStatus("current")
_AdGenFrPVCCurrentEntry_Object = MibTableRow
adGenFrPVCCurrentEntry = _AdGenFrPVCCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 29, 1, 3, 5, 1)
)
adGenFrPVCCurrentEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ADTRAN-GEN-FRAME-RELAY-MIB", "adGenFrPVCDLCIIndex"),
)
if mibBuilder.loadTexts:
    adGenFrPVCCurrentEntry.setStatus("current")
_AdGenFrPVCCurrentInOctets_Type = Counter32
_AdGenFrPVCCurrentInOctets_Object = MibTableColumn
adGenFrPVCCurrentInOctets = _AdGenFrPVCCurrentInOctets_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 29, 1, 3, 5, 1, 1),
    _AdGenFrPVCCurrentInOctets_Type()
)
adGenFrPVCCurrentInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenFrPVCCurrentInOctets.setStatus("current")
_AdGenFrPVCCurrentInPkts_Type = Counter32
_AdGenFrPVCCurrentInPkts_Object = MibTableColumn
adGenFrPVCCurrentInPkts = _AdGenFrPVCCurrentInPkts_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 29, 1, 3, 5, 1, 2),
    _AdGenFrPVCCurrentInPkts_Type()
)
adGenFrPVCCurrentInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenFrPVCCurrentInPkts.setStatus("current")
_AdGenFrPVCCurrentInDiscards_Type = Counter32
_AdGenFrPVCCurrentInDiscards_Object = MibTableColumn
adGenFrPVCCurrentInDiscards = _AdGenFrPVCCurrentInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 29, 1, 3, 5, 1, 3),
    _AdGenFrPVCCurrentInDiscards_Type()
)
adGenFrPVCCurrentInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenFrPVCCurrentInDiscards.setStatus("current")
_AdGenFrPVCCurrentOutOctets_Type = Counter32
_AdGenFrPVCCurrentOutOctets_Object = MibTableColumn
adGenFrPVCCurrentOutOctets = _AdGenFrPVCCurrentOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 29, 1, 3, 5, 1, 5),
    _AdGenFrPVCCurrentOutOctets_Type()
)
adGenFrPVCCurrentOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenFrPVCCurrentOutOctets.setStatus("current")
_AdGenFrPVCCurrentOutPkts_Type = Counter32
_AdGenFrPVCCurrentOutPkts_Object = MibTableColumn
adGenFrPVCCurrentOutPkts = _AdGenFrPVCCurrentOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 29, 1, 3, 5, 1, 6),
    _AdGenFrPVCCurrentOutPkts_Type()
)
adGenFrPVCCurrentOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenFrPVCCurrentOutPkts.setStatus("current")
_AdGenFrPVCCurrentOutDiscards_Type = Counter32
_AdGenFrPVCCurrentOutDiscards_Object = MibTableColumn
adGenFrPVCCurrentOutDiscards = _AdGenFrPVCCurrentOutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 29, 1, 3, 5, 1, 7),
    _AdGenFrPVCCurrentOutDiscards_Type()
)
adGenFrPVCCurrentOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenFrPVCCurrentOutDiscards.setStatus("current")
_AdGenFrPVCCurrentPktsFECN1In_Type = Counter32
_AdGenFrPVCCurrentPktsFECN1In_Object = MibTableColumn
adGenFrPVCCurrentPktsFECN1In = _AdGenFrPVCCurrentPktsFECN1In_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 29, 1, 3, 5, 1, 9),
    _AdGenFrPVCCurrentPktsFECN1In_Type()
)
adGenFrPVCCurrentPktsFECN1In.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenFrPVCCurrentPktsFECN1In.setStatus("current")
_AdGenFrPVCCurrentPktsFECN1Out_Type = Counter32
_AdGenFrPVCCurrentPktsFECN1Out_Object = MibTableColumn
adGenFrPVCCurrentPktsFECN1Out = _AdGenFrPVCCurrentPktsFECN1Out_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 29, 1, 3, 5, 1, 10),
    _AdGenFrPVCCurrentPktsFECN1Out_Type()
)
adGenFrPVCCurrentPktsFECN1Out.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenFrPVCCurrentPktsFECN1Out.setStatus("current")
_AdGenFrPVCCurrentPktsBECN1In_Type = Counter32
_AdGenFrPVCCurrentPktsBECN1In_Object = MibTableColumn
adGenFrPVCCurrentPktsBECN1In = _AdGenFrPVCCurrentPktsBECN1In_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 29, 1, 3, 5, 1, 11),
    _AdGenFrPVCCurrentPktsBECN1In_Type()
)
adGenFrPVCCurrentPktsBECN1In.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenFrPVCCurrentPktsBECN1In.setStatus("current")
_AdGenFrPVCCurrentPktsBECN1Out_Type = Counter32
_AdGenFrPVCCurrentPktsBECN1Out_Object = MibTableColumn
adGenFrPVCCurrentPktsBECN1Out = _AdGenFrPVCCurrentPktsBECN1Out_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 29, 1, 3, 5, 1, 12),
    _AdGenFrPVCCurrentPktsBECN1Out_Type()
)
adGenFrPVCCurrentPktsBECN1Out.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenFrPVCCurrentPktsBECN1Out.setStatus("current")
_AdGenFrPVCCurrentPktsDE1In_Type = Counter32
_AdGenFrPVCCurrentPktsDE1In_Object = MibTableColumn
adGenFrPVCCurrentPktsDE1In = _AdGenFrPVCCurrentPktsDE1In_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 29, 1, 3, 5, 1, 13),
    _AdGenFrPVCCurrentPktsDE1In_Type()
)
adGenFrPVCCurrentPktsDE1In.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenFrPVCCurrentPktsDE1In.setStatus("current")
_AdGenFrPVCCurrentPktsDE1Out_Type = Counter32
_AdGenFrPVCCurrentPktsDE1Out_Object = MibTableColumn
adGenFrPVCCurrentPktsDE1Out = _AdGenFrPVCCurrentPktsDE1Out_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 29, 1, 3, 5, 1, 14),
    _AdGenFrPVCCurrentPktsDE1Out_Type()
)
adGenFrPVCCurrentPktsDE1Out.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenFrPVCCurrentPktsDE1Out.setStatus("current")
_AdGenFrPVCCurrentOctetsDE1In_Type = Counter32
_AdGenFrPVCCurrentOctetsDE1In_Object = MibTableColumn
adGenFrPVCCurrentOctetsDE1In = _AdGenFrPVCCurrentOctetsDE1In_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 29, 1, 3, 5, 1, 15),
    _AdGenFrPVCCurrentOctetsDE1In_Type()
)
adGenFrPVCCurrentOctetsDE1In.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenFrPVCCurrentOctetsDE1In.setStatus("current")
_AdGenFrPVCCurrentOctetsDE1Out_Type = Counter32
_AdGenFrPVCCurrentOctetsDE1Out_Object = MibTableColumn
adGenFrPVCCurrentOctetsDE1Out = _AdGenFrPVCCurrentOctetsDE1Out_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 29, 1, 3, 5, 1, 16),
    _AdGenFrPVCCurrentOctetsDE1Out_Type()
)
adGenFrPVCCurrentOctetsDE1Out.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenFrPVCCurrentOctetsDE1Out.setStatus("current")
_AdGenFrPVCIntervalTable_Object = MibTable
adGenFrPVCIntervalTable = _AdGenFrPVCIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 29, 1, 3, 6)
)
if mibBuilder.loadTexts:
    adGenFrPVCIntervalTable.setStatus("current")
_AdGenFrPVCIntervalEntry_Object = MibTableRow
adGenFrPVCIntervalEntry = _AdGenFrPVCIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 29, 1, 3, 6, 1)
)
adGenFrPVCIntervalEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ADTRAN-GEN-FRAME-RELAY-MIB", "adGenFrPVCDLCIIndex"),
    (0, "ADTRAN-GEN-FRAME-RELAY-MIB", "adGenFrPVCIntervalNumber"),
)
if mibBuilder.loadTexts:
    adGenFrPVCIntervalEntry.setStatus("current")


class _AdGenFrPVCIntervalNumber_Type(Integer32):
    """Custom type adGenFrPVCIntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_AdGenFrPVCIntervalNumber_Type.__name__ = "Integer32"
_AdGenFrPVCIntervalNumber_Object = MibTableColumn
adGenFrPVCIntervalNumber = _AdGenFrPVCIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 29, 1, 3, 6, 1, 1),
    _AdGenFrPVCIntervalNumber_Type()
)
adGenFrPVCIntervalNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adGenFrPVCIntervalNumber.setStatus("current")
_AdGenFrPVCIntervalTimeStamp_Type = DisplayString
_AdGenFrPVCIntervalTimeStamp_Object = MibTableColumn
adGenFrPVCIntervalTimeStamp = _AdGenFrPVCIntervalTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 29, 1, 3, 6, 1, 2),
    _AdGenFrPVCIntervalTimeStamp_Type()
)
adGenFrPVCIntervalTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenFrPVCIntervalTimeStamp.setStatus("current")
_AdGenFrPVCIntervalInOctets_Type = Counter32
_AdGenFrPVCIntervalInOctets_Object = MibTableColumn
adGenFrPVCIntervalInOctets = _AdGenFrPVCIntervalInOctets_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 29, 1, 3, 6, 1, 3),
    _AdGenFrPVCIntervalInOctets_Type()
)
adGenFrPVCIntervalInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenFrPVCIntervalInOctets.setStatus("current")
_AdGenFrPVCIntervalInPkts_Type = Counter32
_AdGenFrPVCIntervalInPkts_Object = MibTableColumn
adGenFrPVCIntervalInPkts = _AdGenFrPVCIntervalInPkts_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 29, 1, 3, 6, 1, 4),
    _AdGenFrPVCIntervalInPkts_Type()
)
adGenFrPVCIntervalInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenFrPVCIntervalInPkts.setStatus("current")
_AdGenFrPVCIntervalInDiscards_Type = Counter32
_AdGenFrPVCIntervalInDiscards_Object = MibTableColumn
adGenFrPVCIntervalInDiscards = _AdGenFrPVCIntervalInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 29, 1, 3, 6, 1, 5),
    _AdGenFrPVCIntervalInDiscards_Type()
)
adGenFrPVCIntervalInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenFrPVCIntervalInDiscards.setStatus("current")
_AdGenFrPVCIntervalOutOctets_Type = Counter32
_AdGenFrPVCIntervalOutOctets_Object = MibTableColumn
adGenFrPVCIntervalOutOctets = _AdGenFrPVCIntervalOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 29, 1, 3, 6, 1, 7),
    _AdGenFrPVCIntervalOutOctets_Type()
)
adGenFrPVCIntervalOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenFrPVCIntervalOutOctets.setStatus("current")
_AdGenFrPVCIntervalOutPkts_Type = Counter32
_AdGenFrPVCIntervalOutPkts_Object = MibTableColumn
adGenFrPVCIntervalOutPkts = _AdGenFrPVCIntervalOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 29, 1, 3, 6, 1, 8),
    _AdGenFrPVCIntervalOutPkts_Type()
)
adGenFrPVCIntervalOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenFrPVCIntervalOutPkts.setStatus("current")
_AdGenFrPVCIntervalOutDiscards_Type = Counter32
_AdGenFrPVCIntervalOutDiscards_Object = MibTableColumn
adGenFrPVCIntervalOutDiscards = _AdGenFrPVCIntervalOutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 29, 1, 3, 6, 1, 9),
    _AdGenFrPVCIntervalOutDiscards_Type()
)
adGenFrPVCIntervalOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenFrPVCIntervalOutDiscards.setStatus("current")
_AdGenFrPVCIntervalPktsFECN1In_Type = Counter32
_AdGenFrPVCIntervalPktsFECN1In_Object = MibTableColumn
adGenFrPVCIntervalPktsFECN1In = _AdGenFrPVCIntervalPktsFECN1In_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 29, 1, 3, 6, 1, 11),
    _AdGenFrPVCIntervalPktsFECN1In_Type()
)
adGenFrPVCIntervalPktsFECN1In.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenFrPVCIntervalPktsFECN1In.setStatus("current")
_AdGenFrPVCIntervalPktsFECN1Out_Type = Counter32
_AdGenFrPVCIntervalPktsFECN1Out_Object = MibTableColumn
adGenFrPVCIntervalPktsFECN1Out = _AdGenFrPVCIntervalPktsFECN1Out_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 29, 1, 3, 6, 1, 12),
    _AdGenFrPVCIntervalPktsFECN1Out_Type()
)
adGenFrPVCIntervalPktsFECN1Out.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenFrPVCIntervalPktsFECN1Out.setStatus("current")
_AdGenFrPVCIntervalPktsBECN1In_Type = Counter32
_AdGenFrPVCIntervalPktsBECN1In_Object = MibTableColumn
adGenFrPVCIntervalPktsBECN1In = _AdGenFrPVCIntervalPktsBECN1In_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 29, 1, 3, 6, 1, 13),
    _AdGenFrPVCIntervalPktsBECN1In_Type()
)
adGenFrPVCIntervalPktsBECN1In.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenFrPVCIntervalPktsBECN1In.setStatus("current")
_AdGenFrPVCIntervalPktsBECN1Out_Type = Counter32
_AdGenFrPVCIntervalPktsBECN1Out_Object = MibTableColumn
adGenFrPVCIntervalPktsBECN1Out = _AdGenFrPVCIntervalPktsBECN1Out_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 29, 1, 3, 6, 1, 14),
    _AdGenFrPVCIntervalPktsBECN1Out_Type()
)
adGenFrPVCIntervalPktsBECN1Out.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenFrPVCIntervalPktsBECN1Out.setStatus("current")
_AdGenFrPVCIntervalPktsDE1In_Type = Counter32
_AdGenFrPVCIntervalPktsDE1In_Object = MibTableColumn
adGenFrPVCIntervalPktsDE1In = _AdGenFrPVCIntervalPktsDE1In_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 29, 1, 3, 6, 1, 15),
    _AdGenFrPVCIntervalPktsDE1In_Type()
)
adGenFrPVCIntervalPktsDE1In.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenFrPVCIntervalPktsDE1In.setStatus("current")
_AdGenFrPVCIntervalPktsDE1Out_Type = Counter32
_AdGenFrPVCIntervalPktsDE1Out_Object = MibTableColumn
adGenFrPVCIntervalPktsDE1Out = _AdGenFrPVCIntervalPktsDE1Out_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 29, 1, 3, 6, 1, 16),
    _AdGenFrPVCIntervalPktsDE1Out_Type()
)
adGenFrPVCIntervalPktsDE1Out.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenFrPVCIntervalPktsDE1Out.setStatus("current")
_AdGenFrPVCIntervalOctetsDE1In_Type = Counter32
_AdGenFrPVCIntervalOctetsDE1In_Object = MibTableColumn
adGenFrPVCIntervalOctetsDE1In = _AdGenFrPVCIntervalOctetsDE1In_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 29, 1, 3, 6, 1, 17),
    _AdGenFrPVCIntervalOctetsDE1In_Type()
)
adGenFrPVCIntervalOctetsDE1In.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenFrPVCIntervalOctetsDE1In.setStatus("current")
_AdGenFrPVCIntervalOctetsDE1Out_Type = Counter32
_AdGenFrPVCIntervalOctetsDE1Out_Object = MibTableColumn
adGenFrPVCIntervalOctetsDE1Out = _AdGenFrPVCIntervalOctetsDE1Out_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 29, 1, 3, 6, 1, 18),
    _AdGenFrPVCIntervalOctetsDE1Out_Type()
)
adGenFrPVCIntervalOctetsDE1Out.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenFrPVCIntervalOctetsDE1Out.setStatus("current")
_AdGenFrPVCDayCurrentTable_Object = MibTable
adGenFrPVCDayCurrentTable = _AdGenFrPVCDayCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 29, 1, 3, 7)
)
if mibBuilder.loadTexts:
    adGenFrPVCDayCurrentTable.setStatus("current")
_AdGenFrPVCDayCurrentEntry_Object = MibTableRow
adGenFrPVCDayCurrentEntry = _AdGenFrPVCDayCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 29, 1, 3, 7, 1)
)
adGenFrPVCDayCurrentEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ADTRAN-GEN-FRAME-RELAY-MIB", "adGenFrPVCDLCIIndex"),
)
if mibBuilder.loadTexts:
    adGenFrPVCDayCurrentEntry.setStatus("current")
_AdGenFrPVCDayCurrentInOctets_Type = Counter32
_AdGenFrPVCDayCurrentInOctets_Object = MibTableColumn
adGenFrPVCDayCurrentInOctets = _AdGenFrPVCDayCurrentInOctets_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 29, 1, 3, 7, 1, 1),
    _AdGenFrPVCDayCurrentInOctets_Type()
)
adGenFrPVCDayCurrentInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenFrPVCDayCurrentInOctets.setStatus("current")
_AdGenFrPVCDayCurrentInPkts_Type = Counter32
_AdGenFrPVCDayCurrentInPkts_Object = MibTableColumn
adGenFrPVCDayCurrentInPkts = _AdGenFrPVCDayCurrentInPkts_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 29, 1, 3, 7, 1, 2),
    _AdGenFrPVCDayCurrentInPkts_Type()
)
adGenFrPVCDayCurrentInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenFrPVCDayCurrentInPkts.setStatus("current")
_AdGenFrPVCDayCurrentInDiscards_Type = Counter32
_AdGenFrPVCDayCurrentInDiscards_Object = MibTableColumn
adGenFrPVCDayCurrentInDiscards = _AdGenFrPVCDayCurrentInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 29, 1, 3, 7, 1, 3),
    _AdGenFrPVCDayCurrentInDiscards_Type()
)
adGenFrPVCDayCurrentInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenFrPVCDayCurrentInDiscards.setStatus("current")
_AdGenFrPVCDayCurrentOutOctets_Type = Counter32
_AdGenFrPVCDayCurrentOutOctets_Object = MibTableColumn
adGenFrPVCDayCurrentOutOctets = _AdGenFrPVCDayCurrentOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 29, 1, 3, 7, 1, 5),
    _AdGenFrPVCDayCurrentOutOctets_Type()
)
adGenFrPVCDayCurrentOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenFrPVCDayCurrentOutOctets.setStatus("current")
_AdGenFrPVCDayCurrentOutPkts_Type = Counter32
_AdGenFrPVCDayCurrentOutPkts_Object = MibTableColumn
adGenFrPVCDayCurrentOutPkts = _AdGenFrPVCDayCurrentOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 29, 1, 3, 7, 1, 6),
    _AdGenFrPVCDayCurrentOutPkts_Type()
)
adGenFrPVCDayCurrentOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenFrPVCDayCurrentOutPkts.setStatus("current")
_AdGenFrPVCDayCurrentOutDiscards_Type = Counter32
_AdGenFrPVCDayCurrentOutDiscards_Object = MibTableColumn
adGenFrPVCDayCurrentOutDiscards = _AdGenFrPVCDayCurrentOutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 29, 1, 3, 7, 1, 7),
    _AdGenFrPVCDayCurrentOutDiscards_Type()
)
adGenFrPVCDayCurrentOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenFrPVCDayCurrentOutDiscards.setStatus("current")
_AdGenFrPVCDayCurrentPktsFECN1In_Type = Counter32
_AdGenFrPVCDayCurrentPktsFECN1In_Object = MibTableColumn
adGenFrPVCDayCurrentPktsFECN1In = _AdGenFrPVCDayCurrentPktsFECN1In_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 29, 1, 3, 7, 1, 9),
    _AdGenFrPVCDayCurrentPktsFECN1In_Type()
)
adGenFrPVCDayCurrentPktsFECN1In.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenFrPVCDayCurrentPktsFECN1In.setStatus("current")
_AdGenFrPVCDayCurrentPktsFECN1Out_Type = Counter32
_AdGenFrPVCDayCurrentPktsFECN1Out_Object = MibTableColumn
adGenFrPVCDayCurrentPktsFECN1Out = _AdGenFrPVCDayCurrentPktsFECN1Out_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 29, 1, 3, 7, 1, 10),
    _AdGenFrPVCDayCurrentPktsFECN1Out_Type()
)
adGenFrPVCDayCurrentPktsFECN1Out.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenFrPVCDayCurrentPktsFECN1Out.setStatus("current")
_AdGenFrPVCDayCurrentPktsBECN1In_Type = Counter32
_AdGenFrPVCDayCurrentPktsBECN1In_Object = MibTableColumn
adGenFrPVCDayCurrentPktsBECN1In = _AdGenFrPVCDayCurrentPktsBECN1In_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 29, 1, 3, 7, 1, 11),
    _AdGenFrPVCDayCurrentPktsBECN1In_Type()
)
adGenFrPVCDayCurrentPktsBECN1In.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenFrPVCDayCurrentPktsBECN1In.setStatus("current")
_AdGenFrPVCDayCurrentPktsBECN1Out_Type = Counter32
_AdGenFrPVCDayCurrentPktsBECN1Out_Object = MibTableColumn
adGenFrPVCDayCurrentPktsBECN1Out = _AdGenFrPVCDayCurrentPktsBECN1Out_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 29, 1, 3, 7, 1, 12),
    _AdGenFrPVCDayCurrentPktsBECN1Out_Type()
)
adGenFrPVCDayCurrentPktsBECN1Out.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenFrPVCDayCurrentPktsBECN1Out.setStatus("current")
_AdGenFrPVCDayCurrentPktsDE1In_Type = Counter32
_AdGenFrPVCDayCurrentPktsDE1In_Object = MibTableColumn
adGenFrPVCDayCurrentPktsDE1In = _AdGenFrPVCDayCurrentPktsDE1In_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 29, 1, 3, 7, 1, 13),
    _AdGenFrPVCDayCurrentPktsDE1In_Type()
)
adGenFrPVCDayCurrentPktsDE1In.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenFrPVCDayCurrentPktsDE1In.setStatus("current")
_AdGenFrPVCDayCurrentPktsDE1Out_Type = Counter32
_AdGenFrPVCDayCurrentPktsDE1Out_Object = MibTableColumn
adGenFrPVCDayCurrentPktsDE1Out = _AdGenFrPVCDayCurrentPktsDE1Out_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 29, 1, 3, 7, 1, 14),
    _AdGenFrPVCDayCurrentPktsDE1Out_Type()
)
adGenFrPVCDayCurrentPktsDE1Out.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenFrPVCDayCurrentPktsDE1Out.setStatus("current")
_AdGenFrPVCDayCurrentOctetsDE1In_Type = Counter32
_AdGenFrPVCDayCurrentOctetsDE1In_Object = MibTableColumn
adGenFrPVCDayCurrentOctetsDE1In = _AdGenFrPVCDayCurrentOctetsDE1In_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 29, 1, 3, 7, 1, 15),
    _AdGenFrPVCDayCurrentOctetsDE1In_Type()
)
adGenFrPVCDayCurrentOctetsDE1In.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenFrPVCDayCurrentOctetsDE1In.setStatus("current")
_AdGenFrPVCDayCurrentOctetsDE1Out_Type = Counter32
_AdGenFrPVCDayCurrentOctetsDE1Out_Object = MibTableColumn
adGenFrPVCDayCurrentOctetsDE1Out = _AdGenFrPVCDayCurrentOctetsDE1Out_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 29, 1, 3, 7, 1, 16),
    _AdGenFrPVCDayCurrentOctetsDE1Out_Type()
)
adGenFrPVCDayCurrentOctetsDE1Out.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenFrPVCDayCurrentOctetsDE1Out.setStatus("current")
_AdGenFrPVCDayIntervalTable_Object = MibTable
adGenFrPVCDayIntervalTable = _AdGenFrPVCDayIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 29, 1, 3, 8)
)
if mibBuilder.loadTexts:
    adGenFrPVCDayIntervalTable.setStatus("current")
_AdGenFrPVCDayIntervalEntry_Object = MibTableRow
adGenFrPVCDayIntervalEntry = _AdGenFrPVCDayIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 29, 1, 3, 8, 1)
)
adGenFrPVCDayIntervalEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ADTRAN-GEN-FRAME-RELAY-MIB", "adGenFrPVCDLCIIndex"),
    (0, "ADTRAN-GEN-FRAME-RELAY-MIB", "adGenFrPVCDayIntervalNumber"),
)
if mibBuilder.loadTexts:
    adGenFrPVCDayIntervalEntry.setStatus("current")


class _AdGenFrPVCDayIntervalNumber_Type(Integer32):
    """Custom type adGenFrPVCDayIntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_AdGenFrPVCDayIntervalNumber_Type.__name__ = "Integer32"
_AdGenFrPVCDayIntervalNumber_Object = MibTableColumn
adGenFrPVCDayIntervalNumber = _AdGenFrPVCDayIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 29, 1, 3, 8, 1, 1),
    _AdGenFrPVCDayIntervalNumber_Type()
)
adGenFrPVCDayIntervalNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adGenFrPVCDayIntervalNumber.setStatus("current")
_AdGenFrPVCDayIntervalTimeStamp_Type = DisplayString
_AdGenFrPVCDayIntervalTimeStamp_Object = MibTableColumn
adGenFrPVCDayIntervalTimeStamp = _AdGenFrPVCDayIntervalTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 29, 1, 3, 8, 1, 2),
    _AdGenFrPVCDayIntervalTimeStamp_Type()
)
adGenFrPVCDayIntervalTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenFrPVCDayIntervalTimeStamp.setStatus("current")
_AdGenFrPVCDayIntervalInOctets_Type = Counter32
_AdGenFrPVCDayIntervalInOctets_Object = MibTableColumn
adGenFrPVCDayIntervalInOctets = _AdGenFrPVCDayIntervalInOctets_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 29, 1, 3, 8, 1, 3),
    _AdGenFrPVCDayIntervalInOctets_Type()
)
adGenFrPVCDayIntervalInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenFrPVCDayIntervalInOctets.setStatus("current")
_AdGenFrPVCDayIntervalInPkts_Type = Counter32
_AdGenFrPVCDayIntervalInPkts_Object = MibTableColumn
adGenFrPVCDayIntervalInPkts = _AdGenFrPVCDayIntervalInPkts_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 29, 1, 3, 8, 1, 4),
    _AdGenFrPVCDayIntervalInPkts_Type()
)
adGenFrPVCDayIntervalInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenFrPVCDayIntervalInPkts.setStatus("current")
_AdGenFrPVCDayIntervalInDiscards_Type = Counter32
_AdGenFrPVCDayIntervalInDiscards_Object = MibTableColumn
adGenFrPVCDayIntervalInDiscards = _AdGenFrPVCDayIntervalInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 29, 1, 3, 8, 1, 5),
    _AdGenFrPVCDayIntervalInDiscards_Type()
)
adGenFrPVCDayIntervalInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenFrPVCDayIntervalInDiscards.setStatus("current")
_AdGenFrPVCDayIntervalOutOctets_Type = Counter32
_AdGenFrPVCDayIntervalOutOctets_Object = MibTableColumn
adGenFrPVCDayIntervalOutOctets = _AdGenFrPVCDayIntervalOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 29, 1, 3, 8, 1, 7),
    _AdGenFrPVCDayIntervalOutOctets_Type()
)
adGenFrPVCDayIntervalOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenFrPVCDayIntervalOutOctets.setStatus("current")
_AdGenFrPVCDayIntervalOutPkts_Type = Counter32
_AdGenFrPVCDayIntervalOutPkts_Object = MibTableColumn
adGenFrPVCDayIntervalOutPkts = _AdGenFrPVCDayIntervalOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 29, 1, 3, 8, 1, 8),
    _AdGenFrPVCDayIntervalOutPkts_Type()
)
adGenFrPVCDayIntervalOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenFrPVCDayIntervalOutPkts.setStatus("current")
_AdGenFrPVCDayIntervalOutDiscards_Type = Counter32
_AdGenFrPVCDayIntervalOutDiscards_Object = MibTableColumn
adGenFrPVCDayIntervalOutDiscards = _AdGenFrPVCDayIntervalOutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 29, 1, 3, 8, 1, 9),
    _AdGenFrPVCDayIntervalOutDiscards_Type()
)
adGenFrPVCDayIntervalOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenFrPVCDayIntervalOutDiscards.setStatus("current")
_AdGenFrPVCDayIntervalPktsFECN1In_Type = Counter32
_AdGenFrPVCDayIntervalPktsFECN1In_Object = MibTableColumn
adGenFrPVCDayIntervalPktsFECN1In = _AdGenFrPVCDayIntervalPktsFECN1In_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 29, 1, 3, 8, 1, 11),
    _AdGenFrPVCDayIntervalPktsFECN1In_Type()
)
adGenFrPVCDayIntervalPktsFECN1In.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenFrPVCDayIntervalPktsFECN1In.setStatus("current")
_AdGenFrPVCDayIntervalPktsFECN1Out_Type = Counter32
_AdGenFrPVCDayIntervalPktsFECN1Out_Object = MibTableColumn
adGenFrPVCDayIntervalPktsFECN1Out = _AdGenFrPVCDayIntervalPktsFECN1Out_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 29, 1, 3, 8, 1, 12),
    _AdGenFrPVCDayIntervalPktsFECN1Out_Type()
)
adGenFrPVCDayIntervalPktsFECN1Out.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenFrPVCDayIntervalPktsFECN1Out.setStatus("current")
_AdGenFrPVCDayIntervalPktsBECN1In_Type = Counter32
_AdGenFrPVCDayIntervalPktsBECN1In_Object = MibTableColumn
adGenFrPVCDayIntervalPktsBECN1In = _AdGenFrPVCDayIntervalPktsBECN1In_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 29, 1, 3, 8, 1, 13),
    _AdGenFrPVCDayIntervalPktsBECN1In_Type()
)
adGenFrPVCDayIntervalPktsBECN1In.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenFrPVCDayIntervalPktsBECN1In.setStatus("current")
_AdGenFrPVCDayIntervalPktsBECN1Out_Type = Counter32
_AdGenFrPVCDayIntervalPktsBECN1Out_Object = MibTableColumn
adGenFrPVCDayIntervalPktsBECN1Out = _AdGenFrPVCDayIntervalPktsBECN1Out_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 29, 1, 3, 8, 1, 14),
    _AdGenFrPVCDayIntervalPktsBECN1Out_Type()
)
adGenFrPVCDayIntervalPktsBECN1Out.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenFrPVCDayIntervalPktsBECN1Out.setStatus("current")
_AdGenFrPVCDayIntervalPktsDE1In_Type = Counter32
_AdGenFrPVCDayIntervalPktsDE1In_Object = MibTableColumn
adGenFrPVCDayIntervalPktsDE1In = _AdGenFrPVCDayIntervalPktsDE1In_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 29, 1, 3, 8, 1, 15),
    _AdGenFrPVCDayIntervalPktsDE1In_Type()
)
adGenFrPVCDayIntervalPktsDE1In.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenFrPVCDayIntervalPktsDE1In.setStatus("current")
_AdGenFrPVCDayIntervalPktsDE1Out_Type = Counter32
_AdGenFrPVCDayIntervalPktsDE1Out_Object = MibTableColumn
adGenFrPVCDayIntervalPktsDE1Out = _AdGenFrPVCDayIntervalPktsDE1Out_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 29, 1, 3, 8, 1, 16),
    _AdGenFrPVCDayIntervalPktsDE1Out_Type()
)
adGenFrPVCDayIntervalPktsDE1Out.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenFrPVCDayIntervalPktsDE1Out.setStatus("current")
_AdGenFrPVCDayIntervalOctetsDE1In_Type = Counter32
_AdGenFrPVCDayIntervalOctetsDE1In_Object = MibTableColumn
adGenFrPVCDayIntervalOctetsDE1In = _AdGenFrPVCDayIntervalOctetsDE1In_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 29, 1, 3, 8, 1, 17),
    _AdGenFrPVCDayIntervalOctetsDE1In_Type()
)
adGenFrPVCDayIntervalOctetsDE1In.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenFrPVCDayIntervalOctetsDE1In.setStatus("current")
_AdGenFrPVCDayIntervalOctetsDE1Out_Type = Counter32
_AdGenFrPVCDayIntervalOctetsDE1Out_Object = MibTableColumn
adGenFrPVCDayIntervalOctetsDE1Out = _AdGenFrPVCDayIntervalOctetsDE1Out_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 29, 1, 3, 8, 1, 18),
    _AdGenFrPVCDayIntervalOctetsDE1Out_Type()
)
adGenFrPVCDayIntervalOctetsDE1Out.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenFrPVCDayIntervalOctetsDE1Out.setStatus("current")
_AdGenFrSlot_ObjectIdentity = ObjectIdentity
adGenFrSlot = _AdGenFrSlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 29, 1, 4)
)
_AdGenFrSlotTable_Object = MibTable
adGenFrSlotTable = _AdGenFrSlotTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 29, 1, 4, 1)
)
if mibBuilder.loadTexts:
    adGenFrSlotTable.setStatus("current")
_AdGenFrSlotEntry_Object = MibTableRow
adGenFrSlotEntry = _AdGenFrSlotEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 29, 1, 4, 1, 1)
)
adGenFrSlotEntry.setIndexNames(
    (0, "ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
)
if mibBuilder.loadTexts:
    adGenFrSlotEntry.setStatus("current")
_AdGenFrSlotGroupLastCreateError_Type = DisplayString
_AdGenFrSlotGroupLastCreateError_Object = MibTableColumn
adGenFrSlotGroupLastCreateError = _AdGenFrSlotGroupLastCreateError_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 29, 1, 4, 1, 1, 1),
    _AdGenFrSlotGroupLastCreateError_Type()
)
adGenFrSlotGroupLastCreateError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenFrSlotGroupLastCreateError.setStatus("current")
_AdGenFrSlotPVCMaxNumber_Type = Unsigned32
_AdGenFrSlotPVCMaxNumber_Object = MibTableColumn
adGenFrSlotPVCMaxNumber = _AdGenFrSlotPVCMaxNumber_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 29, 1, 4, 1, 1, 2),
    _AdGenFrSlotPVCMaxNumber_Type()
)
adGenFrSlotPVCMaxNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenFrSlotPVCMaxNumber.setStatus("current")
_AdGenFrSlotPVCCurrentNumber_Type = Unsigned32
_AdGenFrSlotPVCCurrentNumber_Object = MibTableColumn
adGenFrSlotPVCCurrentNumber = _AdGenFrSlotPVCCurrentNumber_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 29, 1, 4, 1, 1, 3),
    _AdGenFrSlotPVCCurrentNumber_Type()
)
adGenFrSlotPVCCurrentNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenFrSlotPVCCurrentNumber.setStatus("current")
_AdGenFrAlarmsPrefix_ObjectIdentity = ObjectIdentity
adGenFrAlarmsPrefix = _AdGenFrAlarmsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 29, 2)
)
_AdGenFrAlarms_ObjectIdentity = ObjectIdentity
adGenFrAlarms = _AdGenFrAlarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 29, 2, 0)
)

# Managed Objects groups


# Notification objects

adGenFrGroupDownAlarmClr = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 29, 2, 0, 1)
)
adGenFrGroupDownAlarmClr.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifOperStatus"),
        ("ADTRAN-TAeSCUEXT1-MIB", "adTAeSCUTrapAlarmLevel"),
        ("ADTRAN-GEN-FRAME-RELAY-MIB", "adGenFrGroupLmiStatus"))
)
if mibBuilder.loadTexts:
    adGenFrGroupDownAlarmClr.setStatus(
        "current"
    )

adGenFrGroupDownAlarmAct = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 29, 2, 0, 2)
)
adGenFrGroupDownAlarmAct.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifOperStatus"),
        ("ADTRAN-TAeSCUEXT1-MIB", "adTAeSCUTrapAlarmLevel"),
        ("ADTRAN-GEN-FRAME-RELAY-MIB", "adGenFrGroupLmiStatus"))
)
if mibBuilder.loadTexts:
    adGenFrGroupDownAlarmAct.setStatus(
        "current"
    )

adGenFrDlciDownAlarmClr = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 29, 2, 0, 3)
)
adGenFrDlciDownAlarmClr.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GEN-FRAME-RELAY-MIB", "adGenFrPVCIfIndex"),
        ("ADTRAN-GEN-FRAME-RELAY-MIB", "adGenFrPVCDLCIIndex"),
        ("ADTRAN-TAeSCUEXT1-MIB", "adTAeSCUTrapAlarmLevel"),
        ("ADTRAN-GEN-FRAME-RELAY-MIB", "adGenFrPVCState"))
)
if mibBuilder.loadTexts:
    adGenFrDlciDownAlarmClr.setStatus(
        "current"
    )

adGenFrDlciDownAlarmAct = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 29, 2, 0, 4)
)
adGenFrDlciDownAlarmAct.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GEN-FRAME-RELAY-MIB", "adGenFrPVCIfIndex"),
        ("ADTRAN-GEN-FRAME-RELAY-MIB", "adGenFrPVCDLCIIndex"),
        ("ADTRAN-TAeSCUEXT1-MIB", "adTAeSCUTrapAlarmLevel"),
        ("ADTRAN-GEN-FRAME-RELAY-MIB", "adGenFrPVCState"))
)
if mibBuilder.loadTexts:
    adGenFrDlciDownAlarmAct.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ADTRAN-GEN-FRAME-RELAY-MIB",
    **{"adGenFrameRelayMIBObjects": adGenFrameRelayMIBObjects,
       "adGenFrGroup": adGenFrGroup,
       "adGenFrGroupTable": adGenFrGroupTable,
       "adGenFrGroupEntry": adGenFrGroupEntry,
       "adGenFrGroupRowStatus": adGenFrGroupRowStatus,
       "adGenFrGroupStatusString": adGenFrGroupStatusString,
       "adGenFrGroupAdminStatus": adGenFrGroupAdminStatus,
       "adGenFrGroupLmiType": adGenFrGroupLmiType,
       "adGenFrGroupLmiStatus": adGenFrGroupLmiStatus,
       "adGenFrGroupLmiEnquiryIn": adGenFrGroupLmiEnquiryIn,
       "adGenFrGroupLmiEnquiryOut": adGenFrGroupLmiEnquiryOut,
       "adGenFrGroupLmiStatusIn": adGenFrGroupLmiStatusIn,
       "adGenFrGroupLmiStatusOut": adGenFrGroupLmiStatusOut,
       "adGenFrGroupLmiInvalidIn": adGenFrGroupLmiInvalidIn,
       "adGenFrGroupLmiStatusEnqTimeouts": adGenFrGroupLmiStatusEnqTimeouts,
       "adGenFrGroupLmiStatusTimeouts": adGenFrGroupLmiStatusTimeouts,
       "adGenFrGroupClearCounters": adGenFrGroupClearCounters,
       "adGenFrGroupClearPmHistory": adGenFrGroupClearPmHistory,
       "adGenFrGroupLinkLastCreateError": adGenFrGroupLinkLastCreateError,
       "adGenFrGroupPvcLastCreateError": adGenFrGroupPvcLastCreateError,
       "adGenFrGroupCurrentTable": adGenFrGroupCurrentTable,
       "adGenFrGroupCurrentEntry": adGenFrGroupCurrentEntry,
       "adGenFrGroupCurrentInOctets": adGenFrGroupCurrentInOctets,
       "adGenFrGroupCurrentInPkts": adGenFrGroupCurrentInPkts,
       "adGenFrGroupCurrentInDiscards": adGenFrGroupCurrentInDiscards,
       "adGenFrGroupCurrentInErrors": adGenFrGroupCurrentInErrors,
       "adGenFrGroupCurrentOutOctets": adGenFrGroupCurrentOutOctets,
       "adGenFrGroupCurrentOutPkts": adGenFrGroupCurrentOutPkts,
       "adGenFrGroupCurrentOutDiscards": adGenFrGroupCurrentOutDiscards,
       "adGenFrGroupCurrentOutErrors": adGenFrGroupCurrentOutErrors,
       "adGenFrGroupCurrentLmiEnquiryIn": adGenFrGroupCurrentLmiEnquiryIn,
       "adGenFrGroupCurrentLmiEnquiryOut": adGenFrGroupCurrentLmiEnquiryOut,
       "adGenFrGroupCurrentLmiStatusIn": adGenFrGroupCurrentLmiStatusIn,
       "adGenFrGroupCurrentLmiStatusOut": adGenFrGroupCurrentLmiStatusOut,
       "adGenFrGroupCurrentLmiInvalidIn": adGenFrGroupCurrentLmiInvalidIn,
       "adGenFrGroupCurrentLmiStatusEnqTimeouts": adGenFrGroupCurrentLmiStatusEnqTimeouts,
       "adGenFrGroupCurrentLmiStatusTimeouts": adGenFrGroupCurrentLmiStatusTimeouts,
       "adGenFrGroupCurrentNetworkInactive": adGenFrGroupCurrentNetworkInactive,
       "adGenFrGroupIntervalTable": adGenFrGroupIntervalTable,
       "adGenFrGroupIntervalEntry": adGenFrGroupIntervalEntry,
       "adGenFrGroupIntervalNumber": adGenFrGroupIntervalNumber,
       "adGenFrGroupIntervalTimeStamp": adGenFrGroupIntervalTimeStamp,
       "adGenFrGroupIntervalInOctets": adGenFrGroupIntervalInOctets,
       "adGenFrGroupIntervalInPkts": adGenFrGroupIntervalInPkts,
       "adGenFrGroupIntervalInDiscards": adGenFrGroupIntervalInDiscards,
       "adGenFrGroupIntervalInErrors": adGenFrGroupIntervalInErrors,
       "adGenFrGroupIntervalOutOctets": adGenFrGroupIntervalOutOctets,
       "adGenFrGroupIntervalOutPkts": adGenFrGroupIntervalOutPkts,
       "adGenFrGroupIntervalOutDiscards": adGenFrGroupIntervalOutDiscards,
       "adGenFrGroupIntervalOutErrors": adGenFrGroupIntervalOutErrors,
       "adGenFrGroupIntervalLmiEnquiryIn": adGenFrGroupIntervalLmiEnquiryIn,
       "adGenFrGroupIntervalLmiEnquiryOut": adGenFrGroupIntervalLmiEnquiryOut,
       "adGenFrGroupIntervalLmiStatusIn": adGenFrGroupIntervalLmiStatusIn,
       "adGenFrGroupIntervalLmiStatusOut": adGenFrGroupIntervalLmiStatusOut,
       "adGenFrGroupIntervalLmiInvalidIn": adGenFrGroupIntervalLmiInvalidIn,
       "adGenFrGroupIntervalLmiStatusEnqTimeouts": adGenFrGroupIntervalLmiStatusEnqTimeouts,
       "adGenFrGroupIntervalLmiStatusTimeouts": adGenFrGroupIntervalLmiStatusTimeouts,
       "adGenFrGroupIntervalNetworkInactive": adGenFrGroupIntervalNetworkInactive,
       "adGenFrGroupDayCurrentTable": adGenFrGroupDayCurrentTable,
       "adGenFrGroupDayCurrentEntry": adGenFrGroupDayCurrentEntry,
       "adGenFrGroupDayCurrentInOctets": adGenFrGroupDayCurrentInOctets,
       "adGenFrGroupDayCurrentInPkts": adGenFrGroupDayCurrentInPkts,
       "adGenFrGroupDayCurrentInDiscards": adGenFrGroupDayCurrentInDiscards,
       "adGenFrGroupDayCurrentInErrors": adGenFrGroupDayCurrentInErrors,
       "adGenFrGroupDayCurrentOutOctets": adGenFrGroupDayCurrentOutOctets,
       "adGenFrGroupDayCurrentOutPkts": adGenFrGroupDayCurrentOutPkts,
       "adGenFrGroupDayCurrentOutDiscards": adGenFrGroupDayCurrentOutDiscards,
       "adGenFrGroupDayCurrentOutErrors": adGenFrGroupDayCurrentOutErrors,
       "adGenFrGroupDayCurrentLmiEnquiryIn": adGenFrGroupDayCurrentLmiEnquiryIn,
       "adGenFrGroupDayCurrentLmiEnquiryOut": adGenFrGroupDayCurrentLmiEnquiryOut,
       "adGenFrGroupDayCurrentLmiStatusIn": adGenFrGroupDayCurrentLmiStatusIn,
       "adGenFrGroupDayCurrentLmiStatusOut": adGenFrGroupDayCurrentLmiStatusOut,
       "adGenFrGroupDayCurrentLmiInvalidIn": adGenFrGroupDayCurrentLmiInvalidIn,
       "adGenFrGroupDayCurrentLmiStatusEnqTimeouts": adGenFrGroupDayCurrentLmiStatusEnqTimeouts,
       "adGenFrGroupDayCurrentLmiStatusTimeouts": adGenFrGroupDayCurrentLmiStatusTimeouts,
       "adGenFrGroupDayCurrentNetworkInactive": adGenFrGroupDayCurrentNetworkInactive,
       "adGenFrGroupDayIntervalTable": adGenFrGroupDayIntervalTable,
       "adGenFrGroupDayIntervalEntry": adGenFrGroupDayIntervalEntry,
       "adGenFrGroupDayIntervalNumber": adGenFrGroupDayIntervalNumber,
       "adGenFrGroupDayIntervalTimeStamp": adGenFrGroupDayIntervalTimeStamp,
       "adGenFrGroupDayIntervalInOctets": adGenFrGroupDayIntervalInOctets,
       "adGenFrGroupDayIntervalInPkts": adGenFrGroupDayIntervalInPkts,
       "adGenFrGroupDayIntervalInDiscards": adGenFrGroupDayIntervalInDiscards,
       "adGenFrGroupDayIntervalInErrors": adGenFrGroupDayIntervalInErrors,
       "adGenFrGroupDayIntervalOutOctets": adGenFrGroupDayIntervalOutOctets,
       "adGenFrGroupDayIntervalOutPkts": adGenFrGroupDayIntervalOutPkts,
       "adGenFrGroupDayIntervalOutDiscards": adGenFrGroupDayIntervalOutDiscards,
       "adGenFrGroupDayIntervalOutErrors": adGenFrGroupDayIntervalOutErrors,
       "adGenFrGroupDayIntervalLmiEnquiryIn": adGenFrGroupDayIntervalLmiEnquiryIn,
       "adGenFrGroupDayIntervalLmiEnquiryOut": adGenFrGroupDayIntervalLmiEnquiryOut,
       "adGenFrGroupDayIntervalLmiStatusIn": adGenFrGroupDayIntervalLmiStatusIn,
       "adGenFrGroupDayIntervalLmiStatusOut": adGenFrGroupDayIntervalLmiStatusOut,
       "adGenFrGroupDayIntervalLmiInvalidIn": adGenFrGroupDayIntervalLmiInvalidIn,
       "adGenFrGroupDayIntervalLmiStatusEnqTimeouts": adGenFrGroupDayIntervalLmiStatusEnqTimeouts,
       "adGenFrGroupDayIntervalLmiStatusTimeouts": adGenFrGroupDayIntervalLmiStatusTimeouts,
       "adGenFrGroupDayIntervalNetworkInactive": adGenFrGroupDayIntervalNetworkInactive,
       "adGenFrLink": adGenFrLink,
       "adGenFrLinkTable": adGenFrLinkTable,
       "adGenFrLinkEntry": adGenFrLinkEntry,
       "adGenFrLinkGroupIfIndex": adGenFrLinkGroupIfIndex,
       "adGenFrLinkIfIndex": adGenFrLinkIfIndex,
       "adGenFrLinkBundleId": adGenFrLinkBundleId,
       "adGenFrLinkRowStatus": adGenFrLinkRowStatus,
       "adGenFrLinkTimeslots": adGenFrLinkTimeslots,
       "adGenFrLinkStatusString": adGenFrLinkStatusString,
       "adGenFrPVC": adGenFrPVC,
       "adGenFrPVCTable": adGenFrPVCTable,
       "adGenFrPVCEntry": adGenFrPVCEntry,
       "adGenFrPVCIfIndex": adGenFrPVCIfIndex,
       "adGenFrPVCDLCIIndex": adGenFrPVCDLCIIndex,
       "adGenFrPVCStatusString": adGenFrPVCStatusString,
       "adGenFrPVCAdminStatus": adGenFrPVCAdminStatus,
       "adGenFrPVCState": adGenFrPVCState,
       "adGenFrPVCEncapsulation": adGenFrPVCEncapsulation,
       "adGenFrPVCPrimaryPeerIpAddressType": adGenFrPVCPrimaryPeerIpAddressType,
       "adGenFrPVCPrimaryPeerIpAddress": adGenFrPVCPrimaryPeerIpAddress,
       "adGenFrPVCSecondaryPeerAddressType": adGenFrPVCSecondaryPeerAddressType,
       "adGenFrPVCSecondaryPeerIpAddress": adGenFrPVCSecondaryPeerIpAddress,
       "adGenFrPVCPrimaryGatewayAddressType": adGenFrPVCPrimaryGatewayAddressType,
       "adGenFrPVCPrimaryGatewayAddress": adGenFrPVCPrimaryGatewayAddress,
       "adGenFrPVCInverseArpEnable": adGenFrPVCInverseArpEnable,
       "adGenFrPVCLearnedPrimaryPeerIpAddressType": adGenFrPVCLearnedPrimaryPeerIpAddressType,
       "adGenFrPVCLearnedPrimaryPeerIpAddress": adGenFrPVCLearnedPrimaryPeerIpAddress,
       "adGenFrPVCLearnedSecondaryPeerAddressType": adGenFrPVCLearnedSecondaryPeerAddressType,
       "adGenFrPVCLearnedSecondaryPeerIpAddress": adGenFrPVCLearnedSecondaryPeerIpAddress,
       "adGenFrPVCClearCounters": adGenFrPVCClearCounters,
       "adGenFrPVCClearPmHistory": adGenFrPVCClearPmHistory,
       "adGenFrPVCOperStatus": adGenFrPVCOperStatus,
       "adGenFrPVCLastChange": adGenFrPVCLastChange,
       "adGenFrPVCDescription": adGenFrPVCDescription,
       "adGenFrPVCMtu": adGenFrPVCMtu,
       "adGenFrPVCCurrentTable": adGenFrPVCCurrentTable,
       "adGenFrPVCCurrentEntry": adGenFrPVCCurrentEntry,
       "adGenFrPVCCurrentInOctets": adGenFrPVCCurrentInOctets,
       "adGenFrPVCCurrentInPkts": adGenFrPVCCurrentInPkts,
       "adGenFrPVCCurrentInDiscards": adGenFrPVCCurrentInDiscards,
       "adGenFrPVCCurrentOutOctets": adGenFrPVCCurrentOutOctets,
       "adGenFrPVCCurrentOutPkts": adGenFrPVCCurrentOutPkts,
       "adGenFrPVCCurrentOutDiscards": adGenFrPVCCurrentOutDiscards,
       "adGenFrPVCCurrentPktsFECN1In": adGenFrPVCCurrentPktsFECN1In,
       "adGenFrPVCCurrentPktsFECN1Out": adGenFrPVCCurrentPktsFECN1Out,
       "adGenFrPVCCurrentPktsBECN1In": adGenFrPVCCurrentPktsBECN1In,
       "adGenFrPVCCurrentPktsBECN1Out": adGenFrPVCCurrentPktsBECN1Out,
       "adGenFrPVCCurrentPktsDE1In": adGenFrPVCCurrentPktsDE1In,
       "adGenFrPVCCurrentPktsDE1Out": adGenFrPVCCurrentPktsDE1Out,
       "adGenFrPVCCurrentOctetsDE1In": adGenFrPVCCurrentOctetsDE1In,
       "adGenFrPVCCurrentOctetsDE1Out": adGenFrPVCCurrentOctetsDE1Out,
       "adGenFrPVCIntervalTable": adGenFrPVCIntervalTable,
       "adGenFrPVCIntervalEntry": adGenFrPVCIntervalEntry,
       "adGenFrPVCIntervalNumber": adGenFrPVCIntervalNumber,
       "adGenFrPVCIntervalTimeStamp": adGenFrPVCIntervalTimeStamp,
       "adGenFrPVCIntervalInOctets": adGenFrPVCIntervalInOctets,
       "adGenFrPVCIntervalInPkts": adGenFrPVCIntervalInPkts,
       "adGenFrPVCIntervalInDiscards": adGenFrPVCIntervalInDiscards,
       "adGenFrPVCIntervalOutOctets": adGenFrPVCIntervalOutOctets,
       "adGenFrPVCIntervalOutPkts": adGenFrPVCIntervalOutPkts,
       "adGenFrPVCIntervalOutDiscards": adGenFrPVCIntervalOutDiscards,
       "adGenFrPVCIntervalPktsFECN1In": adGenFrPVCIntervalPktsFECN1In,
       "adGenFrPVCIntervalPktsFECN1Out": adGenFrPVCIntervalPktsFECN1Out,
       "adGenFrPVCIntervalPktsBECN1In": adGenFrPVCIntervalPktsBECN1In,
       "adGenFrPVCIntervalPktsBECN1Out": adGenFrPVCIntervalPktsBECN1Out,
       "adGenFrPVCIntervalPktsDE1In": adGenFrPVCIntervalPktsDE1In,
       "adGenFrPVCIntervalPktsDE1Out": adGenFrPVCIntervalPktsDE1Out,
       "adGenFrPVCIntervalOctetsDE1In": adGenFrPVCIntervalOctetsDE1In,
       "adGenFrPVCIntervalOctetsDE1Out": adGenFrPVCIntervalOctetsDE1Out,
       "adGenFrPVCDayCurrentTable": adGenFrPVCDayCurrentTable,
       "adGenFrPVCDayCurrentEntry": adGenFrPVCDayCurrentEntry,
       "adGenFrPVCDayCurrentInOctets": adGenFrPVCDayCurrentInOctets,
       "adGenFrPVCDayCurrentInPkts": adGenFrPVCDayCurrentInPkts,
       "adGenFrPVCDayCurrentInDiscards": adGenFrPVCDayCurrentInDiscards,
       "adGenFrPVCDayCurrentOutOctets": adGenFrPVCDayCurrentOutOctets,
       "adGenFrPVCDayCurrentOutPkts": adGenFrPVCDayCurrentOutPkts,
       "adGenFrPVCDayCurrentOutDiscards": adGenFrPVCDayCurrentOutDiscards,
       "adGenFrPVCDayCurrentPktsFECN1In": adGenFrPVCDayCurrentPktsFECN1In,
       "adGenFrPVCDayCurrentPktsFECN1Out": adGenFrPVCDayCurrentPktsFECN1Out,
       "adGenFrPVCDayCurrentPktsBECN1In": adGenFrPVCDayCurrentPktsBECN1In,
       "adGenFrPVCDayCurrentPktsBECN1Out": adGenFrPVCDayCurrentPktsBECN1Out,
       "adGenFrPVCDayCurrentPktsDE1In": adGenFrPVCDayCurrentPktsDE1In,
       "adGenFrPVCDayCurrentPktsDE1Out": adGenFrPVCDayCurrentPktsDE1Out,
       "adGenFrPVCDayCurrentOctetsDE1In": adGenFrPVCDayCurrentOctetsDE1In,
       "adGenFrPVCDayCurrentOctetsDE1Out": adGenFrPVCDayCurrentOctetsDE1Out,
       "adGenFrPVCDayIntervalTable": adGenFrPVCDayIntervalTable,
       "adGenFrPVCDayIntervalEntry": adGenFrPVCDayIntervalEntry,
       "adGenFrPVCDayIntervalNumber": adGenFrPVCDayIntervalNumber,
       "adGenFrPVCDayIntervalTimeStamp": adGenFrPVCDayIntervalTimeStamp,
       "adGenFrPVCDayIntervalInOctets": adGenFrPVCDayIntervalInOctets,
       "adGenFrPVCDayIntervalInPkts": adGenFrPVCDayIntervalInPkts,
       "adGenFrPVCDayIntervalInDiscards": adGenFrPVCDayIntervalInDiscards,
       "adGenFrPVCDayIntervalOutOctets": adGenFrPVCDayIntervalOutOctets,
       "adGenFrPVCDayIntervalOutPkts": adGenFrPVCDayIntervalOutPkts,
       "adGenFrPVCDayIntervalOutDiscards": adGenFrPVCDayIntervalOutDiscards,
       "adGenFrPVCDayIntervalPktsFECN1In": adGenFrPVCDayIntervalPktsFECN1In,
       "adGenFrPVCDayIntervalPktsFECN1Out": adGenFrPVCDayIntervalPktsFECN1Out,
       "adGenFrPVCDayIntervalPktsBECN1In": adGenFrPVCDayIntervalPktsBECN1In,
       "adGenFrPVCDayIntervalPktsBECN1Out": adGenFrPVCDayIntervalPktsBECN1Out,
       "adGenFrPVCDayIntervalPktsDE1In": adGenFrPVCDayIntervalPktsDE1In,
       "adGenFrPVCDayIntervalPktsDE1Out": adGenFrPVCDayIntervalPktsDE1Out,
       "adGenFrPVCDayIntervalOctetsDE1In": adGenFrPVCDayIntervalOctetsDE1In,
       "adGenFrPVCDayIntervalOctetsDE1Out": adGenFrPVCDayIntervalOctetsDE1Out,
       "adGenFrSlot": adGenFrSlot,
       "adGenFrSlotTable": adGenFrSlotTable,
       "adGenFrSlotEntry": adGenFrSlotEntry,
       "adGenFrSlotGroupLastCreateError": adGenFrSlotGroupLastCreateError,
       "adGenFrSlotPVCMaxNumber": adGenFrSlotPVCMaxNumber,
       "adGenFrSlotPVCCurrentNumber": adGenFrSlotPVCCurrentNumber,
       "adGenFrAlarmsPrefix": adGenFrAlarmsPrefix,
       "adGenFrAlarms": adGenFrAlarms,
       "adGenFrGroupDownAlarmClr": adGenFrGroupDownAlarmClr,
       "adGenFrGroupDownAlarmAct": adGenFrGroupDownAlarmAct,
       "adGenFrDlciDownAlarmClr": adGenFrDlciDownAlarmClr,
       "adGenFrDlciDownAlarmAct": adGenFrDlciDownAlarmAct,
       "adGenFrameRelayMib": adGenFrameRelayMib}
)
