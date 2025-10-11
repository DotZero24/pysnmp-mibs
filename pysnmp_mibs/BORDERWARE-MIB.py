# SNMP MIB module (BORDERWARE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/watchguard/BORDERWARE-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:17:37 2025
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
 Opaque,
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
    "Opaque",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DateAndTime,
 DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

borderware = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8673)
)
if mibBuilder.loadTexts:
    borderware.setRevisions(
        ("2002-11-07 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class Float(TextualConvention, Opaque):
    status = "current"
    subtypeSpec = Opaque.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(7, 7),
    )
    fixed_length = 7



# MIB Managed Objects in the order of their OIDs

_BwProducts_ObjectIdentity = ObjectIdentity
bwProducts = _BwProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8673, 1)
)
_BwProductId_ObjectIdentity = ObjectIdentity
bwProductId = _BwProductId_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8673, 1, 2)
)
_BwFirewallServer7_ObjectIdentity = ObjectIdentity
bwFirewallServer7 = _BwFirewallServer7_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8673, 1, 2, 1)
)
_BwSysMemory_ObjectIdentity = ObjectIdentity
bwSysMemory = _BwSysMemory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8673, 4)
)
_MemIndex_Type = Integer32
_MemIndex_Object = MibScalar
memIndex = _MemIndex_Object(
    (1, 3, 6, 1, 4, 1, 8673, 4, 1),
    _MemIndex_Type()
)
memIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memIndex.setStatus("current")
_MemErrorName_Type = DisplayString
_MemErrorName_Object = MibScalar
memErrorName = _MemErrorName_Object(
    (1, 3, 6, 1, 4, 1, 8673, 4, 2),
    _MemErrorName_Type()
)
memErrorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memErrorName.setStatus("current")
_MemTotalSwap_Type = Integer32
_MemTotalSwap_Object = MibScalar
memTotalSwap = _MemTotalSwap_Object(
    (1, 3, 6, 1, 4, 1, 8673, 4, 3),
    _MemTotalSwap_Type()
)
memTotalSwap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memTotalSwap.setStatus("current")
_MemAvailSwap_Type = Integer32
_MemAvailSwap_Object = MibScalar
memAvailSwap = _MemAvailSwap_Object(
    (1, 3, 6, 1, 4, 1, 8673, 4, 4),
    _MemAvailSwap_Type()
)
memAvailSwap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memAvailSwap.setStatus("current")
_MemTotalReal_Type = Integer32
_MemTotalReal_Object = MibScalar
memTotalReal = _MemTotalReal_Object(
    (1, 3, 6, 1, 4, 1, 8673, 4, 5),
    _MemTotalReal_Type()
)
memTotalReal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memTotalReal.setStatus("current")
_MemAvailReal_Type = Integer32
_MemAvailReal_Object = MibScalar
memAvailReal = _MemAvailReal_Object(
    (1, 3, 6, 1, 4, 1, 8673, 4, 6),
    _MemAvailReal_Type()
)
memAvailReal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memAvailReal.setStatus("current")
_MemTotalSwapTXT_Type = Integer32
_MemTotalSwapTXT_Object = MibScalar
memTotalSwapTXT = _MemTotalSwapTXT_Object(
    (1, 3, 6, 1, 4, 1, 8673, 4, 7),
    _MemTotalSwapTXT_Type()
)
memTotalSwapTXT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memTotalSwapTXT.setStatus("current")
_MemAvailSwapTXT_Type = Integer32
_MemAvailSwapTXT_Object = MibScalar
memAvailSwapTXT = _MemAvailSwapTXT_Object(
    (1, 3, 6, 1, 4, 1, 8673, 4, 8),
    _MemAvailSwapTXT_Type()
)
memAvailSwapTXT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memAvailSwapTXT.setStatus("current")
_MemTotalRealTXT_Type = Integer32
_MemTotalRealTXT_Object = MibScalar
memTotalRealTXT = _MemTotalRealTXT_Object(
    (1, 3, 6, 1, 4, 1, 8673, 4, 9),
    _MemTotalRealTXT_Type()
)
memTotalRealTXT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memTotalRealTXT.setStatus("current")
_MemAvailRealTXT_Type = Integer32
_MemAvailRealTXT_Object = MibScalar
memAvailRealTXT = _MemAvailRealTXT_Object(
    (1, 3, 6, 1, 4, 1, 8673, 4, 10),
    _MemAvailRealTXT_Type()
)
memAvailRealTXT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memAvailRealTXT.setStatus("current")
_MemTotalFree_Type = Integer32
_MemTotalFree_Object = MibScalar
memTotalFree = _MemTotalFree_Object(
    (1, 3, 6, 1, 4, 1, 8673, 4, 11),
    _MemTotalFree_Type()
)
memTotalFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memTotalFree.setStatus("current")
_MemMinimumSwap_Type = Integer32
_MemMinimumSwap_Object = MibScalar
memMinimumSwap = _MemMinimumSwap_Object(
    (1, 3, 6, 1, 4, 1, 8673, 4, 12),
    _MemMinimumSwap_Type()
)
memMinimumSwap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memMinimumSwap.setStatus("current")
_MemShared_Type = Integer32
_MemShared_Object = MibScalar
memShared = _MemShared_Object(
    (1, 3, 6, 1, 4, 1, 8673, 4, 13),
    _MemShared_Type()
)
memShared.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memShared.setStatus("current")
_MemBuffer_Type = Integer32
_MemBuffer_Object = MibScalar
memBuffer = _MemBuffer_Object(
    (1, 3, 6, 1, 4, 1, 8673, 4, 14),
    _MemBuffer_Type()
)
memBuffer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memBuffer.setStatus("current")
_MemCached_Type = Integer32
_MemCached_Object = MibScalar
memCached = _MemCached_Object(
    (1, 3, 6, 1, 4, 1, 8673, 4, 15),
    _MemCached_Type()
)
memCached.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memCached.setStatus("current")
_MemSwapError_Type = Integer32
_MemSwapError_Object = MibScalar
memSwapError = _MemSwapError_Object(
    (1, 3, 6, 1, 4, 1, 8673, 4, 100),
    _MemSwapError_Type()
)
memSwapError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memSwapError.setStatus("current")
_MemSwapErrorMsg_Type = DisplayString
_MemSwapErrorMsg_Object = MibScalar
memSwapErrorMsg = _MemSwapErrorMsg_Object(
    (1, 3, 6, 1, 4, 1, 8673, 4, 101),
    _MemSwapErrorMsg_Type()
)
memSwapErrorMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memSwapErrorMsg.setStatus("current")
_DskTable_Object = MibTable
dskTable = _DskTable_Object(
    (1, 3, 6, 1, 4, 1, 8673, 9)
)
if mibBuilder.loadTexts:
    dskTable.setStatus("current")
_DskEntry_Object = MibTableRow
dskEntry = _DskEntry_Object(
    (1, 3, 6, 1, 4, 1, 8673, 9, 1)
)
dskEntry.setIndexNames(
    (0, "BORDERWARE-MIB", "dskIndex"),
)
if mibBuilder.loadTexts:
    dskEntry.setStatus("current")


class _DskIndex_Type(Integer32):
    """Custom type dskIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DskIndex_Type.__name__ = "Integer32"
_DskIndex_Object = MibTableColumn
dskIndex = _DskIndex_Object(
    (1, 3, 6, 1, 4, 1, 8673, 9, 1, 1),
    _DskIndex_Type()
)
dskIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dskIndex.setStatus("current")
_DskPath_Type = DisplayString
_DskPath_Object = MibTableColumn
dskPath = _DskPath_Object(
    (1, 3, 6, 1, 4, 1, 8673, 9, 1, 2),
    _DskPath_Type()
)
dskPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dskPath.setStatus("current")
_DskDevice_Type = DisplayString
_DskDevice_Object = MibTableColumn
dskDevice = _DskDevice_Object(
    (1, 3, 6, 1, 4, 1, 8673, 9, 1, 3),
    _DskDevice_Type()
)
dskDevice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dskDevice.setStatus("current")
_DskMinimum_Type = Integer32
_DskMinimum_Object = MibTableColumn
dskMinimum = _DskMinimum_Object(
    (1, 3, 6, 1, 4, 1, 8673, 9, 1, 4),
    _DskMinimum_Type()
)
dskMinimum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dskMinimum.setStatus("current")
_DskMinPercent_Type = Integer32
_DskMinPercent_Object = MibTableColumn
dskMinPercent = _DskMinPercent_Object(
    (1, 3, 6, 1, 4, 1, 8673, 9, 1, 5),
    _DskMinPercent_Type()
)
dskMinPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dskMinPercent.setStatus("current")
_DskTotal_Type = Integer32
_DskTotal_Object = MibTableColumn
dskTotal = _DskTotal_Object(
    (1, 3, 6, 1, 4, 1, 8673, 9, 1, 6),
    _DskTotal_Type()
)
dskTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dskTotal.setStatus("current")
_DskAvail_Type = Integer32
_DskAvail_Object = MibTableColumn
dskAvail = _DskAvail_Object(
    (1, 3, 6, 1, 4, 1, 8673, 9, 1, 7),
    _DskAvail_Type()
)
dskAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dskAvail.setStatus("current")
_DskUsed_Type = Integer32
_DskUsed_Object = MibTableColumn
dskUsed = _DskUsed_Object(
    (1, 3, 6, 1, 4, 1, 8673, 9, 1, 8),
    _DskUsed_Type()
)
dskUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dskUsed.setStatus("current")
_DskPercent_Type = Integer32
_DskPercent_Object = MibTableColumn
dskPercent = _DskPercent_Object(
    (1, 3, 6, 1, 4, 1, 8673, 9, 1, 9),
    _DskPercent_Type()
)
dskPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dskPercent.setStatus("current")
_DskPercentNode_Type = Integer32
_DskPercentNode_Object = MibTableColumn
dskPercentNode = _DskPercentNode_Object(
    (1, 3, 6, 1, 4, 1, 8673, 9, 1, 10),
    _DskPercentNode_Type()
)
dskPercentNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dskPercentNode.setStatus("current")
_DskErrorFlag_Type = Integer32
_DskErrorFlag_Object = MibTableColumn
dskErrorFlag = _DskErrorFlag_Object(
    (1, 3, 6, 1, 4, 1, 8673, 9, 1, 100),
    _DskErrorFlag_Type()
)
dskErrorFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dskErrorFlag.setStatus("current")
_DskErrorMsg_Type = DisplayString
_DskErrorMsg_Object = MibTableColumn
dskErrorMsg = _DskErrorMsg_Object(
    (1, 3, 6, 1, 4, 1, 8673, 9, 1, 101),
    _DskErrorMsg_Type()
)
dskErrorMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dskErrorMsg.setStatus("current")
_SystemStats_ObjectIdentity = ObjectIdentity
systemStats = _SystemStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8673, 11)
)
_SsIndex_Type = Integer32
_SsIndex_Object = MibScalar
ssIndex = _SsIndex_Object(
    (1, 3, 6, 1, 4, 1, 8673, 11, 1),
    _SsIndex_Type()
)
ssIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssIndex.setStatus("current")
_SsErrorName_Type = DisplayString
_SsErrorName_Object = MibScalar
ssErrorName = _SsErrorName_Object(
    (1, 3, 6, 1, 4, 1, 8673, 11, 2),
    _SsErrorName_Type()
)
ssErrorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssErrorName.setStatus("current")
_SsSwapIn_Type = Integer32
_SsSwapIn_Object = MibScalar
ssSwapIn = _SsSwapIn_Object(
    (1, 3, 6, 1, 4, 1, 8673, 11, 3),
    _SsSwapIn_Type()
)
ssSwapIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssSwapIn.setStatus("current")
_SsSwapOut_Type = Integer32
_SsSwapOut_Object = MibScalar
ssSwapOut = _SsSwapOut_Object(
    (1, 3, 6, 1, 4, 1, 8673, 11, 4),
    _SsSwapOut_Type()
)
ssSwapOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssSwapOut.setStatus("current")
_SsIOSent_Type = Integer32
_SsIOSent_Object = MibScalar
ssIOSent = _SsIOSent_Object(
    (1, 3, 6, 1, 4, 1, 8673, 11, 5),
    _SsIOSent_Type()
)
ssIOSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssIOSent.setStatus("deprecated")
_SsIOReceive_Type = Integer32
_SsIOReceive_Object = MibScalar
ssIOReceive = _SsIOReceive_Object(
    (1, 3, 6, 1, 4, 1, 8673, 11, 6),
    _SsIOReceive_Type()
)
ssIOReceive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssIOReceive.setStatus("deprecated")
_SsSysInterrupts_Type = Integer32
_SsSysInterrupts_Object = MibScalar
ssSysInterrupts = _SsSysInterrupts_Object(
    (1, 3, 6, 1, 4, 1, 8673, 11, 7),
    _SsSysInterrupts_Type()
)
ssSysInterrupts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssSysInterrupts.setStatus("deprecated")
_SsSysContext_Type = Integer32
_SsSysContext_Object = MibScalar
ssSysContext = _SsSysContext_Object(
    (1, 3, 6, 1, 4, 1, 8673, 11, 8),
    _SsSysContext_Type()
)
ssSysContext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssSysContext.setStatus("deprecated")
_SsCpuUser_Type = Integer32
_SsCpuUser_Object = MibScalar
ssCpuUser = _SsCpuUser_Object(
    (1, 3, 6, 1, 4, 1, 8673, 11, 9),
    _SsCpuUser_Type()
)
ssCpuUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssCpuUser.setStatus("deprecated")
_SsCpuSystem_Type = Integer32
_SsCpuSystem_Object = MibScalar
ssCpuSystem = _SsCpuSystem_Object(
    (1, 3, 6, 1, 4, 1, 8673, 11, 10),
    _SsCpuSystem_Type()
)
ssCpuSystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssCpuSystem.setStatus("deprecated")
_SsCpuIdle_Type = Integer32
_SsCpuIdle_Object = MibScalar
ssCpuIdle = _SsCpuIdle_Object(
    (1, 3, 6, 1, 4, 1, 8673, 11, 11),
    _SsCpuIdle_Type()
)
ssCpuIdle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssCpuIdle.setStatus("deprecated")
_SsCpuRawUser_Type = Counter32
_SsCpuRawUser_Object = MibScalar
ssCpuRawUser = _SsCpuRawUser_Object(
    (1, 3, 6, 1, 4, 1, 8673, 11, 50),
    _SsCpuRawUser_Type()
)
ssCpuRawUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssCpuRawUser.setStatus("current")
_SsCpuRawNice_Type = Counter32
_SsCpuRawNice_Object = MibScalar
ssCpuRawNice = _SsCpuRawNice_Object(
    (1, 3, 6, 1, 4, 1, 8673, 11, 51),
    _SsCpuRawNice_Type()
)
ssCpuRawNice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssCpuRawNice.setStatus("current")
_SsCpuRawSystem_Type = Counter32
_SsCpuRawSystem_Object = MibScalar
ssCpuRawSystem = _SsCpuRawSystem_Object(
    (1, 3, 6, 1, 4, 1, 8673, 11, 52),
    _SsCpuRawSystem_Type()
)
ssCpuRawSystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssCpuRawSystem.setStatus("current")
_SsCpuRawIdle_Type = Counter32
_SsCpuRawIdle_Object = MibScalar
ssCpuRawIdle = _SsCpuRawIdle_Object(
    (1, 3, 6, 1, 4, 1, 8673, 11, 53),
    _SsCpuRawIdle_Type()
)
ssCpuRawIdle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssCpuRawIdle.setStatus("current")
_SsCpuRawWait_Type = Counter32
_SsCpuRawWait_Object = MibScalar
ssCpuRawWait = _SsCpuRawWait_Object(
    (1, 3, 6, 1, 4, 1, 8673, 11, 54),
    _SsCpuRawWait_Type()
)
ssCpuRawWait.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssCpuRawWait.setStatus("current")
_SsCpuRawKernel_Type = Counter32
_SsCpuRawKernel_Object = MibScalar
ssCpuRawKernel = _SsCpuRawKernel_Object(
    (1, 3, 6, 1, 4, 1, 8673, 11, 55),
    _SsCpuRawKernel_Type()
)
ssCpuRawKernel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssCpuRawKernel.setStatus("current")
_SsCpuRawInterrupt_Type = Counter32
_SsCpuRawInterrupt_Object = MibScalar
ssCpuRawInterrupt = _SsCpuRawInterrupt_Object(
    (1, 3, 6, 1, 4, 1, 8673, 11, 56),
    _SsCpuRawInterrupt_Type()
)
ssCpuRawInterrupt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssCpuRawInterrupt.setStatus("current")
_SsIORawSent_Type = Counter32
_SsIORawSent_Object = MibScalar
ssIORawSent = _SsIORawSent_Object(
    (1, 3, 6, 1, 4, 1, 8673, 11, 57),
    _SsIORawSent_Type()
)
ssIORawSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssIORawSent.setStatus("current")
_SsIORawReceived_Type = Counter32
_SsIORawReceived_Object = MibScalar
ssIORawReceived = _SsIORawReceived_Object(
    (1, 3, 6, 1, 4, 1, 8673, 11, 58),
    _SsIORawReceived_Type()
)
ssIORawReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssIORawReceived.setStatus("current")
_SsRawInterrupts_Type = Counter32
_SsRawInterrupts_Object = MibScalar
ssRawInterrupts = _SsRawInterrupts_Object(
    (1, 3, 6, 1, 4, 1, 8673, 11, 59),
    _SsRawInterrupts_Type()
)
ssRawInterrupts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssRawInterrupts.setStatus("current")
_SsRawContexts_Type = Counter32
_SsRawContexts_Object = MibScalar
ssRawContexts = _SsRawContexts_Object(
    (1, 3, 6, 1, 4, 1, 8673, 11, 60),
    _SsRawContexts_Type()
)
ssRawContexts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssRawContexts.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BORDERWARE-MIB",
    **{"Float": Float,
       "borderware": borderware,
       "bwProducts": bwProducts,
       "bwProductId": bwProductId,
       "bwFirewallServer7": bwFirewallServer7,
       "bwSysMemory": bwSysMemory,
       "memIndex": memIndex,
       "memErrorName": memErrorName,
       "memTotalSwap": memTotalSwap,
       "memAvailSwap": memAvailSwap,
       "memTotalReal": memTotalReal,
       "memAvailReal": memAvailReal,
       "memTotalSwapTXT": memTotalSwapTXT,
       "memAvailSwapTXT": memAvailSwapTXT,
       "memTotalRealTXT": memTotalRealTXT,
       "memAvailRealTXT": memAvailRealTXT,
       "memTotalFree": memTotalFree,
       "memMinimumSwap": memMinimumSwap,
       "memShared": memShared,
       "memBuffer": memBuffer,
       "memCached": memCached,
       "memSwapError": memSwapError,
       "memSwapErrorMsg": memSwapErrorMsg,
       "dskTable": dskTable,
       "dskEntry": dskEntry,
       "dskIndex": dskIndex,
       "dskPath": dskPath,
       "dskDevice": dskDevice,
       "dskMinimum": dskMinimum,
       "dskMinPercent": dskMinPercent,
       "dskTotal": dskTotal,
       "dskAvail": dskAvail,
       "dskUsed": dskUsed,
       "dskPercent": dskPercent,
       "dskPercentNode": dskPercentNode,
       "dskErrorFlag": dskErrorFlag,
       "dskErrorMsg": dskErrorMsg,
       "systemStats": systemStats,
       "ssIndex": ssIndex,
       "ssErrorName": ssErrorName,
       "ssSwapIn": ssSwapIn,
       "ssSwapOut": ssSwapOut,
       "ssIOSent": ssIOSent,
       "ssIOReceive": ssIOReceive,
       "ssSysInterrupts": ssSysInterrupts,
       "ssSysContext": ssSysContext,
       "ssCpuUser": ssCpuUser,
       "ssCpuSystem": ssCpuSystem,
       "ssCpuIdle": ssCpuIdle,
       "ssCpuRawUser": ssCpuRawUser,
       "ssCpuRawNice": ssCpuRawNice,
       "ssCpuRawSystem": ssCpuRawSystem,
       "ssCpuRawIdle": ssCpuRawIdle,
       "ssCpuRawWait": ssCpuRawWait,
       "ssCpuRawKernel": ssCpuRawKernel,
       "ssCpuRawInterrupt": ssCpuRawInterrupt,
       "ssIORawSent": ssIORawSent,
       "ssIORawReceived": ssIORawReceived,
       "ssRawInterrupts": ssRawInterrupts,
       "ssRawContexts": ssRawContexts}
)
