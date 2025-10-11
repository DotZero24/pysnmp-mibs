# SNMP MIB module (COLUBRIS-DEVICE-WDS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/colubris/COLUBRIS-DEVICE-WDS-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:29:32 2025
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

(coDevDisIndex,) = mibBuilder.importSymbols(
    "COLUBRIS-DEVICE-MIB",
    "coDevDisIndex")

(colubrisMgmtV2,) = mibBuilder.importSymbols(
    "COLUBRIS-SMI",
    "colubrisMgmtV2")

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
 MacAddress,
 PhysAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

colubrisDeviceWdsMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 5, 34)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ColubrisDeviceWdsMIBObjects_ObjectIdentity = ObjectIdentity
colubrisDeviceWdsMIBObjects = _ColubrisDeviceWdsMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 5, 34, 1)
)
_CoDeviceWDSInfoGroup_ObjectIdentity = ObjectIdentity
coDeviceWDSInfoGroup = _CoDeviceWDSInfoGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 2)
)
_CoDeviceWdsInfoTable_Object = MibTable
coDeviceWdsInfoTable = _CoDeviceWdsInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 2, 1)
)
if mibBuilder.loadTexts:
    coDeviceWdsInfoTable.setStatus("current")
_CoDeviceWdsInfoEntry_Object = MibTableRow
coDeviceWdsInfoEntry = _CoDeviceWdsInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 2, 1, 1)
)
coDeviceWdsInfoEntry.setIndexNames(
    (0, "COLUBRIS-DEVICE-MIB", "coDevDisIndex"),
)
if mibBuilder.loadTexts:
    coDeviceWdsInfoEntry.setStatus("current")


class _CoDevWDSInfoMaxNumberOfGroup_Type(Unsigned32):
    """Custom type coDevWDSInfoMaxNumberOfGroup based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_CoDevWDSInfoMaxNumberOfGroup_Type.__name__ = "Unsigned32"
_CoDevWDSInfoMaxNumberOfGroup_Object = MibTableColumn
coDevWDSInfoMaxNumberOfGroup = _CoDevWDSInfoMaxNumberOfGroup_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 2, 1, 1, 1),
    _CoDevWDSInfoMaxNumberOfGroup_Type()
)
coDevWDSInfoMaxNumberOfGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWDSInfoMaxNumberOfGroup.setStatus("current")
_CoDeviceWDSRadioGroup_ObjectIdentity = ObjectIdentity
coDeviceWDSRadioGroup = _CoDeviceWDSRadioGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 3)
)
_CoDeviceWDSRadioTable_Object = MibTable
coDeviceWDSRadioTable = _CoDeviceWDSRadioTable_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 3, 1)
)
if mibBuilder.loadTexts:
    coDeviceWDSRadioTable.setStatus("current")
_CoDeviceWDSRadioEntry_Object = MibTableRow
coDeviceWDSRadioEntry = _CoDeviceWDSRadioEntry_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 3, 1, 1)
)
coDeviceWDSRadioEntry.setIndexNames(
    (0, "COLUBRIS-DEVICE-MIB", "coDevDisIndex"),
    (0, "COLUBRIS-DEVICE-WDS-MIB", "coDevWDSRadioIndex"),
)
if mibBuilder.loadTexts:
    coDeviceWDSRadioEntry.setStatus("current")


class _CoDevWDSRadioIndex_Type(Integer32):
    """Custom type coDevWDSRadioIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_CoDevWDSRadioIndex_Type.__name__ = "Integer32"
_CoDevWDSRadioIndex_Object = MibTableColumn
coDevWDSRadioIndex = _CoDevWDSRadioIndex_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 3, 1, 1, 1),
    _CoDevWDSRadioIndex_Type()
)
coDevWDSRadioIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    coDevWDSRadioIndex.setStatus("current")
_CoDevWDSRadioAckDistance_Type = Unsigned32
_CoDevWDSRadioAckDistance_Object = MibTableColumn
coDevWDSRadioAckDistance = _CoDevWDSRadioAckDistance_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 3, 1, 1, 2),
    _CoDevWDSRadioAckDistance_Type()
)
coDevWDSRadioAckDistance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWDSRadioAckDistance.setStatus("current")
if mibBuilder.loadTexts:
    coDevWDSRadioAckDistance.setUnits("km")


class _CoDevWDSRadioQoS_Type(Integer32):
    """Custom type coDevWDSRadioQoS based on Integer32"""
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
        *(("disabled", 1),
          ("vlan", 2),
          ("veryHigh", 3),
          ("high", 4),
          ("normal", 5),
          ("low", 6),
          ("diffSrv", 7),
          ("tos", 8),
          ("ipQos", 9))
    )


_CoDevWDSRadioQoS_Type.__name__ = "Integer32"
_CoDevWDSRadioQoS_Object = MibTableColumn
coDevWDSRadioQoS = _CoDevWDSRadioQoS_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 3, 1, 1, 3),
    _CoDevWDSRadioQoS_Type()
)
coDevWDSRadioQoS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWDSRadioQoS.setStatus("current")
_CoDeviceWDSGroupGroup_ObjectIdentity = ObjectIdentity
coDeviceWDSGroupGroup = _CoDeviceWDSGroupGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 4)
)
_CoDeviceWDSGroupTable_Object = MibTable
coDeviceWDSGroupTable = _CoDeviceWDSGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 4, 1)
)
if mibBuilder.loadTexts:
    coDeviceWDSGroupTable.setStatus("current")
_CoDeviceWDSGroupEntry_Object = MibTableRow
coDeviceWDSGroupEntry = _CoDeviceWDSGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 4, 1, 1)
)
coDeviceWDSGroupEntry.setIndexNames(
    (0, "COLUBRIS-DEVICE-MIB", "coDevDisIndex"),
    (0, "COLUBRIS-DEVICE-WDS-MIB", "coDevWDSGroupIndex"),
)
if mibBuilder.loadTexts:
    coDeviceWDSGroupEntry.setStatus("current")


class _CoDevWDSGroupIndex_Type(Integer32):
    """Custom type coDevWDSGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9),
    )


_CoDevWDSGroupIndex_Type.__name__ = "Integer32"
_CoDevWDSGroupIndex_Object = MibTableColumn
coDevWDSGroupIndex = _CoDevWDSGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 4, 1, 1, 1),
    _CoDevWDSGroupIndex_Type()
)
coDevWDSGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    coDevWDSGroupIndex.setStatus("current")


class _CoDevWDSGroupName_Type(DisplayString):
    """Custom type coDevWDSGroupName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CoDevWDSGroupName_Type.__name__ = "DisplayString"
_CoDevWDSGroupName_Object = MibTableColumn
coDevWDSGroupName = _CoDevWDSGroupName_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 4, 1, 1, 2),
    _CoDevWDSGroupName_Type()
)
coDevWDSGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWDSGroupName.setStatus("current")


class _CoDevWDSGroupState_Type(Integer32):
    """Custom type coDevWDSGroupState based on Integer32"""
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
        *(("discovery", 1),
          ("negotiation", 2),
          ("acquisition", 3),
          ("locked", 4),
          ("shutdown", 5))
    )


_CoDevWDSGroupState_Type.__name__ = "Integer32"
_CoDevWDSGroupState_Object = MibTableColumn
coDevWDSGroupState = _CoDevWDSGroupState_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 4, 1, 1, 3),
    _CoDevWDSGroupState_Type()
)
coDevWDSGroupState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWDSGroupState.setStatus("current")


class _CoDevWDSGroupSecurity_Type(Integer32):
    """Custom type coDevWDSGroupSecurity based on Integer32"""
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
        *(("none", 1),
          ("wep", 2),
          ("tkip", 3),
          ("aes", 4))
    )


_CoDevWDSGroupSecurity_Type.__name__ = "Integer32"
_CoDevWDSGroupSecurity_Object = MibTableColumn
coDevWDSGroupSecurity = _CoDevWDSGroupSecurity_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 4, 1, 1, 4),
    _CoDevWDSGroupSecurity_Type()
)
coDevWDSGroupSecurity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWDSGroupSecurity.setStatus("current")


class _CoDevWDSGroupDynamicMode_Type(Integer32):
    """Custom type coDevWDSGroupDynamicMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("master", 1),
          ("slave", 2),
          ("alternateMaster", 3))
    )


_CoDevWDSGroupDynamicMode_Type.__name__ = "Integer32"
_CoDevWDSGroupDynamicMode_Object = MibTableColumn
coDevWDSGroupDynamicMode = _CoDevWDSGroupDynamicMode_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 4, 1, 1, 5),
    _CoDevWDSGroupDynamicMode_Type()
)
coDevWDSGroupDynamicMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWDSGroupDynamicMode.setStatus("current")
_CoDevWDSGroupDynamicGroupId_Type = Unsigned32
_CoDevWDSGroupDynamicGroupId_Object = MibTableColumn
coDevWDSGroupDynamicGroupId = _CoDevWDSGroupDynamicGroupId_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 4, 1, 1, 6),
    _CoDevWDSGroupDynamicGroupId_Type()
)
coDevWDSGroupDynamicGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWDSGroupDynamicGroupId.setStatus("current")
_CoDeviceWDSLinkGroup_ObjectIdentity = ObjectIdentity
coDeviceWDSLinkGroup = _CoDeviceWDSLinkGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 5)
)
_CoDeviceWDSLinkStatusTable_Object = MibTable
coDeviceWDSLinkStatusTable = _CoDeviceWDSLinkStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 5, 1)
)
if mibBuilder.loadTexts:
    coDeviceWDSLinkStatusTable.setStatus("current")
_CoDeviceWDSLinkStatusEntry_Object = MibTableRow
coDeviceWDSLinkStatusEntry = _CoDeviceWDSLinkStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 5, 1, 1)
)
coDeviceWDSLinkStatusEntry.setIndexNames(
    (0, "COLUBRIS-DEVICE-MIB", "coDevDisIndex"),
    (0, "COLUBRIS-DEVICE-WDS-MIB", "coDevWDSGroupIndex"),
    (0, "COLUBRIS-DEVICE-WDS-MIB", "coDevWDSLinkStaIndex"),
)
if mibBuilder.loadTexts:
    coDeviceWDSLinkStatusEntry.setStatus("current")


class _CoDevWDSLinkStaIndex_Type(Integer32):
    """Custom type coDevWDSLinkStaIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CoDevWDSLinkStaIndex_Type.__name__ = "Integer32"
_CoDevWDSLinkStaIndex_Object = MibTableColumn
coDevWDSLinkStaIndex = _CoDevWDSLinkStaIndex_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 5, 1, 1, 1),
    _CoDevWDSLinkStaIndex_Type()
)
coDevWDSLinkStaIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    coDevWDSLinkStaIndex.setStatus("current")


class _CoDevWDSLinkStaState_Type(Integer32):
    """Custom type coDevWDSLinkStaState based on Integer32"""
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
        *(("down", 1),
          ("acquiring", 2),
          ("inactive", 3),
          ("active", 4))
    )


_CoDevWDSLinkStaState_Type.__name__ = "Integer32"
_CoDevWDSLinkStaState_Object = MibTableColumn
coDevWDSLinkStaState = _CoDevWDSLinkStaState_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 5, 1, 1, 2),
    _CoDevWDSLinkStaState_Type()
)
coDevWDSLinkStaState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWDSLinkStaState.setStatus("current")


class _CoDevWDSLinkStaRadio_Type(Integer32):
    """Custom type coDevWDSLinkStaRadio based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_CoDevWDSLinkStaRadio_Type.__name__ = "Integer32"
_CoDevWDSLinkStaRadio_Object = MibTableColumn
coDevWDSLinkStaRadio = _CoDevWDSLinkStaRadio_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 5, 1, 1, 3),
    _CoDevWDSLinkStaRadio_Type()
)
coDevWDSLinkStaRadio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWDSLinkStaRadio.setStatus("current")
_CoDevWDSLinkStaPeerMacAddress_Type = MacAddress
_CoDevWDSLinkStaPeerMacAddress_Object = MibTableColumn
coDevWDSLinkStaPeerMacAddress = _CoDevWDSLinkStaPeerMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 5, 1, 1, 4),
    _CoDevWDSLinkStaPeerMacAddress_Type()
)
coDevWDSLinkStaPeerMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWDSLinkStaPeerMacAddress.setStatus("current")
_CoDevWDSLinkStaMaster_Type = TruthValue
_CoDevWDSLinkStaMaster_Object = MibTableColumn
coDevWDSLinkStaMaster = _CoDevWDSLinkStaMaster_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 5, 1, 1, 5),
    _CoDevWDSLinkStaMaster_Type()
)
coDevWDSLinkStaMaster.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWDSLinkStaMaster.setStatus("current")
_CoDevWDSLinkStaAuthorized_Type = TruthValue
_CoDevWDSLinkStaAuthorized_Object = MibTableColumn
coDevWDSLinkStaAuthorized = _CoDevWDSLinkStaAuthorized_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 5, 1, 1, 6),
    _CoDevWDSLinkStaAuthorized_Type()
)
coDevWDSLinkStaAuthorized.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWDSLinkStaAuthorized.setStatus("current")


class _CoDevWDSLinkStaEncryption_Type(Integer32):
    """Custom type coDevWDSLinkStaEncryption based on Integer32"""
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
        *(("none", 1),
          ("wep", 2),
          ("tkip", 3),
          ("aes", 4))
    )


_CoDevWDSLinkStaEncryption_Type.__name__ = "Integer32"
_CoDevWDSLinkStaEncryption_Object = MibTableColumn
coDevWDSLinkStaEncryption = _CoDevWDSLinkStaEncryption_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 5, 1, 1, 7),
    _CoDevWDSLinkStaEncryption_Type()
)
coDevWDSLinkStaEncryption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWDSLinkStaEncryption.setStatus("current")
_CoDevWDSLinkStaIdleTime_Type = Unsigned32
_CoDevWDSLinkStaIdleTime_Object = MibTableColumn
coDevWDSLinkStaIdleTime = _CoDevWDSLinkStaIdleTime_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 5, 1, 1, 8),
    _CoDevWDSLinkStaIdleTime_Type()
)
coDevWDSLinkStaIdleTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWDSLinkStaIdleTime.setStatus("current")
if mibBuilder.loadTexts:
    coDevWDSLinkStaIdleTime.setUnits("seconds")


class _CoDevWDSLinkStaSNR_Type(Integer32):
    """Custom type coDevWDSLinkStaSNR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 92),
    )


_CoDevWDSLinkStaSNR_Type.__name__ = "Integer32"
_CoDevWDSLinkStaSNR_Object = MibTableColumn
coDevWDSLinkStaSNR = _CoDevWDSLinkStaSNR_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 5, 1, 1, 9),
    _CoDevWDSLinkStaSNR_Type()
)
coDevWDSLinkStaSNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWDSLinkStaSNR.setStatus("current")
if mibBuilder.loadTexts:
    coDevWDSLinkStaSNR.setUnits("dBm")
_CoDevWDSLinkStaTxRate_Type = Unsigned32
_CoDevWDSLinkStaTxRate_Object = MibTableColumn
coDevWDSLinkStaTxRate = _CoDevWDSLinkStaTxRate_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 5, 1, 1, 10),
    _CoDevWDSLinkStaTxRate_Type()
)
coDevWDSLinkStaTxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWDSLinkStaTxRate.setStatus("current")
if mibBuilder.loadTexts:
    coDevWDSLinkStaTxRate.setUnits("500Kb/s")
_CoDevWDSLinkStaRxRate_Type = Unsigned32
_CoDevWDSLinkStaRxRate_Object = MibTableColumn
coDevWDSLinkStaRxRate = _CoDevWDSLinkStaRxRate_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 5, 1, 1, 11),
    _CoDevWDSLinkStaRxRate_Type()
)
coDevWDSLinkStaRxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWDSLinkStaRxRate.setStatus("current")
if mibBuilder.loadTexts:
    coDevWDSLinkStaRxRate.setUnits("500Kb/s")


class _CoDevWDSLinkStaIfIndex_Type(Integer32):
    """Custom type coDevWDSLinkStaIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CoDevWDSLinkStaIfIndex_Type.__name__ = "Integer32"
_CoDevWDSLinkStaIfIndex_Object = MibTableColumn
coDevWDSLinkStaIfIndex = _CoDevWDSLinkStaIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 5, 1, 1, 12),
    _CoDevWDSLinkStaIfIndex_Type()
)
coDevWDSLinkStaIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWDSLinkStaIfIndex.setStatus("current")
_CoDevWDSLinkStaHT_Type = TruthValue
_CoDevWDSLinkStaHT_Object = MibTableColumn
coDevWDSLinkStaHT = _CoDevWDSLinkStaHT_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 5, 1, 1, 13),
    _CoDevWDSLinkStaHT_Type()
)
coDevWDSLinkStaHT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWDSLinkStaHT.setStatus("current")
_CoDevWDSLinkStaTxMCS_Type = Unsigned32
_CoDevWDSLinkStaTxMCS_Object = MibTableColumn
coDevWDSLinkStaTxMCS = _CoDevWDSLinkStaTxMCS_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 5, 1, 1, 14),
    _CoDevWDSLinkStaTxMCS_Type()
)
coDevWDSLinkStaTxMCS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWDSLinkStaTxMCS.setStatus("current")
_CoDevWDSLinkStaRxMCS_Type = Unsigned32
_CoDevWDSLinkStaRxMCS_Object = MibTableColumn
coDevWDSLinkStaRxMCS = _CoDevWDSLinkStaRxMCS_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 5, 1, 1, 15),
    _CoDevWDSLinkStaRxMCS_Type()
)
coDevWDSLinkStaRxMCS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWDSLinkStaRxMCS.setStatus("current")
_CoDevWDSLinkStaSignal_Type = Integer32
_CoDevWDSLinkStaSignal_Object = MibTableColumn
coDevWDSLinkStaSignal = _CoDevWDSLinkStaSignal_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 5, 1, 1, 16),
    _CoDevWDSLinkStaSignal_Type()
)
coDevWDSLinkStaSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWDSLinkStaSignal.setStatus("current")
if mibBuilder.loadTexts:
    coDevWDSLinkStaSignal.setUnits("dBm")
_CoDevWDSLinkStaNoise_Type = Integer32
_CoDevWDSLinkStaNoise_Object = MibTableColumn
coDevWDSLinkStaNoise = _CoDevWDSLinkStaNoise_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 5, 1, 1, 17),
    _CoDevWDSLinkStaNoise_Type()
)
coDevWDSLinkStaNoise.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWDSLinkStaNoise.setStatus("current")
if mibBuilder.loadTexts:
    coDevWDSLinkStaNoise.setUnits("dBm")
_CoDevWDSLinkStaVHT_Type = TruthValue
_CoDevWDSLinkStaVHT_Object = MibTableColumn
coDevWDSLinkStaVHT = _CoDevWDSLinkStaVHT_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 5, 1, 1, 18),
    _CoDevWDSLinkStaVHT_Type()
)
coDevWDSLinkStaVHT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWDSLinkStaVHT.setStatus("current")
_CoDeviceWDSLinkStatsRatesTable_Object = MibTable
coDeviceWDSLinkStatsRatesTable = _CoDeviceWDSLinkStatsRatesTable_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 5, 2)
)
if mibBuilder.loadTexts:
    coDeviceWDSLinkStatsRatesTable.setStatus("current")
_CoDeviceWDSLinkStatsRatesEntry_Object = MibTableRow
coDeviceWDSLinkStatsRatesEntry = _CoDeviceWDSLinkStatsRatesEntry_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 5, 2, 1)
)
if mibBuilder.loadTexts:
    coDeviceWDSLinkStatsRatesEntry.setStatus("current")
_CoDevWDSLinkStsPktsTxRate1_Type = Counter32
_CoDevWDSLinkStsPktsTxRate1_Object = MibTableColumn
coDevWDSLinkStsPktsTxRate1 = _CoDevWDSLinkStsPktsTxRate1_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 5, 2, 1, 1),
    _CoDevWDSLinkStsPktsTxRate1_Type()
)
coDevWDSLinkStsPktsTxRate1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWDSLinkStsPktsTxRate1.setStatus("current")
_CoDevWDSLinkStsPktsTxRate2_Type = Counter32
_CoDevWDSLinkStsPktsTxRate2_Object = MibTableColumn
coDevWDSLinkStsPktsTxRate2 = _CoDevWDSLinkStsPktsTxRate2_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 5, 2, 1, 2),
    _CoDevWDSLinkStsPktsTxRate2_Type()
)
coDevWDSLinkStsPktsTxRate2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWDSLinkStsPktsTxRate2.setStatus("current")
_CoDevWDSLinkStsPktsTxRate5dot5_Type = Counter32
_CoDevWDSLinkStsPktsTxRate5dot5_Object = MibTableColumn
coDevWDSLinkStsPktsTxRate5dot5 = _CoDevWDSLinkStsPktsTxRate5dot5_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 5, 2, 1, 3),
    _CoDevWDSLinkStsPktsTxRate5dot5_Type()
)
coDevWDSLinkStsPktsTxRate5dot5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWDSLinkStsPktsTxRate5dot5.setStatus("current")
_CoDevWDSLinkStsPktsTxRate11_Type = Counter32
_CoDevWDSLinkStsPktsTxRate11_Object = MibTableColumn
coDevWDSLinkStsPktsTxRate11 = _CoDevWDSLinkStsPktsTxRate11_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 5, 2, 1, 4),
    _CoDevWDSLinkStsPktsTxRate11_Type()
)
coDevWDSLinkStsPktsTxRate11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWDSLinkStsPktsTxRate11.setStatus("current")
_CoDevWDSLinkStsPktsTxRate6_Type = Counter32
_CoDevWDSLinkStsPktsTxRate6_Object = MibTableColumn
coDevWDSLinkStsPktsTxRate6 = _CoDevWDSLinkStsPktsTxRate6_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 5, 2, 1, 5),
    _CoDevWDSLinkStsPktsTxRate6_Type()
)
coDevWDSLinkStsPktsTxRate6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWDSLinkStsPktsTxRate6.setStatus("current")
_CoDevWDSLinkStsPktsTxRate9_Type = Counter32
_CoDevWDSLinkStsPktsTxRate9_Object = MibTableColumn
coDevWDSLinkStsPktsTxRate9 = _CoDevWDSLinkStsPktsTxRate9_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 5, 2, 1, 6),
    _CoDevWDSLinkStsPktsTxRate9_Type()
)
coDevWDSLinkStsPktsTxRate9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWDSLinkStsPktsTxRate9.setStatus("current")
_CoDevWDSLinkStsPktsTxRate12_Type = Counter32
_CoDevWDSLinkStsPktsTxRate12_Object = MibTableColumn
coDevWDSLinkStsPktsTxRate12 = _CoDevWDSLinkStsPktsTxRate12_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 5, 2, 1, 7),
    _CoDevWDSLinkStsPktsTxRate12_Type()
)
coDevWDSLinkStsPktsTxRate12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWDSLinkStsPktsTxRate12.setStatus("current")
_CoDevWDSLinkStsPktsTxRate18_Type = Counter32
_CoDevWDSLinkStsPktsTxRate18_Object = MibTableColumn
coDevWDSLinkStsPktsTxRate18 = _CoDevWDSLinkStsPktsTxRate18_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 5, 2, 1, 8),
    _CoDevWDSLinkStsPktsTxRate18_Type()
)
coDevWDSLinkStsPktsTxRate18.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWDSLinkStsPktsTxRate18.setStatus("current")
_CoDevWDSLinkStsPktsTxRate24_Type = Counter32
_CoDevWDSLinkStsPktsTxRate24_Object = MibTableColumn
coDevWDSLinkStsPktsTxRate24 = _CoDevWDSLinkStsPktsTxRate24_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 5, 2, 1, 9),
    _CoDevWDSLinkStsPktsTxRate24_Type()
)
coDevWDSLinkStsPktsTxRate24.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWDSLinkStsPktsTxRate24.setStatus("current")
_CoDevWDSLinkStsPktsTxRate36_Type = Counter32
_CoDevWDSLinkStsPktsTxRate36_Object = MibTableColumn
coDevWDSLinkStsPktsTxRate36 = _CoDevWDSLinkStsPktsTxRate36_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 5, 2, 1, 10),
    _CoDevWDSLinkStsPktsTxRate36_Type()
)
coDevWDSLinkStsPktsTxRate36.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWDSLinkStsPktsTxRate36.setStatus("current")
_CoDevWDSLinkStsPktsTxRate48_Type = Counter32
_CoDevWDSLinkStsPktsTxRate48_Object = MibTableColumn
coDevWDSLinkStsPktsTxRate48 = _CoDevWDSLinkStsPktsTxRate48_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 5, 2, 1, 11),
    _CoDevWDSLinkStsPktsTxRate48_Type()
)
coDevWDSLinkStsPktsTxRate48.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWDSLinkStsPktsTxRate48.setStatus("current")
_CoDevWDSLinkStsPktsTxRate54_Type = Counter32
_CoDevWDSLinkStsPktsTxRate54_Object = MibTableColumn
coDevWDSLinkStsPktsTxRate54 = _CoDevWDSLinkStsPktsTxRate54_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 5, 2, 1, 12),
    _CoDevWDSLinkStsPktsTxRate54_Type()
)
coDevWDSLinkStsPktsTxRate54.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWDSLinkStsPktsTxRate54.setStatus("current")
_CoDevWDSLinkStsPktsRxRate1_Type = Counter32
_CoDevWDSLinkStsPktsRxRate1_Object = MibTableColumn
coDevWDSLinkStsPktsRxRate1 = _CoDevWDSLinkStsPktsRxRate1_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 5, 2, 1, 13),
    _CoDevWDSLinkStsPktsRxRate1_Type()
)
coDevWDSLinkStsPktsRxRate1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWDSLinkStsPktsRxRate1.setStatus("current")
_CoDevWDSLinkStsPktsRxRate2_Type = Counter32
_CoDevWDSLinkStsPktsRxRate2_Object = MibTableColumn
coDevWDSLinkStsPktsRxRate2 = _CoDevWDSLinkStsPktsRxRate2_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 5, 2, 1, 14),
    _CoDevWDSLinkStsPktsRxRate2_Type()
)
coDevWDSLinkStsPktsRxRate2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWDSLinkStsPktsRxRate2.setStatus("current")
_CoDevWDSLinkStsPktsRxRate5dot5_Type = Counter32
_CoDevWDSLinkStsPktsRxRate5dot5_Object = MibTableColumn
coDevWDSLinkStsPktsRxRate5dot5 = _CoDevWDSLinkStsPktsRxRate5dot5_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 5, 2, 1, 15),
    _CoDevWDSLinkStsPktsRxRate5dot5_Type()
)
coDevWDSLinkStsPktsRxRate5dot5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWDSLinkStsPktsRxRate5dot5.setStatus("current")
_CoDevWDSLinkStsPktsRxRate11_Type = Counter32
_CoDevWDSLinkStsPktsRxRate11_Object = MibTableColumn
coDevWDSLinkStsPktsRxRate11 = _CoDevWDSLinkStsPktsRxRate11_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 5, 2, 1, 16),
    _CoDevWDSLinkStsPktsRxRate11_Type()
)
coDevWDSLinkStsPktsRxRate11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWDSLinkStsPktsRxRate11.setStatus("current")
_CoDevWDSLinkStsPktsRxRate6_Type = Counter32
_CoDevWDSLinkStsPktsRxRate6_Object = MibTableColumn
coDevWDSLinkStsPktsRxRate6 = _CoDevWDSLinkStsPktsRxRate6_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 5, 2, 1, 17),
    _CoDevWDSLinkStsPktsRxRate6_Type()
)
coDevWDSLinkStsPktsRxRate6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWDSLinkStsPktsRxRate6.setStatus("current")
_CoDevWDSLinkStsPktsRxRate9_Type = Counter32
_CoDevWDSLinkStsPktsRxRate9_Object = MibTableColumn
coDevWDSLinkStsPktsRxRate9 = _CoDevWDSLinkStsPktsRxRate9_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 5, 2, 1, 18),
    _CoDevWDSLinkStsPktsRxRate9_Type()
)
coDevWDSLinkStsPktsRxRate9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWDSLinkStsPktsRxRate9.setStatus("current")
_CoDevWDSLinkStsPktsRxRate12_Type = Counter32
_CoDevWDSLinkStsPktsRxRate12_Object = MibTableColumn
coDevWDSLinkStsPktsRxRate12 = _CoDevWDSLinkStsPktsRxRate12_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 5, 2, 1, 19),
    _CoDevWDSLinkStsPktsRxRate12_Type()
)
coDevWDSLinkStsPktsRxRate12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWDSLinkStsPktsRxRate12.setStatus("current")
_CoDevWDSLinkStsPktsRxRate18_Type = Counter32
_CoDevWDSLinkStsPktsRxRate18_Object = MibTableColumn
coDevWDSLinkStsPktsRxRate18 = _CoDevWDSLinkStsPktsRxRate18_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 5, 2, 1, 20),
    _CoDevWDSLinkStsPktsRxRate18_Type()
)
coDevWDSLinkStsPktsRxRate18.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWDSLinkStsPktsRxRate18.setStatus("current")
_CoDevWDSLinkStsPktsRxRate24_Type = Counter32
_CoDevWDSLinkStsPktsRxRate24_Object = MibTableColumn
coDevWDSLinkStsPktsRxRate24 = _CoDevWDSLinkStsPktsRxRate24_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 5, 2, 1, 21),
    _CoDevWDSLinkStsPktsRxRate24_Type()
)
coDevWDSLinkStsPktsRxRate24.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWDSLinkStsPktsRxRate24.setStatus("current")
_CoDevWDSLinkStsPktsRxRate36_Type = Counter32
_CoDevWDSLinkStsPktsRxRate36_Object = MibTableColumn
coDevWDSLinkStsPktsRxRate36 = _CoDevWDSLinkStsPktsRxRate36_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 5, 2, 1, 22),
    _CoDevWDSLinkStsPktsRxRate36_Type()
)
coDevWDSLinkStsPktsRxRate36.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWDSLinkStsPktsRxRate36.setStatus("current")
_CoDevWDSLinkStsPktsRxRate48_Type = Counter32
_CoDevWDSLinkStsPktsRxRate48_Object = MibTableColumn
coDevWDSLinkStsPktsRxRate48 = _CoDevWDSLinkStsPktsRxRate48_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 5, 2, 1, 23),
    _CoDevWDSLinkStsPktsRxRate48_Type()
)
coDevWDSLinkStsPktsRxRate48.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWDSLinkStsPktsRxRate48.setStatus("current")
_CoDevWDSLinkStsPktsRxRate54_Type = Counter32
_CoDevWDSLinkStsPktsRxRate54_Object = MibTableColumn
coDevWDSLinkStsPktsRxRate54 = _CoDevWDSLinkStsPktsRxRate54_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 5, 2, 1, 24),
    _CoDevWDSLinkStsPktsRxRate54_Type()
)
coDevWDSLinkStsPktsRxRate54.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWDSLinkStsPktsRxRate54.setStatus("current")
_CoDeviceWDSLinkStatsHTRatesTable_Object = MibTable
coDeviceWDSLinkStatsHTRatesTable = _CoDeviceWDSLinkStatsHTRatesTable_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 5, 3)
)
if mibBuilder.loadTexts:
    coDeviceWDSLinkStatsHTRatesTable.setStatus("current")
_CoDeviceWDSLinkStatsHTRatesEntry_Object = MibTableRow
coDeviceWDSLinkStatsHTRatesEntry = _CoDeviceWDSLinkStatsHTRatesEntry_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 5, 3, 1)
)
if mibBuilder.loadTexts:
    coDeviceWDSLinkStatsHTRatesEntry.setStatus("current")
_CoDevWDSLinkStsPktsTxMCS0_Type = Counter32
_CoDevWDSLinkStsPktsTxMCS0_Object = MibTableColumn
coDevWDSLinkStsPktsTxMCS0 = _CoDevWDSLinkStsPktsTxMCS0_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 5, 3, 1, 1),
    _CoDevWDSLinkStsPktsTxMCS0_Type()
)
coDevWDSLinkStsPktsTxMCS0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWDSLinkStsPktsTxMCS0.setStatus("current")
_CoDevWDSLinkStsPktsTxMCS1_Type = Counter32
_CoDevWDSLinkStsPktsTxMCS1_Object = MibTableColumn
coDevWDSLinkStsPktsTxMCS1 = _CoDevWDSLinkStsPktsTxMCS1_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 5, 3, 1, 2),
    _CoDevWDSLinkStsPktsTxMCS1_Type()
)
coDevWDSLinkStsPktsTxMCS1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWDSLinkStsPktsTxMCS1.setStatus("current")
_CoDevWDSLinkStsPktsTxMCS2_Type = Counter32
_CoDevWDSLinkStsPktsTxMCS2_Object = MibTableColumn
coDevWDSLinkStsPktsTxMCS2 = _CoDevWDSLinkStsPktsTxMCS2_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 5, 3, 1, 3),
    _CoDevWDSLinkStsPktsTxMCS2_Type()
)
coDevWDSLinkStsPktsTxMCS2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWDSLinkStsPktsTxMCS2.setStatus("current")
_CoDevWDSLinkStsPktsTxMCS3_Type = Counter32
_CoDevWDSLinkStsPktsTxMCS3_Object = MibTableColumn
coDevWDSLinkStsPktsTxMCS3 = _CoDevWDSLinkStsPktsTxMCS3_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 5, 3, 1, 4),
    _CoDevWDSLinkStsPktsTxMCS3_Type()
)
coDevWDSLinkStsPktsTxMCS3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWDSLinkStsPktsTxMCS3.setStatus("current")
_CoDevWDSLinkStsPktsTxMCS4_Type = Counter32
_CoDevWDSLinkStsPktsTxMCS4_Object = MibTableColumn
coDevWDSLinkStsPktsTxMCS4 = _CoDevWDSLinkStsPktsTxMCS4_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 5, 3, 1, 5),
    _CoDevWDSLinkStsPktsTxMCS4_Type()
)
coDevWDSLinkStsPktsTxMCS4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWDSLinkStsPktsTxMCS4.setStatus("current")
_CoDevWDSLinkStsPktsTxMCS5_Type = Counter32
_CoDevWDSLinkStsPktsTxMCS5_Object = MibTableColumn
coDevWDSLinkStsPktsTxMCS5 = _CoDevWDSLinkStsPktsTxMCS5_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 5, 3, 1, 6),
    _CoDevWDSLinkStsPktsTxMCS5_Type()
)
coDevWDSLinkStsPktsTxMCS5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWDSLinkStsPktsTxMCS5.setStatus("current")
_CoDevWDSLinkStsPktsTxMCS6_Type = Counter32
_CoDevWDSLinkStsPktsTxMCS6_Object = MibTableColumn
coDevWDSLinkStsPktsTxMCS6 = _CoDevWDSLinkStsPktsTxMCS6_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 5, 3, 1, 7),
    _CoDevWDSLinkStsPktsTxMCS6_Type()
)
coDevWDSLinkStsPktsTxMCS6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWDSLinkStsPktsTxMCS6.setStatus("current")
_CoDevWDSLinkStsPktsTxMCS7_Type = Counter32
_CoDevWDSLinkStsPktsTxMCS7_Object = MibTableColumn
coDevWDSLinkStsPktsTxMCS7 = _CoDevWDSLinkStsPktsTxMCS7_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 5, 3, 1, 8),
    _CoDevWDSLinkStsPktsTxMCS7_Type()
)
coDevWDSLinkStsPktsTxMCS7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWDSLinkStsPktsTxMCS7.setStatus("current")
_CoDevWDSLinkStsPktsTxMCS8_Type = Counter32
_CoDevWDSLinkStsPktsTxMCS8_Object = MibTableColumn
coDevWDSLinkStsPktsTxMCS8 = _CoDevWDSLinkStsPktsTxMCS8_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 5, 3, 1, 9),
    _CoDevWDSLinkStsPktsTxMCS8_Type()
)
coDevWDSLinkStsPktsTxMCS8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWDSLinkStsPktsTxMCS8.setStatus("current")
_CoDevWDSLinkStsPktsTxMCS9_Type = Counter32
_CoDevWDSLinkStsPktsTxMCS9_Object = MibTableColumn
coDevWDSLinkStsPktsTxMCS9 = _CoDevWDSLinkStsPktsTxMCS9_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 5, 3, 1, 10),
    _CoDevWDSLinkStsPktsTxMCS9_Type()
)
coDevWDSLinkStsPktsTxMCS9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWDSLinkStsPktsTxMCS9.setStatus("current")
_CoDevWDSLinkStsPktsTxMCS10_Type = Counter32
_CoDevWDSLinkStsPktsTxMCS10_Object = MibTableColumn
coDevWDSLinkStsPktsTxMCS10 = _CoDevWDSLinkStsPktsTxMCS10_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 5, 3, 1, 11),
    _CoDevWDSLinkStsPktsTxMCS10_Type()
)
coDevWDSLinkStsPktsTxMCS10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWDSLinkStsPktsTxMCS10.setStatus("current")
_CoDevWDSLinkStsPktsTxMCS11_Type = Counter32
_CoDevWDSLinkStsPktsTxMCS11_Object = MibTableColumn
coDevWDSLinkStsPktsTxMCS11 = _CoDevWDSLinkStsPktsTxMCS11_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 5, 3, 1, 12),
    _CoDevWDSLinkStsPktsTxMCS11_Type()
)
coDevWDSLinkStsPktsTxMCS11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWDSLinkStsPktsTxMCS11.setStatus("current")
_CoDevWDSLinkStsPktsTxMCS12_Type = Counter32
_CoDevWDSLinkStsPktsTxMCS12_Object = MibTableColumn
coDevWDSLinkStsPktsTxMCS12 = _CoDevWDSLinkStsPktsTxMCS12_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 5, 3, 1, 13),
    _CoDevWDSLinkStsPktsTxMCS12_Type()
)
coDevWDSLinkStsPktsTxMCS12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWDSLinkStsPktsTxMCS12.setStatus("current")
_CoDevWDSLinkStsPktsTxMCS13_Type = Counter32
_CoDevWDSLinkStsPktsTxMCS13_Object = MibTableColumn
coDevWDSLinkStsPktsTxMCS13 = _CoDevWDSLinkStsPktsTxMCS13_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 5, 3, 1, 14),
    _CoDevWDSLinkStsPktsTxMCS13_Type()
)
coDevWDSLinkStsPktsTxMCS13.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWDSLinkStsPktsTxMCS13.setStatus("current")
_CoDevWDSLinkStsPktsTxMCS14_Type = Counter32
_CoDevWDSLinkStsPktsTxMCS14_Object = MibTableColumn
coDevWDSLinkStsPktsTxMCS14 = _CoDevWDSLinkStsPktsTxMCS14_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 5, 3, 1, 15),
    _CoDevWDSLinkStsPktsTxMCS14_Type()
)
coDevWDSLinkStsPktsTxMCS14.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWDSLinkStsPktsTxMCS14.setStatus("current")
_CoDevWDSLinkStsPktsTxMCS15_Type = Counter32
_CoDevWDSLinkStsPktsTxMCS15_Object = MibTableColumn
coDevWDSLinkStsPktsTxMCS15 = _CoDevWDSLinkStsPktsTxMCS15_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 5, 3, 1, 16),
    _CoDevWDSLinkStsPktsTxMCS15_Type()
)
coDevWDSLinkStsPktsTxMCS15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWDSLinkStsPktsTxMCS15.setStatus("current")
_CoDevWDSLinkStsPktsRxMCS0_Type = Counter32
_CoDevWDSLinkStsPktsRxMCS0_Object = MibTableColumn
coDevWDSLinkStsPktsRxMCS0 = _CoDevWDSLinkStsPktsRxMCS0_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 5, 3, 1, 17),
    _CoDevWDSLinkStsPktsRxMCS0_Type()
)
coDevWDSLinkStsPktsRxMCS0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWDSLinkStsPktsRxMCS0.setStatus("current")
_CoDevWDSLinkStsPktsRxMCS1_Type = Counter32
_CoDevWDSLinkStsPktsRxMCS1_Object = MibTableColumn
coDevWDSLinkStsPktsRxMCS1 = _CoDevWDSLinkStsPktsRxMCS1_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 5, 3, 1, 18),
    _CoDevWDSLinkStsPktsRxMCS1_Type()
)
coDevWDSLinkStsPktsRxMCS1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWDSLinkStsPktsRxMCS1.setStatus("current")
_CoDevWDSLinkStsPktsRxMCS2_Type = Counter32
_CoDevWDSLinkStsPktsRxMCS2_Object = MibTableColumn
coDevWDSLinkStsPktsRxMCS2 = _CoDevWDSLinkStsPktsRxMCS2_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 5, 3, 1, 19),
    _CoDevWDSLinkStsPktsRxMCS2_Type()
)
coDevWDSLinkStsPktsRxMCS2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWDSLinkStsPktsRxMCS2.setStatus("current")
_CoDevWDSLinkStsPktsRxMCS3_Type = Counter32
_CoDevWDSLinkStsPktsRxMCS3_Object = MibTableColumn
coDevWDSLinkStsPktsRxMCS3 = _CoDevWDSLinkStsPktsRxMCS3_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 5, 3, 1, 20),
    _CoDevWDSLinkStsPktsRxMCS3_Type()
)
coDevWDSLinkStsPktsRxMCS3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWDSLinkStsPktsRxMCS3.setStatus("current")
_CoDevWDSLinkStsPktsRxMCS4_Type = Counter32
_CoDevWDSLinkStsPktsRxMCS4_Object = MibTableColumn
coDevWDSLinkStsPktsRxMCS4 = _CoDevWDSLinkStsPktsRxMCS4_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 5, 3, 1, 21),
    _CoDevWDSLinkStsPktsRxMCS4_Type()
)
coDevWDSLinkStsPktsRxMCS4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWDSLinkStsPktsRxMCS4.setStatus("current")
_CoDevWDSLinkStsPktsRxMCS5_Type = Counter32
_CoDevWDSLinkStsPktsRxMCS5_Object = MibTableColumn
coDevWDSLinkStsPktsRxMCS5 = _CoDevWDSLinkStsPktsRxMCS5_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 5, 3, 1, 22),
    _CoDevWDSLinkStsPktsRxMCS5_Type()
)
coDevWDSLinkStsPktsRxMCS5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWDSLinkStsPktsRxMCS5.setStatus("current")
_CoDevWDSLinkStsPktsRxMCS6_Type = Counter32
_CoDevWDSLinkStsPktsRxMCS6_Object = MibTableColumn
coDevWDSLinkStsPktsRxMCS6 = _CoDevWDSLinkStsPktsRxMCS6_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 5, 3, 1, 23),
    _CoDevWDSLinkStsPktsRxMCS6_Type()
)
coDevWDSLinkStsPktsRxMCS6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWDSLinkStsPktsRxMCS6.setStatus("current")
_CoDevWDSLinkStsPktsRxMCS7_Type = Counter32
_CoDevWDSLinkStsPktsRxMCS7_Object = MibTableColumn
coDevWDSLinkStsPktsRxMCS7 = _CoDevWDSLinkStsPktsRxMCS7_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 5, 3, 1, 24),
    _CoDevWDSLinkStsPktsRxMCS7_Type()
)
coDevWDSLinkStsPktsRxMCS7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWDSLinkStsPktsRxMCS7.setStatus("current")
_CoDevWDSLinkStsPktsRxMCS8_Type = Counter32
_CoDevWDSLinkStsPktsRxMCS8_Object = MibTableColumn
coDevWDSLinkStsPktsRxMCS8 = _CoDevWDSLinkStsPktsRxMCS8_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 5, 3, 1, 25),
    _CoDevWDSLinkStsPktsRxMCS8_Type()
)
coDevWDSLinkStsPktsRxMCS8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWDSLinkStsPktsRxMCS8.setStatus("current")
_CoDevWDSLinkStsPktsRxMCS9_Type = Counter32
_CoDevWDSLinkStsPktsRxMCS9_Object = MibTableColumn
coDevWDSLinkStsPktsRxMCS9 = _CoDevWDSLinkStsPktsRxMCS9_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 5, 3, 1, 26),
    _CoDevWDSLinkStsPktsRxMCS9_Type()
)
coDevWDSLinkStsPktsRxMCS9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWDSLinkStsPktsRxMCS9.setStatus("current")
_CoDevWDSLinkStsPktsRxMCS10_Type = Counter32
_CoDevWDSLinkStsPktsRxMCS10_Object = MibTableColumn
coDevWDSLinkStsPktsRxMCS10 = _CoDevWDSLinkStsPktsRxMCS10_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 5, 3, 1, 27),
    _CoDevWDSLinkStsPktsRxMCS10_Type()
)
coDevWDSLinkStsPktsRxMCS10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWDSLinkStsPktsRxMCS10.setStatus("current")
_CoDevWDSLinkStsPktsRxMCS11_Type = Counter32
_CoDevWDSLinkStsPktsRxMCS11_Object = MibTableColumn
coDevWDSLinkStsPktsRxMCS11 = _CoDevWDSLinkStsPktsRxMCS11_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 5, 3, 1, 28),
    _CoDevWDSLinkStsPktsRxMCS11_Type()
)
coDevWDSLinkStsPktsRxMCS11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWDSLinkStsPktsRxMCS11.setStatus("current")
_CoDevWDSLinkStsPktsRxMCS12_Type = Counter32
_CoDevWDSLinkStsPktsRxMCS12_Object = MibTableColumn
coDevWDSLinkStsPktsRxMCS12 = _CoDevWDSLinkStsPktsRxMCS12_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 5, 3, 1, 29),
    _CoDevWDSLinkStsPktsRxMCS12_Type()
)
coDevWDSLinkStsPktsRxMCS12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWDSLinkStsPktsRxMCS12.setStatus("current")
_CoDevWDSLinkStsPktsRxMCS13_Type = Counter32
_CoDevWDSLinkStsPktsRxMCS13_Object = MibTableColumn
coDevWDSLinkStsPktsRxMCS13 = _CoDevWDSLinkStsPktsRxMCS13_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 5, 3, 1, 30),
    _CoDevWDSLinkStsPktsRxMCS13_Type()
)
coDevWDSLinkStsPktsRxMCS13.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWDSLinkStsPktsRxMCS13.setStatus("current")
_CoDevWDSLinkStsPktsRxMCS14_Type = Counter32
_CoDevWDSLinkStsPktsRxMCS14_Object = MibTableColumn
coDevWDSLinkStsPktsRxMCS14 = _CoDevWDSLinkStsPktsRxMCS14_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 5, 3, 1, 31),
    _CoDevWDSLinkStsPktsRxMCS14_Type()
)
coDevWDSLinkStsPktsRxMCS14.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWDSLinkStsPktsRxMCS14.setStatus("current")
_CoDevWDSLinkStsPktsRxMCS15_Type = Counter32
_CoDevWDSLinkStsPktsRxMCS15_Object = MibTableColumn
coDevWDSLinkStsPktsRxMCS15 = _CoDevWDSLinkStsPktsRxMCS15_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 5, 3, 1, 32),
    _CoDevWDSLinkStsPktsRxMCS15_Type()
)
coDevWDSLinkStsPktsRxMCS15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWDSLinkStsPktsRxMCS15.setStatus("current")
_CoDeviceWDSLinkStatsVHTRatesTable_Object = MibTable
coDeviceWDSLinkStatsVHTRatesTable = _CoDeviceWDSLinkStatsVHTRatesTable_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 5, 4)
)
if mibBuilder.loadTexts:
    coDeviceWDSLinkStatsVHTRatesTable.setStatus("current")
_CoDeviceWDSLinkStatsVHTRatesEntry_Object = MibTableRow
coDeviceWDSLinkStatsVHTRatesEntry = _CoDeviceWDSLinkStatsVHTRatesEntry_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 5, 4, 1)
)
if mibBuilder.loadTexts:
    coDeviceWDSLinkStatsVHTRatesEntry.setStatus("current")
_CoDevWDSLinkStsPktsTxNSS1VHTMCS0_Type = Counter32
_CoDevWDSLinkStsPktsTxNSS1VHTMCS0_Object = MibTableColumn
coDevWDSLinkStsPktsTxNSS1VHTMCS0 = _CoDevWDSLinkStsPktsTxNSS1VHTMCS0_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 5, 4, 1, 1),
    _CoDevWDSLinkStsPktsTxNSS1VHTMCS0_Type()
)
coDevWDSLinkStsPktsTxNSS1VHTMCS0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWDSLinkStsPktsTxNSS1VHTMCS0.setStatus("current")
_CoDevWDSLinkStsPktsTxNSS1VHTMCS1_Type = Counter32
_CoDevWDSLinkStsPktsTxNSS1VHTMCS1_Object = MibTableColumn
coDevWDSLinkStsPktsTxNSS1VHTMCS1 = _CoDevWDSLinkStsPktsTxNSS1VHTMCS1_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 5, 4, 1, 2),
    _CoDevWDSLinkStsPktsTxNSS1VHTMCS1_Type()
)
coDevWDSLinkStsPktsTxNSS1VHTMCS1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWDSLinkStsPktsTxNSS1VHTMCS1.setStatus("current")
_CoDevWDSLinkStsPktsTxNSS1VHTMCS2_Type = Counter32
_CoDevWDSLinkStsPktsTxNSS1VHTMCS2_Object = MibTableColumn
coDevWDSLinkStsPktsTxNSS1VHTMCS2 = _CoDevWDSLinkStsPktsTxNSS1VHTMCS2_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 5, 4, 1, 3),
    _CoDevWDSLinkStsPktsTxNSS1VHTMCS2_Type()
)
coDevWDSLinkStsPktsTxNSS1VHTMCS2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWDSLinkStsPktsTxNSS1VHTMCS2.setStatus("current")
_CoDevWDSLinkStsPktsTxNSS1VHTMCS3_Type = Counter32
_CoDevWDSLinkStsPktsTxNSS1VHTMCS3_Object = MibTableColumn
coDevWDSLinkStsPktsTxNSS1VHTMCS3 = _CoDevWDSLinkStsPktsTxNSS1VHTMCS3_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 5, 4, 1, 4),
    _CoDevWDSLinkStsPktsTxNSS1VHTMCS3_Type()
)
coDevWDSLinkStsPktsTxNSS1VHTMCS3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWDSLinkStsPktsTxNSS1VHTMCS3.setStatus("current")
_CoDevWDSLinkStsPktsTxNSS1VHTMCS4_Type = Counter32
_CoDevWDSLinkStsPktsTxNSS1VHTMCS4_Object = MibTableColumn
coDevWDSLinkStsPktsTxNSS1VHTMCS4 = _CoDevWDSLinkStsPktsTxNSS1VHTMCS4_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 5, 4, 1, 5),
    _CoDevWDSLinkStsPktsTxNSS1VHTMCS4_Type()
)
coDevWDSLinkStsPktsTxNSS1VHTMCS4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWDSLinkStsPktsTxNSS1VHTMCS4.setStatus("current")
_CoDevWDSLinkStsPktsTxNSS1VHTMCS5_Type = Counter32
_CoDevWDSLinkStsPktsTxNSS1VHTMCS5_Object = MibTableColumn
coDevWDSLinkStsPktsTxNSS1VHTMCS5 = _CoDevWDSLinkStsPktsTxNSS1VHTMCS5_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 5, 4, 1, 6),
    _CoDevWDSLinkStsPktsTxNSS1VHTMCS5_Type()
)
coDevWDSLinkStsPktsTxNSS1VHTMCS5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWDSLinkStsPktsTxNSS1VHTMCS5.setStatus("current")
_CoDevWDSLinkStsPktsTxNSS1VHTMCS6_Type = Counter32
_CoDevWDSLinkStsPktsTxNSS1VHTMCS6_Object = MibTableColumn
coDevWDSLinkStsPktsTxNSS1VHTMCS6 = _CoDevWDSLinkStsPktsTxNSS1VHTMCS6_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 5, 4, 1, 7),
    _CoDevWDSLinkStsPktsTxNSS1VHTMCS6_Type()
)
coDevWDSLinkStsPktsTxNSS1VHTMCS6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWDSLinkStsPktsTxNSS1VHTMCS6.setStatus("current")
_CoDevWDSLinkStsPktsTxNSS1VHTMCS7_Type = Counter32
_CoDevWDSLinkStsPktsTxNSS1VHTMCS7_Object = MibTableColumn
coDevWDSLinkStsPktsTxNSS1VHTMCS7 = _CoDevWDSLinkStsPktsTxNSS1VHTMCS7_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 5, 4, 1, 8),
    _CoDevWDSLinkStsPktsTxNSS1VHTMCS7_Type()
)
coDevWDSLinkStsPktsTxNSS1VHTMCS7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWDSLinkStsPktsTxNSS1VHTMCS7.setStatus("current")
_CoDevWDSLinkStsPktsTxNSS1VHTMCS8_Type = Counter32
_CoDevWDSLinkStsPktsTxNSS1VHTMCS8_Object = MibTableColumn
coDevWDSLinkStsPktsTxNSS1VHTMCS8 = _CoDevWDSLinkStsPktsTxNSS1VHTMCS8_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 5, 4, 1, 9),
    _CoDevWDSLinkStsPktsTxNSS1VHTMCS8_Type()
)
coDevWDSLinkStsPktsTxNSS1VHTMCS8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWDSLinkStsPktsTxNSS1VHTMCS8.setStatus("current")
_CoDevWDSLinkStsPktsTxNSS1VHTMCS9_Type = Counter32
_CoDevWDSLinkStsPktsTxNSS1VHTMCS9_Object = MibTableColumn
coDevWDSLinkStsPktsTxNSS1VHTMCS9 = _CoDevWDSLinkStsPktsTxNSS1VHTMCS9_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 5, 4, 1, 10),
    _CoDevWDSLinkStsPktsTxNSS1VHTMCS9_Type()
)
coDevWDSLinkStsPktsTxNSS1VHTMCS9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWDSLinkStsPktsTxNSS1VHTMCS9.setStatus("current")
_CoDevWDSLinkStsPktsTxNSS2VHTMCS0_Type = Counter32
_CoDevWDSLinkStsPktsTxNSS2VHTMCS0_Object = MibTableColumn
coDevWDSLinkStsPktsTxNSS2VHTMCS0 = _CoDevWDSLinkStsPktsTxNSS2VHTMCS0_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 5, 4, 1, 11),
    _CoDevWDSLinkStsPktsTxNSS2VHTMCS0_Type()
)
coDevWDSLinkStsPktsTxNSS2VHTMCS0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWDSLinkStsPktsTxNSS2VHTMCS0.setStatus("current")
_CoDevWDSLinkStsPktsTxNSS2VHTMCS1_Type = Counter32
_CoDevWDSLinkStsPktsTxNSS2VHTMCS1_Object = MibTableColumn
coDevWDSLinkStsPktsTxNSS2VHTMCS1 = _CoDevWDSLinkStsPktsTxNSS2VHTMCS1_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 5, 4, 1, 12),
    _CoDevWDSLinkStsPktsTxNSS2VHTMCS1_Type()
)
coDevWDSLinkStsPktsTxNSS2VHTMCS1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWDSLinkStsPktsTxNSS2VHTMCS1.setStatus("current")
_CoDevWDSLinkStsPktsTxNSS2VHTMCS2_Type = Counter32
_CoDevWDSLinkStsPktsTxNSS2VHTMCS2_Object = MibTableColumn
coDevWDSLinkStsPktsTxNSS2VHTMCS2 = _CoDevWDSLinkStsPktsTxNSS2VHTMCS2_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 5, 4, 1, 13),
    _CoDevWDSLinkStsPktsTxNSS2VHTMCS2_Type()
)
coDevWDSLinkStsPktsTxNSS2VHTMCS2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWDSLinkStsPktsTxNSS2VHTMCS2.setStatus("current")
_CoDevWDSLinkStsPktsTxNSS2VHTMCS3_Type = Counter32
_CoDevWDSLinkStsPktsTxNSS2VHTMCS3_Object = MibTableColumn
coDevWDSLinkStsPktsTxNSS2VHTMCS3 = _CoDevWDSLinkStsPktsTxNSS2VHTMCS3_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 5, 4, 1, 14),
    _CoDevWDSLinkStsPktsTxNSS2VHTMCS3_Type()
)
coDevWDSLinkStsPktsTxNSS2VHTMCS3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWDSLinkStsPktsTxNSS2VHTMCS3.setStatus("current")
_CoDevWDSLinkStsPktsTxNSS2VHTMCS4_Type = Counter32
_CoDevWDSLinkStsPktsTxNSS2VHTMCS4_Object = MibTableColumn
coDevWDSLinkStsPktsTxNSS2VHTMCS4 = _CoDevWDSLinkStsPktsTxNSS2VHTMCS4_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 5, 4, 1, 15),
    _CoDevWDSLinkStsPktsTxNSS2VHTMCS4_Type()
)
coDevWDSLinkStsPktsTxNSS2VHTMCS4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWDSLinkStsPktsTxNSS2VHTMCS4.setStatus("current")
_CoDevWDSLinkStsPktsTxNSS2VHTMCS5_Type = Counter32
_CoDevWDSLinkStsPktsTxNSS2VHTMCS5_Object = MibTableColumn
coDevWDSLinkStsPktsTxNSS2VHTMCS5 = _CoDevWDSLinkStsPktsTxNSS2VHTMCS5_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 5, 4, 1, 16),
    _CoDevWDSLinkStsPktsTxNSS2VHTMCS5_Type()
)
coDevWDSLinkStsPktsTxNSS2VHTMCS5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWDSLinkStsPktsTxNSS2VHTMCS5.setStatus("current")
_CoDevWDSLinkStsPktsTxNSS2VHTMCS6_Type = Counter32
_CoDevWDSLinkStsPktsTxNSS2VHTMCS6_Object = MibTableColumn
coDevWDSLinkStsPktsTxNSS2VHTMCS6 = _CoDevWDSLinkStsPktsTxNSS2VHTMCS6_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 5, 4, 1, 17),
    _CoDevWDSLinkStsPktsTxNSS2VHTMCS6_Type()
)
coDevWDSLinkStsPktsTxNSS2VHTMCS6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWDSLinkStsPktsTxNSS2VHTMCS6.setStatus("current")
_CoDevWDSLinkStsPktsTxNSS2VHTMCS7_Type = Counter32
_CoDevWDSLinkStsPktsTxNSS2VHTMCS7_Object = MibTableColumn
coDevWDSLinkStsPktsTxNSS2VHTMCS7 = _CoDevWDSLinkStsPktsTxNSS2VHTMCS7_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 5, 4, 1, 18),
    _CoDevWDSLinkStsPktsTxNSS2VHTMCS7_Type()
)
coDevWDSLinkStsPktsTxNSS2VHTMCS7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWDSLinkStsPktsTxNSS2VHTMCS7.setStatus("current")
_CoDevWDSLinkStsPktsTxNSS2VHTMCS8_Type = Counter32
_CoDevWDSLinkStsPktsTxNSS2VHTMCS8_Object = MibTableColumn
coDevWDSLinkStsPktsTxNSS2VHTMCS8 = _CoDevWDSLinkStsPktsTxNSS2VHTMCS8_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 5, 4, 1, 19),
    _CoDevWDSLinkStsPktsTxNSS2VHTMCS8_Type()
)
coDevWDSLinkStsPktsTxNSS2VHTMCS8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWDSLinkStsPktsTxNSS2VHTMCS8.setStatus("current")
_CoDevWDSLinkStsPktsTxNSS2VHTMCS9_Type = Counter32
_CoDevWDSLinkStsPktsTxNSS2VHTMCS9_Object = MibTableColumn
coDevWDSLinkStsPktsTxNSS2VHTMCS9 = _CoDevWDSLinkStsPktsTxNSS2VHTMCS9_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 5, 4, 1, 20),
    _CoDevWDSLinkStsPktsTxNSS2VHTMCS9_Type()
)
coDevWDSLinkStsPktsTxNSS2VHTMCS9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWDSLinkStsPktsTxNSS2VHTMCS9.setStatus("current")
_CoDevWDSLinkStsPktsTxNSS3VHTMCS0_Type = Counter32
_CoDevWDSLinkStsPktsTxNSS3VHTMCS0_Object = MibTableColumn
coDevWDSLinkStsPktsTxNSS3VHTMCS0 = _CoDevWDSLinkStsPktsTxNSS3VHTMCS0_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 5, 4, 1, 21),
    _CoDevWDSLinkStsPktsTxNSS3VHTMCS0_Type()
)
coDevWDSLinkStsPktsTxNSS3VHTMCS0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWDSLinkStsPktsTxNSS3VHTMCS0.setStatus("current")
_CoDevWDSLinkStsPktsTxNSS3VHTMCS1_Type = Counter32
_CoDevWDSLinkStsPktsTxNSS3VHTMCS1_Object = MibTableColumn
coDevWDSLinkStsPktsTxNSS3VHTMCS1 = _CoDevWDSLinkStsPktsTxNSS3VHTMCS1_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 5, 4, 1, 22),
    _CoDevWDSLinkStsPktsTxNSS3VHTMCS1_Type()
)
coDevWDSLinkStsPktsTxNSS3VHTMCS1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWDSLinkStsPktsTxNSS3VHTMCS1.setStatus("current")
_CoDevWDSLinkStsPktsTxNSS3VHTMCS2_Type = Counter32
_CoDevWDSLinkStsPktsTxNSS3VHTMCS2_Object = MibTableColumn
coDevWDSLinkStsPktsTxNSS3VHTMCS2 = _CoDevWDSLinkStsPktsTxNSS3VHTMCS2_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 5, 4, 1, 23),
    _CoDevWDSLinkStsPktsTxNSS3VHTMCS2_Type()
)
coDevWDSLinkStsPktsTxNSS3VHTMCS2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWDSLinkStsPktsTxNSS3VHTMCS2.setStatus("current")
_CoDevWDSLinkStsPktsTxNSS3VHTMCS3_Type = Counter32
_CoDevWDSLinkStsPktsTxNSS3VHTMCS3_Object = MibTableColumn
coDevWDSLinkStsPktsTxNSS3VHTMCS3 = _CoDevWDSLinkStsPktsTxNSS3VHTMCS3_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 5, 4, 1, 24),
    _CoDevWDSLinkStsPktsTxNSS3VHTMCS3_Type()
)
coDevWDSLinkStsPktsTxNSS3VHTMCS3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWDSLinkStsPktsTxNSS3VHTMCS3.setStatus("current")
_CoDevWDSLinkStsPktsTxNSS3VHTMCS4_Type = Counter32
_CoDevWDSLinkStsPktsTxNSS3VHTMCS4_Object = MibTableColumn
coDevWDSLinkStsPktsTxNSS3VHTMCS4 = _CoDevWDSLinkStsPktsTxNSS3VHTMCS4_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 5, 4, 1, 25),
    _CoDevWDSLinkStsPktsTxNSS3VHTMCS4_Type()
)
coDevWDSLinkStsPktsTxNSS3VHTMCS4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWDSLinkStsPktsTxNSS3VHTMCS4.setStatus("current")
_CoDevWDSLinkStsPktsTxNSS3VHTMCS5_Type = Counter32
_CoDevWDSLinkStsPktsTxNSS3VHTMCS5_Object = MibTableColumn
coDevWDSLinkStsPktsTxNSS3VHTMCS5 = _CoDevWDSLinkStsPktsTxNSS3VHTMCS5_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 5, 4, 1, 26),
    _CoDevWDSLinkStsPktsTxNSS3VHTMCS5_Type()
)
coDevWDSLinkStsPktsTxNSS3VHTMCS5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWDSLinkStsPktsTxNSS3VHTMCS5.setStatus("current")
_CoDevWDSLinkStsPktsTxNSS3VHTMCS6_Type = Counter32
_CoDevWDSLinkStsPktsTxNSS3VHTMCS6_Object = MibTableColumn
coDevWDSLinkStsPktsTxNSS3VHTMCS6 = _CoDevWDSLinkStsPktsTxNSS3VHTMCS6_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 5, 4, 1, 27),
    _CoDevWDSLinkStsPktsTxNSS3VHTMCS6_Type()
)
coDevWDSLinkStsPktsTxNSS3VHTMCS6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWDSLinkStsPktsTxNSS3VHTMCS6.setStatus("current")
_CoDevWDSLinkStsPktsTxNSS3VHTMCS7_Type = Counter32
_CoDevWDSLinkStsPktsTxNSS3VHTMCS7_Object = MibTableColumn
coDevWDSLinkStsPktsTxNSS3VHTMCS7 = _CoDevWDSLinkStsPktsTxNSS3VHTMCS7_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 5, 4, 1, 28),
    _CoDevWDSLinkStsPktsTxNSS3VHTMCS7_Type()
)
coDevWDSLinkStsPktsTxNSS3VHTMCS7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWDSLinkStsPktsTxNSS3VHTMCS7.setStatus("current")
_CoDevWDSLinkStsPktsTxNSS3VHTMCS8_Type = Counter32
_CoDevWDSLinkStsPktsTxNSS3VHTMCS8_Object = MibTableColumn
coDevWDSLinkStsPktsTxNSS3VHTMCS8 = _CoDevWDSLinkStsPktsTxNSS3VHTMCS8_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 5, 4, 1, 29),
    _CoDevWDSLinkStsPktsTxNSS3VHTMCS8_Type()
)
coDevWDSLinkStsPktsTxNSS3VHTMCS8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWDSLinkStsPktsTxNSS3VHTMCS8.setStatus("current")
_CoDevWDSLinkStsPktsTxNSS3VHTMCS9_Type = Counter32
_CoDevWDSLinkStsPktsTxNSS3VHTMCS9_Object = MibTableColumn
coDevWDSLinkStsPktsTxNSS3VHTMCS9 = _CoDevWDSLinkStsPktsTxNSS3VHTMCS9_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 5, 4, 1, 30),
    _CoDevWDSLinkStsPktsTxNSS3VHTMCS9_Type()
)
coDevWDSLinkStsPktsTxNSS3VHTMCS9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWDSLinkStsPktsTxNSS3VHTMCS9.setStatus("current")
_CoDevWDSLinkStsPktsRxNSS1VHTMCS0_Type = Counter32
_CoDevWDSLinkStsPktsRxNSS1VHTMCS0_Object = MibTableColumn
coDevWDSLinkStsPktsRxNSS1VHTMCS0 = _CoDevWDSLinkStsPktsRxNSS1VHTMCS0_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 5, 4, 1, 31),
    _CoDevWDSLinkStsPktsRxNSS1VHTMCS0_Type()
)
coDevWDSLinkStsPktsRxNSS1VHTMCS0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWDSLinkStsPktsRxNSS1VHTMCS0.setStatus("current")
_CoDevWDSLinkStsPktsRxNSS1VHTMCS1_Type = Counter32
_CoDevWDSLinkStsPktsRxNSS1VHTMCS1_Object = MibTableColumn
coDevWDSLinkStsPktsRxNSS1VHTMCS1 = _CoDevWDSLinkStsPktsRxNSS1VHTMCS1_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 5, 4, 1, 32),
    _CoDevWDSLinkStsPktsRxNSS1VHTMCS1_Type()
)
coDevWDSLinkStsPktsRxNSS1VHTMCS1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWDSLinkStsPktsRxNSS1VHTMCS1.setStatus("current")
_CoDevWDSLinkStsPktsRxNSS1VHTMCS2_Type = Counter32
_CoDevWDSLinkStsPktsRxNSS1VHTMCS2_Object = MibTableColumn
coDevWDSLinkStsPktsRxNSS1VHTMCS2 = _CoDevWDSLinkStsPktsRxNSS1VHTMCS2_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 5, 4, 1, 33),
    _CoDevWDSLinkStsPktsRxNSS1VHTMCS2_Type()
)
coDevWDSLinkStsPktsRxNSS1VHTMCS2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWDSLinkStsPktsRxNSS1VHTMCS2.setStatus("current")
_CoDevWDSLinkStsPktsRxNSS1VHTMCS3_Type = Counter32
_CoDevWDSLinkStsPktsRxNSS1VHTMCS3_Object = MibTableColumn
coDevWDSLinkStsPktsRxNSS1VHTMCS3 = _CoDevWDSLinkStsPktsRxNSS1VHTMCS3_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 5, 4, 1, 34),
    _CoDevWDSLinkStsPktsRxNSS1VHTMCS3_Type()
)
coDevWDSLinkStsPktsRxNSS1VHTMCS3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWDSLinkStsPktsRxNSS1VHTMCS3.setStatus("current")
_CoDevWDSLinkStsPktsRxNSS1VHTMCS4_Type = Counter32
_CoDevWDSLinkStsPktsRxNSS1VHTMCS4_Object = MibTableColumn
coDevWDSLinkStsPktsRxNSS1VHTMCS4 = _CoDevWDSLinkStsPktsRxNSS1VHTMCS4_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 5, 4, 1, 35),
    _CoDevWDSLinkStsPktsRxNSS1VHTMCS4_Type()
)
coDevWDSLinkStsPktsRxNSS1VHTMCS4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWDSLinkStsPktsRxNSS1VHTMCS4.setStatus("current")
_CoDevWDSLinkStsPktsRxNSS1VHTMCS5_Type = Counter32
_CoDevWDSLinkStsPktsRxNSS1VHTMCS5_Object = MibTableColumn
coDevWDSLinkStsPktsRxNSS1VHTMCS5 = _CoDevWDSLinkStsPktsRxNSS1VHTMCS5_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 5, 4, 1, 36),
    _CoDevWDSLinkStsPktsRxNSS1VHTMCS5_Type()
)
coDevWDSLinkStsPktsRxNSS1VHTMCS5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWDSLinkStsPktsRxNSS1VHTMCS5.setStatus("current")
_CoDevWDSLinkStsPktsRxNSS1VHTMCS6_Type = Counter32
_CoDevWDSLinkStsPktsRxNSS1VHTMCS6_Object = MibTableColumn
coDevWDSLinkStsPktsRxNSS1VHTMCS6 = _CoDevWDSLinkStsPktsRxNSS1VHTMCS6_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 5, 4, 1, 37),
    _CoDevWDSLinkStsPktsRxNSS1VHTMCS6_Type()
)
coDevWDSLinkStsPktsRxNSS1VHTMCS6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWDSLinkStsPktsRxNSS1VHTMCS6.setStatus("current")
_CoDevWDSLinkStsPktsRxNSS1VHTMCS7_Type = Counter32
_CoDevWDSLinkStsPktsRxNSS1VHTMCS7_Object = MibTableColumn
coDevWDSLinkStsPktsRxNSS1VHTMCS7 = _CoDevWDSLinkStsPktsRxNSS1VHTMCS7_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 5, 4, 1, 38),
    _CoDevWDSLinkStsPktsRxNSS1VHTMCS7_Type()
)
coDevWDSLinkStsPktsRxNSS1VHTMCS7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWDSLinkStsPktsRxNSS1VHTMCS7.setStatus("current")
_CoDevWDSLinkStsPktsRxNSS1VHTMCS8_Type = Counter32
_CoDevWDSLinkStsPktsRxNSS1VHTMCS8_Object = MibTableColumn
coDevWDSLinkStsPktsRxNSS1VHTMCS8 = _CoDevWDSLinkStsPktsRxNSS1VHTMCS8_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 5, 4, 1, 39),
    _CoDevWDSLinkStsPktsRxNSS1VHTMCS8_Type()
)
coDevWDSLinkStsPktsRxNSS1VHTMCS8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWDSLinkStsPktsRxNSS1VHTMCS8.setStatus("current")
_CoDevWDSLinkStsPktsRxNSS1VHTMCS9_Type = Counter32
_CoDevWDSLinkStsPktsRxNSS1VHTMCS9_Object = MibTableColumn
coDevWDSLinkStsPktsRxNSS1VHTMCS9 = _CoDevWDSLinkStsPktsRxNSS1VHTMCS9_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 5, 4, 1, 40),
    _CoDevWDSLinkStsPktsRxNSS1VHTMCS9_Type()
)
coDevWDSLinkStsPktsRxNSS1VHTMCS9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWDSLinkStsPktsRxNSS1VHTMCS9.setStatus("current")
_CoDevWDSLinkStsPktsRxNSS2VHTMCS0_Type = Counter32
_CoDevWDSLinkStsPktsRxNSS2VHTMCS0_Object = MibTableColumn
coDevWDSLinkStsPktsRxNSS2VHTMCS0 = _CoDevWDSLinkStsPktsRxNSS2VHTMCS0_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 5, 4, 1, 41),
    _CoDevWDSLinkStsPktsRxNSS2VHTMCS0_Type()
)
coDevWDSLinkStsPktsRxNSS2VHTMCS0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWDSLinkStsPktsRxNSS2VHTMCS0.setStatus("current")
_CoDevWDSLinkStsPktsRxNSS2VHTMCS1_Type = Counter32
_CoDevWDSLinkStsPktsRxNSS2VHTMCS1_Object = MibTableColumn
coDevWDSLinkStsPktsRxNSS2VHTMCS1 = _CoDevWDSLinkStsPktsRxNSS2VHTMCS1_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 5, 4, 1, 42),
    _CoDevWDSLinkStsPktsRxNSS2VHTMCS1_Type()
)
coDevWDSLinkStsPktsRxNSS2VHTMCS1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWDSLinkStsPktsRxNSS2VHTMCS1.setStatus("current")
_CoDevWDSLinkStsPktsRxNSS2VHTMCS2_Type = Counter32
_CoDevWDSLinkStsPktsRxNSS2VHTMCS2_Object = MibTableColumn
coDevWDSLinkStsPktsRxNSS2VHTMCS2 = _CoDevWDSLinkStsPktsRxNSS2VHTMCS2_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 5, 4, 1, 43),
    _CoDevWDSLinkStsPktsRxNSS2VHTMCS2_Type()
)
coDevWDSLinkStsPktsRxNSS2VHTMCS2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWDSLinkStsPktsRxNSS2VHTMCS2.setStatus("current")
_CoDevWDSLinkStsPktsRxNSS2VHTMCS3_Type = Counter32
_CoDevWDSLinkStsPktsRxNSS2VHTMCS3_Object = MibTableColumn
coDevWDSLinkStsPktsRxNSS2VHTMCS3 = _CoDevWDSLinkStsPktsRxNSS2VHTMCS3_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 5, 4, 1, 44),
    _CoDevWDSLinkStsPktsRxNSS2VHTMCS3_Type()
)
coDevWDSLinkStsPktsRxNSS2VHTMCS3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWDSLinkStsPktsRxNSS2VHTMCS3.setStatus("current")
_CoDevWDSLinkStsPktsRxNSS2VHTMCS4_Type = Counter32
_CoDevWDSLinkStsPktsRxNSS2VHTMCS4_Object = MibTableColumn
coDevWDSLinkStsPktsRxNSS2VHTMCS4 = _CoDevWDSLinkStsPktsRxNSS2VHTMCS4_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 5, 4, 1, 45),
    _CoDevWDSLinkStsPktsRxNSS2VHTMCS4_Type()
)
coDevWDSLinkStsPktsRxNSS2VHTMCS4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWDSLinkStsPktsRxNSS2VHTMCS4.setStatus("current")
_CoDevWDSLinkStsPktsRxNSS2VHTMCS5_Type = Counter32
_CoDevWDSLinkStsPktsRxNSS2VHTMCS5_Object = MibTableColumn
coDevWDSLinkStsPktsRxNSS2VHTMCS5 = _CoDevWDSLinkStsPktsRxNSS2VHTMCS5_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 5, 4, 1, 46),
    _CoDevWDSLinkStsPktsRxNSS2VHTMCS5_Type()
)
coDevWDSLinkStsPktsRxNSS2VHTMCS5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWDSLinkStsPktsRxNSS2VHTMCS5.setStatus("current")
_CoDevWDSLinkStsPktsRxNSS2VHTMCS6_Type = Counter32
_CoDevWDSLinkStsPktsRxNSS2VHTMCS6_Object = MibTableColumn
coDevWDSLinkStsPktsRxNSS2VHTMCS6 = _CoDevWDSLinkStsPktsRxNSS2VHTMCS6_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 5, 4, 1, 47),
    _CoDevWDSLinkStsPktsRxNSS2VHTMCS6_Type()
)
coDevWDSLinkStsPktsRxNSS2VHTMCS6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWDSLinkStsPktsRxNSS2VHTMCS6.setStatus("current")
_CoDevWDSLinkStsPktsRxNSS2VHTMCS7_Type = Counter32
_CoDevWDSLinkStsPktsRxNSS2VHTMCS7_Object = MibTableColumn
coDevWDSLinkStsPktsRxNSS2VHTMCS7 = _CoDevWDSLinkStsPktsRxNSS2VHTMCS7_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 5, 4, 1, 48),
    _CoDevWDSLinkStsPktsRxNSS2VHTMCS7_Type()
)
coDevWDSLinkStsPktsRxNSS2VHTMCS7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWDSLinkStsPktsRxNSS2VHTMCS7.setStatus("current")
_CoDevWDSLinkStsPktsRxNSS2VHTMCS8_Type = Counter32
_CoDevWDSLinkStsPktsRxNSS2VHTMCS8_Object = MibTableColumn
coDevWDSLinkStsPktsRxNSS2VHTMCS8 = _CoDevWDSLinkStsPktsRxNSS2VHTMCS8_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 5, 4, 1, 49),
    _CoDevWDSLinkStsPktsRxNSS2VHTMCS8_Type()
)
coDevWDSLinkStsPktsRxNSS2VHTMCS8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWDSLinkStsPktsRxNSS2VHTMCS8.setStatus("current")
_CoDevWDSLinkStsPktsRxNSS2VHTMCS9_Type = Counter32
_CoDevWDSLinkStsPktsRxNSS2VHTMCS9_Object = MibTableColumn
coDevWDSLinkStsPktsRxNSS2VHTMCS9 = _CoDevWDSLinkStsPktsRxNSS2VHTMCS9_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 5, 4, 1, 50),
    _CoDevWDSLinkStsPktsRxNSS2VHTMCS9_Type()
)
coDevWDSLinkStsPktsRxNSS2VHTMCS9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWDSLinkStsPktsRxNSS2VHTMCS9.setStatus("current")
_CoDevWDSLinkStsPktsRxNSS3VHTMCS0_Type = Counter32
_CoDevWDSLinkStsPktsRxNSS3VHTMCS0_Object = MibTableColumn
coDevWDSLinkStsPktsRxNSS3VHTMCS0 = _CoDevWDSLinkStsPktsRxNSS3VHTMCS0_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 5, 4, 1, 51),
    _CoDevWDSLinkStsPktsRxNSS3VHTMCS0_Type()
)
coDevWDSLinkStsPktsRxNSS3VHTMCS0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWDSLinkStsPktsRxNSS3VHTMCS0.setStatus("current")
_CoDevWDSLinkStsPktsRxNSS3VHTMCS1_Type = Counter32
_CoDevWDSLinkStsPktsRxNSS3VHTMCS1_Object = MibTableColumn
coDevWDSLinkStsPktsRxNSS3VHTMCS1 = _CoDevWDSLinkStsPktsRxNSS3VHTMCS1_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 5, 4, 1, 52),
    _CoDevWDSLinkStsPktsRxNSS3VHTMCS1_Type()
)
coDevWDSLinkStsPktsRxNSS3VHTMCS1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWDSLinkStsPktsRxNSS3VHTMCS1.setStatus("current")
_CoDevWDSLinkStsPktsRxNSS3VHTMCS2_Type = Counter32
_CoDevWDSLinkStsPktsRxNSS3VHTMCS2_Object = MibTableColumn
coDevWDSLinkStsPktsRxNSS3VHTMCS2 = _CoDevWDSLinkStsPktsRxNSS3VHTMCS2_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 5, 4, 1, 53),
    _CoDevWDSLinkStsPktsRxNSS3VHTMCS2_Type()
)
coDevWDSLinkStsPktsRxNSS3VHTMCS2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWDSLinkStsPktsRxNSS3VHTMCS2.setStatus("current")
_CoDevWDSLinkStsPktsRxNSS3VHTMCS3_Type = Counter32
_CoDevWDSLinkStsPktsRxNSS3VHTMCS3_Object = MibTableColumn
coDevWDSLinkStsPktsRxNSS3VHTMCS3 = _CoDevWDSLinkStsPktsRxNSS3VHTMCS3_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 5, 4, 1, 54),
    _CoDevWDSLinkStsPktsRxNSS3VHTMCS3_Type()
)
coDevWDSLinkStsPktsRxNSS3VHTMCS3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWDSLinkStsPktsRxNSS3VHTMCS3.setStatus("current")
_CoDevWDSLinkStsPktsRxNSS3VHTMCS4_Type = Counter32
_CoDevWDSLinkStsPktsRxNSS3VHTMCS4_Object = MibTableColumn
coDevWDSLinkStsPktsRxNSS3VHTMCS4 = _CoDevWDSLinkStsPktsRxNSS3VHTMCS4_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 5, 4, 1, 55),
    _CoDevWDSLinkStsPktsRxNSS3VHTMCS4_Type()
)
coDevWDSLinkStsPktsRxNSS3VHTMCS4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWDSLinkStsPktsRxNSS3VHTMCS4.setStatus("current")
_CoDevWDSLinkStsPktsRxNSS3VHTMCS5_Type = Counter32
_CoDevWDSLinkStsPktsRxNSS3VHTMCS5_Object = MibTableColumn
coDevWDSLinkStsPktsRxNSS3VHTMCS5 = _CoDevWDSLinkStsPktsRxNSS3VHTMCS5_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 5, 4, 1, 56),
    _CoDevWDSLinkStsPktsRxNSS3VHTMCS5_Type()
)
coDevWDSLinkStsPktsRxNSS3VHTMCS5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWDSLinkStsPktsRxNSS3VHTMCS5.setStatus("current")
_CoDevWDSLinkStsPktsRxNSS3VHTMCS6_Type = Counter32
_CoDevWDSLinkStsPktsRxNSS3VHTMCS6_Object = MibTableColumn
coDevWDSLinkStsPktsRxNSS3VHTMCS6 = _CoDevWDSLinkStsPktsRxNSS3VHTMCS6_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 5, 4, 1, 57),
    _CoDevWDSLinkStsPktsRxNSS3VHTMCS6_Type()
)
coDevWDSLinkStsPktsRxNSS3VHTMCS6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWDSLinkStsPktsRxNSS3VHTMCS6.setStatus("current")
_CoDevWDSLinkStsPktsRxNSS3VHTMCS7_Type = Counter32
_CoDevWDSLinkStsPktsRxNSS3VHTMCS7_Object = MibTableColumn
coDevWDSLinkStsPktsRxNSS3VHTMCS7 = _CoDevWDSLinkStsPktsRxNSS3VHTMCS7_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 5, 4, 1, 58),
    _CoDevWDSLinkStsPktsRxNSS3VHTMCS7_Type()
)
coDevWDSLinkStsPktsRxNSS3VHTMCS7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWDSLinkStsPktsRxNSS3VHTMCS7.setStatus("current")
_CoDevWDSLinkStsPktsRxNSS3VHTMCS8_Type = Counter32
_CoDevWDSLinkStsPktsRxNSS3VHTMCS8_Object = MibTableColumn
coDevWDSLinkStsPktsRxNSS3VHTMCS8 = _CoDevWDSLinkStsPktsRxNSS3VHTMCS8_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 5, 4, 1, 59),
    _CoDevWDSLinkStsPktsRxNSS3VHTMCS8_Type()
)
coDevWDSLinkStsPktsRxNSS3VHTMCS8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWDSLinkStsPktsRxNSS3VHTMCS8.setStatus("current")
_CoDevWDSLinkStsPktsRxNSS3VHTMCS9_Type = Counter32
_CoDevWDSLinkStsPktsRxNSS3VHTMCS9_Object = MibTableColumn
coDevWDSLinkStsPktsRxNSS3VHTMCS9 = _CoDevWDSLinkStsPktsRxNSS3VHTMCS9_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 5, 4, 1, 60),
    _CoDevWDSLinkStsPktsRxNSS3VHTMCS9_Type()
)
coDevWDSLinkStsPktsRxNSS3VHTMCS9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWDSLinkStsPktsRxNSS3VHTMCS9.setStatus("current")
_CoDeviceWDSNetworkScanGroup_ObjectIdentity = ObjectIdentity
coDeviceWDSNetworkScanGroup = _CoDeviceWDSNetworkScanGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 6)
)
_CoDeviceWDSNetworkScanTable_Object = MibTable
coDeviceWDSNetworkScanTable = _CoDeviceWDSNetworkScanTable_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 6, 1)
)
if mibBuilder.loadTexts:
    coDeviceWDSNetworkScanTable.setStatus("current")
_CoDeviceWDSNetworkScanEntry_Object = MibTableRow
coDeviceWDSNetworkScanEntry = _CoDeviceWDSNetworkScanEntry_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 6, 1, 1)
)
coDeviceWDSNetworkScanEntry.setIndexNames(
    (0, "COLUBRIS-DEVICE-MIB", "coDevDisIndex"),
    (0, "COLUBRIS-DEVICE-WDS-MIB", "coDevWDSScanRadioIndex"),
    (0, "COLUBRIS-DEVICE-WDS-MIB", "coDevWDSScanPeerIndex"),
)
if mibBuilder.loadTexts:
    coDeviceWDSNetworkScanEntry.setStatus("current")


class _CoDevWDSScanRadioIndex_Type(Integer32):
    """Custom type coDevWDSScanRadioIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_CoDevWDSScanRadioIndex_Type.__name__ = "Integer32"
_CoDevWDSScanRadioIndex_Object = MibTableColumn
coDevWDSScanRadioIndex = _CoDevWDSScanRadioIndex_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 6, 1, 1, 1),
    _CoDevWDSScanRadioIndex_Type()
)
coDevWDSScanRadioIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    coDevWDSScanRadioIndex.setStatus("current")


class _CoDevWDSScanPeerIndex_Type(Integer32):
    """Custom type coDevWDSScanPeerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_CoDevWDSScanPeerIndex_Type.__name__ = "Integer32"
_CoDevWDSScanPeerIndex_Object = MibTableColumn
coDevWDSScanPeerIndex = _CoDevWDSScanPeerIndex_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 6, 1, 1, 2),
    _CoDevWDSScanPeerIndex_Type()
)
coDevWDSScanPeerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    coDevWDSScanPeerIndex.setStatus("current")
_CoDevWDSScanGroupId_Type = Unsigned32
_CoDevWDSScanGroupId_Object = MibTableColumn
coDevWDSScanGroupId = _CoDevWDSScanGroupId_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 6, 1, 1, 3),
    _CoDevWDSScanGroupId_Type()
)
coDevWDSScanGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWDSScanGroupId.setStatus("current")
_CoDevWDSScanPeerMacAddress_Type = MacAddress
_CoDevWDSScanPeerMacAddress_Object = MibTableColumn
coDevWDSScanPeerMacAddress = _CoDevWDSScanPeerMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 6, 1, 1, 4),
    _CoDevWDSScanPeerMacAddress_Type()
)
coDevWDSScanPeerMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWDSScanPeerMacAddress.setStatus("current")


class _CoDevWDSScanChannel_Type(Unsigned32):
    """Custom type coDevWDSScanChannel based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 199),
    )


_CoDevWDSScanChannel_Type.__name__ = "Unsigned32"
_CoDevWDSScanChannel_Object = MibTableColumn
coDevWDSScanChannel = _CoDevWDSScanChannel_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 6, 1, 1, 5),
    _CoDevWDSScanChannel_Type()
)
coDevWDSScanChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWDSScanChannel.setStatus("current")


class _CoDevWDSScanSNR_Type(Integer32):
    """Custom type coDevWDSScanSNR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 92),
    )


_CoDevWDSScanSNR_Type.__name__ = "Integer32"
_CoDevWDSScanSNR_Object = MibTableColumn
coDevWDSScanSNR = _CoDevWDSScanSNR_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 6, 1, 1, 6),
    _CoDevWDSScanSNR_Type()
)
coDevWDSScanSNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWDSScanSNR.setStatus("current")
if mibBuilder.loadTexts:
    coDevWDSScanSNR.setUnits("dBm")


class _CoDevWDSScanMode_Type(Integer32):
    """Custom type coDevWDSScanMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("master", 1),
          ("slave", 2),
          ("alternateMaster", 3))
    )


_CoDevWDSScanMode_Type.__name__ = "Integer32"
_CoDevWDSScanMode_Object = MibTableColumn
coDevWDSScanMode = _CoDevWDSScanMode_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 6, 1, 1, 7),
    _CoDevWDSScanMode_Type()
)
coDevWDSScanMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWDSScanMode.setStatus("current")
_CoDevWDSScanAvailable_Type = TruthValue
_CoDevWDSScanAvailable_Object = MibTableColumn
coDevWDSScanAvailable = _CoDevWDSScanAvailable_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 6, 1, 1, 8),
    _CoDevWDSScanAvailable_Type()
)
coDevWDSScanAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevWDSScanAvailable.setStatus("current")
_ColubrisDeviceWdsMIBNotificationPrefix_ObjectIdentity = ObjectIdentity
colubrisDeviceWdsMIBNotificationPrefix = _ColubrisDeviceWdsMIBNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 5, 34, 2)
)
_ColubrisDeviceWdsMIBNotifications_ObjectIdentity = ObjectIdentity
colubrisDeviceWdsMIBNotifications = _ColubrisDeviceWdsMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 5, 34, 2, 0)
)
_ColubrisDeviceWdsMIBConformance_ObjectIdentity = ObjectIdentity
colubrisDeviceWdsMIBConformance = _ColubrisDeviceWdsMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 5, 34, 3)
)
_ColubrisDeviceWdsMIBCompliances_ObjectIdentity = ObjectIdentity
colubrisDeviceWdsMIBCompliances = _ColubrisDeviceWdsMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 5, 34, 3, 1)
)
_ColubrisDeviceWdsMIBGroups_ObjectIdentity = ObjectIdentity
colubrisDeviceWdsMIBGroups = _ColubrisDeviceWdsMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 5, 34, 3, 2)
)
coDeviceWDSLinkStatusEntry.registerAugmentions(
    ("COLUBRIS-DEVICE-WDS-MIB",
     "coDeviceWDSLinkStatsRatesEntry")
)
coDeviceWDSLinkStatsRatesEntry.setIndexNames(*coDeviceWDSLinkStatusEntry.getIndexNames())
coDeviceWDSLinkStatusEntry.registerAugmentions(
    ("COLUBRIS-DEVICE-WDS-MIB",
     "coDeviceWDSLinkStatsHTRatesEntry")
)
coDeviceWDSLinkStatsHTRatesEntry.setIndexNames(*coDeviceWDSLinkStatusEntry.getIndexNames())
coDeviceWDSLinkStatusEntry.registerAugmentions(
    ("COLUBRIS-DEVICE-WDS-MIB",
     "coDeviceWDSLinkStatsVHTRatesEntry")
)
coDeviceWDSLinkStatsVHTRatesEntry.setIndexNames(*coDeviceWDSLinkStatusEntry.getIndexNames())

# Managed Objects groups

colubrisDeviceWdsInfoMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8744, 5, 34, 3, 2, 1)
)
colubrisDeviceWdsInfoMIBGroup.setObjects(
    ("COLUBRIS-DEVICE-WDS-MIB", "coDevWDSInfoMaxNumberOfGroup")
)
if mibBuilder.loadTexts:
    colubrisDeviceWdsInfoMIBGroup.setStatus("current")

colubrisDeviceWdsRadioMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8744, 5, 34, 3, 2, 2)
)
colubrisDeviceWdsRadioMIBGroup.setObjects(
      *(("COLUBRIS-DEVICE-WDS-MIB", "coDevWDSRadioAckDistance"),
        ("COLUBRIS-DEVICE-WDS-MIB", "coDevWDSRadioQoS"))
)
if mibBuilder.loadTexts:
    colubrisDeviceWdsRadioMIBGroup.setStatus("current")

colubrisDeviceWdsGroupMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8744, 5, 34, 3, 2, 3)
)
colubrisDeviceWdsGroupMIBGroup.setObjects(
      *(("COLUBRIS-DEVICE-WDS-MIB", "coDevWDSGroupName"),
        ("COLUBRIS-DEVICE-WDS-MIB", "coDevWDSGroupState"),
        ("COLUBRIS-DEVICE-WDS-MIB", "coDevWDSGroupSecurity"),
        ("COLUBRIS-DEVICE-WDS-MIB", "coDevWDSGroupDynamicMode"),
        ("COLUBRIS-DEVICE-WDS-MIB", "coDevWDSGroupDynamicGroupId"))
)
if mibBuilder.loadTexts:
    colubrisDeviceWdsGroupMIBGroup.setStatus("current")

colubrisDeviceWdsLinkMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8744, 5, 34, 3, 2, 4)
)
colubrisDeviceWdsLinkMIBGroup.setObjects(
      *(("COLUBRIS-DEVICE-WDS-MIB", "coDevWDSLinkStaState"),
        ("COLUBRIS-DEVICE-WDS-MIB", "coDevWDSLinkStaRadio"),
        ("COLUBRIS-DEVICE-WDS-MIB", "coDevWDSLinkStaPeerMacAddress"),
        ("COLUBRIS-DEVICE-WDS-MIB", "coDevWDSLinkStaMaster"),
        ("COLUBRIS-DEVICE-WDS-MIB", "coDevWDSLinkStaAuthorized"),
        ("COLUBRIS-DEVICE-WDS-MIB", "coDevWDSLinkStaEncryption"),
        ("COLUBRIS-DEVICE-WDS-MIB", "coDevWDSLinkStaIdleTime"),
        ("COLUBRIS-DEVICE-WDS-MIB", "coDevWDSLinkStaSNR"),
        ("COLUBRIS-DEVICE-WDS-MIB", "coDevWDSLinkStaTxRate"),
        ("COLUBRIS-DEVICE-WDS-MIB", "coDevWDSLinkStaRxRate"),
        ("COLUBRIS-DEVICE-WDS-MIB", "coDevWDSLinkStaIfIndex"),
        ("COLUBRIS-DEVICE-WDS-MIB", "coDevWDSLinkStaHT"),
        ("COLUBRIS-DEVICE-WDS-MIB", "coDevWDSLinkStaTxMCS"),
        ("COLUBRIS-DEVICE-WDS-MIB", "coDevWDSLinkStaRxMCS"),
        ("COLUBRIS-DEVICE-WDS-MIB", "coDevWDSLinkStaSignal"),
        ("COLUBRIS-DEVICE-WDS-MIB", "coDevWDSLinkStaNoise"),
        ("COLUBRIS-DEVICE-WDS-MIB", "coDevWDSLinkStaVHT"),
        ("COLUBRIS-DEVICE-WDS-MIB", "coDevWDSLinkStsPktsTxRate1"),
        ("COLUBRIS-DEVICE-WDS-MIB", "coDevWDSLinkStsPktsTxRate2"),
        ("COLUBRIS-DEVICE-WDS-MIB", "coDevWDSLinkStsPktsTxRate5dot5"),
        ("COLUBRIS-DEVICE-WDS-MIB", "coDevWDSLinkStsPktsTxRate11"),
        ("COLUBRIS-DEVICE-WDS-MIB", "coDevWDSLinkStsPktsTxRate6"),
        ("COLUBRIS-DEVICE-WDS-MIB", "coDevWDSLinkStsPktsTxRate9"),
        ("COLUBRIS-DEVICE-WDS-MIB", "coDevWDSLinkStsPktsTxRate12"),
        ("COLUBRIS-DEVICE-WDS-MIB", "coDevWDSLinkStsPktsTxRate18"),
        ("COLUBRIS-DEVICE-WDS-MIB", "coDevWDSLinkStsPktsTxRate24"),
        ("COLUBRIS-DEVICE-WDS-MIB", "coDevWDSLinkStsPktsTxRate36"),
        ("COLUBRIS-DEVICE-WDS-MIB", "coDevWDSLinkStsPktsTxRate48"),
        ("COLUBRIS-DEVICE-WDS-MIB", "coDevWDSLinkStsPktsTxRate54"),
        ("COLUBRIS-DEVICE-WDS-MIB", "coDevWDSLinkStsPktsRxRate1"),
        ("COLUBRIS-DEVICE-WDS-MIB", "coDevWDSLinkStsPktsRxRate2"),
        ("COLUBRIS-DEVICE-WDS-MIB", "coDevWDSLinkStsPktsRxRate5dot5"),
        ("COLUBRIS-DEVICE-WDS-MIB", "coDevWDSLinkStsPktsRxRate11"),
        ("COLUBRIS-DEVICE-WDS-MIB", "coDevWDSLinkStsPktsRxRate6"),
        ("COLUBRIS-DEVICE-WDS-MIB", "coDevWDSLinkStsPktsRxRate9"),
        ("COLUBRIS-DEVICE-WDS-MIB", "coDevWDSLinkStsPktsRxRate12"),
        ("COLUBRIS-DEVICE-WDS-MIB", "coDevWDSLinkStsPktsRxRate18"),
        ("COLUBRIS-DEVICE-WDS-MIB", "coDevWDSLinkStsPktsRxRate24"),
        ("COLUBRIS-DEVICE-WDS-MIB", "coDevWDSLinkStsPktsRxRate36"),
        ("COLUBRIS-DEVICE-WDS-MIB", "coDevWDSLinkStsPktsRxRate48"),
        ("COLUBRIS-DEVICE-WDS-MIB", "coDevWDSLinkStsPktsRxRate54"),
        ("COLUBRIS-DEVICE-WDS-MIB", "coDevWDSLinkStsPktsTxMCS0"),
        ("COLUBRIS-DEVICE-WDS-MIB", "coDevWDSLinkStsPktsTxMCS1"),
        ("COLUBRIS-DEVICE-WDS-MIB", "coDevWDSLinkStsPktsTxMCS2"),
        ("COLUBRIS-DEVICE-WDS-MIB", "coDevWDSLinkStsPktsTxMCS3"),
        ("COLUBRIS-DEVICE-WDS-MIB", "coDevWDSLinkStsPktsTxMCS4"),
        ("COLUBRIS-DEVICE-WDS-MIB", "coDevWDSLinkStsPktsTxMCS5"),
        ("COLUBRIS-DEVICE-WDS-MIB", "coDevWDSLinkStsPktsTxMCS6"),
        ("COLUBRIS-DEVICE-WDS-MIB", "coDevWDSLinkStsPktsTxMCS7"),
        ("COLUBRIS-DEVICE-WDS-MIB", "coDevWDSLinkStsPktsTxMCS8"),
        ("COLUBRIS-DEVICE-WDS-MIB", "coDevWDSLinkStsPktsTxMCS9"),
        ("COLUBRIS-DEVICE-WDS-MIB", "coDevWDSLinkStsPktsTxMCS10"),
        ("COLUBRIS-DEVICE-WDS-MIB", "coDevWDSLinkStsPktsTxMCS11"),
        ("COLUBRIS-DEVICE-WDS-MIB", "coDevWDSLinkStsPktsTxMCS12"),
        ("COLUBRIS-DEVICE-WDS-MIB", "coDevWDSLinkStsPktsTxMCS13"),
        ("COLUBRIS-DEVICE-WDS-MIB", "coDevWDSLinkStsPktsTxMCS14"),
        ("COLUBRIS-DEVICE-WDS-MIB", "coDevWDSLinkStsPktsTxMCS15"),
        ("COLUBRIS-DEVICE-WDS-MIB", "coDevWDSLinkStsPktsRxMCS0"),
        ("COLUBRIS-DEVICE-WDS-MIB", "coDevWDSLinkStsPktsRxMCS1"),
        ("COLUBRIS-DEVICE-WDS-MIB", "coDevWDSLinkStsPktsRxMCS2"),
        ("COLUBRIS-DEVICE-WDS-MIB", "coDevWDSLinkStsPktsRxMCS3"),
        ("COLUBRIS-DEVICE-WDS-MIB", "coDevWDSLinkStsPktsRxMCS4"),
        ("COLUBRIS-DEVICE-WDS-MIB", "coDevWDSLinkStsPktsRxMCS5"),
        ("COLUBRIS-DEVICE-WDS-MIB", "coDevWDSLinkStsPktsRxMCS6"),
        ("COLUBRIS-DEVICE-WDS-MIB", "coDevWDSLinkStsPktsRxMCS7"),
        ("COLUBRIS-DEVICE-WDS-MIB", "coDevWDSLinkStsPktsRxMCS8"),
        ("COLUBRIS-DEVICE-WDS-MIB", "coDevWDSLinkStsPktsRxMCS9"),
        ("COLUBRIS-DEVICE-WDS-MIB", "coDevWDSLinkStsPktsRxMCS10"),
        ("COLUBRIS-DEVICE-WDS-MIB", "coDevWDSLinkStsPktsRxMCS11"),
        ("COLUBRIS-DEVICE-WDS-MIB", "coDevWDSLinkStsPktsRxMCS12"),
        ("COLUBRIS-DEVICE-WDS-MIB", "coDevWDSLinkStsPktsRxMCS13"),
        ("COLUBRIS-DEVICE-WDS-MIB", "coDevWDSLinkStsPktsRxMCS14"),
        ("COLUBRIS-DEVICE-WDS-MIB", "coDevWDSLinkStsPktsRxMCS15"),
        ("COLUBRIS-DEVICE-WDS-MIB", "coDevWDSLinkStsPktsTxNSS1VHTMCS0"),
        ("COLUBRIS-DEVICE-WDS-MIB", "coDevWDSLinkStsPktsTxNSS1VHTMCS1"),
        ("COLUBRIS-DEVICE-WDS-MIB", "coDevWDSLinkStsPktsTxNSS1VHTMCS2"),
        ("COLUBRIS-DEVICE-WDS-MIB", "coDevWDSLinkStsPktsTxNSS1VHTMCS3"),
        ("COLUBRIS-DEVICE-WDS-MIB", "coDevWDSLinkStsPktsTxNSS1VHTMCS4"),
        ("COLUBRIS-DEVICE-WDS-MIB", "coDevWDSLinkStsPktsTxNSS1VHTMCS5"),
        ("COLUBRIS-DEVICE-WDS-MIB", "coDevWDSLinkStsPktsTxNSS1VHTMCS6"),
        ("COLUBRIS-DEVICE-WDS-MIB", "coDevWDSLinkStsPktsTxNSS1VHTMCS7"),
        ("COLUBRIS-DEVICE-WDS-MIB", "coDevWDSLinkStsPktsTxNSS1VHTMCS8"),
        ("COLUBRIS-DEVICE-WDS-MIB", "coDevWDSLinkStsPktsTxNSS1VHTMCS9"),
        ("COLUBRIS-DEVICE-WDS-MIB", "coDevWDSLinkStsPktsTxNSS2VHTMCS0"),
        ("COLUBRIS-DEVICE-WDS-MIB", "coDevWDSLinkStsPktsTxNSS2VHTMCS1"),
        ("COLUBRIS-DEVICE-WDS-MIB", "coDevWDSLinkStsPktsTxNSS2VHTMCS2"),
        ("COLUBRIS-DEVICE-WDS-MIB", "coDevWDSLinkStsPktsTxNSS2VHTMCS3"),
        ("COLUBRIS-DEVICE-WDS-MIB", "coDevWDSLinkStsPktsTxNSS2VHTMCS4"),
        ("COLUBRIS-DEVICE-WDS-MIB", "coDevWDSLinkStsPktsTxNSS2VHTMCS5"),
        ("COLUBRIS-DEVICE-WDS-MIB", "coDevWDSLinkStsPktsTxNSS2VHTMCS6"),
        ("COLUBRIS-DEVICE-WDS-MIB", "coDevWDSLinkStsPktsTxNSS2VHTMCS7"),
        ("COLUBRIS-DEVICE-WDS-MIB", "coDevWDSLinkStsPktsTxNSS2VHTMCS8"),
        ("COLUBRIS-DEVICE-WDS-MIB", "coDevWDSLinkStsPktsTxNSS2VHTMCS9"),
        ("COLUBRIS-DEVICE-WDS-MIB", "coDevWDSLinkStsPktsTxNSS3VHTMCS0"),
        ("COLUBRIS-DEVICE-WDS-MIB", "coDevWDSLinkStsPktsTxNSS3VHTMCS1"),
        ("COLUBRIS-DEVICE-WDS-MIB", "coDevWDSLinkStsPktsTxNSS3VHTMCS2"),
        ("COLUBRIS-DEVICE-WDS-MIB", "coDevWDSLinkStsPktsTxNSS3VHTMCS3"),
        ("COLUBRIS-DEVICE-WDS-MIB", "coDevWDSLinkStsPktsTxNSS3VHTMCS4"),
        ("COLUBRIS-DEVICE-WDS-MIB", "coDevWDSLinkStsPktsTxNSS3VHTMCS5"),
        ("COLUBRIS-DEVICE-WDS-MIB", "coDevWDSLinkStsPktsTxNSS3VHTMCS6"),
        ("COLUBRIS-DEVICE-WDS-MIB", "coDevWDSLinkStsPktsTxNSS3VHTMCS7"),
        ("COLUBRIS-DEVICE-WDS-MIB", "coDevWDSLinkStsPktsTxNSS3VHTMCS8"),
        ("COLUBRIS-DEVICE-WDS-MIB", "coDevWDSLinkStsPktsTxNSS3VHTMCS9"),
        ("COLUBRIS-DEVICE-WDS-MIB", "coDevWDSLinkStsPktsRxNSS1VHTMCS0"),
        ("COLUBRIS-DEVICE-WDS-MIB", "coDevWDSLinkStsPktsRxNSS1VHTMCS1"),
        ("COLUBRIS-DEVICE-WDS-MIB", "coDevWDSLinkStsPktsRxNSS1VHTMCS2"),
        ("COLUBRIS-DEVICE-WDS-MIB", "coDevWDSLinkStsPktsRxNSS1VHTMCS3"),
        ("COLUBRIS-DEVICE-WDS-MIB", "coDevWDSLinkStsPktsRxNSS1VHTMCS4"),
        ("COLUBRIS-DEVICE-WDS-MIB", "coDevWDSLinkStsPktsRxNSS1VHTMCS5"),
        ("COLUBRIS-DEVICE-WDS-MIB", "coDevWDSLinkStsPktsRxNSS1VHTMCS6"),
        ("COLUBRIS-DEVICE-WDS-MIB", "coDevWDSLinkStsPktsRxNSS1VHTMCS7"),
        ("COLUBRIS-DEVICE-WDS-MIB", "coDevWDSLinkStsPktsRxNSS1VHTMCS8"),
        ("COLUBRIS-DEVICE-WDS-MIB", "coDevWDSLinkStsPktsRxNSS1VHTMCS9"),
        ("COLUBRIS-DEVICE-WDS-MIB", "coDevWDSLinkStsPktsRxNSS2VHTMCS0"),
        ("COLUBRIS-DEVICE-WDS-MIB", "coDevWDSLinkStsPktsRxNSS2VHTMCS1"),
        ("COLUBRIS-DEVICE-WDS-MIB", "coDevWDSLinkStsPktsRxNSS2VHTMCS2"),
        ("COLUBRIS-DEVICE-WDS-MIB", "coDevWDSLinkStsPktsRxNSS2VHTMCS3"),
        ("COLUBRIS-DEVICE-WDS-MIB", "coDevWDSLinkStsPktsRxNSS2VHTMCS4"),
        ("COLUBRIS-DEVICE-WDS-MIB", "coDevWDSLinkStsPktsRxNSS2VHTMCS5"),
        ("COLUBRIS-DEVICE-WDS-MIB", "coDevWDSLinkStsPktsRxNSS2VHTMCS6"),
        ("COLUBRIS-DEVICE-WDS-MIB", "coDevWDSLinkStsPktsRxNSS2VHTMCS7"),
        ("COLUBRIS-DEVICE-WDS-MIB", "coDevWDSLinkStsPktsRxNSS2VHTMCS8"),
        ("COLUBRIS-DEVICE-WDS-MIB", "coDevWDSLinkStsPktsRxNSS2VHTMCS9"),
        ("COLUBRIS-DEVICE-WDS-MIB", "coDevWDSLinkStsPktsRxNSS3VHTMCS0"),
        ("COLUBRIS-DEVICE-WDS-MIB", "coDevWDSLinkStsPktsRxNSS3VHTMCS1"),
        ("COLUBRIS-DEVICE-WDS-MIB", "coDevWDSLinkStsPktsRxNSS3VHTMCS2"),
        ("COLUBRIS-DEVICE-WDS-MIB", "coDevWDSLinkStsPktsRxNSS3VHTMCS3"),
        ("COLUBRIS-DEVICE-WDS-MIB", "coDevWDSLinkStsPktsRxNSS3VHTMCS4"),
        ("COLUBRIS-DEVICE-WDS-MIB", "coDevWDSLinkStsPktsRxNSS3VHTMCS5"),
        ("COLUBRIS-DEVICE-WDS-MIB", "coDevWDSLinkStsPktsRxNSS3VHTMCS6"),
        ("COLUBRIS-DEVICE-WDS-MIB", "coDevWDSLinkStsPktsRxNSS3VHTMCS7"),
        ("COLUBRIS-DEVICE-WDS-MIB", "coDevWDSLinkStsPktsRxNSS3VHTMCS8"),
        ("COLUBRIS-DEVICE-WDS-MIB", "coDevWDSLinkStsPktsRxNSS3VHTMCS9"))
)
if mibBuilder.loadTexts:
    colubrisDeviceWdsLinkMIBGroup.setStatus("current")

colubrisDeviceWdsNetworkScanMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8744, 5, 34, 3, 2, 5)
)
colubrisDeviceWdsNetworkScanMIBGroup.setObjects(
      *(("COLUBRIS-DEVICE-WDS-MIB", "coDevWDSScanGroupId"),
        ("COLUBRIS-DEVICE-WDS-MIB", "coDevWDSScanPeerMacAddress"),
        ("COLUBRIS-DEVICE-WDS-MIB", "coDevWDSScanChannel"),
        ("COLUBRIS-DEVICE-WDS-MIB", "coDevWDSScanSNR"),
        ("COLUBRIS-DEVICE-WDS-MIB", "coDevWDSScanMode"),
        ("COLUBRIS-DEVICE-WDS-MIB", "coDevWDSScanAvailable"))
)
if mibBuilder.loadTexts:
    colubrisDeviceWdsNetworkScanMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

colubrisDeviceWdsMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8744, 5, 34, 3, 1, 1)
)
colubrisDeviceWdsMIBCompliance.setObjects(
      *(("COLUBRIS-DEVICE-WDS-MIB", "colubrisDeviceWdsInfoMIBGroup"),
        ("COLUBRIS-DEVICE-WDS-MIB", "colubrisDeviceWdsRadioMIBGroup"),
        ("COLUBRIS-DEVICE-WDS-MIB", "colubrisDeviceWdsGroupMIBGroup"),
        ("COLUBRIS-DEVICE-WDS-MIB", "colubrisDeviceWdsLinkMIBGroup"),
        ("COLUBRIS-DEVICE-WDS-MIB", "colubrisDeviceWdsNetworkScanMIBGroup"))
)
if mibBuilder.loadTexts:
    colubrisDeviceWdsMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "COLUBRIS-DEVICE-WDS-MIB",
    **{"colubrisDeviceWdsMIB": colubrisDeviceWdsMIB,
       "colubrisDeviceWdsMIBObjects": colubrisDeviceWdsMIBObjects,
       "coDeviceWDSInfoGroup": coDeviceWDSInfoGroup,
       "coDeviceWdsInfoTable": coDeviceWdsInfoTable,
       "coDeviceWdsInfoEntry": coDeviceWdsInfoEntry,
       "coDevWDSInfoMaxNumberOfGroup": coDevWDSInfoMaxNumberOfGroup,
       "coDeviceWDSRadioGroup": coDeviceWDSRadioGroup,
       "coDeviceWDSRadioTable": coDeviceWDSRadioTable,
       "coDeviceWDSRadioEntry": coDeviceWDSRadioEntry,
       "coDevWDSRadioIndex": coDevWDSRadioIndex,
       "coDevWDSRadioAckDistance": coDevWDSRadioAckDistance,
       "coDevWDSRadioQoS": coDevWDSRadioQoS,
       "coDeviceWDSGroupGroup": coDeviceWDSGroupGroup,
       "coDeviceWDSGroupTable": coDeviceWDSGroupTable,
       "coDeviceWDSGroupEntry": coDeviceWDSGroupEntry,
       "coDevWDSGroupIndex": coDevWDSGroupIndex,
       "coDevWDSGroupName": coDevWDSGroupName,
       "coDevWDSGroupState": coDevWDSGroupState,
       "coDevWDSGroupSecurity": coDevWDSGroupSecurity,
       "coDevWDSGroupDynamicMode": coDevWDSGroupDynamicMode,
       "coDevWDSGroupDynamicGroupId": coDevWDSGroupDynamicGroupId,
       "coDeviceWDSLinkGroup": coDeviceWDSLinkGroup,
       "coDeviceWDSLinkStatusTable": coDeviceWDSLinkStatusTable,
       "coDeviceWDSLinkStatusEntry": coDeviceWDSLinkStatusEntry,
       "coDevWDSLinkStaIndex": coDevWDSLinkStaIndex,
       "coDevWDSLinkStaState": coDevWDSLinkStaState,
       "coDevWDSLinkStaRadio": coDevWDSLinkStaRadio,
       "coDevWDSLinkStaPeerMacAddress": coDevWDSLinkStaPeerMacAddress,
       "coDevWDSLinkStaMaster": coDevWDSLinkStaMaster,
       "coDevWDSLinkStaAuthorized": coDevWDSLinkStaAuthorized,
       "coDevWDSLinkStaEncryption": coDevWDSLinkStaEncryption,
       "coDevWDSLinkStaIdleTime": coDevWDSLinkStaIdleTime,
       "coDevWDSLinkStaSNR": coDevWDSLinkStaSNR,
       "coDevWDSLinkStaTxRate": coDevWDSLinkStaTxRate,
       "coDevWDSLinkStaRxRate": coDevWDSLinkStaRxRate,
       "coDevWDSLinkStaIfIndex": coDevWDSLinkStaIfIndex,
       "coDevWDSLinkStaHT": coDevWDSLinkStaHT,
       "coDevWDSLinkStaTxMCS": coDevWDSLinkStaTxMCS,
       "coDevWDSLinkStaRxMCS": coDevWDSLinkStaRxMCS,
       "coDevWDSLinkStaSignal": coDevWDSLinkStaSignal,
       "coDevWDSLinkStaNoise": coDevWDSLinkStaNoise,
       "coDevWDSLinkStaVHT": coDevWDSLinkStaVHT,
       "coDeviceWDSLinkStatsRatesTable": coDeviceWDSLinkStatsRatesTable,
       "coDeviceWDSLinkStatsRatesEntry": coDeviceWDSLinkStatsRatesEntry,
       "coDevWDSLinkStsPktsTxRate1": coDevWDSLinkStsPktsTxRate1,
       "coDevWDSLinkStsPktsTxRate2": coDevWDSLinkStsPktsTxRate2,
       "coDevWDSLinkStsPktsTxRate5dot5": coDevWDSLinkStsPktsTxRate5dot5,
       "coDevWDSLinkStsPktsTxRate11": coDevWDSLinkStsPktsTxRate11,
       "coDevWDSLinkStsPktsTxRate6": coDevWDSLinkStsPktsTxRate6,
       "coDevWDSLinkStsPktsTxRate9": coDevWDSLinkStsPktsTxRate9,
       "coDevWDSLinkStsPktsTxRate12": coDevWDSLinkStsPktsTxRate12,
       "coDevWDSLinkStsPktsTxRate18": coDevWDSLinkStsPktsTxRate18,
       "coDevWDSLinkStsPktsTxRate24": coDevWDSLinkStsPktsTxRate24,
       "coDevWDSLinkStsPktsTxRate36": coDevWDSLinkStsPktsTxRate36,
       "coDevWDSLinkStsPktsTxRate48": coDevWDSLinkStsPktsTxRate48,
       "coDevWDSLinkStsPktsTxRate54": coDevWDSLinkStsPktsTxRate54,
       "coDevWDSLinkStsPktsRxRate1": coDevWDSLinkStsPktsRxRate1,
       "coDevWDSLinkStsPktsRxRate2": coDevWDSLinkStsPktsRxRate2,
       "coDevWDSLinkStsPktsRxRate5dot5": coDevWDSLinkStsPktsRxRate5dot5,
       "coDevWDSLinkStsPktsRxRate11": coDevWDSLinkStsPktsRxRate11,
       "coDevWDSLinkStsPktsRxRate6": coDevWDSLinkStsPktsRxRate6,
       "coDevWDSLinkStsPktsRxRate9": coDevWDSLinkStsPktsRxRate9,
       "coDevWDSLinkStsPktsRxRate12": coDevWDSLinkStsPktsRxRate12,
       "coDevWDSLinkStsPktsRxRate18": coDevWDSLinkStsPktsRxRate18,
       "coDevWDSLinkStsPktsRxRate24": coDevWDSLinkStsPktsRxRate24,
       "coDevWDSLinkStsPktsRxRate36": coDevWDSLinkStsPktsRxRate36,
       "coDevWDSLinkStsPktsRxRate48": coDevWDSLinkStsPktsRxRate48,
       "coDevWDSLinkStsPktsRxRate54": coDevWDSLinkStsPktsRxRate54,
       "coDeviceWDSLinkStatsHTRatesTable": coDeviceWDSLinkStatsHTRatesTable,
       "coDeviceWDSLinkStatsHTRatesEntry": coDeviceWDSLinkStatsHTRatesEntry,
       "coDevWDSLinkStsPktsTxMCS0": coDevWDSLinkStsPktsTxMCS0,
       "coDevWDSLinkStsPktsTxMCS1": coDevWDSLinkStsPktsTxMCS1,
       "coDevWDSLinkStsPktsTxMCS2": coDevWDSLinkStsPktsTxMCS2,
       "coDevWDSLinkStsPktsTxMCS3": coDevWDSLinkStsPktsTxMCS3,
       "coDevWDSLinkStsPktsTxMCS4": coDevWDSLinkStsPktsTxMCS4,
       "coDevWDSLinkStsPktsTxMCS5": coDevWDSLinkStsPktsTxMCS5,
       "coDevWDSLinkStsPktsTxMCS6": coDevWDSLinkStsPktsTxMCS6,
       "coDevWDSLinkStsPktsTxMCS7": coDevWDSLinkStsPktsTxMCS7,
       "coDevWDSLinkStsPktsTxMCS8": coDevWDSLinkStsPktsTxMCS8,
       "coDevWDSLinkStsPktsTxMCS9": coDevWDSLinkStsPktsTxMCS9,
       "coDevWDSLinkStsPktsTxMCS10": coDevWDSLinkStsPktsTxMCS10,
       "coDevWDSLinkStsPktsTxMCS11": coDevWDSLinkStsPktsTxMCS11,
       "coDevWDSLinkStsPktsTxMCS12": coDevWDSLinkStsPktsTxMCS12,
       "coDevWDSLinkStsPktsTxMCS13": coDevWDSLinkStsPktsTxMCS13,
       "coDevWDSLinkStsPktsTxMCS14": coDevWDSLinkStsPktsTxMCS14,
       "coDevWDSLinkStsPktsTxMCS15": coDevWDSLinkStsPktsTxMCS15,
       "coDevWDSLinkStsPktsRxMCS0": coDevWDSLinkStsPktsRxMCS0,
       "coDevWDSLinkStsPktsRxMCS1": coDevWDSLinkStsPktsRxMCS1,
       "coDevWDSLinkStsPktsRxMCS2": coDevWDSLinkStsPktsRxMCS2,
       "coDevWDSLinkStsPktsRxMCS3": coDevWDSLinkStsPktsRxMCS3,
       "coDevWDSLinkStsPktsRxMCS4": coDevWDSLinkStsPktsRxMCS4,
       "coDevWDSLinkStsPktsRxMCS5": coDevWDSLinkStsPktsRxMCS5,
       "coDevWDSLinkStsPktsRxMCS6": coDevWDSLinkStsPktsRxMCS6,
       "coDevWDSLinkStsPktsRxMCS7": coDevWDSLinkStsPktsRxMCS7,
       "coDevWDSLinkStsPktsRxMCS8": coDevWDSLinkStsPktsRxMCS8,
       "coDevWDSLinkStsPktsRxMCS9": coDevWDSLinkStsPktsRxMCS9,
       "coDevWDSLinkStsPktsRxMCS10": coDevWDSLinkStsPktsRxMCS10,
       "coDevWDSLinkStsPktsRxMCS11": coDevWDSLinkStsPktsRxMCS11,
       "coDevWDSLinkStsPktsRxMCS12": coDevWDSLinkStsPktsRxMCS12,
       "coDevWDSLinkStsPktsRxMCS13": coDevWDSLinkStsPktsRxMCS13,
       "coDevWDSLinkStsPktsRxMCS14": coDevWDSLinkStsPktsRxMCS14,
       "coDevWDSLinkStsPktsRxMCS15": coDevWDSLinkStsPktsRxMCS15,
       "coDeviceWDSLinkStatsVHTRatesTable": coDeviceWDSLinkStatsVHTRatesTable,
       "coDeviceWDSLinkStatsVHTRatesEntry": coDeviceWDSLinkStatsVHTRatesEntry,
       "coDevWDSLinkStsPktsTxNSS1VHTMCS0": coDevWDSLinkStsPktsTxNSS1VHTMCS0,
       "coDevWDSLinkStsPktsTxNSS1VHTMCS1": coDevWDSLinkStsPktsTxNSS1VHTMCS1,
       "coDevWDSLinkStsPktsTxNSS1VHTMCS2": coDevWDSLinkStsPktsTxNSS1VHTMCS2,
       "coDevWDSLinkStsPktsTxNSS1VHTMCS3": coDevWDSLinkStsPktsTxNSS1VHTMCS3,
       "coDevWDSLinkStsPktsTxNSS1VHTMCS4": coDevWDSLinkStsPktsTxNSS1VHTMCS4,
       "coDevWDSLinkStsPktsTxNSS1VHTMCS5": coDevWDSLinkStsPktsTxNSS1VHTMCS5,
       "coDevWDSLinkStsPktsTxNSS1VHTMCS6": coDevWDSLinkStsPktsTxNSS1VHTMCS6,
       "coDevWDSLinkStsPktsTxNSS1VHTMCS7": coDevWDSLinkStsPktsTxNSS1VHTMCS7,
       "coDevWDSLinkStsPktsTxNSS1VHTMCS8": coDevWDSLinkStsPktsTxNSS1VHTMCS8,
       "coDevWDSLinkStsPktsTxNSS1VHTMCS9": coDevWDSLinkStsPktsTxNSS1VHTMCS9,
       "coDevWDSLinkStsPktsTxNSS2VHTMCS0": coDevWDSLinkStsPktsTxNSS2VHTMCS0,
       "coDevWDSLinkStsPktsTxNSS2VHTMCS1": coDevWDSLinkStsPktsTxNSS2VHTMCS1,
       "coDevWDSLinkStsPktsTxNSS2VHTMCS2": coDevWDSLinkStsPktsTxNSS2VHTMCS2,
       "coDevWDSLinkStsPktsTxNSS2VHTMCS3": coDevWDSLinkStsPktsTxNSS2VHTMCS3,
       "coDevWDSLinkStsPktsTxNSS2VHTMCS4": coDevWDSLinkStsPktsTxNSS2VHTMCS4,
       "coDevWDSLinkStsPktsTxNSS2VHTMCS5": coDevWDSLinkStsPktsTxNSS2VHTMCS5,
       "coDevWDSLinkStsPktsTxNSS2VHTMCS6": coDevWDSLinkStsPktsTxNSS2VHTMCS6,
       "coDevWDSLinkStsPktsTxNSS2VHTMCS7": coDevWDSLinkStsPktsTxNSS2VHTMCS7,
       "coDevWDSLinkStsPktsTxNSS2VHTMCS8": coDevWDSLinkStsPktsTxNSS2VHTMCS8,
       "coDevWDSLinkStsPktsTxNSS2VHTMCS9": coDevWDSLinkStsPktsTxNSS2VHTMCS9,
       "coDevWDSLinkStsPktsTxNSS3VHTMCS0": coDevWDSLinkStsPktsTxNSS3VHTMCS0,
       "coDevWDSLinkStsPktsTxNSS3VHTMCS1": coDevWDSLinkStsPktsTxNSS3VHTMCS1,
       "coDevWDSLinkStsPktsTxNSS3VHTMCS2": coDevWDSLinkStsPktsTxNSS3VHTMCS2,
       "coDevWDSLinkStsPktsTxNSS3VHTMCS3": coDevWDSLinkStsPktsTxNSS3VHTMCS3,
       "coDevWDSLinkStsPktsTxNSS3VHTMCS4": coDevWDSLinkStsPktsTxNSS3VHTMCS4,
       "coDevWDSLinkStsPktsTxNSS3VHTMCS5": coDevWDSLinkStsPktsTxNSS3VHTMCS5,
       "coDevWDSLinkStsPktsTxNSS3VHTMCS6": coDevWDSLinkStsPktsTxNSS3VHTMCS6,
       "coDevWDSLinkStsPktsTxNSS3VHTMCS7": coDevWDSLinkStsPktsTxNSS3VHTMCS7,
       "coDevWDSLinkStsPktsTxNSS3VHTMCS8": coDevWDSLinkStsPktsTxNSS3VHTMCS8,
       "coDevWDSLinkStsPktsTxNSS3VHTMCS9": coDevWDSLinkStsPktsTxNSS3VHTMCS9,
       "coDevWDSLinkStsPktsRxNSS1VHTMCS0": coDevWDSLinkStsPktsRxNSS1VHTMCS0,
       "coDevWDSLinkStsPktsRxNSS1VHTMCS1": coDevWDSLinkStsPktsRxNSS1VHTMCS1,
       "coDevWDSLinkStsPktsRxNSS1VHTMCS2": coDevWDSLinkStsPktsRxNSS1VHTMCS2,
       "coDevWDSLinkStsPktsRxNSS1VHTMCS3": coDevWDSLinkStsPktsRxNSS1VHTMCS3,
       "coDevWDSLinkStsPktsRxNSS1VHTMCS4": coDevWDSLinkStsPktsRxNSS1VHTMCS4,
       "coDevWDSLinkStsPktsRxNSS1VHTMCS5": coDevWDSLinkStsPktsRxNSS1VHTMCS5,
       "coDevWDSLinkStsPktsRxNSS1VHTMCS6": coDevWDSLinkStsPktsRxNSS1VHTMCS6,
       "coDevWDSLinkStsPktsRxNSS1VHTMCS7": coDevWDSLinkStsPktsRxNSS1VHTMCS7,
       "coDevWDSLinkStsPktsRxNSS1VHTMCS8": coDevWDSLinkStsPktsRxNSS1VHTMCS8,
       "coDevWDSLinkStsPktsRxNSS1VHTMCS9": coDevWDSLinkStsPktsRxNSS1VHTMCS9,
       "coDevWDSLinkStsPktsRxNSS2VHTMCS0": coDevWDSLinkStsPktsRxNSS2VHTMCS0,
       "coDevWDSLinkStsPktsRxNSS2VHTMCS1": coDevWDSLinkStsPktsRxNSS2VHTMCS1,
       "coDevWDSLinkStsPktsRxNSS2VHTMCS2": coDevWDSLinkStsPktsRxNSS2VHTMCS2,
       "coDevWDSLinkStsPktsRxNSS2VHTMCS3": coDevWDSLinkStsPktsRxNSS2VHTMCS3,
       "coDevWDSLinkStsPktsRxNSS2VHTMCS4": coDevWDSLinkStsPktsRxNSS2VHTMCS4,
       "coDevWDSLinkStsPktsRxNSS2VHTMCS5": coDevWDSLinkStsPktsRxNSS2VHTMCS5,
       "coDevWDSLinkStsPktsRxNSS2VHTMCS6": coDevWDSLinkStsPktsRxNSS2VHTMCS6,
       "coDevWDSLinkStsPktsRxNSS2VHTMCS7": coDevWDSLinkStsPktsRxNSS2VHTMCS7,
       "coDevWDSLinkStsPktsRxNSS2VHTMCS8": coDevWDSLinkStsPktsRxNSS2VHTMCS8,
       "coDevWDSLinkStsPktsRxNSS2VHTMCS9": coDevWDSLinkStsPktsRxNSS2VHTMCS9,
       "coDevWDSLinkStsPktsRxNSS3VHTMCS0": coDevWDSLinkStsPktsRxNSS3VHTMCS0,
       "coDevWDSLinkStsPktsRxNSS3VHTMCS1": coDevWDSLinkStsPktsRxNSS3VHTMCS1,
       "coDevWDSLinkStsPktsRxNSS3VHTMCS2": coDevWDSLinkStsPktsRxNSS3VHTMCS2,
       "coDevWDSLinkStsPktsRxNSS3VHTMCS3": coDevWDSLinkStsPktsRxNSS3VHTMCS3,
       "coDevWDSLinkStsPktsRxNSS3VHTMCS4": coDevWDSLinkStsPktsRxNSS3VHTMCS4,
       "coDevWDSLinkStsPktsRxNSS3VHTMCS5": coDevWDSLinkStsPktsRxNSS3VHTMCS5,
       "coDevWDSLinkStsPktsRxNSS3VHTMCS6": coDevWDSLinkStsPktsRxNSS3VHTMCS6,
       "coDevWDSLinkStsPktsRxNSS3VHTMCS7": coDevWDSLinkStsPktsRxNSS3VHTMCS7,
       "coDevWDSLinkStsPktsRxNSS3VHTMCS8": coDevWDSLinkStsPktsRxNSS3VHTMCS8,
       "coDevWDSLinkStsPktsRxNSS3VHTMCS9": coDevWDSLinkStsPktsRxNSS3VHTMCS9,
       "coDeviceWDSNetworkScanGroup": coDeviceWDSNetworkScanGroup,
       "coDeviceWDSNetworkScanTable": coDeviceWDSNetworkScanTable,
       "coDeviceWDSNetworkScanEntry": coDeviceWDSNetworkScanEntry,
       "coDevWDSScanRadioIndex": coDevWDSScanRadioIndex,
       "coDevWDSScanPeerIndex": coDevWDSScanPeerIndex,
       "coDevWDSScanGroupId": coDevWDSScanGroupId,
       "coDevWDSScanPeerMacAddress": coDevWDSScanPeerMacAddress,
       "coDevWDSScanChannel": coDevWDSScanChannel,
       "coDevWDSScanSNR": coDevWDSScanSNR,
       "coDevWDSScanMode": coDevWDSScanMode,
       "coDevWDSScanAvailable": coDevWDSScanAvailable,
       "colubrisDeviceWdsMIBNotificationPrefix": colubrisDeviceWdsMIBNotificationPrefix,
       "colubrisDeviceWdsMIBNotifications": colubrisDeviceWdsMIBNotifications,
       "colubrisDeviceWdsMIBConformance": colubrisDeviceWdsMIBConformance,
       "colubrisDeviceWdsMIBCompliances": colubrisDeviceWdsMIBCompliances,
       "colubrisDeviceWdsMIBCompliance": colubrisDeviceWdsMIBCompliance,
       "colubrisDeviceWdsMIBGroups": colubrisDeviceWdsMIBGroups,
       "colubrisDeviceWdsInfoMIBGroup": colubrisDeviceWdsInfoMIBGroup,
       "colubrisDeviceWdsRadioMIBGroup": colubrisDeviceWdsRadioMIBGroup,
       "colubrisDeviceWdsGroupMIBGroup": colubrisDeviceWdsGroupMIBGroup,
       "colubrisDeviceWdsLinkMIBGroup": colubrisDeviceWdsLinkMIBGroup,
       "colubrisDeviceWdsNetworkScanMIBGroup": colubrisDeviceWdsNetworkScanMIBGroup}
)
