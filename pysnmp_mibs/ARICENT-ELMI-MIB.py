# SNMP MIB module (ARICENT-ELMI-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/aricent/ARICENT-ELMI-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:42:52 2025
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

futureElmiMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 159)
)
if mibBuilder.loadTexts:
    futureElmiMIB.setRevisions(
        ("2012-09-05 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class EnabledStatus(TextualConvention, Integer32):
    status = "current"
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



# MIB Managed Objects in the order of their OIDs

_FutureElmi_ObjectIdentity = ObjectIdentity
futureElmi = _FutureElmi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 159, 1)
)


class _FsElmiSystemControl_Type(Integer32):
    """Custom type fsElmiSystemControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("start", 1),
          ("shutdown", 2))
    )


_FsElmiSystemControl_Type.__name__ = "Integer32"
_FsElmiSystemControl_Object = MibScalar
fsElmiSystemControl = _FsElmiSystemControl_Object(
    (1, 3, 6, 1, 4, 1, 2076, 159, 1, 1),
    _FsElmiSystemControl_Type()
)
fsElmiSystemControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsElmiSystemControl.setStatus("current")


class _FsElmiModuleStatus_Type(EnabledStatus):
    """Custom type fsElmiModuleStatus based on EnabledStatus"""
    defaultValue = 1


_FsElmiModuleStatus_Type.__name__ = "EnabledStatus"
_FsElmiModuleStatus_Object = MibScalar
fsElmiModuleStatus = _FsElmiModuleStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 159, 1, 2),
    _FsElmiModuleStatus_Type()
)
fsElmiModuleStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsElmiModuleStatus.setStatus("current")
_FsElmiActivePortCount_Type = Counter32
_FsElmiActivePortCount_Object = MibScalar
fsElmiActivePortCount = _FsElmiActivePortCount_Object(
    (1, 3, 6, 1, 4, 1, 2076, 159, 1, 3),
    _FsElmiActivePortCount_Type()
)
fsElmiActivePortCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsElmiActivePortCount.setStatus("current")


class _FsElmiTraceOption_Type(Integer32):
    """Custom type fsElmiTraceOption based on Integer32"""
    defaultValue = 0


_FsElmiTraceOption_Type.__name__ = "Integer32"
_FsElmiTraceOption_Object = MibScalar
fsElmiTraceOption = _FsElmiTraceOption_Object(
    (1, 3, 6, 1, 4, 1, 2076, 159, 1, 4),
    _FsElmiTraceOption_Type()
)
fsElmiTraceOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsElmiTraceOption.setStatus("current")
_FsElmiBufferOverFlowCount_Type = Counter32
_FsElmiBufferOverFlowCount_Object = MibScalar
fsElmiBufferOverFlowCount = _FsElmiBufferOverFlowCount_Object(
    (1, 3, 6, 1, 4, 1, 2076, 159, 1, 5),
    _FsElmiBufferOverFlowCount_Type()
)
fsElmiBufferOverFlowCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsElmiBufferOverFlowCount.setStatus("current")
_FsElmiMemAllocFailureCount_Type = Counter32
_FsElmiMemAllocFailureCount_Object = MibScalar
fsElmiMemAllocFailureCount = _FsElmiMemAllocFailureCount_Object(
    (1, 3, 6, 1, 4, 1, 2076, 159, 1, 6),
    _FsElmiMemAllocFailureCount_Type()
)
fsElmiMemAllocFailureCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsElmiMemAllocFailureCount.setStatus("current")
_FsElmiPortTable_Object = MibTable
fsElmiPortTable = _FsElmiPortTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 159, 1, 7)
)
if mibBuilder.loadTexts:
    fsElmiPortTable.setStatus("current")
_FsElmiPortEntry_Object = MibTableRow
fsElmiPortEntry = _FsElmiPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 159, 1, 7, 1)
)
fsElmiPortEntry.setIndexNames(
    (0, "ARICENT-ELMI-MIB", "fsElmiPort"),
)
if mibBuilder.loadTexts:
    fsElmiPortEntry.setStatus("current")


class _FsElmiPort_Type(Integer32):
    """Custom type fsElmiPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_FsElmiPort_Type.__name__ = "Integer32"
_FsElmiPort_Object = MibTableColumn
fsElmiPort = _FsElmiPort_Object(
    (1, 3, 6, 1, 4, 1, 2076, 159, 1, 7, 1, 1),
    _FsElmiPort_Type()
)
fsElmiPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsElmiPort.setStatus("current")


class _FsElmiPortElmiStatus_Type(EnabledStatus):
    """Custom type fsElmiPortElmiStatus based on EnabledStatus"""
    defaultValue = 2


_FsElmiPortElmiStatus_Type.__name__ = "EnabledStatus"
_FsElmiPortElmiStatus_Object = MibTableColumn
fsElmiPortElmiStatus = _FsElmiPortElmiStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 159, 1, 7, 1, 2),
    _FsElmiPortElmiStatus_Type()
)
fsElmiPortElmiStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsElmiPortElmiStatus.setStatus("current")


class _FsElmiUniSide_Type(Integer32):
    """Custom type fsElmiUniSide based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unic", 1),
          ("unin", 2))
    )


_FsElmiUniSide_Type.__name__ = "Integer32"
_FsElmiUniSide_Object = MibTableColumn
fsElmiUniSide = _FsElmiUniSide_Object(
    (1, 3, 6, 1, 4, 1, 2076, 159, 1, 7, 1, 3),
    _FsElmiUniSide_Type()
)
fsElmiUniSide.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsElmiUniSide.setStatus("current")


class _FsElmiOperStatus_Type(EnabledStatus):
    """Custom type fsElmiOperStatus based on EnabledStatus"""
    defaultValue = 2


_FsElmiOperStatus_Type.__name__ = "EnabledStatus"
_FsElmiOperStatus_Object = MibTableColumn
fsElmiOperStatus = _FsElmiOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 159, 1, 7, 1, 4),
    _FsElmiOperStatus_Type()
)
fsElmiOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsElmiOperStatus.setStatus("current")


class _FsElmiStatusCounter_Type(Integer32):
    """Custom type fsElmiStatusCounter based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 10),
    )


_FsElmiStatusCounter_Type.__name__ = "Integer32"
_FsElmiStatusCounter_Object = MibTableColumn
fsElmiStatusCounter = _FsElmiStatusCounter_Object(
    (1, 3, 6, 1, 4, 1, 2076, 159, 1, 7, 1, 5),
    _FsElmiStatusCounter_Type()
)
fsElmiStatusCounter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsElmiStatusCounter.setStatus("current")


class _FsElmiPollingVerificationTimerValue_Type(Integer32):
    """Custom type fsElmiPollingVerificationTimerValue based on Integer32"""
    defaultValue = 15

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 30),
    )


_FsElmiPollingVerificationTimerValue_Type.__name__ = "Integer32"
_FsElmiPollingVerificationTimerValue_Object = MibTableColumn
fsElmiPollingVerificationTimerValue = _FsElmiPollingVerificationTimerValue_Object(
    (1, 3, 6, 1, 4, 1, 2076, 159, 1, 7, 1, 6),
    _FsElmiPollingVerificationTimerValue_Type()
)
fsElmiPollingVerificationTimerValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsElmiPollingVerificationTimerValue.setStatus("current")


class _FsElmiPollingTimerValue_Type(Integer32):
    """Custom type fsElmiPollingTimerValue based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 30),
    )


_FsElmiPollingTimerValue_Type.__name__ = "Integer32"
_FsElmiPollingTimerValue_Object = MibTableColumn
fsElmiPollingTimerValue = _FsElmiPollingTimerValue_Object(
    (1, 3, 6, 1, 4, 1, 2076, 159, 1, 7, 1, 7),
    _FsElmiPollingTimerValue_Type()
)
fsElmiPollingTimerValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsElmiPollingTimerValue.setStatus("current")


class _FsElmiPollingCounterValue_Type(Integer32):
    """Custom type fsElmiPollingCounterValue based on Integer32"""
    defaultValue = 360

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65000),
    )


_FsElmiPollingCounterValue_Type.__name__ = "Integer32"
_FsElmiPollingCounterValue_Object = MibTableColumn
fsElmiPollingCounterValue = _FsElmiPollingCounterValue_Object(
    (1, 3, 6, 1, 4, 1, 2076, 159, 1, 7, 1, 8),
    _FsElmiPollingCounterValue_Type()
)
fsElmiPollingCounterValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsElmiPollingCounterValue.setStatus("current")
_FsElmiNoOfConfiguredEvcs_Type = Integer32
_FsElmiNoOfConfiguredEvcs_Object = MibTableColumn
fsElmiNoOfConfiguredEvcs = _FsElmiNoOfConfiguredEvcs_Object(
    (1, 3, 6, 1, 4, 1, 2076, 159, 1, 7, 1, 9),
    _FsElmiNoOfConfiguredEvcs_Type()
)
fsElmiNoOfConfiguredEvcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsElmiNoOfConfiguredEvcs.setStatus("current")
_FsElmiRxElmiCheckEnqMsgCount_Type = Counter32
_FsElmiRxElmiCheckEnqMsgCount_Object = MibTableColumn
fsElmiRxElmiCheckEnqMsgCount = _FsElmiRxElmiCheckEnqMsgCount_Object(
    (1, 3, 6, 1, 4, 1, 2076, 159, 1, 7, 1, 10),
    _FsElmiRxElmiCheckEnqMsgCount_Type()
)
fsElmiRxElmiCheckEnqMsgCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsElmiRxElmiCheckEnqMsgCount.setStatus("current")
_FsElmiRxFullStatusEnqMsgCount_Type = Counter32
_FsElmiRxFullStatusEnqMsgCount_Object = MibTableColumn
fsElmiRxFullStatusEnqMsgCount = _FsElmiRxFullStatusEnqMsgCount_Object(
    (1, 3, 6, 1, 4, 1, 2076, 159, 1, 7, 1, 11),
    _FsElmiRxFullStatusEnqMsgCount_Type()
)
fsElmiRxFullStatusEnqMsgCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsElmiRxFullStatusEnqMsgCount.setStatus("current")
_FsElmiRxFullStatusContEnqMsgCount_Type = Counter32
_FsElmiRxFullStatusContEnqMsgCount_Object = MibTableColumn
fsElmiRxFullStatusContEnqMsgCount = _FsElmiRxFullStatusContEnqMsgCount_Object(
    (1, 3, 6, 1, 4, 1, 2076, 159, 1, 7, 1, 12),
    _FsElmiRxFullStatusContEnqMsgCount_Type()
)
fsElmiRxFullStatusContEnqMsgCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsElmiRxFullStatusContEnqMsgCount.setStatus("current")
_FsElmiTxElmiCheckMsgCount_Type = Counter32
_FsElmiTxElmiCheckMsgCount_Object = MibTableColumn
fsElmiTxElmiCheckMsgCount = _FsElmiTxElmiCheckMsgCount_Object(
    (1, 3, 6, 1, 4, 1, 2076, 159, 1, 7, 1, 13),
    _FsElmiTxElmiCheckMsgCount_Type()
)
fsElmiTxElmiCheckMsgCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsElmiTxElmiCheckMsgCount.setStatus("current")
_FsElmiTxFullStatusMsgCount_Type = Counter32
_FsElmiTxFullStatusMsgCount_Object = MibTableColumn
fsElmiTxFullStatusMsgCount = _FsElmiTxFullStatusMsgCount_Object(
    (1, 3, 6, 1, 4, 1, 2076, 159, 1, 7, 1, 14),
    _FsElmiTxFullStatusMsgCount_Type()
)
fsElmiTxFullStatusMsgCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsElmiTxFullStatusMsgCount.setStatus("current")
_FsElmiTxFullStatusContMsgCount_Type = Counter32
_FsElmiTxFullStatusContMsgCount_Object = MibTableColumn
fsElmiTxFullStatusContMsgCount = _FsElmiTxFullStatusContMsgCount_Object(
    (1, 3, 6, 1, 4, 1, 2076, 159, 1, 7, 1, 15),
    _FsElmiTxFullStatusContMsgCount_Type()
)
fsElmiTxFullStatusContMsgCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsElmiTxFullStatusContMsgCount.setStatus("current")
_FsElmiTxAsyncStatusMsgCount_Type = Counter32
_FsElmiTxAsyncStatusMsgCount_Object = MibTableColumn
fsElmiTxAsyncStatusMsgCount = _FsElmiTxAsyncStatusMsgCount_Object(
    (1, 3, 6, 1, 4, 1, 2076, 159, 1, 7, 1, 16),
    _FsElmiTxAsyncStatusMsgCount_Type()
)
fsElmiTxAsyncStatusMsgCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsElmiTxAsyncStatusMsgCount.setStatus("current")
_FsElmiRxElmiCheckMsgCount_Type = Counter32
_FsElmiRxElmiCheckMsgCount_Object = MibTableColumn
fsElmiRxElmiCheckMsgCount = _FsElmiRxElmiCheckMsgCount_Object(
    (1, 3, 6, 1, 4, 1, 2076, 159, 1, 7, 1, 17),
    _FsElmiRxElmiCheckMsgCount_Type()
)
fsElmiRxElmiCheckMsgCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsElmiRxElmiCheckMsgCount.setStatus("current")
_FsElmiRxFullStatusMsgCount_Type = Counter32
_FsElmiRxFullStatusMsgCount_Object = MibTableColumn
fsElmiRxFullStatusMsgCount = _FsElmiRxFullStatusMsgCount_Object(
    (1, 3, 6, 1, 4, 1, 2076, 159, 1, 7, 1, 18),
    _FsElmiRxFullStatusMsgCount_Type()
)
fsElmiRxFullStatusMsgCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsElmiRxFullStatusMsgCount.setStatus("current")
_FsElmiRxFullStatusContMsgCount_Type = Counter32
_FsElmiRxFullStatusContMsgCount_Object = MibTableColumn
fsElmiRxFullStatusContMsgCount = _FsElmiRxFullStatusContMsgCount_Object(
    (1, 3, 6, 1, 4, 1, 2076, 159, 1, 7, 1, 19),
    _FsElmiRxFullStatusContMsgCount_Type()
)
fsElmiRxFullStatusContMsgCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsElmiRxFullStatusContMsgCount.setStatus("current")
_FsElmiRxAsyncStatusMsgCount_Type = Counter32
_FsElmiRxAsyncStatusMsgCount_Object = MibTableColumn
fsElmiRxAsyncStatusMsgCount = _FsElmiRxAsyncStatusMsgCount_Object(
    (1, 3, 6, 1, 4, 1, 2076, 159, 1, 7, 1, 20),
    _FsElmiRxAsyncStatusMsgCount_Type()
)
fsElmiRxAsyncStatusMsgCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsElmiRxAsyncStatusMsgCount.setStatus("current")
_FsElmiTxElmiCheckEnqMsgCount_Type = Counter32
_FsElmiTxElmiCheckEnqMsgCount_Object = MibTableColumn
fsElmiTxElmiCheckEnqMsgCount = _FsElmiTxElmiCheckEnqMsgCount_Object(
    (1, 3, 6, 1, 4, 1, 2076, 159, 1, 7, 1, 21),
    _FsElmiTxElmiCheckEnqMsgCount_Type()
)
fsElmiTxElmiCheckEnqMsgCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsElmiTxElmiCheckEnqMsgCount.setStatus("current")
_FsElmiTxFullStatusEnqMsgCount_Type = Counter32
_FsElmiTxFullStatusEnqMsgCount_Object = MibTableColumn
fsElmiTxFullStatusEnqMsgCount = _FsElmiTxFullStatusEnqMsgCount_Object(
    (1, 3, 6, 1, 4, 1, 2076, 159, 1, 7, 1, 22),
    _FsElmiTxFullStatusEnqMsgCount_Type()
)
fsElmiTxFullStatusEnqMsgCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsElmiTxFullStatusEnqMsgCount.setStatus("current")
_FsElmiTxFullStatusContEnqMsgCount_Type = Counter32
_FsElmiTxFullStatusContEnqMsgCount_Object = MibTableColumn
fsElmiTxFullStatusContEnqMsgCount = _FsElmiTxFullStatusContEnqMsgCount_Object(
    (1, 3, 6, 1, 4, 1, 2076, 159, 1, 7, 1, 23),
    _FsElmiTxFullStatusContEnqMsgCount_Type()
)
fsElmiTxFullStatusContEnqMsgCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsElmiTxFullStatusContEnqMsgCount.setStatus("current")
_FsElmiRxValidMsgCount_Type = Counter32
_FsElmiRxValidMsgCount_Object = MibTableColumn
fsElmiRxValidMsgCount = _FsElmiRxValidMsgCount_Object(
    (1, 3, 6, 1, 4, 1, 2076, 159, 1, 7, 1, 24),
    _FsElmiRxValidMsgCount_Type()
)
fsElmiRxValidMsgCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsElmiRxValidMsgCount.setStatus("current")
_FsElmiRxInvalidMsgCount_Type = Counter32
_FsElmiRxInvalidMsgCount_Object = MibTableColumn
fsElmiRxInvalidMsgCount = _FsElmiRxInvalidMsgCount_Object(
    (1, 3, 6, 1, 4, 1, 2076, 159, 1, 7, 1, 25),
    _FsElmiRxInvalidMsgCount_Type()
)
fsElmiRxInvalidMsgCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsElmiRxInvalidMsgCount.setStatus("current")
_FsElmiRelErrStatusTimeOutCount_Type = Counter32
_FsElmiRelErrStatusTimeOutCount_Object = MibTableColumn
fsElmiRelErrStatusTimeOutCount = _FsElmiRelErrStatusTimeOutCount_Object(
    (1, 3, 6, 1, 4, 1, 2076, 159, 1, 7, 1, 26),
    _FsElmiRelErrStatusTimeOutCount_Type()
)
fsElmiRelErrStatusTimeOutCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsElmiRelErrStatusTimeOutCount.setStatus("current")
_FsElmiRelErrInvalidSeqNumCount_Type = Counter32
_FsElmiRelErrInvalidSeqNumCount_Object = MibTableColumn
fsElmiRelErrInvalidSeqNumCount = _FsElmiRelErrInvalidSeqNumCount_Object(
    (1, 3, 6, 1, 4, 1, 2076, 159, 1, 7, 1, 27),
    _FsElmiRelErrInvalidSeqNumCount_Type()
)
fsElmiRelErrInvalidSeqNumCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsElmiRelErrInvalidSeqNumCount.setStatus("current")
_FsElmiRelErrInvalidStatusRespCount_Type = Counter32
_FsElmiRelErrInvalidStatusRespCount_Object = MibTableColumn
fsElmiRelErrInvalidStatusRespCount = _FsElmiRelErrInvalidStatusRespCount_Object(
    (1, 3, 6, 1, 4, 1, 2076, 159, 1, 7, 1, 28),
    _FsElmiRelErrInvalidStatusRespCount_Type()
)
fsElmiRelErrInvalidStatusRespCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsElmiRelErrInvalidStatusRespCount.setStatus("current")
_FsElmiRelErrRxUnSolicitedStatusCount_Type = Counter32
_FsElmiRelErrRxUnSolicitedStatusCount_Object = MibTableColumn
fsElmiRelErrRxUnSolicitedStatusCount = _FsElmiRelErrRxUnSolicitedStatusCount_Object(
    (1, 3, 6, 1, 4, 1, 2076, 159, 1, 7, 1, 29),
    _FsElmiRelErrRxUnSolicitedStatusCount_Type()
)
fsElmiRelErrRxUnSolicitedStatusCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsElmiRelErrRxUnSolicitedStatusCount.setStatus("current")
_FsElmiProErrInvalidProtVerCount_Type = Counter32
_FsElmiProErrInvalidProtVerCount_Object = MibTableColumn
fsElmiProErrInvalidProtVerCount = _FsElmiProErrInvalidProtVerCount_Object(
    (1, 3, 6, 1, 4, 1, 2076, 159, 1, 7, 1, 30),
    _FsElmiProErrInvalidProtVerCount_Type()
)
fsElmiProErrInvalidProtVerCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsElmiProErrInvalidProtVerCount.setStatus("current")
_FsElmiProErrInvalidEvcRefIdCount_Type = Counter32
_FsElmiProErrInvalidEvcRefIdCount_Object = MibTableColumn
fsElmiProErrInvalidEvcRefIdCount = _FsElmiProErrInvalidEvcRefIdCount_Object(
    (1, 3, 6, 1, 4, 1, 2076, 159, 1, 7, 1, 31),
    _FsElmiProErrInvalidEvcRefIdCount_Type()
)
fsElmiProErrInvalidEvcRefIdCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsElmiProErrInvalidEvcRefIdCount.setStatus("current")
_FsElmiProErrInvalidMessageTypeCount_Type = Counter32
_FsElmiProErrInvalidMessageTypeCount_Object = MibTableColumn
fsElmiProErrInvalidMessageTypeCount = _FsElmiProErrInvalidMessageTypeCount_Object(
    (1, 3, 6, 1, 4, 1, 2076, 159, 1, 7, 1, 32),
    _FsElmiProErrInvalidMessageTypeCount_Type()
)
fsElmiProErrInvalidMessageTypeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsElmiProErrInvalidMessageTypeCount.setStatus("current")
_FsElmiProErrOutOfSequenceInfoEleCount_Type = Counter32
_FsElmiProErrOutOfSequenceInfoEleCount_Object = MibTableColumn
fsElmiProErrOutOfSequenceInfoEleCount = _FsElmiProErrOutOfSequenceInfoEleCount_Object(
    (1, 3, 6, 1, 4, 1, 2076, 159, 1, 7, 1, 33),
    _FsElmiProErrOutOfSequenceInfoEleCount_Type()
)
fsElmiProErrOutOfSequenceInfoEleCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsElmiProErrOutOfSequenceInfoEleCount.setStatus("current")
_FsElmiProErrDuplicateInfoEleCount_Type = Counter32
_FsElmiProErrDuplicateInfoEleCount_Object = MibTableColumn
fsElmiProErrDuplicateInfoEleCount = _FsElmiProErrDuplicateInfoEleCount_Object(
    (1, 3, 6, 1, 4, 1, 2076, 159, 1, 7, 1, 34),
    _FsElmiProErrDuplicateInfoEleCount_Type()
)
fsElmiProErrDuplicateInfoEleCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsElmiProErrDuplicateInfoEleCount.setStatus("current")
_FsElmiProErrMandatoryInfoEleMissingCount_Type = Counter32
_FsElmiProErrMandatoryInfoEleMissingCount_Object = MibTableColumn
fsElmiProErrMandatoryInfoEleMissingCount = _FsElmiProErrMandatoryInfoEleMissingCount_Object(
    (1, 3, 6, 1, 4, 1, 2076, 159, 1, 7, 1, 35),
    _FsElmiProErrMandatoryInfoEleMissingCount_Type()
)
fsElmiProErrMandatoryInfoEleMissingCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsElmiProErrMandatoryInfoEleMissingCount.setStatus("current")
_FsElmiProErrInvalidMandatoryInfoEleCount_Type = Counter32
_FsElmiProErrInvalidMandatoryInfoEleCount_Object = MibTableColumn
fsElmiProErrInvalidMandatoryInfoEleCount = _FsElmiProErrInvalidMandatoryInfoEleCount_Object(
    (1, 3, 6, 1, 4, 1, 2076, 159, 1, 7, 1, 36),
    _FsElmiProErrInvalidMandatoryInfoEleCount_Type()
)
fsElmiProErrInvalidMandatoryInfoEleCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsElmiProErrInvalidMandatoryInfoEleCount.setStatus("current")
_FsElmiProErrInvalidNonMandatoryInfoEleCount_Type = Counter32
_FsElmiProErrInvalidNonMandatoryInfoEleCount_Object = MibTableColumn
fsElmiProErrInvalidNonMandatoryInfoEleCount = _FsElmiProErrInvalidNonMandatoryInfoEleCount_Object(
    (1, 3, 6, 1, 4, 1, 2076, 159, 1, 7, 1, 37),
    _FsElmiProErrInvalidNonMandatoryInfoEleCount_Type()
)
fsElmiProErrInvalidNonMandatoryInfoEleCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsElmiProErrInvalidNonMandatoryInfoEleCount.setStatus("current")
_FsElmiProErrUnrecognizedInfoEleCount_Type = Counter32
_FsElmiProErrUnrecognizedInfoEleCount_Object = MibTableColumn
fsElmiProErrUnrecognizedInfoEleCount = _FsElmiProErrUnrecognizedInfoEleCount_Object(
    (1, 3, 6, 1, 4, 1, 2076, 159, 1, 7, 1, 38),
    _FsElmiProErrUnrecognizedInfoEleCount_Type()
)
fsElmiProErrUnrecognizedInfoEleCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsElmiProErrUnrecognizedInfoEleCount.setStatus("current")
_FsElmiProErrUnexpectedInfoEleCount_Type = Counter32
_FsElmiProErrUnexpectedInfoEleCount_Object = MibTableColumn
fsElmiProErrUnexpectedInfoEleCount = _FsElmiProErrUnexpectedInfoEleCount_Object(
    (1, 3, 6, 1, 4, 1, 2076, 159, 1, 7, 1, 39),
    _FsElmiProErrUnexpectedInfoEleCount_Type()
)
fsElmiProErrUnexpectedInfoEleCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsElmiProErrUnexpectedInfoEleCount.setStatus("current")
_FsElmiProErrShortMessageCount_Type = Counter32
_FsElmiProErrShortMessageCount_Object = MibTableColumn
fsElmiProErrShortMessageCount = _FsElmiProErrShortMessageCount_Object(
    (1, 3, 6, 1, 4, 1, 2076, 159, 1, 7, 1, 40),
    _FsElmiProErrShortMessageCount_Type()
)
fsElmiProErrShortMessageCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsElmiProErrShortMessageCount.setStatus("current")
_FutureElmiTrapsControl_ObjectIdentity = ObjectIdentity
futureElmiTrapsControl = _FutureElmiTrapsControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 159, 2)
)


class _FsElmiSetGlobalTrapOption_Type(Integer32):
    """Custom type fsElmiSetGlobalTrapOption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_FsElmiSetGlobalTrapOption_Type.__name__ = "Integer32"
_FsElmiSetGlobalTrapOption_Object = MibScalar
fsElmiSetGlobalTrapOption = _FsElmiSetGlobalTrapOption_Object(
    (1, 3, 6, 1, 4, 1, 2076, 159, 2, 1),
    _FsElmiSetGlobalTrapOption_Type()
)
fsElmiSetGlobalTrapOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsElmiSetGlobalTrapOption.setStatus("current")


class _FsElmiSetTraps_Type(Integer32):
    """Custom type fsElmiSetTraps based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_FsElmiSetTraps_Type.__name__ = "Integer32"
_FsElmiSetTraps_Object = MibScalar
fsElmiSetTraps = _FsElmiSetTraps_Object(
    (1, 3, 6, 1, 4, 1, 2076, 159, 2, 2),
    _FsElmiSetTraps_Type()
)
fsElmiSetTraps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsElmiSetTraps.setStatus("current")


class _FsElmiErrTrapType_Type(Integer32):
    """Custom type fsElmiErrTrapType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("memfail", 1),
          ("bufffail", 2))
    )


_FsElmiErrTrapType_Type.__name__ = "Integer32"
_FsElmiErrTrapType_Object = MibScalar
fsElmiErrTrapType = _FsElmiErrTrapType_Object(
    (1, 3, 6, 1, 4, 1, 2076, 159, 2, 3),
    _FsElmiErrTrapType_Type()
)
fsElmiErrTrapType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsElmiErrTrapType.setStatus("current")
_FsElmiPortTrapNotificationTable_Object = MibTable
fsElmiPortTrapNotificationTable = _FsElmiPortTrapNotificationTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 159, 2, 4)
)
if mibBuilder.loadTexts:
    fsElmiPortTrapNotificationTable.setStatus("current")
_FsElmiPortTrapNotificationEntry_Object = MibTableRow
fsElmiPortTrapNotificationEntry = _FsElmiPortTrapNotificationEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 159, 2, 4, 1)
)
fsElmiPortTrapNotificationEntry.setIndexNames(
    (0, "ARICENT-ELMI-MIB", "fsElmiPortTrapIndex"),
)
if mibBuilder.loadTexts:
    fsElmiPortTrapNotificationEntry.setStatus("current")


class _FsElmiPortTrapIndex_Type(Integer32):
    """Custom type fsElmiPortTrapIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_FsElmiPortTrapIndex_Type.__name__ = "Integer32"
_FsElmiPortTrapIndex_Object = MibTableColumn
fsElmiPortTrapIndex = _FsElmiPortTrapIndex_Object(
    (1, 3, 6, 1, 4, 1, 2076, 159, 2, 4, 1, 1),
    _FsElmiPortTrapIndex_Type()
)
fsElmiPortTrapIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsElmiPortTrapIndex.setStatus("current")


class _FsElmiPvtExpired_Type(Integer32):
    """Custom type fsElmiPvtExpired based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("pvtTimerExpired", 0)
    )


_FsElmiPvtExpired_Type.__name__ = "Integer32"
_FsElmiPvtExpired_Object = MibTableColumn
fsElmiPvtExpired = _FsElmiPvtExpired_Object(
    (1, 3, 6, 1, 4, 1, 2076, 159, 2, 4, 1, 2),
    _FsElmiPvtExpired_Type()
)
fsElmiPvtExpired.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsElmiPvtExpired.setStatus("current")


class _FsElmiPtExpired_Type(Integer32):
    """Custom type fsElmiPtExpired based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("ptTimerExpired", 0)
    )


_FsElmiPtExpired_Type.__name__ = "Integer32"
_FsElmiPtExpired_Object = MibTableColumn
fsElmiPtExpired = _FsElmiPtExpired_Object(
    (1, 3, 6, 1, 4, 1, 2076, 159, 2, 4, 1, 3),
    _FsElmiPtExpired_Type()
)
fsElmiPtExpired.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsElmiPtExpired.setStatus("current")


class _FsElmiEvcStatus_Type(Integer32):
    """Custom type fsElmiEvcStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("evcNew", 0),
          ("evcDelete", 1),
          ("evcChange", 2))
    )


_FsElmiEvcStatus_Type.__name__ = "Integer32"
_FsElmiEvcStatus_Object = MibTableColumn
fsElmiEvcStatus = _FsElmiEvcStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 159, 2, 4, 1, 4),
    _FsElmiEvcStatus_Type()
)
fsElmiEvcStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsElmiEvcStatus.setStatus("current")


class _FsElmiUniStatus_Type(Integer32):
    """Custom type fsElmiUniStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("uniChange", 0)
    )


_FsElmiUniStatus_Type.__name__ = "Integer32"
_FsElmiUniStatus_Object = MibTableColumn
fsElmiUniStatus = _FsElmiUniStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 159, 2, 4, 1, 5),
    _FsElmiUniStatus_Type()
)
fsElmiUniStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsElmiUniStatus.setStatus("current")


class _FsElmiEvcId_Type(OctetString):
    """Custom type fsElmiEvcId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(100, 100),
    )
    fixed_length = 100


_FsElmiEvcId_Type.__name__ = "OctetString"
_FsElmiEvcId_Object = MibTableColumn
fsElmiEvcId = _FsElmiEvcId_Object(
    (1, 3, 6, 1, 4, 1, 2076, 159, 2, 4, 1, 6),
    _FsElmiEvcId_Type()
)
fsElmiEvcId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsElmiEvcId.setStatus("current")


class _FsElmiErrType_Type(Integer32):
    """Custom type fsElmiErrType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("reliabilityErrType", 0),
          ("protocolErrType", 1))
    )


_FsElmiErrType_Type.__name__ = "Integer32"
_FsElmiErrType_Object = MibTableColumn
fsElmiErrType = _FsElmiErrType_Object(
    (1, 3, 6, 1, 4, 1, 2076, 159, 2, 4, 1, 7),
    _FsElmiErrType_Type()
)
fsElmiErrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsElmiErrType.setStatus("current")


class _FsElmiOperStatusStatus_Type(Integer32):
    """Custom type fsElmiOperStatusStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("fsElmiOperEnabled", 0),
          ("fsElmiOperDisabled", 1))
    )


_FsElmiOperStatusStatus_Type.__name__ = "Integer32"
_FsElmiOperStatusStatus_Object = MibTableColumn
fsElmiOperStatusStatus = _FsElmiOperStatusStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 159, 2, 4, 1, 8),
    _FsElmiOperStatusStatus_Type()
)
fsElmiOperStatusStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsElmiOperStatusStatus.setStatus("current")
_FutureElmiTraps_ObjectIdentity = ObjectIdentity
futureElmiTraps = _FutureElmiTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 159, 3)
)
_FsElmiTraps_ObjectIdentity = ObjectIdentity
fsElmiTraps = _FsElmiTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 159, 3, 0)
)

# Managed Objects groups


# Notification objects

fsElmiInvalidMsgRxdTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2076, 159, 3, 0, 1)
)
fsElmiInvalidMsgRxdTrap.setObjects(
    ("ARICENT-ELMI-MIB", "fsElmiErrType")
)
if mibBuilder.loadTexts:
    fsElmiInvalidMsgRxdTrap.setStatus(
        "current"
    )

fsElmiErrTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2076, 159, 3, 0, 2)
)
fsElmiErrTrap.setObjects(
    ("ARICENT-ELMI-MIB", "fsElmiErrTrapType")
)
if mibBuilder.loadTexts:
    fsElmiErrTrap.setStatus(
        "current"
    )

fsElmiPvtExpiredTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2076, 159, 3, 0, 3)
)
fsElmiPvtExpiredTrap.setObjects(
    ("ARICENT-ELMI-MIB", "fsElmiPvtExpired")
)
if mibBuilder.loadTexts:
    fsElmiPvtExpiredTrap.setStatus(
        "current"
    )

fsElmiPtExpiredTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2076, 159, 3, 0, 4)
)
fsElmiPtExpiredTrap.setObjects(
    ("ARICENT-ELMI-MIB", "fsElmiPtExpired")
)
if mibBuilder.loadTexts:
    fsElmiPtExpiredTrap.setStatus(
        "current"
    )

fsElmiEvcTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2076, 159, 3, 0, 5)
)
fsElmiEvcTrap.setObjects(
      *(("ARICENT-ELMI-MIB", "fsElmiEvcId"),
        ("ARICENT-ELMI-MIB", "fsElmiEvcStatus"))
)
if mibBuilder.loadTexts:
    fsElmiEvcTrap.setStatus(
        "current"
    )

fsElmiUniTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2076, 159, 3, 0, 6)
)
fsElmiUniTrap.setObjects(
    ("ARICENT-ELMI-MIB", "fsElmiUniStatus")
)
if mibBuilder.loadTexts:
    fsElmiUniTrap.setStatus(
        "current"
    )

fsElmiOperStatusTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2076, 159, 3, 0, 7)
)
fsElmiOperStatusTrap.setObjects(
    ("ARICENT-ELMI-MIB", "fsElmiOperStatusStatus")
)
if mibBuilder.loadTexts:
    fsElmiOperStatusTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ARICENT-ELMI-MIB",
    **{"EnabledStatus": EnabledStatus,
       "futureElmiMIB": futureElmiMIB,
       "futureElmi": futureElmi,
       "fsElmiSystemControl": fsElmiSystemControl,
       "fsElmiModuleStatus": fsElmiModuleStatus,
       "fsElmiActivePortCount": fsElmiActivePortCount,
       "fsElmiTraceOption": fsElmiTraceOption,
       "fsElmiBufferOverFlowCount": fsElmiBufferOverFlowCount,
       "fsElmiMemAllocFailureCount": fsElmiMemAllocFailureCount,
       "fsElmiPortTable": fsElmiPortTable,
       "fsElmiPortEntry": fsElmiPortEntry,
       "fsElmiPort": fsElmiPort,
       "fsElmiPortElmiStatus": fsElmiPortElmiStatus,
       "fsElmiUniSide": fsElmiUniSide,
       "fsElmiOperStatus": fsElmiOperStatus,
       "fsElmiStatusCounter": fsElmiStatusCounter,
       "fsElmiPollingVerificationTimerValue": fsElmiPollingVerificationTimerValue,
       "fsElmiPollingTimerValue": fsElmiPollingTimerValue,
       "fsElmiPollingCounterValue": fsElmiPollingCounterValue,
       "fsElmiNoOfConfiguredEvcs": fsElmiNoOfConfiguredEvcs,
       "fsElmiRxElmiCheckEnqMsgCount": fsElmiRxElmiCheckEnqMsgCount,
       "fsElmiRxFullStatusEnqMsgCount": fsElmiRxFullStatusEnqMsgCount,
       "fsElmiRxFullStatusContEnqMsgCount": fsElmiRxFullStatusContEnqMsgCount,
       "fsElmiTxElmiCheckMsgCount": fsElmiTxElmiCheckMsgCount,
       "fsElmiTxFullStatusMsgCount": fsElmiTxFullStatusMsgCount,
       "fsElmiTxFullStatusContMsgCount": fsElmiTxFullStatusContMsgCount,
       "fsElmiTxAsyncStatusMsgCount": fsElmiTxAsyncStatusMsgCount,
       "fsElmiRxElmiCheckMsgCount": fsElmiRxElmiCheckMsgCount,
       "fsElmiRxFullStatusMsgCount": fsElmiRxFullStatusMsgCount,
       "fsElmiRxFullStatusContMsgCount": fsElmiRxFullStatusContMsgCount,
       "fsElmiRxAsyncStatusMsgCount": fsElmiRxAsyncStatusMsgCount,
       "fsElmiTxElmiCheckEnqMsgCount": fsElmiTxElmiCheckEnqMsgCount,
       "fsElmiTxFullStatusEnqMsgCount": fsElmiTxFullStatusEnqMsgCount,
       "fsElmiTxFullStatusContEnqMsgCount": fsElmiTxFullStatusContEnqMsgCount,
       "fsElmiRxValidMsgCount": fsElmiRxValidMsgCount,
       "fsElmiRxInvalidMsgCount": fsElmiRxInvalidMsgCount,
       "fsElmiRelErrStatusTimeOutCount": fsElmiRelErrStatusTimeOutCount,
       "fsElmiRelErrInvalidSeqNumCount": fsElmiRelErrInvalidSeqNumCount,
       "fsElmiRelErrInvalidStatusRespCount": fsElmiRelErrInvalidStatusRespCount,
       "fsElmiRelErrRxUnSolicitedStatusCount": fsElmiRelErrRxUnSolicitedStatusCount,
       "fsElmiProErrInvalidProtVerCount": fsElmiProErrInvalidProtVerCount,
       "fsElmiProErrInvalidEvcRefIdCount": fsElmiProErrInvalidEvcRefIdCount,
       "fsElmiProErrInvalidMessageTypeCount": fsElmiProErrInvalidMessageTypeCount,
       "fsElmiProErrOutOfSequenceInfoEleCount": fsElmiProErrOutOfSequenceInfoEleCount,
       "fsElmiProErrDuplicateInfoEleCount": fsElmiProErrDuplicateInfoEleCount,
       "fsElmiProErrMandatoryInfoEleMissingCount": fsElmiProErrMandatoryInfoEleMissingCount,
       "fsElmiProErrInvalidMandatoryInfoEleCount": fsElmiProErrInvalidMandatoryInfoEleCount,
       "fsElmiProErrInvalidNonMandatoryInfoEleCount": fsElmiProErrInvalidNonMandatoryInfoEleCount,
       "fsElmiProErrUnrecognizedInfoEleCount": fsElmiProErrUnrecognizedInfoEleCount,
       "fsElmiProErrUnexpectedInfoEleCount": fsElmiProErrUnexpectedInfoEleCount,
       "fsElmiProErrShortMessageCount": fsElmiProErrShortMessageCount,
       "futureElmiTrapsControl": futureElmiTrapsControl,
       "fsElmiSetGlobalTrapOption": fsElmiSetGlobalTrapOption,
       "fsElmiSetTraps": fsElmiSetTraps,
       "fsElmiErrTrapType": fsElmiErrTrapType,
       "fsElmiPortTrapNotificationTable": fsElmiPortTrapNotificationTable,
       "fsElmiPortTrapNotificationEntry": fsElmiPortTrapNotificationEntry,
       "fsElmiPortTrapIndex": fsElmiPortTrapIndex,
       "fsElmiPvtExpired": fsElmiPvtExpired,
       "fsElmiPtExpired": fsElmiPtExpired,
       "fsElmiEvcStatus": fsElmiEvcStatus,
       "fsElmiUniStatus": fsElmiUniStatus,
       "fsElmiEvcId": fsElmiEvcId,
       "fsElmiErrType": fsElmiErrType,
       "fsElmiOperStatusStatus": fsElmiOperStatusStatus,
       "futureElmiTraps": futureElmiTraps,
       "fsElmiTraps": fsElmiTraps,
       "fsElmiInvalidMsgRxdTrap": fsElmiInvalidMsgRxdTrap,
       "fsElmiErrTrap": fsElmiErrTrap,
       "fsElmiPvtExpiredTrap": fsElmiPvtExpiredTrap,
       "fsElmiPtExpiredTrap": fsElmiPtExpiredTrap,
       "fsElmiEvcTrap": fsElmiEvcTrap,
       "fsElmiUniTrap": fsElmiUniTrap,
       "fsElmiOperStatusTrap": fsElmiOperStatusTrap}
)
