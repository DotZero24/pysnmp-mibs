# SNMP MIB module (ARICENT-RM-TE-LINK-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/aricent/ARICENT-RM-TE-LINK-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:43:46 2025
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

(InterfaceIndexOrZero,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero",
    "ifIndex")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

futRMTe = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 72, 10)
)
if mibBuilder.loadTexts:
    futRMTe.setRevisions(
        ("2012-09-05 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class TeLinkPriority(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )



class TeLinkEncodingType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              5,
              7,
              8,
              9,
              11)
        )
    )
    namedValues = NamedValues(
        *(("packet", 1),
          ("ethernet", 2),
          ("ansiEtsiPdh", 3),
          ("sdhItuSonetAnsi", 5),
          ("digitalWrapper", 7),
          ("lambda", 8),
          ("fiber", 9),
          ("fiberChannel", 11))
    )



# MIB Managed Objects in the order of their OIDs

_FutRMTeLinkNotifications_ObjectIdentity = ObjectIdentity
futRMTeLinkNotifications = _FutRMTeLinkNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 72, 10, 0)
)
_FutRMTeLinkObjects_ObjectIdentity = ObjectIdentity
futRMTeLinkObjects = _FutRMTeLinkObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 72, 10, 1)
)
_FutRmTeLinkGeneralGroup_ObjectIdentity = ObjectIdentity
futRmTeLinkGeneralGroup = _FutRmTeLinkGeneralGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 72, 10, 1, 1)
)


class _FutRmTeLinkRegDeregistration_Type(Integer32):
    """Custom type futRmTeLinkRegDeregistration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("register", 1),
          ("deregister", 2))
    )


_FutRmTeLinkRegDeregistration_Type.__name__ = "Integer32"
_FutRmTeLinkRegDeregistration_Object = MibScalar
futRmTeLinkRegDeregistration = _FutRmTeLinkRegDeregistration_Object(
    (1, 3, 6, 1, 4, 1, 2076, 72, 10, 1, 1, 1),
    _FutRmTeLinkRegDeregistration_Type()
)
futRmTeLinkRegDeregistration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    futRmTeLinkRegDeregistration.setStatus("current")
_FutRMTeLinkTable_Object = MibTable
futRMTeLinkTable = _FutRMTeLinkTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 72, 10, 1, 2)
)
if mibBuilder.loadTexts:
    futRMTeLinkTable.setStatus("current")
_FutRMTeLinkEntry_Object = MibTableRow
futRMTeLinkEntry = _FutRMTeLinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 72, 10, 1, 2, 1)
)
futRMTeLinkEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    futRMTeLinkEntry.setStatus("current")
_FutRMTeLinkLocalIpAddr_Type = IpAddress
_FutRMTeLinkLocalIpAddr_Object = MibTableColumn
futRMTeLinkLocalIpAddr = _FutRMTeLinkLocalIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 2076, 72, 10, 1, 2, 1, 1),
    _FutRMTeLinkLocalIpAddr_Type()
)
futRMTeLinkLocalIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    futRMTeLinkLocalIpAddr.setStatus("current")
_FutRMTeLinkRemoteIpAddr_Type = IpAddress
_FutRMTeLinkRemoteIpAddr_Object = MibTableColumn
futRMTeLinkRemoteIpAddr = _FutRMTeLinkRemoteIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 2076, 72, 10, 1, 2, 1, 2),
    _FutRMTeLinkRemoteIpAddr_Type()
)
futRMTeLinkRemoteIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    futRMTeLinkRemoteIpAddr.setStatus("current")
_FutRMTeLinkRemoteRtrId_Type = IpAddress
_FutRMTeLinkRemoteRtrId_Object = MibTableColumn
futRMTeLinkRemoteRtrId = _FutRMTeLinkRemoteRtrId_Object(
    (1, 3, 6, 1, 4, 1, 2076, 72, 10, 1, 2, 1, 3),
    _FutRMTeLinkRemoteRtrId_Type()
)
futRMTeLinkRemoteRtrId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    futRMTeLinkRemoteRtrId.setStatus("current")
_FutRMTeLinkMetric_Type = Unsigned32
_FutRMTeLinkMetric_Object = MibTableColumn
futRMTeLinkMetric = _FutRMTeLinkMetric_Object(
    (1, 3, 6, 1, 4, 1, 2076, 72, 10, 1, 2, 1, 4),
    _FutRMTeLinkMetric_Type()
)
futRMTeLinkMetric.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    futRMTeLinkMetric.setStatus("current")


class _FutRMTeLinkProtectionType_Type(Integer32):
    """Custom type futRMTeLinkProtectionType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8,
              16,
              32,
              64,
              128)
        )
    )
    namedValues = NamedValues(
        *(("extraTraffic", 1),
          ("unprotected", 2),
          ("shared", 4),
          ("dedicated1For1", 8),
          ("dedicated1Plus1", 16),
          ("enhanced", 32),
          ("reserved1", 64),
          ("reserved2", 128))
    )


_FutRMTeLinkProtectionType_Type.__name__ = "Integer32"
_FutRMTeLinkProtectionType_Object = MibTableColumn
futRMTeLinkProtectionType = _FutRMTeLinkProtectionType_Object(
    (1, 3, 6, 1, 4, 1, 2076, 72, 10, 1, 2, 1, 5),
    _FutRMTeLinkProtectionType_Type()
)
futRMTeLinkProtectionType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    futRMTeLinkProtectionType.setStatus("current")
_FutRMTeLinkResourceClass_Type = Unsigned32
_FutRMTeLinkResourceClass_Object = MibTableColumn
futRMTeLinkResourceClass = _FutRMTeLinkResourceClass_Object(
    (1, 3, 6, 1, 4, 1, 2076, 72, 10, 1, 2, 1, 6),
    _FutRMTeLinkResourceClass_Type()
)
futRMTeLinkResourceClass.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    futRMTeLinkResourceClass.setStatus("current")
_FutRMTeLinkIncomingIfId_Type = InterfaceIndexOrZero
_FutRMTeLinkIncomingIfId_Object = MibTableColumn
futRMTeLinkIncomingIfId = _FutRMTeLinkIncomingIfId_Object(
    (1, 3, 6, 1, 4, 1, 2076, 72, 10, 1, 2, 1, 7),
    _FutRMTeLinkIncomingIfId_Type()
)
futRMTeLinkIncomingIfId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    futRMTeLinkIncomingIfId.setStatus("current")
_FutRMTeLinkOutgoingIfId_Type = InterfaceIndexOrZero
_FutRMTeLinkOutgoingIfId_Object = MibTableColumn
futRMTeLinkOutgoingIfId = _FutRMTeLinkOutgoingIfId_Object(
    (1, 3, 6, 1, 4, 1, 2076, 72, 10, 1, 2, 1, 8),
    _FutRMTeLinkOutgoingIfId_Type()
)
futRMTeLinkOutgoingIfId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    futRMTeLinkOutgoingIfId.setStatus("current")
_FutRMTeLinkMaxBw_Type = Unsigned32
_FutRMTeLinkMaxBw_Object = MibTableColumn
futRMTeLinkMaxBw = _FutRMTeLinkMaxBw_Object(
    (1, 3, 6, 1, 4, 1, 2076, 72, 10, 1, 2, 1, 9),
    _FutRMTeLinkMaxBw_Type()
)
futRMTeLinkMaxBw.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    futRMTeLinkMaxBw.setStatus("current")
if mibBuilder.loadTexts:
    futRMTeLinkMaxBw.setUnits("bytes per second")
_FutRMTeLinkMaxResBw_Type = Unsigned32
_FutRMTeLinkMaxResBw_Object = MibTableColumn
futRMTeLinkMaxResBw = _FutRMTeLinkMaxResBw_Object(
    (1, 3, 6, 1, 4, 1, 2076, 72, 10, 1, 2, 1, 10),
    _FutRMTeLinkMaxResBw_Type()
)
futRMTeLinkMaxResBw.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    futRMTeLinkMaxResBw.setStatus("current")
if mibBuilder.loadTexts:
    futRMTeLinkMaxResBw.setUnits("bytes per second")
_FutRMTeLinkAreaId_Type = Unsigned32
_FutRMTeLinkAreaId_Object = MibTableColumn
futRMTeLinkAreaId = _FutRMTeLinkAreaId_Object(
    (1, 3, 6, 1, 4, 1, 2076, 72, 10, 1, 2, 1, 11),
    _FutRMTeLinkAreaId_Type()
)
futRMTeLinkAreaId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    futRMTeLinkAreaId.setStatus("current")


class _FutRMTeLinkInfoType_Type(Integer32):
    """Custom type futRMTeLinkInfoType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("areaIdInfo", 1),
          ("datachannel", 2),
          ("dataAndControlChannel", 3))
    )


_FutRMTeLinkInfoType_Type.__name__ = "Integer32"
_FutRMTeLinkInfoType_Object = MibTableColumn
futRMTeLinkInfoType = _FutRMTeLinkInfoType_Object(
    (1, 3, 6, 1, 4, 1, 2076, 72, 10, 1, 2, 1, 12),
    _FutRMTeLinkInfoType_Type()
)
futRMTeLinkInfoType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    futRMTeLinkInfoType.setStatus("current")
_FutRMTeLinkRowStatus_Type = RowStatus
_FutRMTeLinkRowStatus_Object = MibTableColumn
futRMTeLinkRowStatus = _FutRMTeLinkRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 72, 10, 1, 2, 1, 13),
    _FutRMTeLinkRowStatus_Type()
)
futRMTeLinkRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    futRMTeLinkRowStatus.setStatus("current")
_FutRMTeLinkSwDescriptorTable_Object = MibTable
futRMTeLinkSwDescriptorTable = _FutRMTeLinkSwDescriptorTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 72, 10, 1, 3)
)
if mibBuilder.loadTexts:
    futRMTeLinkSwDescriptorTable.setStatus("current")
_FutRMTeLinkSwDescriptorEntry_Object = MibTableRow
futRMTeLinkSwDescriptorEntry = _FutRMTeLinkSwDescriptorEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 72, 10, 1, 3, 1)
)
futRMTeLinkSwDescriptorEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ARICENT-RM-TE-LINK-MIB", "futRMTeLinkSwDescriptorId"),
)
if mibBuilder.loadTexts:
    futRMTeLinkSwDescriptorEntry.setStatus("current")


class _FutRMTeLinkSwDescriptorId_Type(Unsigned32):
    """Custom type futRMTeLinkSwDescriptorId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_FutRMTeLinkSwDescriptorId_Type.__name__ = "Unsigned32"
_FutRMTeLinkSwDescriptorId_Object = MibTableColumn
futRMTeLinkSwDescriptorId = _FutRMTeLinkSwDescriptorId_Object(
    (1, 3, 6, 1, 4, 1, 2076, 72, 10, 1, 3, 1, 1),
    _FutRMTeLinkSwDescriptorId_Type()
)
futRMTeLinkSwDescriptorId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    futRMTeLinkSwDescriptorId.setStatus("current")


class _FutRMTeLinkSwDescrSwitchingCap_Type(Integer32):
    """Custom type futRMTeLinkSwDescrSwitchingCap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              51,
              100,
              150,
              200)
        )
    )
    namedValues = NamedValues(
        *(("psc1", 1),
          ("psc2", 2),
          ("psc3", 3),
          ("psc4", 4),
          ("l2sc", 51),
          ("tdm", 100),
          ("lsc", 150),
          ("fsc", 200))
    )


_FutRMTeLinkSwDescrSwitchingCap_Type.__name__ = "Integer32"
_FutRMTeLinkSwDescrSwitchingCap_Object = MibTableColumn
futRMTeLinkSwDescrSwitchingCap = _FutRMTeLinkSwDescrSwitchingCap_Object(
    (1, 3, 6, 1, 4, 1, 2076, 72, 10, 1, 3, 1, 2),
    _FutRMTeLinkSwDescrSwitchingCap_Type()
)
futRMTeLinkSwDescrSwitchingCap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    futRMTeLinkSwDescrSwitchingCap.setStatus("current")
_FutRMTeLinkSwDescrEncodingType_Type = TeLinkEncodingType
_FutRMTeLinkSwDescrEncodingType_Object = MibTableColumn
futRMTeLinkSwDescrEncodingType = _FutRMTeLinkSwDescrEncodingType_Object(
    (1, 3, 6, 1, 4, 1, 2076, 72, 10, 1, 3, 1, 3),
    _FutRMTeLinkSwDescrEncodingType_Type()
)
futRMTeLinkSwDescrEncodingType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    futRMTeLinkSwDescrEncodingType.setStatus("current")
_FutRMTeLinkSwDescrMinLSPBandwidth_Type = Unsigned32
_FutRMTeLinkSwDescrMinLSPBandwidth_Object = MibTableColumn
futRMTeLinkSwDescrMinLSPBandwidth = _FutRMTeLinkSwDescrMinLSPBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 2076, 72, 10, 1, 3, 1, 4),
    _FutRMTeLinkSwDescrMinLSPBandwidth_Type()
)
futRMTeLinkSwDescrMinLSPBandwidth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    futRMTeLinkSwDescrMinLSPBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    futRMTeLinkSwDescrMinLSPBandwidth.setUnits("bytes per second")
_FutRMTeLinkSwDescrMTU_Type = Unsigned32
_FutRMTeLinkSwDescrMTU_Object = MibTableColumn
futRMTeLinkSwDescrMTU = _FutRMTeLinkSwDescrMTU_Object(
    (1, 3, 6, 1, 4, 1, 2076, 72, 10, 1, 3, 1, 5),
    _FutRMTeLinkSwDescrMTU_Type()
)
futRMTeLinkSwDescrMTU.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    futRMTeLinkSwDescrMTU.setStatus("current")
_FutRMTeLinkSwDescrIndication_Type = Unsigned32
_FutRMTeLinkSwDescrIndication_Object = MibTableColumn
futRMTeLinkSwDescrIndication = _FutRMTeLinkSwDescrIndication_Object(
    (1, 3, 6, 1, 4, 1, 2076, 72, 10, 1, 3, 1, 6),
    _FutRMTeLinkSwDescrIndication_Type()
)
futRMTeLinkSwDescrIndication.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    futRMTeLinkSwDescrIndication.setStatus("current")
_FutRMTeLinkSwDescrRowStatus_Type = RowStatus
_FutRMTeLinkSwDescrRowStatus_Object = MibTableColumn
futRMTeLinkSwDescrRowStatus = _FutRMTeLinkSwDescrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 72, 10, 1, 3, 1, 7),
    _FutRMTeLinkSwDescrRowStatus_Type()
)
futRMTeLinkSwDescrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    futRMTeLinkSwDescrRowStatus.setStatus("current")
_FutRMTeLinkSwDescrMaxBwTable_Object = MibTable
futRMTeLinkSwDescrMaxBwTable = _FutRMTeLinkSwDescrMaxBwTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 72, 10, 1, 4)
)
if mibBuilder.loadTexts:
    futRMTeLinkSwDescrMaxBwTable.setStatus("current")
_FutRMTeLinkSwDescrMaxBwEntry_Object = MibTableRow
futRMTeLinkSwDescrMaxBwEntry = _FutRMTeLinkSwDescrMaxBwEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 72, 10, 1, 4, 1)
)
futRMTeLinkSwDescrMaxBwEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ARICENT-RM-TE-LINK-MIB", "futRMTeLinkSwDescriptorId"),
    (0, "ARICENT-RM-TE-LINK-MIB", "futRMTeLinkSwDescrMaxBwPriority"),
)
if mibBuilder.loadTexts:
    futRMTeLinkSwDescrMaxBwEntry.setStatus("current")
_FutRMTeLinkSwDescrMaxBwPriority_Type = TeLinkPriority
_FutRMTeLinkSwDescrMaxBwPriority_Object = MibTableColumn
futRMTeLinkSwDescrMaxBwPriority = _FutRMTeLinkSwDescrMaxBwPriority_Object(
    (1, 3, 6, 1, 4, 1, 2076, 72, 10, 1, 4, 1, 1),
    _FutRMTeLinkSwDescrMaxBwPriority_Type()
)
futRMTeLinkSwDescrMaxBwPriority.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    futRMTeLinkSwDescrMaxBwPriority.setStatus("current")
_FutRMTeLinkSwDescrMaxLSPBandwidth_Type = Unsigned32
_FutRMTeLinkSwDescrMaxLSPBandwidth_Object = MibTableColumn
futRMTeLinkSwDescrMaxLSPBandwidth = _FutRMTeLinkSwDescrMaxLSPBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 2076, 72, 10, 1, 4, 1, 2),
    _FutRMTeLinkSwDescrMaxLSPBandwidth_Type()
)
futRMTeLinkSwDescrMaxLSPBandwidth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    futRMTeLinkSwDescrMaxLSPBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    futRMTeLinkSwDescrMaxLSPBandwidth.setUnits("bytes per second")
_FutRMTeLinkSwDescrMaxBwRowStatus_Type = RowStatus
_FutRMTeLinkSwDescrMaxBwRowStatus_Object = MibTableColumn
futRMTeLinkSwDescrMaxBwRowStatus = _FutRMTeLinkSwDescrMaxBwRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 72, 10, 1, 4, 1, 3),
    _FutRMTeLinkSwDescrMaxBwRowStatus_Type()
)
futRMTeLinkSwDescrMaxBwRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    futRMTeLinkSwDescrMaxBwRowStatus.setStatus("current")
_FutRMTeLinkSrlgTable_Object = MibTable
futRMTeLinkSrlgTable = _FutRMTeLinkSrlgTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 72, 10, 1, 5)
)
if mibBuilder.loadTexts:
    futRMTeLinkSrlgTable.setStatus("current")
_FutRMTeLinkSrlgEntry_Object = MibTableRow
futRMTeLinkSrlgEntry = _FutRMTeLinkSrlgEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 72, 10, 1, 5, 1)
)
futRMTeLinkSrlgEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ARICENT-RM-TE-LINK-MIB", "futRMTeLinkSrlg"),
)
if mibBuilder.loadTexts:
    futRMTeLinkSrlgEntry.setStatus("current")


class _FutRMTeLinkSrlg_Type(Unsigned32):
    """Custom type futRMTeLinkSrlg based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FutRMTeLinkSrlg_Type.__name__ = "Unsigned32"
_FutRMTeLinkSrlg_Object = MibTableColumn
futRMTeLinkSrlg = _FutRMTeLinkSrlg_Object(
    (1, 3, 6, 1, 4, 1, 2076, 72, 10, 1, 5, 1, 1),
    _FutRMTeLinkSrlg_Type()
)
futRMTeLinkSrlg.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    futRMTeLinkSrlg.setStatus("current")
_FutRMTeLinkSrlgRowStatus_Type = RowStatus
_FutRMTeLinkSrlgRowStatus_Object = MibTableColumn
futRMTeLinkSrlgRowStatus = _FutRMTeLinkSrlgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 72, 10, 1, 5, 1, 2),
    _FutRMTeLinkSrlgRowStatus_Type()
)
futRMTeLinkSrlgRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    futRMTeLinkSrlgRowStatus.setStatus("current")
_FutRMTeLinkBandwidthTable_Object = MibTable
futRMTeLinkBandwidthTable = _FutRMTeLinkBandwidthTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 72, 10, 1, 6)
)
if mibBuilder.loadTexts:
    futRMTeLinkBandwidthTable.setStatus("current")
_FutRMTeLinkBandwidthEntry_Object = MibTableRow
futRMTeLinkBandwidthEntry = _FutRMTeLinkBandwidthEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 72, 10, 1, 6, 1)
)
futRMTeLinkBandwidthEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ARICENT-RM-TE-LINK-MIB", "futRMTeLinkBandwidthPriority"),
)
if mibBuilder.loadTexts:
    futRMTeLinkBandwidthEntry.setStatus("current")
_FutRMTeLinkBandwidthPriority_Type = TeLinkPriority
_FutRMTeLinkBandwidthPriority_Object = MibTableColumn
futRMTeLinkBandwidthPriority = _FutRMTeLinkBandwidthPriority_Object(
    (1, 3, 6, 1, 4, 1, 2076, 72, 10, 1, 6, 1, 1),
    _FutRMTeLinkBandwidthPriority_Type()
)
futRMTeLinkBandwidthPriority.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    futRMTeLinkBandwidthPriority.setStatus("current")
_FutRMTeLinkUnreservedBandwidth_Type = Unsigned32
_FutRMTeLinkUnreservedBandwidth_Object = MibTableColumn
futRMTeLinkUnreservedBandwidth = _FutRMTeLinkUnreservedBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 2076, 72, 10, 1, 6, 1, 2),
    _FutRMTeLinkUnreservedBandwidth_Type()
)
futRMTeLinkUnreservedBandwidth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    futRMTeLinkUnreservedBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    futRMTeLinkUnreservedBandwidth.setUnits("bytes per second")
_FutRMTeLinkBandwidthRowStatus_Type = RowStatus
_FutRMTeLinkBandwidthRowStatus_Object = MibTableColumn
futRMTeLinkBandwidthRowStatus = _FutRMTeLinkBandwidthRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 72, 10, 1, 6, 1, 3),
    _FutRMTeLinkBandwidthRowStatus_Type()
)
futRMTeLinkBandwidthRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    futRMTeLinkBandwidthRowStatus.setStatus("current")
_FutRMTeLinkConformance_ObjectIdentity = ObjectIdentity
futRMTeLinkConformance = _FutRMTeLinkConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 72, 10, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ARICENT-RM-TE-LINK-MIB",
    **{"TeLinkPriority": TeLinkPriority,
       "TeLinkEncodingType": TeLinkEncodingType,
       "futRMTe": futRMTe,
       "futRMTeLinkNotifications": futRMTeLinkNotifications,
       "futRMTeLinkObjects": futRMTeLinkObjects,
       "futRmTeLinkGeneralGroup": futRmTeLinkGeneralGroup,
       "futRmTeLinkRegDeregistration": futRmTeLinkRegDeregistration,
       "futRMTeLinkTable": futRMTeLinkTable,
       "futRMTeLinkEntry": futRMTeLinkEntry,
       "futRMTeLinkLocalIpAddr": futRMTeLinkLocalIpAddr,
       "futRMTeLinkRemoteIpAddr": futRMTeLinkRemoteIpAddr,
       "futRMTeLinkRemoteRtrId": futRMTeLinkRemoteRtrId,
       "futRMTeLinkMetric": futRMTeLinkMetric,
       "futRMTeLinkProtectionType": futRMTeLinkProtectionType,
       "futRMTeLinkResourceClass": futRMTeLinkResourceClass,
       "futRMTeLinkIncomingIfId": futRMTeLinkIncomingIfId,
       "futRMTeLinkOutgoingIfId": futRMTeLinkOutgoingIfId,
       "futRMTeLinkMaxBw": futRMTeLinkMaxBw,
       "futRMTeLinkMaxResBw": futRMTeLinkMaxResBw,
       "futRMTeLinkAreaId": futRMTeLinkAreaId,
       "futRMTeLinkInfoType": futRMTeLinkInfoType,
       "futRMTeLinkRowStatus": futRMTeLinkRowStatus,
       "futRMTeLinkSwDescriptorTable": futRMTeLinkSwDescriptorTable,
       "futRMTeLinkSwDescriptorEntry": futRMTeLinkSwDescriptorEntry,
       "futRMTeLinkSwDescriptorId": futRMTeLinkSwDescriptorId,
       "futRMTeLinkSwDescrSwitchingCap": futRMTeLinkSwDescrSwitchingCap,
       "futRMTeLinkSwDescrEncodingType": futRMTeLinkSwDescrEncodingType,
       "futRMTeLinkSwDescrMinLSPBandwidth": futRMTeLinkSwDescrMinLSPBandwidth,
       "futRMTeLinkSwDescrMTU": futRMTeLinkSwDescrMTU,
       "futRMTeLinkSwDescrIndication": futRMTeLinkSwDescrIndication,
       "futRMTeLinkSwDescrRowStatus": futRMTeLinkSwDescrRowStatus,
       "futRMTeLinkSwDescrMaxBwTable": futRMTeLinkSwDescrMaxBwTable,
       "futRMTeLinkSwDescrMaxBwEntry": futRMTeLinkSwDescrMaxBwEntry,
       "futRMTeLinkSwDescrMaxBwPriority": futRMTeLinkSwDescrMaxBwPriority,
       "futRMTeLinkSwDescrMaxLSPBandwidth": futRMTeLinkSwDescrMaxLSPBandwidth,
       "futRMTeLinkSwDescrMaxBwRowStatus": futRMTeLinkSwDescrMaxBwRowStatus,
       "futRMTeLinkSrlgTable": futRMTeLinkSrlgTable,
       "futRMTeLinkSrlgEntry": futRMTeLinkSrlgEntry,
       "futRMTeLinkSrlg": futRMTeLinkSrlg,
       "futRMTeLinkSrlgRowStatus": futRMTeLinkSrlgRowStatus,
       "futRMTeLinkBandwidthTable": futRMTeLinkBandwidthTable,
       "futRMTeLinkBandwidthEntry": futRMTeLinkBandwidthEntry,
       "futRMTeLinkBandwidthPriority": futRMTeLinkBandwidthPriority,
       "futRMTeLinkUnreservedBandwidth": futRMTeLinkUnreservedBandwidth,
       "futRMTeLinkBandwidthRowStatus": futRMTeLinkBandwidthRowStatus,
       "futRMTeLinkConformance": futRMTeLinkConformance}
)
