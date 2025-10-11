# SNMP MIB module (ZXEPON-TRAP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/zte/ZXEPON-TRAP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:44:50 2025
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
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

(zxAnEponMib,) = mibBuilder.importSymbols(
    "ZTE-MASTER-MIB",
    "zxAnEponMib")

(onuOnlineForwardAction,
 onuRegisterLoid) = mibBuilder.importSymbols(
    "ZXEPON-SERVICE-PRIVATE-MIB",
    "onuOnlineForwardAction",
    "onuRegisterLoid")


# MODULE-IDENTITY

zxAnEponTrap = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 10)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ZxAnEponTrapOlt_ObjectIdentity = ObjectIdentity
zxAnEponTrapOlt = _ZxAnEponTrapOlt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 10, 1)
)
_ZxAnEponTrapBindVar_ObjectIdentity = ObjectIdentity
zxAnEponTrapBindVar = _ZxAnEponTrapBindVar_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 10, 2)
)


class _ZxAnEponTrapDid_Type(OctetString):
    """Custom type zxAnEponTrapDid based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ZxAnEponTrapDid_Type.__name__ = "OctetString"
_ZxAnEponTrapDid_Object = MibScalar
zxAnEponTrapDid = _ZxAnEponTrapDid_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 10, 2, 1),
    _ZxAnEponTrapDid_Type()
)
zxAnEponTrapDid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponTrapDid.setStatus("current")


class _ZxAnEponTrapMac_Type(OctetString):
    """Custom type zxAnEponTrapMac based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ZxAnEponTrapMac_Type.__name__ = "OctetString"
_ZxAnEponTrapMac_Object = MibScalar
zxAnEponTrapMac = _ZxAnEponTrapMac_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 10, 2, 2),
    _ZxAnEponTrapMac_Type()
)
zxAnEponTrapMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponTrapMac.setStatus("current")


class _ZxAnEponTrapIp_Type(OctetString):
    """Custom type zxAnEponTrapIp based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ZxAnEponTrapIp_Type.__name__ = "OctetString"
_ZxAnEponTrapIp_Object = MibScalar
zxAnEponTrapIp = _ZxAnEponTrapIp_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 10, 2, 3),
    _ZxAnEponTrapIp_Type()
)
zxAnEponTrapIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponTrapIp.setStatus("current")


class _ZxAnEponTrapMask_Type(OctetString):
    """Custom type zxAnEponTrapMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ZxAnEponTrapMask_Type.__name__ = "OctetString"
_ZxAnEponTrapMask_Object = MibScalar
zxAnEponTrapMask = _ZxAnEponTrapMask_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 10, 2, 4),
    _ZxAnEponTrapMask_Type()
)
zxAnEponTrapMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponTrapMask.setStatus("current")


class _ZxAnEponTrapOnuType_Type(OctetString):
    """Custom type zxAnEponTrapOnuType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ZxAnEponTrapOnuType_Type.__name__ = "OctetString"
_ZxAnEponTrapOnuType_Object = MibScalar
zxAnEponTrapOnuType = _ZxAnEponTrapOnuType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 10, 2, 5),
    _ZxAnEponTrapOnuType_Type()
)
zxAnEponTrapOnuType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponTrapOnuType.setStatus("current")


class _ZxAnEponTrapOnuName_Type(OctetString):
    """Custom type zxAnEponTrapOnuName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ZxAnEponTrapOnuName_Type.__name__ = "OctetString"
_ZxAnEponTrapOnuName_Object = MibScalar
zxAnEponTrapOnuName = _ZxAnEponTrapOnuName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 10, 2, 6),
    _ZxAnEponTrapOnuName_Type()
)
zxAnEponTrapOnuName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponTrapOnuName.setStatus("current")


class _ZxAnEponTrapPonLosReason_Type(Integer32):
    """Custom type zxAnEponTrapPonLosReason based on Integer32"""
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
        *(("fiberBroken", 1),
          ("otherReasons", 2),
          ("allOnuDyingGasp", 3),
          ("allOnuNeverOnline", 4))
    )


_ZxAnEponTrapPonLosReason_Type.__name__ = "Integer32"
_ZxAnEponTrapPonLosReason_Object = MibScalar
zxAnEponTrapPonLosReason = _ZxAnEponTrapPonLosReason_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 10, 2, 7),
    _ZxAnEponTrapPonLosReason_Type()
)
zxAnEponTrapPonLosReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponTrapPonLosReason.setStatus("current")


class _ZxAnEponTrapOnuOffLineReason_Type(Integer32):
    """Custom type zxAnEponTrapOnuOffLineReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("subtrunkfibrebreak", 1),
          ("onupoweroff", 2))
    )


_ZxAnEponTrapOnuOffLineReason_Type.__name__ = "Integer32"
_ZxAnEponTrapOnuOffLineReason_Object = MibScalar
zxAnEponTrapOnuOffLineReason = _ZxAnEponTrapOnuOffLineReason_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 10, 2, 8),
    _ZxAnEponTrapOnuOffLineReason_Type()
)
zxAnEponTrapOnuOffLineReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponTrapOnuOffLineReason.setStatus("current")


class _ZxAnEponTrapOltPortName_Type(OctetString):
    """Custom type zxAnEponTrapOltPortName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ZxAnEponTrapOltPortName_Type.__name__ = "OctetString"
_ZxAnEponTrapOltPortName_Object = MibScalar
zxAnEponTrapOltPortName = _ZxAnEponTrapOltPortName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 10, 2, 9),
    _ZxAnEponTrapOltPortName_Type()
)
zxAnEponTrapOltPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponTrapOltPortName.setStatus("current")


class _ZxAnEponTrapOnuModel_Type(OctetString):
    """Custom type zxAnEponTrapOnuModel based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ZxAnEponTrapOnuModel_Type.__name__ = "OctetString"
_ZxAnEponTrapOnuModel_Object = MibScalar
zxAnEponTrapOnuModel = _ZxAnEponTrapOnuModel_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 10, 2, 10),
    _ZxAnEponTrapOnuModel_Type()
)
zxAnEponTrapOnuModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponTrapOnuModel.setStatus("current")


class _ZxAnEponTrapOnuDesc_Type(OctetString):
    """Custom type zxAnEponTrapOnuDesc based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ZxAnEponTrapOnuDesc_Type.__name__ = "OctetString"
_ZxAnEponTrapOnuDesc_Object = MibScalar
zxAnEponTrapOnuDesc = _ZxAnEponTrapOnuDesc_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 10, 2, 11),
    _ZxAnEponTrapOnuDesc_Type()
)
zxAnEponTrapOnuDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponTrapOnuDesc.setStatus("current")


class _ZxAnEponTrapTime_Type(OctetString):
    """Custom type zxAnEponTrapTime based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ZxAnEponTrapTime_Type.__name__ = "OctetString"
_ZxAnEponTrapTime_Object = MibScalar
zxAnEponTrapTime = _ZxAnEponTrapTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 10, 2, 12),
    _ZxAnEponTrapTime_Type()
)
zxAnEponTrapTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponTrapTime.setStatus("current")
_ZxAnEponRogueOnuIdList_Type = ObjectIdentifier
_ZxAnEponRogueOnuIdList_Object = MibScalar
zxAnEponRogueOnuIdList = _ZxAnEponRogueOnuIdList_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 10, 2, 13),
    _ZxAnEponRogueOnuIdList_Type()
)
zxAnEponRogueOnuIdList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponRogueOnuIdList.setStatus("current")
_ZxAnEponHighProbabilityRogueOnuIdList_Type = ObjectIdentifier
_ZxAnEponHighProbabilityRogueOnuIdList_Object = MibScalar
zxAnEponHighProbabilityRogueOnuIdList = _ZxAnEponHighProbabilityRogueOnuIdList_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 10, 2, 14),
    _ZxAnEponHighProbabilityRogueOnuIdList_Type()
)
zxAnEponHighProbabilityRogueOnuIdList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponHighProbabilityRogueOnuIdList.setStatus("current")
_ZxAnEponLowProbabilityRogueOnuIdList_Type = ObjectIdentifier
_ZxAnEponLowProbabilityRogueOnuIdList_Object = MibScalar
zxAnEponLowProbabilityRogueOnuIdList = _ZxAnEponLowProbabilityRogueOnuIdList_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 10, 2, 15),
    _ZxAnEponLowProbabilityRogueOnuIdList_Type()
)
zxAnEponLowProbabilityRogueOnuIdList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponLowProbabilityRogueOnuIdList.setStatus("current")


class _ZxAnEponRogueUnauthOnuList_Type(OctetString):
    """Custom type zxAnEponRogueUnauthOnuList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 768),
    )


_ZxAnEponRogueUnauthOnuList_Type.__name__ = "OctetString"
_ZxAnEponRogueUnauthOnuList_Object = MibScalar
zxAnEponRogueUnauthOnuList = _ZxAnEponRogueUnauthOnuList_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 10, 2, 16),
    _ZxAnEponRogueUnauthOnuList_Type()
)
zxAnEponRogueUnauthOnuList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponRogueUnauthOnuList.setStatus("current")


class _ZxAnEponHighPossibilityRogueUnauthOnuList_Type(OctetString):
    """Custom type zxAnEponHighPossibilityRogueUnauthOnuList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 768),
    )


_ZxAnEponHighPossibilityRogueUnauthOnuList_Type.__name__ = "OctetString"
_ZxAnEponHighPossibilityRogueUnauthOnuList_Object = MibScalar
zxAnEponHighPossibilityRogueUnauthOnuList = _ZxAnEponHighPossibilityRogueUnauthOnuList_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 10, 2, 17),
    _ZxAnEponHighPossibilityRogueUnauthOnuList_Type()
)
zxAnEponHighPossibilityRogueUnauthOnuList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponHighPossibilityRogueUnauthOnuList.setStatus("current")


class _ZxAnEponLowPossibilityRogueUnauthOnuList_Type(OctetString):
    """Custom type zxAnEponLowPossibilityRogueUnauthOnuList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 768),
    )


_ZxAnEponLowPossibilityRogueUnauthOnuList_Type.__name__ = "OctetString"
_ZxAnEponLowPossibilityRogueUnauthOnuList_Object = MibScalar
zxAnEponLowPossibilityRogueUnauthOnuList = _ZxAnEponLowPossibilityRogueUnauthOnuList_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 10, 2, 18),
    _ZxAnEponLowPossibilityRogueUnauthOnuList_Type()
)
zxAnEponLowPossibilityRogueUnauthOnuList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponLowPossibilityRogueUnauthOnuList.setStatus("current")


class _ZxAnEponOnuActualSpeedType_Type(Integer32):
    """Custom type zxAnEponOnuActualSpeedType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("upDownstream1G", 1),
          ("upDownstream10G", 2),
          ("upstream1GAndDownstream10G", 3))
    )


_ZxAnEponOnuActualSpeedType_Type.__name__ = "Integer32"
_ZxAnEponOnuActualSpeedType_Object = MibScalar
zxAnEponOnuActualSpeedType = _ZxAnEponOnuActualSpeedType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 10, 2, 19),
    _ZxAnEponOnuActualSpeedType_Type()
)
zxAnEponOnuActualSpeedType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponOnuActualSpeedType.setStatus("current")


class _ZxAnEponOnuConfigSpeedType_Type(Integer32):
    """Custom type zxAnEponOnuConfigSpeedType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("upDownstream1G", 1),
          ("upDownstream10G", 2),
          ("upstream1GAndDownstream10G", 3))
    )


_ZxAnEponOnuConfigSpeedType_Type.__name__ = "Integer32"
_ZxAnEponOnuConfigSpeedType_Object = MibScalar
zxAnEponOnuConfigSpeedType = _ZxAnEponOnuConfigSpeedType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 10, 2, 20),
    _ZxAnEponOnuConfigSpeedType_Type()
)
zxAnEponOnuConfigSpeedType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponOnuConfigSpeedType.setStatus("current")
_ZxAnEponOnuIfIndex_Type = Integer32
_ZxAnEponOnuIfIndex_Object = MibScalar
zxAnEponOnuIfIndex = _ZxAnEponOnuIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 10, 2, 21),
    _ZxAnEponOnuIfIndex_Type()
)
zxAnEponOnuIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponOnuIfIndex.setStatus("current")
_ZxAnEponTrapEvent_ObjectIdentity = ObjectIdentity
zxAnEponTrapEvent = _ZxAnEponTrapEvent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 10, 3)
)


class _ZxAnEponTrapEventString_Type(OctetString):
    """Custom type zxAnEponTrapEventString based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_ZxAnEponTrapEventString_Type.__name__ = "OctetString"
_ZxAnEponTrapEventString_Object = MibScalar
zxAnEponTrapEventString = _ZxAnEponTrapEventString_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 10, 3, 1),
    _ZxAnEponTrapEventString_Type()
)
zxAnEponTrapEventString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponTrapEventString.setStatus("current")
_ZxAnEponTrapOnu_ObjectIdentity = ObjectIdentity
zxAnEponTrapOnu = _ZxAnEponTrapOnu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 10, 4)
)
_ZxAnEponOnuTrapInfo_ObjectIdentity = ObjectIdentity
zxAnEponOnuTrapInfo = _ZxAnEponOnuTrapInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 10, 4, 1)
)
_ZxAnEponOnuOamObjType_Type = Integer32
_ZxAnEponOnuOamObjType_Object = MibScalar
zxAnEponOnuOamObjType = _ZxAnEponOnuOamObjType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 10, 4, 1, 1),
    _ZxAnEponOnuOamObjType_Type()
)
zxAnEponOnuOamObjType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponOnuOamObjType.setStatus("current")
_ZxAnEponOnuOamInstanceNum_Type = Integer32
_ZxAnEponOnuOamInstanceNum_Object = MibScalar
zxAnEponOnuOamInstanceNum = _ZxAnEponOnuOamInstanceNum_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 10, 4, 1, 2),
    _ZxAnEponOnuOamInstanceNum_Type()
)
zxAnEponOnuOamInstanceNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponOnuOamInstanceNum.setStatus("current")
_ZxAnEponOnuOamAlarmId_Type = Integer32
_ZxAnEponOnuOamAlarmId_Object = MibScalar
zxAnEponOnuOamAlarmId = _ZxAnEponOnuOamAlarmId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 10, 4, 1, 3),
    _ZxAnEponOnuOamAlarmId_Type()
)
zxAnEponOnuOamAlarmId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponOnuOamAlarmId.setStatus("current")
_ZxAnEponOnuOamTimeStamp_Type = Integer32
_ZxAnEponOnuOamTimeStamp_Object = MibScalar
zxAnEponOnuOamTimeStamp = _ZxAnEponOnuOamTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 10, 4, 1, 4),
    _ZxAnEponOnuOamTimeStamp_Type()
)
zxAnEponOnuOamTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponOnuOamTimeStamp.setStatus("current")
_ZxAnEponOnuOamAlarmState_Type = Integer32
_ZxAnEponOnuOamAlarmState_Object = MibScalar
zxAnEponOnuOamAlarmState = _ZxAnEponOnuOamAlarmState_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 10, 4, 1, 5),
    _ZxAnEponOnuOamAlarmState_Type()
)
zxAnEponOnuOamAlarmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponOnuOamAlarmState.setStatus("current")


class _ZxAnEponOnuOamAlarmInfo_Type(DisplayString):
    """Custom type zxAnEponOnuOamAlarmInfo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_ZxAnEponOnuOamAlarmInfo_Type.__name__ = "DisplayString"
_ZxAnEponOnuOamAlarmInfo_Object = MibScalar
zxAnEponOnuOamAlarmInfo = _ZxAnEponOnuOamAlarmInfo_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 10, 4, 1, 6),
    _ZxAnEponOnuOamAlarmInfo_Type()
)
zxAnEponOnuOamAlarmInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponOnuOamAlarmInfo.setStatus("current")


class _ZxAnEponOnuActionResult_Type(Integer32):
    """Custom type zxAnEponOnuActionResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("success", 1),
          ("fail", 2))
    )


_ZxAnEponOnuActionResult_Type.__name__ = "Integer32"
_ZxAnEponOnuActionResult_Object = MibScalar
zxAnEponOnuActionResult = _ZxAnEponOnuActionResult_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 10, 4, 1, 7),
    _ZxAnEponOnuActionResult_Type()
)
zxAnEponOnuActionResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponOnuActionResult.setStatus("current")


class _ZxAnEponOnuLuminousEmissionStatus_Type(Integer32):
    """Custom type zxAnEponOnuLuminousEmissionStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_ZxAnEponOnuLuminousEmissionStatus_Type.__name__ = "Integer32"
_ZxAnEponOnuLuminousEmissionStatus_Object = MibScalar
zxAnEponOnuLuminousEmissionStatus = _ZxAnEponOnuLuminousEmissionStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 10, 4, 1, 8),
    _ZxAnEponOnuLuminousEmissionStatus_Type()
)
zxAnEponOnuLuminousEmissionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponOnuLuminousEmissionStatus.setStatus("current")


class _ZxAnEponOnuDataChannelLinkStatus_Type(Integer32):
    """Custom type zxAnEponOnuDataChannelLinkStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_ZxAnEponOnuDataChannelLinkStatus_Type.__name__ = "Integer32"
_ZxAnEponOnuDataChannelLinkStatus_Object = MibScalar
zxAnEponOnuDataChannelLinkStatus = _ZxAnEponOnuDataChannelLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 10, 4, 1, 9),
    _ZxAnEponOnuDataChannelLinkStatus_Type()
)
zxAnEponOnuDataChannelLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponOnuDataChannelLinkStatus.setStatus("current")


class _ZxAnEponOnuFirmwareVersionUpdateStatus_Type(Integer32):
    """Custom type zxAnEponOnuFirmwareVersionUpdateStatus based on Integer32"""
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
        *(("notstart", 1),
          ("updatefailed", 2),
          ("downloading", 3),
          ("writingimage", 4),
          ("updatefinished", 5))
    )


_ZxAnEponOnuFirmwareVersionUpdateStatus_Type.__name__ = "Integer32"
_ZxAnEponOnuFirmwareVersionUpdateStatus_Object = MibScalar
zxAnEponOnuFirmwareVersionUpdateStatus = _ZxAnEponOnuFirmwareVersionUpdateStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 10, 4, 1, 10),
    _ZxAnEponOnuFirmwareVersionUpdateStatus_Type()
)
zxAnEponOnuFirmwareVersionUpdateStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponOnuFirmwareVersionUpdateStatus.setStatus("current")


class _ZxAnEponOnuFirmwareVersionUpdateFailedReason_Type(Integer32):
    """Custom type zxAnEponOnuFirmwareVersionUpdateFailedReason based on Integer32"""
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
        *(("none", 1),
          ("downloaderror", 2),
          ("downloadtimeout", 3),
          ("onureturnerror", 4),
          ("userabort", 5),
          ("onuoffline", 6))
    )


_ZxAnEponOnuFirmwareVersionUpdateFailedReason_Type.__name__ = "Integer32"
_ZxAnEponOnuFirmwareVersionUpdateFailedReason_Object = MibScalar
zxAnEponOnuFirmwareVersionUpdateFailedReason = _ZxAnEponOnuFirmwareVersionUpdateFailedReason_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 10, 4, 1, 11),
    _ZxAnEponOnuFirmwareVersionUpdateFailedReason_Type()
)
zxAnEponOnuFirmwareVersionUpdateFailedReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponOnuFirmwareVersionUpdateFailedReason.setStatus("current")
_ZxAnEponOnuBaseTrap_ObjectIdentity = ObjectIdentity
zxAnEponOnuBaseTrap = _ZxAnEponOnuBaseTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 10, 4, 2)
)
_ZxAnEponOnuPonIfTrap_ObjectIdentity = ObjectIdentity
zxAnEponOnuPonIfTrap = _ZxAnEponOnuPonIfTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 10, 4, 3)
)
_ZxAnEponOnuCardTrap_ObjectIdentity = ObjectIdentity
zxAnEponOnuCardTrap = _ZxAnEponOnuCardTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 10, 4, 4)
)
_ZxAnEponOnuPortTrap_ObjectIdentity = ObjectIdentity
zxAnEponOnuPortTrap = _ZxAnEponOnuPortTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 10, 4, 5)
)

# Managed Objects groups


# Notification objects

zxAnEponOnuBerOverThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 10, 1, 1)
)
zxAnEponOnuBerOverThreshold.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ZXEPON-TRAP-MIB", "zxAnEponTrapEventString"),
        ("ZXEPON-TRAP-MIB", "zxAnEponTrapOnuType"),
        ("ZXEPON-TRAP-MIB", "zxAnEponTrapOltPortName"),
        ("ZXEPON-TRAP-MIB", "zxAnEponTrapOnuDesc"))
)
if mibBuilder.loadTexts:
    zxAnEponOnuBerOverThreshold.setStatus(
        "current"
    )

zxAnEponOnuBerOverThresholdRestore = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 10, 1, 2)
)
zxAnEponOnuBerOverThresholdRestore.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ZXEPON-TRAP-MIB", "zxAnEponTrapEventString"),
        ("ZXEPON-TRAP-MIB", "zxAnEponTrapOnuType"),
        ("ZXEPON-TRAP-MIB", "zxAnEponTrapOltPortName"),
        ("ZXEPON-TRAP-MIB", "zxAnEponTrapOnuDesc"))
)
if mibBuilder.loadTexts:
    zxAnEponOnuBerOverThresholdRestore.setStatus(
        "current"
    )

zxAnEponDeviceOltPortBerState = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 10, 1, 11)
)
zxAnEponDeviceOltPortBerState.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ZXEPON-TRAP-MIB", "zxAnEponTrapOltPortName"))
)
if mibBuilder.loadTexts:
    zxAnEponDeviceOltPortBerState.setStatus(
        "current"
    )

zxAnEponDeviceOltPortBerStateRestore = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 10, 1, 12)
)
zxAnEponDeviceOltPortBerStateRestore.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ZXEPON-TRAP-MIB", "zxAnEponTrapOltPortName"))
)
if mibBuilder.loadTexts:
    zxAnEponDeviceOltPortBerStateRestore.setStatus(
        "current"
    )

zxAnEponPonLOS = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 10, 1, 13)
)
zxAnEponPonLOS.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ZXEPON-TRAP-MIB", "zxAnEponTrapPonLosReason"),
        ("ZXEPON-TRAP-MIB", "zxAnEponTrapOltPortName"))
)
if mibBuilder.loadTexts:
    zxAnEponPonLOS.setStatus(
        "current"
    )

zxAnEponPonLOSRestore = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 10, 1, 14)
)
zxAnEponPonLOSRestore.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ZXEPON-TRAP-MIB", "zxAnEponTrapPonLosReason"),
        ("ZXEPON-TRAP-MIB", "zxAnEponTrapOltPortName"))
)
if mibBuilder.loadTexts:
    zxAnEponPonLOSRestore.setStatus(
        "current"
    )

zxAnEponOnuOffLine = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 10, 1, 15)
)
zxAnEponOnuOffLine.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ZXEPON-TRAP-MIB", "zxAnEponTrapOnuOffLineReason"),
        ("ZXEPON-TRAP-MIB", "zxAnEponTrapOnuType"),
        ("ZXEPON-TRAP-MIB", "zxAnEponTrapOltPortName"),
        ("ZXEPON-TRAP-MIB", "zxAnEponTrapOnuDesc"),
        ("ZXEPON-TRAP-MIB", "zxAnEponTrapDid"))
)
if mibBuilder.loadTexts:
    zxAnEponOnuOffLine.setStatus(
        "current"
    )

zxAnEponOnuOffLineRestore = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 10, 1, 16)
)
zxAnEponOnuOffLineRestore.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ZXEPON-TRAP-MIB", "zxAnEponTrapOnuOffLineReason"),
        ("ZXEPON-TRAP-MIB", "zxAnEponTrapOnuType"),
        ("ZXEPON-TRAP-MIB", "zxAnEponTrapOltPortName"),
        ("ZXEPON-TRAP-MIB", "zxAnEponTrapOnuDesc"),
        ("ZXEPON-TRAP-MIB", "zxAnEponTrapDid"))
)
if mibBuilder.loadTexts:
    zxAnEponOnuOffLineRestore.setStatus(
        "current"
    )

zxAnEponOnuErroredSymbolPeriodEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 10, 1, 17)
)
zxAnEponOnuErroredSymbolPeriodEvent.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ZXEPON-TRAP-MIB", "zxAnEponTrapOnuType"),
        ("ZXEPON-TRAP-MIB", "zxAnEponTrapOltPortName"),
        ("ZXEPON-TRAP-MIB", "zxAnEponTrapOnuDesc"))
)
if mibBuilder.loadTexts:
    zxAnEponOnuErroredSymbolPeriodEvent.setStatus(
        "current"
    )

zxAnEponOnuErroredSymbolPeriodEventRestore = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 10, 1, 18)
)
zxAnEponOnuErroredSymbolPeriodEventRestore.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ZXEPON-TRAP-MIB", "zxAnEponTrapOnuType"),
        ("ZXEPON-TRAP-MIB", "zxAnEponTrapOltPortName"),
        ("ZXEPON-TRAP-MIB", "zxAnEponTrapOnuDesc"))
)
if mibBuilder.loadTexts:
    zxAnEponOnuErroredSymbolPeriodEventRestore.setStatus(
        "current"
    )

zxAnEponOnuErroredFrameEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 10, 1, 19)
)
zxAnEponOnuErroredFrameEvent.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ZXEPON-TRAP-MIB", "zxAnEponTrapOnuType"),
        ("ZXEPON-TRAP-MIB", "zxAnEponTrapOltPortName"),
        ("ZXEPON-TRAP-MIB", "zxAnEponTrapOnuDesc"))
)
if mibBuilder.loadTexts:
    zxAnEponOnuErroredFrameEvent.setStatus(
        "current"
    )

zxAnEponOnuErroredFrameEventRestore = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 10, 1, 20)
)
zxAnEponOnuErroredFrameEventRestore.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ZXEPON-TRAP-MIB", "zxAnEponTrapOnuType"),
        ("ZXEPON-TRAP-MIB", "zxAnEponTrapOltPortName"),
        ("ZXEPON-TRAP-MIB", "zxAnEponTrapOnuDesc"))
)
if mibBuilder.loadTexts:
    zxAnEponOnuErroredFrameEventRestore.setStatus(
        "current"
    )

zxAnEponOnuErroredFramePeriodEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 10, 1, 21)
)
zxAnEponOnuErroredFramePeriodEvent.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ZXEPON-TRAP-MIB", "zxAnEponTrapOnuType"),
        ("ZXEPON-TRAP-MIB", "zxAnEponTrapOltPortName"),
        ("ZXEPON-TRAP-MIB", "zxAnEponTrapOnuDesc"))
)
if mibBuilder.loadTexts:
    zxAnEponOnuErroredFramePeriodEvent.setStatus(
        "current"
    )

zxAnEponOnuErroredFramePeriodEventRestore = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 10, 1, 22)
)
zxAnEponOnuErroredFramePeriodEventRestore.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ZXEPON-TRAP-MIB", "zxAnEponTrapOnuType"),
        ("ZXEPON-TRAP-MIB", "zxAnEponTrapOltPortName"),
        ("ZXEPON-TRAP-MIB", "zxAnEponTrapOnuDesc"))
)
if mibBuilder.loadTexts:
    zxAnEponOnuErroredFramePeriodEventRestore.setStatus(
        "current"
    )

zxAnEponOnuErroredFrameSecondsSummaryEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 10, 1, 23)
)
zxAnEponOnuErroredFrameSecondsSummaryEvent.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ZXEPON-TRAP-MIB", "zxAnEponTrapOnuType"),
        ("ZXEPON-TRAP-MIB", "zxAnEponTrapOltPortName"),
        ("ZXEPON-TRAP-MIB", "zxAnEponTrapOnuDesc"))
)
if mibBuilder.loadTexts:
    zxAnEponOnuErroredFrameSecondsSummaryEvent.setStatus(
        "current"
    )

zxAnEponOnuErroredFrameSecondsSummaryEventRestore = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 10, 1, 24)
)
zxAnEponOnuErroredFrameSecondsSummaryEventRestore.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ZXEPON-TRAP-MIB", "zxAnEponTrapOnuType"),
        ("ZXEPON-TRAP-MIB", "zxAnEponTrapOltPortName"),
        ("ZXEPON-TRAP-MIB", "zxAnEponTrapOnuDesc"))
)
if mibBuilder.loadTexts:
    zxAnEponOnuErroredFrameSecondsSummaryEventRestore.setStatus(
        "current"
    )

zxAnEponOnuUplinkBitError = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 10, 1, 25)
)
zxAnEponOnuUplinkBitError.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ZXEPON-TRAP-MIB", "zxAnEponTrapOnuType"),
        ("ZXEPON-TRAP-MIB", "zxAnEponTrapOltPortName"),
        ("ZXEPON-TRAP-MIB", "zxAnEponTrapOnuDesc"))
)
if mibBuilder.loadTexts:
    zxAnEponOnuUplinkBitError.setStatus(
        "current"
    )

zxAnEponOnuUplinkBitErrorRestore = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 10, 1, 26)
)
zxAnEponOnuUplinkBitErrorRestore.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ZXEPON-TRAP-MIB", "zxAnEponTrapOnuType"),
        ("ZXEPON-TRAP-MIB", "zxAnEponTrapOltPortName"),
        ("ZXEPON-TRAP-MIB", "zxAnEponTrapOnuDesc"))
)
if mibBuilder.loadTexts:
    zxAnEponOnuUplinkBitErrorRestore.setStatus(
        "current"
    )

zxAnEponOnuUplinkFrameError = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 10, 1, 27)
)
zxAnEponOnuUplinkFrameError.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ZXEPON-TRAP-MIB", "zxAnEponTrapOnuType"),
        ("ZXEPON-TRAP-MIB", "zxAnEponTrapOltPortName"),
        ("ZXEPON-TRAP-MIB", "zxAnEponTrapOnuDesc"))
)
if mibBuilder.loadTexts:
    zxAnEponOnuUplinkFrameError.setStatus(
        "current"
    )

zxAnEponOnuUplinkFrameErrorRestore = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 10, 1, 28)
)
zxAnEponOnuUplinkFrameErrorRestore.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ZXEPON-TRAP-MIB", "zxAnEponTrapOnuType"),
        ("ZXEPON-TRAP-MIB", "zxAnEponTrapOltPortName"),
        ("ZXEPON-TRAP-MIB", "zxAnEponTrapOnuDesc"))
)
if mibBuilder.loadTexts:
    zxAnEponOnuUplinkFrameErrorRestore.setStatus(
        "current"
    )

zxAnEponOnuAuthSuccMsg = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 10, 1, 29)
)
zxAnEponOnuAuthSuccMsg.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ZXEPON-TRAP-MIB", "zxAnEponTrapOnuType"),
        ("ZXEPON-TRAP-MIB", "zxAnEponTrapOltPortName"),
        ("ZXEPON-TRAP-MIB", "zxAnEponTrapOnuDesc"),
        ("ZXEPON-SERVICE-PRIVATE-MIB", "onuOnlineForwardAction"),
        ("ZXEPON-TRAP-MIB", "zxAnEponOnuActualSpeedType"))
)
if mibBuilder.loadTexts:
    zxAnEponOnuAuthSuccMsg.setStatus(
        "current"
    )

zxAnEponPonOpticalTransceiverLos = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 10, 1, 30)
)
zxAnEponPonOpticalTransceiverLos.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ZXEPON-TRAP-MIB", "zxAnEponTrapOltPortName"))
)
if mibBuilder.loadTexts:
    zxAnEponPonOpticalTransceiverLos.setStatus(
        "current"
    )

zxAnEponPonOpticalTransceiverLosRestore = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 10, 1, 31)
)
zxAnEponPonOpticalTransceiverLosRestore.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ZXEPON-TRAP-MIB", "zxAnEponTrapOltPortName"))
)
if mibBuilder.loadTexts:
    zxAnEponPonOpticalTransceiverLosRestore.setStatus(
        "current"
    )

zxAnEponLoidConflict = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 10, 1, 32)
)
zxAnEponLoidConflict.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ZXEPON-SERVICE-PRIVATE-MIB", "onuRegisterLoid"),
        ("ZXEPON-TRAP-MIB", "zxAnEponTrapMac"),
        ("ZXEPON-TRAP-MIB", "zxAnEponOnuIfIndex"))
)
if mibBuilder.loadTexts:
    zxAnEponLoidConflict.setStatus(
        "current"
    )

zxAnEponTrapEventOltReset = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 10, 3, 2)
)
zxAnEponTrapEventOltReset.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ZXEPON-TRAP-MIB", "zxAnEponTrapOltPortName"))
)
if mibBuilder.loadTexts:
    zxAnEponTrapEventOltReset.setStatus(
        "current"
    )

zxAnEponTrapEventOnuOffline = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 10, 3, 3)
)
zxAnEponTrapEventOnuOffline.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    zxAnEponTrapEventOnuOffline.setStatus(
        "current"
    )

zxAnEponTrapEventOnuOnline = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 10, 3, 4)
)
zxAnEponTrapEventOnuOnline.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    zxAnEponTrapEventOnuOnline.setStatus(
        "current"
    )

zxAnEponTrapEventExtendedOamDiscoveryFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 10, 3, 5)
)
zxAnEponTrapEventExtendedOamDiscoveryFail.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ZXEPON-TRAP-MIB", "zxAnEponTrapOltPortName"),
        ("ZXEPON-TRAP-MIB", "zxAnEponTrapOnuDesc"))
)
if mibBuilder.loadTexts:
    zxAnEponTrapEventExtendedOamDiscoveryFail.setStatus(
        "current"
    )

zxAnEponTrapEventLocalOnuConfigureFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 10, 3, 6)
)
zxAnEponTrapEventLocalOnuConfigureFail.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ZXEPON-TRAP-MIB", "zxAnEponTrapOnuType"),
        ("ZXEPON-TRAP-MIB", "zxAnEponTrapOltPortName"),
        ("ZXEPON-TRAP-MIB", "zxAnEponTrapOnuDesc"))
)
if mibBuilder.loadTexts:
    zxAnEponTrapEventLocalOnuConfigureFail.setStatus(
        "current"
    )

zxAnEponTrapEventUnkownOnuOffline = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 10, 3, 7)
)
zxAnEponTrapEventUnkownOnuOffline.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ZXEPON-TRAP-MIB", "zxAnEponTrapEventString"),
        ("ZXEPON-TRAP-MIB", "zxAnEponTrapOnuType"),
        ("ZXEPON-TRAP-MIB", "zxAnEponTrapOltPortName"),
        ("ZXEPON-TRAP-MIB", "zxAnEponTrapDid"))
)
if mibBuilder.loadTexts:
    zxAnEponTrapEventUnkownOnuOffline.setStatus(
        "current"
    )

zxAnEponTrapEventDenyUnkownOnuRegister = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 10, 3, 8)
)
zxAnEponTrapEventDenyUnkownOnuRegister.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ZXEPON-TRAP-MIB", "zxAnEponTrapEventString"),
        ("ZXEPON-TRAP-MIB", "zxAnEponTrapOnuType"),
        ("ZXEPON-TRAP-MIB", "zxAnEponTrapOltPortName"),
        ("ZXEPON-TRAP-MIB", "zxAnEponTrapDid"))
)
if mibBuilder.loadTexts:
    zxAnEponTrapEventDenyUnkownOnuRegister.setStatus(
        "current"
    )

zxAnEponTrapEventUnkownOnuOnline = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 10, 3, 9)
)
zxAnEponTrapEventUnkownOnuOnline.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ZXEPON-TRAP-MIB", "zxAnEponTrapEventString"),
        ("ZXEPON-TRAP-MIB", "zxAnEponTrapOnuType"),
        ("ZXEPON-TRAP-MIB", "zxAnEponTrapOltPortName"),
        ("ZXEPON-TRAP-MIB", "zxAnEponTrapDid"))
)
if mibBuilder.loadTexts:
    zxAnEponTrapEventUnkownOnuOnline.setStatus(
        "current"
    )

zxAnEponTrapEventRemoteOnuConfigureFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 10, 3, 10)
)
zxAnEponTrapEventRemoteOnuConfigureFail.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ZXEPON-TRAP-MIB", "zxAnEponTrapEventString"))
)
if mibBuilder.loadTexts:
    zxAnEponTrapEventRemoteOnuConfigureFail.setStatus(
        "current"
    )

zxAnEponTrapEventTransparent = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 10, 3, 11)
)
zxAnEponTrapEventTransparent.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ZXEPON-TRAP-MIB", "zxAnEponTrapEventString"),
        ("ZXEPON-TRAP-MIB", "zxAnEponTrapOnuType"),
        ("ZXEPON-TRAP-MIB", "zxAnEponTrapOltPortName"),
        ("ZXEPON-TRAP-MIB", "zxAnEponTrapOnuDesc"))
)
if mibBuilder.loadTexts:
    zxAnEponTrapEventTransparent.setStatus(
        "current"
    )

zxAnEponTrapEventOnuDyingGasp = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 10, 3, 12)
)
zxAnEponTrapEventOnuDyingGasp.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ZXEPON-TRAP-MIB", "zxAnEponTrapOnuType"),
        ("ZXEPON-TRAP-MIB", "zxAnEponTrapOltPortName"),
        ("ZXEPON-TRAP-MIB", "zxAnEponTrapOnuDesc"))
)
if mibBuilder.loadTexts:
    zxAnEponTrapEventOnuDyingGasp.setStatus(
        "current"
    )

zxAnEponTrapEventOnuAutoConfigRequest = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 10, 3, 13)
)
zxAnEponTrapEventOnuAutoConfigRequest.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ZXEPON-TRAP-MIB", "zxAnEponTrapDid"),
        ("ZXEPON-TRAP-MIB", "zxAnEponTrapMac"),
        ("ZXEPON-TRAP-MIB", "zxAnEponTrapIp"),
        ("ZXEPON-TRAP-MIB", "zxAnEponTrapMask"),
        ("ZXEPON-TRAP-MIB", "zxAnEponTrapOnuType"),
        ("ZXEPON-TRAP-MIB", "zxAnEponTrapOnuDesc"))
)
if mibBuilder.loadTexts:
    zxAnEponTrapEventOnuAutoConfigRequest.setStatus(
        "current"
    )

zxAnEponTrapEventOnuIpNotAutoConfig = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 10, 3, 14)
)
zxAnEponTrapEventOnuIpNotAutoConfig.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ZXEPON-TRAP-MIB", "zxAnEponTrapEventString"))
)
if mibBuilder.loadTexts:
    zxAnEponTrapEventOnuIpNotAutoConfig.setStatus(
        "current"
    )

zxAnEponTrapEventOnuPowerOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 10, 3, 15)
)
zxAnEponTrapEventOnuPowerOff.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ZXEPON-TRAP-MIB", "zxAnEponTrapOltPortName"),
        ("ZXEPON-TRAP-MIB", "zxAnEponTrapOnuType"),
        ("ZXEPON-TRAP-MIB", "zxAnEponTrapOnuDesc"),
        ("ZXEPON-TRAP-MIB", "zxAnEponTrapDid"))
)
if mibBuilder.loadTexts:
    zxAnEponTrapEventOnuPowerOff.setStatus(
        "current"
    )

zxAnEponTrapEventOnuPowerOffRestore = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 10, 3, 16)
)
zxAnEponTrapEventOnuPowerOffRestore.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ZXEPON-TRAP-MIB", "zxAnEponTrapOltPortName"),
        ("ZXEPON-TRAP-MIB", "zxAnEponTrapOnuType"),
        ("ZXEPON-TRAP-MIB", "zxAnEponTrapOnuDesc"),
        ("ZXEPON-TRAP-MIB", "zxAnEponTrapDid"))
)
if mibBuilder.loadTexts:
    zxAnEponTrapEventOnuPowerOffRestore.setStatus(
        "current"
    )

zxAnEponTrapEventOnuUnauthenticate = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 10, 3, 17)
)
zxAnEponTrapEventOnuUnauthenticate.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ZXEPON-TRAP-MIB", "zxAnEponTrapDid"),
        ("ZXEPON-TRAP-MIB", "zxAnEponTrapMac"),
        ("ZXEPON-TRAP-MIB", "zxAnEponTrapOnuType"),
        ("ZXEPON-TRAP-MIB", "zxAnEponTrapTime"))
)
if mibBuilder.loadTexts:
    zxAnEponTrapEventOnuUnauthenticate.setStatus(
        "current"
    )

zxAnEponTrapEventOnuConstantOptical = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 10, 3, 18)
)
zxAnEponTrapEventOnuConstantOptical.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ZXEPON-TRAP-MIB", "zxAnEponTrapOltPortName"),
        ("ZXEPON-TRAP-MIB", "zxAnEponTrapOnuType"),
        ("ZXEPON-TRAP-MIB", "zxAnEponTrapOnuDesc"),
        ("ZXEPON-TRAP-MIB", "zxAnEponRogueOnuIdList"),
        ("ZXEPON-TRAP-MIB", "zxAnEponHighProbabilityRogueOnuIdList"),
        ("ZXEPON-TRAP-MIB", "zxAnEponLowProbabilityRogueOnuIdList"),
        ("ZXEPON-TRAP-MIB", "zxAnEponRogueUnauthOnuList"),
        ("ZXEPON-TRAP-MIB", "zxAnEponHighPossibilityRogueUnauthOnuList"),
        ("ZXEPON-TRAP-MIB", "zxAnEponLowPossibilityRogueUnauthOnuList"))
)
if mibBuilder.loadTexts:
    zxAnEponTrapEventOnuConstantOptical.setStatus(
        "current"
    )

zxAnEponTrapEventOnuConstantOpticalRestore = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 10, 3, 19)
)
zxAnEponTrapEventOnuConstantOpticalRestore.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ZXEPON-TRAP-MIB", "zxAnEponTrapOltPortName"),
        ("ZXEPON-TRAP-MIB", "zxAnEponTrapOnuType"),
        ("ZXEPON-TRAP-MIB", "zxAnEponTrapOnuDesc"),
        ("ZXEPON-TRAP-MIB", "zxAnEponRogueOnuIdList"),
        ("ZXEPON-TRAP-MIB", "zxAnEponHighProbabilityRogueOnuIdList"),
        ("ZXEPON-TRAP-MIB", "zxAnEponLowProbabilityRogueOnuIdList"),
        ("ZXEPON-TRAP-MIB", "zxAnEponRogueUnauthOnuList"),
        ("ZXEPON-TRAP-MIB", "zxAnEponHighPossibilityRogueUnauthOnuList"),
        ("ZXEPON-TRAP-MIB", "zxAnEponLowPossibilityRogueUnauthOnuList"))
)
if mibBuilder.loadTexts:
    zxAnEponTrapEventOnuConstantOpticalRestore.setStatus(
        "current"
    )

zxAnEponTrapEventPonResetFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 10, 3, 20)
)
zxAnEponTrapEventPonResetFailed.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ZXEPON-TRAP-MIB", "zxAnEponTrapOltPortName"))
)
if mibBuilder.loadTexts:
    zxAnEponTrapEventPonResetFailed.setStatus(
        "current"
    )

zxAnEponOnuSpeedTypeMismatchTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 10, 3, 21)
)
zxAnEponOnuSpeedTypeMismatchTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ZXEPON-TRAP-MIB", "zxAnEponTrapMac"),
        ("ZXEPON-TRAP-MIB", "zxAnEponTrapOnuType"),
        ("ZXEPON-TRAP-MIB", "zxAnEponTrapTime"),
        ("ZXEPON-TRAP-MIB", "zxAnEponOnuActualSpeedType"),
        ("ZXEPON-TRAP-MIB", "zxAnEponOnuConfigSpeedType"),
        ("ZXEPON-TRAP-MIB", "zxAnEponTrapDid"))
)
if mibBuilder.loadTexts:
    zxAnEponOnuSpeedTypeMismatchTrap.setStatus(
        "current"
    )

zxAnEponOnuOamV21Message = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 10, 4, 1, 101)
)
zxAnEponOnuOamV21Message.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ZXEPON-TRAP-MIB", "zxAnEponOnuOamObjType"),
        ("ZXEPON-TRAP-MIB", "zxAnEponOnuOamInstanceNum"),
        ("ZXEPON-TRAP-MIB", "zxAnEponOnuOamAlarmId"),
        ("ZXEPON-TRAP-MIB", "zxAnEponOnuOamTimeStamp"),
        ("ZXEPON-TRAP-MIB", "zxAnEponOnuOamAlarmState"),
        ("ZXEPON-TRAP-MIB", "zxAnEponOnuOamAlarmInfo"))
)
if mibBuilder.loadTexts:
    zxAnEponOnuOamV21Message.setStatus(
        "current"
    )

zxAnEponOnuEquipmentAlm = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 10, 4, 2, 1)
)
zxAnEponOnuEquipmentAlm.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ZXEPON-TRAP-MIB", "zxAnEponOnuOamTimeStamp"),
        ("ZXEPON-TRAP-MIB", "zxAnEponOnuOamAlarmInfo"))
)
if mibBuilder.loadTexts:
    zxAnEponOnuEquipmentAlm.setStatus(
        "current"
    )

zxAnEponOnuEquipmentRestore = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 10, 4, 2, 2)
)
zxAnEponOnuEquipmentRestore.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ZXEPON-TRAP-MIB", "zxAnEponOnuOamTimeStamp"),
        ("ZXEPON-TRAP-MIB", "zxAnEponOnuOamAlarmInfo"))
)
if mibBuilder.loadTexts:
    zxAnEponOnuEquipmentRestore.setStatus(
        "current"
    )

zxAnEponOnuPowerAlm = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 10, 4, 2, 3)
)
zxAnEponOnuPowerAlm.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ZXEPON-TRAP-MIB", "zxAnEponOnuOamTimeStamp"),
        ("ZXEPON-TRAP-MIB", "zxAnEponOnuOamAlarmInfo"))
)
if mibBuilder.loadTexts:
    zxAnEponOnuPowerAlm.setStatus(
        "current"
    )

zxAnEponOnuPowerRestore = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 10, 4, 2, 4)
)
zxAnEponOnuPowerRestore.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ZXEPON-TRAP-MIB", "zxAnEponOnuOamTimeStamp"),
        ("ZXEPON-TRAP-MIB", "zxAnEponOnuOamAlarmInfo"))
)
if mibBuilder.loadTexts:
    zxAnEponOnuPowerRestore.setStatus(
        "current"
    )

zxAnEponOnuButteryMissingAlm = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 10, 4, 2, 5)
)
zxAnEponOnuButteryMissingAlm.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ZXEPON-TRAP-MIB", "zxAnEponOnuOamTimeStamp"))
)
if mibBuilder.loadTexts:
    zxAnEponOnuButteryMissingAlm.setStatus(
        "current"
    )

zxAnEponOnuButteryMissingRestore = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 10, 4, 2, 6)
)
zxAnEponOnuButteryMissingRestore.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ZXEPON-TRAP-MIB", "zxAnEponOnuOamTimeStamp"))
)
if mibBuilder.loadTexts:
    zxAnEponOnuButteryMissingRestore.setStatus(
        "current"
    )

zxAnEponOnuButteryFailureAlm = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 10, 4, 2, 7)
)
zxAnEponOnuButteryFailureAlm.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ZXEPON-TRAP-MIB", "zxAnEponOnuOamTimeStamp"))
)
if mibBuilder.loadTexts:
    zxAnEponOnuButteryFailureAlm.setStatus(
        "current"
    )

zxAnEponOnuButteryFailureRestore = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 10, 4, 2, 8)
)
zxAnEponOnuButteryFailureRestore.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ZXEPON-TRAP-MIB", "zxAnEponOnuOamTimeStamp"))
)
if mibBuilder.loadTexts:
    zxAnEponOnuButteryFailureRestore.setStatus(
        "current"
    )

zxAnEponOnuButteryVoltLowAlm = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 10, 4, 2, 9)
)
zxAnEponOnuButteryVoltLowAlm.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ZXEPON-TRAP-MIB", "zxAnEponOnuOamTimeStamp"),
        ("ZXEPON-TRAP-MIB", "zxAnEponOnuOamAlarmInfo"))
)
if mibBuilder.loadTexts:
    zxAnEponOnuButteryVoltLowAlm.setStatus(
        "current"
    )

zxAnEponOnuButteryVoltLowRestore = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 10, 4, 2, 10)
)
zxAnEponOnuButteryVoltLowRestore.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ZXEPON-TRAP-MIB", "zxAnEponOnuOamTimeStamp"),
        ("ZXEPON-TRAP-MIB", "zxAnEponOnuOamAlarmInfo"))
)
if mibBuilder.loadTexts:
    zxAnEponOnuButteryVoltLowRestore.setStatus(
        "current"
    )

zxAnEponOnuPhysicalIntrusionAlm = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 10, 4, 2, 11)
)
zxAnEponOnuPhysicalIntrusionAlm.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ZXEPON-TRAP-MIB", "zxAnEponOnuOamTimeStamp"))
)
if mibBuilder.loadTexts:
    zxAnEponOnuPhysicalIntrusionAlm.setStatus(
        "current"
    )

zxAnEponOnuPhysicalIntrusionRestore = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 10, 4, 2, 12)
)
zxAnEponOnuPhysicalIntrusionRestore.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ZXEPON-TRAP-MIB", "zxAnEponOnuOamTimeStamp"))
)
if mibBuilder.loadTexts:
    zxAnEponOnuPhysicalIntrusionRestore.setStatus(
        "current"
    )

zxAnEponOnuSelfTestFailureAlm = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 10, 4, 2, 13)
)
zxAnEponOnuSelfTestFailureAlm.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ZXEPON-TRAP-MIB", "zxAnEponOnuOamTimeStamp"),
        ("ZXEPON-TRAP-MIB", "zxAnEponOnuOamAlarmInfo"))
)
if mibBuilder.loadTexts:
    zxAnEponOnuSelfTestFailureAlm.setStatus(
        "current"
    )

zxAnEponOnuSelfTestFailureRestore = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 10, 4, 2, 14)
)
zxAnEponOnuSelfTestFailureRestore.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ZXEPON-TRAP-MIB", "zxAnEponOnuOamTimeStamp"),
        ("ZXEPON-TRAP-MIB", "zxAnEponOnuOamAlarmInfo"))
)
if mibBuilder.loadTexts:
    zxAnEponOnuSelfTestFailureRestore.setStatus(
        "current"
    )

zxAnEponOnuTempHighAlm = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 10, 4, 2, 15)
)
zxAnEponOnuTempHighAlm.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ZXEPON-TRAP-MIB", "zxAnEponOnuOamTimeStamp"),
        ("ZXEPON-TRAP-MIB", "zxAnEponOnuOamAlarmInfo"))
)
if mibBuilder.loadTexts:
    zxAnEponOnuTempHighAlm.setStatus(
        "current"
    )

zxAnEponOnuTempHighAlmRestore = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 10, 4, 2, 16)
)
zxAnEponOnuTempHighAlmRestore.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ZXEPON-TRAP-MIB", "zxAnEponOnuOamTimeStamp"),
        ("ZXEPON-TRAP-MIB", "zxAnEponOnuOamAlarmInfo"))
)
if mibBuilder.loadTexts:
    zxAnEponOnuTempHighAlmRestore.setStatus(
        "current"
    )

zxAnEponOnuTempLowAlm = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 10, 4, 2, 17)
)
zxAnEponOnuTempLowAlm.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ZXEPON-TRAP-MIB", "zxAnEponOnuOamTimeStamp"),
        ("ZXEPON-TRAP-MIB", "zxAnEponOnuOamAlarmInfo"))
)
if mibBuilder.loadTexts:
    zxAnEponOnuTempLowAlm.setStatus(
        "current"
    )

zxAnEponOnuTempLowAlmRestore = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 10, 4, 2, 18)
)
zxAnEponOnuTempLowAlmRestore.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ZXEPON-TRAP-MIB", "zxAnEponOnuOamTimeStamp"),
        ("ZXEPON-TRAP-MIB", "zxAnEponOnuOamAlarmInfo"))
)
if mibBuilder.loadTexts:
    zxAnEponOnuTempLowAlmRestore.setStatus(
        "current"
    )

zxAnEponOnuIADConnectionFailureAlm = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 10, 4, 2, 19)
)
zxAnEponOnuIADConnectionFailureAlm.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ZXEPON-TRAP-MIB", "zxAnEponOnuOamTimeStamp"),
        ("ZXEPON-TRAP-MIB", "zxAnEponOnuOamAlarmInfo"))
)
if mibBuilder.loadTexts:
    zxAnEponOnuIADConnectionFailureAlm.setStatus(
        "current"
    )

zxAnEponOnuIADConnectionFailureRestore = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 10, 4, 2, 20)
)
zxAnEponOnuIADConnectionFailureRestore.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ZXEPON-TRAP-MIB", "zxAnEponOnuOamTimeStamp"),
        ("ZXEPON-TRAP-MIB", "zxAnEponOnuOamAlarmInfo"))
)
if mibBuilder.loadTexts:
    zxAnEponOnuIADConnectionFailureRestore.setStatus(
        "current"
    )

zxAnEponOnuPonSwitchAlm = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 10, 4, 2, 21)
)
zxAnEponOnuPonSwitchAlm.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ZXEPON-TRAP-MIB", "zxAnEponOnuOamTimeStamp"),
        ("ZXEPON-TRAP-MIB", "zxAnEponOnuOamAlarmInfo"))
)
if mibBuilder.loadTexts:
    zxAnEponOnuPonSwitchAlm.setStatus(
        "current"
    )

zxAnEponOnuPonSwitchRestore = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 10, 4, 2, 22)
)
zxAnEponOnuPonSwitchRestore.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ZXEPON-TRAP-MIB", "zxAnEponOnuOamTimeStamp"),
        ("ZXEPON-TRAP-MIB", "zxAnEponOnuOamAlarmInfo"))
)
if mibBuilder.loadTexts:
    zxAnEponOnuPonSwitchRestore.setStatus(
        "current"
    )

zxAnEponOnuResetNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 10, 4, 2, 23)
)
zxAnEponOnuResetNotification.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ZXEPON-TRAP-MIB", "zxAnEponOnuActionResult"))
)
if mibBuilder.loadTexts:
    zxAnEponOnuResetNotification.setStatus(
        "current"
    )

zxAnEponOnuRecoveryNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 10, 4, 2, 24)
)
zxAnEponOnuRecoveryNotification.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ZXEPON-TRAP-MIB", "zxAnEponOnuActionResult"))
)
if mibBuilder.loadTexts:
    zxAnEponOnuRecoveryNotification.setStatus(
        "current"
    )

zxAnEponOnuDataChannelTurnOffNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 10, 4, 2, 25)
)
zxAnEponOnuDataChannelTurnOffNotification.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ZXEPON-TRAP-MIB", "zxAnEponOnuActionResult"),
        ("ZXEPON-TRAP-MIB", "zxAnEponOnuDataChannelLinkStatus"))
)
if mibBuilder.loadTexts:
    zxAnEponOnuDataChannelTurnOffNotification.setStatus(
        "current"
    )

zxAnEponOnuLuminousEmissionOffNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 10, 4, 2, 26)
)
zxAnEponOnuLuminousEmissionOffNotification.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ZXEPON-TRAP-MIB", "zxAnEponOnuActionResult"),
        ("ZXEPON-TRAP-MIB", "zxAnEponOnuLuminousEmissionStatus"))
)
if mibBuilder.loadTexts:
    zxAnEponOnuLuminousEmissionOffNotification.setStatus(
        "current"
    )

zxAnEponOnuFirmwareVersionUpdateNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 10, 4, 2, 27)
)
zxAnEponOnuFirmwareVersionUpdateNotification.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ZXEPON-TRAP-MIB", "zxAnEponOnuVersionUpdateStatus"))
)
if mibBuilder.loadTexts:
    zxAnEponOnuFirmwareVersionUpdateNotification.setStatus(
        "current"
    )

zxAnEponOnuFirmwareVersionUpdateFailedNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 10, 4, 2, 28)
)
zxAnEponOnuFirmwareVersionUpdateFailedNotification.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ZXEPON-TRAP-MIB", "zxAnEponOnuVersionUpdateFailedReason"))
)
if mibBuilder.loadTexts:
    zxAnEponOnuFirmwareVersionUpdateFailedNotification.setStatus(
        "current"
    )

zxAnEponOnuPowerSwitchAlm = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 10, 4, 2, 29)
)
zxAnEponOnuPowerSwitchAlm.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ZXEPON-TRAP-MIB", "zxAnEponOnuOamAlarmInfo"),
        ("ZXEPON-TRAP-MIB", "zxAnEponOnuOamTimeStamp"))
)
if mibBuilder.loadTexts:
    zxAnEponOnuPowerSwitchAlm.setStatus(
        "current"
    )

zxAnEponOnuPowerSwitchRestore = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 10, 4, 2, 30)
)
zxAnEponOnuPowerSwitchRestore.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ZXEPON-TRAP-MIB", "zxAnEponOnuOamAlarmInfo"),
        ("ZXEPON-TRAP-MIB", "zxAnEponOnuOamTimeStamp"))
)
if mibBuilder.loadTexts:
    zxAnEponOnuPowerSwitchRestore.setStatus(
        "current"
    )

zxAnEponOnuPonRxPowerHighAlm = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 10, 4, 3, 1)
)
zxAnEponOnuPonRxPowerHighAlm.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ZXEPON-TRAP-MIB", "zxAnEponOnuOamInstanceNum"),
        ("ZXEPON-TRAP-MIB", "zxAnEponOnuOamTimeStamp"),
        ("ZXEPON-TRAP-MIB", "zxAnEponOnuOamAlarmInfo"))
)
if mibBuilder.loadTexts:
    zxAnEponOnuPonRxPowerHighAlm.setStatus(
        "current"
    )

zxAnEponOnuPonRxPowerHighAlmRestore = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 10, 4, 3, 2)
)
zxAnEponOnuPonRxPowerHighAlmRestore.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ZXEPON-TRAP-MIB", "zxAnEponOnuOamInstanceNum"),
        ("ZXEPON-TRAP-MIB", "zxAnEponOnuOamTimeStamp"),
        ("ZXEPON-TRAP-MIB", "zxAnEponOnuOamAlarmInfo"))
)
if mibBuilder.loadTexts:
    zxAnEponOnuPonRxPowerHighAlmRestore.setStatus(
        "current"
    )

zxAnEponOnuPonRxPowerLowAlm = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 10, 4, 3, 3)
)
zxAnEponOnuPonRxPowerLowAlm.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ZXEPON-TRAP-MIB", "zxAnEponOnuOamInstanceNum"),
        ("ZXEPON-TRAP-MIB", "zxAnEponOnuOamTimeStamp"),
        ("ZXEPON-TRAP-MIB", "zxAnEponOnuOamAlarmInfo"))
)
if mibBuilder.loadTexts:
    zxAnEponOnuPonRxPowerLowAlm.setStatus(
        "current"
    )

zxAnEponOnuPonRxPowerLowAlmRestore = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 10, 4, 3, 4)
)
zxAnEponOnuPonRxPowerLowAlmRestore.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ZXEPON-TRAP-MIB", "zxAnEponOnuOamInstanceNum"),
        ("ZXEPON-TRAP-MIB", "zxAnEponOnuOamTimeStamp"),
        ("ZXEPON-TRAP-MIB", "zxAnEponOnuOamAlarmInfo"))
)
if mibBuilder.loadTexts:
    zxAnEponOnuPonRxPowerLowAlmRestore.setStatus(
        "current"
    )

zxAnEponOnuPonTxPowerHighAlm = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 10, 4, 3, 5)
)
zxAnEponOnuPonTxPowerHighAlm.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ZXEPON-TRAP-MIB", "zxAnEponOnuOamInstanceNum"),
        ("ZXEPON-TRAP-MIB", "zxAnEponOnuOamTimeStamp"),
        ("ZXEPON-TRAP-MIB", "zxAnEponOnuOamAlarmInfo"))
)
if mibBuilder.loadTexts:
    zxAnEponOnuPonTxPowerHighAlm.setStatus(
        "current"
    )

zxAnEponOnuPonTxPowerHighAlmRestore = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 10, 4, 3, 6)
)
zxAnEponOnuPonTxPowerHighAlmRestore.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ZXEPON-TRAP-MIB", "zxAnEponOnuOamInstanceNum"),
        ("ZXEPON-TRAP-MIB", "zxAnEponOnuOamTimeStamp"),
        ("ZXEPON-TRAP-MIB", "zxAnEponOnuOamAlarmInfo"))
)
if mibBuilder.loadTexts:
    zxAnEponOnuPonTxPowerHighAlmRestore.setStatus(
        "current"
    )

zxAnEponOnuPonTxPowerLowAlm = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 10, 4, 3, 7)
)
zxAnEponOnuPonTxPowerLowAlm.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ZXEPON-TRAP-MIB", "zxAnEponOnuOamInstanceNum"),
        ("ZXEPON-TRAP-MIB", "zxAnEponOnuOamTimeStamp"),
        ("ZXEPON-TRAP-MIB", "zxAnEponOnuOamAlarmInfo"))
)
if mibBuilder.loadTexts:
    zxAnEponOnuPonTxPowerLowAlm.setStatus(
        "current"
    )

zxAnEponOnuPonTxPowerLowAlmRestore = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 10, 4, 3, 8)
)
zxAnEponOnuPonTxPowerLowAlmRestore.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ZXEPON-TRAP-MIB", "zxAnEponOnuOamInstanceNum"),
        ("ZXEPON-TRAP-MIB", "zxAnEponOnuOamTimeStamp"),
        ("ZXEPON-TRAP-MIB", "zxAnEponOnuOamAlarmInfo"))
)
if mibBuilder.loadTexts:
    zxAnEponOnuPonTxPowerLowAlmRestore.setStatus(
        "current"
    )

zxAnEponOnuPonTxBiasHighAlm = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 10, 4, 3, 9)
)
zxAnEponOnuPonTxBiasHighAlm.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ZXEPON-TRAP-MIB", "zxAnEponOnuOamInstanceNum"),
        ("ZXEPON-TRAP-MIB", "zxAnEponOnuOamTimeStamp"),
        ("ZXEPON-TRAP-MIB", "zxAnEponOnuOamAlarmInfo"))
)
if mibBuilder.loadTexts:
    zxAnEponOnuPonTxBiasHighAlm.setStatus(
        "current"
    )

zxAnEponOnuPonTxBiasHighAlmRestore = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 10, 4, 3, 10)
)
zxAnEponOnuPonTxBiasHighAlmRestore.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ZXEPON-TRAP-MIB", "zxAnEponOnuOamInstanceNum"),
        ("ZXEPON-TRAP-MIB", "zxAnEponOnuOamTimeStamp"),
        ("ZXEPON-TRAP-MIB", "zxAnEponOnuOamAlarmInfo"))
)
if mibBuilder.loadTexts:
    zxAnEponOnuPonTxBiasHighAlmRestore.setStatus(
        "current"
    )

zxAnEponOnuPonTxBiasLowAlm = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 10, 4, 3, 11)
)
zxAnEponOnuPonTxBiasLowAlm.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ZXEPON-TRAP-MIB", "zxAnEponOnuOamInstanceNum"),
        ("ZXEPON-TRAP-MIB", "zxAnEponOnuOamTimeStamp"),
        ("ZXEPON-TRAP-MIB", "zxAnEponOnuOamAlarmInfo"))
)
if mibBuilder.loadTexts:
    zxAnEponOnuPonTxBiasLowAlm.setStatus(
        "current"
    )

zxAnEponOnuPonTxBiasLowAlmRestore = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 10, 4, 3, 12)
)
zxAnEponOnuPonTxBiasLowAlmRestore.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ZXEPON-TRAP-MIB", "zxAnEponOnuOamInstanceNum"),
        ("ZXEPON-TRAP-MIB", "zxAnEponOnuOamTimeStamp"),
        ("ZXEPON-TRAP-MIB", "zxAnEponOnuOamAlarmInfo"))
)
if mibBuilder.loadTexts:
    zxAnEponOnuPonTxBiasLowAlmRestore.setStatus(
        "current"
    )

zxAnEponPonOnuVccHighAlm = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 10, 4, 3, 13)
)
zxAnEponPonOnuVccHighAlm.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ZXEPON-TRAP-MIB", "zxAnEponOnuOamInstanceNum"),
        ("ZXEPON-TRAP-MIB", "zxAnEponOnuOamTimeStamp"),
        ("ZXEPON-TRAP-MIB", "zxAnEponOnuOamAlarmInfo"))
)
if mibBuilder.loadTexts:
    zxAnEponPonOnuVccHighAlm.setStatus(
        "current"
    )

zxAnEponPonOnuVccHighAlmRestore = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 10, 4, 3, 14)
)
zxAnEponPonOnuVccHighAlmRestore.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ZXEPON-TRAP-MIB", "zxAnEponOnuOamInstanceNum"),
        ("ZXEPON-TRAP-MIB", "zxAnEponOnuOamTimeStamp"),
        ("ZXEPON-TRAP-MIB", "zxAnEponOnuOamAlarmInfo"))
)
if mibBuilder.loadTexts:
    zxAnEponPonOnuVccHighAlmRestore.setStatus(
        "current"
    )

zxAnEponPonOnuVccLowAlm = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 10, 4, 3, 15)
)
zxAnEponPonOnuVccLowAlm.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ZXEPON-TRAP-MIB", "zxAnEponOnuOamInstanceNum"),
        ("ZXEPON-TRAP-MIB", "zxAnEponOnuOamTimeStamp"),
        ("ZXEPON-TRAP-MIB", "zxAnEponOnuOamAlarmInfo"))
)
if mibBuilder.loadTexts:
    zxAnEponPonOnuVccLowAlm.setStatus(
        "current"
    )

zxAnEponPonOnuVccLowAlmRestore = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 10, 4, 3, 16)
)
zxAnEponPonOnuVccLowAlmRestore.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ZXEPON-TRAP-MIB", "zxAnEponOnuOamInstanceNum"),
        ("ZXEPON-TRAP-MIB", "zxAnEponOnuOamTimeStamp"),
        ("ZXEPON-TRAP-MIB", "zxAnEponOnuOamAlarmInfo"))
)
if mibBuilder.loadTexts:
    zxAnEponPonOnuVccLowAlmRestore.setStatus(
        "current"
    )

zxAnEponOnuPonTempHighAlm = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 10, 4, 3, 17)
)
zxAnEponOnuPonTempHighAlm.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ZXEPON-TRAP-MIB", "zxAnEponOnuOamInstanceNum"),
        ("ZXEPON-TRAP-MIB", "zxAnEponOnuOamTimeStamp"),
        ("ZXEPON-TRAP-MIB", "zxAnEponOnuOamAlarmInfo"))
)
if mibBuilder.loadTexts:
    zxAnEponOnuPonTempHighAlm.setStatus(
        "current"
    )

zxAnEponOnuPonTempHighAlmRestore = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 10, 4, 3, 18)
)
zxAnEponOnuPonTempHighAlmRestore.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ZXEPON-TRAP-MIB", "zxAnEponOnuOamInstanceNum"),
        ("ZXEPON-TRAP-MIB", "zxAnEponOnuOamTimeStamp"),
        ("ZXEPON-TRAP-MIB", "zxAnEponOnuOamAlarmInfo"))
)
if mibBuilder.loadTexts:
    zxAnEponOnuPonTempHighAlmRestore.setStatus(
        "current"
    )

zxAnEponOnuPonTempLowAlm = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 10, 4, 3, 19)
)
zxAnEponOnuPonTempLowAlm.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ZXEPON-TRAP-MIB", "zxAnEponOnuOamInstanceNum"),
        ("ZXEPON-TRAP-MIB", "zxAnEponOnuOamTimeStamp"),
        ("ZXEPON-TRAP-MIB", "zxAnEponOnuOamAlarmInfo"))
)
if mibBuilder.loadTexts:
    zxAnEponOnuPonTempLowAlm.setStatus(
        "current"
    )

zxAnEponOnuPonTempLowAlmRestore = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 10, 4, 3, 20)
)
zxAnEponOnuPonTempLowAlmRestore.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ZXEPON-TRAP-MIB", "zxAnEponOnuOamInstanceNum"),
        ("ZXEPON-TRAP-MIB", "zxAnEponOnuOamTimeStamp"),
        ("ZXEPON-TRAP-MIB", "zxAnEponOnuOamAlarmInfo"))
)
if mibBuilder.loadTexts:
    zxAnEponOnuPonTempLowAlmRestore.setStatus(
        "current"
    )

zxAnEponOnuCardAlm = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 10, 4, 4, 1)
)
zxAnEponOnuCardAlm.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ZXEPON-TRAP-MIB", "zxAnEponOnuOamInstanceNum"),
        ("ZXEPON-TRAP-MIB", "zxAnEponOnuOamTimeStamp"),
        ("ZXEPON-TRAP-MIB", "zxAnEponOnuOamAlarmInfo"))
)
if mibBuilder.loadTexts:
    zxAnEponOnuCardAlm.setStatus(
        "current"
    )

zxAnEponOnuCardRestore = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 10, 4, 4, 2)
)
zxAnEponOnuCardRestore.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ZXEPON-TRAP-MIB", "zxAnEponOnuOamInstanceNum"),
        ("ZXEPON-TRAP-MIB", "zxAnEponOnuOamTimeStamp"),
        ("ZXEPON-TRAP-MIB", "zxAnEponOnuOamAlarmInfo"))
)
if mibBuilder.loadTexts:
    zxAnEponOnuCardRestore.setStatus(
        "current"
    )

zxAnEponOnuCardTestFailureAlm = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 10, 4, 4, 3)
)
zxAnEponOnuCardTestFailureAlm.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ZXEPON-TRAP-MIB", "zxAnEponOnuOamInstanceNum"),
        ("ZXEPON-TRAP-MIB", "zxAnEponOnuOamTimeStamp"),
        ("ZXEPON-TRAP-MIB", "zxAnEponOnuOamAlarmInfo"))
)
if mibBuilder.loadTexts:
    zxAnEponOnuCardTestFailureAlm.setStatus(
        "current"
    )

zxAnEponOnuCardTestFailureRestore = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 10, 4, 4, 4)
)
zxAnEponOnuCardTestFailureRestore.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ZXEPON-TRAP-MIB", "zxAnEponOnuOamInstanceNum"),
        ("ZXEPON-TRAP-MIB", "zxAnEponOnuOamTimeStamp"),
        ("ZXEPON-TRAP-MIB", "zxAnEponOnuOamAlarmInfo"))
)
if mibBuilder.loadTexts:
    zxAnEponOnuCardTestFailureRestore.setStatus(
        "current"
    )

zxAnEponOnuEthAutoNegFailureAlm = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 10, 4, 5, 1)
)
zxAnEponOnuEthAutoNegFailureAlm.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ZXEPON-TRAP-MIB", "zxAnEponOnuOamInstanceNum"),
        ("ZXEPON-TRAP-MIB", "zxAnEponOnuOamTimeStamp"))
)
if mibBuilder.loadTexts:
    zxAnEponOnuEthAutoNegFailureAlm.setStatus(
        "current"
    )

zxAnEponOnuEthAutoNegFailureRestore = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 10, 4, 5, 2)
)
zxAnEponOnuEthAutoNegFailureRestore.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ZXEPON-TRAP-MIB", "zxAnEponOnuOamInstanceNum"),
        ("ZXEPON-TRAP-MIB", "zxAnEponOnuOamTimeStamp"))
)
if mibBuilder.loadTexts:
    zxAnEponOnuEthAutoNegFailureRestore.setStatus(
        "current"
    )

zxAnEponOnuEthLOSAlm = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 10, 4, 5, 3)
)
zxAnEponOnuEthLOSAlm.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ZXEPON-TRAP-MIB", "zxAnEponOnuOamInstanceNum"),
        ("ZXEPON-TRAP-MIB", "zxAnEponOnuOamTimeStamp"))
)
if mibBuilder.loadTexts:
    zxAnEponOnuEthLOSAlm.setStatus(
        "current"
    )

zxAnEponOnuEthLOSRestore = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 10, 4, 5, 4)
)
zxAnEponOnuEthLOSRestore.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ZXEPON-TRAP-MIB", "zxAnEponOnuOamInstanceNum"),
        ("ZXEPON-TRAP-MIB", "zxAnEponOnuOamTimeStamp"))
)
if mibBuilder.loadTexts:
    zxAnEponOnuEthLOSRestore.setStatus(
        "current"
    )

zxAnEponOnuEthFailureAlm = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 10, 4, 5, 5)
)
zxAnEponOnuEthFailureAlm.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ZXEPON-TRAP-MIB", "zxAnEponOnuOamInstanceNum"),
        ("ZXEPON-TRAP-MIB", "zxAnEponOnuOamTimeStamp"))
)
if mibBuilder.loadTexts:
    zxAnEponOnuEthFailureAlm.setStatus(
        "current"
    )

zxAnEponOnuEthFailureRestore = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 10, 4, 5, 6)
)
zxAnEponOnuEthFailureRestore.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ZXEPON-TRAP-MIB", "zxAnEponOnuOamInstanceNum"),
        ("ZXEPON-TRAP-MIB", "zxAnEponOnuOamTimeStamp"))
)
if mibBuilder.loadTexts:
    zxAnEponOnuEthFailureRestore.setStatus(
        "current"
    )

zxAnEponOnuEthLoopbackAlm = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 10, 4, 5, 7)
)
zxAnEponOnuEthLoopbackAlm.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ZXEPON-TRAP-MIB", "zxAnEponOnuOamInstanceNum"),
        ("ZXEPON-TRAP-MIB", "zxAnEponOnuOamTimeStamp"),
        ("ZXEPON-TRAP-MIB", "zxAnEponOnuOamAlarmInfo"))
)
if mibBuilder.loadTexts:
    zxAnEponOnuEthLoopbackAlm.setStatus(
        "current"
    )

zxAnEponOnuEthLoopbackRestore = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 10, 4, 5, 8)
)
zxAnEponOnuEthLoopbackRestore.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ZXEPON-TRAP-MIB", "zxAnEponOnuOamInstanceNum"),
        ("ZXEPON-TRAP-MIB", "zxAnEponOnuOamTimeStamp"),
        ("ZXEPON-TRAP-MIB", "zxAnEponOnuOamAlarmInfo"))
)
if mibBuilder.loadTexts:
    zxAnEponOnuEthLoopbackRestore.setStatus(
        "current"
    )

zxAnEponOnuEthCongestionAlm = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 10, 4, 5, 9)
)
zxAnEponOnuEthCongestionAlm.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ZXEPON-TRAP-MIB", "zxAnEponOnuOamInstanceNum"),
        ("ZXEPON-TRAP-MIB", "zxAnEponOnuOamTimeStamp"))
)
if mibBuilder.loadTexts:
    zxAnEponOnuEthCongestionAlm.setStatus(
        "current"
    )

zxAnEponOnuEthCongestionRestore = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 10, 4, 5, 10)
)
zxAnEponOnuEthCongestionRestore.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ZXEPON-TRAP-MIB", "zxAnEponOnuOamInstanceNum"),
        ("ZXEPON-TRAP-MIB", "zxAnEponOnuOamTimeStamp"))
)
if mibBuilder.loadTexts:
    zxAnEponOnuEthCongestionRestore.setStatus(
        "current"
    )

zxAnEponOnuPOTSFailureAlm = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 10, 4, 5, 11)
)
zxAnEponOnuPOTSFailureAlm.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ZXEPON-TRAP-MIB", "zxAnEponOnuOamInstanceNum"),
        ("ZXEPON-TRAP-MIB", "zxAnEponOnuOamTimeStamp"),
        ("ZXEPON-TRAP-MIB", "zxAnEponOnuOamAlarmInfo"))
)
if mibBuilder.loadTexts:
    zxAnEponOnuPOTSFailureAlm.setStatus(
        "current"
    )

zxAnEponOnuPOTSFailureRestore = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 10, 4, 5, 12)
)
zxAnEponOnuPOTSFailureRestore.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ZXEPON-TRAP-MIB", "zxAnEponOnuOamInstanceNum"),
        ("ZXEPON-TRAP-MIB", "zxAnEponOnuOamTimeStamp"),
        ("ZXEPON-TRAP-MIB", "zxAnEponOnuOamAlarmInfo"))
)
if mibBuilder.loadTexts:
    zxAnEponOnuPOTSFailureRestore.setStatus(
        "current"
    )

zxAnEponOnuE1FailureAlm = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 10, 4, 5, 13)
)
zxAnEponOnuE1FailureAlm.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ZXEPON-TRAP-MIB", "zxAnEponOnuOamInstanceNum"),
        ("ZXEPON-TRAP-MIB", "zxAnEponOnuOamTimeStamp"),
        ("ZXEPON-TRAP-MIB", "zxAnEponOnuOamAlarmInfo"))
)
if mibBuilder.loadTexts:
    zxAnEponOnuE1FailureAlm.setStatus(
        "current"
    )

zxAnEponOnuE1FailureRestore = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 10, 4, 5, 14)
)
zxAnEponOnuE1FailureRestore.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ZXEPON-TRAP-MIB", "zxAnEponOnuOamInstanceNum"),
        ("ZXEPON-TRAP-MIB", "zxAnEponOnuOamTimeStamp"),
        ("ZXEPON-TRAP-MIB", "zxAnEponOnuOamAlarmInfo"))
)
if mibBuilder.loadTexts:
    zxAnEponOnuE1FailureRestore.setStatus(
        "current"
    )

zxAnEponOnuE1TimingLockAlm = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 10, 4, 5, 15)
)
zxAnEponOnuE1TimingLockAlm.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ZXEPON-TRAP-MIB", "zxAnEponOnuOamInstanceNum"),
        ("ZXEPON-TRAP-MIB", "zxAnEponOnuOamTimeStamp"))
)
if mibBuilder.loadTexts:
    zxAnEponOnuE1TimingLockAlm.setStatus(
        "current"
    )

zxAnEponOnuE1TimingLockRestore = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 10, 4, 5, 16)
)
zxAnEponOnuE1TimingLockRestore.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ZXEPON-TRAP-MIB", "zxAnEponOnuOamInstanceNum"),
        ("ZXEPON-TRAP-MIB", "zxAnEponOnuOamTimeStamp"))
)
if mibBuilder.loadTexts:
    zxAnEponOnuE1TimingLockRestore.setStatus(
        "current"
    )

zxAnEponOnuE1LosAlm = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 10, 4, 5, 17)
)
zxAnEponOnuE1LosAlm.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ZXEPON-TRAP-MIB", "zxAnEponOnuOamInstanceNum"),
        ("ZXEPON-TRAP-MIB", "zxAnEponOnuOamTimeStamp"))
)
if mibBuilder.loadTexts:
    zxAnEponOnuE1LosAlm.setStatus(
        "current"
    )

zxAnEponOnuE1LosRestore = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 10, 4, 5, 18)
)
zxAnEponOnuE1LosRestore.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ZXEPON-TRAP-MIB", "zxAnEponOnuOamInstanceNum"),
        ("ZXEPON-TRAP-MIB", "zxAnEponOnuOamTimeStamp"))
)
if mibBuilder.loadTexts:
    zxAnEponOnuE1LosRestore.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZXEPON-TRAP-MIB",
    **{"zxAnEponTrap": zxAnEponTrap,
       "zxAnEponTrapOlt": zxAnEponTrapOlt,
       "zxAnEponOnuBerOverThreshold": zxAnEponOnuBerOverThreshold,
       "zxAnEponOnuBerOverThresholdRestore": zxAnEponOnuBerOverThresholdRestore,
       "zxAnEponDeviceOltPortBerState": zxAnEponDeviceOltPortBerState,
       "zxAnEponDeviceOltPortBerStateRestore": zxAnEponDeviceOltPortBerStateRestore,
       "zxAnEponPonLOS": zxAnEponPonLOS,
       "zxAnEponPonLOSRestore": zxAnEponPonLOSRestore,
       "zxAnEponOnuOffLine": zxAnEponOnuOffLine,
       "zxAnEponOnuOffLineRestore": zxAnEponOnuOffLineRestore,
       "zxAnEponOnuErroredSymbolPeriodEvent": zxAnEponOnuErroredSymbolPeriodEvent,
       "zxAnEponOnuErroredSymbolPeriodEventRestore": zxAnEponOnuErroredSymbolPeriodEventRestore,
       "zxAnEponOnuErroredFrameEvent": zxAnEponOnuErroredFrameEvent,
       "zxAnEponOnuErroredFrameEventRestore": zxAnEponOnuErroredFrameEventRestore,
       "zxAnEponOnuErroredFramePeriodEvent": zxAnEponOnuErroredFramePeriodEvent,
       "zxAnEponOnuErroredFramePeriodEventRestore": zxAnEponOnuErroredFramePeriodEventRestore,
       "zxAnEponOnuErroredFrameSecondsSummaryEvent": zxAnEponOnuErroredFrameSecondsSummaryEvent,
       "zxAnEponOnuErroredFrameSecondsSummaryEventRestore": zxAnEponOnuErroredFrameSecondsSummaryEventRestore,
       "zxAnEponOnuUplinkBitError": zxAnEponOnuUplinkBitError,
       "zxAnEponOnuUplinkBitErrorRestore": zxAnEponOnuUplinkBitErrorRestore,
       "zxAnEponOnuUplinkFrameError": zxAnEponOnuUplinkFrameError,
       "zxAnEponOnuUplinkFrameErrorRestore": zxAnEponOnuUplinkFrameErrorRestore,
       "zxAnEponOnuAuthSuccMsg": zxAnEponOnuAuthSuccMsg,
       "zxAnEponPonOpticalTransceiverLos": zxAnEponPonOpticalTransceiverLos,
       "zxAnEponPonOpticalTransceiverLosRestore": zxAnEponPonOpticalTransceiverLosRestore,
       "zxAnEponLoidConflict": zxAnEponLoidConflict,
       "zxAnEponTrapBindVar": zxAnEponTrapBindVar,
       "zxAnEponTrapDid": zxAnEponTrapDid,
       "zxAnEponTrapMac": zxAnEponTrapMac,
       "zxAnEponTrapIp": zxAnEponTrapIp,
       "zxAnEponTrapMask": zxAnEponTrapMask,
       "zxAnEponTrapOnuType": zxAnEponTrapOnuType,
       "zxAnEponTrapOnuName": zxAnEponTrapOnuName,
       "zxAnEponTrapPonLosReason": zxAnEponTrapPonLosReason,
       "zxAnEponTrapOnuOffLineReason": zxAnEponTrapOnuOffLineReason,
       "zxAnEponTrapOltPortName": zxAnEponTrapOltPortName,
       "zxAnEponTrapOnuModel": zxAnEponTrapOnuModel,
       "zxAnEponTrapOnuDesc": zxAnEponTrapOnuDesc,
       "zxAnEponTrapTime": zxAnEponTrapTime,
       "zxAnEponRogueOnuIdList": zxAnEponRogueOnuIdList,
       "zxAnEponHighProbabilityRogueOnuIdList": zxAnEponHighProbabilityRogueOnuIdList,
       "zxAnEponLowProbabilityRogueOnuIdList": zxAnEponLowProbabilityRogueOnuIdList,
       "zxAnEponRogueUnauthOnuList": zxAnEponRogueUnauthOnuList,
       "zxAnEponHighPossibilityRogueUnauthOnuList": zxAnEponHighPossibilityRogueUnauthOnuList,
       "zxAnEponLowPossibilityRogueUnauthOnuList": zxAnEponLowPossibilityRogueUnauthOnuList,
       "zxAnEponOnuActualSpeedType": zxAnEponOnuActualSpeedType,
       "zxAnEponOnuConfigSpeedType": zxAnEponOnuConfigSpeedType,
       "zxAnEponOnuIfIndex": zxAnEponOnuIfIndex,
       "zxAnEponTrapEvent": zxAnEponTrapEvent,
       "zxAnEponTrapEventString": zxAnEponTrapEventString,
       "zxAnEponTrapEventOltReset": zxAnEponTrapEventOltReset,
       "zxAnEponTrapEventOnuOffline": zxAnEponTrapEventOnuOffline,
       "zxAnEponTrapEventOnuOnline": zxAnEponTrapEventOnuOnline,
       "zxAnEponTrapEventExtendedOamDiscoveryFail": zxAnEponTrapEventExtendedOamDiscoveryFail,
       "zxAnEponTrapEventLocalOnuConfigureFail": zxAnEponTrapEventLocalOnuConfigureFail,
       "zxAnEponTrapEventUnkownOnuOffline": zxAnEponTrapEventUnkownOnuOffline,
       "zxAnEponTrapEventDenyUnkownOnuRegister": zxAnEponTrapEventDenyUnkownOnuRegister,
       "zxAnEponTrapEventUnkownOnuOnline": zxAnEponTrapEventUnkownOnuOnline,
       "zxAnEponTrapEventRemoteOnuConfigureFail": zxAnEponTrapEventRemoteOnuConfigureFail,
       "zxAnEponTrapEventTransparent": zxAnEponTrapEventTransparent,
       "zxAnEponTrapEventOnuDyingGasp": zxAnEponTrapEventOnuDyingGasp,
       "zxAnEponTrapEventOnuAutoConfigRequest": zxAnEponTrapEventOnuAutoConfigRequest,
       "zxAnEponTrapEventOnuIpNotAutoConfig": zxAnEponTrapEventOnuIpNotAutoConfig,
       "zxAnEponTrapEventOnuPowerOff": zxAnEponTrapEventOnuPowerOff,
       "zxAnEponTrapEventOnuPowerOffRestore": zxAnEponTrapEventOnuPowerOffRestore,
       "zxAnEponTrapEventOnuUnauthenticate": zxAnEponTrapEventOnuUnauthenticate,
       "zxAnEponTrapEventOnuConstantOptical": zxAnEponTrapEventOnuConstantOptical,
       "zxAnEponTrapEventOnuConstantOpticalRestore": zxAnEponTrapEventOnuConstantOpticalRestore,
       "zxAnEponTrapEventPonResetFailed": zxAnEponTrapEventPonResetFailed,
       "zxAnEponOnuSpeedTypeMismatchTrap": zxAnEponOnuSpeedTypeMismatchTrap,
       "zxAnEponTrapOnu": zxAnEponTrapOnu,
       "zxAnEponOnuTrapInfo": zxAnEponOnuTrapInfo,
       "zxAnEponOnuOamObjType": zxAnEponOnuOamObjType,
       "zxAnEponOnuOamInstanceNum": zxAnEponOnuOamInstanceNum,
       "zxAnEponOnuOamAlarmId": zxAnEponOnuOamAlarmId,
       "zxAnEponOnuOamTimeStamp": zxAnEponOnuOamTimeStamp,
       "zxAnEponOnuOamAlarmState": zxAnEponOnuOamAlarmState,
       "zxAnEponOnuOamAlarmInfo": zxAnEponOnuOamAlarmInfo,
       "zxAnEponOnuActionResult": zxAnEponOnuActionResult,
       "zxAnEponOnuLuminousEmissionStatus": zxAnEponOnuLuminousEmissionStatus,
       "zxAnEponOnuDataChannelLinkStatus": zxAnEponOnuDataChannelLinkStatus,
       "zxAnEponOnuFirmwareVersionUpdateStatus": zxAnEponOnuFirmwareVersionUpdateStatus,
       "zxAnEponOnuFirmwareVersionUpdateFailedReason": zxAnEponOnuFirmwareVersionUpdateFailedReason,
       "zxAnEponOnuOamV21Message": zxAnEponOnuOamV21Message,
       "zxAnEponOnuBaseTrap": zxAnEponOnuBaseTrap,
       "zxAnEponOnuEquipmentAlm": zxAnEponOnuEquipmentAlm,
       "zxAnEponOnuEquipmentRestore": zxAnEponOnuEquipmentRestore,
       "zxAnEponOnuPowerAlm": zxAnEponOnuPowerAlm,
       "zxAnEponOnuPowerRestore": zxAnEponOnuPowerRestore,
       "zxAnEponOnuButteryMissingAlm": zxAnEponOnuButteryMissingAlm,
       "zxAnEponOnuButteryMissingRestore": zxAnEponOnuButteryMissingRestore,
       "zxAnEponOnuButteryFailureAlm": zxAnEponOnuButteryFailureAlm,
       "zxAnEponOnuButteryFailureRestore": zxAnEponOnuButteryFailureRestore,
       "zxAnEponOnuButteryVoltLowAlm": zxAnEponOnuButteryVoltLowAlm,
       "zxAnEponOnuButteryVoltLowRestore": zxAnEponOnuButteryVoltLowRestore,
       "zxAnEponOnuPhysicalIntrusionAlm": zxAnEponOnuPhysicalIntrusionAlm,
       "zxAnEponOnuPhysicalIntrusionRestore": zxAnEponOnuPhysicalIntrusionRestore,
       "zxAnEponOnuSelfTestFailureAlm": zxAnEponOnuSelfTestFailureAlm,
       "zxAnEponOnuSelfTestFailureRestore": zxAnEponOnuSelfTestFailureRestore,
       "zxAnEponOnuTempHighAlm": zxAnEponOnuTempHighAlm,
       "zxAnEponOnuTempHighAlmRestore": zxAnEponOnuTempHighAlmRestore,
       "zxAnEponOnuTempLowAlm": zxAnEponOnuTempLowAlm,
       "zxAnEponOnuTempLowAlmRestore": zxAnEponOnuTempLowAlmRestore,
       "zxAnEponOnuIADConnectionFailureAlm": zxAnEponOnuIADConnectionFailureAlm,
       "zxAnEponOnuIADConnectionFailureRestore": zxAnEponOnuIADConnectionFailureRestore,
       "zxAnEponOnuPonSwitchAlm": zxAnEponOnuPonSwitchAlm,
       "zxAnEponOnuPonSwitchRestore": zxAnEponOnuPonSwitchRestore,
       "zxAnEponOnuResetNotification": zxAnEponOnuResetNotification,
       "zxAnEponOnuRecoveryNotification": zxAnEponOnuRecoveryNotification,
       "zxAnEponOnuDataChannelTurnOffNotification": zxAnEponOnuDataChannelTurnOffNotification,
       "zxAnEponOnuLuminousEmissionOffNotification": zxAnEponOnuLuminousEmissionOffNotification,
       "zxAnEponOnuFirmwareVersionUpdateNotification": zxAnEponOnuFirmwareVersionUpdateNotification,
       "zxAnEponOnuFirmwareVersionUpdateFailedNotification": zxAnEponOnuFirmwareVersionUpdateFailedNotification,
       "zxAnEponOnuPowerSwitchAlm": zxAnEponOnuPowerSwitchAlm,
       "zxAnEponOnuPowerSwitchRestore": zxAnEponOnuPowerSwitchRestore,
       "zxAnEponOnuPonIfTrap": zxAnEponOnuPonIfTrap,
       "zxAnEponOnuPonRxPowerHighAlm": zxAnEponOnuPonRxPowerHighAlm,
       "zxAnEponOnuPonRxPowerHighAlmRestore": zxAnEponOnuPonRxPowerHighAlmRestore,
       "zxAnEponOnuPonRxPowerLowAlm": zxAnEponOnuPonRxPowerLowAlm,
       "zxAnEponOnuPonRxPowerLowAlmRestore": zxAnEponOnuPonRxPowerLowAlmRestore,
       "zxAnEponOnuPonTxPowerHighAlm": zxAnEponOnuPonTxPowerHighAlm,
       "zxAnEponOnuPonTxPowerHighAlmRestore": zxAnEponOnuPonTxPowerHighAlmRestore,
       "zxAnEponOnuPonTxPowerLowAlm": zxAnEponOnuPonTxPowerLowAlm,
       "zxAnEponOnuPonTxPowerLowAlmRestore": zxAnEponOnuPonTxPowerLowAlmRestore,
       "zxAnEponOnuPonTxBiasHighAlm": zxAnEponOnuPonTxBiasHighAlm,
       "zxAnEponOnuPonTxBiasHighAlmRestore": zxAnEponOnuPonTxBiasHighAlmRestore,
       "zxAnEponOnuPonTxBiasLowAlm": zxAnEponOnuPonTxBiasLowAlm,
       "zxAnEponOnuPonTxBiasLowAlmRestore": zxAnEponOnuPonTxBiasLowAlmRestore,
       "zxAnEponPonOnuVccHighAlm": zxAnEponPonOnuVccHighAlm,
       "zxAnEponPonOnuVccHighAlmRestore": zxAnEponPonOnuVccHighAlmRestore,
       "zxAnEponPonOnuVccLowAlm": zxAnEponPonOnuVccLowAlm,
       "zxAnEponPonOnuVccLowAlmRestore": zxAnEponPonOnuVccLowAlmRestore,
       "zxAnEponOnuPonTempHighAlm": zxAnEponOnuPonTempHighAlm,
       "zxAnEponOnuPonTempHighAlmRestore": zxAnEponOnuPonTempHighAlmRestore,
       "zxAnEponOnuPonTempLowAlm": zxAnEponOnuPonTempLowAlm,
       "zxAnEponOnuPonTempLowAlmRestore": zxAnEponOnuPonTempLowAlmRestore,
       "zxAnEponOnuCardTrap": zxAnEponOnuCardTrap,
       "zxAnEponOnuCardAlm": zxAnEponOnuCardAlm,
       "zxAnEponOnuCardRestore": zxAnEponOnuCardRestore,
       "zxAnEponOnuCardTestFailureAlm": zxAnEponOnuCardTestFailureAlm,
       "zxAnEponOnuCardTestFailureRestore": zxAnEponOnuCardTestFailureRestore,
       "zxAnEponOnuPortTrap": zxAnEponOnuPortTrap,
       "zxAnEponOnuEthAutoNegFailureAlm": zxAnEponOnuEthAutoNegFailureAlm,
       "zxAnEponOnuEthAutoNegFailureRestore": zxAnEponOnuEthAutoNegFailureRestore,
       "zxAnEponOnuEthLOSAlm": zxAnEponOnuEthLOSAlm,
       "zxAnEponOnuEthLOSRestore": zxAnEponOnuEthLOSRestore,
       "zxAnEponOnuEthFailureAlm": zxAnEponOnuEthFailureAlm,
       "zxAnEponOnuEthFailureRestore": zxAnEponOnuEthFailureRestore,
       "zxAnEponOnuEthLoopbackAlm": zxAnEponOnuEthLoopbackAlm,
       "zxAnEponOnuEthLoopbackRestore": zxAnEponOnuEthLoopbackRestore,
       "zxAnEponOnuEthCongestionAlm": zxAnEponOnuEthCongestionAlm,
       "zxAnEponOnuEthCongestionRestore": zxAnEponOnuEthCongestionRestore,
       "zxAnEponOnuPOTSFailureAlm": zxAnEponOnuPOTSFailureAlm,
       "zxAnEponOnuPOTSFailureRestore": zxAnEponOnuPOTSFailureRestore,
       "zxAnEponOnuE1FailureAlm": zxAnEponOnuE1FailureAlm,
       "zxAnEponOnuE1FailureRestore": zxAnEponOnuE1FailureRestore,
       "zxAnEponOnuE1TimingLockAlm": zxAnEponOnuE1TimingLockAlm,
       "zxAnEponOnuE1TimingLockRestore": zxAnEponOnuE1TimingLockRestore,
       "zxAnEponOnuE1LosAlm": zxAnEponOnuE1LosAlm,
       "zxAnEponOnuE1LosRestore": zxAnEponOnuE1LosRestore}
)
