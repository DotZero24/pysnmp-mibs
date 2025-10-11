# SNMP MIB module (ADTRAN-GENMUXPONDER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/adtran/ADTRAN-GENMUXPONDER-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:30:41 2025
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

(adGenMuxPonder,
 adGenMuxPonderID) = mibBuilder.importSymbols(
    "ADTRAN-SHARED-CND-SYSTEM-MIB",
    "adGenMuxPonder",
    "adGenMuxPonderID")

(GenSystemInterfaceType,) = mibBuilder.importSymbols(
    "ADTRAN-SHARED-CND-SYSTEM-TC-MIB",
    "GenSystemInterfaceType")

(adTAeSCUTrapAlarmLevel,) = mibBuilder.importSymbols(
    "ADTRAN-TAeSCUEXT1-MIB",
    "adTAeSCUTrapAlarmLevel")

(InterfaceIndex,
 InterfaceIndexOrZero,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero",
    "ifIndex")

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

adGenMuxponderIdentity = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 70, 26, 1)
)
if mibBuilder.loadTexts:
    adGenMuxponderIdentity.setRevisions(
        ("2014-10-17 00:00",
         "2014-09-22 00:00",
         "2014-07-01 00:00",
         "2014-06-13 00:00",
         "2014-01-16 00:00",
         "2013-07-18 00:00",
         "2013-03-20 00:00",
         "2013-01-14 00:00",
         "2012-10-25 00:00",
         "2012-10-16 00:00",
         "2012-09-06 00:00",
         "2012-08-21 00:00",
         "2012-05-17 00:00",
         "2012-03-26 00:00",
         "2012-02-13 00:00",
         "2012-01-26 00:00",
         "2011-12-20 00:00",
         "2011-10-13 00:00",
         "2011-08-15 00:00",
         "2011-06-27 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class MuxPPayloadTypes(TextualConvention, Integer32):
    status = "current"
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
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("sts1", 2),
          ("sts3c", 3),
          ("sts12c", 4),
          ("sts48c", 5),
          ("sts192c", 6),
          ("sonetLine", 7),
          ("vc3", 8),
          ("vc4", 9),
          ("vc4x4c", 10),
          ("vc4x16c", 11),
          ("vc4x64c", 12),
          ("sdhLine", 13),
          ("otnPort", 14),
          ("odu4", 15),
          ("odu3", 16),
          ("odu3e1", 17),
          ("odu3e2", 18),
          ("odu2", 19),
          ("odu2e", 20),
          ("odu2f", 21),
          ("odu1e", 22),
          ("odu1f", 23),
          ("odu1", 24),
          ("odu0", 25),
          ("oduflex", 26),
          ("timeslot", 27),
          ("gigabitEthernet", 28),
          ("tenGigabitEthernet", 29),
          ("fibreChannel1G", 30),
          ("fibreChannel2G", 31),
          ("fibreChannel4G", 32),
          ("fibreChannel8G", 33),
          ("fibreChannel10G", 34))
    )



class MuxPMapInterface(TextualConvention, OctetString):
    status = "current"
    displayHint = "1d 1d 1d 1d 1d 1d 1d 1d 2d"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 10),
    )
    fixed_length = 10



class EthernetPayloadTypes(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notCompatible", 1),
          ("gigabitEthernet", 2),
          ("tenGigabitEthernet", 3))
    )



class FibreChanPayloadTypes(TextualConvention, Integer32):
    status = "current"
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
        *(("notCompatible", 1),
          ("fibreChannel1G", 2),
          ("fibreChannel2G", 3),
          ("fibreChannel4G", 4),
          ("fibreChannel8G", 5),
          ("fibreChannel10G", 6))
    )



# MIB Managed Objects in the order of their OIDs

_AdGenMuxPPhysIfProv_ObjectIdentity = ObjectIdentity
adGenMuxPPhysIfProv = _AdGenMuxPPhysIfProv_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 1)
)
_AdGenMuxPPhysIfProvTable_Object = MibTable
adGenMuxPPhysIfProvTable = _AdGenMuxPPhysIfProvTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 1, 1)
)
if mibBuilder.loadTexts:
    adGenMuxPPhysIfProvTable.setStatus("current")
_AdGenMuxPPhysIfProvEntry_Object = MibTableRow
adGenMuxPPhysIfProvEntry = _AdGenMuxPPhysIfProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 1, 1, 1)
)
adGenMuxPPhysIfProvEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adGenMuxPPhysIfProvEntry.setStatus("current")
_AdGenMuxPPhysIfType_Type = GenSystemInterfaceType
_AdGenMuxPPhysIfType_Object = MibTableColumn
adGenMuxPPhysIfType = _AdGenMuxPPhysIfType_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 1, 1, 1, 1),
    _AdGenMuxPPhysIfType_Type()
)
adGenMuxPPhysIfType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenMuxPPhysIfType.setStatus("current")
_AdGenMuxPPeerIpAddress_Type = IpAddress
_AdGenMuxPPeerIpAddress_Object = MibTableColumn
adGenMuxPPeerIpAddress = _AdGenMuxPPeerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 1, 1, 1, 2),
    _AdGenMuxPPeerIpAddress_Type()
)
adGenMuxPPeerIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenMuxPPeerIpAddress.setStatus("deprecated")
_AdGenMuxPPeerChassisId_Type = DisplayString
_AdGenMuxPPeerChassisId_Object = MibTableColumn
adGenMuxPPeerChassisId = _AdGenMuxPPeerChassisId_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 1, 1, 1, 3),
    _AdGenMuxPPeerChassisId_Type()
)
adGenMuxPPeerChassisId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenMuxPPeerChassisId.setStatus("deprecated")
_AdGenMuxPPeerPortId_Type = DisplayString
_AdGenMuxPPeerPortId_Object = MibTableColumn
adGenMuxPPeerPortId = _AdGenMuxPPeerPortId_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 1, 1, 1, 4),
    _AdGenMuxPPeerPortId_Type()
)
adGenMuxPPeerPortId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenMuxPPeerPortId.setStatus("deprecated")
_AdGenMuxPFacilityLoopbackEnable_Type = TruthValue
_AdGenMuxPFacilityLoopbackEnable_Object = MibTableColumn
adGenMuxPFacilityLoopbackEnable = _AdGenMuxPFacilityLoopbackEnable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 1, 1, 1, 5),
    _AdGenMuxPFacilityLoopbackEnable_Type()
)
adGenMuxPFacilityLoopbackEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenMuxPFacilityLoopbackEnable.setStatus("current")


class _AdGenMuxPFacilityLoopbackTimeout_Type(Integer32):
    """Custom type adGenMuxPFacilityLoopbackTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9999),
    )


_AdGenMuxPFacilityLoopbackTimeout_Type.__name__ = "Integer32"
_AdGenMuxPFacilityLoopbackTimeout_Object = MibTableColumn
adGenMuxPFacilityLoopbackTimeout = _AdGenMuxPFacilityLoopbackTimeout_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 1, 1, 1, 6),
    _AdGenMuxPFacilityLoopbackTimeout_Type()
)
adGenMuxPFacilityLoopbackTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenMuxPFacilityLoopbackTimeout.setStatus("current")


class _AdGenMuxPFacilityLoopbackTimeRemaining_Type(DisplayString):
    """Custom type adGenMuxPFacilityLoopbackTimeRemaining based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_AdGenMuxPFacilityLoopbackTimeRemaining_Type.__name__ = "DisplayString"
_AdGenMuxPFacilityLoopbackTimeRemaining_Object = MibTableColumn
adGenMuxPFacilityLoopbackTimeRemaining = _AdGenMuxPFacilityLoopbackTimeRemaining_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 1, 1, 1, 7),
    _AdGenMuxPFacilityLoopbackTimeRemaining_Type()
)
adGenMuxPFacilityLoopbackTimeRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMuxPFacilityLoopbackTimeRemaining.setStatus("current")
_AdGenMuxPTerminalLoopbackEnable_Type = TruthValue
_AdGenMuxPTerminalLoopbackEnable_Object = MibTableColumn
adGenMuxPTerminalLoopbackEnable = _AdGenMuxPTerminalLoopbackEnable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 1, 1, 1, 8),
    _AdGenMuxPTerminalLoopbackEnable_Type()
)
adGenMuxPTerminalLoopbackEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenMuxPTerminalLoopbackEnable.setStatus("current")


class _AdGenMuxPTerminalLoopbackTimeout_Type(Integer32):
    """Custom type adGenMuxPTerminalLoopbackTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9999),
    )


_AdGenMuxPTerminalLoopbackTimeout_Type.__name__ = "Integer32"
_AdGenMuxPTerminalLoopbackTimeout_Object = MibTableColumn
adGenMuxPTerminalLoopbackTimeout = _AdGenMuxPTerminalLoopbackTimeout_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 1, 1, 1, 9),
    _AdGenMuxPTerminalLoopbackTimeout_Type()
)
adGenMuxPTerminalLoopbackTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenMuxPTerminalLoopbackTimeout.setStatus("current")


class _AdGenMuxPTerminalLoopbackTimeRemaining_Type(DisplayString):
    """Custom type adGenMuxPTerminalLoopbackTimeRemaining based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_AdGenMuxPTerminalLoopbackTimeRemaining_Type.__name__ = "DisplayString"
_AdGenMuxPTerminalLoopbackTimeRemaining_Object = MibTableColumn
adGenMuxPTerminalLoopbackTimeRemaining = _AdGenMuxPTerminalLoopbackTimeRemaining_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 1, 1, 1, 10),
    _AdGenMuxPTerminalLoopbackTimeRemaining_Type()
)
adGenMuxPTerminalLoopbackTimeRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMuxPTerminalLoopbackTimeRemaining.setStatus("current")


class _AdGenMuxPYCableEnable_Type(TruthValue):
    """Custom type adGenMuxPYCableEnable based on TruthValue"""
    defaultValue = 2


_AdGenMuxPYCableEnable_Type.__name__ = "TruthValue"
_AdGenMuxPYCableEnable_Object = MibTableColumn
adGenMuxPYCableEnable = _AdGenMuxPYCableEnable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 1, 1, 1, 11),
    _AdGenMuxPYCableEnable_Type()
)
adGenMuxPYCableEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenMuxPYCableEnable.setStatus("current")


class _AdGenMuxPProtectedPairEnable_Type(TruthValue):
    """Custom type adGenMuxPProtectedPairEnable based on TruthValue"""
    defaultValue = 2


_AdGenMuxPProtectedPairEnable_Type.__name__ = "TruthValue"
_AdGenMuxPProtectedPairEnable_Object = MibTableColumn
adGenMuxPProtectedPairEnable = _AdGenMuxPProtectedPairEnable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 1, 1, 1, 12),
    _AdGenMuxPProtectedPairEnable_Type()
)
adGenMuxPProtectedPairEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenMuxPProtectedPairEnable.setStatus("current")


class _AdGenMuxPForwardingGroupLimitedEnable_Type(TruthValue):
    """Custom type adGenMuxPForwardingGroupLimitedEnable based on TruthValue"""
    defaultValue = 2


_AdGenMuxPForwardingGroupLimitedEnable_Type.__name__ = "TruthValue"
_AdGenMuxPForwardingGroupLimitedEnable_Object = MibTableColumn
adGenMuxPForwardingGroupLimitedEnable = _AdGenMuxPForwardingGroupLimitedEnable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 1, 1, 1, 13),
    _AdGenMuxPForwardingGroupLimitedEnable_Type()
)
adGenMuxPForwardingGroupLimitedEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenMuxPForwardingGroupLimitedEnable.setStatus("current")
_AdGenMuxPCrossConnectProv_ObjectIdentity = ObjectIdentity
adGenMuxPCrossConnectProv = _AdGenMuxPCrossConnectProv_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 2)
)
_AdGenMuxPCrossConnectTable_Object = MibTable
adGenMuxPCrossConnectTable = _AdGenMuxPCrossConnectTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 2, 1)
)
if mibBuilder.loadTexts:
    adGenMuxPCrossConnectTable.setStatus("current")
_AdGenMuxPCrossConnectEntry_Object = MibTableRow
adGenMuxPCrossConnectEntry = _AdGenMuxPCrossConnectEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 2, 1, 1)
)
adGenMuxPCrossConnectEntry.setIndexNames(
    (0, "ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
    (1, "ADTRAN-GENMUXPONDER-MIB", "adGenMuxPCrossConnectName"),
)
if mibBuilder.loadTexts:
    adGenMuxPCrossConnectEntry.setStatus("current")


class _AdGenMuxPCrossConnectName_Type(DisplayString):
    """Custom type adGenMuxPCrossConnectName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 50),
    )


_AdGenMuxPCrossConnectName_Type.__name__ = "DisplayString"
_AdGenMuxPCrossConnectName_Object = MibTableColumn
adGenMuxPCrossConnectName = _AdGenMuxPCrossConnectName_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 2, 1, 1, 1),
    _AdGenMuxPCrossConnectName_Type()
)
adGenMuxPCrossConnectName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adGenMuxPCrossConnectName.setStatus("current")


class _AdGenMuxPCrossConnectType_Type(Integer32):
    """Custom type adGenMuxPCrossConnectType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("twoWay", 1),
          ("oneWay", 2))
    )


_AdGenMuxPCrossConnectType_Type.__name__ = "Integer32"
_AdGenMuxPCrossConnectType_Object = MibTableColumn
adGenMuxPCrossConnectType = _AdGenMuxPCrossConnectType_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 2, 1, 1, 2),
    _AdGenMuxPCrossConnectType_Type()
)
adGenMuxPCrossConnectType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenMuxPCrossConnectType.setStatus("current")
_AdGenMuxPCrossConnectSrcType_Type = MuxPPayloadTypes
_AdGenMuxPCrossConnectSrcType_Object = MibTableColumn
adGenMuxPCrossConnectSrcType = _AdGenMuxPCrossConnectSrcType_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 2, 1, 1, 3),
    _AdGenMuxPCrossConnectSrcType_Type()
)
adGenMuxPCrossConnectSrcType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMuxPCrossConnectSrcType.setStatus("current")
_AdGenMuxPCrossConnectSrcIfIndex_Type = InterfaceIndex
_AdGenMuxPCrossConnectSrcIfIndex_Object = MibTableColumn
adGenMuxPCrossConnectSrcIfIndex = _AdGenMuxPCrossConnectSrcIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 2, 1, 1, 4),
    _AdGenMuxPCrossConnectSrcIfIndex_Type()
)
adGenMuxPCrossConnectSrcIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenMuxPCrossConnectSrcIfIndex.setStatus("current")
_AdGenMuxPCrossConnectDstType_Type = MuxPPayloadTypes
_AdGenMuxPCrossConnectDstType_Object = MibTableColumn
adGenMuxPCrossConnectDstType = _AdGenMuxPCrossConnectDstType_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 2, 1, 1, 5),
    _AdGenMuxPCrossConnectDstType_Type()
)
adGenMuxPCrossConnectDstType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenMuxPCrossConnectDstType.setStatus("current")
_AdGenMuxPCrossConnectDstIfIndex_Type = InterfaceIndex
_AdGenMuxPCrossConnectDstIfIndex_Object = MibTableColumn
adGenMuxPCrossConnectDstIfIndex = _AdGenMuxPCrossConnectDstIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 2, 1, 1, 6),
    _AdGenMuxPCrossConnectDstIfIndex_Type()
)
adGenMuxPCrossConnectDstIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenMuxPCrossConnectDstIfIndex.setStatus("current")
_AdGenMuxPCrossConnectRowStatus_Type = RowStatus
_AdGenMuxPCrossConnectRowStatus_Object = MibTableColumn
adGenMuxPCrossConnectRowStatus = _AdGenMuxPCrossConnectRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 2, 1, 1, 7),
    _AdGenMuxPCrossConnectRowStatus_Type()
)
adGenMuxPCrossConnectRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenMuxPCrossConnectRowStatus.setStatus("current")
_AdGenMuxPCrossConnectLastProvError_Type = DisplayString
_AdGenMuxPCrossConnectLastProvError_Object = MibTableColumn
adGenMuxPCrossConnectLastProvError = _AdGenMuxPCrossConnectLastProvError_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 2, 1, 1, 8),
    _AdGenMuxPCrossConnectLastProvError_Type()
)
adGenMuxPCrossConnectLastProvError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMuxPCrossConnectLastProvError.setStatus("current")
_AdGenMuxPCrossConnectLastCreateErrorTable_Object = MibTable
adGenMuxPCrossConnectLastCreateErrorTable = _AdGenMuxPCrossConnectLastCreateErrorTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 2, 2)
)
if mibBuilder.loadTexts:
    adGenMuxPCrossConnectLastCreateErrorTable.setStatus("current")
_AdGenMuxPCrossConnectLastCreateErrorEntry_Object = MibTableRow
adGenMuxPCrossConnectLastCreateErrorEntry = _AdGenMuxPCrossConnectLastCreateErrorEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 2, 2, 1)
)
adGenMuxPCrossConnectLastCreateErrorEntry.setIndexNames(
    (0, "ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
)
if mibBuilder.loadTexts:
    adGenMuxPCrossConnectLastCreateErrorEntry.setStatus("current")
_AdGenMuxPCrossConnectLastCreateError_Type = DisplayString
_AdGenMuxPCrossConnectLastCreateError_Object = MibTableColumn
adGenMuxPCrossConnectLastCreateError = _AdGenMuxPCrossConnectLastCreateError_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 2, 2, 1, 1),
    _AdGenMuxPCrossConnectLastCreateError_Type()
)
adGenMuxPCrossConnectLastCreateError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMuxPCrossConnectLastCreateError.setStatus("current")
_AdGenMuxPPortCrossConnectStatusTable_Object = MibTable
adGenMuxPPortCrossConnectStatusTable = _AdGenMuxPPortCrossConnectStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 2, 3)
)
if mibBuilder.loadTexts:
    adGenMuxPPortCrossConnectStatusTable.setStatus("current")
_AdGenMuxPPortCrossConnectStatusEntry_Object = MibTableRow
adGenMuxPPortCrossConnectStatusEntry = _AdGenMuxPPortCrossConnectStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 2, 3, 1)
)
adGenMuxPPortCrossConnectStatusEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ADTRAN-GENMUXPONDER-MIB", "adGenMuxPPortCrossConnectName"),
)
if mibBuilder.loadTexts:
    adGenMuxPPortCrossConnectStatusEntry.setStatus("current")


class _AdGenMuxPPortCrossConnectName_Type(DisplayString):
    """Custom type adGenMuxPPortCrossConnectName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 50),
    )


_AdGenMuxPPortCrossConnectName_Type.__name__ = "DisplayString"
_AdGenMuxPPortCrossConnectName_Object = MibTableColumn
adGenMuxPPortCrossConnectName = _AdGenMuxPPortCrossConnectName_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 2, 3, 1, 1),
    _AdGenMuxPPortCrossConnectName_Type()
)
adGenMuxPPortCrossConnectName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMuxPPortCrossConnectName.setStatus("current")


class _AdGenMuxPPortCrossConnectStatus_Type(Integer32):
    """Custom type adGenMuxPPortCrossConnectStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("source", 1),
          ("destination", 2),
          ("sourceAndDestination", 3))
    )


_AdGenMuxPPortCrossConnectStatus_Type.__name__ = "Integer32"
_AdGenMuxPPortCrossConnectStatus_Object = MibTableColumn
adGenMuxPPortCrossConnectStatus = _AdGenMuxPPortCrossConnectStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 2, 3, 1, 2),
    _AdGenMuxPPortCrossConnectStatus_Type()
)
adGenMuxPPortCrossConnectStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMuxPPortCrossConnectStatus.setStatus("current")
_AdGenMuxPProtGroupProv_ObjectIdentity = ObjectIdentity
adGenMuxPProtGroupProv = _AdGenMuxPProtGroupProv_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 3)
)
_AdGenMuxPProtGroupTable_Object = MibTable
adGenMuxPProtGroupTable = _AdGenMuxPProtGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 3, 1)
)
if mibBuilder.loadTexts:
    adGenMuxPProtGroupTable.setStatus("current")
_AdGenMuxPProtGroupEntry_Object = MibTableRow
adGenMuxPProtGroupEntry = _AdGenMuxPProtGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 3, 1, 1)
)
adGenMuxPProtGroupEntry.setIndexNames(
    (0, "ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
    (1, "ADTRAN-GENMUXPONDER-MIB", "adGenMuxPProtGroupName"),
)
if mibBuilder.loadTexts:
    adGenMuxPProtGroupEntry.setStatus("current")


class _AdGenMuxPProtGroupName_Type(DisplayString):
    """Custom type adGenMuxPProtGroupName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 50),
    )


_AdGenMuxPProtGroupName_Type.__name__ = "DisplayString"
_AdGenMuxPProtGroupName_Object = MibTableColumn
adGenMuxPProtGroupName = _AdGenMuxPProtGroupName_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 3, 1, 1, 1),
    _AdGenMuxPProtGroupName_Type()
)
adGenMuxPProtGroupName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adGenMuxPProtGroupName.setStatus("current")


class _AdGenMuxPProtGroupType_Type(Integer32):
    """Custom type adGenMuxPProtGroupType based on Integer32"""
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
        *(("upsr", 1),
          ("terminalUniDir", 2),
          ("terminalBiDir", 3),
          ("yCable", 4))
    )


_AdGenMuxPProtGroupType_Type.__name__ = "Integer32"
_AdGenMuxPProtGroupType_Object = MibTableColumn
adGenMuxPProtGroupType = _AdGenMuxPProtGroupType_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 3, 1, 1, 2),
    _AdGenMuxPProtGroupType_Type()
)
adGenMuxPProtGroupType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenMuxPProtGroupType.setStatus("current")
_AdGenMuxPProtGroupWorkingType_Type = MuxPPayloadTypes
_AdGenMuxPProtGroupWorkingType_Object = MibTableColumn
adGenMuxPProtGroupWorkingType = _AdGenMuxPProtGroupWorkingType_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 3, 1, 1, 3),
    _AdGenMuxPProtGroupWorkingType_Type()
)
adGenMuxPProtGroupWorkingType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMuxPProtGroupWorkingType.setStatus("current")
_AdGenMuxPProtGroupWorkingIfIndex_Type = InterfaceIndex
_AdGenMuxPProtGroupWorkingIfIndex_Object = MibTableColumn
adGenMuxPProtGroupWorkingIfIndex = _AdGenMuxPProtGroupWorkingIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 3, 1, 1, 4),
    _AdGenMuxPProtGroupWorkingIfIndex_Type()
)
adGenMuxPProtGroupWorkingIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenMuxPProtGroupWorkingIfIndex.setStatus("current")
_AdGenMuxPProtGroupProtectingType_Type = MuxPPayloadTypes
_AdGenMuxPProtGroupProtectingType_Object = MibTableColumn
adGenMuxPProtGroupProtectingType = _AdGenMuxPProtGroupProtectingType_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 3, 1, 1, 5),
    _AdGenMuxPProtGroupProtectingType_Type()
)
adGenMuxPProtGroupProtectingType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenMuxPProtGroupProtectingType.setStatus("current")
_AdGenMuxPProtGroupProtectingIfIndex_Type = InterfaceIndex
_AdGenMuxPProtGroupProtectingIfIndex_Object = MibTableColumn
adGenMuxPProtGroupProtectingIfIndex = _AdGenMuxPProtGroupProtectingIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 3, 1, 1, 6),
    _AdGenMuxPProtGroupProtectingIfIndex_Type()
)
adGenMuxPProtGroupProtectingIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenMuxPProtGroupProtectingIfIndex.setStatus("current")
_AdGenMuxPProtGroupRowStatus_Type = RowStatus
_AdGenMuxPProtGroupRowStatus_Object = MibTableColumn
adGenMuxPProtGroupRowStatus = _AdGenMuxPProtGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 3, 1, 1, 7),
    _AdGenMuxPProtGroupRowStatus_Type()
)
adGenMuxPProtGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenMuxPProtGroupRowStatus.setStatus("current")
_AdGenMuxPProtGroupLastProvError_Type = DisplayString
_AdGenMuxPProtGroupLastProvError_Object = MibTableColumn
adGenMuxPProtGroupLastProvError = _AdGenMuxPProtGroupLastProvError_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 3, 1, 1, 8),
    _AdGenMuxPProtGroupLastProvError_Type()
)
adGenMuxPProtGroupLastProvError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMuxPProtGroupLastProvError.setStatus("current")
_AdGenMuxPProtGroupWorkIsOnline_Type = TruthValue
_AdGenMuxPProtGroupWorkIsOnline_Object = MibTableColumn
adGenMuxPProtGroupWorkIsOnline = _AdGenMuxPProtGroupWorkIsOnline_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 3, 1, 1, 9),
    _AdGenMuxPProtGroupWorkIsOnline_Type()
)
adGenMuxPProtGroupWorkIsOnline.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMuxPProtGroupWorkIsOnline.setStatus("current")


class _AdGenMuxPProtGroupSwitchCommands_Type(Integer32):
    """Custom type adGenMuxPProtGroupSwitchCommands based on Integer32"""
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
        *(("clear", 1),
          ("manualSwitchToWork", 2),
          ("manualSwitchToProt", 3),
          ("forceSwitchToWork", 4),
          ("forceSwitchToProt", 5),
          ("lockout", 6))
    )


_AdGenMuxPProtGroupSwitchCommands_Type.__name__ = "Integer32"
_AdGenMuxPProtGroupSwitchCommands_Object = MibTableColumn
adGenMuxPProtGroupSwitchCommands = _AdGenMuxPProtGroupSwitchCommands_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 3, 1, 1, 10),
    _AdGenMuxPProtGroupSwitchCommands_Type()
)
adGenMuxPProtGroupSwitchCommands.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenMuxPProtGroupSwitchCommands.setStatus("current")


class _AdGenMuxPProtGroupWorkEntityStatus_Type(Integer32):
    """Custom type adGenMuxPProtGroupWorkEntityStatus based on Integer32"""
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
        *(("clear", 1),
          ("signalFaulty", 2),
          ("signalDegraded", 3),
          ("down", 4))
    )


_AdGenMuxPProtGroupWorkEntityStatus_Type.__name__ = "Integer32"
_AdGenMuxPProtGroupWorkEntityStatus_Object = MibTableColumn
adGenMuxPProtGroupWorkEntityStatus = _AdGenMuxPProtGroupWorkEntityStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 3, 1, 1, 11),
    _AdGenMuxPProtGroupWorkEntityStatus_Type()
)
adGenMuxPProtGroupWorkEntityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMuxPProtGroupWorkEntityStatus.setStatus("current")


class _AdGenMuxPProtGroupProtectEntityStatus_Type(Integer32):
    """Custom type adGenMuxPProtGroupProtectEntityStatus based on Integer32"""
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
        *(("clear", 1),
          ("signalFaulty", 2),
          ("signalDegraded", 3),
          ("down", 4))
    )


_AdGenMuxPProtGroupProtectEntityStatus_Type.__name__ = "Integer32"
_AdGenMuxPProtGroupProtectEntityStatus_Object = MibTableColumn
adGenMuxPProtGroupProtectEntityStatus = _AdGenMuxPProtGroupProtectEntityStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 3, 1, 1, 12),
    _AdGenMuxPProtGroupProtectEntityStatus_Type()
)
adGenMuxPProtGroupProtectEntityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMuxPProtGroupProtectEntityStatus.setStatus("current")
_AdGenMuxPProtGroupRevertiveEnable_Type = TruthValue
_AdGenMuxPProtGroupRevertiveEnable_Object = MibTableColumn
adGenMuxPProtGroupRevertiveEnable = _AdGenMuxPProtGroupRevertiveEnable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 3, 1, 1, 13),
    _AdGenMuxPProtGroupRevertiveEnable_Type()
)
adGenMuxPProtGroupRevertiveEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenMuxPProtGroupRevertiveEnable.setStatus("current")


class _AdGenMuxPProtGroupWaitToRestoreTime_Type(Integer32):
    """Custom type adGenMuxPProtGroupWaitToRestoreTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_AdGenMuxPProtGroupWaitToRestoreTime_Type.__name__ = "Integer32"
_AdGenMuxPProtGroupWaitToRestoreTime_Object = MibTableColumn
adGenMuxPProtGroupWaitToRestoreTime = _AdGenMuxPProtGroupWaitToRestoreTime_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 3, 1, 1, 14),
    _AdGenMuxPProtGroupWaitToRestoreTime_Type()
)
adGenMuxPProtGroupWaitToRestoreTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenMuxPProtGroupWaitToRestoreTime.setStatus("current")


class _AdGenMuxPProtGroupTxK1Request_Type(Integer32):
    """Custom type adGenMuxPProtGroupTxK1Request based on Integer32"""
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
              12)
        )
    )
    namedValues = NamedValues(
        *(("notAvailable", 1),
          ("noRequest", 2),
          ("doNotRevert", 3),
          ("reverseRequest", 4),
          ("waitToRestore", 5),
          ("manualSwitch", 6),
          ("signalDegrade", 7),
          ("signalFail", 8),
          ("forceSwitch", 9),
          ("lockout", 10),
          ("reserved", 11),
          ("notSupported", 12))
    )


_AdGenMuxPProtGroupTxK1Request_Type.__name__ = "Integer32"
_AdGenMuxPProtGroupTxK1Request_Object = MibTableColumn
adGenMuxPProtGroupTxK1Request = _AdGenMuxPProtGroupTxK1Request_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 3, 1, 1, 15),
    _AdGenMuxPProtGroupTxK1Request_Type()
)
adGenMuxPProtGroupTxK1Request.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMuxPProtGroupTxK1Request.setStatus("current")


class _AdGenMuxPProtGroupTxK1RequestChannel_Type(Integer32):
    """Custom type adGenMuxPProtGroupTxK1RequestChannel based on Integer32"""
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
        *(("notAvailable", 1),
          ("protect", 2),
          ("working", 3),
          ("invalid", 4))
    )


_AdGenMuxPProtGroupTxK1RequestChannel_Type.__name__ = "Integer32"
_AdGenMuxPProtGroupTxK1RequestChannel_Object = MibTableColumn
adGenMuxPProtGroupTxK1RequestChannel = _AdGenMuxPProtGroupTxK1RequestChannel_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 3, 1, 1, 16),
    _AdGenMuxPProtGroupTxK1RequestChannel_Type()
)
adGenMuxPProtGroupTxK1RequestChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMuxPProtGroupTxK1RequestChannel.setStatus("current")


class _AdGenMuxPProtGroupTxK2BridgeChannel_Type(Integer32):
    """Custom type adGenMuxPProtGroupTxK2BridgeChannel based on Integer32"""
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
        *(("notAvailable", 1),
          ("protect", 2),
          ("working", 3),
          ("invalid", 4))
    )


_AdGenMuxPProtGroupTxK2BridgeChannel_Type.__name__ = "Integer32"
_AdGenMuxPProtGroupTxK2BridgeChannel_Object = MibTableColumn
adGenMuxPProtGroupTxK2BridgeChannel = _AdGenMuxPProtGroupTxK2BridgeChannel_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 3, 1, 1, 17),
    _AdGenMuxPProtGroupTxK2BridgeChannel_Type()
)
adGenMuxPProtGroupTxK2BridgeChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMuxPProtGroupTxK2BridgeChannel.setStatus("current")


class _AdGenMuxPProtGroupTxK2APSArchitecture_Type(Integer32):
    """Custom type adGenMuxPProtGroupTxK2APSArchitecture based on Integer32"""
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
        *(("notAvailable", 1),
          ("notProtected", 2),
          ("onePlusOne", 3),
          ("oneToOne", 4))
    )


_AdGenMuxPProtGroupTxK2APSArchitecture_Type.__name__ = "Integer32"
_AdGenMuxPProtGroupTxK2APSArchitecture_Object = MibTableColumn
adGenMuxPProtGroupTxK2APSArchitecture = _AdGenMuxPProtGroupTxK2APSArchitecture_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 3, 1, 1, 18),
    _AdGenMuxPProtGroupTxK2APSArchitecture_Type()
)
adGenMuxPProtGroupTxK2APSArchitecture.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMuxPProtGroupTxK2APSArchitecture.setStatus("current")


class _AdGenMuxPProtGroupTxK2APSMode_Type(Integer32):
    """Custom type adGenMuxPProtGroupTxK2APSMode based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("notAvailable", 1),
          ("unidirectional", 2),
          ("bidirectional", 3),
          ("aisL", 4),
          ("rdiL", 5),
          ("msAis", 6),
          ("msRdi", 7),
          ("reserved", 8))
    )


_AdGenMuxPProtGroupTxK2APSMode_Type.__name__ = "Integer32"
_AdGenMuxPProtGroupTxK2APSMode_Object = MibTableColumn
adGenMuxPProtGroupTxK2APSMode = _AdGenMuxPProtGroupTxK2APSMode_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 3, 1, 1, 19),
    _AdGenMuxPProtGroupTxK2APSMode_Type()
)
adGenMuxPProtGroupTxK2APSMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMuxPProtGroupTxK2APSMode.setStatus("current")


class _AdGenMuxPProtGroupRxK1Request_Type(Integer32):
    """Custom type adGenMuxPProtGroupRxK1Request based on Integer32"""
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
              12)
        )
    )
    namedValues = NamedValues(
        *(("notAvailable", 1),
          ("noRequest", 2),
          ("doNotRevert", 3),
          ("reverseRequest", 4),
          ("waitToRestore", 5),
          ("manualSwitch", 6),
          ("signalDegrade", 7),
          ("signalFail", 8),
          ("forceSwitch", 9),
          ("lockout", 10),
          ("reserved", 11),
          ("notSupported", 12))
    )


_AdGenMuxPProtGroupRxK1Request_Type.__name__ = "Integer32"
_AdGenMuxPProtGroupRxK1Request_Object = MibTableColumn
adGenMuxPProtGroupRxK1Request = _AdGenMuxPProtGroupRxK1Request_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 3, 1, 1, 20),
    _AdGenMuxPProtGroupRxK1Request_Type()
)
adGenMuxPProtGroupRxK1Request.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMuxPProtGroupRxK1Request.setStatus("current")


class _AdGenMuxPProtGroupRxK1RequestChannel_Type(Integer32):
    """Custom type adGenMuxPProtGroupRxK1RequestChannel based on Integer32"""
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
        *(("notAvailable", 1),
          ("protect", 2),
          ("working", 3),
          ("invalid", 4))
    )


_AdGenMuxPProtGroupRxK1RequestChannel_Type.__name__ = "Integer32"
_AdGenMuxPProtGroupRxK1RequestChannel_Object = MibTableColumn
adGenMuxPProtGroupRxK1RequestChannel = _AdGenMuxPProtGroupRxK1RequestChannel_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 3, 1, 1, 21),
    _AdGenMuxPProtGroupRxK1RequestChannel_Type()
)
adGenMuxPProtGroupRxK1RequestChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMuxPProtGroupRxK1RequestChannel.setStatus("current")


class _AdGenMuxPProtGroupRxK2BridgeChannel_Type(Integer32):
    """Custom type adGenMuxPProtGroupRxK2BridgeChannel based on Integer32"""
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
        *(("notAvailable", 1),
          ("protect", 2),
          ("working", 3),
          ("invalid", 4))
    )


_AdGenMuxPProtGroupRxK2BridgeChannel_Type.__name__ = "Integer32"
_AdGenMuxPProtGroupRxK2BridgeChannel_Object = MibTableColumn
adGenMuxPProtGroupRxK2BridgeChannel = _AdGenMuxPProtGroupRxK2BridgeChannel_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 3, 1, 1, 22),
    _AdGenMuxPProtGroupRxK2BridgeChannel_Type()
)
adGenMuxPProtGroupRxK2BridgeChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMuxPProtGroupRxK2BridgeChannel.setStatus("current")


class _AdGenMuxPProtGroupRxK2APSArchitecture_Type(Integer32):
    """Custom type adGenMuxPProtGroupRxK2APSArchitecture based on Integer32"""
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
        *(("notAvailable", 1),
          ("notProtected", 2),
          ("onePlusOne", 3),
          ("oneToOne", 4))
    )


_AdGenMuxPProtGroupRxK2APSArchitecture_Type.__name__ = "Integer32"
_AdGenMuxPProtGroupRxK2APSArchitecture_Object = MibTableColumn
adGenMuxPProtGroupRxK2APSArchitecture = _AdGenMuxPProtGroupRxK2APSArchitecture_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 3, 1, 1, 23),
    _AdGenMuxPProtGroupRxK2APSArchitecture_Type()
)
adGenMuxPProtGroupRxK2APSArchitecture.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMuxPProtGroupRxK2APSArchitecture.setStatus("current")


class _AdGenMuxPProtGroupRxK2APSMode_Type(Integer32):
    """Custom type adGenMuxPProtGroupRxK2APSMode based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("notAvailable", 1),
          ("unidirectional", 2),
          ("bidirectional", 3),
          ("aisL", 4),
          ("rdiL", 5),
          ("msAis", 6),
          ("msRdi", 7),
          ("reserved", 8))
    )


_AdGenMuxPProtGroupRxK2APSMode_Type.__name__ = "Integer32"
_AdGenMuxPProtGroupRxK2APSMode_Object = MibTableColumn
adGenMuxPProtGroupRxK2APSMode = _AdGenMuxPProtGroupRxK2APSMode_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 3, 1, 1, 24),
    _AdGenMuxPProtGroupRxK2APSMode_Type()
)
adGenMuxPProtGroupRxK2APSMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMuxPProtGroupRxK2APSMode.setStatus("current")


class _AdGenMuxPProtGroupOperStatus_Type(Integer32):
    """Custom type adGenMuxPProtGroupOperStatus based on Integer32"""
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


_AdGenMuxPProtGroupOperStatus_Type.__name__ = "Integer32"
_AdGenMuxPProtGroupOperStatus_Object = MibTableColumn
adGenMuxPProtGroupOperStatus = _AdGenMuxPProtGroupOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 3, 1, 1, 25),
    _AdGenMuxPProtGroupOperStatus_Type()
)
adGenMuxPProtGroupOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMuxPProtGroupOperStatus.setStatus("current")
_AdGenMuxPProtGroupStatusString_Type = DisplayString
_AdGenMuxPProtGroupStatusString_Object = MibTableColumn
adGenMuxPProtGroupStatusString = _AdGenMuxPProtGroupStatusString_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 3, 1, 1, 26),
    _AdGenMuxPProtGroupStatusString_Type()
)
adGenMuxPProtGroupStatusString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMuxPProtGroupStatusString.setStatus("current")


class _AdGenMuxPProtGroupWaitToRestoreRemainingTime_Type(Unsigned32):
    """Custom type adGenMuxPProtGroupWaitToRestoreRemainingTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1200),
    )


_AdGenMuxPProtGroupWaitToRestoreRemainingTime_Type.__name__ = "Unsigned32"
_AdGenMuxPProtGroupWaitToRestoreRemainingTime_Object = MibTableColumn
adGenMuxPProtGroupWaitToRestoreRemainingTime = _AdGenMuxPProtGroupWaitToRestoreRemainingTime_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 3, 1, 1, 27),
    _AdGenMuxPProtGroupWaitToRestoreRemainingTime_Type()
)
adGenMuxPProtGroupWaitToRestoreRemainingTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMuxPProtGroupWaitToRestoreRemainingTime.setStatus("current")
if mibBuilder.loadTexts:
    adGenMuxPProtGroupWaitToRestoreRemainingTime.setUnits("seconds")
_AdGenMuxPProtGroupLastCreateErrorTable_Object = MibTable
adGenMuxPProtGroupLastCreateErrorTable = _AdGenMuxPProtGroupLastCreateErrorTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 3, 2)
)
if mibBuilder.loadTexts:
    adGenMuxPProtGroupLastCreateErrorTable.setStatus("current")
_AdGenMuxPProtGroupLastCreateErrorEntry_Object = MibTableRow
adGenMuxPProtGroupLastCreateErrorEntry = _AdGenMuxPProtGroupLastCreateErrorEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 3, 2, 1)
)
adGenMuxPProtGroupLastCreateErrorEntry.setIndexNames(
    (0, "ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
)
if mibBuilder.loadTexts:
    adGenMuxPProtGroupLastCreateErrorEntry.setStatus("current")
_AdGenMuxPProtGroupLastCreateError_Type = DisplayString
_AdGenMuxPProtGroupLastCreateError_Object = MibTableColumn
adGenMuxPProtGroupLastCreateError = _AdGenMuxPProtGroupLastCreateError_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 3, 2, 1, 1),
    _AdGenMuxPProtGroupLastCreateError_Type()
)
adGenMuxPProtGroupLastCreateError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMuxPProtGroupLastCreateError.setStatus("current")
_AdGenMuxPEthernetProtGroupTable_Object = MibTable
adGenMuxPEthernetProtGroupTable = _AdGenMuxPEthernetProtGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 3, 3)
)
if mibBuilder.loadTexts:
    adGenMuxPEthernetProtGroupTable.setStatus("current")
_AdGenMuxPEthernetProtGroupEntry_Object = MibTableRow
adGenMuxPEthernetProtGroupEntry = _AdGenMuxPEthernetProtGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 3, 3, 1)
)
adGenMuxPEthernetProtGroupEntry.setIndexNames(
    (0, "ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
    (1, "ADTRAN-GENMUXPONDER-MIB", "adGenMuxPEthernetProtGroupName"),
)
if mibBuilder.loadTexts:
    adGenMuxPEthernetProtGroupEntry.setStatus("current")


class _AdGenMuxPEthernetProtGroupName_Type(DisplayString):
    """Custom type adGenMuxPEthernetProtGroupName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 50),
    )


_AdGenMuxPEthernetProtGroupName_Type.__name__ = "DisplayString"
_AdGenMuxPEthernetProtGroupName_Object = MibTableColumn
adGenMuxPEthernetProtGroupName = _AdGenMuxPEthernetProtGroupName_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 3, 3, 1, 1),
    _AdGenMuxPEthernetProtGroupName_Type()
)
adGenMuxPEthernetProtGroupName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adGenMuxPEthernetProtGroupName.setStatus("current")


class _AdGenMuxPEthernetProtGroupType_Type(Integer32):
    """Custom type adGenMuxPEthernetProtGroupType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("yCable", 1)
    )


_AdGenMuxPEthernetProtGroupType_Type.__name__ = "Integer32"
_AdGenMuxPEthernetProtGroupType_Object = MibTableColumn
adGenMuxPEthernetProtGroupType = _AdGenMuxPEthernetProtGroupType_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 3, 3, 1, 2),
    _AdGenMuxPEthernetProtGroupType_Type()
)
adGenMuxPEthernetProtGroupType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenMuxPEthernetProtGroupType.setStatus("current")
_AdGenMuxPEthernetProtGroupWorkingType_Type = EthernetPayloadTypes
_AdGenMuxPEthernetProtGroupWorkingType_Object = MibTableColumn
adGenMuxPEthernetProtGroupWorkingType = _AdGenMuxPEthernetProtGroupWorkingType_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 3, 3, 1, 3),
    _AdGenMuxPEthernetProtGroupWorkingType_Type()
)
adGenMuxPEthernetProtGroupWorkingType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMuxPEthernetProtGroupWorkingType.setStatus("current")
_AdGenMuxPEthernetProtGroupWorkingIfIndex_Type = InterfaceIndex
_AdGenMuxPEthernetProtGroupWorkingIfIndex_Object = MibTableColumn
adGenMuxPEthernetProtGroupWorkingIfIndex = _AdGenMuxPEthernetProtGroupWorkingIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 3, 3, 1, 4),
    _AdGenMuxPEthernetProtGroupWorkingIfIndex_Type()
)
adGenMuxPEthernetProtGroupWorkingIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenMuxPEthernetProtGroupWorkingIfIndex.setStatus("current")
_AdGenMuxPEthernetProtGroupProtectingType_Type = EthernetPayloadTypes
_AdGenMuxPEthernetProtGroupProtectingType_Object = MibTableColumn
adGenMuxPEthernetProtGroupProtectingType = _AdGenMuxPEthernetProtGroupProtectingType_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 3, 3, 1, 5),
    _AdGenMuxPEthernetProtGroupProtectingType_Type()
)
adGenMuxPEthernetProtGroupProtectingType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMuxPEthernetProtGroupProtectingType.setStatus("current")
_AdGenMuxPEthernetProtGroupProtectingIfIndex_Type = InterfaceIndex
_AdGenMuxPEthernetProtGroupProtectingIfIndex_Object = MibTableColumn
adGenMuxPEthernetProtGroupProtectingIfIndex = _AdGenMuxPEthernetProtGroupProtectingIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 3, 3, 1, 6),
    _AdGenMuxPEthernetProtGroupProtectingIfIndex_Type()
)
adGenMuxPEthernetProtGroupProtectingIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenMuxPEthernetProtGroupProtectingIfIndex.setStatus("current")
_AdGenMuxPEthernetProtGroupRowStatus_Type = RowStatus
_AdGenMuxPEthernetProtGroupRowStatus_Object = MibTableColumn
adGenMuxPEthernetProtGroupRowStatus = _AdGenMuxPEthernetProtGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 3, 3, 1, 7),
    _AdGenMuxPEthernetProtGroupRowStatus_Type()
)
adGenMuxPEthernetProtGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenMuxPEthernetProtGroupRowStatus.setStatus("current")
_AdGenMuxPEthernetProtGroupLastProvError_Type = DisplayString
_AdGenMuxPEthernetProtGroupLastProvError_Object = MibTableColumn
adGenMuxPEthernetProtGroupLastProvError = _AdGenMuxPEthernetProtGroupLastProvError_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 3, 3, 1, 8),
    _AdGenMuxPEthernetProtGroupLastProvError_Type()
)
adGenMuxPEthernetProtGroupLastProvError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMuxPEthernetProtGroupLastProvError.setStatus("current")


class _AdGenMuxPEthernetProtGroupOperStatus_Type(Integer32):
    """Custom type adGenMuxPEthernetProtGroupOperStatus based on Integer32"""
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


_AdGenMuxPEthernetProtGroupOperStatus_Type.__name__ = "Integer32"
_AdGenMuxPEthernetProtGroupOperStatus_Object = MibTableColumn
adGenMuxPEthernetProtGroupOperStatus = _AdGenMuxPEthernetProtGroupOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 3, 3, 1, 9),
    _AdGenMuxPEthernetProtGroupOperStatus_Type()
)
adGenMuxPEthernetProtGroupOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMuxPEthernetProtGroupOperStatus.setStatus("current")
_AdGenMuxPEthernetProtGroupStatusString_Type = DisplayString
_AdGenMuxPEthernetProtGroupStatusString_Object = MibTableColumn
adGenMuxPEthernetProtGroupStatusString = _AdGenMuxPEthernetProtGroupStatusString_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 3, 3, 1, 10),
    _AdGenMuxPEthernetProtGroupStatusString_Type()
)
adGenMuxPEthernetProtGroupStatusString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMuxPEthernetProtGroupStatusString.setStatus("current")
_AdGenMuxPEthernetProtGroupWorkIsOnline_Type = TruthValue
_AdGenMuxPEthernetProtGroupWorkIsOnline_Object = MibTableColumn
adGenMuxPEthernetProtGroupWorkIsOnline = _AdGenMuxPEthernetProtGroupWorkIsOnline_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 3, 3, 1, 11),
    _AdGenMuxPEthernetProtGroupWorkIsOnline_Type()
)
adGenMuxPEthernetProtGroupWorkIsOnline.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMuxPEthernetProtGroupWorkIsOnline.setStatus("current")


class _AdGenMuxPEthernetProtGroupSwitchCommands_Type(Integer32):
    """Custom type adGenMuxPEthernetProtGroupSwitchCommands based on Integer32"""
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
        *(("clear", 1),
          ("manualSwitchToWork", 2),
          ("manualSwitchToProt", 3),
          ("forceSwitchToWork", 4),
          ("forceSwitchToProt", 5),
          ("lockout", 6))
    )


_AdGenMuxPEthernetProtGroupSwitchCommands_Type.__name__ = "Integer32"
_AdGenMuxPEthernetProtGroupSwitchCommands_Object = MibTableColumn
adGenMuxPEthernetProtGroupSwitchCommands = _AdGenMuxPEthernetProtGroupSwitchCommands_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 3, 3, 1, 12),
    _AdGenMuxPEthernetProtGroupSwitchCommands_Type()
)
adGenMuxPEthernetProtGroupSwitchCommands.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenMuxPEthernetProtGroupSwitchCommands.setStatus("current")


class _AdGenMuxPEthernetProtGroupWorkEntityStatus_Type(Integer32):
    """Custom type adGenMuxPEthernetProtGroupWorkEntityStatus based on Integer32"""
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
        *(("clear", 1),
          ("signalFaulty", 2),
          ("signalDegraded", 3),
          ("down", 4))
    )


_AdGenMuxPEthernetProtGroupWorkEntityStatus_Type.__name__ = "Integer32"
_AdGenMuxPEthernetProtGroupWorkEntityStatus_Object = MibTableColumn
adGenMuxPEthernetProtGroupWorkEntityStatus = _AdGenMuxPEthernetProtGroupWorkEntityStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 3, 3, 1, 13),
    _AdGenMuxPEthernetProtGroupWorkEntityStatus_Type()
)
adGenMuxPEthernetProtGroupWorkEntityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMuxPEthernetProtGroupWorkEntityStatus.setStatus("current")


class _AdGenMuxPEthernetProtGroupProtectEntityStatus_Type(Integer32):
    """Custom type adGenMuxPEthernetProtGroupProtectEntityStatus based on Integer32"""
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
        *(("clear", 1),
          ("signalFaulty", 2),
          ("signalDegraded", 3),
          ("down", 4))
    )


_AdGenMuxPEthernetProtGroupProtectEntityStatus_Type.__name__ = "Integer32"
_AdGenMuxPEthernetProtGroupProtectEntityStatus_Object = MibTableColumn
adGenMuxPEthernetProtGroupProtectEntityStatus = _AdGenMuxPEthernetProtGroupProtectEntityStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 3, 3, 1, 14),
    _AdGenMuxPEthernetProtGroupProtectEntityStatus_Type()
)
adGenMuxPEthernetProtGroupProtectEntityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMuxPEthernetProtGroupProtectEntityStatus.setStatus("current")
_AdGenMuxPEthernetProtGroupRevertiveEnable_Type = TruthValue
_AdGenMuxPEthernetProtGroupRevertiveEnable_Object = MibTableColumn
adGenMuxPEthernetProtGroupRevertiveEnable = _AdGenMuxPEthernetProtGroupRevertiveEnable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 3, 3, 1, 15),
    _AdGenMuxPEthernetProtGroupRevertiveEnable_Type()
)
adGenMuxPEthernetProtGroupRevertiveEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenMuxPEthernetProtGroupRevertiveEnable.setStatus("current")


class _AdGenMuxPEthernetProtGroupWaitToRestoreTime_Type(Integer32):
    """Custom type adGenMuxPEthernetProtGroupWaitToRestoreTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_AdGenMuxPEthernetProtGroupWaitToRestoreTime_Type.__name__ = "Integer32"
_AdGenMuxPEthernetProtGroupWaitToRestoreTime_Object = MibTableColumn
adGenMuxPEthernetProtGroupWaitToRestoreTime = _AdGenMuxPEthernetProtGroupWaitToRestoreTime_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 3, 3, 1, 16),
    _AdGenMuxPEthernetProtGroupWaitToRestoreTime_Type()
)
adGenMuxPEthernetProtGroupWaitToRestoreTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenMuxPEthernetProtGroupWaitToRestoreTime.setStatus("current")


class _AdGenMuxPEthernetProtGroupWaitToRestoreRemainingTime_Type(Unsigned32):
    """Custom type adGenMuxPEthernetProtGroupWaitToRestoreRemainingTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1200),
    )


_AdGenMuxPEthernetProtGroupWaitToRestoreRemainingTime_Type.__name__ = "Unsigned32"
_AdGenMuxPEthernetProtGroupWaitToRestoreRemainingTime_Object = MibTableColumn
adGenMuxPEthernetProtGroupWaitToRestoreRemainingTime = _AdGenMuxPEthernetProtGroupWaitToRestoreRemainingTime_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 3, 3, 1, 17),
    _AdGenMuxPEthernetProtGroupWaitToRestoreRemainingTime_Type()
)
adGenMuxPEthernetProtGroupWaitToRestoreRemainingTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMuxPEthernetProtGroupWaitToRestoreRemainingTime.setStatus("current")
if mibBuilder.loadTexts:
    adGenMuxPEthernetProtGroupWaitToRestoreRemainingTime.setUnits("seconds")
_AdGenMuxPEthernetProtGroupLastCreateErrorTable_Object = MibTable
adGenMuxPEthernetProtGroupLastCreateErrorTable = _AdGenMuxPEthernetProtGroupLastCreateErrorTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 3, 4)
)
if mibBuilder.loadTexts:
    adGenMuxPEthernetProtGroupLastCreateErrorTable.setStatus("current")
_AdGenMuxPEthernetProtGroupLastCreateErrorEntry_Object = MibTableRow
adGenMuxPEthernetProtGroupLastCreateErrorEntry = _AdGenMuxPEthernetProtGroupLastCreateErrorEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 3, 4, 1)
)
adGenMuxPEthernetProtGroupLastCreateErrorEntry.setIndexNames(
    (0, "ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
)
if mibBuilder.loadTexts:
    adGenMuxPEthernetProtGroupLastCreateErrorEntry.setStatus("current")
_AdGenMuxPEthernetProtGroupLastCreateError_Type = DisplayString
_AdGenMuxPEthernetProtGroupLastCreateError_Object = MibTableColumn
adGenMuxPEthernetProtGroupLastCreateError = _AdGenMuxPEthernetProtGroupLastCreateError_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 3, 4, 1, 1),
    _AdGenMuxPEthernetProtGroupLastCreateError_Type()
)
adGenMuxPEthernetProtGroupLastCreateError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMuxPEthernetProtGroupLastCreateError.setStatus("current")
_AdGenMuxPLagGroupProv_ObjectIdentity = ObjectIdentity
adGenMuxPLagGroupProv = _AdGenMuxPLagGroupProv_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 4)
)
_AdGenMuxPLagGroupTable_Object = MibTable
adGenMuxPLagGroupTable = _AdGenMuxPLagGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 4, 1)
)
if mibBuilder.loadTexts:
    adGenMuxPLagGroupTable.setStatus("current")
_AdGenMuxPLagGroupEntry_Object = MibTableRow
adGenMuxPLagGroupEntry = _AdGenMuxPLagGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 4, 1, 1)
)
adGenMuxPLagGroupEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adGenMuxPLagGroupEntry.setStatus("current")
_AdGenMuxPLagGroupRowStatus_Type = RowStatus
_AdGenMuxPLagGroupRowStatus_Object = MibTableColumn
adGenMuxPLagGroupRowStatus = _AdGenMuxPLagGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 4, 1, 1, 1),
    _AdGenMuxPLagGroupRowStatus_Type()
)
adGenMuxPLagGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenMuxPLagGroupRowStatus.setStatus("current")


class _AdGenMuxPLagGroupOperStatus_Type(Integer32):
    """Custom type adGenMuxPLagGroupOperStatus based on Integer32"""
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


_AdGenMuxPLagGroupOperStatus_Type.__name__ = "Integer32"
_AdGenMuxPLagGroupOperStatus_Object = MibTableColumn
adGenMuxPLagGroupOperStatus = _AdGenMuxPLagGroupOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 4, 1, 1, 2),
    _AdGenMuxPLagGroupOperStatus_Type()
)
adGenMuxPLagGroupOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMuxPLagGroupOperStatus.setStatus("current")
_AdGenMuxPLagGroupNumber_Type = Integer32
_AdGenMuxPLagGroupNumber_Object = MibTableColumn
adGenMuxPLagGroupNumber = _AdGenMuxPLagGroupNumber_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 4, 1, 1, 3),
    _AdGenMuxPLagGroupNumber_Type()
)
adGenMuxPLagGroupNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMuxPLagGroupNumber.setStatus("current")


class _AdGenMuxPLagGroupName_Type(DisplayString):
    """Custom type adGenMuxPLagGroupName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 50),
    )


_AdGenMuxPLagGroupName_Type.__name__ = "DisplayString"
_AdGenMuxPLagGroupName_Object = MibTableColumn
adGenMuxPLagGroupName = _AdGenMuxPLagGroupName_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 4, 1, 1, 4),
    _AdGenMuxPLagGroupName_Type()
)
adGenMuxPLagGroupName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenMuxPLagGroupName.setStatus("current")
_AdGenMuxPLagGroupMaxNumCfgLinks_Type = Integer32
_AdGenMuxPLagGroupMaxNumCfgLinks_Object = MibTableColumn
adGenMuxPLagGroupMaxNumCfgLinks = _AdGenMuxPLagGroupMaxNumCfgLinks_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 4, 1, 1, 5),
    _AdGenMuxPLagGroupMaxNumCfgLinks_Type()
)
adGenMuxPLagGroupMaxNumCfgLinks.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenMuxPLagGroupMaxNumCfgLinks.setStatus("current")
_AdGenMuxPLagGroupNumCfgLinks_Type = Integer32
_AdGenMuxPLagGroupNumCfgLinks_Object = MibTableColumn
adGenMuxPLagGroupNumCfgLinks = _AdGenMuxPLagGroupNumCfgLinks_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 4, 1, 1, 6),
    _AdGenMuxPLagGroupNumCfgLinks_Type()
)
adGenMuxPLagGroupNumCfgLinks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMuxPLagGroupNumCfgLinks.setStatus("current")
_AdGenMuxPLagGroupMinNumActLinks_Type = Integer32
_AdGenMuxPLagGroupMinNumActLinks_Object = MibTableColumn
adGenMuxPLagGroupMinNumActLinks = _AdGenMuxPLagGroupMinNumActLinks_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 4, 1, 1, 7),
    _AdGenMuxPLagGroupMinNumActLinks_Type()
)
adGenMuxPLagGroupMinNumActLinks.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenMuxPLagGroupMinNumActLinks.setStatus("current")
_AdGenMuxPLagGroupNumActLinks_Type = Integer32
_AdGenMuxPLagGroupNumActLinks_Object = MibTableColumn
adGenMuxPLagGroupNumActLinks = _AdGenMuxPLagGroupNumActLinks_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 4, 1, 1, 8),
    _AdGenMuxPLagGroupNumActLinks_Type()
)
adGenMuxPLagGroupNumActLinks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMuxPLagGroupNumActLinks.setStatus("current")
_AdGenMuxPLagGroupLastChange_Type = TimeTicks
_AdGenMuxPLagGroupLastChange_Object = MibTableColumn
adGenMuxPLagGroupLastChange = _AdGenMuxPLagGroupLastChange_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 4, 1, 1, 9),
    _AdGenMuxPLagGroupLastChange_Type()
)
adGenMuxPLagGroupLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMuxPLagGroupLastChange.setStatus("current")
_AdGenMuxPLagGroupLastError_Type = DisplayString
_AdGenMuxPLagGroupLastError_Object = MibTableColumn
adGenMuxPLagGroupLastError = _AdGenMuxPLagGroupLastError_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 4, 1, 1, 10),
    _AdGenMuxPLagGroupLastError_Type()
)
adGenMuxPLagGroupLastError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMuxPLagGroupLastError.setStatus("current")


class _AdGenMuxPLagGroupMinActLinkAlarmEnable_Type(TruthValue):
    """Custom type adGenMuxPLagGroupMinActLinkAlarmEnable based on TruthValue"""
    defaultValue = 1


_AdGenMuxPLagGroupMinActLinkAlarmEnable_Type.__name__ = "TruthValue"
_AdGenMuxPLagGroupMinActLinkAlarmEnable_Object = MibTableColumn
adGenMuxPLagGroupMinActLinkAlarmEnable = _AdGenMuxPLagGroupMinActLinkAlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 4, 1, 1, 11),
    _AdGenMuxPLagGroupMinActLinkAlarmEnable_Type()
)
adGenMuxPLagGroupMinActLinkAlarmEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenMuxPLagGroupMinActLinkAlarmEnable.setStatus("current")
_AdGenMuxPLagGroupLastCreateErrorTable_Object = MibTable
adGenMuxPLagGroupLastCreateErrorTable = _AdGenMuxPLagGroupLastCreateErrorTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 4, 2)
)
if mibBuilder.loadTexts:
    adGenMuxPLagGroupLastCreateErrorTable.setStatus("current")
_AdGenMuxPLagGroupLastCreateErrorEntry_Object = MibTableRow
adGenMuxPLagGroupLastCreateErrorEntry = _AdGenMuxPLagGroupLastCreateErrorEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 4, 2, 1)
)
adGenMuxPLagGroupLastCreateErrorEntry.setIndexNames(
    (0, "ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
)
if mibBuilder.loadTexts:
    adGenMuxPLagGroupLastCreateErrorEntry.setStatus("current")
_AdGenMuxPLagGroupLastCreateError_Type = DisplayString
_AdGenMuxPLagGroupLastCreateError_Object = MibTableColumn
adGenMuxPLagGroupLastCreateError = _AdGenMuxPLagGroupLastCreateError_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 4, 2, 1, 1),
    _AdGenMuxPLagGroupLastCreateError_Type()
)
adGenMuxPLagGroupLastCreateError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMuxPLagGroupLastCreateError.setStatus("current")
_AdGenMuxPLagPortMapTable_Object = MibTable
adGenMuxPLagPortMapTable = _AdGenMuxPLagPortMapTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 4, 3)
)
if mibBuilder.loadTexts:
    adGenMuxPLagPortMapTable.setStatus("current")
_AdGenMuxPLagPortMapEntry_Object = MibTableRow
adGenMuxPLagPortMapEntry = _AdGenMuxPLagPortMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 4, 3, 1)
)
adGenMuxPLagPortMapEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ADTRAN-GENMUXPONDER-MIB", "adGenMuxPLagPortMapPort"),
)
if mibBuilder.loadTexts:
    adGenMuxPLagPortMapEntry.setStatus("current")
_AdGenMuxPLagPortMapPort_Type = InterfaceIndex
_AdGenMuxPLagPortMapPort_Object = MibTableColumn
adGenMuxPLagPortMapPort = _AdGenMuxPLagPortMapPort_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 4, 3, 1, 1),
    _AdGenMuxPLagPortMapPort_Type()
)
adGenMuxPLagPortMapPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adGenMuxPLagPortMapPort.setStatus("current")
_AdGenMuxPLagPortMapRowStatus_Type = RowStatus
_AdGenMuxPLagPortMapRowStatus_Object = MibTableColumn
adGenMuxPLagPortMapRowStatus = _AdGenMuxPLagPortMapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 4, 3, 1, 2),
    _AdGenMuxPLagPortMapRowStatus_Type()
)
adGenMuxPLagPortMapRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenMuxPLagPortMapRowStatus.setStatus("current")


class _AdGenMuxPLagPortMapOperStatus_Type(Integer32):
    """Custom type adGenMuxPLagPortMapOperStatus based on Integer32"""
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


_AdGenMuxPLagPortMapOperStatus_Type.__name__ = "Integer32"
_AdGenMuxPLagPortMapOperStatus_Object = MibTableColumn
adGenMuxPLagPortMapOperStatus = _AdGenMuxPLagPortMapOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 4, 3, 1, 3),
    _AdGenMuxPLagPortMapOperStatus_Type()
)
adGenMuxPLagPortMapOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMuxPLagPortMapOperStatus.setStatus("current")
_AdGenMuxPLagPortMapLagNumber_Type = Integer32
_AdGenMuxPLagPortMapLagNumber_Object = MibTableColumn
adGenMuxPLagPortMapLagNumber = _AdGenMuxPLagPortMapLagNumber_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 4, 3, 1, 4),
    _AdGenMuxPLagPortMapLagNumber_Type()
)
adGenMuxPLagPortMapLagNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMuxPLagPortMapLagNumber.setStatus("current")
_AdGenMuxPLagPortMapPortNumber_Type = Integer32
_AdGenMuxPLagPortMapPortNumber_Object = MibTableColumn
adGenMuxPLagPortMapPortNumber = _AdGenMuxPLagPortMapPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 4, 3, 1, 5),
    _AdGenMuxPLagPortMapPortNumber_Type()
)
adGenMuxPLagPortMapPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMuxPLagPortMapPortNumber.setStatus("current")
_AdGenMuxPLagPortMapLastChange_Type = TimeTicks
_AdGenMuxPLagPortMapLastChange_Object = MibTableColumn
adGenMuxPLagPortMapLastChange = _AdGenMuxPLagPortMapLastChange_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 4, 3, 1, 6),
    _AdGenMuxPLagPortMapLastChange_Type()
)
adGenMuxPLagPortMapLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMuxPLagPortMapLastChange.setStatus("current")
_AdGenMuxPLagPortMapLastError_Type = DisplayString
_AdGenMuxPLagPortMapLastError_Object = MibTableColumn
adGenMuxPLagPortMapLastError = _AdGenMuxPLagPortMapLastError_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 4, 3, 1, 7),
    _AdGenMuxPLagPortMapLastError_Type()
)
adGenMuxPLagPortMapLastError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMuxPLagPortMapLastError.setStatus("current")
_AdGenMuxPLagPortMapLastCreateErrorTable_Object = MibTable
adGenMuxPLagPortMapLastCreateErrorTable = _AdGenMuxPLagPortMapLastCreateErrorTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 4, 4)
)
if mibBuilder.loadTexts:
    adGenMuxPLagPortMapLastCreateErrorTable.setStatus("current")
_AdGenMuxPLagPortMapLastCreateErrorEntry_Object = MibTableRow
adGenMuxPLagPortMapLastCreateErrorEntry = _AdGenMuxPLagPortMapLastCreateErrorEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 4, 4, 1)
)
adGenMuxPLagPortMapLastCreateErrorEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adGenMuxPLagPortMapLastCreateErrorEntry.setStatus("current")
_AdGenMuxPLagPortMapLastCreateError_Type = DisplayString
_AdGenMuxPLagPortMapLastCreateError_Object = MibTableColumn
adGenMuxPLagPortMapLastCreateError = _AdGenMuxPLagPortMapLastCreateError_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 4, 4, 1, 1),
    _AdGenMuxPLagPortMapLastCreateError_Type()
)
adGenMuxPLagPortMapLastCreateError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMuxPLagPortMapLastCreateError.setStatus("current")
_AdGenMuxPLagPortStatusTable_Object = MibTable
adGenMuxPLagPortStatusTable = _AdGenMuxPLagPortStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 4, 5)
)
if mibBuilder.loadTexts:
    adGenMuxPLagPortStatusTable.setStatus("current")
_AdGenMuxPLagPortStatusEntry_Object = MibTableRow
adGenMuxPLagPortStatusEntry = _AdGenMuxPLagPortStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 4, 5, 1)
)
adGenMuxPLagPortStatusEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adGenMuxPLagPortStatusEntry.setStatus("current")
_AdGenMuxPLagPortStatusLagIfIndex_Type = Integer32
_AdGenMuxPLagPortStatusLagIfIndex_Object = MibTableColumn
adGenMuxPLagPortStatusLagIfIndex = _AdGenMuxPLagPortStatusLagIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 4, 5, 1, 1),
    _AdGenMuxPLagPortStatusLagIfIndex_Type()
)
adGenMuxPLagPortStatusLagIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMuxPLagPortStatusLagIfIndex.setStatus("current")


class _AdGenMuxPLagPortStatusOperStatus_Type(Integer32):
    """Custom type adGenMuxPLagPortStatusOperStatus based on Integer32"""
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


_AdGenMuxPLagPortStatusOperStatus_Type.__name__ = "Integer32"
_AdGenMuxPLagPortStatusOperStatus_Object = MibTableColumn
adGenMuxPLagPortStatusOperStatus = _AdGenMuxPLagPortStatusOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 4, 5, 1, 2),
    _AdGenMuxPLagPortStatusOperStatus_Type()
)
adGenMuxPLagPortStatusOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMuxPLagPortStatusOperStatus.setStatus("current")
_AdGenMuxPTiming_ObjectIdentity = ObjectIdentity
adGenMuxPTiming = _AdGenMuxPTiming_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 5)
)
_AdGenMuxPTimingProv_ObjectIdentity = ObjectIdentity
adGenMuxPTimingProv = _AdGenMuxPTimingProv_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 5, 1)
)
_AdGenMuxPTimingProvTable_Object = MibTable
adGenMuxPTimingProvTable = _AdGenMuxPTimingProvTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 5, 1, 1)
)
if mibBuilder.loadTexts:
    adGenMuxPTimingProvTable.setStatus("current")
_AdGenMuxPTimingProvEntry_Object = MibTableRow
adGenMuxPTimingProvEntry = _AdGenMuxPTimingProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 5, 1, 1, 1)
)
adGenMuxPTimingProvEntry.setIndexNames(
    (0, "ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
)
if mibBuilder.loadTexts:
    adGenMuxPTimingProvEntry.setStatus("current")


class _AdGenMuxPTimingPrimarySourceSelection_Type(Integer32):
    """Custom type adGenMuxPTimingPrimarySourceSelection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("system", 1),
          ("interface", 2),
          ("interfaceFixed", 3))
    )


_AdGenMuxPTimingPrimarySourceSelection_Type.__name__ = "Integer32"
_AdGenMuxPTimingPrimarySourceSelection_Object = MibTableColumn
adGenMuxPTimingPrimarySourceSelection = _AdGenMuxPTimingPrimarySourceSelection_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 5, 1, 1, 1, 1),
    _AdGenMuxPTimingPrimarySourceSelection_Type()
)
adGenMuxPTimingPrimarySourceSelection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenMuxPTimingPrimarySourceSelection.setStatus("current")
_AdGenMuxPTimingPrimarySourceInterface_Type = InterfaceIndexOrZero
_AdGenMuxPTimingPrimarySourceInterface_Object = MibTableColumn
adGenMuxPTimingPrimarySourceInterface = _AdGenMuxPTimingPrimarySourceInterface_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 5, 1, 1, 1, 2),
    _AdGenMuxPTimingPrimarySourceInterface_Type()
)
adGenMuxPTimingPrimarySourceInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenMuxPTimingPrimarySourceInterface.setStatus("current")


class _AdGenMuxPTimingSecondarySourceSelection_Type(Integer32):
    """Custom type adGenMuxPTimingSecondarySourceSelection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("system", 1),
          ("interface", 2),
          ("interfaceFixed", 3))
    )


_AdGenMuxPTimingSecondarySourceSelection_Type.__name__ = "Integer32"
_AdGenMuxPTimingSecondarySourceSelection_Object = MibTableColumn
adGenMuxPTimingSecondarySourceSelection = _AdGenMuxPTimingSecondarySourceSelection_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 5, 1, 1, 1, 3),
    _AdGenMuxPTimingSecondarySourceSelection_Type()
)
adGenMuxPTimingSecondarySourceSelection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenMuxPTimingSecondarySourceSelection.setStatus("current")
_AdGenMuxPTimingSecondarySourceInterface_Type = InterfaceIndexOrZero
_AdGenMuxPTimingSecondarySourceInterface_Object = MibTableColumn
adGenMuxPTimingSecondarySourceInterface = _AdGenMuxPTimingSecondarySourceInterface_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 5, 1, 1, 1, 4),
    _AdGenMuxPTimingSecondarySourceInterface_Type()
)
adGenMuxPTimingSecondarySourceInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenMuxPTimingSecondarySourceInterface.setStatus("current")
_AdGenMuxPTimingAlarmEnablePrimaryFailed_Type = TruthValue
_AdGenMuxPTimingAlarmEnablePrimaryFailed_Object = MibTableColumn
adGenMuxPTimingAlarmEnablePrimaryFailed = _AdGenMuxPTimingAlarmEnablePrimaryFailed_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 5, 1, 1, 1, 5),
    _AdGenMuxPTimingAlarmEnablePrimaryFailed_Type()
)
adGenMuxPTimingAlarmEnablePrimaryFailed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenMuxPTimingAlarmEnablePrimaryFailed.setStatus("current")
_AdGenMuxPTimingAlarmEnableSecondaryFailed_Type = TruthValue
_AdGenMuxPTimingAlarmEnableSecondaryFailed_Object = MibTableColumn
adGenMuxPTimingAlarmEnableSecondaryFailed = _AdGenMuxPTimingAlarmEnableSecondaryFailed_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 5, 1, 1, 1, 6),
    _AdGenMuxPTimingAlarmEnableSecondaryFailed_Type()
)
adGenMuxPTimingAlarmEnableSecondaryFailed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenMuxPTimingAlarmEnableSecondaryFailed.setStatus("current")
_AdGenMuxPTimingAlarmEnableHoldover_Type = TruthValue
_AdGenMuxPTimingAlarmEnableHoldover_Object = MibTableColumn
adGenMuxPTimingAlarmEnableHoldover = _AdGenMuxPTimingAlarmEnableHoldover_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 5, 1, 1, 1, 7),
    _AdGenMuxPTimingAlarmEnableHoldover_Type()
)
adGenMuxPTimingAlarmEnableHoldover.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenMuxPTimingAlarmEnableHoldover.setStatus("current")


class _AdGenMuxPTimingReceiveSSMEnable_Type(Integer32):
    """Custom type adGenMuxPTimingReceiveSSMEnable based on Integer32"""
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


_AdGenMuxPTimingReceiveSSMEnable_Type.__name__ = "Integer32"
_AdGenMuxPTimingReceiveSSMEnable_Object = MibTableColumn
adGenMuxPTimingReceiveSSMEnable = _AdGenMuxPTimingReceiveSSMEnable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 5, 1, 1, 1, 8),
    _AdGenMuxPTimingReceiveSSMEnable_Type()
)
adGenMuxPTimingReceiveSSMEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenMuxPTimingReceiveSSMEnable.setStatus("deprecated")


class _AdGenMuxPTimingForceClockFailover_Type(Integer32):
    """Custom type adGenMuxPTimingForceClockFailover based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("failOver", 1),
          ("notAvailable", 2))
    )


_AdGenMuxPTimingForceClockFailover_Type.__name__ = "Integer32"
_AdGenMuxPTimingForceClockFailover_Object = MibTableColumn
adGenMuxPTimingForceClockFailover = _AdGenMuxPTimingForceClockFailover_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 5, 1, 1, 1, 9),
    _AdGenMuxPTimingForceClockFailover_Type()
)
adGenMuxPTimingForceClockFailover.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenMuxPTimingForceClockFailover.setStatus("current")


class _AdGenMuxPTimingRevertiveSwitchType_Type(Integer32):
    """Custom type adGenMuxPTimingRevertiveSwitchType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ssm", 1),
          ("none", 2))
    )


_AdGenMuxPTimingRevertiveSwitchType_Type.__name__ = "Integer32"
_AdGenMuxPTimingRevertiveSwitchType_Object = MibTableColumn
adGenMuxPTimingRevertiveSwitchType = _AdGenMuxPTimingRevertiveSwitchType_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 5, 1, 1, 1, 10),
    _AdGenMuxPTimingRevertiveSwitchType_Type()
)
adGenMuxPTimingRevertiveSwitchType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenMuxPTimingRevertiveSwitchType.setStatus("current")
_AdGenMuxPTimingLastError_Type = DisplayString
_AdGenMuxPTimingLastError_Object = MibTableColumn
adGenMuxPTimingLastError = _AdGenMuxPTimingLastError_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 5, 1, 1, 1, 11),
    _AdGenMuxPTimingLastError_Type()
)
adGenMuxPTimingLastError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMuxPTimingLastError.setStatus("current")


class _AdGenMuxPTimingSystemTimingType_Type(Integer32):
    """Custom type adGenMuxPTimingSystemTimingType based on Integer32"""
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
        *(("none", 1),
          ("loopA", 2),
          ("loopB", 3))
    )


_AdGenMuxPTimingSystemTimingType_Type.__name__ = "Integer32"
_AdGenMuxPTimingSystemTimingType_Object = MibTableColumn
adGenMuxPTimingSystemTimingType = _AdGenMuxPTimingSystemTimingType_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 5, 1, 1, 1, 12),
    _AdGenMuxPTimingSystemTimingType_Type()
)
adGenMuxPTimingSystemTimingType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenMuxPTimingSystemTimingType.setStatus("current")
_AdGenMuxPTimingProvPortTable_Object = MibTable
adGenMuxPTimingProvPortTable = _AdGenMuxPTimingProvPortTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 5, 1, 2)
)
if mibBuilder.loadTexts:
    adGenMuxPTimingProvPortTable.setStatus("current")
_AdGenMuxPTimingProvPortEntry_Object = MibTableRow
adGenMuxPTimingProvPortEntry = _AdGenMuxPTimingProvPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 5, 1, 2, 1)
)
adGenMuxPTimingProvPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adGenMuxPTimingProvPortEntry.setStatus("current")


class _AdGenMuxPTimingTransmitSSMEnable_Type(Integer32):
    """Custom type adGenMuxPTimingTransmitSSMEnable based on Integer32"""
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


_AdGenMuxPTimingTransmitSSMEnable_Type.__name__ = "Integer32"
_AdGenMuxPTimingTransmitSSMEnable_Object = MibTableColumn
adGenMuxPTimingTransmitSSMEnable = _AdGenMuxPTimingTransmitSSMEnable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 5, 1, 2, 1, 1),
    _AdGenMuxPTimingTransmitSSMEnable_Type()
)
adGenMuxPTimingTransmitSSMEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenMuxPTimingTransmitSSMEnable.setStatus("current")


class _AdGenMuxPTimingEsmcType_Type(Integer32):
    """Custom type adGenMuxPTimingEsmcType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("syncEECOption1", 1),
          ("syncEECOption2", 2))
    )


_AdGenMuxPTimingEsmcType_Type.__name__ = "Integer32"
_AdGenMuxPTimingEsmcType_Object = MibTableColumn
adGenMuxPTimingEsmcType = _AdGenMuxPTimingEsmcType_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 5, 1, 2, 1, 2),
    _AdGenMuxPTimingEsmcType_Type()
)
adGenMuxPTimingEsmcType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenMuxPTimingEsmcType.setStatus("current")
_AdGenMuxPTimingStatus_ObjectIdentity = ObjectIdentity
adGenMuxPTimingStatus = _AdGenMuxPTimingStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 5, 2)
)
_AdGenMuxPTimingStatusTable_Object = MibTable
adGenMuxPTimingStatusTable = _AdGenMuxPTimingStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 5, 2, 1)
)
if mibBuilder.loadTexts:
    adGenMuxPTimingStatusTable.setStatus("current")
_AdGenMuxPTimingStatusEntry_Object = MibTableRow
adGenMuxPTimingStatusEntry = _AdGenMuxPTimingStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 5, 2, 1, 1)
)
adGenMuxPTimingStatusEntry.setIndexNames(
    (0, "ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
)
if mibBuilder.loadTexts:
    adGenMuxPTimingStatusEntry.setStatus("current")


class _AdGenMuxPTimingCurrentSourceType_Type(Integer32):
    """Custom type adGenMuxPTimingCurrentSourceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("primary", 1),
          ("secondary", 2),
          ("internal", 3))
    )


_AdGenMuxPTimingCurrentSourceType_Type.__name__ = "Integer32"
_AdGenMuxPTimingCurrentSourceType_Object = MibTableColumn
adGenMuxPTimingCurrentSourceType = _AdGenMuxPTimingCurrentSourceType_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 5, 2, 1, 1, 1),
    _AdGenMuxPTimingCurrentSourceType_Type()
)
adGenMuxPTimingCurrentSourceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMuxPTimingCurrentSourceType.setStatus("current")


class _AdGenMuxPTimingPrimarySourceHealth_Type(Integer32):
    """Custom type adGenMuxPTimingPrimarySourceHealth based on Integer32"""
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


_AdGenMuxPTimingPrimarySourceHealth_Type.__name__ = "Integer32"
_AdGenMuxPTimingPrimarySourceHealth_Object = MibTableColumn
adGenMuxPTimingPrimarySourceHealth = _AdGenMuxPTimingPrimarySourceHealth_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 5, 2, 1, 1, 2),
    _AdGenMuxPTimingPrimarySourceHealth_Type()
)
adGenMuxPTimingPrimarySourceHealth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMuxPTimingPrimarySourceHealth.setStatus("current")


class _AdGenMuxPTimingSecondarySourceHealth_Type(Integer32):
    """Custom type adGenMuxPTimingSecondarySourceHealth based on Integer32"""
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


_AdGenMuxPTimingSecondarySourceHealth_Type.__name__ = "Integer32"
_AdGenMuxPTimingSecondarySourceHealth_Object = MibTableColumn
adGenMuxPTimingSecondarySourceHealth = _AdGenMuxPTimingSecondarySourceHealth_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 5, 2, 1, 1, 3),
    _AdGenMuxPTimingSecondarySourceHealth_Type()
)
adGenMuxPTimingSecondarySourceHealth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMuxPTimingSecondarySourceHealth.setStatus("current")
_AdGenMuxPTimingPrimarySourceRxSSM_Type = DisplayString
_AdGenMuxPTimingPrimarySourceRxSSM_Object = MibTableColumn
adGenMuxPTimingPrimarySourceRxSSM = _AdGenMuxPTimingPrimarySourceRxSSM_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 5, 2, 1, 1, 4),
    _AdGenMuxPTimingPrimarySourceRxSSM_Type()
)
adGenMuxPTimingPrimarySourceRxSSM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMuxPTimingPrimarySourceRxSSM.setStatus("current")
_AdGenMuxPTimingSecondarySourceRxSSM_Type = DisplayString
_AdGenMuxPTimingSecondarySourceRxSSM_Object = MibTableColumn
adGenMuxPTimingSecondarySourceRxSSM = _AdGenMuxPTimingSecondarySourceRxSSM_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 5, 2, 1, 1, 5),
    _AdGenMuxPTimingSecondarySourceRxSSM_Type()
)
adGenMuxPTimingSecondarySourceRxSSM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMuxPTimingSecondarySourceRxSSM.setStatus("current")
_AdGenMuxPTimingTxSSM1_Type = DisplayString
_AdGenMuxPTimingTxSSM1_Object = MibTableColumn
adGenMuxPTimingTxSSM1 = _AdGenMuxPTimingTxSSM1_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 5, 2, 1, 1, 6),
    _AdGenMuxPTimingTxSSM1_Type()
)
adGenMuxPTimingTxSSM1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMuxPTimingTxSSM1.setStatus("current")
_AdGenMuxPTimingTxSSM2_Type = DisplayString
_AdGenMuxPTimingTxSSM2_Object = MibTableColumn
adGenMuxPTimingTxSSM2 = _AdGenMuxPTimingTxSSM2_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 5, 2, 1, 1, 7),
    _AdGenMuxPTimingTxSSM2_Type()
)
adGenMuxPTimingTxSSM2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMuxPTimingTxSSM2.setStatus("current")
_AdGenMuxPTimingAlarmPrefix_ObjectIdentity = ObjectIdentity
adGenMuxPTimingAlarmPrefix = _AdGenMuxPTimingAlarmPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 5, 3)
)
_AdGenMuxPTimingAlarms_ObjectIdentity = ObjectIdentity
adGenMuxPTimingAlarms = _AdGenMuxPTimingAlarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 5, 3, 0)
)
_AdGenMuxPPhysPeerProv_ObjectIdentity = ObjectIdentity
adGenMuxPPhysPeerProv = _AdGenMuxPPhysPeerProv_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 6)
)
_AdGenMuxPPhysPeerProvTable_Object = MibTable
adGenMuxPPhysPeerProvTable = _AdGenMuxPPhysPeerProvTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 6, 1)
)
if mibBuilder.loadTexts:
    adGenMuxPPhysPeerProvTable.setStatus("deprecated")
_AdGenMuxPPhysPeerProvEntry_Object = MibTableRow
adGenMuxPPhysPeerProvEntry = _AdGenMuxPPhysPeerProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 6, 1, 1)
)
adGenMuxPPhysPeerProvEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adGenMuxPPhysPeerProvEntry.setStatus("deprecated")
_AdGenMuxPPhysPeerOneIpAddressTx_Type = IpAddress
_AdGenMuxPPhysPeerOneIpAddressTx_Object = MibTableColumn
adGenMuxPPhysPeerOneIpAddressTx = _AdGenMuxPPhysPeerOneIpAddressTx_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 6, 1, 1, 1),
    _AdGenMuxPPhysPeerOneIpAddressTx_Type()
)
adGenMuxPPhysPeerOneIpAddressTx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenMuxPPhysPeerOneIpAddressTx.setStatus("deprecated")
_AdGenMuxPPhysPeerOneIpAddressRx_Type = IpAddress
_AdGenMuxPPhysPeerOneIpAddressRx_Object = MibTableColumn
adGenMuxPPhysPeerOneIpAddressRx = _AdGenMuxPPhysPeerOneIpAddressRx_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 6, 1, 1, 2),
    _AdGenMuxPPhysPeerOneIpAddressRx_Type()
)
adGenMuxPPhysPeerOneIpAddressRx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenMuxPPhysPeerOneIpAddressRx.setStatus("deprecated")
_AdGenMuxPPhysPeerOneChassisIdTx_Type = DisplayString
_AdGenMuxPPhysPeerOneChassisIdTx_Object = MibTableColumn
adGenMuxPPhysPeerOneChassisIdTx = _AdGenMuxPPhysPeerOneChassisIdTx_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 6, 1, 1, 3),
    _AdGenMuxPPhysPeerOneChassisIdTx_Type()
)
adGenMuxPPhysPeerOneChassisIdTx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenMuxPPhysPeerOneChassisIdTx.setStatus("deprecated")
_AdGenMuxPPhysPeerOneChassisIdRx_Type = DisplayString
_AdGenMuxPPhysPeerOneChassisIdRx_Object = MibTableColumn
adGenMuxPPhysPeerOneChassisIdRx = _AdGenMuxPPhysPeerOneChassisIdRx_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 6, 1, 1, 4),
    _AdGenMuxPPhysPeerOneChassisIdRx_Type()
)
adGenMuxPPhysPeerOneChassisIdRx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenMuxPPhysPeerOneChassisIdRx.setStatus("deprecated")
_AdGenMuxPPhysPeerOnePortIdTx_Type = DisplayString
_AdGenMuxPPhysPeerOnePortIdTx_Object = MibTableColumn
adGenMuxPPhysPeerOnePortIdTx = _AdGenMuxPPhysPeerOnePortIdTx_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 6, 1, 1, 5),
    _AdGenMuxPPhysPeerOnePortIdTx_Type()
)
adGenMuxPPhysPeerOnePortIdTx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenMuxPPhysPeerOnePortIdTx.setStatus("deprecated")
_AdGenMuxPPhysPeerOnePortIdRx_Type = DisplayString
_AdGenMuxPPhysPeerOnePortIdRx_Object = MibTableColumn
adGenMuxPPhysPeerOnePortIdRx = _AdGenMuxPPhysPeerOnePortIdRx_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 6, 1, 1, 6),
    _AdGenMuxPPhysPeerOnePortIdRx_Type()
)
adGenMuxPPhysPeerOnePortIdRx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenMuxPPhysPeerOnePortIdRx.setStatus("deprecated")
_AdGenMuxPPhysPeerTwoIpAddressTx_Type = IpAddress
_AdGenMuxPPhysPeerTwoIpAddressTx_Object = MibTableColumn
adGenMuxPPhysPeerTwoIpAddressTx = _AdGenMuxPPhysPeerTwoIpAddressTx_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 6, 1, 1, 7),
    _AdGenMuxPPhysPeerTwoIpAddressTx_Type()
)
adGenMuxPPhysPeerTwoIpAddressTx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenMuxPPhysPeerTwoIpAddressTx.setStatus("deprecated")
_AdGenMuxPPhysPeerTwoIpAddressRx_Type = IpAddress
_AdGenMuxPPhysPeerTwoIpAddressRx_Object = MibTableColumn
adGenMuxPPhysPeerTwoIpAddressRx = _AdGenMuxPPhysPeerTwoIpAddressRx_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 6, 1, 1, 8),
    _AdGenMuxPPhysPeerTwoIpAddressRx_Type()
)
adGenMuxPPhysPeerTwoIpAddressRx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenMuxPPhysPeerTwoIpAddressRx.setStatus("deprecated")
_AdGenMuxPPhysPeerTwoChassisIdTx_Type = DisplayString
_AdGenMuxPPhysPeerTwoChassisIdTx_Object = MibTableColumn
adGenMuxPPhysPeerTwoChassisIdTx = _AdGenMuxPPhysPeerTwoChassisIdTx_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 6, 1, 1, 9),
    _AdGenMuxPPhysPeerTwoChassisIdTx_Type()
)
adGenMuxPPhysPeerTwoChassisIdTx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenMuxPPhysPeerTwoChassisIdTx.setStatus("deprecated")
_AdGenMuxPPhysPeerTwoChassisIdRx_Type = DisplayString
_AdGenMuxPPhysPeerTwoChassisIdRx_Object = MibTableColumn
adGenMuxPPhysPeerTwoChassisIdRx = _AdGenMuxPPhysPeerTwoChassisIdRx_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 6, 1, 1, 10),
    _AdGenMuxPPhysPeerTwoChassisIdRx_Type()
)
adGenMuxPPhysPeerTwoChassisIdRx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenMuxPPhysPeerTwoChassisIdRx.setStatus("deprecated")
_AdGenMuxPPhysPeerTwoPortIdTx_Type = DisplayString
_AdGenMuxPPhysPeerTwoPortIdTx_Object = MibTableColumn
adGenMuxPPhysPeerTwoPortIdTx = _AdGenMuxPPhysPeerTwoPortIdTx_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 6, 1, 1, 11),
    _AdGenMuxPPhysPeerTwoPortIdTx_Type()
)
adGenMuxPPhysPeerTwoPortIdTx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenMuxPPhysPeerTwoPortIdTx.setStatus("deprecated")
_AdGenMuxPPhysPeerTwoPortIdRx_Type = DisplayString
_AdGenMuxPPhysPeerTwoPortIdRx_Object = MibTableColumn
adGenMuxPPhysPeerTwoPortIdRx = _AdGenMuxPPhysPeerTwoPortIdRx_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 6, 1, 1, 12),
    _AdGenMuxPPhysPeerTwoPortIdRx_Type()
)
adGenMuxPPhysPeerTwoPortIdRx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenMuxPPhysPeerTwoPortIdRx.setStatus("deprecated")
_AdGenMuxPIfStatus_ObjectIdentity = ObjectIdentity
adGenMuxPIfStatus = _AdGenMuxPIfStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 7)
)
_AdGenMuxPIfStatusTable_Object = MibTable
adGenMuxPIfStatusTable = _AdGenMuxPIfStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 7, 1)
)
if mibBuilder.loadTexts:
    adGenMuxPIfStatusTable.setStatus("current")
_AdGenMuxPIfStatusEntry_Object = MibTableRow
adGenMuxPIfStatusEntry = _AdGenMuxPIfStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 7, 1, 1)
)
adGenMuxPIfStatusEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adGenMuxPIfStatusEntry.setStatus("current")


class _AdGenMuxPInterfacePortStatus_Type(Bits):
    """Custom type adGenMuxPInterfacePortStatus based on Bits"""
    namedValues = NamedValues(
        *(("fault", 0),
          ("superordinateFault", 1),
          ("subordinateFault", 2),
          ("superordinateUnassigned", 3),
          ("subordinateInserviceOrMaintenance", 4),
          ("protected", 5),
          ("superordinateProtected", 6),
          ("subordinateProtected", 7),
          ("mapped", 8),
          ("reserved1", 9),
          ("subordinateMapped", 10),
          ("crossconnected", 11),
          ("reserved2", 12),
          ("subordinateCrossConnected", 13),
          ("online", 14))
    )

_AdGenMuxPInterfacePortStatus_Type.__name__ = "Bits"
_AdGenMuxPInterfacePortStatus_Object = MibTableColumn
adGenMuxPInterfacePortStatus = _AdGenMuxPInterfacePortStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 7, 1, 1, 1),
    _AdGenMuxPInterfacePortStatus_Type()
)
adGenMuxPInterfacePortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMuxPInterfacePortStatus.setStatus("current")


class _AdGenMuxPInterfacePortProtGrpName_Type(DisplayString):
    """Custom type adGenMuxPInterfacePortProtGrpName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 50),
    )


_AdGenMuxPInterfacePortProtGrpName_Type.__name__ = "DisplayString"
_AdGenMuxPInterfacePortProtGrpName_Object = MibTableColumn
adGenMuxPInterfacePortProtGrpName = _AdGenMuxPInterfacePortProtGrpName_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 7, 1, 1, 2),
    _AdGenMuxPInterfacePortProtGrpName_Type()
)
adGenMuxPInterfacePortProtGrpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMuxPInterfacePortProtGrpName.setStatus("current")
_AdGenMuxPMappingProv_ObjectIdentity = ObjectIdentity
adGenMuxPMappingProv = _AdGenMuxPMappingProv_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 8)
)
_AdGenMuxPMappingTable_Object = MibTable
adGenMuxPMappingTable = _AdGenMuxPMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 8, 1)
)
if mibBuilder.loadTexts:
    adGenMuxPMappingTable.setStatus("current")
_AdGenMuxPMappingEntry_Object = MibTableRow
adGenMuxPMappingEntry = _AdGenMuxPMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 8, 1, 1)
)
adGenMuxPMappingEntry.setIndexNames(
    (0, "ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
    (1, "ADTRAN-GENMUXPONDER-MIB", "adGenMuxPMappingName"),
)
if mibBuilder.loadTexts:
    adGenMuxPMappingEntry.setStatus("current")


class _AdGenMuxPMappingName_Type(DisplayString):
    """Custom type adGenMuxPMappingName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 50),
    )


_AdGenMuxPMappingName_Type.__name__ = "DisplayString"
_AdGenMuxPMappingName_Object = MibTableColumn
adGenMuxPMappingName = _AdGenMuxPMappingName_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 8, 1, 1, 1),
    _AdGenMuxPMappingName_Type()
)
adGenMuxPMappingName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adGenMuxPMappingName.setStatus("current")


class _AdGenMuxPMappingType_Type(Integer32):
    """Custom type adGenMuxPMappingType based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("bitTransparentSynchronous", 1),
          ("bitTransparentAsynchronous", 2),
          ("gfpfNontransparent", 3),
          ("gfpfSemitransparent", 4),
          ("gfptTransparent", 5),
          ("wis", 6),
          ("passthrough", 7),
          ("crossconnect", 8),
          ("gmp", 9))
    )


_AdGenMuxPMappingType_Type.__name__ = "Integer32"
_AdGenMuxPMappingType_Object = MibTableColumn
adGenMuxPMappingType = _AdGenMuxPMappingType_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 8, 1, 1, 2),
    _AdGenMuxPMappingType_Type()
)
adGenMuxPMappingType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenMuxPMappingType.setStatus("current")


class _AdGenMuxPMappingDirection_Type(Integer32):
    """Custom type adGenMuxPMappingDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("twoWay", 1),
          ("oneWay", 2))
    )


_AdGenMuxPMappingDirection_Type.__name__ = "Integer32"
_AdGenMuxPMappingDirection_Object = MibTableColumn
adGenMuxPMappingDirection = _AdGenMuxPMappingDirection_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 8, 1, 1, 3),
    _AdGenMuxPMappingDirection_Type()
)
adGenMuxPMappingDirection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenMuxPMappingDirection.setStatus("current")
_AdGenMuxPMappingSrcType_Type = MuxPPayloadTypes
_AdGenMuxPMappingSrcType_Object = MibTableColumn
adGenMuxPMappingSrcType = _AdGenMuxPMappingSrcType_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 8, 1, 1, 4),
    _AdGenMuxPMappingSrcType_Type()
)
adGenMuxPMappingSrcType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMuxPMappingSrcType.setStatus("current")
_AdGenMuxPMappingSrcInterface_Type = MuxPMapInterface
_AdGenMuxPMappingSrcInterface_Object = MibTableColumn
adGenMuxPMappingSrcInterface = _AdGenMuxPMappingSrcInterface_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 8, 1, 1, 5),
    _AdGenMuxPMappingSrcInterface_Type()
)
adGenMuxPMappingSrcInterface.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenMuxPMappingSrcInterface.setStatus("current")
_AdGenMuxPMappingDstType_Type = MuxPPayloadTypes
_AdGenMuxPMappingDstType_Object = MibTableColumn
adGenMuxPMappingDstType = _AdGenMuxPMappingDstType_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 8, 1, 1, 6),
    _AdGenMuxPMappingDstType_Type()
)
adGenMuxPMappingDstType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenMuxPMappingDstType.setStatus("current")
_AdGenMuxPMappingDstInterface_Type = MuxPMapInterface
_AdGenMuxPMappingDstInterface_Object = MibTableColumn
adGenMuxPMappingDstInterface = _AdGenMuxPMappingDstInterface_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 8, 1, 1, 7),
    _AdGenMuxPMappingDstInterface_Type()
)
adGenMuxPMappingDstInterface.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenMuxPMappingDstInterface.setStatus("current")
_AdGenMuxPMappingRowStatus_Type = RowStatus
_AdGenMuxPMappingRowStatus_Object = MibTableColumn
adGenMuxPMappingRowStatus = _AdGenMuxPMappingRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 8, 1, 1, 8),
    _AdGenMuxPMappingRowStatus_Type()
)
adGenMuxPMappingRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenMuxPMappingRowStatus.setStatus("current")
_AdGenMuxPMappingLastProvError_Type = DisplayString
_AdGenMuxPMappingLastProvError_Object = MibTableColumn
adGenMuxPMappingLastProvError = _AdGenMuxPMappingLastProvError_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 8, 1, 1, 9),
    _AdGenMuxPMappingLastProvError_Type()
)
adGenMuxPMappingLastProvError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMuxPMappingLastProvError.setStatus("current")


class _AdGenMuxPMappingOperStatus_Type(Integer32):
    """Custom type adGenMuxPMappingOperStatus based on Integer32"""
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


_AdGenMuxPMappingOperStatus_Type.__name__ = "Integer32"
_AdGenMuxPMappingOperStatus_Object = MibTableColumn
adGenMuxPMappingOperStatus = _AdGenMuxPMappingOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 8, 1, 1, 10),
    _AdGenMuxPMappingOperStatus_Type()
)
adGenMuxPMappingOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMuxPMappingOperStatus.setStatus("current")
_AdGenMuxPMappingStatusString_Type = DisplayString
_AdGenMuxPMappingStatusString_Object = MibTableColumn
adGenMuxPMappingStatusString = _AdGenMuxPMappingStatusString_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 8, 1, 1, 11),
    _AdGenMuxPMappingStatusString_Type()
)
adGenMuxPMappingStatusString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMuxPMappingStatusString.setStatus("current")
_AdGenMuxPMappingLastCreateErrorTable_Object = MibTable
adGenMuxPMappingLastCreateErrorTable = _AdGenMuxPMappingLastCreateErrorTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 8, 2)
)
if mibBuilder.loadTexts:
    adGenMuxPMappingLastCreateErrorTable.setStatus("current")
_AdGenMuxPMappingLastCreateErrorEntry_Object = MibTableRow
adGenMuxPMappingLastCreateErrorEntry = _AdGenMuxPMappingLastCreateErrorEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 8, 2, 1)
)
adGenMuxPMappingLastCreateErrorEntry.setIndexNames(
    (0, "ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
)
if mibBuilder.loadTexts:
    adGenMuxPMappingLastCreateErrorEntry.setStatus("current")
_AdGenMuxPMappingLastCreateError_Type = DisplayString
_AdGenMuxPMappingLastCreateError_Object = MibTableColumn
adGenMuxPMappingLastCreateError = _AdGenMuxPMappingLastCreateError_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 8, 2, 1, 1),
    _AdGenMuxPMappingLastCreateError_Type()
)
adGenMuxPMappingLastCreateError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMuxPMappingLastCreateError.setStatus("current")
_AdGenMuxPPortMappingStatusTable_Object = MibTable
adGenMuxPPortMappingStatusTable = _AdGenMuxPPortMappingStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 8, 3)
)
if mibBuilder.loadTexts:
    adGenMuxPPortMappingStatusTable.setStatus("current")
_AdGenMuxPPortMappingStatusEntry_Object = MibTableRow
adGenMuxPPortMappingStatusEntry = _AdGenMuxPPortMappingStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 8, 3, 1)
)
adGenMuxPPortMappingStatusEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ADTRAN-GENMUXPONDER-MIB", "adGenMuxPPortMappingName"),
)
if mibBuilder.loadTexts:
    adGenMuxPPortMappingStatusEntry.setStatus("current")


class _AdGenMuxPPortMappingName_Type(DisplayString):
    """Custom type adGenMuxPPortMappingName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 50),
    )


_AdGenMuxPPortMappingName_Type.__name__ = "DisplayString"
_AdGenMuxPPortMappingName_Object = MibTableColumn
adGenMuxPPortMappingName = _AdGenMuxPPortMappingName_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 8, 3, 1, 1),
    _AdGenMuxPPortMappingName_Type()
)
adGenMuxPPortMappingName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMuxPPortMappingName.setStatus("current")


class _AdGenMuxPPortMappingStatus_Type(Integer32):
    """Custom type adGenMuxPPortMappingStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("source", 1),
          ("destination", 2),
          ("sourceAndDestination", 3))
    )


_AdGenMuxPPortMappingStatus_Type.__name__ = "Integer32"
_AdGenMuxPPortMappingStatus_Object = MibTableColumn
adGenMuxPPortMappingStatus = _AdGenMuxPPortMappingStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 8, 3, 1, 2),
    _AdGenMuxPPortMappingStatus_Type()
)
adGenMuxPPortMappingStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMuxPPortMappingStatus.setStatus("current")
_AdGenMuxPMultiProtGroupProv_ObjectIdentity = ObjectIdentity
adGenMuxPMultiProtGroupProv = _AdGenMuxPMultiProtGroupProv_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 9)
)
_AdGenMuxPMultiProtGroupTable_Object = MibTable
adGenMuxPMultiProtGroupTable = _AdGenMuxPMultiProtGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 9, 1)
)
if mibBuilder.loadTexts:
    adGenMuxPMultiProtGroupTable.setStatus("current")
_AdGenMuxPMultiProtGroupEntry_Object = MibTableRow
adGenMuxPMultiProtGroupEntry = _AdGenMuxPMultiProtGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 9, 1, 1)
)
adGenMuxPMultiProtGroupEntry.setIndexNames(
    (0, "ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
    (1, "ADTRAN-GENMUXPONDER-MIB", "adGenMuxPMultiProtGroupName"),
)
if mibBuilder.loadTexts:
    adGenMuxPMultiProtGroupEntry.setStatus("current")


class _AdGenMuxPMultiProtGroupName_Type(DisplayString):
    """Custom type adGenMuxPMultiProtGroupName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 50),
    )


_AdGenMuxPMultiProtGroupName_Type.__name__ = "DisplayString"
_AdGenMuxPMultiProtGroupName_Object = MibTableColumn
adGenMuxPMultiProtGroupName = _AdGenMuxPMultiProtGroupName_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 9, 1, 1, 1),
    _AdGenMuxPMultiProtGroupName_Type()
)
adGenMuxPMultiProtGroupName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adGenMuxPMultiProtGroupName.setStatus("current")
_AdGenMuxPMultiProtGroupRowStatus_Type = RowStatus
_AdGenMuxPMultiProtGroupRowStatus_Object = MibTableColumn
adGenMuxPMultiProtGroupRowStatus = _AdGenMuxPMultiProtGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 9, 1, 1, 2),
    _AdGenMuxPMultiProtGroupRowStatus_Type()
)
adGenMuxPMultiProtGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenMuxPMultiProtGroupRowStatus.setStatus("current")
_AdGenMuxPMultiProtGroupLastProvError_Type = DisplayString
_AdGenMuxPMultiProtGroupLastProvError_Object = MibTableColumn
adGenMuxPMultiProtGroupLastProvError = _AdGenMuxPMultiProtGroupLastProvError_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 9, 1, 1, 3),
    _AdGenMuxPMultiProtGroupLastProvError_Type()
)
adGenMuxPMultiProtGroupLastProvError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMuxPMultiProtGroupLastProvError.setStatus("current")


class _AdGenMuxPMultiProtGroupOperStatus_Type(Integer32):
    """Custom type adGenMuxPMultiProtGroupOperStatus based on Integer32"""
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


_AdGenMuxPMultiProtGroupOperStatus_Type.__name__ = "Integer32"
_AdGenMuxPMultiProtGroupOperStatus_Object = MibTableColumn
adGenMuxPMultiProtGroupOperStatus = _AdGenMuxPMultiProtGroupOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 9, 1, 1, 4),
    _AdGenMuxPMultiProtGroupOperStatus_Type()
)
adGenMuxPMultiProtGroupOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMuxPMultiProtGroupOperStatus.setStatus("current")
_AdGenMuxPMultiProtGroupStatusString_Type = DisplayString
_AdGenMuxPMultiProtGroupStatusString_Object = MibTableColumn
adGenMuxPMultiProtGroupStatusString = _AdGenMuxPMultiProtGroupStatusString_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 9, 1, 1, 5),
    _AdGenMuxPMultiProtGroupStatusString_Type()
)
adGenMuxPMultiProtGroupStatusString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMuxPMultiProtGroupStatusString.setStatus("current")
_AdGenMuxPMultiProtGroupWorkIsOnline_Type = TruthValue
_AdGenMuxPMultiProtGroupWorkIsOnline_Object = MibTableColumn
adGenMuxPMultiProtGroupWorkIsOnline = _AdGenMuxPMultiProtGroupWorkIsOnline_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 9, 1, 1, 6),
    _AdGenMuxPMultiProtGroupWorkIsOnline_Type()
)
adGenMuxPMultiProtGroupWorkIsOnline.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMuxPMultiProtGroupWorkIsOnline.setStatus("current")


class _AdGenMuxPMultiProtGroupSwitchCommands_Type(Integer32):
    """Custom type adGenMuxPMultiProtGroupSwitchCommands based on Integer32"""
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
        *(("clear", 1),
          ("manualSwitchToWork", 2),
          ("manualSwitchToProt", 3),
          ("forceSwitchToWork", 4),
          ("forceSwitchToProt", 5),
          ("lockout", 6))
    )


_AdGenMuxPMultiProtGroupSwitchCommands_Type.__name__ = "Integer32"
_AdGenMuxPMultiProtGroupSwitchCommands_Object = MibTableColumn
adGenMuxPMultiProtGroupSwitchCommands = _AdGenMuxPMultiProtGroupSwitchCommands_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 9, 1, 1, 7),
    _AdGenMuxPMultiProtGroupSwitchCommands_Type()
)
adGenMuxPMultiProtGroupSwitchCommands.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenMuxPMultiProtGroupSwitchCommands.setStatus("current")
_AdGenMuxPMultiProtGroupRevertiveEnable_Type = TruthValue
_AdGenMuxPMultiProtGroupRevertiveEnable_Object = MibTableColumn
adGenMuxPMultiProtGroupRevertiveEnable = _AdGenMuxPMultiProtGroupRevertiveEnable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 9, 1, 1, 8),
    _AdGenMuxPMultiProtGroupRevertiveEnable_Type()
)
adGenMuxPMultiProtGroupRevertiveEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenMuxPMultiProtGroupRevertiveEnable.setStatus("current")


class _AdGenMuxPMultiProtGroupWaitToRestoreTime_Type(Integer32):
    """Custom type adGenMuxPMultiProtGroupWaitToRestoreTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_AdGenMuxPMultiProtGroupWaitToRestoreTime_Type.__name__ = "Integer32"
_AdGenMuxPMultiProtGroupWaitToRestoreTime_Object = MibTableColumn
adGenMuxPMultiProtGroupWaitToRestoreTime = _AdGenMuxPMultiProtGroupWaitToRestoreTime_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 9, 1, 1, 9),
    _AdGenMuxPMultiProtGroupWaitToRestoreTime_Type()
)
adGenMuxPMultiProtGroupWaitToRestoreTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenMuxPMultiProtGroupWaitToRestoreTime.setStatus("current")
_AdGenMuxPMultiProtGroupLastCreateErrorTable_Object = MibTable
adGenMuxPMultiProtGroupLastCreateErrorTable = _AdGenMuxPMultiProtGroupLastCreateErrorTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 9, 2)
)
if mibBuilder.loadTexts:
    adGenMuxPMultiProtGroupLastCreateErrorTable.setStatus("current")
_AdGenMuxPMultiProtGroupLastCreateErrorEntry_Object = MibTableRow
adGenMuxPMultiProtGroupLastCreateErrorEntry = _AdGenMuxPMultiProtGroupLastCreateErrorEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 9, 2, 1)
)
adGenMuxPMultiProtGroupLastCreateErrorEntry.setIndexNames(
    (0, "ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
)
if mibBuilder.loadTexts:
    adGenMuxPMultiProtGroupLastCreateErrorEntry.setStatus("current")
_AdGenMuxPMultiProtGroupLastCreateError_Type = DisplayString
_AdGenMuxPMultiProtGroupLastCreateError_Object = MibTableColumn
adGenMuxPMultiProtGroupLastCreateError = _AdGenMuxPMultiProtGroupLastCreateError_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 9, 2, 1, 1),
    _AdGenMuxPMultiProtGroupLastCreateError_Type()
)
adGenMuxPMultiProtGroupLastCreateError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMuxPMultiProtGroupLastCreateError.setStatus("current")
_AdGenMuxPMultiSonetProtPairTable_Object = MibTable
adGenMuxPMultiSonetProtPairTable = _AdGenMuxPMultiSonetProtPairTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 9, 3)
)
if mibBuilder.loadTexts:
    adGenMuxPMultiSonetProtPairTable.setStatus("current")
_AdGenMuxPMultiSonetProtPairEntry_Object = MibTableRow
adGenMuxPMultiSonetProtPairEntry = _AdGenMuxPMultiSonetProtPairEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 9, 3, 1)
)
adGenMuxPMultiSonetProtPairEntry.setIndexNames(
    (0, "ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
    (0, "ADTRAN-GENMUXPONDER-MIB", "adGenMuxPMultiProtGroupName"),
    (1, "ADTRAN-GENMUXPONDER-MIB", "adGenMuxPMultiSonetProtPairName"),
)
if mibBuilder.loadTexts:
    adGenMuxPMultiSonetProtPairEntry.setStatus("current")


class _AdGenMuxPMultiSonetProtPairName_Type(DisplayString):
    """Custom type adGenMuxPMultiSonetProtPairName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 50),
    )


_AdGenMuxPMultiSonetProtPairName_Type.__name__ = "DisplayString"
_AdGenMuxPMultiSonetProtPairName_Object = MibTableColumn
adGenMuxPMultiSonetProtPairName = _AdGenMuxPMultiSonetProtPairName_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 9, 3, 1, 1),
    _AdGenMuxPMultiSonetProtPairName_Type()
)
adGenMuxPMultiSonetProtPairName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adGenMuxPMultiSonetProtPairName.setStatus("current")


class _AdGenMuxPMultiSonetProtPairType_Type(Integer32):
    """Custom type adGenMuxPMultiSonetProtPairType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("terminalUniDir", 1),
          ("yCable", 2))
    )


_AdGenMuxPMultiSonetProtPairType_Type.__name__ = "Integer32"
_AdGenMuxPMultiSonetProtPairType_Object = MibTableColumn
adGenMuxPMultiSonetProtPairType = _AdGenMuxPMultiSonetProtPairType_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 9, 3, 1, 2),
    _AdGenMuxPMultiSonetProtPairType_Type()
)
adGenMuxPMultiSonetProtPairType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenMuxPMultiSonetProtPairType.setStatus("current")
_AdGenMuxPMultiSonetProtPairWorkingType_Type = MuxPPayloadTypes
_AdGenMuxPMultiSonetProtPairWorkingType_Object = MibTableColumn
adGenMuxPMultiSonetProtPairWorkingType = _AdGenMuxPMultiSonetProtPairWorkingType_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 9, 3, 1, 3),
    _AdGenMuxPMultiSonetProtPairWorkingType_Type()
)
adGenMuxPMultiSonetProtPairWorkingType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMuxPMultiSonetProtPairWorkingType.setStatus("current")
_AdGenMuxPMultiSonetProtPairWorkingIfIndex_Type = InterfaceIndex
_AdGenMuxPMultiSonetProtPairWorkingIfIndex_Object = MibTableColumn
adGenMuxPMultiSonetProtPairWorkingIfIndex = _AdGenMuxPMultiSonetProtPairWorkingIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 9, 3, 1, 4),
    _AdGenMuxPMultiSonetProtPairWorkingIfIndex_Type()
)
adGenMuxPMultiSonetProtPairWorkingIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenMuxPMultiSonetProtPairWorkingIfIndex.setStatus("current")
_AdGenMuxPMultiSonetProtPairProtectingType_Type = MuxPPayloadTypes
_AdGenMuxPMultiSonetProtPairProtectingType_Object = MibTableColumn
adGenMuxPMultiSonetProtPairProtectingType = _AdGenMuxPMultiSonetProtPairProtectingType_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 9, 3, 1, 5),
    _AdGenMuxPMultiSonetProtPairProtectingType_Type()
)
adGenMuxPMultiSonetProtPairProtectingType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMuxPMultiSonetProtPairProtectingType.setStatus("current")
_AdGenMuxPMultiSonetProtPairProtectingIfIndex_Type = InterfaceIndex
_AdGenMuxPMultiSonetProtPairProtectingIfIndex_Object = MibTableColumn
adGenMuxPMultiSonetProtPairProtectingIfIndex = _AdGenMuxPMultiSonetProtPairProtectingIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 9, 3, 1, 6),
    _AdGenMuxPMultiSonetProtPairProtectingIfIndex_Type()
)
adGenMuxPMultiSonetProtPairProtectingIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenMuxPMultiSonetProtPairProtectingIfIndex.setStatus("current")
_AdGenMuxPMultiSonetProtPairRowStatus_Type = RowStatus
_AdGenMuxPMultiSonetProtPairRowStatus_Object = MibTableColumn
adGenMuxPMultiSonetProtPairRowStatus = _AdGenMuxPMultiSonetProtPairRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 9, 3, 1, 7),
    _AdGenMuxPMultiSonetProtPairRowStatus_Type()
)
adGenMuxPMultiSonetProtPairRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenMuxPMultiSonetProtPairRowStatus.setStatus("current")
_AdGenMuxPMultiSonetProtPairLastProvError_Type = DisplayString
_AdGenMuxPMultiSonetProtPairLastProvError_Object = MibTableColumn
adGenMuxPMultiSonetProtPairLastProvError = _AdGenMuxPMultiSonetProtPairLastProvError_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 9, 3, 1, 8),
    _AdGenMuxPMultiSonetProtPairLastProvError_Type()
)
adGenMuxPMultiSonetProtPairLastProvError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMuxPMultiSonetProtPairLastProvError.setStatus("current")


class _AdGenMuxPMultiSonetProtPairWorkEntityStatus_Type(Integer32):
    """Custom type adGenMuxPMultiSonetProtPairWorkEntityStatus based on Integer32"""
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
        *(("clear", 1),
          ("signalFaulty", 2),
          ("signalDegraded", 3),
          ("down", 4))
    )


_AdGenMuxPMultiSonetProtPairWorkEntityStatus_Type.__name__ = "Integer32"
_AdGenMuxPMultiSonetProtPairWorkEntityStatus_Object = MibTableColumn
adGenMuxPMultiSonetProtPairWorkEntityStatus = _AdGenMuxPMultiSonetProtPairWorkEntityStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 9, 3, 1, 9),
    _AdGenMuxPMultiSonetProtPairWorkEntityStatus_Type()
)
adGenMuxPMultiSonetProtPairWorkEntityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMuxPMultiSonetProtPairWorkEntityStatus.setStatus("current")


class _AdGenMuxPMultiSonetProtPairProtectEntityStatus_Type(Integer32):
    """Custom type adGenMuxPMultiSonetProtPairProtectEntityStatus based on Integer32"""
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
        *(("clear", 1),
          ("signalFaulty", 2),
          ("signalDegraded", 3),
          ("down", 4))
    )


_AdGenMuxPMultiSonetProtPairProtectEntityStatus_Type.__name__ = "Integer32"
_AdGenMuxPMultiSonetProtPairProtectEntityStatus_Object = MibTableColumn
adGenMuxPMultiSonetProtPairProtectEntityStatus = _AdGenMuxPMultiSonetProtPairProtectEntityStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 9, 3, 1, 10),
    _AdGenMuxPMultiSonetProtPairProtectEntityStatus_Type()
)
adGenMuxPMultiSonetProtPairProtectEntityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMuxPMultiSonetProtPairProtectEntityStatus.setStatus("current")


class _AdGenMuxPMultiSonetProtPairTxK1Request_Type(Integer32):
    """Custom type adGenMuxPMultiSonetProtPairTxK1Request based on Integer32"""
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
              12)
        )
    )
    namedValues = NamedValues(
        *(("notAvailable", 1),
          ("noRequest", 2),
          ("doNotRevert", 3),
          ("reverseRequest", 4),
          ("waitToRestore", 5),
          ("manualSwitch", 6),
          ("signalDegrade", 7),
          ("signalFail", 8),
          ("forceSwitch", 9),
          ("lockout", 10),
          ("reserved", 11),
          ("notSupported", 12))
    )


_AdGenMuxPMultiSonetProtPairTxK1Request_Type.__name__ = "Integer32"
_AdGenMuxPMultiSonetProtPairTxK1Request_Object = MibTableColumn
adGenMuxPMultiSonetProtPairTxK1Request = _AdGenMuxPMultiSonetProtPairTxK1Request_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 9, 3, 1, 11),
    _AdGenMuxPMultiSonetProtPairTxK1Request_Type()
)
adGenMuxPMultiSonetProtPairTxK1Request.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMuxPMultiSonetProtPairTxK1Request.setStatus("current")


class _AdGenMuxPMultiSonetProtPairTxK1RequestChannel_Type(Integer32):
    """Custom type adGenMuxPMultiSonetProtPairTxK1RequestChannel based on Integer32"""
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
        *(("notAvailable", 1),
          ("protect", 2),
          ("working", 3),
          ("invalid", 4))
    )


_AdGenMuxPMultiSonetProtPairTxK1RequestChannel_Type.__name__ = "Integer32"
_AdGenMuxPMultiSonetProtPairTxK1RequestChannel_Object = MibTableColumn
adGenMuxPMultiSonetProtPairTxK1RequestChannel = _AdGenMuxPMultiSonetProtPairTxK1RequestChannel_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 9, 3, 1, 12),
    _AdGenMuxPMultiSonetProtPairTxK1RequestChannel_Type()
)
adGenMuxPMultiSonetProtPairTxK1RequestChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMuxPMultiSonetProtPairTxK1RequestChannel.setStatus("current")


class _AdGenMuxPMultiSonetProtPairTxK2BridgeChannel_Type(Integer32):
    """Custom type adGenMuxPMultiSonetProtPairTxK2BridgeChannel based on Integer32"""
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
        *(("notAvailable", 1),
          ("protect", 2),
          ("working", 3),
          ("invalid", 4))
    )


_AdGenMuxPMultiSonetProtPairTxK2BridgeChannel_Type.__name__ = "Integer32"
_AdGenMuxPMultiSonetProtPairTxK2BridgeChannel_Object = MibTableColumn
adGenMuxPMultiSonetProtPairTxK2BridgeChannel = _AdGenMuxPMultiSonetProtPairTxK2BridgeChannel_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 9, 3, 1, 13),
    _AdGenMuxPMultiSonetProtPairTxK2BridgeChannel_Type()
)
adGenMuxPMultiSonetProtPairTxK2BridgeChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMuxPMultiSonetProtPairTxK2BridgeChannel.setStatus("current")


class _AdGenMuxPMultiSonetProtPairTxK2APSArchitecture_Type(Integer32):
    """Custom type adGenMuxPMultiSonetProtPairTxK2APSArchitecture based on Integer32"""
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
        *(("notAvailable", 1),
          ("notProtected", 2),
          ("onePlusOne", 3),
          ("oneToOne", 4))
    )


_AdGenMuxPMultiSonetProtPairTxK2APSArchitecture_Type.__name__ = "Integer32"
_AdGenMuxPMultiSonetProtPairTxK2APSArchitecture_Object = MibTableColumn
adGenMuxPMultiSonetProtPairTxK2APSArchitecture = _AdGenMuxPMultiSonetProtPairTxK2APSArchitecture_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 9, 3, 1, 14),
    _AdGenMuxPMultiSonetProtPairTxK2APSArchitecture_Type()
)
adGenMuxPMultiSonetProtPairTxK2APSArchitecture.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMuxPMultiSonetProtPairTxK2APSArchitecture.setStatus("current")


class _AdGenMuxPMultiSonetProtPairTxK2APSMode_Type(Integer32):
    """Custom type adGenMuxPMultiSonetProtPairTxK2APSMode based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("notAvailable", 1),
          ("unidirectional", 2),
          ("bidirectional", 3),
          ("aisL", 4),
          ("rdiL", 5),
          ("msAis", 6),
          ("msRdi", 7),
          ("reserved", 8))
    )


_AdGenMuxPMultiSonetProtPairTxK2APSMode_Type.__name__ = "Integer32"
_AdGenMuxPMultiSonetProtPairTxK2APSMode_Object = MibTableColumn
adGenMuxPMultiSonetProtPairTxK2APSMode = _AdGenMuxPMultiSonetProtPairTxK2APSMode_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 9, 3, 1, 15),
    _AdGenMuxPMultiSonetProtPairTxK2APSMode_Type()
)
adGenMuxPMultiSonetProtPairTxK2APSMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMuxPMultiSonetProtPairTxK2APSMode.setStatus("current")


class _AdGenMuxPMultiSonetProtPairRxK1Request_Type(Integer32):
    """Custom type adGenMuxPMultiSonetProtPairRxK1Request based on Integer32"""
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
              12)
        )
    )
    namedValues = NamedValues(
        *(("notAvailable", 1),
          ("noRequest", 2),
          ("doNotRevert", 3),
          ("reverseRequest", 4),
          ("waitToRestore", 5),
          ("manualSwitch", 6),
          ("signalDegrade", 7),
          ("signalFail", 8),
          ("forceSwitch", 9),
          ("lockout", 10),
          ("reserved", 11),
          ("notSupported", 12))
    )


_AdGenMuxPMultiSonetProtPairRxK1Request_Type.__name__ = "Integer32"
_AdGenMuxPMultiSonetProtPairRxK1Request_Object = MibTableColumn
adGenMuxPMultiSonetProtPairRxK1Request = _AdGenMuxPMultiSonetProtPairRxK1Request_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 9, 3, 1, 16),
    _AdGenMuxPMultiSonetProtPairRxK1Request_Type()
)
adGenMuxPMultiSonetProtPairRxK1Request.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMuxPMultiSonetProtPairRxK1Request.setStatus("current")


class _AdGenMuxPMultiSonetProtPairRxK1RequestChannel_Type(Integer32):
    """Custom type adGenMuxPMultiSonetProtPairRxK1RequestChannel based on Integer32"""
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
        *(("notAvailable", 1),
          ("protect", 2),
          ("working", 3),
          ("invalid", 4))
    )


_AdGenMuxPMultiSonetProtPairRxK1RequestChannel_Type.__name__ = "Integer32"
_AdGenMuxPMultiSonetProtPairRxK1RequestChannel_Object = MibTableColumn
adGenMuxPMultiSonetProtPairRxK1RequestChannel = _AdGenMuxPMultiSonetProtPairRxK1RequestChannel_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 9, 3, 1, 17),
    _AdGenMuxPMultiSonetProtPairRxK1RequestChannel_Type()
)
adGenMuxPMultiSonetProtPairRxK1RequestChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMuxPMultiSonetProtPairRxK1RequestChannel.setStatus("current")


class _AdGenMuxPMultiSonetProtPairRxK2BridgeChannel_Type(Integer32):
    """Custom type adGenMuxPMultiSonetProtPairRxK2BridgeChannel based on Integer32"""
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
        *(("notAvailable", 1),
          ("protect", 2),
          ("working", 3),
          ("invalid", 4))
    )


_AdGenMuxPMultiSonetProtPairRxK2BridgeChannel_Type.__name__ = "Integer32"
_AdGenMuxPMultiSonetProtPairRxK2BridgeChannel_Object = MibTableColumn
adGenMuxPMultiSonetProtPairRxK2BridgeChannel = _AdGenMuxPMultiSonetProtPairRxK2BridgeChannel_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 9, 3, 1, 18),
    _AdGenMuxPMultiSonetProtPairRxK2BridgeChannel_Type()
)
adGenMuxPMultiSonetProtPairRxK2BridgeChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMuxPMultiSonetProtPairRxK2BridgeChannel.setStatus("current")


class _AdGenMuxPMultiSonetProtPairRxK2APSArchitecture_Type(Integer32):
    """Custom type adGenMuxPMultiSonetProtPairRxK2APSArchitecture based on Integer32"""
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
        *(("notAvailable", 1),
          ("notProtected", 2),
          ("onePlusOne", 3),
          ("oneToOne", 4))
    )


_AdGenMuxPMultiSonetProtPairRxK2APSArchitecture_Type.__name__ = "Integer32"
_AdGenMuxPMultiSonetProtPairRxK2APSArchitecture_Object = MibTableColumn
adGenMuxPMultiSonetProtPairRxK2APSArchitecture = _AdGenMuxPMultiSonetProtPairRxK2APSArchitecture_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 9, 3, 1, 19),
    _AdGenMuxPMultiSonetProtPairRxK2APSArchitecture_Type()
)
adGenMuxPMultiSonetProtPairRxK2APSArchitecture.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMuxPMultiSonetProtPairRxK2APSArchitecture.setStatus("current")


class _AdGenMuxPMultiSonetProtPairRxK2APSMode_Type(Integer32):
    """Custom type adGenMuxPMultiSonetProtPairRxK2APSMode based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("notAvailable", 1),
          ("unidirectional", 2),
          ("bidirectional", 3),
          ("aisL", 4),
          ("rdiL", 5),
          ("msAis", 6),
          ("msRdi", 7),
          ("reserved", 8))
    )


_AdGenMuxPMultiSonetProtPairRxK2APSMode_Type.__name__ = "Integer32"
_AdGenMuxPMultiSonetProtPairRxK2APSMode_Object = MibTableColumn
adGenMuxPMultiSonetProtPairRxK2APSMode = _AdGenMuxPMultiSonetProtPairRxK2APSMode_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 9, 3, 1, 20),
    _AdGenMuxPMultiSonetProtPairRxK2APSMode_Type()
)
adGenMuxPMultiSonetProtPairRxK2APSMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMuxPMultiSonetProtPairRxK2APSMode.setStatus("current")


class _AdGenMuxPMultiSonetProtPairOperStatus_Type(Integer32):
    """Custom type adGenMuxPMultiSonetProtPairOperStatus based on Integer32"""
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


_AdGenMuxPMultiSonetProtPairOperStatus_Type.__name__ = "Integer32"
_AdGenMuxPMultiSonetProtPairOperStatus_Object = MibTableColumn
adGenMuxPMultiSonetProtPairOperStatus = _AdGenMuxPMultiSonetProtPairOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 9, 3, 1, 21),
    _AdGenMuxPMultiSonetProtPairOperStatus_Type()
)
adGenMuxPMultiSonetProtPairOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMuxPMultiSonetProtPairOperStatus.setStatus("current")
_AdGenMuxPMultiSonetProtPairStatusString_Type = DisplayString
_AdGenMuxPMultiSonetProtPairStatusString_Object = MibTableColumn
adGenMuxPMultiSonetProtPairStatusString = _AdGenMuxPMultiSonetProtPairStatusString_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 9, 3, 1, 22),
    _AdGenMuxPMultiSonetProtPairStatusString_Type()
)
adGenMuxPMultiSonetProtPairStatusString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMuxPMultiSonetProtPairStatusString.setStatus("current")
_AdGenMuxPMultiSonetProtPairLastCreateErrorTable_Object = MibTable
adGenMuxPMultiSonetProtPairLastCreateErrorTable = _AdGenMuxPMultiSonetProtPairLastCreateErrorTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 9, 4)
)
if mibBuilder.loadTexts:
    adGenMuxPMultiSonetProtPairLastCreateErrorTable.setStatus("current")
_AdGenMuxPMultiSonetProtPairLastCreateErrorEntry_Object = MibTableRow
adGenMuxPMultiSonetProtPairLastCreateErrorEntry = _AdGenMuxPMultiSonetProtPairLastCreateErrorEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 9, 4, 1)
)
adGenMuxPMultiSonetProtPairLastCreateErrorEntry.setIndexNames(
    (0, "ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
    (0, "ADTRAN-GENMUXPONDER-MIB", "adGenMuxPMultiProtGroupName"),
)
if mibBuilder.loadTexts:
    adGenMuxPMultiSonetProtPairLastCreateErrorEntry.setStatus("current")
_AdGenMuxPMultiSonetProtPairLastCreateError_Type = DisplayString
_AdGenMuxPMultiSonetProtPairLastCreateError_Object = MibTableColumn
adGenMuxPMultiSonetProtPairLastCreateError = _AdGenMuxPMultiSonetProtPairLastCreateError_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 9, 4, 1, 1),
    _AdGenMuxPMultiSonetProtPairLastCreateError_Type()
)
adGenMuxPMultiSonetProtPairLastCreateError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMuxPMultiSonetProtPairLastCreateError.setStatus("current")
_AdGenMuxPMultiEthernetProtPairTable_Object = MibTable
adGenMuxPMultiEthernetProtPairTable = _AdGenMuxPMultiEthernetProtPairTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 9, 5)
)
if mibBuilder.loadTexts:
    adGenMuxPMultiEthernetProtPairTable.setStatus("current")
_AdGenMuxPMultiEthernetProtPairEntry_Object = MibTableRow
adGenMuxPMultiEthernetProtPairEntry = _AdGenMuxPMultiEthernetProtPairEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 9, 5, 1)
)
adGenMuxPMultiEthernetProtPairEntry.setIndexNames(
    (0, "ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
    (0, "ADTRAN-GENMUXPONDER-MIB", "adGenMuxPMultiProtGroupName"),
    (1, "ADTRAN-GENMUXPONDER-MIB", "adGenMuxPMultiEthernetProtPairName"),
)
if mibBuilder.loadTexts:
    adGenMuxPMultiEthernetProtPairEntry.setStatus("current")


class _AdGenMuxPMultiEthernetProtPairName_Type(DisplayString):
    """Custom type adGenMuxPMultiEthernetProtPairName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 50),
    )


_AdGenMuxPMultiEthernetProtPairName_Type.__name__ = "DisplayString"
_AdGenMuxPMultiEthernetProtPairName_Object = MibTableColumn
adGenMuxPMultiEthernetProtPairName = _AdGenMuxPMultiEthernetProtPairName_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 9, 5, 1, 1),
    _AdGenMuxPMultiEthernetProtPairName_Type()
)
adGenMuxPMultiEthernetProtPairName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adGenMuxPMultiEthernetProtPairName.setStatus("current")


class _AdGenMuxPMultiEthernetProtPairType_Type(Integer32):
    """Custom type adGenMuxPMultiEthernetProtPairType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("yCable", 1)
    )


_AdGenMuxPMultiEthernetProtPairType_Type.__name__ = "Integer32"
_AdGenMuxPMultiEthernetProtPairType_Object = MibTableColumn
adGenMuxPMultiEthernetProtPairType = _AdGenMuxPMultiEthernetProtPairType_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 9, 5, 1, 2),
    _AdGenMuxPMultiEthernetProtPairType_Type()
)
adGenMuxPMultiEthernetProtPairType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenMuxPMultiEthernetProtPairType.setStatus("current")
_AdGenMuxPMultiEthernetProtPairWorkingType_Type = EthernetPayloadTypes
_AdGenMuxPMultiEthernetProtPairWorkingType_Object = MibTableColumn
adGenMuxPMultiEthernetProtPairWorkingType = _AdGenMuxPMultiEthernetProtPairWorkingType_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 9, 5, 1, 3),
    _AdGenMuxPMultiEthernetProtPairWorkingType_Type()
)
adGenMuxPMultiEthernetProtPairWorkingType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMuxPMultiEthernetProtPairWorkingType.setStatus("current")
_AdGenMuxPMultiEthernetProtPairWorkingIfIndex_Type = InterfaceIndex
_AdGenMuxPMultiEthernetProtPairWorkingIfIndex_Object = MibTableColumn
adGenMuxPMultiEthernetProtPairWorkingIfIndex = _AdGenMuxPMultiEthernetProtPairWorkingIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 9, 5, 1, 4),
    _AdGenMuxPMultiEthernetProtPairWorkingIfIndex_Type()
)
adGenMuxPMultiEthernetProtPairWorkingIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenMuxPMultiEthernetProtPairWorkingIfIndex.setStatus("current")
_AdGenMuxPMultiEthernetProtPairProtectingType_Type = EthernetPayloadTypes
_AdGenMuxPMultiEthernetProtPairProtectingType_Object = MibTableColumn
adGenMuxPMultiEthernetProtPairProtectingType = _AdGenMuxPMultiEthernetProtPairProtectingType_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 9, 5, 1, 5),
    _AdGenMuxPMultiEthernetProtPairProtectingType_Type()
)
adGenMuxPMultiEthernetProtPairProtectingType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMuxPMultiEthernetProtPairProtectingType.setStatus("current")
_AdGenMuxPMultiEthernetProtPairProtectingIfIndex_Type = InterfaceIndex
_AdGenMuxPMultiEthernetProtPairProtectingIfIndex_Object = MibTableColumn
adGenMuxPMultiEthernetProtPairProtectingIfIndex = _AdGenMuxPMultiEthernetProtPairProtectingIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 9, 5, 1, 6),
    _AdGenMuxPMultiEthernetProtPairProtectingIfIndex_Type()
)
adGenMuxPMultiEthernetProtPairProtectingIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenMuxPMultiEthernetProtPairProtectingIfIndex.setStatus("current")
_AdGenMuxPMultiEthernetProtPairRowStatus_Type = RowStatus
_AdGenMuxPMultiEthernetProtPairRowStatus_Object = MibTableColumn
adGenMuxPMultiEthernetProtPairRowStatus = _AdGenMuxPMultiEthernetProtPairRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 9, 5, 1, 7),
    _AdGenMuxPMultiEthernetProtPairRowStatus_Type()
)
adGenMuxPMultiEthernetProtPairRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenMuxPMultiEthernetProtPairRowStatus.setStatus("current")
_AdGenMuxPMultiEthernetProtPairLastProvError_Type = DisplayString
_AdGenMuxPMultiEthernetProtPairLastProvError_Object = MibTableColumn
adGenMuxPMultiEthernetProtPairLastProvError = _AdGenMuxPMultiEthernetProtPairLastProvError_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 9, 5, 1, 8),
    _AdGenMuxPMultiEthernetProtPairLastProvError_Type()
)
adGenMuxPMultiEthernetProtPairLastProvError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMuxPMultiEthernetProtPairLastProvError.setStatus("current")


class _AdGenMuxPMultiEthernetProtPairOperStatus_Type(Integer32):
    """Custom type adGenMuxPMultiEthernetProtPairOperStatus based on Integer32"""
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


_AdGenMuxPMultiEthernetProtPairOperStatus_Type.__name__ = "Integer32"
_AdGenMuxPMultiEthernetProtPairOperStatus_Object = MibTableColumn
adGenMuxPMultiEthernetProtPairOperStatus = _AdGenMuxPMultiEthernetProtPairOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 9, 5, 1, 9),
    _AdGenMuxPMultiEthernetProtPairOperStatus_Type()
)
adGenMuxPMultiEthernetProtPairOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMuxPMultiEthernetProtPairOperStatus.setStatus("current")
_AdGenMuxPMultiEthernetProtPairStatusString_Type = DisplayString
_AdGenMuxPMultiEthernetProtPairStatusString_Object = MibTableColumn
adGenMuxPMultiEthernetProtPairStatusString = _AdGenMuxPMultiEthernetProtPairStatusString_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 9, 5, 1, 10),
    _AdGenMuxPMultiEthernetProtPairStatusString_Type()
)
adGenMuxPMultiEthernetProtPairStatusString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMuxPMultiEthernetProtPairStatusString.setStatus("current")


class _AdGenMuxPMultiEthernetProtPairWorkEntityStatus_Type(Integer32):
    """Custom type adGenMuxPMultiEthernetProtPairWorkEntityStatus based on Integer32"""
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
        *(("clear", 1),
          ("signalFaulty", 2),
          ("signalDegraded", 3),
          ("down", 4))
    )


_AdGenMuxPMultiEthernetProtPairWorkEntityStatus_Type.__name__ = "Integer32"
_AdGenMuxPMultiEthernetProtPairWorkEntityStatus_Object = MibTableColumn
adGenMuxPMultiEthernetProtPairWorkEntityStatus = _AdGenMuxPMultiEthernetProtPairWorkEntityStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 9, 5, 1, 11),
    _AdGenMuxPMultiEthernetProtPairWorkEntityStatus_Type()
)
adGenMuxPMultiEthernetProtPairWorkEntityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMuxPMultiEthernetProtPairWorkEntityStatus.setStatus("current")


class _AdGenMuxPMultiEthernetProtPairProtectEntityStatus_Type(Integer32):
    """Custom type adGenMuxPMultiEthernetProtPairProtectEntityStatus based on Integer32"""
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
        *(("clear", 1),
          ("signalFaulty", 2),
          ("signalDegraded", 3),
          ("down", 4))
    )


_AdGenMuxPMultiEthernetProtPairProtectEntityStatus_Type.__name__ = "Integer32"
_AdGenMuxPMultiEthernetProtPairProtectEntityStatus_Object = MibTableColumn
adGenMuxPMultiEthernetProtPairProtectEntityStatus = _AdGenMuxPMultiEthernetProtPairProtectEntityStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 9, 5, 1, 12),
    _AdGenMuxPMultiEthernetProtPairProtectEntityStatus_Type()
)
adGenMuxPMultiEthernetProtPairProtectEntityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMuxPMultiEthernetProtPairProtectEntityStatus.setStatus("current")
_AdGenMuxPMultiEthernetProtPairLastCreateErrorTable_Object = MibTable
adGenMuxPMultiEthernetProtPairLastCreateErrorTable = _AdGenMuxPMultiEthernetProtPairLastCreateErrorTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 9, 6)
)
if mibBuilder.loadTexts:
    adGenMuxPMultiEthernetProtPairLastCreateErrorTable.setStatus("current")
_AdGenMuxPMultiEthernetProtPairLastCreateErrorEntry_Object = MibTableRow
adGenMuxPMultiEthernetProtPairLastCreateErrorEntry = _AdGenMuxPMultiEthernetProtPairLastCreateErrorEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 9, 6, 1)
)
adGenMuxPMultiEthernetProtPairLastCreateErrorEntry.setIndexNames(
    (0, "ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
    (0, "ADTRAN-GENMUXPONDER-MIB", "adGenMuxPMultiProtGroupName"),
)
if mibBuilder.loadTexts:
    adGenMuxPMultiEthernetProtPairLastCreateErrorEntry.setStatus("current")
_AdGenMuxPMultiEthernetProtPairLastCreateError_Type = DisplayString
_AdGenMuxPMultiEthernetProtPairLastCreateError_Object = MibTableColumn
adGenMuxPMultiEthernetProtPairLastCreateError = _AdGenMuxPMultiEthernetProtPairLastCreateError_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 9, 6, 1, 1),
    _AdGenMuxPMultiEthernetProtPairLastCreateError_Type()
)
adGenMuxPMultiEthernetProtPairLastCreateError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMuxPMultiEthernetProtPairLastCreateError.setStatus("current")
_AdGenMuxPMultiFibreChannelProtPairTable_Object = MibTable
adGenMuxPMultiFibreChannelProtPairTable = _AdGenMuxPMultiFibreChannelProtPairTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 9, 7)
)
if mibBuilder.loadTexts:
    adGenMuxPMultiFibreChannelProtPairTable.setStatus("current")
_AdGenMuxPMultiFibreChannelProtPairEntry_Object = MibTableRow
adGenMuxPMultiFibreChannelProtPairEntry = _AdGenMuxPMultiFibreChannelProtPairEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 9, 7, 1)
)
adGenMuxPMultiFibreChannelProtPairEntry.setIndexNames(
    (0, "ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
    (0, "ADTRAN-GENMUXPONDER-MIB", "adGenMuxPMultiProtGroupName"),
    (1, "ADTRAN-GENMUXPONDER-MIB", "adGenMuxPMultiFibreChannelProtPairName"),
)
if mibBuilder.loadTexts:
    adGenMuxPMultiFibreChannelProtPairEntry.setStatus("current")


class _AdGenMuxPMultiFibreChannelProtPairName_Type(DisplayString):
    """Custom type adGenMuxPMultiFibreChannelProtPairName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 50),
    )


_AdGenMuxPMultiFibreChannelProtPairName_Type.__name__ = "DisplayString"
_AdGenMuxPMultiFibreChannelProtPairName_Object = MibTableColumn
adGenMuxPMultiFibreChannelProtPairName = _AdGenMuxPMultiFibreChannelProtPairName_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 9, 7, 1, 1),
    _AdGenMuxPMultiFibreChannelProtPairName_Type()
)
adGenMuxPMultiFibreChannelProtPairName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adGenMuxPMultiFibreChannelProtPairName.setStatus("current")


class _AdGenMuxPMultiFibreChannelProtPairType_Type(Integer32):
    """Custom type adGenMuxPMultiFibreChannelProtPairType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("yCable", 1)
    )


_AdGenMuxPMultiFibreChannelProtPairType_Type.__name__ = "Integer32"
_AdGenMuxPMultiFibreChannelProtPairType_Object = MibTableColumn
adGenMuxPMultiFibreChannelProtPairType = _AdGenMuxPMultiFibreChannelProtPairType_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 9, 7, 1, 2),
    _AdGenMuxPMultiFibreChannelProtPairType_Type()
)
adGenMuxPMultiFibreChannelProtPairType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenMuxPMultiFibreChannelProtPairType.setStatus("current")
_AdGenMuxPMultiFibreChannelProtPairWorkingType_Type = FibreChanPayloadTypes
_AdGenMuxPMultiFibreChannelProtPairWorkingType_Object = MibTableColumn
adGenMuxPMultiFibreChannelProtPairWorkingType = _AdGenMuxPMultiFibreChannelProtPairWorkingType_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 9, 7, 1, 3),
    _AdGenMuxPMultiFibreChannelProtPairWorkingType_Type()
)
adGenMuxPMultiFibreChannelProtPairWorkingType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMuxPMultiFibreChannelProtPairWorkingType.setStatus("current")
_AdGenMuxPMultiFibreChannelProtPairWorkingIfIndex_Type = InterfaceIndex
_AdGenMuxPMultiFibreChannelProtPairWorkingIfIndex_Object = MibTableColumn
adGenMuxPMultiFibreChannelProtPairWorkingIfIndex = _AdGenMuxPMultiFibreChannelProtPairWorkingIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 9, 7, 1, 4),
    _AdGenMuxPMultiFibreChannelProtPairWorkingIfIndex_Type()
)
adGenMuxPMultiFibreChannelProtPairWorkingIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenMuxPMultiFibreChannelProtPairWorkingIfIndex.setStatus("current")
_AdGenMuxPMultiFibreChannelProtPairProtectingType_Type = FibreChanPayloadTypes
_AdGenMuxPMultiFibreChannelProtPairProtectingType_Object = MibTableColumn
adGenMuxPMultiFibreChannelProtPairProtectingType = _AdGenMuxPMultiFibreChannelProtPairProtectingType_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 9, 7, 1, 5),
    _AdGenMuxPMultiFibreChannelProtPairProtectingType_Type()
)
adGenMuxPMultiFibreChannelProtPairProtectingType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMuxPMultiFibreChannelProtPairProtectingType.setStatus("current")
_AdGenMuxPMultiFibreChannelProtPairProtectingIfIndex_Type = InterfaceIndex
_AdGenMuxPMultiFibreChannelProtPairProtectingIfIndex_Object = MibTableColumn
adGenMuxPMultiFibreChannelProtPairProtectingIfIndex = _AdGenMuxPMultiFibreChannelProtPairProtectingIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 9, 7, 1, 6),
    _AdGenMuxPMultiFibreChannelProtPairProtectingIfIndex_Type()
)
adGenMuxPMultiFibreChannelProtPairProtectingIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenMuxPMultiFibreChannelProtPairProtectingIfIndex.setStatus("current")
_AdGenMuxPMultiFibreChannelProtPairRowStatus_Type = RowStatus
_AdGenMuxPMultiFibreChannelProtPairRowStatus_Object = MibTableColumn
adGenMuxPMultiFibreChannelProtPairRowStatus = _AdGenMuxPMultiFibreChannelProtPairRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 9, 7, 1, 7),
    _AdGenMuxPMultiFibreChannelProtPairRowStatus_Type()
)
adGenMuxPMultiFibreChannelProtPairRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenMuxPMultiFibreChannelProtPairRowStatus.setStatus("current")
_AdGenMuxPMultiFibreChannelProtPairLastProvError_Type = DisplayString
_AdGenMuxPMultiFibreChannelProtPairLastProvError_Object = MibTableColumn
adGenMuxPMultiFibreChannelProtPairLastProvError = _AdGenMuxPMultiFibreChannelProtPairLastProvError_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 9, 7, 1, 8),
    _AdGenMuxPMultiFibreChannelProtPairLastProvError_Type()
)
adGenMuxPMultiFibreChannelProtPairLastProvError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMuxPMultiFibreChannelProtPairLastProvError.setStatus("current")


class _AdGenMuxPMultiFibreChannelProtPairOperStatus_Type(Integer32):
    """Custom type adGenMuxPMultiFibreChannelProtPairOperStatus based on Integer32"""
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


_AdGenMuxPMultiFibreChannelProtPairOperStatus_Type.__name__ = "Integer32"
_AdGenMuxPMultiFibreChannelProtPairOperStatus_Object = MibTableColumn
adGenMuxPMultiFibreChannelProtPairOperStatus = _AdGenMuxPMultiFibreChannelProtPairOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 9, 7, 1, 9),
    _AdGenMuxPMultiFibreChannelProtPairOperStatus_Type()
)
adGenMuxPMultiFibreChannelProtPairOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMuxPMultiFibreChannelProtPairOperStatus.setStatus("current")
_AdGenMuxPMultiFibreChannelProtPairStatusString_Type = DisplayString
_AdGenMuxPMultiFibreChannelProtPairStatusString_Object = MibTableColumn
adGenMuxPMultiFibreChannelProtPairStatusString = _AdGenMuxPMultiFibreChannelProtPairStatusString_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 9, 7, 1, 10),
    _AdGenMuxPMultiFibreChannelProtPairStatusString_Type()
)
adGenMuxPMultiFibreChannelProtPairStatusString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMuxPMultiFibreChannelProtPairStatusString.setStatus("current")


class _AdGenMuxPMultiFibreChannelProtPairWorkEntityStatus_Type(Integer32):
    """Custom type adGenMuxPMultiFibreChannelProtPairWorkEntityStatus based on Integer32"""
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
        *(("clear", 1),
          ("signalFaulty", 2),
          ("signalDegraded", 3),
          ("down", 4))
    )


_AdGenMuxPMultiFibreChannelProtPairWorkEntityStatus_Type.__name__ = "Integer32"
_AdGenMuxPMultiFibreChannelProtPairWorkEntityStatus_Object = MibTableColumn
adGenMuxPMultiFibreChannelProtPairWorkEntityStatus = _AdGenMuxPMultiFibreChannelProtPairWorkEntityStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 9, 7, 1, 11),
    _AdGenMuxPMultiFibreChannelProtPairWorkEntityStatus_Type()
)
adGenMuxPMultiFibreChannelProtPairWorkEntityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMuxPMultiFibreChannelProtPairWorkEntityStatus.setStatus("current")


class _AdGenMuxPMultiFibreChannelProtPairProtectEntityStatus_Type(Integer32):
    """Custom type adGenMuxPMultiFibreChannelProtPairProtectEntityStatus based on Integer32"""
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
        *(("clear", 1),
          ("signalFaulty", 2),
          ("signalDegraded", 3),
          ("down", 4))
    )


_AdGenMuxPMultiFibreChannelProtPairProtectEntityStatus_Type.__name__ = "Integer32"
_AdGenMuxPMultiFibreChannelProtPairProtectEntityStatus_Object = MibTableColumn
adGenMuxPMultiFibreChannelProtPairProtectEntityStatus = _AdGenMuxPMultiFibreChannelProtPairProtectEntityStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 9, 7, 1, 12),
    _AdGenMuxPMultiFibreChannelProtPairProtectEntityStatus_Type()
)
adGenMuxPMultiFibreChannelProtPairProtectEntityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMuxPMultiFibreChannelProtPairProtectEntityStatus.setStatus("current")
_AdGenMuxPMultiFibreChannelProtPairLastCreateErrorTable_Object = MibTable
adGenMuxPMultiFibreChannelProtPairLastCreateErrorTable = _AdGenMuxPMultiFibreChannelProtPairLastCreateErrorTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 9, 8)
)
if mibBuilder.loadTexts:
    adGenMuxPMultiFibreChannelProtPairLastCreateErrorTable.setStatus("current")
_AdGenMuxPMultiFibreChannelProtPairLastCreateErrorEntry_Object = MibTableRow
adGenMuxPMultiFibreChannelProtPairLastCreateErrorEntry = _AdGenMuxPMultiFibreChannelProtPairLastCreateErrorEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 9, 8, 1)
)
adGenMuxPMultiFibreChannelProtPairLastCreateErrorEntry.setIndexNames(
    (0, "ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
    (0, "ADTRAN-GENMUXPONDER-MIB", "adGenMuxPMultiProtGroupName"),
)
if mibBuilder.loadTexts:
    adGenMuxPMultiFibreChannelProtPairLastCreateErrorEntry.setStatus("current")
_AdGenMuxPMultiFibreChannelProtPairLastCreateError_Type = DisplayString
_AdGenMuxPMultiFibreChannelProtPairLastCreateError_Object = MibTableColumn
adGenMuxPMultiFibreChannelProtPairLastCreateError = _AdGenMuxPMultiFibreChannelProtPairLastCreateError_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 9, 8, 1, 1),
    _AdGenMuxPMultiFibreChannelProtPairLastCreateError_Type()
)
adGenMuxPMultiFibreChannelProtPairLastCreateError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMuxPMultiFibreChannelProtPairLastCreateError.setStatus("current")
_AdGenMuxPAlarm_ObjectIdentity = ObjectIdentity
adGenMuxPAlarm = _AdGenMuxPAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 100)
)
_AdGenMuxPAlarmEvents_ObjectIdentity = ObjectIdentity
adGenMuxPAlarmEvents = _AdGenMuxPAlarmEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 100, 0)
)

# Managed Objects groups


# Notification objects

adGenMuxPTimingPriSrcFailClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 5, 3, 0, 2)
)
adGenMuxPTimingPriSrcFailClear.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-TAeSCUEXT1-MIB", "adTAeSCUTrapAlarmLevel"))
)
if mibBuilder.loadTexts:
    adGenMuxPTimingPriSrcFailClear.setStatus(
        "current"
    )

adGenMuxPTimingPriSrcFailSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 5, 3, 0, 3)
)
adGenMuxPTimingPriSrcFailSet.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-TAeSCUEXT1-MIB", "adTAeSCUTrapAlarmLevel"))
)
if mibBuilder.loadTexts:
    adGenMuxPTimingPriSrcFailSet.setStatus(
        "current"
    )

adGenMuxPTimingSecSrcFailClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 5, 3, 0, 4)
)
adGenMuxPTimingSecSrcFailClear.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-TAeSCUEXT1-MIB", "adTAeSCUTrapAlarmLevel"))
)
if mibBuilder.loadTexts:
    adGenMuxPTimingSecSrcFailClear.setStatus(
        "current"
    )

adGenMuxPTimingSecSrcFailSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 5, 3, 0, 5)
)
adGenMuxPTimingSecSrcFailSet.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-TAeSCUEXT1-MIB", "adTAeSCUTrapAlarmLevel"))
)
if mibBuilder.loadTexts:
    adGenMuxPTimingSecSrcFailSet.setStatus(
        "current"
    )

adGenMuxPTimingHoldoverClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 5, 3, 0, 6)
)
adGenMuxPTimingHoldoverClear.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-TAeSCUEXT1-MIB", "adTAeSCUTrapAlarmLevel"))
)
if mibBuilder.loadTexts:
    adGenMuxPTimingHoldoverClear.setStatus(
        "current"
    )

adGenMuxPTimingHoldoverSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 5, 3, 0, 7)
)
adGenMuxPTimingHoldoverSet.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-TAeSCUEXT1-MIB", "adTAeSCUTrapAlarmLevel"))
)
if mibBuilder.loadTexts:
    adGenMuxPTimingHoldoverSet.setStatus(
        "current"
    )

adGenMuxPLFDClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 100, 0, 1)
)
adGenMuxPLFDClear.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENMUXPONDER-MIB", "adGenMuxPMappingType"))
)
if mibBuilder.loadTexts:
    adGenMuxPLFDClear.setStatus(
        "current"
    )

adGenMuxPLFDSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 100, 0, 2)
)
adGenMuxPLFDSet.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENMUXPONDER-MIB", "adGenMuxPMappingType"))
)
if mibBuilder.loadTexts:
    adGenMuxPLFDSet.setStatus(
        "current"
    )

adGenMuxPUPMClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 100, 0, 3)
)
adGenMuxPUPMClear.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-TAeSCUEXT1-MIB", "adTAeSCUTrapAlarmLevel"),
        ("ADTRAN-GENMUXPONDER-MIB", "adGenMuxPMappingType"))
)
if mibBuilder.loadTexts:
    adGenMuxPUPMClear.setStatus(
        "current"
    )

adGenMuxPUPMSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 26, 100, 0, 4)
)
adGenMuxPUPMSet.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-TAeSCUEXT1-MIB", "adTAeSCUTrapAlarmLevel"),
        ("ADTRAN-GENMUXPONDER-MIB", "adGenMuxPMappingType"))
)
if mibBuilder.loadTexts:
    adGenMuxPUPMSet.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ADTRAN-GENMUXPONDER-MIB",
    **{"MuxPPayloadTypes": MuxPPayloadTypes,
       "MuxPMapInterface": MuxPMapInterface,
       "EthernetPayloadTypes": EthernetPayloadTypes,
       "FibreChanPayloadTypes": FibreChanPayloadTypes,
       "adGenMuxPPhysIfProv": adGenMuxPPhysIfProv,
       "adGenMuxPPhysIfProvTable": adGenMuxPPhysIfProvTable,
       "adGenMuxPPhysIfProvEntry": adGenMuxPPhysIfProvEntry,
       "adGenMuxPPhysIfType": adGenMuxPPhysIfType,
       "adGenMuxPPeerIpAddress": adGenMuxPPeerIpAddress,
       "adGenMuxPPeerChassisId": adGenMuxPPeerChassisId,
       "adGenMuxPPeerPortId": adGenMuxPPeerPortId,
       "adGenMuxPFacilityLoopbackEnable": adGenMuxPFacilityLoopbackEnable,
       "adGenMuxPFacilityLoopbackTimeout": adGenMuxPFacilityLoopbackTimeout,
       "adGenMuxPFacilityLoopbackTimeRemaining": adGenMuxPFacilityLoopbackTimeRemaining,
       "adGenMuxPTerminalLoopbackEnable": adGenMuxPTerminalLoopbackEnable,
       "adGenMuxPTerminalLoopbackTimeout": adGenMuxPTerminalLoopbackTimeout,
       "adGenMuxPTerminalLoopbackTimeRemaining": adGenMuxPTerminalLoopbackTimeRemaining,
       "adGenMuxPYCableEnable": adGenMuxPYCableEnable,
       "adGenMuxPProtectedPairEnable": adGenMuxPProtectedPairEnable,
       "adGenMuxPForwardingGroupLimitedEnable": adGenMuxPForwardingGroupLimitedEnable,
       "adGenMuxPCrossConnectProv": adGenMuxPCrossConnectProv,
       "adGenMuxPCrossConnectTable": adGenMuxPCrossConnectTable,
       "adGenMuxPCrossConnectEntry": adGenMuxPCrossConnectEntry,
       "adGenMuxPCrossConnectName": adGenMuxPCrossConnectName,
       "adGenMuxPCrossConnectType": adGenMuxPCrossConnectType,
       "adGenMuxPCrossConnectSrcType": adGenMuxPCrossConnectSrcType,
       "adGenMuxPCrossConnectSrcIfIndex": adGenMuxPCrossConnectSrcIfIndex,
       "adGenMuxPCrossConnectDstType": adGenMuxPCrossConnectDstType,
       "adGenMuxPCrossConnectDstIfIndex": adGenMuxPCrossConnectDstIfIndex,
       "adGenMuxPCrossConnectRowStatus": adGenMuxPCrossConnectRowStatus,
       "adGenMuxPCrossConnectLastProvError": adGenMuxPCrossConnectLastProvError,
       "adGenMuxPCrossConnectLastCreateErrorTable": adGenMuxPCrossConnectLastCreateErrorTable,
       "adGenMuxPCrossConnectLastCreateErrorEntry": adGenMuxPCrossConnectLastCreateErrorEntry,
       "adGenMuxPCrossConnectLastCreateError": adGenMuxPCrossConnectLastCreateError,
       "adGenMuxPPortCrossConnectStatusTable": adGenMuxPPortCrossConnectStatusTable,
       "adGenMuxPPortCrossConnectStatusEntry": adGenMuxPPortCrossConnectStatusEntry,
       "adGenMuxPPortCrossConnectName": adGenMuxPPortCrossConnectName,
       "adGenMuxPPortCrossConnectStatus": adGenMuxPPortCrossConnectStatus,
       "adGenMuxPProtGroupProv": adGenMuxPProtGroupProv,
       "adGenMuxPProtGroupTable": adGenMuxPProtGroupTable,
       "adGenMuxPProtGroupEntry": adGenMuxPProtGroupEntry,
       "adGenMuxPProtGroupName": adGenMuxPProtGroupName,
       "adGenMuxPProtGroupType": adGenMuxPProtGroupType,
       "adGenMuxPProtGroupWorkingType": adGenMuxPProtGroupWorkingType,
       "adGenMuxPProtGroupWorkingIfIndex": adGenMuxPProtGroupWorkingIfIndex,
       "adGenMuxPProtGroupProtectingType": adGenMuxPProtGroupProtectingType,
       "adGenMuxPProtGroupProtectingIfIndex": adGenMuxPProtGroupProtectingIfIndex,
       "adGenMuxPProtGroupRowStatus": adGenMuxPProtGroupRowStatus,
       "adGenMuxPProtGroupLastProvError": adGenMuxPProtGroupLastProvError,
       "adGenMuxPProtGroupWorkIsOnline": adGenMuxPProtGroupWorkIsOnline,
       "adGenMuxPProtGroupSwitchCommands": adGenMuxPProtGroupSwitchCommands,
       "adGenMuxPProtGroupWorkEntityStatus": adGenMuxPProtGroupWorkEntityStatus,
       "adGenMuxPProtGroupProtectEntityStatus": adGenMuxPProtGroupProtectEntityStatus,
       "adGenMuxPProtGroupRevertiveEnable": adGenMuxPProtGroupRevertiveEnable,
       "adGenMuxPProtGroupWaitToRestoreTime": adGenMuxPProtGroupWaitToRestoreTime,
       "adGenMuxPProtGroupTxK1Request": adGenMuxPProtGroupTxK1Request,
       "adGenMuxPProtGroupTxK1RequestChannel": adGenMuxPProtGroupTxK1RequestChannel,
       "adGenMuxPProtGroupTxK2BridgeChannel": adGenMuxPProtGroupTxK2BridgeChannel,
       "adGenMuxPProtGroupTxK2APSArchitecture": adGenMuxPProtGroupTxK2APSArchitecture,
       "adGenMuxPProtGroupTxK2APSMode": adGenMuxPProtGroupTxK2APSMode,
       "adGenMuxPProtGroupRxK1Request": adGenMuxPProtGroupRxK1Request,
       "adGenMuxPProtGroupRxK1RequestChannel": adGenMuxPProtGroupRxK1RequestChannel,
       "adGenMuxPProtGroupRxK2BridgeChannel": adGenMuxPProtGroupRxK2BridgeChannel,
       "adGenMuxPProtGroupRxK2APSArchitecture": adGenMuxPProtGroupRxK2APSArchitecture,
       "adGenMuxPProtGroupRxK2APSMode": adGenMuxPProtGroupRxK2APSMode,
       "adGenMuxPProtGroupOperStatus": adGenMuxPProtGroupOperStatus,
       "adGenMuxPProtGroupStatusString": adGenMuxPProtGroupStatusString,
       "adGenMuxPProtGroupWaitToRestoreRemainingTime": adGenMuxPProtGroupWaitToRestoreRemainingTime,
       "adGenMuxPProtGroupLastCreateErrorTable": adGenMuxPProtGroupLastCreateErrorTable,
       "adGenMuxPProtGroupLastCreateErrorEntry": adGenMuxPProtGroupLastCreateErrorEntry,
       "adGenMuxPProtGroupLastCreateError": adGenMuxPProtGroupLastCreateError,
       "adGenMuxPEthernetProtGroupTable": adGenMuxPEthernetProtGroupTable,
       "adGenMuxPEthernetProtGroupEntry": adGenMuxPEthernetProtGroupEntry,
       "adGenMuxPEthernetProtGroupName": adGenMuxPEthernetProtGroupName,
       "adGenMuxPEthernetProtGroupType": adGenMuxPEthernetProtGroupType,
       "adGenMuxPEthernetProtGroupWorkingType": adGenMuxPEthernetProtGroupWorkingType,
       "adGenMuxPEthernetProtGroupWorkingIfIndex": adGenMuxPEthernetProtGroupWorkingIfIndex,
       "adGenMuxPEthernetProtGroupProtectingType": adGenMuxPEthernetProtGroupProtectingType,
       "adGenMuxPEthernetProtGroupProtectingIfIndex": adGenMuxPEthernetProtGroupProtectingIfIndex,
       "adGenMuxPEthernetProtGroupRowStatus": adGenMuxPEthernetProtGroupRowStatus,
       "adGenMuxPEthernetProtGroupLastProvError": adGenMuxPEthernetProtGroupLastProvError,
       "adGenMuxPEthernetProtGroupOperStatus": adGenMuxPEthernetProtGroupOperStatus,
       "adGenMuxPEthernetProtGroupStatusString": adGenMuxPEthernetProtGroupStatusString,
       "adGenMuxPEthernetProtGroupWorkIsOnline": adGenMuxPEthernetProtGroupWorkIsOnline,
       "adGenMuxPEthernetProtGroupSwitchCommands": adGenMuxPEthernetProtGroupSwitchCommands,
       "adGenMuxPEthernetProtGroupWorkEntityStatus": adGenMuxPEthernetProtGroupWorkEntityStatus,
       "adGenMuxPEthernetProtGroupProtectEntityStatus": adGenMuxPEthernetProtGroupProtectEntityStatus,
       "adGenMuxPEthernetProtGroupRevertiveEnable": adGenMuxPEthernetProtGroupRevertiveEnable,
       "adGenMuxPEthernetProtGroupWaitToRestoreTime": adGenMuxPEthernetProtGroupWaitToRestoreTime,
       "adGenMuxPEthernetProtGroupWaitToRestoreRemainingTime": adGenMuxPEthernetProtGroupWaitToRestoreRemainingTime,
       "adGenMuxPEthernetProtGroupLastCreateErrorTable": adGenMuxPEthernetProtGroupLastCreateErrorTable,
       "adGenMuxPEthernetProtGroupLastCreateErrorEntry": adGenMuxPEthernetProtGroupLastCreateErrorEntry,
       "adGenMuxPEthernetProtGroupLastCreateError": adGenMuxPEthernetProtGroupLastCreateError,
       "adGenMuxPLagGroupProv": adGenMuxPLagGroupProv,
       "adGenMuxPLagGroupTable": adGenMuxPLagGroupTable,
       "adGenMuxPLagGroupEntry": adGenMuxPLagGroupEntry,
       "adGenMuxPLagGroupRowStatus": adGenMuxPLagGroupRowStatus,
       "adGenMuxPLagGroupOperStatus": adGenMuxPLagGroupOperStatus,
       "adGenMuxPLagGroupNumber": adGenMuxPLagGroupNumber,
       "adGenMuxPLagGroupName": adGenMuxPLagGroupName,
       "adGenMuxPLagGroupMaxNumCfgLinks": adGenMuxPLagGroupMaxNumCfgLinks,
       "adGenMuxPLagGroupNumCfgLinks": adGenMuxPLagGroupNumCfgLinks,
       "adGenMuxPLagGroupMinNumActLinks": adGenMuxPLagGroupMinNumActLinks,
       "adGenMuxPLagGroupNumActLinks": adGenMuxPLagGroupNumActLinks,
       "adGenMuxPLagGroupLastChange": adGenMuxPLagGroupLastChange,
       "adGenMuxPLagGroupLastError": adGenMuxPLagGroupLastError,
       "adGenMuxPLagGroupMinActLinkAlarmEnable": adGenMuxPLagGroupMinActLinkAlarmEnable,
       "adGenMuxPLagGroupLastCreateErrorTable": adGenMuxPLagGroupLastCreateErrorTable,
       "adGenMuxPLagGroupLastCreateErrorEntry": adGenMuxPLagGroupLastCreateErrorEntry,
       "adGenMuxPLagGroupLastCreateError": adGenMuxPLagGroupLastCreateError,
       "adGenMuxPLagPortMapTable": adGenMuxPLagPortMapTable,
       "adGenMuxPLagPortMapEntry": adGenMuxPLagPortMapEntry,
       "adGenMuxPLagPortMapPort": adGenMuxPLagPortMapPort,
       "adGenMuxPLagPortMapRowStatus": adGenMuxPLagPortMapRowStatus,
       "adGenMuxPLagPortMapOperStatus": adGenMuxPLagPortMapOperStatus,
       "adGenMuxPLagPortMapLagNumber": adGenMuxPLagPortMapLagNumber,
       "adGenMuxPLagPortMapPortNumber": adGenMuxPLagPortMapPortNumber,
       "adGenMuxPLagPortMapLastChange": adGenMuxPLagPortMapLastChange,
       "adGenMuxPLagPortMapLastError": adGenMuxPLagPortMapLastError,
       "adGenMuxPLagPortMapLastCreateErrorTable": adGenMuxPLagPortMapLastCreateErrorTable,
       "adGenMuxPLagPortMapLastCreateErrorEntry": adGenMuxPLagPortMapLastCreateErrorEntry,
       "adGenMuxPLagPortMapLastCreateError": adGenMuxPLagPortMapLastCreateError,
       "adGenMuxPLagPortStatusTable": adGenMuxPLagPortStatusTable,
       "adGenMuxPLagPortStatusEntry": adGenMuxPLagPortStatusEntry,
       "adGenMuxPLagPortStatusLagIfIndex": adGenMuxPLagPortStatusLagIfIndex,
       "adGenMuxPLagPortStatusOperStatus": adGenMuxPLagPortStatusOperStatus,
       "adGenMuxPTiming": adGenMuxPTiming,
       "adGenMuxPTimingProv": adGenMuxPTimingProv,
       "adGenMuxPTimingProvTable": adGenMuxPTimingProvTable,
       "adGenMuxPTimingProvEntry": adGenMuxPTimingProvEntry,
       "adGenMuxPTimingPrimarySourceSelection": adGenMuxPTimingPrimarySourceSelection,
       "adGenMuxPTimingPrimarySourceInterface": adGenMuxPTimingPrimarySourceInterface,
       "adGenMuxPTimingSecondarySourceSelection": adGenMuxPTimingSecondarySourceSelection,
       "adGenMuxPTimingSecondarySourceInterface": adGenMuxPTimingSecondarySourceInterface,
       "adGenMuxPTimingAlarmEnablePrimaryFailed": adGenMuxPTimingAlarmEnablePrimaryFailed,
       "adGenMuxPTimingAlarmEnableSecondaryFailed": adGenMuxPTimingAlarmEnableSecondaryFailed,
       "adGenMuxPTimingAlarmEnableHoldover": adGenMuxPTimingAlarmEnableHoldover,
       "adGenMuxPTimingReceiveSSMEnable": adGenMuxPTimingReceiveSSMEnable,
       "adGenMuxPTimingForceClockFailover": adGenMuxPTimingForceClockFailover,
       "adGenMuxPTimingRevertiveSwitchType": adGenMuxPTimingRevertiveSwitchType,
       "adGenMuxPTimingLastError": adGenMuxPTimingLastError,
       "adGenMuxPTimingSystemTimingType": adGenMuxPTimingSystemTimingType,
       "adGenMuxPTimingProvPortTable": adGenMuxPTimingProvPortTable,
       "adGenMuxPTimingProvPortEntry": adGenMuxPTimingProvPortEntry,
       "adGenMuxPTimingTransmitSSMEnable": adGenMuxPTimingTransmitSSMEnable,
       "adGenMuxPTimingEsmcType": adGenMuxPTimingEsmcType,
       "adGenMuxPTimingStatus": adGenMuxPTimingStatus,
       "adGenMuxPTimingStatusTable": adGenMuxPTimingStatusTable,
       "adGenMuxPTimingStatusEntry": adGenMuxPTimingStatusEntry,
       "adGenMuxPTimingCurrentSourceType": adGenMuxPTimingCurrentSourceType,
       "adGenMuxPTimingPrimarySourceHealth": adGenMuxPTimingPrimarySourceHealth,
       "adGenMuxPTimingSecondarySourceHealth": adGenMuxPTimingSecondarySourceHealth,
       "adGenMuxPTimingPrimarySourceRxSSM": adGenMuxPTimingPrimarySourceRxSSM,
       "adGenMuxPTimingSecondarySourceRxSSM": adGenMuxPTimingSecondarySourceRxSSM,
       "adGenMuxPTimingTxSSM1": adGenMuxPTimingTxSSM1,
       "adGenMuxPTimingTxSSM2": adGenMuxPTimingTxSSM2,
       "adGenMuxPTimingAlarmPrefix": adGenMuxPTimingAlarmPrefix,
       "adGenMuxPTimingAlarms": adGenMuxPTimingAlarms,
       "adGenMuxPTimingPriSrcFailClear": adGenMuxPTimingPriSrcFailClear,
       "adGenMuxPTimingPriSrcFailSet": adGenMuxPTimingPriSrcFailSet,
       "adGenMuxPTimingSecSrcFailClear": adGenMuxPTimingSecSrcFailClear,
       "adGenMuxPTimingSecSrcFailSet": adGenMuxPTimingSecSrcFailSet,
       "adGenMuxPTimingHoldoverClear": adGenMuxPTimingHoldoverClear,
       "adGenMuxPTimingHoldoverSet": adGenMuxPTimingHoldoverSet,
       "adGenMuxPPhysPeerProv": adGenMuxPPhysPeerProv,
       "adGenMuxPPhysPeerProvTable": adGenMuxPPhysPeerProvTable,
       "adGenMuxPPhysPeerProvEntry": adGenMuxPPhysPeerProvEntry,
       "adGenMuxPPhysPeerOneIpAddressTx": adGenMuxPPhysPeerOneIpAddressTx,
       "adGenMuxPPhysPeerOneIpAddressRx": adGenMuxPPhysPeerOneIpAddressRx,
       "adGenMuxPPhysPeerOneChassisIdTx": adGenMuxPPhysPeerOneChassisIdTx,
       "adGenMuxPPhysPeerOneChassisIdRx": adGenMuxPPhysPeerOneChassisIdRx,
       "adGenMuxPPhysPeerOnePortIdTx": adGenMuxPPhysPeerOnePortIdTx,
       "adGenMuxPPhysPeerOnePortIdRx": adGenMuxPPhysPeerOnePortIdRx,
       "adGenMuxPPhysPeerTwoIpAddressTx": adGenMuxPPhysPeerTwoIpAddressTx,
       "adGenMuxPPhysPeerTwoIpAddressRx": adGenMuxPPhysPeerTwoIpAddressRx,
       "adGenMuxPPhysPeerTwoChassisIdTx": adGenMuxPPhysPeerTwoChassisIdTx,
       "adGenMuxPPhysPeerTwoChassisIdRx": adGenMuxPPhysPeerTwoChassisIdRx,
       "adGenMuxPPhysPeerTwoPortIdTx": adGenMuxPPhysPeerTwoPortIdTx,
       "adGenMuxPPhysPeerTwoPortIdRx": adGenMuxPPhysPeerTwoPortIdRx,
       "adGenMuxPIfStatus": adGenMuxPIfStatus,
       "adGenMuxPIfStatusTable": adGenMuxPIfStatusTable,
       "adGenMuxPIfStatusEntry": adGenMuxPIfStatusEntry,
       "adGenMuxPInterfacePortStatus": adGenMuxPInterfacePortStatus,
       "adGenMuxPInterfacePortProtGrpName": adGenMuxPInterfacePortProtGrpName,
       "adGenMuxPMappingProv": adGenMuxPMappingProv,
       "adGenMuxPMappingTable": adGenMuxPMappingTable,
       "adGenMuxPMappingEntry": adGenMuxPMappingEntry,
       "adGenMuxPMappingName": adGenMuxPMappingName,
       "adGenMuxPMappingType": adGenMuxPMappingType,
       "adGenMuxPMappingDirection": adGenMuxPMappingDirection,
       "adGenMuxPMappingSrcType": adGenMuxPMappingSrcType,
       "adGenMuxPMappingSrcInterface": adGenMuxPMappingSrcInterface,
       "adGenMuxPMappingDstType": adGenMuxPMappingDstType,
       "adGenMuxPMappingDstInterface": adGenMuxPMappingDstInterface,
       "adGenMuxPMappingRowStatus": adGenMuxPMappingRowStatus,
       "adGenMuxPMappingLastProvError": adGenMuxPMappingLastProvError,
       "adGenMuxPMappingOperStatus": adGenMuxPMappingOperStatus,
       "adGenMuxPMappingStatusString": adGenMuxPMappingStatusString,
       "adGenMuxPMappingLastCreateErrorTable": adGenMuxPMappingLastCreateErrorTable,
       "adGenMuxPMappingLastCreateErrorEntry": adGenMuxPMappingLastCreateErrorEntry,
       "adGenMuxPMappingLastCreateError": adGenMuxPMappingLastCreateError,
       "adGenMuxPPortMappingStatusTable": adGenMuxPPortMappingStatusTable,
       "adGenMuxPPortMappingStatusEntry": adGenMuxPPortMappingStatusEntry,
       "adGenMuxPPortMappingName": adGenMuxPPortMappingName,
       "adGenMuxPPortMappingStatus": adGenMuxPPortMappingStatus,
       "adGenMuxPMultiProtGroupProv": adGenMuxPMultiProtGroupProv,
       "adGenMuxPMultiProtGroupTable": adGenMuxPMultiProtGroupTable,
       "adGenMuxPMultiProtGroupEntry": adGenMuxPMultiProtGroupEntry,
       "adGenMuxPMultiProtGroupName": adGenMuxPMultiProtGroupName,
       "adGenMuxPMultiProtGroupRowStatus": adGenMuxPMultiProtGroupRowStatus,
       "adGenMuxPMultiProtGroupLastProvError": adGenMuxPMultiProtGroupLastProvError,
       "adGenMuxPMultiProtGroupOperStatus": adGenMuxPMultiProtGroupOperStatus,
       "adGenMuxPMultiProtGroupStatusString": adGenMuxPMultiProtGroupStatusString,
       "adGenMuxPMultiProtGroupWorkIsOnline": adGenMuxPMultiProtGroupWorkIsOnline,
       "adGenMuxPMultiProtGroupSwitchCommands": adGenMuxPMultiProtGroupSwitchCommands,
       "adGenMuxPMultiProtGroupRevertiveEnable": adGenMuxPMultiProtGroupRevertiveEnable,
       "adGenMuxPMultiProtGroupWaitToRestoreTime": adGenMuxPMultiProtGroupWaitToRestoreTime,
       "adGenMuxPMultiProtGroupLastCreateErrorTable": adGenMuxPMultiProtGroupLastCreateErrorTable,
       "adGenMuxPMultiProtGroupLastCreateErrorEntry": adGenMuxPMultiProtGroupLastCreateErrorEntry,
       "adGenMuxPMultiProtGroupLastCreateError": adGenMuxPMultiProtGroupLastCreateError,
       "adGenMuxPMultiSonetProtPairTable": adGenMuxPMultiSonetProtPairTable,
       "adGenMuxPMultiSonetProtPairEntry": adGenMuxPMultiSonetProtPairEntry,
       "adGenMuxPMultiSonetProtPairName": adGenMuxPMultiSonetProtPairName,
       "adGenMuxPMultiSonetProtPairType": adGenMuxPMultiSonetProtPairType,
       "adGenMuxPMultiSonetProtPairWorkingType": adGenMuxPMultiSonetProtPairWorkingType,
       "adGenMuxPMultiSonetProtPairWorkingIfIndex": adGenMuxPMultiSonetProtPairWorkingIfIndex,
       "adGenMuxPMultiSonetProtPairProtectingType": adGenMuxPMultiSonetProtPairProtectingType,
       "adGenMuxPMultiSonetProtPairProtectingIfIndex": adGenMuxPMultiSonetProtPairProtectingIfIndex,
       "adGenMuxPMultiSonetProtPairRowStatus": adGenMuxPMultiSonetProtPairRowStatus,
       "adGenMuxPMultiSonetProtPairLastProvError": adGenMuxPMultiSonetProtPairLastProvError,
       "adGenMuxPMultiSonetProtPairWorkEntityStatus": adGenMuxPMultiSonetProtPairWorkEntityStatus,
       "adGenMuxPMultiSonetProtPairProtectEntityStatus": adGenMuxPMultiSonetProtPairProtectEntityStatus,
       "adGenMuxPMultiSonetProtPairTxK1Request": adGenMuxPMultiSonetProtPairTxK1Request,
       "adGenMuxPMultiSonetProtPairTxK1RequestChannel": adGenMuxPMultiSonetProtPairTxK1RequestChannel,
       "adGenMuxPMultiSonetProtPairTxK2BridgeChannel": adGenMuxPMultiSonetProtPairTxK2BridgeChannel,
       "adGenMuxPMultiSonetProtPairTxK2APSArchitecture": adGenMuxPMultiSonetProtPairTxK2APSArchitecture,
       "adGenMuxPMultiSonetProtPairTxK2APSMode": adGenMuxPMultiSonetProtPairTxK2APSMode,
       "adGenMuxPMultiSonetProtPairRxK1Request": adGenMuxPMultiSonetProtPairRxK1Request,
       "adGenMuxPMultiSonetProtPairRxK1RequestChannel": adGenMuxPMultiSonetProtPairRxK1RequestChannel,
       "adGenMuxPMultiSonetProtPairRxK2BridgeChannel": adGenMuxPMultiSonetProtPairRxK2BridgeChannel,
       "adGenMuxPMultiSonetProtPairRxK2APSArchitecture": adGenMuxPMultiSonetProtPairRxK2APSArchitecture,
       "adGenMuxPMultiSonetProtPairRxK2APSMode": adGenMuxPMultiSonetProtPairRxK2APSMode,
       "adGenMuxPMultiSonetProtPairOperStatus": adGenMuxPMultiSonetProtPairOperStatus,
       "adGenMuxPMultiSonetProtPairStatusString": adGenMuxPMultiSonetProtPairStatusString,
       "adGenMuxPMultiSonetProtPairLastCreateErrorTable": adGenMuxPMultiSonetProtPairLastCreateErrorTable,
       "adGenMuxPMultiSonetProtPairLastCreateErrorEntry": adGenMuxPMultiSonetProtPairLastCreateErrorEntry,
       "adGenMuxPMultiSonetProtPairLastCreateError": adGenMuxPMultiSonetProtPairLastCreateError,
       "adGenMuxPMultiEthernetProtPairTable": adGenMuxPMultiEthernetProtPairTable,
       "adGenMuxPMultiEthernetProtPairEntry": adGenMuxPMultiEthernetProtPairEntry,
       "adGenMuxPMultiEthernetProtPairName": adGenMuxPMultiEthernetProtPairName,
       "adGenMuxPMultiEthernetProtPairType": adGenMuxPMultiEthernetProtPairType,
       "adGenMuxPMultiEthernetProtPairWorkingType": adGenMuxPMultiEthernetProtPairWorkingType,
       "adGenMuxPMultiEthernetProtPairWorkingIfIndex": adGenMuxPMultiEthernetProtPairWorkingIfIndex,
       "adGenMuxPMultiEthernetProtPairProtectingType": adGenMuxPMultiEthernetProtPairProtectingType,
       "adGenMuxPMultiEthernetProtPairProtectingIfIndex": adGenMuxPMultiEthernetProtPairProtectingIfIndex,
       "adGenMuxPMultiEthernetProtPairRowStatus": adGenMuxPMultiEthernetProtPairRowStatus,
       "adGenMuxPMultiEthernetProtPairLastProvError": adGenMuxPMultiEthernetProtPairLastProvError,
       "adGenMuxPMultiEthernetProtPairOperStatus": adGenMuxPMultiEthernetProtPairOperStatus,
       "adGenMuxPMultiEthernetProtPairStatusString": adGenMuxPMultiEthernetProtPairStatusString,
       "adGenMuxPMultiEthernetProtPairWorkEntityStatus": adGenMuxPMultiEthernetProtPairWorkEntityStatus,
       "adGenMuxPMultiEthernetProtPairProtectEntityStatus": adGenMuxPMultiEthernetProtPairProtectEntityStatus,
       "adGenMuxPMultiEthernetProtPairLastCreateErrorTable": adGenMuxPMultiEthernetProtPairLastCreateErrorTable,
       "adGenMuxPMultiEthernetProtPairLastCreateErrorEntry": adGenMuxPMultiEthernetProtPairLastCreateErrorEntry,
       "adGenMuxPMultiEthernetProtPairLastCreateError": adGenMuxPMultiEthernetProtPairLastCreateError,
       "adGenMuxPMultiFibreChannelProtPairTable": adGenMuxPMultiFibreChannelProtPairTable,
       "adGenMuxPMultiFibreChannelProtPairEntry": adGenMuxPMultiFibreChannelProtPairEntry,
       "adGenMuxPMultiFibreChannelProtPairName": adGenMuxPMultiFibreChannelProtPairName,
       "adGenMuxPMultiFibreChannelProtPairType": adGenMuxPMultiFibreChannelProtPairType,
       "adGenMuxPMultiFibreChannelProtPairWorkingType": adGenMuxPMultiFibreChannelProtPairWorkingType,
       "adGenMuxPMultiFibreChannelProtPairWorkingIfIndex": adGenMuxPMultiFibreChannelProtPairWorkingIfIndex,
       "adGenMuxPMultiFibreChannelProtPairProtectingType": adGenMuxPMultiFibreChannelProtPairProtectingType,
       "adGenMuxPMultiFibreChannelProtPairProtectingIfIndex": adGenMuxPMultiFibreChannelProtPairProtectingIfIndex,
       "adGenMuxPMultiFibreChannelProtPairRowStatus": adGenMuxPMultiFibreChannelProtPairRowStatus,
       "adGenMuxPMultiFibreChannelProtPairLastProvError": adGenMuxPMultiFibreChannelProtPairLastProvError,
       "adGenMuxPMultiFibreChannelProtPairOperStatus": adGenMuxPMultiFibreChannelProtPairOperStatus,
       "adGenMuxPMultiFibreChannelProtPairStatusString": adGenMuxPMultiFibreChannelProtPairStatusString,
       "adGenMuxPMultiFibreChannelProtPairWorkEntityStatus": adGenMuxPMultiFibreChannelProtPairWorkEntityStatus,
       "adGenMuxPMultiFibreChannelProtPairProtectEntityStatus": adGenMuxPMultiFibreChannelProtPairProtectEntityStatus,
       "adGenMuxPMultiFibreChannelProtPairLastCreateErrorTable": adGenMuxPMultiFibreChannelProtPairLastCreateErrorTable,
       "adGenMuxPMultiFibreChannelProtPairLastCreateErrorEntry": adGenMuxPMultiFibreChannelProtPairLastCreateErrorEntry,
       "adGenMuxPMultiFibreChannelProtPairLastCreateError": adGenMuxPMultiFibreChannelProtPairLastCreateError,
       "adGenMuxPAlarm": adGenMuxPAlarm,
       "adGenMuxPAlarmEvents": adGenMuxPAlarmEvents,
       "adGenMuxPLFDClear": adGenMuxPLFDClear,
       "adGenMuxPLFDSet": adGenMuxPLFDSet,
       "adGenMuxPUPMClear": adGenMuxPUPMClear,
       "adGenMuxPUPMSet": adGenMuxPUPMSet,
       "adGenMuxponderIdentity": adGenMuxponderIdentity}
)
