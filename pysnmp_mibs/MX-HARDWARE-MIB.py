# SNMP MIB module (MX-HARDWARE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/media5/MX-HARDWARE-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:06:28 2025
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

(mediatrixHardware,) = mibBuilder.importSymbols(
    "MX-SMI2",
    "mediatrixHardware")

(MxActivationState,
 MxAdvancedIpPort,
 MxDigitMap,
 MxEnableState,
 MxIpAddress,
 MxIpHostName,
 MxIpPort,
 MxIpSubnetMask) = mibBuilder.importSymbols(
    "MX-TC",
    "MxActivationState",
    "MxAdvancedIpPort",
    "MxDigitMap",
    "MxEnableState",
    "MxIpAddress",
    "MxIpHostName",
    "MxIpPort",
    "MxIpSubnetMask")

(MxFloat32,
 MxIpAddr,
 MxIpAddrMask,
 MxIpAddrPort,
 MxIpHostNamePort,
 MxUInt64,
 MxUri,
 MxUrl) = mibBuilder.importSymbols(
    "MX-TC2",
    "MxFloat32",
    "MxIpAddr",
    "MxIpAddrMask",
    "MxIpAddrPort",
    "MxIpHostNamePort",
    "MxUInt64",
    "MxUri",
    "MxUrl")

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

hardwareMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 500, 40000)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HardwareMIBObjects_ObjectIdentity = ObjectIdentity
hardwareMIBObjects = _HardwareMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 500, 40000, 1)
)


class _ResetButtonManagement_Type(Integer32):
    """Custom type resetButtonManagement based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200)
        )
    )
    namedValues = NamedValues(
        *(("all", 100),
          ("disablePartialReset", 200))
    )


_ResetButtonManagement_Type.__name__ = "Integer32"
_ResetButtonManagement_Object = MibScalar
resetButtonManagement = _ResetButtonManagement_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 500, 40000, 1, 100),
    _ResetButtonManagement_Type()
)
resetButtonManagement.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    resetButtonManagement.setStatus("current")


class _InteropForceDspResync_Type(Integer32):
    """Custom type interopForceDspResync based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200)
        )
    )
    namedValues = NamedValues(
        *(("disable", 100),
          ("enable", 200))
    )


_InteropForceDspResync_Type.__name__ = "Integer32"
_InteropForceDspResync_Object = MibScalar
interopForceDspResync = _InteropForceDspResync_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 500, 40000, 1, 200),
    _InteropForceDspResync_Type()
)
interopForceDspResync.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    interopForceDspResync.setStatus("current")
_Fxs_ObjectIdentity = ObjectIdentity
fxs = _Fxs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 500, 40000, 1, 1000)
)


class _RingManagement_Type(Integer32):
    """Custom type ringManagement based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200)
        )
    )
    namedValues = NamedValues(
        *(("cascade", 100),
          ("simultaneous", 200))
    )


_RingManagement_Type.__name__ = "Integer32"
_RingManagement_Object = MibScalar
ringManagement = _RingManagement_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 500, 40000, 1, 1000, 100),
    _RingManagement_Type()
)
ringManagement.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ringManagement.setStatus("current")
_Pri_ObjectIdentity = ObjectIdentity
pri = _Pri_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 500, 40000, 1, 2000)
)
_PortsStatusTable_Object = MibTable
portsStatusTable = _PortsStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 500, 40000, 1, 2000, 100)
)
if mibBuilder.loadTexts:
    portsStatusTable.setStatus("current")
_PortsStatusEntry_Object = MibTableRow
portsStatusEntry = _PortsStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 500, 40000, 1, 2000, 100, 1)
)
portsStatusEntry.setIndexNames(
    (0, "MX-HARDWARE-MIB", "portsStatusPort"),
)
if mibBuilder.loadTexts:
    portsStatusEntry.setStatus("current")
_PortsStatusPort_Type = OctetString
_PortsStatusPort_Object = MibTableColumn
portsStatusPort = _PortsStatusPort_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 500, 40000, 1, 2000, 100, 1, 100),
    _PortsStatusPort_Type()
)
portsStatusPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portsStatusPort.setStatus("current")


class _PortsStatusLineType_Type(Integer32):
    """Custom type portsStatusLineType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200)
        )
    )
    namedValues = NamedValues(
        *(("e1", 100),
          ("t1", 200))
    )


_PortsStatusLineType_Type.__name__ = "Integer32"
_PortsStatusLineType_Object = MibTableColumn
portsStatusLineType = _PortsStatusLineType_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 500, 40000, 1, 2000, 100, 1, 300),
    _PortsStatusLineType_Type()
)
portsStatusLineType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portsStatusLineType.setStatus("current")


class _PortsStatusSignaling_Type(Integer32):
    """Custom type portsStatusSignaling based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200,
              300)
        )
    )
    namedValues = NamedValues(
        *(("isdn", 100),
          ("r2", 200),
          ("eam", 300))
    )


_PortsStatusSignaling_Type.__name__ = "Integer32"
_PortsStatusSignaling_Object = MibTableColumn
portsStatusSignaling = _PortsStatusSignaling_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 500, 40000, 1, 2000, 100, 1, 400),
    _PortsStatusSignaling_Type()
)
portsStatusSignaling.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portsStatusSignaling.setStatus("current")
_PortsTable_Object = MibTable
portsTable = _PortsTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 500, 40000, 1, 2000, 200)
)
if mibBuilder.loadTexts:
    portsTable.setStatus("current")
_PortsEntry_Object = MibTableRow
portsEntry = _PortsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 500, 40000, 1, 2000, 200, 1)
)
portsEntry.setIndexNames(
    (0, "MX-HARDWARE-MIB", "portsPort"),
)
if mibBuilder.loadTexts:
    portsEntry.setStatus("current")
_PortsPort_Type = OctetString
_PortsPort_Object = MibTableColumn
portsPort = _PortsPort_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 500, 40000, 1, 2000, 200, 1, 100),
    _PortsPort_Type()
)
portsPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portsPort.setStatus("current")


class _PortsLineType_Type(Integer32):
    """Custom type portsLineType based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200)
        )
    )
    namedValues = NamedValues(
        *(("e1", 100),
          ("t1", 200))
    )


_PortsLineType_Type.__name__ = "Integer32"
_PortsLineType_Object = MibTableColumn
portsLineType = _PortsLineType_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 500, 40000, 1, 2000, 200, 1, 300),
    _PortsLineType_Type()
)
portsLineType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portsLineType.setStatus("current")


class _PortsSignaling_Type(Integer32):
    """Custom type portsSignaling based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200,
              300)
        )
    )
    namedValues = NamedValues(
        *(("isdn", 100),
          ("r2", 200),
          ("eam", 300))
    )


_PortsSignaling_Type.__name__ = "Integer32"
_PortsSignaling_Object = MibTableColumn
portsSignaling = _PortsSignaling_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 500, 40000, 1, 2000, 200, 1, 400),
    _PortsSignaling_Type()
)
portsSignaling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portsSignaling.setStatus("current")
_StatisticsGroup_ObjectIdentity = ObjectIdentity
statisticsGroup = _StatisticsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 500, 40000, 1, 2000, 1000)
)
_StatsInfoTable_Object = MibTable
statsInfoTable = _StatsInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 500, 40000, 1, 2000, 1000, 100)
)
if mibBuilder.loadTexts:
    statsInfoTable.setStatus("current")
_StatsInfoEntry_Object = MibTableRow
statsInfoEntry = _StatsInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 500, 40000, 1, 2000, 1000, 100, 1)
)
statsInfoEntry.setIndexNames(
    (0, "MX-HARDWARE-MIB", "statsInfoPort"),
)
if mibBuilder.loadTexts:
    statsInfoEntry.setStatus("current")
_StatsInfoPort_Type = OctetString
_StatsInfoPort_Object = MibTableColumn
statsInfoPort = _StatsInfoPort_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 500, 40000, 1, 2000, 1000, 100, 1, 100),
    _StatsInfoPort_Type()
)
statsInfoPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statsInfoPort.setStatus("current")
_StatsInfoFramesTransmitted_Type = Unsigned32
_StatsInfoFramesTransmitted_Object = MibTableColumn
statsInfoFramesTransmitted = _StatsInfoFramesTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 500, 40000, 1, 2000, 1000, 100, 1, 200),
    _StatsInfoFramesTransmitted_Type()
)
statsInfoFramesTransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statsInfoFramesTransmitted.setStatus("current")
_StatsInfoFramesReceived_Type = Unsigned32
_StatsInfoFramesReceived_Object = MibTableColumn
statsInfoFramesReceived = _StatsInfoFramesReceived_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 500, 40000, 1, 2000, 1000, 100, 1, 300),
    _StatsInfoFramesReceived_Type()
)
statsInfoFramesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statsInfoFramesReceived.setStatus("current")
_StatsInfoOctetsTransmitted_Type = Unsigned32
_StatsInfoOctetsTransmitted_Object = MibTableColumn
statsInfoOctetsTransmitted = _StatsInfoOctetsTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 500, 40000, 1, 2000, 1000, 100, 1, 400),
    _StatsInfoOctetsTransmitted_Type()
)
statsInfoOctetsTransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statsInfoOctetsTransmitted.setStatus("current")
_StatsInfoOctetsReceived_Type = Unsigned32
_StatsInfoOctetsReceived_Object = MibTableColumn
statsInfoOctetsReceived = _StatsInfoOctetsReceived_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 500, 40000, 1, 2000, 1000, 100, 1, 500),
    _StatsInfoOctetsReceived_Type()
)
statsInfoOctetsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statsInfoOctetsReceived.setStatus("current")
_StatsInfoFcsErrors_Type = Unsigned32
_StatsInfoFcsErrors_Object = MibTableColumn
statsInfoFcsErrors = _StatsInfoFcsErrors_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 500, 40000, 1, 2000, 1000, 100, 1, 600),
    _StatsInfoFcsErrors_Type()
)
statsInfoFcsErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statsInfoFcsErrors.setStatus("current")
_StatsInfoFramesDropped_Type = Unsigned32
_StatsInfoFramesDropped_Object = MibTableColumn
statsInfoFramesDropped = _StatsInfoFramesDropped_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 500, 40000, 1, 2000, 1000, 100, 1, 700),
    _StatsInfoFramesDropped_Type()
)
statsInfoFramesDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statsInfoFramesDropped.setStatus("current")
_StatsInfoOctetsDropped_Type = Unsigned32
_StatsInfoOctetsDropped_Object = MibTableColumn
statsInfoOctetsDropped = _StatsInfoOctetsDropped_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 500, 40000, 1, 2000, 1000, 100, 1, 800),
    _StatsInfoOctetsDropped_Type()
)
statsInfoOctetsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statsInfoOctetsDropped.setStatus("current")
_StatsInfoNegativeFrameSlipsTransmitted_Type = Unsigned32
_StatsInfoNegativeFrameSlipsTransmitted_Object = MibTableColumn
statsInfoNegativeFrameSlipsTransmitted = _StatsInfoNegativeFrameSlipsTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 500, 40000, 1, 2000, 1000, 100, 1, 900),
    _StatsInfoNegativeFrameSlipsTransmitted_Type()
)
statsInfoNegativeFrameSlipsTransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statsInfoNegativeFrameSlipsTransmitted.setStatus("current")
_StatsInfoNegativeFrameSlipsReceived_Type = Unsigned32
_StatsInfoNegativeFrameSlipsReceived_Object = MibTableColumn
statsInfoNegativeFrameSlipsReceived = _StatsInfoNegativeFrameSlipsReceived_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 500, 40000, 1, 2000, 1000, 100, 1, 1000),
    _StatsInfoNegativeFrameSlipsReceived_Type()
)
statsInfoNegativeFrameSlipsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statsInfoNegativeFrameSlipsReceived.setStatus("current")
_StatsInfoPositiveFrameSlipsTransmitted_Type = Unsigned32
_StatsInfoPositiveFrameSlipsTransmitted_Object = MibTableColumn
statsInfoPositiveFrameSlipsTransmitted = _StatsInfoPositiveFrameSlipsTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 500, 40000, 1, 2000, 1000, 100, 1, 1100),
    _StatsInfoPositiveFrameSlipsTransmitted_Type()
)
statsInfoPositiveFrameSlipsTransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statsInfoPositiveFrameSlipsTransmitted.setStatus("current")
_StatsInfoPositiveFrameSlipsReceived_Type = Unsigned32
_StatsInfoPositiveFrameSlipsReceived_Object = MibTableColumn
statsInfoPositiveFrameSlipsReceived = _StatsInfoPositiveFrameSlipsReceived_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 500, 40000, 1, 2000, 1000, 100, 1, 1200),
    _StatsInfoPositiveFrameSlipsReceived_Type()
)
statsInfoPositiveFrameSlipsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statsInfoPositiveFrameSlipsReceived.setStatus("current")
_StatsInfoFramingErrors_Type = Unsigned32
_StatsInfoFramingErrors_Object = MibTableColumn
statsInfoFramingErrors = _StatsInfoFramingErrors_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 500, 40000, 1, 2000, 1000, 100, 1, 1300),
    _StatsInfoFramingErrors_Type()
)
statsInfoFramingErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statsInfoFramingErrors.setStatus("current")
_StatsInfoCodeViolations_Type = Unsigned32
_StatsInfoCodeViolations_Object = MibTableColumn
statsInfoCodeViolations = _StatsInfoCodeViolations_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 500, 40000, 1, 2000, 1000, 100, 1, 1400),
    _StatsInfoCodeViolations_Type()
)
statsInfoCodeViolations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statsInfoCodeViolations.setStatus("current")
_StatsInfoCRCErrors_Type = Unsigned32
_StatsInfoCRCErrors_Object = MibTableColumn
statsInfoCRCErrors = _StatsInfoCRCErrors_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 500, 40000, 1, 2000, 1000, 100, 1, 1500),
    _StatsInfoCRCErrors_Type()
)
statsInfoCRCErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statsInfoCRCErrors.setStatus("current")
_StatsInfoEBitErrors_Type = Unsigned32
_StatsInfoEBitErrors_Object = MibTableColumn
statsInfoEBitErrors = _StatsInfoEBitErrors_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 500, 40000, 1, 2000, 1000, 100, 1, 1600),
    _StatsInfoEBitErrors_Type()
)
statsInfoEBitErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statsInfoEBitErrors.setStatus("current")
_StatsInfoBlockErrors_Type = Unsigned32
_StatsInfoBlockErrors_Object = MibTableColumn
statsInfoBlockErrors = _StatsInfoBlockErrors_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 500, 40000, 1, 2000, 1000, 100, 1, 1700),
    _StatsInfoBlockErrors_Type()
)
statsInfoBlockErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statsInfoBlockErrors.setStatus("current")


class _StatsInfoResetStats_Type(Integer32):
    """Custom type statsInfoResetStats based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              10)
        )
    )
    namedValues = NamedValues(
        *(("noOp", 0),
          ("resetStats", 10))
    )


_StatsInfoResetStats_Type.__name__ = "Integer32"
_StatsInfoResetStats_Object = MibTableColumn
statsInfoResetStats = _StatsInfoResetStats_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 500, 40000, 1, 2000, 1000, 100, 1, 10000),
    _StatsInfoResetStats_Type()
)
statsInfoResetStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    statsInfoResetStats.setStatus("current")
_Bri_ObjectIdentity = ObjectIdentity
bri = _Bri_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 500, 40000, 1, 3000)
)
_BriPortsStatusTable_Object = MibTable
briPortsStatusTable = _BriPortsStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 500, 40000, 1, 3000, 100)
)
if mibBuilder.loadTexts:
    briPortsStatusTable.setStatus("current")
_BriPortsStatusEntry_Object = MibTableRow
briPortsStatusEntry = _BriPortsStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 500, 40000, 1, 3000, 100, 1)
)
briPortsStatusEntry.setIndexNames(
    (0, "MX-HARDWARE-MIB", "briPortsStatusPort"),
)
if mibBuilder.loadTexts:
    briPortsStatusEntry.setStatus("current")
_BriPortsStatusPort_Type = OctetString
_BriPortsStatusPort_Object = MibTableColumn
briPortsStatusPort = _BriPortsStatusPort_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 500, 40000, 1, 3000, 100, 1, 100),
    _BriPortsStatusPort_Type()
)
briPortsStatusPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    briPortsStatusPort.setStatus("current")


class _BriPortsStatusPowerFeeding_Type(Integer32):
    """Custom type briPortsStatusPowerFeeding based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200,
              300,
              400)
        )
    )
    namedValues = NamedValues(
        *(("on", 100),
          ("off", 200),
          ("unavailable", 300),
          ("unsupported", 400))
    )


_BriPortsStatusPowerFeeding_Type.__name__ = "Integer32"
_BriPortsStatusPowerFeeding_Object = MibTableColumn
briPortsStatusPowerFeeding = _BriPortsStatusPowerFeeding_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 500, 40000, 1, 3000, 100, 1, 200),
    _BriPortsStatusPowerFeeding_Type()
)
briPortsStatusPowerFeeding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    briPortsStatusPowerFeeding.setStatus("current")
_BriPortsTable_Object = MibTable
briPortsTable = _BriPortsTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 500, 40000, 1, 3000, 200)
)
if mibBuilder.loadTexts:
    briPortsTable.setStatus("current")
_BriPortsEntry_Object = MibTableRow
briPortsEntry = _BriPortsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 500, 40000, 1, 3000, 200, 1)
)
briPortsEntry.setIndexNames(
    (0, "MX-HARDWARE-MIB", "briPortsPort"),
)
if mibBuilder.loadTexts:
    briPortsEntry.setStatus("current")
_BriPortsPort_Type = OctetString
_BriPortsPort_Object = MibTableColumn
briPortsPort = _BriPortsPort_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 500, 40000, 1, 3000, 200, 1, 100),
    _BriPortsPort_Type()
)
briPortsPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    briPortsPort.setStatus("current")


class _BriPortsPowerFeedingEnable_Type(MxEnableState):
    """Custom type briPortsPowerFeedingEnable based on MxEnableState"""
    defaultValue = 0


_BriPortsPowerFeedingEnable_Type.__name__ = "MxEnableState"
_BriPortsPowerFeedingEnable_Object = MibTableColumn
briPortsPowerFeedingEnable = _BriPortsPowerFeedingEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 500, 40000, 1, 3000, 200, 1, 200),
    _BriPortsPowerFeedingEnable_Type()
)
briPortsPowerFeedingEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    briPortsPowerFeedingEnable.setStatus("current")
_ClockReference_ObjectIdentity = ObjectIdentity
clockReference = _ClockReference_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 500, 40000, 1, 5000)
)
_ClockReferenceList_Type = OctetString
_ClockReferenceList_Object = MibScalar
clockReferenceList = _ClockReferenceList_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 500, 40000, 1, 5000, 100),
    _ClockReferenceList_Type()
)
clockReferenceList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clockReferenceList.setStatus("current")


class _ClockReferenceSource_Type(OctetString):
    """Custom type clockReferenceSource based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ClockReferenceSource_Type.__name__ = "OctetString"
_ClockReferenceSource_Object = MibScalar
clockReferenceSource = _ClockReferenceSource_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 500, 40000, 1, 5000, 200),
    _ClockReferenceSource_Type()
)
clockReferenceSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clockReferenceSource.setStatus("current")
_ClockReferenceStatus_Type = OctetString
_ClockReferenceStatus_Object = MibScalar
clockReferenceStatus = _ClockReferenceStatus_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 500, 40000, 1, 5000, 300),
    _ClockReferenceStatus_Type()
)
clockReferenceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clockReferenceStatus.setStatus("current")
_Eth_ObjectIdentity = ObjectIdentity
eth = _Eth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 500, 40000, 1, 10000)
)


class _PortsConfiguration_Type(Integer32):
    """Custom type portsConfiguration based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200)
        )
    )
    namedValues = NamedValues(
        *(("separate", 100),
          ("bridge", 200))
    )


_PortsConfiguration_Type.__name__ = "Integer32"
_PortsConfiguration_Object = MibScalar
portsConfiguration = _PortsConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 500, 40000, 1, 10000, 100),
    _PortsConfiguration_Type()
)
portsConfiguration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portsConfiguration.setStatus("current")


class _KernelNetworkPriority_Type(Unsigned32):
    """Custom type kernelNetworkPriority based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_KernelNetworkPriority_Type.__name__ = "Unsigned32"
_KernelNetworkPriority_Object = MibScalar
kernelNetworkPriority = _KernelNetworkPriority_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 500, 40000, 1, 10000, 200),
    _KernelNetworkPriority_Type()
)
kernelNetworkPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    kernelNetworkPriority.setStatus("current")
_DebugGroup_ObjectIdentity = ObjectIdentity
debugGroup = _DebugGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 500, 40000, 1, 50000)
)
_NotificationsGroup_ObjectIdentity = ObjectIdentity
notificationsGroup = _NotificationsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 500, 40000, 1, 60010)
)


class _MinSeverity_Type(Integer32):
    """Custom type minSeverity based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              100,
              200,
              300,
              400,
              500)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("debug", 100),
          ("info", 200),
          ("warning", 300),
          ("error", 400),
          ("critical", 500))
    )


_MinSeverity_Type.__name__ = "Integer32"
_MinSeverity_Object = MibScalar
minSeverity = _MinSeverity_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 500, 40000, 1, 60010, 100),
    _MinSeverity_Type()
)
minSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    minSeverity.setStatus("current")
_ConfigurationGroup_ObjectIdentity = ObjectIdentity
configurationGroup = _ConfigurationGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 500, 40000, 1, 60020)
)


class _NeedRestartInfo_Type(Integer32):
    """Custom type needRestartInfo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              100)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 100))
    )


_NeedRestartInfo_Type.__name__ = "Integer32"
_NeedRestartInfo_Object = MibScalar
needRestartInfo = _NeedRestartInfo_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 500, 40000, 1, 60020, 100),
    _NeedRestartInfo_Type()
)
needRestartInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    needRestartInfo.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MX-HARDWARE-MIB",
    **{"hardwareMIB": hardwareMIB,
       "hardwareMIBObjects": hardwareMIBObjects,
       "resetButtonManagement": resetButtonManagement,
       "interopForceDspResync": interopForceDspResync,
       "fxs": fxs,
       "ringManagement": ringManagement,
       "pri": pri,
       "portsStatusTable": portsStatusTable,
       "portsStatusEntry": portsStatusEntry,
       "portsStatusPort": portsStatusPort,
       "portsStatusLineType": portsStatusLineType,
       "portsStatusSignaling": portsStatusSignaling,
       "portsTable": portsTable,
       "portsEntry": portsEntry,
       "portsPort": portsPort,
       "portsLineType": portsLineType,
       "portsSignaling": portsSignaling,
       "statisticsGroup": statisticsGroup,
       "statsInfoTable": statsInfoTable,
       "statsInfoEntry": statsInfoEntry,
       "statsInfoPort": statsInfoPort,
       "statsInfoFramesTransmitted": statsInfoFramesTransmitted,
       "statsInfoFramesReceived": statsInfoFramesReceived,
       "statsInfoOctetsTransmitted": statsInfoOctetsTransmitted,
       "statsInfoOctetsReceived": statsInfoOctetsReceived,
       "statsInfoFcsErrors": statsInfoFcsErrors,
       "statsInfoFramesDropped": statsInfoFramesDropped,
       "statsInfoOctetsDropped": statsInfoOctetsDropped,
       "statsInfoNegativeFrameSlipsTransmitted": statsInfoNegativeFrameSlipsTransmitted,
       "statsInfoNegativeFrameSlipsReceived": statsInfoNegativeFrameSlipsReceived,
       "statsInfoPositiveFrameSlipsTransmitted": statsInfoPositiveFrameSlipsTransmitted,
       "statsInfoPositiveFrameSlipsReceived": statsInfoPositiveFrameSlipsReceived,
       "statsInfoFramingErrors": statsInfoFramingErrors,
       "statsInfoCodeViolations": statsInfoCodeViolations,
       "statsInfoCRCErrors": statsInfoCRCErrors,
       "statsInfoEBitErrors": statsInfoEBitErrors,
       "statsInfoBlockErrors": statsInfoBlockErrors,
       "statsInfoResetStats": statsInfoResetStats,
       "bri": bri,
       "briPortsStatusTable": briPortsStatusTable,
       "briPortsStatusEntry": briPortsStatusEntry,
       "briPortsStatusPort": briPortsStatusPort,
       "briPortsStatusPowerFeeding": briPortsStatusPowerFeeding,
       "briPortsTable": briPortsTable,
       "briPortsEntry": briPortsEntry,
       "briPortsPort": briPortsPort,
       "briPortsPowerFeedingEnable": briPortsPowerFeedingEnable,
       "clockReference": clockReference,
       "clockReferenceList": clockReferenceList,
       "clockReferenceSource": clockReferenceSource,
       "clockReferenceStatus": clockReferenceStatus,
       "eth": eth,
       "portsConfiguration": portsConfiguration,
       "kernelNetworkPriority": kernelNetworkPriority,
       "debugGroup": debugGroup,
       "notificationsGroup": notificationsGroup,
       "minSeverity": minSeverity,
       "configurationGroup": configurationGroup,
       "needRestartInfo": needRestartInfo}
)
