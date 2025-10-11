# SNMP MIB module (IPE-DOT3OAM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/nec/IPE-DOT3OAM-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:53:51 2025
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

(InterfaceIndex,
 InterfaceIndexOrZero) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero")

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
 MacAddress,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



class EnableDisableValue(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 0),
          ("disable", 1),
          ("enable", 2))
    )



class SeverityValue(TextualConvention, Integer32):
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
        *(("cleared", 1),
          ("indetermine", 2),
          ("critical", 3),
          ("major", 4),
          ("minor", 5),
          ("warning", 6))
    )



# MIB Managed Objects in the order of their OIDs

_Nec_ObjectIdentity = ObjectIdentity
nec = _Nec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119)
)
_Nec_mib_ObjectIdentity = ObjectIdentity
nec_mib = _Nec_mib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2)
)
_NecProductDepend_ObjectIdentity = ObjectIdentity
necProductDepend = _NecProductDepend_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2, 3)
)
_RadioEquipment_ObjectIdentity = ObjectIdentity
radioEquipment = _RadioEquipment_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69)
)
_PasoNeoIpe_common_ObjectIdentity = ObjectIdentity
pasoNeoIpe_common = _PasoNeoIpe_common_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501)
)
_AlarmStatusGroup_ObjectIdentity = ObjectIdentity
alarmStatusGroup = _AlarmStatusGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 3)
)
_AsDot3OamGroup_ObjectIdentity = ObjectIdentity
asDot3OamGroup = _AsDot3OamGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 3, 46)
)
_AsDot3OamPortTable_Object = MibTable
asDot3OamPortTable = _AsDot3OamPortTable_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 3, 46, 1)
)
if mibBuilder.loadTexts:
    asDot3OamPortTable.setStatus("current")
_AsDot3OamPortEntry_Object = MibTableRow
asDot3OamPortEntry = _AsDot3OamPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 3, 46, 1, 1)
)
asDot3OamPortEntry.setIndexNames(
    (0, "IPE-DOT3OAM-MIB", "asDot3OamPortIfIndex"),
)
if mibBuilder.loadTexts:
    asDot3OamPortEntry.setStatus("current")
_AsDot3OamPortIfIndex_Type = InterfaceIndex
_AsDot3OamPortIfIndex_Object = MibTableColumn
asDot3OamPortIfIndex = _AsDot3OamPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 3, 46, 1, 1, 1),
    _AsDot3OamPortIfIndex_Type()
)
asDot3OamPortIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    asDot3OamPortIfIndex.setStatus("current")
_AsDot3OamPortNEAddress_Type = IpAddress
_AsDot3OamPortNEAddress_Object = MibTableColumn
asDot3OamPortNEAddress = _AsDot3OamPortNEAddress_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 3, 46, 1, 1, 2),
    _AsDot3OamPortNEAddress_Type()
)
asDot3OamPortNEAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    asDot3OamPortNEAddress.setStatus("current")


class _AsDot3OamPortOperStatus_Type(Integer32):
    """Custom type asDot3OamPortOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
        *(("invalid", 0),
          ("disabled", 1),
          ("linkFault", 2),
          ("passiveWait", 3),
          ("activeSendLocal", 4),
          ("sendLocalAndRemote", 5),
          ("sendLocalAndRemoteOK", 6),
          ("oamPeeringLocallyRejected", 7),
          ("oamPeeringRemotelyRejected", 8),
          ("operational", 9),
          ("nonOperHalfDuplex", 10))
    )


_AsDot3OamPortOperStatus_Type.__name__ = "Integer32"
_AsDot3OamPortOperStatus_Object = MibTableColumn
asDot3OamPortOperStatus = _AsDot3OamPortOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 3, 46, 1, 1, 3),
    _AsDot3OamPortOperStatus_Type()
)
asDot3OamPortOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asDot3OamPortOperStatus.setStatus("current")


class _AsDot3OamPortMaxOamPduSize_Type(Unsigned32):
    """Custom type asDot3OamPortMaxOamPduSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(64, 1518),
    )


_AsDot3OamPortMaxOamPduSize_Type.__name__ = "Unsigned32"
_AsDot3OamPortMaxOamPduSize_Object = MibTableColumn
asDot3OamPortMaxOamPduSize = _AsDot3OamPortMaxOamPduSize_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 3, 46, 1, 1, 4),
    _AsDot3OamPortMaxOamPduSize_Type()
)
asDot3OamPortMaxOamPduSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asDot3OamPortMaxOamPduSize.setStatus("current")
if mibBuilder.loadTexts:
    asDot3OamPortMaxOamPduSize.setUnits("octets")


class _AsDot3OamPortConfigRevision_Type(Unsigned32):
    """Custom type asDot3OamPortConfigRevision based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AsDot3OamPortConfigRevision_Type.__name__ = "Unsigned32"
_AsDot3OamPortConfigRevision_Object = MibTableColumn
asDot3OamPortConfigRevision = _AsDot3OamPortConfigRevision_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 3, 46, 1, 1, 5),
    _AsDot3OamPortConfigRevision_Type()
)
asDot3OamPortConfigRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asDot3OamPortConfigRevision.setStatus("current")


class _AsDot3OamPortFunctionsSupported_Type(Bits):
    """Custom type asDot3OamPortFunctionsSupported based on Bits"""
    namedValues = NamedValues(
        *(("unidirectionalSupport", 0),
          ("loopbackSupport", 1),
          ("eventSupport", 2),
          ("variableSupport", 3))
    )

_AsDot3OamPortFunctionsSupported_Type.__name__ = "Bits"
_AsDot3OamPortFunctionsSupported_Object = MibTableColumn
asDot3OamPortFunctionsSupported = _AsDot3OamPortFunctionsSupported_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 3, 46, 1, 1, 6),
    _AsDot3OamPortFunctionsSupported_Type()
)
asDot3OamPortFunctionsSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asDot3OamPortFunctionsSupported.setStatus("current")
_AsDot3OamPeerTable_Object = MibTable
asDot3OamPeerTable = _AsDot3OamPeerTable_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 3, 46, 2)
)
if mibBuilder.loadTexts:
    asDot3OamPeerTable.setStatus("current")
_AsDot3OamPeerEntry_Object = MibTableRow
asDot3OamPeerEntry = _AsDot3OamPeerEntry_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 3, 46, 2, 1)
)
asDot3OamPeerEntry.setIndexNames(
    (0, "IPE-DOT3OAM-MIB", "asDot3OamPeerIfIndex"),
)
if mibBuilder.loadTexts:
    asDot3OamPeerEntry.setStatus("current")
_AsDot3OamPeerIfIndex_Type = InterfaceIndex
_AsDot3OamPeerIfIndex_Object = MibTableColumn
asDot3OamPeerIfIndex = _AsDot3OamPeerIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 3, 46, 2, 1, 1),
    _AsDot3OamPeerIfIndex_Type()
)
asDot3OamPeerIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    asDot3OamPeerIfIndex.setStatus("current")
_AsDot3OamPeerNEAddress_Type = IpAddress
_AsDot3OamPeerNEAddress_Object = MibTableColumn
asDot3OamPeerNEAddress = _AsDot3OamPeerNEAddress_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 3, 46, 2, 1, 2),
    _AsDot3OamPeerNEAddress_Type()
)
asDot3OamPeerNEAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    asDot3OamPeerNEAddress.setStatus("current")
_AsDot3OamPeerMacAddress_Type = MacAddress
_AsDot3OamPeerMacAddress_Object = MibTableColumn
asDot3OamPeerMacAddress = _AsDot3OamPeerMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 3, 46, 2, 1, 3),
    _AsDot3OamPeerMacAddress_Type()
)
asDot3OamPeerMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asDot3OamPeerMacAddress.setStatus("current")


class _AsDot3OamPeerVendorOui_Type(OctetString):
    """Custom type asDot3OamPeerVendorOui based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )
    fixed_length = 3


_AsDot3OamPeerVendorOui_Type.__name__ = "OctetString"
_AsDot3OamPeerVendorOui_Object = MibTableColumn
asDot3OamPeerVendorOui = _AsDot3OamPeerVendorOui_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 3, 46, 2, 1, 4),
    _AsDot3OamPeerVendorOui_Type()
)
asDot3OamPeerVendorOui.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asDot3OamPeerVendorOui.setStatus("current")
_AsDot3OamPeerVendorInfo_Type = Unsigned32
_AsDot3OamPeerVendorInfo_Object = MibTableColumn
asDot3OamPeerVendorInfo = _AsDot3OamPeerVendorInfo_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 3, 46, 2, 1, 5),
    _AsDot3OamPeerVendorInfo_Type()
)
asDot3OamPeerVendorInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asDot3OamPeerVendorInfo.setStatus("current")


class _AsDot3OamPeerMode_Type(Integer32):
    """Custom type asDot3OamPeerMode based on Integer32"""
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
        *(("invalid", 0),
          ("passive", 1),
          ("active", 2),
          ("unknown", 3))
    )


_AsDot3OamPeerMode_Type.__name__ = "Integer32"
_AsDot3OamPeerMode_Object = MibTableColumn
asDot3OamPeerMode = _AsDot3OamPeerMode_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 3, 46, 2, 1, 6),
    _AsDot3OamPeerMode_Type()
)
asDot3OamPeerMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asDot3OamPeerMode.setStatus("current")


class _AsDot3OamPeerMaxOamPduSize_Type(Unsigned32):
    """Custom type asDot3OamPeerMaxOamPduSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(64, 1518),
    )


_AsDot3OamPeerMaxOamPduSize_Type.__name__ = "Unsigned32"
_AsDot3OamPeerMaxOamPduSize_Object = MibTableColumn
asDot3OamPeerMaxOamPduSize = _AsDot3OamPeerMaxOamPduSize_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 3, 46, 2, 1, 7),
    _AsDot3OamPeerMaxOamPduSize_Type()
)
asDot3OamPeerMaxOamPduSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asDot3OamPeerMaxOamPduSize.setStatus("current")
if mibBuilder.loadTexts:
    asDot3OamPeerMaxOamPduSize.setUnits("octets")


class _AsDot3OamPeerConfigRevision_Type(Unsigned32):
    """Custom type asDot3OamPeerConfigRevision based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AsDot3OamPeerConfigRevision_Type.__name__ = "Unsigned32"
_AsDot3OamPeerConfigRevision_Object = MibTableColumn
asDot3OamPeerConfigRevision = _AsDot3OamPeerConfigRevision_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 3, 46, 2, 1, 8),
    _AsDot3OamPeerConfigRevision_Type()
)
asDot3OamPeerConfigRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asDot3OamPeerConfigRevision.setStatus("current")


class _AsDot3OamPeerFunctionsSupported_Type(Bits):
    """Custom type asDot3OamPeerFunctionsSupported based on Bits"""
    namedValues = NamedValues(
        *(("unidirectionalSupport", 0),
          ("loopbackSupport", 1),
          ("eventSupport", 2),
          ("variableSupport", 3))
    )

_AsDot3OamPeerFunctionsSupported_Type.__name__ = "Bits"
_AsDot3OamPeerFunctionsSupported_Object = MibTableColumn
asDot3OamPeerFunctionsSupported = _AsDot3OamPeerFunctionsSupported_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 3, 46, 2, 1, 9),
    _AsDot3OamPeerFunctionsSupported_Type()
)
asDot3OamPeerFunctionsSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asDot3OamPeerFunctionsSupported.setStatus("current")
_AsDot3OamPortStatsTable_Object = MibTable
asDot3OamPortStatsTable = _AsDot3OamPortStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 3, 46, 3)
)
if mibBuilder.loadTexts:
    asDot3OamPortStatsTable.setStatus("current")
_AsDot3OamPortStatsEntry_Object = MibTableRow
asDot3OamPortStatsEntry = _AsDot3OamPortStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 3, 46, 3, 1)
)
asDot3OamPortStatsEntry.setIndexNames(
    (0, "IPE-DOT3OAM-MIB", "asDot3OamPortStatsIfIndex"),
)
if mibBuilder.loadTexts:
    asDot3OamPortStatsEntry.setStatus("current")
_AsDot3OamPortStatsIfIndex_Type = InterfaceIndex
_AsDot3OamPortStatsIfIndex_Object = MibTableColumn
asDot3OamPortStatsIfIndex = _AsDot3OamPortStatsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 3, 46, 3, 1, 1),
    _AsDot3OamPortStatsIfIndex_Type()
)
asDot3OamPortStatsIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    asDot3OamPortStatsIfIndex.setStatus("current")
_AsDot3OamPortStatsNEAddress_Type = IpAddress
_AsDot3OamPortStatsNEAddress_Object = MibTableColumn
asDot3OamPortStatsNEAddress = _AsDot3OamPortStatsNEAddress_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 3, 46, 3, 1, 2),
    _AsDot3OamPortStatsNEAddress_Type()
)
asDot3OamPortStatsNEAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    asDot3OamPortStatsNEAddress.setStatus("current")
_AsDot3OamInformationTx_Type = Counter32
_AsDot3OamInformationTx_Object = MibTableColumn
asDot3OamInformationTx = _AsDot3OamInformationTx_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 3, 46, 3, 1, 3),
    _AsDot3OamInformationTx_Type()
)
asDot3OamInformationTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asDot3OamInformationTx.setStatus("current")
_AsDot3OamInformationRx_Type = Counter32
_AsDot3OamInformationRx_Object = MibTableColumn
asDot3OamInformationRx = _AsDot3OamInformationRx_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 3, 46, 3, 1, 4),
    _AsDot3OamInformationRx_Type()
)
asDot3OamInformationRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asDot3OamInformationRx.setStatus("current")
_AsDot3OamUniqueEventNotifTx_Type = Counter32
_AsDot3OamUniqueEventNotifTx_Object = MibTableColumn
asDot3OamUniqueEventNotifTx = _AsDot3OamUniqueEventNotifTx_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 3, 46, 3, 1, 5),
    _AsDot3OamUniqueEventNotifTx_Type()
)
asDot3OamUniqueEventNotifTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asDot3OamUniqueEventNotifTx.setStatus("current")
_AsDot3OamUniqueEventNotifRx_Type = Counter32
_AsDot3OamUniqueEventNotifRx_Object = MibTableColumn
asDot3OamUniqueEventNotifRx = _AsDot3OamUniqueEventNotifRx_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 3, 46, 3, 1, 6),
    _AsDot3OamUniqueEventNotifRx_Type()
)
asDot3OamUniqueEventNotifRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asDot3OamUniqueEventNotifRx.setStatus("current")
_AsDot3OamDuplicateEventNotifTx_Type = Counter32
_AsDot3OamDuplicateEventNotifTx_Object = MibTableColumn
asDot3OamDuplicateEventNotifTx = _AsDot3OamDuplicateEventNotifTx_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 3, 46, 3, 1, 7),
    _AsDot3OamDuplicateEventNotifTx_Type()
)
asDot3OamDuplicateEventNotifTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asDot3OamDuplicateEventNotifTx.setStatus("current")
_AsDot3OamDuplicateEventNotifRx_Type = Counter32
_AsDot3OamDuplicateEventNotifRx_Object = MibTableColumn
asDot3OamDuplicateEventNotifRx = _AsDot3OamDuplicateEventNotifRx_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 3, 46, 3, 1, 8),
    _AsDot3OamDuplicateEventNotifRx_Type()
)
asDot3OamDuplicateEventNotifRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asDot3OamDuplicateEventNotifRx.setStatus("current")
_AsDot3OamLoopbackControlTx_Type = Counter32
_AsDot3OamLoopbackControlTx_Object = MibTableColumn
asDot3OamLoopbackControlTx = _AsDot3OamLoopbackControlTx_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 3, 46, 3, 1, 9),
    _AsDot3OamLoopbackControlTx_Type()
)
asDot3OamLoopbackControlTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asDot3OamLoopbackControlTx.setStatus("current")
_AsDot3OamLoopbackControlRx_Type = Counter32
_AsDot3OamLoopbackControlRx_Object = MibTableColumn
asDot3OamLoopbackControlRx = _AsDot3OamLoopbackControlRx_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 3, 46, 3, 1, 10),
    _AsDot3OamLoopbackControlRx_Type()
)
asDot3OamLoopbackControlRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asDot3OamLoopbackControlRx.setStatus("current")
_AsDot3OamVariableRequestTx_Type = Counter32
_AsDot3OamVariableRequestTx_Object = MibTableColumn
asDot3OamVariableRequestTx = _AsDot3OamVariableRequestTx_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 3, 46, 3, 1, 11),
    _AsDot3OamVariableRequestTx_Type()
)
asDot3OamVariableRequestTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asDot3OamVariableRequestTx.setStatus("current")
_AsDot3OamVariableRequestRx_Type = Counter32
_AsDot3OamVariableRequestRx_Object = MibTableColumn
asDot3OamVariableRequestRx = _AsDot3OamVariableRequestRx_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 3, 46, 3, 1, 12),
    _AsDot3OamVariableRequestRx_Type()
)
asDot3OamVariableRequestRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asDot3OamVariableRequestRx.setStatus("current")
_AsDot3OamVariableResponseTx_Type = Counter32
_AsDot3OamVariableResponseTx_Object = MibTableColumn
asDot3OamVariableResponseTx = _AsDot3OamVariableResponseTx_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 3, 46, 3, 1, 13),
    _AsDot3OamVariableResponseTx_Type()
)
asDot3OamVariableResponseTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asDot3OamVariableResponseTx.setStatus("current")
_AsDot3OamVariableResponseRx_Type = Counter32
_AsDot3OamVariableResponseRx_Object = MibTableColumn
asDot3OamVariableResponseRx = _AsDot3OamVariableResponseRx_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 3, 46, 3, 1, 14),
    _AsDot3OamVariableResponseRx_Type()
)
asDot3OamVariableResponseRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asDot3OamVariableResponseRx.setStatus("current")
_AsDot3OamOrgSpecificTx_Type = Counter32
_AsDot3OamOrgSpecificTx_Object = MibTableColumn
asDot3OamOrgSpecificTx = _AsDot3OamOrgSpecificTx_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 3, 46, 3, 1, 15),
    _AsDot3OamOrgSpecificTx_Type()
)
asDot3OamOrgSpecificTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asDot3OamOrgSpecificTx.setStatus("current")
_AsDot3OamOrgSpecificRx_Type = Counter32
_AsDot3OamOrgSpecificRx_Object = MibTableColumn
asDot3OamOrgSpecificRx = _AsDot3OamOrgSpecificRx_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 3, 46, 3, 1, 16),
    _AsDot3OamOrgSpecificRx_Type()
)
asDot3OamOrgSpecificRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asDot3OamOrgSpecificRx.setStatus("current")
_AsDot3OamUnsupportedCodesTx_Type = Counter32
_AsDot3OamUnsupportedCodesTx_Object = MibTableColumn
asDot3OamUnsupportedCodesTx = _AsDot3OamUnsupportedCodesTx_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 3, 46, 3, 1, 17),
    _AsDot3OamUnsupportedCodesTx_Type()
)
asDot3OamUnsupportedCodesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asDot3OamUnsupportedCodesTx.setStatus("current")
_AsDot3OamUnsupportedCodesRx_Type = Counter32
_AsDot3OamUnsupportedCodesRx_Object = MibTableColumn
asDot3OamUnsupportedCodesRx = _AsDot3OamUnsupportedCodesRx_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 3, 46, 3, 1, 18),
    _AsDot3OamUnsupportedCodesRx_Type()
)
asDot3OamUnsupportedCodesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asDot3OamUnsupportedCodesRx.setStatus("current")
_AsDot3OamFramesLostDueToOam_Type = Counter32
_AsDot3OamFramesLostDueToOam_Object = MibTableColumn
asDot3OamFramesLostDueToOam = _AsDot3OamFramesLostDueToOam_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 3, 46, 3, 1, 19),
    _AsDot3OamFramesLostDueToOam_Type()
)
asDot3OamFramesLostDueToOam.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asDot3OamFramesLostDueToOam.setStatus("current")
_AsDot3OamPortAlarmTable_Object = MibTable
asDot3OamPortAlarmTable = _AsDot3OamPortAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 3, 46, 4)
)
if mibBuilder.loadTexts:
    asDot3OamPortAlarmTable.setStatus("current")
_AsDot3OamPortAlarmEntry_Object = MibTableRow
asDot3OamPortAlarmEntry = _AsDot3OamPortAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 3, 46, 4, 1)
)
asDot3OamPortAlarmEntry.setIndexNames(
    (0, "IPE-DOT3OAM-MIB", "asDot3OamPortAlarmIfIndex"),
)
if mibBuilder.loadTexts:
    asDot3OamPortAlarmEntry.setStatus("current")
_AsDot3OamPortAlarmIfIndex_Type = InterfaceIndex
_AsDot3OamPortAlarmIfIndex_Object = MibTableColumn
asDot3OamPortAlarmIfIndex = _AsDot3OamPortAlarmIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 3, 46, 4, 1, 1),
    _AsDot3OamPortAlarmIfIndex_Type()
)
asDot3OamPortAlarmIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    asDot3OamPortAlarmIfIndex.setStatus("current")
_AsDot3OamPortAlarmNEAddress_Type = IpAddress
_AsDot3OamPortAlarmNEAddress_Object = MibTableColumn
asDot3OamPortAlarmNEAddress = _AsDot3OamPortAlarmNEAddress_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 3, 46, 4, 1, 2),
    _AsDot3OamPortAlarmNEAddress_Type()
)
asDot3OamPortAlarmNEAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    asDot3OamPortAlarmNEAddress.setStatus("current")
_AsDot3OamPortLinkOamDown_Type = SeverityValue
_AsDot3OamPortLinkOamDown_Object = MibTableColumn
asDot3OamPortLinkOamDown = _AsDot3OamPortLinkOamDown_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 3, 46, 4, 1, 3),
    _AsDot3OamPortLinkOamDown_Type()
)
asDot3OamPortLinkOamDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asDot3OamPortLinkOamDown.setStatus("current")


class _AsDot3OamPortLocalDyingGasp_Type(Integer32):
    """Custom type asDot3OamPortLocalDyingGasp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 0),
          ("normal", 1),
          ("generated", 2))
    )


_AsDot3OamPortLocalDyingGasp_Type.__name__ = "Integer32"
_AsDot3OamPortLocalDyingGasp_Object = MibTableColumn
asDot3OamPortLocalDyingGasp = _AsDot3OamPortLocalDyingGasp_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 3, 46, 4, 1, 4),
    _AsDot3OamPortLocalDyingGasp_Type()
)
asDot3OamPortLocalDyingGasp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asDot3OamPortLocalDyingGasp.setStatus("current")


class _AsDot3OamPortLocalCriticalEvent_Type(Integer32):
    """Custom type asDot3OamPortLocalCriticalEvent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 0),
          ("normal", 1),
          ("generated", 2))
    )


_AsDot3OamPortLocalCriticalEvent_Type.__name__ = "Integer32"
_AsDot3OamPortLocalCriticalEvent_Object = MibTableColumn
asDot3OamPortLocalCriticalEvent = _AsDot3OamPortLocalCriticalEvent_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 3, 46, 4, 1, 5),
    _AsDot3OamPortLocalCriticalEvent_Type()
)
asDot3OamPortLocalCriticalEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asDot3OamPortLocalCriticalEvent.setStatus("current")


class _AsDot3OamPortRemoteErroredSymbolEvent_Type(Integer32):
    """Custom type asDot3OamPortRemoteErroredSymbolEvent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 0),
          ("normal", 1),
          ("received", 2))
    )


_AsDot3OamPortRemoteErroredSymbolEvent_Type.__name__ = "Integer32"
_AsDot3OamPortRemoteErroredSymbolEvent_Object = MibTableColumn
asDot3OamPortRemoteErroredSymbolEvent = _AsDot3OamPortRemoteErroredSymbolEvent_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 3, 46, 4, 1, 6),
    _AsDot3OamPortRemoteErroredSymbolEvent_Type()
)
asDot3OamPortRemoteErroredSymbolEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asDot3OamPortRemoteErroredSymbolEvent.setStatus("current")


class _AsDot3OamPortRemoteErroredFramePeriodEvent_Type(Integer32):
    """Custom type asDot3OamPortRemoteErroredFramePeriodEvent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 0),
          ("normal", 1),
          ("received", 2))
    )


_AsDot3OamPortRemoteErroredFramePeriodEvent_Type.__name__ = "Integer32"
_AsDot3OamPortRemoteErroredFramePeriodEvent_Object = MibTableColumn
asDot3OamPortRemoteErroredFramePeriodEvent = _AsDot3OamPortRemoteErroredFramePeriodEvent_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 3, 46, 4, 1, 7),
    _AsDot3OamPortRemoteErroredFramePeriodEvent_Type()
)
asDot3OamPortRemoteErroredFramePeriodEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asDot3OamPortRemoteErroredFramePeriodEvent.setStatus("current")


class _AsDot3OamPortRemoteErroredFrameEvent_Type(Integer32):
    """Custom type asDot3OamPortRemoteErroredFrameEvent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 0),
          ("normal", 1),
          ("received", 2))
    )


_AsDot3OamPortRemoteErroredFrameEvent_Type.__name__ = "Integer32"
_AsDot3OamPortRemoteErroredFrameEvent_Object = MibTableColumn
asDot3OamPortRemoteErroredFrameEvent = _AsDot3OamPortRemoteErroredFrameEvent_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 3, 46, 4, 1, 8),
    _AsDot3OamPortRemoteErroredFrameEvent_Type()
)
asDot3OamPortRemoteErroredFrameEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asDot3OamPortRemoteErroredFrameEvent.setStatus("current")


class _AsDot3OamPortRemoteErroredFrameSecondEvent_Type(Integer32):
    """Custom type asDot3OamPortRemoteErroredFrameSecondEvent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 0),
          ("normal", 1),
          ("received", 2))
    )


_AsDot3OamPortRemoteErroredFrameSecondEvent_Type.__name__ = "Integer32"
_AsDot3OamPortRemoteErroredFrameSecondEvent_Object = MibTableColumn
asDot3OamPortRemoteErroredFrameSecondEvent = _AsDot3OamPortRemoteErroredFrameSecondEvent_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 3, 46, 4, 1, 9),
    _AsDot3OamPortRemoteErroredFrameSecondEvent_Type()
)
asDot3OamPortRemoteErroredFrameSecondEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asDot3OamPortRemoteErroredFrameSecondEvent.setStatus("current")
_AsDot3OamPortRemoteLinkFault_Type = SeverityValue
_AsDot3OamPortRemoteLinkFault_Object = MibTableColumn
asDot3OamPortRemoteLinkFault = _AsDot3OamPortRemoteLinkFault_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 3, 46, 4, 1, 10),
    _AsDot3OamPortRemoteLinkFault_Type()
)
asDot3OamPortRemoteLinkFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asDot3OamPortRemoteLinkFault.setStatus("current")
_AsDot3OamPortRemoteDyingGasp_Type = SeverityValue
_AsDot3OamPortRemoteDyingGasp_Object = MibTableColumn
asDot3OamPortRemoteDyingGasp = _AsDot3OamPortRemoteDyingGasp_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 3, 46, 4, 1, 11),
    _AsDot3OamPortRemoteDyingGasp_Type()
)
asDot3OamPortRemoteDyingGasp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asDot3OamPortRemoteDyingGasp.setStatus("current")
_AsDot3OamPortRemoteCriticalEvent_Type = SeverityValue
_AsDot3OamPortRemoteCriticalEvent_Object = MibTableColumn
asDot3OamPortRemoteCriticalEvent = _AsDot3OamPortRemoteCriticalEvent_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 3, 46, 4, 1, 12),
    _AsDot3OamPortRemoteCriticalEvent_Type()
)
asDot3OamPortRemoteCriticalEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asDot3OamPortRemoteCriticalEvent.setStatus("current")
_ProvisioningGroup_ObjectIdentity = ObjectIdentity
provisioningGroup = _ProvisioningGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5)
)
_ProvDot3OamGroup_ObjectIdentity = ObjectIdentity
provDot3OamGroup = _ProvDot3OamGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 46)
)
_ProvDot3OamPortTable_Object = MibTable
provDot3OamPortTable = _ProvDot3OamPortTable_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 46, 1)
)
if mibBuilder.loadTexts:
    provDot3OamPortTable.setStatus("current")
_ProvDot3OamPortEntry_Object = MibTableRow
provDot3OamPortEntry = _ProvDot3OamPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 46, 1, 1)
)
provDot3OamPortEntry.setIndexNames(
    (0, "IPE-DOT3OAM-MIB", "provDot3OamPortIfIndex"),
)
if mibBuilder.loadTexts:
    provDot3OamPortEntry.setStatus("current")
_ProvDot3OamPortIfIndex_Type = InterfaceIndex
_ProvDot3OamPortIfIndex_Object = MibTableColumn
provDot3OamPortIfIndex = _ProvDot3OamPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 46, 1, 1, 1),
    _ProvDot3OamPortIfIndex_Type()
)
provDot3OamPortIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    provDot3OamPortIfIndex.setStatus("current")
_ProvDot3OamPortNEAddress_Type = IpAddress
_ProvDot3OamPortNEAddress_Object = MibTableColumn
provDot3OamPortNEAddress = _ProvDot3OamPortNEAddress_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 46, 1, 1, 2),
    _ProvDot3OamPortNEAddress_Type()
)
provDot3OamPortNEAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    provDot3OamPortNEAddress.setStatus("current")


class _ProvDot3OamPortEnabled_Type(EnableDisableValue):
    """Custom type provDot3OamPortEnabled based on EnableDisableValue"""
    defaultValue = 1


_ProvDot3OamPortEnabled_Type.__name__ = "EnableDisableValue"
_ProvDot3OamPortEnabled_Object = MibTableColumn
provDot3OamPortEnabled = _ProvDot3OamPortEnabled_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 46, 1, 1, 3),
    _ProvDot3OamPortEnabled_Type()
)
provDot3OamPortEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    provDot3OamPortEnabled.setStatus("current")


class _ProvDot3OamPortMode_Type(Integer32):
    """Custom type provDot3OamPortMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("passive", 1),
          ("active", 2))
    )


_ProvDot3OamPortMode_Type.__name__ = "Integer32"
_ProvDot3OamPortMode_Object = MibTableColumn
provDot3OamPortMode = _ProvDot3OamPortMode_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 46, 1, 1, 4),
    _ProvDot3OamPortMode_Type()
)
provDot3OamPortMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    provDot3OamPortMode.setStatus("current")


class _ProvDot3OamTxPduRepetitionTimes_Type(Integer32):
    """Custom type provDot3OamTxPduRepetitionTimes based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_ProvDot3OamTxPduRepetitionTimes_Type.__name__ = "Integer32"
_ProvDot3OamTxPduRepetitionTimes_Object = MibTableColumn
provDot3OamTxPduRepetitionTimes = _ProvDot3OamTxPduRepetitionTimes_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 46, 1, 1, 5),
    _ProvDot3OamTxPduRepetitionTimes_Type()
)
provDot3OamTxPduRepetitionTimes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    provDot3OamTxPduRepetitionTimes.setStatus("current")


class _ProvDot3OamLocalLinkLostTimer_Type(Integer32):
    """Custom type provDot3OamLocalLinkLostTimer based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_ProvDot3OamLocalLinkLostTimer_Type.__name__ = "Integer32"
_ProvDot3OamLocalLinkLostTimer_Object = MibTableColumn
provDot3OamLocalLinkLostTimer = _ProvDot3OamLocalLinkLostTimer_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 46, 1, 1, 6),
    _ProvDot3OamLocalLinkLostTimer_Type()
)
provDot3OamLocalLinkLostTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    provDot3OamLocalLinkLostTimer.setStatus("current")
if mibBuilder.loadTexts:
    provDot3OamLocalLinkLostTimer.setUnits("seconds")


class _ProvDot3OamTxPduCounts_Type(Integer32):
    """Custom type provDot3OamTxPduCounts based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_ProvDot3OamTxPduCounts_Type.__name__ = "Integer32"
_ProvDot3OamTxPduCounts_Object = MibTableColumn
provDot3OamTxPduCounts = _ProvDot3OamTxPduCounts_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 46, 1, 1, 7),
    _ProvDot3OamTxPduCounts_Type()
)
provDot3OamTxPduCounts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    provDot3OamTxPduCounts.setStatus("current")


class _ProvDot3OamLoopbackIgnoreRx_Type(Integer32):
    """Custom type provDot3OamLoopbackIgnoreRx based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ignore", 1),
          ("process", 2))
    )


_ProvDot3OamLoopbackIgnoreRx_Type.__name__ = "Integer32"
_ProvDot3OamLoopbackIgnoreRx_Object = MibTableColumn
provDot3OamLoopbackIgnoreRx = _ProvDot3OamLoopbackIgnoreRx_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 46, 1, 1, 8),
    _ProvDot3OamLoopbackIgnoreRx_Type()
)
provDot3OamLoopbackIgnoreRx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    provDot3OamLoopbackIgnoreRx.setStatus("current")


class _ProvDot3OamLlfCriticalEvent_Type(EnableDisableValue):
    """Custom type provDot3OamLlfCriticalEvent based on EnableDisableValue"""
    defaultValue = 2


_ProvDot3OamLlfCriticalEvent_Type.__name__ = "EnableDisableValue"
_ProvDot3OamLlfCriticalEvent_Object = MibTableColumn
provDot3OamLlfCriticalEvent = _ProvDot3OamLlfCriticalEvent_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 46, 1, 1, 9),
    _ProvDot3OamLlfCriticalEvent_Type()
)
provDot3OamLlfCriticalEvent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    provDot3OamLlfCriticalEvent.setStatus("current")
_ProvDot3OamEventTable_Object = MibTable
provDot3OamEventTable = _ProvDot3OamEventTable_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 46, 3)
)
if mibBuilder.loadTexts:
    provDot3OamEventTable.setStatus("current")
_ProvDot3OamEventEntry_Object = MibTableRow
provDot3OamEventEntry = _ProvDot3OamEventEntry_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 46, 3, 1)
)
provDot3OamEventEntry.setIndexNames(
    (0, "IPE-DOT3OAM-MIB", "provDot3OamEventIfIndex"),
)
if mibBuilder.loadTexts:
    provDot3OamEventEntry.setStatus("current")
_ProvDot3OamEventIfIndex_Type = InterfaceIndex
_ProvDot3OamEventIfIndex_Object = MibTableColumn
provDot3OamEventIfIndex = _ProvDot3OamEventIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 46, 3, 1, 1),
    _ProvDot3OamEventIfIndex_Type()
)
provDot3OamEventIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    provDot3OamEventIfIndex.setStatus("current")
_ProvDot3OamEventNEAddress_Type = IpAddress
_ProvDot3OamEventNEAddress_Object = MibTableColumn
provDot3OamEventNEAddress = _ProvDot3OamEventNEAddress_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 46, 3, 1, 2),
    _ProvDot3OamEventNEAddress_Type()
)
provDot3OamEventNEAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    provDot3OamEventNEAddress.setStatus("current")


class _ProvDot3OamErrSymPeriodEvNotifEnable_Type(EnableDisableValue):
    """Custom type provDot3OamErrSymPeriodEvNotifEnable based on EnableDisableValue"""
    defaultValue = 1


_ProvDot3OamErrSymPeriodEvNotifEnable_Type.__name__ = "EnableDisableValue"
_ProvDot3OamErrSymPeriodEvNotifEnable_Object = MibTableColumn
provDot3OamErrSymPeriodEvNotifEnable = _ProvDot3OamErrSymPeriodEvNotifEnable_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 46, 3, 1, 3),
    _ProvDot3OamErrSymPeriodEvNotifEnable_Type()
)
provDot3OamErrSymPeriodEvNotifEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    provDot3OamErrSymPeriodEvNotifEnable.setStatus("current")


class _ProvDot3OamErrFramePeriodEvNotifEnable_Type(EnableDisableValue):
    """Custom type provDot3OamErrFramePeriodEvNotifEnable based on EnableDisableValue"""
    defaultValue = 1


_ProvDot3OamErrFramePeriodEvNotifEnable_Type.__name__ = "EnableDisableValue"
_ProvDot3OamErrFramePeriodEvNotifEnable_Object = MibTableColumn
provDot3OamErrFramePeriodEvNotifEnable = _ProvDot3OamErrFramePeriodEvNotifEnable_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 46, 3, 1, 4),
    _ProvDot3OamErrFramePeriodEvNotifEnable_Type()
)
provDot3OamErrFramePeriodEvNotifEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    provDot3OamErrFramePeriodEvNotifEnable.setStatus("current")


class _ProvDot3OamErrFrameEvNotifEnable_Type(EnableDisableValue):
    """Custom type provDot3OamErrFrameEvNotifEnable based on EnableDisableValue"""
    defaultValue = 1


_ProvDot3OamErrFrameEvNotifEnable_Type.__name__ = "EnableDisableValue"
_ProvDot3OamErrFrameEvNotifEnable_Object = MibTableColumn
provDot3OamErrFrameEvNotifEnable = _ProvDot3OamErrFrameEvNotifEnable_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 46, 3, 1, 5),
    _ProvDot3OamErrFrameEvNotifEnable_Type()
)
provDot3OamErrFrameEvNotifEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    provDot3OamErrFrameEvNotifEnable.setStatus("current")


class _ProvDot3OamErrFrameSecsEvNotifEnable_Type(EnableDisableValue):
    """Custom type provDot3OamErrFrameSecsEvNotifEnable based on EnableDisableValue"""
    defaultValue = 1


_ProvDot3OamErrFrameSecsEvNotifEnable_Type.__name__ = "EnableDisableValue"
_ProvDot3OamErrFrameSecsEvNotifEnable_Object = MibTableColumn
provDot3OamErrFrameSecsEvNotifEnable = _ProvDot3OamErrFrameSecsEvNotifEnable_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 46, 3, 1, 6),
    _ProvDot3OamErrFrameSecsEvNotifEnable_Type()
)
provDot3OamErrFrameSecsEvNotifEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    provDot3OamErrFrameSecsEvNotifEnable.setStatus("current")


class _ProvDot3OamDyingGaspEnable_Type(EnableDisableValue):
    """Custom type provDot3OamDyingGaspEnable based on EnableDisableValue"""
    defaultValue = 2


_ProvDot3OamDyingGaspEnable_Type.__name__ = "EnableDisableValue"
_ProvDot3OamDyingGaspEnable_Object = MibTableColumn
provDot3OamDyingGaspEnable = _ProvDot3OamDyingGaspEnable_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 46, 3, 1, 7),
    _ProvDot3OamDyingGaspEnable_Type()
)
provDot3OamDyingGaspEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    provDot3OamDyingGaspEnable.setStatus("current")


class _ProvDot3OamCriticalEventEnable_Type(EnableDisableValue):
    """Custom type provDot3OamCriticalEventEnable based on EnableDisableValue"""
    defaultValue = 2


_ProvDot3OamCriticalEventEnable_Type.__name__ = "EnableDisableValue"
_ProvDot3OamCriticalEventEnable_Object = MibTableColumn
provDot3OamCriticalEventEnable = _ProvDot3OamCriticalEventEnable_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 46, 3, 1, 8),
    _ProvDot3OamCriticalEventEnable_Type()
)
provDot3OamCriticalEventEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    provDot3OamCriticalEventEnable.setStatus("current")
_MaintenanceGroup_ObjectIdentity = ObjectIdentity
maintenanceGroup = _MaintenanceGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 6)
)
_MaintDot3OamGroup_ObjectIdentity = ObjectIdentity
maintDot3OamGroup = _MaintDot3OamGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 6, 46)
)
_MaintDot3OamLoopbackTable_Object = MibTable
maintDot3OamLoopbackTable = _MaintDot3OamLoopbackTable_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 6, 46, 1)
)
if mibBuilder.loadTexts:
    maintDot3OamLoopbackTable.setStatus("current")
_MaintDot3OamLoopbackEntry_Object = MibTableRow
maintDot3OamLoopbackEntry = _MaintDot3OamLoopbackEntry_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 6, 46, 1, 1)
)
maintDot3OamLoopbackEntry.setIndexNames(
    (0, "IPE-DOT3OAM-MIB", "maintDot3OamLoopbackIndex"),
)
if mibBuilder.loadTexts:
    maintDot3OamLoopbackEntry.setStatus("current")


class _MaintDot3OamLoopbackIndex_Type(Integer32):
    """Custom type maintDot3OamLoopbackIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_MaintDot3OamLoopbackIndex_Type.__name__ = "Integer32"
_MaintDot3OamLoopbackIndex_Object = MibTableColumn
maintDot3OamLoopbackIndex = _MaintDot3OamLoopbackIndex_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 6, 46, 1, 1, 1),
    _MaintDot3OamLoopbackIndex_Type()
)
maintDot3OamLoopbackIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    maintDot3OamLoopbackIndex.setStatus("current")
_MaintDot3OamLoopbackNEAddress_Type = IpAddress
_MaintDot3OamLoopbackNEAddress_Object = MibTableColumn
maintDot3OamLoopbackNEAddress = _MaintDot3OamLoopbackNEAddress_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 6, 46, 1, 1, 2),
    _MaintDot3OamLoopbackNEAddress_Type()
)
maintDot3OamLoopbackNEAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    maintDot3OamLoopbackNEAddress.setStatus("current")
_MaintDot3OamLoopbackIfIndex_Type = InterfaceIndexOrZero
_MaintDot3OamLoopbackIfIndex_Object = MibTableColumn
maintDot3OamLoopbackIfIndex = _MaintDot3OamLoopbackIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 6, 46, 1, 1, 3),
    _MaintDot3OamLoopbackIfIndex_Type()
)
maintDot3OamLoopbackIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    maintDot3OamLoopbackIfIndex.setStatus("current")


class _MaintDot3OamLoopbackExecute_Type(Integer32):
    """Custom type maintDot3OamLoopbackExecute based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("start", 1),
          ("stop", 2))
    )


_MaintDot3OamLoopbackExecute_Type.__name__ = "Integer32"
_MaintDot3OamLoopbackExecute_Object = MibTableColumn
maintDot3OamLoopbackExecute = _MaintDot3OamLoopbackExecute_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 6, 46, 1, 1, 4),
    _MaintDot3OamLoopbackExecute_Type()
)
maintDot3OamLoopbackExecute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    maintDot3OamLoopbackExecute.setStatus("current")


class _MaintDot3OamLoopbackFrames_Type(Unsigned32):
    """Custom type maintDot3OamLoopbackFrames based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MaintDot3OamLoopbackFrames_Type.__name__ = "Unsigned32"
_MaintDot3OamLoopbackFrames_Object = MibTableColumn
maintDot3OamLoopbackFrames = _MaintDot3OamLoopbackFrames_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 6, 46, 1, 1, 5),
    _MaintDot3OamLoopbackFrames_Type()
)
maintDot3OamLoopbackFrames.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    maintDot3OamLoopbackFrames.setStatus("current")


class _MaintDot3OamLoopbackPDULength_Type(Unsigned32):
    """Custom type maintDot3OamLoopbackPDULength based on Unsigned32"""
    defaultValue = 64

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(64, 1518),
    )


_MaintDot3OamLoopbackPDULength_Type.__name__ = "Unsigned32"
_MaintDot3OamLoopbackPDULength_Object = MibTableColumn
maintDot3OamLoopbackPDULength = _MaintDot3OamLoopbackPDULength_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 6, 46, 1, 1, 6),
    _MaintDot3OamLoopbackPDULength_Type()
)
maintDot3OamLoopbackPDULength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    maintDot3OamLoopbackPDULength.setStatus("current")


class _MaintDot3OamLoopbackTxCounts_Type(Unsigned32):
    """Custom type maintDot3OamLoopbackTxCounts based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_MaintDot3OamLoopbackTxCounts_Type.__name__ = "Unsigned32"
_MaintDot3OamLoopbackTxCounts_Object = MibTableColumn
maintDot3OamLoopbackTxCounts = _MaintDot3OamLoopbackTxCounts_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 6, 46, 1, 1, 7),
    _MaintDot3OamLoopbackTxCounts_Type()
)
maintDot3OamLoopbackTxCounts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    maintDot3OamLoopbackTxCounts.setStatus("current")


class _MaintDot3OamLoopbackTimeout_Type(Unsigned32):
    """Custom type maintDot3OamLoopbackTimeout based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_MaintDot3OamLoopbackTimeout_Type.__name__ = "Unsigned32"
_MaintDot3OamLoopbackTimeout_Object = MibTableColumn
maintDot3OamLoopbackTimeout = _MaintDot3OamLoopbackTimeout_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 6, 46, 1, 1, 8),
    _MaintDot3OamLoopbackTimeout_Type()
)
maintDot3OamLoopbackTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    maintDot3OamLoopbackTimeout.setStatus("current")
if mibBuilder.loadTexts:
    maintDot3OamLoopbackTimeout.setUnits("seconds")
_MaintDot3OamLoopbackResultTable_Object = MibTable
maintDot3OamLoopbackResultTable = _MaintDot3OamLoopbackResultTable_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 6, 46, 2)
)
if mibBuilder.loadTexts:
    maintDot3OamLoopbackResultTable.setStatus("current")
_MaintDot3OamLoopbackResultEntry_Object = MibTableRow
maintDot3OamLoopbackResultEntry = _MaintDot3OamLoopbackResultEntry_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 6, 46, 2, 1)
)
maintDot3OamLoopbackResultEntry.setIndexNames(
    (0, "IPE-DOT3OAM-MIB", "maintDot3OamLoopbackResultIndex"),
)
if mibBuilder.loadTexts:
    maintDot3OamLoopbackResultEntry.setStatus("current")


class _MaintDot3OamLoopbackResultIndex_Type(Integer32):
    """Custom type maintDot3OamLoopbackResultIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_MaintDot3OamLoopbackResultIndex_Type.__name__ = "Integer32"
_MaintDot3OamLoopbackResultIndex_Object = MibTableColumn
maintDot3OamLoopbackResultIndex = _MaintDot3OamLoopbackResultIndex_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 6, 46, 2, 1, 1),
    _MaintDot3OamLoopbackResultIndex_Type()
)
maintDot3OamLoopbackResultIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    maintDot3OamLoopbackResultIndex.setStatus("current")
_MaintDot3OamLoopbackResultNEAddress_Type = IpAddress
_MaintDot3OamLoopbackResultNEAddress_Object = MibTableColumn
maintDot3OamLoopbackResultNEAddress = _MaintDot3OamLoopbackResultNEAddress_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 6, 46, 2, 1, 2),
    _MaintDot3OamLoopbackResultNEAddress_Type()
)
maintDot3OamLoopbackResultNEAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    maintDot3OamLoopbackResultNEAddress.setStatus("current")
_MaintDot3OamLoopbackResultTxFrames_Type = Unsigned32
_MaintDot3OamLoopbackResultTxFrames_Object = MibTableColumn
maintDot3OamLoopbackResultTxFrames = _MaintDot3OamLoopbackResultTxFrames_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 6, 46, 2, 1, 3),
    _MaintDot3OamLoopbackResultTxFrames_Type()
)
maintDot3OamLoopbackResultTxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maintDot3OamLoopbackResultTxFrames.setStatus("current")
_MaintDot3OamLoopbackResultTxFrameOctets_Type = Unsigned32
_MaintDot3OamLoopbackResultTxFrameOctets_Object = MibTableColumn
maintDot3OamLoopbackResultTxFrameOctets = _MaintDot3OamLoopbackResultTxFrameOctets_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 6, 46, 2, 1, 4),
    _MaintDot3OamLoopbackResultTxFrameOctets_Type()
)
maintDot3OamLoopbackResultTxFrameOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maintDot3OamLoopbackResultTxFrameOctets.setStatus("current")
_MaintDot3OamLoopbackResultRxFrames_Type = Unsigned32
_MaintDot3OamLoopbackResultRxFrames_Object = MibTableColumn
maintDot3OamLoopbackResultRxFrames = _MaintDot3OamLoopbackResultRxFrames_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 6, 46, 2, 1, 5),
    _MaintDot3OamLoopbackResultRxFrames_Type()
)
maintDot3OamLoopbackResultRxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maintDot3OamLoopbackResultRxFrames.setStatus("current")
_MaintDot3OamLoopbackResultRxFrameOctets_Type = Unsigned32
_MaintDot3OamLoopbackResultRxFrameOctets_Object = MibTableColumn
maintDot3OamLoopbackResultRxFrameOctets = _MaintDot3OamLoopbackResultRxFrameOctets_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 6, 46, 2, 1, 6),
    _MaintDot3OamLoopbackResultRxFrameOctets_Type()
)
maintDot3OamLoopbackResultRxFrameOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maintDot3OamLoopbackResultRxFrameOctets.setStatus("current")
_MaintDot3OamLoopbackResultRxErroredFrames_Type = Unsigned32
_MaintDot3OamLoopbackResultRxErroredFrames_Object = MibTableColumn
maintDot3OamLoopbackResultRxErroredFrames = _MaintDot3OamLoopbackResultRxErroredFrames_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 6, 46, 2, 1, 7),
    _MaintDot3OamLoopbackResultRxErroredFrames_Type()
)
maintDot3OamLoopbackResultRxErroredFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maintDot3OamLoopbackResultRxErroredFrames.setStatus("current")


class _MaintDot3OamLoopbackResultExecStatus_Type(Integer32):
    """Custom type maintDot3OamLoopbackResultExecStatus based on Integer32"""
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
        *(("noLoopback", 1),
          ("failed", 2),
          ("completed", 3),
          ("executing", 4))
    )


_MaintDot3OamLoopbackResultExecStatus_Type.__name__ = "Integer32"
_MaintDot3OamLoopbackResultExecStatus_Object = MibTableColumn
maintDot3OamLoopbackResultExecStatus = _MaintDot3OamLoopbackResultExecStatus_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 6, 46, 2, 1, 8),
    _MaintDot3OamLoopbackResultExecStatus_Type()
)
maintDot3OamLoopbackResultExecStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maintDot3OamLoopbackResultExecStatus.setStatus("current")
_MaintDot3OamLoopbackResultLastExecute_Type = DateAndTime
_MaintDot3OamLoopbackResultLastExecute_Object = MibTableColumn
maintDot3OamLoopbackResultLastExecute = _MaintDot3OamLoopbackResultLastExecute_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 6, 46, 2, 1, 9),
    _MaintDot3OamLoopbackResultLastExecute_Type()
)
maintDot3OamLoopbackResultLastExecute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maintDot3OamLoopbackResultLastExecute.setStatus("current")
_MaintDot3OamLoopbackPortTable_Object = MibTable
maintDot3OamLoopbackPortTable = _MaintDot3OamLoopbackPortTable_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 6, 46, 3)
)
if mibBuilder.loadTexts:
    maintDot3OamLoopbackPortTable.setStatus("current")
_MaintDot3OamLoopbackPortEntry_Object = MibTableRow
maintDot3OamLoopbackPortEntry = _MaintDot3OamLoopbackPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 6, 46, 3, 1)
)
maintDot3OamLoopbackPortEntry.setIndexNames(
    (0, "IPE-DOT3OAM-MIB", "maintDot3OamLoopbackPortIfIndex"),
)
if mibBuilder.loadTexts:
    maintDot3OamLoopbackPortEntry.setStatus("current")
_MaintDot3OamLoopbackPortIfIndex_Type = InterfaceIndex
_MaintDot3OamLoopbackPortIfIndex_Object = MibTableColumn
maintDot3OamLoopbackPortIfIndex = _MaintDot3OamLoopbackPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 6, 46, 3, 1, 1),
    _MaintDot3OamLoopbackPortIfIndex_Type()
)
maintDot3OamLoopbackPortIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    maintDot3OamLoopbackPortIfIndex.setStatus("current")
_MaintDot3OamLoopbackPortNEAddress_Type = IpAddress
_MaintDot3OamLoopbackPortNEAddress_Object = MibTableColumn
maintDot3OamLoopbackPortNEAddress = _MaintDot3OamLoopbackPortNEAddress_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 6, 46, 3, 1, 2),
    _MaintDot3OamLoopbackPortNEAddress_Type()
)
maintDot3OamLoopbackPortNEAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    maintDot3OamLoopbackPortNEAddress.setStatus("current")


class _MaintDot3OamLoopbackPortControl_Type(Integer32):
    """Custom type maintDot3OamLoopbackPortControl based on Integer32"""
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
        *(("invalid", 0),
          ("noOperation", 1),
          ("initiateLoopback", 2),
          ("terminateLoopback", 3))
    )


_MaintDot3OamLoopbackPortControl_Type.__name__ = "Integer32"
_MaintDot3OamLoopbackPortControl_Object = MibTableColumn
maintDot3OamLoopbackPortControl = _MaintDot3OamLoopbackPortControl_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 6, 46, 3, 1, 3),
    _MaintDot3OamLoopbackPortControl_Type()
)
maintDot3OamLoopbackPortControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    maintDot3OamLoopbackPortControl.setStatus("current")


class _MaintDot3OamLoopbackPortStatus_Type(Integer32):
    """Custom type maintDot3OamLoopbackPortStatus based on Integer32"""
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
        *(("invalid", 0),
          ("noLoopback", 1),
          ("remoteLoopback", 2),
          ("localLoopback", 3))
    )


_MaintDot3OamLoopbackPortStatus_Type.__name__ = "Integer32"
_MaintDot3OamLoopbackPortStatus_Object = MibTableColumn
maintDot3OamLoopbackPortStatus = _MaintDot3OamLoopbackPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 6, 46, 3, 1, 4),
    _MaintDot3OamLoopbackPortStatus_Type()
)
maintDot3OamLoopbackPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maintDot3OamLoopbackPortStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IPE-DOT3OAM-MIB",
    **{"EnableDisableValue": EnableDisableValue,
       "SeverityValue": SeverityValue,
       "nec": nec,
       "nec-mib": nec_mib,
       "necProductDepend": necProductDepend,
       "radioEquipment": radioEquipment,
       "pasoNeoIpe-common": pasoNeoIpe_common,
       "alarmStatusGroup": alarmStatusGroup,
       "asDot3OamGroup": asDot3OamGroup,
       "asDot3OamPortTable": asDot3OamPortTable,
       "asDot3OamPortEntry": asDot3OamPortEntry,
       "asDot3OamPortIfIndex": asDot3OamPortIfIndex,
       "asDot3OamPortNEAddress": asDot3OamPortNEAddress,
       "asDot3OamPortOperStatus": asDot3OamPortOperStatus,
       "asDot3OamPortMaxOamPduSize": asDot3OamPortMaxOamPduSize,
       "asDot3OamPortConfigRevision": asDot3OamPortConfigRevision,
       "asDot3OamPortFunctionsSupported": asDot3OamPortFunctionsSupported,
       "asDot3OamPeerTable": asDot3OamPeerTable,
       "asDot3OamPeerEntry": asDot3OamPeerEntry,
       "asDot3OamPeerIfIndex": asDot3OamPeerIfIndex,
       "asDot3OamPeerNEAddress": asDot3OamPeerNEAddress,
       "asDot3OamPeerMacAddress": asDot3OamPeerMacAddress,
       "asDot3OamPeerVendorOui": asDot3OamPeerVendorOui,
       "asDot3OamPeerVendorInfo": asDot3OamPeerVendorInfo,
       "asDot3OamPeerMode": asDot3OamPeerMode,
       "asDot3OamPeerMaxOamPduSize": asDot3OamPeerMaxOamPduSize,
       "asDot3OamPeerConfigRevision": asDot3OamPeerConfigRevision,
       "asDot3OamPeerFunctionsSupported": asDot3OamPeerFunctionsSupported,
       "asDot3OamPortStatsTable": asDot3OamPortStatsTable,
       "asDot3OamPortStatsEntry": asDot3OamPortStatsEntry,
       "asDot3OamPortStatsIfIndex": asDot3OamPortStatsIfIndex,
       "asDot3OamPortStatsNEAddress": asDot3OamPortStatsNEAddress,
       "asDot3OamInformationTx": asDot3OamInformationTx,
       "asDot3OamInformationRx": asDot3OamInformationRx,
       "asDot3OamUniqueEventNotifTx": asDot3OamUniqueEventNotifTx,
       "asDot3OamUniqueEventNotifRx": asDot3OamUniqueEventNotifRx,
       "asDot3OamDuplicateEventNotifTx": asDot3OamDuplicateEventNotifTx,
       "asDot3OamDuplicateEventNotifRx": asDot3OamDuplicateEventNotifRx,
       "asDot3OamLoopbackControlTx": asDot3OamLoopbackControlTx,
       "asDot3OamLoopbackControlRx": asDot3OamLoopbackControlRx,
       "asDot3OamVariableRequestTx": asDot3OamVariableRequestTx,
       "asDot3OamVariableRequestRx": asDot3OamVariableRequestRx,
       "asDot3OamVariableResponseTx": asDot3OamVariableResponseTx,
       "asDot3OamVariableResponseRx": asDot3OamVariableResponseRx,
       "asDot3OamOrgSpecificTx": asDot3OamOrgSpecificTx,
       "asDot3OamOrgSpecificRx": asDot3OamOrgSpecificRx,
       "asDot3OamUnsupportedCodesTx": asDot3OamUnsupportedCodesTx,
       "asDot3OamUnsupportedCodesRx": asDot3OamUnsupportedCodesRx,
       "asDot3OamFramesLostDueToOam": asDot3OamFramesLostDueToOam,
       "asDot3OamPortAlarmTable": asDot3OamPortAlarmTable,
       "asDot3OamPortAlarmEntry": asDot3OamPortAlarmEntry,
       "asDot3OamPortAlarmIfIndex": asDot3OamPortAlarmIfIndex,
       "asDot3OamPortAlarmNEAddress": asDot3OamPortAlarmNEAddress,
       "asDot3OamPortLinkOamDown": asDot3OamPortLinkOamDown,
       "asDot3OamPortLocalDyingGasp": asDot3OamPortLocalDyingGasp,
       "asDot3OamPortLocalCriticalEvent": asDot3OamPortLocalCriticalEvent,
       "asDot3OamPortRemoteErroredSymbolEvent": asDot3OamPortRemoteErroredSymbolEvent,
       "asDot3OamPortRemoteErroredFramePeriodEvent": asDot3OamPortRemoteErroredFramePeriodEvent,
       "asDot3OamPortRemoteErroredFrameEvent": asDot3OamPortRemoteErroredFrameEvent,
       "asDot3OamPortRemoteErroredFrameSecondEvent": asDot3OamPortRemoteErroredFrameSecondEvent,
       "asDot3OamPortRemoteLinkFault": asDot3OamPortRemoteLinkFault,
       "asDot3OamPortRemoteDyingGasp": asDot3OamPortRemoteDyingGasp,
       "asDot3OamPortRemoteCriticalEvent": asDot3OamPortRemoteCriticalEvent,
       "provisioningGroup": provisioningGroup,
       "provDot3OamGroup": provDot3OamGroup,
       "provDot3OamPortTable": provDot3OamPortTable,
       "provDot3OamPortEntry": provDot3OamPortEntry,
       "provDot3OamPortIfIndex": provDot3OamPortIfIndex,
       "provDot3OamPortNEAddress": provDot3OamPortNEAddress,
       "provDot3OamPortEnabled": provDot3OamPortEnabled,
       "provDot3OamPortMode": provDot3OamPortMode,
       "provDot3OamTxPduRepetitionTimes": provDot3OamTxPduRepetitionTimes,
       "provDot3OamLocalLinkLostTimer": provDot3OamLocalLinkLostTimer,
       "provDot3OamTxPduCounts": provDot3OamTxPduCounts,
       "provDot3OamLoopbackIgnoreRx": provDot3OamLoopbackIgnoreRx,
       "provDot3OamLlfCriticalEvent": provDot3OamLlfCriticalEvent,
       "provDot3OamEventTable": provDot3OamEventTable,
       "provDot3OamEventEntry": provDot3OamEventEntry,
       "provDot3OamEventIfIndex": provDot3OamEventIfIndex,
       "provDot3OamEventNEAddress": provDot3OamEventNEAddress,
       "provDot3OamErrSymPeriodEvNotifEnable": provDot3OamErrSymPeriodEvNotifEnable,
       "provDot3OamErrFramePeriodEvNotifEnable": provDot3OamErrFramePeriodEvNotifEnable,
       "provDot3OamErrFrameEvNotifEnable": provDot3OamErrFrameEvNotifEnable,
       "provDot3OamErrFrameSecsEvNotifEnable": provDot3OamErrFrameSecsEvNotifEnable,
       "provDot3OamDyingGaspEnable": provDot3OamDyingGaspEnable,
       "provDot3OamCriticalEventEnable": provDot3OamCriticalEventEnable,
       "maintenanceGroup": maintenanceGroup,
       "maintDot3OamGroup": maintDot3OamGroup,
       "maintDot3OamLoopbackTable": maintDot3OamLoopbackTable,
       "maintDot3OamLoopbackEntry": maintDot3OamLoopbackEntry,
       "maintDot3OamLoopbackIndex": maintDot3OamLoopbackIndex,
       "maintDot3OamLoopbackNEAddress": maintDot3OamLoopbackNEAddress,
       "maintDot3OamLoopbackIfIndex": maintDot3OamLoopbackIfIndex,
       "maintDot3OamLoopbackExecute": maintDot3OamLoopbackExecute,
       "maintDot3OamLoopbackFrames": maintDot3OamLoopbackFrames,
       "maintDot3OamLoopbackPDULength": maintDot3OamLoopbackPDULength,
       "maintDot3OamLoopbackTxCounts": maintDot3OamLoopbackTxCounts,
       "maintDot3OamLoopbackTimeout": maintDot3OamLoopbackTimeout,
       "maintDot3OamLoopbackResultTable": maintDot3OamLoopbackResultTable,
       "maintDot3OamLoopbackResultEntry": maintDot3OamLoopbackResultEntry,
       "maintDot3OamLoopbackResultIndex": maintDot3OamLoopbackResultIndex,
       "maintDot3OamLoopbackResultNEAddress": maintDot3OamLoopbackResultNEAddress,
       "maintDot3OamLoopbackResultTxFrames": maintDot3OamLoopbackResultTxFrames,
       "maintDot3OamLoopbackResultTxFrameOctets": maintDot3OamLoopbackResultTxFrameOctets,
       "maintDot3OamLoopbackResultRxFrames": maintDot3OamLoopbackResultRxFrames,
       "maintDot3OamLoopbackResultRxFrameOctets": maintDot3OamLoopbackResultRxFrameOctets,
       "maintDot3OamLoopbackResultRxErroredFrames": maintDot3OamLoopbackResultRxErroredFrames,
       "maintDot3OamLoopbackResultExecStatus": maintDot3OamLoopbackResultExecStatus,
       "maintDot3OamLoopbackResultLastExecute": maintDot3OamLoopbackResultLastExecute,
       "maintDot3OamLoopbackPortTable": maintDot3OamLoopbackPortTable,
       "maintDot3OamLoopbackPortEntry": maintDot3OamLoopbackPortEntry,
       "maintDot3OamLoopbackPortIfIndex": maintDot3OamLoopbackPortIfIndex,
       "maintDot3OamLoopbackPortNEAddress": maintDot3OamLoopbackPortNEAddress,
       "maintDot3OamLoopbackPortControl": maintDot3OamLoopbackPortControl,
       "maintDot3OamLoopbackPortStatus": maintDot3OamLoopbackPortStatus}
)
