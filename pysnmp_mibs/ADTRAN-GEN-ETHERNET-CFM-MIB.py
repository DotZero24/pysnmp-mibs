# SNMP MIB module (ADTRAN-GEN-ETHERNET-CFM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/adtran/ADTRAN-GEN-ETHERNET-CFM-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:32:42 2025
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

(adGenEthernetCfm,
 adGenEthernetCfmID) = mibBuilder.importSymbols(
    "ADTRAN-GEN-ETHERNET-OAM-MIB",
    "adGenEthernetCfm",
    "adGenEthernetCfmID")

(adTrapInformSeqNum,) = mibBuilder.importSymbols(
    "ADTRAN-GENTRAPINFORM-MIB",
    "adTrapInformSeqNum")

(dot1agCfmLtrSeqNumber,
 dot1agCfmMaCompEntry,
 dot1agCfmMaCompPrimaryVlanId,
 dot1agCfmMaIndex,
 dot1agCfmMaMepListEntry,
 dot1agCfmMaNetEntry,
 dot1agCfmMaNetFormat,
 dot1agCfmMaNetName,
 dot1agCfmMdEntry,
 dot1agCfmMdFormat,
 dot1agCfmMdIndex,
 dot1agCfmMdMdLevel,
 dot1agCfmMdName,
 dot1agCfmMepDbRMepIdentifier,
 dot1agCfmMepDirection,
 dot1agCfmMepEntry,
 dot1agCfmMepIdentifier,
 dot1agCfmMepIfIndex,
 dot1agCfmMepPrimaryVid,
 dot1agCfmVlanEntry) = mibBuilder.importSymbols(
    "IEEE8021-CFM-MIB",
    "dot1agCfmLtrSeqNumber",
    "dot1agCfmMaCompEntry",
    "dot1agCfmMaCompPrimaryVlanId",
    "dot1agCfmMaIndex",
    "dot1agCfmMaMepListEntry",
    "dot1agCfmMaNetEntry",
    "dot1agCfmMaNetFormat",
    "dot1agCfmMaNetName",
    "dot1agCfmMdEntry",
    "dot1agCfmMdFormat",
    "dot1agCfmMdIndex",
    "dot1agCfmMdMdLevel",
    "dot1agCfmMdName",
    "dot1agCfmMepDbRMepIdentifier",
    "dot1agCfmMepDirection",
    "dot1agCfmMepEntry",
    "dot1agCfmMepIdentifier",
    "dot1agCfmMepIfIndex",
    "dot1agCfmMepPrimaryVid",
    "dot1agCfmVlanEntry")

(ifDescr,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifDescr")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

adGenEthCfmMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 75, 1, 1)
)
if mibBuilder.loadTexts:
    adGenEthCfmMib.setRevisions(
        ("2008-04-25 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class AdGenEthCfmMaNetEntryMepDbRule(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("configuredOnly", 1),
          ("autoDiscovery", 2),
          ("autoLearning", 3))
    )



class AdGenEthCfmRemoteMepState(TextualConvention, Integer32):
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
        *(("rMepIdle", 1),
          ("rMepStart", 2),
          ("rMepStaticFailed", 3),
          ("rMepStaticOk", 4),
          ("rMepDiscoveredFail", 5),
          ("rMepDiscoveredOk", 6))
    )



class AdGenEthCfmRMepProvisioningState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("static", 1),
          ("dynamic", 2))
    )



class AdGenEthCfmRMepLockClear(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("lock", 1),
          ("clear", 2))
    )



# MIB Managed Objects in the order of their OIDs

_AdGenEthCfmNotifications_ObjectIdentity = ObjectIdentity
adGenEthCfmNotifications = _AdGenEthCfmNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 1, 0)
)
_AdGenEthCfmMIBObjects_ObjectIdentity = ObjectIdentity
adGenEthCfmMIBObjects = _AdGenEthCfmMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 1, 1)
)
_AdGenEthCfmSystem_ObjectIdentity = ObjectIdentity
adGenEthCfmSystem = _AdGenEthCfmSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 1, 1, 1)
)
_AdGenEthCfmEnabled_Type = TruthValue
_AdGenEthCfmEnabled_Object = MibScalar
adGenEthCfmEnabled = _AdGenEthCfmEnabled_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 1, 1, 1, 1),
    _AdGenEthCfmEnabled_Type()
)
adGenEthCfmEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenEthCfmEnabled.setStatus("current")
_AdGenEthCfmProvisioningUpdates_Type = Unsigned32
_AdGenEthCfmProvisioningUpdates_Object = MibScalar
adGenEthCfmProvisioningUpdates = _AdGenEthCfmProvisioningUpdates_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 1, 1, 1, 2),
    _AdGenEthCfmProvisioningUpdates_Type()
)
adGenEthCfmProvisioningUpdates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEthCfmProvisioningUpdates.setStatus("current")


class _AdGenEthCfmLinkTraceCacheTimeout_Type(Unsigned32):
    """Custom type adGenEthCfmLinkTraceCacheTimeout based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AdGenEthCfmLinkTraceCacheTimeout_Type.__name__ = "Unsigned32"
_AdGenEthCfmLinkTraceCacheTimeout_Object = MibScalar
adGenEthCfmLinkTraceCacheTimeout = _AdGenEthCfmLinkTraceCacheTimeout_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 1, 1, 1, 3),
    _AdGenEthCfmLinkTraceCacheTimeout_Type()
)
adGenEthCfmLinkTraceCacheTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenEthCfmLinkTraceCacheTimeout.setStatus("current")


class _AdGenEthCfmLinkTraceCacheSize_Type(Unsigned32):
    """Custom type adGenEthCfmLinkTraceCacheSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_AdGenEthCfmLinkTraceCacheSize_Type.__name__ = "Unsigned32"
_AdGenEthCfmLinkTraceCacheSize_Object = MibScalar
adGenEthCfmLinkTraceCacheSize = _AdGenEthCfmLinkTraceCacheSize_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 1, 1, 1, 4),
    _AdGenEthCfmLinkTraceCacheSize_Type()
)
adGenEthCfmLinkTraceCacheSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenEthCfmLinkTraceCacheSize.setStatus("current")
_AdGenEthCfmDefaultMd_ObjectIdentity = ObjectIdentity
adGenEthCfmDefaultMd = _AdGenEthCfmDefaultMd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 1, 1, 3)
)
_AdGenEthCfmDefaultMdLastCreateError_Type = DisplayString
_AdGenEthCfmDefaultMdLastCreateError_Object = MibScalar
adGenEthCfmDefaultMdLastCreateError = _AdGenEthCfmDefaultMdLastCreateError_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 1, 1, 3, 1),
    _AdGenEthCfmDefaultMdLastCreateError_Type()
)
adGenEthCfmDefaultMdLastCreateError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEthCfmDefaultMdLastCreateError.setStatus("current")
_AdGenEthCfmVlan_ObjectIdentity = ObjectIdentity
adGenEthCfmVlan = _AdGenEthCfmVlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 1, 1, 4)
)
_AdGenEthCfmVlanTable_Object = MibTable
adGenEthCfmVlanTable = _AdGenEthCfmVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 1, 1, 4, 1)
)
if mibBuilder.loadTexts:
    adGenEthCfmVlanTable.setStatus("current")
_AdGenEthCfmVlanEntry_Object = MibTableRow
adGenEthCfmVlanEntry = _AdGenEthCfmVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 1, 1, 4, 1, 1)
)
if mibBuilder.loadTexts:
    adGenEthCfmVlanEntry.setStatus("current")
_AdGenEthCfmVlanErrorStatus_Type = DisplayString
_AdGenEthCfmVlanErrorStatus_Object = MibTableColumn
adGenEthCfmVlanErrorStatus = _AdGenEthCfmVlanErrorStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 1, 1, 4, 1, 1, 1),
    _AdGenEthCfmVlanErrorStatus_Type()
)
adGenEthCfmVlanErrorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEthCfmVlanErrorStatus.setStatus("current")
_AdGenEthCfmMd_ObjectIdentity = ObjectIdentity
adGenEthCfmMd = _AdGenEthCfmMd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 1, 1, 6)
)
_AdGenEthCfmMdMaxNumber_Type = Unsigned32
_AdGenEthCfmMdMaxNumber_Object = MibScalar
adGenEthCfmMdMaxNumber = _AdGenEthCfmMdMaxNumber_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 1, 1, 6, 1),
    _AdGenEthCfmMdMaxNumber_Type()
)
adGenEthCfmMdMaxNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEthCfmMdMaxNumber.setStatus("current")
_AdGenEthCfmMdCurrentNumber_Type = Unsigned32
_AdGenEthCfmMdCurrentNumber_Object = MibScalar
adGenEthCfmMdCurrentNumber = _AdGenEthCfmMdCurrentNumber_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 1, 1, 6, 2),
    _AdGenEthCfmMdCurrentNumber_Type()
)
adGenEthCfmMdCurrentNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEthCfmMdCurrentNumber.setStatus("current")
_AdGenEthCfmMdLastCreateError_Type = DisplayString
_AdGenEthCfmMdLastCreateError_Object = MibScalar
adGenEthCfmMdLastCreateError = _AdGenEthCfmMdLastCreateError_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 1, 1, 6, 3),
    _AdGenEthCfmMdLastCreateError_Type()
)
adGenEthCfmMdLastCreateError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEthCfmMdLastCreateError.setStatus("current")
_AdGenEthCfmMdTable_Object = MibTable
adGenEthCfmMdTable = _AdGenEthCfmMdTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 1, 1, 6, 4)
)
if mibBuilder.loadTexts:
    adGenEthCfmMdTable.setStatus("current")
_AdGenEthCfmMdEntry_Object = MibTableRow
adGenEthCfmMdEntry = _AdGenEthCfmMdEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 1, 1, 6, 4, 1)
)
if mibBuilder.loadTexts:
    adGenEthCfmMdEntry.setStatus("current")
_AdGenEthCfmMdErrorStatus_Type = DisplayString
_AdGenEthCfmMdErrorStatus_Object = MibTableColumn
adGenEthCfmMdErrorStatus = _AdGenEthCfmMdErrorStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 1, 1, 6, 4, 1, 1),
    _AdGenEthCfmMdErrorStatus_Type()
)
adGenEthCfmMdErrorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEthCfmMdErrorStatus.setStatus("current")
_AdGenEthCfmMdCfmEnabled_Type = TruthValue
_AdGenEthCfmMdCfmEnabled_Object = MibTableColumn
adGenEthCfmMdCfmEnabled = _AdGenEthCfmMdCfmEnabled_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 1, 1, 6, 4, 1, 2),
    _AdGenEthCfmMdCfmEnabled_Type()
)
adGenEthCfmMdCfmEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenEthCfmMdCfmEnabled.setStatus("current")
_AdGenEthCfmMdCcmEnabled_Type = TruthValue
_AdGenEthCfmMdCcmEnabled_Object = MibTableColumn
adGenEthCfmMdCcmEnabled = _AdGenEthCfmMdCcmEnabled_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 1, 1, 6, 4, 1, 3),
    _AdGenEthCfmMdCcmEnabled_Type()
)
adGenEthCfmMdCcmEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenEthCfmMdCcmEnabled.setStatus("current")
_AdGenEthCfmMa_ObjectIdentity = ObjectIdentity
adGenEthCfmMa = _AdGenEthCfmMa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 1, 1, 7)
)
_AdGenEthCfmMaMaxNumber_Type = Unsigned32
_AdGenEthCfmMaMaxNumber_Object = MibScalar
adGenEthCfmMaMaxNumber = _AdGenEthCfmMaMaxNumber_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 1, 1, 7, 1),
    _AdGenEthCfmMaMaxNumber_Type()
)
adGenEthCfmMaMaxNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEthCfmMaMaxNumber.setStatus("current")
_AdGenEthCfmMaCurrentNumber_Type = Unsigned32
_AdGenEthCfmMaCurrentNumber_Object = MibScalar
adGenEthCfmMaCurrentNumber = _AdGenEthCfmMaCurrentNumber_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 1, 1, 7, 2),
    _AdGenEthCfmMaCurrentNumber_Type()
)
adGenEthCfmMaCurrentNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEthCfmMaCurrentNumber.setStatus("current")
_AdGenEthCfmMaNet_ObjectIdentity = ObjectIdentity
adGenEthCfmMaNet = _AdGenEthCfmMaNet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 1, 1, 7, 3)
)
_AdGenEthCfmMaNetLastCreateError_Type = DisplayString
_AdGenEthCfmMaNetLastCreateError_Object = MibScalar
adGenEthCfmMaNetLastCreateError = _AdGenEthCfmMaNetLastCreateError_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 1, 1, 7, 3, 1),
    _AdGenEthCfmMaNetLastCreateError_Type()
)
adGenEthCfmMaNetLastCreateError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEthCfmMaNetLastCreateError.setStatus("current")
_AdGenEthCfmMaNetTable_Object = MibTable
adGenEthCfmMaNetTable = _AdGenEthCfmMaNetTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 1, 1, 7, 3, 2)
)
if mibBuilder.loadTexts:
    adGenEthCfmMaNetTable.setStatus("current")
_AdGenEthCfmMaNetEntry_Object = MibTableRow
adGenEthCfmMaNetEntry = _AdGenEthCfmMaNetEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 1, 1, 7, 3, 2, 1)
)
if mibBuilder.loadTexts:
    adGenEthCfmMaNetEntry.setStatus("current")
_AdGenEthCfmMaNetErrorStatus_Type = DisplayString
_AdGenEthCfmMaNetErrorStatus_Object = MibTableColumn
adGenEthCfmMaNetErrorStatus = _AdGenEthCfmMaNetErrorStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 1, 1, 7, 3, 2, 1, 1),
    _AdGenEthCfmMaNetErrorStatus_Type()
)
adGenEthCfmMaNetErrorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEthCfmMaNetErrorStatus.setStatus("current")
_AdGenEthCfmMaNetCfmEnabled_Type = TruthValue
_AdGenEthCfmMaNetCfmEnabled_Object = MibTableColumn
adGenEthCfmMaNetCfmEnabled = _AdGenEthCfmMaNetCfmEnabled_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 1, 1, 7, 3, 2, 1, 2),
    _AdGenEthCfmMaNetCfmEnabled_Type()
)
adGenEthCfmMaNetCfmEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenEthCfmMaNetCfmEnabled.setStatus("current")
_AdGenEthCfmMaNetCcmEnabled_Type = TruthValue
_AdGenEthCfmMaNetCcmEnabled_Object = MibTableColumn
adGenEthCfmMaNetCcmEnabled = _AdGenEthCfmMaNetCcmEnabled_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 1, 1, 7, 3, 2, 1, 3),
    _AdGenEthCfmMaNetCcmEnabled_Type()
)
adGenEthCfmMaNetCcmEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenEthCfmMaNetCcmEnabled.setStatus("current")
_AdGenEthCfmMaNetMepDbRule_Type = AdGenEthCfmMaNetEntryMepDbRule
_AdGenEthCfmMaNetMepDbRule_Object = MibTableColumn
adGenEthCfmMaNetMepDbRule = _AdGenEthCfmMaNetMepDbRule_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 1, 1, 7, 3, 2, 1, 4),
    _AdGenEthCfmMaNetMepDbRule_Type()
)
adGenEthCfmMaNetMepDbRule.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenEthCfmMaNetMepDbRule.setStatus("current")
_AdGenEthCfmMaNetRMepHoldTime_Type = Unsigned32
_AdGenEthCfmMaNetRMepHoldTime_Object = MibTableColumn
adGenEthCfmMaNetRMepHoldTime = _AdGenEthCfmMaNetRMepHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 1, 1, 7, 3, 2, 1, 5),
    _AdGenEthCfmMaNetRMepHoldTime_Type()
)
adGenEthCfmMaNetRMepHoldTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenEthCfmMaNetRMepHoldTime.setStatus("current")
_AdGenEthCfmMaComp_ObjectIdentity = ObjectIdentity
adGenEthCfmMaComp = _AdGenEthCfmMaComp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 1, 1, 7, 4)
)
_AdGenEthCfmMaCompLastCreateError_Type = DisplayString
_AdGenEthCfmMaCompLastCreateError_Object = MibScalar
adGenEthCfmMaCompLastCreateError = _AdGenEthCfmMaCompLastCreateError_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 1, 1, 7, 4, 1),
    _AdGenEthCfmMaCompLastCreateError_Type()
)
adGenEthCfmMaCompLastCreateError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEthCfmMaCompLastCreateError.setStatus("current")
_AdGenEthCfmMaCompTable_Object = MibTable
adGenEthCfmMaCompTable = _AdGenEthCfmMaCompTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 1, 1, 7, 4, 2)
)
if mibBuilder.loadTexts:
    adGenEthCfmMaCompTable.setStatus("current")
_AdGenEthCfmMaCompEntry_Object = MibTableRow
adGenEthCfmMaCompEntry = _AdGenEthCfmMaCompEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 1, 1, 7, 4, 2, 1)
)
if mibBuilder.loadTexts:
    adGenEthCfmMaCompEntry.setStatus("current")
_AdGenEthCfmMaCompErrorStatus_Type = DisplayString
_AdGenEthCfmMaCompErrorStatus_Object = MibTableColumn
adGenEthCfmMaCompErrorStatus = _AdGenEthCfmMaCompErrorStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 1, 1, 7, 4, 2, 1, 1),
    _AdGenEthCfmMaCompErrorStatus_Type()
)
adGenEthCfmMaCompErrorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEthCfmMaCompErrorStatus.setStatus("current")
_AdGenEthCfmMaMepList_ObjectIdentity = ObjectIdentity
adGenEthCfmMaMepList = _AdGenEthCfmMaMepList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 1, 1, 7, 5)
)
_AdGenEthCfmMaMepListLastCreateError_Type = DisplayString
_AdGenEthCfmMaMepListLastCreateError_Object = MibScalar
adGenEthCfmMaMepListLastCreateError = _AdGenEthCfmMaMepListLastCreateError_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 1, 1, 7, 5, 1),
    _AdGenEthCfmMaMepListLastCreateError_Type()
)
adGenEthCfmMaMepListLastCreateError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEthCfmMaMepListLastCreateError.setStatus("current")
_AdGenEthCfmMaMepListTable_Object = MibTable
adGenEthCfmMaMepListTable = _AdGenEthCfmMaMepListTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 1, 1, 7, 5, 2)
)
if mibBuilder.loadTexts:
    adGenEthCfmMaMepListTable.setStatus("current")
_AdGenEthCfmMaMepListEntry_Object = MibTableRow
adGenEthCfmMaMepListEntry = _AdGenEthCfmMaMepListEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 1, 1, 7, 5, 2, 1)
)
if mibBuilder.loadTexts:
    adGenEthCfmMaMepListEntry.setStatus("current")
_AdGenEthCfmMaMepListErrorStatus_Type = DisplayString
_AdGenEthCfmMaMepListErrorStatus_Object = MibTableColumn
adGenEthCfmMaMepListErrorStatus = _AdGenEthCfmMaMepListErrorStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 1, 1, 7, 5, 2, 1, 1),
    _AdGenEthCfmMaMepListErrorStatus_Type()
)
adGenEthCfmMaMepListErrorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEthCfmMaMepListErrorStatus.setStatus("current")
_AdGenEthCfmMep_ObjectIdentity = ObjectIdentity
adGenEthCfmMep = _AdGenEthCfmMep_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 1, 1, 8)
)
_AdGenEthCfmMepMaxNumber_Type = Unsigned32
_AdGenEthCfmMepMaxNumber_Object = MibScalar
adGenEthCfmMepMaxNumber = _AdGenEthCfmMepMaxNumber_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 1, 1, 8, 1),
    _AdGenEthCfmMepMaxNumber_Type()
)
adGenEthCfmMepMaxNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEthCfmMepMaxNumber.setStatus("current")
_AdGenEthCfmMepCurrentNumber_Type = Unsigned32
_AdGenEthCfmMepCurrentNumber_Object = MibScalar
adGenEthCfmMepCurrentNumber = _AdGenEthCfmMepCurrentNumber_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 1, 1, 8, 2),
    _AdGenEthCfmMepCurrentNumber_Type()
)
adGenEthCfmMepCurrentNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEthCfmMepCurrentNumber.setStatus("current")
_AdGenEthCfmMepLastCreateError_Type = DisplayString
_AdGenEthCfmMepLastCreateError_Object = MibScalar
adGenEthCfmMepLastCreateError = _AdGenEthCfmMepLastCreateError_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 1, 1, 8, 3),
    _AdGenEthCfmMepLastCreateError_Type()
)
adGenEthCfmMepLastCreateError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEthCfmMepLastCreateError.setStatus("current")
_AdGenEthCfmMepTable_Object = MibTable
adGenEthCfmMepTable = _AdGenEthCfmMepTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 1, 1, 8, 4)
)
if mibBuilder.loadTexts:
    adGenEthCfmMepTable.setStatus("current")
_AdGenEthCfmMepEntry_Object = MibTableRow
adGenEthCfmMepEntry = _AdGenEthCfmMepEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 1, 1, 8, 4, 1)
)
if mibBuilder.loadTexts:
    adGenEthCfmMepEntry.setStatus("current")
_AdGenEthCfmMepLoopbackErrorStatus_Type = DisplayString
_AdGenEthCfmMepLoopbackErrorStatus_Object = MibTableColumn
adGenEthCfmMepLoopbackErrorStatus = _AdGenEthCfmMepLoopbackErrorStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 1, 1, 8, 4, 1, 1),
    _AdGenEthCfmMepLoopbackErrorStatus_Type()
)
adGenEthCfmMepLoopbackErrorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEthCfmMepLoopbackErrorStatus.setStatus("current")


class _AdGenEthCfmMepLoopbackTimeout_Type(Unsigned32):
    """Custom type adGenEthCfmMepLoopbackTimeout based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 60000),
    )


_AdGenEthCfmMepLoopbackTimeout_Type.__name__ = "Unsigned32"
_AdGenEthCfmMepLoopbackTimeout_Object = MibTableColumn
adGenEthCfmMepLoopbackTimeout = _AdGenEthCfmMepLoopbackTimeout_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 1, 1, 8, 4, 1, 2),
    _AdGenEthCfmMepLoopbackTimeout_Type()
)
adGenEthCfmMepLoopbackTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenEthCfmMepLoopbackTimeout.setStatus("current")


class _AdGenEthCfmMepLoopbackInterframeDelay_Type(Unsigned32):
    """Custom type adGenEthCfmMepLoopbackInterframeDelay based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 5000),
    )


_AdGenEthCfmMepLoopbackInterframeDelay_Type.__name__ = "Unsigned32"
_AdGenEthCfmMepLoopbackInterframeDelay_Object = MibTableColumn
adGenEthCfmMepLoopbackInterframeDelay = _AdGenEthCfmMepLoopbackInterframeDelay_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 1, 1, 8, 4, 1, 3),
    _AdGenEthCfmMepLoopbackInterframeDelay_Type()
)
adGenEthCfmMepLoopbackInterframeDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenEthCfmMepLoopbackInterframeDelay.setStatus("current")
_AdGenEthCfmMepErrorStatus_Type = DisplayString
_AdGenEthCfmMepErrorStatus_Object = MibTableColumn
adGenEthCfmMepErrorStatus = _AdGenEthCfmMepErrorStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 1, 1, 8, 4, 1, 4),
    _AdGenEthCfmMepErrorStatus_Type()
)
adGenEthCfmMepErrorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEthCfmMepErrorStatus.setStatus("current")
_AdGenEthCfmMepLinkTraceErrorStatus_Type = DisplayString
_AdGenEthCfmMepLinkTraceErrorStatus_Object = MibTableColumn
adGenEthCfmMepLinkTraceErrorStatus = _AdGenEthCfmMepLinkTraceErrorStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 1, 1, 8, 4, 1, 5),
    _AdGenEthCfmMepLinkTraceErrorStatus_Type()
)
adGenEthCfmMepLinkTraceErrorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEthCfmMepLinkTraceErrorStatus.setStatus("current")
_AdGenEthCfmMepLbrResponseTimeMin_Type = Unsigned32
_AdGenEthCfmMepLbrResponseTimeMin_Object = MibTableColumn
adGenEthCfmMepLbrResponseTimeMin = _AdGenEthCfmMepLbrResponseTimeMin_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 1, 1, 8, 4, 1, 6),
    _AdGenEthCfmMepLbrResponseTimeMin_Type()
)
adGenEthCfmMepLbrResponseTimeMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEthCfmMepLbrResponseTimeMin.setStatus("current")
_AdGenEthCfmMepLbrResponseTimeMax_Type = Unsigned32
_AdGenEthCfmMepLbrResponseTimeMax_Object = MibTableColumn
adGenEthCfmMepLbrResponseTimeMax = _AdGenEthCfmMepLbrResponseTimeMax_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 1, 1, 8, 4, 1, 7),
    _AdGenEthCfmMepLbrResponseTimeMax_Type()
)
adGenEthCfmMepLbrResponseTimeMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEthCfmMepLbrResponseTimeMax.setStatus("current")
_AdGenEthCfmMepLbrResponseTimeAvg_Type = Unsigned32
_AdGenEthCfmMepLbrResponseTimeAvg_Object = MibTableColumn
adGenEthCfmMepLbrResponseTimeAvg = _AdGenEthCfmMepLbrResponseTimeAvg_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 1, 1, 8, 4, 1, 8),
    _AdGenEthCfmMepLbrResponseTimeAvg_Type()
)
adGenEthCfmMepLbrResponseTimeAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEthCfmMepLbrResponseTimeAvg.setStatus("current")
_AdGenEthCfmMepLoopbackCancel_Type = TruthValue
_AdGenEthCfmMepLoopbackCancel_Object = MibTableColumn
adGenEthCfmMepLoopbackCancel = _AdGenEthCfmMepLoopbackCancel_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 1, 1, 8, 4, 1, 9),
    _AdGenEthCfmMepLoopbackCancel_Type()
)
adGenEthCfmMepLoopbackCancel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenEthCfmMepLoopbackCancel.setStatus("current")
_AdGenEthCfmMepTransmitLtmStatus_Type = TruthValue
_AdGenEthCfmMepTransmitLtmStatus_Object = MibTableColumn
adGenEthCfmMepTransmitLtmStatus = _AdGenEthCfmMepTransmitLtmStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 1, 1, 8, 4, 1, 10),
    _AdGenEthCfmMepTransmitLtmStatus_Type()
)
adGenEthCfmMepTransmitLtmStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenEthCfmMepTransmitLtmStatus.setStatus("current")
_AdGenEthCfmMepLinkAwarenessPeers_Type = DisplayString
_AdGenEthCfmMepLinkAwarenessPeers_Object = MibTableColumn
adGenEthCfmMepLinkAwarenessPeers = _AdGenEthCfmMepLinkAwarenessPeers_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 1, 1, 8, 4, 1, 11),
    _AdGenEthCfmMepLinkAwarenessPeers_Type()
)
adGenEthCfmMepLinkAwarenessPeers.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenEthCfmMepLinkAwarenessPeers.setStatus("current")


class _AdGenEthCfmMepLinkAwarenessMode_Type(Integer32):
    """Custom type adGenEthCfmMepLinkAwarenessMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("interfaceStatusTlv", 1),
          ("noCcm", 2))
    )


_AdGenEthCfmMepLinkAwarenessMode_Type.__name__ = "Integer32"
_AdGenEthCfmMepLinkAwarenessMode_Object = MibTableColumn
adGenEthCfmMepLinkAwarenessMode = _AdGenEthCfmMepLinkAwarenessMode_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 1, 1, 8, 4, 1, 12),
    _AdGenEthCfmMepLinkAwarenessMode_Type()
)
adGenEthCfmMepLinkAwarenessMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenEthCfmMepLinkAwarenessMode.setStatus("current")
_AdGenEthCfmMepLinkTraceTable_Object = MibTable
adGenEthCfmMepLinkTraceTable = _AdGenEthCfmMepLinkTraceTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 1, 1, 8, 5)
)
if mibBuilder.loadTexts:
    adGenEthCfmMepLinkTraceTable.setStatus("current")
_AdGenEthCfmMepLinkTraceEntry_Object = MibTableRow
adGenEthCfmMepLinkTraceEntry = _AdGenEthCfmMepLinkTraceEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 1, 1, 8, 5, 1)
)
adGenEthCfmMepLinkTraceEntry.setIndexNames(
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMdIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMaIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMepIdentifier"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmLtrSeqNumber"),
)
if mibBuilder.loadTexts:
    adGenEthCfmMepLinkTraceEntry.setStatus("current")
_AdGenEthCfmMepLinkTraceTimeRemaining_Type = Unsigned32
_AdGenEthCfmMepLinkTraceTimeRemaining_Object = MibTableColumn
adGenEthCfmMepLinkTraceTimeRemaining = _AdGenEthCfmMepLinkTraceTimeRemaining_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 1, 1, 8, 5, 1, 1),
    _AdGenEthCfmMepLinkTraceTimeRemaining_Type()
)
adGenEthCfmMepLinkTraceTimeRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEthCfmMepLinkTraceTimeRemaining.setStatus("current")
_AdGenEthCfmMepDbTable_Object = MibTable
adGenEthCfmMepDbTable = _AdGenEthCfmMepDbTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 1, 1, 8, 6)
)
if mibBuilder.loadTexts:
    adGenEthCfmMepDbTable.setStatus("current")
_AdGenEthCfmMepDbEntry_Object = MibTableRow
adGenEthCfmMepDbEntry = _AdGenEthCfmMepDbEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 1, 1, 8, 6, 1)
)
adGenEthCfmMepDbEntry.setIndexNames(
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMdIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMaIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMepIdentifier"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMepDbRMepIdentifier"),
)
if mibBuilder.loadTexts:
    adGenEthCfmMepDbEntry.setStatus("current")
_AdGenEthCfmMepDbRMepState_Type = AdGenEthCfmRemoteMepState
_AdGenEthCfmMepDbRMepState_Object = MibTableColumn
adGenEthCfmMepDbRMepState = _AdGenEthCfmMepDbRMepState_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 1, 1, 8, 6, 1, 1),
    _AdGenEthCfmMepDbRMepState_Type()
)
adGenEthCfmMepDbRMepState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEthCfmMepDbRMepState.setStatus("current")
_AdGenEthCfmMepDbRMepProvisioningState_Type = AdGenEthCfmRMepProvisioningState
_AdGenEthCfmMepDbRMepProvisioningState_Object = MibTableColumn
adGenEthCfmMepDbRMepProvisioningState = _AdGenEthCfmMepDbRMepProvisioningState_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 1, 1, 8, 6, 1, 2),
    _AdGenEthCfmMepDbRMepProvisioningState_Type()
)
adGenEthCfmMepDbRMepProvisioningState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEthCfmMepDbRMepProvisioningState.setStatus("current")
_AdGenEthCfmMepDbRMepEdit_Type = AdGenEthCfmRMepLockClear
_AdGenEthCfmMepDbRMepEdit_Object = MibTableColumn
adGenEthCfmMepDbRMepEdit = _AdGenEthCfmMepDbRMepEdit_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 1, 1, 8, 6, 1, 3),
    _AdGenEthCfmMepDbRMepEdit_Type()
)
adGenEthCfmMepDbRMepEdit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenEthCfmMepDbRMepEdit.setStatus("current")
dot1agCfmVlanEntry.registerAugmentions(
    ("ADTRAN-GEN-ETHERNET-CFM-MIB",
     "adGenEthCfmVlanEntry")
)
adGenEthCfmVlanEntry.setIndexNames(*dot1agCfmVlanEntry.getIndexNames())
dot1agCfmMdEntry.registerAugmentions(
    ("ADTRAN-GEN-ETHERNET-CFM-MIB",
     "adGenEthCfmMdEntry")
)
adGenEthCfmMdEntry.setIndexNames(*dot1agCfmMdEntry.getIndexNames())
dot1agCfmMaNetEntry.registerAugmentions(
    ("ADTRAN-GEN-ETHERNET-CFM-MIB",
     "adGenEthCfmMaNetEntry")
)
adGenEthCfmMaNetEntry.setIndexNames(*dot1agCfmMaNetEntry.getIndexNames())
dot1agCfmMaCompEntry.registerAugmentions(
    ("ADTRAN-GEN-ETHERNET-CFM-MIB",
     "adGenEthCfmMaCompEntry")
)
adGenEthCfmMaCompEntry.setIndexNames(*dot1agCfmMaCompEntry.getIndexNames())
dot1agCfmMaMepListEntry.registerAugmentions(
    ("ADTRAN-GEN-ETHERNET-CFM-MIB",
     "adGenEthCfmMaMepListEntry")
)
adGenEthCfmMaMepListEntry.setIndexNames(*dot1agCfmMaMepListEntry.getIndexNames())
dot1agCfmMepEntry.registerAugmentions(
    ("ADTRAN-GEN-ETHERNET-CFM-MIB",
     "adGenEthCfmMepEntry")
)
adGenEthCfmMepEntry.setIndexNames(*dot1agCfmMepEntry.getIndexNames())

# Managed Objects groups


# Notification objects

adGenEthCfmRDISet = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 1, 0, 1)
)
adGenEthCfmRDISet.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("IEEE8021-CFM-MIB", "dot1agCfmMepIfIndex"),
        ("IF-MIB", "ifDescr"),
        ("IEEE8021-CFM-MIB", "dot1agCfmMdFormat"),
        ("IEEE8021-CFM-MIB", "dot1agCfmMdName"),
        ("IEEE8021-CFM-MIB", "dot1agCfmMdMdLevel"),
        ("IEEE8021-CFM-MIB", "dot1agCfmMaNetFormat"),
        ("IEEE8021-CFM-MIB", "dot1agCfmMaNetName"),
        ("IEEE8021-CFM-MIB", "dot1agCfmMaCompPrimaryVlanId"),
        ("IEEE8021-CFM-MIB", "dot1agCfmMepDirection"),
        ("IEEE8021-CFM-MIB", "dot1agCfmMepPrimaryVid"))
)
if mibBuilder.loadTexts:
    adGenEthCfmRDISet.setStatus(
        "current"
    )

adGenEthCfmRDIClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 1, 0, 2)
)
adGenEthCfmRDIClear.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("IEEE8021-CFM-MIB", "dot1agCfmMepIfIndex"),
        ("IF-MIB", "ifDescr"),
        ("IEEE8021-CFM-MIB", "dot1agCfmMdFormat"),
        ("IEEE8021-CFM-MIB", "dot1agCfmMdName"),
        ("IEEE8021-CFM-MIB", "dot1agCfmMdMdLevel"),
        ("IEEE8021-CFM-MIB", "dot1agCfmMaNetFormat"),
        ("IEEE8021-CFM-MIB", "dot1agCfmMaNetName"),
        ("IEEE8021-CFM-MIB", "dot1agCfmMaCompPrimaryVlanId"),
        ("IEEE8021-CFM-MIB", "dot1agCfmMepDirection"),
        ("IEEE8021-CFM-MIB", "dot1agCfmMepPrimaryVid"))
)
if mibBuilder.loadTexts:
    adGenEthCfmRDIClear.setStatus(
        "current"
    )

adGenEthCfmMacStatusSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 1, 0, 3)
)
adGenEthCfmMacStatusSet.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("IEEE8021-CFM-MIB", "dot1agCfmMepIfIndex"),
        ("IF-MIB", "ifDescr"),
        ("IEEE8021-CFM-MIB", "dot1agCfmMdFormat"),
        ("IEEE8021-CFM-MIB", "dot1agCfmMdName"),
        ("IEEE8021-CFM-MIB", "dot1agCfmMdMdLevel"),
        ("IEEE8021-CFM-MIB", "dot1agCfmMaNetFormat"),
        ("IEEE8021-CFM-MIB", "dot1agCfmMaNetName"),
        ("IEEE8021-CFM-MIB", "dot1agCfmMaCompPrimaryVlanId"),
        ("IEEE8021-CFM-MIB", "dot1agCfmMepDirection"),
        ("IEEE8021-CFM-MIB", "dot1agCfmMepPrimaryVid"))
)
if mibBuilder.loadTexts:
    adGenEthCfmMacStatusSet.setStatus(
        "current"
    )

adGenEthCfmMacStatusClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 1, 0, 4)
)
adGenEthCfmMacStatusClear.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("IEEE8021-CFM-MIB", "dot1agCfmMepIfIndex"),
        ("IF-MIB", "ifDescr"),
        ("IEEE8021-CFM-MIB", "dot1agCfmMdFormat"),
        ("IEEE8021-CFM-MIB", "dot1agCfmMdName"),
        ("IEEE8021-CFM-MIB", "dot1agCfmMdMdLevel"),
        ("IEEE8021-CFM-MIB", "dot1agCfmMaNetFormat"),
        ("IEEE8021-CFM-MIB", "dot1agCfmMaNetName"),
        ("IEEE8021-CFM-MIB", "dot1agCfmMaCompPrimaryVlanId"),
        ("IEEE8021-CFM-MIB", "dot1agCfmMepDirection"),
        ("IEEE8021-CFM-MIB", "dot1agCfmMepPrimaryVid"))
)
if mibBuilder.loadTexts:
    adGenEthCfmMacStatusClear.setStatus(
        "current"
    )

adGenEthCfmRemoteCCMSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 1, 0, 5)
)
adGenEthCfmRemoteCCMSet.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("IEEE8021-CFM-MIB", "dot1agCfmMepIfIndex"),
        ("IF-MIB", "ifDescr"),
        ("IEEE8021-CFM-MIB", "dot1agCfmMdFormat"),
        ("IEEE8021-CFM-MIB", "dot1agCfmMdName"),
        ("IEEE8021-CFM-MIB", "dot1agCfmMdMdLevel"),
        ("IEEE8021-CFM-MIB", "dot1agCfmMaNetFormat"),
        ("IEEE8021-CFM-MIB", "dot1agCfmMaNetName"),
        ("IEEE8021-CFM-MIB", "dot1agCfmMaCompPrimaryVlanId"),
        ("IEEE8021-CFM-MIB", "dot1agCfmMepDirection"),
        ("IEEE8021-CFM-MIB", "dot1agCfmMepPrimaryVid"))
)
if mibBuilder.loadTexts:
    adGenEthCfmRemoteCCMSet.setStatus(
        "current"
    )

adGenEthCfmRemoteCCMClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 1, 0, 6)
)
adGenEthCfmRemoteCCMClear.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("IEEE8021-CFM-MIB", "dot1agCfmMepIfIndex"),
        ("IF-MIB", "ifDescr"),
        ("IEEE8021-CFM-MIB", "dot1agCfmMdFormat"),
        ("IEEE8021-CFM-MIB", "dot1agCfmMdName"),
        ("IEEE8021-CFM-MIB", "dot1agCfmMdMdLevel"),
        ("IEEE8021-CFM-MIB", "dot1agCfmMaNetFormat"),
        ("IEEE8021-CFM-MIB", "dot1agCfmMaNetName"),
        ("IEEE8021-CFM-MIB", "dot1agCfmMaCompPrimaryVlanId"),
        ("IEEE8021-CFM-MIB", "dot1agCfmMepDirection"),
        ("IEEE8021-CFM-MIB", "dot1agCfmMepPrimaryVid"))
)
if mibBuilder.loadTexts:
    adGenEthCfmRemoteCCMClear.setStatus(
        "current"
    )

adGenEthCfmErroredCCMSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 1, 0, 7)
)
adGenEthCfmErroredCCMSet.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("IEEE8021-CFM-MIB", "dot1agCfmMepIfIndex"),
        ("IF-MIB", "ifDescr"),
        ("IEEE8021-CFM-MIB", "dot1agCfmMdFormat"),
        ("IEEE8021-CFM-MIB", "dot1agCfmMdName"),
        ("IEEE8021-CFM-MIB", "dot1agCfmMdMdLevel"),
        ("IEEE8021-CFM-MIB", "dot1agCfmMaNetFormat"),
        ("IEEE8021-CFM-MIB", "dot1agCfmMaNetName"),
        ("IEEE8021-CFM-MIB", "dot1agCfmMaCompPrimaryVlanId"),
        ("IEEE8021-CFM-MIB", "dot1agCfmMepDirection"),
        ("IEEE8021-CFM-MIB", "dot1agCfmMepPrimaryVid"))
)
if mibBuilder.loadTexts:
    adGenEthCfmErroredCCMSet.setStatus(
        "current"
    )

adGenEthCfmErroredCCMClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 1, 0, 8)
)
adGenEthCfmErroredCCMClear.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("IEEE8021-CFM-MIB", "dot1agCfmMepIfIndex"),
        ("IF-MIB", "ifDescr"),
        ("IEEE8021-CFM-MIB", "dot1agCfmMdFormat"),
        ("IEEE8021-CFM-MIB", "dot1agCfmMdName"),
        ("IEEE8021-CFM-MIB", "dot1agCfmMdMdLevel"),
        ("IEEE8021-CFM-MIB", "dot1agCfmMaNetFormat"),
        ("IEEE8021-CFM-MIB", "dot1agCfmMaNetName"),
        ("IEEE8021-CFM-MIB", "dot1agCfmMaCompPrimaryVlanId"),
        ("IEEE8021-CFM-MIB", "dot1agCfmMepDirection"),
        ("IEEE8021-CFM-MIB", "dot1agCfmMepPrimaryVid"))
)
if mibBuilder.loadTexts:
    adGenEthCfmErroredCCMClear.setStatus(
        "current"
    )

adGenEthCfmXconCCMSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 1, 0, 9)
)
adGenEthCfmXconCCMSet.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("IEEE8021-CFM-MIB", "dot1agCfmMepIfIndex"),
        ("IF-MIB", "ifDescr"),
        ("IEEE8021-CFM-MIB", "dot1agCfmMdFormat"),
        ("IEEE8021-CFM-MIB", "dot1agCfmMdName"),
        ("IEEE8021-CFM-MIB", "dot1agCfmMdMdLevel"),
        ("IEEE8021-CFM-MIB", "dot1agCfmMaNetFormat"),
        ("IEEE8021-CFM-MIB", "dot1agCfmMaNetName"),
        ("IEEE8021-CFM-MIB", "dot1agCfmMaCompPrimaryVlanId"),
        ("IEEE8021-CFM-MIB", "dot1agCfmMepDirection"),
        ("IEEE8021-CFM-MIB", "dot1agCfmMepPrimaryVid"))
)
if mibBuilder.loadTexts:
    adGenEthCfmXconCCMSet.setStatus(
        "current"
    )

adGenEthCfmXconCCMClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 75, 1, 0, 10)
)
adGenEthCfmXconCCMClear.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("IEEE8021-CFM-MIB", "dot1agCfmMepIfIndex"),
        ("IF-MIB", "ifDescr"),
        ("IEEE8021-CFM-MIB", "dot1agCfmMdFormat"),
        ("IEEE8021-CFM-MIB", "dot1agCfmMdName"),
        ("IEEE8021-CFM-MIB", "dot1agCfmMdMdLevel"),
        ("IEEE8021-CFM-MIB", "dot1agCfmMaNetFormat"),
        ("IEEE8021-CFM-MIB", "dot1agCfmMaNetName"),
        ("IEEE8021-CFM-MIB", "dot1agCfmMaCompPrimaryVlanId"),
        ("IEEE8021-CFM-MIB", "dot1agCfmMepDirection"),
        ("IEEE8021-CFM-MIB", "dot1agCfmMepPrimaryVid"))
)
if mibBuilder.loadTexts:
    adGenEthCfmXconCCMClear.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ADTRAN-GEN-ETHERNET-CFM-MIB",
    **{"AdGenEthCfmMaNetEntryMepDbRule": AdGenEthCfmMaNetEntryMepDbRule,
       "AdGenEthCfmRemoteMepState": AdGenEthCfmRemoteMepState,
       "AdGenEthCfmRMepProvisioningState": AdGenEthCfmRMepProvisioningState,
       "AdGenEthCfmRMepLockClear": AdGenEthCfmRMepLockClear,
       "adGenEthCfmNotifications": adGenEthCfmNotifications,
       "adGenEthCfmRDISet": adGenEthCfmRDISet,
       "adGenEthCfmRDIClear": adGenEthCfmRDIClear,
       "adGenEthCfmMacStatusSet": adGenEthCfmMacStatusSet,
       "adGenEthCfmMacStatusClear": adGenEthCfmMacStatusClear,
       "adGenEthCfmRemoteCCMSet": adGenEthCfmRemoteCCMSet,
       "adGenEthCfmRemoteCCMClear": adGenEthCfmRemoteCCMClear,
       "adGenEthCfmErroredCCMSet": adGenEthCfmErroredCCMSet,
       "adGenEthCfmErroredCCMClear": adGenEthCfmErroredCCMClear,
       "adGenEthCfmXconCCMSet": adGenEthCfmXconCCMSet,
       "adGenEthCfmXconCCMClear": adGenEthCfmXconCCMClear,
       "adGenEthCfmMIBObjects": adGenEthCfmMIBObjects,
       "adGenEthCfmSystem": adGenEthCfmSystem,
       "adGenEthCfmEnabled": adGenEthCfmEnabled,
       "adGenEthCfmProvisioningUpdates": adGenEthCfmProvisioningUpdates,
       "adGenEthCfmLinkTraceCacheTimeout": adGenEthCfmLinkTraceCacheTimeout,
       "adGenEthCfmLinkTraceCacheSize": adGenEthCfmLinkTraceCacheSize,
       "adGenEthCfmDefaultMd": adGenEthCfmDefaultMd,
       "adGenEthCfmDefaultMdLastCreateError": adGenEthCfmDefaultMdLastCreateError,
       "adGenEthCfmVlan": adGenEthCfmVlan,
       "adGenEthCfmVlanTable": adGenEthCfmVlanTable,
       "adGenEthCfmVlanEntry": adGenEthCfmVlanEntry,
       "adGenEthCfmVlanErrorStatus": adGenEthCfmVlanErrorStatus,
       "adGenEthCfmMd": adGenEthCfmMd,
       "adGenEthCfmMdMaxNumber": adGenEthCfmMdMaxNumber,
       "adGenEthCfmMdCurrentNumber": adGenEthCfmMdCurrentNumber,
       "adGenEthCfmMdLastCreateError": adGenEthCfmMdLastCreateError,
       "adGenEthCfmMdTable": adGenEthCfmMdTable,
       "adGenEthCfmMdEntry": adGenEthCfmMdEntry,
       "adGenEthCfmMdErrorStatus": adGenEthCfmMdErrorStatus,
       "adGenEthCfmMdCfmEnabled": adGenEthCfmMdCfmEnabled,
       "adGenEthCfmMdCcmEnabled": adGenEthCfmMdCcmEnabled,
       "adGenEthCfmMa": adGenEthCfmMa,
       "adGenEthCfmMaMaxNumber": adGenEthCfmMaMaxNumber,
       "adGenEthCfmMaCurrentNumber": adGenEthCfmMaCurrentNumber,
       "adGenEthCfmMaNet": adGenEthCfmMaNet,
       "adGenEthCfmMaNetLastCreateError": adGenEthCfmMaNetLastCreateError,
       "adGenEthCfmMaNetTable": adGenEthCfmMaNetTable,
       "adGenEthCfmMaNetEntry": adGenEthCfmMaNetEntry,
       "adGenEthCfmMaNetErrorStatus": adGenEthCfmMaNetErrorStatus,
       "adGenEthCfmMaNetCfmEnabled": adGenEthCfmMaNetCfmEnabled,
       "adGenEthCfmMaNetCcmEnabled": adGenEthCfmMaNetCcmEnabled,
       "adGenEthCfmMaNetMepDbRule": adGenEthCfmMaNetMepDbRule,
       "adGenEthCfmMaNetRMepHoldTime": adGenEthCfmMaNetRMepHoldTime,
       "adGenEthCfmMaComp": adGenEthCfmMaComp,
       "adGenEthCfmMaCompLastCreateError": adGenEthCfmMaCompLastCreateError,
       "adGenEthCfmMaCompTable": adGenEthCfmMaCompTable,
       "adGenEthCfmMaCompEntry": adGenEthCfmMaCompEntry,
       "adGenEthCfmMaCompErrorStatus": adGenEthCfmMaCompErrorStatus,
       "adGenEthCfmMaMepList": adGenEthCfmMaMepList,
       "adGenEthCfmMaMepListLastCreateError": adGenEthCfmMaMepListLastCreateError,
       "adGenEthCfmMaMepListTable": adGenEthCfmMaMepListTable,
       "adGenEthCfmMaMepListEntry": adGenEthCfmMaMepListEntry,
       "adGenEthCfmMaMepListErrorStatus": adGenEthCfmMaMepListErrorStatus,
       "adGenEthCfmMep": adGenEthCfmMep,
       "adGenEthCfmMepMaxNumber": adGenEthCfmMepMaxNumber,
       "adGenEthCfmMepCurrentNumber": adGenEthCfmMepCurrentNumber,
       "adGenEthCfmMepLastCreateError": adGenEthCfmMepLastCreateError,
       "adGenEthCfmMepTable": adGenEthCfmMepTable,
       "adGenEthCfmMepEntry": adGenEthCfmMepEntry,
       "adGenEthCfmMepLoopbackErrorStatus": adGenEthCfmMepLoopbackErrorStatus,
       "adGenEthCfmMepLoopbackTimeout": adGenEthCfmMepLoopbackTimeout,
       "adGenEthCfmMepLoopbackInterframeDelay": adGenEthCfmMepLoopbackInterframeDelay,
       "adGenEthCfmMepErrorStatus": adGenEthCfmMepErrorStatus,
       "adGenEthCfmMepLinkTraceErrorStatus": adGenEthCfmMepLinkTraceErrorStatus,
       "adGenEthCfmMepLbrResponseTimeMin": adGenEthCfmMepLbrResponseTimeMin,
       "adGenEthCfmMepLbrResponseTimeMax": adGenEthCfmMepLbrResponseTimeMax,
       "adGenEthCfmMepLbrResponseTimeAvg": adGenEthCfmMepLbrResponseTimeAvg,
       "adGenEthCfmMepLoopbackCancel": adGenEthCfmMepLoopbackCancel,
       "adGenEthCfmMepTransmitLtmStatus": adGenEthCfmMepTransmitLtmStatus,
       "adGenEthCfmMepLinkAwarenessPeers": adGenEthCfmMepLinkAwarenessPeers,
       "adGenEthCfmMepLinkAwarenessMode": adGenEthCfmMepLinkAwarenessMode,
       "adGenEthCfmMepLinkTraceTable": adGenEthCfmMepLinkTraceTable,
       "adGenEthCfmMepLinkTraceEntry": adGenEthCfmMepLinkTraceEntry,
       "adGenEthCfmMepLinkTraceTimeRemaining": adGenEthCfmMepLinkTraceTimeRemaining,
       "adGenEthCfmMepDbTable": adGenEthCfmMepDbTable,
       "adGenEthCfmMepDbEntry": adGenEthCfmMepDbEntry,
       "adGenEthCfmMepDbRMepState": adGenEthCfmMepDbRMepState,
       "adGenEthCfmMepDbRMepProvisioningState": adGenEthCfmMepDbRMepProvisioningState,
       "adGenEthCfmMepDbRMepEdit": adGenEthCfmMepDbRMepEdit,
       "adGenEthCfmMib": adGenEthCfmMib}
)
