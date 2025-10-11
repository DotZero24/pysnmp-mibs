# SNMP MIB module (IPAD-IPSTART-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/zhone/IPAD-IPSTART-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:11:24 2025
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

(ipadPPP,
 ipadServiceIndex,
 ipadTrapsPrefix) = mibBuilder.importSymbols(
    "IPADv2-MIB",
    "ipadPPP",
    "ipadServiceIndex",
    "ipadTrapsPrefix")

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

ipadIPStart = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 7, 4)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_IpadPPPStartTable_Object = MibTable
ipadPPPStartTable = _IpadPPPStartTable_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 7, 4, 1)
)
if mibBuilder.loadTexts:
    ipadPPPStartTable.setStatus("current")
_IpadPPPStartTableEntry_Object = MibTableRow
ipadPPPStartTableEntry = _IpadPPPStartTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 7, 4, 1, 1)
)
ipadPPPStartTableEntry.setIndexNames(
    (0, "IPAD-IPSTART-MIB", "ipadPPPStartService"),
)
if mibBuilder.loadTexts:
    ipadPPPStartTableEntry.setStatus("current")
_IpadPPPStartService_Type = Integer32
_IpadPPPStartService_Object = MibTableColumn
ipadPPPStartService = _IpadPPPStartService_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 7, 4, 1, 1, 1),
    _IpadPPPStartService_Type()
)
ipadPPPStartService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadPPPStartService.setStatus("current")


class _IpadPPPStartLCPState_Type(Integer32):
    """Custom type ipadPPPStartLCPState based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("initial", 1),
          ("starting", 2),
          ("closed", 3),
          ("stopped", 4),
          ("closing", 5),
          ("stopping", 6),
          ("reqSent", 7),
          ("ackRcvd", 8),
          ("ackSent", 9),
          ("opened", 10))
    )


_IpadPPPStartLCPState_Type.__name__ = "Integer32"
_IpadPPPStartLCPState_Object = MibTableColumn
ipadPPPStartLCPState = _IpadPPPStartLCPState_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 7, 4, 1, 1, 2),
    _IpadPPPStartLCPState_Type()
)
ipadPPPStartLCPState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadPPPStartLCPState.setStatus("current")
_IpadPPPStartLCPStateTime_Type = Integer32
_IpadPPPStartLCPStateTime_Object = MibTableColumn
ipadPPPStartLCPStateTime = _IpadPPPStartLCPStateTime_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 7, 4, 1, 1, 3),
    _IpadPPPStartLCPStateTime_Type()
)
ipadPPPStartLCPStateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadPPPStartLCPStateTime.setStatus("current")
_IpadPPPStartLCPStateChanges_Type = Integer32
_IpadPPPStartLCPStateChanges_Object = MibTableColumn
ipadPPPStartLCPStateChanges = _IpadPPPStartLCPStateChanges_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 7, 4, 1, 1, 4),
    _IpadPPPStartLCPStateChanges_Type()
)
ipadPPPStartLCPStateChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadPPPStartLCPStateChanges.setStatus("current")
_IpadPPPStartLCPMRU_Type = Integer32
_IpadPPPStartLCPMRU_Object = MibTableColumn
ipadPPPStartLCPMRU = _IpadPPPStartLCPMRU_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 7, 4, 1, 1, 5),
    _IpadPPPStartLCPMRU_Type()
)
ipadPPPStartLCPMRU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadPPPStartLCPMRU.setStatus("current")


class _IpadPPPStartLCPAsyncCCM_Type(DisplayString):
    """Custom type ipadPPPStartLCPAsyncCCM based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4


_IpadPPPStartLCPAsyncCCM_Type.__name__ = "DisplayString"
_IpadPPPStartLCPAsyncCCM_Object = MibTableColumn
ipadPPPStartLCPAsyncCCM = _IpadPPPStartLCPAsyncCCM_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 7, 4, 1, 1, 6),
    _IpadPPPStartLCPAsyncCCM_Type()
)
ipadPPPStartLCPAsyncCCM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadPPPStartLCPAsyncCCM.setStatus("current")


class _IpadPPPStartLCPAuthProtocol_Type(Integer32):
    """Custom type ipadPPPStartLCPAuthProtocol based on Integer32"""
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
        *(("unknown", 1),
          ("other", 2),
          ("pap", 3),
          ("chap", 4),
          ("spap", 5),
          ("eap", 6))
    )


_IpadPPPStartLCPAuthProtocol_Type.__name__ = "Integer32"
_IpadPPPStartLCPAuthProtocol_Object = MibTableColumn
ipadPPPStartLCPAuthProtocol = _IpadPPPStartLCPAuthProtocol_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 7, 4, 1, 1, 7),
    _IpadPPPStartLCPAuthProtocol_Type()
)
ipadPPPStartLCPAuthProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadPPPStartLCPAuthProtocol.setStatus("current")


class _IpadPPPStartLCPQualityProtocol_Type(Integer32):
    """Custom type ipadPPPStartLCPQualityProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("other", 2),
          ("lqr", 3))
    )


_IpadPPPStartLCPQualityProtocol_Type.__name__ = "Integer32"
_IpadPPPStartLCPQualityProtocol_Object = MibTableColumn
ipadPPPStartLCPQualityProtocol = _IpadPPPStartLCPQualityProtocol_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 7, 4, 1, 1, 8),
    _IpadPPPStartLCPQualityProtocol_Type()
)
ipadPPPStartLCPQualityProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadPPPStartLCPQualityProtocol.setStatus("current")


class _IpadPPPStartLCPMagicNumber_Type(DisplayString):
    """Custom type ipadPPPStartLCPMagicNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4


_IpadPPPStartLCPMagicNumber_Type.__name__ = "DisplayString"
_IpadPPPStartLCPMagicNumber_Object = MibTableColumn
ipadPPPStartLCPMagicNumber = _IpadPPPStartLCPMagicNumber_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 7, 4, 1, 1, 9),
    _IpadPPPStartLCPMagicNumber_Type()
)
ipadPPPStartLCPMagicNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadPPPStartLCPMagicNumber.setStatus("current")


class _IpadPPPStartLCPPFC_Type(Integer32):
    """Custom type ipadPPPStartLCPPFC based on Integer32"""
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


_IpadPPPStartLCPPFC_Type.__name__ = "Integer32"
_IpadPPPStartLCPPFC_Object = MibTableColumn
ipadPPPStartLCPPFC = _IpadPPPStartLCPPFC_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 7, 4, 1, 1, 10),
    _IpadPPPStartLCPPFC_Type()
)
ipadPPPStartLCPPFC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadPPPStartLCPPFC.setStatus("current")


class _IpadPPPStartLCPACFC_Type(Integer32):
    """Custom type ipadPPPStartLCPACFC based on Integer32"""
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


_IpadPPPStartLCPACFC_Type.__name__ = "Integer32"
_IpadPPPStartLCPACFC_Object = MibTableColumn
ipadPPPStartLCPACFC = _IpadPPPStartLCPACFC_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 7, 4, 1, 1, 11),
    _IpadPPPStartLCPACFC_Type()
)
ipadPPPStartLCPACFC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadPPPStartLCPACFC.setStatus("current")


class _IpadPPPStartLCPFCSAlternatives_Type(Integer32):
    """Custom type ipadPPPStartLCPFCSAlternatives based on Integer32"""
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
        *(("unknown", 1),
          ("other", 2),
          ("nullFCS", 3),
          ("ccitt16bitFCS", 4),
          ("ccitt32bitFCS", 5))
    )


_IpadPPPStartLCPFCSAlternatives_Type.__name__ = "Integer32"
_IpadPPPStartLCPFCSAlternatives_Object = MibTableColumn
ipadPPPStartLCPFCSAlternatives = _IpadPPPStartLCPFCSAlternatives_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 7, 4, 1, 1, 12),
    _IpadPPPStartLCPFCSAlternatives_Type()
)
ipadPPPStartLCPFCSAlternatives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadPPPStartLCPFCSAlternatives.setStatus("current")
_IpadPPPStartLCPSDP_Type = Integer32
_IpadPPPStartLCPSDP_Object = MibTableColumn
ipadPPPStartLCPSDP = _IpadPPPStartLCPSDP_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 7, 4, 1, 1, 13),
    _IpadPPPStartLCPSDP_Type()
)
ipadPPPStartLCPSDP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadPPPStartLCPSDP.setStatus("current")


class _IpadPPPStartLCPCompoundFrames_Type(Integer32):
    """Custom type ipadPPPStartLCPCompoundFrames based on Integer32"""
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


_IpadPPPStartLCPCompoundFrames_Type.__name__ = "Integer32"
_IpadPPPStartLCPCompoundFrames_Object = MibTableColumn
ipadPPPStartLCPCompoundFrames = _IpadPPPStartLCPCompoundFrames_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 7, 4, 1, 1, 14),
    _IpadPPPStartLCPCompoundFrames_Type()
)
ipadPPPStartLCPCompoundFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadPPPStartLCPCompoundFrames.setStatus("current")


class _IpadPPPStartAuthState_Type(Integer32):
    """Custom type ipadPPPStartAuthState based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("initial", 1),
          ("starting", 2),
          ("closed", 3),
          ("stopped", 4),
          ("closing", 5),
          ("stopping", 6),
          ("reqSent", 7),
          ("ackRcvd", 8),
          ("ackSent", 9),
          ("opened", 10))
    )


_IpadPPPStartAuthState_Type.__name__ = "Integer32"
_IpadPPPStartAuthState_Object = MibTableColumn
ipadPPPStartAuthState = _IpadPPPStartAuthState_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 7, 4, 1, 1, 15),
    _IpadPPPStartAuthState_Type()
)
ipadPPPStartAuthState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadPPPStartAuthState.setStatus("current")
_IpadPPPStartAuthStateTime_Type = Integer32
_IpadPPPStartAuthStateTime_Object = MibTableColumn
ipadPPPStartAuthStateTime = _IpadPPPStartAuthStateTime_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 7, 4, 1, 1, 16),
    _IpadPPPStartAuthStateTime_Type()
)
ipadPPPStartAuthStateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadPPPStartAuthStateTime.setStatus("current")
_IpadPPPStartAuthStateChanges_Type = Integer32
_IpadPPPStartAuthStateChanges_Object = MibTableColumn
ipadPPPStartAuthStateChanges = _IpadPPPStartAuthStateChanges_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 7, 4, 1, 1, 17),
    _IpadPPPStartAuthStateChanges_Type()
)
ipadPPPStartAuthStateChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadPPPStartAuthStateChanges.setStatus("current")
_IpadPPPStartAuthFailureCount_Type = Integer32
_IpadPPPStartAuthFailureCount_Object = MibTableColumn
ipadPPPStartAuthFailureCount = _IpadPPPStartAuthFailureCount_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 7, 4, 1, 1, 18),
    _IpadPPPStartAuthFailureCount_Type()
)
ipadPPPStartAuthFailureCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadPPPStartAuthFailureCount.setStatus("current")


class _IpadPPPStartAuthFailureTrapEnable_Type(Integer32):
    """Custom type ipadPPPStartAuthFailureTrapEnable based on Integer32"""
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


_IpadPPPStartAuthFailureTrapEnable_Type.__name__ = "Integer32"
_IpadPPPStartAuthFailureTrapEnable_Object = MibTableColumn
ipadPPPStartAuthFailureTrapEnable = _IpadPPPStartAuthFailureTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 7, 4, 1, 1, 19),
    _IpadPPPStartAuthFailureTrapEnable_Type()
)
ipadPPPStartAuthFailureTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipadPPPStartAuthFailureTrapEnable.setStatus("current")


class _IpadPPPStartIPCPState_Type(Integer32):
    """Custom type ipadPPPStartIPCPState based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("initial", 1),
          ("starting", 2),
          ("closed", 3),
          ("stopped", 4),
          ("closing", 5),
          ("stopping", 6),
          ("reqSent", 7),
          ("ackRcvd", 8),
          ("ackSent", 9),
          ("opened", 10))
    )


_IpadPPPStartIPCPState_Type.__name__ = "Integer32"
_IpadPPPStartIPCPState_Object = MibTableColumn
ipadPPPStartIPCPState = _IpadPPPStartIPCPState_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 7, 4, 1, 1, 20),
    _IpadPPPStartIPCPState_Type()
)
ipadPPPStartIPCPState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadPPPStartIPCPState.setStatus("current")
_IpadPPPStartIPCPStateTime_Type = Integer32
_IpadPPPStartIPCPStateTime_Object = MibTableColumn
ipadPPPStartIPCPStateTime = _IpadPPPStartIPCPStateTime_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 7, 4, 1, 1, 21),
    _IpadPPPStartIPCPStateTime_Type()
)
ipadPPPStartIPCPStateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadPPPStartIPCPStateTime.setStatus("current")
_IpadPPPStartIPCPStateChanges_Type = Integer32
_IpadPPPStartIPCPStateChanges_Object = MibTableColumn
ipadPPPStartIPCPStateChanges = _IpadPPPStartIPCPStateChanges_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 7, 4, 1, 1, 22),
    _IpadPPPStartIPCPStateChanges_Type()
)
ipadPPPStartIPCPStateChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadPPPStartIPCPStateChanges.setStatus("current")
_IpadPPPStartIPCPIPSource_Type = IpAddress
_IpadPPPStartIPCPIPSource_Object = MibTableColumn
ipadPPPStartIPCPIPSource = _IpadPPPStartIPCPIPSource_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 7, 4, 1, 1, 23),
    _IpadPPPStartIPCPIPSource_Type()
)
ipadPPPStartIPCPIPSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadPPPStartIPCPIPSource.setStatus("current")
_IpadPPPStartIPCPIPDestAddress_Type = IpAddress
_IpadPPPStartIPCPIPDestAddress_Object = MibTableColumn
ipadPPPStartIPCPIPDestAddress = _IpadPPPStartIPCPIPDestAddress_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 7, 4, 1, 1, 24),
    _IpadPPPStartIPCPIPDestAddress_Type()
)
ipadPPPStartIPCPIPDestAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadPPPStartIPCPIPDestAddress.setStatus("current")


class _IpadPPPStartIPCPCompressionProtocol_Type(Integer32):
    """Custom type ipadPPPStartIPCPCompressionProtocol based on Integer32"""
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
        *(("unknown", 1),
          ("other", 2),
          ("regularIPdata", 3),
          ("compressedTCP", 4),
          ("uncompressedTCP", 5))
    )


_IpadPPPStartIPCPCompressionProtocol_Type.__name__ = "Integer32"
_IpadPPPStartIPCPCompressionProtocol_Object = MibTableColumn
ipadPPPStartIPCPCompressionProtocol = _IpadPPPStartIPCPCompressionProtocol_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 7, 4, 1, 1, 25),
    _IpadPPPStartIPCPCompressionProtocol_Type()
)
ipadPPPStartIPCPCompressionProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadPPPStartIPCPCompressionProtocol.setStatus("current")
_IpadPPPStartLCPHistoryTable_Object = MibTable
ipadPPPStartLCPHistoryTable = _IpadPPPStartLCPHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 7, 4, 2)
)
if mibBuilder.loadTexts:
    ipadPPPStartLCPHistoryTable.setStatus("current")
_IpadPPPStartLCPHistoryTableEntry_Object = MibTableRow
ipadPPPStartLCPHistoryTableEntry = _IpadPPPStartLCPHistoryTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 7, 4, 2, 1)
)
ipadPPPStartLCPHistoryTableEntry.setIndexNames(
    (0, "IPADv2-MIB", "ipadServiceIndex"),
    (0, "IPAD-IPSTART-MIB", "ipadPPPStartLCPHistoryIndex"),
)
if mibBuilder.loadTexts:
    ipadPPPStartLCPHistoryTableEntry.setStatus("current")
_IpadPPPStartLCPHistoryIndex_Type = Integer32
_IpadPPPStartLCPHistoryIndex_Object = MibTableColumn
ipadPPPStartLCPHistoryIndex = _IpadPPPStartLCPHistoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 7, 4, 2, 1, 1),
    _IpadPPPStartLCPHistoryIndex_Type()
)
ipadPPPStartLCPHistoryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadPPPStartLCPHistoryIndex.setStatus("current")


class _IpadPPPStartLCPHistoryState_Type(Integer32):
    """Custom type ipadPPPStartLCPHistoryState based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("initial", 1),
          ("starting", 2),
          ("closed", 3),
          ("stopped", 4),
          ("closing", 5),
          ("stopping", 6),
          ("reqSent", 7),
          ("ackRcvd", 8),
          ("ackSent", 9),
          ("opened", 10))
    )


_IpadPPPStartLCPHistoryState_Type.__name__ = "Integer32"
_IpadPPPStartLCPHistoryState_Object = MibTableColumn
ipadPPPStartLCPHistoryState = _IpadPPPStartLCPHistoryState_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 7, 4, 2, 1, 2),
    _IpadPPPStartLCPHistoryState_Type()
)
ipadPPPStartLCPHistoryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadPPPStartLCPHistoryState.setStatus("current")
_IpadPPPStartLCPHistoryStateTime_Type = Integer32
_IpadPPPStartLCPHistoryStateTime_Object = MibTableColumn
ipadPPPStartLCPHistoryStateTime = _IpadPPPStartLCPHistoryStateTime_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 7, 4, 2, 1, 3),
    _IpadPPPStartLCPHistoryStateTime_Type()
)
ipadPPPStartLCPHistoryStateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadPPPStartLCPHistoryStateTime.setStatus("current")
_IpadPPPStartAuthHistoryTable_Object = MibTable
ipadPPPStartAuthHistoryTable = _IpadPPPStartAuthHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 7, 4, 3)
)
if mibBuilder.loadTexts:
    ipadPPPStartAuthHistoryTable.setStatus("current")
_IpadPPPStartAuthHistoryTableEntry_Object = MibTableRow
ipadPPPStartAuthHistoryTableEntry = _IpadPPPStartAuthHistoryTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 7, 4, 3, 1)
)
ipadPPPStartAuthHistoryTableEntry.setIndexNames(
    (0, "IPADv2-MIB", "ipadServiceIndex"),
    (0, "IPAD-IPSTART-MIB", "ipadPPPStartAuthHistoryIndex"),
)
if mibBuilder.loadTexts:
    ipadPPPStartAuthHistoryTableEntry.setStatus("current")
_IpadPPPStartAuthHistoryIndex_Type = Integer32
_IpadPPPStartAuthHistoryIndex_Object = MibTableColumn
ipadPPPStartAuthHistoryIndex = _IpadPPPStartAuthHistoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 7, 4, 3, 1, 1),
    _IpadPPPStartAuthHistoryIndex_Type()
)
ipadPPPStartAuthHistoryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadPPPStartAuthHistoryIndex.setStatus("current")


class _IpadPPPStartAuthHistoryState_Type(Integer32):
    """Custom type ipadPPPStartAuthHistoryState based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("initial", 1),
          ("starting", 2),
          ("closed", 3),
          ("stopped", 4),
          ("closing", 5),
          ("stopping", 6),
          ("reqSent", 7),
          ("ackRcvd", 8),
          ("ackSent", 9),
          ("opened", 10))
    )


_IpadPPPStartAuthHistoryState_Type.__name__ = "Integer32"
_IpadPPPStartAuthHistoryState_Object = MibTableColumn
ipadPPPStartAuthHistoryState = _IpadPPPStartAuthHistoryState_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 7, 4, 3, 1, 2),
    _IpadPPPStartAuthHistoryState_Type()
)
ipadPPPStartAuthHistoryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadPPPStartAuthHistoryState.setStatus("current")
_IpadPPPStartAuthHistoryStateTime_Type = Integer32
_IpadPPPStartAuthHistoryStateTime_Object = MibTableColumn
ipadPPPStartAuthHistoryStateTime = _IpadPPPStartAuthHistoryStateTime_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 7, 4, 3, 1, 3),
    _IpadPPPStartAuthHistoryStateTime_Type()
)
ipadPPPStartAuthHistoryStateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadPPPStartAuthHistoryStateTime.setStatus("current")
_IpadPPPStartIPCPHistoryTable_Object = MibTable
ipadPPPStartIPCPHistoryTable = _IpadPPPStartIPCPHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 7, 4, 4)
)
if mibBuilder.loadTexts:
    ipadPPPStartIPCPHistoryTable.setStatus("current")
_IpadPPPStartIPCPHistoryTableEntry_Object = MibTableRow
ipadPPPStartIPCPHistoryTableEntry = _IpadPPPStartIPCPHistoryTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 7, 4, 4, 1)
)
ipadPPPStartIPCPHistoryTableEntry.setIndexNames(
    (0, "IPADv2-MIB", "ipadServiceIndex"),
    (0, "IPAD-IPSTART-MIB", "ipadPPPStartIPCPHistoryIndex"),
)
if mibBuilder.loadTexts:
    ipadPPPStartIPCPHistoryTableEntry.setStatus("current")
_IpadPPPStartIPCPHistoryIndex_Type = Integer32
_IpadPPPStartIPCPHistoryIndex_Object = MibTableColumn
ipadPPPStartIPCPHistoryIndex = _IpadPPPStartIPCPHistoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 7, 4, 4, 1, 1),
    _IpadPPPStartIPCPHistoryIndex_Type()
)
ipadPPPStartIPCPHistoryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadPPPStartIPCPHistoryIndex.setStatus("current")


class _IpadPPPStartIPCPHistoryState_Type(Integer32):
    """Custom type ipadPPPStartIPCPHistoryState based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("initial", 1),
          ("starting", 2),
          ("closed", 3),
          ("stopped", 4),
          ("closing", 5),
          ("stopping", 6),
          ("reqSent", 7),
          ("ackRcvd", 8),
          ("ackSent", 9),
          ("opened", 10))
    )


_IpadPPPStartIPCPHistoryState_Type.__name__ = "Integer32"
_IpadPPPStartIPCPHistoryState_Object = MibTableColumn
ipadPPPStartIPCPHistoryState = _IpadPPPStartIPCPHistoryState_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 7, 4, 4, 1, 2),
    _IpadPPPStartIPCPHistoryState_Type()
)
ipadPPPStartIPCPHistoryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadPPPStartIPCPHistoryState.setStatus("current")
_IpadPPPStartIPCPHistoryStateTime_Type = Integer32
_IpadPPPStartIPCPHistoryStateTime_Object = MibTableColumn
ipadPPPStartIPCPHistoryStateTime = _IpadPPPStartIPCPHistoryStateTime_Object(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 7, 4, 4, 1, 3),
    _IpadPPPStartIPCPHistoryStateTime_Type()
)
ipadPPPStartIPCPHistoryStateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipadPPPStartIPCPHistoryStateTime.setStatus("current")

# Managed Objects groups


# Notification objects

ipadPPPStartAuthFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 321, 100, 1, 999, 0, 25050)
)
ipadPPPStartAuthFailureTrap.setObjects(
    ("IPAD-IPSTART-MIB", "ipadPPPStartAuthFailureCount")
)
if mibBuilder.loadTexts:
    ipadPPPStartAuthFailureTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IPAD-IPSTART-MIB",
    **{"ipadIPStart": ipadIPStart,
       "ipadPPPStartTable": ipadPPPStartTable,
       "ipadPPPStartTableEntry": ipadPPPStartTableEntry,
       "ipadPPPStartService": ipadPPPStartService,
       "ipadPPPStartLCPState": ipadPPPStartLCPState,
       "ipadPPPStartLCPStateTime": ipadPPPStartLCPStateTime,
       "ipadPPPStartLCPStateChanges": ipadPPPStartLCPStateChanges,
       "ipadPPPStartLCPMRU": ipadPPPStartLCPMRU,
       "ipadPPPStartLCPAsyncCCM": ipadPPPStartLCPAsyncCCM,
       "ipadPPPStartLCPAuthProtocol": ipadPPPStartLCPAuthProtocol,
       "ipadPPPStartLCPQualityProtocol": ipadPPPStartLCPQualityProtocol,
       "ipadPPPStartLCPMagicNumber": ipadPPPStartLCPMagicNumber,
       "ipadPPPStartLCPPFC": ipadPPPStartLCPPFC,
       "ipadPPPStartLCPACFC": ipadPPPStartLCPACFC,
       "ipadPPPStartLCPFCSAlternatives": ipadPPPStartLCPFCSAlternatives,
       "ipadPPPStartLCPSDP": ipadPPPStartLCPSDP,
       "ipadPPPStartLCPCompoundFrames": ipadPPPStartLCPCompoundFrames,
       "ipadPPPStartAuthState": ipadPPPStartAuthState,
       "ipadPPPStartAuthStateTime": ipadPPPStartAuthStateTime,
       "ipadPPPStartAuthStateChanges": ipadPPPStartAuthStateChanges,
       "ipadPPPStartAuthFailureCount": ipadPPPStartAuthFailureCount,
       "ipadPPPStartAuthFailureTrapEnable": ipadPPPStartAuthFailureTrapEnable,
       "ipadPPPStartIPCPState": ipadPPPStartIPCPState,
       "ipadPPPStartIPCPStateTime": ipadPPPStartIPCPStateTime,
       "ipadPPPStartIPCPStateChanges": ipadPPPStartIPCPStateChanges,
       "ipadPPPStartIPCPIPSource": ipadPPPStartIPCPIPSource,
       "ipadPPPStartIPCPIPDestAddress": ipadPPPStartIPCPIPDestAddress,
       "ipadPPPStartIPCPCompressionProtocol": ipadPPPStartIPCPCompressionProtocol,
       "ipadPPPStartLCPHistoryTable": ipadPPPStartLCPHistoryTable,
       "ipadPPPStartLCPHistoryTableEntry": ipadPPPStartLCPHistoryTableEntry,
       "ipadPPPStartLCPHistoryIndex": ipadPPPStartLCPHistoryIndex,
       "ipadPPPStartLCPHistoryState": ipadPPPStartLCPHistoryState,
       "ipadPPPStartLCPHistoryStateTime": ipadPPPStartLCPHistoryStateTime,
       "ipadPPPStartAuthHistoryTable": ipadPPPStartAuthHistoryTable,
       "ipadPPPStartAuthHistoryTableEntry": ipadPPPStartAuthHistoryTableEntry,
       "ipadPPPStartAuthHistoryIndex": ipadPPPStartAuthHistoryIndex,
       "ipadPPPStartAuthHistoryState": ipadPPPStartAuthHistoryState,
       "ipadPPPStartAuthHistoryStateTime": ipadPPPStartAuthHistoryStateTime,
       "ipadPPPStartIPCPHistoryTable": ipadPPPStartIPCPHistoryTable,
       "ipadPPPStartIPCPHistoryTableEntry": ipadPPPStartIPCPHistoryTableEntry,
       "ipadPPPStartIPCPHistoryIndex": ipadPPPStartIPCPHistoryIndex,
       "ipadPPPStartIPCPHistoryState": ipadPPPStartIPCPHistoryState,
       "ipadPPPStartIPCPHistoryStateTime": ipadPPPStartIPCPHistoryStateTime,
       "ipadPPPStartAuthFailureTrap": ipadPPPStartAuthFailureTrap}
)
