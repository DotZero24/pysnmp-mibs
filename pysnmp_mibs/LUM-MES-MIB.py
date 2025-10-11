# SNMP MIB module (LUM-MES-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/LUM-MES-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:17:04 2025
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

(lumMesMIB,
 lumModules) = mibBuilder.importSymbols(
    "LUM-REG",
    "lumMesMIB",
    "lumModules")

(BoardOrInterfaceAdminStatus,
 BoardOrInterfaceOperStatus,
 CommandString,
 FaultStatus,
 MgmtNameString,
 ObjectProperty,
 PortNumber,
 ServiceIdWithNotUsed,
 SlotNumber,
 SubrackNumber) = mibBuilder.importSymbols(
    "LUM-TC",
    "BoardOrInterfaceAdminStatus",
    "BoardOrInterfaceOperStatus",
    "CommandString",
    "FaultStatus",
    "MgmtNameString",
    "ObjectProperty",
    "PortNumber",
    "ServiceIdWithNotUsed",
    "SlotNumber",
    "SubrackNumber")

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
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

lumMesMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 1, 1, 32)
)
if mibBuilder.loadTexts:
    lumMesMIBModule.setRevisions(
        ("2018-12-21 00:00",
         "2018-05-31 00:00",
         "2018-02-06 00:00",
         "2017-12-15 00:00",
         "2017-06-15 00:00",
         "2016-11-17 00:00",
         "2016-10-31 00:00",
         "2016-04-30 00:00",
         "2016-01-11 00:00",
         "2015-12-15 00:00",
         "2015-04-15 00:00",
         "2015-02-11 00:00",
         "2015-01-15 00:00",
         "2014-10-29 00:00",
         "2014-08-16 00:00",
         "2014-05-16 00:00",
         "2013-11-01 00:00",
         "2013-05-01 00:00",
         "2012-12-20 00:00",
         "2012-03-30 00:00",
         "2011-12-20 00:00",
         "2011-07-04 00:00",
         "2011-04-21 00:00",
         "2008-02-26 00:00",
         "2008-02-21 00:00",
         "2008-01-30 00:00",
         "2007-11-15 00:00",
         "2007-11-09 00:00",
         "2007-10-25 00:00",
         "2007-04-17 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class MesQProfileId(TextualConvention, Integer32):
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
              9,
              10,
              11,
              12,
              13,
              14)
        )
    )
    namedValues = NamedValues(
        *(("strict1", 1),
          ("strict2", 2),
          ("strict3", 3),
          ("strict4", 4),
          ("strict5", 5),
          ("strict6", 6),
          ("wrr1", 7),
          ("wrr2", 8),
          ("wrr3", 9),
          ("wrr4", 10),
          ("wrr5", 11),
          ("wrr6", 12),
          ("wrr7", 13),
          ("wrr8", 14))
    )



class Dot1agCfmMaintDomainNameType(TextualConvention, Integer32):
    status = "current"
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
          ("dnsLikeName", 2),
          ("macAddressAndUint", 3),
          ("charString", 4))
    )



class Dot1agCfmMaintDomainName(TextualConvention, OctetString):
    status = "current"
    displayHint = "43a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 43),
    )



class Dot1agCfmMaintAssocNameType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              32)
        )
    )
    namedValues = NamedValues(
        *(("primaryVid", 1),
          ("charString", 2),
          ("unsignedInt16", 3),
          ("rfc2685VpnId", 4),
          ("icc", 32))
    )



class Dot1agCfmMaintAssocName(TextualConvention, OctetString):
    status = "current"
    displayHint = "45a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 45),
    )



class Dot1agCfmMDLevel(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )



class Dot1agCfmMDLevelOrNone(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 7),
    )



class Dot1agCfmMpDirection(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 1),
          ("up", 2))
    )



class Dot1agCfmCcmInterval(TextualConvention, Integer32):
    status = "current"
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("intervalInvalid", 0),
          ("interval300Hz", 1),
          ("interval10ms", 2),
          ("interval100ms", 3),
          ("interval1s", 4),
          ("interval10s", 5),
          ("interval1min", 6),
          ("interval10min", 7))
    )



class Dot1agCfmMepId(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8191),
    )



class MesLacpLinkProtectionValue(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("onePlusOne", 1))
    )



# MIB Managed Objects in the order of their OIDs

_LumMesConfs_ObjectIdentity = ObjectIdentity
lumMesConfs = _LumMesConfs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 1)
)
_LumMesGroups_ObjectIdentity = ObjectIdentity
lumMesGroups = _LumMesGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 1, 1)
)
_LumMesCompl_ObjectIdentity = ObjectIdentity
lumMesCompl = _LumMesCompl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 1, 2)
)
_LumMesMIBObjects_ObjectIdentity = ObjectIdentity
lumMesMIBObjects = _LumMesMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2)
)
_MesGeneral_ObjectIdentity = ObjectIdentity
mesGeneral = _MesGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 1)
)
_MesGeneralConfigLastChangeTime_Type = DateAndTime
_MesGeneralConfigLastChangeTime_Object = MibScalar
mesGeneralConfigLastChangeTime = _MesGeneralConfigLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 1, 1),
    _MesGeneralConfigLastChangeTime_Type()
)
mesGeneralConfigLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesGeneralConfigLastChangeTime.setStatus("current")
_MesGeneralStateLastChangeTime_Type = DateAndTime
_MesGeneralStateLastChangeTime_Object = MibScalar
mesGeneralStateLastChangeTime = _MesGeneralStateLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 1, 2),
    _MesGeneralStateLastChangeTime_Type()
)
mesGeneralStateLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesGeneralStateLastChangeTime.setStatus("current")
_MesGeneralUniTableSize_Type = Unsigned32
_MesGeneralUniTableSize_Object = MibScalar
mesGeneralUniTableSize = _MesGeneralUniTableSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 1, 3),
    _MesGeneralUniTableSize_Type()
)
mesGeneralUniTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesGeneralUniTableSize.setStatus("obsolete")
_MesGeneralNniTableSize_Type = Unsigned32
_MesGeneralNniTableSize_Object = MibScalar
mesGeneralNniTableSize = _MesGeneralNniTableSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 1, 4),
    _MesGeneralNniTableSize_Type()
)
mesGeneralNniTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesGeneralNniTableSize.setStatus("obsolete")
_MesGeneralEvcTableSize_Type = Unsigned32
_MesGeneralEvcTableSize_Object = MibScalar
mesGeneralEvcTableSize = _MesGeneralEvcTableSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 1, 5),
    _MesGeneralEvcTableSize_Type()
)
mesGeneralEvcTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesGeneralEvcTableSize.setStatus("obsolete")
_MesGeneralBwpTableSize_Type = Unsigned32
_MesGeneralBwpTableSize_Object = MibScalar
mesGeneralBwpTableSize = _MesGeneralBwpTableSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 1, 6),
    _MesGeneralBwpTableSize_Type()
)
mesGeneralBwpTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesGeneralBwpTableSize.setStatus("current")
_MesGeneralCeEvcMapTableSize_Type = Unsigned32
_MesGeneralCeEvcMapTableSize_Object = MibScalar
mesGeneralCeEvcMapTableSize = _MesGeneralCeEvcMapTableSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 1, 7),
    _MesGeneralCeEvcMapTableSize_Type()
)
mesGeneralCeEvcMapTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesGeneralCeEvcMapTableSize.setStatus("obsolete")
_MesGeneralMepTableSize_Type = Unsigned32
_MesGeneralMepTableSize_Object = MibScalar
mesGeneralMepTableSize = _MesGeneralMepTableSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 1, 8),
    _MesGeneralMepTableSize_Type()
)
mesGeneralMepTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesGeneralMepTableSize.setStatus("obsolete")
_MesGeneralMegTableSize_Type = Unsigned32
_MesGeneralMegTableSize_Object = MibScalar
mesGeneralMegTableSize = _MesGeneralMegTableSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 1, 9),
    _MesGeneralMegTableSize_Type()
)
mesGeneralMegTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesGeneralMegTableSize.setStatus("obsolete")
_MesGeneralEvcBwpMapTableSize_Type = Unsigned32
_MesGeneralEvcBwpMapTableSize_Object = MibScalar
mesGeneralEvcBwpMapTableSize = _MesGeneralEvcBwpMapTableSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 1, 10),
    _MesGeneralEvcBwpMapTableSize_Type()
)
mesGeneralEvcBwpMapTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesGeneralEvcBwpMapTableSize.setStatus("obsolete")
_MesGeneralPortTableSize_Type = Unsigned32
_MesGeneralPortTableSize_Object = MibScalar
mesGeneralPortTableSize = _MesGeneralPortTableSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 1, 11),
    _MesGeneralPortTableSize_Type()
)
mesGeneralPortTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesGeneralPortTableSize.setStatus("current")
_MesGeneralVlanMapTableSize_Type = Unsigned32
_MesGeneralVlanMapTableSize_Object = MibScalar
mesGeneralVlanMapTableSize = _MesGeneralVlanMapTableSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 1, 12),
    _MesGeneralVlanMapTableSize_Type()
)
mesGeneralVlanMapTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesGeneralVlanMapTableSize.setStatus("current")
_MesGeneralMgmtVlanTableSize_Type = Unsigned32
_MesGeneralMgmtVlanTableSize_Object = MibScalar
mesGeneralMgmtVlanTableSize = _MesGeneralMgmtVlanTableSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 1, 13),
    _MesGeneralMgmtVlanTableSize_Type()
)
mesGeneralMgmtVlanTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesGeneralMgmtVlanTableSize.setStatus("current")
_MesGeneralLagTableSize_Type = Unsigned32
_MesGeneralLagTableSize_Object = MibScalar
mesGeneralLagTableSize = _MesGeneralLagTableSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 1, 14),
    _MesGeneralLagTableSize_Type()
)
mesGeneralLagTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesGeneralLagTableSize.setStatus("current")
_MesGeneralPolicingTableSize_Type = Unsigned32
_MesGeneralPolicingTableSize_Object = MibScalar
mesGeneralPolicingTableSize = _MesGeneralPolicingTableSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 1, 15),
    _MesGeneralPolicingTableSize_Type()
)
mesGeneralPolicingTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesGeneralPolicingTableSize.setStatus("current")
_MesGeneralShapingTableSize_Type = Unsigned32
_MesGeneralShapingTableSize_Object = MibScalar
mesGeneralShapingTableSize = _MesGeneralShapingTableSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 1, 16),
    _MesGeneralShapingTableSize_Type()
)
mesGeneralShapingTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesGeneralShapingTableSize.setStatus("current")
_MesGeneralBwpMapTableSize_Type = Unsigned32
_MesGeneralBwpMapTableSize_Object = MibScalar
mesGeneralBwpMapTableSize = _MesGeneralBwpMapTableSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 1, 17),
    _MesGeneralBwpMapTableSize_Type()
)
mesGeneralBwpMapTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesGeneralBwpMapTableSize.setStatus("current")
_MesGeneralCosTableSize_Type = Unsigned32
_MesGeneralCosTableSize_Object = MibScalar
mesGeneralCosTableSize = _MesGeneralCosTableSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 1, 18),
    _MesGeneralCosTableSize_Type()
)
mesGeneralCosTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesGeneralCosTableSize.setStatus("current")
_MesGeneralMirroringTableSize_Type = Unsigned32
_MesGeneralMirroringTableSize_Object = MibScalar
mesGeneralMirroringTableSize = _MesGeneralMirroringTableSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 1, 19),
    _MesGeneralMirroringTableSize_Type()
)
mesGeneralMirroringTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesGeneralMirroringTableSize.setStatus("current")
_MesGeneralVlanTagRuleTableSize_Type = Unsigned32
_MesGeneralVlanTagRuleTableSize_Object = MibScalar
mesGeneralVlanTagRuleTableSize = _MesGeneralVlanTagRuleTableSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 1, 20),
    _MesGeneralVlanTagRuleTableSize_Type()
)
mesGeneralVlanTagRuleTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesGeneralVlanTagRuleTableSize.setStatus("current")
_MesGeneralVlanTagClassVlanTableSize_Type = Unsigned32
_MesGeneralVlanTagClassVlanTableSize_Object = MibScalar
mesGeneralVlanTagClassVlanTableSize = _MesGeneralVlanTagClassVlanTableSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 1, 21),
    _MesGeneralVlanTagClassVlanTableSize_Type()
)
mesGeneralVlanTagClassVlanTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesGeneralVlanTagClassVlanTableSize.setStatus("current")
_MesGeneralCosProfileTableSize_Type = Unsigned32
_MesGeneralCosProfileTableSize_Object = MibScalar
mesGeneralCosProfileTableSize = _MesGeneralCosProfileTableSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 1, 22),
    _MesGeneralCosProfileTableSize_Type()
)
mesGeneralCosProfileTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesGeneralCosProfileTableSize.setStatus("current")
_MesGeneralMaidTableSize_Type = Unsigned32
_MesGeneralMaidTableSize_Object = MibScalar
mesGeneralMaidTableSize = _MesGeneralMaidTableSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 1, 23),
    _MesGeneralMaidTableSize_Type()
)
mesGeneralMaidTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesGeneralMaidTableSize.setStatus("current")
_MesGeneralCfmMepTableSize_Type = Unsigned32
_MesGeneralCfmMepTableSize_Object = MibScalar
mesGeneralCfmMepTableSize = _MesGeneralCfmMepTableSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 1, 24),
    _MesGeneralCfmMepTableSize_Type()
)
mesGeneralCfmMepTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesGeneralCfmMepTableSize.setStatus("current")
_MesGeneralErpTableSize_Type = Unsigned32
_MesGeneralErpTableSize_Object = MibScalar
mesGeneralErpTableSize = _MesGeneralErpTableSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 1, 25),
    _MesGeneralErpTableSize_Type()
)
mesGeneralErpTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesGeneralErpTableSize.setStatus("current")
_MesGeneralClassTableSize_Type = Unsigned32
_MesGeneralClassTableSize_Object = MibScalar
mesGeneralClassTableSize = _MesGeneralClassTableSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 1, 26),
    _MesGeneralClassTableSize_Type()
)
mesGeneralClassTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesGeneralClassTableSize.setStatus("current")
_MesGeneralActionTableSize_Type = Unsigned32
_MesGeneralActionTableSize_Object = MibScalar
mesGeneralActionTableSize = _MesGeneralActionTableSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 1, 27),
    _MesGeneralActionTableSize_Type()
)
mesGeneralActionTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesGeneralActionTableSize.setStatus("current")
_MesGeneralPolicyTableSize_Type = Unsigned32
_MesGeneralPolicyTableSize_Object = MibScalar
mesGeneralPolicyTableSize = _MesGeneralPolicyTableSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 1, 28),
    _MesGeneralPolicyTableSize_Type()
)
mesGeneralPolicyTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesGeneralPolicyTableSize.setStatus("current")
_MesGeneralErrorPropTableSize_Type = Unsigned32
_MesGeneralErrorPropTableSize_Object = MibScalar
mesGeneralErrorPropTableSize = _MesGeneralErrorPropTableSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 1, 29),
    _MesGeneralErrorPropTableSize_Type()
)
mesGeneralErrorPropTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesGeneralErrorPropTableSize.setStatus("current")
_MesGeneralVlanProtTableSize_Type = Unsigned32
_MesGeneralVlanProtTableSize_Object = MibScalar
mesGeneralVlanProtTableSize = _MesGeneralVlanProtTableSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 1, 30),
    _MesGeneralVlanProtTableSize_Type()
)
mesGeneralVlanProtTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesGeneralVlanProtTableSize.setStatus("current")
_MesGeneralLacpTableSize_Type = Unsigned32
_MesGeneralLacpTableSize_Object = MibScalar
mesGeneralLacpTableSize = _MesGeneralLacpTableSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 1, 31),
    _MesGeneralLacpTableSize_Type()
)
mesGeneralLacpTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesGeneralLacpTableSize.setStatus("current")
_MesGeneralLagStateLastChangeTime_Type = DateAndTime
_MesGeneralLagStateLastChangeTime_Object = MibScalar
mesGeneralLagStateLastChangeTime = _MesGeneralLagStateLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 1, 32),
    _MesGeneralLagStateLastChangeTime_Type()
)
mesGeneralLagStateLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesGeneralLagStateLastChangeTime.setStatus("current")
_MesGeneralLagConfigLastChangeTime_Type = DateAndTime
_MesGeneralLagConfigLastChangeTime_Object = MibScalar
mesGeneralLagConfigLastChangeTime = _MesGeneralLagConfigLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 1, 33),
    _MesGeneralLagConfigLastChangeTime_Type()
)
mesGeneralLagConfigLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesGeneralLagConfigLastChangeTime.setStatus("current")
_MesGeneralErpStateLastChangeTime_Type = DateAndTime
_MesGeneralErpStateLastChangeTime_Object = MibScalar
mesGeneralErpStateLastChangeTime = _MesGeneralErpStateLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 1, 34),
    _MesGeneralErpStateLastChangeTime_Type()
)
mesGeneralErpStateLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesGeneralErpStateLastChangeTime.setStatus("current")
_MesGeneralErpConfigLastChangeTime_Type = DateAndTime
_MesGeneralErpConfigLastChangeTime_Object = MibScalar
mesGeneralErpConfigLastChangeTime = _MesGeneralErpConfigLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 1, 35),
    _MesGeneralErpConfigLastChangeTime_Type()
)
mesGeneralErpConfigLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesGeneralErpConfigLastChangeTime.setStatus("current")
_MesGeneralMaidStateLastChangeTime_Type = DateAndTime
_MesGeneralMaidStateLastChangeTime_Object = MibScalar
mesGeneralMaidStateLastChangeTime = _MesGeneralMaidStateLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 1, 36),
    _MesGeneralMaidStateLastChangeTime_Type()
)
mesGeneralMaidStateLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesGeneralMaidStateLastChangeTime.setStatus("current")
_MesGeneralMaidConfigLastChangeTime_Type = DateAndTime
_MesGeneralMaidConfigLastChangeTime_Object = MibScalar
mesGeneralMaidConfigLastChangeTime = _MesGeneralMaidConfigLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 1, 37),
    _MesGeneralMaidConfigLastChangeTime_Type()
)
mesGeneralMaidConfigLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesGeneralMaidConfigLastChangeTime.setStatus("current")
_MesGeneralCfmMepStateLastChangeTime_Type = DateAndTime
_MesGeneralCfmMepStateLastChangeTime_Object = MibScalar
mesGeneralCfmMepStateLastChangeTime = _MesGeneralCfmMepStateLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 1, 38),
    _MesGeneralCfmMepStateLastChangeTime_Type()
)
mesGeneralCfmMepStateLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesGeneralCfmMepStateLastChangeTime.setStatus("current")
_MesGeneralCfmMepConfigLastChangeTime_Type = DateAndTime
_MesGeneralCfmMepConfigLastChangeTime_Object = MibScalar
mesGeneralCfmMepConfigLastChangeTime = _MesGeneralCfmMepConfigLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 1, 39),
    _MesGeneralCfmMepConfigLastChangeTime_Type()
)
mesGeneralCfmMepConfigLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesGeneralCfmMepConfigLastChangeTime.setStatus("current")
_MesGeneralVlanMapStateLastChangeTime_Type = DateAndTime
_MesGeneralVlanMapStateLastChangeTime_Object = MibScalar
mesGeneralVlanMapStateLastChangeTime = _MesGeneralVlanMapStateLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 1, 40),
    _MesGeneralVlanMapStateLastChangeTime_Type()
)
mesGeneralVlanMapStateLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesGeneralVlanMapStateLastChangeTime.setStatus("current")
_MesGeneralVlanMapConfigLastChangeTime_Type = DateAndTime
_MesGeneralVlanMapConfigLastChangeTime_Object = MibScalar
mesGeneralVlanMapConfigLastChangeTime = _MesGeneralVlanMapConfigLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 1, 41),
    _MesGeneralVlanMapConfigLastChangeTime_Type()
)
mesGeneralVlanMapConfigLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesGeneralVlanMapConfigLastChangeTime.setStatus("current")
_MesGeneralMgmtVlanStateLastChangeTime_Type = DateAndTime
_MesGeneralMgmtVlanStateLastChangeTime_Object = MibScalar
mesGeneralMgmtVlanStateLastChangeTime = _MesGeneralMgmtVlanStateLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 1, 42),
    _MesGeneralMgmtVlanStateLastChangeTime_Type()
)
mesGeneralMgmtVlanStateLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesGeneralMgmtVlanStateLastChangeTime.setStatus("current")
_MesGeneralMgmtVlanConfigLastChangeTime_Type = DateAndTime
_MesGeneralMgmtVlanConfigLastChangeTime_Object = MibScalar
mesGeneralMgmtVlanConfigLastChangeTime = _MesGeneralMgmtVlanConfigLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 1, 43),
    _MesGeneralMgmtVlanConfigLastChangeTime_Type()
)
mesGeneralMgmtVlanConfigLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesGeneralMgmtVlanConfigLastChangeTime.setStatus("current")
_MesGeneralClassStateLastChangeTime_Type = DateAndTime
_MesGeneralClassStateLastChangeTime_Object = MibScalar
mesGeneralClassStateLastChangeTime = _MesGeneralClassStateLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 1, 44),
    _MesGeneralClassStateLastChangeTime_Type()
)
mesGeneralClassStateLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesGeneralClassStateLastChangeTime.setStatus("current")
_MesGeneralClassConfigLastChangeTime_Type = DateAndTime
_MesGeneralClassConfigLastChangeTime_Object = MibScalar
mesGeneralClassConfigLastChangeTime = _MesGeneralClassConfigLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 1, 45),
    _MesGeneralClassConfigLastChangeTime_Type()
)
mesGeneralClassConfigLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesGeneralClassConfigLastChangeTime.setStatus("current")
_MesGeneralActionStateLastChangeTime_Type = DateAndTime
_MesGeneralActionStateLastChangeTime_Object = MibScalar
mesGeneralActionStateLastChangeTime = _MesGeneralActionStateLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 1, 46),
    _MesGeneralActionStateLastChangeTime_Type()
)
mesGeneralActionStateLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesGeneralActionStateLastChangeTime.setStatus("current")
_MesGeneralActionConfigLastChangeTime_Type = DateAndTime
_MesGeneralActionConfigLastChangeTime_Object = MibScalar
mesGeneralActionConfigLastChangeTime = _MesGeneralActionConfigLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 1, 47),
    _MesGeneralActionConfigLastChangeTime_Type()
)
mesGeneralActionConfigLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesGeneralActionConfigLastChangeTime.setStatus("current")
_MesGeneralPolicyStateLastChangeTime_Type = DateAndTime
_MesGeneralPolicyStateLastChangeTime_Object = MibScalar
mesGeneralPolicyStateLastChangeTime = _MesGeneralPolicyStateLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 1, 48),
    _MesGeneralPolicyStateLastChangeTime_Type()
)
mesGeneralPolicyStateLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesGeneralPolicyStateLastChangeTime.setStatus("current")
_MesGeneralPolicyConfigLastChangeTime_Type = DateAndTime
_MesGeneralPolicyConfigLastChangeTime_Object = MibScalar
mesGeneralPolicyConfigLastChangeTime = _MesGeneralPolicyConfigLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 1, 49),
    _MesGeneralPolicyConfigLastChangeTime_Type()
)
mesGeneralPolicyConfigLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesGeneralPolicyConfigLastChangeTime.setStatus("current")
_MesGeneralErrorPropStateLastChangeTime_Type = DateAndTime
_MesGeneralErrorPropStateLastChangeTime_Object = MibScalar
mesGeneralErrorPropStateLastChangeTime = _MesGeneralErrorPropStateLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 1, 50),
    _MesGeneralErrorPropStateLastChangeTime_Type()
)
mesGeneralErrorPropStateLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesGeneralErrorPropStateLastChangeTime.setStatus("current")
_MesGeneralErrorPropConfigLastChangeTime_Type = DateAndTime
_MesGeneralErrorPropConfigLastChangeTime_Object = MibScalar
mesGeneralErrorPropConfigLastChangeTime = _MesGeneralErrorPropConfigLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 1, 51),
    _MesGeneralErrorPropConfigLastChangeTime_Type()
)
mesGeneralErrorPropConfigLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesGeneralErrorPropConfigLastChangeTime.setStatus("current")
_MesGeneralVlanProtStateLastChangeTime_Type = DateAndTime
_MesGeneralVlanProtStateLastChangeTime_Object = MibScalar
mesGeneralVlanProtStateLastChangeTime = _MesGeneralVlanProtStateLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 1, 52),
    _MesGeneralVlanProtStateLastChangeTime_Type()
)
mesGeneralVlanProtStateLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesGeneralVlanProtStateLastChangeTime.setStatus("current")
_MesGeneralVlanProtConfigLastChangeTime_Type = DateAndTime
_MesGeneralVlanProtConfigLastChangeTime_Object = MibScalar
mesGeneralVlanProtConfigLastChangeTime = _MesGeneralVlanProtConfigLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 1, 53),
    _MesGeneralVlanProtConfigLastChangeTime_Type()
)
mesGeneralVlanProtConfigLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesGeneralVlanProtConfigLastChangeTime.setStatus("current")
_MesGeneralLacpStateLastChangeTime_Type = DateAndTime
_MesGeneralLacpStateLastChangeTime_Object = MibScalar
mesGeneralLacpStateLastChangeTime = _MesGeneralLacpStateLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 1, 54),
    _MesGeneralLacpStateLastChangeTime_Type()
)
mesGeneralLacpStateLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesGeneralLacpStateLastChangeTime.setStatus("current")
_MesGeneralLacpConfigLastChangeTime_Type = DateAndTime
_MesGeneralLacpConfigLastChangeTime_Object = MibScalar
mesGeneralLacpConfigLastChangeTime = _MesGeneralLacpConfigLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 1, 55),
    _MesGeneralLacpConfigLastChangeTime_Type()
)
mesGeneralLacpConfigLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesGeneralLacpConfigLastChangeTime.setStatus("current")
_MesGeneralPolicingStateLastChangeTime_Type = DateAndTime
_MesGeneralPolicingStateLastChangeTime_Object = MibScalar
mesGeneralPolicingStateLastChangeTime = _MesGeneralPolicingStateLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 1, 56),
    _MesGeneralPolicingStateLastChangeTime_Type()
)
mesGeneralPolicingStateLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesGeneralPolicingStateLastChangeTime.setStatus("current")
_MesGeneralPolicingConfigLastChangeTime_Type = DateAndTime
_MesGeneralPolicingConfigLastChangeTime_Object = MibScalar
mesGeneralPolicingConfigLastChangeTime = _MesGeneralPolicingConfigLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 1, 57),
    _MesGeneralPolicingConfigLastChangeTime_Type()
)
mesGeneralPolicingConfigLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesGeneralPolicingConfigLastChangeTime.setStatus("current")
_MesGeneralShapingStateLastChangeTime_Type = DateAndTime
_MesGeneralShapingStateLastChangeTime_Object = MibScalar
mesGeneralShapingStateLastChangeTime = _MesGeneralShapingStateLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 1, 58),
    _MesGeneralShapingStateLastChangeTime_Type()
)
mesGeneralShapingStateLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesGeneralShapingStateLastChangeTime.setStatus("current")
_MesGeneralShapingConfigLastChangeTime_Type = DateAndTime
_MesGeneralShapingConfigLastChangeTime_Object = MibScalar
mesGeneralShapingConfigLastChangeTime = _MesGeneralShapingConfigLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 1, 59),
    _MesGeneralShapingConfigLastChangeTime_Type()
)
mesGeneralShapingConfigLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesGeneralShapingConfigLastChangeTime.setStatus("current")
_MesGeneralCosStateLastChangeTime_Type = DateAndTime
_MesGeneralCosStateLastChangeTime_Object = MibScalar
mesGeneralCosStateLastChangeTime = _MesGeneralCosStateLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 1, 60),
    _MesGeneralCosStateLastChangeTime_Type()
)
mesGeneralCosStateLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesGeneralCosStateLastChangeTime.setStatus("current")
_MesGeneralCosConfigLastChangeTime_Type = DateAndTime
_MesGeneralCosConfigLastChangeTime_Object = MibScalar
mesGeneralCosConfigLastChangeTime = _MesGeneralCosConfigLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 1, 61),
    _MesGeneralCosConfigLastChangeTime_Type()
)
mesGeneralCosConfigLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesGeneralCosConfigLastChangeTime.setStatus("current")
_MesGeneralBwpMapStateLastChangeTime_Type = DateAndTime
_MesGeneralBwpMapStateLastChangeTime_Object = MibScalar
mesGeneralBwpMapStateLastChangeTime = _MesGeneralBwpMapStateLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 1, 62),
    _MesGeneralBwpMapStateLastChangeTime_Type()
)
mesGeneralBwpMapStateLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesGeneralBwpMapStateLastChangeTime.setStatus("current")
_MesGeneralBwpMapConfigLastChangeTime_Type = DateAndTime
_MesGeneralBwpMapConfigLastChangeTime_Object = MibScalar
mesGeneralBwpMapConfigLastChangeTime = _MesGeneralBwpMapConfigLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 1, 63),
    _MesGeneralBwpMapConfigLastChangeTime_Type()
)
mesGeneralBwpMapConfigLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesGeneralBwpMapConfigLastChangeTime.setStatus("current")
_MesGeneralMirroringStateLastChangeTime_Type = DateAndTime
_MesGeneralMirroringStateLastChangeTime_Object = MibScalar
mesGeneralMirroringStateLastChangeTime = _MesGeneralMirroringStateLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 1, 64),
    _MesGeneralMirroringStateLastChangeTime_Type()
)
mesGeneralMirroringStateLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesGeneralMirroringStateLastChangeTime.setStatus("current")
_MesGeneralMirroringConfigLastChangeTime_Type = DateAndTime
_MesGeneralMirroringConfigLastChangeTime_Object = MibScalar
mesGeneralMirroringConfigLastChangeTime = _MesGeneralMirroringConfigLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 1, 65),
    _MesGeneralMirroringConfigLastChangeTime_Type()
)
mesGeneralMirroringConfigLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesGeneralMirroringConfigLastChangeTime.setStatus("current")
_MesGeneralVlanTagRuleStateLastChangeTime_Type = DateAndTime
_MesGeneralVlanTagRuleStateLastChangeTime_Object = MibScalar
mesGeneralVlanTagRuleStateLastChangeTime = _MesGeneralVlanTagRuleStateLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 1, 66),
    _MesGeneralVlanTagRuleStateLastChangeTime_Type()
)
mesGeneralVlanTagRuleStateLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesGeneralVlanTagRuleStateLastChangeTime.setStatus("current")
_MesGeneralVlanTagRuleConfigLastChangeTime_Type = DateAndTime
_MesGeneralVlanTagRuleConfigLastChangeTime_Object = MibScalar
mesGeneralVlanTagRuleConfigLastChangeTime = _MesGeneralVlanTagRuleConfigLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 1, 67),
    _MesGeneralVlanTagRuleConfigLastChangeTime_Type()
)
mesGeneralVlanTagRuleConfigLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesGeneralVlanTagRuleConfigLastChangeTime.setStatus("current")
_MesGeneralVlanTagClassVlanStateLastChangeTime_Type = DateAndTime
_MesGeneralVlanTagClassVlanStateLastChangeTime_Object = MibScalar
mesGeneralVlanTagClassVlanStateLastChangeTime = _MesGeneralVlanTagClassVlanStateLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 1, 68),
    _MesGeneralVlanTagClassVlanStateLastChangeTime_Type()
)
mesGeneralVlanTagClassVlanStateLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesGeneralVlanTagClassVlanStateLastChangeTime.setStatus("current")
_MesGeneralVlanTagClassVlanConfigLastChangeTime_Type = DateAndTime
_MesGeneralVlanTagClassVlanConfigLastChangeTime_Object = MibScalar
mesGeneralVlanTagClassVlanConfigLastChangeTime = _MesGeneralVlanTagClassVlanConfigLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 1, 69),
    _MesGeneralVlanTagClassVlanConfigLastChangeTime_Type()
)
mesGeneralVlanTagClassVlanConfigLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesGeneralVlanTagClassVlanConfigLastChangeTime.setStatus("current")
_MesGeneralCosProfileStateLastChangeTime_Type = DateAndTime
_MesGeneralCosProfileStateLastChangeTime_Object = MibScalar
mesGeneralCosProfileStateLastChangeTime = _MesGeneralCosProfileStateLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 1, 70),
    _MesGeneralCosProfileStateLastChangeTime_Type()
)
mesGeneralCosProfileStateLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesGeneralCosProfileStateLastChangeTime.setStatus("current")
_MesGeneralCosProfileConfigLastChangeTime_Type = DateAndTime
_MesGeneralCosProfileConfigLastChangeTime_Object = MibScalar
mesGeneralCosProfileConfigLastChangeTime = _MesGeneralCosProfileConfigLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 1, 71),
    _MesGeneralCosProfileConfigLastChangeTime_Type()
)
mesGeneralCosProfileConfigLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesGeneralCosProfileConfigLastChangeTime.setStatus("current")
_MesGeneralBwpStateLastChangeTime_Type = DateAndTime
_MesGeneralBwpStateLastChangeTime_Object = MibScalar
mesGeneralBwpStateLastChangeTime = _MesGeneralBwpStateLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 1, 72),
    _MesGeneralBwpStateLastChangeTime_Type()
)
mesGeneralBwpStateLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesGeneralBwpStateLastChangeTime.setStatus("current")
_MesGeneralBwpConfigLastChangeTime_Type = DateAndTime
_MesGeneralBwpConfigLastChangeTime_Object = MibScalar
mesGeneralBwpConfigLastChangeTime = _MesGeneralBwpConfigLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 1, 73),
    _MesGeneralBwpConfigLastChangeTime_Type()
)
mesGeneralBwpConfigLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesGeneralBwpConfigLastChangeTime.setStatus("current")
_MesGeneralMiscStateLastChangeTime_Type = DateAndTime
_MesGeneralMiscStateLastChangeTime_Object = MibScalar
mesGeneralMiscStateLastChangeTime = _MesGeneralMiscStateLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 1, 74),
    _MesGeneralMiscStateLastChangeTime_Type()
)
mesGeneralMiscStateLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesGeneralMiscStateLastChangeTime.setStatus("current")
_MesGeneralMiscConfigLastChangeTime_Type = DateAndTime
_MesGeneralMiscConfigLastChangeTime_Object = MibScalar
mesGeneralMiscConfigLastChangeTime = _MesGeneralMiscConfigLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 1, 75),
    _MesGeneralMiscConfigLastChangeTime_Type()
)
mesGeneralMiscConfigLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesGeneralMiscConfigLastChangeTime.setStatus("current")
_MesGeneralPortStateLastChangeTime_Type = DateAndTime
_MesGeneralPortStateLastChangeTime_Object = MibScalar
mesGeneralPortStateLastChangeTime = _MesGeneralPortStateLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 1, 76),
    _MesGeneralPortStateLastChangeTime_Type()
)
mesGeneralPortStateLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesGeneralPortStateLastChangeTime.setStatus("current")
_MesGeneralPortConfigLastChangeTime_Type = DateAndTime
_MesGeneralPortConfigLastChangeTime_Object = MibScalar
mesGeneralPortConfigLastChangeTime = _MesGeneralPortConfigLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 1, 77),
    _MesGeneralPortConfigLastChangeTime_Type()
)
mesGeneralPortConfigLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesGeneralPortConfigLastChangeTime.setStatus("current")
_MesUniList_ObjectIdentity = ObjectIdentity
mesUniList = _MesUniList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 2)
)
_MesUniTable_Object = MibTable
mesUniTable = _MesUniTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 2, 1)
)
if mibBuilder.loadTexts:
    mesUniTable.setStatus("obsolete")
_MesUniEntry_Object = MibTableRow
mesUniEntry = _MesUniEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 2, 1, 1)
)
mesUniEntry.setIndexNames(
    (0, "LUM-MES-MIB", "mesUniIndex"),
)
if mibBuilder.loadTexts:
    mesUniEntry.setStatus("current")


class _MesUniIndex_Type(Unsigned32):
    """Custom type mesUniIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_MesUniIndex_Type.__name__ = "Unsigned32"
_MesUniIndex_Object = MibTableColumn
mesUniIndex = _MesUniIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 2, 1, 1, 1),
    _MesUniIndex_Type()
)
mesUniIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesUniIndex.setStatus("current")
_MesUniName_Type = MgmtNameString
_MesUniName_Object = MibTableColumn
mesUniName = _MesUniName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 2, 1, 1, 2),
    _MesUniName_Type()
)
mesUniName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesUniName.setStatus("current")


class _MesUniDescr_Type(DisplayString):
    """Custom type mesUniDescr based on DisplayString"""
    defaultValue = OctetString("")


_MesUniDescr_Type.__name__ = "DisplayString"
_MesUniDescr_Object = MibTableColumn
mesUniDescr = _MesUniDescr_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 2, 1, 1, 3),
    _MesUniDescr_Type()
)
mesUniDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mesUniDescr.setStatus("current")
_MesUniSubrack_Type = SubrackNumber
_MesUniSubrack_Object = MibTableColumn
mesUniSubrack = _MesUniSubrack_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 2, 1, 1, 4),
    _MesUniSubrack_Type()
)
mesUniSubrack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesUniSubrack.setStatus("current")
_MesUniSlot_Type = SlotNumber
_MesUniSlot_Object = MibTableColumn
mesUniSlot = _MesUniSlot_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 2, 1, 1, 5),
    _MesUniSlot_Type()
)
mesUniSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesUniSlot.setStatus("current")
_MesUniTxPort_Type = PortNumber
_MesUniTxPort_Object = MibTableColumn
mesUniTxPort = _MesUniTxPort_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 2, 1, 1, 6),
    _MesUniTxPort_Type()
)
mesUniTxPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesUniTxPort.setStatus("current")
_MesUniRxPort_Type = PortNumber
_MesUniRxPort_Object = MibTableColumn
mesUniRxPort = _MesUniRxPort_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 2, 1, 1, 7),
    _MesUniRxPort_Type()
)
mesUniRxPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesUniRxPort.setStatus("current")
_MesUniObjectProperty_Type = ObjectProperty
_MesUniObjectProperty_Object = MibTableColumn
mesUniObjectProperty = _MesUniObjectProperty_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 2, 1, 1, 8),
    _MesUniObjectProperty_Type()
)
mesUniObjectProperty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesUniObjectProperty.setStatus("current")


class _MesUniAdminStatus_Type(BoardOrInterfaceAdminStatus):
    """Custom type mesUniAdminStatus based on BoardOrInterfaceAdminStatus"""
    defaultValue = 3


_MesUniAdminStatus_Type.__name__ = "BoardOrInterfaceAdminStatus"
_MesUniAdminStatus_Object = MibTableColumn
mesUniAdminStatus = _MesUniAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 2, 1, 1, 9),
    _MesUniAdminStatus_Type()
)
mesUniAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mesUniAdminStatus.setStatus("current")


class _MesUniOperStatus_Type(BoardOrInterfaceOperStatus):
    """Custom type mesUniOperStatus based on BoardOrInterfaceOperStatus"""
    defaultValue = 1


_MesUniOperStatus_Type.__name__ = "BoardOrInterfaceOperStatus"
_MesUniOperStatus_Object = MibTableColumn
mesUniOperStatus = _MesUniOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 2, 1, 1, 10),
    _MesUniOperStatus_Type()
)
mesUniOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesUniOperStatus.setStatus("current")


class _MesUniIdentifier_Type(DisplayString):
    """Custom type mesUniIdentifier based on DisplayString"""
    defaultValue = OctetString("")


_MesUniIdentifier_Type.__name__ = "DisplayString"
_MesUniIdentifier_Object = MibTableColumn
mesUniIdentifier = _MesUniIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 2, 1, 1, 11),
    _MesUniIdentifier_Type()
)
mesUniIdentifier.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesUniIdentifier.setStatus("current")


class _MesUniMtuSize_Type(Unsigned32):
    """Custom type mesUniMtuSize based on Unsigned32"""
    defaultValue = 1518

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1518, 9600),
    )


_MesUniMtuSize_Type.__name__ = "Unsigned32"
_MesUniMtuSize_Object = MibTableColumn
mesUniMtuSize = _MesUniMtuSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 2, 1, 1, 12),
    _MesUniMtuSize_Type()
)
mesUniMtuSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mesUniMtuSize.setStatus("current")


class _MesUniMaxNoOfEvcs_Type(Unsigned32):
    """Custom type mesUniMaxNoOfEvcs based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_MesUniMaxNoOfEvcs_Type.__name__ = "Unsigned32"
_MesUniMaxNoOfEvcs_Object = MibTableColumn
mesUniMaxNoOfEvcs = _MesUniMaxNoOfEvcs_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 2, 1, 1, 13),
    _MesUniMaxNoOfEvcs_Type()
)
mesUniMaxNoOfEvcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesUniMaxNoOfEvcs.setStatus("current")
_MesUniCurrentNoOfEvcs_Type = Unsigned32
_MesUniCurrentNoOfEvcs_Object = MibTableColumn
mesUniCurrentNoOfEvcs = _MesUniCurrentNoOfEvcs_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 2, 1, 1, 14),
    _MesUniCurrentNoOfEvcs_Type()
)
mesUniCurrentNoOfEvcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesUniCurrentNoOfEvcs.setStatus("current")
_MesUniAvailableCapacity_Type = Unsigned32
_MesUniAvailableCapacity_Object = MibTableColumn
mesUniAvailableCapacity = _MesUniAvailableCapacity_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 2, 1, 1, 15),
    _MesUniAvailableCapacity_Type()
)
mesUniAvailableCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesUniAvailableCapacity.setStatus("current")


class _MesUniServiceMultiplexing_Type(Integer32):
    """Custom type mesUniServiceMultiplexing based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_MesUniServiceMultiplexing_Type.__name__ = "Integer32"
_MesUniServiceMultiplexing_Object = MibTableColumn
mesUniServiceMultiplexing = _MesUniServiceMultiplexing_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 2, 1, 1, 16),
    _MesUniServiceMultiplexing_Type()
)
mesUniServiceMultiplexing.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesUniServiceMultiplexing.setStatus("current")


class _MesUniBundling_Type(Integer32):
    """Custom type mesUniBundling based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_MesUniBundling_Type.__name__ = "Integer32"
_MesUniBundling_Object = MibTableColumn
mesUniBundling = _MesUniBundling_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 2, 1, 1, 17),
    _MesUniBundling_Type()
)
mesUniBundling.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesUniBundling.setStatus("current")


class _MesUniAllToOneBundling_Type(Integer32):
    """Custom type mesUniAllToOneBundling based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_MesUniAllToOneBundling_Type.__name__ = "Integer32"
_MesUniAllToOneBundling_Object = MibTableColumn
mesUniAllToOneBundling = _MesUniAllToOneBundling_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 2, 1, 1, 18),
    _MesUniAllToOneBundling_Type()
)
mesUniAllToOneBundling.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesUniAllToOneBundling.setStatus("current")


class _MesUniUntaggedCeVlanIdAssignment_Type(Unsigned32):
    """Custom type mesUniUntaggedCeVlanIdAssignment based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_MesUniUntaggedCeVlanIdAssignment_Type.__name__ = "Unsigned32"
_MesUniUntaggedCeVlanIdAssignment_Object = MibTableColumn
mesUniUntaggedCeVlanIdAssignment = _MesUniUntaggedCeVlanIdAssignment_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 2, 1, 1, 19),
    _MesUniUntaggedCeVlanIdAssignment_Type()
)
mesUniUntaggedCeVlanIdAssignment.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesUniUntaggedCeVlanIdAssignment.setStatus("current")
_MesUniAssociateBwp_Type = CommandString
_MesUniAssociateBwp_Object = MibTableColumn
mesUniAssociateBwp = _MesUniAssociateBwp_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 2, 1, 1, 20),
    _MesUniAssociateBwp_Type()
)
mesUniAssociateBwp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesUniAssociateBwp.setStatus("current")
_MesUniReleaseBwp_Type = CommandString
_MesUniReleaseBwp_Object = MibTableColumn
mesUniReleaseBwp = _MesUniReleaseBwp_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 2, 1, 1, 21),
    _MesUniReleaseBwp_Type()
)
mesUniReleaseBwp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesUniReleaseBwp.setStatus("current")


class _MesUniIngressBwProfilePerUni_Type(Integer32):
    """Custom type mesUniIngressBwProfilePerUni based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_MesUniIngressBwProfilePerUni_Type.__name__ = "Integer32"
_MesUniIngressBwProfilePerUni_Object = MibTableColumn
mesUniIngressBwProfilePerUni = _MesUniIngressBwProfilePerUni_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 2, 1, 1, 22),
    _MesUniIngressBwProfilePerUni_Type()
)
mesUniIngressBwProfilePerUni.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesUniIngressBwProfilePerUni.setStatus("current")


class _MesUniIngressBwp_Type(DisplayString):
    """Custom type mesUniIngressBwp based on DisplayString"""
    defaultValue = OctetString("")


_MesUniIngressBwp_Type.__name__ = "DisplayString"
_MesUniIngressBwp_Object = MibTableColumn
mesUniIngressBwp = _MesUniIngressBwp_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 2, 1, 1, 23),
    _MesUniIngressBwp_Type()
)
mesUniIngressBwp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesUniIngressBwp.setStatus("current")


class _MesUniEgressBwProfilePerUni_Type(Integer32):
    """Custom type mesUniEgressBwProfilePerUni based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_MesUniEgressBwProfilePerUni_Type.__name__ = "Integer32"
_MesUniEgressBwProfilePerUni_Object = MibTableColumn
mesUniEgressBwProfilePerUni = _MesUniEgressBwProfilePerUni_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 2, 1, 1, 24),
    _MesUniEgressBwProfilePerUni_Type()
)
mesUniEgressBwProfilePerUni.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesUniEgressBwProfilePerUni.setStatus("current")


class _MesUniEgressBwp_Type(DisplayString):
    """Custom type mesUniEgressBwp based on DisplayString"""
    defaultValue = OctetString("")


_MesUniEgressBwp_Type.__name__ = "DisplayString"
_MesUniEgressBwp_Object = MibTableColumn
mesUniEgressBwp = _MesUniEgressBwp_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 2, 1, 1, 25),
    _MesUniEgressBwp_Type()
)
mesUniEgressBwp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesUniEgressBwp.setStatus("current")


class _MesUniL2ControlProtocolProcessing_Type(Integer32):
    """Custom type mesUniL2ControlProtocolProcessing based on Integer32"""
    defaultValue = 3

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
        *(("discard", 1),
          ("peer", 2),
          ("passToEvc", 3),
          ("peerAndPassToEvc", 4))
    )


_MesUniL2ControlProtocolProcessing_Type.__name__ = "Integer32"
_MesUniL2ControlProtocolProcessing_Object = MibTableColumn
mesUniL2ControlProtocolProcessing = _MesUniL2ControlProtocolProcessing_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 2, 1, 1, 26),
    _MesUniL2ControlProtocolProcessing_Type()
)
mesUniL2ControlProtocolProcessing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mesUniL2ControlProtocolProcessing.setStatus("deprecated")
_MesUniSetupCommand_Type = CommandString
_MesUniSetupCommand_Object = MibTableColumn
mesUniSetupCommand = _MesUniSetupCommand_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 2, 1, 1, 27),
    _MesUniSetupCommand_Type()
)
mesUniSetupCommand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesUniSetupCommand.setStatus("current")
_MesUniCreateEvcCommand_Type = CommandString
_MesUniCreateEvcCommand_Object = MibTableColumn
mesUniCreateEvcCommand = _MesUniCreateEvcCommand_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 2, 1, 1, 28),
    _MesUniCreateEvcCommand_Type()
)
mesUniCreateEvcCommand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesUniCreateEvcCommand.setStatus("current")
_MesUniListCeVlanIdsCommand_Type = CommandString
_MesUniListCeVlanIdsCommand_Object = MibTableColumn
mesUniListCeVlanIdsCommand = _MesUniListCeVlanIdsCommand_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 2, 1, 1, 29),
    _MesUniListCeVlanIdsCommand_Type()
)
mesUniListCeVlanIdsCommand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesUniListCeVlanIdsCommand.setStatus("current")


class _MesUniTaggingOfUntaggedFrames_Type(Integer32):
    """Custom type mesUniTaggingOfUntaggedFrames based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_MesUniTaggingOfUntaggedFrames_Type.__name__ = "Integer32"
_MesUniTaggingOfUntaggedFrames_Object = MibTableColumn
mesUniTaggingOfUntaggedFrames = _MesUniTaggingOfUntaggedFrames_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 2, 1, 1, 30),
    _MesUniTaggingOfUntaggedFrames_Type()
)
mesUniTaggingOfUntaggedFrames.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesUniTaggingOfUntaggedFrames.setStatus("current")
_MesUniCeVlanIdAssignmentCommand_Type = CommandString
_MesUniCeVlanIdAssignmentCommand_Object = MibTableColumn
mesUniCeVlanIdAssignmentCommand = _MesUniCeVlanIdAssignmentCommand_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 2, 1, 1, 31),
    _MesUniCeVlanIdAssignmentCommand_Type()
)
mesUniCeVlanIdAssignmentCommand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesUniCeVlanIdAssignmentCommand.setStatus("current")


class _MesUniL2SpanningTreeProcessing_Type(Integer32):
    """Custom type mesUniL2SpanningTreeProcessing based on Integer32"""
    defaultValue = 1

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
        *(("discard", 1),
          ("peer", 2),
          ("passToEvc", 3),
          ("peerAndPassToEvc", 4))
    )


_MesUniL2SpanningTreeProcessing_Type.__name__ = "Integer32"
_MesUniL2SpanningTreeProcessing_Object = MibTableColumn
mesUniL2SpanningTreeProcessing = _MesUniL2SpanningTreeProcessing_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 2, 1, 1, 32),
    _MesUniL2SpanningTreeProcessing_Type()
)
mesUniL2SpanningTreeProcessing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mesUniL2SpanningTreeProcessing.setStatus("current")


class _MesUniL2PauseProcessing_Type(Integer32):
    """Custom type mesUniL2PauseProcessing based on Integer32"""
    defaultValue = 1

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
        *(("discard", 1),
          ("peer", 2),
          ("passToEvc", 3),
          ("peerAndPassToEvc", 4))
    )


_MesUniL2PauseProcessing_Type.__name__ = "Integer32"
_MesUniL2PauseProcessing_Object = MibTableColumn
mesUniL2PauseProcessing = _MesUniL2PauseProcessing_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 2, 1, 1, 33),
    _MesUniL2PauseProcessing_Type()
)
mesUniL2PauseProcessing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mesUniL2PauseProcessing.setStatus("current")


class _MesUniL2SlowProtocolsProcessing_Type(Integer32):
    """Custom type mesUniL2SlowProtocolsProcessing based on Integer32"""
    defaultValue = 1

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
        *(("discard", 1),
          ("peer", 2),
          ("passToEvc", 3),
          ("peerAndPassToEvc", 4))
    )


_MesUniL2SlowProtocolsProcessing_Type.__name__ = "Integer32"
_MesUniL2SlowProtocolsProcessing_Object = MibTableColumn
mesUniL2SlowProtocolsProcessing = _MesUniL2SlowProtocolsProcessing_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 2, 1, 1, 34),
    _MesUniL2SlowProtocolsProcessing_Type()
)
mesUniL2SlowProtocolsProcessing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mesUniL2SlowProtocolsProcessing.setStatus("current")


class _MesUniL2PortAuthenticationProcessing_Type(Integer32):
    """Custom type mesUniL2PortAuthenticationProcessing based on Integer32"""
    defaultValue = 1

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
        *(("discard", 1),
          ("peer", 2),
          ("passToEvc", 3),
          ("peerAndPassToEvc", 4))
    )


_MesUniL2PortAuthenticationProcessing_Type.__name__ = "Integer32"
_MesUniL2PortAuthenticationProcessing_Object = MibTableColumn
mesUniL2PortAuthenticationProcessing = _MesUniL2PortAuthenticationProcessing_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 2, 1, 1, 35),
    _MesUniL2PortAuthenticationProcessing_Type()
)
mesUniL2PortAuthenticationProcessing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mesUniL2PortAuthenticationProcessing.setStatus("current")


class _MesUniL2OtherBridgeBlockProcessing_Type(Integer32):
    """Custom type mesUniL2OtherBridgeBlockProcessing based on Integer32"""
    defaultValue = 1

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
        *(("discard", 1),
          ("peer", 2),
          ("passToEvc", 3),
          ("peerAndPassToEvc", 4))
    )


_MesUniL2OtherBridgeBlockProcessing_Type.__name__ = "Integer32"
_MesUniL2OtherBridgeBlockProcessing_Object = MibTableColumn
mesUniL2OtherBridgeBlockProcessing = _MesUniL2OtherBridgeBlockProcessing_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 2, 1, 1, 36),
    _MesUniL2OtherBridgeBlockProcessing_Type()
)
mesUniL2OtherBridgeBlockProcessing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mesUniL2OtherBridgeBlockProcessing.setStatus("current")


class _MesUniL2AllLANsBridgeMgmtProcessing_Type(Integer32):
    """Custom type mesUniL2AllLANsBridgeMgmtProcessing based on Integer32"""
    defaultValue = 1

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
        *(("discard", 1),
          ("peer", 2),
          ("passToEvc", 3),
          ("peerAndPassToEvc", 4))
    )


_MesUniL2AllLANsBridgeMgmtProcessing_Type.__name__ = "Integer32"
_MesUniL2AllLANsBridgeMgmtProcessing_Object = MibTableColumn
mesUniL2AllLANsBridgeMgmtProcessing = _MesUniL2AllLANsBridgeMgmtProcessing_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 2, 1, 1, 37),
    _MesUniL2AllLANsBridgeMgmtProcessing_Type()
)
mesUniL2AllLANsBridgeMgmtProcessing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mesUniL2AllLANsBridgeMgmtProcessing.setStatus("current")


class _MesUniL2GarpProcessing_Type(Integer32):
    """Custom type mesUniL2GarpProcessing based on Integer32"""
    defaultValue = 1

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
        *(("discard", 1),
          ("peer", 2),
          ("passToEvc", 3),
          ("peerAndPassToEvc", 4))
    )


_MesUniL2GarpProcessing_Type.__name__ = "Integer32"
_MesUniL2GarpProcessing_Object = MibTableColumn
mesUniL2GarpProcessing = _MesUniL2GarpProcessing_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 2, 1, 1, 38),
    _MesUniL2GarpProcessing_Type()
)
mesUniL2GarpProcessing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mesUniL2GarpProcessing.setStatus("current")


class _MesUniL2OamUniMeProcessing_Type(Integer32):
    """Custom type mesUniL2OamUniMeProcessing based on Integer32"""
    defaultValue = 1

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
        *(("discard", 1),
          ("peer", 2),
          ("passToEvc", 3),
          ("peerAndPassToEvc", 4))
    )


_MesUniL2OamUniMeProcessing_Type.__name__ = "Integer32"
_MesUniL2OamUniMeProcessing_Object = MibTableColumn
mesUniL2OamUniMeProcessing = _MesUniL2OamUniMeProcessing_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 2, 1, 1, 39),
    _MesUniL2OamUniMeProcessing_Type()
)
mesUniL2OamUniMeProcessing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mesUniL2OamUniMeProcessing.setStatus("current")


class _MesUniTagTransparency_Type(Integer32):
    """Custom type mesUniTagTransparency based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_MesUniTagTransparency_Type.__name__ = "Integer32"
_MesUniTagTransparency_Object = MibTableColumn
mesUniTagTransparency = _MesUniTagTransparency_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 2, 1, 1, 40),
    _MesUniTagTransparency_Type()
)
mesUniTagTransparency.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesUniTagTransparency.setStatus("current")


class _MesUniMgmtVlan_Type(Integer32):
    """Custom type mesUniMgmtVlan based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_MesUniMgmtVlan_Type.__name__ = "Integer32"
_MesUniMgmtVlan_Object = MibTableColumn
mesUniMgmtVlan = _MesUniMgmtVlan_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 2, 1, 1, 41),
    _MesUniMgmtVlan_Type()
)
mesUniMgmtVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mesUniMgmtVlan.setStatus("current")
_MesUniDefineMgmtVlan_Type = CommandString
_MesUniDefineMgmtVlan_Object = MibTableColumn
mesUniDefineMgmtVlan = _MesUniDefineMgmtVlan_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 2, 1, 1, 42),
    _MesUniDefineMgmtVlan_Type()
)
mesUniDefineMgmtVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesUniDefineMgmtVlan.setStatus("current")


class _MesUniMgmtVlanTagType_Type(Integer32):
    """Custom type mesUniMgmtVlanTagType based on Integer32"""
    defaultValue = 0

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
        *(("noTag", 0),
          ("qTag0x8100", 1),
          ("sTag0x88a8", 2),
          ("tag0x9100", 3),
          ("macInMac", 4),
          ("other", 5))
    )


_MesUniMgmtVlanTagType_Type.__name__ = "Integer32"
_MesUniMgmtVlanTagType_Object = MibTableColumn
mesUniMgmtVlanTagType = _MesUniMgmtVlanTagType_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 2, 1, 1, 43),
    _MesUniMgmtVlanTagType_Type()
)
mesUniMgmtVlanTagType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesUniMgmtVlanTagType.setStatus("current")


class _MesUniMgmtVlanEtherType_Type(Unsigned32):
    """Custom type mesUniMgmtVlanEtherType based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MesUniMgmtVlanEtherType_Type.__name__ = "Unsigned32"
_MesUniMgmtVlanEtherType_Object = MibTableColumn
mesUniMgmtVlanEtherType = _MesUniMgmtVlanEtherType_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 2, 1, 1, 44),
    _MesUniMgmtVlanEtherType_Type()
)
mesUniMgmtVlanEtherType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesUniMgmtVlanEtherType.setStatus("current")


class _MesUniMgmtVlanVlanId_Type(Unsigned32):
    """Custom type mesUniMgmtVlanVlanId based on Unsigned32"""
    defaultValue = 4094

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_MesUniMgmtVlanVlanId_Type.__name__ = "Unsigned32"
_MesUniMgmtVlanVlanId_Object = MibTableColumn
mesUniMgmtVlanVlanId = _MesUniMgmtVlanVlanId_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 2, 1, 1, 45),
    _MesUniMgmtVlanVlanId_Type()
)
mesUniMgmtVlanVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesUniMgmtVlanVlanId.setStatus("current")


class _MesUniMgmtVlanPriority_Type(Unsigned32):
    """Custom type mesUniMgmtVlanPriority based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_MesUniMgmtVlanPriority_Type.__name__ = "Unsigned32"
_MesUniMgmtVlanPriority_Object = MibTableColumn
mesUniMgmtVlanPriority = _MesUniMgmtVlanPriority_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 2, 1, 1, 46),
    _MesUniMgmtVlanPriority_Type()
)
mesUniMgmtVlanPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesUniMgmtVlanPriority.setStatus("current")
_MesUniMgmtVlanMacAddress_Type = MacAddress
_MesUniMgmtVlanMacAddress_Object = MibTableColumn
mesUniMgmtVlanMacAddress = _MesUniMgmtVlanMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 2, 1, 1, 47),
    _MesUniMgmtVlanMacAddress_Type()
)
mesUniMgmtVlanMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesUniMgmtVlanMacAddress.setStatus("current")


class _MesUniMacInMac_Type(Integer32):
    """Custom type mesUniMacInMac based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_MesUniMacInMac_Type.__name__ = "Integer32"
_MesUniMacInMac_Object = MibTableColumn
mesUniMacInMac = _MesUniMacInMac_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 2, 1, 1, 48),
    _MesUniMacInMac_Type()
)
mesUniMacInMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesUniMacInMac.setStatus("current")


class _MesUniMacInMacIsid_Type(Unsigned32):
    """Custom type mesUniMacInMacIsid based on Unsigned32"""
    defaultValue = 256

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(256, 16777214),
    )


_MesUniMacInMacIsid_Type.__name__ = "Unsigned32"
_MesUniMacInMacIsid_Object = MibTableColumn
mesUniMacInMacIsid = _MesUniMacInMacIsid_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 2, 1, 1, 49),
    _MesUniMacInMacIsid_Type()
)
mesUniMacInMacIsid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesUniMacInMacIsid.setStatus("current")


class _MesUniMacInMacDa_Type(DisplayString):
    """Custom type mesUniMacInMacDa based on DisplayString"""
    defaultValue = OctetString("")


_MesUniMacInMacDa_Type.__name__ = "DisplayString"
_MesUniMacInMacDa_Object = MibTableColumn
mesUniMacInMacDa = _MesUniMacInMacDa_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 2, 1, 1, 50),
    _MesUniMacInMacDa_Type()
)
mesUniMacInMacDa.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesUniMacInMacDa.setStatus("current")
_MesUniDefineMac_Type = CommandString
_MesUniDefineMac_Object = MibTableColumn
mesUniDefineMac = _MesUniDefineMac_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 2, 1, 1, 51),
    _MesUniDefineMac_Type()
)
mesUniDefineMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesUniDefineMac.setStatus("current")


class _MesUniLagStatus_Type(Integer32):
    """Custom type mesUniLagStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noLag", 1),
          ("master", 2),
          ("slave", 3))
    )


_MesUniLagStatus_Type.__name__ = "Integer32"
_MesUniLagStatus_Object = MibTableColumn
mesUniLagStatus = _MesUniLagStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 2, 1, 1, 52),
    _MesUniLagStatus_Type()
)
mesUniLagStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesUniLagStatus.setStatus("current")


class _MesUniLagPortmask_Type(Unsigned32):
    """Custom type mesUniLagPortmask based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MesUniLagPortmask_Type.__name__ = "Unsigned32"
_MesUniLagPortmask_Object = MibTableColumn
mesUniLagPortmask = _MesUniLagPortmask_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 2, 1, 1, 53),
    _MesUniLagPortmask_Type()
)
mesUniLagPortmask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesUniLagPortmask.setStatus("current")
_MesUniAssociateLag_Type = CommandString
_MesUniAssociateLag_Object = MibTableColumn
mesUniAssociateLag = _MesUniAssociateLag_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 2, 1, 1, 54),
    _MesUniAssociateLag_Type()
)
mesUniAssociateLag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesUniAssociateLag.setStatus("current")
_MesNniList_ObjectIdentity = ObjectIdentity
mesNniList = _MesNniList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 3)
)
_MesNniTable_Object = MibTable
mesNniTable = _MesNniTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 3, 1)
)
if mibBuilder.loadTexts:
    mesNniTable.setStatus("obsolete")
_MesNniEntry_Object = MibTableRow
mesNniEntry = _MesNniEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 3, 1, 1)
)
mesNniEntry.setIndexNames(
    (0, "LUM-MES-MIB", "mesNniIndex"),
)
if mibBuilder.loadTexts:
    mesNniEntry.setStatus("current")


class _MesNniIndex_Type(Unsigned32):
    """Custom type mesNniIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_MesNniIndex_Type.__name__ = "Unsigned32"
_MesNniIndex_Object = MibTableColumn
mesNniIndex = _MesNniIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 3, 1, 1, 1),
    _MesNniIndex_Type()
)
mesNniIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesNniIndex.setStatus("current")
_MesNniName_Type = MgmtNameString
_MesNniName_Object = MibTableColumn
mesNniName = _MesNniName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 3, 1, 1, 2),
    _MesNniName_Type()
)
mesNniName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesNniName.setStatus("current")


class _MesNniDescr_Type(DisplayString):
    """Custom type mesNniDescr based on DisplayString"""
    defaultValue = OctetString("")


_MesNniDescr_Type.__name__ = "DisplayString"
_MesNniDescr_Object = MibTableColumn
mesNniDescr = _MesNniDescr_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 3, 1, 1, 3),
    _MesNniDescr_Type()
)
mesNniDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mesNniDescr.setStatus("current")
_MesNniSubrack_Type = SubrackNumber
_MesNniSubrack_Object = MibTableColumn
mesNniSubrack = _MesNniSubrack_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 3, 1, 1, 4),
    _MesNniSubrack_Type()
)
mesNniSubrack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesNniSubrack.setStatus("current")
_MesNniSlot_Type = SlotNumber
_MesNniSlot_Object = MibTableColumn
mesNniSlot = _MesNniSlot_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 3, 1, 1, 5),
    _MesNniSlot_Type()
)
mesNniSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesNniSlot.setStatus("current")
_MesNniTxPort_Type = PortNumber
_MesNniTxPort_Object = MibTableColumn
mesNniTxPort = _MesNniTxPort_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 3, 1, 1, 6),
    _MesNniTxPort_Type()
)
mesNniTxPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesNniTxPort.setStatus("current")
_MesNniRxPort_Type = PortNumber
_MesNniRxPort_Object = MibTableColumn
mesNniRxPort = _MesNniRxPort_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 3, 1, 1, 7),
    _MesNniRxPort_Type()
)
mesNniRxPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesNniRxPort.setStatus("current")
_MesNniObjectProperty_Type = ObjectProperty
_MesNniObjectProperty_Object = MibTableColumn
mesNniObjectProperty = _MesNniObjectProperty_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 3, 1, 1, 8),
    _MesNniObjectProperty_Type()
)
mesNniObjectProperty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesNniObjectProperty.setStatus("current")


class _MesNniAdminStatus_Type(BoardOrInterfaceAdminStatus):
    """Custom type mesNniAdminStatus based on BoardOrInterfaceAdminStatus"""
    defaultValue = 3


_MesNniAdminStatus_Type.__name__ = "BoardOrInterfaceAdminStatus"
_MesNniAdminStatus_Object = MibTableColumn
mesNniAdminStatus = _MesNniAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 3, 1, 1, 9),
    _MesNniAdminStatus_Type()
)
mesNniAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mesNniAdminStatus.setStatus("current")


class _MesNniOperStatus_Type(BoardOrInterfaceOperStatus):
    """Custom type mesNniOperStatus based on BoardOrInterfaceOperStatus"""
    defaultValue = 1


_MesNniOperStatus_Type.__name__ = "BoardOrInterfaceOperStatus"
_MesNniOperStatus_Object = MibTableColumn
mesNniOperStatus = _MesNniOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 3, 1, 1, 10),
    _MesNniOperStatus_Type()
)
mesNniOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesNniOperStatus.setStatus("current")


class _MesNniIdentifier_Type(DisplayString):
    """Custom type mesNniIdentifier based on DisplayString"""
    defaultValue = OctetString("")


_MesNniIdentifier_Type.__name__ = "DisplayString"
_MesNniIdentifier_Object = MibTableColumn
mesNniIdentifier = _MesNniIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 3, 1, 1, 11),
    _MesNniIdentifier_Type()
)
mesNniIdentifier.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesNniIdentifier.setStatus("current")
_MesNniCurrentNoOfEvcs_Type = Unsigned32
_MesNniCurrentNoOfEvcs_Object = MibTableColumn
mesNniCurrentNoOfEvcs = _MesNniCurrentNoOfEvcs_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 3, 1, 1, 12),
    _MesNniCurrentNoOfEvcs_Type()
)
mesNniCurrentNoOfEvcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesNniCurrentNoOfEvcs.setStatus("current")


class _MesNniAvailableCapacity_Type(Unsigned32):
    """Custom type mesNniAvailableCapacity based on Unsigned32"""
    defaultValue = 1


_MesNniAvailableCapacity_Type.__name__ = "Unsigned32"
_MesNniAvailableCapacity_Object = MibTableColumn
mesNniAvailableCapacity = _MesNniAvailableCapacity_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 3, 1, 1, 13),
    _MesNniAvailableCapacity_Type()
)
mesNniAvailableCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesNniAvailableCapacity.setStatus("current")
_MesNniDefineMgmtVlan_Type = CommandString
_MesNniDefineMgmtVlan_Object = MibTableColumn
mesNniDefineMgmtVlan = _MesNniDefineMgmtVlan_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 3, 1, 1, 14),
    _MesNniDefineMgmtVlan_Type()
)
mesNniDefineMgmtVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesNniDefineMgmtVlan.setStatus("current")


class _MesNniMgmtVlanTagType_Type(Integer32):
    """Custom type mesNniMgmtVlanTagType based on Integer32"""
    defaultValue = 0

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
        *(("noTag", 0),
          ("qTag0x8100", 1),
          ("sTag0x88a8", 2),
          ("tag0x9100", 3),
          ("macInMac", 4),
          ("other", 5))
    )


_MesNniMgmtVlanTagType_Type.__name__ = "Integer32"
_MesNniMgmtVlanTagType_Object = MibTableColumn
mesNniMgmtVlanTagType = _MesNniMgmtVlanTagType_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 3, 1, 1, 15),
    _MesNniMgmtVlanTagType_Type()
)
mesNniMgmtVlanTagType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesNniMgmtVlanTagType.setStatus("current")


class _MesNniMgmtVlanEtherType_Type(Unsigned32):
    """Custom type mesNniMgmtVlanEtherType based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MesNniMgmtVlanEtherType_Type.__name__ = "Unsigned32"
_MesNniMgmtVlanEtherType_Object = MibTableColumn
mesNniMgmtVlanEtherType = _MesNniMgmtVlanEtherType_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 3, 1, 1, 16),
    _MesNniMgmtVlanEtherType_Type()
)
mesNniMgmtVlanEtherType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesNniMgmtVlanEtherType.setStatus("current")


class _MesNniMgmtVlanVlanId_Type(Unsigned32):
    """Custom type mesNniMgmtVlanVlanId based on Unsigned32"""
    defaultValue = 4094

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_MesNniMgmtVlanVlanId_Type.__name__ = "Unsigned32"
_MesNniMgmtVlanVlanId_Object = MibTableColumn
mesNniMgmtVlanVlanId = _MesNniMgmtVlanVlanId_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 3, 1, 1, 17),
    _MesNniMgmtVlanVlanId_Type()
)
mesNniMgmtVlanVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesNniMgmtVlanVlanId.setStatus("current")


class _MesNniMgmtVlanPriority_Type(Unsigned32):
    """Custom type mesNniMgmtVlanPriority based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_MesNniMgmtVlanPriority_Type.__name__ = "Unsigned32"
_MesNniMgmtVlanPriority_Object = MibTableColumn
mesNniMgmtVlanPriority = _MesNniMgmtVlanPriority_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 3, 1, 1, 18),
    _MesNniMgmtVlanPriority_Type()
)
mesNniMgmtVlanPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesNniMgmtVlanPriority.setStatus("current")
_MesNniMgmtVlanIpAddress_Type = IpAddress
_MesNniMgmtVlanIpAddress_Object = MibTableColumn
mesNniMgmtVlanIpAddress = _MesNniMgmtVlanIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 3, 1, 1, 19),
    _MesNniMgmtVlanIpAddress_Type()
)
mesNniMgmtVlanIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mesNniMgmtVlanIpAddress.setStatus("current")
_MesNniMgmtVlanNetMask_Type = IpAddress
_MesNniMgmtVlanNetMask_Object = MibTableColumn
mesNniMgmtVlanNetMask = _MesNniMgmtVlanNetMask_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 3, 1, 1, 20),
    _MesNniMgmtVlanNetMask_Type()
)
mesNniMgmtVlanNetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mesNniMgmtVlanNetMask.setStatus("current")
_MesNniMgmtVlanMacAddress_Type = MacAddress
_MesNniMgmtVlanMacAddress_Object = MibTableColumn
mesNniMgmtVlanMacAddress = _MesNniMgmtVlanMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 3, 1, 1, 21),
    _MesNniMgmtVlanMacAddress_Type()
)
mesNniMgmtVlanMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesNniMgmtVlanMacAddress.setStatus("current")
_MesNniSetupCommand_Type = CommandString
_MesNniSetupCommand_Object = MibTableColumn
mesNniSetupCommand = _MesNniSetupCommand_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 3, 1, 1, 22),
    _MesNniSetupCommand_Type()
)
mesNniSetupCommand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesNniSetupCommand.setStatus("current")


class _MesNniMgmtVlan_Type(Integer32):
    """Custom type mesNniMgmtVlan based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_MesNniMgmtVlan_Type.__name__ = "Integer32"
_MesNniMgmtVlan_Object = MibTableColumn
mesNniMgmtVlan = _MesNniMgmtVlan_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 3, 1, 1, 23),
    _MesNniMgmtVlan_Type()
)
mesNniMgmtVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mesNniMgmtVlan.setStatus("current")


class _MesNniMacInMac_Type(Integer32):
    """Custom type mesNniMacInMac based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_MesNniMacInMac_Type.__name__ = "Integer32"
_MesNniMacInMac_Object = MibTableColumn
mesNniMacInMac = _MesNniMacInMac_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 3, 1, 1, 24),
    _MesNniMacInMac_Type()
)
mesNniMacInMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesNniMacInMac.setStatus("current")


class _MesNniMacInMacIsid_Type(Unsigned32):
    """Custom type mesNniMacInMacIsid based on Unsigned32"""
    defaultValue = 256

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(256, 16777214),
    )


_MesNniMacInMacIsid_Type.__name__ = "Unsigned32"
_MesNniMacInMacIsid_Object = MibTableColumn
mesNniMacInMacIsid = _MesNniMacInMacIsid_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 3, 1, 1, 25),
    _MesNniMacInMacIsid_Type()
)
mesNniMacInMacIsid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesNniMacInMacIsid.setStatus("current")


class _MesNniMacInMacDa_Type(DisplayString):
    """Custom type mesNniMacInMacDa based on DisplayString"""
    defaultValue = OctetString("")


_MesNniMacInMacDa_Type.__name__ = "DisplayString"
_MesNniMacInMacDa_Object = MibTableColumn
mesNniMacInMacDa = _MesNniMacInMacDa_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 3, 1, 1, 26),
    _MesNniMacInMacDa_Type()
)
mesNniMacInMacDa.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesNniMacInMacDa.setStatus("current")
_MesNniDefineMac_Type = CommandString
_MesNniDefineMac_Object = MibTableColumn
mesNniDefineMac = _MesNniDefineMac_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 3, 1, 1, 27),
    _MesNniDefineMac_Type()
)
mesNniDefineMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesNniDefineMac.setStatus("current")


class _MesNniLagStatus_Type(Integer32):
    """Custom type mesNniLagStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_MesNniLagStatus_Type.__name__ = "Integer32"
_MesNniLagStatus_Object = MibTableColumn
mesNniLagStatus = _MesNniLagStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 3, 1, 1, 28),
    _MesNniLagStatus_Type()
)
mesNniLagStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mesNniLagStatus.setStatus("current")
_MesEvcList_ObjectIdentity = ObjectIdentity
mesEvcList = _MesEvcList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 4)
)
_MesEvcTable_Object = MibTable
mesEvcTable = _MesEvcTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 4, 1)
)
if mibBuilder.loadTexts:
    mesEvcTable.setStatus("obsolete")
_MesEvcEntry_Object = MibTableRow
mesEvcEntry = _MesEvcEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 4, 1, 1)
)
mesEvcEntry.setIndexNames(
    (0, "LUM-MES-MIB", "mesEvcIndex"),
)
if mibBuilder.loadTexts:
    mesEvcEntry.setStatus("current")


class _MesEvcIndex_Type(Unsigned32):
    """Custom type mesEvcIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_MesEvcIndex_Type.__name__ = "Unsigned32"
_MesEvcIndex_Object = MibTableColumn
mesEvcIndex = _MesEvcIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 4, 1, 1, 1),
    _MesEvcIndex_Type()
)
mesEvcIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesEvcIndex.setStatus("current")
_MesEvcName_Type = MgmtNameString
_MesEvcName_Object = MibTableColumn
mesEvcName = _MesEvcName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 4, 1, 1, 2),
    _MesEvcName_Type()
)
mesEvcName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesEvcName.setStatus("current")


class _MesEvcDescr_Type(DisplayString):
    """Custom type mesEvcDescr based on DisplayString"""
    defaultValue = OctetString("")


_MesEvcDescr_Type.__name__ = "DisplayString"
_MesEvcDescr_Object = MibTableColumn
mesEvcDescr = _MesEvcDescr_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 4, 1, 1, 3),
    _MesEvcDescr_Type()
)
mesEvcDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mesEvcDescr.setStatus("current")
_MesEvcObjectProperty_Type = ObjectProperty
_MesEvcObjectProperty_Object = MibTableColumn
mesEvcObjectProperty = _MesEvcObjectProperty_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 4, 1, 1, 4),
    _MesEvcObjectProperty_Type()
)
mesEvcObjectProperty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesEvcObjectProperty.setStatus("current")


class _MesEvcAdminStatus_Type(BoardOrInterfaceAdminStatus):
    """Custom type mesEvcAdminStatus based on BoardOrInterfaceAdminStatus"""
    defaultValue = 1


_MesEvcAdminStatus_Type.__name__ = "BoardOrInterfaceAdminStatus"
_MesEvcAdminStatus_Object = MibTableColumn
mesEvcAdminStatus = _MesEvcAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 4, 1, 1, 5),
    _MesEvcAdminStatus_Type()
)
mesEvcAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mesEvcAdminStatus.setStatus("current")


class _MesEvcOperStatus_Type(BoardOrInterfaceOperStatus):
    """Custom type mesEvcOperStatus based on BoardOrInterfaceOperStatus"""
    defaultValue = 1


_MesEvcOperStatus_Type.__name__ = "BoardOrInterfaceOperStatus"
_MesEvcOperStatus_Object = MibTableColumn
mesEvcOperStatus = _MesEvcOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 4, 1, 1, 6),
    _MesEvcOperStatus_Type()
)
mesEvcOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesEvcOperStatus.setStatus("current")


class _MesEvcIdentifier_Type(DisplayString):
    """Custom type mesEvcIdentifier based on DisplayString"""
    defaultValue = OctetString("")


_MesEvcIdentifier_Type.__name__ = "DisplayString"
_MesEvcIdentifier_Object = MibTableColumn
mesEvcIdentifier = _MesEvcIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 4, 1, 1, 7),
    _MesEvcIdentifier_Type()
)
mesEvcIdentifier.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesEvcIdentifier.setStatus("current")
_MesEvcUniIdentifier_Type = DisplayString
_MesEvcUniIdentifier_Object = MibTableColumn
mesEvcUniIdentifier = _MesEvcUniIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 4, 1, 1, 8),
    _MesEvcUniIdentifier_Type()
)
mesEvcUniIdentifier.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesEvcUniIdentifier.setStatus("current")
_MesEvcNniIdentifier_Type = DisplayString
_MesEvcNniIdentifier_Object = MibTableColumn
mesEvcNniIdentifier = _MesEvcNniIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 4, 1, 1, 9),
    _MesEvcNniIdentifier_Type()
)
mesEvcNniIdentifier.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesEvcNniIdentifier.setStatus("current")


class _MesEvcType_Type(Integer32):
    """Custom type mesEvcType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("pointToPoint", 1),
          ("multiPointToMultiPoint", 2))
    )


_MesEvcType_Type.__name__ = "Integer32"
_MesEvcType_Object = MibTableColumn
mesEvcType = _MesEvcType_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 4, 1, 1, 10),
    _MesEvcType_Type()
)
mesEvcType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesEvcType.setStatus("current")


class _MesEvcMtuSize_Type(Unsigned32):
    """Custom type mesEvcMtuSize based on Unsigned32"""
    defaultValue = 1518

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1518, 9600),
    )


_MesEvcMtuSize_Type.__name__ = "Unsigned32"
_MesEvcMtuSize_Object = MibTableColumn
mesEvcMtuSize = _MesEvcMtuSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 4, 1, 1, 11),
    _MesEvcMtuSize_Type()
)
mesEvcMtuSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mesEvcMtuSize.setStatus("current")


class _MesEvcFrameDeliveryUnicast_Type(Integer32):
    """Custom type mesEvcFrameDeliveryUnicast based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("discard", 1),
          ("deliverUnconditionally", 2),
          ("deliverConditionally", 3))
    )


_MesEvcFrameDeliveryUnicast_Type.__name__ = "Integer32"
_MesEvcFrameDeliveryUnicast_Object = MibTableColumn
mesEvcFrameDeliveryUnicast = _MesEvcFrameDeliveryUnicast_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 4, 1, 1, 12),
    _MesEvcFrameDeliveryUnicast_Type()
)
mesEvcFrameDeliveryUnicast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mesEvcFrameDeliveryUnicast.setStatus("current")


class _MesEvcFrameDeliveryMulticast_Type(Integer32):
    """Custom type mesEvcFrameDeliveryMulticast based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("discard", 1),
          ("deliverUnconditionally", 2),
          ("deliverConditionally", 3))
    )


_MesEvcFrameDeliveryMulticast_Type.__name__ = "Integer32"
_MesEvcFrameDeliveryMulticast_Object = MibTableColumn
mesEvcFrameDeliveryMulticast = _MesEvcFrameDeliveryMulticast_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 4, 1, 1, 13),
    _MesEvcFrameDeliveryMulticast_Type()
)
mesEvcFrameDeliveryMulticast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mesEvcFrameDeliveryMulticast.setStatus("current")


class _MesEvcFrameDeliveryBroadcast_Type(Integer32):
    """Custom type mesEvcFrameDeliveryBroadcast based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("discard", 1),
          ("deliverUnconditionally", 2),
          ("deliverConditionally", 3))
    )


_MesEvcFrameDeliveryBroadcast_Type.__name__ = "Integer32"
_MesEvcFrameDeliveryBroadcast_Object = MibTableColumn
mesEvcFrameDeliveryBroadcast = _MesEvcFrameDeliveryBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 4, 1, 1, 14),
    _MesEvcFrameDeliveryBroadcast_Type()
)
mesEvcFrameDeliveryBroadcast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mesEvcFrameDeliveryBroadcast.setStatus("current")
_MesEvcDefineL2Control_Type = CommandString
_MesEvcDefineL2Control_Object = MibTableColumn
mesEvcDefineL2Control = _MesEvcDefineL2Control_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 4, 1, 1, 15),
    _MesEvcDefineL2Control_Type()
)
mesEvcDefineL2Control.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesEvcDefineL2Control.setStatus("current")


class _MesEvcL2ControlProtocolDisposition_Type(Integer32):
    """Custom type mesEvcL2ControlProtocolDisposition based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("discard", 1),
          ("tunnel", 2),
          ("wrapMac", 3))
    )


_MesEvcL2ControlProtocolDisposition_Type.__name__ = "Integer32"
_MesEvcL2ControlProtocolDisposition_Object = MibTableColumn
mesEvcL2ControlProtocolDisposition = _MesEvcL2ControlProtocolDisposition_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 4, 1, 1, 16),
    _MesEvcL2ControlProtocolDisposition_Type()
)
mesEvcL2ControlProtocolDisposition.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesEvcL2ControlProtocolDisposition.setStatus("current")
_MesEvcL2DestinationMacAddress_Type = MacAddress
_MesEvcL2DestinationMacAddress_Object = MibTableColumn
mesEvcL2DestinationMacAddress = _MesEvcL2DestinationMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 4, 1, 1, 17),
    _MesEvcL2DestinationMacAddress_Type()
)
mesEvcL2DestinationMacAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesEvcL2DestinationMacAddress.setStatus("current")


class _MesEvcCeVlanIdPreservation_Type(Integer32):
    """Custom type mesEvcCeVlanIdPreservation based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_MesEvcCeVlanIdPreservation_Type.__name__ = "Integer32"
_MesEvcCeVlanIdPreservation_Object = MibTableColumn
mesEvcCeVlanIdPreservation = _MesEvcCeVlanIdPreservation_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 4, 1, 1, 18),
    _MesEvcCeVlanIdPreservation_Type()
)
mesEvcCeVlanIdPreservation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mesEvcCeVlanIdPreservation.setStatus("current")


class _MesEvcCosPreservation_Type(Integer32):
    """Custom type mesEvcCosPreservation based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_MesEvcCosPreservation_Type.__name__ = "Integer32"
_MesEvcCosPreservation_Object = MibTableColumn
mesEvcCosPreservation = _MesEvcCosPreservation_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 4, 1, 1, 19),
    _MesEvcCosPreservation_Type()
)
mesEvcCosPreservation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mesEvcCosPreservation.setStatus("current")
_MesEvcAssociateBwp_Type = CommandString
_MesEvcAssociateBwp_Object = MibTableColumn
mesEvcAssociateBwp = _MesEvcAssociateBwp_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 4, 1, 1, 20),
    _MesEvcAssociateBwp_Type()
)
mesEvcAssociateBwp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesEvcAssociateBwp.setStatus("current")
_MesEvcReleaseBwp_Type = CommandString
_MesEvcReleaseBwp_Object = MibTableColumn
mesEvcReleaseBwp = _MesEvcReleaseBwp_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 4, 1, 1, 21),
    _MesEvcReleaseBwp_Type()
)
mesEvcReleaseBwp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesEvcReleaseBwp.setStatus("current")


class _MesEvcIngressBwProfilePerEvc_Type(Integer32):
    """Custom type mesEvcIngressBwProfilePerEvc based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_MesEvcIngressBwProfilePerEvc_Type.__name__ = "Integer32"
_MesEvcIngressBwProfilePerEvc_Object = MibTableColumn
mesEvcIngressBwProfilePerEvc = _MesEvcIngressBwProfilePerEvc_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 4, 1, 1, 22),
    _MesEvcIngressBwProfilePerEvc_Type()
)
mesEvcIngressBwProfilePerEvc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesEvcIngressBwProfilePerEvc.setStatus("current")


class _MesEvcIngressBwp_Type(DisplayString):
    """Custom type mesEvcIngressBwp based on DisplayString"""
    defaultValue = OctetString("")


_MesEvcIngressBwp_Type.__name__ = "DisplayString"
_MesEvcIngressBwp_Object = MibTableColumn
mesEvcIngressBwp = _MesEvcIngressBwp_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 4, 1, 1, 23),
    _MesEvcIngressBwp_Type()
)
mesEvcIngressBwp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesEvcIngressBwp.setStatus("current")


class _MesEvcEgressBwProfilePerEvc_Type(Integer32):
    """Custom type mesEvcEgressBwProfilePerEvc based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_MesEvcEgressBwProfilePerEvc_Type.__name__ = "Integer32"
_MesEvcEgressBwProfilePerEvc_Object = MibTableColumn
mesEvcEgressBwProfilePerEvc = _MesEvcEgressBwProfilePerEvc_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 4, 1, 1, 24),
    _MesEvcEgressBwProfilePerEvc_Type()
)
mesEvcEgressBwProfilePerEvc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesEvcEgressBwProfilePerEvc.setStatus("current")


class _MesEvcEgressBwp_Type(DisplayString):
    """Custom type mesEvcEgressBwp based on DisplayString"""
    defaultValue = OctetString("")


_MesEvcEgressBwp_Type.__name__ = "DisplayString"
_MesEvcEgressBwp_Object = MibTableColumn
mesEvcEgressBwp = _MesEvcEgressBwp_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 4, 1, 1, 25),
    _MesEvcEgressBwp_Type()
)
mesEvcEgressBwp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesEvcEgressBwp.setStatus("current")
_MesEvcCreateCeVlanIdMap_Type = CommandString
_MesEvcCreateCeVlanIdMap_Object = MibTableColumn
mesEvcCreateCeVlanIdMap = _MesEvcCreateCeVlanIdMap_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 4, 1, 1, 26),
    _MesEvcCreateCeVlanIdMap_Type()
)
mesEvcCreateCeVlanIdMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesEvcCreateCeVlanIdMap.setStatus("current")
_MesEvcDefineProviderTag_Type = CommandString
_MesEvcDefineProviderTag_Object = MibTableColumn
mesEvcDefineProviderTag = _MesEvcDefineProviderTag_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 4, 1, 1, 27),
    _MesEvcDefineProviderTag_Type()
)
mesEvcDefineProviderTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesEvcDefineProviderTag.setStatus("current")


class _MesEvcProviderTagType_Type(Integer32):
    """Custom type mesEvcProviderTagType based on Integer32"""
    defaultValue = 2

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
        *(("noTag", 0),
          ("qTag0x8100", 1),
          ("sTag0x88a8", 2),
          ("tag0x9100", 3),
          ("macInMac", 4),
          ("other", 5))
    )


_MesEvcProviderTagType_Type.__name__ = "Integer32"
_MesEvcProviderTagType_Object = MibTableColumn
mesEvcProviderTagType = _MesEvcProviderTagType_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 4, 1, 1, 28),
    _MesEvcProviderTagType_Type()
)
mesEvcProviderTagType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesEvcProviderTagType.setStatus("current")


class _MesEvcProviderTagEtherType_Type(Unsigned32):
    """Custom type mesEvcProviderTagEtherType based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MesEvcProviderTagEtherType_Type.__name__ = "Unsigned32"
_MesEvcProviderTagEtherType_Object = MibTableColumn
mesEvcProviderTagEtherType = _MesEvcProviderTagEtherType_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 4, 1, 1, 29),
    _MesEvcProviderTagEtherType_Type()
)
mesEvcProviderTagEtherType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesEvcProviderTagEtherType.setStatus("current")


class _MesEvcProviderTagVlanId_Type(Unsigned32):
    """Custom type mesEvcProviderTagVlanId based on Unsigned32"""
    defaultValue = 4094

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_MesEvcProviderTagVlanId_Type.__name__ = "Unsigned32"
_MesEvcProviderTagVlanId_Object = MibTableColumn
mesEvcProviderTagVlanId = _MesEvcProviderTagVlanId_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 4, 1, 1, 30),
    _MesEvcProviderTagVlanId_Type()
)
mesEvcProviderTagVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesEvcProviderTagVlanId.setStatus("current")
_MesEvcDefineClassOfService_Type = CommandString
_MesEvcDefineClassOfService_Object = MibTableColumn
mesEvcDefineClassOfService = _MesEvcDefineClassOfService_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 4, 1, 1, 31),
    _MesEvcDefineClassOfService_Type()
)
mesEvcDefineClassOfService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesEvcDefineClassOfService.setStatus("current")


class _MesEvcCoSClassification_Type(Integer32):
    """Custom type mesEvcCoSClassification based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("manual", 1),
          ("cePriority", 2),
          ("dscp", 3))
    )


_MesEvcCoSClassification_Type.__name__ = "Integer32"
_MesEvcCoSClassification_Object = MibTableColumn
mesEvcCoSClassification = _MesEvcCoSClassification_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 4, 1, 1, 32),
    _MesEvcCoSClassification_Type()
)
mesEvcCoSClassification.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesEvcCoSClassification.setStatus("deprecated")


class _MesEvcCoSPriority_Type(Unsigned32):
    """Custom type mesEvcCoSPriority based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_MesEvcCoSPriority_Type.__name__ = "Unsigned32"
_MesEvcCoSPriority_Object = MibTableColumn
mesEvcCoSPriority = _MesEvcCoSPriority_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 4, 1, 1, 33),
    _MesEvcCoSPriority_Type()
)
mesEvcCoSPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mesEvcCoSPriority.setStatus("current")


class _MesEvcInternalReference_Type(Unsigned32):
    """Custom type mesEvcInternalReference based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MesEvcInternalReference_Type.__name__ = "Unsigned32"
_MesEvcInternalReference_Object = MibTableColumn
mesEvcInternalReference = _MesEvcInternalReference_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 4, 1, 1, 34),
    _MesEvcInternalReference_Type()
)
mesEvcInternalReference.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesEvcInternalReference.setStatus("current")
_MesEvcRowStatus_Type = RowStatus
_MesEvcRowStatus_Object = MibTableColumn
mesEvcRowStatus = _MesEvcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 4, 1, 1, 35),
    _MesEvcRowStatus_Type()
)
mesEvcRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesEvcRowStatus.setStatus("current")


class _MesEvcQProfile_Type(MesQProfileId):
    """Custom type mesEvcQProfile based on MesQProfileId"""
    defaultValue = 12


_MesEvcQProfile_Type.__name__ = "MesQProfileId"
_MesEvcQProfile_Object = MibTableColumn
mesEvcQProfile = _MesEvcQProfile_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 4, 1, 1, 36),
    _MesEvcQProfile_Type()
)
mesEvcQProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mesEvcQProfile.setStatus("current")


class _MesEvcCeVlanIdMap_Type(DisplayString):
    """Custom type mesEvcCeVlanIdMap based on DisplayString"""
    defaultValue = OctetString("")


_MesEvcCeVlanIdMap_Type.__name__ = "DisplayString"
_MesEvcCeVlanIdMap_Object = MibTableColumn
mesEvcCeVlanIdMap = _MesEvcCeVlanIdMap_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 4, 1, 1, 37),
    _MesEvcCeVlanIdMap_Type()
)
mesEvcCeVlanIdMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesEvcCeVlanIdMap.setStatus("current")


class _MesEvcDefaultCeVlanPriority_Type(Unsigned32):
    """Custom type mesEvcDefaultCeVlanPriority based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_MesEvcDefaultCeVlanPriority_Type.__name__ = "Unsigned32"
_MesEvcDefaultCeVlanPriority_Object = MibTableColumn
mesEvcDefaultCeVlanPriority = _MesEvcDefaultCeVlanPriority_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 4, 1, 1, 38),
    _MesEvcDefaultCeVlanPriority_Type()
)
mesEvcDefaultCeVlanPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mesEvcDefaultCeVlanPriority.setStatus("current")


class _MesEvcClientEgressTagVlanIdAssignment_Type(Integer32):
    """Custom type mesEvcClientEgressTagVlanIdAssignment based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("set", 1),
          ("copy", 2))
    )


_MesEvcClientEgressTagVlanIdAssignment_Type.__name__ = "Integer32"
_MesEvcClientEgressTagVlanIdAssignment_Object = MibTableColumn
mesEvcClientEgressTagVlanIdAssignment = _MesEvcClientEgressTagVlanIdAssignment_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 4, 1, 1, 39),
    _MesEvcClientEgressTagVlanIdAssignment_Type()
)
mesEvcClientEgressTagVlanIdAssignment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mesEvcClientEgressTagVlanIdAssignment.setStatus("current")


class _MesEvcClientEgressTagVlanId_Type(Unsigned32):
    """Custom type mesEvcClientEgressTagVlanId based on Unsigned32"""
    defaultValue = 4094

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_MesEvcClientEgressTagVlanId_Type.__name__ = "Unsigned32"
_MesEvcClientEgressTagVlanId_Object = MibTableColumn
mesEvcClientEgressTagVlanId = _MesEvcClientEgressTagVlanId_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 4, 1, 1, 40),
    _MesEvcClientEgressTagVlanId_Type()
)
mesEvcClientEgressTagVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mesEvcClientEgressTagVlanId.setStatus("current")


class _MesEvcTagPriorityAssignment_Type(Integer32):
    """Custom type mesEvcTagPriorityAssignment based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("set", 1),
          ("preserve", 2))
    )


_MesEvcTagPriorityAssignment_Type.__name__ = "Integer32"
_MesEvcTagPriorityAssignment_Object = MibTableColumn
mesEvcTagPriorityAssignment = _MesEvcTagPriorityAssignment_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 4, 1, 1, 41),
    _MesEvcTagPriorityAssignment_Type()
)
mesEvcTagPriorityAssignment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mesEvcTagPriorityAssignment.setStatus("current")


class _MesEvcClientEgressTagTypeAssignment_Type(Integer32):
    """Custom type mesEvcClientEgressTagTypeAssignment based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("set", 1),
          ("copy", 2))
    )


_MesEvcClientEgressTagTypeAssignment_Type.__name__ = "Integer32"
_MesEvcClientEgressTagTypeAssignment_Object = MibTableColumn
mesEvcClientEgressTagTypeAssignment = _MesEvcClientEgressTagTypeAssignment_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 4, 1, 1, 42),
    _MesEvcClientEgressTagTypeAssignment_Type()
)
mesEvcClientEgressTagTypeAssignment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mesEvcClientEgressTagTypeAssignment.setStatus("current")


class _MesEvcClientEgressTagType_Type(Integer32):
    """Custom type mesEvcClientEgressTagType based on Integer32"""
    defaultValue = 2

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
        *(("noTag", 0),
          ("qTag0x8100", 1),
          ("sTag0x88a8", 2),
          ("tag0x9100", 3),
          ("macInMac", 4),
          ("other", 5))
    )


_MesEvcClientEgressTagType_Type.__name__ = "Integer32"
_MesEvcClientEgressTagType_Object = MibTableColumn
mesEvcClientEgressTagType = _MesEvcClientEgressTagType_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 4, 1, 1, 43),
    _MesEvcClientEgressTagType_Type()
)
mesEvcClientEgressTagType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mesEvcClientEgressTagType.setStatus("current")


class _MesEvcClientEgressTagEtherType_Type(Unsigned32):
    """Custom type mesEvcClientEgressTagEtherType based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MesEvcClientEgressTagEtherType_Type.__name__ = "Unsigned32"
_MesEvcClientEgressTagEtherType_Object = MibTableColumn
mesEvcClientEgressTagEtherType = _MesEvcClientEgressTagEtherType_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 4, 1, 1, 44),
    _MesEvcClientEgressTagEtherType_Type()
)
mesEvcClientEgressTagEtherType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mesEvcClientEgressTagEtherType.setStatus("current")


class _MesEvcMacInMac_Type(Integer32):
    """Custom type mesEvcMacInMac based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_MesEvcMacInMac_Type.__name__ = "Integer32"
_MesEvcMacInMac_Object = MibTableColumn
mesEvcMacInMac = _MesEvcMacInMac_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 4, 1, 1, 45),
    _MesEvcMacInMac_Type()
)
mesEvcMacInMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesEvcMacInMac.setStatus("current")


class _MesEvcMacInMacLtoC_Type(Integer32):
    """Custom type mesEvcMacInMacLtoC based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_MesEvcMacInMacLtoC_Type.__name__ = "Integer32"
_MesEvcMacInMacLtoC_Object = MibTableColumn
mesEvcMacInMacLtoC = _MesEvcMacInMacLtoC_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 4, 1, 1, 46),
    _MesEvcMacInMacLtoC_Type()
)
mesEvcMacInMacLtoC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesEvcMacInMacLtoC.setStatus("current")


class _MesEvcCopyIsid_Type(Integer32):
    """Custom type mesEvcCopyIsid based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_MesEvcCopyIsid_Type.__name__ = "Integer32"
_MesEvcCopyIsid_Object = MibTableColumn
mesEvcCopyIsid = _MesEvcCopyIsid_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 4, 1, 1, 47),
    _MesEvcCopyIsid_Type()
)
mesEvcCopyIsid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesEvcCopyIsid.setStatus("current")


class _MesEvcMacInMacIsid_Type(Unsigned32):
    """Custom type mesEvcMacInMacIsid based on Unsigned32"""
    defaultValue = 256

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(256, 16777214),
    )


_MesEvcMacInMacIsid_Type.__name__ = "Unsigned32"
_MesEvcMacInMacIsid_Object = MibTableColumn
mesEvcMacInMacIsid = _MesEvcMacInMacIsid_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 4, 1, 1, 48),
    _MesEvcMacInMacIsid_Type()
)
mesEvcMacInMacIsid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesEvcMacInMacIsid.setStatus("current")


class _MesEvcMacInMacIsidLtoC_Type(Unsigned32):
    """Custom type mesEvcMacInMacIsidLtoC based on Unsigned32"""
    defaultValue = 256

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(256, 16777214),
    )


_MesEvcMacInMacIsidLtoC_Type.__name__ = "Unsigned32"
_MesEvcMacInMacIsidLtoC_Object = MibTableColumn
mesEvcMacInMacIsidLtoC = _MesEvcMacInMacIsidLtoC_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 4, 1, 1, 49),
    _MesEvcMacInMacIsidLtoC_Type()
)
mesEvcMacInMacIsidLtoC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesEvcMacInMacIsidLtoC.setStatus("current")


class _MesEvcMacInMacDa_Type(DisplayString):
    """Custom type mesEvcMacInMacDa based on DisplayString"""
    defaultValue = OctetString("")


_MesEvcMacInMacDa_Type.__name__ = "DisplayString"
_MesEvcMacInMacDa_Object = MibTableColumn
mesEvcMacInMacDa = _MesEvcMacInMacDa_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 4, 1, 1, 50),
    _MesEvcMacInMacDa_Type()
)
mesEvcMacInMacDa.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesEvcMacInMacDa.setStatus("current")


class _MesEvcMacInMacDaLtoC_Type(DisplayString):
    """Custom type mesEvcMacInMacDaLtoC based on DisplayString"""
    defaultValue = OctetString("")


_MesEvcMacInMacDaLtoC_Type.__name__ = "DisplayString"
_MesEvcMacInMacDaLtoC_Object = MibTableColumn
mesEvcMacInMacDaLtoC = _MesEvcMacInMacDaLtoC_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 4, 1, 1, 51),
    _MesEvcMacInMacDaLtoC_Type()
)
mesEvcMacInMacDaLtoC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesEvcMacInMacDaLtoC.setStatus("current")
_MesEvcDefineMac_Type = CommandString
_MesEvcDefineMac_Object = MibTableColumn
mesEvcDefineMac = _MesEvcDefineMac_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 4, 1, 1, 52),
    _MesEvcDefineMac_Type()
)
mesEvcDefineMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesEvcDefineMac.setStatus("current")


class _MesEvcIngressBwProfileModel_Type(Integer32):
    """Custom type mesEvcIngressBwProfileModel based on Integer32"""
    defaultValue = 1

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
          ("bwpPerUni", 2),
          ("bwpPerEvc", 3),
          ("bwpPerCos", 4))
    )


_MesEvcIngressBwProfileModel_Type.__name__ = "Integer32"
_MesEvcIngressBwProfileModel_Object = MibTableColumn
mesEvcIngressBwProfileModel = _MesEvcIngressBwProfileModel_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 4, 1, 1, 53),
    _MesEvcIngressBwProfileModel_Type()
)
mesEvcIngressBwProfileModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesEvcIngressBwProfileModel.setStatus("current")


class _MesEvcIngressBwProfileMap_Type(DisplayString):
    """Custom type mesEvcIngressBwProfileMap based on DisplayString"""
    defaultValue = OctetString("")


_MesEvcIngressBwProfileMap_Type.__name__ = "DisplayString"
_MesEvcIngressBwProfileMap_Object = MibTableColumn
mesEvcIngressBwProfileMap = _MesEvcIngressBwProfileMap_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 4, 1, 1, 54),
    _MesEvcIngressBwProfileMap_Type()
)
mesEvcIngressBwProfileMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesEvcIngressBwProfileMap.setStatus("current")
_MesCeEvcMapList_ObjectIdentity = ObjectIdentity
mesCeEvcMapList = _MesCeEvcMapList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 5)
)
_MesCeEvcMapTable_Object = MibTable
mesCeEvcMapTable = _MesCeEvcMapTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 5, 1)
)
if mibBuilder.loadTexts:
    mesCeEvcMapTable.setStatus("obsolete")
_MesCeEvcMapEntry_Object = MibTableRow
mesCeEvcMapEntry = _MesCeEvcMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 5, 1, 1)
)
mesCeEvcMapEntry.setIndexNames(
    (0, "LUM-MES-MIB", "mesCeEvcMapIndex"),
)
if mibBuilder.loadTexts:
    mesCeEvcMapEntry.setStatus("current")


class _MesCeEvcMapIndex_Type(Unsigned32):
    """Custom type mesCeEvcMapIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_MesCeEvcMapIndex_Type.__name__ = "Unsigned32"
_MesCeEvcMapIndex_Object = MibTableColumn
mesCeEvcMapIndex = _MesCeEvcMapIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 5, 1, 1, 1),
    _MesCeEvcMapIndex_Type()
)
mesCeEvcMapIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesCeEvcMapIndex.setStatus("current")
_MesCeEvcMapName_Type = MgmtNameString
_MesCeEvcMapName_Object = MibTableColumn
mesCeEvcMapName = _MesCeEvcMapName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 5, 1, 1, 2),
    _MesCeEvcMapName_Type()
)
mesCeEvcMapName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesCeEvcMapName.setStatus("current")
_MesCeEvcMapObjectProperty_Type = ObjectProperty
_MesCeEvcMapObjectProperty_Object = MibTableColumn
mesCeEvcMapObjectProperty = _MesCeEvcMapObjectProperty_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 5, 1, 1, 3),
    _MesCeEvcMapObjectProperty_Type()
)
mesCeEvcMapObjectProperty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesCeEvcMapObjectProperty.setStatus("current")


class _MesCeEvcMapType_Type(Integer32):
    """Custom type mesCeEvcMapType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("single", 1),
          ("range", 2))
    )


_MesCeEvcMapType_Type.__name__ = "Integer32"
_MesCeEvcMapType_Object = MibTableColumn
mesCeEvcMapType = _MesCeEvcMapType_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 5, 1, 1, 4),
    _MesCeEvcMapType_Type()
)
mesCeEvcMapType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesCeEvcMapType.setStatus("current")


class _MesCeEvcMapVlanIdRangeLower_Type(Unsigned32):
    """Custom type mesCeEvcMapVlanIdRangeLower based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_MesCeEvcMapVlanIdRangeLower_Type.__name__ = "Unsigned32"
_MesCeEvcMapVlanIdRangeLower_Object = MibTableColumn
mesCeEvcMapVlanIdRangeLower = _MesCeEvcMapVlanIdRangeLower_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 5, 1, 1, 5),
    _MesCeEvcMapVlanIdRangeLower_Type()
)
mesCeEvcMapVlanIdRangeLower.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesCeEvcMapVlanIdRangeLower.setStatus("current")


class _MesCeEvcMapVlanIdRangeUpper_Type(Unsigned32):
    """Custom type mesCeEvcMapVlanIdRangeUpper based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_MesCeEvcMapVlanIdRangeUpper_Type.__name__ = "Unsigned32"
_MesCeEvcMapVlanIdRangeUpper_Object = MibTableColumn
mesCeEvcMapVlanIdRangeUpper = _MesCeEvcMapVlanIdRangeUpper_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 5, 1, 1, 6),
    _MesCeEvcMapVlanIdRangeUpper_Type()
)
mesCeEvcMapVlanIdRangeUpper.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesCeEvcMapVlanIdRangeUpper.setStatus("current")
_MesCeEvcMapEvcId_Type = MgmtNameString
_MesCeEvcMapEvcId_Object = MibTableColumn
mesCeEvcMapEvcId = _MesCeEvcMapEvcId_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 5, 1, 1, 7),
    _MesCeEvcMapEvcId_Type()
)
mesCeEvcMapEvcId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesCeEvcMapEvcId.setStatus("current")


class _MesCeEvcMapInternalReference_Type(Unsigned32):
    """Custom type mesCeEvcMapInternalReference based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MesCeEvcMapInternalReference_Type.__name__ = "Unsigned32"
_MesCeEvcMapInternalReference_Object = MibTableColumn
mesCeEvcMapInternalReference = _MesCeEvcMapInternalReference_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 5, 1, 1, 8),
    _MesCeEvcMapInternalReference_Type()
)
mesCeEvcMapInternalReference.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesCeEvcMapInternalReference.setStatus("current")
_MesCeEvcMapRowStatus_Type = RowStatus
_MesCeEvcMapRowStatus_Object = MibTableColumn
mesCeEvcMapRowStatus = _MesCeEvcMapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 5, 1, 1, 9),
    _MesCeEvcMapRowStatus_Type()
)
mesCeEvcMapRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesCeEvcMapRowStatus.setStatus("current")


class _MesCeEvcMapPrio0Included_Type(Integer32):
    """Custom type mesCeEvcMapPrio0Included based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_MesCeEvcMapPrio0Included_Type.__name__ = "Integer32"
_MesCeEvcMapPrio0Included_Object = MibTableColumn
mesCeEvcMapPrio0Included = _MesCeEvcMapPrio0Included_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 5, 1, 1, 10),
    _MesCeEvcMapPrio0Included_Type()
)
mesCeEvcMapPrio0Included.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mesCeEvcMapPrio0Included.setStatus("current")


class _MesCeEvcMapPrio1Included_Type(Integer32):
    """Custom type mesCeEvcMapPrio1Included based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_MesCeEvcMapPrio1Included_Type.__name__ = "Integer32"
_MesCeEvcMapPrio1Included_Object = MibTableColumn
mesCeEvcMapPrio1Included = _MesCeEvcMapPrio1Included_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 5, 1, 1, 11),
    _MesCeEvcMapPrio1Included_Type()
)
mesCeEvcMapPrio1Included.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mesCeEvcMapPrio1Included.setStatus("current")


class _MesCeEvcMapPrio2Included_Type(Integer32):
    """Custom type mesCeEvcMapPrio2Included based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_MesCeEvcMapPrio2Included_Type.__name__ = "Integer32"
_MesCeEvcMapPrio2Included_Object = MibTableColumn
mesCeEvcMapPrio2Included = _MesCeEvcMapPrio2Included_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 5, 1, 1, 12),
    _MesCeEvcMapPrio2Included_Type()
)
mesCeEvcMapPrio2Included.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mesCeEvcMapPrio2Included.setStatus("current")


class _MesCeEvcMapPrio3Included_Type(Integer32):
    """Custom type mesCeEvcMapPrio3Included based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_MesCeEvcMapPrio3Included_Type.__name__ = "Integer32"
_MesCeEvcMapPrio3Included_Object = MibTableColumn
mesCeEvcMapPrio3Included = _MesCeEvcMapPrio3Included_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 5, 1, 1, 13),
    _MesCeEvcMapPrio3Included_Type()
)
mesCeEvcMapPrio3Included.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mesCeEvcMapPrio3Included.setStatus("current")


class _MesCeEvcMapPrio4Included_Type(Integer32):
    """Custom type mesCeEvcMapPrio4Included based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_MesCeEvcMapPrio4Included_Type.__name__ = "Integer32"
_MesCeEvcMapPrio4Included_Object = MibTableColumn
mesCeEvcMapPrio4Included = _MesCeEvcMapPrio4Included_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 5, 1, 1, 14),
    _MesCeEvcMapPrio4Included_Type()
)
mesCeEvcMapPrio4Included.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mesCeEvcMapPrio4Included.setStatus("current")


class _MesCeEvcMapPrio5Included_Type(Integer32):
    """Custom type mesCeEvcMapPrio5Included based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_MesCeEvcMapPrio5Included_Type.__name__ = "Integer32"
_MesCeEvcMapPrio5Included_Object = MibTableColumn
mesCeEvcMapPrio5Included = _MesCeEvcMapPrio5Included_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 5, 1, 1, 15),
    _MesCeEvcMapPrio5Included_Type()
)
mesCeEvcMapPrio5Included.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mesCeEvcMapPrio5Included.setStatus("current")


class _MesCeEvcMapPrio6Included_Type(Integer32):
    """Custom type mesCeEvcMapPrio6Included based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_MesCeEvcMapPrio6Included_Type.__name__ = "Integer32"
_MesCeEvcMapPrio6Included_Object = MibTableColumn
mesCeEvcMapPrio6Included = _MesCeEvcMapPrio6Included_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 5, 1, 1, 16),
    _MesCeEvcMapPrio6Included_Type()
)
mesCeEvcMapPrio6Included.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mesCeEvcMapPrio6Included.setStatus("current")


class _MesCeEvcMapPrio7Included_Type(Integer32):
    """Custom type mesCeEvcMapPrio7Included based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_MesCeEvcMapPrio7Included_Type.__name__ = "Integer32"
_MesCeEvcMapPrio7Included_Object = MibTableColumn
mesCeEvcMapPrio7Included = _MesCeEvcMapPrio7Included_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 5, 1, 1, 17),
    _MesCeEvcMapPrio7Included_Type()
)
mesCeEvcMapPrio7Included.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mesCeEvcMapPrio7Included.setStatus("current")


class _MesCeEvcMapDefaultCeVlanId_Type(Unsigned32):
    """Custom type mesCeEvcMapDefaultCeVlanId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_MesCeEvcMapDefaultCeVlanId_Type.__name__ = "Unsigned32"
_MesCeEvcMapDefaultCeVlanId_Object = MibTableColumn
mesCeEvcMapDefaultCeVlanId = _MesCeEvcMapDefaultCeVlanId_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 5, 1, 1, 18),
    _MesCeEvcMapDefaultCeVlanId_Type()
)
mesCeEvcMapDefaultCeVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesCeEvcMapDefaultCeVlanId.setStatus("current")


class _MesCeEvcMapPrioIncluded_Type(Unsigned32):
    """Custom type mesCeEvcMapPrioIncluded based on Unsigned32"""
    defaultValue = 255

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MesCeEvcMapPrioIncluded_Type.__name__ = "Unsigned32"
_MesCeEvcMapPrioIncluded_Object = MibTableColumn
mesCeEvcMapPrioIncluded = _MesCeEvcMapPrioIncluded_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 5, 1, 1, 19),
    _MesCeEvcMapPrioIncluded_Type()
)
mesCeEvcMapPrioIncluded.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesCeEvcMapPrioIncluded.setStatus("current")
_MesBwpList_ObjectIdentity = ObjectIdentity
mesBwpList = _MesBwpList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 6)
)
_MesBwpTable_Object = MibTable
mesBwpTable = _MesBwpTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 6, 1)
)
if mibBuilder.loadTexts:
    mesBwpTable.setStatus("current")
_MesBwpEntry_Object = MibTableRow
mesBwpEntry = _MesBwpEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 6, 1, 1)
)
mesBwpEntry.setIndexNames(
    (0, "LUM-MES-MIB", "mesBwpIndex"),
)
if mibBuilder.loadTexts:
    mesBwpEntry.setStatus("current")


class _MesBwpIndex_Type(Unsigned32):
    """Custom type mesBwpIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_MesBwpIndex_Type.__name__ = "Unsigned32"
_MesBwpIndex_Object = MibTableColumn
mesBwpIndex = _MesBwpIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 6, 1, 1, 1),
    _MesBwpIndex_Type()
)
mesBwpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesBwpIndex.setStatus("current")
_MesBwpName_Type = MgmtNameString
_MesBwpName_Object = MibTableColumn
mesBwpName = _MesBwpName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 6, 1, 1, 2),
    _MesBwpName_Type()
)
mesBwpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesBwpName.setStatus("current")
_MesBwpObjectProperty_Type = ObjectProperty
_MesBwpObjectProperty_Object = MibTableColumn
mesBwpObjectProperty = _MesBwpObjectProperty_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 6, 1, 1, 3),
    _MesBwpObjectProperty_Type()
)
mesBwpObjectProperty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesBwpObjectProperty.setStatus("current")


class _MesBwpCoSIdentifier_Type(MgmtNameString):
    """Custom type mesBwpCoSIdentifier based on MgmtNameString"""
    subtypeSpec = MgmtNameString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 24),
    )


_MesBwpCoSIdentifier_Type.__name__ = "MgmtNameString"
_MesBwpCoSIdentifier_Object = MibTableColumn
mesBwpCoSIdentifier = _MesBwpCoSIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 6, 1, 1, 4),
    _MesBwpCoSIdentifier_Type()
)
mesBwpCoSIdentifier.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesBwpCoSIdentifier.setStatus("current")


class _MesBwpCir_Type(Unsigned32):
    """Custom type mesBwpCir based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000000),
    )


_MesBwpCir_Type.__name__ = "Unsigned32"
_MesBwpCir_Object = MibTableColumn
mesBwpCir = _MesBwpCir_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 6, 1, 1, 5),
    _MesBwpCir_Type()
)
mesBwpCir.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mesBwpCir.setStatus("current")


class _MesBwpCbs_Type(Unsigned32):
    """Custom type mesBwpCbs based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MesBwpCbs_Type.__name__ = "Unsigned32"
_MesBwpCbs_Object = MibTableColumn
mesBwpCbs = _MesBwpCbs_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 6, 1, 1, 6),
    _MesBwpCbs_Type()
)
mesBwpCbs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mesBwpCbs.setStatus("current")


class _MesBwpEir_Type(Unsigned32):
    """Custom type mesBwpEir based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000000),
    )


_MesBwpEir_Type.__name__ = "Unsigned32"
_MesBwpEir_Object = MibTableColumn
mesBwpEir = _MesBwpEir_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 6, 1, 1, 7),
    _MesBwpEir_Type()
)
mesBwpEir.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mesBwpEir.setStatus("current")


class _MesBwpEbs_Type(Unsigned32):
    """Custom type mesBwpEbs based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MesBwpEbs_Type.__name__ = "Unsigned32"
_MesBwpEbs_Object = MibTableColumn
mesBwpEbs = _MesBwpEbs_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 6, 1, 1, 8),
    _MesBwpEbs_Type()
)
mesBwpEbs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mesBwpEbs.setStatus("current")


class _MesBwpCouplingFlag_Type(Unsigned32):
    """Custom type mesBwpCouplingFlag based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_MesBwpCouplingFlag_Type.__name__ = "Unsigned32"
_MesBwpCouplingFlag_Object = MibTableColumn
mesBwpCouplingFlag = _MesBwpCouplingFlag_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 6, 1, 1, 9),
    _MesBwpCouplingFlag_Type()
)
mesBwpCouplingFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesBwpCouplingFlag.setStatus("current")


class _MesBwpColorMode_Type(Integer32):
    """Custom type mesBwpColorMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("colorAware", 1),
          ("colorBlind", 2))
    )


_MesBwpColorMode_Type.__name__ = "Integer32"
_MesBwpColorMode_Object = MibTableColumn
mesBwpColorMode = _MesBwpColorMode_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 6, 1, 1, 10),
    _MesBwpColorMode_Type()
)
mesBwpColorMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mesBwpColorMode.setStatus("current")


class _MesBwpInternalReference_Type(Unsigned32):
    """Custom type mesBwpInternalReference based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MesBwpInternalReference_Type.__name__ = "Unsigned32"
_MesBwpInternalReference_Object = MibTableColumn
mesBwpInternalReference = _MesBwpInternalReference_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 6, 1, 1, 11),
    _MesBwpInternalReference_Type()
)
mesBwpInternalReference.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesBwpInternalReference.setStatus("current")
_MesBwpRowStatus_Type = RowStatus
_MesBwpRowStatus_Object = MibTableColumn
mesBwpRowStatus = _MesBwpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 6, 1, 1, 12),
    _MesBwpRowStatus_Type()
)
mesBwpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesBwpRowStatus.setStatus("current")


class _MesBwpServiceId_Type(ServiceIdWithNotUsed):
    """Custom type mesBwpServiceId based on ServiceIdWithNotUsed"""
    defaultValue = -1


_MesBwpServiceId_Type.__name__ = "ServiceIdWithNotUsed"
_MesBwpServiceId_Object = MibTableColumn
mesBwpServiceId = _MesBwpServiceId_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 6, 1, 1, 13),
    _MesBwpServiceId_Type()
)
mesBwpServiceId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mesBwpServiceId.setStatus("current")


class _MesBwpPolicerId_Type(Integer32):
    """Custom type mesBwpPolicerId based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_MesBwpPolicerId_Type.__name__ = "Integer32"
_MesBwpPolicerId_Object = MibTableColumn
mesBwpPolicerId = _MesBwpPolicerId_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 6, 1, 1, 14),
    _MesBwpPolicerId_Type()
)
mesBwpPolicerId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesBwpPolicerId.setStatus("current")
_MesBwpSubrack_Type = SubrackNumber
_MesBwpSubrack_Object = MibTableColumn
mesBwpSubrack = _MesBwpSubrack_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 6, 1, 1, 15),
    _MesBwpSubrack_Type()
)
mesBwpSubrack.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesBwpSubrack.setStatus("current")
_MesBwpSlot_Type = SlotNumber
_MesBwpSlot_Object = MibTableColumn
mesBwpSlot = _MesBwpSlot_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 6, 1, 1, 16),
    _MesBwpSlot_Type()
)
mesBwpSlot.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesBwpSlot.setStatus("current")
_MesQProfileList_ObjectIdentity = ObjectIdentity
mesQProfileList = _MesQProfileList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 7)
)
_MesQProfileTable_Object = MibTable
mesQProfileTable = _MesQProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 7, 1)
)
if mibBuilder.loadTexts:
    mesQProfileTable.setStatus("obsolete")
_MesQProfileEntry_Object = MibTableRow
mesQProfileEntry = _MesQProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 7, 1, 1)
)
mesQProfileEntry.setIndexNames(
    (0, "LUM-MES-MIB", "mesQProfileIndex"),
)
if mibBuilder.loadTexts:
    mesQProfileEntry.setStatus("current")


class _MesQProfileIndex_Type(Unsigned32):
    """Custom type mesQProfileIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_MesQProfileIndex_Type.__name__ = "Unsigned32"
_MesQProfileIndex_Object = MibTableColumn
mesQProfileIndex = _MesQProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 7, 1, 1, 1),
    _MesQProfileIndex_Type()
)
mesQProfileIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesQProfileIndex.setStatus("current")
_MesQProfileName_Type = MgmtNameString
_MesQProfileName_Object = MibTableColumn
mesQProfileName = _MesQProfileName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 7, 1, 1, 2),
    _MesQProfileName_Type()
)
mesQProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesQProfileName.setStatus("current")
_MesQProfileObjectProperty_Type = ObjectProperty
_MesQProfileObjectProperty_Object = MibTableColumn
mesQProfileObjectProperty = _MesQProfileObjectProperty_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 7, 1, 1, 3),
    _MesQProfileObjectProperty_Type()
)
mesQProfileObjectProperty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesQProfileObjectProperty.setStatus("current")
_MesQProfileId_Type = MesQProfileId
_MesQProfileId_Object = MibTableColumn
mesQProfileId = _MesQProfileId_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 7, 1, 1, 4),
    _MesQProfileId_Type()
)
mesQProfileId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesQProfileId.setStatus("current")


class _MesQProfileType_Type(Integer32):
    """Custom type mesQProfileType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("strictPriority", 1),
          ("roundRobin", 2),
          ("weightedRoundRobin", 3))
    )


_MesQProfileType_Type.__name__ = "Integer32"
_MesQProfileType_Object = MibTableColumn
mesQProfileType = _MesQProfileType_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 7, 1, 1, 5),
    _MesQProfileType_Type()
)
mesQProfileType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesQProfileType.setStatus("current")


class _MesQProfileWeight_Type(Unsigned32):
    """Custom type mesQProfileWeight based on Unsigned32"""
    defaultValue = 63

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_MesQProfileWeight_Type.__name__ = "Unsigned32"
_MesQProfileWeight_Object = MibTableColumn
mesQProfileWeight = _MesQProfileWeight_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 7, 1, 1, 6),
    _MesQProfileWeight_Type()
)
mesQProfileWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mesQProfileWeight.setStatus("current")


class _MesQProfileGreenLowThreshold_Type(Unsigned32):
    """Custom type mesQProfileGreenLowThreshold based on Unsigned32"""
    defaultValue = 81920

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(9600, 524288),
    )


_MesQProfileGreenLowThreshold_Type.__name__ = "Unsigned32"
_MesQProfileGreenLowThreshold_Object = MibTableColumn
mesQProfileGreenLowThreshold = _MesQProfileGreenLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 7, 1, 1, 7),
    _MesQProfileGreenLowThreshold_Type()
)
mesQProfileGreenLowThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mesQProfileGreenLowThreshold.setStatus("current")


class _MesQProfileGreenHighThreshold_Type(Unsigned32):
    """Custom type mesQProfileGreenHighThreshold based on Unsigned32"""
    defaultValue = 163840

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(9600, 524288),
    )


_MesQProfileGreenHighThreshold_Type.__name__ = "Unsigned32"
_MesQProfileGreenHighThreshold_Object = MibTableColumn
mesQProfileGreenHighThreshold = _MesQProfileGreenHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 7, 1, 1, 8),
    _MesQProfileGreenHighThreshold_Type()
)
mesQProfileGreenHighThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mesQProfileGreenHighThreshold.setStatus("current")


class _MesQProfileGreenDropProbability_Type(Unsigned32):
    """Custom type mesQProfileGreenDropProbability based on Unsigned32"""
    defaultValue = 77

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_MesQProfileGreenDropProbability_Type.__name__ = "Unsigned32"
_MesQProfileGreenDropProbability_Object = MibTableColumn
mesQProfileGreenDropProbability = _MesQProfileGreenDropProbability_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 7, 1, 1, 9),
    _MesQProfileGreenDropProbability_Type()
)
mesQProfileGreenDropProbability.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mesQProfileGreenDropProbability.setStatus("current")


class _MesQProfileYellowLowThreshold_Type(Unsigned32):
    """Custom type mesQProfileYellowLowThreshold based on Unsigned32"""
    defaultValue = 40960

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(9600, 524288),
    )


_MesQProfileYellowLowThreshold_Type.__name__ = "Unsigned32"
_MesQProfileYellowLowThreshold_Object = MibTableColumn
mesQProfileYellowLowThreshold = _MesQProfileYellowLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 7, 1, 1, 10),
    _MesQProfileYellowLowThreshold_Type()
)
mesQProfileYellowLowThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mesQProfileYellowLowThreshold.setStatus("current")


class _MesQProfileYellowHighThreshold_Type(Unsigned32):
    """Custom type mesQProfileYellowHighThreshold based on Unsigned32"""
    defaultValue = 81920

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(9600, 524288),
    )


_MesQProfileYellowHighThreshold_Type.__name__ = "Unsigned32"
_MesQProfileYellowHighThreshold_Object = MibTableColumn
mesQProfileYellowHighThreshold = _MesQProfileYellowHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 7, 1, 1, 11),
    _MesQProfileYellowHighThreshold_Type()
)
mesQProfileYellowHighThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mesQProfileYellowHighThreshold.setStatus("current")


class _MesQProfileYellowDropProbability_Type(Unsigned32):
    """Custom type mesQProfileYellowDropProbability based on Unsigned32"""
    defaultValue = 85

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_MesQProfileYellowDropProbability_Type.__name__ = "Unsigned32"
_MesQProfileYellowDropProbability_Object = MibTableColumn
mesQProfileYellowDropProbability = _MesQProfileYellowDropProbability_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 7, 1, 1, 12),
    _MesQProfileYellowDropProbability_Type()
)
mesQProfileYellowDropProbability.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mesQProfileYellowDropProbability.setStatus("current")


class _MesQProfileInternalReference_Type(Unsigned32):
    """Custom type mesQProfileInternalReference based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MesQProfileInternalReference_Type.__name__ = "Unsigned32"
_MesQProfileInternalReference_Object = MibTableColumn
mesQProfileInternalReference = _MesQProfileInternalReference_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 7, 1, 1, 13),
    _MesQProfileInternalReference_Type()
)
mesQProfileInternalReference.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesQProfileInternalReference.setStatus("current")
_MesMepList_ObjectIdentity = ObjectIdentity
mesMepList = _MesMepList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 8)
)
_MesMepTable_Object = MibTable
mesMepTable = _MesMepTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 8, 1)
)
if mibBuilder.loadTexts:
    mesMepTable.setStatus("obsolete")
_MesMepEntry_Object = MibTableRow
mesMepEntry = _MesMepEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 8, 1, 1)
)
mesMepEntry.setIndexNames(
    (0, "LUM-MES-MIB", "mesMepIndex"),
)
if mibBuilder.loadTexts:
    mesMepEntry.setStatus("current")


class _MesMepIndex_Type(Unsigned32):
    """Custom type mesMepIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_MesMepIndex_Type.__name__ = "Unsigned32"
_MesMepIndex_Object = MibTableColumn
mesMepIndex = _MesMepIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 8, 1, 1, 1),
    _MesMepIndex_Type()
)
mesMepIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesMepIndex.setStatus("current")
_MesMepName_Type = MgmtNameString
_MesMepName_Object = MibTableColumn
mesMepName = _MesMepName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 8, 1, 1, 2),
    _MesMepName_Type()
)
mesMepName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesMepName.setStatus("current")
_MesMepObjectProperty_Type = ObjectProperty
_MesMepObjectProperty_Object = MibTableColumn
mesMepObjectProperty = _MesMepObjectProperty_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 8, 1, 1, 3),
    _MesMepObjectProperty_Type()
)
mesMepObjectProperty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesMepObjectProperty.setStatus("current")


class _MesMepInternalReference_Type(Unsigned32):
    """Custom type mesMepInternalReference based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MesMepInternalReference_Type.__name__ = "Unsigned32"
_MesMepInternalReference_Object = MibTableColumn
mesMepInternalReference = _MesMepInternalReference_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 8, 1, 1, 4),
    _MesMepInternalReference_Type()
)
mesMepInternalReference.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesMepInternalReference.setStatus("current")


class _MesMepMeIdentifier_Type(MgmtNameString):
    """Custom type mesMepMeIdentifier based on MgmtNameString"""
    defaultValue = OctetString("")


_MesMepMeIdentifier_Type.__name__ = "MgmtNameString"
_MesMepMeIdentifier_Object = MibTableColumn
mesMepMeIdentifier = _MesMepMeIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 8, 1, 1, 5),
    _MesMepMeIdentifier_Type()
)
mesMepMeIdentifier.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesMepMeIdentifier.setStatus("current")


class _MesMepAdminStatus_Type(BoardOrInterfaceAdminStatus):
    """Custom type mesMepAdminStatus based on BoardOrInterfaceAdminStatus"""
    defaultValue = 1


_MesMepAdminStatus_Type.__name__ = "BoardOrInterfaceAdminStatus"
_MesMepAdminStatus_Object = MibTableColumn
mesMepAdminStatus = _MesMepAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 8, 1, 1, 6),
    _MesMepAdminStatus_Type()
)
mesMepAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mesMepAdminStatus.setStatus("current")


class _MesMepOperStatus_Type(BoardOrInterfaceOperStatus):
    """Custom type mesMepOperStatus based on BoardOrInterfaceOperStatus"""
    defaultValue = 1


_MesMepOperStatus_Type.__name__ = "BoardOrInterfaceOperStatus"
_MesMepOperStatus_Object = MibTableColumn
mesMepOperStatus = _MesMepOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 8, 1, 1, 7),
    _MesMepOperStatus_Type()
)
mesMepOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesMepOperStatus.setStatus("current")


class _MesMepTransmissionInterval_Type(Unsigned32):
    """Custom type mesMepTransmissionInterval based on Unsigned32"""
    defaultValue = 1000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 600000),
    )


_MesMepTransmissionInterval_Type.__name__ = "Unsigned32"
_MesMepTransmissionInterval_Object = MibTableColumn
mesMepTransmissionInterval = _MesMepTransmissionInterval_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 8, 1, 1, 8),
    _MesMepTransmissionInterval_Type()
)
mesMepTransmissionInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mesMepTransmissionInterval.setStatus("current")
_MesMepLossOfContinuity_Type = FaultStatus
_MesMepLossOfContinuity_Object = MibTableColumn
mesMepLossOfContinuity = _MesMepLossOfContinuity_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 8, 1, 1, 9),
    _MesMepLossOfContinuity_Type()
)
mesMepLossOfContinuity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesMepLossOfContinuity.setStatus("current")
_MesMepUnexpectedMegId_Type = FaultStatus
_MesMepUnexpectedMegId_Object = MibTableColumn
mesMepUnexpectedMegId = _MesMepUnexpectedMegId_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 8, 1, 1, 10),
    _MesMepUnexpectedMegId_Type()
)
mesMepUnexpectedMegId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesMepUnexpectedMegId.setStatus("current")
_MesMepUnexpectedTransmissionInterval_Type = FaultStatus
_MesMepUnexpectedTransmissionInterval_Object = MibTableColumn
mesMepUnexpectedTransmissionInterval = _MesMepUnexpectedTransmissionInterval_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 8, 1, 1, 11),
    _MesMepUnexpectedTransmissionInterval_Type()
)
mesMepUnexpectedTransmissionInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesMepUnexpectedTransmissionInterval.setStatus("current")
_MesMepRemoteDefectIndication_Type = FaultStatus
_MesMepRemoteDefectIndication_Object = MibTableColumn
mesMepRemoteDefectIndication = _MesMepRemoteDefectIndication_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 8, 1, 1, 12),
    _MesMepRemoteDefectIndication_Type()
)
mesMepRemoteDefectIndication.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesMepRemoteDefectIndication.setStatus("current")
_MesMepUnexpectedOpCode_Type = FaultStatus
_MesMepUnexpectedOpCode_Object = MibTableColumn
mesMepUnexpectedOpCode = _MesMepUnexpectedOpCode_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 8, 1, 1, 13),
    _MesMepUnexpectedOpCode_Type()
)
mesMepUnexpectedOpCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesMepUnexpectedOpCode.setStatus("current")
_MesMepAlarmIndicationSignal_Type = FaultStatus
_MesMepAlarmIndicationSignal_Object = MibTableColumn
mesMepAlarmIndicationSignal = _MesMepAlarmIndicationSignal_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 8, 1, 1, 14),
    _MesMepAlarmIndicationSignal_Type()
)
mesMepAlarmIndicationSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesMepAlarmIndicationSignal.setStatus("current")


class _MesMepMegIdFormatReceived_Type(Integer32):
    """Custom type mesMepMegIdFormatReceived based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              32)
        )
    )
    namedValues = NamedValues(
        *(("other", 0),
          ("icc", 32))
    )


_MesMepMegIdFormatReceived_Type.__name__ = "Integer32"
_MesMepMegIdFormatReceived_Object = MibTableColumn
mesMepMegIdFormatReceived = _MesMepMegIdFormatReceived_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 8, 1, 1, 15),
    _MesMepMegIdFormatReceived_Type()
)
mesMepMegIdFormatReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesMepMegIdFormatReceived.setStatus("current")


class _MesMepMegIdIccReceived_Type(DisplayString):
    """Custom type mesMepMegIdIccReceived based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 13),
    )


_MesMepMegIdIccReceived_Type.__name__ = "DisplayString"
_MesMepMegIdIccReceived_Object = MibTableColumn
mesMepMegIdIccReceived = _MesMepMegIdIccReceived_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 8, 1, 1, 16),
    _MesMepMegIdIccReceived_Type()
)
mesMepMegIdIccReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesMepMegIdIccReceived.setStatus("current")


class _MesMepMegIdReceived_Type(OctetString):
    """Custom type mesMepMegIdReceived based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(48, 48),
    )
    fixed_length = 48


_MesMepMegIdReceived_Type.__name__ = "OctetString"
_MesMepMegIdReceived_Object = MibTableColumn
mesMepMegIdReceived = _MesMepMegIdReceived_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 8, 1, 1, 17),
    _MesMepMegIdReceived_Type()
)
mesMepMegIdReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesMepMegIdReceived.setStatus("current")


class _MesMepId_Type(Unsigned32):
    """Custom type mesMepId based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8191),
    )


_MesMepId_Type.__name__ = "Unsigned32"
_MesMepId_Object = MibTableColumn
mesMepId = _MesMepId_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 8, 1, 1, 18),
    _MesMepId_Type()
)
mesMepId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mesMepId.setStatus("current")


class _MesMepIdExpected_Type(Unsigned32):
    """Custom type mesMepIdExpected based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8191),
    )


_MesMepIdExpected_Type.__name__ = "Unsigned32"
_MesMepIdExpected_Object = MibTableColumn
mesMepIdExpected = _MesMepIdExpected_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 8, 1, 1, 19),
    _MesMepIdExpected_Type()
)
mesMepIdExpected.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mesMepIdExpected.setStatus("current")


class _MesMepIdReceived_Type(Unsigned32):
    """Custom type mesMepIdReceived based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8191),
    )


_MesMepIdReceived_Type.__name__ = "Unsigned32"
_MesMepIdReceived_Object = MibTableColumn
mesMepIdReceived = _MesMepIdReceived_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 8, 1, 1, 20),
    _MesMepIdReceived_Type()
)
mesMepIdReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesMepIdReceived.setStatus("current")
_MesMepUnexpectedMepId_Type = FaultStatus
_MesMepUnexpectedMepId_Object = MibTableColumn
mesMepUnexpectedMepId = _MesMepUnexpectedMepId_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 8, 1, 1, 21),
    _MesMepUnexpectedMepId_Type()
)
mesMepUnexpectedMepId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesMepUnexpectedMepId.setStatus("current")
_MesMepUnexpectedMegLevel_Type = FaultStatus
_MesMepUnexpectedMegLevel_Object = MibTableColumn
mesMepUnexpectedMegLevel = _MesMepUnexpectedMegLevel_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 8, 1, 1, 22),
    _MesMepUnexpectedMegLevel_Type()
)
mesMepUnexpectedMegLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesMepUnexpectedMegLevel.setStatus("current")


class _MesMepMegId_Type(OctetString):
    """Custom type mesMepMegId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(48, 48),
    )
    fixed_length = 48


_MesMepMegId_Type.__name__ = "OctetString"
_MesMepMegId_Object = MibTableColumn
mesMepMegId = _MesMepMegId_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 8, 1, 1, 23),
    _MesMepMegId_Type()
)
mesMepMegId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mesMepMegId.setStatus("current")


class _MesMepMegIdFormat_Type(Integer32):
    """Custom type mesMepMegIdFormat based on Integer32"""
    defaultValue = 32

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            32
        )
    )
    namedValues = NamedValues(
        ("icc", 32)
    )


_MesMepMegIdFormat_Type.__name__ = "Integer32"
_MesMepMegIdFormat_Object = MibTableColumn
mesMepMegIdFormat = _MesMepMegIdFormat_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 8, 1, 1, 24),
    _MesMepMegIdFormat_Type()
)
mesMepMegIdFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mesMepMegIdFormat.setStatus("current")


class _MesMepMegIdIcc_Type(DisplayString):
    """Custom type mesMepMegIdIcc based on DisplayString"""
    defaultValue = OctetString("undefined")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 13),
    )


_MesMepMegIdIcc_Type.__name__ = "DisplayString"
_MesMepMegIdIcc_Object = MibTableColumn
mesMepMegIdIcc = _MesMepMegIdIcc_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 8, 1, 1, 25),
    _MesMepMegIdIcc_Type()
)
mesMepMegIdIcc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mesMepMegIdIcc.setStatus("current")
_MesMegList_ObjectIdentity = ObjectIdentity
mesMegList = _MesMegList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 9)
)
_MesMegTable_Object = MibTable
mesMegTable = _MesMegTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 9, 1)
)
if mibBuilder.loadTexts:
    mesMegTable.setStatus("obsolete")
_MesMegEntry_Object = MibTableRow
mesMegEntry = _MesMegEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 9, 1, 1)
)
mesMegEntry.setIndexNames(
    (0, "LUM-MES-MIB", "mesMegIndex"),
)
if mibBuilder.loadTexts:
    mesMegEntry.setStatus("current")


class _MesMegIndex_Type(Unsigned32):
    """Custom type mesMegIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_MesMegIndex_Type.__name__ = "Unsigned32"
_MesMegIndex_Object = MibTableColumn
mesMegIndex = _MesMegIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 9, 1, 1, 1),
    _MesMegIndex_Type()
)
mesMegIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesMegIndex.setStatus("current")
_MesMegName_Type = MgmtNameString
_MesMegName_Object = MibTableColumn
mesMegName = _MesMegName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 9, 1, 1, 2),
    _MesMegName_Type()
)
mesMegName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesMegName.setStatus("current")
_MesMegObjectProperty_Type = ObjectProperty
_MesMegObjectProperty_Object = MibTableColumn
mesMegObjectProperty = _MesMegObjectProperty_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 9, 1, 1, 3),
    _MesMegObjectProperty_Type()
)
mesMegObjectProperty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesMegObjectProperty.setStatus("current")


class _MesMegInternalReference_Type(Unsigned32):
    """Custom type mesMegInternalReference based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MesMegInternalReference_Type.__name__ = "Unsigned32"
_MesMegInternalReference_Object = MibTableColumn
mesMegInternalReference = _MesMegInternalReference_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 9, 1, 1, 4),
    _MesMegInternalReference_Type()
)
mesMegInternalReference.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesMegInternalReference.setStatus("current")


class _MesMegAdminStatus_Type(BoardOrInterfaceAdminStatus):
    """Custom type mesMegAdminStatus based on BoardOrInterfaceAdminStatus"""
    defaultValue = 1


_MesMegAdminStatus_Type.__name__ = "BoardOrInterfaceAdminStatus"
_MesMegAdminStatus_Object = MibTableColumn
mesMegAdminStatus = _MesMegAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 9, 1, 1, 5),
    _MesMegAdminStatus_Type()
)
mesMegAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mesMegAdminStatus.setStatus("current")


class _MesMegOperStatus_Type(BoardOrInterfaceOperStatus):
    """Custom type mesMegOperStatus based on BoardOrInterfaceOperStatus"""
    defaultValue = 1


_MesMegOperStatus_Type.__name__ = "BoardOrInterfaceOperStatus"
_MesMegOperStatus_Object = MibTableColumn
mesMegOperStatus = _MesMegOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 9, 1, 1, 6),
    _MesMegOperStatus_Type()
)
mesMegOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesMegOperStatus.setStatus("current")


class _MesMegLevel_Type(Unsigned32):
    """Custom type mesMegLevel based on Unsigned32"""
    defaultValue = 4

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_MesMegLevel_Type.__name__ = "Unsigned32"
_MesMegLevel_Object = MibTableColumn
mesMegLevel = _MesMegLevel_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 9, 1, 1, 10),
    _MesMegLevel_Type()
)
mesMegLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mesMegLevel.setStatus("current")
_MesMegUnexpectedMessage_Type = FaultStatus
_MesMegUnexpectedMessage_Object = MibTableColumn
mesMegUnexpectedMessage = _MesMegUnexpectedMessage_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 9, 1, 1, 11),
    _MesMegUnexpectedMessage_Type()
)
mesMegUnexpectedMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesMegUnexpectedMessage.setStatus("current")
_MesMiscList_ObjectIdentity = ObjectIdentity
mesMiscList = _MesMiscList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 10)
)
_MesMiscTable_Object = MibTable
mesMiscTable = _MesMiscTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 10, 1)
)
if mibBuilder.loadTexts:
    mesMiscTable.setStatus("current")
_MesMiscEntry_Object = MibTableRow
mesMiscEntry = _MesMiscEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 10, 1, 1)
)
mesMiscEntry.setIndexNames(
    (0, "LUM-MES-MIB", "mesMiscIndex"),
)
if mibBuilder.loadTexts:
    mesMiscEntry.setStatus("current")


class _MesMiscIndex_Type(Unsigned32):
    """Custom type mesMiscIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_MesMiscIndex_Type.__name__ = "Unsigned32"
_MesMiscIndex_Object = MibTableColumn
mesMiscIndex = _MesMiscIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 10, 1, 1, 1),
    _MesMiscIndex_Type()
)
mesMiscIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesMiscIndex.setStatus("current")
_MesMiscName_Type = MgmtNameString
_MesMiscName_Object = MibTableColumn
mesMiscName = _MesMiscName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 10, 1, 1, 2),
    _MesMiscName_Type()
)
mesMiscName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesMiscName.setStatus("current")
_MesMiscObjectProperty_Type = ObjectProperty
_MesMiscObjectProperty_Object = MibTableColumn
mesMiscObjectProperty = _MesMiscObjectProperty_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 10, 1, 1, 3),
    _MesMiscObjectProperty_Type()
)
mesMiscObjectProperty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesMiscObjectProperty.setStatus("current")


class _MesMiscInternalReference_Type(Unsigned32):
    """Custom type mesMiscInternalReference based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MesMiscInternalReference_Type.__name__ = "Unsigned32"
_MesMiscInternalReference_Object = MibTableColumn
mesMiscInternalReference = _MesMiscInternalReference_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 10, 1, 1, 4),
    _MesMiscInternalReference_Type()
)
mesMiscInternalReference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesMiscInternalReference.setStatus("current")


class _MesMiscAdminStatus_Type(BoardOrInterfaceAdminStatus):
    """Custom type mesMiscAdminStatus based on BoardOrInterfaceAdminStatus"""
    defaultValue = 1


_MesMiscAdminStatus_Type.__name__ = "BoardOrInterfaceAdminStatus"
_MesMiscAdminStatus_Object = MibTableColumn
mesMiscAdminStatus = _MesMiscAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 10, 1, 1, 5),
    _MesMiscAdminStatus_Type()
)
mesMiscAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mesMiscAdminStatus.setStatus("current")


class _MesMiscOperStatus_Type(BoardOrInterfaceOperStatus):
    """Custom type mesMiscOperStatus based on BoardOrInterfaceOperStatus"""
    defaultValue = 1


_MesMiscOperStatus_Type.__name__ = "BoardOrInterfaceOperStatus"
_MesMiscOperStatus_Object = MibTableColumn
mesMiscOperStatus = _MesMiscOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 10, 1, 1, 6),
    _MesMiscOperStatus_Type()
)
mesMiscOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesMiscOperStatus.setStatus("current")


class _MesMiscMgmtVlanIpAddress_Type(IpAddress):
    """Custom type mesMiscMgmtVlanIpAddress based on IpAddress"""
    defaultHexValue = "00000000"


_MesMiscMgmtVlanIpAddress_Type.__name__ = "IpAddress"
_MesMiscMgmtVlanIpAddress_Object = MibTableColumn
mesMiscMgmtVlanIpAddress = _MesMiscMgmtVlanIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 10, 1, 1, 7),
    _MesMiscMgmtVlanIpAddress_Type()
)
mesMiscMgmtVlanIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesMiscMgmtVlanIpAddress.setStatus("current")


class _MesMiscMgmtVlanNetMask_Type(IpAddress):
    """Custom type mesMiscMgmtVlanNetMask based on IpAddress"""
    defaultHexValue = "00000000"


_MesMiscMgmtVlanNetMask_Type.__name__ = "IpAddress"
_MesMiscMgmtVlanNetMask_Object = MibTableColumn
mesMiscMgmtVlanNetMask = _MesMiscMgmtVlanNetMask_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 10, 1, 1, 8),
    _MesMiscMgmtVlanNetMask_Type()
)
mesMiscMgmtVlanNetMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesMiscMgmtVlanNetMask.setStatus("current")


class _MesMiscMgmtVlanMacAddress0_Type(DisplayString):
    """Custom type mesMiscMgmtVlanMacAddress0 based on DisplayString"""
    defaultValue = OctetString("")


_MesMiscMgmtVlanMacAddress0_Type.__name__ = "DisplayString"
_MesMiscMgmtVlanMacAddress0_Object = MibTableColumn
mesMiscMgmtVlanMacAddress0 = _MesMiscMgmtVlanMacAddress0_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 10, 1, 1, 9),
    _MesMiscMgmtVlanMacAddress0_Type()
)
mesMiscMgmtVlanMacAddress0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesMiscMgmtVlanMacAddress0.setStatus("current")


class _MesMiscMgmtVlanMacAddress1_Type(DisplayString):
    """Custom type mesMiscMgmtVlanMacAddress1 based on DisplayString"""
    defaultValue = OctetString("")


_MesMiscMgmtVlanMacAddress1_Type.__name__ = "DisplayString"
_MesMiscMgmtVlanMacAddress1_Object = MibTableColumn
mesMiscMgmtVlanMacAddress1 = _MesMiscMgmtVlanMacAddress1_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 10, 1, 1, 10),
    _MesMiscMgmtVlanMacAddress1_Type()
)
mesMiscMgmtVlanMacAddress1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesMiscMgmtVlanMacAddress1.setStatus("current")


class _MesMiscMgmtVlanMacAddress2_Type(DisplayString):
    """Custom type mesMiscMgmtVlanMacAddress2 based on DisplayString"""
    defaultValue = OctetString("")


_MesMiscMgmtVlanMacAddress2_Type.__name__ = "DisplayString"
_MesMiscMgmtVlanMacAddress2_Object = MibTableColumn
mesMiscMgmtVlanMacAddress2 = _MesMiscMgmtVlanMacAddress2_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 10, 1, 1, 11),
    _MesMiscMgmtVlanMacAddress2_Type()
)
mesMiscMgmtVlanMacAddress2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesMiscMgmtVlanMacAddress2.setStatus("current")
_MesMiscConfigureAddress_Type = CommandString
_MesMiscConfigureAddress_Object = MibTableColumn
mesMiscConfigureAddress = _MesMiscConfigureAddress_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 10, 1, 1, 12),
    _MesMiscConfigureAddress_Type()
)
mesMiscConfigureAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesMiscConfigureAddress.setStatus("current")


class _MesMiscMgmtVlanNode_Type(Integer32):
    """Custom type mesMiscMgmtVlanNode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("bridge2dcn", 2),
          ("on", 3))
    )


_MesMiscMgmtVlanNode_Type.__name__ = "Integer32"
_MesMiscMgmtVlanNode_Object = MibTableColumn
mesMiscMgmtVlanNode = _MesMiscMgmtVlanNode_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 10, 1, 1, 13),
    _MesMiscMgmtVlanNode_Type()
)
mesMiscMgmtVlanNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesMiscMgmtVlanNode.setStatus("current")


class _MesMiscMacAgeing_Type(Unsigned32):
    """Custom type mesMiscMacAgeing based on Unsigned32"""
    defaultValue = 300

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 1000000),
    )


_MesMiscMacAgeing_Type.__name__ = "Unsigned32"
_MesMiscMacAgeing_Object = MibTableColumn
mesMiscMacAgeing = _MesMiscMacAgeing_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 10, 1, 1, 14),
    _MesMiscMacAgeing_Type()
)
mesMiscMacAgeing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mesMiscMacAgeing.setStatus("current")
_MesMiscMacGetTable_Type = CommandString
_MesMiscMacGetTable_Object = MibTableColumn
mesMiscMacGetTable = _MesMiscMacGetTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 10, 1, 1, 15),
    _MesMiscMacGetTable_Type()
)
mesMiscMacGetTable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesMiscMacGetTable.setStatus("current")


class _MesMiscNoOfMegs_Type(Unsigned32):
    """Custom type mesMiscNoOfMegs based on Unsigned32"""
    defaultValue = 0


_MesMiscNoOfMegs_Type.__name__ = "Unsigned32"
_MesMiscNoOfMegs_Object = MibTableColumn
mesMiscNoOfMegs = _MesMiscNoOfMegs_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 10, 1, 1, 16),
    _MesMiscNoOfMegs_Type()
)
mesMiscNoOfMegs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesMiscNoOfMegs.setStatus("current")
_MesMiscAssociateMeg_Type = CommandString
_MesMiscAssociateMeg_Object = MibTableColumn
mesMiscAssociateMeg = _MesMiscAssociateMeg_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 10, 1, 1, 17),
    _MesMiscAssociateMeg_Type()
)
mesMiscAssociateMeg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesMiscAssociateMeg.setStatus("current")


class _MesMiscNoOfErps_Type(Unsigned32):
    """Custom type mesMiscNoOfErps based on Unsigned32"""
    defaultValue = 0


_MesMiscNoOfErps_Type.__name__ = "Unsigned32"
_MesMiscNoOfErps_Object = MibTableColumn
mesMiscNoOfErps = _MesMiscNoOfErps_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 10, 1, 1, 18),
    _MesMiscNoOfErps_Type()
)
mesMiscNoOfErps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesMiscNoOfErps.setStatus("current")
_MesMiscAssociateErp_Type = CommandString
_MesMiscAssociateErp_Object = MibTableColumn
mesMiscAssociateErp = _MesMiscAssociateErp_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 10, 1, 1, 19),
    _MesMiscAssociateErp_Type()
)
mesMiscAssociateErp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesMiscAssociateErp.setStatus("current")


class _MesMiscL2Mode_Type(Integer32):
    """Custom type mesMiscL2Mode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("switch", 1),
          ("aggregator", 2))
    )


_MesMiscL2Mode_Type.__name__ = "Integer32"
_MesMiscL2Mode_Object = MibTableColumn
mesMiscL2Mode = _MesMiscL2Mode_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 10, 1, 1, 20),
    _MesMiscL2Mode_Type()
)
mesMiscL2Mode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesMiscL2Mode.setStatus("current")
_MesMiscConfigureMode_Type = CommandString
_MesMiscConfigureMode_Object = MibTableColumn
mesMiscConfigureMode = _MesMiscConfigureMode_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 10, 1, 1, 21),
    _MesMiscConfigureMode_Type()
)
mesMiscConfigureMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesMiscConfigureMode.setStatus("current")


class _MesMiscIdentity_Type(Counter64):
    """Custom type mesMiscIdentity based on Counter64"""
    defaultValue = 0


_MesMiscIdentity_Type.__name__ = "Counter64"
_MesMiscIdentity_Object = MibTableColumn
mesMiscIdentity = _MesMiscIdentity_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 10, 1, 1, 22),
    _MesMiscIdentity_Type()
)
mesMiscIdentity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesMiscIdentity.setStatus("current")
_MesMiscAssociateClass_Type = CommandString
_MesMiscAssociateClass_Object = MibTableColumn
mesMiscAssociateClass = _MesMiscAssociateClass_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 10, 1, 1, 23),
    _MesMiscAssociateClass_Type()
)
mesMiscAssociateClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesMiscAssociateClass.setStatus("current")
_MesMiscAssociateBwp_Type = CommandString
_MesMiscAssociateBwp_Object = MibTableColumn
mesMiscAssociateBwp = _MesMiscAssociateBwp_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 10, 1, 1, 24),
    _MesMiscAssociateBwp_Type()
)
mesMiscAssociateBwp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesMiscAssociateBwp.setStatus("current")


class _MesMiscWred_Type(Integer32):
    """Custom type mesMiscWred based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_MesMiscWred_Type.__name__ = "Integer32"
_MesMiscWred_Object = MibTableColumn
mesMiscWred = _MesMiscWred_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 10, 1, 1, 25),
    _MesMiscWred_Type()
)
mesMiscWred.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mesMiscWred.setStatus("current")
_MesMiscGetPacketMonitor_Type = CommandString
_MesMiscGetPacketMonitor_Object = MibTableColumn
mesMiscGetPacketMonitor = _MesMiscGetPacketMonitor_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 10, 1, 1, 26),
    _MesMiscGetPacketMonitor_Type()
)
mesMiscGetPacketMonitor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesMiscGetPacketMonitor.setStatus("current")


class _MesMiscSfpPortUsageCurrent_Type(Integer32):
    """Custom type mesMiscSfpPortUsageCurrent based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("external", 1),
          ("mgmtVlan", 2))
    )


_MesMiscSfpPortUsageCurrent_Type.__name__ = "Integer32"
_MesMiscSfpPortUsageCurrent_Object = MibTableColumn
mesMiscSfpPortUsageCurrent = _MesMiscSfpPortUsageCurrent_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 10, 1, 1, 27),
    _MesMiscSfpPortUsageCurrent_Type()
)
mesMiscSfpPortUsageCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesMiscSfpPortUsageCurrent.setStatus("current")


class _MesMiscSfpPortUsageNext_Type(Integer32):
    """Custom type mesMiscSfpPortUsageNext based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("external", 1),
          ("mgmtVlan", 2))
    )


_MesMiscSfpPortUsageNext_Type.__name__ = "Integer32"
_MesMiscSfpPortUsageNext_Object = MibTableColumn
mesMiscSfpPortUsageNext = _MesMiscSfpPortUsageNext_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 10, 1, 1, 28),
    _MesMiscSfpPortUsageNext_Type()
)
mesMiscSfpPortUsageNext.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mesMiscSfpPortUsageNext.setStatus("current")
_MesMiscAssociateErrorProp_Type = CommandString
_MesMiscAssociateErrorProp_Object = MibTableColumn
mesMiscAssociateErrorProp = _MesMiscAssociateErrorProp_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 10, 1, 1, 29),
    _MesMiscAssociateErrorProp_Type()
)
mesMiscAssociateErrorProp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesMiscAssociateErrorProp.setStatus("current")


class _MesMiscNoOfErpV2s_Type(Unsigned32):
    """Custom type mesMiscNoOfErpV2s based on Unsigned32"""
    defaultValue = 0


_MesMiscNoOfErpV2s_Type.__name__ = "Unsigned32"
_MesMiscNoOfErpV2s_Object = MibTableColumn
mesMiscNoOfErpV2s = _MesMiscNoOfErpV2s_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 10, 1, 1, 30),
    _MesMiscNoOfErpV2s_Type()
)
mesMiscNoOfErpV2s.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesMiscNoOfErpV2s.setStatus("current")
_MesMiscAssociateErpV2_Type = CommandString
_MesMiscAssociateErpV2_Object = MibTableColumn
mesMiscAssociateErpV2 = _MesMiscAssociateErpV2_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 10, 1, 1, 31),
    _MesMiscAssociateErpV2_Type()
)
mesMiscAssociateErpV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesMiscAssociateErpV2.setStatus("current")
_MesMiscAssociateVlanProt_Type = CommandString
_MesMiscAssociateVlanProt_Object = MibTableColumn
mesMiscAssociateVlanProt = _MesMiscAssociateVlanProt_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 10, 1, 1, 32),
    _MesMiscAssociateVlanProt_Type()
)
mesMiscAssociateVlanProt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesMiscAssociateVlanProt.setStatus("current")
_MesMiscCreateVlan_Type = CommandString
_MesMiscCreateVlan_Object = MibTableColumn
mesMiscCreateVlan = _MesMiscCreateVlan_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 10, 1, 1, 33),
    _MesMiscCreateVlan_Type()
)
mesMiscCreateVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesMiscCreateVlan.setStatus("current")


class _MesMiscEnablePtp1588_Type(Integer32):
    """Custom type mesMiscEnablePtp1588 based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_MesMiscEnablePtp1588_Type.__name__ = "Integer32"
_MesMiscEnablePtp1588_Object = MibTableColumn
mesMiscEnablePtp1588 = _MesMiscEnablePtp1588_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 10, 1, 1, 34),
    _MesMiscEnablePtp1588_Type()
)
mesMiscEnablePtp1588.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mesMiscEnablePtp1588.setStatus("current")


class _MesMiscEnableStpMgmtVlan_Type(Integer32):
    """Custom type mesMiscEnableStpMgmtVlan based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_MesMiscEnableStpMgmtVlan_Type.__name__ = "Integer32"
_MesMiscEnableStpMgmtVlan_Object = MibTableColumn
mesMiscEnableStpMgmtVlan = _MesMiscEnableStpMgmtVlan_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 10, 1, 1, 35),
    _MesMiscEnableStpMgmtVlan_Type()
)
mesMiscEnableStpMgmtVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mesMiscEnableStpMgmtVlan.setStatus("current")
_MesMiscAssociateClassAdvanced_Type = CommandString
_MesMiscAssociateClassAdvanced_Object = MibTableColumn
mesMiscAssociateClassAdvanced = _MesMiscAssociateClassAdvanced_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 10, 1, 1, 36),
    _MesMiscAssociateClassAdvanced_Type()
)
mesMiscAssociateClassAdvanced.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesMiscAssociateClassAdvanced.setStatus("current")
_MesMiscAssociateErpAdvanced_Type = CommandString
_MesMiscAssociateErpAdvanced_Object = MibTableColumn
mesMiscAssociateErpAdvanced = _MesMiscAssociateErpAdvanced_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 10, 1, 1, 37),
    _MesMiscAssociateErpAdvanced_Type()
)
mesMiscAssociateErpAdvanced.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesMiscAssociateErpAdvanced.setStatus("current")
_MesMiscAssociateMegAdvanced_Type = CommandString
_MesMiscAssociateMegAdvanced_Object = MibTableColumn
mesMiscAssociateMegAdvanced = _MesMiscAssociateMegAdvanced_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 10, 1, 1, 38),
    _MesMiscAssociateMegAdvanced_Type()
)
mesMiscAssociateMegAdvanced.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesMiscAssociateMegAdvanced.setStatus("current")
_MesMiscCreateClass_Type = CommandString
_MesMiscCreateClass_Object = MibTableColumn
mesMiscCreateClass = _MesMiscCreateClass_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 10, 1, 1, 39),
    _MesMiscCreateClass_Type()
)
mesMiscCreateClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesMiscCreateClass.setStatus("current")
_MesMiscCreateAction_Type = CommandString
_MesMiscCreateAction_Object = MibTableColumn
mesMiscCreateAction = _MesMiscCreateAction_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 10, 1, 1, 40),
    _MesMiscCreateAction_Type()
)
mesMiscCreateAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesMiscCreateAction.setStatus("current")
_MesMiscCreateMeg_Type = CommandString
_MesMiscCreateMeg_Object = MibTableColumn
mesMiscCreateMeg = _MesMiscCreateMeg_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 10, 1, 1, 41),
    _MesMiscCreateMeg_Type()
)
mesMiscCreateMeg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesMiscCreateMeg.setStatus("current")
_MesMiscCreateMep_Type = CommandString
_MesMiscCreateMep_Object = MibTableColumn
mesMiscCreateMep = _MesMiscCreateMep_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 10, 1, 1, 42),
    _MesMiscCreateMep_Type()
)
mesMiscCreateMep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesMiscCreateMep.setStatus("current")
_MesMiscCreateErrorProp_Type = CommandString
_MesMiscCreateErrorProp_Object = MibTableColumn
mesMiscCreateErrorProp = _MesMiscCreateErrorProp_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 10, 1, 1, 43),
    _MesMiscCreateErrorProp_Type()
)
mesMiscCreateErrorProp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesMiscCreateErrorProp.setStatus("current")
_MesMiscCreatePolicer_Type = CommandString
_MesMiscCreatePolicer_Object = MibTableColumn
mesMiscCreatePolicer = _MesMiscCreatePolicer_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 10, 1, 1, 44),
    _MesMiscCreatePolicer_Type()
)
mesMiscCreatePolicer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesMiscCreatePolicer.setStatus("current")
_MesMiscResendConfig_Type = CommandString
_MesMiscResendConfig_Object = MibTableColumn
mesMiscResendConfig = _MesMiscResendConfig_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 10, 1, 1, 45),
    _MesMiscResendConfig_Type()
)
mesMiscResendConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesMiscResendConfig.setStatus("current")
_MesEvcBwpMapList_ObjectIdentity = ObjectIdentity
mesEvcBwpMapList = _MesEvcBwpMapList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 11)
)
_MesEvcBwpMapTable_Object = MibTable
mesEvcBwpMapTable = _MesEvcBwpMapTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 11, 1)
)
if mibBuilder.loadTexts:
    mesEvcBwpMapTable.setStatus("obsolete")
_MesEvcBwpMapEntry_Object = MibTableRow
mesEvcBwpMapEntry = _MesEvcBwpMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 11, 1, 1)
)
mesEvcBwpMapEntry.setIndexNames(
    (0, "LUM-MES-MIB", "mesEvcBwpMapIndex"),
)
if mibBuilder.loadTexts:
    mesEvcBwpMapEntry.setStatus("current")


class _MesEvcBwpMapIndex_Type(Unsigned32):
    """Custom type mesEvcBwpMapIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_MesEvcBwpMapIndex_Type.__name__ = "Unsigned32"
_MesEvcBwpMapIndex_Object = MibTableColumn
mesEvcBwpMapIndex = _MesEvcBwpMapIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 11, 1, 1, 1),
    _MesEvcBwpMapIndex_Type()
)
mesEvcBwpMapIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesEvcBwpMapIndex.setStatus("current")
_MesEvcBwpMapName_Type = MgmtNameString
_MesEvcBwpMapName_Object = MibTableColumn
mesEvcBwpMapName = _MesEvcBwpMapName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 11, 1, 1, 2),
    _MesEvcBwpMapName_Type()
)
mesEvcBwpMapName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesEvcBwpMapName.setStatus("current")
_MesEvcBwpMapObjectProperty_Type = ObjectProperty
_MesEvcBwpMapObjectProperty_Object = MibTableColumn
mesEvcBwpMapObjectProperty = _MesEvcBwpMapObjectProperty_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 11, 1, 1, 3),
    _MesEvcBwpMapObjectProperty_Type()
)
mesEvcBwpMapObjectProperty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesEvcBwpMapObjectProperty.setStatus("current")
_MesEvcBwpMapEvcId_Type = MgmtNameString
_MesEvcBwpMapEvcId_Object = MibTableColumn
mesEvcBwpMapEvcId = _MesEvcBwpMapEvcId_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 11, 1, 1, 4),
    _MesEvcBwpMapEvcId_Type()
)
mesEvcBwpMapEvcId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesEvcBwpMapEvcId.setStatus("current")
_MesEvcBwpMapBwpId_Type = MgmtNameString
_MesEvcBwpMapBwpId_Object = MibTableColumn
mesEvcBwpMapBwpId = _MesEvcBwpMapBwpId_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 11, 1, 1, 5),
    _MesEvcBwpMapBwpId_Type()
)
mesEvcBwpMapBwpId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesEvcBwpMapBwpId.setStatus("current")


class _MesEvcBwpMapModel_Type(Integer32):
    """Custom type mesEvcBwpMapModel based on Integer32"""
    defaultValue = 3

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
          ("bwpPerUni", 2),
          ("bwpPerEvc", 3),
          ("bwpPerCos", 4))
    )


_MesEvcBwpMapModel_Type.__name__ = "Integer32"
_MesEvcBwpMapModel_Object = MibTableColumn
mesEvcBwpMapModel = _MesEvcBwpMapModel_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 11, 1, 1, 6),
    _MesEvcBwpMapModel_Type()
)
mesEvcBwpMapModel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesEvcBwpMapModel.setStatus("current")


class _MesEvcBwpMapPriority_Type(Unsigned32):
    """Custom type mesEvcBwpMapPriority based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_MesEvcBwpMapPriority_Type.__name__ = "Unsigned32"
_MesEvcBwpMapPriority_Object = MibTableColumn
mesEvcBwpMapPriority = _MesEvcBwpMapPriority_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 11, 1, 1, 7),
    _MesEvcBwpMapPriority_Type()
)
mesEvcBwpMapPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesEvcBwpMapPriority.setStatus("current")


class _MesEvcBwpMapInternalReference_Type(Unsigned32):
    """Custom type mesEvcBwpMapInternalReference based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MesEvcBwpMapInternalReference_Type.__name__ = "Unsigned32"
_MesEvcBwpMapInternalReference_Object = MibTableColumn
mesEvcBwpMapInternalReference = _MesEvcBwpMapInternalReference_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 11, 1, 1, 8),
    _MesEvcBwpMapInternalReference_Type()
)
mesEvcBwpMapInternalReference.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesEvcBwpMapInternalReference.setStatus("current")
_MesEvcBwpMapRowStatus_Type = RowStatus
_MesEvcBwpMapRowStatus_Object = MibTableColumn
mesEvcBwpMapRowStatus = _MesEvcBwpMapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 11, 1, 1, 9),
    _MesEvcBwpMapRowStatus_Type()
)
mesEvcBwpMapRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesEvcBwpMapRowStatus.setStatus("current")
_MesPortList_ObjectIdentity = ObjectIdentity
mesPortList = _MesPortList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 12)
)
_MesPortTable_Object = MibTable
mesPortTable = _MesPortTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 12, 1)
)
if mibBuilder.loadTexts:
    mesPortTable.setStatus("current")
_MesPortEntry_Object = MibTableRow
mesPortEntry = _MesPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 12, 1, 1)
)
mesPortEntry.setIndexNames(
    (0, "LUM-MES-MIB", "mesPortIndex"),
)
if mibBuilder.loadTexts:
    mesPortEntry.setStatus("current")


class _MesPortIndex_Type(Unsigned32):
    """Custom type mesPortIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_MesPortIndex_Type.__name__ = "Unsigned32"
_MesPortIndex_Object = MibTableColumn
mesPortIndex = _MesPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 12, 1, 1, 1),
    _MesPortIndex_Type()
)
mesPortIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesPortIndex.setStatus("current")
_MesPortName_Type = MgmtNameString
_MesPortName_Object = MibTableColumn
mesPortName = _MesPortName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 12, 1, 1, 2),
    _MesPortName_Type()
)
mesPortName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesPortName.setStatus("current")


class _MesPortDescr_Type(DisplayString):
    """Custom type mesPortDescr based on DisplayString"""
    defaultValue = OctetString("")


_MesPortDescr_Type.__name__ = "DisplayString"
_MesPortDescr_Object = MibTableColumn
mesPortDescr = _MesPortDescr_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 12, 1, 1, 3),
    _MesPortDescr_Type()
)
mesPortDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mesPortDescr.setStatus("current")
_MesPortSubrack_Type = SubrackNumber
_MesPortSubrack_Object = MibTableColumn
mesPortSubrack = _MesPortSubrack_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 12, 1, 1, 4),
    _MesPortSubrack_Type()
)
mesPortSubrack.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesPortSubrack.setStatus("current")
_MesPortSlot_Type = SlotNumber
_MesPortSlot_Object = MibTableColumn
mesPortSlot = _MesPortSlot_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 12, 1, 1, 5),
    _MesPortSlot_Type()
)
mesPortSlot.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesPortSlot.setStatus("current")
_MesPortTxPort_Type = PortNumber
_MesPortTxPort_Object = MibTableColumn
mesPortTxPort = _MesPortTxPort_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 12, 1, 1, 6),
    _MesPortTxPort_Type()
)
mesPortTxPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesPortTxPort.setStatus("current")
_MesPortRxPort_Type = PortNumber
_MesPortRxPort_Object = MibTableColumn
mesPortRxPort = _MesPortRxPort_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 12, 1, 1, 7),
    _MesPortRxPort_Type()
)
mesPortRxPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesPortRxPort.setStatus("current")


class _MesPortAdminStatus_Type(BoardOrInterfaceAdminStatus):
    """Custom type mesPortAdminStatus based on BoardOrInterfaceAdminStatus"""
    defaultValue = 3


_MesPortAdminStatus_Type.__name__ = "BoardOrInterfaceAdminStatus"
_MesPortAdminStatus_Object = MibTableColumn
mesPortAdminStatus = _MesPortAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 12, 1, 1, 8),
    _MesPortAdminStatus_Type()
)
mesPortAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mesPortAdminStatus.setStatus("current")


class _MesPortOperStatus_Type(BoardOrInterfaceOperStatus):
    """Custom type mesPortOperStatus based on BoardOrInterfaceOperStatus"""
    defaultValue = 3


_MesPortOperStatus_Type.__name__ = "BoardOrInterfaceOperStatus"
_MesPortOperStatus_Object = MibTableColumn
mesPortOperStatus = _MesPortOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 12, 1, 1, 9),
    _MesPortOperStatus_Type()
)
mesPortOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesPortOperStatus.setStatus("current")


class _MesPortMtuSize_Type(Unsigned32):
    """Custom type mesPortMtuSize based on Unsigned32"""
    defaultValue = 2096

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1518, 10248),
    )


_MesPortMtuSize_Type.__name__ = "Unsigned32"
_MesPortMtuSize_Object = MibTableColumn
mesPortMtuSize = _MesPortMtuSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 12, 1, 1, 10),
    _MesPortMtuSize_Type()
)
mesPortMtuSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mesPortMtuSize.setStatus("current")


class _MesPortTagType_Type(Integer32):
    """Custom type mesPortTagType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              5)
        )
    )
    namedValues = NamedValues(
        *(("qTag0x8100", 1),
          ("sTag0x88a8", 2),
          ("other", 5))
    )


_MesPortTagType_Type.__name__ = "Integer32"
_MesPortTagType_Object = MibTableColumn
mesPortTagType = _MesPortTagType_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 12, 1, 1, 11),
    _MesPortTagType_Type()
)
mesPortTagType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesPortTagType.setStatus("current")
_MesPortNoOfVlans_Type = Unsigned32
_MesPortNoOfVlans_Object = MibTableColumn
mesPortNoOfVlans = _MesPortNoOfVlans_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 12, 1, 1, 12),
    _MesPortNoOfVlans_Type()
)
mesPortNoOfVlans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesPortNoOfVlans.setStatus("current")


class _MesPortVlanAware_Type(Integer32):
    """Custom type mesPortVlanAware based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_MesPortVlanAware_Type.__name__ = "Integer32"
_MesPortVlanAware_Object = MibTableColumn
mesPortVlanAware = _MesPortVlanAware_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 12, 1, 1, 13),
    _MesPortVlanAware_Type()
)
mesPortVlanAware.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mesPortVlanAware.setStatus("current")


class _MesPortVlanTagged_Type(Integer32):
    """Custom type mesPortVlanTagged based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_MesPortVlanTagged_Type.__name__ = "Integer32"
_MesPortVlanTagged_Object = MibTableColumn
mesPortVlanTagged = _MesPortVlanTagged_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 12, 1, 1, 14),
    _MesPortVlanTagged_Type()
)
mesPortVlanTagged.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mesPortVlanTagged.setStatus("current")


class _MesPortVlanUntagged_Type(Integer32):
    """Custom type mesPortVlanUntagged based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_MesPortVlanUntagged_Type.__name__ = "Integer32"
_MesPortVlanUntagged_Object = MibTableColumn
mesPortVlanUntagged = _MesPortVlanUntagged_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 12, 1, 1, 15),
    _MesPortVlanUntagged_Type()
)
mesPortVlanUntagged.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mesPortVlanUntagged.setStatus("current")


class _MesPortIngressFiltering_Type(Integer32):
    """Custom type mesPortIngressFiltering based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_MesPortIngressFiltering_Type.__name__ = "Integer32"
_MesPortIngressFiltering_Object = MibTableColumn
mesPortIngressFiltering = _MesPortIngressFiltering_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 12, 1, 1, 16),
    _MesPortIngressFiltering_Type()
)
mesPortIngressFiltering.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mesPortIngressFiltering.setStatus("current")


class _MesPortEgressTag_Type(Integer32):
    """Custom type mesPortEgressTag based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_MesPortEgressTag_Type.__name__ = "Integer32"
_MesPortEgressTag_Object = MibTableColumn
mesPortEgressTag = _MesPortEgressTag_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 12, 1, 1, 17),
    _MesPortEgressTag_Type()
)
mesPortEgressTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mesPortEgressTag.setStatus("current")


class _MesPortDefaultCeVlanId_Type(Unsigned32):
    """Custom type mesPortDefaultCeVlanId based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_MesPortDefaultCeVlanId_Type.__name__ = "Unsigned32"
_MesPortDefaultCeVlanId_Object = MibTableColumn
mesPortDefaultCeVlanId = _MesPortDefaultCeVlanId_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 12, 1, 1, 18),
    _MesPortDefaultCeVlanId_Type()
)
mesPortDefaultCeVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mesPortDefaultCeVlanId.setStatus("current")
_MesPortAssociateVlan_Type = CommandString
_MesPortAssociateVlan_Object = MibTableColumn
mesPortAssociateVlan = _MesPortAssociateVlan_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 12, 1, 1, 19),
    _MesPortAssociateVlan_Type()
)
mesPortAssociateVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesPortAssociateVlan.setStatus("current")
_MesPortReleaseVlan_Type = CommandString
_MesPortReleaseVlan_Object = MibTableColumn
mesPortReleaseVlan = _MesPortReleaseVlan_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 12, 1, 1, 20),
    _MesPortReleaseVlan_Type()
)
mesPortReleaseVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesPortReleaseVlan.setStatus("current")


class _MesPortActingAsLine_Type(Integer32):
    """Custom type mesPortActingAsLine based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_MesPortActingAsLine_Type.__name__ = "Integer32"
_MesPortActingAsLine_Object = MibTableColumn
mesPortActingAsLine = _MesPortActingAsLine_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 12, 1, 1, 21),
    _MesPortActingAsLine_Type()
)
mesPortActingAsLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesPortActingAsLine.setStatus("current")


class _MesPortTrustedPortmask_Type(Unsigned32):
    """Custom type mesPortTrustedPortmask based on Unsigned32"""
    defaultValue = 4294967295

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MesPortTrustedPortmask_Type.__name__ = "Unsigned32"
_MesPortTrustedPortmask_Object = MibTableColumn
mesPortTrustedPortmask = _MesPortTrustedPortmask_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 12, 1, 1, 22),
    _MesPortTrustedPortmask_Type()
)
mesPortTrustedPortmask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesPortTrustedPortmask.setStatus("current")
_MesPortConfigureTrustedPortmask_Type = CommandString
_MesPortConfigureTrustedPortmask_Object = MibTableColumn
mesPortConfigureTrustedPortmask = _MesPortConfigureTrustedPortmask_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 12, 1, 1, 23),
    _MesPortConfigureTrustedPortmask_Type()
)
mesPortConfigureTrustedPortmask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesPortConfigureTrustedPortmask.setStatus("current")


class _MesPortMacAddress_Type(DisplayString):
    """Custom type mesPortMacAddress based on DisplayString"""
    defaultValue = OctetString("")


_MesPortMacAddress_Type.__name__ = "DisplayString"
_MesPortMacAddress_Object = MibTableColumn
mesPortMacAddress = _MesPortMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 12, 1, 1, 24),
    _MesPortMacAddress_Type()
)
mesPortMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesPortMacAddress.setStatus("current")


class _MesPortLagStatus_Type(Integer32):
    """Custom type mesPortLagStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noLag", 1),
          ("master", 2),
          ("slave", 3))
    )


_MesPortLagStatus_Type.__name__ = "Integer32"
_MesPortLagStatus_Object = MibTableColumn
mesPortLagStatus = _MesPortLagStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 12, 1, 1, 25),
    _MesPortLagStatus_Type()
)
mesPortLagStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesPortLagStatus.setStatus("current")


class _MesPortLagPortmask_Type(Unsigned32):
    """Custom type mesPortLagPortmask based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MesPortLagPortmask_Type.__name__ = "Unsigned32"
_MesPortLagPortmask_Object = MibTableColumn
mesPortLagPortmask = _MesPortLagPortmask_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 12, 1, 1, 26),
    _MesPortLagPortmask_Type()
)
mesPortLagPortmask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesPortLagPortmask.setStatus("current")
_MesPortAssociateLag_Type = CommandString
_MesPortAssociateLag_Object = MibTableColumn
mesPortAssociateLag = _MesPortAssociateLag_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 12, 1, 1, 27),
    _MesPortAssociateLag_Type()
)
mesPortAssociateLag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesPortAssociateLag.setStatus("current")


class _MesPortTxEthUtilization_Type(Unsigned32):
    """Custom type mesPortTxEthUtilization based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
        ValueRangeConstraint(2147483646, 2147483646),
    )


_MesPortTxEthUtilization_Type.__name__ = "Unsigned32"
_MesPortTxEthUtilization_Object = MibTableColumn
mesPortTxEthUtilization = _MesPortTxEthUtilization_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 12, 1, 1, 28),
    _MesPortTxEthUtilization_Type()
)
mesPortTxEthUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesPortTxEthUtilization.setStatus("current")


class _MesPortRxEthUtilization_Type(Unsigned32):
    """Custom type mesPortRxEthUtilization based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
        ValueRangeConstraint(2147483646, 2147483646),
    )


_MesPortRxEthUtilization_Type.__name__ = "Unsigned32"
_MesPortRxEthUtilization_Object = MibTableColumn
mesPortRxEthUtilization = _MesPortRxEthUtilization_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 12, 1, 1, 29),
    _MesPortRxEthUtilization_Type()
)
mesPortRxEthUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesPortRxEthUtilization.setStatus("current")


class _MesPortFlowControlMode_Type(Integer32):
    """Custom type mesPortFlowControlMode based on Integer32"""
    defaultValue = 1

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
        *(("noPause", 1),
          ("rxPause", 2),
          ("txPause", 3),
          ("bothPause", 4))
    )


_MesPortFlowControlMode_Type.__name__ = "Integer32"
_MesPortFlowControlMode_Object = MibTableColumn
mesPortFlowControlMode = _MesPortFlowControlMode_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 12, 1, 1, 30),
    _MesPortFlowControlMode_Type()
)
mesPortFlowControlMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mesPortFlowControlMode.setStatus("current")


class _MesPortAutoNegotiationMode_Type(Integer32):
    """Custom type mesPortAutoNegotiationMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_MesPortAutoNegotiationMode_Type.__name__ = "Integer32"
_MesPortAutoNegotiationMode_Object = MibTableColumn
mesPortAutoNegotiationMode = _MesPortAutoNegotiationMode_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 12, 1, 1, 31),
    _MesPortAutoNegotiationMode_Type()
)
mesPortAutoNegotiationMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mesPortAutoNegotiationMode.setStatus("current")


class _MesPortAutoNegotiationStatus_Type(Integer32):
    """Custom type mesPortAutoNegotiationStatus based on Integer32"""
    defaultValue = 1

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
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("incomplete", 1),
          ("halfDuplex", 2),
          ("fullDuplex", 3),
          ("halfDuplexRxPauseOn", 4),
          ("halfDuplexTxPauseOn", 5),
          ("halfDuplexRxTxPauseOn", 6),
          ("fullDuplexRxPauseOn", 7),
          ("fullDuplexTxPauseOn", 8),
          ("fullDuplexRxTxPauseOn", 9),
          ("fullDuplexFec", 10),
          ("fec", 11))
    )


_MesPortAutoNegotiationStatus_Type.__name__ = "Integer32"
_MesPortAutoNegotiationStatus_Object = MibTableColumn
mesPortAutoNegotiationStatus = _MesPortAutoNegotiationStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 12, 1, 1, 32),
    _MesPortAutoNegotiationStatus_Type()
)
mesPortAutoNegotiationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesPortAutoNegotiationStatus.setStatus("current")
_MesPortLinkDown_Type = FaultStatus
_MesPortLinkDown_Object = MibTableColumn
mesPortLinkDown = _MesPortLinkDown_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 12, 1, 1, 33),
    _MesPortLinkDown_Type()
)
mesPortLinkDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesPortLinkDown.setStatus("current")
_MesPortLinkFaultRemote_Type = FaultStatus
_MesPortLinkFaultRemote_Object = MibTableColumn
mesPortLinkFaultRemote = _MesPortLinkFaultRemote_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 12, 1, 1, 34),
    _MesPortLinkFaultRemote_Type()
)
mesPortLinkFaultRemote.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesPortLinkFaultRemote.setStatus("current")
_MesPortLinkFaultLocal_Type = FaultStatus
_MesPortLinkFaultLocal_Object = MibTableColumn
mesPortLinkFaultLocal = _MesPortLinkFaultLocal_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 12, 1, 1, 35),
    _MesPortLinkFaultLocal_Type()
)
mesPortLinkFaultLocal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesPortLinkFaultLocal.setStatus("current")


class _MesPortNoOfShapers_Type(Unsigned32):
    """Custom type mesPortNoOfShapers based on Unsigned32"""
    defaultValue = 0


_MesPortNoOfShapers_Type.__name__ = "Unsigned32"
_MesPortNoOfShapers_Object = MibTableColumn
mesPortNoOfShapers = _MesPortNoOfShapers_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 12, 1, 1, 36),
    _MesPortNoOfShapers_Type()
)
mesPortNoOfShapers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesPortNoOfShapers.setStatus("current")


class _MesPortNoOfPolicers_Type(Unsigned32):
    """Custom type mesPortNoOfPolicers based on Unsigned32"""
    defaultValue = 0


_MesPortNoOfPolicers_Type.__name__ = "Unsigned32"
_MesPortNoOfPolicers_Object = MibTableColumn
mesPortNoOfPolicers = _MesPortNoOfPolicers_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 12, 1, 1, 37),
    _MesPortNoOfPolicers_Type()
)
mesPortNoOfPolicers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesPortNoOfPolicers.setStatus("current")
_MesPortAssociateShaper_Type = CommandString
_MesPortAssociateShaper_Object = MibTableColumn
mesPortAssociateShaper = _MesPortAssociateShaper_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 12, 1, 1, 38),
    _MesPortAssociateShaper_Type()
)
mesPortAssociateShaper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesPortAssociateShaper.setStatus("current")
_MesPortReleaseShaper_Type = CommandString
_MesPortReleaseShaper_Object = MibTableColumn
mesPortReleaseShaper = _MesPortReleaseShaper_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 12, 1, 1, 39),
    _MesPortReleaseShaper_Type()
)
mesPortReleaseShaper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesPortReleaseShaper.setStatus("current")
_MesPortAssociatePolicer_Type = CommandString
_MesPortAssociatePolicer_Object = MibTableColumn
mesPortAssociatePolicer = _MesPortAssociatePolicer_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 12, 1, 1, 40),
    _MesPortAssociatePolicer_Type()
)
mesPortAssociatePolicer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesPortAssociatePolicer.setStatus("current")
_MesPortReleasePolicer_Type = CommandString
_MesPortReleasePolicer_Object = MibTableColumn
mesPortReleasePolicer = _MesPortReleasePolicer_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 12, 1, 1, 41),
    _MesPortReleasePolicer_Type()
)
mesPortReleasePolicer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesPortReleasePolicer.setStatus("current")
_MesPortRestartAutoNegotiation_Type = CommandString
_MesPortRestartAutoNegotiation_Object = MibTableColumn
mesPortRestartAutoNegotiation = _MesPortRestartAutoNegotiation_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 12, 1, 1, 42),
    _MesPortRestartAutoNegotiation_Type()
)
mesPortRestartAutoNegotiation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesPortRestartAutoNegotiation.setStatus("current")
_MesPortConfigureLine_Type = CommandString
_MesPortConfigureLine_Object = MibTableColumn
mesPortConfigureLine = _MesPortConfigureLine_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 12, 1, 1, 43),
    _MesPortConfigureLine_Type()
)
mesPortConfigureLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesPortConfigureLine.setStatus("current")


class _MesPortEtherType_Type(Unsigned32):
    """Custom type mesPortEtherType based on Unsigned32"""
    defaultValue = 33024

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MesPortEtherType_Type.__name__ = "Unsigned32"
_MesPortEtherType_Object = MibTableColumn
mesPortEtherType = _MesPortEtherType_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 12, 1, 1, 44),
    _MesPortEtherType_Type()
)
mesPortEtherType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesPortEtherType.setStatus("current")
_MesPortConfigureEtherType_Type = CommandString
_MesPortConfigureEtherType_Object = MibTableColumn
mesPortConfigureEtherType = _MesPortConfigureEtherType_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 12, 1, 1, 45),
    _MesPortConfigureEtherType_Type()
)
mesPortConfigureEtherType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesPortConfigureEtherType.setStatus("current")


class _MesPortNoOfMirrorSources_Type(Unsigned32):
    """Custom type mesPortNoOfMirrorSources based on Unsigned32"""
    defaultValue = 0


_MesPortNoOfMirrorSources_Type.__name__ = "Unsigned32"
_MesPortNoOfMirrorSources_Object = MibTableColumn
mesPortNoOfMirrorSources = _MesPortNoOfMirrorSources_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 12, 1, 1, 46),
    _MesPortNoOfMirrorSources_Type()
)
mesPortNoOfMirrorSources.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesPortNoOfMirrorSources.setStatus("current")


class _MesPortMirroring_Type(Integer32):
    """Custom type mesPortMirroring based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_MesPortMirroring_Type.__name__ = "Integer32"
_MesPortMirroring_Object = MibTableColumn
mesPortMirroring = _MesPortMirroring_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 12, 1, 1, 47),
    _MesPortMirroring_Type()
)
mesPortMirroring.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesPortMirroring.setStatus("current")


class _MesPortIngressPushTag_Type(Integer32):
    """Custom type mesPortIngressPushTag based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_MesPortIngressPushTag_Type.__name__ = "Integer32"
_MesPortIngressPushTag_Object = MibTableColumn
mesPortIngressPushTag = _MesPortIngressPushTag_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 12, 1, 1, 48),
    _MesPortIngressPushTag_Type()
)
mesPortIngressPushTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mesPortIngressPushTag.setStatus("current")


class _MesPortEgressPopTag_Type(Integer32):
    """Custom type mesPortEgressPopTag based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_MesPortEgressPopTag_Type.__name__ = "Integer32"
_MesPortEgressPopTag_Object = MibTableColumn
mesPortEgressPopTag = _MesPortEgressPopTag_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 12, 1, 1, 49),
    _MesPortEgressPopTag_Type()
)
mesPortEgressPopTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mesPortEgressPopTag.setStatus("current")


class _MesPortDefaultCeVlanPriority_Type(Unsigned32):
    """Custom type mesPortDefaultCeVlanPriority based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_MesPortDefaultCeVlanPriority_Type.__name__ = "Unsigned32"
_MesPortDefaultCeVlanPriority_Object = MibTableColumn
mesPortDefaultCeVlanPriority = _MesPortDefaultCeVlanPriority_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 12, 1, 1, 50),
    _MesPortDefaultCeVlanPriority_Type()
)
mesPortDefaultCeVlanPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mesPortDefaultCeVlanPriority.setStatus("current")
_MesPortConfigureTagRule_Type = CommandString
_MesPortConfigureTagRule_Object = MibTableColumn
mesPortConfigureTagRule = _MesPortConfigureTagRule_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 12, 1, 1, 51),
    _MesPortConfigureTagRule_Type()
)
mesPortConfigureTagRule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesPortConfigureTagRule.setStatus("current")


class _MesPortCosProfile_Type(Integer32):
    """Custom type mesPortCosProfile based on Integer32"""
    defaultValue = 1

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
        *(("profile1", 1),
          ("profile2", 2),
          ("profile3", 3),
          ("profile4", 4))
    )


_MesPortCosProfile_Type.__name__ = "Integer32"
_MesPortCosProfile_Object = MibTableColumn
mesPortCosProfile = _MesPortCosProfile_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 12, 1, 1, 52),
    _MesPortCosProfile_Type()
)
mesPortCosProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mesPortCosProfile.setStatus("current")


class _MesPortMode_Type(Integer32):
    """Custom type mesPortMode based on Integer32"""
    defaultValue = 3

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
        *(("uni", 1),
          ("uniMux", 2),
          ("nni", 3),
          ("userDefined", 4))
    )


_MesPortMode_Type.__name__ = "Integer32"
_MesPortMode_Object = MibTableColumn
mesPortMode = _MesPortMode_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 12, 1, 1, 53),
    _MesPortMode_Type()
)
mesPortMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mesPortMode.setStatus("current")


class _MesPortPrioAssignment_Type(Integer32):
    """Custom type mesPortPrioAssignment based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("set", 1),
          ("copy", 2))
    )


_MesPortPrioAssignment_Type.__name__ = "Integer32"
_MesPortPrioAssignment_Object = MibTableColumn
mesPortPrioAssignment = _MesPortPrioAssignment_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 12, 1, 1, 54),
    _MesPortPrioAssignment_Type()
)
mesPortPrioAssignment.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesPortPrioAssignment.setStatus("current")
_MesPortConfigurePrioAssignment_Type = CommandString
_MesPortConfigurePrioAssignment_Object = MibTableColumn
mesPortConfigurePrioAssignment = _MesPortConfigurePrioAssignment_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 12, 1, 1, 55),
    _MesPortConfigurePrioAssignment_Type()
)
mesPortConfigurePrioAssignment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesPortConfigurePrioAssignment.setStatus("current")
_MesPortNoOfTagRules_Type = Unsigned32
_MesPortNoOfTagRules_Object = MibTableColumn
mesPortNoOfTagRules = _MesPortNoOfTagRules_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 12, 1, 1, 56),
    _MesPortNoOfTagRules_Type()
)
mesPortNoOfTagRules.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesPortNoOfTagRules.setStatus("current")
_MesPortNoOfVlanSchedPrios_Type = Unsigned32
_MesPortNoOfVlanSchedPrios_Object = MibTableColumn
mesPortNoOfVlanSchedPrios = _MesPortNoOfVlanSchedPrios_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 12, 1, 1, 57),
    _MesPortNoOfVlanSchedPrios_Type()
)
mesPortNoOfVlanSchedPrios.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesPortNoOfVlanSchedPrios.setStatus("deprecated")
_MesPortObjectProperty_Type = ObjectProperty
_MesPortObjectProperty_Object = MibTableColumn
mesPortObjectProperty = _MesPortObjectProperty_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 12, 1, 1, 58),
    _MesPortObjectProperty_Type()
)
mesPortObjectProperty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesPortObjectProperty.setStatus("current")
_MesPortHighBitErrorRate_Type = FaultStatus
_MesPortHighBitErrorRate_Object = MibTableColumn
mesPortHighBitErrorRate = _MesPortHighBitErrorRate_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 12, 1, 1, 59),
    _MesPortHighBitErrorRate_Type()
)
mesPortHighBitErrorRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesPortHighBitErrorRate.setStatus("current")


class _MesPortIdx_Type(Integer32):
    """Custom type mesPortIdx based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_MesPortIdx_Type.__name__ = "Integer32"
_MesPortIdx_Object = MibTableColumn
mesPortIdx = _MesPortIdx_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 12, 1, 1, 60),
    _MesPortIdx_Type()
)
mesPortIdx.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesPortIdx.setStatus("current")


class _MesPortIfNo_Type(PortNumber):
    """Custom type mesPortIfNo based on PortNumber"""
    defaultValue = 1


_MesPortIfNo_Type.__name__ = "PortNumber"
_MesPortIfNo_Object = MibTableColumn
mesPortIfNo = _MesPortIfNo_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 12, 1, 1, 61),
    _MesPortIfNo_Type()
)
mesPortIfNo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesPortIfNo.setStatus("current")


class _MesPortClientIdx_Type(Integer32):
    """Custom type mesPortClientIdx based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_MesPortClientIdx_Type.__name__ = "Integer32"
_MesPortClientIdx_Object = MibTableColumn
mesPortClientIdx = _MesPortClientIdx_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 12, 1, 1, 62),
    _MesPortClientIdx_Type()
)
mesPortClientIdx.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesPortClientIdx.setStatus("current")


class _MesPortUpPortId_Type(Integer32):
    """Custom type mesPortUpPortId based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_MesPortUpPortId_Type.__name__ = "Integer32"
_MesPortUpPortId_Object = MibTableColumn
mesPortUpPortId = _MesPortUpPortId_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 12, 1, 1, 63),
    _MesPortUpPortId_Type()
)
mesPortUpPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesPortUpPortId.setStatus("current")


class _MesPortLagPortmaskIf1_Type(Unsigned32):
    """Custom type mesPortLagPortmaskIf1 based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MesPortLagPortmaskIf1_Type.__name__ = "Unsigned32"
_MesPortLagPortmaskIf1_Object = MibTableColumn
mesPortLagPortmaskIf1 = _MesPortLagPortmaskIf1_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 12, 1, 1, 64),
    _MesPortLagPortmaskIf1_Type()
)
mesPortLagPortmaskIf1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesPortLagPortmaskIf1.setStatus("current")


class _MesPortLagPortmaskIf2_Type(Unsigned32):
    """Custom type mesPortLagPortmaskIf2 based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MesPortLagPortmaskIf2_Type.__name__ = "Unsigned32"
_MesPortLagPortmaskIf2_Object = MibTableColumn
mesPortLagPortmaskIf2 = _MesPortLagPortmaskIf2_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 12, 1, 1, 65),
    _MesPortLagPortmaskIf2_Type()
)
mesPortLagPortmaskIf2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesPortLagPortmaskIf2.setStatus("current")


class _MesPortLagPortmaskIf3_Type(Unsigned32):
    """Custom type mesPortLagPortmaskIf3 based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MesPortLagPortmaskIf3_Type.__name__ = "Unsigned32"
_MesPortLagPortmaskIf3_Object = MibTableColumn
mesPortLagPortmaskIf3 = _MesPortLagPortmaskIf3_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 12, 1, 1, 66),
    _MesPortLagPortmaskIf3_Type()
)
mesPortLagPortmaskIf3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesPortLagPortmaskIf3.setStatus("current")


class _MesPortLagPortmaskIf4_Type(Unsigned32):
    """Custom type mesPortLagPortmaskIf4 based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MesPortLagPortmaskIf4_Type.__name__ = "Unsigned32"
_MesPortLagPortmaskIf4_Object = MibTableColumn
mesPortLagPortmaskIf4 = _MesPortLagPortmaskIf4_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 12, 1, 1, 67),
    _MesPortLagPortmaskIf4_Type()
)
mesPortLagPortmaskIf4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesPortLagPortmaskIf4.setStatus("current")


class _MesPortLagPortmaskIf5_Type(Unsigned32):
    """Custom type mesPortLagPortmaskIf5 based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MesPortLagPortmaskIf5_Type.__name__ = "Unsigned32"
_MesPortLagPortmaskIf5_Object = MibTableColumn
mesPortLagPortmaskIf5 = _MesPortLagPortmaskIf5_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 12, 1, 1, 68),
    _MesPortLagPortmaskIf5_Type()
)
mesPortLagPortmaskIf5.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesPortLagPortmaskIf5.setStatus("current")


class _MesPortLagPortmaskIf6_Type(Unsigned32):
    """Custom type mesPortLagPortmaskIf6 based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MesPortLagPortmaskIf6_Type.__name__ = "Unsigned32"
_MesPortLagPortmaskIf6_Object = MibTableColumn
mesPortLagPortmaskIf6 = _MesPortLagPortmaskIf6_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 12, 1, 1, 69),
    _MesPortLagPortmaskIf6_Type()
)
mesPortLagPortmaskIf6.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesPortLagPortmaskIf6.setStatus("current")


class _MesPortLagPortmaskIf7_Type(Unsigned32):
    """Custom type mesPortLagPortmaskIf7 based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MesPortLagPortmaskIf7_Type.__name__ = "Unsigned32"
_MesPortLagPortmaskIf7_Object = MibTableColumn
mesPortLagPortmaskIf7 = _MesPortLagPortmaskIf7_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 12, 1, 1, 70),
    _MesPortLagPortmaskIf7_Type()
)
mesPortLagPortmaskIf7.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesPortLagPortmaskIf7.setStatus("current")


class _MesPortLagPortmaskIf8_Type(Unsigned32):
    """Custom type mesPortLagPortmaskIf8 based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MesPortLagPortmaskIf8_Type.__name__ = "Unsigned32"
_MesPortLagPortmaskIf8_Object = MibTableColumn
mesPortLagPortmaskIf8 = _MesPortLagPortmaskIf8_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 12, 1, 1, 71),
    _MesPortLagPortmaskIf8_Type()
)
mesPortLagPortmaskIf8.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesPortLagPortmaskIf8.setStatus("current")


class _MesPortAutoNegMasterSlaveCfg_Type(Integer32):
    """Custom type mesPortAutoNegMasterSlaveCfg based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 0),
          ("master", 1),
          ("slave", 2))
    )


_MesPortAutoNegMasterSlaveCfg_Type.__name__ = "Integer32"
_MesPortAutoNegMasterSlaveCfg_Object = MibTableColumn
mesPortAutoNegMasterSlaveCfg = _MesPortAutoNegMasterSlaveCfg_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 12, 1, 1, 72),
    _MesPortAutoNegMasterSlaveCfg_Type()
)
mesPortAutoNegMasterSlaveCfg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mesPortAutoNegMasterSlaveCfg.setStatus("current")


class _MesPortAutoNegMasterSlaveStatus_Type(Integer32):
    """Custom type mesPortAutoNegMasterSlaveStatus based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("master", 1),
          ("slave", 2))
    )


_MesPortAutoNegMasterSlaveStatus_Type.__name__ = "Integer32"
_MesPortAutoNegMasterSlaveStatus_Object = MibTableColumn
mesPortAutoNegMasterSlaveStatus = _MesPortAutoNegMasterSlaveStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 12, 1, 1, 73),
    _MesPortAutoNegMasterSlaveStatus_Type()
)
mesPortAutoNegMasterSlaveStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesPortAutoNegMasterSlaveStatus.setStatus("current")


class _MesPortLagPortmaskIf9_Type(Unsigned32):
    """Custom type mesPortLagPortmaskIf9 based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MesPortLagPortmaskIf9_Type.__name__ = "Unsigned32"
_MesPortLagPortmaskIf9_Object = MibTableColumn
mesPortLagPortmaskIf9 = _MesPortLagPortmaskIf9_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 12, 1, 1, 74),
    _MesPortLagPortmaskIf9_Type()
)
mesPortLagPortmaskIf9.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesPortLagPortmaskIf9.setStatus("current")


class _MesPortLagPortmaskIf10_Type(Unsigned32):
    """Custom type mesPortLagPortmaskIf10 based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MesPortLagPortmaskIf10_Type.__name__ = "Unsigned32"
_MesPortLagPortmaskIf10_Object = MibTableColumn
mesPortLagPortmaskIf10 = _MesPortLagPortmaskIf10_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 12, 1, 1, 75),
    _MesPortLagPortmaskIf10_Type()
)
mesPortLagPortmaskIf10.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesPortLagPortmaskIf10.setStatus("current")


class _MesPortLagPortmaskIf11_Type(Unsigned32):
    """Custom type mesPortLagPortmaskIf11 based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MesPortLagPortmaskIf11_Type.__name__ = "Unsigned32"
_MesPortLagPortmaskIf11_Object = MibTableColumn
mesPortLagPortmaskIf11 = _MesPortLagPortmaskIf11_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 12, 1, 1, 76),
    _MesPortLagPortmaskIf11_Type()
)
mesPortLagPortmaskIf11.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesPortLagPortmaskIf11.setStatus("current")


class _MesPortLagPortmaskIf12_Type(Unsigned32):
    """Custom type mesPortLagPortmaskIf12 based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MesPortLagPortmaskIf12_Type.__name__ = "Unsigned32"
_MesPortLagPortmaskIf12_Object = MibTableColumn
mesPortLagPortmaskIf12 = _MesPortLagPortmaskIf12_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 12, 1, 1, 77),
    _MesPortLagPortmaskIf12_Type()
)
mesPortLagPortmaskIf12.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesPortLagPortmaskIf12.setStatus("current")


class _MesPortLagPortmaskIf13_Type(Unsigned32):
    """Custom type mesPortLagPortmaskIf13 based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MesPortLagPortmaskIf13_Type.__name__ = "Unsigned32"
_MesPortLagPortmaskIf13_Object = MibTableColumn
mesPortLagPortmaskIf13 = _MesPortLagPortmaskIf13_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 12, 1, 1, 78),
    _MesPortLagPortmaskIf13_Type()
)
mesPortLagPortmaskIf13.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesPortLagPortmaskIf13.setStatus("current")


class _MesPortLagPortmaskIf14_Type(Unsigned32):
    """Custom type mesPortLagPortmaskIf14 based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MesPortLagPortmaskIf14_Type.__name__ = "Unsigned32"
_MesPortLagPortmaskIf14_Object = MibTableColumn
mesPortLagPortmaskIf14 = _MesPortLagPortmaskIf14_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 12, 1, 1, 79),
    _MesPortLagPortmaskIf14_Type()
)
mesPortLagPortmaskIf14.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesPortLagPortmaskIf14.setStatus("current")


class _MesPortLagPortmaskIf15_Type(Unsigned32):
    """Custom type mesPortLagPortmaskIf15 based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MesPortLagPortmaskIf15_Type.__name__ = "Unsigned32"
_MesPortLagPortmaskIf15_Object = MibTableColumn
mesPortLagPortmaskIf15 = _MesPortLagPortmaskIf15_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 12, 1, 1, 80),
    _MesPortLagPortmaskIf15_Type()
)
mesPortLagPortmaskIf15.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesPortLagPortmaskIf15.setStatus("current")


class _MesPortLagPortmaskIf16_Type(Unsigned32):
    """Custom type mesPortLagPortmaskIf16 based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MesPortLagPortmaskIf16_Type.__name__ = "Unsigned32"
_MesPortLagPortmaskIf16_Object = MibTableColumn
mesPortLagPortmaskIf16 = _MesPortLagPortmaskIf16_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 12, 1, 1, 81),
    _MesPortLagPortmaskIf16_Type()
)
mesPortLagPortmaskIf16.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesPortLagPortmaskIf16.setStatus("current")
_MesPortCreateVlanTagClass_Type = CommandString
_MesPortCreateVlanTagClass_Object = MibTableColumn
mesPortCreateVlanTagClass = _MesPortCreateVlanTagClass_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 12, 1, 1, 82),
    _MesPortCreateVlanTagClass_Type()
)
mesPortCreateVlanTagClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesPortCreateVlanTagClass.setStatus("current")
_MesPortCreateTagRuleWoutClass_Type = CommandString
_MesPortCreateTagRuleWoutClass_Object = MibTableColumn
mesPortCreateTagRuleWoutClass = _MesPortCreateTagRuleWoutClass_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 12, 1, 1, 83),
    _MesPortCreateTagRuleWoutClass_Type()
)
mesPortCreateTagRuleWoutClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesPortCreateTagRuleWoutClass.setStatus("current")


class _MesPortTrustedPortmaskIf2_Type(Unsigned32):
    """Custom type mesPortTrustedPortmaskIf2 based on Unsigned32"""
    defaultValue = 4294967295

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MesPortTrustedPortmaskIf2_Type.__name__ = "Unsigned32"
_MesPortTrustedPortmaskIf2_Object = MibTableColumn
mesPortTrustedPortmaskIf2 = _MesPortTrustedPortmaskIf2_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 12, 1, 1, 84),
    _MesPortTrustedPortmaskIf2_Type()
)
mesPortTrustedPortmaskIf2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesPortTrustedPortmaskIf2.setStatus("current")


class _MesPortTrustedPortmaskIf3_Type(Unsigned32):
    """Custom type mesPortTrustedPortmaskIf3 based on Unsigned32"""
    defaultValue = 4294967295

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MesPortTrustedPortmaskIf3_Type.__name__ = "Unsigned32"
_MesPortTrustedPortmaskIf3_Object = MibTableColumn
mesPortTrustedPortmaskIf3 = _MesPortTrustedPortmaskIf3_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 12, 1, 1, 85),
    _MesPortTrustedPortmaskIf3_Type()
)
mesPortTrustedPortmaskIf3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesPortTrustedPortmaskIf3.setStatus("current")


class _MesPortTrustedPortmaskIf4_Type(Unsigned32):
    """Custom type mesPortTrustedPortmaskIf4 based on Unsigned32"""
    defaultValue = 4294967295

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MesPortTrustedPortmaskIf4_Type.__name__ = "Unsigned32"
_MesPortTrustedPortmaskIf4_Object = MibTableColumn
mesPortTrustedPortmaskIf4 = _MesPortTrustedPortmaskIf4_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 12, 1, 1, 86),
    _MesPortTrustedPortmaskIf4_Type()
)
mesPortTrustedPortmaskIf4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesPortTrustedPortmaskIf4.setStatus("current")


class _MesPortTrustedPortmaskIf5_Type(Unsigned32):
    """Custom type mesPortTrustedPortmaskIf5 based on Unsigned32"""
    defaultValue = 4294967295

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MesPortTrustedPortmaskIf5_Type.__name__ = "Unsigned32"
_MesPortTrustedPortmaskIf5_Object = MibTableColumn
mesPortTrustedPortmaskIf5 = _MesPortTrustedPortmaskIf5_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 12, 1, 1, 87),
    _MesPortTrustedPortmaskIf5_Type()
)
mesPortTrustedPortmaskIf5.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesPortTrustedPortmaskIf5.setStatus("current")


class _MesPortTrustedPortmaskIf6_Type(Unsigned32):
    """Custom type mesPortTrustedPortmaskIf6 based on Unsigned32"""
    defaultValue = 4294967295

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MesPortTrustedPortmaskIf6_Type.__name__ = "Unsigned32"
_MesPortTrustedPortmaskIf6_Object = MibTableColumn
mesPortTrustedPortmaskIf6 = _MesPortTrustedPortmaskIf6_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 12, 1, 1, 88),
    _MesPortTrustedPortmaskIf6_Type()
)
mesPortTrustedPortmaskIf6.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesPortTrustedPortmaskIf6.setStatus("current")


class _MesPortTrustedPortmaskIf7_Type(Unsigned32):
    """Custom type mesPortTrustedPortmaskIf7 based on Unsigned32"""
    defaultValue = 4294967295

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MesPortTrustedPortmaskIf7_Type.__name__ = "Unsigned32"
_MesPortTrustedPortmaskIf7_Object = MibTableColumn
mesPortTrustedPortmaskIf7 = _MesPortTrustedPortmaskIf7_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 12, 1, 1, 89),
    _MesPortTrustedPortmaskIf7_Type()
)
mesPortTrustedPortmaskIf7.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesPortTrustedPortmaskIf7.setStatus("current")


class _MesPortTrustedPortmaskIf8_Type(Unsigned32):
    """Custom type mesPortTrustedPortmaskIf8 based on Unsigned32"""
    defaultValue = 4294967295

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MesPortTrustedPortmaskIf8_Type.__name__ = "Unsigned32"
_MesPortTrustedPortmaskIf8_Object = MibTableColumn
mesPortTrustedPortmaskIf8 = _MesPortTrustedPortmaskIf8_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 12, 1, 1, 90),
    _MesPortTrustedPortmaskIf8_Type()
)
mesPortTrustedPortmaskIf8.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesPortTrustedPortmaskIf8.setStatus("current")


class _MesPortTrustedPortmaskIf9_Type(Unsigned32):
    """Custom type mesPortTrustedPortmaskIf9 based on Unsigned32"""
    defaultValue = 4294967295

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MesPortTrustedPortmaskIf9_Type.__name__ = "Unsigned32"
_MesPortTrustedPortmaskIf9_Object = MibTableColumn
mesPortTrustedPortmaskIf9 = _MesPortTrustedPortmaskIf9_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 12, 1, 1, 91),
    _MesPortTrustedPortmaskIf9_Type()
)
mesPortTrustedPortmaskIf9.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesPortTrustedPortmaskIf9.setStatus("current")


class _MesPortTrustedPortmaskIf10_Type(Unsigned32):
    """Custom type mesPortTrustedPortmaskIf10 based on Unsigned32"""
    defaultValue = 4294967295

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MesPortTrustedPortmaskIf10_Type.__name__ = "Unsigned32"
_MesPortTrustedPortmaskIf10_Object = MibTableColumn
mesPortTrustedPortmaskIf10 = _MesPortTrustedPortmaskIf10_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 12, 1, 1, 92),
    _MesPortTrustedPortmaskIf10_Type()
)
mesPortTrustedPortmaskIf10.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesPortTrustedPortmaskIf10.setStatus("current")


class _MesPortTrustedPortmaskIf11_Type(Unsigned32):
    """Custom type mesPortTrustedPortmaskIf11 based on Unsigned32"""
    defaultValue = 4294967295

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MesPortTrustedPortmaskIf11_Type.__name__ = "Unsigned32"
_MesPortTrustedPortmaskIf11_Object = MibTableColumn
mesPortTrustedPortmaskIf11 = _MesPortTrustedPortmaskIf11_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 12, 1, 1, 93),
    _MesPortTrustedPortmaskIf11_Type()
)
mesPortTrustedPortmaskIf11.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesPortTrustedPortmaskIf11.setStatus("current")


class _MesPortTrustedPortmaskIf12_Type(Unsigned32):
    """Custom type mesPortTrustedPortmaskIf12 based on Unsigned32"""
    defaultValue = 4294967295

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MesPortTrustedPortmaskIf12_Type.__name__ = "Unsigned32"
_MesPortTrustedPortmaskIf12_Object = MibTableColumn
mesPortTrustedPortmaskIf12 = _MesPortTrustedPortmaskIf12_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 12, 1, 1, 94),
    _MesPortTrustedPortmaskIf12_Type()
)
mesPortTrustedPortmaskIf12.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesPortTrustedPortmaskIf12.setStatus("current")


class _MesPortTrustedPortmaskIf13_Type(Unsigned32):
    """Custom type mesPortTrustedPortmaskIf13 based on Unsigned32"""
    defaultValue = 4294967295

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MesPortTrustedPortmaskIf13_Type.__name__ = "Unsigned32"
_MesPortTrustedPortmaskIf13_Object = MibTableColumn
mesPortTrustedPortmaskIf13 = _MesPortTrustedPortmaskIf13_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 12, 1, 1, 95),
    _MesPortTrustedPortmaskIf13_Type()
)
mesPortTrustedPortmaskIf13.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesPortTrustedPortmaskIf13.setStatus("current")


class _MesPortTrustedPortmaskIf14_Type(Unsigned32):
    """Custom type mesPortTrustedPortmaskIf14 based on Unsigned32"""
    defaultValue = 4294967295

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MesPortTrustedPortmaskIf14_Type.__name__ = "Unsigned32"
_MesPortTrustedPortmaskIf14_Object = MibTableColumn
mesPortTrustedPortmaskIf14 = _MesPortTrustedPortmaskIf14_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 12, 1, 1, 96),
    _MesPortTrustedPortmaskIf14_Type()
)
mesPortTrustedPortmaskIf14.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesPortTrustedPortmaskIf14.setStatus("current")


class _MesPortTrustedPortmaskIf15_Type(Unsigned32):
    """Custom type mesPortTrustedPortmaskIf15 based on Unsigned32"""
    defaultValue = 4294967295

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MesPortTrustedPortmaskIf15_Type.__name__ = "Unsigned32"
_MesPortTrustedPortmaskIf15_Object = MibTableColumn
mesPortTrustedPortmaskIf15 = _MesPortTrustedPortmaskIf15_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 12, 1, 1, 97),
    _MesPortTrustedPortmaskIf15_Type()
)
mesPortTrustedPortmaskIf15.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesPortTrustedPortmaskIf15.setStatus("current")


class _MesPortTrustedPortmaskIf16_Type(Unsigned32):
    """Custom type mesPortTrustedPortmaskIf16 based on Unsigned32"""
    defaultValue = 4294967295

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MesPortTrustedPortmaskIf16_Type.__name__ = "Unsigned32"
_MesPortTrustedPortmaskIf16_Object = MibTableColumn
mesPortTrustedPortmaskIf16 = _MesPortTrustedPortmaskIf16_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 12, 1, 1, 98),
    _MesPortTrustedPortmaskIf16_Type()
)
mesPortTrustedPortmaskIf16.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesPortTrustedPortmaskIf16.setStatus("current")


class _MesPortServiceId_Type(ServiceIdWithNotUsed):
    """Custom type mesPortServiceId based on ServiceIdWithNotUsed"""
    defaultValue = -1


_MesPortServiceId_Type.__name__ = "ServiceIdWithNotUsed"
_MesPortServiceId_Object = MibTableColumn
mesPortServiceId = _MesPortServiceId_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 12, 1, 1, 99),
    _MesPortServiceId_Type()
)
mesPortServiceId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mesPortServiceId.setStatus("current")
_MesVlanMapList_ObjectIdentity = ObjectIdentity
mesVlanMapList = _MesVlanMapList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 13)
)
_MesVlanMapTable_Object = MibTable
mesVlanMapTable = _MesVlanMapTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 13, 1)
)
if mibBuilder.loadTexts:
    mesVlanMapTable.setStatus("current")
_MesVlanMapEntry_Object = MibTableRow
mesVlanMapEntry = _MesVlanMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 13, 1, 1)
)
mesVlanMapEntry.setIndexNames(
    (0, "LUM-MES-MIB", "mesVlanMapIndex"),
)
if mibBuilder.loadTexts:
    mesVlanMapEntry.setStatus("current")


class _MesVlanMapIndex_Type(Unsigned32):
    """Custom type mesVlanMapIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_MesVlanMapIndex_Type.__name__ = "Unsigned32"
_MesVlanMapIndex_Object = MibTableColumn
mesVlanMapIndex = _MesVlanMapIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 13, 1, 1, 1),
    _MesVlanMapIndex_Type()
)
mesVlanMapIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesVlanMapIndex.setStatus("current")
_MesVlanMapName_Type = MgmtNameString
_MesVlanMapName_Object = MibTableColumn
mesVlanMapName = _MesVlanMapName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 13, 1, 1, 2),
    _MesVlanMapName_Type()
)
mesVlanMapName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesVlanMapName.setStatus("current")


class _MesVlanMapVlanIdRangeLower_Type(Unsigned32):
    """Custom type mesVlanMapVlanIdRangeLower based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_MesVlanMapVlanIdRangeLower_Type.__name__ = "Unsigned32"
_MesVlanMapVlanIdRangeLower_Object = MibTableColumn
mesVlanMapVlanIdRangeLower = _MesVlanMapVlanIdRangeLower_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 13, 1, 1, 3),
    _MesVlanMapVlanIdRangeLower_Type()
)
mesVlanMapVlanIdRangeLower.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesVlanMapVlanIdRangeLower.setStatus("current")


class _MesVlanMapVlanIdRangeUpper_Type(Unsigned32):
    """Custom type mesVlanMapVlanIdRangeUpper based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_MesVlanMapVlanIdRangeUpper_Type.__name__ = "Unsigned32"
_MesVlanMapVlanIdRangeUpper_Object = MibTableColumn
mesVlanMapVlanIdRangeUpper = _MesVlanMapVlanIdRangeUpper_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 13, 1, 1, 4),
    _MesVlanMapVlanIdRangeUpper_Type()
)
mesVlanMapVlanIdRangeUpper.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesVlanMapVlanIdRangeUpper.setStatus("current")


class _MesVlanMapInternalReference_Type(Unsigned32):
    """Custom type mesVlanMapInternalReference based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MesVlanMapInternalReference_Type.__name__ = "Unsigned32"
_MesVlanMapInternalReference_Object = MibTableColumn
mesVlanMapInternalReference = _MesVlanMapInternalReference_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 13, 1, 1, 5),
    _MesVlanMapInternalReference_Type()
)
mesVlanMapInternalReference.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesVlanMapInternalReference.setStatus("current")


class _MesVlanMapPortmask_Type(Unsigned32):
    """Custom type mesVlanMapPortmask based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MesVlanMapPortmask_Type.__name__ = "Unsigned32"
_MesVlanMapPortmask_Object = MibTableColumn
mesVlanMapPortmask = _MesVlanMapPortmask_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 13, 1, 1, 6),
    _MesVlanMapPortmask_Type()
)
mesVlanMapPortmask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesVlanMapPortmask.setStatus("current")
_MesVlanMapConfigurePortMask_Type = CommandString
_MesVlanMapConfigurePortMask_Object = MibTableColumn
mesVlanMapConfigurePortMask = _MesVlanMapConfigurePortMask_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 13, 1, 1, 7),
    _MesVlanMapConfigurePortMask_Type()
)
mesVlanMapConfigurePortMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesVlanMapConfigurePortMask.setStatus("current")


class _MesVlanMapLearning_Type(Integer32):
    """Custom type mesVlanMapLearning based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_MesVlanMapLearning_Type.__name__ = "Integer32"
_MesVlanMapLearning_Object = MibTableColumn
mesVlanMapLearning = _MesVlanMapLearning_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 13, 1, 1, 8),
    _MesVlanMapLearning_Type()
)
mesVlanMapLearning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mesVlanMapLearning.setStatus("current")


class _MesVlanMapEtherType_Type(Integer32):
    """Custom type mesVlanMapEtherType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("qTag0x8100", 1),
          ("sTag0x88a8", 2))
    )


_MesVlanMapEtherType_Type.__name__ = "Integer32"
_MesVlanMapEtherType_Object = MibTableColumn
mesVlanMapEtherType = _MesVlanMapEtherType_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 13, 1, 1, 9),
    _MesVlanMapEtherType_Type()
)
mesVlanMapEtherType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mesVlanMapEtherType.setStatus("current")
_MesVlanMapRowStatus_Type = RowStatus
_MesVlanMapRowStatus_Object = MibTableColumn
mesVlanMapRowStatus = _MesVlanMapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 13, 1, 1, 10),
    _MesVlanMapRowStatus_Type()
)
mesVlanMapRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesVlanMapRowStatus.setStatus("current")


class _MesVlanMapDescr_Type(DisplayString):
    """Custom type mesVlanMapDescr based on DisplayString"""
    defaultValue = OctetString("")


_MesVlanMapDescr_Type.__name__ = "DisplayString"
_MesVlanMapDescr_Object = MibTableColumn
mesVlanMapDescr = _MesVlanMapDescr_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 13, 1, 1, 11),
    _MesVlanMapDescr_Type()
)
mesVlanMapDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mesVlanMapDescr.setStatus("current")
_MesVlanMapTrustPorts_Type = CommandString
_MesVlanMapTrustPorts_Object = MibTableColumn
mesVlanMapTrustPorts = _MesVlanMapTrustPorts_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 13, 1, 1, 12),
    _MesVlanMapTrustPorts_Type()
)
mesVlanMapTrustPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesVlanMapTrustPorts.setStatus("current")


class _MesVlanMapRings_Type(Counter64):
    """Custom type mesVlanMapRings based on Counter64"""
    defaultValue = 0


_MesVlanMapRings_Type.__name__ = "Counter64"
_MesVlanMapRings_Object = MibTableColumn
mesVlanMapRings = _MesVlanMapRings_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 13, 1, 1, 13),
    _MesVlanMapRings_Type()
)
mesVlanMapRings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesVlanMapRings.setStatus("current")


class _MesVlanMapServiceId_Type(ServiceIdWithNotUsed):
    """Custom type mesVlanMapServiceId based on ServiceIdWithNotUsed"""
    defaultValue = -1


_MesVlanMapServiceId_Type.__name__ = "ServiceIdWithNotUsed"
_MesVlanMapServiceId_Object = MibTableColumn
mesVlanMapServiceId = _MesVlanMapServiceId_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 13, 1, 1, 14),
    _MesVlanMapServiceId_Type()
)
mesVlanMapServiceId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mesVlanMapServiceId.setStatus("current")


class _MesVlanMapPortmaskIf1_Type(Unsigned32):
    """Custom type mesVlanMapPortmaskIf1 based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MesVlanMapPortmaskIf1_Type.__name__ = "Unsigned32"
_MesVlanMapPortmaskIf1_Object = MibTableColumn
mesVlanMapPortmaskIf1 = _MesVlanMapPortmaskIf1_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 13, 1, 1, 15),
    _MesVlanMapPortmaskIf1_Type()
)
mesVlanMapPortmaskIf1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesVlanMapPortmaskIf1.setStatus("current")


class _MesVlanMapPortmaskIf2_Type(Unsigned32):
    """Custom type mesVlanMapPortmaskIf2 based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MesVlanMapPortmaskIf2_Type.__name__ = "Unsigned32"
_MesVlanMapPortmaskIf2_Object = MibTableColumn
mesVlanMapPortmaskIf2 = _MesVlanMapPortmaskIf2_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 13, 1, 1, 16),
    _MesVlanMapPortmaskIf2_Type()
)
mesVlanMapPortmaskIf2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesVlanMapPortmaskIf2.setStatus("current")


class _MesVlanMapPortmaskIf3_Type(Unsigned32):
    """Custom type mesVlanMapPortmaskIf3 based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MesVlanMapPortmaskIf3_Type.__name__ = "Unsigned32"
_MesVlanMapPortmaskIf3_Object = MibTableColumn
mesVlanMapPortmaskIf3 = _MesVlanMapPortmaskIf3_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 13, 1, 1, 17),
    _MesVlanMapPortmaskIf3_Type()
)
mesVlanMapPortmaskIf3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesVlanMapPortmaskIf3.setStatus("current")


class _MesVlanMapPortmaskIf4_Type(Unsigned32):
    """Custom type mesVlanMapPortmaskIf4 based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MesVlanMapPortmaskIf4_Type.__name__ = "Unsigned32"
_MesVlanMapPortmaskIf4_Object = MibTableColumn
mesVlanMapPortmaskIf4 = _MesVlanMapPortmaskIf4_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 13, 1, 1, 18),
    _MesVlanMapPortmaskIf4_Type()
)
mesVlanMapPortmaskIf4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesVlanMapPortmaskIf4.setStatus("current")


class _MesVlanMapPortmaskIf5_Type(Unsigned32):
    """Custom type mesVlanMapPortmaskIf5 based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MesVlanMapPortmaskIf5_Type.__name__ = "Unsigned32"
_MesVlanMapPortmaskIf5_Object = MibTableColumn
mesVlanMapPortmaskIf5 = _MesVlanMapPortmaskIf5_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 13, 1, 1, 19),
    _MesVlanMapPortmaskIf5_Type()
)
mesVlanMapPortmaskIf5.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesVlanMapPortmaskIf5.setStatus("current")


class _MesVlanMapPortmaskIf6_Type(Unsigned32):
    """Custom type mesVlanMapPortmaskIf6 based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MesVlanMapPortmaskIf6_Type.__name__ = "Unsigned32"
_MesVlanMapPortmaskIf6_Object = MibTableColumn
mesVlanMapPortmaskIf6 = _MesVlanMapPortmaskIf6_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 13, 1, 1, 20),
    _MesVlanMapPortmaskIf6_Type()
)
mesVlanMapPortmaskIf6.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesVlanMapPortmaskIf6.setStatus("current")


class _MesVlanMapPortmaskIf7_Type(Unsigned32):
    """Custom type mesVlanMapPortmaskIf7 based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MesVlanMapPortmaskIf7_Type.__name__ = "Unsigned32"
_MesVlanMapPortmaskIf7_Object = MibTableColumn
mesVlanMapPortmaskIf7 = _MesVlanMapPortmaskIf7_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 13, 1, 1, 21),
    _MesVlanMapPortmaskIf7_Type()
)
mesVlanMapPortmaskIf7.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesVlanMapPortmaskIf7.setStatus("current")


class _MesVlanMapPortmaskIf8_Type(Unsigned32):
    """Custom type mesVlanMapPortmaskIf8 based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MesVlanMapPortmaskIf8_Type.__name__ = "Unsigned32"
_MesVlanMapPortmaskIf8_Object = MibTableColumn
mesVlanMapPortmaskIf8 = _MesVlanMapPortmaskIf8_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 13, 1, 1, 22),
    _MesVlanMapPortmaskIf8_Type()
)
mesVlanMapPortmaskIf8.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesVlanMapPortmaskIf8.setStatus("current")
_MesVlanMapPrepareConfigPortMask_Type = CommandString
_MesVlanMapPrepareConfigPortMask_Object = MibTableColumn
mesVlanMapPrepareConfigPortMask = _MesVlanMapPrepareConfigPortMask_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 13, 1, 1, 23),
    _MesVlanMapPrepareConfigPortMask_Type()
)
mesVlanMapPrepareConfigPortMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesVlanMapPrepareConfigPortMask.setStatus("current")


class _MesVlanMapPortmaskIf9_Type(Unsigned32):
    """Custom type mesVlanMapPortmaskIf9 based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MesVlanMapPortmaskIf9_Type.__name__ = "Unsigned32"
_MesVlanMapPortmaskIf9_Object = MibTableColumn
mesVlanMapPortmaskIf9 = _MesVlanMapPortmaskIf9_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 13, 1, 1, 24),
    _MesVlanMapPortmaskIf9_Type()
)
mesVlanMapPortmaskIf9.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesVlanMapPortmaskIf9.setStatus("current")


class _MesVlanMapPortmaskIf10_Type(Unsigned32):
    """Custom type mesVlanMapPortmaskIf10 based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MesVlanMapPortmaskIf10_Type.__name__ = "Unsigned32"
_MesVlanMapPortmaskIf10_Object = MibTableColumn
mesVlanMapPortmaskIf10 = _MesVlanMapPortmaskIf10_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 13, 1, 1, 25),
    _MesVlanMapPortmaskIf10_Type()
)
mesVlanMapPortmaskIf10.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesVlanMapPortmaskIf10.setStatus("current")


class _MesVlanMapPortmaskIf11_Type(Unsigned32):
    """Custom type mesVlanMapPortmaskIf11 based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MesVlanMapPortmaskIf11_Type.__name__ = "Unsigned32"
_MesVlanMapPortmaskIf11_Object = MibTableColumn
mesVlanMapPortmaskIf11 = _MesVlanMapPortmaskIf11_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 13, 1, 1, 26),
    _MesVlanMapPortmaskIf11_Type()
)
mesVlanMapPortmaskIf11.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesVlanMapPortmaskIf11.setStatus("current")


class _MesVlanMapPortmaskIf12_Type(Unsigned32):
    """Custom type mesVlanMapPortmaskIf12 based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MesVlanMapPortmaskIf12_Type.__name__ = "Unsigned32"
_MesVlanMapPortmaskIf12_Object = MibTableColumn
mesVlanMapPortmaskIf12 = _MesVlanMapPortmaskIf12_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 13, 1, 1, 27),
    _MesVlanMapPortmaskIf12_Type()
)
mesVlanMapPortmaskIf12.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesVlanMapPortmaskIf12.setStatus("current")


class _MesVlanMapPortmaskIf13_Type(Unsigned32):
    """Custom type mesVlanMapPortmaskIf13 based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MesVlanMapPortmaskIf13_Type.__name__ = "Unsigned32"
_MesVlanMapPortmaskIf13_Object = MibTableColumn
mesVlanMapPortmaskIf13 = _MesVlanMapPortmaskIf13_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 13, 1, 1, 28),
    _MesVlanMapPortmaskIf13_Type()
)
mesVlanMapPortmaskIf13.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesVlanMapPortmaskIf13.setStatus("current")


class _MesVlanMapPortmaskIf14_Type(Unsigned32):
    """Custom type mesVlanMapPortmaskIf14 based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MesVlanMapPortmaskIf14_Type.__name__ = "Unsigned32"
_MesVlanMapPortmaskIf14_Object = MibTableColumn
mesVlanMapPortmaskIf14 = _MesVlanMapPortmaskIf14_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 13, 1, 1, 29),
    _MesVlanMapPortmaskIf14_Type()
)
mesVlanMapPortmaskIf14.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesVlanMapPortmaskIf14.setStatus("current")


class _MesVlanMapPortmaskIf15_Type(Unsigned32):
    """Custom type mesVlanMapPortmaskIf15 based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MesVlanMapPortmaskIf15_Type.__name__ = "Unsigned32"
_MesVlanMapPortmaskIf15_Object = MibTableColumn
mesVlanMapPortmaskIf15 = _MesVlanMapPortmaskIf15_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 13, 1, 1, 30),
    _MesVlanMapPortmaskIf15_Type()
)
mesVlanMapPortmaskIf15.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesVlanMapPortmaskIf15.setStatus("current")


class _MesVlanMapPortmaskIf16_Type(Unsigned32):
    """Custom type mesVlanMapPortmaskIf16 based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MesVlanMapPortmaskIf16_Type.__name__ = "Unsigned32"
_MesVlanMapPortmaskIf16_Object = MibTableColumn
mesVlanMapPortmaskIf16 = _MesVlanMapPortmaskIf16_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 13, 1, 1, 31),
    _MesVlanMapPortmaskIf16_Type()
)
mesVlanMapPortmaskIf16.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesVlanMapPortmaskIf16.setStatus("current")
_MesVlanMapSubrack_Type = SubrackNumber
_MesVlanMapSubrack_Object = MibTableColumn
mesVlanMapSubrack = _MesVlanMapSubrack_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 13, 1, 1, 32),
    _MesVlanMapSubrack_Type()
)
mesVlanMapSubrack.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesVlanMapSubrack.setStatus("current")
_MesVlanMapSlot_Type = SlotNumber
_MesVlanMapSlot_Object = MibTableColumn
mesVlanMapSlot = _MesVlanMapSlot_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 13, 1, 1, 33),
    _MesVlanMapSlot_Type()
)
mesVlanMapSlot.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesVlanMapSlot.setStatus("current")


class _MesVlanMapMacLearningLimit_Type(Unsigned32):
    """Custom type mesVlanMapMacLearningLimit based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 262143),
    )


_MesVlanMapMacLearningLimit_Type.__name__ = "Unsigned32"
_MesVlanMapMacLearningLimit_Object = MibTableColumn
mesVlanMapMacLearningLimit = _MesVlanMapMacLearningLimit_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 13, 1, 1, 34),
    _MesVlanMapMacLearningLimit_Type()
)
mesVlanMapMacLearningLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesVlanMapMacLearningLimit.setStatus("current")
_MesMgmtVlanList_ObjectIdentity = ObjectIdentity
mesMgmtVlanList = _MesMgmtVlanList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 14)
)
_MesMgmtVlanTable_Object = MibTable
mesMgmtVlanTable = _MesMgmtVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 14, 1)
)
if mibBuilder.loadTexts:
    mesMgmtVlanTable.setStatus("current")
_MesMgmtVlanEntry_Object = MibTableRow
mesMgmtVlanEntry = _MesMgmtVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 14, 1, 1)
)
mesMgmtVlanEntry.setIndexNames(
    (0, "LUM-MES-MIB", "mesMgmtVlanIndex"),
)
if mibBuilder.loadTexts:
    mesMgmtVlanEntry.setStatus("current")


class _MesMgmtVlanIndex_Type(Unsigned32):
    """Custom type mesMgmtVlanIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_MesMgmtVlanIndex_Type.__name__ = "Unsigned32"
_MesMgmtVlanIndex_Object = MibTableColumn
mesMgmtVlanIndex = _MesMgmtVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 14, 1, 1, 1),
    _MesMgmtVlanIndex_Type()
)
mesMgmtVlanIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesMgmtVlanIndex.setStatus("current")
_MesMgmtVlanName_Type = MgmtNameString
_MesMgmtVlanName_Object = MibTableColumn
mesMgmtVlanName = _MesMgmtVlanName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 14, 1, 1, 2),
    _MesMgmtVlanName_Type()
)
mesMgmtVlanName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesMgmtVlanName.setStatus("current")


class _MesMgmtVlanDescr_Type(DisplayString):
    """Custom type mesMgmtVlanDescr based on DisplayString"""
    defaultValue = OctetString("")


_MesMgmtVlanDescr_Type.__name__ = "DisplayString"
_MesMgmtVlanDescr_Object = MibTableColumn
mesMgmtVlanDescr = _MesMgmtVlanDescr_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 14, 1, 1, 3),
    _MesMgmtVlanDescr_Type()
)
mesMgmtVlanDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mesMgmtVlanDescr.setStatus("current")
_MesMgmtVlanSubrack_Type = SubrackNumber
_MesMgmtVlanSubrack_Object = MibTableColumn
mesMgmtVlanSubrack = _MesMgmtVlanSubrack_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 14, 1, 1, 4),
    _MesMgmtVlanSubrack_Type()
)
mesMgmtVlanSubrack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesMgmtVlanSubrack.setStatus("current")
_MesMgmtVlanSlot_Type = SlotNumber
_MesMgmtVlanSlot_Object = MibTableColumn
mesMgmtVlanSlot = _MesMgmtVlanSlot_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 14, 1, 1, 5),
    _MesMgmtVlanSlot_Type()
)
mesMgmtVlanSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesMgmtVlanSlot.setStatus("current")
_MesMgmtVlanTxPort_Type = PortNumber
_MesMgmtVlanTxPort_Object = MibTableColumn
mesMgmtVlanTxPort = _MesMgmtVlanTxPort_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 14, 1, 1, 6),
    _MesMgmtVlanTxPort_Type()
)
mesMgmtVlanTxPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesMgmtVlanTxPort.setStatus("current")
_MesMgmtVlanRxPort_Type = PortNumber
_MesMgmtVlanRxPort_Object = MibTableColumn
mesMgmtVlanRxPort = _MesMgmtVlanRxPort_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 14, 1, 1, 7),
    _MesMgmtVlanRxPort_Type()
)
mesMgmtVlanRxPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesMgmtVlanRxPort.setStatus("current")
_MesMgmtVlanObjectProperty_Type = ObjectProperty
_MesMgmtVlanObjectProperty_Object = MibTableColumn
mesMgmtVlanObjectProperty = _MesMgmtVlanObjectProperty_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 14, 1, 1, 8),
    _MesMgmtVlanObjectProperty_Type()
)
mesMgmtVlanObjectProperty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesMgmtVlanObjectProperty.setStatus("current")


class _MesMgmtVlanAdminStatus_Type(BoardOrInterfaceAdminStatus):
    """Custom type mesMgmtVlanAdminStatus based on BoardOrInterfaceAdminStatus"""
    defaultValue = 1


_MesMgmtVlanAdminStatus_Type.__name__ = "BoardOrInterfaceAdminStatus"
_MesMgmtVlanAdminStatus_Object = MibTableColumn
mesMgmtVlanAdminStatus = _MesMgmtVlanAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 14, 1, 1, 9),
    _MesMgmtVlanAdminStatus_Type()
)
mesMgmtVlanAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mesMgmtVlanAdminStatus.setStatus("current")
_MesMgmtVlanConfigure_Type = CommandString
_MesMgmtVlanConfigure_Object = MibTableColumn
mesMgmtVlanConfigure = _MesMgmtVlanConfigure_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 14, 1, 1, 10),
    _MesMgmtVlanConfigure_Type()
)
mesMgmtVlanConfigure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesMgmtVlanConfigure.setStatus("current")


class _MesMgmtVlanTagType_Type(Integer32):
    """Custom type mesMgmtVlanTagType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("qTag0x8100", 1),
          ("sTag0x88a8", 2))
    )


_MesMgmtVlanTagType_Type.__name__ = "Integer32"
_MesMgmtVlanTagType_Object = MibTableColumn
mesMgmtVlanTagType = _MesMgmtVlanTagType_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 14, 1, 1, 11),
    _MesMgmtVlanTagType_Type()
)
mesMgmtVlanTagType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesMgmtVlanTagType.setStatus("current")


class _MesMgmtVlanEtherType_Type(Unsigned32):
    """Custom type mesMgmtVlanEtherType based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MesMgmtVlanEtherType_Type.__name__ = "Unsigned32"
_MesMgmtVlanEtherType_Object = MibTableColumn
mesMgmtVlanEtherType = _MesMgmtVlanEtherType_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 14, 1, 1, 12),
    _MesMgmtVlanEtherType_Type()
)
mesMgmtVlanEtherType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesMgmtVlanEtherType.setStatus("current")


class _MesMgmtVlanVlanId_Type(Unsigned32):
    """Custom type mesMgmtVlanVlanId based on Unsigned32"""
    defaultValue = 4094

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_MesMgmtVlanVlanId_Type.__name__ = "Unsigned32"
_MesMgmtVlanVlanId_Object = MibTableColumn
mesMgmtVlanVlanId = _MesMgmtVlanVlanId_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 14, 1, 1, 13),
    _MesMgmtVlanVlanId_Type()
)
mesMgmtVlanVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesMgmtVlanVlanId.setStatus("current")


class _MesMgmtVlanPriority_Type(Unsigned32):
    """Custom type mesMgmtVlanPriority based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_MesMgmtVlanPriority_Type.__name__ = "Unsigned32"
_MesMgmtVlanPriority_Object = MibTableColumn
mesMgmtVlanPriority = _MesMgmtVlanPriority_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 14, 1, 1, 14),
    _MesMgmtVlanPriority_Type()
)
mesMgmtVlanPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesMgmtVlanPriority.setStatus("current")


class _MesMgmtVlanMacInMac_Type(Integer32):
    """Custom type mesMgmtVlanMacInMac based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_MesMgmtVlanMacInMac_Type.__name__ = "Integer32"
_MesMgmtVlanMacInMac_Object = MibTableColumn
mesMgmtVlanMacInMac = _MesMgmtVlanMacInMac_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 14, 1, 1, 15),
    _MesMgmtVlanMacInMac_Type()
)
mesMgmtVlanMacInMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesMgmtVlanMacInMac.setStatus("current")


class _MesMgmtVlanMacInMacIsid_Type(Unsigned32):
    """Custom type mesMgmtVlanMacInMacIsid based on Unsigned32"""
    defaultValue = 256

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(256, 16777214),
    )


_MesMgmtVlanMacInMacIsid_Type.__name__ = "Unsigned32"
_MesMgmtVlanMacInMacIsid_Object = MibTableColumn
mesMgmtVlanMacInMacIsid = _MesMgmtVlanMacInMacIsid_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 14, 1, 1, 16),
    _MesMgmtVlanMacInMacIsid_Type()
)
mesMgmtVlanMacInMacIsid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesMgmtVlanMacInMacIsid.setStatus("current")


class _MesMgmtVlanMacInMacDa_Type(DisplayString):
    """Custom type mesMgmtVlanMacInMacDa based on DisplayString"""
    defaultValue = OctetString("")


_MesMgmtVlanMacInMacDa_Type.__name__ = "DisplayString"
_MesMgmtVlanMacInMacDa_Object = MibTableColumn
mesMgmtVlanMacInMacDa = _MesMgmtVlanMacInMacDa_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 14, 1, 1, 17),
    _MesMgmtVlanMacInMacDa_Type()
)
mesMgmtVlanMacInMacDa.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesMgmtVlanMacInMacDa.setStatus("current")


class _MesMgmtVlanForceMgmtVlan_Type(Integer32):
    """Custom type mesMgmtVlanForceMgmtVlan based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_MesMgmtVlanForceMgmtVlan_Type.__name__ = "Integer32"
_MesMgmtVlanForceMgmtVlan_Object = MibTableColumn
mesMgmtVlanForceMgmtVlan = _MesMgmtVlanForceMgmtVlan_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 14, 1, 1, 18),
    _MesMgmtVlanForceMgmtVlan_Type()
)
mesMgmtVlanForceMgmtVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mesMgmtVlanForceMgmtVlan.setStatus("current")


class _MesMgmtVlanRings_Type(Counter64):
    """Custom type mesMgmtVlanRings based on Counter64"""
    defaultValue = 0


_MesMgmtVlanRings_Type.__name__ = "Counter64"
_MesMgmtVlanRings_Object = MibTableColumn
mesMgmtVlanRings = _MesMgmtVlanRings_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 14, 1, 1, 19),
    _MesMgmtVlanRings_Type()
)
mesMgmtVlanRings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesMgmtVlanRings.setStatus("current")


class _MesMgmtVlanIfNo_Type(PortNumber):
    """Custom type mesMgmtVlanIfNo based on PortNumber"""
    defaultValue = 1


_MesMgmtVlanIfNo_Type.__name__ = "PortNumber"
_MesMgmtVlanIfNo_Object = MibTableColumn
mesMgmtVlanIfNo = _MesMgmtVlanIfNo_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 14, 1, 1, 20),
    _MesMgmtVlanIfNo_Type()
)
mesMgmtVlanIfNo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesMgmtVlanIfNo.setStatus("current")
_MesLagList_ObjectIdentity = ObjectIdentity
mesLagList = _MesLagList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 15)
)
_MesLagTable_Object = MibTable
mesLagTable = _MesLagTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 15, 1)
)
if mibBuilder.loadTexts:
    mesLagTable.setStatus("current")
_MesLagEntry_Object = MibTableRow
mesLagEntry = _MesLagEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 15, 1, 1)
)
mesLagEntry.setIndexNames(
    (0, "LUM-MES-MIB", "mesLagIndex"),
)
if mibBuilder.loadTexts:
    mesLagEntry.setStatus("current")


class _MesLagIndex_Type(Unsigned32):
    """Custom type mesLagIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_MesLagIndex_Type.__name__ = "Unsigned32"
_MesLagIndex_Object = MibTableColumn
mesLagIndex = _MesLagIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 15, 1, 1, 1),
    _MesLagIndex_Type()
)
mesLagIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesLagIndex.setStatus("current")
_MesLagName_Type = MgmtNameString
_MesLagName_Object = MibTableColumn
mesLagName = _MesLagName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 15, 1, 1, 2),
    _MesLagName_Type()
)
mesLagName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesLagName.setStatus("current")


class _MesLagInternalReference_Type(Unsigned32):
    """Custom type mesLagInternalReference based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MesLagInternalReference_Type.__name__ = "Unsigned32"
_MesLagInternalReference_Object = MibTableColumn
mesLagInternalReference = _MesLagInternalReference_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 15, 1, 1, 3),
    _MesLagInternalReference_Type()
)
mesLagInternalReference.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesLagInternalReference.setStatus("current")


class _MesLagPortmask_Type(Unsigned32):
    """Custom type mesLagPortmask based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MesLagPortmask_Type.__name__ = "Unsigned32"
_MesLagPortmask_Object = MibTableColumn
mesLagPortmask = _MesLagPortmask_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 15, 1, 1, 4),
    _MesLagPortmask_Type()
)
mesLagPortmask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesLagPortmask.setStatus("current")


class _MesLagMasterIndex_Type(Unsigned32):
    """Custom type mesLagMasterIndex based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MesLagMasterIndex_Type.__name__ = "Unsigned32"
_MesLagMasterIndex_Object = MibTableColumn
mesLagMasterIndex = _MesLagMasterIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 15, 1, 1, 5),
    _MesLagMasterIndex_Type()
)
mesLagMasterIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesLagMasterIndex.setStatus("current")
_MesLagConfigure_Type = CommandString
_MesLagConfigure_Object = MibTableColumn
mesLagConfigure = _MesLagConfigure_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 15, 1, 1, 6),
    _MesLagConfigure_Type()
)
mesLagConfigure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesLagConfigure.setStatus("current")


class _MesLagHash_Type(Integer32):
    """Custom type mesLagHash based on Integer32"""
    defaultValue = 5

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
        *(("mac", 1),
          ("ip", 2),
          ("vlan", 3),
          ("mpls", 4),
          ("automatic", 5))
    )


_MesLagHash_Type.__name__ = "Integer32"
_MesLagHash_Object = MibTableColumn
mesLagHash = _MesLagHash_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 15, 1, 1, 7),
    _MesLagHash_Type()
)
mesLagHash.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesLagHash.setStatus("current")


class _MesLagIdentifier_Type(DisplayString):
    """Custom type mesLagIdentifier based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 17),
    )


_MesLagIdentifier_Type.__name__ = "DisplayString"
_MesLagIdentifier_Object = MibTableColumn
mesLagIdentifier = _MesLagIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 15, 1, 1, 8),
    _MesLagIdentifier_Type()
)
mesLagIdentifier.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesLagIdentifier.setStatus("current")
_MesLagRowStatus_Type = RowStatus
_MesLagRowStatus_Object = MibTableColumn
mesLagRowStatus = _MesLagRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 15, 1, 1, 9),
    _MesLagRowStatus_Type()
)
mesLagRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesLagRowStatus.setStatus("current")


class _MesLagLacpEnabled_Type(Integer32):
    """Custom type mesLagLacpEnabled based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("passive", 1),
          ("active", 2))
    )


_MesLagLacpEnabled_Type.__name__ = "Integer32"
_MesLagLacpEnabled_Object = MibTableColumn
mesLagLacpEnabled = _MesLagLacpEnabled_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 15, 1, 1, 10),
    _MesLagLacpEnabled_Type()
)
mesLagLacpEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mesLagLacpEnabled.setStatus("current")


class _MesLagLacpSystemPriority_Type(Unsigned32):
    """Custom type mesLagLacpSystemPriority based on Unsigned32"""
    defaultValue = 32768

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MesLagLacpSystemPriority_Type.__name__ = "Unsigned32"
_MesLagLacpSystemPriority_Object = MibTableColumn
mesLagLacpSystemPriority = _MesLagLacpSystemPriority_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 15, 1, 1, 11),
    _MesLagLacpSystemPriority_Type()
)
mesLagLacpSystemPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesLagLacpSystemPriority.setStatus("current")


class _MesLagLacpPeriod_Type(Integer32):
    """Custom type mesLagLacpPeriod based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("slow", 0),
          ("fast", 1))
    )


_MesLagLacpPeriod_Type.__name__ = "Integer32"
_MesLagLacpPeriod_Object = MibTableColumn
mesLagLacpPeriod = _MesLagLacpPeriod_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 15, 1, 1, 12),
    _MesLagLacpPeriod_Type()
)
mesLagLacpPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mesLagLacpPeriod.setStatus("current")


class _MesLagLacpLinkProtection_Type(MesLacpLinkProtectionValue):
    """Custom type mesLagLacpLinkProtection based on MesLacpLinkProtectionValue"""
    defaultValue = 0


_MesLagLacpLinkProtection_Type.__name__ = "MesLacpLinkProtectionValue"
_MesLagLacpLinkProtection_Object = MibTableColumn
mesLagLacpLinkProtection = _MesLagLacpLinkProtection_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 15, 1, 1, 13),
    _MesLagLacpLinkProtection_Type()
)
mesLagLacpLinkProtection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mesLagLacpLinkProtection.setStatus("deprecated")
_MesLagDegraded_Type = FaultStatus
_MesLagDegraded_Object = MibTableColumn
mesLagDegraded = _MesLagDegraded_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 15, 1, 1, 14),
    _MesLagDegraded_Type()
)
mesLagDegraded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesLagDegraded.setStatus("current")
_MesLagFailure_Type = FaultStatus
_MesLagFailure_Object = MibTableColumn
mesLagFailure = _MesLagFailure_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 15, 1, 1, 15),
    _MesLagFailure_Type()
)
mesLagFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesLagFailure.setStatus("current")


class _MesLagLacpMaxNumberOfActiveLinks_Type(Unsigned32):
    """Custom type mesLagLacpMaxNumberOfActiveLinks based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 12),
    )


_MesLagLacpMaxNumberOfActiveLinks_Type.__name__ = "Unsigned32"
_MesLagLacpMaxNumberOfActiveLinks_Object = MibTableColumn
mesLagLacpMaxNumberOfActiveLinks = _MesLagLacpMaxNumberOfActiveLinks_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 15, 1, 1, 16),
    _MesLagLacpMaxNumberOfActiveLinks_Type()
)
mesLagLacpMaxNumberOfActiveLinks.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mesLagLacpMaxNumberOfActiveLinks.setStatus("current")
_MesLagNoOfPorts_Type = Unsigned32
_MesLagNoOfPorts_Object = MibTableColumn
mesLagNoOfPorts = _MesLagNoOfPorts_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 15, 1, 1, 17),
    _MesLagNoOfPorts_Type()
)
mesLagNoOfPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesLagNoOfPorts.setStatus("current")


class _MesLagLacpMinNumberOfActiveLinks_Type(Unsigned32):
    """Custom type mesLagLacpMinNumberOfActiveLinks based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 12),
    )


_MesLagLacpMinNumberOfActiveLinks_Type.__name__ = "Unsigned32"
_MesLagLacpMinNumberOfActiveLinks_Object = MibTableColumn
mesLagLacpMinNumberOfActiveLinks = _MesLagLacpMinNumberOfActiveLinks_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 15, 1, 1, 18),
    _MesLagLacpMinNumberOfActiveLinks_Type()
)
mesLagLacpMinNumberOfActiveLinks.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mesLagLacpMinNumberOfActiveLinks.setStatus("current")


class _MesLagIsMcLag_Type(Integer32):
    """Custom type mesLagIsMcLag based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_MesLagIsMcLag_Type.__name__ = "Integer32"
_MesLagIsMcLag_Object = MibTableColumn
mesLagIsMcLag = _MesLagIsMcLag_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 15, 1, 1, 19),
    _MesLagIsMcLag_Type()
)
mesLagIsMcLag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mesLagIsMcLag.setStatus("current")
_MesLagConfigureTagRule_Type = CommandString
_MesLagConfigureTagRule_Object = MibTableColumn
mesLagConfigureTagRule = _MesLagConfigureTagRule_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 15, 1, 1, 20),
    _MesLagConfigureTagRule_Type()
)
mesLagConfigureTagRule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesLagConfigureTagRule.setStatus("current")
_MesLagNoOfTagRules_Type = Unsigned32
_MesLagNoOfTagRules_Object = MibTableColumn
mesLagNoOfTagRules = _MesLagNoOfTagRules_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 15, 1, 1, 21),
    _MesLagNoOfTagRules_Type()
)
mesLagNoOfTagRules.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesLagNoOfTagRules.setStatus("current")


class _MesLagDescr_Type(DisplayString):
    """Custom type mesLagDescr based on DisplayString"""
    defaultValue = OctetString("")


_MesLagDescr_Type.__name__ = "DisplayString"
_MesLagDescr_Object = MibTableColumn
mesLagDescr = _MesLagDescr_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 15, 1, 1, 22),
    _MesLagDescr_Type()
)
mesLagDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mesLagDescr.setStatus("current")


class _MesLagAdminStatus_Type(BoardOrInterfaceAdminStatus):
    """Custom type mesLagAdminStatus based on BoardOrInterfaceAdminStatus"""
    defaultValue = 3


_MesLagAdminStatus_Type.__name__ = "BoardOrInterfaceAdminStatus"
_MesLagAdminStatus_Object = MibTableColumn
mesLagAdminStatus = _MesLagAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 15, 1, 1, 23),
    _MesLagAdminStatus_Type()
)
mesLagAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mesLagAdminStatus.setStatus("current")


class _MesLagOperStatus_Type(BoardOrInterfaceOperStatus):
    """Custom type mesLagOperStatus based on BoardOrInterfaceOperStatus"""
    defaultValue = 1


_MesLagOperStatus_Type.__name__ = "BoardOrInterfaceOperStatus"
_MesLagOperStatus_Object = MibTableColumn
mesLagOperStatus = _MesLagOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 15, 1, 1, 24),
    _MesLagOperStatus_Type()
)
mesLagOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesLagOperStatus.setStatus("current")


class _MesLagPortmaskIf1_Type(Unsigned32):
    """Custom type mesLagPortmaskIf1 based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MesLagPortmaskIf1_Type.__name__ = "Unsigned32"
_MesLagPortmaskIf1_Object = MibTableColumn
mesLagPortmaskIf1 = _MesLagPortmaskIf1_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 15, 1, 1, 25),
    _MesLagPortmaskIf1_Type()
)
mesLagPortmaskIf1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesLagPortmaskIf1.setStatus("current")


class _MesLagPortmaskIf2_Type(Unsigned32):
    """Custom type mesLagPortmaskIf2 based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MesLagPortmaskIf2_Type.__name__ = "Unsigned32"
_MesLagPortmaskIf2_Object = MibTableColumn
mesLagPortmaskIf2 = _MesLagPortmaskIf2_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 15, 1, 1, 26),
    _MesLagPortmaskIf2_Type()
)
mesLagPortmaskIf2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesLagPortmaskIf2.setStatus("current")


class _MesLagPortmaskIf3_Type(Unsigned32):
    """Custom type mesLagPortmaskIf3 based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MesLagPortmaskIf3_Type.__name__ = "Unsigned32"
_MesLagPortmaskIf3_Object = MibTableColumn
mesLagPortmaskIf3 = _MesLagPortmaskIf3_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 15, 1, 1, 27),
    _MesLagPortmaskIf3_Type()
)
mesLagPortmaskIf3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesLagPortmaskIf3.setStatus("current")


class _MesLagPortmaskIf4_Type(Unsigned32):
    """Custom type mesLagPortmaskIf4 based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MesLagPortmaskIf4_Type.__name__ = "Unsigned32"
_MesLagPortmaskIf4_Object = MibTableColumn
mesLagPortmaskIf4 = _MesLagPortmaskIf4_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 15, 1, 1, 28),
    _MesLagPortmaskIf4_Type()
)
mesLagPortmaskIf4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesLagPortmaskIf4.setStatus("current")


class _MesLagPortmaskIf5_Type(Unsigned32):
    """Custom type mesLagPortmaskIf5 based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MesLagPortmaskIf5_Type.__name__ = "Unsigned32"
_MesLagPortmaskIf5_Object = MibTableColumn
mesLagPortmaskIf5 = _MesLagPortmaskIf5_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 15, 1, 1, 29),
    _MesLagPortmaskIf5_Type()
)
mesLagPortmaskIf5.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesLagPortmaskIf5.setStatus("current")


class _MesLagPortmaskIf6_Type(Unsigned32):
    """Custom type mesLagPortmaskIf6 based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MesLagPortmaskIf6_Type.__name__ = "Unsigned32"
_MesLagPortmaskIf6_Object = MibTableColumn
mesLagPortmaskIf6 = _MesLagPortmaskIf6_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 15, 1, 1, 30),
    _MesLagPortmaskIf6_Type()
)
mesLagPortmaskIf6.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesLagPortmaskIf6.setStatus("current")


class _MesLagPortmaskIf7_Type(Unsigned32):
    """Custom type mesLagPortmaskIf7 based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MesLagPortmaskIf7_Type.__name__ = "Unsigned32"
_MesLagPortmaskIf7_Object = MibTableColumn
mesLagPortmaskIf7 = _MesLagPortmaskIf7_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 15, 1, 1, 31),
    _MesLagPortmaskIf7_Type()
)
mesLagPortmaskIf7.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesLagPortmaskIf7.setStatus("current")


class _MesLagPortmaskIf8_Type(Unsigned32):
    """Custom type mesLagPortmaskIf8 based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MesLagPortmaskIf8_Type.__name__ = "Unsigned32"
_MesLagPortmaskIf8_Object = MibTableColumn
mesLagPortmaskIf8 = _MesLagPortmaskIf8_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 15, 1, 1, 32),
    _MesLagPortmaskIf8_Type()
)
mesLagPortmaskIf8.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesLagPortmaskIf8.setStatus("current")


class _MesLagMasterIfNo_Type(PortNumber):
    """Custom type mesLagMasterIfNo based on PortNumber"""
    defaultValue = 1


_MesLagMasterIfNo_Type.__name__ = "PortNumber"
_MesLagMasterIfNo_Object = MibTableColumn
mesLagMasterIfNo = _MesLagMasterIfNo_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 15, 1, 1, 33),
    _MesLagMasterIfNo_Type()
)
mesLagMasterIfNo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesLagMasterIfNo.setStatus("current")


class _MesLagMasterTxPort_Type(PortNumber):
    """Custom type mesLagMasterTxPort based on PortNumber"""
    defaultValue = 0


_MesLagMasterTxPort_Type.__name__ = "PortNumber"
_MesLagMasterTxPort_Object = MibTableColumn
mesLagMasterTxPort = _MesLagMasterTxPort_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 15, 1, 1, 34),
    _MesLagMasterTxPort_Type()
)
mesLagMasterTxPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesLagMasterTxPort.setStatus("current")


class _MesLagLocalId_Type(Integer32):
    """Custom type mesLagLocalId based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_MesLagLocalId_Type.__name__ = "Integer32"
_MesLagLocalId_Object = MibTableColumn
mesLagLocalId = _MesLagLocalId_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 15, 1, 1, 35),
    _MesLagLocalId_Type()
)
mesLagLocalId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesLagLocalId.setStatus("current")
_MesLagPrepareConfigPortMask_Type = CommandString
_MesLagPrepareConfigPortMask_Object = MibTableColumn
mesLagPrepareConfigPortMask = _MesLagPrepareConfigPortMask_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 15, 1, 1, 36),
    _MesLagPrepareConfigPortMask_Type()
)
mesLagPrepareConfigPortMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesLagPrepareConfigPortMask.setStatus("current")


class _MesLagPortmaskIf9_Type(Unsigned32):
    """Custom type mesLagPortmaskIf9 based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MesLagPortmaskIf9_Type.__name__ = "Unsigned32"
_MesLagPortmaskIf9_Object = MibTableColumn
mesLagPortmaskIf9 = _MesLagPortmaskIf9_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 15, 1, 1, 37),
    _MesLagPortmaskIf9_Type()
)
mesLagPortmaskIf9.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesLagPortmaskIf9.setStatus("current")


class _MesLagPortmaskIf10_Type(Unsigned32):
    """Custom type mesLagPortmaskIf10 based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MesLagPortmaskIf10_Type.__name__ = "Unsigned32"
_MesLagPortmaskIf10_Object = MibTableColumn
mesLagPortmaskIf10 = _MesLagPortmaskIf10_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 15, 1, 1, 38),
    _MesLagPortmaskIf10_Type()
)
mesLagPortmaskIf10.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesLagPortmaskIf10.setStatus("current")


class _MesLagPortmaskIf11_Type(Unsigned32):
    """Custom type mesLagPortmaskIf11 based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MesLagPortmaskIf11_Type.__name__ = "Unsigned32"
_MesLagPortmaskIf11_Object = MibTableColumn
mesLagPortmaskIf11 = _MesLagPortmaskIf11_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 15, 1, 1, 39),
    _MesLagPortmaskIf11_Type()
)
mesLagPortmaskIf11.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesLagPortmaskIf11.setStatus("current")


class _MesLagPortmaskIf12_Type(Unsigned32):
    """Custom type mesLagPortmaskIf12 based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MesLagPortmaskIf12_Type.__name__ = "Unsigned32"
_MesLagPortmaskIf12_Object = MibTableColumn
mesLagPortmaskIf12 = _MesLagPortmaskIf12_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 15, 1, 1, 40),
    _MesLagPortmaskIf12_Type()
)
mesLagPortmaskIf12.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesLagPortmaskIf12.setStatus("current")


class _MesLagPortmaskIf13_Type(Unsigned32):
    """Custom type mesLagPortmaskIf13 based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MesLagPortmaskIf13_Type.__name__ = "Unsigned32"
_MesLagPortmaskIf13_Object = MibTableColumn
mesLagPortmaskIf13 = _MesLagPortmaskIf13_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 15, 1, 1, 41),
    _MesLagPortmaskIf13_Type()
)
mesLagPortmaskIf13.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesLagPortmaskIf13.setStatus("current")


class _MesLagPortmaskIf14_Type(Unsigned32):
    """Custom type mesLagPortmaskIf14 based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MesLagPortmaskIf14_Type.__name__ = "Unsigned32"
_MesLagPortmaskIf14_Object = MibTableColumn
mesLagPortmaskIf14 = _MesLagPortmaskIf14_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 15, 1, 1, 42),
    _MesLagPortmaskIf14_Type()
)
mesLagPortmaskIf14.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesLagPortmaskIf14.setStatus("current")


class _MesLagPortmaskIf15_Type(Unsigned32):
    """Custom type mesLagPortmaskIf15 based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MesLagPortmaskIf15_Type.__name__ = "Unsigned32"
_MesLagPortmaskIf15_Object = MibTableColumn
mesLagPortmaskIf15 = _MesLagPortmaskIf15_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 15, 1, 1, 43),
    _MesLagPortmaskIf15_Type()
)
mesLagPortmaskIf15.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesLagPortmaskIf15.setStatus("current")


class _MesLagPortmaskIf16_Type(Unsigned32):
    """Custom type mesLagPortmaskIf16 based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MesLagPortmaskIf16_Type.__name__ = "Unsigned32"
_MesLagPortmaskIf16_Object = MibTableColumn
mesLagPortmaskIf16 = _MesLagPortmaskIf16_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 15, 1, 1, 44),
    _MesLagPortmaskIf16_Type()
)
mesLagPortmaskIf16.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesLagPortmaskIf16.setStatus("current")


class _MesLagServiceId_Type(ServiceIdWithNotUsed):
    """Custom type mesLagServiceId based on ServiceIdWithNotUsed"""
    defaultValue = -1


_MesLagServiceId_Type.__name__ = "ServiceIdWithNotUsed"
_MesLagServiceId_Object = MibTableColumn
mesLagServiceId = _MesLagServiceId_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 15, 1, 1, 45),
    _MesLagServiceId_Type()
)
mesLagServiceId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mesLagServiceId.setStatus("current")
_MesPolicingList_ObjectIdentity = ObjectIdentity
mesPolicingList = _MesPolicingList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 16)
)
_MesPolicingTable_Object = MibTable
mesPolicingTable = _MesPolicingTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 16, 1)
)
if mibBuilder.loadTexts:
    mesPolicingTable.setStatus("current")
_MesPolicingEntry_Object = MibTableRow
mesPolicingEntry = _MesPolicingEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 16, 1, 1)
)
mesPolicingEntry.setIndexNames(
    (0, "LUM-MES-MIB", "mesPolicingIndex"),
)
if mibBuilder.loadTexts:
    mesPolicingEntry.setStatus("current")


class _MesPolicingIndex_Type(Unsigned32):
    """Custom type mesPolicingIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_MesPolicingIndex_Type.__name__ = "Unsigned32"
_MesPolicingIndex_Object = MibTableColumn
mesPolicingIndex = _MesPolicingIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 16, 1, 1, 1),
    _MesPolicingIndex_Type()
)
mesPolicingIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesPolicingIndex.setStatus("current")
_MesPolicingName_Type = MgmtNameString
_MesPolicingName_Object = MibTableColumn
mesPolicingName = _MesPolicingName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 16, 1, 1, 2),
    _MesPolicingName_Type()
)
mesPolicingName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesPolicingName.setStatus("current")


class _MesPolicingRate_Type(Unsigned32):
    """Custom type mesPolicingRate based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000000),
    )


_MesPolicingRate_Type.__name__ = "Unsigned32"
_MesPolicingRate_Object = MibTableColumn
mesPolicingRate = _MesPolicingRate_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 16, 1, 1, 3),
    _MesPolicingRate_Type()
)
mesPolicingRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mesPolicingRate.setStatus("current")


class _MesPolicingBurstSize_Type(Unsigned32):
    """Custom type mesPolicingBurstSize based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16320),
    )


_MesPolicingBurstSize_Type.__name__ = "Unsigned32"
_MesPolicingBurstSize_Object = MibTableColumn
mesPolicingBurstSize = _MesPolicingBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 16, 1, 1, 4),
    _MesPolicingBurstSize_Type()
)
mesPolicingBurstSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mesPolicingBurstSize.setStatus("current")


class _MesPolicingType_Type(Integer32):
    """Custom type mesPolicingType based on Integer32"""
    defaultValue = 1

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
        *(("all", 1),
          ("broadcast", 2),
          ("broadcastMulticast", 3),
          ("broadcastUnknownunicast", 4),
          ("broadcastMulticastUnknownunicast", 5))
    )


_MesPolicingType_Type.__name__ = "Integer32"
_MesPolicingType_Object = MibTableColumn
mesPolicingType = _MesPolicingType_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 16, 1, 1, 5),
    _MesPolicingType_Type()
)
mesPolicingType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesPolicingType.setStatus("current")


class _MesPolicingInternalReference_Type(Unsigned32):
    """Custom type mesPolicingInternalReference based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MesPolicingInternalReference_Type.__name__ = "Unsigned32"
_MesPolicingInternalReference_Object = MibTableColumn
mesPolicingInternalReference = _MesPolicingInternalReference_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 16, 1, 1, 6),
    _MesPolicingInternalReference_Type()
)
mesPolicingInternalReference.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesPolicingInternalReference.setStatus("obsolete")


class _MesPolicingIdentifier_Type(DisplayString):
    """Custom type mesPolicingIdentifier based on DisplayString"""
    defaultValue = OctetString(" ")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_MesPolicingIdentifier_Type.__name__ = "DisplayString"
_MesPolicingIdentifier_Object = MibTableColumn
mesPolicingIdentifier = _MesPolicingIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 16, 1, 1, 7),
    _MesPolicingIdentifier_Type()
)
mesPolicingIdentifier.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesPolicingIdentifier.setStatus("current")


class _MesPolicingUpId_Type(Unsigned32):
    """Custom type mesPolicingUpId based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MesPolicingUpId_Type.__name__ = "Unsigned32"
_MesPolicingUpId_Object = MibTableColumn
mesPolicingUpId = _MesPolicingUpId_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 16, 1, 1, 8),
    _MesPolicingUpId_Type()
)
mesPolicingUpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesPolicingUpId.setStatus("current")


class _MesPolicingBurstSize2_Type(Unsigned32):
    """Custom type mesPolicingBurstSize2 based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_MesPolicingBurstSize2_Type.__name__ = "Unsigned32"
_MesPolicingBurstSize2_Object = MibTableColumn
mesPolicingBurstSize2 = _MesPolicingBurstSize2_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 16, 1, 1, 9),
    _MesPolicingBurstSize2_Type()
)
mesPolicingBurstSize2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mesPolicingBurstSize2.setStatus("current")


class _MesPolicingId_Type(Integer32):
    """Custom type mesPolicingId based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_MesPolicingId_Type.__name__ = "Integer32"
_MesPolicingId_Object = MibTableColumn
mesPolicingId = _MesPolicingId_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 16, 1, 1, 10),
    _MesPolicingId_Type()
)
mesPolicingId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesPolicingId.setStatus("current")
_MesShapingList_ObjectIdentity = ObjectIdentity
mesShapingList = _MesShapingList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 17)
)
_MesShapingTable_Object = MibTable
mesShapingTable = _MesShapingTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 17, 1)
)
if mibBuilder.loadTexts:
    mesShapingTable.setStatus("current")
_MesShapingEntry_Object = MibTableRow
mesShapingEntry = _MesShapingEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 17, 1, 1)
)
mesShapingEntry.setIndexNames(
    (0, "LUM-MES-MIB", "mesShapingIndex"),
)
if mibBuilder.loadTexts:
    mesShapingEntry.setStatus("current")


class _MesShapingIndex_Type(Unsigned32):
    """Custom type mesShapingIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_MesShapingIndex_Type.__name__ = "Unsigned32"
_MesShapingIndex_Object = MibTableColumn
mesShapingIndex = _MesShapingIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 17, 1, 1, 1),
    _MesShapingIndex_Type()
)
mesShapingIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesShapingIndex.setStatus("current")
_MesShapingName_Type = MgmtNameString
_MesShapingName_Object = MibTableColumn
mesShapingName = _MesShapingName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 17, 1, 1, 2),
    _MesShapingName_Type()
)
mesShapingName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesShapingName.setStatus("current")


class _MesShapingRate_Type(Unsigned32):
    """Custom type mesShapingRate based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000000),
    )


_MesShapingRate_Type.__name__ = "Unsigned32"
_MesShapingRate_Object = MibTableColumn
mesShapingRate = _MesShapingRate_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 17, 1, 1, 3),
    _MesShapingRate_Type()
)
mesShapingRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mesShapingRate.setStatus("current")


class _MesShapingBurstSize_Type(Unsigned32):
    """Custom type mesShapingBurstSize based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8128),
    )


_MesShapingBurstSize_Type.__name__ = "Unsigned32"
_MesShapingBurstSize_Object = MibTableColumn
mesShapingBurstSize = _MesShapingBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 17, 1, 1, 4),
    _MesShapingBurstSize_Type()
)
mesShapingBurstSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mesShapingBurstSize.setStatus("current")


class _MesShapingQueue_Type(Unsigned32):
    """Custom type mesShapingQueue based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_MesShapingQueue_Type.__name__ = "Unsigned32"
_MesShapingQueue_Object = MibTableColumn
mesShapingQueue = _MesShapingQueue_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 17, 1, 1, 5),
    _MesShapingQueue_Type()
)
mesShapingQueue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesShapingQueue.setStatus("current")


class _MesShapingInternalReference_Type(Unsigned32):
    """Custom type mesShapingInternalReference based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MesShapingInternalReference_Type.__name__ = "Unsigned32"
_MesShapingInternalReference_Object = MibTableColumn
mesShapingInternalReference = _MesShapingInternalReference_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 17, 1, 1, 6),
    _MesShapingInternalReference_Type()
)
mesShapingInternalReference.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesShapingInternalReference.setStatus("obsolete")


class _MesShapingExcess_Type(Integer32):
    """Custom type mesShapingExcess based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_MesShapingExcess_Type.__name__ = "Integer32"
_MesShapingExcess_Object = MibTableColumn
mesShapingExcess = _MesShapingExcess_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 17, 1, 1, 7),
    _MesShapingExcess_Type()
)
mesShapingExcess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mesShapingExcess.setStatus("current")


class _MesShapingIdentifier_Type(DisplayString):
    """Custom type mesShapingIdentifier based on DisplayString"""
    defaultValue = OctetString(" ")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 21),
    )


_MesShapingIdentifier_Type.__name__ = "DisplayString"
_MesShapingIdentifier_Object = MibTableColumn
mesShapingIdentifier = _MesShapingIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 17, 1, 1, 8),
    _MesShapingIdentifier_Type()
)
mesShapingIdentifier.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesShapingIdentifier.setStatus("current")


class _MesShapingMinRate_Type(Unsigned32):
    """Custom type mesShapingMinRate based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000000),
    )


_MesShapingMinRate_Type.__name__ = "Unsigned32"
_MesShapingMinRate_Object = MibTableColumn
mesShapingMinRate = _MesShapingMinRate_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 17, 1, 1, 9),
    _MesShapingMinRate_Type()
)
mesShapingMinRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mesShapingMinRate.setStatus("current")


class _MesShapingLocalId_Type(Integer32):
    """Custom type mesShapingLocalId based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_MesShapingLocalId_Type.__name__ = "Integer32"
_MesShapingLocalId_Object = MibTableColumn
mesShapingLocalId = _MesShapingLocalId_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 17, 1, 1, 10),
    _MesShapingLocalId_Type()
)
mesShapingLocalId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesShapingLocalId.setStatus("current")
_MesCosList_ObjectIdentity = ObjectIdentity
mesCosList = _MesCosList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 18)
)
_MesCosTable_Object = MibTable
mesCosTable = _MesCosTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 18, 1)
)
if mibBuilder.loadTexts:
    mesCosTable.setStatus("current")
_MesCosEntry_Object = MibTableRow
mesCosEntry = _MesCosEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 18, 1, 1)
)
mesCosEntry.setIndexNames(
    (0, "LUM-MES-MIB", "mesCosIndex"),
)
if mibBuilder.loadTexts:
    mesCosEntry.setStatus("current")


class _MesCosIndex_Type(Unsigned32):
    """Custom type mesCosIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_MesCosIndex_Type.__name__ = "Unsigned32"
_MesCosIndex_Object = MibTableColumn
mesCosIndex = _MesCosIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 18, 1, 1, 1),
    _MesCosIndex_Type()
)
mesCosIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesCosIndex.setStatus("current")
_MesCosName_Type = MgmtNameString
_MesCosName_Object = MibTableColumn
mesCosName = _MesCosName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 18, 1, 1, 2),
    _MesCosName_Type()
)
mesCosName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesCosName.setStatus("current")
_MesCosTxPort_Type = PortNumber
_MesCosTxPort_Object = MibTableColumn
mesCosTxPort = _MesCosTxPort_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 18, 1, 1, 3),
    _MesCosTxPort_Type()
)
mesCosTxPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesCosTxPort.setStatus("current")


class _MesCosMap_Type(Integer32):
    """Custom type mesCosMap based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_MesCosMap_Type.__name__ = "Integer32"
_MesCosMap_Object = MibTableColumn
mesCosMap = _MesCosMap_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 18, 1, 1, 4),
    _MesCosMap_Type()
)
mesCosMap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mesCosMap.setStatus("current")


class _MesCosPriority0_Type(Integer32):
    """Custom type mesCosPriority0 based on Integer32"""
    defaultValue = 1

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
              8)
        )
    )
    namedValues = NamedValues(
        *(("q1", 1),
          ("q2", 2),
          ("q3", 3),
          ("q4", 4),
          ("q5", 5),
          ("q6", 6),
          ("q7", 7),
          ("q8", 8))
    )


_MesCosPriority0_Type.__name__ = "Integer32"
_MesCosPriority0_Object = MibTableColumn
mesCosPriority0 = _MesCosPriority0_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 18, 1, 1, 5),
    _MesCosPriority0_Type()
)
mesCosPriority0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mesCosPriority0.setStatus("current")


class _MesCosPriority1_Type(Integer32):
    """Custom type mesCosPriority1 based on Integer32"""
    defaultValue = 1

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
              8)
        )
    )
    namedValues = NamedValues(
        *(("q1", 1),
          ("q2", 2),
          ("q3", 3),
          ("q4", 4),
          ("q5", 5),
          ("q6", 6),
          ("q7", 7),
          ("q8", 8))
    )


_MesCosPriority1_Type.__name__ = "Integer32"
_MesCosPriority1_Object = MibTableColumn
mesCosPriority1 = _MesCosPriority1_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 18, 1, 1, 6),
    _MesCosPriority1_Type()
)
mesCosPriority1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mesCosPriority1.setStatus("current")


class _MesCosPriority2_Type(Integer32):
    """Custom type mesCosPriority2 based on Integer32"""
    defaultValue = 1

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
              8)
        )
    )
    namedValues = NamedValues(
        *(("q1", 1),
          ("q2", 2),
          ("q3", 3),
          ("q4", 4),
          ("q5", 5),
          ("q6", 6),
          ("q7", 7),
          ("q8", 8))
    )


_MesCosPriority2_Type.__name__ = "Integer32"
_MesCosPriority2_Object = MibTableColumn
mesCosPriority2 = _MesCosPriority2_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 18, 1, 1, 7),
    _MesCosPriority2_Type()
)
mesCosPriority2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mesCosPriority2.setStatus("current")


class _MesCosPriority3_Type(Integer32):
    """Custom type mesCosPriority3 based on Integer32"""
    defaultValue = 1

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
              8)
        )
    )
    namedValues = NamedValues(
        *(("q1", 1),
          ("q2", 2),
          ("q3", 3),
          ("q4", 4),
          ("q5", 5),
          ("q6", 6),
          ("q7", 7),
          ("q8", 8))
    )


_MesCosPriority3_Type.__name__ = "Integer32"
_MesCosPriority3_Object = MibTableColumn
mesCosPriority3 = _MesCosPriority3_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 18, 1, 1, 8),
    _MesCosPriority3_Type()
)
mesCosPriority3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mesCosPriority3.setStatus("current")


class _MesCosPriority4_Type(Integer32):
    """Custom type mesCosPriority4 based on Integer32"""
    defaultValue = 1

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
              8)
        )
    )
    namedValues = NamedValues(
        *(("q1", 1),
          ("q2", 2),
          ("q3", 3),
          ("q4", 4),
          ("q5", 5),
          ("q6", 6),
          ("q7", 7),
          ("q8", 8))
    )


_MesCosPriority4_Type.__name__ = "Integer32"
_MesCosPriority4_Object = MibTableColumn
mesCosPriority4 = _MesCosPriority4_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 18, 1, 1, 9),
    _MesCosPriority4_Type()
)
mesCosPriority4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mesCosPriority4.setStatus("current")


class _MesCosPriority5_Type(Integer32):
    """Custom type mesCosPriority5 based on Integer32"""
    defaultValue = 1

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
              8)
        )
    )
    namedValues = NamedValues(
        *(("q1", 1),
          ("q2", 2),
          ("q3", 3),
          ("q4", 4),
          ("q5", 5),
          ("q6", 6),
          ("q7", 7),
          ("q8", 8))
    )


_MesCosPriority5_Type.__name__ = "Integer32"
_MesCosPriority5_Object = MibTableColumn
mesCosPriority5 = _MesCosPriority5_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 18, 1, 1, 10),
    _MesCosPriority5_Type()
)
mesCosPriority5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mesCosPriority5.setStatus("current")


class _MesCosPriority6_Type(Integer32):
    """Custom type mesCosPriority6 based on Integer32"""
    defaultValue = 1

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
              8)
        )
    )
    namedValues = NamedValues(
        *(("q1", 1),
          ("q2", 2),
          ("q3", 3),
          ("q4", 4),
          ("q5", 5),
          ("q6", 6),
          ("q7", 7),
          ("q8", 8))
    )


_MesCosPriority6_Type.__name__ = "Integer32"
_MesCosPriority6_Object = MibTableColumn
mesCosPriority6 = _MesCosPriority6_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 18, 1, 1, 11),
    _MesCosPriority6_Type()
)
mesCosPriority6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mesCosPriority6.setStatus("current")


class _MesCosPriority7_Type(Integer32):
    """Custom type mesCosPriority7 based on Integer32"""
    defaultValue = 1

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
              8)
        )
    )
    namedValues = NamedValues(
        *(("q1", 1),
          ("q2", 2),
          ("q3", 3),
          ("q4", 4),
          ("q5", 5),
          ("q6", 6),
          ("q7", 7),
          ("q8", 8))
    )


_MesCosPriority7_Type.__name__ = "Integer32"
_MesCosPriority7_Object = MibTableColumn
mesCosPriority7 = _MesCosPriority7_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 18, 1, 1, 12),
    _MesCosPriority7_Type()
)
mesCosPriority7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mesCosPriority7.setStatus("current")
_MesBwpMapList_ObjectIdentity = ObjectIdentity
mesBwpMapList = _MesBwpMapList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 19)
)
_MesBwpMapTable_Object = MibTable
mesBwpMapTable = _MesBwpMapTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 19, 1)
)
if mibBuilder.loadTexts:
    mesBwpMapTable.setStatus("current")
_MesBwpMapEntry_Object = MibTableRow
mesBwpMapEntry = _MesBwpMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 19, 1, 1)
)
mesBwpMapEntry.setIndexNames(
    (0, "LUM-MES-MIB", "mesBwpMapIndex"),
)
if mibBuilder.loadTexts:
    mesBwpMapEntry.setStatus("current")


class _MesBwpMapIndex_Type(Unsigned32):
    """Custom type mesBwpMapIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_MesBwpMapIndex_Type.__name__ = "Unsigned32"
_MesBwpMapIndex_Object = MibTableColumn
mesBwpMapIndex = _MesBwpMapIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 19, 1, 1, 1),
    _MesBwpMapIndex_Type()
)
mesBwpMapIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesBwpMapIndex.setStatus("current")
_MesBwpMapName_Type = MgmtNameString
_MesBwpMapName_Object = MibTableColumn
mesBwpMapName = _MesBwpMapName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 19, 1, 1, 2),
    _MesBwpMapName_Type()
)
mesBwpMapName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesBwpMapName.setStatus("current")
_MesBwpMapPortName_Type = MgmtNameString
_MesBwpMapPortName_Object = MibTableColumn
mesBwpMapPortName = _MesBwpMapPortName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 19, 1, 1, 3),
    _MesBwpMapPortName_Type()
)
mesBwpMapPortName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesBwpMapPortName.setStatus("current")
_MesBwpMapBwpName_Type = MgmtNameString
_MesBwpMapBwpName_Object = MibTableColumn
mesBwpMapBwpName = _MesBwpMapBwpName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 19, 1, 1, 4),
    _MesBwpMapBwpName_Type()
)
mesBwpMapBwpName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesBwpMapBwpName.setStatus("current")


class _MesBwpMapInternalReference_Type(Unsigned32):
    """Custom type mesBwpMapInternalReference based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MesBwpMapInternalReference_Type.__name__ = "Unsigned32"
_MesBwpMapInternalReference_Object = MibTableColumn
mesBwpMapInternalReference = _MesBwpMapInternalReference_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 19, 1, 1, 5),
    _MesBwpMapInternalReference_Type()
)
mesBwpMapInternalReference.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesBwpMapInternalReference.setStatus("current")
_MesMirroringList_ObjectIdentity = ObjectIdentity
mesMirroringList = _MesMirroringList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 20)
)
_MesMirroringTable_Object = MibTable
mesMirroringTable = _MesMirroringTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 20, 1)
)
if mibBuilder.loadTexts:
    mesMirroringTable.setStatus("current")
_MesMirroringEntry_Object = MibTableRow
mesMirroringEntry = _MesMirroringEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 20, 1, 1)
)
mesMirroringEntry.setIndexNames(
    (0, "LUM-MES-MIB", "mesMirroringIndex"),
)
if mibBuilder.loadTexts:
    mesMirroringEntry.setStatus("current")


class _MesMirroringIndex_Type(Unsigned32):
    """Custom type mesMirroringIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_MesMirroringIndex_Type.__name__ = "Unsigned32"
_MesMirroringIndex_Object = MibTableColumn
mesMirroringIndex = _MesMirroringIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 20, 1, 1, 1),
    _MesMirroringIndex_Type()
)
mesMirroringIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesMirroringIndex.setStatus("current")
_MesMirroringName_Type = MgmtNameString
_MesMirroringName_Object = MibTableColumn
mesMirroringName = _MesMirroringName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 20, 1, 1, 2),
    _MesMirroringName_Type()
)
mesMirroringName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesMirroringName.setStatus("current")


class _MesMirroringDestination_Type(Unsigned32):
    """Custom type mesMirroringDestination based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MesMirroringDestination_Type.__name__ = "Unsigned32"
_MesMirroringDestination_Object = MibTableColumn
mesMirroringDestination = _MesMirroringDestination_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 20, 1, 1, 3),
    _MesMirroringDestination_Type()
)
mesMirroringDestination.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesMirroringDestination.setStatus("current")


class _MesMirroringDirection_Type(Integer32):
    """Custom type mesMirroringDirection based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ingress", 1),
          ("egress", 2),
          ("both", 3))
    )


_MesMirroringDirection_Type.__name__ = "Integer32"
_MesMirroringDirection_Object = MibTableColumn
mesMirroringDirection = _MesMirroringDirection_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 20, 1, 1, 4),
    _MesMirroringDirection_Type()
)
mesMirroringDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mesMirroringDirection.setStatus("current")
_MesMirroringConfigureDestination_Type = CommandString
_MesMirroringConfigureDestination_Object = MibTableColumn
mesMirroringConfigureDestination = _MesMirroringConfigureDestination_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 20, 1, 1, 5),
    _MesMirroringConfigureDestination_Type()
)
mesMirroringConfigureDestination.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesMirroringConfigureDestination.setStatus("current")


class _MesMirroringDestInterface_Type(PortNumber):
    """Custom type mesMirroringDestInterface based on PortNumber"""
    defaultValue = 0


_MesMirroringDestInterface_Type.__name__ = "PortNumber"
_MesMirroringDestInterface_Object = MibTableColumn
mesMirroringDestInterface = _MesMirroringDestInterface_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 20, 1, 1, 6),
    _MesMirroringDestInterface_Type()
)
mesMirroringDestInterface.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesMirroringDestInterface.setStatus("current")


class _MesMirroringDestTxPort_Type(PortNumber):
    """Custom type mesMirroringDestTxPort based on PortNumber"""
    defaultValue = 0


_MesMirroringDestTxPort_Type.__name__ = "PortNumber"
_MesMirroringDestTxPort_Object = MibTableColumn
mesMirroringDestTxPort = _MesMirroringDestTxPort_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 20, 1, 1, 7),
    _MesMirroringDestTxPort_Type()
)
mesMirroringDestTxPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesMirroringDestTxPort.setStatus("current")


class _MesMirroringIfNo_Type(PortNumber):
    """Custom type mesMirroringIfNo based on PortNumber"""
    defaultValue = 1


_MesMirroringIfNo_Type.__name__ = "PortNumber"
_MesMirroringIfNo_Object = MibTableColumn
mesMirroringIfNo = _MesMirroringIfNo_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 20, 1, 1, 8),
    _MesMirroringIfNo_Type()
)
mesMirroringIfNo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesMirroringIfNo.setStatus("current")


class _MesMirroringTxPort_Type(PortNumber):
    """Custom type mesMirroringTxPort based on PortNumber"""
    defaultValue = 1


_MesMirroringTxPort_Type.__name__ = "PortNumber"
_MesMirroringTxPort_Object = MibTableColumn
mesMirroringTxPort = _MesMirroringTxPort_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 20, 1, 1, 9),
    _MesMirroringTxPort_Type()
)
mesMirroringTxPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesMirroringTxPort.setStatus("current")
_MesVlanTagRuleList_ObjectIdentity = ObjectIdentity
mesVlanTagRuleList = _MesVlanTagRuleList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 21)
)
_MesVlanTagRuleTable_Object = MibTable
mesVlanTagRuleTable = _MesVlanTagRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 21, 1)
)
if mibBuilder.loadTexts:
    mesVlanTagRuleTable.setStatus("current")
_MesVlanTagRuleEntry_Object = MibTableRow
mesVlanTagRuleEntry = _MesVlanTagRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 21, 1, 1)
)
mesVlanTagRuleEntry.setIndexNames(
    (0, "LUM-MES-MIB", "mesVlanTagRuleIndex"),
)
if mibBuilder.loadTexts:
    mesVlanTagRuleEntry.setStatus("current")


class _MesVlanTagRuleIndex_Type(Unsigned32):
    """Custom type mesVlanTagRuleIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_MesVlanTagRuleIndex_Type.__name__ = "Unsigned32"
_MesVlanTagRuleIndex_Object = MibTableColumn
mesVlanTagRuleIndex = _MesVlanTagRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 21, 1, 1, 1),
    _MesVlanTagRuleIndex_Type()
)
mesVlanTagRuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesVlanTagRuleIndex.setStatus("current")
_MesVlanTagRuleName_Type = MgmtNameString
_MesVlanTagRuleName_Object = MibTableColumn
mesVlanTagRuleName = _MesVlanTagRuleName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 21, 1, 1, 2),
    _MesVlanTagRuleName_Type()
)
mesVlanTagRuleName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesVlanTagRuleName.setStatus("current")


class _MesVlanTagRuleInternalReference_Type(Unsigned32):
    """Custom type mesVlanTagRuleInternalReference based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MesVlanTagRuleInternalReference_Type.__name__ = "Unsigned32"
_MesVlanTagRuleInternalReference_Object = MibTableColumn
mesVlanTagRuleInternalReference = _MesVlanTagRuleInternalReference_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 21, 1, 1, 3),
    _MesVlanTagRuleInternalReference_Type()
)
mesVlanTagRuleInternalReference.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesVlanTagRuleInternalReference.setStatus("current")


class _MesVlanTagRuleClassificationName_Type(DisplayString):
    """Custom type mesVlanTagRuleClassificationName based on DisplayString"""
    defaultValue = OctetString("")


_MesVlanTagRuleClassificationName_Type.__name__ = "DisplayString"
_MesVlanTagRuleClassificationName_Object = MibTableColumn
mesVlanTagRuleClassificationName = _MesVlanTagRuleClassificationName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 21, 1, 1, 4),
    _MesVlanTagRuleClassificationName_Type()
)
mesVlanTagRuleClassificationName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesVlanTagRuleClassificationName.setStatus("current")


class _MesVlanTagRuleType_Type(Integer32):
    """Custom type mesVlanTagRuleType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ingress", 1),
          ("egress", 2),
          ("queue", 3))
    )


_MesVlanTagRuleType_Type.__name__ = "Integer32"
_MesVlanTagRuleType_Object = MibTableColumn
mesVlanTagRuleType = _MesVlanTagRuleType_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 21, 1, 1, 5),
    _MesVlanTagRuleType_Type()
)
mesVlanTagRuleType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesVlanTagRuleType.setStatus("current")


class _MesVlanTagRuleOperation_Type(Integer32):
    """Custom type mesVlanTagRuleOperation based on Integer32"""
    defaultValue = 1

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
        *(("none", 1),
          ("pop", 2),
          ("push", 3),
          ("swap", 4),
          ("pushPush", 5),
          ("swapPush", 6),
          ("swapSwap", 7),
          ("popPop", 8),
          ("popSwap", 9))
    )


_MesVlanTagRuleOperation_Type.__name__ = "Integer32"
_MesVlanTagRuleOperation_Object = MibTableColumn
mesVlanTagRuleOperation = _MesVlanTagRuleOperation_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 21, 1, 1, 6),
    _MesVlanTagRuleOperation_Type()
)
mesVlanTagRuleOperation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesVlanTagRuleOperation.setStatus("current")


class _MesVlanTagRuleInnerVlanId_Type(Unsigned32):
    """Custom type mesVlanTagRuleInnerVlanId based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )


_MesVlanTagRuleInnerVlanId_Type.__name__ = "Unsigned32"
_MesVlanTagRuleInnerVlanId_Object = MibTableColumn
mesVlanTagRuleInnerVlanId = _MesVlanTagRuleInnerVlanId_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 21, 1, 1, 7),
    _MesVlanTagRuleInnerVlanId_Type()
)
mesVlanTagRuleInnerVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mesVlanTagRuleInnerVlanId.setStatus("current")


class _MesVlanTagRuleInnerPrio_Type(Unsigned32):
    """Custom type mesVlanTagRuleInnerPrio based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_MesVlanTagRuleInnerPrio_Type.__name__ = "Unsigned32"
_MesVlanTagRuleInnerPrio_Object = MibTableColumn
mesVlanTagRuleInnerPrio = _MesVlanTagRuleInnerPrio_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 21, 1, 1, 8),
    _MesVlanTagRuleInnerPrio_Type()
)
mesVlanTagRuleInnerPrio.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mesVlanTagRuleInnerPrio.setStatus("current")


class _MesVlanTagRuleOuterVlanId_Type(Unsigned32):
    """Custom type mesVlanTagRuleOuterVlanId based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )


_MesVlanTagRuleOuterVlanId_Type.__name__ = "Unsigned32"
_MesVlanTagRuleOuterVlanId_Object = MibTableColumn
mesVlanTagRuleOuterVlanId = _MesVlanTagRuleOuterVlanId_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 21, 1, 1, 9),
    _MesVlanTagRuleOuterVlanId_Type()
)
mesVlanTagRuleOuterVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mesVlanTagRuleOuterVlanId.setStatus("current")


class _MesVlanTagRuleOuterPrio_Type(Unsigned32):
    """Custom type mesVlanTagRuleOuterPrio based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_MesVlanTagRuleOuterPrio_Type.__name__ = "Unsigned32"
_MesVlanTagRuleOuterPrio_Object = MibTableColumn
mesVlanTagRuleOuterPrio = _MesVlanTagRuleOuterPrio_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 21, 1, 1, 10),
    _MesVlanTagRuleOuterPrio_Type()
)
mesVlanTagRuleOuterPrio.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mesVlanTagRuleOuterPrio.setStatus("current")


class _MesVlanTagRulePrioAssignment_Type(Integer32):
    """Custom type mesVlanTagRulePrioAssignment based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("set", 1),
          ("copy", 2),
          ("none", 3))
    )


_MesVlanTagRulePrioAssignment_Type.__name__ = "Integer32"
_MesVlanTagRulePrioAssignment_Object = MibTableColumn
mesVlanTagRulePrioAssignment = _MesVlanTagRulePrioAssignment_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 21, 1, 1, 11),
    _MesVlanTagRulePrioAssignment_Type()
)
mesVlanTagRulePrioAssignment.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesVlanTagRulePrioAssignment.setStatus("current")
_MesVlanTagRuleConfigurePrioAssignment_Type = CommandString
_MesVlanTagRuleConfigurePrioAssignment_Object = MibTableColumn
mesVlanTagRuleConfigurePrioAssignment = _MesVlanTagRuleConfigurePrioAssignment_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 21, 1, 1, 12),
    _MesVlanTagRuleConfigurePrioAssignment_Type()
)
mesVlanTagRuleConfigurePrioAssignment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesVlanTagRuleConfigurePrioAssignment.setStatus("current")


class _MesVlanTagRuleQueue_Type(Unsigned32):
    """Custom type mesVlanTagRuleQueue based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_MesVlanTagRuleQueue_Type.__name__ = "Unsigned32"
_MesVlanTagRuleQueue_Object = MibTableColumn
mesVlanTagRuleQueue = _MesVlanTagRuleQueue_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 21, 1, 1, 13),
    _MesVlanTagRuleQueue_Type()
)
mesVlanTagRuleQueue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mesVlanTagRuleQueue.setStatus("current")
_MesVlanTagRuleRowStatus_Type = RowStatus
_MesVlanTagRuleRowStatus_Object = MibTableColumn
mesVlanTagRuleRowStatus = _MesVlanTagRuleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 21, 1, 1, 14),
    _MesVlanTagRuleRowStatus_Type()
)
mesVlanTagRuleRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesVlanTagRuleRowStatus.setStatus("current")


class _MesVlanTagRuleInterfaceName_Type(DisplayString):
    """Custom type mesVlanTagRuleInterfaceName based on DisplayString"""
    defaultValue = OctetString("")


_MesVlanTagRuleInterfaceName_Type.__name__ = "DisplayString"
_MesVlanTagRuleInterfaceName_Object = MibTableColumn
mesVlanTagRuleInterfaceName = _MesVlanTagRuleInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 21, 1, 1, 15),
    _MesVlanTagRuleInterfaceName_Type()
)
mesVlanTagRuleInterfaceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesVlanTagRuleInterfaceName.setStatus("current")
_MesVlanTagClassVlanList_ObjectIdentity = ObjectIdentity
mesVlanTagClassVlanList = _MesVlanTagClassVlanList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 22)
)
_MesVlanTagClassVlanTable_Object = MibTable
mesVlanTagClassVlanTable = _MesVlanTagClassVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 22, 1)
)
if mibBuilder.loadTexts:
    mesVlanTagClassVlanTable.setStatus("current")
_MesVlanTagClassVlanEntry_Object = MibTableRow
mesVlanTagClassVlanEntry = _MesVlanTagClassVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 22, 1, 1)
)
mesVlanTagClassVlanEntry.setIndexNames(
    (0, "LUM-MES-MIB", "mesVlanTagClassVlanIndex"),
)
if mibBuilder.loadTexts:
    mesVlanTagClassVlanEntry.setStatus("current")


class _MesVlanTagClassVlanIndex_Type(Unsigned32):
    """Custom type mesVlanTagClassVlanIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_MesVlanTagClassVlanIndex_Type.__name__ = "Unsigned32"
_MesVlanTagClassVlanIndex_Object = MibTableColumn
mesVlanTagClassVlanIndex = _MesVlanTagClassVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 22, 1, 1, 1),
    _MesVlanTagClassVlanIndex_Type()
)
mesVlanTagClassVlanIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesVlanTagClassVlanIndex.setStatus("current")
_MesVlanTagClassVlanName_Type = MgmtNameString
_MesVlanTagClassVlanName_Object = MibTableColumn
mesVlanTagClassVlanName = _MesVlanTagClassVlanName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 22, 1, 1, 2),
    _MesVlanTagClassVlanName_Type()
)
mesVlanTagClassVlanName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesVlanTagClassVlanName.setStatus("current")
_MesVlanTagClassVlanTxPort_Type = PortNumber
_MesVlanTagClassVlanTxPort_Object = MibTableColumn
mesVlanTagClassVlanTxPort = _MesVlanTagClassVlanTxPort_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 22, 1, 1, 3),
    _MesVlanTagClassVlanTxPort_Type()
)
mesVlanTagClassVlanTxPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesVlanTagClassVlanTxPort.setStatus("current")


class _MesVlanTagClassVlanInternalReference_Type(Unsigned32):
    """Custom type mesVlanTagClassVlanInternalReference based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MesVlanTagClassVlanInternalReference_Type.__name__ = "Unsigned32"
_MesVlanTagClassVlanInternalReference_Object = MibTableColumn
mesVlanTagClassVlanInternalReference = _MesVlanTagClassVlanInternalReference_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 22, 1, 1, 4),
    _MesVlanTagClassVlanInternalReference_Type()
)
mesVlanTagClassVlanInternalReference.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesVlanTagClassVlanInternalReference.setStatus("current")


class _MesVlanTagClassVlanRuleName_Type(DisplayString):
    """Custom type mesVlanTagClassVlanRuleName based on DisplayString"""
    defaultValue = OctetString("")


_MesVlanTagClassVlanRuleName_Type.__name__ = "DisplayString"
_MesVlanTagClassVlanRuleName_Object = MibTableColumn
mesVlanTagClassVlanRuleName = _MesVlanTagClassVlanRuleName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 22, 1, 1, 5),
    _MesVlanTagClassVlanRuleName_Type()
)
mesVlanTagClassVlanRuleName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesVlanTagClassVlanRuleName.setStatus("current")


class _MesVlanTagClassVlanRuleIndex_Type(Unsigned32):
    """Custom type mesVlanTagClassVlanRuleIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_MesVlanTagClassVlanRuleIndex_Type.__name__ = "Unsigned32"
_MesVlanTagClassVlanRuleIndex_Object = MibTableColumn
mesVlanTagClassVlanRuleIndex = _MesVlanTagClassVlanRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 22, 1, 1, 6),
    _MesVlanTagClassVlanRuleIndex_Type()
)
mesVlanTagClassVlanRuleIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesVlanTagClassVlanRuleIndex.setStatus("current")


class _MesVlanTagClassVlanOuterVlanId_Type(Integer32):
    """Custom type mesVlanTagClassVlanOuterVlanId based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 4094),
    )


_MesVlanTagClassVlanOuterVlanId_Type.__name__ = "Integer32"
_MesVlanTagClassVlanOuterVlanId_Object = MibTableColumn
mesVlanTagClassVlanOuterVlanId = _MesVlanTagClassVlanOuterVlanId_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 22, 1, 1, 7),
    _MesVlanTagClassVlanOuterVlanId_Type()
)
mesVlanTagClassVlanOuterVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesVlanTagClassVlanOuterVlanId.setStatus("current")


class _MesVlanTagClassVlanLagIndex_Type(Unsigned32):
    """Custom type mesVlanTagClassVlanLagIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MesVlanTagClassVlanLagIndex_Type.__name__ = "Unsigned32"
_MesVlanTagClassVlanLagIndex_Object = MibTableColumn
mesVlanTagClassVlanLagIndex = _MesVlanTagClassVlanLagIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 22, 1, 1, 8),
    _MesVlanTagClassVlanLagIndex_Type()
)
mesVlanTagClassVlanLagIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesVlanTagClassVlanLagIndex.setStatus("current")


class _MesVlanTagClassVlanResourceType_Type(Integer32):
    """Custom type mesVlanTagClassVlanResourceType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("port", 1),
          ("lag", 2))
    )


_MesVlanTagClassVlanResourceType_Type.__name__ = "Integer32"
_MesVlanTagClassVlanResourceType_Object = MibTableColumn
mesVlanTagClassVlanResourceType = _MesVlanTagClassVlanResourceType_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 22, 1, 1, 9),
    _MesVlanTagClassVlanResourceType_Type()
)
mesVlanTagClassVlanResourceType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesVlanTagClassVlanResourceType.setStatus("current")


class _MesVlanTagClassVlanIfNo_Type(PortNumber):
    """Custom type mesVlanTagClassVlanIfNo based on PortNumber"""
    defaultValue = 1


_MesVlanTagClassVlanIfNo_Type.__name__ = "PortNumber"
_MesVlanTagClassVlanIfNo_Object = MibTableColumn
mesVlanTagClassVlanIfNo = _MesVlanTagClassVlanIfNo_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 22, 1, 1, 10),
    _MesVlanTagClassVlanIfNo_Type()
)
mesVlanTagClassVlanIfNo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesVlanTagClassVlanIfNo.setStatus("current")


class _MesVlanTagClassVlanLocalId_Type(Integer32):
    """Custom type mesVlanTagClassVlanLocalId based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_MesVlanTagClassVlanLocalId_Type.__name__ = "Integer32"
_MesVlanTagClassVlanLocalId_Object = MibTableColumn
mesVlanTagClassVlanLocalId = _MesVlanTagClassVlanLocalId_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 22, 1, 1, 11),
    _MesVlanTagClassVlanLocalId_Type()
)
mesVlanTagClassVlanLocalId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesVlanTagClassVlanLocalId.setStatus("current")
_MesVlanTagClassVlanRowStatus_Type = RowStatus
_MesVlanTagClassVlanRowStatus_Object = MibTableColumn
mesVlanTagClassVlanRowStatus = _MesVlanTagClassVlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 22, 1, 1, 12),
    _MesVlanTagClassVlanRowStatus_Type()
)
mesVlanTagClassVlanRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesVlanTagClassVlanRowStatus.setStatus("current")
_MesCosProfileList_ObjectIdentity = ObjectIdentity
mesCosProfileList = _MesCosProfileList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 23)
)
_MesCosProfileTable_Object = MibTable
mesCosProfileTable = _MesCosProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 23, 1)
)
if mibBuilder.loadTexts:
    mesCosProfileTable.setStatus("current")
_MesCosProfileEntry_Object = MibTableRow
mesCosProfileEntry = _MesCosProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 23, 1, 1)
)
mesCosProfileEntry.setIndexNames(
    (0, "LUM-MES-MIB", "mesCosProfileIndex"),
)
if mibBuilder.loadTexts:
    mesCosProfileEntry.setStatus("current")


class _MesCosProfileIndex_Type(Unsigned32):
    """Custom type mesCosProfileIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_MesCosProfileIndex_Type.__name__ = "Unsigned32"
_MesCosProfileIndex_Object = MibTableColumn
mesCosProfileIndex = _MesCosProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 23, 1, 1, 1),
    _MesCosProfileIndex_Type()
)
mesCosProfileIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesCosProfileIndex.setStatus("current")
_MesCosProfileName_Type = MgmtNameString
_MesCosProfileName_Object = MibTableColumn
mesCosProfileName = _MesCosProfileName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 23, 1, 1, 2),
    _MesCosProfileName_Type()
)
mesCosProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesCosProfileName.setStatus("current")


class _MesCosProfilePortmask_Type(Unsigned32):
    """Custom type mesCosProfilePortmask based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MesCosProfilePortmask_Type.__name__ = "Unsigned32"
_MesCosProfilePortmask_Object = MibTableColumn
mesCosProfilePortmask = _MesCosProfilePortmask_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 23, 1, 1, 3),
    _MesCosProfilePortmask_Type()
)
mesCosProfilePortmask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesCosProfilePortmask.setStatus("current")


class _MesCosProfileScheduler_Type(Integer32):
    """Custom type mesCosProfileScheduler based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("strict", 1),
          ("rr", 2),
          ("wrr", 3))
    )


_MesCosProfileScheduler_Type.__name__ = "Integer32"
_MesCosProfileScheduler_Object = MibTableColumn
mesCosProfileScheduler = _MesCosProfileScheduler_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 23, 1, 1, 4),
    _MesCosProfileScheduler_Type()
)
mesCosProfileScheduler.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesCosProfileScheduler.setStatus("current")


class _MesCosProfileWeight0_Type(Unsigned32):
    """Custom type mesCosProfileWeight0 based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_MesCosProfileWeight0_Type.__name__ = "Unsigned32"
_MesCosProfileWeight0_Object = MibTableColumn
mesCosProfileWeight0 = _MesCosProfileWeight0_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 23, 1, 1, 5),
    _MesCosProfileWeight0_Type()
)
mesCosProfileWeight0.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesCosProfileWeight0.setStatus("current")


class _MesCosProfileWeight1_Type(Unsigned32):
    """Custom type mesCosProfileWeight1 based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_MesCosProfileWeight1_Type.__name__ = "Unsigned32"
_MesCosProfileWeight1_Object = MibTableColumn
mesCosProfileWeight1 = _MesCosProfileWeight1_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 23, 1, 1, 6),
    _MesCosProfileWeight1_Type()
)
mesCosProfileWeight1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesCosProfileWeight1.setStatus("current")


class _MesCosProfileWeight2_Type(Unsigned32):
    """Custom type mesCosProfileWeight2 based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_MesCosProfileWeight2_Type.__name__ = "Unsigned32"
_MesCosProfileWeight2_Object = MibTableColumn
mesCosProfileWeight2 = _MesCosProfileWeight2_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 23, 1, 1, 7),
    _MesCosProfileWeight2_Type()
)
mesCosProfileWeight2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesCosProfileWeight2.setStatus("current")


class _MesCosProfileWeight3_Type(Unsigned32):
    """Custom type mesCosProfileWeight3 based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_MesCosProfileWeight3_Type.__name__ = "Unsigned32"
_MesCosProfileWeight3_Object = MibTableColumn
mesCosProfileWeight3 = _MesCosProfileWeight3_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 23, 1, 1, 8),
    _MesCosProfileWeight3_Type()
)
mesCosProfileWeight3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesCosProfileWeight3.setStatus("current")


class _MesCosProfileWeight4_Type(Unsigned32):
    """Custom type mesCosProfileWeight4 based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_MesCosProfileWeight4_Type.__name__ = "Unsigned32"
_MesCosProfileWeight4_Object = MibTableColumn
mesCosProfileWeight4 = _MesCosProfileWeight4_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 23, 1, 1, 9),
    _MesCosProfileWeight4_Type()
)
mesCosProfileWeight4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesCosProfileWeight4.setStatus("current")


class _MesCosProfileWeight5_Type(Unsigned32):
    """Custom type mesCosProfileWeight5 based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_MesCosProfileWeight5_Type.__name__ = "Unsigned32"
_MesCosProfileWeight5_Object = MibTableColumn
mesCosProfileWeight5 = _MesCosProfileWeight5_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 23, 1, 1, 10),
    _MesCosProfileWeight5_Type()
)
mesCosProfileWeight5.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesCosProfileWeight5.setStatus("current")


class _MesCosProfileWeight6_Type(Unsigned32):
    """Custom type mesCosProfileWeight6 based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_MesCosProfileWeight6_Type.__name__ = "Unsigned32"
_MesCosProfileWeight6_Object = MibTableColumn
mesCosProfileWeight6 = _MesCosProfileWeight6_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 23, 1, 1, 11),
    _MesCosProfileWeight6_Type()
)
mesCosProfileWeight6.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesCosProfileWeight6.setStatus("current")


class _MesCosProfileWeight7_Type(Unsigned32):
    """Custom type mesCosProfileWeight7 based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_MesCosProfileWeight7_Type.__name__ = "Unsigned32"
_MesCosProfileWeight7_Object = MibTableColumn
mesCosProfileWeight7 = _MesCosProfileWeight7_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 23, 1, 1, 12),
    _MesCosProfileWeight7_Type()
)
mesCosProfileWeight7.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesCosProfileWeight7.setStatus("current")


class _MesCosProfilePriority0_Type(Integer32):
    """Custom type mesCosProfilePriority0 based on Integer32"""
    defaultValue = 1

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
              8)
        )
    )
    namedValues = NamedValues(
        *(("q1", 1),
          ("q2", 2),
          ("q3", 3),
          ("q4", 4),
          ("q5", 5),
          ("q6", 6),
          ("q7", 7),
          ("q8", 8))
    )


_MesCosProfilePriority0_Type.__name__ = "Integer32"
_MesCosProfilePriority0_Object = MibTableColumn
mesCosProfilePriority0 = _MesCosProfilePriority0_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 23, 1, 1, 13),
    _MesCosProfilePriority0_Type()
)
mesCosProfilePriority0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mesCosProfilePriority0.setStatus("current")


class _MesCosProfilePriority1_Type(Integer32):
    """Custom type mesCosProfilePriority1 based on Integer32"""
    defaultValue = 2

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
              8)
        )
    )
    namedValues = NamedValues(
        *(("q1", 1),
          ("q2", 2),
          ("q3", 3),
          ("q4", 4),
          ("q5", 5),
          ("q6", 6),
          ("q7", 7),
          ("q8", 8))
    )


_MesCosProfilePriority1_Type.__name__ = "Integer32"
_MesCosProfilePriority1_Object = MibTableColumn
mesCosProfilePriority1 = _MesCosProfilePriority1_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 23, 1, 1, 14),
    _MesCosProfilePriority1_Type()
)
mesCosProfilePriority1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mesCosProfilePriority1.setStatus("current")


class _MesCosProfilePriority2_Type(Integer32):
    """Custom type mesCosProfilePriority2 based on Integer32"""
    defaultValue = 3

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
              8)
        )
    )
    namedValues = NamedValues(
        *(("q1", 1),
          ("q2", 2),
          ("q3", 3),
          ("q4", 4),
          ("q5", 5),
          ("q6", 6),
          ("q7", 7),
          ("q8", 8))
    )


_MesCosProfilePriority2_Type.__name__ = "Integer32"
_MesCosProfilePriority2_Object = MibTableColumn
mesCosProfilePriority2 = _MesCosProfilePriority2_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 23, 1, 1, 15),
    _MesCosProfilePriority2_Type()
)
mesCosProfilePriority2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mesCosProfilePriority2.setStatus("current")


class _MesCosProfilePriority3_Type(Integer32):
    """Custom type mesCosProfilePriority3 based on Integer32"""
    defaultValue = 4

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
              8)
        )
    )
    namedValues = NamedValues(
        *(("q1", 1),
          ("q2", 2),
          ("q3", 3),
          ("q4", 4),
          ("q5", 5),
          ("q6", 6),
          ("q7", 7),
          ("q8", 8))
    )


_MesCosProfilePriority3_Type.__name__ = "Integer32"
_MesCosProfilePriority3_Object = MibTableColumn
mesCosProfilePriority3 = _MesCosProfilePriority3_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 23, 1, 1, 16),
    _MesCosProfilePriority3_Type()
)
mesCosProfilePriority3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mesCosProfilePriority3.setStatus("current")


class _MesCosProfilePriority4_Type(Integer32):
    """Custom type mesCosProfilePriority4 based on Integer32"""
    defaultValue = 5

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
              8)
        )
    )
    namedValues = NamedValues(
        *(("q1", 1),
          ("q2", 2),
          ("q3", 3),
          ("q4", 4),
          ("q5", 5),
          ("q6", 6),
          ("q7", 7),
          ("q8", 8))
    )


_MesCosProfilePriority4_Type.__name__ = "Integer32"
_MesCosProfilePriority4_Object = MibTableColumn
mesCosProfilePriority4 = _MesCosProfilePriority4_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 23, 1, 1, 17),
    _MesCosProfilePriority4_Type()
)
mesCosProfilePriority4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mesCosProfilePriority4.setStatus("current")


class _MesCosProfilePriority5_Type(Integer32):
    """Custom type mesCosProfilePriority5 based on Integer32"""
    defaultValue = 6

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
              8)
        )
    )
    namedValues = NamedValues(
        *(("q1", 1),
          ("q2", 2),
          ("q3", 3),
          ("q4", 4),
          ("q5", 5),
          ("q6", 6),
          ("q7", 7),
          ("q8", 8))
    )


_MesCosProfilePriority5_Type.__name__ = "Integer32"
_MesCosProfilePriority5_Object = MibTableColumn
mesCosProfilePriority5 = _MesCosProfilePriority5_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 23, 1, 1, 18),
    _MesCosProfilePriority5_Type()
)
mesCosProfilePriority5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mesCosProfilePriority5.setStatus("current")


class _MesCosProfilePriority6_Type(Integer32):
    """Custom type mesCosProfilePriority6 based on Integer32"""
    defaultValue = 7

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
              8)
        )
    )
    namedValues = NamedValues(
        *(("q1", 1),
          ("q2", 2),
          ("q3", 3),
          ("q4", 4),
          ("q5", 5),
          ("q6", 6),
          ("q7", 7),
          ("q8", 8))
    )


_MesCosProfilePriority6_Type.__name__ = "Integer32"
_MesCosProfilePriority6_Object = MibTableColumn
mesCosProfilePriority6 = _MesCosProfilePriority6_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 23, 1, 1, 19),
    _MesCosProfilePriority6_Type()
)
mesCosProfilePriority6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mesCosProfilePriority6.setStatus("current")


class _MesCosProfilePriority7_Type(Integer32):
    """Custom type mesCosProfilePriority7 based on Integer32"""
    defaultValue = 8

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
              8)
        )
    )
    namedValues = NamedValues(
        *(("q1", 1),
          ("q2", 2),
          ("q3", 3),
          ("q4", 4),
          ("q5", 5),
          ("q6", 6),
          ("q7", 7),
          ("q8", 8))
    )


_MesCosProfilePriority7_Type.__name__ = "Integer32"
_MesCosProfilePriority7_Object = MibTableColumn
mesCosProfilePriority7 = _MesCosProfilePriority7_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 23, 1, 1, 20),
    _MesCosProfilePriority7_Type()
)
mesCosProfilePriority7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mesCosProfilePriority7.setStatus("current")
_MesCosProfileConfigureScheduler_Type = CommandString
_MesCosProfileConfigureScheduler_Object = MibTableColumn
mesCosProfileConfigureScheduler = _MesCosProfileConfigureScheduler_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 23, 1, 1, 21),
    _MesCosProfileConfigureScheduler_Type()
)
mesCosProfileConfigureScheduler.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesCosProfileConfigureScheduler.setStatus("current")


class _MesCosProfileIngressPcpDecoding_Type(Integer32):
    """Custom type mesCosProfileIngressPcpDecoding based on Integer32"""
    defaultValue = 1

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
        *(("disabled", 1),
          ("userDefined", 2),
          ("pcp8P0D", 3),
          ("pcp7P1D", 4),
          ("pcp6P2D", 5),
          ("pcp5P3D", 6))
    )


_MesCosProfileIngressPcpDecoding_Type.__name__ = "Integer32"
_MesCosProfileIngressPcpDecoding_Object = MibTableColumn
mesCosProfileIngressPcpDecoding = _MesCosProfileIngressPcpDecoding_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 23, 1, 1, 22),
    _MesCosProfileIngressPcpDecoding_Type()
)
mesCosProfileIngressPcpDecoding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mesCosProfileIngressPcpDecoding.setStatus("current")


class _MesCosProfileIngressDeiDecoding_Type(Integer32):
    """Custom type mesCosProfileIngressDeiDecoding based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_MesCosProfileIngressDeiDecoding_Type.__name__ = "Integer32"
_MesCosProfileIngressDeiDecoding_Object = MibTableColumn
mesCosProfileIngressDeiDecoding = _MesCosProfileIngressDeiDecoding_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 23, 1, 1, 23),
    _MesCosProfileIngressDeiDecoding_Type()
)
mesCosProfileIngressDeiDecoding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mesCosProfileIngressDeiDecoding.setStatus("current")


class _MesCosProfileIngressColor0_Type(Integer32):
    """Custom type mesCosProfileIngressColor0 based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("green", 1),
          ("yellow", 2))
    )


_MesCosProfileIngressColor0_Type.__name__ = "Integer32"
_MesCosProfileIngressColor0_Object = MibTableColumn
mesCosProfileIngressColor0 = _MesCosProfileIngressColor0_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 23, 1, 1, 24),
    _MesCosProfileIngressColor0_Type()
)
mesCosProfileIngressColor0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mesCosProfileIngressColor0.setStatus("current")


class _MesCosProfileIngressColor1_Type(Integer32):
    """Custom type mesCosProfileIngressColor1 based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("green", 1),
          ("yellow", 2))
    )


_MesCosProfileIngressColor1_Type.__name__ = "Integer32"
_MesCosProfileIngressColor1_Object = MibTableColumn
mesCosProfileIngressColor1 = _MesCosProfileIngressColor1_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 23, 1, 1, 25),
    _MesCosProfileIngressColor1_Type()
)
mesCosProfileIngressColor1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mesCosProfileIngressColor1.setStatus("current")


class _MesCosProfileIngressColor2_Type(Integer32):
    """Custom type mesCosProfileIngressColor2 based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("green", 1),
          ("yellow", 2))
    )


_MesCosProfileIngressColor2_Type.__name__ = "Integer32"
_MesCosProfileIngressColor2_Object = MibTableColumn
mesCosProfileIngressColor2 = _MesCosProfileIngressColor2_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 23, 1, 1, 26),
    _MesCosProfileIngressColor2_Type()
)
mesCosProfileIngressColor2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mesCosProfileIngressColor2.setStatus("current")


class _MesCosProfileIngressColor3_Type(Integer32):
    """Custom type mesCosProfileIngressColor3 based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("green", 1),
          ("yellow", 2))
    )


_MesCosProfileIngressColor3_Type.__name__ = "Integer32"
_MesCosProfileIngressColor3_Object = MibTableColumn
mesCosProfileIngressColor3 = _MesCosProfileIngressColor3_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 23, 1, 1, 27),
    _MesCosProfileIngressColor3_Type()
)
mesCosProfileIngressColor3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mesCosProfileIngressColor3.setStatus("current")


class _MesCosProfileIngressColor4_Type(Integer32):
    """Custom type mesCosProfileIngressColor4 based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("green", 1),
          ("yellow", 2))
    )


_MesCosProfileIngressColor4_Type.__name__ = "Integer32"
_MesCosProfileIngressColor4_Object = MibTableColumn
mesCosProfileIngressColor4 = _MesCosProfileIngressColor4_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 23, 1, 1, 28),
    _MesCosProfileIngressColor4_Type()
)
mesCosProfileIngressColor4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mesCosProfileIngressColor4.setStatus("current")


class _MesCosProfileIngressColor5_Type(Integer32):
    """Custom type mesCosProfileIngressColor5 based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("green", 1),
          ("yellow", 2))
    )


_MesCosProfileIngressColor5_Type.__name__ = "Integer32"
_MesCosProfileIngressColor5_Object = MibTableColumn
mesCosProfileIngressColor5 = _MesCosProfileIngressColor5_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 23, 1, 1, 29),
    _MesCosProfileIngressColor5_Type()
)
mesCosProfileIngressColor5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mesCosProfileIngressColor5.setStatus("current")


class _MesCosProfileIngressColor6_Type(Integer32):
    """Custom type mesCosProfileIngressColor6 based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("green", 1),
          ("yellow", 2))
    )


_MesCosProfileIngressColor6_Type.__name__ = "Integer32"
_MesCosProfileIngressColor6_Object = MibTableColumn
mesCosProfileIngressColor6 = _MesCosProfileIngressColor6_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 23, 1, 1, 30),
    _MesCosProfileIngressColor6_Type()
)
mesCosProfileIngressColor6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mesCosProfileIngressColor6.setStatus("current")


class _MesCosProfileIngressColor7_Type(Integer32):
    """Custom type mesCosProfileIngressColor7 based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("green", 1),
          ("yellow", 2))
    )


_MesCosProfileIngressColor7_Type.__name__ = "Integer32"
_MesCosProfileIngressColor7_Object = MibTableColumn
mesCosProfileIngressColor7 = _MesCosProfileIngressColor7_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 23, 1, 1, 31),
    _MesCosProfileIngressColor7_Type()
)
mesCosProfileIngressColor7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mesCosProfileIngressColor7.setStatus("current")


class _MesCosProfileEgressPcpEncoding_Type(Integer32):
    """Custom type mesCosProfileEgressPcpEncoding based on Integer32"""
    defaultValue = 1

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
        *(("disabled", 1),
          ("userDefined", 2),
          ("pcp8P0D", 3),
          ("pcp7P1D", 4),
          ("pcp6P2D", 5),
          ("pcp5P3D", 6))
    )


_MesCosProfileEgressPcpEncoding_Type.__name__ = "Integer32"
_MesCosProfileEgressPcpEncoding_Object = MibTableColumn
mesCosProfileEgressPcpEncoding = _MesCosProfileEgressPcpEncoding_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 23, 1, 1, 32),
    _MesCosProfileEgressPcpEncoding_Type()
)
mesCosProfileEgressPcpEncoding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mesCosProfileEgressPcpEncoding.setStatus("current")


class _MesCosProfileEgressDeiEncoding_Type(Integer32):
    """Custom type mesCosProfileEgressDeiEncoding based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_MesCosProfileEgressDeiEncoding_Type.__name__ = "Integer32"
_MesCosProfileEgressDeiEncoding_Object = MibTableColumn
mesCosProfileEgressDeiEncoding = _MesCosProfileEgressDeiEncoding_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 23, 1, 1, 33),
    _MesCosProfileEgressDeiEncoding_Type()
)
mesCosProfileEgressDeiEncoding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mesCosProfileEgressDeiEncoding.setStatus("current")


class _MesCosProfileEgressPcpGreen0_Type(Unsigned32):
    """Custom type mesCosProfileEgressPcpGreen0 based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_MesCosProfileEgressPcpGreen0_Type.__name__ = "Unsigned32"
_MesCosProfileEgressPcpGreen0_Object = MibTableColumn
mesCosProfileEgressPcpGreen0 = _MesCosProfileEgressPcpGreen0_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 23, 1, 1, 34),
    _MesCosProfileEgressPcpGreen0_Type()
)
mesCosProfileEgressPcpGreen0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mesCosProfileEgressPcpGreen0.setStatus("current")


class _MesCosProfileEgressPcpGreen1_Type(Unsigned32):
    """Custom type mesCosProfileEgressPcpGreen1 based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_MesCosProfileEgressPcpGreen1_Type.__name__ = "Unsigned32"
_MesCosProfileEgressPcpGreen1_Object = MibTableColumn
mesCosProfileEgressPcpGreen1 = _MesCosProfileEgressPcpGreen1_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 23, 1, 1, 35),
    _MesCosProfileEgressPcpGreen1_Type()
)
mesCosProfileEgressPcpGreen1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mesCosProfileEgressPcpGreen1.setStatus("current")


class _MesCosProfileEgressPcpGreen2_Type(Unsigned32):
    """Custom type mesCosProfileEgressPcpGreen2 based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_MesCosProfileEgressPcpGreen2_Type.__name__ = "Unsigned32"
_MesCosProfileEgressPcpGreen2_Object = MibTableColumn
mesCosProfileEgressPcpGreen2 = _MesCosProfileEgressPcpGreen2_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 23, 1, 1, 36),
    _MesCosProfileEgressPcpGreen2_Type()
)
mesCosProfileEgressPcpGreen2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mesCosProfileEgressPcpGreen2.setStatus("current")


class _MesCosProfileEgressPcpGreen3_Type(Unsigned32):
    """Custom type mesCosProfileEgressPcpGreen3 based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_MesCosProfileEgressPcpGreen3_Type.__name__ = "Unsigned32"
_MesCosProfileEgressPcpGreen3_Object = MibTableColumn
mesCosProfileEgressPcpGreen3 = _MesCosProfileEgressPcpGreen3_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 23, 1, 1, 37),
    _MesCosProfileEgressPcpGreen3_Type()
)
mesCosProfileEgressPcpGreen3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mesCosProfileEgressPcpGreen3.setStatus("current")


class _MesCosProfileEgressPcpGreen4_Type(Unsigned32):
    """Custom type mesCosProfileEgressPcpGreen4 based on Unsigned32"""
    defaultValue = 4

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_MesCosProfileEgressPcpGreen4_Type.__name__ = "Unsigned32"
_MesCosProfileEgressPcpGreen4_Object = MibTableColumn
mesCosProfileEgressPcpGreen4 = _MesCosProfileEgressPcpGreen4_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 23, 1, 1, 38),
    _MesCosProfileEgressPcpGreen4_Type()
)
mesCosProfileEgressPcpGreen4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mesCosProfileEgressPcpGreen4.setStatus("current")


class _MesCosProfileEgressPcpGreen5_Type(Unsigned32):
    """Custom type mesCosProfileEgressPcpGreen5 based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_MesCosProfileEgressPcpGreen5_Type.__name__ = "Unsigned32"
_MesCosProfileEgressPcpGreen5_Object = MibTableColumn
mesCosProfileEgressPcpGreen5 = _MesCosProfileEgressPcpGreen5_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 23, 1, 1, 39),
    _MesCosProfileEgressPcpGreen5_Type()
)
mesCosProfileEgressPcpGreen5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mesCosProfileEgressPcpGreen5.setStatus("current")


class _MesCosProfileEgressPcpGreen6_Type(Unsigned32):
    """Custom type mesCosProfileEgressPcpGreen6 based on Unsigned32"""
    defaultValue = 6

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_MesCosProfileEgressPcpGreen6_Type.__name__ = "Unsigned32"
_MesCosProfileEgressPcpGreen6_Object = MibTableColumn
mesCosProfileEgressPcpGreen6 = _MesCosProfileEgressPcpGreen6_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 23, 1, 1, 40),
    _MesCosProfileEgressPcpGreen6_Type()
)
mesCosProfileEgressPcpGreen6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mesCosProfileEgressPcpGreen6.setStatus("current")


class _MesCosProfileEgressPcpGreen7_Type(Unsigned32):
    """Custom type mesCosProfileEgressPcpGreen7 based on Unsigned32"""
    defaultValue = 7

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_MesCosProfileEgressPcpGreen7_Type.__name__ = "Unsigned32"
_MesCosProfileEgressPcpGreen7_Object = MibTableColumn
mesCosProfileEgressPcpGreen7 = _MesCosProfileEgressPcpGreen7_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 23, 1, 1, 41),
    _MesCosProfileEgressPcpGreen7_Type()
)
mesCosProfileEgressPcpGreen7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mesCosProfileEgressPcpGreen7.setStatus("current")


class _MesCosProfileEgressPcpYellow0_Type(Unsigned32):
    """Custom type mesCosProfileEgressPcpYellow0 based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_MesCosProfileEgressPcpYellow0_Type.__name__ = "Unsigned32"
_MesCosProfileEgressPcpYellow0_Object = MibTableColumn
mesCosProfileEgressPcpYellow0 = _MesCosProfileEgressPcpYellow0_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 23, 1, 1, 42),
    _MesCosProfileEgressPcpYellow0_Type()
)
mesCosProfileEgressPcpYellow0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mesCosProfileEgressPcpYellow0.setStatus("current")


class _MesCosProfileEgressPcpYellow1_Type(Unsigned32):
    """Custom type mesCosProfileEgressPcpYellow1 based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_MesCosProfileEgressPcpYellow1_Type.__name__ = "Unsigned32"
_MesCosProfileEgressPcpYellow1_Object = MibTableColumn
mesCosProfileEgressPcpYellow1 = _MesCosProfileEgressPcpYellow1_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 23, 1, 1, 43),
    _MesCosProfileEgressPcpYellow1_Type()
)
mesCosProfileEgressPcpYellow1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mesCosProfileEgressPcpYellow1.setStatus("current")


class _MesCosProfileEgressPcpYellow2_Type(Unsigned32):
    """Custom type mesCosProfileEgressPcpYellow2 based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_MesCosProfileEgressPcpYellow2_Type.__name__ = "Unsigned32"
_MesCosProfileEgressPcpYellow2_Object = MibTableColumn
mesCosProfileEgressPcpYellow2 = _MesCosProfileEgressPcpYellow2_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 23, 1, 1, 44),
    _MesCosProfileEgressPcpYellow2_Type()
)
mesCosProfileEgressPcpYellow2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mesCosProfileEgressPcpYellow2.setStatus("current")


class _MesCosProfileEgressPcpYellow3_Type(Unsigned32):
    """Custom type mesCosProfileEgressPcpYellow3 based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_MesCosProfileEgressPcpYellow3_Type.__name__ = "Unsigned32"
_MesCosProfileEgressPcpYellow3_Object = MibTableColumn
mesCosProfileEgressPcpYellow3 = _MesCosProfileEgressPcpYellow3_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 23, 1, 1, 45),
    _MesCosProfileEgressPcpYellow3_Type()
)
mesCosProfileEgressPcpYellow3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mesCosProfileEgressPcpYellow3.setStatus("current")


class _MesCosProfileEgressPcpYellow4_Type(Unsigned32):
    """Custom type mesCosProfileEgressPcpYellow4 based on Unsigned32"""
    defaultValue = 4

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_MesCosProfileEgressPcpYellow4_Type.__name__ = "Unsigned32"
_MesCosProfileEgressPcpYellow4_Object = MibTableColumn
mesCosProfileEgressPcpYellow4 = _MesCosProfileEgressPcpYellow4_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 23, 1, 1, 46),
    _MesCosProfileEgressPcpYellow4_Type()
)
mesCosProfileEgressPcpYellow4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mesCosProfileEgressPcpYellow4.setStatus("current")


class _MesCosProfileEgressPcpYellow5_Type(Unsigned32):
    """Custom type mesCosProfileEgressPcpYellow5 based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_MesCosProfileEgressPcpYellow5_Type.__name__ = "Unsigned32"
_MesCosProfileEgressPcpYellow5_Object = MibTableColumn
mesCosProfileEgressPcpYellow5 = _MesCosProfileEgressPcpYellow5_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 23, 1, 1, 47),
    _MesCosProfileEgressPcpYellow5_Type()
)
mesCosProfileEgressPcpYellow5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mesCosProfileEgressPcpYellow5.setStatus("current")


class _MesCosProfileEgressPcpYellow6_Type(Unsigned32):
    """Custom type mesCosProfileEgressPcpYellow6 based on Unsigned32"""
    defaultValue = 6

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_MesCosProfileEgressPcpYellow6_Type.__name__ = "Unsigned32"
_MesCosProfileEgressPcpYellow6_Object = MibTableColumn
mesCosProfileEgressPcpYellow6 = _MesCosProfileEgressPcpYellow6_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 23, 1, 1, 48),
    _MesCosProfileEgressPcpYellow6_Type()
)
mesCosProfileEgressPcpYellow6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mesCosProfileEgressPcpYellow6.setStatus("current")


class _MesCosProfileEgressPcpYellow7_Type(Unsigned32):
    """Custom type mesCosProfileEgressPcpYellow7 based on Unsigned32"""
    defaultValue = 7

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_MesCosProfileEgressPcpYellow7_Type.__name__ = "Unsigned32"
_MesCosProfileEgressPcpYellow7_Object = MibTableColumn
mesCosProfileEgressPcpYellow7 = _MesCosProfileEgressPcpYellow7_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 23, 1, 1, 49),
    _MesCosProfileEgressPcpYellow7_Type()
)
mesCosProfileEgressPcpYellow7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mesCosProfileEgressPcpYellow7.setStatus("current")


class _MesCosProfilePortmaskIf1_Type(Unsigned32):
    """Custom type mesCosProfilePortmaskIf1 based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MesCosProfilePortmaskIf1_Type.__name__ = "Unsigned32"
_MesCosProfilePortmaskIf1_Object = MibTableColumn
mesCosProfilePortmaskIf1 = _MesCosProfilePortmaskIf1_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 23, 1, 1, 50),
    _MesCosProfilePortmaskIf1_Type()
)
mesCosProfilePortmaskIf1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesCosProfilePortmaskIf1.setStatus("current")


class _MesCosProfilePortmaskIf2_Type(Unsigned32):
    """Custom type mesCosProfilePortmaskIf2 based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MesCosProfilePortmaskIf2_Type.__name__ = "Unsigned32"
_MesCosProfilePortmaskIf2_Object = MibTableColumn
mesCosProfilePortmaskIf2 = _MesCosProfilePortmaskIf2_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 23, 1, 1, 51),
    _MesCosProfilePortmaskIf2_Type()
)
mesCosProfilePortmaskIf2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesCosProfilePortmaskIf2.setStatus("current")


class _MesCosProfilePortmaskIf3_Type(Unsigned32):
    """Custom type mesCosProfilePortmaskIf3 based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MesCosProfilePortmaskIf3_Type.__name__ = "Unsigned32"
_MesCosProfilePortmaskIf3_Object = MibTableColumn
mesCosProfilePortmaskIf3 = _MesCosProfilePortmaskIf3_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 23, 1, 1, 52),
    _MesCosProfilePortmaskIf3_Type()
)
mesCosProfilePortmaskIf3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesCosProfilePortmaskIf3.setStatus("current")


class _MesCosProfilePortmaskIf4_Type(Unsigned32):
    """Custom type mesCosProfilePortmaskIf4 based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MesCosProfilePortmaskIf4_Type.__name__ = "Unsigned32"
_MesCosProfilePortmaskIf4_Object = MibTableColumn
mesCosProfilePortmaskIf4 = _MesCosProfilePortmaskIf4_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 23, 1, 1, 53),
    _MesCosProfilePortmaskIf4_Type()
)
mesCosProfilePortmaskIf4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesCosProfilePortmaskIf4.setStatus("current")


class _MesCosProfilePortmaskIf5_Type(Unsigned32):
    """Custom type mesCosProfilePortmaskIf5 based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MesCosProfilePortmaskIf5_Type.__name__ = "Unsigned32"
_MesCosProfilePortmaskIf5_Object = MibTableColumn
mesCosProfilePortmaskIf5 = _MesCosProfilePortmaskIf5_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 23, 1, 1, 54),
    _MesCosProfilePortmaskIf5_Type()
)
mesCosProfilePortmaskIf5.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesCosProfilePortmaskIf5.setStatus("current")


class _MesCosProfilePortmaskIf6_Type(Unsigned32):
    """Custom type mesCosProfilePortmaskIf6 based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MesCosProfilePortmaskIf6_Type.__name__ = "Unsigned32"
_MesCosProfilePortmaskIf6_Object = MibTableColumn
mesCosProfilePortmaskIf6 = _MesCosProfilePortmaskIf6_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 23, 1, 1, 55),
    _MesCosProfilePortmaskIf6_Type()
)
mesCosProfilePortmaskIf6.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesCosProfilePortmaskIf6.setStatus("current")


class _MesCosProfilePortmaskIf7_Type(Unsigned32):
    """Custom type mesCosProfilePortmaskIf7 based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MesCosProfilePortmaskIf7_Type.__name__ = "Unsigned32"
_MesCosProfilePortmaskIf7_Object = MibTableColumn
mesCosProfilePortmaskIf7 = _MesCosProfilePortmaskIf7_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 23, 1, 1, 56),
    _MesCosProfilePortmaskIf7_Type()
)
mesCosProfilePortmaskIf7.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesCosProfilePortmaskIf7.setStatus("current")


class _MesCosProfilePortmaskIf8_Type(Unsigned32):
    """Custom type mesCosProfilePortmaskIf8 based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MesCosProfilePortmaskIf8_Type.__name__ = "Unsigned32"
_MesCosProfilePortmaskIf8_Object = MibTableColumn
mesCosProfilePortmaskIf8 = _MesCosProfilePortmaskIf8_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 23, 1, 1, 57),
    _MesCosProfilePortmaskIf8_Type()
)
mesCosProfilePortmaskIf8.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesCosProfilePortmaskIf8.setStatus("current")


class _MesCosProfilePortmaskIf9_Type(Unsigned32):
    """Custom type mesCosProfilePortmaskIf9 based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MesCosProfilePortmaskIf9_Type.__name__ = "Unsigned32"
_MesCosProfilePortmaskIf9_Object = MibTableColumn
mesCosProfilePortmaskIf9 = _MesCosProfilePortmaskIf9_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 23, 1, 1, 58),
    _MesCosProfilePortmaskIf9_Type()
)
mesCosProfilePortmaskIf9.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesCosProfilePortmaskIf9.setStatus("current")


class _MesCosProfilePortmaskIf10_Type(Unsigned32):
    """Custom type mesCosProfilePortmaskIf10 based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MesCosProfilePortmaskIf10_Type.__name__ = "Unsigned32"
_MesCosProfilePortmaskIf10_Object = MibTableColumn
mesCosProfilePortmaskIf10 = _MesCosProfilePortmaskIf10_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 23, 1, 1, 59),
    _MesCosProfilePortmaskIf10_Type()
)
mesCosProfilePortmaskIf10.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesCosProfilePortmaskIf10.setStatus("current")


class _MesCosProfilePortmaskIf11_Type(Unsigned32):
    """Custom type mesCosProfilePortmaskIf11 based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MesCosProfilePortmaskIf11_Type.__name__ = "Unsigned32"
_MesCosProfilePortmaskIf11_Object = MibTableColumn
mesCosProfilePortmaskIf11 = _MesCosProfilePortmaskIf11_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 23, 1, 1, 60),
    _MesCosProfilePortmaskIf11_Type()
)
mesCosProfilePortmaskIf11.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesCosProfilePortmaskIf11.setStatus("current")


class _MesCosProfilePortmaskIf12_Type(Unsigned32):
    """Custom type mesCosProfilePortmaskIf12 based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MesCosProfilePortmaskIf12_Type.__name__ = "Unsigned32"
_MesCosProfilePortmaskIf12_Object = MibTableColumn
mesCosProfilePortmaskIf12 = _MesCosProfilePortmaskIf12_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 23, 1, 1, 61),
    _MesCosProfilePortmaskIf12_Type()
)
mesCosProfilePortmaskIf12.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesCosProfilePortmaskIf12.setStatus("current")


class _MesCosProfilePortmaskIf13_Type(Unsigned32):
    """Custom type mesCosProfilePortmaskIf13 based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MesCosProfilePortmaskIf13_Type.__name__ = "Unsigned32"
_MesCosProfilePortmaskIf13_Object = MibTableColumn
mesCosProfilePortmaskIf13 = _MesCosProfilePortmaskIf13_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 23, 1, 1, 62),
    _MesCosProfilePortmaskIf13_Type()
)
mesCosProfilePortmaskIf13.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesCosProfilePortmaskIf13.setStatus("current")


class _MesCosProfilePortmaskIf14_Type(Unsigned32):
    """Custom type mesCosProfilePortmaskIf14 based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MesCosProfilePortmaskIf14_Type.__name__ = "Unsigned32"
_MesCosProfilePortmaskIf14_Object = MibTableColumn
mesCosProfilePortmaskIf14 = _MesCosProfilePortmaskIf14_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 23, 1, 1, 63),
    _MesCosProfilePortmaskIf14_Type()
)
mesCosProfilePortmaskIf14.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesCosProfilePortmaskIf14.setStatus("current")


class _MesCosProfilePortmaskIf15_Type(Unsigned32):
    """Custom type mesCosProfilePortmaskIf15 based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MesCosProfilePortmaskIf15_Type.__name__ = "Unsigned32"
_MesCosProfilePortmaskIf15_Object = MibTableColumn
mesCosProfilePortmaskIf15 = _MesCosProfilePortmaskIf15_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 23, 1, 1, 64),
    _MesCosProfilePortmaskIf15_Type()
)
mesCosProfilePortmaskIf15.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesCosProfilePortmaskIf15.setStatus("current")


class _MesCosProfilePortmaskIf16_Type(Unsigned32):
    """Custom type mesCosProfilePortmaskIf16 based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MesCosProfilePortmaskIf16_Type.__name__ = "Unsigned32"
_MesCosProfilePortmaskIf16_Object = MibTableColumn
mesCosProfilePortmaskIf16 = _MesCosProfilePortmaskIf16_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 23, 1, 1, 65),
    _MesCosProfilePortmaskIf16_Type()
)
mesCosProfilePortmaskIf16.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesCosProfilePortmaskIf16.setStatus("current")
_MesMaidList_ObjectIdentity = ObjectIdentity
mesMaidList = _MesMaidList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 24)
)
_MesMaidTable_Object = MibTable
mesMaidTable = _MesMaidTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 24, 1)
)
if mibBuilder.loadTexts:
    mesMaidTable.setStatus("current")
_MesMaidEntry_Object = MibTableRow
mesMaidEntry = _MesMaidEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 24, 1, 1)
)
mesMaidEntry.setIndexNames(
    (0, "LUM-MES-MIB", "mesMaidIndex"),
)
if mibBuilder.loadTexts:
    mesMaidEntry.setStatus("current")


class _MesMaidIndex_Type(Unsigned32):
    """Custom type mesMaidIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_MesMaidIndex_Type.__name__ = "Unsigned32"
_MesMaidIndex_Object = MibTableColumn
mesMaidIndex = _MesMaidIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 24, 1, 1, 1),
    _MesMaidIndex_Type()
)
mesMaidIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesMaidIndex.setStatus("current")
_MesMaidName_Type = MgmtNameString
_MesMaidName_Object = MibTableColumn
mesMaidName = _MesMaidName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 24, 1, 1, 2),
    _MesMaidName_Type()
)
mesMaidName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesMaidName.setStatus("current")


class _MesMaidGroupId_Type(Unsigned32):
    """Custom type mesMaidGroupId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_MesMaidGroupId_Type.__name__ = "Unsigned32"
_MesMaidGroupId_Object = MibTableColumn
mesMaidGroupId = _MesMaidGroupId_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 24, 1, 1, 3),
    _MesMaidGroupId_Type()
)
mesMaidGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesMaidGroupId.setStatus("current")


class _MesMaidMdFormat_Type(Dot1agCfmMaintDomainNameType):
    """Custom type mesMaidMdFormat based on Dot1agCfmMaintDomainNameType"""
    defaultValue = 4


_MesMaidMdFormat_Type.__name__ = "Dot1agCfmMaintDomainNameType"
_MesMaidMdFormat_Object = MibTableColumn
mesMaidMdFormat = _MesMaidMdFormat_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 24, 1, 1, 4),
    _MesMaidMdFormat_Type()
)
mesMaidMdFormat.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesMaidMdFormat.setStatus("current")


class _MesMaidMdName_Type(Dot1agCfmMaintDomainName):
    """Custom type mesMaidMdName based on Dot1agCfmMaintDomainName"""
    defaultValue = OctetString("DEFAULT")


_MesMaidMdName_Type.__name__ = "Dot1agCfmMaintDomainName"
_MesMaidMdName_Object = MibTableColumn
mesMaidMdName = _MesMaidMdName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 24, 1, 1, 5),
    _MesMaidMdName_Type()
)
mesMaidMdName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesMaidMdName.setStatus("current")


class _MesMaidMdMac_Type(DisplayString):
    """Custom type mesMaidMdMac based on DisplayString"""
    defaultValue = OctetString(" ")


_MesMaidMdMac_Type.__name__ = "DisplayString"
_MesMaidMdMac_Object = MibTableColumn
mesMaidMdMac = _MesMaidMdMac_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 24, 1, 1, 6),
    _MesMaidMdMac_Type()
)
mesMaidMdMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesMaidMdMac.setStatus("current")


class _MesMaidMd2Octet_Type(DisplayString):
    """Custom type mesMaidMd2Octet based on DisplayString"""
    defaultValue = OctetString(" ")


_MesMaidMd2Octet_Type.__name__ = "DisplayString"
_MesMaidMd2Octet_Object = MibTableColumn
mesMaidMd2Octet = _MesMaidMd2Octet_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 24, 1, 1, 7),
    _MesMaidMd2Octet_Type()
)
mesMaidMd2Octet.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesMaidMd2Octet.setStatus("current")


class _MesMaidMdString_Type(DisplayString):
    """Custom type mesMaidMdString based on DisplayString"""
    defaultValue = OctetString(" ")


_MesMaidMdString_Type.__name__ = "DisplayString"
_MesMaidMdString_Object = MibTableColumn
mesMaidMdString = _MesMaidMdString_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 24, 1, 1, 8),
    _MesMaidMdString_Type()
)
mesMaidMdString.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesMaidMdString.setStatus("current")


class _MesMaidLevel_Type(Dot1agCfmMDLevel):
    """Custom type mesMaidLevel based on Dot1agCfmMDLevel"""
    defaultValue = 0


_MesMaidLevel_Type.__name__ = "Dot1agCfmMDLevel"
_MesMaidLevel_Object = MibTableColumn
mesMaidLevel = _MesMaidLevel_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 24, 1, 1, 9),
    _MesMaidLevel_Type()
)
mesMaidLevel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesMaidLevel.setStatus("current")
_MesMaidMaFormat_Type = Dot1agCfmMaintAssocNameType
_MesMaidMaFormat_Object = MibTableColumn
mesMaidMaFormat = _MesMaidMaFormat_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 24, 1, 1, 10),
    _MesMaidMaFormat_Type()
)
mesMaidMaFormat.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesMaidMaFormat.setStatus("current")
_MesMaidMaName_Type = Dot1agCfmMaintAssocName
_MesMaidMaName_Object = MibTableColumn
mesMaidMaName = _MesMaidMaName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 24, 1, 1, 11),
    _MesMaidMaName_Type()
)
mesMaidMaName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesMaidMaName.setStatus("current")


class _MesMaidMaVpnOui_Type(DisplayString):
    """Custom type mesMaidMaVpnOui based on DisplayString"""
    defaultValue = OctetString(" ")


_MesMaidMaVpnOui_Type.__name__ = "DisplayString"
_MesMaidMaVpnOui_Object = MibTableColumn
mesMaidMaVpnOui = _MesMaidMaVpnOui_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 24, 1, 1, 12),
    _MesMaidMaVpnOui_Type()
)
mesMaidMaVpnOui.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesMaidMaVpnOui.setStatus("current")


class _MesMaidMaVpnIndex_Type(DisplayString):
    """Custom type mesMaidMaVpnIndex based on DisplayString"""
    defaultValue = OctetString(" ")


_MesMaidMaVpnIndex_Type.__name__ = "DisplayString"
_MesMaidMaVpnIndex_Object = MibTableColumn
mesMaidMaVpnIndex = _MesMaidMaVpnIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 24, 1, 1, 13),
    _MesMaidMaVpnIndex_Type()
)
mesMaidMaVpnIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesMaidMaVpnIndex.setStatus("current")


class _MesMaidMa2Octet_Type(DisplayString):
    """Custom type mesMaidMa2Octet based on DisplayString"""
    defaultValue = OctetString(" ")


_MesMaidMa2Octet_Type.__name__ = "DisplayString"
_MesMaidMa2Octet_Object = MibTableColumn
mesMaidMa2Octet = _MesMaidMa2Octet_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 24, 1, 1, 14),
    _MesMaidMa2Octet_Type()
)
mesMaidMa2Octet.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesMaidMa2Octet.setStatus("current")


class _MesMaidMaVlan_Type(DisplayString):
    """Custom type mesMaidMaVlan based on DisplayString"""
    defaultValue = OctetString(" ")


_MesMaidMaVlan_Type.__name__ = "DisplayString"
_MesMaidMaVlan_Object = MibTableColumn
mesMaidMaVlan = _MesMaidMaVlan_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 24, 1, 1, 15),
    _MesMaidMaVlan_Type()
)
mesMaidMaVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesMaidMaVlan.setStatus("current")


class _MesMaidMaString_Type(DisplayString):
    """Custom type mesMaidMaString based on DisplayString"""
    defaultValue = OctetString(" ")


_MesMaidMaString_Type.__name__ = "DisplayString"
_MesMaidMaString_Object = MibTableColumn
mesMaidMaString = _MesMaidMaString_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 24, 1, 1, 16),
    _MesMaidMaString_Type()
)
mesMaidMaString.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesMaidMaString.setStatus("current")


class _MesMaidCcmInterval_Type(Dot1agCfmCcmInterval):
    """Custom type mesMaidCcmInterval based on Dot1agCfmCcmInterval"""
    defaultValue = 5


_MesMaidCcmInterval_Type.__name__ = "Dot1agCfmCcmInterval"
_MesMaidCcmInterval_Object = MibTableColumn
mesMaidCcmInterval = _MesMaidCcmInterval_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 24, 1, 1, 17),
    _MesMaidCcmInterval_Type()
)
mesMaidCcmInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mesMaidCcmInterval.setStatus("current")


class _MesMaidInternalReference_Type(Unsigned32):
    """Custom type mesMaidInternalReference based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MesMaidInternalReference_Type.__name__ = "Unsigned32"
_MesMaidInternalReference_Object = MibTableColumn
mesMaidInternalReference = _MesMaidInternalReference_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 24, 1, 1, 18),
    _MesMaidInternalReference_Type()
)
mesMaidInternalReference.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesMaidInternalReference.setStatus("current")


class _MesMaidIdentifier_Type(DisplayString):
    """Custom type mesMaidIdentifier based on DisplayString"""
    defaultValue = OctetString(" ")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_MesMaidIdentifier_Type.__name__ = "DisplayString"
_MesMaidIdentifier_Object = MibTableColumn
mesMaidIdentifier = _MesMaidIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 24, 1, 1, 19),
    _MesMaidIdentifier_Type()
)
mesMaidIdentifier.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesMaidIdentifier.setStatus("current")


class _MesMaidNoOfMeps_Type(Unsigned32):
    """Custom type mesMaidNoOfMeps based on Unsigned32"""
    defaultValue = 0


_MesMaidNoOfMeps_Type.__name__ = "Unsigned32"
_MesMaidNoOfMeps_Object = MibTableColumn
mesMaidNoOfMeps = _MesMaidNoOfMeps_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 24, 1, 1, 20),
    _MesMaidNoOfMeps_Type()
)
mesMaidNoOfMeps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesMaidNoOfMeps.setStatus("current")
_MesMaidAssociateMep_Type = CommandString
_MesMaidAssociateMep_Object = MibTableColumn
mesMaidAssociateMep = _MesMaidAssociateMep_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 24, 1, 1, 21),
    _MesMaidAssociateMep_Type()
)
mesMaidAssociateMep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesMaidAssociateMep.setStatus("current")
_MesMaidReleaseMeps_Type = CommandString
_MesMaidReleaseMeps_Object = MibTableColumn
mesMaidReleaseMeps = _MesMaidReleaseMeps_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 24, 1, 1, 22),
    _MesMaidReleaseMeps_Type()
)
mesMaidReleaseMeps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesMaidReleaseMeps.setStatus("current")
_MesMaidRowStatus_Type = RowStatus
_MesMaidRowStatus_Object = MibTableColumn
mesMaidRowStatus = _MesMaidRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 24, 1, 1, 23),
    _MesMaidRowStatus_Type()
)
mesMaidRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesMaidRowStatus.setStatus("current")


class _MesMaidNoOfUpMeps_Type(Unsigned32):
    """Custom type mesMaidNoOfUpMeps based on Unsigned32"""
    defaultValue = 0


_MesMaidNoOfUpMeps_Type.__name__ = "Unsigned32"
_MesMaidNoOfUpMeps_Object = MibTableColumn
mesMaidNoOfUpMeps = _MesMaidNoOfUpMeps_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 24, 1, 1, 24),
    _MesMaidNoOfUpMeps_Type()
)
mesMaidNoOfUpMeps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesMaidNoOfUpMeps.setStatus("current")


class _MesMaidLocalDeviceType_Type(Integer32):
    """Custom type mesMaidLocalDeviceType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("emxp", 1),
          ("nidGe", 2))
    )


_MesMaidLocalDeviceType_Type.__name__ = "Integer32"
_MesMaidLocalDeviceType_Object = MibTableColumn
mesMaidLocalDeviceType = _MesMaidLocalDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 24, 1, 1, 25),
    _MesMaidLocalDeviceType_Type()
)
mesMaidLocalDeviceType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesMaidLocalDeviceType.setStatus("current")


class _MesMaidViewFilter_Type(Integer32):
    """Custom type mesMaidViewFilter based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("emxp", 1),
          ("nidGe", 2))
    )


_MesMaidViewFilter_Type.__name__ = "Integer32"
_MesMaidViewFilter_Object = MibTableColumn
mesMaidViewFilter = _MesMaidViewFilter_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 24, 1, 1, 26),
    _MesMaidViewFilter_Type()
)
mesMaidViewFilter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesMaidViewFilter.setStatus("current")


class _MesMaidNoOfNidMeps_Type(Unsigned32):
    """Custom type mesMaidNoOfNidMeps based on Unsigned32"""
    defaultValue = 0


_MesMaidNoOfNidMeps_Type.__name__ = "Unsigned32"
_MesMaidNoOfNidMeps_Object = MibTableColumn
mesMaidNoOfNidMeps = _MesMaidNoOfNidMeps_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 24, 1, 1, 27),
    _MesMaidNoOfNidMeps_Type()
)
mesMaidNoOfNidMeps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesMaidNoOfNidMeps.setStatus("current")
_MesMaidAssociateMepNid_Type = CommandString
_MesMaidAssociateMepNid_Object = MibTableColumn
mesMaidAssociateMepNid = _MesMaidAssociateMepNid_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 24, 1, 1, 28),
    _MesMaidAssociateMepNid_Type()
)
mesMaidAssociateMepNid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesMaidAssociateMepNid.setStatus("current")
_MesMaidAssociateMepAdvanced_Type = CommandString
_MesMaidAssociateMepAdvanced_Object = MibTableColumn
mesMaidAssociateMepAdvanced = _MesMaidAssociateMepAdvanced_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 24, 1, 1, 29),
    _MesMaidAssociateMepAdvanced_Type()
)
mesMaidAssociateMepAdvanced.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesMaidAssociateMepAdvanced.setStatus("current")
_MesMaidSubrack_Type = SubrackNumber
_MesMaidSubrack_Object = MibTableColumn
mesMaidSubrack = _MesMaidSubrack_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 24, 1, 1, 30),
    _MesMaidSubrack_Type()
)
mesMaidSubrack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesMaidSubrack.setStatus("current")
_MesMaidSlot_Type = SlotNumber
_MesMaidSlot_Object = MibTableColumn
mesMaidSlot = _MesMaidSlot_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 24, 1, 1, 31),
    _MesMaidSlot_Type()
)
mesMaidSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesMaidSlot.setStatus("current")


class _MesMaidServiceId_Type(ServiceIdWithNotUsed):
    """Custom type mesMaidServiceId based on ServiceIdWithNotUsed"""
    defaultValue = -1


_MesMaidServiceId_Type.__name__ = "ServiceIdWithNotUsed"
_MesMaidServiceId_Object = MibTableColumn
mesMaidServiceId = _MesMaidServiceId_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 24, 1, 1, 32),
    _MesMaidServiceId_Type()
)
mesMaidServiceId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mesMaidServiceId.setStatus("current")
_MesCfmMepList_ObjectIdentity = ObjectIdentity
mesCfmMepList = _MesCfmMepList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 25)
)
_MesCfmMepTable_Object = MibTable
mesCfmMepTable = _MesCfmMepTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 25, 1)
)
if mibBuilder.loadTexts:
    mesCfmMepTable.setStatus("current")
_MesCfmMepEntry_Object = MibTableRow
mesCfmMepEntry = _MesCfmMepEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 25, 1, 1)
)
mesCfmMepEntry.setIndexNames(
    (0, "LUM-MES-MIB", "mesCfmMepIndex"),
)
if mibBuilder.loadTexts:
    mesCfmMepEntry.setStatus("current")


class _MesCfmMepIndex_Type(Unsigned32):
    """Custom type mesCfmMepIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_MesCfmMepIndex_Type.__name__ = "Unsigned32"
_MesCfmMepIndex_Object = MibTableColumn
mesCfmMepIndex = _MesCfmMepIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 25, 1, 1, 1),
    _MesCfmMepIndex_Type()
)
mesCfmMepIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesCfmMepIndex.setStatus("current")
_MesCfmMepName_Type = MgmtNameString
_MesCfmMepName_Object = MibTableColumn
mesCfmMepName = _MesCfmMepName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 25, 1, 1, 2),
    _MesCfmMepName_Type()
)
mesCfmMepName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesCfmMepName.setStatus("current")


class _MesCfmMepMaid_Type(DisplayString):
    """Custom type mesCfmMepMaid based on DisplayString"""
    defaultValue = OctetString(" ")


_MesCfmMepMaid_Type.__name__ = "DisplayString"
_MesCfmMepMaid_Object = MibTableColumn
mesCfmMepMaid = _MesCfmMepMaid_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 25, 1, 1, 3),
    _MesCfmMepMaid_Type()
)
mesCfmMepMaid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesCfmMepMaid.setStatus("current")


class _MesCfmMepTxPort_Type(PortNumber):
    """Custom type mesCfmMepTxPort based on PortNumber"""
    defaultValue = 1


_MesCfmMepTxPort_Type.__name__ = "PortNumber"
_MesCfmMepTxPort_Object = MibTableColumn
mesCfmMepTxPort = _MesCfmMepTxPort_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 25, 1, 1, 4),
    _MesCfmMepTxPort_Type()
)
mesCfmMepTxPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesCfmMepTxPort.setStatus("current")
_MesCfmMepPortName_Type = DisplayString
_MesCfmMepPortName_Object = MibTableColumn
mesCfmMepPortName = _MesCfmMepPortName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 25, 1, 1, 5),
    _MesCfmMepPortName_Type()
)
mesCfmMepPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesCfmMepPortName.setStatus("current")


class _MesCfmMepAdminStatus_Type(BoardOrInterfaceAdminStatus):
    """Custom type mesCfmMepAdminStatus based on BoardOrInterfaceAdminStatus"""
    defaultValue = 3


_MesCfmMepAdminStatus_Type.__name__ = "BoardOrInterfaceAdminStatus"
_MesCfmMepAdminStatus_Object = MibTableColumn
mesCfmMepAdminStatus = _MesCfmMepAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 25, 1, 1, 6),
    _MesCfmMepAdminStatus_Type()
)
mesCfmMepAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mesCfmMepAdminStatus.setStatus("current")


class _MesCfmMepOperStatus_Type(BoardOrInterfaceOperStatus):
    """Custom type mesCfmMepOperStatus based on BoardOrInterfaceOperStatus"""
    defaultValue = 1


_MesCfmMepOperStatus_Type.__name__ = "BoardOrInterfaceOperStatus"
_MesCfmMepOperStatus_Object = MibTableColumn
mesCfmMepOperStatus = _MesCfmMepOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 25, 1, 1, 7),
    _MesCfmMepOperStatus_Type()
)
mesCfmMepOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesCfmMepOperStatus.setStatus("current")


class _MesCfmMepPrimaryVid_Type(Unsigned32):
    """Custom type mesCfmMepPrimaryVid based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_MesCfmMepPrimaryVid_Type.__name__ = "Unsigned32"
_MesCfmMepPrimaryVid_Object = MibTableColumn
mesCfmMepPrimaryVid = _MesCfmMepPrimaryVid_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 25, 1, 1, 8),
    _MesCfmMepPrimaryVid_Type()
)
mesCfmMepPrimaryVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mesCfmMepPrimaryVid.setStatus("current")


class _MesCfmMepVlanPriority_Type(Integer32):
    """Custom type mesCfmMepVlanPriority based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_MesCfmMepVlanPriority_Type.__name__ = "Integer32"
_MesCfmMepVlanPriority_Object = MibTableColumn
mesCfmMepVlanPriority = _MesCfmMepVlanPriority_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 25, 1, 1, 9),
    _MesCfmMepVlanPriority_Type()
)
mesCfmMepVlanPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mesCfmMepVlanPriority.setStatus("current")


class _MesCfmMepType_Type(Integer32):
    """Custom type mesCfmMepType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("local", 1),
          ("remote", 2))
    )


_MesCfmMepType_Type.__name__ = "Integer32"
_MesCfmMepType_Object = MibTableColumn
mesCfmMepType = _MesCfmMepType_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 25, 1, 1, 10),
    _MesCfmMepType_Type()
)
mesCfmMepType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesCfmMepType.setStatus("current")


class _MesCfmMepIdentifier_Type(Dot1agCfmMepId):
    """Custom type mesCfmMepIdentifier based on Dot1agCfmMepId"""
    defaultValue = 1


_MesCfmMepIdentifier_Type.__name__ = "Dot1agCfmMepId"
_MesCfmMepIdentifier_Object = MibTableColumn
mesCfmMepIdentifier = _MesCfmMepIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 25, 1, 1, 11),
    _MesCfmMepIdentifier_Type()
)
mesCfmMepIdentifier.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesCfmMepIdentifier.setStatus("current")


class _MesCfmMepInternalReference_Type(Unsigned32):
    """Custom type mesCfmMepInternalReference based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MesCfmMepInternalReference_Type.__name__ = "Unsigned32"
_MesCfmMepInternalReference_Object = MibTableColumn
mesCfmMepInternalReference = _MesCfmMepInternalReference_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 25, 1, 1, 12),
    _MesCfmMepInternalReference_Type()
)
mesCfmMepInternalReference.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesCfmMepInternalReference.setStatus("current")
_MesCfmMepRDICCM_Type = FaultStatus
_MesCfmMepRDICCM_Object = MibTableColumn
mesCfmMepRDICCM = _MesCfmMepRDICCM_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 25, 1, 1, 13),
    _MesCfmMepRDICCM_Type()
)
mesCfmMepRDICCM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesCfmMepRDICCM.setStatus("current")
_MesCfmMepMACstatus_Type = FaultStatus
_MesCfmMepMACstatus_Object = MibTableColumn
mesCfmMepMACstatus = _MesCfmMepMACstatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 25, 1, 1, 14),
    _MesCfmMepMACstatus_Type()
)
mesCfmMepMACstatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesCfmMepMACstatus.setStatus("current")
_MesCfmMepRemoteCCM_Type = FaultStatus
_MesCfmMepRemoteCCM_Object = MibTableColumn
mesCfmMepRemoteCCM = _MesCfmMepRemoteCCM_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 25, 1, 1, 15),
    _MesCfmMepRemoteCCM_Type()
)
mesCfmMepRemoteCCM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesCfmMepRemoteCCM.setStatus("current")
_MesCfmMepErrorCCM_Type = FaultStatus
_MesCfmMepErrorCCM_Object = MibTableColumn
mesCfmMepErrorCCM = _MesCfmMepErrorCCM_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 25, 1, 1, 16),
    _MesCfmMepErrorCCM_Type()
)
mesCfmMepErrorCCM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesCfmMepErrorCCM.setStatus("current")
_MesCfmMepXconCCM_Type = FaultStatus
_MesCfmMepXconCCM_Object = MibTableColumn
mesCfmMepXconCCM = _MesCfmMepXconCCM_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 25, 1, 1, 17),
    _MesCfmMepXconCCM_Type()
)
mesCfmMepXconCCM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesCfmMepXconCCM.setStatus("current")
_MesCfmMepAis_Type = FaultStatus
_MesCfmMepAis_Object = MibTableColumn
mesCfmMepAis = _MesCfmMepAis_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 25, 1, 1, 18),
    _MesCfmMepAis_Type()
)
mesCfmMepAis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesCfmMepAis.setStatus("current")
_MesCfmMepChangePort_Type = CommandString
_MesCfmMepChangePort_Object = MibTableColumn
mesCfmMepChangePort = _MesCfmMepChangePort_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 25, 1, 1, 19),
    _MesCfmMepChangePort_Type()
)
mesCfmMepChangePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesCfmMepChangePort.setStatus("deprecated")


class _MesCfmMepTransmitLbrStatus_Type(Integer32):
    """Custom type mesCfmMepTransmitLbrStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_MesCfmMepTransmitLbrStatus_Type.__name__ = "Integer32"
_MesCfmMepTransmitLbrStatus_Object = MibTableColumn
mesCfmMepTransmitLbrStatus = _MesCfmMepTransmitLbrStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 25, 1, 1, 20),
    _MesCfmMepTransmitLbrStatus_Type()
)
mesCfmMepTransmitLbrStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mesCfmMepTransmitLbrStatus.setStatus("current")
_MesCfmMepRowStatus_Type = RowStatus
_MesCfmMepRowStatus_Object = MibTableColumn
mesCfmMepRowStatus = _MesCfmMepRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 25, 1, 1, 21),
    _MesCfmMepRowStatus_Type()
)
mesCfmMepRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesCfmMepRowStatus.setStatus("current")


class _MesCfmMepDirection_Type(Dot1agCfmMpDirection):
    """Custom type mesCfmMepDirection based on Dot1agCfmMpDirection"""
    defaultValue = 1


_MesCfmMepDirection_Type.__name__ = "Dot1agCfmMpDirection"
_MesCfmMepDirection_Object = MibTableColumn
mesCfmMepDirection = _MesCfmMepDirection_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 25, 1, 1, 22),
    _MesCfmMepDirection_Type()
)
mesCfmMepDirection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesCfmMepDirection.setStatus("current")


class _MesCfmMepCcmSeqNumStatus_Type(Integer32):
    """Custom type mesCfmMepCcmSeqNumStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_MesCfmMepCcmSeqNumStatus_Type.__name__ = "Integer32"
_MesCfmMepCcmSeqNumStatus_Object = MibTableColumn
mesCfmMepCcmSeqNumStatus = _MesCfmMepCcmSeqNumStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 25, 1, 1, 23),
    _MesCfmMepCcmSeqNumStatus_Type()
)
mesCfmMepCcmSeqNumStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mesCfmMepCcmSeqNumStatus.setStatus("current")
_MesCfmMepRemoteCsfLos_Type = FaultStatus
_MesCfmMepRemoteCsfLos_Object = MibTableColumn
mesCfmMepRemoteCsfLos = _MesCfmMepRemoteCsfLos_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 25, 1, 1, 24),
    _MesCfmMepRemoteCsfLos_Type()
)
mesCfmMepRemoteCsfLos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesCfmMepRemoteCsfLos.setStatus("current")
_MesCfmMepRemoteCsfRdi_Type = FaultStatus
_MesCfmMepRemoteCsfRdi_Object = MibTableColumn
mesCfmMepRemoteCsfRdi = _MesCfmMepRemoteCsfRdi_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 25, 1, 1, 25),
    _MesCfmMepRemoteCsfRdi_Type()
)
mesCfmMepRemoteCsfRdi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesCfmMepRemoteCsfRdi.setStatus("current")
_MesCfmMepRemoteCsfFdi_Type = FaultStatus
_MesCfmMepRemoteCsfFdi_Object = MibTableColumn
mesCfmMepRemoteCsfFdi = _MesCfmMepRemoteCsfFdi_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 25, 1, 1, 26),
    _MesCfmMepRemoteCsfFdi_Type()
)
mesCfmMepRemoteCsfFdi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesCfmMepRemoteCsfFdi.setStatus("current")
_MesCfmMepLocalCsfLos_Type = FaultStatus
_MesCfmMepLocalCsfLos_Object = MibTableColumn
mesCfmMepLocalCsfLos = _MesCfmMepLocalCsfLos_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 25, 1, 1, 27),
    _MesCfmMepLocalCsfLos_Type()
)
mesCfmMepLocalCsfLos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesCfmMepLocalCsfLos.setStatus("current")


class _MesCfmMepLocalDeviceType_Type(Integer32):
    """Custom type mesCfmMepLocalDeviceType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("emxp", 1),
          ("nidGe", 2))
    )


_MesCfmMepLocalDeviceType_Type.__name__ = "Integer32"
_MesCfmMepLocalDeviceType_Object = MibTableColumn
mesCfmMepLocalDeviceType = _MesCfmMepLocalDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 25, 1, 1, 28),
    _MesCfmMepLocalDeviceType_Type()
)
mesCfmMepLocalDeviceType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesCfmMepLocalDeviceType.setStatus("current")


class _MesCfmMepLocalDeviceName_Type(DisplayString):
    """Custom type mesCfmMepLocalDeviceName based on DisplayString"""
    defaultValue = OctetString(" ")


_MesCfmMepLocalDeviceName_Type.__name__ = "DisplayString"
_MesCfmMepLocalDeviceName_Object = MibTableColumn
mesCfmMepLocalDeviceName = _MesCfmMepLocalDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 25, 1, 1, 29),
    _MesCfmMepLocalDeviceName_Type()
)
mesCfmMepLocalDeviceName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesCfmMepLocalDeviceName.setStatus("current")


class _MesCfmMepLocalDeviceId_Type(Unsigned32):
    """Custom type mesCfmMepLocalDeviceId based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MesCfmMepLocalDeviceId_Type.__name__ = "Unsigned32"
_MesCfmMepLocalDeviceId_Object = MibTableColumn
mesCfmMepLocalDeviceId = _MesCfmMepLocalDeviceId_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 25, 1, 1, 30),
    _MesCfmMepLocalDeviceId_Type()
)
mesCfmMepLocalDeviceId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesCfmMepLocalDeviceId.setStatus("current")


class _MesCfmMepViewFilter_Type(Integer32):
    """Custom type mesCfmMepViewFilter based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("emxp", 1),
          ("nidGe", 2))
    )


_MesCfmMepViewFilter_Type.__name__ = "Integer32"
_MesCfmMepViewFilter_Object = MibTableColumn
mesCfmMepViewFilter = _MesCfmMepViewFilter_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 25, 1, 1, 31),
    _MesCfmMepViewFilter_Type()
)
mesCfmMepViewFilter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesCfmMepViewFilter.setStatus("current")
_MesCfmMepUnexpectedPeriod_Type = FaultStatus
_MesCfmMepUnexpectedPeriod_Object = MibTableColumn
mesCfmMepUnexpectedPeriod = _MesCfmMepUnexpectedPeriod_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 25, 1, 1, 32),
    _MesCfmMepUnexpectedPeriod_Type()
)
mesCfmMepUnexpectedPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesCfmMepUnexpectedPeriod.setStatus("current")
_MesCfmMepUnexpectedMepId_Type = FaultStatus
_MesCfmMepUnexpectedMepId_Object = MibTableColumn
mesCfmMepUnexpectedMepId = _MesCfmMepUnexpectedMepId_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 25, 1, 1, 33),
    _MesCfmMepUnexpectedMepId_Type()
)
mesCfmMepUnexpectedMepId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesCfmMepUnexpectedMepId.setStatus("current")
_MesCfmMepUnexpectedMegLevel_Type = FaultStatus
_MesCfmMepUnexpectedMegLevel_Object = MibTableColumn
mesCfmMepUnexpectedMegLevel = _MesCfmMepUnexpectedMegLevel_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 25, 1, 1, 34),
    _MesCfmMepUnexpectedMegLevel_Type()
)
mesCfmMepUnexpectedMegLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesCfmMepUnexpectedMegLevel.setStatus("current")
_MesCfmMepMismerge_Type = FaultStatus
_MesCfmMepMismerge_Object = MibTableColumn
mesCfmMepMismerge = _MesCfmMepMismerge_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 25, 1, 1, 35),
    _MesCfmMepMismerge_Type()
)
mesCfmMepMismerge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesCfmMepMismerge.setStatus("current")


class _MesCfmMepNoOfLMs_Type(Unsigned32):
    """Custom type mesCfmMepNoOfLMs based on Unsigned32"""
    defaultValue = 0


_MesCfmMepNoOfLMs_Type.__name__ = "Unsigned32"
_MesCfmMepNoOfLMs_Object = MibTableColumn
mesCfmMepNoOfLMs = _MesCfmMepNoOfLMs_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 25, 1, 1, 36),
    _MesCfmMepNoOfLMs_Type()
)
mesCfmMepNoOfLMs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesCfmMepNoOfLMs.setStatus("current")


class _MesCfmMepNoOfDMs_Type(Unsigned32):
    """Custom type mesCfmMepNoOfDMs based on Unsigned32"""
    defaultValue = 0


_MesCfmMepNoOfDMs_Type.__name__ = "Unsigned32"
_MesCfmMepNoOfDMs_Object = MibTableColumn
mesCfmMepNoOfDMs = _MesCfmMepNoOfDMs_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 25, 1, 1, 37),
    _MesCfmMepNoOfDMs_Type()
)
mesCfmMepNoOfDMs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesCfmMepNoOfDMs.setStatus("current")
_MesCfmMepAssociateLM_Type = CommandString
_MesCfmMepAssociateLM_Object = MibTableColumn
mesCfmMepAssociateLM = _MesCfmMepAssociateLM_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 25, 1, 1, 38),
    _MesCfmMepAssociateLM_Type()
)
mesCfmMepAssociateLM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesCfmMepAssociateLM.setStatus("current")
_MesCfmMepAssociateDM_Type = CommandString
_MesCfmMepAssociateDM_Object = MibTableColumn
mesCfmMepAssociateDM = _MesCfmMepAssociateDM_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 25, 1, 1, 39),
    _MesCfmMepAssociateDM_Type()
)
mesCfmMepAssociateDM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesCfmMepAssociateDM.setStatus("current")


class _MesCfmMepTransmitDmrStatus_Type(Integer32):
    """Custom type mesCfmMepTransmitDmrStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_MesCfmMepTransmitDmrStatus_Type.__name__ = "Integer32"
_MesCfmMepTransmitDmrStatus_Object = MibTableColumn
mesCfmMepTransmitDmrStatus = _MesCfmMepTransmitDmrStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 25, 1, 1, 40),
    _MesCfmMepTransmitDmrStatus_Type()
)
mesCfmMepTransmitDmrStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mesCfmMepTransmitDmrStatus.setStatus("current")


class _MesCfmMepTransmitLmrStatus_Type(Integer32):
    """Custom type mesCfmMepTransmitLmrStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_MesCfmMepTransmitLmrStatus_Type.__name__ = "Integer32"
_MesCfmMepTransmitLmrStatus_Object = MibTableColumn
mesCfmMepTransmitLmrStatus = _MesCfmMepTransmitLmrStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 25, 1, 1, 41),
    _MesCfmMepTransmitLmrStatus_Type()
)
mesCfmMepTransmitLmrStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mesCfmMepTransmitLmrStatus.setStatus("current")


class _MesCfmMepLmCosAwareness_Type(Integer32):
    """Custom type mesCfmMepLmCosAwareness based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("priorityBlind", 1),
          ("priorityAware", 2))
    )


_MesCfmMepLmCosAwareness_Type.__name__ = "Integer32"
_MesCfmMepLmCosAwareness_Object = MibTableColumn
mesCfmMepLmCosAwareness = _MesCfmMepLmCosAwareness_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 25, 1, 1, 42),
    _MesCfmMepLmCosAwareness_Type()
)
mesCfmMepLmCosAwareness.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mesCfmMepLmCosAwareness.setStatus("current")


class _MesCfmMepResourceType_Type(Integer32):
    """Custom type mesCfmMepResourceType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("port", 1),
          ("lag", 2))
    )


_MesCfmMepResourceType_Type.__name__ = "Integer32"
_MesCfmMepResourceType_Object = MibTableColumn
mesCfmMepResourceType = _MesCfmMepResourceType_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 25, 1, 1, 43),
    _MesCfmMepResourceType_Type()
)
mesCfmMepResourceType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesCfmMepResourceType.setStatus("current")


class _MesCfmMepLagId_Type(DisplayString):
    """Custom type mesCfmMepLagId based on DisplayString"""
    defaultValue = OctetString(" ")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 17),
    )


_MesCfmMepLagId_Type.__name__ = "DisplayString"
_MesCfmMepLagId_Object = MibTableColumn
mesCfmMepLagId = _MesCfmMepLagId_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 25, 1, 1, 44),
    _MesCfmMepLagId_Type()
)
mesCfmMepLagId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesCfmMepLagId.setStatus("current")


class _MesCfmMepInterfaceName_Type(DisplayString):
    """Custom type mesCfmMepInterfaceName based on DisplayString"""
    defaultValue = OctetString(" ")


_MesCfmMepInterfaceName_Type.__name__ = "DisplayString"
_MesCfmMepInterfaceName_Object = MibTableColumn
mesCfmMepInterfaceName = _MesCfmMepInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 25, 1, 1, 45),
    _MesCfmMepInterfaceName_Type()
)
mesCfmMepInterfaceName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesCfmMepInterfaceName.setStatus("current")


class _MesCfmMepIfNo_Type(PortNumber):
    """Custom type mesCfmMepIfNo based on PortNumber"""
    defaultValue = 1


_MesCfmMepIfNo_Type.__name__ = "PortNumber"
_MesCfmMepIfNo_Object = MibTableColumn
mesCfmMepIfNo = _MesCfmMepIfNo_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 25, 1, 1, 46),
    _MesCfmMepIfNo_Type()
)
mesCfmMepIfNo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesCfmMepIfNo.setStatus("current")


class _MesCfmMepLocalId_Type(Integer32):
    """Custom type mesCfmMepLocalId based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_MesCfmMepLocalId_Type.__name__ = "Integer32"
_MesCfmMepLocalId_Object = MibTableColumn
mesCfmMepLocalId = _MesCfmMepLocalId_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 25, 1, 1, 47),
    _MesCfmMepLocalId_Type()
)
mesCfmMepLocalId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesCfmMepLocalId.setStatus("current")
_MesCfmMepSubrack_Type = SubrackNumber
_MesCfmMepSubrack_Object = MibTableColumn
mesCfmMepSubrack = _MesCfmMepSubrack_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 25, 1, 1, 48),
    _MesCfmMepSubrack_Type()
)
mesCfmMepSubrack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesCfmMepSubrack.setStatus("current")
_MesCfmMepSlot_Type = SlotNumber
_MesCfmMepSlot_Object = MibTableColumn
mesCfmMepSlot = _MesCfmMepSlot_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 25, 1, 1, 49),
    _MesCfmMepSlot_Type()
)
mesCfmMepSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesCfmMepSlot.setStatus("current")


class _MesCfmMepServiceId_Type(ServiceIdWithNotUsed):
    """Custom type mesCfmMepServiceId based on ServiceIdWithNotUsed"""
    defaultValue = -1


_MesCfmMepServiceId_Type.__name__ = "ServiceIdWithNotUsed"
_MesCfmMepServiceId_Object = MibTableColumn
mesCfmMepServiceId = _MesCfmMepServiceId_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 25, 1, 1, 50),
    _MesCfmMepServiceId_Type()
)
mesCfmMepServiceId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mesCfmMepServiceId.setStatus("current")
_MesErpList_ObjectIdentity = ObjectIdentity
mesErpList = _MesErpList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 26)
)
_MesErpTable_Object = MibTable
mesErpTable = _MesErpTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 26, 1)
)
if mibBuilder.loadTexts:
    mesErpTable.setStatus("current")
_MesErpEntry_Object = MibTableRow
mesErpEntry = _MesErpEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 26, 1, 1)
)
mesErpEntry.setIndexNames(
    (0, "LUM-MES-MIB", "mesErpIndex"),
)
if mibBuilder.loadTexts:
    mesErpEntry.setStatus("current")


class _MesErpIndex_Type(Unsigned32):
    """Custom type mesErpIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_MesErpIndex_Type.__name__ = "Unsigned32"
_MesErpIndex_Object = MibTableColumn
mesErpIndex = _MesErpIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 26, 1, 1, 1),
    _MesErpIndex_Type()
)
mesErpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesErpIndex.setStatus("current")
_MesErpName_Type = MgmtNameString
_MesErpName_Object = MibTableColumn
mesErpName = _MesErpName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 26, 1, 1, 2),
    _MesErpName_Type()
)
mesErpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesErpName.setStatus("current")


class _MesErpPortLeft_Type(Unsigned32):
    """Custom type mesErpPortLeft based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MesErpPortLeft_Type.__name__ = "Unsigned32"
_MesErpPortLeft_Object = MibTableColumn
mesErpPortLeft = _MesErpPortLeft_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 26, 1, 1, 3),
    _MesErpPortLeft_Type()
)
mesErpPortLeft.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesErpPortLeft.setStatus("current")


class _MesErpPortRight_Type(Unsigned32):
    """Custom type mesErpPortRight based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MesErpPortRight_Type.__name__ = "Unsigned32"
_MesErpPortRight_Object = MibTableColumn
mesErpPortRight = _MesErpPortRight_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 26, 1, 1, 4),
    _MesErpPortRight_Type()
)
mesErpPortRight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesErpPortRight.setStatus("current")


class _MesErpAdminStatus_Type(BoardOrInterfaceAdminStatus):
    """Custom type mesErpAdminStatus based on BoardOrInterfaceAdminStatus"""
    defaultValue = 3


_MesErpAdminStatus_Type.__name__ = "BoardOrInterfaceAdminStatus"
_MesErpAdminStatus_Object = MibTableColumn
mesErpAdminStatus = _MesErpAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 26, 1, 1, 5),
    _MesErpAdminStatus_Type()
)
mesErpAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mesErpAdminStatus.setStatus("current")


class _MesErpInternalReference_Type(Unsigned32):
    """Custom type mesErpInternalReference based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MesErpInternalReference_Type.__name__ = "Unsigned32"
_MesErpInternalReference_Object = MibTableColumn
mesErpInternalReference = _MesErpInternalReference_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 26, 1, 1, 6),
    _MesErpInternalReference_Type()
)
mesErpInternalReference.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesErpInternalReference.setStatus("current")


class _MesErpDescr_Type(DisplayString):
    """Custom type mesErpDescr based on DisplayString"""
    defaultValue = OctetString("")


_MesErpDescr_Type.__name__ = "DisplayString"
_MesErpDescr_Object = MibTableColumn
mesErpDescr = _MesErpDescr_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 26, 1, 1, 7),
    _MesErpDescr_Type()
)
mesErpDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mesErpDescr.setStatus("current")


class _MesErpVlanId_Type(Unsigned32):
    """Custom type mesErpVlanId based on Unsigned32"""
    defaultValue = 4094

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_MesErpVlanId_Type.__name__ = "Unsigned32"
_MesErpVlanId_Object = MibTableColumn
mesErpVlanId = _MesErpVlanId_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 26, 1, 1, 8),
    _MesErpVlanId_Type()
)
mesErpVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesErpVlanId.setStatus("current")


class _MesErpMegLevel_Type(Dot1agCfmMDLevel):
    """Custom type mesErpMegLevel based on Dot1agCfmMDLevel"""
    defaultValue = 3


_MesErpMegLevel_Type.__name__ = "Dot1agCfmMDLevel"
_MesErpMegLevel_Object = MibTableColumn
mesErpMegLevel = _MesErpMegLevel_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 26, 1, 1, 9),
    _MesErpMegLevel_Type()
)
mesErpMegLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mesErpMegLevel.setStatus("current")


class _MesErpProtLink_Type(Integer32):
    """Custom type mesErpProtLink based on Integer32"""
    defaultValue = 1

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
        *(("none", 1),
          ("left", 2),
          ("right", 3),
          ("leftNeighbour", 4),
          ("rightNeighbour", 5))
    )


_MesErpProtLink_Type.__name__ = "Integer32"
_MesErpProtLink_Object = MibTableColumn
mesErpProtLink = _MesErpProtLink_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 26, 1, 1, 10),
    _MesErpProtLink_Type()
)
mesErpProtLink.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mesErpProtLink.setStatus("current")


class _MesErpGuardTime_Type(Unsigned32):
    """Custom type mesErpGuardTime based on Unsigned32"""
    defaultValue = 500

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 2000),
    )


_MesErpGuardTime_Type.__name__ = "Unsigned32"
_MesErpGuardTime_Object = MibTableColumn
mesErpGuardTime = _MesErpGuardTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 26, 1, 1, 11),
    _MesErpGuardTime_Type()
)
mesErpGuardTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mesErpGuardTime.setStatus("current")


class _MesErpHoldOffTime_Type(Unsigned32):
    """Custom type mesErpHoldOffTime based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_MesErpHoldOffTime_Type.__name__ = "Unsigned32"
_MesErpHoldOffTime_Object = MibTableColumn
mesErpHoldOffTime = _MesErpHoldOffTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 26, 1, 1, 12),
    _MesErpHoldOffTime_Type()
)
mesErpHoldOffTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesErpHoldOffTime.setStatus("current")


class _MesErpWtrTime_Type(Unsigned32):
    """Custom type mesErpWtrTime based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_MesErpWtrTime_Type.__name__ = "Unsigned32"
_MesErpWtrTime_Object = MibTableColumn
mesErpWtrTime = _MesErpWtrTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 26, 1, 1, 13),
    _MesErpWtrTime_Type()
)
mesErpWtrTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mesErpWtrTime.setStatus("current")


class _MesErpOamDetectionLeft_Type(Integer32):
    """Custom type mesErpOamDetectionLeft based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_MesErpOamDetectionLeft_Type.__name__ = "Integer32"
_MesErpOamDetectionLeft_Object = MibTableColumn
mesErpOamDetectionLeft = _MesErpOamDetectionLeft_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 26, 1, 1, 14),
    _MesErpOamDetectionLeft_Type()
)
mesErpOamDetectionLeft.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mesErpOamDetectionLeft.setStatus("current")


class _MesErpOamDetectionRight_Type(Integer32):
    """Custom type mesErpOamDetectionRight based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_MesErpOamDetectionRight_Type.__name__ = "Integer32"
_MesErpOamDetectionRight_Object = MibTableColumn
mesErpOamDetectionRight = _MesErpOamDetectionRight_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 26, 1, 1, 15),
    _MesErpOamDetectionRight_Type()
)
mesErpOamDetectionRight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mesErpOamDetectionRight.setStatus("current")


class _MesErpStatusLeft_Type(Integer32):
    """Custom type mesErpStatusLeft based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("forwarding", 1),
          ("blocked", 2))
    )


_MesErpStatusLeft_Type.__name__ = "Integer32"
_MesErpStatusLeft_Object = MibTableColumn
mesErpStatusLeft = _MesErpStatusLeft_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 26, 1, 1, 16),
    _MesErpStatusLeft_Type()
)
mesErpStatusLeft.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesErpStatusLeft.setStatus("current")


class _MesErpStatusRight_Type(Integer32):
    """Custom type mesErpStatusRight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("forwarding", 1),
          ("blocked", 2))
    )


_MesErpStatusRight_Type.__name__ = "Integer32"
_MesErpStatusRight_Object = MibTableColumn
mesErpStatusRight = _MesErpStatusRight_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 26, 1, 1, 17),
    _MesErpStatusRight_Type()
)
mesErpStatusRight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesErpStatusRight.setStatus("current")


class _MesErpProtState_Type(Integer32):
    """Custom type mesErpProtState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("starting", 1),
          ("idle", 2),
          ("protection", 3),
          ("manualSwitch", 4),
          ("forcedSwitch", 5),
          ("pending", 6))
    )


_MesErpProtState_Type.__name__ = "Integer32"
_MesErpProtState_Object = MibTableColumn
mesErpProtState = _MesErpProtState_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 26, 1, 1, 18),
    _MesErpProtState_Type()
)
mesErpProtState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesErpProtState.setStatus("current")


class _MesErpActiveEvent_Type(Integer32):
    """Custom type mesErpActiveEvent based on Integer32"""
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
              10,
              11,
              12,
              13,
              14,
              15,
              16)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("none", 1),
          ("localSignalFail", 2),
          ("localClearSignalFail", 3),
          ("remoteSignalFail", 4),
          ("wtrExpire", 5),
          ("wtrRunning", 6),
          ("noRequestRb", 7),
          ("noRequest", 8),
          ("localClear", 9),
          ("localFs", 10),
          ("remoteFs", 11),
          ("remoteMs", 12),
          ("localMs", 13),
          ("wtbExpires", 14),
          ("wtbRunning", 15),
          ("remoteEvent", 16))
    )


_MesErpActiveEvent_Type.__name__ = "Integer32"
_MesErpActiveEvent_Object = MibTableColumn
mesErpActiveEvent = _MesErpActiveEvent_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 26, 1, 1, 19),
    _MesErpActiveEvent_Type()
)
mesErpActiveEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesErpActiveEvent.setStatus("current")


class _MesErpRapsReqState_Type(Integer32):
    """Custom type mesErpRapsReqState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("signalFail", 1),
          ("noRequest", 2),
          ("reserved", 3),
          ("reqStateForcedSwitch", 4),
          ("reqStateEvent", 5),
          ("reqManualSwitch", 6))
    )


_MesErpRapsReqState_Type.__name__ = "Integer32"
_MesErpRapsReqState_Object = MibTableColumn
mesErpRapsReqState = _MesErpRapsReqState_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 26, 1, 1, 20),
    _MesErpRapsReqState_Type()
)
mesErpRapsReqState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesErpRapsReqState.setStatus("current")
_MesErpServiceFailure_Type = FaultStatus
_MesErpServiceFailure_Object = MibTableColumn
mesErpServiceFailure = _MesErpServiceFailure_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 26, 1, 1, 21),
    _MesErpServiceFailure_Type()
)
mesErpServiceFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesErpServiceFailure.setStatus("current")
_MesErpServiceDegraded_Type = FaultStatus
_MesErpServiceDegraded_Object = MibTableColumn
mesErpServiceDegraded = _MesErpServiceDegraded_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 26, 1, 1, 22),
    _MesErpServiceDegraded_Type()
)
mesErpServiceDegraded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesErpServiceDegraded.setStatus("current")
_MesErpUnexpectedMegLevel_Type = FaultStatus
_MesErpUnexpectedMegLevel_Object = MibTableColumn
mesErpUnexpectedMegLevel = _MesErpUnexpectedMegLevel_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 26, 1, 1, 23),
    _MesErpUnexpectedMegLevel_Type()
)
mesErpUnexpectedMegLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesErpUnexpectedMegLevel.setStatus("current")
_MesErpCommunicationFailure_Type = FaultStatus
_MesErpCommunicationFailure_Object = MibTableColumn
mesErpCommunicationFailure = _MesErpCommunicationFailure_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 26, 1, 1, 24),
    _MesErpCommunicationFailure_Type()
)
mesErpCommunicationFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesErpCommunicationFailure.setStatus("current")
_MesErpChangePort_Type = CommandString
_MesErpChangePort_Object = MibTableColumn
mesErpChangePort = _MesErpChangePort_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 26, 1, 1, 25),
    _MesErpChangePort_Type()
)
mesErpChangePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesErpChangePort.setStatus("deprecated")
_MesErpRowStatus_Type = RowStatus
_MesErpRowStatus_Object = MibTableColumn
mesErpRowStatus = _MesErpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 26, 1, 1, 26),
    _MesErpRowStatus_Type()
)
mesErpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesErpRowStatus.setStatus("current")


class _MesErpNodeType_Type(Integer32):
    """Custom type mesErpNodeType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ringNode", 1),
          ("subInterconnection", 2))
    )


_MesErpNodeType_Type.__name__ = "Integer32"
_MesErpNodeType_Object = MibTableColumn
mesErpNodeType = _MesErpNodeType_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 26, 1, 1, 27),
    _MesErpNodeType_Type()
)
mesErpNodeType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesErpNodeType.setStatus("current")


class _MesErpProtectionMode_Type(Integer32):
    """Custom type mesErpProtectionMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nonRevertive", 1),
          ("revertive", 2))
    )


_MesErpProtectionMode_Type.__name__ = "Integer32"
_MesErpProtectionMode_Object = MibTableColumn
mesErpProtectionMode = _MesErpProtectionMode_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 26, 1, 1, 28),
    _MesErpProtectionMode_Type()
)
mesErpProtectionMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mesErpProtectionMode.setStatus("current")


class _MesErpVersion_Type(Integer32):
    """Custom type mesErpVersion based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("erpV1", 1),
          ("erpV2", 2))
    )


_MesErpVersion_Type.__name__ = "Integer32"
_MesErpVersion_Object = MibTableColumn
mesErpVersion = _MesErpVersion_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 26, 1, 1, 29),
    _MesErpVersion_Type()
)
mesErpVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesErpVersion.setStatus("current")


class _MesErpMajorName_Type(MgmtNameString):
    """Custom type mesErpMajorName based on MgmtNameString"""
    defaultValue = OctetString("")


_MesErpMajorName_Type.__name__ = "MgmtNameString"
_MesErpMajorName_Object = MibTableColumn
mesErpMajorName = _MesErpMajorName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 26, 1, 1, 30),
    _MesErpMajorName_Type()
)
mesErpMajorName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesErpMajorName.setStatus("current")


class _MesErpRingId_Type(Unsigned32):
    """Custom type mesErpRingId based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 239),
    )


_MesErpRingId_Type.__name__ = "Unsigned32"
_MesErpRingId_Object = MibTableColumn
mesErpRingId = _MesErpRingId_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 26, 1, 1, 31),
    _MesErpRingId_Type()
)
mesErpRingId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesErpRingId.setStatus("current")


class _MesErpRingIndex_Type(Unsigned32):
    """Custom type mesErpRingIndex based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_MesErpRingIndex_Type.__name__ = "Unsigned32"
_MesErpRingIndex_Object = MibTableColumn
mesErpRingIndex = _MesErpRingIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 26, 1, 1, 32),
    _MesErpRingIndex_Type()
)
mesErpRingIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesErpRingIndex.setStatus("current")


class _MesErpOperatorCommand_Type(Integer32):
    """Custom type mesErpOperatorCommand based on Integer32"""
    defaultValue = 1

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
        *(("noRequest", 1),
          ("forcedLeft", 2),
          ("forcedRight", 3),
          ("manualLeft", 4),
          ("manualRight", 5),
          ("clear", 6))
    )


_MesErpOperatorCommand_Type.__name__ = "Integer32"
_MesErpOperatorCommand_Object = MibTableColumn
mesErpOperatorCommand = _MesErpOperatorCommand_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 26, 1, 1, 33),
    _MesErpOperatorCommand_Type()
)
mesErpOperatorCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mesErpOperatorCommand.setStatus("current")


class _MesErpGroupId_Type(Unsigned32):
    """Custom type mesErpGroupId based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MesErpGroupId_Type.__name__ = "Unsigned32"
_MesErpGroupId_Object = MibTableColumn
mesErpGroupId = _MesErpGroupId_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 26, 1, 1, 34),
    _MesErpGroupId_Type()
)
mesErpGroupId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesErpGroupId.setStatus("current")
_MesErpSwitchInformation_Type = FaultStatus
_MesErpSwitchInformation_Object = MibTableColumn
mesErpSwitchInformation = _MesErpSwitchInformation_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 26, 1, 1, 35),
    _MesErpSwitchInformation_Type()
)
mesErpSwitchInformation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesErpSwitchInformation.setStatus("current")


class _MesErpTopologyChangePropagation_Type(Integer32):
    """Custom type mesErpTopologyChangePropagation based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_MesErpTopologyChangePropagation_Type.__name__ = "Integer32"
_MesErpTopologyChangePropagation_Object = MibTableColumn
mesErpTopologyChangePropagation = _MesErpTopologyChangePropagation_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 26, 1, 1, 36),
    _MesErpTopologyChangePropagation_Type()
)
mesErpTopologyChangePropagation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mesErpTopologyChangePropagation.setStatus("current")


class _MesErpSubRings_Type(Counter64):
    """Custom type mesErpSubRings based on Counter64"""
    defaultValue = 0


_MesErpSubRings_Type.__name__ = "Counter64"
_MesErpSubRings_Object = MibTableColumn
mesErpSubRings = _MesErpSubRings_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 26, 1, 1, 37),
    _MesErpSubRings_Type()
)
mesErpSubRings.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesErpSubRings.setStatus("current")


class _MesErpResourceTypeLeft_Type(Integer32):
    """Custom type mesErpResourceTypeLeft based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("port", 1),
          ("lag", 2))
    )


_MesErpResourceTypeLeft_Type.__name__ = "Integer32"
_MesErpResourceTypeLeft_Object = MibTableColumn
mesErpResourceTypeLeft = _MesErpResourceTypeLeft_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 26, 1, 1, 38),
    _MesErpResourceTypeLeft_Type()
)
mesErpResourceTypeLeft.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesErpResourceTypeLeft.setStatus("current")


class _MesErpLagIdLeft_Type(DisplayString):
    """Custom type mesErpLagIdLeft based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 17),
    )


_MesErpLagIdLeft_Type.__name__ = "DisplayString"
_MesErpLagIdLeft_Object = MibTableColumn
mesErpLagIdLeft = _MesErpLagIdLeft_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 26, 1, 1, 39),
    _MesErpLagIdLeft_Type()
)
mesErpLagIdLeft.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesErpLagIdLeft.setStatus("current")


class _MesErpResourceTypeRight_Type(Integer32):
    """Custom type mesErpResourceTypeRight based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("port", 1),
          ("lag", 2))
    )


_MesErpResourceTypeRight_Type.__name__ = "Integer32"
_MesErpResourceTypeRight_Object = MibTableColumn
mesErpResourceTypeRight = _MesErpResourceTypeRight_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 26, 1, 1, 40),
    _MesErpResourceTypeRight_Type()
)
mesErpResourceTypeRight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesErpResourceTypeRight.setStatus("current")


class _MesErpLagIdRight_Type(DisplayString):
    """Custom type mesErpLagIdRight based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 17),
    )


_MesErpLagIdRight_Type.__name__ = "DisplayString"
_MesErpLagIdRight_Object = MibTableColumn
mesErpLagIdRight = _MesErpLagIdRight_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 26, 1, 1, 41),
    _MesErpLagIdRight_Type()
)
mesErpLagIdRight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesErpLagIdRight.setStatus("current")


class _MesErpInterfaceLeft_Type(DisplayString):
    """Custom type mesErpInterfaceLeft based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 17),
    )


_MesErpInterfaceLeft_Type.__name__ = "DisplayString"
_MesErpInterfaceLeft_Object = MibTableColumn
mesErpInterfaceLeft = _MesErpInterfaceLeft_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 26, 1, 1, 42),
    _MesErpInterfaceLeft_Type()
)
mesErpInterfaceLeft.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesErpInterfaceLeft.setStatus("current")


class _MesErpInterfaceRight_Type(DisplayString):
    """Custom type mesErpInterfaceRight based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 17),
    )


_MesErpInterfaceRight_Type.__name__ = "DisplayString"
_MesErpInterfaceRight_Object = MibTableColumn
mesErpInterfaceRight = _MesErpInterfaceRight_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 26, 1, 1, 43),
    _MesErpInterfaceRight_Type()
)
mesErpInterfaceRight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesErpInterfaceRight.setStatus("current")
_MesErpProvisioningMismatch_Type = FaultStatus
_MesErpProvisioningMismatch_Object = MibTableColumn
mesErpProvisioningMismatch = _MesErpProvisioningMismatch_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 26, 1, 1, 44),
    _MesErpProvisioningMismatch_Type()
)
mesErpProvisioningMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesErpProvisioningMismatch.setStatus("current")


class _MesErpIfNoLeft_Type(PortNumber):
    """Custom type mesErpIfNoLeft based on PortNumber"""
    defaultValue = 1


_MesErpIfNoLeft_Type.__name__ = "PortNumber"
_MesErpIfNoLeft_Object = MibTableColumn
mesErpIfNoLeft = _MesErpIfNoLeft_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 26, 1, 1, 45),
    _MesErpIfNoLeft_Type()
)
mesErpIfNoLeft.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesErpIfNoLeft.setStatus("current")


class _MesErpTxPortLeft_Type(PortNumber):
    """Custom type mesErpTxPortLeft based on PortNumber"""
    defaultValue = 0


_MesErpTxPortLeft_Type.__name__ = "PortNumber"
_MesErpTxPortLeft_Object = MibTableColumn
mesErpTxPortLeft = _MesErpTxPortLeft_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 26, 1, 1, 46),
    _MesErpTxPortLeft_Type()
)
mesErpTxPortLeft.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesErpTxPortLeft.setStatus("current")


class _MesErpIfNoRight_Type(PortNumber):
    """Custom type mesErpIfNoRight based on PortNumber"""
    defaultValue = 1


_MesErpIfNoRight_Type.__name__ = "PortNumber"
_MesErpIfNoRight_Object = MibTableColumn
mesErpIfNoRight = _MesErpIfNoRight_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 26, 1, 1, 47),
    _MesErpIfNoRight_Type()
)
mesErpIfNoRight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesErpIfNoRight.setStatus("current")


class _MesErpTxPortRight_Type(PortNumber):
    """Custom type mesErpTxPortRight based on PortNumber"""
    defaultValue = 0


_MesErpTxPortRight_Type.__name__ = "PortNumber"
_MesErpTxPortRight_Object = MibTableColumn
mesErpTxPortRight = _MesErpTxPortRight_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 26, 1, 1, 48),
    _MesErpTxPortRight_Type()
)
mesErpTxPortRight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesErpTxPortRight.setStatus("current")


class _MesErpOamDetectionVlanId_Type(Unsigned32):
    """Custom type mesErpOamDetectionVlanId based on Unsigned32"""
    defaultValue = 4094

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_MesErpOamDetectionVlanId_Type.__name__ = "Unsigned32"
_MesErpOamDetectionVlanId_Object = MibTableColumn
mesErpOamDetectionVlanId = _MesErpOamDetectionVlanId_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 26, 1, 1, 49),
    _MesErpOamDetectionVlanId_Type()
)
mesErpOamDetectionVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mesErpOamDetectionVlanId.setStatus("current")
_MesClassList_ObjectIdentity = ObjectIdentity
mesClassList = _MesClassList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 27)
)
_MesClassTable_Object = MibTable
mesClassTable = _MesClassTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 27, 1)
)
if mibBuilder.loadTexts:
    mesClassTable.setStatus("current")
_MesClassEntry_Object = MibTableRow
mesClassEntry = _MesClassEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 27, 1, 1)
)
mesClassEntry.setIndexNames(
    (0, "LUM-MES-MIB", "mesClassIndex"),
)
if mibBuilder.loadTexts:
    mesClassEntry.setStatus("current")


class _MesClassIndex_Type(Unsigned32):
    """Custom type mesClassIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_MesClassIndex_Type.__name__ = "Unsigned32"
_MesClassIndex_Object = MibTableColumn
mesClassIndex = _MesClassIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 27, 1, 1, 1),
    _MesClassIndex_Type()
)
mesClassIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesClassIndex.setStatus("current")
_MesClassName_Type = MgmtNameString
_MesClassName_Object = MibTableColumn
mesClassName = _MesClassName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 27, 1, 1, 2),
    _MesClassName_Type()
)
mesClassName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesClassName.setStatus("current")


class _MesClassIdentifier_Type(DisplayString):
    """Custom type mesClassIdentifier based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 22),
    )


_MesClassIdentifier_Type.__name__ = "DisplayString"
_MesClassIdentifier_Object = MibTableColumn
mesClassIdentifier = _MesClassIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 27, 1, 1, 3),
    _MesClassIdentifier_Type()
)
mesClassIdentifier.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesClassIdentifier.setStatus("current")


class _MesClassInternalReference_Type(Unsigned32):
    """Custom type mesClassInternalReference based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MesClassInternalReference_Type.__name__ = "Unsigned32"
_MesClassInternalReference_Object = MibTableColumn
mesClassInternalReference = _MesClassInternalReference_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 27, 1, 1, 4),
    _MesClassInternalReference_Type()
)
mesClassInternalReference.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesClassInternalReference.setStatus("current")


class _MesClassPort_Type(Unsigned32):
    """Custom type mesClassPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MesClassPort_Type.__name__ = "Unsigned32"
_MesClassPort_Object = MibTableColumn
mesClassPort = _MesClassPort_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 27, 1, 1, 5),
    _MesClassPort_Type()
)
mesClassPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesClassPort.setStatus("current")
_MesClassLagId_Type = MgmtNameString
_MesClassLagId_Object = MibTableColumn
mesClassLagId = _MesClassLagId_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 27, 1, 1, 6),
    _MesClassLagId_Type()
)
mesClassLagId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesClassLagId.setStatus("current")


class _MesClassOuterVlanId_Type(Integer32):
    """Custom type mesClassOuterVlanId based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 4094),
    )


_MesClassOuterVlanId_Type.__name__ = "Integer32"
_MesClassOuterVlanId_Object = MibTableColumn
mesClassOuterVlanId = _MesClassOuterVlanId_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 27, 1, 1, 7),
    _MesClassOuterVlanId_Type()
)
mesClassOuterVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesClassOuterVlanId.setStatus("current")


class _MesClassOuterVlanPcp_Type(Integer32):
    """Custom type mesClassOuterVlanPcp based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 7),
    )


_MesClassOuterVlanPcp_Type.__name__ = "Integer32"
_MesClassOuterVlanPcp_Object = MibTableColumn
mesClassOuterVlanPcp = _MesClassOuterVlanPcp_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 27, 1, 1, 8),
    _MesClassOuterVlanPcp_Type()
)
mesClassOuterVlanPcp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesClassOuterVlanPcp.setStatus("current")


class _MesClassPrecedence_Type(Unsigned32):
    """Custom type mesClassPrecedence based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 511),
    )


_MesClassPrecedence_Type.__name__ = "Unsigned32"
_MesClassPrecedence_Object = MibTableColumn
mesClassPrecedence = _MesClassPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 27, 1, 1, 9),
    _MesClassPrecedence_Type()
)
mesClassPrecedence.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesClassPrecedence.setStatus("current")
_MesClassDaMacAddress_Type = MacAddress
_MesClassDaMacAddress_Object = MibTableColumn
mesClassDaMacAddress = _MesClassDaMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 27, 1, 1, 10),
    _MesClassDaMacAddress_Type()
)
mesClassDaMacAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesClassDaMacAddress.setStatus("current")
_MesClassAssociateAction_Type = CommandString
_MesClassAssociateAction_Object = MibTableColumn
mesClassAssociateAction = _MesClassAssociateAction_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 27, 1, 1, 11),
    _MesClassAssociateAction_Type()
)
mesClassAssociateAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesClassAssociateAction.setStatus("current")
_MesClassRowStatus_Type = RowStatus
_MesClassRowStatus_Object = MibTableColumn
mesClassRowStatus = _MesClassRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 27, 1, 1, 12),
    _MesClassRowStatus_Type()
)
mesClassRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesClassRowStatus.setStatus("current")


class _MesClassDaMacAddressMask_Type(MacAddress):
    """Custom type mesClassDaMacAddressMask based on MacAddress"""
    defaultHexValue = "FFFFFFFFFFFF"


_MesClassDaMacAddressMask_Type.__name__ = "MacAddress"
_MesClassDaMacAddressMask_Object = MibTableColumn
mesClassDaMacAddressMask = _MesClassDaMacAddressMask_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 27, 1, 1, 13),
    _MesClassDaMacAddressMask_Type()
)
mesClassDaMacAddressMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesClassDaMacAddressMask.setStatus("current")


class _MesClassInnerVlanId_Type(Integer32):
    """Custom type mesClassInnerVlanId based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 4094),
    )


_MesClassInnerVlanId_Type.__name__ = "Integer32"
_MesClassInnerVlanId_Object = MibTableColumn
mesClassInnerVlanId = _MesClassInnerVlanId_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 27, 1, 1, 14),
    _MesClassInnerVlanId_Type()
)
mesClassInnerVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesClassInnerVlanId.setStatus("current")


class _MesClassInnerVlanPcp_Type(Integer32):
    """Custom type mesClassInnerVlanPcp based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 7),
    )


_MesClassInnerVlanPcp_Type.__name__ = "Integer32"
_MesClassInnerVlanPcp_Object = MibTableColumn
mesClassInnerVlanPcp = _MesClassInnerVlanPcp_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 27, 1, 1, 15),
    _MesClassInnerVlanPcp_Type()
)
mesClassInnerVlanPcp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesClassInnerVlanPcp.setStatus("current")


class _MesClassDSCP_Type(Integer32):
    """Custom type mesClassDSCP based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 63),
    )


_MesClassDSCP_Type.__name__ = "Integer32"
_MesClassDSCP_Object = MibTableColumn
mesClassDSCP = _MesClassDSCP_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 27, 1, 1, 16),
    _MesClassDSCP_Type()
)
mesClassDSCP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesClassDSCP.setStatus("current")


class _MesClassInnerVlanCfi_Type(Integer32):
    """Custom type mesClassInnerVlanCfi based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 1),
    )


_MesClassInnerVlanCfi_Type.__name__ = "Integer32"
_MesClassInnerVlanCfi_Object = MibTableColumn
mesClassInnerVlanCfi = _MesClassInnerVlanCfi_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 27, 1, 1, 17),
    _MesClassInnerVlanCfi_Type()
)
mesClassInnerVlanCfi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesClassInnerVlanCfi.setStatus("current")


class _MesClassOuterVlanCfi_Type(Integer32):
    """Custom type mesClassOuterVlanCfi based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 1),
    )


_MesClassOuterVlanCfi_Type.__name__ = "Integer32"
_MesClassOuterVlanCfi_Object = MibTableColumn
mesClassOuterVlanCfi = _MesClassOuterVlanCfi_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 27, 1, 1, 18),
    _MesClassOuterVlanCfi_Type()
)
mesClassOuterVlanCfi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesClassOuterVlanCfi.setStatus("current")


class _MesClassDirection_Type(Integer32):
    """Custom type mesClassDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("ingress", 1),
          ("egress", 2))
    )


_MesClassDirection_Type.__name__ = "Integer32"
_MesClassDirection_Object = MibTableColumn
mesClassDirection = _MesClassDirection_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 27, 1, 1, 19),
    _MesClassDirection_Type()
)
mesClassDirection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesClassDirection.setStatus("current")


class _MesClassOuterTpid_Type(Integer32):
    """Custom type mesClassOuterTpid based on Integer32"""
    defaultValue = 1

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
        *(("undefined", 0),
          ("anyTag", 1),
          ("qTag0x8100", 2),
          ("sTag0x88a8", 3))
    )


_MesClassOuterTpid_Type.__name__ = "Integer32"
_MesClassOuterTpid_Object = MibTableColumn
mesClassOuterTpid = _MesClassOuterTpid_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 27, 1, 1, 20),
    _MesClassOuterTpid_Type()
)
mesClassOuterTpid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesClassOuterTpid.setStatus("current")


class _MesClassInternalClassId_Type(Unsigned32):
    """Custom type mesClassInternalClassId based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MesClassInternalClassId_Type.__name__ = "Unsigned32"
_MesClassInternalClassId_Object = MibTableColumn
mesClassInternalClassId = _MesClassInternalClassId_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 27, 1, 1, 21),
    _MesClassInternalClassId_Type()
)
mesClassInternalClassId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesClassInternalClassId.setStatus("current")


class _MesClassSourceAddressIPV4_Type(Unsigned32):
    """Custom type mesClassSourceAddressIPV4 based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MesClassSourceAddressIPV4_Type.__name__ = "Unsigned32"
_MesClassSourceAddressIPV4_Object = MibTableColumn
mesClassSourceAddressIPV4 = _MesClassSourceAddressIPV4_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 27, 1, 1, 22),
    _MesClassSourceAddressIPV4_Type()
)
mesClassSourceAddressIPV4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesClassSourceAddressIPV4.setStatus("current")


class _MesClassSourceMaskIPV4_Type(Unsigned32):
    """Custom type mesClassSourceMaskIPV4 based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MesClassSourceMaskIPV4_Type.__name__ = "Unsigned32"
_MesClassSourceMaskIPV4_Object = MibTableColumn
mesClassSourceMaskIPV4 = _MesClassSourceMaskIPV4_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 27, 1, 1, 23),
    _MesClassSourceMaskIPV4_Type()
)
mesClassSourceMaskIPV4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesClassSourceMaskIPV4.setStatus("current")


class _MesClassDestAddressIPV4_Type(Unsigned32):
    """Custom type mesClassDestAddressIPV4 based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MesClassDestAddressIPV4_Type.__name__ = "Unsigned32"
_MesClassDestAddressIPV4_Object = MibTableColumn
mesClassDestAddressIPV4 = _MesClassDestAddressIPV4_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 27, 1, 1, 24),
    _MesClassDestAddressIPV4_Type()
)
mesClassDestAddressIPV4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesClassDestAddressIPV4.setStatus("current")


class _MesClassDestMaskIPV4_Type(Unsigned32):
    """Custom type mesClassDestMaskIPV4 based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MesClassDestMaskIPV4_Type.__name__ = "Unsigned32"
_MesClassDestMaskIPV4_Object = MibTableColumn
mesClassDestMaskIPV4 = _MesClassDestMaskIPV4_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 27, 1, 1, 25),
    _MesClassDestMaskIPV4_Type()
)
mesClassDestMaskIPV4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesClassDestMaskIPV4.setStatus("current")
_MesClassSubrack_Type = SubrackNumber
_MesClassSubrack_Object = MibTableColumn
mesClassSubrack = _MesClassSubrack_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 27, 1, 1, 26),
    _MesClassSubrack_Type()
)
mesClassSubrack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesClassSubrack.setStatus("current")
_MesClassSlot_Type = SlotNumber
_MesClassSlot_Object = MibTableColumn
mesClassSlot = _MesClassSlot_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 27, 1, 1, 27),
    _MesClassSlot_Type()
)
mesClassSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesClassSlot.setStatus("current")


class _MesClassVlanStackStructure_Type(Integer32):
    """Custom type mesClassVlanStackStructure based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("untagged", 1))
    )


_MesClassVlanStackStructure_Type.__name__ = "Integer32"
_MesClassVlanStackStructure_Object = MibTableColumn
mesClassVlanStackStructure = _MesClassVlanStackStructure_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 27, 1, 1, 28),
    _MesClassVlanStackStructure_Type()
)
mesClassVlanStackStructure.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesClassVlanStackStructure.setStatus("current")


class _MesClassServiceId_Type(ServiceIdWithNotUsed):
    """Custom type mesClassServiceId based on ServiceIdWithNotUsed"""
    defaultValue = -1


_MesClassServiceId_Type.__name__ = "ServiceIdWithNotUsed"
_MesClassServiceId_Object = MibTableColumn
mesClassServiceId = _MesClassServiceId_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 27, 1, 1, 29),
    _MesClassServiceId_Type()
)
mesClassServiceId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mesClassServiceId.setStatus("current")


class _MesClassEthertype_Type(Integer32):
    """Custom type mesClassEthertype based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("ipv40x0800", 1),
          ("ipv60x86DD", 2),
          ("slow0x8809", 3),
          ("macsec0x88E5", 4),
          ("ptp0x88F7", 5),
          ("oamcfm0x8902", 6))
    )


_MesClassEthertype_Type.__name__ = "Integer32"
_MesClassEthertype_Object = MibTableColumn
mesClassEthertype = _MesClassEthertype_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 27, 1, 1, 30),
    _MesClassEthertype_Type()
)
mesClassEthertype.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesClassEthertype.setStatus("current")


class _MesClassIfNo_Type(PortNumber):
    """Custom type mesClassIfNo based on PortNumber"""
    defaultValue = 1


_MesClassIfNo_Type.__name__ = "PortNumber"
_MesClassIfNo_Object = MibTableColumn
mesClassIfNo = _MesClassIfNo_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 27, 1, 1, 31),
    _MesClassIfNo_Type()
)
mesClassIfNo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesClassIfNo.setStatus("current")


class _MesClassTxPort_Type(PortNumber):
    """Custom type mesClassTxPort based on PortNumber"""
    defaultValue = 0


_MesClassTxPort_Type.__name__ = "PortNumber"
_MesClassTxPort_Object = MibTableColumn
mesClassTxPort = _MesClassTxPort_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 27, 1, 1, 32),
    _MesClassTxPort_Type()
)
mesClassTxPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesClassTxPort.setStatus("current")
_MesClassAssociateActionAdvanced_Type = CommandString
_MesClassAssociateActionAdvanced_Object = MibTableColumn
mesClassAssociateActionAdvanced = _MesClassAssociateActionAdvanced_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 27, 1, 1, 39),
    _MesClassAssociateActionAdvanced_Type()
)
mesClassAssociateActionAdvanced.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesClassAssociateActionAdvanced.setStatus("current")
_MesActionList_ObjectIdentity = ObjectIdentity
mesActionList = _MesActionList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 28)
)
_MesActionTable_Object = MibTable
mesActionTable = _MesActionTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 28, 1)
)
if mibBuilder.loadTexts:
    mesActionTable.setStatus("current")
_MesActionEntry_Object = MibTableRow
mesActionEntry = _MesActionEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 28, 1, 1)
)
mesActionEntry.setIndexNames(
    (0, "LUM-MES-MIB", "mesActionIndex"),
)
if mibBuilder.loadTexts:
    mesActionEntry.setStatus("current")


class _MesActionIndex_Type(Unsigned32):
    """Custom type mesActionIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_MesActionIndex_Type.__name__ = "Unsigned32"
_MesActionIndex_Object = MibTableColumn
mesActionIndex = _MesActionIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 28, 1, 1, 1),
    _MesActionIndex_Type()
)
mesActionIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesActionIndex.setStatus("current")
_MesActionName_Type = MgmtNameString
_MesActionName_Object = MibTableColumn
mesActionName = _MesActionName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 28, 1, 1, 2),
    _MesActionName_Type()
)
mesActionName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesActionName.setStatus("current")


class _MesActionIdentifier_Type(DisplayString):
    """Custom type mesActionIdentifier based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 21),
    )


_MesActionIdentifier_Type.__name__ = "DisplayString"
_MesActionIdentifier_Object = MibTableColumn
mesActionIdentifier = _MesActionIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 28, 1, 1, 3),
    _MesActionIdentifier_Type()
)
mesActionIdentifier.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesActionIdentifier.setStatus("current")


class _MesActionInternalReference_Type(Unsigned32):
    """Custom type mesActionInternalReference based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MesActionInternalReference_Type.__name__ = "Unsigned32"
_MesActionInternalReference_Object = MibTableColumn
mesActionInternalReference = _MesActionInternalReference_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 28, 1, 1, 4),
    _MesActionInternalReference_Type()
)
mesActionInternalReference.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesActionInternalReference.setStatus("current")


class _MesActionType_Type(Integer32):
    """Custom type mesActionType based on Integer32"""
    defaultValue = 1

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
              10,
              11,
              12,
              13)
        )
    )
    namedValues = NamedValues(
        *(("police", 1),
          ("greenPcp", 2),
          ("yellowPcp", 3),
          ("outerVlanIdPush", 4),
          ("outerVlanIdSwap", 5),
          ("innerVlanPop", 6),
          ("drop", 7),
          ("innerVlanIdPush", 8),
          ("innerVlanIdSwap", 9),
          ("greenQueue", 10),
          ("yellowQueue", 11),
          ("outerVlanPcpCopy", 12),
          ("redirect", 13))
    )


_MesActionType_Type.__name__ = "Integer32"
_MesActionType_Object = MibTableColumn
mesActionType = _MesActionType_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 28, 1, 1, 5),
    _MesActionType_Type()
)
mesActionType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesActionType.setStatus("current")


class _MesActionOuterVlanId_Type(Unsigned32):
    """Custom type mesActionOuterVlanId based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_MesActionOuterVlanId_Type.__name__ = "Unsigned32"
_MesActionOuterVlanId_Object = MibTableColumn
mesActionOuterVlanId = _MesActionOuterVlanId_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 28, 1, 1, 6),
    _MesActionOuterVlanId_Type()
)
mesActionOuterVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mesActionOuterVlanId.setStatus("current")


class _MesActionPcp_Type(Unsigned32):
    """Custom type mesActionPcp based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_MesActionPcp_Type.__name__ = "Unsigned32"
_MesActionPcp_Object = MibTableColumn
mesActionPcp = _MesActionPcp_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 28, 1, 1, 7),
    _MesActionPcp_Type()
)
mesActionPcp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mesActionPcp.setStatus("current")


class _MesActionPolicerId_Type(DisplayString):
    """Custom type mesActionPolicerId based on DisplayString"""
    defaultValue = OctetString("")


_MesActionPolicerId_Type.__name__ = "DisplayString"
_MesActionPolicerId_Object = MibTableColumn
mesActionPolicerId = _MesActionPolicerId_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 28, 1, 1, 8),
    _MesActionPolicerId_Type()
)
mesActionPolicerId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesActionPolicerId.setStatus("current")


class _MesActionInnerVlanId_Type(Unsigned32):
    """Custom type mesActionInnerVlanId based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_MesActionInnerVlanId_Type.__name__ = "Unsigned32"
_MesActionInnerVlanId_Object = MibTableColumn
mesActionInnerVlanId = _MesActionInnerVlanId_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 28, 1, 1, 9),
    _MesActionInnerVlanId_Type()
)
mesActionInnerVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mesActionInnerVlanId.setStatus("current")


class _MesActionQueue_Type(Unsigned32):
    """Custom type mesActionQueue based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_MesActionQueue_Type.__name__ = "Unsigned32"
_MesActionQueue_Object = MibTableColumn
mesActionQueue = _MesActionQueue_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 28, 1, 1, 10),
    _MesActionQueue_Type()
)
mesActionQueue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesActionQueue.setStatus("current")
_MesActionRowStatus_Type = RowStatus
_MesActionRowStatus_Object = MibTableColumn
mesActionRowStatus = _MesActionRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 28, 1, 1, 11),
    _MesActionRowStatus_Type()
)
mesActionRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesActionRowStatus.setStatus("current")


class _MesActionRedirectPort_Type(Unsigned32):
    """Custom type mesActionRedirectPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MesActionRedirectPort_Type.__name__ = "Unsigned32"
_MesActionRedirectPort_Object = MibTableColumn
mesActionRedirectPort = _MesActionRedirectPort_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 28, 1, 1, 12),
    _MesActionRedirectPort_Type()
)
mesActionRedirectPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesActionRedirectPort.setStatus("current")


class _MesActionServiceId_Type(ServiceIdWithNotUsed):
    """Custom type mesActionServiceId based on ServiceIdWithNotUsed"""
    defaultValue = -1


_MesActionServiceId_Type.__name__ = "ServiceIdWithNotUsed"
_MesActionServiceId_Object = MibTableColumn
mesActionServiceId = _MesActionServiceId_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 28, 1, 1, 13),
    _MesActionServiceId_Type()
)
mesActionServiceId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mesActionServiceId.setStatus("current")


class _MesActionRedirectIfNo_Type(PortNumber):
    """Custom type mesActionRedirectIfNo based on PortNumber"""
    defaultValue = 1


_MesActionRedirectIfNo_Type.__name__ = "PortNumber"
_MesActionRedirectIfNo_Object = MibTableColumn
mesActionRedirectIfNo = _MesActionRedirectIfNo_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 28, 1, 1, 14),
    _MesActionRedirectIfNo_Type()
)
mesActionRedirectIfNo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesActionRedirectIfNo.setStatus("current")


class _MesActionRedirectTxPort_Type(PortNumber):
    """Custom type mesActionRedirectTxPort based on PortNumber"""
    defaultValue = 0


_MesActionRedirectTxPort_Type.__name__ = "PortNumber"
_MesActionRedirectTxPort_Object = MibTableColumn
mesActionRedirectTxPort = _MesActionRedirectTxPort_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 28, 1, 1, 15),
    _MesActionRedirectTxPort_Type()
)
mesActionRedirectTxPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesActionRedirectTxPort.setStatus("current")


class _MesActionClassId_Type(DisplayString):
    """Custom type mesActionClassId based on DisplayString"""
    defaultValue = OctetString("")


_MesActionClassId_Type.__name__ = "DisplayString"
_MesActionClassId_Object = MibTableColumn
mesActionClassId = _MesActionClassId_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 28, 1, 1, 16),
    _MesActionClassId_Type()
)
mesActionClassId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesActionClassId.setStatus("current")
_MesActionSubrack_Type = SubrackNumber
_MesActionSubrack_Object = MibTableColumn
mesActionSubrack = _MesActionSubrack_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 28, 1, 1, 17),
    _MesActionSubrack_Type()
)
mesActionSubrack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesActionSubrack.setStatus("current")
_MesActionSlot_Type = SlotNumber
_MesActionSlot_Object = MibTableColumn
mesActionSlot = _MesActionSlot_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 28, 1, 1, 18),
    _MesActionSlot_Type()
)
mesActionSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesActionSlot.setStatus("current")
_MesPolicyList_ObjectIdentity = ObjectIdentity
mesPolicyList = _MesPolicyList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 29)
)
_MesPolicyTable_Object = MibTable
mesPolicyTable = _MesPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 29, 1)
)
if mibBuilder.loadTexts:
    mesPolicyTable.setStatus("current")
_MesPolicyEntry_Object = MibTableRow
mesPolicyEntry = _MesPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 29, 1, 1)
)
mesPolicyEntry.setIndexNames(
    (0, "LUM-MES-MIB", "mesPolicyIndex"),
)
if mibBuilder.loadTexts:
    mesPolicyEntry.setStatus("current")


class _MesPolicyIndex_Type(Unsigned32):
    """Custom type mesPolicyIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_MesPolicyIndex_Type.__name__ = "Unsigned32"
_MesPolicyIndex_Object = MibTableColumn
mesPolicyIndex = _MesPolicyIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 29, 1, 1, 1),
    _MesPolicyIndex_Type()
)
mesPolicyIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesPolicyIndex.setStatus("current")
_MesPolicyName_Type = MgmtNameString
_MesPolicyName_Object = MibTableColumn
mesPolicyName = _MesPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 29, 1, 1, 2),
    _MesPolicyName_Type()
)
mesPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesPolicyName.setStatus("current")


class _MesPolicyInternalReference_Type(Unsigned32):
    """Custom type mesPolicyInternalReference based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MesPolicyInternalReference_Type.__name__ = "Unsigned32"
_MesPolicyInternalReference_Object = MibTableColumn
mesPolicyInternalReference = _MesPolicyInternalReference_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 29, 1, 1, 4),
    _MesPolicyInternalReference_Type()
)
mesPolicyInternalReference.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesPolicyInternalReference.setStatus("current")
_MesPolicyClass_Type = DisplayString
_MesPolicyClass_Object = MibTableColumn
mesPolicyClass = _MesPolicyClass_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 29, 1, 1, 5),
    _MesPolicyClass_Type()
)
mesPolicyClass.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesPolicyClass.setStatus("current")
_MesPolicyAction_Type = DisplayString
_MesPolicyAction_Object = MibTableColumn
mesPolicyAction = _MesPolicyAction_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 29, 1, 1, 6),
    _MesPolicyAction_Type()
)
mesPolicyAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesPolicyAction.setStatus("current")


class _MesPolicyServiceId_Type(ServiceIdWithNotUsed):
    """Custom type mesPolicyServiceId based on ServiceIdWithNotUsed"""
    defaultValue = -1


_MesPolicyServiceId_Type.__name__ = "ServiceIdWithNotUsed"
_MesPolicyServiceId_Object = MibTableColumn
mesPolicyServiceId = _MesPolicyServiceId_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 29, 1, 1, 7),
    _MesPolicyServiceId_Type()
)
mesPolicyServiceId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mesPolicyServiceId.setStatus("current")
_MesErrorPropList_ObjectIdentity = ObjectIdentity
mesErrorPropList = _MesErrorPropList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 30)
)
_MesErrorPropTable_Object = MibTable
mesErrorPropTable = _MesErrorPropTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 30, 1)
)
if mibBuilder.loadTexts:
    mesErrorPropTable.setStatus("current")
_MesErrorPropEntry_Object = MibTableRow
mesErrorPropEntry = _MesErrorPropEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 30, 1, 1)
)
mesErrorPropEntry.setIndexNames(
    (0, "LUM-MES-MIB", "mesErrorPropIndex"),
)
if mibBuilder.loadTexts:
    mesErrorPropEntry.setStatus("current")


class _MesErrorPropIndex_Type(Unsigned32):
    """Custom type mesErrorPropIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_MesErrorPropIndex_Type.__name__ = "Unsigned32"
_MesErrorPropIndex_Object = MibTableColumn
mesErrorPropIndex = _MesErrorPropIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 30, 1, 1, 1),
    _MesErrorPropIndex_Type()
)
mesErrorPropIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesErrorPropIndex.setStatus("current")
_MesErrorPropName_Type = MgmtNameString
_MesErrorPropName_Object = MibTableColumn
mesErrorPropName = _MesErrorPropName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 30, 1, 1, 2),
    _MesErrorPropName_Type()
)
mesErrorPropName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesErrorPropName.setStatus("current")


class _MesErrorPropDescr_Type(DisplayString):
    """Custom type mesErrorPropDescr based on DisplayString"""
    defaultValue = OctetString("")


_MesErrorPropDescr_Type.__name__ = "DisplayString"
_MesErrorPropDescr_Object = MibTableColumn
mesErrorPropDescr = _MesErrorPropDescr_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 30, 1, 1, 3),
    _MesErrorPropDescr_Type()
)
mesErrorPropDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mesErrorPropDescr.setStatus("current")


class _MesErrorPropInternalReference_Type(Unsigned32):
    """Custom type mesErrorPropInternalReference based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MesErrorPropInternalReference_Type.__name__ = "Unsigned32"
_MesErrorPropInternalReference_Object = MibTableColumn
mesErrorPropInternalReference = _MesErrorPropInternalReference_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 30, 1, 1, 4),
    _MesErrorPropInternalReference_Type()
)
mesErrorPropInternalReference.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesErrorPropInternalReference.setStatus("current")


class _MesErrorPropAdminStatus_Type(BoardOrInterfaceAdminStatus):
    """Custom type mesErrorPropAdminStatus based on BoardOrInterfaceAdminStatus"""
    defaultValue = 3


_MesErrorPropAdminStatus_Type.__name__ = "BoardOrInterfaceAdminStatus"
_MesErrorPropAdminStatus_Object = MibTableColumn
mesErrorPropAdminStatus = _MesErrorPropAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 30, 1, 1, 5),
    _MesErrorPropAdminStatus_Type()
)
mesErrorPropAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mesErrorPropAdminStatus.setStatus("current")


class _MesErrorPropOperStatus_Type(BoardOrInterfaceOperStatus):
    """Custom type mesErrorPropOperStatus based on BoardOrInterfaceOperStatus"""
    defaultValue = 2


_MesErrorPropOperStatus_Type.__name__ = "BoardOrInterfaceOperStatus"
_MesErrorPropOperStatus_Object = MibTableColumn
mesErrorPropOperStatus = _MesErrorPropOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 30, 1, 1, 6),
    _MesErrorPropOperStatus_Type()
)
mesErrorPropOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesErrorPropOperStatus.setStatus("current")


class _MesErrorPropState_Type(Integer32):
    """Custom type mesErrorPropState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 1),
          ("active", 2))
    )


_MesErrorPropState_Type.__name__ = "Integer32"
_MesErrorPropState_Object = MibTableColumn
mesErrorPropState = _MesErrorPropState_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 30, 1, 1, 7),
    _MesErrorPropState_Type()
)
mesErrorPropState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesErrorPropState.setStatus("current")


class _MesErrorPropTriggerType_Type(Integer32):
    """Custom type mesErrorPropTriggerType based on Integer32"""
    defaultValue = 1

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
        *(("mepStatus", 1),
          ("portStatus", 2),
          ("mepCsf", 3),
          ("lagStateChange", 4))
    )


_MesErrorPropTriggerType_Type.__name__ = "Integer32"
_MesErrorPropTriggerType_Object = MibTableColumn
mesErrorPropTriggerType = _MesErrorPropTriggerType_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 30, 1, 1, 8),
    _MesErrorPropTriggerType_Type()
)
mesErrorPropTriggerType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesErrorPropTriggerType.setStatus("current")
_MesErrorPropTriggerObject_Type = DisplayString
_MesErrorPropTriggerObject_Object = MibTableColumn
mesErrorPropTriggerObject = _MesErrorPropTriggerObject_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 30, 1, 1, 9),
    _MesErrorPropTriggerObject_Type()
)
mesErrorPropTriggerObject.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesErrorPropTriggerObject.setStatus("current")
_MesErrorPropTriggerPortIndex_Type = Unsigned32
_MesErrorPropTriggerPortIndex_Object = MibTableColumn
mesErrorPropTriggerPortIndex = _MesErrorPropTriggerPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 30, 1, 1, 10),
    _MesErrorPropTriggerPortIndex_Type()
)
mesErrorPropTriggerPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesErrorPropTriggerPortIndex.setStatus("current")
_MesErrorPropTriggerMepIndex_Type = Unsigned32
_MesErrorPropTriggerMepIndex_Object = MibTableColumn
mesErrorPropTriggerMepIndex = _MesErrorPropTriggerMepIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 30, 1, 1, 11),
    _MesErrorPropTriggerMepIndex_Type()
)
mesErrorPropTriggerMepIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesErrorPropTriggerMepIndex.setStatus("current")


class _MesErrorPropActionType_Type(Integer32):
    """Custom type mesErrorPropActionType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("laserShutdown", 1),
          ("sendCsf", 3),
          ("flushMacTable", 4),
          ("flushMacTableAll", 5),
          ("flushMacTableERPv2", 6))
    )


_MesErrorPropActionType_Type.__name__ = "Integer32"
_MesErrorPropActionType_Object = MibTableColumn
mesErrorPropActionType = _MesErrorPropActionType_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 30, 1, 1, 12),
    _MesErrorPropActionType_Type()
)
mesErrorPropActionType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesErrorPropActionType.setStatus("current")
_MesErrorPropActionObject_Type = DisplayString
_MesErrorPropActionObject_Object = MibTableColumn
mesErrorPropActionObject = _MesErrorPropActionObject_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 30, 1, 1, 13),
    _MesErrorPropActionObject_Type()
)
mesErrorPropActionObject.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesErrorPropActionObject.setStatus("current")
_MesErrorPropActionPortIndex_Type = Unsigned32
_MesErrorPropActionPortIndex_Object = MibTableColumn
mesErrorPropActionPortIndex = _MesErrorPropActionPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 30, 1, 1, 14),
    _MesErrorPropActionPortIndex_Type()
)
mesErrorPropActionPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesErrorPropActionPortIndex.setStatus("current")


class _MesErrorPropActionMepIndex_Type(Unsigned32):
    """Custom type mesErrorPropActionMepIndex based on Unsigned32"""
    defaultValue = 0


_MesErrorPropActionMepIndex_Type.__name__ = "Unsigned32"
_MesErrorPropActionMepIndex_Object = MibTableColumn
mesErrorPropActionMepIndex = _MesErrorPropActionMepIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 30, 1, 1, 15),
    _MesErrorPropActionMepIndex_Type()
)
mesErrorPropActionMepIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesErrorPropActionMepIndex.setStatus("current")


class _MesErrorPropHoldOffTimer_Type(Unsigned32):
    """Custom type mesErrorPropHoldOffTimer based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_MesErrorPropHoldOffTimer_Type.__name__ = "Unsigned32"
_MesErrorPropHoldOffTimer_Object = MibTableColumn
mesErrorPropHoldOffTimer = _MesErrorPropHoldOffTimer_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 30, 1, 1, 16),
    _MesErrorPropHoldOffTimer_Type()
)
mesErrorPropHoldOffTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mesErrorPropHoldOffTimer.setStatus("current")
_MesErrorPropRowStatus_Type = RowStatus
_MesErrorPropRowStatus_Object = MibTableColumn
mesErrorPropRowStatus = _MesErrorPropRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 30, 1, 1, 17),
    _MesErrorPropRowStatus_Type()
)
mesErrorPropRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesErrorPropRowStatus.setStatus("current")
_MesErrorPropFault_Type = FaultStatus
_MesErrorPropFault_Object = MibTableColumn
mesErrorPropFault = _MesErrorPropFault_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 30, 1, 1, 18),
    _MesErrorPropFault_Type()
)
mesErrorPropFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesErrorPropFault.setStatus("current")


class _MesErrorPropActionErpIndex_Type(Unsigned32):
    """Custom type mesErrorPropActionErpIndex based on Unsigned32"""
    defaultValue = 0


_MesErrorPropActionErpIndex_Type.__name__ = "Unsigned32"
_MesErrorPropActionErpIndex_Object = MibTableColumn
mesErrorPropActionErpIndex = _MesErrorPropActionErpIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 30, 1, 1, 19),
    _MesErrorPropActionErpIndex_Type()
)
mesErrorPropActionErpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesErrorPropActionErpIndex.setStatus("current")
_MesErrorPropTriggerLagIndex_Type = Unsigned32
_MesErrorPropTriggerLagIndex_Object = MibTableColumn
mesErrorPropTriggerLagIndex = _MesErrorPropTriggerLagIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 30, 1, 1, 20),
    _MesErrorPropTriggerLagIndex_Type()
)
mesErrorPropTriggerLagIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesErrorPropTriggerLagIndex.setStatus("current")
_MesErrorPropSubrack_Type = SubrackNumber
_MesErrorPropSubrack_Object = MibTableColumn
mesErrorPropSubrack = _MesErrorPropSubrack_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 30, 1, 1, 21),
    _MesErrorPropSubrack_Type()
)
mesErrorPropSubrack.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesErrorPropSubrack.setStatus("current")
_MesErrorPropSlot_Type = SlotNumber
_MesErrorPropSlot_Object = MibTableColumn
mesErrorPropSlot = _MesErrorPropSlot_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 30, 1, 1, 22),
    _MesErrorPropSlot_Type()
)
mesErrorPropSlot.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesErrorPropSlot.setStatus("current")


class _MesErrorPropServiceId_Type(ServiceIdWithNotUsed):
    """Custom type mesErrorPropServiceId based on ServiceIdWithNotUsed"""
    defaultValue = -1


_MesErrorPropServiceId_Type.__name__ = "ServiceIdWithNotUsed"
_MesErrorPropServiceId_Object = MibTableColumn
mesErrorPropServiceId = _MesErrorPropServiceId_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 30, 1, 1, 23),
    _MesErrorPropServiceId_Type()
)
mesErrorPropServiceId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mesErrorPropServiceId.setStatus("current")
_MesVlanProtList_ObjectIdentity = ObjectIdentity
mesVlanProtList = _MesVlanProtList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 31)
)
_MesVlanProtTable_Object = MibTable
mesVlanProtTable = _MesVlanProtTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 31, 1)
)
if mibBuilder.loadTexts:
    mesVlanProtTable.setStatus("current")
_MesVlanProtEntry_Object = MibTableRow
mesVlanProtEntry = _MesVlanProtEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 31, 1, 1)
)
mesVlanProtEntry.setIndexNames(
    (0, "LUM-MES-MIB", "mesVlanProtIndex"),
)
if mibBuilder.loadTexts:
    mesVlanProtEntry.setStatus("current")


class _MesVlanProtIndex_Type(Unsigned32):
    """Custom type mesVlanProtIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_MesVlanProtIndex_Type.__name__ = "Unsigned32"
_MesVlanProtIndex_Object = MibTableColumn
mesVlanProtIndex = _MesVlanProtIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 31, 1, 1, 1),
    _MesVlanProtIndex_Type()
)
mesVlanProtIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesVlanProtIndex.setStatus("current")
_MesVlanProtName_Type = MgmtNameString
_MesVlanProtName_Object = MibTableColumn
mesVlanProtName = _MesVlanProtName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 31, 1, 1, 2),
    _MesVlanProtName_Type()
)
mesVlanProtName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesVlanProtName.setStatus("current")


class _MesVlanProtInternalReference_Type(Unsigned32):
    """Custom type mesVlanProtInternalReference based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MesVlanProtInternalReference_Type.__name__ = "Unsigned32"
_MesVlanProtInternalReference_Object = MibTableColumn
mesVlanProtInternalReference = _MesVlanProtInternalReference_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 31, 1, 1, 3),
    _MesVlanProtInternalReference_Type()
)
mesVlanProtInternalReference.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesVlanProtInternalReference.setStatus("current")


class _MesVlanProtRings_Type(Counter64):
    """Custom type mesVlanProtRings based on Counter64"""
    defaultValue = 0


_MesVlanProtRings_Type.__name__ = "Counter64"
_MesVlanProtRings_Object = MibTableColumn
mesVlanProtRings = _MesVlanProtRings_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 31, 1, 1, 4),
    _MesVlanProtRings_Type()
)
mesVlanProtRings.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesVlanProtRings.setStatus("current")


class _MesVlanProtProtectedVlan_Type(DisplayString):
    """Custom type mesVlanProtProtectedVlan based on DisplayString"""
    defaultValue = OctetString("")


_MesVlanProtProtectedVlan_Type.__name__ = "DisplayString"
_MesVlanProtProtectedVlan_Object = MibTableColumn
mesVlanProtProtectedVlan = _MesVlanProtProtectedVlan_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 31, 1, 1, 5),
    _MesVlanProtProtectedVlan_Type()
)
mesVlanProtProtectedVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mesVlanProtProtectedVlan.setStatus("current")


class _MesVlanProtGroupId_Type(Unsigned32):
    """Custom type mesVlanProtGroupId based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MesVlanProtGroupId_Type.__name__ = "Unsigned32"
_MesVlanProtGroupId_Object = MibTableColumn
mesVlanProtGroupId = _MesVlanProtGroupId_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 31, 1, 1, 6),
    _MesVlanProtGroupId_Type()
)
mesVlanProtGroupId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesVlanProtGroupId.setStatus("current")


class _MesVlanProtIdentifier_Type(DisplayString):
    """Custom type mesVlanProtIdentifier based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 19),
    )


_MesVlanProtIdentifier_Type.__name__ = "DisplayString"
_MesVlanProtIdentifier_Object = MibTableColumn
mesVlanProtIdentifier = _MesVlanProtIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 31, 1, 1, 7),
    _MesVlanProtIdentifier_Type()
)
mesVlanProtIdentifier.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesVlanProtIdentifier.setStatus("current")
_MesVlanProtAddRingAction_Type = CommandString
_MesVlanProtAddRingAction_Object = MibTableColumn
mesVlanProtAddRingAction = _MesVlanProtAddRingAction_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 31, 1, 1, 8),
    _MesVlanProtAddRingAction_Type()
)
mesVlanProtAddRingAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesVlanProtAddRingAction.setStatus("current")
_MesVlanProtRemoveRingAction_Type = CommandString
_MesVlanProtRemoveRingAction_Object = MibTableColumn
mesVlanProtRemoveRingAction = _MesVlanProtRemoveRingAction_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 31, 1, 1, 9),
    _MesVlanProtRemoveRingAction_Type()
)
mesVlanProtRemoveRingAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesVlanProtRemoveRingAction.setStatus("current")


class _MesVlanProtDescr_Type(DisplayString):
    """Custom type mesVlanProtDescr based on DisplayString"""
    defaultValue = OctetString("")


_MesVlanProtDescr_Type.__name__ = "DisplayString"
_MesVlanProtDescr_Object = MibTableColumn
mesVlanProtDescr = _MesVlanProtDescr_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 31, 1, 1, 10),
    _MesVlanProtDescr_Type()
)
mesVlanProtDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mesVlanProtDescr.setStatus("current")
_MesVlanProtChangeVlansAction_Type = CommandString
_MesVlanProtChangeVlansAction_Object = MibTableColumn
mesVlanProtChangeVlansAction = _MesVlanProtChangeVlansAction_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 31, 1, 1, 11),
    _MesVlanProtChangeVlansAction_Type()
)
mesVlanProtChangeVlansAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesVlanProtChangeVlansAction.setStatus("current")
_MesLacpList_ObjectIdentity = ObjectIdentity
mesLacpList = _MesLacpList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 32)
)
_MesLacpTable_Object = MibTable
mesLacpTable = _MesLacpTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 32, 1)
)
if mibBuilder.loadTexts:
    mesLacpTable.setStatus("current")
_MesLacpEntry_Object = MibTableRow
mesLacpEntry = _MesLacpEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 32, 1, 1)
)
mesLacpEntry.setIndexNames(
    (0, "LUM-MES-MIB", "mesLacpIndex"),
)
if mibBuilder.loadTexts:
    mesLacpEntry.setStatus("current")


class _MesLacpIndex_Type(Unsigned32):
    """Custom type mesLacpIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_MesLacpIndex_Type.__name__ = "Unsigned32"
_MesLacpIndex_Object = MibTableColumn
mesLacpIndex = _MesLacpIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 32, 1, 1, 1),
    _MesLacpIndex_Type()
)
mesLacpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesLacpIndex.setStatus("current")
_MesLacpName_Type = MgmtNameString
_MesLacpName_Object = MibTableColumn
mesLacpName = _MesLacpName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 32, 1, 1, 2),
    _MesLacpName_Type()
)
mesLacpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesLacpName.setStatus("current")


class _MesLacpInternalReference_Type(Unsigned32):
    """Custom type mesLacpInternalReference based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MesLacpInternalReference_Type.__name__ = "Unsigned32"
_MesLacpInternalReference_Object = MibTableColumn
mesLacpInternalReference = _MesLacpInternalReference_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 32, 1, 1, 3),
    _MesLacpInternalReference_Type()
)
mesLacpInternalReference.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesLacpInternalReference.setStatus("current")
_MesLacpLagIdentifier_Type = DisplayString
_MesLacpLagIdentifier_Object = MibTableColumn
mesLacpLagIdentifier = _MesLacpLagIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 32, 1, 1, 4),
    _MesLacpLagIdentifier_Type()
)
mesLacpLagIdentifier.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesLacpLagIdentifier.setStatus("current")
_MesLacpLagId_Type = DisplayString
_MesLacpLagId_Object = MibTableColumn
mesLacpLagId = _MesLacpLagId_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 32, 1, 1, 5),
    _MesLacpLagId_Type()
)
mesLacpLagId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesLacpLagId.setStatus("current")


class _MesLacpPortPriority_Type(Unsigned32):
    """Custom type mesLacpPortPriority based on Unsigned32"""
    defaultValue = 32768

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MesLacpPortPriority_Type.__name__ = "Unsigned32"
_MesLacpPortPriority_Object = MibTableColumn
mesLacpPortPriority = _MesLacpPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 32, 1, 1, 6),
    _MesLacpPortPriority_Type()
)
mesLacpPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mesLacpPortPriority.setStatus("current")


class _MesLacpSelected_Type(Integer32):
    """Custom type mesLacpSelected based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unselected", 0),
          ("selected", 1),
          ("standby", 2))
    )


_MesLacpSelected_Type.__name__ = "Integer32"
_MesLacpSelected_Object = MibTableColumn
mesLacpSelected = _MesLacpSelected_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 32, 1, 1, 7),
    _MesLacpSelected_Type()
)
mesLacpSelected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesLacpSelected.setStatus("current")


class _MesLacpReceiveState_Type(Integer32):
    """Custom type mesLacpReceiveState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("expired", 0),
          ("defaulted", 1),
          ("current", 2))
    )


_MesLacpReceiveState_Type.__name__ = "Integer32"
_MesLacpReceiveState_Object = MibTableColumn
mesLacpReceiveState = _MesLacpReceiveState_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 32, 1, 1, 8),
    _MesLacpReceiveState_Type()
)
mesLacpReceiveState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesLacpReceiveState.setStatus("current")


class _MesLacpTransmitState_Type(Integer32):
    """Custom type mesLacpTransmitState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("slowPeriodic", 0),
          ("fastPeriodic", 1))
    )


_MesLacpTransmitState_Type.__name__ = "Integer32"
_MesLacpTransmitState_Object = MibTableColumn
mesLacpTransmitState = _MesLacpTransmitState_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 32, 1, 1, 9),
    _MesLacpTransmitState_Type()
)
mesLacpTransmitState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesLacpTransmitState.setStatus("current")


class _MesLacpMuxState_Type(Integer32):
    """Custom type mesLacpMuxState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("detached", 0),
          ("attached", 1),
          ("collectingDistributing", 2))
    )


_MesLacpMuxState_Type.__name__ = "Integer32"
_MesLacpMuxState_Object = MibTableColumn
mesLacpMuxState = _MesLacpMuxState_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 32, 1, 1, 10),
    _MesLacpMuxState_Type()
)
mesLacpMuxState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesLacpMuxState.setStatus("current")


class _MesLacpActorExpired_Type(Integer32):
    """Custom type mesLacpActorExpired based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_MesLacpActorExpired_Type.__name__ = "Integer32"
_MesLacpActorExpired_Object = MibTableColumn
mesLacpActorExpired = _MesLacpActorExpired_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 32, 1, 1, 11),
    _MesLacpActorExpired_Type()
)
mesLacpActorExpired.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesLacpActorExpired.setStatus("current")


class _MesLacpActorDefault_Type(Integer32):
    """Custom type mesLacpActorDefault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_MesLacpActorDefault_Type.__name__ = "Integer32"
_MesLacpActorDefault_Object = MibTableColumn
mesLacpActorDefault = _MesLacpActorDefault_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 32, 1, 1, 12),
    _MesLacpActorDefault_Type()
)
mesLacpActorDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesLacpActorDefault.setStatus("current")


class _MesLacpActorDistributing_Type(Integer32):
    """Custom type mesLacpActorDistributing based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_MesLacpActorDistributing_Type.__name__ = "Integer32"
_MesLacpActorDistributing_Object = MibTableColumn
mesLacpActorDistributing = _MesLacpActorDistributing_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 32, 1, 1, 13),
    _MesLacpActorDistributing_Type()
)
mesLacpActorDistributing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesLacpActorDistributing.setStatus("current")


class _MesLacpActorCollecting_Type(Integer32):
    """Custom type mesLacpActorCollecting based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_MesLacpActorCollecting_Type.__name__ = "Integer32"
_MesLacpActorCollecting_Object = MibTableColumn
mesLacpActorCollecting = _MesLacpActorCollecting_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 32, 1, 1, 14),
    _MesLacpActorCollecting_Type()
)
mesLacpActorCollecting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesLacpActorCollecting.setStatus("current")


class _MesLacpActorSynchronization_Type(Integer32):
    """Custom type mesLacpActorSynchronization based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("outOfSync", 0),
          ("inSync", 1))
    )


_MesLacpActorSynchronization_Type.__name__ = "Integer32"
_MesLacpActorSynchronization_Object = MibTableColumn
mesLacpActorSynchronization = _MesLacpActorSynchronization_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 32, 1, 1, 15),
    _MesLacpActorSynchronization_Type()
)
mesLacpActorSynchronization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesLacpActorSynchronization.setStatus("current")


class _MesLacpActorAggregation_Type(Integer32):
    """Custom type mesLacpActorAggregation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_MesLacpActorAggregation_Type.__name__ = "Integer32"
_MesLacpActorAggregation_Object = MibTableColumn
mesLacpActorAggregation = _MesLacpActorAggregation_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 32, 1, 1, 16),
    _MesLacpActorAggregation_Type()
)
mesLacpActorAggregation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesLacpActorAggregation.setStatus("current")


class _MesLacpActorTimeout_Type(Integer32):
    """Custom type mesLacpActorTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("slowPeriodic", 0),
          ("fastPeriodic", 1))
    )


_MesLacpActorTimeout_Type.__name__ = "Integer32"
_MesLacpActorTimeout_Object = MibTableColumn
mesLacpActorTimeout = _MesLacpActorTimeout_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 32, 1, 1, 17),
    _MesLacpActorTimeout_Type()
)
mesLacpActorTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesLacpActorTimeout.setStatus("current")


class _MesLacpActorActivity_Type(Integer32):
    """Custom type mesLacpActorActivity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("passive", 0),
          ("active", 1))
    )


_MesLacpActorActivity_Type.__name__ = "Integer32"
_MesLacpActorActivity_Object = MibTableColumn
mesLacpActorActivity = _MesLacpActorActivity_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 32, 1, 1, 18),
    _MesLacpActorActivity_Type()
)
mesLacpActorActivity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesLacpActorActivity.setStatus("current")


class _MesLacpPartnerExpired_Type(Integer32):
    """Custom type mesLacpPartnerExpired based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_MesLacpPartnerExpired_Type.__name__ = "Integer32"
_MesLacpPartnerExpired_Object = MibTableColumn
mesLacpPartnerExpired = _MesLacpPartnerExpired_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 32, 1, 1, 19),
    _MesLacpPartnerExpired_Type()
)
mesLacpPartnerExpired.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesLacpPartnerExpired.setStatus("current")


class _MesLacpPartnerDefault_Type(Integer32):
    """Custom type mesLacpPartnerDefault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_MesLacpPartnerDefault_Type.__name__ = "Integer32"
_MesLacpPartnerDefault_Object = MibTableColumn
mesLacpPartnerDefault = _MesLacpPartnerDefault_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 32, 1, 1, 20),
    _MesLacpPartnerDefault_Type()
)
mesLacpPartnerDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesLacpPartnerDefault.setStatus("current")


class _MesLacpPartnerDistributing_Type(Integer32):
    """Custom type mesLacpPartnerDistributing based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_MesLacpPartnerDistributing_Type.__name__ = "Integer32"
_MesLacpPartnerDistributing_Object = MibTableColumn
mesLacpPartnerDistributing = _MesLacpPartnerDistributing_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 32, 1, 1, 21),
    _MesLacpPartnerDistributing_Type()
)
mesLacpPartnerDistributing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesLacpPartnerDistributing.setStatus("current")


class _MesLacpPartnerCollecting_Type(Integer32):
    """Custom type mesLacpPartnerCollecting based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_MesLacpPartnerCollecting_Type.__name__ = "Integer32"
_MesLacpPartnerCollecting_Object = MibTableColumn
mesLacpPartnerCollecting = _MesLacpPartnerCollecting_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 32, 1, 1, 22),
    _MesLacpPartnerCollecting_Type()
)
mesLacpPartnerCollecting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesLacpPartnerCollecting.setStatus("current")


class _MesLacpPartnerSynchronization_Type(Integer32):
    """Custom type mesLacpPartnerSynchronization based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("outOfSync", 0),
          ("inSync", 1))
    )


_MesLacpPartnerSynchronization_Type.__name__ = "Integer32"
_MesLacpPartnerSynchronization_Object = MibTableColumn
mesLacpPartnerSynchronization = _MesLacpPartnerSynchronization_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 32, 1, 1, 23),
    _MesLacpPartnerSynchronization_Type()
)
mesLacpPartnerSynchronization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesLacpPartnerSynchronization.setStatus("current")


class _MesLacpPartnerAggregation_Type(Integer32):
    """Custom type mesLacpPartnerAggregation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_MesLacpPartnerAggregation_Type.__name__ = "Integer32"
_MesLacpPartnerAggregation_Object = MibTableColumn
mesLacpPartnerAggregation = _MesLacpPartnerAggregation_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 32, 1, 1, 24),
    _MesLacpPartnerAggregation_Type()
)
mesLacpPartnerAggregation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesLacpPartnerAggregation.setStatus("current")


class _MesLacpPartnerTimeout_Type(Integer32):
    """Custom type mesLacpPartnerTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("slowPeriodic", 0),
          ("fastPeriodic", 1))
    )


_MesLacpPartnerTimeout_Type.__name__ = "Integer32"
_MesLacpPartnerTimeout_Object = MibTableColumn
mesLacpPartnerTimeout = _MesLacpPartnerTimeout_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 32, 1, 1, 25),
    _MesLacpPartnerTimeout_Type()
)
mesLacpPartnerTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesLacpPartnerTimeout.setStatus("current")


class _MesLacpPartnerActivity_Type(Integer32):
    """Custom type mesLacpPartnerActivity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("passive", 0),
          ("active", 1))
    )


_MesLacpPartnerActivity_Type.__name__ = "Integer32"
_MesLacpPartnerActivity_Object = MibTableColumn
mesLacpPartnerActivity = _MesLacpPartnerActivity_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 32, 1, 1, 26),
    _MesLacpPartnerActivity_Type()
)
mesLacpPartnerActivity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesLacpPartnerActivity.setStatus("current")
_MesLacpTxLacpPdus_Type = Counter64
_MesLacpTxLacpPdus_Object = MibTableColumn
mesLacpTxLacpPdus = _MesLacpTxLacpPdus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 32, 1, 1, 27),
    _MesLacpTxLacpPdus_Type()
)
mesLacpTxLacpPdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesLacpTxLacpPdus.setStatus("current")
_MesLacpRxLacpPdus_Type = Counter64
_MesLacpRxLacpPdus_Object = MibTableColumn
mesLacpRxLacpPdus = _MesLacpRxLacpPdus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 32, 1, 1, 28),
    _MesLacpRxLacpPdus_Type()
)
mesLacpRxLacpPdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesLacpRxLacpPdus.setStatus("current")


class _MesLacpInternalIndex_Type(Unsigned32):
    """Custom type mesLacpInternalIndex based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MesLacpInternalIndex_Type.__name__ = "Unsigned32"
_MesLacpInternalIndex_Object = MibTableColumn
mesLacpInternalIndex = _MesLacpInternalIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 32, 1, 1, 29),
    _MesLacpInternalIndex_Type()
)
mesLacpInternalIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesLacpInternalIndex.setStatus("current")


class _MesLacpResetCounters_Type(Integer32):
    """Custom type mesLacpResetCounters based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("reset", 2))
    )


_MesLacpResetCounters_Type.__name__ = "Integer32"
_MesLacpResetCounters_Object = MibTableColumn
mesLacpResetCounters = _MesLacpResetCounters_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 32, 1, 1, 30),
    _MesLacpResetCounters_Type()
)
mesLacpResetCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mesLacpResetCounters.setStatus("current")


class _MesLacpIfNo_Type(PortNumber):
    """Custom type mesLacpIfNo based on PortNumber"""
    defaultValue = 1


_MesLacpIfNo_Type.__name__ = "PortNumber"
_MesLacpIfNo_Object = MibTableColumn
mesLacpIfNo = _MesLacpIfNo_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 32, 1, 1, 31),
    _MesLacpIfNo_Type()
)
mesLacpIfNo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesLacpIfNo.setStatus("current")


class _MesLacpTxPort_Type(PortNumber):
    """Custom type mesLacpTxPort based on PortNumber"""
    defaultValue = 0


_MesLacpTxPort_Type.__name__ = "PortNumber"
_MesLacpTxPort_Object = MibTableColumn
mesLacpTxPort = _MesLacpTxPort_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 32, 1, 1, 32),
    _MesLacpTxPort_Type()
)
mesLacpTxPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mesLacpTxPort.setStatus("current")


class _MesLacpUpPortId_Type(Integer32):
    """Custom type mesLacpUpPortId based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_MesLacpUpPortId_Type.__name__ = "Integer32"
_MesLacpUpPortId_Object = MibTableColumn
mesLacpUpPortId = _MesLacpUpPortId_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 2, 32, 1, 1, 33),
    _MesLacpUpPortId_Type()
)
mesLacpUpPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mesLacpUpPortId.setStatus("current")

# Managed Objects groups

mesGeneralGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 1, 1, 1)
)
mesGeneralGroup.setObjects(
      *(("LUM-MES-MIB", "mesGeneralConfigLastChangeTime"),
        ("LUM-MES-MIB", "mesGeneralStateLastChangeTime"),
        ("LUM-MES-MIB", "mesGeneralUniTableSize"),
        ("LUM-MES-MIB", "mesGeneralNniTableSize"),
        ("LUM-MES-MIB", "mesGeneralEvcTableSize"),
        ("LUM-MES-MIB", "mesGeneralBwpTableSize"),
        ("LUM-MES-MIB", "mesGeneralCeEvcMapTableSize"))
)
if mibBuilder.loadTexts:
    mesGeneralGroup.setStatus("deprecated")

mesUniGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 1, 1, 2)
)
mesUniGroup.setObjects(
      *(("LUM-MES-MIB", "mesUniIndex"),
        ("LUM-MES-MIB", "mesUniName"),
        ("LUM-MES-MIB", "mesUniDescr"),
        ("LUM-MES-MIB", "mesUniSubrack"),
        ("LUM-MES-MIB", "mesUniSlot"),
        ("LUM-MES-MIB", "mesUniTxPort"),
        ("LUM-MES-MIB", "mesUniRxPort"),
        ("LUM-MES-MIB", "mesUniObjectProperty"),
        ("LUM-MES-MIB", "mesUniAdminStatus"),
        ("LUM-MES-MIB", "mesUniOperStatus"),
        ("LUM-MES-MIB", "mesUniIdentifier"),
        ("LUM-MES-MIB", "mesUniMtuSize"),
        ("LUM-MES-MIB", "mesUniMaxNoOfEvcs"),
        ("LUM-MES-MIB", "mesUniCurrentNoOfEvcs"),
        ("LUM-MES-MIB", "mesUniAvailableCapacity"),
        ("LUM-MES-MIB", "mesUniServiceMultiplexing"),
        ("LUM-MES-MIB", "mesUniBundling"),
        ("LUM-MES-MIB", "mesUniAllToOneBundling"),
        ("LUM-MES-MIB", "mesUniUntaggedCeVlanIdAssignment"),
        ("LUM-MES-MIB", "mesUniAssociateBwp"),
        ("LUM-MES-MIB", "mesUniReleaseBwp"),
        ("LUM-MES-MIB", "mesUniIngressBwProfilePerUni"),
        ("LUM-MES-MIB", "mesUniIngressBwp"),
        ("LUM-MES-MIB", "mesUniEgressBwProfilePerUni"),
        ("LUM-MES-MIB", "mesUniEgressBwp"),
        ("LUM-MES-MIB", "mesUniL2ControlProtocolProcessing"),
        ("LUM-MES-MIB", "mesUniSetupCommand"),
        ("LUM-MES-MIB", "mesUniCreateEvcCommand"),
        ("LUM-MES-MIB", "mesUniListCeVlanIdsCommand"),
        ("LUM-MES-MIB", "mesUniTaggingOfUntaggedFrames"),
        ("LUM-MES-MIB", "mesUniCeVlanIdAssignmentCommand"))
)
if mibBuilder.loadTexts:
    mesUniGroup.setStatus("deprecated")

mesNniGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 1, 1, 3)
)
mesNniGroup.setObjects(
      *(("LUM-MES-MIB", "mesNniIndex"),
        ("LUM-MES-MIB", "mesNniName"),
        ("LUM-MES-MIB", "mesNniDescr"),
        ("LUM-MES-MIB", "mesNniSubrack"),
        ("LUM-MES-MIB", "mesNniSlot"),
        ("LUM-MES-MIB", "mesNniTxPort"),
        ("LUM-MES-MIB", "mesNniRxPort"),
        ("LUM-MES-MIB", "mesNniObjectProperty"),
        ("LUM-MES-MIB", "mesNniAdminStatus"),
        ("LUM-MES-MIB", "mesNniOperStatus"),
        ("LUM-MES-MIB", "mesNniIdentifier"),
        ("LUM-MES-MIB", "mesNniCurrentNoOfEvcs"),
        ("LUM-MES-MIB", "mesNniAvailableCapacity"),
        ("LUM-MES-MIB", "mesNniDefineMgmtVlan"),
        ("LUM-MES-MIB", "mesNniMgmtVlanTagType"),
        ("LUM-MES-MIB", "mesNniMgmtVlanEtherType"),
        ("LUM-MES-MIB", "mesNniMgmtVlanVlanId"),
        ("LUM-MES-MIB", "mesNniMgmtVlanPriority"),
        ("LUM-MES-MIB", "mesNniMgmtVlanIpAddress"),
        ("LUM-MES-MIB", "mesNniMgmtVlanNetMask"),
        ("LUM-MES-MIB", "mesNniMgmtVlanMacAddress"))
)
if mibBuilder.loadTexts:
    mesNniGroup.setStatus("deprecated")

mesEvcGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 1, 1, 4)
)
mesEvcGroup.setObjects(
      *(("LUM-MES-MIB", "mesEvcIndex"),
        ("LUM-MES-MIB", "mesEvcName"),
        ("LUM-MES-MIB", "mesEvcDescr"),
        ("LUM-MES-MIB", "mesEvcObjectProperty"),
        ("LUM-MES-MIB", "mesEvcAdminStatus"),
        ("LUM-MES-MIB", "mesEvcOperStatus"),
        ("LUM-MES-MIB", "mesEvcIdentifier"),
        ("LUM-MES-MIB", "mesEvcUniIdentifier"),
        ("LUM-MES-MIB", "mesEvcNniIdentifier"),
        ("LUM-MES-MIB", "mesEvcType"),
        ("LUM-MES-MIB", "mesEvcMtuSize"),
        ("LUM-MES-MIB", "mesEvcFrameDeliveryUnicast"),
        ("LUM-MES-MIB", "mesEvcFrameDeliveryMulticast"),
        ("LUM-MES-MIB", "mesEvcFrameDeliveryBroadcast"),
        ("LUM-MES-MIB", "mesEvcDefineL2Control"),
        ("LUM-MES-MIB", "mesEvcL2ControlProtocolDisposition"),
        ("LUM-MES-MIB", "mesEvcL2DestinationMacAddress"),
        ("LUM-MES-MIB", "mesEvcCeVlanIdPreservation"),
        ("LUM-MES-MIB", "mesEvcCosPreservation"),
        ("LUM-MES-MIB", "mesEvcAssociateBwp"),
        ("LUM-MES-MIB", "mesEvcReleaseBwp"),
        ("LUM-MES-MIB", "mesEvcIngressBwProfilePerEvc"),
        ("LUM-MES-MIB", "mesEvcIngressBwp"),
        ("LUM-MES-MIB", "mesEvcEgressBwProfilePerEvc"),
        ("LUM-MES-MIB", "mesEvcEgressBwp"),
        ("LUM-MES-MIB", "mesEvcCreateCeVlanIdMap"),
        ("LUM-MES-MIB", "mesEvcDefineProviderTag"),
        ("LUM-MES-MIB", "mesEvcProviderTagType"),
        ("LUM-MES-MIB", "mesEvcProviderTagEtherType"),
        ("LUM-MES-MIB", "mesEvcProviderTagVlanId"),
        ("LUM-MES-MIB", "mesEvcDefineClassOfService"),
        ("LUM-MES-MIB", "mesEvcCoSClassification"),
        ("LUM-MES-MIB", "mesEvcCoSPriority"),
        ("LUM-MES-MIB", "mesEvcInternalReference"))
)
if mibBuilder.loadTexts:
    mesEvcGroup.setStatus("deprecated")

mesCeEvcMapGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 1, 1, 5)
)
mesCeEvcMapGroup.setObjects(
      *(("LUM-MES-MIB", "mesCeEvcMapIndex"),
        ("LUM-MES-MIB", "mesCeEvcMapName"),
        ("LUM-MES-MIB", "mesCeEvcMapObjectProperty"),
        ("LUM-MES-MIB", "mesCeEvcMapType"),
        ("LUM-MES-MIB", "mesCeEvcMapVlanIdRangeLower"),
        ("LUM-MES-MIB", "mesCeEvcMapVlanIdRangeUpper"),
        ("LUM-MES-MIB", "mesCeEvcMapEvcId"),
        ("LUM-MES-MIB", "mesCeEvcMapInternalReference"))
)
if mibBuilder.loadTexts:
    mesCeEvcMapGroup.setStatus("deprecated")

mesBwpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 1, 1, 6)
)
mesBwpGroup.setObjects(
      *(("LUM-MES-MIB", "mesBwpIndex"),
        ("LUM-MES-MIB", "mesBwpName"),
        ("LUM-MES-MIB", "mesBwpObjectProperty"),
        ("LUM-MES-MIB", "mesBwpCoSIdentifier"),
        ("LUM-MES-MIB", "mesBwpCir"),
        ("LUM-MES-MIB", "mesBwpCbs"),
        ("LUM-MES-MIB", "mesBwpEir"),
        ("LUM-MES-MIB", "mesBwpEbs"),
        ("LUM-MES-MIB", "mesBwpCouplingFlag"),
        ("LUM-MES-MIB", "mesBwpColorMode"),
        ("LUM-MES-MIB", "mesBwpInternalReference"))
)
if mibBuilder.loadTexts:
    mesBwpGroup.setStatus("deprecated")

mesCeEvcMapGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 1, 1, 7)
)
mesCeEvcMapGroupV2.setObjects(
      *(("LUM-MES-MIB", "mesCeEvcMapIndex"),
        ("LUM-MES-MIB", "mesCeEvcMapName"),
        ("LUM-MES-MIB", "mesCeEvcMapObjectProperty"),
        ("LUM-MES-MIB", "mesCeEvcMapType"),
        ("LUM-MES-MIB", "mesCeEvcMapVlanIdRangeLower"),
        ("LUM-MES-MIB", "mesCeEvcMapVlanIdRangeUpper"),
        ("LUM-MES-MIB", "mesCeEvcMapEvcId"),
        ("LUM-MES-MIB", "mesCeEvcMapInternalReference"),
        ("LUM-MES-MIB", "mesCeEvcMapRowStatus"),
        ("LUM-MES-MIB", "mesCeEvcMapPrio0Included"),
        ("LUM-MES-MIB", "mesCeEvcMapPrio1Included"),
        ("LUM-MES-MIB", "mesCeEvcMapPrio2Included"),
        ("LUM-MES-MIB", "mesCeEvcMapPrio3Included"),
        ("LUM-MES-MIB", "mesCeEvcMapPrio4Included"),
        ("LUM-MES-MIB", "mesCeEvcMapPrio5Included"),
        ("LUM-MES-MIB", "mesCeEvcMapPrio6Included"),
        ("LUM-MES-MIB", "mesCeEvcMapPrio7Included"),
        ("LUM-MES-MIB", "mesCeEvcMapDefaultCeVlanId"),
        ("LUM-MES-MIB", "mesCeEvcMapPrioIncluded"))
)
if mibBuilder.loadTexts:
    mesCeEvcMapGroupV2.setStatus("current")

mesBwpGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 1, 1, 8)
)
mesBwpGroupV2.setObjects(
      *(("LUM-MES-MIB", "mesBwpIndex"),
        ("LUM-MES-MIB", "mesBwpName"),
        ("LUM-MES-MIB", "mesBwpObjectProperty"),
        ("LUM-MES-MIB", "mesBwpCoSIdentifier"),
        ("LUM-MES-MIB", "mesBwpCir"),
        ("LUM-MES-MIB", "mesBwpCbs"),
        ("LUM-MES-MIB", "mesBwpEir"),
        ("LUM-MES-MIB", "mesBwpEbs"),
        ("LUM-MES-MIB", "mesBwpCouplingFlag"),
        ("LUM-MES-MIB", "mesBwpColorMode"),
        ("LUM-MES-MIB", "mesBwpInternalReference"),
        ("LUM-MES-MIB", "mesBwpRowStatus"))
)
if mibBuilder.loadTexts:
    mesBwpGroupV2.setStatus("deprecated")

mesUniGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 1, 1, 9)
)
mesUniGroupV2.setObjects(
      *(("LUM-MES-MIB", "mesUniIndex"),
        ("LUM-MES-MIB", "mesUniName"),
        ("LUM-MES-MIB", "mesUniDescr"),
        ("LUM-MES-MIB", "mesUniSubrack"),
        ("LUM-MES-MIB", "mesUniSlot"),
        ("LUM-MES-MIB", "mesUniTxPort"),
        ("LUM-MES-MIB", "mesUniRxPort"),
        ("LUM-MES-MIB", "mesUniObjectProperty"),
        ("LUM-MES-MIB", "mesUniAdminStatus"),
        ("LUM-MES-MIB", "mesUniOperStatus"),
        ("LUM-MES-MIB", "mesUniIdentifier"),
        ("LUM-MES-MIB", "mesUniMtuSize"),
        ("LUM-MES-MIB", "mesUniMaxNoOfEvcs"),
        ("LUM-MES-MIB", "mesUniCurrentNoOfEvcs"),
        ("LUM-MES-MIB", "mesUniAvailableCapacity"),
        ("LUM-MES-MIB", "mesUniServiceMultiplexing"),
        ("LUM-MES-MIB", "mesUniBundling"),
        ("LUM-MES-MIB", "mesUniAllToOneBundling"),
        ("LUM-MES-MIB", "mesUniUntaggedCeVlanIdAssignment"),
        ("LUM-MES-MIB", "mesUniAssociateBwp"),
        ("LUM-MES-MIB", "mesUniReleaseBwp"),
        ("LUM-MES-MIB", "mesUniIngressBwProfilePerUni"),
        ("LUM-MES-MIB", "mesUniIngressBwp"),
        ("LUM-MES-MIB", "mesUniEgressBwProfilePerUni"),
        ("LUM-MES-MIB", "mesUniEgressBwp"),
        ("LUM-MES-MIB", "mesUniSetupCommand"),
        ("LUM-MES-MIB", "mesUniCreateEvcCommand"),
        ("LUM-MES-MIB", "mesUniListCeVlanIdsCommand"),
        ("LUM-MES-MIB", "mesUniTaggingOfUntaggedFrames"),
        ("LUM-MES-MIB", "mesUniCeVlanIdAssignmentCommand"),
        ("LUM-MES-MIB", "mesUniL2SpanningTreeProcessing"),
        ("LUM-MES-MIB", "mesUniL2PauseProcessing"),
        ("LUM-MES-MIB", "mesUniL2SlowProtocolsProcessing"),
        ("LUM-MES-MIB", "mesUniL2PortAuthenticationProcessing"),
        ("LUM-MES-MIB", "mesUniL2OtherBridgeBlockProcessing"),
        ("LUM-MES-MIB", "mesUniL2AllLANsBridgeMgmtProcessing"),
        ("LUM-MES-MIB", "mesUniL2GarpProcessing"),
        ("LUM-MES-MIB", "mesUniL2OamUniMeProcessing"))
)
if mibBuilder.loadTexts:
    mesUniGroupV2.setStatus("deprecated")

mesEvcGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 1, 1, 10)
)
mesEvcGroupV2.setObjects(
      *(("LUM-MES-MIB", "mesEvcIndex"),
        ("LUM-MES-MIB", "mesEvcName"),
        ("LUM-MES-MIB", "mesEvcDescr"),
        ("LUM-MES-MIB", "mesEvcObjectProperty"),
        ("LUM-MES-MIB", "mesEvcAdminStatus"),
        ("LUM-MES-MIB", "mesEvcOperStatus"),
        ("LUM-MES-MIB", "mesEvcIdentifier"),
        ("LUM-MES-MIB", "mesEvcUniIdentifier"),
        ("LUM-MES-MIB", "mesEvcNniIdentifier"),
        ("LUM-MES-MIB", "mesEvcType"),
        ("LUM-MES-MIB", "mesEvcMtuSize"),
        ("LUM-MES-MIB", "mesEvcFrameDeliveryUnicast"),
        ("LUM-MES-MIB", "mesEvcFrameDeliveryMulticast"),
        ("LUM-MES-MIB", "mesEvcFrameDeliveryBroadcast"),
        ("LUM-MES-MIB", "mesEvcDefineL2Control"),
        ("LUM-MES-MIB", "mesEvcL2ControlProtocolDisposition"),
        ("LUM-MES-MIB", "mesEvcL2DestinationMacAddress"),
        ("LUM-MES-MIB", "mesEvcCeVlanIdPreservation"),
        ("LUM-MES-MIB", "mesEvcCosPreservation"),
        ("LUM-MES-MIB", "mesEvcAssociateBwp"),
        ("LUM-MES-MIB", "mesEvcReleaseBwp"),
        ("LUM-MES-MIB", "mesEvcIngressBwProfilePerEvc"),
        ("LUM-MES-MIB", "mesEvcIngressBwp"),
        ("LUM-MES-MIB", "mesEvcEgressBwProfilePerEvc"),
        ("LUM-MES-MIB", "mesEvcEgressBwp"),
        ("LUM-MES-MIB", "mesEvcCreateCeVlanIdMap"),
        ("LUM-MES-MIB", "mesEvcDefineProviderTag"),
        ("LUM-MES-MIB", "mesEvcProviderTagType"),
        ("LUM-MES-MIB", "mesEvcProviderTagEtherType"),
        ("LUM-MES-MIB", "mesEvcProviderTagVlanId"),
        ("LUM-MES-MIB", "mesEvcDefineClassOfService"),
        ("LUM-MES-MIB", "mesEvcCoSClassification"),
        ("LUM-MES-MIB", "mesEvcCoSPriority"),
        ("LUM-MES-MIB", "mesEvcInternalReference"),
        ("LUM-MES-MIB", "mesEvcRowStatus"),
        ("LUM-MES-MIB", "mesEvcQProfile"),
        ("LUM-MES-MIB", "mesEvcCeVlanIdMap"),
        ("LUM-MES-MIB", "mesEvcDefaultCeVlanPriority"))
)
if mibBuilder.loadTexts:
    mesEvcGroupV2.setStatus("deprecated")

mesQProfileGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 1, 1, 11)
)
mesQProfileGroup.setObjects(
      *(("LUM-MES-MIB", "mesQProfileIndex"),
        ("LUM-MES-MIB", "mesQProfileName"),
        ("LUM-MES-MIB", "mesQProfileObjectProperty"),
        ("LUM-MES-MIB", "mesQProfileType"),
        ("LUM-MES-MIB", "mesQProfileId"),
        ("LUM-MES-MIB", "mesQProfileType"),
        ("LUM-MES-MIB", "mesQProfileWeight"),
        ("LUM-MES-MIB", "mesQProfileGreenLowThreshold"),
        ("LUM-MES-MIB", "mesQProfileGreenHighThreshold"),
        ("LUM-MES-MIB", "mesQProfileGreenDropProbability"),
        ("LUM-MES-MIB", "mesQProfileYellowLowThreshold"),
        ("LUM-MES-MIB", "mesQProfileYellowHighThreshold"),
        ("LUM-MES-MIB", "mesQProfileYellowDropProbability"),
        ("LUM-MES-MIB", "mesQProfileInternalReference"))
)
if mibBuilder.loadTexts:
    mesQProfileGroup.setStatus("current")

mesMepGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 1, 1, 12)
)
mesMepGroup.setObjects(
      *(("LUM-MES-MIB", "mesMepIndex"),
        ("LUM-MES-MIB", "mesMepName"),
        ("LUM-MES-MIB", "mesMepObjectProperty"),
        ("LUM-MES-MIB", "mesMepMeIdentifier"),
        ("LUM-MES-MIB", "mesMepInternalReference"),
        ("LUM-MES-MIB", "mesMepAdminStatus"),
        ("LUM-MES-MIB", "mesMepOperStatus"),
        ("LUM-MES-MIB", "mesMepTransmissionInterval"),
        ("LUM-MES-MIB", "mesMepLossOfContinuity"),
        ("LUM-MES-MIB", "mesMepUnexpectedMegId"),
        ("LUM-MES-MIB", "mesMepUnexpectedTransmissionInterval"),
        ("LUM-MES-MIB", "mesMepRemoteDefectIndication"),
        ("LUM-MES-MIB", "mesMepUnexpectedOpCode"),
        ("LUM-MES-MIB", "mesMepAlarmIndicationSignal"),
        ("LUM-MES-MIB", "mesMepMegIdFormatReceived"),
        ("LUM-MES-MIB", "mesMepMegIdReceived"),
        ("LUM-MES-MIB", "mesMepMegIdIccReceived"),
        ("LUM-MES-MIB", "mesMepId"),
        ("LUM-MES-MIB", "mesMepIdExpected"),
        ("LUM-MES-MIB", "mesMepIdReceived"),
        ("LUM-MES-MIB", "mesMepUnexpectedMepId"),
        ("LUM-MES-MIB", "mesMepUnexpectedMegLevel"),
        ("LUM-MES-MIB", "mesMepMegId"),
        ("LUM-MES-MIB", "mesMepMegIdFormat"),
        ("LUM-MES-MIB", "mesMepMegIdIcc"))
)
if mibBuilder.loadTexts:
    mesMepGroup.setStatus("current")

mesGeneralGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 1, 1, 13)
)
mesGeneralGroupV2.setObjects(
      *(("LUM-MES-MIB", "mesGeneralConfigLastChangeTime"),
        ("LUM-MES-MIB", "mesGeneralStateLastChangeTime"),
        ("LUM-MES-MIB", "mesGeneralUniTableSize"),
        ("LUM-MES-MIB", "mesGeneralNniTableSize"),
        ("LUM-MES-MIB", "mesGeneralEvcTableSize"),
        ("LUM-MES-MIB", "mesGeneralBwpTableSize"),
        ("LUM-MES-MIB", "mesGeneralCeEvcMapTableSize"),
        ("LUM-MES-MIB", "mesGeneralMepTableSize"),
        ("LUM-MES-MIB", "mesGeneralMegTableSize"),
        ("LUM-MES-MIB", "mesGeneralEvcBwpMapTableSize"))
)
if mibBuilder.loadTexts:
    mesGeneralGroupV2.setStatus("deprecated")

mesMegGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 1, 1, 14)
)
mesMegGroup.setObjects(
      *(("LUM-MES-MIB", "mesMegIndex"),
        ("LUM-MES-MIB", "mesMegName"),
        ("LUM-MES-MIB", "mesMegObjectProperty"),
        ("LUM-MES-MIB", "mesMegInternalReference"),
        ("LUM-MES-MIB", "mesMegAdminStatus"),
        ("LUM-MES-MIB", "mesMegOperStatus"),
        ("LUM-MES-MIB", "mesMegLevel"),
        ("LUM-MES-MIB", "mesMegUnexpectedMessage"))
)
if mibBuilder.loadTexts:
    mesMegGroup.setStatus("current")

mesUniGroupV3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 1, 1, 15)
)
mesUniGroupV3.setObjects(
      *(("LUM-MES-MIB", "mesUniIndex"),
        ("LUM-MES-MIB", "mesUniName"),
        ("LUM-MES-MIB", "mesUniDescr"),
        ("LUM-MES-MIB", "mesUniSubrack"),
        ("LUM-MES-MIB", "mesUniSlot"),
        ("LUM-MES-MIB", "mesUniTxPort"),
        ("LUM-MES-MIB", "mesUniRxPort"),
        ("LUM-MES-MIB", "mesUniObjectProperty"),
        ("LUM-MES-MIB", "mesUniAdminStatus"),
        ("LUM-MES-MIB", "mesUniOperStatus"),
        ("LUM-MES-MIB", "mesUniIdentifier"),
        ("LUM-MES-MIB", "mesUniMtuSize"),
        ("LUM-MES-MIB", "mesUniMaxNoOfEvcs"),
        ("LUM-MES-MIB", "mesUniCurrentNoOfEvcs"),
        ("LUM-MES-MIB", "mesUniAvailableCapacity"),
        ("LUM-MES-MIB", "mesUniServiceMultiplexing"),
        ("LUM-MES-MIB", "mesUniBundling"),
        ("LUM-MES-MIB", "mesUniAllToOneBundling"),
        ("LUM-MES-MIB", "mesUniUntaggedCeVlanIdAssignment"),
        ("LUM-MES-MIB", "mesUniAssociateBwp"),
        ("LUM-MES-MIB", "mesUniReleaseBwp"),
        ("LUM-MES-MIB", "mesUniIngressBwProfilePerUni"),
        ("LUM-MES-MIB", "mesUniIngressBwp"),
        ("LUM-MES-MIB", "mesUniEgressBwProfilePerUni"),
        ("LUM-MES-MIB", "mesUniEgressBwp"),
        ("LUM-MES-MIB", "mesUniSetupCommand"),
        ("LUM-MES-MIB", "mesUniCreateEvcCommand"),
        ("LUM-MES-MIB", "mesUniListCeVlanIdsCommand"),
        ("LUM-MES-MIB", "mesUniTaggingOfUntaggedFrames"),
        ("LUM-MES-MIB", "mesUniCeVlanIdAssignmentCommand"),
        ("LUM-MES-MIB", "mesUniL2SpanningTreeProcessing"),
        ("LUM-MES-MIB", "mesUniL2PauseProcessing"),
        ("LUM-MES-MIB", "mesUniL2SlowProtocolsProcessing"),
        ("LUM-MES-MIB", "mesUniL2PortAuthenticationProcessing"),
        ("LUM-MES-MIB", "mesUniL2OtherBridgeBlockProcessing"),
        ("LUM-MES-MIB", "mesUniL2AllLANsBridgeMgmtProcessing"),
        ("LUM-MES-MIB", "mesUniL2GarpProcessing"),
        ("LUM-MES-MIB", "mesUniL2OamUniMeProcessing"),
        ("LUM-MES-MIB", "mesUniTagTransparency"),
        ("LUM-MES-MIB", "mesUniMgmtVlan"),
        ("LUM-MES-MIB", "mesUniDefineMgmtVlan"),
        ("LUM-MES-MIB", "mesUniMgmtVlanTagType"),
        ("LUM-MES-MIB", "mesUniMgmtVlanEtherType"),
        ("LUM-MES-MIB", "mesUniMgmtVlanVlanId"),
        ("LUM-MES-MIB", "mesUniMgmtVlanPriority"),
        ("LUM-MES-MIB", "mesUniMgmtVlanMacAddress"),
        ("LUM-MES-MIB", "mesUniMacInMac"),
        ("LUM-MES-MIB", "mesUniMacInMacIsid"),
        ("LUM-MES-MIB", "mesUniMacInMacDa"),
        ("LUM-MES-MIB", "mesUniDefineMac"))
)
if mibBuilder.loadTexts:
    mesUniGroupV3.setStatus("deprecated")

mesEvcGroupV3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 1, 1, 16)
)
mesEvcGroupV3.setObjects(
      *(("LUM-MES-MIB", "mesEvcIndex"),
        ("LUM-MES-MIB", "mesEvcName"),
        ("LUM-MES-MIB", "mesEvcDescr"),
        ("LUM-MES-MIB", "mesEvcObjectProperty"),
        ("LUM-MES-MIB", "mesEvcAdminStatus"),
        ("LUM-MES-MIB", "mesEvcOperStatus"),
        ("LUM-MES-MIB", "mesEvcIdentifier"),
        ("LUM-MES-MIB", "mesEvcUniIdentifier"),
        ("LUM-MES-MIB", "mesEvcNniIdentifier"),
        ("LUM-MES-MIB", "mesEvcType"),
        ("LUM-MES-MIB", "mesEvcMtuSize"),
        ("LUM-MES-MIB", "mesEvcFrameDeliveryUnicast"),
        ("LUM-MES-MIB", "mesEvcFrameDeliveryMulticast"),
        ("LUM-MES-MIB", "mesEvcFrameDeliveryBroadcast"),
        ("LUM-MES-MIB", "mesEvcDefineL2Control"),
        ("LUM-MES-MIB", "mesEvcL2ControlProtocolDisposition"),
        ("LUM-MES-MIB", "mesEvcL2DestinationMacAddress"),
        ("LUM-MES-MIB", "mesEvcCeVlanIdPreservation"),
        ("LUM-MES-MIB", "mesEvcCosPreservation"),
        ("LUM-MES-MIB", "mesEvcAssociateBwp"),
        ("LUM-MES-MIB", "mesEvcReleaseBwp"),
        ("LUM-MES-MIB", "mesEvcIngressBwProfilePerEvc"),
        ("LUM-MES-MIB", "mesEvcIngressBwp"),
        ("LUM-MES-MIB", "mesEvcEgressBwProfilePerEvc"),
        ("LUM-MES-MIB", "mesEvcEgressBwp"),
        ("LUM-MES-MIB", "mesEvcCreateCeVlanIdMap"),
        ("LUM-MES-MIB", "mesEvcDefineProviderTag"),
        ("LUM-MES-MIB", "mesEvcProviderTagType"),
        ("LUM-MES-MIB", "mesEvcProviderTagEtherType"),
        ("LUM-MES-MIB", "mesEvcProviderTagVlanId"),
        ("LUM-MES-MIB", "mesEvcDefineClassOfService"),
        ("LUM-MES-MIB", "mesEvcCoSPriority"),
        ("LUM-MES-MIB", "mesEvcInternalReference"),
        ("LUM-MES-MIB", "mesEvcRowStatus"),
        ("LUM-MES-MIB", "mesEvcQProfile"),
        ("LUM-MES-MIB", "mesEvcCeVlanIdMap"),
        ("LUM-MES-MIB", "mesEvcDefaultCeVlanPriority"),
        ("LUM-MES-MIB", "mesEvcClientEgressTagVlanIdAssignment"),
        ("LUM-MES-MIB", "mesEvcClientEgressTagVlanId"),
        ("LUM-MES-MIB", "mesEvcTagPriorityAssignment"),
        ("LUM-MES-MIB", "mesEvcClientEgressTagTypeAssignment"),
        ("LUM-MES-MIB", "mesEvcClientEgressTagType"),
        ("LUM-MES-MIB", "mesEvcClientEgressTagEtherType"),
        ("LUM-MES-MIB", "mesEvcMacInMac"),
        ("LUM-MES-MIB", "mesEvcMacInMacLtoC"),
        ("LUM-MES-MIB", "mesEvcCopyIsid"),
        ("LUM-MES-MIB", "mesEvcMacInMacIsid"),
        ("LUM-MES-MIB", "mesEvcMacInMacIsidLtoC"),
        ("LUM-MES-MIB", "mesEvcMacInMacDa"),
        ("LUM-MES-MIB", "mesEvcMacInMacDaLtoC"),
        ("LUM-MES-MIB", "mesEvcDefineMac"),
        ("LUM-MES-MIB", "mesEvcIngressBwProfileModel"),
        ("LUM-MES-MIB", "mesEvcIngressBwProfileMap"))
)
if mibBuilder.loadTexts:
    mesEvcGroupV3.setStatus("current")

mesNniGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 1, 1, 17)
)
mesNniGroupV2.setObjects(
      *(("LUM-MES-MIB", "mesNniIndex"),
        ("LUM-MES-MIB", "mesNniName"),
        ("LUM-MES-MIB", "mesNniDescr"),
        ("LUM-MES-MIB", "mesNniSubrack"),
        ("LUM-MES-MIB", "mesNniSlot"),
        ("LUM-MES-MIB", "mesNniTxPort"),
        ("LUM-MES-MIB", "mesNniRxPort"),
        ("LUM-MES-MIB", "mesNniObjectProperty"),
        ("LUM-MES-MIB", "mesNniAdminStatus"),
        ("LUM-MES-MIB", "mesNniOperStatus"),
        ("LUM-MES-MIB", "mesNniIdentifier"),
        ("LUM-MES-MIB", "mesNniCurrentNoOfEvcs"),
        ("LUM-MES-MIB", "mesNniAvailableCapacity"),
        ("LUM-MES-MIB", "mesNniDefineMgmtVlan"),
        ("LUM-MES-MIB", "mesNniMgmtVlanTagType"),
        ("LUM-MES-MIB", "mesNniMgmtVlanEtherType"),
        ("LUM-MES-MIB", "mesNniMgmtVlanVlanId"),
        ("LUM-MES-MIB", "mesNniMgmtVlanPriority"),
        ("LUM-MES-MIB", "mesNniMgmtVlanIpAddress"),
        ("LUM-MES-MIB", "mesNniMgmtVlanNetMask"),
        ("LUM-MES-MIB", "mesNniMgmtVlanMacAddress"),
        ("LUM-MES-MIB", "mesNniSetupCommand"),
        ("LUM-MES-MIB", "mesNniMgmtVlan"),
        ("LUM-MES-MIB", "mesNniMacInMac"),
        ("LUM-MES-MIB", "mesNniMacInMacIsid"),
        ("LUM-MES-MIB", "mesNniMacInMacDa"),
        ("LUM-MES-MIB", "mesNniDefineMac"))
)
if mibBuilder.loadTexts:
    mesNniGroupV2.setStatus("deprecated")

mesMiscGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 1, 1, 18)
)
mesMiscGroup.setObjects(
      *(("LUM-MES-MIB", "mesMiscIndex"),
        ("LUM-MES-MIB", "mesMiscName"),
        ("LUM-MES-MIB", "mesMiscObjectProperty"),
        ("LUM-MES-MIB", "mesMiscAdminStatus"),
        ("LUM-MES-MIB", "mesMiscOperStatus"),
        ("LUM-MES-MIB", "mesMiscMgmtVlanIpAddress"),
        ("LUM-MES-MIB", "mesMiscMgmtVlanNetMask"),
        ("LUM-MES-MIB", "mesMiscMgmtVlanMacAddress0"),
        ("LUM-MES-MIB", "mesMiscMgmtVlanMacAddress1"),
        ("LUM-MES-MIB", "mesMiscMgmtVlanMacAddress2"))
)
if mibBuilder.loadTexts:
    mesMiscGroup.setStatus("deprecated")

mesEvcBwpMapGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 1, 1, 19)
)
mesEvcBwpMapGroup.setObjects(
      *(("LUM-MES-MIB", "mesEvcBwpMapIndex"),
        ("LUM-MES-MIB", "mesEvcBwpMapName"),
        ("LUM-MES-MIB", "mesEvcBwpMapObjectProperty"),
        ("LUM-MES-MIB", "mesEvcBwpMapEvcId"),
        ("LUM-MES-MIB", "mesEvcBwpMapModel"),
        ("LUM-MES-MIB", "mesEvcBwpMapPriority"),
        ("LUM-MES-MIB", "mesEvcBwpMapBwpId"),
        ("LUM-MES-MIB", "mesEvcBwpMapInternalReference"),
        ("LUM-MES-MIB", "mesEvcBwpMapRowStatus"))
)
if mibBuilder.loadTexts:
    mesEvcBwpMapGroup.setStatus("current")

mesGeneralGroupV3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 1, 1, 20)
)
mesGeneralGroupV3.setObjects(
      *(("LUM-MES-MIB", "mesGeneralConfigLastChangeTime"),
        ("LUM-MES-MIB", "mesGeneralStateLastChangeTime"),
        ("LUM-MES-MIB", "mesGeneralUniTableSize"),
        ("LUM-MES-MIB", "mesGeneralNniTableSize"),
        ("LUM-MES-MIB", "mesGeneralEvcTableSize"),
        ("LUM-MES-MIB", "mesGeneralBwpTableSize"),
        ("LUM-MES-MIB", "mesGeneralCeEvcMapTableSize"),
        ("LUM-MES-MIB", "mesGeneralMepTableSize"),
        ("LUM-MES-MIB", "mesGeneralMegTableSize"),
        ("LUM-MES-MIB", "mesGeneralEvcBwpMapTableSize"),
        ("LUM-MES-MIB", "mesGeneralPortTableSize"),
        ("LUM-MES-MIB", "mesGeneralVlanMapTableSize"))
)
if mibBuilder.loadTexts:
    mesGeneralGroupV3.setStatus("deprecated")

mesPortGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 1, 1, 21)
)
mesPortGroup.setObjects(
      *(("LUM-MES-MIB", "mesPortIndex"),
        ("LUM-MES-MIB", "mesPortName"),
        ("LUM-MES-MIB", "mesPortDescr"),
        ("LUM-MES-MIB", "mesPortSubrack"),
        ("LUM-MES-MIB", "mesPortSlot"),
        ("LUM-MES-MIB", "mesPortTxPort"),
        ("LUM-MES-MIB", "mesPortRxPort"),
        ("LUM-MES-MIB", "mesPortAdminStatus"),
        ("LUM-MES-MIB", "mesPortOperStatus"),
        ("LUM-MES-MIB", "mesPortMtuSize"),
        ("LUM-MES-MIB", "mesPortTagType"),
        ("LUM-MES-MIB", "mesPortNoOfVlans"),
        ("LUM-MES-MIB", "mesPortVlanAware"),
        ("LUM-MES-MIB", "mesPortVlanTagged"),
        ("LUM-MES-MIB", "mesPortVlanUntagged"),
        ("LUM-MES-MIB", "mesPortIngressFiltering"),
        ("LUM-MES-MIB", "mesPortEgressTag"),
        ("LUM-MES-MIB", "mesPortDefaultCeVlanId"),
        ("LUM-MES-MIB", "mesPortAssociateVlan"),
        ("LUM-MES-MIB", "mesPortReleaseVlan"),
        ("LUM-MES-MIB", "mesPortActingAsLine"),
        ("LUM-MES-MIB", "mesPortTrustedPortmask"),
        ("LUM-MES-MIB", "mesPortMacAddress"),
        ("LUM-MES-MIB", "mesPortLagStatus"),
        ("LUM-MES-MIB", "mesPortLagPortmask"),
        ("LUM-MES-MIB", "mesPortAssociateLag"),
        ("LUM-MES-MIB", "mesPortTxEthUtilization"),
        ("LUM-MES-MIB", "mesPortRxEthUtilization"),
        ("LUM-MES-MIB", "mesPortFlowControlMode"),
        ("LUM-MES-MIB", "mesPortAutoNegotiationMode"),
        ("LUM-MES-MIB", "mesPortAutoNegotiationStatus"),
        ("LUM-MES-MIB", "mesPortLinkDown"),
        ("LUM-MES-MIB", "mesPortLinkFaultRemote"),
        ("LUM-MES-MIB", "mesPortLinkFaultLocal"))
)
if mibBuilder.loadTexts:
    mesPortGroup.setStatus("deprecated")

mesVlanMapGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 1, 1, 22)
)
mesVlanMapGroup.setObjects(
      *(("LUM-MES-MIB", "mesVlanMapIndex"),
        ("LUM-MES-MIB", "mesVlanMapName"),
        ("LUM-MES-MIB", "mesVlanMapVlanIdRangeLower"),
        ("LUM-MES-MIB", "mesVlanMapVlanIdRangeUpper"),
        ("LUM-MES-MIB", "mesVlanMapInternalReference"),
        ("LUM-MES-MIB", "mesVlanMapPortmask"))
)
if mibBuilder.loadTexts:
    mesVlanMapGroup.setStatus("deprecated")

mesMgmtVlanGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 1, 1, 23)
)
mesMgmtVlanGroup.setObjects(
      *(("LUM-MES-MIB", "mesMgmtVlanIndex"),
        ("LUM-MES-MIB", "mesMgmtVlanName"),
        ("LUM-MES-MIB", "mesMgmtVlanDescr"),
        ("LUM-MES-MIB", "mesMgmtVlanSubrack"),
        ("LUM-MES-MIB", "mesMgmtVlanSlot"),
        ("LUM-MES-MIB", "mesMgmtVlanTxPort"),
        ("LUM-MES-MIB", "mesMgmtVlanRxPort"),
        ("LUM-MES-MIB", "mesMgmtVlanObjectProperty"),
        ("LUM-MES-MIB", "mesMgmtVlanAdminStatus"),
        ("LUM-MES-MIB", "mesMgmtVlanConfigure"),
        ("LUM-MES-MIB", "mesMgmtVlanTagType"),
        ("LUM-MES-MIB", "mesMgmtVlanEtherType"),
        ("LUM-MES-MIB", "mesMgmtVlanVlanId"),
        ("LUM-MES-MIB", "mesMgmtVlanPriority"),
        ("LUM-MES-MIB", "mesMgmtVlanMacInMac"),
        ("LUM-MES-MIB", "mesMgmtVlanMacInMacIsid"),
        ("LUM-MES-MIB", "mesMgmtVlanMacInMacDa"))
)
if mibBuilder.loadTexts:
    mesMgmtVlanGroup.setStatus("deprecated")

mesMiscGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 1, 1, 24)
)
mesMiscGroupV2.setObjects(
      *(("LUM-MES-MIB", "mesMiscIndex"),
        ("LUM-MES-MIB", "mesMiscName"),
        ("LUM-MES-MIB", "mesMiscObjectProperty"),
        ("LUM-MES-MIB", "mesMiscAdminStatus"),
        ("LUM-MES-MIB", "mesMiscOperStatus"),
        ("LUM-MES-MIB", "mesMiscMgmtVlanIpAddress"),
        ("LUM-MES-MIB", "mesMiscMgmtVlanNetMask"),
        ("LUM-MES-MIB", "mesMiscMgmtVlanMacAddress0"),
        ("LUM-MES-MIB", "mesMiscMgmtVlanMacAddress1"),
        ("LUM-MES-MIB", "mesMiscMgmtVlanMacAddress2"),
        ("LUM-MES-MIB", "mesMiscConfigureAddress"))
)
if mibBuilder.loadTexts:
    mesMiscGroupV2.setStatus("deprecated")

mesLagGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 1, 1, 25)
)
mesLagGroup.setObjects(
      *(("LUM-MES-MIB", "mesLagIndex"),
        ("LUM-MES-MIB", "mesLagName"),
        ("LUM-MES-MIB", "mesLagInternalReference"),
        ("LUM-MES-MIB", "mesLagPortmask"),
        ("LUM-MES-MIB", "mesLagMasterIndex"),
        ("LUM-MES-MIB", "mesLagConfigure"))
)
if mibBuilder.loadTexts:
    mesLagGroup.setStatus("deprecated")

mesNniGroupV3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 1, 1, 26)
)
mesNniGroupV3.setObjects(
      *(("LUM-MES-MIB", "mesNniIndex"),
        ("LUM-MES-MIB", "mesNniName"),
        ("LUM-MES-MIB", "mesNniDescr"),
        ("LUM-MES-MIB", "mesNniSubrack"),
        ("LUM-MES-MIB", "mesNniSlot"),
        ("LUM-MES-MIB", "mesNniTxPort"),
        ("LUM-MES-MIB", "mesNniRxPort"),
        ("LUM-MES-MIB", "mesNniObjectProperty"),
        ("LUM-MES-MIB", "mesNniAdminStatus"),
        ("LUM-MES-MIB", "mesNniOperStatus"),
        ("LUM-MES-MIB", "mesNniIdentifier"),
        ("LUM-MES-MIB", "mesNniCurrentNoOfEvcs"),
        ("LUM-MES-MIB", "mesNniAvailableCapacity"),
        ("LUM-MES-MIB", "mesNniDefineMgmtVlan"),
        ("LUM-MES-MIB", "mesNniMgmtVlanTagType"),
        ("LUM-MES-MIB", "mesNniMgmtVlanEtherType"),
        ("LUM-MES-MIB", "mesNniMgmtVlanVlanId"),
        ("LUM-MES-MIB", "mesNniMgmtVlanPriority"),
        ("LUM-MES-MIB", "mesNniMgmtVlanIpAddress"),
        ("LUM-MES-MIB", "mesNniMgmtVlanNetMask"),
        ("LUM-MES-MIB", "mesNniMgmtVlanMacAddress"),
        ("LUM-MES-MIB", "mesNniSetupCommand"),
        ("LUM-MES-MIB", "mesNniMgmtVlan"),
        ("LUM-MES-MIB", "mesNniMacInMac"),
        ("LUM-MES-MIB", "mesNniMacInMacIsid"),
        ("LUM-MES-MIB", "mesNniMacInMacDa"),
        ("LUM-MES-MIB", "mesNniDefineMac"),
        ("LUM-MES-MIB", "mesNniLagStatus"))
)
if mibBuilder.loadTexts:
    mesNniGroupV3.setStatus("current")

mesPortGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 1, 1, 27)
)
mesPortGroupV2.setObjects(
      *(("LUM-MES-MIB", "mesPortIndex"),
        ("LUM-MES-MIB", "mesPortName"),
        ("LUM-MES-MIB", "mesPortDescr"),
        ("LUM-MES-MIB", "mesPortSubrack"),
        ("LUM-MES-MIB", "mesPortSlot"),
        ("LUM-MES-MIB", "mesPortTxPort"),
        ("LUM-MES-MIB", "mesPortRxPort"),
        ("LUM-MES-MIB", "mesPortAdminStatus"),
        ("LUM-MES-MIB", "mesPortOperStatus"),
        ("LUM-MES-MIB", "mesPortMtuSize"),
        ("LUM-MES-MIB", "mesPortTagType"),
        ("LUM-MES-MIB", "mesPortNoOfVlans"),
        ("LUM-MES-MIB", "mesPortVlanAware"),
        ("LUM-MES-MIB", "mesPortVlanTagged"),
        ("LUM-MES-MIB", "mesPortVlanUntagged"),
        ("LUM-MES-MIB", "mesPortIngressFiltering"),
        ("LUM-MES-MIB", "mesPortEgressTag"),
        ("LUM-MES-MIB", "mesPortDefaultCeVlanId"),
        ("LUM-MES-MIB", "mesPortAssociateVlan"),
        ("LUM-MES-MIB", "mesPortReleaseVlan"),
        ("LUM-MES-MIB", "mesPortActingAsLine"),
        ("LUM-MES-MIB", "mesPortTrustedPortmask"),
        ("LUM-MES-MIB", "mesPortMacAddress"),
        ("LUM-MES-MIB", "mesPortLagStatus"),
        ("LUM-MES-MIB", "mesPortLagPortmask"),
        ("LUM-MES-MIB", "mesPortAssociateLag"),
        ("LUM-MES-MIB", "mesPortTxEthUtilization"),
        ("LUM-MES-MIB", "mesPortRxEthUtilization"),
        ("LUM-MES-MIB", "mesPortFlowControlMode"),
        ("LUM-MES-MIB", "mesPortAutoNegotiationMode"),
        ("LUM-MES-MIB", "mesPortAutoNegotiationStatus"),
        ("LUM-MES-MIB", "mesPortLinkDown"),
        ("LUM-MES-MIB", "mesPortLinkFaultRemote"),
        ("LUM-MES-MIB", "mesPortLinkFaultLocal"),
        ("LUM-MES-MIB", "mesPortNoOfShapers"),
        ("LUM-MES-MIB", "mesPortNoOfPolicers"),
        ("LUM-MES-MIB", "mesPortAssociateShaper"),
        ("LUM-MES-MIB", "mesPortReleaseShaper"),
        ("LUM-MES-MIB", "mesPortAssociatePolicer"),
        ("LUM-MES-MIB", "mesPortReleasePolicer"),
        ("LUM-MES-MIB", "mesPortRestartAutoNegotiation"),
        ("LUM-MES-MIB", "mesPortConfigureLine"))
)
if mibBuilder.loadTexts:
    mesPortGroupV2.setStatus("deprecated")

mesPolicingGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 1, 1, 28)
)
mesPolicingGroup.setObjects(
      *(("LUM-MES-MIB", "mesPolicingIndex"),
        ("LUM-MES-MIB", "mesPolicingName"),
        ("LUM-MES-MIB", "mesPolicingRate"),
        ("LUM-MES-MIB", "mesPolicingBurstSize"),
        ("LUM-MES-MIB", "mesPolicingType"),
        ("LUM-MES-MIB", "mesPolicingInternalReference"),
        ("LUM-MES-MIB", "mesPolicingIdentifier"))
)
if mibBuilder.loadTexts:
    mesPolicingGroup.setStatus("deprecated")

mesShapingGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 1, 1, 29)
)
mesShapingGroup.setObjects(
      *(("LUM-MES-MIB", "mesShapingIndex"),
        ("LUM-MES-MIB", "mesShapingName"),
        ("LUM-MES-MIB", "mesShapingRate"),
        ("LUM-MES-MIB", "mesShapingBurstSize"),
        ("LUM-MES-MIB", "mesShapingQueue"),
        ("LUM-MES-MIB", "mesShapingInternalReference"),
        ("LUM-MES-MIB", "mesShapingExcess"),
        ("LUM-MES-MIB", "mesShapingIdentifier"))
)
if mibBuilder.loadTexts:
    mesShapingGroup.setStatus("deprecated")

mesCosGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 1, 1, 30)
)
mesCosGroup.setObjects(
      *(("LUM-MES-MIB", "mesCosIndex"),
        ("LUM-MES-MIB", "mesCosName"),
        ("LUM-MES-MIB", "mesCosTxPort"),
        ("LUM-MES-MIB", "mesCosMap"),
        ("LUM-MES-MIB", "mesCosPriority0"),
        ("LUM-MES-MIB", "mesCosPriority1"),
        ("LUM-MES-MIB", "mesCosPriority2"),
        ("LUM-MES-MIB", "mesCosPriority3"),
        ("LUM-MES-MIB", "mesCosPriority4"),
        ("LUM-MES-MIB", "mesCosPriority5"),
        ("LUM-MES-MIB", "mesCosPriority6"),
        ("LUM-MES-MIB", "mesCosPriority7"))
)
if mibBuilder.loadTexts:
    mesCosGroup.setStatus("current")

mesBwpMapGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 1, 1, 31)
)
mesBwpMapGroup.setObjects(
      *(("LUM-MES-MIB", "mesBwpMapIndex"),
        ("LUM-MES-MIB", "mesBwpMapName"),
        ("LUM-MES-MIB", "mesBwpMapPortName"),
        ("LUM-MES-MIB", "mesBwpMapBwpName"),
        ("LUM-MES-MIB", "mesBwpMapInternalReference"))
)
if mibBuilder.loadTexts:
    mesBwpMapGroup.setStatus("deprecated")

mesUniGroupV4 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 1, 1, 32)
)
mesUniGroupV4.setObjects(
      *(("LUM-MES-MIB", "mesUniIndex"),
        ("LUM-MES-MIB", "mesUniName"),
        ("LUM-MES-MIB", "mesUniDescr"),
        ("LUM-MES-MIB", "mesUniSubrack"),
        ("LUM-MES-MIB", "mesUniSlot"),
        ("LUM-MES-MIB", "mesUniTxPort"),
        ("LUM-MES-MIB", "mesUniRxPort"),
        ("LUM-MES-MIB", "mesUniObjectProperty"),
        ("LUM-MES-MIB", "mesUniAdminStatus"),
        ("LUM-MES-MIB", "mesUniOperStatus"),
        ("LUM-MES-MIB", "mesUniIdentifier"),
        ("LUM-MES-MIB", "mesUniMtuSize"),
        ("LUM-MES-MIB", "mesUniMaxNoOfEvcs"),
        ("LUM-MES-MIB", "mesUniCurrentNoOfEvcs"),
        ("LUM-MES-MIB", "mesUniAvailableCapacity"),
        ("LUM-MES-MIB", "mesUniServiceMultiplexing"),
        ("LUM-MES-MIB", "mesUniBundling"),
        ("LUM-MES-MIB", "mesUniAllToOneBundling"),
        ("LUM-MES-MIB", "mesUniUntaggedCeVlanIdAssignment"),
        ("LUM-MES-MIB", "mesUniAssociateBwp"),
        ("LUM-MES-MIB", "mesUniReleaseBwp"),
        ("LUM-MES-MIB", "mesUniIngressBwProfilePerUni"),
        ("LUM-MES-MIB", "mesUniIngressBwp"),
        ("LUM-MES-MIB", "mesUniEgressBwProfilePerUni"),
        ("LUM-MES-MIB", "mesUniEgressBwp"),
        ("LUM-MES-MIB", "mesUniSetupCommand"),
        ("LUM-MES-MIB", "mesUniCreateEvcCommand"),
        ("LUM-MES-MIB", "mesUniListCeVlanIdsCommand"),
        ("LUM-MES-MIB", "mesUniTaggingOfUntaggedFrames"),
        ("LUM-MES-MIB", "mesUniCeVlanIdAssignmentCommand"),
        ("LUM-MES-MIB", "mesUniL2SpanningTreeProcessing"),
        ("LUM-MES-MIB", "mesUniL2PauseProcessing"),
        ("LUM-MES-MIB", "mesUniL2SlowProtocolsProcessing"),
        ("LUM-MES-MIB", "mesUniL2PortAuthenticationProcessing"),
        ("LUM-MES-MIB", "mesUniL2OtherBridgeBlockProcessing"),
        ("LUM-MES-MIB", "mesUniL2AllLANsBridgeMgmtProcessing"),
        ("LUM-MES-MIB", "mesUniL2GarpProcessing"),
        ("LUM-MES-MIB", "mesUniL2OamUniMeProcessing"),
        ("LUM-MES-MIB", "mesUniTagTransparency"),
        ("LUM-MES-MIB", "mesUniMgmtVlan"),
        ("LUM-MES-MIB", "mesUniDefineMgmtVlan"),
        ("LUM-MES-MIB", "mesUniMgmtVlanTagType"),
        ("LUM-MES-MIB", "mesUniMgmtVlanEtherType"),
        ("LUM-MES-MIB", "mesUniMgmtVlanVlanId"),
        ("LUM-MES-MIB", "mesUniMgmtVlanPriority"),
        ("LUM-MES-MIB", "mesUniMgmtVlanMacAddress"),
        ("LUM-MES-MIB", "mesUniMacInMac"),
        ("LUM-MES-MIB", "mesUniMacInMacIsid"),
        ("LUM-MES-MIB", "mesUniMacInMacDa"),
        ("LUM-MES-MIB", "mesUniDefineMac"),
        ("LUM-MES-MIB", "mesUniLagStatus"),
        ("LUM-MES-MIB", "mesUniLagPortmask"),
        ("LUM-MES-MIB", "mesUniAssociateLag"))
)
if mibBuilder.loadTexts:
    mesUniGroupV4.setStatus("current")

mesGeneralGroupV4 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 1, 1, 33)
)
mesGeneralGroupV4.setObjects(
      *(("LUM-MES-MIB", "mesGeneralConfigLastChangeTime"),
        ("LUM-MES-MIB", "mesGeneralStateLastChangeTime"),
        ("LUM-MES-MIB", "mesGeneralUniTableSize"),
        ("LUM-MES-MIB", "mesGeneralNniTableSize"),
        ("LUM-MES-MIB", "mesGeneralEvcTableSize"),
        ("LUM-MES-MIB", "mesGeneralBwpTableSize"),
        ("LUM-MES-MIB", "mesGeneralCeEvcMapTableSize"),
        ("LUM-MES-MIB", "mesGeneralMepTableSize"),
        ("LUM-MES-MIB", "mesGeneralMegTableSize"),
        ("LUM-MES-MIB", "mesGeneralEvcBwpMapTableSize"),
        ("LUM-MES-MIB", "mesGeneralPortTableSize"),
        ("LUM-MES-MIB", "mesGeneralVlanMapTableSize"),
        ("LUM-MES-MIB", "mesGeneralMgmtVlanTableSize"),
        ("LUM-MES-MIB", "mesGeneralLagTableSize"),
        ("LUM-MES-MIB", "mesGeneralPolicingTableSize"),
        ("LUM-MES-MIB", "mesGeneralShapingTableSize"),
        ("LUM-MES-MIB", "mesGeneralBwpMapTableSize"),
        ("LUM-MES-MIB", "mesGeneralCosTableSize"))
)
if mibBuilder.loadTexts:
    mesGeneralGroupV4.setStatus("deprecated")

mesPortGroupV3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 1, 1, 34)
)
mesPortGroupV3.setObjects(
      *(("LUM-MES-MIB", "mesPortIndex"),
        ("LUM-MES-MIB", "mesPortName"),
        ("LUM-MES-MIB", "mesPortDescr"),
        ("LUM-MES-MIB", "mesPortSubrack"),
        ("LUM-MES-MIB", "mesPortSlot"),
        ("LUM-MES-MIB", "mesPortTxPort"),
        ("LUM-MES-MIB", "mesPortRxPort"),
        ("LUM-MES-MIB", "mesPortAdminStatus"),
        ("LUM-MES-MIB", "mesPortOperStatus"),
        ("LUM-MES-MIB", "mesPortMtuSize"),
        ("LUM-MES-MIB", "mesPortTagType"),
        ("LUM-MES-MIB", "mesPortNoOfVlans"),
        ("LUM-MES-MIB", "mesPortVlanAware"),
        ("LUM-MES-MIB", "mesPortVlanTagged"),
        ("LUM-MES-MIB", "mesPortVlanUntagged"),
        ("LUM-MES-MIB", "mesPortIngressFiltering"),
        ("LUM-MES-MIB", "mesPortEgressTag"),
        ("LUM-MES-MIB", "mesPortDefaultCeVlanId"),
        ("LUM-MES-MIB", "mesPortAssociateVlan"),
        ("LUM-MES-MIB", "mesPortReleaseVlan"),
        ("LUM-MES-MIB", "mesPortActingAsLine"),
        ("LUM-MES-MIB", "mesPortTrustedPortmask"),
        ("LUM-MES-MIB", "mesPortMacAddress"),
        ("LUM-MES-MIB", "mesPortLagStatus"),
        ("LUM-MES-MIB", "mesPortLagPortmask"),
        ("LUM-MES-MIB", "mesPortAssociateLag"),
        ("LUM-MES-MIB", "mesPortTxEthUtilization"),
        ("LUM-MES-MIB", "mesPortRxEthUtilization"),
        ("LUM-MES-MIB", "mesPortFlowControlMode"),
        ("LUM-MES-MIB", "mesPortAutoNegotiationMode"),
        ("LUM-MES-MIB", "mesPortAutoNegotiationStatus"),
        ("LUM-MES-MIB", "mesPortLinkDown"),
        ("LUM-MES-MIB", "mesPortLinkFaultRemote"),
        ("LUM-MES-MIB", "mesPortLinkFaultLocal"),
        ("LUM-MES-MIB", "mesPortNoOfShapers"),
        ("LUM-MES-MIB", "mesPortNoOfPolicers"),
        ("LUM-MES-MIB", "mesPortAssociateShaper"),
        ("LUM-MES-MIB", "mesPortReleaseShaper"),
        ("LUM-MES-MIB", "mesPortAssociatePolicer"),
        ("LUM-MES-MIB", "mesPortReleasePolicer"),
        ("LUM-MES-MIB", "mesPortRestartAutoNegotiation"),
        ("LUM-MES-MIB", "mesPortConfigureLine"),
        ("LUM-MES-MIB", "mesPortEtherType"),
        ("LUM-MES-MIB", "mesPortConfigureEtherType"),
        ("LUM-MES-MIB", "mesPortNoOfMirrorSources"),
        ("LUM-MES-MIB", "mesPortMirroring"),
        ("LUM-MES-MIB", "mesPortIngressPushTag"),
        ("LUM-MES-MIB", "mesPortEgressPopTag"),
        ("LUM-MES-MIB", "mesPortDefaultCeVlanPriority"),
        ("LUM-MES-MIB", "mesPortConfigureTagRule"))
)
if mibBuilder.loadTexts:
    mesPortGroupV3.setStatus("deprecated")

mesMirroringGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 1, 1, 36)
)
mesMirroringGroup.setObjects(
      *(("LUM-MES-MIB", "mesMirroringIndex"),
        ("LUM-MES-MIB", "mesMirroringName"),
        ("LUM-MES-MIB", "mesMirroringDestination"),
        ("LUM-MES-MIB", "mesMirroringDirection"),
        ("LUM-MES-MIB", "mesMirroringConfigureDestination"))
)
if mibBuilder.loadTexts:
    mesMirroringGroup.setStatus("deprecated")

mesMiscGroupV3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 1, 1, 37)
)
mesMiscGroupV3.setObjects(
      *(("LUM-MES-MIB", "mesMiscIndex"),
        ("LUM-MES-MIB", "mesMiscName"),
        ("LUM-MES-MIB", "mesMiscObjectProperty"),
        ("LUM-MES-MIB", "mesMiscAdminStatus"),
        ("LUM-MES-MIB", "mesMiscOperStatus"),
        ("LUM-MES-MIB", "mesMiscMgmtVlanIpAddress"),
        ("LUM-MES-MIB", "mesMiscMgmtVlanNetMask"),
        ("LUM-MES-MIB", "mesMiscMgmtVlanMacAddress0"),
        ("LUM-MES-MIB", "mesMiscMgmtVlanMacAddress1"),
        ("LUM-MES-MIB", "mesMiscMgmtVlanMacAddress2"),
        ("LUM-MES-MIB", "mesMiscConfigureAddress"),
        ("LUM-MES-MIB", "mesMiscMgmtVlanNode"),
        ("LUM-MES-MIB", "mesMiscMacAgeing"),
        ("LUM-MES-MIB", "mesMiscMacGetTable"))
)
if mibBuilder.loadTexts:
    mesMiscGroupV3.setStatus("deprecated")

mesVlanTagRuleGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 1, 1, 38)
)
mesVlanTagRuleGroup.setObjects(
      *(("LUM-MES-MIB", "mesVlanTagRuleIndex"),
        ("LUM-MES-MIB", "mesVlanTagRuleName"),
        ("LUM-MES-MIB", "mesVlanTagRuleInternalReference"),
        ("LUM-MES-MIB", "mesVlanTagRuleClassificationName"),
        ("LUM-MES-MIB", "mesVlanTagRuleType"),
        ("LUM-MES-MIB", "mesVlanTagRuleOperation"),
        ("LUM-MES-MIB", "mesVlanTagRuleInnerPrio"),
        ("LUM-MES-MIB", "mesVlanTagRuleInnerVlanId"),
        ("LUM-MES-MIB", "mesVlanTagRuleOuterPrio"),
        ("LUM-MES-MIB", "mesVlanTagRuleOuterVlanId"))
)
if mibBuilder.loadTexts:
    mesVlanTagRuleGroup.setStatus("deprecated")

mesVlanTagClassVlanGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 1, 1, 39)
)
mesVlanTagClassVlanGroup.setObjects(
      *(("LUM-MES-MIB", "mesVlanTagClassVlanIndex"),
        ("LUM-MES-MIB", "mesVlanTagClassVlanName"),
        ("LUM-MES-MIB", "mesVlanTagClassVlanInternalReference"),
        ("LUM-MES-MIB", "mesVlanTagClassVlanTxPort"),
        ("LUM-MES-MIB", "mesVlanTagClassVlanOuterVlanId"))
)
if mibBuilder.loadTexts:
    mesVlanTagClassVlanGroup.setStatus("deprecated")

mesVlanMapGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 1, 1, 40)
)
mesVlanMapGroupV2.setObjects(
      *(("LUM-MES-MIB", "mesVlanMapIndex"),
        ("LUM-MES-MIB", "mesVlanMapName"),
        ("LUM-MES-MIB", "mesVlanMapVlanIdRangeLower"),
        ("LUM-MES-MIB", "mesVlanMapVlanIdRangeUpper"),
        ("LUM-MES-MIB", "mesVlanMapInternalReference"),
        ("LUM-MES-MIB", "mesVlanMapPortmask"),
        ("LUM-MES-MIB", "mesVlanMapConfigurePortMask"),
        ("LUM-MES-MIB", "mesVlanMapLearning"))
)
if mibBuilder.loadTexts:
    mesVlanMapGroupV2.setStatus("deprecated")

mesCosProfileGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 1, 1, 41)
)
mesCosProfileGroup.setObjects(
      *(("LUM-MES-MIB", "mesCosProfileIndex"),
        ("LUM-MES-MIB", "mesCosProfileName"),
        ("LUM-MES-MIB", "mesCosProfilePortmask"),
        ("LUM-MES-MIB", "mesCosProfileScheduler"),
        ("LUM-MES-MIB", "mesCosProfileWeight0"),
        ("LUM-MES-MIB", "mesCosProfileWeight1"),
        ("LUM-MES-MIB", "mesCosProfileWeight2"),
        ("LUM-MES-MIB", "mesCosProfileWeight3"),
        ("LUM-MES-MIB", "mesCosProfileWeight4"),
        ("LUM-MES-MIB", "mesCosProfileWeight5"),
        ("LUM-MES-MIB", "mesCosProfileWeight6"),
        ("LUM-MES-MIB", "mesCosProfileWeight7"),
        ("LUM-MES-MIB", "mesCosProfilePriority0"),
        ("LUM-MES-MIB", "mesCosProfilePriority1"),
        ("LUM-MES-MIB", "mesCosProfilePriority2"),
        ("LUM-MES-MIB", "mesCosProfilePriority3"),
        ("LUM-MES-MIB", "mesCosProfilePriority4"),
        ("LUM-MES-MIB", "mesCosProfilePriority5"),
        ("LUM-MES-MIB", "mesCosProfilePriority6"),
        ("LUM-MES-MIB", "mesCosProfilePriority7"),
        ("LUM-MES-MIB", "mesCosProfileConfigureScheduler"))
)
if mibBuilder.loadTexts:
    mesCosProfileGroup.setStatus("deprecated")

mesLagGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 1, 1, 42)
)
mesLagGroupV2.setObjects(
      *(("LUM-MES-MIB", "mesLagIndex"),
        ("LUM-MES-MIB", "mesLagName"),
        ("LUM-MES-MIB", "mesLagInternalReference"),
        ("LUM-MES-MIB", "mesLagPortmask"),
        ("LUM-MES-MIB", "mesLagMasterIndex"),
        ("LUM-MES-MIB", "mesLagConfigure"),
        ("LUM-MES-MIB", "mesLagHash"))
)
if mibBuilder.loadTexts:
    mesLagGroupV2.setStatus("deprecated")

mesPortGroupV4 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 1, 1, 43)
)
mesPortGroupV4.setObjects(
      *(("LUM-MES-MIB", "mesPortIndex"),
        ("LUM-MES-MIB", "mesPortName"),
        ("LUM-MES-MIB", "mesPortDescr"),
        ("LUM-MES-MIB", "mesPortSubrack"),
        ("LUM-MES-MIB", "mesPortSlot"),
        ("LUM-MES-MIB", "mesPortTxPort"),
        ("LUM-MES-MIB", "mesPortRxPort"),
        ("LUM-MES-MIB", "mesPortAdminStatus"),
        ("LUM-MES-MIB", "mesPortOperStatus"),
        ("LUM-MES-MIB", "mesPortMtuSize"),
        ("LUM-MES-MIB", "mesPortTagType"),
        ("LUM-MES-MIB", "mesPortNoOfVlans"),
        ("LUM-MES-MIB", "mesPortVlanAware"),
        ("LUM-MES-MIB", "mesPortVlanTagged"),
        ("LUM-MES-MIB", "mesPortVlanUntagged"),
        ("LUM-MES-MIB", "mesPortIngressFiltering"),
        ("LUM-MES-MIB", "mesPortEgressTag"),
        ("LUM-MES-MIB", "mesPortDefaultCeVlanId"),
        ("LUM-MES-MIB", "mesPortAssociateVlan"),
        ("LUM-MES-MIB", "mesPortReleaseVlan"),
        ("LUM-MES-MIB", "mesPortActingAsLine"),
        ("LUM-MES-MIB", "mesPortTrustedPortmask"),
        ("LUM-MES-MIB", "mesPortMacAddress"),
        ("LUM-MES-MIB", "mesPortLagStatus"),
        ("LUM-MES-MIB", "mesPortLagPortmask"),
        ("LUM-MES-MIB", "mesPortAssociateLag"),
        ("LUM-MES-MIB", "mesPortTxEthUtilization"),
        ("LUM-MES-MIB", "mesPortRxEthUtilization"),
        ("LUM-MES-MIB", "mesPortFlowControlMode"),
        ("LUM-MES-MIB", "mesPortAutoNegotiationMode"),
        ("LUM-MES-MIB", "mesPortAutoNegotiationStatus"),
        ("LUM-MES-MIB", "mesPortLinkDown"),
        ("LUM-MES-MIB", "mesPortLinkFaultRemote"),
        ("LUM-MES-MIB", "mesPortLinkFaultLocal"),
        ("LUM-MES-MIB", "mesPortNoOfShapers"),
        ("LUM-MES-MIB", "mesPortNoOfPolicers"),
        ("LUM-MES-MIB", "mesPortAssociateShaper"),
        ("LUM-MES-MIB", "mesPortReleaseShaper"),
        ("LUM-MES-MIB", "mesPortAssociatePolicer"),
        ("LUM-MES-MIB", "mesPortReleasePolicer"),
        ("LUM-MES-MIB", "mesPortRestartAutoNegotiation"),
        ("LUM-MES-MIB", "mesPortConfigureLine"),
        ("LUM-MES-MIB", "mesPortEtherType"),
        ("LUM-MES-MIB", "mesPortConfigureEtherType"),
        ("LUM-MES-MIB", "mesPortNoOfMirrorSources"),
        ("LUM-MES-MIB", "mesPortMirroring"),
        ("LUM-MES-MIB", "mesPortIngressPushTag"),
        ("LUM-MES-MIB", "mesPortEgressPopTag"),
        ("LUM-MES-MIB", "mesPortDefaultCeVlanPriority"),
        ("LUM-MES-MIB", "mesPortConfigureTagRule"),
        ("LUM-MES-MIB", "mesPortMode"),
        ("LUM-MES-MIB", "mesPortPrioAssignment"),
        ("LUM-MES-MIB", "mesPortConfigurePrioAssignment"),
        ("LUM-MES-MIB", "mesPortNoOfTagRules"),
        ("LUM-MES-MIB", "mesPortNoOfVlanSchedPrios"))
)
if mibBuilder.loadTexts:
    mesPortGroupV4.setStatus("deprecated")

mesMiscGroupV4 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 1, 1, 44)
)
mesMiscGroupV4.setObjects(
      *(("LUM-MES-MIB", "mesMiscIndex"),
        ("LUM-MES-MIB", "mesMiscName"),
        ("LUM-MES-MIB", "mesMiscObjectProperty"),
        ("LUM-MES-MIB", "mesMiscAdminStatus"),
        ("LUM-MES-MIB", "mesMiscOperStatus"),
        ("LUM-MES-MIB", "mesMiscMgmtVlanIpAddress"),
        ("LUM-MES-MIB", "mesMiscMgmtVlanNetMask"),
        ("LUM-MES-MIB", "mesMiscMgmtVlanMacAddress0"),
        ("LUM-MES-MIB", "mesMiscMgmtVlanMacAddress1"),
        ("LUM-MES-MIB", "mesMiscMgmtVlanMacAddress2"),
        ("LUM-MES-MIB", "mesMiscConfigureAddress"),
        ("LUM-MES-MIB", "mesMiscMgmtVlanNode"),
        ("LUM-MES-MIB", "mesMiscMacAgeing"),
        ("LUM-MES-MIB", "mesMiscMacGetTable"),
        ("LUM-MES-MIB", "mesMiscNoOfMegs"),
        ("LUM-MES-MIB", "mesMiscAssociateMeg"),
        ("LUM-MES-MIB", "mesMiscNoOfErps"),
        ("LUM-MES-MIB", "mesMiscAssociateErp"),
        ("LUM-MES-MIB", "mesMiscL2Mode"),
        ("LUM-MES-MIB", "mesMiscConfigureMode"),
        ("LUM-MES-MIB", "mesMiscIdentity"))
)
if mibBuilder.loadTexts:
    mesMiscGroupV4.setStatus("deprecated")

mesMaidGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 1, 1, 45)
)
mesMaidGroup.setObjects(
      *(("LUM-MES-MIB", "mesMaidIndex"),
        ("LUM-MES-MIB", "mesMaidName"),
        ("LUM-MES-MIB", "mesMaidGroupId"),
        ("LUM-MES-MIB", "mesMaidMdFormat"),
        ("LUM-MES-MIB", "mesMaidMdName"),
        ("LUM-MES-MIB", "mesMaidMdMac"),
        ("LUM-MES-MIB", "mesMaidMd2Octet"),
        ("LUM-MES-MIB", "mesMaidMdString"),
        ("LUM-MES-MIB", "mesMaidLevel"),
        ("LUM-MES-MIB", "mesMaidMaFormat"),
        ("LUM-MES-MIB", "mesMaidMaName"),
        ("LUM-MES-MIB", "mesMaidMaVpnOui"),
        ("LUM-MES-MIB", "mesMaidMaVpnIndex"),
        ("LUM-MES-MIB", "mesMaidMa2Octet"),
        ("LUM-MES-MIB", "mesMaidMaVlan"),
        ("LUM-MES-MIB", "mesMaidMaString"),
        ("LUM-MES-MIB", "mesMaidCcmInterval"),
        ("LUM-MES-MIB", "mesMaidInternalReference"),
        ("LUM-MES-MIB", "mesMaidIdentifier"),
        ("LUM-MES-MIB", "mesMaidNoOfMeps"),
        ("LUM-MES-MIB", "mesMaidAssociateMep"),
        ("LUM-MES-MIB", "mesMaidReleaseMeps"))
)
if mibBuilder.loadTexts:
    mesMaidGroup.setStatus("deprecated")

mesCfmMepGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 1, 1, 46)
)
mesCfmMepGroup.setObjects(
      *(("LUM-MES-MIB", "mesCfmMepIndex"),
        ("LUM-MES-MIB", "mesCfmMepName"),
        ("LUM-MES-MIB", "mesCfmMepMaid"),
        ("LUM-MES-MIB", "mesCfmMepTxPort"),
        ("LUM-MES-MIB", "mesCfmMepPortName"),
        ("LUM-MES-MIB", "mesCfmMepPrimaryVid"),
        ("LUM-MES-MIB", "mesCfmMepAdminStatus"),
        ("LUM-MES-MIB", "mesCfmMepOperStatus"),
        ("LUM-MES-MIB", "mesCfmMepVlanPriority"),
        ("LUM-MES-MIB", "mesCfmMepType"),
        ("LUM-MES-MIB", "mesCfmMepIdentifier"),
        ("LUM-MES-MIB", "mesCfmMepInternalReference"),
        ("LUM-MES-MIB", "mesCfmMepRDICCM"),
        ("LUM-MES-MIB", "mesCfmMepMACstatus"),
        ("LUM-MES-MIB", "mesCfmMepRemoteCCM"),
        ("LUM-MES-MIB", "mesCfmMepErrorCCM"),
        ("LUM-MES-MIB", "mesCfmMepXconCCM"),
        ("LUM-MES-MIB", "mesCfmMepAis"),
        ("LUM-MES-MIB", "mesCfmMepChangePort"))
)
if mibBuilder.loadTexts:
    mesCfmMepGroup.setStatus("deprecated")

mesErpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 1, 1, 47)
)
mesErpGroup.setObjects(
      *(("LUM-MES-MIB", "mesErpIndex"),
        ("LUM-MES-MIB", "mesErpName"),
        ("LUM-MES-MIB", "mesErpPortLeft"),
        ("LUM-MES-MIB", "mesErpPortRight"),
        ("LUM-MES-MIB", "mesErpAdminStatus"),
        ("LUM-MES-MIB", "mesErpInternalReference"),
        ("LUM-MES-MIB", "mesErpDescr"),
        ("LUM-MES-MIB", "mesErpVlanId"),
        ("LUM-MES-MIB", "mesErpMegLevel"),
        ("LUM-MES-MIB", "mesErpProtLink"),
        ("LUM-MES-MIB", "mesErpGuardTime"),
        ("LUM-MES-MIB", "mesErpHoldOffTime"),
        ("LUM-MES-MIB", "mesErpWtrTime"),
        ("LUM-MES-MIB", "mesErpOamDetectionLeft"),
        ("LUM-MES-MIB", "mesErpOamDetectionRight"),
        ("LUM-MES-MIB", "mesErpStatusLeft"),
        ("LUM-MES-MIB", "mesErpStatusRight"),
        ("LUM-MES-MIB", "mesErpProtState"),
        ("LUM-MES-MIB", "mesErpActiveEvent"),
        ("LUM-MES-MIB", "mesErpRapsReqState"),
        ("LUM-MES-MIB", "mesErpServiceFailure"),
        ("LUM-MES-MIB", "mesErpServiceDegraded"),
        ("LUM-MES-MIB", "mesErpUnexpectedMegLevel"),
        ("LUM-MES-MIB", "mesErpCommunicationFailure"),
        ("LUM-MES-MIB", "mesErpChangePort"))
)
if mibBuilder.loadTexts:
    mesErpGroup.setStatus("deprecated")

mesVlanMapGroupV3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 1, 1, 48)
)
mesVlanMapGroupV3.setObjects(
      *(("LUM-MES-MIB", "mesVlanMapIndex"),
        ("LUM-MES-MIB", "mesVlanMapName"),
        ("LUM-MES-MIB", "mesVlanMapVlanIdRangeLower"),
        ("LUM-MES-MIB", "mesVlanMapVlanIdRangeUpper"),
        ("LUM-MES-MIB", "mesVlanMapInternalReference"),
        ("LUM-MES-MIB", "mesVlanMapPortmask"),
        ("LUM-MES-MIB", "mesVlanMapConfigurePortMask"),
        ("LUM-MES-MIB", "mesVlanMapLearning"),
        ("LUM-MES-MIB", "mesVlanMapEtherType"))
)
if mibBuilder.loadTexts:
    mesVlanMapGroupV3.setStatus("deprecated")

mesVlanTagRuleGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 1, 1, 49)
)
mesVlanTagRuleGroupV2.setObjects(
      *(("LUM-MES-MIB", "mesVlanTagRuleIndex"),
        ("LUM-MES-MIB", "mesVlanTagRuleName"),
        ("LUM-MES-MIB", "mesVlanTagRuleInternalReference"),
        ("LUM-MES-MIB", "mesVlanTagRuleClassificationName"),
        ("LUM-MES-MIB", "mesVlanTagRuleType"),
        ("LUM-MES-MIB", "mesVlanTagRuleOperation"),
        ("LUM-MES-MIB", "mesVlanTagRuleInnerVlanId"),
        ("LUM-MES-MIB", "mesVlanTagRuleInnerPrio"),
        ("LUM-MES-MIB", "mesVlanTagRuleOuterVlanId"),
        ("LUM-MES-MIB", "mesVlanTagRuleOuterPrio"),
        ("LUM-MES-MIB", "mesVlanTagRulePrioAssignment"),
        ("LUM-MES-MIB", "mesVlanTagRuleConfigurePrioAssignment"),
        ("LUM-MES-MIB", "mesVlanTagRuleQueue"))
)
if mibBuilder.loadTexts:
    mesVlanTagRuleGroupV2.setStatus("deprecated")

mesVlanTagClassVlanGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 1, 1, 50)
)
mesVlanTagClassVlanGroupV2.setObjects(
      *(("LUM-MES-MIB", "mesVlanTagClassVlanIndex"),
        ("LUM-MES-MIB", "mesVlanTagClassVlanName"),
        ("LUM-MES-MIB", "mesVlanTagClassVlanTxPort"),
        ("LUM-MES-MIB", "mesVlanTagClassVlanInternalReference"),
        ("LUM-MES-MIB", "mesVlanTagClassVlanRuleName"),
        ("LUM-MES-MIB", "mesVlanTagClassVlanRuleIndex"),
        ("LUM-MES-MIB", "mesVlanTagClassVlanOuterVlanId"))
)
if mibBuilder.loadTexts:
    mesVlanTagClassVlanGroupV2.setStatus("deprecated")

mesMirroringGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 1, 1, 51)
)
mesMirroringGroupV2.setObjects(
      *(("LUM-MES-MIB", "mesMirroringIndex"),
        ("LUM-MES-MIB", "mesMirroringName"),
        ("LUM-MES-MIB", "mesMirroringDestination"),
        ("LUM-MES-MIB", "mesMirroringDirection"),
        ("LUM-MES-MIB", "mesMirroringConfigureDestination"))
)
if mibBuilder.loadTexts:
    mesMirroringGroupV2.setStatus("deprecated")

mesShapingGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 1, 1, 52)
)
mesShapingGroupV2.setObjects(
      *(("LUM-MES-MIB", "mesShapingIndex"),
        ("LUM-MES-MIB", "mesShapingName"),
        ("LUM-MES-MIB", "mesShapingRate"),
        ("LUM-MES-MIB", "mesShapingBurstSize"),
        ("LUM-MES-MIB", "mesShapingQueue"),
        ("LUM-MES-MIB", "mesShapingInternalReference"),
        ("LUM-MES-MIB", "mesShapingExcess"),
        ("LUM-MES-MIB", "mesShapingIdentifier"),
        ("LUM-MES-MIB", "mesShapingMinRate"))
)
if mibBuilder.loadTexts:
    mesShapingGroupV2.setStatus("deprecated")

mesPortGroupV5 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 1, 1, 53)
)
mesPortGroupV5.setObjects(
      *(("LUM-MES-MIB", "mesPortIndex"),
        ("LUM-MES-MIB", "mesPortName"),
        ("LUM-MES-MIB", "mesPortDescr"),
        ("LUM-MES-MIB", "mesPortSubrack"),
        ("LUM-MES-MIB", "mesPortSlot"),
        ("LUM-MES-MIB", "mesPortTxPort"),
        ("LUM-MES-MIB", "mesPortRxPort"),
        ("LUM-MES-MIB", "mesPortAdminStatus"),
        ("LUM-MES-MIB", "mesPortOperStatus"),
        ("LUM-MES-MIB", "mesPortMtuSize"),
        ("LUM-MES-MIB", "mesPortTagType"),
        ("LUM-MES-MIB", "mesPortNoOfVlans"),
        ("LUM-MES-MIB", "mesPortVlanAware"),
        ("LUM-MES-MIB", "mesPortVlanTagged"),
        ("LUM-MES-MIB", "mesPortVlanUntagged"),
        ("LUM-MES-MIB", "mesPortIngressFiltering"),
        ("LUM-MES-MIB", "mesPortEgressTag"),
        ("LUM-MES-MIB", "mesPortDefaultCeVlanId"),
        ("LUM-MES-MIB", "mesPortAssociateVlan"),
        ("LUM-MES-MIB", "mesPortReleaseVlan"),
        ("LUM-MES-MIB", "mesPortActingAsLine"),
        ("LUM-MES-MIB", "mesPortTrustedPortmask"),
        ("LUM-MES-MIB", "mesPortMacAddress"),
        ("LUM-MES-MIB", "mesPortLagStatus"),
        ("LUM-MES-MIB", "mesPortLagPortmask"),
        ("LUM-MES-MIB", "mesPortAssociateLag"),
        ("LUM-MES-MIB", "mesPortTxEthUtilization"),
        ("LUM-MES-MIB", "mesPortRxEthUtilization"),
        ("LUM-MES-MIB", "mesPortFlowControlMode"),
        ("LUM-MES-MIB", "mesPortAutoNegotiationMode"),
        ("LUM-MES-MIB", "mesPortAutoNegotiationStatus"),
        ("LUM-MES-MIB", "mesPortLinkDown"),
        ("LUM-MES-MIB", "mesPortLinkFaultRemote"),
        ("LUM-MES-MIB", "mesPortLinkFaultLocal"),
        ("LUM-MES-MIB", "mesPortNoOfShapers"),
        ("LUM-MES-MIB", "mesPortNoOfPolicers"),
        ("LUM-MES-MIB", "mesPortAssociateShaper"),
        ("LUM-MES-MIB", "mesPortReleaseShaper"),
        ("LUM-MES-MIB", "mesPortAssociatePolicer"),
        ("LUM-MES-MIB", "mesPortReleasePolicer"),
        ("LUM-MES-MIB", "mesPortRestartAutoNegotiation"),
        ("LUM-MES-MIB", "mesPortConfigureLine"),
        ("LUM-MES-MIB", "mesPortEtherType"),
        ("LUM-MES-MIB", "mesPortConfigureEtherType"),
        ("LUM-MES-MIB", "mesPortNoOfMirrorSources"),
        ("LUM-MES-MIB", "mesPortMirroring"),
        ("LUM-MES-MIB", "mesPortIngressPushTag"),
        ("LUM-MES-MIB", "mesPortEgressPopTag"),
        ("LUM-MES-MIB", "mesPortDefaultCeVlanPriority"),
        ("LUM-MES-MIB", "mesPortConfigureTagRule"),
        ("LUM-MES-MIB", "mesPortMode"),
        ("LUM-MES-MIB", "mesPortPrioAssignment"),
        ("LUM-MES-MIB", "mesPortConfigurePrioAssignment"),
        ("LUM-MES-MIB", "mesPortNoOfTagRules"),
        ("LUM-MES-MIB", "mesPortNoOfVlanSchedPrios"))
)
if mibBuilder.loadTexts:
    mesPortGroupV5.setStatus("deprecated")

mesBwpMapGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 1, 1, 54)
)
mesBwpMapGroupV2.setObjects(
      *(("LUM-MES-MIB", "mesBwpMapIndex"),
        ("LUM-MES-MIB", "mesBwpMapName"),
        ("LUM-MES-MIB", "mesBwpMapPortName"),
        ("LUM-MES-MIB", "mesBwpMapBwpName"),
        ("LUM-MES-MIB", "mesBwpMapInternalReference"))
)
if mibBuilder.loadTexts:
    mesBwpMapGroupV2.setStatus("current")

mesClassGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 1, 1, 55)
)
mesClassGroup.setObjects(
      *(("LUM-MES-MIB", "mesClassIndex"),
        ("LUM-MES-MIB", "mesClassName"),
        ("LUM-MES-MIB", "mesClassIdentifier"),
        ("LUM-MES-MIB", "mesClassPort"),
        ("LUM-MES-MIB", "mesClassLagId"),
        ("LUM-MES-MIB", "mesClassInternalReference"),
        ("LUM-MES-MIB", "mesClassOuterVlanId"),
        ("LUM-MES-MIB", "mesClassOuterVlanPcp"),
        ("LUM-MES-MIB", "mesClassPrecedence"),
        ("LUM-MES-MIB", "mesClassDaMacAddress"),
        ("LUM-MES-MIB", "mesClassAssociateAction"),
        ("LUM-MES-MIB", "mesClassRowStatus"))
)
if mibBuilder.loadTexts:
    mesClassGroup.setStatus("deprecated")

mesMiscGroupV5 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 1, 1, 56)
)
mesMiscGroupV5.setObjects(
      *(("LUM-MES-MIB", "mesMiscIndex"),
        ("LUM-MES-MIB", "mesMiscName"),
        ("LUM-MES-MIB", "mesMiscObjectProperty"),
        ("LUM-MES-MIB", "mesMiscAdminStatus"),
        ("LUM-MES-MIB", "mesMiscOperStatus"),
        ("LUM-MES-MIB", "mesMiscMgmtVlanIpAddress"),
        ("LUM-MES-MIB", "mesMiscMgmtVlanNetMask"),
        ("LUM-MES-MIB", "mesMiscMgmtVlanMacAddress0"),
        ("LUM-MES-MIB", "mesMiscMgmtVlanMacAddress1"),
        ("LUM-MES-MIB", "mesMiscMgmtVlanMacAddress2"),
        ("LUM-MES-MIB", "mesMiscConfigureAddress"),
        ("LUM-MES-MIB", "mesMiscMgmtVlanNode"),
        ("LUM-MES-MIB", "mesMiscMacAgeing"),
        ("LUM-MES-MIB", "mesMiscMacGetTable"),
        ("LUM-MES-MIB", "mesMiscNoOfMegs"),
        ("LUM-MES-MIB", "mesMiscAssociateMeg"),
        ("LUM-MES-MIB", "mesMiscNoOfErps"),
        ("LUM-MES-MIB", "mesMiscAssociateErp"),
        ("LUM-MES-MIB", "mesMiscL2Mode"),
        ("LUM-MES-MIB", "mesMiscConfigureMode"),
        ("LUM-MES-MIB", "mesMiscIdentity"),
        ("LUM-MES-MIB", "mesMiscAssociateClass"),
        ("LUM-MES-MIB", "mesMiscAssociateBwp"),
        ("LUM-MES-MIB", "mesMiscWred"))
)
if mibBuilder.loadTexts:
    mesMiscGroupV5.setStatus("deprecated")

mesActionGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 1, 1, 57)
)
mesActionGroup.setObjects(
      *(("LUM-MES-MIB", "mesActionIndex"),
        ("LUM-MES-MIB", "mesActionName"),
        ("LUM-MES-MIB", "mesActionIdentifier"),
        ("LUM-MES-MIB", "mesActionInternalReference"),
        ("LUM-MES-MIB", "mesActionType"),
        ("LUM-MES-MIB", "mesActionOuterVlanId"),
        ("LUM-MES-MIB", "mesActionPcp"),
        ("LUM-MES-MIB", "mesActionPolicerId"),
        ("LUM-MES-MIB", "mesActionInnerVlanId"),
        ("LUM-MES-MIB", "mesActionQueue"),
        ("LUM-MES-MIB", "mesActionRowStatus"))
)
if mibBuilder.loadTexts:
    mesActionGroup.setStatus("deprecated")

mesPolicyGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 1, 1, 58)
)
mesPolicyGroup.setObjects(
      *(("LUM-MES-MIB", "mesPolicyIndex"),
        ("LUM-MES-MIB", "mesPolicyName"),
        ("LUM-MES-MIB", "mesPolicyInternalReference"),
        ("LUM-MES-MIB", "mesPolicyClass"),
        ("LUM-MES-MIB", "mesPolicyAction"))
)
if mibBuilder.loadTexts:
    mesPolicyGroup.setStatus("deprecated")

mesCosProfileGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 1, 1, 59)
)
mesCosProfileGroupV2.setObjects(
      *(("LUM-MES-MIB", "mesCosProfileIndex"),
        ("LUM-MES-MIB", "mesCosProfileName"),
        ("LUM-MES-MIB", "mesCosProfilePortmask"),
        ("LUM-MES-MIB", "mesCosProfileScheduler"),
        ("LUM-MES-MIB", "mesCosProfileWeight0"),
        ("LUM-MES-MIB", "mesCosProfileWeight1"),
        ("LUM-MES-MIB", "mesCosProfileWeight2"),
        ("LUM-MES-MIB", "mesCosProfileWeight3"),
        ("LUM-MES-MIB", "mesCosProfileWeight4"),
        ("LUM-MES-MIB", "mesCosProfileWeight5"),
        ("LUM-MES-MIB", "mesCosProfileWeight6"),
        ("LUM-MES-MIB", "mesCosProfileWeight7"),
        ("LUM-MES-MIB", "mesCosProfilePriority0"),
        ("LUM-MES-MIB", "mesCosProfilePriority1"),
        ("LUM-MES-MIB", "mesCosProfilePriority2"),
        ("LUM-MES-MIB", "mesCosProfilePriority3"),
        ("LUM-MES-MIB", "mesCosProfilePriority4"),
        ("LUM-MES-MIB", "mesCosProfilePriority5"),
        ("LUM-MES-MIB", "mesCosProfilePriority6"),
        ("LUM-MES-MIB", "mesCosProfilePriority7"),
        ("LUM-MES-MIB", "mesCosProfileConfigureScheduler"),
        ("LUM-MES-MIB", "mesCosProfileIngressPcpDecoding"),
        ("LUM-MES-MIB", "mesCosProfileIngressDeiDecoding"),
        ("LUM-MES-MIB", "mesCosProfileIngressColor0"),
        ("LUM-MES-MIB", "mesCosProfileIngressColor1"),
        ("LUM-MES-MIB", "mesCosProfileIngressColor2"),
        ("LUM-MES-MIB", "mesCosProfileIngressColor3"),
        ("LUM-MES-MIB", "mesCosProfileIngressColor4"),
        ("LUM-MES-MIB", "mesCosProfileIngressColor5"),
        ("LUM-MES-MIB", "mesCosProfileIngressColor6"),
        ("LUM-MES-MIB", "mesCosProfileIngressColor7"),
        ("LUM-MES-MIB", "mesCosProfileEgressPcpEncoding"),
        ("LUM-MES-MIB", "mesCosProfileEgressDeiEncoding"),
        ("LUM-MES-MIB", "mesCosProfileEgressPcpGreen0"),
        ("LUM-MES-MIB", "mesCosProfileEgressPcpGreen1"),
        ("LUM-MES-MIB", "mesCosProfileEgressPcpGreen2"),
        ("LUM-MES-MIB", "mesCosProfileEgressPcpGreen3"),
        ("LUM-MES-MIB", "mesCosProfileEgressPcpGreen4"),
        ("LUM-MES-MIB", "mesCosProfileEgressPcpGreen5"),
        ("LUM-MES-MIB", "mesCosProfileEgressPcpGreen6"),
        ("LUM-MES-MIB", "mesCosProfileEgressPcpGreen7"),
        ("LUM-MES-MIB", "mesCosProfileEgressPcpYellow0"),
        ("LUM-MES-MIB", "mesCosProfileEgressPcpYellow1"),
        ("LUM-MES-MIB", "mesCosProfileEgressPcpYellow2"),
        ("LUM-MES-MIB", "mesCosProfileEgressPcpYellow3"),
        ("LUM-MES-MIB", "mesCosProfileEgressPcpYellow4"),
        ("LUM-MES-MIB", "mesCosProfileEgressPcpYellow5"),
        ("LUM-MES-MIB", "mesCosProfileEgressPcpYellow6"),
        ("LUM-MES-MIB", "mesCosProfileEgressPcpYellow7"))
)
if mibBuilder.loadTexts:
    mesCosProfileGroupV2.setStatus("deprecated")

mesLagGroupV3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 1, 1, 60)
)
mesLagGroupV3.setObjects(
      *(("LUM-MES-MIB", "mesLagIndex"),
        ("LUM-MES-MIB", "mesLagName"),
        ("LUM-MES-MIB", "mesLagInternalReference"),
        ("LUM-MES-MIB", "mesLagPortmask"),
        ("LUM-MES-MIB", "mesLagMasterIndex"),
        ("LUM-MES-MIB", "mesLagConfigure"),
        ("LUM-MES-MIB", "mesLagHash"),
        ("LUM-MES-MIB", "mesLagIdentifier"),
        ("LUM-MES-MIB", "mesLagRowStatus"))
)
if mibBuilder.loadTexts:
    mesLagGroupV3.setStatus("deprecated")

mesVlanMapGroupV4 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 1, 1, 61)
)
mesVlanMapGroupV4.setObjects(
      *(("LUM-MES-MIB", "mesVlanMapIndex"),
        ("LUM-MES-MIB", "mesVlanMapName"),
        ("LUM-MES-MIB", "mesVlanMapVlanIdRangeLower"),
        ("LUM-MES-MIB", "mesVlanMapVlanIdRangeUpper"),
        ("LUM-MES-MIB", "mesVlanMapInternalReference"),
        ("LUM-MES-MIB", "mesVlanMapPortmask"),
        ("LUM-MES-MIB", "mesVlanMapConfigurePortMask"),
        ("LUM-MES-MIB", "mesVlanMapLearning"),
        ("LUM-MES-MIB", "mesVlanMapEtherType"),
        ("LUM-MES-MIB", "mesVlanMapRowStatus"))
)
if mibBuilder.loadTexts:
    mesVlanMapGroupV4.setStatus("deprecated")

mesCfmMepGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 1, 1, 62)
)
mesCfmMepGroupV2.setObjects(
      *(("LUM-MES-MIB", "mesCfmMepIndex"),
        ("LUM-MES-MIB", "mesCfmMepName"),
        ("LUM-MES-MIB", "mesCfmMepMaid"),
        ("LUM-MES-MIB", "mesCfmMepTxPort"),
        ("LUM-MES-MIB", "mesCfmMepPortName"),
        ("LUM-MES-MIB", "mesCfmMepPrimaryVid"),
        ("LUM-MES-MIB", "mesCfmMepAdminStatus"),
        ("LUM-MES-MIB", "mesCfmMepOperStatus"),
        ("LUM-MES-MIB", "mesCfmMepVlanPriority"),
        ("LUM-MES-MIB", "mesCfmMepType"),
        ("LUM-MES-MIB", "mesCfmMepIdentifier"),
        ("LUM-MES-MIB", "mesCfmMepInternalReference"),
        ("LUM-MES-MIB", "mesCfmMepRDICCM"),
        ("LUM-MES-MIB", "mesCfmMepMACstatus"),
        ("LUM-MES-MIB", "mesCfmMepRemoteCCM"),
        ("LUM-MES-MIB", "mesCfmMepErrorCCM"),
        ("LUM-MES-MIB", "mesCfmMepXconCCM"),
        ("LUM-MES-MIB", "mesCfmMepAis"),
        ("LUM-MES-MIB", "mesCfmMepChangePort"),
        ("LUM-MES-MIB", "mesCfmMepTransmitLbrStatus"),
        ("LUM-MES-MIB", "mesCfmMepRowStatus"))
)
if mibBuilder.loadTexts:
    mesCfmMepGroupV2.setStatus("deprecated")

mesVlanTagRuleGroupV3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 1, 1, 63)
)
mesVlanTagRuleGroupV3.setObjects(
      *(("LUM-MES-MIB", "mesVlanTagRuleIndex"),
        ("LUM-MES-MIB", "mesVlanTagRuleName"),
        ("LUM-MES-MIB", "mesVlanTagRuleInternalReference"),
        ("LUM-MES-MIB", "mesVlanTagRuleClassificationName"),
        ("LUM-MES-MIB", "mesVlanTagRuleType"),
        ("LUM-MES-MIB", "mesVlanTagRuleOperation"),
        ("LUM-MES-MIB", "mesVlanTagRuleInnerVlanId"),
        ("LUM-MES-MIB", "mesVlanTagRuleInnerPrio"),
        ("LUM-MES-MIB", "mesVlanTagRuleOuterVlanId"),
        ("LUM-MES-MIB", "mesVlanTagRuleOuterPrio"),
        ("LUM-MES-MIB", "mesVlanTagRulePrioAssignment"),
        ("LUM-MES-MIB", "mesVlanTagRuleConfigurePrioAssignment"),
        ("LUM-MES-MIB", "mesVlanTagRuleQueue"),
        ("LUM-MES-MIB", "mesVlanTagRuleRowStatus"))
)
if mibBuilder.loadTexts:
    mesVlanTagRuleGroupV3.setStatus("deprecated")

mesErpGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 1, 1, 64)
)
mesErpGroupV2.setObjects(
      *(("LUM-MES-MIB", "mesErpIndex"),
        ("LUM-MES-MIB", "mesErpName"),
        ("LUM-MES-MIB", "mesErpPortLeft"),
        ("LUM-MES-MIB", "mesErpPortRight"),
        ("LUM-MES-MIB", "mesErpAdminStatus"),
        ("LUM-MES-MIB", "mesErpInternalReference"),
        ("LUM-MES-MIB", "mesErpDescr"),
        ("LUM-MES-MIB", "mesErpVlanId"),
        ("LUM-MES-MIB", "mesErpMegLevel"),
        ("LUM-MES-MIB", "mesErpProtLink"),
        ("LUM-MES-MIB", "mesErpGuardTime"),
        ("LUM-MES-MIB", "mesErpHoldOffTime"),
        ("LUM-MES-MIB", "mesErpWtrTime"),
        ("LUM-MES-MIB", "mesErpOamDetectionLeft"),
        ("LUM-MES-MIB", "mesErpOamDetectionRight"),
        ("LUM-MES-MIB", "mesErpStatusLeft"),
        ("LUM-MES-MIB", "mesErpStatusRight"),
        ("LUM-MES-MIB", "mesErpProtState"),
        ("LUM-MES-MIB", "mesErpActiveEvent"),
        ("LUM-MES-MIB", "mesErpRapsReqState"),
        ("LUM-MES-MIB", "mesErpServiceFailure"),
        ("LUM-MES-MIB", "mesErpServiceDegraded"),
        ("LUM-MES-MIB", "mesErpUnexpectedMegLevel"),
        ("LUM-MES-MIB", "mesErpCommunicationFailure"),
        ("LUM-MES-MIB", "mesErpChangePort"),
        ("LUM-MES-MIB", "mesErpRowStatus"))
)
if mibBuilder.loadTexts:
    mesErpGroupV2.setStatus("deprecated")

mesMaidGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 1, 1, 65)
)
mesMaidGroupV2.setObjects(
      *(("LUM-MES-MIB", "mesMaidIndex"),
        ("LUM-MES-MIB", "mesMaidName"),
        ("LUM-MES-MIB", "mesMaidGroupId"),
        ("LUM-MES-MIB", "mesMaidMdFormat"),
        ("LUM-MES-MIB", "mesMaidMdName"),
        ("LUM-MES-MIB", "mesMaidMdMac"),
        ("LUM-MES-MIB", "mesMaidMd2Octet"),
        ("LUM-MES-MIB", "mesMaidMdString"),
        ("LUM-MES-MIB", "mesMaidLevel"),
        ("LUM-MES-MIB", "mesMaidMaFormat"),
        ("LUM-MES-MIB", "mesMaidMaName"),
        ("LUM-MES-MIB", "mesMaidMaVpnOui"),
        ("LUM-MES-MIB", "mesMaidMaVpnIndex"),
        ("LUM-MES-MIB", "mesMaidMa2Octet"),
        ("LUM-MES-MIB", "mesMaidMaVlan"),
        ("LUM-MES-MIB", "mesMaidMaString"),
        ("LUM-MES-MIB", "mesMaidCcmInterval"),
        ("LUM-MES-MIB", "mesMaidInternalReference"),
        ("LUM-MES-MIB", "mesMaidIdentifier"),
        ("LUM-MES-MIB", "mesMaidNoOfMeps"),
        ("LUM-MES-MIB", "mesMaidAssociateMep"),
        ("LUM-MES-MIB", "mesMaidReleaseMeps"),
        ("LUM-MES-MIB", "mesMaidRowStatus"))
)
if mibBuilder.loadTexts:
    mesMaidGroupV2.setStatus("deprecated")

mesMiscGroupV6 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 1, 1, 66)
)
mesMiscGroupV6.setObjects(
      *(("LUM-MES-MIB", "mesMiscIndex"),
        ("LUM-MES-MIB", "mesMiscName"),
        ("LUM-MES-MIB", "mesMiscObjectProperty"),
        ("LUM-MES-MIB", "mesMiscAdminStatus"),
        ("LUM-MES-MIB", "mesMiscOperStatus"),
        ("LUM-MES-MIB", "mesMiscMgmtVlanIpAddress"),
        ("LUM-MES-MIB", "mesMiscMgmtVlanNetMask"),
        ("LUM-MES-MIB", "mesMiscMgmtVlanMacAddress0"),
        ("LUM-MES-MIB", "mesMiscMgmtVlanMacAddress1"),
        ("LUM-MES-MIB", "mesMiscMgmtVlanMacAddress2"),
        ("LUM-MES-MIB", "mesMiscConfigureAddress"),
        ("LUM-MES-MIB", "mesMiscMgmtVlanNode"),
        ("LUM-MES-MIB", "mesMiscMacAgeing"),
        ("LUM-MES-MIB", "mesMiscMacGetTable"),
        ("LUM-MES-MIB", "mesMiscNoOfMegs"),
        ("LUM-MES-MIB", "mesMiscAssociateMeg"),
        ("LUM-MES-MIB", "mesMiscNoOfErps"),
        ("LUM-MES-MIB", "mesMiscAssociateErp"),
        ("LUM-MES-MIB", "mesMiscL2Mode"),
        ("LUM-MES-MIB", "mesMiscConfigureMode"),
        ("LUM-MES-MIB", "mesMiscIdentity"),
        ("LUM-MES-MIB", "mesMiscAssociateClass"),
        ("LUM-MES-MIB", "mesMiscAssociateBwp"),
        ("LUM-MES-MIB", "mesMiscWred"),
        ("LUM-MES-MIB", "mesMiscGetPacketMonitor"))
)
if mibBuilder.loadTexts:
    mesMiscGroupV6.setStatus("deprecated")

mesVlanMapGroupV5 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 1, 1, 67)
)
mesVlanMapGroupV5.setObjects(
      *(("LUM-MES-MIB", "mesVlanMapIndex"),
        ("LUM-MES-MIB", "mesVlanMapName"),
        ("LUM-MES-MIB", "mesVlanMapVlanIdRangeLower"),
        ("LUM-MES-MIB", "mesVlanMapVlanIdRangeUpper"),
        ("LUM-MES-MIB", "mesVlanMapInternalReference"),
        ("LUM-MES-MIB", "mesVlanMapPortmask"),
        ("LUM-MES-MIB", "mesVlanMapConfigurePortMask"),
        ("LUM-MES-MIB", "mesVlanMapLearning"),
        ("LUM-MES-MIB", "mesVlanMapEtherType"),
        ("LUM-MES-MIB", "mesVlanMapRowStatus"),
        ("LUM-MES-MIB", "mesVlanMapDescr"),
        ("LUM-MES-MIB", "mesVlanMapTrustPorts"))
)
if mibBuilder.loadTexts:
    mesVlanMapGroupV5.setStatus("current")

mesClassGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 1, 1, 68)
)
mesClassGroupV2.setObjects(
      *(("LUM-MES-MIB", "mesClassIndex"),
        ("LUM-MES-MIB", "mesClassName"),
        ("LUM-MES-MIB", "mesClassIdentifier"),
        ("LUM-MES-MIB", "mesClassPort"),
        ("LUM-MES-MIB", "mesClassLagId"),
        ("LUM-MES-MIB", "mesClassInternalReference"),
        ("LUM-MES-MIB", "mesClassOuterVlanId"),
        ("LUM-MES-MIB", "mesClassOuterVlanPcp"),
        ("LUM-MES-MIB", "mesClassPrecedence"),
        ("LUM-MES-MIB", "mesClassDaMacAddress"),
        ("LUM-MES-MIB", "mesClassAssociateAction"),
        ("LUM-MES-MIB", "mesClassRowStatus"),
        ("LUM-MES-MIB", "mesClassDaMacAddressMask"),
        ("LUM-MES-MIB", "mesClassDSCP"),
        ("LUM-MES-MIB", "mesClassInnerVlanId"),
        ("LUM-MES-MIB", "mesClassInnerVlanPcp"),
        ("LUM-MES-MIB", "mesClassInnerVlanCfi"),
        ("LUM-MES-MIB", "mesClassOuterVlanCfi"),
        ("LUM-MES-MIB", "mesClassDirection"),
        ("LUM-MES-MIB", "mesClassOuterTpid"))
)
if mibBuilder.loadTexts:
    mesClassGroupV2.setStatus("deprecated")

mesPortGroupV6 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 1, 1, 69)
)
mesPortGroupV6.setObjects(
      *(("LUM-MES-MIB", "mesPortIndex"),
        ("LUM-MES-MIB", "mesPortName"),
        ("LUM-MES-MIB", "mesPortDescr"),
        ("LUM-MES-MIB", "mesPortSubrack"),
        ("LUM-MES-MIB", "mesPortSlot"),
        ("LUM-MES-MIB", "mesPortTxPort"),
        ("LUM-MES-MIB", "mesPortRxPort"),
        ("LUM-MES-MIB", "mesPortAdminStatus"),
        ("LUM-MES-MIB", "mesPortOperStatus"),
        ("LUM-MES-MIB", "mesPortMtuSize"),
        ("LUM-MES-MIB", "mesPortTagType"),
        ("LUM-MES-MIB", "mesPortNoOfVlans"),
        ("LUM-MES-MIB", "mesPortVlanAware"),
        ("LUM-MES-MIB", "mesPortVlanTagged"),
        ("LUM-MES-MIB", "mesPortVlanUntagged"),
        ("LUM-MES-MIB", "mesPortIngressFiltering"),
        ("LUM-MES-MIB", "mesPortEgressTag"),
        ("LUM-MES-MIB", "mesPortDefaultCeVlanId"),
        ("LUM-MES-MIB", "mesPortAssociateVlan"),
        ("LUM-MES-MIB", "mesPortReleaseVlan"),
        ("LUM-MES-MIB", "mesPortActingAsLine"),
        ("LUM-MES-MIB", "mesPortTrustedPortmask"),
        ("LUM-MES-MIB", "mesPortMacAddress"),
        ("LUM-MES-MIB", "mesPortLagStatus"),
        ("LUM-MES-MIB", "mesPortLagPortmask"),
        ("LUM-MES-MIB", "mesPortAssociateLag"),
        ("LUM-MES-MIB", "mesPortTxEthUtilization"),
        ("LUM-MES-MIB", "mesPortRxEthUtilization"),
        ("LUM-MES-MIB", "mesPortFlowControlMode"),
        ("LUM-MES-MIB", "mesPortAutoNegotiationMode"),
        ("LUM-MES-MIB", "mesPortAutoNegotiationStatus"),
        ("LUM-MES-MIB", "mesPortLinkDown"),
        ("LUM-MES-MIB", "mesPortLinkFaultRemote"),
        ("LUM-MES-MIB", "mesPortLinkFaultLocal"),
        ("LUM-MES-MIB", "mesPortNoOfShapers"),
        ("LUM-MES-MIB", "mesPortNoOfPolicers"),
        ("LUM-MES-MIB", "mesPortAssociateShaper"),
        ("LUM-MES-MIB", "mesPortReleaseShaper"),
        ("LUM-MES-MIB", "mesPortAssociatePolicer"),
        ("LUM-MES-MIB", "mesPortReleasePolicer"),
        ("LUM-MES-MIB", "mesPortRestartAutoNegotiation"),
        ("LUM-MES-MIB", "mesPortConfigureLine"),
        ("LUM-MES-MIB", "mesPortEtherType"),
        ("LUM-MES-MIB", "mesPortConfigureEtherType"),
        ("LUM-MES-MIB", "mesPortNoOfMirrorSources"),
        ("LUM-MES-MIB", "mesPortMirroring"),
        ("LUM-MES-MIB", "mesPortIngressPushTag"),
        ("LUM-MES-MIB", "mesPortEgressPopTag"),
        ("LUM-MES-MIB", "mesPortDefaultCeVlanPriority"),
        ("LUM-MES-MIB", "mesPortConfigureTagRule"),
        ("LUM-MES-MIB", "mesPortMode"),
        ("LUM-MES-MIB", "mesPortPrioAssignment"),
        ("LUM-MES-MIB", "mesPortConfigurePrioAssignment"),
        ("LUM-MES-MIB", "mesPortNoOfTagRules"),
        ("LUM-MES-MIB", "mesPortNoOfVlanSchedPrios"),
        ("LUM-MES-MIB", "mesPortObjectProperty"),
        ("LUM-MES-MIB", "mesPortHighBitErrorRate"))
)
if mibBuilder.loadTexts:
    mesPortGroupV6.setStatus("deprecated")

mesMiscGroupV7 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 1, 1, 70)
)
mesMiscGroupV7.setObjects(
      *(("LUM-MES-MIB", "mesMiscIndex"),
        ("LUM-MES-MIB", "mesMiscName"),
        ("LUM-MES-MIB", "mesMiscObjectProperty"),
        ("LUM-MES-MIB", "mesMiscAdminStatus"),
        ("LUM-MES-MIB", "mesMiscOperStatus"),
        ("LUM-MES-MIB", "mesMiscMgmtVlanIpAddress"),
        ("LUM-MES-MIB", "mesMiscMgmtVlanNetMask"),
        ("LUM-MES-MIB", "mesMiscMgmtVlanMacAddress0"),
        ("LUM-MES-MIB", "mesMiscMgmtVlanMacAddress1"),
        ("LUM-MES-MIB", "mesMiscMgmtVlanMacAddress2"),
        ("LUM-MES-MIB", "mesMiscConfigureAddress"),
        ("LUM-MES-MIB", "mesMiscMgmtVlanNode"),
        ("LUM-MES-MIB", "mesMiscMacAgeing"),
        ("LUM-MES-MIB", "mesMiscMacGetTable"),
        ("LUM-MES-MIB", "mesMiscNoOfMegs"),
        ("LUM-MES-MIB", "mesMiscAssociateMeg"),
        ("LUM-MES-MIB", "mesMiscNoOfErps"),
        ("LUM-MES-MIB", "mesMiscAssociateErp"),
        ("LUM-MES-MIB", "mesMiscL2Mode"),
        ("LUM-MES-MIB", "mesMiscConfigureMode"),
        ("LUM-MES-MIB", "mesMiscIdentity"),
        ("LUM-MES-MIB", "mesMiscAssociateClass"),
        ("LUM-MES-MIB", "mesMiscAssociateBwp"),
        ("LUM-MES-MIB", "mesMiscWred"),
        ("LUM-MES-MIB", "mesMiscGetPacketMonitor"),
        ("LUM-MES-MIB", "mesMiscSfpPortUsageCurrent"),
        ("LUM-MES-MIB", "mesMiscSfpPortUsageNext"))
)
if mibBuilder.loadTexts:
    mesMiscGroupV7.setStatus("current")

mesCfmMepGroupV3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 1, 1, 71)
)
mesCfmMepGroupV3.setObjects(
      *(("LUM-MES-MIB", "mesCfmMepIndex"),
        ("LUM-MES-MIB", "mesCfmMepName"),
        ("LUM-MES-MIB", "mesCfmMepMaid"),
        ("LUM-MES-MIB", "mesCfmMepTxPort"),
        ("LUM-MES-MIB", "mesCfmMepPortName"),
        ("LUM-MES-MIB", "mesCfmMepPrimaryVid"),
        ("LUM-MES-MIB", "mesCfmMepAdminStatus"),
        ("LUM-MES-MIB", "mesCfmMepOperStatus"),
        ("LUM-MES-MIB", "mesCfmMepVlanPriority"),
        ("LUM-MES-MIB", "mesCfmMepType"),
        ("LUM-MES-MIB", "mesCfmMepIdentifier"),
        ("LUM-MES-MIB", "mesCfmMepInternalReference"),
        ("LUM-MES-MIB", "mesCfmMepRDICCM"),
        ("LUM-MES-MIB", "mesCfmMepMACstatus"),
        ("LUM-MES-MIB", "mesCfmMepRemoteCCM"),
        ("LUM-MES-MIB", "mesCfmMepErrorCCM"),
        ("LUM-MES-MIB", "mesCfmMepXconCCM"),
        ("LUM-MES-MIB", "mesCfmMepAis"),
        ("LUM-MES-MIB", "mesCfmMepChangePort"),
        ("LUM-MES-MIB", "mesCfmMepTransmitLbrStatus"),
        ("LUM-MES-MIB", "mesCfmMepRowStatus"),
        ("LUM-MES-MIB", "mesCfmMepDirection"),
        ("LUM-MES-MIB", "mesCfmMepCcmSeqNumStatus"))
)
if mibBuilder.loadTexts:
    mesCfmMepGroupV3.setStatus("current")

mesMaidGroupV3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 1, 1, 72)
)
mesMaidGroupV3.setObjects(
      *(("LUM-MES-MIB", "mesMaidIndex"),
        ("LUM-MES-MIB", "mesMaidName"),
        ("LUM-MES-MIB", "mesMaidGroupId"),
        ("LUM-MES-MIB", "mesMaidMdFormat"),
        ("LUM-MES-MIB", "mesMaidMdName"),
        ("LUM-MES-MIB", "mesMaidMdMac"),
        ("LUM-MES-MIB", "mesMaidMd2Octet"),
        ("LUM-MES-MIB", "mesMaidMdString"),
        ("LUM-MES-MIB", "mesMaidLevel"),
        ("LUM-MES-MIB", "mesMaidMaFormat"),
        ("LUM-MES-MIB", "mesMaidMaName"),
        ("LUM-MES-MIB", "mesMaidMaVpnOui"),
        ("LUM-MES-MIB", "mesMaidMaVpnIndex"),
        ("LUM-MES-MIB", "mesMaidMa2Octet"),
        ("LUM-MES-MIB", "mesMaidMaVlan"),
        ("LUM-MES-MIB", "mesMaidMaString"),
        ("LUM-MES-MIB", "mesMaidCcmInterval"),
        ("LUM-MES-MIB", "mesMaidInternalReference"),
        ("LUM-MES-MIB", "mesMaidIdentifier"),
        ("LUM-MES-MIB", "mesMaidNoOfMeps"),
        ("LUM-MES-MIB", "mesMaidAssociateMep"),
        ("LUM-MES-MIB", "mesMaidReleaseMeps"),
        ("LUM-MES-MIB", "mesMaidRowStatus"),
        ("LUM-MES-MIB", "mesMaidNoOfUpMeps"))
)
if mibBuilder.loadTexts:
    mesMaidGroupV3.setStatus("deprecated")

mesMgmtVlanGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 1, 1, 73)
)
mesMgmtVlanGroupV2.setObjects(
      *(("LUM-MES-MIB", "mesMgmtVlanIndex"),
        ("LUM-MES-MIB", "mesMgmtVlanName"),
        ("LUM-MES-MIB", "mesMgmtVlanDescr"),
        ("LUM-MES-MIB", "mesMgmtVlanSubrack"),
        ("LUM-MES-MIB", "mesMgmtVlanSlot"),
        ("LUM-MES-MIB", "mesMgmtVlanTxPort"),
        ("LUM-MES-MIB", "mesMgmtVlanRxPort"),
        ("LUM-MES-MIB", "mesMgmtVlanObjectProperty"),
        ("LUM-MES-MIB", "mesMgmtVlanAdminStatus"),
        ("LUM-MES-MIB", "mesMgmtVlanConfigure"),
        ("LUM-MES-MIB", "mesMgmtVlanTagType"),
        ("LUM-MES-MIB", "mesMgmtVlanEtherType"),
        ("LUM-MES-MIB", "mesMgmtVlanVlanId"),
        ("LUM-MES-MIB", "mesMgmtVlanPriority"),
        ("LUM-MES-MIB", "mesMgmtVlanMacInMac"),
        ("LUM-MES-MIB", "mesMgmtVlanMacInMacIsid"),
        ("LUM-MES-MIB", "mesMgmtVlanMacInMacDa"),
        ("LUM-MES-MIB", "mesMgmtVlanForceMgmtVlan"))
)
if mibBuilder.loadTexts:
    mesMgmtVlanGroupV2.setStatus("deprecated")

mesErrorPropGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 1, 1, 74)
)
mesErrorPropGroup.setObjects(
      *(("LUM-MES-MIB", "mesErrorPropIndex"),
        ("LUM-MES-MIB", "mesErrorPropName"),
        ("LUM-MES-MIB", "mesErrorPropDescr"),
        ("LUM-MES-MIB", "mesErrorPropInternalReference"),
        ("LUM-MES-MIB", "mesErrorPropAdminStatus"),
        ("LUM-MES-MIB", "mesErrorPropOperStatus"),
        ("LUM-MES-MIB", "mesErrorPropState"),
        ("LUM-MES-MIB", "mesErrorPropTriggerType"),
        ("LUM-MES-MIB", "mesErrorPropTriggerObject"),
        ("LUM-MES-MIB", "mesErrorPropTriggerPortIndex"),
        ("LUM-MES-MIB", "mesErrorPropTriggerMepIndex"),
        ("LUM-MES-MIB", "mesErrorPropActionType"),
        ("LUM-MES-MIB", "mesErrorPropActionObject"),
        ("LUM-MES-MIB", "mesErrorPropActionPortIndex"),
        ("LUM-MES-MIB", "mesErrorPropActionMepIndex"),
        ("LUM-MES-MIB", "mesErrorPropHoldOffTimer"),
        ("LUM-MES-MIB", "mesErrorPropRowStatus"),
        ("LUM-MES-MIB", "mesErrorPropFault"))
)
if mibBuilder.loadTexts:
    mesErrorPropGroup.setStatus("deprecated")

mesMiscGroupV8 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 1, 1, 75)
)
mesMiscGroupV8.setObjects(
      *(("LUM-MES-MIB", "mesMiscIndex"),
        ("LUM-MES-MIB", "mesMiscName"),
        ("LUM-MES-MIB", "mesMiscObjectProperty"),
        ("LUM-MES-MIB", "mesMiscAdminStatus"),
        ("LUM-MES-MIB", "mesMiscOperStatus"),
        ("LUM-MES-MIB", "mesMiscMgmtVlanIpAddress"),
        ("LUM-MES-MIB", "mesMiscMgmtVlanNetMask"),
        ("LUM-MES-MIB", "mesMiscMgmtVlanMacAddress0"),
        ("LUM-MES-MIB", "mesMiscMgmtVlanMacAddress1"),
        ("LUM-MES-MIB", "mesMiscMgmtVlanMacAddress2"),
        ("LUM-MES-MIB", "mesMiscConfigureAddress"),
        ("LUM-MES-MIB", "mesMiscMgmtVlanNode"),
        ("LUM-MES-MIB", "mesMiscMacAgeing"),
        ("LUM-MES-MIB", "mesMiscMacGetTable"),
        ("LUM-MES-MIB", "mesMiscNoOfMegs"),
        ("LUM-MES-MIB", "mesMiscAssociateMeg"),
        ("LUM-MES-MIB", "mesMiscNoOfErps"),
        ("LUM-MES-MIB", "mesMiscAssociateErp"),
        ("LUM-MES-MIB", "mesMiscL2Mode"),
        ("LUM-MES-MIB", "mesMiscConfigureMode"),
        ("LUM-MES-MIB", "mesMiscIdentity"),
        ("LUM-MES-MIB", "mesMiscAssociateClass"),
        ("LUM-MES-MIB", "mesMiscAssociateBwp"),
        ("LUM-MES-MIB", "mesMiscWred"),
        ("LUM-MES-MIB", "mesMiscGetPacketMonitor"),
        ("LUM-MES-MIB", "mesMiscSfpPortUsageCurrent"),
        ("LUM-MES-MIB", "mesMiscSfpPortUsageNext"),
        ("LUM-MES-MIB", "mesMiscAssociateErrorProp"))
)
if mibBuilder.loadTexts:
    mesMiscGroupV8.setStatus("deprecated")

mesGeneralGroupV5 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 1, 1, 76)
)
mesGeneralGroupV5.setObjects(
      *(("LUM-MES-MIB", "mesGeneralConfigLastChangeTime"),
        ("LUM-MES-MIB", "mesGeneralStateLastChangeTime"),
        ("LUM-MES-MIB", "mesGeneralUniTableSize"),
        ("LUM-MES-MIB", "mesGeneralNniTableSize"),
        ("LUM-MES-MIB", "mesGeneralEvcTableSize"),
        ("LUM-MES-MIB", "mesGeneralBwpTableSize"),
        ("LUM-MES-MIB", "mesGeneralCeEvcMapTableSize"),
        ("LUM-MES-MIB", "mesGeneralMepTableSize"),
        ("LUM-MES-MIB", "mesGeneralMegTableSize"),
        ("LUM-MES-MIB", "mesGeneralEvcBwpMapTableSize"),
        ("LUM-MES-MIB", "mesGeneralPortTableSize"),
        ("LUM-MES-MIB", "mesGeneralVlanMapTableSize"),
        ("LUM-MES-MIB", "mesGeneralMgmtVlanTableSize"),
        ("LUM-MES-MIB", "mesGeneralLagTableSize"),
        ("LUM-MES-MIB", "mesGeneralPolicingTableSize"),
        ("LUM-MES-MIB", "mesGeneralShapingTableSize"),
        ("LUM-MES-MIB", "mesGeneralBwpMapTableSize"),
        ("LUM-MES-MIB", "mesGeneralCosTableSize"),
        ("LUM-MES-MIB", "mesGeneralErrorPropTableSize"))
)
if mibBuilder.loadTexts:
    mesGeneralGroupV5.setStatus("deprecated")

mesCfmMepGroupV4 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 1, 1, 77)
)
mesCfmMepGroupV4.setObjects(
      *(("LUM-MES-MIB", "mesCfmMepIndex"),
        ("LUM-MES-MIB", "mesCfmMepName"),
        ("LUM-MES-MIB", "mesCfmMepMaid"),
        ("LUM-MES-MIB", "mesCfmMepTxPort"),
        ("LUM-MES-MIB", "mesCfmMepPortName"),
        ("LUM-MES-MIB", "mesCfmMepPrimaryVid"),
        ("LUM-MES-MIB", "mesCfmMepAdminStatus"),
        ("LUM-MES-MIB", "mesCfmMepOperStatus"),
        ("LUM-MES-MIB", "mesCfmMepVlanPriority"),
        ("LUM-MES-MIB", "mesCfmMepType"),
        ("LUM-MES-MIB", "mesCfmMepIdentifier"),
        ("LUM-MES-MIB", "mesCfmMepInternalReference"),
        ("LUM-MES-MIB", "mesCfmMepRDICCM"),
        ("LUM-MES-MIB", "mesCfmMepMACstatus"),
        ("LUM-MES-MIB", "mesCfmMepRemoteCCM"),
        ("LUM-MES-MIB", "mesCfmMepErrorCCM"),
        ("LUM-MES-MIB", "mesCfmMepXconCCM"),
        ("LUM-MES-MIB", "mesCfmMepAis"),
        ("LUM-MES-MIB", "mesCfmMepChangePort"),
        ("LUM-MES-MIB", "mesCfmMepTransmitLbrStatus"),
        ("LUM-MES-MIB", "mesCfmMepRowStatus"),
        ("LUM-MES-MIB", "mesCfmMepDirection"),
        ("LUM-MES-MIB", "mesCfmMepCcmSeqNumStatus"),
        ("LUM-MES-MIB", "mesCfmMepRemoteCsfLos"),
        ("LUM-MES-MIB", "mesCfmMepRemoteCsfRdi"),
        ("LUM-MES-MIB", "mesCfmMepRemoteCsfFdi"),
        ("LUM-MES-MIB", "mesCfmMepLocalCsfLos"),
        ("LUM-MES-MIB", "mesCfmMepLocalDeviceType"),
        ("LUM-MES-MIB", "mesCfmMepLocalDeviceName"),
        ("LUM-MES-MIB", "mesCfmMepLocalDeviceId"),
        ("LUM-MES-MIB", "mesCfmMepViewFilter"),
        ("LUM-MES-MIB", "mesCfmMepUnexpectedPeriod"),
        ("LUM-MES-MIB", "mesCfmMepUnexpectedMepId"),
        ("LUM-MES-MIB", "mesCfmMepUnexpectedMegLevel"),
        ("LUM-MES-MIB", "mesCfmMepMismerge"))
)
if mibBuilder.loadTexts:
    mesCfmMepGroupV4.setStatus("current")

mesMaidGroupV4 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 1, 1, 78)
)
mesMaidGroupV4.setObjects(
      *(("LUM-MES-MIB", "mesMaidIndex"),
        ("LUM-MES-MIB", "mesMaidName"),
        ("LUM-MES-MIB", "mesMaidGroupId"),
        ("LUM-MES-MIB", "mesMaidMdFormat"),
        ("LUM-MES-MIB", "mesMaidMdName"),
        ("LUM-MES-MIB", "mesMaidMdMac"),
        ("LUM-MES-MIB", "mesMaidMd2Octet"),
        ("LUM-MES-MIB", "mesMaidMdString"),
        ("LUM-MES-MIB", "mesMaidLevel"),
        ("LUM-MES-MIB", "mesMaidMaFormat"),
        ("LUM-MES-MIB", "mesMaidMaName"),
        ("LUM-MES-MIB", "mesMaidMaVpnOui"),
        ("LUM-MES-MIB", "mesMaidMaVpnIndex"),
        ("LUM-MES-MIB", "mesMaidMa2Octet"),
        ("LUM-MES-MIB", "mesMaidMaVlan"),
        ("LUM-MES-MIB", "mesMaidMaString"),
        ("LUM-MES-MIB", "mesMaidCcmInterval"),
        ("LUM-MES-MIB", "mesMaidInternalReference"),
        ("LUM-MES-MIB", "mesMaidIdentifier"),
        ("LUM-MES-MIB", "mesMaidNoOfMeps"),
        ("LUM-MES-MIB", "mesMaidAssociateMep"),
        ("LUM-MES-MIB", "mesMaidReleaseMeps"),
        ("LUM-MES-MIB", "mesMaidRowStatus"),
        ("LUM-MES-MIB", "mesMaidNoOfUpMeps"),
        ("LUM-MES-MIB", "mesMaidNoOfNidMeps"),
        ("LUM-MES-MIB", "mesMaidLocalDeviceType"),
        ("LUM-MES-MIB", "mesMaidViewFilter"))
)
if mibBuilder.loadTexts:
    mesMaidGroupV4.setStatus("deprecated")

mesMiscGroupV9 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 1, 1, 79)
)
mesMiscGroupV9.setObjects(
      *(("LUM-MES-MIB", "mesMiscIndex"),
        ("LUM-MES-MIB", "mesMiscName"),
        ("LUM-MES-MIB", "mesMiscObjectProperty"),
        ("LUM-MES-MIB", "mesMiscAdminStatus"),
        ("LUM-MES-MIB", "mesMiscOperStatus"),
        ("LUM-MES-MIB", "mesMiscMgmtVlanIpAddress"),
        ("LUM-MES-MIB", "mesMiscMgmtVlanNetMask"),
        ("LUM-MES-MIB", "mesMiscMgmtVlanMacAddress0"),
        ("LUM-MES-MIB", "mesMiscMgmtVlanMacAddress1"),
        ("LUM-MES-MIB", "mesMiscMgmtVlanMacAddress2"),
        ("LUM-MES-MIB", "mesMiscConfigureAddress"),
        ("LUM-MES-MIB", "mesMiscMgmtVlanNode"),
        ("LUM-MES-MIB", "mesMiscMacAgeing"),
        ("LUM-MES-MIB", "mesMiscMacGetTable"),
        ("LUM-MES-MIB", "mesMiscNoOfMegs"),
        ("LUM-MES-MIB", "mesMiscAssociateMeg"),
        ("LUM-MES-MIB", "mesMiscNoOfErps"),
        ("LUM-MES-MIB", "mesMiscAssociateErp"),
        ("LUM-MES-MIB", "mesMiscL2Mode"),
        ("LUM-MES-MIB", "mesMiscConfigureMode"),
        ("LUM-MES-MIB", "mesMiscIdentity"),
        ("LUM-MES-MIB", "mesMiscAssociateClass"),
        ("LUM-MES-MIB", "mesMiscAssociateBwp"),
        ("LUM-MES-MIB", "mesMiscWred"),
        ("LUM-MES-MIB", "mesMiscGetPacketMonitor"),
        ("LUM-MES-MIB", "mesMiscSfpPortUsageCurrent"),
        ("LUM-MES-MIB", "mesMiscSfpPortUsageNext"),
        ("LUM-MES-MIB", "mesMiscNoOfErpV2s"),
        ("LUM-MES-MIB", "mesMiscAssociateErpV2"),
        ("LUM-MES-MIB", "mesMiscAssociateVlanProt"))
)
if mibBuilder.loadTexts:
    mesMiscGroupV9.setStatus("deprecated")

mesErpGroupV3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 1, 1, 80)
)
mesErpGroupV3.setObjects(
      *(("LUM-MES-MIB", "mesErpIndex"),
        ("LUM-MES-MIB", "mesErpName"),
        ("LUM-MES-MIB", "mesErpPortLeft"),
        ("LUM-MES-MIB", "mesErpPortRight"),
        ("LUM-MES-MIB", "mesErpAdminStatus"),
        ("LUM-MES-MIB", "mesErpInternalReference"),
        ("LUM-MES-MIB", "mesErpDescr"),
        ("LUM-MES-MIB", "mesErpVlanId"),
        ("LUM-MES-MIB", "mesErpMegLevel"),
        ("LUM-MES-MIB", "mesErpProtLink"),
        ("LUM-MES-MIB", "mesErpGuardTime"),
        ("LUM-MES-MIB", "mesErpHoldOffTime"),
        ("LUM-MES-MIB", "mesErpWtrTime"),
        ("LUM-MES-MIB", "mesErpOamDetectionLeft"),
        ("LUM-MES-MIB", "mesErpOamDetectionRight"),
        ("LUM-MES-MIB", "mesErpStatusLeft"),
        ("LUM-MES-MIB", "mesErpStatusRight"),
        ("LUM-MES-MIB", "mesErpProtState"),
        ("LUM-MES-MIB", "mesErpActiveEvent"),
        ("LUM-MES-MIB", "mesErpRapsReqState"),
        ("LUM-MES-MIB", "mesErpServiceFailure"),
        ("LUM-MES-MIB", "mesErpServiceDegraded"),
        ("LUM-MES-MIB", "mesErpUnexpectedMegLevel"),
        ("LUM-MES-MIB", "mesErpCommunicationFailure"),
        ("LUM-MES-MIB", "mesErpChangePort"),
        ("LUM-MES-MIB", "mesErpRowStatus"),
        ("LUM-MES-MIB", "mesErpNodeType"),
        ("LUM-MES-MIB", "mesErpProtectionMode"),
        ("LUM-MES-MIB", "mesErpVersion"),
        ("LUM-MES-MIB", "mesErpMajorName"),
        ("LUM-MES-MIB", "mesErpRingId"),
        ("LUM-MES-MIB", "mesErpRingIndex"),
        ("LUM-MES-MIB", "mesErpOperatorCommand"),
        ("LUM-MES-MIB", "mesErpGroupId"),
        ("LUM-MES-MIB", "mesErpSwitchInformation"),
        ("LUM-MES-MIB", "mesErpTopologyChangePropagation"),
        ("LUM-MES-MIB", "mesErpSubRings"))
)
if mibBuilder.loadTexts:
    mesErpGroupV3.setStatus("deprecated")

mesVlanProtV1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 1, 1, 81)
)
mesVlanProtV1.setObjects(
      *(("LUM-MES-MIB", "mesVlanProtIndex"),
        ("LUM-MES-MIB", "mesVlanProtName"),
        ("LUM-MES-MIB", "mesVlanProtInternalReference"),
        ("LUM-MES-MIB", "mesVlanProtRings"),
        ("LUM-MES-MIB", "mesVlanProtProtectedVlan"),
        ("LUM-MES-MIB", "mesVlanProtGroupId"),
        ("LUM-MES-MIB", "mesVlanProtAddRingAction"),
        ("LUM-MES-MIB", "mesVlanProtRemoveRingAction"),
        ("LUM-MES-MIB", "mesVlanProtDescr"),
        ("LUM-MES-MIB", "mesVlanProtChangeVlansAction"))
)
if mibBuilder.loadTexts:
    mesVlanProtV1.setStatus("current")

mesCfmMepGroupV5 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 1, 1, 82)
)
mesCfmMepGroupV5.setObjects(
      *(("LUM-MES-MIB", "mesCfmMepIndex"),
        ("LUM-MES-MIB", "mesCfmMepName"),
        ("LUM-MES-MIB", "mesCfmMepMaid"),
        ("LUM-MES-MIB", "mesCfmMepTxPort"),
        ("LUM-MES-MIB", "mesCfmMepPortName"),
        ("LUM-MES-MIB", "mesCfmMepPrimaryVid"),
        ("LUM-MES-MIB", "mesCfmMepAdminStatus"),
        ("LUM-MES-MIB", "mesCfmMepOperStatus"),
        ("LUM-MES-MIB", "mesCfmMepVlanPriority"),
        ("LUM-MES-MIB", "mesCfmMepType"),
        ("LUM-MES-MIB", "mesCfmMepIdentifier"),
        ("LUM-MES-MIB", "mesCfmMepInternalReference"),
        ("LUM-MES-MIB", "mesCfmMepRDICCM"),
        ("LUM-MES-MIB", "mesCfmMepMACstatus"),
        ("LUM-MES-MIB", "mesCfmMepRemoteCCM"),
        ("LUM-MES-MIB", "mesCfmMepErrorCCM"),
        ("LUM-MES-MIB", "mesCfmMepXconCCM"),
        ("LUM-MES-MIB", "mesCfmMepAis"),
        ("LUM-MES-MIB", "mesCfmMepChangePort"),
        ("LUM-MES-MIB", "mesCfmMepTransmitLbrStatus"),
        ("LUM-MES-MIB", "mesCfmMepRowStatus"),
        ("LUM-MES-MIB", "mesCfmMepDirection"),
        ("LUM-MES-MIB", "mesCfmMepCcmSeqNumStatus"),
        ("LUM-MES-MIB", "mesCfmMepRemoteCsfLos"),
        ("LUM-MES-MIB", "mesCfmMepRemoteCsfRdi"),
        ("LUM-MES-MIB", "mesCfmMepRemoteCsfFdi"),
        ("LUM-MES-MIB", "mesCfmMepLocalCsfLos"),
        ("LUM-MES-MIB", "mesCfmMepLocalDeviceType"),
        ("LUM-MES-MIB", "mesCfmMepLocalDeviceName"),
        ("LUM-MES-MIB", "mesCfmMepLocalDeviceId"),
        ("LUM-MES-MIB", "mesCfmMepViewFilter"),
        ("LUM-MES-MIB", "mesCfmMepUnexpectedPeriod"),
        ("LUM-MES-MIB", "mesCfmMepUnexpectedMepId"),
        ("LUM-MES-MIB", "mesCfmMepUnexpectedMegLevel"),
        ("LUM-MES-MIB", "mesCfmMepMismerge"),
        ("LUM-MES-MIB", "mesCfmMepNoOfLMs"),
        ("LUM-MES-MIB", "mesCfmMepNoOfDMs"))
)
if mibBuilder.loadTexts:
    mesCfmMepGroupV5.setStatus("current")

mesVlanMapGroupV6 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 1, 1, 83)
)
mesVlanMapGroupV6.setObjects(
      *(("LUM-MES-MIB", "mesVlanMapIndex"),
        ("LUM-MES-MIB", "mesVlanMapName"),
        ("LUM-MES-MIB", "mesVlanMapVlanIdRangeLower"),
        ("LUM-MES-MIB", "mesVlanMapVlanIdRangeUpper"),
        ("LUM-MES-MIB", "mesVlanMapInternalReference"),
        ("LUM-MES-MIB", "mesVlanMapPortmask"),
        ("LUM-MES-MIB", "mesVlanMapConfigurePortMask"),
        ("LUM-MES-MIB", "mesVlanMapLearning"),
        ("LUM-MES-MIB", "mesVlanMapEtherType"),
        ("LUM-MES-MIB", "mesVlanMapRowStatus"),
        ("LUM-MES-MIB", "mesVlanMapDescr"),
        ("LUM-MES-MIB", "mesVlanMapTrustPorts"),
        ("LUM-MES-MIB", "mesVlanMapRings"))
)
if mibBuilder.loadTexts:
    mesVlanMapGroupV6.setStatus("deprecated")

mesClassGroupV3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 1, 1, 84)
)
mesClassGroupV3.setObjects(
      *(("LUM-MES-MIB", "mesClassIndex"),
        ("LUM-MES-MIB", "mesClassName"),
        ("LUM-MES-MIB", "mesClassIdentifier"),
        ("LUM-MES-MIB", "mesClassPort"),
        ("LUM-MES-MIB", "mesClassLagId"),
        ("LUM-MES-MIB", "mesClassInternalReference"),
        ("LUM-MES-MIB", "mesClassOuterVlanId"),
        ("LUM-MES-MIB", "mesClassOuterVlanPcp"),
        ("LUM-MES-MIB", "mesClassPrecedence"),
        ("LUM-MES-MIB", "mesClassDaMacAddress"),
        ("LUM-MES-MIB", "mesClassAssociateAction"),
        ("LUM-MES-MIB", "mesClassRowStatus"),
        ("LUM-MES-MIB", "mesClassDaMacAddressMask"),
        ("LUM-MES-MIB", "mesClassDSCP"),
        ("LUM-MES-MIB", "mesClassInnerVlanId"),
        ("LUM-MES-MIB", "mesClassInnerVlanPcp"),
        ("LUM-MES-MIB", "mesClassInnerVlanCfi"),
        ("LUM-MES-MIB", "mesClassOuterVlanCfi"),
        ("LUM-MES-MIB", "mesClassDirection"),
        ("LUM-MES-MIB", "mesClassOuterTpid"),
        ("LUM-MES-MIB", "mesClassInternalClassId"))
)
if mibBuilder.loadTexts:
    mesClassGroupV3.setStatus("deprecated")

mesMgmtVlanGroupV3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 1, 1, 85)
)
mesMgmtVlanGroupV3.setObjects(
      *(("LUM-MES-MIB", "mesMgmtVlanIndex"),
        ("LUM-MES-MIB", "mesMgmtVlanName"),
        ("LUM-MES-MIB", "mesMgmtVlanDescr"),
        ("LUM-MES-MIB", "mesMgmtVlanSubrack"),
        ("LUM-MES-MIB", "mesMgmtVlanSlot"),
        ("LUM-MES-MIB", "mesMgmtVlanTxPort"),
        ("LUM-MES-MIB", "mesMgmtVlanRxPort"),
        ("LUM-MES-MIB", "mesMgmtVlanObjectProperty"),
        ("LUM-MES-MIB", "mesMgmtVlanAdminStatus"),
        ("LUM-MES-MIB", "mesMgmtVlanConfigure"),
        ("LUM-MES-MIB", "mesMgmtVlanTagType"),
        ("LUM-MES-MIB", "mesMgmtVlanEtherType"),
        ("LUM-MES-MIB", "mesMgmtVlanVlanId"),
        ("LUM-MES-MIB", "mesMgmtVlanPriority"),
        ("LUM-MES-MIB", "mesMgmtVlanMacInMac"),
        ("LUM-MES-MIB", "mesMgmtVlanMacInMacIsid"),
        ("LUM-MES-MIB", "mesMgmtVlanMacInMacDa"),
        ("LUM-MES-MIB", "mesMgmtVlanForceMgmtVlan"),
        ("LUM-MES-MIB", "mesMgmtVlanRings"))
)
if mibBuilder.loadTexts:
    mesMgmtVlanGroupV3.setStatus("deprecated")

mesClassGroupV4 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 1, 1, 86)
)
mesClassGroupV4.setObjects(
      *(("LUM-MES-MIB", "mesClassIndex"),
        ("LUM-MES-MIB", "mesClassName"),
        ("LUM-MES-MIB", "mesClassIdentifier"),
        ("LUM-MES-MIB", "mesClassPort"),
        ("LUM-MES-MIB", "mesClassLagId"),
        ("LUM-MES-MIB", "mesClassInternalReference"),
        ("LUM-MES-MIB", "mesClassOuterVlanId"),
        ("LUM-MES-MIB", "mesClassOuterVlanPcp"),
        ("LUM-MES-MIB", "mesClassPrecedence"),
        ("LUM-MES-MIB", "mesClassDaMacAddress"),
        ("LUM-MES-MIB", "mesClassAssociateAction"),
        ("LUM-MES-MIB", "mesClassRowStatus"),
        ("LUM-MES-MIB", "mesClassDaMacAddressMask"),
        ("LUM-MES-MIB", "mesClassDSCP"),
        ("LUM-MES-MIB", "mesClassInnerVlanId"),
        ("LUM-MES-MIB", "mesClassInnerVlanPcp"),
        ("LUM-MES-MIB", "mesClassInnerVlanCfi"),
        ("LUM-MES-MIB", "mesClassOuterVlanCfi"),
        ("LUM-MES-MIB", "mesClassDirection"),
        ("LUM-MES-MIB", "mesClassOuterTpid"),
        ("LUM-MES-MIB", "mesClassInternalClassId"),
        ("LUM-MES-MIB", "mesClassSourceAddressIPV4"),
        ("LUM-MES-MIB", "mesClassSourceMaskIPV4"),
        ("LUM-MES-MIB", "mesClassDestAddressIPV4"),
        ("LUM-MES-MIB", "mesClassDestMaskIPV4"),
        ("LUM-MES-MIB", "mesClassSubrack"),
        ("LUM-MES-MIB", "mesClassSlot"),
        ("LUM-MES-MIB", "mesClassVlanStackStructure"),
        ("LUM-MES-MIB", "mesClassServiceId"))
)
if mibBuilder.loadTexts:
    mesClassGroupV4.setStatus("deprecated")

mesActionGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 1, 1, 87)
)
mesActionGroupV2.setObjects(
      *(("LUM-MES-MIB", "mesActionIndex"),
        ("LUM-MES-MIB", "mesActionName"),
        ("LUM-MES-MIB", "mesActionIdentifier"),
        ("LUM-MES-MIB", "mesActionInternalReference"),
        ("LUM-MES-MIB", "mesActionType"),
        ("LUM-MES-MIB", "mesActionOuterVlanId"),
        ("LUM-MES-MIB", "mesActionPcp"),
        ("LUM-MES-MIB", "mesActionPolicerId"),
        ("LUM-MES-MIB", "mesActionInnerVlanId"),
        ("LUM-MES-MIB", "mesActionQueue"),
        ("LUM-MES-MIB", "mesActionRowStatus"),
        ("LUM-MES-MIB", "mesActionRedirectPort"),
        ("LUM-MES-MIB", "mesActionServiceId"))
)
if mibBuilder.loadTexts:
    mesActionGroupV2.setStatus("deprecated")

mesCfmMepGroupV6 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 1, 1, 88)
)
mesCfmMepGroupV6.setObjects(
      *(("LUM-MES-MIB", "mesCfmMepIndex"),
        ("LUM-MES-MIB", "mesCfmMepName"),
        ("LUM-MES-MIB", "mesCfmMepMaid"),
        ("LUM-MES-MIB", "mesCfmMepTxPort"),
        ("LUM-MES-MIB", "mesCfmMepPortName"),
        ("LUM-MES-MIB", "mesCfmMepPrimaryVid"),
        ("LUM-MES-MIB", "mesCfmMepAdminStatus"),
        ("LUM-MES-MIB", "mesCfmMepOperStatus"),
        ("LUM-MES-MIB", "mesCfmMepVlanPriority"),
        ("LUM-MES-MIB", "mesCfmMepType"),
        ("LUM-MES-MIB", "mesCfmMepIdentifier"),
        ("LUM-MES-MIB", "mesCfmMepInternalReference"),
        ("LUM-MES-MIB", "mesCfmMepRDICCM"),
        ("LUM-MES-MIB", "mesCfmMepMACstatus"),
        ("LUM-MES-MIB", "mesCfmMepRemoteCCM"),
        ("LUM-MES-MIB", "mesCfmMepErrorCCM"),
        ("LUM-MES-MIB", "mesCfmMepXconCCM"),
        ("LUM-MES-MIB", "mesCfmMepAis"),
        ("LUM-MES-MIB", "mesCfmMepChangePort"),
        ("LUM-MES-MIB", "mesCfmMepTransmitLbrStatus"),
        ("LUM-MES-MIB", "mesCfmMepRowStatus"),
        ("LUM-MES-MIB", "mesCfmMepDirection"),
        ("LUM-MES-MIB", "mesCfmMepCcmSeqNumStatus"),
        ("LUM-MES-MIB", "mesCfmMepRemoteCsfLos"),
        ("LUM-MES-MIB", "mesCfmMepRemoteCsfRdi"),
        ("LUM-MES-MIB", "mesCfmMepRemoteCsfFdi"),
        ("LUM-MES-MIB", "mesCfmMepLocalCsfLos"),
        ("LUM-MES-MIB", "mesCfmMepLocalDeviceType"),
        ("LUM-MES-MIB", "mesCfmMepLocalDeviceName"),
        ("LUM-MES-MIB", "mesCfmMepLocalDeviceId"),
        ("LUM-MES-MIB", "mesCfmMepViewFilter"),
        ("LUM-MES-MIB", "mesCfmMepUnexpectedPeriod"),
        ("LUM-MES-MIB", "mesCfmMepUnexpectedMepId"),
        ("LUM-MES-MIB", "mesCfmMepUnexpectedMegLevel"),
        ("LUM-MES-MIB", "mesCfmMepMismerge"),
        ("LUM-MES-MIB", "mesCfmMepNoOfLMs"),
        ("LUM-MES-MIB", "mesCfmMepNoOfDMs"),
        ("LUM-MES-MIB", "mesCfmMepTransmitDmrStatus"),
        ("LUM-MES-MIB", "mesCfmMepTransmitLmrStatus"),
        ("LUM-MES-MIB", "mesCfmMepLmCosAwareness"))
)
if mibBuilder.loadTexts:
    mesCfmMepGroupV6.setStatus("deprecated")

mesLacpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 1, 1, 89)
)
mesLacpGroup.setObjects(
      *(("LUM-MES-MIB", "mesLacpIndex"),
        ("LUM-MES-MIB", "mesLacpName"),
        ("LUM-MES-MIB", "mesLacpInternalReference"),
        ("LUM-MES-MIB", "mesLacpLagIdentifier"),
        ("LUM-MES-MIB", "mesLacpLagId"),
        ("LUM-MES-MIB", "mesLacpPortPriority"),
        ("LUM-MES-MIB", "mesLacpSelected"),
        ("LUM-MES-MIB", "mesLacpReceiveState"),
        ("LUM-MES-MIB", "mesLacpTransmitState"),
        ("LUM-MES-MIB", "mesLacpMuxState"),
        ("LUM-MES-MIB", "mesLacpActorExpired"),
        ("LUM-MES-MIB", "mesLacpActorDefault"),
        ("LUM-MES-MIB", "mesLacpActorDistributing"),
        ("LUM-MES-MIB", "mesLacpActorCollecting"),
        ("LUM-MES-MIB", "mesLacpActorSynchronization"),
        ("LUM-MES-MIB", "mesLacpActorAggregation"),
        ("LUM-MES-MIB", "mesLacpActorTimeout"),
        ("LUM-MES-MIB", "mesLacpActorActivity"),
        ("LUM-MES-MIB", "mesLacpPartnerExpired"),
        ("LUM-MES-MIB", "mesLacpPartnerDefault"),
        ("LUM-MES-MIB", "mesLacpPartnerDistributing"),
        ("LUM-MES-MIB", "mesLacpPartnerCollecting"),
        ("LUM-MES-MIB", "mesLacpPartnerSynchronization"),
        ("LUM-MES-MIB", "mesLacpPartnerAggregation"),
        ("LUM-MES-MIB", "mesLacpPartnerTimeout"),
        ("LUM-MES-MIB", "mesLacpPartnerActivity"),
        ("LUM-MES-MIB", "mesLacpTxLacpPdus"),
        ("LUM-MES-MIB", "mesLacpRxLacpPdus"),
        ("LUM-MES-MIB", "mesLacpInternalIndex"),
        ("LUM-MES-MIB", "mesLacpResetCounters"))
)
if mibBuilder.loadTexts:
    mesLacpGroup.setStatus("deprecated")

mesVlanMapGroupV7 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 1, 1, 90)
)
mesVlanMapGroupV7.setObjects(
      *(("LUM-MES-MIB", "mesVlanMapIndex"),
        ("LUM-MES-MIB", "mesVlanMapName"),
        ("LUM-MES-MIB", "mesVlanMapVlanIdRangeLower"),
        ("LUM-MES-MIB", "mesVlanMapVlanIdRangeUpper"),
        ("LUM-MES-MIB", "mesVlanMapInternalReference"),
        ("LUM-MES-MIB", "mesVlanMapPortmask"),
        ("LUM-MES-MIB", "mesVlanMapConfigurePortMask"),
        ("LUM-MES-MIB", "mesVlanMapLearning"),
        ("LUM-MES-MIB", "mesVlanMapEtherType"),
        ("LUM-MES-MIB", "mesVlanMapRowStatus"),
        ("LUM-MES-MIB", "mesVlanMapDescr"),
        ("LUM-MES-MIB", "mesVlanMapTrustPorts"),
        ("LUM-MES-MIB", "mesVlanMapRings"),
        ("LUM-MES-MIB", "mesVlanMapServiceId"))
)
if mibBuilder.loadTexts:
    mesVlanMapGroupV7.setStatus("deprecated")

mesPolicyGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 1, 1, 91)
)
mesPolicyGroupV2.setObjects(
      *(("LUM-MES-MIB", "mesPolicyIndex"),
        ("LUM-MES-MIB", "mesPolicyName"),
        ("LUM-MES-MIB", "mesPolicyInternalReference"),
        ("LUM-MES-MIB", "mesPolicyClass"),
        ("LUM-MES-MIB", "mesPolicyAction"),
        ("LUM-MES-MIB", "mesPolicyServiceId"))
)
if mibBuilder.loadTexts:
    mesPolicyGroupV2.setStatus("current")

mesBwpGroupV3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 1, 1, 92)
)
mesBwpGroupV3.setObjects(
      *(("LUM-MES-MIB", "mesBwpIndex"),
        ("LUM-MES-MIB", "mesBwpName"),
        ("LUM-MES-MIB", "mesBwpObjectProperty"),
        ("LUM-MES-MIB", "mesBwpCoSIdentifier"),
        ("LUM-MES-MIB", "mesBwpCir"),
        ("LUM-MES-MIB", "mesBwpCbs"),
        ("LUM-MES-MIB", "mesBwpEir"),
        ("LUM-MES-MIB", "mesBwpEbs"),
        ("LUM-MES-MIB", "mesBwpCouplingFlag"),
        ("LUM-MES-MIB", "mesBwpColorMode"),
        ("LUM-MES-MIB", "mesBwpInternalReference"),
        ("LUM-MES-MIB", "mesBwpRowStatus"),
        ("LUM-MES-MIB", "mesBwpServiceId"))
)
if mibBuilder.loadTexts:
    mesBwpGroupV3.setStatus("deprecated")

mesLagGroupV4 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 1, 1, 93)
)
mesLagGroupV4.setObjects(
      *(("LUM-MES-MIB", "mesLagIndex"),
        ("LUM-MES-MIB", "mesLagName"),
        ("LUM-MES-MIB", "mesLagInternalReference"),
        ("LUM-MES-MIB", "mesLagPortmask"),
        ("LUM-MES-MIB", "mesLagMasterIndex"),
        ("LUM-MES-MIB", "mesLagConfigure"),
        ("LUM-MES-MIB", "mesLagHash"),
        ("LUM-MES-MIB", "mesLagIdentifier"),
        ("LUM-MES-MIB", "mesLagRowStatus"),
        ("LUM-MES-MIB", "mesLagLacpEnabled"),
        ("LUM-MES-MIB", "mesLagLacpSystemPriority"),
        ("LUM-MES-MIB", "mesLagLacpPeriod"),
        ("LUM-MES-MIB", "mesLagDegraded"),
        ("LUM-MES-MIB", "mesLagFailure"))
)
if mibBuilder.loadTexts:
    mesLagGroupV4.setStatus("deprecated")

mesLagGroupV5 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 1, 1, 94)
)
mesLagGroupV5.setObjects(
      *(("LUM-MES-MIB", "mesLagIndex"),
        ("LUM-MES-MIB", "mesLagName"),
        ("LUM-MES-MIB", "mesLagInternalReference"),
        ("LUM-MES-MIB", "mesLagPortmask"),
        ("LUM-MES-MIB", "mesLagMasterIndex"),
        ("LUM-MES-MIB", "mesLagConfigure"),
        ("LUM-MES-MIB", "mesLagHash"),
        ("LUM-MES-MIB", "mesLagIdentifier"),
        ("LUM-MES-MIB", "mesLagRowStatus"),
        ("LUM-MES-MIB", "mesLagLacpEnabled"),
        ("LUM-MES-MIB", "mesLagLacpSystemPriority"),
        ("LUM-MES-MIB", "mesLagLacpPeriod"),
        ("LUM-MES-MIB", "mesLagLacpLinkProtection"),
        ("LUM-MES-MIB", "mesLagDegraded"),
        ("LUM-MES-MIB", "mesLagFailure"),
        ("LUM-MES-MIB", "mesLagLacpMaxNumberOfActiveLinks"),
        ("LUM-MES-MIB", "mesLagNoOfPorts"),
        ("LUM-MES-MIB", "mesLagLacpMinNumberOfActiveLinks"))
)
if mibBuilder.loadTexts:
    mesLagGroupV5.setStatus("deprecated")

mesCfmMepGroupV7 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 1, 1, 95)
)
mesCfmMepGroupV7.setObjects(
      *(("LUM-MES-MIB", "mesCfmMepIndex"),
        ("LUM-MES-MIB", "mesCfmMepName"),
        ("LUM-MES-MIB", "mesCfmMepMaid"),
        ("LUM-MES-MIB", "mesCfmMepTxPort"),
        ("LUM-MES-MIB", "mesCfmMepPortName"),
        ("LUM-MES-MIB", "mesCfmMepPrimaryVid"),
        ("LUM-MES-MIB", "mesCfmMepAdminStatus"),
        ("LUM-MES-MIB", "mesCfmMepOperStatus"),
        ("LUM-MES-MIB", "mesCfmMepVlanPriority"),
        ("LUM-MES-MIB", "mesCfmMepType"),
        ("LUM-MES-MIB", "mesCfmMepIdentifier"),
        ("LUM-MES-MIB", "mesCfmMepInternalReference"),
        ("LUM-MES-MIB", "mesCfmMepRDICCM"),
        ("LUM-MES-MIB", "mesCfmMepMACstatus"),
        ("LUM-MES-MIB", "mesCfmMepRemoteCCM"),
        ("LUM-MES-MIB", "mesCfmMepErrorCCM"),
        ("LUM-MES-MIB", "mesCfmMepXconCCM"),
        ("LUM-MES-MIB", "mesCfmMepAis"),
        ("LUM-MES-MIB", "mesCfmMepChangePort"),
        ("LUM-MES-MIB", "mesCfmMepTransmitLbrStatus"),
        ("LUM-MES-MIB", "mesCfmMepRowStatus"),
        ("LUM-MES-MIB", "mesCfmMepDirection"),
        ("LUM-MES-MIB", "mesCfmMepCcmSeqNumStatus"),
        ("LUM-MES-MIB", "mesCfmMepRemoteCsfLos"),
        ("LUM-MES-MIB", "mesCfmMepRemoteCsfRdi"),
        ("LUM-MES-MIB", "mesCfmMepRemoteCsfFdi"),
        ("LUM-MES-MIB", "mesCfmMepLocalCsfLos"),
        ("LUM-MES-MIB", "mesCfmMepLocalDeviceType"),
        ("LUM-MES-MIB", "mesCfmMepLocalDeviceName"),
        ("LUM-MES-MIB", "mesCfmMepLocalDeviceId"),
        ("LUM-MES-MIB", "mesCfmMepViewFilter"),
        ("LUM-MES-MIB", "mesCfmMepUnexpectedPeriod"),
        ("LUM-MES-MIB", "mesCfmMepUnexpectedMepId"),
        ("LUM-MES-MIB", "mesCfmMepUnexpectedMegLevel"),
        ("LUM-MES-MIB", "mesCfmMepMismerge"),
        ("LUM-MES-MIB", "mesCfmMepNoOfLMs"),
        ("LUM-MES-MIB", "mesCfmMepNoOfDMs"),
        ("LUM-MES-MIB", "mesCfmMepTransmitDmrStatus"),
        ("LUM-MES-MIB", "mesCfmMepTransmitLmrStatus"),
        ("LUM-MES-MIB", "mesCfmMepLmCosAwareness"),
        ("LUM-MES-MIB", "mesCfmMepResourceType"),
        ("LUM-MES-MIB", "mesCfmMepLagId"),
        ("LUM-MES-MIB", "mesCfmMepInterfaceName"))
)
if mibBuilder.loadTexts:
    mesCfmMepGroupV7.setStatus("deprecated")

mesErpGroupV4 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 1, 1, 96)
)
mesErpGroupV4.setObjects(
      *(("LUM-MES-MIB", "mesErpIndex"),
        ("LUM-MES-MIB", "mesErpName"),
        ("LUM-MES-MIB", "mesErpPortLeft"),
        ("LUM-MES-MIB", "mesErpPortRight"),
        ("LUM-MES-MIB", "mesErpAdminStatus"),
        ("LUM-MES-MIB", "mesErpInternalReference"),
        ("LUM-MES-MIB", "mesErpDescr"),
        ("LUM-MES-MIB", "mesErpVlanId"),
        ("LUM-MES-MIB", "mesErpMegLevel"),
        ("LUM-MES-MIB", "mesErpProtLink"),
        ("LUM-MES-MIB", "mesErpGuardTime"),
        ("LUM-MES-MIB", "mesErpHoldOffTime"),
        ("LUM-MES-MIB", "mesErpWtrTime"),
        ("LUM-MES-MIB", "mesErpOamDetectionLeft"),
        ("LUM-MES-MIB", "mesErpOamDetectionRight"),
        ("LUM-MES-MIB", "mesErpStatusLeft"),
        ("LUM-MES-MIB", "mesErpStatusRight"),
        ("LUM-MES-MIB", "mesErpProtState"),
        ("LUM-MES-MIB", "mesErpActiveEvent"),
        ("LUM-MES-MIB", "mesErpRapsReqState"),
        ("LUM-MES-MIB", "mesErpServiceFailure"),
        ("LUM-MES-MIB", "mesErpServiceDegraded"),
        ("LUM-MES-MIB", "mesErpUnexpectedMegLevel"),
        ("LUM-MES-MIB", "mesErpCommunicationFailure"),
        ("LUM-MES-MIB", "mesErpChangePort"),
        ("LUM-MES-MIB", "mesErpRowStatus"),
        ("LUM-MES-MIB", "mesErpNodeType"),
        ("LUM-MES-MIB", "mesErpProtectionMode"),
        ("LUM-MES-MIB", "mesErpVersion"),
        ("LUM-MES-MIB", "mesErpMajorName"),
        ("LUM-MES-MIB", "mesErpRingId"),
        ("LUM-MES-MIB", "mesErpRingIndex"),
        ("LUM-MES-MIB", "mesErpOperatorCommand"),
        ("LUM-MES-MIB", "mesErpGroupId"),
        ("LUM-MES-MIB", "mesErpSwitchInformation"),
        ("LUM-MES-MIB", "mesErpTopologyChangePropagation"),
        ("LUM-MES-MIB", "mesErpSubRings"),
        ("LUM-MES-MIB", "mesErpResourceTypeLeft"),
        ("LUM-MES-MIB", "mesErpLagIdLeft"),
        ("LUM-MES-MIB", "mesErpResourceTypeRight"),
        ("LUM-MES-MIB", "mesErpLagIdRight"),
        ("LUM-MES-MIB", "mesErpInterfaceLeft"),
        ("LUM-MES-MIB", "mesErpInterfaceRight"))
)
if mibBuilder.loadTexts:
    mesErpGroupV4.setStatus("deprecated")

mesLagGroupV6 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 1, 1, 97)
)
mesLagGroupV6.setObjects(
      *(("LUM-MES-MIB", "mesLagIndex"),
        ("LUM-MES-MIB", "mesLagName"),
        ("LUM-MES-MIB", "mesLagInternalReference"),
        ("LUM-MES-MIB", "mesLagPortmask"),
        ("LUM-MES-MIB", "mesLagMasterIndex"),
        ("LUM-MES-MIB", "mesLagConfigure"),
        ("LUM-MES-MIB", "mesLagHash"),
        ("LUM-MES-MIB", "mesLagIdentifier"),
        ("LUM-MES-MIB", "mesLagRowStatus"),
        ("LUM-MES-MIB", "mesLagLacpEnabled"),
        ("LUM-MES-MIB", "mesLagLacpSystemPriority"),
        ("LUM-MES-MIB", "mesLagLacpPeriod"),
        ("LUM-MES-MIB", "mesLagLacpLinkProtection"),
        ("LUM-MES-MIB", "mesLagDegraded"),
        ("LUM-MES-MIB", "mesLagFailure"),
        ("LUM-MES-MIB", "mesLagLacpMaxNumberOfActiveLinks"),
        ("LUM-MES-MIB", "mesLagNoOfPorts"),
        ("LUM-MES-MIB", "mesLagLacpMinNumberOfActiveLinks"),
        ("LUM-MES-MIB", "mesLagIsMcLag"))
)
if mibBuilder.loadTexts:
    mesLagGroupV6.setStatus("deprecated")

mesErpGroupV5 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 1, 1, 98)
)
mesErpGroupV5.setObjects(
      *(("LUM-MES-MIB", "mesErpIndex"),
        ("LUM-MES-MIB", "mesErpName"),
        ("LUM-MES-MIB", "mesErpPortLeft"),
        ("LUM-MES-MIB", "mesErpPortRight"),
        ("LUM-MES-MIB", "mesErpAdminStatus"),
        ("LUM-MES-MIB", "mesErpInternalReference"),
        ("LUM-MES-MIB", "mesErpDescr"),
        ("LUM-MES-MIB", "mesErpVlanId"),
        ("LUM-MES-MIB", "mesErpMegLevel"),
        ("LUM-MES-MIB", "mesErpProtLink"),
        ("LUM-MES-MIB", "mesErpGuardTime"),
        ("LUM-MES-MIB", "mesErpHoldOffTime"),
        ("LUM-MES-MIB", "mesErpWtrTime"),
        ("LUM-MES-MIB", "mesErpOamDetectionLeft"),
        ("LUM-MES-MIB", "mesErpOamDetectionRight"),
        ("LUM-MES-MIB", "mesErpStatusLeft"),
        ("LUM-MES-MIB", "mesErpStatusRight"),
        ("LUM-MES-MIB", "mesErpProtState"),
        ("LUM-MES-MIB", "mesErpActiveEvent"),
        ("LUM-MES-MIB", "mesErpRapsReqState"),
        ("LUM-MES-MIB", "mesErpServiceFailure"),
        ("LUM-MES-MIB", "mesErpServiceDegraded"),
        ("LUM-MES-MIB", "mesErpUnexpectedMegLevel"),
        ("LUM-MES-MIB", "mesErpCommunicationFailure"),
        ("LUM-MES-MIB", "mesErpProvisioningMismatch"),
        ("LUM-MES-MIB", "mesErpChangePort"),
        ("LUM-MES-MIB", "mesErpRowStatus"),
        ("LUM-MES-MIB", "mesErpNodeType"),
        ("LUM-MES-MIB", "mesErpProtectionMode"),
        ("LUM-MES-MIB", "mesErpVersion"),
        ("LUM-MES-MIB", "mesErpMajorName"),
        ("LUM-MES-MIB", "mesErpRingId"),
        ("LUM-MES-MIB", "mesErpRingIndex"),
        ("LUM-MES-MIB", "mesErpOperatorCommand"),
        ("LUM-MES-MIB", "mesErpGroupId"),
        ("LUM-MES-MIB", "mesErpSwitchInformation"),
        ("LUM-MES-MIB", "mesErpTopologyChangePropagation"),
        ("LUM-MES-MIB", "mesErpSubRings"),
        ("LUM-MES-MIB", "mesErpResourceTypeLeft"),
        ("LUM-MES-MIB", "mesErpLagIdLeft"),
        ("LUM-MES-MIB", "mesErpResourceTypeRight"),
        ("LUM-MES-MIB", "mesErpLagIdRight"),
        ("LUM-MES-MIB", "mesErpInterfaceLeft"),
        ("LUM-MES-MIB", "mesErpInterfaceRight"))
)
if mibBuilder.loadTexts:
    mesErpGroupV5.setStatus("deprecated")

mesLagGroupV7 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 1, 1, 99)
)
mesLagGroupV7.setObjects(
      *(("LUM-MES-MIB", "mesLagIndex"),
        ("LUM-MES-MIB", "mesLagName"),
        ("LUM-MES-MIB", "mesLagInternalReference"),
        ("LUM-MES-MIB", "mesLagPortmask"),
        ("LUM-MES-MIB", "mesLagMasterIndex"),
        ("LUM-MES-MIB", "mesLagConfigure"),
        ("LUM-MES-MIB", "mesLagHash"),
        ("LUM-MES-MIB", "mesLagIdentifier"),
        ("LUM-MES-MIB", "mesLagRowStatus"),
        ("LUM-MES-MIB", "mesLagLacpEnabled"),
        ("LUM-MES-MIB", "mesLagLacpSystemPriority"),
        ("LUM-MES-MIB", "mesLagLacpPeriod"),
        ("LUM-MES-MIB", "mesLagLacpLinkProtection"),
        ("LUM-MES-MIB", "mesLagDegraded"),
        ("LUM-MES-MIB", "mesLagFailure"),
        ("LUM-MES-MIB", "mesLagLacpMaxNumberOfActiveLinks"),
        ("LUM-MES-MIB", "mesLagNoOfPorts"),
        ("LUM-MES-MIB", "mesLagLacpMinNumberOfActiveLinks"),
        ("LUM-MES-MIB", "mesLagIsMcLag"),
        ("LUM-MES-MIB", "mesLagConfigureTagRule"),
        ("LUM-MES-MIB", "mesLagNoOfTagRules"),
        ("LUM-MES-MIB", "mesLagDescr"),
        ("LUM-MES-MIB", "mesLagAdminStatus"),
        ("LUM-MES-MIB", "mesLagOperStatus"))
)
if mibBuilder.loadTexts:
    mesLagGroupV7.setStatus("deprecated")

mesVlanTagClassVlanGroupV3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 1, 1, 100)
)
mesVlanTagClassVlanGroupV3.setObjects(
      *(("LUM-MES-MIB", "mesVlanTagClassVlanIndex"),
        ("LUM-MES-MIB", "mesVlanTagClassVlanName"),
        ("LUM-MES-MIB", "mesVlanTagClassVlanTxPort"),
        ("LUM-MES-MIB", "mesVlanTagClassVlanInternalReference"),
        ("LUM-MES-MIB", "mesVlanTagClassVlanRuleName"),
        ("LUM-MES-MIB", "mesVlanTagClassVlanRuleIndex"),
        ("LUM-MES-MIB", "mesVlanTagClassVlanOuterVlanId"),
        ("LUM-MES-MIB", "mesVlanTagClassVlanLagIndex"))
)
if mibBuilder.loadTexts:
    mesVlanTagClassVlanGroupV3.setStatus("deprecated")

mesCfmMepGroupV8 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 1, 1, 101)
)
mesCfmMepGroupV8.setObjects(
      *(("LUM-MES-MIB", "mesCfmMepIndex"),
        ("LUM-MES-MIB", "mesCfmMepName"),
        ("LUM-MES-MIB", "mesCfmMepMaid"),
        ("LUM-MES-MIB", "mesCfmMepTxPort"),
        ("LUM-MES-MIB", "mesCfmMepPortName"),
        ("LUM-MES-MIB", "mesCfmMepPrimaryVid"),
        ("LUM-MES-MIB", "mesCfmMepAdminStatus"),
        ("LUM-MES-MIB", "mesCfmMepOperStatus"),
        ("LUM-MES-MIB", "mesCfmMepVlanPriority"),
        ("LUM-MES-MIB", "mesCfmMepType"),
        ("LUM-MES-MIB", "mesCfmMepIdentifier"),
        ("LUM-MES-MIB", "mesCfmMepInternalReference"),
        ("LUM-MES-MIB", "mesCfmMepRDICCM"),
        ("LUM-MES-MIB", "mesCfmMepMACstatus"),
        ("LUM-MES-MIB", "mesCfmMepRemoteCCM"),
        ("LUM-MES-MIB", "mesCfmMepErrorCCM"),
        ("LUM-MES-MIB", "mesCfmMepXconCCM"),
        ("LUM-MES-MIB", "mesCfmMepAis"),
        ("LUM-MES-MIB", "mesCfmMepTransmitLbrStatus"),
        ("LUM-MES-MIB", "mesCfmMepRowStatus"),
        ("LUM-MES-MIB", "mesCfmMepDirection"),
        ("LUM-MES-MIB", "mesCfmMepCcmSeqNumStatus"),
        ("LUM-MES-MIB", "mesCfmMepRemoteCsfLos"),
        ("LUM-MES-MIB", "mesCfmMepRemoteCsfRdi"),
        ("LUM-MES-MIB", "mesCfmMepRemoteCsfFdi"),
        ("LUM-MES-MIB", "mesCfmMepLocalCsfLos"),
        ("LUM-MES-MIB", "mesCfmMepLocalDeviceType"),
        ("LUM-MES-MIB", "mesCfmMepLocalDeviceName"),
        ("LUM-MES-MIB", "mesCfmMepLocalDeviceId"),
        ("LUM-MES-MIB", "mesCfmMepViewFilter"),
        ("LUM-MES-MIB", "mesCfmMepUnexpectedPeriod"),
        ("LUM-MES-MIB", "mesCfmMepUnexpectedMepId"),
        ("LUM-MES-MIB", "mesCfmMepUnexpectedMegLevel"),
        ("LUM-MES-MIB", "mesCfmMepMismerge"),
        ("LUM-MES-MIB", "mesCfmMepNoOfLMs"),
        ("LUM-MES-MIB", "mesCfmMepNoOfDMs"),
        ("LUM-MES-MIB", "mesCfmMepTransmitDmrStatus"),
        ("LUM-MES-MIB", "mesCfmMepTransmitLmrStatus"),
        ("LUM-MES-MIB", "mesCfmMepLmCosAwareness"),
        ("LUM-MES-MIB", "mesCfmMepResourceType"),
        ("LUM-MES-MIB", "mesCfmMepLagId"),
        ("LUM-MES-MIB", "mesCfmMepInterfaceName"))
)
if mibBuilder.loadTexts:
    mesCfmMepGroupV8.setStatus("deprecated")

mesMaidGroupV5 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 1, 1, 102)
)
mesMaidGroupV5.setObjects(
      *(("LUM-MES-MIB", "mesMaidIndex"),
        ("LUM-MES-MIB", "mesMaidName"),
        ("LUM-MES-MIB", "mesMaidGroupId"),
        ("LUM-MES-MIB", "mesMaidMdFormat"),
        ("LUM-MES-MIB", "mesMaidMdName"),
        ("LUM-MES-MIB", "mesMaidMdMac"),
        ("LUM-MES-MIB", "mesMaidMd2Octet"),
        ("LUM-MES-MIB", "mesMaidMdString"),
        ("LUM-MES-MIB", "mesMaidLevel"),
        ("LUM-MES-MIB", "mesMaidMaFormat"),
        ("LUM-MES-MIB", "mesMaidMaName"),
        ("LUM-MES-MIB", "mesMaidMaVpnOui"),
        ("LUM-MES-MIB", "mesMaidMaVpnIndex"),
        ("LUM-MES-MIB", "mesMaidMa2Octet"),
        ("LUM-MES-MIB", "mesMaidMaVlan"),
        ("LUM-MES-MIB", "mesMaidMaString"),
        ("LUM-MES-MIB", "mesMaidCcmInterval"),
        ("LUM-MES-MIB", "mesMaidInternalReference"),
        ("LUM-MES-MIB", "mesMaidIdentifier"),
        ("LUM-MES-MIB", "mesMaidNoOfMeps"),
        ("LUM-MES-MIB", "mesMaidAssociateMep"),
        ("LUM-MES-MIB", "mesMaidReleaseMeps"),
        ("LUM-MES-MIB", "mesMaidRowStatus"),
        ("LUM-MES-MIB", "mesMaidNoOfUpMeps"),
        ("LUM-MES-MIB", "mesMaidNoOfNidMeps"),
        ("LUM-MES-MIB", "mesMaidLocalDeviceType"),
        ("LUM-MES-MIB", "mesMaidViewFilter"),
        ("LUM-MES-MIB", "mesMaidAssociateMepNid"))
)
if mibBuilder.loadTexts:
    mesMaidGroupV5.setStatus("deprecated")

mesPortGroupV7 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 1, 1, 103)
)
mesPortGroupV7.setObjects(
      *(("LUM-MES-MIB", "mesPortIndex"),
        ("LUM-MES-MIB", "mesPortName"),
        ("LUM-MES-MIB", "mesPortDescr"),
        ("LUM-MES-MIB", "mesPortSubrack"),
        ("LUM-MES-MIB", "mesPortSlot"),
        ("LUM-MES-MIB", "mesPortTxPort"),
        ("LUM-MES-MIB", "mesPortRxPort"),
        ("LUM-MES-MIB", "mesPortAdminStatus"),
        ("LUM-MES-MIB", "mesPortOperStatus"),
        ("LUM-MES-MIB", "mesPortMtuSize"),
        ("LUM-MES-MIB", "mesPortTagType"),
        ("LUM-MES-MIB", "mesPortNoOfVlans"),
        ("LUM-MES-MIB", "mesPortVlanAware"),
        ("LUM-MES-MIB", "mesPortVlanTagged"),
        ("LUM-MES-MIB", "mesPortVlanUntagged"),
        ("LUM-MES-MIB", "mesPortIngressFiltering"),
        ("LUM-MES-MIB", "mesPortEgressTag"),
        ("LUM-MES-MIB", "mesPortDefaultCeVlanId"),
        ("LUM-MES-MIB", "mesPortAssociateVlan"),
        ("LUM-MES-MIB", "mesPortReleaseVlan"),
        ("LUM-MES-MIB", "mesPortActingAsLine"),
        ("LUM-MES-MIB", "mesPortTrustedPortmask"),
        ("LUM-MES-MIB", "mesPortConfigureTrustedPortmask"),
        ("LUM-MES-MIB", "mesPortMacAddress"),
        ("LUM-MES-MIB", "mesPortLagStatus"),
        ("LUM-MES-MIB", "mesPortLagPortmask"),
        ("LUM-MES-MIB", "mesPortAssociateLag"),
        ("LUM-MES-MIB", "mesPortTxEthUtilization"),
        ("LUM-MES-MIB", "mesPortRxEthUtilization"),
        ("LUM-MES-MIB", "mesPortFlowControlMode"),
        ("LUM-MES-MIB", "mesPortAutoNegotiationMode"),
        ("LUM-MES-MIB", "mesPortAutoNegotiationStatus"),
        ("LUM-MES-MIB", "mesPortLinkDown"),
        ("LUM-MES-MIB", "mesPortLinkFaultRemote"),
        ("LUM-MES-MIB", "mesPortLinkFaultLocal"),
        ("LUM-MES-MIB", "mesPortNoOfShapers"),
        ("LUM-MES-MIB", "mesPortNoOfPolicers"),
        ("LUM-MES-MIB", "mesPortAssociateShaper"),
        ("LUM-MES-MIB", "mesPortReleaseShaper"),
        ("LUM-MES-MIB", "mesPortAssociatePolicer"),
        ("LUM-MES-MIB", "mesPortReleasePolicer"),
        ("LUM-MES-MIB", "mesPortRestartAutoNegotiation"),
        ("LUM-MES-MIB", "mesPortConfigureLine"),
        ("LUM-MES-MIB", "mesPortEtherType"),
        ("LUM-MES-MIB", "mesPortConfigureEtherType"),
        ("LUM-MES-MIB", "mesPortNoOfMirrorSources"),
        ("LUM-MES-MIB", "mesPortMirroring"),
        ("LUM-MES-MIB", "mesPortIngressPushTag"),
        ("LUM-MES-MIB", "mesPortEgressPopTag"),
        ("LUM-MES-MIB", "mesPortDefaultCeVlanPriority"),
        ("LUM-MES-MIB", "mesPortConfigureTagRule"),
        ("LUM-MES-MIB", "mesPortCosProfile"),
        ("LUM-MES-MIB", "mesPortMode"),
        ("LUM-MES-MIB", "mesPortPrioAssignment"),
        ("LUM-MES-MIB", "mesPortConfigurePrioAssignment"),
        ("LUM-MES-MIB", "mesPortNoOfTagRules"),
        ("LUM-MES-MIB", "mesPortNoOfVlanSchedPrios"),
        ("LUM-MES-MIB", "mesPortObjectProperty"),
        ("LUM-MES-MIB", "mesPortHighBitErrorRate"),
        ("LUM-MES-MIB", "mesPortIdx"),
        ("LUM-MES-MIB", "mesPortIfNo"),
        ("LUM-MES-MIB", "mesPortClientIdx"),
        ("LUM-MES-MIB", "mesPortUpPortId"),
        ("LUM-MES-MIB", "mesPortLagPortmaskIf1"),
        ("LUM-MES-MIB", "mesPortLagPortmaskIf2"),
        ("LUM-MES-MIB", "mesPortLagPortmaskIf3"),
        ("LUM-MES-MIB", "mesPortLagPortmaskIf4"),
        ("LUM-MES-MIB", "mesPortLagPortmaskIf5"),
        ("LUM-MES-MIB", "mesPortLagPortmaskIf6"),
        ("LUM-MES-MIB", "mesPortLagPortmaskIf7"),
        ("LUM-MES-MIB", "mesPortLagPortmaskIf8"))
)
if mibBuilder.loadTexts:
    mesPortGroupV7.setStatus("deprecated")

mesVlanMapGroupV8 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 1, 1, 104)
)
mesVlanMapGroupV8.setObjects(
      *(("LUM-MES-MIB", "mesVlanMapIndex"),
        ("LUM-MES-MIB", "mesVlanMapName"),
        ("LUM-MES-MIB", "mesVlanMapVlanIdRangeLower"),
        ("LUM-MES-MIB", "mesVlanMapVlanIdRangeUpper"),
        ("LUM-MES-MIB", "mesVlanMapInternalReference"),
        ("LUM-MES-MIB", "mesVlanMapPortmask"),
        ("LUM-MES-MIB", "mesVlanMapConfigurePortMask"),
        ("LUM-MES-MIB", "mesVlanMapLearning"),
        ("LUM-MES-MIB", "mesVlanMapEtherType"),
        ("LUM-MES-MIB", "mesVlanMapRowStatus"),
        ("LUM-MES-MIB", "mesVlanMapDescr"),
        ("LUM-MES-MIB", "mesVlanMapTrustPorts"),
        ("LUM-MES-MIB", "mesVlanMapRings"),
        ("LUM-MES-MIB", "mesVlanMapServiceId"),
        ("LUM-MES-MIB", "mesVlanMapPortmaskIf1"),
        ("LUM-MES-MIB", "mesVlanMapPortmaskIf2"),
        ("LUM-MES-MIB", "mesVlanMapPortmaskIf3"),
        ("LUM-MES-MIB", "mesVlanMapPortmaskIf4"),
        ("LUM-MES-MIB", "mesVlanMapPortmaskIf5"),
        ("LUM-MES-MIB", "mesVlanMapPortmaskIf6"),
        ("LUM-MES-MIB", "mesVlanMapPortmaskIf7"),
        ("LUM-MES-MIB", "mesVlanMapPortmaskIf8"),
        ("LUM-MES-MIB", "mesVlanMapPrepareConfigPortMask"))
)
if mibBuilder.loadTexts:
    mesVlanMapGroupV8.setStatus("deprecated")

mesErpGroupV6 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 1, 1, 105)
)
mesErpGroupV6.setObjects(
      *(("LUM-MES-MIB", "mesErpIndex"),
        ("LUM-MES-MIB", "mesErpName"),
        ("LUM-MES-MIB", "mesErpPortLeft"),
        ("LUM-MES-MIB", "mesErpPortRight"),
        ("LUM-MES-MIB", "mesErpAdminStatus"),
        ("LUM-MES-MIB", "mesErpInternalReference"),
        ("LUM-MES-MIB", "mesErpDescr"),
        ("LUM-MES-MIB", "mesErpVlanId"),
        ("LUM-MES-MIB", "mesErpMegLevel"),
        ("LUM-MES-MIB", "mesErpProtLink"),
        ("LUM-MES-MIB", "mesErpGuardTime"),
        ("LUM-MES-MIB", "mesErpHoldOffTime"),
        ("LUM-MES-MIB", "mesErpWtrTime"),
        ("LUM-MES-MIB", "mesErpOamDetectionLeft"),
        ("LUM-MES-MIB", "mesErpOamDetectionRight"),
        ("LUM-MES-MIB", "mesErpStatusLeft"),
        ("LUM-MES-MIB", "mesErpStatusRight"),
        ("LUM-MES-MIB", "mesErpProtState"),
        ("LUM-MES-MIB", "mesErpActiveEvent"),
        ("LUM-MES-MIB", "mesErpRapsReqState"),
        ("LUM-MES-MIB", "mesErpServiceFailure"),
        ("LUM-MES-MIB", "mesErpServiceDegraded"),
        ("LUM-MES-MIB", "mesErpUnexpectedMegLevel"),
        ("LUM-MES-MIB", "mesErpCommunicationFailure"),
        ("LUM-MES-MIB", "mesErpProvisioningMismatch"),
        ("LUM-MES-MIB", "mesErpRowStatus"),
        ("LUM-MES-MIB", "mesErpNodeType"),
        ("LUM-MES-MIB", "mesErpProtectionMode"),
        ("LUM-MES-MIB", "mesErpVersion"),
        ("LUM-MES-MIB", "mesErpMajorName"),
        ("LUM-MES-MIB", "mesErpRingId"),
        ("LUM-MES-MIB", "mesErpRingIndex"),
        ("LUM-MES-MIB", "mesErpOperatorCommand"),
        ("LUM-MES-MIB", "mesErpGroupId"),
        ("LUM-MES-MIB", "mesErpSwitchInformation"),
        ("LUM-MES-MIB", "mesErpTopologyChangePropagation"),
        ("LUM-MES-MIB", "mesErpSubRings"),
        ("LUM-MES-MIB", "mesErpResourceTypeLeft"),
        ("LUM-MES-MIB", "mesErpLagIdLeft"),
        ("LUM-MES-MIB", "mesErpResourceTypeRight"),
        ("LUM-MES-MIB", "mesErpLagIdRight"),
        ("LUM-MES-MIB", "mesErpInterfaceLeft"),
        ("LUM-MES-MIB", "mesErpInterfaceRight"),
        ("LUM-MES-MIB", "mesErpIfNoLeft"),
        ("LUM-MES-MIB", "mesErpTxPortLeft"),
        ("LUM-MES-MIB", "mesErpIfNoRight"),
        ("LUM-MES-MIB", "mesErpTxPortRight"))
)
if mibBuilder.loadTexts:
    mesErpGroupV6.setStatus("deprecated")

mesMgmtVlanGroupV4 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 1, 1, 106)
)
mesMgmtVlanGroupV4.setObjects(
      *(("LUM-MES-MIB", "mesMgmtVlanIndex"),
        ("LUM-MES-MIB", "mesMgmtVlanName"),
        ("LUM-MES-MIB", "mesMgmtVlanDescr"),
        ("LUM-MES-MIB", "mesMgmtVlanSubrack"),
        ("LUM-MES-MIB", "mesMgmtVlanSlot"),
        ("LUM-MES-MIB", "mesMgmtVlanTxPort"),
        ("LUM-MES-MIB", "mesMgmtVlanRxPort"),
        ("LUM-MES-MIB", "mesMgmtVlanObjectProperty"),
        ("LUM-MES-MIB", "mesMgmtVlanAdminStatus"),
        ("LUM-MES-MIB", "mesMgmtVlanConfigure"),
        ("LUM-MES-MIB", "mesMgmtVlanTagType"),
        ("LUM-MES-MIB", "mesMgmtVlanEtherType"),
        ("LUM-MES-MIB", "mesMgmtVlanVlanId"),
        ("LUM-MES-MIB", "mesMgmtVlanPriority"),
        ("LUM-MES-MIB", "mesMgmtVlanMacInMac"),
        ("LUM-MES-MIB", "mesMgmtVlanMacInMacIsid"),
        ("LUM-MES-MIB", "mesMgmtVlanMacInMacDa"),
        ("LUM-MES-MIB", "mesMgmtVlanForceMgmtVlan"),
        ("LUM-MES-MIB", "mesMgmtVlanRings"),
        ("LUM-MES-MIB", "mesMgmtVlanIfNo"))
)
if mibBuilder.loadTexts:
    mesMgmtVlanGroupV4.setStatus("current")

mesPolicingGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 1, 1, 107)
)
mesPolicingGroupV2.setObjects(
      *(("LUM-MES-MIB", "mesPolicingIndex"),
        ("LUM-MES-MIB", "mesPolicingName"),
        ("LUM-MES-MIB", "mesPolicingRate"),
        ("LUM-MES-MIB", "mesPolicingBurstSize"),
        ("LUM-MES-MIB", "mesPolicingType"),
        ("LUM-MES-MIB", "mesPolicingInternalReference"),
        ("LUM-MES-MIB", "mesPolicingIdentifier"),
        ("LUM-MES-MIB", "mesPolicingUpId"))
)
if mibBuilder.loadTexts:
    mesPolicingGroupV2.setStatus("deprecated")

mesLagGroupV8 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 1, 1, 108)
)
mesLagGroupV8.setObjects(
      *(("LUM-MES-MIB", "mesLagIndex"),
        ("LUM-MES-MIB", "mesLagName"),
        ("LUM-MES-MIB", "mesLagInternalReference"),
        ("LUM-MES-MIB", "mesLagPortmask"),
        ("LUM-MES-MIB", "mesLagMasterIndex"),
        ("LUM-MES-MIB", "mesLagConfigure"),
        ("LUM-MES-MIB", "mesLagHash"),
        ("LUM-MES-MIB", "mesLagIdentifier"),
        ("LUM-MES-MIB", "mesLagRowStatus"),
        ("LUM-MES-MIB", "mesLagLacpEnabled"),
        ("LUM-MES-MIB", "mesLagLacpSystemPriority"),
        ("LUM-MES-MIB", "mesLagLacpPeriod"),
        ("LUM-MES-MIB", "mesLagLacpLinkProtection"),
        ("LUM-MES-MIB", "mesLagDegraded"),
        ("LUM-MES-MIB", "mesLagFailure"),
        ("LUM-MES-MIB", "mesLagLacpMaxNumberOfActiveLinks"),
        ("LUM-MES-MIB", "mesLagNoOfPorts"),
        ("LUM-MES-MIB", "mesLagLacpMinNumberOfActiveLinks"),
        ("LUM-MES-MIB", "mesLagIsMcLag"),
        ("LUM-MES-MIB", "mesLagConfigureTagRule"),
        ("LUM-MES-MIB", "mesLagNoOfTagRules"),
        ("LUM-MES-MIB", "mesLagDescr"),
        ("LUM-MES-MIB", "mesLagAdminStatus"),
        ("LUM-MES-MIB", "mesLagOperStatus"),
        ("LUM-MES-MIB", "mesLagPortmaskIf1"),
        ("LUM-MES-MIB", "mesLagPortmaskIf2"),
        ("LUM-MES-MIB", "mesLagPortmaskIf3"),
        ("LUM-MES-MIB", "mesLagPortmaskIf4"),
        ("LUM-MES-MIB", "mesLagPortmaskIf5"),
        ("LUM-MES-MIB", "mesLagPortmaskIf6"),
        ("LUM-MES-MIB", "mesLagPortmaskIf7"),
        ("LUM-MES-MIB", "mesLagPortmaskIf8"),
        ("LUM-MES-MIB", "mesLagMasterIfNo"),
        ("LUM-MES-MIB", "mesLagMasterTxPort"),
        ("LUM-MES-MIB", "mesLagLocalId"),
        ("LUM-MES-MIB", "mesLagPrepareConfigPortMask"))
)
if mibBuilder.loadTexts:
    mesLagGroupV8.setStatus("deprecated")

mesCosProfileGroupV3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 1, 1, 109)
)
mesCosProfileGroupV3.setObjects(
      *(("LUM-MES-MIB", "mesCosProfileIndex"),
        ("LUM-MES-MIB", "mesCosProfileName"),
        ("LUM-MES-MIB", "mesCosProfilePortmask"),
        ("LUM-MES-MIB", "mesCosProfilePortmaskIf1"),
        ("LUM-MES-MIB", "mesCosProfilePortmaskIf2"),
        ("LUM-MES-MIB", "mesCosProfilePortmaskIf3"),
        ("LUM-MES-MIB", "mesCosProfilePortmaskIf4"),
        ("LUM-MES-MIB", "mesCosProfilePortmaskIf5"),
        ("LUM-MES-MIB", "mesCosProfilePortmaskIf6"),
        ("LUM-MES-MIB", "mesCosProfilePortmaskIf7"),
        ("LUM-MES-MIB", "mesCosProfilePortmaskIf8"),
        ("LUM-MES-MIB", "mesCosProfileScheduler"),
        ("LUM-MES-MIB", "mesCosProfileWeight0"),
        ("LUM-MES-MIB", "mesCosProfileWeight1"),
        ("LUM-MES-MIB", "mesCosProfileWeight2"),
        ("LUM-MES-MIB", "mesCosProfileWeight3"),
        ("LUM-MES-MIB", "mesCosProfileWeight4"),
        ("LUM-MES-MIB", "mesCosProfileWeight5"),
        ("LUM-MES-MIB", "mesCosProfileWeight6"),
        ("LUM-MES-MIB", "mesCosProfileWeight7"),
        ("LUM-MES-MIB", "mesCosProfilePriority0"),
        ("LUM-MES-MIB", "mesCosProfilePriority1"),
        ("LUM-MES-MIB", "mesCosProfilePriority2"),
        ("LUM-MES-MIB", "mesCosProfilePriority3"),
        ("LUM-MES-MIB", "mesCosProfilePriority4"),
        ("LUM-MES-MIB", "mesCosProfilePriority5"),
        ("LUM-MES-MIB", "mesCosProfilePriority6"),
        ("LUM-MES-MIB", "mesCosProfilePriority7"),
        ("LUM-MES-MIB", "mesCosProfileConfigureScheduler"),
        ("LUM-MES-MIB", "mesCosProfileIngressPcpDecoding"),
        ("LUM-MES-MIB", "mesCosProfileIngressDeiDecoding"),
        ("LUM-MES-MIB", "mesCosProfileIngressColor0"),
        ("LUM-MES-MIB", "mesCosProfileIngressColor1"),
        ("LUM-MES-MIB", "mesCosProfileIngressColor2"),
        ("LUM-MES-MIB", "mesCosProfileIngressColor3"),
        ("LUM-MES-MIB", "mesCosProfileIngressColor4"),
        ("LUM-MES-MIB", "mesCosProfileIngressColor5"),
        ("LUM-MES-MIB", "mesCosProfileIngressColor6"),
        ("LUM-MES-MIB", "mesCosProfileIngressColor7"),
        ("LUM-MES-MIB", "mesCosProfileEgressPcpEncoding"),
        ("LUM-MES-MIB", "mesCosProfileEgressDeiEncoding"),
        ("LUM-MES-MIB", "mesCosProfileEgressPcpGreen0"),
        ("LUM-MES-MIB", "mesCosProfileEgressPcpGreen1"),
        ("LUM-MES-MIB", "mesCosProfileEgressPcpGreen2"),
        ("LUM-MES-MIB", "mesCosProfileEgressPcpGreen3"),
        ("LUM-MES-MIB", "mesCosProfileEgressPcpGreen4"),
        ("LUM-MES-MIB", "mesCosProfileEgressPcpGreen5"),
        ("LUM-MES-MIB", "mesCosProfileEgressPcpGreen6"),
        ("LUM-MES-MIB", "mesCosProfileEgressPcpGreen7"),
        ("LUM-MES-MIB", "mesCosProfileEgressPcpYellow0"),
        ("LUM-MES-MIB", "mesCosProfileEgressPcpYellow1"),
        ("LUM-MES-MIB", "mesCosProfileEgressPcpYellow2"),
        ("LUM-MES-MIB", "mesCosProfileEgressPcpYellow3"),
        ("LUM-MES-MIB", "mesCosProfileEgressPcpYellow4"),
        ("LUM-MES-MIB", "mesCosProfileEgressPcpYellow5"),
        ("LUM-MES-MIB", "mesCosProfileEgressPcpYellow6"),
        ("LUM-MES-MIB", "mesCosProfileEgressPcpYellow7"))
)
if mibBuilder.loadTexts:
    mesCosProfileGroupV3.setStatus("deprecated")

mesVlanTagClassVlanGroupV4 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 1, 1, 110)
)
mesVlanTagClassVlanGroupV4.setObjects(
      *(("LUM-MES-MIB", "mesVlanTagClassVlanIndex"),
        ("LUM-MES-MIB", "mesVlanTagClassVlanName"),
        ("LUM-MES-MIB", "mesVlanTagClassVlanTxPort"),
        ("LUM-MES-MIB", "mesVlanTagClassVlanInternalReference"),
        ("LUM-MES-MIB", "mesVlanTagClassVlanRuleName"),
        ("LUM-MES-MIB", "mesVlanTagClassVlanRuleIndex"),
        ("LUM-MES-MIB", "mesVlanTagClassVlanOuterVlanId"),
        ("LUM-MES-MIB", "mesVlanTagClassVlanLagIndex"),
        ("LUM-MES-MIB", "mesVlanTagClassVlanIfNo"))
)
if mibBuilder.loadTexts:
    mesVlanTagClassVlanGroupV4.setStatus("deprecated")

mesLacpGroupV1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 1, 1, 111)
)
mesLacpGroupV1.setObjects(
      *(("LUM-MES-MIB", "mesLacpIndex"),
        ("LUM-MES-MIB", "mesLacpName"),
        ("LUM-MES-MIB", "mesLacpInternalReference"),
        ("LUM-MES-MIB", "mesLacpLagIdentifier"),
        ("LUM-MES-MIB", "mesLacpLagId"),
        ("LUM-MES-MIB", "mesLacpPortPriority"),
        ("LUM-MES-MIB", "mesLacpSelected"),
        ("LUM-MES-MIB", "mesLacpReceiveState"),
        ("LUM-MES-MIB", "mesLacpTransmitState"),
        ("LUM-MES-MIB", "mesLacpMuxState"),
        ("LUM-MES-MIB", "mesLacpActorExpired"),
        ("LUM-MES-MIB", "mesLacpActorDefault"),
        ("LUM-MES-MIB", "mesLacpActorDistributing"),
        ("LUM-MES-MIB", "mesLacpActorCollecting"),
        ("LUM-MES-MIB", "mesLacpActorSynchronization"),
        ("LUM-MES-MIB", "mesLacpActorAggregation"),
        ("LUM-MES-MIB", "mesLacpActorTimeout"),
        ("LUM-MES-MIB", "mesLacpActorActivity"),
        ("LUM-MES-MIB", "mesLacpPartnerExpired"),
        ("LUM-MES-MIB", "mesLacpPartnerDefault"),
        ("LUM-MES-MIB", "mesLacpPartnerDistributing"),
        ("LUM-MES-MIB", "mesLacpPartnerCollecting"),
        ("LUM-MES-MIB", "mesLacpPartnerSynchronization"),
        ("LUM-MES-MIB", "mesLacpPartnerAggregation"),
        ("LUM-MES-MIB", "mesLacpPartnerTimeout"),
        ("LUM-MES-MIB", "mesLacpPartnerActivity"),
        ("LUM-MES-MIB", "mesLacpTxLacpPdus"),
        ("LUM-MES-MIB", "mesLacpRxLacpPdus"),
        ("LUM-MES-MIB", "mesLacpInternalIndex"),
        ("LUM-MES-MIB", "mesLacpResetCounters"),
        ("LUM-MES-MIB", "mesLacpIfNo"),
        ("LUM-MES-MIB", "mesLacpTxPort"),
        ("LUM-MES-MIB", "mesLacpUpPortId"))
)
if mibBuilder.loadTexts:
    mesLacpGroupV1.setStatus("current")

mesVlanTagRuleGroupV4 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 1, 1, 112)
)
mesVlanTagRuleGroupV4.setObjects(
      *(("LUM-MES-MIB", "mesVlanTagRuleIndex"),
        ("LUM-MES-MIB", "mesVlanTagRuleName"),
        ("LUM-MES-MIB", "mesVlanTagRuleInternalReference"),
        ("LUM-MES-MIB", "mesVlanTagRuleClassificationName"),
        ("LUM-MES-MIB", "mesVlanTagRuleType"),
        ("LUM-MES-MIB", "mesVlanTagRuleOperation"),
        ("LUM-MES-MIB", "mesVlanTagRuleInnerVlanId"),
        ("LUM-MES-MIB", "mesVlanTagRuleInnerPrio"),
        ("LUM-MES-MIB", "mesVlanTagRuleOuterVlanId"),
        ("LUM-MES-MIB", "mesVlanTagRuleOuterPrio"),
        ("LUM-MES-MIB", "mesVlanTagRulePrioAssignment"),
        ("LUM-MES-MIB", "mesVlanTagRuleConfigurePrioAssignment"),
        ("LUM-MES-MIB", "mesVlanTagRuleQueue"),
        ("LUM-MES-MIB", "mesVlanTagRuleRowStatus"),
        ("LUM-MES-MIB", "mesVlanTagRuleInterfaceName"))
)
if mibBuilder.loadTexts:
    mesVlanTagRuleGroupV4.setStatus("current")

mesCfmMepGroupV9 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 1, 1, 113)
)
mesCfmMepGroupV9.setObjects(
      *(("LUM-MES-MIB", "mesCfmMepIndex"),
        ("LUM-MES-MIB", "mesCfmMepName"),
        ("LUM-MES-MIB", "mesCfmMepMaid"),
        ("LUM-MES-MIB", "mesCfmMepTxPort"),
        ("LUM-MES-MIB", "mesCfmMepPortName"),
        ("LUM-MES-MIB", "mesCfmMepPrimaryVid"),
        ("LUM-MES-MIB", "mesCfmMepAdminStatus"),
        ("LUM-MES-MIB", "mesCfmMepOperStatus"),
        ("LUM-MES-MIB", "mesCfmMepVlanPriority"),
        ("LUM-MES-MIB", "mesCfmMepType"),
        ("LUM-MES-MIB", "mesCfmMepIdentifier"),
        ("LUM-MES-MIB", "mesCfmMepInternalReference"),
        ("LUM-MES-MIB", "mesCfmMepRDICCM"),
        ("LUM-MES-MIB", "mesCfmMepMACstatus"),
        ("LUM-MES-MIB", "mesCfmMepRemoteCCM"),
        ("LUM-MES-MIB", "mesCfmMepErrorCCM"),
        ("LUM-MES-MIB", "mesCfmMepXconCCM"),
        ("LUM-MES-MIB", "mesCfmMepAis"),
        ("LUM-MES-MIB", "mesCfmMepTransmitLbrStatus"),
        ("LUM-MES-MIB", "mesCfmMepRowStatus"),
        ("LUM-MES-MIB", "mesCfmMepDirection"),
        ("LUM-MES-MIB", "mesCfmMepCcmSeqNumStatus"),
        ("LUM-MES-MIB", "mesCfmMepRemoteCsfLos"),
        ("LUM-MES-MIB", "mesCfmMepRemoteCsfRdi"),
        ("LUM-MES-MIB", "mesCfmMepRemoteCsfFdi"),
        ("LUM-MES-MIB", "mesCfmMepLocalCsfLos"),
        ("LUM-MES-MIB", "mesCfmMepLocalDeviceType"),
        ("LUM-MES-MIB", "mesCfmMepLocalDeviceName"),
        ("LUM-MES-MIB", "mesCfmMepLocalDeviceId"),
        ("LUM-MES-MIB", "mesCfmMepViewFilter"),
        ("LUM-MES-MIB", "mesCfmMepUnexpectedPeriod"),
        ("LUM-MES-MIB", "mesCfmMepUnexpectedMepId"),
        ("LUM-MES-MIB", "mesCfmMepUnexpectedMegLevel"),
        ("LUM-MES-MIB", "mesCfmMepMismerge"),
        ("LUM-MES-MIB", "mesCfmMepNoOfLMs"),
        ("LUM-MES-MIB", "mesCfmMepNoOfDMs"),
        ("LUM-MES-MIB", "mesCfmMepTransmitDmrStatus"),
        ("LUM-MES-MIB", "mesCfmMepTransmitLmrStatus"),
        ("LUM-MES-MIB", "mesCfmMepLmCosAwareness"),
        ("LUM-MES-MIB", "mesCfmMepResourceType"),
        ("LUM-MES-MIB", "mesCfmMepLagId"),
        ("LUM-MES-MIB", "mesCfmMepInterfaceName"),
        ("LUM-MES-MIB", "mesCfmMepIfNo"))
)
if mibBuilder.loadTexts:
    mesCfmMepGroupV9.setStatus("deprecated")

mesPolicingGroupV3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 1, 1, 114)
)
mesPolicingGroupV3.setObjects(
      *(("LUM-MES-MIB", "mesPolicingIndex"),
        ("LUM-MES-MIB", "mesPolicingName"),
        ("LUM-MES-MIB", "mesPolicingRate"),
        ("LUM-MES-MIB", "mesPolicingType"),
        ("LUM-MES-MIB", "mesPolicingInternalReference"),
        ("LUM-MES-MIB", "mesPolicingIdentifier"),
        ("LUM-MES-MIB", "mesPolicingUpId"),
        ("LUM-MES-MIB", "mesPolicingBurstSize2"))
)
if mibBuilder.loadTexts:
    mesPolicingGroupV3.setStatus("deprecated")

mesErpGroupV7 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 1, 1, 115)
)
mesErpGroupV7.setObjects(
      *(("LUM-MES-MIB", "mesErpIndex"),
        ("LUM-MES-MIB", "mesErpName"),
        ("LUM-MES-MIB", "mesErpPortLeft"),
        ("LUM-MES-MIB", "mesErpPortRight"),
        ("LUM-MES-MIB", "mesErpAdminStatus"),
        ("LUM-MES-MIB", "mesErpInternalReference"),
        ("LUM-MES-MIB", "mesErpDescr"),
        ("LUM-MES-MIB", "mesErpVlanId"),
        ("LUM-MES-MIB", "mesErpMegLevel"),
        ("LUM-MES-MIB", "mesErpProtLink"),
        ("LUM-MES-MIB", "mesErpGuardTime"),
        ("LUM-MES-MIB", "mesErpHoldOffTime"),
        ("LUM-MES-MIB", "mesErpWtrTime"),
        ("LUM-MES-MIB", "mesErpOamDetectionLeft"),
        ("LUM-MES-MIB", "mesErpOamDetectionRight"),
        ("LUM-MES-MIB", "mesErpStatusLeft"),
        ("LUM-MES-MIB", "mesErpStatusRight"),
        ("LUM-MES-MIB", "mesErpProtState"),
        ("LUM-MES-MIB", "mesErpActiveEvent"),
        ("LUM-MES-MIB", "mesErpRapsReqState"),
        ("LUM-MES-MIB", "mesErpServiceFailure"),
        ("LUM-MES-MIB", "mesErpServiceDegraded"),
        ("LUM-MES-MIB", "mesErpUnexpectedMegLevel"),
        ("LUM-MES-MIB", "mesErpCommunicationFailure"),
        ("LUM-MES-MIB", "mesErpProvisioningMismatch"),
        ("LUM-MES-MIB", "mesErpRowStatus"),
        ("LUM-MES-MIB", "mesErpNodeType"),
        ("LUM-MES-MIB", "mesErpProtectionMode"),
        ("LUM-MES-MIB", "mesErpVersion"),
        ("LUM-MES-MIB", "mesErpMajorName"),
        ("LUM-MES-MIB", "mesErpRingId"),
        ("LUM-MES-MIB", "mesErpRingIndex"),
        ("LUM-MES-MIB", "mesErpOperatorCommand"),
        ("LUM-MES-MIB", "mesErpGroupId"),
        ("LUM-MES-MIB", "mesErpSwitchInformation"),
        ("LUM-MES-MIB", "mesErpTopologyChangePropagation"),
        ("LUM-MES-MIB", "mesErpSubRings"),
        ("LUM-MES-MIB", "mesErpResourceTypeLeft"),
        ("LUM-MES-MIB", "mesErpLagIdLeft"),
        ("LUM-MES-MIB", "mesErpResourceTypeRight"),
        ("LUM-MES-MIB", "mesErpLagIdRight"),
        ("LUM-MES-MIB", "mesErpInterfaceLeft"),
        ("LUM-MES-MIB", "mesErpInterfaceRight"),
        ("LUM-MES-MIB", "mesErpIfNoLeft"),
        ("LUM-MES-MIB", "mesErpTxPortLeft"),
        ("LUM-MES-MIB", "mesErpIfNoRight"),
        ("LUM-MES-MIB", "mesErpTxPortRight"),
        ("LUM-MES-MIB", "mesErpOamDetectionVlanId"))
)
if mibBuilder.loadTexts:
    mesErpGroupV7.setStatus("current")

mesPortGroupV8 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 1, 1, 116)
)
mesPortGroupV8.setObjects(
      *(("LUM-MES-MIB", "mesPortIndex"),
        ("LUM-MES-MIB", "mesPortName"),
        ("LUM-MES-MIB", "mesPortDescr"),
        ("LUM-MES-MIB", "mesPortSubrack"),
        ("LUM-MES-MIB", "mesPortSlot"),
        ("LUM-MES-MIB", "mesPortTxPort"),
        ("LUM-MES-MIB", "mesPortRxPort"),
        ("LUM-MES-MIB", "mesPortAdminStatus"),
        ("LUM-MES-MIB", "mesPortOperStatus"),
        ("LUM-MES-MIB", "mesPortMtuSize"),
        ("LUM-MES-MIB", "mesPortTagType"),
        ("LUM-MES-MIB", "mesPortNoOfVlans"),
        ("LUM-MES-MIB", "mesPortVlanAware"),
        ("LUM-MES-MIB", "mesPortVlanTagged"),
        ("LUM-MES-MIB", "mesPortVlanUntagged"),
        ("LUM-MES-MIB", "mesPortIngressFiltering"),
        ("LUM-MES-MIB", "mesPortEgressTag"),
        ("LUM-MES-MIB", "mesPortDefaultCeVlanId"),
        ("LUM-MES-MIB", "mesPortAssociateVlan"),
        ("LUM-MES-MIB", "mesPortReleaseVlan"),
        ("LUM-MES-MIB", "mesPortActingAsLine"),
        ("LUM-MES-MIB", "mesPortTrustedPortmask"),
        ("LUM-MES-MIB", "mesPortConfigureTrustedPortmask"),
        ("LUM-MES-MIB", "mesPortMacAddress"),
        ("LUM-MES-MIB", "mesPortLagStatus"),
        ("LUM-MES-MIB", "mesPortLagPortmask"),
        ("LUM-MES-MIB", "mesPortAssociateLag"),
        ("LUM-MES-MIB", "mesPortTxEthUtilization"),
        ("LUM-MES-MIB", "mesPortRxEthUtilization"),
        ("LUM-MES-MIB", "mesPortFlowControlMode"),
        ("LUM-MES-MIB", "mesPortAutoNegotiationMode"),
        ("LUM-MES-MIB", "mesPortAutoNegotiationStatus"),
        ("LUM-MES-MIB", "mesPortLinkDown"),
        ("LUM-MES-MIB", "mesPortLinkFaultRemote"),
        ("LUM-MES-MIB", "mesPortLinkFaultLocal"),
        ("LUM-MES-MIB", "mesPortNoOfShapers"),
        ("LUM-MES-MIB", "mesPortNoOfPolicers"),
        ("LUM-MES-MIB", "mesPortAssociateShaper"),
        ("LUM-MES-MIB", "mesPortReleaseShaper"),
        ("LUM-MES-MIB", "mesPortAssociatePolicer"),
        ("LUM-MES-MIB", "mesPortReleasePolicer"),
        ("LUM-MES-MIB", "mesPortRestartAutoNegotiation"),
        ("LUM-MES-MIB", "mesPortConfigureLine"),
        ("LUM-MES-MIB", "mesPortEtherType"),
        ("LUM-MES-MIB", "mesPortConfigureEtherType"),
        ("LUM-MES-MIB", "mesPortNoOfMirrorSources"),
        ("LUM-MES-MIB", "mesPortMirroring"),
        ("LUM-MES-MIB", "mesPortIngressPushTag"),
        ("LUM-MES-MIB", "mesPortEgressPopTag"),
        ("LUM-MES-MIB", "mesPortDefaultCeVlanPriority"),
        ("LUM-MES-MIB", "mesPortConfigureTagRule"),
        ("LUM-MES-MIB", "mesPortCosProfile"),
        ("LUM-MES-MIB", "mesPortMode"),
        ("LUM-MES-MIB", "mesPortPrioAssignment"),
        ("LUM-MES-MIB", "mesPortConfigurePrioAssignment"),
        ("LUM-MES-MIB", "mesPortNoOfTagRules"),
        ("LUM-MES-MIB", "mesPortObjectProperty"),
        ("LUM-MES-MIB", "mesPortHighBitErrorRate"),
        ("LUM-MES-MIB", "mesPortIdx"),
        ("LUM-MES-MIB", "mesPortIfNo"),
        ("LUM-MES-MIB", "mesPortClientIdx"),
        ("LUM-MES-MIB", "mesPortUpPortId"),
        ("LUM-MES-MIB", "mesPortLagPortmaskIf1"),
        ("LUM-MES-MIB", "mesPortLagPortmaskIf2"),
        ("LUM-MES-MIB", "mesPortLagPortmaskIf3"),
        ("LUM-MES-MIB", "mesPortLagPortmaskIf4"),
        ("LUM-MES-MIB", "mesPortLagPortmaskIf5"),
        ("LUM-MES-MIB", "mesPortLagPortmaskIf6"),
        ("LUM-MES-MIB", "mesPortLagPortmaskIf7"),
        ("LUM-MES-MIB", "mesPortLagPortmaskIf8"))
)
if mibBuilder.loadTexts:
    mesPortGroupV8.setStatus("deprecated")

mesActionGroupV3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 1, 1, 117)
)
mesActionGroupV3.setObjects(
      *(("LUM-MES-MIB", "mesActionIndex"),
        ("LUM-MES-MIB", "mesActionName"),
        ("LUM-MES-MIB", "mesActionIdentifier"),
        ("LUM-MES-MIB", "mesActionInternalReference"),
        ("LUM-MES-MIB", "mesActionType"),
        ("LUM-MES-MIB", "mesActionOuterVlanId"),
        ("LUM-MES-MIB", "mesActionPcp"),
        ("LUM-MES-MIB", "mesActionPolicerId"),
        ("LUM-MES-MIB", "mesActionInnerVlanId"),
        ("LUM-MES-MIB", "mesActionQueue"),
        ("LUM-MES-MIB", "mesActionRowStatus"),
        ("LUM-MES-MIB", "mesActionRedirectPort"),
        ("LUM-MES-MIB", "mesActionServiceId"),
        ("LUM-MES-MIB", "mesActionRedirectIfNo"),
        ("LUM-MES-MIB", "mesActionRedirectTxPort"))
)
if mibBuilder.loadTexts:
    mesActionGroupV3.setStatus("deprecated")

mesClassGroupV5 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 1, 1, 118)
)
mesClassGroupV5.setObjects(
      *(("LUM-MES-MIB", "mesClassIndex"),
        ("LUM-MES-MIB", "mesClassName"),
        ("LUM-MES-MIB", "mesClassIdentifier"),
        ("LUM-MES-MIB", "mesClassPort"),
        ("LUM-MES-MIB", "mesClassLagId"),
        ("LUM-MES-MIB", "mesClassInternalReference"),
        ("LUM-MES-MIB", "mesClassOuterVlanId"),
        ("LUM-MES-MIB", "mesClassOuterVlanPcp"),
        ("LUM-MES-MIB", "mesClassPrecedence"),
        ("LUM-MES-MIB", "mesClassDaMacAddress"),
        ("LUM-MES-MIB", "mesClassAssociateAction"),
        ("LUM-MES-MIB", "mesClassRowStatus"),
        ("LUM-MES-MIB", "mesClassDaMacAddressMask"),
        ("LUM-MES-MIB", "mesClassDSCP"),
        ("LUM-MES-MIB", "mesClassInnerVlanId"),
        ("LUM-MES-MIB", "mesClassInnerVlanPcp"),
        ("LUM-MES-MIB", "mesClassInnerVlanCfi"),
        ("LUM-MES-MIB", "mesClassOuterVlanCfi"),
        ("LUM-MES-MIB", "mesClassDirection"),
        ("LUM-MES-MIB", "mesClassOuterTpid"),
        ("LUM-MES-MIB", "mesClassInternalClassId"),
        ("LUM-MES-MIB", "mesClassSourceAddressIPV4"),
        ("LUM-MES-MIB", "mesClassSourceMaskIPV4"),
        ("LUM-MES-MIB", "mesClassDestAddressIPV4"),
        ("LUM-MES-MIB", "mesClassDestMaskIPV4"),
        ("LUM-MES-MIB", "mesClassSubrack"),
        ("LUM-MES-MIB", "mesClassSlot"),
        ("LUM-MES-MIB", "mesClassVlanStackStructure"),
        ("LUM-MES-MIB", "mesClassServiceId"),
        ("LUM-MES-MIB", "mesClassIfNo"),
        ("LUM-MES-MIB", "mesClassTxPort"))
)
if mibBuilder.loadTexts:
    mesClassGroupV5.setStatus("deprecated")

mesShapingGroupV3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 1, 1, 119)
)
mesShapingGroupV3.setObjects(
      *(("LUM-MES-MIB", "mesShapingIndex"),
        ("LUM-MES-MIB", "mesShapingName"),
        ("LUM-MES-MIB", "mesShapingRate"),
        ("LUM-MES-MIB", "mesShapingBurstSize"),
        ("LUM-MES-MIB", "mesShapingQueue"),
        ("LUM-MES-MIB", "mesShapingInternalReference"),
        ("LUM-MES-MIB", "mesShapingExcess"),
        ("LUM-MES-MIB", "mesShapingIdentifier"),
        ("LUM-MES-MIB", "mesShapingMinRate"),
        ("LUM-MES-MIB", "mesShapingLocalId"))
)
if mibBuilder.loadTexts:
    mesShapingGroupV3.setStatus("current")

mesPolicingGroupV4 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 1, 1, 120)
)
mesPolicingGroupV4.setObjects(
      *(("LUM-MES-MIB", "mesPolicingIndex"),
        ("LUM-MES-MIB", "mesPolicingName"),
        ("LUM-MES-MIB", "mesPolicingRate"),
        ("LUM-MES-MIB", "mesPolicingType"),
        ("LUM-MES-MIB", "mesPolicingInternalReference"),
        ("LUM-MES-MIB", "mesPolicingIdentifier"),
        ("LUM-MES-MIB", "mesPolicingUpId"),
        ("LUM-MES-MIB", "mesPolicingBurstSize2"),
        ("LUM-MES-MIB", "mesPolicingId"))
)
if mibBuilder.loadTexts:
    mesPolicingGroupV4.setStatus("current")

mesBwpGroupV4 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 1, 1, 121)
)
mesBwpGroupV4.setObjects(
      *(("LUM-MES-MIB", "mesBwpIndex"),
        ("LUM-MES-MIB", "mesBwpName"),
        ("LUM-MES-MIB", "mesBwpObjectProperty"),
        ("LUM-MES-MIB", "mesBwpCoSIdentifier"),
        ("LUM-MES-MIB", "mesBwpCir"),
        ("LUM-MES-MIB", "mesBwpCbs"),
        ("LUM-MES-MIB", "mesBwpEir"),
        ("LUM-MES-MIB", "mesBwpEbs"),
        ("LUM-MES-MIB", "mesBwpCouplingFlag"),
        ("LUM-MES-MIB", "mesBwpColorMode"),
        ("LUM-MES-MIB", "mesBwpInternalReference"),
        ("LUM-MES-MIB", "mesBwpRowStatus"),
        ("LUM-MES-MIB", "mesBwpServiceId"),
        ("LUM-MES-MIB", "mesBwpPolicerId"))
)
if mibBuilder.loadTexts:
    mesBwpGroupV4.setStatus("deprecated")

mesCfmMepGroupV10 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 1, 1, 122)
)
mesCfmMepGroupV10.setObjects(
      *(("LUM-MES-MIB", "mesCfmMepIndex"),
        ("LUM-MES-MIB", "mesCfmMepName"),
        ("LUM-MES-MIB", "mesCfmMepMaid"),
        ("LUM-MES-MIB", "mesCfmMepTxPort"),
        ("LUM-MES-MIB", "mesCfmMepPortName"),
        ("LUM-MES-MIB", "mesCfmMepPrimaryVid"),
        ("LUM-MES-MIB", "mesCfmMepAdminStatus"),
        ("LUM-MES-MIB", "mesCfmMepOperStatus"),
        ("LUM-MES-MIB", "mesCfmMepVlanPriority"),
        ("LUM-MES-MIB", "mesCfmMepType"),
        ("LUM-MES-MIB", "mesCfmMepIdentifier"),
        ("LUM-MES-MIB", "mesCfmMepInternalReference"),
        ("LUM-MES-MIB", "mesCfmMepRDICCM"),
        ("LUM-MES-MIB", "mesCfmMepMACstatus"),
        ("LUM-MES-MIB", "mesCfmMepRemoteCCM"),
        ("LUM-MES-MIB", "mesCfmMepErrorCCM"),
        ("LUM-MES-MIB", "mesCfmMepXconCCM"),
        ("LUM-MES-MIB", "mesCfmMepAis"),
        ("LUM-MES-MIB", "mesCfmMepTransmitLbrStatus"),
        ("LUM-MES-MIB", "mesCfmMepRowStatus"),
        ("LUM-MES-MIB", "mesCfmMepDirection"),
        ("LUM-MES-MIB", "mesCfmMepCcmSeqNumStatus"),
        ("LUM-MES-MIB", "mesCfmMepRemoteCsfLos"),
        ("LUM-MES-MIB", "mesCfmMepRemoteCsfRdi"),
        ("LUM-MES-MIB", "mesCfmMepRemoteCsfFdi"),
        ("LUM-MES-MIB", "mesCfmMepLocalCsfLos"),
        ("LUM-MES-MIB", "mesCfmMepLocalDeviceType"),
        ("LUM-MES-MIB", "mesCfmMepLocalDeviceName"),
        ("LUM-MES-MIB", "mesCfmMepLocalDeviceId"),
        ("LUM-MES-MIB", "mesCfmMepViewFilter"),
        ("LUM-MES-MIB", "mesCfmMepUnexpectedPeriod"),
        ("LUM-MES-MIB", "mesCfmMepUnexpectedMepId"),
        ("LUM-MES-MIB", "mesCfmMepUnexpectedMegLevel"),
        ("LUM-MES-MIB", "mesCfmMepMismerge"),
        ("LUM-MES-MIB", "mesCfmMepNoOfLMs"),
        ("LUM-MES-MIB", "mesCfmMepNoOfDMs"),
        ("LUM-MES-MIB", "mesCfmMepTransmitDmrStatus"),
        ("LUM-MES-MIB", "mesCfmMepTransmitLmrStatus"),
        ("LUM-MES-MIB", "mesCfmMepLmCosAwareness"),
        ("LUM-MES-MIB", "mesCfmMepResourceType"),
        ("LUM-MES-MIB", "mesCfmMepLagId"),
        ("LUM-MES-MIB", "mesCfmMepInterfaceName"),
        ("LUM-MES-MIB", "mesCfmMepIfNo"),
        ("LUM-MES-MIB", "mesCfmMepLocalId"))
)
if mibBuilder.loadTexts:
    mesCfmMepGroupV10.setStatus("deprecated")

mesPortGroupV9 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 1, 1, 123)
)
mesPortGroupV9.setObjects(
      *(("LUM-MES-MIB", "mesPortIndex"),
        ("LUM-MES-MIB", "mesPortName"),
        ("LUM-MES-MIB", "mesPortDescr"),
        ("LUM-MES-MIB", "mesPortSubrack"),
        ("LUM-MES-MIB", "mesPortSlot"),
        ("LUM-MES-MIB", "mesPortTxPort"),
        ("LUM-MES-MIB", "mesPortRxPort"),
        ("LUM-MES-MIB", "mesPortAdminStatus"),
        ("LUM-MES-MIB", "mesPortOperStatus"),
        ("LUM-MES-MIB", "mesPortMtuSize"),
        ("LUM-MES-MIB", "mesPortTagType"),
        ("LUM-MES-MIB", "mesPortNoOfVlans"),
        ("LUM-MES-MIB", "mesPortVlanAware"),
        ("LUM-MES-MIB", "mesPortVlanTagged"),
        ("LUM-MES-MIB", "mesPortVlanUntagged"),
        ("LUM-MES-MIB", "mesPortIngressFiltering"),
        ("LUM-MES-MIB", "mesPortEgressTag"),
        ("LUM-MES-MIB", "mesPortDefaultCeVlanId"),
        ("LUM-MES-MIB", "mesPortAssociateVlan"),
        ("LUM-MES-MIB", "mesPortReleaseVlan"),
        ("LUM-MES-MIB", "mesPortActingAsLine"),
        ("LUM-MES-MIB", "mesPortTrustedPortmask"),
        ("LUM-MES-MIB", "mesPortConfigureTrustedPortmask"),
        ("LUM-MES-MIB", "mesPortMacAddress"),
        ("LUM-MES-MIB", "mesPortLagStatus"),
        ("LUM-MES-MIB", "mesPortLagPortmask"),
        ("LUM-MES-MIB", "mesPortAssociateLag"),
        ("LUM-MES-MIB", "mesPortTxEthUtilization"),
        ("LUM-MES-MIB", "mesPortRxEthUtilization"),
        ("LUM-MES-MIB", "mesPortFlowControlMode"),
        ("LUM-MES-MIB", "mesPortAutoNegotiationMode"),
        ("LUM-MES-MIB", "mesPortAutoNegotiationStatus"),
        ("LUM-MES-MIB", "mesPortLinkDown"),
        ("LUM-MES-MIB", "mesPortLinkFaultRemote"),
        ("LUM-MES-MIB", "mesPortLinkFaultLocal"),
        ("LUM-MES-MIB", "mesPortNoOfShapers"),
        ("LUM-MES-MIB", "mesPortNoOfPolicers"),
        ("LUM-MES-MIB", "mesPortAssociateShaper"),
        ("LUM-MES-MIB", "mesPortReleaseShaper"),
        ("LUM-MES-MIB", "mesPortAssociatePolicer"),
        ("LUM-MES-MIB", "mesPortReleasePolicer"),
        ("LUM-MES-MIB", "mesPortRestartAutoNegotiation"),
        ("LUM-MES-MIB", "mesPortConfigureLine"),
        ("LUM-MES-MIB", "mesPortEtherType"),
        ("LUM-MES-MIB", "mesPortConfigureEtherType"),
        ("LUM-MES-MIB", "mesPortNoOfMirrorSources"),
        ("LUM-MES-MIB", "mesPortMirroring"),
        ("LUM-MES-MIB", "mesPortIngressPushTag"),
        ("LUM-MES-MIB", "mesPortEgressPopTag"),
        ("LUM-MES-MIB", "mesPortDefaultCeVlanPriority"),
        ("LUM-MES-MIB", "mesPortConfigureTagRule"),
        ("LUM-MES-MIB", "mesPortCosProfile"),
        ("LUM-MES-MIB", "mesPortMode"),
        ("LUM-MES-MIB", "mesPortPrioAssignment"),
        ("LUM-MES-MIB", "mesPortConfigurePrioAssignment"),
        ("LUM-MES-MIB", "mesPortNoOfTagRules"),
        ("LUM-MES-MIB", "mesPortObjectProperty"),
        ("LUM-MES-MIB", "mesPortHighBitErrorRate"),
        ("LUM-MES-MIB", "mesPortIdx"),
        ("LUM-MES-MIB", "mesPortIfNo"),
        ("LUM-MES-MIB", "mesPortClientIdx"),
        ("LUM-MES-MIB", "mesPortUpPortId"),
        ("LUM-MES-MIB", "mesPortLagPortmaskIf1"),
        ("LUM-MES-MIB", "mesPortLagPortmaskIf2"),
        ("LUM-MES-MIB", "mesPortLagPortmaskIf3"),
        ("LUM-MES-MIB", "mesPortLagPortmaskIf4"),
        ("LUM-MES-MIB", "mesPortLagPortmaskIf5"),
        ("LUM-MES-MIB", "mesPortLagPortmaskIf6"),
        ("LUM-MES-MIB", "mesPortLagPortmaskIf7"),
        ("LUM-MES-MIB", "mesPortLagPortmaskIf8"),
        ("LUM-MES-MIB", "mesPortAutoNegMasterSlaveCfg"),
        ("LUM-MES-MIB", "mesPortAutoNegMasterSlaveStatus"))
)
if mibBuilder.loadTexts:
    mesPortGroupV9.setStatus("deprecated")

mesGeneralGroupV6 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 1, 1, 124)
)
mesGeneralGroupV6.setObjects(
      *(("LUM-MES-MIB", "mesGeneralConfigLastChangeTime"),
        ("LUM-MES-MIB", "mesGeneralStateLastChangeTime"),
        ("LUM-MES-MIB", "mesGeneralUniTableSize"),
        ("LUM-MES-MIB", "mesGeneralNniTableSize"),
        ("LUM-MES-MIB", "mesGeneralEvcTableSize"),
        ("LUM-MES-MIB", "mesGeneralBwpTableSize"),
        ("LUM-MES-MIB", "mesGeneralCeEvcMapTableSize"),
        ("LUM-MES-MIB", "mesGeneralMepTableSize"),
        ("LUM-MES-MIB", "mesGeneralMegTableSize"),
        ("LUM-MES-MIB", "mesGeneralEvcBwpMapTableSize"),
        ("LUM-MES-MIB", "mesGeneralPortTableSize"),
        ("LUM-MES-MIB", "mesGeneralVlanMapTableSize"),
        ("LUM-MES-MIB", "mesGeneralMgmtVlanTableSize"),
        ("LUM-MES-MIB", "mesGeneralLagTableSize"),
        ("LUM-MES-MIB", "mesGeneralPolicingTableSize"),
        ("LUM-MES-MIB", "mesGeneralShapingTableSize"),
        ("LUM-MES-MIB", "mesGeneralBwpMapTableSize"),
        ("LUM-MES-MIB", "mesGeneralCosTableSize"),
        ("LUM-MES-MIB", "mesGeneralErrorPropTableSize"),
        ("LUM-MES-MIB", "mesGeneralLagStateLastChangeTime"),
        ("LUM-MES-MIB", "mesGeneralLagConfigLastChangeTime"),
        ("LUM-MES-MIB", "mesGeneralErpStateLastChangeTime"),
        ("LUM-MES-MIB", "mesGeneralErpConfigLastChangeTime"),
        ("LUM-MES-MIB", "mesGeneralMaidStateLastChangeTime"),
        ("LUM-MES-MIB", "mesGeneralMaidConfigLastChangeTime"),
        ("LUM-MES-MIB", "mesGeneralCfmMepStateLastChangeTime"),
        ("LUM-MES-MIB", "mesGeneralCfmMepConfigLastChangeTime"),
        ("LUM-MES-MIB", "mesGeneralVlanMapStateLastChangeTime"),
        ("LUM-MES-MIB", "mesGeneralVlanMapConfigLastChangeTime"),
        ("LUM-MES-MIB", "mesGeneralMgmtVlanStateLastChangeTime"),
        ("LUM-MES-MIB", "mesGeneralMgmtVlanConfigLastChangeTime"),
        ("LUM-MES-MIB", "mesGeneralClassStateLastChangeTime"),
        ("LUM-MES-MIB", "mesGeneralClassConfigLastChangeTime"),
        ("LUM-MES-MIB", "mesGeneralActionStateLastChangeTime"),
        ("LUM-MES-MIB", "mesGeneralActionConfigLastChangeTime"),
        ("LUM-MES-MIB", "mesGeneralPolicyStateLastChangeTime"),
        ("LUM-MES-MIB", "mesGeneralPolicyConfigLastChangeTime"),
        ("LUM-MES-MIB", "mesGeneralErrorPropStateLastChangeTime"),
        ("LUM-MES-MIB", "mesGeneralErrorPropConfigLastChangeTime"),
        ("LUM-MES-MIB", "mesGeneralVlanProtStateLastChangeTime"),
        ("LUM-MES-MIB", "mesGeneralVlanProtConfigLastChangeTime"),
        ("LUM-MES-MIB", "mesGeneralLacpStateLastChangeTime"),
        ("LUM-MES-MIB", "mesGeneralLacpConfigLastChangeTime"),
        ("LUM-MES-MIB", "mesGeneralPolicingStateLastChangeTime"),
        ("LUM-MES-MIB", "mesGeneralPolicingConfigLastChangeTime"),
        ("LUM-MES-MIB", "mesGeneralShapingStateLastChangeTime"),
        ("LUM-MES-MIB", "mesGeneralShapingConfigLastChangeTime"),
        ("LUM-MES-MIB", "mesGeneralCosStateLastChangeTime"),
        ("LUM-MES-MIB", "mesGeneralCosConfigLastChangeTime"),
        ("LUM-MES-MIB", "mesGeneralBwpMapStateLastChangeTime"),
        ("LUM-MES-MIB", "mesGeneralBwpMapConfigLastChangeTime"),
        ("LUM-MES-MIB", "mesGeneralMirroringStateLastChangeTime"),
        ("LUM-MES-MIB", "mesGeneralMirroringConfigLastChangeTime"),
        ("LUM-MES-MIB", "mesGeneralVlanTagRuleStateLastChangeTime"),
        ("LUM-MES-MIB", "mesGeneralVlanTagRuleConfigLastChangeTime"),
        ("LUM-MES-MIB", "mesGeneralVlanTagClassVlanStateLastChangeTime"),
        ("LUM-MES-MIB", "mesGeneralVlanTagClassVlanConfigLastChangeTime"),
        ("LUM-MES-MIB", "mesGeneralCosProfileStateLastChangeTime"),
        ("LUM-MES-MIB", "mesGeneralCosProfileConfigLastChangeTime"),
        ("LUM-MES-MIB", "mesGeneralBwpStateLastChangeTime"),
        ("LUM-MES-MIB", "mesGeneralBwpConfigLastChangeTime"),
        ("LUM-MES-MIB", "mesGeneralMiscStateLastChangeTime"),
        ("LUM-MES-MIB", "mesGeneralMiscConfigLastChangeTime"),
        ("LUM-MES-MIB", "mesGeneralPortStateLastChangeTime"),
        ("LUM-MES-MIB", "mesGeneralPortConfigLastChangeTime"))
)
if mibBuilder.loadTexts:
    mesGeneralGroupV6.setStatus("current")

mesVlanMapGroupV9 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 1, 1, 125)
)
mesVlanMapGroupV9.setObjects(
      *(("LUM-MES-MIB", "mesVlanMapIndex"),
        ("LUM-MES-MIB", "mesVlanMapName"),
        ("LUM-MES-MIB", "mesVlanMapVlanIdRangeLower"),
        ("LUM-MES-MIB", "mesVlanMapVlanIdRangeUpper"),
        ("LUM-MES-MIB", "mesVlanMapInternalReference"),
        ("LUM-MES-MIB", "mesVlanMapPortmask"),
        ("LUM-MES-MIB", "mesVlanMapConfigurePortMask"),
        ("LUM-MES-MIB", "mesVlanMapLearning"),
        ("LUM-MES-MIB", "mesVlanMapEtherType"),
        ("LUM-MES-MIB", "mesVlanMapRowStatus"),
        ("LUM-MES-MIB", "mesVlanMapDescr"),
        ("LUM-MES-MIB", "mesVlanMapTrustPorts"),
        ("LUM-MES-MIB", "mesVlanMapRings"),
        ("LUM-MES-MIB", "mesVlanMapServiceId"),
        ("LUM-MES-MIB", "mesVlanMapPortmaskIf1"),
        ("LUM-MES-MIB", "mesVlanMapPortmaskIf2"),
        ("LUM-MES-MIB", "mesVlanMapPortmaskIf3"),
        ("LUM-MES-MIB", "mesVlanMapPortmaskIf4"),
        ("LUM-MES-MIB", "mesVlanMapPortmaskIf5"),
        ("LUM-MES-MIB", "mesVlanMapPortmaskIf6"),
        ("LUM-MES-MIB", "mesVlanMapPortmaskIf7"),
        ("LUM-MES-MIB", "mesVlanMapPortmaskIf8"),
        ("LUM-MES-MIB", "mesVlanMapPrepareConfigPortMask"),
        ("LUM-MES-MIB", "mesVlanMapPortmaskIf9"),
        ("LUM-MES-MIB", "mesVlanMapPortmaskIf10"),
        ("LUM-MES-MIB", "mesVlanMapPortmaskIf11"),
        ("LUM-MES-MIB", "mesVlanMapPortmaskIf12"),
        ("LUM-MES-MIB", "mesVlanMapPortmaskIf13"),
        ("LUM-MES-MIB", "mesVlanMapPortmaskIf14"),
        ("LUM-MES-MIB", "mesVlanMapPortmaskIf15"),
        ("LUM-MES-MIB", "mesVlanMapPortmaskIf16"),
        ("LUM-MES-MIB", "mesVlanMapSubrack"),
        ("LUM-MES-MIB", "mesVlanMapSlot"))
)
if mibBuilder.loadTexts:
    mesVlanMapGroupV9.setStatus("deprecated")

mesMirroringGroupV3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 1, 1, 126)
)
mesMirroringGroupV3.setObjects(
      *(("LUM-MES-MIB", "mesMirroringIndex"),
        ("LUM-MES-MIB", "mesMirroringName"),
        ("LUM-MES-MIB", "mesMirroringDestination"),
        ("LUM-MES-MIB", "mesMirroringDirection"),
        ("LUM-MES-MIB", "mesMirroringConfigureDestination"),
        ("LUM-MES-MIB", "mesMirroringDestInterface"),
        ("LUM-MES-MIB", "mesMirroringDestTxPort"),
        ("LUM-MES-MIB", "mesMirroringIfNo"),
        ("LUM-MES-MIB", "mesMirroringTxPort"))
)
if mibBuilder.loadTexts:
    mesMirroringGroupV3.setStatus("current")

mesMiscGroupV10 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 1, 1, 127)
)
mesMiscGroupV10.setObjects(
      *(("LUM-MES-MIB", "mesMiscIndex"),
        ("LUM-MES-MIB", "mesMiscName"),
        ("LUM-MES-MIB", "mesMiscObjectProperty"),
        ("LUM-MES-MIB", "mesMiscAdminStatus"),
        ("LUM-MES-MIB", "mesMiscOperStatus"),
        ("LUM-MES-MIB", "mesMiscMgmtVlanIpAddress"),
        ("LUM-MES-MIB", "mesMiscMgmtVlanNetMask"),
        ("LUM-MES-MIB", "mesMiscMgmtVlanMacAddress0"),
        ("LUM-MES-MIB", "mesMiscMgmtVlanMacAddress1"),
        ("LUM-MES-MIB", "mesMiscMgmtVlanMacAddress2"),
        ("LUM-MES-MIB", "mesMiscConfigureAddress"),
        ("LUM-MES-MIB", "mesMiscMgmtVlanNode"),
        ("LUM-MES-MIB", "mesMiscMacAgeing"),
        ("LUM-MES-MIB", "mesMiscMacGetTable"),
        ("LUM-MES-MIB", "mesMiscNoOfMegs"),
        ("LUM-MES-MIB", "mesMiscAssociateMeg"),
        ("LUM-MES-MIB", "mesMiscNoOfErps"),
        ("LUM-MES-MIB", "mesMiscAssociateErp"),
        ("LUM-MES-MIB", "mesMiscL2Mode"),
        ("LUM-MES-MIB", "mesMiscConfigureMode"),
        ("LUM-MES-MIB", "mesMiscIdentity"),
        ("LUM-MES-MIB", "mesMiscAssociateClass"),
        ("LUM-MES-MIB", "mesMiscAssociateBwp"),
        ("LUM-MES-MIB", "mesMiscWred"),
        ("LUM-MES-MIB", "mesMiscGetPacketMonitor"),
        ("LUM-MES-MIB", "mesMiscSfpPortUsageCurrent"),
        ("LUM-MES-MIB", "mesMiscSfpPortUsageNext"),
        ("LUM-MES-MIB", "mesMiscNoOfErpV2s"),
        ("LUM-MES-MIB", "mesMiscAssociateErpV2"),
        ("LUM-MES-MIB", "mesMiscAssociateVlanProt"),
        ("LUM-MES-MIB", "mesMiscAssociateClassAdvanced"),
        ("LUM-MES-MIB", "mesMiscAssociateErpAdvanced"),
        ("LUM-MES-MIB", "mesMiscAssociateMegAdvanced"),
        ("LUM-MES-MIB", "mesMiscCreateClass"),
        ("LUM-MES-MIB", "mesMiscCreateAction"),
        ("LUM-MES-MIB", "mesMiscCreateMeg"),
        ("LUM-MES-MIB", "mesMiscCreateMep"),
        ("LUM-MES-MIB", "mesMiscCreateErrorProp"),
        ("LUM-MES-MIB", "mesMiscCreatePolicer"))
)
if mibBuilder.loadTexts:
    mesMiscGroupV10.setStatus("current")

mesClassGroupV6 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 1, 1, 128)
)
mesClassGroupV6.setObjects(
      *(("LUM-MES-MIB", "mesClassIndex"),
        ("LUM-MES-MIB", "mesClassName"),
        ("LUM-MES-MIB", "mesClassIdentifier"),
        ("LUM-MES-MIB", "mesClassPort"),
        ("LUM-MES-MIB", "mesClassLagId"),
        ("LUM-MES-MIB", "mesClassInternalReference"),
        ("LUM-MES-MIB", "mesClassOuterVlanId"),
        ("LUM-MES-MIB", "mesClassOuterVlanPcp"),
        ("LUM-MES-MIB", "mesClassPrecedence"),
        ("LUM-MES-MIB", "mesClassDaMacAddress"),
        ("LUM-MES-MIB", "mesClassAssociateAction"),
        ("LUM-MES-MIB", "mesClassRowStatus"),
        ("LUM-MES-MIB", "mesClassDaMacAddressMask"),
        ("LUM-MES-MIB", "mesClassDSCP"),
        ("LUM-MES-MIB", "mesClassInnerVlanId"),
        ("LUM-MES-MIB", "mesClassInnerVlanPcp"),
        ("LUM-MES-MIB", "mesClassInnerVlanCfi"),
        ("LUM-MES-MIB", "mesClassOuterVlanCfi"),
        ("LUM-MES-MIB", "mesClassDirection"),
        ("LUM-MES-MIB", "mesClassOuterTpid"),
        ("LUM-MES-MIB", "mesClassInternalClassId"),
        ("LUM-MES-MIB", "mesClassSourceAddressIPV4"),
        ("LUM-MES-MIB", "mesClassSourceMaskIPV4"),
        ("LUM-MES-MIB", "mesClassDestAddressIPV4"),
        ("LUM-MES-MIB", "mesClassDestMaskIPV4"),
        ("LUM-MES-MIB", "mesClassSubrack"),
        ("LUM-MES-MIB", "mesClassSlot"),
        ("LUM-MES-MIB", "mesClassVlanStackStructure"),
        ("LUM-MES-MIB", "mesClassServiceId"),
        ("LUM-MES-MIB", "mesClassIfNo"),
        ("LUM-MES-MIB", "mesClassTxPort"),
        ("LUM-MES-MIB", "mesClassAssociateActionAdvanced"))
)
if mibBuilder.loadTexts:
    mesClassGroupV6.setStatus("current")

mesMaidGroupV6 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 1, 1, 129)
)
mesMaidGroupV6.setObjects(
      *(("LUM-MES-MIB", "mesMaidIndex"),
        ("LUM-MES-MIB", "mesMaidName"),
        ("LUM-MES-MIB", "mesMaidGroupId"),
        ("LUM-MES-MIB", "mesMaidMdFormat"),
        ("LUM-MES-MIB", "mesMaidMdName"),
        ("LUM-MES-MIB", "mesMaidMdMac"),
        ("LUM-MES-MIB", "mesMaidMd2Octet"),
        ("LUM-MES-MIB", "mesMaidMdString"),
        ("LUM-MES-MIB", "mesMaidLevel"),
        ("LUM-MES-MIB", "mesMaidMaFormat"),
        ("LUM-MES-MIB", "mesMaidMaName"),
        ("LUM-MES-MIB", "mesMaidMaVpnOui"),
        ("LUM-MES-MIB", "mesMaidMaVpnIndex"),
        ("LUM-MES-MIB", "mesMaidMa2Octet"),
        ("LUM-MES-MIB", "mesMaidMaVlan"),
        ("LUM-MES-MIB", "mesMaidMaString"),
        ("LUM-MES-MIB", "mesMaidCcmInterval"),
        ("LUM-MES-MIB", "mesMaidInternalReference"),
        ("LUM-MES-MIB", "mesMaidIdentifier"),
        ("LUM-MES-MIB", "mesMaidNoOfMeps"),
        ("LUM-MES-MIB", "mesMaidAssociateMep"),
        ("LUM-MES-MIB", "mesMaidReleaseMeps"),
        ("LUM-MES-MIB", "mesMaidRowStatus"),
        ("LUM-MES-MIB", "mesMaidNoOfUpMeps"),
        ("LUM-MES-MIB", "mesMaidNoOfNidMeps"),
        ("LUM-MES-MIB", "mesMaidLocalDeviceType"),
        ("LUM-MES-MIB", "mesMaidViewFilter"),
        ("LUM-MES-MIB", "mesMaidAssociateMepNid"),
        ("LUM-MES-MIB", "mesMaidAssociateMepAdvanced"),
        ("LUM-MES-MIB", "mesMaidSubrack"),
        ("LUM-MES-MIB", "mesMaidSlot"),
        ("LUM-MES-MIB", "mesMaidServiceId"))
)
if mibBuilder.loadTexts:
    mesMaidGroupV6.setStatus("current")

mesPortGroupV10 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 1, 1, 130)
)
mesPortGroupV10.setObjects(
      *(("LUM-MES-MIB", "mesPortIndex"),
        ("LUM-MES-MIB", "mesPortName"),
        ("LUM-MES-MIB", "mesPortDescr"),
        ("LUM-MES-MIB", "mesPortSubrack"),
        ("LUM-MES-MIB", "mesPortSlot"),
        ("LUM-MES-MIB", "mesPortTxPort"),
        ("LUM-MES-MIB", "mesPortRxPort"),
        ("LUM-MES-MIB", "mesPortAdminStatus"),
        ("LUM-MES-MIB", "mesPortOperStatus"),
        ("LUM-MES-MIB", "mesPortMtuSize"),
        ("LUM-MES-MIB", "mesPortTagType"),
        ("LUM-MES-MIB", "mesPortNoOfVlans"),
        ("LUM-MES-MIB", "mesPortVlanAware"),
        ("LUM-MES-MIB", "mesPortVlanTagged"),
        ("LUM-MES-MIB", "mesPortVlanUntagged"),
        ("LUM-MES-MIB", "mesPortIngressFiltering"),
        ("LUM-MES-MIB", "mesPortEgressTag"),
        ("LUM-MES-MIB", "mesPortDefaultCeVlanId"),
        ("LUM-MES-MIB", "mesPortAssociateVlan"),
        ("LUM-MES-MIB", "mesPortReleaseVlan"),
        ("LUM-MES-MIB", "mesPortActingAsLine"),
        ("LUM-MES-MIB", "mesPortTrustedPortmask"),
        ("LUM-MES-MIB", "mesPortConfigureTrustedPortmask"),
        ("LUM-MES-MIB", "mesPortMacAddress"),
        ("LUM-MES-MIB", "mesPortLagStatus"),
        ("LUM-MES-MIB", "mesPortLagPortmask"),
        ("LUM-MES-MIB", "mesPortAssociateLag"),
        ("LUM-MES-MIB", "mesPortTxEthUtilization"),
        ("LUM-MES-MIB", "mesPortRxEthUtilization"),
        ("LUM-MES-MIB", "mesPortFlowControlMode"),
        ("LUM-MES-MIB", "mesPortAutoNegotiationMode"),
        ("LUM-MES-MIB", "mesPortAutoNegotiationStatus"),
        ("LUM-MES-MIB", "mesPortLinkDown"),
        ("LUM-MES-MIB", "mesPortLinkFaultRemote"),
        ("LUM-MES-MIB", "mesPortLinkFaultLocal"),
        ("LUM-MES-MIB", "mesPortNoOfShapers"),
        ("LUM-MES-MIB", "mesPortNoOfPolicers"),
        ("LUM-MES-MIB", "mesPortAssociateShaper"),
        ("LUM-MES-MIB", "mesPortReleaseShaper"),
        ("LUM-MES-MIB", "mesPortAssociatePolicer"),
        ("LUM-MES-MIB", "mesPortReleasePolicer"),
        ("LUM-MES-MIB", "mesPortRestartAutoNegotiation"),
        ("LUM-MES-MIB", "mesPortConfigureLine"),
        ("LUM-MES-MIB", "mesPortEtherType"),
        ("LUM-MES-MIB", "mesPortConfigureEtherType"),
        ("LUM-MES-MIB", "mesPortNoOfMirrorSources"),
        ("LUM-MES-MIB", "mesPortMirroring"),
        ("LUM-MES-MIB", "mesPortIngressPushTag"),
        ("LUM-MES-MIB", "mesPortEgressPopTag"),
        ("LUM-MES-MIB", "mesPortDefaultCeVlanPriority"),
        ("LUM-MES-MIB", "mesPortConfigureTagRule"),
        ("LUM-MES-MIB", "mesPortCosProfile"),
        ("LUM-MES-MIB", "mesPortMode"),
        ("LUM-MES-MIB", "mesPortPrioAssignment"),
        ("LUM-MES-MIB", "mesPortConfigurePrioAssignment"),
        ("LUM-MES-MIB", "mesPortNoOfTagRules"),
        ("LUM-MES-MIB", "mesPortObjectProperty"),
        ("LUM-MES-MIB", "mesPortHighBitErrorRate"),
        ("LUM-MES-MIB", "mesPortIdx"),
        ("LUM-MES-MIB", "mesPortIfNo"),
        ("LUM-MES-MIB", "mesPortClientIdx"),
        ("LUM-MES-MIB", "mesPortUpPortId"),
        ("LUM-MES-MIB", "mesPortLagPortmaskIf1"),
        ("LUM-MES-MIB", "mesPortLagPortmaskIf2"),
        ("LUM-MES-MIB", "mesPortLagPortmaskIf3"),
        ("LUM-MES-MIB", "mesPortLagPortmaskIf4"),
        ("LUM-MES-MIB", "mesPortLagPortmaskIf5"),
        ("LUM-MES-MIB", "mesPortLagPortmaskIf6"),
        ("LUM-MES-MIB", "mesPortLagPortmaskIf7"),
        ("LUM-MES-MIB", "mesPortLagPortmaskIf8"),
        ("LUM-MES-MIB", "mesPortAutoNegMasterSlaveCfg"),
        ("LUM-MES-MIB", "mesPortAutoNegMasterSlaveStatus"),
        ("LUM-MES-MIB", "mesPortLagPortmaskIf9"),
        ("LUM-MES-MIB", "mesPortLagPortmaskIf10"),
        ("LUM-MES-MIB", "mesPortLagPortmaskIf11"),
        ("LUM-MES-MIB", "mesPortLagPortmaskIf12"),
        ("LUM-MES-MIB", "mesPortLagPortmaskIf13"),
        ("LUM-MES-MIB", "mesPortLagPortmaskIf14"),
        ("LUM-MES-MIB", "mesPortLagPortmaskIf15"),
        ("LUM-MES-MIB", "mesPortLagPortmaskIf16"),
        ("LUM-MES-MIB", "mesPortCreateVlanTagClass"),
        ("LUM-MES-MIB", "mesPortCreateTagRuleWoutClass"))
)
if mibBuilder.loadTexts:
    mesPortGroupV10.setStatus("deprecated")

mesCosProfileGroupV4 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 1, 1, 131)
)
mesCosProfileGroupV4.setObjects(
      *(("LUM-MES-MIB", "mesCosProfileIndex"),
        ("LUM-MES-MIB", "mesCosProfileName"),
        ("LUM-MES-MIB", "mesCosProfilePortmask"),
        ("LUM-MES-MIB", "mesCosProfilePortmaskIf1"),
        ("LUM-MES-MIB", "mesCosProfilePortmaskIf2"),
        ("LUM-MES-MIB", "mesCosProfilePortmaskIf3"),
        ("LUM-MES-MIB", "mesCosProfilePortmaskIf4"),
        ("LUM-MES-MIB", "mesCosProfilePortmaskIf5"),
        ("LUM-MES-MIB", "mesCosProfilePortmaskIf6"),
        ("LUM-MES-MIB", "mesCosProfilePortmaskIf7"),
        ("LUM-MES-MIB", "mesCosProfilePortmaskIf8"),
        ("LUM-MES-MIB", "mesCosProfileScheduler"),
        ("LUM-MES-MIB", "mesCosProfileWeight0"),
        ("LUM-MES-MIB", "mesCosProfileWeight1"),
        ("LUM-MES-MIB", "mesCosProfileWeight2"),
        ("LUM-MES-MIB", "mesCosProfileWeight3"),
        ("LUM-MES-MIB", "mesCosProfileWeight4"),
        ("LUM-MES-MIB", "mesCosProfileWeight5"),
        ("LUM-MES-MIB", "mesCosProfileWeight6"),
        ("LUM-MES-MIB", "mesCosProfileWeight7"),
        ("LUM-MES-MIB", "mesCosProfilePriority0"),
        ("LUM-MES-MIB", "mesCosProfilePriority1"),
        ("LUM-MES-MIB", "mesCosProfilePriority2"),
        ("LUM-MES-MIB", "mesCosProfilePriority3"),
        ("LUM-MES-MIB", "mesCosProfilePriority4"),
        ("LUM-MES-MIB", "mesCosProfilePriority5"),
        ("LUM-MES-MIB", "mesCosProfilePriority6"),
        ("LUM-MES-MIB", "mesCosProfilePriority7"),
        ("LUM-MES-MIB", "mesCosProfileConfigureScheduler"),
        ("LUM-MES-MIB", "mesCosProfileIngressPcpDecoding"),
        ("LUM-MES-MIB", "mesCosProfileIngressDeiDecoding"),
        ("LUM-MES-MIB", "mesCosProfileIngressColor0"),
        ("LUM-MES-MIB", "mesCosProfileIngressColor1"),
        ("LUM-MES-MIB", "mesCosProfileIngressColor2"),
        ("LUM-MES-MIB", "mesCosProfileIngressColor3"),
        ("LUM-MES-MIB", "mesCosProfileIngressColor4"),
        ("LUM-MES-MIB", "mesCosProfileIngressColor5"),
        ("LUM-MES-MIB", "mesCosProfileIngressColor6"),
        ("LUM-MES-MIB", "mesCosProfileIngressColor7"),
        ("LUM-MES-MIB", "mesCosProfileEgressPcpEncoding"),
        ("LUM-MES-MIB", "mesCosProfileEgressDeiEncoding"),
        ("LUM-MES-MIB", "mesCosProfileEgressPcpGreen0"),
        ("LUM-MES-MIB", "mesCosProfileEgressPcpGreen1"),
        ("LUM-MES-MIB", "mesCosProfileEgressPcpGreen2"),
        ("LUM-MES-MIB", "mesCosProfileEgressPcpGreen3"),
        ("LUM-MES-MIB", "mesCosProfileEgressPcpGreen4"),
        ("LUM-MES-MIB", "mesCosProfileEgressPcpGreen5"),
        ("LUM-MES-MIB", "mesCosProfileEgressPcpGreen6"),
        ("LUM-MES-MIB", "mesCosProfileEgressPcpGreen7"),
        ("LUM-MES-MIB", "mesCosProfileEgressPcpYellow0"),
        ("LUM-MES-MIB", "mesCosProfileEgressPcpYellow1"),
        ("LUM-MES-MIB", "mesCosProfileEgressPcpYellow2"),
        ("LUM-MES-MIB", "mesCosProfileEgressPcpYellow3"),
        ("LUM-MES-MIB", "mesCosProfileEgressPcpYellow4"),
        ("LUM-MES-MIB", "mesCosProfileEgressPcpYellow5"),
        ("LUM-MES-MIB", "mesCosProfileEgressPcpYellow6"),
        ("LUM-MES-MIB", "mesCosProfileEgressPcpYellow7"))
)
if mibBuilder.loadTexts:
    mesCosProfileGroupV4.setStatus("current")

mesLagGroupV9 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 1, 1, 132)
)
mesLagGroupV9.setObjects(
      *(("LUM-MES-MIB", "mesLagIndex"),
        ("LUM-MES-MIB", "mesLagName"),
        ("LUM-MES-MIB", "mesLagInternalReference"),
        ("LUM-MES-MIB", "mesLagPortmask"),
        ("LUM-MES-MIB", "mesLagMasterIndex"),
        ("LUM-MES-MIB", "mesLagConfigure"),
        ("LUM-MES-MIB", "mesLagHash"),
        ("LUM-MES-MIB", "mesLagIdentifier"),
        ("LUM-MES-MIB", "mesLagRowStatus"),
        ("LUM-MES-MIB", "mesLagLacpEnabled"),
        ("LUM-MES-MIB", "mesLagLacpSystemPriority"),
        ("LUM-MES-MIB", "mesLagLacpPeriod"),
        ("LUM-MES-MIB", "mesLagLacpLinkProtection"),
        ("LUM-MES-MIB", "mesLagDegraded"),
        ("LUM-MES-MIB", "mesLagFailure"),
        ("LUM-MES-MIB", "mesLagLacpMaxNumberOfActiveLinks"),
        ("LUM-MES-MIB", "mesLagNoOfPorts"),
        ("LUM-MES-MIB", "mesLagLacpMinNumberOfActiveLinks"),
        ("LUM-MES-MIB", "mesLagIsMcLag"),
        ("LUM-MES-MIB", "mesLagConfigureTagRule"),
        ("LUM-MES-MIB", "mesLagNoOfTagRules"),
        ("LUM-MES-MIB", "mesLagDescr"),
        ("LUM-MES-MIB", "mesLagAdminStatus"),
        ("LUM-MES-MIB", "mesLagOperStatus"),
        ("LUM-MES-MIB", "mesLagPortmaskIf1"),
        ("LUM-MES-MIB", "mesLagPortmaskIf2"),
        ("LUM-MES-MIB", "mesLagPortmaskIf3"),
        ("LUM-MES-MIB", "mesLagPortmaskIf4"),
        ("LUM-MES-MIB", "mesLagPortmaskIf5"),
        ("LUM-MES-MIB", "mesLagPortmaskIf6"),
        ("LUM-MES-MIB", "mesLagPortmaskIf7"),
        ("LUM-MES-MIB", "mesLagPortmaskIf8"),
        ("LUM-MES-MIB", "mesLagMasterIfNo"),
        ("LUM-MES-MIB", "mesLagMasterTxPort"),
        ("LUM-MES-MIB", "mesLagLocalId"),
        ("LUM-MES-MIB", "mesLagPrepareConfigPortMask"),
        ("LUM-MES-MIB", "mesLagPortmaskIf9"),
        ("LUM-MES-MIB", "mesLagPortmaskIf10"),
        ("LUM-MES-MIB", "mesLagPortmaskIf11"),
        ("LUM-MES-MIB", "mesLagPortmaskIf12"),
        ("LUM-MES-MIB", "mesLagPortmaskIf13"),
        ("LUM-MES-MIB", "mesLagPortmaskIf14"),
        ("LUM-MES-MIB", "mesLagPortmaskIf15"),
        ("LUM-MES-MIB", "mesLagPortmaskIf16"),
        ("LUM-MES-MIB", "mesLagServiceId"))
)
if mibBuilder.loadTexts:
    mesLagGroupV9.setStatus("current")

mesVlanTagClassVlanGroupV5 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 1, 1, 133)
)
mesVlanTagClassVlanGroupV5.setObjects(
      *(("LUM-MES-MIB", "mesVlanTagClassVlanIndex"),
        ("LUM-MES-MIB", "mesVlanTagClassVlanName"),
        ("LUM-MES-MIB", "mesVlanTagClassVlanTxPort"),
        ("LUM-MES-MIB", "mesVlanTagClassVlanInternalReference"),
        ("LUM-MES-MIB", "mesVlanTagClassVlanRuleName"),
        ("LUM-MES-MIB", "mesVlanTagClassVlanRuleIndex"),
        ("LUM-MES-MIB", "mesVlanTagClassVlanOuterVlanId"),
        ("LUM-MES-MIB", "mesVlanTagClassVlanLagIndex"),
        ("LUM-MES-MIB", "mesVlanTagClassVlanIfNo"),
        ("LUM-MES-MIB", "mesVlanTagClassVlanLocalId"),
        ("LUM-MES-MIB", "mesVlanTagClassVlanRowStatus"))
)
if mibBuilder.loadTexts:
    mesVlanTagClassVlanGroupV5.setStatus("current")

mesActionGroupV4 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 1, 1, 134)
)
mesActionGroupV4.setObjects(
      *(("LUM-MES-MIB", "mesActionIndex"),
        ("LUM-MES-MIB", "mesActionName"),
        ("LUM-MES-MIB", "mesActionIdentifier"),
        ("LUM-MES-MIB", "mesActionInternalReference"),
        ("LUM-MES-MIB", "mesActionType"),
        ("LUM-MES-MIB", "mesActionOuterVlanId"),
        ("LUM-MES-MIB", "mesActionPcp"),
        ("LUM-MES-MIB", "mesActionPolicerId"),
        ("LUM-MES-MIB", "mesActionInnerVlanId"),
        ("LUM-MES-MIB", "mesActionQueue"),
        ("LUM-MES-MIB", "mesActionRowStatus"),
        ("LUM-MES-MIB", "mesActionRedirectPort"),
        ("LUM-MES-MIB", "mesActionServiceId"),
        ("LUM-MES-MIB", "mesActionRedirectIfNo"),
        ("LUM-MES-MIB", "mesActionRedirectTxPort"),
        ("LUM-MES-MIB", "mesActionClassId"),
        ("LUM-MES-MIB", "mesActionSubrack"),
        ("LUM-MES-MIB", "mesActionSlot"))
)
if mibBuilder.loadTexts:
    mesActionGroupV4.setStatus("current")

mesErrorPropGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 1, 1, 135)
)
mesErrorPropGroupV2.setObjects(
      *(("LUM-MES-MIB", "mesErrorPropIndex"),
        ("LUM-MES-MIB", "mesErrorPropName"),
        ("LUM-MES-MIB", "mesErrorPropDescr"),
        ("LUM-MES-MIB", "mesErrorPropInternalReference"),
        ("LUM-MES-MIB", "mesErrorPropAdminStatus"),
        ("LUM-MES-MIB", "mesErrorPropOperStatus"),
        ("LUM-MES-MIB", "mesErrorPropState"),
        ("LUM-MES-MIB", "mesErrorPropTriggerType"),
        ("LUM-MES-MIB", "mesErrorPropTriggerObject"),
        ("LUM-MES-MIB", "mesErrorPropTriggerPortIndex"),
        ("LUM-MES-MIB", "mesErrorPropTriggerMepIndex"),
        ("LUM-MES-MIB", "mesErrorPropActionType"),
        ("LUM-MES-MIB", "mesErrorPropActionObject"),
        ("LUM-MES-MIB", "mesErrorPropActionPortIndex"),
        ("LUM-MES-MIB", "mesErrorPropActionMepIndex"),
        ("LUM-MES-MIB", "mesErrorPropHoldOffTimer"),
        ("LUM-MES-MIB", "mesErrorPropRowStatus"),
        ("LUM-MES-MIB", "mesErrorPropFault"),
        ("LUM-MES-MIB", "mesErrorPropSubrack"),
        ("LUM-MES-MIB", "mesErrorPropSlot"),
        ("LUM-MES-MIB", "mesErrorPropServiceId"))
)
if mibBuilder.loadTexts:
    mesErrorPropGroupV2.setStatus("current")

mesBwpGroupV5 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 1, 1, 136)
)
mesBwpGroupV5.setObjects(
      *(("LUM-MES-MIB", "mesBwpIndex"),
        ("LUM-MES-MIB", "mesBwpName"),
        ("LUM-MES-MIB", "mesBwpObjectProperty"),
        ("LUM-MES-MIB", "mesBwpCoSIdentifier"),
        ("LUM-MES-MIB", "mesBwpCir"),
        ("LUM-MES-MIB", "mesBwpCbs"),
        ("LUM-MES-MIB", "mesBwpEir"),
        ("LUM-MES-MIB", "mesBwpEbs"),
        ("LUM-MES-MIB", "mesBwpCouplingFlag"),
        ("LUM-MES-MIB", "mesBwpColorMode"),
        ("LUM-MES-MIB", "mesBwpInternalReference"),
        ("LUM-MES-MIB", "mesBwpRowStatus"),
        ("LUM-MES-MIB", "mesBwpServiceId"),
        ("LUM-MES-MIB", "mesBwpPolicerId"),
        ("LUM-MES-MIB", "mesBwpSubrack"),
        ("LUM-MES-MIB", "mesBwpSlot"))
)
if mibBuilder.loadTexts:
    mesBwpGroupV5.setStatus("current")

mesPortGroupV11 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 1, 1, 137)
)
mesPortGroupV11.setObjects(
      *(("LUM-MES-MIB", "mesPortIndex"),
        ("LUM-MES-MIB", "mesPortName"),
        ("LUM-MES-MIB", "mesPortDescr"),
        ("LUM-MES-MIB", "mesPortSubrack"),
        ("LUM-MES-MIB", "mesPortSlot"),
        ("LUM-MES-MIB", "mesPortTxPort"),
        ("LUM-MES-MIB", "mesPortRxPort"),
        ("LUM-MES-MIB", "mesPortAdminStatus"),
        ("LUM-MES-MIB", "mesPortOperStatus"),
        ("LUM-MES-MIB", "mesPortMtuSize"),
        ("LUM-MES-MIB", "mesPortTagType"),
        ("LUM-MES-MIB", "mesPortNoOfVlans"),
        ("LUM-MES-MIB", "mesPortVlanAware"),
        ("LUM-MES-MIB", "mesPortVlanTagged"),
        ("LUM-MES-MIB", "mesPortVlanUntagged"),
        ("LUM-MES-MIB", "mesPortIngressFiltering"),
        ("LUM-MES-MIB", "mesPortEgressTag"),
        ("LUM-MES-MIB", "mesPortDefaultCeVlanId"),
        ("LUM-MES-MIB", "mesPortAssociateVlan"),
        ("LUM-MES-MIB", "mesPortReleaseVlan"),
        ("LUM-MES-MIB", "mesPortActingAsLine"),
        ("LUM-MES-MIB", "mesPortTrustedPortmask"),
        ("LUM-MES-MIB", "mesPortConfigureTrustedPortmask"),
        ("LUM-MES-MIB", "mesPortMacAddress"),
        ("LUM-MES-MIB", "mesPortLagStatus"),
        ("LUM-MES-MIB", "mesPortLagPortmask"),
        ("LUM-MES-MIB", "mesPortAssociateLag"),
        ("LUM-MES-MIB", "mesPortTxEthUtilization"),
        ("LUM-MES-MIB", "mesPortRxEthUtilization"),
        ("LUM-MES-MIB", "mesPortFlowControlMode"),
        ("LUM-MES-MIB", "mesPortAutoNegotiationMode"),
        ("LUM-MES-MIB", "mesPortAutoNegotiationStatus"),
        ("LUM-MES-MIB", "mesPortLinkDown"),
        ("LUM-MES-MIB", "mesPortLinkFaultRemote"),
        ("LUM-MES-MIB", "mesPortLinkFaultLocal"),
        ("LUM-MES-MIB", "mesPortNoOfShapers"),
        ("LUM-MES-MIB", "mesPortNoOfPolicers"),
        ("LUM-MES-MIB", "mesPortAssociateShaper"),
        ("LUM-MES-MIB", "mesPortReleaseShaper"),
        ("LUM-MES-MIB", "mesPortAssociatePolicer"),
        ("LUM-MES-MIB", "mesPortReleasePolicer"),
        ("LUM-MES-MIB", "mesPortRestartAutoNegotiation"),
        ("LUM-MES-MIB", "mesPortConfigureLine"),
        ("LUM-MES-MIB", "mesPortEtherType"),
        ("LUM-MES-MIB", "mesPortConfigureEtherType"),
        ("LUM-MES-MIB", "mesPortNoOfMirrorSources"),
        ("LUM-MES-MIB", "mesPortMirroring"),
        ("LUM-MES-MIB", "mesPortIngressPushTag"),
        ("LUM-MES-MIB", "mesPortEgressPopTag"),
        ("LUM-MES-MIB", "mesPortDefaultCeVlanPriority"),
        ("LUM-MES-MIB", "mesPortConfigureTagRule"),
        ("LUM-MES-MIB", "mesPortCosProfile"),
        ("LUM-MES-MIB", "mesPortMode"),
        ("LUM-MES-MIB", "mesPortPrioAssignment"),
        ("LUM-MES-MIB", "mesPortConfigurePrioAssignment"),
        ("LUM-MES-MIB", "mesPortNoOfTagRules"),
        ("LUM-MES-MIB", "mesPortObjectProperty"),
        ("LUM-MES-MIB", "mesPortHighBitErrorRate"),
        ("LUM-MES-MIB", "mesPortIdx"),
        ("LUM-MES-MIB", "mesPortIfNo"),
        ("LUM-MES-MIB", "mesPortClientIdx"),
        ("LUM-MES-MIB", "mesPortUpPortId"),
        ("LUM-MES-MIB", "mesPortLagPortmaskIf1"),
        ("LUM-MES-MIB", "mesPortLagPortmaskIf2"),
        ("LUM-MES-MIB", "mesPortLagPortmaskIf3"),
        ("LUM-MES-MIB", "mesPortLagPortmaskIf4"),
        ("LUM-MES-MIB", "mesPortLagPortmaskIf5"),
        ("LUM-MES-MIB", "mesPortLagPortmaskIf6"),
        ("LUM-MES-MIB", "mesPortLagPortmaskIf7"),
        ("LUM-MES-MIB", "mesPortLagPortmaskIf8"),
        ("LUM-MES-MIB", "mesPortAutoNegMasterSlaveCfg"),
        ("LUM-MES-MIB", "mesPortAutoNegMasterSlaveStatus"),
        ("LUM-MES-MIB", "mesPortLagPortmaskIf9"),
        ("LUM-MES-MIB", "mesPortLagPortmaskIf10"),
        ("LUM-MES-MIB", "mesPortLagPortmaskIf11"),
        ("LUM-MES-MIB", "mesPortLagPortmaskIf12"),
        ("LUM-MES-MIB", "mesPortLagPortmaskIf13"),
        ("LUM-MES-MIB", "mesPortLagPortmaskIf14"),
        ("LUM-MES-MIB", "mesPortLagPortmaskIf15"),
        ("LUM-MES-MIB", "mesPortLagPortmaskIf16"),
        ("LUM-MES-MIB", "mesPortCreateVlanTagClass"),
        ("LUM-MES-MIB", "mesPortCreateTagRuleWoutClass"),
        ("LUM-MES-MIB", "mesPortTrustedPortmaskIf2"),
        ("LUM-MES-MIB", "mesPortTrustedPortmaskIf3"),
        ("LUM-MES-MIB", "mesPortTrustedPortmaskIf4"),
        ("LUM-MES-MIB", "mesPortTrustedPortmaskIf5"),
        ("LUM-MES-MIB", "mesPortTrustedPortmaskIf6"),
        ("LUM-MES-MIB", "mesPortTrustedPortmaskIf7"),
        ("LUM-MES-MIB", "mesPortTrustedPortmaskIf8"),
        ("LUM-MES-MIB", "mesPortTrustedPortmaskIf9"),
        ("LUM-MES-MIB", "mesPortTrustedPortmaskIf10"),
        ("LUM-MES-MIB", "mesPortTrustedPortmaskIf11"),
        ("LUM-MES-MIB", "mesPortTrustedPortmaskIf12"),
        ("LUM-MES-MIB", "mesPortTrustedPortmaskIf13"),
        ("LUM-MES-MIB", "mesPortTrustedPortmaskIf14"),
        ("LUM-MES-MIB", "mesPortTrustedPortmaskIf15"),
        ("LUM-MES-MIB", "mesPortTrustedPortmaskIf16"),
        ("LUM-MES-MIB", "mesPortServiceId"))
)
if mibBuilder.loadTexts:
    mesPortGroupV11.setStatus("current")

mesCfmMepGroupV11 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 1, 1, 138)
)
mesCfmMepGroupV11.setObjects(
      *(("LUM-MES-MIB", "mesCfmMepIndex"),
        ("LUM-MES-MIB", "mesCfmMepName"),
        ("LUM-MES-MIB", "mesCfmMepMaid"),
        ("LUM-MES-MIB", "mesCfmMepTxPort"),
        ("LUM-MES-MIB", "mesCfmMepPortName"),
        ("LUM-MES-MIB", "mesCfmMepPrimaryVid"),
        ("LUM-MES-MIB", "mesCfmMepAdminStatus"),
        ("LUM-MES-MIB", "mesCfmMepOperStatus"),
        ("LUM-MES-MIB", "mesCfmMepVlanPriority"),
        ("LUM-MES-MIB", "mesCfmMepType"),
        ("LUM-MES-MIB", "mesCfmMepIdentifier"),
        ("LUM-MES-MIB", "mesCfmMepInternalReference"),
        ("LUM-MES-MIB", "mesCfmMepRDICCM"),
        ("LUM-MES-MIB", "mesCfmMepMACstatus"),
        ("LUM-MES-MIB", "mesCfmMepRemoteCCM"),
        ("LUM-MES-MIB", "mesCfmMepErrorCCM"),
        ("LUM-MES-MIB", "mesCfmMepXconCCM"),
        ("LUM-MES-MIB", "mesCfmMepAis"),
        ("LUM-MES-MIB", "mesCfmMepTransmitLbrStatus"),
        ("LUM-MES-MIB", "mesCfmMepRowStatus"),
        ("LUM-MES-MIB", "mesCfmMepDirection"),
        ("LUM-MES-MIB", "mesCfmMepCcmSeqNumStatus"),
        ("LUM-MES-MIB", "mesCfmMepRemoteCsfLos"),
        ("LUM-MES-MIB", "mesCfmMepRemoteCsfRdi"),
        ("LUM-MES-MIB", "mesCfmMepRemoteCsfFdi"),
        ("LUM-MES-MIB", "mesCfmMepLocalCsfLos"),
        ("LUM-MES-MIB", "mesCfmMepLocalDeviceType"),
        ("LUM-MES-MIB", "mesCfmMepLocalDeviceName"),
        ("LUM-MES-MIB", "mesCfmMepLocalDeviceId"),
        ("LUM-MES-MIB", "mesCfmMepViewFilter"),
        ("LUM-MES-MIB", "mesCfmMepUnexpectedPeriod"),
        ("LUM-MES-MIB", "mesCfmMepUnexpectedMepId"),
        ("LUM-MES-MIB", "mesCfmMepUnexpectedMegLevel"),
        ("LUM-MES-MIB", "mesCfmMepMismerge"),
        ("LUM-MES-MIB", "mesCfmMepNoOfLMs"),
        ("LUM-MES-MIB", "mesCfmMepNoOfDMs"),
        ("LUM-MES-MIB", "mesCfmMepTransmitDmrStatus"),
        ("LUM-MES-MIB", "mesCfmMepTransmitLmrStatus"),
        ("LUM-MES-MIB", "mesCfmMepLmCosAwareness"),
        ("LUM-MES-MIB", "mesCfmMepResourceType"),
        ("LUM-MES-MIB", "mesCfmMepLagId"),
        ("LUM-MES-MIB", "mesCfmMepInterfaceName"),
        ("LUM-MES-MIB", "mesCfmMepIfNo"),
        ("LUM-MES-MIB", "mesCfmMepLocalId"),
        ("LUM-MES-MIB", "mesCfmMepSubrack"),
        ("LUM-MES-MIB", "mesCfmMepSlot"),
        ("LUM-MES-MIB", "mesCfmMepServiceId"))
)
if mibBuilder.loadTexts:
    mesCfmMepGroupV11.setStatus("current")

mesVlanMapGroupV10 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 1, 1, 139)
)
mesVlanMapGroupV10.setObjects(
      *(("LUM-MES-MIB", "mesVlanMapIndex"),
        ("LUM-MES-MIB", "mesVlanMapName"),
        ("LUM-MES-MIB", "mesVlanMapVlanIdRangeLower"),
        ("LUM-MES-MIB", "mesVlanMapVlanIdRangeUpper"),
        ("LUM-MES-MIB", "mesVlanMapInternalReference"),
        ("LUM-MES-MIB", "mesVlanMapPortmask"),
        ("LUM-MES-MIB", "mesVlanMapConfigurePortMask"),
        ("LUM-MES-MIB", "mesVlanMapLearning"),
        ("LUM-MES-MIB", "mesVlanMapEtherType"),
        ("LUM-MES-MIB", "mesVlanMapRowStatus"),
        ("LUM-MES-MIB", "mesVlanMapDescr"),
        ("LUM-MES-MIB", "mesVlanMapTrustPorts"),
        ("LUM-MES-MIB", "mesVlanMapRings"),
        ("LUM-MES-MIB", "mesVlanMapServiceId"),
        ("LUM-MES-MIB", "mesVlanMapPortmaskIf1"),
        ("LUM-MES-MIB", "mesVlanMapPortmaskIf2"),
        ("LUM-MES-MIB", "mesVlanMapPortmaskIf3"),
        ("LUM-MES-MIB", "mesVlanMapPortmaskIf4"),
        ("LUM-MES-MIB", "mesVlanMapPortmaskIf5"),
        ("LUM-MES-MIB", "mesVlanMapPortmaskIf6"),
        ("LUM-MES-MIB", "mesVlanMapPortmaskIf7"),
        ("LUM-MES-MIB", "mesVlanMapPortmaskIf8"),
        ("LUM-MES-MIB", "mesVlanMapPrepareConfigPortMask"),
        ("LUM-MES-MIB", "mesVlanMapPortmaskIf9"),
        ("LUM-MES-MIB", "mesVlanMapPortmaskIf10"),
        ("LUM-MES-MIB", "mesVlanMapPortmaskIf11"),
        ("LUM-MES-MIB", "mesVlanMapPortmaskIf12"),
        ("LUM-MES-MIB", "mesVlanMapPortmaskIf13"),
        ("LUM-MES-MIB", "mesVlanMapPortmaskIf14"),
        ("LUM-MES-MIB", "mesVlanMapPortmaskIf15"),
        ("LUM-MES-MIB", "mesVlanMapPortmaskIf16"),
        ("LUM-MES-MIB", "mesVlanMapSubrack"),
        ("LUM-MES-MIB", "mesVlanMapSlot"),
        ("LUM-MES-MIB", "mesVlanMapMacLearningLimit"))
)
if mibBuilder.loadTexts:
    mesVlanMapGroupV10.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

lumMesBasicComplV1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 1, 2, 1)
)
lumMesBasicComplV1.setObjects(
      *(("LUM-MES-MIB", "mesGeneralGroup"),
        ("LUM-MES-MIB", "mesUniGroup"),
        ("LUM-MES-MIB", "mesNniGroup"),
        ("LUM-MES-MIB", "mesEvcGroup"),
        ("LUM-MES-MIB", "mesCeEvcMapGroup"),
        ("LUM-MES-MIB", "mesBwpGroup"))
)
if mibBuilder.loadTexts:
    lumMesBasicComplV1.setStatus(
        "deprecated"
    )

lumMesBasicComplV2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 1, 2, 2)
)
lumMesBasicComplV2.setObjects(
      *(("LUM-MES-MIB", "mesGeneralGroup"),
        ("LUM-MES-MIB", "mesUniGroupV2"),
        ("LUM-MES-MIB", "mesNniGroup"),
        ("LUM-MES-MIB", "mesEvcGroupV2"),
        ("LUM-MES-MIB", "mesCeEvcMapGroupV2"),
        ("LUM-MES-MIB", "mesBwpGroupV2"),
        ("LUM-MES-MIB", "mesQProfileGroup"))
)
if mibBuilder.loadTexts:
    lumMesBasicComplV2.setStatus(
        "deprecated"
    )

lumMesBasicComplV3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 1, 2, 3)
)
lumMesBasicComplV3.setObjects(
      *(("LUM-MES-MIB", "mesGeneralGroupV2"),
        ("LUM-MES-MIB", "mesUniGroupV3"),
        ("LUM-MES-MIB", "mesNniGroupV2"),
        ("LUM-MES-MIB", "mesEvcGroupV3"),
        ("LUM-MES-MIB", "mesCeEvcMapGroupV2"),
        ("LUM-MES-MIB", "mesBwpGroupV2"),
        ("LUM-MES-MIB", "mesQProfileGroup"),
        ("LUM-MES-MIB", "mesMepGroup"),
        ("LUM-MES-MIB", "mesMegGroup"),
        ("LUM-MES-MIB", "mesMiscGroup"),
        ("LUM-MES-MIB", "mesEvcBwpMapGroup"))
)
if mibBuilder.loadTexts:
    lumMesBasicComplV3.setStatus(
        "deprecated"
    )

lumMesBasicComplV4 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 1, 2, 4)
)
lumMesBasicComplV4.setObjects(
      *(("LUM-MES-MIB", "mesGeneralGroupV3"),
        ("LUM-MES-MIB", "mesUniGroupV3"),
        ("LUM-MES-MIB", "mesNniGroupV2"),
        ("LUM-MES-MIB", "mesEvcGroupV3"),
        ("LUM-MES-MIB", "mesCeEvcMapGroupV2"),
        ("LUM-MES-MIB", "mesBwpGroupV2"),
        ("LUM-MES-MIB", "mesQProfileGroup"),
        ("LUM-MES-MIB", "mesMepGroup"),
        ("LUM-MES-MIB", "mesMegGroup"),
        ("LUM-MES-MIB", "mesMiscGroupV2"),
        ("LUM-MES-MIB", "mesEvcBwpMapGroup"),
        ("LUM-MES-MIB", "mesPortGroup"),
        ("LUM-MES-MIB", "mesVlanMapGroup"),
        ("LUM-MES-MIB", "mesMgmtVlanGroup"),
        ("LUM-MES-MIB", "mesLagGroup"))
)
if mibBuilder.loadTexts:
    lumMesBasicComplV4.setStatus(
        "deprecated"
    )

lumMesBasicComplV5 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 1, 2, 5)
)
lumMesBasicComplV5.setObjects(
      *(("LUM-MES-MIB", "mesGeneralGroupV3"),
        ("LUM-MES-MIB", "mesUniGroupV4"),
        ("LUM-MES-MIB", "mesNniGroupV3"),
        ("LUM-MES-MIB", "mesEvcGroupV3"),
        ("LUM-MES-MIB", "mesCeEvcMapGroupV2"),
        ("LUM-MES-MIB", "mesBwpGroupV2"),
        ("LUM-MES-MIB", "mesQProfileGroup"),
        ("LUM-MES-MIB", "mesMepGroup"),
        ("LUM-MES-MIB", "mesMegGroup"),
        ("LUM-MES-MIB", "mesMiscGroupV2"),
        ("LUM-MES-MIB", "mesEvcBwpMapGroup"),
        ("LUM-MES-MIB", "mesPortGroupV2"),
        ("LUM-MES-MIB", "mesVlanMapGroup"),
        ("LUM-MES-MIB", "mesBwpMapGroup"),
        ("LUM-MES-MIB", "mesMgmtVlanGroup"),
        ("LUM-MES-MIB", "mesLagGroup"),
        ("LUM-MES-MIB", "mesPolicingGroup"),
        ("LUM-MES-MIB", "mesShapingGroup"),
        ("LUM-MES-MIB", "mesCosGroup"))
)
if mibBuilder.loadTexts:
    lumMesBasicComplV5.setStatus(
        "deprecated"
    )

lumMesBasicComplV6 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 1, 2, 6)
)
lumMesBasicComplV6.setObjects(
      *(("LUM-MES-MIB", "mesGeneralGroupV3"),
        ("LUM-MES-MIB", "mesUniGroupV4"),
        ("LUM-MES-MIB", "mesNniGroupV3"),
        ("LUM-MES-MIB", "mesEvcGroupV3"),
        ("LUM-MES-MIB", "mesCeEvcMapGroupV2"),
        ("LUM-MES-MIB", "mesBwpGroupV2"),
        ("LUM-MES-MIB", "mesQProfileGroup"),
        ("LUM-MES-MIB", "mesMepGroup"),
        ("LUM-MES-MIB", "mesMegGroup"),
        ("LUM-MES-MIB", "mesMiscGroupV3"),
        ("LUM-MES-MIB", "mesEvcBwpMapGroup"),
        ("LUM-MES-MIB", "mesPortGroupV3"),
        ("LUM-MES-MIB", "mesVlanMapGroupV2"),
        ("LUM-MES-MIB", "mesBwpMapGroup"),
        ("LUM-MES-MIB", "mesMgmtVlanGroup"),
        ("LUM-MES-MIB", "mesLagGroup"),
        ("LUM-MES-MIB", "mesPolicingGroup"),
        ("LUM-MES-MIB", "mesShapingGroup"),
        ("LUM-MES-MIB", "mesCosGroup"),
        ("LUM-MES-MIB", "mesMirroringGroup"),
        ("LUM-MES-MIB", "mesVlanTagRuleGroup"),
        ("LUM-MES-MIB", "mesVlanTagClassVlanGroup"),
        ("LUM-MES-MIB", "mesCosProfileGroup"))
)
if mibBuilder.loadTexts:
    lumMesBasicComplV6.setStatus(
        "deprecated"
    )

lumMesBasicComplV7 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 1, 2, 7)
)
lumMesBasicComplV7.setObjects(
      *(("LUM-MES-MIB", "mesGeneralGroupV3"),
        ("LUM-MES-MIB", "mesUniGroupV4"),
        ("LUM-MES-MIB", "mesNniGroupV3"),
        ("LUM-MES-MIB", "mesEvcGroupV3"),
        ("LUM-MES-MIB", "mesCeEvcMapGroupV2"),
        ("LUM-MES-MIB", "mesBwpGroupV2"),
        ("LUM-MES-MIB", "mesQProfileGroup"),
        ("LUM-MES-MIB", "mesMepGroup"),
        ("LUM-MES-MIB", "mesMegGroup"),
        ("LUM-MES-MIB", "mesMiscGroupV4"),
        ("LUM-MES-MIB", "mesEvcBwpMapGroup"),
        ("LUM-MES-MIB", "mesPortGroupV4"),
        ("LUM-MES-MIB", "mesVlanMapGroupV3"),
        ("LUM-MES-MIB", "mesBwpMapGroup"),
        ("LUM-MES-MIB", "mesMgmtVlanGroup"),
        ("LUM-MES-MIB", "mesLagGroupV2"),
        ("LUM-MES-MIB", "mesPolicingGroup"),
        ("LUM-MES-MIB", "mesShapingGroup"),
        ("LUM-MES-MIB", "mesCosGroup"),
        ("LUM-MES-MIB", "mesMirroringGroupV2"),
        ("LUM-MES-MIB", "mesVlanTagRuleGroupV2"),
        ("LUM-MES-MIB", "mesVlanTagClassVlanGroupV2"),
        ("LUM-MES-MIB", "mesCosProfileGroup"),
        ("LUM-MES-MIB", "mesMaidGroup"),
        ("LUM-MES-MIB", "mesCfmMepGroup"),
        ("LUM-MES-MIB", "mesErpGroup"))
)
if mibBuilder.loadTexts:
    lumMesBasicComplV7.setStatus(
        "deprecated"
    )

lumMesBasicComplV8 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 1, 2, 8)
)
lumMesBasicComplV8.setObjects(
      *(("LUM-MES-MIB", "mesGeneralGroupV3"),
        ("LUM-MES-MIB", "mesUniGroupV4"),
        ("LUM-MES-MIB", "mesNniGroupV3"),
        ("LUM-MES-MIB", "mesEvcGroupV3"),
        ("LUM-MES-MIB", "mesCeEvcMapGroupV2"),
        ("LUM-MES-MIB", "mesBwpGroupV2"),
        ("LUM-MES-MIB", "mesQProfileGroup"),
        ("LUM-MES-MIB", "mesMepGroup"),
        ("LUM-MES-MIB", "mesMegGroup"),
        ("LUM-MES-MIB", "mesMiscGroupV4"),
        ("LUM-MES-MIB", "mesEvcBwpMapGroup"),
        ("LUM-MES-MIB", "mesPortGroupV4"),
        ("LUM-MES-MIB", "mesVlanMapGroupV3"),
        ("LUM-MES-MIB", "mesBwpMapGroup"),
        ("LUM-MES-MIB", "mesMgmtVlanGroup"),
        ("LUM-MES-MIB", "mesLagGroupV2"),
        ("LUM-MES-MIB", "mesPolicingGroup"),
        ("LUM-MES-MIB", "mesShapingGroupV2"),
        ("LUM-MES-MIB", "mesCosGroup"),
        ("LUM-MES-MIB", "mesMirroringGroupV2"),
        ("LUM-MES-MIB", "mesVlanTagRuleGroupV2"),
        ("LUM-MES-MIB", "mesVlanTagClassVlanGroupV2"),
        ("LUM-MES-MIB", "mesCosProfileGroup"),
        ("LUM-MES-MIB", "mesMaidGroup"),
        ("LUM-MES-MIB", "mesCfmMepGroup"),
        ("LUM-MES-MIB", "mesErpGroup"))
)
if mibBuilder.loadTexts:
    lumMesBasicComplV8.setStatus(
        "deprecated"
    )

lumMesBasicComplV9 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 1, 2, 9)
)
lumMesBasicComplV9.setObjects(
      *(("LUM-MES-MIB", "mesGeneralGroupV3"),
        ("LUM-MES-MIB", "mesUniGroupV4"),
        ("LUM-MES-MIB", "mesNniGroupV3"),
        ("LUM-MES-MIB", "mesEvcGroupV3"),
        ("LUM-MES-MIB", "mesCeEvcMapGroupV2"),
        ("LUM-MES-MIB", "mesBwpGroupV2"),
        ("LUM-MES-MIB", "mesQProfileGroup"),
        ("LUM-MES-MIB", "mesMepGroup"),
        ("LUM-MES-MIB", "mesMegGroup"),
        ("LUM-MES-MIB", "mesMiscGroupV5"),
        ("LUM-MES-MIB", "mesEvcBwpMapGroup"),
        ("LUM-MES-MIB", "mesPortGroupV5"),
        ("LUM-MES-MIB", "mesVlanMapGroupV4"),
        ("LUM-MES-MIB", "mesBwpMapGroupV2"),
        ("LUM-MES-MIB", "mesMgmtVlanGroup"),
        ("LUM-MES-MIB", "mesLagGroupV3"),
        ("LUM-MES-MIB", "mesPolicingGroup"),
        ("LUM-MES-MIB", "mesShapingGroupV2"),
        ("LUM-MES-MIB", "mesCosGroup"),
        ("LUM-MES-MIB", "mesMirroringGroupV2"),
        ("LUM-MES-MIB", "mesVlanTagRuleGroupV3"),
        ("LUM-MES-MIB", "mesVlanTagClassVlanGroupV2"),
        ("LUM-MES-MIB", "mesCosProfileGroupV2"),
        ("LUM-MES-MIB", "mesMaidGroupV2"),
        ("LUM-MES-MIB", "mesCfmMepGroupV2"),
        ("LUM-MES-MIB", "mesErpGroupV2"),
        ("LUM-MES-MIB", "mesClassGroup"),
        ("LUM-MES-MIB", "mesActionGroup"),
        ("LUM-MES-MIB", "mesPolicyGroup"))
)
if mibBuilder.loadTexts:
    lumMesBasicComplV9.setStatus(
        "deprecated"
    )

lumMesBasicComplV10 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 1, 2, 10)
)
lumMesBasicComplV10.setObjects(
      *(("LUM-MES-MIB", "mesGeneralGroupV3"),
        ("LUM-MES-MIB", "mesBwpGroupV2"),
        ("LUM-MES-MIB", "mesMiscGroupV6"),
        ("LUM-MES-MIB", "mesPortGroupV5"),
        ("LUM-MES-MIB", "mesVlanMapGroupV5"),
        ("LUM-MES-MIB", "mesBwpMapGroupV2"),
        ("LUM-MES-MIB", "mesMgmtVlanGroup"),
        ("LUM-MES-MIB", "mesLagGroupV3"),
        ("LUM-MES-MIB", "mesPolicingGroup"),
        ("LUM-MES-MIB", "mesShapingGroupV2"),
        ("LUM-MES-MIB", "mesCosGroup"),
        ("LUM-MES-MIB", "mesMirroringGroupV2"),
        ("LUM-MES-MIB", "mesVlanTagRuleGroupV3"),
        ("LUM-MES-MIB", "mesVlanTagClassVlanGroupV2"),
        ("LUM-MES-MIB", "mesCosProfileGroupV2"),
        ("LUM-MES-MIB", "mesMaidGroupV2"),
        ("LUM-MES-MIB", "mesCfmMepGroupV2"),
        ("LUM-MES-MIB", "mesErpGroupV2"),
        ("LUM-MES-MIB", "mesClassGroup"),
        ("LUM-MES-MIB", "mesActionGroup"),
        ("LUM-MES-MIB", "mesPolicyGroup"))
)
if mibBuilder.loadTexts:
    lumMesBasicComplV10.setStatus(
        "deprecated"
    )

lumMesBasicComplV11 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 1, 2, 11)
)
lumMesBasicComplV11.setObjects(
      *(("LUM-MES-MIB", "mesGeneralGroupV3"),
        ("LUM-MES-MIB", "mesBwpGroupV2"),
        ("LUM-MES-MIB", "mesMiscGroupV7"),
        ("LUM-MES-MIB", "mesPortGroupV6"),
        ("LUM-MES-MIB", "mesVlanMapGroupV5"),
        ("LUM-MES-MIB", "mesBwpMapGroupV2"),
        ("LUM-MES-MIB", "mesMgmtVlanGroup"),
        ("LUM-MES-MIB", "mesLagGroupV3"),
        ("LUM-MES-MIB", "mesPolicingGroup"),
        ("LUM-MES-MIB", "mesShapingGroupV2"),
        ("LUM-MES-MIB", "mesCosGroup"),
        ("LUM-MES-MIB", "mesMirroringGroupV2"),
        ("LUM-MES-MIB", "mesVlanTagRuleGroupV3"),
        ("LUM-MES-MIB", "mesVlanTagClassVlanGroupV2"),
        ("LUM-MES-MIB", "mesCosProfileGroupV2"),
        ("LUM-MES-MIB", "mesMaidGroupV3"),
        ("LUM-MES-MIB", "mesCfmMepGroupV3"),
        ("LUM-MES-MIB", "mesErpGroupV2"),
        ("LUM-MES-MIB", "mesClassGroupV2"),
        ("LUM-MES-MIB", "mesActionGroup"),
        ("LUM-MES-MIB", "mesPolicyGroup"))
)
if mibBuilder.loadTexts:
    lumMesBasicComplV11.setStatus(
        "deprecated"
    )

lumMesBasicComplV12 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 1, 2, 12)
)
lumMesBasicComplV12.setObjects(
      *(("LUM-MES-MIB", "mesGeneralGroupV3"),
        ("LUM-MES-MIB", "mesBwpGroupV2"),
        ("LUM-MES-MIB", "mesMiscGroupV7"),
        ("LUM-MES-MIB", "mesPortGroupV6"),
        ("LUM-MES-MIB", "mesVlanMapGroupV5"),
        ("LUM-MES-MIB", "mesBwpMapGroupV2"),
        ("LUM-MES-MIB", "mesMgmtVlanGroupV2"),
        ("LUM-MES-MIB", "mesLagGroupV3"),
        ("LUM-MES-MIB", "mesPolicingGroup"),
        ("LUM-MES-MIB", "mesShapingGroupV2"),
        ("LUM-MES-MIB", "mesCosGroup"),
        ("LUM-MES-MIB", "mesMirroringGroupV2"),
        ("LUM-MES-MIB", "mesVlanTagRuleGroupV3"),
        ("LUM-MES-MIB", "mesVlanTagClassVlanGroupV2"),
        ("LUM-MES-MIB", "mesCosProfileGroupV2"),
        ("LUM-MES-MIB", "mesMaidGroupV3"),
        ("LUM-MES-MIB", "mesCfmMepGroupV3"),
        ("LUM-MES-MIB", "mesErpGroupV2"),
        ("LUM-MES-MIB", "mesClassGroupV2"),
        ("LUM-MES-MIB", "mesActionGroup"),
        ("LUM-MES-MIB", "mesPolicyGroup"))
)
if mibBuilder.loadTexts:
    lumMesBasicComplV12.setStatus(
        "deprecated"
    )

lumMesBasicComplV13 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 1, 2, 13)
)
lumMesBasicComplV13.setObjects(
      *(("LUM-MES-MIB", "mesGeneralGroupV3"),
        ("LUM-MES-MIB", "mesBwpGroupV2"),
        ("LUM-MES-MIB", "mesMiscGroupV8"),
        ("LUM-MES-MIB", "mesPortGroupV6"),
        ("LUM-MES-MIB", "mesVlanMapGroupV5"),
        ("LUM-MES-MIB", "mesBwpMapGroupV2"),
        ("LUM-MES-MIB", "mesMgmtVlanGroupV2"),
        ("LUM-MES-MIB", "mesLagGroupV3"),
        ("LUM-MES-MIB", "mesPolicingGroup"),
        ("LUM-MES-MIB", "mesShapingGroupV2"),
        ("LUM-MES-MIB", "mesCosGroup"),
        ("LUM-MES-MIB", "mesMirroringGroupV2"),
        ("LUM-MES-MIB", "mesVlanTagRuleGroupV3"),
        ("LUM-MES-MIB", "mesVlanTagClassVlanGroupV2"),
        ("LUM-MES-MIB", "mesCosProfileGroupV2"),
        ("LUM-MES-MIB", "mesMaidGroupV4"),
        ("LUM-MES-MIB", "mesCfmMepGroupV4"),
        ("LUM-MES-MIB", "mesErpGroupV2"),
        ("LUM-MES-MIB", "mesClassGroupV2"),
        ("LUM-MES-MIB", "mesActionGroup"),
        ("LUM-MES-MIB", "mesPolicyGroup"),
        ("LUM-MES-MIB", "mesErrorPropGroup"))
)
if mibBuilder.loadTexts:
    lumMesBasicComplV13.setStatus(
        "deprecated"
    )

lumMesBasicComplV14 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 1, 2, 14)
)
lumMesBasicComplV14.setObjects(
      *(("LUM-MES-MIB", "mesGeneralGroupV3"),
        ("LUM-MES-MIB", "mesBwpGroupV2"),
        ("LUM-MES-MIB", "mesMiscGroupV9"),
        ("LUM-MES-MIB", "mesPortGroupV6"),
        ("LUM-MES-MIB", "mesVlanMapGroupV6"),
        ("LUM-MES-MIB", "mesBwpMapGroupV2"),
        ("LUM-MES-MIB", "mesMgmtVlanGroupV3"),
        ("LUM-MES-MIB", "mesLagGroupV3"),
        ("LUM-MES-MIB", "mesPolicingGroup"),
        ("LUM-MES-MIB", "mesShapingGroupV2"),
        ("LUM-MES-MIB", "mesCosGroup"),
        ("LUM-MES-MIB", "mesMirroringGroupV2"),
        ("LUM-MES-MIB", "mesVlanTagRuleGroupV3"),
        ("LUM-MES-MIB", "mesVlanTagClassVlanGroupV2"),
        ("LUM-MES-MIB", "mesCosProfileGroupV2"),
        ("LUM-MES-MIB", "mesMaidGroupV4"),
        ("LUM-MES-MIB", "mesCfmMepGroupV5"),
        ("LUM-MES-MIB", "mesErpGroupV3"),
        ("LUM-MES-MIB", "mesClassGroupV3"),
        ("LUM-MES-MIB", "mesActionGroup"),
        ("LUM-MES-MIB", "mesPolicyGroup"),
        ("LUM-MES-MIB", "mesErrorPropGroup"),
        ("LUM-MES-MIB", "mesVlanProtV1"))
)
if mibBuilder.loadTexts:
    lumMesBasicComplV14.setStatus(
        "deprecated"
    )

lumMesBasicComplV15 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 1, 2, 15)
)
lumMesBasicComplV15.setObjects(
      *(("LUM-MES-MIB", "mesGeneralGroupV3"),
        ("LUM-MES-MIB", "mesBwpGroupV3"),
        ("LUM-MES-MIB", "mesMiscGroupV9"),
        ("LUM-MES-MIB", "mesPortGroupV6"),
        ("LUM-MES-MIB", "mesVlanMapGroupV7"),
        ("LUM-MES-MIB", "mesBwpMapGroupV2"),
        ("LUM-MES-MIB", "mesMgmtVlanGroupV3"),
        ("LUM-MES-MIB", "mesLagGroupV4"),
        ("LUM-MES-MIB", "mesPolicingGroup"),
        ("LUM-MES-MIB", "mesShapingGroupV2"),
        ("LUM-MES-MIB", "mesCosGroup"),
        ("LUM-MES-MIB", "mesMirroringGroupV2"),
        ("LUM-MES-MIB", "mesVlanTagRuleGroupV3"),
        ("LUM-MES-MIB", "mesVlanTagClassVlanGroupV2"),
        ("LUM-MES-MIB", "mesCosProfileGroupV2"),
        ("LUM-MES-MIB", "mesMaidGroupV4"),
        ("LUM-MES-MIB", "mesCfmMepGroupV6"),
        ("LUM-MES-MIB", "mesErpGroupV3"),
        ("LUM-MES-MIB", "mesClassGroupV4"),
        ("LUM-MES-MIB", "mesActionGroupV2"),
        ("LUM-MES-MIB", "mesPolicyGroupV2"),
        ("LUM-MES-MIB", "mesErrorPropGroup"),
        ("LUM-MES-MIB", "mesVlanProtV1"),
        ("LUM-MES-MIB", "mesLacpGroup"))
)
if mibBuilder.loadTexts:
    lumMesBasicComplV15.setStatus(
        "deprecated"
    )

lumMesBasicComplV16 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 1, 2, 16)
)
lumMesBasicComplV16.setObjects(
      *(("LUM-MES-MIB", "mesGeneralGroupV3"),
        ("LUM-MES-MIB", "mesBwpGroupV3"),
        ("LUM-MES-MIB", "mesMiscGroupV9"),
        ("LUM-MES-MIB", "mesPortGroupV6"),
        ("LUM-MES-MIB", "mesVlanMapGroupV7"),
        ("LUM-MES-MIB", "mesBwpMapGroupV2"),
        ("LUM-MES-MIB", "mesMgmtVlanGroupV3"),
        ("LUM-MES-MIB", "mesLagGroupV5"),
        ("LUM-MES-MIB", "mesPolicingGroup"),
        ("LUM-MES-MIB", "mesShapingGroupV2"),
        ("LUM-MES-MIB", "mesCosGroup"),
        ("LUM-MES-MIB", "mesMirroringGroupV2"),
        ("LUM-MES-MIB", "mesVlanTagRuleGroupV3"),
        ("LUM-MES-MIB", "mesVlanTagClassVlanGroupV2"),
        ("LUM-MES-MIB", "mesCosProfileGroupV2"),
        ("LUM-MES-MIB", "mesMaidGroupV4"),
        ("LUM-MES-MIB", "mesCfmMepGroupV6"),
        ("LUM-MES-MIB", "mesErpGroupV3"),
        ("LUM-MES-MIB", "mesClassGroupV4"),
        ("LUM-MES-MIB", "mesActionGroupV2"),
        ("LUM-MES-MIB", "mesPolicyGroupV2"),
        ("LUM-MES-MIB", "mesErrorPropGroup"),
        ("LUM-MES-MIB", "mesVlanProtV1"),
        ("LUM-MES-MIB", "mesLacpGroup"))
)
if mibBuilder.loadTexts:
    lumMesBasicComplV16.setStatus(
        "deprecated"
    )

lumMesBasicComplV17 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 1, 2, 17)
)
lumMesBasicComplV17.setObjects(
      *(("LUM-MES-MIB", "mesGeneralGroupV3"),
        ("LUM-MES-MIB", "mesBwpGroupV3"),
        ("LUM-MES-MIB", "mesMiscGroupV9"),
        ("LUM-MES-MIB", "mesPortGroupV6"),
        ("LUM-MES-MIB", "mesVlanMapGroupV7"),
        ("LUM-MES-MIB", "mesBwpMapGroupV2"),
        ("LUM-MES-MIB", "mesMgmtVlanGroupV3"),
        ("LUM-MES-MIB", "mesLagGroupV6"),
        ("LUM-MES-MIB", "mesPolicingGroup"),
        ("LUM-MES-MIB", "mesShapingGroupV2"),
        ("LUM-MES-MIB", "mesCosGroup"),
        ("LUM-MES-MIB", "mesMirroringGroupV2"),
        ("LUM-MES-MIB", "mesVlanTagRuleGroupV3"),
        ("LUM-MES-MIB", "mesVlanTagClassVlanGroupV2"),
        ("LUM-MES-MIB", "mesCosProfileGroupV2"),
        ("LUM-MES-MIB", "mesMaidGroupV4"),
        ("LUM-MES-MIB", "mesCfmMepGroupV7"),
        ("LUM-MES-MIB", "mesErpGroupV4"),
        ("LUM-MES-MIB", "mesClassGroupV4"),
        ("LUM-MES-MIB", "mesActionGroupV2"),
        ("LUM-MES-MIB", "mesPolicyGroupV2"),
        ("LUM-MES-MIB", "mesErrorPropGroup"),
        ("LUM-MES-MIB", "mesVlanProtV1"),
        ("LUM-MES-MIB", "mesLacpGroup"))
)
if mibBuilder.loadTexts:
    lumMesBasicComplV17.setStatus(
        "deprecated"
    )

lumMesBasicComplV18 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 1, 2, 18)
)
lumMesBasicComplV18.setObjects(
      *(("LUM-MES-MIB", "mesGeneralGroupV5"),
        ("LUM-MES-MIB", "mesBwpGroupV3"),
        ("LUM-MES-MIB", "mesMiscGroupV9"),
        ("LUM-MES-MIB", "mesPortGroupV6"),
        ("LUM-MES-MIB", "mesVlanMapGroupV7"),
        ("LUM-MES-MIB", "mesBwpMapGroupV2"),
        ("LUM-MES-MIB", "mesMgmtVlanGroupV3"),
        ("LUM-MES-MIB", "mesLagGroupV7"),
        ("LUM-MES-MIB", "mesPolicingGroup"),
        ("LUM-MES-MIB", "mesShapingGroupV2"),
        ("LUM-MES-MIB", "mesCosGroup"),
        ("LUM-MES-MIB", "mesMirroringGroupV2"),
        ("LUM-MES-MIB", "mesVlanTagRuleGroupV3"),
        ("LUM-MES-MIB", "mesVlanTagClassVlanGroupV3"),
        ("LUM-MES-MIB", "mesCosProfileGroupV2"),
        ("LUM-MES-MIB", "mesMaidGroupV5"),
        ("LUM-MES-MIB", "mesCfmMepGroupV8"),
        ("LUM-MES-MIB", "mesErpGroupV5"),
        ("LUM-MES-MIB", "mesClassGroupV4"),
        ("LUM-MES-MIB", "mesActionGroupV2"),
        ("LUM-MES-MIB", "mesPolicyGroupV2"),
        ("LUM-MES-MIB", "mesErrorPropGroup"),
        ("LUM-MES-MIB", "mesVlanProtV1"),
        ("LUM-MES-MIB", "mesLacpGroup"))
)
if mibBuilder.loadTexts:
    lumMesBasicComplV18.setStatus(
        "deprecated"
    )

lumMesBasicComplV22 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 1, 2, 22)
)
lumMesBasicComplV22.setObjects(
      *(("LUM-MES-MIB", "mesGeneralGroupV5"),
        ("LUM-MES-MIB", "mesBwpGroupV3"),
        ("LUM-MES-MIB", "mesMiscGroupV9"),
        ("LUM-MES-MIB", "mesPortGroupV7"),
        ("LUM-MES-MIB", "mesVlanMapGroupV8"),
        ("LUM-MES-MIB", "mesBwpMapGroupV2"),
        ("LUM-MES-MIB", "mesMgmtVlanGroupV4"),
        ("LUM-MES-MIB", "mesLagGroupV8"),
        ("LUM-MES-MIB", "mesPolicingGroupV2"),
        ("LUM-MES-MIB", "mesShapingGroupV2"),
        ("LUM-MES-MIB", "mesCosGroup"),
        ("LUM-MES-MIB", "mesMirroringGroupV2"),
        ("LUM-MES-MIB", "mesVlanTagRuleGroupV4"),
        ("LUM-MES-MIB", "mesVlanTagClassVlanGroupV4"),
        ("LUM-MES-MIB", "mesCosProfileGroupV3"),
        ("LUM-MES-MIB", "mesMaidGroupV5"),
        ("LUM-MES-MIB", "mesCfmMepGroupV9"),
        ("LUM-MES-MIB", "mesErpGroupV6"),
        ("LUM-MES-MIB", "mesClassGroupV4"),
        ("LUM-MES-MIB", "mesActionGroupV2"),
        ("LUM-MES-MIB", "mesPolicyGroupV2"),
        ("LUM-MES-MIB", "mesErrorPropGroup"),
        ("LUM-MES-MIB", "mesVlanProtV1"),
        ("LUM-MES-MIB", "mesLacpGroupV1"))
)
if mibBuilder.loadTexts:
    lumMesBasicComplV22.setStatus(
        "deprecated"
    )

lumMesBasicComplV23 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 1, 2, 23)
)
lumMesBasicComplV23.setObjects(
      *(("LUM-MES-MIB", "mesGeneralGroupV5"),
        ("LUM-MES-MIB", "mesBwpGroupV3"),
        ("LUM-MES-MIB", "mesMiscGroupV9"),
        ("LUM-MES-MIB", "mesPortGroupV7"),
        ("LUM-MES-MIB", "mesVlanMapGroupV8"),
        ("LUM-MES-MIB", "mesBwpMapGroupV2"),
        ("LUM-MES-MIB", "mesMgmtVlanGroupV4"),
        ("LUM-MES-MIB", "mesLagGroupV8"),
        ("LUM-MES-MIB", "mesPolicingGroupV3"),
        ("LUM-MES-MIB", "mesShapingGroupV2"),
        ("LUM-MES-MIB", "mesCosGroup"),
        ("LUM-MES-MIB", "mesMirroringGroupV2"),
        ("LUM-MES-MIB", "mesVlanTagRuleGroupV4"),
        ("LUM-MES-MIB", "mesVlanTagClassVlanGroupV4"),
        ("LUM-MES-MIB", "mesCosProfileGroupV3"),
        ("LUM-MES-MIB", "mesMaidGroupV5"),
        ("LUM-MES-MIB", "mesCfmMepGroupV9"),
        ("LUM-MES-MIB", "mesErpGroupV6"),
        ("LUM-MES-MIB", "mesClassGroupV4"),
        ("LUM-MES-MIB", "mesActionGroupV2"),
        ("LUM-MES-MIB", "mesPolicyGroupV2"),
        ("LUM-MES-MIB", "mesErrorPropGroup"),
        ("LUM-MES-MIB", "mesVlanProtV1"),
        ("LUM-MES-MIB", "mesLacpGroupV1"))
)
if mibBuilder.loadTexts:
    lumMesBasicComplV23.setStatus(
        "deprecated"
    )

lumMesBasicComplV24 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 1, 2, 24)
)
lumMesBasicComplV24.setObjects(
      *(("LUM-MES-MIB", "mesGeneralGroupV5"),
        ("LUM-MES-MIB", "mesBwpGroupV4"),
        ("LUM-MES-MIB", "mesMiscGroupV9"),
        ("LUM-MES-MIB", "mesPortGroupV8"),
        ("LUM-MES-MIB", "mesVlanMapGroupV8"),
        ("LUM-MES-MIB", "mesBwpMapGroupV2"),
        ("LUM-MES-MIB", "mesMgmtVlanGroupV4"),
        ("LUM-MES-MIB", "mesLagGroupV8"),
        ("LUM-MES-MIB", "mesPolicingGroupV4"),
        ("LUM-MES-MIB", "mesShapingGroupV3"),
        ("LUM-MES-MIB", "mesCosGroup"),
        ("LUM-MES-MIB", "mesMirroringGroupV2"),
        ("LUM-MES-MIB", "mesVlanTagRuleGroupV4"),
        ("LUM-MES-MIB", "mesVlanTagClassVlanGroupV4"),
        ("LUM-MES-MIB", "mesCosProfileGroupV3"),
        ("LUM-MES-MIB", "mesMaidGroupV5"),
        ("LUM-MES-MIB", "mesCfmMepGroupV9"),
        ("LUM-MES-MIB", "mesErpGroupV7"),
        ("LUM-MES-MIB", "mesClassGroupV5"),
        ("LUM-MES-MIB", "mesActionGroupV3"),
        ("LUM-MES-MIB", "mesPolicyGroupV2"),
        ("LUM-MES-MIB", "mesErrorPropGroup"),
        ("LUM-MES-MIB", "mesVlanProtV1"),
        ("LUM-MES-MIB", "mesLacpGroupV1"))
)
if mibBuilder.loadTexts:
    lumMesBasicComplV24.setStatus(
        "deprecated"
    )

lumMesBasicComplV25 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 1, 2, 25)
)
lumMesBasicComplV25.setObjects(
      *(("LUM-MES-MIB", "mesGeneralGroupV5"),
        ("LUM-MES-MIB", "mesBwpGroupV4"),
        ("LUM-MES-MIB", "mesMiscGroupV9"),
        ("LUM-MES-MIB", "mesPortGroupV8"),
        ("LUM-MES-MIB", "mesVlanMapGroupV8"),
        ("LUM-MES-MIB", "mesBwpMapGroupV2"),
        ("LUM-MES-MIB", "mesMgmtVlanGroupV4"),
        ("LUM-MES-MIB", "mesLagGroupV8"),
        ("LUM-MES-MIB", "mesPolicingGroupV4"),
        ("LUM-MES-MIB", "mesShapingGroupV3"),
        ("LUM-MES-MIB", "mesCosGroup"),
        ("LUM-MES-MIB", "mesMirroringGroupV2"),
        ("LUM-MES-MIB", "mesVlanTagRuleGroupV4"),
        ("LUM-MES-MIB", "mesVlanTagClassVlanGroupV4"),
        ("LUM-MES-MIB", "mesCosProfileGroupV3"),
        ("LUM-MES-MIB", "mesMaidGroupV5"),
        ("LUM-MES-MIB", "mesCfmMepGroupV10"),
        ("LUM-MES-MIB", "mesErpGroupV7"),
        ("LUM-MES-MIB", "mesClassGroupV5"),
        ("LUM-MES-MIB", "mesActionGroupV3"),
        ("LUM-MES-MIB", "mesPolicyGroupV2"),
        ("LUM-MES-MIB", "mesErrorPropGroup"),
        ("LUM-MES-MIB", "mesVlanProtV1"),
        ("LUM-MES-MIB", "mesLacpGroupV1"))
)
if mibBuilder.loadTexts:
    lumMesBasicComplV25.setStatus(
        "deprecated"
    )

lumMesBasicComplV26 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 1, 2, 26)
)
lumMesBasicComplV26.setObjects(
      *(("LUM-MES-MIB", "mesGeneralGroupV6"),
        ("LUM-MES-MIB", "mesBwpGroupV4"),
        ("LUM-MES-MIB", "mesMiscGroupV9"),
        ("LUM-MES-MIB", "mesPortGroupV9"),
        ("LUM-MES-MIB", "mesVlanMapGroupV8"),
        ("LUM-MES-MIB", "mesBwpMapGroupV2"),
        ("LUM-MES-MIB", "mesMgmtVlanGroupV4"),
        ("LUM-MES-MIB", "mesLagGroupV8"),
        ("LUM-MES-MIB", "mesPolicingGroupV4"),
        ("LUM-MES-MIB", "mesShapingGroupV3"),
        ("LUM-MES-MIB", "mesCosGroup"),
        ("LUM-MES-MIB", "mesMirroringGroupV2"),
        ("LUM-MES-MIB", "mesVlanTagRuleGroupV4"),
        ("LUM-MES-MIB", "mesVlanTagClassVlanGroupV4"),
        ("LUM-MES-MIB", "mesCosProfileGroupV3"),
        ("LUM-MES-MIB", "mesMaidGroupV5"),
        ("LUM-MES-MIB", "mesCfmMepGroupV10"),
        ("LUM-MES-MIB", "mesErpGroupV7"),
        ("LUM-MES-MIB", "mesClassGroupV5"),
        ("LUM-MES-MIB", "mesActionGroupV3"),
        ("LUM-MES-MIB", "mesPolicyGroupV2"),
        ("LUM-MES-MIB", "mesErrorPropGroup"),
        ("LUM-MES-MIB", "mesVlanProtV1"),
        ("LUM-MES-MIB", "mesLacpGroupV1"))
)
if mibBuilder.loadTexts:
    lumMesBasicComplV26.setStatus(
        "deprecated"
    )

lumMesBasicComplV27 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 1, 2, 27)
)
lumMesBasicComplV27.setObjects(
      *(("LUM-MES-MIB", "mesGeneralGroupV6"),
        ("LUM-MES-MIB", "mesBwpGroupV4"),
        ("LUM-MES-MIB", "mesMiscGroupV9"),
        ("LUM-MES-MIB", "mesPortGroupV9"),
        ("LUM-MES-MIB", "mesVlanMapGroupV9"),
        ("LUM-MES-MIB", "mesBwpMapGroupV2"),
        ("LUM-MES-MIB", "mesMgmtVlanGroupV4"),
        ("LUM-MES-MIB", "mesLagGroupV8"),
        ("LUM-MES-MIB", "mesPolicingGroupV4"),
        ("LUM-MES-MIB", "mesShapingGroupV3"),
        ("LUM-MES-MIB", "mesCosGroup"),
        ("LUM-MES-MIB", "mesMirroringGroupV3"),
        ("LUM-MES-MIB", "mesVlanTagRuleGroupV4"),
        ("LUM-MES-MIB", "mesVlanTagClassVlanGroupV4"),
        ("LUM-MES-MIB", "mesCosProfileGroupV3"),
        ("LUM-MES-MIB", "mesMaidGroupV5"),
        ("LUM-MES-MIB", "mesCfmMepGroupV10"),
        ("LUM-MES-MIB", "mesErpGroupV7"),
        ("LUM-MES-MIB", "mesClassGroupV5"),
        ("LUM-MES-MIB", "mesActionGroupV3"),
        ("LUM-MES-MIB", "mesPolicyGroupV2"),
        ("LUM-MES-MIB", "mesErrorPropGroup"),
        ("LUM-MES-MIB", "mesVlanProtV1"),
        ("LUM-MES-MIB", "mesLacpGroupV1"))
)
if mibBuilder.loadTexts:
    lumMesBasicComplV27.setStatus(
        "deprecated"
    )

lumMesBasicComplV28 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 1, 2, 28)
)
lumMesBasicComplV28.setObjects(
      *(("LUM-MES-MIB", "mesGeneralGroupV6"),
        ("LUM-MES-MIB", "mesBwpGroupV5"),
        ("LUM-MES-MIB", "mesMiscGroupV10"),
        ("LUM-MES-MIB", "mesPortGroupV10"),
        ("LUM-MES-MIB", "mesVlanMapGroupV9"),
        ("LUM-MES-MIB", "mesBwpMapGroupV2"),
        ("LUM-MES-MIB", "mesMgmtVlanGroupV4"),
        ("LUM-MES-MIB", "mesLagGroupV9"),
        ("LUM-MES-MIB", "mesPolicingGroupV4"),
        ("LUM-MES-MIB", "mesShapingGroupV3"),
        ("LUM-MES-MIB", "mesCosGroup"),
        ("LUM-MES-MIB", "mesMirroringGroupV3"),
        ("LUM-MES-MIB", "mesVlanTagRuleGroupV4"),
        ("LUM-MES-MIB", "mesVlanTagClassVlanGroupV5"),
        ("LUM-MES-MIB", "mesCosProfileGroupV4"),
        ("LUM-MES-MIB", "mesMaidGroupV6"),
        ("LUM-MES-MIB", "mesCfmMepGroupV11"),
        ("LUM-MES-MIB", "mesErpGroupV7"),
        ("LUM-MES-MIB", "mesClassGroupV6"),
        ("LUM-MES-MIB", "mesActionGroupV4"),
        ("LUM-MES-MIB", "mesPolicyGroupV2"),
        ("LUM-MES-MIB", "mesErrorPropGroupV2"),
        ("LUM-MES-MIB", "mesVlanProtV1"),
        ("LUM-MES-MIB", "mesLacpGroupV1"))
)
if mibBuilder.loadTexts:
    lumMesBasicComplV28.setStatus(
        "deprecated"
    )

lumMesBasicComplV29 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 1, 2, 29)
)
lumMesBasicComplV29.setObjects(
      *(("LUM-MES-MIB", "mesGeneralGroupV6"),
        ("LUM-MES-MIB", "mesBwpGroupV5"),
        ("LUM-MES-MIB", "mesMiscGroupV10"),
        ("LUM-MES-MIB", "mesPortGroupV11"),
        ("LUM-MES-MIB", "mesVlanMapGroupV9"),
        ("LUM-MES-MIB", "mesBwpMapGroupV2"),
        ("LUM-MES-MIB", "mesMgmtVlanGroupV4"),
        ("LUM-MES-MIB", "mesLagGroupV9"),
        ("LUM-MES-MIB", "mesPolicingGroupV4"),
        ("LUM-MES-MIB", "mesShapingGroupV3"),
        ("LUM-MES-MIB", "mesCosGroup"),
        ("LUM-MES-MIB", "mesMirroringGroupV3"),
        ("LUM-MES-MIB", "mesVlanTagRuleGroupV4"),
        ("LUM-MES-MIB", "mesVlanTagClassVlanGroupV5"),
        ("LUM-MES-MIB", "mesCosProfileGroupV4"),
        ("LUM-MES-MIB", "mesMaidGroupV6"),
        ("LUM-MES-MIB", "mesCfmMepGroupV10"),
        ("LUM-MES-MIB", "mesErpGroupV7"),
        ("LUM-MES-MIB", "mesClassGroupV6"),
        ("LUM-MES-MIB", "mesActionGroupV4"),
        ("LUM-MES-MIB", "mesPolicyGroupV2"),
        ("LUM-MES-MIB", "mesErrorPropGroupV2"),
        ("LUM-MES-MIB", "mesVlanProtV1"),
        ("LUM-MES-MIB", "mesLacpGroupV1"))
)
if mibBuilder.loadTexts:
    lumMesBasicComplV29.setStatus(
        "deprecated"
    )

lumMesBasicComplV30 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 32, 1, 2, 30)
)
lumMesBasicComplV30.setObjects(
      *(("LUM-MES-MIB", "mesGeneralGroupV6"),
        ("LUM-MES-MIB", "mesBwpGroupV5"),
        ("LUM-MES-MIB", "mesMiscGroupV10"),
        ("LUM-MES-MIB", "mesPortGroupV11"),
        ("LUM-MES-MIB", "mesVlanMapGroupV10"),
        ("LUM-MES-MIB", "mesBwpMapGroupV2"),
        ("LUM-MES-MIB", "mesMgmtVlanGroupV4"),
        ("LUM-MES-MIB", "mesLagGroupV9"),
        ("LUM-MES-MIB", "mesPolicingGroupV4"),
        ("LUM-MES-MIB", "mesShapingGroupV3"),
        ("LUM-MES-MIB", "mesCosGroup"),
        ("LUM-MES-MIB", "mesMirroringGroupV3"),
        ("LUM-MES-MIB", "mesVlanTagRuleGroupV4"),
        ("LUM-MES-MIB", "mesVlanTagClassVlanGroupV5"),
        ("LUM-MES-MIB", "mesCosProfileGroupV4"),
        ("LUM-MES-MIB", "mesMaidGroupV6"),
        ("LUM-MES-MIB", "mesCfmMepGroupV10"),
        ("LUM-MES-MIB", "mesErpGroupV7"),
        ("LUM-MES-MIB", "mesClassGroupV6"),
        ("LUM-MES-MIB", "mesActionGroupV4"),
        ("LUM-MES-MIB", "mesPolicyGroupV2"),
        ("LUM-MES-MIB", "mesErrorPropGroupV2"),
        ("LUM-MES-MIB", "mesVlanProtV1"),
        ("LUM-MES-MIB", "mesLacpGroupV1"))
)
if mibBuilder.loadTexts:
    lumMesBasicComplV30.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LUM-MES-MIB",
    **{"MesQProfileId": MesQProfileId,
       "Dot1agCfmMaintDomainNameType": Dot1agCfmMaintDomainNameType,
       "Dot1agCfmMaintDomainName": Dot1agCfmMaintDomainName,
       "Dot1agCfmMaintAssocNameType": Dot1agCfmMaintAssocNameType,
       "Dot1agCfmMaintAssocName": Dot1agCfmMaintAssocName,
       "Dot1agCfmMDLevel": Dot1agCfmMDLevel,
       "Dot1agCfmMDLevelOrNone": Dot1agCfmMDLevelOrNone,
       "Dot1agCfmMpDirection": Dot1agCfmMpDirection,
       "Dot1agCfmCcmInterval": Dot1agCfmCcmInterval,
       "Dot1agCfmMepId": Dot1agCfmMepId,
       "MesLacpLinkProtectionValue": MesLacpLinkProtectionValue,
       "lumMesMIBModule": lumMesMIBModule,
       "lumMesConfs": lumMesConfs,
       "lumMesGroups": lumMesGroups,
       "mesGeneralGroup": mesGeneralGroup,
       "mesUniGroup": mesUniGroup,
       "mesNniGroup": mesNniGroup,
       "mesEvcGroup": mesEvcGroup,
       "mesCeEvcMapGroup": mesCeEvcMapGroup,
       "mesBwpGroup": mesBwpGroup,
       "mesCeEvcMapGroupV2": mesCeEvcMapGroupV2,
       "mesBwpGroupV2": mesBwpGroupV2,
       "mesUniGroupV2": mesUniGroupV2,
       "mesEvcGroupV2": mesEvcGroupV2,
       "mesQProfileGroup": mesQProfileGroup,
       "mesMepGroup": mesMepGroup,
       "mesGeneralGroupV2": mesGeneralGroupV2,
       "mesMegGroup": mesMegGroup,
       "mesUniGroupV3": mesUniGroupV3,
       "mesEvcGroupV3": mesEvcGroupV3,
       "mesNniGroupV2": mesNniGroupV2,
       "mesMiscGroup": mesMiscGroup,
       "mesEvcBwpMapGroup": mesEvcBwpMapGroup,
       "mesGeneralGroupV3": mesGeneralGroupV3,
       "mesPortGroup": mesPortGroup,
       "mesVlanMapGroup": mesVlanMapGroup,
       "mesMgmtVlanGroup": mesMgmtVlanGroup,
       "mesMiscGroupV2": mesMiscGroupV2,
       "mesLagGroup": mesLagGroup,
       "mesNniGroupV3": mesNniGroupV3,
       "mesPortGroupV2": mesPortGroupV2,
       "mesPolicingGroup": mesPolicingGroup,
       "mesShapingGroup": mesShapingGroup,
       "mesCosGroup": mesCosGroup,
       "mesBwpMapGroup": mesBwpMapGroup,
       "mesUniGroupV4": mesUniGroupV4,
       "mesGeneralGroupV4": mesGeneralGroupV4,
       "mesPortGroupV3": mesPortGroupV3,
       "mesMirroringGroup": mesMirroringGroup,
       "mesMiscGroupV3": mesMiscGroupV3,
       "mesVlanTagRuleGroup": mesVlanTagRuleGroup,
       "mesVlanTagClassVlanGroup": mesVlanTagClassVlanGroup,
       "mesVlanMapGroupV2": mesVlanMapGroupV2,
       "mesCosProfileGroup": mesCosProfileGroup,
       "mesLagGroupV2": mesLagGroupV2,
       "mesPortGroupV4": mesPortGroupV4,
       "mesMiscGroupV4": mesMiscGroupV4,
       "mesMaidGroup": mesMaidGroup,
       "mesCfmMepGroup": mesCfmMepGroup,
       "mesErpGroup": mesErpGroup,
       "mesVlanMapGroupV3": mesVlanMapGroupV3,
       "mesVlanTagRuleGroupV2": mesVlanTagRuleGroupV2,
       "mesVlanTagClassVlanGroupV2": mesVlanTagClassVlanGroupV2,
       "mesMirroringGroupV2": mesMirroringGroupV2,
       "mesShapingGroupV2": mesShapingGroupV2,
       "mesPortGroupV5": mesPortGroupV5,
       "mesBwpMapGroupV2": mesBwpMapGroupV2,
       "mesClassGroup": mesClassGroup,
       "mesMiscGroupV5": mesMiscGroupV5,
       "mesActionGroup": mesActionGroup,
       "mesPolicyGroup": mesPolicyGroup,
       "mesCosProfileGroupV2": mesCosProfileGroupV2,
       "mesLagGroupV3": mesLagGroupV3,
       "mesVlanMapGroupV4": mesVlanMapGroupV4,
       "mesCfmMepGroupV2": mesCfmMepGroupV2,
       "mesVlanTagRuleGroupV3": mesVlanTagRuleGroupV3,
       "mesErpGroupV2": mesErpGroupV2,
       "mesMaidGroupV2": mesMaidGroupV2,
       "mesMiscGroupV6": mesMiscGroupV6,
       "mesVlanMapGroupV5": mesVlanMapGroupV5,
       "mesClassGroupV2": mesClassGroupV2,
       "mesPortGroupV6": mesPortGroupV6,
       "mesMiscGroupV7": mesMiscGroupV7,
       "mesCfmMepGroupV3": mesCfmMepGroupV3,
       "mesMaidGroupV3": mesMaidGroupV3,
       "mesMgmtVlanGroupV2": mesMgmtVlanGroupV2,
       "mesErrorPropGroup": mesErrorPropGroup,
       "mesMiscGroupV8": mesMiscGroupV8,
       "mesGeneralGroupV5": mesGeneralGroupV5,
       "mesCfmMepGroupV4": mesCfmMepGroupV4,
       "mesMaidGroupV4": mesMaidGroupV4,
       "mesMiscGroupV9": mesMiscGroupV9,
       "mesErpGroupV3": mesErpGroupV3,
       "mesVlanProtV1": mesVlanProtV1,
       "mesCfmMepGroupV5": mesCfmMepGroupV5,
       "mesVlanMapGroupV6": mesVlanMapGroupV6,
       "mesClassGroupV3": mesClassGroupV3,
       "mesMgmtVlanGroupV3": mesMgmtVlanGroupV3,
       "mesClassGroupV4": mesClassGroupV4,
       "mesActionGroupV2": mesActionGroupV2,
       "mesCfmMepGroupV6": mesCfmMepGroupV6,
       "mesLacpGroup": mesLacpGroup,
       "mesVlanMapGroupV7": mesVlanMapGroupV7,
       "mesPolicyGroupV2": mesPolicyGroupV2,
       "mesBwpGroupV3": mesBwpGroupV3,
       "mesLagGroupV4": mesLagGroupV4,
       "mesLagGroupV5": mesLagGroupV5,
       "mesCfmMepGroupV7": mesCfmMepGroupV7,
       "mesErpGroupV4": mesErpGroupV4,
       "mesLagGroupV6": mesLagGroupV6,
       "mesErpGroupV5": mesErpGroupV5,
       "mesLagGroupV7": mesLagGroupV7,
       "mesVlanTagClassVlanGroupV3": mesVlanTagClassVlanGroupV3,
       "mesCfmMepGroupV8": mesCfmMepGroupV8,
       "mesMaidGroupV5": mesMaidGroupV5,
       "mesPortGroupV7": mesPortGroupV7,
       "mesVlanMapGroupV8": mesVlanMapGroupV8,
       "mesErpGroupV6": mesErpGroupV6,
       "mesMgmtVlanGroupV4": mesMgmtVlanGroupV4,
       "mesPolicingGroupV2": mesPolicingGroupV2,
       "mesLagGroupV8": mesLagGroupV8,
       "mesCosProfileGroupV3": mesCosProfileGroupV3,
       "mesVlanTagClassVlanGroupV4": mesVlanTagClassVlanGroupV4,
       "mesLacpGroupV1": mesLacpGroupV1,
       "mesVlanTagRuleGroupV4": mesVlanTagRuleGroupV4,
       "mesCfmMepGroupV9": mesCfmMepGroupV9,
       "mesPolicingGroupV3": mesPolicingGroupV3,
       "mesErpGroupV7": mesErpGroupV7,
       "mesPortGroupV8": mesPortGroupV8,
       "mesActionGroupV3": mesActionGroupV3,
       "mesClassGroupV5": mesClassGroupV5,
       "mesShapingGroupV3": mesShapingGroupV3,
       "mesPolicingGroupV4": mesPolicingGroupV4,
       "mesBwpGroupV4": mesBwpGroupV4,
       "mesCfmMepGroupV10": mesCfmMepGroupV10,
       "mesPortGroupV9": mesPortGroupV9,
       "mesGeneralGroupV6": mesGeneralGroupV6,
       "mesVlanMapGroupV9": mesVlanMapGroupV9,
       "mesMirroringGroupV3": mesMirroringGroupV3,
       "mesMiscGroupV10": mesMiscGroupV10,
       "mesClassGroupV6": mesClassGroupV6,
       "mesMaidGroupV6": mesMaidGroupV6,
       "mesPortGroupV10": mesPortGroupV10,
       "mesCosProfileGroupV4": mesCosProfileGroupV4,
       "mesLagGroupV9": mesLagGroupV9,
       "mesVlanTagClassVlanGroupV5": mesVlanTagClassVlanGroupV5,
       "mesActionGroupV4": mesActionGroupV4,
       "mesErrorPropGroupV2": mesErrorPropGroupV2,
       "mesBwpGroupV5": mesBwpGroupV5,
       "mesPortGroupV11": mesPortGroupV11,
       "mesCfmMepGroupV11": mesCfmMepGroupV11,
       "mesVlanMapGroupV10": mesVlanMapGroupV10,
       "lumMesCompl": lumMesCompl,
       "lumMesBasicComplV1": lumMesBasicComplV1,
       "lumMesBasicComplV2": lumMesBasicComplV2,
       "lumMesBasicComplV3": lumMesBasicComplV3,
       "lumMesBasicComplV4": lumMesBasicComplV4,
       "lumMesBasicComplV5": lumMesBasicComplV5,
       "lumMesBasicComplV6": lumMesBasicComplV6,
       "lumMesBasicComplV7": lumMesBasicComplV7,
       "lumMesBasicComplV8": lumMesBasicComplV8,
       "lumMesBasicComplV9": lumMesBasicComplV9,
       "lumMesBasicComplV10": lumMesBasicComplV10,
       "lumMesBasicComplV11": lumMesBasicComplV11,
       "lumMesBasicComplV12": lumMesBasicComplV12,
       "lumMesBasicComplV13": lumMesBasicComplV13,
       "lumMesBasicComplV14": lumMesBasicComplV14,
       "lumMesBasicComplV15": lumMesBasicComplV15,
       "lumMesBasicComplV16": lumMesBasicComplV16,
       "lumMesBasicComplV17": lumMesBasicComplV17,
       "lumMesBasicComplV18": lumMesBasicComplV18,
       "lumMesBasicComplV22": lumMesBasicComplV22,
       "lumMesBasicComplV23": lumMesBasicComplV23,
       "lumMesBasicComplV24": lumMesBasicComplV24,
       "lumMesBasicComplV25": lumMesBasicComplV25,
       "lumMesBasicComplV26": lumMesBasicComplV26,
       "lumMesBasicComplV27": lumMesBasicComplV27,
       "lumMesBasicComplV28": lumMesBasicComplV28,
       "lumMesBasicComplV29": lumMesBasicComplV29,
       "lumMesBasicComplV30": lumMesBasicComplV30,
       "lumMesMIBObjects": lumMesMIBObjects,
       "mesGeneral": mesGeneral,
       "mesGeneralConfigLastChangeTime": mesGeneralConfigLastChangeTime,
       "mesGeneralStateLastChangeTime": mesGeneralStateLastChangeTime,
       "mesGeneralUniTableSize": mesGeneralUniTableSize,
       "mesGeneralNniTableSize": mesGeneralNniTableSize,
       "mesGeneralEvcTableSize": mesGeneralEvcTableSize,
       "mesGeneralBwpTableSize": mesGeneralBwpTableSize,
       "mesGeneralCeEvcMapTableSize": mesGeneralCeEvcMapTableSize,
       "mesGeneralMepTableSize": mesGeneralMepTableSize,
       "mesGeneralMegTableSize": mesGeneralMegTableSize,
       "mesGeneralEvcBwpMapTableSize": mesGeneralEvcBwpMapTableSize,
       "mesGeneralPortTableSize": mesGeneralPortTableSize,
       "mesGeneralVlanMapTableSize": mesGeneralVlanMapTableSize,
       "mesGeneralMgmtVlanTableSize": mesGeneralMgmtVlanTableSize,
       "mesGeneralLagTableSize": mesGeneralLagTableSize,
       "mesGeneralPolicingTableSize": mesGeneralPolicingTableSize,
       "mesGeneralShapingTableSize": mesGeneralShapingTableSize,
       "mesGeneralBwpMapTableSize": mesGeneralBwpMapTableSize,
       "mesGeneralCosTableSize": mesGeneralCosTableSize,
       "mesGeneralMirroringTableSize": mesGeneralMirroringTableSize,
       "mesGeneralVlanTagRuleTableSize": mesGeneralVlanTagRuleTableSize,
       "mesGeneralVlanTagClassVlanTableSize": mesGeneralVlanTagClassVlanTableSize,
       "mesGeneralCosProfileTableSize": mesGeneralCosProfileTableSize,
       "mesGeneralMaidTableSize": mesGeneralMaidTableSize,
       "mesGeneralCfmMepTableSize": mesGeneralCfmMepTableSize,
       "mesGeneralErpTableSize": mesGeneralErpTableSize,
       "mesGeneralClassTableSize": mesGeneralClassTableSize,
       "mesGeneralActionTableSize": mesGeneralActionTableSize,
       "mesGeneralPolicyTableSize": mesGeneralPolicyTableSize,
       "mesGeneralErrorPropTableSize": mesGeneralErrorPropTableSize,
       "mesGeneralVlanProtTableSize": mesGeneralVlanProtTableSize,
       "mesGeneralLacpTableSize": mesGeneralLacpTableSize,
       "mesGeneralLagStateLastChangeTime": mesGeneralLagStateLastChangeTime,
       "mesGeneralLagConfigLastChangeTime": mesGeneralLagConfigLastChangeTime,
       "mesGeneralErpStateLastChangeTime": mesGeneralErpStateLastChangeTime,
       "mesGeneralErpConfigLastChangeTime": mesGeneralErpConfigLastChangeTime,
       "mesGeneralMaidStateLastChangeTime": mesGeneralMaidStateLastChangeTime,
       "mesGeneralMaidConfigLastChangeTime": mesGeneralMaidConfigLastChangeTime,
       "mesGeneralCfmMepStateLastChangeTime": mesGeneralCfmMepStateLastChangeTime,
       "mesGeneralCfmMepConfigLastChangeTime": mesGeneralCfmMepConfigLastChangeTime,
       "mesGeneralVlanMapStateLastChangeTime": mesGeneralVlanMapStateLastChangeTime,
       "mesGeneralVlanMapConfigLastChangeTime": mesGeneralVlanMapConfigLastChangeTime,
       "mesGeneralMgmtVlanStateLastChangeTime": mesGeneralMgmtVlanStateLastChangeTime,
       "mesGeneralMgmtVlanConfigLastChangeTime": mesGeneralMgmtVlanConfigLastChangeTime,
       "mesGeneralClassStateLastChangeTime": mesGeneralClassStateLastChangeTime,
       "mesGeneralClassConfigLastChangeTime": mesGeneralClassConfigLastChangeTime,
       "mesGeneralActionStateLastChangeTime": mesGeneralActionStateLastChangeTime,
       "mesGeneralActionConfigLastChangeTime": mesGeneralActionConfigLastChangeTime,
       "mesGeneralPolicyStateLastChangeTime": mesGeneralPolicyStateLastChangeTime,
       "mesGeneralPolicyConfigLastChangeTime": mesGeneralPolicyConfigLastChangeTime,
       "mesGeneralErrorPropStateLastChangeTime": mesGeneralErrorPropStateLastChangeTime,
       "mesGeneralErrorPropConfigLastChangeTime": mesGeneralErrorPropConfigLastChangeTime,
       "mesGeneralVlanProtStateLastChangeTime": mesGeneralVlanProtStateLastChangeTime,
       "mesGeneralVlanProtConfigLastChangeTime": mesGeneralVlanProtConfigLastChangeTime,
       "mesGeneralLacpStateLastChangeTime": mesGeneralLacpStateLastChangeTime,
       "mesGeneralLacpConfigLastChangeTime": mesGeneralLacpConfigLastChangeTime,
       "mesGeneralPolicingStateLastChangeTime": mesGeneralPolicingStateLastChangeTime,
       "mesGeneralPolicingConfigLastChangeTime": mesGeneralPolicingConfigLastChangeTime,
       "mesGeneralShapingStateLastChangeTime": mesGeneralShapingStateLastChangeTime,
       "mesGeneralShapingConfigLastChangeTime": mesGeneralShapingConfigLastChangeTime,
       "mesGeneralCosStateLastChangeTime": mesGeneralCosStateLastChangeTime,
       "mesGeneralCosConfigLastChangeTime": mesGeneralCosConfigLastChangeTime,
       "mesGeneralBwpMapStateLastChangeTime": mesGeneralBwpMapStateLastChangeTime,
       "mesGeneralBwpMapConfigLastChangeTime": mesGeneralBwpMapConfigLastChangeTime,
       "mesGeneralMirroringStateLastChangeTime": mesGeneralMirroringStateLastChangeTime,
       "mesGeneralMirroringConfigLastChangeTime": mesGeneralMirroringConfigLastChangeTime,
       "mesGeneralVlanTagRuleStateLastChangeTime": mesGeneralVlanTagRuleStateLastChangeTime,
       "mesGeneralVlanTagRuleConfigLastChangeTime": mesGeneralVlanTagRuleConfigLastChangeTime,
       "mesGeneralVlanTagClassVlanStateLastChangeTime": mesGeneralVlanTagClassVlanStateLastChangeTime,
       "mesGeneralVlanTagClassVlanConfigLastChangeTime": mesGeneralVlanTagClassVlanConfigLastChangeTime,
       "mesGeneralCosProfileStateLastChangeTime": mesGeneralCosProfileStateLastChangeTime,
       "mesGeneralCosProfileConfigLastChangeTime": mesGeneralCosProfileConfigLastChangeTime,
       "mesGeneralBwpStateLastChangeTime": mesGeneralBwpStateLastChangeTime,
       "mesGeneralBwpConfigLastChangeTime": mesGeneralBwpConfigLastChangeTime,
       "mesGeneralMiscStateLastChangeTime": mesGeneralMiscStateLastChangeTime,
       "mesGeneralMiscConfigLastChangeTime": mesGeneralMiscConfigLastChangeTime,
       "mesGeneralPortStateLastChangeTime": mesGeneralPortStateLastChangeTime,
       "mesGeneralPortConfigLastChangeTime": mesGeneralPortConfigLastChangeTime,
       "mesUniList": mesUniList,
       "mesUniTable": mesUniTable,
       "mesUniEntry": mesUniEntry,
       "mesUniIndex": mesUniIndex,
       "mesUniName": mesUniName,
       "mesUniDescr": mesUniDescr,
       "mesUniSubrack": mesUniSubrack,
       "mesUniSlot": mesUniSlot,
       "mesUniTxPort": mesUniTxPort,
       "mesUniRxPort": mesUniRxPort,
       "mesUniObjectProperty": mesUniObjectProperty,
       "mesUniAdminStatus": mesUniAdminStatus,
       "mesUniOperStatus": mesUniOperStatus,
       "mesUniIdentifier": mesUniIdentifier,
       "mesUniMtuSize": mesUniMtuSize,
       "mesUniMaxNoOfEvcs": mesUniMaxNoOfEvcs,
       "mesUniCurrentNoOfEvcs": mesUniCurrentNoOfEvcs,
       "mesUniAvailableCapacity": mesUniAvailableCapacity,
       "mesUniServiceMultiplexing": mesUniServiceMultiplexing,
       "mesUniBundling": mesUniBundling,
       "mesUniAllToOneBundling": mesUniAllToOneBundling,
       "mesUniUntaggedCeVlanIdAssignment": mesUniUntaggedCeVlanIdAssignment,
       "mesUniAssociateBwp": mesUniAssociateBwp,
       "mesUniReleaseBwp": mesUniReleaseBwp,
       "mesUniIngressBwProfilePerUni": mesUniIngressBwProfilePerUni,
       "mesUniIngressBwp": mesUniIngressBwp,
       "mesUniEgressBwProfilePerUni": mesUniEgressBwProfilePerUni,
       "mesUniEgressBwp": mesUniEgressBwp,
       "mesUniL2ControlProtocolProcessing": mesUniL2ControlProtocolProcessing,
       "mesUniSetupCommand": mesUniSetupCommand,
       "mesUniCreateEvcCommand": mesUniCreateEvcCommand,
       "mesUniListCeVlanIdsCommand": mesUniListCeVlanIdsCommand,
       "mesUniTaggingOfUntaggedFrames": mesUniTaggingOfUntaggedFrames,
       "mesUniCeVlanIdAssignmentCommand": mesUniCeVlanIdAssignmentCommand,
       "mesUniL2SpanningTreeProcessing": mesUniL2SpanningTreeProcessing,
       "mesUniL2PauseProcessing": mesUniL2PauseProcessing,
       "mesUniL2SlowProtocolsProcessing": mesUniL2SlowProtocolsProcessing,
       "mesUniL2PortAuthenticationProcessing": mesUniL2PortAuthenticationProcessing,
       "mesUniL2OtherBridgeBlockProcessing": mesUniL2OtherBridgeBlockProcessing,
       "mesUniL2AllLANsBridgeMgmtProcessing": mesUniL2AllLANsBridgeMgmtProcessing,
       "mesUniL2GarpProcessing": mesUniL2GarpProcessing,
       "mesUniL2OamUniMeProcessing": mesUniL2OamUniMeProcessing,
       "mesUniTagTransparency": mesUniTagTransparency,
       "mesUniMgmtVlan": mesUniMgmtVlan,
       "mesUniDefineMgmtVlan": mesUniDefineMgmtVlan,
       "mesUniMgmtVlanTagType": mesUniMgmtVlanTagType,
       "mesUniMgmtVlanEtherType": mesUniMgmtVlanEtherType,
       "mesUniMgmtVlanVlanId": mesUniMgmtVlanVlanId,
       "mesUniMgmtVlanPriority": mesUniMgmtVlanPriority,
       "mesUniMgmtVlanMacAddress": mesUniMgmtVlanMacAddress,
       "mesUniMacInMac": mesUniMacInMac,
       "mesUniMacInMacIsid": mesUniMacInMacIsid,
       "mesUniMacInMacDa": mesUniMacInMacDa,
       "mesUniDefineMac": mesUniDefineMac,
       "mesUniLagStatus": mesUniLagStatus,
       "mesUniLagPortmask": mesUniLagPortmask,
       "mesUniAssociateLag": mesUniAssociateLag,
       "mesNniList": mesNniList,
       "mesNniTable": mesNniTable,
       "mesNniEntry": mesNniEntry,
       "mesNniIndex": mesNniIndex,
       "mesNniName": mesNniName,
       "mesNniDescr": mesNniDescr,
       "mesNniSubrack": mesNniSubrack,
       "mesNniSlot": mesNniSlot,
       "mesNniTxPort": mesNniTxPort,
       "mesNniRxPort": mesNniRxPort,
       "mesNniObjectProperty": mesNniObjectProperty,
       "mesNniAdminStatus": mesNniAdminStatus,
       "mesNniOperStatus": mesNniOperStatus,
       "mesNniIdentifier": mesNniIdentifier,
       "mesNniCurrentNoOfEvcs": mesNniCurrentNoOfEvcs,
       "mesNniAvailableCapacity": mesNniAvailableCapacity,
       "mesNniDefineMgmtVlan": mesNniDefineMgmtVlan,
       "mesNniMgmtVlanTagType": mesNniMgmtVlanTagType,
       "mesNniMgmtVlanEtherType": mesNniMgmtVlanEtherType,
       "mesNniMgmtVlanVlanId": mesNniMgmtVlanVlanId,
       "mesNniMgmtVlanPriority": mesNniMgmtVlanPriority,
       "mesNniMgmtVlanIpAddress": mesNniMgmtVlanIpAddress,
       "mesNniMgmtVlanNetMask": mesNniMgmtVlanNetMask,
       "mesNniMgmtVlanMacAddress": mesNniMgmtVlanMacAddress,
       "mesNniSetupCommand": mesNniSetupCommand,
       "mesNniMgmtVlan": mesNniMgmtVlan,
       "mesNniMacInMac": mesNniMacInMac,
       "mesNniMacInMacIsid": mesNniMacInMacIsid,
       "mesNniMacInMacDa": mesNniMacInMacDa,
       "mesNniDefineMac": mesNniDefineMac,
       "mesNniLagStatus": mesNniLagStatus,
       "mesEvcList": mesEvcList,
       "mesEvcTable": mesEvcTable,
       "mesEvcEntry": mesEvcEntry,
       "mesEvcIndex": mesEvcIndex,
       "mesEvcName": mesEvcName,
       "mesEvcDescr": mesEvcDescr,
       "mesEvcObjectProperty": mesEvcObjectProperty,
       "mesEvcAdminStatus": mesEvcAdminStatus,
       "mesEvcOperStatus": mesEvcOperStatus,
       "mesEvcIdentifier": mesEvcIdentifier,
       "mesEvcUniIdentifier": mesEvcUniIdentifier,
       "mesEvcNniIdentifier": mesEvcNniIdentifier,
       "mesEvcType": mesEvcType,
       "mesEvcMtuSize": mesEvcMtuSize,
       "mesEvcFrameDeliveryUnicast": mesEvcFrameDeliveryUnicast,
       "mesEvcFrameDeliveryMulticast": mesEvcFrameDeliveryMulticast,
       "mesEvcFrameDeliveryBroadcast": mesEvcFrameDeliveryBroadcast,
       "mesEvcDefineL2Control": mesEvcDefineL2Control,
       "mesEvcL2ControlProtocolDisposition": mesEvcL2ControlProtocolDisposition,
       "mesEvcL2DestinationMacAddress": mesEvcL2DestinationMacAddress,
       "mesEvcCeVlanIdPreservation": mesEvcCeVlanIdPreservation,
       "mesEvcCosPreservation": mesEvcCosPreservation,
       "mesEvcAssociateBwp": mesEvcAssociateBwp,
       "mesEvcReleaseBwp": mesEvcReleaseBwp,
       "mesEvcIngressBwProfilePerEvc": mesEvcIngressBwProfilePerEvc,
       "mesEvcIngressBwp": mesEvcIngressBwp,
       "mesEvcEgressBwProfilePerEvc": mesEvcEgressBwProfilePerEvc,
       "mesEvcEgressBwp": mesEvcEgressBwp,
       "mesEvcCreateCeVlanIdMap": mesEvcCreateCeVlanIdMap,
       "mesEvcDefineProviderTag": mesEvcDefineProviderTag,
       "mesEvcProviderTagType": mesEvcProviderTagType,
       "mesEvcProviderTagEtherType": mesEvcProviderTagEtherType,
       "mesEvcProviderTagVlanId": mesEvcProviderTagVlanId,
       "mesEvcDefineClassOfService": mesEvcDefineClassOfService,
       "mesEvcCoSClassification": mesEvcCoSClassification,
       "mesEvcCoSPriority": mesEvcCoSPriority,
       "mesEvcInternalReference": mesEvcInternalReference,
       "mesEvcRowStatus": mesEvcRowStatus,
       "mesEvcQProfile": mesEvcQProfile,
       "mesEvcCeVlanIdMap": mesEvcCeVlanIdMap,
       "mesEvcDefaultCeVlanPriority": mesEvcDefaultCeVlanPriority,
       "mesEvcClientEgressTagVlanIdAssignment": mesEvcClientEgressTagVlanIdAssignment,
       "mesEvcClientEgressTagVlanId": mesEvcClientEgressTagVlanId,
       "mesEvcTagPriorityAssignment": mesEvcTagPriorityAssignment,
       "mesEvcClientEgressTagTypeAssignment": mesEvcClientEgressTagTypeAssignment,
       "mesEvcClientEgressTagType": mesEvcClientEgressTagType,
       "mesEvcClientEgressTagEtherType": mesEvcClientEgressTagEtherType,
       "mesEvcMacInMac": mesEvcMacInMac,
       "mesEvcMacInMacLtoC": mesEvcMacInMacLtoC,
       "mesEvcCopyIsid": mesEvcCopyIsid,
       "mesEvcMacInMacIsid": mesEvcMacInMacIsid,
       "mesEvcMacInMacIsidLtoC": mesEvcMacInMacIsidLtoC,
       "mesEvcMacInMacDa": mesEvcMacInMacDa,
       "mesEvcMacInMacDaLtoC": mesEvcMacInMacDaLtoC,
       "mesEvcDefineMac": mesEvcDefineMac,
       "mesEvcIngressBwProfileModel": mesEvcIngressBwProfileModel,
       "mesEvcIngressBwProfileMap": mesEvcIngressBwProfileMap,
       "mesCeEvcMapList": mesCeEvcMapList,
       "mesCeEvcMapTable": mesCeEvcMapTable,
       "mesCeEvcMapEntry": mesCeEvcMapEntry,
       "mesCeEvcMapIndex": mesCeEvcMapIndex,
       "mesCeEvcMapName": mesCeEvcMapName,
       "mesCeEvcMapObjectProperty": mesCeEvcMapObjectProperty,
       "mesCeEvcMapType": mesCeEvcMapType,
       "mesCeEvcMapVlanIdRangeLower": mesCeEvcMapVlanIdRangeLower,
       "mesCeEvcMapVlanIdRangeUpper": mesCeEvcMapVlanIdRangeUpper,
       "mesCeEvcMapEvcId": mesCeEvcMapEvcId,
       "mesCeEvcMapInternalReference": mesCeEvcMapInternalReference,
       "mesCeEvcMapRowStatus": mesCeEvcMapRowStatus,
       "mesCeEvcMapPrio0Included": mesCeEvcMapPrio0Included,
       "mesCeEvcMapPrio1Included": mesCeEvcMapPrio1Included,
       "mesCeEvcMapPrio2Included": mesCeEvcMapPrio2Included,
       "mesCeEvcMapPrio3Included": mesCeEvcMapPrio3Included,
       "mesCeEvcMapPrio4Included": mesCeEvcMapPrio4Included,
       "mesCeEvcMapPrio5Included": mesCeEvcMapPrio5Included,
       "mesCeEvcMapPrio6Included": mesCeEvcMapPrio6Included,
       "mesCeEvcMapPrio7Included": mesCeEvcMapPrio7Included,
       "mesCeEvcMapDefaultCeVlanId": mesCeEvcMapDefaultCeVlanId,
       "mesCeEvcMapPrioIncluded": mesCeEvcMapPrioIncluded,
       "mesBwpList": mesBwpList,
       "mesBwpTable": mesBwpTable,
       "mesBwpEntry": mesBwpEntry,
       "mesBwpIndex": mesBwpIndex,
       "mesBwpName": mesBwpName,
       "mesBwpObjectProperty": mesBwpObjectProperty,
       "mesBwpCoSIdentifier": mesBwpCoSIdentifier,
       "mesBwpCir": mesBwpCir,
       "mesBwpCbs": mesBwpCbs,
       "mesBwpEir": mesBwpEir,
       "mesBwpEbs": mesBwpEbs,
       "mesBwpCouplingFlag": mesBwpCouplingFlag,
       "mesBwpColorMode": mesBwpColorMode,
       "mesBwpInternalReference": mesBwpInternalReference,
       "mesBwpRowStatus": mesBwpRowStatus,
       "mesBwpServiceId": mesBwpServiceId,
       "mesBwpPolicerId": mesBwpPolicerId,
       "mesBwpSubrack": mesBwpSubrack,
       "mesBwpSlot": mesBwpSlot,
       "mesQProfileList": mesQProfileList,
       "mesQProfileTable": mesQProfileTable,
       "mesQProfileEntry": mesQProfileEntry,
       "mesQProfileIndex": mesQProfileIndex,
       "mesQProfileName": mesQProfileName,
       "mesQProfileObjectProperty": mesQProfileObjectProperty,
       "mesQProfileId": mesQProfileId,
       "mesQProfileType": mesQProfileType,
       "mesQProfileWeight": mesQProfileWeight,
       "mesQProfileGreenLowThreshold": mesQProfileGreenLowThreshold,
       "mesQProfileGreenHighThreshold": mesQProfileGreenHighThreshold,
       "mesQProfileGreenDropProbability": mesQProfileGreenDropProbability,
       "mesQProfileYellowLowThreshold": mesQProfileYellowLowThreshold,
       "mesQProfileYellowHighThreshold": mesQProfileYellowHighThreshold,
       "mesQProfileYellowDropProbability": mesQProfileYellowDropProbability,
       "mesQProfileInternalReference": mesQProfileInternalReference,
       "mesMepList": mesMepList,
       "mesMepTable": mesMepTable,
       "mesMepEntry": mesMepEntry,
       "mesMepIndex": mesMepIndex,
       "mesMepName": mesMepName,
       "mesMepObjectProperty": mesMepObjectProperty,
       "mesMepInternalReference": mesMepInternalReference,
       "mesMepMeIdentifier": mesMepMeIdentifier,
       "mesMepAdminStatus": mesMepAdminStatus,
       "mesMepOperStatus": mesMepOperStatus,
       "mesMepTransmissionInterval": mesMepTransmissionInterval,
       "mesMepLossOfContinuity": mesMepLossOfContinuity,
       "mesMepUnexpectedMegId": mesMepUnexpectedMegId,
       "mesMepUnexpectedTransmissionInterval": mesMepUnexpectedTransmissionInterval,
       "mesMepRemoteDefectIndication": mesMepRemoteDefectIndication,
       "mesMepUnexpectedOpCode": mesMepUnexpectedOpCode,
       "mesMepAlarmIndicationSignal": mesMepAlarmIndicationSignal,
       "mesMepMegIdFormatReceived": mesMepMegIdFormatReceived,
       "mesMepMegIdIccReceived": mesMepMegIdIccReceived,
       "mesMepMegIdReceived": mesMepMegIdReceived,
       "mesMepId": mesMepId,
       "mesMepIdExpected": mesMepIdExpected,
       "mesMepIdReceived": mesMepIdReceived,
       "mesMepUnexpectedMepId": mesMepUnexpectedMepId,
       "mesMepUnexpectedMegLevel": mesMepUnexpectedMegLevel,
       "mesMepMegId": mesMepMegId,
       "mesMepMegIdFormat": mesMepMegIdFormat,
       "mesMepMegIdIcc": mesMepMegIdIcc,
       "mesMegList": mesMegList,
       "mesMegTable": mesMegTable,
       "mesMegEntry": mesMegEntry,
       "mesMegIndex": mesMegIndex,
       "mesMegName": mesMegName,
       "mesMegObjectProperty": mesMegObjectProperty,
       "mesMegInternalReference": mesMegInternalReference,
       "mesMegAdminStatus": mesMegAdminStatus,
       "mesMegOperStatus": mesMegOperStatus,
       "mesMegLevel": mesMegLevel,
       "mesMegUnexpectedMessage": mesMegUnexpectedMessage,
       "mesMiscList": mesMiscList,
       "mesMiscTable": mesMiscTable,
       "mesMiscEntry": mesMiscEntry,
       "mesMiscIndex": mesMiscIndex,
       "mesMiscName": mesMiscName,
       "mesMiscObjectProperty": mesMiscObjectProperty,
       "mesMiscInternalReference": mesMiscInternalReference,
       "mesMiscAdminStatus": mesMiscAdminStatus,
       "mesMiscOperStatus": mesMiscOperStatus,
       "mesMiscMgmtVlanIpAddress": mesMiscMgmtVlanIpAddress,
       "mesMiscMgmtVlanNetMask": mesMiscMgmtVlanNetMask,
       "mesMiscMgmtVlanMacAddress0": mesMiscMgmtVlanMacAddress0,
       "mesMiscMgmtVlanMacAddress1": mesMiscMgmtVlanMacAddress1,
       "mesMiscMgmtVlanMacAddress2": mesMiscMgmtVlanMacAddress2,
       "mesMiscConfigureAddress": mesMiscConfigureAddress,
       "mesMiscMgmtVlanNode": mesMiscMgmtVlanNode,
       "mesMiscMacAgeing": mesMiscMacAgeing,
       "mesMiscMacGetTable": mesMiscMacGetTable,
       "mesMiscNoOfMegs": mesMiscNoOfMegs,
       "mesMiscAssociateMeg": mesMiscAssociateMeg,
       "mesMiscNoOfErps": mesMiscNoOfErps,
       "mesMiscAssociateErp": mesMiscAssociateErp,
       "mesMiscL2Mode": mesMiscL2Mode,
       "mesMiscConfigureMode": mesMiscConfigureMode,
       "mesMiscIdentity": mesMiscIdentity,
       "mesMiscAssociateClass": mesMiscAssociateClass,
       "mesMiscAssociateBwp": mesMiscAssociateBwp,
       "mesMiscWred": mesMiscWred,
       "mesMiscGetPacketMonitor": mesMiscGetPacketMonitor,
       "mesMiscSfpPortUsageCurrent": mesMiscSfpPortUsageCurrent,
       "mesMiscSfpPortUsageNext": mesMiscSfpPortUsageNext,
       "mesMiscAssociateErrorProp": mesMiscAssociateErrorProp,
       "mesMiscNoOfErpV2s": mesMiscNoOfErpV2s,
       "mesMiscAssociateErpV2": mesMiscAssociateErpV2,
       "mesMiscAssociateVlanProt": mesMiscAssociateVlanProt,
       "mesMiscCreateVlan": mesMiscCreateVlan,
       "mesMiscEnablePtp1588": mesMiscEnablePtp1588,
       "mesMiscEnableStpMgmtVlan": mesMiscEnableStpMgmtVlan,
       "mesMiscAssociateClassAdvanced": mesMiscAssociateClassAdvanced,
       "mesMiscAssociateErpAdvanced": mesMiscAssociateErpAdvanced,
       "mesMiscAssociateMegAdvanced": mesMiscAssociateMegAdvanced,
       "mesMiscCreateClass": mesMiscCreateClass,
       "mesMiscCreateAction": mesMiscCreateAction,
       "mesMiscCreateMeg": mesMiscCreateMeg,
       "mesMiscCreateMep": mesMiscCreateMep,
       "mesMiscCreateErrorProp": mesMiscCreateErrorProp,
       "mesMiscCreatePolicer": mesMiscCreatePolicer,
       "mesMiscResendConfig": mesMiscResendConfig,
       "mesEvcBwpMapList": mesEvcBwpMapList,
       "mesEvcBwpMapTable": mesEvcBwpMapTable,
       "mesEvcBwpMapEntry": mesEvcBwpMapEntry,
       "mesEvcBwpMapIndex": mesEvcBwpMapIndex,
       "mesEvcBwpMapName": mesEvcBwpMapName,
       "mesEvcBwpMapObjectProperty": mesEvcBwpMapObjectProperty,
       "mesEvcBwpMapEvcId": mesEvcBwpMapEvcId,
       "mesEvcBwpMapBwpId": mesEvcBwpMapBwpId,
       "mesEvcBwpMapModel": mesEvcBwpMapModel,
       "mesEvcBwpMapPriority": mesEvcBwpMapPriority,
       "mesEvcBwpMapInternalReference": mesEvcBwpMapInternalReference,
       "mesEvcBwpMapRowStatus": mesEvcBwpMapRowStatus,
       "mesPortList": mesPortList,
       "mesPortTable": mesPortTable,
       "mesPortEntry": mesPortEntry,
       "mesPortIndex": mesPortIndex,
       "mesPortName": mesPortName,
       "mesPortDescr": mesPortDescr,
       "mesPortSubrack": mesPortSubrack,
       "mesPortSlot": mesPortSlot,
       "mesPortTxPort": mesPortTxPort,
       "mesPortRxPort": mesPortRxPort,
       "mesPortAdminStatus": mesPortAdminStatus,
       "mesPortOperStatus": mesPortOperStatus,
       "mesPortMtuSize": mesPortMtuSize,
       "mesPortTagType": mesPortTagType,
       "mesPortNoOfVlans": mesPortNoOfVlans,
       "mesPortVlanAware": mesPortVlanAware,
       "mesPortVlanTagged": mesPortVlanTagged,
       "mesPortVlanUntagged": mesPortVlanUntagged,
       "mesPortIngressFiltering": mesPortIngressFiltering,
       "mesPortEgressTag": mesPortEgressTag,
       "mesPortDefaultCeVlanId": mesPortDefaultCeVlanId,
       "mesPortAssociateVlan": mesPortAssociateVlan,
       "mesPortReleaseVlan": mesPortReleaseVlan,
       "mesPortActingAsLine": mesPortActingAsLine,
       "mesPortTrustedPortmask": mesPortTrustedPortmask,
       "mesPortConfigureTrustedPortmask": mesPortConfigureTrustedPortmask,
       "mesPortMacAddress": mesPortMacAddress,
       "mesPortLagStatus": mesPortLagStatus,
       "mesPortLagPortmask": mesPortLagPortmask,
       "mesPortAssociateLag": mesPortAssociateLag,
       "mesPortTxEthUtilization": mesPortTxEthUtilization,
       "mesPortRxEthUtilization": mesPortRxEthUtilization,
       "mesPortFlowControlMode": mesPortFlowControlMode,
       "mesPortAutoNegotiationMode": mesPortAutoNegotiationMode,
       "mesPortAutoNegotiationStatus": mesPortAutoNegotiationStatus,
       "mesPortLinkDown": mesPortLinkDown,
       "mesPortLinkFaultRemote": mesPortLinkFaultRemote,
       "mesPortLinkFaultLocal": mesPortLinkFaultLocal,
       "mesPortNoOfShapers": mesPortNoOfShapers,
       "mesPortNoOfPolicers": mesPortNoOfPolicers,
       "mesPortAssociateShaper": mesPortAssociateShaper,
       "mesPortReleaseShaper": mesPortReleaseShaper,
       "mesPortAssociatePolicer": mesPortAssociatePolicer,
       "mesPortReleasePolicer": mesPortReleasePolicer,
       "mesPortRestartAutoNegotiation": mesPortRestartAutoNegotiation,
       "mesPortConfigureLine": mesPortConfigureLine,
       "mesPortEtherType": mesPortEtherType,
       "mesPortConfigureEtherType": mesPortConfigureEtherType,
       "mesPortNoOfMirrorSources": mesPortNoOfMirrorSources,
       "mesPortMirroring": mesPortMirroring,
       "mesPortIngressPushTag": mesPortIngressPushTag,
       "mesPortEgressPopTag": mesPortEgressPopTag,
       "mesPortDefaultCeVlanPriority": mesPortDefaultCeVlanPriority,
       "mesPortConfigureTagRule": mesPortConfigureTagRule,
       "mesPortCosProfile": mesPortCosProfile,
       "mesPortMode": mesPortMode,
       "mesPortPrioAssignment": mesPortPrioAssignment,
       "mesPortConfigurePrioAssignment": mesPortConfigurePrioAssignment,
       "mesPortNoOfTagRules": mesPortNoOfTagRules,
       "mesPortNoOfVlanSchedPrios": mesPortNoOfVlanSchedPrios,
       "mesPortObjectProperty": mesPortObjectProperty,
       "mesPortHighBitErrorRate": mesPortHighBitErrorRate,
       "mesPortIdx": mesPortIdx,
       "mesPortIfNo": mesPortIfNo,
       "mesPortClientIdx": mesPortClientIdx,
       "mesPortUpPortId": mesPortUpPortId,
       "mesPortLagPortmaskIf1": mesPortLagPortmaskIf1,
       "mesPortLagPortmaskIf2": mesPortLagPortmaskIf2,
       "mesPortLagPortmaskIf3": mesPortLagPortmaskIf3,
       "mesPortLagPortmaskIf4": mesPortLagPortmaskIf4,
       "mesPortLagPortmaskIf5": mesPortLagPortmaskIf5,
       "mesPortLagPortmaskIf6": mesPortLagPortmaskIf6,
       "mesPortLagPortmaskIf7": mesPortLagPortmaskIf7,
       "mesPortLagPortmaskIf8": mesPortLagPortmaskIf8,
       "mesPortAutoNegMasterSlaveCfg": mesPortAutoNegMasterSlaveCfg,
       "mesPortAutoNegMasterSlaveStatus": mesPortAutoNegMasterSlaveStatus,
       "mesPortLagPortmaskIf9": mesPortLagPortmaskIf9,
       "mesPortLagPortmaskIf10": mesPortLagPortmaskIf10,
       "mesPortLagPortmaskIf11": mesPortLagPortmaskIf11,
       "mesPortLagPortmaskIf12": mesPortLagPortmaskIf12,
       "mesPortLagPortmaskIf13": mesPortLagPortmaskIf13,
       "mesPortLagPortmaskIf14": mesPortLagPortmaskIf14,
       "mesPortLagPortmaskIf15": mesPortLagPortmaskIf15,
       "mesPortLagPortmaskIf16": mesPortLagPortmaskIf16,
       "mesPortCreateVlanTagClass": mesPortCreateVlanTagClass,
       "mesPortCreateTagRuleWoutClass": mesPortCreateTagRuleWoutClass,
       "mesPortTrustedPortmaskIf2": mesPortTrustedPortmaskIf2,
       "mesPortTrustedPortmaskIf3": mesPortTrustedPortmaskIf3,
       "mesPortTrustedPortmaskIf4": mesPortTrustedPortmaskIf4,
       "mesPortTrustedPortmaskIf5": mesPortTrustedPortmaskIf5,
       "mesPortTrustedPortmaskIf6": mesPortTrustedPortmaskIf6,
       "mesPortTrustedPortmaskIf7": mesPortTrustedPortmaskIf7,
       "mesPortTrustedPortmaskIf8": mesPortTrustedPortmaskIf8,
       "mesPortTrustedPortmaskIf9": mesPortTrustedPortmaskIf9,
       "mesPortTrustedPortmaskIf10": mesPortTrustedPortmaskIf10,
       "mesPortTrustedPortmaskIf11": mesPortTrustedPortmaskIf11,
       "mesPortTrustedPortmaskIf12": mesPortTrustedPortmaskIf12,
       "mesPortTrustedPortmaskIf13": mesPortTrustedPortmaskIf13,
       "mesPortTrustedPortmaskIf14": mesPortTrustedPortmaskIf14,
       "mesPortTrustedPortmaskIf15": mesPortTrustedPortmaskIf15,
       "mesPortTrustedPortmaskIf16": mesPortTrustedPortmaskIf16,
       "mesPortServiceId": mesPortServiceId,
       "mesVlanMapList": mesVlanMapList,
       "mesVlanMapTable": mesVlanMapTable,
       "mesVlanMapEntry": mesVlanMapEntry,
       "mesVlanMapIndex": mesVlanMapIndex,
       "mesVlanMapName": mesVlanMapName,
       "mesVlanMapVlanIdRangeLower": mesVlanMapVlanIdRangeLower,
       "mesVlanMapVlanIdRangeUpper": mesVlanMapVlanIdRangeUpper,
       "mesVlanMapInternalReference": mesVlanMapInternalReference,
       "mesVlanMapPortmask": mesVlanMapPortmask,
       "mesVlanMapConfigurePortMask": mesVlanMapConfigurePortMask,
       "mesVlanMapLearning": mesVlanMapLearning,
       "mesVlanMapEtherType": mesVlanMapEtherType,
       "mesVlanMapRowStatus": mesVlanMapRowStatus,
       "mesVlanMapDescr": mesVlanMapDescr,
       "mesVlanMapTrustPorts": mesVlanMapTrustPorts,
       "mesVlanMapRings": mesVlanMapRings,
       "mesVlanMapServiceId": mesVlanMapServiceId,
       "mesVlanMapPortmaskIf1": mesVlanMapPortmaskIf1,
       "mesVlanMapPortmaskIf2": mesVlanMapPortmaskIf2,
       "mesVlanMapPortmaskIf3": mesVlanMapPortmaskIf3,
       "mesVlanMapPortmaskIf4": mesVlanMapPortmaskIf4,
       "mesVlanMapPortmaskIf5": mesVlanMapPortmaskIf5,
       "mesVlanMapPortmaskIf6": mesVlanMapPortmaskIf6,
       "mesVlanMapPortmaskIf7": mesVlanMapPortmaskIf7,
       "mesVlanMapPortmaskIf8": mesVlanMapPortmaskIf8,
       "mesVlanMapPrepareConfigPortMask": mesVlanMapPrepareConfigPortMask,
       "mesVlanMapPortmaskIf9": mesVlanMapPortmaskIf9,
       "mesVlanMapPortmaskIf10": mesVlanMapPortmaskIf10,
       "mesVlanMapPortmaskIf11": mesVlanMapPortmaskIf11,
       "mesVlanMapPortmaskIf12": mesVlanMapPortmaskIf12,
       "mesVlanMapPortmaskIf13": mesVlanMapPortmaskIf13,
       "mesVlanMapPortmaskIf14": mesVlanMapPortmaskIf14,
       "mesVlanMapPortmaskIf15": mesVlanMapPortmaskIf15,
       "mesVlanMapPortmaskIf16": mesVlanMapPortmaskIf16,
       "mesVlanMapSubrack": mesVlanMapSubrack,
       "mesVlanMapSlot": mesVlanMapSlot,
       "mesVlanMapMacLearningLimit": mesVlanMapMacLearningLimit,
       "mesMgmtVlanList": mesMgmtVlanList,
       "mesMgmtVlanTable": mesMgmtVlanTable,
       "mesMgmtVlanEntry": mesMgmtVlanEntry,
       "mesMgmtVlanIndex": mesMgmtVlanIndex,
       "mesMgmtVlanName": mesMgmtVlanName,
       "mesMgmtVlanDescr": mesMgmtVlanDescr,
       "mesMgmtVlanSubrack": mesMgmtVlanSubrack,
       "mesMgmtVlanSlot": mesMgmtVlanSlot,
       "mesMgmtVlanTxPort": mesMgmtVlanTxPort,
       "mesMgmtVlanRxPort": mesMgmtVlanRxPort,
       "mesMgmtVlanObjectProperty": mesMgmtVlanObjectProperty,
       "mesMgmtVlanAdminStatus": mesMgmtVlanAdminStatus,
       "mesMgmtVlanConfigure": mesMgmtVlanConfigure,
       "mesMgmtVlanTagType": mesMgmtVlanTagType,
       "mesMgmtVlanEtherType": mesMgmtVlanEtherType,
       "mesMgmtVlanVlanId": mesMgmtVlanVlanId,
       "mesMgmtVlanPriority": mesMgmtVlanPriority,
       "mesMgmtVlanMacInMac": mesMgmtVlanMacInMac,
       "mesMgmtVlanMacInMacIsid": mesMgmtVlanMacInMacIsid,
       "mesMgmtVlanMacInMacDa": mesMgmtVlanMacInMacDa,
       "mesMgmtVlanForceMgmtVlan": mesMgmtVlanForceMgmtVlan,
       "mesMgmtVlanRings": mesMgmtVlanRings,
       "mesMgmtVlanIfNo": mesMgmtVlanIfNo,
       "mesLagList": mesLagList,
       "mesLagTable": mesLagTable,
       "mesLagEntry": mesLagEntry,
       "mesLagIndex": mesLagIndex,
       "mesLagName": mesLagName,
       "mesLagInternalReference": mesLagInternalReference,
       "mesLagPortmask": mesLagPortmask,
       "mesLagMasterIndex": mesLagMasterIndex,
       "mesLagConfigure": mesLagConfigure,
       "mesLagHash": mesLagHash,
       "mesLagIdentifier": mesLagIdentifier,
       "mesLagRowStatus": mesLagRowStatus,
       "mesLagLacpEnabled": mesLagLacpEnabled,
       "mesLagLacpSystemPriority": mesLagLacpSystemPriority,
       "mesLagLacpPeriod": mesLagLacpPeriod,
       "mesLagLacpLinkProtection": mesLagLacpLinkProtection,
       "mesLagDegraded": mesLagDegraded,
       "mesLagFailure": mesLagFailure,
       "mesLagLacpMaxNumberOfActiveLinks": mesLagLacpMaxNumberOfActiveLinks,
       "mesLagNoOfPorts": mesLagNoOfPorts,
       "mesLagLacpMinNumberOfActiveLinks": mesLagLacpMinNumberOfActiveLinks,
       "mesLagIsMcLag": mesLagIsMcLag,
       "mesLagConfigureTagRule": mesLagConfigureTagRule,
       "mesLagNoOfTagRules": mesLagNoOfTagRules,
       "mesLagDescr": mesLagDescr,
       "mesLagAdminStatus": mesLagAdminStatus,
       "mesLagOperStatus": mesLagOperStatus,
       "mesLagPortmaskIf1": mesLagPortmaskIf1,
       "mesLagPortmaskIf2": mesLagPortmaskIf2,
       "mesLagPortmaskIf3": mesLagPortmaskIf3,
       "mesLagPortmaskIf4": mesLagPortmaskIf4,
       "mesLagPortmaskIf5": mesLagPortmaskIf5,
       "mesLagPortmaskIf6": mesLagPortmaskIf6,
       "mesLagPortmaskIf7": mesLagPortmaskIf7,
       "mesLagPortmaskIf8": mesLagPortmaskIf8,
       "mesLagMasterIfNo": mesLagMasterIfNo,
       "mesLagMasterTxPort": mesLagMasterTxPort,
       "mesLagLocalId": mesLagLocalId,
       "mesLagPrepareConfigPortMask": mesLagPrepareConfigPortMask,
       "mesLagPortmaskIf9": mesLagPortmaskIf9,
       "mesLagPortmaskIf10": mesLagPortmaskIf10,
       "mesLagPortmaskIf11": mesLagPortmaskIf11,
       "mesLagPortmaskIf12": mesLagPortmaskIf12,
       "mesLagPortmaskIf13": mesLagPortmaskIf13,
       "mesLagPortmaskIf14": mesLagPortmaskIf14,
       "mesLagPortmaskIf15": mesLagPortmaskIf15,
       "mesLagPortmaskIf16": mesLagPortmaskIf16,
       "mesLagServiceId": mesLagServiceId,
       "mesPolicingList": mesPolicingList,
       "mesPolicingTable": mesPolicingTable,
       "mesPolicingEntry": mesPolicingEntry,
       "mesPolicingIndex": mesPolicingIndex,
       "mesPolicingName": mesPolicingName,
       "mesPolicingRate": mesPolicingRate,
       "mesPolicingBurstSize": mesPolicingBurstSize,
       "mesPolicingType": mesPolicingType,
       "mesPolicingInternalReference": mesPolicingInternalReference,
       "mesPolicingIdentifier": mesPolicingIdentifier,
       "mesPolicingUpId": mesPolicingUpId,
       "mesPolicingBurstSize2": mesPolicingBurstSize2,
       "mesPolicingId": mesPolicingId,
       "mesShapingList": mesShapingList,
       "mesShapingTable": mesShapingTable,
       "mesShapingEntry": mesShapingEntry,
       "mesShapingIndex": mesShapingIndex,
       "mesShapingName": mesShapingName,
       "mesShapingRate": mesShapingRate,
       "mesShapingBurstSize": mesShapingBurstSize,
       "mesShapingQueue": mesShapingQueue,
       "mesShapingInternalReference": mesShapingInternalReference,
       "mesShapingExcess": mesShapingExcess,
       "mesShapingIdentifier": mesShapingIdentifier,
       "mesShapingMinRate": mesShapingMinRate,
       "mesShapingLocalId": mesShapingLocalId,
       "mesCosList": mesCosList,
       "mesCosTable": mesCosTable,
       "mesCosEntry": mesCosEntry,
       "mesCosIndex": mesCosIndex,
       "mesCosName": mesCosName,
       "mesCosTxPort": mesCosTxPort,
       "mesCosMap": mesCosMap,
       "mesCosPriority0": mesCosPriority0,
       "mesCosPriority1": mesCosPriority1,
       "mesCosPriority2": mesCosPriority2,
       "mesCosPriority3": mesCosPriority3,
       "mesCosPriority4": mesCosPriority4,
       "mesCosPriority5": mesCosPriority5,
       "mesCosPriority6": mesCosPriority6,
       "mesCosPriority7": mesCosPriority7,
       "mesBwpMapList": mesBwpMapList,
       "mesBwpMapTable": mesBwpMapTable,
       "mesBwpMapEntry": mesBwpMapEntry,
       "mesBwpMapIndex": mesBwpMapIndex,
       "mesBwpMapName": mesBwpMapName,
       "mesBwpMapPortName": mesBwpMapPortName,
       "mesBwpMapBwpName": mesBwpMapBwpName,
       "mesBwpMapInternalReference": mesBwpMapInternalReference,
       "mesMirroringList": mesMirroringList,
       "mesMirroringTable": mesMirroringTable,
       "mesMirroringEntry": mesMirroringEntry,
       "mesMirroringIndex": mesMirroringIndex,
       "mesMirroringName": mesMirroringName,
       "mesMirroringDestination": mesMirroringDestination,
       "mesMirroringDirection": mesMirroringDirection,
       "mesMirroringConfigureDestination": mesMirroringConfigureDestination,
       "mesMirroringDestInterface": mesMirroringDestInterface,
       "mesMirroringDestTxPort": mesMirroringDestTxPort,
       "mesMirroringIfNo": mesMirroringIfNo,
       "mesMirroringTxPort": mesMirroringTxPort,
       "mesVlanTagRuleList": mesVlanTagRuleList,
       "mesVlanTagRuleTable": mesVlanTagRuleTable,
       "mesVlanTagRuleEntry": mesVlanTagRuleEntry,
       "mesVlanTagRuleIndex": mesVlanTagRuleIndex,
       "mesVlanTagRuleName": mesVlanTagRuleName,
       "mesVlanTagRuleInternalReference": mesVlanTagRuleInternalReference,
       "mesVlanTagRuleClassificationName": mesVlanTagRuleClassificationName,
       "mesVlanTagRuleType": mesVlanTagRuleType,
       "mesVlanTagRuleOperation": mesVlanTagRuleOperation,
       "mesVlanTagRuleInnerVlanId": mesVlanTagRuleInnerVlanId,
       "mesVlanTagRuleInnerPrio": mesVlanTagRuleInnerPrio,
       "mesVlanTagRuleOuterVlanId": mesVlanTagRuleOuterVlanId,
       "mesVlanTagRuleOuterPrio": mesVlanTagRuleOuterPrio,
       "mesVlanTagRulePrioAssignment": mesVlanTagRulePrioAssignment,
       "mesVlanTagRuleConfigurePrioAssignment": mesVlanTagRuleConfigurePrioAssignment,
       "mesVlanTagRuleQueue": mesVlanTagRuleQueue,
       "mesVlanTagRuleRowStatus": mesVlanTagRuleRowStatus,
       "mesVlanTagRuleInterfaceName": mesVlanTagRuleInterfaceName,
       "mesVlanTagClassVlanList": mesVlanTagClassVlanList,
       "mesVlanTagClassVlanTable": mesVlanTagClassVlanTable,
       "mesVlanTagClassVlanEntry": mesVlanTagClassVlanEntry,
       "mesVlanTagClassVlanIndex": mesVlanTagClassVlanIndex,
       "mesVlanTagClassVlanName": mesVlanTagClassVlanName,
       "mesVlanTagClassVlanTxPort": mesVlanTagClassVlanTxPort,
       "mesVlanTagClassVlanInternalReference": mesVlanTagClassVlanInternalReference,
       "mesVlanTagClassVlanRuleName": mesVlanTagClassVlanRuleName,
       "mesVlanTagClassVlanRuleIndex": mesVlanTagClassVlanRuleIndex,
       "mesVlanTagClassVlanOuterVlanId": mesVlanTagClassVlanOuterVlanId,
       "mesVlanTagClassVlanLagIndex": mesVlanTagClassVlanLagIndex,
       "mesVlanTagClassVlanResourceType": mesVlanTagClassVlanResourceType,
       "mesVlanTagClassVlanIfNo": mesVlanTagClassVlanIfNo,
       "mesVlanTagClassVlanLocalId": mesVlanTagClassVlanLocalId,
       "mesVlanTagClassVlanRowStatus": mesVlanTagClassVlanRowStatus,
       "mesCosProfileList": mesCosProfileList,
       "mesCosProfileTable": mesCosProfileTable,
       "mesCosProfileEntry": mesCosProfileEntry,
       "mesCosProfileIndex": mesCosProfileIndex,
       "mesCosProfileName": mesCosProfileName,
       "mesCosProfilePortmask": mesCosProfilePortmask,
       "mesCosProfileScheduler": mesCosProfileScheduler,
       "mesCosProfileWeight0": mesCosProfileWeight0,
       "mesCosProfileWeight1": mesCosProfileWeight1,
       "mesCosProfileWeight2": mesCosProfileWeight2,
       "mesCosProfileWeight3": mesCosProfileWeight3,
       "mesCosProfileWeight4": mesCosProfileWeight4,
       "mesCosProfileWeight5": mesCosProfileWeight5,
       "mesCosProfileWeight6": mesCosProfileWeight6,
       "mesCosProfileWeight7": mesCosProfileWeight7,
       "mesCosProfilePriority0": mesCosProfilePriority0,
       "mesCosProfilePriority1": mesCosProfilePriority1,
       "mesCosProfilePriority2": mesCosProfilePriority2,
       "mesCosProfilePriority3": mesCosProfilePriority3,
       "mesCosProfilePriority4": mesCosProfilePriority4,
       "mesCosProfilePriority5": mesCosProfilePriority5,
       "mesCosProfilePriority6": mesCosProfilePriority6,
       "mesCosProfilePriority7": mesCosProfilePriority7,
       "mesCosProfileConfigureScheduler": mesCosProfileConfigureScheduler,
       "mesCosProfileIngressPcpDecoding": mesCosProfileIngressPcpDecoding,
       "mesCosProfileIngressDeiDecoding": mesCosProfileIngressDeiDecoding,
       "mesCosProfileIngressColor0": mesCosProfileIngressColor0,
       "mesCosProfileIngressColor1": mesCosProfileIngressColor1,
       "mesCosProfileIngressColor2": mesCosProfileIngressColor2,
       "mesCosProfileIngressColor3": mesCosProfileIngressColor3,
       "mesCosProfileIngressColor4": mesCosProfileIngressColor4,
       "mesCosProfileIngressColor5": mesCosProfileIngressColor5,
       "mesCosProfileIngressColor6": mesCosProfileIngressColor6,
       "mesCosProfileIngressColor7": mesCosProfileIngressColor7,
       "mesCosProfileEgressPcpEncoding": mesCosProfileEgressPcpEncoding,
       "mesCosProfileEgressDeiEncoding": mesCosProfileEgressDeiEncoding,
       "mesCosProfileEgressPcpGreen0": mesCosProfileEgressPcpGreen0,
       "mesCosProfileEgressPcpGreen1": mesCosProfileEgressPcpGreen1,
       "mesCosProfileEgressPcpGreen2": mesCosProfileEgressPcpGreen2,
       "mesCosProfileEgressPcpGreen3": mesCosProfileEgressPcpGreen3,
       "mesCosProfileEgressPcpGreen4": mesCosProfileEgressPcpGreen4,
       "mesCosProfileEgressPcpGreen5": mesCosProfileEgressPcpGreen5,
       "mesCosProfileEgressPcpGreen6": mesCosProfileEgressPcpGreen6,
       "mesCosProfileEgressPcpGreen7": mesCosProfileEgressPcpGreen7,
       "mesCosProfileEgressPcpYellow0": mesCosProfileEgressPcpYellow0,
       "mesCosProfileEgressPcpYellow1": mesCosProfileEgressPcpYellow1,
       "mesCosProfileEgressPcpYellow2": mesCosProfileEgressPcpYellow2,
       "mesCosProfileEgressPcpYellow3": mesCosProfileEgressPcpYellow3,
       "mesCosProfileEgressPcpYellow4": mesCosProfileEgressPcpYellow4,
       "mesCosProfileEgressPcpYellow5": mesCosProfileEgressPcpYellow5,
       "mesCosProfileEgressPcpYellow6": mesCosProfileEgressPcpYellow6,
       "mesCosProfileEgressPcpYellow7": mesCosProfileEgressPcpYellow7,
       "mesCosProfilePortmaskIf1": mesCosProfilePortmaskIf1,
       "mesCosProfilePortmaskIf2": mesCosProfilePortmaskIf2,
       "mesCosProfilePortmaskIf3": mesCosProfilePortmaskIf3,
       "mesCosProfilePortmaskIf4": mesCosProfilePortmaskIf4,
       "mesCosProfilePortmaskIf5": mesCosProfilePortmaskIf5,
       "mesCosProfilePortmaskIf6": mesCosProfilePortmaskIf6,
       "mesCosProfilePortmaskIf7": mesCosProfilePortmaskIf7,
       "mesCosProfilePortmaskIf8": mesCosProfilePortmaskIf8,
       "mesCosProfilePortmaskIf9": mesCosProfilePortmaskIf9,
       "mesCosProfilePortmaskIf10": mesCosProfilePortmaskIf10,
       "mesCosProfilePortmaskIf11": mesCosProfilePortmaskIf11,
       "mesCosProfilePortmaskIf12": mesCosProfilePortmaskIf12,
       "mesCosProfilePortmaskIf13": mesCosProfilePortmaskIf13,
       "mesCosProfilePortmaskIf14": mesCosProfilePortmaskIf14,
       "mesCosProfilePortmaskIf15": mesCosProfilePortmaskIf15,
       "mesCosProfilePortmaskIf16": mesCosProfilePortmaskIf16,
       "mesMaidList": mesMaidList,
       "mesMaidTable": mesMaidTable,
       "mesMaidEntry": mesMaidEntry,
       "mesMaidIndex": mesMaidIndex,
       "mesMaidName": mesMaidName,
       "mesMaidGroupId": mesMaidGroupId,
       "mesMaidMdFormat": mesMaidMdFormat,
       "mesMaidMdName": mesMaidMdName,
       "mesMaidMdMac": mesMaidMdMac,
       "mesMaidMd2Octet": mesMaidMd2Octet,
       "mesMaidMdString": mesMaidMdString,
       "mesMaidLevel": mesMaidLevel,
       "mesMaidMaFormat": mesMaidMaFormat,
       "mesMaidMaName": mesMaidMaName,
       "mesMaidMaVpnOui": mesMaidMaVpnOui,
       "mesMaidMaVpnIndex": mesMaidMaVpnIndex,
       "mesMaidMa2Octet": mesMaidMa2Octet,
       "mesMaidMaVlan": mesMaidMaVlan,
       "mesMaidMaString": mesMaidMaString,
       "mesMaidCcmInterval": mesMaidCcmInterval,
       "mesMaidInternalReference": mesMaidInternalReference,
       "mesMaidIdentifier": mesMaidIdentifier,
       "mesMaidNoOfMeps": mesMaidNoOfMeps,
       "mesMaidAssociateMep": mesMaidAssociateMep,
       "mesMaidReleaseMeps": mesMaidReleaseMeps,
       "mesMaidRowStatus": mesMaidRowStatus,
       "mesMaidNoOfUpMeps": mesMaidNoOfUpMeps,
       "mesMaidLocalDeviceType": mesMaidLocalDeviceType,
       "mesMaidViewFilter": mesMaidViewFilter,
       "mesMaidNoOfNidMeps": mesMaidNoOfNidMeps,
       "mesMaidAssociateMepNid": mesMaidAssociateMepNid,
       "mesMaidAssociateMepAdvanced": mesMaidAssociateMepAdvanced,
       "mesMaidSubrack": mesMaidSubrack,
       "mesMaidSlot": mesMaidSlot,
       "mesMaidServiceId": mesMaidServiceId,
       "mesCfmMepList": mesCfmMepList,
       "mesCfmMepTable": mesCfmMepTable,
       "mesCfmMepEntry": mesCfmMepEntry,
       "mesCfmMepIndex": mesCfmMepIndex,
       "mesCfmMepName": mesCfmMepName,
       "mesCfmMepMaid": mesCfmMepMaid,
       "mesCfmMepTxPort": mesCfmMepTxPort,
       "mesCfmMepPortName": mesCfmMepPortName,
       "mesCfmMepAdminStatus": mesCfmMepAdminStatus,
       "mesCfmMepOperStatus": mesCfmMepOperStatus,
       "mesCfmMepPrimaryVid": mesCfmMepPrimaryVid,
       "mesCfmMepVlanPriority": mesCfmMepVlanPriority,
       "mesCfmMepType": mesCfmMepType,
       "mesCfmMepIdentifier": mesCfmMepIdentifier,
       "mesCfmMepInternalReference": mesCfmMepInternalReference,
       "mesCfmMepRDICCM": mesCfmMepRDICCM,
       "mesCfmMepMACstatus": mesCfmMepMACstatus,
       "mesCfmMepRemoteCCM": mesCfmMepRemoteCCM,
       "mesCfmMepErrorCCM": mesCfmMepErrorCCM,
       "mesCfmMepXconCCM": mesCfmMepXconCCM,
       "mesCfmMepAis": mesCfmMepAis,
       "mesCfmMepChangePort": mesCfmMepChangePort,
       "mesCfmMepTransmitLbrStatus": mesCfmMepTransmitLbrStatus,
       "mesCfmMepRowStatus": mesCfmMepRowStatus,
       "mesCfmMepDirection": mesCfmMepDirection,
       "mesCfmMepCcmSeqNumStatus": mesCfmMepCcmSeqNumStatus,
       "mesCfmMepRemoteCsfLos": mesCfmMepRemoteCsfLos,
       "mesCfmMepRemoteCsfRdi": mesCfmMepRemoteCsfRdi,
       "mesCfmMepRemoteCsfFdi": mesCfmMepRemoteCsfFdi,
       "mesCfmMepLocalCsfLos": mesCfmMepLocalCsfLos,
       "mesCfmMepLocalDeviceType": mesCfmMepLocalDeviceType,
       "mesCfmMepLocalDeviceName": mesCfmMepLocalDeviceName,
       "mesCfmMepLocalDeviceId": mesCfmMepLocalDeviceId,
       "mesCfmMepViewFilter": mesCfmMepViewFilter,
       "mesCfmMepUnexpectedPeriod": mesCfmMepUnexpectedPeriod,
       "mesCfmMepUnexpectedMepId": mesCfmMepUnexpectedMepId,
       "mesCfmMepUnexpectedMegLevel": mesCfmMepUnexpectedMegLevel,
       "mesCfmMepMismerge": mesCfmMepMismerge,
       "mesCfmMepNoOfLMs": mesCfmMepNoOfLMs,
       "mesCfmMepNoOfDMs": mesCfmMepNoOfDMs,
       "mesCfmMepAssociateLM": mesCfmMepAssociateLM,
       "mesCfmMepAssociateDM": mesCfmMepAssociateDM,
       "mesCfmMepTransmitDmrStatus": mesCfmMepTransmitDmrStatus,
       "mesCfmMepTransmitLmrStatus": mesCfmMepTransmitLmrStatus,
       "mesCfmMepLmCosAwareness": mesCfmMepLmCosAwareness,
       "mesCfmMepResourceType": mesCfmMepResourceType,
       "mesCfmMepLagId": mesCfmMepLagId,
       "mesCfmMepInterfaceName": mesCfmMepInterfaceName,
       "mesCfmMepIfNo": mesCfmMepIfNo,
       "mesCfmMepLocalId": mesCfmMepLocalId,
       "mesCfmMepSubrack": mesCfmMepSubrack,
       "mesCfmMepSlot": mesCfmMepSlot,
       "mesCfmMepServiceId": mesCfmMepServiceId,
       "mesErpList": mesErpList,
       "mesErpTable": mesErpTable,
       "mesErpEntry": mesErpEntry,
       "mesErpIndex": mesErpIndex,
       "mesErpName": mesErpName,
       "mesErpPortLeft": mesErpPortLeft,
       "mesErpPortRight": mesErpPortRight,
       "mesErpAdminStatus": mesErpAdminStatus,
       "mesErpInternalReference": mesErpInternalReference,
       "mesErpDescr": mesErpDescr,
       "mesErpVlanId": mesErpVlanId,
       "mesErpMegLevel": mesErpMegLevel,
       "mesErpProtLink": mesErpProtLink,
       "mesErpGuardTime": mesErpGuardTime,
       "mesErpHoldOffTime": mesErpHoldOffTime,
       "mesErpWtrTime": mesErpWtrTime,
       "mesErpOamDetectionLeft": mesErpOamDetectionLeft,
       "mesErpOamDetectionRight": mesErpOamDetectionRight,
       "mesErpStatusLeft": mesErpStatusLeft,
       "mesErpStatusRight": mesErpStatusRight,
       "mesErpProtState": mesErpProtState,
       "mesErpActiveEvent": mesErpActiveEvent,
       "mesErpRapsReqState": mesErpRapsReqState,
       "mesErpServiceFailure": mesErpServiceFailure,
       "mesErpServiceDegraded": mesErpServiceDegraded,
       "mesErpUnexpectedMegLevel": mesErpUnexpectedMegLevel,
       "mesErpCommunicationFailure": mesErpCommunicationFailure,
       "mesErpChangePort": mesErpChangePort,
       "mesErpRowStatus": mesErpRowStatus,
       "mesErpNodeType": mesErpNodeType,
       "mesErpProtectionMode": mesErpProtectionMode,
       "mesErpVersion": mesErpVersion,
       "mesErpMajorName": mesErpMajorName,
       "mesErpRingId": mesErpRingId,
       "mesErpRingIndex": mesErpRingIndex,
       "mesErpOperatorCommand": mesErpOperatorCommand,
       "mesErpGroupId": mesErpGroupId,
       "mesErpSwitchInformation": mesErpSwitchInformation,
       "mesErpTopologyChangePropagation": mesErpTopologyChangePropagation,
       "mesErpSubRings": mesErpSubRings,
       "mesErpResourceTypeLeft": mesErpResourceTypeLeft,
       "mesErpLagIdLeft": mesErpLagIdLeft,
       "mesErpResourceTypeRight": mesErpResourceTypeRight,
       "mesErpLagIdRight": mesErpLagIdRight,
       "mesErpInterfaceLeft": mesErpInterfaceLeft,
       "mesErpInterfaceRight": mesErpInterfaceRight,
       "mesErpProvisioningMismatch": mesErpProvisioningMismatch,
       "mesErpIfNoLeft": mesErpIfNoLeft,
       "mesErpTxPortLeft": mesErpTxPortLeft,
       "mesErpIfNoRight": mesErpIfNoRight,
       "mesErpTxPortRight": mesErpTxPortRight,
       "mesErpOamDetectionVlanId": mesErpOamDetectionVlanId,
       "mesClassList": mesClassList,
       "mesClassTable": mesClassTable,
       "mesClassEntry": mesClassEntry,
       "mesClassIndex": mesClassIndex,
       "mesClassName": mesClassName,
       "mesClassIdentifier": mesClassIdentifier,
       "mesClassInternalReference": mesClassInternalReference,
       "mesClassPort": mesClassPort,
       "mesClassLagId": mesClassLagId,
       "mesClassOuterVlanId": mesClassOuterVlanId,
       "mesClassOuterVlanPcp": mesClassOuterVlanPcp,
       "mesClassPrecedence": mesClassPrecedence,
       "mesClassDaMacAddress": mesClassDaMacAddress,
       "mesClassAssociateAction": mesClassAssociateAction,
       "mesClassRowStatus": mesClassRowStatus,
       "mesClassDaMacAddressMask": mesClassDaMacAddressMask,
       "mesClassInnerVlanId": mesClassInnerVlanId,
       "mesClassInnerVlanPcp": mesClassInnerVlanPcp,
       "mesClassDSCP": mesClassDSCP,
       "mesClassInnerVlanCfi": mesClassInnerVlanCfi,
       "mesClassOuterVlanCfi": mesClassOuterVlanCfi,
       "mesClassDirection": mesClassDirection,
       "mesClassOuterTpid": mesClassOuterTpid,
       "mesClassInternalClassId": mesClassInternalClassId,
       "mesClassSourceAddressIPV4": mesClassSourceAddressIPV4,
       "mesClassSourceMaskIPV4": mesClassSourceMaskIPV4,
       "mesClassDestAddressIPV4": mesClassDestAddressIPV4,
       "mesClassDestMaskIPV4": mesClassDestMaskIPV4,
       "mesClassSubrack": mesClassSubrack,
       "mesClassSlot": mesClassSlot,
       "mesClassVlanStackStructure": mesClassVlanStackStructure,
       "mesClassServiceId": mesClassServiceId,
       "mesClassEthertype": mesClassEthertype,
       "mesClassIfNo": mesClassIfNo,
       "mesClassTxPort": mesClassTxPort,
       "mesClassAssociateActionAdvanced": mesClassAssociateActionAdvanced,
       "mesActionList": mesActionList,
       "mesActionTable": mesActionTable,
       "mesActionEntry": mesActionEntry,
       "mesActionIndex": mesActionIndex,
       "mesActionName": mesActionName,
       "mesActionIdentifier": mesActionIdentifier,
       "mesActionInternalReference": mesActionInternalReference,
       "mesActionType": mesActionType,
       "mesActionOuterVlanId": mesActionOuterVlanId,
       "mesActionPcp": mesActionPcp,
       "mesActionPolicerId": mesActionPolicerId,
       "mesActionInnerVlanId": mesActionInnerVlanId,
       "mesActionQueue": mesActionQueue,
       "mesActionRowStatus": mesActionRowStatus,
       "mesActionRedirectPort": mesActionRedirectPort,
       "mesActionServiceId": mesActionServiceId,
       "mesActionRedirectIfNo": mesActionRedirectIfNo,
       "mesActionRedirectTxPort": mesActionRedirectTxPort,
       "mesActionClassId": mesActionClassId,
       "mesActionSubrack": mesActionSubrack,
       "mesActionSlot": mesActionSlot,
       "mesPolicyList": mesPolicyList,
       "mesPolicyTable": mesPolicyTable,
       "mesPolicyEntry": mesPolicyEntry,
       "mesPolicyIndex": mesPolicyIndex,
       "mesPolicyName": mesPolicyName,
       "mesPolicyInternalReference": mesPolicyInternalReference,
       "mesPolicyClass": mesPolicyClass,
       "mesPolicyAction": mesPolicyAction,
       "mesPolicyServiceId": mesPolicyServiceId,
       "mesErrorPropList": mesErrorPropList,
       "mesErrorPropTable": mesErrorPropTable,
       "mesErrorPropEntry": mesErrorPropEntry,
       "mesErrorPropIndex": mesErrorPropIndex,
       "mesErrorPropName": mesErrorPropName,
       "mesErrorPropDescr": mesErrorPropDescr,
       "mesErrorPropInternalReference": mesErrorPropInternalReference,
       "mesErrorPropAdminStatus": mesErrorPropAdminStatus,
       "mesErrorPropOperStatus": mesErrorPropOperStatus,
       "mesErrorPropState": mesErrorPropState,
       "mesErrorPropTriggerType": mesErrorPropTriggerType,
       "mesErrorPropTriggerObject": mesErrorPropTriggerObject,
       "mesErrorPropTriggerPortIndex": mesErrorPropTriggerPortIndex,
       "mesErrorPropTriggerMepIndex": mesErrorPropTriggerMepIndex,
       "mesErrorPropActionType": mesErrorPropActionType,
       "mesErrorPropActionObject": mesErrorPropActionObject,
       "mesErrorPropActionPortIndex": mesErrorPropActionPortIndex,
       "mesErrorPropActionMepIndex": mesErrorPropActionMepIndex,
       "mesErrorPropHoldOffTimer": mesErrorPropHoldOffTimer,
       "mesErrorPropRowStatus": mesErrorPropRowStatus,
       "mesErrorPropFault": mesErrorPropFault,
       "mesErrorPropActionErpIndex": mesErrorPropActionErpIndex,
       "mesErrorPropTriggerLagIndex": mesErrorPropTriggerLagIndex,
       "mesErrorPropSubrack": mesErrorPropSubrack,
       "mesErrorPropSlot": mesErrorPropSlot,
       "mesErrorPropServiceId": mesErrorPropServiceId,
       "mesVlanProtList": mesVlanProtList,
       "mesVlanProtTable": mesVlanProtTable,
       "mesVlanProtEntry": mesVlanProtEntry,
       "mesVlanProtIndex": mesVlanProtIndex,
       "mesVlanProtName": mesVlanProtName,
       "mesVlanProtInternalReference": mesVlanProtInternalReference,
       "mesVlanProtRings": mesVlanProtRings,
       "mesVlanProtProtectedVlan": mesVlanProtProtectedVlan,
       "mesVlanProtGroupId": mesVlanProtGroupId,
       "mesVlanProtIdentifier": mesVlanProtIdentifier,
       "mesVlanProtAddRingAction": mesVlanProtAddRingAction,
       "mesVlanProtRemoveRingAction": mesVlanProtRemoveRingAction,
       "mesVlanProtDescr": mesVlanProtDescr,
       "mesVlanProtChangeVlansAction": mesVlanProtChangeVlansAction,
       "mesLacpList": mesLacpList,
       "mesLacpTable": mesLacpTable,
       "mesLacpEntry": mesLacpEntry,
       "mesLacpIndex": mesLacpIndex,
       "mesLacpName": mesLacpName,
       "mesLacpInternalReference": mesLacpInternalReference,
       "mesLacpLagIdentifier": mesLacpLagIdentifier,
       "mesLacpLagId": mesLacpLagId,
       "mesLacpPortPriority": mesLacpPortPriority,
       "mesLacpSelected": mesLacpSelected,
       "mesLacpReceiveState": mesLacpReceiveState,
       "mesLacpTransmitState": mesLacpTransmitState,
       "mesLacpMuxState": mesLacpMuxState,
       "mesLacpActorExpired": mesLacpActorExpired,
       "mesLacpActorDefault": mesLacpActorDefault,
       "mesLacpActorDistributing": mesLacpActorDistributing,
       "mesLacpActorCollecting": mesLacpActorCollecting,
       "mesLacpActorSynchronization": mesLacpActorSynchronization,
       "mesLacpActorAggregation": mesLacpActorAggregation,
       "mesLacpActorTimeout": mesLacpActorTimeout,
       "mesLacpActorActivity": mesLacpActorActivity,
       "mesLacpPartnerExpired": mesLacpPartnerExpired,
       "mesLacpPartnerDefault": mesLacpPartnerDefault,
       "mesLacpPartnerDistributing": mesLacpPartnerDistributing,
       "mesLacpPartnerCollecting": mesLacpPartnerCollecting,
       "mesLacpPartnerSynchronization": mesLacpPartnerSynchronization,
       "mesLacpPartnerAggregation": mesLacpPartnerAggregation,
       "mesLacpPartnerTimeout": mesLacpPartnerTimeout,
       "mesLacpPartnerActivity": mesLacpPartnerActivity,
       "mesLacpTxLacpPdus": mesLacpTxLacpPdus,
       "mesLacpRxLacpPdus": mesLacpRxLacpPdus,
       "mesLacpInternalIndex": mesLacpInternalIndex,
       "mesLacpResetCounters": mesLacpResetCounters,
       "mesLacpIfNo": mesLacpIfNo,
       "mesLacpTxPort": mesLacpTxPort,
       "mesLacpUpPortId": mesLacpUpPortId}
)
