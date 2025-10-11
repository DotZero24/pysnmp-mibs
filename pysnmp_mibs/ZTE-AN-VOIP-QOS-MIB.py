# SNMP MIB module (ZTE-AN-VOIP-QOS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/zte/ZTE-AN-VOIP-QOS-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:44:57 2025
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

zxAnVoipQosMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Zte_ObjectIdentity = ObjectIdentity
zte = _Zte_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902)
)
_ZxAn_ObjectIdentity = ObjectIdentity
zxAn = _ZxAn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015)
)
_MsagmajorVersion_ObjectIdentity = ObjectIdentity
msagmajorVersion = _MsagmajorVersion_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3)
)
_MsagVoipQovs_ObjectIdentity = ObjectIdentity
msagVoipQovs = _MsagVoipQovs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 7)
)
_MsagVoipQovsParaSetTable_Object = MibTable
msagVoipQovsParaSetTable = _MsagVoipQovsParaSetTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 7, 1)
)
if mibBuilder.loadTexts:
    msagVoipQovsParaSetTable.setStatus("current")
_MsagVoipQovsParaSetEntry_Object = MibTableRow
msagVoipQovsParaSetEntry = _MsagVoipQovsParaSetEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 7, 1, 1)
)
msagVoipQovsParaSetEntry.setIndexNames(
    (0, "ZTE-AN-VOIP-QOS-MIB", "msagVoipQovsParaIndex"),
)
if mibBuilder.loadTexts:
    msagVoipQovsParaSetEntry.setStatus("current")


class _MsagVoipQovsParaIndex_Type(Integer32):
    """Custom type msagVoipQovsParaIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_MsagVoipQovsParaIndex_Type.__name__ = "Integer32"
_MsagVoipQovsParaIndex_Object = MibTableColumn
msagVoipQovsParaIndex = _MsagVoipQovsParaIndex_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 7, 1, 1, 1),
    _MsagVoipQovsParaIndex_Type()
)
msagVoipQovsParaIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    msagVoipQovsParaIndex.setStatus("current")


class _MsagVoipQovsParaTimer_Type(Integer32):
    """Custom type msagVoipQovsParaTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_MsagVoipQovsParaTimer_Type.__name__ = "Integer32"
_MsagVoipQovsParaTimer_Object = MibTableColumn
msagVoipQovsParaTimer = _MsagVoipQovsParaTimer_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 7, 1, 1, 2),
    _MsagVoipQovsParaTimer_Type()
)
msagVoipQovsParaTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msagVoipQovsParaTimer.setStatus("current")


class _MsagVoipQovsParaDelayThresh_Type(Integer32):
    """Custom type msagVoipQovsParaDelayThresh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_MsagVoipQovsParaDelayThresh_Type.__name__ = "Integer32"
_MsagVoipQovsParaDelayThresh_Object = MibTableColumn
msagVoipQovsParaDelayThresh = _MsagVoipQovsParaDelayThresh_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 7, 1, 1, 3),
    _MsagVoipQovsParaDelayThresh_Type()
)
msagVoipQovsParaDelayThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msagVoipQovsParaDelayThresh.setStatus("current")


class _MsagVoipQovsParaLossThresh_Type(Integer32):
    """Custom type msagVoipQovsParaLossThresh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_MsagVoipQovsParaLossThresh_Type.__name__ = "Integer32"
_MsagVoipQovsParaLossThresh_Object = MibTableColumn
msagVoipQovsParaLossThresh = _MsagVoipQovsParaLossThresh_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 7, 1, 1, 4),
    _MsagVoipQovsParaLossThresh_Type()
)
msagVoipQovsParaLossThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msagVoipQovsParaLossThresh.setStatus("current")


class _MsagVoipQovsParaJitterThresh_Type(Integer32):
    """Custom type msagVoipQovsParaJitterThresh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_MsagVoipQovsParaJitterThresh_Type.__name__ = "Integer32"
_MsagVoipQovsParaJitterThresh_Object = MibTableColumn
msagVoipQovsParaJitterThresh = _MsagVoipQovsParaJitterThresh_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 7, 1, 1, 5),
    _MsagVoipQovsParaJitterThresh_Type()
)
msagVoipQovsParaJitterThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msagVoipQovsParaJitterThresh.setStatus("current")
_MsagVoipQovsCommandTable_Object = MibTable
msagVoipQovsCommandTable = _MsagVoipQovsCommandTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 7, 2)
)
if mibBuilder.loadTexts:
    msagVoipQovsCommandTable.setStatus("current")
_MsagVoipQovsCommandEntry_Object = MibTableRow
msagVoipQovsCommandEntry = _MsagVoipQovsCommandEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 7, 2, 1)
)
msagVoipQovsCommandEntry.setIndexNames(
    (0, "ZTE-AN-VOIP-QOS-MIB", "msagVoipQovsCmdRackno"),
    (0, "ZTE-AN-VOIP-QOS-MIB", "msagVoipQovsCmdShelfno"),
    (0, "ZTE-AN-VOIP-QOS-MIB", "msagVoipQovsCmdSlotno"),
    (0, "ZTE-AN-VOIP-QOS-MIB", "msagVoipQovsCmdIndex"),
)
if mibBuilder.loadTexts:
    msagVoipQovsCommandEntry.setStatus("current")


class _MsagVoipQovsCmdRackno_Type(Integer32):
    """Custom type msagVoipQovsCmdRackno based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_MsagVoipQovsCmdRackno_Type.__name__ = "Integer32"
_MsagVoipQovsCmdRackno_Object = MibTableColumn
msagVoipQovsCmdRackno = _MsagVoipQovsCmdRackno_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 7, 2, 1, 1),
    _MsagVoipQovsCmdRackno_Type()
)
msagVoipQovsCmdRackno.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    msagVoipQovsCmdRackno.setStatus("current")


class _MsagVoipQovsCmdShelfno_Type(Integer32):
    """Custom type msagVoipQovsCmdShelfno based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_MsagVoipQovsCmdShelfno_Type.__name__ = "Integer32"
_MsagVoipQovsCmdShelfno_Object = MibTableColumn
msagVoipQovsCmdShelfno = _MsagVoipQovsCmdShelfno_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 7, 2, 1, 2),
    _MsagVoipQovsCmdShelfno_Type()
)
msagVoipQovsCmdShelfno.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    msagVoipQovsCmdShelfno.setStatus("current")


class _MsagVoipQovsCmdSlotno_Type(Integer32):
    """Custom type msagVoipQovsCmdSlotno based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 23),
    )


_MsagVoipQovsCmdSlotno_Type.__name__ = "Integer32"
_MsagVoipQovsCmdSlotno_Object = MibTableColumn
msagVoipQovsCmdSlotno = _MsagVoipQovsCmdSlotno_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 7, 2, 1, 3),
    _MsagVoipQovsCmdSlotno_Type()
)
msagVoipQovsCmdSlotno.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    msagVoipQovsCmdSlotno.setStatus("current")


class _MsagVoipQovsCmdIndex_Type(Integer32):
    """Custom type msagVoipQovsCmdIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 23),
    )


_MsagVoipQovsCmdIndex_Type.__name__ = "Integer32"
_MsagVoipQovsCmdIndex_Object = MibTableColumn
msagVoipQovsCmdIndex = _MsagVoipQovsCmdIndex_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 7, 2, 1, 4),
    _MsagVoipQovsCmdIndex_Type()
)
msagVoipQovsCmdIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    msagVoipQovsCmdIndex.setStatus("current")


class _MsagVoipQovsCmdno_Type(Integer32):
    """Custom type msagVoipQovsCmdno based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cmdStart", 1),
          ("cmdEnd", 2))
    )


_MsagVoipQovsCmdno_Type.__name__ = "Integer32"
_MsagVoipQovsCmdno_Object = MibTableColumn
msagVoipQovsCmdno = _MsagVoipQovsCmdno_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 7, 2, 1, 5),
    _MsagVoipQovsCmdno_Type()
)
msagVoipQovsCmdno.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msagVoipQovsCmdno.setStatus("current")
_MsagVoipQovsResultTable_Object = MibTable
msagVoipQovsResultTable = _MsagVoipQovsResultTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 7, 3)
)
if mibBuilder.loadTexts:
    msagVoipQovsResultTable.setStatus("current")
_MsagVoipQovsResultEntry_Object = MibTableRow
msagVoipQovsResultEntry = _MsagVoipQovsResultEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 7, 3, 1)
)
msagVoipQovsResultEntry.setIndexNames(
    (0, "ZTE-AN-VOIP-QOS-MIB", "msagVoipQRRackno"),
    (0, "ZTE-AN-VOIP-QOS-MIB", "msagVoipQRShelfno"),
    (0, "ZTE-AN-VOIP-QOS-MIB", "msagVoipQRSlotno"),
    (0, "ZTE-AN-VOIP-QOS-MIB", "msagVoipQRIndex"),
)
if mibBuilder.loadTexts:
    msagVoipQovsResultEntry.setStatus("current")


class _MsagVoipQRRackno_Type(Integer32):
    """Custom type msagVoipQRRackno based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_MsagVoipQRRackno_Type.__name__ = "Integer32"
_MsagVoipQRRackno_Object = MibTableColumn
msagVoipQRRackno = _MsagVoipQRRackno_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 7, 3, 1, 1),
    _MsagVoipQRRackno_Type()
)
msagVoipQRRackno.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    msagVoipQRRackno.setStatus("current")


class _MsagVoipQRShelfno_Type(Integer32):
    """Custom type msagVoipQRShelfno based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_MsagVoipQRShelfno_Type.__name__ = "Integer32"
_MsagVoipQRShelfno_Object = MibTableColumn
msagVoipQRShelfno = _MsagVoipQRShelfno_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 7, 3, 1, 2),
    _MsagVoipQRShelfno_Type()
)
msagVoipQRShelfno.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    msagVoipQRShelfno.setStatus("current")


class _MsagVoipQRSlotno_Type(Integer32):
    """Custom type msagVoipQRSlotno based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 23),
    )


_MsagVoipQRSlotno_Type.__name__ = "Integer32"
_MsagVoipQRSlotno_Object = MibTableColumn
msagVoipQRSlotno = _MsagVoipQRSlotno_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 7, 3, 1, 3),
    _MsagVoipQRSlotno_Type()
)
msagVoipQRSlotno.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    msagVoipQRSlotno.setStatus("current")


class _MsagVoipQRIndex_Type(Integer32):
    """Custom type msagVoipQRIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 23),
    )


_MsagVoipQRIndex_Type.__name__ = "Integer32"
_MsagVoipQRIndex_Object = MibTableColumn
msagVoipQRIndex = _MsagVoipQRIndex_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 7, 3, 1, 4),
    _MsagVoipQRIndex_Type()
)
msagVoipQRIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    msagVoipQRIndex.setStatus("current")


class _MsagVoipQRDelay_Type(Integer32):
    """Custom type msagVoipQRDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_MsagVoipQRDelay_Type.__name__ = "Integer32"
_MsagVoipQRDelay_Object = MibTableColumn
msagVoipQRDelay = _MsagVoipQRDelay_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 7, 3, 1, 5),
    _MsagVoipQRDelay_Type()
)
msagVoipQRDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msagVoipQRDelay.setStatus("current")


class _MsagVoipQRLoss_Type(Integer32):
    """Custom type msagVoipQRLoss based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_MsagVoipQRLoss_Type.__name__ = "Integer32"
_MsagVoipQRLoss_Object = MibTableColumn
msagVoipQRLoss = _MsagVoipQRLoss_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 7, 3, 1, 6),
    _MsagVoipQRLoss_Type()
)
msagVoipQRLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msagVoipQRLoss.setStatus("current")


class _MsagVoipQRJitter_Type(Integer32):
    """Custom type msagVoipQRJitter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_MsagVoipQRJitter_Type.__name__ = "Integer32"
_MsagVoipQRJitter_Object = MibTableColumn
msagVoipQRJitter = _MsagVoipQRJitter_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 7, 3, 1, 7),
    _MsagVoipQRJitter_Type()
)
msagVoipQRJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msagVoipQRJitter.setStatus("current")
_MsagVoipQRSrcPort_Type = Integer32
_MsagVoipQRSrcPort_Object = MibTableColumn
msagVoipQRSrcPort = _MsagVoipQRSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 7, 3, 1, 8),
    _MsagVoipQRSrcPort_Type()
)
msagVoipQRSrcPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msagVoipQRSrcPort.setStatus("current")
_MsagVoipQRDestPort_Type = Integer32
_MsagVoipQRDestPort_Object = MibTableColumn
msagVoipQRDestPort = _MsagVoipQRDestPort_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 7, 3, 1, 9),
    _MsagVoipQRDestPort_Type()
)
msagVoipQRDestPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msagVoipQRDestPort.setStatus("current")
_MsagVoipQRSrcIPAddr_Type = IpAddress
_MsagVoipQRSrcIPAddr_Object = MibTableColumn
msagVoipQRSrcIPAddr = _MsagVoipQRSrcIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 7, 3, 1, 10),
    _MsagVoipQRSrcIPAddr_Type()
)
msagVoipQRSrcIPAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msagVoipQRSrcIPAddr.setStatus("current")
_MsagVoipQRTime_Type = Integer32
_MsagVoipQRTime_Object = MibTableColumn
msagVoipQRTime = _MsagVoipQRTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 7, 3, 1, 11),
    _MsagVoipQRTime_Type()
)
msagVoipQRTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msagVoipQRTime.setStatus("current")
_MsagVoipQRMos_Type = Integer32
_MsagVoipQRMos_Object = MibTableColumn
msagVoipQRMos = _MsagVoipQRMos_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 7, 3, 1, 12),
    _MsagVoipQRMos_Type()
)
msagVoipQRMos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msagVoipQRMos.setStatus("current")
_MsagVoipQRLossRate_Type = Integer32
_MsagVoipQRLossRate_Object = MibTableColumn
msagVoipQRLossRate = _MsagVoipQRLossRate_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 7, 3, 1, 13),
    _MsagVoipQRLossRate_Type()
)
msagVoipQRLossRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msagVoipQRLossRate.setStatus("current")
_MsagVoipQRsignalLev_Type = Integer32
_MsagVoipQRsignalLev_Object = MibTableColumn
msagVoipQRsignalLev = _MsagVoipQRsignalLev_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 7, 3, 1, 14),
    _MsagVoipQRsignalLev_Type()
)
msagVoipQRsignalLev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msagVoipQRsignalLev.setStatus("current")
_MsagVoipQRnoiseLev_Type = Integer32
_MsagVoipQRnoiseLev_Object = MibTableColumn
msagVoipQRnoiseLev = _MsagVoipQRnoiseLev_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 7, 3, 1, 15),
    _MsagVoipQRnoiseLev_Type()
)
msagVoipQRnoiseLev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msagVoipQRnoiseLev.setStatus("current")
_MsagVoipQRRERL_Type = Integer32
_MsagVoipQRRERL_Object = MibTableColumn
msagVoipQRRERL = _MsagVoipQRRERL_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 7, 3, 1, 16),
    _MsagVoipQRRERL_Type()
)
msagVoipQRRERL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msagVoipQRRERL.setStatus("current")
_MsagVoipQRBurstDuration_Type = Integer32
_MsagVoipQRBurstDuration_Object = MibTableColumn
msagVoipQRBurstDuration = _MsagVoipQRBurstDuration_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 7, 3, 1, 17),
    _MsagVoipQRBurstDuration_Type()
)
msagVoipQRBurstDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msagVoipQRBurstDuration.setStatus("current")
_MsagVoipQRgapDuration_Type = Integer32
_MsagVoipQRgapDuration_Object = MibTableColumn
msagVoipQRgapDuration = _MsagVoipQRgapDuration_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 7, 3, 1, 18),
    _MsagVoipQRgapDuration_Type()
)
msagVoipQRgapDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msagVoipQRgapDuration.setStatus("current")
_MsagVoipQRBurstDensity_Type = Integer32
_MsagVoipQRBurstDensity_Object = MibTableColumn
msagVoipQRBurstDensity = _MsagVoipQRBurstDensity_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 7, 3, 1, 19),
    _MsagVoipQRBurstDensity_Type()
)
msagVoipQRBurstDensity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msagVoipQRBurstDensity.setStatus("current")
_MsagVoipQRGapDensity_Type = Integer32
_MsagVoipQRGapDensity_Object = MibTableColumn
msagVoipQRGapDensity = _MsagVoipQRGapDensity_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 7, 3, 1, 20),
    _MsagVoipQRGapDensity_Type()
)
msagVoipQRGapDensity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msagVoipQRGapDensity.setStatus("current")
_MsagNarrowGetNext_Type = Integer32
_MsagNarrowGetNext_Object = MibScalar
msagNarrowGetNext = _MsagNarrowGetNext_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 7, 10),
    _MsagNarrowGetNext_Type()
)
msagNarrowGetNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msagNarrowGetNext.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZTE-AN-VOIP-QOS-MIB",
    **{"zte": zte,
       "zxAn": zxAn,
       "zxAnVoipQosMib": zxAnVoipQosMib,
       "msagmajorVersion": msagmajorVersion,
       "msagVoipQovs": msagVoipQovs,
       "msagVoipQovsParaSetTable": msagVoipQovsParaSetTable,
       "msagVoipQovsParaSetEntry": msagVoipQovsParaSetEntry,
       "msagVoipQovsParaIndex": msagVoipQovsParaIndex,
       "msagVoipQovsParaTimer": msagVoipQovsParaTimer,
       "msagVoipQovsParaDelayThresh": msagVoipQovsParaDelayThresh,
       "msagVoipQovsParaLossThresh": msagVoipQovsParaLossThresh,
       "msagVoipQovsParaJitterThresh": msagVoipQovsParaJitterThresh,
       "msagVoipQovsCommandTable": msagVoipQovsCommandTable,
       "msagVoipQovsCommandEntry": msagVoipQovsCommandEntry,
       "msagVoipQovsCmdRackno": msagVoipQovsCmdRackno,
       "msagVoipQovsCmdShelfno": msagVoipQovsCmdShelfno,
       "msagVoipQovsCmdSlotno": msagVoipQovsCmdSlotno,
       "msagVoipQovsCmdIndex": msagVoipQovsCmdIndex,
       "msagVoipQovsCmdno": msagVoipQovsCmdno,
       "msagVoipQovsResultTable": msagVoipQovsResultTable,
       "msagVoipQovsResultEntry": msagVoipQovsResultEntry,
       "msagVoipQRRackno": msagVoipQRRackno,
       "msagVoipQRShelfno": msagVoipQRShelfno,
       "msagVoipQRSlotno": msagVoipQRSlotno,
       "msagVoipQRIndex": msagVoipQRIndex,
       "msagVoipQRDelay": msagVoipQRDelay,
       "msagVoipQRLoss": msagVoipQRLoss,
       "msagVoipQRJitter": msagVoipQRJitter,
       "msagVoipQRSrcPort": msagVoipQRSrcPort,
       "msagVoipQRDestPort": msagVoipQRDestPort,
       "msagVoipQRSrcIPAddr": msagVoipQRSrcIPAddr,
       "msagVoipQRTime": msagVoipQRTime,
       "msagVoipQRMos": msagVoipQRMos,
       "msagVoipQRLossRate": msagVoipQRLossRate,
       "msagVoipQRsignalLev": msagVoipQRsignalLev,
       "msagVoipQRnoiseLev": msagVoipQRnoiseLev,
       "msagVoipQRRERL": msagVoipQRRERL,
       "msagVoipQRBurstDuration": msagVoipQRBurstDuration,
       "msagVoipQRgapDuration": msagVoipQRgapDuration,
       "msagVoipQRBurstDensity": msagVoipQRBurstDensity,
       "msagVoipQRGapDensity": msagVoipQRGapDensity,
       "msagNarrowGetNext": msagNarrowGetNext}
)
