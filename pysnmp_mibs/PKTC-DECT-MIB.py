# SNMP MIB module (PKTC-DECT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/rfc/PKTC-DECT-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:19:09 2025
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

(pktcApplicationMibs,) = mibBuilder.importSymbols(
    "CLAB-DEF-MIB",
    "pktcApplicationMibs")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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

(DateAndTime,
 DisplayString,
 PhysAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

pktcDectMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 4)
)
if mibBuilder.loadTexts:
    pktcDectMib.setRevisions(
        ("2009-09-17 00:00",
         "2009-02-26 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class PktcSpecVersion(TextualConvention, Unsigned32):
    status = "current"


class PktcDectPPState(TextualConvention, Integer32):
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("idleUnlocked", 2),
          ("activeUnlocked", 3),
          ("idleLocked", 4),
          ("activeLocked", 5),
          ("noFPInRange", 6),
          ("waitingEasyPairing", 7),
          ("easyPairingFailed", 8),
          ("easyPINFailed", 9))
    )



# MIB Managed Objects in the order of their OIDs

_PktcDectNotifications_ObjectIdentity = ObjectIdentity
pktcDectNotifications = _PktcDectNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 4, 0)
)
_PktcDectObjects_ObjectIdentity = ObjectIdentity
pktcDectObjects = _PktcDectObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 4, 1)
)
_PktcDectFP_ObjectIdentity = ObjectIdentity
pktcDectFP = _PktcDectFP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 4, 1, 1)
)
_PktcDectFPMaxNumPP_Type = Unsigned32
_PktcDectFPMaxNumPP_Object = MibScalar
pktcDectFPMaxNumPP = _PktcDectFPMaxNumPP_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 4, 1, 1, 1),
    _PktcDectFPMaxNumPP_Type()
)
pktcDectFPMaxNumPP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcDectFPMaxNumPP.setStatus("current")
if mibBuilder.loadTexts:
    pktcDectFPMaxNumPP.setUnits("PPs")
_PktcDectFPMaxActivePP_Type = Unsigned32
_PktcDectFPMaxActivePP_Object = MibScalar
pktcDectFPMaxActivePP = _PktcDectFPMaxActivePP_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 4, 1, 1, 2),
    _PktcDectFPMaxActivePP_Type()
)
pktcDectFPMaxActivePP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcDectFPMaxActivePP.setStatus("current")
if mibBuilder.loadTexts:
    pktcDectFPMaxActivePP.setUnits("PPs")


class _PktcDectFPLockListCfg_Type(Bits):
    """Custom type pktcDectFPLockListCfg based on Bits"""
    namedValues = NamedValues(
        *(("listOfSupportedLists", 0),
          ("missedCallsList", 1),
          ("outgoingCallsLlist", 2),
          ("incomingAcceptedCallsList", 3),
          ("allCallsList", 4),
          ("contactList", 5),
          ("internalNamesList", 6),
          ("dectSsystemSettingsList", 7),
          ("lineSettingsList", 8),
          ("unused9", 9),
          ("unused10", 10),
          ("unused11", 11),
          ("unused12", 12),
          ("unused13", 13),
          ("unused14", 14),
          ("unused15", 15),
          ("unused16", 16),
          ("unused17", 17),
          ("unused18", 18),
          ("unused19", 19),
          ("unused20", 20),
          ("unused21", 21),
          ("unused22", 22),
          ("unused23", 23),
          ("unused24", 24),
          ("unused25", 25),
          ("unused26", 26),
          ("unused27", 27),
          ("unused28", 28),
          ("unused29", 29),
          ("unused30", 30),
          ("unused31", 31))
    )

_PktcDectFPLockListCfg_Type.__name__ = "Bits"
_PktcDectFPLockListCfg_Object = MibScalar
pktcDectFPLockListCfg = _PktcDectFPLockListCfg_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 4, 1, 1, 3),
    _PktcDectFPLockListCfg_Type()
)
pktcDectFPLockListCfg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcDectFPLockListCfg.setStatus("current")


class _PktcDectFPZeroEmissionEnabled_Type(TruthValue):
    """Custom type pktcDectFPZeroEmissionEnabled based on TruthValue"""
    defaultValue = 1


_PktcDectFPZeroEmissionEnabled_Type.__name__ = "TruthValue"
_PktcDectFPZeroEmissionEnabled_Object = MibScalar
pktcDectFPZeroEmissionEnabled = _PktcDectFPZeroEmissionEnabled_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 4, 1, 1, 4),
    _PktcDectFPZeroEmissionEnabled_Type()
)
pktcDectFPZeroEmissionEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcDectFPZeroEmissionEnabled.setStatus("current")


class _PktcDectFPPairingType_Type(SnmpAdminString):
    """Custom type pktcDectFPPairingType based on SnmpAdminString"""
    defaultValue = OctetString("0000")


_PktcDectFPPairingType_Type.__name__ = "SnmpAdminString"
_PktcDectFPPairingType_Object = MibScalar
pktcDectFPPairingType = _PktcDectFPPairingType_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 4, 1, 1, 5),
    _PktcDectFPPairingType_Type()
)
pktcDectFPPairingType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcDectFPPairingType.setStatus("current")


class _PktcDectFPEasyPairingActivate_Type(TruthValue):
    """Custom type pktcDectFPEasyPairingActivate based on TruthValue"""
    defaultValue = 1


_PktcDectFPEasyPairingActivate_Type.__name__ = "TruthValue"
_PktcDectFPEasyPairingActivate_Object = MibScalar
pktcDectFPEasyPairingActivate = _PktcDectFPEasyPairingActivate_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 4, 1, 1, 6),
    _PktcDectFPEasyPairingActivate_Type()
)
pktcDectFPEasyPairingActivate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcDectFPEasyPairingActivate.setStatus("current")
_PktcDectFPName_Type = SnmpAdminString
_PktcDectFPName_Object = MibScalar
pktcDectFPName = _PktcDectFPName_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 4, 1, 1, 7),
    _PktcDectFPName_Type()
)
pktcDectFPName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcDectFPName.setStatus("current")


class _PktcDectFPGeneralCapabilities_Type(Bits):
    """Custom type pktcDectFPGeneralCapabilities based on Bits"""
    namedValues = NamedValues(
        ("none", 0)
    )

_PktcDectFPGeneralCapabilities_Type.__name__ = "Bits"
_PktcDectFPGeneralCapabilities_Object = MibScalar
pktcDectFPGeneralCapabilities = _PktcDectFPGeneralCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 4, 1, 1, 8),
    _PktcDectFPGeneralCapabilities_Type()
)
pktcDectFPGeneralCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcDectFPGeneralCapabilities.setStatus("current")


class _PktcDectFPExtendedCapabilities_Type(Bits):
    """Custom type pktcDectFPExtendedCapabilities based on Bits"""
    namedValues = NamedValues(
        *(("unused0", 0),
          ("unused1", 1),
          ("unused2", 2),
          ("unused3", 3),
          ("unused4", 4),
          ("unused5", 5),
          ("unused6", 6),
          ("unused7", 7),
          ("unused8", 8),
          ("unused9", 9),
          ("unused10", 10),
          ("unused11", 11),
          ("unused12", 12),
          ("unused13", 13),
          ("listAccess", 14),
          ("unused15", 15),
          ("unused16", 16),
          ("unused17", 17),
          ("unused18", 18),
          ("parallelCall", 19),
          ("unused20", 20),
          ("unused21", 21),
          ("unused22", 22),
          ("zeroEmission", 23),
          ("unused24", 24),
          ("unused25", 25),
          ("multipleLines", 26),
          ("multipleCalls", 27),
          ("unused28", 28),
          ("unused29", 29),
          ("unused30", 30),
          ("unused31", 31))
    )

_PktcDectFPExtendedCapabilities_Type.__name__ = "Bits"
_PktcDectFPExtendedCapabilities_Object = MibScalar
pktcDectFPExtendedCapabilities = _PktcDectFPExtendedCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 4, 1, 1, 9),
    _PktcDectFPExtendedCapabilities_Type()
)
pktcDectFPExtendedCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcDectFPExtendedCapabilities.setStatus("current")
_PktcDectHDVoiceProfile_ObjectIdentity = ObjectIdentity
pktcDectHDVoiceProfile = _PktcDectHDVoiceProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 4, 1, 2)
)
_PktcDectHDVoiceProfileBasicService_Type = PktcSpecVersion
_PktcDectHDVoiceProfileBasicService_Object = MibScalar
pktcDectHDVoiceProfileBasicService = _PktcDectHDVoiceProfileBasicService_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 4, 1, 2, 1),
    _PktcDectHDVoiceProfileBasicService_Type()
)
pktcDectHDVoiceProfileBasicService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcDectHDVoiceProfileBasicService.setStatus("current")
_PktcDectHDVoiceProfileNCS_Type = PktcSpecVersion
_PktcDectHDVoiceProfileNCS_Object = MibScalar
pktcDectHDVoiceProfileNCS = _PktcDectHDVoiceProfileNCS_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 4, 1, 2, 2),
    _PktcDectHDVoiceProfileNCS_Type()
)
pktcDectHDVoiceProfileNCS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcDectHDVoiceProfileNCS.setStatus("current")
_PktcDectHDVoiceProfileSIP_Type = PktcSpecVersion
_PktcDectHDVoiceProfileSIP_Object = MibScalar
pktcDectHDVoiceProfileSIP = _PktcDectHDVoiceProfileSIP_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 4, 1, 2, 3),
    _PktcDectHDVoiceProfileSIP_Type()
)
pktcDectHDVoiceProfileSIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcDectHDVoiceProfileSIP.setStatus("current")
_PktcDectCodec_ObjectIdentity = ObjectIdentity
pktcDectCodec = _PktcDectCodec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 4, 1, 3)
)


class _PktcDectCodecPrefList_Type(SnmpAdminString):
    """Custom type pktcDectCodecPrefList based on SnmpAdminString"""
    defaultValue = OctetString("G722,PCMU,PCMA")


_PktcDectCodecPrefList_Type.__name__ = "SnmpAdminString"
_PktcDectCodecPrefList_Object = MibScalar
pktcDectCodecPrefList = _PktcDectCodecPrefList_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 4, 1, 3, 1),
    _PktcDectCodecPrefList_Type()
)
pktcDectCodecPrefList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcDectCodecPrefList.setStatus("current")
_PktcDectDTMF_ObjectIdentity = ObjectIdentity
pktcDectDTMF = _PktcDectDTMF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 4, 1, 4)
)


class _PktcDectDTMFToneDuration_Type(Unsigned32):
    """Custom type pktcDectDTMFToneDuration based on Unsigned32"""
    defaultValue = 100


_PktcDectDTMFToneDuration_Type.__name__ = "Unsigned32"
_PktcDectDTMFToneDuration_Object = MibScalar
pktcDectDTMFToneDuration = _PktcDectDTMFToneDuration_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 4, 1, 4, 1),
    _PktcDectDTMFToneDuration_Type()
)
pktcDectDTMFToneDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcDectDTMFToneDuration.setStatus("current")
if mibBuilder.loadTexts:
    pktcDectDTMFToneDuration.setUnits("milliseconds")
_PktcDectBargeIn_ObjectIdentity = ObjectIdentity
pktcDectBargeIn = _PktcDectBargeIn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 4, 1, 5)
)


class _PktcDectBargeInEnabled_Type(TruthValue):
    """Custom type pktcDectBargeInEnabled based on TruthValue"""
    defaultValue = 1


_PktcDectBargeInEnabled_Type.__name__ = "TruthValue"
_PktcDectBargeInEnabled_Object = MibScalar
pktcDectBargeInEnabled = _PktcDectBargeInEnabled_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 4, 1, 5, 1),
    _PktcDectBargeInEnabled_Type()
)
pktcDectBargeInEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcDectBargeInEnabled.setStatus("current")
_PktcDectServiceStatus_ObjectIdentity = ObjectIdentity
pktcDectServiceStatus = _PktcDectServiceStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 4, 1, 6)
)


class _PktcDectServiceStatusDeactivationDisplay_Type(SnmpAdminString):
    """Custom type pktcDectServiceStatusDeactivationDisplay based on SnmpAdminString"""
    defaultValue = OctetString("Service Deactivated")


_PktcDectServiceStatusDeactivationDisplay_Type.__name__ = "SnmpAdminString"
_PktcDectServiceStatusDeactivationDisplay_Object = MibScalar
pktcDectServiceStatusDeactivationDisplay = _PktcDectServiceStatusDeactivationDisplay_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 4, 1, 6, 1),
    _PktcDectServiceStatusDeactivationDisplay_Type()
)
pktcDectServiceStatusDeactivationDisplay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcDectServiceStatusDeactivationDisplay.setStatus("current")


class _PktcDectServiceStatusConnectivityDisplay_Type(SnmpAdminString):
    """Custom type pktcDectServiceStatusConnectivityDisplay based on SnmpAdminString"""
    defaultValue = OctetString("Network Unavailable")


_PktcDectServiceStatusConnectivityDisplay_Type.__name__ = "SnmpAdminString"
_PktcDectServiceStatusConnectivityDisplay_Object = MibScalar
pktcDectServiceStatusConnectivityDisplay = _PktcDectServiceStatusConnectivityDisplay_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 4, 1, 6, 2),
    _PktcDectServiceStatusConnectivityDisplay_Type()
)
pktcDectServiceStatusConnectivityDisplay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcDectServiceStatusConnectivityDisplay.setStatus("current")
_PktcDectAnalogAlarmCfgTable_Object = MibTable
pktcDectAnalogAlarmCfgTable = _PktcDectAnalogAlarmCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 4, 1, 7)
)
if mibBuilder.loadTexts:
    pktcDectAnalogAlarmCfgTable.setStatus("current")
_PktcDectAnalogAlarmCfgEntry_Object = MibTableRow
pktcDectAnalogAlarmCfgEntry = _PktcDectAnalogAlarmCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 4, 1, 7, 1)
)
pktcDectAnalogAlarmCfgEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    pktcDectAnalogAlarmCfgEntry.setStatus("current")


class _PktcDectAnalogAlarmCfgState_Type(Integer32):
    """Custom type pktcDectAnalogAlarmCfgState based on Integer32"""
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
          ("preemptive", 2),
          ("simultanousCalls", 3))
    )


_PktcDectAnalogAlarmCfgState_Type.__name__ = "Integer32"
_PktcDectAnalogAlarmCfgState_Object = MibTableColumn
pktcDectAnalogAlarmCfgState = _PktcDectAnalogAlarmCfgState_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 4, 1, 7, 1, 1),
    _PktcDectAnalogAlarmCfgState_Type()
)
pktcDectAnalogAlarmCfgState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcDectAnalogAlarmCfgState.setStatus("current")
_PktcDectPPTable_Object = MibTable
pktcDectPPTable = _PktcDectPPTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 4, 1, 8)
)
if mibBuilder.loadTexts:
    pktcDectPPTable.setStatus("current")
_PktcDectPPEntry_Object = MibTableRow
pktcDectPPEntry = _PktcDectPPEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 4, 1, 8, 1)
)
pktcDectPPEntry.setIndexNames(
    (0, "PKTC-DECT-MIB", "pktcDectPPId"),
)
if mibBuilder.loadTexts:
    pktcDectPPEntry.setStatus("current")


class _PktcDectPPId_Type(Unsigned32):
    """Custom type pktcDectPPId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_PktcDectPPId_Type.__name__ = "Unsigned32"
_PktcDectPPId_Object = MibTableColumn
pktcDectPPId = _PktcDectPPId_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 4, 1, 8, 1, 1),
    _PktcDectPPId_Type()
)
pktcDectPPId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pktcDectPPId.setStatus("current")


class _PktcDectPPIPEI_Type(OctetString):
    """Custom type pktcDectPPIPEI based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_PktcDectPPIPEI_Type.__name__ = "OctetString"
_PktcDectPPIPEI_Object = MibTableColumn
pktcDectPPIPEI = _PktcDectPPIPEI_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 4, 1, 8, 1, 2),
    _PktcDectPPIPEI_Type()
)
pktcDectPPIPEI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcDectPPIPEI.setStatus("current")


class _PktcDectPPTerminalID_Type(Unsigned32):
    """Custom type pktcDectPPTerminalID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_PktcDectPPTerminalID_Type.__name__ = "Unsigned32"
_PktcDectPPTerminalID_Object = MibTableColumn
pktcDectPPTerminalID = _PktcDectPPTerminalID_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 4, 1, 8, 1, 3),
    _PktcDectPPTerminalID_Type()
)
pktcDectPPTerminalID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcDectPPTerminalID.setStatus("current")
_PktcDectPPStatus_Type = PktcDectPPState
_PktcDectPPStatus_Object = MibTableColumn
pktcDectPPStatus = _PktcDectPPStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 4, 1, 8, 1, 4),
    _PktcDectPPStatus_Type()
)
pktcDectPPStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcDectPPStatus.setStatus("current")


class _PktcDectPPRegCtrl_Type(Integer32):
    """Custom type pktcDectPPRegCtrl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("register", 1),
          ("deregister", 2),
          ("remove", 3))
    )


_PktcDectPPRegCtrl_Type.__name__ = "Integer32"
_PktcDectPPRegCtrl_Object = MibTableColumn
pktcDectPPRegCtrl = _PktcDectPPRegCtrl_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 4, 1, 8, 1, 5),
    _PktcDectPPRegCtrl_Type()
)
pktcDectPPRegCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcDectPPRegCtrl.setStatus("current")
_PktcDectPPCapabilitiesTable_Object = MibTable
pktcDectPPCapabilitiesTable = _PktcDectPPCapabilitiesTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 4, 1, 9)
)
if mibBuilder.loadTexts:
    pktcDectPPCapabilitiesTable.setStatus("current")
_PktcDectPPCapabilitiesEntry_Object = MibTableRow
pktcDectPPCapabilitiesEntry = _PktcDectPPCapabilitiesEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 4, 1, 9, 1)
)
pktcDectPPCapabilitiesEntry.setIndexNames(
    (0, "PKTC-DECT-MIB", "pktcDectPPId"),
)
if mibBuilder.loadTexts:
    pktcDectPPCapabilitiesEntry.setStatus("current")


class _PktcDectPPCapabilitiesDisplay_Type(Integer32):
    """Custom type pktcDectPPCapabilitiesDisplay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("na", 0),
          ("noDisplay", 1),
          ("numeric", 2),
          ("numericPlus", 3),
          ("alphanumeric", 4),
          ("fullDisplay", 5))
    )


_PktcDectPPCapabilitiesDisplay_Type.__name__ = "Integer32"
_PktcDectPPCapabilitiesDisplay_Object = MibTableColumn
pktcDectPPCapabilitiesDisplay = _PktcDectPPCapabilitiesDisplay_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 4, 1, 9, 1, 1),
    _PktcDectPPCapabilitiesDisplay_Type()
)
pktcDectPPCapabilitiesDisplay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcDectPPCapabilitiesDisplay.setStatus("current")


class _PktcDectPPCapabilitiesTone_Type(Integer32):
    """Custom type pktcDectPPCapabilitiesTone based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("na", 0),
          ("notone", 1),
          ("dialTone", 2),
          ("e182", 3),
          ("dect", 4))
    )


_PktcDectPPCapabilitiesTone_Type.__name__ = "Integer32"
_PktcDectPPCapabilitiesTone_Object = MibTableColumn
pktcDectPPCapabilitiesTone = _PktcDectPPCapabilitiesTone_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 4, 1, 9, 1, 2),
    _PktcDectPPCapabilitiesTone_Type()
)
pktcDectPPCapabilitiesTone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcDectPPCapabilitiesTone.setStatus("current")


class _PktcDectPPCapabilitiesEcho_Type(Integer32):
    """Custom type pktcDectPPCapabilitiesEcho based on Integer32"""
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
        *(("na", 0),
          ("minTCL", 1),
          ("fullTCL", 2),
          ("voip", 3))
    )


_PktcDectPPCapabilitiesEcho_Type.__name__ = "Integer32"
_PktcDectPPCapabilitiesEcho_Object = MibTableColumn
pktcDectPPCapabilitiesEcho = _PktcDectPPCapabilitiesEcho_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 4, 1, 9, 1, 3),
    _PktcDectPPCapabilitiesEcho_Type()
)
pktcDectPPCapabilitiesEcho.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcDectPPCapabilitiesEcho.setStatus("current")


class _PktcDectPPCapabilitiesAmbientNoiseRejection_Type(Integer32):
    """Custom type pktcDectPPCapabilitiesAmbientNoiseRejection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("na", 0),
          ("noSupport", 1),
          ("support", 2))
    )


_PktcDectPPCapabilitiesAmbientNoiseRejection_Type.__name__ = "Integer32"
_PktcDectPPCapabilitiesAmbientNoiseRejection_Object = MibTableColumn
pktcDectPPCapabilitiesAmbientNoiseRejection = _PktcDectPPCapabilitiesAmbientNoiseRejection_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 4, 1, 9, 1, 4),
    _PktcDectPPCapabilitiesAmbientNoiseRejection_Type()
)
pktcDectPPCapabilitiesAmbientNoiseRejection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcDectPPCapabilitiesAmbientNoiseRejection.setStatus("current")


class _PktcDectPPCapabilitiesAdaptiveVolumeCtrl_Type(Integer32):
    """Custom type pktcDectPPCapabilitiesAdaptiveVolumeCtrl based on Integer32"""
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
        *(("na", 0),
          ("noSupported", 1),
          ("used", 2),
          ("disabled", 3))
    )


_PktcDectPPCapabilitiesAdaptiveVolumeCtrl_Type.__name__ = "Integer32"
_PktcDectPPCapabilitiesAdaptiveVolumeCtrl_Object = MibTableColumn
pktcDectPPCapabilitiesAdaptiveVolumeCtrl = _PktcDectPPCapabilitiesAdaptiveVolumeCtrl_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 4, 1, 9, 1, 5),
    _PktcDectPPCapabilitiesAdaptiveVolumeCtrl_Type()
)
pktcDectPPCapabilitiesAdaptiveVolumeCtrl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcDectPPCapabilitiesAdaptiveVolumeCtrl.setStatus("current")


class _PktcDectPPCapabilitiesSlotType_Type(Bits):
    """Custom type pktcDectPPCapabilitiesSlotType based on Bits"""
    namedValues = NamedValues(
        *(("unused0", 0),
          ("unused1", 1),
          ("unused2", 2),
          ("doubleSlot", 3),
          ("fullSlot", 4),
          ("unused5", 5),
          ("unused6", 6),
          ("halfSlot", 7))
    )

_PktcDectPPCapabilitiesSlotType_Type.__name__ = "Bits"
_PktcDectPPCapabilitiesSlotType_Object = MibTableColumn
pktcDectPPCapabilitiesSlotType = _PktcDectPPCapabilitiesSlotType_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 4, 1, 9, 1, 6),
    _PktcDectPPCapabilitiesSlotType_Type()
)
pktcDectPPCapabilitiesSlotType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcDectPPCapabilitiesSlotType.setStatus("current")


class _PktcDectPPCapabilitiesStoredDisplayChars_Type(Unsigned32):
    """Custom type pktcDectPPCapabilitiesStoredDisplayChars based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16363),
    )


_PktcDectPPCapabilitiesStoredDisplayChars_Type.__name__ = "Unsigned32"
_PktcDectPPCapabilitiesStoredDisplayChars_Object = MibTableColumn
pktcDectPPCapabilitiesStoredDisplayChars = _PktcDectPPCapabilitiesStoredDisplayChars_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 4, 1, 9, 1, 7),
    _PktcDectPPCapabilitiesStoredDisplayChars_Type()
)
pktcDectPPCapabilitiesStoredDisplayChars.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcDectPPCapabilitiesStoredDisplayChars.setStatus("current")


class _PktcDectPPCapabilitiesDisplayLines_Type(Unsigned32):
    """Custom type pktcDectPPCapabilitiesDisplayLines based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_PktcDectPPCapabilitiesDisplayLines_Type.__name__ = "Unsigned32"
_PktcDectPPCapabilitiesDisplayLines_Object = MibTableColumn
pktcDectPPCapabilitiesDisplayLines = _PktcDectPPCapabilitiesDisplayLines_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 4, 1, 9, 1, 8),
    _PktcDectPPCapabilitiesDisplayLines_Type()
)
pktcDectPPCapabilitiesDisplayLines.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcDectPPCapabilitiesDisplayLines.setStatus("current")


class _PktcDectPPCapabilitiesCharsPerDisplayLine_Type(Unsigned32):
    """Custom type pktcDectPPCapabilitiesCharsPerDisplayLine based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_PktcDectPPCapabilitiesCharsPerDisplayLine_Type.__name__ = "Unsigned32"
_PktcDectPPCapabilitiesCharsPerDisplayLine_Object = MibTableColumn
pktcDectPPCapabilitiesCharsPerDisplayLine = _PktcDectPPCapabilitiesCharsPerDisplayLine_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 4, 1, 9, 1, 9),
    _PktcDectPPCapabilitiesCharsPerDisplayLine_Type()
)
pktcDectPPCapabilitiesCharsPerDisplayLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcDectPPCapabilitiesCharsPerDisplayLine.setStatus("current")


class _PktcDectPPCapabilitiesScrollBehavior_Type(Integer32):
    """Custom type pktcDectPPCapabilitiesScrollBehavior based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("na", 0),
          ("type1", 1),
          ("type", 2))
    )


_PktcDectPPCapabilitiesScrollBehavior_Type.__name__ = "Integer32"
_PktcDectPPCapabilitiesScrollBehavior_Object = MibTableColumn
pktcDectPPCapabilitiesScrollBehavior = _PktcDectPPCapabilitiesScrollBehavior_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 4, 1, 9, 1, 10),
    _PktcDectPPCapabilitiesScrollBehavior_Type()
)
pktcDectPPCapabilitiesScrollBehavior.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcDectPPCapabilitiesScrollBehavior.setStatus("current")


class _PktcDectPPCapabilitiesProfile_Type(Bits):
    """Custom type pktcDectPPCapabilitiesProfile based on Bits"""
    namedValues = NamedValues(
        *(("unused0", 0),
          ("unused1", 1),
          ("unused2", 2),
          ("unused3", 3),
          ("unused4", 4),
          ("gapSupport", 5),
          ("unused6", 6),
          ("unused7", 7),
          ("unused8", 8),
          ("unused9", 9),
          ("unused10", 10),
          ("unused11", 11),
          ("unused12", 12),
          ("unused13", 13),
          ("unused14", 14),
          ("unused15", 15),
          ("unused16", 16),
          ("unused17", 17),
          ("unused18", 18),
          ("unused19", 19),
          ("unused20", 20),
          ("unused21", 21),
          ("unused22", 22),
          ("unused23", 23),
          ("unused24", 24),
          ("unused25", 25),
          ("unused26", 26),
          ("unused27", 27),
          ("unused28", 28),
          ("unused29", 29),
          ("unused30", 30),
          ("unused31", 31),
          ("unused32", 32),
          ("unused33", 33),
          ("unused34", 34),
          ("unused35", 35),
          ("unused36", 36),
          ("unused37", 37),
          ("unused38", 38),
          ("unused39", 39),
          ("unused40", 40),
          ("zeroEmissionSupport", 41),
          ("unused42", 42),
          ("unused43", 43),
          ("unused44", 44),
          ("unused45", 45),
          ("unused46", 46),
          ("unused47", 47),
          ("unused48", 48),
          ("unused49", 49),
          ("multipleLlines", 50),
          ("parallelCall", 51),
          ("callIdentification", 52),
          ("wideband", 53),
          ("part3", 54),
          ("unused55", 55),
          ("unused56", 56),
          ("unused57", 57),
          ("unused58", 58),
          ("unused59", 59),
          ("unused60", 60),
          ("unused61", 61),
          ("unused62", 62),
          ("unused63", 63),
          ("unused64", 64))
    )

_PktcDectPPCapabilitiesProfile_Type.__name__ = "Bits"
_PktcDectPPCapabilitiesProfile_Object = MibTableColumn
pktcDectPPCapabilitiesProfile = _PktcDectPPCapabilitiesProfile_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 4, 1, 9, 1, 11),
    _PktcDectPPCapabilitiesProfile_Type()
)
pktcDectPPCapabilitiesProfile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcDectPPCapabilitiesProfile.setStatus("current")
_PktcDectListAccessTable_Object = MibTable
pktcDectListAccessTable = _PktcDectListAccessTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 4, 1, 10)
)
if mibBuilder.loadTexts:
    pktcDectListAccessTable.setStatus("current")
_PktcDectListAccessEntry_Object = MibTableRow
pktcDectListAccessEntry = _PktcDectListAccessEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 4, 1, 10, 1)
)
pktcDectListAccessEntry.setIndexNames(
    (0, "PKTC-DECT-MIB", "pktcDectListAccessIndex"),
)
if mibBuilder.loadTexts:
    pktcDectListAccessEntry.setStatus("current")


class _PktcDectListAccessIndex_Type(Unsigned32):
    """Custom type pktcDectListAccessIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_PktcDectListAccessIndex_Type.__name__ = "Unsigned32"
_PktcDectListAccessIndex_Object = MibTableColumn
pktcDectListAccessIndex = _PktcDectListAccessIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 4, 1, 10, 1, 1),
    _PktcDectListAccessIndex_Type()
)
pktcDectListAccessIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pktcDectListAccessIndex.setStatus("current")


class _PktcDectListAccesslistID_Type(Unsigned32):
    """Custom type pktcDectListAccesslistID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_PktcDectListAccesslistID_Type.__name__ = "Unsigned32"
_PktcDectListAccesslistID_Object = MibTableColumn
pktcDectListAccesslistID = _PktcDectListAccesslistID_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 4, 1, 10, 1, 2),
    _PktcDectListAccesslistID_Type()
)
pktcDectListAccesslistID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcDectListAccesslistID.setStatus("current")
_PktcDectListAccessDescr_Type = SnmpAdminString
_PktcDectListAccessDescr_Object = MibTableColumn
pktcDectListAccessDescr = _PktcDectListAccessDescr_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 4, 1, 10, 1, 3),
    _PktcDectListAccessDescr_Type()
)
pktcDectListAccessDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcDectListAccessDescr.setStatus("current")
_PktcDectInternalNamesListTable_Object = MibTable
pktcDectInternalNamesListTable = _PktcDectInternalNamesListTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 4, 1, 11)
)
if mibBuilder.loadTexts:
    pktcDectInternalNamesListTable.setStatus("current")
_PktcDectInternalNamesListEntry_Object = MibTableRow
pktcDectInternalNamesListEntry = _PktcDectInternalNamesListEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 4, 1, 11, 1)
)
pktcDectInternalNamesListEntry.setIndexNames(
    (0, "PKTC-DECT-MIB", "pktcDectInternalNamesListIndex"),
)
if mibBuilder.loadTexts:
    pktcDectInternalNamesListEntry.setStatus("current")


class _PktcDectInternalNamesListIndex_Type(Unsigned32):
    """Custom type pktcDectInternalNamesListIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32767),
    )


_PktcDectInternalNamesListIndex_Type.__name__ = "Unsigned32"
_PktcDectInternalNamesListIndex_Object = MibTableColumn
pktcDectInternalNamesListIndex = _PktcDectInternalNamesListIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 4, 1, 11, 1, 1),
    _PktcDectInternalNamesListIndex_Type()
)
pktcDectInternalNamesListIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pktcDectInternalNamesListIndex.setStatus("current")


class _PktcDectInternalNamesListNumber_Type(Unsigned32):
    """Custom type pktcDectInternalNamesListNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32767),
    )


_PktcDectInternalNamesListNumber_Type.__name__ = "Unsigned32"
_PktcDectInternalNamesListNumber_Object = MibTableColumn
pktcDectInternalNamesListNumber = _PktcDectInternalNamesListNumber_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 4, 1, 11, 1, 2),
    _PktcDectInternalNamesListNumber_Type()
)
pktcDectInternalNamesListNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcDectInternalNamesListNumber.setStatus("current")
_PktcDectInternalNamesListName_Type = SnmpAdminString
_PktcDectInternalNamesListName_Object = MibTableColumn
pktcDectInternalNamesListName = _PktcDectInternalNamesListName_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 4, 1, 11, 1, 3),
    _PktcDectInternalNamesListName_Type()
)
pktcDectInternalNamesListName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcDectInternalNamesListName.setStatus("current")
_PktcDectLineSettingsListTable_Object = MibTable
pktcDectLineSettingsListTable = _PktcDectLineSettingsListTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 4, 1, 12)
)
if mibBuilder.loadTexts:
    pktcDectLineSettingsListTable.setStatus("current")
_PktcDectLineSettingsListEntry_Object = MibTableRow
pktcDectLineSettingsListEntry = _PktcDectLineSettingsListEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 4, 1, 12, 1)
)
pktcDectLineSettingsListEntry.setIndexNames(
    (0, "PKTC-DECT-MIB", "pktcDectLineSettingsListIndex"),
)
if mibBuilder.loadTexts:
    pktcDectLineSettingsListEntry.setStatus("current")


class _PktcDectLineSettingsListIndex_Type(Unsigned32):
    """Custom type pktcDectLineSettingsListIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_PktcDectLineSettingsListIndex_Type.__name__ = "Unsigned32"
_PktcDectLineSettingsListIndex_Object = MibTableColumn
pktcDectLineSettingsListIndex = _PktcDectLineSettingsListIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 4, 1, 12, 1, 1),
    _PktcDectLineSettingsListIndex_Type()
)
pktcDectLineSettingsListIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pktcDectLineSettingsListIndex.setStatus("current")


class _PktcDectLineSettingsListLineId_Type(Unsigned32):
    """Custom type pktcDectLineSettingsListLineId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_PktcDectLineSettingsListLineId_Type.__name__ = "Unsigned32"
_PktcDectLineSettingsListLineId_Object = MibTableColumn
pktcDectLineSettingsListLineId = _PktcDectLineSettingsListLineId_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 4, 1, 12, 1, 2),
    _PktcDectLineSettingsListLineId_Type()
)
pktcDectLineSettingsListLineId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcDectLineSettingsListLineId.setStatus("current")
_PktcDectLineSettingsListLineName_Type = SnmpAdminString
_PktcDectLineSettingsListLineName_Object = MibTableColumn
pktcDectLineSettingsListLineName = _PktcDectLineSettingsListLineName_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 4, 1, 12, 1, 3),
    _PktcDectLineSettingsListLineName_Type()
)
pktcDectLineSettingsListLineName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcDectLineSettingsListLineName.setStatus("current")
_PktcDectLineSettingsListAttachedHandsets_Type = SnmpAdminString
_PktcDectLineSettingsListAttachedHandsets_Object = MibTableColumn
pktcDectLineSettingsListAttachedHandsets = _PktcDectLineSettingsListAttachedHandsets_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 4, 1, 12, 1, 4),
    _PktcDectLineSettingsListAttachedHandsets_Type()
)
pktcDectLineSettingsListAttachedHandsets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcDectLineSettingsListAttachedHandsets.setStatus("current")
_PktcDectLineSettingsListDialingPrefix_Type = SnmpAdminString
_PktcDectLineSettingsListDialingPrefix_Object = MibTableColumn
pktcDectLineSettingsListDialingPrefix = _PktcDectLineSettingsListDialingPrefix_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 4, 1, 12, 1, 5),
    _PktcDectLineSettingsListDialingPrefix_Type()
)
pktcDectLineSettingsListDialingPrefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcDectLineSettingsListDialingPrefix.setStatus("current")


class _PktcDectLineSettingsListFPMelody_Type(Unsigned32):
    """Custom type pktcDectLineSettingsListFPMelody based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_PktcDectLineSettingsListFPMelody_Type.__name__ = "Unsigned32"
_PktcDectLineSettingsListFPMelody_Object = MibTableColumn
pktcDectLineSettingsListFPMelody = _PktcDectLineSettingsListFPMelody_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 4, 1, 12, 1, 6),
    _PktcDectLineSettingsListFPMelody_Type()
)
pktcDectLineSettingsListFPMelody.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcDectLineSettingsListFPMelody.setStatus("current")


class _PktcDectLineSettingsListFPVolume_Type(Unsigned32):
    """Custom type pktcDectLineSettingsListFPVolume based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_PktcDectLineSettingsListFPVolume_Type.__name__ = "Unsigned32"
_PktcDectLineSettingsListFPVolume_Object = MibTableColumn
pktcDectLineSettingsListFPVolume = _PktcDectLineSettingsListFPVolume_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 4, 1, 12, 1, 7),
    _PktcDectLineSettingsListFPVolume_Type()
)
pktcDectLineSettingsListFPVolume.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcDectLineSettingsListFPVolume.setStatus("current")
_PktcDectLineSettingsListBlockedNB_Type = TruthValue
_PktcDectLineSettingsListBlockedNB_Object = MibTableColumn
pktcDectLineSettingsListBlockedNB = _PktcDectLineSettingsListBlockedNB_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 4, 1, 12, 1, 8),
    _PktcDectLineSettingsListBlockedNB_Type()
)
pktcDectLineSettingsListBlockedNB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcDectLineSettingsListBlockedNB.setStatus("current")
_PktcDectLineSettingsListMultipleCalls_Type = TruthValue
_PktcDectLineSettingsListMultipleCalls_Object = MibTableColumn
pktcDectLineSettingsListMultipleCalls = _PktcDectLineSettingsListMultipleCalls_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 4, 1, 12, 1, 9),
    _PktcDectLineSettingsListMultipleCalls_Type()
)
pktcDectLineSettingsListMultipleCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcDectLineSettingsListMultipleCalls.setStatus("current")
_PktcDectLineSettingsListIntrusionCall_Type = TruthValue
_PktcDectLineSettingsListIntrusionCall_Object = MibTableColumn
pktcDectLineSettingsListIntrusionCall = _PktcDectLineSettingsListIntrusionCall_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 4, 1, 12, 1, 10),
    _PktcDectLineSettingsListIntrusionCall_Type()
)
pktcDectLineSettingsListIntrusionCall.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcDectLineSettingsListIntrusionCall.setStatus("current")
_PktcDectPerformanceTable_Object = MibTable
pktcDectPerformanceTable = _PktcDectPerformanceTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 4, 1, 13)
)
if mibBuilder.loadTexts:
    pktcDectPerformanceTable.setStatus("current")
_PktcDectPerformanceEntry_Object = MibTableRow
pktcDectPerformanceEntry = _PktcDectPerformanceEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 4, 1, 13, 1)
)
pktcDectPerformanceEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    pktcDectPerformanceEntry.setStatus("current")
_PktcDectPerformanceRecordNum_Type = Unsigned32
_PktcDectPerformanceRecordNum_Object = MibTableColumn
pktcDectPerformanceRecordNum = _PktcDectPerformanceRecordNum_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 4, 1, 13, 1, 1),
    _PktcDectPerformanceRecordNum_Type()
)
pktcDectPerformanceRecordNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcDectPerformanceRecordNum.setStatus("current")
_PktcDectPerformanceHandovers_Type = Counter32
_PktcDectPerformanceHandovers_Object = MibTableColumn
pktcDectPerformanceHandovers = _PktcDectPerformanceHandovers_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 4, 1, 13, 1, 2),
    _PktcDectPerformanceHandovers_Type()
)
pktcDectPerformanceHandovers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcDectPerformanceHandovers.setStatus("current")
_PktcDectPerformanceRTDelay_Type = Unsigned32
_PktcDectPerformanceRTDelay_Object = MibTableColumn
pktcDectPerformanceRTDelay = _PktcDectPerformanceRTDelay_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 4, 1, 13, 1, 3),
    _PktcDectPerformanceRTDelay_Type()
)
pktcDectPerformanceRTDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcDectPerformanceRTDelay.setStatus("current")
_PktcDectPerformanceSyncFailures_Type = Counter32
_PktcDectPerformanceSyncFailures_Object = MibTableColumn
pktcDectPerformanceSyncFailures = _PktcDectPerformanceSyncFailures_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 4, 1, 13, 1, 4),
    _PktcDectPerformanceSyncFailures_Type()
)
pktcDectPerformanceSyncFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcDectPerformanceSyncFailures.setStatus("current")
_PktcDectPerformanceControlFieldErrs_Type = Counter32
_PktcDectPerformanceControlFieldErrs_Object = MibTableColumn
pktcDectPerformanceControlFieldErrs = _PktcDectPerformanceControlFieldErrs_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 4, 1, 13, 1, 5),
    _PktcDectPerformanceControlFieldErrs_Type()
)
pktcDectPerformanceControlFieldErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcDectPerformanceControlFieldErrs.setStatus("current")
_PktcDectPerformancePayloadErrs_Type = Counter32
_PktcDectPerformancePayloadErrs_Object = MibTableColumn
pktcDectPerformancePayloadErrs = _PktcDectPerformancePayloadErrs_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 4, 1, 13, 1, 6),
    _PktcDectPerformancePayloadErrs_Type()
)
pktcDectPerformancePayloadErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcDectPerformancePayloadErrs.setStatus("current")
_PktcDectPerformanceSlidingCollisions_Type = Counter32
_PktcDectPerformanceSlidingCollisions_Object = MibTableColumn
pktcDectPerformanceSlidingCollisions = _PktcDectPerformanceSlidingCollisions_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 4, 1, 13, 1, 7),
    _PktcDectPerformanceSlidingCollisions_Type()
)
pktcDectPerformanceSlidingCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcDectPerformanceSlidingCollisions.setStatus("current")
_PktcDectPerformanceLinkErrsQbit_Type = Counter32
_PktcDectPerformanceLinkErrsQbit_Object = MibTableColumn
pktcDectPerformanceLinkErrsQbit = _PktcDectPerformanceLinkErrsQbit_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 4, 1, 13, 1, 8),
    _PktcDectPerformanceLinkErrsQbit_Type()
)
pktcDectPerformanceLinkErrsQbit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcDectPerformanceLinkErrsQbit.setStatus("current")
_PktcDectStatusTable_Object = MibTable
pktcDectStatusTable = _PktcDectStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 4, 1, 14)
)
if mibBuilder.loadTexts:
    pktcDectStatusTable.setStatus("current")
_PktcDectStatusEntry_Object = MibTableRow
pktcDectStatusEntry = _PktcDectStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 4, 1, 14, 1)
)
pktcDectStatusEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    pktcDectStatusEntry.setStatus("current")
_PktcDectStatusLastLocate_Type = DateAndTime
_PktcDectStatusLastLocate_Object = MibTableColumn
pktcDectStatusLastLocate = _PktcDectStatusLastLocate_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 4, 1, 14, 1, 1),
    _PktcDectStatusLastLocate_Type()
)
pktcDectStatusLastLocate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcDectStatusLastLocate.setStatus("current")
_PktcDectStatusNumLocateMsgs_Type = Counter32
_PktcDectStatusNumLocateMsgs_Object = MibTableColumn
pktcDectStatusNumLocateMsgs = _PktcDectStatusNumLocateMsgs_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 4, 1, 14, 1, 2),
    _PktcDectStatusNumLocateMsgs_Type()
)
pktcDectStatusNumLocateMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcDectStatusNumLocateMsgs.setStatus("current")
_PktcDectStatusNumConnectionFailures_Type = Counter32
_PktcDectStatusNumConnectionFailures_Object = MibTableColumn
pktcDectStatusNumConnectionFailures = _PktcDectStatusNumConnectionFailures_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 4, 1, 14, 1, 3),
    _PktcDectStatusNumConnectionFailures_Type()
)
pktcDectStatusNumConnectionFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcDectStatusNumConnectionFailures.setStatus("current")
_PktcDectStatusNumActivitySuccess_Type = Counter32
_PktcDectStatusNumActivitySuccess_Object = MibTableColumn
pktcDectStatusNumActivitySuccess = _PktcDectStatusNumActivitySuccess_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 4, 1, 14, 1, 4),
    _PktcDectStatusNumActivitySuccess_Type()
)
pktcDectStatusNumActivitySuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcDectStatusNumActivitySuccess.setStatus("current")
_PktcDectStatusLastActivityFailure_Type = DateAndTime
_PktcDectStatusLastActivityFailure_Object = MibTableColumn
pktcDectStatusLastActivityFailure = _PktcDectStatusLastActivityFailure_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 4, 1, 14, 1, 5),
    _PktcDectStatusLastActivityFailure_Type()
)
pktcDectStatusLastActivityFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcDectStatusLastActivityFailure.setStatus("current")
_PktcDectStatusRSSI_Type = Unsigned32
_PktcDectStatusRSSI_Object = MibTableColumn
pktcDectStatusRSSI = _PktcDectStatusRSSI_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 4, 1, 14, 1, 6),
    _PktcDectStatusRSSI_Type()
)
pktcDectStatusRSSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcDectStatusRSSI.setStatus("current")
_PktcDectMibConformance_ObjectIdentity = ObjectIdentity
pktcDectMibConformance = _PktcDectMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 4, 2)
)
_PktcDectMibCompliances_ObjectIdentity = ObjectIdentity
pktcDectMibCompliances = _PktcDectMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 4, 2, 1)
)
_PktcDectMibGroups_ObjectIdentity = ObjectIdentity
pktcDectMibGroups = _PktcDectMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 4, 2, 2)
)

# Managed Objects groups

pktcDectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 4, 2, 2, 1)
)
pktcDectGroup.setObjects(
      *(("PKTC-DECT-MIB", "pktcDectFPMaxNumPP"),
        ("PKTC-DECT-MIB", "pktcDectFPMaxActivePP"),
        ("PKTC-DECT-MIB", "pktcDectFPLockListCfg"),
        ("PKTC-DECT-MIB", "pktcDectFPZeroEmissionEnabled"),
        ("PKTC-DECT-MIB", "pktcDectFPPairingType"),
        ("PKTC-DECT-MIB", "pktcDectFPEasyPairingActivate"),
        ("PKTC-DECT-MIB", "pktcDectFPName"),
        ("PKTC-DECT-MIB", "pktcDectFPGeneralCapabilities"),
        ("PKTC-DECT-MIB", "pktcDectFPExtendedCapabilities"),
        ("PKTC-DECT-MIB", "pktcDectHDVoiceProfileBasicService"),
        ("PKTC-DECT-MIB", "pktcDectHDVoiceProfileNCS"),
        ("PKTC-DECT-MIB", "pktcDectHDVoiceProfileSIP"),
        ("PKTC-DECT-MIB", "pktcDectCodecPrefList"),
        ("PKTC-DECT-MIB", "pktcDectDTMFToneDuration"),
        ("PKTC-DECT-MIB", "pktcDectBargeInEnabled"),
        ("PKTC-DECT-MIB", "pktcDectServiceStatusDeactivationDisplay"),
        ("PKTC-DECT-MIB", "pktcDectServiceStatusConnectivityDisplay"),
        ("PKTC-DECT-MIB", "pktcDectAnalogAlarmCfgState"),
        ("PKTC-DECT-MIB", "pktcDectListAccesslistID"),
        ("PKTC-DECT-MIB", "pktcDectListAccessDescr"),
        ("PKTC-DECT-MIB", "pktcDectInternalNamesListNumber"),
        ("PKTC-DECT-MIB", "pktcDectInternalNamesListName"),
        ("PKTC-DECT-MIB", "pktcDectLineSettingsListLineId"),
        ("PKTC-DECT-MIB", "pktcDectLineSettingsListLineName"),
        ("PKTC-DECT-MIB", "pktcDectLineSettingsListAttachedHandsets"),
        ("PKTC-DECT-MIB", "pktcDectLineSettingsListDialingPrefix"),
        ("PKTC-DECT-MIB", "pktcDectLineSettingsListFPMelody"),
        ("PKTC-DECT-MIB", "pktcDectLineSettingsListFPVolume"),
        ("PKTC-DECT-MIB", "pktcDectLineSettingsListBlockedNB"),
        ("PKTC-DECT-MIB", "pktcDectLineSettingsListMultipleCalls"),
        ("PKTC-DECT-MIB", "pktcDectLineSettingsListIntrusionCall"),
        ("PKTC-DECT-MIB", "pktcDectPerformanceRecordNum"),
        ("PKTC-DECT-MIB", "pktcDectPerformanceHandovers"),
        ("PKTC-DECT-MIB", "pktcDectPerformanceRTDelay"),
        ("PKTC-DECT-MIB", "pktcDectPerformanceSyncFailures"),
        ("PKTC-DECT-MIB", "pktcDectPerformanceControlFieldErrs"),
        ("PKTC-DECT-MIB", "pktcDectPerformancePayloadErrs"),
        ("PKTC-DECT-MIB", "pktcDectPerformanceSlidingCollisions"),
        ("PKTC-DECT-MIB", "pktcDectPerformanceLinkErrsQbit"),
        ("PKTC-DECT-MIB", "pktcDectStatusLastLocate"),
        ("PKTC-DECT-MIB", "pktcDectStatusNumLocateMsgs"),
        ("PKTC-DECT-MIB", "pktcDectStatusNumConnectionFailures"),
        ("PKTC-DECT-MIB", "pktcDectStatusNumActivitySuccess"),
        ("PKTC-DECT-MIB", "pktcDectStatusLastActivityFailure"),
        ("PKTC-DECT-MIB", "pktcDectStatusRSSI"),
        ("PKTC-DECT-MIB", "pktcDectPPIPEI"),
        ("PKTC-DECT-MIB", "pktcDectPPTerminalID"),
        ("PKTC-DECT-MIB", "pktcDectPPStatus"),
        ("PKTC-DECT-MIB", "pktcDectPPRegCtrl"),
        ("PKTC-DECT-MIB", "pktcDectPPCapabilitiesDisplay"),
        ("PKTC-DECT-MIB", "pktcDectPPCapabilitiesTone"),
        ("PKTC-DECT-MIB", "pktcDectPPCapabilitiesEcho"),
        ("PKTC-DECT-MIB", "pktcDectPPCapabilitiesAmbientNoiseRejection"),
        ("PKTC-DECT-MIB", "pktcDectPPCapabilitiesAdaptiveVolumeCtrl"),
        ("PKTC-DECT-MIB", "pktcDectPPCapabilitiesSlotType"),
        ("PKTC-DECT-MIB", "pktcDectPPCapabilitiesStoredDisplayChars"),
        ("PKTC-DECT-MIB", "pktcDectPPCapabilitiesDisplayLines"),
        ("PKTC-DECT-MIB", "pktcDectPPCapabilitiesCharsPerDisplayLine"),
        ("PKTC-DECT-MIB", "pktcDectPPCapabilitiesScrollBehavior"),
        ("PKTC-DECT-MIB", "pktcDectPPCapabilitiesProfile"))
)
if mibBuilder.loadTexts:
    pktcDectGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

pktcDectCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 8, 4, 2, 1, 1)
)
pktcDectCompliance.setObjects(
    ("PKTC-DECT-MIB", "pktcDectGroup")
)
if mibBuilder.loadTexts:
    pktcDectCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PKTC-DECT-MIB",
    **{"PktcSpecVersion": PktcSpecVersion,
       "PktcDectPPState": PktcDectPPState,
       "pktcDectMib": pktcDectMib,
       "pktcDectNotifications": pktcDectNotifications,
       "pktcDectObjects": pktcDectObjects,
       "pktcDectFP": pktcDectFP,
       "pktcDectFPMaxNumPP": pktcDectFPMaxNumPP,
       "pktcDectFPMaxActivePP": pktcDectFPMaxActivePP,
       "pktcDectFPLockListCfg": pktcDectFPLockListCfg,
       "pktcDectFPZeroEmissionEnabled": pktcDectFPZeroEmissionEnabled,
       "pktcDectFPPairingType": pktcDectFPPairingType,
       "pktcDectFPEasyPairingActivate": pktcDectFPEasyPairingActivate,
       "pktcDectFPName": pktcDectFPName,
       "pktcDectFPGeneralCapabilities": pktcDectFPGeneralCapabilities,
       "pktcDectFPExtendedCapabilities": pktcDectFPExtendedCapabilities,
       "pktcDectHDVoiceProfile": pktcDectHDVoiceProfile,
       "pktcDectHDVoiceProfileBasicService": pktcDectHDVoiceProfileBasicService,
       "pktcDectHDVoiceProfileNCS": pktcDectHDVoiceProfileNCS,
       "pktcDectHDVoiceProfileSIP": pktcDectHDVoiceProfileSIP,
       "pktcDectCodec": pktcDectCodec,
       "pktcDectCodecPrefList": pktcDectCodecPrefList,
       "pktcDectDTMF": pktcDectDTMF,
       "pktcDectDTMFToneDuration": pktcDectDTMFToneDuration,
       "pktcDectBargeIn": pktcDectBargeIn,
       "pktcDectBargeInEnabled": pktcDectBargeInEnabled,
       "pktcDectServiceStatus": pktcDectServiceStatus,
       "pktcDectServiceStatusDeactivationDisplay": pktcDectServiceStatusDeactivationDisplay,
       "pktcDectServiceStatusConnectivityDisplay": pktcDectServiceStatusConnectivityDisplay,
       "pktcDectAnalogAlarmCfgTable": pktcDectAnalogAlarmCfgTable,
       "pktcDectAnalogAlarmCfgEntry": pktcDectAnalogAlarmCfgEntry,
       "pktcDectAnalogAlarmCfgState": pktcDectAnalogAlarmCfgState,
       "pktcDectPPTable": pktcDectPPTable,
       "pktcDectPPEntry": pktcDectPPEntry,
       "pktcDectPPId": pktcDectPPId,
       "pktcDectPPIPEI": pktcDectPPIPEI,
       "pktcDectPPTerminalID": pktcDectPPTerminalID,
       "pktcDectPPStatus": pktcDectPPStatus,
       "pktcDectPPRegCtrl": pktcDectPPRegCtrl,
       "pktcDectPPCapabilitiesTable": pktcDectPPCapabilitiesTable,
       "pktcDectPPCapabilitiesEntry": pktcDectPPCapabilitiesEntry,
       "pktcDectPPCapabilitiesDisplay": pktcDectPPCapabilitiesDisplay,
       "pktcDectPPCapabilitiesTone": pktcDectPPCapabilitiesTone,
       "pktcDectPPCapabilitiesEcho": pktcDectPPCapabilitiesEcho,
       "pktcDectPPCapabilitiesAmbientNoiseRejection": pktcDectPPCapabilitiesAmbientNoiseRejection,
       "pktcDectPPCapabilitiesAdaptiveVolumeCtrl": pktcDectPPCapabilitiesAdaptiveVolumeCtrl,
       "pktcDectPPCapabilitiesSlotType": pktcDectPPCapabilitiesSlotType,
       "pktcDectPPCapabilitiesStoredDisplayChars": pktcDectPPCapabilitiesStoredDisplayChars,
       "pktcDectPPCapabilitiesDisplayLines": pktcDectPPCapabilitiesDisplayLines,
       "pktcDectPPCapabilitiesCharsPerDisplayLine": pktcDectPPCapabilitiesCharsPerDisplayLine,
       "pktcDectPPCapabilitiesScrollBehavior": pktcDectPPCapabilitiesScrollBehavior,
       "pktcDectPPCapabilitiesProfile": pktcDectPPCapabilitiesProfile,
       "pktcDectListAccessTable": pktcDectListAccessTable,
       "pktcDectListAccessEntry": pktcDectListAccessEntry,
       "pktcDectListAccessIndex": pktcDectListAccessIndex,
       "pktcDectListAccesslistID": pktcDectListAccesslistID,
       "pktcDectListAccessDescr": pktcDectListAccessDescr,
       "pktcDectInternalNamesListTable": pktcDectInternalNamesListTable,
       "pktcDectInternalNamesListEntry": pktcDectInternalNamesListEntry,
       "pktcDectInternalNamesListIndex": pktcDectInternalNamesListIndex,
       "pktcDectInternalNamesListNumber": pktcDectInternalNamesListNumber,
       "pktcDectInternalNamesListName": pktcDectInternalNamesListName,
       "pktcDectLineSettingsListTable": pktcDectLineSettingsListTable,
       "pktcDectLineSettingsListEntry": pktcDectLineSettingsListEntry,
       "pktcDectLineSettingsListIndex": pktcDectLineSettingsListIndex,
       "pktcDectLineSettingsListLineId": pktcDectLineSettingsListLineId,
       "pktcDectLineSettingsListLineName": pktcDectLineSettingsListLineName,
       "pktcDectLineSettingsListAttachedHandsets": pktcDectLineSettingsListAttachedHandsets,
       "pktcDectLineSettingsListDialingPrefix": pktcDectLineSettingsListDialingPrefix,
       "pktcDectLineSettingsListFPMelody": pktcDectLineSettingsListFPMelody,
       "pktcDectLineSettingsListFPVolume": pktcDectLineSettingsListFPVolume,
       "pktcDectLineSettingsListBlockedNB": pktcDectLineSettingsListBlockedNB,
       "pktcDectLineSettingsListMultipleCalls": pktcDectLineSettingsListMultipleCalls,
       "pktcDectLineSettingsListIntrusionCall": pktcDectLineSettingsListIntrusionCall,
       "pktcDectPerformanceTable": pktcDectPerformanceTable,
       "pktcDectPerformanceEntry": pktcDectPerformanceEntry,
       "pktcDectPerformanceRecordNum": pktcDectPerformanceRecordNum,
       "pktcDectPerformanceHandovers": pktcDectPerformanceHandovers,
       "pktcDectPerformanceRTDelay": pktcDectPerformanceRTDelay,
       "pktcDectPerformanceSyncFailures": pktcDectPerformanceSyncFailures,
       "pktcDectPerformanceControlFieldErrs": pktcDectPerformanceControlFieldErrs,
       "pktcDectPerformancePayloadErrs": pktcDectPerformancePayloadErrs,
       "pktcDectPerformanceSlidingCollisions": pktcDectPerformanceSlidingCollisions,
       "pktcDectPerformanceLinkErrsQbit": pktcDectPerformanceLinkErrsQbit,
       "pktcDectStatusTable": pktcDectStatusTable,
       "pktcDectStatusEntry": pktcDectStatusEntry,
       "pktcDectStatusLastLocate": pktcDectStatusLastLocate,
       "pktcDectStatusNumLocateMsgs": pktcDectStatusNumLocateMsgs,
       "pktcDectStatusNumConnectionFailures": pktcDectStatusNumConnectionFailures,
       "pktcDectStatusNumActivitySuccess": pktcDectStatusNumActivitySuccess,
       "pktcDectStatusLastActivityFailure": pktcDectStatusLastActivityFailure,
       "pktcDectStatusRSSI": pktcDectStatusRSSI,
       "pktcDectMibConformance": pktcDectMibConformance,
       "pktcDectMibCompliances": pktcDectMibCompliances,
       "pktcDectCompliance": pktcDectCompliance,
       "pktcDectMibGroups": pktcDectMibGroups,
       "pktcDectGroup": pktcDectGroup}
)
