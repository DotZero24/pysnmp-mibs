# SNMP MIB module (MBG-MGMT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/meinberg/MBG-MGMT-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:07:08 2025
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

(mbgSnmpRoot,) = mibBuilder.importSymbols(
    "MBG-SNMP-ROOT-MIB",
    "mbgSnmpRoot")

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

mbgManagement = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5597, 7)
)
if mibBuilder.loadTexts:
    mbgManagement.setRevisions(
        ("2017-11-09 07:07",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class NtpTimestamp(TextualConvention, OctetString):
    status = "current"
    displayHint = "255a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(27, 27),
    )
    fixed_length = 27



class YesNo(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )



class NtpReach(TextualConvention, Integer32):
    status = "current"
    displayHint = "o"


# MIB Managed Objects in the order of their OIDs

_MbgMgmtObjects_ObjectIdentity = ObjectIdentity
mbgMgmtObjects = _MbgMgmtObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5597, 7, 1)
)
_MbgMgmtNtp_ObjectIdentity = ObjectIdentity
mbgMgmtNtp = _MbgMgmtNtp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5597, 7, 1, 1)
)
_MbgMgmtNtpConfig_ObjectIdentity = ObjectIdentity
mbgMgmtNtpConfig = _MbgMgmtNtpConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5597, 7, 1, 1, 1)
)
_MbgMgmtNtpState_ObjectIdentity = ObjectIdentity
mbgMgmtNtpState = _MbgMgmtNtpState_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5597, 7, 1, 1, 2)
)
_MbgMgmtNtpSysState_ObjectIdentity = ObjectIdentity
mbgMgmtNtpSysState = _MbgMgmtNtpSysState_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5597, 7, 1, 1, 2, 1)
)


class _MbgMgmtNtpSysStateMain_Type(Integer32):
    """Custom type mbgMgmtNtpSysStateMain based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("init", 0),
          ("sync", 1),
          ("notSync", 2),
          ("stopped", 3))
    )


_MbgMgmtNtpSysStateMain_Type.__name__ = "Integer32"
_MbgMgmtNtpSysStateMain_Object = MibScalar
mbgMgmtNtpSysStateMain = _MbgMgmtNtpSysStateMain_Object(
    (1, 3, 6, 1, 4, 1, 5597, 7, 1, 1, 2, 1, 1),
    _MbgMgmtNtpSysStateMain_Type()
)
mbgMgmtNtpSysStateMain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgMgmtNtpSysStateMain.setStatus("current")
_MbgMgmtNtpSysStateRefId_Type = DisplayString
_MbgMgmtNtpSysStateRefId_Object = MibScalar
mbgMgmtNtpSysStateRefId = _MbgMgmtNtpSysStateRefId_Object(
    (1, 3, 6, 1, 4, 1, 5597, 7, 1, 1, 2, 1, 2),
    _MbgMgmtNtpSysStateRefId_Type()
)
mbgMgmtNtpSysStateRefId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgMgmtNtpSysStateRefId.setStatus("current")


class _MbgMgmtNtpSysStateStratum_Type(Integer32):
    """Custom type mbgMgmtNtpSysStateStratum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_MbgMgmtNtpSysStateStratum_Type.__name__ = "Integer32"
_MbgMgmtNtpSysStateStratum_Object = MibScalar
mbgMgmtNtpSysStateStratum = _MbgMgmtNtpSysStateStratum_Object(
    (1, 3, 6, 1, 4, 1, 5597, 7, 1, 1, 2, 1, 3),
    _MbgMgmtNtpSysStateStratum_Type()
)
mbgMgmtNtpSysStateStratum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgMgmtNtpSysStateStratum.setStatus("current")


class _MbgMgmtNtpSysStateLeapIndicator_Type(Integer32):
    """Custom type mbgMgmtNtpSysStateLeapIndicator based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("addSecond", 1),
          ("deleteSecond", 2),
          ("alarm", 3))
    )


_MbgMgmtNtpSysStateLeapIndicator_Type.__name__ = "Integer32"
_MbgMgmtNtpSysStateLeapIndicator_Object = MibScalar
mbgMgmtNtpSysStateLeapIndicator = _MbgMgmtNtpSysStateLeapIndicator_Object(
    (1, 3, 6, 1, 4, 1, 5597, 7, 1, 1, 2, 1, 4),
    _MbgMgmtNtpSysStateLeapIndicator_Type()
)
mbgMgmtNtpSysStateLeapIndicator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgMgmtNtpSysStateLeapIndicator.setStatus("current")
_MbgMgmtNtpSysStateAssocId_Type = Unsigned32
_MbgMgmtNtpSysStateAssocId_Object = MibScalar
mbgMgmtNtpSysStateAssocId = _MbgMgmtNtpSysStateAssocId_Object(
    (1, 3, 6, 1, 4, 1, 5597, 7, 1, 1, 2, 1, 5),
    _MbgMgmtNtpSysStateAssocId_Type()
)
mbgMgmtNtpSysStateAssocId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgMgmtNtpSysStateAssocId.setStatus("current")
_MbgMgmtNtpSysStateTime_Type = NtpTimestamp
_MbgMgmtNtpSysStateTime_Object = MibScalar
mbgMgmtNtpSysStateTime = _MbgMgmtNtpSysStateTime_Object(
    (1, 3, 6, 1, 4, 1, 5597, 7, 1, 1, 2, 1, 6),
    _MbgMgmtNtpSysStateTime_Type()
)
mbgMgmtNtpSysStateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgMgmtNtpSysStateTime.setStatus("current")
_MbgMgmtNtpSysStateRootDelay_Type = Integer32
_MbgMgmtNtpSysStateRootDelay_Object = MibScalar
mbgMgmtNtpSysStateRootDelay = _MbgMgmtNtpSysStateRootDelay_Object(
    (1, 3, 6, 1, 4, 1, 5597, 7, 1, 1, 2, 1, 7),
    _MbgMgmtNtpSysStateRootDelay_Type()
)
mbgMgmtNtpSysStateRootDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgMgmtNtpSysStateRootDelay.setStatus("current")
if mibBuilder.loadTexts:
    mbgMgmtNtpSysStateRootDelay.setUnits("us")
_MbgMgmtNtpSysStateRootDispersion_Type = Integer32
_MbgMgmtNtpSysStateRootDispersion_Object = MibScalar
mbgMgmtNtpSysStateRootDispersion = _MbgMgmtNtpSysStateRootDispersion_Object(
    (1, 3, 6, 1, 4, 1, 5597, 7, 1, 1, 2, 1, 8),
    _MbgMgmtNtpSysStateRootDispersion_Type()
)
mbgMgmtNtpSysStateRootDispersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgMgmtNtpSysStateRootDispersion.setStatus("current")
if mibBuilder.loadTexts:
    mbgMgmtNtpSysStateRootDispersion.setUnits("us")
_MbgMgmtNtpRefclkStates_ObjectIdentity = ObjectIdentity
mbgMgmtNtpRefclkStates = _MbgMgmtNtpRefclkStates_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5597, 7, 1, 1, 2, 2)
)
_MbgMgmtNtpRefclkStateTable_Object = MibTable
mbgMgmtNtpRefclkStateTable = _MbgMgmtNtpRefclkStateTable_Object(
    (1, 3, 6, 1, 4, 1, 5597, 7, 1, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    mbgMgmtNtpRefclkStateTable.setStatus("current")
_MbgMgmtNtpRefclkStateTableEntry_Object = MibTableRow
mbgMgmtNtpRefclkStateTableEntry = _MbgMgmtNtpRefclkStateTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 5597, 7, 1, 1, 2, 2, 1, 1)
)
mbgMgmtNtpRefclkStateTableEntry.setIndexNames(
    (0, "MBG-MGMT-MIB", "mbgMgmtNtpRefclkStateIndex"),
)
if mibBuilder.loadTexts:
    mbgMgmtNtpRefclkStateTableEntry.setStatus("current")
_MbgMgmtNtpRefclkStateIndex_Type = Unsigned32
_MbgMgmtNtpRefclkStateIndex_Object = MibTableColumn
mbgMgmtNtpRefclkStateIndex = _MbgMgmtNtpRefclkStateIndex_Object(
    (1, 3, 6, 1, 4, 1, 5597, 7, 1, 1, 2, 2, 1, 1, 1),
    _MbgMgmtNtpRefclkStateIndex_Type()
)
mbgMgmtNtpRefclkStateIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mbgMgmtNtpRefclkStateIndex.setStatus("current")
_MbgMgmtNtpRefclkStateValid_Type = YesNo
_MbgMgmtNtpRefclkStateValid_Object = MibTableColumn
mbgMgmtNtpRefclkStateValid = _MbgMgmtNtpRefclkStateValid_Object(
    (1, 3, 6, 1, 4, 1, 5597, 7, 1, 1, 2, 2, 1, 1, 2),
    _MbgMgmtNtpRefclkStateValid_Type()
)
mbgMgmtNtpRefclkStateValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgMgmtNtpRefclkStateValid.setStatus("current")
_MbgMgmtNtpRefclkStateRefId_Type = DisplayString
_MbgMgmtNtpRefclkStateRefId_Object = MibTableColumn
mbgMgmtNtpRefclkStateRefId = _MbgMgmtNtpRefclkStateRefId_Object(
    (1, 3, 6, 1, 4, 1, 5597, 7, 1, 1, 2, 2, 1, 1, 3),
    _MbgMgmtNtpRefclkStateRefId_Type()
)
mbgMgmtNtpRefclkStateRefId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgMgmtNtpRefclkStateRefId.setStatus("current")


class _MbgMgmtNtpRefclkStateStratum_Type(Integer32):
    """Custom type mbgMgmtNtpRefclkStateStratum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_MbgMgmtNtpRefclkStateStratum_Type.__name__ = "Integer32"
_MbgMgmtNtpRefclkStateStratum_Object = MibTableColumn
mbgMgmtNtpRefclkStateStratum = _MbgMgmtNtpRefclkStateStratum_Object(
    (1, 3, 6, 1, 4, 1, 5597, 7, 1, 1, 2, 2, 1, 1, 4),
    _MbgMgmtNtpRefclkStateStratum_Type()
)
mbgMgmtNtpRefclkStateStratum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgMgmtNtpRefclkStateStratum.setStatus("current")
_MbgMgmtNtpRefclkStateReach_Type = NtpReach
_MbgMgmtNtpRefclkStateReach_Object = MibTableColumn
mbgMgmtNtpRefclkStateReach = _MbgMgmtNtpRefclkStateReach_Object(
    (1, 3, 6, 1, 4, 1, 5597, 7, 1, 1, 2, 2, 1, 1, 5),
    _MbgMgmtNtpRefclkStateReach_Type()
)
mbgMgmtNtpRefclkStateReach.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgMgmtNtpRefclkStateReach.setStatus("current")
_MbgMgmtNtpRefclkStateAssocId_Type = Integer32
_MbgMgmtNtpRefclkStateAssocId_Object = MibTableColumn
mbgMgmtNtpRefclkStateAssocId = _MbgMgmtNtpRefclkStateAssocId_Object(
    (1, 3, 6, 1, 4, 1, 5597, 7, 1, 1, 2, 2, 1, 1, 6),
    _MbgMgmtNtpRefclkStateAssocId_Type()
)
mbgMgmtNtpRefclkStateAssocId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgMgmtNtpRefclkStateAssocId.setStatus("current")
_MbgMgmtNtpRefclkStateTime_Type = NtpTimestamp
_MbgMgmtNtpRefclkStateTime_Object = MibTableColumn
mbgMgmtNtpRefclkStateTime = _MbgMgmtNtpRefclkStateTime_Object(
    (1, 3, 6, 1, 4, 1, 5597, 7, 1, 1, 2, 2, 1, 1, 7),
    _MbgMgmtNtpRefclkStateTime_Type()
)
mbgMgmtNtpRefclkStateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgMgmtNtpRefclkStateTime.setStatus("current")
_MbgMgmtNtpRefclkOffset_Type = Integer32
_MbgMgmtNtpRefclkOffset_Object = MibTableColumn
mbgMgmtNtpRefclkOffset = _MbgMgmtNtpRefclkOffset_Object(
    (1, 3, 6, 1, 4, 1, 5597, 7, 1, 1, 2, 2, 1, 1, 8),
    _MbgMgmtNtpRefclkOffset_Type()
)
mbgMgmtNtpRefclkOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgMgmtNtpRefclkOffset.setStatus("current")
if mibBuilder.loadTexts:
    mbgMgmtNtpRefclkOffset.setUnits("ns")
_MbgMgmtNtpRefclkDelay_Type = Integer32
_MbgMgmtNtpRefclkDelay_Object = MibTableColumn
mbgMgmtNtpRefclkDelay = _MbgMgmtNtpRefclkDelay_Object(
    (1, 3, 6, 1, 4, 1, 5597, 7, 1, 1, 2, 2, 1, 1, 9),
    _MbgMgmtNtpRefclkDelay_Type()
)
mbgMgmtNtpRefclkDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgMgmtNtpRefclkDelay.setStatus("current")
if mibBuilder.loadTexts:
    mbgMgmtNtpRefclkDelay.setUnits("ns")
_MbgMgmtNtpRefclkDispersion_Type = Integer32
_MbgMgmtNtpRefclkDispersion_Object = MibTableColumn
mbgMgmtNtpRefclkDispersion = _MbgMgmtNtpRefclkDispersion_Object(
    (1, 3, 6, 1, 4, 1, 5597, 7, 1, 1, 2, 2, 1, 1, 10),
    _MbgMgmtNtpRefclkDispersion_Type()
)
mbgMgmtNtpRefclkDispersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgMgmtNtpRefclkDispersion.setStatus("current")
if mibBuilder.loadTexts:
    mbgMgmtNtpRefclkDispersion.setUnits("us")
_MbgMgmtNtpRefclkJitter_Type = Integer32
_MbgMgmtNtpRefclkJitter_Object = MibTableColumn
mbgMgmtNtpRefclkJitter = _MbgMgmtNtpRefclkJitter_Object(
    (1, 3, 6, 1, 4, 1, 5597, 7, 1, 1, 2, 2, 1, 1, 11),
    _MbgMgmtNtpRefclkJitter_Type()
)
mbgMgmtNtpRefclkJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgMgmtNtpRefclkJitter.setStatus("current")
if mibBuilder.loadTexts:
    mbgMgmtNtpRefclkJitter.setUnits("us")
_MbgMgmtNtpPeerStates_ObjectIdentity = ObjectIdentity
mbgMgmtNtpPeerStates = _MbgMgmtNtpPeerStates_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5597, 7, 1, 1, 2, 3)
)
_MbgMgmtNtpPeerStateTable_Object = MibTable
mbgMgmtNtpPeerStateTable = _MbgMgmtNtpPeerStateTable_Object(
    (1, 3, 6, 1, 4, 1, 5597, 7, 1, 1, 2, 3, 1)
)
if mibBuilder.loadTexts:
    mbgMgmtNtpPeerStateTable.setStatus("current")
_MbgMgmtNtpPeerStateTableEntry_Object = MibTableRow
mbgMgmtNtpPeerStateTableEntry = _MbgMgmtNtpPeerStateTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 5597, 7, 1, 1, 2, 3, 1, 1)
)
mbgMgmtNtpPeerStateTableEntry.setIndexNames(
    (0, "MBG-MGMT-MIB", "mbgMgmtNtpPeerStateIndex"),
)
if mibBuilder.loadTexts:
    mbgMgmtNtpPeerStateTableEntry.setStatus("current")
_MbgMgmtNtpPeerStateIndex_Type = Unsigned32
_MbgMgmtNtpPeerStateIndex_Object = MibTableColumn
mbgMgmtNtpPeerStateIndex = _MbgMgmtNtpPeerStateIndex_Object(
    (1, 3, 6, 1, 4, 1, 5597, 7, 1, 1, 2, 3, 1, 1, 1),
    _MbgMgmtNtpPeerStateIndex_Type()
)
mbgMgmtNtpPeerStateIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mbgMgmtNtpPeerStateIndex.setStatus("current")
_MbgMgmtNtpPeerStateValid_Type = YesNo
_MbgMgmtNtpPeerStateValid_Object = MibTableColumn
mbgMgmtNtpPeerStateValid = _MbgMgmtNtpPeerStateValid_Object(
    (1, 3, 6, 1, 4, 1, 5597, 7, 1, 1, 2, 3, 1, 1, 2),
    _MbgMgmtNtpPeerStateValid_Type()
)
mbgMgmtNtpPeerStateValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgMgmtNtpPeerStateValid.setStatus("current")
_MbgMgmtNtpPeerStateRefId_Type = DisplayString
_MbgMgmtNtpPeerStateRefId_Object = MibTableColumn
mbgMgmtNtpPeerStateRefId = _MbgMgmtNtpPeerStateRefId_Object(
    (1, 3, 6, 1, 4, 1, 5597, 7, 1, 1, 2, 3, 1, 1, 3),
    _MbgMgmtNtpPeerStateRefId_Type()
)
mbgMgmtNtpPeerStateRefId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgMgmtNtpPeerStateRefId.setStatus("current")


class _MbgMgmtNtpPeerStateStratum_Type(Integer32):
    """Custom type mbgMgmtNtpPeerStateStratum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_MbgMgmtNtpPeerStateStratum_Type.__name__ = "Integer32"
_MbgMgmtNtpPeerStateStratum_Object = MibTableColumn
mbgMgmtNtpPeerStateStratum = _MbgMgmtNtpPeerStateStratum_Object(
    (1, 3, 6, 1, 4, 1, 5597, 7, 1, 1, 2, 3, 1, 1, 4),
    _MbgMgmtNtpPeerStateStratum_Type()
)
mbgMgmtNtpPeerStateStratum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgMgmtNtpPeerStateStratum.setStatus("current")
_MbgMgmtNtpPeerStateReach_Type = NtpReach
_MbgMgmtNtpPeerStateReach_Object = MibTableColumn
mbgMgmtNtpPeerStateReach = _MbgMgmtNtpPeerStateReach_Object(
    (1, 3, 6, 1, 4, 1, 5597, 7, 1, 1, 2, 3, 1, 1, 5),
    _MbgMgmtNtpPeerStateReach_Type()
)
mbgMgmtNtpPeerStateReach.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgMgmtNtpPeerStateReach.setStatus("current")
_MbgMgmtNtpPeerStateAssocId_Type = Integer32
_MbgMgmtNtpPeerStateAssocId_Object = MibTableColumn
mbgMgmtNtpPeerStateAssocId = _MbgMgmtNtpPeerStateAssocId_Object(
    (1, 3, 6, 1, 4, 1, 5597, 7, 1, 1, 2, 3, 1, 1, 6),
    _MbgMgmtNtpPeerStateAssocId_Type()
)
mbgMgmtNtpPeerStateAssocId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgMgmtNtpPeerStateAssocId.setStatus("current")
_MbgMgmtNtpPeerStateTime_Type = NtpTimestamp
_MbgMgmtNtpPeerStateTime_Object = MibTableColumn
mbgMgmtNtpPeerStateTime = _MbgMgmtNtpPeerStateTime_Object(
    (1, 3, 6, 1, 4, 1, 5597, 7, 1, 1, 2, 3, 1, 1, 7),
    _MbgMgmtNtpPeerStateTime_Type()
)
mbgMgmtNtpPeerStateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgMgmtNtpPeerStateTime.setStatus("current")
_MbgMgmtNtpPeerOffset_Type = Integer32
_MbgMgmtNtpPeerOffset_Object = MibTableColumn
mbgMgmtNtpPeerOffset = _MbgMgmtNtpPeerOffset_Object(
    (1, 3, 6, 1, 4, 1, 5597, 7, 1, 1, 2, 3, 1, 1, 8),
    _MbgMgmtNtpPeerOffset_Type()
)
mbgMgmtNtpPeerOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgMgmtNtpPeerOffset.setStatus("current")
if mibBuilder.loadTexts:
    mbgMgmtNtpPeerOffset.setUnits("ns")
_MbgMgmtNtpPeerDelay_Type = Integer32
_MbgMgmtNtpPeerDelay_Object = MibTableColumn
mbgMgmtNtpPeerDelay = _MbgMgmtNtpPeerDelay_Object(
    (1, 3, 6, 1, 4, 1, 5597, 7, 1, 1, 2, 3, 1, 1, 9),
    _MbgMgmtNtpPeerDelay_Type()
)
mbgMgmtNtpPeerDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgMgmtNtpPeerDelay.setStatus("current")
if mibBuilder.loadTexts:
    mbgMgmtNtpPeerDelay.setUnits("ns")
_MbgMgmtNtpPeerDispersion_Type = Integer32
_MbgMgmtNtpPeerDispersion_Object = MibTableColumn
mbgMgmtNtpPeerDispersion = _MbgMgmtNtpPeerDispersion_Object(
    (1, 3, 6, 1, 4, 1, 5597, 7, 1, 1, 2, 3, 1, 1, 10),
    _MbgMgmtNtpPeerDispersion_Type()
)
mbgMgmtNtpPeerDispersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgMgmtNtpPeerDispersion.setStatus("current")
if mibBuilder.loadTexts:
    mbgMgmtNtpPeerDispersion.setUnits("us")
_MbgMgmtNtpPeerJitter_Type = Integer32
_MbgMgmtNtpPeerJitter_Object = MibTableColumn
mbgMgmtNtpPeerJitter = _MbgMgmtNtpPeerJitter_Object(
    (1, 3, 6, 1, 4, 1, 5597, 7, 1, 1, 2, 3, 1, 1, 11),
    _MbgMgmtNtpPeerJitter_Type()
)
mbgMgmtNtpPeerJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mbgMgmtNtpPeerJitter.setStatus("current")
if mibBuilder.loadTexts:
    mbgMgmtNtpPeerJitter.setUnits("us")
_MbgMgmtNotifications_ObjectIdentity = ObjectIdentity
mbgMgmtNotifications = _MbgMgmtNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5597, 7, 2)
)
_MbgMgmtTraps_ObjectIdentity = ObjectIdentity
mbgMgmtTraps = _MbgMgmtTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5597, 7, 2, 0)
)
_MbgMgmtConformance_ObjectIdentity = ObjectIdentity
mbgMgmtConformance = _MbgMgmtConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5597, 7, 90)
)
_MbgMgmtCompliances_ObjectIdentity = ObjectIdentity
mbgMgmtCompliances = _MbgMgmtCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5597, 7, 90, 1)
)
_MbgMgmtGroups_ObjectIdentity = ObjectIdentity
mbgMgmtGroups = _MbgMgmtGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5597, 7, 90, 2)
)

# Managed Objects groups

mbgMgmtObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5597, 7, 90, 2, 1)
)
mbgMgmtObjectsGroup.setObjects(
      *(("MBG-MGMT-MIB", "mbgMgmtNtpSysStateMain"),
        ("MBG-MGMT-MIB", "mbgMgmtNtpSysStateRefId"),
        ("MBG-MGMT-MIB", "mbgMgmtNtpSysStateStratum"),
        ("MBG-MGMT-MIB", "mbgMgmtNtpSysStateLeapIndicator"),
        ("MBG-MGMT-MIB", "mbgMgmtNtpSysStateAssocId"),
        ("MBG-MGMT-MIB", "mbgMgmtNtpSysStateTime"),
        ("MBG-MGMT-MIB", "mbgMgmtNtpSysStateRootDelay"),
        ("MBG-MGMT-MIB", "mbgMgmtNtpSysStateRootDispersion"),
        ("MBG-MGMT-MIB", "mbgMgmtNtpRefclkStateValid"),
        ("MBG-MGMT-MIB", "mbgMgmtNtpRefclkStateRefId"),
        ("MBG-MGMT-MIB", "mbgMgmtNtpRefclkStateStratum"),
        ("MBG-MGMT-MIB", "mbgMgmtNtpRefclkStateReach"),
        ("MBG-MGMT-MIB", "mbgMgmtNtpRefclkStateAssocId"),
        ("MBG-MGMT-MIB", "mbgMgmtNtpRefclkStateTime"),
        ("MBG-MGMT-MIB", "mbgMgmtNtpRefclkOffset"),
        ("MBG-MGMT-MIB", "mbgMgmtNtpRefclkDelay"),
        ("MBG-MGMT-MIB", "mbgMgmtNtpRefclkDispersion"),
        ("MBG-MGMT-MIB", "mbgMgmtNtpRefclkJitter"),
        ("MBG-MGMT-MIB", "mbgMgmtNtpPeerStateValid"),
        ("MBG-MGMT-MIB", "mbgMgmtNtpPeerStateRefId"),
        ("MBG-MGMT-MIB", "mbgMgmtNtpPeerStateStratum"),
        ("MBG-MGMT-MIB", "mbgMgmtNtpPeerStateReach"),
        ("MBG-MGMT-MIB", "mbgMgmtNtpPeerStateAssocId"),
        ("MBG-MGMT-MIB", "mbgMgmtNtpPeerStateTime"),
        ("MBG-MGMT-MIB", "mbgMgmtNtpPeerOffset"),
        ("MBG-MGMT-MIB", "mbgMgmtNtpPeerDelay"),
        ("MBG-MGMT-MIB", "mbgMgmtNtpPeerDispersion"),
        ("MBG-MGMT-MIB", "mbgMgmtNtpPeerJitter"))
)
if mibBuilder.loadTexts:
    mbgMgmtObjectsGroup.setStatus("current")


# Notification objects

mbgMgmtTrapNtpMainState = NotificationType(
    (1, 3, 6, 1, 4, 1, 5597, 7, 2, 0, 1)
)
mbgMgmtTrapNtpMainState.setObjects(
      *(("MBG-MGMT-MIB", "mbgMgmtNtpSysStateMain"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    mbgMgmtTrapNtpMainState.setStatus(
        "current"
    )

mbgMgmtTrapHeartbeat = NotificationType(
    (1, 3, 6, 1, 4, 1, 5597, 7, 2, 0, 2)
)
mbgMgmtTrapHeartbeat.setObjects(
    ("SNMPv2-MIB", "sysName")
)
if mibBuilder.loadTexts:
    mbgMgmtTrapHeartbeat.setStatus(
        "current"
    )


# Notifications groups

mbgMgmtNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 5597, 7, 90, 2, 2)
)
mbgMgmtNotificationGroup.setObjects(
      *(("MBG-MGMT-MIB", "mbgMgmtTrapNtpMainState"),
        ("MBG-MGMT-MIB", "mbgMgmtTrapHeartbeat"))
)
if mibBuilder.loadTexts:
    mbgMgmtNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

mbgMgmtCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5597, 7, 90, 1, 1)
)
mbgMgmtCompliance.setObjects(
      *(("MBG-MGMT-MIB", "mbgMgmtObjectsGroup"),
        ("MBG-MGMT-MIB", "mbgMgmtNotificationGroup"))
)
if mibBuilder.loadTexts:
    mbgMgmtCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MBG-MGMT-MIB",
    **{"NtpTimestamp": NtpTimestamp,
       "YesNo": YesNo,
       "NtpReach": NtpReach,
       "mbgManagement": mbgManagement,
       "mbgMgmtObjects": mbgMgmtObjects,
       "mbgMgmtNtp": mbgMgmtNtp,
       "mbgMgmtNtpConfig": mbgMgmtNtpConfig,
       "mbgMgmtNtpState": mbgMgmtNtpState,
       "mbgMgmtNtpSysState": mbgMgmtNtpSysState,
       "mbgMgmtNtpSysStateMain": mbgMgmtNtpSysStateMain,
       "mbgMgmtNtpSysStateRefId": mbgMgmtNtpSysStateRefId,
       "mbgMgmtNtpSysStateStratum": mbgMgmtNtpSysStateStratum,
       "mbgMgmtNtpSysStateLeapIndicator": mbgMgmtNtpSysStateLeapIndicator,
       "mbgMgmtNtpSysStateAssocId": mbgMgmtNtpSysStateAssocId,
       "mbgMgmtNtpSysStateTime": mbgMgmtNtpSysStateTime,
       "mbgMgmtNtpSysStateRootDelay": mbgMgmtNtpSysStateRootDelay,
       "mbgMgmtNtpSysStateRootDispersion": mbgMgmtNtpSysStateRootDispersion,
       "mbgMgmtNtpRefclkStates": mbgMgmtNtpRefclkStates,
       "mbgMgmtNtpRefclkStateTable": mbgMgmtNtpRefclkStateTable,
       "mbgMgmtNtpRefclkStateTableEntry": mbgMgmtNtpRefclkStateTableEntry,
       "mbgMgmtNtpRefclkStateIndex": mbgMgmtNtpRefclkStateIndex,
       "mbgMgmtNtpRefclkStateValid": mbgMgmtNtpRefclkStateValid,
       "mbgMgmtNtpRefclkStateRefId": mbgMgmtNtpRefclkStateRefId,
       "mbgMgmtNtpRefclkStateStratum": mbgMgmtNtpRefclkStateStratum,
       "mbgMgmtNtpRefclkStateReach": mbgMgmtNtpRefclkStateReach,
       "mbgMgmtNtpRefclkStateAssocId": mbgMgmtNtpRefclkStateAssocId,
       "mbgMgmtNtpRefclkStateTime": mbgMgmtNtpRefclkStateTime,
       "mbgMgmtNtpRefclkOffset": mbgMgmtNtpRefclkOffset,
       "mbgMgmtNtpRefclkDelay": mbgMgmtNtpRefclkDelay,
       "mbgMgmtNtpRefclkDispersion": mbgMgmtNtpRefclkDispersion,
       "mbgMgmtNtpRefclkJitter": mbgMgmtNtpRefclkJitter,
       "mbgMgmtNtpPeerStates": mbgMgmtNtpPeerStates,
       "mbgMgmtNtpPeerStateTable": mbgMgmtNtpPeerStateTable,
       "mbgMgmtNtpPeerStateTableEntry": mbgMgmtNtpPeerStateTableEntry,
       "mbgMgmtNtpPeerStateIndex": mbgMgmtNtpPeerStateIndex,
       "mbgMgmtNtpPeerStateValid": mbgMgmtNtpPeerStateValid,
       "mbgMgmtNtpPeerStateRefId": mbgMgmtNtpPeerStateRefId,
       "mbgMgmtNtpPeerStateStratum": mbgMgmtNtpPeerStateStratum,
       "mbgMgmtNtpPeerStateReach": mbgMgmtNtpPeerStateReach,
       "mbgMgmtNtpPeerStateAssocId": mbgMgmtNtpPeerStateAssocId,
       "mbgMgmtNtpPeerStateTime": mbgMgmtNtpPeerStateTime,
       "mbgMgmtNtpPeerOffset": mbgMgmtNtpPeerOffset,
       "mbgMgmtNtpPeerDelay": mbgMgmtNtpPeerDelay,
       "mbgMgmtNtpPeerDispersion": mbgMgmtNtpPeerDispersion,
       "mbgMgmtNtpPeerJitter": mbgMgmtNtpPeerJitter,
       "mbgMgmtNotifications": mbgMgmtNotifications,
       "mbgMgmtTraps": mbgMgmtTraps,
       "mbgMgmtTrapNtpMainState": mbgMgmtTrapNtpMainState,
       "mbgMgmtTrapHeartbeat": mbgMgmtTrapHeartbeat,
       "mbgMgmtConformance": mbgMgmtConformance,
       "mbgMgmtCompliances": mbgMgmtCompliances,
       "mbgMgmtCompliance": mbgMgmtCompliance,
       "mbgMgmtGroups": mbgMgmtGroups,
       "mbgMgmtObjectsGroup": mbgMgmtObjectsGroup,
       "mbgMgmtNotificationGroup": mbgMgmtNotificationGroup}
)
